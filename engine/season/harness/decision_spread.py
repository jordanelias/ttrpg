"""`harness.decision_spread` -- ARE THE REALM'S DECISIONS UNIQUE, AND WHICH TERM MAKES THEM SO (v9 IN-62).

ED-IN-0293's headline expectation (*"I expect all of this to end up generating unique decisions"*) as
three readings and three arms. Every reading that BUILDS A REALM lives here; `harness/conviction_spread.py`
is not extended, because it declares that it *"MEASURES THE TABLE, NOT A RUN"* (`:34-37`) and builds no
world. The score's terms have ONE owner, `decision/choose.py::score_terms` -> `(pursuit, stance, fit)`;
this module calls it (through the module, so a rebind of it reaches every reading) and never
re-derives a term.

    python -m engine.season.harness.decision_spread --persons
    python -m engine.season.harness.decision_spread --decisions [--control | --null]
    python -m engine.season.harness.decision_spread --season    [--control | --null]
    python -m engine.season.harness.decision_spread --arms
    python -m engine.season.harness.decision_spread --retries [--seed N] [--seasons K]

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
               Per-person RESOLVED verb multisets (the acts the fold resolved, `d.resolved`: made or refused
               in the fold, not those refused at admission), how many are distinct, and per answered
               question its source and goal class. Also the draw split of every deliberation (below).
               ATTENTION is read here ONLY: `--decisions` hands every person the same question, so it
               cannot see which question a person answered.
  --arms       PLAYS FOUR SEASONS, ONE PER ARM, in this process: `question_aggregation_rule` {first, all} x
               `stance_polarity` {legacy, declared} (§J.2's ask-then row, H-54 / H-194). Each arm prints
               the `--season` reading and the `--decisions` attribution counts under that arm.

  --retries    PLAYS `--seasons` SEASONS (default 2) as `populated.run` plays them, and prints the FIVE READINGS of
               `16_PESSIMIST_CORE_a_refusal_is_remembered` (A-81, "a refusal is remembered"): what a person does
               with an opportunity he was refused. `play_retries`' docstring defines each row; `retry_rows` computes
               them from the attempts, a pure function.
  --control    ARM 0: every holder of a pursuit vector gets the realm-mean vector AND the realm-mean
               `conviction` (the score projects `crisis_weights`, which scales `doctrine` by conviction,
               IN-71); since SE-06 the 37 population cohorts hold a vector too (their territory's
               temperament), so they are in the mean and are flattened to it: this arm is NOT like-for-like
               with dated readings taken while they held none, and it also writes the realm-mean `conviction` into
               cohorts that hold `{}` in shipped play (which switches on their doctrine scaling and affiliation scars); goals unseeded
               (`build_realm(goals=False)`, IN-68) AND the goals file read as empty (`no_goals()`; salience
               reads `data/goals.py::expected`). Creed stance rows keep their build-time weights. There is no
               switch for cohort temperaments off: the revert is deleting `cohorts.yaml: temperaments:`.
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

THE DECIDING TERM (`decision/choose.py::deciding_term`, the one owner; `attribute_top` scores a candidate set and calls it,
`play_season` takes it over what the chooser itself ranked), in the order it is tested:
  1. `draw`      the sampler's top is NOT the score's top (the draw outvoted the score), or the top two
                 scores are within `EPS` and `choice_temperature` > 0 (the draw ordered them). The label
                 stays one; `draw_kind` splits it: `tie` (the draw ordered a tie) against `outvoted` (the
                 draw overrode a leader). Both modes print the split, the outvoted margins' median beside
                 `choice_temperature`, and how many readings (and persons) had EVERY candidate score 0
                 (`field_zero`);
  2. `tiebreak`  the top two scores are within `EPS` at temperature 0 (`(verb, subject)` ordered them);
  3. otherwise the TERMS whose removal leaves the top no longer strictly ahead of the field (it changes, or
     collapses into a tie): `pursuit`, `stance`, `fit`, joined by `+`; `overdetermined` if no single
     term's removal does (two terms each separate it alone).
So the attribution CAN say "no state decided": two persons with nothing separating their candidates read
`draw` or `tiebreak`, never `pursuit`.

NOTHING HERE IS PINNED AS A GOLDEN. The first run of an instrument IS the baseline (Jordan, 2026-09-14);
the commit that adds a mover quotes the base and the mover's reading side by side. `harness/delta.py` and
`harness/arms.py` read no person's score and are not extended.

SEAMS AND KNOWN LIMITS (the code is the mechanism; these are what the code does not do):
  * `attribute_top` calls the chooser's own ordering (`choose.score_order`, then `choose.sample_order`)
    and its score terms (`choose.score_terms`); nothing is repeated. `test_in62_decision_spread.py` pins
    the top it returns to the real chooser's.
  * The draw is `draw_factory(world_seed, tick)` at the build's tick: a `--decisions` top is the top at that
    tick, not a distribution over ticks.
  * Absent in `--season`: a resolved act whose `(actor, verb, subject)` the watch did not see leave a
    deliberation (a re-minted id) is counted `unmapped`, printed, and not attributed.
  * `--season`'s draw split is read off the chooser's own deliberation through `make_chooser(watch=...)`
    (B09.13): the ranking, terms and sampled order the chooser used, not a second scoring of its opening set.
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

from ..data import goals as goals_data
from ..data import verbs as V
from ..data.requires import WORLD_ONLY_STEMS
from ..data.rosters import FACTION_BY_PROP, PURSUIT_AXES, faction_prop_id
from ..data.verbs import alignment_at
from ..decision import assemble, choose as CH, opening_set
from ..decision.options import project, subject_is_opponent
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..seam.wrappers.sigma import believed_odds_query
from ..state.carriers import Question, subject_of
from ..state.ids import draw_factory
from . import probes as P
from .corpus_run import attempts
from ..boot.realm import build_realm

EPS = CH.ATTRIBUTION_EPS      # the attribution's float-tie tolerance: one value, owned beside the rule that reads it (`choose.deciding_term`)
# [JUSTIFIED: the instrument's near-identical bar for a cosine between two persons' vectors (IN-64's EXIT 'pairs above 0.99'), a reading threshold and not a game number]
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


def realm_mean_conviction(w) -> dict:
    """The mean `Person.conviction` of the persons who hold one, per affiliation (a person who holds none
    is the absence of a view, as in `realm_mean_pursuits`)."""
    holders = [p for p in w.persons.values() if p.conviction]
    names = sorted({k for p in holders for k in p.conviction})
    return {k: round(sum(float(p.conviction.get(k, 0)) for p in holders) / len(holders)) for k in names}


def apply_control(w) -> dict:
    """ARM 0: every person who HOLDS a pursuit vector gets the realm-mean vector, a COPY each, and the
    realm-mean `conviction` -- the score projects `person_q.crisis_weights`, which scales `doctrine` by the
    person's own conviction (IN-71), so a control that left convictions alone would keep per-person
    variance in. A person who holds no vector (since SE-06 only a guard cohort, `build_realm(guards=True)`) is left as
    the tree has them: giving them one would move their tops from draw-decided to pursuit-decided in this arm
    only. The 37 population cohorts hold their territory's vector, so they are in the mean and flattened to
    it. Returns the mean."""
    mean = realm_mean_pursuits(w)
    conv = realm_mean_conviction(w)
    for p in w.persons.values():
        if p.pursuits:
            p.pursuits = dict(mean)
            p.conviction = dict(conv)
    return mean


@contextlib.contextmanager
def no_goals():
    """ARM 0's other half: the goals FILE read as empty for the reading. `build_realm(goals=False)` stops
    SEEDING, but `world_q.attention_key`'s salience reads `data/goals.py::expected` straight off the module
    cache, so without this the control's creed salience still sums the file's goal pursuits. Restored."""
    with goals_data.rows_replaced():
        yield


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


def attribute_top(p, cands: list, fx, draw=None, odds=None) -> dict:
    """Rank `cands` for `p` as the chooser does and say WHICH TERM decided the top: it SCORES, ORDERS and SAMPLES `cands`
    (a second scoring, for a reader that has no chooser's deliberation to watch: `read_decisions`' common set) and hands the
    result to `choose.deciding_term`, the one owner of the rule (the module docstring lists its tests in order). Returns
    `{top, decider, margin, scores, terms, draw_kind, field_zero}`; `scores` and `terms` are parallel to `cands`. `cands` empty
    -> `top` None, `decider` `none`; one candidate -> `sole`. A reading of a deliberation the chooser itself ran does not call
    this: it takes `make_chooser(watch=...)`'s lists and calls `deciding_term` (`play_season`).

    `draw_kind` SPLITS THE `draw` LABEL (the `decider` label itself is unchanged): `None` when the draw
    decided nothing; `tie` when the top two scores are within `EPS` and `choice_temperature` > 0 (the draw
    ordered them, and the sampled top is one of the tied); `outvoted` when the sampler's top is NOT the
    strict score top (the draw overrode a score that had a leader). `field_zero` is true when every
    candidate's score is within `EPS` of 0: nothing the
    person holds scores any candidate, so no state decided the top (the vectorless).

    `odds` (CR-17) is the believed-odds query a View carries (`View.odds`; `seam/wrappers/sigma.py::
    believed_odds_query`), handed to `score_terms` as the chooser hands it: `None` reads the score without
    the believed-chance factor, which is also what `odds_weighting` `none` reads whatever is passed."""
    if not cands:
        return CH.deciding_term([], [], None, 0.0)
    memo = CH.deliberation_memo(p, fx)
    terms = [CH.score_terms(p, c, fx, memo, odds) for c in cands]
    by_id = {id(c): CH.score_total(t) for c, t in zip(cands, terms)}
    ranked = CH.score_order(cands, by_id)               # the chooser's own ordering, not a second copy
    actual = CH.sample_order(ranked, lambda c: by_id[id(c)], p, fx, draw)[0]
    return CH.deciding_term(cands, terms, actual, float(fx.get("choice_temperature")))


def new_split() -> dict:
    """An empty tally of `attribute_top`'s `draw_kind` and `field_zero` (see `tally_split`)."""
    return {"read": 0, "strict": 0, "strict_outvoted": 0, "tie": 0, "outvoted": 0, "outvoted_margins": [], "field_zero": 0,
            "zero_persons": set()}


