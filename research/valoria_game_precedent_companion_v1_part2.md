# Game Precedent Companion — Part 2: Comparison, Complements, Synergies

## Status: PROPOSED (2026-08-28) · reference under §0.05, not canon
## Version: v1.0 · Lane: IN (cross-cutting)
## Reads: `valoria_game_precedent_companion_v1.md` (the corpus · the survey by system)

**Reading order:** [Part 1 · The Corpus and the Survey](valoria_game_precedent_companion_v1.md) → [Part 2 · Comparison, Complements, Synergies](valoria_game_precedent_companion_v1_part2.md)

Part 1 reported what each game does. This part compares across them: what several independent titles
arrived at separately, what the genre has *not* settled, which precedents solve opposite halves of one
problem, and which borrowings make each other cheaper.

---

## §3 CROSS-COMPARISON

### 3.1 The convergences — where independent titles arrived at the same shape

A convergence is worth more than a good idea from one game, because it survived several teams' worth
of playtesting under different constraints. Ranked by how many independent sources agree.

| # | Convergence | Sources | Status in Valoria |
|---|---|---|---|
| **X1** | **Who holds the office is separate from who controls the officeholder.** | Kremlin (influence over politicians, never ownership) · CK (negotiable vassal contracts) · Ming *piaoni* (the drafter frames what the signer ratifies) · Byzantine Office-vs-Dignity · Venetian rectors as patronage brokers | **Absent entirely.** No custodian/holder split, no drafting layer, no contract object |
| **X2** | **Legible inputs, fuzzy thresholds — and legibility is what separates a celebrated system from a resented one.** | 5/5 personnel lanes on the threshold half (TK Satisfaction · JA2's hidden tolerance clock · RoTK `LOY ≤ 70` · Triangle Strategy's hidden number · CK opinion under opaque dread); 4/5 on the legibility half, decisively **JA2**, whose social layer is loved and whose tactical math is resented *in the same game* — and whose v1.13 fix **exposed the models rather than changing them** | Undecided, and it is a **no-GM constraint**, not a taste call: *you owe the player the reasons, never the trigger point* |
| **X3** | **Every game punishes idleness.** | 4/5 lanes: JA2 docks merc morale *and* town loyalty after three days without offensive action · TK loses satisfaction for idle characters and names "give them something to do" as the top mitigation · CK's unlanded courtiers leave at 2%/month · RoTK officers want posts | **No state degrades from neglect.** An unassigned person is inert, not restless |
| **X4** | **Levy and professional are different economies, not different tiers.** | 4/4 muster lanes. CK: levies cost **zero** gold, rationed politically and temporally; men-at-arms cost gold + prestige + maintenance *while unraised*, tripling when fielded · Shogun 2 as a starting-stat delta · JA2 prices the bought channel strictly worse on economics, winning only on speed | One Muster, and it is **the professional model wearing a generic label** — its own grounding is Wallenstein, a contractor paid regardless |
| **X5** | **Garrison is an assignment, never a unit type.** | 4/4: JA2 · Brigandine · Unicorn Overlord · Total War | `Territory.garrison` is a boolean written once and read once |
| **X6** | **Fold the administrative layer into a role the player already wants to use.** | 4/5 lanes, and it is Total War's own twenty-year arc: classic agents → Rome II's three-type consolidation → Warhammer's Hero fusion → Three Kingdoms' general-does-assignments | The Slate doctrine already lands where that series eventually arrived |
| **X7** | **Layered conditioned generation, with a conditioning layer above any local solver.** | Arrived at **four times**: DF worldgen · Caves of Qud's abstract-then-reify · Ultima Ratio Regum's culture stack · and the *rival* WFC/Model-Synthesis paradigm, whose map-scale homogenisation was rediscovered and fixed the same way by two unrelated teams | VSG's vertical stack is this shape; 1 of 15 weight tables authored |
| **X8** | **Small tagged units recombined by matching is the only answer anyone found to expression.** | DF, Nemesis and Wildermyth hit the Tale-Spin effect independently and converged here | `ledger.py`'s five tag families are exactly this shape, with zero writers |

**The pattern across X1–X8 that the master document also found from the other direction:** in six of
eight, Valoria already owns the primitive and does not run it. The convergences are not asking for new
subsystems; they are asking for callers.

### 3.2 The divergences — where the genre has not settled, and Valoria is not behind

These are the entries to cite when someone says a design is unproven. They are unproven *for everyone*.

