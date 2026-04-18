<!-- PATCHES APPLIED (session 2026-04-14): PP-600-623 — full Thread system redesign. PP-631 (2026-04-13): POP cap note, Community Organizing pool. PP-632 (2026-04-13): Knot mechanics (pool, tiers, formation, breaking).
     Key changes: pool unified to (Spirit×2)+History+TPS; TN-based difficulty; three-axis Ob;
     Gap self-closure by scale; RS cap struck; WR/WC redesigned; Dissonance→Spirit check.
     All prior pool formulas, Ob tables, and RS cap entries below are superseded by PP-600-623.
     Superseded sections retained for patch history reference. -->

# params_threadwork.md — Thread Operations — CANONICAL STATE 2026-04-14

## Practitioner Stats (PP-616-623 canonical)
| Stat | Range | Description |
|------|-------|-------------|
| Thread Sensitivity (TS) | 0–100 | Perceptual depth. Gates scale access and Distance. |
| Thread Pool Score (TPS) | TS ÷ 10 (round down) | Added to all Thread operation pools. |
| Coherence | 10→0 | Ontological rendering frame. Practitioners only. |
| Spirit | 1–7 | Primary attribute for all Thread operations. |
| Focus | 1–7 | Contact Rounds duration only. Not a pool dice contributor. |

## Thread Pool (PP-616, PP-618, PP-619 — canonical)
**Single formula for ALL Thread operations:**
Pool = (Spirit × 2) + History + TPS

History: 1D per point, cap 3 points. +3D constant (floor) always present.
Full TPS always included. No exceptions.

## Community Organizing — Canonical Pool (PP-616 supersedes PP-250)
**Pool = (Spirit × 2) + History + TPS** (PP-616: all Thread operations unified)
TN: 7 | Ob: 3 | RS outcome: Success = RS +1; Overwhelming = RS +2
Requires: Revolution Mandate ≥ 1. One per contact window round. Not a Domain Action — a Thread operation.
Note: PP-250 Community Organizing formula (Attunement + History + TPS) is superseded by PP-616. (PP-631)


## Knot Mechanics (PP-632 — canonical)

**Ontological basis:** Knots are being-with (Mitsein), not Thread operations. Any character. TS not required.

**Pool = (Bonds × 2) + 3**
| Tier | Point Cost |
|------|-----------|
| Close | 5 |
| Medium | 2 |
| Loose | 1 |

**Max Knot count = floor(Bonds/2)+1**

**Formation:** Max Disposition (floor(Bonds/2)+1) + Connect roll TN 7, Ob = tier + Disposition subtracted. Partial = one tier below.

**Effects:** +1D social with partner; no Disposition decay; shared Composure buffer; relational contagion (P-12) for practitioners; Knot-mediated remote Thread-Read (TS 30+, +1 strain/use).

**Breaking:**
- Rupture: points return; Disposition →−4; Composure damage = tier cost. **Simultaneous Rupture cap (PP-633):** multiple Knots rupturing same scene → total Composure damage capped at floor(Composure×0.75), min = highest single-tier cost. Non-Composure effects uncapped.
- Loss: points return; Disposition track removed; Coherence −1; Composure damage = tier cost

**Threadcut being Knot strain:** +1 self-maintenance strain per Knot use. At 5: rendering instability. −1/season rest.

## TN Modifiers (PP-619 — canonical)
| Operation type | TN |
|---|---|
| All standard operations (Weave, Pull, Mend, Leap, Community Weave) | 7 |
| Binding Ops (Lock, Dissolution) | 8 |
| Past-Oriented Pulling (POP) | 8 |
| POP Binding (Past-Oriented Lock or Dissolution) | 9 |

## Three-Axis Ob System (PP-622, PP-623 — canonical)
**Total Ob = Depth Ob + Breadth Ob + Distance Ob**
TN modifiers apply on top of total Ob.

### Depth Ob — Fibonacci (1, 2, 3, 5, 8, 13)
How primordial is the Thread being engaged? Closest to Ein Sof = hardest.

| Depth | Ob | Mending Ob | TS minimum | Physical scope |
|---|---|---|---|---|
| Object | 1 | n/a | 30+ | One discrete thing |
| Personal | 2 | n/a | 30+ | One person's Thread configuration |
| Relational | 3 | 2 | 50+ | Connections between specific entities |
| Field | 5 | 4 | 50+ | Coherent local area: battlefield, town, valley |
| Structural | 8 | 7 | 70+ | Full regional domain = one BG territory |
| Foundational | 13 | 12 | 90+ | Thread substrate conditions; Calamity wound |

