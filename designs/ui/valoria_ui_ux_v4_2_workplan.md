# VALORIA — UI/UX v4.1 REPAIR WORKPLAN

**Date:** 2026-04-16
**Source audit:** `designs/ui/valoria_ui_ux_v4_1_max_audit.md` (69 findings, 20 P1 / 37 P2 / 12 P3)
**Target:** `designs/ui/valoria_ui_ux_v4_2.md` (replacement canonical document)
**Status:** WORKPLAN — awaiting Jordan's approval of sequencing and finding accepts/rejects before execution begins

---

## §0 — EXECUTION PRINCIPLES

**Principle 1 — Dependency before severity.** F-15 (delete CD track) and F-16 (delete Taint track) must precede F-58 (Part 14 index rewrite) because the index rows cite the invented tracks. Dependency chains are specified per stage below.

**Principle 2 — Canon-compliance first.** Canon breaches (F-15, F-16, F-55) resolve before any other changes. These are active contamination of the Godot reference; fixing them unblocks downstream work without prejudice.

**Principle 3 — One stage = one commit.** Each stage produces a commit with scoped changes, passing `h.safe_commit()` and CI. No cross-stage mixing.

**Principle 4 — Defer editorial authorship.** Work items flagged `[EDITORIAL]` require Jordan's creative authorship and do not proceed without explicit delivery (e.g., F-68's 22 cutscene trigger enumeration depends on arc_register content; the *mechanical* enumeration can be done mechanically, but trigger *naming* may require editorial pass).

**Principle 5 — F-69 Option B first.** The status-line correction is a single-line change that honestly describes the document's dependency on v4 and unblocks all subsequent work without forcing full restatement. This is Stage 1.

---

## §1 — STAGE DEPENDENCY MAP

```
Stage 1 — Honesty fix (F-69 Option B)                    [no dependencies]
   │
   ▼
Stage 2 — Canon breach deletions (F-15, F-16, F-55, F-58) [depends on 1]
   │
   ▼
Stage 3 — Threshold corrections (F-17, F-26, F-56, F-59, F-67) [depends on 2]
   │
   ▼
Stage 4 — Integration proposal H-items (F-7, F-11, F-32, F-33, F-36)  [depends on 2]
   │
   ▼
Stage 5 — Missing UI surfaces — Personal scale (F-1, F-2, F-5, F-8, F-12, F-13, F-19, F-20) [depends on 3, 4]
   │
   ▼
Stage 6 — Missing UI surfaces — Settlement / Faction (F-23, F-24, F-25, F-27, F-29, F-31, F-34, F-35, F-52, F-54) [depends on 3, 4]
   │
   ▼
Stage 7 — Missing UI surfaces — Thread / Mass / Cross-scale (F-3, F-6, F-14, F-18, F-21, F-22, F-38, F-44, F-45, F-47) [depends on 3, 4]
   │
   ▼
Stage 8 — Oath II compliance — per-action cost previews (F-4, F-28, F-47, F-50, F-51, F-53) [depends on 4, 5, 6]
   │
   ▼
Stage 9 — Appendix E engineering depth (F-61, F-62, F-64, F-65) [independent of 5–8]
   │
   ▼
Stage 10 — Resolved Items Index rewrite (F-58, F-59, F-60) [depends on 2, 3]
   │
   ▼
Stage 11 — Spec autonomy remediation — section restatement (F-68, F-69 Option A) [depends on 1–10]
   │
   ▼
Stage 12 — P3 enrichment pass (F-14, F-30, F-37, F-41, F-46, F-49, F-57, F-63, F-66) [final]
   │
   ▼
Stage 13 — v4.2 publication
```

Stages 1–3 are **unblocking** — they remove contamination and inconsistency without adding content. Stages 4–8 are **content additions** — UI surfaces for mechanics that have spec in v30 docs but no surface in v4.1. Stage 9 is **engineering depth**. Stages 10–12 are **cleanup and enrichment**. Stage 13 is publication.

---

## §2 — STAGE DETAIL

### Stage 1 — Honesty fix (F-69 Option B)

**Scope:** Change the status-line claim on v4.1 from "CANONICAL — approved for development reference" to an honest description of the document's current state.

**Work items:**

| Item | File | Change | Validation |
|---|---|---|---|
| 1.1 | `designs/ui/valoria_ui_ux_v4_1.md` line 5 | Status: `CANONICAL` → `CANONICAL — structural supplement to v4. v4 remains authoritative for content-level UI specification until incremental restatement completes. Spec-autonomy target: v4.2+` | Grep confirms new status line; diff ≤ 3 lines |
| 1.2 | `canon/editorial_ledger.yaml` | New entry: ED-637 (F-69 recorded) | next_id bumped to 602 |

**Acceptance gate:** Jordan confirms Option B (status line change) over Option A (full immediate restatement).

**Blocks:** all subsequent stages (they need honest baseline).

**Commit message:**
```
[DOC] ui_ux_v4_1 honest status line (F-69 Option B)

- Status line now acknowledges v4 dependency explicitly
- ED-637 records spec-autonomy pattern for v4.2 remediation
- No mechanical change
```

---

### Stage 2 — Canon breach deletions

**Scope:** Remove the three canon-contamination items from v4.1. Each is a mechanical track or propagation rule that contradicts canonical source.

