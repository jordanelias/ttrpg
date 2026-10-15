"""`harness.decision_spread` -- ARE THE REALM'S DECISIONS UNIQUE, AND WHICH TERM MAKES THEM SO (v9 IN-62).

ED-IN-0293's headline expectation (*"I expect all of this to end up generating unique decisions"*) as
three readings and three arms. Every reading that BUILDS A REALM lives here; `harness/conviction_spread.py`
is not extended, because it declares that it *"MEASURES THE TABLE, NOT A RUN"* (`:34-37`) and builds no
world. The score's terms have ONE owner, `decision/choose.py::score_terms` -> `(pursuit, stance,
urgency)`; this module calls it (through the module, so a rebind of it reaches every reading) and never
re-derives a term.

    python -m engine.season.harness.decision_spread --persons
    python -m engine.season.harness.decision_spread --decisions [--control | --null]
    python -m engine.season.harness.decision_spread --season    [--control | --null]
    python -m engine.season.harness.decision_spread --arms

WHAT EACH MODE READS, AND WHETHER IT PLAYS A SEASON (each prints the answer in its own header):

  --persons    BUILT REALM, NO SEASON.  Pairwise cosine of the projected vectors (`decision.project`,
               the seven-axis basis the score dots against): pairs above 0.99, the median, cosine to the
               mean vector; persons with a zero vector are counted and left out of the cosines (a cosine
               to nothing is undefined). Identical FULL-PROFILE groups over (the 15-vector of pursuits to
               2 dp, the affiliation vector `Person.conviction`, the factions committed to, the goal-commit
               set). Cohorts are grouped by territory.
  --decisions  BUILT REALM, NO SEASON.  One `claim_landed`-shaped question per COMMON referent -- the head
               of each faction whose Proposition names a person (the Crown's head is the King) -- handed
               to every person. The common candidate set is the intersection of the opening sets of the
               persons who form any, formed as `harness/corpus_run.py:958-960` forms them (`assemble`,
               `opening_set`), narrowed to `resolvable_verbs()` as the chooser narrows. Per person: the top
               candidate and its DECIDING TERM (`attribute_top`).
  --season     PLAYS ONE SEASON (`populated.run`'s composition, the chooser watched and never steered).
               Per-person executed verb multisets, how many are distinct, and per answered question its
               source and goal class. ATTENTION is read here ONLY: `--decisions` hands every person the
               same question, so it cannot see which question a person answered.
  --arms       PLAYS FOUR SEASONS, ONE PER ARM, in this process: `question_aggregation_rule` {first, all} x
               `stance_polarity` {legacy, declared} (§J.2's ask-then row, H-54 / H-194). Each arm prints
               the `--season` reading and the `--decisions` attribution counts under that arm.

  --control    ARM 0: every person's `pursuits` replaced by the realm-mean vector (the mean of the persons
               who hold one) and goals unseeded (`build_realm(goals=False)`, IN-68). Cohort temperaments
               off is a further switch SE-06 adds; before it lands the arm prints that it is a no-op.
               Applies to --persons, --decisions and --season.
  --null       `data/verbs.py::alignment_at('uniform')` (H-66, `:1407-1414`: *"`uniform` IS THE CONTROL"*)
               bound for the reading and restored after. Under it the pursuit term is one number for every
               candidate, so a top attributed to `pursuit` is a defect of the attribution. Applies to
               --decisions and --season (--persons reads no alignment cell and says so). The projection's
               own `uniform` is NOT the null: `pursuit_projection` declares a `sweep:` and has no
               `projection_at()` (`data/verbs.py:1166-1172`), and under a uniform projection the pursuit
               dot still varies by verb identically for everyone.

THERE IS NO `--cells`: per-cell leverage needs a projection rebind the tree does not have; the cells the
cast producer questioned go to the cell-value and cosine pass with `--decisions`' deciding-term reading as
evidence, and no cell is edited here.

THE DECIDING TERM (`attribute_top`), in the order it is tested:
  1. `draw`      the sampler's top is NOT the score's top (the draw outvoted the score), or the top two
                 scores are within `EPS` and `choice_temperature` > 0 (the draw ordered them);
  2. `tiebreak`  the top two scores are within `EPS` at temperature 0 (`(verb, subject)` ordered them);
  3. otherwise the TERMS whose removal leaves the top no longer strictly ahead of the field (it changes, or
     collapses into a tie): `pursuit`, `stance`, `urgency`, joined by `+`; `overdetermined` if no single
     term's removal does (two terms each separate it alone). Urgency has no candidate in it and can
     never decide.
So the attribution CAN say "no state decided": two persons with nothing separating their candidates read
`draw` or `tiebreak`, never `pursuit`.

NOTHING HERE IS PINNED AS A GOLDEN. The first run of an instrument IS the baseline (Jordan, 2026-09-14);
the commit that adds a mover quotes the base and the mover's reading side by side. `harness/delta.py` and
`harness/arms.py` read no person's score and are not extended.

SEAMS AND KNOWN LIMITS (the code is the mechanism; these are what the code does not do):
  * `attribute_top` repeats the chooser's ORDERING (`sorted` on `(-score, verb, subject)`, then
    `choose._sample_order`) because `make_chooser` holds it inside `choose`; the score FORMULA is not
    repeated. `test_in62_decision_spread.py` pins the top it returns to the real chooser's.
  * The draw is `draw_factory(world_seed, tick)` at the build's tick: a `--decisions` top is the top at that
    tick, not a distribution over ticks.
  * Absent in `--season`: an executed act whose `(actor, verb, subject)` the watch did not see leave a
    deliberation (a re-minted id) is counted `unmapped`, printed, and not attributed.
"""
from __future__ import annotations

