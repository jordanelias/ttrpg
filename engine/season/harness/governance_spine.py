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

B21.72, `play`: A SCENARIO ON THIS SPINE (FA standalone S1, S2, S5, S6). `situation` makes one of three openings by the
game's own acts through the fold at tick 0, `play` runs seasons from it with one person's choices handed to a callback
(`harness/play_surface.py`) and the rest on the shipped chooser, and `digest` is the printed summary of what happened, as a
news digest is: one line per occurrence, read off the log and the tenures, written nowhere. It adds no rule and edits no
file under `loop/`, `state/`, `queries/`, `decision/` or `data/`: with no pick the run is `populated.run`'s on the same world.
`python -m engine.season.harness.governance_spine play SEED SEASONS {vacancy|order|succession} [--player ID] [--pick I,I,...]`.

B21.74, `recall`, `--world realm`, `loop_closed` (`06_FA_shortest_loop_B`): `recall` is `order`'s opening with a longer ending (the run goes on two seasons
after the player's seat is gone, so the filling of it is seen); `play(..., world="realm")` is `populated.run` on the built realm with the digest printed;
`loop_closed` is one pure reader of whether the five links of the loop (an order, an answer to it, a response to a withheld answer, a seat closed, a seat
filled) each occurred, and who acted in them. `play SEED SEASONS --world realm`.
"""

from __future__ import annotations

import argparse
import contextlib
import sys
from collections import Counter
from typing import Callable, Iterator, Optional, Sequence

from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
from engine.substrate import names as _names

from ..boot.chooser import chooser
from ..boot.realm import build_realm, place_person
from ..data import files
from ..data.matrix import Step, WriteClass, matrix_row
from ..data.rosters import FACTION_BY_PROP, RESTRAINT_KINDS, SUCCESSIONS, load_yaml, remit_or_default
from ..data.verbs import REFUSAL_KINDS, VERB_TABLE
from ..decision.choose import make_ranker
from ..decision.options import seat_of
from ..decision.sheet import development_space
from ..gaps import Forbidden
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..queries import faction_q, world_q
from ..queries.person_q import COMPLIANCE_WITHHELD, addressed_to
from ..state.attribution import causing_act
from ..state.carriers import Act, Office, Person, Proposition, Rung, Site, Tenure, generated_attributes, is_clock_stage
from ..state.containment import parent_of
from ..state.gate import TENURE_CLOSED
from ..state.ids import H, draw_factory
from ..state.world import World
from .heir_hears import holder as _holder_of
from .play_surface import dispatching_chooser

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
    """The thirteen-seat spine: 13 rungs, 13 generic offices, 13 generic holders, and one
    `dwelling` Site per `hearth` rung (`24d-i`; see the note at the mint).

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
        # B01a: a drawn sheet, as every other world's persons hold (the aperture measures this world beside the realm).
        w.persons[pid] = Person(pid, name=f"{row['post']} of {key}",
                                attributes=generated_attributes(w.world_seed, pid, w.fixtures.get("generated_attribute_range")))
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
        # B21.71: HOW THE SEAT IS FILLED AND WHO MAY STRIP IT, read off the row (a member of
        # `rosters.yaml: conferral_bases` / `revocation_bases`, which `Office.__post_init__` refuses
        # a value off). `.get` is an absent key reading `None`, the realm row's own `null`: with
        # neither basis `may_fill` is false for every pair, so a row that forgot them builds a seat
        # nobody can fill, which is the state this edit ended.
        w.offices[oid] = Office(oid, str(row["post"]), rid, remit_or_default([]),
                                conferral=row.get("conferral"), revocation=row.get("revocation"),
                                faction=SPINE_FACTION)
        w.add_tenure(Tenure(f"lt_hold_{key}", pid, oid, "hold", 0))
        w.add_tenure(Tenure(f"lt_in_{key}", pid, rid, "contain", 0))
        # Plan position `19c`: the holder LIVES at his seat's rung, too -- `populated.build_realm`'s
        # rule, so the two chains start with residence and presence agreeing (`_eff_migrate`).
        w.add_tenure(Tenure(f"lt_home_{key}", pid, rid, world_q.RESIDE_KIND, 0))
        if under is not None:
            w.add_tenure(Tenure(f"lt_up_{key}", rid, under, "contain", 0))
        # ⚠ A DWELLING PER HEARTH, BY `populated.build_realm`'s RULE (`ED-SE-0055`, plan position
        # `24d-i`). The ruling names `build_realm` only; minting here too is `24d-i`'s own
        # architecture call. Two reasons. This spine is the template the realm is fine-tuned FROM
        # (this module's header), so a spine hearth with no dwelling would give the two worlds
        # different hearths. And `19c`'s `migrate` runs its observable on the spine's two disjoint
        # chains. Without dwellings every rung's `capacity` would be the floor, the same number
        # on every rung, so no throttle that depends on housing built could show there. With one
        # per hearth, the realm counts two and each chain below it counts one. The id follows
        # this module's `l<letter>_<key>` convention with `s` for Site, and the starting
        # condition is the realm's, full `condition_scale`.
        if kind == "hearth":
            sid = f"ls_{key}_dwelling"
            w.sites[sid] = Site(sid, rid, "dwelling",
                                condition=w.fixtures.get("condition_scale"))
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

# ---------------------------------------------------------------------------------------------------
# B21.72 -- A SCENARIO THAT PLAYS (`06_FA_playable_scenario`): situation, digest, offered, play.
# ---------------------------------------------------------------------------------------------------

# ⚠ THE SEAT A SUCCESSION SCENARIO PASSES, NAMED FROM THE SOVEREIGN'S OWN SEAT (`<his office id>_<this>`), NEVER A LITERAL ID. No act
# mints a seat whose basis only the claim opens (`establish` founds `appointed`, `offices.yaml: founding`), so `situation` builds it as `build`
# builds every seat (the fixture is this module's), and the act that matters, the `release`, goes through the fold.
THRONE_SUFFIX = "throne"

