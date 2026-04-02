# VALORIA DEBATE SYSTEM REDESIGN v1

## Source: Prior Investigation + Continuation
## Model: Opus 4.6
## Status: PARTS 1–4 = DESIGN REFERENCE ONLY (quaestio structure deprecated). PART 6 = OPERATIVE SYSTEM.
## See Part 6 for all playable mechanics.

---

# PART ONE: STRUCTURAL INVESTIGATION

## 1.1 The Parity Problem

§8 Combat is the most mechanically developed subsystem in Valoria. §9 Social is not. This is a design debt, not an intentional asymmetry. The game's design intent — that political drama is at least co-equal with physical violence as a mode of play — requires that the Debate system offer the same tactical depth, decision-making density, and character differentiation as combat.

Current §9 offers none of these. A Debate is: roll Cognition + History, simultaneously, compare successes, accumulate strain. Repeat. The only decision is whether to Unmask. There is no initiative, no positional play, no action selection, no group dynamic, no resource management beyond Composure threshold, and no mechanical consequence for different argument strategies beyond a ±2D penalty for style mismatch.

Combat, by contrast, offers: pool-split allocation, initiative with multiple transfer mechanisms, seven distinct actions, weapon types with identity-defining properties, armour as a matchup problem, stamina as a degrading resource, range as a positional axis, group combat with Fibonacci scaling, and crits as breakthrough moments. Every round of combat contains multiple meaningful decisions.

## 1.2 Structural Gap Findings

**F-1: No initiative.** Combat grants initiative to the fighter at correct range; initiative transfers on hit, feint, or distance change. Debate has no equivalent. Both orators roll simultaneously with identical information. This eliminates the tactical advantage of preparation, reading, and rhetorical positioning.

**F-2: No pool split.** Combat's core decision — how to divide dice between offence and defence — has no social parallel. A debater commits their entire pool every exchange with no allocation tradeoff.

**F-3: No action variety.** Combat offers Strike, Feint, Establish Distance, Take a Breath, Full Guard, Disarm, Retrieve. Debate offers: exchange. One action. No feint, no repositioning, no recovery option beyond Unmask (which ends the Debate).

**F-4: No positional axis.** Combat tracks range (Close/Far zone) as a persistent state that determines who can act and who must manoeuvre. Debate has no equivalent spatial, conceptual, or procedural position.

**F-5: No group dynamic.** Combat has Fibonacci group bonus and split-pool defence against multiple attackers. Multi-party Debates have no mechanical structure.

**F-6: No resource arc.** Combat has stamina that degrades round-by-round, forcing Take a Breath or Out of Breath. Composure is a threshold, not a resource — it fires once (Rattled) and then the debater is simply worse. There is no recovery option and no degradation curve.

**F-7: No attribute differentiation.** Combat uses Agility (pool size), Endurance (stamina, health), Strength (damage). Three attributes with distinct mechanical roles. Debate uses Cognition alone. A character's Presence, Attunement, Memory, Bonds, and Poise are mechanically irrelevant to Debate exchanges despite being conceptually relevant.

**F-8: No matchup problem.** Combat has weapon weight, type, and reach creating asymmetric matchups (Light Cut vs Heavy Armour is functionally useless; Heavy Blunt vs Heavy Armour is devastating). Debate rhetoric styles are cosmetically different but mechanically identical — Evidence vs Character vs Consequence produces the same roll against the same Ob.

---

# PART TWO: HISTORICAL AND PHILOSOPHICAL PRECEDENT

## 2.1 The Scholastic Disputatio

The medieval university disputation (disputatio) is the single closest real-world model to a formal Debate in Valoria's setting. It was a structured adversarial procedure with defined roles, sequential phases, and institutional consequences.

**Structure of the Quaestio Disputata:**

1. **Propositio (Proposition):** The proponent states a thesis. This is not merely an opening argument — it is a formal declaration of the position to be defended, with its scope and terms defined.

2. **Obiectiones (Objections):** The opponent presents objections — reasons why the thesis is false, incomplete, or contradictory. Each objection must address the thesis directly; irrelevant objections are dismissed by the presiding master.

3. **Sed Contra (On the contrary):** The proponent (or their seconds) responds not by answering each objection but by presenting an authoritative counter-statement — a principle, precedent, or evidence that contradicts the objections as a class. This is not a rebuttal of each objection individually. It is a reframing that shifts the ground.

4. **Respondeo (I reply):** The proponent's positive argument. Having heard the objections and stated the Sed Contra, the proponent now constructs the full case. This is the strongest phase for the proposer — they have heard the opposition, established their counter-principle, and now argue from full preparation.

5. **Ad Obiectiones (To the objections):** Specific replies to each individual objection raised. Any objection not addressed is conceded.

**Key design insight:** The disputatio is not symmetric. The proposer and objector have different capabilities at each phase. The objector is strongest at phase 2 (objections) and weakest at phase 4 (they can only listen). The proposer is weakest at phase 2 (they must absorb criticism) and strongest at phase 4 (they reply from full context). This creates a tactical arc within a single exchange that simultaneous rolling cannot produce.

**Second insight:** "Unaddressed objections stand." This is not a modern convention — it was a formal rule of the disputatio. An objection the proponent fails to address in the Ad Obiectiones is treated as conceded. This creates a memory and management challenge: the more objections raised, the more the proponent must handle in their reply.

## 2.2 Aristotelian Rhetoric

Aristotle's *Rhetoric* identifies three modes of persuasion that Valoria already maps to its three styles:

| Aristotle | Valoria | Domain |
|---|---|---|
| Logos (logical argument) | Evidence Style | Past facts, records, precedent |
| Ethos (character/credibility) | Character Style | Present virtue, reputation, identity |
| Pathos (emotional appeal) | Consequence Style | Future stakes, what should be done |

But Aristotle's analysis goes further than style labels. He identifies that each mode has a **proper audience** — logos persuades the educated, ethos persuades those who respect authority, pathos persuades the crowd. The current system ignores this. All three styles are mechanically equivalent against all audiences.

**Design insight:** Rhetoric style should interact with audience composition. A Character Style argument before the Church (which values virtue and orthodoxy) should be mechanically distinct from a Character Style argument before Hafenmark (which values commercial reliability). The audience is not passive — it filters the argument through its own institutional logic.

## 2.3 Parliamentary Procedure

