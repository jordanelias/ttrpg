# VALORIA — SOCIAL CONTEST SYSTEM v2
## [EDITORIAL: ED-136 — System name: "Contest" proposed. Candidates: Contest, Contention, Proceeding.]
## Patches applied: PP-234, PP-235, PP-236, PP-237, PP-272, PP-278, PP-279
## Status: DESIGN PROPOSAL — supersedes debate_system_redesign_v1.md Part 6 upon approval
## Source: Opus 4.6 session 2026-04-04
## Patch: PP-234 (genre restructure, attribute renames, Composure resolution, faction boost revision, dice consistency)
## Three-mode: TTRPG (§§1–9), Board Game (§10), Hybrid (§11)

### Attribute renames
- Presence → Charisma (Cha). "Presence" reserved as Husserlian technical term: the immediacy of being given to consciousness.
- Memory → Recall (Rec). "Memory" freed for genre name.
- All other attributes unchanged: Agility (Agi), Endurance (End), Strength (Str), Cognition (Cog), Focus (Foc), Attunement (Att), Bonds (Bon), Spirit (Spi).

### Genre restructure
- Three genres (Past/Present/Future) → two genres (Memory/Projection).
- "Present" is not a temporal position but the operation site where rendering occurs (Husserlian presence). "Character/Present" arguments decompose into retention (Memory) or protention (Projection) claims.
- Memory = temporal retention, actual, epistemically accessible. What has been given to consciousness.
- Projection = temporal protention, potential, epistemically inaccessible. What has yet to be given to consciousness.

---

## §1 CORE PRINCIPLE: FORMAT FOLLOWS CONTEXT

The contest system does not have a fixed format. Exchange count, role structure, audience weight, and available actions vary by institutional context and adjudicator type. The Game Master (GM) sets the format at setup; players know it before the contest begins.

**A contest is initiated when:** (a) two or more parties with opposed positions are present, AND (b) the outcome is uncertain and consequential. GMs should not call for a contest when one side has no plausible case or when the outcome is predetermined by prior Domain Actions.

**Let It Ride:** once a contest resolves a question, that question cannot be re-contested unless circumstances have significantly changed (new evidence, new faction alignment, intervening Domain Action, changed political situation). This is a direct application of the core engine's Let It Ride principle (§1.5) to the contest system.

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

If the question does not clearly favour one genre, the GM assigns whichever is more relevant. Both genres are always available to both orators.

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

**Step 6 — Define stakes.** What each side wins, loses, or compromises on. Record before first exchange.

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

**Design note:** the three social attributes (Cognition, Charisma, Attunement) each have a domain where they are primary. High-Cognition characters excel before judges and tribunals. High-Charisma characters excel before crowds and parliaments. High-Attunement characters excel in private dealings. This produces meaningful character differentiation across social contexts without adding mechanical complexity — the formula is the same; only the base attribute changes.

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

**Step 2 — Choose:** Each orator selects genre (Memory or Projection) and orientation (Revealing or Obscuring).

**Step 2b — Corroborate (optional):** A corroborator present at the contest may declare support before the Argue roll. On success: primary orator gains +1D for this exchange. Corroborator must be a declared coalition member (Knot not required). Knot-sharing corroborators roll at Ob 1; non-Knot coalition members roll at Ob 2. In asymmetric proceedings: all corroborators for the disadvantaged party use Ob 2 regardless of Knot. (PP-257) On failure: corroborator takes 1 strain.

**Step 3 — Argue:**
Initiative holder declares argument and rolls first. Respondent hears, then declares and rolls.

Pool: (Primary Attribute × 2) + History bonus (per §3), TN 7.
Add genre/orientation bonus dice per §2 Step 3 (primary genre +1D; audience boost match +1D; max +2D total).
Recall bonus: +2D when citing a specific, named, verifiable claim (document, date, prior statement, named precedent). Binary. Available in either genre.
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
One orator invokes what has been (Memory); the other projects what could become (Projection). The fundamental rhetorical collision.
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

