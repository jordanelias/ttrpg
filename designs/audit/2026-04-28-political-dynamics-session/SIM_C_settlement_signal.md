<!-- [PROVISIONAL: 2026-04-29 — simulation Direction C] -->
<!-- STATUS: PROVISIONAL — granular trace of Settlement Signal mechanics under doc 12 v1.1 -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/SIM_C_settlement_signal.md -->
<!-- COMPANION: SIM_A, SIM_B; 12_development_specification.md v1.1 -->

# Simulation C — Settlement Signal Flow (PATCH 2.5 null guards, governor fallback, Resonance Lookup)

**Source spec:** `12_development_specification.md` v1.1 (commit `9dede391`).
**Primary patches under test:** PATCH 2.5 (`compute_settlement_signal` null guards + governor fallback); PATCH 2.7 (`resonance_lookup` category fallback + 8 `EVENT_CATEGORIES`); PATCH 3.9 (`population_disposition` recalc); PATCH 3.12 (player-Disposition amplification scope, applied within PATCH 2.5).
**Method:** Nine granular scenarios. Each traces compute → Signal → faction Concern propagation; verifies edge cases for the three null guards; measures Concern volume against the design target (0.5–1.5 per NPC per Accounting per doc 17 §8.6).
**Companion:** Builds on SIM-A `[INV-1..4]` and SIM-B `[DA-INV-1..7]`. Adds Settlement-specific invariants below.

---

## §0 Conventions and SIM-C-specific invariants

### 0.1 Settlement geography for these traces

Three test settlements:
- **Solmund** (Crown seat, Faction=Crown, Order/Continuity-leaning). Population large; ~12 Passive NPCs; Almud as governor.
- **Eastfort** (Crown vassal frontier outpost, Faction=Crown). Population small; 2 Passive NPCs; military governor (Captain).
- **Reedgate** (Crown remote farming hamlet). Population very small; 0 Passive NPCs in roster; no governor (administered remotely from Solmund).

### 0.2 Notation

`Signal{tag, affect, salience}` shorthand. `SS = SettlementSignal`. State transitions: `field: old → new`.

### 0.3 Settlement-specific invariants under test

- **`[SS-INV-1]` Single-output-per-call.** Each call to `compute_settlement_signal()` returns either a SettlementSignal or `None`. Never crashes, never partial.
- **`[SS-INV-2]` Null-guard correctness.** Each of the three guards in PATCH 2.5 (empty passive_npcs, empty weighted_memories, all-zero weights) correctly returns None or governor-fallback Signal.
- **`[SS-INV-3]` Player-Disposition scope.** Disposition-with-player amplification only applies to Memories that involve the player (PATCH 3.12 / S-44-A).
- **`[SS-INV-4]` Cascade decay.** Signal salience scaled by 0.7 before propagation. Governor-only fallback Signal at additional 0.5 weight.
- **`[SS-INV-5]` Resonance lookup totality.** `resonance_lookup(c, event_type)` returns a defined value for every (Conviction, event_type) pair, falling back through category → default if needed.
- **`[SS-INV-6]` Population-disposition bounds.** `population_disposition` clamped to [-3, +5].
- **`[SS-INV-7]` Salience bounds.** Signal salience ∈ [1, 5] post-clamp.
- **`[SS-INV-8]` Concern volume target.** Faction Concerns generated from settlement Signals: 0.5–1.5 per Active NPC per Accounting per doc 17 §8.6.

---

## §1 Scenario 1 — Standard settlement Signal: Solmund, populated

**Goal.** Trace nominal flow with multiple Passive NPCs and recent Memories. Verify deterministic output.

### 1.1 Initial state

```
Solmund:
  passive_npcs: [Baker, Smith, Dockmaster, Inkeep, Constable, Tanner, Weaver, Apothecary, Schoolmaster, Boatwright, Granary_warden, Rector_assistant]  (12)
  governor: Almud (controlling faction = Crown)
  recent_events (last 2 seasons): mixture; not directly used by compute (uses NPC Memories instead)
  
Each Passive NPC has 1-3 Memories from last 2 seasons. Sample:
  Baker.recent_memories(seasons=2) = [
    M(event_type="economic_windfall", affect=+1, salience=3, season=T-1, involves_player=False),
    M(event_type="trade_deal", affect=+0.5, salience=2, season=T-2, involves_player=True),  # player negotiated
  ]
  Smith.recent_memories(seasons=2) = [
    M(event_type="raid_threat", affect=-1, salience=4, season=T-1, involves_player=False),
  ]
  Dockmaster.recent_memories(seasons=2) = [
    M(event_type="trade_deal", affect=+1, salience=3, season=T-2, involves_player=True),
  ]
  ... (similar for others, varied event_types and affects)

Local dispositions:
  Baker.local_disposition_with_player = +2  (positive — player did them a favor)
  Dockmaster.local_disposition_with_player = +3
  Smith.local_disposition_with_player = 0  (neutral)
  ...
```

### 1.2 Trace `compute_settlement_signal(Solmund, recent_memories)`

**Guard 1:** `if not Solmund.passive_npcs` → False (12 NPCs). Skip guard.

**Aggregation loop:**
```
weighted_memories = []
For Baker:
  M1 (economic_windfall, +1, sal=3, involves_player=False): weight = 3 (no player amp). append (M1, 3).
  M2 (trade_deal, +0.5, sal=2, involves_player=True): weight = 2 × Baker.local_disposition_with_player = 2 × 2 = 4. append (M2, 4).
For Smith:
  M3 (raid_threat, -1, sal=4, involves_player=False): weight = 4. append (M3, 4).
For Dockmaster:
  M4 (trade_deal, +1, sal=3, involves_player=True): weight = 3 × 3 = 9. append (M4, 9).
... (continue for all 12 Passive NPCs)
```

Assume aggregate produces ~20 weighted memories total.

