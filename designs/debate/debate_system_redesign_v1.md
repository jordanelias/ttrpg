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

**What Burning Wheel gets right:** Scripted actions create the decision density that simultaneous rolling lacks. The compromise mechanic makes close debates more interesting than blowouts.

**What Burning Wheel gets wrong for Valoria:** Burning Wheel's three-volley scripting system is abstract — the actions don't map to recognisable rhetorical moves. "Obfuscate" and "Dismiss" are mechanical categories, not things a person actually does in a formal debate. The system also doesn't distinguish between different kinds of argument or different audience contexts.

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

**Audience Disposition tracking:** The audience has an initial Disposition set by the Game Master. Each exchange shifts it:
- Exchange won by Margin ≥ 3 (Overwhelming): +1 step toward winner
- Appeal to the Room success: ±1 step (per §3.4)
- Unmask: +2 steps toward the unmasking orator (vulnerability is persuasive) unless the revealed truth damages their position (Game Master call)
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

**Mixed audiences:** In Parliament, multiple factions are present. The Game Master determines the dominant faction(s) in the room. If no faction dominates, no resonance modifier applies.

**[EDITORIAL: Niflhel social mode]** — Niflhel characters should not access the formal Debate structure. Their social toolkit is Reading Exchange, private manipulation (Appeal against individuals), and Thread operations. They do not argue in public. This is a faction-asymmetric design that mirrors Niflhel's asymmetric military and Thread capabilities.

## 3.8 Thread Consequences by Genre

When a Debate concludes, the winning argument's genre determines the type of Thread consequence that fires (co-movement from the social event):

| Genre Won | Thread Consequence | Mechanism |
|---|---|---|
| **Evidence** | Pulling — temporal co-movement | The audience re-experiences the cited past. Observers with Thread Sensitivity 30+ perceive a thread-shimmer in the room. Rendering Stability +1. The past was invoked with enough force to disturb the present's temporal configuration. |
| **Character** | Co-movement — epistemic shift | An Overwhelming Character victory shifts how the audience renders the target's identity. Disposition change with all present witnesses. This is not Thread manipulation — it is the natural co-movement of an epistemic event at social scale. No Rendering Stability change unless a practitioner amplifies it. |
| **Consequence** | Actualization — Domain Echo | The argued future becomes a probability anchor. +1D on the first Domain Action pursuing that consequence within the season. The argument's force partially actualizes the future it described. Rendering Stability +1 if the consequence involves Thread-sensitive matters. |

**Classification [PP-461]:** §3.8 consequences are social co-movement events, not Thread operations. P-01 mandatory three-dimensional auto-effects do not apply. The three-dimensional descriptions above are narrative guidance for the Game Master, not mechanical mandates.

**Mandatory mechanical effects (fire automatically):** RS +1 for Evidence and Consequence genre wins. Disposition change with all witnesses for Character genre wins. Reputation shifts and rendering shifts: Game Master-narrated.

**Canon grounding (P-01, Inseparability):** These are three descriptions of the same co-movement. The system foregrounds one dimension per genre for mechanical clarity, but the Game Master should narrate all three dimensions shifting. Social events at sufficient scale always produce co-movement. Debate is high-intensity social rendering; the threads move.

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

**Casual Dispute (street, tavern, personal):** Simplified. 1 exchange only. No audience tracking. No Thread consequences. Proposer determined by who initiated the argument. If it escalates, the Game Master may upgrade to a Formal Debate with additional exchanges.

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

3. **[EDITORIAL: Concentration attribute — RESOLVED PP-460]** — Focus confirmed. Concentration = Focus + Presence. Poise deprecated.

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
## Version: v1.8 (PP-449–PP-468 applied 2026-04-08 — audit/sim pass: Refute Ob1, BG weight scope, Deadlock + Doubt Marker, Concentration editorial closure — SIM-SC-01 P1/P2 resolutions: genre adjacency, interaction names, resistance, Obscuring, TIE scope, Regroup, Composure, Thread co-movement classification)
## Parts 1–4 retained as design reference and historical/philosophical foundation

---

## NOTE ON STRUCTURE

Parts 1–4 document the quaestio-based design (five-phase exchange). The stress tests (v1 and v2) were conducted on a simpler exchange-based system with genre/orientation/Conviction Track mechanics. That simpler system produced better play outcomes and is the compiled operative specification below. The quaestio structure is preserved as a design reference and may be revisited as a variant for Grand Debate or formal academic settings. The faction resonance table (§3.7), thread consequences (§3.8), and corroboration mechanic (§3.5) carry forward unchanged.

