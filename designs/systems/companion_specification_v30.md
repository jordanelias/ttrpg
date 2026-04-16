<!-- SKELETON — mechanical spec only -->
<!-- No infill file yet -->
<!-- Status: PROPOSAL — requires approval before integration -->
<!-- Date: 2026-04-16 -->
<!-- Affects: S10 NPC Behavior, S11 Combat, S12 Social Contests, S14 Fieldwork, S17 Scale Transitions, S18 Characters -->
<!-- Cross-references: player_agency_v30.md, npc_behavior_v30.md §9.5 (recruitment), fieldwork_v30.md §2.7/§5, social_contest_v30.md §9.2 (corroboration), scale_transitions_v30.md §5/§7 (Domain Echo / Sufficient Scope), combat_v30.md -->
<!-- Canon compliance: P-01 (co-movement applies to companion Thread ops), P-12 (Knot strain propagates through companion relationship), P-15 (three-layer being-persistence — companion relationship is cultural-personal, Knot is metaphysical) -->

# VALORIA — Companion Specification
## What it means for an NPC to travel with the player

---

## §1 — DEFINITION

A companion is a named NPC who travels with the player character across territories and seasons. A companion is not a hireling (no wage), not a summon (no magical bond), and not a party member in the D&D sense (no independent leveling). A companion is a person who has chosen to walk with you because your relationship is worth the risk.

Maximum: 2 companions at any time. This constraint is cognitive — three or more companions dilute the player's relationship investment below the threshold where individual companions feel significant. Dragon Age and Tyranny both demonstrate that 2–3 active companions is the sweet spot for meaningful relationship gameplay.

---

## §2 — FORMATION

### §2.1 Eligibility

An NPC is eligible for companionship if ALL hold:
- Disposition ≥ +3 toward the player
- Not currently serving as a faction leader
- Not under active Heresy Investigation targeting them
- Player has interacted with the NPC in at least 2 prior scenes (relationship has history)

### §2.2 Invitation

The player may invite an eligible NPC during any social scene. This is a Connect action (Bonds pool per fieldwork_v30 §2.1).

