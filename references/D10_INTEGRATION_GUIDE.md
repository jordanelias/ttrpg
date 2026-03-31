# D10 Success Probability Table — Integration Guide

**Reference:** `d10_success_probabilities.json` (40% success per die: TN7 on d10)

## Skills Using This Table

### 1. valoria-simulator (Mode A — Single Mechanic Isolation)

**When to use:**
- Building probability tables during isolation tests
- Calculating P(≥N successes) for dice pools in scenario resolution
- Validating that pool sizes produce intended success rates

**Lookup pattern:**
```javascript
const prob = lookupTable[trials][successes];
// Example: lookupTable["10"]["5"] → 0.37 (37% chance of 5+ successes in 10 dice)
```

**Integration:**
- Replaced approximation section (lines 128–150 in SKILL.md)
- Quick-reference table embedded for common pools (4D–20D)
- Directs to full JSON for edge cases and non-standard pools

**Output format (Mode A):**
```markdown
## [Mechanic Name]
### Probability Table
| Pool Size | Ob 1 | Ob 2 | Ob 3 | Ob 4 | Ob 5 |
|-----------|------|------|------|------|------|
| 4D | 0.87 | 0.52 | 0.18 | 0.03 | 0.00 |
| 6D | 0.95 | 0.77 | 0.46 | 0.18 | 0.04 |
...
```

---

### 2. valoria-mechanic-audit (Mode B — Number System Coherence)

**When to use:**
- Auditing whether different pool mechanics produce coherent probabilities
- Checking if difficulty scaling (TN/Ob) is consistent across subsystems
- Validating that derived pool sizes don't produce unintuitive cliffs or dead zones

**Typical audit question:**
> "Social combat pools range 1–10D. Combat pools range 2–15D. Are success probabilities comparable at equivalent difficulty?"

**Integration:**
- Added to Mode B procedure (lines 32–41 in SKILL.md)
- Referenced when flagging inconsistencies in number systems
- Used to generate calibration findings

**Output format (Mode B):**
```markdown
### Number System Coherence

#### Dice Pool Probability Calibration
| Subsystem | Min Pool | Max Pool | P(Success) @ Min | P(Success) @ Max | Coherence |
|-----------|----------|----------|------------------|------------------|-----------|
| Social Combat | 1D | 10D | 0.40 | 0.99 | ✓ Linear escalation |
| Combat | 2D | 15D | 0.64 | 1.00 | ⚠ Approaches ceiling early |
...
```

---

## Data Format

All 400 values (20 trials × 20 successes) pre-computed via **binomial CDF**:
- **No approximation** — use for critical edge cases
- **Rounding:** 2 decimal places; 0.00 = probability < 0.005

### Query Structure
```json
{
  "metadata": { ... },
  "table": {
    "1": {"1": 0.40, "2": 0.00},
    "2": {"1": 0.64, "2": 0.16, "3": 0.00},
    ...
    "20": { ... }
  },
  "usage": { "query": "table[trials][successes]", ... }
}
```

---

## Usage Constraints

- **Trials:** 1–20 (extend if mechanics use 20+ dice)
- **Successes:** 1–20 (extend if Ob values exceed 20)
- **Success rate:** Fixed at 40% per die (TN7 on d10)
- **Does NOT account for:** 1s subtracting, chain bonuses, other modifier mechanics

---

## Maintenance

If mechanics change:
1. Update success rate in `metadata.success_probability_per_die`
2. Recompute binomial CDF for all trials/successes
3. Update both skill SKILL.md references
4. Commit to GitHub: `references/d10_success_probabilities.json`

---

## Example: Simulator Mode A Output

**Mechanic:** Social Influence (pool = Rhetoric + History)

```markdown
## Social Influence — Isolation Test

### Input Space
| Variable | Min | Typical | Max |
|----------|-----|---------|-----|
| Rhetoric | 1 | 3 | 5 |
| History | 0 | 2 | 5 |
| Pool | 1D | 5D | 10D |
| Ob | 1 | 2 | 4 |

### Probability Distribution (from d10_success_probabilities.json)
| Pool | Ob 1 | Ob 2 | Ob 3 | Ob 4 |
|------|------|------|------|------|
| 1D | 0.40 | 0.00 | 0.00 | 0.00 |
| 3D | 0.78 | 0.35 | 0.06 | 0.00 |
| 5D | 0.92 | 0.66 | 0.32 | 0.09 |
| 7D | 0.97 | 0.84 | 0.58 | 0.29 |
| 10D | 0.99 | 0.95 | 0.83 | 0.62 |

### Findings
- 1D pool has zero probability above Ob 1: auto-fail at Ob 2+ (degenerate case)
- 10D pool @ Ob 1 effectively auto-succeeds: consider raising minimum Ob
- Success probability scales linearly with pool size (good coherence)
```

---

## Example: Mechanic-Audit Mode B Output

**Subsystem:** Faction Operations (faction stats 1–10)

```markdown
### Number System Coherence: Faction Operations

Faction stats (1–10) derive pool sizes for operations:
- Morale stat → pool = Morale
- Wealth stat → pool = Wealth
- ...

#### Probability Calibration
| Stat | Derived Pool | P(Success, Ob1) | P(Success, Ob2) | P(Success, Ob3) |
|------|--------------|-----------------|-----------------|-----------------|
| 1 | 1D | 0.40 | 0.00 | 0.00 |
| 3 | 3D | 0.78 | 0.35 | 0.06 |
| 5 | 5D | 0.92 | 0.66 | 0.32 |
| 10 | 10D | 0.99 | 0.95 | 0.83 |

#### Findings
- **Coherence Issue (P2):** Stat 1 factions have zero success at Ob 2+. This matches character mechanics (1D auto-fails above certain thresholds) — CONSISTENT.
- **Probability Floor:** Min pool (1D) reaches only 40% success. Consider whether mechanical outcome justifies low floor (e.g., Beginner's Luck exception).
```

---

## GitHub Location

```
jordanelias/ttrpg
├── main
│   └── references/
│       └── d10_success_probabilities.json
```

Loaded by simulator and mechanic-audit on demand.
