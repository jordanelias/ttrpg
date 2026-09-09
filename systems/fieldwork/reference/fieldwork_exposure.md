# VALORIA — FIELDWORK SYSTEM v1.1 — §6 Exposure
## Parent: designs/scene/fieldwork_v30.md
## Status: DESIGN — canonical subsystem file. See parent for full cross-references.
## Mode applicability: TTRPG / Hybrid / Board Game / Godot

## §6 EXPOSURE

Exposure tracks how much attention the character has drawn through their fieldwork activities — both physical (being seen, leaving traces) and social (asking the wrong questions, contacting the wrong people).

### §6.1 Cover (Derived Value)

**Cover = Cognition + most relevant History for concealment/tradecraft.**

Cover determines Exposure thresholds. Higher Cover shifts thresholds upward, paralleling how Endurance determines Stamina capacity and Charisma determines Composure capacity.

| Cover | Noticed | Watched | Compromised |
|-------|---------|---------|-------------|
| 1–3 | 3 | 5 | 7 |
| 4–5 | 4 | 6 | 8 |
| 6–7 | 5 | 7 | 9 |
| 8–9 | 6 | 8 | 10 |
| 10–11 | 7 | 9 | 11 |
| 12+ | 8 | 10 | 12 |

### §6.2 Exposure Track

**Exposure: 0 (start of season in each territory).** Accumulates through fieldwork actions.

| Exposure | State | Consequence |
|----------|-------|-------------|
| Below Noticed | Low profile | No effect. |
| Noticed threshold | Noticed | +1 Ob to all fieldwork rolls in this territory for remainder of season. NPCs at Disposition ≤ 0 become aware of the character's activities. |
| Watched threshold | Watched | The dominant faction in this territory may respond. Church: Heresy Investigation eligible. Crown: arrest or surveillance. Varfell: Tribune counter-intelligence. |
| Compromised threshold | Compromised | Current scene ends. The character must leave the territory or go to ground (1 full scene of inactivity). All NPC Dispositions in this territory: −1. Active investigations in this territory: +2 Ob until Exposure resets. |

### §6.3 Exposure Sources

| Source | Exposure Gained |
|--------|----------------|
| Failed exploration/investigation roll | +1 (Failure) or +2 (if Depth ≥ 3) |
| Thread-Read action | +1 (Thread operations are detectable per params_threadwork.md §Observation) |
| Sensitive character present at Depth 3+ POI | +1 (perceptual engagement detectable) |
| Non-sensitive character present at Depth 3+ POI | +0 (institutionally invisible) |
| Surveil action | +2 (extended conspicuous presence) |
| Failed social action at Disposition ≤ 0 | +1 (hostile NPC may report the interaction) |
| Time in hostile territory | +1 per scene (cumulative) |
| Conspicuous action (contacting known dissidents, entering restricted areas, using Thread operations publicly) | +1 per action |
| Niflhel social action | +2 (conspicuous existence) |

### §6.4 Exposure Reduction

| Method | Exposure Reduced |
|--------|-----------------|
| Successful concealment (Cognition × 2, Ob 2) | −2. Requires one scene of active effort. |
| Leave territory | Reset to 0 in new territory. |
| Season change | Reset to 0 in all territories. |
| Cover identity (requires setup: successful Charisma roll Ob 2 before fieldwork begins) | −1 per scene passively (cover absorbs attention). Cover blown on any Compromised result. |
| Faction support (allied faction uses resources to shield the character) | −2 per season. BG: costs 1 Wealth or 1 Influence. TTRPG: requires a successful Diplomacy or social action (Ob 2) establishing the alliance, or an existing narrative alliance. Hybrid: BG resource cost applies. |

### §6.5 Exposure and Church Attention Pool

In territories where the Church has influence (Piety Track ≥ 3 or Church-controlled), Exposure feeds the Church Attention Pool:
- At Watched threshold: +1 Attention Pool in this territory at next Accounting.
- At Compromised threshold: +1 Attention Pool in this territory immediately. (Not +2 — capped at +1 per character per season to prevent runaway CI acceleration.)

**Cap:** A single character's Exposure contributes at most +1 AP per territory per season. Multiple characters' Exposure in the same territory stacks to a maximum of +2 AP per territory per season from fieldwork sources. This prevents fieldwork-heavy campaigns from generating unbounded CI acceleration through the AP → Heresy Investigation → CI pipeline.

---

## §7 DERIVED VALUES SUMMARY

| Value | Formula | Range | Parallel |
|-------|---------|-------|---------|
| Fieldwork Pool | (Primary Attribute × 2) + History bonus | Variable | Combat Pool; Argue Pool |
| Exploration Ob | Depth base + modifiers | 1–10+ | Ob scale per params_core.md |
| Investigation Threshold | GM-set (3/5/8 by scope) | 3–8 | Clock-style progress track |
| Disposition | Starting value ± social actions | −5 to +5 | Asymmetric per-NPC per-PC |
| Cover | Cognition + most relevant History | 2–14 | Composure (Cha + 6); Stamina (End + Hist + 1) |
| Exposure | 0 + accumulation vs Cover-derived thresholds | 0–10+ | Strain toward Composure threshold |

---