**Ob = floor(NPC's highest Disposition toward any other faction ÷ 2) + 1, minimum Ob 1.**

An NPC deeply loyal to their faction is harder to invite — they have existing commitments. An NPC with weak faction ties is easier. This uses the same Ob formula as the NPC Recruitment procedure (npc_behavior_v30 §9.5) but without the Hook system — companionship is relational, not transactional.

| Degree | Result |
|--------|--------|
| Failure | NPC declines. May retry next season. No Disposition change. |
| Partial | NPC interested but has obligations this season. Accepts automatically next season if re-invited. |
| Success | NPC joins. Starting companion Disposition = current Disposition. |
| Overwhelming | NPC joins eagerly. Disposition +1. Reveals one personal Conviction the player did not know. |

### §2.3 Companion Slot Management

If both companion slots are filled and the player wants to invite a new NPC, they must first dismiss a current companion. Dismissal costs Disposition −1 with the dismissed companion and generates a departure scene (see §3).

---

## §3 — DEPARTURE

A companion departs if any of the following conditions are met:
- Disposition drops below +1 (relationship insufficient)
- Knot strain exceeds NPC's Bonds capacity (if Knotted — per threadwork_v30 Knot strain rules)
- Companion's active Conviction is violated by the player's actions 3 times (tracked per season; resets at year end)
- Companion's faction enters Survival priority (Stability ≤ 2) — recalled by institutional obligation
- Player dismisses them (free action)

### §3.1 Departure Scene

Departure is always a scene. The companion does not silently vanish. They explain why they are leaving. The departure scene does not cost a scene action — it is mandatory and free.

During the departure scene, the player may attempt one persuasion: a social contest (1 exchange, Attunement-primary, no adjudicator) to convince them to stay. If the departure cause is Conviction violation (3 strikes), the persuasion Ob is +2 (the betrayal is structural, not misunderstanding). If the departure cause is faction recall, the persuasion Ob is +1 (institutional loyalty competes with personal bond).

Successful persuasion: companion stays for 1 additional season. The underlying cause must be addressed by season end or they depart without a second persuasion opportunity.

---

## §4 — COMPANION ACTIONS

### §4.1 Free Social Action

Each companion generates 1 free action per season that can be used as EITHER a social fieldwork action (companion role) OR a governance action (governor role, if the companion is also a settlement governor per settlement_layer_v30 §3.2). The player chooses each season which role the companion prioritizes. This creates a meaningful trade-off: relationship deepening vs settlement development. The player does not spend a scene action. The free action can be:
- **Read** (learn companion's current state — emotional condition, active Conviction, attitude toward recent events)
- **Converse** (shift Disposition, gather information the companion knows)
- **Connect** (deepen the relationship toward Knot eligibility)

Pool and Ob per fieldwork_v30 §5.2. The free action cannot be: Investigate, Negotiate, or Rumour (these require scene context, not travel conversation).

### §4.2 Scene Participation

When the player pursues a scene, companions are present unless the scene is explicitly solo (infiltration, covert meeting). Present companions participate as follows:

**Combat:** Companion fights using their own stats per combat_v30. They follow the player's tactical lead but may deviate if the combat conflicts with their Conviction. A companion with Equity conviction may refuse to attack civilians. A companion with Order conviction may refuse to ambush (honorable engagement only). Deviation is not disobedience — it is character. Companion wounds are tracked independently. Companion incapacitation → forced departure at season end unless Healed or Mended.

**Social Contest:** Companion may Corroborate per social_contest_v30 §9.2. Knot-sharing companions: Ob 1. Non-Knotted: Ob 2. The companion may only Corroborate arguments consistent with their own Conviction. An Order-conviction companion will not Corroborate an argument advocating institutional disruption.

**Investigation:** Companion assists per fieldwork_v30 §3.2 (multi-character exploration). +1 to leader's net on Success, +1 Exposure on Failure. Maximum 1 companion assists per investigation action (the second companion, if present, cannot stack assistance).

**Thread Operations:** If companion TS ≥ 30, they may participate in collective Thread operations per threadwork_v30. If TS < 30, they are a non-sensitive partner subject to Dissonance checks per fieldwork_v30 §2.7.

### §4.3 Companion Commentary

At the end of each scene, the companion offers one comment on what happened. The comment reflects their Conviction and Resonant Style.

- **TTRPG:** GM voices the companion's comment based on their Stance Triangle (npc_behavior_v30 §2).
- **Videogame:** Generated from companion's Conviction, the scene's outcome, and the player's choices. The companion approves when the player acts consistently with the companion's Conviction (+1 Disposition over time) and disapproves when the player contradicts it (−1 Disposition over time, tracked toward the 3-violation departure threshold).
- **Hybrid:** GM voices during Personal Phase.

### §4.4 Scene Slate Commentary

When the Scene Slate is presented each season, each companion states their opinion on 1–2 entries. The opinion reflects their Conviction:
- Order conviction: "We should attend to the stability crisis first."
- Equity conviction: "The common folk in Grauwald need us more than the parliament does."
- Reason conviction: "The Thread anomaly is the real threat. Politics can wait."
- Faith conviction: "The Church summons cannot be ignored. Refusal has consequences."

This is advisory, not binding. The player decides. But the companion's perspective is always present in the decision, giving the world a personal voice in the player's triage.

---

## §5 — COMPANION AND THE WORLD BRIDGE

### §5.1 Domain Echo Modification

A companion's presence in a scene adds +1 to the player's net successes for Sufficient Scope evaluation (scale_transitions_v30 §7). The companion makes personal actions more politically visible — the player is not a lone operative but a named figure with a retinue. This effectively lowers the Domain Echo threshold without changing its rules.

### §5.2 Faction Feedback Loop

The companion's faction receives feedback on the player's treatment of the companion:
- Season end, companion Disposition ≥ +3: companion's faction Disposition toward player +1 (good report)
- Season end, companion Conviction violated this season: companion's faction Disposition toward player −1 (bad report)
- Companion departure due to player action: companion's faction Disposition toward player −2 (the player mistreated one of their own)

This creates a World→Player bridge through the companion: the player's personal relationship with the companion has faction-level consequences. Treating Baralta's aide well improves relations with Hafenmark. Betraying Vaynard's scholar damages relations with Varfell.

### §5.3 Companion Arc Integration

Companions retain their full NPC arc profiles (npc_behavior_v30 §5.2). Traveling with the player does not suspend their arc — it accelerates it. The companion is exposed to more events, more choices, more ethical pressure than a stationary NPC. Their Conviction Scar accumulation rate may be higher because the player's actions constantly test their framework.

When a companion's arc branch trigger fires while they are traveling with the player, the arc scene IS a Priority 0 mandatory Scene Slate entry. The player witnesses the companion's transformation directly. They cannot miss it. This is the Dragon Age moment — when your companion changes, you are there.

---

## §6 — COMPANION INTERDEPENDENCY MATRIX

| System | Interaction |
|--------|------------|
| S06 Faction Layer | Companion faction Disposition feedback (§5.2). Companion presence modifies Domain Echo threshold (§5.1). |
| S10 NPC Behavior | Companion IS an NPC with full Stance Triangle. All NPC behavior rules apply. Arc profiles active. |
| S11 Combat | Companion fights with own stats. Combat Conviction deviation possible. Incapacitation triggers departure. |
| S12 Social Contest | Companion Corroborates with Conviction constraint. Knot-sharing reduces Ob. |
| S14 Fieldwork | Companion assists exploration/investigation. Free social action per season (§4.1). |
| S17 Scale Transitions | Companion presence modifies Sufficient Scope. Companion arc moments are mandatory Zoom In triggers. |
| S18 Characters | Companion Knot formation uses standard Knot rules. Companion departure produces Knot strain if Knotted. |

---

## §7 — OPEN ITEMS

| ID | Description | Priority |
|----|-------------|----------|
| ED-COMP-01 | Named companion candidates per faction: which NPCs are designed as companion-eligible? Cross-reference with NPC roster. | P2 |
| ED-COMP-02 | Companion combat AI: does the companion act autonomously in combat, or does the player direct them? TTRPG: GM runs companion. Videogame: AI with Conviction-based behavior. Confirm. | P2 |
| ED-COMP-03 | Companion and mass combat: does the companion function as a unit officer, a personal-scale participant, or both? | P3 |
| ED-COMP-04 | Companion departure Knot consequence: if a Knotted companion departs, does the Knot break (rupture) or persist at distance (dormant)? Canon P-12 suggests Knots are constitutive and do not break by choice — the Knot persists but strain accumulates. Confirm. | P2 |

---

## §8 — PROPAGATION ON ACCEPTANCE

| File | Change |
|------|--------|
| references/canonical_sources.yaml | New system entry: companion_specification |
| designs/systems/player_agency_v30.md | §4.2 Step 5 references companion Scene Slate commentary |
| designs/systems/npc_behavior_v30.md | §9.5 cross-reference: recruitment vs companionship distinction |
| designs/combat/combat_v30.md | Multi-character combat rules cross-reference |
| designs/fieldwork/fieldwork_v30.md | §3.2 multi-character assistance cross-reference |
| designs/contest/social_contest_v30.md | §9.2 Corroboration cross-reference |
| designs/hybrid/scale_transitions_v30.md | §7 Sufficient Scope modification |
| references/file_index_summary.md | New file entry |
| canon/editorial_ledger.yaml | ED-COMP-01 through ED-COMP-04 |

*End of document.*
