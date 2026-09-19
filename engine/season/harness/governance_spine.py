"""THE GENERIC GOVERNANCE SPINE — build the world `engine/season/governance_spine.yaml` declares.

⚠⚠ A TEST FIXTURE, NOT CANON. Read `governance_spine.yaml`'s own header first: it says why these thirteen
seats are deliberately characterless, why thirteen rather than Jordan's 127, and which of his
design asks are recorded there rather than half-built.

WHY IT IS A SEPARATE BUILDER AND NOT A FLAG ON `populated.build_realm`. The authored realm is a
PLACE — 46 named NPCs, 37 settlements, real factions — and its rung census is irregular by
design (`{realm: 1, duchy: 3, territory: 17, ...}`) because it follows canon. This is a REGULAR
spine whose only property is its shape, and the two must not be conflated: a flag would make one
world answer two questions, and a later reader could not tell which census a measurement came
from. Jordan's *"fine tune FROM generics"* is a MERGE onto this spine, and a merge needs the spine
to exist on its own first.

⚠ WHAT IS ACTUALLY NEW HERE IS THE **REGULARITY**, NOT THE DEPTH — AND AN EARLIER DRAFT OF THIS
HEADER CLAIMED OTHERWISE. It said this was "the first world in the tree to build a `province` rung"
and "the first exercise of a seven-deep containment chain". Both are false, and the falsifier is one
line: `corpus_run.build_at({'id': ..., 'scale': 'person'}, 0)` slices `rung_kinds` from the case's
scale upward, so every person-scale case — 37 of them, per ED-IN-0255 — already builds a province
and a depth-7 chain. Only the narrow claim about `populated.build_realm` held: THAT builder goes
realm -> duchy -> territory and skips `province`. What this spine adds is a world whose census is
regular and whose branching is declared, so a measurement over it means something; corpus worlds
are one chain wide and cannot show dissemination fanning out or aggregation folding in.
"""

from __future__ import annotations

from engine.substrate import names as _names

from ..data import files
from ..data.rosters import load_yaml, remit_or_default
from ..queries import world_q
from ..state.carriers import Office, Person, Rung, Tenure
from ..state.world import World

# ⚠ THE ANCHOR IS `data/files.py`, NOT A LOCAL `__file__`. That module is the package's single
# path owner for DATA FILES. ⚠ An earlier version of this comment stated the invariant as
# `grep -rln __file__ season/` printing `data/files.py` alone — which is FALSE, and this comment
# was one of the three hits that made it so (the literal in the sentence matches the grep). The
# true statement is narrower: `data/files.py` owns every path to a REGISTRY the package loads;
# `tests/test_season_shape.py` legitimately resolves a `.py` for an AST walk. A local `parents[1]`
# here would be correct only while this
# module sits in `harness/`; move it one level and it resolves to a wrong-but-existing
# directory, which is the silent failure `harness/populated.py` records paying for once.
SPINE_YAML = files.GOVERNANCE_SPINE_YAML

# ⚠ ONE NAME, ONE PLACE — AND A LITERAL HERE WOULD HAVE BEEN THE SECOND COPY. The fixture faction
# is authored at `references/names_index.yaml: world.faction_x` and reaches the season loop through
# `rosters.yaml: factions` (`from_names: faction`). Spelling `"faction x"` in this module would put
# the same string in two files, so a rename at the index would fail thirteen seats inside
# `office_faction` with a message about a non-canonical faction rather than about the stale literal
# — §0.05 cl.3, "never keep a second copy". The ID is the durable thing; the display string is not.
SPINE_FACTION_ID = "world.faction_x"
SPINE_FACTION = _names.canonical_for(SPINE_FACTION_ID)


