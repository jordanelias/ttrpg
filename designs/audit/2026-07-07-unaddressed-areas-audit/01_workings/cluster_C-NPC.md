# cluster_C-NPC

_Evidence cluster dossier, read-only; archived verbatim from the agent's final message by the Fable orchestrator (2026-07-07). Verdicts pending refuter pass + Fable adjudication - see `unaddressed_areas_audit_v1.md`._

# Cluster C-NPC dossier

## Positive sweep table (mechanism · doc § · sim file:line · verdict)

| # | Mechanism | Doc § | Sim file:line | Verdict |
|---|---|---|---|---|
| 1 | Conviction Scar accumulation — per-Conviction thresholds (1/2/3+), season cap, Certainty scaling | `designs/personal/conviction_track_v1.md` §2–3 (lines 32–88) | `sim/personal/conviction.py:51-65` (constants), `:196-226` (`apply_conviction_scar`) | **MATCH** — thresholds (destabilise/shift/crisis), season cap =1, and Certainty scaling (C0:−1, C5:+1) are correctly ported. Sim silently interpolates C1/C4 (doc only specifies C0, C2–3, C5) — minor, unflagged, P3. |
| 2 | Conviction taxonomy identity (which 9/13 names are valid) | `designs/personal/conviction_taxonomy_v30.md:29-41` (canonical 13: Faith/Authority/Order/Scholastic/Utility/Equity/Liberty/Precedent/Community/Identity/Warden/Virtue/Honor) | `sim/personal/conviction.py:46-49` (legacy 9: Faith/Order/Reason/Equity/Precedent/Autonomy/Continuity/Community/Warden) | **KNOWN-TRACKED, already REFUTED→P3** (`01_workings/refutations/refute_sim-conviction-taxonomy-stale.md`) — sim mirrors §3's still-un-migrated Thread-Operation matrix column names, not §1's superseded taxonomy; root cause is ED-1006 (open), not a sim bug. Do not re-file as NEW. |
| 3 | Knots→Conviction wiring on Close Knot break | `designs/personal/knots_v30.md` §6.1 | `sim/personal/knots.py:323-333` calls `apply_conviction_scar(..., conviction='Loyalty', ...)` | **BROKEN — NEW.** `'Loyalty'` is in neither the legacy 9-set nor the canonical 13-set (conviction.py:46-49 / taxonomy_v30.md:29-41). `apply_conviction_scar`'s own guard (conviction.py:189-191) silently no-ops on unrecognized Convictions. The Close-Knot-break "Conviction Scar" consequence is dead code — see C-NPC-2. |
| 4 | Thread Event × Conviction Scar Matrix (which witnessed op Scars which Conviction) | `conviction_track_v1.md` §3 (lines 70–84) | *(none found)* | **NO SIM IMPLEMENTATION.** `apply_conviction_scar()` requires the caller to already know which Conviction to Scar (conviction.py:172-174, "Caller determines from §3 matrix"); the only real caller (`knots.py`) isn't a Thread-witness event at all. |
| 5 | Resonant Style opponent-targeting (§6.2–6.5 four-way effect table: Piety Track bonus / +2 strain / Doubt Marker / Ob−1) | `designs/npcs/npc_behavior_v30.md:694-738` | *(none found)* | **NO SIM IMPLEMENTATION.** The only Style-alignment code in `sim/personal/contest/armature.py` is a different, later-added, judge-aimed continuous mechanic — its own docstring (lines 23-27, 100-105) states "NO pre-existing continuous dot-product… anywhere in sim/personal" and explicitly disclaims reuse of the canonical opponent-aimed +1D mechanic. |
| 6 | BG Faction Priority Trees (9 deterministic decision ladders) | `npc_behavior_v30.md:768-895` (§8.1–8.10) | `sim/autoload/npc_ai.py:22-28` | **STUB — 0% implemented.** File is titled "NPC priority trees, action selection, faction AI dispatch" but both entry points (`select_action`, `evaluate_priority_stack`) are bare `raise NotImplementedError`. R-3's "working as constrained" verdict (NERS audit) is a *design*-level GD-2 compliance call and says nothing about the sim — it doesn't run this system at all. |
| 7 | NPC Outreach/Demand (§8.11, "world's actors do not wait to be approached") | `npc_behavior_v30.md:895-963` | *(none found)* | **NO SIM IMPLEMENTATION.** Zero "outreach"/"demand" tokens anywhere in `sim/` (confirmed by corpus grep). Independent of EP-7's visibility bug, the feature doesn't exist in the reference engine yet. |
| 8 | Concern/Project/Opinion/Off-screen engine (doc-12 Procedures B/C/D/E — the core of GAP-5) | `references/module_contracts.yaml:105-176`; `designs/provincial/political_dynamics_keys_migration_v30.md` (whole doc) | *(none — the "L1127"-style citations point at `designs/audit/2026-04-28-political-dynamics-session/12_development_specification.md`, a **design doc**, not code)* | **NO PYTHON IMPLEMENTATION EXISTS ANYWHERE.** Confirmed by repo-wide grep for `generate_concern`/`resolve_concern`/`advance_project`/`apply_drift` — every hit is prose pseudocode in design docs. See C-NPC-1. |

