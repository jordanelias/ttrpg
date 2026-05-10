<!-- v30 path update applied 2026-04-13 -->
# VALORIA PROPAGATION MAP

> **Historical batches archived.** Sections from 2026-05-02 (Mandate audit ED-784, Register cap ED-786, ED-784 Phase 2 sweep commits A–D) moved to `archives/propagation/propagation_map_archive_2026_05_02.md` (this archival sweep). Earlier batches: `references/propagation_map_archive_2026-05-10.md` (root-level), `archives/propagation/propagation_map_archive_2026_05_01*.md` (4 batches). Active file tracks 2026-05-09 onwards.

## PP-716 — Wound mechanic correction (2026-05-09)
**Source:** Jordan canonical clarification.
**Files patched:** designs/scene/derived_stats_v30.md (§4.1 authoritative), designs/scene/combat_v30.md (L253-378 wound spec + thread interface), designs/threadwork/threadwork_v30.md (Leap/Weaving/Pulling/Mending/FR pool penalty), params/combat.md (Health formula + Thread interface), params/mass_combat.md (CF Zoom-In).
**Propagation:** All references to wound-induced +1 Ob (combat→thread, mass-Command, BG-CF) flipped to −1D Pool. All Vitality = End × 10 references reverted to Health = (End+6)×(MW+1). MW = floor(End/2)+1 restored. derived_stats_v30 §4.1 made authoritative source; other files reference §4.1.
**ED resolved:** ED-789. **ED reverted:** ED-694.
**Open propagation:** tests/sim/combat_arch_residual_stress_01/r1_wound_permanence.md (Module 1 R1) is SUPERSEDED — banner added; needs redo against PP-716 canon. canonical_sources.yaml SHAs marked PENDING_PP_716 pending freshness_gate refresh.

## PP-717 npc_behavior §1.2 stale-redirect fix (2026-05-10)
**Class E (editorial); applied this commit.** No mechanical propagation; corrects documentation pointer drift.
- `designs/npcs/npc_behavior_v30.md §1.2`: redirects updated to point at `designs/personal/conviction_taxonomy_v30.md` (PP-684 canonical) and companion `conviction_axis_matrix_v30.md`.
- `designs/personal/conviction_track_v1.md`: SUPERSEDED banner added at top; §1 deprecated; §2 Scar accumulation preserved as canonical pending PP-718 weight-scaling review.
- `references/canonical_sources.yaml`: conviction_track entry annotated as PARTIALLY SUPERSEDED.
- No code changes. No simulation re-run.
- Surfaced by: conviction_stress_01 (A-L09 P1 drift) commit 57bd26f4.
- Cross-reference: this PP unblocks future readers of npc_behavior_v30 §1.2 from learning the legacy 9-Conviction set.

---

*Older entries (before the most recent 8) archived to `references/propagation_map_archive_2026-05-10.md` on 2026-05-10 to keep working file under 15k-token CI limit.*

## PP-719 fieldwork §5.6b sustained Disposition reduction clarification (2026-05-10)
**Class E (editorial); applied this commit.** Single-line clarification, no mechanical change.
- `designs/scene/fieldwork_v30.md §5.6b`: "sustained for 2 seasons" → "2 consecutive seasons (defined as Disposition value at Accounting in season N below +3 AND season N+1 below +3, both unbroken). Non-consecutive seasons below +3 do not aggregate."
- Surfaced by: EC-F2.A-01 in `fieldwork_lifecycle_stress_01` (commit ddccbf9a).
- No simulation re-run required.

## PP-720 R7 stress-FF threshold spec (2026-05-10)
**Class C (mechanical — parameter/resolution-path extension); applied this commit.**
- `designs/scene/combat_v30.md §5`: new subsection "Stress-FF (ranged into melee under stress conditions)" inserted before §6 ARMOUR.
- Stress conditions: Wounds ≥1 OR Composure ≤3 OR environmental degradation.
- Resolution: secondary FF roll TN+1 (single-stress) / TN+2 (multi-stress); damage = floor(STR/2) + weapon_mod_vs_armour.
- No new Ob channel; uses canonical Combat Pool + TN modifier.
- Tabletop fallback waiver clause preserves Game-Master flexibility.
- Surfaced by: combat_arch_residual_stress_01 Module 7 R7 (commit c58bc670).

## PP-721 R9 routine-encounter B-mode presentation flag (2026-05-10)
**Class C (UX/presentation parameter); applied this commit.**
- `designs/scene/combat_v30.md §8`: new subsection "Architecture-B Presentation Flag" inserted before §9 MASS COMBAT.
- B-mode flag triggers: (1) fixed-geometry zone, (2) scripted entry positions, (3) single fixed objective, (4) stakes routine (no C-duel triggers).
- UI effect only: discrete position-cells, narrowed Stunt vocabulary, 8-actor cap. Mechanics unchanged.
- Tabletop fallback: B-mode is videogame-specific; tabletop ignores.
- Surfaced by: combat_arch_residual_stress_01 Module 9 R9 (commit 1c31109d C9.3 deferred refinement).