def spec() -> list[dict]:
    """The declared rungs, parent-first. The FILE is the owner; this reads it (§0.05)."""
    # ⚠ `load_yaml` TAKES TEXT, NOT A PATH, and it is reused rather than replaced by a bare
    # `yaml.safe_load` because it carries the duplicate-key refusal (§8 — one rule, one owner):
    # `safe_load` keeps the LAST of two same-named keys silently, "which is how two `writes_note`
    # cells became one".
    rows = (load_yaml(SPINE_YAML.read_text(encoding="utf-8")) or {}).get("rungs") or []
    if not rows:
        raise AssertionError(f"{SPINE_YAML} declares no rungs")
    # ⚠ `load_yaml`'s DUPLICATE-KEY REFUSAL DOES NOT REACH `id:` VALUES, and the comment above
    # would read as though it did. That guard fires on two same-named keys in one MAPPING; these
    # ids are field values repeated across SEQUENCE items, which YAML considers well-formed. Left
    # unchecked, a duplicated row silently overwrote `w.rungs[id]`, `w.persons[...]` and
    # `w.offices[...]` in `build`, and minted a second Tenure sharing one id — so the one property
    # that makes these seats addressable was the one property nothing verified.
    # ⚠ THE SUFFIX IS WHAT IS CHECKED, NOT THE ID, because the suffix is what addresses the seat.
    # `build` derives `lp_<suffix>`, `lo_<suffix>` and three Tenure ids from `rid[3:]`, so two
    # DISTINCT ids sharing a suffix (`lr_realm` / `xx_realm`) collide on all five while passing an
    # id-only check — and `add_tenure` performs no id-uniqueness check of its own. An earlier
    # version checked `id` alone while its message promised the holder and the office.
    ids = [str(r.get("id") or "") for r in rows]
    if any(len(i) < 4 for i in ids):
        raise AssertionError(
            f"{SPINE_YAML} declares a rung id shorter than four characters ("
            f"{[i for i in ids if len(i) < 4]}). `build` derives every holder, office and tenure "
            f"id from `id[3:]`, which would be empty")
    keys = [i[3:] for i in ids]
    dupes = sorted({k for k in keys if keys.count(k) > 1})
    if dupes:
        raise AssertionError(
            f"{SPINE_YAML} declares the seat key(s) {', '.join(map(repr, dupes))} more than once "
            f"(ids: {sorted(i for i in ids if i[3:] in dupes)}). A key addresses a rung, its "
            f"holder, its office and three tenures; a repeat overwrites all of them silently")
    return rows


