> ## RELAY STAGE G · EMERGENCE PRECEDENT — `sonnet`, research only
> ## Status: **REFERENCE (2026-09-06). External material; nothing here is a design decision.**
>
> What actually stores story in CK2/3, Dwarf Fortress, RimWorld, the Nemesis system, Caves of Qud /
> Ultima Ratio Regum, King of Dragon Pass / Six Ages, and Pentiment — per system: what is stored, what
> makes a character act surprisingly, what makes an event memorable, what escalates, and what stops
> the output being a log.
>
> **Run at `sonnet` deliberately.** This is pattern recognition over public material, not judgment;
> `CLAUDE.md` §10 says promote a tier only on evidence a cheaper one failed the node, and none had.
>
> ⭐ **The section that earns its place is THE MEMORY QUESTION at the end.** Its finding — *the single
> mechanism that reliably prevents a retained memory from sitting inert is coupling the read to a
> specific decision-evaluation point, never a generic ambient scan* — is what reframes `P-42`, and its
> counter-example is exactly this design's shape: RimWorld surfaces memory only into mood, and is the
> one system where players report memories that should matter quietly expiring.
>
> The pass flags its own lower-confidence material (the two tabletop entries were not freshly
> verified) rather than asserting it.

---

# Emergent Narrative: Mechanisms Reference

Method note: I ran targeted searches to verify the specifics below rather than working purely from memory (CK2/3, RimWorld, Nemesis, Qud/URR, Six Ages, Pentiment). Burning Wheel and Ars Magica are from tabletop-design knowledge without fresh verification — flagged where confidence is lower. Where a source didn't give me a hard number, I say so rather than inventing one.

---

## Per-system breakdown

### Crusader Kings II/III

| | Mechanism |
|---|---|
| **Stored** | Per character: traits (personality traits like Wrathful/Ambitious act as literal AI weight multipliers), a per-*pair* opinion **stack** — not a single number but a list of named modifiers, each with source, magnitude, and its own decay/expiry; discrete relation flags (rival, lover, nemesis) separate from the decaying opinion number; hooks (weak = single-use, ~+200 modifier once; strong = persists while both live, reusable after a cooldown); secrets (typed, with a known-by list); stress and a breaking point. |
| **Acts** | No authored per-character logic — an AI **utility scorer**. Every candidate action (murder, marriage, scheme) gets a score built from trait weights × current opinion × stress × hooks/secrets held × succession incentives. "Why did my son murder my wife": Wrathful/Callous trait weights the murder-scheme category up; an opinion stack full of negative modifiers (disinherited, insulted, rival-of-mother) lowers the threshold; a scheme's power (Intrigue skill + accomplices) ticks monthly against her resistance until it resolves probabilistically. |
| **Memorable** | An event is retained when it (a) writes a permanent character-history/timeline entry, (b) upgrades a decaying opinion modifier into a durable relation flag (rival→nemesis), or (c) creates a Secret whose *discovery* is itself a future event. Small opinion swings that never cross into a flag just decay and vanish. |
| **Escalation** | Independent opinion penalties compound past a scheme-availability threshold; a resolved scheme (a murder) mints new hooks/secrets held by co-conspirators, lowering the threshold for the *next* scheme against someone else. At the realm scale, many vassals independently cross a low-opinion threshold from the same cause (tyranny, kinslaying) and join one faction near-simultaneously — reads as an authored uprising, is really correlated independent thresholds. |
| **Anti-log** | Event pop-ups quote the *specific* modifiers present rather than generic text; the UI surfaces only the causally relevant subset of the opinion stack for the decision at hand, not the full list. |

### Dwarf Fortress

