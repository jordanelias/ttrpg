"""`harness.chronicle` -- a render of ONE seed's deepest cross-person chain, read OUTSIDE the simulation.

Plan position IN-37 (`STORY-READ`). `harness/storybar.py::read` already classifies every act's
antecedents and computes its cross-person chain depth; this module composes on it and does one more
thing: it picks the deepest chain and prints it as lines a reader can follow. It re-implements none
of the classification, writes nothing to the `World`, grades nothing and is wired into no gate.

THE OBSERVER, NOT A CARRIER (`ED-IN-0225`). The pick is an observer's reading of depth over a finished
log. Nothing here is stored in the simulation: no arc, story or thread carrier, field, Event kind or
register row exists or is created, and nothing is ranked by salience inside the loop (the loop never
imports this module). `tests/test_in37_chronicle.py` observes this -- the World's content hash, log
length and write list are unchanged by a render, and the module's AST names no write call.

THE PICK (`deepest_chain`, pure over `storybar.read`'s rows). The END of the chain is the act of
greatest `depth`; ties go to the act logged FIRST (`read` returns acts in first-logged order, and the
scan keeps the first act that reaches a new maximum). The chain is then walked BACK: from an act of
depth d, its antecedent is the act among its `cross` antecedents whose depth is d - 1, ties to the
SMALLEST ACT ID (`storybar.read` sorts `cross` lexicographically), not the one logged first. Because depth is `1 + max(depth of cross antecedents)`, such an antecedent
always exists. The chain is returned root-first, so the render reads in causal order. A run whose
deepest chain is depth 1 (no act answered another person's) renders its first-logged act alone,
and says so.

THE RENDER (`render`, pure over `(log, act_of, rows, persons)`, so a test can plant on it). One line
per act in causal order:
  `<n>. season <s> | <actor> <verb> | emitted <kind, kind> | answers <m>. <actor> <verb>`
where `<actor>` is the Person's `name` when it has one and the id otherwise, `<kind>`s are the
distinct Event kinds the act emitted in log order, and the first line reads `opens the chain`. `<m>`
is the line number of the antecedent act, always an earlier line.

THE SELECTION (CR-68, `chronicle.main`, which holds `w`). By default the pick runs over CONSEQUENCE ACTS:
`arc.consequence_acts(w, act_of)` (over `arc.consequence_kinds`, the one owner of the predicate; `arc.py` imports `storybar`, so the predicate cannot
live there) names the acts that caused an Event whose Receipt writes a `(kind, field)` of `arc.py`'s
`ARC_SELF` or `ARC_WORLD`. This module holds no roster of its own. Every other act is cut the way
`storybar._executed_rows` cuts a refused one (`read`'s `refused` argument is handed the acts that are NOT
consequence acts): the act, and every cross edge into it, leave the rows and `depth` is recomputed along
what remains; a cut act is not bridged over. `deepest_chain(rows)` is unchanged and stays pure over the
rows it is handed. A graded loss that writes (a lost duel, a `field.lost`) is a consequence act; a refusal
writes nothing and is not. `--all-acts` restores the pick over every act, today's selection before CR-68;
the retired `--executed-only` cut by the driver's refusal rule, which counts a graded loss as refused.
The header line keeps its fields and gains `consequence_acts=` at its end (`acts=` stays the count of
every act read); `depth=` is the rendered chain's. A log with no consequence act says so and renders nothing.
[ASSUMPTION; medium; Jordan to correct; revert: restore `--executed-only` and the depth-only pick]

LIMIT, STATED. An "answers" edge is any cause edge that resolves through `act_of` to another person's
act (`storybar.read`: an occasion Event is such a cause too), so a chain shows what an act had among its
causes, not that the later actor decided BECAUSE of the earlier one. The render says "answers" and means
"had among its causes". And an act counts as a consequence by what its OWN Events wrote; what other
people's acts or MATTER chained after it does not count for it.

THE STORY READING (CR-69, `consequence_chains`, behind `--chains`). Over the same consequence acts, per seed:
the number of CHAIN ENDS -- consequence acts that no other consequence act answers (along the `cross`
edges of the rows cut to consequence acts, as above; a person's later act answering his own is no `cross`
edge) -- whose cross-person depth, recomputed along those edges only, is at least `--min-depth`; and a
histogram of the Event kinds carried by the Receipts that made each such end a consequence act
(`arc.consequence_kinds`, the one owner of the predicate; kinds are READ OFF the log). NO roster of story
types and NO classification into war / succession / ruin / grudge; no pass bar, no default for `--min-depth`
(`--chains` without it is refused). It does not call `storybar.chains`, does not touch `_executed_rows`
(it reads `read`'s `executed` rows, as the pick does) and changes no existing result. A reading, never a
guard. Kinds are counted here once, raw, over the chain ends only: `harness/strife.py` maps Event kinds to
its move codes over the whole log and owns that tabulation; this block maps nothing to a code.
[ASSUMPTION; medium; Jordan to correct; revert: delete the reader]

Entry point: `python -m engine.season.harness.chronicle --seed S --seasons K [--cap C] [--all-acts]
[--chains --min-depth D]`. `--seed` and
`--seasons` are required and have no default (this file is inside `tools/ci_sim_fabrication_check.py`'s
blocking scope, the reason `harness/storybar.py` and `harness/soak.py` give); `--cap` is optional and
is `build_realm`'s own parameter, defaulting to its own `None`, the full realm. The header line
prints `PYTHONHASHSEED`, as `storybar`'s does.
"""