| # | Open problem | The evidence |
|---|---|---|
| **D1** | **The appointed-governor role.** | Total War added, removed and re-added it **three times for three different reasons across twenty years.** Verbatim: *"There is no convergent answer — this is a real, unsettled design tension, not a solved problem you are behind on."* |
| **D2** | **Legibility versus depth.** | *"No shipped game in this domain has found a formula-legible system that critics also called deep, nor a deep system that critics also called clear."* Seven titles, each drawing one of the two complaints: CK3 pays for shown percentages with additively confusing modifier stacks; Victoria 3 pays for a stated Legitimacy formula with "deep as a puddle"; EU4's estates have real depth of intent and are tuned below the threshold of mattering; Imperator had real interaction depth and a down-direction that read as a bug. **Valoria's ambition — legible odds on a strategic layer with stochastic resolution — is that genre's own open problem** |
| **D3** | **Personal-scale leverage across three orders of magnitude of mass.** | *"No precedent in this survey demonstrates a mechanism whose personal-scale contribution is provably leverage-in-band from N=1 to N=1000+."* Every mechanism is scale-blind (Dominions' commander anchor, TW's lord aura) or fully fused (Mount & Blade). Best read as **well-funded teams tried and did not solve it** |
| **D4** | **Auto-resolve calibration.** | CA **never published a target** in twenty years. The two dominant complaints are mirror images of one cause: auto-resolve collapses a multi-dimensional space into a scalar, so it is systematically wrong for exactly the battles that turn on the dropped dimension |
| **D5** | **The content of an argument.** | Nothing models it. BW abstracts to Body of Argument; Ace Attorney reduces to one correct pair; Victoria 3 substitutes faction arithmetic; Diplomacy leaves it to the players' mouths |
| **D6** | **Expressing interior state.** | Named *"perhaps the hardest challenge"* in the field's own literature. Physics has graphics; nothing equivalent exists for mood, grudge, loyalty or ambition. Every "solution" narrows scope instead of generalising |
| **D7** | **Certifying generated content is good.** | Only *varied* is measurable. Fourteen years on, the literature still argues about which metrics to plot, and "interesting" and "characterful" have **no proposed measurement at all** |

### 3.3 The failure shapes — five, and each has a mechanical detector

The dossier programme clusters ten shipped failures into five reusable shapes. What makes them
valuable is that each converts into a **test that is pure arithmetic and needs no campaign run** —
and each passes §0.1 pt 5's load-bearing predicate, because its subject is a game mechanic.

| shape | shipped instance | the detector |
|---|---|---|
| **A — the direction that cannot run** | **Imperator: Rome's** launch Loyalty: governors lost 20+ on appointment alone and bled regardless of play; Paradox scrapped the whole action-currency four months later. Its mirror: **EU4's estates**, whose thresholds were never reached | Run the **maximum** available per-season mitigation against the maximum accrual and assert the net is recoverable. Plus a reachability bar with a **control arm**: X% of campaigns cross the threshold by season N; a mechanic firing in 0% of the control's complement is deleted, not tuned |
| **B — the extreme the model never meets** | ***Duel of Wits*** collapsing to "the bigger number wins fast" at 21-vs-11 · **Blades'** P(fail) falling 50% → 1.6% from N=1 to N=6 with no floor · **Dominions/Mount & Blade** as the two poles of the leverage failure | A pre-roll **gap detector** (past a declared pool ratio, fast-path to a single opposed resolution) · a checked-in test computing **all band probabilities across the practical pool range**, failing below a declared floor · a **leverage-in-band sweep** across three orders of magnitude of N |
| **C — two answers to one question** | **Total War's autoresolve divergence** — two different algorithms, ~20 years unfixed, exploited in both directions | One resolver, two entry points; a **two-sample K-S test** on outcome distributions at the declared extremes, CI-gated. *A failing instance is a design bug, not a known issue* |
| **D — the substrate mistaken for the game** | The **Tale-Spin effect** (DF, Nemesis, Wildermyth, independently) · **CK2's apophenia**, flagged by its own developer as not-a-mechanism · the **oatmeal problem** and WFC's local-only homogenisation | Budget expression as a first-class line item **in the same milestone** as the substrate. Acceptance bar: *a specific reachable state has a specific enumerated expression path* — not that the state is tracked. And *a metric that is also a knob cannot be evidence* |
| **E — the bypassed causal chain** | **Shadow of War's War Chests** — buying the *output* of an earned relationship corroded the system **for non-payers too**; Monolith removed the market | No convenience path may produce a relational outcome the history does not justify. Concretely: a **provenance field bound to the causing event** on every durable tag, and a test that no reachable tag has empty provenance |

