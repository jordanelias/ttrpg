# PC round — part 2: the sweep and the clock table, what the mass-battle abstraction should assume, the coding items

## Status: PROPOSAL (continues `PC_ROUND_SPEC.md`; reference, resolves nothing at runtime, CLAUDE.md §0.05)

## 4. The consistency sweep (2026-11-12)

### 4.1 What was searched, and the decisions it applied

Searched (grep over `proposals/`, `master/`, `unified/` of the suite, `.md`): "round(s)", "turn(s)", "bout(s)",
"beat(s)", "engagement(s)", "exchange", durations ("ten seconds", "~10s", "N seconds"), `turn_start`, `max_bouts`,
"twelve turns". Three conflicts were found and decided:

1. **The duel's "turn" is a round.** A-9 owns "turn" (a scene's short sequence); the PC files used "turn" for the
   fight's iterations because the code does (`turn_start`, `decide(turn)`). Decided by A-101 (ladder 1): every duel
   "turn" reads **round**; proposed identifiers that carried `turn`/`turns` are renamed in the proposals
   (`CombatOutcome.rounds`, `Surrender.round`, `DecisiveBeat.round`, `SceneShape.rounds`, the Observation term
   `fight_rounds`, the riposte's key `"upset:<round>"` and event `finalblow_riposte(round, by)`); tree identifiers
   are the rename candidate PCR-3.
2. **"About ten seconds" for a round.** Corrected to A-101's indicator (4 to 10 seconds, of the exchange cap, never
   a clock) where stated: PA §1, `unified/work/R1_READ.md:326`; the code's own `wrapper.py:576` is PCR-1's edit.
3. **The season's "round" collides with A-101's.** The word test (STAGES.md): both senses pass ordinary English
   (a boxing round; a round of turns in a board game), so a fresh reader cannot tell which is meant where both
   appear, and test (a) fails. Jordan's word (A-101) keeps "round"; the season's within-season pass of
   DELIBERATE, RESOLVE and WITNESS (`Claim.round`, `SeasonDriver.round`, `scene_budget`) is called a **lap** in
   prose (ordinary: one circuit of a course; unused in the suite and the tree, checked by grep; "cycle" refused,
   it names dependency cycles throughout the suite; "pass" refused, it names review passes and a fencing step).
   The tree identifiers are the rename candidate PCR-4. Files with a dense season sense got a `Reconciled:` note;
   the rest change at their next edit (STAGES.md rule 3), listed in the glossary's *lap* row.