| | Mechanism |
|---|---|
| **Stored** | A "historical figure" (a small, promoted subset of all units) carries: typed relationships (friend/grudge/rival/family, each with a strength value); ~50 personality **facets** (0–100, govern *how* they act) plus separate **values** (what they believe is good — loyalty, mercy, tradition); a memory log of witnessed/participated events; ~14 **needs** (pray, socialize, be outdoors…) each with its own decay/fulfillment rate; a stress number. Artifacts separately carry an ownership/battle history. |
| **Acts** | Facets/values are read directly by the simulation: a grudge relation is a standing eligibility flag that unlocks hostile actions (sabotage, refusal to work together) when opportunity arises; a value violated by a witnessed event (a merciful dwarf watching an execution) generates a thought that raises stress; stress crossing a threshold triggers a mental break whose *type* is picked partly by personality. No scripted plot — behavior falls out of facet/value/need state matched against the current situation. |
| **Memorable** | A memory persists as a discrete **world-log event with links** (figure↔figure, figure↔site, figure↔artifact) once it clears a significance bar — it isn't "remembered" so much as durably indexed, queryable later in Legends Mode. |
| **Escalation** | A grudge is a standing flag that accumulates with repeat causes; a killing is itself a new event witnessed by the victim's kin, who form independent second-order grudges — one death seeds several feuds. At the civ scale, worldgen wars/migrations are driven by accumulated site/faction relationship scores crossing thresholds. |
| **Anti-log** | Legends Mode renders the linked event graph as connective prose ("X became enraged after the death of Y... X murdered Z") rather than a timestamp list — the *links between records* are what make it readable as causal chain, not just chronological. This partially fails at scale (see failure modes). |

### RimWorld

| | Mechanism |
|---|---|
| **Stored** | Per pawn: up to 3 traits (weighted, partly-exclusive pool); a backstory pair granting skill passions and an implied history; a live-computed opinion score per pawn-pair from trait compatibility + history flags (blood relative, ex-lover, failed romance); mood = **sum of active "thought" objects**, each an independent memory moodlet with its own magnitude and decay timer. |
| **Acts** | The storyteller (Cassandra/Randy/Phoebe) is an external director scheduling incident type/severity from wealth, population, days-since-last-incident against a target curve — verified cadence: Cassandra ~4.6 on-days with a 1.9-day raid cooldown; Phoebe 8 off/8 on with max one raid; Randy near-uniform, firing roughly every 1.35 days. Per-pawn "surprise" comes from mood crossing a trait-scaled threshold — defaults **5% extreme / 20% major / 35% minor**, individually adjustable by traits (Steadfast raises it, Nervous lowers it), clamped to a 1–50% band for the minor threshold — which fires a mental break whose *flavor* (binge, wander, murderous, catatonic) is trait/skill-weighted, not authored per pawn. |
| **Memorable** | Exactly as long as its decay timer lasts, with explicit exceptions promoted out of the decay queue permanently: a failed romance becomes a permanent "ex-lover" tag; scars and lost limbs are permanent and read out in the pawn's bio forever. |
| **Escalation** | Thoughts stack additively — several small negatives near-simultaneously (a death + bad meal + sleeping rough) jointly cross a threshold none would alone. A mental break itself often spawns new negative thoughts in bystanders ("witnessed mental break"), chaining outward. Colony-scale: the storyteller scales raid difficulty with wealth, so solving one crisis by growing wealth *is* the escalation mechanism. |
| **Anti-log** | Mood tooltips always show the causal list (named thoughts summing to current mood); Randy Random is, by design, the closer-to-log control condition — the game deliberately ships Cassandra/Phoebe's curve-shaping as the "story" default rather than pure Poisson. (This last framing — Randy-as-control — is my own reading of the design intent, not a quoted developer statement.) |

### Caves of Qud / Ultima Ratio Regum

