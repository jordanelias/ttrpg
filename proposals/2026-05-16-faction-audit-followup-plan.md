# Faction Audit Follow-Up Plan

## Status: SUPERSEDED / OBSOLETE — process plan; Phase-0/1 closed same-day, Phase-2 Jordan decisions never taken, ground since covered by the 2026-07-08/09 comparative-governance-research lineage. Archive candidate (2026-06-28 currency sweep, Bucket B). [## Status: heading added 2026-07-15]

**Date:** 2026-05-16
**Status:** PROVISIONAL — proposal-of-process; Jordan-approval-gated for execution
**Source audit:** `designs/audit/2026-05-16-faction-ners-all-directions.md` (commit ffb1e57)
**Scope:** address 17 findings (A-1..A-17) + 2 carry-forwards from the faction NERS audit of PP-686 v2 architecture + faction layer + adjacent systems
**Authority:** plan proposes structure; Jordan approves Phase 2 decisions, Phase 3 documentation, and each Phase 4 proposal individually per `throughlines_meta §10`

---

## §0 Plan framing

This plan is a worklist of next-step actions on the 17 audit findings. Each finding resolves to one of five **response modes**:

- **VERIFY** — fetch unread canon to confirm/refute the finding; may close as "already done"
- **PROPOSE** — draft a mechanic addition or refinement; Jordan approves before commit-to-canonical
- **DOCUMENT** — write a clarifying paragraph in canonical docs; no mechanical change
- **DECIDE** — Jordan-only; framing question with options, not a recommendation
- **MAINTENANCE** — run an existing tool / fix infrastructure already flagged

**This plan is the structured option.** Jordan may execute findings ad-hoc as bandwidth permits — the plan is not a binding commitment, and many findings may close on Phase 1 verification without further work.

**Plan structure as template.** The 5-phase dependency-graphed format is heavier than typical workplan docs (`engine_ners_2026-05-15.md` used flat U-1..U-9 worklist). Retained here because dependency-blocking relationships exist (D-2.3 → PC-4.1, PC-4.5; D-2.1 → PC-4.2) that flat lists hide. May serve as template for future multi-finding audits; may also be flattened if process weight proves unhelpful.

---

## §1 Worklist (20 items)

### Phase 0 — Maintenance (parallel; no design judgment)

| ID | Source | Sev | Deliverable | Authority |
|---|---|---|---|---|
| M-0.1 | A-10 | P3 | Run `freshness_gate.py --update`; refresh 4 stale canonical sources flagged by bootstrap | Tooling — Claude executes |
| M-0.2 | carry-fwd | P2 | Run editorial_ledger atomizer (`archive_by_status`); archive resolved ED entries to dated archive; verify ledger drops below 4k token threshold | Tooling — Claude executes |

### Phase 1 — Verifications (close-or-escalate)

Each is a bounded fetch task. Outcome modes: **CLOSE** (finding resolves on full read), **REFRAME** (smaller than stated), **ESCALATE** (becomes Phase 4 proposal).

| ID | Source | Sev | Read | Determine | Expected outcome |
|---|---|---|---|---|---|
| V-1.1 | A-5 | P3 | `faction_politics_v30.md` full · `factions_personal_v30.md` full | Default visibility of faction stats | Likely CLOSE if strategic-fog already in canon per `faction_stats_renaissance_review` recommendations |
| V-1.2 | A-6 | P3 | (same files as V-1.1) | Coalition cost structure | Unknown — depends on alliance mechanics in `faction_politics_v30` |
| V-1.3 | A-11 | P3 | `victory_v30.md` full | Post-victory-impossibility persistence path | Unknown |
| V-1.4 | A-15 | P2 | `params/factions.md` full (2,961 chars, already fetched) · `settlement_layer_v30.md` full · `mass_battle_v30.md` | Wealth-generation mechanism — production, trade, taxation, upkeep | **Likely CLOSE — `params/factions.md` likely contains wealth flow; A-15 was outside-review finding made without full read.** If genuinely absent at architectural level → Class A canonization trigger, Jordan-decision before draft. |
| V-1.5 | A-16 | P2 | `ci_political_v30.md` full | Church-as-territorial-power dimension | Likely REFRAME — `valoria_political_hierarchy_v30` (already read) shows Church territorial entries; full `ci_political_v30` likely covers territorial mechanism |
| V-1.6 | A-17 | P3 | `campaign_architecture_v30.md` · `arc_expansion_v30.md` | Offstage / extra-peninsular factional pressure scope | Likely CLOSE / DOCUMENT-SCOPE — Valoria appears intentionally peninsula-bounded |
| V-1.7 | M-1 | P3 | `conviction_taxonomy_v30.md` (PP-684) · `key_substrate_v30.md` (PP-687) | Personal-scale ↔ faction-scale Conviction flow soundness (needed to fully verify §5.2 bottom-up chain from audit) | Verification — closes audit `[GAP]` on PP-684/PP-687 unread |

