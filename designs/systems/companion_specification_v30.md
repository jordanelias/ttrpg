<!-- companion_specification_v30.md — created 2026-04-16 -->
<!-- Resolves: ED-555 (missing doc), ED-557 (stat gen), ED-559 (combat AI), ED-571 (distinction) -->
<!-- Sources: mass_battle_v30 §D.2, npc_behavior_v30 §9.5, scale_transitions_v30 §4.3.2, combat_v30 §4 -->
<!-- Status: DESIGN PROPOSAL — awaiting approval -->

# VALORIA — Companion Specification v1.0
## Date: 2026-04-16

---

## §1 DEFINITION AND SCOPE

### §1.1 What a Companion Is

A **Companion** is a named NPC who has formed a sustained personal relationship with the Player Character through play, meeting a mechanical threshold (Disposition ≥ +3), and who travels with the PC as a persistent presence across sessions.

Companions have three defining properties:
1. **Personal scale presence:** Participate in scene-level action — combat, Corroborate in contests, assist fieldwork.
2. **Persistent tracking:** State (Disposition, Wounds, Coherence) tracked between sessions; not reset at scene end.
3. **Narrative investment:** Death, departure, or betrayal fires a dedicated departure scene (not a generic consequence).

### §1.2 Companion vs. Recruited NPC

| Property | Companion | Recruited NPC |
|----------|-----------|---------------|
| Scale | Personal (scene-level) | Faction (BG-level) |
| PC proximity | Travels with PC | Operates within faction structure |
| Relationship ending | Departure scene (major beat) | Mandate −1 (talent drain) |
| Combat | Active personal combat | Commands units, not present personally |
| Disposition tracked | To PC personally | To faction |
| Source | Disposition ≥ +3 through organic play | Recruitment roll (npc_behavior §9.5) |
| Maximum active | 2 simultaneously | Unlimited |

A single NPC may be both — the officer-governor path (mass_battle §D.2) produces exactly this. Companion role governs personal-scale; Recruited role governs faction-scale.

### §1.3 Maximum Companions

Maximum **2 active Companions simultaneously.** A third requires releasing one existing Companion first (departure scene required for the released Companion).

---

## §2 ACQUIRING A COMPANION

### §2.1 Eligibility

NPC becomes eligible at **Disposition ≥ +3** through:
- **Officer path:** Unit officer reaching Disposition +3 through battle service (mass_battle §D.2).
- **Social path:** Any named NPC reached through sustained social fieldwork or crisis intervention.
- **Knot path:** Any NPC who forms a Close Knot — relational intimacy equivalent to Companion eligibility.

### §2.2 Companionship Scene

When eligibility is reached: Priority 1 Scene Slate entry fires. Player may attend or decline. Scene structure:
1. **Moment of truth:** NPC states why they want to travel. Conviction governs framing.
2. **PC response:** Acceptance (Companion activated) or decline (NPC remains allied at Disposition +3).
3. **On acceptance:** Player and GM agree on the Companion's role (guardian, advisor, scout, practitioner).

---

## §3 COMPANION STATS

### §3.1 Officer-Path Stat Generation

| Stat | Formula | Notes |
|------|---------|-------|
| Agility | floor(faction Military ÷ 2) | 1–3 |
| STR | floor(faction Military ÷ 2) | 1–3 |
| Endurance | floor(faction Military ÷ 2) + 1 | 2–4 |
| Cognition | 2 | Military professional baseline |
| Charisma | 2 | Functional but not exceptional |
| Spirit | 2 | Grounded |

**Combat Pool = (Agility × 2) + History bonus + 3.** History: Combat/Military 2 pts = +2D. Pool at Military 4 faction: (2×2)+2+3 = 9D.

**Wound Interval = Endurance + 6.** At Endurance 3: WI = 9. Max Wounds = 2. Fragile by PC standards — correct for a companion who should feel vulnerable.

**Weapon:** Default Medium Blade (Long Heavy Blade, TN 7), or faction standard. Armour: Medium. Upgrade to Heavy: Wealth −1 once from PC.

### §3.2 Social-Path Stat Generation

Named NPCs: GM assigns stats consistent with established characterisation (Vaynard: Cognition 5, Agility 2; Vossen: Charisma 5, Agility 3). Procedural social companions use default: Agility 2, STR 2, Endurance 3, Cognition 3, Charisma 3.

### §3.3 Practitioner Companions

| NPC | TS | Starting Coherence |
|-----|-----|-------------------|
| Edeyja | 50+ | 7 (damaged from warden work) |
| Maret Uln | 35 | 10 |
| Torsvald | 20+ | 8 |

Practitioner companions perform Thread operations per threadwork_v30. PC is responsible for declaring Companion Thread intent in Phase 1.

---

## §4 COMPANION COMBAT AI

### §4.1 Priority Tree (When PC Does Not Direct)

| Priority | Condition | Action |
|----------|-----------|--------|
| 1 | Wounds ≥ Max Wounds − 1 | Full Guard. Do not attack. |
| 2 | PC attacked by 2+ opponents AND no supporting ally | Rescue (minimum 3 dice committed). |
| 3 | PC is Wounded AND Companion Conviction aligns with PC | Strike highest-threat opponent to PC. Full Off minus 4D Def. |
| 4 | PC winning (holds initiative) | Standard split: floor(pool/2) Off, rest Def. Same target as PC. |
| 5 | Default | Nearest opponent. Equal Off/Def split. |