import argparse
import contextlib
import math
import statistics
import sys
from collections import Counter
from typing import Optional

from engine.substrate.descriptors import PURSUITS

from ..data import verbs as V
from ..data.rosters import PURSUIT_AXES
from ..data.verbs import VERB_TABLE, alignment_at
from ..decision import assemble, choose as CH, make_chooser, opening_set
from ..decision.options import project
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..state.carriers import Candidate, Question
from ..state.ids import H, draw_factory
from . import probes as P
from .populated import build_realm

# [canonical: workplans/valoria_master_workplan_v9_part5.md §IN-62 — a float-tie tolerance, not a game number]
EPS = 1e-9
TERMS = ("pursuit", "stance", "urgency")
# [canonical: workplans/valoria_master_workplan_v9_part5.md §IN-64 EXIT — "pairs above 0.99"]
COSINE_HIGH = 0.99


# ---------------------------------------------------------------------------------------------
# ARMS


def realm_mean_pursuits(w) -> dict:
    """The mean of the pursuit vectors of the persons who hold one (`{}`-holders are not averaged in:
    a person with no vector is the absence of a view, not a view of zero)."""
    holders = [p for p in w.persons.values() if p.pursuits]
    if not holders:
        return {}
    return {name: sum(float(p.pursuits.get(name, 0.0)) for p in holders) / len(holders)
            for name in PURSUITS}


def apply_control(w) -> dict:
    """ARM 0: every person's `pursuits` becomes the realm-mean vector, a COPY each. Returns the mean."""
    mean = realm_mean_pursuits(w)
    for p in w.persons.values():
        p.pursuits = dict(mean)
    return mean


@contextlib.contextmanager
def null_alignment():
    """H-66's `uniform` bound on `data.verbs.ALIGNMENT` (the one binding `align` reads) and restored
    after, so the rebind cannot outlive the reading that wanted it."""
    saved = V.ALIGNMENT
    V.ALIGNMENT = alignment_at("uniform")
    try:
        yield
    finally:
        V.ALIGNMENT = saved


# ---------------------------------------------------------------------------------------------
# THE ATTRIBUTION


