<!-- PATCHES APPLIED (session 2026-04-14): PP-600-623 — full Thread system redesign. PP-631 (2026-04-13): POP cap note, Community Weaving pool corrected to (Spirit×2)+History+TPS.
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

## Community Weaving — Canonical Pool (PP-616 supersedes PP-250)
**Pool = (Spirit × 2) + History + TPS** (PP-616: all Thread operations unified)
TN: 7 | Ob: 3 | RS outcome: Success = RS +1; Overwhelming = RS +2
Requires: Revolution Mandate ≥ 1. One per contact window round. Not a Domain Action — a Thread operation.
Note: PP-250 Community Weaving formula (Attunement + History + TPS) is superseded by PP-616. (PP-631)

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
## SUPERSEDED SECTIONS (patch history reference — values below are stale)
<!-- All pool formulas, Ob tables, and RS entries prior to PP-600 are superseded.
     Retained below for traceability. Do not use for mechanical reference. -->


<!-- version: v0.14-AUD3-R1 | source: threadwork_v30.md | last_updated: 2026-04-03 -->
<!-- PATCHES APPLIED (canonical): PP-107, PP-166, PP-168, PP-181–182, PP-190–209, PP-221, PP-223–226, PP-232, PP-239–240, PP-250, PP-252–253, PP-258, PP-260–261, PP-263–265, PP-279, PP-281, PP-289–290, PP-303–304, PP-314–315, PP-330, PP-387, PP-389, PP-397, PP-497, PP-502, PP-551, PP-553, PP-555, PP-581, PP-583, PP-590, PP-600–610, PP-616–623 -->
<!-- PP-232: Leap pool adds Spirit; Leap Failure outcome corrected; POP TN corrected to 8; sequential failure rule corrected; -->
<!--         Weaving Structural Ob corrected to 8; Diagnosis struck ED-134; FR term flagged ED-135 (open); ED-030/034/121/124/134 resolved 2026-04-03. -->
<!-- stage3_thread_operations.md is EMPTY in v0.14. All values from threadwork_v30.md. -->
<!-- STALE CHECK: All values [PROPOSAL]. Verify against compiled stage3 before use. -->

# params_threadwork.md — Thread Operations (v2.5)

## Practitioner Stats
| Stat | Range | Description |
|------|-------|-------------|
| Thread Sensitivity (TS) | 0–100 | Perception depth. Hard cap: 100. |
| Rendering Stability (RS) | 100→0 | World coherence (shared track) |
| Coherence | 10→0 | Personal rendering stability |
| Focus | 1–7 | Contact duration in rounds |
| Thread Pool Score | Thread Sensitivity ÷ 10 (round down) | Thread Pool Score — added to operation pools |


## RS=0 Lockout (PP-166)
Thread operations **cannot be attempted** when RS = 0. The substrate has no remaining integrity to engage. All Leap eligibility checks fail automatically at RS = 0. RS = 0 triggers the Rupture (shared loss condition — see stage12_campaign_modes §12.2).

## RS Ceiling
RS maximum: **100**. RS cannot exceed 100 through any restoration effect. If a restoration result would push RS above 100, RS = 100.

## Coherence Starting Value
Coherence starts at **10** for all characters (confirmed: stage1_core_engine §2.3). Counts down toward 0. Recovery per stage1 derived stats table.

## Thread Depth (TD) — REMOVED (PP-166)
Thread Depth (TD) was defined in prior params versions as a stat with range 0–10. It does not appear in threadwork_v30.md or any current operation formula. **TD is a phantom definition from a prior design iteration — it has no mechanical function and is not tracked.** Removed from all params files.

## Leap Roll
Pool: Spirit + Attunement + relevant History bonus + Thread Pool Score | TN: 7 (PP-232)
| Thread Sensitivity | Ob | Wound modifier |
|----|----|-|
| 30–49 | 2 | +1 Ob per Wound |
| 50+ | 1 | +1 Ob per Wound |

| Degree | Outcome |
|--------|---------|
| Overwhelming | Clean suspension. Next op Ob −1 (min 1). +1 Thread Sensitivity. |
| Success | Contact established. Proceed. |
| Partial | Unstable. Op Ob +1. −2 Composure. |
| Failure | Thread contact fails. −1D to Thread Pool Score for remainder of scene. (PP-232) |

Eligibility: Approach Training tag; Thread Sensitivity 30+; not in melee with declared attacker. (PP-232 — incapacitation threshold condition removed; not a defined mechanic in this context.)
Full-round action (Priority 5). Only reactive defence available during Leap round.

## Contact Duration
Contact rounds = Focus score. Round 1 = Leap (no op). Ops begin Round 2.
| Focus | Op Rounds | Ops Available |
|-------|-----------|---------------|
| 1 | 0 | Experience only |
| 2 | 1 | One op |
| 3 | 2 | Two ops |
| 4+ | 3+ | Three or more |

Sequential failure: a failed operation ejects the practitioner from the contact window and applies −1D to Thread Pool Score for the remainder of the scene. (PP-232)

## Diagnosis — STRUCK (ED-134 resolved 2026-04-03)
Diagnosis as a mandatory pre-operation procedural gate is removed. Practitioner either suspends sense of self or does not — no separate timed action required. Operations proceed directly.
Priority 4 action. No roll. Mandatory before: Mending, Locking, Dissolution, Past-Oriented Pulling.
Skip before FR: +2 Ob + auto Gap on Failure. Skip before Mending: +2 Ob. Skip before POP: +3 Ob + temporal Gap on Failure.

## Operations — Pools and TNs
All operations: Pool uses Spirit + relevant History bonus + Thread Pool Score unless stated. TN 7 standard.
TN 8: Locking, Dissolution, and Past-Oriented Pulling. [EDITORIAL: ED-135 — "Forced Resolution (FR)" as a collective term is disputed. Pending replacement terminology.]

