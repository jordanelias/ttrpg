<!-- [PROVISIONAL: 2026-04-29 — integration patch: doc 12 v1.2.1 ↔ player_agency_v30] -->
<!-- STATUS: PROVISIONAL — integration patch document; no spec edits applied -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/26_integration_player_agency.md -->

# Integration Patch — doc 12 v1.2.1 ↔ `designs/architecture/player_agency_v30.md`

**Purpose.** Document points of contact between political dynamics system v1.2.1 and canonical Player Agency System (player_agency_v30, status: CANONICAL approved 2026-04-17).

**Status.** PROVISIONAL — surveys integration touch-points; no spec edits applied.

---

## §1 OVERLAP MAP

doc 12's player-facing surfaces directly extend player_agency_v30's core constructs. **This is the heaviest-overlap integration of the three.**

| doc 12 mechanic | player_agency_v30 counterpart | Relationship |
|---|---|---|
| §7.6 NPC Outreach Generation (P3 default + escalation) | §4 Scene Slate (slate generation, priority ordering) | **EXTENDING** — Outreach scenes feed the Slate |
| §2.5.2 Knot Rupture | §4.2 Generation Algorithm Step 1 mandatory triggers ("Knot Partner in Crisis") | **OVERLAPPING** — both reference Knot crisis |
| §1.1 N-DIAG-A Inner-Circle Threshold Milestone | §4.2 Step 1 mandatory triggers (rank advancement) | **OVERLAPPING** — milestone scenes are Slate entries |
| §6.2 Procedure E (Off-Screen Interactions / gossip) | §4.5 Opportunities Not Pursued (NPC AI advances state) | **PARALLEL** — both handle off-screen NPC behavior |
| §8.1 Standing Recalc | §5 Stature Progression / §5.2 Leadership Acquisition | **CONNECTED** — doc 12 Standing maps to Agency Stature |
| §6.2 Procedure D Opinion Drift | §6.2 Modifiers (Knot scene-action bonus) | **REINFORCING** — Opinion shifts feed Knot strength |
| §5.4 Faction Crisis state | §4.2 Step 1 mandatory triggers ("Stability Crisis") | **OVERLAPPING** — Crisis triggers Mandatory scene |

---

## §2 KEY POINTS OF CONTACT

### 2.1 Scene Slate priority alignment

**player_agency_v30 §4.2 Step 1** specifies mandatory scenes (Priority 0):
- Player in Accord 0 territory (Revolt)
- Player target of Heresy Investigation
- Mass battle in territory
- Faction leader assassinated/overthrown/incapacitated

**doc 12 v1.2.1 §7.6 PATCH 3.10** specifies Outreach priorities:
- P3 default (available, skippable)
- P2 mandatory (escalation at salience-5/ttl-1, Knot via PATCH 3.6)
- P2 mandatory does NOT match P0 in player_agency_v30's priority taxonomy.

**Apparent conflict — priority numbering.** player_agency_v30 uses Priority 0 (Mandatory Crisis), Priority 1 (next-tier), etc. doc 12 uses Priority 2 (mandatory) and Priority 3 (available).

**Resolution:** These are different priority *systems*:
- player_agency_v30 numbers from 0 (highest urgency).
- doc 12 §7.6 PATCH 3.10 numbers from 1 (treating P3 as "available" not as "low priority").

**Recommendation:** Standardize. Two options:
- (a) doc 12 renumbers: P3 → P5 (available); P2 → P1 (mandatory). Aligns with player_agency_v30's hierarchical numbering.
- (b) player_agency_v30 absorbs doc 12's relative-numbering as a different layer. doc 12's "P2 mandatory Outreach" is a player_agency_v30 "Priority 1" entry (one tier below Priority 0 mandatory crises).

**Recommendation: option (b)** — fewer doc edits; both numbering systems coexist. Mapping table:

| doc 12 priority | player_agency_v30 Slate priority | Meaning |
|---|---|---|
| (none) | Priority 0 | Mandatory Crisis (faction-level) |
| Priority 2 (Outreach mandatory) | Priority 1 | Mandatory inner-circle relational |
| Priority 3 (Outreach default) | Priority 4 (Territorial) or Priority 5 (Personal) | Available scenes |

**INTEGRATION-PATCH-2.1 (recommended):** doc 12 §7.6 PATCH 3.10 — add note: *"doc 12's Priority 2/3 Outreach numbering is local to Outreach generation. When Outreach scenes appear in the Scene Slate (per `player_agency_v30.md` §4 Scene Slate), they map to Slate priority levels:"* (then the table above).