PC direct control (Phase 1 declaration) overrides the AI tree.

### §4.2 Fibonacci Contribution

A Companion attacking the same target as the PC contributes the Fibonacci group bonus (+1D Off per additional attacker per combat §8). The Companion is a genuine tactical asset, not flavour.

### §4.3 Proxy Command (Companion when PC General incapacitated)

| Roll | Pool | Ob | On Success | On Failure |
|------|------|-----|-----------|-----------|
| Command re-establish | Cognition + relevant History | 3 | Units fight under Companion's Command = floor(Military/2) | Units fight at 1D minimum |

Ob 3 (harder than PC's Ob 2 — Companion lacks full authority). Intentionally low success probability (~12% for Cognition 2): Companion is not a general replacement.

---

## §5 COMPANION MASS COMBAT ROLE

### §5.1 Tier Table

| Disposition | Capability |
|------------|-----------|
| +3 | Commands assigned unit. PC Morale Effect (+1 Discipline) applies to Companion's unit even when PC is in personal combat. |
| +4 | Sub-commander: unit fights under Companion's Command rating independently of PC's split. Companion's unit generates 1 extra Co-Movement draw at Cascade if it fought this turn. |
| +5 | All of +4. Auto-stabilise PC (Stage 1 incapacitation) once per battle — no Medicine action required. |

### §5.2 Tactic Capability as Sub-Commander (+4)

| Tier | Tactics | Roll |
|------|---------|------|
| Tier 1 | Standard Advance, Disciplined Defence | Automatic |
| Tier 2 | Feigned Retreat, Hammer & Anvil, Refused Flank | Ob 2 Command check |
| Special | Envelopment, Ambush | Not available |

### §5.3 PC Embedding Amplification

When both PC and Companion are in the same territory during Strategic Phase: the +1D BG embedding bonus (scale_transitions §9) applies to **two** Domain Actions instead of one. Maximum 2 Domain Actions per season receive embedding bonus.

---

## §6 COMPANION DEPARTURE

### §6.1 Departure Conditions

| Condition | Type | Scene |
|-----------|------|-------|
| Killed in combat | Combat death | Departure scene + death cascade (combat §13.3) |
| Belief contradiction: 3 Scars as Companion | Conviction departure | Departure scene: final appeal roll (1 contest exchange). Success = stays + Scar cleared. Failure = leaves. |
| Player voluntarily releases | Voluntary | Farewell scene. No death cascade. Disposition maintained. |
| Rival faction recruitment succeeds | Defection | Departure scene. Counter-offer eligible (npc_behavior §9.5 incentive table). |
| PC faction collapses (Stability 0) | Dissolution | Companion becomes unaligned. May rejoin without new companionship scene when faction reconstitutes. |

### §6.2 Departure Scene

Priority 0 (mandatory) fires on any non-voluntary departure. Scene structure by type:

*Combat death:* Aftermath aftermath choice (§D.1) applied to companion specifically. Tend the Wounded Ob 3 (harder — Companion is more severely wounded). Success: incapacitated, removed from active service until next session's scene. Failure: confirmed dead, death cascade fires.

*Conviction departure:* NPC states violated Belief. Player's final social appeal: 1 contest exchange. Success: NPC stays + Scar cleared. Failure: NPC leaves.

*Defection:* Player may counter-offer at same incentive tier as rival. Success: Companion stays. Failure: departs.

### §6.3 Grief Mechanic (Optional, GM discretion)

On Companion death at Disposition ≥ +4: PC enters Grief for 1 season. All social rolls involving Conviction statements: +1 Ob. Clears when PC has 1 scene explicitly processing the loss.

---

## §7 COMPANION SCENES AND BONUSES

### §7.1 Scene Generation

Companions generate scenes through:
1. **Arc triggers:** Companion Arc Trigger (scale_transitions §4.3.2) fires mandatory scene when companion's arc branch condition is met.
2. **Outreach:** Companion at Disposition +3/+4 may initiate Outreach (npc_behavior §8.11.4) when scene slot is open. Companion Outreach prioritised over non-Knotted NPC Outreach.

### §7.2 Bonuses in Scenes

| Scene type | Bonus |
|-----------|-------|
| Investigation fieldwork | +1D at Disposition +4 (max +1D regardless of Companion count) |
| Social contest (Corroborate) | Ob 1 if Knot present (standard Corroborate rule) |
| Expedition/movement | −1 time unit to scene cost at Disposition +3 |
| "Where Were You?" retrospective | Companion delivers news filtered through their Conviction |

---

## §8 CANON COMPLIANCE

| Constraint | Status |
|-----------|--------|
| mass_battle §D.2 (officer → companion path) | Codified in §2.1 |
| npc_behavior §9.5 (recruitment vs companion) | Distinction in §1.2 |
| scale_transitions §4.3.2 (Companion Arc Trigger) | §7.1 |
| scale_transitions §4.4 (companion in retrospective scenes) | §7.2 |
| combat §13.3 (death cascade) | §6.1 |
| social_contest §4 Step 2b (Corroborate) | §7.2 |

---

## §9 PROPAGATION

| File | Change |
|------|--------|
| references/canonical_sources.yaml | Add companion_specification entry |
| designs/mass_combat/mass_battle_v30.md §D.2 | Update forward reference: companion_specification_v30 §2.1 exists |
| references/params_factions.md | Companion stat tables |
