# Workplan v12 — part 10, continued: batch B14-pc-outcome

## Status: PROPOSED (the continuation of author lane A10's part, written to a second file at an item boundary, `V12_STRUCTURE_part2.md` §4.1; its head, words, paths and the realm hash reading are the first file's; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

---

## Batch B14-pc-outcome · lane PC · wave W8 · step S8 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B14-pc-outcome
IN-FLIGHT ROW: registers/handoffs/HANDOFF_PC.md, Open table
GATE: Batch B00-ids @c3418a6a160fc6a17e5a8bf45112a0e55699a695
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B13-pc-package
GATE: Batch B05-one-roll
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: none — the batch makes the typed outcome B15, B16, B19a and B19 read (`V12_STRUCTURE.md` §2.2, "none of its own"); IS-B1 §1.1 row 6: after it "the workbench and the loop run one entry; the victor is recorded; an `undecided` fight still writes". The close quotes R-04.c5 (i)'s `aperture 2 s` reading at s = 0, 1, 2 (`combat.fight` in `ENGINES`; `accept` attempted, executed and refused on `exists:challenge`) as a re-read, not a status move (A-114)
BATCH GATE (read once, on the closing tree, at B14.99; `PYTHONHASHSEED=0` on every seeded command):
  `python tools/export_engine_params.py --check` → exit 0 on schema 8 (B14.12) with the `CFG` moves of B14.08 and B14.18;
  `python -m pytest engine/season/tests/test_combat_module.py tests/valoria/test_combat_scene_shape.py tests/valoria/test_engine_params_bridge.py tests/valoria/test_combat_invariants.py engine/season/tests/test_vm_phy_a_custody.py -q` → all pass;
  `python systems/combat/combat_engine_v1/workbench/export_parity_probe.py` → `50 weapons; max |derived − recomputed| <= 1e-9`, exit 0 (B14.12);
  `python systems/combat/combat_engine_v1/workbench/round_state_probe.py` → 0 fighter-starts in a half-sword form (B14.13);
  `python systems/combat/combat_engine_v1/state_graph.py` → PASS (B14.21);
  the realm hash reading at seeds 0, 1, 2 → moved, each mover named alone in B14.99's commit body with the before-reading (`reading @<sha>` of B05's close, or B06's after-reading if B06 merged first in S8, `V12_STRUCTURE_part3.md` §7.4): `prevailed` (B14.02), `fell_to` (B14.03), the scene's shape (B14.15), the hand (B14.16), the believed price of a fight (B14.24) (`accept`'s formation, once B14.27's, landed in B01 and moves nothing here); with each reverted alone, the hash before it returns (`03_PC_typed_outcome_one_door` gate 2);
  `python -m engine.season.harness.aperture 2 --seeds 0 1 2` → `ENGINES` `combat.fight` and `accept`'s attempted, executed and refused-on-`exists:challenge` (0) quoted before (`reading @<sha>`) and after (`14_VERBS_PHYSICAL_A` gate; `IS-PC-03`'s reading is B15's and B16's, not this batch's) `[ASSUMPTION: `aperture` takes `<seasons> --seeds …` — basis: IS-A §3's "`aperture 2 --seeds 0 1 2`" (`V12_STRUCTURE.md` §3); its flags were not opened by this lane]`;
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`) (H-98, H-123, H-64, H-264, H-349, H-97, H-258 edited; the two new fixture rows); `--requirements` → nine lines, unchanged in verdict; `python tools/m1_acceptance.py --summary` → verdict line quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch touches `modules/combat`, the seam, the loop, tools and registers: the full gates), once, at B14.99;
  the glossary rows each item names, read against the code it landed;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; no conjunct is named, so no `reading:` record is written; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B14.99: the realm pins (`engine/season/tests/_realm_goldens.py`), the corpus pins, `test_go07_canonical_digest.py`'s pins, and the combat goldens under `engine/tests/` and `tests/valoria/r3_identity_golden.json` that any item moved; the workbench armour reference `systems/combat/combat_engine_v1/workbench/data/combat_armour_reference.json` is re-recorded by its own item (B14.13, "`--update` once", the file's own rule) and the export by its exporter (B14.08, B14.12, B14.18), never by hand. Read against B06's after-reading (`reading @<sha>`): B06 merges first of S8's two movers and B14 rebases on it (part 2 §3; `V12_STRUCTURE_part3.md` §7.4; lane H3). The commit says "re-pin: `prevailed`, `fell_to`, the scene's shape, the hand, the believed fight price, `accept` formed on a heard challenge; each declared".
