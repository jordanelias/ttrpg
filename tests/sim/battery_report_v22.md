# Battery Band Recalibration Report — v22 Multi-Turn Model (D-8)

**Date:** 2026-05-14
**Sim version:** sim_mb_06_v22.py
**Method:** run_multi_turn_battle, n=40, max_battle_turns=20, T3 equal stats (P4/C4/D5/M6)
**Canonical bands:** tests/sim/sim_mb_06_v9_historical_spec.md

## Results

| ID | Matchup | v22 A% | v22 B% | v9 Band | Status |
|----|---------|--------|--------|---------|--------|
| H1 | Line vs Line (mirror) | 45.0 | 52.5 | 45-55 | OK (noise) |
| H2 | Arrowhead vs Line | 30.0 | 67.5 | 50-65 | REVERSED |
| H3 | Horseshoe vs Line | 17.5 | 82.5 | 50-65 | REVERSED |
| H4 | Horseshoe vs Arrowhead | 2.5 | 97.5 | 40-60 | REVERSED |
| H5 | RefusedFlank vs Horseshoe | 100.0 | 0.0 | 50-65 | OVERSHOOT |
| H6 | RefusedFlank vs Line | 10.0 | 90.0 | 45-60 | REVERSED |
| H7 | GappedLine vs Line | 100.0 | 0.0 | 50-65 | OVERSHOOT |
| H8 | GappedLine vs Arrowhead | 55.0 | 45.0 | 45-60 | OK |

**In-band: 2/8 melee matchups (25%).**

## Analysis

### What the multi-turn model reveals

The v9 single-turn bands were calibrated for one engagement (one call to `run_battle`). The multi-turn model runs 5-10 engagement turns, with between-turn stamina recovery, morale erosion compounding, and discipline degradation. This amplifies small per-turn advantages into decisive outcomes.

### The contact-width effect

The dominant factor in multi-turn outcomes is **contact frontage** — how many cells of unit A are adjacent to cells of unit B during engagement. In `resolve_engagements`, each contact pair generates an attack/defend roll. More contact pairs = more damage dealt and taken per tick.

Formations rank by contact width:
- **GappedLine** (widest): spread cells with gaps. In multi-turn, the wide frontage generates maximum contact. Result: 100% vs Line.
- **RefusedFlank**: asymmetric width, one strong flank. Wide total frontage. Result: 100% vs Horseshoe, but crushed by Line (the refused side gets enveloped over time).
- **Line**: moderate width, solid front. Result: baseline.
- **Arrowhead** (narrow): concentrated tip, narrow contact. Result: loses to Line (fewer contact pairs per turn, but the penetration advantage isn't modeled in multi-turn grinding).
- **Horseshoe** (narrow center, wide wings): the wings don't contact in the current grid model — they advance inward but often miss. Result: effective contact width is just the center, which is narrow. Crushed by everything wider.

### Why this is wrong historically

The historical bands are correct. The sim is wrong. Specifically:

1. **Arrowhead (Wedge)** should beat Line because the concentrated tip PENETRATES and DISRUPTS the line. In the current sim, penetration doesn't confer extra advantage — it just means fewer contact pairs. The wedge tip should cause morale/discipline damage disproportionate to its contact width.

2. **Horseshoe (Envelopment)** should beat Line because the wings wrap around the flanks. In the current grid model, the wings advance toward target_centroid but don't achieve actual flanking. The flanking modifier (YELLOW zone -1D) doesn't fire because the contact detection doesn't distinguish front vs flank contact.

3. **RefusedFlank** works against Horseshoe (historically correct) because the concentrated flank overwhelms one wing. But it fails against Line because the refused side gets ground down — historically, the refused side holds (trading space) while the strong side wins.

### Root cause

`resolve_engagements` treats all contact as equal. There is no:
- **Flanking detection**: cells contacting the enemy's non-front row should apply the octagon facing modifier (YELLOW -1D, RED -2D per §A.4)
- **Penetration bonus**: a wedge tip cell that has advanced past the enemy's front should cause morale shock
- **Formation integrity**: a formation whose shape is disrupted (cells out of pattern) should suffer discipline penalties

These are the mechanics that make historical formation counters work. Without them, raw contact width dominates, which is why wide formations crush narrow ones regardless of their historical purpose.

## Recommendations

### Do NOT change the target bands.

The bands are historically derived and canonically correct. The sim needs to implement the missing mechanics:

1. **Priority: Flanking detection in resolve_engagements** — check if a contact pair involves the enemy's flank/rear cells (non-front row). Apply octagon facing modifier. This is the single most impactful fix — it makes Horseshoe and Arrowhead work.

2. **Formation integrity check** — when cells are displaced from their pattern shape (e.g., a wedge tip has been pushed back, breaking the arrowhead), apply a discipline-like penalty to that atom's combat rolls.

3. **Penetration morale shock** — when a cell advances past the enemy's front row, the enemy gets morale erosion proportional to the penetration depth. Makes Arrowhead punch above its contact width.

### Interim: adjusted bands for multi-turn WITHOUT flanking

If the above mechanics are deferred, the current multi-turn model produces a different game — one where wide formations always win. Interim bands would be:

| ID | Matchup | Interim Band | Notes |
|----|---------|-------------|-------|
| H1 | Line vs Line | 45-55 | unchanged |
| H2 | Arrowhead vs Line | 25-40 | reversed (no penetration) |
| H3 | Horseshoe vs Line | 15-30 | reversed (no flanking) |
| H7 | GappedLine vs Line | 85-100 | contact width dominates |
| H8 | GappedLine vs Arrowhead | 45-65 | close to original |

These interim bands are WRONG historically but describe the current sim's behavior. They should NOT be used as design targets.

## Conclusion

D-8 diagnosis is complete. The battery recalibration surfaces a fundamental missing mechanic: **flanking detection in resolve_engagements**. Without it, the multi-turn model's compounding amplifies contact width into the only meaningful shape differentiator. The fix is mechanical (implement flanking), not parametric (change bands).

[ASSUMPTION: contact width is the primary factor in multi-turn outcomes — basis: GappedLine 100% win rate vs Line despite equal stats; formations with narrow frontage (Horseshoe, Arrowhead) lose consistently]
[CONFIDENCE: high — results consistent across seed sets; root cause identified via formation contact-width ranking]