---

## 6.0 Core Principle: Format Follows Context

The debate system does not have a fixed format. Exchange count, role structure, audience weight, and available actions all vary based on the institutional context and whether an audience is present. The Game Master sets the format at setup; players know it before the debate begins.

**What varies by context:**

| Variable | Private Negotiation | Parliamentary Session | Church Tribunal | Street Dispute |
|----------|--------------------|-----------------------|-----------------|----------------|
| Exchange count | 1–2 | 4–6 | 1–5 (Inquisitor sets) | 1 |
| Role structure | Symmetric, alternating | Symmetric, alternating | Asymmetric (Institution proposes throughout) | Initiator proposes |
| Audience | None (or named third party) | Faction delegates — weighted by composition | Church judges only | Bystanders (low resistance) |
| Audience resistance | 0 (no institutional inertia) | Average faction Stability − 1 | Halved for accused | 0 |
| Available actions | All | All | Accused cannot Call for Division | All |
| Thread consequences | Only on Unmask or extreme outcome | Standard | Standard | Only on Unmask |
| Conviction Track | Optional (or Game Master-narrated) | Active | Active (starts biased) | Optional |

**Audience presence changes the system fundamentally:**
- With audience: Conviction Track active. Genre weights apply. Audience resistance set by institutional composition.
- Without audience: No Conviction Track. Winner determined by exchange count. Strain still accumulates — the stakes are relational, not political.

**The Game Master declares at setup:**
1. Exchange count
2. Role structure (symmetric / asymmetric / who proposes)
3. Audience present? If yes: faction composition, resistance, starting track position
4. Available actions (any restrictions for this institutional context)
5. Stakes

This declaration is made before the first exchange. Players may not request format changes mid-debate.

**Debate initiation (Principle 1 — roll only when meaningful):** A Debate is initiated when: (a) two orators with opposed positions are present in an institutional context that recognises formal argument, AND (b) the outcome is uncertain and consequential. GMs should not call for a Debate when one side has no plausible case (institutional gatekeeping prevents the debate from being called), or when the outcome is predetermined by prior Domain Actions. [PP-107]

---

## 6.1 Game Master Setup (Before Debate Begins)

**Step 1 — Determine Primary Genre from the Question:**

| Question Type | Primary Genre |
|---|---|
| "Did X happen? / Was X done?" | Past |
| "Is X true? / Is this person fit?" | Present |
| "Should we do X? / What should be done?" | Future |

**Step 2 — Set Genre Weights from Audience Ethical Mode [PP-453]:**

Genre weights use an adjacency model based on the Past→Present→Future arc:

| Genre vs Question Type | Base Weight |
|---|---|
| Primary (matches question type) | ×1.0 |
| Adjacent (one step on arc) | ×0.75 |
| Opposed (two steps from primary) | ×0.5 |

Adjacency:
- Past primary: Present = adjacent (×0.75), Future = opposed (×0.5)
- Present primary: Past = adjacent (×0.75), Future = adjacent (×0.75) — Present is the central genre
- Future primary: Present = adjacent (×0.75), Past = opposed (×0.5)

Audience ethical mode boosts ONE genre by +0.25:
| Faction / Mode | Boosted Genre | Boosted Weight |
|---|---|---|
| Virtue ethics (Crown) | Present | ×1.25 if primary, ×1.0 if adjacent |
| Divine command (Church) | Past | ×1.25 if primary, ×1.0 if adjacent |
| Categorical imperative (Hafenmark) | Past | ×1.25 if primary, ×1.0 if adjacent |
| Consequentialism (Varfell) | Future | ×1.25 if primary, ×1.0 if adjacent |
| Moral relativism (Guilds) | GM chooses | ×1.25 on chosen genre |
| Rawlsian social contract (Restoration) | Future | ×1.25 if primary, ×1.0 if adjacent |

Weight range: 0.5–1.25. Fixed at setup. Do not shift dynamically. Record in ledger.

**Step 3 — Set Orientation Weights:**
- Revealing: ×1.0 (default)
- Obscuring: Obscuring does NOT move the Conviction Track toward the user's position. A winning Obscuring exchange places a **Doubt Marker** on the opponent instead (see §6.4).

**Step 4 — Set Conviction Track:**
- Scale: 0 to 10. Side A wins at ≥7. Side B wins at ≤3. Compromise zone: 4–6.
- Starting position: Game Master-set (typical neutral: 4–6). Record in ledger.
- Audience resistance: ceil(average Stability of represented factions / 4). Typical range: 1–2. Example: Hafenmark Stability 4 → ceil(4/4) = 1; Guilds Stability 5 → ceil(5/4) = 2. [PP-451 — aligned with params_debate PP-278]

