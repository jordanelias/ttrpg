"""`loop/sides.py` -- WHO CONTESTS, WHEN THE PRIZE BELONGS TO `mass_battle` RATHER THAN A
PERSON-TO-PERSON SUBSYSTEM (M4, `ED-IN-0279` clause (a)).

`_target = payload.get("subject")` names a PERSON for `kill / wound`'s victim and `tell`'s
addressee, and the fold's own `_parties = [a.actor, _target]` was never wrong for that shape.
`march`'s subject names the settlement being marched on, and putting a Rung id into a
PERSONS-ALWAYS claimant list (`seam/contest.py`'s S39.1) would be exactly the violation that
invariant exists to catch.

⚠ **DISPATCHING ON THE SHAPE OF `target` (person vs. rung) IS UNSAFE, AND THIS MODULE'S FIRST
WRITING DID EXACTLY THAT -- FOUND BY THE CORPUS SUITE, NOT REASONED OUT IN ADVANCE.**
`ARC-40`'s `tell` binds a Candidate subject to `r_realm`, the campaign root RUNG -- news can be
ABOUT a place -- and a shape-based dispatch routed it into the army-muster branch, which found no
seat (`tell`'s eligibility is `own`, never `remit:`) and returned `claimants=[]`, tripping
`seam/contest.py`'s own `Forbidden("contest with no claimants")`. A person-shaped subject and a
rung-shaped subject are NOT one-to-one with which sides a contest needs; `tell` proves it.

THE ACTUAL DISCRIMINANT IS THE PRIZE'S OWN SUBSYSTEM, read the same way `contest_subsystem`
already reads it (`ED-SC-0033` clause (1): *"the seam dispatches by manifest ROW rather than the
hardcoded personal_combat literal"*) -- never the verb's name, and never the accident of what a
candidate's subject happens to resolve to. A prize routed to `mass_battle` needs an ARMY on each
side; every other prize needs the two-person shape every contested verb has used since `kill /
wound`. `sides_of` takes the PRIZE, not the target's type, as what it branches on."""

from __future__ import annotations

from typing import Optional

from .. import manifest
from ..data.rosters import faction_prop_id
from ..queries.world_q import ancestry, holder_faction_of, home_of, mustered
from ..state.carriers import Act
from ..state.world import World