Real parliamentary proceedings (Westminster, continental European, and medieval royal councils) share structural features relevant to game design:

**The Speaker / Presiding Officer:** Someone controls who speaks, when, and for how long. In Valoria's context, this role is held by the institutional setting — the Parliament, the Court, the Church tribunal. The institution's rules constrain the debaters, not the other way around.

**Points of Order and Privilege:** Interruptions are possible but procedurally constrained. A member may interrupt to raise a point of order (the opponent is violating procedure) or a point of privilege (the opponent's argument affects the member's rights). These are not arguments — they are procedural interventions that change the rules of the exchange mid-stream.

**Division (Voting):** At any point after debate, a member may call for division — forcing the question to a vote. This is the mechanism by which debate transitions to decision. In Valoria's terms: the debater who controls the timing of the call for division has a significant advantage, because they choose when to stop arguing and start counting.

**Whipping:** In parliamentary systems, party discipline is enforced through whips — persuasion, pressure, and sometimes coercion applied to members before the vote. This is the group dynamic that §9 lacks: pre-debate preparation, alliance-building, and backstage negotiation that affects the formal proceeding.

**The Filibuster:** An orator can consume time as a strategic resource. In the current system, a Debate has a fixed exchange count. There is no mechanism for one side to extend or compress the proceeding — and therefore no strategic value in controlling tempo.

## 2.4 Royal Court Proceedings

Medieval and early modern royal courts operated under a different logic than parliamentary procedure:

**Audience with the Monarch:** Not a debate between equals. The petitioner presents; the monarch (or their chancellor) interrogates; the monarch decides. The petitioner has no right to object. Arguments must be framed in terms the court recognises — custom, precedent, royal prerogative.

**The Privy Council:** Advisory bodies where the monarch's trusted counsellors debate among themselves before advising. Here the dynamic shifts: the counsellors argue with each other, and the monarch observes. The winner is not who argues best but who the monarch is persuaded by — and the monarch may be persuaded by factors outside the argument (personal loyalty, factional interest, prior obligation).

**Trials by Inquisition:** The Church's inquisitorial procedure is not adversarial but investigative. There is no defending counsel. The inquisitor asks questions, the accused answers. The burden is on the accused to satisfy the inquisitor, not on the inquisitor to prove guilt. This produces a fundamentally asymmetric debate structure where one side has all the procedural power and the other has only the strength of their answers.

**Design insight:** Not all Debates should be symmetric. A petitioner before the Crown should face a structurally different procedure than two counsellors arguing before the Parliament. The institution shapes the rules.

## 2.5 Burning Wheel's Duel of Wits

The closest TTRPG precedent. Key features:

- **Body of Argument:** Each side has a "health pool" (Will + relevant skill) that depletes through the debate. When it reaches 0, you've lost. The margin of loss determines the compromise.
- **Scripted actions:** Each round, both sides secretly script three volleys from: Point, Obfuscate, Dismiss, Avoid, Incite, Rebuttal. Each volley type has different effects against each other (rock-paper-scissors-like).
- **Compromise:** The loser gets concessions proportional to how much Body of Argument the winner lost. A 5-0 wipe is total victory. A 5-4 is a pyrrhic win — the loser barely lost and extracts major compromise.

**What BW gets right:** Scripted actions create the decision density that simultaneous rolling lacks. The compromise mechanic makes close debates more interesting than blowouts.

**What BW gets wrong for Valoria:** BW's three-volley scripting system is abstract — the actions don't map to recognisable rhetorical moves. "Obfuscate" and "Dismiss" are mechanical categories, not things a person actually does in a formal debate. The system also doesn't distinguish between different kinds of argument or different audience contexts.

## 2.6 Twilight Imperium 4 — Political Phase

TI4's political system is relevant for Valoria's Grand Debate / Parliamentary Vote:

- **Agenda Cards:** The topic of debate is externally determined, not chosen by the debaters. This prevents stalling.
- **Riders:** Players can attach secondary proposals to the main agenda. If the agenda passes, riders attached to it also pass. This creates deal-making and alliance dynamics that pure argument cannot.
- **For/Against with Trade Goods:** Players spend influence (a resource) to vote. More influence = more votes. Rhetoric is irrelevant — it's pure resource commitment. This is the opposite extreme from Valoria, but it highlights that institutional decisions involve resource expenditure, not just argument quality.

---

# PART THREE: DESIGN ARCHITECTURE

## 3.1 Core Principle: The Exchange as Quaestio

Replace the current simultaneous-roll exchange with a sequential five-phase exchange modelled on the Scholastic quaestio. Each phase uses a different attribute, creating attribute rotation within a single exchange. The proposer and objector have asymmetric capabilities — different phases favour different roles.

### The Five Phases

| Phase | Name | Who Acts | Attribute | What Happens |
|---|---|---|---|---|
| 1 | **Proposition** | Proposer | Cognition | State the thesis. Roll Cognition + History. Successes set the **Thesis Strength** — the number the objector must meet or exceed. |
| 2 | **Objection** | Objector | Memory | Raise objections. Roll Memory + History. Each success is one **Objection Marker** placed. The objector is recalling precedent, identifying contradictions, citing counter-evidence. |
| 3 | **Sed Contra** | Proposer | Presence | Reframe. Roll Presence + History. Each success removes one Objection Marker. This is not answering each objection — it is asserting an authoritative counter-principle that undermines the objections as a class. Presence because this is about commanding the room, not about reasoning. |
| 4 | **Respondeo** | Proposer | Cognition | Full argument. Roll Cognition + History. Successes add to Thesis Strength. The proposer has heard the objections and the Sed Contra; they now argue from full context. |
| 5 | **Distinction** | Objector | Poise | Final rebuttal. Roll Poise + History. Each success reduces Thesis Strength by 1. Poise because this is about composure under pressure — finding the precise flaw in a fully developed argument while the room watches. |

### Exchange Resolution

After Phase 5:
- **Remaining Thesis Strength > 0:** Proposer wins the exchange. Remaining Thesis Strength = margin of victory.
- **Remaining Thesis Strength ≤ 0:** Objector wins. Absolute value of remaining Thesis Strength = margin of victory.
- **Remaining Objection Markers (unaddressed):** Each unaddressed Objection Marker (placed in Phase 2, not removed in Phase 3) is an argument the proposer failed to counter. Each unaddressed marker inflicts +1 strain on the proposer regardless of who won the exchange — "unaddressed objections stand."

