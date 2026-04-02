<!-- version: v0.14+design-ST | source: threadwork_redesign_v25.md | last_updated: 2026-04-02 -->
<!-- PATCHES APPLIED: P-11–P-30 (prior); ST-TW-01–05 added 2026-04-02; Mode index added to source doc -->
<!-- stage3_thread_operations.md is EMPTY in v0.14. All values from threadwork_redesign_v25.md. -->
<!-- STALE CHECK: All values [PROPOSAL]. Verify against compiled stage3 before use. -->

# params_threadwork.md — Thread Operations (v2.5)

## Practitioner Stats
| Stat | Range | Description |
|------|-------|-------------|
| Thread Sensitivity (TS) | 0–100+ | Perception depth |
| Thread Depth (TD) | 0–10 | Active engagement depth |
| Rendering Stability (RS) | 100→0 | World coherence (shared track) |
| Coherence | 10→0 | Personal rendering stability |
| Focus | 1–5+ | Contact duration in rounds |
| TPS | TS ÷ 10 (round down) | Thread Pool Score — added to operation pools |

## Leap Roll
Pool: Attunement + relevant History bonus + TPS | TN: 7
| TS | Ob | Wound modifier |
|----|----|-|
| 30–49 | 2 | +1 Ob per Wound |
| 50+ | 1 | +1 Ob per Wound |

| Degree | Outcome |
|--------|---------|
| Overwhelming | Clean suspension. Next op Ob −1 (min 1). +1 TS. |
| Success | Contact established. Proceed. |
| Partial | Unstable. Op Ob +1. −2 Composure. |
| Failure | Snaps back. −4 Composure. Rattled. No op this scene. |

Eligibility: Approach Training tag; TS 30+; not in melee with declared attacker; not at incapacitation threshold (⌈Health÷2⌉).
Full-round action (Priority 5). Only reactive defence available during Leap round.

## Contact Duration
Contact rounds = Focus score. Round 1 = Leap (no op). Ops begin Round 2.
| Focus | Op Rounds | Ops Available |
|-------|-----------|---------------|
| 1 | 0 | Experience only |
| 2 | 1 | One op |
| 3 | 2 | Two ops |
| 4+ | 3+ | Three or more |

Sequential failure penalty: +1 Ob per prior failure in same contact window (cumulative).

## Diagnosis
Priority 4 action. No roll. Mandatory before: Mending, Locking, Dissolution, Past-Oriented Pulling.
Skip before FR: +2 Ob + auto Gap on Failure. Skip before Mending: +2 Ob. Skip before POP: +3 Ob + temporal Gap on Failure.

## Operations — Pools and TNs
All operations: Pool uses Spirit + relevant History bonus + TPS unless stated. TN 7 standard.
TN 8: Forced Resolution (Lock/Dissolution) and Past-Oriented Pulling.

### Weaving (Things Cohere)
| Scale | Ob | Min TS |
|-------|----|--------|
| Object | 1 | 30+ |
| Personal | 2 | 30+ |
| Relational | 3 | 50+ |
| Territorial | 4 | 50+ |
| Structural | 5 | 70+ |

| Degree | RS | Coherence | Other |
|--------|-----|-----------|-------|
| Overwhelming | +1 (Relational+ only) | 0 | +1 TS |
| Success | 0 | 0 | — |
| Partial | 0 | −1 | RS 0; Stability −1 |
| Failure | −2 (Shifting Object at RS≤40; Gap at RS≤20) | −1 | Stability −2 |

Over-actualisation (Relational+ success): subsequent ops on same config +1 Ob (clears 1 season or after Pull).
Overweaving: each op after first in contact window +1 Ob. Collapsed overweave: RS −3.

### Pulling (Things Open)
Pool: Spirit + History + TPS | TN 7
| Actualisation | Ob | Min TS |
|---------------|----|--------|
| Loosely actualised | 1 | 30+ |
| Normal | 2 | 30+ |
| Firmly actualised | 3 | 50+ |
| Previously Woven | 4 | 50+ |
| Foundational | 5 | 70+ |

