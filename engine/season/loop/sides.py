"""`loop/sides.py` -- WHO CONTESTS, WHEN THE PRIZE BELONGS TO `mass_battle` RATHER THAN A
PERSON-TO-PERSON SUBSYSTEM (M4, `ED-IN-0279` clause (a)).

`_target = payload[row.counterparty or "subject"]` names a PERSON for `kill / wound`'s victim
(`subject`) and `tell`'s addressee (`to`, its counterparty), and the fold's own `_parties =
[a.actor, _target]` was never wrong for that shape.
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
from ..data.rosters import MARCH_TARGET_KINDS, faction_prop_id
from ..queries.world_q import (
    DETAIN_KIND, ancestry, holder_faction_of, home_of, mustered, restrained,
)
from ..state.carriers import Act
from ..state.world import World


def sides_of(w: World, a: Act, target: Optional[str],
             prize: str) -> tuple[list[str], Optional[str], str]:
    """`(claimants, subject, rung)` for `contest()`, given `target` -- the act's
    `payload[row.counterparty or "subject"]`, its opponent -- and the PRIZE its verb row contests.

    TWO SHAPES, dispatched on `manifest.resolve("contest", prize)["module"]`:

    - NOT `mass_battle` (`the body`, `a standing`, `a proposition` -- every prize before M4):
      UNCHANGED from the pre-M4 fold. `claimants = [a.actor, target]` (or `[a.actor]` alone when
      `target` is absent or IS the actor), `subject = target`, `rung` = the pre-M4 placeholder
      (`a.payload` if it happens to be a bare string, else `"R"`) -- nothing reads it for this
      shape and nothing should start relying on it here.

    - `mass_battle` (`a field`, `march`'s prize): `claimants` is the MUSTERED ARMY at the actor's
      own nearest settlement, under the FACTION OF THE OFFICE THE ACT WAS EXERCISED THROUGH --
      `a.via`, `seat_of`'s own field (`decision/options.py`), read here rather than
      re-derived, because the chooser already computed which seat granted the act and the fold
      trusts the same value everywhere else it appears (`_eligible`'s `remit:` branch,
      `loop/resolve.py`). `subject` is the DEFENDING faction -- `world_q.holder_faction_of(w,
      target)`, which walks `target`'s own ancestry to the nearest HELD rung (a settlement is
      never itself the object of a `hold` in this corpus) and reads that holder's faction.
      ⚠ SINCE v9 IN-13 (#453 §9.6): `subject` is `None` when the target's holder IS the actor's
      faction or nobody holds it -- no opposing side, which the provider answers `Unopposed` and
      the effect answers with the army's arrival -- and a target outside `MARCH_TARGET_KINDS`
      musters `claimants = []` (H-149's refusal, moved off `subject`).
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
        # v9 SC-03a (#453 §10.4 step 3, K-53): A PRISONER IS NOT IN THE ARMY. Every claimant holding
        # a live `detain` is excluded (`world_q.restrained`, the custody's one read), order kept. ⚠
        # THE ATTACKING SIDE ONLY, AND THAT IS NAMED, NOT SETTLED: the DEFENDERS are mustered by the
        # provider (`seam/wrappers/mass_battle.py`, `mustered` at the target), which #453 does not
        # name as a reader; moving the exclusion into `mustered` itself would cover both sides from
        # one owner and is the cleaner home, left to the lane that owns that wrapper.
        claimants = [p for p in claimants if not restrained(w, p, DETAIN_KIND)]
        # ⚠ `H-149` (`march_target_kinds`, closed at `[settlement]`) IS ENFORCED HERE, NOT LEFT
        # DECLARED-AND-UNREAD (found by `valoria-critic`: `_eff_march`'s own comment claimed this
        # check and it did not exist). `requires_typed` only answers *does a Rung of this id
        # exist*, never a sub-kind filter (`march`'s own `requires_typed_note` -- a sixth typed
        # form is the second resolver S27.2 refuses), so the kind check has to live where the
        # target's Rung object is already in scope. A non-settlement target musters an EMPTY army
        # (since v9 IN-13; it forced `subject` `None` until then, when `None` also meant an unheld
        # target and both refused) -- `_contest`'s PARTY-GAP catch (M4) refuses it gracefully, and
        # an unheld settlement, which IS a legitimate destination, now arrives (`Unopposed`).
        # ⚠ THE KIND CHECK IS INLINE, MARCH-SPECIFIC BUSINESS LOGIC IN A FUNCTION WHOSE OWN
        # CONTRACT IS "DISPATCH BY THE PRIZE'S SUBSYSTEM, NEVER THE VERB" -- disclosed (M4 review
        # pass, `/simplify` altitude finding), not fixed. `sides_of` takes `prize`, not `verb`,
        # specifically so it stays verb-agnostic; a second `mass_battle`-routed verb with a
        # different target-kind rule would have nowhere generic to read one from. The deeper fix
        # is a target-kind constraint carried as DATA (a manifest or verb-row field, read the way
        # `manifest.resolve(...)["module"]` already is), not this `w.rungs[target].kind` check --
        # left for a future session, since `march` is still the only `mass_battle`-routed verb.
        # ⚠ AGAINST THE ROSTER, NOT A HARDCODED `"settlement"` STRING (M4 review pass, a second
        # correctional finding: the first writing checked the literal string, so extending
        # `march_target_kinds` later would still change nothing here -- exactly the
        # declared-but-unread defect this check exists to close, reintroduced one level down).
        target_kind = w.rungs[target].kind if target is not None and target in w.rungs else None
        # v9 IN-13 (#453 §9.6 code edit (iii), §14.8): H-149's REFUSAL NOW RIDES AN EMPTY ARMY, NOT
        # `subject = None`. A non-settlement target musters nobody, so the wrapper's existing
        # empty-`claimants` PARTY-GAP refuses it exactly where it always refused (`_contest`'s catch,
        # `march.refused`), and `subject = None` comes to mean ONE thing only: no opposing holder.
        if target is None or target_kind not in MARCH_TARGET_KINDS:
            return ([], None, target or "R")
        # THE STAKE IS DERIVED AT THE DESTINATION, NEVER DECLARED (#453 §9.6 code edit (i), H-151's
        # reverted fix restored): `holder == mine` -- a relocation (or, if an enemy march follows, a
        # defence) -- and `holder is None` -- arrival at unheld land, no title write (H-166) -- both
        # name NO opposing side, and the wrapper answers `subject = None` with its `Unopposed` shape.
        # Only another holder is a capture attempt: opposed if its people are mustered there,
        # unopposed if not (the wrapper's `mustered` read decides which; this function does not
        # call it a second time). So a same-faction target no longer musters the actor's own people
        # as "defenders" (H-151), and its EMPTY case stays `Unopposed` as it always resolved.
        holder = holder_faction_of(w, target)
        subject = None if holder is None or holder == faction else holder
        return (claimants, subject, target)
    # EVERY OTHER PRIZE: the pre-M4 fold's own construction, byte-for-byte.
    rung = a.payload if isinstance(a.payload, str) else None
    return ([a.actor] + ([target] if target and target != a.actor else []), target, rung or "R")