"Beat", "exchange" and "engagement" were found used consistently with §2.1 in the PC files (a beat is a loop step;
an exchange one attack with its defence; "engagement" the code's name for the round); `03_PC_typed_outcome_one_door.md`'s
`DecisiveBeat` (the beat in which the felling wound landed) keeps its name. MB uses of "bout", "field tick" and
"window" agree with the clock table. "Engagement" in MB prose is already refused by the MB lexicon.

### 4.2 Files edited (29), each with a `Reconciled:` line or a marked in-row correction, 2026-11-12, A-101

| file | change |
|---|---|
| `unified/U1_GLOSSARY.md` | §D *round* row → *lap*; §E *exchange*, *bout* rows and the riposte's ids; new §K (fight, round, duel round, closing, attack attempt, separation, beat, turn) and the clock table |
| `unified/U1_OWNERS_AND_VOCABULARY.md` | the *round / turn / tick* row marked superseded, old text kept |
| `unified/MB_LEXICON_part2.md` | *bout* row's refused senses; *duel round* row (same round; no tick advance) |
| `unified/MB_LEXICON_part3.md` | D-7's reason column |
| `unified/U3_DEPENDENCY_ORDER.md` | §1 items 15 (PCR-1 first in B15) and 16 (PCR-2, PCR-3 in B16); a `Reconciled:` line |
| `unified/work/R1_READ.md` | the *round* row's "about ten seconds" corrected in place |
| `master/instructions/IS_B1_PC_MB_DICE.md` | a `Reconciled:` line (turn → round, `fight_round`, the three items) |
| `proposals/03_PC_duel_round_and_approach.md` | §1's "about ten seconds"; `Reconciled:` note |
| `proposals/03_PC_duel_round_and_approach_B.md` | `Reconciled:` note: PCR-1/2/3 amendments to step 1 and the key |
| `proposals/03_PC_typed_outcome_one_door.md` | Part A fields `round`/`rounds`; seam keys; note |
| `proposals/16_PESSIMIST_PC_C_what_the_world_keeps_of_a_fight.md` | `SceneShape.rounds`, `fight_rounds` (six sites); note |
| `proposals/18_DETERMINISM_no_certain_matchup.md` | key `"upset:<round>"`, event `finalblow_riposte(round, by)`; note |
| `proposals/03_PC_exits_withdrawal_recovery.md`, `03_PC_weapon_form_at_round_start.md`, `03_PC_loadout_and_carry.md`, `16_PESSIMIST_PC_A_…`, `16_PESSIMIST_PC_B_…`, `16_PESSIMIST_PC_D_…`, `29_DICE_one_opposed_rule_form_and_tuning.md`, `U5b_PC_rulings_in_the_fight.md`, `U5a_capability_home_and_two_inputs.md` | `Reconciled:` note: the duel's "turn" reads round (and file-specific: the withdrawal at a round's top; the form reset also at a re-opening; figures pre-PCR-1) |
| `proposals/27_MB_E_…`, `28_CORE_scene_access_A_…`, `_B_…`, `_C_…`, `16_PESSIMIST_CORE_no_stored_plan.md`, `_a_scene_runs_in_its_own_order.md`, `_the_nine_gate_and_a_knockout_reading.md`, `18_DETERMINISM_rival_acts_in_one_fold.md` | `Reconciled:` note: "round" here is the season's **lap** |

### 4.3 Not edited, and why