**Work items:**

| Item | Finding | File + Section | Change | Canonical source |
|---|---|---|---|---|
| 2.1 | F-15 | `valoria_ui_ux_v4_1.md` §9.8 (CD accumulation) | Delete §9.8 entirely | `threadwork_v30.md` §8.1 (Taint/CD struck from canon) |
| 2.2 | F-16 | `valoria_ui_ux_v4_1.md` §9.7 | Delete "Taint distinguished from Coherence" block (lines 846–848). Relocate "Beliefs show transformation-candidates ghosted" effect to Coherence ≤ 3 / ≤ 2 per threadwork §3.3 | `threadwork_v30.md` §3.4, §8.1 |
| 2.3 | F-16 (cont) | `valoria_ui_ux_v4_1.md` §11.3 character sheet | Remove `Taint (separate from Coherence per §9.7)` line; remove "No Coherence, no Taint, no TS field" mention of Taint | `threadwork_v30.md` §3.4 |
| 2.4 | F-16 (cont) | `valoria_ui_ux_v4_1.md` §10.2 | Delete "Taint track does not apply" line (Threadcut beings) | N/A — Taint removed globally |
| 2.5 | F-55 | `valoria_ui_ux_v4_1.md` §9.9 | Rewrite "Strain auto-accumulates per P-12 Patch O (+1 strain/season on Close Knots at Taint 4–6)" per canonical TS-state table from `npc_behavior_v30.md` §5.0b. Color-code graph edges by TS state, not Taint | `npc_behavior_v30.md` §5.0b |
| 2.6 | F-58 | `valoria_ui_ux_v4_1.md` Part 14 rows 1204–1205 | Delete row 1204 (P-10 falsely resolved). Rewrite row 1205 (P-11): cite §9.5 co-movement panel, not §9.8 | N/A — derived |
| 2.7 | Register | `canon/editorial_ledger.yaml` | Entries: ED-638 (F-15), ED-639 (F-16), ED-640 (F-55), ED-641 (F-58) | — |
| 2.8 | Register | `references/file_index_summary.md` | Mark ui_ux as propagation-pending until Stage 13 | — |

**Acceptance gate:** Canon-guard CI pass confirms no Taint/CD references remain in v4.1.

**Blocks:** Stages 3, 4, 5, 6, 7, 10.

**Commit message:**
```
[FIX] v4_1 canon breaches — delete CD / Taint / P-10-11 index rows

- F-15: §9.8 CD track (contradicts threadwork §8.1 — CD struck)
- F-16: Taint references across §9.7, §10.2, §11.3 (threadwork §3.4)
- F-55: Knot propagation rewritten per npc_behavior §5.0b TS-state table
- F-58: Part 14 rows 1204–1205 revised (P-10 falsely resolved; P-11 cited wrong section)
- ED-638 through ED-641 recorded
```

---

### Stage 3 — Threshold corrections

**Scope:** Numerical/threshold errors verified against canonical sources during re-test.

**Work items:**

| Item | Finding | File + Section | Change | Source |
|---|---|---|---|---|
| 3.1 | F-17 | `valoria_ui_ux_v4_1.md` §13.7.3 line 1138 | Change "Coherence ≤ 5" to "Coherence ≤ 7" (covers full Dissonant band) | `threadwork_v30.md` §3.3 |
| 3.2 | F-26 | `valoria_ui_ux_v4_1.md` §8.4 | Split Bypass rule: non-Fortress `Military > Defense + 2`; Fortress `Military > Defense + 3` | `settlement_layer_v30.md` §5.1 lines 237, 241 |
| 3.3 | F-56 | `valoria_ui_ux_v4_1.md` §9.7 TS 70+ row | Split into TS 70–89 (−1 MS/session) and TS 90+ (−1 MS/scene) | `threadwork_v30.md` PP-197 |
| 3.4 | F-59 | `valoria_ui_ux_v4_1.md` Part 14 UI-03 | Update threshold reference from Coherence ≤ 5 to ≤ 7 to align with 3.1 | Derived from 3.1 |
| 3.5 | F-67 | `valoria_ui_ux_v4_1.md` §9.4 | Rename three-axis first axis from "Scale" to "Breadth" | `threadwork_v30.md` §2.4 (PP-622/PP-623 rename) |
| 3.6 | Register | `canon/editorial_ledger.yaml` | Entries: ED-642 (F-17), ED-643 (F-26), ED-644 (F-56), ED-645 (F-67) | — |

**Acceptance gate:** Numeric grep confirms all threshold values match canon sources.

**Blocks:** Stage 5, 6, 7 (threshold-correct UI surfaces).

**Commit message:**
```
[FIX] v4_1 threshold corrections against canonical v30 sources

- F-17: Coherence ≤ 5 → ≤ 7 (full Dissonant band per threadwork §3.3)
- F-26: Bypass rule split — non-Fortress +2, Fortress +3 (settlement_layer §5.1)
- F-56: TS 70+ row split — 70–89 vs 90+ (threadwork PP-197)
- F-59: UI-03 threshold aligned with §13.7.3 repair
- F-67: Three-axis "Scale" → "Breadth" (threadwork §2.4 post-PP-622)
- ED-642 through ED-645 recorded
```

---

### Stage 4 — Integration proposal H-items