Object-scale Gaps self-close in 1 season with no RS drain. No Mending required.
Mending Depth Ob = Depth Ob − 1 (working with substrate's self-repair tendency).
Foundational Mending: Ob 12. At Foundational depth the self-repair tendency is itself
disrupted; the −1 reduction remains but the base is 13, so Mending is Ob 12.

### Breadth Ob — How much at that depth?
| Breadth | Example | Ob |
|---|---|---|
| Single | One entity, one connection | 0 |
| Small group | 2–10 entities | 1 |
| Formation | 10–1000; a town | 2 |
| Battlefield | 1000–10000; a battle area | 3 |
| Regional | Entire BG territory | 4 |

### Distance Ob — How far from practitioner's body?
| Distance | Range | Ob | TS minimum |
|---|---|---|---|
| Contact/Close | 0–10m | 0 | 30+ |
| Near | 10–100m | 1 | 50+ |
| Distant | 100m–1km | 2 | 70+ |
| Far | 1km+ | 3 | 90+ |

### Probability reference (E[net] per die: TN7=0.4, TN8=0.3, TN9=0.2)
| Pool | TN7 E[net] | TN8 E[net] |
|---|---|---|
| 10D (Beginner) | 4.0 | 3.0 |
| 14D (Capable) | 5.6 | 4.2 |
| 17D (Expert) | 6.8 | 5.1 |
| 20D (Master) | 8.0 | 6.0 |
| 22D (Edeyja) | 8.8 | 6.6 |
SD ≈ 0.8√N. P(success) uses normal approximation with continuity correction.
Key: 22D TN7 Ob13 ≈ 16%. 22D TN7 Ob12 (Foundational Mending) ≈ 22%.

## Gap Self-Closure by Scale (PP-604 — canonical)
Reality self-heals. Rate proportional to disruption scale.

| Gap scale | n | Self-closes after | RS drain/open season | Total untouched | Mending Depth Ob |
|---|---|---|---|---|---|
| Object | 0 | 1 season | 0 | 0 | n/a |
| Relational | 1 | 2 seasons | 1 | 1 | 2 |
| Field | 2 | 4 seasons | 2 | 6 | 4 |
| Structural | 3 | 8 seasons | 3 | 21 | 7 |
| Foundational | 5 | 32 seasons | 5 | 155 | 12 |

Mending Ob = Depth Ob (from table above) + age modifier (0/+1/+2 fresh/established/entrenched).
Lock chronic drift: Object=0; Personal=-1/season; Relational=-1→-2 (season 4+);
  Field=-2→-3; Structural=-3→-5. All per territory with active Lock.

Scale hierarchy rule: Mending at scale X cannot hold while a disruption at scale X+1+
persists in the same area. Must work from deepest disruption upward.

## Dissolution Gap Creation (PP-604 — canonical)
Immediate breach cost: n RS (one-time). Degree determines Gap scale:
- Overwhelming: Gap closes within scene. Breach cost only.
- Success: Gap at target configuration's scale n.
- Partial: Gap at n+1 scale.
- Failure: Gap at n+2 scale.

## RS Track (PP-603 — canonical)
Range 100→0. Seasonal cap: STRUCK (PP-603). Reality takes full consequence.
Starting: TTRPG default 60; BG default 72.
RS = 0: Rupture (shared loss).

## Dissonance — Spirit Check (PP-607, PP-610 — canonical)
When Thread operations fire nearby, character enters Thread-disrupted space, or POP
affects their temporal experience: Spirit check TN7 vs Dissonance Factor.

Dissonance Factor by source:
- Thread operation nearby (brief): 1
- Thread operation nearby (significant): 2
- POP affecting character's own memories: 3
- Entering Field-scale Gap: 2
- Entering Structural-scale Gap: 3
- Extended time in Foundational zone: 4

Failure: Spirit −1D for rest of scene (acute) or season (sustained).
Clears at scene/season end. No permanent penalties.
TS 30+ on Success: readable Thread information (Discovery Event or Belief revision).

## Substrate Saturation Counter (PP-606 — canonical; was Dissonant Counter PP-502)
When ≥ 3 Thread operations fire in a single mass battle turn, substrate saturates:
| Condition | Effect |
|---|---|
| 3+ ops in one battle turn | All subsequent ops that turn: +1 Ob, +1 Coherence cost (cap +2 each) |
| Counter ≥ 3 (cumulative across turns) | All Thread ops in battle zone: +2 Ob remainder of battle |
| Counter ≥ 3 at battle end | RS −1 at next Accounting (PP-600). Hard cap −1/battle. |
Counter resets at battle end. Battle-context Thread Debt expires at battle season end.

## Warden Recognition (WR) — 0–3 (PP-605 — canonical)
Varfell-specific. Gates WC advancement.
| WR | State |
|---|---|
| 0 | Wardens unaware or indifferent |
| 1 | Wardens observed; assessing |
| 2 | Wardens recognise as steward. WC activates. Edeyja engages TS 30+. |
| 3 | Deep trust. Edeyja coordinates Mending. WC can reach 3. |
Advance: Forgetting Check Success +1; Overwhelming +1 additional.
Decrease: TE-13 Military in T15 −1 WR AND −1 WC; RM emergence −2; No expedition 3+ seasons −1.

## Warden Cooperation (WC) — 0–3 (PP-605 — canonical)
Peninsula-wide. Requires WR threshold.
| WC | Effect | WR gate |
|---|---|---|
| 0 | No effect | — |
| 1 | +1D all Thread ops peninsula-wide | WR ≥ 2 |
| 2 | All RS drain from Gaps and Locks halved | WR ≥ 2 |
| 3 | Edeyja actively Mending. RS +2/season. | WR 3 |

## Einhir Foundational Sites (PP-609 — canonical)
The Einhir operated FROM Foundational-stabilized sites, not AT Foundational scale.
Four Foundational conditions they stabilized:
(1) Temporal coherence — things become sequentially and continuously
(2) Spatial extension — things occupy distinct positions
(3) Configurational legibility — Thread configurations are readable
(4) Actualization — configurations are determinate rather than oscillating
T15 Askeheim = most significant stabilization site. Calamity = Structural operation failure
→ stabilization collapse → Foundational Gap network consuming own self-repair context.
Scale hierarchy applies: Edeyja must isolate individual Foundational gaps from network,
Mend at Ob 12 (P≈22% per attempt), then Structural conditions stabilize, then lower
scales self-close naturally. Conflict in Proximity 1–3 territories resets isolation work.

---