### Weaving (Things Cohere)
| Scale | Ob | Min Thread Sensitivity |
|-------|----|--------|
| Object | 1 | 30+ |
| Personal | 2 | 30+ |
| Relational | 3 | 50+ |
| Territorial | 4 | 50+ |
| Structural | 8 | 70+ | (PP-232 — corrected from 5)

| Degree | Rendering Stability | Coherence | Other |
|--------|-----|-----------|-------|
| Overwhelming | +1 (Relational+ only) | 0 | +1 Thread Sensitivity |
| Success | 0 | 0 | — |
| Partial | 0 | −1 | Rendering Stability 0; Stability −1 |
| Failure | −2 (Shifting Object at Rendering Stability≤40; Gap at Rendering Stability≤20) | −1 | Stability −2 |

Over-actualisation (Relational+ success): subsequent ops on same config +1 Ob (clears 1 season or after Pull).
Overweaving: each op after first in contact window +1 Ob. Collapsed overweave: Rendering Stability −3.

### Pulling (Things Open)
Pool: Spirit + History + Thread Pool Score | TN 7
| Actualisation | Ob | Min Thread Sensitivity |
|---------------|----|--------|
| Loosely actualised | 1 | 30+ |
| Normal | 2 | 30+ |
| Firmly actualised | 3 | 50+ |
| Previously Woven | 4 | 50+ |
| Foundational | 5 | 70+ |

Duration by surplus: 0 = end of scene. 1 = end of session. 2+ = next seasonal accounting.

| Degree | Rendering Stability | Coherence |
|--------|----|-----------|
| Overwhelming | 0 | 0 |
| Success | 0 | 0 |
| Partial | −1 | −1 |
| Failure | −2 | −1 (snap-back: 1 Wound, no armour) |

### Past-Oriented Pulling
Pool: Spirit + History + Thread Pool Score÷2 (round down) | TN 8 (PP-232 — corrected from TN 7)
Requirements: Thread Sensitivity 70+; Rendering Stability ≤ 60.
| Recency | Ob |
|---------|----|
| Same scene/session | 3 |
| 1–2 seasons | 4 |
| 3–5 seasons | 5 |
| 6–10 seasons | 6 |
| 10+/generational | 7 |
| Foundational | Ob 7 + 2 surcharge = 9; Rendering Stability consequence ×3 |

Active Knot Crisis on target: +1 Ob.
Rendering Stability minimum cost: −3 on Success. Failure: snap-back Wound + Rendering Stability −6 minimum.

### Locking (Forced Resolution)
Pool: Spirit + History (no Thread Pool Score) | TN 7 (TN 8 for FR)
Requirements: Thread Sensitivity 50+. Min Ob: 4.
| Scale | Ob |
|-------|----|
| Object | 4 |
| Personal | 5 |
| Relational/Process | 6 |
| Territorial | 7 |
| Structural/Foundational | 8+ |

Thread Sensitivity 70+: −1 to all FR Rendering Stability costs (min 1).

| Degree | Rendering Stability | Coherence |
|--------|----|-----------|
| Overwhelming | −1 | 0; +1 Thread Sensitivity |
| Success | −1 | 0 |
| Partial | −2 | −1 (cap) |
| Failure | −3 | −1 (cap); 2 Wounds; adjacent ops +1 Ob rest of season |

Chronic drift: 2–3 seasons: Rendering Stability −1/season + ops +1 Ob. 4+ seasons: Rendering Stability −2/season. Permanent: Rendering Stability drift ceases; permanent +1 Ob adjacent.
Reversal Ob: original practitioner's Thread Sensitivity ÷ 10 (round up) − 2, min 1.

### Dissolution (Forced Resolution)
Pool: Spirit + History (no Thread Pool Score) | TN 7 (TN 8 for FR)
Requirements: Thread Sensitivity 50+. Min Ob: 4. Same Ob table as Lock.

| Degree | Rendering Stability | Coherence |
|--------|----|-----------|
| Overwhelming | −3 | 0; micro-Gap forms/closes in scene |
| Success | −5 | 0; Gap forms, closes end of scene |
| Partial | −6 | −1 (cap); Shifting Object; Gap doesn't close without Mending |
| Failure | −8 | −1 (cap); full Gap; Monstrous Incursion; Practitioner incapacitated |

### Mending (Substrate Repair)
Pool: Attunement + Focus + Thread Pool Score | TN 7
Requirements: Thread Sensitivity 50+. Target must be a Gap, Shifting Object, or Locked Zone border.
Ob ceiling: 8 (regardless of stacked modifiers).
| Gap Type | Ob | Min Thread Sensitivity |
|----------|----|--------|
| Shifting Object | 2 | 50+ |
| Micro-Gap (same scene) | 3 | 50+ |
| Standard Gap (1 session–1 season) | 5 | 50+ |
| Entrenched Gap (1+ seasons) | 6 | 70+ |
| Catastrophic Gap (3+ seasons) | 7 | 70+ |
| Locked Zone border | 8+ | 70+ |

| Degree | Rendering Stability | Coherence |
|--------|----|-----------|
| Overwhelming | +2 | −1 (base) |
| Success | +1 | −1 (base) |
| Partial | 0 | −1 (cap); Gap reduced one severity |
| Failure | −2 | −1 (cap) |

Threadcut being interference: +Ob = being's Thread Sensitivity ÷ 20 (round up), max +4.

## Coherence (10→0)
Starting: 10 (all practitioners). Non-practitioners: not tracked.
Loss per operation cap: −1 max per single operation regardless of combined sources.

| Source | Loss |
|--------|------|
| Object/Personal scale op | 0 |
| Relational scale op | −1 |
| Territorial scale op | −1 |
| Structural scale op | −2 |
| FR Lock or Dissolution (any scale) | −1 additional |
| Past-Oriented Pulling | −1 additional. **Cap applies** (unlike Binding Ops per PP-196). Total POP cost = −1 max regardless of scale. (PP-631) |
| Mending | −1 |
| Dissolution residue use | −1 additional (not subject to cap) |
| History Resonance risk die shows 1 | −1 |
| Degree table Failure (Relational+ scale) | apply as written |