Both explicitly reject full historical simulation in favor of **"generate the events, then rationalize them"** (Jason Grinblat's own framing at GDC 2018) — the opposite of Dwarf Fortress's forward-simulated history, and the single biggest mechanical distinction in this whole set.

| | Mechanism |
|---|---|
| **Stored** | Qud: per sultan, a fixed biography of 8+ core events drawn from a pool of ~17 types (assassinate the old sultan, be betrayed, etc.), typically 10–22 events total (11–14 common); a "favored factions" set derived from which factions had positive relations *during* those events; downstream sultan-cult membership drawn from those favored factions. Players navigate 67 persistent factions with numeric reputation. URR: per culture (20+ per world), a generated religion (via a branching/fractal grammar splitting into sects), philosophy, art style, and social norms, plus a faction layer added in v0.11. |
| **Acts** | There is no in-fiction agent deciding at play time. A **state machine constrains which event types can legally follow which**, a sequence is chosen at worldgen, and a replacement grammar then generates prose that *rationalizes* the chosen sequence as if it were causal. Agency is authorial-at-generation-time, not simulated-at-play-time — structurally unlike every other system here except KoDP/Pentiment. |
| **Memorable** | Guaranteed by construction: the whole biography is short and complete, so nothing is generated and then forgotten. It's "memorable" only insofar as it left a discoverable trace (a cult, a place name, item lore) for the player to decode — memorability is a content-authoring guarantee, not an emergent filter. |
| **Escalation** | Bounded by the fixed biography length; the real "escalation" surface is downstream reference density (how many cults/places/items cite a given sultan), which is interpretive rather than simulated. |
| **Anti-log** | Solved by never running long enough to become a log — a short, complete, internally-consistent arc has no tail to degenerate into. Tradeoff: one-shot fixed content rather than an open-ended simulation. |

### Shadow of Mordor / Shadow of War — Nemesis system

| | Mechanism |
|---|---|
| **Stored** | Per orc: generated identity (appearance, voice, combat style); a Power Level that gates a Strengths/Weaknesses list (low power → more weaknesses, fewer strengths, and the reverse at high power); rank (grunt→captain→warchief) and hierarchy position (bodyguards, feuds with peer orcs); and the actual payload — a **per-relationship record of specific encounters** with the player (who killed/humiliated/spared whom), with visible scars applied from those specific events. Per the patent language: "predefined events between the player and first NPC result in changing parameters of the second NPC" — typed records, not a scalar reputation. |
| **Acts** | A state machine keyed to encounter *outcome*: player kills orc → gone (unless it "cheats death"); orc kills/routs player → orc levels up, gains a strength, sheds a weakness, sometimes gets promoted, and a personality-flavored taunt is generated referencing the specific encounter (weapon used, whether you fled). This is closer to scripted state transition than the continuous utility-scoring of CK/DF/RimWorld — worth being explicit that it's mechanically shallower, and it earns its narrative punch mostly from #3 and #5. |
| **Memorable** | Not emergent-filtered — deliberately guaranteed. The moment an orc beats the player it is flagged Nemesis and preferentially re-queued to recur; the memory is written onto the orc's identity itself (name, scar, taunt) rather than a separate log. |
| **Escalation** | Strictly monotonic per orc — every player loss adds a level with no decay, capped only by rank ceiling. No release valve except the player eventually killing them. |
| **Anti-log** | Aggressive re-surfacing (a beaten orc is scheduled to reappear, not left to random encounter odds) plus identity-embedded memory — there is no separate log UI at all; the world model *is* the narrative surface. |

### King of Dragon Pass / Six Ages

| | Mechanism |
|---|---|
| **Stored** | Each of 7 named Ring/council seats holds a character with a personality profile and a specific cult devotion — verified: advice about a god only fires if a Ring member actually worships that god. Clan-level state (relations with neighbors, the clan's own chosen mythic history) persists across the game and, in Six Ages, across a trilogy. |
| **Acts** | Advisors don't reason independently — they **gate/flavor a fixed pool of pre-written lines**: which line surfaces depends on (a) which personality/cult combination currently sits in the Ring, (b) the event context, and (c) rare bonus interjections deliberately prioritized by the designers when 2–3 Ring members share a trait/cult, specifically because that's rare. This is authored-content selection gated by simulated state, not independent reasoning — mechanically the shallowest system in this set. |
| **Memorable** | Made memorable by naming and recurrence — the same named advisors persist across in-fiction years and their canned reactions accumulate into a felt personality; early mythic-history choices are checked for consistency against which rituals/magic work later. |
| **Escalation** | Slow drift in clan-vs-clan standing and magic favor crossing thresholds into raids/alliances, punctuated by big single-event ruptures (broken oath, botched ritual) rather than compounding chains. |
| **Anti-log** | Guaranteed by writing quality, not emergent structure — flag this explicitly: KoDP/Six Ages lean almost entirely on authored branching keyed to state, least on emergent mechanism. |

### Pentiment

| | Mechanism |
|---|---|
| **Stored** | Many small, specific flags per NPC set by individual dialogue choices (verified: a widow remembers a specific act of kindness), plus persuasion-check modifiers from prior choices and background traits — fine-grained flags, not an aggregate reputation score. |
| **Acts** | No NPC agency at all — a **later scene branches on a checked flag** (a witness lies for you or doesn't; someone abandons you at a climax or doesn't). Same structural shallowness as KoDP, but with much finer grain and much longer delay — payoffs land acts/years later in the game's own timeline. |
| **Memorable** | Guaranteed, not emergent — the game explicitly tells the player "this will be remembered" at the moment of choice. Trades emergent surprise for guaranteed long-delay payoff, the opposite tradeoff from RimWorld/CK. |
| **Escalation** | Mostly single-hop (this choice → this one later scene), not compounding; the escalation that exists is authored *stakes* scaling across acts (village dispute → murder → the town's religious future), not a mechanical chain. |
| **Anti-log** | No simulation running, so no log to degenerate into. The actual risk it manages is the opposite — choices feeling inconsequential because effects are invisible for hours — fought with the explicit "will be remembered" prompt. |

---

## Tabletop precedents (lower confidence, not freshly verified)

**Burning Wheel** — each PC has 3 Beliefs (concrete, actionable goal statements), 3 Instincts (always-on reflex triggers, "when X, do Y"), and traits. The GM is *obligated* to challenge Beliefs, and Artha (the advancement currency) is paid for actually testing a Belief, not for having written one — so the mechanism that "makes a character act surprisingly" is a human-authored utility function (the Belief) that the table is structurally required to pressure-test, and the story is literally the record of belief→test→revision. This is a hand-run analogue of CK's trait-weighted scorer, except the weighting is player-declared per session rather than computed.

**Ars Magica** — troupe play (players rotate who Storyguides and who runs secondary NPCs across a saga) plus abstracted "seasons" of offscreen time (lab totals, seasonal covenant-event tables) let characters accumulate decades of simulated-but-untold history — feuds between covenants, Tribunal politics, standing grudges between named magi — the tabletop analogue of CK dynastic memory. The mechanism that makes it CK-like is specifically the combination of *long unplayed time-skips resolved by lightweight systems* plus a shared setting all troupe-run NPCs must stay consistent within.

---

## The common mechanisms (ranked)

| Rank | Mechanism | Present in | Minimum data/decision structure |
|---|---|---|---|
| 1 | **Typed, persistent relationship records, not a scalar** | CK, DF, RimWorld, Nemesis, Qud, KoDP/Six Ages (6/8) | Keyed pair `(A,B) → {type: enum, magnitude, source_event_ref, expiry: none\|timer}`. The type field is what a bare "opinion number" lacks and what lets the record gate specific *actions* rather than just color a mood. |
| 2 | **Memory that gates ELIGIBILITY, not just flavor** | DF (grudge→sabotage eligible), CK (hook→blackmail/immunity), Nemesis (vendetta→re-queue priority), RimWorld only partially (thoughts only ever feed mood, never gate an action directly — a real gap, see below) | A stored record must appear as a precondition/weight in at least one *action-availability* check, not only in a display string. This is the single most load-bearing mechanism and the one purely-cosmetic reputation systems miss. |
| 3 | **Escalation via threshold-crossing with shared causes** | CK (opinion stack→scheme threshold), DF (values-violation→stress→mental break; grudge accumulation→feud), RimWorld (thought sum→mental break threshold) | Several independently-updated quantities that share an underlying cause cross their own discrete gates near-simultaneously — reads as an authored climax, is actually correlated independent thresholds. Nemesis has a degenerate one-variable version (monotonic counter, no threshold math needed). |
| 4 | **Identity-embedded memory over a separate log** | RimWorld (scars), Nemesis (scars + name + taunts), DF (artifact/figure history), CK (title/dynasty history) | Write the consequence onto the *entity's own state* (appearance, name, title) so every future encounter re-surfaces it automatically, at zero query cost — versus a ledger that has to be actively read. |
| 5 | **A decision procedure split: computed utility vs. authored-branch-selection** | Computed: CK, DF, RimWorld. Authored: KoDP/Six Ages, Pentiment, Qud/URR (generate-then-rationalize). Nemesis sits between (scripted state machine, not utility-scored, but the state *is* generated). | Not a single common mechanism so much as a real fork worth naming: systems that compute a score from stored state at decision time genuinely simulate; systems that select among pre-written branches by stored state get emergent-*feeling* output far more cheaply but cannot exceed their authored content. |

---

## Failure modes

- **Undifferentiated NPCs.** No per-entity individuating data (traits/facets/backstory) means there's no reason to remember one over another — the majority of DF units are never promoted to "historical figure" for exactly this reason (a deliberate cost-control cut, not an oversight).
- **Memory that never surfaces.** Data is stored but nothing *queries* it at a decision point — the generic AAA-game "reputation number" nobody's behavior actually reads. This is different from #2 above (memory not gating anything) in that here the data structure might even support gating, but no code path checks it.
- **Decorrelated event stream / no causal chain.** Each incident is drawn independently with no link to prior ones — Randy Random is the acknowledged closer-to-this option in RimWorld's own storyteller lineup; pure Poisson raid generators generally.
- **Escalation with no terminus or release valve.** Numbers only go up (unbounded opinion stacking, unbounded threat scaling) — becomes swingy/absurd rather than dramatic. The systems above avoid this via hard caps: DF clamps facets 0–100; RimWorld thoughts expire on a timer; CK weak hooks are single-use; Nemesis caps escalation at the rank ceiling.
- **Legibility collapse at scale.** The mechanism is real but produces more state than a human can parse — DF's own Legends Mode is the known example: past a certain world-age the linked-event graph that's supposed to read as prose starts reading as a database dump again. Real emergent mechanism, but the *anti-log* layer (curation/narration) didn't scale with it.
- **Cosmetic memory.** Stored, displayed, and never fed back into behavior — the most common failure in "believable NPC" tech demos specifically: a relationship diary UI wired to nothing.
- **Mistaking authored-branch systems for simulated ones.** Qud/URR/KoDP/Pentiment are bounded by design (fixed biography length, fixed Ring size, finite flag set); running them far past their intended scope exposes the seams (content pool exhaustion, branch repetition) in a way true simulations don't hit the same way.

---

## The memory question, treated separately

The systems split into two genuinely different designs, and conflating them is itself a common mistake:

**(A) Time-decay memory** — cheap, fully automatic, ambient.
**(B) Event/existence-keyed memory** — no time decay; evicted only by a state change (target dies, item used, hook spent).

| System | How much retained | What's evicted first / how | How it surfaces at the right moment |
|---|---|---|---|
| **CK2/3** | Opinion modifiers: unlimited underlying count, each with its own decay duration (some effectively permanent, e.g. reputation-linked traits); UI **displays only the first ~10** — a legibility cap layered on an uncapped calculation, not a data cap. Hooks: weak hooks evicted on *use* (not time); strong hooks persist while both characters live, cooldown-gated for reuse. | Weak hooks: single use. Temporary opinion modifiers: fixed decay timer. Nothing evicted by importance-ranking — only by time or by being spent. | Coupled to the *specific decision UI* — a scheme panel shows "you hold a hook on them" exactly where that hook is decision-relevant, not in a separate diary. |
| **Dwarf Fortress** | Facets/values: fixed set every historical figure always has (~50 facets); not capped by count, but only values *outside the 40–60 middle band* generate a visible "thoughts and preferences" report — most of the structure is silent, not deleted. The real cap is **inclusion, not decay**: most units are simply never promoted to historical-figure status at all, wholesale exclusion rather than a decay curve. | Nothing decays out of an included figure's record; what's excluded is excluded permanently at the population level. | Continuous, not episodic — facets/values are read every tick something relevant happens, functioning as a standing disposition rather than a recalled memory that "fires" at a moment. |
| **RimWorld** | Each thought/memory: hard, independent decay timer (days-scale), unrelated to anything else happening — this is the cleanest pure-eviction-by-time design in the set. Explicit permanent exceptions are *promoted out* of the decay queue: ex-lover tags, scars, lost limbs. | Oldest/lowest-magnitude thoughts simply expire on schedule; nothing is evicted by importance, only by elapsed time. | Fully automatic — the mood sum recomputes every tick, so there's no separate "surface this" trigger. Cost: a RimWorld memory can only ever affect *mood*, never gate a specific future decision the way a CK hook or DF grudge does. |
| **Nemesis system** | Effectively unlimited per-orc memory for as long as that specific orc is alive — no observed decay mechanic. | Eviction is by **death**, not time: kill the orc, its specific memory is (mostly) gone, though the patent's follower/vendetta-transfer mechanic can hand some of it to a subordinate. | The strongest active-surfacing design here: the system *schedules* a nemesis orc to reappear in the next relevant encounter rather than leaving recurrence to random chance. |
| **Qud / URR** | Finite by construction (a fixed 10–22-event biography; a fixed generated religion/culture) — nothing is forgotten because nothing beyond the fixed slate was ever generated. | No eviction mechanism needed — there's no ongoing accumulation to prune. | Entirely player-driven archaeology; the system never decides when to "bring it up," the player finds the clue. |
| **KoDP / Six Ages** | Bounded by the 7-seat Ring — a member's traits/cult only matter while they hold a seat. | Eviction = removal from the council (death, replacement) — a hard structural cap, not decay. | Authored and high-precision: a stored trait surfaces exactly when its matching event-type is checked, with zero recall outside those wired hooks. |
| **Pentiment** | Unbounded count across the whole (~25 in-fiction year) game — no eviction at all. | Nothing evicted; every flag persists, but each is single-purpose (read by exactly one later scene). | Guaranteed by the writers wiring each flag to a specific known future check — strongest possible precision, but zero surfacing anywhere the writers didn't pre-wire. |
| **Burning Wheel** | No engine at all — memory is a human GM's job. Instincts are the closest analogue to a guaranteed-surface mechanism: written as an explicit IF-trigger-THEN-behavior line, so they fire on a recognizable condition every time. | N/A (human judgment) | The Instinct format itself is the lesson: a trigger-condition written into the memory *is* the surfacing mechanism, at zero bookkeeping cost. |

**The lesson that generalizes:** the single mechanism that reliably prevents a retained memory from sitting inert is **coupling the read to a specific decision-evaluation point** (a scheme's availability check, an encounter-selection scheduler, a mental-break trigger, a scene gate) — never a generic ambient "tick" scan. Every system above that surfaces memory well (CK's hook-in-the-scheme-panel, Nemesis's active re-queue, KoDP/Pentiment's wired scene checks) does this explicitly; RimWorld's thought-sum is the one design here that surfaces memory only ambiently (into mood) and, not coincidentally, is also the one where players report memories that "clearly should matter" quietly expiring before they do.

---

**Sources used:** [RimWorld Wiki: Mental Break Threshold](https://rimworldwiki.com/wiki/Mental_Break_Threshold) · [RimWorld Wiki: AI Storytellers](https://rimworldwiki.com/wiki/AI_Storytellers) · [How the Nemesis System Creates Stories](https://medium.com/@niklaseckstein/how-the-nemesis-system-creates-stories-d26754b30d2e) · [Nemesis — Shadow of War Wiki](https://shadowofwar.fandom.com/wiki/Nemesis) · [US Patent 10,926,179B2](https://patents.google.com/patent/US10926179B2/en) · [The 10-Year Journey of Ultima Ratio Regum](https://www.gamedeveloper.com/design/the-10-year-journey-of-ultima-ratio-regum-the-culture-generating-roguelike) · [Ultima Ratio Regum (Wikipedia)](https://en.wikipedia.org/wiki/Ultima_Ratio_Regum_(video_game)) · [DF Wiki: Personality facet](https://dwarffortresswiki.org/index.php/DF2014:Personality_facet) · [DF Wiki: Historical figure](https://dwarffortresswiki.org/index.php/DF2014:Historical_figure) · [Caves of Qud Wiki: Sultan histories](https://wiki.cavesofqud.com/wiki/Sultan_histories) · [Caves of Qud Wiki: Factions](https://wiki.cavesofqud.com/wiki/Factions) · [GDC Vault: Procedurally Generating History in Caves of Qud](https://gdcvault.com/play/1024990/Procedurally-Generating-History-in-Caves) · [CK3 Intrigue Guide (Prima)](https://primagames.com/gaming/crusader-kings-3-intrigue-schemes-hooks-secrets) · [CK3 Modifiers Wiki](https://ck3.paradoxwikis.com/Modifiers) · [Six Ages Dev Blog: Advice](https://blog.sixages.com/index.php/2021/05/18/advice/) · [Pentiment interview — Digital Trends](https://www.digitaltrends.com/gaming/pentiment-interview-alec-frey-choice/) · [Pentiment Wiki: Dialogue system](https://pentiment.fandom.com/wiki/Dialogue_system)