EXPECTED RED UNTIL B14.99 (under `[skip ci]`, E-1; one batch line, repair lane R1): the realm and corpus pins any mover item of this batch moves read red from its first mover (B14.02) to the re-pin; the files that pin them (`git grep -lE '"[0-9a-f]{32}"'` over the test trees and the golden files, those this batch names): `engine/season/tests/_realm_goldens.py` (B02's one pin file); `engine/season/tests/test_go07_canonical_digest.py` (its asserting test, `SHIPPED`/`CENSUS`); `tests/valoria/r3_identity_golden.json`; `tests/valoria/test_combat_audit_pins.py`; `tools/ci_golden_modes_check.py`.
IDS: ED-PC 0; H 2 (the register rows of the fixtures `mark_ob`, B14.23, and `believed_fight_samples`, B14.24 `[ASSUMPTION: each new `Fixtures` key needs its own register row, `04` §B.13 #11 as H-98's text cites it — basis: `hole_register.yaml` H-98 names that rule]`)
DIALS AT CONTROL: `body_mark_model` = `deepest_gate` (shipped, the arm the tree runs today; `none` is the control); flipped to `drawn` by B15 (`U5b_PC_residue` §7: "the flip is read with the calibration batch, after A3 (B15)"); target: "200 seeded fights that leave a survivor at his limit: the three outcomes each occur". `mark_ob` = `[ASSUMPTION]` seed value, read only under `drawn`; set by B15 with that flip; target as above. `CFG['READ_SCALE']` = 1.0 (byte-identical); set by B15 (`U5b_PC_residue` §1: "the fit rides the calibration batch"); target: "Perception 5 against 3" does not "exceed four points of score".
UNDECIDED: (1) U3 §1 item 14 names `U5b_PC_residue` §7–§8; the proposal's own Lands line ("§2, §4–§10 in B14 (U3 places §7–§8 there); §1 items 1–2 in B14"), U3 §3.1 (the node whole in B14) and §1.2's B14 row agree on the wider set, so §1 items 1–2, §2, §4–§10 are items here; §3 is B18's, §1 items 3–5 B15's. (2) `14_VERBS_PHYSICAL_A` puts A0 (`addressed_records`) in B29 with A1–A2 and A4 in B14, but A4's stamp calls A0 and its own order is "A0, then A1 … Then A4": A0 lands here with A4 (B14.27), the only order with no back edge (ladder step 5); B29's author finds it landed. (3) `U5b_PC_residue` §4 edit 2 removes `wrapper.fight`'s `rng` default and fallback, which B06.05 also removes (`11_GO_one_draw_owner` row 3) in the same step S8: B14.20 removes `cfg`'s default and the self-fight; the `rng` half is B06.05's, and the signature line, one line in one function of a shared file, is kept once at merge (B06 first, `V12_STRUCTURE_part3.md` §7.3, §7.4). (4) CP-T03-06 sits under the intake's B14 heading but its entry reads "after B14 (`16_PESSIMIST_PC_C`) and B10 (`02_CHAR_scar_is_a_wound`)"; B10 closes at S11, after B14, so by E-8's exception it joins B15, the first PC batch whose `after` list holds both B10 and B14 (`V12_STRUCTURE.md` §2.1): B14.14 is its POINTER, and B15's author carries it. (5) `U5b_PC_residue` §7 says "pool his body band"; A-6, A-7 and A-8 (applied to the sibling mortal-wound draw in `14_VERBS_PHYSICAL_A`'s head) make every such roll the one pool rule on the untrained default with the body band entering as levels through the `wounds` source; B14.23 writes the ruled form and says so. (6) `U5b_PC_residue` §6 item 1 (a clause in the v11 PC-08 Phase-C row) is not carried: v11 is retired at adoption and PC-08 is a held entry (the intake `:510`), whose text keeps the clause's subject (`combat_systems.py`'s `KNOWN BROKEN-LOGIC` tempo note). (7) `U5b_PC_residue` §6 item 2 offers "renamed" or "left … and the shadow recorded"; its gate (`import trace` from the workbench directory prints the standard library's path) is met only by the rename, so B14.22 renames. (8) `03_PC_typed_outcome_one_door` Part C R-PC-03 is superseded in its own text by `18_DETERMINISM_no_certain_matchup` edit 2 (B15): no item.
C(B14-pc-outcome): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *prevailed*, *riposte*, *record*, *scene*, *round*;
  `modules/combat/fight.py` (`fight`, `_lift`); `modules/combat/wrapper.py` (`fight`, `engagement`'s open-measure reset, `_TRACE`); `modules/combat/combat_systems.py` (`halfsword_target`, the 18 constants); `modules/combat/core.py` (`resolve`); `modules/combat/config.py` (`CFG`, line 1); `modules/combat/contact.py` (`GRAB_OUTCOMES`); `modules/combat/weapon_physics.py` (line 3's citation); `modules/combat/weapons.py` (schema header); `engine/substrate/combat_kit.py`;
  `engine/season/queries/inputs.py` (`PersonalCombatInput`); `engine/season/seam/wrappers/combat.py` (`resolve`, `combat_input`, `fight_estimate`, `surrender_of`, `_wound_state`); `engine/season/seam/wrappers/sigma.py` (`believed_chance`); `engine/season/loop/effects_combat.py` (`_eff_kill`, `_eff_capture`, `fight_ending`, `_marks`, `broke_observed`); `engine/season/loop/witness.py` (WITNESS deposit of a fight's Event); `engine/season/queries/person_q.py` (`deed_doer`); `engine/season/queries/world_q.py` (`_stamped`, `CHALLENGE_KIND`, `detainees_held`); `engine/season/harness/chronicle.py` (`lines`); `engine/season/state/carriers.py` (`Event.observed`'s comment); `engine/season/data/fixtures.py`; `engine/season/data/verbs.py`; `engine/season/rosters.yaml` (`fight_endings`, `observation_terms`, `body_mark_models`); `engine/season/verb_table.yaml` (`accept`); `engine/season/hole_register.yaml`; `engine/season/requirements.yaml` (R-09 `blocks:`);
  `tools/export_engine_params.py`; `engine/engine_params/combat_engine_v1.json`; `systems/combat/combat_engine_v1/workbench/` (`server.py`, `trace.py` → `fight_trace.py`, `balance.py`, `probabilities.py`, `catalogue.py`, `armour_participation.py`, `build_levers.py`, `commentary.py`, `narrate.py`, `structure_scan.py`, `data/combat_armour_reference.json`); `systems/combat/combat_engine_v1/state_graph.py`; `proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md` (Status line); `registers/handoffs/HANDOFF_PC.md`;
  the tests named in the items; instruments: the realm hash reading, `aperture`, `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/export_engine_params.py`; the closing SHAs of B00, B01, B02, B13, B05; the permanent surface.
COST: small builds and edits, six declared movers; producer `valoria-author` on `sonnet`, `high`; the R-PC-17 golden judgment and the PC-21 design `opus`; A4's gate read by `opus` (`14_VERBS_PHYSICAL_A`, "one `opus` read of each gate"); PC review, GO review of the export.
EST: 14.1 h [estimate: `V12_STRUCTURE.md` §2.4's formula over this batch's 29 positions (0.4 h × 29 + 2.5 h), E-15; §2.2 gave 6 h by members]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B14.01 | the combat outcome is a dataclass; the seam returns only what is read | `03_PC_typed_outcome_one_door` Part A (record and `resolve`) | BUILD | EQUAL | Batch B13, Batch B05 |
| B14.02 | the fighter left standing `prevailed`; an undecided fight still writes | Part A (`prevailed`, A-81) | BUILD | MOVER(behaviour) | B14.01 |
| B14.03 | a felling records its source and weapon (`fell_to`) | Part A (`fell_to`) | BUILD | MOVER(behaviour) | B14.02 |
| B14.04 | H-98 closed; R-09's `blocks:` re-pointed | Part C R-PC-01 | BUILD | EQUAL | B14.03 |
| B14.05 | H-123's site, the PC handoff, dead `designs/audit/` citations | Part C R-PC-15 | BUILD | EQUAL | B14.03 |
| B14.06 | the CR-85 design's Status line | Part C R-PC-16 | BUILD | EQUAL | — |
| B14.07 | the exchange's net through the one boost call | Part C R-PC-17 | BUILD | MOVER(behaviour), declared if a golden moves | B14.03 |
| B14.08 | the 18 `combat_systems` constants into `CFG` | Part C R-PC-18 | BUILD | EQUAL | B14.03 |
| B14.09 | the state graph says it is reference | Part C R-PC-20 | BUILD | EQUAL | — |
| B14.10 | the workbench's degree distribution reads the dice owner | Part C R-PC-42 | BUILD | EQUAL | Batch B05 |
| B14.11 | one door: the workbench calls the entry the loop calls | Part B | BUILD | EQUAL | B14.01 to B14.10 |
| B14.12 | the export carries the weapons, the derived quantities and the module constants | `03_PC_weapon_records_in_the_export` | BUILD | EQUAL | B14.08, B14.11 |
| B14.13 | a round opens with the weapon as issued | `03_PC_weapon_form_at_round_start` | BUILD | EQUAL (season); the armour reference re-recorded | B14.12 |
| B14.14 | the survivor's grudge (moves to B15) | intake `:491` CP-T03-06 | POINTER | — | — |
| B14.15 | what the world keeps of a fight: the scene's shape | `16_PESSIMIST_PC_C` 1 | BUILD | MOVER(behaviour) | B14.03, B14.13 |
| B14.16 | the hand that killed is named | `16_PESSIMIST_PC_C` 2 | BUILD | MOVER(behaviour) | B14.15 |
| B14.17 | which term carries the read's slope | `U5b_PC_residue` §1 item 1 | READING | — | B14.11 |
| B14.18 | the read's literal scale becomes `CFG['READ_SCALE']` | `U5b_PC_residue` §1 item 2 | BUILD | EQUAL | B14.12 |
| B14.19 | the grapple's outcome names say what they do | `U5b_PC_residue` §2 | BUILD | EQUAL | — |
| B14.20 | a self-fight is refused; `wrapper.fight` takes its `cfg` | `U5b_PC_residue` §4 | BUILD | EQUAL | B14.11 |
| B14.21 | six stale texts | `U5b_PC_residue` §5 | BUILD | EQUAL | B14.09 |
| B14.22 | the workbench's `trace.py` stops shadowing the library | `U5b_PC_residue` §6 item 2 | BUILD | EQUAL | B14.11 |
| B14.23 | the lasting mark may be drawn (shipped at today's arm) | `U5b_PC_residue` §7 | BUILD | EQUAL | B14.03 |
| B14.24 | a fight is priced by believed odds | `U5b_PC_residue` §8 | BUILD | MOVER(behaviour) | B14.01, Batch B05 |
| B14.25 | five register rows brought to the tree | `U5b_PC_residue` §9 | BUILD | EQUAL | B14.23 |
| B14.26 | the conditional test loops assert they asserted | `IS-PC-04` (`U5b_PC_residue` §10) | BUILD | EQUAL | — |
| B14.27 | a challenge heard of is accepted (with the addressed-Record reader); the reader and stamp landed in B01, the gate test remains | `14_VERBS_PHYSICAL_A` A0, A4 | BUILD | EQUAL | B14.01, Batch B01 |
| B14.28 | the opponent model: the design | intake `:492` PC-21 | DESIGN-FIRST | — | — |
| B14.99 | re-pin and close readings | E-1 | BUILD | MOVER (the re-pin) | B14.01 to B14.28 |

Not in this batch, and where each is: `U5b_PC_residue` §1 items 3–5 (B15, the calibration batch), §3 (B18); `14_VERBS_PHYSICAL_A` A3 (B15), A1–A2 (B29); `03_PC_typed_outcome_one_door` R-PC-03 (superseded, UNDECIDED (8)); CP-T03-06 (B15, UNDECIDED (4)); `U5d_GO_owed_edits` §2 (b) is carried by B14.02 (the witness's deposit of a fight's `ending`).

### B14.01 — the combat outcome is a dataclass; the seam returns only what is read · `03_PC_typed_outcome_one_door` Part A (record and `resolve`) · BUILD · HASH EQUAL
- SOURCE: `proposals/03_PC_typed_outcome_one_door.md` "Part A", "Implementation" order (1) first commit ("the record and `resolve`'s return (hash EQUAL)"), "Falsifier"; `unified/U3_CONFLICT_LEDGER.md` C3-L5; rulings A-101 (round), D-U1-08; closes F-PC-06, F-PC-07, R-PC-02, R-PC-04, R-PC-05.
- ADVANCES: none of the nine; one shape at every module seam (B15 to B19a read it).
- INSTRUCTION:
  1. `engine/season/queries/inputs.py`, beside `PersonalCombatInput`:
     ```python
     @dataclass(frozen=True)
     class PartyWounds:            # one party's lifted tracker, in `rosters.yaml: wound_quantities` order
         felled: bool
         wounds: int
         max_wounds: int
         health_remaining: int
         health_full: int

     @dataclass(frozen=True)
     class Surrender:              # the scene's `yield` event, as `surrender_of` lifts it today
         by: str
         round: int                # the round at whose start or end the yield came (A-101; was `turn`)
         accepted: bool

     @dataclass(frozen=True)
     class DecisiveBeat:           # the wound that ended it, read off the trace's last felling `wound` event
         by: str                   # the striker's id
         victim: str
         source: str               # wrapper's own site names: exchange | bind | stophit | pursuit | displace_graze
         weapon: str               # the striker's weapon key at that beat
         round: int                # the round it landed in (A-101; was `turn`)

     @dataclass(frozen=True)
     class CombatOutcome:
         claimants: tuple                  # (A, B), as the input
         wounds: Mapping[str, PartyWounds] # keyed by claimant id; a party with no tracker is absent (the host refuses)
         surrender: Optional[Surrender]
         beat: Optional[DecisiveBeat]      # None when nobody was felled
         rounds: int                       # rounds fought (A-101; was `turns`, the `turn_start` count)
         trace: tuple                      # the scene's events, for a viewer; folded nowhere
     ```
  2. "`modules/combat/fight.py::fight` returns `CombatOutcome`. It builds `PartyWounds` from the fields the input names, as `_lift` does now; a field the tracker lacks still refuses in the host by name."
  3. "`seam/wrappers/combat.py::resolve` returns `dict(status="RESOLVED", module=…, resolver="d_sigma", wound_state=…, surrender=…, beat=…, rounds=…, trace=…)`. `winner`, `result`, `unresolved`, `bouts`, `parties` and `seed` are deleted (ladder rung 2: no reader). `fight_estimate` reads `wounds` and `surrender` off the record. The integer `wrapper.fight` returns is no longer lifted." The upset is not touched here (B15's `18_DETERMINISM_no_certain_matchup` makes it a riposte the trackers record).
  4. "This record is not a `Margin`, and must not be 'fixed' into one: combat's degree is read off its wound state" (the 2026-09-03 ruling); its docstring says so.
- WHERE: `engine/season/queries/inputs.py` (`PartyWounds`, `Surrender`, `DecisiveBeat`, `CombatOutcome`); `modules/combat/fight.py` (`fight`, `_lift`); `engine/season/seam/wrappers/combat.py` (`resolve`, `fight_estimate`); `engine/season/tests/test_combat_module.py`.
- TESTS: in `engine/season/tests/test_combat_module.py` (existing; "the oracle comparison re-pointed at the record's fields"), written first and read red: `test_resolve_returns_no_winner_key`.
- FALSIFIER and CONTROL: "any reader of a deleted key (the build fails at that reader)"; `git grep -nE "\[\"(winner|result|unresolved|bouts|parties|seed)\"\]|\.get\(\"(winner|bouts)\"" engine/season -- '*.py'` (tests excluded) prints no reader. Control: the realm hash reading at seed 0 equal to the batch's base (`reading @<sha>`) (the fold reads `wound_state` and `surrender` only).
- GATE: `python -m pytest engine/season/tests/test_combat_module.py -q` → pass; the realm hash reading (`HASH READING`) at seed 0 → equal to the base.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `queries/inputs.py::PersonalCombatInput`, `modules/combat/fight.py::fight`, `::_lift`, `seam/wrappers/combat.py::resolve`, `::fight_estimate`, `::surrender_of`; V12 Batch B13 (`modules/combat` a package, CI-09), Batch B05.
- GLOSSARY: none (*record*'s row already says "dataclass", U4d).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B14's `valoria-author` producer, `isolation: worktree`; `Item: B14.01`, `[skip ci]`.

### B14.02 — the fighter left standing `prevailed`; an undecided fight still writes · `03_PC_typed_outcome_one_door` Part A (`prevailed`, A-81) · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, Part A's `prevailed` and A-81 bullet, "Implementation" order (1) ("then `prevailed` and `fell_to` (the two declared movers, each alone)"); `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-11a; `U3_CONFLICT_LEDGER.md` C3-C11; `proposals/U5d_GO_owed_edits.md` §2 (b) ("WITNESS deposits the band Event's `ending` to a co-located witness, at PC's owner"); rulings A-81; closes H-348, IS-PC-P3.
- ADVANCES: none of the nine; IS-B1 §1.0's ending kinds (`prevailed` joins `fight_endings`).
- INSTRUCTION: "`rosters.yaml: fight_endings` gains `prevailed` (D-U1-11a). `loop/effects_combat.py::fight_ending` returns `prevailed` for a party who is neither felled nor the yielder when the other party is; `undecided` only when neither is." "*(A-81, C3-C11:)* an `undecided` fight still writes: its Event is witnessed and WITNESS deposits it to those present (`co_located` firsthand), and each party holds his own claim of the fight." Open `loop/witness.py`'s deposit of a fight's Event at the item's open and record in the commit body whether the `co_located` deposit and the parties' own claims already happen for an `undecided` Event; edit only what is missing.
- WHERE: `engine/season/rosters.yaml` (`fight_endings`); `engine/season/loop/effects_combat.py` (`fight_ending`); `engine/season/loop/witness.py` (only if the reading above finds the deposit missing); `engine/season/tests/test_combat_module.py`.
- TESTS: `test_the_party_left_standing_is_prevailed` (written first, red: `undecided` today). `[ASSUMPTION: test name; the item creates it]` `test_an_undecided_fight_is_witnessed_by_those_present` (E-3), red only if the reading finds the deposit missing.
- FALSIFIER and CONTROL: "a hand-built fight whose log names the felled party `prevailed`". Control: with `prevailed` reverted alone, the realm hash at seed 0 equals B14.01's reading (`03_PC_typed_outcome_one_door` gate 2: "each moved alone and named in the commit body").
- GATE: `python -m pytest engine/season/tests/test_combat_module.py -q -k "prevailed or undecided"` → pass; the realm hash reading (`HASH READING`) at seed 0 → moved from B14.01's, the move named.
- HASH MOVERS: "Declared hash mover for every log that carries the field" (`Event.ending`). B14's one re-pin in B14.99.
- DEPENDS ON: V12 B14.01; EXISTS-IN-TREE `loop/effects_combat.py::fight_ending`, `rosters.yaml: fight_endings`, `loop/witness.py`.
- GLOSSARY: row *prevailed* (add if absent): "prevailed: the ending of a fight for the party who was neither felled nor yielded while the other was, as one who prevails in a contest wins it"; owner `rosters.yaml: fight_endings`; rejected `standing` (D-U1-11a: it names three other things).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B14's producer; `Item: B14.02`, `[skip ci]`.

### B14.03 — a felling records its source and weapon (`fell_to`) · `03_PC_typed_outcome_one_door` Part A (`fell_to`) · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, Part A's `_eff_kill` bullet; D-U1-06; C3-L5; closes F-PC-08 (a).
- ADVANCES: none of the nine; R-01/R-07 contributors (a deed others can hold).
- INSTRUCTION: "`loop/effects_combat.py::_eff_kill`: a felled party's Subject carries `Observation(victim, "fell_to", f"{beat.source}:{beat.weapon}")` beside what it carries now, on `CP-T04-01`'s `broke_observed` precedent (an Event has no payload, so a cause rides `Event.observed`). `observed` is the one channel for a derived outcome WITNESS deposits; `fell_to` is added to the closed roster `rosters.yaml: observation_terms` in the same commit (a term outside it is refused), and `state/carriers.py::Event.observed`'s comment gains *"and the outcomes an effect derives from the scene it wrote (a felling's source, a body that broke first, a named draw), as Observations WITNESS deposits; never an actor, a target or a recipient (S19.3)"*. `fell_to` names a source and a weapon, never a doer. `[ASSUMPTION; medium; Jordan to correct; revert: drop the Observation and the roster member]`." The comment edit changes no field (D-04: not an encoding mover).
- WHERE: `engine/season/loop/effects_combat.py` (`_eff_kill`); `engine/season/rosters.yaml` (`observation_terms`); `engine/season/state/carriers.py` (`Event.observed`'s comment); `engine/season/tests/test_combat_module.py`.
- TESTS: `test_a_felling_deposits_fell_to_under_observation_terms` (written first, red).
- FALSIFIER and CONTROL: a felled party's Event with no `fell_to`; a `fell_to` value naming a person. Control: with `fell_to` reverted alone, the realm hash at seed 0 equals B14.02's reading.
- GATE: `python -m pytest engine/season/tests/test_combat_module.py -q -k fell_to` → pass; the realm hash reading (`HASH READING`) at seed 0 → moved from B14.02's, named.
- HASH MOVERS: "Declared hash mover for every log with a felling." B14.99.
- DEPENDS ON: V12 B14.01 (`DecisiveBeat`), B14.02; EXISTS-IN-TREE `loop/effects_combat.py::broke_observed`, `rosters.yaml: observation_terms`, `state/carriers.py::Event.observed`.
- GLOSSARY: none `[ASSUMPTION: `fell_to` is a roster member, not a term the glossary carries]`.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B14's producer; `Item: B14.03`, `[skip ci]`.

### B14.04 — H-98 closed; R-09's `blocks:` re-pointed · Part C R-PC-01 · BUILD · HASH EQUAL
- SOURCE: `03_PC_typed_outcome_one_door.md` Part C row R-PC-01; closes H-98.
- ADVANCES: none of the nine (R-09's record is made true to the tree).
- INSTRUCTION: "H-98: grade to closed, cite CP-T03-00 (each party is written by his own band, so a decisive win is the victor `Untouched` and a narrow one the victor `Wounded`). R-09 `blocks:` re-pointed from H-98 to the two things that block it for combat: reach and per-person inputs." The two are named by their v12 carriers: reach `03_PC_duel_chain_reach` (V12 Batch B01, landed) and per-person inputs `03_PC_person_inputs_content` (B18) `[ASSUMPTION: `blocks:` takes ids; the two are written as the hole or plan ids the register accepts, read from `register.py`'s `blocks` rule at the item's open — basis: R-09's `blocks: [H-98]` at `aa31fd2`]`.
- WHERE: `engine/season/hole_register.yaml` (H-98); `engine/season/requirements.yaml` (R-09 `blocks:`).
- TESTS: none new.
- FALSIFIER and CONTROL: `register --check` refuses the edited rows. Control: the realm hash at seed 0 equal to B14.03's (no code).
- GATE: `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `--requirements` → nine lines.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `hole_register.yaml` H-98, `requirements.yaml` R-09 `blocks: [H-98]`; V12 Batch B02 (`IS-A-01` keeps `blocks:`, removes only `measured:`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B14's producer; `Item: B14.04`, `[skip ci]`.

### B14.05 — H-123's site, the PC handoff, dead `designs/audit/` citations · Part C R-PC-15 · BUILD · HASH EQUAL
- SOURCE: `proposals/03_PC_typed_outcome_one_door.md` Part C row R-PC-15.
- ADVANCES: none (stale text; CLAUDE.md §1).
- INSTRUCTION: "H-123's site to `loop/effects_combat.py`; the handoff names its two documents by bare filename (CLAUDE.md §1); each dead citation rewritten to the bare filename or deleted where the file no longer exists" — the "sixteen `designs/audit/` citations in `modules/combat/*.py`" (`git grep -n "designs/audit/" modules/combat` at the item's open; each resolved through `tools/pathres.py`'s exact-row `load_alias_map()`, never `resolve()`, CLAUDE.md §8). B03a (CI-02) may already have rewritten them as comments: those it rewrote are skipped and listed.
- WHERE: `engine/season/hole_register.yaml` (H-123 `site:`); `registers/handoffs/HANDOFF_PC.md`; `modules/combat/*.py` (the comments the grep prints).
- TESTS: none.
- FALSIFIER and CONTROL: a remaining `designs/audit/` path in `modules/combat`. Control: AST equality of every edited `.py` (comment-only).
- GATE: `git grep -c "designs/audit/" modules/combat` → no output, exit 1 (with no hit `git grep -c` prints nothing; at the tree of 2026-11-13 it prints six `file:count` lines, 16 hits, exit 0: the control; repair lane R2a, K2 #13); `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE H-123; V12 Batch B03a (CI-02's comment rewrite of the same files).
- GLOSSARY: none.
- COST and TIER: edit; `haiku`-assisted, `sonnet` lands.
- LANDS IT: B14's producer; `Item: B14.05`, `[skip ci]`.

### B14.06 — the CR-85 design's Status line · Part C R-PC-16 · BUILD · HASH EQUAL
- SOURCE: `proposals/03_PC_typed_outcome_one_door.md` Part C row R-PC-16; ED-IN-0351.
- ADVANCES: none.
- INSTRUCTION: `proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md`, its `## Status:` line becomes: "PROPOSED; ratification withdrawn (ED-IN-0351). Its combat build is in the tree (`modules/combat/attributes.py`, `core.py`, `fight.py`) and stands on this unratified design". (A-112 has since answered the question that held its design, the intake `:504`; the line states the record and decides nothing.)
- WHERE: `proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md` (Status line).
- TESTS: none.
- FALSIFIER and CONTROL: `python tools/currency_consistency_check.py` refuses the line. Control: no code.
- GATE: `python tools/currency_consistency_check.py` → exit 0. Record line, not a gate arm (it reads a `## Status:` line, which observes the edit and no behaviour; CLAUDE.md §0.05; repair lane R2a, K2 #12): `grep -c '^## Status:' proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md` → 1, quoted in the commit body.
- HASH MOVERS: none. DEPENDS ON: EXISTS-IN-TREE the file. GLOSSARY: none.
- COST and TIER: edit; `haiku`.
- LANDS IT: B14's producer; `Item: B14.06`, `[skip ci]`.

### B14.07 — the exchange's net through the one boost call · Part C R-PC-17 · BUILD · HASH MOVER(behaviour), declared if a golden moves
- SOURCE: `proposals/03_PC_typed_outcome_one_door.md` Part C row R-PC-17; "Falsifier" (R-PC-17); "Implementation" ("the golden re-record judgment for R-PC-17 `opus`").
- ADVANCES: none; S (one substrate call for the boost).
- INSTRUCTION: `modules/combat/core.py::resolve`: "`net = roll_net(pool, rng) + SL.net_boost(net_sigma, pool)`. Measured equal to the inline form to one unit in the last place at four points; a golden that moves is re-recorded and said so." At `aa31fd2` the line reads `net = roll_net(pool, rng) + SL.soft_cap(net_sigma) * SL.sigma_n(pool)`; B05 (`U5a_DICE_owed_edits` §1, `10_DICE_one_roller_one_fraction_rule`) may have rewritten it: re-open it at the item's open, and if B05 already routes the boost through `net_boost`, the item is recorded as done by B05 in the commit body and skipped.
- WHERE: `modules/combat/core.py` (`resolve`).
- TESTS: `tests/valoria/test_combat_invariants.py` (existing, must pass).
- FALSIFIER and CONTROL: "the combat goldens under `engine/tests/` and `tests/valoria/r3_identity_golden.json`; a moved golden is the finding, re-recorded only with the move stated." Control: the realm hash at seed 0 equal to B14.03's (every person fights an arming sword in light armour; a last-place difference crosses no threshold `[ASSUMPTION — basis: the source's four-point measurement]`).
- GATE: `python -m pytest tests/valoria/test_combat_invariants.py -q -m combat` → pass; `python tools/ci_golden_modes_check.py` and the combat goldens → equal, or each moved golden listed for B14.99 with `opus`'s reading.
- HASH MOVERS: a combat golden that moves by one unit in the last place, if any. Declared; B14.99.
- DEPENDS ON: EXISTS-IN-TREE `modules/combat/core.py::resolve`, `engine/dice_engine/sigma_leverage.py::net_boost`; V12 Batch B05.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`; the golden judgment `opus`.
- LANDS IT: B14's producer; `Item: B14.07`, `[skip ci]`.

### B14.08 — the 18 `combat_systems` constants into `CFG` · Part C R-PC-18 · BUILD · HASH EQUAL
- SOURCE: `proposals/03_PC_typed_outcome_one_door.md` Part C row R-PC-18; gate 4 ("the count of `combat_systems.py` module-level numeric constants absent from the export is 0"); closes F-PC-10.
- ADVANCES: none; CLAUDE.md §5 (a value the port uses lives in the typed export).
- INSTRUCTION: "move `REAR_CLEARANCE_TEMPO_K`, `REAR_CLEARANCE_STR_K`, `RANGE_AVAIL_FLOOR`, `RANGE_COMMIT_PEAK`, `RANGE_COMMIT_FLOOR`, `LEGIB_SWING_ROOM_K`, `STOPHIT_RANGE_K`, `FACING_VOID_K`, `FACING_PROFILE_K`, `FACING_VOID_GAIN`, `MODE_PERC_MIN`, `CLOSE_EFF_GAP_REF`, `CLOSE_EFF_FLOOR`, `MODE_EDGE_MIN`, `MODE_TIP_MIN`, `SELECT_EPS`, `TRUE_TIME_REF`, `ARREST_POB_REF` into `CFG`, values unchanged, readers through `cfg[...]`; re-derive the export with `tools/export_engine_params.py --build`. Functions that take no `cfg` today (`close_efficacy`, `range_utilization`, `_commit_range_factor`) gain it."
- WHERE: `modules/combat/combat_systems.py` (the 18 constants, their readers, the three functions' signatures and callers); `modules/combat/config.py` (`CFG`); `engine/engine_params/combat_engine_v1.json` (re-derived).
- TESTS: `tests/valoria/test_combat_invariants.py`, `tests/valoria/test_engine_params_bridge.py` (existing).
- FALSIFIER and CONTROL: a constant left at module level in `combat_systems.py` and absent from the export. Control: the combat goldens and the realm hash at seed 0 equal to B14.07's (values unchanged).
- GATE: `python tools/export_engine_params.py --check` → exit 0; `python -m pytest tests/valoria/test_combat_invariants.py tests/valoria/test_engine_params_bridge.py -q` → pass; the realm hash (`HASH READING`) at seed 0 → equal.
- HASH MOVERS: none (the export file's content changes, re-derived by its tool).
- DEPENDS ON: EXISTS-IN-TREE the 18 names in `modules/combat/combat_systems.py`, `config.py::CFG`, `tools/export_engine_params.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B14's producer; `Item: B14.08`, `[skip ci]`.

### B14.09 — the state graph says it is reference · Part C R-PC-20 · BUILD · HASH EQUAL
- SOURCE: `proposals/03_PC_typed_outcome_one_door.md` Part C row R-PC-20.
- INSTRUCTION: `systems/combat/combat_engine_v1/state_graph.py`'s module docstring: "state that the graph is reference for the Plan-layer proposal and is not read by `wrapper.engagement`".
- WHERE: `systems/combat/combat_engine_v1/state_graph.py` (docstring).
- ADVANCES: none. TESTS: none.
- FALSIFIER and CONTROL: an importer of `state_graph` under `modules/` or `engine/` (`git grep -n state_graph modules engine` prints none). Control: AST of the file's code equal.
- GATE: `python systems/combat/combat_engine_v1/state_graph.py` → PASS.
- HASH MOVERS: none. DEPENDS ON: EXISTS-IN-TREE the file. GLOSSARY: none.
- COST and TIER: edit; `haiku`.
- LANDS IT: B14's producer; `Item: B14.09`, `[skip ci]`.

### B14.10 — the workbench's degree distribution reads the dice owner · Part C R-PC-42 · BUILD · HASH EQUAL
- SOURCE: `proposals/03_PC_typed_outcome_one_door.md` Part C row R-PC-42 (addendum F-PC-23).
- ADVANCES: none; S (one sampler's closed form, not a frozen copy).
- INSTRUCTION: `systems/combat/combat_engine_v1/workbench/probabilities.py::degree_distribution`: "the mean and spread of the exchange roll are read from the dice engine `core.resolve` uses (`roll_net_continuous`'s closed form, `sigma_leverage.band_odds` after `U5a_DICE_owed_edits.md` §1), not rebuilt from the frozen harness's constants; the falsifier the file names (`tests/valoria/test_combat_ob_from_defender_consumers.py`) is run once at landing".
- WHERE: `systems/combat/combat_engine_v1/workbench/probabilities.py` (`degree_distribution`).
- TESTS: `tests/valoria/test_combat_ob_from_defender_consumers.py` (existing), run once.
- FALSIFIER and CONTROL: `degree_distribution` reading a constant not imported from `engine/dice_engine/`. Control: no season path imports the workbench.
- GATE: `python -m pytest tests/valoria/test_combat_ob_from_defender_consumers.py -q` → pass; `grep -n "import" systems/combat/combat_engine_v1/workbench/probabilities.py` → `sigma_leverage` among the imports.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B05 (`band_odds` on the Normal closed form, `U5a_DICE_owed_edits` §1 row 2); EXISTS-IN-TREE `probabilities.py::degree_distribution`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B14's producer; `Item: B14.10`, `[skip ci]`.

### B14.11 — one door: the workbench calls the entry the loop calls · `03_PC_typed_outcome_one_door` Part B · BUILD · HASH EQUAL
- SOURCE: the same file, "Part B — one door", "Gate" 3, "Falsifier" (Part B), "Implementation" order (3) ("Part B last"); D-U1-08 (the record's raw `scores` are B15's, `U5b_PC_rulings_in_the_fight` §2; "Part B's four fields land first with defaults"); closes F-PC-11, R-PC-09, R-PC-10.
- ADVANCES: none; the standalone scene and the season scene become the same call (IS-B1 §1.1 row 6).
- INSTRUCTION:
  1. "`PersonalCombatInput` gains four fields, each defaulting to `()` so every existing record is the record it was: `traditions`, `techniques` (each party's `{name: level}`), `axes` (each party's `{axis: bonus}`; named `axes`, not `skills`, U1 glossary) and `dispositions`. `fight.py` passes them to `Combatant` (whose own attribute stays `skills`) as it passes kits. The season fills none of them until a carrier exists (`03_PC_person_inputs_content.md`)."
  2. "`fight(inp, rng, decide=None, cfg=None, max_bouts=None)`: the two extra parameters are the workbench's (a config overlay and a bout cap), forwarded to `wrapper.fight`; the host never passes them." (`max_bouts` is the tree's name until PCR-3, B16: `NAMES` there.)
  3. "`wrapper.fight(..., trace=None)`: the engine binds and restores `_TRACE` itself from the argument, so no caller touches the module attribute … `fight.py` passes a list's `append`."
  4. "`workbench/trace.py::run_traced_fight` and `workbench/balance.py::winrate` build a `PersonalCombatInput` and call `modules.combat.fight:fight`; `server.py::_make_fighter` becomes a record builder. `workbench/server.py` uses `HTTPServer` in place of `ThreadingHTTPServer` (one trace hook, one request at a time)."
- WHERE: `engine/season/queries/inputs.py` (`PersonalCombatInput`: four fields); `modules/combat/fight.py` (`fight`'s signature, the pass-through); `modules/combat/wrapper.py` (`fight`'s `trace`, `_TRACE` binding); `systems/combat/combat_engine_v1/workbench/trace.py` (`run_traced_fight`), `balance.py` (`winrate`), `server.py` (`_make_fighter`, the server class).
- TESTS: `[ASSUMPTION: test name; the item creates it]` `tests/valoria/test_combat_one_door.py::test_workbench_trace_and_entry_give_identical_events` (gate 3: "A workbench trace and an entry call at one seed and one matchup produce identical event lists"), written first and red (the workbench calls `wrapper.fight` on `Combatant`s).
- FALSIFIER and CONTROL: "one seed at which the workbench's result differs from the entry's on the same record". Control: `PersonalCombatInput` with the four fields at `()` gives B14.10's realm hash at seed 0 (`PersonalCombatInput` is not a `World` carrier: no encoding move).
- GATE: `python -m pytest tests/valoria/test_combat_one_door.py engine/season/tests/test_combat_module.py -q` → pass; `git grep -n "wrapper._TRACE\s*=" systems modules engine` → nothing; the realm hash (`HASH READING`) at seed 0 → equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 B14.01 (the record), B14.08; EXISTS-IN-TREE `workbench/trace.py::run_traced_fight`, `balance.py::winrate`, `server.py::_make_fighter`, `wrapper.py::_TRACE`.
- GLOSSARY: none (*skill* already rejects `skills` for the slot family; `axes` is the code's name).
- NAMES: `max_bouts` stays until B16 (`max_bouts` → `max_rounds`, PCR-3).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B14's producer; `Item: B14.11`, `[skip ci]`.

### B14.12 — the export carries the weapons, the derived quantities and the module constants · `03_PC_weapon_records_in_the_export` · BUILD · HASH EQUAL
- SOURCE: `proposals/03_PC_weapon_records_in_the_export.md` "The resolution, decided" 1–4, 7, "Exact edits" 1–4, "Gate", "Implementation" ("Exact edits 1 → 2 (regenerate with `--build`, never by hand) → 4 → 3; then the parity probe"); `U3_CONFLICT_LEDGER.md` C3-N17, C3-N18; A-29; closes F-PC-15, F-PC-20.
- ADVANCES: none; CLAUDE.md §5 and §6 (the port has the weapons it applies the coefficients to).
- INSTRUCTION (one item: the four edits share the exporter and its one gate, E-13):
  1. "`tools/export_engine_params.py`: `_weapons_section(weapons)` (authored fields only, an explicit field list taken from the schema header and refused on an unknown field, so a new field is a deliberate schema bump); `_derived_section(...)` calling the catalogue's quantity registry; `_defined_constants(path)` over the five modules; `_kit_section` split into `weapons` and `forms`; `SCHEMA_VERSION` 7 → 8 with its note." Decided: "Baked fields (`geo`, `gap`, `_derived`, `hand_guard`, `blade_guard`) are not exported as inputs"; the `derived` section is "per startable weapon, the quantities `workbench/catalogue.py::QUANTITIES` already enumerates … computed by the oracle … never an input"; the constants are collected "**defined in** `weapon_physics.py`, `combat_systems.py`, `combatant.py`, `ability_primitives.py` and `traditions.py` into sections of those names, by the syntax tree (assignment targets in the module's own body), not by `dir()`"; "`kit.weapons` lists the records without a `base` (50); `kit.forms` maps each form to its base (4)".
  2. "`engine/engine_params/combat_engine_v1.json`: regenerated, committed with the exporter."
  3. "`engine/substrate/combat_kit.py`: `WEAPONS` reads the 50; `FORMS` added for a reader that needs the mapping. No season file changes."
  4. "`modules/combat/config.py:1`: the header sentence corrected to say which constants `CFG` holds and which live with the physics (R-PC-18's wording if that lands first)" — B14.08 has landed it.
  5. The parity probe, written first as `systems/combat/combat_engine_v1/workbench/export_parity_probe.py` ("reads only `engine/engine_params/combat_engine_v1.json`; asserts no `modules.combat.weapons` in `sys.modules` after it runs"). "Inline literals stay where they are" (decided 7).
- WHERE: `tools/export_engine_params.py` (`_weapons_section`, `_derived_section`, `_defined_constants`, `_kit_section`, `SCHEMA_VERSION`); `engine/engine_params/combat_engine_v1.json` (re-derived); `engine/substrate/combat_kit.py` (`WEAPONS`, `FORMS`); `modules/combat/config.py` (line 1); NEW `systems/combat/combat_engine_v1/workbench/export_parity_probe.py`; `tests/valoria/test_engine_params_bridge.py`.
- TESTS: in `tests/valoria/test_engine_params_bridge.py` (existing), written first and red: `test_kit_weapons_lists_no_halfsword_form`, `test_every_constant_defined_in_the_five_modules_is_exported`; `tests/valoria/test_combat_invariants.py` (existing, reads the export) green.
- FALSIFIER and CONTROL: "A quantity the engine computes for a weapon that cannot be recomputed from the export; a constant defined in one of the five modules and absent from its section; a form accepted as a person's kit." The probe's planted control: "one exported mass edited in a copy … prints the weapon and exits 1". Control: "`build_realm(0)` one-season hash EQUAL" (B14.11's reading).
- GATE: `python tools/export_engine_params.py --check` → exit 0; `python systems/combat/combat_engine_v1/workbench/export_parity_probe.py` → `50 weapons; max |derived − recomputed| <= 1e-9`, exit 0 (the 1e-9 parity stated against the float contract, A-29); `python systems/combat/combat_engine_v1/workbench/structure_scan.py` section [H] → `[]`; the realm hash (`HASH READING`) at seed 0 → equal.
- HASH MOVERS: none in a season; "the export file itself (schema 7 → 8)", re-derived.
- DEPENDS ON: V12 B14.08 (the `CFG` moves), B14.11; EXISTS-IN-TREE `tools/export_engine_params.py::_kit_section`, `::_module_constants`, `SCHEMA_VERSION = 7`, `workbench/catalogue.py::QUANTITIES`, `engine/substrate/combat_kit.py`.
- GLOSSARY: none.
- COST and TIER: edit (exporter and one regenerated artifact); `sonnet`; GO review.
- LANDS IT: B14's producer; `Item: B14.12`, `[skip ci]`.

### B14.13 — a round opens with the weapon as issued · `03_PC_weapon_form_at_round_start` · BUILD · HASH EQUAL (season); the armour reference re-recorded
- SOURCE: `proposals/03_PC_weapon_form_at_round_start.md` "The resolution, decided", "Gate", "Implementation"; rulings A-101 (the code's `engagement` is one round); closes F-PC-16.
- ADVANCES: none; S (one reset for all per-round geometry).
- INSTRUCTION, in the source's order: "(1) write `workbench/round_state_probe.py` and record its pre-edit reading" (`systems/combat/combat_engine_v1/workbench/round_state_probe.py`: "for N fights over the four matchups, count fighter-starts whose `engagement_start` event shows a `_halfsword` record"); "(2) `base_form` in `combat_systems.py`" — "`base_form(c) -> str`, pure: `HALFSWORD_BASE.get(c.weapon, c.weapon)` (the mapping is already imported there and already the first line of `halfsword_target`)"; "(3) the reset line in `wrapper.py`'s open-measure loop" — "`c.weapon = S.base_form(c)` beside `c.grip_position = 0.0; c.lunge_depth = 0.0`. The wrapper owns the mutation, as now"; "(4) re-run the probe, `armour_participation.py --drift`, then `--update` once." "No constant, no draw: the reset reads no random number."
- WHERE: NEW `systems/combat/combat_engine_v1/workbench/round_state_probe.py`; `modules/combat/combat_systems.py` (`base_form`); `modules/combat/wrapper.py` (`engagement`'s open-measure reset); `systems/combat/combat_engine_v1/workbench/data/combat_armour_reference.json` (re-recorded by `--update`); `engine/season/tests/test_combat_module.py`.
- TESTS: `engine/season/tests/test_combat_module.py::test_no_engagement_opens_in_a_halfsword_form` ("a longsword against plate at three seeds; assert every `engagement_start` weapon key is a base key; `assert checked >= 1`"), written first and red; `tests/valoria/test_combat_invariants.py` must pass.
- FALSIFIER and CONTROL: "After the edit, an engagement whose `engagement_start` event shows a `_halfsword` record as either fighter's weapon; a fight between two arming swords whose trace differs from today's at any seed." Control: "The mirror control (`build_levers.py mirror`) for longsword in plate stays at 50 ± 2."
- GATE: `python systems/combat/combat_engine_v1/workbench/round_state_probe.py` → before "1,142 of 3,318 at 800 fights", after "**0**"; `python systems/combat/combat_engine_v1/workbench/armour_participation.py --drift` printed in the commit body, then `--update` once ("Expected movers: the four half-swording weapons at medium and heavy"); the realm hash (`HASH READING`) at seed 0 → equal to B14.12's.
- HASH MOVERS: "the armour reference and any pin that fights a half-swording weapon in rigid armour; season hash EQUAL". The armour reference is re-recorded here by its tool (the file's own rule); any such combat pin goes to B14.99.
- DEPENDS ON: EXISTS-IN-TREE `combat_systems.py::halfsword_target`, `HALFSWORD_BASE`, `wrapper.py` (`c.grip_position = 0.0; c.lunge_depth = 0.0`), `workbench/armour_participation.py`; V12 B14.12.
- GLOSSARY: none (the round's word is A-101's; `engagement` is the code's name until B16's PCR-3).
- COST and TIER: edit plus one deliberate re-record; `sonnet`.
- LANDS IT: B14's producer; `Item: B14.13`, `[skip ci]`.

### B14.14 — the survivor's grudge · intake `:491` CP-T03-06 · POINTER
- What it is: CP-T03-06 (carry-forward `master/eval/E1.md:467`, `E4.md:1074`): "MEASURE first, then DESIGN-FIRST, then BUILD — or CUT": at seeds 0–2, two seasons (`aperture 2 0`), for each fight a person survived with a Wounded band, read the survivor's `queries/person_q.py::regard` toward his opponent, whether it reaches a Candidate under `stance_polarity: declared`, and whether it is still held; non-zero, reaching and surviving → CUT with the reading quoted; zero or fading → the design names the cause it repairs ("no doer attributed or eviction") and builds only that.
- Where it lands: **B15-pc-calibration** (UNDECIDED (4)): it reads B14.16's `fell_to_hand` (the "no doer" cause) and B10's `02_CHAR_scar_is_a_wound` (the regard half); B15 follows both. Placed here by §5.6's first rule (`16_PESSIMIST_PC_C` names CP-T03-06) and moved by E-8's exception.
- GATE: none in B14; B15's author writes the MEASURE item with the entry's gate.

### B14.15 — what the world keeps of a fight: the scene's shape · `16_PESSIMIST_PC_C` 1 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/16_PESSIMIST_PC_C_what_the_world_keeps_of_a_fight.md` "The resolution, decided" 1, "Exact edits" rows 1–4 and 6, "Gate" 1, 3–5, "Cost class" (order: "the roster members → `SceneShape` and the module fold → the seam's return → `_eff_kill`'s Observations → `deed_doer` → the chronicle line"); D-U1-06; A-33, A-101; closes F-PES-PC-05.
- ADVANCES: R-01 and R-07 contributors (a deed others can hold); none moves.
- INSTRUCTION:
  1. `rosters.yaml: observation_terms` gains `blows_landed`, `fight_rounds`, `first_blood`, `lead_changes` (and `fell_to_hand`, used by B14.16, in this commit so the roster is edited once); "`first_blood` and `fell_to_hand` are deposited only through channels whose `observation_terms.supplied_by` includes `who`" (`co_located`, `witness_key`), never `document_key`, `post_remit` or `chronicle`; the counts ride every channel.
  2. `engine/season/queries/inputs.py`: "`CombatOutcome` gains `shape: SceneShape`":
     ```python
     @dataclass(frozen=True)
     class SceneShape:
         rounds: int                # rounds fought: the `turn_start` count (today's `bouts`; A-101, was `turns`)
         blows: Mapping[str, int]   # wounding blows LANDED, by claimant id
         first_blood: Optional[str] # who landed the first wounding blow; None if none landed
         lead_changes: int          # times the party ahead on Health fraction changed
         nearest: Mapping[str, int] # each party's lowest Health remaining during the scene, in points
     ```
  3. `modules/combat/fight.py` "builds `SceneShape` from `trace`; no engine change" ("a pure fold over `wound`, `turn_start`, `yield`; no new engine event").
  4. `seam/wrappers/combat.py::resolve` "returns `shape=` beside `beat=`".
  5. "`loop/effects_combat.py::_eff_kill` puts on the act's success Events, for each party `p`: `Observation(p, "blows_landed", shape.blows[p])`, and once per scene (subject the actor): `Observation(actor, "fight_rounds", shape.rounds)`, `Observation(shape.first_blood, "first_blood", True)` when not `None`, and `Observation(actor, "lead_changes", shape.lead_changes)`" (and `_eff_capture` through its base).
  6. "`engine/season/harness/chronicle.py::lines`: where an act's Events carry `fight_rounds`, the line appends `(n rounds, first blood X, k lead changes)`; a render change only."
- WHERE: `engine/season/rosters.yaml` (`observation_terms`); `engine/season/queries/inputs.py` (`SceneShape`, `CombatOutcome.shape`); `modules/combat/fight.py`; `engine/season/seam/wrappers/combat.py` (`resolve`); `engine/season/loop/effects_combat.py` (`_eff_kill`, `_eff_capture`); `engine/season/harness/chronicle.py` (`lines`); NEW `tests/valoria/test_combat_scene_shape.py`.
- TESTS: NEW `tests/valoria/test_combat_scene_shape.py` (beside `test_combat_audit_pins.py`), written first and red: `test_scene_shape_is_a_pure_fold_over_trace`, `test_played_and_automated_scenes_carry_equal_observations` (gate 4), `test_document_post_remit_and_chronicle_witnesses_hold_no_fell_to_hand` (gate 5; its `first_blood` half here, its `fell_to_hand` half green at B14.16). Gate 1 as a test of the same file `[ASSUMPTION: test name; the item creates it]` `test_a_seed_1003_fight_carries_its_shape` (the S1 probe restated, U3 §6.2: "the three Events of the seed-1003 fight carry `fight_rounds 8`, `blows_landed` for both parties summing to 5, `first_blood` and `lead_changes`"; the expected numbers are the scratch probe's at `826b747` and are re-read at this tree, the commit body quoting both).
- FALSIFIER and CONTROL: "A fight whose Events let a reader recover neither its length nor who struck first." Control: "with the Observations withheld the pre-change hash returns" (B14.13's reading at seed 0).
- GATE: `python -m pytest tests/valoria/test_combat_scene_shape.py -q -m combat` → pass (EXPECTED RED UNTIL B14.16: `test_fell_to_hand_names_the_prevailing_party`); the realm hash (`HASH READING`) at seed 0 → moved from B14.13's, named.
- HASH MOVERS: "every log with a fight (`Event.observed` is hashed)". B14.99.
- DEPENDS ON: V12 B14.01 (`CombatOutcome`), B14.03 (`fell_to`, the roster precedent), B14.13 (its source's order: "after … `03_PC_weapon_form_at_round_start.md`"); EXISTS-IN-TREE `rosters.yaml: observation_terms` (with `supplied_by`), `chronicle.py::lines`, `effects_combat.py::_eff_kill`, `::_eff_capture`.
- GLOSSARY: none `[ASSUMPTION: the five predicates are roster members, not glossary terms]`.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B14's producer; `Item: B14.15`, `[skip ci]`.

### B14.16 — the hand that killed is named · `16_PESSIMIST_PC_C` 2 · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, "The resolution, decided" 2, "Exact edits" rows `_eff_kill` and `deed_doer`, "Gate" 2, 5; A-33; closes F-PES-PC-06.
- ADVANCES: R-07 contributor (a self-defence killer becomes knowable).
- INSTRUCTION: "For a felled party who is the act's *actor*, `_eff_kill`'s Subject carries `Observation(felled, "fell_to_hand", prevailing_party)`. `queries/person_q.py::deed_doer` reads a `fell_to_hand` Observation on the claim's Event first and returns its value; the `seen.who` pairing stands for every other case." "the `LIMIT, stated` note … restated as closed". The roster member landed in B14.15.
- WHERE: `engine/season/loop/effects_combat.py` (`_eff_kill`); `engine/season/queries/person_q.py` (`deed_doer` and its `LIMIT, stated` note); `tests/valoria/test_combat_scene_shape.py`.
- TESTS: `test_fell_to_hand_names_the_prevailing_party` (gate 2) turns green; gate 5's `fell_to_hand` half green. Gate 2 restates the S7 probe (U3 §6.2): "in every scene where the actor is felled, `deed_doer` on the bystander's `person.died` claim returns the standing party; before the change it returns `None` or the dead man", over 100 fights `assert checked >= 100`.
- FALSIFIER and CONTROL: "a death in self-defence after which no witness can name the killer"; a `document_key` witness holding `fell_to_hand`. Control: with the Observation withheld, B14.15's hash at seed 0 returns.
- GATE: `python -m pytest tests/valoria/test_combat_scene_shape.py -q -m combat` → all pass; the realm hash (`HASH READING`) at seed 0 → moved from B14.15's, named.
- HASH MOVERS: every log where an actor is felled. B14.99.
- DEPENDS ON: V12 B14.15; EXISTS-IN-TREE `person_q.py::deed_doer`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B14's producer; `Item: B14.16`, `[skip ci]`.

### B14.17 — which term carries the read's slope · `U5b_PC_residue` §1 item 1 · READING
- The reading (Readings block, R14-1): "ablate in turn the read's logistic (`modules/combat/combat_systems.py`, `core.logistic((read_d-read_a)/1.0)`), `mode_sigma`'s read term, `init_emphasis_sigma` and `tempo_pressure`, at Perception 5 against 3, n 1,000, with the disjoint-seed control; record which moves the 94.2%." A workbench reading, no edit, run by `haiku` (`valoria-measure`) and read by `opus`; quoted at the close. Restates the scratch `fight_trace.py`/`pD_skill.py` probes (U3 §6.2) as a reading of `workbench/build_levers.py` `[ASSUMPTION: the ablation is run through `build_levers.py`'s lever table — basis: §1 item 3 names it the executable owner]`.

### B14.18 — the read's literal scale becomes `CFG['READ_SCALE']` · `U5b_PC_residue` §1 item 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5b_PC_residue.md` §1 item 2, "Gate", "Falsifier"; closes R-PC-43 (part), F-PES-PC-08 (part).
- ADVANCES: none; a lever a sweep can fit (B15).
- INSTRUCTION: "`modules/combat/config.py`: the literal `1.0` of the read's logistic becomes `CFG['READ_SCALE']` (value 1.0, byte-identical), so the exporter carries it and a sweep can fit it." The read site in `combat_systems.py` reads `cfg['READ_SCALE']`; re-derive the export with `tools/export_engine_params.py --build`.
- WHERE: `modules/combat/config.py` (`CFG['READ_SCALE']`); `modules/combat/combat_systems.py` (the read's logistic); `engine/engine_params/combat_engine_v1.json` (re-derived).
- TESTS: `tests/valoria/test_combat_invariants.py` (existing).
- FALSIFIER and CONTROL: "A fitted `READ_SCALE` under which Perception 5 against 3 still exceeds four points of score" (read at B15). Control: "`READ_SCALE` at 1.0 is byte-identical": the combat goldens and the realm hash at seed 0 equal to B14.16's.
- GATE: `python tools/export_engine_params.py --check` → exit 0; the combat goldens → equal; the realm hash (`HASH READING`) at seed 0 → equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 B14.12 (the export's schema 8), B14.08; EXISTS-IN-TREE `combat_systems.py` (`core.logistic((read_d-read_a)/1.0)`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B14's producer; `Item: B14.18`, `[skip ci]`.

### B14.19 — the grapple's outcome names say what they do · `U5b_PC_residue` §2 · BUILD · HASH EQUAL
- SOURCE: `U5b_PC_residue.md` §2 items 1–3, "Gate", "Falsifier"; closes F-PES-PC-10.
- ADVANCES: none.
- INSTRUCTION: (1) "`contact.py`: the note above `GRAB_OUTCOMES` states what each outcome does (a poise or an initiative shift) and that none removes a weapon, moves a fighter to the ground or holds him." (2) "The names are trace vocabulary and are **not shown to a player** … neither file renders a `GRAB_OUTCOMES` member today …, so there is no edit now; the rule binds the first rendering added" — written into the same note. (3) "The port does not carry the contact axis until one outcome has an effect a fold or a grid reads: one line in `11_GO_port_gate_order_and_coverage.md`'s coverage list" — that file is a proposal of the suite, not code; the line is B41's to read `[ASSUMPTION: no edit of a proposal in a code batch; B41's author carries it]`.
- WHERE: `modules/combat/contact.py` (the comment above `GRAB_OUTCOMES`).
- TESTS: none (a comment).
- FALSIFIER and CONTROL: "A player-facing string built from a `GRAB_OUTCOMES` member" (`grep -n "disarm\|foot_pin\|GRAB_OUTCOMES" systems/combat/combat_engine_v1/workbench/narrate.py systems/combat/combat_engine_v1/workbench/commentary.py` prints nothing). Control: AST of `contact.py` equal.
- GATE: the grep above → nothing; AST equality of `contact.py`.
- HASH MOVERS: none. DEPENDS ON: EXISTS-IN-TREE `contact.py::GRAB_OUTCOMES`. GLOSSARY: none.
- COST and TIER: edit; `haiku`.
- LANDS IT: B14's producer; `Item: B14.19`, `[skip ci]`.

### B14.20 — a self-fight is refused; `wrapper.fight` takes its `cfg` · `U5b_PC_residue` §4 · BUILD · HASH EQUAL
- SOURCE: `U5b_PC_residue.md` §4 edits 1–2, "Gate", "Falsifier", "Tests"; `R1_READ.md` §1.1 (no new raise on a port-reached path); U5a C5.
- ADVANCES: none; R (the mechanism at its extreme).
- INSTRUCTION: (1) "`engine/season/seam/wrappers/combat.py::resolve`: take `fight_estimate`'s `PARTY-GAP` line (`actor == target`) so one id as both claimants is refused before the engine is called." (2) "`modules/combat/wrapper.py`: `def fight(A, B, cfg=None, rng=None, …)` becomes `def fight(A, B, cfg, rng, …)` (no default for either; `cfg=None` still means `CFG` inside), and the fallback `rng=rng or random.Random()` is deleted, so a missing stream is a signature error at the call site, not a branch. … the three that omit `cfg` gain `cfg=None` explicitly: `modules/combat/fight.py`, `tests/valoria/test_combat_ob_from_defender_consumers.py`, `engine/season/tests/test_combat_module.py`." The `rng` half is also B06.05's (UNDECIDED (3)): kept once at merge; this item owns `cfg`'s half and the three callers.
- WHERE: `engine/season/seam/wrappers/combat.py` (`resolve`); `modules/combat/wrapper.py` (`fight`'s signature); `modules/combat/fight.py`; `tests/valoria/test_combat_ob_from_defender_consumers.py`; `engine/season/tests/test_combat_module.py`.
- TESTS: in `engine/season/tests/test_combat_module.py`, written first and red: `test_a_self_fight_is_refused_party_gap`, `test_wrapper_fight_has_no_default_stream`.
- FALSIFIER and CONTROL: "A combat test that passes with no stream supplied." Control: the realm hash at seed 0 equal to B14.18's ("no shipped act reaches it").
- GATE: "A hand-built self-fight returns `PARTY-GAP`; `git grep -n "random.Random()" modules/combat` prints nothing; `inspect.signature(wrapper.fight).parameters['rng'].default is inspect._empty`" (and `['cfg']` likewise); the realm hash (`HASH READING`) at seed 0 → equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 B14.11 (`fight.py`'s call shape); EXISTS-IN-TREE `seam/wrappers/combat.py::fight_estimate`'s `PARTY-GAP`, `wrapper.py::fight`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B14's producer; `Item: B14.20`, `[skip ci]`.

### B14.21 — six stale texts · `U5b_PC_residue` §5 · BUILD · HASH EQUAL
- SOURCE: `U5b_PC_residue.md` §5 table, "Gate"; closes R-PC-39, F-PC-22.
- ADVANCES: none.
- INSTRUCTION ("Each corrected at its site … in one commit"): `systems/combat/combat_engine_v1/workbench/build_levers.py` "the armour docstring: `act_cost` charges the wearer when Strength is short of the tier's demand"; `systems/combat/combat_engine_v1/state_graph.py` "`beat_exhaustion`'s note: 'not observed in 1,728 fights (addendum E-B15) nor in 11,000 (`16_PESSIMIST_PC.md` §1.3)'; the 'MEASURED, do not re-litigate' sentence deleted"; `state_graph.py`, "the `site:` values: line numbers dropped, as the injection table already did"; `workbench/probabilities.py` "the citation of `wrapper.py:173-198` re-pointed to the function name"; `modules/combat/weapon_physics.py:3` "`combatant.WEAPONS` → `weapons.WEAPONS`"; the quarantined skeleton under `.designs/` "not edited".
- WHERE: the five files named.
- TESTS: none.
- FALSIFIER and CONTROL: a code line changed (AST equality of each edited `.py` except `state_graph.py`'s `site:` strings). Control: the realm hash at seed 0 equal.
- GATE: "`python systems/combat/combat_engine_v1/state_graph.py` still prints PASS."
- HASH MOVERS: none. DEPENDS ON: V12 B14.09 (the same file's docstring). GLOSSARY: none.
- COST and TIER: edit; `haiku`.
- LANDS IT: B14's producer; `Item: B14.21`, `[skip ci]`.

### B14.22 — the workbench's `trace.py` stops shadowing the library · `U5b_PC_residue` §6 item 2 · BUILD · HASH EQUAL
- SOURCE: `U5b_PC_residue.md` §6 item 2, "Gate"; closes R-PC-21's second half, F-PC-11 (part).
- ADVANCES: none.
- INSTRUCTION: "`systems/combat/combat_engine_v1/workbench/trace.py` shadows the standard library's `trace` once its directory is on `sys.path`. It is renamed `fight_trace.py` with its importers, **five** at the tree: `workbench/commentary.py`, `workbench/server.py`, `workbench/narrate.py`, `systems/combat/combat_engine_v1/state_graph.py`, `tests/valoria/test_combat_tradition_levers.py`" (re-grep at the item's open: `git grep -n "\btrace\b" systems/combat tests/valoria | grep import`). "The path inserts in `modules/combat/` themselves … get no edit" (B13 removed them).
- WHERE: `systems/combat/combat_engine_v1/workbench/trace.py` → `fight_trace.py` (`git mv`); its importers.
- TESTS: `tests/valoria/test_combat_tradition_levers.py` (existing, re-pointed).
- FALSIFIER and CONTROL: an importer left on `trace`. Control: B14.11's one-door test green.
- GATE: "`python -c "import trace; print(trace.__file__)"` from the workbench directory prints the standard library's path"; `python -m pytest tests/valoria/test_combat_tradition_levers.py tests/valoria/test_combat_one_door.py -q` → pass.
- HASH MOVERS: none. DEPENDS ON: V12 B14.11 (rewrote `run_traced_fight`). GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B14's producer; `Item: B14.22`, `[skip ci]`.

### B14.23 — the lasting mark may be drawn (shipped at today's arm) · `U5b_PC_residue` §7 · BUILD · HASH EQUAL
- SOURCE: `U5b_PC_residue.md` §7 items 1–3, "Gate", "Falsifier", "Tests", "Lands"; rulings A-30, A-5, A-6, A-7, A-8; closes G-22 (`audits/25_GROUNDING_ENGINE.md`), H-258 (with B14.25).
- ADVANCES: R-09.d contributor at the flip (B15); none at ship.
- INSTRUCTION:
  1. "`rosters.yaml: body_mark_models` gains `drawn`; `data/fixtures.py`: the swept set becomes `none` (control) / `deepest_gate` (today) / `drawn`; the shipped value stays `deepest_gate` until the gate is read."
  2. "`_marks` under `drawn`: for each survivor at his limit, one roll keyed `H(seed, tick, victim, "fight.mark")` (A-30: its own key, never a position in the scene's stream after the mortal-wound draw …): pool his body band, obstacle the fixture `mark_ob`, on the one sampler. Failure: the ceiling falls two bands' worth (`marked_ceiling` applied twice); Partial: it falls as today; Success and better: no mark. One Observation `marked` on the Event." Written in the ruled form (UNDECIDED (5)): the pool is the one pool rule on the untrained default, the survivor's body band entering as levels through the `wounds` source (A-6, A-7, A-8), as `14_VERBS_PHYSICAL_A` A3 states for the sibling draw; the key through the one draw owner (`draw_factory`, B06) — in the step's parallel order B06 merges first (`V12_STRUCTURE_part3.md` §7.4) and this item's stream is whatever `draw_factory` returns on its base. `marked` joins `observation_terms`.
  3. "A3's Partial band ('left for dead, the lasting mark follows') keeps its certainty" (B15's).
  4. `mark_ob` is a new `Fixtures` key with its register row (IDS: H block slot 1), `[ASSUMPTION]` value, `[JUSTIFIED: …]` tag pointing at that row.
- WHERE: `engine/season/rosters.yaml` (`body_mark_models`, `observation_terms`); `engine/season/data/fixtures.py` (`body_mark_model`'s swept set, `mark_ob`); `engine/season/loop/effects_combat.py` (`_marks`); `engine/season/hole_register.yaml` (the `mark_ob` row); `engine/season/tests/test_combat_module.py`.
- TESTS: "`engine/season/tests/test_combat_module.py::test_drawn_marks_yield_all_three_outcomes_over_200_seeds` (`assert checked >= 200`), `::test_deepest_gate_reproduces_the_pre_change_hash`", written first (the first red: no `drawn`).
- FALSIFIER and CONTROL: "Under `drawn`, a mark on every such survivor." Control: "(`deepest_gate`) reproduces the pre-change hash" (B14.22's reading at seed 0).
- GATE: the two tests → pass; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); the realm hash (`HASH READING`) at seed 0 → equal to B14.22's.
- HASH MOVERS: none at ship ("At the flip: every fight with a survivor at his limit", B15).
- DEPENDS ON: V12 B14.03; EXISTS-IN-TREE `effects_combat.py::_marks`, `rosters.yaml: body_mark_models`, `fixtures.py::body_mark_model`; V12 Batch B05 (the one sampler, the one pool rule `pool_of`).
- GLOSSARY: none.
- IDS: H block slot 1.
- COST and TIER: small build; `sonnet`.
- LANDS IT: B14's producer; `Item: B14.23`, `[skip ci]`.

### B14.24 — a fight is priced by believed odds · `U5b_PC_residue` §8 · BUILD · HASH MOVER(behaviour)
- SOURCE: `U5b_PC_residue.md` §8 items 1–3, "Gate", "Falsifier", "Movers", "Depends on"; U5a F-DICE-14 Edit C; addendum C-9; rulings A-1, A-30.
- ADVANCES: R-08 contributor (a choice weighed on a believed picture); none moves.
- INSTRUCTION:
  1. "`believed_chance`: for a row whose prize binds the `personal_combat` provider, the answer is the `estimate` provider's (`seam/wrappers/combat.py::fight_estimate`: the resolver sampled on a private stream keyed `H(seed, tick, believer, "estimate.fight")` (A-30), moving no hash), read over the bands asked, **on the believer's own picture of the opponent** (his kit and wounds as the believer's ledger gives them; the world's where he has seen them). A person who knows nothing of the opponent's kit gets the default kit, not the true one."
  2. "No closed form and no table: an estimate is the resolver sampled (Layer 1 §27.2; A-1)."
  3. "`fight_estimate`'s sample count for this caller is a fixture (`believed_fight_samples`, seed 60: a belief is not a measurement), separate from the display's 400." Its register row: IDS H block slot 2.
- WHERE: `engine/season/seam/wrappers/sigma.py` (`believed_chance`); `engine/season/seam/wrappers/combat.py` (`fight_estimate`'s caller-picture input and key); `engine/season/seam/wrappers/_estimate.py` (`rng_of`'s purpose, if the key is built there); `engine/season/data/fixtures.py` (`believed_fight_samples`); `engine/season/hole_register.yaml` (its row).
- TESTS: `[ASSUMPTION: test name; the item creates it]` `engine/season/tests/test_combat_module.py::test_a_hurt_man_forms_fight_less_often_on_believed_odds` (the gate's reading as a test: "with `odds_weighting: believed`: a person at `body` 400 forms `fight` on an unhurt opponent less often than the same person unhurt, over seeds 0 to 29", `assert checked >= 30`), written first and red; `::test_an_estimate_reads_no_kit_the_believer_has_no_claim_about` (the falsifier).
- FALSIFIER and CONTROL: "An estimate that reads a kit the believer has no claim about." Control: "the estimate's stream leaves `content_hash` unchanged when the act is not chosen"; with `odds_weighting: none` the hash at seed 0 equals B14.23's.
- GATE: the two tests → pass; the realm hash (`HASH READING`) at seed 0 → moved (`odds_weighting` ships `believed`, `data/fixtures.py`), named.
- HASH MOVERS: "Every world in which a violent Candidate is scored." B14.99.
- DEPENDS ON: V12 Batch B05 (`10_DICE_believed_odds_have_a_prior` Edits A–B); V12 B14.01 (`fight_estimate` reads the record); EXISTS-IN-TREE `sigma.py::believed_chance`, `combat.py::fight_estimate`, `fixtures.py::odds_weighting` (`believed`, H-248).
- GLOSSARY: none.
- IDS: H block slot 2.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B14's producer; `Item: B14.24`, `[skip ci]`.

### B14.25 — five register rows brought to the tree · `U5b_PC_residue` §9 · BUILD · HASH EQUAL
- SOURCE: `U5b_PC_residue.md` §9 table, "Gate".
- ADVANCES: none.
- INSTRUCTION: "H-64 closed: `fight` is a table row; the stale symbol in its text stays marked. H-264 re-pointed: the duel is no longer the only door; `03_PC_duel_chain_reach.md` and A-16's carrier are named as its closers; it closes when `aperture` shows a fight from a person's own act. H-349 re-measured by `16_PESSIMIST_PC.md` §2.3 (light armour 1.5 points; plate a certainty); pointed at `16_PESSIMIST_PC_D`. H-97 pointed at `U5b_PC_rulings_in_the_fight.md` §3. H-258 grade corrected from 'closed as an assumption' to 'a certainty at the gate (G-22)'; pointed at §7" (B14.23 here; the flip in B15).
- WHERE: `engine/season/hole_register.yaml` (H-64, H-264, H-349, H-97, H-258).
- TESTS: none.
- FALSIFIER and CONTROL: `register --check` refusing an edited row. Control: no code.
- GATE: "`python -m engine.season.harness.register --requirements` still loads"; `--check` → exit 0.
- HASH MOVERS: none. DEPENDS ON: EXISTS-IN-TREE the five rows; V12 B14.23. GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B14's producer; `Item: B14.25`, `[skip ci]`.

### B14.26 — the conditional test loops assert they asserted · `IS-PC-04` (`U5b_PC_residue` §10) · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_B1_PC_MB_DICE.md` "Item: IS-PC-04" (its reading P-4); `proposals/U5b_PC_residue.md` §10 (INCOMPLETE, SITE: `unified/U4_DOCUMENT_STATUS.md` §3.4); closes U5b §10, `audits/01_CORE_audit_addendum_C_tests.md:263`'s PC hand-over.
- ADVANCES: none; CLAUDE.md §0.1 pt 2.
- INSTRUCTION (§5.7 SITE: the first step records what is found): "the criterion, stated: a `for` loop inside a `test_*` function in which every `assert` sits under an `if`, a `try` or a `match`. P-4 applied it to `tests/valoria/test_combat*.py` and finds four functions: `test_combat_duel_terms.py::test_yield_and_blood_are_different_stops` (no counter in the function); `test_combat_invariants.py::test_rear_clearance_monotone_non_decreasing` (over `C.WEAPONS.items()`); `test_combat_invariants.py::test_reach_class_beats_arming_not_inverted`; `test_combat_strength_jobs.py::test_an_armoured_weak_fighter_tires_faster_than_an_unarmoured_one`. The last three already name a counter-like variable and are opened first to see whether it is asserted. For each function that does not assert its count, add a counter and `assert checked >= N` with `N` read from the roster the loop covers, as the proposal's step 2 orders." "`[ASSUMPTION: these four are the set to edit; the proposal's count of ten came from a scan with a criterion this lane cannot see — basis: P-4; the landing session re-runs the scan over the files it touches and edits what it finds, without widening to other lanes' tests]`". The scan is run once as a reading (`ast` over `tests/valoria/test_combat*.py`), its output in the commit body, no file committed (the restated `scan_tests.py`, U3 §6.2).
- WHERE: `tests/valoria/test_combat_duel_terms.py`, `tests/valoria/test_combat_invariants.py`, `tests/valoria/test_combat_strength_jobs.py`.
- TESTS: the edited functions themselves.
- FALSIFIER and CONTROL: "with the loop's roster emptied in process, each edited test fails on its counter". Control: the three files green as shipped.
- GATE: "the three files green; the emptied-roster run red" (`python -m pytest tests/valoria/test_combat_duel_terms.py tests/valoria/test_combat_invariants.py tests/valoria/test_combat_strength_jobs.py -q` → pass; the emptied-roster run, by `monkeypatch` in a scratch invocation, → each edited test fails).
- HASH MOVERS: none. DEPENDS ON: nothing. GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B14's producer; `Item: B14.26`, `[skip ci]`.

### B14.27 — a challenge heard of is accepted (with the addressed-Record reader) · `14_VERBS_PHYSICAL_A` A0, A4 · BUILD · HASH EQUAL
- SOURCE: `proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` "A0 — the shared primitive", "A4 — `accept`", "Order of landing", "Gate", "Falsifier"; `audits/14_VERBS_PHYSICAL.md` §4.7 (the gate); A-21 (a challenge stays in person, `with`); `unified/U3_DEPENDENCY_ORDER.md` §4.1 row 52 (A4 in B14); UNDECIDED (2) (A0 with it); closes the audit's §4 (`accept` refused 27 of 27 on `exists:challenge=0`).
- ADVANCES: R-05 contributor (`accept`; its BUILT OUT reading is B29's, IS-A §12.2); R-04.c5 (i) re-read.
- ⚠ STEPS 1 TO 3 ARE EXISTS-IN-TREE (landed in B01; re-marked 2026-11-14, B01's terminal critique): `world_q.py::addressed_records` (with a `named` parameter) and `::challenges_heard`, stamped as `Record` by `questions_for` beside `writs_held`, and `accept`'s `referent_class_note` already says the challenged forms `accept` on a challenge he has heard of (the "minted into the challenger's hand … until H-229's `give`" sentence is gone). Do not rebuild them. What this item still owes is the gate test through the real chooser, its falsifier on the stamp alone, and the aperture reading. The test cannot start red (the behaviour it gates exists), so it is written green and seen red on the planted `()`; nothing in the engine is edited, so the realm hash does not move (HASH EQUAL).
- INSTRUCTION (as first written; steps 1 to 3 are the record of what B01 landed, not work):
  1. A0, `engine/season/queries/world_q.py`:
     ```python
     def addressed_records(w: World, p: Person, kind: str) -> tuple[str, ...]:
         """Live Records of `kind` whose addressee key (`RECORD_CONTENT["addressee"]`) is `p.id` and whose id
         `p`'s own ledger names (`person_q.ledger_names`), sorted. A Record addressed to a man who has not
         heard of it is not his business. The one owner of "addressed to him and heard of", read by the
         warrant stamp (A1) and the challenge stamp (A4). Resolver-side, read-only (`detainees_held`' shape).
         No mint, so ED-IN-0292 (1) stands."""
     ```
  2. A4, `queries/world_q.py`: "stamp term `challenges_heard(w, p)` = `addressed_records(w, p, CHALLENGE_KIND)`, stamped under `Record` in `_stamped`."
  3. A4, `verb_table.yaml`, row `accept`, `referent_class_note`: "replace the sentence beginning *'⚠ A CHALLENGE IS MINTED INTO THE CHALLENGER'S HAND'* through *'…until H-229's `give` reaches the realm.'* with *'A challenge is minted into the challenger's hand. The challenged forms `accept` on it once he has heard of it (`world_q.challenges_heard`, 14_VERBS_PHYSICAL_A A4); the cell asks nothing of holding.'*" `STOPS IF` the sentence is not in the note at the item's open (B01's lane A may have rewritten the row): the commit body quotes the note as found, and the replacement sentence is appended in its place.
- WHERE: NEW `engine/season/tests/test_vm_phy_a_custody.py` (the only file this item writes; `world_q.py` and `verb_table.yaml` are read, not edited).
- TESTS: NEW `engine/season/tests/test_vm_phy_a_custody.py` ("four functions, one per gate of the audit's §1.7, §2.7, §3.7, §4.7"); this item writes the A4 function, first, GREEN on the tree (B01 landed the stamp) and seen red on the planted `()` below: `[ASSUMPTION: test name; the item creates it]` `test_accept_forms_on_a_heard_challenge` — the audit §4.7 gate: "A seeded realm with one planted dispute between two co-located persons, run through the real chooser with no hand-built act, produces `challenge.issued`, then an `accept` attempted by the challenged, then a scene fought under `blood` terms with `duel.yielded` or `body.changed`. **Control:** without the new stamp, the challenged's opening set has no `accept` (the pre-change shape after lane A). **Planted failure:** the stamp reader returning `()` reproduces 0 `accept` formations." B15 (A3) and B29 (A1, A2) add the other three functions.
- FALSIFIER and CONTROL: "return `()` from `challenges_heard`" (alone, by monkeypatch) turns the test red. Control: as the gate's. (`engine/season/tests/test_b11a_duel_reach.py`'s chain falsifier, B01's, drives formed Candidates through hand-built acts and reverts the whole lane at once; this test is the real chooser and the stamp alone.)
- GATE: `python -m pytest engine/season/tests/test_vm_phy_a_custody.py -q` → pass; `python -m engine.season.harness.aperture 2 --seeds 0 1 2` read once and quoted (no before/after: nothing is edited): "`accept` refusals on `exists:challenge` equal 0"; the realm hash (`HASH READING`) at seed 0 → equal to B14.25's.
- HASH MOVERS: none (EQUAL): `accept`'s formation moved the hash in B01 (`test_b11a_duel_reach.py`'s `POST`), not here.
- DEPENDS ON: EXISTS-IN-TREE `world_q.py::addressed_records`, `::challenges_heard`, `::questions_for`'s stamp, `CHALLENGE_KIND`, `person_q.py::ledger_names` (all landed in B01); V12 Batch B01 (lane A's duel chain: the challenge Record addressed to the challenged).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`; the gate read by `opus`.
- LANDS IT: B14's producer; `Item: B14.27`, `[skip ci]`.

### B14.28 — the opponent model: the design · intake `:492` PC-21 · DESIGN-FIRST
- SOURCE: the intake `:492` PC-21 (carry-forward `master/eval/E1.md:3838`, `E4.md:3403`, copying `workplans/valoria_master_workplan_v11_part17.md:65-77`); ED-IN-0347; rulings A-112 (combat reads skill scores through the skill table), D-18; placed at the batch's tail (§5.6's third rule: no member names PC-21; its text says "design-first at B14/B15").
- ADVANCES: none; R (the opponent read) for a later build.
- INSTRUCTION: write the design stating (1) to (4) with falsifiers, no code (the entry's REMAINING UNBUILT, copied): "(1) familiarity as a per-bout input set by the seam (AR-47, AR-48), derived from the holder's own past fights against that weapon class (`wclass`) and his tradition's skills, storing nothing (adj §2.2 (viii)); the label function stays the module default for un-seamed callers; where a person's tradition lives (no `Person` carrier exists; CR-33's keys are the candidate); (2) the anticipation on a missed read, combining familiarity, the defender's Attunement and the opponent's visible state, and its effect on the draw order (the `modes[rng.randrange(3)]` contract); (3) the opponent's state composed from what the module already tracks (fatigue, wounds, poise, initiative, `disp`) before any new quantity is coined (AR-38); (4) nearness to yielding read against PC-10a's threshold, and its consumer, or the statement that it has none yet (AR-42)." After B06, the draw-order contract reads `modes[rng.below(3)]` (`NAMES`). A choice the design cannot settle by the ladder ends the batch's run `STOPPED` for Jordan (D-18); the build lands in the next batch that edits `modules/combat` and `seam/wrappers/combat.py` after the design merges (the entry: "its builds slot by R8 into the next batch editing `modules/combat` and `seam/wrappers/combat.py`").
- WHERE: NEW `proposals/2026-11-12-pc-opponent-model/00_DESIGN.md` `[ASSUMPTION: path — basis: CLAUDE.md §3, new design work goes to `proposals/`; the entry says "ONE design file under `proposals/`"]`.
- TESTS: none (no code).
- FALSIFIER and CONTROL: the entry's EXIT: "the file states (1) to (4) with falsifiers: at least, a fighter with a record of fights against a weapon class reads it better than one without, and equally at no record; an attuned defender's missed-read guess beats a uniform one against a fixed-disposition opponent and not against a neutral one; CONTROL: every term at its control reproduces the base hash and the combat pins. No code."
- GATE: the file exists and states (1) to (4), each with a falsifier; `git diff --name-only <batch-start-sha>..HEAD -- engine modules tools` shows nothing from this commit; a `ners` critic's reading in the commit body.
- HASH MOVERS: "the design none; each build declared."
- DEPENDS ON: EXISTS-IN-TREE `modules/combat/traditions.py` (`familiarity`), `combat_systems.py::read_contest`, `world_q.practice`; V12 B14.27 (none of substance: the tail position).
- GLOSSARY: none (the design proposes; a word it coins is added when its build lands).
- NAMES: `rng.randrange(3)` → `rng.below(3)` (B06.04).
- COST and TIER: design; `opus`, `high`, with a `ners` critic.
- LANDS IT: B14's producer on `opus`; `Item: B14.28`, `[skip ci]`.

## Readings (B14)
- R14-1 (B14.17): the ablation table of `U5b_PC_residue` §1 item 1 at Perception 5 against 3, n 1,000, each of the four terms ablated in turn, with the disjoint-seed control; the term that moves the 94.2% named. Copied into the close's commit body as run.

### B14.99 — re-pin and close readings · E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `03_PC_typed_outcome_one_door` gate 2 ("Season hashes: seeds 0 to 2 equal to the pre-change hashes with the `prevailed` value and the `fell_to` Observation each reverted; each one moved alone and named in the commit body"); CLAUDE.md §7.
- ADVANCES: none (the record of the close).
- INSTRUCTION: (1) Re-record, once, every pin the RE-PIN line names that an item moved; old and new values in the commit body; each mover of the BATCH GATE named with its seed-0 reading from its item. B06 merges first in S8 (part 2 §3): rebase on its merge first and read B06's after-reading as the baseline (`V12_STRUCTURE_part3.md` §7.4; lane H3). (2) The batch's readings (BATCH GATE) and R14-1. (3) No `reading:` record (no conjunct named).
- WHERE: the pin files of the RE-PIN line.
- TESTS: none new; the full suite once (E-2).
- FALSIFIER and CONTROL: a moved pin not traced to a declared item. Control: each mover reverted alone returns the hash before it.
- GATE: the BATCH GATE, read once on this commit's tree.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: V12 B14.01 to B14.28.
- GLOSSARY: none.
- COST and TIER: reading; `sonnet` runs, `opus` reads the R-PC-17 goldens if any moved.
- LANDS IT: B14's producer; `Item: B14.99`, the batch's last `Item:` commit (no `[skip ci]`).

SERIAL EDGES: within the batch: B14.01 → B14.02 → B14.03 (Part A's three commits, the movers "each alone") → B14.04, B14.05, B14.07, B14.08 (Part C "after Part A") → B14.11 (Part B "last" of its file) → B14.12 (after the `CFG` moves and the one door; "R-PC-18's wording if that lands first") → B14.13 (its source: "after `03_PC_typed_outcome_one_door.md` and `03_PC_weapon_records_in_the_export.md`") → B14.15 → B14.16 (`16_PESSIMIST_PC_C`'s order; the roster edited once in B14.15) → B14.18 (the export at schema 8) → B14.20 (after `fight.py`'s call shape) → B14.23 → B14.25 (H-258 points at B14.23) → B14.27 → B14.28 → B14.99. B14.09 → B14.21 (`state_graph.py`). B14.11 → B14.22 (`run_traced_fight` rewritten before the rename). B14.01 → B14.24 (`fight_estimate` reads the record).
  With other batches, by file (U3 §5.1, `→` landing order): `seam/wrappers/combat.py` B04 → B06 → B14 → B15 → B16; `modules/combat/wrapper.py`, `combat_systems.py` B05 → B06 → B14 → B15 → B16; `queries/inputs.py` B05 → B14 → B15 → B16; `loop/effects_combat.py` B04 → B12 → B14 → B16 → B17 … (U3 lists B12 before B14 by handle; in time B14 (S8) precedes B12a (S13), and the merge order is §2.1's); `queries/person_q.py` B04 → B06 → B09 → B10 → B11 → B14 … (B14 edits `deed_doer`, a different function from B06's and B09's); `queries/world_q.py` B05 → B06 → B07 → … → B14 (`addressed_records`, `challenges_heard`, `_stamped`) → B15 → B21 → B29; `rosters.yaml` B05 → B07 → B14 → … (`fight_endings`, `observation_terms`, `body_mark_models`: keys B07 does not edit); `verb_table.yaml` B07 → B14 (`accept`) → B15; `hole_register.yaml`, `requirements.yaml` (permanent surface, from B14's blocks); `tools/export_engine_params.py`, `combat_engine_v1.json` B14 → B15 → B17; `systems/combat/combat_engine_v1/workbench/` B14 → B15 (PCR-1's `round_probe.py`). The census rows U3 lacks (the workbench files, `chronicle.py`, `contact.py`, `combat_kit.py`) are H2's to merge.
PARALLEL: S8 with B06-keyed-draw (IN). Shared files: `modules/combat/wrapper.py` (B06.04 the aggressor tie-break in `engagement`, B06.05 `fight`'s `rng` default; here B14.11 `fight`'s `trace`, B14.13 `engagement`'s open-measure reset, B14.20 `fight`'s `cfg`): `fight`'s signature line is edited by both (UNDECIDED (3)), so the coordinator serialises the pair on that file or keeps the one line by hand at merge (`V12_STRUCTURE_part3.md` §7.3); `modules/combat/combat_systems.py` (B06.04 the commit's Beta draw and `read_contest`; here `base_form`, the 18 constants, the read's scale: different functions, except that B14.08 moves constants `read_contest` may read — merged by hand); `engine/season/seam/wrappers/combat.py` (B06.04 the contest call's stream; here `resolve`'s return, `fight_estimate`): one function, `resolve`, edited by both — serialised or kept by hand; `seam/wrappers/sigma.py` (B06.01 `believed_chance`'s sum, B06.05 the roll's default; here B14.24 `believed_chance`'s combat branch): one function edited by both — kept by hand; `queries/person_q.py` (B06.01's sums; here `deed_doer`). Both are mover batches: B06 merges first, B14 rebases and re-pins once (§7.4).

| STOP. Batch B14-pc-outcome closes here |

---
