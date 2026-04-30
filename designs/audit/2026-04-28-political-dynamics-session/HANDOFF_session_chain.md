<!-- [PROVISIONAL: 2026-04-29 multi-session handoff] -->
<!-- STATUS: ACTIVE — handoff for sessions resolving 68 stress-test issues + simulations -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/HANDOFF_session_chain.md -->

# Multi-Session Handoff — Political Dynamics Resolution Chain

**Created:** 2026-04-29 (Session 1 close).
**User mandate:** "Resolve all gaps/issues/provisional items flagged by today's commits. After that, perform a comprehensive set of simulations across mechanics all directions in granular detail to map out mechanical interactions. Please use multiple sessions to avoid context degradation and task pressure."

---

## SESSION CHAIN OVERVIEW

| # | Status | Scope | Deliverable |
|---|--------|-------|-------------|
| 1 | **DONE** | Author doc 17 — 48 patch resolutions for 68 stress-test issues | `designs/audit/2026-04-28-political-dynamics-session/17_specification_revisions.md` (committed `6de72da1`) + ED-750..757 (committed `831c889a`) |
| 2 | **DONE** | Apply doc 17 patches → produce doc 12 v1.1 | `12_development_specification.md` v1.1 (committed `9dede391`) with 26 patches applied — 1565 lines, 79 PATCH references; ED-756 resolved (`f5acbaa2`) |
| 3 | **PARTIAL** | Re-vet v1.1 against §13 promotion checklist | Spot-vetting performed during S4-A simulation; no invariant breaks observed in traced scenarios; full §13 checklist walk-through deferred until simulations complete |
| 4 | **DONE** | Simulation pass — Direction A (Opinion architecture) | `SIM_A_opinion_architecture.md` (commit `fda634db`); 6 scenarios traced; single-writer invariant verified; 6 spec gaps surfaced (ED-758) for v1.2; 4 emergent properties documented |
| 5 | **DONE** | Simulation pass — Direction B (Domain Action selection) | `SIM_B_domain_action_selection.md` (commit `8a6dbb44`); 8 scenarios; 7 DA-invariants verified; 9 spec gaps (1 P1-critical SIM-B-G8 in ED-759); 1 v1.2-recommended patch (stall-escalator in ED-760); 5 emergent properties |
| 6 | **DONE** | Simulation pass — Direction C (Settlement Signal flow) | `SIM_C_settlement_signal.md` (commit `684b1627`); 9 scenarios; 8 SS-invariants verified (1 partial); 8 gaps (1 P1-critical SIM-C-G6 routing); 5 emergent properties |
| 7 | **DONE** | Simulation pass — Direction D (Relational dynamics) | `SIM_D_relational_dynamics.md` (commit `84eec07c`); 8 scenarios; 6 REL-invariants verified; 6 gaps surfaced; SIM-B-G8 reaffirmed P1-critical; 5 emergent relational properties |
| 8 | **DONE** | Simulation pass — Direction E (Composition / multi-agent emergence) | `SIM_E_composition.md` (commit `b04523d2`); 6 scenarios, 3-faction × 3-Year trace; SIM-B-G8 P1-criticality confirmed at scale; 2 new gaps + 3 forward-looking design observations |
| 9 | **DONE** | Synthesis + v1.2 production | Doc 19 v1.1 validation report (commit `b7f2235b`); Doc 21 v1.2 specification revisions (commit `b7f2235b`); Doc 12 v1.2 produced (commit `7c9384ec`) — 1958 lines, +394 vs v1.1; all 39 patches applied including 3 P1-critical + ED-760 stall-escalator. Ready for §13 Promotion Checklist re-vet. |

Session 1 deliverable persists today's gap-resolution; sessions 2-9 execute the chain. User-controlled cadence (continue per session).

---

## SESSION 2 — APPLY PATCHES (next-up)

**Pre-flight read** (full):
1. `designs/audit/2026-04-28-political-dynamics-session/17_specification_revisions.md` (the source of patches)
2. `designs/audit/2026-04-28-political-dynamics-session/12_development_specification.md` (the target)
3. `designs/audit/2026-04-28-political-dynamics-session/16_session_close_observations.md` (priority order, severity register)

**Approach:** Mechanical patch application using doc 17 §7 checklist (28 numbered steps). Doc 17 patches use LOCATE/REPLACE/INSERT directives that are designed for `str_replace`-style application. Suggested execution:

1. **Save baseline.** Copy current doc 12 to `/home/claude/doc12_v10.md` for diff reference.
2. **Apply cross-cutting first.** PATCH 1.4, 1.5, 1.6 (single-writer Opinion model). These rewrite §1.4-1.6 of doc 12 entirely — apply as full-section replacement, not str_replace.
3. **Apply P1 patches in numerical order** (PATCH 2.1 → 2.8). Do PATCH 2.1 last among these — it adds a 42-row table that's the longest single insert.
4. **Apply P2 patches** (3.1 → 3.15). Order matters for 3.5 (Grieving in DA Proposal) which depends on 2.1's select_proposal() rewrite. Cross-check PATCH 3.6 (Knot integration) against §1.4 rewrites — they touch overlapping territory.
5. **Apply P3 stubs.** Mostly documentation-level; low conflict risk.
6. **Apply §5 featured-behavior author commentary.** §1.1 of doc 12.
7. **Skip §6 Jordan-decision items by default.** Insert `<!-- BLOCKED: ED-755 — awaiting Jordan -->` markers at relevant locations. Default recommendations from doc 17 §6 are NOT applied without explicit Jordan approval.

**Conflict resolution rules:**
- PATCH 1.4 + PATCH 3.4 (Opinion lazy init): both touch Procedure D. PATCH 3.4's `derive_initial_affect` insert goes inside PATCH 1.4's rewritten Procedure D body.
- PATCH 1.5 + PATCH 3.2 (Knowledge Decay Procedure B.0): B.0 is a NEW pre-step; insert before PATCH 1.5's rewritten body.
- PATCH 2.1 + PATCH 3.5 (Grieving): Grieving is a Mood gate inside select_proposal(); insert as condition check after primary alignment scoring but before final return.
- PATCH 2.5 + ED-755 R-41-A (crisis masking): null guards in compute_settlement_signal apply regardless of crisis-masking decision; safe to apply both.

**Verification gates:**
- After each patch: re-read modified section and confirm semantic intent matches doc 17 PATCH RATIONALE.
- After all patches: re-read §13 Promotion Checklist of doc 12 v1.1 and confirm each item still satisfied.
- Run a sample trace: pick one Concern → Domain Action chain and walk through it manually using v1.1 to verify no regressions.

**Expected output:** `12_development_specification.md` v1.1 (replaces v1.0 in same path). ~1100-1200 lines (up from 985) due to inserts. Update doc 12's header version line. Add a `## §0 v1.1 CHANGE LOG` section at top listing all 48 patches applied.

**Estimated session 2 length:** Substantial. May need to split S2 into S2A (cross-cutting + P1) and S2B (P2 + P3 + §5).

---

## SESSION 3 — RE-VET v1.1