def tally_split(split: dict, pid: str, r: dict) -> None:
    """Fold one `attribute_top` result for person `pid` into `split`: one reading counted, the draw's kind
    counted (an outvoted top keeps its margin: the leader's lead over the runner-up, `best - second`, which is
    a LOWER BOUND on the gap the draw overcame, larger when the drawn top is a third or lower candidate),
    a `field_zero` reading counted and its person remembered. `strict` counts the readings whose leader leads
    the runner-up by more than `EPS` (a sole candidate has no runner-up), the readings that HAVE a leader for
    the draw to pass over; `strict_outvoted` is the `outvoted` among them (`outvoted` alone also counts a
    pick below a tied pair at the top, which has no strict leader to be "not the top candidate"). A reading with no candidate (`decider` `none`) is not a reading."""
    if r["decider"] == "none":
        return
    split["read"] += 1
    if r["margin"] is not None and r["margin"] > EPS:
        split["strict"] += 1
        split["strict_outvoted"] += r["draw_kind"] == "outvoted"
    if r["draw_kind"]:
        split[r["draw_kind"]] += 1
    if r["draw_kind"] == "outvoted":
        split["outvoted_margins"].append(r["margin"])
    if r["field_zero"]:
        split["field_zero"] += 1
        split["zero_persons"].add(pid)