| Coherence | State | Key Effects |
|-----------|-------|-------------|
| 10–8 | Stable | No penalty |
| 7–5 | Dissonant | Narrative flickers |
| 4–3 | Fragmented | −1D social/Recall; +1 Ob all ops |
| 2 | Fractured | −2D social/Recall; +1 Ob all Thread ops (PP-221); Belief Co-Authorship begins |
| 1 | Severed | −2D; dissociative episodes; +2 Ob all ops |
| 0 | Rendering Crisis | Campaign event. Non-Player Character if unresolved by season end. |

Recovery: Full season non-practice: +1. Anchoring Scene (Bonds TN7 Ob2): +1. Cannot exceed 10.

## Dissolution Residue
Bonus dice: Potency rating (1–5). Explode on 9–10.
Cost: −1 Coherence per use (additional; not subject to §3.2 op cap at Relational+).
Same source: +1 Ob per prior use.

## Rendering Stability (RS) Track
Range: 100→0. Starting: Rendering Stability 60 (TTRPG default campaign). Board Game default: 72 — see params_board_game.
| Rendering Stability | State | World Effects |
|----|-------|---------------|
| 100–80 | Stable | None |
| 79–60 | Strained | Occasional wrongness near Thread sites |
| 59–40 | Fragile | Shifting Objects spontaneous (1/season); Thread ops +1 Ob in affected territories |
| 39–20 | Fractured | Spontaneous Gaps (1d10/season; 1–2 = Gap); Monstrous Incursion risk; rendering failures |
| 19–1 | Critical | As Fractured + doubled Gap risk; +1 Ob worldwide; faction Stability checks Ob1; Mandate 0 → Faction Fracture |
| 0 | The Rupture | Campaign ends |

Rendering Stability threshold effects: activate/deactivate at Accounting, not mid-scene.
Rendering Stability threshold effects are cumulative (each lower band includes all higher band effects).
Seasonal cap: ±10 net Rendering Stability change per season (applies at Accounting).

Key Rendering Stability degradation values:
- FR Dissolution Failure: −8. Dissolution Success: −5. POP Success: −3 minimum.
- Gap persisting per season: −4. Lock chronic drift: −1 to −2/season.
- Winter annual drift: −1. Siege per season: −1.
- Mending Success: +1. Mending Overwhelming: +2.
- Weaving Overwhelming (Relational+): +1.

## Collective Operations
Anchor: highest Thread Sensitivity practitioner. Rolls full pool.
Helper contribution: ⌊Cognition ÷ 2⌋ bonus dice each.
If pool drops below half Anchor's solo pool: +1 Ob.
Directly opposing Beliefs: pre-Leap Belief check (Spirit TN7 Ob1) or helper drops out.
Tangential conflicting Beliefs: helper dice don't chain on 10.

<!-- PP-632 applied 2026-04-13: Opposing Operations — Contested Intentionality -->

## Opposing Operations — Contested Intentionality (PP-632)
**Scope:** Two practitioners in contact targeting the same configuration with opposing intentionalities.
**Opposing pairs:** Weave/Pull, Lock/Dissolution, Lock/Pull, Weave/Dissolution.
**Not opposing:** Weave/Lock, Pull/Dissolution (compound). Any op/Mending (different target category). Different-scale ops (different configurations).

### Opposing Engagement Modifier
+floor(opponent TPS ÷ 2), minimum +1. Stacks with all other Ob modifiers.
| Opponent TPS | +Ob |
|---|---|
| 3 | +1 |
| 4–5 | +2 |
| 6–7 | +3 |
| 8–9 | +4 |
| 10 | +5 |

### Resolution
| A | B | Outcome | RS | A Cost | B Cost |
|---|---|---|---|---|---|
| ≥Ob | ≥Ob | Shifting Object | worst RS +1 | Coh §3.2; +1 Ob, 2 Comp | same |
| ≥Ob | Partial | A resolves (O→S; S stays) | A RS +1 | Coh §3.2; 1 Comp | Coh §3.2; +1 Ob, 2 Comp; no degree-table |
| ≥Ob | Fail | A resolves at degree | A RS only | normal | standard Failure |
| Partial | Partial | d6: 1–2 SO (−1 scale); 3–6 none | −1 | Coh §3.2; +1 Ob, 2 Comp | same |
| Partial | Fail | A Partial resolves | A Partial RS | normal | standard Failure |
| Fail | Fail | nothing | −1 | Coh §3.2; 1 Comp | same |

### FR vs FR Both-Fail
Object RS −1 (d6:1 SO); Personal −2 (1–2); Relational −3 (1–3); Territorial −4 (1–4); Structural −5 (1–5). Both +2 Ob, 4 Comp.

### Knot Strain
Standard loser: +1 Ob next op, 2 Composure. Winner: 1 Composure.
FR loser: +2 Ob, 4 Composure. If winner Dissolved: +1 Wound (knot tear). Winner: 2 Composure.
Tie (both ≥Ob): both +1 Ob, 2 Comp. FR tie: +2 Ob, 4 Comp.
Both fail: 1 Composure each.
Composure restores at scene change. Ob penalty: next Thread op or scene end.

### Co-Movement
Coherence: per-practitioner §3.2. Epistemic + actual: ONCE for compound event.

### Sustained Opposition
+1 Ob sequential failure if target changed. SO on existing SO: advance 1 deterioration tier (seasons→sessions→scene).

### N-Way (3+)
Automatic lattice collapse. All fail. Gap at target scale. RS −(2 × n). All: +2 Ob, 4 Comp.

### Mending Immunity
Cannot be directly opposed. Indirect: +1 Ob co-movement at site; P-17; territory effects. Ceiling 8.

