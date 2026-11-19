"""`harness.chronicle` -- a render of ONE seed's deepest cross-person chain, read OUTSIDE the simulation.

Plan position IN-37 (`STORY-READ`). `harness/storybar.py::read` already classifies every act's
antecedents and computes its cross-person chain depth; this module composes on it and does one more
thing: it picks the deepest chain and prints it as lines a reader can follow. It re-implements none
of the classification, writes nothing to the `World`, grades nothing and is wired into no gate.

THE OBSERVER, NOT A CARRIER. `ED-IN-0225` (2026-09-13) ruled that an arc has no carrier -- no type, no
rung, no tenure kind -- and that the carrier is not to be built. The pick is an observer's reading of
depth over a finished log. Nothing here is stored in the simulation: no arc, story or thread carrier, field, Event kind or
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

THE PROPAGATION READING (B02.16, behind `--propagation`; CLAUDE.md §4: the word and its definition). *How
far the played world's state differs from the same built world in which nobody acts.* ONE built world
is deep-copied twice (`storybar.fork`); one copy is played as the chronicle plays it, the other runs the
same seasons with a chooser that returns no act (MATTER and CALENDAR run in both, so the null arm is the
world's own clock and nothing else). Three columns, each a pure function over `World` that reads the
stores the content hash reads and owns no rule:
  (1) `moved_by_persons(w_played, w_null)` -- counts of differing entries, played against null, by
      component (`COMPONENTS`) and, beside them, the tenure Events by cause (`TENURE_CAUSES`);
  (2) `answered_outside_writing(w, verb_table)` -- executed cross-person answers whose verb is not
      deposit-only or emission-only (`corpus_run.emits_and_writes_nothing`'s census, plus the rows whose
      only `writes` are a Record, a Proposition or a Claim);
  (3) `terminals_answered(w)` -- per terminal Event kind (`TERMINALS`), how many were emitted and, of
      those, how many stand among the causes of another person's executed act.
Nothing here reads a status, a threshold or `requirements.yaml`; no `measure:` reads it (C3-K5: the removal
test is R-01's and R-02's instrument, this is a reading beside it). THE CONTROLS, both directions
(`tests/test_chronicle_propagation.py`): the null arm against itself reads zero in columns 1 and 2 and
answers nothing in column 3; a planted death of one seat-holder is seen in columns 1 and 3. If either
fails the reading is void. LIMITS: `act_of` is rebuilt from the log (`attribution.causing_act`: the first cause that is an act, which
is the driver's own map on a played run) because a World holds no driver; a MATTER Event whose first cause is an act id (a term
closure cites the act that wound the clock) would be read as that act's.

Entry point: `python -m engine.season.harness.chronicle --seed S --seasons K [--cap C] [--all-acts]
[--chains --min-depth D] [--propagation]`. `--seed` and
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

from ..data.rosters import MARGIN_ENDING
from ..data.rosters import PERSON_DIED
from ..data.verbs import VERB_TABLE
from ..loop.effects_combat import FIGHT_ROUNDS, FIRST_BLOOD, LEAD_CHANGES
from ..state.attribution import causing_act
from . import arc as ARC
from . import storybar as SB
from .corpus_run import emits_and_writes_nothing
from ..boot.realm import build_realm


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


def _rolled(log, act_of: dict) -> dict:
    """`{act_id: the margin tuple its Events carry}` (B05.18, SC-P1: `Event.ending` under `rosters.yaml: margin_endings`). A scene's
    `ending` (`fight_endings`: pairs of person and word) is not a margin tuple and is not read here: the keys decide."""
    out: dict = {}
    for e in log:
        a = act_of.get(e.id)
        end = getattr(e, "ending", ())                    # a planted Event (a test's namespace) may carry none
        if a is not None and end and {k for k, _v in end} == set(MARGIN_ENDING):
            out.setdefault(a.id, end)
    return out


def _shapes(log, act_of: dict, persons) -> dict:
    """`{act_id: "(n rounds, first blood X, k lead changes)"}` for each act whose Events carry `fight_rounds` (B14.15), read off
    the Observations `loop/effects_combat.py::scene_observed` put there; X is the person's name as a line names its actor, or
    `no first blood` where no blow landed. An act whose Events carry none gains nothing. A render change only."""
    out: dict = {}
    for e in log:
        a = act_of.get(e.id)
        if a is None or a.id in out:
            continue
        seen = getattr(e, "observed", ())                 # a planted Event (a test's namespace) may carry none
        held = {o.predicate: o.value for o in seen if o.predicate in (FIGHT_ROUNDS, LEAD_CHANGES)}
        if FIGHT_ROUNDS not in held:
            continue
        n, k = held[FIGHT_ROUNDS], held.get(LEAD_CHANGES, 0)
        first = next((o.subject for o in seen if o.predicate == FIRST_BLOOD), None)
        who = "no first blood" if first is None else f"first blood {_name(persons, first)}"
        out[a.id] = f"({n} round{'' if n == 1 else 's'}, {who}, {k} lead change{'' if k == 1 else 's'})"
    return out


def rolled_text(ending: tuple) -> str:
    """One act's roll as a line: *obstacle 3.7 = even 2.4 + difficulty 0.5 + opposition 0.8, pool 4.0, net 3.1, margin -0.6; leverage: proofs +2, favour +1*
    (SC-B Edit B's form). The terms are `Margin.terms` as it carried them; the levels are the aggressor's less the defender's per source."""
    d = dict(ending)
    terms = " + ".join(f"{n} {v:.3g}" for n, v in d["terms"])
    lev = ", ".join(f"{n} {a - b:+d}" for n, a, b in d["levels"] if a != b) or "none"
    return (f"obstacle {d['ob']:.3g} = {terms}, pool {d['pool']:.3g}, net {d['net']:.3g}, margin {d['margin']:.3g}; "
            f"leverage {d['leverage']:+.3g}: {lev}")


def lines(log, act_of: dict, rows: dict, persons) -> list:
    """The chain as structured lines: `[{"n", "act", "season", "actor", "verb", "kinds", "rolled",
    "shape", "answers"}]`, `rolled` the margin tuple of a social roll's Events (`()` for every act none graded),
    `shape` a fight's `(n rounds, first blood X, k lead changes)` (`""` for every act whose Events carry no `fight_rounds`, B14.15),
    `answers` the earlier line's `n` (None on the first). Root first."""
    chain = deepest_chain(rows)
    kinds = _kinds(log, act_of)
    rolled = _rolled(log, act_of)
    shapes = _shapes(log, act_of, persons)
    verb = {}
    for a in act_of.values():
        verb.setdefault(a.id, a.verb)
    out = []
    for i, aid in enumerate(chain):
        r = rows[aid]
        out.append({"n": i + 1, "act": aid, "season": r["season"],
                    "actor": _name(persons, r["actor"]), "verb": verb.get(aid, "?"),
                    "kinds": kinds.get(aid, []), "rolled": rolled.get(aid, ()),
                    "shape": shapes.get(aid, ""), "answers": i if i else None})
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
        roll = f" (rolled: {rolled_text(l['rolled'])})" if l["rolled"] else ""        # B05.18: beside what it emitted, where a margin graded it
        roll += f" {l['shape']}" if l["shape"] else ""                                                                 # B14.15: and a fight's shape
        out.append(f"{l['n']}. season {l['season']} | {l['actor']} {l['verb']} | "
                   f"emitted {', '.join(l['kinds']) or '(nothing)'}{roll} | {tail}")
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
# THE PROPAGATION READING (B02.16). Pure over `World`s; the module docstring defines it.
# ---------------------------------------------------------------------------------------------

#: Column 1's components, in print order: what is compared between the played and the null arm.
COMPONENTS = ("persons", "seat holds", "site conditions", "rungs", "stores", "stance rows",
              "pursuits", "convictions")

#: Column 1's tenure-change causes, in print order. `other` holds what none of the five names, so the
#: causes add to the tenure Events read.
TENURE_CAUSES = ("death", "term", "revocation", "claim", "conquest", "other")

#: The Event kinds that change who holds what. A reading of Events, so a change a verb makes without
#: one of these kinds is not here.
TENURE_EVENT_KINDS = ("tenure.opened", "tenure.closed", "succession.claimed")

#: The acts whose Events name their own cause, by verb row (`verb_table.yaml`). An act with another
#: verb is read `term` when its `tenure.closed` came later than the act (MATTER's maturing of a term it declared),
#: else `other`; an act-less `tenure.closed` is `term` too.
TENURE_CAUSE_OF_VERB = {"revoke": "revocation", "succeed": "claim", "seize": "conquest"}

#: Column 3's terminal Event kinds: what happened to a person, a seat, a field, a matter, a telling or a body.
TERMINALS = (PERSON_DIED, "tenure.closed", "field.won", "field.lost", "matter.determined",
             "news.told", "body.changed")

#: The kinds a row may write and still be deposit-only (column 2): a document, a proposition, a claim.
DEPOSIT_KINDS = ("Record", "Proposition", "Claim")


def _act_of(w) -> dict:
    """`{Event id: Act}` rebuilt from the log through `attribution.causing_act`, the one owner of which act
    caused an Event; equals `SeasonDriver.act_of` on a played run (seed 0, two seasons: 1809 of 1809
    Events). A World holds no driver."""
    out = {}
    for e in w.log:
        a = causing_act(w, e)
        if a is not None:
            out[e.id] = a
    return out


def _executed(w, act_of: dict) -> dict:
    """`storybar.read`'s executed rows over `w`: every act not refused (`corpus_run.attempts`' rule, read
    over the ticks the world has run), with its `cross` antecedents cut the same way. One season bound
    stands for the whole run: no column here reads a season."""
    refused = SB.refusal_sets(w, max(w.tick, 0))[0]
    return SB.read(w.log, act_of, [0], refused)["executed"]


def _differing(a: dict, b: dict) -> int:
    """How many keys of the union of `a` and `b` read differently (absent counts as a value)."""
    gone = object()
    return sum(1 for k in a.keys() | b.keys() if a.get(k, gone) != b.get(k, gone))


def _projection(w) -> dict:
    """`{component: {key: value}}` for `COMPONENTS`: the state a person's choice can move. A reading of
    the stores the content hash folds; no rule. A stance row is keyed by its text and counted, so two
    equal rows are two entries."""
    stance, pursuits, convictions = Counter(), {}, {}
    for pid, p in w.persons.items():
        for row in p.stance:
            stance[(pid, repr(row))] += 1
        pursuits.update({(pid, k): v for k, v in p.pursuits.items()})
        convictions.update({(pid, k): v for k, v in p.conviction.items()})
    return {
        "persons": {pid: p.weight for pid, p in w.persons.items()},
        "seat holds": {(t.subject, t.object): True for t in w.tenures
                       if t.kind == "hold" and t.live and t.object in w.offices},
        "site conditions": {sid: s.condition for sid, s in w.sites.items()},
        "rungs": {rid: (r.kind, tuple(sorted(map(str, r.envelope)))) for rid, r in w.rungs.items()},
        "stores": {(rid, matter): n for rid, r in w.rungs.items() for matter, n in r.stores.items()},
        "stance rows": dict(stance),
        "pursuits": pursuits,
        "convictions": convictions,
    }


def tenure_changes_by_cause(w) -> dict:
    """`{cause: count}` over `TENURE_CAUSES`: the tenure Events (`TENURE_EVENT_KINDS`) in `w.log`, each read
    once. DEATH: a `tenure.closed` whose Events were written with a `person.died` (same `causes`, same
    tick: the gate's one write for a death, `loop/matter.py::_die` and the fold's kill). Else the act that
    caused it, by verb (`TENURE_CAUSE_OF_VERB`); else a `tenure.closed` is TERM when it came LATER than
    the act it names (MATTER's maturing of a declared term closes with `causes=[term.declared_by]`, the
    declaring act's id, so `_act_of` ties it to that act and only its tick tells it from a close the act
    made itself; with no act at all a `tenure.closed` is `term` too); else `other`."""
    died = {(tuple(e.causes), e.emitted_at) for e in w.log if e.kind == PERSON_DIED}
    act_of = _act_of(w)
    first_at: dict = {}
    for e in w.log:
        if (a := act_of.get(e.id)) is not None:
            first_at[a.id] = min(first_at.get(a.id, e.emitted_at), e.emitted_at)
    out = {c: 0 for c in TENURE_CAUSES}
    for e in w.log:
        if e.kind not in TENURE_EVENT_KINDS:
            continue
        a = act_of.get(e.id)
        if e.kind == "tenure.closed" and (tuple(e.causes), e.emitted_at) in died:
            cause = "death"
        elif a is not None:
            cause = TENURE_CAUSE_OF_VERB.get(a.verb) or (
                "term" if e.kind == "tenure.closed" and e.emitted_at > first_at[a.id] else "other")
        else:
            cause = "term" if e.kind == "tenure.closed" else "other"
        out[cause] += 1
    return out


def moved_by_persons(w_played, w_null) -> dict:
    """COLUMN 1. `{name: count}`: for each of `COMPONENTS`, how many entries of the played world's
    state differ from the null world's (an entry in one and not the other differs), then
    `tenure.<cause>` for each of `TENURE_CAUSES`, the difference in tenure Events of that cause. Zero
    everywhere exactly when nothing a person did reached the state."""
    pa, pn = _projection(w_played), _projection(w_null)
    out = {c: _differing(pa[c], pn[c]) for c in COMPONENTS}
    ta, tn = tenure_changes_by_cause(w_played), tenure_changes_by_cause(w_null)
    out.update({f"tenure.{c}": abs(ta[c] - tn[c]) for c in TENURE_CAUSES})
    return out


def _is_deposit_only(row) -> bool:
    """A row whose `writes` are all documents, propositions or claims (never empty)."""
    return bool(row.writes) and all(x.split(".")[0] in DEPOSIT_KINDS for x in row.writes)


def answered_outside_writing(w, verb_table) -> int:
    """COLUMN 2. How many executed acts answered another person's act (a `cross` antecedent) by a verb that
    is not deposit-only or emission-only: not in `corpus_run.emits_and_writes_nothing(verb_table)`'s census
    and not a row whose only `writes` are a Record, a Proposition or a Claim (`DEPOSIT_KINDS`). An act
    whose verb has no row in `verb_table` counts: nothing says it only deposits."""
    silent = set(emits_and_writes_nothing(verb_table)) | {v for v, r in verb_table.items()
                                                          if _is_deposit_only(r)}
    rows = _executed(w, _act_of(w))
    return sum(1 for aid, r in rows.items() if r["cross"] and w.acts.get(aid).verb not in silent)


def terminals_answered(w) -> dict:
    """COLUMN 3. `{kind: (emitted, answered)}` for each of `TERMINALS`: the Events of that kind in the log
    and, of those, how many stand among the `causes` of an executed act by a person other than the one who
    caused the terminal (a terminal no act caused, as MATTER's, is another person's to every actor). Each
    terminal counts once however many acts cite it."""
    act_of = _act_of(w)
    executed = _executed(w, act_of)
    kind = {e.id: e.kind for e in w.log if e.kind in TERMINALS}
    cited = set()
    for e in w.log:
        a = act_of.get(e.id)
        if a is None or a.id not in executed:
            continue
        for c in e.causes:
            if c in kind and getattr(act_of.get(c), "actor", None) != a.actor:
                cited.add(c)
    emitted = Counter(kind.values())
    answered = Counter(kind[c] for c in cited)
    return {k: (emitted[k], answered[k]) for k in TERMINALS}


def nobody_acts(chooser):
    """`drive`'s `wrap_chooser` for the null arm: every person's scene is empty, whatever the chooser would
    have chosen. The season's MATTER and CALENDAR still run."""
    return lambda p, v, s, ask_budget: []


def propagation(base, seasons: int) -> dict:
    """THE READING over ONE built world `base`, never run itself: a played copy and a null copy
    (`nobody_acts`), each `seasons` seasons. Returns `{"moved", "outside_writing", "terminals",
    "null_terminals"}`: columns 1 to 3 of the played arm, and column 3 of the null arm beside it so a
    terminal MATTER emits in both reads against its own denominator."""
    arms = {}
    for name, wrap in (("played", None), ("null", nobody_acts)):
        w = SB.fork(base)
        arms[name] = SB.drive(w.world_seed, seasons, "off", world=w, wrap_chooser=wrap)[0]
    return {"moved": moved_by_persons(arms["played"], arms["null"]),
            "outside_writing": answered_outside_writing(arms["played"], VERB_TABLE),
            "terminals": terminals_answered(arms["played"]),
            "null_terminals": terminals_answered(arms["null"])}


def render_propagation(seed, seasons: int, cap, res: dict) -> str:
    """The three columns as text, one line per entry."""
    out = [f"propagation seed={seed} seasons={seasons} cap={cap} PYTHONHASHSEED={os.environ.get('PYTHONHASHSEED')}",
           "(1) moved by persons: entries of the played state that differ from the null arm's"]
    out += [f"    {k:<22} {n:>6}" for k, n in res["moved"].items()]
    out.append(f"(2) answered outside writing: {res['outside_writing']} executed cross-person answers "
               "by a verb that is not deposit-only or emission-only")
    out.append("(3) terminals answered: emitted / answered by another person's executed act   "
               "[null arm: emitted / answered]")
    for k, (n, a) in res["terminals"].items():
        nn, na = res["null_terminals"][k]
        out.append(f"    {k:<18} {n:>6} / {a:<6}   [{nn} / {na}]")
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
    ap.add_argument("--propagation", action="store_true",
                    help="print the propagation reading INSTEAD of the chain: how far the played world's state "
                         "differs from the same built world where nobody acts (three columns: entries moved by "
                         "persons, executed answers outside writing, terminal Events answered); a reading, no bar")
    args = ap.parse_args(argv)
    if args.chains and args.min_depth is None:
        ap.error("--chains requires --min-depth (no default)")
    if args.propagation and (args.chains or args.all_acts):
        ap.error("--propagation prints its own reading; it takes neither --chains nor --all-acts")
    if args.propagation:
        base = build_realm(args.seed, args.cap)
        print(render_propagation(args.seed, args.seasons, args.cap, propagation(base, args.seasons)))
        return 0

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
