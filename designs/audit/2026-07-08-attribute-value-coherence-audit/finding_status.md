# Finding status — tallies through the critic funnel

## Status: PROPOSED (read-only audit, 2026-07-08) · Lane: IN · Anchor: ED-IN-0029

## 1. Before / after the critic funnel

### 1.1 As filed by the 7 dossiers (75 findings)

| Cluster | P1 | P2 | P3 | Total |
|---|---|---|---|---|
| C1 attributes/aggregates | 5 | 4 | 2 | 11 |
| C2 derived values | 3 | 3 | 4 | 10 |
| C3 pools | 1 | 7 | 2 | 10 |
| C4 tracks/clocks | 6 | 6 | 3 | 15 |
| C5 faction/settlement | 3 | 5 | 5 | 13 |
| C6 code constants | 0 | 3 | 5 | 8 |
| C7 cross-index | 3 | 4 | 1 | 8 |
| **Total filed** | **21** | **32** | **22** | **75** |

### 1.2 Critic verdicts (per cluster, findings only; unification-option verdicts in §1.4)

| Cluster | uphold | soften | sharpen | overturn | missed filed | missed folded as distinct |
|---|---|---|---|---|---|---|
| C1 | 8 | 3 (F3, F7, F9) | 0 | 0 | 1 | 1 (M1) |
| C2 | 7 | 2 (F1, F2) | 1 (F3) | 0 | 1 | 1 (M1) |
| C3 | 9 | 1 (F4) | 0 | 0 | 2 | 1 (M1; M2 deduped → C7-F2) |
| C4 | 12 | 2 (F1, F7) | 1 (F9) | 0 | 2 | 1 (M2; M1 absorbed into F9's sharpen) |
| C5 | 10 | 3 (F3, F8, F9) | 0 | 0 | 2 | 1 (M2; M1 deduped → C1-F11) |
| C6 | 4 | 3 (F2, F6, F8) | 0 | **1 (F5)** | 2 | 2 (M1, M2) |
| C7 | 4 | 3 (F1, F3, F8) | 1 (F2) | 0 | 1 | 1 (M1) |
| **Total** | **54** | **17** | **3** | **1** | **11** | **8** |

Check: 54+17+3+1 = 75 filed. 75 − 1 overturned + 8 distinct critic-sourced = **82 confirmed**.

Softens by effect: 5 severity downgrades (C2-F1/F2 P1→P2; C4-F1 P1→P2; C4-F7 P1→P2 + kind
collision→crosswalk; C5-F3 P1→P2 + kind→enforcement-gap; C5-F8 P2→P3; C7-F8 P2→P3 +
kind→stale — that is 7 rows, of which 2 also recalibrated), 4 calibration-only corrections
(C1-F3 NEW→KT; C1-F9 NEW→KT; C3-F4 NEW→KU; C7-F1 NEW→KT; C6-F8 KT→NEW), 4 claim-narrowings
with severity kept (C1-F7 glossary half miscited; C3-F4 naming prior art; C5-F9 Prosperity half
struck; C7-F3 wording; C6-F2 "byte-identical" claim falsified — the falsified half became C6-M1),
and citation-precision notes (C2-F3 :301→:298; C3-F7 :452→:455/458; C6-F6 :15→:11).
Sharpens: C2-F3 (+ledger self-falsification), C4-F9 (P2→P1, absorbs C4-M1), C7-F2 (+ED-830
non-propagation, 3-way bucket disagreement).
Overturn: C6-F5 — the workbench m1_dice_sigma_core imports are an explicit in-line ED-1085
dev-tooling exception (`workbench/presets.py:18`), not a contradiction; C6-U4 falls with it.

### 1.3 Confirmed register (post-funnel, deduped)

| Cluster | P1 | P2 | P3 | Total |
|---|---|---|---|---|
| C1 | 5 (F1,F3,F4,F5,F6) | 4 (F2,F7,F10,F11) | 3 (F8,F9,M1) | 12 |
| C2 | 1 (F3) | 6 (F1,F2,F4,F5,F6,M1) | 4 (F7,F8,F9,F10) | 11 |
| C3 | 1 (F1) | 8 (F2,F3,F4,F5,F6,F7,F10,M1) | 2 (F8,F9) | 11 |
| C4 | 5 (F2,F3,F5,F9,F10) | 8 (F1,F4,F6,F7,F8,F11,F12,M2) | 3 (F13,F14,F15) | 16 |
| C5 | 2 (F1,F2) | 6 (F3,F4,F5,F6,F7,M2) | 6 (F8,F9,F10,F11,F12,F13) | 14 |
| C6 | 1 (M1) | 3 (F1,F2,F3) | 5 (F4,F6,F7,F8,M2) | 9 |
| C7 | 3 (F1,F2,F6) | 4 (F3,F4,F5,M1) | 2 (F7,F8) | 9 |
| **Total confirmed** | **18** | **39** | **25** | **82** |

Dedupes applied: C3-M2 = C7-F2 (Coherence unregistered/mis-bucketed — counted once at C7, P1);
C4-M1 absorbed into sharpened C4-F9 (Standing range collision); C5-M1 = C1-F11 (Influence
alias collision — counted once at C1).

### 1.4 Unification-option verdicts (docket hygiene)

30 options reviewed: 21 uphold · 9 soften · 0 overturn (C6-U4 mooted by C6-F5's overturn).
Notable: C1-U1 self-contradicted U2/U3 (reconciled in OPT-AV-1); C7-U1 ruled a fork ED-644 holds
open (reframed option-only in OPT-AV-13); C3-U1 silently widened ED-920's scope (flagged in
OPT-AV-9); C3-U3 minted a third name against prior art (corrected to "Political Pool" in
OPT-AV-18); C5-U2's ratify default flagged SE-owned; C4-U4/U8 + C2-U2/U3 lane-feed corrections
applied in the docket.

## 2. Confirmed findings by kind (post-funnel)

| kind | count | | kind | count |
|---|---|---|---|---|
| stale | 21 | | key-binding-gap | 4 |
| collision | 11 | | unregistered | 4 |
| enforcement-gap | 10 | | dead | 3 |
| export-drift | 3 | | synonym | 3 |
| orphan | 2 | | other (incl. 9 census corrections + crosswalk/taxonomy) | 21 |

## 3. Confirmed findings by calibration (post-funnel)

| | C1 | C2 | C3 | C4 | C5 | C6 | C7 | Total |
|---|---|---|---|---|---|---|---|---|
| NEW | 7 | 10 | 7 | 9 | 13 | 7 | 5 | **58** |
| KNOWN-TRACKED | 4 | 1 | 1 | 6 | 1 | 1 | 4 | **18** |
| KNOWN-UNTRACKED | 1 | 0 | 3 | 1 | 0 | 1 | 0 | **6** |

## 4. Census stats

- **88 rows**, 0 duplicates (verified programmatically at merge), 6 clusters (C1:14 · C2:22 · C3:8
  · C4:14 · C5:12+Mandate · C6:18); no C7 rows by design.
- Statuses as filed: **46 COHERENT · 21 DRIFTED · 10 UNREGISTERED-LOAD-BEARING · 5 ORPHANED ·
  4 AMBIGUOUS · 2 DEAD**.
- Post-audit status corrections (see report §4): Agility ORPHANED→live-consumer; Renown
  ORPHANED→defined (cap open); Concentration AMBIGUOUS→coherent (mis-citation); STAMINA_REF
  DEAD→live-unported; Resonant Style defining-surface miscited; settlement-weight inputs
  AMBIGUOUS→contract-under-registration. Adjusted picture: **~44 COHERENT-or-better, and the
  AMBIGUOUS class shrinks from 4 to 2** (Will/Spirit primacy; Piety Track family).
- Validation spot-check: **9/10 pass, 1 fail** (Contest Track Starting Position cited
  `modes.py:5-6`; real definitions at `:450-451` — corrected via C6-F7, which also caught the
  Readiness-constants citation).

## 5. Coverage notes (inherited from finders + merge; not re-swept)

- **F-GODOT finder failure + same-day backfill (disclosed, not silent):** the F-GODOT finder
  failed structured-output in the workflow run, so the census merge and the C6 dossier ran on
  6 finder inventories (C6 read the Godot surfaces directly regardless — its RESIST/exporter
  findings stand). Backfilled standalone same-day as `01_workings/finder_F-GODOT.json` (42 items,
  10 findings). **The backfill's findings did NOT pass the critic funnel** and are excluded from
  the §1.3 confirmed register (82): 4 duplicate confirmed C6 rows (C6-M1/M2/F2/F3), **6 are
  NEW-uncritiqued** — sharpest: F-GODOT-05 (P2, `tradition_resource.gd` + `german.tres` implement
  the 7-channel tradition-weight model Jordan REMOVED from the oracle 2026-06-29 while the .gd
  header claims "routing is complete"), F-GODOT-06 (P2, three Phase-B6-retired weapon fields
  carried), F-GODOT-07 (P2, weapon `.tres` data drift: pre-U0 units, both `reach_adj` values wrong
  vs oracle), F-GODOT-08/-10 (P3), and F-GODOT-09 (P3, a *correction* to C6 §3: `strike_module.gd:74-75`
  already inlines OW_MAX/OW_Z and `:135` hardcodes PER_DIE[7], making the exported `tn_standard`
  dead-in-port). These route with OPT-AV-15's re-export/port-annotation work (feeds PC/GO).
- **Not swept:** module_contracts `doc: null` modules (F-C coverage note; ED-1051 territory);
  `sim/thread/*`, `sim/world/*` (F-SIM); fieldwork/npc-arc tables beyond cross-references
  (F-DESIGN). Any quantity all 6 finders missed is not in the census — residual risk inherited
  from the finder stage.
- **Excluded by scope (named, not silently dropped):** non-quantity hygiene findings (broken
  board_game/factions indexes, patch_history pointers F-PARAMS-08, board_game_misc stub
  F-PARAMS-10, co-file staleness F-DESIGN-7, FIX-01/02/13 tooling splits) — routed to the docket's
  hygiene batch instead of census rows; resolver/procedure specs (Domain Action δ/margin,
  PP-249 Overwhelming rule — the latter captured under Degree Thresholds); FIX-14's PW/NPE/TK
  acronyms (no defining surface anywhere — would violate cardinal rule a).
- **Critic-surfaced coverage gaps in the dossiers themselves:** C3 never consulted the existing
  naming-collision lane (mechanical_terms_index / collision_registry / silo_overlap_matrix /
  name_collision_database) its own sibling census cites; C2 never inspected
  mass_battle_v30.md's wound-penalty carrier; C7 scoped itself to 8 surfaces and missed the seven
  zero-consumer registries (C7-M1); C1's headline percentages for A17/A18 (via C7) lack per-item
  citations — flagged as seed-only in the extension §3.
- **Conformance across dossiers:** no build-state-as-verdict violations found in any cluster (C1-F8
  and C6-F4 *correct* upstream build-state conflations); rule-(c) violations found and fixed in
  calibration (C1-F3/F9, C7-F1/F8); one rule-(e) violation found and reframed (C7-U1); lane-feed
  under-scoping corrected on 6 options.
