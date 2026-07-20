<!-- [PROVISIONAL: 2026-04-29 — integration patch: doc 12 v1.2.1 ↔ npc_behavior_v30] -->
<!-- STATUS: PROVISIONAL — integration patch document; no spec edits applied to either source -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/25_integration_npc_behavior.md -->

# Integration Patch — doc 12 v1.2.1 ↔ `designs/npcs/npc_behavior_v30.md`

**Purpose.** Document points of contact between political dynamics system v1.2.1 (doc 12) and canonical NPC Ethical Stance and Resonance Behavior System (npc_behavior_v30, status: CANONICAL approved 2026-04-17).

**Status.** PROVISIONAL — surveys integration touch-points, identifies overlaps and conflicts, recommends resolution paths. No spec edits applied to either source by this document; recommendations require Jordan adoption.

**Method.** Spot-survey of npc_behavior_v30 sections that interact with doc 12 mechanics; identify overlap, complement, and conflict patterns; tabulate recommended integration patches.

---

## §1 OVERLAP MAP

doc 12 v1.2.1 introduces several mechanics that intersect with npc_behavior_v30's existing structures:

| doc 12 mechanic | npc_behavior_v30 counterpart | Relationship |
|---|---|---|
| §2 NPC data structures (Mood, Concerns, Memories, Opinions, Beliefs, Convictions, Standing) | §1 Stance Triangle (Conviction, Resonant Style, Mastery Style); §2 Named NPC Stance Triangles | **OVERLAPPING** — both systems define NPC inner state |
| §2.5.2 Knot Rupture | §3 Beliefs / §3.4 Thread Operation → Conviction Scar Triggers | **COMPLEMENTARY** — Knot rupture extends Scar mechanics |
| §3 Armature (Conviction interpretation) | §1.1 Stance Triangle / §1.2 Conviction Taxonomy | **OVERLAPPING** — both encode Conviction |
| §5.3 Faction Meta-Armature | §2.15 Crown Inner Circle / §2.16-17 Hafenmark/Varfell ICs (named-NPC tables) | **COMPLEMENTARY** — meta-armature aggregates over named NPCs |
| §5.4.1 Faction Succession (PATCH v1.2-19) | §2 Named NPC roster (e.g., §2.8 Prince Torben Almqvist as Crown heir) | **OVERLAPPING** — succession candidate logic must reference roster |
| §6.2 Procedure D Opinion Drift | §3.2 Belief Revision | **PARALLEL** — both produce inner-state change but operate on different data structures |
| §8.1 Standing Recalc | (no direct counterpart) | **NEW MECHANIC** — extends NPC system |

---

## §2 KEY POINTS OF CONTACT (substantive integration questions)

### 2.1 Conviction representation

**npc_behavior_v30 §1.2** lists 7 Convictions: `{Authority, Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity}` (the existing canonical 7-Conviction taxonomy).

**doc 12 v1.2.1** uses 7 Convictions: `{Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity}`.

**Apparent conflict — Authority.** npc_behavior_v30 includes "Authority" as a Conviction; doc 12 does not.

**Resolution path:** This is likely a v1.2.1-side concern. doc 12's Conviction list excludes Authority because Authority is encoded *implicitly* through Standing/leader-flag (institutional position) rather than as a Conviction stance. But npc_behavior_v30 explicitly includes Authority in §1.2 — and the named NPCs in §2.15 use it (e.g., Wilhelm Voss has "Mastery Style: Authority" — wait, that's Mastery Style not Conviction).

Re-reading §2.15: the column "Conviction" lists Order/Precedent/Autonomy/Faith — same 7 minus Authority. The "MS" column is Mastery Style, listing Authority/Evidence/Consequence — a different axis.

**Conclusion:** doc 12's 7-Conviction taxonomy *matches* npc_behavior_v30 §1.2 once "Authority" is recognized as a Mastery Style axis, not a Conviction. **No conflict.** Recommend: doc 12 §3 Armature should explicitly cross-reference npc_behavior_v30 §1.1 Stance Triangle to clarify the relationship.

**INTEGRATION-PATCH-1.1 (recommended for v1.2.2 or canonical-promotion edit):** doc 12 §3 Armature header — add cross-reference: *"Convictions in this doc correspond to those in `npc_behavior_v30.md` §1.2 (Conviction Taxonomy). Mastery Style and Resonant Style — also defined in npc_behavior_v30 — are orthogonal axes not directly modeled in doc 12's Armature, but are consumed by `interpret_event_affect()` and Armature interpretation when authoring scenes."*

### 2.2 Belief Revision mechanics

**npc_behavior_v30 §3.2** specifies Belief Revision as: "An NPC revises a Belief when ALL of the following hold: (1) A Contest produces decisive outcome (Conviction Track ≥ 7 or ≤ 3) against the NPC; (2) The winning argument used the NPC's primary or secondary Resonant Style."

**doc 12 v1.2.1** specifies Belief Revision in two paths:
- Path A (Total Victory Social Contest): Belief revises on decisive outcome.
- Path B: 2 contradicting Memories at salience ≥ 3 (existing spec).

