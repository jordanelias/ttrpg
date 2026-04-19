<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: social_contest_v30_infill.md -->

<!-- v30 baseline — renamed from designs/contest/social_contest_system_v2.md on 2026-04-13 -->
# VALORIA — SOCIAL CONTEST SYSTEM v2
## [EDITORIAL: ED-136 — System name: "Contest" proposed. Candidates: Contest, Contention, Proceeding.]
## Patches applied: PP-234, PP-235, PP-236, PP-237, PP-272, PP-278, PP-279
## Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance). Supersedes debate_system_redesign_v1.md Part 6.
## Source: Opus 4.6 session 2026-04-04
## Patch: PP-234 (genre restructure, attribute renames, Composure resolution, faction boost revision, dice consistency)
## Three-mode: TTRPG (§§1–9), Board Game (§10), Hybrid (§11)

### Attribute renames
- Memory → Recall (Rec). "Memory" freed for genre name.

### Genre restructure
- Three genres (Past/Present/Future) → two genres (Memory/Projection).

---

## §1 CORE PRINCIPLE: FORMAT FOLLOWS CONTEXT




---

## §2 GM SETUP (Before Contest Begins)

**Step 1 — Determine adjudicator type:**

| Type | Who decides | Examples | Primary attribute |
|---|---|---|---|
| Expert judge | A single authority evaluates arguments on merits | Royal Audience, Church Tribunal, Guild Arbitration | Cognition |
| Crowd | A collective audience reacts to delivery and force | Parliamentary session, public forum, street crowd | Charisma |
| No adjudicator | The parties themselves are the decision-makers | Private negotiation, personal appeal | Attunement |
| Panel | Multiple individual judges deliberating | [EDITORIAL: ED-137 — panel mechanics not yet designed. Use Expert Judge as provisional.] | Cognition |

The adjudicator type determines the primary attribute for the Argue pool (§4, Step 3). The adjudicator type is **fixed for the duration of a contest.** If circumstances change enough to shift the adjudicator type (a private negotiation goes public), the current contest ends and a new contest begins under the new type.

**Step 2 — Determine primary genre from the question:**

| Question shape | Primary genre |
|---|---|
| "Did X happen? Was X done? What was established?" | Memory |
| "Should we do X? What will follow? What should become?" | Projection |


**Step 3 — Set genre and orientation dice:**

Base: orators arguing in the primary genre receive +1D. Orators arguing in the non-primary genre receive +0D.

Audience boost: the dominant faction's boost adds +1D to any argument matching their boosted axis. A faction boosts ONE of four options (one genre OR one orientation, not both):

| Faction | Ethical Mode | Boost | Axis |
|---|---|---|---|
| Church | Divine Command | Obscuring | Orientation |
| Crown | Virtue Ethics | Revealing | Orientation |
| Varfell | Consequentialism | Projection | Genre |
| Hafenmark | Categorical Imperative | Memory | Genre |
| Restoration | Rawlsian Social Contract | Revealing | Orientation |
| Guilds | Moral Relativism | GM picks one | Either |
| Löwenritter | Duty-based (if emerged) | Projection | Genre |
| Niflhel | — | GM picks one | Either |

An orator's total bonus dice from genre + audience: maximum +2D (primary genre +1D AND audience boost matches on the other axis +1D). Minimum +0D (non-primary genre, audience boost doesn't match).

These dice are added to the Argue pool at Step 3 of each exchange. They are fixed at setup — no mid-contest changes.

**Step 4 — Set Conviction Track:**
- Scale: 0–10. Side A wins at ≥ 7. Side B wins at ≤ 3. Compromise zone: 4–6.
- Starting position: GM-set (typical neutral: 5).
- Audience resistance: average Stability of represented factions, round up, then −1 (minimum 0). Typical range: 0–2.
- With no adjudicator (private negotiation, personal appeal): Conviction Track is optional. If not used, winner determined by exchange majority. If exchange majority is tied, the contest stalls: strain persists, all Read results from the contest become permanent knowledge (the parties learned things about each other that cannot be unlearned), and the relationship is stressed. The narrative moves forward — the failure to agree IS a consequential outcome.

**Step 5 — Set exchange count and role structure:**

| Proceeding Type | Exchange Count | Role Structure | Audience Resistance Modifier |
|---|---|---|---|
| Formal Contest (Parliament) | 3 | Alternating | Standard |
| Grand Contest (faction-defining) | 5 | Alternating | Standard |
| Royal Audience | 3 | Crown objects throughout | Halved for petitioner |
| Church Tribunal | 1–5 (Inquisitor sets) | Inquisitor proposes throughout | Halved for accused |
| Guild Arbitration | 3 | Symmetric before arbiter | Standard |
| Casual Dispute | 1 | Initiator proposes | N/A (no tracker) |
| Private Negotiation | 1–3 | Symmetric | N/A (tracker optional) |
| Personal Appeal | 1 | Appealer proposes | N/A (tracker optional) |