### 3.4 The nulls, collected

Stating these together is the single most useful service this document performs, because each is a
place where citing precedent would be *false comfort*:

1. Nothing models the content of an argument (D5).
2. Nothing solves personal-scale leverage across mass sizes (D3).
3. No general expression channel exists for interior state (D6).
4. No method certifies generated content is good, only varied (D7).
5. **No precedent defends a cross-scale bridge whose default state is indistinguishable from its
   absence.** Every surveyed game either has no such seam or ships an explicit, imperfect one.
6. **Nothing caps unit *quality* by a faction scalar.** 4/4 franchises cap *quantity* by rank or title
   and let effectiveness climb open-endedly. Valoria's Military-as-quality-ceiling is unprecedented —
   **defend it as a statement of faction military culture; do not go looking for a precedent that
   isn't there.** (Shogun 2's softer counter-model is worth knowing: ashigaru start worse but *can*
   earn honour, so their gap is a floor, not a ceiling.)
7. **Every franchise resolves non-payment as permanent desertion.** Both of Valoria's canonical
   Wealth-0 options are recoverable. Combined with "a destroyed unit loses all Experience
   permanently", permanent desertion would make an army brutally hard to rebuild. Keep recoverable —
   deliberately, and knowing it is the outlier.

---

## §4 COMPLEMENTS — precedents that solve opposite halves of one problem

A complement is two sources that are each incomplete and that compose. These are more useful than
either half and none of them is in the corpus as a pair; the pairing is this document's contribution.

**K1 — CK3's landless track × Dwarf Fortress's consequence-free demotion.**
CK3 says a demotion must be **its own game, not a debuff** — an action-set flag per band, not a
multiplier on existing actions. DF warns from the other side that **demotion with no residual reads
consequence-free once survived**; a comeback that resets to zero is a reset button. Both are answered
by one object: *the demoted state carries tags forward* — a Grudge against whoever demoted them,
Leverage they retained. **Valoria already implements the residual DF lacks**: `succeed_governor` calls
`ledger_sweep`, and durable tags survive the handover. It has zero callers and no tag writer exists.
Add **Shogun 2's visible band over a hidden precise value** and the pair becomes shippable: three
bands — *seated*, *displaced*, *dishonoured* — is enough, and the band is what keeps the down-direction
from reading as arbitrary.

**K2 — Burning Wheel's scaled compromise × The Republic of Rome's shared loss.**
BW makes the **cost of victory** real at the *scene* scale: the winner concedes in proportion to how
much of his own position was destroyed. RoR makes obstruction have a ceiling at the *assembly* scale:
the polity itself can fail and everyone loses. Neither alone answers "why would self-interested actors
ever agree" — BW leaves a determined obstructor unpunished across scenes, RoR leaves a scene-level
victory free. Together they close both ends. The survey rates BW's compromise *"the most valuable
single loan"* and RoR's shared loss *"not optional"*, and they were surveyed independently.

**K3 — Kremlin's influence-not-ownership × Ming's *piaoni* drafting right.**
Both are *power without a power stat*, from opposite directions — one social, one procedural. Kremlin
separates who holds the office from who controls the holder; *piaoni* separates who drafts the
decision from who signs it. Compose them and a clerk with no vote, no title and no patron is still
dangerous, which is the best available answer to *"why would a player care about a clerkship."*

**K4 — Victoria 3's enactment clock × EU4's estates warning.**
V3 supplies the structure: a measure is a process with duration, running probability, discrete
setbacks, a failure state with a cooldown, and **an opposition that grows precisely because you
attempted it.** EU4 supplies the guard: a mechanism engineered not to fire is indistinguishable from
one that doesn't exist. The pair says *build the clock, and ship it with a reachability bar and a
control arm.* ⚠ And carry the dossier's separate warning: **V3's parameters do not transfer.** The
100-day stage, the 2×/1.5× class multipliers and the legitimacy bands are tuned for a nation-state
grand strategy running 1836–1936. **The structure transfers; the tuning does not, and only the
structure was actually researched.**