**OBSCURING WIN** (winning any exchange with Obscuring orientation):
- Conviction Track does not move toward winner.
- Place a Doubt Marker on the opponent.
- Doubt Marker effect: opponent's next winning exchange has its margin reduced by 2 before resistance is applied (minimum 0).
- Only one Doubt Marker active at a time. New replaces old.
- Consumed on use.

**Step 5 — Forfeit actions:**
- **Regroup:** Forfeit exchange. No argument, no strain. Conviction Track moves +1 toward non-forfeiting side. Concentration restores by Focus score.
- **Concede a Point:** Forfeit exchange. Take 1 strain. Conviction Track moves +1 toward non-forfeiting side. Gain +1D on next exchange.

**Step 6 — Strain and Concentration:**

**Composure = Charisma + 6.** Range 7–13. Social damage buffer before Rattled. [RESOLVES ED-127. Parallel to Health = Endurance + 6. One attribute + constant per derived track. Charisma governs social resilience the way Endurance governs physical resilience.]

- Strain accumulates toward Composure threshold.
- At strain ≥ Composure: take a **Rattled** mark (Composure resets to full, excess strain carries over).
- All subsequent contest rolls: +1 Ob per Rattled level (cumulative).
- At 2 Rattled marks: socially incapacitated — cannot participate in formal social scenes until recovered. Informal conversation still possible.
- Rattled recovery: 1 mark clears per full scene of non-social activity or rest.
- Composure recovery: full restore at scene change (new location, new interlocutors).
- Knot as Composure buffer: redirect Composure damage to a Knot (+1 strain per use). Prevents Rattled but accelerates Knot decay.

**Concentration = Focus + Recall.** Range 2–14. Depletes by 1 per exchange, −1 additional on exchange loss.
- At Concentration 0: **Spent** — next exchange: −2D to all rolls; opponent gets +1D. Then resets to maximum.
- If both Rattled and Spent active: penalties cumulative. Pool minimum 1D per core engine.

**Step 7 — GM records exchange on hidden ledger.**

---

## §5 INITIATIVE

- Exchange 1: higher Attunement acts last (declares second; information advantage).
- Subsequent exchanges: transfers to exchange winner.
- On tie: stays with current holder.
- Institutional override: in asymmetric proceedings, the institution determines who proposes regardless of Attunement.
- [EDITORIAL: ED-138 — Social initiative is deterministic (higher Attunement always wins Exchange 1). Combat initiative is rolled. Consider whether social initiative should be rolled (Attunement vs Attunement, TN 7, Ob 1) for consistency. Current deterministic version kept pending decision.]

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

**Disposition and Reputation shifts** fire from Total Victory regardless of genre. An overwhelming win in any genre shifts how the audience renders the participants — this is a rendering consequence of social intensity, not a genre effect.

**Domain Echo:**
- Decisive win + Memory genre: winning faction's Mandate +1 in the domain of the cited precedent.
- Decisive win + Projection genre: +1D on first Domain Action pursuing the argued outcome within the season.
- Compromise: no Domain Echo.

**Total Victory** (Conviction Track ≥ 9 or ≤ 1): losing primary orator gains Contest Fatigue (−1D next social roll, one instance per session, clears at next session start if unused). Winning orator gains +1 Momentum (if below cap 4). Disposition change with all witnesses; Reputation shift (GM-set magnitude). In Board Game (BG) Parliamentary Vote: losing coalition's dominant faction takes Mandate −1 for one season.

**Post-contest recovery:** all strain and Concentration depletion clear at scene end. Spent clears at scene end. RS changes subject to RS ceiling (100) and RS=0 lockout.

---

## §7 ASYMMETRIC PROCEEDINGS