### Mass Battle
Highest net wins. Winner at degree, loser Partial. Tie: SO + both Partial. RS ×3 (PP-192). Temporal NOT ×3 (PP-226).

### Board Game
Both succeed: SO + Co-Movement Card. One succeeds: resolves + Co-Movement Card. Both fail: nothing. No personal-scale consequences.

### Hybrid Cross-Phase
Personal Phase roll stands. BG rolls at Cascade. Modifier: TTRPG uses BG NPC's TPS (or faction Int ÷ 2, min 1). BG uses TTRPG TPS.


## Cross-Mode Thread
| Rule | TTRPG | Board Game | Hybrid |
|------|-------|-----------|--------|
| Operations | Weaving/Pulling/Mending/Lock/Dissolution | Weave/Mend/Investigate/Harvest orders | Personal: TTRPG; Strategic: BG |
| Co-movement | Version C (temporal + epistemic + d6) | Co-Movement Cards (18) | Personal: Version C; Strategic: Cards |
| Coherence | Tracked per Player Character | Not tracked | Tracked during Personal Phase only |
| Rendering Stability | 100→0 at Accounting | 100→0 at Accounting | Cascade Phase Accounting; cap ±10 |
| Lock drift | Game Master tracks | Territory card: Rendering Stability −1/season | TTRPG Lock → territory card at Cascade |

## Observation / Detection
| Observer Thread Sensitivity | Perception |
|-------------|-----------|
| 0–9 | Nothing |
| 10–29 | Vague unease |
| 30–49 | Senses operation, general direction |
| 50–69 | Identifies type and target |
| 70+ | Full configuration |

Concealment from Thread Sensitivity 30+ observers: Cognition only (no History), TN7, Ob = observer Thread Sensitivity ÷ 30 (round up). Pre-Leap action.


## P1 Audit Resolutions — AUD-TW-001 (PP-190–PP-195)

### PP-190: Leap Combat Action Economy (ED-124/ED-134 resolved 2026-04-03)
Diagnosis struck as mandatory action. In mass battle: Leap proceeds directly in Phase 4. In personal combat: Leap = Priority 5 full-round action (no Diagnosis prerequisite). PP-190 2-round rule removed — personal combat only constraint lifted.

### PP-193: P-22 Paradox Window Resolution [PROVISIONAL]
Auto-resolves at window end (1d3 scenes). Early closure: Mending (Ob 3 = Micro-Gap). Exploitation: +2 Ob to operations targeting paradoxed thread; Failure collapses window.

### PP-194: Rendering Crisis Resolution [PROVISIONAL]
Requires: (1) full season no Thread practice; (2) 3 Anchoring Scenes (Bonds TN7 Ob2 each); (3) physical stability.
Resolution roll: Close Knot Bonds + successful Anchoring Scenes, TN7 Ob3.
| Degree | Coherence restored |
|--------|-------------------|
| Overwhelming | 4 (−1 TS permanent) |
| Success | 3 (−1 TS permanent) |
| Partial | 1 (another arc needed) |
| Failure | 0 → Non-Player Character at season end |

### PP-192: Mass Battle RS Multiplier [PROVISIONAL]
All RS costs from Thread ops in mass battle ×3. Coherence costs unaffected.
See params_mass_combat §Mass Battle RS Multiplier.

### PP-191: Lock Phase in Mass Combat [PROVISIONAL]
Offensive Lock = Phase 4 (declared at Phase 1). Support Lock = Phase 6 Step 5 (declared at Phase 1). Default if undeclared: Phase 6.

### PP-195: Community Weaving Procedure [PROVISIONAL]
Revolution Domain Action. Pool: Mandate (as dice) + History, TN7, Ob3.
Success=RS+1, Overwhelming=RS+2, Partial=RS+0, Failure=RS+0 and Mandate−1. Once/season. Mandate≥1 required.


## Canon-Derived Resolutions — ED-099–106 (PP-196–200)

### ED-099 — RESOLVED (intended): Temporal weight inert for non-POP ops
Canon §1.3 + §19.1: Ob captures actualization. Temporal weight manifests through co-movement auto-effects, not Ob difficulty. Old vs. new configurations are equally hard to Weave — but produce different co-movement consequences. No change to Ob tables. Temporal weight is a co-movement input, not an Ob modifier.

### ED-100 — RESOLVED (no change): Lock axis attribution
Canon §1.1 Inseparability: actuality is Lock's PRIMARY target (drives to full actualization). Intelligibility (frozen face) and temporality (unable to become) are constitutive co-movement consequences, per P-01. Three-way description is correct — it is the inseparability principle working. Clarification note only: Lock primarily targets actuality axis; other effects are inseparability consequences.

### ED-101 — RESOLVED (independence canon-mandated, with exception): Coherence/RS independence
Canon Amendment 01 §3: Coherence and RS are orthogonal. Independence is correct for TS 0–89. Exception: TS 90+ at Coherence 0 causes reality strain RS cost (PP-197). For TS 70–89 at Coherence 0: −1 RS/session. For TS 90+ at Coherence 0: −1 RS/scene.

### ED-102 — RESOLVED (intended, canon-consistent): POP RS ≤ 60 gate
Canon §6.1: Strained substrate = thinner membrane between intelligible and unintelligible. POP requires stressed substrate because temporal depth is closer to the surface when the fabric is taut. The perverse incentive is intentional design — using world degradation as a tool is a real choice with real consequences (per §23.3). No change.

### ED-103 — RESOLVED (patch PP-196): FR surcharge cap exemption
Canon §1.1 + P-01: FR operations are deeper ontological violations. FR surcharge now exempt from §3.2 cap (consistent with Dissolution residue exemption). See PP-196 for revised cost table.
| Scale | FR Lock/Dissolution | Non-FR at same scale |
|-------|---------------------|----------------------|
| Object/Personal | −1 (FR surcharge only) | 0 |
| Relational | −2 (−1 scale + −1 FR) | −1 |
| Territorial | −2 (−1 scale + −1 FR) | −1 |
| Structural | −3 (−2 scale + −1 FR) | −2 |

