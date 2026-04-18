# VALORIA — Campaign Architecture v1
## Date: 2026-04-17
## Status: CANONICAL — approved by Jordan 2026-04-17
## Scope: Consolidated design for all systems introduced or corrected in the 2026-04-17 victory revision session. Church settlement infrastructure, CI=100, RM identity, Thread revelation curve, phased IP escalation, Altonia repulsion, MS loss reform, Coherence asymmetry, Mending community, Portrait Retirement, Lineage, Warden faction paths.
## Supersedes: All prior "alternate victory condition" framing. All "shared loss" framing. The ×3 mass battle MS multiplier. Flat Coherence cost tables.
## Cross-references: victory_v30.md, peninsular_strain_v1.md, settlement_layer_v30.md, threadwork_v30.md, params_threadwork.md, rs_budget.md, player_agency_v30.md, npc_behavior_v30.md

---

# PART 1: CHURCH SETTLEMENT INFRASTRUCTURE

## §1.1 Four Independent Axes

Church presence in a settlement is four independent attributes, not a linear progression.

**Axis 1 — Religious Building (mutually exclusive):**
| Level | PT Effect | Seizure Ob Mod | Notes |
|-------|-----------|----------------|-------|
| None | 0 | 0 | No foothold |
| Chapel | +0.5/season | 0 | Traveling priest. Latent faith. |
| Church | +1/season | −1 | Resident priest. Inquisitor visits viable. |
| Cathedral | +2/season, +0.5 to adjacent | −2 | Irreplaceable. Destroyed only by Mass Battle. |

**Axis 2 — Templar Station (yes/no):**
+1 TC/season in territory. Can interrupt rival Domain Actions (+1 Ob, costs 1 TC). Seizure Ob −1.

**Axis 3 — Inquisitor Base (yes/no):**
Surveillance Zone: practitioners Concealment test each season. RM organizing +1 Ob. 1 Church Attention/season if RM present. Seizure Ob −1.

**Axis 4 — Church Governor (yes/no):**
Church official governs settlement. De facto Church territory. Removal: Mass Battle, Mandate Challenge (Ob 6+), or RM community action OW. Seizure Ob −2.

## §1.2 Combined Modifiers

Axes stack independently. Maximum per-settlement Seizure Ob modifier: −6 (Cathedral + Templar + Inquisitor + Governor). Territory modifier = sum across all settlements.

Base Seizure Ob = 7 − PT. With territory infrastructure modifier applied.

## §1.3 CI=100 — Mass Seizure Declaration

When CI reaches 100: every territory with at least one settlement containing a Church building (Chapel+) is targeted for simultaneous Seizure. Individual Ob per territory = 7 − PT − (sum of infrastructure modifiers across settlements in that territory).

The Mass Seizure Declaration is a mandatory Zoom In scene. Archbishop declares. All factions get 1 Emergency Session season to respond. Then each territory resolves independently.

CI=100 does not mean Church wins. It means Church makes its bid for theocracy. Success is per-territory. The Church still needs all 15 territories at Accord ≥ 2 for Peninsular Sovereignty.

Seized territories start at Accord 1 (military-equivalent) or Accord 2 (if PT ≥ 3). Church must govern what it seized.

---

# PART 2: RESTORATION MOVEMENT — IDENTITY

## §2.1 What RM Is

RM is a sociopolitical movement to end the caste system and restore Einhir governance. The Einhir governance model: node-based meritocratic consensus cells — governance through equity, participation, care, and collaborative decision-making. Utopian anarchism structured as a self-governing network.

**RM does not believe threadwork is real.** Threadwork is folklore to RM. The governance nodes were physically located at Threadweaving sites, but RM views the Thread component as fable. RM restores the political model, not the metaphysical practice.

## §2.2 RM Actions — Political, Not Thread

"Community Organizing" for RM is political organizing, NOT a Thread operation. Rename across all docs to **Community Organizing** when RM is the actor. The action:
- Builds consensus-governance cells in settlements
- Uses social stats (Charisma, Attunement), not Thread stats (Spirit)
- Produces Presence markers, PT reduction through cultural displacement, governance-cell establishment
- Does NOT produce MS change, co-movement, or any Thread mechanical effect

PT reduction by RM is sociological: Church institutional authority displaced by RM institutional authority. People attend consensus assemblies instead of sermons. Slower than Thread-based PT reduction but more persistent.

## §2.3 RM's Crisis — When Folklore Becomes Real

When Thread phenomena become publicly visible (see Part 4), RM discovers the governance nodes they've been building ARE Threadweaving sites. Three possible NPC arc paths for Maret Vossen:
- **Embrace:** RM integrates Thread reality. The governance model was always metaphysical. RM becomes potential Warden ally.
- **Denial:** RM insists the model works politically, not metaphysically. Coherent but disadvantaged.
- **Schism:** Movement splits. Thread-aware branch allies with Wardens/Varfell. Rationalist branch maintains pure political program.

Player influence determines which path. Social contests, evidence presentation, Thread demonstrations shift Vossen's arc.

---