**Scope:** Absorb integration_proposal's five high-value recommendations. Each converts a Personal-scale mechanic into Faction-scale consequence with Godot-ready UI specification.

**Work items:**

| Item | Finding | File + Section | Change | Dep source |
|---|---|---|---|---|
| 4.1 | F-7 | `valoria_ui_ux_v4_1.md` §5.3 | Rewrite 8-row table as 7-gate Dialogue Lattice taxonomy (Attribute, Evidence, Belief, Certainty, History, Disposition, TS). Add visibility-rules subsection (visible-locked vs hidden, hint text). Integrate existing Conviction-lock / Framework-aligned rows as gate-type variants | `investigation_systems_proposal_2026-04-15.md` §Gate Types |
| 4.2 | F-11 | `valoria_ui_ux_v4_1.md` §6.1 Step 2 | Add Style Decision UI: 4 plain-language buttons (Cite the record / Show the future / Raise the doubt / Anchor the fear). Appraise result surfaces recommendation | `integration_proposal_2026-04-15.md` Part 9 |
| 4.3 | F-32 | `valoria_ui_ux_v4_1.md` §9.4 and §11.1 | Add Domain Echo Reference Table as pre-commit UI in Thread panel (§9.4) and Domain Action panel (§11.1). Table content per integration_proposal Part 8 (13 rows). Stature modifier visible | `integration_proposal_2026-04-15.md` Part 8 |
| 4.4 | F-33 | `valoria_ui_ux_v4_1.md` §6.2 | Add Parliamentary Intent scene action for Standing 3+ characters. Binds Finding to next Parliamentary vote; +1D Corroboration appears on next Senator card | `integration_proposal_2026-04-15.md` Gap 3 |
| 4.5 | F-36 | `valoria_ui_ux_v4_1.md` new §11.1c "Independent Actor progression" | Panel shows current Stage (1–5) + requirements for next stage. Cutscene tier per Stage-up | `settlement_layer_v30.md` §6.2 + `player_agency_v30.md` §5.4 |
| 4.6 | Register | `canon/editorial_ledger.yaml` | Entries: ED-646 (F-7), ED-647 (F-11), ED-648 (F-32), ED-649 (F-33), ED-650 (F-36) | — |

**Acceptance gate:** integration_proposal H-1 through H-6 recommendations cross-referenced; each has a v4.1 repair cited.

**Blocks:** Stage 5, 8 (content-surface additions require taxonomy).

**Commit message:**
```
[FEAT] v4_1 integration_proposal H-item absorption

- F-7: §5.3 Dialogue Lattice 7-gate taxonomy with visibility rules
- F-11: §6.1 Contest Style Decision UI (4 plain-language buttons)
- F-32: Domain Echo Reference Table pre-commit UI in §9.4 and §11.1
- F-33: §6.2 Parliamentary Intent for Standing 3+
- F-36: §11.1c Independent Actor Stage 1–5 progression panel
- ED-646 through ED-650 recorded
```

---

### Stage 5 — Missing UI surfaces — Personal scale

**Scope:** UI surfaces for Personal-scale mechanics that have spec in v30 docs but no surface in v4.1.

**Work items:**

| Item | Finding | Section | Change | Dep source |
|---|---|---|---|---|
| 5.1 | F-1 | §1.2 Phase 1a | Fork flow: Operative/Agent = receive-and-dismiss; Counselor+ = Negotiate button → Private Negotiation contest + Priority Stack Adjustment visualization + leader portrait scar on Overwhelming | `integration_proposal` Gap 1 + `player_agency_v30` §5 |
| 5.2 | F-2 | §2.5 Slate | Add one-line companion opinion text under the tag on each companion-commented entry | `companion_specification_v30` §4.4 |
| 5.3 | F-5 | §4.4 | Multi-territory Exposure strip in left panel; collapsed by default to current territory; expand-on-click; season-reset animation at Phase 0 | `fieldwork_v30` §6.2 |
| 5.4 | F-8 | §5.3 | [SINCERE]/[INSTRUMENTAL] tagging row type + inline Spirit roll animation on click. Belief-gated rows auto-tag [SINCERE] with ✦ mark | `fieldwork_v30` §5.3 + `investigation_proposal` §Sincerity Gate Integration |
| 5.5 | F-12 | §7.5 | Contested-pool manoeuvre sub-panel: Feint dice-commit slider (min 3); Rescue eligibility check on hover; Disarm/Tie Up/Retrieve/Establish Distance/Escape contested-pool previews | `combat_v30` §4 |
| 5.6 | F-13 | §7.6 | Specify 5-panel Death Cascade animated sequence: Knot rupture → Slate entries added → faction Stability tick → Exposure strip → Conviction prompt. Each 0.8–1.2s | `combat_v30` §13.3 |
| 5.7 | F-19 | §9.7 Coherence 0 row | Replace "Cutscene fires — TS-branched outcome" with Rendering Crisis arc: Priority 0 Slate entry, season counter, Anchoring Scenes progress (0/3), Bonds resolution roll at Accounting. PP-206 TS 30–31 warning modal | `threadwork_v30` §3.7 + PP-194 + PP-206 |
| 5.8 | F-20 | §11.5 | Separate Companion Connection (Disp +5) from Knot formation (TS ≥ 30 both parties). Add "Knot candidate" chip at Disp +5; Knot Formation action opens only if TS gate met | `fieldwork_v30` §5.6 + `npc_behavior_v30` §6.3 |
| 5.9 | Register | `canon/editorial_ledger.yaml` | Entries: ED-651 through ED-658 | — |