WORLDS = ("spine", "realm")
SITUATIONS = ("vacancy", "order", "succession", "recall")

# B21.74: THE SEASONS A SCENARIO GOES ON AFTER THE PLAYER'S SEAT IS GONE, by situation (none named: it ends at once). `recall` is `order`'s opening; what it
# adds is that the run does not stop on the revocation, so the filling of the seat is seen (`06_FA_shortest_loop_B`, "The resolution": two seasons later).
LINGER_AFTER_UNSEATED = {"recall": 2}


def _seat_of(w: World, player: str) -> Office:
    """The seat the player plays through: his first live seat-`hold` (`World.seat_holds`, store order). A scenario is one seat's season of rule."""
    held = w.seat_holds(player)
    if not held:
        raise _refused(f"{player!r} holds no seat on this world, so there is no seat to play through", "the player is a seat-holder")
    return w.offices[held[0].object]


def _refused(msg: str, needs: str) -> Exception:
    return Forbidden(msg, "harness/governance_spine.py::situation", needs=needs,
                     law="B21.72 -- a scenario starts from a state the engine produced: a situation the fold refuses stops the run, never a fallback")


def _top_rung(w: World) -> Optional[str]:
    """The id of the first rung of the realm's kind (`world_q.REALM_KIND`, the top of the ordered `rung_kinds` roster), or `None`."""
    return next((r.id for r in w.rungs.values() if r.kind == world_q.REALM_KIND), None)


def _held_seats(w: World, where: Callable) -> list:
    """The ids, sorted, of the seats `where(office)` admits that someone holds."""
    return sorted(o.id for o in w.offices.values() if where(o) and _holder_of(w, o.id))


def default_player(w: World) -> str:
    """The holder of the first seat (by id) one rung below the top of the ladder: the Duke of the first chain, on this spine. Read off the
    containment tree, so no id is spelt."""
    top = _top_rung(w)
    below = _held_seats(w, lambda o: o.rung and top and parent_of(w, o.rung) == top)
    if not below:
        raise _refused("the world has no seat one rung below its top to play", "a seated rung under the realm")
    return _holder_of(w, below[0])


def _sovereign(w: World, seat: Office) -> Office:
    """The seat on the top rung of `seat`'s own chain (the Sovereign, on this spine)."""
    top = world_q.ancestry(w, seat.rung)[-1]
    held = _held_seats(w, lambda o: o.rung == top)
    if not held:
        raise _refused(f"no seat on {top!r}, the top of the player's chain, has a holder", "a seated top rung")
    if held[0] == seat.id:
        raise _refused(f"{seat.id!r} is itself the top of its chain: nothing stands above it to issue or to pass a seat", "a player below the top seat")
    return w.offices[held[0]]


def _titles(w: World, seat: Office) -> tuple:
    """The seats of the player's own rung kind that someone holds, by id: the set of titles a succession lists (A-19), the player's among them."""
    kind = w.rungs[seat.rung].kind
    out = tuple(_held_seats(w, lambda o: o.rung in w.rungs and w.rungs[o.rung].kind == kind))
    if len(out) < 2:
        raise _refused(f"only {len(out)} seat(s) of the player's rung kind {kind!r} are held; a succession lists a set of at least two titles",
                       "two held seats of the player's rung kind")
    return out


def successions_for(w: World, name: str, player: str) -> dict:
    """The scenario-local `successions` row `play` sets for the run: `{throne id: (title, ...)}` for `succession`, `{}` for any other situation."""
    if name != "succession":
        return {}
    seat = _seat_of(w, player)
    return {f"{_sovereign(w, seat).id}_{THRONE_SUFFIX}": _titles(w, seat)}


def _open(w: World, d: SeasonDriver, act: Act) -> None:
    """ONE OPENING ACT THROUGH THE FOLD, THEN WHAT THE SEASON DOES WITH ITS EVENTS: logged (S19.5) and witnessed, so the people near it hold what they saw.
    A refusal (a kind some row emits on refusal) or an act the fold answered with nothing stops the scenario naming the Event. A drawn
    failure is no refusal: D-08, it is the scenario's opening and the digest reports its band."""
    w.step, w.frozen = Step.RESOLVE, False
    events = d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    refusals = [e for e in events if e.kind in REFUSAL_KINDS]
    if refusals or not events:
        named = ", ".join(e.kind for e in refusals) or "no Event at all"
        raise _refused(f"the fold refused the opening act {act.id!r} ({act.verb}): {named}", "an opening act the fold admits")
    for e in events:
        w.log.append(e)
    d.witness(mint_token(w, WriteClass.INTERIOR), events)


def _opening(w: World, name: str, player: str) -> Iterator[Act]:
    """The hand-built acts of `name`, one at a time: each is folded before the next is built, so a later act reads the world the earlier one made."""
    seat = _seat_of(w, player)
    if name == "vacancy":
        # the seat one rung below the player's, laid down by the man who holds it
        below = _held_seats(w, lambda o: o.rung and parent_of(w, o.rung) == seat.rung)
        if not below:
            raise _refused(f"no held seat stands one rung below {seat.id!r}", "a held seat beneath the player's")
        yield Act(id=f"scn:vacancy:{below[0]}", actor=_holder_of(w, below[0]), verb="release", payload={"subject": below[0]}, via=below[0])
    elif name in ("order", "recall"):
        sov = _sovereign(w, seat)
        sovereign = _holder_of(w, sov.id)
        # a writ's terms are something its issuer holds a claim on: he utters one first, as the engine's own acts do
        yield Act(id="scn:order:terms", actor=sovereign, verb="utter")
        yield Act(id="scn:order:writ", actor=sovereign, verb="issue", via=sov.id,
                  payload={"subject": "prop:scn:order:terms", "to": player})
    elif name == "succession":
        sov = _sovereign(w, seat)
        (tid, _), = successions_for(w, name, player).items()
        if tid not in w.offices:
            w.offices[tid] = Office(tid, "Throne", sov.rung, remit_or_default([]), conferral="inheritance", revocation=None,
                                    faction=sov.faction)
            w.add_tenure(Tenure(f"lt_hold_{tid}", _holder_of(w, sov.id), tid, "hold", w.tick))
        yield Act(id=f"scn:succession:{tid}", actor=_holder_of(w, sov.id), verb="release", payload={"subject": tid}, via=tid)
    else:
        raise _refused(f"{name!r} is no situation; the table is {SITUATIONS}", "one of " + "|".join(SITUATIONS))