**Step 5 — Define Stakes:** What each side wins, loses, or compromises on. Record before debate begins.

**Step 6 — Record all of the above in the hidden Game Master ledger before the first exchange.**

---

## 6.2 Derived Values

| Value | Formula |
|---|---|
| Presence modifier | max(0, floor((Presence − 3) / 2)) → Pres 1–3: +0; Pres 4–5: +1; Pres 6–7: +2. Minimum 0 — never negative. [PP-101] |
| Focus defence | floor(Focus / 2) → passive, no roll |
| Composure | Charisma (Cha) + 6. Range 7–13. Parallels Health = Endurance + 6. [PP-460, ED-127 resolved] |
| Concentration | Focus + Presence. Depletes per exchange (not during Regroup). Minimum 0. [PP-455] |
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
| Failure (0) | Misleading signal: Game Master identifies a genre as strong that is actually weak. Orator acts on false intelligence. |
| Partial (1) | Primary genre identified only. No orientation signal. |
| Success (2) | Primary genre + whether Revealing or Obscuring is preferred. |
| Overwhelming (3+) | Genre + orientation + one specific detail (swing faction, emotional state, key individual). |

**Step 2 — Choose:** Each orator selects genre (Past / Present / Future) and orientation (Revealing / Obscuring).

**Step 2b — Corroborate (optional) [PP-459, ED-014 resolved]:** Before rolling, a corroborator present at the debate may declare support. Any ally who witnessed the relevant events may corroborate. On success (Bonds, Ob 1, TN 7): primary orator gains +1D for this exchange's Argue roll. Knot holders give full Knot bonus (not capped at +1D). Knot is no longer required — witnessing is. Maximum one corroborator per side per exchange. Asymmetric proceedings: accused corroborators roll Bonds Ob 2 [PP-116]. GAP-DS-12 resolved.

**Step 2c — Refute (optional) [PP-465]:** Declared after opponent claims Memory bonus (+2D), before dice are rolled. Roll Recall (Rec) alone, TN 7, Ob 1.
| Degree | Effect |
|---|---|
| Failure | Refute fails. Opponent Memory bonus stands. |
| Success | Memory bonus denied. Opponent loses +2D. |
| Overwhelming | Memory bonus denied AND opponent −1D on Argue roll this exchange. |
Maximum one Refute per exchange per orator. Cannot Refute a Refute. If Memory bonus was already denied this exchange (prior Refute succeeded), a second Refute has no target and may not be declared.

**Step 3 — Argue:** Initiative holder declares argument and rolls first. Respondent hears declaration, then chooses genre/orientation and rolls.
- Pool: (Presence × 2) + History bonus, TN 7.
- **No fixed Ob.** Argue rolls are comparative margin-based, not Ob-based. The Read roll uses Ob 1 (Step 1). Argue rolls produce net successes feeding the margin formula — no independent Ob target. [PP-112 / GAP-DS-01]
- Memory bonus: +2D when citing a specific, named, verifiable claim (document, date, prior statement, named precedent). Binary. Available in any genre.
- **Momentum:** 1 Momentum may be spent before rolling to add 1 automatic success to the Argue result. Declared before dice rolled. Non-Thread rule per params_core. [PP-112 / GAP-DS-17]
- **Genre pivot:** No restriction on genre choice between exchanges. An orator may choose any genre each exchange. Genre weight applies normally — off-primary choices receive ×0.5 or ×1.5 weight per audience. [PP-112 / GAP-DS-07]

**Step 4 — Resolve by Interaction Type:**

**CLASH** (same genre, opposite orientation):
- Compare successes. Higher wins. Margin = difference.
- **Obscuring check fires first:** if the winner used Obscuring orientation, skip effective_margin formula — place Doubt Marker on opponent, no CT movement. [PP-450]
- **Revealing winner:** effective_margin = floor(margin × genre_weight). No orientation weight — Revealing weight is ×1.0 (identity; omitted). [PP-450]
- If effective_margin > resistance → Δ = effective_margin − resistance toward winner's position.
- If effective_margin ≤ resistance → 0 movement.
- Strain to loser: margin + 1 + winner's Presence modifier − loser's Focus defence. Minimum 1 strain. [PP-103]