**Phase 1 checkpoint (per M-7 / O-2):** if ≥3 verifications close as "already done," re-evaluate whether Phase 4 needs full proposal structure or compresses to 2 items. Document closure verdicts inline in this plan when each verification completes.

### Phase 2 — Jordan decisions (frame, not recommend)

Each is a question with options labeled α/β/γ. Claude does not pick.

**D-2.1 — Candidate М-12: regime-relative category mutation** (from A-7)
- *Question:* Is cross-faction rule-space mutation (private war → treason as crown centralizes) a meta-throughline warranting М-12, or is distributed coverage across Mission-shift + CI + Excommunication sufficient?
- *Option α:* Admit М-12. Becomes 12th meta-throughline; triggers Class A canonization work per `throughlines_meta §8.1` — formal Μ-mode mapping, Τ-anchor identification, vetting block, sim battery design.
- *Option β:* Document distributed sufficiency. Add §10.x to `throughlines_meta.md` explaining why М-1..М-11 cover the dynamic; close A-7; A-2 proceeds standalone.
- *Option γ:* Scope-bound deliberately. Acknowledge dynamic exists in source material but is not modeled at faction layer; document boundary in `canon_constraints` or `intent_of_game.yaml`.
- *Authority:* Jordan-owned (М-additions per `throughlines_meta §10`).
- *Blocks:* PC-4.2 (political hierarchy mutability) — final form depends on this decision.

**D-2.2 — Candidate М-13: recognition as substrate-state constitution** (from A-8)
- *Question:* Is faction-to-faction recognition (diplomatic acknowledgment as constitutive of position) a meta-throughline warranting М-13, or is distributed coverage across М-3 + М-4 + М-8 sufficient?
- *Options α/β/γ:* mirror D-2.1 structure (admit / document distributed sufficiency / scope-bound).
- *Authority:* Jordan-owned.
- *Blocks:* nothing in Phase 4 directly; affects V-1.1 scoping (if М-13 admitted, strategic-fog mechanics may attach to recognition graph).

**D-2.3 — P-01 Inseparability / DA-as-thread-operation canon-check** (from A-9, P1-candidate)
- *Question:* Is faction Domain Action a thread operation under P-14 (Board/VG modes must express inseparability)?
- *Option α — Yes, DA is thread op.* P-01 three-dimensional auto-effects (temporal CD, epistemic certainty, actualized d6 consequence) must fire on every faction DA. `faction_behavior_v30 §3.7` is incomplete; requires DA Ob calculation revision. P1 finding stands; append to `editorial_ledger.yaml` after M-0.2.
- *Option β — No, DA is not thread op.* P-14 boundary needs explicit documentation: "thread operations are scene-level character actions; faction DA is a higher-aggregation mechanic with its own compliance regime." P-01 does not apply. A-9 closes; PC-4.1 and PC-4.5 proceed without P-01 dependency.
- *Option γ — Hybrid.* Some DA categories are thread ops; others not. Requires per-category mapping in `key_type_registry`.
- *Authority:* Jordan-owned (P-01/P-14 are tier-N constraints).
- *Blocks:* PC-4.1 (Legitimacy × Military interaction) and PC-4.5 (key-registry change protocol) — both need to know whether P-01 applies.