# PART 3: MS LOSS REFORM AND COHERENCE ASYMMETRY

## §3.1 Mass Battle MS Loss — ×3 Multiplier Struck

Replace with flat additive:
- Standard Mass Battle: −1 MS per battle, regardless of scale or outcome
- Mass Battle in destabilized substrate (MS ≤ 10): −1 MS + Stability Check (Ob 3), failure adds −1 MS (max −2/battle)

Three battles per season = −3 MS. Predictable. Cumulative. No spikes. Player can see degradation coming and choose to stop fighting.

## §3.2 Coherence Cost Asymmetry

| Threadwork Type | Coherence Cost | Rationale |
|----------------|---------------|-----------|
| Mending (standard) | 0 | Aligned with substrate coherence. Healing, not violation. |
| Mending (OW or extended) | 1 | Even aligned work under extreme strain leaves a mark. |
| Mending (seasonal fatigue) | +1 cumulative Ob per Mending in same season | Fatigue, not corruption. Resets each season. |
| Sight (passive) | 0 | Observation doesn't alter flow. |
| Sight (active/forced) | 1 | Forcing sight into torn areas is against the flow. |
| Lock | 1 per test | Freezing flow is against substrate nature. |
| Dissolution | 2 per test | Active unmaking. Tears rather than heals. |
| Extraction | 1–2 (by scale) | Removing from substrate carries cost. |
| Binding | 2 per test | Imposing permanent constraint. |

Mending at 0 cost means practitioners can Mend sustainably without self-destruction. The seasonal fatigue Ob (+1 cumulative, resets each season) prevents infinite Mending within a single season without invoking Coherence damage.

## §3.3 Mending Community

Edeyja is the best Mender (Spirit 6) but NOT the only one. The Warden community, some RM-adjacent practitioners (post-revelation), some Varfell-aligned threadworkers, and potentially pre-schism Church mystics all engage in Mending.

| Spirit | Tier | Standard Success MS | OW MS |
|--------|------|-------------------|-------|
| 1–2 | Journeyman | +1 | +2 |
| 3–4 | Skilled | +1 | +3 |
| 5 | Expert | +2 | +4 |
| 6 (Edeyja) | Master | +2 | +5. May Mend in destabilized zones (MS ≤ 5) without Stability Check. |

MS recovery is cumulative across all active Menders per season.

---

# PART 4: THREAD REVELATION CURVE

## §4.1 Starting State

At game start (MS ~72), threadwork is folklore. Common people: old stories. Church: heresy framework. Crown/Hafenmark: irrelevant. Varfell: knows (VTM track). Wardens: living it (marginal).

## §4.2 MS-Driven Visibility

| MS Band | What Non-Practitioners See | Political Impact |
|---------|---------------------------|-----------------|
| 100–80 | Nothing. Folklore. | None. |
| 79–60 | Subtle anomalies near Southernmost. Animals, crops. | Mild unease. Church: "God's testing ground." |
| 59–40 | Observable. Gaps as physical distortions. Disappearances. | Fear. Church scrambles. Crown must act. Varfell gains value. RM denial harder. |
| 39–20 | Peninsula-wide. Rendering failures in daily life. Threadcut beings encountered by ordinary people. | Crisis of understanding. "The stories were true." Every faction must respond. |
| 19–1 | Undeniable. Non-practitioners perceive substrate. World visibly frays. | Existential reorientation. Political order challenged at its foundations. |

## §4.3 Revelation Triggers

Specific events accelerate visibility regardless of MS: renowned character performs threadwork publicly; Threadcut being encountered in populated settlement; Edeyja's Mending produces visible results; mass battle involving Thread operations; RM discovers governance node IS a Threadweaving site.

Each trigger fires a Revelation Event scene — mandatory Scene Slate entry where player and NPCs react.

---

# PART 5: PHASED IP ESCALATION AND ALTONIAN REPULSION

## §5.1 Three-Phase Invasion

**Phase 1 (IP reaches 100):** First mountain pass. One border territory under Active Invasion. Domain Actions +1 Ob in contested territory. IP decay begins.

**Phase 2 (IP sustained 85+ for 3 seasons after Phase 1):** Second corridor through Schoenland. Two additional territories. Altonian Governorate formally established (Mandate 2, Military 4, Stability 3). Underground Network activates.

**Phase 3 (IP sustained 80+ for 3 more seasons):** Third corridor northwest. Governorate contiguous territory chain. Mandate 3, Military 5, Stability 4. All faction Domain Actions +2 Ob in occupied territories.

Phase retreats: IP < 85 → Phase 1 retreats. IP < 75 → Phase 2 retreats. IP < 60 → full retreat.

## §5.2 Altonia Can Be Repelled

**Military repulsion:** Two consecutive Overwhelming Mass Battle results vs Altonian forces → full withdrawal. IP resets to 60. Cannot rise above 80 for 10 seasons.

**Diplomatic repulsion:** Elske Loyalty ≥ 6 + Social Contest vs Vanguard Commander (Ob 4) + IP < 80 → IP drops to 40. Overwhelming: IP to 20 + Non-Aggression Pact 20 seasons.