def situation(w: World, name: str, player: str) -> list:
    """`vacancy`, `order`, `succession` or `recall` (`order`'s opening; the name selects `play`'s ending rule), MADE BY THE GAME'S OWN ACTS through `SeasonDriver`'s fold at tick 0 (never by a branch on an id and never by
    writing a carrier of the situation directly), and the acts returned so the digest can cite them. A situation whose opening act the fold refuses raises,
    naming the Event, so a scenario cannot start from a state the engine did not produce. D-08: a set-up act is a draw where its row contests a prize,
    so it can come out otherwise; the scenario does not force it, and a set-up that failed is itself the opening situation (the digest reports its band).
    ⚠ `succession` builds ONE seat before its act, the throne (see `THRONE_SUFFIX`); everything else is an act."""
    d = SeasonDriver(w)
    acts = []
    for act in _opening(w, name, player):
        _open(w, d, act)
        acts.append(act)
    return acts


_situation = situation          # `play`'s own `situation` parameter shadows the name


# THE DIGEST'S SUBJECTS, BY THE VERBS THAT PRODUCE THEM. A KIND IS NEVER SPELT HERE: each verb's kinds are read off `VERB_TABLE`'s `emits` (every degree's branch
# and the refusal kinds), so a row that gains a kind is read with no edit here.
_DIGESTED = {
    "seat": ("release", "confer", "revoke", "succeed"),
    "writ": ("issue", "dispatch"),
    "answer": ("comply", "evade / defy", "construe"),
    "restraint": ("arrest", "pardon"),
    "oath": ("oblige",),
    "stores": ("requisition",),
}
_GROUP_OF_VERB = {v: g for g, vs in _DIGESTED.items() for v in vs}
_EDGE_GROUPS = frozenset({"seat", "restraint", "oath"})     # the groups whose line is about a tenure edge
OATH_KIND = "oblige"                                        # the tenure kind of a sworn man's edge (`data/verbs.py::TENURE_KINDS`)


def _kinds_of(verb: str) -> frozenset:
    row = VERB_TABLE[verb]
    return frozenset((*row.emits, *row.emits_on_refusal))


_KINDS_OF_VERB = {v: _kinds_of(v) for v in _GROUP_OF_VERB}
_SEAT_KINDS = frozenset().union(*(_KINDS_OF_VERB[v] for v in _DIGESTED["seat"]))


def digest(w: World, since: int) -> list:
    """`list[str]`: ONE LINE PER OCCURRENCE in `w.log[since:]` of a seat opened or closed, a writ issued and each answer to it, a ban or custody opened or
    ended, an oath taken or released, stores moved by `requisition` (the word is a news digest's: a short printed summary of what happened). A PURE READER: it
    reads the log, the act store and `w.tenures` and writes nothing. An Event is the digest's when the act that caused it is a verb of `_DIGESTED` and the kind
    is one of that verb's; an Event no act caused (a term running out, a death) is the digest's when it is one of the seat verbs' kinds and names a seat-hold."""
    edges = {t.id: t for t in w.tenures}

    def who(pid: Optional[str]) -> str:
        p = w.persons.get(pid) if pid else None
        return f"{p.name} ({pid})" if p is not None and getattr(p, "name", None) else str(pid)

    def seat(oid: str) -> str:
        o = w.offices.get(oid)
        return f"{o.post} ({oid})" if o is not None else str(oid)

    def reported(t: Tenure) -> bool:
        """A seat-`hold`, an `oblige` (an oath), a `detain` or a `ban`: the edges a line is about. A `hold` on a Record is a writ held, not a seat."""
        return (t.kind == "hold" and t.object in w.offices) or t.kind == OATH_KIND or t.kind in RESTRAINT_KINDS

    lines = []
    for e in w.log[since:]:
        act = causing_act(w, e)
        touched = [edges[c.subject] for c in e.changes if c.subject in edges]
        named = [t for t in touched if reported(t)]
        if act is not None:
            if e.kind not in _KINDS_OF_VERB.get(act.verb, ()):
                continue
            if touched and not named and _GROUP_OF_VERB[act.verb] in _EDGE_GROUPS:
                continue                    # a seat verb that moved only a writ or a commitment: no seat or oath moved
        elif not (e.kind in _SEAT_KINDS and any(t.object in w.offices for t in named)):
            continue
        opened = "closed" if e.kind == TENURE_CLOSED else "opened"
        if named:
            what = "; ".join(f"{who(t.subject)}: {t.kind} on {seat(t.object) if t.object in w.offices else t.object} {opened}" for t in named)
        else:
            d = act.payload if act is not None and isinstance(act.payload, dict) else {}
            what = ", ".join(f"{k}={d[k]}" for k in sorted(d) if isinstance(d[k], (str, int, float))) or "-"
        by = f"by {act.verb} of {who(act.actor)}" + (f" through {seat(act.via)}" if act.via else "") if act is not None else "by no act"
        lines.append(f"  t{e.emitted_at} {e.kind}{' [' + e.degree + ']' if e.degree else ''}: {what}; {by}")
    return lines