- **`unified/DECISIONS_ANSWERED.md`** (Jordan's record): A-101's consequence column lists *initiative* among the
  carried state and says the exchange's attack attempts "are what the engine's beats are"; §2.4 and §1 of the spec
  decide otherwise (initiative resets; a beat is a loop step that holds at most one attack). A-63/A-64's
  consequence text uses "round" for the season's lap. The record is the orchestrator's to amend; listed in the
  receipt and in `PCR_FOR_JORDAN.md` item 1.
- **`unified/DECISIONS_FOR_JORDAN.md`**, `master/eval/*`, `master/HOLISTIC_*`, closure and conflict ledgers: question
  and audit records, edited only by their owners; their season "round"s read as laps by the glossary.
- **About 60 files with one or two season-sense "round"s** (the count in §4.1's grep): changed at their next edit
  (STAGES.md rule 3); the glossary's *lap* row is the instruction.
- **`master/mb_abstraction/`**: not present when read; not edited by rule. §5 is its input.

## 5. What the mass-battle abstraction lane should assume (A-100; `master/mb_abstraction/`, not edited here)

`master/mb_abstraction/` did not exist when this lane read the tree (2026-11-12, `ls`), so nothing of it was read.
A-100 derives the weapon-on-weapon and weapon-on-armour damage ranges by simulating personal combat. What that lane
can take from this one:

1. **The sampling unit is the round, not the fight.** One `fight_round` call (§6 PCR-3) returns the two
   `DuelState`s after it (damage, stamina, concentration, poise, form), `ended_by`, `exchanges` and `attempts` per
   party. A per-round damage distribution is the difference of the `cumulative_damage` fields; per attack attempt it
   is that over `attempts`. A whole fight is a loop the abstraction need not run, except to read rounds-to-decision.
2. **Sample after B15 and after PCR-1, never before.** Every figure in `PC_ROUND_SPEC.md` §1.1 is the pre-A-31
   engine: the damage scale (A-31), the commit window, the armour draw and the yield draw (B15) and the round boundary
   (PCR-1) all move per-round damage. An exporter whose `--check` round-trip is pinned before B15 closes pins numbers
   B15 will move.
3. **No seconds.** A round is 1 to 4 exchanges at closed measure (the cap, `BURST_MAX = 4`) plus the closing's
   stop-hits; its 4 to 10 seconds is an indicator (A-101), about one to two field ticks of about four seconds
   (`unified/MB_LEXICON_part2.md:15`). An exporter must not carry a seconds-per-exchange figure as data; if the
   field needs exchanges per tick it derives them from the round's own counts at a stated estimate, marked as one.
4. **Fatigue is per act and per separation.** Stamina is spent per attack act (`combat_systems.act_cost`) and by
   percussion taken, and recovered at each separation (`wrapper.py:614`). A unit's fatigue derived from personal
   combat should read stamina spent per round or per attempt, not per second (the one stamina ledger,
   `proposals/16_PESSIMIST_MB_one_stamina_ledger.md`, is the MB owner).
5. **Reach acts in the closing.** The longer weapon's advantage is in the round's closing (stop-hits, the arrest,
   `wrapper.py:221-262`) and in the re-presentation gate at entry; in matched-reach pairs the closing is instant.
   Army-scale range (missiles by distance) is A-100's separate layer 1 and has no personal-combat source.
6. **No mounts.** The duel engine has no horse and no charge by a mounted man, so pike against cavalry and bow
   against cavalry (A-100's layer 2) cannot be derived from it; the arrest impulse of a braced point
   (`systems.arrest_impulse`) is the nearest primitive and is a person's.
7. **The upset riposte** (`18_DETERMINISM_no_certain_matchup.md`) acts at a fight's deciding felling, so it moves
   fight endings, not the per-round damage distribution, except in the round that would have felled.
8. **A duel round inside a battle** is depth 1 and calls nothing (A-72); the field calls at most one round per pair
   per window and does not advance its tick count for it (`PC_ROUND_SPEC.md` §2.6).

## 6. Coding items (v12 batch form, `master/INSTRUCTION_SUITE_ORDER.md`)

Each item: Item · advanced · INSTRUCTION · WHERE · FALSIFIER and control · GATE · hash movers · depends on · lane ·
batch · cost and tier · what lands it. Layer 1 conformance (Lens B, `skills/layer-conformance/SKILL.md`) is stated
once at the end and holds for every item.

### Item: PCR-1 — a round ends at every separation, and says how it ended

- **Advances:** A-101 (the round as a boundary); R-04's combat scale row (`engine/season/requirements.yaml`) only in
  the sense that the duel round becomes observable; B15's calibration is then taken on A-101's rounds.
- **INSTRUCTION** (ordered):
  1. Write the instrument first: `systems/combat/combat_engine_v1/workbench/round_probe.py` (beside
     `build_levers.py`), the scratchpad `probe.py`/`probe3.py` of `PC_ROUND_SPEC.md` §1.1 as a workbench script:
     for named pairs and a seed range it prints rounds per fight, exchanges per round (mean and distribution),
     attack attempts per round, loop beats per round, the share of rounds in which both fought, the share
     re-opened inside the round, and the round endings by reason. Run it on the tree before step 2 and keep the
     printed table in the commit body (the baseline).
  2. `modules/combat/vocabulary.py`: add `ROUND_ENDS = ('clean_defence', 'burst_ceiling', 'collapse', 'disengage',
     'reopen', 'terms', 'felled', 'beat_exhaustion')`, a closed set, with a one-sentence definition (a round's ending:
     how the fighters came apart, or that one fell).
  3. `modules/combat/wrapper.py::engagement`: at the created-moment reopen (`:189-191`) replace `continue` by
     `_emit('separation', reason='reopen'); return None, False, 'reopen'`; at the clean fighting withdrawal
     (`:208-210`, after its `disengage` emit) replace `continue` by `_emit('separation', reason='disengage');
     return None, False, 'disengage'`. Every other `return` gains its reason as the third element (`'felled'` at
     each felling return, the emitted reason at each separation). The docstring says "one round (A-101): the two
     close, exchange attempts to attack, and separate", and the comment at `:471-477` drops "TURN" for "ROUND".
  4. `wrapper.fight`: unpack `loser, prev_closed, ended_by = engagement(...)`; emit `ended_by` on the
     `engagement_end` event; the comment at `:576` loses "~10s turn" and says "ONE round".
  5. `modules/combat/config.py:112`: the `BURST_MAX` comment reads "the per-round exchange cap (A-101: the 4-10 s
     band is an indicator of this cap, not a clock)". No value changes.
- **WHERE:** `modules/combat/wrapper.py`, `modules/combat/vocabulary.py`, `modules/combat/config.py` (comment),
  `systems/combat/combat_engine_v1/workbench/round_probe.py` (new); the test below.
- **Tests:** `tests/valoria/test_combat_round_boundary.py` (new): `test_no_round_closes_twice` — over 200 seeds of
  staff/none against dagger/none and poleaxe/heavy against longsword/heavy, between an `engagement_start` and the
  round's `engagement_end` no `approach` event follows a beat at closed measure (the falsifier, below), and
  `assert checked >= 200` (CLAUDE.md §0.1 pt 2); `test_separation_reasons_are_closed` — every `separation`
  reason and every returned `ended_by` is in `ROUND_ENDS`; `test_equal_reach_is_untouched` — the arming mirror at
  seeds 0–199 gives the same results and the same trace as the pre-change engine, pinned as a count of results and
  events (the control: with equal reach neither re-opening branch draws, `wrapper.py:188`, `:206` short-circuit on
  `base_gap > CLOSE_GAP_REF`).
- **FALSIFIER:** an `approach` event after a closed beat inside one round. **Control:** the equal-reach mirror,
  byte-identical (above), and `round_probe.py` before and after: re-opened-inside-the-round falls from 4.3–5.0% to
  0% in the reach-mismatched pairs and the `reopen`/`disengage` endings appear in about the same share.
- **GATE:** `python -m pytest tests/valoria/test_combat_round_boundary.py -q` green; `round_probe.py`'s after-table
  in the commit body with the expected reading above; `python tools/export_engine_params.py --check` green
  (`ROUND_ENDS` is not a `CFG` key, so the export does not move; a moved export is a defect).
- **Hash movers (declared):** every seeded result of a fight between two persons whose reaches differ beyond the
  latch band (combat goldens in `tests/valoria/test_combat_audit_pins.py` and siblings, the workbench balance tables,
  the season pins where such fights occur). Co-batched with B15's one re-record of the combat goldens, so it is
  re-pinned once.
- **Depends on:** nothing PROPOSED; the tree as it stands (EXISTS-IN-TREE: `engagement`, its one caller
  `wrapper.fight:595`, verified by grep).
- **Lane:** PC. **Batch:** B15-pc-calibration, **first item, before UPR §4's damage scale** (new edge: the scale and
  every B15 reading are taken on A-101's rounds; `unified/U3_DEPENDENCY_ORDER.md` B15 line, edited in this lane).
- **Cost and tier:** small build; `sonnet` writes it; the probe run is `haiku` (`valoria-measure`); the before/after
  table read by the B15 `opus` reader.
- **Lands it:** the PC implementation session under `/methodology-execute Batch B15-pc-calibration`.

### Item: PCR-2 — the round's outcome carries its ending (amends PB step 1)

- **Advances:** A-101 (what a round returns), A-3's discipline (an ending, not a winner), A-4/A-72 (the round a
  battle calls).
- **INSTRUCTION:** build PB step 1 (`03_PC_duel_round_and_approach_B.md` §2, §7) with four amendments:
  (1) the entry is `modules/combat/fight.py::fight_round(inp: DuelRoundInput, rng, deciders=None) ->
  DuelRoundOutcome` (not `round`, which would shadow the builtin; the composition role stays `combat.round`, target
  `modules.combat.fight:fight_round` in `references/module_contracts.yaml` `composition_roles:`);
  (2) `engine/season/queries/inputs.py::DuelRoundOutcome` gains `ended_by: str` (a member of `ROUND_ENDS`),
  `exchanges: int`, `attempts: Mapping[str, int]` (attack attempts per claimant: the `roll`, `stophit` and pursued
  `disengage` events by striker), read from what `engagement` returns and the round's own trace;
  (3) the between-round recovery (`wrapper.py:613-615`) is applied inside `fight_round` only when `ended_by` is a
  separation (not `felled`, not `terms`);
  (4) `fight` is the loop over `fight_round` up to `max_rounds` (12).
- **WHERE:** `modules/combat/fight.py`, `engine/season/queries/inputs.py`, `references/module_contracts.yaml`, the
  PB step-1 tests.
- **Tests:** PB's `test_twelve_round_calls_equal_one_fight` and `test_round_keeps_no_state_between_calls`
  (`engine/season/tests/test_rem31_grid_suspension.py`, `test_combat_module.py`), plus
  `engine/season/tests/test_combat_module.py::test_round_outcome_names_how_it_ended` — over 100 seeds the outcome's
  `ended_by` equals the trace's last `separation` reason or `felled`, `exchanges` equals the round's `outcome`
  count, and `sum(attempts.values())` equals its `roll` + `stophit` + pursued `disengage` count; `assert checked >=
  100`.
- **FALSIFIER:** a round outcome whose `ended_by` disagrees with its trace; a recovery applied after a felling; a
  `winner` field on the round. **Control:** twelve `fight_round` calls by hand equal `fight` at three seeds (PB).
- **GATE:** the named tests green; season hash EQUAL (PB step 1 is hash-EQUAL; the three added fields are read by
  nothing in a season).
- **Hash movers:** none.
- **Depends on:** PCR-1 (the three-element return) (PROPOSED); `11_GO_one_draw_owner.md` (B06) for step 2 only.
- **Lane:** PC. **Batch:** B16-pc-round, with PB step 1. **Cost and tier:** small build, `sonnet`. **Lands it:** the
  PC session under `/methodology-execute Batch B16-pc-round`.

### Item: PCR-3 — one word in code for the round (rename candidate, hash-EQUAL expected)

- **Advances:** STAGES.md's word test and rule 2 (the glossary matches the code); A-101.
- **INSTRUCTION:** in one commit, with the glossary row (`unified/U1_GLOSSARY.md` §K) replaced by a pointer to the
  code owner: `wrapper.fight(max_bouts=12)` → `max_rounds`; trace kinds `turn_start` → `round_start`,
  `engagement_end` → `round_end`, and every event field `turn=` → `round=` (`yield`, `withdraw`, `turn_start`,
  `engagement_end`); `Yield.turn` → `Yield.round`; `TURN_CHOICES` → `ROUND_CHOICES`; `CombatTurnView` (and its
  `.turn`) → `CombatRoundView` (`.round`); `modules/combat/fight.py`'s docstrings ("one bout scene" → "one fight");
  `seam/wrappers/combat.py`'s `bouts` → `rounds` (or, if B14 has deleted `bouts`, `CombatOutcome.rounds` as
  `03_PC_typed_outcome_one_door.md` now reads); `config.py`'s "per-TURN burst ceiling". `wrapper.engagement` keeps its
  name (a function called `round` would shadow the builtin the file calls at every emit).
