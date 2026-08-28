# Game Precedent Companion — What Other Games Did, and What Held

## Status: PROPOSED (2026-08-28) · reference under §0.05, not canon
## Version: v1.0 · Lane: IN (cross-cutting)
## Companion to: `valoria_systems_integration_master_v1{,_part2,_part3,_part4}.md`
## Parts: this file (the corpus · the survey by system) · `_part2` (cross-comparison · complements · synergies · the steal/refuse table)

**Reading order:** [Part 1 · The Corpus and the Survey](valoria_game_precedent_companion_v1.md) → [Part 2 · Comparison, Complements, Synergies](valoria_game_precedent_companion_v1_part2.md)

**What this is.** The integration master says what Valoria *has*. This says what everyone else
*built*, where it held, and where it broke — collated from every game-precedent pass in the
repository and compared across them.

**What it is not.** It is not a case that Valoria should imitate anything. Roughly a third of the
findings below are **nulls** — problems the genre has not solved, or has solved four different ways
and abandoned three. Those are the most useful entries, because a null tells you that you are not
behind; you are early.

---

## §1 THE CORPUS

### 1.1 Three independent research programs, not one

The game-precedent material in this tree was produced by three programs that never read each other.
That independence is what makes the convergences in `_part2` §3 worth anything.

| program | where it lives | what it surveyed | method |
|---|---|---|---|
| **Political mechanics** (2026-08-06) | `audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md` §3 | TTRPG debate systems, courtroom adventure games, narrative RPGs, grand strategy, and seven negotiation board games | Built the primitive catalogue upward from named historical mechanisms **and named existing game systems**; a primitive had to appear in two independent historical systems, or one historical and one game, to qualify |
| **Personnel and muster** (2026-08-27) | `research/personnel_muster_integration_master_v1.md` §§2, 3–8 | Nine passes: Romance of the Three Kingdoms VI–XIII · Nobunaga's Ambition · CK2/CK3 · Total War (Medieval II, Empire, Shogun 2, Rome II, Attila, Warhammer, Three Kingdoms) · Jagged Alliance 1/2/v1.13/3 · Brigandine · Unicorn Overlord · Tactics Ogre · Triangle Strategy · Radiata Stories | Five lanes on personnel, four on mustering, each reporting a convergence count across lanes |
| **Failure dossiers P1–P5** (2026-08-25) | `proposals/2026-08-25-throughlines-and-precedent/08_ch5_what_we_should_not_do.md`, and cited through chapters 1–4 | Imperator: Rome · EU4 · Victoria 3 · CK3 · Shadow of War · Dwarf Fortress · Nemesis system · Wildermyth · Burning Wheel · Blades in the Dark · Wave Function Collapse · Total War autoresolve · Dominions · Mount & Blade · Caves of Qud · Ultima Ratio Regum | Inverted: every mechanism the other chapters *recommended* had to arrive with a shipped precedent that **failed while holding it** |

**Two attribution notes, because the lane structure hides them.** The **KOEI lane** merged *Romance
of the Three Kingdoms* VI–XIII and *Nobunaga's Ambition* (1983, Sphere of Influence, Iron Triangle,
Awakening) into one pass, so findings credited to "RoTK" below are the lane's, drawn from whichever
title the fetched sources documented — the *RoTK 8 Remake* and *Awakening* manuals were the two that
fetched, which is why the specific numbers cluster there. And **Tactics Ogre (SNES/PSP/Reborn) was
surveyed and produced no attributable finding that survived into the tree.** It is on the source list
and nowhere else; said plainly so its presence on the roster is not read as coverage.

A fourth body — `audit/2026-07-09-comparative-governance-research/` and
`research/fa_se_historical_precedent_research_v1.md` — is **historical**, not ludic: Byzantium, Song–Ming
China, feudal Japan, the HRE, Venice, Renaissance Italy, Habsburg Spain. It is cited here only where a
game and an institution converge on the same shape, because that coincidence is the strongest form of
evidence in the corpus. Do not read this document as a survey of it.

### 1.2 The sourcing floor, stated once and binding throughout

