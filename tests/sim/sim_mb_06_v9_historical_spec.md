# SIM-MB-06 v9 Historical Accuracy Specification
# Date: 2026-05-12
# Status: SPEC — drives v9 battery targets
# Companion: references/historical/precedents_warfare.md §1.1; mass_battle_v30.md §A.6, §A.8

## Scope

This spec maps each atom-shape and formation matchup to an expected win-rate band
grounded in (a) the design doc's explicit formation counter logic (§A.6, §A.8 of
mass_battle_v30.md) and (b) historical precedent from the warfare precedents
reference. Used to validate that v9 produces historically defensible battle results.

## Atom-shape → historical formation mapping

| Atom shape   | Historical formation     | Period exemplar                          |
|--------------|--------------------------|------------------------------------------|
| Line         | Linear/Phalanx           | Greek hoplite phalanx; Roman triplex acies front |
| Arrowhead    | Wedge (cuneus)           | Macedonian wedge; Roman cuneus; Norman conroi   |
| Horseshoe    | Envelopment / Crescent   | Cannae (Hannibal, 216 BC); Mongol tulughma     |
| GappedLine   | Manipular checkerboard   | Roman manipular legion (vs phalanx, Pydna 168 BC) |
| RefusedFlank | Refused flank / Oblique  | Leuctra (Epaminondas, 371 BC); Leuthen (Frederick II) |

## Unit-type → historical role mapping

| unit_type | Historical role             | Combat doctrine                       |
|-----------|------------------------------|---------------------------------------|
| melee     | Heavy/light infantry, cavalry | Engages at contact (existing v8 logic) |
| ranged    | Archers, crossbows, slingers | Fires in Phase 2 (before close); see Volley |
| (future)  | Cavalry (Speed-Fast melee)   | Out of scope for v9                   |

## Historical win-rate target bands

Targets derived from (i) the §A.6 formation counter table dice modifiers,
(ii) §A.8 tactical counters, and (iii) historical battle outcomes. Where
the design doc gives mechanical modifiers, the band is set by translating
the dice differential into win-rate at equal Power/Command/Discipline; where
only historical narrative is available, the band is wider.

### Equal-quality melee matchups (T3, equal Power=4, Command=4, Discipline=5)

| # | Matchup                          | Target band | Source                                   |
|---|----------------------------------|-------------|------------------------------------------|
| H1 | Line vs Line (mirror)            | 45–55%      | Sanity: symmetric. Mirror bias <±8pp.    |
| H2 | Arrowhead (Wedge) vs Line        | 50–65%      | §A.6: Wedge +2D off / −1D def vs Line.   |
|   |                                  |             | Historical: cuneus consistently broke    |
|   |                                  |             | linear formations of equal quality.      |
| H3 | Horseshoe (Envelopment) vs Line  | 50–65%      | Cannae (216 BC): envelopment destroys    |
|   |                                  |             | linear advance. Refused Flank is the     |
|   |                                  |             | named counter, not Line.                 |
| H4 | Horseshoe vs Arrowhead (Cannae)  | 40–60%      | §A.8: Envelopment beats single-axis      |
|   |                                  |             | advance (Wedge is single-axis). Cannae   |
|   |                                  |             | proper. Tight band — wedge tip can       |
|   |                                  |             | still punch if center holds.             |
| H5 | RefusedFlank vs Horseshoe        | 50–65%      | §A.8: Refused Flank is explicit          |
|   |                                  |             | Envelopment counter. Leuctra precedent.  |
| H6 | RefusedFlank vs Line             | 45–60%      | Oblique order (Frederick II, Leuthen):   |
|   |                                  |             | concentrates one flank, slight edge.     |
| H7 | GappedLine (Manipular) vs Line   | 50–65%      | Pydna 168 BC: Roman maniples broke       |
|   |                                  |             | Macedonian phalanx via gap-flexibility.  |
| H8 | GappedLine vs Arrowhead          | 45–60%      | Maniples could absorb wedge penetration  |
|   |                                  |             | and flank it. Slight edge to GappedLine. |

### Reversed matchups (for asymmetry confirmation)

| # | Matchup                          | Target band | Note                                       |
|---|----------------------------------|-------------|--------------------------------------------|
| H9 | Line vs Arrowhead                | 35–50%      | Inverse of H2.                            |
| H10| Line vs Horseshoe                | 35–50%      | Inverse of H3.                            |
| H11| Arrowhead vs Horseshoe           | 40–60%      | Symmetric with H4 (different A/B side).   |

### Ranged unit matchups (v9 introduces troop_type='ranged')

| # | Matchup                              | Target band | Source                              |
|---|--------------------------------------|-------------|-------------------------------------|
| R1 | Pure Ranged vs Pure Line (open field) | 30–50%     | §A.7 PP-503: Volley pool = Power    |
|   |                                       |             | only (1-7), TN 6. Open ground:      |
|   |                                       |             | melee closes and routs ranged.      |
|   |                                       |             | Crécy/Agincourt won only with       |
|   |                                       |             | terrain/stakes (out of scope).      |
| R2 | Ranged + Line vs Line+Line (combined) | 55–70%     | Combined arms beats pure melee.     |
|   |                                       |             | Hastings, Crécy pattern.            |
| R3 | Ranged sanity: Ranged vs Ranged       | 45–55%     | Mirror sanity for new unit_type.    |

### Lethality targets

| # | Metric                       | Target | Source                                       |
|---|------------------------------|--------|----------------------------------------------|
| L1 | Mean turns to resolve (Line mirror, T3) | 3–6   | v8 SIM-MB-05A baseline; v8 currently 9.8 (OPEN) |
| L2 | Draw rate (T3 matchups)      | <15%   | Battles should resolve before max_turns      |
| L3 | One-turn kills (any matchup) | 0      | v8 SIM-MB-05A regression test                |

## Lethality interaction note

v8 closed with two open tensions: G (Horseshoe vs Line 31.7% — below H3 band) and H
(lethality t=9.8 — above L1 band). H3 is the diagnostic test for G; L1 for H. v9 work
should resolve both as side-effect of correctly modeling the formation counters, not via
ad-hoc damage multipliers.

## What NOT to over-fit

- Specific battle outcomes (Cannae 50,000 destroyed 86,000) cannot be replicated by
  a sim that doesn't model the *specific* terrain/command/morale conditions of those
  battles. The targets are *bands* representing the general pattern, not exact reproduction.
- Refused Flank as a defensive posture is structurally weaker on attack — its narrow band
  in H5/H6 reflects that.
- Wedge advantage (H2) assumes equal Power/Command; against superior generalship, a Line
  with better commander still wins (Agincourt: English archers + Henry V vs French knights
  with no unified command).

## Non-targets (out of scope for v9)

- Shield Wall (separate formation_modifier, not yet implemented)
- Skirmish (separate unit_type)
- Cavalry (Speed-Fast melee with charge bonus)
- Terrain modifiers (§A.9)
- Thread operations (§A.10)
- Combined Power-Command effects (all matchups assume equal-stat units)

These are deferred to v10+. The v9 targets above use uniform Power=4, Command=4,
Discipline=5, Morale=6 to isolate formation/unit_type effects.
