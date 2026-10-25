"""P12 -- A14(e): acts that emitted ONLY the fallback kinds `act.ineligible` / `act.refused` (no row's
`emits_on_refusal` names them, so the driver's rule counts such an act EXECUTED). Seed list x seasons.
  PYTHONHASHSEED=0 python3 probes/p12_fallback_kinds.py SEASONS SEED [SEED ...]"""
import sys
from collections import Counter, defaultdict
sys.path.insert(0, "/home/user/ttrpg")
from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.data.verbs import VERB_TABLE, REFUSAL_KINDS
from engine.season.state.ids import H, draw_factory
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm
FALL = {"act.ineligible", "act.refused"}
print("fallback kinds in REFUSAL_KINDS:", sorted(FALL & set(REFUSAL_KINDS)))
seasons = int(sys.argv[1]); T = Counter(); V = Counter()
for seed in map(int, sys.argv[2:]):
    w = build_realm(seed, None); d = SeasonDriver(w); cap = []
    o, oe = d.resolve, d.encounter
    def resolve(tok, acts, cmd, _o=o):
        ev = _o(tok, acts, cmd); cap.append([list(acts), list(ev)]); return ev
    def encounter(tok, events, cmd, _o=oe):
        ev = _o(tok, events, cmd); cap[-1][1].extend(ev); return ev
    d.resolve, d.encounter = resolve, encounter
    mint = lambda pid, verb, sj: H(w.world_seed, w.tick, pid, f"act:{verb}:{sj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(seasons):
        d.season(ch, question=None, subsistence=P.SUBSIST, contest_max_depth=w.fixtures.get("contest_max_depth"))
    for acts, ev in cap:
        em = defaultdict(list)
        for e in ev:
            a = d.act_of.get(e.id)
            if a is not None: em[a.id].append(e.kind)
        for a in acts:
            ks = em.get(a.id, []); row = VERB_TABLE[a.verb]
            T["attempted"] += 1
            if any(k in (row.emits_on_refusal or ()) for k in ks): T["refused"] += 1; continue
            if not ks: T["null"] += 1; continue
            T["executed_by_driver_rule"] += 1
            if set(ks) <= FALL:
                T["executed_but_only_fallback_kinds"] += 1; V[a.verb] += 1
    print(f"seed={seed} hash={w.content_hash()[:16]}", flush=True)
print(dict(T)); print(V.most_common(12))
