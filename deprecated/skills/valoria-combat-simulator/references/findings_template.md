# Findings Template

Use this structure for every simulation run output file.

---

# Combat Simulation — Run [N]

**Parameters:** Str [X] / End [X] / Agi [X], [Proficiency] (Combat Pool [N]), Health [N]  
**Stamina:** None/Light=[N], Medium=[N], Heavy=[N]  
**N fights:** [N] per matchup | **Max rounds:** [N]  
**Valid builds:** [N] | **Matchups:** [N]  
**Date:** [session date]

---

## Top / Bottom Builds

| Rank | Weapon | Armour | Avg Win% |
|---|---|---|---|

---

## Balance Flags

### P1 Issues (>85% win rate, non-mirror)
[List matchups]

### P2 Issues (70–85% win rate, non-mirror)
[List matchups — top 10 only unless instructed otherwise]

### Reach Findings
- Short vs Long avg win rate: [X]%
- Expected (with manoeuvre): [X]% — [above/below threshold]
- Versatile vs Long same-weight: [X]% gap

---

## Findings

### F-SIM-[RUN]-[NNN] — [Title] — Priority [P1/P2/P3]
**Observation:** [What the data shows]  
**Root cause:** [Mechanical reason]  
**Implication:** [Design consequence]  
**Patch options:**
- A: [option]
- B: [option]

---

## Model Notes
[Any simulation assumptions that affected results — e.g., always-contest strategy,
wounds not modelled, manoeuvre success rate at given Agi]

---

## Patch Proposals Generated

| ID | Component | Finding | Priority |
|---|---|---|---|
| PP-SIM-[N] | | | |

---

## Raw Results (sorted by A Win%)

[Full matchup table]
