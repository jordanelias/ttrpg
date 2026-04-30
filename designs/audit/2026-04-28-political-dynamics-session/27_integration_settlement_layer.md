<!-- [PROVISIONAL: 2026-04-29 — integration patch: doc 12 v1.2.1 ↔ settlement_layer_v30] -->
<!-- STATUS: PROVISIONAL — integration patch document; no spec edits applied -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/27_integration_settlement_layer.md -->

# Integration Patch — doc 12 v1.2.1 ↔ `designs/territory/settlement_layer_v30.md`

**Purpose.** Document points of contact between political dynamics system v1.2.1 and canonical Settlement Layer Specification (settlement_layer_v30, status: CANONICAL approved 2026-04-17).

**Status.** PROVISIONAL — surveys integration touch-points; no spec edits applied.

---

## §1 OVERLAP MAP

doc 12's settlement-related mechanics (Settlement Signals, population_disposition, governance) interact with settlement_layer_v30's foundational settlement structures.

| doc 12 mechanic | settlement_layer_v30 counterpart | Relationship |
|---|---|---|
| §5.1 Settlement Meta-Armature | §1.3 Settlement Stats (Prosperity/Defense/Order) | **EXTENDING** — doc 12 builds on stats |
| §5.2 Settlement Signal flow | §4.3 Settlement Events | **OVERLAPPING** — both produce settlement-derived political effects |
| §5.2 Concern routing (PATCH v1.2-2) — `settlement.governor` | §3.1 Two-Tier Authority Model (Governor slot) | **REINFORCING** — doc 12 uses canonical Governor structure |
| §5.2 routing Tier 2 — "seat settlement" | §1.2 Settlement Types / §2.1 Settlement Registry (seat-of-province) | **OVERLAPPING** — seat designation must agree |
| §3.9 / PATCH 3.9 `population_disposition` | §1.3 Order stat + §4.3 Settlement Events | **EXTENDING** — population_disposition is a derived per-faction value |
| §5.2 routing Tier 1 — `settlement.governor.is_active_npc()` | §3.2 Governor Assignment (Officer NPC, subnational faction, or vacant) | **CRITICAL** — must determine NPC-vs-not |

---

## §2 KEY POINTS OF CONTACT

### 2.1 Settlement stats vs Population Disposition

**settlement_layer_v30 §1.3** specifies three settlement stats (Prosperity/Defense/Order, 0-5 scale) producing derived values (Local Economy, Garrison Strength, Public Order).

**doc 12 v1.2.1 §3.9 PATCH 3.9** specifies `population_disposition[settlement, faction]` as a per-faction derived value:
```
population_disposition = clamp(
    0.4 × normalized_order + 0.4 × normalized_prosperity + 0.2 × recent_event_delta,
    -3, +5
)
```

Where `normalized_order = (settlement.order - 5) / 2.5` and `normalized_prosperity = (settlement.prosperity - 5) / 2.5`.

**Conflict — order scale.** doc 12 implicitly assumes Order is on a 0-10 scale (midpoint 5 → 0; max 10 → +2). settlement_layer_v30 §1.3 says Order is 0-5 scale.

**Resolution:** doc 12's normalization is wrong for settlement_layer_v30's actual 0-5 scale. Should be `normalized_order = (settlement.order - 2.5) / 1.25` to map [0, 5] → [-2, +2].

**INTEGRATION-PATCH-3.1 (CRITICAL — recommended):** doc 12 §3.9 PATCH 3.9 — fix normalization for actual settlement-stat scale:

```
normalized_order = (settlement.order - 2.5) / 1.25  # maps [0,5] → [-2, +2]
normalized_prosperity = (settlement.prosperity - 2.5) / 1.25  # maps [0,5] → [-2, +2]
```

