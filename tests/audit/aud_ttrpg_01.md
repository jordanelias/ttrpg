# TTRPG Mode Mechanic Audit — AUD-TTRPG-01
## Date: 2026-04-02
## Modes run: A (Formula), B (Number Systems), C (Interaction Chains), D (Gap Detection), E (Core Principles), F (Playtest Burden), G (Cross-Mode)
## Sources: params_core, params_combat, params_threadwork, params_debate, params_factions, params_scale_transitions, stage1, stage2, stage10, stage11, stage12, stage13, canon/02_canon_constraints.md

---

## Mode A — Formula Validation

| ID | Formula | Min | Max | Issues | Severity |
|----|---------|-----|-----|--------|----------|
| FA-01 | Pool = Attribute + (History pts + 3) | 6 | 18 | Attr min=1 assumed — no explicit floor in params | P3 |
| FA-02 | Combat Pool = (Agility×2)+History+3, min 5 | 5 | 23+ | No pool cap stated | P2 |
| FA-03 | Stamina = Endurance+History+1 (−armour mod) | 0 (underflow) | — | Stamina can reach ≤0 before combat with Endurance 1 + Heavy armour (−2 mod) → Out of Breath forced at round start | P1 |
| FA-04 | Damage = excess successes + STR + weapon mod | 2 | uncapped | Critical (excess≥3): weapon mod doubled — no damage ceiling | P2 |
| FA-05 | Max Wounds = f(Endurance) | — | — | Gap at Endurance 0 — if Endurance min=1, no issue. Confirm range. | P3 |
| FA-06 | TPS = TS÷10 (round down) | 3 (TS 30) | 10+ | No ceiling concern for TS≤100; TS>100 undefined | P3 |
| FA-07 | Leap Pool = Attunement+History+TPS | — | — | Minimum pool: core min 1D applies but not cross-referenced in Leap section | P3 |
| FA-08 | Composure = Presence+6 (NPC formula) | — | — | PC Composure formula absent from all player-facing rules | P1 |
| FA-09 | Debate pool = (Presence×2)+History bonus | 2 | 20 | OK |  |
| FA-10 | Conviction movement = ⌊(margin×genre_wt×orient_wt)−resistance⌋ | 0 | — | Floor correctly 0. OK |  |
| FA-11 | Inspiration: total ≤ Resolve; individual ≤ Spirit | — | — | Dual caps — interaction when total cap = individual cap = Spirit not stated explicitly | P2 |
| FA-12 | Fork = +1D per 3 full points (min +1D if any) | +1D | +3D+ | "minimum +1D if any points" conflicts with "+1D per 3 full points" — additive or floor? | P2 |
| FA-13 | +1 Ob per Wound | +0 | +4 Ob | OK |  |
| FA-14 | Domain Action Ob = target faction stat | 1 | 7 | Ethical framework modifier + other mods — stack order and Ob cap not stated for domain actions | P2 |
| FA-15 | RS thread op costs by degree | — | — | No RS=0 lockout gate defined | P1 |

---

## Mode B — Number System Coherence

| System | Range | Issues | Severity |
|--------|-------|--------|----------|
| Attributes | 1–5 (inferred) | Max not in params_core — only in CP table | P2 |
| History points | 0–Memory | Memory range/start undefined | P1 |
| Thread Depth (TD) | 0–10 | Defined but unused in any formula | P2 (dead stat) |
| Rendering Stability | 100→0 | No ceiling for restoration above 100 | P2 |
| Coherence | 10→0 | Starting value unconfirmed in params | P2 |
| Focus | 1–5+ | Derivation absent — attribute, derived, or purchased? | P1 |
| RS start (TTRPG) | Conflict | params_factions: 60 vs stage12: 72 | P1 |
| Faction stat floor | 1–7 | Behaviour at 0 undefined | P2 |
| TS ceiling | 0–100+ | No hard upper bound; TPS grows indefinitely | P3 |

---

## Mode C — Interaction Chain Analysis