### 2.2 Knot mandatory P2 ↔ player_agency_v30 §4.2 Step 1 mandatory

**doc 12 v1.2.1 §7.6 PATCH 3.6** says Knot Outreach is P2 mandatory when Knot partner has Concern at salience ≥ 2.

**player_agency_v30 §4.2 Step 1** mandatory triggers include "Knot Partner in Crisis" (single trigger condition).

**Apparent conflict — frequency.** doc 12 PATCH 3.6 fires at salience ≥ 2 (relatively low threshold); player_agency_v30 fires at "Crisis" (higher threshold). doc 12 fires more often.

**Resolution:** These are *different scenes*:
- doc 12 PATCH 3.6 generates *routine* Knot Outreach (regular relational maintenance).
- player_agency_v30 §4.2 Step 1 "Knot Partner in Crisis" is a *pivotal moment* (e.g., Spouse falsely accused of treason, or imprisoned).

**INTEGRATION-PATCH-2.2 (recommended):** Both specs — clarify the distinction. doc 12 §7.6 PATCH 3.6 should add: *"Routine Knot Outreach (this PATCH) is distinct from `player_agency_v30.md` §4.2 Step 1 'Knot Partner in Crisis' mandatory trigger; the latter fires for severe single-event arc-fork moments (imprisonment, mortal injury, overt betrayal). Routine Knot Outreach handles ongoing relational maintenance; Crisis triggers handle dramatic peaks."*

Similarly, player_agency_v30 §4.2 Step 1 should reference doc 12's PATCH 3.6 as the routine-Knot-engagement mechanism.

### 2.3 Standing ↔ Stature

**player_agency_v30 §5.1** specifies Stature Levels: Petitioner (S0), Protégé (S1), Member (S2), Confidante (S3), Lieutenant (S4), Senior (S5), Inner Circle (S6), Regent-Designate (S7).

**doc 12 v1.2.1 §8.1** specifies Standing range [3, 7]. doc 12's "Standing 4" is player_agency's "Lieutenant"; "Standing 5" is "Senior"; "Standing 6" is "Inner Circle"; "Standing 7" is "Regent-Designate."

**Subtle conflict — terminology.** doc 12 says "Inner Circle" includes Standing 4+. player_agency_v30 §5.1 calls Standing 6 "Inner Circle" specifically.

**Resolution:** doc 12 uses "inner circle" lowercase as a generic descriptor for high-Standing NPCs (S4+). player_agency_v30 §5.1 uses "Inner Circle" capitalized as a specific Stature label (S6).

**INTEGRATION-PATCH-2.3 (recommended):** doc 12 §8.1 / §5.3 / §1.1 — replace lowercase "inner circle" with "high-Standing peers" or "S4+ inner-circle-eligible" to disambiguate from player_agency_v30's specific Stature label. Or, alternatively, doc 12 should consistently use "inner circle" lowercase to mean S4+ (the existing pattern) and player_agency_v30 should use "Inner Circle" capitalized for S6 specifically (the existing pattern). **This is mostly a typographical convention to maintain.**

### 2.4 Standing recalc ↔ Leadership Acquisition

**player_agency_v30 §5.2** specifies Leadership Acquisition: how a player advances through Stature levels. References Recognition Events, Standing 3 specialty branch selection at Formal Recognition Event, etc.

**doc 12 v1.2.1 §8.1** specifies Standing recalc at Year boundary based on per-Year counters.

**No conflict.** doc 12's Standing recalc applies to *NPC* Standing trajectories. player_agency_v30 §5.2's Leadership Acquisition applies to *Player* Stature trajectory. Different subjects.

**INTEGRATION-PATCH-2.4 (recommended):** doc 12 §8.1 — add inline note: *"This recalc applies to Active NPCs. Player Standing/Stature progression follows `player_agency_v30.md` §5 (Recognition Events, Acquisition criteria). Player Standing in this doc 12 framework can also be recalculated using the same formula at S5+ (when Player joins the Faction Meta-Armature aggregate per §5.3); however, Player Stature progression at S0-S4 follows player_agency_v30."*

### 2.5 Procedure E ↔ §4.5 Opportunities Not Pursued

**player_agency_v30 §4.5** specifies Opportunities Not Pursued — scenes the Player skipped advance via NPC AI / clock advancement.

**doc 12 v1.2.1 §6.2 Procedure E** specifies Off-Screen Interactions — gossip propagation among NPCs the Player isn't engaging with.

**Substantively complementary.** Both handle off-screen NPC behavior, but at different scales:
- player_agency_v30 §4.5 = scene-level (Player skipped this scene → NPC AI proceeds).
- doc 12 §6.2 Procedure E = inter-NPC level (NPCs interact with each other; gossip propagates).