**K5 — Triangle Strategy's pre-vote intelligence gate × Valoria's own `BandExtension`.**
TS gates **which arguments you may attempt** on information gathered beforehand — a link between
investigation and contest that Valoria's two systems do not have at all. But TS's hard *"wrong appeal
= flat fail"* is a special case in a continuous system, i.e. scripting drift. **The softer version is
already a built primitive**: `dice_engine.BandExtension` declares a named policy whose only power is
`may_overwhelm` — it **may veto an Overwhelming and can do nothing else**, and the ladder's
single-owner test enrols every extension. A mismatched appeal declares a BandExtension; your ceiling
drops. In-idiom, zero new machinery, and it directly rewards the legwork a political game should
reward.

**K6 — Old World's emitted ambitions × Kremlin's mortality clock.**
Old World answers *"what does this character want"* generatively — goals emitted by the intersection
of a ruler's attitudes with the desires of the most influential families — and puts outstanding
ambitions on a countdown when he dies. Kremlin makes mortality the pacing device outright. Together:
motives are generated rather than authored, and they **expire**, which produces constant legible
pressure at no authoring cost.

**K7 — Football Manager's fidelity ladder × Total War's divergence.**
FM shows the shape that works: every fixture is **specific**, resolved at three fidelities of the
**same engine**, calibrated so instant ≈ played. TW shows the shape that fails: a *different
algorithm* for the fast path, twenty years divergent, exploited both ways. The complement is the
design instruction — *one engine, several entry points, and the fast path must be the same engine run
headless.* Valoria's parliamentary bridge is currently TW-shaped: a generic per-season roll rather
than the resolution of a **specific motion drawn from the slate**.

**K8 — Jagged Alliance 3's compression × every lane's maximalism.**
Every one of the nine passes recommended its own game's full apparatus. **JA3 compressed JA2's
five-layer morale stack, ±25 pairwise matrix, event deltas and prejudice axes into "liked squadmate
present: +1 AP; disliked: −1 AP"** — without losing the feel. That ratio is the ambition ceiling for a
d10/TN-7 engine, and it is the antidote to the survey's own recommendations. Read every other entry in
this document through it.

**K9 — RoTK VIII's order-gated conscription × JA2's per-unit loyalty charge.**
Both price recruitment in consent rather than coin, and they are the two halves of one dial. JA2
charges **per unit purchased**, globally rather than to the receiving sector, and scales the charge
with quality (0.15/veteran against 0.1/regular). RoTK VIII sets **hard floors**: below 50 order,
conscription capacity and soldier income fall; below 25 (revolt), conscription is unavailable
entirely. The per-unit cost is the live mechanic that shapes every decision; the floor is the rare
event that gives it a hard edge. Scope the floor to revolt-adjacent only — *"a population in open
revolt will not hand you soldiers"* is a different claim from *"you govern badly here"* — or the two
double-count.

---

## §5 SYNERGIES — where one borrowing makes another cheaper

A synergy is different from a complement: not two halves of one problem, but one primitive that
several unrelated borrowings all land on. These determine build order.

### S1 — The tag ledger is the shared substrate for six separate borrowings

| borrowing | what it needs |
|---|---|
| CK's council-seat denial (−40 opinion for a figure passed over) | *"a named NPC who wanted a post and didn't get it accrues a **Grudge** tag"* — one line in an appointment flow |
| Medieval II's trait triggers, the franchise's best-loved character mechanic | a tag ledger with **legible triggers** (the lesson is legibility, not more tags) |
| CK3 × DF's demotion residual (K1) | **durable tags surviving succession** — already implemented |
| Shadow of War's guard (failure shape E) | a **provenance field** bound to the causing event on every tag |
| The Tale-Spin answer (X8) | **small tagged units recombined by matching** — the tag families *are* this |
| Venice's *relazione*, a cumulative inheritable document updated by successive holders | a tag stream attached to a **place**, not an officeholder |

**Six borrowings, one module, already built and inert.** This is the strongest synergy in the survey,
and it lands on exactly the module the integration master's F3 identifies from the opposite direction.

### S2 — Three findings collapse into one build order for population

CK3's ambient-spawn warning says **generate on demand, not on a clock**. Radiata Stories says 175 NPCs
are affordable **because each is a config row**, and to port the principle onto the axes that carry
your mechanics rather than onto clock-time. And the integration master's own F10 shows a loader is
golden-safe only behind a dedicated RNG substream, because the season tick already runs a live
`world.rng` consumer over the population store.

Three independent findings, one sequence: **give the NPE its own stream, then load the rows, and never
build the spawner.** Valoria's registry is already 46 config rows.

### S3 — The auto-resolve fix and the cross-scale fix are the same fix

This one is not in the corpus and follows from putting two of its findings together.