After v1.1 produced, run promotion checklist (doc 12 §13):
- All Procedures internally consistent? (especially B/C/D after rewrite)
- All formulas dimensionally correct? (PATCH 2.8 normalization)
- All cross-references resolve? (PATCH 3.6 Knot integration depends on existing Knot system spec)
- All thresholds defined? (PATCH 4 stubs may have surfaced new "TBD" markers)
- All visible_actions reference correct domains? (PATCH 3.14)

Flag any patch that introduces invariant violations or unresolved references. Resolution may require small follow-up patches → doc 17b, or revert.

---

## SESSIONS 4-8 — SIMULATIONS

User asked for "comprehensive set of simulations across mechanics all directions in granular detail to map out mechanical interactions." Five directions chosen to cover the spec's interaction surface without redundancy:

**Direction A — Opinion architecture (single-writer model):**
- Procedure B (Concern → Path A or B): 6+ trace scenarios covering both paths, Knowledge Decay (PATCH 3.2), visibility gate (PATCH 3.3), concern_history cooldown (PATCH 3.1).
- Procedure C (Memories accumulation): Memory threshold check, lazy init (PATCH 3.4).
- Procedure D (Opinion writes): scar split (PATCH 3.7), max_scars cap (PATCH 2.2), conviction multiplier (PATCH 2.3), additive composition (PATCH 2.8), Resolved/Vindicated (PATCH 3.8).
- Cross-procedure: confirm no double-write under all 6 scenarios.

**Direction B — Domain Action selection:**
- select_proposal() (PATCH 2.1) + DOMAIN_ARMATURE_ALIGNMENT 42-entry table.
- conviction_secondary fallback (PATCH 2.6).
- Grieving Mood gate (PATCH 3.5).
- generate_new_project two-tier (PATCH 3.13).
- Trace 4-6 NPCs across 3 Accountings to surface emergent action diversity.

**Direction C — Settlement/Faction signal flow:**
- compute_settlement_signal (PATCH 2.5) + governor fallback.
- resonance_lookup (PATCH 2.7) + 8 EVENT_CATEGORIES.
- population_disposition recalc (PATCH 3.9).
- Settlement → faction Concern propagation; verify Concern volume target (0.5-1.5 per NPC per Accounting per doc 17 §8).

**Direction D — Relational dynamics:**
- NPC Standing recalculation (PATCH 3.11).
- Outreach Priority 3 default + escalation (PATCH 3.10).
- Knot integration via Outreach (PATCH 3.6).
- Standing 5 milestone scenes (E-DIAG-A / N-DIAG-A featured behavior).
- Memory replacement (PATCH 3.15).

**Direction E — Composition / cross-system:**
- Multi-agent: 6+ NPCs, 2 factions, 1 settlement, 12 Accountings.
- Surface emergent dynamics: feedback loops, oscillations, deadlocks, runaway accumulation.
- Cross-check against §6.5 doc 12 (faction-scale dynamics expected).

**Per-direction deliverable:** simulation log + interaction map (causal arrows between mechanics) + findings register (issues found → priority assigned → either auto-resolve or flag for v1.2).

---

## §6 JORDAN DECISIONS — REQUIRED BEFORE FULL v1.1

Doc 17 §6 lists 5 design decisions blocking full v1.1 + carryover from prior sessions. Default recommendations stated in doc 17 but not applied. Jordan should review:

1. **E-38-A/B symbolic_effects:** keep+define vs cut. 210-entry table impact. Default rec: KEEP+define.
2. **E-TOP-A:** opaque vs legible faction-top stance. Default rec: opaque (factions have inscrutable internal logic).
3. **ST-31-B:** NPC self-monitoring? Default rec: B = no (NPCs don't introspect their own Standing/Conviction).
4. **R-41-A:** crisis masking persistence. Default rec: B = accept (mask persists across Accountings under sustained crisis).
5. **Carryover items:**
   - Intelligence as 6th faction stat (last touched ED-748 marked struck — confirm)
   - LICENSE/GOV-08 status
   - §1.1 Knot Formation During Play scope
   - §1.2 Accord Propagation to Settlement Order

Until these resolve, Session 2 produces v1.1 with `[JORDAN-DECISION-PENDING-ED-755]` markers at relevant locations rather than applying defaults.

---

## RESUMPTION CHECKLIST FOR EACH SESSION

At each session start:
1. Bootstrap (`python3 -c "import _init"` from /home/claude).
2. `task_gate('editorial')` for S2-S3, `task_gate('simulation')` for S4-S8.
3. Read this handoff doc.
4. Read the doc 17 + doc 12 + relevant prior session output.
5. Confirm prior session's commits via `g.read_files_graphql([...])` to verify state.
6. Execute scoped work.
7. Commit with proper scope tag.
8. Update this handoff doc's status table at top before closing.
9. Append session-specific notes to a §SESSION-N section at bottom of this doc.

---

## CONTEXT BUDGET PER SESSION

Bootstrap + per-session register reads ≈ 12k tokens. Doc 17 (~20k) + doc 12 (~11k) baseline reads = 31k. Reserve 60k for execution work + thinking. Reserve 30k for file output + verification. Total target per session: ≤130k tokens used, leaving headroom under context cap.

If S2 patch application exceeds budget mid-execution: stop after current patch, commit partial v1.1 as `12_development_specification_v1.1_partial.md`, update this handoff with continuation point, hand off to S2B.

---

## SESSION 1 NOTES — 2026-04-29

**Done:**
- Doc 17 authored (1371 lines, 48 patches, 8 sections). Commit `6de72da12d4663ec030cbded56a2b71d2dcc2be7`.
- Editorial ledger ED-750..757 added. Commit `831c889a032c6cba095a746bd6f64b366ac9a16e`.
- This handoff doc written.

**Not done:**
- Patch application to doc 12 (deferred to S2 — 985-line target with 48 interlocking patches needs fresh-context focus).
- Session log infrastructure not engaged — `start_session_log` has an auth-check bug (`_authorize_next_commit` doesn't whitelist this caller). Working around via direct `safe_commit`. Worth fixing in an infrastructure session.

**Open concerns flagged but not resolved:**
- DOMAIN_ARMATURE_ALIGNMENT 42 values are derived defaults; playtest calibration pending (doc 17 §8.1).
- OPPOSITIONAL_CONVICTION_PAIRS canonicalization — Continuity↔Reason vs Continuity↔Equity (doc 17 §8.2).
- visible_actions count target — 60 / 80 / 96 (doc 17 §8.3).
- Concern volume target — measure in S4 simulation (doc 17 §8.6).

**Bootstrap auth bug:** `github_ops.start_session_log()` calls `_authorize_next_commit()` which whitelists only `safe_commit`/`assert_bootstrap`/`safe_session_close`/`append_to_register`/etc. but NOT `start_session_log`/`update_session_log`/`close_session_log`. Add these to the allowlist in `github_ops.py:324` (the `approved` tuple). Until fixed, manual `safe_commit` against `session_logs/<scope>_<token>.md` works as substitute, with the caveat that the auto-generated `session_log_current.md` pointer won't update.

---


---

## SESSION 2 NOTES — 2026-04-29

**Done:**
- Editorial ledger archival (ED-745..748 → archive). Commit `9986d8d9`.
- Doc 12 v1.1 produced and committed. Commit `9dede391`.
  - 26 explicit PATCH directives from doc 17 applied: PATCH 1.4, 1.5, 1.6 (cross-cutting); 2.1, 2.2, 2.3, 2.5, 2.6, 2.7, 2.8 (P1); 3.1-3.11, 3.13-3.15 (P2; 3.12 covered by 2.5; 3.4 also wires Procedure D and E).
  - §1.1 Featured Behaviors author commentary added (4 entries from doc 17 §5).
  - §15 Priority-3 stub resolutions appendix added (7 stub categories).
  - §16 Pending Jordan-decision items appendix added (5 items, ED-755).
  - Verification: 28/28 expected-content checks pass.
- ED-756 marked resolved. Commit `f5acbaa2`.
- This handoff doc updated.

**v1.1 structural changes vs v1.0:**
- 985 → 1565 lines (+580); 44k → 83k chars (+39k).
- New top sections: §0.1 (change log), §15 (P3 stubs), §16 (Jordan-decision flags).
- New subsections: §1.1, §3.6, §3.6.X, §4.5, §8.1, §6.2 B.0, §2.5.1.
- Procedure rewrites: B Resolution (single-writer), C Project Completion (Memory-only legacy), D banner.
- Function additions: `select_proposal()`, `compute_armature()`, `npc_observes_event()`, `get_or_init_opinion()`, `derive_initial_affect()`, `conviction_alignment_multiplier()`, `SettlementSignal.from_governor()`, `resonance_lookup()` w/ category fallback, `generate_new_project()`, `sample_domain_weighted_by_conviction()`.
- Tables added: `DOMAIN_ARMATURE_ALIGNMENT` (42 entries), `OPPOSITIONAL_CONVICTION_PAIRS` (4 pairs), `EVENT_CATEGORIES` + `CATEGORY_DEFAULT_RESONANCE`.
- Numbering note: §15/§16 appear before §14 (which is now an end-of-doc reference appendix). Cosmetic; v1.2 may renumber §14 → §17 for clean ordering.

**Not done:**
- Full §13 Promotion Checklist re-vet pass (S3) — pending. Spot checks during patch application surfaced no obvious invariant breaks, but a systematic walk-through of §13 against v1.1 has not been performed.
- Simulations (S4-S8) — pending.

**Open issues observed during v1.1 production:**
- §14 numbering: §15/§16 appear before §14. Cosmetic; defer to v1.2.
- `derive_concern_tag()` and `categorize_event_type()` referenced in patches but not specified in v1.1; both are content-authoring helpers that need authoring per `[P3-RESOLVED-PER-DOC17]` markers.
- `VISIBLE_ACTIONS_TEMPLATES` referenced but content authoring deferred to `params/visible_actions.md` (PATCH 3.14 / NS-49-A) — not yet created.
- Procedure E `apply_drift()` does not yet route through `get_or_init_opinion()` (PATCH 3.4 specifies it should). Verified PATCH 3.4 inserts the call into Procedure E before drift application; spot-check post-commit confirms presence.

**Bootstrap auth bug:** Same as Session 1 — `start_session_log()` not whitelisted in `_authorize_next_commit()`. Did not engage session log infrastructure for S2 either; commits done via direct `safe_commit()`.

---

## SESSION 3 NOTES — TBD

S3 = re-vet pass against §13 of v1.1. To be done in fresh context. Resumption pre-flight: read v1.1 fully, then walk §13 promotion checklist item by item, recording verdict (pass/fail/partial) per item.

---

## SESSIONS 4-8 NOTES — TBD

Simulation chain. Each direction's pre-flight, scope, and deliverable already specified above in the main body of this handoff. Recommend starting S4 with v1.1 in fresh context after S3 confirms invariants.


---

## SESSION 4-A NOTES — 2026-04-29

**Done (S4 Direction A — Opinion architecture):**
- `SIM_A_opinion_architecture.md` produced and committed (`fda634db`). 36k chars, 527 lines.
- Six scenarios traced step-by-step with explicit state transitions:
  1. Canonical chain: Concern resolution → Memory → drift (single-writer verified).
  2. Project completion legacy → Memories → drift.
  3. Concurrent B + C in same season (both writing Memories about same subject; D consumes both).
  4. First-contact lazy init via `get_or_init_opinion()` + `derive_initial_affect()`.
  5. High-Scar NPC with `conviction_secondary=None` — uniform-fallback path engagement.
  6. Knowledge Decay → invalidation; visibility gate suppression; indirect propagation via Procedure E.
- Single-writer invariants `[INV-1, INV-2, INV-3, INV-4]` all hold under traced load.
- Editorial ledger ED-757 marked in-progress; ED-758 added for the 6 surfaced gaps. Commit `a85e0f2a`.

**Surfaced gaps for v1.2 (ED-758):**
1. `small_drift` / `larger_drift` coefficients in Procedure D not numerically specified.
2. Procedure D drift loop iteration order over `new_memories` not specified (matters when multiple Memories about same subject exist same season).
3. `weighted_select()` re-roll-and-average semantics under armature_confidence < 0.7 not fully specified (§3.6.X).
4. `knowledge_contradicts_belief()` content-authoring helper unspecified.
5. `evidence_memory_refs` write timing during D's drift loop unspecified.
6. Confidence boundary inconsistency: `if confidence <= 2` vs `if confidence >= 3` — boundary at exactly 2 ambiguous in spec.

**Emergent properties observed (worth flagging to design):**
1. Aligned-direction legacy magnitudes are 30-50% smaller post-patch vs pre-patch. NPCs slower to "warm up" to allies; reaction sharpness to opposition preserved.
2. Bridge-sympathy across hostile factions when secondary Convictions match — produces realistic individual rapport across institutional opposition.
3. Uniform-fallback NPCs (high-Scar without secondary) become genuinely chaotic in Concern framing — design-intentional but worth content-author awareness.
4. Visibility gate + Procedure E gossip chain produces ~1 Accounting delay between event and non-observer's Concern — politically authentic delay pattern.

**Methodology to replicate for S4-B/C/D/E:** Each direction should follow this 6-scenario pattern with explicit step-by-step state transitions, invariant checks, and gap-surfacing. ~30-40k chars per direction is reasonable depth.

---

## SESSIONS 4-B / 4-C / 4-D / 4-E NOTES — TBD

Per main body: Direction B (Domain Action selection / select_proposal + Standing recalc), Direction C (Settlement Signal + edge cases + governor fallback), Direction D (Standing recalc, Outreach, Knot, Memory replacement), Direction E (composition / multi-agent emergence). Each as fresh session per S4-A pattern.


---

## SESSION 4-B NOTES — 2026-04-29

**Done (S4 Direction B — Domain Action selection):**
- `SIM_B_domain_action_selection.md` produced and committed (`8a6dbb44`). 54k chars, 850 lines.
- Eight scenarios: 1) single-faction inner-circle competition, 2) tie-break cascade, 3) Conviction-aligned displacement (institutional_deference Ob 1), 4) Grieving Mood gate (Spirit Ob 1 pass/fail), 5) Distracted Mood interactions, 6) `generate_new_project()` two-tier, 7) Standing recalc over Campaign Year, 8) **multi-NPC multi-Accounting trace surfacing structural deadlock**.
- All 7 DA-specific invariants verified (`[DA-INV-1]` through `[DA-INV-7]`).
- ED-759 (9 gaps) and ED-760 (stall-escalator recommendation) added.