**AMPLIFY** (same genre, same orientation) [renamed from COMPETITION — PP-452]:
- Combined pool resolution: both orators on same genre+orientation combine dice. Cap: highest individual pool × 2. [PP-242/250]
- Compare combined pool total successes vs opposing orator's successes. Margin = difference.
- Obscuring check fires first (same as CLASH). [PP-450]
- Revealing winner: effective_margin = floor(margin × genre_weight). CT movement if > resistance.
- Strain to loser: (margin − 1, min 1) + 1 + winner's Presence modifier − loser's Focus defence. Minimum 1 strain. [PP-103]

**CROSS** (different genres) [renamed from DIVERGENCE — PP-452]:
- No direct comparison. Each side evaluated independently. Resolution simultaneous. [PP-245]
- effective_margin for each = floor((successes / 2) × genre_weight). Orientation weight fixed at 1.0 for both (Obscuring in CROSS: if that side had the larger delta, place Doubt Marker instead of CT movement). [PP-099 retained]
- If net successes negative: effective_margin = 0 (no CT movement). No additional Concentration depletion — CROSS produces no winner/loser designation. [PP-456]
- For each side: if effective_margin > resistance → Δ = effective_margin − resistance toward that side's position.
- Net CT movement = difference of the two deltas, toward higher-delta side.
- No strain dealt. Neither argument attacked the other.
- Initiative stays with holder.
- **CROSS both-zero:** if both effective_margins = 0 (both below or at resistance), no CT movement, no strain, no initiative transfer. TIE rule does NOT apply to CROSS. [PP-449]

**TIE** (equal successes — CLASH or AMPLIFY only):
- Both orators take 1 strain.
- CT moves +1 toward initiative holder's position.
- Initiative stays with holder.
- Does not apply to CROSS. [PP-449]

**DOUBT MARKER** (placed on Obscuring win in CLASH, AMPLIFY, or CROSS):
- Opponent's next winning exchange: effective_margin reduced by 2 before resistance is applied.
- One active at a time. Second Obscuring win replaces existing Doubt Marker (no stacking). [PP-113]
- Consumed on use.
- **Design intent [PP-462]:** Doubt Marker is proportional — denies all movement against evenly-matched opponents (margin 2–3), reduces but does not cancel against dominant opponents (margin 5+). Obscuring is the tactically correct play when behind, not a universal denial.

**Deadlock State** (replaces "DIVERGE state" — PP-452):
- Declared by GM at exchange 3+ when both orators choose same orientation for 2+ consecutive exchanges.
- No Step 1/Appraise. No Choose. Direct pool vs pool, flat genre weights (×1.0 both sides). [ED-133/PP-313]
- Doubt Marker applies normally (reduces effective_margin by 2; GW=1.0 so effective_margin = margin before Doubt reduction). [PP-467]
- Regroup is available. Forfeiting does not trigger the exit condition (margin ≥2 exit requires an argued exchange win).
- Ends when one orator wins an argued exchange by margin ≥ 2.

**Step 5 — Forfeit actions [PP-454, PP-455]:**
- **Regroup:** Forfeit exchange. No argument, no strain, no CT movement. Concentration restores by max(Focus score, 2). Does not count as an exchange win or loss — no Concentration depletion this exchange. **Spent interaction:** If Concentration was 0 when Regroup declared, Regroup consumes the Spent state without applying the −2D/+1D penalty. Concentration restores to max(Focus, 2).
- **Concede a Point:** Forfeit exchange. Take 1 strain. CT moves +1 toward non-forfeiting side. Gain +1D on next exchange's argument roll. (Concede and Regroup are distinct: Regroup = neutral recovery; Concede = strategic retreat with a bonus.)

**Step 6 — Strain and Concentration:**
- Strain accumulates toward Composure.
- At strain ≥ Composure: **Rattled** — −2D to all debate rolls; Focus defence is lost (strain not reduced). Persists until Unmask or scene end. **Stacking with Spent:** If both Rattled and Spent are active simultaneously, penalties apply cumulatively (−4D total; opponent also gains +1D from Spent). Pool minimum of 1D (params_core) applies as the floor. [PP-106]
- Concentration depletes: −1 per exchange end. −1 additional on exchange loss (CLASH or AMPLIFY only — not CROSS, not Regroup). [PP-455, PP-456]
- Regroup: no Concentration depletion this exchange. Concentration restores instead.
- CROSS: no winner/loser designation — no additional −1. Standard −1 per exchange applies.
- Concentration minimum: 0. Multiple triggers cannot reduce below 0. Spent fires once when Concentration reaches 0. [PP-463]
- At Concentration 0: **Spent** — next exchange: −2D; opponent gets +1D. Concentration then resets to maximum.

**Step 7 — Game Master records exchange on hidden ledger.**

---

## 6.5 Post-Debate Resolution

