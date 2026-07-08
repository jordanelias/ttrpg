# Handoff — SE (Settlements)

Lane-scoped continuity for the `SE` (settlements) lane, per the `ED-<LANE>-NNNN` namespace
(`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md` is the
index; see it for cross-lane/global items.

No active work tracked in this lane as of the 2026-07-02 HANDOFF split. Canonical head:
`designs/territory/settlement_layer_v30.md` (+ `settlement_adjacency_v30.md`,
`territory_temperaments_v30.md`, `designs/world/geography_v30.md`).

## Pending

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

(none currently tracked.)