def attribute_top(p, cands: list, fx, draw=None, subsistence: float = 0.0) -> dict:
    """Rank `cands` for `p` as the chooser does and say WHICH TERM decided the top (the module docstring
    lists the tests in order). Returns `{top, decider, margin, scores, terms}`; `scores` and `terms` are
    parallel to `cands`. `cands` empty -> `top` None, `decider` `none`; one candidate -> `sole`."""
    if not cands:
        return {"top": None, "decider": "none", "margin": None, "scores": [], "terms": []}
    memo = CH.deliberation_memo(p, subsistence, fx)
    terms = [CH.score_terms(p, c, fx, memo) for c in cands]
    scores = [t[0] + t[1] + t[2] for t in terms]
    if len(cands) == 1:
        return {"top": cands[0], "decider": "sole", "margin": None, "scores": scores, "terms": terms}
    by_id = {id(c): s for c, s in zip(cands, scores)}
    order = sorted(range(len(cands)), key=lambda i: (-scores[i], cands[i].verb, cands[i].subject or ""))
    ranked = [cands[i] for i in order]
    actual = CH._sample_order(ranked, lambda c: by_id[id(c)], p, fx, draw)[0]
    ai = next(i for i, c in enumerate(cands) if c is actual)
    best, second = scores[order[0]], scores[order[1]]
    margin = best - second
    tau = float(fx.get("choice_temperature"))
    if ai != order[0]:
        decider = "draw"
    elif margin <= EPS:
        decider = "draw" if tau > 0 else "tiebreak"
    else:
        deciding = []
        for k, name in enumerate(TERMS):
            rest = [scores[j] - terms[j][k] for j in range(len(cands))]
            if rest[ai] - max(r for j, r in enumerate(rest) if j != ai) <= EPS:
                deciding.append(name)
        decider = "+".join(deciding) if deciding else "overdetermined"
    return {"top": actual, "decider": decider, "margin": margin, "scores": scores, "terms": terms}


# ---------------------------------------------------------------------------------------------
# --persons


def _cosine(a: list, b: list) -> Optional[float]:
    na, nb = math.sqrt(sum(x * x for x in a)), math.sqrt(sum(x * x for x in b))
    if na == 0 or nb == 0:
        return None
    return sum(x * y for x, y in zip(a, b)) / (na * nb)


def projected_vector(p, fx) -> list:
    axis_w = project(p, fx.get("scar_weight_shift"))
    return [axis_w[ax] for ax in PURSUIT_AXES]


def territory_of(w, pid: str) -> str:
    """The first TERRITORY rung on the person's home ancestry (`containment.ancestry`, the one walk);
    their home rung itself when none is a territory."""
    home = world_q.home_of(w).get(pid)
    if home is None:
        return "-"
    for r in world_q.ancestry(w, home):
        if w.rungs[r].kind == "territory":
            return r
    return home


def profile_key(w, p) -> tuple:
    """The FULL profile: 15-vector to 2 dp, affiliation vector, factions committed to, goal-commit set."""
    pur = tuple(round(float(p.pursuits.get(n, 0.0)), 2) for n in PURSUITS)
    aff = tuple(sorted((k, v) for k, v in (p.conviction or {}).items()))
    commits = sorted(t.object for t in p.tenures if t.kind == "commit" and t.live)
    fac = tuple(o for o in commits if o in w.propositions and o.startswith("fac_"))
    goals = tuple(o for o in commits if o not in fac)
    return (pur, aff, fac, goals)