**Step 7 — Record all above in the hidden GM ledger.**

---

## §3 ARGUE POOL CONSTRUCTION

The primary attribute for the Argue roll shifts based on the adjudicator type.

**Argue Pool = (Primary Attribute × 2) + History bonus**

| Adjudicator Type | Primary Attribute | Reasoning |
|---|---|---|
| Expert judge | Cognition | Judge evaluates logical structure |
| Crowd | Charisma | Crowd responds to delivery and authority |
| No adjudicator | Attunement | You must read the other party and calibrate |
| Panel | Cognition | [PROVISIONAL — ED-137] |

TN: 7 (Standard). Situational modifiers per core engine (TN 6 Controlled, TN 8 Desperate) apply as normal.

This follows the same pool construction pattern as combat: Combat Pool = (Agility × 2) + weapon proficiency History + 3. The doubled attribute makes the primary attribute the dominant factor, with History providing depth of experience. The +3 constant from combat and general skill rolls is included in the History bonus formula (History bonus = points + 3, per §4.1 of Stage 2).

The Appraise step (§4, Step 1) always uses Attunement regardless of adjudicator type. Appraising the audience or opponent is always an act of empathetic perception. (PP-278)


---

## §4 EXCHANGE STRUCTURE

**Step 1 — Appraise (both orators) (PP-278):**
Roll Attunement alone (no History), TN 7, Ob 1.

Each exchange's Appraise senses the CURRENT state of the audience (which may have shifted from Doubt Markers, track movement, or strain). This is not a re-attempt of the same question — it is a fresh perception of changed circumstances.

| Appraise Net Successes | Information |
|---|---|
| Failure (0) | Misleading signal: GM identifies a wrong boost as the audience's actual boost |
| Partial (1) | Boosted axis type identified (genre or orientation) but not which specific one |
| Success (2) | Full boost identified (e.g. "this audience favours Revealing") |
| Overwhelming (3+) | Boost identified + one specific detail: a key individual's Belief, the audience's resistance threshold, or the opponent's emotional state |


**Step 2b — Corroborate (optional):** A corroborator present at the contest may declare support before the Argue roll. On success: primary orator gains +1D for this exchange. Corroborator must be a declared coalition member (Knot not required). Knot-sharing corroborators roll at Ob 1; non-Knot coalition members roll at Ob 2. In asymmetric proceedings: all corroborators for the disadvantaged party use Ob 2 regardless of Knot. (PP-257) On failure: corroborator takes 1 strain.

**Step 3 — Argue:**
Initiative holder declares argument and rolls first. Respondent hears, then declares and rolls.

Pool: (Primary Attribute × 2) + History bonus (per §3), TN 7.
Add genre/orientation bonus dice per §2 Step 3 (primary genre +1D; audience boost match +1D; max +2D total).
Recall bonus: +2D when citing a specific, named, verifiable claim (document, date, prior statement, named precedent). Binary. Available in either genre.

**Grand Contest Recall (PP-NEW, ED-617):** In Grand Contests (5-exchange format), the Recall bonus (+2D) applies *once per cited source for the entire contest*, not once per exchange. After Recall is used for a specific document, date, or named precedent, that source is exhausted and cannot generate a new Recall bonus in later exchanges. The orator must cite a different source to claim Recall in subsequent exchanges. This prevents pool-compounding from repeating a single high-quality citation across all five exchanges. Formal Contests (3 exchanges) retain per-exchange Recall (shorter format makes source-cycling mechanically impractical).
Momentum: before rolling, spend any amount of Momentum to add automatic successes (1 Momentum = 1 success, per core engine §1.7).

**Step 4 — Resolve by interaction type:**

**CLASH** (same genre, opposite orientation):
Direct contest within the same temporal horizon.
- Compare successes. Higher wins. Margin = difference.
- If margin > resistance → Conviction Track moves (margin − resistance) toward winner's position.
- If margin ≤ resistance → 0 movement.
- Strain to loser: margin + Charisma modifier of winner − Focus defence of loser. **Minimum 0.** [Matches combat damage minimum 0. Focus defence can fully absorb strain just as armour can fully absorb damage.]
- Charisma modifier: max(0, floor((Charisma − 3) ÷ 2)) → Cha 1–3: +0; Cha 4–5: +1; Cha 6–7: +2.
- Focus defence: floor(Focus ÷ 2) → Foc 1: 0; Foc 2–3: 1; Foc 4–5: 2; Foc 6–7: 3.

