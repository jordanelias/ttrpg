# MB · the field as a playable game: a scenario, choices before and during, a report after, armies that exist

## Status: PROPOSED

Lane MB, with named dependencies on CORE, CHAR, SE and PC. Carries R-07, R-11, R-17, R-20, R-22 of
`audits/04_MB_audit.md` §6.2 and its §8 steps 4, 4a, 4b, 5, 5a, 5b, 6. Assumes
`04_MB_headcount_grade_and_scale.md` and the outcome record of `04_MB_typed_outcome_and_one_path.md`.
Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

In order of landing: (1) nothing in a shipped season, a harness scenario only; (2) with a decider absent,
nothing (the played mode is the same call with a decider); (3) two declared hash movers: preset armies
installed at realm build, and the army and order verbs offered to the people who hold them; (4) the
aftermath writes on `Won`. After (3) a seeded realm fights fields with armies in natural play.

## The problem (audit F-MB-03, F-MB-15, F-MB-16; §9; §17; §18)

There is no scenario that exercises only this subsystem; every choice surface that exists is withheld or
off; nothing can be decided once a field starts; nothing explains the result; the non-player commander is
one fixed doctrine folded outside the chooser; and in natural play no field is fought (seed 0, two seasons,
with and without preset armies). Measured at army scale: an even 18-tick engagement is usually indecisive
(spearmen 600 v 600, seed 5: 0 and 36 casualties, no rout; over 72 ticks, 93 and 104, still no rout), so
a game made of single engagements is a game of draws unless a draw is a state a commander acts on.

The stated referents describe the missing parts (sourced in the audit's §18): standing orders set in
advance and a predicted outcome shown before the fight (Unicorn Overlord, `tutorials/T19`); instructions
before the match, shouts and changes during it, a review after (Football Manager 26, `tutorials/T16`);
fight, delegate or withdraw at contact (Total War, `tutorials/T07`); command, send troops or
auto-resolve (Bannerlord, `tables/R2`, memory-grade for the three-way menu). The archived design had the
same shape: three legal points at which a battle may be entered, a general's action each turn, an
aftermath scene with choices.

## The resolution, decided

### A. The scenario and its instrument (alone; no shipped behaviour moves)

New `engine/season/harness/field_scene.py`:

- `build(seed) -> World`: two factions; each with a seat whose remit grants `march` and `marshal`, an
  army Record minted and filled through the real verbs from cohorts with real training Sites (so the
  doctrine has a barracks, a range and a stable to use), a settlement each, one garrisoned; stores at
  both treasuries. Built with `Fixtures` overrides that un-withhold the army verbs, `marshal` and
  `surrender` and roster `march_postures: [storm, besiege]` **for this world only**.
- `play(w, policies, seasons) -> Report`: runs `SeasonDriver.season` with
  `play_surface.dispatching_chooser`; `policies` maps a person to a callback (the player-proxy) or leaves
  him to `auto`. A policy sees `military_menu.menu`, `field_estimate` and, once a field is drawn, the
  last `FieldOutcome`.
- `Report`: per field, the estimate shown, the choices taken, the outcome record, each named person's
  `body` and stance before and after, where everyone stands.

End condition of the scenario: one faction's seat holds both settlements (`seize` after occupation), or a
`surrender`, or the season cap.

### B. Choices during a field: the same call with a decider (step 4a)

`modules/mass_battle/massbattle.py::resolve_field(inp, rng, *, troops_a=None, troops_b=None, decide=None)`.

- `battle_loop.run_battle` gains `on_phase: Optional[Callable]`, called where `phase_boundary` is called
  today (ticks 6 and 12), after it. `None` is today's loop exactly.
- `resolve_field` wraps the host's `decide` so it never sees a `Unit`: it is handed a frozen
  `FieldPhaseView(phase, side, parts=((id, share, routed), ...), enemy_in_contact: bool)` for **its own
  side only** and returns a `PhaseOrder(approach, retreat)` or `None`. `approach` is one of the roster
  `advance | line | defend` (the army strategies, `orderofbattle.STRATEGIES`), applied as the stance of
  each class of subformation exactly as `_spec_for` applies a strategy at deployment; `retreat: True`
  sets the `retreat` stance and `conceded` on every subunit, the primitive `_retreat_orders` already uses.
- `engine/season/seam/wrappers/mass_battle.py::resolve` forwards `host.decide` when the host plays a
  claimant or the defending commander, as `seam/wrappers/combat.py:394-395` does for a duel (REM-31; the
  ratified `proposals/2026-10-07-grid-mode-suspension.md`). The `host` keyword is already in the
  signature.
- A side nobody plays has no decider: its standing instructions (`fall_back_at`, `retreat_at`, the
  strategy) are the decision, as today.

This is one resolver at two fidelities with nothing forked, which is what the 2026-07-08 doctrine rules
for every scale.

### C. Choices between engagements

With `Drawn` (proposal `04_MB_headcount_grade_and_scale.md`) both armies remain where they were. The next
round's acts are ordinary acts by the people involved: `march` again (a second engagement on the
survivors, since cohort bodies carry the losses), `march` with `posture: besiege`, `marshal` a retreat
line, `surrender`, or nothing. No new verb.

### D. The report (step 4b)

`FieldOutcome.report: tuple` of at most three `PhaseSummary(phase, attacker=(lost_share, parts_broken),
defender=(...), flanked: (bool, bool))`, built in `massbattle.py` from the engine's own trace categories
(`casualty`, `melee`) with `resolution.tracing()` opened inside the call and closed before it returns.
`_eff_march` writes `broke_observed` for both sides and one `Observation` per phase summary on the band
Event (an Event has no payload field; Observations are its carrier, as CP-T04-01 established). A
bystander's account of a battle is then something `tell` can carry.

