"""P1 -- per-verb census of attempted / executed / refused / null acts on the shipped realm.

Classification copies loop/driver.py:489-505 exactly: an act is REFUSED if any Event it emitted is a
kind in its row's `emits_on_refusal`; EXECUTED if it emitted >=1 Event and none is a refusal kind; NULL
if it emitted nothing. Acts are captured by wrapping the driver INSTANCE's `resolve` and `encounter`
(the same lists the driver classifies). The run composition is harness/storybar.py::drive's.

Also: kind-mismatch -- an attempted act whose subject id resolves to a world record of a kind its
verb's subject class does not name (reported only if the row exposes a subject kind; see code).

Usage (from /home/user/ttrpg): python -m ... not a module; run as
  PYTHONHASHSEED=0 python3 probes/p1_refusal_census.py SEASONS SEED [SEED ...]
"""
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, "/home/user/ttrpg")

from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.state.ids import H, draw_factory
from engine.season.data.verbs import VERB_TABLE, REFUSAL_KINDS
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm

CLOSERS = ["determine", "confer", "covenant", "open_case", "commit", "release", "oblige", "revoke",
           "succeed", "arrest", "issue", "petition", "found", "build", "work", "give", "restore", "tend"]


def run(seed, seasons):
    w = build_realm(seed, None)
    d = SeasonDriver(w)
    captured = []          # (round_acts, events)
    orig_resolve, orig_enc = d.resolve, d.encounter
    state = {"acts": None}

    def resolve(tok, acts, cmd):
        state["acts"] = list(acts)
        ev = orig_resolve(tok, acts, cmd)
        captured.append([list(acts), list(ev)])
        return ev

    def encounter(tok, events, cmd):
        ev = orig_enc(tok, events, cmd)
        captured[-1][1].extend(ev)
        return ev

    d.resolve, d.encounter = resolve, encounter
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(seasons):
        d.season(ch, question=None, subsistence=P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    per = defaultdict(Counter)
    for acts, events in captured:
        emitted = defaultdict(list)
        for e in events:
            a = d.act_of.get(e.id)
            if a is not None:
                emitted[a.id].append(e.kind)
        for a in acts:
            row = VERB_TABLE.get(a.verb)
            ks = emitted.get(a.id, [])
            per[a.verb]["attempted"] += 1
            if not ks:
                per[a.verb]["null"] += 1
            elif any(k in (row.emits_on_refusal or ()) for k in ks):
                per[a.verb]["refused"] += 1
                for k in ks:
                    if k in (row.emits_on_refusal or ()):
                        per[a.verb]["rk:" + k] += 1
            else:
                per[a.verb]["executed"] += 1
    return w, per


def main():
    seasons = int(sys.argv[1])
    seeds = [int(s) for s in sys.argv[2:]]
    out = {"seasons": seasons, "seeds": {}, "pooled": {}}
    pooled = defaultdict(Counter)
    for s in seeds:
        w, per = run(s, seasons)
        tot = Counter()
        for v, c in per.items():
            pooled[v].update(c)
            tot.update({k: c[k] for k in ("attempted", "executed", "refused", "null")})
        out["seeds"][s] = {"log_len": len(w.log), "hash": w.content_hash()[:16], "tick": w.tick,
                           "persons": len(w.persons), **tot}
        print(f"seed={s} seasons={seasons} log={len(w.log)} tick={w.tick} hash={w.content_hash()[:16]} "
              f"attempted={tot['attempted']} executed={tot['executed']} refused={tot['refused']} "
              f"null={tot['null']}", flush=True)
    out["pooled"] = {v: dict(c) for v, c in sorted(pooled.items())}
    T = Counter()
    for c in pooled.values():
        T.update({k: c[k] for k in ("attempted", "executed", "refused", "null")})
    print("POOLED", dict(T))
    print(f"{'verb':14s} {'att':>6s} {'exe':>6s} {'ref':>6s} {'null':>6s}")
    for v in sorted(pooled, key=lambda v: -pooled[v]["attempted"]):
        c = pooled[v]
        print(f"{v:14s} {c['attempted']:6d} {c['executed']:6d} {c['refused']:6d} {c['null']:6d}")
    print("CLOSERS")
    for v in CLOSERS:
        c = pooled.get(v, Counter())
        rks = {k[3:]: n for k, n in c.items() if k.startswith("rk:")}
        print(f"{v:14s} att={c['attempted']} exe={c['executed']} ref={c['refused']} null={c['null']} "
              f"in_table={v in VERB_TABLE} resolvable={v in resolvable_verbs()} refusal_kinds={rks}")
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"p1_out_s{seasons}.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
