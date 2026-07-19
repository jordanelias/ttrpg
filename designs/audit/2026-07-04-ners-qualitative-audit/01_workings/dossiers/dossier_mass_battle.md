# Mass Battle Lane Dossier — Qualitative NERS Audit (2026-07-04)

Sources read: `designs/provincial/mass_battle_v30.md` (full, both halves), `designs/provincial/mass_battle_integration_v30.md` (full), `designs/architecture/scale_transitions_v30.md` §3.5-§3.9 (General Duel / Scene→Mass / Fieldwork↔All), `designs/audit/2026-07-04-mass-battle-cannae-gauge-audit/README.md` (freshest related audit, checked for calibration overlap).

## Core loop
Muster (faction layer) → March (territory) → 7-phase Battle Turn (§A.7: Strategy Declaration → Volley → Manoeuvre → Offensive Thread → Engagement → Cascade → Reform) repeated until rout/destruction/stalemate → Part D aftermath scene + named-officer fallout → Part E faction/settlement consequences → Part A.13 between-battle reinforcement/Discipline persistence.

## Decision points (rating)
1. **Phase 1 Strategy Declaration** (formation × Off/Def split × tactic × Thread intent, per sub-unit, ≤3 TTRPG/≤11 videogame) — **moderate**. Real tactic-counter web (§A.8: Wedge>Line, Shield Wall>Wedge, Envelopment vs Refused Flank, Hammer&Anvil) but see F3/F4 below on how much this actually swings outcomes vs. Command.
2. **Splitting vs concentration** (§A.8 doctrine) — **moderate, contaminated** — see F3.
3. **General Duel entry** (Phase 6 general action: Rally/Reinforce Discipline/Support Threadweave/**Personal combat**/Stabilise) — **moderate**: genuine risk-reward (suspend Command for a shot at a decisive personal-scale outcome), but thin follow-through (1 exchange/turn, max 5, no Thread option for a practitioner-general — F1).
4. **Thread ops in battle** (§A.10: diagnosis Phase 1, rear-safe vs frontline-risky Leap, Coherence spend toward Severance) — **rich**: a genuine attrition-vs-payoff gamble layered onto the battle clock.
5. **Post-battle aftermath scene** (Part D §D.1: Tend wounded / Survey damage / Address population, 3 distinct checks, distinct payoffs incl. hidden-consequence reveal) — **rich**. Strongest single decision point in the lane.
6. **Army composition / campaign strategy** (Levy defensive-only vs Professional costly-but-mobile, §A.14c; Campaign Supply attrition, §A.14b) — **rich**: a genuine standing strategic trade-off, not per-turn but campaign-shaping.
7. **Scene→Mass bonus consumption** (§3.8) — **degenerate-to-absent** as a mass-battle-side decision: it's an input from a prior scene, and mass_battle_v30.md never hooks it at all — see F2.
8. **Reinforcement/Reform** (§A.13, Muster) — **moderate**: Discipline persistence forces genuine multi-battle resource management (F8's complexity caveat applies to legibility, not richness).

## North Star assessment
**Choice density: moderate**, bimodal — the strategic layer (composition, Levy/Professional, Thread gamble, aftermath scene) is rich and clearly collision-engine-feeding; the turn-by-turn tactical layer is narrower than its apparent complexity suggests once Command asymmetry and the (contaminated) splitting-dominance finding are accounted for.
**Collision feed**: General Duel and the aftermath scene are the two designed collision points connecting personal-scale player agency to strategic-scale consequence (officer capture/disposition, settlement Order, hidden Findings). Both are well-built but General Duel is Thread-blind (F1) and the Scene→Mass channel is unconsumed (F2), so the actual feed is narrower than designed.

## N/Omega/Q observations
- **Q-robust tension**: §A.1's stated axiom "Command=7 vs Command=1 produces a near-certain outcome before a die is rolled" is explicit, DELIBERATE — but is in tension with the Q-robust "three viable approaches" test and Ω non-dominance. Cite mass_battle_v30.md §A.1.
- **Q-elegant tension**: the ED-1019+ per-sub-unit continuous-Morale/aggregate/cascade model (§A.4) is deep but the Army Morale composite (bottom of file, "derived_stats_v1 §8.2") is the one legible surface — depth is real but the underlying state (per-sub-unit float Morale, troop-weighted aggregates) is not something a player reads directly; the composite is doing real legibility work and should be checked for videogame HUD parity.
- **N**: Campaign Supply / Levy Restriction (§A.14b/c) model real historical political-military dynamics economically — solid N grounding, one-sentence rules with real strategic bite.

## Threadwork junctures
- **Present**: §A.10 (full Ob/Coherence-cost table by scale), §3.5/§3.6 (Thread→Faction is Domain Action; Thread→Mass positioning + Coherence-cost rules), §A.14 Woven-unit brittleness (MS≤40 trigger).
- **Absent-but-plausible**: General Duel (§3.7) personal-combat exchange has no Thread/Leap option for a practitioner-general — inherits combat_engine_v1's zero-threadwork state (ED-911, open P1) at exactly the juncture where a Thread-sensitive general duel would be most dramatically loaded.
- **Absent-but-plausible**: §3.8 Scene→Mass bonuses cover Social/Investigation/Combat wins but no Thread-scene win channel feeds a mass-battle bonus, despite Thread being the most battle-relevant personal-scale action per §A.10's own density.
- **Absent-deliberate**: none found stated for this lane — the mass-battle/Thread integration is comparatively the most built-out cross-system Thread surface in the corpus (per grounding doc 03 item "Mass battle ... full-but-record-defective").

## Dramatic legibility
**Partial.** *Whose position at risk*: yes — Army Morale composite + persistent Discipline give one legible number/threshold ladder. *What happens if no one acts*: yes — Campaign Supply attrition, Prosperity-0 Size loss, idle-army Morale loss are all explicit deterministic drains. *What does each named actor want*: **no** — from mass_battle_v30.md/integration state alone there is no motive/goal field; that's imported from faction/NPC layers, so this subsystem alone cannot answer the third question.

## Candidate degenerate lines
- Splitting-dominates-concentration doctrine (§A.8) — see F3, evidence itself now suspect.
- "Generalship dominates" as stated design axiom (§A.1) — see F4.

## Edges in/out
| Dir | Other | Mechanism | Status |
|---|---|---|---|
| in | Faction (Muster, Command formula Cha/Cog) | §A.5 | implemented |
| out | Faction/Settlement (Part E consequences, Mandate, Military) | §A.13/Part E | implemented |
| out | Settlement (aftermath scene, officer-as-governor) | Part D | implemented |
| in/out | Thread (§A.10, §3.5/§3.6) | Coherence cost tables | implemented |
| in/out | Personal combat (General Duel, §3.7) | Command suspension | implemented, but Thread-blind (divergent re: ED-911) |
| in | Scene (Social/Investigation/Combat win, §3.8) | +1D / Reform bonus | **declared-only** — not hooked in mass_battle_v30.md |
| in | Geography (§A.9 Phase-3 terrain derivation, ED-780) | terrain polygons | implemented |
| out | Sim engine (config.py, gauge_mb.py) | leading-canon numeric authority | divergent from several design-doc values (25×25 vs 50-grid geometry, splitting-doctrine numbers) — tracked ED-899/ED-909/ED-MB-0001/ED-MB-0002 |

## Directions
- top-down: the Command-dominance axiom is philosophy-consistent with "generalship is the battle" but strains Ω non-dominance as written.
- bottom-up: sim engine (config.py/orchestration.py) is leading canon and has moved past this doc's geometry/pool formulas in several places (banners acknowledge this); ED-MB-0002 (2026-07-04) shows even the doc's own cited simulation evidence (splitting doctrine) may be contaminated.
- lateral: General Duel/Scene-bonus are the sibling-subsystem hooks; both are thinner in practice than mass battle's own Thread integration.
- diagonal: aftermath scene + named officers are the strongest cross-scale narrative payoff in this lane.
- forwards: LC-8/ED-MB-0001/ED-MB-0002 show active, well-disciplined engine work in flight; design-doc geometry (§A.3b) is explicitly marked superseded pending re-derivation.
- backwards: §A.3b geometry and §A.8 splitting numbers both carry supersession/contamination risk flagged in-repo already.

## Findings (8)
See structured output.
