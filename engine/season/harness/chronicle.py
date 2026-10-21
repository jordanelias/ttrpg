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

Entry point: `python -m engine.season.harness.chronicle --seed S --seasons K [--cap C]`. `--seed` and
`--seasons` are required and have no default (this file is inside `tools/ci_sim_fabrication_check.py`'s
blocking scope, the reason `harness/storybar.py` and `harness/soak.py` give); `--cap` is optional and
is `build_realm`'s own parameter, defaulting to its own `None`, the full realm. The header line
prints `PYTHONHASHSEED`, as `storybar`'s does.
"""

from __future__ import annotations

import argparse
import os
import sys

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
    args = ap.parse_args(argv)

    w, d, bounds = SB.drive(args.seed, args.seasons, args.arm, args.cap)
    res = SB.read(w.log, d.act_of, bounds)
    chain = deepest_chain(res["acts"])
    print(f"chronicle seed={args.seed} seasons={args.seasons} arm={args.arm} cap={args.cap} "
          f"acts={len(res['acts'])} depth={len(chain)} PYTHONHASHSEED={os.environ.get('PYTHONHASHSEED')}")
    print(render(w.log, d.act_of, res["acts"], w.persons))
    return 0


if __name__ == "__main__":
    sys.exit(main())
