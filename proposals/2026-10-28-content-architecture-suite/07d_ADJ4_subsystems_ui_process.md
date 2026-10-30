# ADJ4: subsystem rules, UI/Godot, process (C-493..C-628, C-671..C-754; 220 rows)

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Part 07d of the suite: conflict adjudication ADJ4 (adjudicator subagent; `adjudication/ADJ4_subsystems_ui_process.md`, 220 rows C-493..C-628 and C-671..C-754); the suite's 754 recorded conflicts are split over 07a to 07d by cluster. The session copied the file into the suite at 07:10:35 under this name. Base: the Write call of 07:04:02 (15,065 bytes). Replayed in time order: one Edit-tool call (07:04:43) and six python heredocs (07:04:18, :25, :33, :49, :55 and 07:05:00), all applied, none failed. Result 14,330 bytes, equal to the size the session recorded at 07:10:36; the first 80 lines are identical to the session's partial read at 07:19:27. Nothing touched it after the copy into the suite. Every Edit-tool call and every heredoc against this file in the transcript was replayed, so unlike parts 01 to 04 nothing in this file is known to be missing. The first line below is the file's own heading; the banner, provenance and rule were inserted after it. The suite was written in a session of 2026-10-28 that committed nothing; its files existed only in that session's scratchpad. This file is a reconstruction from the session transcript (second pass, 2026-10-30; the first pass could not see this part), not the original file. Where this text and the tree disagree, the tree wins; every figure and line citation is as of the session's HEAD (`ttrpg` be24c71) and is unre-verified.

---

HEAD `be24c71`; verified at source unless tagged. VT = `verb_table.yaml`.

**Head.** 220 rows, 37 clusters; none needs a new design ruling. Code answers most:
- TN is 7 and refused otherwise.
- Wounds add fractional Ob.
- A personal fight resolves at RESOLVE; only a field resolves at ENCOUNTER.
- The mass-battle pool is quality times numbers, with no Command term.
- Godot is 4.7 (ED-GO-0002).
- Pre-quarantine "CANONICAL" lines yield to ARCHIVED banners (ED-IN-0231).

The downstream reports carry four real errors (§2): where the personal fight happens, "the verdict reads nobody", the odds policy for Proceedings, and P3's "new" rulings. Two items are Jordan's because they are Layer 0 or another repo (§3).

## 1. Clusters