def offered(p, v, s, ask_budget, auto, *, rank: Callable) -> list:
    """FOR THE PLAYER'S DELIBERATION: the seat-gated candidates `opening_set` formed, as `rank` (the `make_ranker` call `development_space` reads) ordered
    them, grouped by the remit act that opens each, every one with the seat it would be exercised through. The index in front is the one `pick` takes.
    The shape of a `play_surface` callback (`s`, `ask_budget` and `auto` are the seam's and are not read); `rank` is the one added keyword. [`IS-B3-FA-02` deletes
    this at B34.]"""
    groups: dict = {}
    for i, c in enumerate(rank(p, v)):
        row = VERB_TABLE.get(c.verb)
        gates = [e.partition(":")[2] for e in (row.eligibility if row is not None else ()) if e.startswith("remit:")]
        to = {k: x for k, x in (c.operands or {}).items() if isinstance(x, str) and k != "via"}
        said = " ".join(f"{k}={x}" for k, x in sorted(to.items()))
        seat = seat_of(p, c)
        line = f"    [{i}] " + " ".join(x for x in (c.verb, c.subject or "", said, f"through {seat}" if seat else "") if x)
        # a verb no seat's remit gates (`succeed`: the title-holder's own claim) is offered too, under the heading that says so
        for act in gates or [None]:
            groups.setdefault(act, []).append(line)
    return [line for act in sorted(groups, key=lambda a: (a is None, a or ""))
            for line in ((f"  by the remit to {act}:" if act else "  as himself, through no seat's remit:"), *groups[act])]


@contextlib.contextmanager
def _successions_set(mapping: dict) -> Iterator[None]:
    """`SUCCESSIONS` changed IN PLACE for one run and put back: the three readers (`state/gate.py`, `decision/options.py`, `loop/effects_governance.py`) hold
    a `from`-import of the one dict, so only an in-place change reaches them (the tests' own `monkeypatch.setitem`). Each key's prior value is restored, or the
    key deleted if the run added it, whether the run ended or raised."""
    absent = object()
    prior = {k: SUCCESSIONS.get(k, absent) for k in mapping}
    try:
        for k, titles in mapping.items():
            SUCCESSIONS[k] = tuple(titles)
        yield
    finally:
        for k, was in prior.items():
            if was is absent:
                SUCCESSIONS.pop(k, None)
            else:
                SUCCESSIONS[k] = was


def standing_lines(w: World) -> list:
    """Each rostered faction's `faction_q.standing` record at the realm rung (B03.65's caller; no second footprint, density or provinces reading here); B21.74 adds `faction_q.weight` (B21.68)."""
    top = _top_rung(w)
    if top is None:
        return []
    out = []
    for prop, name in FACTION_BY_PROP.items():
        s = faction_q.standing(w, prop, top)
        out.append(f"  faction {name}: footprint {len(s.footprint)} rungs, {s.present} of {s.persons} present, "
                   f"largest holder's share {s.sovereign_share:.2f}, {len(s.provinces)} provinces, weight {faction_q.weight(w, prop):g}")
    return out


def _ending(w: World, n: int, seasons: int, unseated: Optional[int] = None, linger: int = 0) -> Optional[str]:
    """The first of the three endings that holds, each a Query: the player holds no seat (`unseated` is the season he was first found without one, and `linger`
    seasons have run since); an ending is reached; the season count is."""
    if unseated is not None and n - unseated >= linger:
        return "the player holds no seat"
    reached = world_q.endings_reached(w)
    if reached:
        return "an ending was reached: " + ", ".join(r.ending for r in reached)
    return "the season count was reached" if n >= seasons else None


# THE FIVE LINKS' VERBS, and the kinds each makes, read off `VERB_TABLE` (every degree's branch, the refusal kinds taken out: a refused act is no attempt). The two
# kinds named here are the ones the engine reads by name elsewhere (`TENURE_CLOSED`, `COMPLIANCE_WITHHELD`).
_ANSWERS = ("comply", "evade / defy", "construe")
_RESPONSES = ("revoke", "open_case", "arrest")
_MADE = {v: _kinds_of(v) - frozenset(VERB_TABLE[v].emits_on_refusal) for v in ("issue", *_ANSWERS, *_RESPONSES)}
# A SEAT-HOLD OPENS in the successful bands of the two verbs that give one (the Failure band writes no tenure); the kind a close takes is the one they share.
_OPENS = frozenset(k for v in ("confer", "succeed") for degree, ks in VERB_TABLE[v].emits_by_degree.items()
                   if degree != DEGREE_LABEL[Degree.FAILURE] for k in ks) - {TENURE_CLOSED}
# WHAT CLOSED A SEAT-HOLD, by the verb of the act that closed it; no act is a death (the seat's own receipt, `Subject.seat`) or a term running out. `confer` and
# `succeed` close the incumbent's hold as they give the seat on, so the seat is never empty: not a vacating.
_CLOSED_BY = {"release": "release", "revoke": "revocation", "seize": "seizure"}
LOOP_LINKS = ("ordered", "answered", "responded", "vacated", "filled")