**Blocks:** Stage 8 (Oath II preview depends on these surfaces existing).

**Commit message:**
```
[FEAT] v4_1 Personal-scale UI surfaces for v30 mechanics

- F-1: Phase 1a Counselor+ Duty negotiation fork
- F-2: Slate companion opinion text
- F-5: Multi-territory Exposure strip
- F-8: Sincerity Gate row type + roll animation
- F-12: Contested-pool manoeuvre sub-panels
- F-13: 5-panel Death Cascade animation sequence
- F-19: Rendering Crisis arc UI (replaces single cutscene)
- F-20: Companion Connection / Knot formation gate separation
- ED-651 through ED-658 recorded
```

---

### Stage 6 — Missing UI surfaces — Settlement / Faction

**Scope:** UI surfaces for Settlement- and Faction-scale mechanics.

**Work items:**

| Item | Finding | Section | Change | Dep source |
|---|---|---|---|---|
| 6.1 | F-23 | §11.2 | Governor Panel spec: settlement stat block (P/D/O with caps); 4 action buttons with Ob + pool preview; confirm-commit modal with degree bands | `settlement_layer_v30` §3.2 |
| 6.2 | F-24 | §3.3 | Subnational management strip in province panel: governor per settlement; Grant/Revoke affordance (Counselor+ only); Order/Disposition cost modal on revoke | `settlement_layer_v30` §3.3 |
| 6.3 | F-25 | §2.5 Slate entry format | Add settlement prefix `[S-nnn Name]` + event-type icon. Settlement anchor clickable | `settlement_layer_v30` §4.1 |
| 6.4 | F-27 | §2.6 companion strip | Phase 1c assignment radio per governor-companion: Social / Governance. Opportunity cost on hover | `companion_specification_v30` §4.1 |
| 6.5 | F-29 | §11.1 | Enumerate Hand Panel card face fields: name (faction-typographed), pool attribute + stat, Ob hint, cooldown/unlock, Casus Belli target. Hover = full text | `board_game_v30` card plays |
| 6.6 | F-31 | §1.2 Phase 3 Cascade | Per-step dismissal shows "Resolved immediately" vs "Queued to next Accounting"; Cascade Depth Cap of 3 enforced visually | `board_game_v30` Cascade Depth Cap |
| 6.7 | F-34 | §6.5 Ratification | Post-win Obligation naming modal: winner types/selects commitment. Settlement-targeted Obligations per peninsular_strain C-08 selectable. Bound Obligation appears as pinned clock | `social_contest_v30` §6.1 + `peninsular_strain_v1` C-08 |
| 6.8 | F-35 | §11.1b new subsection "Leadership" | Standing 4+: "Challenge Leadership" action in Hand Panel footer. Standing 5 on leader removal: Priority 0 Slate entry offering leadership | `player_agency_v30` §5.2 |
| 6.9 | F-52 | §2.1 visibility table | Add PI row: visible at Counselor+ in Parliament-participating factions (Crown/Hafenmark/Church/Guilds/Löwenritter/RM). Tooltip: "Parliament Integrity — N/20. Auto-resolves at 20." | `clock_registry_v30` §Shared Clocks |
| 6.10 | F-54 | §2.1 visibility + §11.3 | Generational Shift visible from Year 8. Character sheet shows age penalty. NPC sheets show succession-candidate arrow at Threshold 4+ | `settlement_layer_v30` §7.2 |
| 6.11 | Register | `canon/editorial_ledger.yaml` | Entries: ED-659 through ED-668 | — |

**Blocks:** Stage 8 (preview requires these panels exist).

**Commit message:**
```
[FEAT] v4_1 Settlement/Faction UI surfaces for v30 mechanics

- F-23: Governor Panel stat block + action Ob/pool preview
- F-24: Subnational management Grant/Revoke flow in province panel
- F-25: Settlement-prefixed Slate entries with event icons
- F-27: Companion-governor Social/Governance assignment radio
- F-29: Hand Panel card face field enumeration
- F-31: Cascade Depth Cap immediate-vs-queued display
- F-34: Obligation naming modal post-Contest
- F-35: Leadership Challenge action (Standing 4+)
- F-52: PI clock visibility at Counselor+ Parliament factions
- F-54: Generational Shift clock + character-sheet age penalty
- ED-659 through ED-668 recorded
```

---

### Stage 7 — Missing UI surfaces — Thread / Mass / Cross-scale

**Scope:** Thread-system UI, Mass Battle UI, and cross-scale transition surfaces.

**Work items:**