- Game Master reveals ledger.
- Conviction Track position determines outcome: ≥7 = Side A wins; ≤3 = Side B wins; 4–6 = compromise (Game Master narrates partial outcome proportional to final position).
- Winner's final genre + orientation determines Thread co-movement type (see §3.8, which carries forward unchanged).
- Stakes resolve. **Domain Echo (canonical consequence by win type) [PP-110 — table stub; full table pending editorial]:**
  - Decisive win (Conviction Track ≥7 or ≤3) + Future genre: Domain Echo fires — winner gains +1D on first Domain Action pursuing the argued future within the season.
  - Decisive win + Evidence genre (Past): winning faction's Mandate +1 in the domain of the cited precedent.
  - Decisive win + Character genre (Present): Disposition change with all witnesses; Reputation shift (Game Master-set magnitude).
  - Compromise (4–6): No Domain Echo. Stakes partially resolve per final Conviction Track position proportional to win threshold distance.
- **Post-debate recovery:** All strain and Concentration depletion clear at scene end. Spent clears at scene end. [PP-108]
- **Debate Fatigue [PP-457]:** If an orator reaches Rattled threshold at any point during the debate, Debate Fatigue is set immediately — regardless of subsequent outcome (win, lose, concede, Unmask). Effect: −1D on their next social roll this session (Argue, Corroborate, or Circles); consumed after that roll. One instance per session. Clears at next session start if unused.
- **Total Victory [PP-114]:** If the winning side's final Conviction Track position is ≥ 9 (Side A) or ≤ 1 (Side B), the victory is Total. Additional consequences: losing faction's primary orator gains Debate Fatigue regardless of Rattled status; winning orator gains +1 Momentum (if below cap 4). In BG Parliamentary Vote, Total Victory additionally applies Mandate −1 to the losing coalition's dominant faction for one season. [GAP-DS-03 resolved]
- **Rendering Stability changes from debate [PP-122]:** Thread co-movement consequences from §3.8 (RS changes from genre-win) are subject to the RS ceiling (100) and RS=0 lockout. If RS = 100, no RS gain from debate fires. If RS = 0, the substrate is Ruptured — no RS changes from debate fire in either direction. Debate-generated RS changes follow the same ceiling/floor rules as direct Thread operations.

---

## 6.6 Faction Resonance Integration

The faction resonance table (§3.7) integrates with genre weights as follows:

The ethical mode adjustments in §6.1 Step 2 ARE the faction resonance system. The +0.5 genre adjustment is the mechanical expression of institutional receptiveness. The ±1D modifiers described in §3.7 are superseded by the genre weight system — genre weight ×1.5 captures the +1D effect more consistently.

Exception retained from §3.7: Niflhel does not participate in formal debate structures. Their social toolkit is Reading Exchange, private manipulation, and Thread operations only.

**Beliefs integration [PP-115]:** Winning an exchange while arguing for a position directly aligned with the orator's stated Belief counts as a Belief achievement for Momentum purposes (params_core: Momentum gained on Belief achieved). Game Master confirms alignment at exchange end. Maximum 1 Momentum per debate from Belief alignment. [GAP-DS-19 resolved / ED-054 resolved — PROVISIONAL]

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
| Church Tribunal | 1–5 (Inquisitor sets) | Inquisitor proposes throughout | Halved for accused. **Design note [PP-109]:** With Conviction Track starting at 6 (biased), boosted genre (Past ×1.5), and pool gap ≥ 4D, P(one-exchange resolution) ≈ 88%. GMs seeking dramatic Tribunal play should set exchange count ≥ 3 and start Conviction Track at 5 (neutral). Exchange count 1 is appropriate only for summary proceedings where the outcome is near-certain by intent. |
| Casual Dispute | 1 | Initiator proposes | N/A (no tracker) |

**Corroboration in asymmetric proceedings [PP-116]:** The accused or petitioner may have corroborators. In asymmetric proceedings, corroboration uses Bonds Ob 2 (vs Ob 1 symmetric). On failure: corroborator takes 1 strain. Advantaged party corroborates at standard Ob 1. [GAP-DS-18 resolved / ED-055 resolved — PROVISIONAL]

