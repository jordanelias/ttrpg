# ED Options — drafted candidates, NOT filed

## Status: RATIFIED (Jordan, 2026-07-05 — ALL 12 accepted and FILED in the ledger; forks resolved to audit defaults. See ID map below.)
## Date: 2026-07-04

**These entries are NOT in `canon/editorial_ledger.jsonl`.** Per the ED-1094 merge-ratifies
convention, filing them in this PR would ratify them on merge; they are held back loudly instead.
To adopt one: allocate its lane ID per `references/id_reservations.yaml` protocol (read
`next_free`, allocate, bump, co-commit), paste the JSON line into the ledger, and cite this file
as source. Severity and lane are proposals. Numbers `NNNN` are placeholders — never max+1.

---

**E-1 · `ED-SE-NNNN` — Settlement governance loop: ratify-or-revise the redesign** (P2, F-1)
```json
{"id": "ED-SE-NNNN", "status": "open", "priority": "P2", "needs_jordan": true, "title": "Ratified settlement governance loop is a four-verb stat-pump; drafted redesign is untracked", "detail": "settlement_layer_v30 §3.2 offers one mandatory verb from four stat-pumps/season; governance_play_redesign_v1.md self-diagnoses the collapse ('roll one die a season') and its G1 prerequisite (sim/territory/registry.py + ledger, 6 tests) is already built. Decide: ratify the redesign (possibly staged), revise it, or explicitly defer with a banner. Until decided, add the proposal to CURRENT.md's settlement row and HANDOFF_SE pending items so it cannot orphan.", "source": "designs/audit/2026-07-04-ners-qualitative-audit/ners_qualitative_audit_v1.md F-1"}
```

**E-2 · `ED-IN-NNNN` — Convergence Markers need a detector/applier** (P2, F-2)
```json
{"id": "ED-IN-NNNN", "status": "open", "priority": "P2", "needs_jordan": true, "title": "The 'emergent narrative engine' (8 Convergence Markers) has no runtime mechanism", "detail": "arc_register_events.md §VI markers are hand-authored trigger+payload rows with no detector, no Key type, no module contract, no sim module; their combined payloads are non-summative by the doc's own header, so an applier is required. Author a minimal detector (registry of trigger-pairs checked per Accounting, emitting meta.convergence_marker consumed by articulation §3.1). Candidate home: game_director (doc:null) or a new small module. Also fix throughlines_complete T-24's 'not designed — structural' overclaim or implement to match it.", "source": "ners_qualitative_audit_v1.md F-2"}
```

**E-3 · `ED-IN-NNNN` — Articulation trigger ruleset omissions + §6.4 false assertion** (P2, F-4)
```json
{"id": "ED-IN-NNNN", "status": "open", "priority": "P2", "needs_jordan": false, "title": "articulation §3.1 omits scene.battle_concluded / scene.investigation_resolved (+combat_resolved); §6.4 asserts an unstated rule", "detail": "Both types are registry-declared consumed (key_type_registry §7 L682/L705); §3.1's 10-trigger ruleset has neither; §6.4 L296 claims battle_concluded 'already triggers Tier 2' — contradicted by the doc's own Stage-10 belief_revised precedent (defaults are not self-executing; a trigger row had to be added). Add trigger rows 11-12 (+combat_resolved variant), correct §6.4, re-run the Stage-10-style articulation sim battery over the new rows.", "source": "ners_qualitative_audit_v1.md F-4"}
```

**E-4 · `ED-IN-NNNN` — Playability layer currency: UI/UX v4.1 stale-CANONICAL + no legibility home** (P2, F-3)
```json
{"id": "ED-IN-NNNN", "status": "open", "priority": "P2", "needs_jordan": true, "title": "Player-facing/legibility layer has no maintained home; UI/UX v4.1 reads CANONICAL against superseded deps", "detail": "valoria_ui_ux_v4_1.md (CANONICAL 2026-04-16, deps include superseded combat_v30, specifies STRUCK Taint/CD tracks) is absent from CURRENT.md; the v4.2 repair workplan (69 findings/20 P1) was never executed; only current-era interaction artifact is the DRAFT contest walkthrough. Decide the standing policy: per-subsystem walkthroughs as subsystems stabilize (the SC-lane method — then banner v4.1 as superseded-method and state the policy where CURRENT.md points at it) vs reviving a corpus-wide spec. Either way add a legibility/UI row to CURRENT.md.", "source": "ners_qualitative_audit_v1.md F-3"}
```

