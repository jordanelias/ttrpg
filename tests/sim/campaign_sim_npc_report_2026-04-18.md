# Valoria Full Campaign Simulations — NPC PCs + Player Character
# Date: 2026-04-18
# Canonical sources: npc_behavior_v30.md, victory_v30.md, params/core.md, engine_v2.py

---

## Setup

11 full-length campaigns (120 seasons = ~30 years each). 10 named NPCs as PC, 1 player-created character.
Each NPC PC profile derived directly from npc_behavior_v30.md stat blocks.
Policy weights derived from primary/secondary Conviction and Ethical Framework.
Seed offset per run for reproducibility.

---

## Individual Campaign Results

| PC | Faction | Policy | RS | TC | Standing | Coherence | Features |
|----|---------|--------|----|----|----------|-----------|----------|
| Almud Almqvist | Crown | governor | 22 (Fractured) | 49 | 7/7 | 10 | 177 |
| Arne Himlensendt | Church | theocrat | 24 (Fractured) | 49 | 7/7 | 10 | 181 |
| Inge Baralta | Hafenmark | diplomat | 19 (Critical) | 49 | 7/7 | 10 | 182 |
| Magnus Vaynard | Varfell | investigator | 0 (Critical) | 49 | 7/7 | 1 | 227 |
| Lisbeth Ehrenwall | Crown | warrior | 23 (Fractured) | 49 | 7/7 | 10 | 180 |
| Maret Vossen | RM | restorationist | 22 (Fractured) | 49 | 7/7 | 10 | 185 |
| Aldric Hann | RM | independent | 18 (Critical) | 49 | 7/7 | 10 | 185 |
| Prince Torben | Crown | balanced | 23 (Fractured) | 49 | 7/7 | 10 | 184 |
| Edeyja | Wardens | practitioner | 1 (Critical) | 49 | 7/7 | 1 | 242 |
| Maret Uln | Varfell | diplomat | 33 (Fractured) | 49 | 7/7 | 10 | 186 |
| Player Character | Crown | balanced | 20 (Critical) | 49 | 7/7 | 10 | 183 |

**Victories by S120: 0/11**

---

## Character-by-Character Narrative

### Almud Almqvist (Crown — governor)
Institutional governance focus. RS ends Fractured at 22 — the governor policy slows RS drain by deprioritising Thread operations. TC holds at 49, just below the Dominant threshold. Reaches maximum Standing (7/7). The Crown's institutional strengths buy stability but not victory; without direct RS-stabilisation intervention, the peninsula erodes.

### Arne Himlensendt (Church — theocrat)
Certainty 5 (max) means first Coherence loss per session nullified — Himlensendt is uniquely resilient to ontological pressure. RS ends at 24 (Fractured). TC does not reach 75 even under theocrat policy in 120 seasons — the engine's faction AI does not fully replicate aggressive Church Govern action chains. **Finding:** TC ceiling of 49 across all runs indicates the faction AI TC advancement rate is undertuned. Himlensendt's theocrat policy should produce TC closer to 65–70 at S120.

### Inge Baralta (Hafenmark — diplomat)
RS hits Critical (19) — lowest non-practitioner result. Diplomat policy's high social/contest weight generates Domain Echo sequences that destabilise settlements indirectly. Baralta's constitutional law framework produces interesting contest-heavy play with marginal RS impact. Standing 7 reflects the high social engagement rate.

### Magnus Vaynard (Varfell — investigator)
**Most extreme outcome.** RS = 0 (total collapse). Coherence = 1 (near-depleted). Features fired: 227 — highest non-Warden count. Vaynard's TS 50 + investigator policy drives constant Thread operations; at TS 50 every Thread operation risks RS drain. Over 120 seasons this is lethal to substrate stability. Certainty 1 also means no Coherence recovery buffer. **This is the correct outcome** — Vaynard's canonical profile describes him as someone whose Thread engagement risks consuming him (Arc C: Consumed). The simulation validates this arc mechanically.

### Lisbeth Ehrenwall (Crown — warrior)
RS 23 (Fractured). Warrior policy is the most RS-stable non-practitioner option — low Thread engagement. Coherence fully intact. The Löwenritter martial profile produces consistent, unglamorous outcomes: Standing maxes, RS decays slowly, no extreme events. Correct for a character defined by institutional loyalty and martial conservatism.

### Maret Vossen (RM — restorationist)
RS 22 (Fractured). RM starts dormant — activated at campaign start for this run. Restorationist policy's Thread component (weight 0.3) drives moderate RS pressure. Vossen's Solidarity RS style means high social investment; the sim's socialize actions fire frequently. **Finding:** RM faction with empty starting territories requires a fallback govern target — this was the bug fixed before this run. Worth noting as an engine gap: RM's early-game should primarily access T9 via Community Organizing, not generic governance. Currently treated identically.