**Asymmetric strain [PP-116]:** The advantaged orator accumulates 0 strain from Divergence exchanges (design intent confirmed — institution's rhetorical weight means even losing arguments do not exhaust the institutional position). CLASH strain applies normally when advantaged side loses. [ED-058 resolved — PROVISIONAL]

---

## 6.8 Untested / Open Items

Items resolved in v1.4/v1.5 are marked ✓. Remaining open items retained for tracking.

| Item | Status |
|---|---|
| Multi-party debates (3+ orators) | ✓ Resolved — §6.12 Coalition Structure |
| Thread operations during debate | ✓ Resolved — §6.15; temporal axis conflict PP-123 |
| Corroboration §3.5 in practice | Partial — PP-104 stub; full port pending ED-051 |
| Parliamentary proceeding with new formulas | ✓ Tested — SIM-D-02, SIM-D-04 |
| Royal Audience proceeding | Open — P2, not yet stress-tested |
| Casual Dispute edge cases | Open — P3 |
| Regroup exploit in Grand Debate | ✓ Addressed — Concentration depletion PP-102 |
| Genre pivot mid-debate | ✓ Resolved — PP-112 (unrestricted between exchanges) |
| Rattled → Unmask decision point | Open — P2, not yet triggered in simulation |
| Multiple Doubt Markers in same exchange | ✓ Resolved — PP-113 (replacement rule) |
| Mixed Guilds audience calibration | Open — P2 |
| BG Parliamentary Vote | ✓ Resolved — §6.13 |
| Hybrid Debate | ✓ Resolved — §6.14 |
| Pre-Debate Preparation | ✓ Resolved — §6.11 |
| Thread temporal axis conflict | ✓ PP-123 provisional |

---

## 6.9 Updated Open Items (Part 5 superseded by this list)

All items from §5.1 carry forward, plus additions from stress tests:

**Mechanical — resolved in v1.4/v1.5 (all below):**
- [GAP-DS-01] ✓ PP-112 — no fixed Ob; comparative margin-based.
- [GAP-DS-02] ✓ §6.15 — between-exchange Thread procedure.
- [GAP-DS-03] ✓ PP-114 — Total Victory consequences.
- [GAP-DS-04] ✓ §6.11 — prep roll for TTRPG; Diplomacy action for BG.
- [GAP-DS-05] ✓ §6.13 — BG Parliamentary Vote.
- [GAP-DS-06] ✓ §6.12 — Coalition Structure.
- [GAP-DS-07] ✓ PP-112 — genre pivot unrestricted between exchanges.
- [GAP-DS-08] ✓ PP-113 — replacement intentional, no stacking.

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
## 6.11 Pre-Debate Preparation

Available when an orator has deliberate preparation time before a formal debate. Not available for impromptu debates (Street Dispute, surprise confrontation).

**Pool:** Attunement + most relevant History, TN 7, Ob 1.

| Degree | Effect |
|--------|--------|
| Failure/Partial | No effect. |
| Success | +1D on Exchange 1 Argue roll only. |
| Overwhelming | +1D on Exchange 1 Argue roll AND Exchange 1 Read uses TN 6 instead of TN 7. |

**Time requirement:** At least 1 hour of deliberate preparation. Rushed preparation (less than 1 hour): TN 8.

**Cross-mode:** TTRPG and Hybrid only. In BG Parliamentary Vote, a faction that spent a Diplomacy domain action targeting the vote's subject in the preceding season gains +1D on their vote roll. [GAP-DS-04 resolved]

---

## 6.12 Multi-Party Debate — Coalition Structure

Use when more than two orators debate. Niflhel characters are excluded from formal coalitions (see §6.6).

**Declaration:** Each orator declares Side A or Side B at setup. No side-switching after declaration. Non-declaring orators are neutral observers (no mechanical participation).

**Lead orator:** Each side nominates one Lead per exchange. Lead may change between exchanges. Any coalition member may lead.

**Corroboration:** Non-lead coalition members may Corroborate the lead per Step 2b (§6.4). Maximum 1 corroborator per side per exchange regardless of coalition size. Only the first declared corroborator counts per exchange.

**Composure and Rattled:** Tracked individually. A Rattled orator cannot lead or Corroborate. If all orators on one side are Rattled simultaneously, that side must Regroup for the next exchange.

**Concentration:** Tracked individually. Only the Lead's Concentration depletes each exchange. Non-leading coalition members' Concentration is unchanged while they are not leading. This is the coalition endurance advantage — not greater movement per exchange, but sustained fresh leads when the opposing side is fatigued.

**Initiative:** Transfers to the winning side. That side nominates who holds initiative for the next exchange.

**Cross-mode:** In BG Parliamentary Vote (§6.13), factions pool their Mandate dice — this is the BG equivalent of coalition corroboration. [GAP-DS-06 resolved]

**Design note:** Corroboration's +1D bonus is most impactful in CLASH and COMPETITION exchanges (where margin determines movement and strain) and negligible in DIVERGENCE exchanges (where the /2 halving in the effective_margin formula absorbs the bonus die). Coalitions benefit most from corroboration when they can force CLASH exchanges by reading the opponent's genre and matching it. [PP-117]

---

## 6.13 Board Game Parliamentary Vote

Faction-level debate resolution for BG scale. Use when the scene is narrated at BG scale. To zoom into personal scale, use §6.14 (Hybrid Debate).

### BG Vote Setup

**Step 1 — Declare sides:** Each participating faction declares Side A or Side B. Non-declaring factions Abstain — they do not contribute pool dice.

**Step 2 — Genre and weights:** Same as §6.1 Steps 1–2, including the PP-453 adjacency model. Each side declares one genre for all its factions. Weights: primary ×1.0, adjacent ×0.75, opposed ×0.5, with +0.25 boost from audience ethical mode. [PP-466]

**Step 3 — Resistance:** Base 0. Parliament is the institution — no external audience resistance. If a faction with Stability ≥ 6 Abstains: +1 to resistance (maximum +2 from all Abstains). This represents the political weight of their neutrality.

**Step 4 — Starting Conviction Track:** Position 5 (neutral) unless prior lobbying shifted it. Each successful Diplomacy domain action targeting this vote in the preceding season: +1 to starting Conviction Track toward the lobbying side (maximum ±2 from lobbying).

### BG Vote Resolution

**Pool:** Sum of Mandate of all factions on each side. Roll combined pool TN 7.

**effective_vote for each side:** floor(net_successes × genre_weight)

**Movement:** If effective_vote > resistance → Δ = effective_vote − resistance. Apply both deltas; net Conviction Track movement = Δ_A − Δ_B.

**Resolution:** Conviction Track ≥ 7 = motion passes; Conviction Track ≤ 3 = motion fails; Conviction Track 4–6 = motion referred to committee (no immediate change, may be raised next season). **Zero-zero ruling [PP-117]:** If both sides produce effective_vote = 0 (both fail to exceed resistance), motion is automatically referred to committee regardless of Conviction Track position. The TTRPG TIE rule does not apply at BG scale — there is no initiative holder.

**Multi-round:** If no threshold reached after 1 round, each subsequent season's Parliament may vote again (1 Domain Action slot per participating faction). Factions may spend Diplomacy domain actions between rounds for +1D to their coalition's next roll (maximum +2D from lobbying).

**Thread consequences:** Do not fire from BG Parliamentary Vote. Thread co-movement requires personal-scale argument. [Commensurate with R-65 mode restriction]

**Orientation absent by design [PP-119]:** BG Parliamentary Vote has no Obscuring/Doubt Marker equivalent. Factions vote publicly — personal-scale rhetorical deflection does not apply at faction-pool level. This is an intentional abstraction: BG scale removes orientation tactics, retaining only genre choice and pool size.

**Genre pivot between rounds [PP-119]:** Sides may change their genre declaration between vote rounds. Pivoting to a secondary-weight genre (e.g., switching to Past ×0.5 for a Crown audience) is permitted but rarely advantageous — genre weight is determined by audience ethical mode, which does not change between rounds.

**Total Victory in BG:** Conviction Track ≥ 9 or ≤ 1 after a round → losing coalition's dominant faction takes Mandate −1 for one season. [GAP-DS-05 resolved / ED-053 resolved]

---

## 6.14 Hybrid Debate

Use when a named character is present and their personal skill matters, but faction-level forces are also in play.

**Step 1 — BG layer:** Run one round of BG Parliamentary Vote (§6.13) using faction pools. Apply Conviction Track offset, capped at ±2 from neutral (5) regardless of actual Δ.

**Step 2 — Set TTRPG starting Conviction Track:** Neutral 5 ± capped BG offset, then clamped to the compromise zone (4–6). The personal debate always begins in compromise — faction lobbying determines where within that zone, not whether the outcome is pre-decided. [PP-120 PROVISIONAL]

| BG offset | Starting TC |
|-----------|------------|
| +2 toward Side A | 6 (Side A dominant compromise) |
| +1 toward Side A | 6 |
| 0 | 5 (neutral) |
| +1 toward Side B | 4 |
| +2 toward Side B | 4 (Side B dominant compromise) |

Rationale: A TC starting at 7 or above pre-decides the outcome before named characters speak, making the Hybrid debate scene dramatically hollow. The clamp to 4–6 ensures personal skill always matters.

**Step 3 — TTRPG personal debate:** Run standard Formal Debate (3 exchanges) or Grand Debate (5 exchanges) per §6.4–§6.9 from the adjusted starting Conviction Track. **Exchange count is determined by the Game Master based on context (same as pure TTRPG), not by the number of BG vote rounds. These are independent parameters.** [PP-118]

**Step 4 — Resolution:** Final TTRPG Conviction Track position determines outcome. Faction stat consequences apply as in TTRPG debates. Thread consequences may fire (personal-scale argument satisfies the requirement).

**Rendering Stability propagation:** If the TTRPG debate's winning genre triggers an Rendering Stability change (§3.8), apply to TTRPG-layer Rendering Stability. BG layer has no Rendering Stability equivalent. Domain Echo affecting BG faction stats propagates through normal Domain Echo procedure. [ED-056 resolved / ED-057 resolved — PROVISIONAL]

**Design intent:** The BG layer sets political environment (faction strength, prior lobbying); the TTRPG layer resolves the decisive personal moment. A weaker faction's named character can overcome institutional disadvantage through personal skill.

---

## 6.15 Thread Operations In and Around Debate

### During Argue Step
Practitioner Weaving bonus (R-65, §6.10) applies when the practitioner declares Weaving before rolling in Step 3. Visible to all observers.

### Between Exchanges
A practitioner may initiate a Thread operation between exchanges (after Step 7, before the next Step 1). Procedure:
1. Declare at end of exchange (after Game Master records).
2. Resolve Thread operation per threadwork rules (roll, dimensional auto-effects, Coherence check).
3. Effects apply before next exchange's Read step.

| Operation | Debate Effect |
|-----------|--------------|
| W-42 / audience-affecting Weave | Shifts audience Disposition (Game Master narrates). Does NOT change genre weights — weights are institutional, fixed at setup. May shift next Read roll difficulty by ±1 TN (Game Master discretion). |
| R-65 continuation | If practitioner used R-65 during prior Argue step, bonus continues automatically into next exchange — no additional between-exchange action. |
| Personal operations (Dissolution, Pulling, etc.) | No debate effect. Affects practitioner's own Rendering Stability/Coherence only. |

**Genre weights are fixed at setup.** Thread operations cannot change them mid-debate.

**Temporal axis conflict [PP-123 PROVISIONAL]:** When a practitioner conducts a between-exchange Thread operation whose temporal axis contradicts the current debate's primary genre — specifically, a Past-axis operation (Past-Oriented Pulling, or any operation whose temporal auto-effect invokes historical configurations) during a Future-primary debate, or a Future-axis operation during a Past-primary debate — both orators' Read rolls in the immediately following exchange use TN 8 (Desperate) instead of TN 7. The temporal cross-contamination from the Thread operation makes audience state harder to read. This applies only to operations with explicit temporal auto-effects. Neutral operations (Mending, Locking) and same-axis operations (Weaving Present during Present-genre debate) do not trigger this penalty.

**Church Heresy Investigation:** Observed Thread operation during debate (at any point) → Church may immediately file Heresy Investigation Domain Action (Ob 2 vs practitioner's faction Mandate). [GAP-DS-02 resolved]

**Exception [PP-121 PROVISIONAL]:** The Church does not initiate Heresy Investigation against its own ordained members (Cardinals, Confessors, ordained priests) who use Thread operations in demonstrable support of Church institutional interests during a debate. Opposing factions who observe the operation may still file a Heresy Investigation as their own Domain Action. The distinction: Church self-policing vs. faction-level accusation.

---

## 6.10 PRACTITIONER WEAVING IN DEBATES (R-65)

Confirmed pool formula: **(Presence × 2) + History bonus, TN 7.**

Note: SIM-DEBT-01 RESOLVED (2026-04-02). Stress tests SIM-D-01 and SIM-D-02 confirmed calibration under (Presence × 2) + History pool. See references/params_debate.md for updated baselines.

### R-65 — Practitioner Weaving Bonus in Debates
A practitioner with Thread Sensitivity ≥ 30 who is actively in Thread contact during a Debate exchange adds bonus dice to their pool equal to floor(Thread Sensitivity ÷ 30):
- Thread Sensitivity 30–59: +1D
- Thread Sensitivity 60–89: +2D
- Thread Sensitivity 90+: +3D

The practitioner must declare the Weaving before rolling. The operation is visible to all observers (practitioner is in contact while debating). Church may immediately call for Heresy Investigation on observation. After the exchange, the practitioner makes a Coherence check at Ob 1 — maintaining Debate and Thread contact simultaneously stresses the configuration.

**Mode applicability:** TTRPG and Hybrid only. No Board Game equivalent (faction Thread orders are not tied to individual debate exchanges).