- **WHERE (measured by `grep -rln "turn_start\|engagement_end\|CombatTurnView\|max_bouts"`, 14 files):**
  `modules/combat/wrapper.py`, `fight.py`, `config.py`; `engine/season/queries/inputs.py`;
  `engine/season/seam/wrappers/combat.py`; `systems/combat/combat_engine_v1/workbench/trace.py`, `commentary.py`,
  `narrate.py`; `systems/combat/combat_engine_v1/state_graph.py`; `engine/season/tests/test_rem31_grid_suspension.py`,
  `test_pc10b_challenge_record.py`; `tests/valoria/test_combat_duel_terms.py`, `test_combat_yield.py`;
  `tools/build_identifier_census.py`.
- **FALSIFIER:** a remaining `turn_start` or `max_bouts` in the combat files (`git grep`); a season hash that moves.
  **Control:** the combat goldens and the season pins unchanged.
- **GATE:** the four named test files and the workbench narrator's own run green; season golden pins EQUAL
  `[ASSUMPTION: trace event names and the round count do not enter World.content_hash(); the pins are the check]`.
- **Hash movers:** none expected; if the season pin moves, the assumption was wrong and the item stops.
- **Depends on:** PCR-2 (same files, same batch). **Lane:** PC. **Batch:** B16-pc-round, after PCR-2.
  **Cost and tier:** small mechanical rename, `haiku` for the edits with a `sonnet` check. **Lands it:** as PCR-2.