Duration by surplus: 0 = end of scene. 1 = end of session. 2+ = next seasonal accounting.

| Degree | RS | Coherence |
|--------|----|-----------|
| Overwhelming | 0 | 0 |
| Success | 0 | 0 |
| Partial | −1 | −1 |
| Failure | −2 | −1 (snap-back: 1 Wound, no armour) |

### Past-Oriented Pulling
Pool: Spirit + History + TPS÷2 (round down) | TN 7
Requirements: TS 70+; RS ≤ 60; Diagnosis mandatory.
| Recency | Ob |
|---------|----|
| Same scene/session | 3 |
| 1–2 seasons | 4 |
| 3–5 seasons | 5 |
| 6–10 seasons | 6 |
| 10+/generational | 7 |
| Foundational | Ob 7 + 2 surcharge = 9; RS consequence ×3 |

Active Knot Crisis on target: +1 Ob.
RS minimum cost: −3 on Success. Failure: snap-back Wound + RS −6 minimum.

### Locking (Forced Resolution)
Pool: Spirit + History (no TPS) | TN 7 (TN 8 for FR)
Requirements: TS 50+; Diagnosis mandatory. Min Ob: 4.
| Scale | Ob |
|-------|----|
| Object | 4 |
| Personal | 5 |
| Relational/Process | 6 |
| Territorial | 7 |
| Structural/Foundational | 8+ |

TS 70+: −1 to all FR RS costs (min 1).

| Degree | RS | Coherence |
|--------|----|-----------|
| Overwhelming | −1 | 0; +1 TS |
| Success | −1 | 0 |
| Partial | −2 | −1 (cap) |
| Failure | −3 | −1 (cap); 2 Wounds; adjacent ops +1 Ob rest of season |

Chronic drift: 2–3 seasons: RS −1/season + ops +1 Ob. 4+ seasons: RS −2/season. Permanent: RS drift ceases; permanent +1 Ob adjacent.
Reversal Ob: original practitioner's TS ÷ 10 (round up) − 2, min 1.

### Dissolution (Forced Resolution)
Pool: Spirit + History (no TPS) | TN 7 (TN 8 for FR)
Requirements: TS 50+; Diagnosis mandatory. Min Ob: 4. Same Ob table as Lock.

| Degree | RS | Coherence |
|--------|----|-----------|
| Overwhelming | −3 | 0; micro-Gap forms/closes in scene |
| Success | −5 | 0; Gap forms, closes end of scene |
| Partial | −6 | −1 (cap); Shifting Object; Gap doesn't close without Mending |
| Failure | −8 | −1 (cap); full Gap; Monstrous Incursion; Practitioner incapacitated |

### Mending (Substrate Repair)
Pool: Attunement + Focus + TPS | TN 7
Requirements: TS 50+; Diagnosis mandatory. Target must be a Gap, Shifting Object, or Locked Zone border.
Ob ceiling: 8 (regardless of stacked modifiers).
| Gap Type | Ob | Min TS |
|----------|----|--------|
| Shifting Object | 2 | 50+ |
| Micro-Gap (same scene) | 3 | 50+ |
| Standard Gap (1 session–1 season) | 5 | 50+ |
| Entrenched Gap (1+ seasons) | 6 | 70+ |
| Catastrophic Gap (3+ seasons) | 7 | 70+ |
| Locked Zone border | 8+ | 70+ |

| Degree | RS | Coherence |
|--------|----|-----------|
| Overwhelming | +2 | −1 (base) |
| Success | +1 | −1 (base) |
| Partial | 0 | −1 (cap); Gap reduced one severity |
| Failure | −2 | −1 (cap) |

Threadcut being interference: +Ob = being's TS ÷ 20 (round up), max +4.

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
| Past-Oriented Pulling | −1 additional |
| Mending | −1 |
| Dissolution residue use | −1 additional (not subject to cap) |
| History Resonance risk die shows 1 | −1 |
| Degree table Failure (Relational+ scale) | apply as written |