**E-5 · `ED-WR-NNNN` — Complete GD-1's sweep of peninsular_strain_v30 (~8 co-victory sites)** (P3, F-5)
```json
{"id": "ED-WR-NNNN", "status": "open", "priority": "P3", "needs_jordan": false, "title": "peninsular_strain_v30 never received GD-1's Partition/co-victory strike banners", "detail": "§6.3 + L129/220/310/457/493/571/590 still carry co-victory as unmarked canonical text; sibling victory_v30 §0.1 was banner-swept. Residual of the tracked pending Pass-2k batch (canonical_sources.yaml FACTION-SPECIFIC-VICTORY-PATHS). Sweep with [SUPERSEDED-BY: GD-1] banners; derive sweep targets by grep, not by GD-1's hand list (see E-7).", "source": "ners_qualitative_audit_v1.md F-5"}
```

**E-6 · `ED-IN-NNNN` — Steering-surface reconciliation** (P2, S-2)
```json
{"id": "ED-IN-NNNN", "status": "open", "priority": "P2", "needs_jordan": true, "title": "Steering surfaces disagree: workplan v5 vs CURRENT.md/decision-queue on J-38; roadmap_state.yaml describes a May track; queue items 1-3 pre-R2", "detail": "Fix the J-38 status line in workplan v5 (propagation spec is CANONICAL per ED-1093); regenerate-or-retire roadmap_state.yaml; refresh decision-queue items 1-3 against merged R2. Adopt the hierarchy: CURRENT.md -> lane handoffs -> decision queue authoritative; workplan v5 derived (points at handoffs instead of duplicating status). Consider a monthly reconcile session type per strategic_judgments J-14.", "source": "strategic_judgments.md J-12/J-13/J-14; audit S-2"}
```

**E-7 · `ED-IN-NNNN` — Register back-propagation gate** (P2, S-1)
```json
{"id": "ED-IN-NNNN", "status": "open", "priority": "P2", "needs_jordan": true, "title": "Ratifications never round-trip to mechanics_index/supersession_register (frozen at ED-912/06-28)", "detail": "supersession_register has no GD-1 entry (root cause of E-5) and no mass-battle/contest flips; mechanics_index's mass_battle and social_contest entries describe a materially false 'not built' baseline; its conviction_scar row cites the territorial Piety doc for the personal Scar mechanic. Extend ED-1094 with a register-touch rule: a PR flipping a ## Status: line or striking a mechanic co-commits the register rows; enforce via a currency-gate-family CI check in tools/ (one rule, one home).", "source": "ners_qualitative_audit_v1.md S-1; strategic_judgments J-9"}
```

**E-8 · `ED-WR-NNNN` — MS/RS: one name, complete the sweep** (P2)
```json
{"id": "ED-WR-NNNN", "status": "open", "priority": "P2", "needs_jordan": true, "title": "World-stability track is MS in threadwork_v30 §5 but RS in params/threadwork.md — relitigated 3x, sweep never finished", "detail": "ED-428 (keep RS) -> ED-731 (propagate MS) -> ED-772 (continue sweep) and params/threadwork.md still reads RS; names_index registers the rename at enforce:warn only. Pick the final name once, sweep both canonical carriers + victory's MS clock reference, flip the names_index entry to enforce:block. Precondition for any typed engine-params export binding this track (CLAUDE.md §5).", "source": "audit §4 preconditions; centralization lens"}
```

**E-9 · `ED-PC-NNNN` — Schedule the combat player-interface + ED-911 as named increments** (P2)
```json
{"id": "ED-PC-NNNN", "status": "open", "priority": "P2", "needs_jordan": true, "title": "Combat's player-input surface and thread interface (ED-911) are deliberate staging with no scheduled slot", "detail": "wrapper.engagement() has no player-decision parameter (verified; DELIBERATE sim-first staging per refutation R-1) and R2/R3 sequences reserve no increment for either the input surface or ED-911 (a regression from combat_v30 §10's Leap-in-combat). Add both as named post-R3 sequence entries (align with phase4_5_plan_v1's abilities-as-access layer and the walkthrough-first method from the SC lane). Do not start before R3 lands (strategic_judgments J-2).", "source": "audit R-1 + §4 wire-it #1; strategic_judgments J-5"}
```