def build(seed: int = 0) -> World:
    """The thirteen-seat spine: 13 rungs, 13 generic offices, 13 generic holders.

    ⚠ PARENT-FIRST AND ASSERTED, NOT ASSUMED. `World.add_tenure` refuses a `contain` edge that
    does not ASCEND `rung_kinds` strictly, so the file's order is load-bearing: a child declared
    before its parent raises rather than seating quietly. The assertion below states that
    dependency where a reader meets it, because the failure is otherwise a confusing `KeyError`
    from `contain_ascends` rather than a statement about the file.
    """
    w = World(world_seed=seed)
    rows = spec()
    for row in rows:
        rid, kind, under = row["id"], row["kind"], row.get("under")
        # The seat key: one slice, five derived ids. `spec()` has already refused a duplicate key
        # and an id too short to slice, so this is safe to take once rather than per use.
        key = rid[3:]
        # ⚠ THE RUNG KIND IS **NOT** CHECKED HERE, DELIBERATELY. `Rung.__init__` already does it
        # against the same `RUNG_KINDS` roster and raises a typed `Forbidden(..., "S10", law=...)`.
        # A pre-check here read as belt-and-braces but was strictly worse: it could never DISAGREE
        # (same roster), and it made the carrier's typed refusal unreachable from this path,
        # substituting a bare `AssertionError` that the tree's error vocabulary does not recognise
        # — `harness/corpus_run.py` catches `(Unspecified, Forbidden, Unowned)` by type. §8.
        # ⚠ AND THE FOUR `AssertionError`s THIS MODULE DOES RAISE ARE NOT A CONTRADICTION OF THAT,
        # though they read as one. Those fire on a malformed `governance_spine.yaml` — a FIXTURE'S
        # OWN declaration, authored in this repo and read by nothing but tests. They are the
        # fixture refusing to build, not the engine grading a world, so there is no run for
        # `corpus_run` to grade and nothing for the typed vocabulary to carry. The rule above is
        # about a refusal on the ENGINE's path, which is the path a rung kind is checked on.
        if under is not None and under not in w.rungs:
            raise AssertionError(
                f"{rid} is declared under {under!r}, which is not built yet — "
                f"`governance_spine.yaml` must list every parent BEFORE its children, because "
                f"`add_tenure` refuses a `contain` edge that does not ascend the ladder")
        w.rungs[rid] = Rung(rid, kind)

        pid = f"lp_{key}"
        w.persons[pid] = Person(pid, name=f"{row['post']} of {key}")
        # ⚠ A PERSON IS ALSO A RUNG, AND OMITTING THIS BROKE THE ONE THING THE SPINE IS FOR.
        # `rung_kinds` opens with `person`, and all three sibling builders mint this seat --
        # `populated.build_realm` (46 of 46), `corpus_run.build_at`, `probes.py`. This builder did
        # not, so the 13 `lt_in_*` contain edges put persons in the containment TREE while
        # `w.rungs` did not know them: `world_q.descendants(w, 'lr_realm')` returned 25 ids of
        # which 13 were unresolvable, and `r1_aggregate` -- R-1, the aggregation half of
        # *"we don't know how dissemination and aggregation works"* -- raised `KeyError: 'lp_realm'`
        # on the only world built to observe it. The shape test passed throughout, because a census
        # of rungs, offices and holders never drives an aggregate.
        w.rungs[pid] = Rung(pid, "person")

        oid = f"lo_{key}"
        # ⚠ NO REMIT IS AUTHORED HERE. `remit_or_default([])` fills from
        # `rosters.yaml: remit_default`, the testing default, which is the ONE owner of that rule
        # and says at length that it is not canon.
        # ⚠ `faction x`, A TEST FACTION, RULED BY JORDAN: *"place them all under 'faction x' as a
        # test faction"*. It cannot be placeless: `office_faction` REFUSES an office naming neither
        # a `body` nor a `faction`, and a declared faction must be a roster member (`H-99` +
        # §42.2's polarity, *"no evidence of belonging is a refusal, never a default faction"*), so
        # a fully generic seat is forbidden by design — the code being right.
        # ⚠ AN EARLIER VERSION USED `Crown` AND THAT WAS WRONG: it would have made a fixture look
        # like canon Crown structure. `faction x` is unmistakable, which is the point.
        # The member is authored at `references/names_index.yaml` (`world.faction_x`) and reaches
        # this roster through `from_names: faction` — edit the naming index, never the roster.
        w.offices[oid] = Office(oid, str(row["post"]), rid, remit_or_default([]),
                                faction=SPINE_FACTION)
        w.add_tenure(Tenure(f"lt_hold_{key}", pid, oid, "hold", 0))
        w.add_tenure(Tenure(f"lt_in_{key}", pid, rid, "contain", 0))
        if under is not None:
            w.add_tenure(Tenure(f"lt_up_{key}", rid, under, "contain", 0))
    return w