| Item | Finding | Section | Change | Dep source |
|---|---|---|---|---|
| 7.1 | F-3 | §3.4 location cards | Time-of-day strip per location card; NPC time-cue line; grayed/returns-at hint when NPC absent | `investigation_proposal` §Temporal Dimension |
| 7.2 | F-6 | §4.6 | Specify persistent Case Board: nodes per Evidence, connections drawn on Reconstruct, auto-arrange + player-drag, synthesis-branch target regions. Persistent across seasons. Access via `J` tab | `investigation_proposal` §Case Board |
| 7.3 | F-14 | §9.3 | Pre-Leap Diagnosis preview panel: target configuration properties + three-axis Ob estimate. Distinct from commit modal | `threadwork_v30` §2.2 + §2.3 |
| 7.4 | F-18 | §9.4 | Residue inventory row in Thread panel: token icons with potency rating; click adds to pool with volatility warning. Hidden if none held | `threadwork_v30` §3.4 |
| 7.5 | F-21 | §10.2 | Name the stat Rendering Strain (not "Thread cost accumulating"); cap = Health; De-Actualization cascade at Strain = Health. Observer-dependency rendering per TS table | `threadwork_v30` §6.2, §6.4 |
| 7.6 | F-22 | §13 + §9.6 MS Critical | Rupture = mandatory cutscene list entry (3-minute tier); MS Critical band (19–1) adds per-season Crisis Accounting banner showing MS trajectory + projected Rupture season | `threadwork_v30` §5.3 design note |
| 7.7 | F-38 | §8.2 | Two errors to fix: (a) Phase 4 runs always, renders observer's-perception view per threadwork §2.3 Observation table; (b) General Duel is generic Personal Action at Phase 5 Priority 8, not practitioner-gated | `mass_battle_v30` §A.7 + `scale_transitions_v30` §3.7 |
| 7.8 | F-44 | §13 + §1.4 | Retrospective Zoom In mini-cutscene: fires when player arrives/communicates with territory where major event occurred offscreen. Routes via companion → Knot → messenger → ambient rumor per scale_transitions §4.3 Retrospective | `scale_transitions_v30` §4.3 |
| 7.9 | F-45 | §12.1 | Add 5 missing transition rows: Fieldwork → Contest (Findings as +1D/Finding prep); Fieldwork → Mass Battle (suspension); BG Survey → TTRPG (Fieldwork Offset from degree); Combat → Fieldwork (Exposure codification +1/+2/+3); Contest → Fieldwork (Appraise → Evidence +1 Testimonial) | `scale_transitions_v30` §3.9 |
| 7.10 | F-47 | §7.7 + §9.4 + §11.1 + §6 | Extend Sufficient Scope indicator beyond personal combat to all four gateway points: Combat (§7.7 existing), Thread (§9.4), Domain Action (§11.1), Contest (§6). Show which of 7 conditions apply; companion +1 modifier visible | `scale_transitions_v30` §7 |
| 7.11 | Register | `canon/editorial_ledger.yaml` | Entries: ED-669 through ED-678 | — |

**Blocks:** Stage 8.

**Commit message:**
```
[FEAT] v4_1 Thread/Mass/Cross-scale UI surfaces

- F-3: Location cards time-of-day cues
- F-6: Persistent Case Board (replaces Reconstruct templates alone)
- F-14: Pre-Leap Diagnosis preview
- F-18: Dissolution residue inventory
- F-21: Rendering Strain naming for Threadcut beings
- F-22: Rupture cutscene + Critical-band Crisis Accounting banner
- F-38: Mass battle Phase 4 observer view + General Duel gate correction
- F-44: Retrospective Zoom In mini-cutscene
- F-45: 5 missing transitions added to §12.1 inventory
- F-47: Sufficient Scope indicator extended to all 4 gateways
- ED-669 through ED-678 recorded
```

---

### Stage 8 — Oath II compliance (pre-commit cost previews)

**Scope:** The class of findings where v4.1 asserts an affordance exists but doesn't specify its content. Oath II compliance requires every number the player needs to plan with is visible.

**Work items:**

| Item | Finding | Section | Change | Dep source |
|---|---|---|---|---|
| 8.1 | F-4 | §4.3 | Restate fully (not defer to v4): per-action cost matrix (scene-action / Exposure Success / Exposure Failure / Coherence / MS / Depth cap at TS 0) on button hover | `fieldwork_v30` §4.2 + §6.3 |
| 8.2 | F-28 | §11.1 Domain Action flow | Rewrite: target → Sufficient Scope projection → Institutional challenge check (challenges core institutional authority AND target Mandate ≥ 4) → Uphold/Appease modal with NPC-AI rule transparent → roll → Echo animation | `board_game_v30` PP-189 |
| 8.3 | F-47 | — | Already addressed in 7.10; this item verifies extension is complete across all 4 gateways | — |
| 8.4 | F-50 | §2.1 three-clock summary | CI threshold markers visible: seasons-to-threshold trajectory (passive +1/season → seasons to 65/75/80) | `victory_v30` CI milestones |
| 8.5 | F-51 | §2.1 three-clock summary | IP threshold markers visible: 40 / 60 / 75 / 100 milestones | `clock_registry_v30` + `victory_v30` |
| 8.6 | F-53 | §4.3 per-action preview | Add Calamity Ob modifier row: +1 Ob per MS band below 60 at current Proximity per fieldwork §1 | `fieldwork_v30` §1 + `calamity_radiation_v30` |
| 8.7 | Register | `canon/editorial_ledger.yaml` | Entries: ED-679 through ED-683 | — |

**Blocks:** Stage 10 (index rewrite must reflect final state).