def read_persons(w) -> dict:
    """The `--persons` figures on a built realm (no season is played)."""
    w._rehome()
    fx = w.fixtures
    ids = sorted(w.persons)
    vecs = {pid: projected_vector(w.persons[pid], fx) for pid in ids}
    live = [pid for pid in ids if any(vecs[pid])]
    cos = [c for i, a in enumerate(live) for b in live[i + 1:]
           if (c := _cosine(vecs[a], vecs[b])) is not None]
    mean = [sum(vecs[pid][k] for pid in live) / len(live) for k in range(len(PURSUIT_AXES))] if live else []
    to_mean = [c for pid in live if mean and (c := _cosine(vecs[pid], mean)) is not None]
    groups: dict = {}
    for pid in ids:
        groups.setdefault(profile_key(w, w.persons[pid]), []).append(pid)
    identical = {k: v for k, v in groups.items() if len(v) > 1}
    cohorts: dict = {}
    for pid in ids:
        if w.persons[pid].is_cohort:
            cohorts.setdefault(territory_of(w, pid), []).append(pid)
    return {
        "persons": len(ids), "cast": sum(1 for pid in ids if not w.persons[pid].is_cohort),
        "cohorts": sum(1 for pid in ids if w.persons[pid].is_cohort),
        "zero_vector": len(ids) - len(live), "with_vector": len(live),
        "pairs": len(cos), "pairs_above": sum(1 for c in cos if c > COSINE_HIGH),
        "median_cos": statistics.median(cos) if cos else None,
        "cos_to_mean_median": statistics.median(to_mean) if to_mean else None,
        "cos_to_mean_min": min(to_mean) if to_mean else None,
        "identical_groups": len(identical),
        "identical_groups_cast": sum(1 for v in identical.values()
                                     if not w.persons[v[0]].is_cohort),
        "identical_members": sum(len(v) for v in identical.values()),
        "identical_largest": max((len(v) for v in identical.values()), default=0),
        "distinct_profiles": len(groups),
        "cohort_territories": {
            t: {"cohorts": len(pids),
                "distinct_vectors": len({tuple(round(x, 6) for x in vecs[pid]) for pid in pids}),
                "distinct_profiles": len({profile_key(w, w.persons[pid]) for pid in pids})}
            for t, pids in sorted(cohorts.items())},
    }


# ---------------------------------------------------------------------------------------------
# --decisions


def common_referents(w) -> list:
    """`[(label, person id)]`: the head of every faction whose Proposition names a person. The Crown's
    head is the King. A person heading two factions appears once (first label)."""
    out, seen = [], set()
    for pid_, prop in sorted(w.propositions.items()):
        if not pid_.startswith("fac_") or prop.subject not in w.persons or prop.subject in seen:
            continue
        seen.add(prop.subject)
        out.append(("King (" + pid_ + ")" if pid_ == "fac_crown" else pid_, prop.subject))
    return out


def decision_question(referent: str) -> Question:
    """A `claim_landed`-shaped question about `referent`, the form `questions_for` stamps for a landed
    claim (`world_q.py:1858`), with an id that names this reading."""
    return Question(f"q:claim:spread:{referent}", "claim_landed", (referent,), f"claim:spread:{referent}")


def formed_set(w, p, q) -> list:
    """`p`'s opening set for `q`, formed as `corpus_run.py:958-960` forms it, narrowed to the verbs the
    fold resolves (the chooser's own `verbs=`)."""
    view = assemble(p, q, w.fixtures.get("view_k"))
    foldable = resolvable_verbs()
    return [c for c in opening_set(p, view, q, w.fixtures) if c.verb in foldable]


def read_decisions(w) -> dict:
    """The `--decisions` figures on a built realm (no season is played). Per referent: the persons handed
    the question, those who form any candidate, the common set (intersection of those), the number of
    distinct tops, and the deciding-term counts."""
    w._rehome()
    fx = w.fixtures
    draw = draw_factory(w.world_seed, lambda: w.tick)
    rows = []
    for label, ref in common_referents(w):
        q = decision_question(ref)
        formed = {pid: formed_set(w, p, q) for pid, p in sorted(w.persons.items())}
        keyed = {pid: {(c.verb, c.subject): c for c in cs} for pid, cs in formed.items() if cs}
        common = set.intersection(*(set(k) for k in keyed.values())) if keyed else set()
        tops: dict = {}
        deciders: Counter = Counter()
        for pid in keyed:
            cands = [keyed[pid][k] for k in sorted(common, key=lambda k: (k[0], k[1] or ""))]
            r = attribute_top(w.persons[pid], cands, fx, draw, P.SUBSIST(w.persons[pid], w))
            deciders[r["decider"]] += 1
            tops[pid] = (r["top"].verb, r["top"].subject) if r["top"] else None
        rows.append({"referent": label, "handed": len(formed), "forming": len(keyed),
                     "common": len(common), "distinct_tops": len(set(tops.values())),
                     "deciders": dict(deciders), "tops": tops})
    return {"rows": rows}