| Coherence | State | Key Effects |
|-----------|-------|-------------|
| 10–8 | Stable | No penalty |
| 7–5 | Dissonant | Narrative flickers |
| 4–3 | Fragmented | −1D social/Memory; +1 Ob all ops |
| 2 | Fractured | −2D social/Memory; Belief Co-Authorship begins |
| 1 | Severed | −2D; dissociative episodes; +2 Ob all ops |
| 0 | Rendering Crisis | Campaign event. NPC if unresolved by season end. |

Recovery: Full season non-practice: +1. Anchoring Scene (Bonds TN7 Ob2): +1. Cannot exceed 10.

## Dissolution Residue
Bonus dice: Potency rating (1–5). Explode on 9–10.
Cost: −1 Coherence per use (additional; not subject to §3.2 op cap at Relational+).
Same source: +1 Ob per prior use.

## Rendering Stability (RS) Track
Range: 100→0. Starting: RS 60 (default campaign).
| RS | State | World Effects |
|----|-------|---------------|
| 100–80 | Stable | None |
| 79–60 | Strained | Occasional wrongness near Thread sites |
| 59–40 | Fragile | Shifting Objects spontaneous (1/season); Thread ops +1 Ob in affected territories |
| 39–20 | Fractured | Spontaneous Gaps (1d10/season; 1–2 = Gap); Monstrous Incursion risk; rendering failures |
| 19–1 | Critical | As Fractured + doubled Gap risk; +1 Ob worldwide; faction Stability checks Ob1; Mandate 0 → Faction Fracture |
| 0 | The Rupture | Campaign ends |

RS threshold effects: activate/deactivate at Accounting, not mid-scene.
RS threshold effects are cumulative (each lower band includes all higher band effects).
Seasonal cap: ±10 net RS change per season (applies at Accounting).

Key RS degradation values:
- FR Dissolution Failure: −8. Dissolution Success: −5. POP Success: −3 minimum.
- Gap persisting per season: −4. Lock chronic drift: −1 to −2/season.
- Winter annual drift: −1. Siege per season: −1.
- Mending Success: +1. Mending Overwhelming: +2.
- Weaving Overwhelming (Relational+): +1.

## Collective Operations
Anchor: highest TS practitioner. Rolls full pool.
Helper contribution: ⌊Cognition ÷ 2⌋ bonus dice each.
If pool drops below half Anchor's solo pool: +1 Ob.
Directly opposing Beliefs: pre-Leap Belief check (Spirit TN7 Ob1) or helper drops out.
Tangential conflicting Beliefs: helper dice don't chain on 10.

## Cross-Mode Thread
| Rule | TTRPG | Board Game | Hybrid |
|------|-------|-----------|--------|
| Operations | Weaving/Pulling/Mending/Lock/Dissolution | Weave/Mend/Investigate/Harvest orders | Personal: TTRPG; Strategic: BG |
| Co-movement | Version C (temporal + epistemic + d6) | Co-Movement Cards (18) | Personal: Version C; Strategic: Cards |
| Coherence | Tracked per PC | Not tracked | Tracked during Personal Phase only |
| RS | 100→0 at Accounting | 100→0 at Accounting | Cascade Phase Accounting; cap ±10 |
| Lock drift | GM tracks | Territory card: RS −1/season | TTRPG Lock → territory card at Cascade |

## Observation / Detection
| Observer TS | Perception |
|-------------|-----------|
| 0–9 | Nothing |
| 10–29 | Vague unease |
| 30–49 | Senses operation, general direction |
| 50–69 | Identifies type and target |
| 70+ | Full configuration |

Concealment from TS 30+ observers: Cognition only (no History), TN7, Ob = observer TS ÷ 30 (round up). Pre-Leap action.

<!-- patch_history: references/params_threadwork_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->
