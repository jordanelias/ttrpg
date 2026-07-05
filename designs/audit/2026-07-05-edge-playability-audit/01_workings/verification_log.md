# Fable verification log — edge-playability audit

## Status: RATIFIED (Jordan, 2026-07-05 — "Ratify all", with the report)
_Every headline claim carried into `../edge_playability_audit_v1.md` was independently re-checked
by the Fable orchestrator against the working tree (commit `28be79c` + this branch), per the
charter's relay discipline. Format: claim → check → outcome._

## Confirmed verbatim / by direct read

| # | Claim (cluster) | Check | Outcome |
|---|---|---|---|
| V1 | `sim/personal/investigation.py` entry points are stubs (A) | read L22–31 | CONFIRMED — all three `NotImplementedError("Pass 2l armature stub")` |
| V2 | fieldwork Interview is still single-roll, no Lattice/Gate tokens (A) | grep `fieldwork_investigation.md` | CONFIRMED — 0 hits for Lattice/Gate/Genome; Interview = "Attunement" row |
| V3 | combat_engine_v1 has no fieldwork-Exposure consumer (A) | grep engine `*.py` | CONFIRMED — only in-fight `overcommit_exposure` (`wrapper.py:189`) |
| V4 | §9.6 chamber-violence auto-forfeit (A) | read `social_contest_v30_infill.md:47-49` | CONFIRMED verbatim |
| V5 | No fieldwork/investigation row in CURRENT.md (A) | full read of CURRENT.md | CONFIRMED — also no scale_transitions / player_agency rows (I) |
| V6 | `faction_politics_expanded_v1.md` does not exist (C/E) | `find` whole tree | CONFIRMED — dead file; 57 corpus citations still point at it; "debt scene" exists ONLY in `scale_transitions_v30.md:138` |
| V7 | articulation §3.1 = 10 triggers; no scene_outcome family, no env.disaster/env.crisis, no standing_change; da.covert_betrayal gated `exposed==true`; §6.4 L296 asserts battle_concluded "already triggers Tier 2" (C/D/G) | read §3.1 table + L296 | CONFIRMED. Correction applied: trigger #3 fires succession only for `succession_mode in [contested, emergency, imposed]` — routine succession does NOT fire (narrows cluster C's "unconditionally") |
| V8 | settlement_layer_v30.md contains zero "Key"/"emit" tokens; module contract emits only `env.population_change`; `g_ord0`/`g_def0` carry no emit clause (G) | grep -c + contract read | CONFIRMED — grep count 0 |
| V9 | `state.standing_change.trigger` enum includes `death`; officer deaths emit child standing_change Keys (G) | read registry L488–505, L702 | CONFIRMED |
| V10 | UI v4/v4_1/v4_2 have zero hits for Why?/diagnostic/chronicle/Key log/articulation (G) | grep -c all three files | CONFIRMED — 0/0/0 |
| V11 | §5.5 vs §2.7 Accord/Order stacking contradiction; §7 Step 4c resolves neither (B) | read `peninsular_strain_v30.md:196` + scale_transitions §5.5 | CONFIRMED — "stack normally… cap ±1 per source" vs "do not stack… whichever produces the higher Accord applies" |
| V12 | ED-936 routing note denies direct consumption of contest/combat_resolved while module_contracts faction_state `consumes` lists contest_resolved (B) | read `faction_behavior_v30.md:433` + contracts L72 | CONFIRMED verbatim |
| V13 | `private_observers` hard-coded on ambient-fabric Keys (F) | grep doc-12 | CONFIRMED at 6 sites (L134, 358, 387 + visibility_defaults L451/476/519) |
| V14 | npc_behavior §6.1/§6.1b are empty headers (F) | read L675–690 | CONFIRMED — literally empty |
| V15 | Thread-violation companion departure: "No appeal roll — the act is unambiguous" (F) | read `companion_specification_v30.md:163` | CONFIRMED verbatim (ED-666); Conviction-departure sibling row DOES allow a final appeal roll |
| V16 | faction_politics_v30.md is a real, CANONICAL home doc (E) | head + wc | CONFIRMED — 1,115 lines, `Status: CANONICAL (approved Jordan 2026-04-17, PP-660)`; module_contracts `doc: null` is stale |
| V17 | BG card-hand verb table exists at `params/bg/core.md` L208–232 (E) | read | CONFIRMED — Muster/March/Govern/Trade/Diplomacy/Survey/Fortify + per-faction actions |
| V18 | IP has narrated milestones 60/80/90; MS has none (E) | grep victory_v30 + params/bg/core.md | CONFIRMED with nuance: `params/bg/core.md:174` gives MS ≤50/35/20 *mechanical* Calamity-Drift steps, but no narrated Scene-Slate milestone ladder; the asymmetry claim stands for player-facing beats |
| V19 | fieldwork_hybrid §9.2 lacks the bonus-scene rule; it survives only in infill, GM-phrased, with the superseded 2–3 scene cap (I) | read §9.1–9.2 + grep infills | CONFIRMED |
| V20 | `params/board_game.md` links all point at nonexistent `references/params_bg_*.md` (I) | grep -c + ls | CONFIRMED — 16 `params_bg_` reference lines, 0 targets exist |
| V21 | `params/bg/victory.md` retains struck Varfell Path C (VTM=5) + VTM co-victory thresholds (I) | grep both files | CONFIRMED — Path C at 2 sites; `victory_v30.md:388` = "Path C — STRUCK (PP-663, 2026-04-19)" |
| V22 | scale_transitions §3.2 "GM recognises faction scope"; §6.1/§6.3 empty headers (I) | direct read (full file read by orchestrator) | CONFIRMED |