**Substantive question:** Does Path B in doc 12 conflict with npc_behavior_v30 §3.2's "Contest required" rule?

**Resolution path:** doc 12 Path B is a *novel mechanic* — accumulated-Memory-driven Belief revision without an explicit Contest. This is consistent with the political dynamics system's broader pattern (drift via accumulated Memory) but extends npc_behavior_v30's contest-only model. 

**INTEGRATION-PATCH-1.2 (recommended):** Either:
- (a) Update npc_behavior_v30 §3.2 to add: *"Path B accumulated-Memory revision per `12_development_specification.md` §6.2 Procedure D — 2+ contradicting Memories at salience ≥ 3 produce Belief revision without a Contest. Resonant Style requirement does not apply to Path B (Memory accumulation is style-agnostic)."*
- (b) Update doc 12 §6.2 Procedure D to defer to npc_behavior_v30 §3.2 — i.e., Path B requires *one* of the contradicting Memories to come from a Contest event. **Less elegant** because it requires Path B to inherit Path A's structural constraint.

**Recommendation: option (a)** — extend npc_behavior_v30 §3.2 to acknowledge Path B as an additional revision path. doc 12 v1.2.1 already operates with Path B; npc_behavior_v30 should reflect this.

### 2.3 Scar accumulation

**npc_behavior_v30 §3.3** defines a Scar table: 0 → 1 → 2 → 3+ Scars produce escalating Conviction effects (secondary activation, primary shift, full crisis). Crisis table specifies dice rolls for unpredictable behavior.

**doc 12 v1.2.1** uses Scars in Standing recalc (`-0.5 × public_conviction_scars_this_year`) but doesn't model the Scar-accumulation effects on behavior — those remain in npc_behavior_v30.

**No conflict.** doc 12 references Scars; npc_behavior_v30 specifies their per-NPC behavioral effects. Integration is clean.

**INTEGRATION-PATCH-1.3 (minor cross-reference):** doc 12 §8.1 PATCH 3.11 / Standing recalc — add inline note: *"`public_conviction_scars_this_year` follows the Scar accumulation framework in `npc_behavior_v30.md` §3.3; Scars from this Year contribute to Standing recalc; cumulative Scar effects on behavior (secondary Conviction activation, etc.) are governed by npc_behavior_v30 §3.3."*

### 2.4 Crown Inner Circle (named NPCs)

**npc_behavior_v30 §2.15** specifies Crown Inner Circle by name with explicit Conviction/Mastery Style/Certainty stats:
- Wilhelm Voss (Royal Marshal, Order/Authority/4)
- Annalie Reichard (Lord Treasurer, Precedent/Evidence/5)
- Kolbrun Thale (Spymaster, Autonomy/Consequence/3)
- Father Gustav Linder (Archbishop's Rep, Faith/Authority/5)
- Theodor Kreutz (Royal Guard Captain, Order/Authority/4)

**doc 12 v1.2.1** uses generic NPC names in simulation (Almud as "Crown leader," Marshal as Order primary, etc.). **These are not the same NPCs as the canonical roster.**

**Significant integration question:** Does the simulation chain's modeling reflect the canonical Crown Inner Circle, or does it use abstracted placeholders?

**Reading the simulations:** SIM-A through SIM-H use NPC names like "Almud" (matching King Almud Almqvist), "Marshal" (matching Wilhelm Voss role), "Confessor" (the Faith voice), etc. The simulation NPCs roughly map to canonical roles but not by exact identity. **The simulations validated mechanics, not specific NPC behaviors.**

**INTEGRATION-PATCH-1.4 (significant — recommended):** doc 12 §0 (intro) or §2 — add cross-reference: *"For specific Named NPC instances, refer to `npc_behavior_v30.md` §2 Named NPC Stance Triangles. The simulation chain (SIM-A through SIM-H) used role-typed placeholder NPCs (Almud, Marshal, Confessor, Reformer); these correspond to canonical Crown Inner Circle (King Almud Almqvist, Wilhelm Voss, Father Gustav Linder, etc.) per npc_behavior_v30 §2.15. Implementation should bind doc 12 mechanics to canonical named NPCs at engine-init time."*

### 2.5 Decision derivation

**npc_behavior_v30 §4.1** specifies Decision Procedure for Named NPCs (16 lines of dense logic — primary Conviction, Resonant Style, Mastery Style, Stance check ordering).

**doc 12 v1.2.1** specifies Procedures B/C/D/E for Concern generation, project advancement, opinion drift, gossip propagation.

**Are these the same Procedure?** NO — they operate at different scales:
- npc_behavior_v30 §4.1 = per-NPC per-decision (single decision point, e.g., "how does Wilhelm Voss respond to this contested ruling?")
- doc 12 §6.2 = per-Accounting batched processing for the whole NPC roster

**No conflict.** doc 12's Procedures are higher-level batched logic; npc_behavior_v30 §4.1 is the per-decision logic invoked *by* doc 12 mechanics (e.g., when Procedure B generates a Concern that requires the NPC to make a contested decision, that contest invokes npc_behavior_v30's Decision Procedure).