### Item: PCR-4 — the season's "round" becomes "lap" (tree-name candidate, cost to measure)

- **Advances:** the word test (one meaning for "round": A-101's, Jordan's own word).
- **INSTRUCTION (candidate, not decided to build):** rename the season's within-season pass — `state/carriers.py::
  Claim.round`, `SeasonDriver.round`, the fixture `scenes_per_round`, the `(tick, round)` keys
  (`questions_for(since=…)`, `_deliberated_at`), `loop/resolve.py::rival_key`'s `("round", person)` — to `lap`.
  Prose already says **lap** (glossary §K).
- **WHERE:** to measure: `git grep -n "\.round\b\|scenes_per_round\|\"round\"" engine/season` (41 non-test `.round`
  reads counted here by `grep -rn "\.round\b" engine/season --include=*.py | grep -v tests`), the fixtures file and
  the tests.
- **FALSIFIER / control:** season pins EQUAL if field names do not enter `World.content_hash()`; if `Claim`'s field
  name enters the hash, every pin moves once (declared).
- **Depends on:** nothing. **Lane:** IN. **Batch:** the v12 rename batch beside A-98's `capability` rename candidate
  (`U1_GLOSSARY.md` §H), or cut if its cost exceeds its reach. **Cost and tier:** to measure first (`haiku`
  count), then `sonnet`. **Lands it:** the IN session, only if v12 schedules it.

### What is NOT an item (decided, nothing to build)

- **The exchange cap's value** stays `BURST_MAX = 4` (`PC_ROUND_SPEC.md` §2.2); B15's calibration may move it only
  inside 3 to 5 with the reason stated against A-101's indicator, never to make a round a duration.
- **The fight's budget** stays twelve rounds; B15 reads the undecided share there.
- **No seconds clock, no per-second fatigue, no stored round duration** (§2.6).
- **No new disengagement trigger** (poise, a landed hit): §2.2's table. A calibration lane may test a poise-break
  separation as an arm against the control; it is not ordered.
- **PB step 5** (the `duel` callable in a field) needs nothing new beyond reading `ended_by`, `exchanges`,
  `attempts`; it stays in B30.

### Layer 1 conformance (Lens B), for every item above

- **The module row** (`04` §A.2; CLAUDE.md §3's restatement of `holonic_ARCHITECTURE.md` §43, §45: a registered
  module takes typed input, returns typed outcome, holds no token, keeps no game state). `fight_round` takes
  `DuelRoundInput`, returns `DuelRoundOutcome` (frozen dataclasses), keeps nothing between calls (PB's
  `test_round_keeps_no_state_between_calls`); the round's carried state is the caller's (A-4). Grade: STRUCTURAL
  (typed), checked by the named test. *Not read here:* the `holonic_ARCHITECTURE.md` sections themselves (cited
  through CLAUDE.md §3).
- **Row 22, as amended (A-4):** no token crosses the seam; a person-supplied callable (the deciders, the `duel`
  callable) crosses as an input and carries no token. PCR-1 to PCR-3 add no callable. Conformant.
- **Row 19, as amended (A-72):** the nesting cap is the fixture `contest_nesting_cap` (1). A round calls nothing:
  `engagement` and `fight_round` reach no role. Conformant; PB step 5 counts the field's call against the cap.
- **Row 52 (A-96), the one engine-formed act:** a round forms no act. A felling, a yield or a separation is read by
  the host from the outcome (`loop/effects_combat.py`), and only the guard's `capture` on a Failure of the access
  draw is formed by the engine (`04:177`, `:654`). No item here forms an act. Conformant.
- **§27.2 / §C.4, one resolver:** the round in a duel, a skirmish and a battle is the same `engagement`; the
  exchange cap and the endings are read from `CFG` and `ROUND_ENDS`, the one owner each. No second formula.