## npc_memory state

`module_contracts.yaml:177-196` — `doc: null`, `resolver: state_reader [ASSUMPTION]`, consumes 4 Key types from `npc_behavior`, **`emits: []`**. It is not merely undocumented; per its own contract it is a pure write-only sink with no declared read-path to any consumer.

**What canon actually says, anywhere:** the only schema is a "bridge" class (`MemoryReference`) inside `political_dynamics_keys_migration_v30.md` §2.3 (lines 51-73) — read-through accessors onto Key-log entries, capped at 10 references, decaying salience. No standalone design doc exists (`gap_notes` line 192: "home doc unlocated… standalone spec [GAP]").

**What breaks without it:**
- `npc_behavior_v30.md` §6.1/§6.1b "Appraise Revelation" — empty section headers (lines 679-685); a Contest win at Overwhelming promises "one Belief revealed" and delivers nothing (edge-playability E3, confirmed P1 MISSING).
- P-09 (memory-pulling must be messy/costly/detectable) has zero mechanical surface for named-NPC memory (NERS `npc-memory-p09-gap`, KNOWN-TRACKED).
- The emergent-narrative-engine-v2 spec (2026-07-05) explicitly assumes npc_memory functions as an *existing* reader for its "ethics-as-pattern" design (`01_workings/draft_s1_q1_q2.md:65`) while its own substrate section marks npc_memory **"UNCHANGED (retain `doc: null`)"** (`01_workings/spec_sections/s4_substrate.md:330-332`) — the newest major design layer is knowingly building on a dependency it acknowledges has no home.

**Unreconciled fork (new observation):** two live, contradictory proposals exist and neither has been actioned or flagged against the other. (a) `designs/audit/2026-06-28-distillation-coherence/distillation_coherence_report.md:80` recommends **retiring the module boundary** — "Mark as owned sub-component of npc_behavior… Don't register separately until/unless Knowledge is Key-migrated" (unexecuted, "needs-your-call"). (b) **ED-WR-0003** (filed 2026-07-05, `handoffs/HANDOFF_WR.md:9-15`) calls for **building it out** — writing the §6.1/§6.1b revelation procedures plus an "overheard" visibility rule. Fold-it-away and build-it-out are not compatible next steps, and nothing in the corpus notes the tension.

## 2-cycle damper state