**Commit message:**
```
[FIX] v4_1 Oath II compliance — pre-commit cost previews

- F-4: §4.3 fieldwork per-action cost matrix (full restatement, no v4 defer)
- F-28: §11.1 Uphold/Appease precise trigger (institutional challenge AND Mandate ≥ 4)
- F-50/F-51: CI/IP threshold markers in three-clock summary
- F-53: Calamity Ob modifier in fieldwork per-action preview
- ED-679 through ED-683 recorded
```

---

### Stage 9 — Appendix E engineering depth

**Scope:** Godot-implementation specifics. Can proceed in parallel with Stages 5–7.

**Work items:**

| Item | Finding | Section | Change |
|---|---|---|---|
| 9.1 | F-61 | Appendix E Core resources | Expand from 10 to 17 types: add Belief, Knot, Obligation, Duty, Disposition, Evidence, Clock |
| 9.2 | F-62 | Appendix E Signal bus | Enumerate ≥ 30 signals (currently 3). Full list in work document; minimum: obligation_added/removed, knot_formed/strained/ruptured, coherence_band_crossed, rs_band_crossed, tc/ip/pi_threshold_crossed, belief_scar_added, conviction_strain_added/revised, disposition_changed, exposure_threshold_crossed, season_boundary, phase_transition, scene_action_spent, sufficient_scope_triggered, domain_echo_fired, cutscene_queued |
| 9.3 | F-64 | Appendix E Save system | Expand: resource-ref vs embedded-copy strategy; version header format; migration fallback behavior; expected file size bounds |
| 9.4 | F-65 | Appendix A Input | Capability-gated shortcut remapping rule: remapped bindings persist across capability state; keystroke = no-op until capability acquired; no re-map prompt on capability gain |
| 9.5 | Register | `canon/editorial_ledger.yaml` | Entries: ED-684 through ED-687 |

**Independent of:** Stages 5, 6, 7 (engineering spec depth is orthogonal to UI-surface additions).

**Commit message:**
```
[FEAT] v4_1 Appendix E engineering depth

- F-61: Core resources list expanded (10 → 17)
- F-62: Signal bus enumerated (≥ 30 signals)
- F-64: Save system strategy specified
- F-65: Capability-gated shortcut remapping rule
- ED-684 through ED-687 recorded
```

---

### Stage 10 — Resolved Items Index rewrite

**Scope:** Rewrite Part 14 to reflect all Stage 1–9 corrections. Also handles F-60 split.

**Work items:**

| Item | Finding | Section | Change |
|---|---|---|---|
| 10.1 | F-58 (complete) | Part 14 | Final state of P-10 / P-11 rows after Stages 2 (delete false) and 5–7 (add real) |
| 10.2 | F-59 (complete) | Part 14 UI-03 | Coherence threshold matches Stage 3 §13.7.3 repair |
| 10.3 | F-60 | Part 14 UI-09 | Split compound row: UI-09a (settlement capture side-panel, §8.4); UI-09b (General Duel Zoom In, §8.3) |
| 10.4 | Add rows for new resolutions from Stages 4–8 | Part 14 | UI-16 (Dialogue Lattice 7-gate per F-7), UI-17 (Style Decision UI per F-11), UI-18 (Domain Echo Reference Table per F-32), UI-19 (Parliamentary Intent per F-33), UI-20 (Independent progression per F-36), UI-21 (Sincerity Gate UI per F-8), UI-22 (Case Board per F-6), UI-23 (Rendering Crisis arc per F-19), UI-24 (Sufficient Scope across 4 gateways per F-47) |
| 10.5 | Register | `canon/editorial_ledger.yaml` | Entry ED-688 |

**Blocks:** Stage 13 publication.

**Commit message:**
```
[DOC] v4_1 Part 14 Resolved Items Index rewrite

- F-58: P-10 / P-11 rows reflect Stage 2 deletions + Stage 5–7 additions
- F-59: UI-03 threshold aligned
- F-60: UI-09 split into UI-09a / UI-09b
- UI-16 through UI-24 added for Stages 4–8 resolutions
- ED-688 recorded
```

---

### Stage 11 — Spec autonomy remediation

**Scope:** Restate sections that v4.1 currently defers to v4 so v4.2 becomes a true standalone reference. F-69 Option A (long-term target) realized here.

**Work items:**

| Item | Finding | Section | Change | Work estimate |
|---|---|---|---|---|
| 11.1 | F-68 | §13.2 | Enumerate the 22 mandatory cutscene triggers inline. Incorporate Generational Shift events (F-54), Rupture specification (F-22), Rendering Crisis arc opening (F-19) | Medium — list exists in v4; revision needed |
| 11.2 | F-69 Opt A | §4.3 | Restate action panel contents (partly done in Stage 8 F-4) | Small — Stage 8 delivers most |
| 11.3 | F-69 Opt A | §5.2 | Restate dialogue layout (NPC portrait, dialog text, 5–8 response options, companion commentary placement) | Medium |
| 11.4 | F-69 Opt A | §6.2 | Restate Parliament chamber view (spatial faction arrangement, motion declaration, tally, Veto, Rebuttal) | Medium |
| 11.5 | F-69 Opt A | §7.5 | Restate 12 combat actions list (partly done in Stage 5 F-12 for contested-pool manoeuvres) | Small — Stage 5 delivers most |
| 11.6 | F-69 Opt A | §7.6 | Restate Dice/damage/Fibonacci/Rescue flow (Death Cascade handled in Stage 5 F-13) | Small — Stage 5 delivers most |
| 11.7 | F-69 Opt A | §7.7 | Restate Sufficient Scope indicator (extended in Stage 7 F-47) | Trivial — already extended |
| 11.8 | F-69 Opt A | §8.1 | Restate battle map visual spec (16×10 hex, unit tokens, formation indicators, terrain modifiers) | Medium |
| 11.9 | Status line | Header | Change status from "structural supplement to v4" (Stage 1) to "CANONICAL — standalone Godot development reference" | Trivial |
| 11.10 | Register | `canon/editorial_ledger.yaml` | Entry ED-689 (F-68 complete), ED-690 (F-69 Option A complete) |