## PP-722 PP-349 stale Niflhel example fix (2026-05-10)
**Class E (editorial); applied this commit.** Surgical 5-word replacement.
- `designs/scene/social_contest_v30.md` PP-349 paragraph: "collaborating with Niflhel" → "collaborating with crime or underground networks operating against Church interests".
- Aligns canonical example with Jordan's 2026-05-09 Niflhel dissolution decision (G-L03 from setup_ignition_stress_01 commit cab3bd85).
- Surfaced by: F3 Heresy Investigation EC-F3.A-01 (commit 8de82dbb).

## PP-718 Conviction Scar accumulation per-Conviction clarification (2026-05-10)
**Class B (system extension); applied this commit.** Closes P1 ambiguity from conviction_stress_01 (commit 57bd26f4); reserved by PP-717 as next_pp.
- `designs/personal/conviction_track_v1.md §2`: rewritten to specify per-Conviction Scar accumulation under PP-684 structured concentration.
  - Crisis at 3+ Scars on **any single Conviction** (not aggregate count).
  - Multi-primary NPCs Scar each Conviction independently; concurrent crises possible.
  - Cultural-background Conviction crises produce muted drift (no full arc transition).
  - Crisis table roll 5 updated: "Autonomy survival" → Self-Other-orientation override (Autonomy not canonical post-PP-684; renamed Liberty).
- `references/canonical_sources.yaml` conviction_track entry: status note updated; pending-PP-718 mark cleared.
- Migration from legacy single-primary model preserves Scar counts on migrated Convictions (Reason→Scholastic, Continuity→roster-determined, Autonomy→Liberty).
- Surfaced by: conviction_stress_01 deferred-refinement Test 2 (commit 57bd26f4).