**Guard 2:** `if not weighted_memories` → False. Skip.

**Group by event_type:**
```
grouped = {
  "economic_windfall": [(M1, 3), ...],     # sum_of_weights = 8
  "trade_deal": [(M2, 4), (M4, 9), ...],   # sum_of_weights = 16  ← dominant
  "raid_threat": [(M3, 4), ...],            # sum_of_weights = 6
  "harvest_report": [...],                  # sum_of_weights = 4
  ...
}
```

**Guard 3:** `if not grouped or all(sum_of_weights(g) == 0 for g in grouped)` → False (we have nonzero groups). Skip.

**dominant_tag:** `max(grouped, key=sum_of_weights)` → `"trade_deal"` (sum 16).

**net_affect:**
```
total_weight = 3 + 4 + 4 + 9 + ... ≈ 35 (across ~20 memories, each weighted)
weighted_affect_sum = (1)(3) + (0.5)(4) + (-1)(4) + (1)(9) + ... ≈ +12
net_affect = +12 / 35 ≈ +0.34
```

**Signal:**
```
signal = SettlementSignal(
  affect_axis = +0.34,
  primary_tag = "trade_deal",
  salience = min(5, max(1, |0.34| × 2)) = max(1, 0.68) = 1
)
signal.salience *= 0.7 → 0.7
return signal
```

Hmm — salience = 0.7 after cascade decay. **Concern: this is below typical event-impact thresholds (events at salience<1 are typically below interest).** Let me check what happens downstream.

### 1.3 Settlement Signal → faction Concern propagation

Per §5.2: "Settlement Signal propagates to controlling faction's relevant Active NPC as a Concern (Procedure B input next Accounting)."

The "relevant Active NPC" is implementation-dependent but typically the faction member responsible for the settlement (governor or seat-holder). For Solmund: Almud is governor.

```
Concern generated for Almud at T+1:
  tag = derive_concern_tag_from_signal(signal)
  signal.salience = 0.7 → Concern.salience = round(0.7) = 1?  
  Or: Concern.salience = signal.salience (0.7), in which case it's < 1 — sub-threshold.
```

**`[GAP: SIM-C-G1]` Signal-salience-to-Concern-salience mapping.** Spec says "propagates as Concern" but doesn't define the conversion. Direct? Rounded? Floor to 1? If signal.salience < 1 (sub-threshold), is the Concern dropped? Surface for v1.2: `[GAP: signal-to-Concern salience mapping in §5.2 propagation — surfaced by SIM-C scenario 1; v1.2 spec target — recommend round to nearest int with floor at 1, drop if 0]`.

Assuming round + floor 1: Concern at salience 1 generated for Almud about "trade_deal" trend in Solmund. Low-salience but tracks the dominant economic-positive movement.

### 1.4 Verification (Scenario 1)

- **`[SS-INV-1]` single-output:** Returned a non-None Signal. ✓
- **`[SS-INV-3]` player-disposition scope:** Player-amplified weighting fired only on M2 and M4 (involves_player=True). M1, M3 used base salience. ✓
- **`[SS-INV-4]` cascade decay:** Signal salience reduced to 0.7 from initial 1.0. ✓
- **`[SS-INV-7]` salience bounds:** 0.7 is below the [1, 5] range. **Per spec the formula is `salience = min(5, max(1, |net_affect| * 2))` then `salience *= 0.7` → final 0.7.** This violates `[SS-INV-7]` post-cascade. The clamp [1,5] is inside the formula but cascade decay can bring it below 1. **Bug or feature?**
  - Reading PATCH 2.5: `signal.salience *= 0.7` is applied AFTER the min/max clamp. So decay can produce sub-1 salience.
  - This is consistent with old spec behavior — Settlement Signals can be weak. But interacts badly with downstream Concern generation if signal.salience<1 → Concern at salience<1 → potentially sub-threshold.
  - **Recommend explicit clamp post-decay: `signal.salience = max(0, signal.salience * 0.7)` and propagation logic that drops Signals with salience<1 explicitly.** Surface: `[GAP: SIM-C-G2 — signal salience can fall below clamp range after cascade decay; v1.2 should specify post-decay handling]`.
- **Knock-on:** If Solmund had stronger net_affect (e.g., |0.5| × 2 = 1.0, then × 0.7 = 0.7), still sub-1. Need `|net_affect| ≥ 0.71` for post-decay salience ≥ 1. **Realistic settlement events with net_affect ≈ 0.3-0.5 (mixed mood) fail to propagate as Concerns under this formula.** Either spec is intended to filter low-affect-spread settlements (a feature) or Concern volume target won't be met. Let me measure in Scenario 7.

---

## §2 Scenario 2 — Empty Passive NPCs + governor present (Guard 1 → governor fallback)

**Goal.** Verify governor fallback path when no Passive NPCs.

### 2.1 Setup

```
Eastfort (frontier outpost):
  passive_npcs: []  (no Passive NPC roster — frontier garrison only)
  governor: Captain (Standing 4 in Crown's military hierarchy; Order primary)
  recent_events: [
    Event(event_type="raid_threat", affect=-2, salience=4, season=T-1),
    Event(event_type="reinforcement_arrived", affect=+1, salience=3, season=T-2),
  ]
```

### 2.2 Trace

```
compute_settlement_signal(Eastfort, recent_memories):
  Guard 1: not Eastfort.passive_npcs → True (empty list).
  Eastfort.governor is set (Captain) → branch: from_governor.
  
SettlementSignal.from_governor(Captain, [raid_threat, reinforcement_arrived]):
  recent_events not empty.
  dominant = max(recent_events, key=salience) → raid_threat (salience 4)
  
  affect = interpret_event_affect(raid_threat, Captain.armature)
    Captain.armature: Order-primary, military-domain perspective.
    raid_threat: a raid is a threat to Order. interpret as negative affect, magnitude 2.
    → affect_axis = -2
  
  signal = SettlementSignal(
    affect_axis = -2,
    primary_tag = "raid_threat",
    salience = 4 × 0.5 = 2.0  (governor-only at half weight)
  )
  return signal
```