**Blocks:** Stage 13 publication.

**Commit message:**
```
[DOC] v4_1 → v4_2 spec autonomy — section restatement

- F-68: §13.2 22 mandatory triggers enumerated inline
- F-69 Opt A: §§4.3, 5.2, 6.2, 7.5, 7.6, 7.7, 8.1 restated inline
- Status line: v4.2 becomes standalone canonical reference
- ED-689 and ED-690 recorded
```

---

### Stage 12 — P3 enrichment

**Scope:** Precision refinements and small-value additions.

**Work items:**

| Item | Finding | Section | Change |
|---|---|---|---|
| 12.1 | F-30 | §2.1 Framework Drift strip | Hover tooltip content: which of 9 drift triggers fired this season, projected result |
| 12.2 | F-37 | §11.1 | Faction collapse → city-state Hand Panel transformation animation (loses Mandate/Military; retains Influence/Wealth/Stability) |
| 12.3 | F-41 | §8.1 | Flanking visualization (hex-side arrows) specified |
| 12.4 | F-46 | scene opening HUD | BG Survey Offset pill shown on next-scene fieldwork in surveyed territory |
| 12.5 | F-49 | §8.3 General Duel | CF wound penalty carry-over visible on mass-battle resume: commander shows +1 Ob pip |
| 12.6 | F-57 | §P0 Oath II Violation Test 3 | Tighten: "Does the UI reveal content at a Depth the character's perception cannot reach via *any* of the gates specified in fieldwork §1?" |
| 12.7 | F-63 | Appendix E | Verify card count against game repo authoritative registry; update manifest |
| 12.8 | F-66 | Appendix A | Expand shortcut list with layer navigation (S = Settlement / Strategic, B = breadcrumb jump, etc.) |
| 12.9 | Register | `canon/editorial_ledger.yaml` | Entries: ED-691 through ED-696 |

**Commit message:**
```
[POLISH] v4_2 P3 enrichment pass

- F-30: Framework Drift tooltip content
- F-37: City-state Hand Panel transformation
- F-41: Flanking hex-side arrows
- F-46: BG Survey Offset pill
- F-49: CF wound penalty carry-over display
- F-57: Oath II Violation Test 3 precision
- F-63: Card manifest verified against game repo
- F-66: Shortcut list expanded
- ED-691 through ED-696 recorded
```

---

### Stage 13 — v4.2 publication

**Scope:** Final validation and canonical registration.

**Work items:**

| Item | Action |
|---|---|
| 13.1 | Rename file: `designs/ui/valoria_ui_ux_v4_1.md` → `designs/ui/valoria_ui_ux_v4_2.md` |
| 13.2 | Update `references/canonical_sources.yaml` ui entry to v4_2 (add SHA pin post-commit) |
| 13.3 | Update `references/file_index_summary.md`: ui_ux_reference entry → v4_2; clear propagation-pending |
| 13.4 | Freshness check: `freshness_gate.py` against all Stage 2–11 canonical source pins |
| 13.5 | Close all Stage 2–12 ED entries in `editorial_ledger.yaml`; archive resolved |
| 13.6 | Session log entry recording v4.2 publication |

**Commit message:**
```
[PUBLISH] valoria_ui_ux v4_1 → v4_2

All 69 audit findings resolved (Stages 1–12).
- 3 canon breaches removed (F-15, F-16, F-55)
- 5 spec-autonomy sections restated
- 22 cutscene triggers enumerated
- Domain Echo Reference Table canonical in UI
- 5 integration_proposal H-items absorbed
- Standalone Godot development reference status achieved
- ED-637 through ED-696 closed
```

---

## §3 — EXECUTION PRECONDITIONS

Before Stage 1 begins, Jordan must confirm:

**3.1 Findings accepts/rejects.** Any of the 69 findings Jordan disputes remove from the workplan. Current assumption: all 69 are accepted as-stated in the audit file (post-corrections applied during re-test).

**3.2 F-69 Option B vs Option A preference.** Workplan assumes Option B in Stage 1 (short-term honesty), Option A in Stage 11 (long-term restatement). If Jordan prefers Option A immediately, Stages 11 and 1 merge, and the rest of the plan shifts right.

**3.3 Stage granularity.** Workplan is 13 stages = 13 commits. If Jordan wants denser commits (e.g., one per finding) or coarser (e.g., all P1 in one commit), restructure.

**3.4 Editorial authorship dependencies.** Two findings require Jordan's creative authorship:
- **F-68** — 22 cutscene trigger enumeration may require arc_register content review
- **F-25** — settlement event icons (7 types) require visual-design authorship, not just spec

