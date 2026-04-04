# SIM-DEBT-01 RESOLUTION — Debate System Re-Simulation
## ID: SIM-D-05
## Date: 2026-04-03
## Pool: (Cognition × 2) + History | Initiative: Attunement | TN 7
## Source: designs/debate/debate_system_redesign_v1.md Part 6 (as corrected by PP-232)
## Modes: A (isolation), D (full scenarios + edge cases), J (cognitive load), L (precedent comparison)
## n = 10,000 per scenario

---

## PRE-SIM NOTE — Design Doc Conflict
Part 6 v1.6 body text says pool = (Presence × 2) + History. Stale — PP-232 corrected to (Cognition × 2) + History.
params_debate.md header is authoritative. Part 6 body requires update. Filed PP-233.

---

## MODE A: ARGUE POOL ISOLATION (CLASH, genre_weight=1.0, resistance=1)

| Matchup | A Pool | B Pool | A Win% | B Win% | Tie% | Avg Δ/xch |
|---------|--------|--------|--------|--------|------|-----------|
| Scholar v Scholar    | 11 | 11 | 41.9% | 41.7% | 16.4% | +0.16 |
| Scholar v Diplomat   | 11 |  8 | 62.3% | 21.6% | 16.1% | +0.92 |
| Scholar v Novice     | 11 |  5 | 83.6% |  6.4% | 10.0% | +1.75 |
| Veteran v Scholar    |  9 | 11 | 27.6% | 55.6% | 16.8% | −0.36 |
| Inquisitor v Scholar | 10 | 11 | 34.4% | 48.1% | 17.5% | −0.07 |
| Diplomat v Orator    |  8 |  8 | 39.6% | 40.7% | 19.7% | +0.20 |
| Novice v Novice      |  5 |  5 | 37.0% | 38.1% | 24.9% | +0.23 |

## ARGUE POOL SUMMARY TABLE

| Character | Cog | Hist | Pool | Read (Att) | Composure | Concentration |
|-----------|-----|------|------|-----------|-----------|---------------|
| Scholar    | 4 | 3 | 11 | 3 | 7 | 6 |
| Diplomat   | 3 | 2 |  8 | 3 | 8 | 7 |
| Inquisitor | 4 | 2 | 10 | 4 | 8 | 7 |
| Novice     | 2 | 1 |  5 | 2 | 7 | 4 |
| Veteran    | 3 | 3 |  9 | 4 | 8 | 6 |
| Orator     | 3 | 2 |  8 | 3 | 9 | 7 |

## MODE A: GENRE WEIGHT IMPACT (Scholar v Diplomat, res=1)
Genre weight affects Conviction Track movement rate only — not win probability (Finding A-1).

| Weight | A Win% | B Win% | Avg Δ/xch |
|--------|--------|--------|-----------|
| ×0.5 | 62.8% | 21.4% | +0.31 |
| ×1.0 | 62.6% | 21.6% | +0.93 |
| ×1.5 | 62.9% | 21.1% | +1.44 |

## MODE A: RESISTANCE IMPACT (Scholar v Diplomat, gw=1.0)

| Resistance | A Win% | Avg Δ/xch |
|-----------|--------|-----------|
| 0 | 62.8% | +1.37 |
| 1 | 62.9% | +0.96 |
| 2 | 63.4% | +0.61 |
| 3 | 63.0% | +0.38 |

## MODE A: MEMORY BONUS +2D

| Config | A Win% | B Win% | Avg Δ/xch |
|--------|--------|--------|-----------|
| A+0D v B+0D | 63.2% | 20.9% | +0.94 |
| A+0D v B+2D | 47.4% | 34.9% | +0.41 |
| A+2D v B+0D | 74.5% | 13.7% | +1.53 |
| A+2D v B+2D | 60.8% | 24.5% | +0.92 |

---

## MODE D: FULL FORMAL DEBATE (3 exchanges, start=5, res=1)

| Matchup | A Win% | B Win% | Compromise% |
|---------|--------|--------|------------|
| Scholar v Scholar    | 33.0% | 27.9% | 39.1% |
| Scholar v Diplomat   | 66.9% |  6.0% | 27.1% |
| Scholar v Novice     | 94.1% |  0.3% |  5.6% |
| Inquisitor v Veteran | 44.7% | 17.9% | 37.4% |
| Diplomat v Orator    | 31.2% | 24.0% | 44.8% |
| Novice v Novice      | 30.1% | 19.8% | 50.1% |
| Scholar v Veteran    | 47.8% | 15.4% | 36.8% |

## MODE D: GRAND DEBATE (5 exchanges)

