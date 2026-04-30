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
| 2 | PENDING | Apply doc 17 patches → produce doc 12 v1.1 | `12_development_specification.md` v1.1 with all 48 patches applied |
| 3 | PENDING | Re-vet v1.1 against §13 promotion checklist | Vetting report; flag any patch that breaks invariants |
| 4 | PENDING | Simulation pass — Direction A (Opinion architecture) | Granular interaction map for B/C/D Procedures + Knowledge→Concern→Action chain |
| 5 | PENDING | Simulation pass — Direction B (Domain Action selection) | Trace alignment-table + scar-cap + conviction-multiplier interactions |
| 6 | PENDING | Simulation pass — Direction C (Settlement/Faction signal flow) | Settlement Signal → Concern → Domain Action propagation |
| 7 | PENDING | Simulation pass — Direction D (Relational dynamics) | Standing recalc, Outreach, Knot integration, Memory accumulation |
| 8 | PENDING | Simulation pass — Direction E (Composition / cross-system) | Multi-agent trace; emergent behaviors at faction scale |
| 9 | PENDING | Simulation synthesis | Roll-up findings; surface unresolved interactions for v1.2 |

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

**END OF HANDOFF v1.**