def loop_closed(w: World, since: int) -> dict:
    """WHETHER THE LOOP CLOSED over `w.log[since:]`, A PURE READER (the log, the act store, `w.tenures` and `w.records`; it writes nothing): an order, an answer to
    it, a response to a withheld answer, a seat closed, a seat filled. Each count is of ACTS (one act that emits two kinds is one), read through the act that
    caused the Event (`causing_act`):
      `ordered`   `issue`'s acts that made a writ;
      `answered`  `comply`'s, `evade / defy`'s and `construe`'s acts whose actor is an addressee of the writ the act names (`person_q.addressed_to`);
      `responded` ATTEMPTED `revoke`, `open_case` and `arrest` acts (a resisted `revoke` is one, a refused act is none) whose actor issued a writ that their
                  subject, or a holder of the seat they name, had withheld compliance on EARLIER in the log; `responded_bands` is the band each reached
                  (`None`: the verb draws none);
      `vacated`   closes of a seat-`hold`, by cause (`vacated_by`: death, release, revocation, term, seizure);
      `filled`    opens of a seat-`hold` on an Office with an earlier close of a `hold` on it not yet filled;
      `persons`   the distinct actors of the acts above.
    `closed` is the five links all above zero. A writ made before `since` is outside the reading."""
    log = w.log[since:]
    edges = {t.id: t for t in w.tenures}
    held: dict = {}                       # person -> the seats he holds or held (a revoked man's closed hold stays on his own list)
    for t in w.tenures:
        if t.kind == "hold" and t.object in w.offices:
            held.setdefault(t.subject, set()).add(t.object)
    writ_by: dict = {}                    # record id -> the `issue` act of the Event that first named it
    withheld: dict = {}                   # writ id -> the addressees who withheld compliance on it
    ordered, answered, responses, closes, vacant, filled = set(), set(), {}, [], {}, 0
    actors: set = set()
    for e in log:
        act = causing_act(w, e)
        verb = act.verb if act is not None else None
        if verb == "issue" and e.kind in _MADE["issue"]:
            ordered.add(act.id)
            actors.add(act.actor)
            for c in e.changes:
                writ_by.setdefault(c.subject, act)
        elif verb in _ANSWERS and e.kind in _MADE[verb]:
            writ = act.payload.get("subject") if isinstance(act.payload, dict) else None
            rec = w.records.get(writ)
            if rec is not None and addressed_to(rec.subject_matter, act.actor):
                answered.add(act.id)
                actors.add(act.actor)
                if e.kind == COMPLIANCE_WITHHELD:
                    withheld.setdefault(writ, set()).add(act.actor)
        elif verb in _RESPONSES and e.kind in _MADE[verb] and act.id not in responses:
            target = act.payload.get("subject") if isinstance(act.payload, dict) else None
            if any(writ_by[r].actor == act.actor and (target in who or any(target in held.get(a, ()) for a in who))
                   for r, who in withheld.items() if r in writ_by):
                responses[act.id] = e.degree
                actors.add(act.actor)
        if e.kind == TENURE_CLOSED:
            for c in e.changes:
                t = edges.get(c.subject)
                office = t.object if t is not None and t.kind == "hold" else c.subject if c.subject in w.offices else None
                if office not in w.offices:
                    continue
                if verb in _CLOSED_BY:
                    cause = _CLOSED_BY[verb]
                    actors.add(act.actor)
                elif t is None:
                    cause = "death"       # the seat's own receipt: a dead man's tenures leave the store with him (`Subject.seat`)
                elif t.term is not None and e.causes == [t.term.declared_by]:
                    cause = "term"        # MATTER matured it, citing the act that wound the clock
                else:
                    continue
                closes.append(cause)
                vacant[office] = vacant.get(office, 0) + 1
        elif e.kind in _OPENS:
            for c in e.changes:
                t = edges.get(c.subject)
                if t is not None and t.kind == "hold" and t.object in w.offices and vacant.get(t.object):
                    vacant[t.object] -= 1
                    filled += 1
                    if act is not None:
                        actors.add(act.actor)
    out = {"ordered": len(ordered), "answered": len(answered), "responded": len(responses), "vacated": len(closes), "filled": filled,
           "persons": len(actors), "responded_bands": dict(Counter(responses.values())), "vacated_by": dict(Counter(closes))}
    out["closed"] = all(out[k] > 0 for k in LOOP_LINKS)
    return out


def loop_line(r: dict) -> str:
    """`loop_closed`'s reading as the one line `play` prints."""
    bands = ", ".join(f"{b or 'no draw'} x{n}" for b, n in sorted(r["responded_bands"].items(), key=str))
    by = ", ".join(f"{c} x{n}" for c, n in sorted(r["vacated_by"].items()))
    return (f"loop: ordered {r['ordered']}, answered {r['answered']}, responded {r['responded']}" + (f" ({bands})" if bands else "")
            + f", vacated {r['vacated']}" + (f" ({by})" if by else "") + f", filled {r['filled']}; persons {r['persons']}; closed {r['closed']}")


def play(seed: int, seasons: int, situation: Optional[str] = None, player: Optional[str] = None, pick: Optional[Sequence[int]] = None,
         out: Callable[[str], None] = print, *, world: str = "spine") -> dict:
    """Builds the spine, makes `situation`, and runs up to `seasons` seasons with `dispatching_chooser(auto, {player: callback})`, printing the digest and
    each faction's standing after every season, then `loop_closed`'s line. `pick=None` is the shipped chooser for everyone: the run is `populated.run`'s on the
    same world (the control). A `pick` (indices into the offer `offered` prints) is spent at the player's FIRST deliberation, through `development_space`; after
    it the player takes the shipped order (`take_ranked`), so he acts as himself. `pick=()` shows the offer and takes nothing. Stops at the first of: the player
    holds no seat (`recall`: `LINGER_AFTER_UNSEATED` seasons after the one he was first found without it); `world_q.endings_reached` is non-empty; the season
    count. `SUCCESSIONS` is the scenario's for the run and restored after it, a run that raises included.
    `world="realm"` (B21.74) is the built realm, read as it is built: `situation`, `player` and `pick` must be None (no hand-made opening, nobody played), and it
    runs the season count whole, so it is `populated.run`'s on the same seed with the digest printed.
    Returns `{"world", "ended", "seasons", "acts", "loop"}` (`loop` is `loop_closed(w, 0)`)."""
    if world not in WORLDS:
        raise _refused(f"{world!r} is no world; the table is {WORLDS}", "one of " + "|".join(WORLDS))
    if world == "realm":
        if situation is not None or player is not None or pick is not None:
            raise _refused("the realm is read as it is built: no situation, no player and no pick", "situation=None, player=None, pick=None")
        out(f"realm, seed {seed}, nobody played")
        return _run(build_realm(seed), seasons, None, None, out, lambda n: None)
    if situation is None:
        raise _refused("the spine needs a situation", "one of " + "|".join(SITUATIONS))
    w = build(seed)
    player = player or default_player(w)
    mapping = successions_for(w, situation, player)
    with _successions_set(mapping):
        acts = _situation(w, situation, player)
        out(f"{situation}, seed {seed}, playing {player}: opening act(s) {[a.id for a in acts]}")
        for line in digest(w, 0):
            out(line)
        verbs = resolvable_verbs()
        overrides: dict = {}
        if pick is not None:
            overrides[player] = _callback(w, tuple(pick), verbs, out)
        unseated: list = []

        def ended_at(n: int) -> Optional[str]:
            if not unseated and not w.seat_holds(player):
                unseated.append(n)
            return _ending(w, n, seasons, unseated[0] if unseated else None, LINGER_AFTER_UNSEATED.get(situation, 0))
        res = _run(w, seasons, verbs, overrides, out, ended_at)
    res["acts"] = acts
    return res


