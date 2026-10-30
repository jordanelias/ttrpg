# ADJ3: Events/decks, arcs/NPC arcs, clocks/world/victory (C-250..282, C-283..373, C-629..670; 166 rows)

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Part 07c of the suite: conflict adjudication ADJ3 (adjudicator subagent; `adjudication/ADJ3_events_arcs_clocks.md`, 166 rows C-250..C-373 and C-629..C-670); the suite's 754 recorded conflicts are split over 07a to 07d by cluster. The session copied the file into the suite at 07:10:35 under this name. Base: the Write call of 07:04:04 (16,175 bytes). Replayed in time order: five Edit-tool calls (07:04:19, :22, :28, :32, :36) and five python heredocs (07:04:55, 07:05:10, 07:05:20, 07:05:28, 07:05:35), all applied, none failed. Result 14,308 bytes, equal to the size the session recorded at 07:10:36, and byte-identical (line numbers stripped) to the session's own read of the file at 07:05:54. Nothing touched it after the copy into the suite. Every Edit-tool call and every heredoc against this file in the transcript was replayed, so unlike parts 01 to 04 nothing in this file is known to be missing. The first line below is the file's own heading; the banner, provenance and rule were inserted after it. The suite was written in a session of 2026-10-28 that committed nothing; its files existed only in that session's scratchpad. This file is a reconstruction from the session transcript (second pass, 2026-10-30; the first pass could not see this part), not the original file. Where this text and the tree disagree, the tree wins; every figure and line citation is as of the session's HEAD (`ttrpg` be24c71) and is unre-verified.

---

Repo `be24c71`. Every cite was opened or re-measured.

**Head.** No row needs Jordan. 57 sit on a retired mechanism (Π, CI/IP/RS/MS/WC/Accord/Turmoil/PV scalars, Loyalty and Coup counters, the Key log, GM procedures); 35 are design-vs-design rows the plan or a later ruling decides; the rest are stale cites, drifted numbers or code-wins. Most important corrections: REPORT §11 item 7's ED-IN-0225 question is answered by precedent (withdraw it), and Vaynard's "empty" Arc A/B bodies exist in the superseded v1 file.

## Measured at HEAD (the numbers the clusters below rest on)
- **Tensions.** `engine/season/tensions.yaml` is absent. The plan adopts 6 cards. `build_realm(tensions=True)` "draws one card, equally likely" (`workplans/valoria_master_workplan_v10_part4.md:526`). The cards are Royal Crisis, Feldmark Famine, Cardinal Independence, Guild Fracture, Einhir Incident and Ministry Crisis (`:527`). The switch ships off.
- **Card counts.**
  - Jordan's 45 = Tensions 6 + Goldenfurt 28 + 11 named cards (`_part6:218`; `_part12:274-275`).
  - Goldenfurt is 3+5+3+4+5+6+2 = 28 (`.designs/systems/settlements/goldenfurt_slice/reference/event_deck.md:17-25`).
  - Grounded deck "58" is the file's claim (`proposals/grounded_event_card_deck_v1.md:5`, `:21-22`; 40 KEEP + 19 REVISE = 59); by script it names 50 card ids and writes 8 in full. Not in the 45.
- **Arcs.**
  - 55 numbers, 58 titles (16-18 exist twice: `gm_ref/arcs_10_18.md`, root `arcs_16_19.md`); `_part12:276` agrees.
  - `ENDINGS_CLASSIFIED.yaml`: 50 rows = 48 ARC (01-18, 20-45, R16-R19) + EMG-10/11. By script: 18 unforced DECIDER/ROLL, 11 forced, 8 THRESHOLD, 9 NEVER, 2 UNCLEAR, matching `_part4:529`.
  - ARC-19 is ARC-R19. ARC-46..55 are unclassified (they are in `cases/ARC4.yaml` only).
  - The 9 NEVER rows are ARC-05, 16, 24, 25, 26, 28, 36, 38 and 39 (39 is forced).
  - 97 ARC-lane cases; 143 = 97 + 46 NPC (archive ledger `:3209-3237`).
  - ARC-S* is a third series, from the deleted 138-arc arc_register (`references/propagation_map.md:73`).
- **Clocks.** None runs in the loop.
  - The loop has "six steps, four barriers… no container gets a clock" (`engine/season/loop/driver.py:239-240`) and "NO CLOCK GENERATES" (`loop/census.py:39`).
  - CI, IP and RS were retired at 29a/29b (`systems/overview/sim/__init__.py:9-13`).
  - `ms_track.py` (MS_START 60) is still on disk with no importer. Its retirement is owed at 29a-ms.
  - The lattice coupling replaces the MS scalar (`hole_register.yaml:4884`; `loop/matter.py:136-138`).
  - Turmoil, Accord, WC, Prosperity, PV: zero hits in `engine/season` py.
