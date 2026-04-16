# VALORIA — Player-World Bridge: Part 1 Revision Package
## Priority 1: Player Agency System — Canonization + Renown + Mechanical Scene Slate
## Priority 2: Companion Specification
## Date: 2026-04-16
## Status: PROPOSAL — requires approval before integration
## Supersedes: player_agency_v30.md §4 (Scene Slate generation), §5 (Stature Progression — extended, not replaced)
## Affects: S06 Faction Layer, S10 NPC Behavior, S12 Social Contests, S14 Fieldwork, S17 Scale Transitions, S18 Characters
## Bridge document reference: designs/audit/player_world_bridge_2026-04-16.md

---

# SECTION A: PLAYER AGENCY REVISIONS

## A.1 Renown Track (NEW — extends §5 Stature)

Standing (0–5) measures the player's relationship with one faction. Renown (0–10) measures the player's personal authority across the peninsula — the sum of what they have done, independent of who they serve.

### A.1.1 Definition

Renown represents the player's accumulated personal significance. It is not fame (fame is reputation, which already exists). It is the world's registration of the player as someone whose actions reshape outcomes. Renown persists across faction changes, survives faction collapse, and accumulates regardless of faction alignment.

### A.1.2 Renown Sources

| Source | Renown Gained | Condition |
|--------|--------------|-----------|
| Belief fulfilled | +1 | Belief completed per player_agency §2.3 |
| Duty exceeded | +1 | Duty completed with Exceeding result per §3.4 |
| Domain Echo produced | +1 | Any personal-scale action that fires Domain Echo per scale_transitions §5 |
| NPC arc influenced | +1 | Player action causes NPC Belief Scar per npc_behavior §3.2 |
| Investigation resolved (Complex+) | +1 | Evidence Track threshold 5+ reached per fieldwork §4.1 |
| Mass battle participated | +1 | Player present for mass battle resolution (command or combat) |
| Territory governance | +1 | Player governs territory and Accord improves during their tenure |
| Knot formed | +1 | New Knot established with named NPC |

**Cap:** +2 Renown per season maximum. Renown does not decay.

### A.1.3 Renown Thresholds

| Renown | Stature | Mechanical Unlock |
|--------|---------|-------------------|
| 0–2 | Unknown | No cross-faction recognition. Default. |
| 3–4 | Noted | NPCs at neutral Disposition start at +1 instead of 0. The player is someone people have heard of. |
| 5–6 | Respected | Cross-faction influence: player may suggest (non-binding) Domain Actions to any faction whose leader has Disposition ≥ +1. +1D on Impress actions. |
| 7–8 | Renowned | Independent political action: player may declare one Domain Action per season using Renown ÷ 2 (round down) as pool, without faction backing. The action targets one territory the player is present in. This is personal authority — not institutional. |
| 9–10 | Sovereign | The player is a political entity. They may found an organization (see player_agency §5.3 — now viable because Renown provides the resource base). May call a Grand Contest at any time. All NPC factions must evaluate whether to court, oppose, or accommodate the player at Priority 2 of their trees. |

### A.1.4 Interaction with Standing

Standing and Renown are independent. A player at Standing 5 / Renown 3 is a faction insider without cross-faction reputation. A player at Standing 0 / Renown 8 is an independent operator with enormous personal authority. Both are viable paths. The tension between them mirrors CK3's tension between feudal rank and personal prestige.

### A.1.5 Renown and Independent Path

The bridge overview identified the independent path (player_agency §5.3) as a "punishment path" — loss of faction resources with no alternative power structure. Renown fixes this. An independent player accumulates Renown normally (Beliefs, investigations, NPC arcs) and at Renown 7+ can take Domain Actions independently. The independent path becomes the Mount & Blade path: start as nobody, accumulate personal power, become politically significant through accumulated deeds rather than institutional membership.

---

## A.2 Mechanical Scene Slate Generation (REPLACES §4.2 narrative description)

The existing Scene Slate specification describes five priority levels abstractly. This revision makes generation deterministic and auditable.

### A.2.1 Generation Algorithm

At the start of each season's Personal Phase, execute the following:

**Step 1 — Crisis Scan (Priority 0 — mandatory, cannot be declined):**

For each condition in the following list, if TRUE, generate one mandatory scene entry:
- Player is in or adjacent to a territory at Accord 0 (Revolt)
- Player is the target of an active Heresy Investigation
- A mass battle is occurring in the player's territory
- Player's faction leader is assassinated, overthrown, or incapacitated this season