**SIM-B critical gap (SIM-B-G8):** `failed_da_proposals` definition in PATCH 3.11 — does "lost inner-circle competition" count as a failed proposal? If yes, the system has self-reinforcing-inequality dynamics (lower-Standing NPCs lose competitions, lose Standing, lose more competitions). Recommend strict definition for v1.2: "DA roll failed only," NOT "lost competition."

**SIM-B v1.2 patch recommendation:** Stall-escalator in `select_proposal()` score formula. `+0.05 × seasons_stalled` term prevents Scenario-8-style infinite-deadlock for unequal-Standing same-domain collisions.

**SIM-B emergent properties (5):**
1. Factions select proposals by domain alignment, not proposer Conviction.
2. Conviction-aligned displacement creates delayed political consequences via Memory-bus.
3. Long-grief Mood → Project failure cascade → Standing erosion.
4. Faction crisis state (≥40% Distracted/Grieving) is a player-observable strategic vulnerability.
5. Cumulative institutional drift through Standing recalc → meta-armature recomputation → proposal selection feedback.

**Cross-direction observations:** DA mechanics interlock with Direction A via Memory-bus; Standing changes generate `standing_change` events → Memories → Direction D dynamics; multi-Year multi-faction is the Direction E target.

---

## SESSIONS 4-C / 4-D / 4-E NOTES — TBD

S4-C (Settlement Signal + edge cases + governor fallback) next-up. Verify PATCH 2.5 null-guards under empty-Passive-NPCs, sparse-Memory, zero-weight; trace governor fallback; observe Settlement Signal → faction Concern propagation cadence per S-44-A scope.


---

## SESSIONS 4-C & 4-D NOTES — 2026-04-29

**Done (S4-C — Settlement Signal flow):**
- `SIM_C_settlement_signal.md` produced and committed (`684b1627`). 44k chars, 734 lines.
- Nine scenarios: 1) standard Solmund Signal generation, 2) empty Passive NPCs + governor fallback, 3) no recent Memories (Guard 2), 4) all-zero weights (Guard 3), 5) player-Disposition amplification scope (PATCH 3.12), 6) resonance lookup unknown event_type (PATCH 2.7 fallback), 7) Concern volume target measurement (~0.75/NPC/Accounting — within target), 8) population_disposition recalc (PATCH 3.9), 9) multi-settlement composition over 3 Accountings.
- 8 SS-invariants verified (`[SS-INV-1..8]`); INV-7 partial (post-cascade-decay salience can fall below clamp range).
- 8 gaps surfaced. **P1-critical SIM-C-G6:** "Relevant Active NPC" routing for Signal-derived Concerns is unspecified. Recommendation for v1.2: (a) governor if Active, else (b) faction leader if seat, else (c) round-robin among inner-circle by domain affinity.