**D-2.4 — Generational / dynastic compounding scope** (from A-3, reclassified from PC-4.3 per authority correction)
- *Question:* Should multi-season dynastic compounding (decade-scale marriage strategy producing claim-strength accumulation, Habsburg-pattern) be mechanically modeled or scope-bound?
- *Option α — Mechanical:* Add slow-burn dynastic-claim accumulator. Mutual claim-strength accrues over N seasons between marriage-aligned factions; at threshold, claim becomes actionable. Substantial new mechanical surface.
- *Option β — Scope-bound:* Document Valoria campaign time horizon as multi-season but not multi-decade; generational compounding is below mechanical resolution. Paragraph in `intent_of_game.yaml` or `campaign_architecture`.
- *Authority:* Jordan-owned (campaign-time-horizon question — Ω-tier).
- *Blocks:* nothing.

**Phase 2 timing note (per O-3):** the dependency graph captures *what blocks what*, not expected duration. Jordan decisions in Phase 2 likely resolve in a single conversation each.

### Phase 3 — Documentation (parallelizable with Phase 1; no mechanical change)

| ID | Source | Sev | Deliverable | Target file |
|---|---|---|---|---|
| DOC-3.1 | A-13 | P2 | Add §0 or §10 to `faction_behavior_v30.md` naming "hybrid asymmetric" as design intent: shared mechanics layer (stats, four-component model, Accounting cycle) + asymmetric layer (roles, Unique Actions, role-specific tracks). Cite this audit as source. | `designs/provincial/faction_behavior_v30.md` |
| DOC-3.2 | A-14 | P3 | Add stat bucketing to `stats_1_7_scale.md` per ED-830 / `derived_stats_v30 §14` 4-bucket taxonomy. Verify §14 placement before commit. | `params/factions/stats_1_7_scale.md` |
| DOC-3.3 | B-2 | P3 | Add design-principle note: "0-floor stats (Legitimacy, Popular_Support, Mandate) are erodable to zero with mechanical consequence — full procedural revocation. 1-floor stats (Influence, Wealth, Military, Intel, Stability) are persistent — capacity that does not nullify." | `params/factions/stats_1_7_scale.md` or `faction_behavior_v30.md §2` |

### Phase 4 — Mechanic proposals (Class B patch register; conditional on Phase 2)

Each becomes a `proposals/PP-NNN-*.md` entry with vetting block per PP-674. Candidate IDs `PC-N`; assigned PP-N at Jordan approval. **Each PC-4.x advances from proposal → PROVISIONAL canon only after sim battery PASS; remains PROVISIONAL pending Class A vetting per PP-674; reaches CANONICAL on Jordan ratification** (per M-4).

**Intra-phase priority** (per O-7): high-value first.

**PC-4.4 (priority 1) — Unified success-induced stress mechanism** (from A-4; reordered per M-3 / O-4)
- *Lead proposal:* Single generalized "success-induced stress" formula applied to all six roles with role-specific consequences, NOT 5 separate mechanics.
- *Formula sketch:* when a role's primary advantage stat exceeds threshold for N consecutive seasons, faction emits a `mechanical.success_stress` Key; role-specific consequences fire (Crown → bureaucracy independence Ob+, Church → schism risk roll, Hafenmark → oligarchic capture, Varfell → paranoid Cascade Strictness shift, Restoration Movement → Mission Strictness increment, Löwenritter → already has coup trigger; verify compatibility).
- *Files touched:* `faction_behavior_v30.md` (new §3.X), `params/factions/stats_1_7_scale.md` (role-specific consequence table)
- *Dependency:* none direct
- *Alternative R-form:* per-role narrow triggers (the 5 sub-proposals from Pass 2) — fall back to this only if unified formula fails sim battery
- *Sim battery (proposal-level sketch — full design in patch register entry):* 6 simulation runs (one per role); verify stress mechanism fires within reasonable timeframe under aggressive play; never fires under conservative play; consequence severity scales with stat magnitude
- *Priority basis:* P2; addresses largest research-grounded gap (T-7 turn-on-you across all roles); high subject N

