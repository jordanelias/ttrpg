# PC — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Subject: personal combat. `modules/combat/` (the engine), `systems/combat/` (the oracle-side data
and workbench), `engine/season/seam/wrappers/combat.py` (the host adapter), `engine/season/seam/ladder.py`
(the band read), `engine/season/loop/effects_combat.py` (the fold's writes), the typed export
`engine/engine_params/combat_engine_v1.json`, positions B10-11 / PC-nn / CP-T03-nn, and the
player-agency, tradition-curriculum and sparring proposals. Every figure below is a reading taken at
this SHA with `PYTHONHASHSEED=0`; §12 lists each command.

## 0. Verdict

DRAFT — replaced at the end of the read (the head is written first, CLAUDE.md §10 pt 2).

## 1. What it is, as coded

### 1.1 The path a fight takes (opened at each call site)

1. A person's act with verb `fight`, `accept` or `capture` declares `contests: the body`
   (`engine/season/verb_table.yaml`). The fold reaches the provider registered as
   `@provider("contest", "personal_combat")`: `engine/season/seam/wrappers/combat.py:324` (`resolve`).
2. `resolve` builds one frozen `PersonalCombatInput` (`combat_input`, `combat.py:197-232`): the two
   claimants, each one's `end` (`party_end`, `:143-152`: authored Endurance or 4, less one per body
   band, floored at 1), the wound quantities to lift, each kit (`world_q.kit_of`), each `faculty`
   (`pool.py::faculty`), the duel `terms` and the authored attributes.
3. It seeds `random.Random(int(H(world_seed, tick, a_id, "contest:<prize>:<cause>"), 16))`
   (`combat.py:388`) and calls the module entry it found by composition row (`entry_for`, `:389`), never
   by import.
4. `modules/combat/fight.py:55-117` builds two fresh `Combatant`s, sets `wrapper._TRACE` for the call,
   runs `wrapper.fight(A, B, rng, terms, decide)` and returns `{status, result, trace, ends,
   wound_state}`. It reads no `World`.
5. `wrapper.fight` (`modules/combat/wrapper.py:555-625`) runs up to `max_bouts=12` engagements; each
   `engagement` (`:76-481`) is an approach phase (stop-hits, arrest) and a tempo-gated closed exchange
   (commit depth, read contest, defence mode, one `core.resolve` roll per exchange, damage through
   `core.strike`, bind loop, contact axis). Every wound goes through one site, `_wound` (`:24-34`).
6. Back in the host: `seam/ladder.py::party_degree` (`:121-171`) reads each party's band off his lifted
   tracker (`Felled` / `Wounded` / `Untouched`); the act's band is the worst over both
   (`combat_degree`, `:174-195`).
7. `loop/effects_combat.py::_eff_kill` (`:61-254`) writes each party by his own band: `Felled` -> body 0
   and `World.remove_person` (which closes his tenures; each emptied seat is named, `death_subjects`);
   `Wounded` -> `body x health_remaining // health_full`, floored at 1 (`_harm`, `:427-447`), a lasting
   ceiling mark at the deepest gate (`_marks`, `:394-424`) and one point of `arms` capability if he
   already holds the key (`_grown`, `:271-296`). `_eff_capture` (`:333-381`) adds one `detain` edge
   when the subject yielded.