The auto/manual doctrine's own recorded debt is that the shipped parliamentary vote is *"a generic
per-season roll, not the resolution of a specific motion drawn from the slate"* — which is precisely
the **Total War shape** (a fast path that is a different thing from the played path) rather than the
**Football Manager shape** (the same engine resolving *this specific fixture* at a chosen fidelity).

The integration master's cheapest parliament fix is *give the motion a subject*. **That is the same
edit.** Giving the vote a specific slate event to resolve is what converts the auto-resolver from
TW-shaped to FM-shaped, and it is also what makes the parity harness a well-posed test — a derivation
has a target to hit only once both fidelities resolve the *same* event. One function, two systems.

### S4 — Three muster borrowings are blocked on one missing object

Class-gating troop types (X-ref TK), garrison-as-assignment (X5), and the levy/professional split (X4)
all require a **unit record**, and Valoria has none: `Faction` has no unit list, and `Territory` has
only a `garrison` boolean. Muster currently writes `faction.Mil` directly. So the unit-object schema is
the real cost of all three and should be priced once, as a schema, rather than three times as
mechanics.

Note the failure mode TK's class-gating fixes, because it is the reason to prefer it: **gate on a
class and losing a person means promoting another; gate on biography — "the officer with Cavalry
History" — and losing one person costs you cavalry permanently.**

### S5 — The failure-shape detectors are one test suite, not five projects

§3.3's five detectors are all arithmetic, none needs a campaign run, and together they cover the
mechanisms the integration master's proposals actually propose to build:

- **A** guards any demotion, suspicion or pressure writer before it lands.
- **B** guards the degree ladder's band widths and any personal→mass leverage carrier.
- **C** guards the mass-battle survivor-ratio map, which currently carries a **second, self-disclosed
  degree semantics** for one event class.
- **D** guards any "emergent narrative" claim made on the Key substrate.
- **E** guards the ledger's first production writer.

Five guards, one milestone, and each satisfies the load-bearing predicate because its subject is a
mechanic the player experiences rather than repository apparatus.

### S6 — X2 makes the no-GM problem tractable, and nothing else in the corpus does

Valoria has no GM. Nobody narrates why a governor defected, why a motion carried, or why a faction
turned. The JA2 finding — that **legibility is what separated the loved half of one game from the
resented half of the same game**, and that the community fix **exposed the models rather than
changing them** — is the only surveyed evidence that speaks directly to that constraint. Composed with
Shogun 2's visible-band presentation (K1) and the 5/5 fuzzy-threshold convergence, it yields a single
rule that costs no mechanics at all:

> **Publish every input. Publish a band, not a number. Never publish the trigger point.**

That rule is free, it applies to every system in the integration master, and it is the closest thing
the survey offers to an answer for D2 — the legibility-versus-depth problem that no shipped title in
the genre has solved.

---

## §6 THE STEAL / REFUSE TABLE

Ranked by value per unit of cost. Every entry carries its failure mode, because **a borrowed
mechanism whose failure mode is not stated has not been researched, only cited.**

### Steal — cheap, and each lands on a primitive that already exists

| # | Steal | From | Attached failure |
|---|---|---|---|
| 1 | **A Grudge tag written at the moment a figure is passed over or demoted** | CK's council-seat denial; CK3 × DF (K1) | Shadow of War: the tag needs **provenance bound to the causing event**, or a later convenience path can forge the relationship |
| 2 | **Publish inputs, publish a band, never publish the trigger** | JA2 v1.13 · Shogun 2 · the 5/5 convergence | JA2 itself: the *same game* was resented where its math was opaque |
| 3 | **Recorded defeat** — a motion carried and vetoed persists with no force and full citability | Roman *senatus auctoritas*; *"very few games have this and it is nearly free"* | None found. It survived the survey's own adversarial attack |
| 4 | **Scaled compromise** — the winner concedes in proportion to what winning cost | Burning Wheel, in print and in play since 2002 | The documented complaints about that system concern **manoeuvre balance, never the compromise rule** |
| 5 | **Give the vote a specific slate event to resolve** | Football Manager (K7, S3) | Total War: a fast path that is a *different algorithm* diverges and gets exploited both ways |
| 6 | **Investigation output caps a contest's ceiling** via the existing `BandExtension` | Triangle Strategy, softened (K5) | TS's own hard gate is scripting drift — take the veto-an-Overwhelming form, not the flat-fail form |
| 7 | **Idleness costs something** | 4/5 lanes (X3) | None; the convergence is unusually clean |