from __future__ import annotations

import argparse
import os
import sys
from collections import Counter

from . import arc as ARC
from . import storybar as SB


# ---------------------------------------------------------------------------------------------
# THE PICK. Pure: `storybar.read`'s rows.
# ---------------------------------------------------------------------------------------------

def deepest_chain(rows: dict) -> list:
    """Act ids of the deepest cross-person chain, root first. `rows` is `read(...)["acts"]`.

    The end act is the first-logged act of maximal depth; each step back takes the cross antecedent
    one level shallower, the smallest act id on a tie (`cross` is sorted). Empty when there are no acts."""
    if not rows:
        return []
    end, best = None, 0
    for aid, r in rows.items():
        if r["depth"] > best:                  # strict: the first-logged act at a depth keeps it
            end, best = aid, r["depth"]
    chain = [end]
    cur = end
    while rows[cur]["depth"] > 1:
        want = rows[cur]["depth"] - 1
        cur = next(b for b in rows[cur]["cross"] if b in rows and rows[b]["depth"] == want)
        chain.append(cur)
    chain.reverse()
    return chain


# ---------------------------------------------------------------------------------------------
# THE RENDER. Pure: the log, `act_of`, the rows, and the persons table.
# ---------------------------------------------------------------------------------------------

def _name(persons, actor: str) -> str:
    return getattr(persons.get(actor), "name", "") or actor


def _kinds(log, act_of: dict) -> dict:
    """`{act_id: [distinct Event kinds in log order]}`."""
    out: dict = {}
    for e in log:
        a = act_of.get(e.id)
        if a is None:
            continue
        ks = out.setdefault(a.id, [])
        if e.kind not in ks:
            ks.append(e.kind)
    return out


def lines(log, act_of: dict, rows: dict, persons) -> list:
    """The chain as structured lines: `[{"n", "act", "season", "actor", "verb", "kinds",
    "answers"}]`, `answers` the earlier line's `n` (None on the first). Root first."""
    chain = deepest_chain(rows)
    kinds = _kinds(log, act_of)
    verb = {}
    for a in act_of.values():
        verb.setdefault(a.id, a.verb)
    out = []
    for i, aid in enumerate(chain):
        r = rows[aid]
        out.append({"n": i + 1, "act": aid, "season": r["season"],
                    "actor": _name(persons, r["actor"]), "verb": verb.get(aid, "?"),
                    "kinds": kinds.get(aid, []),
                    "answers": i if i else None})
    return out


def render(log, act_of: dict, rows: dict, persons) -> str:
    """The deepest cross-person chain as readable text, one line per act in causal order."""
    ls = lines(log, act_of, rows, persons)
    if not ls:
        return "no acts in the log; nothing to chronicle"
    out = []
    if len(ls) == 1:
        out.append("no act answered another person's act; the first-logged act alone:")
    for l in ls:
        if l["answers"] is None:
            tail = "opens the chain"
        else:
            a = ls[l["answers"] - 1]
            tail = f"answers {a['n']}. {a['actor']} {a['verb']}"
        out.append(f"{l['n']}. season {l['season']} | {l['actor']} {l['verb']} | "
                   f"emitted {', '.join(l['kinds']) or '(nothing)'} | {tail}")
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# THE STORY READING (CR-69). Over `(w, act_of, bounds, min_depth)`; `log` lets a control hand in
# `arc.shuffled_causes(...)`.
# ---------------------------------------------------------------------------------------------