def census(w: World) -> dict:
    """What the spine IS, as numbers — for a caller that wants to assert the shape.

    ⚠ EVERY ROW HERE MUST BE ABLE TO GO WRONG (§0.1 pt 2), AND AN EARLIER VERSION HAD THREE THAT
    COULD NOT. `persons` and `seated` exist because a census of thirteen rungs, thirteen offices
    and thirteen hold-Tenures said nothing about whether a PERSON was on the other end of any of
    them: deleting `build`'s `w.persons[pid] = Person(...)` line left this dict byte-identical,
    because `held` counts hold Tenures by `t.object in w.offices` and `add_tenure` routes an
    ownerless hold to `_unowned` without refusing. The holders are the thing the spine was asked
    for — "we don't know how dissemination and aggregation works" is a question about people —
    so their absence must be observable here.
    """
    from collections import Counter
    if not w.rungs:
        raise AssertionError(
            "census() was given a world with no rungs. It reports the SHAPE of a containment "
            "spine, and an empty world has none — build one with `governance_spine.build(seed)`")
    # ⚠ `world_q.ancestry` IS THE OWNER OF THIS WALK AND IS CALLED RATHER THAN REBUILT (§8).
    # Two earlier versions were wrong in different ways: a dict comprehension over `w.tenures`
    # (which keeps the LAST live `contain` edge where `parent_of` returns the FIRST), then a local
    # `while` loop over `parent_of` that was left in place when `ancestry` was extracted — so the
    # helper's own docstring named this function as one of the three it had consolidated while
    # this function was still the third copy. It is now actually the caller the docstring claims.
    # ⚠ THE CHAINS ARE KEPT, NOT RECOMPUTED. An earlier version took `len(ancestry(...)) - 1` and
    # THREW THE CHAIN AWAY, then called `parent_of` again per rung to build `has_child` and once
    # more per place rung for `place_child` — re-deriving a value `ancestry` had already computed
    # as its own first step. MEASURED on the 13-seat fixture: 162 `parent_of` calls, of which 39
    # (24%) were that re-derivation. Trivial in absolute terms — sub-millisecond, and `census` runs
    # twice in the whole suite — but the chain is what every row below actually wants, so keeping
    # it is the simpler code as well as the cheaper.
    anc = {rid: world_q.ancestry(w, rid) for rid in w.rungs}
    depth = {rid: len(chain) - 1 for rid, chain in anc.items()}
    # ⚠ THE CONTAINMENT TREE HOLDS TWO KINDS OF NODE AND THE SHAPE CLAIMS ARE ABOUT ONE OF THEM.
    # `person` is the first member of `rung_kinds`, so every holder is a rung AND a leaf of the
    # tree. The declared spine — seven levels, one branch point, two hearth ends — is a claim
    # about PLACES, and reporting one undivided set made it unstatable: with persons minted, no
    # place rung is childless, so a bare `leaves` returns the 13 people and `max_depth` is 7.
    # Both readings are kept, because both are true and a caller needs to say which it means.
    places = {rid: r for rid, r in w.rungs.items() if r.kind != "person"}
    has_child = {chain[1] for chain in anc.values() if len(chain) > 1}
    place_child = {anc[rid][1] for rid in places if len(anc[rid]) > 1}
    # ⚠ FILTERED ONCE, READ THREE TIMES. The same three-condition predicate was spelled at each
    # of `held`, `seated` and `granted`; a later edit to what counts as held (a quarantined
    # office, say) would have had three sites and missing one desyncs the very three rows this
    # function exists to keep honest about each other.
    holds = [t for t in w.tenures
             if t.kind == "hold" and t.live and t.object in w.offices]
    holders = {t.subject for t in holds}
    return {
        "rungs": len(w.rungs),
        "place_rungs": len(places),
        "by_kind": dict(Counter(r.kind for r in w.rungs.values())),
        "offices": len(w.offices),
        "persons": len(w.persons),
        "held": len(holds),
        # ⚠ A HOLD WHOSE HOLDER DOES NOT EXIST IS NOT A SEAT. This is the row that separates
        # thirteen Tenures from thirteen people, and it is what `held` alone could not say.
        "seated": sum(1 for pid in holders if pid in w.persons),
        "granted": sum(1 for t in holds if t.granted_acts),
        "max_depth": max(depth.values()),
        "place_depth": max(depth[rid] for rid in places),
        # ⚠ LEAVES ARE CHILDLESS RUNGS, NOT DEEPEST ONES. Those coincide on a regular spine and
        # diverge the moment one is not: a childless `settlement` at depth 3 is a genuine dead end
        # that a `v == max_depth` test silently omitted, under a key named `leaves`.
        "leaves": sorted(rid for rid in w.rungs if rid not in has_child),
        "place_leaves": sorted(rid for rid in places if rid not in place_child),
    }

if __name__ == "__main__":  # pragma: no cover
    import json
    print(json.dumps(census(build(0)), indent=2, sort_keys=True))
