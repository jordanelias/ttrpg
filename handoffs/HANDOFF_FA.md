# Handoff — FA (Faction Actions)

Lane-scoped continuity for the `FA` (faction actions) lane, per the `ED-<LANE>-NNNN` namespace
(`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md` is the
index; see it for cross-lane/global items.

No active work tracked in this lane as of the 2026-07-02 HANDOFF split. Canonical heads:
`designs/provincial/faction_canon_v30.md`, `faction_layer_v30.md`, `faction_behavior_v30.md`,
`faction_state_authoring_v30.md` (overview: `designs/factions/faction_systems_overview_v30.md`).

## Pending

- **FA/SE historical-precedent research docket (filed 2026-07-08).**
  `designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md`
  — an intensive historical/political-science research pass (Jordan-requested) covering fiscal
  sociology, tax farming, moral-economy dearth politics, urban charters, provincial-governor
  oversight, conquest terms, parish-level church-state jurisdiction, frontier colonization,
  succession/regency, and legitimacy theory (Weber/Olson/Hirschman/Ibn Khaldun) — chosen to be
  disjoint from the deliberation-and-procedure research already mined for the SC lane. Distills
  into 9 FA-lane mechanical proposals + a citation-patch batch, filed as **ED-FA-0007..0016**
  (see `canon/editorial_ledger.jsonl` for each item's full scope; `needs_jordan` forks:
  ED-FA-0009 coercion/capital muster asymmetry, ED-FA-0012 Sack mechanic (part c only),
  ED-FA-0013 Regency interregnum, ED-FA-0014 Protected Tributary, ED-FA-0015 Guild embargo).
  Report's own priority order: **FA-1 + FA-2 (fiscal stance + muster re-grounding) next**, then
  FA-5/FA-6(a/b) riding the ED-FA-0004 Stratum-B rewrite. Not yet authored into the design docs —
  this filing is the docket; a follow-on pass drafts each accepted item into
  `faction_layer_v30`/`faction_canon_v30`/`faction_action.py` as PROPOSED.
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

- **Author FA-1/FA-2 (fiscal stance + muster re-grounding) into `faction_layer_v30`/
  `faction_action.py`** — the historical-precedent docket's top FA-lane priority (see Pending).
- **`ci_political_v30` read-routing bug (LB-24, tracked as an `IN`-lane tooling item in
  `handoffs/HANDOFF_IN.md`):** raw `designs/provincial/ci_political_v30.md` is ~26k but tracked
  read returns 0 (index-routes) — this is a routing/tooling bug, not a faction-content decision,
  but the affected file is faction/political content so cross-referenced here.