**PC-4.1 (priority 2) — Legitimacy × Military interaction rule** (from A-1)
- *Proposal:* Combined-axis gating for consolidator-class actions. Crown's `Royal Decree` Unique Action requires `Legitimacy + Military ≥ X` (or `min(Legit, Military) ≥ X`); failure of either axis fails the action. Models Henry-VII / Louis-XI / Ferdinand consolidator profile per audit T-2.
- *Files touched:* `params/factions/stats_1_7_scale.md` (Unique Action gating), `faction_behavior_v30.md §3.7` (DA Ob if interaction generalizes beyond Royal Decree)
- *Dependency:* **D-2.3 — if DA is thread op, interaction rule must engage P-01 three-dimensional auto-effects**
- *Alternative R-form:* per-action narrow gating vs. generalized DA Ob bonus when both axes ≥ threshold
- *Sim battery (sketch):* 9 starting profiles (Legit ∈ {2,4,6} × Mil ∈ {2,4,6}); measure victory-track progress; consolidator profiles should outperform single-axis profiles
- *Priority basis:* P2; T-2 is foundational Renaissance dynamic

**PC-4.2 (priority 3) — Political hierarchy mutability** (from A-2; conditional on D-2.1)
- *Proposal:* Identify positions in `valoria_political_hierarchy_v30.md` that are faction-mutable (contestable and capturable) vs. authored-fixed (campaign scaffold). Likely vassal-suzerain edges between Crown and noble houses mutable; geographic structure fixed.
- *Files touched:* `designs/territory/valoria_political_hierarchy_v30.md` (annotate per-position mutability), possibly new `faction.captured_offices` schema field in `faction_behavior_v30 §2`
- *Dependency:* **D-2.1 — if М-12 admitted, this proposal folds into М-12 mechanism; if not, standalone**
- *Alternative R-form:* binary capture vs. fractional capture (mirror `fractional_province_ownership_v30` pattern)
- *Sim battery (sketch):* multi-faction contest for single office; verify non-degenerate outcomes (no stalemate, no instant-flip)
- *Priority basis:* P2; T-4 institutional-arena dynamic

**PC-4.5 (priority 4) — Key-registry change protocol** (from A-12)
- *Proposal:* Document subscription-pattern behavior on key registry changes. Specify: (a) new key types → graceful default for consumers; (b) deprecated key types → grace period + migration path; (c) schema changes → `schema_version` field with consumer-side migration.
- *Files touched:* `designs/architecture/key_type_registry_v30.md`, `key_substrate_v30.md`
- *Dependency:* **D-2.3 — if DA is thread op, key-registry changes interact with P-01 compliance**
- *Sim battery:* N/A (architecture-level documentation)
- *Priority basis:* P2; affects robustness of substrate-emit/consume pattern

---

## §2 Sequencing + batching (per M-5)

| Phase | Runs when | Parallel with |
|---|---|---|
| 0 Maintenance | Immediately | Phase 1, Phase 3 |
| 1 Verifications | Immediately | Phase 0, Phase 3 |
| 2 Jordan decisions | When Jordan available | Phase 1, Phase 3 |
| 3 Documentation | Immediately | Phase 0, Phase 1, Phase 2 |
| 4 Mechanic proposals | After Phase 2 decisions land for blocked items | sequential within phase |

**Strict blocks:**
- PC-4.1, PC-4.5 strictly blocked by D-2.3
- PC-4.2 strictly blocked by D-2.1
- A-9 P1 appendix to editorial_ledger strictly blocked by M-0.2

**Soft blocks (proceed but flag):**
- Phase 4 proposals may begin drafting before Phase 2 decisions land, but cannot finalize / commit until decisions resolve

**Phase 1 checkpoint** (per M-7): if ≥3 verifications close as "already done," re-evaluate Phase 4 scope.

---

## §3 Authority structure

Per `throughlines_meta §10`:

- **N / Ω / М changes** — Jordan owns. Plan flags candidates М-12, М-13 in D-2.1, D-2.2; does not auto-add.
- **Μ application** — Claude applies (rating per §3 rubric, ✓ / + / ◐ / ○).
- **Τ proposals** — Claude proposes; Jordan accepts/rejects. No new Τ proposed in this plan.
- **Class A canonization** — Jordan ratifies after PROVISIONAL period + sim PASS + vetting block per PP-674.
- **Class B patches** — each PC-4.x is Class B; Jordan reviews each individually; sim battery PASS required before promotion to CANONICAL.

**Plan does not:**
- Modify canonical files (only proposes modifications)
- Add ED entries autonomously (P1 candidate A-9 awaits decision + ledger atomization)
- Override authority on candidate М-12 / М-13 (decisions framed, not recommended)
- Implement in Godot (Μ̄ tier, dev team)

---

## §4 Plan limitations

