"""`harness.invariants` — the season's RUN-TIME invariants, as predicates over a finished World.

WHAT THIS IS FOR. `tools/m1_acceptance.py` row 5 is *"N seeds, zero invariant violations"*, and
it has been `blocked` since the gate was written, on *"property-based tests (Hypothesis) over a
season run"*. This is that row's instrument. It is the ONE owner of what a season must not have
done; `m1_acceptance` and `tests/valoria/test_season_invariant_sweep.py` both call it rather than
each keeping a battery (§8).

⚠⚠ **THE SELECTION RULE IS THE WHOLE DESIGN, AND IT EXCLUDES MOST OF WHAT LOOKS LIKE AN
INVARIANT.** `World.add_tenure` already refuses a `Tenure` whose `kind` is off the roster and a
`contain` edge that does not ascend the rung ladder — it raises at WRITE. So asserting either
here would be `pytest.approx` on an exactness claim: *"not a weak test but an absent one"*
(`CLAUDE.md` §0.1 pt 2). An invariant earns a row below only if **nothing in the tree enforces it
on write**, so a season really can produce a World that violates it. Every predicate here was
checked against its constructor before being written, and every one is mutation-verified in
`test_season_invariant_sweep.py` — a predicate that cannot be made to fire is deleted, not kept
for completeness.

⚠ **WHY NOT `hypothesis`, WHICH ROW 5 NAMES.** It is not a dependency anywhere in this tree and
CI's `unit-tests` job installs only `pyyaml pytest numpy pytest-xdist`
(`.github/workflows/valoria-ci.yml`), so a new third-party import in a blocking-gate test file
would collect-error the whole job. `tests/valoria/test_dice_engine_properties.py` hit this first
and set the precedent: the property-testing METHOD (many seeds, one invariant, reproducible)
without the dependency. Row 5's `unblocked_by` string names the library because that is how the
technique is usually spelled; what it is actually asking for is the sweep.

⚠ **THIS REPORTS, IT DOES NOT RAISE.** A violation is a finding about the season loop, and an
instrument that dies on the first one cannot tell you whether there is one or forty. Callers
decide what a non-empty list means.
"""
from __future__ import annotations

import inspect as _inspect
from collections import Counter

# §F2's stance row is `(referent, valence -5..+5, weight 0..5)` (#353 `:333`). The bound is the
# row type's, single-owned where the loyalty translation reads it.
from ..data.cast import STANCE_VALENCE_SCALE

#: Every invariant's id, in report order. A stable roster so a caller can name one.
INVARIANTS = (
    "tenure_interval",
    "tenure_referent",
    "log_ids_unique",
    "log_not_from_the_future",
    "claim_not_from_the_future",
    "body_in_range",
    "stance_row_shape",
    "office_singly_held",
)


def _entities(w) -> set:
    """Everything a Tenure or Proposition may legitimately name.

    ⚠⚠ **THIS SET WAS WRONG ON ITS FIRST WRITING AND THE ERROR IS RECORDED RATHER THAN QUIETLY
    PATCHED, BECAUSE IT IS THE FAILURE MODE THIS WHOLE MODULE IS EXPOSED TO.** It omitted
    `w.records`, and the first sweep duly reported **176 violations across 24 seeds** — a
    headline number, mostly `live hold ... names 'rec:...' which is no person, rung, office,
    proposition or site`. Every one of those was manufactured by the predicate. A Record is a
    thing a person HOLDS — a deed, a writ — so a `hold` edge naming one is the carrier working
    exactly as designed.
    
    An invariant sweep's characteristic failure is not missing a defect; it is inventing a
    hundred, because a predicate that is slightly too narrow fires on every healthy row and looks
    like a discovery. The guard against it is that the entity set is enumerated from `World`'s own
    `__init__` (`state/world.py:151-166`) rather than from what came to mind, and
    `test_the_entity_set_covers_every_world_collection_a_tenure_can_name` pins it there so a
    collection added later cannot silently start reading as dangling."""
    return (set(w.persons) | set(w.rungs) | set(w.offices) | set(w.propositions)
            | set(w.sites) | set(w.records) | set(w.dates)
            | set(w.petitions) | set(w.dispensations))