| ID | Chain | Flag | Severity |
|----|-------|------|----------|
| IC-01 | Belief → CP award | Two contradictory CP tables (stage2 §4.2 vs stage10 §10.2) | P1 |
| IC-02 | Domain Echo | "Sufficient scope" undefined — GM narrative call with no mechanical gate | P2 |
| IC-03 | Combat pool allocation | Offence/Defence split procedure not documented | P2 |
| IC-04 | Thread op → RS=0 | No lockout; chain continues to undefined state | P1 |
| IC-05 | Personal→Faction transition | "Same roll, two Obs" — unclear if net checked twice | P2 |
| IC-06 | Faction unique actions | 4 factions missing unique action documentation | P1 |
| IC-07 | Domain Action CP | No structured award formula — full GM discretion | P2 |
| IC-08 | Wound dual penalty | −1D/wound AND +1Ob/wound — cumulative effect not quantified | P2 |

---

## Mode D — Gap Register (new entries)

| ID | Type | Description | Location | Severity | Status |
|----|------|-------------|----------|----------|--------|
| GAP-TTRPG-01 | Missing formula | PC Composure formula | stage2, params_core | P1 | Open |
| GAP-TTRPG-02 | Missing definition | Memory score: range, start, derivation | stage2, params_core | P1 | Open |
| GAP-TTRPG-03 | Missing definition | Focus score derivation | params_threadwork | P1 | Open |
| GAP-TTRPG-04 | Conflicting tables | Belief CP awards stage2 vs stage10 | stage2 vs stage10 | P1 | Open |
| GAP-TTRPG-05 | Missing rule | RS=0 lockout gate | params_threadwork | P1 | Open |
| GAP-TTRPG-16 | Clock conflict | RS start: 60 (params_factions) vs 72 (stage12) | params_factions, stage12 | P1 | Open |
| GAP-TTRPG-17 | Missing content | Hafenmark/Guilds/Niflhel/Löwenritter unique actions | params_factions | P1 | Open |
| GAP-TTRPG-21 | Stamina underflow | Stamina ≤0 before combat at Endurance 1 + Heavy armour | params_combat | P1 | Open |
| GAP-TTRPG-06 | Missing rule | Domain Echo scope trigger | stage11 | P2 | Open |
| GAP-TTRPG-07 | Missing procedure | Offence/Defence allocation declaration | params_combat | P2 | Open |
| GAP-TTRPG-08 | Orphaned stat | Thread Depth (TD) defined but unreferenced by formulas | params_threadwork | P2 | Open |
| GAP-TTRPG-09 | Missing start value | Coherence starting value | params_threadwork | P2 | Open |
| GAP-TTRPG-10 | Missing ceiling | RS restoration above 100 | params_threadwork | P2 | Open |
| GAP-TTRPG-11 | Missing range | Attribute max not in params | params_core | P2 | Open |
| GAP-TTRPG-12 | Ambiguity | Fork rule minimum vs per-3-points | stage2 | P2 | Open |
| GAP-TTRPG-13 | Ambiguity | Inspiration dual caps interaction | stage2, stage10 | P2 | Open |
| GAP-TTRPG-14 | Missing ceiling | Combat pool cap | params_combat | P2 | Open |
| GAP-TTRPG-15 | Missing behaviour | Faction stat at 0 | params_factions | P2 | Open |
| GAP-TTRPG-18 | Ambiguity | Personal→Faction same-roll two-Ob check | stage11 | P2 | Open |
| GAP-TTRPG-19 | Missing structure | Domain Action CP award formula | stage10 | P2 | Open |
| GAP-TTRPG-20 | Missing ceiling | TS hard upper bound | params_threadwork | P3 | Open |
| GAP-TTRPG-22 | Quantification gap | Wound dual penalty cumulative effect | params_combat | P2 | Open |

---

## Mode E — Core Principles Compliance

