# Mass-Battle Engine — Wiring Stress Test & Top-Down Historical Validation

**Date:** 2026-06-22 · **Engine:** `tests/sim/mass_battle/` @ HEAD `c8ef557c` (orphaning + comment fixes applied) · **Method:** differential flag-toggling (bottom-up wiring) + comparison against cited historical analyses (top-down).

## Verdict

Every intended-active mechanic is **wired and load-bearing** — toggling each one shifts battle outcomes; none is silently inert (the failure mode the ED-1032 orphaning bug exemplified). The engine's emergent behavior **matches the historical analyses** across all six anchors tested. The intended-dormant `_envelopment_sigma` returns exactly `0.0` by design (the no-double-count basis for the PP-683 resolution); `reform`/`rally` remain intended-deferred.

## Part 1 — Wiring stress test (bottom-up)

Each mechanic's env flag (or trigger condition) is toggled across the 9-matchup battery; an outcome shift proves it load-bearing. Byte-identical results under a toggle mean the mechanic is either not triggered by that scenario (re-tested under its proper trigger) or genuinely cancels under symmetric inputs.

| Mechanic | Probe | Result | Wired |
|---|---|---|---|
| Per-cell combat (`PER_CELL`) | toggle, full battery | shifts nearly every matchup (e.g. CB 1/0/9 → 9/0/1) | ✓ |
| Lanchester lethality (`LANCHESTER_ENABLED`) | toggle, full battery | shifts lethality (CE meanHPb 175.7 → 118.2) | ✓ |
| Command-sigma pool (`COMMAND_SIGMA_ENABLED`) | pool probe + asymmetric command | pool 6 (on) vs 8 (off) at half-cohesion; **cmd6 beats cmd2 20/0**; symmetric command cancels (genuine, not inert) | ✓ |
| Brace / square (`PC_BRACE_ENABLED`) | CB cav-vs-braced, toggle | brace-off → cavalry wins 1→4, infantry HP 340→261, routs 1→4; control CL identical (instruction-gated) | ✓ |
| Envelopment shock (`PC_ENVELOP_SHOCK`) | constructed fix+envelop (2-subunit), toggle | enveloped unit routs **12/15** (on) vs 8/15 (off); provably inert in lone 1v1 (no double-count) | ✓ |
| Envelop maneuver (`PC_ENVELOP_PATH`) | constructed `envelop` instruction, toggle | outcome shifts with toggle | ✓ |
| Formation drift + orphan-fix (ED-1032) | pre-fix `simpkg` vs fixed | AH shifts (7/4/1 vs 6/4/2); orphan count → 0 (prior validation) | ✓ |
| Morale erosion + rout | full battery | units rout (CE rtB 10/12; CS rtB 8/10) | ✓ |
| Volley (ranged) | ranged-vs-melee trace | 77 volley events fired | ✓ |
| `_envelopment_sigma` | direct call | returns **0.0** — dormant by design (NERS-N/E, no double-count) | dormant ✓ |
| `reform` / `rally` | — | intended between-turns-only / deferred stub | n/a |

**Key finding.** Two mechanics (command-sigma under symmetric command; envelop-shock in a lone 1v1) returned byte-identical results under their toggle — **not** because they are unwired, but because their trigger was unmet. Both fire decisively once the proper condition is constructed (asymmetric command; a unit fixed-and-flanked by a separate body). This is correct conditional design, not inertness — and it is exactly what distinguishes a wired-but-untriggered mechanic from a silently-orphaned one.

## Part 2 — Top-down historical validation