Mandatory scenes consume 1 scene action each but cannot be deferred or declined. If mandatory scenes exceed the scene action budget, remaining mandatory scenes resolve through NPC AI with the player present but unable to direct outcomes.

**Step 2 — Crisis Events (Priority 1 — presented but optional):**

For each condition, if TRUE, generate one scene entry:
- Any territory within 2 adjacencies of player at Accord ≤ 1
- Any NPC with Disposition ≥ +1 toward player has Scar count ≥ 2 (conviction crisis)
- Any NPC Knotted to the player has arc branch trigger condition met
- Any global clock crossed a band threshold this season (MS, CI, IP)
- Any NPC with Disposition ≥ +2 has an active Belief that conflicts with their faction's current priority (visible internal conflict)

**Step 3 — Duty-Aligned (Priority 2):**

Parse current Duty. Generate 1–2 scenes matching Duty requirements:
- Duty type "Investigate" → scene in the Duty's target territory with relevant NPC or location
- Duty type "Diplomacy" → scene with the Duty's target NPC
- Duty type "Governance" → scene in the Duty's target territory with local NPCs
- Duty type "Protection" → scene with the threatened NPC or asset
- Other Duty types → map to the most relevant fieldwork activity

**Step 4 — Belief-Aligned (Priority 3):**

For each active Belief, scan for intersection with:
- Named NPCs (exact name match in Belief text)
- Faction references (faction name match)
- Territory references (territory name match)
- System keywords ("Thread," "Church," "investigation," "treaty," "Einhir," "Calamity")

For each intersection found, generate one scene entry with the matching NPC/location. Maximum 3 Belief-generated scenes.

**Step 5 — NPC Outreach (Priority 3 — NEW):**

For each named NPC where ALL of the following hold:
- Disposition ≥ +2 toward the player
- NPC has an active Belief relevant to the player's location or faction
- NPC's priority tree fired an action this season that could benefit from the player's involvement

Generate one scene entry: "[NPC] seeks to meet with you. [One-sentence description of their agenda]."

For each named NPC where ALL of the following hold:
- Disposition ≤ −2 toward the player
- NPC holds institutional authority over the player's current territory
- NPC's priority tree fired an action targeting the player's faction or interests

Generate one scene entry: "[NPC] has summoned you. [One-sentence description of the demand]." Declining an NPC demand: Disposition −1 with the NPC, +1 Exposure in their territory.

**Step 6 — Territorial (Priority 4):**

Generate 1–2 scenes from the player's current territory:
- New NPC arrival (NPC from a different territory visiting or displaced)
- Trade/economic event (merchant caravan, resource dispute, guild activity)
- Thread phenomenon (if RS ≤ 60 in this territory's Calamity band)
- Military movement (if any faction moved units into or through the territory)

**Step 7 — Ambient (Priority 5):**

Generate 1 ambient scene: an unstructured encounter offering low-stakes information or minor relationship opportunity.

### A.2.2 Slate Presentation

The Slate presents all generated entries to the player as a list. Each entry shows:
- NPC name and location
- One-sentence description
- Tag(s): which Belief, Duty, or game-state condition generated this entry
- Priority level (visible to player — they should know what is urgent)

### A.2.3 Opportunity Resolution (Not Pursued)

For each Priority 1–3 entry the player does not pursue:

| Entry Source | Resolution |
|-------------|-----------|
| NPC arc moment | NPC resolves based on their Conviction and AI priority. Belief Scar may occur without player influence. Player's Disposition with NPC does not change (they weren't involved). |
| Territory crisis | Faction AI handles via Govern roll at faction stat level. Accord adjusts based on result. |
| Clock threshold | Effects propagate normally. No player mitigation. |
| Duty-aligned | Duty is not completed. Standing −1 at Accounting. |
| NPC Outreach | NPC acts without player input. Disposition −1 (NPC feels ignored) if NPC Disposition was ≥ +3. |
| NPC demand | Disposition −1 with NPC. +1 Exposure. Potential escalation (Heresy Investigation, military action, political pressure) at NPC's discretion per priority tree. |

---

## A.3 Belief-Conviction Vocabulary Unification (CONSOLIDATION)

Per bridge overview §2.3: player Beliefs and NPC Convictions serve the same function. Unify vocabulary:

**Conviction** = what an actor (player or NPC) holds as fundamentally true and worth acting on. Players author their own Convictions (formerly "Beliefs"). NPCs have system-authored Convictions.

**Resonant Style** = the type of argument that can challenge a Conviction. Both player Convictions and NPC Convictions are vulnerable to Resonant Styles. When an NPC's argument targets a player's Conviction successfully (Contest victory using the correct Resonant Style), the player marks a Conviction strain. Three strains: the Conviction transforms or is abandoned.