| # | Principle | Status | Notes |
|---|-----------|--------|-------|
| 1 | Roll only when meaningful | PRESENT | Let It Ride §1.5 |
| 2 | Let It Ride | PRESENT | §1.5 |
| 3 | Fail Forward | PRESENT | §1.6 |
| 4 | Histories not Skills | PRESENT | §4.1 |
| 5 | Pool = Attribute + History bonus | PRESENT | Consistent across all systems |
| 6 | Wound escalating Ob | PRESENT | +1Ob/wound confirmed |
| 7 | Inspiration/Spirit economy | PRESENT | §4.3 |
| 8 | Beliefs as moral character | ALTERED | Maxims cut; stage10 still references Maxims in CP table — stale reference | P2 |
| 9 | Social combat via Rhetoric | PARTIAL | Debate present; Negotiation absent as distinct system | P2 |
| 10 | Reach/Speed priority | PRESENT | |
| 11 | Phase-based combat | ALTERED | Phase structure implicit in personal combat but not formally stated | P2 |
| 12 | Beginner's Luck | PRESENT | §1.8 |
| 13 | Circles and Resources | PRESENT | CP table confirmed |

---

## Mode F — Playtest Burden

| Mechanic | Time(s) | Lookups | Tracking | Decisions | Load | Flag |
|----------|---------|---------|----------|-----------|------|------|
| History roll | 30 | 0 | 1 | 1 | Low | — |
| Personal combat round | 90 | 2 | 5 | 3 | High | P1: >90s + 5 parallel tracks every round |
| Thread Leap | 60 | 3 | 4 | 2 | High | P2 |
| Thread operation (e.g. Weave) | 90 | 4 | 6 | 3 | High | P1: highest-burden mechanic in system |
| Debate exchange | 75 | 3 | 5 | 4 | High | P2 |
| Domain Action | 30 | 1 | 2 | 1 | Low | — |
| Seasonal Accounting | 900 | Multiple | All clocks + faction stats | Many | High | P2: no GM checklist |
| Inspiration Stunt | 45 | 1 | 3 | 2 | Medium | — |

---

## Mode G — Cross-Mode Consistency

| Mechanic | Modes | Transition Defined? | State Preserved? | Flag |
|----------|-------|---------------------|------------------|------|
| Faction stats | ALL | Minimal (one sentence) | Yes | P2: no formal handoff sheet |
| TC/RS/IP clocks | ALL | Implied | Yes | P1: RS start conflict compounds at mode switch |
| Personal characters | TTRPG/HYB | "Suspended" only | Unknown | P1: reactivation procedure undefined |
| Thread operations | TTRPG/HYB | Absent in BG | N/A | P2: no BG abstraction for Thread→faction effects |
| Personal↔Unit combat | HYB | Not defined | N/A | P1: HYB personal/unit transition missing |
| Debate | TTRPG/HYB | BG substitution informal | Partial | P2: no documented substitution rule |
| CP/Advancement | TTRPG only | Undefined on switch | Unknown | P2: no rule for CP accrued across mode switches |

---

## Summary

**P1 count: 11**
**P2 count: 14**
**P3 count: 4**

### Top P1s requiring editorial attention:
- GAP-TTRPG-04: Belief CP conflict (stage2 vs stage10) — resolve immediately
- GAP-TTRPG-16: RS starting value conflict — resolve immediately  
- GAP-TTRPG-01: PC Composure formula — define and add to params
- GAP-TTRPG-02/03: Memory and Focus undefined — define in params
- GAP-TTRPG-21: Stamina underflow — patch params_combat with minimum stamina=1 or armour exclusion rule
- GAP-TTRPG-17: 4 faction unique actions missing — extract from stage6

### Recommended next actions (priority order):
1. PATCH: Resolve GAP-TTRPG-04 (Belief CP conflict) — one table is wrong, editorial decision needed
2. PATCH: Resolve GAP-TTRPG-16 (RS start) — params_factions or stage12 needs correction
3. PATCH: Add PC Composure = Presence + 6 to params_debate and stage2 (if same as NPC formula — confirm)
4. EXTRACT: Read stage6 §8.4–8.8 for missing faction unique actions
5. PATCH: Stamina minimum = 1 rule in params_combat
6. DEFINE: Memory (range: 1–5? tied to attribute?), Focus (derived how?)