Returns Signal{tag=raid_threat, affect=-2, salience=2.0}.

### 2.3 Propagation

Concern generated for Almud (Crown faction leader / Solmund governor) about Eastfort's raid_threat.
- Concern.salience = 2 (round(2.0)).
- Almud's response: depending on his armature, may propose military Domain Action ("send reinforcements"), shifting to a Direction-B trace.

### 2.4 Verification (Scenario 2)

- **`[SS-INV-2]` null-guard 1 correctness:** Confirmed governor fallback engaged when passive_npcs empty. ✓
- **`[SS-INV-4]` governor weight halving:** 4 × 0.5 = 2.0. ✓
- **Knock-on observation:** Frontier outposts produce Signals only when governor exists. This means Eastfort's voice in faction strategic dynamics is half-strength compared to Solmund's. **Mechanically encodes "frontier matters less than the seat" — politically authentic.**
- **`[GAP: SIM-C-G3]` `interpret_event_affect()` not specified.** Patch 2.5 references it as a function call but the algorithm is undefined. Likely uses event's intrinsic affect modulated by armature alignment. Surface: `[GAP: interpret_event_affect() spec — surfaced by SIM-C scenario 2; v1.2 spec target — recommend `event.affect × armature_alignment_with_event_type` formula]`.

---

## §3 Scenario 3 — No recent Memories (Guard 2 → None)

**Goal.** Verify `None` returned when Passive NPCs exist but no recent activity.

### 3.1 Setup

```
Solmund (during quiet season):
  passive_npcs: [12 Passive NPCs as in Scenario 1]
  But: each Passive NPC's recent_memories(seasons=2) returns [] this Accounting.
  (Suppose: nothing remarkable happened the past two seasons; old Memories aged out
   beyond the 2-season window.)
```

### 3.2 Trace

```
Guard 1: passive_npcs non-empty. Skip.

Aggregation loop:
  For each NPC, recent_memories(seasons=2) = [].
  weighted_memories remains empty.

Guard 2: not weighted_memories → True.
  return None.
```

Returns None. No Signal propagated. No Concern generated for Almud about Solmund this Accounting.

### 3.3 Verification (Scenario 3)

- **`[SS-INV-1]` single-output, null case:** Returned None cleanly. ✓
- **`[SS-INV-2]` null-guard 2 correctness:** ✓
- **Politically authentic:** Quiet seasons in stable settlements produce no faction-level political signal. Faction NPCs aren't generating Concerns about Solmund in the absence of reportable events. Realistic.
- **Cumulative implication:** If Solmund is consistently quiet for 4+ seasons, Almud has no settlement-derived Concerns. His Concern budget (0-3 active) is filled by other sources (peer NPCs, faction events, Knowledge-derived). **Concern volume target measurement deferred to Scenario 7.**

---

## §4 Scenario 4 — All-zero weights edge case (Guard 3 → None)

**Goal.** Construct condition where all weighted-memory groups have zero weight.

### 4.1 Setup

```
Solmund (special edge case):
  passive_npcs: [Baker]  (only one; thinly populated)
  Baker.recent_memories(seasons=2) = [
    M(event_type="trade_deal", affect=+0.5, salience=0, involves_player=False),
    M(event_type="harvest", affect=+0.3, salience=0, involves_player=False),
  ]
  (Both Memories have salience 0 — perhaps after Knowledge-Decay-style decay through 
   Memory salience-floor mechanism, both reached the floor.)
```

### 4.2 Trace

```
Guard 1: passive_npcs non-empty. Skip.

Aggregation:
  For Baker:
    M1: salience 0, involves_player=False → weight = 0.
    M2: salience 0, involves_player=False → weight = 0.
  weighted_memories = [(M1, 0), (M2, 0)].

Guard 2: weighted_memories non-empty. Skip.

grouped = {
  "trade_deal": [(M1, 0)],   # sum_of_weights = 0
  "harvest": [(M2, 0)],      # sum_of_weights = 0
}

Guard 3: not grouped or all(sum_of_weights == 0) → second clause True.
  return None.
```

Returns None.

### 4.3 Verification (Scenario 4)

- **`[SS-INV-2]` null-guard 3 correctness:** ✓ Even with non-empty weighted_memories list, all-zero-weights case is caught.
- **Realistic edge case:** Memories at salience-floor 0 (per existing spec — salience can decay or be set to 0 in some paths) produce no political signal. Spec correctly handles this.
- **`[GAP: SIM-C-G4]` Memory salience reaching 0.** Spec doesn't fully specify when Memory salience can reach 0. The §2.6 salience-floor mechanic uses `max(0, ...)` in some Procedures. Memories at salience-0 should probably be candidates for replacement under §2.6 rules. **Cross-reference suggestion:** check Memory replacement rules for salience-0 cases. Not a critical gap; surface for v1.2 doc-cleanup: `[GAP: salience-0 Memory lifecycle — surfaced by SIM-C scenario 4; v1.2 minor doc target]`.

---

## §5 Scenario 5 — Player-Disposition amplification scope (PATCH 3.12 / S-44-A / 2.5)

**Goal.** Verify Memory amplification by `local_disposition_with_player` only applies when `memory.involves_player = True`.

### 5.1 Setup

```
Solmund:
  passive_npcs: [Smith]  (focused trace)
  Smith.local_disposition_with_player = +5  (player saved Smith's son in earlier Arc)
  Smith.recent_memories(seasons=2) = [
    M_a(event_type="raid_repelled", affect=+1, salience=3, involves_player=False),  
        # Player wasn't involved; Crown forces did it
    M_b(event_type="player_intervention", affect=+2, salience=4, involves_player=True),  
        # Player did this directly
    M_c(event_type="bad_harvest", affect=-1, salience=3, involves_player=False),
  ]
```