### ED-104 — RESOLVED (ruling PP-199): POP displacement of debate subject
If POP displaces debated event: disputed party loses Memory bonus for displaced claims. Debate continues (no restart). Opposing party may invoke displacement as Present-genre argument. Temporal Disjunction: −1D Argue for characters arguing from displaced past (one exchange). See PP-199 in threadwork doc.

### ED-105 — RESOLVED (patch PP-198): Hybrid Coherence declaration rule
Canon Amendment 01 §2–3: Coherence = layer 2 suspension cost. Only the Leap-performer pays. Replaced "narratively leads" with binary: PC who declares leadership at Phase 1 of Cascade Phase pays Coherence cost. No declaration = no cost. See PP-198.

### ED-106 — RESOLVED (ruling PP-200): Coherence initialization BG→Hybrid
Canon Amendment 01 §3: Layer 2 intact before any Leap. First Personal Phase in Hybrid: Coherence = 10. Subsequent: carry forward last recorded value. GMs track per PC on Hybrid tracking sheet. See PP-200.


## Sim-Debt Resolutions — SIM-X-17 through SIM-X-20 (PP-201–207)

### PP-201 (P1): Mass battle Dissolution warning
E[RS per Dissolution attempt at TS70] = −18.4. Three attempts = E[RS] 6 (Critical) from RS 60. Single Failure at RS<24 = Rupture. Dissolution is campaign-altering. See params_mass_combat.

### PP-202 (P2): Rendering Crisis arc stability disruption
Arc pauses (not resets) if physical stability fails mid-arc. Disrupted seasons extend non-practice requirement. Thread ops during disrupted season resets non-practice counter entirely.

### PP-203 (P3): Sequential POPs on paradoxed thread
Second POP targeting a thread in paradox window auto-fails (no roll, no RS cost). Coherence and Focus consumed. Window unaffected.

### PP-204 (P3): RS<24 mass battle Rupture threshold
GM mandatory disclosure before any mass battle Dissolution declaration when RS<24. Dissolution Failure = −24 RS = Rupture if RS<24.

### PP-205 (P2 / ED-107): Hybrid co-declaration tie-break
Highest Thread Sensitivity declares. Tie = first declared at table. Non-declaring PC pays no Coherence.

### PP-206 (P3): TS 30-31 Rendering Crisis GM guidance
GM must disclose before arc: Success/Overwhelming at TS 30-31 reduces TS to 29 or below Leap minimum (30). Practitioner may lose Thread ops permanently.

### PP-207 (P3): Hybrid Coherence pacing guidance
Sustainable: 1 Personal Relational op + 1 Strategic declaration/session → Rendering Crisis ~session 10. Two of each → Crisis by session 3-5 (not intended).


## SIM-X-21 Gap Resolutions (PP-208–209)

### PP-208: OA modifier does not carry through to Shifting Object
When a Woven thread shatters into Shifting Object via brittleness, OA +1 Ob modifier does not apply to the new configuration. Mending proceeds at base Ob. Exception: OA applies if Mending targets still-Woven thread before it shatters.

### PP-209: Double OA stacking — two independent Weavings same scene
Two separate successful Weavings of same thread in separate contact windows = two OA stacks (+2 Ob total). Both clear after 1 season or Pull. Doubly OA = more severe brittleness shattering (Shifting Object forms 1 tier more advanced). Overweaving rule (intra-window +1 Ob cumulative) does not apply across separate windows.



## SIM-X-22 Provisional Patches (PP-221, PP-223, PP-225, PP-226)

### PP-221: Coherence 2 (Fractured) Thread Ob Penalty [PROVISIONAL]
Coherence 2 (Fractured) = +1 Ob all Thread operations. Consistent with the 4–3 band penalty progression (4–3 = +1 Ob ops; 2 = +1 Ob ops + social/Memory penalties; 1 = +2 Ob ops).

### PP-223: Mass Battle Turn = 1 Scene [PROVISIONAL]
One mass battle turn = 1 scene for all RS threshold effects, Coherence-0 leakage, and paradox window ticking. This means: RS threshold effects activate/deactivate once per battle turn (at Phase 6 Cascade); Coherence-0 leakage fires once per battle turn; paradox window duration counts 1 tick per battle turn. ED-123 pending confirmation.

### PP-225: RS ×3 Multiplier Applies to Gains [PROVISIONAL]
The mass battle RS ×3 multiplier (PP-192) applies to RS gains as well as costs. Weaving Overwhelming at Relational+ scale in mass battle = RS +3 (not +1). Mending Success = RS +3 (not +1). Mending Overwhelming = RS +6 (not +2). This makes Mending viable as a strategic mass-battle action.

### PP-226: Temporal Auto-Effect RS NOT Subject to ×3 [PROVISIONAL]
Temporal auto-effect RS costs from Past-Oriented Pulling (PP-181) are NOT subject to the mass battle ×3 multiplier. The temporal auto-effect is a separate system triggered by recency band, not an operation RS cost. It fires independently of mass battle context. The ×3 multiplier applies only to operation-table RS costs (degree outcomes).

<!-- patch_history: references/params_threadwork_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->
## Actual Auto-Effect Table — Personal-Scale Operations (PP-181)

When a Thread operation fires at personal scale (not mass combat), the Actual d6 consequence follows this table. Roll d6 (or use expected value = 3-4 for simulation):

| d6 | Actual consequence |
|----|-------------------|
| 1 | Nothing observable. The operation is unwitnessed. |
| 2 | A minor physical object nearby shifts — falls, opens, tips. Narrative only. |
| 3 | A nearby person (TS 0) feels brief disorientation or dread. Recovers in moments. |
| 4 | A sensory anomaly in the area — cold breath, scent out of place, sound. Narrative only. |
| 5 | A document, object, or memory relevant to the operation's target becomes momentarily prominent. +1D on the next investigation roll in this scene. |
| 6 | A minor structural consequence — a door opens, a fire gutters, a clock stops. GM discretion; narrative significant but not mechanically dangerous. |