This is symmetrical. The player can wound NPC Convictions via Resonant Style targeting. NPCs can wound player Convictions via the same mechanic. The world affects the player the same way the player affects the world.

**Mechanical change:** Rename "Beliefs" to "Convictions" throughout player_agency_v30. The §2 section becomes "§2 — CONVICTIONS" with identical content except the name.

---

# SECTION B: COMPANION SPECIFICATION (NEW)

## B.1 Definition

A companion is a named NPC who travels with the player character. Maximum: 2 companions at any time (cognitive load constraint — more than 2 companions splits player attention below the threshold of meaningful relationship).

## B.2 Formation

### B.2.1 Eligibility

An NPC is eligible for companionship if:
- Disposition ≥ +3 toward the player
- Not currently serving as a faction leader
- Not currently under active Heresy Investigation targeting them
- Player has interacted with the NPC in at least 2 prior scenes (relationship has established history)

### B.2.2 Invitation

The player may invite an eligible NPC during any social scene. This is a Connect action (Bonds, Ob = floor(NPC's highest Disposition toward any other faction ÷ 2) + 1, minimum 1). Per the recruitment procedure (npc_behavior §9.5) with one modification: companions are not recruited — they are invited. No Hook system applies. The NPC joins because the relationship is genuine.

| Degree | Result |
|--------|--------|
| Failure | NPC declines. May retry next season. No Disposition change. |
| Partial | NPC is interested but has obligations this season. Will accept next season automatically if re-invited. |
| Success | NPC joins. Starting companion Disposition = current Disposition. |
| Overwhelming | NPC joins eagerly. +1 Disposition. Reveals one personal Conviction (one the player did not know). |

### B.2.3 Departure

A companion departs if:
- Disposition drops below +1 (relationship insufficient to sustain travel together)
- Knot strain exceeds the NPC's Bonds capacity (if Knotted)
- The companion's active Conviction is violated by the player's actions (3 violations = departure)
- The companion's faction enters Survival priority (Stability ≤ 2) — they are recalled
- The player dismisses them (free action, Disposition −1)

Departure is always a scene. The companion does not silently vanish. They explain why they are leaving. The player may attempt to persuade them to stay (social contest, 1 exchange, Attunement-primary). The farewell scene does not cost a scene action — it is mandatory and free, because the end of a companionship is always worth experiencing.

## B.3 Companion Actions

### B.3.1 Free Social Action

Each companion generates 1 free social fieldwork action per season. This represents conversation during travel — the player does not spend a scene action to talk to their companion. The free action can be: Read (learn the companion's current state), Converse (shift Disposition, gather information the companion knows), or Connect (deepen the relationship).

### B.3.2 Scene Participation

When the player pursues a scene, companions are present unless the scene is explicitly solo (infiltration, private meeting). Companions participate:

- **Combat:** Companion fights using their own stats. They follow the player's tactical lead but may deviate if the situation conflicts with their Conviction (e.g., a companion with Equity conviction may refuse to attack civilians). Companion wounds are tracked independently. Companion incapacitation → forced departure at season end unless Mended.
- **Social Contest:** Companion may Corroborate per social_contest §9.2. Knot-sharing companions: Ob 1. Non-Knotted: Ob 2.
- **Investigation:** Companion assists per fieldwork §3.2 (multi-character exploration). +1 to leader's net on Success, +1 Exposure on failure.
- **Thread Operations:** If the companion has TS ≥ 30, they may participate in collective Thread operations. If TS < 30, they are a non-sensitive partner subject to Dissonance checks per fieldwork §2.7.

### B.3.3 Companion Commentary

At the end of each scene, the companion offers one comment on what happened. The comment reflects their Conviction and Resonant Style. This is the Dragon Age/Tyranny mechanic — the companion is the player's mirror. Their commentary is not mechanical (no dice, no Ob). It is narrative texture that makes the world's response to the player's actions personal and immediate.

Implementation:
- **TTRPG:** GM voices the companion's comment based on their Stance Triangle.
- **Videogame:** Generated from the companion's Conviction, Resonant Style, and the scene's outcome. Template: "[Companion name] [reaction verb] when [scene outcome]. They say: '[1-sentence comment reflecting their Conviction].'"
- **Hybrid:** GM voices during Personal Phase.

### B.3.4 Companion Reaction to Scene Slate

When the Scene Slate is presented, each companion states their opinion on 1–2 entries. The opinion reflects their Conviction:
- An NPC with Order conviction: "We should attend the parliament session. Stability matters."
- An NPC with Equity conviction: "The people in Grauwald need help more than Baralta does."
- An NPC with Reason conviction: "The Thread anomaly is more important than politics. Let the factions handle their own problems."

This is not binding. The player decides. But the companion's voice is always present in the decision.

## B.4 Companion and Domain Echo

A companion's participation in a scene adds +1 to the player's net successes for Sufficient Scope evaluation (scale_transitions §7). The companion's presence makes personal actions more politically visible — you are not a lone operative, you are a named figure with a retinue. This lowers the Domain Echo threshold without changing its rules.

## B.5 Companion and the Interdependency Matrix

| System | Companion Interaction |
|--------|----------------------|
| S06 Faction | Companion's faction Disposition toward player shifts ±1 based on companion's seasonal report. Good treatment = +1. Conviction violation = −1. |
| S10 NPC | Companion IS an NPC with full Stance Triangle. All NPC behavior rules apply. |
| S11 Combat | Companion fights. Companion wounds/death cascade per NPC rules. |
| S12 Contest | Companion Corroborates. Companion's Conviction may conflict with player's argument. |
| S14 Fieldwork | Companion assists exploration/investigation. Free social action per season. |
| S17 Scale | Companion presence modifies Sufficient Scope threshold. Companion present during Zoom In. |
| S18 Character | Companion Knot formation uses standard Knot rules. |

---

# SECTION C: IMPLEMENTATION SEQUENCE

## C.1 Immediate (This Revision Package)

1. Rename "Beliefs" to "Convictions" in player_agency_v30.
2. Add §5.4 Renown Track to player_agency_v30.
3. Replace §4.2 with mechanical Scene Slate generation algorithm (§A.2).
4. Add §4.2b NPC Outreach generation (formerly bridge overview §1.8 proposal).
5. Add §4.5b Opportunity Resolution table.
6. Write companion_specification_v30.md (new file, ~150 lines from §B above).

## C.2 Next Session (Priorities 3–5)

7. Extend npc_behavior_v30 §8 priority trees to generate NPC Outreach entries.
8. Add mandatory Zoom In triggers to scale_transitions_v30 §4.3.
9. Add "Where Were You?" retrospective scene generation to scale_transitions_v30.
10. Add Investigation Synthesis (Reconstruct as completion mechanic) to fieldwork_v30 §4.
11. Add NPC-initiated social entries to fieldwork_v30 §5.

## C.3 Following Session (Priorities 6–8)

12. Add Obligation system to social_contest_v30 §6 (post-contest binding commitments).
13. Add Scar visibility to npc_behavior_v30 §3.3.
14. Add multiple Accord pathways to peninsular_strain_v1 §2.
15. Add Domain Echo on named NPC combat to scale_transitions_v30 §5.
16. Add combat reputation cascade.
17. Add combat death cascade.

## C.4 Final Session (Priorities 9–10 + Holistic Review)

18. Add CV change flavor events to conviction_track_v30.
19. Add Church pressure indicators.
20. Add post-battle consequence scenes to mass_battle_v30.
21. Add named unit officers.
22. **Holistic review:** Read all revised documents. Evaluate every system on World→Player and Player→World. Verify interdependency matrix still holds. Run compound chain analysis on the revised specifications.

---

# SECTION D: PROPAGATION MAP

| Changed File | Systems Affected | Propagation Required |
|-------------|-----------------|---------------------|
| player_agency_v30.md | S06, S10, S14, S17, S18 | params_core (character creation step), canonical_sources.yaml, session_log |
| companion_specification_v30.md (NEW) | S10, S11, S12, S14, S17, S18 | canonical_sources.yaml, file_index, NPC roster annotations |
| npc_behavior_v30.md (§8 extension) | S06, S14, S17 | NPC priority trees in params_factions |
| scale_transitions_v30.md (§4.3 extension) | S06, S10, S16 | arc_register (Zoom In triggers) |
| fieldwork_v30.md (§4 + §5 extension) | S10, S12 | params_fieldwork |
| social_contest_v30.md (§6 extension) | S06, S10 | params_contest |
| peninsular_strain_v1.md (§2 extension) | S03, S06, S07 | victory_v30, params_board_game |
| combat_v30.md (Domain Echo extension) | S06, S17 | params_combat |
| conviction_track_v30.md (presentation layer) | S08 | None — additive only |
| mass_battle_v30.md (aftermath scenes) | S10, S17 | params_mass_combat |

---

*End of revision package.*
