# Refutation notes — ui-spec-stranded-off-index

## Factual claims (all verified TRUE)
- `designs/ui/valoria_ui_ux_v4_1.md` header: Status CANONICAL, dated 2026-04-16, deps = "all 19 v30
  canonical design documents + combat_v30 ED-548". combat_v30 is now PARTIALLY SUPERSEDED (CURRENT
  head = combat_engine_v1), so v4.1 rests on a shifted foundation.
- CURRENT.md: 15 subsystem rows enumerated (combat, mass battle, social, faction, settlement,
  threadwork, architecture x2, articulation, npc, workplan, godot, board, dice). NO UI / player_agency
  / legibility row. Verified.
- `valoria_ui_ux_v4_2_workplan.md`: Status "WORKPLAN — awaiting Jordan's approval ... before execution
  begins." Source audit = 69 findings / 20 P1. Target `valoria_ui_ux_v4_2.md` ABSENT from `designs/ui/`
  (dir listing confirms: only v4, v4_1, workplan, audits, supplement — no v4_2). Verified.
- DRAFT contest walkthrough exists: `designs/audit/2026-07-01-contest-player-interaction/
  player_interaction_walkthrough_v1.md`, Status DRAFT, "the only current-era interaction artifact"
  claim holds — it is the sole current-gen player-facing spec.

## Intent hunt (searched: ledger, supersession register, workplan v5, roadmap_state, decision queue,
handoffs)
- Ledger: UI mentions are all OLD (ED-697/544/548, all 2026-04-16..18) + ED-1058 (contest dicts). NO
  entry tracking v4.1 staleness or v4.2 non-execution.
- `canon/supersession_register.yaml`: v4.1 NOT marked superseded anywhere. Stale-CANONICAL, unflagged.
- `designs/workplans/valoria_master_workplan_v5.md`: ZERO hits for ui/player-facing/legibility/
  interface/walkthrough. No sequenced slot for the player-facing layer.
- `references/roadmap_state.yaml`: no UI/player entry.
- 23-item decision queue: no UI item.
- COUNTER-evidence (partial): HANDOFF_SC.md §52-53 + HANDOFF.md §55-56 show the SC walkthrough was
  "seeded ahead of Stage 6 so every later stage designs toward it" — a DELIBERATE per-subsystem method.
  Walkthrough header confirms: "Everything built so far ... Nothing yet answers what the player
  actually sees and do" — the current-gen method is bottom-up per-subsystem, not a monolithic UI doc.

## Assessment
The intent hunt did NOT refute — it strengthened the factual core. The corpus-wide player-facing layer
is genuinely off every currency/sequencing artifact, and stale-CANONICAL v4.1 (resting on superseded
combat_v30) is unflagged in supersession/ledger. No documented deliberate deferral exists.

BUT the finding overstates two things:
1. "only comprehensive player-facing spec" — v4.1 is a *structural supplement*; v4.1 header itself says
   "v4 remains authoritative for content-level UI specification." v4.md (161KB) is the larger content
   spec. Both predate current gen, so the thrust survives, but the singular framing is imprecise.
2. Severity P1 / "actively undermines the North Star." The game is pre-implementation (Godot 1/27
   modules, Gate-0 unexecuted). The dramatic-legibility bar is applied PER-SUBSYSTEM (the audit does
   this; the SC lane does this). Authoring a comprehensive UI monolith now, mid mechanic-churn
   (combat R3, social rebuild Stage 4), would be premature — a stale monolith is arguably the correct
   state during churn. The gap is forward-debt that narrows legibility coverage and carries a real
   drift hazard (CANONICAL UI rendering superseded combat_v30), but it does not BLOCK emergence today.
   That is P2, not P1.

## Intent
UNDETERMINED. A plausible deliberate sequencing rationale exists (defer corpus UI until subsystems
finalize; the SC per-subsystem walkthrough is evidence of the intended method) — but it is UNDOCUMENTED
for the corpus-wide layer, and v4.1's stale-CANONICAL status is affirmatively unmanaged. Cannot call it
cleanly DELIBERATE-with-safeguard nor cleanly NOT-INTENDED.

## Novelty
NEW confirmed — not in calibration list, ledger, supersession, handoffs, or decision queue. (The SC
walkthrough in HANDOFF_SC is a narrower, different item.)

## Verdict: PLAUSIBLE
Factual scaffolding fully verified (cannot refute), but the P1 severity and "actively undermines"
framing are overstated given deliberate per-subsystem method + pre-implementation timing. Revise to P2,
direction backwards, Q-robust. Real, worth tracking; not a North-Star blocker.