**INTEGRATION-PATCH-2.5 (recommended):** doc 12 §6.2 Procedure E — add cross-reference: *"Procedure E handles inter-NPC interactions and gossip propagation. This complements `player_agency_v30.md` §4.5 Opportunities Not Pursued, which handles Scene-Slate-level player-skipped scenes. Procedure E executes at every Accounting; player_agency §4.5 executes per Scene Slate cycle."*

### 2.6 Faction Crisis state ↔ Stability Crisis mandatory trigger

**player_agency_v30 §4.2 Step 1** lists "Stability Crisis (faction-scale collapse; faction enters mandatory Crisis at all settlements)" as Priority 0 mandatory trigger.

**doc 12 v1.2.1 §5.4** specifies Faction Crisis state when ≥40% of inner circle is Distracted/Grieving.

**Same concept, different specifications.** player_agency_v30 references "Stability Crisis" as a state; doc 12 specifies the trigger threshold (40%).

**INTEGRATION-PATCH-2.6 (recommended):** Both specs — cross-reference. doc 12 §5.4 should add: *"This Faction Crisis state is the canonical 'Stability Crisis' referenced in `player_agency_v30.md` §4.2 Step 1; entering this state generates Priority 0 mandatory Slate entries for the Player."*

player_agency_v30 §4.2 Step 1 should reference doc 12's 40% threshold as the trigger condition.

---

## §3 NEW MECHANIC: Knot rupture as Slate event

doc 12 v1.2.1 §2.5.2 introduces Knot Rupture as a public salience-5 event with cascading consequences.

**player_agency_v30** does not currently include Knot Rupture as a mandatory Slate trigger. But by the spec's own logic, a public salience-5 event involving the Player should generate a Mandatory scene.

**INTEGRATION-PATCH-2.7 (recommended):** player_agency_v30 §4.2 Step 1 — add to mandatory triggers:
- *"Knot rupture event involving Player (per `12_development_specification.md` §2.5.2 / SIM-H-G2 / PATCH v1.2-3). Generates a mandatory Slate entry the season of rupture for any inner-circle observer; for the Player as participant, the rupture itself is the scene (no separate Slate entry needed; the rupture mechanic produces the scene as part of its specification)."*

This is a meaningful spec extension to player_agency_v30 — recommend separate editorial commit with Jordan acknowledgment.

---

## §4 INTEGRATION-PATCH SUMMARY

Seven recommended integration patches. Most are cross-references; INT-2.7 is a substantive extension of player_agency_v30.

| Patch ID | Type | Source | Action |
|---|---|---|---|
| INT-2.1 | Cross-reference table | doc 12 §7.6 | Map P2/P3 Outreach numbering to player_agency Slate priorities |
| INT-2.2 | Bilateral cross-ref | doc 12 §7.6 PATCH 3.6 + player_agency §4.2 Step 1 | Distinguish routine vs Crisis Knot scenes |
| INT-2.3 | Typographical convention | doc 12 throughout | Disambiguate "inner circle" vs "Inner Circle" |
| INT-2.4 | Cross-reference | doc 12 §8.1 | Note Standing recalc applies to NPCs; Player follows player_agency §5 |
| INT-2.5 | Cross-reference | doc 12 §6.2 Procedure E | Distinguish Procedure E from player_agency §4.5 |
| INT-2.6 | Bilateral cross-ref | doc 12 §5.4 + player_agency §4.2 Step 1 | Identify Faction Crisis ↔ Stability Crisis |
| INT-2.7 | Spec extension | player_agency §4.2 Step 1 | Add Knot rupture to mandatory triggers |

Estimated total spec-edit time: ~45 minutes.

---

## §5 RECOMMENDED PLAN

For canonical promotion of doc 12 v1.2.1:

1. **Adopt INT-2.1, 2.3, 2.4, 2.5** (doc 12-side cross-references and typographical conventions) — single editorial commit; ~15 minutes.
2. **Adopt INT-2.2 and INT-2.6** (bilateral cross-references) — separate editorial commit touching both docs; ~10 minutes.
3. **Adopt INT-2.7** (player_agency_v30 Knot Rupture mandatory) — separate editorial commit; ~5 minutes for spec edit + Jordan acknowledgment.

After INT-2.1 through INT-2.7: doc 12 ↔ player_agency_v30 integration is complete and §13 Item 5 partial (player_agency portion) is satisfied.

---

**END OF PLAYER AGENCY INTEGRATION PATCH.**