def _all_tenures(w) -> list:
    """Every Tenure in the world. `World.tenures` is the single owner; this only names it.

    ⚠⚠ **THIS FUNCTION USED TO MERGE THE TWO STORES BY HAND, AND THE COMMENT JUSTIFYING THAT WAS
    FALSE.** It read `list(w.tenures) + list(w._unowned)` with an `id()`-keyed dedup, and claimed
    *"a sweep reading only `w.tenures` would examine the person-owned half and report zero
    violations for the other"*. `World.tenures` (`state/world.py:186-194`) already calls
    `_rehome()` and then extends with `self._unowned` — so the hand-merge double-added every
    unowned Tenure and survived **only** because of the dedup pass, which is direct evidence the
    duplication was never checked against the property it was working around. §8: the rule lives
    once, and it already lived in `World`.

    Kept as a named function rather than inlined because three predicates share it and
    `violations()` computes it once for all of them."""
    return list(w.tenures)


def tenure_interval(w, tenures=None) -> list:
    """An ended Tenure ended no earlier than it began.

    NOT ENFORCED ON WRITE: `add_tenure` checks `kind` and ladder ascent and never looks at
    `since`/`until`, and `until` is set by whatever ends the tenure, long after the write. A
    negative interval makes `live` and every `since`-ordered read disagree about what happened."""
    bad = []
    for t in (_all_tenures(w) if tenures is None else tenures):
        if t.until is not None and t.until < t.since:
            bad.append(f"tenure_interval: {t.id!r} ends at {t.until} but began at {t.since}")
    return bad


def tenure_referent(w, tenures=None) -> list:
    """A live Tenure names things that exist on both ends.

    NOT ENFORCED ON WRITE: `add_tenure` indexes `self.rungs[...]` only inside the `contain`
    branch, so a `hold`, `commit`, `oblige`, `succeed`, `tie` or `knot` edge to an id naming
    nothing is accepted in silence. That is how `leaders()` can read an office nobody has and
    return a plausible empty list — the defect shape this repository has already met twice."""
    ents, bad = _entities(w), []
    for t in (_all_tenures(w) if tenures is None else tenures):
        if not t.live:
            continue
        for end, who in (("subject", t.subject), ("object", t.object)):
            if who not in ents:
                bad.append(f"tenure_referent: live {t.kind} {t.id!r} names {who!r} as its "
                           f"{end}, which is no person, rung, office, proposition or site")
    return bad


def log_ids_unique(w) -> list:
    """No two Events share an id.

    NOT ENFORCED ON WRITE: the log is a plain append. `probes.py` records the real occurrence —
    *"person in one tick shared ONE ID"* — where an id minted from `(seed, tick, ...)` collided
    because the varying term was left out. A duplicate id makes `causes[]` ambiguous, so every
    provenance walk over the log silently follows the wrong edge."""
    dupes = [k for k, n in Counter(e.id for e in w.log).items() if n > 1]
    return [f"log_ids_unique: event id {k!r} appears more than once" for k in sorted(dupes)]


def log_not_from_the_future(w) -> list:
    """No Event is stamped after the world's own clock.

    NOT ENFORCED ON WRITE: `emitted_at` is supplied by the emitter and never compared to
    `w.tick`. An Event from the future is how a non-decreasing season index stops being one —
    the invariant `probes.py` names as one of the three a per-container clock would void."""
    return [f"log_not_from_the_future: event {e.id!r} emitted_at={e.emitted_at} > tick {w.tick}"
            for e in w.log if e.emitted_at > w.tick]


def claim_not_from_the_future(w) -> list:
    """No Claim in any ledger is stamped after the world's own clock.

    NOT ENFORCED ON WRITE: a Claim is appended to `Person.ledger` directly. This one is
    load-bearing on DELIBERATION rather than on bookkeeping: `questions_for`'s `since` selects
    claims by `(when, round)`, so a claim from the future is permanently new and raises its Q2
    question every season forever."""
    bad = []
    for p in w.persons.values():
        for c in p.ledger:
            if c.when > w.tick:
                bad.append(f"claim_not_from_the_future: {p.id}'s claim {c.id!r} "
                           f"when={c.when} > tick {w.tick}")
    return bad


def body_in_range(w) -> list:
    """A person's body sits on the fixed-point scale `Site.condition` uses, `[0, scale]`.

    NOT ENFORCED ON WRITE: `Person.body` is a plain field with a default; nothing clamps it. Its
    docstring is explicit that the scale is `condition_scale` and NOT a literal 1000, so the bound
    is read from the fixtures here rather than retyped (`G1`)."""
    scale = w.fixtures.get("condition_scale")
    return [f"body_in_range: {p.id} body={p.body} outside [0, {scale}]"
            for p in w.persons.values() if not (0 <= p.body <= scale)]