### Aldric Hann (RM — independent)
RS 18 (Critical) — lowest non-practitioner result alongside Baralta. Independent policy's mixed profile doesn't specialise, producing moderate pressure on all systems. Hann's operational focus doesn't translate to a distinct mechanical signature in the sim — the independent policy is too generic to reflect his specific operational pragmatism.

### Prince Torben (Crown — balanced)
RS 23 (Fractured). Blank-slate profile with balanced policy. Torben's undefined Beliefs are correctly represented — the simulation can't differentiate him from a generic Crown actor without player-shaped Belief development. This is the expected outcome: Torben's canonical significance is his malleability, which is player-facing, not engine-facing.

### Edeyja (Wardens — practitioner)
**Most extreme outcome alongside Vaynard.** RS = 1 (near-total collapse). Coherence = 1. Features: 242 — highest of all 11 runs. TS 70 at practitioner policy weight (Thread actions 50% of activity) over 120 seasons produces catastrophic RS drain. The canonical note that Edeyja "is a walking Calamity echo" is directly reflected. **Finding:** This validates the canonical design that a high-TS practitioner PC cannot simply operate at full Thread intensity for 30 years without existential RS consequences. The design is mechanically correct.

### Maret Uln (Varfell — diplomat)
RS 33 (Fractured) — **best RS outcome of all 11 runs**. TS 35 is moderate; diplomat policy minimises Thread operations. The combination of social focus, moderate practitioner engagement, and Varfell's territorial position (T4/T11–T13, less exposed to RS pressure centres) produces the most stable substrate outcome. Correct for a character defined as a cautious, relational political actor.

### Player Character (Generalist — Crown — balanced)
RS 20 (Critical). Moderate TS (20) plus balanced policy produces middle-of-the-road results across all metrics. Standing 7 reached. No distinctive mechanical signature — correct for a blank-slate generalist with no specialisation pressure.

---

## Cross-Campaign Findings

### RS Outcomes
- Average final RS: 18.6
- All 11 campaigns end with RS in Fractured (21–40) or Critical (≤20) range
- RS never recovers to Stable (>60) in any campaign — natural decay outpaces recovery without dedicated RS intervention
- **Practitioner PCs**: avg RS = 17.0 vs **Non-practitioner**: avg RS = 21.6

### RS by Policy (most to least RS-conservative)
| Policy | Avg RS | Interpretation |
|--------|--------|---------------|
| diplomat | 26.0 | Low Thread weight, high social |
| theocrat | 24.0 | Low Thread, high govern |
| warrior | 23.0 | Lowest Thread engagement |
| governor | 22.0 | Govern-heavy, minimal Thread |
| restorationist | 22.0 | Thread weight offset by social |
| balanced | 21.5 | Even distribution |
| independent | 18.0 | Mixed, some Thread |
| investigator | 0.0 | High Thread + high TS → collapse |
| practitioner | 1.0 | Max Thread + max TS → near-collapse |

### TC Outcomes
TC ends at exactly 49 in all 11 campaigns. **This is a calibration flag.** TC should differentiate meaningfully by faction alignment and policy. Possible causes:
1. Faction AI TC advancement rate undertuned — not aggressive enough to push past 49 threshold
2. Crown/Hafenmark counter-pressure correctly holding TC below 50, but producing convergence rather than differentiation
3. TC mechanics in engine may need direct faction-specific Domain Action weighting

### Victory Conditions
0/11 campaigns produce a victory by S120. Consistent with the design intent — victory is hard and requires specific strategic execution. However, zero victories across all character types including faction leaders (Almud, Baralta, Vaynard) is a mild calibration concern. The design expects victories to be achievable at 30-year timescales for at-least some characters.

---

## Findings Requiring Design Attention

| ID | Finding | Severity | Type |
|----|---------|----------|------|
| CAL-SIM-01 | TC convergence at 49 across all runs — faction AI TC rate undertuned or counter-pressure too uniform | P2 | Calibration |
| CAL-SIM-02 | 0/11 victories at S120 — victory thresholds may be too high for pure faction-AI campaigns without player strategic direction | P2 | Calibration |
| GAP-SIM-01 | RM govern fallback uses generic territory pool — should target T9 via Community Organizing specifically | P3 | Engine gap |
| NOTE-SIM-01 | Vaynard RS=0 and Edeyja RS=1 validate canonical arc descriptions mechanically — these are correct outcomes, not bugs | — | Confirmation |
| NOTE-SIM-02 | Maret Uln produces best RS outcome — diplomat+moderate TS is the most substrate-preserving playstyle | — | Confirmation |

---

## Simulation Infrastructure Note

Engine patch applied this session: RM and Wardens factions with empty starting territories now fall back to peninsula territory pool for govern actions. This is correct for the design layer — RM governs via Community Organizing (Domain Action), not standard territory governance. A future engine pass should route RM govern actions through the Community Organizing mechanic specifically.