def _run(w: World, seasons: int, verbs, overrides: Optional[dict], out: Callable[[str], None], ended_at: Callable) -> dict:
    """The season loop `play` shares between its two worlds: one `SeasonDriver` on `chooser(w)` behind `dispatching_chooser(auto, overrides)`, the digest and
    each faction's standing after every season, `ended_at(n)` asked after it (the realm's never ends it: the count runs whole), and `loop_closed` over the
    whole log at the end."""
    verbs = verbs or resolvable_verbs()
    choose = dispatching_chooser(chooser(w, verbs=verbs), overrides or {})
    d = SeasonDriver(w)
    ran, ended = 0, None
    for n in range(1, seasons + 1):
        since = len(w.log)
        d.season(choose, None, contest_max_depth=w.fixtures.get("contest_max_depth"))
        ran = n
        out(f"season {n}:")
        # `digest` is one line per occurrence; the shipped chooser repeats the same refused act, so the printed season folds equal lines into `(xN)`
        for line, times in Counter(digest(w, since)).items():
            out(line + (f" (x{times})" if times > 1 else ""))
        for line in standing_lines(w):
            out(line)
        ended = ended_at(n)
        if ended:
            break
    ended = ended or "the season count was reached"
    out(f"ended after {ran} season(s): {ended}")
    loop = loop_closed(w, 0)
    out(loop_line(loop))
    return {"world": w, "ended": ended, "seasons": ran, "acts": [], "loop": loop}


def _callback(w: World, chosen: tuple, verbs, out: Callable[[str], None]) -> Callable:
    """The player's `play_surface` callback: `offered` printed, then `chosen` through `development_space` at the first deliberation, the shipped order after.
    ⚠ The act-id mint and the draw are `boot/chooser.py::chooser`'s own two lines, repeated: that function builds them inside and exposes neither, and a
    space built on a different mint or draw is a different candidate set (`development_space`'s docstring)."""
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    draw = draw_factory(w.world_seed, lambda: w.tick)
    rank = make_ranker(w.fixtures, verbs, draw)
    spent = []

    def pick_of(sheet) -> Sequence[int]:
        if spent:
            return range(len(sheet.candidates))
        spent.append(True)
        return chosen
    space = development_space(w.fixtures, mint, pick_of, verbs, draw)

    def callback(p, v, s, ask_budget, auto) -> list:
        if not spent:
            for line in offered(p, v, s, ask_budget, auto, rank=rank):
                out(line)
        return space(p, v, s, ask_budget, auto)
    return callback


# ---------------------------------------------------------------------------------------------------
# B24.15 -- THE HEARING SCENARIO (HEAR_B edit 9): `build_hearing`, the world `harness/scenarios.py::SCENARIOS["hearing"]` plays.
# ---------------------------------------------------------------------------------------------------
HEARING_VENUE, HEARING_PLACE = "lr_settlement_a", "lr_hearth_a"     # where the sitting is held / where the matter lives: the spine's first chain, a settlement and a hearth under it
ACCUSER, ACCUSED = "lp_accuser", "lp_accused"
ACCUSER_SEAT, CHARGE = "lo_accuser", "prop:hear:charge"
EXHIBITS = 3                                                          # `IS-B2` §1.0: "two parties each with three filed exhibits"