### 1. Cannae (216 BC) — envelopment → disintegration. **MATCH**
*Analysis:* Hannibal's ~50,000 (40k infantry + 10k cavalry) double-enveloped ~86,000 Romans; Roman dead ~70,000 (Polybius) / 48,200 killed + 20,000 captured (Livy); Carthaginian ~5,700–6,000. The decisive mechanism was not attrition but cohesion collapse — surrounded and unable to maneuver, the Roman army disintegrated as a coherent fighting force. *[Polybius/Livy via Dickinson DCC; Britannica; warontherocks 2025]*
*Engine:* a smaller fix+envelop force makes the enveloped unit **shatter** (routs 12/15 with shock on vs 8/15 off), and the shock is morale-driven (collapse → rout), not physical grind; the smaller enveloping force beats the larger. This reproduces disintegration-via-encirclement. Per the PP-683 resolution, the engine delivers this through the moral shock rather than a redundant morale-cap removal — confirmed here.

### 2. Waterloo (1815) — infantry squares defeat cavalry. **MATCH**
*Analysis:* steady, disciplined infantry squares broke repeated French cavalry charges; formed cavalry cannot ride down a formed square. *[established military history; engine cites Courtrai / Swiss / Waterloo]*
*Engine:* braced infantry (CB) holds vs cavalry (mostly draws, infantry HP 340 vs cavalry 276); removing brace lets cavalry break through (wins 4, infantry HP 261, routs 4). The reciprocal charge-recoil shatters a charge driven into a braced + deep + disciplined wall.

### 3. Lanchester — melee is linear, not square. **MATCH**
*Analysis:* Lanchester's Linear Law governs ancient/melee combat — each fighter engages one opponent, casualties are proportional to the combatants in contact, fighting strength scales linearly with group size, and frontage alters a battle's duration, not its outcome. The Square Law (strength ∝ size²) applies only to aimed firearm combat. *[Lanchester via Wikipedia; doolanshire; arXiv 2512.21957 "First Linear Law = ancient cold-weapon"]*
*Engine:* explicitly tunes the Lanchester exponent to ~1 (linear); numerical superiority enters as a linear edge via overlap/envelopment, "never square" (code comment); the `LANCHESTER_ENABLED` toggle confirms the term is wired.

### 4. Command / generalship as force-multiplier. **MATCH**
*Analysis:* superior command repeatedly defeated larger forces (Hannibal at Cannae; Alexander; Napoleon) — generalship is decisive, not a marginal modifier.
*Engine:* command quality dominates outcomes — cmd6 beats cmd2 **20/0**, regardless of the cohesion-pool flag (which modulates only the margin).

### 5. du Picq — morale, not destruction, decides melee. **MATCH**
*Analysis:* Ardant du Picq's *Battle Studies* holds that the unfaceable attack on a pinned unit collapses morale before it inflicts physical destruction; melee is decided by the will to stand. *[du Picq, established; engine cites *Battle Studies*]*
*Engine:* envelop-shock operates on morale (collapses morale → rout); the enveloped unit routs rather than being physically annihilated — the mechanism is psychological, as du Picq argued.

### 6. Sustained combat / rank rotation. **MATCH (qualitative)**
*Analysis:* ancient pitched battles lasted hours, with front ranks rotating to sustain the fight.
*Engine:* battles run multiple turns/phases (up to the 20-turn cap), with front-rank rotation modeled; combat does not resolve in a single exchange.

## Caveats (honest scope)

- The validation is **qualitative / directional** — the engine reproduces the *direction* and *mechanism* of each historical outcome, not calibrated casualty ratios.
- Army-scale multi-unit encirclement (D-3) is not implemented; the Cannae geometry was reproduced with a constructed 2-subunit fix+envelop unit, the engine's available proxy for the fix-and-flank condition.
- Cannae and Lanchester are web-grounded (T1–T2 sources cited); Waterloo and du Picq are stated from established military-historical consensus and the engine's own design citations rather than fresh primary retrieval.

## Sources

- **Cannae:** Britannica; Dickinson College Commentaries (Polybius/Livy); warontherocks (2025); World History Edu.
- **Lanchester:** Wikipedia; doolanshire.net; arXiv 2512.21957; FSU math notes; ScienceDirect.
- **Waterloo squares / du Picq:** established military history; engine design citations (`orchestration.py` comments).