**E-10 · `ED-SC-NNNN` / `ED-MB-NNNN` — Targeted dominance sweeps for the unverified hunt lines** (P3)
```json
{"id": "ED-SC-NNNN", "status": "open", "priority": "P3", "needs_jordan": false, "title": "Sweep the unverified degenerate-play candidates when their lanes next open", "detail": "Social (fold into Stage 4): Recall/Corroborate/Prep stacking vs a global pool cap; boost-lookup vs Appraise value; coalition-vs-solo floor (ED-297 ratified coalition dominance - decide the solo floor). Combat (post-R3 re-hunt): armor-tier no-downside, imposition asymmetry, ability-stacking budget (ability_primitives.py enforces no cap while config prose claims one - fix the false claim either way). Mass battle: split-vs-concentration evidence contamination already tracked ED-MB-0002; Company-scale thread-cost arbitrage rides ED-1010. All are [OPEN - Jordan tuning]-sensitive: verify structure survives retuning before filing as defects. Full list: 01_workings/deferred_unverified.json + p3.json.", "source": "audit §5"}
```

**E-11 · `ED-IN-NNNN` — Naming-authority unification (glossary / names_index / descriptor_registry)** (P2)
```json
{"id": "ED-IN-NNNN", "status": "open", "priority": "P2", "needs_jordan": true, "title": "Two files self-declare naming authority and disagree (7-attr glossary vs 9-attr registry); resonance_style deprecated-but-live", "detail": "Fold glossary's canonical-name tables into the names_index mirror gate (or generate glossary from names_index); reconcile the attribute roster (7 vs 9, and which of Cognition/Presence/Spirit are canonical vs alias) - note mass_combat's Command formula (PP-232) is written against legacy names; reconcile descriptor_registry's retired resonance_style against npc_behavior §1.3's live Resonant Style. Then flip Godot-load-bearing name entries warn->block.", "source": "centralization lens; strategic_judgments J-10"}
```

**E-12 · `ED-FI-NNNN` — Audit the investigation lane (GAP-1)** (P3)
```json
{"id": "ED-FI-NNNN", "status": "open", "priority": "P3", "needs_jordan": false, "title": "investigation_systems_v30 was audited by no lane; it is the home of orphan throughlines T-02/T-30", "detail": "Run the dossier + threadwork-juncture + legibility pass on investigation_systems_v30 (+ fieldwork_v30 overlap) using this audit's charter and schemas (01_workings has the templates). T-02 (rendering=consciousness) and T-30 (information asymmetry) currently have no audited mechanical carrier.", "source": "audit GAP-1"}
```

---

*Selection guidance (Fable judgment, not binding): if picking three, take **E-2 + E-3 + E-7** —
together they make computed emergence arrive and render (the audit's bottom line), and they stop
the register drift that caused F-5. E-1 is the largest single playability win. E-8 is the
cheapest precondition-clearing pick before any Godot export work.*

---

## RATIFICATION ADDENDUM (2026-07-05)

All 12 options were **accepted by Jordan** (post-merge instruction on PR #77) and are now FILED
in `canon/editorial_ledger.jsonl` with lane IDs allocated per `references/id_reservations.yaml`.
Internal forks resolved to the audit defaults: **E-1** adopt the governance-redesign path;
**E-4** per-subsystem walkthrough method as standing policy; **E-8** MS (Mending Stability) wins.
The "options, not filed" framing above is retained as the historical record of the hold-back.

| Option | Filed as | Fork resolution |
|---|---|---|
| E-1 | `ED-SE-0001` | adopt redesign path |
| E-2 | `ED-IN-0003` | — (execution vehicle: 2026-07-05 narrative-engine effort) |
| E-3 | `ED-IN-0004` | — (execution vehicle: 2026-07-05 narrative-engine effort) |
| E-4 | `ED-IN-0005` | per-subsystem walkthrough policy |
| E-5 | `ED-WR-0001` | — |
| E-6 | `ED-IN-0006` | — |
| E-7 | `ED-IN-0007` | — |
| E-8 | `ED-WR-0002` | MS wins |
| E-9 | `ED-PC-0001` | — |
| E-10 | `ED-SC-0001` | — |
| E-11 | `ED-IN-0008` | — |
| E-12 | `ED-FI-0001` | — |