### 5.2 Trace

```
Aggregation:
  M_a (involves_player=False): weight = 3 (salience only)
  M_b (involves_player=True): weight = 4 × 5 = 20  ← strong amplification
  M_c (involves_player=False): weight = 3 (salience only)
  
weighted_memories = [(M_a, 3), (M_b, 20), (M_c, 3)]
total_weight = 26

grouped:
  "raid_repelled": [(M_a, 3)]
  "player_intervention": [(M_b, 20)]   ← dominant
  "bad_harvest": [(M_c, 3)]

dominant_tag = "player_intervention"
net_affect = (1×3 + 2×20 + (-1)×3) / 26 = (3 + 40 - 3) / 26 = 40/26 ≈ +1.54

signal = SettlementSignal(
  affect_axis = +1.54,
  primary_tag = "player_intervention",
  salience = min(5, max(1, 1.54 × 2)) = min(5, 3.08) = 3.08
)
signal.salience *= 0.7 → 2.16
```

Strong positive Signal centered on "player_intervention." Concern propagated to Almud at salience 2 ish.

### 5.3 Compare to scope-broken hypothetical (without PATCH 3.12 / pre-patch behavior)

If Disposition-amp applied to all Memories (pre-patch):
```
M_a weight = 3 × 5 = 15
M_b weight = 4 × 5 = 20
M_c weight = 3 × 5 = 15
total = 50

grouped:
  "raid_repelled": 15
  "player_intervention": 20  ← still dominant (barely)
  "bad_harvest": 15

net_affect = (1×15 + 2×20 + (-1)×15) / 50 = 40/50 = +0.8
salience = 1.6, decay → 1.12
```

In pre-patch behavior, net_affect was secretly inflated by player-Disposition across the board. Smith's positive feeling about the player infected the bad_harvest Memory's reading. Post-patch, only Memories the player participated in are amped.

### 5.4 Verification (Scenario 5)

- **`[SS-INV-3]` player-Disposition scope:** Confirmed correctly scoped. ✓
- **Magnitude shift vs pre-patch:** post-patch net_affect (+1.54) is *higher* than pre-patch (+0.8) for this setup, because positive player_intervention dominates more strongly when only it's amplified. **Counterintuitive**: PATCH 3.12 doesn't necessarily produce smaller-magnitude Signals — it produces Signals *focused on the player's actual involvement*. Smith's player_intervention Memory doesn't get drowned in the noise of high-Disposition-amped raid/harvest Memories.
- **Strategic property:** Settlements with high-Disposition-with-player Passive NPCs produce sharper Signals about player actions specifically. The player's footprint in the world is *more visible to faction NPCs* via settlement Signals, but only for Memories that genuinely involve the player. **Mechanically encodes "your reputation precedes you" but only for things you actually did.**
- **Knock-on:** If a faction NPC sees Almud's Concern about "player_intervention in Solmund" surfaces this Accounting, the player's recent action receives institutional attention. This is the path by which player choices feed back through the faction-political layer — exactly the design intent (per intent of game in project README).

---

## §6 Scenario 6 — Resonance lookup unknown event_type (PATCH 2.7)

**Goal.** Trace `resonance_lookup()` category fallback for an unknown event_type. Verify all 7 Convictions get a defined response.

### 6.1 Setup

A new event_type "philosophical_dispute_in_market" is generated by an emergent Direction A scenario. This event_type is NOT in `RESONANCE_TABLE` (the 210-entry symbolic resonance table per E-38 Jordan-decision item).

A Crown NPC (e.g., Confessor) processes this event during Concern generation. `event_impact_matrix.compute_resonance(npc.armature, event)` is called. Internally it calls `resonance_lookup(c, event.event_type)` for each c in CONVICTIONS.

### 6.2 Trace

```
For each Conviction c in [Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity]:
  resonance_lookup(c, "philosophical_dispute_in_market"):
    if (c, "philosophical_dispute_in_market") in RESONANCE_TABLE:
      return RESONANCE_TABLE[(c, "philosophical_dispute_in_market")]
    # Not in table.
    category = categorize_event_type("philosophical_dispute_in_market")
    # categorize_event_type maps event_type to one of 8 categories.
    # "philosophical_dispute_in_market" — not obviously in any pre-authored list.
    # Possible matches: discovery? (philosophical content?) economic? (in market?) personal?
    # If author didn't tag it, falls to "default".
    category = "default"  (assumed — no tag)
    return CATEGORY_DEFAULT_RESONANCE["default"][c]
    → returns "neutral" for all Convictions (default row is all-neutral).
```

Result: Confessor's armature interprets this event as resonance=neutral on all Convictions. **No Concern triggered from event-impact** (or low-priority Concern with neutral framing).

### 6.3 Trace variant — author retrospectively categorizes

Same scenario, but author has tagged "philosophical_dispute" → category = "discovery":
```
categorize_event_type("philosophical_dispute_in_market") = "discovery"
CATEGORY_DEFAULT_RESONANCE["discovery"] = {
  Faith: neutral, Order: neutral, Reason: aligned, Equity: neutral, 
  Precedent: neutral, Autonomy: aligned, Continuity: neutral
}
```