**Resistance repulsion (during Occupation):** Underground Network Mandate 3 + Governorate Accord 0 in all occupied territories + Mass Battle Success vs Governorate → full withdrawal. IP resets to 30.

After repulsion by any path: IP freezes, cannot rise. Altonian threat permanently resolved for campaign.

---

# PART 6: WARDEN FACTION PATHS

## §6.1 Starting State

Wardens: ~8–15 Einhir in Southernmost. Informal network, not a faction. No hierarchy, no charter. Edeyja is the best Mender, not a leader. The "council" is people meeting and saying "this is bad." No political influence, no military capacity, no economic resources.

## §6.2 Five Paths to Political Relevance

**A — Recruited by Varfell.** WR 3+ → institutional branch of Varfell. Gains Varfell's resources; Varfell gains Thread capability. Risk: Mending used as political leverage.

**B — Recruited by RM (post-revelation).** RM Embrace arc + Vossen alliance with Wardens. RM governance cells + Warden Mending. Most philosophically complete alliance.

**C — Recruited by player.** High WR + player's Founded Org → Warden-aligned political entity. Player builds the faction from scratch.

**D — Recruited by Lenneth.** Elske Loyalty Track + Schoenland diplomacy → Crown-Warden integration. Thread stewardship as royal governance function.

**E — Independent (crisis-driven).** MS ≤ 20 → Wardens realize marginal Mending is insufficient. Declare Mending Sanctuaries. Enforce with Thread capability. Conquest driven by desperation. The hardest and most distinctive path.

## §6.3 Warden Faction Mechanics (if activated)

- Consensus governance (not hierarchical). Governance stat = average Spirit of active Menders.
- Acquisition via Mending Sanctuaries — demonstrated stewardship earns governance recognition.
- Victory path: still Peninsular Sovereignty, but through stewardship not conquest. Hardest path.

---

# PART 7: PORTRAIT RETIREMENT AND LINEAGE

## §7.1 Portrait Retirement ("A Life in Valoria")

Non-faction characters end by choosing when to stop. After ≥ 2 of 3 starting Convictions resolved (Fulfilled/Failed/Transformed), the option "Conclude this story" appears at any season transition.

Selecting it fires the Portrait Sequence: Opening Line, Conviction Chapter (3 arcs), World Footprint (counterfactual impact), Relationship Map (Knots), Final State, The World They Leave.

## §7.2 Draft Portrait

Available from main menu at any time. Shows what the Portrait would say now. Current Conviction states, current Knots, current Footprint. The in-play feedback mechanism for non-faction players.

## §7.3 Conviction Resolution States

Each of the player's 3 starting Convictions tracks resolution state:
- **Fulfilled** — player completed ≥2 scene actions in pursuit; external world state aligned
- **Failed** — external event prevented fulfillment despite player engagement (≥1 scene action)
- **Transformed** — Conviction changed through play (≥1 Conviction-adjacent scene before transformation)
- **Unresolved** — no sufficient engagement

Deliberate self-contradiction does not produce valid resolution (exploit gate per audit Problem 03).

## §7.4 Lineage Acts (3 types)

| Type | Inheritance | How Established |
|------|------------|-----------------|
| Mentorship | Skills at 60%, Founded Org membership, 1 Close Knot (Disposition −2) | Designate mentee (existing NPC, Disposition ≥ +3) |
| Succession | Standing, titles, faction affiliation, estates | Declare heir (dialogue/scene) |
| Thread Legacy | WR at half (rounded down), Thread knowledge, discoverable Knot in substrate | Embed knowledge (requires WR ≥ 2) |

Death without Lineage Act: clean break. New character in same world, no mechanical inheritance. Predecessor's Portrait recorded. World continues.

---

# PART 8: PROPAGATION REQUIRED

This document is the canonical source for all systems above. The following existing documents require cross-reference updates to point here. These are propagation tasks for follow-up sessions:

| Target Document | Section | Change |
|-----------------|---------|--------|
| settlement_layer_v30 §1.4 | Church axes | Add cross-ref to this doc Part 1 |
| victory_v30 §5 | World-State Transitions | Add phased IP detail from Part 5 |
| victory_v30 §7 | TC/CI | Add CI=100 Mass Seizure from Part 1 §1.3 |
| threadwork_v30 §5.2 | MS sources | Strike ×3, reference Part 3 §3.1 |
| params_threadwork §Coherence | Cost table | Replace with Part 3 §3.2 |
| rs_budget §2.2 | Mass battle drain | Update from ×3 to flat −1 |
| player_agency_v30 §2 | Convictions | Add resolution-state tracking from Part 7 §7.3 |
| All RM references | "Community Organizing" | Rename to "Community Organizing" per Part 2 §2.2 |
| worldbuilding_v30 or threadwork_v30 | Thread visibility | Add revelation curve from Part 4 |
| npc_behavior_v30 | Warden paths | Add cross-ref to Part 6 |
| videogame_mode_spec | All sections | Update for Portrait Retirement, Lineage, CI=100, IP phases |