The personnel program records it plainly and it applies to everything numeric below: **fan wikis were
bot-walled almost everywhere.** `ck3.paradoxwikis.com`, `ck2.paradoxwikis.com` and
`forum.paradoxplaza.com` returned 403 to two independent agents; `koei.fandom.com` and `neoseeker.com`
returned 402/403; the Brigandine and Unicorn Overlord wikis would not load. The load-bearing numbers
rest on guide sites, forum synthesis, `acoup.blog`, and the handful of official manuals that do fetch
(Koei Tecmo's *Awakening* and *RoTK 8 Remake* manuals, Total War Academy, the JA2 v1.13 docs).

**So: treat every specific number as a lead, not a settled fact. The durable findings are the
convergences, which are structural rather than numeric.** Several dossier claims are additionally
marked `[UNVERIFIED]` or community-derived at source — notably the Dominions assassination-meta claim,
the *Duel of Wits* 21-vs-11 account, and the whole Blades failure corpus — and those marks are
preserved here rather than laundered.

Two claims are stronger than the rest because they come from official documentation or from published
rules: Victoria 3's law-enactment arithmetic (game files, via the official wiki), Pax Pamir 2e's
market pricing (rulebook), and Burning Wheel's *Duel of Wits* structure (Burning Wheel Gold).

---

## §2 THE SURVEY, BY SYSTEM

Organised against the integration master's ten systems so the two documents index into each other.
Each subsection: **what the games do · where it broke · what it means for a d10/TN-7 no-GM engine.**

---

### 2.1 Faction strategy — the action economy

**What they do.** Nobody surveyed resolves a faction's season with a single weighted draw.

- **Victoria 3** composes government from **interest groups holding clout**; the rest are opposition.
  Legitimacy (0–100) derives principally from the total clout of governing groups. Below 25, the
  government cannot pass any law except one supported by an active movement, and an enactment already
  in progress makes no progress at all.
- **CK3** makes vassal obligations **negotiable contracts**, and **crown authority** has four levels
  that gate what the liege may do *at all* — at the lowest, vassals may war on each other and the
  liege can only ask them to stop; only at level two can succession law be changed or titles revoked.
- **Old World** emits a ruler's goals from the intersection of his own attitudes **and the desires of
  the most influential families**; when he dies, outstanding ambitions go on a clock.
- **John Company** makes most successful ventures require the cooperation of **several offices held by
  different players**, with two voting layers, one of which can change the game's own rules.
- **Kremlin** is the sharpest: players do not own politicians. They hold **influence over** politicians
  arranged in a pyramid, and the politicians age and die.

**Where it broke.** Devereaux's reading of CK3 is the one to carry: it has mechanics for wanting
vassals and for vassals making life difficult, but is *"set up so you can generally succeed at things
kings wanted to do but were unable to pull off"*, with personal-opinion bonuses papering over
structural factors. The dossier turns that into a constraint: **cap the influence of affection — some
conflicts must be positional and unbuyable.**

**For Valoria.** Every one of these gives a faction an *interior* — an office structure, a family
network, a contract, a mortality clock. Valoria's faction personality is `if faction.name == 'Crown'`.
The cheapest of the five to reach is Old World's: goals emitted by a person crossed with the houses
around him, expiring on death. It needs the person object and nothing else.

---

### 2.2 Parliament — deliberation, and the enactment of law

**What they do.** This is the best-served system in the survey, and one loan dominates.

**Victoria 3's law enactment is a process, not a toggle**, and the dossier calls it *the single most
important structural loan* in the political survey:

- Multi-stage, each stage with a **running success chance and a stall chance**. Governing interest
  groups and non-passive supporting movements add to success; all non-marginalized opposing groups and
  movements add to stall. The ruler's stance adds ±5% per step of difference.
- **Three setbacks over the process and the enactment fails**, locking the law out for two years.
- Base 100 days per stage; governing-principle laws double, power-distribution and economic-system
  laws 1.5×; legitimacy above 90 cuts 25%, legitimacy 25–49 adds 50%.
- **And the half most designs omit: attempting the measure mobilizes the opposition.** Participation in
  opposing movements rises on attempt — half immediately, the rest bleeding in weekly — and above a
  threshold, revolution. *Reform must be able to make things worse.*

Around it, four procedural loans the survey grounds in Rome and Ming China rather than in games,
because no game implements them:

- **Agenda control** (*relatio*) — the presiding officer states the question, and *the wording fixes
  which question the body is even sitting at.*
- **Division** (*discessio*) — where several conflicting motions are live, **the chair chooses which to
  put and in what order**, voting singly until one carries. Agenda order is the chair's weapon.
- **Recorded defeat** (*senatus auctoritas*) — a motion that carried and was vetoed persists as a
  record with no force and full citability. The survey's verdict: *"very few games have this and it is
  nearly free to implement."*
- **Drafting right** (*piaoni*) — whoever drafts the response frames the decision the superior then
  ratifies or rejects. Models bureaucratic power with **no power stat at all**: the clerk who drafts
  outranks the minister who signs.

**And one board-game rule the survey calls non-optional:** *The Republic of Rome*'s **shared loss** —
foreign threat and popular unrest can destroy the state and everyone loses. Without it, an assembly of
self-interested actors never agrees and obstruction has no ceiling.

**Where it broke.** **EU4's estates** are the canonical *ignorable* mechanic — legible,
well-motivated, and tuned so its failure state is rarely reached; players "hardly even bother",
because the loyalty floor sat near 40 and nothing crossed it. The lesson binds every threshold in this
system: **a mechanism engineered not to fire is indistinguishable from one that does not exist.**

**For Valoria.** The master document's parliament findings and this survey meet exactly: Valoria has
the vote and none of the procedure. It has no agenda control (the bridge derives *who*, never *what*),
no chair, no recorded defeat, no drafting layer, and no shared-loss condition. It does have the one
thing V3 warns about — a rider that fires every season regardless — which is the opposite failure from
EU4's.

---

### 2.3 Settlement governance — the appointed governor

**What they do — and this is the corpus's most important null.**

> **Total War added, removed and re-added the governor role three times, for three different reasons,
> across twenty years.** The personnel program's verdict, verbatim: *"There is no convergent answer —
> this is a real, unsettled design tension, not a solved problem you are behind on."*

What the surveyed games *do* supply is narrower and better:

- **RoTK's domestic-action table** is the closest live template: eight commands, each keyed to one of
  four stats, flat 10 gold per officer — and **Commerce, Cultivate and Conscript all drop Safety.**
  Every gain costs you elsewhere, arrived at independently of Valoria's own verb tradeoffs.
- **CK's council-seat denial**, scaled down: a powerful figure passed over accrues a flat −40 opinion.
  You need no Council institution to get the payoff — you need *"a named NPC who wanted a post and
  didn't get it accrues a Grudge tag"*, which is one line in an appointment flow.
- **Medieval II's trait triggers** are the franchise's best-loved character mechanic and map onto a tag
  ledger. The lesson is *keep the triggers legible*, not *add more tags*.
- **CK3's landless-adventurer track**: demotion must be **its own game, not a debuff.** A demoted
  officer that merely loses bonuses is a subtraction, and subtractions are not play. What is needed is
  a game-mode/action-set flag per band, not a multiplier on existing actions.

**Where it broke.** **Dwarf Fortress supplies the counter-warning**: demotion with no residual reads
consequence-free once survived. A comeback that resets to zero is a reset button. And **Imperator:
Rome** is the arithmetic warning — governors lost 20+ loyalty on appointment alone and bled regardless
of play; Paradox scrapped the whole action-currency four months later. The rule that falls out:
**test the down-direction against the best-case counter-investment, not the average.** If the fastest
possible remediation still nets negative, the mechanic is broken, not hard.

**For Valoria.** The CK3/DF pair is answered by one object, and Valoria already has it: durable ledger
tags surviving succession. `succeed_governor` calls `ledger_sweep`, and durable tags (`ttl=None`)
always survive the handover — *the exact property DF lacks.* It has never run, and no tag writer of
any kind exists.

---

### 2.4 Territory — conquest, and the terms of submission

**What they do.** The games are thinner here than the history is, and the survey says so.

- The load-bearing loan is **Venice's *dedizione***: cities submitted through **negotiated pacts**
  rather than annexation, keeping local statutes, tax exemptions, guild privileges and communal
  councils in exchange for loyalty and appellate supremacy. Generalised in the primitive catalogue as
  a **Charter of Submission**: *conquest should produce a negotiation, not a colour change. What you
  leave standing determines what governing costs for the rest of the game.*
- **Split command** — the Venetian *rettori* (a *podestà* over civil justice, a *capitano* over
  military affairs) and the Carolingian *missi* in lay-and-ecclesiastic pairs. Neither officer can
  defect alone, and the player who holds one must court the other.
- **Decree with compliance** — a decree lands in each locality with a *compliance roll*, not an
  effect. The survey names the failure of the instant-global-decree as *"the single most common error
  in governance games"*, and grounds the fix in the capitulary record, which repeatedly re-prohibits
  the same abuses — documentary proof that promulgation did not equal enforcement.
- **Assessment** — a survey converting heterogeneous holdings into one comparable number, which then
  becomes the base of every later obligation. The design instruction is unusually strong: *make the
  survey playable.* Deciding to assess, choosing the assessors, and adjudicating the resistance is a
  better governance scene than any budget screen.

**For Valoria.** Its conquest is a colour change: ownership transfers immediately, the designed
three-season Occupation phase is skipped, and no charter is negotiated. The Entry Terms fork
(Confirm Privileges vs Impose Administration) is the *dedizione* shape and is the only authored rule
anywhere that seeds settlement Legitimacy.

---

### 2.5 People — rosters, rank, loyalty and defection

This is the deepest-surveyed system, with five independent lanes, and it produced the corpus's two
hardest design rules.

**Rule 1 — legible inputs, fuzzy thresholds (5/5 lanes).** Every surveyed game keeps the *defection
threshold* unpublished while making the *inputs* visible: Three Kingdoms' Satisfaction, JA2's hidden
tolerance clock, RoTK's `LOY ≤ 70` recruiter-side tell, Triangle Strategy's hidden per-character
number, CK's opinion floor under opaque dread interplay.

Independently, **4/5 lanes show legibility is what separates a celebrated system from a resented
one** — JA2's social layer is loved and its tactical math resented *in the same game*, and v1.13's fix
**exposed the models rather than changing them**, shipping an audit tool itemising every pairwise
opinion by source.

> For a **no-GM engine** these combine into a hard constraint: *you owe the player the reasons, never
> the trigger point.* There is nobody to narrate why a governor defected.

**Shogun 2 supplies the presentation form** that makes hiding non-arbitrary: a **visible band over a
hidden precise value**. That is what keeps a demotion from reading as capricious.

**Rule 2 — JA3, not JA2.** Every lane recommended its own game's full apparatus. **Jagged Alliance 3
compressed JA2's five-layer morale stack, ±25 pairwise matrix, event deltas and prejudice axes into
"liked squadmate present: +1 AP; disliked: −1 AP"** without losing the feel. That is the ambition
ceiling for a d10/TN-7 engine and the antidote to importing five games' worth of machinery.

**Every game punishes idleness (4/5 lanes).** JA2 docks both merc morale and town loyalty after three
days without offensive action; Three Kingdoms loses satisfaction for idle characters and names *"give
them something to do"* as the top mitigation; CK's unlanded courtiers leave at a base 2%/month; RoTK
officers want posts. **Valoria has no state that degrades from neglect** — an unassigned person is
inert, not restless.

**Population: generate on demand, not on a clock (2/2 converging lanes, against their own subject).**
The CK lane argued *against* importing CK3's population model, citing its documented symptoms —
roughly 6–7 parentless sixteen-year-olds spawning monthly, late-game saves past ~24,000 characters,
two community mods pulling in **opposite** directions, and Paradox's own fix throttling the tap at the
low-value tail. The Radiata Stories lane found 175 NPCs affordable *because each is a config row* with
a static 2–3 block schedule — but that schedule is pure spatial theatre gating fetch-quests, with zero
connection to persuasion or office-holding. **Port the principle (cheap row, theatre not simulation)
onto the axes that carry your mechanics, not onto clock-time.**

**Where it broke.** **Shadow of War's War Chests** — buying the *output* of an earned relationship
corroded the system **for non-payers too**, by breaking the causal chain; Monolith removed the market.
The guard: no convenience path may produce a relational outcome the history does not justify.

**Vocabulary.** The Total War lane recommended adopting Three Kingdoms' "Administrator" and the
personnel program **rejected it** — *governor* is already canonical, in code, and carries
settlement-residence semantics TK's Administrator explicitly lacks. The overloaded term is **officer**,
which mass battle owns as the unit commander.

---

### 2.6 Economy — the levy, and what a soldier costs

**The strongest structural finding in the muster research: split levy from professional (4/4 lanes).**

- **CK is explicit**: **levies cost zero gold to raise or hold** — a standing entitlement drawn down,
  rationed *politically* (contract %, control, opinion) and *temporally* (muster travel time), never
  economically. Men-at-arms cost gold plus prestige, carry maintenance **even while unraised**, and
  maintenance **roughly triples once fielded**.
- **Shogun 2** implements the same split as a *starting-stat delta*: 0-honour ashigaru begin at −4
  morale with essentially no building requirements; samurai sit behind building chains.
- **JA2** prices its two channels so the bought option is **strictly worse on economics and wins only
  on speed**: ~$75/head to train green militia against $440/head for bought regulars, 2× the daily
  upkeep, *plus* the loyalty tax training doesn't carry.

**Recruitment costs consent, not only money (2/4 lanes).** JA2's Kerberus channel charges town loyalty
**per unit purchased** — 0.1 per regular, 0.15 per veteran — **globally, not to the receiving
sector**, rationalised as *"the population is wary of foreign guns with no ties to the country."*
Quality and consent-cost move together: veterans cost 50% more loyalty per head. RoTK VIII Remake
drops city public order on Conscript, and below 25 order (revolt) **conscription is unavailable
entirely**.

**And an enemy action nobody else has**: in RoTK VIII, enemy schemes deliberately lower a rival city's
order **specifically to block its recruitment.**

**For Valoria.** Its Muster is *already the professional model wearing a generic label* — ED-FA-0009's
grounding is Wallenstein, a mercenary contractor paid regardless, which is not a feudal levy. And the
precedent for splitting a ratified action exists inside Valoria's own canon: Knights Templar are
raised by Sacred Assembly at Ob 3 with no Wealth roll and a cap of 2, explicitly "not standard Muster".

---

### 2.7 Mass battle — and the personal↔mass seam

**The corpus's hardest null, and it is worth quoting rather than paraphrasing:**

> *"No precedent in this survey demonstrates a mechanism whose personal-scale contribution is provably
> leverage-in-band across the full range from N=1 to N=1000+."*

Every surveyed mechanism is one of two poles:

- **Scale-blind (flat)** — dominates a small mass, evaporates in a large one. **Dominions'** single-
  commander rout: *"the biggest army in the universe will rout if it is led by a single commander, and
  he is killed"* `[UNVERIFIED — player-community consensus]`. **Total War's** lord aura is the same
  shape.
- **Fully fused** — one engine, consistent, and the personal actor becomes **irrelevant as N grows**.
  **Mount & Blade** is the case.

The reading the dossier adds, and the one that matters: these are best read as evidence that
**well-funded teams tried and did not solve it**, not that nobody looked.

**What the games do supply, and it is genuinely useful:**

- **Garrison is an assignment, never a unit type (4/4 convergence)** — JA2, Brigandine, Unicorn
  Overlord and Total War all treat garrison-versus-field as *the same unit pool wearing a different
  assignment*. Do not build a garrison troop type. (Open fork: JA2's garrison units *can* move
  offensively, and it is a major feature.)
- **Gate troop types on officer CLASS, not biography (Total War: Three Kingdoms).** Strategists unlock
  ranged and siege; *"a mixed-archetype army is the intended way to access a full unit roster."* And
  TK's version fixes the failure mode: gate on a **class** and losing a person means promoting
  another; gate on *biography* — "the officer with Cavalry History" — and losing one person costs you
  cavalry permanently.
- **Two-tier defeat severity (Three Kingdoms).** A general's death destroys his retinue **only if the
  whole army also routs**; partial defeat preserves the formation.
- **Proximity-at-rout (Brigandine).** Knights never die, they retreat; what is permanently lost are
  the monsters killed **or stranded outside the knight's Rune Area when he retreats.** *The commander
  is a reusable chassis; the army under him is the consumable.*

**What nobody does, and Valoria should defend rather than justify.** 4/4 franchises cap unit
**quantity** by rank or title (RoTK Class → troops per unit; RoTK VI rank → command cap; CK title →
2–5 regiment slots; Rome II Imperium → army count). **None caps how good a unit can be** by a faction
scalar, and CK explicitly lets effectiveness climb open-endedly. Valoria's Military-as-quality-ceiling
is unprecedented — keep it as a deliberate statement of faction military culture, and do not cite
precedent for it. Note Shogun 2's softer counter-model: ashigaru start worse but *can* earn honour, so
their gap is a floor, not a ceiling.

---

### 2.8 Cross-scale — the fidelity ladder, and the second resolver

**The framing is Jordan's own, from 2026-07-08:** *"faction parliament actions are the auto-resolve
version of playing them out as a scene, in parallel to Total War where you can play the battle or auto
it."*

**Two precedents, and they are not the same shape.**

- **Football Manager is the clean one.** Every **fixture is specific** — this match, these players,
  this rivalry — resolved at three fidelities of the **same match engine**: full match / commentary /
  instant result, *calibrated so instant ≈ played.*
- **Total War is the cautionary one.** Auto-resolve is a **different algorithm** from the battle
  engine. The divergence has run ~20 years unfixed and is exploited in both directions. **CA never
  published a calibration target.** The community's two dominant complaints are mirror images —
  "auto-resolve is too punishing" and "auto-resolve doesn't credit my army's quality" — and both are
  the same underlying problem: **auto-resolve collapses a multi-dimensional tactical space into a
  scalar, so it is systematically wrong for exactly the battles that turn on the dimension it
  dropped.**
- **XCOM** sits between: the strategic slate surfaces specific missions, you play the ones that
  matter, the rest are abstracted.

**The dossier's blunt conclusion:** Dominions and Mount & Blade achieve perfect resolution-consistency
*by never offering a second path*; Total War is the only surveyed precedent with two paths, and the
only one with a documented, unsolved, two-decade consistency failure. So *"don't build a second
resolver at all"* **is the first option on the table, not a corner case.**

**The reframe the personnel program adds, which is the most useful thing in the game research:** your
**Auto** tier is an *easier* problem than TW's, because in Auto the player made no choices to
compress. Your **Witnessed** tier is the danger case — present, one light roll — because that is
structurally closest to the scalar collapse. Therefore **do not tolerance-test the mean; test the
failure mode.** The right question is *"does Auto ever produce a result a player who did play it out
would call unrecognisable?"* — a distribution-**shape** question, not a distribution-**centre** one.
And because Valoria's fidelities get used for scenes that may never recur — unlike TW's dozens of
battles per campaign, whose errors average out or get save-scummed away — err toward **legible,
coarse-grained and inspectable**: a short list of factors the player can see feeding the roll. *That
is the opposite of what TW shipped, and exactly the complaint TW players never stopped making.*

**And one structural warning Valoria currently violates.** No surveyed precedent defends a cross-scale
bridge whose default state is *"off equals doesn't exist"* — every surveyed game either has no such
seam or ships an explicit, imperfect one. `DISPATCH_COMBAT_BRIDGE` ships default OFF.

---

### 2.9 Generation and emergence

**The architecture is the field's consensus answer, arrived at four times independently.** Dwarf
Fortress worldgen, Caves of Qud's abstract-then-reify model and Ultima Ratio Regum's culture stack all
converged on a layered, conditioned generation stack — and the **rival** paradigm converged on it too:
WFC/Model Synthesis's documented homogenisation at map scale was rediscovered and fixed the same way
by two unrelated teams, both adding **a conditioning layer above the local solver.**

**Three failures that cluster, and they are the ones to fear:**

- **The Tale-Spin effect.** DF, the Nemesis system and Wildermyth hit it independently: the state space
  grows combinatorially while authored expression grows linearly. All three teams converged on the same
  answer — small tagged units recombined by matching.
- **The oatmeal problem, and WFC's local-only homogenisation.** Variety measured on axes humans do not
  perceive is not variety; local coherence implies nothing global. Compton's budget rule attaches:
  **not everyone can be a main character** — concentrate generative budget rather than spreading it.
- **CK2's apophenia.** A real and delightful effect that **its own developer flagged as not a
  mechanism**; Paradox was exploring "emergence detection" because waiting for coincidence is a
  limitation, not a strategy.

**The null that binds hardest.** Ryan, Mateas & Wardrip-Fruin name it *"perhaps the hardest challenge
we present in this paper"*: **physics has graphics**, so any reachable physical state is visible at
zero marginal authoring cost, and **no equivalent exists for mood, grudge, loyalty or ambition.**
Every surveyed mechanism that "solves" it *narrows scope* rather than generalising — DF's templated
flavour text over a facet band, Nemesis's small closed trait vocabulary, Wildermyth's hand-written
per-personality variants, explicitly not procedural by its developers' own account.

> The sentence the dossier asks be carried verbatim: **any plan that treats "we have the Key
> substrate" as equivalent to "we have emergent narrative" is skipping exactly the step every
> precedent struggled hardest with.** Tracking and expressing are different problems, and the field
> failed at the second.

**And the ceiling on any verification gate:** no general method certifies generated content is *good*,
only that it is *varied*. Fourteen years after Smith & Whitehead, the literature is still arguing
about **which metrics to plot**, and Compton's "interesting" and "characterful" are named as real
target properties with **no proposed measurement at all**.

---

### 2.10 Adjudication and social contest

**The one genuinely structured debate system in wide use is Burning Wheel's *Duel of Wits*.** Each side
declares a **Statement of Purpose**; each rolls a register-appropriate skill (Oratory, Rhetoric,
Persuasion, Interrogation) and adds successes to Will to get a **Body of Argument**. Play runs in
volleys of three rounds; each round both sides **secretly script** one manoeuvre from Point, Dismiss,
Avoid, Obfuscate, Rebuttal, Feint, Incite. Reduce the opponent to zero and you win — **but you must
offer a compromise scaled to how much of your own Body of Argument you lost.**

Four things it gets right: stakes declared *before* the mechanics run; **the compromise rule**;
simultaneous secret scripting, which makes it a prediction game rather than alternating checks; and
that it binds **public performance, not belief** — a losing debater has conceded the floor, not changed
his mind.

**Where it broke, and this is the survey's most valuable single finding.** Players converge on Point
and Dismiss because both drive the opponent's Body of Argument down fastest; Obfuscate appears
occasionally; **Rebuttal almost never gets used, because so many manoeuvres beat it.** The manoeuvre
set is not balanced, so a rich option space collapses to two verbs.

> **The constraint:** if debate manoeuvres are differentiated only by *damage output*, players will
> find the two highest-damage ones and stop. Manoeuvres must differ in **what they change about the
> state of the argument**, not in how much they subtract.

A second, independent failure of the same system: **at a 21-vs-11 Body of Argument it collapses to
"the bigger number wins fast"**, and Burning Wheel bolted on *Bloody Versus* afterwards
`[UNVERIFIED single actual-play account, commonly cited]`. *A manoeuvre layer earns its complexity
only while the sides are close.*

**The contradiction-finding family** — Ace Attorney and Danganronpa — has a precisely documented
structural limit: each round has **one correct statement-and-bullet combination**, and the space is
deliberately pruned to two-to-four statements and one-to-three bullets on normal difficulty. So:
*contradiction-matching is a puzzle with one solution, not a debate. It produces excellent
moment-to-moment tension and zero political modelling, because in a political trial the winner is
often the side whose evidence is worse.* The salvageable part is **inventory-as-argument**: claims are
objects you hold, spend and lose.

**Disco Elysium's transferable idea** is that skills are not modifiers but **interlocutors** — each has
a voice, an agenda and a personality, and they contradict each other inside the player's head, so an
internal conflict generates the external choice. Applied: give the player's *positions* voices. A
character publicly committed to something should have that commitment argue with him when expedience
beckons.

**Suzerain's** strength is that **advice is interested** — cabinet ministers advise in their own
interest — and its weakness is that resolution is largely branch selection, so the player chooses
between authored futures rather than operating a system. **Pentiment** is the model of *investigation
under an authority that will act regardless of truth*: the player's accusation has consequences the
game refuses to grade as correct `[UNVERIFIED as to specific mechanics]`.

**Triangle Strategy** supplies a link Valoria lacks entirely: it **gates which arguments you may
attempt on information gathered beforehand.**

**And the null.** *No game in this survey models the content of an argument.* Burning Wheel abstracts
it into Body of Argument; Ace Attorney reduces it to one correct pair; Victoria 3 replaces it with
faction arithmetic; Diplomacy leaves it entirely to the players' mouths.

---

### 2.11 Negotiation and diplomacy — the board-game family

Four rules, each from a different game, and each cheap:

- **Diplomacy (1954)** — a negotiation phase, then simultaneous execution, with **no mechanism
  whatever for enforcing an agreement.** Every promise is cheap talk, and everything interesting
  follows from that one omission. *This must be the default, with binding instruments as the expensive
  exception. A world where treaties bind automatically has no diplomacy in it.*
- **Pax Pamir 2e / Pax Renaissance** — **positional pricing.** A two-row market where the leftmost card
  is free and each further card costs one more, **paid by placing coins on the cards you skip** — so
  passing over a card subsidises the next player who takes it. The cleanest available model of
  political opportunity cost: *seizing the alliance you need funds your rival's second choice.*
- **Die Macher** — the **shadow-opinion track**: party positions and public opinion are separate
  tracks, and the *distance between them* is what scores.
- **Machiavelli** (the Diplomacy variant) — bribery as an **explicit legal action**, which converts
  negotiation from cheap talk into a market.

---

### 2.12 Mount & Blade — the closest whole-game analogue, and the thinnest treatment

Mount & Blade is the nearest thing in the survey to *Valoria entire*: a character with a personal
combat layer, a party, settlements to govern, faction politics, kingdom creation, and mass battles the
character personally fights in. Every other surveyed title covers one or two of Valoria's layers. This
one covers most of them.

**And the corpus treats it in three roles that do not agree with each other.**

1. **As a declared precedent.** `player_agency_v30 §1` names Mount & Blade / Manor Lords among
   Valoria's models, alongside RoTK Officer Mode, CK3 Vassal Play, Disco Elysium, Pathologic 2 and
   Pentiment. The faction-emergence arc — working up from nothing to founding your own faction — is
   explicitly the M&B / Manor Lords analogue, and a UI audit calls it *"the design's most rewarding
   long-form arc."*
2. **As the negative case that defines Valoria's whole cross-scale ambition.** `throughlines_meta_infill.md`
   uses it to specify what Valoria is *not*: *"this distinguishes Valoria from games where strategic
   and personal play are mechanically isolated (Pillars of Eternity's stronghold vs party-level play;
   **Mount & Blade's faction politics vs character combat**)."* The Ω-clause on cross-scale
   consequence exists because M&B has both layers and does not couple them.
3. **As a failure pole.** The P5 dossier uses it for the *fully fused* end of the leverage problem —
   one engine, consistent, and **the personal actor becomes irrelevant as N grows** (§2.7, D3).

**Reading the three together is the finding, and nobody in the corpus has.** M&B is simultaneously the
game Valoria most resembles in *scope*, the game it defines itself against in *coupling*, and one of
the two poles of the seam problem it has not solved. Roles 2 and 3 are the same defect seen from
different distances: a personal actor whose contribution does not scale is *why* the two layers read
as isolated. So the failure pole is not a separate finding from the isolation critique — it is its
mechanism.

**The consequence for Valoria is uncomfortable and worth stating.** Its cross-scale layer is the thing
that would distinguish it from its own nearest analogue, and that layer is currently one working
crossing — a faction arguing with itself — behind a default-off bridge. **The distinguishing feature
is the unbuilt one.**

⚠ **This section is assembled from three thin corpus mentions, not from a research pass.** No lane
surveyed Mount & Blade or Bannerlord as a subject; it appears only as a comparator. Given that it is
the closest whole-game analogue *and* a declared precedent, that is the most consequential coverage
gap in the survey — see §2.13.

### 2.13 The coverage gaps, named rather than filled

Each of these is a title the corpus either declares as a precedent or obviously should have surveyed,
and did not. **No finding is asserted for any of them.** What is given is the specific question a pass
would be commissioned to answer, so the gap is actionable rather than merely admitted.

| title | status in the corpus | the question a pass should answer |
|---|---|---|
| **Heroes of Might and Magic** | **Absent entirely.** Not surveyed, not declared, not cited | Recruitment itself is well covered — RoTK's Conscript spends gold and drops order, Total War gates the roster behind building chains (Shogun 2's ashigaru/samurai split is exactly that), CK's levies are a standing entitlement and its men-at-arms are bought. What none of those supplies is HoMM's narrower shape: **the rate of accrual is a property of a built structure in a specific place, and the stock piles up whether or not you visit it.** Total War buildings gate *what and how fast you may recruit*; a HoMM dwelling determines *how much has accumulated while you were elsewhere*, so the decision is when to convert a stock rather than whether to spend an action generating one. That is the shape that would give `facility_tier` — an authored progression axis that **nothing in Valoria ever raises** — a reason to exist, and it sits next to the levy half of X4 rather than replacing it. *Is per-settlement accrual the missing writer for `facility_tier`, and does it double-count against CK's entitlement model?* |
| **Mount & Blade / Bannerlord** | Declared precedent; used only as a comparator and a failure pole (§2.12) | *How do its settlement governance, party/companion roster and kingdom-creation arcs actually connect to its faction politics — and where, precisely, does the coupling stop?* The corpus asserts the layers are isolated; nothing establishes **where** |
| **Shadow Empire** | Named at the governance redesign as the model for principal-agent friction, alongside EU4 estates | *What does its governor/administrator friction model do that EU4's estates do not?* It is cited as a model and never surveyed |
| **Manor Lords** | Named with M&B at `player_agency_v30 §1` for the faction-emergence arc | *What does the build-and-grow arc look like when it is the whole game rather than a layer?* Adjacent to the HoMM question |
| **Pathologic 2** | Named at `player_agency_v30 §1` | *Its subject is scarcity and irreversibility under a clock — the one tonal register Valoria's Calamity setting implies and no surveyed title supplies* |
| **Tactics Ogre** | Surveyed; produced no surviving attributable finding | Either the pass found nothing transferable or the finding was lost. Worth one line of disposition rather than a silent roster entry |

**Why this table matters more than it looks.** Four of the six are **declared precedents in Valoria's
own design heads** — they are cited as models by documents that shape the design, and no research pass
has ever tested whether they support what they are cited for. That is the same shape as the
integration master's F3: agreement across surfaces that all descend from one un-audited source.

---