def stance_row_shape(w) -> list:
    """Every stance row is `(referent, valence -5..+5, weight 0..5)`.

    NOT ENFORCED ON WRITE: `Person.stance` is a `list[tuple]` and `stance_toward` reads
    `row[1] * row[2]` off whatever is there. A malformed row does not raise — it silently
    contributes a wrong term to every candidate naming that referent."""
    lim, bad = STANCE_VALENCE_SCALE, []
    for p in w.persons.values():
        for row in p.stance:
            if len(row) < 3:
                bad.append(f"stance_row_shape: {p.id} has a stance row of length {len(row)}")
                continue
            _, val, wt = row[0], row[1], row[2]
            if not (-lim <= val <= lim):
                bad.append(f"stance_row_shape: {p.id} valence {val} outside [-{lim}, +{lim}]")
            if not (0 <= wt <= lim):
                bad.append(f"stance_row_shape: {p.id} weight {wt} outside [0, {lim}]")
    return bad


# ⚠⚠ **`ought_names_an_entity` WAS THE NINTH PREDICATE AND IT IS DELETED. IT WAS WRONG, AND WHAT
# IT MISLABELLED AS A DEFECT IS THE PROBE WORLD'S ENTIRE MOTIVE.**
#
# It asserted that every OUGHT Proposition's subject must name an entity, citing `ED-IN-0210`
# Ruling 1 (*"verbs invoke mechanisms or interactions between a character and another
# entity/character"*) and `build_at`'s measured **0 of 4,870 acts naming another person**. It
# fired 40 times across 24 headless seeds, on `headless.py`'s `prop_einhir` — subject
# `einhir_texts`, a bare string — and on the Propositions the loop mints from it.
#
# **MEASURED, and this is the number that settled it:** patch `loop/deliberate.questions_for` to
# drop any `need` question whose referent names no entity — the narrowest repair that would have
# satisfied the predicate — and **acts go to 0 on every seed tested** (45, 40, 38, 37, 42, 41 →
# 0, 0, 0, 0, 0, 0), with 120 questions dropped. `headless.py` says why in its own comment:
# *"Q4 is the only reason she acts."* Carin's standing ambition is `the Einhir texts should
# survive` — a belief about a THING, deliberately — and the whole probe world hangs off it.
#
# So the corpus supports a topic-subjected Proposition and the predicate forbade it. What
# `ED-IN-0210` and F8 actually forbid is narrower and is still checked: F8 reverted `_eff_oblige`
# for **opening a Tenure** to a non-entity, which is `tenure_referent` above, and `build_at`'s
# defect was a Proposition subjected on a RUNG — an entity of the wrong KIND, not a topic.
#
# ⚠ **IT IS DELETED RATHER THAN DEMOTED TO A WARNING, ON THIS MODULE'S OWN RULE.** A predicate
# kept as "declared × 24, new × 16" would be a permanent non-zero that trains the next reader to
# skim the report — and a sweep nobody reads is worse than one that does not exist. The
# `DECLARED` map went with it: its only entry existed to excuse this predicate.
#
# ⚠ **THIS IS THE SECOND TIME THIS MODULE OVER-FIRED, WHICH IS THE POINT WORTH CARRYING FORWARD.**
# First `_entities` omitted `w.records` and invented 136 violations; then this predicate
# criminalised the probe world's motive. Both were caught by measuring what the "fix" would cost
# rather than by re-reading the predicate. **An invariant sweep must be falsified against the
# ENGINE, not only against a mutated world:** a mutation proves a predicate CAN fire, and only an
# experiment on the real loop proves it SHOULD.


def office_singly_held(w, tenures=None) -> list:
    """No Office is held by two people at once.

    NOT ENFORCED ON WRITE: nothing looks at the other `hold` edges when one is added. §11 makes
    an Office a SEAT — it has `conferral`, `revocation` and an upkeep — and a seat two people
    occupy is the scarcity defect this repository has already shipped once, where every person
    got an office and `leaders() == members()` for all eight factions."""
    held = Counter(t.object for t in (_all_tenures(w) if tenures is None else tenures)
                   if t.kind == "hold" and t.live and t.object in w.offices)
    return [f"office_singly_held: office {oid!r} is held by {n} people at once"
            for oid, n in sorted(held.items()) if n > 1]


#: id -> predicate. The roster above fixes the order; this is the dispatch.
CHECKS = {name: globals()[name] for name in INVARIANTS}

#: Which predicates accept the shared Tenure list `violations()` builds once per world.
_TAKES_TENURES = {name: "tenures" in _inspect.signature(fn).parameters
                  for name, fn in CHECKS.items()}