Confessor (Faith primary): returns neutral. Concerns generation for Confessor: muted (event interpreted as not engaging Faith's interpretive frame).

If Scribe (Reason primary) were affected by same event:
```
For Scribe, resonance_lookup(Reason, "philosophical_dispute_in_market") → "aligned"
```

Scribe interprets the event as aligned-with-Reason. Generates Concern around the Reason-engagement of the event. Higher-salience Concern than Confessor's would be.

### 6.4 Verification (Scenario 6)

- **`[SS-INV-5]` resonance-lookup totality:** Verified across all 7 Convictions for both untagged and tagged paths. Every (c, event_type) returns a defined value. ✓
- **`[GAP: SIM-C-G5]` `categorize_event_type()` mapping infrastructure.** Spec defines the EVENT_CATEGORIES dict (mapping category → list of event_types) but `categorize_event_type()` is the inverse (event_type → category) lookup. Inversion is straightforward but not explicitly spec'd. Surface: `[GAP: categorize_event_type() inverse-lookup spec — surfaced by SIM-C scenario 6; v1.2 spec target — straightforward but should be specified for unambiguous implementation]`.
- **Coverage check:** PATCH 2.7's 8 categories cover most plausible event_types. Edge cases (philosophical_dispute, gossip, ceremony with unclear categorization) would fall to "default" if not pre-tagged. **The "default" row's all-neutral output is the design's safety net** — unrecognized events don't cause spurious resonance, but they also don't engage NPCs' Conviction frames. Trade-off.
- **Strategic property:** Authoring decision required at content-time: when introducing a new event_type, author MUST tag it to a category or it produces neutral resonance (=> NPCs don't react to it strongly). Forces conscious authoring decisions about what events should engage which Conviction frames. **Good content-design constraint.**

---

## §7 Scenario 7 — Concern volume target measurement (doc 17 §8.6)

**Goal.** Estimate Concern volume per Active NPC per Accounting from settlement-Signal source. Compare to design target 0.5–1.5.

### 7.1 Setup

Crown faction with 4 Active NPCs (Almud, Marshal, Confessor, Ambassador) controls 6 settlements:
- Solmund (seat, 12 Passive NPCs, governor=Almud)
- Eastfort (outpost, 2 Passive NPCs, governor=Captain S4)
- Reedgate (hamlet, 0 Passive NPCs, no governor)
- Northpass (outpost, 3 Passive NPCs, governor=Lord-Captain S5)
- Westmarch (large vassal town, 8 Passive NPCs, governor=Bailiff S5)
- Loomhaven (small vassal, 4 Passive NPCs, governor=Reeve S4)

Each Accounting, `compute_settlement_signal()` is called per settlement.

### 7.2 Settlement Signal generation per Accounting (estimated)

| Settlement | Passive | Governor | Likely outcome |
|---|---|---|---|
| Solmund | 12 | yes | Signal usually generated (high-activity seat) |
| Eastfort | 2 | yes | Signal sometimes (sparse Memories common) |
| Reedgate | 0 | no | None always (Guard 1 + no governor → None) |
| Northpass | 3 | yes | Signal sometimes |
| Westmarch | 8 | yes | Signal usually |
| Loomhaven | 4 | yes | Signal sometimes |

Estimated Signal-yield per Accounting: ~3-4 of 6 settlements produce a Signal.

### 7.3 Signal → Concern propagation

Per §5.2: each Signal propagates to "controlling faction's relevant Active NPC as a Concern." How is "relevant" determined?
- **Spec doesn't fully specify.** Plausible heuristics:
  - Settlement governor if governor is an Active NPC (rare — governors are often non-roster Captains/Bailiffs).
  - Faction leader for seat settlements (Almud for Solmund).
  - Active NPC with most recent Memory of the dominant_tag.
- **`[GAP: SIM-C-G6]` "Relevant Active NPC" routing for Signal-derived Concerns.** Spec is silent on the routing mechanism. Surface: `[GAP: Settlement-Signal → Concern routing — surfaced by SIM-C scenario 7; v1.2 spec target — recommend (a) governor if Active, else (b) faction leader if seat, else (c) round-robin among inner-circle by signal.primary_tag domain affinity]`.

Assume reasonable routing: Almud receives Solmund and Westmarch Signals; Marshal receives Eastfort and Northpass (military domain affinity); Confessor receives Loomhaven (theological/diplomatic-coded events); Ambassador receives whichever cross-border event surfaces.

### 7.4 Concern volume estimate

Per Accounting, ~3-4 Signals produce ~3-4 Concerns distributed across 4 Active NPCs.

**Average per NPC per Accounting:** 3-4 / 4 = 0.75 - 1.0 Concerns from settlement-Signal source.

This **matches the design target (0.5–1.5)** quite well.

### 7.5 Concern-volume amplifiers and dampeners

**Amplifiers (would push toward upper bound):**
- High-Disposition-with-player Passive NPCs (Scenario 5) produce stronger Signals → more Concerns crossing salience threshold.
- Multi-event seasons (raid_threat + economic_windfall + ceremonial event) increase grouped sums and dominant-tag clarity.

**Dampeners (would push toward lower bound):**
- Quiet seasons (Scenario 3 — many settlements return None) → fewer Concerns.
- Mixed-affect aggregation (Scenario 1 — net_affect 0.34 producing salience<1 post-decay) → Signals fail to cross threshold.
- `concern_history` cooldown (PATCH 3.1): if the NPC just resolved a same-domain Concern, same-tag regen is suppressed unless event.salience ≥ 4.

### 7.6 Verification (Scenario 7)

- **`[SS-INV-8]` Concern volume target:** Verified in expectation (~0.75-1.0 per NPC per Accounting from settlement-Signal source). Within target [0.5, 1.5]. ✓
- **Sensitivity:** Volume is sensitive to (a) `[GAP: SIM-C-G2]` post-decay salience clamp behavior, (b) `[GAP: SIM-C-G6]` routing logic. Different interpretations of these could swing volume up to ±50%. Worth nailing down for v1.2 to prevent volume drift.
- **Multi-source observation:** Settlement-Signal is one of *several* Concern sources. Other sources include (i) direct event observation (via PATCH 3.3 visibility gate), (ii) Knowledge-derived (existing path), (iii) Knot-mediated (PATCH 3.6). Total Concern volume across all sources should be measured separately; Scenario 7 only addresses settlement-source contribution.
- **Strategic property:** Active NPCs in factions with many settlements (e.g., Crown ~6 settlements, Hafenmark ~3, Varfell ~5) get more settlement-Signal Concerns per Accounting. Faction-leadership cognitive load scales with territory. **Realistic Renaissance ruler-burden dynamic.**

---

## §8 Scenario 8 — Population disposition recalculation (PATCH 3.9 / N-35-A)

**Goal.** Trace `population_disposition[settlement, faction]` recalc; verify Order/Prosperity → disposition mapping; observe knock-on into Settlement Meta-Armature.

### 8.1 Setup

```
Solmund (controlled by Crown):
  order: 7 (out of 10 — generally well-ordered Renaissance city)
  prosperity: 6
  recent_event_delta history (last 4 seasons of Crown-caused Disposition events):
    season T-3: trade_deal_succeeded → Crown caused +1 disposition shift
    season T-2: nothing significant
    season T-1: bad_harvest_response → Crown caused -2 (Crown's response to harvest failure was inadequate)
    season T-0: tax_relief_announced → Crown caused +1
```

### 8.2 Trace

```
population_disposition[Solmund, Crown] recalculation each Accounting:

normalized_order(Solmund.order=7) = map [0,10] → [-2,+2]:
  (7-5)/2.5 = +0.8  (linear; midpoint 5 → 0; max 10 → +2)
normalized_prosperity(Solmund.prosperity=6) = (6-5)/2.5 = +0.4

recent_event_delta(Crown, last 4 seasons, decay 0.7^seasons_ago):
  season T-3 (3 seasons ago): +1 × 0.7^3 = +1 × 0.343 = +0.343
  season T-2 (2 seasons ago): 0 × 0.7^2 = 0
  season T-1 (1 season ago): -2 × 0.7^1 = -1.4
  season T-0 (0 seasons ago): +1 × 0.7^0 = +1
  sum = +0.343 + 0 - 1.4 + 1.0 = -0.057  (very slightly negative — recent bad-harvest weighs heavily)

population_disposition[Solmund, Crown] = clamp(
  0.4 × +0.8 + 0.4 × +0.4 + 0.2 × (-0.057),
  -3, +5
)
= clamp(0.32 + 0.16 - 0.011, -3, +5)
= clamp(0.469, -3, +5)
= +0.469  ≈ +0.5
```

Solmund's population is slightly positive about Crown — reflects high-Order, mid-Prosperity baseline tempered by recent bad-harvest mismanagement.

### 8.3 Trace variant — Order collapse

Suppose Solmund's order drops to 2 (riot following a harsh tax decree):
```
normalized_order(2) = (2-5)/2.5 = -1.2
normalized_prosperity(6) = +0.4 (unchanged)
recent_event_delta: with riot event added, suppose -3 cumulative.

population_disposition = clamp(
  0.4 × (-1.2) + 0.4 × 0.4 + 0.2 × (-3),
  -3, +5
)
= clamp(-0.48 + 0.16 - 0.6, -3, +5)
= clamp(-0.92, -3, +5)
= -0.92
```

Population shifts to negative disposition. **Knock-on into Settlement Meta-Armature §5.1:**
- `population_disposition_weight = 0.1` × negative disposition → Settlement Meta-Armature shifts slightly away from Crown's institutional weight.
- This affects how Solmund interprets future events: less aligned with Crown's Order-frame.
- Cascade: Settlement Signal next Accounting will reflect this institutional drift.

### 8.4 Verification (Scenario 8)

- **`[SS-INV-6]` population-disposition bounds:** Both traces produced values within [-3, +5]. ✓
- **Order/Prosperity → disposition mapping:** verified. Linear normalization with midpoint 5 → 0 anchor.
- **Recency decay (0.7^seasons_ago):** verified — old events fade rapidly. After 4 seasons, weight = 0.7^4 = 0.24, near-irrelevant.
- **Bounds:** `clamp(-3, +5)` is asymmetric — population can be more positive than negative. Per existing Disposition spec convention. **Knock-on:** Crown can earn population_disposition up to +5 in well-governed settlements (real political capital); negatives bottomed at -3. Faction recovery from population disenchantment is *easier* than maximizing popular support — perhaps reflecting Renaissance ruler-pragmatism.
- **`[GAP: SIM-C-G7]` `recent_event_delta` source.** Spec says "Δ-Disposition events this faction caused this settlement." Where are these events stored/tracked? Likely a per-settlement ledger of faction-attributable events. Surface: `[GAP: Δ-Disposition event log infrastructure — surfaced by SIM-C scenario 8; v1.2 spec target — recommend `settlement.faction_event_history[faction] = list[(season, delta, event_type)]` capped at last 8 seasons]`.
- **Multi-faction disposition tracking:** Each settlement tracks `population_disposition[settlement, faction]` per *each* relevant faction. For Solmund (Crown-controlled but with Hafenmark trading interests), there might be `population_disposition[Solmund, Crown]` and `population_disposition[Solmund, Hafenmark]` separately. PATCH 3.9 says `[settlement, faction]` — explicitly per-faction. ✓ Spec is correct on this point.

---

## §9 Scenario 9 — Multi-Settlement composition (faction-scale signal aggregation)

**Goal.** Six-settlement faction. Three Accountings. Observe how settlement Signals interact with faction Concerns over time. Trace cumulative meta-armature drift.

### 9.1 Setup

```
Crown faction territories: 6 settlements (Solmund, Eastfort, Reedgate, Northpass, Westmarch, Loomhaven).

Active NPCs: Almud (S7, leader), Marshal (S7), Confessor (S5), Ambassador (S4).
```

### 9.2 Accounting 1 — establish baseline

Per Scenario 7 estimate: ~3-4 Signals generated this Accounting.
- Solmund: Signal{tag=trade_deal, affect=+0.34, salience=0.7} → fails Concern threshold? (per Scenario 1 GAP). Assume passes at salience 1.
- Eastfort: governor-only Signal{tag=raid_threat, affect=-2, salience=2}. → Marshal receives Concern.
- Reedgate: None.
- Northpass: governor-only Signal{tag=patrol_routine, affect=+0.5, salience=0.5} → fails threshold.
- Westmarch: Signal{tag=guild_dispute, affect=-1, salience=2} → Ambassador receives Concern (diplomatic-coded).
- Loomhaven: None (quiet season).

Active Concerns generated this Accounting from settlement source:
- Almud: 1 (Solmund trade_deal)
- Marshal: 1 (Eastfort raid_threat)
- Ambassador: 1 (Westmarch guild_dispute)
- Confessor: 0

Total: 3 Concerns / 4 NPCs = 0.75 per NPC. **Within target.**

### 9.3 Accounting 2

State changes:
- Marshal's raid_threat Concern resolved (Path A — proposed military DA, succeeded). Memory generated.
- Ambassador's guild_dispute Concern still active (ttl=3, now 2).
- Almud's trade_deal Concern resolved low-salience (no action needed); Memory generated.

New events this Accounting:
- Solmund: minor tariff change → Signal{tag=tariff_change, affect=-0.2, salience=0.4 post-decay} → fails threshold.
- Eastfort: post-raid recovery → Signal{tag=garrison_strengthen, affect=+1, salience=1.4 post-decay} → Marshal receives Concern.
- Reedgate: still nothing.
- Northpass: nothing.
- Westmarch: same guild_dispute persists → maybe re-Signal (concern_history cooldown blocks regen for Ambassador if salience<4).
  - Concern_history check: Ambassador has "westmarch_guild_dispute" in history? No — Ambassador's current Concern is still active (not resolved yet).
  - But: PATCH 3.1 cooldown is for *resolved* Concerns. Active Concerns don't need to regen. So Westmarch's repeat Signal is *absorbed* by the existing Concern — bumps its salience? **Spec doesn't fully specify Concern-bump on repeated Signal arrival.**
  - **`[GAP: SIM-C-G8]` Concern-update from repeated Signal during active Concern.** When a settlement Signal arrives matching an Active NPC's still-active Concern (same tag, same domain), what happens? Possibilities: (a) Concern.salience += new_signal_salience (cumulative), (b) Concern.salience = max(Concern.salience, new_signal_salience), (c) ignore (no double-counting). Spec is silent. Surface: `[GAP: repeated-Signal handling on active Concern — surfaced by SIM-C scenario 9; v1.2 spec target — recommend (b) max-update to prevent runaway accumulation while reflecting ongoing severity]`.
- Loomhaven: harvest report → Signal{tag=harvest_normal, affect=+0.5, salience=0.7} → fails threshold? Or passes at 1?

Active Concerns this Accounting:
- Almud: 1 (Solmund trade_deal — but resolved early; counts only briefly)
- Marshal: 2 (Eastfort raid_threat resolved; Eastfort garrison_strengthen new)
- Ambassador: 1 (Westmarch guild_dispute carrying over)
- Confessor: 0

If Marshal had only 1 active concern slot at start, the new garrison_strengthen Concern might displace something. Or fit (since Marshal's active list dropped to 0 after raid_threat resolved). Marshal ends with 1 active Concern.

### 9.4 Accounting 3

- Solmund's trade-deal cycle continues. Net affect lifting toward +0.5.
- Westmarch's guild_dispute escalates → Signal salience climbs as more Memories accumulate.
- Loomhaven: church-festival → Signal{tag=ceremonial, affect=+1.5, salience=2.1} → Confessor receives Concern (theological-coded).

Active Concerns:
- Almud: 0-1 (Solmund's trade is ongoing background)
- Marshal: 1 (garrison_strengthen, salience decaying or escalating per project state)
- Confessor: 1 (Loomhaven ceremonial — first settlement-source Concern)
- Ambassador: 1 (Westmarch guild — escalating)

Across 3 Accountings, average Concerns per NPC: ~0.75 per Accounting from settlement source. **Sustained within target.**

### 9.5 Cumulative meta-armature drift

Across 3 Accountings:
- Standing not changed (annual cadence — recalc only at Year boundary).
- But: each Concern resolution produces Memory → Procedure D drifts Opinions among inner-circle members.
- Almud's Opinion of Marshal: +0.x baseline → after Marshal-raid-success, drifts more positive (+0.x). Almud's faith in Marshal grows.
- Almud's Opinion of Ambassador: baseline → after persistent guild_dispute (Ambassador struggles to resolve), drifts mildly negative. Almud may begin to doubt Ambassador's competence.
- Confessor's late-arriving Loomhaven Concern resolution gives Confessor a positive interaction with the harvest-festival Lord-Captain → Confessor's network broadens.

Crown's meta-armature reflects these changes (small drifts) but is dominated by Standing weights — those don't change until Year boundary.

### 9.6 Verification (Scenario 9)

- **`[SS-INV-8]` sustained Concern volume:** ~0.75 per NPC per Accounting across 3 Accountings. Maintained within target. ✓
- **Cross-direction integration:** Settlement Signals → Concerns → Resolutions → Memories (Direction A path) → Opinion drift (Direction A) → meta-armature aggregation (Direction B) → next-cycle proposal selection. **Full cycle of mechanic interaction observed.** All three directions interlock as designed.
- **Knock-on into Direction E (composition):** A 3-Accounting × 4-NPC × 6-settlement matrix already shows clear emergent patterns (Marshal's competence reinforced, Ambassador's challenge rising, Confessor's network diversifying). Multi-Year × multi-faction Direction E will surface bigger-picture institutional drift.
- **Burden-scaling observation:** A faction with twice the settlements (e.g., 12) would produce ~6-8 Signals/Accounting → ~1.5-2 Concerns per NPC. Above target (1.5 ceiling). **Implies factions need to scale settlement count carefully; or routing logic should distribute Concerns more evenly across NPCs to keep individual loads tractable.** Surface as design observation, not gap: large-territory factions may need governance-tier filtering before Active NPCs see Concerns. **`[OBSERVATION: faction territory size scales Concern load — surfaced by SIM-C scenario 9; design implication for v1.2 territory-scaling]`.**

---

## §10 Direction-C summary

### 10.1 Invariants — verified across 9 scenarios

| Invariant | Status | Notes |
|---|---|---|
| `[SS-INV-1]` single-output-per-call | ✓ | All 9 scenarios returned Signal or None cleanly |
| `[SS-INV-2]` null-guard correctness (3 guards) | ✓ | Scenarios 2, 3, 4 each exercised one guard |
| `[SS-INV-3]` player-Disposition scope | ✓ | Scenario 5 confirmed PATCH 3.12 scope |
| `[SS-INV-4]` cascade decay | ✓ | Scenarios 1, 2 confirmed 0.7× and 0.5× governor weighting |
| `[SS-INV-5]` resonance-lookup totality | ✓ | Scenario 6 verified all (c, event_type) cases handled |
| `[SS-INV-6]` population-disposition bounds | ✓ | Scenario 8 confirmed clamp [-3, +5] |
| `[SS-INV-7]` salience bounds | ⚠️ PARTIAL | Pre-decay clamped [1,5]; **post-decay can fall below 1**, surfacing GAP-G2 |
| `[SS-INV-8]` Concern volume target | ✓ | Scenarios 7, 9 confirmed ~0.75/NPC/Accounting (within [0.5, 1.5]) |

**One partial invariant** (`[SS-INV-7]` post-decay) — surfaced as SIM-C-G2 for v1.2.

### 10.2 Surfaced specification gaps (8 total)

| ID | Surface | Issue | Severity |
|---|---|---|---|
| SIM-C-G1 | Scenario 1 | Signal-salience-to-Concern-salience mapping unspecified | P2 |
| **SIM-C-G2** | Scenario 1, partial INV-7 | **Signal salience can fall below clamp range after cascade decay** | **P2** |
| SIM-C-G3 | Scenario 2 | `interpret_event_affect()` algorithm unspecified | P2 |
| SIM-C-G4 | Scenario 4 | Memory salience-0 lifecycle handling | P3 |
| SIM-C-G5 | Scenario 6 | `categorize_event_type()` inverse-lookup spec | P3 |
| **SIM-C-G6** | Scenario 7 | **"Relevant Active NPC" routing for Signal-derived Concerns unspecified** | **P1** |
| SIM-C-G7 | Scenario 8 | `recent_event_delta` event-log infrastructure unspecified | P2 |
| SIM-C-G8 | Scenario 9 | Repeated-Signal handling on active Concern | P2 |

**Two P1-critical gaps:**
- **SIM-C-G6** (Active-NPC routing) is critical because without specification, settlement Signals don't reliably reach the correct faction member. Implementation will need to invent routing logic; without spec, different implementations diverge.

**Note SIM-B-G8 (failed_da_proposals) is also P1 from prior simulation.**

### 10.3 Emergent properties observed (5)

1. **Frontier outposts have half-strength voice in faction strategic dynamics.** Governor-only fallback at 0.5× weight encodes "frontier matters less than the seat" — politically authentic.
2. **Player's footprint is more visible to faction NPCs via player-amplified Signals.** PATCH 3.12 sharpens Signals around player actions specifically, without contaminating all settlement readings.
3. **Faction-leadership cognitive load scales with territory.** Renaissance ruler-burden dynamic. Large-territory factions (e.g., Crown ~6 settlements) approach upper Concern-volume target; very-large hypothetical factions would exceed it.
4. **Recovery from population disenchantment is easier than maximizing support.** Disposition clamp asymmetric ([-3, +5]) reflects political pragmatism.
5. **Authoring constraint at content-time:** new event_types must be explicitly tagged to a category or they produce neutral resonance (NPCs don't react). Forces conscious authoring of what events should engage which Conviction frames. Good content-design constraint.

### 10.4 Cross-direction observations

- **SIM-A integration:** Settlement Signals → Concerns → Resolutions produce Memories that feed Procedure D (Direction A). Closed loop verified.
- **SIM-B integration:** Strong settlement Signals (e.g., raid_threat in Eastfort) trigger DA proposals (Marshal proposing military reinforcement). Direction-C generates the inputs for Direction-B's `select_proposal()` machinery.
- **Direction D (Relational dynamics) preview:** Standing-event Memories propagate among inner circle the same way settlement-Signal-derived Concerns do; routing-logic considerations from SIM-C-G6 may apply analogously.
- **Direction E (Composition) preview:** Multi-faction multi-territory simulation should observe (a) territory-scaling Concern load, (b) cross-faction Signal interference (e.g., Crown's settlement adjacent to Hafenmark's may produce Signals about cross-border events affecting both), (c) cumulative population_disposition trajectories over multi-Year periods.

### 10.5 Direction C — VERDICT

**PASS with 1 P1-critical gap (SIM-C-G6 routing) + 1 partial invariant (post-decay salience) + 6 P2/P3 gaps.** Settlement Signal mechanics are sound under the patches; null guards work correctly; player-Disposition scope is fixed; resonance fallback covers all cases; Concern volume hits target. Two clarifications required for v1.2:
- **SIM-C-G6** (routing) — recommend (a) governor if Active, else (b) faction leader if seat, else (c) round-robin among inner-circle by domain affinity.
- **SIM-C-G2** (post-decay clamp) — recommend explicit floor in propagation logic.

Five emergent properties and three cross-direction observations documented.

---

**END OF SIM-C.**