def sides_of(w: World, a: Act, target: Optional[str],
             prize: str) -> tuple[list[str], Optional[str], str]:
    """`(claimants, subject, rung)` for `contest()`, given the act's own `payload["subject"]`
    and the PRIZE its verb row contests.

    TWO SHAPES, dispatched on `manifest.resolve("contest", prize)["module"]`:

    - NOT `mass_battle` (`the body`, `a standing`, `a proposition` -- every prize before M4):
      UNCHANGED from the pre-M4 fold. `claimants = [a.actor, target]` (or `[a.actor]` alone when
      `target` is absent or IS the actor), `subject = target`, `rung` = the pre-M4 placeholder
      (`a.payload` if it happens to be a bare string, else `"R"`) -- nothing reads it for this
      shape and nothing should start relying on it here.

    - `mass_battle` (`a field`, `march`'s prize): `claimants` is the MUSTERED ARMY at the actor's
      own nearest settlement, under the FACTION OF THE OFFICE THE ACT WAS EXERCISED THROUGH --
      `a.via`, `exercised_seat`'s own field (`decision/options.py`), read here rather than
      re-derived, because the chooser already computed which seat granted the act and the fold
      trusts the same value everywhere else it appears (`_eligible`'s `remit:` branch,
      `loop/resolve.py`). `subject` is the DEFENDING faction -- `world_q.holder_faction_of(w,
      target)`, which walks `target`'s own ancestry to the nearest HELD rung (a settlement is
      never itself the object of a `hold` in this corpus) and reads that holder's faction.
      `rung` is `target` itself: the place a field battle scopes its defence to
      (`world_q.mustered`, called by the provider). `target` is TRUSTED to be a Rung here --
      `march`'s own `requires: existence of: subject kind: Rung` is what makes that true, not
      this function re-checking it.

      ⚠ `Office.faction` IS A DISPLAY VALUE (`'Crown'`), NOT A PROPOSITION ID (`'fac_crown'`) --
      `Proposition.value`, not `.id`. `mustered`/`members` key on the id, via `commit`'s own
      `t.object`. `faction_prop_id`, `data/rosters.py`'s *"ONE OWNER OF THE FACTION-ID
      RELATION"*, converts one to the other -- its own docstring names the exact failure of
      skipping this step: *"a silently empty query"*, `leaders()` returning `[]` for every
      faction once `populated.py` formed the id inline instead of through the one owner.

    ⚠ AN ACTOR WITH NO SEAT, NO HOME, OR NO SETTLEMENT ABOVE THEM MUSTERS AN EMPTY ARMY, NOT A
    RAISE. `contest()`'s own PARTY-GAP discipline is the caller's to apply -- `claimants=[]`
    reaches `combat.py`/`sigma.py`/`mass_battle.py` exactly as an empty list from any other route
    would, and each already refuses it by name. Manufacturing a refusal here would be a second
    copy of a rule `seam/wrappers/*` already owns (§8)."""
    prize_row = manifest.resolve("contest", prize)
    if prize_row is not None and prize_row.get("module") == "mass_battle":
        office = w.offices.get(a.via)
        faction = faction_prop_id(office.faction) if office is not None and office.faction else None
        home = home_of(w).get(a.actor)
        chain = ancestry(w, home) if home is not None else []
        origin = next((r for r in chain if w.rungs.get(r) is not None
                       and w.rungs[r].kind == "settlement"), None)
        claimants = mustered(w, origin, faction) if origin and faction else []
        # ⚠ `H-149` (`march_target_kinds`, closed at `[settlement]`) IS ENFORCED HERE, NOT LEFT
        # DECLARED-AND-UNREAD (found by `valoria-critic`: `_eff_march`'s own comment claimed this
        # check and it did not exist). `requires_typed` only answers *does a Rung of this id
        # exist*, never a sub-kind filter (`march`'s own `requires_typed_note` -- a sixth typed
        # form is the second resolver S27.2 refuses), so the kind check has to live where the
        # target's Rung object is already in scope. A non-settlement target forces `subject`
        # `None`, which is the SAME shape `holder_faction_of` returning `None` already is --
        # `_contest`'s PARTY-GAP catch (M4, found in the same pass) refuses it gracefully, one
        # mechanism for both "no legitimate defending scope exists" causes rather than two.
        # ⚠ THE KIND CHECK IS INLINE, MARCH-SPECIFIC BUSINESS LOGIC IN A FUNCTION WHOSE OWN
        # CONTRACT IS "DISPATCH BY THE PRIZE'S SUBSYSTEM, NEVER THE VERB" -- disclosed (M4 review
        # pass, `/simplify` altitude finding), not fixed. `sides_of` takes `prize`, not `verb`,
        # specifically so it stays verb-agnostic; a second `mass_battle`-routed verb with a
        # different target-kind rule would have nowhere generic to read one from. The deeper fix
        # is a target-kind constraint carried as DATA (a manifest or verb-row field, read the way
        # `manifest.resolve(...)["module"]` already is), not this `w.rungs[target].kind` check --
        # left for a future session, since `march` is still the only `mass_battle`-routed verb.
        target_kind = w.rungs[target].kind if target is not None and target in w.rungs else None
        subject = (holder_faction_of(w, target)
                   if target is not None and target_kind == "settlement" else None)
        # ⚠ A TARGET HELD BY THE ACTOR'S OWN FACTION, WITH THAT FACTION'S OWN PEOPLE PRESENT TO
        # MUSTER AS "DEFENDERS", IS NOT REFUSED HERE -- found in the same pass, NOT fixed, on
        # purpose. Jordan's verbatim ruling frames march as meeting an OPPOSITION army, which a
        # same-faction target is not; but `test_an_unopposed_march_writes_nothing_on_either_side`
        # already relies, correctly, on a same-faction EMPTY target resolving `Unopposed` rather
        # than refusing -- and this function has no cheap way to tell "empty" from "occupied by
        # my own people" without calling `mustered` a second time (the wrapper's own job) just to
        # decide. Refusing unconditionally on `subject == faction` breaks that test; refusing only
        # when non-empty needs the duplicate call. Left OPEN rather than guessed either way --
        # see `H-150`-adjacent note in `hole_register.yaml` (M4 review pass) for the disclosure.
        return (claimants, subject, target or "R")
    # EVERY OTHER PRIZE: the pre-M4 fold's own construction, byte-for-byte.
    rung = a.payload if isinstance(a.payload, str) else None
    return ([a.actor] + ([target] if target and target != a.actor else []), target, rung or "R")