### Steal — structural, and worth the cost

| # | Steal | From | Attached failure |
|---|---|---|---|
| 8 | **The enactment clock** — a measure is a process that mobilises its own opposition | Victoria 3 (K4) | EU4: tune it to fire on a normal timeline **or cut it**. And the parameters do not transfer |
| 9 | **Levy and professional as different economies** | 4/4 (X4) | Splitting a ratified action is a canon change; Valoria's own Templar exception is the precedent that it can be done once |
| 10 | **Garrison as an assignment on existing units** | 4/4 (X5) | Blocked on the unit-object schema (S4). Open fork: JA2's garrisons can move offensively |
| 11 | **Shared loss — the polity itself can fail** | The Republic of Rome (K2) | In single-player it disciplines **AI factions**, which is an AI problem, not a rules problem — a harder cost than the survey acknowledged |
| 12 | **Drafting right** — the clerk who drafts outranks the minister who signs | Ming *piaoni* (K3) | None found; models bureaucratic power with no power stat |

### Refuse

| # | Refuse | Why |
|---|---|---|
| 13 | **CK3's ambient population model** | 6–7 parentless sixteen-year-olds monthly, 24,000-character late saves, two community mods pulling in **opposite** directions, and Paradox's own fix throttling the low-value tail. **Generate on demand, not on a clock** |
| 14 | **A second resolver of any kind** | Dominions and Mount & Blade achieve consistency by never offering one; Total War is the only precedent with two paths and the only one with a twenty-year unsolved divergence. *"Don't build a second resolver at all" is the first option on the table, not a corner case* |
| 15 | **Contradiction-matching as a primary political resolution** | One correct pair per round; excellent tension, **zero political modelling** — and in a political trial the winner is often the side whose evidence is worse. Keep only *inventory-as-argument* |
| 16 | **Manoeuvre sets differentiated by damage output** | *Duel of Wits*: players found the two highest-damage verbs and stopped, and Rebuttal went unused because too much beat it |
| 17 | **Personal relationship modifiers large enough to dissolve structural conflict** | The CK3 critique: opinion bonuses paper over structural factors, so *"you can generally succeed at things kings wanted to do but were unable to pull off."* **Some conflicts must be positional and unbuyable** |
| 18 | **Three Kingdoms' "Administrator" as a vocabulary import** | Solves the wrong half. *Governor* is already canonical, in code, and carries residence semantics TK's Administrator lacks. The overloaded word is **officer** |
| 19 | **Treating "we have the Key substrate" as "we have emergent narrative"** | The one sentence the dossier asks be carried verbatim. Tracking and expressing are different problems and **the field failed at the second** |

---

## §7 WHAT THIS DOES NOT COVER

- **`systems/fieldwork/` and `systems/social_contest/`** were on no harvest lane's manifest for the
  integration master, and the precedent material for social contest here comes from the political
  survey rather than from a reading of those subsystems. Investigation-side precedent (Pentiment,
  Ace Attorney, Triangle Strategy) is reported at the survey's own confidence.
- **No precedent claim here was re-verified against its source.** The dossiers' `[UNVERIFIED]` and
  community-derived marks are preserved rather than laundered, and §1.2's bot-wall caveat applies to
  every number.
- **The historical corpus is not surveyed here.** Byzantium, Song–Ming China, feudal Japan, the HRE,
  Venice, Renaissance Italy and Habsburg Spain are cited only where a game and an institution converge
  on the same shape. `audit/2026-07-09-comparative-governance-research/` and
  `research/fa_se_historical_precedent_research_v1.md` are the documents for that, and the second
  carries 58 proposals judged 44-keep / 14-cut.
- **Six titles are surveyed thinly or not at all, and Part 1 §2.13 registers them** with the specific
  question each would answer rather than filling the gap with assertion. The sharpest is **Mount &
  Blade** (Part 1 §2.12): the closest whole-game analogue to Valoria's entire scope, a declared
  precedent at `player_agency_v30 §1`, and surveyed only as a comparator and a failure pole. **Heroes
  of Might and Magic** is absent entirely, and holds the one recruitment shape the four surveyed
  models do not — accrual as a property of a built structure in a place.
- **Four of those six are declared precedents in Valoria's own design heads**, cited as models by
  documents that shape the design, with no pass ever testing whether they support what they are cited
  for. That is the same shape as the integration master's F3.
- **Nothing here is a recommendation to build.** The integration master's `_part4` §6 holds the
  proposals; this document supplies the failure modes that must travel with them.
