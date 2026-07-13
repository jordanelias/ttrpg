# Handoff — SE (Settlements)

Lane-scoped continuity for the `SE` (settlements) lane, per the `ED-<LANE>-NNNN` namespace
(`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md` is the
index; see it for cross-lane/global items.

No active work tracked in this lane as of the 2026-07-02 HANDOFF split. Canonical head:
`designs/territory/settlement_layer_v30.md` (+ `settlement_adjacency_v30.md`,
`territory_temperaments_v30.md`, `designs/world/geography_v30.md`).

## Pending

- **Comparative-governance-research docket round 2 (filed + partly executed 2026-07-09).**
  `designs/audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md`
  — see `handoffs/HANDOFF_FA.md` for the full docket description (shared report, split by lane).
  Filed as **ED-SE-0018..0044** (see `canon/editorial_ledger.jsonl`; 27 SE-lane items, 7 authored,
  20 open/needs_jordan — the largest single-session SE allocation to date).
  **Authored into `governance_play_redesign_v1.md` / `settlement_layer_v30.md` as PROPOSED text
  (2026-07-09; no sim code — SE still has no player-verb execution code, per the ED-SE-0005
  precedent):**
  - **ED-SE-0018/ED-SE-0019 `governance_play_redesign_v1.md` §1.3a** — Locked Extraction Figures:
    one shared substrate (`assessed_base`), two acquisition triggers — unilateral **Survey**
    (Hideyoshi's *Taikō Kenchi* cadastral survey; composes with `faction_layer_v30` §5.9 Fiscal
    Stance) and negotiated **Encabezamiento** (Cortes of Castile, 1534), the latter opening a
    **fifth Ledger-of-Consequence tag family, Compact** (§1.6).
  - **ED-SE-0020 §1.3b** — Bind the Cells: a new `Keep Order` method (goningumi five-household
    collective liability, Hideyoshi 1597), with a compounding "Cell Revolt" Crisis-card failure
    mode.
  - **ED-SE-0021 `settlement_layer_v30.md` §3.3b** — Za patron-lapse: extends the §3.3a Charter
    machinery with a **patron** field; privileges lapse automatically when the patron's own
    standing falls, no Quo Warranto needed.
  - **ED-SE-0022 `governance_play_redesign_v1.md` §1.1a** — Clerk Capacity: a second, *opaque*
    AP source (Ming-Qing *zhixiàn* thin-bureaucracy model) with a hidden Clerk Corruption counter
    discoverable only via Investigate.
  - **ED-SE-0023 §1.3c** — Ordenanza Ratification: a new `Hold Court` branch for guild
    self-authored rules (Spanish *gremios*), three-way Ratify/Reject/Amend fork that can lock
    caste exclusion into settlement policy.
  - **ED-SE-0024 `settlement_layer_v30.md` §3.3c** — The Seggio Council: a new subnational-faction
    archetype (Naples's *Seggi*) sitting deliberately *outside* the Charter/Quo-Warranto system —
    bespoke non-transferable privileges, inherited/married/seized only.
  **Not authored this session** (queued, see Next actions): the promote-ready-but-unlanded P2/P3
  items (CHN-6, HRE-3, HRE-4, VEN-SE-2, IT-1, HAB-1) and the 20-item SE-lane share of the
  needs_jordan queue.

- **FA/SE historical-precedent research docket (filed 2026-07-08; built out same-day via an
  agonist-antagonist-judge Workflow).**
  `designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md`
  — see `handoffs/HANDOFF_FA.md` for the full docket description (shared report, split by lane).
  Distills into 10 SE-lane mechanical proposals + a citation patch, filed as **ED-SE-0007..0017**
  (see `canon/editorial_ledger.jsonl` for execution notes; remaining `needs_jordan` forks:
  ED-SE-0013 oversight-toolkit venal-appointment variant, ED-SE-0014 Local Interdict, ED-SE-0015
  Plant Colony, ED-SE-0017 optional founder-solidarity bonus).
  **Built same-day (2026-07-08) — all AUTHORED into `settlement_layer_v30.md` as PROPOSED text**
  (no sim code; SE has no player-verb execution code yet, per the ED-SE-0005 precedent):
  - **ED-SE-0007 (SE-1) §1.8a** — the Weberian L/PS derivation-event table (already drafted; the
    report's own #1 priority, unblocking the items below).
  - **ED-SE-0012 (SE-6) §1.8b** — Succession continuity.
  - **ED-SE-0016 (SE-10) §1.8c** — Weight loss as Exit (Hirschman closure).
  - **ED-SE-0010 (SE-4) §3.3a** — Charters/prescription/Quo Warranto.
  - **ED-SE-0008 (SE-2) §4.3a** — Dearth chain + granary.
  - **ED-SE-0009 (SE-3) §4.3b** — Grain routes (closes the open `geography_v30` ED-054/BALANCE-005
    item mechanically).
  - **ED-SE-0011 (SE-5) §5.3** — Entry Terms at control transfer (Confirm Privileges seeds L=3 /
    Impose Administration seeds L=1). **Partially LIVE in sim**: `faction_action.py`'s ED-FA-0013
    conquest-terms fork reads this exact seed value (a dormant, non-serialized
    `Territory.entry_terms_l_seed` proxy pending LPS-1) — the two lanes are reconciled, not
    independently drifting.
  - **ED-SE-0017 (CP-2) §7.1** — Ibn Khaldun *asabiyyah* annotation on the Generational Shift
    clock (core annotation only; the optional founder-solidarity mechanic stays needs_jordan).
  Ratification of the PROPOSED sections tracks ordinary merge review (CLAUDE.md §1, ED-1094) —
  none of these were flagged as held-back exceptions. Sim implementation of SE-2/SE-3/SE-4/SE-6/
  SE-10 (beyond SE-5's dormant proxy) remains a follow-on lane, riding the ED-SE-0001
  `governance_play_redesign` staging where noted in each ledger entry.
- **ED-SE-0005 (RESOLVED 2026-07-08) — pessimist-audit SE verdicts EXECUTED.** The first execution
  of a ratified pessimist-action-audit lane docket (ED-IN-0027). Done: `player_agency_v30 §9` Trade
  PRUNED (folded into Guild-contracts income), Fund-settlement-development MERGED into Develop
  funding, free Sponsor-settlement-event retired into the Debt-bearing `Sponsor`; `settlement_layer_v30`
  §3.2 Administer annotated DISTILL (info→Investigate, maintenance→AP-not-spent; the *physical* fold
  lands when `governance_play_redesign_v1` supersedes §3.2 at OPT-16), §3.3 Grant/Revoke annotated as
  an FA-owned `da.public_governance` Domain Action (single-home = the `domain_actions` doc, ED-FA-0002);
  `governance_play_redesign_v1` (proposal) refined — Investigate reuses the fieldwork Investigation
  resolver, Treat's chit call-in trigger is now specified (Debt tag → Friction card, §1.6/§2.3);
  `module_contracts` settlement_economy SE-side retirement confirmed; a stale `combat_v30` Trade
  pointer fixed. **Residual for OPT-16 (governance-redesign staging):** the physical §3.2 Administer
  removal + the Develop-funding merge land when the redesign is ratified — the decisions are baked in,
  not left silent. No sim work (SE has no player-verb execution code).

- **ED-SE-0002 (open, needs_jordan) — Accord/Order stacking ruling.** Filed 2026-07-05 from the
  ratified edge-playability audit (PR #81, "Ratify all"; finding EP-9): `scale_transitions_v30`
  §5.5 ("do not stack — higher Accord applies") vs `peninsular_strain_v30` §2.7 ("stack
  normally, cap ±1 per source") give opposite answers for player-plus-governor acting on the
  same settlement in one season; Accounting §7 Step 4c resolves neither. Jordan rules which text
  wins; loser gets a supersession marker; Step 4c gains the resolving clause. See
  `designs/audit/2026-07-05-edge-playability-audit/edge_playability_audit_v1.md` §1 EP-9.
  (Sibling lane context: ED-SE-0001, the governance_play_redesign path — filed 2026-07-05 from
  the NERS-audit ratification — composes; the edge audit's ep-31/E9 dual-authority seam notes
  feed that work.)

- **ED-SE-0001 (ratified, work-ordered 2026-07-05; tracking executed 2026-07-07 via ED-SE-0004) —
  Settlement governance-loop redesign tracking.** Filed from the ratified NERS qualitative audit
  (PR #77, post-merge "Ratify all"). Ordered action: track `designs/territory/governance_play_redesign_v1.md`
  staging toward canon ratification so it cannot orphan — the F-1 recurrence guard (C-NERSPESS-4 found
  this ordered update had never been executed). G1 prerequisite already built: `sim/territory/registry.py`
  + tests (per NERS refutation R-5). CURRENT.md's settlement row now carries the proposal pointer
  (OPT-16). Source: `designs/audit/2026-07-04-ners-qualitative-audit/ners_qualitative_audit_v1.md` F-1.

## Decisions

(none logged under this lane split.)

## Next actions

- **D1–D6 all RULED 2026-07-13 (ED-IN-0046/0047)** — `governance_consolidation_v1.md §6` and
  `ners_vsg_reconciliation_v1.md` are both updated with the full ruling record. SE-lane concrete
  effect: §1.3a's D3 gate is cleared (Compact = a recurring `Debt` subtype — E3's subsistence
  floor is the remaining authoring gap); §1.0c (ED-FA-0020, FA-lane but composes with SE) and
  four SE items (Za patron-lapse ED-SE-0021, Ordenanza ED-SE-0023, plus FA's 2.5a) are RATIFIED
  outright — **authoring the ratified text into `governance_play_redesign_v1.md`/
  `settlement_layer_v30.md` as CANONICAL prose is now the concrete next action**, not a decision
  wait. **B1 (faction count) is RULED**: starting count = 4, matching `valoria_political_hierarchy_v30.md`'s
  duchy+Church structure exactly; `ED-FA-0001` resolved.
- **B2 — context gathered 2026-07-13, awaiting Jordan's confirmation, not yet a ruling.** Not really
  a design fork: `valoria_geography_v30.yaml` (the map) has no Goldenfurt at all and still uses the
  old S-006=Lowenskyst-Fortress/S-007=Garrison-Town numbering; `settlement_layer_v30.md`'s own
  settlement table already flipped this (S-006=Goldenfurt/Kronmark, S-007=Lowenskyst Fortress) via a
  migration note at lines 488–489, but the same file's line 912 has a stale reference to the old
  numbering, and the geography YAML was never updated at all. Lean offered: finish the
  already-started fix (line 912 + actually add Goldenfurt to the geography YAML with real
  coordinates/polygon/roads), matching what `settlement_layer_v30.md`'s primary table and all of
  `goldenfurt_slice/` already assume.
- **B12 — a live worldbuilding decision, conflicts with existing Class A canon. Do NOT edit any
  settlement/territory doc for B12 until it lands.** Jordan described a genuine hierarchy expansion
  (Settlement → Territory [multiple settlements] → Province [multiple territories]) that directly
  contradicts `valoria_political_hierarchy_v30.md` (PP-726)'s explicit "Territory = Settlement"
  equivalence — PP-726 currently has no tier between Settlement and Province at all. Two readings
  offered to Jordan (insert a new Territory tier and rework PP-726 §2.1–§2.5 around it, vs. some
  other mapping onto PP-726's existing structure) — see `ners_vsg_reconciliation_v1.md §5` item 4
  for the full finding, including the people-based-faction-power and cross-scale-independence content
  Jordan specified alongside it.
- **Read `designs/architecture/ners_vsg_reconciliation_v1.md` (2026-07-13) before resuming any
  item below.** It cross-reads `governance_consolidation_v1.md`'s D1–D5/E1–E7 decision surface
  against `tools/sim_harness/`'s 19-adapter empirical pass
  (`designs/audit/2026-07-12-pr119-harness-verification/`) and VSG's generator proposal
  (`designs/territory/settlement_generator_v1.md` + `generation_sourcebook_v1.md`), and proposes
  one merged sequence (Phase 0–7). Headline corrections it makes to this list: the promote-ready
  items below now have per-item NERS dispositions (HRE-4/HAB-1/HRE-3/CHN-6 are clean KEEPs ready
  to author; VEN-SE-2/IT-2/IT-1/HAB-4 need a named REFINE first — see the doc's Phase 3); E1
  (port the Π restoring term) cannot land alone, per §3 of the reconciliation doc; a new decision
  D6 (which G606 recall-clock wiring ships) is now open and blocks D5's execution.
- **Land the remaining promote-ready P2/P3 items from the 2026-07-09 docket**: CHN-6 (Gongsuo
  Registration), HRE-3 (Convene the Circle), HRE-4 (Borrow), VEN-SE-2 (Boschi Pubblici
  Requisition), IT-1 + HAB-1 (fold into SE-7's oversight toolkit as a 5-instrument menu per the
  docket's own S-2 synthesis). See STEP 3 §4 sequencing recommendation, and the reconciliation
  doc's Phase 2/3 for the refined per-item dispositions.
- **Author card-deck specs for the 2026-07-09 batch's new triggers** (Cell Revolt, the
  clerk-corruption Intrigue, "Guild seeks Ordenanza sanction," "Patron's Rivals Move") per the
  `governance_play_redesign_v1.md` §2.2 schema — only noted inline at §2.3 so far, not fully
  specced as standalone cards.
- **Implement the SE-1..SE-6/SE-10 PROPOSED sections in sim** — `settlement_layer_v30` §1.8a/b/c,
  §3.3a, §4.3a/b, §5.3 are drafted (see Pending); no sim code exists yet for any of them beyond
  SE-5's dormant `entry_terms_l_seed` proxy. Sequencing recommendation (from the source docket)
  still holds: SE-5/SE-6 (transfer/succession) → SE-2/SE-3 (dearth + grain) → SE-4 riding the
  ED-SE-0001 ratification track.
- **Author the remaining `needs_jordan` forks** (ED-SE-0013/0014/0015/0017's optional mechanic)
  once Jordan rules each.