def carrier_census(w) -> dict:
    """How many ROWS each predicate actually had to look at. The anti-vacuity term.

    ⚠⚠ **`checked` USED TO COUNT PREDICATES OFFERED, WHICH CANNOT SEE THE FAILURE IT EXISTS FOR.**
    `sweep` reported `checked += len(INVARIANTS)` — 8 per seed, whether or not any of the eight
    had a single row to inspect. MEASURED 2026-09-15: the `headless` world the milestone gate
    sweeps contains **0 Offices and 0 stance rows**, so `office_singly_held` and
    `stance_row_shape` quantified over collections that are EMPTY BY CONSTRUCTION and reported
    clean forever. A count of predicates offered says "8 checks ran"; a count of rows says
    "offices: 0", which is the difference between a clean result and an unasked question.

    That is the ED-MB-0042 shape this module's own header disclaims, reproduced inside the term
    written to prevent it — so the term now counts the thing it claimed to."""
    return {
        "tenures": len(_all_tenures(w)),
        "events": len(w.log),
        "claims": sum(len(p.ledger) for p in w.persons.values()),
        "persons": len(w.persons),
        "stance_rows": sum(len(p.stance) for p in w.persons.values()),
        "offices": len(w.offices),
        "propositions": len(w.propositions),
    }


def violations(w) -> list:
    """Every invariant violation in `w`, in `INVARIANTS` order. Empty is the healthy answer.

    The shared Tenure list is built ONCE here and handed to the three predicates that read it,
    rather than each rebuilding it — `violations` runs once per seed and the gate sweeps 24, so
    the hand-rebuild was 72 full walks where 24 do."""
    tenures = _all_tenures(w)
    out = []
    for name in INVARIANTS:
        fn = CHECKS[name]
        out.extend(fn(w, tenures) if _TAKES_TENURES.get(name) else fn(w))
    return out


#: (invariant, offending id) -> the citation that declares it. A KNOWN violation, never a
#: silenced one: `sweep` routes a declared hit to `declared` rather than dropping it, so the count
#: stays visible, and every entry must cite a register row.
#:
#: ⚠ **EMPTY, AND THAT IS A RESULT RATHER THAN AN UNUSED FEATURE.** Its one entry excused
#: `ought_names_an_entity` on `prop_einhir`. That predicate is deleted (see above) because the
#: thing it flagged is the probe world's designed motive, so the exception it needed went with it.
#: The mechanism stays because the next real declared exception should not have to reinvent it —
#: and because an empty map is the honest state when every predicate reports clean on its own.
DECLARED = {}


def _declared_for(message: str):
    """The citation declaring `message`, or `None`. Matches on the invariant and the named id."""
    name = message.split(":", 1)[0]
    for (inv, ident), cite in DECLARED.items():
        if inv == name and f"'{ident}'" in message:
            return cite
    return None


def sweep(build, seeds) -> dict:
    """Run `build(seed)` for each seed and collect violations.

    `build` returns a finished World. Returns `{"seeds", "examined", "unexercised",
    "violations", "declared", "by_seed"}`, where `violations` is the NEW ones and `declared` the
    ones `DECLARED` already cites. A caller gates on `violations`; `declared` is reported, never
    silently dropped.

    ⚠⚠ **`unexercised` IS THE HONEST HALF AND IT IS WHY THIS RETURNS A CENSUS AT ALL.** It names
    every carrier the sweep never saw a single row of, so a caller can tell "clean" from "never
    asked". A world with `offices: 0` proves nothing about `office_singly_held`, and the previous
    `checked` term — predicates OFFERED, not rows READ — reported 8 checks either way.

    ⚠ **`checked` EXISTS SO A ZERO CANNOT MEAN "LOOKED AT NOTHING".** `CLAUDE.md` §0.1 pt 2: a
    loop that asserts conditionally must assert that it asserted. A sweep over an empty seed list,
    or one whose builder silently returned a bare World, reports `violations: []` — which is
    indistinguishable from a clean run unless the caller can also see how much work happened."""
    seeds = list(seeds)
    by_seed, new, declared = {}, [], []
    examined = {k: 0 for k in carrier_census_keys()}
    for s in seeds:
        w = build(s)
        for k, n in carrier_census(w).items():
            examined[k] += n
        v = violations(w)
        if v:
            by_seed[s] = v
        for m in v:
            (declared if _declared_for(m) else new).append(f"seed {s}: {m}")
    return {"seeds": len(seeds), "examined": examined,
            "unexercised": sorted(k for k, n in examined.items() if n == 0),
            "violations": new, "declared": declared, "by_seed": by_seed}


def carrier_census_keys() -> tuple:
    """The census keys, fixed so a sweep over zero seeds still reports every carrier as 0."""
    return ("tenures", "events", "claims", "persons", "stance_rows", "offices", "propositions")