| Matchup | A Win% | B Win% | Compromise% |
|---------|--------|--------|------------|
| Scholar v Scholar    | 40.1% | 35.5% | 24.4% |
| Scholar v Diplomat   | 79.0% |  6.7% | 14.3% |
| Scholar v Novice     | 99.6% |  0.1% |  0.4% |
| Inquisitor v Veteran | 57.8% | 17.6% | 24.5% |
| Diplomat v Orator    | 36.1% | 33.2% | 30.7% |
| Novice v Novice      | 36.8% | 28.1% | 35.1% |
| Scholar v Veteran    | 66.1% | 14.1% | 19.7% |

## MODE D: CHURCH TRIBUNAL (asymmetric, CT starts 6, Past ×1.5)

| Setup | Inq Win% | Accused Win% | Compromise% |
|-------|----------|-------------|-------------|
| Inq v Novice (1 xch)  | 73.4% |  0.6% | 25.9% |
| Inq v Novice (3 xch)  | 96.1% |  0.2% |  3.7% |
| Inq v Scholar (1 xch) | 36.8% | 18.3% | 44.9% |
| Inq v Scholar (3 xch) | 39.5% | 31.9% | 28.6% |
| Inq v Veteran (1 xch) | 48.4% |  8.9% | 42.7% |
| Inq v Veteran (3 xch) | 63.8% | 13.1% | 23.1% |

## MODE D: STRAIN ARC — P(Rattled), 3 exchanges

| Matchup | Composure | P(Rattled) |
|---------|-----------|-----------|
| Scholar v Scholar (mirror) | 7 |  6.9% |
| Novice v Novice (mirror)   | 7 |  1.0% |
| Scholar v Inquisitor        | 7 |  3.4% |
| Scholar v Diplomat          | 7 |  0.6% |
| Diplomat v Scholar          | 8 | 17.1% |

## MODE D: CONCENTRATION DEPLETION (5-exchange Grand Debate)

| Scenario | Result |
|----------|--------|
| Scholar v Scholar (Conc=6) | 54.6% chance any Spent triggers |
| Novice v Novice (Conc=4)   | 100% fully exhausted by end |

---

## MODE L: FORMULA COMPARISON

| Formula | Scholar Pool | Diplomat Pool | Scholar Win% | Diplomat Win% |
|---------|-------------|--------------|-------------|--------------|
| Old (Presence×2+Hist) |  9 | 10 | 33.9% | 47.8% |
| New (Cognition×2+Hist) | 11 |  8 | 62.9% | 20.6% |

PP-232 validated. Old formula inverted design intent — high Presence dominated. New formula correctly makes Cognition the debate attribute.

---

## FINDINGS SUMMARY

| ID | Sev | Finding | Action |
|----|-----|---------|--------|
| F-SIM-D05-01 | P1 | Part 6 body text uses stale pool formula (Presence×2) | PP-233: doc fix |
| F-SIM-D05-02 | P2 | Scholar v Novice near-deterministic (94–99%) | GM guidance note |
| F-SIM-D05-03 | P2 | Novice Grand Debate always hits Spent — snowball risk | GM guidance: Formal only for low-stats |
| F-SIM-D05-04 | P2 | Resistance >2 with ≤3 exchanges rarely decisive | GM guidance to §6.7 |
| F-SIM-D05-05 | P3 | Orator (Pres5/Cog3) very weak in Formal Debate | ED-134 flagged |
| F-SIM-D05-06 | INFO | PP-232 validated — design intent confirmed | Close SIM-DEBT-01 |
| F-SIM-D05-07 | INFO | §6.7 Tribunal design note (PP-109) confirmed | No action |

## EDITORIAL FLAGS
[EDITORIAL: ED-134 — Orator archetype (high Presence, avg Cognition) mechanically weak in Formal Debate
under PP-232. Confirm intended: Orators are not Formal Debate characters. If not intended, consider
Presence modifier to Argue pool for non-formal contexts or dedicated Mass Address mechanic.]

## SIM-DEBT STATUS
- SIM-DEBT-01: RESOLVED
- SIM-DEBT-02: Corroboration in CLASH calibration — still open

## NEW BASELINES

| Matchup | Pool (A/B) | Formal Win% (A/B/Comp) | Grand Win% (A/B/Comp) |
|---------|-----------|----------------------|----------------------|
| Scholar v Scholar  | 11/11 | 33/28/39% | 40/36/24% |
| Scholar v Diplomat | 11/8  | 67/6/27%  | 79/7/14%  |
| Scholar v Novice   | 11/5  | 94/0/6%   | 99/0/1%   |
| Diplomat v Orator  | 8/8   | 31/24/45% | 36/33/31% |
| Inq v Veteran      | 10/9  | 45/18/37% | 58/18/25% |
| Novice v Novice    | 5/5   | 30/20/50% | 37/28/35% |