## ED-777 5-arc reframe — closure (2026-05-10)
**Class C (content reframe per Jordan's 2026-05-09 G-L03 decision); applied this commit.**
- `references/arcs/arc_register_factions.md` NIFLHEL section: rewritten as "CRIME & UNDERGROUND NETWORKS (settlement-layer phenomena — formerly NIFLHEL fourth-tier)".
- ARC-S11 reframed: "Headless Network" → "Underground Network Engagement" (per-settlement Intel; four-arm structure dissolved with Niflhel).
- ARC-S54 reframed: "Quiet Overreach" → "Underground Operational Detection" (Thread-signature dependency removed).
- ARC-S55 reframed: "Arms Out of Sync" → "Network Coordination Failure".
- NPC-ARC-VIR reframed: Virke as smuggling/criminal-network family.
- ARC-T25 reframed: criminal-network ownership ultimatum.
- ED-777 status: open → closed.
- Surfaced by: setup_ignition_stress_01 G-L02 (commit cab3bd85).

## ED-780 Phase 3 geography spec — closure (2026-05-10)
**Class B (system extension); applied this commit.** Phase 3 mechanical body authored.
- `designs/territory/march_layer_v30.md`: skeleton filled (~7.4k → ~15k chars). §§1.1-1.4 cavalry/skirmish/supply/multi-army coord; §§2.2-2.4 cache invalidation/UI/route blocking; §§3.1-3.4 fog/scouting/counter-recon/Thread-Witnessed; §4.3 bypass; §§5.2-5.4 multi-edge/engagement/Casus Belli; §§7.2-7.3 radiation traversal/Askeheim Gates; §8.2 hex-grid + geographic battle-terrain derivation. Naval §6 deferred to ED-055.
- `designs/provincial/mass_battle_v30.md §A.9 ENVIRONMENTAL MODIFIERS`: Phase 3 extension clause — geographic battle-terrain derivation at engagement coordinates via geography polygon query.
- `designs/territory/settlement_adjacency_v30.md §6`: cross-reference to march_layer added; Edge Type → Manoeuvre Modifier mapping consumed by march_layer §4.2.
- ED-780 status: standing → closed.
- ED-781 (Phase 4 stress tests) standing.
- Surfaced by: setup_ignition_stress_01 G-L05 (commit cab3bd85).

## PP-718 vetting walkthrough — full M-1..M-11 (2026-05-10)
**Class B vetting documentation; commit follows PP-718 mechanical commit 239922c6.** No mechanical change to PP-718; replaces the abbreviated vetting block in patch_register with full per-pattern walkthrough grounded in canonical reads.
- `canon/patch_register_active.yaml` PP-718 entry: vetting block expanded to per-M reasoning (M-1 through M-11), T-touches enumeration (extends 6, preserves 8, breaks 0), Q-robust/smooth/elegant detail. m_summary: 6+/3✓/1○/0−.
- `designs/personal/conviction_track_v1_pp718_vetting.md` (NEW): standalone full walkthrough doc with N/Μ/М/Τ/Q sections, M-1..M-11 per-pattern reasoning, per-T touch verdicts. ~273 lines / ~35k chars.
- `references/canonical_sources.yaml`: pp718_vetting_walkthrough field added under conviction_track entry.
- Sources read at full depth for the walkthrough: throughlines_meta (skeleton + infill §3.4-§3.8), conviction_taxonomy_v30, conviction_axis_matrix_v30, conviction_track_v1 (post-PP-717/PP-718 state), npc_behavior_v30 §1-§3, conviction_migration_roster_v30.

## PP-718 vetting walkthrough — m_summary count correction (2026-05-10)
**Class E (editorial fix); applied this commit.** Off-by-one defect in m_summary count corrected.
- `canon/patch_register_active.yaml` PP-718 vetting m_summary: "6 + · 3 ✓ · 1 ○ · 0 −" → "7 + · 3 ✓ · 1 ○ · 0 −". Actual M-ratings (M-1+, M-3+, M-4+, M-5+, M-6+, M-9+, M-11+ = 7) verified against per-pattern body.
- `designs/personal/conviction_track_v1_pp718_vetting.md` §М summary: "Six +, three ✓..." → "Seven +, three ✓..."; final summary table row "**6 + · 3 ✓ ... pass**" → "**7 + · 3 ✓ ... pass**".
- No mechanical change. Self-review caught the inconsistency between counted ratings (7 +) and summary claim (6 +).

## PP-718 vetting walkthrough — M-1/M-9 recalibration (2026-05-10)
**Class E (vetting documentation refinement); applied this commit.** No mechanical change to PP-718.
- Initial walkthrough (commit 39bd08c5; count fix 5a47da16) rated M-1 and M-9 as +.
- Independent-reviewer-style reconsideration determined both should be ✓:
  - **M-1**: PP-684's own vetting block already credits M-1 + for vector pressure-axes ("Convictions provide axis for continuous-pressure interpretation"). PP-718 ensures the Scar layer composes correctly with that extension but does not introduce a new M-1 pattern instance.
  - **M-9**: PP-684's vetting credits M-9 + for Self-Other drift ("new state-evolution dynamic"); legacy v1 carries the moral-injury ontological inversion (Scar mechanic itself). PP-718 routes both upstream inversions through the vector model rather than introducing a new ontological inversion.
- Final ratings: M-3/M-4/M-5/M-6/M-11 = 5 + (substrate vectorization through crisis layer; axis-specific institutional erosion; cross-scale axis-specificity; per-axis forced-choice; per-axis voluntary cultivation); M-1/M-7/M-8/M-9/M-10 = 5 ✓ (faithful preservation of upstream patterns); M-2 = ○ (scope mismatch).
- m_summary updated: "5 + · 5 ✓ · 1 ○ · 0 −" with revision-rationale note.
- Pass/fail verdict unchanged (zero violations both before and after recalibration).
- Self-review bias acknowledged: this walkthrough was authored about Claude's own prior PP-718 work; recalibration tightens the credit assignment without changing the canonical commit.

## PP-723 Settlement-level adjacency graph authored (2026-05-10)
**Class B (system extension); applied this commit.** Closes ED-710 placeholder + improvement_avenues A1 P1 gap.
- `designs/territory/valoria_geography_v30.yaml`: new `settlement_adjacency:` block (49 edges across 36 settlements; 19 intra-province, 26 inter-province, 4 thread-witnessed). Total file 28k → 32k chars.
- `designs/territory/settlement_adjacency_v30.md`: §1.2 rewritten (rule-as-implemented spec; 8 hand-specified overrides documented; 4 Thread-Witnessed edges enumerated); §5 Open Items "Adjacency map file" CLOSED; banner updated to "PARTIALLY SUPERSEDED post PP-723."
- Resolves geography_phase4_stress_01 ED-781 finding that mass_battle §A.9 Phase 3 geographic-derivation clause had no settlement-edge data to consume.
- Two-tier composition: territory adjacency (26 edges, drives strategic march_layer routing) + settlement adjacency (49 edges, drives tactical battle-arrival edge derivation).
- Vetting: 3 + · 4 ✓ · 4 ○ · 0 − pass. Genuine extensions: M-2 (geography-holds-pressure settlement-granular) and M-5 (two-tier scale composition).

## Patch Register Archival 2026-05-10

19 applied patches (PP-684..688, PP-705..723) archived to `archives/patches/patch_register_archive_2026_05_10.yaml`. No mechanical propagation required — all patches already fully applied and verified in canon. Active register reduced from ~15k to ~1.5k tokens.

## PP-723 vetting m_summary count correction (2026-05-10)
**Class E (vetting documentation refinement); applied this commit.** No mechanical change to PP-723.
- PP-723 m_summary corrected from "3 + · 4 ✓ · 4 ○" to "2 + · 4 ✓ · 5 ○": post-commit read-back caught off-by-one against actual ratings.
- Actual M-ratings: M-1 ○ · M-2 + · M-3 ✓ · M-4 ○ · M-5 + · M-6 ✓ · M-7 ✓ · M-8 ○ · M-9 ○ · M-10 ✓ · M-11 ○ = 2 + · 4 ✓ · 5 ○ · 0 −.
- Pass/fail verdict unchanged (zero violations).
- Correction applied at archives/patches/patch_register_archive_2026_05_10.yaml (PP-723 was auto-archived between the original commit 0a4a1ff7 and this correction commit, so the fix lands in the archive rather than active register).
- This is the third off-by-one detection across recent vetting work (PP-718 walkthrough commit 5a47da16; PP-718 recalibration commit 04d026a0; this); a process improvement (D1 from improvement_avenues_2026-05-10) for tighter post-commit verification is now demonstrably load-bearing.

## PP-724 NPC-NPC relational graph framework (2026-05-10)
**Class A new substrate-defining system; B1.1 of improvement_avenues_2026-05-10.** Authored designs/npcs/npc_relational_graph_v30.md (~585 lines / ~47k chars). Six canonical edge types (sworn-bond, liege-vassal, kinship, patronage, rivalry, feud); per-edge state machine paralleling F2 Knot lifecycle (fieldwork §5.6b); strain accumulation/decay/break/rupture rules; multi-edge composition rules; NPC-NPC Disposition derivation; hooks for B1.2 (defection cascade), B1.3 (faction-Cascade integration), B1.4 (settlement-coupling).
- `designs/npcs/npc_relational_graph_v30.md`: NEW. PROVISIONAL.
- `references/canonical_sources.yaml`: npc_relational_graph entry added under Canonical NPC docs.
- Closes the canon-wide gap surfaced in improvement_avenues §B1: ROTK + CK3 precedents named in settlement_layer §Precedent + settlement_adjacency canon-compliance had no relational-graph mechanic.
- Composes with PP-684 (Conviction taxonomy), PP-685 (Migration roster), PP-686 (Cascade math, B1.3 hook), PP-718 (per-Conviction Scar; §3.9 Honor-crisis cascade), PP-723 (settlement adjacency, §6 distance-strain hook).
- Vetting: 6 + · 2 ✓ · 3 ○ · 0 − pass. Genuine extensions on M-1/M-3/M-4/M-5/M-6/M-11; faithful preservation on M-7/M-10; scope-mismatch ○ on M-2 (geography deferred to B1.4), M-8 (access pattern), M-9 (clinical-borrowing pattern).
- Q-robust: three viable approaches per relational situation (cultivate, exploit, reconcile); world-state visible per-edge; mechanic fires without player action. Q-smooth: methodology mirrors Knot lifecycle. Q-elegant: core rule restatable in one paragraph; second-order Honor-crisis cascade composes cleanly with PP-718.
- B2 (named-NPC instantiation), B1.2 (defection cascade body), B1.3 (faction-Cascade integration body), B1.4 (settlement-coupling body) all deferred follow-up.

## PP-725 Settlement coupling for relational graph (B1.4 of improvement_avenues_2026-05-10) (2026-05-10)
**Class B (system extension); applied this commit.** Composes A1 (PP-723) + B1.1 (PP-724) per Jordan's specific guidance ('settlements need zoomed-in geography and ROTK network style is key' — B1.4 is the intersection).
- `designs/npcs/npc_relational_graph_v30.md` §6 promoted from [Hook for B1.4 — Deferred] to [Implemented PP-725 / B1.4]. Adds: §6.1 NPC residence canon (7-faction HQ mapping + Governor inheritance + explicit override field), §6.2 hop-distance algorithm (BFS with Thread-Witnessed bypass at TS ≥ 30), §6.3 strain-trigger scaling classification (3 buckets: scale / already-geographic / no-scale), §6.4 officer reassignment shock rules, §6.5 worked examples (6 canonical pairs 0..7 hops), §6.6 integration formula.
- Doc 46k → 55k chars (+9k).
- Vetting: 3 + · 2 ✓ · 6 ○ · 0 − pass. Genuine extensions: M-2, M-5, M-10.
- Algorithm validated: BFS on canonical 49-edge graph from PP-723 — all 36 settlements connected; max pair-distance 7 hops (Baralta S-015 ↔ Schoenland Governor S-035). 7-hop max pre-validates ED-055 naval-scope as strategic-compression mechanism (A3 P1 from improvement_avenues).
