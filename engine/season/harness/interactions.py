"""`harness.interactions` -- AN INTERACTION AUDIT LOG: who did what to whom, on which question, from which
candidate table, under which relation facts, and what the fold made of it. ED-IN-0335's instrument (Jordan,
2026-11-05: *"I want you to log character interactions so that we can audit then diagnose why this kind of
behaviour is occurring"*). It DIAGNOSES; it changes no choice.

    python -m engine.season.harness.interactions <seasons> <seed> [--no-acquaintances] [--out PATH] [--audit]

THE OBSERVER, NOT A CARRIER (`harness/chronicle.py`'s precedent, CR-68/CR-69). The chooser is WRAPPED, never
steered: the wrapper calls the real `make_chooser` chooser, returns its scenes untouched, and then re-reads
the deliberation through the chooser's OWN single owners -- `opening_set` (narrowed to `resolvable_verbs()`
exactly as `make_chooser(verbs=...)` narrows), `choose.deliberation_memo` + `choose.score_terms` (the score's
terms), `choose.score_order` + `choose.sample_order` (the ranking and the Gumbel order), and
`decision_spread.attribute_top` (the deciding term). `harness/decision_spread.py::play_season` is the same
shape. NO HOOK IS ADDED TO `decision/choose.py`: the draw is keyed per candidate (`state/ids.py::draw_factory`
re-seeds from `(seed, tick, person, purpose)`), so a second reading consumes nothing. Whether the
re-read table IS the chooser's table is checked, not assumed: every act the chooser returned must match a
candidate of the re-read table by its minted id (`table_check`), and `test_interactions_log.py` asserts zero
misses. `World.content_hash()` with the observer on equals the hash with it off (same test).

ROWS (JSONL, one object per line, `kind` first):
  * `deliberation` -- every call of `choose` (a person with no question gets a row with `question: null`):
    season/tick/round, the actor, the question answered (id, source, referents, classes, `about`), its
    position in the person's question list and that list's sources, the CLAIM behind a question whose
    `about` is a claim the person holds (id, subject, predicate, source, chain, and its origin: an
    acquaintance claim written at build by CR-81 is recognised by membership in `w._acquaintances`, the ids
    `seed_acquaintances` returned), the candidate table (verb, subject, `to`, `pursuit`, `stance`, score,
    softmax probability of being sampled first at `choice_temperature`, score rank, sampled rank, chosen),
    the deciding term, the refusal gate's reading, and the relation facts toward every PERSON a chosen act
    names as `subject` or `to`.
  * `act` -- every act in the act store (`w.acts`, ATTEMPTED: `corpus_run.attempts`' set) naming another
    person as `subject` or `to`: its id and scene, the verb, both persons, whether the verb is HOSTILE
    (the score's own opponent rule, `options.subject_is_opponent`, with the person as `subject`), the
    deliberation it came from (by index), the relation facts AT DECISION TIME, the chosen candidate's terms
    and ranks, and the fold outcome (`corpus_run._attribute_acts`' made/refused rule, the one owner; plus the
    kinds of every Event `SeasonDriver.act_of` attributes to the act, and the `observed` reads of its refusal
    Events).

RELATION FACTS (`relation`), each read through the owner the tree has, at decision time:
  * same faction: `world_q.faction_holding` for both (None for none-or-many);
  * offices held: the person's live `hold` Tenures on an `Office` [ASSUMPTION: no single-owner reader of
    "the seats a person holds" exists; `options.exercisable_seats` is per verb row];
  * office relation: `state/gate.py::seated_on_the_rung_above_structure` both ways (the rung-above rule the
    revocation basis reads), same rung, `faction_q.purview` containment, and `faction_q.subordinates`'
    `oblige` edge both ways. Where none applies the row says `none the code reads`;
  * the actor holds an office whose `Office.faction` is the target's faction (ED-IN-0335's column);
  * the target is his faction's HEAD: the person a faction Proposition names as `subject` (the reading
    `decision_spread.common_referents` takes; `faction_q.head` reads `Tenure.degree` and is `None` in every
    built world, its own docstring);
  * `person_q.stance_toward`, `person_q.regard` with `person_q.deeds_judged`' two parts, and whether the
    actor's BUILD-TIME stance rows already held a negative row against the target (`person_q.held_against`
    over a snapshot taken before season 1: "authored hostility");
  * `person_q.known_persons` membership, and per source which of the actor's claims name the target (each
    claim asked of `known_persons` alone, then labelled `exists` / `seen` / `told` by the predicate
    `known_persons` reads -- [ASSUMPTION: the labelling repeats that function's three-way branch; the
    membership itself is the owner's answer]).

WHAT THE LOG CANNOT SHOW: (1) the candidates `opening_set` DECLINED to form (eligibility, the counterparty
rule, `own_stance_declines`, `held_edge_declines`, the dormant refusal gate) -- only what it formed; (2) why
the fold refused beyond the refusal Event's kind and its `observed` reads (a `REQUIRES_PREDICATES` verb reads
through a hand-written predicate that records nothing, `Event.observed`'s own comment); (3) contested acts'
opposing side's choice; (4) acts the chooser queued that a later re-deliberation replaced (they are in the
deliberation row's `chosen`, and absent from `act` rows). The rows are measured; the docstring is claimed.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import tempfile
from collections import Counter

from ..data.rosters import FACTION_BY_PROP, faction_prop_id
from ..data.verbs import VERB_TABLE, act_key
from ..decision import choose as CH, make_chooser, opening_set
from ..decision.options import refusal_tolerance, refuses, subject_is_opponent
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import faction_q, person_q, world_q
from ..state.gate import seated_on_the_rung_above_structure
from ..state.ids import H, draw_factory
from . import corpus_run
from .decision_spread import attribute_top
from .populated import build_realm

HOSTILE = tuple(sorted(v for v, r in VERB_TABLE.items() if subject_is_opponent(r)))
CONTESTED_COUNTERPARTY = tuple(sorted(v for v, r in VERB_TABLE.items()
                                      if r.contests and not subject_is_opponent(r)))
CLASSES = ("authored hostility", "same faction", "same faction, different office", "unaffiliated",
           "different faction, rival (stance<0)", "different faction, neutral")


# ---------------------------------------------------------------------------------------------
# RELATION FACTS


def held_offices(w, pid: str) -> list:
    p = w.persons.get(pid)
    if p is None:
        return []
    return sorted({t.object for t in p.tenures if t.kind == "hold" and t.live and t.object in w.offices})


def same_faction(w, a: str, t: str) -> bool:
    """Both cohere under one faction (`world_q.faction_holding`, the one owner). A module function so a test
    can plant a wrong reading here and see the log go wrong (the planted-failure control)."""
    fa = world_q.faction_holding(w, a)
    return fa is not None and fa == world_q.faction_holding(w, t)


def faction_heads(w) -> dict:
    """faction Proposition id -> the person it names as `subject` (see the module docstring)."""
    return {pid_: prop.subject for pid_, prop in w.propositions.items()
            if pid_ in FACTION_BY_PROP and prop.subject in w.persons}


def office_relation(w, a: str, t: str) -> list:
    A, T = held_offices(w, a), held_offices(w, t)
    if not A or not T:
        return ["n/a: " + ("neither" if not A and not T else ("actor" if not A else "target"))
                + " holds an office"]
    rel = set()
    for x in A:
        ox = w.offices[x]
        subs = set(faction_q.subordinates(w, x))
        reach = set(faction_q.purview(w, x))
        for y in T:
            oy = w.offices[y]
            if x == y:
                rel.add("same seat")
            if seated_on_the_rung_above_structure(w, ox, oy):
                rel.add("actor's seat on the rung above target's")
            if seated_on_the_rung_above_structure(w, oy, ox):
                rel.add("target's seat on the rung above actor's")
            if ox.rung is not None and ox.rung == oy.rung and x != y:
                rel.add("same rung (peer)")
            if oy.rung is not None and oy.rung in reach and oy.rung != ox.rung:
                rel.add("target's seat in actor's purview")
            if t in subs:
                rel.add("target obliged to actor's seat")
            if a in set(faction_q.subordinates(w, y)):
                rel.add("actor obliged to target's seat")
    return sorted(rel) or ["none the code reads (parent_of / purview / oblige)"]


def known_via(p, t: str) -> dict:
    """Which of `p`'s claims make `t` known, by `known_persons`' three sources."""
    pred = person_q.KNOWN_PERSON_CLAIM.get("predicate")
    out: dict = {}
    for c in p.ledger:
        if t not in person_q.known_persons([c], p.id):
            continue
        if c.chain and c.chain[-1] == t:
            out.setdefault("told", []).append(c.id)
        if c.predicate == pred and c.subject == t:
            out.setdefault("exists", []).append(c.id)
        elif c.predicate == person_q.SEEN_PREDICATE:
            out.setdefault("seen", []).append(c.id)
    return out


def relation(w, a: str, t: str, authored: dict, heads: dict) -> dict:
    p = w.persons[a]
    fx = w.fixtures
    fa, ft = world_q.faction_holding(w, a), world_q.faction_holding(w, t)
    sf = same_faction(w, a, t)
    offs_a, offs_t = held_offices(w, a), held_offices(w, t)
    stance = person_q.stance_toward(p, t)
    judged, told = person_q.deeds_judged(p, t, fx.get("scar_weight_shift"))
    via = known_via(p, t)
    # `Office.faction` is the faction NAME (`office_faction`); `faction_holding` answers the Proposition id
    off_in_tf = bool(ft) and any(w.offices[o].faction and faction_prop_id(w.offices[o].faction) == ft
                                 for o in offs_a)
    if t in authored.get(a, ()):
        cls = "authored hostility"
    elif sf:
        cls = "same faction, different office" if offs_a and offs_t and offs_a != offs_t else "same faction"
    elif fa is None or ft is None:
        cls = "unaffiliated"
    else:
        cls = "different faction, rival (stance<0)" if stance < 0 else "different faction, neutral"
    return {"same_faction": sf, "actor_faction": fa, "target_faction": ft,
            "actor_offices": offs_a, "target_offices": offs_t,
            "office_relation": office_relation(w, a, t),
            "actor_office_in_target_faction": off_in_tf,
            "target_is_faction_head": ft is not None and heads.get(ft) == t,
            "target_heads": sorted(f for f, h in heads.items() if h == t),
            "stance": stance, "regard": person_q.regard(p, t, fx), "judged": judged, "told": told,
            "authored_negative_row": t in authored.get(a, ()),
            "known": t in person_q.known_persons(p.ledger, a), "known_via": via, "class": cls}


def person_targets(persons, actor: str, payload) -> dict:
    """`{id: [roles]}`: the persons other than `actor` an act names as `subject` and/or `to`. `persons` is
    every id that was a Person when it was read (a target felled in the season is gone from `w.persons` at
    its end, and is still the target)."""
    pay = payload if isinstance(payload, dict) else {}
    out: dict = {}
    for role in ("subject", "to"):
        t = pay.get(role)
        if isinstance(t, str) and t in persons and t != actor:
            out.setdefault(t, []).append(role)
    return out


def is_hostile(verb: str, roles) -> bool:
    """The score's own opponent rule (`subject_is_opponent`), with the target as the act's `subject`."""
    row = VERB_TABLE.get(verb)
    return row is not None and subject_is_opponent(row) and "subject" in roles


# ---------------------------------------------------------------------------------------------
# THE RUN


def _question(q, p, acq: set) -> dict | None:
    if q is None:
        return None
    out = {"id": q.id, "source": q.source, "referents": list(q.referents),
           "classes": [list(x) for x in q.classes], "about": q.about, "claim": None}
    c = next((c for c in p.ledger if c.id == q.about), None)
    if c is not None:
        origin = ("acquaintance (CR-81 build claim)" if c.id in acq else
                  "told" if c.chain else "seen" if c.predicate == person_q.SEEN_PREDICATE
                  else "own:" + str(c.source))
        out["claim"] = {"id": c.id, "subject": c.subject, "predicate": c.predicate, "source": c.source,
                        "when": c.when, "chain": list(c.chain or ()), "origin": origin}
    return out


def run(seed: int, seasons: int, acquaintances: bool = True, observe: bool = True, world=None):
    """Build `build_realm(seed, acquaintances=...)` (or use `world`), play `seasons` seasons with the chooser
    watched when `observe`, and return `(w, d, rows)`. `observe=False` is the hash control's other arm: the
    same chooser, unwrapped."""
    w = build_realm(seed, acquaintances=acquaintances) if world is None else world
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    foldable = resolvable_verbs()
    draw = draw_factory(w.world_seed, lambda: w.tick)
    real = make_chooser(w.fixtures, mint, verbs=foldable, draw=draw)
    acq = set(getattr(w, "_acquaintances", ()) or ())
    authored = {pid: {row[0] for row in p.stance if person_q.held_against(p, row[0])}
                for pid, p in w.persons.items()}
    heads = faction_heads(w)
    fx = w.fixtures
    tau = float(fx.get("choice_temperature"))
    axis = fx.get("refusal_axis")
    delibs: list = []
    by_act: dict = {}                      # id(Act) -> (deliberation index, candidate index)
    held: list = []                        # keeps every returned Act alive, so `id()` stays unique
    season_no = [0]
    names = {pid: p.name for pid, p in w.persons.items()}     # every Person seen; grows at each deliberation

    def watched(p, v, s, ask_budget):
        scenes = real(p, v, s, ask_budget)
        for pid, x in w.persons.items():
            names.setdefault(pid, x.name)
        q = getattr(v, "question", None)
        qs = list(getattr(v, "questions", ()) or ())
        row = {"kind": "deliberation", "i": len(delibs), "season": season_no[0], "tick": w.tick,
               "round": d.round, "actor": p.id, "name": p.name,
               "faction": world_q.faction_holding(w, p.id), "offices": held_offices(w, p.id),
               "question": _question(q, p, acq),
               "question_position": next((i for i, x in enumerate(qs) if x is q), None),
               "questions": len(qs), "question_sources": [x.source for x in qs],
               "acquaintance_questions": sum(1 for x in qs if x.about in acq),
               "candidates": [], "table_check": None, "decider": None, "relations": {}}
        delibs.append(row)
        if q is None:
            return scenes
        cands = [c for c in opening_set(p, v, q, fx) if c.verb in foldable]
        memo = CH.deliberation_memo(p, fx)
        terms = [CH.score_terms(p, c, fx, memo) for c in cands]
        scores = {id(c): t[0] + t[1] for c, t in zip(cands, terms)}
        ranked = CH.score_order(cands, scores)
        sampled = CH.sample_order(ranked, lambda c: scores[id(c)], p, fx, draw)
        rank = {id(c): i for i, c in enumerate(ranked)}
        srank = {id(c): i for i, c in enumerate(sampled)}
        if cands and tau > 0:
            top = max(scores.values())
            ex = {k: math.exp((s - top) / tau) for k, s in scores.items()}
            z = sum(ex.values())
            prob = {k: e / z for k, e in ex.items()}
        else:
            prob = {id(c): float(srank[id(c)] == 0) for c in cands}
        minted = {mint(p.id, c.verb, act_key(c.verb, c.subject, c.operands)): k for k, c in enumerate(cands)}
        returned = [a for sc in scenes for a in sc.acts]
        chosen = {}
        missed = 0
        for a in returned:
            k = minted.get(a.id)
            if k is None:
                missed += 1
                continue
            chosen[k] = a.id
            by_act[id(a)] = (row["i"], k)
            held.append(a)
        row["table_check"] = {"returned_acts": len(returned), "unmatched": missed}
        for k, (c, t) in enumerate(zip(cands, terms)):
            ops = c.operands or {}
            row["candidates"].append({
                "verb": c.verb, "subject": c.subject, "to": ops.get("to"),
                "hostile": is_hostile(c.verb, ("subject",)) and c.subject in w.persons,
                "pursuit": t[0], "stance": t[1], "score": t[0] + t[1], "p_first": prob[id(c)],
                "score_rank": rank[id(c)], "sample_rank": srank[id(c)],
                "chosen": k in chosen, "act": chosen.get(k)})
        r = attribute_top(p, cands, fx, draw)
        row["decider"] = {"decider": r["decider"], "margin": r["margin"], "draw_kind": r["draw_kind"]}
        tol = refusal_tolerance(p, axis)
        row["refusal_gate"] = ("unarmed (refusal_axis unset)" if tol is None else
                               {c["verb"]: refuses(c["verb"], axis, tol)
                                for c in row["candidates"] if c["chosen"]})
        for a in returned:
            for t in person_targets(w.persons, p.id, a.payload):
                if t not in row["relations"]:
                    row["relations"][t] = relation(w, p.id, t, authored, heads)
        return scenes

    for _ in range(seasons):
        season_no[0] += 1
        d.season(watched if observe else real, question=None,
                 contest_max_depth=fx.get("contest_max_depth"))
    if not observe:
        return w, d, []
    return w, d, delibs + act_rows(w, d, seasons, delibs, by_act, names)


def act_rows(w, d, seasons: int, delibs: list, by_act: dict, names: dict) -> list:
    kinds: dict = {}
    observed: dict = {}
    for e in w.log:
        a = d.act_of.get(e.id)
        if a is None:
            continue
        kinds.setdefault(a.id, [])
        if e.kind not in kinds[a.id]:
            kinds[a.id].append(e.kind)
        row = VERB_TABLE.get(a.verb)
        if row is not None and e.kind in (row.emits_on_refusal or ()) and e.observed:
            observed.setdefault(a.id, []).extend(repr(o) for o in e.observed)
    out = []
    for a, made, refused in corpus_run.attempts(w, seasons):
        for t, roles in person_targets(names, a.actor, a.payload).items():
            src = by_act.get(id(a))
            dl = delibs[src[0]] if src else None
            cand = dl["candidates"][src[1]] if src else None
            q = dl["question"] if dl else None
            out.append({
                "kind": "act", "act": a.id, "scene": a.scene, "verb": a.verb, "roles": roles,
                "hostile": is_hostile(a.verb, roles),
                "season": dl["season"] if dl else None, "tick": dl["tick"] if dl else None,
                "round": dl["round"] if dl else None,
                "actor": a.actor, "actor_name": names.get(a.actor),
                "actor_faction": dl["faction"] if dl else None, "actor_offices": dl["offices"] if dl else None,
                "target": t, "target_name": names.get(t), "target_alive_at_end": t in w.persons,
                "deliberation": dl["i"] if dl else None,
                "question": q, "question_position": dl["question_position"] if dl else None,
                "relation": dl["relations"].get(t) if dl else None,
                "candidate": cand, "candidates": len(dl["candidates"]) if dl else None,
                "decider": dl["decider"] if dl else None,
                "made": list(made), "refused": list(refused), "events": kinds.get(a.id, []),
                "refusal_observed": observed.get(a.id, []),
                "outcome": "refused" if refused else ("executed" if made else "no declared event")})
    return out


# ---------------------------------------------------------------------------------------------
# READINGS


def audit(rows: list) -> list:
    """The act rows a designer would flag: a HOSTILE act between same-faction persons with stance >= 0."""
    return [r for r in rows if r["kind"] == "act" and r["hostile"] and r["relation"]
            and r["relation"]["same_faction"] and r["relation"]["stance"] >= 0]


def summary(rows: list) -> dict:
    acts = [r for r in rows if r["kind"] == "act"]
    by = Counter((r["verb"], r["relation"]["class"] if r["relation"] else "unmapped") for r in acts)
    verbs = Counter(r["verb"] for r in acts)
    flagged = audit(rows)
    src = Counter((r["question"] or {}).get("source") for r in flagged)
    origin = Counter(((r["question"] or {}).get("claim") or {}).get("origin") for r in flagged)
    hostile = [r for r in acts if r["hostile"] and r["relation"]]
    office_col = Counter((r["verb"], r["relation"]["actor_office_in_target_faction"]) for r in hostile)
    vs_head = [r for r in hostile if r["relation"]["target_is_faction_head"]]
    delib = [r for r in rows if r["kind"] == "deliberation"]
    return {"acts": len(acts), "by": by, "verbs": verbs, "flagged": len(flagged), "flagged_sources": src,
            "flagged_origins": origin, "office_col": office_col,
            "vs_head": [(r["season"], r["actor"], r["actor_name"], r["verb"], r["target"], r["target_name"],
                         r["relation"]["same_faction"], r["relation"]["stance"], r["outcome"])
                        for r in vs_head],
            "deliberations": len(delib),
            "unmatched": sum((r["table_check"] or {}).get("unmatched", 0) for r in delib),
            "unmapped_acts": sum(1 for r in acts if r["deliberation"] is None)}


def print_summary(s: dict, header: str) -> None:
    print(header)
    print(f"  deliberations {s['deliberations']}; acts with a person target {s['acts']} "
          f"(unmapped to a deliberation {s['unmapped_acts']}; chooser acts unmatched in the re-read table "
          f"{s['unmatched']})")
    print(f"  hostile verbs (the table's opponent rule, `subject_is_opponent`): {', '.join(HOSTILE)}; "
          f"contested against a counterparty: {', '.join(CONTESTED_COUNTERPARTY)}")
    order = sorted(s["verbs"], key=lambda v: (v not in HOSTILE, -s["verbs"][v], v))
    print("  verb            H  " + " | ".join(f"{c[:22]:>22}" for c in CLASSES + ("unmapped",)))
    for v in order:
        print(f"  {v:15} {'H' if v in HOSTILE else ' '}  "
              + " | ".join(f"{s['by'].get((v, c), 0):>22}" for c in CLASSES + ("unmapped",)))
    print(f"  HOSTILE acts between same-faction persons at stance >= 0: {s['flagged']}; by question source "
          f"{dict(s['flagged_sources'])}; by the question's claim origin {dict(s['flagged_origins'])}")
    print("  hostile acts by whether the actor holds an office of the target's faction: "
          + ", ".join(f"{v}/{'yes' if k else 'no'} {n}" for (v, k), n in sorted(s["office_col"].items())))
    print(f"  hostile acts against a faction HEAD: {len(s['vs_head'])}")
    for x in s["vs_head"]:
        print(f"    s{x[0]} {x[1]} {x[2]} {x[3]} -> {x[4]} {x[5]} same_faction={x[6]} stance={x[7]:g} {x[8]}")


def print_audit(rows: list) -> None:
    for r in audit(rows):
        rel, q = r["relation"], r["question"] or {}
        print(f"s{r['season']} t{r['tick']} r{r['round']} {r['actor']} {r['actor_name']} "
              f"[{rel['actor_faction']} {rel['actor_offices']}] {r['verb']} -> {r['target']} {r['target_name']} "
              f"[{rel['target_faction']} {rel['target_offices']}] outcome {r['outcome']} {r['events']}")
        print(f"   question {q.get('id')} ({q.get('source')}), position {r['question_position']}, claim "
              f"{(q.get('claim') or {}).get('origin')}; stance {rel['stance']:g} regard {rel['regard']:g} "
              f"office {rel['office_relation']} head-of {rel['target_heads']}; decider {r['decider']}")
        dl = r["deliberation"]
        for c in sorted(_rows_by_i(rows)[dl]["candidates"], key=lambda c: c["sample_rank"]):
            print(f"     {'*' if c['chosen'] else ' '} {c['verb']:14} {str(c['subject']):22} "
                  f"pursuit {c['pursuit']:+.3f} stance {c['stance']:+.3f} score {c['score']:+.3f} "
                  f"p_first {c['p_first']:.3f} rank {c['score_rank']} sampled {c['sample_rank']}")


def _rows_by_i(rows: list) -> dict:
    return {r["i"]: r for r in rows if r["kind"] == "deliberation"}


def write_jsonl(rows: list, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, sort_keys=False, default=str) + "\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="interactions", description=__doc__.split("\n\n")[0])
    ap.add_argument("seasons", type=int)
    ap.add_argument("seed", type=int)
    ap.add_argument("--no-acquaintances", action="store_true",
                    help="build_realm(acquaintances=False): CR-81's control arm")
    ap.add_argument("--out", default=None, help="JSONL path (default: the system temp directory)")
    ap.add_argument("--audit", action="store_true",
                    help="print only hostile acts between same-faction persons at stance >= 0, with tables")
    a = ap.parse_args(argv)
    acq = not a.no_acquaintances
    out = a.out or os.path.join(tempfile.gettempdir(),
                                f"interactions_s{a.seed}_n{a.seasons}{'' if acq else '_noacq'}.jsonl")
    w, _, rows = run(a.seed, a.seasons, acquaintances=acq)
    write_jsonl(rows, out)
    print(f"interactions seed {a.seed} seasons {a.seasons} acquaintances {'on' if acq else 'off'} "
          f"PYTHONHASHSEED={os.environ.get('PYTHONHASHSEED')} -> {out}; content_hash {w.content_hash()}")
    if a.audit:
        print_audit(rows)
    else:
        print_summary(summary(rows), "SUMMARY")
    return 0


if __name__ == "__main__":
    sys.exit(main())