### Strain

The loser of the exchange takes strain equal to the winner's margin of victory (minimum 1). The proposer additionally takes +1 strain per unaddressed Objection Marker. Strain accumulates across exchanges toward the Composure threshold as in the current system.

### Role Alternation

In a multi-exchange Debate, roles alternate. The proposer in exchange 1 becomes the objector in exchange 2. This ensures both sides face both the offensive burden (defending a thesis) and the defensive burden (attacking one).

## 3.2 The Attribute Map

The five-phase structure uses four of the ten attributes across a single exchange:

| Attribute | Phase | Role | Combat Parallel |
|---|---|---|---|
| Cognition | 1 (Proposition), 4 (Respondeo) | Reasoning, argument construction | Agility (pool size, action economy) |
| Memory | 2 (Objection) | Recall of precedent, citation, contradiction-finding | — (no direct parallel; closest is weapon type selection) |
| Presence | 3 (Sed Contra) | Commanding authority, reframing | Strength (damage output) |
| Poise | 5 (Distinction) | Composure under pressure, precision | Endurance (stamina, staying power) |

**Attunement** remains the Reading Exchange attribute (pre-debate perception).
**Bonds** is the Corroboration attribute (group support action — see §3.5).

This means a character with high Cognition but low Memory is a strong proposer but a weak objector. A character with high Presence dominates the Sed Contra but cannot construct the original argument. A character with high Poise is devastating in the final rebuttal but contributes little to the opening phases. This IS the weapon-type differentiation problem solved for social combat — different characters are differently shaped for debate, just as different weapon types create different combat identities.

## 3.3 Initiative: Who Proposes?

In combat, initiative determines who declares last — a genuine tactical advantage. In Debate, initiative determines **who proposes first** in exchange 1.

**Why this matters:** The proposer has the structural advantage in the quaestio — they speak first (Phase 1), reframe (Phase 3), and deliver the full argument (Phase 4). Three of five phases belong to them. But the objector has the devastating final word (Phase 5) and the "unaddressed objections stand" rule. The role with more phases is not necessarily the stronger role.

**Initiative determination:**

- **Institutional default:** The setting determines who proposes. In Parliament, the party introducing the motion proposes. In a royal audience, the petitioner proposes. In a Church tribunal, the Inquisitor proposes (the accused is structurally the objector — they can only respond to charges). In a street argument, the aggressor proposes.
- **Contested initiative:** When no institutional default applies, both orators roll Presence, Ob 1. Higher net successes proposes first. Tie: the orator with the higher Presence score proposes (they command the room).
- **Voluntary yield:** An orator may yield initiative — choosing to object rather than propose. This is tactically interesting: if you believe you are stronger in the Distinction phase (high Poise) than in the Proposition/Respondeo (lower Cognition), you may prefer to object.

## 3.4 Actions Beyond the Exchange

Combat has seven actions. Debate should have more than one. The following actions are available in addition to the standard exchange:

**Concede a Point (replaces one exchange):** Voluntarily forfeit one exchange. The opponent wins it automatically with margin 1. The conceding orator takes 1 strain but gains +1D on their next Proposition or Respondeo roll — they have narrowed the debate to ground they can defend. Strategic retreat.

**Call for Division (Grand Debate / Parliamentary Vote only):** After any completed exchange, an orator may call for division — moving the question to a vote. This ends the Debate prematurely. Resolution: count exchanges won by each side so far. If one side has a majority, they win. If tied, the presiding authority breaks the tie (institutional advantage). Tactical use: call for division when you're ahead but expect to lose remaining exchanges.

**Challenge (interrupt Phase 2 or Phase 5):** During the opponent's Objection or Distinction phase, the orator may Challenge — claiming the argument violates the terms of the debate, introduces fabricated evidence, or misrepresents the position. Roll Cognition, Ob 2. Success: the challenged phase's successes are halved (round down). Failure: the challenger takes +1 strain (the interruption backfired — they look desperate). Maximum one Challenge per exchange per orator.

**Appeal to the Room (replaces Sed Contra, Phase 3 only):** Instead of rolling Presence to remove Objection Markers, the proposer appeals directly to the audience. Roll Presence + History against the audience's Disposition Ob. Success: audience Disposition improves one step toward the proposer, and Objection Markers are reduced by the audience's new Disposition level (Friendly = 2 removed, Neutral = 1, etc.). Failure: audience Disposition worsens one step. This is high-risk/high-reward — it bypasses the argumentative structure entirely and goes straight to the crowd.

**Unmask (unchanged from current §9):** Available at any point. Clears strain, reveals truth, ends the formal Debate. Cannot resume. The prior conversation's architecture preserves this.

## 3.5 Corroboration (Group Dynamic)

Combat has Fibonacci group bonus. Debate has **Corroboration** — allies supporting the primary orator.

**Mechanism:** A corroborator is a character present at the Debate who is not the primary orator. During any phase, the corroborator may roll Bonds + relevant History, Ob 1. On success: the primary orator gains +1D for that phase only. On Overwhelming (net ≥ 2): +2D.

**Constraints:**
- Maximum one corroborator per phase.
- Each corroborator can support once per exchange (one phase only).
- The corroborator must have a Knot with the primary orator (they are drawing on a real relationship, not just standing nearby).
- If the corroborator has no relevant History for the topic, they roll Bonds alone (no History bonus).

**Why Bonds:** Corroboration is not about the corroborator's own argument. It is about their relationship with the primary orator — a nod of confirmation, a whispered reminder, a visible show of support that reinforces the orator's position. Bonds measures the strength of that relational support.

**Combat parallel:** Fibonacci bonus adds dice. Corroboration adds dice. But where Fibonacci is purely numerical (more attackers = more dice), Corroboration is constrained by relationship (Knot required) and timing (one phase per exchange). This makes it a preparation reward — you brought the right allies, positioned them correctly, and they intervened at the right moment.

## 3.6 Audience Disposition as a Second Win-Condition

In the current system, the audience is passive — the winner is determined by exchange count. The redesign introduces audience Disposition as a **parallel win-condition** for Formal and Grand Debates.

**Dual victory conditions:**
1. **Exchange majority:** Win more exchanges than the opponent.
2. **Audience capture:** End the Debate with the audience at Friendly disposition toward you AND Hostile or worse toward the opponent.