def build_hearing(seed: int = 0, exhibits: tuple = (EXHIBITS, EXHIBITS)) -> World:
    """THE HEARING WORLD (HEAR_B edit 9, `IS-B2` §1.0): the spine (`build`), with the sitting's opening made by the game's own acts through the fold at tick 0, as `inquiry_world`'s
    premise is (`_open`: a refusal stops the build, naming the Event):
      * a SITTING THAT FIRED -- the Mayor of `HEARING_VENUE` `convene`s it, and CALENDAR and WITNESS run once, so a Date is due and fired, a slot is formed on the docket and the
        bench holds the claim that it fired (`world_q.sittings_before`);
      * a CASE FILE and a DOCKET ITEM that names it (`DOCKET_CASE`) -- the Mayor `open_case`s `ACCUSED`, which fills the slot (a computed case: it is heard under the `default` rite);
      * A BENCH -- the spine's own seats over the venue (each carries `determine` in the remit `remit_or_default` fills), and `ACCUSER`'s: a magistrate's seat scoped to the
        venue that may `determine`, so the accuser is a seat-holder who brings the matter and the presiding seat is another's (`sigma.proceeding_input`: the bearer is `for`);
      * TWO PARTIES holding `exhibits` Records each, `(accuser's, accused's)`, three apiece unless a caller asks for another hand (`create_record`, folded; FI is stubbed by
        planted state, no inquiry verb runs). They are what `sigma._items_of` reads as a party's items today (the Records he holds); the case file's own `filed` stages are
        B24.25's (`speak` writes them), so none is planted here.
      * THE SEATED ACCUSER is a person of his own sheet: a `justice` pursuit and a `commit` to an OUGHT whose subject is the accused (his charge), so the sitting question is
        the first he answers (`world_q.attention_key`, tier 0) and `determine` of the accused is among his candidates.
    The world runs at its OWN arm of two settings, set here and nowhere else (the shipped realm is a separate world that ships `sitting_exchanges` 1 as well; the `.sweep` here is this fixture's own arm, kept so the world does not move with the shipped value): `sitting_exchanges` 1 (the attendees'
    effort is exchanges) and `npc_decider_roles` naming the proceeding role (the NPC attendees decide by a draw over their own interior). The opening acts are folded at the flat
    fold (no task draw); the world plays at its own arm. Returns the world at tick 1, the sitting due."""
    from ..seam.wrappers.sigma import PROCEEDING_ROLE
    from .flat_fold import flat_fold_fixtures
    w = build(seed)
    played = w.fixtures.sweep("sitting_exchanges", 1).sweep("npc_decider_roles", (PROCEEDING_ROLE,))
    attrs = lambda pid: generated_attributes(w.world_seed, pid, w.fixtures.get("generated_attribute_range"))
    place_person(w, ACCUSED, "the accused", HEARING_PLACE, attributes=attrs(ACCUSED))
    place_person(w, ACCUSER, "the accuser", HEARING_VENUE, attributes=attrs(ACCUSER), pursuits={"justice": 1.0})
    w.offices[ACCUSER_SEAT] = Office(ACCUSER_SEAT, "Magistrate", HEARING_VENUE, remit_or_default([]), scope_rung=HEARING_VENUE, faction=SPINE_FACTION)
    w.add_tenure(Tenure("lt_hold_accuser", ACCUSER, ACCUSER_SEAT, "hold", 0))
    w.propositions[CHARGE] = Proposition(CHARGE, "OUGHT", ACCUSED, "answers to the bench", True, 0)
    w.add_tenure(Tenure("lt_commit_accuser", ACCUSER, CHARGE, "commit", 0))
    mayor, seat = _holder_of(w, f"lo_{HEARING_VENUE[3:]}"), f"lo_{HEARING_VENUE[3:]}"
    w.fixtures = flat_fold_fixtures(w.fixtures)
    try:
        d = SeasonDriver(w)
        _open(w, d, Act(id="hear:convene", actor=mayor, verb="convene", via=seat, payload={"subject": HEARING_VENUE, "when": w.tick}))
        w.step = Step.CALENDAR
        fired = d.calendar(mint_token(w, WriteClass.CALENDAR))                       # the Date is due this tick: it fires, and the bench is told
        w.log.extend(fired)
        d.witness(mint_token(w, WriteClass.INTERIOR), fired)
        _open(w, d, Act(id="hear:case", actor=mayor, verb="open_case", via=seat, payload={"subject": ACCUSED}))
        for who, held in zip((ACCUSER, ACCUSED), exhibits):
            for n in range(held):
                _open(w, d, Act(id=f"hear:file:{who}:{n}", actor=who, verb="create_record", payload={"kind": "text"}))
    finally:
        w.fixtures = played
    w.tick = HEARING_OPENS
    return w


# B24.38 (IS-B2-SC-08) -- HOW A SITTING ENDED, AND WHAT ITS ENDING WROTE. Computed over the log and the case file, stored nowhere.
HEARING_ENDINGS = ("carried", "carried_in_part", "dismissed", "adjourned", "lapsed", "agreed", "parted")     # the one owner of the seven names; `scenarios.SCENARIOS["hearing"].kinds` keys them
# [JUSTIFIED: tick 1: the tick `build_hearing` hands the world at (the opening acts are folded at tick 0), so an Event before it is the premise's; a tick of the world, not a tunable.]
HEARING_OPENS = 1
_DISPOSAL = frozenset(k for ks in VERB_TABLE["determine"].emits_by_degree.values() for k in ks) - frozenset(matrix_row("Person", "pursuits").emits)   # `determine`'s band kinds, its pursuit move out


def _matter_of(w: World, e) -> Optional[str]:
    """The `subject` of the act that caused Event `e` (the matter a verb is about), `None` where no act did or the act names none."""
    a = causing_act(w, e)
    return a.payload.get("subject") if a is not None and isinstance(a.payload, dict) else None


def sitting_events(w: World, matter: str) -> list:
    """The Events, in log order, of every SITTING HELD on `matter` since the opening: the disposal Events (`determine`'s band kinds, never its refusal or its vote, which carry no sitting) of
    a `determine` act whose subject is `matter`."""
    return [e for e in w.log if e.kind in _DISPOSAL and e.emitted_at >= HEARING_OPENS and world_q.ending_arrangement(e) is not None
            and getattr(causing_act(w, e), "verb", None) == "determine" and _matter_of(w, e) == matter]


def hearing_ending(w: World, matter: str) -> str:
    """HOW THE LAST SITTING HELD ON `matter` ENDED: one of `HEARING_ENDINGS`, read off the log (its Event's beats, card and band) and nothing else; no sitting held is `lapsed`. In this order:
      * `adjourned`       -- the sitting's last move was the bench's `adjourn` (`world_q.adjourned_by`; it ends `budget`, B24.06): the matter is put off to a later sitting;
      * `agreed`/`parted` -- NOBODY DECIDES (`card.decided_by` empty: a consent room, where each party's own accept is the act): `agreed` where the sitting ended `yielded` (an accept is `ended
                             == "yielded"`), `parted` where it ended any other way. [No consent sitting is hosted until B28 (`_eff_determine`, B24.31), so neither is reached today.]
      * `dismissed`       -- the band is `Failure`: `matter.undetermined`, which `determine` emits where the room heard the matter and disposed of nothing
                             [ASSUMPTION: `dismissed` reads `matter.undetermined` until B27's acquittal makes it reachable as the row's own -- basis: `verb_table.yaml: determine` emits it at Failure today];
      * `carried_in_part` -- the band is `Partial` (the held matter: the disposal opens graded `Partial`);
      * `carried`         -- `Success` or `Overwhelming`: the disposal opens at that band.
    The LAST sitting is the matter's present standing; an earlier one's ending is not what the matter now is."""
    held = sitting_events(w, matter)
    if not held:
        return "lapsed"
    e = held[-1]
    if world_q.adjourned_by(world_q.ending_beats(e)) is not None:
        return "adjourned"
    if not world_q.ending_card(e).decided_by:
        return "agreed" if world_q.ending_sitting(e).ended == "yielded" else "parted"
    if e.degree == DEGREE_LABEL[Degree.FAILURE]:
        return "dismissed"
    return "carried_in_part" if e.degree == DEGREE_LABEL[Degree.PARTIAL] else "carried"


