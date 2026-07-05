# Handoff — FA (Faction Actions)

Lane-scoped continuity for the `FA` (faction actions) lane, per the `ED-<LANE>-NNNN` namespace
(`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md` is the
index; see it for cross-lane/global items.

No active work tracked in this lane as of the 2026-07-02 HANDOFF split. Canonical heads:
`designs/provincial/faction_canon_v30.md`, `faction_layer_v30.md`, `faction_behavior_v30.md`,
`faction_state_authoring_v30.md` (overview: `designs/factions/faction_systems_overview_v30.md`).

## Pending

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

- **`ci_political_v30` read-routing bug (LB-24, tracked as an `IN`-lane tooling item in
  `handoffs/HANDOFF_IN.md`):** raw `designs/provincial/ci_political_v30.md` is ~26k but tracked
  read returns 0 (index-routes) — this is a routing/tooling bug, not a faction-content decision,
  but the affected file is faction/political content so cross-referenced here.
