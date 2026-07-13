# Handoff — FA (Faction Actions)

Lane-scoped continuity for the `FA` (faction actions) lane, per the `ED-<LANE>-NNNN` namespace
(`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md` is the
index; see it for cross-lane/global items.

No active work tracked in this lane as of the 2026-07-02 HANDOFF split. Canonical heads:
`designs/provincial/faction_canon_v30.md`, `faction_layer_v30.md`, `faction_behavior_v30.md`,
`faction_state_authoring_v30.md` (overview: `designs/factions/faction_systems_overview_v30.md`).

## Pending

- **Comparative-governance-research docket round 2 (filed + partly executed 2026-07-09; a
  22-agent Workflow — 7 civilizations × research→adversarial-verify→distill, Sonnet-tier, then a
  single Opus 4.8 judgment pass).**
  `designs/audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md`
  — Jordan-requested extension of the round-1 docket below, covering Byzantium, feudal/imperial
  China, feudal Japan, the Holy Roman Empire, Venice (Stato da Mar/Terraferma), Renaissance Italy
  outside Venice, and Habsburg Spain, targeting settlement-management and intra-faction
  rank-advancement content specifically. Each research lane was steered off everything round-1 and
  the 2026-06-28 deliberation corpus already mined. The Opus judge pass caught and corrected a
  stale premise several proposals inherited (the "missing Guilds ladder," which `faction_politics_v30`
  §2.5 already authors in full — the actually-flat surface is the Crown Administrative branch,
  §1.1b) and cut 14 of 58 proposals as redundant/pattern-matched/too-vague before curating the
  remaining 44. Filed as **ED-FA-0018..0034** (see `canon/editorial_ledger.jsonl` for each item's
  scope; `needs_jordan` forks: ED-FA-0018 CHN-2 examination pipeline for the Administrative
  branch — the single highest-value open rank decision — plus ED-FA-0027/0028/0029/0030/0031
  BYZ-1/9/7/8, CHN-8-0031, ED-FA-0032/0033 FA-JP3/5, ED-FA-0034 HAB-2).
  **Authored into `faction_politics_v30.md` as PROPOSED text (2026-07-09):**
  - **ED-FA-0019 §1.0b** — Recognition Fork (Confirm/New-Grant), a cross-rank dimension applying
    uniformly across all four primary ladders (Kamakura *honryoando*/*shin'on*).
  - **ED-FA-0020 §1.0c** — Court Attendance + hostage-kin, Standing-4+ absentee-governor dimension
    (*sankin-kōtai*).
  - **ED-FA-0021 §1.0d** — Patron-Sponsored Performance Audit, an optional Standing-6+ toggle on
    the Obligations column that auto-lapses with its patron (Zhang Juzheng's *kaochengfa*).
  - **ED-FA-0022/ED-FA-0023 §2.5a** — Guild-ladder entry/mastership forks, landed together per the
    judged synthesis: guarantor-vs-sole-patron entry (Book of the Eparch) and capital-gated
    Free Mastership vs the examined path (Arte della Lana), both writing durable tags that
    interact with the ladder's existing caste bias.
  **Not authored this session** (queued, see Next actions below): the promote-ready-but-unlanded
  P2/P3 items (HRE-2, HAB-4, IT-2) and the full needs_jordan queue.

- **FA/SE historical-precedent research docket (filed 2026-07-08; built out same-day via an
  agonist-antagonist-judge Workflow).**
  `designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md`
  — an intensive historical/political-science research pass (Jordan-requested) covering fiscal
  sociology, tax farming, moral-economy dearth politics, urban charters, provincial-governor
  oversight, conquest terms, parish-level church-state jurisdiction, frontier colonization,
  succession/regency, and legitimacy theory (Weber/Olson/Hirschman/Ibn Khaldun) — chosen to be
  disjoint from the deliberation-and-procedure research already mined for the SC lane. Distills
  into 9 FA-lane mechanical proposals + a citation-patch batch, filed as **ED-FA-0008..0017**
  (see `canon/editorial_ledger.jsonl` for each item's full scope and execution notes; remaining
  `needs_jordan` forks: ED-FA-0010 coercion/capital muster asymmetry, ED-FA-0013 Sack mechanic
  (part c only, (a)/(b) EXECUTED), ED-FA-0014 Regency interregnum, ED-FA-0015 Protected Tributary,
  ED-FA-0016 Guild embargo).
  **Built same-day (2026-07-08):**
  - **ED-FA-0009 (RESOLVED) — Muster re-grounded** as a fiscal-military purchase in
    `faction_action.py::_try_muster` (W−1 up front, pool = Mil + floor(W/2)).
  - **ED-FA-0012 (RESOLVED) — state-conditioned action-mix**: `faction_take_action` re-weights the
    30/35/20/15 PRIOR vector by Conquest-target/Mil-advantage/undergoverned-share/threat signals
    (all `[SEED]`, RNG-free) before drawing, then renormalizes; degenerates to the original mix in
    a neutral state. Built ahead of the ED-FA-0004 Stratum-B (LPS-1) rewrite this docket originally
    recommended waiting for — a disclosed sequencing deviation, not a silent one; will need
    revisiting when Mandate relocates per-settlement.
  - **ED-FA-0013 (a)/(b) EXECUTED, (c) still needs_jordan** — `_try_conquest` forks Terms
    (Success: Accord −10, seeds settlement `entry_terms_l_seed = 3`, matching the SE-lane's own
    §5.3 Confirm-Privileges value, not this docket's flatter "2") vs Storm (Overwhelming: Accord
    −25, unchanged). Disclosed consequence: `resolve_mass_battle` essentially never yields
    attacker-Overwhelming in practice, so Terms now replaces the old flat −25 for nearly all
    conquests — a game-wide Accord-softening side effect.
  - **ED-FA-0017 (RESOLVED) — all four citation patches** (CP-1 succession split-ratio, CP-3
    parliamentary abstention, CP-4 Casus Belli, CP-5 Crown Initiative modes) landed as
    grounding comments; no numeric values changed.
  - **ED-FA-0008 (still open) — FA-1 Fiscal Stance** drafted into `faction_layer_v30` §5.9 as
    PROPOSED text only; the Treasury-coupling sim implementation is a follow-on lane.
  - **Parliamentary Censure wired into the campaign loop** (the ED-SC-0007 residual item 2): see
    `handoffs/HANDOFF_SC.md` — reuses the existing faction-unique action slot
    (`_try_faction_unique`), so every parliamentary-eligible faction can now propose a Censure.
    Surfaced a genuine cross-lane NEEDS-JORDAN question (Mandate-stacking on a total-victory pass)
    filed as **ED-SC-0015** — see that handoff.
- **ED-FA-0006 (RESOLVED 2026-07-08) — pessimist-audit FA verdicts EXECUTED** (FA-lane follow-up to
  ED-IN-0027). `params/bg/core.md`: Diplomacy-between-players DISTILLED → Treaty §3.3 Ph2; Thread
  Operation single-sourced to the TW lane (Pontifex/Weaver slot-eligibility kept); Spy given its
  missing Failure branch. `faction_layer_v30`: §5.4's five punitive motions reframed as severity
  **tiers of one "Parliamentary Sanction" action** (tier names retained so Sacred-Veto/CB/Guilds-vote/
  §5.6 hooks still resolve; constructive motions untouched); §1.5 Claim Masterless annotated as a
  March/Conquest target-variant. `module_contracts` `domain_actions`: da.* reframed as an outcome-tag
  crosswalk on the existing catalogs (not a standalone module), resolving C-FA-12 — directional
  first-pass mapping recorded, ambiguous bucket boundaries flagged for Jordan (not fabricated).
  **Feeds ED-FA-0002 (below):** the da.* half of that home-doc task is now scoped down to "add the
  per-verb tag column + rule the flagged boundaries," not "author a new system." No sim edits.
  **Decision packet available** for the three boundaries:
  `designs/audit/2026-07-08-pessimist-action-audit/decision_packets/DP-1_FA_da_bucket_boundaries.md`.

- **ED-FA-0002 (open) — author the strategic-turn surface / `domain_actions` home doc.** Filed
  2026-07-05 from the ratified edge-playability audit (PR #81, "Ratify all"; finding EP-2): the
  `da.*` five-type family is a retroactive outcome classifier, not a verb menu; the real verbs
  are fragmented across `params/bg/core.md` (card-hand + Ob table), `params/bg/faction_actions.md`,
  and the faction_layer resolver. One home doc unifies them and flips the `domain_actions`
  doc:null (composes with ED-1051). See the audit report §1 EP-2 / §7 item 5.
- **ED-FA-0003 (open) — BG victory-params re-export.** Filed 2026-07-05 (same batch; finding
  EP-10): `params/bg/victory.md` still carries struck Varfell Path C (VTM=5, PP-663) + pre-PP-663
  VTM/territory co-victory thresholds; `params/board_game.md` index 100% dead links;
  `params/bg/phases.md` Hollow-Victory contradiction + dead victory path cite. Re-derive from
  `victory_v30.md`; an S-1/ED-IN-0007 register-back-propagation exemplar.

## Decisions

(none logged under this lane split.)

## Next actions

- **D1–D6 all RULED 2026-07-13 (ED-IN-0046/0047)** — see `governance_consolidation_v1.md §6` for the
  full record. FA-lane effect: §1.0c Court Attendance (ED-FA-0020) and both §2.5a Guild forks
  (ED-FA-0022/0023) are RATIFIED outright — author into `faction_politics_v30.md` as CANONICAL prose
  next. §1.0d (ED-FA-0021, Kaochengfa) MERGES into the suspicion/recall spine as a modifier, wired as
  cumulative per-Defy-season accrual (D6), **but authoring it requires landing E11 in the same
  pass** — a new symmetric suspicion-*reduction* mechanic (sustained compliance/consistency), per
  Jordan's ruling: "if there is a way to advance suspicion from non-compliance, there must be a way
  to reduce suspicion by over-compliance." `needs_jordan` is now FALSE on ED-FA-0021 — this is an
  authoring task, not a further decision wait.
- **B1 RULED 2026-07-13 (ED-IN-0047)** — starting faction count = 4 (Valorsmark, Hafenmark, Varfell,
  Church of Solmund); `ED-FA-0001` resolved. Emergent factions are explicit and intentional (RM,
  Löwenritter-style post-coup splits, an Altonia-usurper archetype) reusing already-designed
  mechanisms — see `ED-FA-0001`'s ledger entry.
- **B12 is a live, cross-lane worldbuilding decision — do not author faction-tier content assuming
  either reading until it lands.** Jordan described local/provincial/national-scale factions as
  independent tiers (not necessarily nested — a local faction need not belong to a provincial one),
  factions holding *people* rather than territory as their power base, and settlements/territories/
  provinces able to become independent of, or be claimed directly by, a faction from a different
  scale (e.g., a single settlement claimed by a national faction like the Restoration Movement). This
  conflicts with existing Class A canon (`valoria_political_hierarchy_v30.md`'s "Territory =
  Settlement" equivalence) — see `ners_vsg_reconciliation_v1.md §5` item 4 for the full finding and
  the two readings offered to Jordan.
- **Read `designs/architecture/ners_vsg_reconciliation_v1.md` (2026-07-13)** before landing
  HRE-2/HAB-4/IT-2 below — `tools/sim_harness/`'s NERS review found HRE-2 needs an explicit
  acquisition cost added (currently an uncosted 81%-favorable bet, E10), HAB-4 needs a Ministry
  action-economy foundation authored first (E9, Part 7 currently grants no per-Ministry action
  capability), and IT-2's Aspetto ×0.5 clause needs reconciling against all four real
  `faction.Mil` read sites named in the doc (E8) before it ships. The same doc also validated the
  Ascendancy character-power system (Part 40, `designs/audit/2026-07-12-governance-compendium/`)
  as the review's single strongest KEEP — ready to author into canon independent of anything else
  on this list.
- **Resolve ED-FA-0018 (CHN-2 Examination Ladder)** — the single highest-value open rank decision
  from the 2026-07-09 docket: does the Crown Administrative branch (§1.1b, currently the ladder
  system's one genuinely flat sub-office surface) get a non-Skyrim-Eight credentialing pipeline
  (capped pass rates, direct Standing-3 appointment, a "Waiting Laureate Pool")? Recommended yes
  per the docket's own judgment. Decide this before BYZ-1 (next item) — they compose.
- **Land the remaining promote-ready P2/P3 items from the 2026-07-09 docket**: HRE-2 (Chapter
  Capture, faction_politics §1.4d), HAB-4 (Overlapping Consulta, §7.1a), IT-2 (Condotta
  three-phase contract, faction_action.py). See the docket's STEP 3 §4 sequencing recommendation.
- **Take the 2026-07-09 needs_jordan queue to a decision memo** alongside the round-1 leftovers
  below — start with BYZ-1 (Office/Dignity Standing-split) since HAB-2 (Valido) explicitly composes
  with it (§5 items 1-3 of the new docket).
- **Implement FA-1 Fiscal Stance in sim** — `faction_layer_v30` §5.9 is drafted (PROPOSED); wire
  the per-faction/province stance choice + yield formula into `sim/territory/registry.py`'s
  Treasury accounting (ED-FA-0008, still open).
- **Author FA-6(c) Sack** (ED-FA-0013, needs_jordan) once Jordan rules the atrocity-content /
  W-for-legitimacy exchange-rate tone call.
- **Jordan ruling needed: ED-SC-0015** (Parliamentary total-victory Mandate stacking) — surfaced
  by this session's Censure build; see `handoffs/HANDOFF_SC.md`.
- **`ci_political_v30` read-routing bug (LB-24, tracked as an `IN`-lane tooling item in
  `handoffs/HANDOFF_IN.md`):** raw `designs/provincial/ci_political_v30.md` is ~26k but tracked
  read returns 0 (index-routes) — this is a routing/tooling bug, not a faction-content decision,
  but the affected file is faction/political content so cross-referenced here.