- **Endings.** Two rows exist: `peninsular_sovereignty` (victory) and `theocracy` (`rosters.yaml:2553-2615`). Both are read by `endings_reached`. None is reachable: H-176 is graded `absent` (`hole_register.yaml:3969-3978`). The fix is CP-T09-04's unpeopled `seize` (`_part8:27`).
- **Calendar.** There is no year unless `season_factor_draw` has a table, which ships `()` (`queries/world_q.py:936-942`). A card may not carry a date (`_part4:526`; T-c).
- **Records and tenures.**
  - `record_kinds` = text, dispensation, petition, works, faction_sheet, cover (`rosters.yaml`).
  - `tenure_kinds` has 10 members, including detain, ban, tie and knot.
  - `open_case` mints kind `text` (`loop/effects_information.py:286-287`).

## Clusters
| cluster | rows | class | winner and basis | action |
|---|---|---|---|---|
| Π draw and bands | C-250, C-280 | R | Π is a stored pressure aggregate; refused by T-a (`_part12:274`) [RETIRED] | none |
| Deck size 60-100 | C-251, C-281 | R | Per-season deck refused (M16(b), `_part4:525`); moot | none |
| soak, chronicle, census "unbuilt" | C-252..254 | C | `harness/soak.py:7` grades two things; `harness/chronicle.py` exists; `loop/census.py:96` writes | none |
| `01_THE_TEN` count | C-255 | N | 14 items + §F; PROPOSED, held back | none |
| v7/v8 workplan cites | C-256 | S | Only v10 exists (`ls workplans/`) | read as v10 |
| FORCE-* vs occasion emitter | C-257 | D | M16(b): FORCE-WEATHER adopted, emitter refused (`_part4:525`) | none |
| deck "exists" vs "none" | C-258, C-282 | C | No deck code. Both decks stay PROPOSED and held back (`_part4:525`) | none |
| card-id schemes | C-259 | D | Plan prefixes Propositions `tension_<card>_` (`_part4:526`). Case ids are series-prefixed (CR-44, `_part12:276`) | none |
| ED-IN-0225 location | C-260 | S | The row is at archive `:3209`. The archive is the ledger for pre-September ids | none |
| arrangement keys | C-261, C-273 | N | 13 keys + id = 14 (`data/arrangements.py:72`; `arrangements.yaml:8-14`) | none |
| proceedings K-rows | C-262..266, C-274..277 | C | Code: 6 record kinds; `detain`/`ban` tenures; `WARRANT_ACT = "dispatch"` (`state/gate.py:272`); arrest detains to the issuing seat (`verb_table.yaml:189`). `interrogate`, `confession.made` unbuilt (`hole_register.yaml:4765-4769`) | none |
| `sim/` paths in auto_manual | C-267 | S | `sim/` is dissolved (CLAUDE.md §3) | none |
| Tensions size, draw, contents | C-268, C-269 | D | Plan: 6 cards, draw 1, conflict_architecture's six (`_part4:526-527`); early_game's 8/draw 2 and T1-T3 lose | none |
| Löwenritter pressure; calendar deadlines | C-270, C-271 | D | Cut (`conflict_architecture_proposal.md:153`, `:157`). Dates are also barred from cards (T-c, `_part4:526`) | none |
| MS ×3 per battle | C-272 | R | MS scalar [RETIRED] | none |
| EventImpact, Doc 12 vs Keys | C-278, C-279 | R | Both dead (ED-IN-0232); live form `Event.causes[]` (`state/carriers.py:258`) | none |
| arc counts and denominators | C-283, C-290, C-299 | N | See "Measured" above. ENDINGS (arc closings) and `rosters: endings` (realm ends) are different objects | none |
| same number, different arc | C-284, C-285, C-297, C-323 | S | Series prefixes resolve it: ARC-NN = gm_ref, ARC-R16..19 = root, NSC-NN = scenario chains (`ENDINGS_CLASSIFIED.yaml`; `cases/ARC5.yaml`) | none |
| arc-reachability internals | C-286..289, C-373 | D | Later §3.1 governs; story and mechanism are separate scores (`04_SYNTHESIS.md:8-20`) [UNVERIFIED: exp-8] | none |
| Torben loyalty clock, Coup Counter, Warden at MS ≤ 50 | C-291..293 | R | Counters and the MS scalar [RETIRED] | none |
| throughline self-drift | C-294..296 | N/S | The table beats the prose summary. The file is `throughline_resolutions_v30.md` | none |
| arc form (prose, branches, ladder) | C-298, C-369 | D | M20(b): ordered stage conditions on the person's own ledger; `closing`, `successor` and `deal` are struck (`scratchpad/src/v10-05-jordan-queue.md:165-170`) | none |
| chain/*.yaml unparseable | C-300 | C | Committed evidence read by `corpus_run` (`harness/corpus_run.py:226-233`), not loaded data | none |
| NPC arc maps (Himlensendt C, Vaynard A/B, arc_expansion_v1) | C-301, C-302, C-372 | S | v30 lost the bodies; `.designs/systems/npcs/reference/npc_behavior_system_v1.md:496-506` has Vaynard A/B in full, `:466` Himlensendt C's "TS may awaken from 0". arc_expansion_v1 is now `arcs_src/.../arc_expansion_v30.md`. Triggers [RETIRED] | transcribe from v1 |
| narrative voice canon vs skill | C-303..306, C-311, C-368 | D | No CURRENT.md voice row; the canon file is quarantined, so `skills/prose-writer/SKILL.md` is the one live surface (render-only). Coherence tiers (narrator) and Truth tiers (`solmund_voice_v30.md` §18, liturgical register) are two registers, not rivals. Neither has input: no Person coherence field, only a write guard (`state/world.py:1010-1017`) [GAP] | SKILL.md cites by bare filename |
| SHAPES vs arc classifier | C-307, C-370 | S | `SHAPES` holds contest-outcome shapes in the orphaned kernel (`systems/social_contest/sim/contest/narrative.py:25`), not arcs | none |
| relationship model | C-308 | C | `tenure_kinds`: `tie`, `knot` | none |
| Goldenfurt vs grounded card schema | C-309 | D | Neither is adopted. CL-EVENTS (3)'s Tensions schema is the one schema, and either deck reopens card by card through it (`_part12:274-275`) | none |
| P-03 and "no omniscient narrator" | C-310 | D | This derives from P-03 (`canon/02_canon_constraints.md:44`); it does not contradict it. P-03's "GM is the rendering engine" clause is [RETIRED] | none |
| level-0 name | C-367 | D | Canon says "Coherence Failure" (`canon/01_foundations_amendment_self_rendering.md:92`), and canon beats the skill's "Rendering Crisis" (`coherence-tiers.md:264`) | rename the skill heading |
| gm_ref arcs 1-18 internal drift | C-312..322 | R 7, S 3, N 1 | PI, IP, Debt tokens, NPC AI table, "4d10 TN7", Pull Ob [RETIRED]. Card index: 25 (`gm_ref/arcs_10_18.md:527-557`). README and file names: archive history | none |
| arcs 20-35 drift | C-324..345 | R 13, C 4, N 2, S 3 | MS/RS, IP, Loyalty, Mandate, Stability, CI/TC, TT, Coup Counter [RETIRED]. Tiles: Askeheim T15, Schoenland T16 (`systems/settlements/valoria_geography_v30.yaml:201-216`). TS authored per cast row (`data/cast.py:283`), written by none (`harness/loops.py:96`). No exchange count in the interim roll | none |
| arcs 36-55 drift | C-346..363 | R 10, D 7, C 1 | CV, Mandate, MS/RS, Torben start, coup ceiling, Stability [RETIRED]. 46-55: `arcs_46_55_resolved.md` (later) governs; ED-411 (resolved) beats T-09 (proposed). Radiation: lattice coupling, one ring a season (IN-35) | none |
| precedent disputes | C-364..366, C-661..669 | P | External facts only | none |
| emergent working records | C-371 | L | The head is `narrative_engine_design_v2_churn.md`, RATIFIED, ED-IN-0011 (`CURRENT.md:35`) | none |
| CI seizure and ceiling | C-629..631 | R | `ci_track` retired at 29b | none |
| MATTER duties; deaths | C-632, C-670 | C | Three motions, maturation, fading, standing crossings (`matter.py:1`, `:187`, `:401-437`); hunger binds after CR-22 [UNVERIFIED] | none |
| ending layers | C-633, C-634 | C | Vocabulary built, nothing reachable (H-176) | build CP-T09-04 (B10-17) |
| step and tick labels | C-635, C-637 | N | Six steps, four barriers (`driver.py:239`). `w.tick` is the only season count | none |
| hunger cover | C-636 | C | Counts ore and timber as food; CR-22 owns it [UNVERIFIED] | none |
| ED-IN-0202 | C-638 | L | Last row: closed, 2026-10-26 (`editorial_ledger_in.jsonl`) | none |
| Accord, Prosperity, RS scales | C-639..641, C-654 | R | Stored scalars cut (#457 §5, `rosters.yaml:2591`). `starting_pros` in geography is read by nothing | none |
| calamity radiation types | C-642 | C | Replaced by the IN-35 lattice coupling (`hole_register.yaml:4884`) | none |
| Partition and Terminal | C-643..646, C-659 | D 4, R 1 | GD-1: sole victory, and Partition is STRUCK (`canon/04_game_design_constraints.md:27`). The Terminal route rides on MS [RETIRED] | none |
| IP occupation; IP from battles | C-647, C-655 | R | `ip_track` retired at 29a | none |
| Turmoil vs Strain; win clauses | C-648, C-660 | D | ED-WR-0004 superseded as to mechanism. GD-1's Accord, PS and sustain clauses survive only as the `rosters.yaml:2590-2600` assumption (`_part10:131`) | none until H-176 opens |
| PV 31 vs 30 | C-649 | R | PV retired. Code counts every territory under a `realm` rung | none |
| WC endgame | C-650 | R | Ambient track [RETIRED] | none |
| MS/RS naming; MS start | C-651, C-652 | R | Both scalars [RETIRED]. MS_START 60 survives only in the unimported `ms_track.py` | 29a-ms deletes it |
| Elske start | C-653 | R | Loyalty scalar [RETIRED] | none |
| Articulation | C-656, C-657 | R | Consumes the Key log (`articulation_layer_v30.md:16-18`); reference only | none |
| duplicate §5, victory_v30 | C-658 | S | Archive typo | none |

Stale registry: `references/module_contracts.yaml:542` and `registers/mechanics_index.yaml:140` call `ms_track` the "live tick"; it has no importer (`systems/overview/sim/__init__.py:9-10`). Fix both in the 29a-ms commit.

## Corrections to the proposals and the main report
1. **REPORT §8 item 3 and §11 item 7(c): the ED-IN-0225 question is not Jordan's.**
   - ED-IN-0225 refuses only an arc *carrier* (archive `:3209-3237`), and M20(b) already narrowed it (`v10-05-jordan-queue.md:165-170`). The plan already quotes arcs as provenance: B6.n ladders name their source arc (`_part12:276`); Tensions rows quote archived lines in `source:` (`_part4:527`). It routes NEVER arcs to "an open situation whose opening conditions are Tensions-shaped" (`_part4:529`).
   - Fix: delete the sub-question; amend `_part12:276` "no arc is a carrier, a card field or a loaded row" to "…a carrier or a loaded row; a row may quote one in `source:`". A provenance string changes no behaviour.
2. **REPORT §8 "only 2 of the 9 NEVER arcs are among the numbered 55" is wrong:** all 9 are numbered; the "2" is the NEVER-WORKED pair (19, 52). REPORT §9 "arc 19 is both a NEVER arc and dead" is wrong too: ARC-R19 is DECIDER, forced.
3. **REPORT §9, A5 §4: "Vaynard A and B empty" is a transcription loss.** The full bodies are at `npc_behavior_system_v1.md:496-506`, and Himlensendt C's TS clause is at `:466`. Fix: "recoverable from the v1 file".
4. **A5 §2, REPORT §8 (Rendstad), P1-B (Klapp):** `open_case` mints a `text` Record (`effects_information.py:286-287`); `assessment` and `exposure` are not record kinds. Mark both NEW, each landing with its reader.
5. **A5 §2 "each world draws 6 (2 Tensions plus 4 openable)":** the plan draws 1 Tensions card (`_part4:526`). Fix: 1 + 4 = 5, so P ≥ 25. The REPORT already says one card.
6. **REPORT §7:** cite "6 cards, draw 1" to the plan (`_part4:526-527`, `_part6:217`), not the archive (§0.05).
7. **A5 §1, REPORT §7:** the grounded deck's "58" is its own claim (50 ids named, 8 written); keep it out of Jordan's 45.
8. **P1 table, B column "M3 + ED-IN-0225 narrowed":** change to "M3 + a plan-text amendment (`_part12:276`)", per item 1. P1-C's "arcs as templates" (arcs as loaded rows) is a real change and stays an amendment.

## Needs Jordan
None. Code, a later ruling (M16(b), M20(b), ED-WR-0004 superseded, GD-1) or plan text decides every cluster. Nearest candidate: GD-1's sustain/Accord/PS clauses, held as the `rosters.yaml:2590-2600` assumption under the plan's LEAVE trigger (`_part10:131`), which cannot fire before CP-T09-04.

## Rows resolved by class (166)
R 57 · D 35 · C 27 · S 21 · N 12 · P 12 · L 2 · J 0.