**Standard proceedings (Parliament, inter-faction):** Full symmetric system. Proposer role alternates each exchange. Initiative transfers per §5 independently.

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
| Composure | Charisma + 6 | 7–13 | Health = Endurance + 6 |
| Charisma modifier | max(0, floor((Cha − 3) ÷ 2)) | 0–2 | — |
| Focus defence | floor(Foc ÷ 2) | 0–3 | Armour Rating (damage reduction) |
| Concentration | Focus + Recall | 2–14 | Stamina = Endurance + History + 1 |
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

### §9.2 Multi-Party Contest — Coalition Structure
Each orator declares Side A or Side B at setup. No side-switching. Each side nominates one Lead per exchange (may change between exchanges). Non-lead coalition members may Corroborate (max 1 per side per exchange). Composure and Rattled tracked individually. **Coalition Concentration — shared pool (PP-237):** Concentration tracks on a shared pool equal to the sum of all coalition members' (Focus + Recall) at contest setup. Each exchange depletes the shared pool by 1 (plus 1 on exchange loss) regardless of which member holds Lead. Rotating Lead does not reset depletion. Spent triggers at 0; pool resets to its setup total. Initiative transfers to winning side; that side nominates holder.

### §9.3 Practitioner Weaving in Contests (R-65)
A practitioner with TS ≥ 30 in active Thread contact adds bonus dice: floor(TS ÷ 30) (+1D at 30, +2D at 60, +3D at 90). Must declare before rolling. Visible to all observers. Church may file Heresy Investigation on observation. After exchange: Coherence check Ob 1.

### §9.4 Thread Operations Between Exchanges
A practitioner may initiate a Thread operation between exchanges. Effects apply before next exchange's Read step. Genre/orientation dice are fixed at setup — Thread operations cannot change them mid-contest. Temporal axis conflict: if the Thread operation's temporal axis contradicts the contest's primary genre (Memory-axis operation during Projection-primary contest, or vice versa), both orators' Read rolls in the next exchange use TN 8.

### §9.5 Beliefs Integration
Winning an exchange while arguing for a position aligned with the orator's stated Belief counts as a Belief achievement for Momentum. Max 1 Momentum per contest from Belief alignment.

### §9.6 Forced Unmask
Violence in the contest chamber = immediate Unmask. Violent party auto-loses. Exception: monster incursion or external catastrophe = postponement. Proceeding resumes next scene if both parties survive.

### §9.7 Niflhel Social Toolkit
Niflhel cannot participate in Formal or Grand Contests. Their social toolkit:
- Private negotiation: one-on-one only; Attunement-primary pool (per §3 "no adjudicator"); TN 7; Ob = target's Stability.
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

1. **BG layer:** run one round of BG Parliamentary Vote (§10). Apply Conviction Track offset, capped at ±2 from neutral.
2. **Set TTRPG starting Conviction Track:** 5 ± capped BG offset, clamped to compromise zone (4–6).
3. **TTRPG personal contest:** run standard Formal (3 exchanges) or Grand (5 exchanges) per §§4–7 from adjusted starting position.
4. **Resolution:** final TTRPG Conviction Track position determines outcome. Thread consequences may fire.

---

## §12 OPEN ITEMS AND EDITORIAL FLAGS

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
| ED-138 | Social initiative deterministic vs rolled. Current: deterministic (higher Attunement). Combat: rolled. Consistency question. | P2 |

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
| compilation/v0.14/stage1_core_engine.md | Attribute rename in attribute table and derived scores |
| compilation/v0.14/stage2_characters.md | Attribute rename throughout; Composure formula; Circles/Resources pool base; §4.14 social rolls |
| designs/mass_combat/mass_battle_v3.md | Coherence Rating derivation: ⌈(Charisma + Cognition) ÷ 2⌉ |
| references/params_mass_combat.md | Coherence Rating derivation |
| references/params_core.md | Attribute names; Composure in derived scores |
| references/params_combat.md | Any Presence references |
| All test outputs referencing old genre names | Flag as stale |