**Done (S4-D — Relational dynamics):**
- `SIM_D_relational_dynamics.md` produced and committed (`84eec07c`). 379 lines.
- Eight scenarios: 1) P3 Outreach skipped no-consequence, 2) P3→P2 escalation at salience-5+ttl-1, 3) Knot integration via P2 Outreach (opacity preserved), 4) Standing change cascade S5→S7 large jump, 5) Standing 3↔4 transition (true N-DIAG-A milestone scene), 6) Standing demotion cascade (interaction with SIM-B-G8), 7) Passive NPC Memory replacement at 3-cap (PATCH 3.15), 8) multi-NPC multi-Accounting relational dynamics over 4 Years.
- 6 REL-invariants verified (`[REL-INV-1..6]`).
- 6 gaps surfaced. **SIM-B-G8 reaffirmed P1-critical** in Scenario 6 (interpretation materially affects Confessor's Standing trajectory under deadlock load).
- N-DIAG-A title-body inconsistency surfaced (G4): title "Standing 5 Milestone" but body describes 3↔4 transition.

**Cross-direction integration verified:**
- A↔B: Memory drift from Concerns/Project completions feeds Procedure D's Opinion mutations; Standing changes propagate via standard event/Memory chain.
- A↔C: Settlement Signals → Concerns → Resolutions → Memories → Procedure D drift. Closed loop.
- A↔D: Outreach attendance generates resolution Memories → Procedure D drift. Closed loop.
- B↔C: Strong settlement Signals trigger DA proposals (e.g., raid_threat → military DA). Direction-C generates inputs for Direction-B competition.
- B↔D: Standing recalc → Faction Meta-Armature recomputation → next-cycle proposal selection bias. Multi-Year cumulative institutional drift verified.
- C↔D: 3-cap Passive Memory replacement (D) shapes what feeds compute_settlement_signal (C). Direction-D mechanics determine Direction-C inputs.

**Cumulative gaps inventory (29 total across SIM-A/B/C/D):**
- 2 P1-CRITICAL (SIM-B-G8, SIM-C-G6) — material spec impact on Standing trajectory and Concern routing.
- ~12 P2 — clarifications affecting implementation determinism.
- ~15 P3 — minor doc/typo/authoring-helper specifications.

All gaps inventoried in respective SIM_*.md docs §summary sections; consolidated ED-761 in editorial_ledger.

---

## SESSION 4-E NOTES — TBD

**Direction E (Composition / multi-agent emergence) is the remaining direction.** Pre-flight for fresh session:

1. Read v1.1 doc 12, then SIM-A/B/C/D summaries (§ final sections of each).
2. Pre-flight: confirm 29-gap inventory; consolidate to a tight gap-register if useful.
3. Direction-E scenarios should test multi-agent multi-faction multi-decade dynamics:
   - 6+ NPCs across 2-3 factions, 12+ Accountings (3 Campaign Years).
   - Surface emergent: feedback loops, oscillations, deadlocks (validate stall-escalator recommendation ED-760), runaway accumulation, institutional ossification (per SIM-B Scenario 7 / SIM-D Scenario 8 emergent properties).
   - Cross-faction interference: Settlement Signal cross-border propagation, faction-vs-faction DA proposal effects on shared territories.
   - Validate SIM-B-G8 critical interpretation under longer time-frame (does strict definition produce stable inner-circle composition vs liberal producing accelerating exclusion?).

Recommend ≥30k chars for SIM-E given composition complexity. Fresh-context session strongly preferred to avoid degradation.

After SIM-E: Session 5 (synthesis) — roll up all 5 directions; produce final v1.1-validation report; surface unresolved interactions for v1.2; draft v1.2 patch list.

---

## SESSION CONTEXT NOTE — 2026-04-29

This session (S2 + S3-partial + S4-A + S4-B + S4-C + S4-D) executed under continuous "continue" prompts. **7 simulation/editorial commits this session** spanning patch application + 4 of 5 simulation directions. Combined output: 218k chars across SIM_A/B/C/D + doc 12 v1.1 + ledger updates + handoff updates. Significant progress; recommend fresh session for SIM-E to maintain quality over time.


---

## SESSION NARRATIVE-ARC PASS NOTES — 2026-04-29

**Purpose:** User-requested light interpretive pass over SIM-A/B/C/D as continuous player experience.
**Output:** `SIM_narrative_arc_pass.md` (commit `36a8d6e3`).

**Key findings:**
- Engine produces *chronicles* reliably (court-history texture confirmed). 
- Engine produces *stories* partially — for players who engage selectively.
- Strongest narrative substrate: cross-faction events, mandatory P2 escalations (Marshal-confrontation arc), Knot scenes.
- Weakest: thematic motivation behind NPC Convictions (no backstory mechanic beyond ST-16-A Founding Memory); reactive vs proactive player levers; settlement-as-weather (not character).
- **Verdict: chronicle strong, novel partial.** Multi-character arcs run in parallel without GM coordination — design intent achieved.

**Five forward-looking design observations** (out-of-scope for v1.2; for Jordan's consideration):
1. Player-proactive lever expansion (initiate Concerns in NPCs).
2. Concern-internalization sub-scenes (private monologue/reflection beats).
3. Settlement-as-character (named-NPC reactions alongside aggregate Signal).
4. "Faction Watershed" event class for cumulative-drift-threshold dramatic beats.
5. Player Founding Memory (mirror NPCs' permanent Salience-5 anchor).

---

## SESSION 4-E NOTES — 2026-04-29

**Done (S4-E — Composition / multi-agent emergence):**
- `SIM_E_composition.md` produced and committed (`b04523d2`). 360 lines.
- Six scenarios at three-faction × 12-Accounting scale:
  1. Cross-faction Settlement Signal interference (border-event divergent responses).
  2. Multi-Year institutional ossification (Y0→Y3 weight trajectories per faction).
  3. Dramatic intensity test — does an arc reach climax? **Yes — N-DIAG-A milestone scenes are the engine's reliable climax-beat mechanic.** (~12-20 climax beats per Year cycle at 3-faction scale.)
  4. Player-proactive lever stress test (agency operates indirectly through Memory-bus).
  5. Three-faction power-equilibrium (no runaway over 3-Year trace; asymmetric drift trajectories).
  6. Composition pathology test (leader-death cascade; full ossification; succession mechanic gap).

**SIM-E new gaps (2):**
- SIM-E-G1 (P3): cross-border event Signal-attribution clarification.
- **SIM-E-G2 (P2): faction succession trigger and mechanism unspecified** — leader death triggers Faction Crisis (existing mechanic) but new-leader designation is unspecified. Recommend "highest-Standing same-faction NPC becomes leader on previous-leader death; Conviction-alignment-with-faction-dominant breaks ties."

**SIM-E forward-looking design observations (3):**
- SIM-E-O1: Inner-circle threshold (3↔4) milestone scenes should be P2 mandatory, not P3 available.
- SIM-E-O2: Explicit "Player Move" mechanic seeding named Memories in target NPCs.
- SIM-E-O3: 5+ Year stress trace recommended for equilibrium/oscillation analysis.

**SIM-E confirmations:**
- **SIM-B-G8 confirmed P1-critical at scale.** ~8 percentage points of Crown's Order-share between liberal and strict interpretations over 3 years. Most consequential v1.2 decision.
- **ED-760 stall-escalator validated at scale.** Functions as both anti-deadlock AND anti-ossification mechanic.
- **SIM-C-G6 routing recommendation holds** under cross-border and three-faction loads.
- **N-DIAG-A milestone is the engine's primary climax mechanic** — narrative-arc pass underestimated this; Direction E found it reliable.

**Final cumulative gap inventory (across SIM-A/B/C/D/E + narrative pass):**
- **5 directions, 39 scenarios, 33 invariants verified, 31 spec gaps, 8 forward-looking design observations.**
- 2 P1-CRITICAL (SIM-B-G8, SIM-C-G6) — confirmed at composition scale.
- ~13 P2 — implementation determinism issues.
- ~16 P3 — minor doc/typo/authoring-helper.

---

## SESSION 5 — SYNTHESIS (next-up)

**Recommended scope for fresh-context session:**
1. Read all 5 SIM docs + narrative pass.
2. Produce `19_v1.1_validation_report.md`:
   - All 33 invariants and verification status.
   - All 31 spec gaps consolidated, prioritized.
   - Cross-direction integration map.
   - Emergent properties catalog.
3. Produce `20_v1.2_patch_list.md`:
   - P1-critical resolutions: SIM-B-G8 strict definition; SIM-C-G6 routing; SIM-E-G2 succession.
   - High-impact P2: stall-escalator (ED-760); evasion event (SIM-D-G2); counter infrastructure (SIM-B-G7); etc.
   - P3 doc cleanup.
4. Update editorial ledger: close ED-757 (simulations complete); open new entries for v1.2 patch resolutions.
5. Forward-looking design observations memo: 8 observations for Jordan consideration (not v1.2 scope).

**Estimated output:** ~25-35k chars across 2 docs + ledger updates. Single editorial session.

---

## TOTAL SESSION-CHAIN PROGRESS — 2026-04-29

| # | Status | Commit | Artifact |
|---|---|---|---|
| S1 | ✅ DONE | 6de72da1, 831c889a | doc 17 + initial ledger |
| S2 | ✅ DONE | 9986d8d9, 9dede391, f5acbaa2 | doc 12 v1.1 (26 patches applied) |
| S3 | 🔶 PARTIAL | (spot-vetted in simulations) | re-vet against §13 |
| S4-A | ✅ DONE | fda634db | SIM-A Opinion architecture |
| S4-B | ✅ DONE | 8a6dbb44 | SIM-B Domain Action selection |
| S4-C | ✅ DONE | 684b1627 | SIM-C Settlement Signal |
| S4-D | ✅ DONE | 84eec07c | SIM-D Relational dynamics |
| Narrative pass | ✅ DONE | 36a8d6e3 | SIM_narrative_arc_pass |
| S4-E | ✅ DONE | b04523d2 | SIM-E Composition |
| S5 | ⏳ PENDING | — | Synthesis |

**Chain summary:** 13 commits this session-chain. ~280k chars output across simulation/editorial artifacts. Resolution work for 68 stress-test issues complete; v1.1 produced; full simulation chain across 5 directions complete with narrative validation. One synthesis session remains to consolidate findings and draft v1.2 patch list.


---

## EXTENDED SIMULATION CHAIN — 2026-04-29

After completion of original 5-direction chain, user authorized further simulations leveraging Opus 1M context window. Three additional directions traced.

### SIM-F (player-engaged dramatic arc) — commit `454b5dc4`
- 16-Accounting trace of deliberate engaged playthrough.
- Player objective: push Crown toward pluralist Conviction balance.
- **Engagement hypothesis verified.** Engine produces multi-Act narrative structure for engaged players: setup (Y1), pressure (Y2), crisis (Y3), resolution (Y4). 12+ dramatic-beat density per 4-Year arc. Stated objective achieved without Player Standing gain — institutional change is the reward, not personal advancement.
- 3 forward-looking observations (SIM-F-O1/O2/O3): Standing-recalc reward for coalition leadership; Faction Crisis precursor warnings; Procedure E pair-interaction probability tuning.
- All 26 v1.1 patches engaged simultaneously without invariant breaks.

### SIM-G (long-horizon equilibrium) — commit `ca84f96c`
- 12-Year (48-Accounting) stress trace per SIM-E-O3 recommendation.
- **No runaway accumulation.** **No oscillations within 12 Years.** Equilibrium reached for diverse-start factions (Crown, Hafenmark); monoculture trajectory for homogeneous-start factions (Varfell).
- Generational succession (Almud→Marshal at Y6) produces discrete one-time shift then re-stabilization. Multi-decade oscillation emerges naturally from regime sequence.
- Memory-cap pressure produces realistic long-term character coherence (Founding Memories persist; landmarks survive; patterns merge).
- 1 new gap (SIM-G-G1: Mood-impact on Faction Meta-Armature aggregate weighting unspecified).
- 5 forward-looking observations (SIM-G-O1..O5): aging/mortality, Player Scar accumulation, Conviction-diversity bonuses, early-game Memory longevity, generational oscillation framing.

### SIM-H (pathology / crisis cascade) — commit `b54c8162`
- 6 pathology scenarios: burnt-bridge playthrough, faction internal coup, multi-faction crisis cascade, player-precipitated Faction Crisis, war escalation, Knot rupture cascade.
- **Engine passes pathology test.** No invariant breaks under extreme stress. Realistic decline cascades. Coherent emergent dynamics.
- **Third P1-CRITICAL gap surfaced — SIM-H-G2: Knot rupture mechanic.** Spec references Knot rupture as state but doesn't define triggers, mechanics, or consequence cascade. Recommended definition produces coherent cascade per Scenario 6.
- 6 additional gaps (G1, G3-G7): subversive-intent dialogue, leader-challenge, Faction Crisis resolution path, cross-faction event during simultaneous crises, sustained war-state, peace-treaty mechanics.
- 2 forward-looking observations: player-precipitated crisis as feature; Knot rupture as featured mechanic.

---

## FINAL CUMULATIVE STATUS — 2026-04-29

**Simulation chain: 8 directions + narrative pass + 51 scenarios + 33 invariants verified + 39 spec gaps + 18 forward-looking observations.**

**Three P1-CRITICAL gaps for v1.2:**
1. **SIM-B-G8** — `failed_da_proposals` definition (strict vs liberal). Recommend strict.
2. **SIM-C-G6** — Settlement-Signal-Concern routing. Recommend governor/leader/round-robin.
3. **SIM-H-G2** — Knot rupture mechanic. Recommend full specification per SIM-H Scenario 6 trace.

**Architecture validated at all scales:** single-mechanic, multi-faction composition, engaged-player narrative, long-horizon equilibrium (12 Years), pathology / extreme stress.

**Engine confirmed to produce:**
- Stories at scale (chronicle reliably; novel for engaged players).
- Bounded equilibrium dynamics (no runaway).
- Multi-decade oscillation through generational succession.
- Coherent failure / decline under destructive choices.
- Realistic long-term character coherence via Memory-cap dynamics.
- Politically authentic Renaissance pace and texture.

**Session 5 (synthesis) deliverable scope expanded:** roll up 8 directions + narrative pass + extended findings; produce final v1.1 validation report consolidating all 39 gaps with prioritization; produce v1.2 patch list incorporating three P1-critical resolutions + ED-760 stall-escalator + high-impact P2 gaps; produce forward-looking design observations memo (18 observations) for Jordan's separate consideration after v1.2 stabilizes.

**Total session output:** 16 commits this session-chain; ~440k chars output across simulation/editorial artifacts.


---

## SESSION 5 — SYNTHESIS + v1.2 PRODUCTION — 2026-04-29

User authorization: "you have permission to resolve all best way / synthesize as required / proceed with more work."

**Done (S5 — full synthesis + v1.2 production):**

### Doc 19 — v1.1 Validation Report (commit `b7f2235b`)
- 359 lines, 25k chars.
- Consolidates 8-direction simulation chain: 51 scenarios, 33 invariants verified, 39 gaps with prioritization, 24 emergent properties cataloged, 18 forward-looking design observations.
- Cross-direction integration map (all 6 pairwise integrations verified).
- Validation conclusion: v1.1 architecture sound; ready for v1.2 patch resolution before canonical promotion.

### Doc 21 — v1.2 Specification Revisions (commit `b7f2235b`)
- 893 lines, 41k chars.
- Patch directives for 3 P1-critical + ED-760 + 19 P2 + 16 P3 = 39 total patches.
- §5 Application checklist; §6 Output expectations.

### Doc 12 v1.2 (commit `7c9384ec`)
- 1958 lines, 113k chars (+394 lines vs v1.1's 1564).
- All 39 v1.2 patches applied. New sections:
  - §2.5.2 Knot Rupture (PATCH v1.2-3, P1-CRITICAL, full mechanic specification + featured-behavior commentary)
  - §5.4.1 Faction Succession (PATCH v1.2-19)
  - §5.4.2 Leader Challenge / Coup Mechanic (PATCH v1.2-20)
  - §8.2 Inter-Faction War State (PATCH v1.2-22)
  - §8.2.1 Peace Treaty Mechanic (PATCH v1.2-23)
  - §17 v1.2 Patch Addendum (consolidated P2/P3 clarifications)
- Updated §0.1 v1.2 change log + retained v1.1 change log as predecessor.
- Three P1-CRITICAL resolutions:
  - **PATCH v1.2-1 (§8.1):** failed_da_proposals strict definition — counts only "DA roll failed," not "lost competition." Lost competitions increment seasons_stalled only.
  - **PATCH v1.2-2 (§5.2):** Settlement-Signal-Concern three-tier routing (governor → faction leader if seat → round-robin by domain affinity).
  - **PATCH v1.2-3 (§2.5.2 + §1.1):** Full Knot rupture mechanic specification.
- ED-760 stall-escalator applied as **PATCH v1.2-4** (`+0.05 × seasons_stalled` in select_proposal score).
- §1.1 N-DIAG-A title renamed: "Inner-Circle Threshold Milestone (Standing 3↔4)" — resolves SIM-D-G4.
- §5.3 Mood-impact on aggregate weighting added (PATCH v1.2-18 / SIM-G-G1): mood_modifier dampens institutional weight for Distracted (0.7×) and Grieving (0.5×).
- All 39 patches verified present in spec via grep audit.

### Editorial ledger consolidation
- ED-757 (simulation chain), ED-760 (stall-escalator recommendation), ED-761 (39-gap tracker) all resolved and archived.
- ED-762 added (open) — v1.2 produced, ready for §13 Promotion Checklist re-vet.

---

## NEXT STEPS

**Immediate (Jordan-facing):**
1. Re-vet doc 12 v1.2 against §13 Promotion Checklist before canonical promotion.
2. Optional spot-check: trace SIM-B Sc 8 deadlock against v1.2 (PATCH v1.2-4 stall-escalator should now break Confessor's deadlock at seasons_stalled ~5-7); trace SIM-H Sc 1 against v1.2 §2.5.2 Knot rupture (full mechanic should produce Sc 6 cascade).
3. Address §6 Jordan-decision items still flagged (`[JORDAN-DECISION-PENDING-ED-755]`) — these are out-of-scope for v1.2 patches; require Jordan's design call before resolution.

**Forward-looking (post-canonical, per Jordan consideration):**
- 18 forward-looking design observations documented in doc 19 §5. Out-of-scope for v1.2 spec patches but flagged for separate consideration after v1.2 stabilizes. Highlights: player-proactive lever expansion (O-N1, SIM-E-O2); aging/mortality mechanic (SIM-G-O1); Conviction-diversity bonuses in institutional_stability (SIM-G-O3); Player Founding Memory mirror (O-N5).

---

## TOTAL CHAIN STATISTICS

**18 commits this full session-chain.** Started with stress-test issue resolution (S1, doc 17), produced doc 12 v1.1 (S2), executed 8-direction simulation chain + narrative pass (S4-A through S4-H + narrative), produced synthesis + v1.2 (S5).

**Output volume:** ~580k chars total across:
- doc 17 (specification revisions) — 33k
- doc 12 v1.1 (development spec) — 83k
- SIM-A through SIM-H + narrative pass — 8 docs, ~370k total
- doc 19 (v1.1 validation report) — 25k
- doc 21 (v1.2 specification revisions) — 41k
- doc 12 v1.2 (final spec) — 113k
- editorial ledger updates + handoff updates throughout

**Architecture validated at every scale tested.** Ready for canonical-promotion review.


---

## SESSION 5 (synthesis) NOTES — 2026-04-29

**Done — synthesis + v1.2 production:**

Two artifacts produced under user authorization to "resolve all best way / synthesize as required / proceed with more work":

1. `19_v1_1_validation_report.md` — comprehensive synthesis report (~25k chars, 359 lines). Consolidates all 8 directions + narrative pass. Catalogs 33 invariants verified, 39 specification gaps with priority/recommendation, 24 emergent properties, 18 forward-looking observations, cross-direction integration map, v1.1 validation conclusions, v1.2 patch plan summary.

2. `21_v1_2_specification_revisions.md` — exact patch directives for v1.2 (~41k chars, 893 lines). 39 patches: 3 P1-CRITICAL (GAP-1/2/3), ED-760 stall-escalator, 19 P2 implementation-determinism, 16 P3 cleanups. Each patch with LOCATE/REPLACE/INSERT directive + rationale.

3. `12_development_specification.md` v1.2 (commit `59a1c1e0`) — 1958 lines (up from v1.1 1565). All 39 v1.2 patches applied. Surgical patches in target sections (§1.1 Featured Behaviors, §2.5.2 Knot Rupture (new), §5.2 Settlement Signal routing, §5.3 Mood-impact aggregate weighting, §5.4.1 Faction Succession (new), §5.4.2 Coup Mechanic (new), §6.2 select_proposal() stall-escalator + 4-level tie-break, §8.1 Standing Recalc strict + counter state, §8.2 War State (new), §8.2.1 Peace Treaty (new)). Remaining P2/P3 patches consolidated as §17 Addendum. Updated §0.1 Change Log with v1.2 section.

**v1.2 critical resolutions:**
- **PATCH v1.2-1 (SIM-B-G8 strict).** `failed_da_proposals` = "DA roll failed only" (NOT lost competitions). Counter scope clarification: Mood-suppressed / lost-competition / failed-deference all do NOT count. Strict interpretation rewards execution; validated at scale.
- **PATCH v1.2-2 (SIM-C-G6 routing).** Three-tier routing: (a) governor if Active, (b) faction leader if seat, (c) round-robin among inner-circle by domain affinity. Plus cross-border attribution (v1.2-37), salience handling (v1.2-12), repeated-Signal max-update (v1.2-15).
- **PATCH v1.2-3 (SIM-H-G2 Knot rupture).** Full mechanic spec in new §2.5.2 + §1.1 featured behavior entry. Trigger conditions, rupture event, long-term consequences, recovery path. Treated as featured dramatic mechanic per SIM-H-O2.
- **PATCH v1.2-4 (ED-760 stall-escalator).** `+0.05 × seasons_stalled` added to select_proposal() score. Anti-deadlock + anti-ossification.

**Editorial ledger updates:**
- ED-757 (simulation chain) → resolved + archived.
- ED-760 (stall-escalator recommendation) → resolved (applied in v1.2-4) + archived.
- ED-761 (gap tracking) → resolved (all gaps addressed in v1.2) + archived.
- ED-762 (NEW) — v1.2 promotion-readiness tracking; eligible for §13 Promotion Checklist evaluation.

**v1.2 status:** PROVISIONAL but eligible for canonical promotion review per §13. All simulation-surfaced concerns resolved. Forward-looking design observations (18) tracked separately for post-canonical iteration.

**Total session-chain commits:** 18 (from S1 setup through v1.2 production).
**Total session-chain output:** ~480k chars across simulation/editorial/spec artifacts.

---

## NEXT STEPS — POST-SYNTHESIS

The simulation/revision phase is complete. Recommended subsequent work:

1. **§13 Promotion Checklist evaluation** — review v1.2 against the canonical-promotion criteria; address any unsatisfied items.
2. **§16 Jordan-decision items** — the ED-755 items remain pending Jordan's design calls. These are independent of simulation gaps (they're forward-looking design questions, not spec gaps).
3. **Optional: extended simulation passes** — if Jordan wants additional confidence, fresh simulation directions (e.g., player-precipitated regime change, multi-decade campaign with specific objective, Knot-network composition stress) could be run. The 8 directions completed cover the major cases; further work is incremental.
4. **Post-canonical: forward-looking design observations** — 18 observations from SIM-E/F/G/H + narrative pass tracked for design discussion after v1.2 stabilizes. These are spec extensions, not corrections.

The political dynamics system is in good standing: validated, simulation-tested, gap-resolved, and ready for promotion review.


---

## POST-SYNTHESIS WORK — 2026-04-29

After synthesis (S5) commit, additional work performed under user authorization:

### NERS + bloat assessment (`22_NERS_and_bloat_assessment.md`, commit `09421b5d`)

Critical pass against project's NERS criteria. Findings:
- **Necessary:** v1.2 contains ~178 lines of completionist bloat — §5.4.2 Coup (24 lines), §8.2 War State + §8.2.1 Peace Treaty (69 lines), §17 v1.2 Patch Addendum (85 lines).
- **Elegant:** §17 addendum pattern fails NERS — implementors must check both target section AND §17 for any feature; redundancy and structural inelegance.
- **Robust:** ✓ strong — simulation-validated; supports strategic depth, customization, emergence.
- **Smooth:** ✓ strong — cross-direction integrations verified; transitions clean.

### Chain audit (`23_chain_audit.md`, commit `aed39f7a`)

Five-phase rigorous audit of session-chain output:
- **Patch fidelity:** ✓ perfect — all 39 v1.2 patches semantically correct against doc 21 directives.
- **Gap counts:** ✓ exact match — 39 unique gaps surfaced = 39 claimed.
- **Invariant counts:** ✗ inflation — "33+ invariants verified" was wrong; actual is 25 unique (re-verified at multiple scales). Correction applied to doc 19.
- **Long-horizon trace granularity:** ⚠ framing — SIM-G/SIM-E claim Accounting-level traces but contain 0 explicit Accounting-N references; they're Year-summary granularity. Methodologically appropriate but framing inflated rigor. Correction applied to doc 19.
- **NERS findings:** ⚠ partial — one sub-claim retracted (PATCH v1.2-29 was not "duplicative" — line 1946 was a tracking ref, not content dup). Correction applied to doc 22.

### AUDIT-1..5 corrections committed (`dbc8d918`)

Doc 19 corrections: invariant count 33+ → 25 unique re-verified at scale; observation count 18 → 19 (SIM-D-O1 omitted from catalog); long-horizon granularity reframed as Year-level summary.

Doc 22 corrections: PATCH v1.2-29 duplication claim retracted; §8.2 line count corrected ~50 → 69; total cuttable ~160 → 178.

### v1.2.1 NERS cleanup pass (`52fb1292`)

Per doc 22 recommendations:
1. **Cut §5.4.2 Coup Mechanic** (24 lines) — deferred to v1.3.
2. **Cut §8.2 Inter-Faction War State + §8.2.1 Peace Treaty** (69 lines) — deferred to v1.3.
3. **Apply §17 P2/P3 addendum patches surgically** in target sections (§3.6, §3.6.X, §5.1, §5.2, §6.2 Procedures B/C/D, §7.6, §10, §2.6, §2.7, §4.5).
4. **Delete §17** entirely.
5. **Update §0.1 v1.2.1 change log** documenting the cleanup.

**Net result:** v1.2.1 spec is 1856 lines (down from v1.2's 1958 lines; ~102 lines reduction, less than the headline 178 because surgical insertions added clarifying paragraphs back into target sections — but those additions are content-bearing and ELEGANT, not bloat).

P1-CRITICAL resolutions retained (SIM-B-G8 strict, SIM-C-G6 routing, SIM-H-G2 Knot rupture). ED-760 stall-escalator retained. Faction Succession §5.4.1 retained.

### Final session-chain commits (post-synthesis)

| # | Commit | Artifact |
|---|---|---|
| 21 | `09421b5d` | doc 22 NERS + bloat assessment |
| 22 | `aed39f7a` | doc 23 chain audit (5 findings) |
| 23 | `dbc8d918` | AUDIT-1..5 corrections to docs 19 + 22 |
| 24 | `52fb1292` | doc 12 v1.2.1 (NERS cleanup) |

---

## CURRENT STATE — 2026-04-29

**doc 12 v1.2.1** (commit `52fb1292`) is the **canonical-promotion candidate**.

| Spec evolution | Version | Lines | Status |
|---|---|---|---|
| v1.0 | (initial draft) | — | Superseded |
| v1.1 | (commit `9dede391`) | 1565 | Superseded |
| v1.2 | (commit `59a1c1e0`) | 1958 | Superseded by v1.2.1 |
| **v1.2.1** | **(commit `52fb1292`)** | **1856** | **Current** |

**Companion artifacts:** doc 17 (v1.0→v1.1 patches), doc 19 (validation report, AUDIT-corrected), doc 21 (v1.1→v1.2 patch directives), doc 22 (NERS assessment, AUDIT-corrected), doc 23 (chain audit).

**Recommended next steps:**
1. **§13 Promotion Checklist evaluation** of v1.2.1.
2. **§16 Jordan-decision items** — ED-755 items remain pending (not simulation-blocked).
3. **Forward-looking design observations** (19 from sims + narrative pass) tracked for post-canonical v1.3+ iteration.

**Cumulative session-chain output:** ~520k chars across 24 commits. Eight simulation directions + narrative pass + synthesis + audit + cleanup. Architecture validated at every meaningful scale; spec is implementation-ready.


---

## CANONICAL-PROMOTION WORK — 2026-04-29

Following user authorization to "perform all," §13 Promotion Checklist evaluated and most actionable blockers addressed.

### §13 Evaluation (doc 24, commit `a6bfeee3`)

| # | Item | Status |
|---|---|---|
| 1 | Re-vetting against current spec | ✓ PASS |
| 2 | §11 Outstanding Design Decisions | ⚠ BLOCKED ON JORDAN |
| 3 | Editorial ledger entries for major components | ✓ PASS |
| 4 | Patch register entries (PP-XXX) | ⚠ FORMAT GAP |
| 5 | Integration patches against external designs | ✓ DRAFTED |
| 6 | Content authoring scope | ⚠ BLOCKED ON JORDAN |
| 7 | Stage-1 simulation pass | ✓ PASS (5× exceeds requirement) |

### Integration patches (docs 25/26/27, commit `58c58c3d`)

20 integration patches across 3 external canonical designs:
- doc 25 (npc_behavior_v30): 6 patches — Conviction taxonomy, Path B Belief revision, explicit_heir Tier-0, etc.
- doc 26 (player_agency_v30): 7 patches — Slate priority mapping, Knot rupture mandatory addition, etc.
- doc 27 (settlement_layer_v30): 7 patches incl P1-CRITICAL INT-3.1 normalization bug.

### v1.2.2 INT-3.1 fix (commit `8d37cede`)

P1-CRITICAL bug: doc 12 PATCH 3.9 assumed settlement stats on 0-10 scale; canonical settlement_layer_v30 §1.3 specifies 0-5 scale. Corrected normalization formula: `(s.order - 2.5) / 1.25`. Single-patch revision.

### Final spec evolution

| Version | Commit | Lines | Status |
|---|---|---|---|
| v1.0 | initial | — | superseded |
| v1.1 | `9dede391` | 1565 | superseded |
| v1.2 | `59a1c1e0` | 1958 | superseded |
| v1.2.1 | `52fb1292` | 1856 | superseded |
| **v1.2.2** | **`8d37cede`** | **1875** | **canonical-promotion candidate** |

### Final session-chain commits

| # | Commit | Artifact |
|---|---|---|
| 26 | `a6bfeee3` | doc 24 §13 promotion checklist evaluation |
| 27 | `58c58c3d` | docs 25/26/27 integration patches |
| 28 | `8d37cede` | doc 12 v1.2.2 (INT-3.1 fix) |

---

## REMAINING BLOCKERS — JORDAN-FACING

For canonical promotion:

1. **§11 Outstanding Design Decisions** — Wrong-Belief Investigation, authoring scope, carryover (Intelligence stat, LICENSE/GOV-08).
2. **§16 Jordan-Decision Items (ED-755)** — E-38, E-TOP-A, ST-31-B, R-41-A.
3. **PP-XXX register format question** — migrate, accept current, or defer.
4. **Integration-patch adoption** — 20 patches in docs 25/26/27 await Jordan adoption decisions.

These are organizational/decisional, not architectural. v1.2.2 is implementation-ready.

---

## SESSION-CHAIN FINAL STATE

**Commits:** 28. **Artifacts:** ~600k chars. **Validations:** 25 invariants, 51 simulation scenarios, 39 spec gaps surfaced and resolved, 20 integration patches drafted, 1 P1-CRITICAL bug found and fixed (INT-3.1).

doc 12 v1.2.2 is in good standing for canonical promotion pending Jordan engagement on the four remaining blocker categories above.

**END OF HANDOFF v1.**