Workplan treats these as mechanical-enumerable (what's listed in v30 sources) but Jordan may want editorial pass on them before Stage 7 / 11.

**3.5 Mass battle Godot priority.** F-38 (mass battle Phase 4) and F-39 (per-phase UI spec) are P1 and P2 respectively. If Godot milestone does not include Mass Battle in near term, F-39 can defer to v4.3; F-38 remains in Stage 7 as canon-correctness.

**3.6 Investigation proposal status.** Stages 4 and 7 absorb findings from `investigation_systems_proposal_2026-04-15.md` — status "PROPOSAL — requires approval before integration." Confirm this proposal is approved for v4.2 integration. If not approved, F-6 (Case Board), F-7 (7-gate Dialogue Lattice), F-3 (time-of-day / Drift) all revert to v4.1 treatments.

---

## §4 — WORK TOTALS

| Stage | Items | P1 count | P2 count | P3 count | EDs allocated | Blocking? |
|---|---|---|---|---|---|---|
| 1 | 2 | 1 (F-69) | — | — | ED-637 | Yes, blocks all |
| 2 | 8 | 4 | — | — | ED-638–605 | Yes, blocks 3–7 |
| 3 | 6 | 2 | 3 | — | ED-642–609 | Yes, blocks 5–7 |
| 4 | 6 | 5 | — | — | ED-646–614 | Yes, blocks 5, 8 |
| 5 | 9 | 5 | 3 | — | ED-651–622 | Partial blocker 8 |
| 6 | 11 | 3 | 7 | — | ED-659–632 | Partial blocker 8 |
| 7 | 11 | 4 | 6 | — | ED-669–642 | Partial blocker 8 |
| 8 | 7 | 1 | 5 | — | ED-679–647 | Yes, blocks 10 |
| 9 | 5 | 2 | 2 | — | ED-684–651 | Independent |
| 10 | 5 | 1 | 2 | 1 | ED-688 | Yes, blocks 13 |
| 11 | 10 | 2 | 6 | — | ED-689–654 | Yes, blocks 13 |
| 12 | 9 | — | — | 8 | ED-691–660 | Independent |
| 13 | 6 | — | — | — | — | — |
| **Total** | **95** | **30** | **34** | **9** | **ED-637–660** | — |

P-count reflects workplan *items*, which exceeds the 69 findings because several findings split across multiple work items (e.g., F-16 across 2.2, 2.3, 2.4; F-47 across 7.10 and 8.3). All 69 findings are covered.

---

## §5 — PROPAGATION NOTES

Changes to `valoria_ui_ux_v4_1.md` propagate to:

| File | Trigger | Action |
|---|---|---|
| `references/canonical_sources.yaml` | File rename in Stage 13 | Update ui entry, SHA pin |
| `references/file_index_summary.md` | Any commit | Update propagation-pending count |
| `canon/editorial_ledger.yaml` | Every stage | Add entries per stage table |
| `canon/editorial_ledger_summary.yaml` | Stage 13 close | Update P1 count |
| `session_log_current.md` | Every session | Record stage progress |

No v30 design file changes required — v4.2 consumes canonical v30 sources without modifying them. This is a UI-layer-only update.

---

## §6 — RISK ITEMS

**R-1 [High]** — F-68 enumeration of 22 cutscene triggers may expose that the v4 list is itself outdated (e.g., doesn't include settlement-scale events from settlement_layer_v30). If v4's list is stale, Stage 11 doubles in scope.

**R-2 [Medium]** — F-7 7-gate Dialogue Lattice may require `[EDITORIAL]`-tier content: the seven gate types exist mechanically in investigation_proposal, but *utterance content* per gate is per-NPC editorial authorship. Stage 4 delivers the mechanical taxonomy; content-authorship is out of scope.

**R-3 [Medium]** — F-32 Domain Echo Reference Table (integration_proposal Part 8) contains 13 action-type rows. Verifying each row against canonical v30 sources (combat §13.1, threadwork §5.2, social_contest §6, fieldwork §2.5, settlement_layer §3.2) may reveal inconsistencies that require v30-side reconciliation, not just v4.2-side absorption. This is integration_proposal's B-1 blocker explicitly.

**R-4 [Low]** — F-19 Rendering Crisis arc requires new Priority 0 Slate entry type (not currently enumerated in player_agency §4.2 Step 1). Either player_agency needs an update, or the workplan treats this arc as a special-case entry not requiring player_agency revision.

**R-5 [Low]** — F-52 PI clock visibility condition ("Parliament-participating factions") lists 6 factions, but faction_layer_v30 may define Parliament participation differently. Verify before Stage 6.

---

## §7 — ACCEPTANCE GATE

Jordan confirms one of:

- **A.** Accept workplan as-stated. Begin Stage 1. All 69 findings, all 13 stages, 30 P1 items, 34 P2, 9 P3.
- **B.** Accept with modifications. Specify which findings to reject, which stages to restructure, which risks to accept/mitigate.
- **C.** Partial accept: execute Stages 1–3 (canon correctness) and halt before Stage 4. This delivers a clean v4.1 baseline without adding content, pending further design discussion on integration_proposal absorption (Stage 4).
- **D.** Reject workplan. Audit findings remain recorded; no action taken.

Default assumption if no response: workplan holds; no execution begins.

---

*End of workplan.*