## Reclassified by verification

| # | Agent claim | Reclassification |
|---|---|---|
| R1 | Cluster D "CF2 NEW P2": mass_battle §A.10 War row −2/op vs cap −1/op | **KNOWN-TRACKED = ED-1010** (open, P1) — the ledger entry names this exact §A.10 contradiction ("CONTRADICTED by mass_battle_v30 §A.10 War row (-2/op) which also cites the cap to 'threadwork_v30 §3.2' where no cap text exists"). Carried only as seam-impact commentary. |
| R2 | Cluster I finding 5 "NEW": D.6 double-count | **KNOWN-TRACKED** — `propagation_spec_v1.md` §5's own ranked open-flag register carries D.6/OF-D6 (also HANDOFF_IN). The player-chair oscillation framing is the dossier's addition; the flag is not new. |
| R3 | Cluster C E3/E14 "succession fires Tier-2 unconditionally" | Narrowed — conditional on `succession_mode in [contested, emergency, imposed]` (V7). Routine succession is itself un-rendered, which folds into EP-4/EP-3's family pattern. |
| R4 | Cluster E "MS has no approach-warning ladder" | Nuanced per V18 — mechanical thresholds exist (Calamity Drift); narrated milestone beats do not. |
| R5 | Cluster C "debt scene per §1 missing from faction_politics_v30 §1" | Strengthened per V6 — the cited FILE is dead, not just the section; merges with cluster E's stale-doc:null finding into one dangling-citation family (57 sites). |

## Not independently verified (carried at dossier confidence, flagged in report)

- Cluster D CF7 (siege-turtle stack) — corroborates a prior hunt note; calibration-sensitive, left P3/UNDETERMINED as sweep target.
- Cluster F E1 latency-conflation risk (immediate stakes vs batched opinion) — the damper texts are confirmed; the "conflation" is interpretive, marked as design-risk not defect.
- Cluster G payload-sufficiency judgments (F-F) — registry lines confirmed; "sufficient for a because-clause" is qualitative.
- Line-number citations inside dossiers are the agents' own; section-level citations were the verification target.