### E. Armies that exist, and commanders who choose (steps 5, 5a; declared movers)

- `engine/season/harness/populated.py::build_realm`: after the cast is seated, `army_presets.install(w)`
  when `Fixtures army_presets` is `on` (new fixture, shipped `off`; the flip is its own commit).
- Realm data (SE's file): one training Site of each kind at each faction's seat settlement, so the
  doctrine raises more than levy. Without it the realm's armies are levy alone, which the measured run
  shows barely fight (14 of 20 indecisive at 900 v 600, survivors 0.98 and 0.96).
- `modules/mass_battle/troop_types/presets.py::ROLE_OF['levy']`: `'Hold'` in place of `'Reserve'`: a
  levy line stands as a line. (The archived design restricts levy to its home territory; the code has no
  such rule. Whether to add it is a design call for FA and is not made here.)
- The doctrine becomes data: `ARM_SHARES` moves to a typed file under `engine/engine_params/` keyed by a
  doctrine name (`balanced` = today's 45/25/20; at least `foot`, `horse`, `missile` beside it). The
  commander's `create_record` act names the doctrine; which one a given leader picks is the chooser's,
  on cells CHAR owns. `plan(q)` reads `q.doctrine`.
- `harness/army_presets.py::install` issues its commands through `military_menu.callback` and
  `dispatching_chooser` (CR-52's build) instead of folding them directly.
- `engine/season/data/verbs.py::opportunity_key`: for a verb in `ARMY_VERBS` the key includes a digest of
  the payload, so a commander may give several army commands in a season.
- `marshal` fans `retreat_at` only (three candidates, not forty-five); the role key leaves the standing
  order (audit §5.4, H-361).
- `Fixtures field_subunits: person` (in proposal 1) and, after the above, `withheld_verbs` loses the army
  verbs, `marshal` and `surrender` (a declared mover, with the aperture reading in its commit).

**Who marches where** (MB-08's half, R-20). `march` forms on Rungs a person's questions name. The
missing candidate is a settlement held by a faction the marcher's seat is hostile to. That is a question
source (`decision/questions.py`) and a pursuit cell, both CORE's and CHAR's. What MB supplies: the
referent class is already `Rung` and `sides_of` already refuses a bad kind, so no MB edit is needed.

### F. An NPC may weigh a field (step 5b; design-first)

`field_estimate(w, actor, via, target, order=None, believed=None)`: when `believed` is given (a mapping
the host builds from the actor's claims about the defenders' strength and walls), the input is built
from it instead of from the world. A person who knows nothing gets no estimate. This does not let an NPC
read the world's odds (the recorded rule, AQ-X1, stands for that); whether a belief-based estimate
satisfies it is CHAR's reconciliation, named in the audit's §16.

### G. Aftermath (step 6)

`_eff_march` on `Won`: each routed defender who is not removed is re-homed to the nearest rung his
faction holds (`world_q.governing_hold` up his own chain, else the faction's seat rung), by `_relocate`
under the gate's `muster` basis; if there is none he stays. On `Won`, each winner who holds a negative
row toward his own faction (`person_q.held_against`) loses one. Both are behind the existing
`field_casualty_model` roster's precedent: a fixture `field_aftermath` (`off` control, `withdraw`
shipped).

## Gate (execution artifacts)

1. `field_scene.play` at one seed under two policies (storm at once; besiege then storm) ends in
   different bands with different persons hurt; the same policy at two seeds differs.
2. `resolve_field` with `decide=None` and with a decider returning `None`: equal outcome and equal draw
   count at seeds 0 to 19. With a decider ordering `defend` at phase 1: the outcome differs at some seed.
3. A folded field's Event carries, for both sides, who broke first and in which phase.
4. `aperture 2 s`, s = 0 to 2, after the flips: `field.won + field.lost + field.drawn` above 0 at every
   seed; `army.recruited`, `army.formed`, `army.assigned`, `order.marshaled` out of the never-emitted list.
5. Two leaders naming different doctrines raise different armies from equal means.
6. After a folded `field.won` with a routed defender who holds another rung, `mustered(target, loser)`
   is empty; a faction that loses, loses, then wins starts its next field at morale 4.

## Falsifier

Any of: a policy that cannot change a scenario's ending; a decider that cannot change an outcome at any
of 100 seeds (then the levers are cosmetic at the ruled friction, the conflict named in the audit's
§11); a realm with presets on that still fights no field in two seasons at three seeds (then the missing
piece is the march candidate, and this proposal has not closed R-20).

## NERS

- **N.** From the player's direction: without a scenario and a choice there is no game here. From the
  world's: without armies and a reason to march there is no war for anyone to remember. From the
  architecture's: the decider is the combat module's shape reused, not a new one.
- **R.** Strategic thought (estimate, exit, siege or storm), customisation (the army, the doctrine),
  the no-player half (commanders who raise and march), completeness (a draw has somewhere to go).
- **S.** One call at two fidelities; pauses at the engine's own phase boundaries and between rounds;
  the approach roster is the strategy roster, one vocabulary.
- **E, last.** A handful of small records and one harness file against a subsystem that today
  contributes no Event to a season. Legibility is the point: an estimate before, a report after.

## Cost class

A: small build. B, D: small build. C: none. E: small build plus two declared flips and a data edit
outside the lane. F: design-first. G: edit.

## Conflicts with ruled items, named and not resolved

Friction at sigma 1.1 (`ED-MB-0016`): the falsifier above is where it would show. `ED-IN-0301` (a field
is fought the round it is declared): unchanged; the decider acts inside that call.