def split_figures(split: dict) -> dict:
    """The printable figures of a tally: counts, the outvoted margins' median (None when none), and the
    distinct persons with a `field_zero` reading."""
    m = split["outvoted_margins"]
    return {"read": split["read"], "strict": split["strict"],
            "strict_outvoted": split["strict_outvoted"], "tie": split["tie"], "outvoted": split["outvoted"],
            "outvoted_median_margin": statistics.median(m) if m else None,
            "field_zero": split["field_zero"], "zero_persons": len(split["zero_persons"])}


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


def territory_of(w, pid: str, homes: Optional[dict] = None) -> str:
    """The first TERRITORY rung on the person's home ancestry (`world_q.enclosing_territory`, the one walk);
    their home rung itself when none is a territory. `homes` is `world_q.home_of(w)` where the caller
    already holds it (a loop over persons), else it is read here -- the map is a scan of every tenure."""
    home = (world_q.home_of(w) if homes is None else homes).get(pid)
    if home is None:
        return "-"
    return world_q.enclosing_territory(w, home) or home


def profile_key(w, p) -> tuple:
    """The FULL profile: 15-vector to 2 dp, affiliation vector, factions committed to, goal-commit set."""
    pur = tuple(round(float(p.pursuits.get(n, 0.0)), 2) for n in PURSUITS)
    aff = tuple(sorted((k, v) for k, v in (p.conviction or {}).items()))
    commits = sorted(t.object for t in p.tenures if t.kind == "commit" and t.live)
    fac = tuple(o for o in commits if o in w.propositions and o in FACTION_BY_PROP)
    # ORG GOALS ONLY: each cast person's own want (`prop_<cid>`) is unique to them, so counting it would make
    # every two persons with a want differ by construction and the identical-profile reading vacuous.
    goals = tuple(o for o in commits if o not in fac and goals_data.goal(o) is not None)
    return (pur, aff, fac, goals)