def sitting_exchanges(w: World, matter: str) -> int:
    """The items the sittings held on `matter` entered or struck: `world_q.ending_exchanges` summed over their Events."""
    return sum(len(world_q.ending_exchanges(e)) for e in sitting_events(w, matter))


def sitting_writes(w: World, matter: str) -> Counter:
    """THE DURABLE WRITES THE MATTER'S EVENTS MADE since the opening (A-81: no ending leaves the stage bare), by kind: `stages` -- the case-file stages that are no clock's (an exchange, an
    adjournment, a filed, excluded or answered item) on each case file an Event of the matter wrote; `tenures` -- Tenures opened or closed by them; `claims` -- `claim.deposited` Events caused by
    them, the claims their witnesses were given. The Events are the sittings' own (`sitting_events`: the disposal Events of the `determine`s on `matter`), not every act that names it, so an
    ending's count is what its sitting wrote; `stages` reads the whole of each case file such an Event wrote, a sitting's filed items among them. A `determine`'s budget debit is not a write
    and is not counted. A reader: it changes nothing, and each cell reads 0 where nothing of its kind was written."""
    mine = {e.id for e in sitting_events(w, matter)}
    tenures = {t.id for t in w.tenures}
    files, opened = set(), 0
    for e in w.log:
        if e.id in mine:
            files.update(c.subject for c in e.changes if c.subject in w.records)
            opened += sum(1 for c in e.changes if c.subject in tenures)
    return Counter(stages=sum(1 for f in files for st in w.records[f].stages if not is_clock_stage(st)), tenures=opened,
                   claims=sum(1 for e in w.log if e.kind == "claim.deposited" and any(c in mine for c in e.causes)))


# B24.32 -- THE RUN'S SHAPE (KERN_B "What is carried": `narrative.py`'s four arcs, read in the harness over the sitting's own beats). Computed, stored nowhere.
RUN_SHAPES = ("rout", "reversal", "collapse", "split")
PLAIN = "plain"                      # a run that is none of the four (the kernel's clear win, nail-biter and deadlock are not carried)
# [canonical: ROUT_MARGIN of the retired SC05 kernel's `narrative.py` (B24.33; its four rules are in 1a19cf74e's body) -- a [SEED] there as here, Jordan-calibratable; the lean it reads is `Beat.mood`, the room's lean toward `for` in -1..1]
ROUT_MARGIN = 0.30


def run_shape(exchanges: Sequence, carried: Optional[bool] = None) -> str:
    """THE SHAPE OF A RUN, one of `RUN_SHAPES` or `PLAIN`, read over `Outcome.beats` (`exchanges`, in order). The room's lean toward `for` at each exchange is that `Beat.mood`
    (the weighted mean of the deciders' tracks, -1..1); the side who WON is the one the close carried (`carried`: True `for`, False `against`, as the host reads
    `Outcome.verdicts`), else the side the room leans to at the end. In the order they bind:
      * `collapse` -- the run ENDS ON A FAULT: its last exchange recorded one (`Beat.fault`), so it was settled by what a side did and not by the merits;
      * `split`    -- the close went the other way from the room: the room leans to one side at the end (the last `Beat.mood` is not 0) and the close carried the other's;
      * `reversal` -- the winner CROSSED from behind to ahead in the back half of the run (a crossing at or after the midpoint of the exchanges);
      * `rout`     -- the winner was NEVER behind at any exchange and the room leans past `ROUT_MARGIN` to him at the end.
    Anything else is `PLAIN`, and so is a run of no exchanges, and (only where `carried` is `None`) one the room ends level: a given `carried` names a winner even over a level end, so it
    may still read `reversal`. It reads nothing but the beats and the one `carried`; the module records no shape."""
    beats = tuple(exchanges)
    if not beats:
        return PLAIN
    if beats[-1].fault is not None:
        return "collapse"
    leads = [(b.mood > 0) - (b.mood < 0) for b in beats]          # the sign of the room's lean after each exchange
    room = leads[-1]
    win = room if carried is None else (1 if carried else -1)
    if room and win != room:
        return "split"
    if not win:
        return PLAIN
    if any(leads[k] == win and leads[k - 1] == -win for k in range(max(1, len(leads) // 2), len(leads))):
        return "reversal"
    if abs(beats[-1].mood) > ROUT_MARGIN and -win not in leads:
        return "rout"
    return PLAIN


def main(argv: Optional[Sequence[str]] = None) -> int:
    """`governance_spine` prints the census; `governance_spine play SEED SEASONS {vacancy|order|succession|recall} [--player ID] [--pick I,I,...]` plays a scenario,
    and `governance_spine play SEED SEASONS --world realm` reads the built realm (no situation, no player), both ending in `loop_closed`'s line.
    Seed and seasons have no default (this file is inside `tools/ci_sim_fabrication_check.py`'s scope; `harness/storybar.py` gives the same reason).
    `--pick ''` shows the offer and takes nothing; no `--pick` is the control, the shipped chooser for everyone."""
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        import json
        print(json.dumps(census(build(0)), indent=2, sort_keys=True))
        return 0
    ap = argparse.ArgumentParser(prog="governance_spine")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pl = sub.add_parser("play", help="play a scenario on the governance test world")
    pl.add_argument("seed", type=int)
    pl.add_argument("seasons", type=int)
    pl.add_argument("situation", nargs="?", choices=SITUATIONS, default=None, help="named for the spine, absent for --world realm")
    pl.add_argument("--world", choices=WORLDS, default="spine", help="spine: the governance test world and a situation; realm: the built realm, nobody played")
    pl.add_argument("--player", default=None, help="a person id; default the Duke of the first chain (default_player)")
    pl.add_argument("--pick", default=None, help="comma-separated candidate indices, spent at the first deliberation; '' shows the offer only")
    a = ap.parse_args(argv)
    pick = None if a.pick is None else tuple(int(x) for x in a.pick.split(",") if x.strip())
    play(a.seed, a.seasons, a.situation, a.player, pick, world=a.world)
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