**REINFORCE** (same genre, same orientation):
Both orators push in the same direction within the same temporal horizon.
- Same resolution as CLASH.
- Strain to loser: (margin − 1, minimum 0) + Charisma modifier − Focus defence. Minimum 0.

**CROSS** (different genres):
- No direct comparison. Each argument evaluated independently.
- Effective margin for each = floor(successes ÷ 2).
- For each side: if effective margin > resistance → that side moves the track (effective margin − resistance) toward their position.
- Net track movement = difference between the two movements; direction toward the side with larger movement.
- Obscuring in CROSS: if the side with larger movement used Obscuring, place a Doubt Marker on the opponent instead of track movement.
- No strain dealt. Neither argument attacked the other.
- Initiative stays with holder.

**TIE** (equal successes, any interaction type):
- Both orators take 1 strain. **Exception (PP-236): if the interaction type is CROSS, no strain is dealt — CROSS no-strain rule takes precedence. Neither argument attacked the other; a tie does not change that structural fact.**
- Conviction Track moves +1 toward initiative holder's position.
- Initiative stays with holder.

- Conviction Track does not move toward winner.
- Place a Doubt Marker on the opponent.
- Doubt Marker effect: opponent's next winning exchange has its margin reduced by 2 before resistance is applied (minimum 0).
- Only one Doubt Marker active at a time. New replaces old.
- Consumed on use.

**Step 5 — Forfeit actions:**
- **Regroup:** Forfeit exchange. No argument, no strain. Conviction Track moves +1 toward non-forfeiting side. Concentration restores to max (Focus × 3).
- **Concede a Point:** Forfeit exchange. Take 1 strain. Conviction Track moves +1 toward non-forfeiting side. Gain +1D on next exchange.

**Step 6 — Strain and Concentration:**

**Composure = Charisma × 3.** Range 3–21. Social damage buffer before Rattled. [ED-127 resolved, ED-694 updated. Single attribute × multiplier. Strain, Charisma modifier, and Focus defence all scaled ×3 to match. Equipment (attire, regalia) adds flat Composure.]

- Strain accumulates toward Composure threshold.
- All subsequent contest rolls: +1 Ob per Rattled level (cumulative).
- Rattled recovery: 1 mark clears per full scene of non-social activity or rest.
- Composure recovery: full restore at scene change (new location, new interlocutors).