def _pair_cosines(vecs: dict, ids: list) -> list:
    """The cosine of every pair among `ids`, in `ids` order; a pair with a zero vector is left out."""
    return [c for i, a in enumerate(ids) for b in ids[i + 1:] if (c := _cosine(vecs[a], vecs[b])) is not None]


def read_persons(w) -> dict:
    """The `--persons` figures on a built realm (no season is played)."""
    w._rehome()
    fx = w.fixtures
    ids = sorted(w.persons)
    vecs = {pid: projected_vector(w.persons[pid], fx) for pid in ids}
    live = [pid for pid in ids if any(vecs[pid])]
    cos = _pair_cosines(vecs, live)
    mean = [sum(vecs[pid][k] for pid in live) / len(live) for k in range(len(PURSUIT_AXES))] if live else []
    to_mean = [c for pid in live if mean and (c := _cosine(vecs[pid], mean)) is not None]
    # THE CAST ALONE (SE-06): cohorts of equal temperament ratio hold the same vector by declaration, so `pairs_above` over all
    # persons with a vector counts those pairs too; the cast's own reading is the one IN-62's EXIT bounds.
    cast_live = [pid for pid in live if not w.persons[pid].is_cohort]
    cast_cos = _pair_cosines(vecs, cast_live)
    groups: dict = {}
    for pid in ids:
        groups.setdefault(profile_key(w, w.persons[pid]), []).append(pid)
    identical = {k: v for k, v in groups.items() if len(v) > 1}
    cohorts: dict = {}
    homes = world_q.home_of(w)
    for pid in ids:
        if w.persons[pid].is_cohort:
            cohorts.setdefault(territory_of(w, pid, homes), []).append(pid)
    return {
        "persons": len(ids), "cast": sum(1 for pid in ids if not w.persons[pid].is_cohort),
        "cohorts": sum(1 for pid in ids if w.persons[pid].is_cohort),
        "zero_vector": len(ids) - len(live), "with_vector": len(live), "cast_with_vector": len(cast_live),
        "pairs": len(cos), "pairs_above": sum(1 for c in cos if c > COSINE_HIGH),
        "pairs_above_cast": sum(1 for c in cast_cos if c > COSINE_HIGH),
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
        if pid_ not in FACTION_BY_PROP or prop.subject not in w.persons or prop.subject in seen:
            continue
        seen.add(prop.subject)
        out.append(("King (" + pid_ + ")" if pid_ == faction_prop_id("Valorsmark") else pid_, prop.subject))
    return out


def decision_question(referent: str) -> Question:
    """A `claim_landed`-shaped question about `referent`, the form `questions_for` stamps for a landed
    claim (`world_q.py`'s `questions_for` `claim_landed` Question), with an id that names this reading."""
    return Question(f"q:claim:spread:{referent}", "claim_landed", (referent,), f"claim:spread:{referent}")


def formed_set(w, p, q, foldable=None) -> list:
    """`p`'s opening set for `q`, formed as `corpus_run.py:958-960` forms it, narrowed to the verbs the
    fold resolves (the chooser's own `verbs=`; `foldable` where the caller already holds the set)."""
    view = assemble(p, q, w.fixtures.get("view_k"))
    foldable = resolvable_verbs() if foldable is None else foldable
    return [c for c in opening_set(p, view, q, w.fixtures) if c.verb in foldable]


def is_self_plea(c, actor: str) -> bool:
    """WHETHER CANDIDATE `c` IS A SELF-PLEA by `actor`: an act contested against its subject (`options.subject_is_opponent`)
    whose subject is the actor himself. `opening_set` forms one only on a row declaring `subject_may_be_self` (`speak`);
    `choose.py`'s polarity (`subject != p.id`) reads the same split. A candidate whose subject is the actor on a row NOT
    contested against its subject (the referent's own `move`, `train`, ...) is no plea, so the key does not split it: a bare
    `c.subject == actor` marks every row the referent himself forms and leaves the common set empty."""
    row = V.VERB_TABLE.get(c.verb)
    return c.subject == actor and row is not None and subject_is_opponent(row)


def read_decisions(w) -> dict:
    """The `--decisions` figures on a built realm (no season is played). Per referent: the persons handed
    the question, those who form any candidate, the common set (intersection of those), the number of
    distinct tops, and the deciding-term counts."""
    w._rehome()
    fx = w.fixtures
    draw = draw_factory(w.world_seed, lambda: w.tick)
    rows = []
    foldable = resolvable_verbs()
    total = new_split()
    for label, ref in common_referents(w):
        q = decision_question(ref)
        split = new_split()
        formed = {pid: formed_set(w, p, q, foldable) for pid, p in sorted(w.persons.items())}
        keyed = {pid: {(c.verb, c.subject, is_self_plea(c, pid)): c for c in cs} for pid, cs in formed.items() if cs}
        common = set.intersection(*(set(k) for k in keyed.values())) if keyed else set()
        tops: dict = {}
        deciders: Counter = Counter()
        order = sorted(common, key=lambda k: (k[0], k[1] or ""))
        for pid in keyed:
            cands = [keyed[pid][k] for k in order]
            r = attribute_top(w.persons[pid], cands, fx, draw,
                              believed_odds_query(w, w.persons[pid]))   # CR-17: the query his View carries
            deciders[r["decider"]] += 1
            tally_split(split, pid, r)
            tally_split(total, pid, r)
            tops[pid] = (r["top"].verb, r["top"].subject, is_self_plea(r["top"], pid)) if r["top"] else None
        by_faction: dict = {}
        for pid, top in tops.items():
            fac = world_q.faction_holding(w, pid)
            if fac is not None and top is not None:
                by_faction.setdefault(fac, set()).add(top)
        rows.append({"referent": label, "handed": len(formed), "forming": len(keyed),
                     "common": len(common), "distinct_tops": len({t for t in tops.values() if t is not None}),
                     "faction_tops": sum(len(v) for v in by_faction.values()),
                     "deciders": dict(deciders), "tops": tops, "split": split_figures(split)})
    return {"rows": rows, "split": split_figures(total), "tau": float(fx.get("choice_temperature"))}


# ---------------------------------------------------------------------------------------------
# --season


def goal_class(q) -> str:
    """The one classifier of a question's goal class: for a `need` question, `own want` (about a
    `prop_` Proposition), `creed` (about a faction's Proposition), the org goal's id (a goal in
    `goals_data`) or `other need`; `-` for a non-`need` source. `play_season` calls it, and
    `harness/aperture.py::class_label` calls it. No second classifier is written."""
    if q.source != "need":
        return "-"
    if q.about.startswith("prop_"):
        return "own want"
    if q.about in FACTION_BY_PROP:
        return "creed"
    return q.about if goals_data.goal(q.about) is not None else "other need"   # an org goal, by id


def play_season(w, seasons: int = 1) -> dict:
    """Play `seasons` seasons through `populated.run`'s composition with the chooser WATCHED, never
    steered, and read what each person did and which question they answered.

    WHAT "DID" MEANS (HR-8): the acts the fold RESOLVED (`d.resolved`), not the acts EXECUTED (made, in
    `corpus_run._attribute_acts`'s made/refused rule) and not the acts ATTEMPTED (`corpus_run.attempts`,
    the act store). The `acts` count, the verb multisets and `per_act` all read the fold set: an act that
    entered the fold and was refused there is in them, and a contested act refused at admission, which
    never enters `d.resolved`, is not."""
    d = SeasonDriver(w)
    tau = float(w.fixtures.get("choice_temperature"))
    split = new_split()                    # every deliberation's `draw_kind` / `field_zero`, read beside the chooser
    answered: Counter = Counter()          # (source, goal class) -> deliberations
    by_act: dict = {}                      # (actor, verb, subject) -> (source, goal class)
    heard: list = []                       # the key of the deliberation the hook just reported (empty: it had no question)

    def watch(p, q, ranked, terms, sampled):
        # `make_chooser`'s observer hook: what the chooser itself ranked, scored and sampled (B09.13). Nothing is
        # scored again and nothing is steered; `choose.deciding_term` is the one owner of the attribution rule.
        tally_split(split, p.id, CH.deciding_term(ranked, terms, sampled[0] if sampled else None, tau))
        key = (q.source, goal_class(q))
        answered[key] += 1
        heard.append(key)

    real = P.chooser(w, verbs=resolvable_verbs(), watch=watch)

    def watched(p, v, s, ask_budget):
        # only to see the SCENES the chooser returned (the hook is handed the ranking, not the acts packed from it)
        heard.clear()
        scenes = real(p, v, s, ask_budget)
        if heard:
            for sc in scenes:
                for a in sc.acts:
                    by_act[(p.id, a.verb, subject_of(a))] = heard[0]
        return scenes

    for _ in range(seasons):
        d.season(watched, question=None,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    multisets: dict = {}
    per_act: Counter = Counter()
    unmapped = 0
    for a in d.resolved:
        multisets.setdefault(a.actor, Counter())[a.verb] += 1
        key = by_act.get((a.actor, a.verb, subject_of(a)))
        if key is None:
            unmapped += 1
        else:
            per_act[key] += 1
    sigs = Counter(tuple(sorted(c.items())) for c in multisets.values())
    return {"seasons": seasons, "acts": len(d.resolved), "actors": len(multisets),
            "distinct_multisets": len(sigs), "largest_shared": max(sigs.values(), default=0),
            "answered": dict(answered), "per_act": dict(per_act), "unmapped": unmapped,
            "split": split_figures(split), "tau": float(w.fixtures.get("choice_temperature")),
            "hash": w.content_hash()}


# ---------------------------------------------------------------------------------------------
# --retries


RETRY_CLASSES = ("world-only", "unobserved", "taught")


def refusal_class(events: list) -> str:
    """THE CLASS OF ONE REFUSED ATTEMPT, by what the fold recorded on its refusal Event (`Event.observed`: the reads the fold made, the
    last of which decided). `unobserved` -- the Event holds no read; `world-only` -- the last read's stem is one a ledger never answers
    (`data/requires.py::WORLD_ONLY_STEMS`, `with` chiefly, which `loop/witness.py` rules *"observed, never deposited"*); `taught`
    otherwise (a read WITNESS deposits, so the teaching channel reaches it). The first two are the classes outside that channel."""
    obs = tuple(events[0].observed or ()) if events else ()
    if not obs:
        return "unobserved"
    return "world-only" if obs[-1].predicate.partition(":")[0] in WORLD_ONLY_STEMS else "taught"


def retry_attempts(w, d, season_ends: list) -> list:
    """`[{"season", "actor", "verb", "subject", "cohort", "refused", "ok", "class", "key"}]` -- EVERY ATTEMPT, in resolution order: every act
    that entered RESOLVE (the act store, `corpus_run.attempts`, not only the acts the fold resolved), one row per act whose verb is a
    table row. `refused` is True when a kind of the row's `emits_on_refusal` stands in the log for it (`corpus_run`'s one made/refused
    rule); `ok` when it is not refused and an `emits` kind of the row stands there. A graded loss (a lost `examine`, whose refusal
    kind is also an `emits` kind) is REFUSED here. `season_ends[i]` is `len(w.acts)` after season `i`, so an act's season is read off
    its position in the store. The OPPORTUNITY an attempt belongs to is `key = (actor, verb, subject)`."""
    refusals: dict = {}
    for e in w.log:
        a = d.act_of.get(e.id)
        if a is not None:
            refusals.setdefault(a.id, []).append(e)
    place = {a.id: j for j, a in enumerate(w.acts)}
    out = []
    for a, made, refused in attempts(w, len(season_ends)):
        season = next(k for k, end in enumerate(season_ends) if place[a.id] < end)
        evs = [e for e in refusals.get(a.id, ()) if e.kind in refused]
        out.append({"season": season, "actor": a.actor, "verb": a.verb, "subject": subject_of(a),
                    "cohort": a.actor in w.persons and w.persons[a.actor].is_cohort,
                    "refused": bool(refused), "ok": bool(made) and not refused,
                    "class": refusal_class(evs) if refused else "", "key": (a.actor, a.verb, subject_of(a))})
    return out


def retry_rows(attempts_: list, seasons: int) -> dict:
    """THE FIVE ROWS' FIGURES from `retry_attempts`' rows (a pure function, so a test may hand it rows), over INDIVIDUALS (`Person.weight == 1`;
    a cohort's act is a mass and not a person's choice):

      (b) `again[class]` -- of the REFUSED attempts of each class, how many have a LATER attempt on the same opportunity (the source's "41%
          of refused opportunities are attempted again by the same person"); `again_ok` the same over the EXECUTED attempts, the control
          the source's bar names ("about 20%");
      (c) `share[season]` -- the refusal share of acts: attempts refused over all attempts, per season (C3-N13: acts by individuals, not
          cohorts, refused, over all acts by individuals);
      (d) `stuck_pairs`, `stuck_acts` -- `(actor, verb)` pairs attempted three or more times and refused EVERY time, and their acts;
      (e) `retries_ok` -- attempts that succeed on an opportunity refused at an EARLIER attempt."""
    solo = [r for r in attempts_ if not r["cohort"]]
    last_at: dict = {}
    first_refused: dict = {}
    for j, r in enumerate(solo):
        last_at[r["key"]] = j
        if r["refused"]:
            first_refused.setdefault(r["key"], j)
    again = {c: [0, 0] for c in RETRY_CLASSES}
    again_ok = [0, 0]
    for j, r in enumerate(solo):
        later = last_at[r["key"]] > j
        if r["refused"]:
            again[r["class"]][1] += 1
            again[r["class"]][0] += later
        elif r["ok"]:
            again_ok[1] += 1
            again_ok[0] += later
    share = []
    for s in range(seasons):
        mine = [r for r in solo if r["season"] == s]
        share.append((sum(r["refused"] for r in mine), len(mine)))
    pairs: dict = {}
    for r in solo:
        pairs.setdefault((r["actor"], r["verb"]), []).append(r["refused"])
    stuck = [v for v in pairs.values() if len(v) >= 3 and all(v)]
    return {"again": {c: tuple(v) for c, v in again.items()}, "again_ok": tuple(again_ok), "share": share,
            "stuck_pairs": len(stuck), "stuck_acts": sum(len(v) for v in stuck),
            "retries_ok": sum(1 for j, r in enumerate(solo) if r["ok"] and first_refused.get(r["key"], j) < j)}


def play_retries(seed: int, seasons: int) -> dict:
    """THE FIVE READINGS of `16_PESSIMIST_CORE_a_refusal_is_remembered` ("Gate") over `seasons` seasons of `build_realm(seed)`, played as
    `populated.run` plays them (so a content hash here is the one the plan's HASH READING prints), the chooser watched by nobody.

      (a) the CONTROL ARM's content hash, `refusal_memory = 0.0` (the factor is exactly 1.0), beside the shipped arm's;
      (b) refused opportunities attempted again, the world-only and unobserved classes (`refusal_class`), against the executed-act control;
      (c) individuals' refusal share of acts, by season; (d) `(actor, verb)` pairs attempted three or more times and refused every time;
      (e) retries that succeed -- (b) to (e) by `retry_rows`, over the SHIPPED arm."""
    def play(control: bool):
        w = build_realm(seed)
        if control:
            w.fixtures = w.fixtures.sweep("refusal_memory", 0.0)
        d = SeasonDriver(w)
        ch = P.chooser(w, verbs=resolvable_verbs())
        ends = []
        for _ in range(seasons):
            d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
            ends.append(len(w.acts))
        return w, d, ends

    w, d, ends = play(False)
    control = play(True)[0]
    out = retry_rows(retry_attempts(w, d, ends), seasons)
    out.update({"seed": seed, "seasons": seasons, "attempts": len(w.acts), "hash": w.content_hash(),
                "control_hash": control.content_hash()})
    return out


def print_retries(r: dict) -> None:
    def pct(k: int, n: int) -> str:
        return "-" if n == 0 else f"{100.0 * k / n:.1f}% ({k} of {n})"
    ag = r["again"]
    unteachable = (ag["world-only"][0] + ag["unobserved"][0], ag["world-only"][1] + ag["unobserved"][1])
    print(f"--retries  seed {r['seed']}, {r['seasons']} SEASON(S), {r['attempts']} attempts in the act store")
    print(f"  (a) control arm [refusal_memory = 0.0] content_hash {r['control_hash']}; shipped arm {r['hash']}")
    print(f"  (b) refused opportunities attempted again, world-only and unobserved classes: {pct(*unteachable)} "
          f"[world-only {pct(*ag['world-only'])}; unobserved {pct(*ag['unobserved'])}]; "
          f"control, executed acts' opportunities attempted again: {pct(*r['again_ok'])}; taught class {pct(*ag['taught'])}")
    print("  (c) individuals' refusal share of acts: " + "; ".join(f"season {i} {pct(*v)}" for i, v in enumerate(r["share"])))
    print(f"  (d) (actor, verb) pairs of individuals attempted 3+ times and refused every time: "
          f"{r['stuck_pairs']} pairs, {r['stuck_acts']} acts")
    print(f"  (e) retries that succeed (executed, on an opportunity refused at an earlier attempt): {r['retries_ok']}")


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
    print(f"  among the cast alone ({r['cast_with_vector']} with a vector): above {COSINE_HIGH}: "
          f"{r['pairs_above_cast']}")
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
    print("  referent                         handed forming common distinct-tops faction-tops  deciding term (persons)")
    for row in r["rows"]:
        dec = ", ".join(f"{k} {v}" for k, v in sorted(row["deciders"].items()))
        print(f"  {row['referent']:32} {row['handed']:5} {row['forming']:7} {row['common']:6} "
              f"{row['distinct_tops']:13} {row['faction_tops']:12}  {dec}")
    tot = _decider_total(r)
    print(f"  all referents: {dict(sorted(tot.items()))}; distinct tops {sum(r_['distinct_tops'] for r_ in r['rows'])}"
          f"; distinct tops within a faction, summed over its factions {sum(r_['faction_tops'] for r_ in r['rows'])}")
    print_split(r["split"], r["tau"])


def print_split(sp: dict, tau: float) -> None:
    """The draw split and the vectorless count (`attribute_top`'s `draw_kind` and `field_zero`). The
    `draw` label's two halves: a `tie` the draw ordered, an `outvoted` score leader the draw overrode."""
    med = _fmt(sp["outvoted_median_margin"])
    print(f"  the draw's {sp['tie'] + sp['outvoted']} tops, split: tie {sp['tie']}, outvoted {sp['outvoted']}; "
          f"outvoted margins' median {med} against choice_temperature {tau:g}")
    print(f"  every candidate scores 0: {sp['field_zero']} of {sp['read']} readings, "
          f"{sp['zero_persons']} distinct persons")


def print_season(r: dict, arm: str) -> None:
    print(f"--season [{arm}]  PLAYS {r['seasons']} SEASON(S)")
    print(f"  acts {r['acts']} by {r['actors']} actors; distinct per-person resolved verb multisets "
          f"{r['distinct_multisets']} (largest shared by {r['largest_shared']} persons)")
    print("  answered question (source / goal class): deliberations")
    for k, v in sorted(r["answered"].items()):
        print(f"    {k[0]:14} {k[1]:10} {v}")
    print("  resolved acts by the question answered: "
          + ", ".join(f"{k[0]}/{k[1]} {v}" for k, v in sorted(r["per_act"].items()))
          + f"; unmapped {r['unmapped']}")
    print_split(r["split"], r["tau"])
    # k = the deliberations whose pick was not the strict leader, n = the deliberations with a strict top (`tally_split`)
    print(f"  not the top candidate: {r['split']['strict_outvoted']} of {r['split']['strict']}")
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
    ap.add_argument("--retries", action="store_true", help="PLAYS --seasons seasons: the five readings of a remembered refusal")
    ap.add_argument("--seasons", type=int, default=2, help="seasons --retries plays (default 2)")
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args(argv)
    if a.retries:
        if a.arms or a.control or a.null or a.persons or a.decisions or a.season:
            ap.error("--retries is its own mode: it takes no other reading or arm flag")
        print_retries(play_retries(a.seed, a.seasons))
        return 0
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
              "`goals.yaml` carries rows since FA-05, FA-06); the population cohorts are flattened to the mean too (SE-06; see `--control` in --help)")
    with (null_alignment() if a.null else contextlib.nullcontext()), \
            (no_goals() if a.control else contextlib.nullcontext()):
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
