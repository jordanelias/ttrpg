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
    "ought_names_an_entity",
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
    """Every Tenure in the world, however it is stored.

    ⚠ BOTH STORES, AND THAT IS NOT DEFENSIVE — IT IS WHERE A MISS WOULD HIDE. `W5` moved Tenures
    onto their SUBJECT (`Person.tenures`), because `Tenure`'s own docstring says the subject owns
    it; a Tenure whose subject is not a person (`contain : Rung -> Rung` is most of them) has no
    person to live on and goes to `World._unowned`. A sweep reading only `w.tenures` would examine
    the person-owned half and report zero violations for the other, which is the sham-clear this
    module exists to avoid."""
    seen, out = set(), []
    for t in list(getattr(w, "tenures", []) or []) + list(getattr(w, "_unowned", []) or []):
        if id(t) not in seen:
            seen.add(id(t))
            out.append(t)
    return out


def tenure_interval(w) -> list:
    """An ended Tenure ended no earlier than it began.

    NOT ENFORCED ON WRITE: `add_tenure` checks `kind` and ladder ascent and never looks at
    `since`/`until`, and `until` is set by whatever ends the tenure, long after the write. A
    negative interval makes `live` and every `since`-ordered read disagree about what happened."""
    bad = []
    for t in _all_tenures(w):
        if t.until is not None and t.until < t.since:
            bad.append(f"tenure_interval: {t.id!r} ends at {t.until} but began at {t.since}")
    return bad


def tenure_referent(w) -> list:
    """A live Tenure names things that exist on both ends.

    NOT ENFORCED ON WRITE: `add_tenure` indexes `self.rungs[...]` only inside the `contain`
    branch, so a `hold`, `commit`, `oblige`, `succeed`, `tie` or `knot` edge to an id naming
    nothing is accepted in silence. That is how `leaders()` can read an office nobody has and
    return a plausible empty list — the defect shape this repository has already met twice."""
    ents, bad = _entities(w), []
    for t in _all_tenures(w):
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


def ought_names_an_entity(w) -> list:
    """Every OUGHT Proposition's subject names something an act can be about.

    NOT ENFORCED ON WRITE: `Proposition` is a frozen dataclass with a `str` subject and no
    validation. This is `ED-IN-0210` Ruling 1 as a run-time predicate — *"verbs invoke mechanisms
    or interactions between a character and another entity/character. they are not fiats."* Q4
    emits `(prop.subject,)` as a question's referent and `options.py` clause 3 is
    `subject in referents(q)`, so a subject naming nothing produces candidates about nothing.
    `build_at` shipped exactly that and measured **0 of 4,870 acts naming another person**."""
    ents = _entities(w)
    return [f"ought_names_an_entity: {pid!r} is an OUGHT whose subject {p.subject!r} "
            f"names no entity in the world"
            for pid, p in sorted(w.propositions.items())
            if str(p.mood).upper() == "OUGHT" and p.subject not in ents]


def office_singly_held(w) -> list:
    """No Office is held by two people at once.

    NOT ENFORCED ON WRITE: nothing looks at the other `hold` edges when one is added. §11 makes
    an Office a SEAT — it has `conferral`, `revocation` and an upkeep — and a seat two people
    occupy is the scarcity defect this repository has already shipped once, where every person
    got an office and `leaders() == members()` for all eight factions."""
    held = Counter(t.object for t in _all_tenures(w)
                   if t.kind == "hold" and t.live and t.object in w.offices)
    return [f"office_singly_held: office {oid!r} is held by {n} people at once"
            for oid, n in sorted(held.items()) if n > 1]


#: id -> predicate. The roster above fixes the order; this is the dispatch.
CHECKS = {name: globals()[name] for name in INVARIANTS}


def violations(w) -> list:
    """Every invariant violation in `w`, in `INVARIANTS` order. Empty is the healthy answer."""
    out = []
    for name in INVARIANTS:
        out.extend(CHECKS[name](w))
    return out


#: (invariant, offending id) -> the citation that declares it. A KNOWN condition, not a pass.
#:
#: ⚠⚠ **A DECLARED EXCEPTION MUST CARRY A CITATION, AND THAT IS WHAT KEEPS THIS FROM BECOMING A
#: RUG.** The one entry below is `headless.py`'s `prop_einhir` — `Proposition("prop_einhir",
#: "OUGHT", "einhir_texts", ...)`, whose subject is a bare string naming no entity. This sweep
#: FOUND it independently, from the predicate, which is the strongest evidence available that the
#: predicate observes something real; the tree had already found it by hand and filed it as **F8 /
#: `ED-IN-0211`**, the finding that got `_eff_oblige` REVERTED for *"opening a Tenure to
#: `einhir_texts`, a bare string naming no entity"*.
#:
#: ⚠ **AND THE FIXTURE STAYS, WHICH IS WHY THIS LIST EXISTS AT ALL.** The obvious way to green
#: this row is to point Carin's want at a person, the way `populated.py` already points every
#: want. That would be wrong: `predicates.py`'s `_req_release` is built ON this case — a closer
#: is safe *because* a subject naming nothing matches no Tenure — and
#: `test_season_shape.py:8262` pins `("einhir_texts", "exists:Record", 0)` as the premise of that
#: argument. Deleting the fixture would delete the negative case that makes the opener/closer
#: asymmetry demonstrable. So it is declared, with its citation, and counted separately forever.
DECLARED = {
    ("ought_names_an_entity", "prop_einhir"):
        "F8 / ED-IN-0211 — headless.py's authored fixture; the negative case `_req_release` is "
        "built on. See predicates.py:205 and test_season_shape.py:8262.",
}


def _declared_for(message: str):
    """The citation declaring `message`, or `None`. Matches on the invariant and the named id."""
    name = message.split(":", 1)[0]
    for (inv, ident), cite in DECLARED.items():
        if inv == name and f"'{ident}'" in message:
            return cite
    return None


def sweep(build, seeds) -> dict:
    """Run `build(seed)` for each seed and collect violations.

    `build` returns a finished World. Returns
    `{"seeds": n, "checked": n_invariants_run, "violations": [...], "declared": [...],
    "by_seed": {...}}`, where `violations` is the NEW ones and `declared` the ones `DECLARED`
    already cites. A caller gates on `violations`; `declared` is reported, never silently dropped.

    ⚠ **`checked` EXISTS SO A ZERO CANNOT MEAN "LOOKED AT NOTHING".** `CLAUDE.md` §0.1 pt 2: a
    loop that asserts conditionally must assert that it asserted. A sweep over an empty seed list,
    or one whose builder silently returned a bare World, reports `violations: []` — which is
    indistinguishable from a clean run unless the caller can also see how much work happened."""
    seeds = list(seeds)
    by_seed, checked, new, declared = {}, 0, [], []
    for s in seeds:
        v = violations(build(s))
        checked += len(INVARIANTS)
        if v:
            by_seed[s] = v
        for m in v:
            (declared if _declared_for(m) else new).append(f"seed {s}: {m}")
    return {"seeds": len(seeds), "checked": checked,
            "violations": new, "declared": declared, "by_seed": by_seed}