**Concentration = Focus × 3.** Range 3–21. Depletes by 3 per exchange, −3 additional on exchange loss. (ED-694: Recall removed — Recall's role is the +2D citation bonus in Argue, not sustained focus.)
- At Concentration 0: **Spent** — next exchange: −2D to all rolls; opponent gets +1D. Then resets to maximum.
  **Spent timing:** Concentration is checked after Step 4 (CLASH/REINFORCE resolution). If Concentration reaches 0 at Step 4, Spent is entered immediately — but the penalty applies to the *next* exchange, not the current one (the triggering exchange has already rolled in Step 3). Spent resets to Focus × 3 after the penalty exchange resolves.
- If both Rattled and Spent active: penalties cumulative. Pool minimum 1D per core engine.

**Step 7 — GM records exchange on hidden ledger.**

---

## §5 INITIATIVE

- Exchange 1: **Rolled** — both orators roll Attunement, TN 7, Ob 1. Higher net successes acts last (declares second; information advantage). On tie: higher Attunement stat wins. On stat tie: neutral party (adjudicator) assigns. (ED-581 resolution: rolled initiative aligns with combat initiative for cross-system consistency. The roll adds variance to opening exchanges — a less attuned orator can occasionally seize the read.)
- Subsequent exchanges: transfers to exchange winner.
- On tie: stays with current holder.

---

## §6 POST-CONTEST RESOLUTION

- GM reveals ledger.
- Conviction Track ≥ 7 = Side A wins; ≤ 3 = Side B wins; 4–6 = compromise (GM narrates partial outcome proportional to final position).
- No Conviction Track (private): exchange majority determines winner. Tie = stall with consequences (see §2 Step 4).

**Thread co-movement by winning genre:**

| Genre Won | Thread Consequence |
|---|---|
| Memory | Temporal co-movement (retention shift). The audience re-experiences cited configurations. Observers with Thread Sensitivity (TS) 30+ perceive thread-shimmer. Rendering Stability (RS) +1. |
| Projection | Actualization co-movement (protention anchor). The argued future becomes a probability anchor. +1D on the first Domain Action pursuing that outcome within the season. RS +1 if the projection involves Thread-sensitive matters. |


**Domain Echo:**
- Decisive win + Memory genre: winning faction's Mandate +1 in the domain of the cited precedent.
- Decisive win + Projection genre: +1D on first Domain Action pursuing the argued outcome within the season.
- Compromise: no Domain Echo.

**Total Victory** (Conviction Track ≥ 9 or ≤ 1): losing primary orator gains Contest Fatigue (−1D next social roll, one instance per session, clears at next session start if unused). Winning orator gains +1 Momentum (if below cap 4). Disposition change with all witnesses; Reputation shift (GM-set magnitude). In Board Game (BG) Parliamentary Vote: losing coalition's dominant faction takes Mandate −1 for one season.

**Post-contest recovery:** all strain and Concentration depletion clear at scene end. Spent clears at scene end. RS changes subject to RS ceiling (100) and RS=0 lockout.

### §6.1 Obligations (NEW — post-contest binding commitments)

**GM advisory — Obligation tracking (ED-619):** GMs are advised to cap active Obligations at 3 simultaneously across all parties for tracking tractability. Beyond 3 active Obligations in the same campaign season, use a dedicated ledger rather than session notes. The system allows any number of concurrent Obligations; the cap is a GM guidance note, not a mechanical limit.

A Decisive win (Conviction Track ≥ 7 or ≤ 3) in a Formal or Grand Contest produces a binding **Obligation** — a mechanical commitment that persists across seasons. The Obligation is the contest's lasting consequence in the game world, not just a stat change.

**Obligation structure:** The winning side names one specific commitment that the losing side must honor. The commitment must be achievable and verifiable (not "be good" but "withdraw Templars from Gransol within 2 seasons").

| Contest Type | Obligation Duration | Violation Consequence |
|-------------|--------------------|--------------------|
| Formal Contest (Parliament) | 2 seasons | Violating faction: Mandate −1. Reputation shift. Contest Fatigue on faction leader. |
| Grand Contest | 4 seasons or until a specified game-state condition changes | Violating faction: Mandate −2. Stability −1. Faction's next DA targeting the violated party faces +2 Ob (institutional credibility lost). |
| Royal Audience | 2 seasons (Crown-imposed) | Crown Mandate −1 on violation (the Crown's word is broken). |
| Church Tribunal | Until formally revoked by Church authority | Heresy Investigation acceleration. Excommunication eligible. |

**Settlement-targeted Obligations (per settlement_bridge_unification C-08):** Obligations may target specific settlements instead of provinces. Examples: "Church must not station Inquisitors in S-017 Gransol Market Quarter for 2 seasons"; "Crown must maintain Defense ≥ 2 in S-006 Lowenskyst Fortress"; "Varfell must not develop Prosperity in S-032 Oastad Shrine." Settlement-targeted Obligations use the settlement stat as the verification condition. Violation consequences are the same as province-level Obligations.

**Obligation tracking:** Obligations are tracked as clocks per clock_registry_v30. Each Obligation has: source (which contest), parties (who is bound), commitment (what must be done or not done), duration (seasons remaining), and violation trigger (what constitutes breach).

**Player Obligations:** When the player loses a contest, they receive an Obligation. The player is not forced to comply — they may violate it. Violation consequences apply: the player's faction loses Mandate, the player loses Reputation, and the NPC who won the original contest gains Disposition +1 toward the player's rivals (the violation justifies their position).

**NPC Obligations:** When an NPC faction loses a contest and receives an Obligation, the NPC priority tree is modified: any action that would violate the Obligation is blocked for the Obligation's duration unless the faction enters Survival priority (Stability ≤ 2). This means a won contest has lasting strategic impact — the player can constrain an NPC faction's behavior through political victory, not just stat changes.

### §6.2 Conviction Scar Visibility (NEW — player-facing)

When a player's contest argument produces a Conviction Scar on an NPC (per npc_behavior_v30 §3.2 — decisive outcome via Resonant Style targeting with Conviction engagement), the player receives a narrative signal. The GM states: "Something shifted in [NPC]'s expression. Your argument reached something they cannot dismiss." This is not a stat reveal — the player does not learn the Scar count. They learn that their words had structural impact.

**Videogame implementation:** NPC portrait shows a subtle visual indicator (a crack, a flicker, a moment of instability) when a Scar is produced. The indicator is momentary — it does not persist on the portrait. The player must remember that they wounded this NPC's conviction. If they Appraise in a future contest, the Scar count is revealed per npc_behavior §3.1 (Appraise Overwhelming: one Conviction revealed).

### §6.3 Chain Contests (NEW — unresolved tension generates follow-up)

When a contest ends in Compromise (Conviction Track 4–6), the tension is deferred, not resolved. The unresolved contest generates a Scene Slate entry for the following season per player_agency_v30 §4.2 (Priority 1 — the unresolved political tension is a crisis event).

**Chain contest rules:**
- The follow-up contest starts at the Conviction Track's final position from the previous contest (not reset to 5). If the first contest ended at Track 4, the chain contest starts at Track 4.
- All strain and Concentration reset normally between sessions.
- Disposition changes from the first contest carry into the second.
- The NPC's Scar count from the first contest persists — accumulated wounds do not heal between chain contests.
- A chain contest's Decisive win produces an Obligation (§6.1) as normal. A second Compromise extends the chain — another follow-up Scene Slate entry for the next season.

**Resistance stall-break (ED-582):** If two consecutive exchanges in a chain contest produce zero track movement (both sides' margins ≤ resistance), the contest enters Deadlock. In Deadlock:
- Resistance for both sides drops by 1 (minimum 0) for the remainder of this contest.
- If a third consecutive zero-movement exchange occurs after the Resistance drop, the contest ends immediately as a Compromise at the current track position.
- Rationale: prolonged mutual stonewalling exhausts the audience's patience. The institutional pressure forces resolution or capitulation.
- Maximum chain length: 3 contests. After 3 consecutive Compromises, the tension resolves as a permanent stalemate: both parties establish a cold equilibrium. Disposition freezes at current level. Neither party can initiate a contest on this topic for 4 seasons.

---

## §7 ASYMMETRIC PROCEEDINGS


**Asymmetric proceedings (Church Tribunal, Royal Audience, Inquisition):**
- Institution assigns Proposer/Respondent roles. Roles do NOT alternate.
- Disadvantaged party (accused, petitioner) faces halved resistance (round up) when moving the Conviction Track.
- Advantaged orator accumulates 0 strain from CROSS exchanges.
- CLASH strain applies normally when advantaged side loses.

**Church Tribunal specifics:** Accused has no corroboration. Exchange count set by Inquisitor (1–5). (PP-272: 'Division' stricken — term was vestigial from an earlier parliamentary design pass; it has no mechanical definition in the current system.) Conviction Track starts biased at 6. Church boosts Obscuring — the Inquisitor's arguments that foreclose the accused's epistemic standing carry institutional weight.

---

## §8 DERIVED VALUES SUMMARY

| Value | Formula | Range | Parallel |
|---|---|---|---|
| Composure | Charisma × 3 | 3–21 | Vitality = Endurance × 10 (ED-694) |
| Charisma modifier | max(0, floor((Cha − 3) ÷ 2)) × 3 | 0–6 | — |
| Focus defence | floor(Foc ÷ 2) × 3 | 0–9 | Armour Rating (damage reduction), scaled ×3 |
| Concentration | Focus × 3 | 3–21 | Maximum = Focus × 3 (Regroup restores to max). Recall removed — no conceptual link to sustained focus. (ED-694) |
| Appraise pool | Attunement only | 1–7 | — |
| Argue pool | (Primary Attribute × 2) + History bonus | Variable | Combat Pool = (Agility × 2) + History + 3 |

---

## §9 ADDITIONAL TTRPG RULES

### §9.1 Pre-Contest Preparation
Available when an orator has deliberate preparation time. Not available for impromptu contests.

Pool: Attunement + most relevant History, TN 7, Ob 1.

| Degree | Effect |
|---|---|
| Failure / Partial | No effect |
| Success | +1D on Exchange 1 Argue roll |
| Overwhelming | +1D on Exchange 1 Argue roll AND Exchange 1 Appraise uses TN 6 |

Time requirement: at least 1 hour. Rushed (< 1 hour): TN 8.

**Evidence Track Findings as preparation (F-TRANS-11):** Findings from a completed fieldwork investigation may be cited in the Contest opening. Each Finding cited grants +1D on Exchange 1 (maximum +2D from Findings, regardless of count). Findings are not consumed by citation — they remain on the Evidence Track for future use. Finding citation must be declared at contest setup (GM sets scope: the Finding must be relevant to the contest's subject matter). This bonus stacks with standard preparation (+1D), for a maximum Exchange 1 bonus of +3D when both are available. Requires prior multi-scene investigation to produce Findings. Reference: fieldwork_investigation.md §2.3, §4.1.

### §9.2 Multi-Party Contest — Coalition Structure
Each orator declares Side A or Side B at setup. No side-switching. Each side nominates one Lead per exchange (may change between exchanges). Non-lead coalition members may Corroborate (max 1 per side per exchange). Composure and Rattled tracked individually. **Coalition Concentration — shared pool (PP-237):** Concentration tracks on a shared pool equal to the sum of all coalition members' (Focus + Recall) at contest setup. Each exchange depletes the shared pool by 1 (plus 1 on exchange loss) regardless of which member holds Lead. Rotating Lead does not reset depletion. Spent triggers at 0; pool resets to its setup total. Initiative transfers to winning side; that side nominates holder.

### §9.3 Practitioner Weaving in Contests (R-65)
A practitioner with TS ≥ 30 in active Thread contact adds bonus dice: floor(TS ÷ 30) (+1D at 30, +2D at 60, +3D at 90). Must declare before rolling. Visible to all observers. Church may file Heresy Investigation on observation. After exchange: Coherence check Ob 1.

### §9.4 Thread Operations Between Exchanges
A practitioner may initiate a Thread operation between exchanges. Effects apply before next exchange's Read step. Genre/orientation dice are fixed at setup — Thread operations cannot change them mid-contest. Temporal axis conflict: if the Thread operation's temporal axis contradicts the contest's primary genre (Memory-axis operation during Projection-primary contest, or vice versa), both orators' Read rolls in the next exchange use TN 8.


**Temporal Axis Conflict (PP-351):** If a practitioner initiates a Thread operation on a temporal axis that opposes the contest's primary temporal orientation (e.g., a Past-axis operation during a Future-primary contest, or vice versa), the resulting temporal dissonance imposes TN 8 on both orators' next Read roll. This applies regardless of which side the practitioner supports — temporal contradiction disrupts the entire epistemic field. Same-axis operations and non-temporal Thread operations (Object-scale, Relational without temporal component) are unaffected.
### §9.4b Adjudicator Thread Response (ED-667)

When an adjudicator (NPC presiding over formal proceedings — Court, Tribunal, Parliamentary Session, Church Inquiry) witnesses Thread use during the proceeding:

| Adjudicator Certainty | Response |
|---|---|
| C5 (Orthodox) | Declares proceedings **corrupted**. Contest immediately suspended. Church Heresy Investigation fires (existing PP-182 pathway). Adjudicator's Faith Conviction receives Scar per §3.4 of npc_behavior_v30. Results from the corrupted exchange are voided — last exchange before Thread use stands as final. |
| C4 (Faithful) | Declares **irregularity**. Current exchange result stands but adjudicator applies +1 Ob to all subsequent rolls by the Thread-using party (procedural suspicion). Church Investigation optional (adjudicator discretion based on Scar count). |
| C3 (Questioning) | Notes the event. No procedural consequence. Adjudicator's internal conflict deepens — Conviction Scar check per §3.4. May influence post-contest Disposition shift toward the Thread-using party (curiosity or fear, GM judgment). |
| C2–0 (Skeptic to Accepted) | No procedural response. Thread use is understood as part of reality. If adjudicator has TS ≥ 30: may privately note the Thread-user's technique as relevant evidence (adds +1 to Evidence Track if investigation active). |

**Scope:** This applies only to formal adjudicated proceedings (Court, Tribunal, Parliamentary Session, Church Inquiry). Informal debates, tavern arguments, and private conversations are not adjudicated and do not fire this response.

**Visibility gate:** Adjudicator must perceive the Thread use. Per threadwork_v30 §2.3 visibility table: TS 0–9 perceives nothing; TS 10–29 perceives vague unease (triggers at C5 only if adjudicator is already suspicious); TS 30+ perceives the operation. If the practitioner successfully conceals (Cognition roll per §2.3), adjudicator does not respond.

---

### §9.5 Beliefs Integration
Winning an exchange while arguing for a position aligned with the orator's stated Belief counts as a Belief achievement for Momentum. Max 1 Momentum per contest from Belief alignment.

### §9.6 Forced Unmask

### §9.7 Niflhel Social Toolkit
Niflhel cannot participate in Formal or Grand Contests. Their social toolkit:
- Private negotiation: one-on-one only; Attunement-primary pool (per §3 "no adjudicator"); TN 7; Ob = floor(target Stability / 2) + 1.
- Thread Insight (TS ≥ 30 only): Attunement read before negotiation reveals one unstated position.
[EDITORIAL: ED-041 — full Niflhel social toolkit pending design.]

---

## §10 BOARD GAME PARLIAMENTARY VOTE

Faction-level contest resolution for BG scale. To zoom into personal scale, use §11 (Hybrid).

### BG Vote Setup
1. Each faction declares Side A or Side B. Non-declaring factions Abstain.
2. Each side declares one genre (Memory or Projection).
3. Resistance: base 0. If a faction with Stability ≥ 6 Abstains: +1 resistance (max +2).
4. Starting Conviction Track: 5 ± lobbying offset. Each successful Diplomacy action targeting this vote in preceding season: +1 toward lobbying side (max ±2).

**Lobby cap — BG mode (ED-621):** The lobbying offset is restricted to the compromise zone at BG Vote start. Maximum starting Conviction Track: 6. Minimum starting track: 4. Lobbying cannot predetermine a vote — it provides advantage, not a guaranteed outcome. This matches the Hybrid mode restriction (§11 / PP-256). Example: if lobbying would push the track to 7, it is capped at 6.

### BG Vote Resolution
Pool: sum of Mandate of all factions on each side. Roll combined pool TN 7.
Genre bonus: +1D if the side's genre matches the primary genre of the question.
Audience boost: +1D if the side's genre matches the Parliament's dominant faction boost. [Orientation boost does not apply at BG scale — factions vote publicly.]

Each side: if net successes > resistance → movement = successes − resistance.
Net track movement = difference; direction toward the larger side.
Conviction Track ≥ 7 = motion passes; ≤ 3 = motion fails; 4–6 = referred to committee.
Zero-zero: if both sides fail to exceed resistance, motion referred to committee.
Thread consequences do not fire from BG Parliamentary Vote (personal-scale argument required).
Total Victory: Conviction Track ≥ 9 or ≤ 1 → losing coalition's dominant faction takes Mandate −1 for one season.

---

## §11 HYBRID CONTEST

1. **BG layer:** run one round of BG Parliamentary Vote (§10). Apply Conviction Track offset, capped at ±2 from neutral. Per PP-256, BG lobbying offset is restricted to the compromise zone (4–6 at Hybrid session start); the BG layer cannot produce a final resolution — the TTRPG layer always runs.
2. **Set TTRPG starting Conviction Track:** 5 ± capped BG offset, clamped to compromise zone (4–6).
4. **Resolution:** final TTRPG Conviction Track position determines outcome. Thread consequences may fire.

---

## §7.1 Excommunication Tribunal (ED-625 — approved 2026-04-17)

Special Asymmetric Proceeding (§7) initiated by Church. Prerequisites: TC ≥ 40, Church Mandate ≥ 4, Evidence Track ≥ 3 on target from prior HI OR documented Obligation violation OR 2 prior Tribunal convictions.

**Modifications vs standard §7:**
- Conviction Track starts at **7** (Church near-decisive before Exchange 1 — institutional fait accompli)
- No accused corroboration permitted
- Exchange count: 1–3 (set by Inquisitor)
- Resistance for accused: halved (same as standard)

*The correct strategic counter is preventing the filing, not defending at Tribunal. See §10.1 Parliamentary Stay. Filing can be prevented while TC < 55.*

**Consequences on success:**
- Named NPC: TC +4; target Mandate −2; Certainty forced to min(current, 2); arc transition; all NPCs Disposition ≥ +1 to target check Certainty Ob 1 or lose Disposition −1.
- Player Character: Faction Mandate −3; excluded from Parliamentary motions; Standing −2; Faith-conviction Companions make departure scene check (Scar 1).
- Faction: Mandate −2; all Church Domain Actions vs faction Ob −1; TC +3.

**Revocation — Act of Contrition:** Church declares (Mandate ≥ 5, TC ≥ 50 required). Target fulfils Obligation abjuring the violation. Result: Church Mandate −1, TC −1, Excommunication lifted.

---


**Church Self-Investigation Exception (PP-349):** The Church does not file Heresy Investigation against its own ordained members who are supporting Church interests. An ordained member acting in alignment with Church doctrine, even if their methods are controversial, is shielded from internal investigation. This does not prevent: (1) opposing factions from filing Heresy Investigation against Church members via the standard PP-182 path, or (2) the Church from investigating ordained members who are actively working against Church interests (e.g., aiding the Restoration Movement, collaborating with Niflhel).
## §10.1 Parliamentary Stay (ED-631)

A Parliamentary Stay is a Senator Inward motion that halts an active Church Tribunal filing for 1 season. It represents Parliament asserting civil jurisdiction over an ecclesiastical proceeding.

**Requirements:** 2+ factions on Side A (the filing-suspension side). Church on Side B. Standard BG Parliamentary Vote resolution (§10).

**Availability:** Only while TC < 55. At TC 55+, the Church's TC political pool bonus (floor(TC/20)) makes the Stay motion effectively unpassable — Church's institutional authority at that level exceeds Parliamentary reach.

**Effect on success:** The Church Tribunal is suspended for 1 season. Church may re-file in the following season (no permanent bar). The Stay buys 1 season of disruption window — enough for the target to address one prerequisite condition (Attention Pool reduction, prior conviction, Obligation status).

**Effect on failure:** The Tribunal proceeds immediately. The motion's failure cannot be appealed or re-filed in the same season.

**TC < 55 gate rationale:** As Church grows more prominent (TC 55 = Church Prominent milestone), Parliamentary institutions lose the political standing to override ecclesiastical authority. The Stay window closes as Church grows — creating a genuine strategic timing incentive: suppress TC before it reaches 55, or lose the ability to check Church judicial power through Parliament.

---

## §12 OPEN ITEMS AND EDITORIAL FLAGS

| ED-667 | Adjudicator Thread Response: §9.4b added. Certainty-indexed response table. Visibility gate. Propagation from npc_behavior_v30 ED-663. | P1 — resolved |

### Resolved by this version (PP-234)
| Item | Resolution |
|---|---|
| ED-127 (Composure redesign) | Composure = Charisma + 6. Parallels Health = Endurance + 6. |
| Three-genre system | Turfed. Two genres (Memory/Projection). |
| Faction boost system | Four options (Memory/Projection/Revealing/Obscuring), one per faction. |
| Fractional multipliers | Replaced with integer bonus dice (+1D primary, +1D audience boost). |
| Presence → Charisma | Applied throughout. |
| Memory → Recall | Applied throughout. |
| Attribute weight by adjudicator type | §3 table. |
| Strain minimum inconsistency | Strain minimum 0 (matches combat damage minimum 0). |
| Momentum spend cap | Matches core engine: any amount, not limited to 1. |
| Private negotiation tie / Fail Forward | Stall with consequences (strain persists, Read info permanent). |
| Contest-level Let It Ride | Explicit rule in §1. |
| Adjudicator type mid-contest | Fixed per contest; change = new contest. |

### New editorial items
| ID | Description | Priority |
|---|---|---|
| ED-136 | System rename: "Debate" → "Contest" (or alternative). Pending user decision. | P1 |
| ED-137 | Panel adjudicator type not yet designed. Using Expert Judge as provisional. | P2 |
| ED-138 | Social initiative deterministic vs rolled. **Resolved (ED-581):** Changed to rolled (Attunement vs Attunement, TN 7, Ob 1). See §5. | Resolved |

### Carried forward
| ID | Description | Priority |
|---|---|---|
| ED-132 | Appraise step action name resolved: Appraise (PP-278) | P3 |
| ED-133 | Diverge state — superseded by CROSS. Confirm Diverge no longer needed. | P2 |
| ED-041 | Niflhel social toolkit — provisional stub in §9.7 | P2 |
| ED-051 | Corroboration full port (Knot requirement removed per ED-014) | P3 |

### Future design work (not blocking)
| Topic | Status |
|---|---|
| Escalation between social modes (negotiation → debate → appeal) | Conceptually identified, not designed |
| Negotiation compromise resolution (ZOPA-style) | Identified as structurally different from Conviction Track, not designed |
| Mass battle rally action (Attunement-based) | Gap identified, belongs in mass_battle_v3 |
| Appraise step expansion (reveal Beliefs, Knot vulnerabilities) | Conceptually identified, not specified |

### Simulation debt
| ID | Description |
|---|---|
| SIM-DEBT-03 | Full re-simulation under two-genre system with integer bonus dice. All prior SIM-D baselines invalidated. |
| SIM-DEBT-04 | Adjudicator-type pool variation untested. Charisma×2 and Attunement×2 pools need calibration. |

### Propagation required on approval
| File | Change |
|---|---|
| references/params_debate.md | Full rewrite |
| references/canonical_sources.yaml | Update canonical doc for social_debate |
| references/propagation_map.md | Update cross-references |
| compilation/v0.14/stage1_core_engine_deprecated.md | Attribute rename in attribute table and derived scores |
| compilation/v0.14/stage2_characters_deprecated.md | Attribute rename throughout; Composure formula; Circles/Resources pool base; §4.14 social rolls |
| designs/mass_combat/mass_battle_v3.md | Coherence Rating derivation: ⌈(Charisma + Cognition) ÷ 2⌉ |
| references/params_mass_combat.md | Coherence Rating derivation |
| references/params_core.md | Attribute names; Composure in derived scores |
| references/params_combat.md | Any Presence references |
| All test outputs referencing old genre names | Flag as stale |