def chain_ends(rows: dict, min_depth: int) -> list:
    """Act ids in `rows` (consequence rows: `read(...)["executed"]` over the cut) that no other row answers
    (no row lists them in `cross`) and whose `depth` is at least `min_depth`, in row order."""
    answered = {b for r in rows.values() for b in r["cross"]}
    return [aid for aid, r in rows.items() if aid not in answered and r["depth"] >= min_depth]


def consequence_chains(w, act_of: dict, bounds: list, min_depth: int, log=None) -> dict:
    """CR-69 -- `{"consequence_acts": n, "chain_ends": m, "kinds": {Event kind: ends carrying it}}`.

    The ends are `chain_ends` over the rows `storybar.read` gives with every NON-consequence act cut (and
    the edges into it, depth recomputed, as the pick does); `kinds` counts, per kind, the ends whose
    consequence-making Events (`arc.consequence_kinds`) include it, sorted by kind. `log` defaults to
    `w.log`; the control `arc.shuffled_causes(w.log, seed)` breaks only the links. Reads only."""
    log = list(w.log if log is None else log)
    made = ARC.consequence_kinds(w, act_of, log)
    cut = frozenset(a.id for a in act_of.values() if a.id not in made)
    rows = SB.read(log, act_of, bounds, cut)["executed"]
    ends = chain_ends(rows, min_depth)
    hist = Counter(k for aid in ends for k in made[aid])
    return {"consequence_acts": len(made), "chain_ends": len(ends), "kinds": dict(sorted(hist.items()))}


def render_chains(seed, min_depth: int, res: dict) -> str:
    """The reading as a two-line block."""
    kinds = ", ".join(f"{k}={n}" for k, n in res["kinds"].items()) or "(none)"
    return (f"chains seed={seed} min_depth={min_depth} consequence_acts={res['consequence_acts']} "
            f"chain_ends={res['chain_ends']}\nkinds on the ends' consequence Events: {kinds}")


# ---------------------------------------------------------------------------------------------
# CLI.
# ---------------------------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--seasons", type=int, required=True)
    ap.add_argument("--arm", choices=SB.ARMS, default=SB.ARMS[0],
                    help=f"forcing arm; built: {', '.join(SB.ARMS)}")
    ap.add_argument("--cap", type=int, default=None,
                    help="build_realm's cast cap; omitted = build_realm's own None, the full realm")
    ap.add_argument("--all-acts", action="store_true",
                    help="pick the deepest chain over EVERY act, as before CR-68; without it the pick "
                         "runs over consequence acts only (arc.consequence_acts: an Event the act "
                         "caused carries a Receipt writing a (kind, field) of ARC_SELF or ARC_WORLD; "
                         "the other acts and every edge into one are cut, depth recomputed)")
    ap.add_argument("--chains", action="store_true",
                    help="after the render, print the story reading (CR-69): the count of consequence chain "
                         "ends of cross-person depth at least --min-depth and a histogram of the Event kinds "
                         "that made them consequence acts; a reading, no bar")
    ap.add_argument("--min-depth", type=int, default=None,
                    help="REQUIRED with --chains, no default: the least cross-person depth of a chain end counted")
    args = ap.parse_args(argv)
    if args.chains and args.min_depth is None:
        ap.error("--chains requires --min-depth (no default)")

    w, d, bounds = SB.drive(args.seed, args.seasons, args.arm, args.cap)
    consequence = ARC.consequence_acts(w, d.act_of)
    cut = None
    if not args.all_acts:
        cut = frozenset(a for a in {a.id for a in d.act_of.values()} if a not in consequence)
    res = SB.read(w.log, d.act_of, bounds, cut)
    rows = res["acts"] if args.all_acts else res["executed"]
    chain = deepest_chain(rows)
    head = (f"chronicle seed={args.seed} seasons={args.seasons} arm={args.arm} cap={args.cap} "
            f"acts={len(res['acts'])} depth={len(chain)} PYTHONHASHSEED={os.environ.get('PYTHONHASHSEED')} "
            f"consequence_acts={len(consequence)}")
    print(head)
    if not rows and res["acts"]:
        print("no consequence act in the log; --all-acts renders over every act")
    else:
        print(render(w.log, d.act_of, rows, w.persons))
    if args.chains:
        print(render_chains(args.seed, args.min_depth,
                            consequence_chains(w, d.act_of, bounds, args.min_depth)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