**For simulation:** Use expected value d6=3-4 (minor observational consequence). [PP-181]

## Temporal Auto-Effect RS Cost — Past-Oriented Pulling (PP-181)

POP operations produce an additional RS cost from temporal auto-effect, independent of the operation's own RS cost:

| Recency band | Temporal auto-effect RS |
|-------------|------------------------|
| Same scene/session | 0 (no temporal stress) |
| 1–2 seasons | 0 |
| 3–5 seasons | −1 |
| 6–10 seasons | −1 |
| 10+/generational | −1 |
| Foundational | −2 |

Applied after operation RS cost. The temporal auto-effect fires regardless of success/failure. [PP-181]

## Territorial+ Locking — Design Note (PP-181)

Territorial Locking (Ob 7, TN8, no Thread Pool Score) and above is near-impossible by design. P(success) < 2% even for TS 80+ practitioners. This is philosophically consistent with P-06 (threadcut = "radically IS without becoming") — practitioners cannot lock strategic-scale configurations. To achieve strategic-scale future constraint, use sustained Relational-scale Weaving over multiple seasons instead. [PP-181]

## Partial Lock Duration (PP-181)

A Partial Lock result produces a volatile lock. Effect: +1 Ob on Domain Actions/operations attempting to override the locked configuration. Duration: 1 season only (degrades naturally). Chronic drift (RS −1/season from season 2) applies only to successful Locks, not Partial Locks. [PP-181]

## Epistemic Auto-Effect — TC Trigger (PP-182)

A TS 30+ Church observer witnessing a Thread operation does NOT automatically trigger TC increase. Observation alone is insufficient. TC increase from epistemic auto-effect requires:
1. A Church actor with TS 30+ witnesses the operation AND
2. The Church initiates a formal Investigation (one Church Domain Action, Ob 2).
If the investigation proceeds: TC +1 at next Accounting.
If the Church does not investigate (or cannot): no TC effect from observation.

This prevents automatic TC escalation from all Thread ops in Church-adjacent locations. [PP-182]

## Thread Combat vs Mode 3 Entities (ED-030 resolved 2026-04-03)
Pool split (Offence/Defence) applies to Thread pool same as combat pool.
Thread Offence vs entity Coherence Rating (Ob = entity CR).
Thread Defence vs entity counter-unravelling attempts.

## Ceiral Ritual — BG RS Propagation (ED-034 resolved 2026-04-03)
Ceiral Ritual RS changes propagate at full TTRPG value to BG RS track (immediate, per state_transfer_spec PP-107).
BG Co-Movement card ceiling (RS +1) applies ONLY to BG-initiated Thread abstraction — not to TTRPG Zoom In scenes.
Ritual outcomes: Success RS −6, Overwhelming RS −10, Partial RS −3, Failure RS +8. Apply directly.

## Mass Combat Paradox Window — Scene Definition (ED-121 resolved 2026-04-03)
Scene for mass combat paradox window = number of battle turns before the paradox window closes for the season.
Not a single battle turn. GM tracks window closure per season.

## Co-Movement Axes — Operation (ED-086 resolved 2026-04-03)
Three axes confirmed: Temporal, Epistemic, Actuality. D10 roll.
All three axes fire simultaneously — not sequential staging.

---
<!-- PP-239 applied 2026-04-04: RS no natural decay clarification -->
<!-- PP-240 applied 2026-04-04: Forgetting Check stacking rule (PROVISIONAL) -->

## RS Change Rule (PP-239)
**RS does not decay naturally. All RS changes are event-driven:**
- Thread operation degree outcomes (see operation tables)
- Lock chronic drift: −1 RS/season per territory with active Lock (seasons 1–3); −2 RS/season (seasons 4+)
- Gap persistence: −4 RS/season per active Gap at Accounting
- Mending success: +1 to +2 RS per operation
- No baseline seasonal RS reduction exists.

## Forgetting Check Stacking Rule (PP-240) [PROVISIONAL — ED-153 adjacent]
Multiple Forgetting Checks in the same session:
- Within a single scene: only the deepest applicable Ob applies (checks do not stack within one scene).
- Across multiple scenes in the same session: each check is independent. A Failure on an earlier check does not increase Ob for subsequent checks — the Forgetting strips content, not the mechanism itself.
- Collective Forgetting (multiple practitioners present): [GAP-H-01 — undefined. Do not apply any rule until defined.]
---
<!-- PP-253 2026-04-04: ED-153 resolved — Collective Forgetting rule -->

## Collective Forgetting (PP-253) [FLAGGED FOR REVIEW: ED-153-R]
When multiple practitioners are present during Southernmost exposure:
- Each makes their own Forgetting Check independently.
- A practitioner who passes (Success or Overwhelming) may act as a Recall Anchor for one other practitioner who failed or partially failed.
- Recall Anchor effect: the failing practitioner retains facts only (as if they had achieved Success), regardless of their actual roll result. Emotional conviction is still lost.
- One Anchor per failed practitioner. An Anchor cannot anchor more than one other.
- Non-practitioners cannot anchor anyone.
[FLAGGED FOR REVIEW: ED-153-R — confirm Anchor mechanic; confirm non-practitioner exclusion.]

## ED-024 Resolution (PP-263) [FLAGGED FOR DESIGNER REVIEW]
Southernmost Mode 3 entity provisional stat block (minimal):
| Stat | Value | Notes |
|------|-------|-------|
| Thread Pool Score | 8 | Acts as a practitioner at TS 80+ |
| Coherence | N/A | Cannot degrade — no rendering substrate |
| Wound threshold | 12 | Physical damage valid only while in material-adjacent state |
| Initiative | Always last | Entities do not declare; they respond |
| Thread Operation | Weaving (automatic, no Leap) | Once per round, object scale |
Full stat blocks require designer decision. This is a floor for simulation purposes only.
[FLAGGED: full Mode 3 entity design deferred.]