# ---------------------------------------------------------------------------------------------
# --season


def play_season(w, seasons: int = 1) -> dict:
    """Play `seasons` seasons through `populated.run`'s composition with the chooser WATCHED, never
    steered, and read what each person did and which question they answered."""
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    real = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                        draw=draw_factory(w.world_seed, lambda: w.tick))
    answered: Counter = Counter()          # (source, goal class) -> deliberations
    by_act: dict = {}                      # (actor, verb, subject) -> (source, goal class)

    def goal_class(q) -> str:
        if q.source != "need":
            return "-"
        return "own want" if q.about.startswith("prop_") else (
            "creed" if q.about.startswith("fac_") else "other need")

    def watched(p, v, s, ask_budget):
        scenes = real(p, v, s, ask_budget)
        q = getattr(v, "question", None)
        if q is not None:
            key = (q.source, goal_class(q))
            answered[key] += 1
            for sc in scenes:
                for a in sc.acts:
                    subj = (a.payload or {}).get("subject") if isinstance(a.payload, dict) else None
                    by_act[(p.id, a.verb, subj)] = key
        return scenes

    for _ in range(seasons):
        d.season(watched, question=None, subsistence=P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    multisets: dict = {}
    per_act: Counter = Counter()
    unmapped = 0
    for a in d.resolved:
        multisets.setdefault(a.actor, Counter())[a.verb] += 1
        subj = (a.payload or {}).get("subject") if isinstance(a.payload, dict) else None
        key = by_act.get((a.actor, a.verb, subj))
        if key is None:
            unmapped += 1
        else:
            per_act[key] += 1
    sigs = Counter(tuple(sorted(c.items())) for c in multisets.values())
    return {"seasons": seasons, "acts": len(d.resolved), "actors": len(multisets),
            "distinct_multisets": len(sigs), "largest_shared": max(sigs.values(), default=0),
            "answered": dict(answered), "per_act": dict(per_act), "unmapped": unmapped,
            "hash": w.content_hash()}


# ---------------------------------------------------------------------------------------------
# PRINTING


def _fmt(x) -> str:
    return "-" if x is None else f"{x:.4f}"


def print_persons(r: dict, arm: str) -> None:
    print(f"--persons [{arm}]  BUILT REALM, NO SEASON PLAYED")
    print(f"  persons {r['persons']} (cast {r['cast']}, cohorts {r['cohorts']}); "
          f"{r['with_vector']} hold a projected vector, {r['zero_vector']} hold none")
    print(f"  pairs over the {r['with_vector']} with a vector: {r['pairs']}; above {COSINE_HIGH}: "
          f"{r['pairs_above']}; median cosine {_fmt(r['median_cos'])}")
    print(f"  cosine to the mean vector: median {_fmt(r['cos_to_mean_median'])}, min {_fmt(r['cos_to_mean_min'])}")
    print(f"  identical full-profile groups (size > 1): {r['identical_groups']} covering "
          f"{r['identical_members']} persons ({r['identical_groups_cast']} among the cast) (largest {r['identical_largest']}); "
          f"distinct profiles {r['distinct_profiles']} of {r['persons']}")
    ct = r["cohort_territories"]
    if ct:
        print(f"  cohorts by territory ({len(ct)} territories):  territory  cohorts  distinct-vectors  distinct-profiles")
        for t, row in ct.items():
            print(f"    {t:24} {row['cohorts']:3}  {row['distinct_vectors']:3}  {row['distinct_profiles']:3}")


def print_decisions(r: dict, arm: str) -> None:
    print(f"--decisions [{arm}]  BUILT REALM, NO SEASON PLAYED")
    print("  referent                         handed forming common distinct-tops  deciding term (persons)")
    for row in r["rows"]:
        dec = ", ".join(f"{k} {v}" for k, v in sorted(row["deciders"].items()))
        print(f"  {row['referent']:32} {row['handed']:5} {row['forming']:7} {row['common']:6} "
              f"{row['distinct_tops']:13}  {dec}")
    tot: Counter = Counter()
    for row in r["rows"]:
        tot.update(row["deciders"])
    print(f"  all referents: {dict(sorted(tot.items()))}")


def print_season(r: dict, arm: str) -> None:
    print(f"--season [{arm}]  PLAYS {r['seasons']} SEASON(S)")
    print(f"  acts {r['acts']} by {r['actors']} actors; distinct per-person executed verb multisets "
          f"{r['distinct_multisets']} (largest shared by {r['largest_shared']} persons)")
    print("  answered question (source / goal class): deliberations")
    for k, v in sorted(r["answered"].items()):
        print(f"    {k[0]:14} {k[1]:10} {v}")
    print("  executed acts by the question answered: "
          + ", ".join(f"{k[0]}/{k[1]} {v}" for k, v in sorted(r["per_act"].items()))
          + f"; unmapped {r['unmapped']}")
    print(f"  content_hash {r['hash']}")


def _decider_total(r: dict) -> dict:
    tot: Counter = Counter()
    for row in r["rows"]:
        tot.update(row["deciders"])
    return dict(sorted(tot.items()))


def _build(seed: int, control: bool):
    w = build_realm(seed, goals=not control)
    if control:
        apply_control(w)
    return w


def run_arms(seed: int) -> list:
    """`--arms`: four seasons, one per (rule, polarity), each with its `--decisions` counts. One process,
    one `PYTHONHASHSEED` for every arm (the caller exports it)."""
    out = []
    for rule in ("first", "all"):
        for pol in ("legacy", "declared"):
            w = build_realm(seed)
            w.fixtures = w.fixtures.sweep("question_aggregation_rule", rule).sweep("stance_polarity", pol)
            dec = read_decisions(w)
            out.append({"rule": rule, "polarity": pol, "decisions": _decider_total(dec),
                        "season": play_season(w, 1)})
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="decision_spread", description=__doc__.split("\n\n")[0])
    ap.add_argument("--persons", action="store_true", help="built realm, NO season")
    ap.add_argument("--decisions", action="store_true", help="built realm, NO season")
    ap.add_argument("--season", action="store_true", help="PLAYS one season")
    ap.add_argument("--arms", action="store_true", help="PLAYS four seasons, one per arm")
    ap.add_argument("--control", action="store_true", help="arm 0: pursuits = realm mean")
    ap.add_argument("--null", action="store_true", help="alignment 'uniform' (H-66)")
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args(argv)
    if a.arms and (a.control or a.null or a.persons or a.decisions or a.season):
        ap.error("--arms is its own mode: it takes no other reading or arm flag")
    if a.control and a.null:
        ap.error("--control and --null are separate arms; run them apart")
    if not (a.persons or a.decisions or a.season or a.arms):
        if not (a.control or a.null):
            ap.error("name a reading: --persons, --decisions, --season or --arms")
        a.decisions = True                 # an arm alone reads the cheapest realm reading
        print("(--control/--null alone implies --decisions)")
    if a.arms:
        for row in run_arms(a.seed):
            print(f"ARM question_aggregation_rule={row['rule']} stance_polarity={row['polarity']}")
            print(f"  --decisions deciding term: {row['decisions']}")
            print_season(row["season"], f"{row['rule']}/{row['polarity']}")
        return 0
    arm = "control: pursuits = realm mean" if a.control else (
        "null: alignment uniform" if a.null else "shipped")
    if a.control:
        print("--control: goals are unseeded (IN-68: `build_realm(goals=False)`; the shipped "
              "`goals.yaml` carries rows since FA-05, FA-06); cohort temperaments off is NOT YET A SWITCH (SE-06)")
    with (null_alignment() if a.null else contextlib.nullcontext()):
        if a.persons:
            if a.null:
                print("--null: --persons reads no alignment cell; the null changes nothing here")
            print_persons(read_persons(_build(a.seed, a.control)), arm)
        if a.decisions:
            print_decisions(read_decisions(_build(a.seed, a.control)), arm)
        if a.season:
            print_season(play_season(_build(a.seed, a.control), 1), arm)
    return 0


if __name__ == "__main__":
    sys.exit(main())
