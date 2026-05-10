<!-- v30 path update applied 2026-04-13 -->
# VALORIA PROPAGATION MAP
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

---

*Older entries (before the most recent 6) archived to `references/propagation_map_archive_2026-05-10b.md` on 2026-05-10 (second rotation this date) to keep working file under 5k-token CI limit.*