**This is a real bug in doc 12's PATCH 3.9.** The simulation chain didn't catch it because SIM-C used illustrative values (settlement.order = 7 in scenario 8 — incompatible with settlement_layer_v30's 0-5 scale). **Recommend fix in v1.2.2.**

### 2.2 Governor field semantics

**doc 12 v1.2.1 §5.2 PATCH v1.2-2** routing Tier 1: `if settlement.governor and settlement.governor.is_active_npc(): return settlement.governor`.

**settlement_layer_v30 §3.2** specifies Governor Assignment: Governor can be (a) Player character, (b) Officer NPC, (c) Subnational faction, or (d) Vacant.

**Issue:** doc 12 assumes `settlement.governor` is a single NPC. settlement_layer_v30 has three governor types plus vacant. Routing Tier 1 only handles type (b) Officer NPC.

**Resolution:** Extend routing logic to handle all governor types:
- Player character governor → Player IS Active NPC (S5+); routing returns Player.
- Officer NPC → existing Tier 1.
- Subnational faction → not a single NPC; route to faction's leader.
- Vacant → fall through to Tier 2.

**INTEGRATION-PATCH-3.2 (recommended):** doc 12 §5.2 PATCH v1.2-2 — extend Tier 1:

```
function route_signal_to_concern(signal, settlement, faction):
    # Tier 1 — settlement governor (handle all governor types per settlement_layer_v30 §3.2)
    if settlement.governor:
        if settlement.governor.type == "player_character":
            return settlement.governor  # Player at S5+ receives Concerns
        elif settlement.governor.type == "officer_npc" and settlement.governor.is_active_npc():
            return settlement.governor
        elif settlement.governor.type == "subnational_faction":
            return settlement.governor.leader  # subnational faction's leader
        # type "vacant" or non-Active officer → fall through to Tier 2

    # Tier 2 — faction leader if seat settlement
    ...
```

### 2.3 Seat settlement designation

**doc 12 v1.2.1 §5.2 PATCH v1.2-2** routing Tier 2: `if settlement == faction.seat_settlement: return faction.leader`.

**settlement_layer_v30 §1.2** specifies Settlement Types and §2.1 Settlement Registry — but I don't see explicit "seat" designation in the heading list.

**Resolution:** Need to verify that `faction.seat_settlement` is a defined attribute in settlement_layer_v30 or must be added.

**INTEGRATION-PATCH-3.3 (recommended):** Cross-check:
- If settlement_layer_v30 specifies seat-of-faction in §2.1 Settlement Registry: doc 12 references the canonical attribute. ✓
- If not explicitly specified: settlement_layer_v30 should add `faction.seat_settlement` as derived attribute (e.g., the settlement of type "Capital" or "Provincial Seat" controlled by the faction).

**Action:** Read settlement_layer_v30 §2.1 in detail; confirm seat designation; add cross-reference in doc 12 §5.2 noting the source of `faction.seat_settlement`.

### 2.4 Settlement Events ↔ Settlement Signals

**settlement_layer_v30 §4.3** specifies Settlement Events: 0-1 local events per season based on settlement stats:
- Prosperity 0 → Famine, Order −1 automatic.
- Defense 0 + adjacent hostile military → Raid/siege.
- Order 0 → Local revolt.
- Order 5 + Prosperity 4+ → Flourishing event.
- (More from §4.3 table.)

These are *engine-generated events* that feed into the Scene Slate at Priority 4 (Territorial).

**doc 12 v1.2.1 §5.2** specifies Settlement Signals as derived from NPC Memories (`compute_settlement_signal`).

**Substantively complementary, not conflicting:**
- settlement_layer_v30 §4.3 = events generated *from settlement stat conditions*.
- doc 12 §5.2 = Signal aggregated *from NPC Memories about events*.

The relationship: settlement_layer_v30 §4.3 events are *inputs* to NPC Memory generation (via Event Impact Matrix); those Memories are then aggregated into doc 12's Settlement Signal.

**INTEGRATION-PATCH-3.4 (recommended):** doc 12 §5.2 — add cross-reference: *"Settlement-stat-derived events (per `settlement_layer_v30.md` §4.3 — Famine, Raid, Local Revolt, Flourishing, etc.) are processed through standard Event Impact Matrix to generate NPC Memories. Those Memories then contribute to `compute_settlement_signal()` aggregation per this section. The two specs are complementary: settlement_layer_v30 specifies what events fire from settlement-stat conditions; doc 12 specifies how those events propagate through Passive NPCs as a faction-political Signal."*

### 2.5 Provincial Authority vs Settlement Governor

**settlement_layer_v30 §3.1** specifies Two-Tier Authority Model: Provincial Authority (national-level faction) vs Settlement Governor (officer/faction managing settlement).

**doc 12 v1.2.1** uses `controlling_faction` and `governor` — implicit two-tier mapping but not explicit.

**INTEGRATION-PATCH-3.5 (recommended):** doc 12 §5.1 / §5.2 — add explicit cross-reference: *"`settlement.controlling_faction` corresponds to settlement_layer_v30 §3.1 'Provincial Authority' (national-level). `settlement.governor` corresponds to settlement_layer_v30 §3.1 'Settlement Governor' (local-level). The two may agree or disagree; per settlement_layer_v30 §3.1, when they disagree, governance tension generates gameplay (which doc 12 surfaces as Concerns and Settlement Signals)."*

### 2.6 Subnational faction Concern routing

**settlement_layer_v30 §3.3** specifies Subnational Faction Governance — settlements can be governed by *subnational factions* (e.g., a guild, a church wing, a local Restoration Movement chapter).

**doc 12 v1.2.1** doesn't explicitly model subnational factions in routing — its Concern routing assumes a single Active NPC governor or escalates to faction leader.

**Resolution:** When governor is a subnational faction (per settlement_layer_v30 §3.3), routing should send Concern to that subnational faction's leadership chain, not skip to the *national* faction leader.

**INTEGRATION-PATCH-3.6 (recommended):** doc 12 §5.2 PATCH v1.2-2 — extend routing logic to handle subnational-faction governors. (This was already partially addressed in INT-3.2's Tier 1 extension; INT-3.6 is the explicit cross-reference to settlement_layer_v30 §3.3 as the source of the subnational faction structure.)

---

## §3 NEW MECHANIC: doc 12 → settlement_layer_v30

doc 12 v1.2.1 introduces population_disposition (per-faction settlement-population sentiment). This is a NEW concept not in settlement_layer_v30.

**INTEGRATION-PATCH-3.7 (recommended):** settlement_layer_v30 — add reference in §1.3 Settlement Stats (or new subsection): *"The political dynamics system (`12_development_specification.md` §3.9 / PATCH 3.9) introduces a per-faction `population_disposition[settlement, faction]` derived value separate from Order. Order tracks institutional governance stability; population_disposition tracks settlement-population sentiment toward each faction. These are computed independently; both contribute to settlement-political behavior."*

This is a meaningful spec extension to settlement_layer_v30 — recommend separate editorial commit with Jordan acknowledgment.

---

## §4 INTEGRATION-PATCH SUMMARY

Seven recommended integration patches. INT-3.1 is critical (fixes a real bug); others are cross-references and one extension.

| Patch ID | Type | Source | Action |
|---|---|---|---|
| **INT-3.1** | **Bug fix** | doc 12 §3.9 PATCH 3.9 | **Fix order/prosperity normalization for 0-5 scale** |
| INT-3.2 | Mechanic extension | doc 12 §5.2 PATCH v1.2-2 | Extend Tier-1 routing for all governor types |
| INT-3.3 | Cross-reference verify | doc 12 §5.2 + settlement_layer §2.1 | Confirm `faction.seat_settlement` defined |
| INT-3.4 | Cross-reference | doc 12 §5.2 | Identify settlement-events ↔ Signals relationship |
| INT-3.5 | Cross-reference | doc 12 §5.1 / §5.2 | Map controlling_faction/governor ↔ Two-Tier Authority |
| INT-3.6 | Mechanic clarification | doc 12 §5.2 | Subnational-faction Concern routing (subset of INT-3.2) |
| INT-3.7 | Spec extension | settlement_layer_v30 | Reference doc 12's population_disposition |

INT-3.1 is critical and should be applied to v1.2.2. The simulation chain used illustrative settlement.order = 7 values that aren't valid under settlement_layer_v30's 0-5 scale.

Estimated total spec-edit time: ~45 minutes (most is INT-3.1 verification + downstream simulation re-check).

---

## §5 RECOMMENDED PLAN

For canonical promotion of doc 12 v1.2.1:

1. **Apply INT-3.1 immediately** — bug fix in doc 12 §3.9. Verify against SIM-C scenarios (the illustrative settlement.order values used in SIM-C scenarios 1, 8 may need adjustment in those simulation docs to use 0-5 range; though those are audit-history docs and the recalibrated math doesn't change the verification conclusions). Single editorial commit.
2. **Apply INT-3.2, 3.4, 3.5, 3.6** (doc 12-side cross-references and routing extensions) — single editorial commit.
3. **Verify INT-3.3** by inspecting settlement_layer_v30 §2.1; either confirm seat-settlement attribute exists or document the addition.
4. **Apply INT-3.7** (settlement_layer_v30 reference to population_disposition) — separate editorial commit; requires Jordan acknowledgment for canonical-doc edit.

After INT-3.1 through INT-3.7: doc 12 ↔ settlement_layer_v30 integration is complete and §13 Item 5 (settlement_layer portion) is satisfied.

---

**END OF SETTLEMENT LAYER INTEGRATION PATCH.**

---

## §6 CROSS-INTEGRATION SUMMARY (across docs 25, 26, 27)

| Integration target | # patches | Critical findings |
|---|---|---|
| npc_behavior_v30 (doc 25) | 6 | INT-1.6 explicit_heir Tier-0; otherwise documentation cross-refs |
| player_agency_v30 (doc 26) | 7 | INT-2.7 Knot rupture mandatory addition; otherwise documentation cross-refs |
| settlement_layer_v30 (doc 27) | 7 | **INT-3.1 normalization bug fix (P1-CRITICAL)** |

**Total: 20 integration patches across 3 external designs.**

**One critical finding:** INT-3.1 (population_disposition normalization for 0-5 scale) is a real bug in doc 12 v1.2.1 PATCH 3.9. The simulation chain did not catch it because illustrative test values were on a 0-10 scale instead of the canonical 0-5 scale. Recommend immediate fix in v1.2.2.

**Next step recommendation:** Apply INT-3.1 fix as v1.2.2 (single-patch revision); apply remaining 19 documentation/extension patches as canonical-promotion editorial work.