The `social_contest ↔ npc_behavior` 2-cycle self-contradiction is **still live today (independently re-verified 2026-07-07)**:
- `references/module_contracts.yaml:153` (npc_behavior's own loop entry): `"dampers unconfirmed [OPEN — Jordan]"`.
- `references/module_contracts.yaml:442` (social_contest's loop entry, same cycle): `"BOUNDED [verification LD-1]: Procedure-D batch cadence (1/Accounting) + |delta-affect|>=0.5 emission threshold + Chain-Contest cap 3 then 4-season cold equilibrium. NOTE: the affect_axis clamp is NOT in canon…"`.

**What exactly is undecided:** two things, layered.
1. **A stale/false "resolved" claim.** `designs/audit/2026-06-28-distillation-coherence/verification_addendum.md:53` asserts "the two contract flags 'dampers unconfirmed [OPEN — Jordan]' are stale" and its `open_decisions.md` §0b lists "social_contest<->npc 2-cycle damper [LD-1]" under **"Also applied."** In fact the fix (citing the numeric bounds) was written into the **social_contest block only**; npc_behavior's mirror entry was never touched. §1 of the same `open_decisions.md` file (line 22) simultaneously lists this as "**still deferred**" — the document contradicts itself about its own completion state.
2. **Even the "BOUNDED" side admits an unconfirmed premise.** Its own note: "the affect_axis clamp is NOT in canon; convergence rests on these bounds + the saturating §5.4 drift curve." So the numeric bounds it cites are real (Procedure-D 1/Accounting cadence, |Δaffect|≥0.5, Chain-Contest cap 3), but the clamp that would make them actually *bound* the loop (rather than just throttle its cadence) has not been located in canon.

Net: this is not an open design question awaiting Jordan's input on numbers — the numbers exist and were half-applied. It's an unreconciled annotation plus one unverified premise (the affect_axis clamp). ep-17 (edge-playability) independently reaches the compatible but distinct point that canon nowhere distinguishes "immediate in-scene stakes" from "durable behavioral echo" (batched to Accounting) — a design-legibility gap layered on top of the annotation bug, both unresolved.

## Orphan triage: category census · staleness · disposition proposal

**Method:** read the full header/structure (Executive Summary, Findings-by-Unit index, Findings Table format) and sampled ~250 of 449 findings via the compact Findings Table — all 61 HIGH rows, all 83 NOTE rows, and large contiguous MEDIUM/SOFT/LOW blocks (≈lines 155–306, 380–449, 530–604 of the source doc).

**Category census** (from the doc's own Executive Summary, cross-checked arithmetic — both sum to 449):

| Severity | Count | | Category | Count |
|---|---|---|---|---|
| HIGH | 61 | | contradiction | 138 |
| MEDIUM | 121 | | gap | 85 |
| SOFT | 49 | | naming | 54 |
| LOW | 135 | | canon | 52 |
| NOTE | 83 | | mechanical | 51 |
| | | | note | 69 |

**Dominant substantive clusters** (from sampling, cutting across the formal categories):
- **A — Conviction-taxonomy migration debt** (PP-684 13-set / PP-685 migration roster): legacy labels (Reason/Autonomy/Continuity) used unannotated as live canon; NPCs absent from the migration roster; conflicting Conviction values across roster/behavior/analyses/foils for the same NPC. By far the largest generator — touches nearly every per-NPC unit plus all 3 dedicated taxonomy-integrity units, spans contradiction/gap/naming/canon.
- **B — TS/Certainty stat contradictions** across roster/behavior/analyses/registry (second-largest cluster; contradiction+mechanical).
- **C — Ethical Framework labels used as live Ob-drivers** without the `[SUPERSEDED→PP-686 §3.7]` annotation (systematic, per-NPC "canon" pattern).
- **D — Struck/superseded mechanics still invoked** (VTM, Niflhel, Coup Counter, GD-1-violating co-victory language) — smaller but concentrated in HIGH severity.
- **E — Missing mechanical scaffolding for Tier-2/background NPCs** (no Resonant Style / Beliefs / Certainty / absent from behavior doc) — "gap" category.
- **F — Self-refuting "note" findings**: a large share of the 83 NOTE rows are the audit's own adversarial verifier confirming a candidate premise was **false** (e.g., "Almud/Vaynard/Himlensendt are NOT placeholder names," multiple P-04/P-08/P-10 "clean" confirmations) — signal, not debt.

**Staleness assessment.** I spot-checked representative HIGH items directly against the current working tree rather than trusting the doc's self-reported "CONFIRMED" tags:
- Almud TS 28 (AUD-NPC2-031/032/053's subject) is **still present today**: `npc_behavior_v30.md:528`.
- The deprecated "Order → Autonomy" Conviction label is **still live today**: `npc_behavior_v30.md:569`.
- `sim/personal/conviction.py`'s legacy 9-Conviction set is **still live today** (independently confirmed above).
- "Cardinal Reichard" was **not** found in a targeted grep of `npc_behavior_v30.md` itself — the audit's citations for that finding point at the relational graph and migration roster, not this file, so that specific naming item's staleness is genuinely uncertain (unlike the taxonomy debt, which I positively confirmed is still live).
- A repo-wide grep for `AUD-NPC` / `npc-comprehensive-audit` / "449 finding" outside the audit doc itself surfaces **no downstream action** — no ED filed, no HANDOFF reference, no workplan lane, no CURRENT.md mention. `tools/observability/npc_audit_report_gen.py` is a report-generator, not evidence of a fix pass.
- No post-06-22 work touched this content: the 06-28 distillation-coherence pass edited only `module_contracts.yaml` metadata; the 07-04 NERS audit's only npc_behavior engagement was two refuted candidate findings on different subjects (critic's own G3: "a lane that ran but returned empty"); the 07-05 edge-playability audit (EP-7/ep-14–20) found adjacent but non-overlapping seam issues; the 07-05 narrative-engine-v2 spec explicitly left npc_behavior/npc_memory content unchanged.

**Conclusion: essentially the entire 449-finding backlog is unaddressed**, two weeks on. Nothing here contradicts the charter's premise that this is audit-rich, execution-light debt.

**Disposition proposal, per category (not per finding):**

| Category | Proposed disposition |
|---|---|
| **contradiction (138)** | **FOLD** the majority (Conviction/TS/Certainty value clashes, ~estimate 80–90 of 138 from sampling) into one mechanical reconciliation pass keyed to PP-685's migration roster as designated-PRIMARY (the audit itself applies this hierarchy consistently — no fresh judgment needed, a haiku/sonnet-tier propagation job). **RETIRE** the subset the audit's own note/DOWNGRADED items already refute as false positives. **KEEP** a handful as standalone HIGH EDs where cross-doc canon-supersession stakes are structural (e.g. Niflhel dissolution self-contradiction AUD-NPC2-014/015; GD-1 co-victory violation AUD-NPC2-018). |
| **gap (85)** | **FOLD** the "absent from migration roster / no Conviction vector / no RS / no Beliefs" subset into the *same* reconciliation pass as contradiction — completing PP-685 resolves both simultaneously. **RETIRE** background-NPC gaps the audit itself marks Tier-2/DOWNGRADED absent a named mechanical dependency. |
| **naming (54)** | **SPLIT.** Deprecated-label-without-supersession-note items → fold into the reconciliation pass (same root cause). Placeholder/misfiled-name items (Cardinal Reichard, "Vorn," faction misfiling) → **RETAIN as a targeted verification pass** before filing — staleness here is plausibly higher than the taxonomy cluster (see above). |
| **canon (52)** | **FOLD** into the reconciliation pass — almost entirely the Ethical-Framework-as-live-Ob-driver-without-`[SUPERSEDED→PP-686 §3.7]` pattern, a mechanical annotation sweep. |
| **mechanical (51)** | **KEEP as individual/small-batch EDs** — heterogeneous, judgment-requiring (struck-mechanic replacement decisions like Maret's VTM-gated succession; TS-threshold-band corrections; stat-cap ambiguities). Not safe to fold. |
| **note (69)** | **RETIRE** the majority (self-refuting false-positive confirmations, "clean" compliance notes) — valuable as permanent record, not actionable debt. **KEEP** a small residual of genuine meta-process/housekeeping items (e.g. AUD-NPC2-388's flag that `npc_behavior_system_v1.md` carries the superseded 9-set with no supersession banner). |

**Net recommendation for the single triage ED the workplan's T2 row calls for:** one consolidated "Conviction/Ethics/TS migration-completion" ED absorbing the bulk of contradiction+gap+naming+canon (roughly 250–300 of 449 by sampling-based estimate); a small set of individually-judged EDs for the mechanical/GD-1-violation items (~10–15); a targeted naming-hygiene verification pass (~10–15, staleness-uncertain); archival retirement (no ED) of the self-refuting note-category items (~40–50).

## Findings (C-NPC-1..N)

**C-NPC-1.** The concern/opinion/project engine (doc-12 Procedures B/C/D/E) that GAP-5's positive verdict rests on has **zero Python sim implementation anywhere in the repo** — every citation ("doc-12 L1127" etc.) resolves to `designs/audit/2026-04-28-political-dynamics-session/12_development_specification.md`, a design doc, not code. Six of the eight central npc_behavior mechanisms I checked (Procedures B–E, Resonant Style opponent-targeting, Outreach/Demand, BG Priority Trees) have no sim counterpart at all. GAP-5's "absence-of-finding rests on the dossier alone" understates the problem: a sim-based check was never *possible* for most of this system's surface, not merely unattempted. **P1. KNOWN-TRACKED** (GAP-5, deepened with specific scope: which mechanisms are literally unverifiable and why). Evidence: `sim/autoload/npc_ai.py:1-28`; repo-wide grep for `generate_concern`/`resolve_concern`/`advance_project`/`apply_drift` (zero code hits); `designs/provincial/political_dynamics_keys_migration_v30.md:8,20-25`.

**C-NPC-2.** `sim/personal/knots.py:328-331` calls `apply_conviction_scar(actor, ..., conviction='Loyalty', ...)` on a high-strain Close Knot break, but `'Loyalty'` is not a member of `CONVICTIONS` in `sim/personal/conviction.py:46-49` under either the legacy or canonical taxonomy. The function's own guard (`conviction.py:189-191`) silently returns `magnitude=0` for unrecognized names, so this call is dead code: the design intent "high-strain Close Knot break Scars a Conviction" (`knots_v30.md` §6.1) never actually fires in the reference sim, despite the returned `consequences` dict claiming `conviction_scar: 1`. **P2. NEW.** Evidence: `sim/personal/knots.py:314,323-331`; `sim/personal/conviction.py:46-49,183-191`.

**C-NPC-3.** The Thread Event × Conviction Scar Matrix (`conviction_track_v1.md` §3) — the doc's own primary specified trigger for Conviction Scars — has no sim wiring. `apply_conviction_scar()` requires the caller to already resolve the matrix lookup; the one real caller (`knots.py`) implements an unrelated trigger (Knot rupture, not Thread-witnessing). No file in `sim/thread/*.py` calls into `sim/personal/conviction.py` at all (confirmed by grep). **P2. NEW.**

**C-NPC-4.** The canonical opponent-aimed Resonant Style targeting mechanic (`npc_behavior_v30.md` §6.2–6.5 — the four-way per-style effect table central to the dossier's core loop) has no sim implementation. The only Style-alignment code that exists (`sim/personal/contest/armature.py`) is a separate, later-authored, judge-aimed continuous mechanic that its own extensive docstring explicitly disclaims as a reuse of the canonical mechanic ("NO pre-existing continuous dot-product… anywhere in sim/personal," lines 23-27). **P2. NEW.**

**C-NPC-5.** `sim/autoload/npc_ai.py` — the dedicated module for the 9 BG Faction Priority Trees — is a complete stub (both entry points `raise NotImplementedError`). R-3's NERS verdict ("deterministic priority trees… working as constrained," `ners_qualitative_audit_v1.md:299`) is a design-compliance verdict about GD-2 and says nothing about sim coverage; the reference implementation of this central mechanism is 0% built. This is properly C-STUB's remit for the aggregate stub×milestone map, but is flagged here as directly load-bearing evidence for GAP-5. **P2. NEW** (the specific GAP-5/R-3 linkage is new; the raw stub fact likely belongs to the charter's already-known "~19 stubs" aggregate).

**C-NPC-6.** §8.11 Outreach/Demand — the mechanism EP-7's finding directly critiques for structural player-invisibility — has no sim implementation at all (zero "outreach"/"demand" hits in `sim/`). Independent of the visibility bug, the feature doesn't exist yet in the reference engine. **P3. NEW.**

**C-NPC-7.** The social_contest↔npc_behavior 2-cycle damper self-contradiction (`module_contracts.yaml:153` vs `:442`) is confirmed still live today. Worse than previously framed: `designs/audit/2026-06-28-distillation-coherence/open_decisions.md` believed this was closed ("Also applied," §0b) while its own §1 simultaneously lists it "still deferred," and `verification_addendum.md:53` asserts the flag is "stale" — the fix was applied to only one of the two mirror-image contract blocks. Even the "fixed" side admits its convergence premise (the affect_axis clamp) "is NOT in canon." **P1. KNOWN-TRACKED** (NERS `contract-2cycle-self-contradiction`, `02_interdependency_map.md:25`) — the half-applied-fix-that-was-believed-complete framing is new evidence.

**C-NPC-8.** `npc_memory` remains `doc:null` with `emits: []` — a declared pure sink with no read-path even in principle. Two live, unreconciled, contradictory proposals exist: retire the module boundary entirely (distillation-coherence, unexecuted) vs. build out its player-facing procedures (ED-WR-0003, unexecuted) — nobody has flagged the tension. Separately, the emergent-narrative-engine-v2 spec (2026-07-05) treats npc_memory as an assumed-functional "existing reader" for its ethics-as-pattern design while its own substrate section marks it unchanged/still-null — the newest major design layer knowingly depends on a documented gap. **P1/P2. KNOWN-TRACKED** (ED-WR-0003; distillation-coherence Lens 2) — the fork-between-proposals and the narrative-engine-v2 dependency angle are new.

**C-NPC-9.** The 2026-06-22 449-finding NPC audit is, as far as any corpus signal shows, **entirely unaddressed** two weeks later — I verified this directly (Almud TS 28, deprecated "Autonomy" label, and the stale sim Conviction taxonomy are all still live) rather than trusting the doc's internal "CONFIRMED" self-tags, and a repo-wide search found no ED, HANDOFF entry, or workplan lane referencing it. **P2. NEW** (the specific "verified-still-live, zero downstream action" finding, as distinct from the audit's mere existence, which is already known per the charter).

## Honest gaps

- I sampled ~250 of 449 findings via the compact Findings Table (all HIGH, all NOTE, large MEDIUM/SOFT/LOW blocks) but did not read the "Detailed Findings" prose section (source doc lines 605–3157) for any finding, and did not independently recompute the category/severity census row-by-row — I used the doc's own Executive Summary totals, arithmetic-checked against my sample rather than fully rebuilt.
- Staleness was spot-checked on ~5 representative items (Almud TS, deprecated Conviction labels, "Cardinal Reichard," sim taxonomy, the module_contracts damper), not re-verified finding-by-finding across all 449.
- The "no sim implementation found" verdicts in the positive-sweep table rest on grep/read absence-of-evidence across `sim/`, not on executing the code; for a codebase this well-organized that's strong but not proof.
- I did not read `12_development_specification.md` (the 1875-line doc-12 pseudocode source) for its own internal consistency — only confirmed it exists and is the sole basis for Procedures B–E.
- I did not investigate ED-1006 (the tracked root cause for the 3-way piety/conviction_track taxonomy collision) beyond the NERS refutation's citation of it.
- Several findings here plainly overlap other clusters' remits (C-STUB for the stub×milestone census generally; C-FA for faction_state/faction_politics boundary and struck-mechanic debt like VTM/Coup Counter) — flagged, not resolved, since reconciling ownership is a synthesis-stage job.
- The "5–8 central mechanisms" selection for the positive sweep is my own judgment call about what's load-bearing in npc_behavior; a different selection could surface a different verified/unverified split, though the headline result (most of the system has no sim oracle to check against) is robust to that choice given how many mechanisms it held across.