| cluster | rows | class | winner, one-line basis | action |
|---|---|---|---|---|
| Dice TN | C-596 | C | TN 7 always: `_require_tn7` refuses any other value (`engine/dice_engine/dice_engine.py:182-199`); MB `roll_pool` asserts it (`modules/mass_battle/resolution.py:46`); VOLLEY_TN deleted (`systems/mass_battle/sim/bat.py:210`). D14's "never reads it" is superseded (ED-IN-0196) | none |
| Advantage vs obstacle | C-493, 494, 495, 592 | C/S | No conflict. Advantage is a μ-shift (`seam/wrappers/sigma.py:41`). The room's favour and forgery quality are *instance modifiers* under Jordan's 2026-08-14 "score/2 plus modifiers" (`modules/social_contest/roll.py:63-100`). The Gaussian `p_success` gap is real (R-F11) | build `odds_of` (B10-08) |
| Wounds, Health | C-497, 499, 520, 527, 552, 553, 595, 597 | C/D | ED-PC-0005 (`editorial_ledger_pc_archive.jsonl:3`): each wound adds a fractional Ob, 0.15 attacking and 0.25 defending (`modules/combat/config.py:123`), folded into net_sigma; `WOUND_POOL_PENALTY` removed (`combatant.py:16`). "−1D per wound" (UI v4.1, PP-716, fieldwork:112) loses. Thread Leap: +0.15 per wound beats a flat +1 (unbuilt). Health = §4.1 (`combatant.py:42`) | none |
| Combat formulas, resolver head | C-496, 518, 519, 521-526, 530-532, 537, 538 | C/S/N/L | `modules/combat/` is the head (`CURRENT.md:21`). The combat_reference and combat_engine_v1 formulas are reference. Seize is DEAD in code (`ability_primitives.py:25`, `combat_systems.py:1069`). HEAD LOC: combat 5,727, MB 10,163; 54 weapon keys | none |
| Fight timing, trace | C-498, 528, 529 | C | "the body" carries no `step:`, so it fights at RESOLVE (`engine/season/rosters.yaml:1079`, :1293-1300). Only "a field" has `step: ENCOUNTER` (:1284). The move to ENCOUNTER is REM-31 (B10-10, unbuilt). The trace is returned (`seam/wrappers/combat.py:252`) | build REM-31 |
| Margin ladder, outcome vocab | C-500, 501, 565-571 | C/R | One owner, `seam/ladder.py::degree_of`, with separate bands per subsystem (`combat_degree` :136, `field_degree` :185). Errata G5 and F-S1-3 ("shared four-band ladder") are wrong. The key_type_registry vocabularies and fuse/CI-curve arming are [RETIRED] | none |
| MB pool, stats, Command, morale | C-508-517, 536 | C/R | `POOL_QUALITY_MODEL` is on (`modules/mass_battle/config.py:556`): pool = eff_power × eff_size × 0.5, with **no Command** (Jordan 2026-07-08). Command = (2·CHA+COG)/3, clamped 1-7 (`core/exchange.py:55-64`), so caps 3 and 11 lose. Morale starts from the members' mean stance toward their own faction (`massbattle.py:119`); `_morale_start_from_stability` is deleted (:34). Templar power 5, disc 6 (`troop_types/registry.py:49`). Encirclement is a flat −1D, floor 1 (`orchestration.py:1304`). Faction Military stats are [RETIRED] | none |
| MB seam, errata K-F | C-502-507, 572 | C | D14's code side holds. A same-faction field cannot occur (`loop/sides.py:130-133` gives the subject None, so the field is Unopposed). | none |
| MB historical | C-533-535 | S | Superseded by ED-MB-0001..0003 | none |
| Fieldwork, Knots, case board | C-539, 541-548, 555, 556, 564, 591 | C/D/N | Knots: the ED-912 −5..+5 gauge (`systems/fieldwork/sim/knots.py:13-95`). Formation = Spirit×2 + History at Ob 2 (:57-59), so §5.6a's "+3" loses. Rupture −1 Coherence is kept in code (:95), flagged UNVERIFIED. knots.py is test-only. Interview goes through the Lattice (ED-FI-0004), but the VT row writes `[]`. Exposure and Cover (555, 556) are unbuilt: decide at build. **The case board is unbuilt** (0 symbols in engine/modules) | none |
| Threadwork rules | C-540, 549-551, 554, 557-563 | C/D/L/R | Code: `DEPTH_OB` and `DEPTH_TS_MINIMUM` (`operations.py:77-95`), Leap gate TS 30 (:358-366, beating the registry's 25), bands (`threadcut.py:37-42`), and Coherence as distance (`coherence.py`). The `keys.py:65` scale roster is [RETIRED] | none |
| Thread pool (PP-624) | (priority; no row) | D | M18 TAKEN (b), `min(3,history)+3` (v10 `-05` M18). The code still reads `min(3, history+3)` (`operations.py:246`) | build REM-45 (B10-15) |
| Old social contest rules | C-573-579 | C/D | Superseded by Proceedings (ED-SC-0033). Composure is retired (CR3; `contest/wrapper.py:319`). Opposed Ob = score/2 + modifiers (`roll.py:67-69`). The pool is `pool_default` for everyone (`sigma.py:119-131`) | none |
| SC kernel vs Proceedings | C-580 | D | ED-SC-0033 (2026-09-06) ruled the old kernel retired. SC-05 (2026-10-16) kept `roll.py` and did not adopt the kernel. The plan contradicts itself on timing: `_part3:489` "the plan's scheduling call (A1-58)" against `_part5:301` "HELD until Jordan names it". Step 2 settles it: retirement is ruled and the timing is scheduling | correct `_part5:301`; schedule SC-05. The CLAUDE.md §3 line goes to §3 below |
| Proceedings status, built | C-581, 582 | S/L | ED-SC-0039 flipped only README, 04 and 21. `07_THE_GAME` and `19_PLAN` stay reference, so there is no conflict. "Nothing exists until SC-01" is met (`rosters.yaml:1080` BUILT) | none |
| Speech kinds 12/15 vs 6 | (priority) | N | 6 are built, all forensic (`arrangements.yaml` `speech_kinds`). 12 is the design list (`04_VERBS.md:236-239`). 15 is a corroboration remark (:301-303), not a rival roster | build the rest under SC-02 |
| `systems/social_contest` 18 vs 47 files | (priority) | N | 18 files at HEAD (`git ls-files`). "47" predates the .md quarantine (ED-IN-0231) | none |
| Scales, Base Ob | C-593, 594 | D | Base Ob by scale is Thread-only (Jordan 2026-09-05, `requirements.yaml:43-44`, `roll.py:71`). The 5, 6 and 3 "scales" name different things | none |
| Precedent disagreements | C-583-590, 749-752 | P | Source-internal; no repo rule rests on them | none |
| Godot version | C-628 | L | **4.7** (ED-GO-0002, `editorial_ledger_go.jsonl:1`, RULED 2026-10-09; 4.6 superseded). `valoria-game` still pins 4.3 (`project.godot:11`, `godot-ci.yml:68`) and its README says 4.6 | Jordan side: GO-06/GO-13 (§3) |
| Godot repo state | C-598, 601-607 | C/N/S/R | Measured: 8 .tscn, 129 .gd, 37 .tres (22 characters, 15 triggers), 13 GdUnit suites (0 GUT), 289 `func test_`. Port constants have 13 keys against ttrpg's 6; the 7 extra keys (CI_START, VICTORY_SUSTAIN_SEASONS, COHERENCE_*) belong to retired models. Divergences (C-602) are decided by the engine under ED-1050: accord is [RETIRED] and Coherence is a distance. `godot/skeleton` still has 20 files (GO-14) | Jordan side; build GO-14 |
| Player seat | C-599, 600 | C | None. `dispatching_chooser` is called only by tests (`harness/play_surface.py:41`) | build REM-30/31 |
| Play-surface docs vs loop | C-608-610, 612, 613 | C/D/S | The code's return carries endings (`driver.py:537`) and the code's step list holds. Modes give way to fidelities on one resolver (ED-SC-0013, resolved); "no mode switch" agrees. The `sim/` paths are dissolved | none |
| Godot docs | C-614, 615, 743, 744 | L | The conversion strategy is PROPOSED and governing. The four 2026-04-18 docs are STALE (CLAUDE.md §6) | none |
| UI spec status, parts, counts | C-611, 616-621, 625-627 | L/N/S | Every UI file is ARCHIVED (ED-IN-0231 banners). v4 skips Parts 10-20 (`valoria_ui_ux_v4.md:1504`→:1779); v4.1 restructures into Parts 0-14 (:901-1190). v4.1 is 1,438 lines; the audit has 69 F-ids, 16 P1. No live UI spec | none |
| UI retired tracks | C-622-624 | R/D | The CD and Taint tracks and the 10→0 Coherence thresholds are [RETIRED] (ambient tracks; Coherence is a distance). Scale/Breadth is an unexecuted, archived rename | none |
| Key substrate | C-671, 672, 753 | R | [RETIRED], ED-IN-0232 (`registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml:3779`). `keys.py` is gone. Port `KeyStore.gd` survives | port-side delete |
| GM premise | C-754 | R | [RETIRED] (CLAUDE.md:5). `factions_personal_v30.md` lives in `.designs` | none |
| ED id locations | (priority) | S | ED-IN-0204, 0225, 0231 and 0232 are in `registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml` (:1956, :3209, :3697, :3779), not in the jsonl files | none |
| Status words | C-681-683, 690, 699, 704, 706, 723, 724 | L | The ledger's last row decides. ED-IN-0113 is closed. ED-IN-0243 and ED-IN-0299 are ratified as intent. Ratification is per file (ED-SC-0039 pattern), so README headers that say "HELD BACK" yield to the flipped files | none |
| Workplan versions, pointers | C-691-694, 745-747 | S/N | v7 and v8 are FORKED (`references/restructure_ledger.md:2629`, :2836-2838). The live `_part4` and `_part5` govern. ED-IN-0300 is ratified (row 86). B10-02 closed in be24c71 | none |
| M2 carrier | C-707 | D | The B10-19 card says "changes code: no" (`_part3:449`) | correct the head §4 text: M2 has no building batch until NM-W4..W9 slot |
| Verb lexicon | C-695-698, 700-702 | C/N/D | VT decides: 56 rows. `argue` is present and `persuade` absent. `levy`, `repudiate` and `interrogate` are absent. `evade / defy` and `tie / knot` are single rows | none |
| BUILT labels | C-674, 677, 679 | C | `systems/world/sim/npe.py` is deleted (29d), so "BUILT" there is stale. No relational-graph symbol exists | none |
| PP numbering, allocation | C-680, 722 | S | PP-684..688 became PP-711..715 (`patch_register_active.yaml:17`). PP is not frozen: CLAUDE.md §4 freezes the flat ED sequence; PP uses `next_free` | correct the canon/behavior cites |
| Vocabulary collisions | C-678, 748 | D/C | "Ascendancy layer" breaks THE LAYERS for new work only (ED-IN-0179: no retrofit). The alias_registry phantom vocabulary loses to doc plus code | none |
| Decision-layer notes | C-686-689 | S/D | No conflict: `stance_gain` reads at 1+g with g=1, so 2× is the documented behaviour (`choose.py:73-77`). The precedence and Habit claims are unbuilt proposals | none |
| Line drift, process wording | C-675, 676, 684, 685, 703, 705, 708-721, 725-727 | S/C | The faction-string truncation is fixed (`npc_registry.yaml:1466`, :1498). Grading-wording rows: process-only, dropped (§0.1 pt 5) | none |
| Status-map rows | C-728-742 | L | CURRENT.md and the ledgers decide | none |
| Balance oracle | C-673 | S | Retired (file absent; CLAUDE.md §7). The throughlines caveat is stale | none |

## 2. Corrections to the proposals and the main report

1. **REPORT §14 table (line 321)** says "`contest` provider and ENCOUNTER step BUILT" for personal combat. It should say "`contest` provider BUILT, fought at RESOLVE (`rosters.yaml:1079`); ENCOUNTER holds only `a field` (:1284); the move is REM-31." **A7 §3 "(ENCOUNTER step)"** should read "RESOLVE".
2. **"The verdict reads nobody: pool 2 vs Ob 2"** (REPORT:228 and :323, A4:47, A7:90, P3:35). Since SC-02 `22a`, the obstacle subtracts the bench's `reception` (gain 1.0, H-215) and the unmirrored `proofs` (`roll.py:63-100`; `test_sc02_reception.py`). The fix: "the pool reads nobody (`pool_default`, `sigma.py:119-131`), and under the H-213 ceiling of 2 the room can only *lower* the obstacle." [UNVERIFIED: non-zero reception in a seeded run.]
3. **A7 §5 "Conflict … the newer ruling wins: show the band"** is wrong. `21_RECONCILIATION.md:617`, ratified as intent (ED-SC-0039), refuses to show the room, the obstacle or the odds, and makes that refusal structural. CP-T01-03 is NARROWED and held (`_part13:40`). Proceedings shows no odds, as P3 has it.
   Settled: combat facts only (Jordan, this session); Proceedings none (21:617); the actor's own other rolled acts band odds (CP-T01-03 (a)).
4. **P3 L-1 "NEW ruling"** is Jordan's own directive from this session. Record it as a GO/PC ledger row citing his words, and do not ask him again.
5. **P3-B L-2** says believed odds were "withdrawn (AM-B-03)". The decision round's M1 DECISION *releases* CP-T01-03 mode (b) (v10 `-05` M1; `_part4:144`). A display reader is a build, not a new ruling.
6. **P2:79, Command.** Under `POOL_QUALITY_MODEL` (default on, `config.py:556`), Command does not enter the raw combat pool; it reaches morale, formation-hold and rout only. The coded derivation is `round((2·CHA+COG)/3)` clamped 1-7 (`exchange.py:55-64`), with no "key excess". A `command` key therefore moves no exchange roll unless that term is added.
7. **A4:16 "UI v4 jumps Part 9 → 21"**: Parts 10-14 exist in v4.1 (`valoria_ui_ux_v4_1.md:901-1190`). All UI files are archived.
8. **REPORT:32 (valoria-game)**: add that it pins 4.3 against the ruled 4.7, and that its hand-copied `game_constants.json` carries 7 keys for retired models (13 against ttrpg's 6).

## 3. Needs Jordan (2)

1. **CLAUDE.md §3, Layer 0 (NEW).** The line "systems/ — design source of truth for combat, social_contest and mass_battle (retained by ED-IN-0204)" contradicts ED-SC-0033's retirement of the old SC kernel and ED-IN-0284's "all as modules". ED-IN-0283 (d) leaves that line to you. Recommend rewording it: those subsystems' code lives in `modules/`, the old kernel `systems/social_contest/sim/contest/` retires at SC-05, and the `systems/` folders stay as homes (ED-IN-0283).
2. **valoria-game version and divergences (M13, an ACTION; GO-06/GO-13).** Your repo still pins Godot 4.3 (README says 4.6) against your 4.7 ruling, and it carries the retired accord tracker and the 10→0 Coherence track. Recommend one port PR: move to 4.7.x, drop the 7 stale constants, and delete `KeyStore.gd` and the 15 trigger resources (ED-1050: the port follows the oracle).

## 4. Rows resolved by class

| C | S | L | D | R | P | N | J | total |
|---|---|---|---|---|---|---|---|---|
| 70 | 49 | 37 | 29 | 13 | 12 | 10 | 0 | 220 |

By heading: SUBSYSTEM 105, UI/GODOT 31, PROCESS 84.