## ED-029 Resolution (PP-264) [FLAGGED]
Purpose tracking in Southernmost: **Clarity countdown** mechanic adopted (provisional).
- Start: Clarity = d3+1 (rolled at entry to each Southernmost zone).
- Each hour of exposure: Clarity −1.
- Clarity 0: character must succeed at a Spirit check TN 7 Ob 2 or leave the zone immediately (Purpose dissolves).
- Thread Sensitivity ≥ 40: +1 Clarity at zone entry.
[FLAGGED: confirm d3+1 range and Spirit check parameters.]

## ED-030 Resolution (PP-265)
Thread combat vs Mode 3 entities: **Thread pool split (Off/Def) applies** identically to personal combat pool split.
- Offence dice roll vs entity Thread resistance (TPS 8 = Ob 8 to overcome).
- Defence dice absorb entity's Weaving attempts (entity Weaving = Ob equal to PC Defence allocation net).
- No separate Thread combat system needed.
[FLAGGED: confirm Ob derivation for entity Thread resistance.]

## ED-119 Resolution (PP-279) [SUPERSEDED 2026-04-11]
<!-- PP-279 DISSOLVED. Lenneth TS 72 replaced by TS 8 (starting) with archive-based development path.
See designs/npcs/lenneth_threadwork_design.md for full design.
Lenneth is patron, not practitioner. Catherine the Great parallel.
Mira relationship: patron-to-practitioner (archive access), not teacher-to-student.
ED-119 resolved by 2026-04-11 session. ED-161 also resolved. ED-413 documents the dissolution. -->
Lenneth Almqvist: Thread Sensitivity **8** (starting). Development path: archive research (Spirit + Einhir Scholar, TN 7, Ob 2). Maximum potential TS 40-50.

## ED-134 Resolution (PP-289)
Diagnosis as mandatory pre-operation: confirmed as **perception act**, not a separate operation.
Diagnosis reveals: Thread configuration type, approximate scale, RS signature. Takes no action economy slot in TTRPG (perception is continuous for Leap-eligible practitioners). In mass battle: collapsed into Leap per PP-224.
ED-134 resolved — Diagnosis is not a separate action; it is the practitioner's default mode of Thread perception during contact.

## ED-135 Resolution (PP-290)
"Forced Resolution (FR)" as collective label for Locking and Dissolution: **renamed to Restricted Operations (RO)**.
Rationale: "Forced Resolution" implies inevitability; these operations are costly choices. "Restricted" captures: available only to practitioners; restricted by Coherence cost; restricted by Ob; restricted by RS.
All params_threadwork references to FR updated to RO.
[FLAGGED: confirm rename before compilation.]

---
<!-- PP-303 2026-04-04: Shifting Object encounter rule (PROVISIONAL ED-173) -->

## Shifting Object Encounter Rule (PP-303) [PROVISIONAL — ED-173]
When a Shifting Object is present in a territory (formed from Fragile band RS consequence or operation failure):
- Practitioners within 50m: Coherence check TN 7 Ob 1 per scene. Failure: Coherence −1.
- Non-practitioners: Certainty −1 (PP-551) after 1+ hour of proximity. (Witnessing Thread phenomena moves the character toward Thread acceptance.)
- Mending the Shifting Object: treated as Micro-Gap, Ob 2.
- Dissolution: Ob 3 (standard small-scale Dissolution).
Shifting Objects persist until addressed. Each season unaddressed: +1 Ob to Thread operations in that territory.
[FLAGGED: confirm Coherence check parameters and seasonal Ob accumulation.]

## Document RS Resonance (PP-258)
A Thread Sensitivity 50+ practitioner reading a pre-Solmund first-person Thread-perception document gains:
- RS +2 (one-time per document per character)
- Requires: TS ≥ 50, full scene of contact, primary first-person account (not secondary analysis)
- Does not stack with active Thread operations in the same scene (larger RS change applies)
- Subsequent readings of the same document: no RS effect

## Collective Forgetting — Companion Carrying (PP-279)
A practitioner who succeeds on their Forgetting boundary Leap may carry companions:
- Each companion: −2 Coherence/round (cumulative)
- Maximum companions = practitioner's Focus − 1
- Focus 1: 0 companions. Focus 3: max 2. Focus 5: max 4.
- Companion must remain within Thread contact throughout crossing.

---
<!-- PP-281 2026-04-04: Untrained Leap auto-fail -->

## Untrained Leap Auto-Fail (PP-281) [PROVISIONAL — ED-178]
A practitioner who attempts Leap without the Approach Training tag:
- The Leap roll **auto-fails** (no dice rolled).
- Consequence (as for Leap Failure): Thread contact fails; −1D to Thread Pool Score for remainder of scene.
- Additional consequence (untrained only): **Certainty −1** (uncontrolled contact with Thread substrate without preparation disturbs epistemic grounding).
- No RS cost from auto-fail (operation never reached the operation phase).
- Coherence is NOT reduced by auto-fail (only by successful contact that then degrades).

[Certainty −1 confirmed per PP-551 redesign. Non-practitioner Thread exposure moves toward Thread acceptance. Coherence −1 is reserved for practitioners performing operations.]

## ED-119 Resolution (PP-304) — Lenneth Almqvist TS [SUPERSEDED 2026-04-11]
<!-- PP-304 DISSOLVED. See PP-279 supersession note above. Lenneth TS 8 starting, development via archive. -->
Lenneth Almqvist: Thread Sensitivity **8** (starting). See designs/npcs/lenneth_threadwork_design.md.