A debater who wins the exchange majority but loses the audience achieves a **procedural victory** — they argued better but failed to persuade. The institution may honour the result, but the political consequences are muted.

A debater who loses the exchange majority but captures the audience achieves a **popular victory** — they lost the argument but won the room. The institution may reject the result, but the political consequences are significant (Domain Echo fires based on audience response, not exchange count).

A debater who wins both achieves a **total victory** — full consequences, exchange and audience.

**Audience Disposition tracking:** The audience has an initial Disposition set by the GM. Each exchange shifts it:
- Exchange won by Margin ≥ 3 (Overwhelming): +1 step toward winner
- Appeal to the Room success: ±1 step (per §3.4)
- Unmask: +2 steps toward the unmasking orator (vulnerability is persuasive) unless the revealed truth damages their position (GM call)
- Rhetoric Genre match (see §3.7): if the winning orator's genre matches the audience's institutional resonance, +1 step

## 3.7 Rhetoric Genre and Institutional Resonance

The three rhetoric styles (Evidence, Character, Consequence) become **genres** with mechanical interaction against audience faction identity.

**Faction Resonance Table:**

| Faction | Primary Resonance | Secondary Resonance | Resistant To |
|---|---|---|---|
| Crown | Character (royal authority, lineage, virtue) | Consequence (what is best for the realm) | Evidence (the Crown is above precedent) |
| Church | Evidence (scripture, doctrine, recorded revelation) | Character (piety, orthodoxy, moral standing) | Consequence (worldly outcomes are secondary to divine truth) |
| Hafenmark | Consequence (commercial outcomes, prosperity, practical benefit) | Evidence (contracts, ledgers, market data) | Character (merchants judge by results, not virtue) |
| Varfell | Evidence (intelligence, documented facts, observed reality) | Consequence (strategic outcomes, power dynamics) | Character (Varfell distrusts virtue claims on principle) |
| Guilds | Consequence (workers' welfare, economic justice, practical reform) | Character (solidarity, collective identity, trustworthiness) | Evidence (statistics can be made to say anything) |
| Niflhel | — | — | All genres (Niflhel does not participate in formal debate structures; their social mode is private manipulation, not public argument) |
| Revolution | Character (moral authority, courage, authenticity) | Consequence (liberation, justice, the future) | Evidence (the old order's records are instruments of oppression) |

**Mechanical effect:** When the orator's declared genre matches the audience faction's Primary Resonance: +1D to the Sed Contra or Respondeo phase (the audience is predisposed to hear this kind of argument). When it matches Secondary Resonance: no bonus but no resistance. When it matches the "Resistant To" genre: −1D to the Sed Contra or Respondeo (the audience actively resists this framing).

**Mixed audiences:** In Parliament, multiple factions are present. The GM determines the dominant faction(s) in the room. If no faction dominates, no resonance modifier applies.

**[EDITORIAL: Niflhel social mode]** — Niflhel characters should not access the formal Debate structure. Their social toolkit is Reading Exchange, private manipulation (Appeal against individuals), and Thread operations. They do not argue in public. This is a faction-asymmetric design that mirrors Niflhel's asymmetric military and Thread capabilities.

## 3.8 Thread Consequences by Genre

When a Debate concludes, the winning argument's genre determines the type of Thread consequence that fires (co-movement from the social event):

| Genre Won | Thread Consequence | Mechanism |
|---|---|---|
| **Evidence** | Pulling — temporal co-movement | The audience re-experiences the cited past. Observers with TS 30+ perceive a thread-shimmer in the room. RS +1. The past was invoked with enough force to disturb the present's temporal configuration. |
| **Character** | Co-movement — epistemic shift | An Overwhelming Character victory shifts how the audience renders the target's identity. Disposition change with all present witnesses. This is not Thread manipulation — it is the natural co-movement of an epistemic event at social scale. No RS change unless a practitioner amplifies it. |
| **Consequence** | Actualization — Domain Echo | The argued future becomes a probability anchor. +1D on the first Domain Action pursuing that consequence within the season. The argument's force partially actualizes the future it described. RS +1 if the consequence involves Thread-sensitive matters. |

**Canon grounding (P-01, Inseparability):** These are not three separate effects. They are three descriptions of the same co-movement. An Evidence argument that invokes the past also shifts how the audience renders the present (epistemic) and partially actualizes a future response (actual). The system foregrounds one dimension per genre for mechanical clarity, but the GM should narrate all three dimensions shifting. The Thread consequence fires automatically — social events at sufficient scale always produce co-movement. Debate is high-intensity social rendering; the threads move.

## 3.9 Stamina Analogue: Concentration

Combat has Stamina (depletes by 1 per round, Out of Breath at 0). Debate needs a parallel resource that degrades over the course of the proceeding.

**Concentration = Focus + History bonus (relevant to the topic)**

Concentration depletes by 1 at the end of each exchange (not each phase). At Concentration 0, the orator is **Spent** — the social analogue of Out of Breath:
- Concentration restores to maximum.
- The orator's next exchange is at −2D to all phases (exhaustion, loss of thread, repeating themselves).
- The opponent gains +1D to their Distinction phase in that exchange (the spent orator is vulnerable to a precision strike).

**Recover Concentration:** An orator may, instead of participating in an exchange as primary, declare **Regroup**. They forfeit the exchange (opponent wins automatically, margin 1, as with Concede a Point). Concentration restores by Focus score. This is the Debate equivalent of Take a Breath — you sacrifice a round to recover resources.

**Design intent:** Concentration creates a tempo arc. A debater with high Focus (large Concentration pool) can sustain longer debates without becoming Spent. A debater with low Focus must either win quickly or Regroup — revealing vulnerability. Grand Debates (5 exchanges) will push most characters to the Concentration limit; only those with Focus 4+ can sustain the full proceeding without regrouping.

## 3.10 Asymmetric Proceedings

Not all Debates are symmetric. The institution shapes the rules.

**Formal Debate (Parliament, inter-faction):** Full symmetric quaestio. 3 exchanges, roles alternate. Audience is Parliament (mixed faction resonance).

**Grand Debate (faction-defining):** 5 exchanges, roles alternate. Dual win-condition (exchange + audience). Thread consequences fire. Full consequences per current rules + this redesign.

**Royal Audience (petitioner before the Crown):** Asymmetric. The petitioner proposes; the Crown objects. Roles do NOT alternate — the Crown retains the objector position for all exchanges. The petitioner must defend their thesis against repeated challenge. Exchange count: 3. The Crown may Call for Division at any time. The audience is the Court (Crown resonance applies). This structurally favours the Crown, as intended — petitioning the monarch is not a contest between equals.

**Church Tribunal (Inquisitorial proceeding):** Asymmetric. The Inquisitor proposes (presents charges); the accused is the objector. But the Inquisitor also controls the Phase 3 Sed Contra — the accused has no Sed Contra phase. Their only actions are Objection (Phase 2) and Distinction (Phase 5). Exchange count: set by the Inquisitor (1–5). The accused may not Call for Division. The audience is the Church (Evidence resonance applies). This is deliberately oppressive — the Church tribunal is not designed for justice but for doctrinal enforcement.

**Casual Dispute (street, tavern, personal):** Simplified. 1 exchange only. No audience tracking. No Thread consequences. Proposer determined by who initiated the argument. If it escalates, the GM may upgrade to a Formal Debate with additional exchanges.

**[EDITORIAL: additional proceeding types]** — Consider: Guild arbitration (three-party: two disputants + Guild arbiter who holds the tie-breaking Distinction), Varfell internal review (closed-door, no audience, winner determined by Distinction phase alone — pure precision), Revolution assembly (audience IS the orator — direct democracy, Appeal to the Room replaces the entire quaestio).

---

# PART FOUR: COMBAT STRUCTURAL PARALLEL TABLE

| Combat Feature | Debate Parallel | Mechanism |
|---|---|---|
| Combat Pool (Agility × 2 + History + 3) | Phase-specific pools (attribute + History) | Attribute rotates by phase; no single "debate pool" |
| Pool split (Offence / Defence) | Role assignment (Proposer / Objector) | Structural asymmetry replaces allocation asymmetry |
| Initiative (structural, transfer on hit/feint) | Proposition right (institutional, contested, voluntary yield) | Who proposes first determines the structural advantage |
| Actions (Strike, Feint, Full Guard, etc.) | Actions (Exchange, Concede, Challenge, Appeal to Room, Regroup) | Decision density per exchange, not per round |
| Weapon types (Light/Heavy, Cut/Blunt) | Rhetoric genres (Evidence, Character, Consequence) | Matchup problem against audience faction resonance |
| Range (Close/Far zone) | Proceeding type (Royal Audience, Parliament, Tribunal, etc.) | Institution constrains available actions and role assignment |
| Stamina (degrades per round) | Concentration (degrades per exchange) | Resource arc with recovery option (Regroup ≈ Take a Breath) |
| Wounds (threshold incapacitation) | Composure / Rattled (threshold debuff) | Strain accumulation toward dramatic threshold |
| Fibonacci group bonus | Corroboration via Bonds | Ally support with Knot constraint |
| Armour (DR by weapon type) | Faction resonance (±1D by genre match) | Defensive matchup modifier |
| Crits (excess ≥ 3) | Overwhelming (margin ≥ 3) | Breakthrough moment with escalated consequences |
| Out of Breath (forced recovery) | Spent (forced recovery) | Resource depletion consequence |
| Disarm | Inspiration attack (Character Style, net ≤ 0) | Removes opponent's resource through specific targeting |
| Mass combat (unit-scale abstraction) | Parliamentary Vote (faction-pool abstraction) | Scale shift with simplified resolution |

---

# PART FIVE: OPEN ITEMS

## 5.1 Editorial Decisions Required

1. **[EDITORIAL: Niflhel formal Debate access]** — Should Niflhel characters be excluded from formal Debate entirely, or permitted with no faction resonance bonuses?

2. **[EDITORIAL: Proceeding type catalogue]** — Which asymmetric proceedings exist beyond Royal Audience and Church Tribunal? Guild arbitration? Varfell review? Revolution assembly?

3. **[EDITORIAL: Concentration attribute]** — Focus is proposed. Poise is the alternative (composure under sustained pressure). Which?

4. **[EDITORIAL: Audience Disposition as win-condition]** — Does dual win-condition (exchange + audience) apply to all Formal/Grand Debates, or only Grand Debates?

5. **[EDITORIAL: Role alternation in 5-exchange Grand Debate]** — Exchange 5 has one side proposing 3 times and the other 2. Which side gets the extra proposition? The initiator? Or does the Grand Debate use a different structure (e.g., 5 exchanges with alternating roles, 3-2 split, and the side with 3 propositions is the faction that called for the Grand Debate)?

6. **[EDITORIAL: Corroboration Knot requirement]** — Is the Knot requirement too restrictive? Should any ally present be able to corroborate, with Knot holders getting +1D to their corroboration roll?

7. **[EDITORIAL: Thread consequences for Casual Disputes]** — Currently no Thread consequences for casual disputes. Should high-strain casual disputes (Rattled trigger) produce minor co-movement?

## 5.2 Gaps Requiring Design

[GAP-DS-01] Exact Ob tables for each phase of the quaestio — currently assumes Ob 1 throughout, but institutional context may warrant variable Ob per phase.

[GAP-DS-02] Interaction between Thread operations and Debate — what happens when a practitioner Weaves on a Debate subject mid-proceeding? The stage15 catalogue has entries (W-42: Crowd Coherence) but no resolution procedure for within-Debate Thread interference.

[GAP-DS-03] Grand Debate total loss (5-0): current rule is +1 Ob for one season. Under the new system with dual win-condition, what are the consequences of total exchange loss + total audience loss?

[GAP-DS-04] How does the Reading Exchange interact with the quaestio? Currently it provides +1D to "the first formal Exchange." Under the new system, does this mean +1D to Phase 1 of Exchange 1? Or +1D to all phases of Exchange 1?

[GAP-DS-05] Mass Debate / Parliamentary Vote procedure under the quaestio system. The current system uses "best of 3 exchanges with faction pools." The quaestio structure may need simplification for faction-level resolution.

---

*End of design proposal. All mechanical content is provisional pending editorial approval and stress testing.*

---

# PART SIX: COMPILED MECHANICAL SPECIFICATION
## Source: debate_stress_test_v1.md + debate_stress_test_v2.md
## Status: OPERATIVE — supersedes quaestio design (Parts 3–4) for play purposes
## Version: v1.3 (PP-101 through PP-111 applied in-place 2026-04-02)
## Parts 1–4 retained as design reference and historical/philosophical foundation

---

## NOTE ON STRUCTURE

Parts 1–4 document the quaestio-based design (five-phase exchange). The stress tests (v1 and v2) were conducted on a simpler exchange-based system with genre/orientation/Conviction Track mechanics. That simpler system produced better play outcomes and is the compiled operative specification below. The quaestio structure is preserved as a design reference and may be revisited as a variant for Grand Debate or formal academic settings. The faction resonance table (§3.7), thread consequences (§3.8), and corroboration mechanic (§3.5) carry forward unchanged.

---

## 6.0 Core Principle: Format Follows Context

The debate system does not have a fixed format. Exchange count, role structure, audience weight, and available actions all vary based on the institutional context and whether an audience is present. The GM sets the format at setup; players know it before the debate begins.

**What varies by context:**

| Variable | Private Negotiation | Parliamentary Session | Church Tribunal | Street Dispute |
|----------|--------------------|-----------------------|-----------------|----------------|
| Exchange count | 1–2 | 4–6 | 1–5 (Inquisitor sets) | 1 |
| Role structure | Symmetric, alternating | Symmetric, alternating | Asymmetric (Institution proposes throughout) | Initiator proposes |
| Audience | None (or named third party) | Faction delegates — weighted by composition | Church judges only | Bystanders (low resistance) |
| Audience resistance | 0 (no institutional inertia) | Average faction Stability − 1 | Halved for accused | 0 |
| Available actions | All | All | Accused cannot Call for Division | All |
| Thread consequences | Only on Unmask or extreme outcome | Standard | Standard | Only on Unmask |
| Conviction Track | Optional (or GM-narrated) | Active | Active (starts biased) | Optional |

**Audience presence changes the system fundamentally:**
- With audience: Conviction Track active. Genre weights apply. Audience resistance set by institutional composition.
- Without audience: No Conviction Track. Winner determined by exchange count. Strain still accumulates — the stakes are relational, not political.

**The GM declares at setup:**
1. Exchange count
2. Role structure (symmetric / asymmetric / who proposes)
3. Audience present? If yes: faction composition, resistance, starting track position
4. Available actions (any restrictions for this institutional context)
5. Stakes

This declaration is made before the first exchange. Players may not request format changes mid-debate.

**Debate initiation (Principle 1 — roll only when meaningful):** A Debate is initiated when: (a) two orators with opposed positions are present in an institutional context that recognises formal argument, AND (b) the outcome is uncertain and consequential. GMs should not call for a Debate when one side has no plausible case (institutional gatekeeping prevents the debate from being called), or when the outcome is predetermined by prior Domain Actions. [PP-107]

---

## 6.1 GM Setup (Before Debate Begins)

**Step 1 — Determine Primary Genre from the Question:**

| Question Type | Primary Genre |
|---|---|
| "Did X happen? / Was X done?" | Past |
| "Is X true? / Is this person fit?" | Present |
| "Should we do X? / What should be done?" | Future |

**Step 2 — Set Genre Weights from Audience Ethical Mode:**
- Primary genre: ×1.0
- Other two genres: ×0.5 base
- Audience ethical mode adjusts ONE genre by +0.5:

| Faction / Mode | Adjustment |
|---|---|
| Virtue ethics (Crown) | Present +0.5 |
| Divine command (Church) | Past +0.5 |
| Categorical imperative (Hafenmark) | Past +0.5 |
| Consequentialism (Varfell) | Future +0.5 |
| Moral relativism (Guilds) | GM chooses based on context (this IS moral relativism) |
| Rawlsian social contract (Restoration) | Future +0.5 |

Weight range: 0.5, 1.0, or 1.5. Never 0, never above 1.5. Weights are fixed at setup. Do not shift dynamically. Record in ledger.

**Step 3 — Set Orientation Weights:**
- Revealing: ×1.0 (default)
- Obscuring: Obscuring does NOT move the Conviction Track toward the user's position. A winning Obscuring exchange places a **Doubt Marker** on the opponent instead (see §6.4).

**Step 4 — Set Conviction Track:**
- Scale: 0 to 10. Side A wins at ≥7. Side B wins at ≤3. Compromise zone: 4–6.
- Starting position: GM-set (typical neutral: 4–6). Record in ledger.
- Audience resistance: average Stability of represented factions, round up, then −1 (minimum 0). Typical range: 0–2.

**Step 5 — Define Stakes:** What each side wins, loses, or compromises on. Record before debate begins.

**Step 6 — Record all of the above in the hidden GM ledger before the first exchange.**

---

## 6.2 Derived Values

| Value | Formula |
|---|---|
| Presence modifier | max(0, floor((Presence − 3) / 2)) → Pres 1–3: +0; Pres 4–5: +1; Pres 6–7: +2. Minimum 0 — never negative. [PP-101] |
| Focus defence | floor(Focus / 2) → passive, no roll |
| Composure | Poise + Bonds + 3. Range 5–17. |
| Concentration | Focus + Presence. Depletes per exchange. |
| Attunement read pool | Attunement score only (no History bonus) |

---

## 6.3 Initiative

- Exchange 1: higher Presence speaks first (proposes).
- Subsequent exchanges: transfers to exchange winner.
- On tie: stays with current holder.
- After Divergence: stays with holder.
- Institutional override: in asymmetric proceedings, the institution determines who proposes regardless of Presence (see §6.9).

---

## 6.4 Exchange Structure

**Step 1 — Read (both orators):**
Roll Attunement alone (no History), TN 7, Ob 1.

| Net Successes | Output |
|---|---|
| Failure (0) | Misleading signal: GM identifies a genre as strong that is actually weak. Orator acts on false intelligence. |
| Partial (1) | Primary genre identified only. No orientation signal. |
| Success (2) | Primary genre + whether Revealing or Obscuring is preferred. |
| Overwhelming (3+) | Genre + orientation + one specific detail (swing faction, emotional state, key individual). |

**Step 2 — Choose:** Each orator selects genre (Past / Present / Future) and orientation (Revealing / Obscuring).

**Step 2b — Corroborate (optional):** Before rolling, a corroborator present at the debate may declare support (see §3.5 for full procedure — [GAP-DS-12: corroboration not yet fully ported to Part 6; use §3.5 as provisional reference]). On success: primary orator gains +1D for this exchange's Argue roll. Corroborator must share a Knot with the primary orator. [PP-104 — stub; full procedure pending editorial resolution of Knot requirement]

**Step 3 — Argue:** Initiative holder declares argument and rolls first. Respondent hears declaration, then chooses genre/orientation and rolls.
- Pool: (Presence × 2) + History bonus, TN 7.
- Memory bonus: +2D when citing a specific, named, verifiable claim (document, date, prior statement, named precedent). Binary — either it qualifies or it doesn't. Available in any genre.

**Step 4 — Resolve by Interaction Type:**

**CLASH** (same genre, opposite orientation):
- Compare successes. Higher wins. Margin = difference.
- effective_margin = floor(margin × genre_weight × orientation_weight_of_winner).
- If effective_margin > resistance → Δ = effective_margin − resistance toward winner's position on Conviction Track.
- If effective_margin ≤ resistance → 0 movement.
- Strain to loser: margin + 1 + winner's Presence modifier. Reduced by loser's Focus defence: floor(Focus/2). Minimum 1 strain regardless of Focus defence. [PP-103]

**COMPETITION** (same genre, same orientation):
- Same resolution as Clash.
- Strain to loser: (margin − 1, minimum 1) + 1 + winner's Presence modifier. Reduced by Focus defence. Minimum 1 strain regardless of Focus defence. [PP-103]
- No loser tracker contribution.

**DIVERGENCE** (different genre):
- No direct comparison. Each argument evaluated independently.
- effective_margin for each = floor((successes / 2) × genre_weight × 1.0). [orientation_weight fixed at 1.0 in Divergence — Obscuring is handled separately below. Half successes brings Divergence into comparable scale with Clash margin.] If net successes are negative (fumbles exceeded hits), effective_margin is negative and is treated as 0 by the gate (not > resistance → no movement). [PP-111]
- For each side: if effective_margin > resistance → Δ = effective_margin − resistance toward that side's position.
- Net tracker movement = difference between the two deltas; direction: toward the side with the larger delta.
- **Obscuring in Divergence [PROVISIONAL: PP-099]:** If the side with the larger delta used Obscuring orientation, place a Doubt Marker on the opponent instead of applying tracker movement. Conviction Track does not move.
- No strain dealt. Neither argument attacked the other.
- Initiative stays with holder.
- **TIE override [PROVISIONAL: PP-097]:** If both orators score equal successes (including both scoring 0), the TIE rule fires instead: both take 1 strain, Conviction Track moves +1 toward initiative holder. The "any interaction type" specification in the TIE rule takes priority over Divergence independent evaluation.

**TIE** (equal successes, any interaction type):
- Both orators take 1 strain.
- Conviction Track moves +1 toward initiative holder's position.
- Initiative stays with holder.

**OBSCURING WIN** (winning exchange with Obscuring orientation):
- Conviction Track does not move toward winner.
- Instead: place a Doubt Marker on the opponent.
- Doubt Marker effect: opponent's next winning exchange has its effective_margin reduced by 2 before resistance is applied.
- Only one Doubt Marker can be active at a time. If a second Obscuring win occurs while a Doubt Marker is already active, it replaces the existing marker (no stacking).
- Doubt Marker is consumed on use.

**Step 5 — Forfeit actions:**
- **Regroup:** Forfeit exchange. No argument, no strain. Conviction Track moves +1 toward non-forfeiting side (fixed, no genre weight). Concentration restores by Focus score. **Spent interaction [PROVISIONAL: PP-098]:** If Concentration was 0 when Regroup is declared, Regroup consumes the Spent state without applying the −2D/+1D penalty — no argue roll occurs during Regroup so the penalty has no target. Concentration then resets to maximum normally.
- **Concede a Point:** Forfeit exchange. Take 1 strain. Conviction Track moves +1 toward non-forfeiting side. Gain +1D on next exchange's argument roll.

**Step 6 — Strain and Concentration:**
- Strain accumulates toward Composure.
- At strain ≥ Composure: **Rattled** — −2D to all debate rolls; Focus defence is lost (strain not reduced). Persists until Unmask or scene end. **Stacking with Spent:** If both Rattled and Spent are active simultaneously, penalties apply cumulatively (−4D total; opponent also gains +1D from Spent). Pool minimum of 1D (params_core) applies as the floor. [PP-106]
- Concentration depletes: −1 per exchange, −1 additional on any exchange loss. (Regroup counts as a loss for concentration purposes.) Concentration minimum is 0 — it cannot go below 0 from multiple depletion triggers in a single exchange; Spent fires immediately when Concentration reaches 0. [PP-102]
- At Concentration 0: **Spent** — next exchange: −2D; opponent gets +1D. Concentration then resets to maximum.

**Step 7 — GM records exchange on hidden ledger.**

---

## 6.5 Post-Debate Resolution

- GM reveals ledger.
- Conviction Track position determines outcome: ≥7 = Side A wins; ≤3 = Side B wins; 4–6 = compromise (GM narrates partial outcome proportional to final position).
- Winner's final genre + orientation determines Thread co-movement type (see §3.8, which carries forward unchanged).
- Stakes resolve. **Domain Echo (canonical consequence by win type) [PP-110 — table stub; full table pending editorial]:**
  - Decisive win (TC ≥7 or ≤3) + Future genre: Domain Echo fires — winner gains +1D on first Domain Action pursuing the argued future within the season.
  - Decisive win + Evidence genre (Past): winning faction's Mandate +1 in the domain of the cited precedent.
  - Decisive win + Character genre (Present): Disposition change with all witnesses; Reputation shift (GM-set magnitude).
  - Compromise (4–6): No Domain Echo. Stakes partially resolve per final TC position proportional to win threshold distance.
- **Post-debate recovery:** All strain clears at scene end. Rattled and Spent states clear at scene end. Debate leaves no persistent character state (no wound equivalent). [PP-108] [DESIGN NOTE: This means debate has no next-scene consequence on the character sheet — see GAP-DS-16 for whether this is intended.]

---

## 6.6 Faction Resonance Integration

The faction resonance table (§3.7) integrates with genre weights as follows:

The ethical mode adjustments in §6.1 Step 2 ARE the faction resonance system. The +0.5 genre adjustment is the mechanical expression of institutional receptiveness. The ±1D modifiers described in §3.7 are superseded by the genre weight system — genre weight ×1.5 for the audience's preferred genre captures the +1D effect more consistently.

Exception retained from §3.7: Niflhel does not participate in formal debate structures. Niflhel characters have no faction resonance modifier and cannot benefit from audience composition. Their social toolkit is Reading Exchange, private manipulation, and Thread operations only.

---

## 6.7 Asymmetric Proceedings

**Standard proceedings (Parliament, inter-faction):** Full symmetric system. **Proposer role** alternates each exchange (1→A, 2→B, 3→A…). **Initiative** transfers per §6.4 rules independently: exchange winner takes initiative; Divergence retains with holder. These are separate mechanics — proposer role does not reset initiative. [PROVISIONAL: PP-100]

**Asymmetric proceedings (Church Tribunal, Royal Audience, Inquisition):**
- Institutional rules override initiative. The institution assigns Proposer/Respondent roles.
- Roles do NOT alternate — the institution retains the advantaged position throughout.
- Asymmetric resistance rule: in asymmetric proceedings, the disadvantaged party (accused, petitioner) faces **halved resistance** (round up) when moving the Conviction Track in their favour. The advantaged party (inquisitor, Crown) faces full institutional resistance for their tracker movement. This represents the institution being hard to sway toward the accused's position — but not impossibly so.

| Proceeding Type | Exchange Count | Role Structure | Audience Resistance Modifier |
|---|---|---|---|
| Formal Debate (Parliament) | 3 | Alternating | Standard |
| Grand Debate (faction-defining) | 5 | Alternating | Standard |
| Royal Audience | 3 | Crown objects throughout | Halved for petitioner |
| Church Tribunal | 1–5 (Inquisitor sets) | Inquisitor proposes throughout | Halved for accused. **Design note [PP-109]:** With TC starting at 6 (biased), boosted genre (Past ×1.5), and pool gap ≥ 4D, P(one-exchange resolution) ≈ 88%. GMs seeking dramatic Tribunal play should set exchange count ≥ 3 and start TC at 5 (neutral). Exchange count 1 is appropriate only for summary proceedings where the outcome is near-certain by intent. |
| Casual Dispute | 1 | Initiator proposes | N/A (no tracker) |

---

## 6.8 Untested Items (Require Separate Testing)

The following items were identified in stress test v2 as requiring future testing:

| Item | Priority |
|---|---|
| Multi-party debates (3+ orators): no procedure exists | P1 |
| Thread operations during debate: no interaction procedure | P1 |
| Corroboration from §3.5 in practice (not tested in v1/v2 retests) | P2 |
| Parliamentary proceeding with new formulas | P2 |
| Royal Audience proceeding (stress test v2 tested Tribunal only) | P2 |
| Casual Dispute edge cases (single exchange + tracker) | P3 |
| Regroup exploit in Grand Debate (partially addressed by Concentration depletion change) | P2 |
| Genre pivot mid-debate (orator argues against the Question's genre): no procedure | P2 |
| Rattled → Unmask decision point (Rattled never triggered in retests) | P2 |
| Multiple Doubt Markers in same exchange | P3 |
| Mixed audience with Guilds (moral relativism — GM flex): calibration needed | P2 |

---

## 6.9 Updated Open Items (Part 5 superseded by this list)

All items from §5.1 carry forward, plus additions from stress tests:

**Mechanical — requires design decision:**
- [GAP-DS-01] Phase Ob tables carry forward (Ob 1 throughout assumed — verify)
- [GAP-DS-02] Thread operations mid-debate — no procedure
- [GAP-DS-03] Total loss (5-0) consequences under dual-track system
- [GAP-DS-04] Reading Exchange +1D placement in new system (Phase 1 only, or full Exchange 1?)
- [GAP-DS-05] Parliamentary Vote under compiled system
- [GAP-DS-06] Multi-party debate structure (P1 — blocking for Parliament scenarios)
- [GAP-DS-07] Genre pivot: declared mid-debate change to Question's genre — permitted? Cost?
- [GAP-DS-08] Single Doubt Marker replacement rule — confirm intended behaviour when second Obscuring win fires before first Doubt Marker is consumed

**Editorial — requires user approval:**
- [EDITORIAL: Niflhel formal Debate access] (carried from §5.1)
- [EDITORIAL: Proceeding type catalogue] (carried)
- [EDITORIAL: Concentration attribute — Focus vs Poise] (carried; stress test used Focus — confirm)
- [EDITORIAL: Audience Disposition win-condition scope — all Formal vs Grand only] (carried; stress test used Conviction Track for all types — confirm)
- [EDITORIAL: Grand Debate role alternation — 5 exchanges, which side proposes 3 times?] (carried)
- [EDITORIAL: Corroboration Knot requirement] (carried)
- [EDITORIAL: Thread consequences for Casual Disputes] (carried)
- [EDITORIAL: Can the accused have corroborators in a Church Tribunal?] (from stress test v2, scenario 2)
- [EDITORIAL: Does resistance apply symmetrically to prosecution in asymmetric proceedings?] (stress test v2 Finding v2-06 — tentative answer: yes, confirm)
- [EDITORIAL: Is Obscuring as pure denial / Doubt Marker the intended function?] (v2-P02 — confirm design intent)
- [EDITORIAL: Niflhel social mode — what CAN they do if excluded from formal debate?] (stress test v2 Phase 4)
## 6.10 PRACTITIONER WEAVING IN DEBATES (R-65)

Confirmed pool formula: **(Presence × 2) + History bonus, TN 7.**

Note: SIM-DEBT-01 RESOLVED (2026-04-02). Stress tests SIM-D-01 and SIM-D-02 confirmed calibration under (Presence × 2) + History pool. See references/params_debate.md for updated baselines.

### R-65 — Practitioner Weaving Bonus in Debates
A practitioner with TS ≥ 30 who is actively in Thread contact during a Debate exchange adds bonus dice to their pool equal to floor(TS ÷ 30):
- TS 30–59: +1D
- TS 60–89: +2D
- TS 90+: +3D

The practitioner must declare the Weaving before rolling. The operation is visible to all observers (practitioner is in contact while debating). Church may immediately call for Heresy Investigation on observation. After the exchange, the practitioner makes a Coherence check at Ob 1 — maintaining Debate and Thread contact simultaneously stresses the configuration.

**Mode applicability:** TTRPG and Hybrid only. No Board Game equivalent (faction Thread orders are not tied to individual debate exchanges).