**INTEGRATION-PATCH-1.5 (recommended):** doc 12 §6.2 — add cross-reference at top: *"Per-NPC contest-resolution logic (when Procedure B/C/D triggers a decision point requiring Conviction/Resonant-Style/Mastery-Style adjudication) defers to `npc_behavior_v30.md` §4.1 Decision Procedure for Named NPCs. doc 12 Procedures handle batched per-Accounting state evolution; npc_behavior_v30 §4.1 handles per-decision adjudication."*

### 2.6 Faction Succession (PATCH v1.2-19) ↔ Named-NPC roster

**doc 12 v1.2.1 §5.4.1** specifies `designate_new_leader(faction)` — selects highest-Standing same-faction Active NPC; tie-break by Conviction-alignment.

**npc_behavior_v30 §2.8** specifies Prince Torben Almqvist as Crown heir explicitly. The canonical roster has a *named* succession candidate.

**Conflict:** doc 12's algorithmic selection might not produce Prince Torben as successor if his Standing isn't highest at succession-trigger time. The canonical narrative expects Torben to inherit; doc 12's algorithm doesn't guarantee this.

**Resolution path:** Two options:
- (a) doc 12's algorithmic selection is the authoritative mechanism; canonical roster's "heir" designation is descriptive intent that the algorithm should validate (i.e., Torben should be designed to have highest Standing among non-leader inner circle when succession fires).
- (b) Add an "explicit_heir" field per faction; doc 12's `designate_new_leader` checks `explicit_heir` first before falling to algorithmic selection.

**Recommendation: option (b)** — explicit-heir override. Renaissance political reality includes designated heirs; the engine should respect designation when content authoring specifies it.

**INTEGRATION-PATCH-1.6 (recommended):** doc 12 §5.4.1 — modify `designate_new_leader()`:

```
function designate_new_leader(faction):
    # Tier 0 — explicit heir designation (PATCH-INT-1.6 / npc_behavior_v30 §2.8 cross-ref)
    if faction.explicit_heir and faction.explicit_heir.is_active() and faction.explicit_heir in faction.inner_circle:
        return faction.explicit_heir
    
    # Tier 1 — highest-Standing same-faction Active NPC (existing logic)
    ...
```

`faction.explicit_heir` is content-authored (per npc_behavior_v30 named-roster designation); algorithmic fallback applies when no heir designated or designated heir unavailable.

---

## §3 NON-INTEGRATION ITEMS

These doc 12 mechanics have **no counterpart** in npc_behavior_v30 and require no cross-reference:

- §5.2 Settlement Signal flow (operates at settlement layer, not NPC layer).
- §6.2 Procedure E Off-Screen Interactions (gossip mechanic — novel).
- §7.6 NPC Outreach Generation (Scene Slate input — see player_agency_v30 integration patch separately).
- §8.1 NPC Standing Recalculation (novel mechanic).

---

## §4 INTEGRATION-PATCH SUMMARY

Six recommended integration patches. None require simulation re-validation (changes are documentation/cross-reference, not mechanic alteration). Estimated total spec-edit time: ~30 minutes.

| Patch ID | Type | Source | Action |
|---|---|---|---|
| INT-1.1 | Cross-reference | doc 12 §3 | Add Conviction taxonomy cross-ref to npc_behavior_v30 §1.2 |
| INT-1.2 | Spec extension | npc_behavior_v30 §3.2 | Add Path B (Memory-accumulation Belief revision) |
| INT-1.3 | Cross-reference | doc 12 §8.1 | Add Scar framework reference to npc_behavior_v30 §3.3 |
| INT-1.4 | Cross-reference | doc 12 §0 or §2 | Add Named-NPC roster reference to npc_behavior_v30 §2 |
| INT-1.5 | Cross-reference | doc 12 §6.2 | Add Decision Procedure reference to npc_behavior_v30 §4.1 |
| INT-1.6 | Mechanic update | doc 12 §5.4.1 | Add `explicit_heir` Tier-0 to `designate_new_leader()` |

INT-1.2 and INT-1.6 are mechanic-affecting (extend behavior); the others are documentation cross-references. All are forward-compatible with existing canonical content.

---

## §5 RECOMMENDED INTEGRATION-PATCH PLAN

For canonical promotion of doc 12 v1.2.1:

1. **Adopt INT-1.1, 1.3, 1.4, 1.5** (cross-references) — single editorial commit; ~10 minutes.
2. **Adopt INT-1.6** (`explicit_heir` Tier-0) — single editorial commit; ~5 minutes for spec edit + brief simulation re-check (doc 12 v1.2.1 §5.4.1 still operates correctly because Tier-0 falls through to Tier-1 when no heir is set).
3. **Adopt INT-1.2** (npc_behavior_v30 Path B addition) — requires editing canonical npc_behavior_v30; recommend separate editorial session with explicit Jordan acknowledgment that v1.2.1's Path B is being canonicalized into npc_behavior_v30.

After INT-1.1 through INT-1.6: doc 12 ↔ npc_behavior_v30 integration is complete and §13 Item 5 (npc_behavior integration patches) is satisfied.

---

**END OF NPC BEHAVIOR INTEGRATION PATCH.**