## ED-134 Resolution (PP-314) — Diagnosis Rationale
Diagnosis: confirmed as perception act, not a separate operation.
Diagnosis reveals Thread configuration type, scale, RS signature during active Leap contact.
Takes no action economy slot in TTRPG (perception is continuous for Leap-eligible practitioners).
In mass battle: collapsed into Leap per PP-224. ED-134 resolved.


## ED-135 Resolution (PP-315) — FR Terminology [FLAGGED]
"Forced Resolution (FR)" renamed to **Restricted Operations (RO)**.
"Restricted" captures: available only to practitioners; restricted by Coherence, Ob, and RS.
All params_threadwork FR references updated to RO.
[FLAGGED: confirm rename before compilation.]


## ED-153 Resolution (PP-330) — Collective Forgetting Anchor [FLAGGED]
Recall Anchor mechanic: practitioner who passes Forgetting Check may anchor one other who failed/partially failed.
Anchor elevates failing practitioner to fact-retention (as if Success) — emotional conviction still lost.
One anchor per failed practitioner; Anchor cannot anchor more than one other. Non-practitioners excluded.
[FLAGGED: confirm Anchor mechanic before Southernmost compilation.]

## Binding Operations (PP-252) — formerly Forced Resolution (FR)
'Forced Resolution (FR)' deprecated. All references replaced with 'Binding Operations (BO)'.
- Lock = Binding to State
- Dissolution = Binding to Absence
Binding Op surcharge exempt from §3.2 Coherence cap (PP-196): Object/Personal=−1, Relational/Territorial=−2, Structural=−3.

## Community Weaving — Canonical Formula (PP-250)
Supersedes all prior Community Weaving entries (PP-168, PP-195 partial entries deprecated).
Pool: Attunement + History bonus + Thread Pool Score
TN: 7 | Ob: 3
RS outcome: Success = RS +1; Overwhelming = RS +2
This is a Thread operation, not a Domain Action. No faction stat involvement.
Competes for Thread contact window with other ops — cannot be performed as narrative downtime.
One Community Weave per contact window round; replaces another op that round.
Primary player-accessible RS restoration mechanism.

## Hybrid Strategic Phase — Temporal Auto-Effects (PP-260)
Thread operations at Strategic Phase (Hybrid BG layer):
- Dissolution: TC +1 (destabilising)
- Past-Oriented Pulling: TC −1
- Lock / Weave / Mend: no TC change
Paradox window: POP at Strategic scale opens paradox for current season.
All contested Domain Actions during that season: +1 Ob from temporal instability. Closes at next Accounting.

## Binding Operations Scope Gate in Mass Battle (PP-261)
Binding Ops at Relational scale in mass battle require Thread Sensitivity 90+ for >50% success.
TS 70 practitioners: do not attempt Binding Ops in mass battle. RS cost without viable success probability.

## ED-301 Propagation: TS/Coherence Orthogonality — Canonical Framing
- **Thread Sensitivity (TS)**: governs depth and breadth of thread perception — what is accessible and legible as thread. Identical in effect at any Coherence level.
- **Coherence**: governs the ontological rendering frame — how much of that perception remains translatable into human terms. Coherence loss = expansion beyond human rendering frame, not degradation.
- **Coherence 0**: layer 2 (always-already self-rendering) has ceased. Character passes to GM. Released Coherence 0 characters become world-state contributors, GM-rendered from co-authored belief/inspiration material (Coherence 3 co-authoring protocol).
- See canon/01_foundations_amendment_self_rendering.md §Amendment 3–4 for full TS-gated branching.
- **Mode 3 entities (ED-024)**: threadcut beings whose excess existence cannot be fully rendered. Presence produces structural entanglement in environment and nearby beings as side-effect (cf. Solmund/Locked zones). Non-Thread engagement ontologically irrelevant. TS 50+ required. GM references standard Thread operation tables at beyond-human scale. No stat block. Provisional archetypes struck (P-05 violation).


## Inert Knowledge (P-08, PP-497)

Non-sensitive characters (Thread Sensitivity (TS) 0) may learn, memorise, and recite Thread-related information from texts, instruction, or observation. This knowledge is Inert: it cannot be used to perform Thread operations, diagnose Thread states, or perceive Thread-level phenomena. The barrier is metaphysical (TS 0 consciousness cannot render Thread-level structure), not institutional. A non-sensitive with complete written instructions for a Weaving cannot execute it. A sensitive (TS ≥ 10) with the same instructions can, because their consciousness renders the Thread-level structure that the instructions describe.

**Mechanical implication:** No amount of study, training, or exposure grants Thread operational capability to a TS 0 character. TS must be ≥ 10 (Practitioner designation) before any Thread operation can be attempted. The epistemological barrier is not a skill check — it is a hard gate on rendering capacity.

**Church and institutional reinforcement (P-08 note):** The Church reinforces the epistemological barrier institutionally, but the barrier would exist without the Church. Publishing all Thread-related documents publicly would not enable non-sensitives to perform Thread operations. It would enable them to recite the procedures — inertly.


## War-Scale Dissonant Thread Effects (PP-502, ED-362 resolved)

When ≥ 3 Thread operations fire in a single mass battle turn, the substrate becomes saturated:

| Condition | Effect |
|-----------|--------|
| 3+ Thread ops in one battle turn | All subsequent Thread ops that turn: +1 Ob, +1 Coherence cost (cap: +2 each) |
| Dissonant Counter ≥ 3 (cumulative across turns) | All Thread ops in battle zone: +2 Ob for remainder of battle (substrate saturation) |
| Dissonant Counter ≥ 3 at battle end | RS −2 at next Accounting (in addition to individual op RS costs) |

Dissonant Counter: +1 per battle turn with ≥ 3 Thread operations. Resets at battle end. Does not persist between battles.

[EDITORIAL: ED-362 — resolved provisionally. Creates natural ceiling on mass-battle Thread spam. Flagged for simulation under SIM-DISSONANT.]