Acknowledged limitations the plan does not pretend to solve:

**O-1 / capacity.** This is a two-person project. The 20-item structure scales but does not assume all items execute. Realistic expectation: Phase 0 + Phase 1 + Phase 3 complete in tight sequence; Phase 2 resolves as Jordan engages; Phase 4 executes selectively per priority order. Items not addressed become known technical debt, not silent failures.

**O-2 / findings-may-close.** The audit produced 17 findings, of which V-1.1, V-1.4, V-1.5, V-1.6 are flagged "likely CLOSE" in §1. If Phase 1 verifications resolve these, the active plan contracts to ~10 items. Plan should not be measured by completion rate against 20.

**O-8 / audit framework ≠ "what makes the game better".** Plan structure follows audit-finding-resolution logic. This is the user's requested framing. A separate "what would actually make the game better to play" plan would have different structure, prioritize playtest signal over audit findings, and possibly conclude that some audit findings are not gameplay-relevant.

**Audit-may-have-been-over-critical.** PP-686 v2 reached canonical with Stage 10 sim PASS. Producing 17 findings on a freshly canonical system, of which only 1 is P1-candidate, suggests either the audit is over-critical or the architecture is solid with mostly polish-level gaps. The plan does not retract any audit finding; that judgment belongs in Phase 1 verification outcomes, not in plan structure.

---

## §5 Meta-audit verdict (Pass 3 final)

| Axis | Verdict | Basis |
|---|---|---|
| **N** Necessary | **PASS** | Every plan item traces to an audit finding |
| **R** Robust | **PASS w/ reservations** | Most items surface alternatives; Phase 3 single-path appropriate; PC-4.4 unified-first-then-fallback now surfaces alternative R-form correctly |
| **S** Smooth | **PASS** | M-5 batching rule added; M-7 checkpoint added; strict-vs-soft blocks distinguished |
| **E** Elegant | **PASS** | 5-phase structure restatable; second-order effects predictable; PC-4.4 unified-formula complexity reduced from 5 sub-proposals to one with role-specific consequences |

**Aggregate Pass 3 meta-verdict: PASS. 7 Pass-2 meta-findings (M-1..M-7) addressed; 8 outside-review concerns (O-1..O-8) addressed where actionable, acknowledged where not.**

---

## §6 Carry-forward

These items remain open after this plan commits:

1. **P1 candidate A-9** — pending (a) M-0.2 editorial_ledger atomization, (b) D-2.3 Jordan canon-check on DA-as-thread-operation. After both: append A-9 to `canon/editorial_ledger.yaml` if D-2.3 lands on Option α (DA is thread op).
2. **Bootstrap COMPLIANCE warnings** — 2 auto-fixable, addressed by M-0.2; 3 non-blocking warnings — investigate per Phase 0.
3. **`[FRESHNESS ⚠] 4 stale canonical source(s)`** — addressed by M-0.1.
4. **Candidate М-12 / М-13** — pending D-2.1 / D-2.2 Jordan decisions.
5. **Personal-scale verification gap** — addressed by V-1.7 in Phase 1.

---

## §7 Audit trail summary

```
Pass 1 (in-chat): plan framing, 19-item triage, sequencing, ask
Pass 2 (in-chat): full worklist, NERS+six-direction meta-audit, 7 meta-findings M-1..M-7
Pass 3 (this commit): outside-reviewer pass (8 concerns O-1..O-8), corrections applied, consolidated plan, meta-verdict PASS
```

**Bias acknowledgment:** plan author = audit author = plan meta-auditor = outside-reviewer. Quadruple self-authoring. Pass 3 outside-review surfaced 8 real concerns including 1 authority correction (PC-4.3 → D-2.4); plan now reflects those corrections. Pass 2 single-pass would have shipped a less honest plan.

**`[CONFIDENCE: medium-high]`** on plan structure and dependency graph.
**`[CONFIDENCE: medium]`** on whether Phase 4 proposals address the right level of granularity — PC-4.4 unified-vs-split was the largest open uncertainty and the unified-first approach (M-3 / O-4 correction) is the better hypothesis but not validated.
**`[GAP: sim battery designs are proposal-level sketches]`** — each PC-4.x patch register entry will need full sim battery design per PP-674 vetting block discipline.
