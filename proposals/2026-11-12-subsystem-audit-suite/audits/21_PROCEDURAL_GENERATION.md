# PROCEDURAL GENERATION — precedent study, design of the generation kit, and implementation plan

## Status: REFERENCE (a design audit and plan; resolves nothing at runtime, CLAUDE.md §0.05)
## Read at: d5d9ede (working tree)

Requested by Jordan, 2026-11-12: *"investigate how procedural generation is to be used to fill in content and
context and aid in constructing emergent narrative and world churn (look at our precedent games for
inspiration, especially the detective procedural generation one) and how to make it work with our game,
complete with detailed plan for implementation."* Lane: Fable design lane (authority as in `AUDIT_BRIEF.md`,
"Authority granted": proposals only; nothing here edits code, registries or canon). Proposals:
`proposals/21_PROCEDURAL_*.md` (index in §8).

## 0. Verdict

**Valoria today generates nothing: the world it builds is one hand-assembled world, identical at every
seed, and the single largest obstacle to procedural generation is not a missing generator but a missing
*past*.** `harness/populated.py::build_realm(seed)` reads canon geography, an authored venue table, an
authored cast of 46 case persons plus 37 cohorts, and stamps them; a probe at seeds 0, 1 and 2 finds the
rungs, persons, names, homes, pursuits, sites, site conditions, stores and offices equal, with two tenure
ids (a hash of the seed) the only difference (§12, probe P1). Every settlement has the same three sites
(harbour, seam, garrison) and a cohort of weight 2; no person holds an attribute in the shipped arm; no
person has a parent, a deed, a birth season or a history; no Event precedes tick 0. The seed therefore
moves only what happens *after* the build, and the story a seed can tell is bounded by a starting state
with no differences in it for anyone to want, envy, remember or investigate.

The precedents converge on one finding that transfers, and it is the one the "detective" precedent is
built on: **generated content becomes story when it is the residue of a simulated history, not the output
of a content roller.** Shadows of Doubt generates a city, then people with jobs, homes and acquaintances,
then *runs the simulation forward before the player arrives* so that a killer with a relationship to the
victim commits the murder inside the same simulation the detective later reads; the evidence is whatever
that simulated act left behind, which is why the developer saves every object in the world (he cannot
know in advance which will be evidence). Dwarf Fortress does the same at the scale of centuries; Caves of
Qud shows the cheaper inverse (draw events, rationalise afterwards) and where it is enough (in-world
texts) and not enough (anything that must be investigated). RimWorld and Left 4 Dead show that churn is a
*pacing* problem solved by a state-reading event selector, not a content problem. The storylet
literature (Short; Failbetter) supplies the unit: content + prerequisites + effects, drawn by salience.

Valoria is unusually well placed to use this, because the hard half already exists and is owned once: an
Event log with causes, per-holder Claim ledgers with provenance and decay, a WITNESS channel, one chooser
serving NPC and player-proxy, one seeded draw owner, one graded ladder, a season loop that runs with no
player. **The kit designed here therefore adds one mechanism and a set of typed tables, not a second
engine: (1) a *worldgen* package that draws a realm's variable layer from designer-editable tables under
constraints and rejects incoherent draws; (2) a *prologue* that runs the real season loop for N seasons
before play (optionally N generations at a coarse cadence), so that deeds, grudges, debts, kinships,
offices-by-deed and at least one concealed wrong exist as Events and Claims with true trails before
anyone investigates; (3) a *case seeder* that does not write a case but arms the conditions of one (a
motive, a means, an opportunity drawn from the persons' own state) and lets the persons' acts through the
ordinary verbs commit it or fail to; (4) state-dependent *storylet and storm pools* for churn; (5) a
grammar for names and texts.** Hand-authoring keeps canon, the named NPCs, the factions, the three founding
houses and the set-piece arcs; generation fills the rest and gives the authored arcs a context to land in.

What must be said plainly: the detective loop cannot be delivered by generation alone. The tree's own FI
and LACUNA audits establish that the investigation verbs mostly write nothing, that one covert kind
exists, that no accusation executes and no conclusion is committed (`08_FI_audit.md`, `19_LACUNA_…`,
`D_T06.md` rows 8, 12, 16, 18). A generated case with a true trail is necessary and not sufficient; the
plan in §8 sequences the generator batches *behind* those lanes' proposals and names each dependency
edge. No shipped game solves the generated *whodunit with a deceiving witness and a fallible verdict
resolved by draws*; Shadows of Doubt grades the name by exact match. That is a null, and Valoria's
position on it (the world answers later; nothing is graded against truth) is a design choice the kit
must support rather than a solved problem it can copy.

## 1. Precedents, sourced

**Sourcing tiers used in this section.** `[P url]` = page body read this session; `[S url]` = search-result
snippet only this session; `[T path]` = the tree's own research, with its own tier tag carried (`V2`/`V3` =
page read by that earlier pass); `[M]` = memory, not re-checked this session. External requests carried
game search terms only. Blocked this session: `colepowered.com` posts (empty body returned for DevBlogs
#2, #8, #10), `whynowgaming.com` (403), `indiedb.com` (403), `pcgamer.com` (headline only); DevBlogs #18
and #23 are video posts whose text carries no method. So the Shadows of Doubt *generation method* below is
mostly snippet-grade and tree-grade, with two page reads; shapes are the durable finding, figures are leads.

### 1.1 Shadows of Doubt (ColePowered) — "the detective procedural generation one"

| question | finding | tier |
|---|---|---|
| What is generated | A city per save from a seed: a nested location hierarchy City > District > Block > Building > Floor > Address > Room > Tile, with hand-built floor pieces arranged procedurally; then citizens (roughly 300–700 by city size) each with a job, a home, a daily schedule, 23 identifying profile fields (name, fingerprint, address, telephone, workplace, handwriting…), acquaintances; companies; documents, V-mails, call logs, receipts; then murders. | hierarchy `[S colepowered.com DevBlog #13]`; population and profile `[T R5 §2, T06, V2/V3 wiki via api.php]` |
| From what | Hand-authored building floor pieces, item and text presets, six killer archetypes each with a signature evidence pattern; a seed. | `[T R5 §2 V2 wiki Cases rev 2026-09-10]` |
| Order | Places first, then companies and homes, then citizens fitted to them, then a simulated stretch of history before play: "the game simulates 12 hours of history for all its inhabitants" on city load; in the first prototype the game "begin[s] simulating a day at its maximum simulation speed, which is about x60" until a murder happens. | `[S whynowgaming/Wireframe]`, `[S DevBlog #10, prototype; may not hold for 1.0]` |
| The case | Not a script. A killer is selected among citizens; in the prototype "the AI killer picks an acquaintance", follows the victim until they are alone, kills, and leaves the weapon and prints where the act put them. "The murder needs to happen, basically, before you get there, and all these clues need to be set up." The same case shape "can play out with different people in different parts of the city". After a resolved case, the game picks the next killer after some time; an unresolved killer keeps killing. | `[S DevBlog #10]`, `[S Wireframe quote]`, `[S Edge via Magzter]`, `[T T06 §2 V3 Wikipedia]` |
| Why the trail is true | Evidence is the world's own objects in the state the simulation left them. The developer saves "every item in the world, not only nearby or carried objects", because he "can't predict which objects will matter as case evidence". | `[P colepowered.itch.io DevBlog #30, 2022]` |
| How coherence is kept | Each citizen's routine is goal-based with needs (eat, drink, sleep), replacing an earlier "almost completely pre-computed" routine that broke when interrupted; high update rate only for citizens near the player ("about 95%" run cheap). Leads chain by shared keys (name → address → workplace → phone). | `[P colepowered.itch.io DevBlog #15, 2019-04-24]`; chain `[T T06 §2 step 5]` |
| How a generated thing becomes a story | The player assembles it: evidence pinned to a board, strings drawn automatically to sources, a Resolution Form on which only the killer's name is pass/fail (+1000 / −100) and four optional fields pay if right. Witnesses' memories fade and a witness whose presence looks bad may lie (2018 design, not re-verified for 1.0). | `[T R5 §2 V2 wiki Resolution Form rev 2025-02-27; devblog 8 2018]` |
| Authored against generated | One hand-crafted tutorial case ("The Dead of Night") cast onto a generated city; everything after is generated. A custom dialogue editor exposes "a wide number of procedural fields and variables" to writers. | `[T T06 §1]`, `[P colepowered.itch.io DevBlog #28, 2021-10-01]` |
| What it does NOT solve | (a) Motive: six archetypes, not persons' own reasons; critics note cases "lack broader narrative connection" `[S Wikipedia mirror]`. (b) No citizen-to-citizen rumour found (`T R5 §2 I3 PART`). (c) The verdict is an exact-match grade against truth, with no trial and no fallible judge. (d) Consequence is a fine and another body; the city does not change politically. (e) Seeds are not stable across versions `[T T06 §1]`. (f) Sameness: a small archetype set over a large city is Compton's oatmeal problem. |

**What transfers.** The order (place → institution → person → relationship → *simulate* → crime inside the
simulation → evidence as residue); the casting of a case shape onto whoever the state supplies; the
keyed-lead chain; the save-everything consequence (in Valoria: every Event and Claim is already kept).
**What does not.** Physical forensics at tile scale (Valoria's unit is the rung and the season scene, not
the tile and the minute); the exact-match oracle (ruled out by the knowledge-model axiom, `D_T06.md` row
12); archetype killers (scripting drift: a killer kind is a special-cased entity; Valoria's motive must be
a person's own goal, grievance or need).

### 1.2 The other generation precedents

Tree sources first; `[T …]` carries the tree's own tier. Hades and Spelunky are not in the tree (0 files by
grep) and are given from memory only, as marked.

| precedent | what is generated, from what | constraints and how coherence is kept | how a generated thing becomes a story | what it does NOT solve | tier |
|---|---|---|---|---|---|
| **Dwarf Fortress** | Terrain from separately generated fields (temperature, rainfall, elevation, drainage) whose interplay sets the biome; then history simulated forward; historical figures who "run plots, funding, assassination" and visit the fort | "Break the system down into basic elements and interactions"; "operate at the level of what the player sees or one layer below"; real-world analogs correct defects | Legends are the residue of the simulated history; the fort meets figures who already have a past | Adams' chapter is about terrain only and licenses no claim about story; raw simulation output "almost never has story structure" (Ryan via Short); scale (about 200 dwarves) defeats the player's memory (Sylvester) | `[T E17 P(full)]`, `[T R3a:64 V2]`, `[T E12bcd S]`, `[T G13 S]` |
| **Caves of Qud** | Five sultans' biographies: about thirteen state-parameterised random events each, text from a Tracery-like replacement grammar | Events are random; each event's text pulls a cause from current state, or writes one into state; a per-sultan *domain* symbol threads the texts | Coherence is the reader's (apophenia) over shared state; histories also instantiate sites and items | "A generation method for a subordinate system": histories are fixed before play and need not agree with the player's acts; coherence judged by the authors | `[T E15 P(full)]` |
| **Crusader Kings 3** | Characters with traits, kin, claims and secrets; events from weighted pools keyed to character state | Eligibility triggers plus weights; dynasty and claim structure supply continuity | Kin labels and claims make every death a succession question | Tree holds the realm and secrets tables (`R1`), not the generator; event text is authored per event (large content load) | `[T R1 V2]`, generator detail `[M]` |
| **RimWorld** | Incidents drawn from a categorised database by a storyteller reading "a few statistics" (wealth, colonists, recent harm); threat points with an adaptation factor that shrinks raids for a struggling colony | Small named cast (about 12), labels on health and relationships; incidents designed to last and overlap; "hurt without killing" | Apophenia over a legible, small, remembered cast; pacing as alternating threat and rest | A director is a non-person actor; "the Simulation Dream fails because players neither want nor can perceive that much simulation" is the developer's opinion, unmeasured | `[T G13, G14 S]`, `[T R3a:125-126 V2]` |
| **Left 4 Dead** | Enemy population and pacing by an AI Director estimating each player's intensity | Simple algorithms; build-up, peak, relax | Pacing, not content | Same: a director | `[T G10 P(full)]` |
| **Wildermyth** | Authored stories cast onto generated heroes: "targets are filled in listed order"; a mandatory role plus a score threshold "sends the game to another story when no hero fits"; a calamity card after every battle and at intervals; an event becomes 1/4 as likely in the next campaign each time it occurs | Role casting by query; repeat suppression | Authored beats land on people the player already knows | Stories are authored whole; variety is the deck's size | `[T R8:126,133,136 V2]` |
| **Fallen London / Sunless Sea** | Storylets: content + prerequisites (qualities) + effects; a hidden quality re-rolled 1–100 gates many storylets | Quality gates; salience | Player picks among unlocked content (QBN); "a small enough, recombinable unit that most classic narrative structures can be expressed in it" | "New bookkeeping and tuning burdens"; the fully branching time cave wastes the approach | `[T G07, G11 P(full)]`, `[T T08:110 V3]` |
| **Kenshi; Mount & Blade** | World states that change "whether or not you act"; parties, lords and wars churning on a fixed map | Faction-level state machines; a fixed map with moving holders | The player arrives in a world already in motion | World states are hand-keyed flags (Kenshi); lords are thin characters (M&B) | `[T R2:205 V2]`, `[T R2]`, detail `[M]` |
| **Prom Week / Versu / Façade** | Social moves selected from rule sets over character state; Façade: about 27 beats, about 15 per run, at most 25% of content per run, about three person-years | Authored social rules and beats; a drama manager sequences (Façade) | Character-specific responses to the same situation | Authoring cost per minute of play is very high; a drama manager is a non-person actor | `[T 00_README cross-check; 02_interactive_drama P]` |
| **Lacuna** (contrast: authored) | Nothing. Cases are authored with a hidden answer key | "Many channels out, few channels back in": one committed, unverified Case Sheet | The wrong answer cascades into later authored cases | One railroad per wrong answer, all authored | `[T 19_LACUNA audit, page read by that lane]` |
| **Blade Runner (1997)** | The culprit set is randomised per playthrough over an authored cast | Evidence must therefore be generative, not scripted | Replays differ in who is guilty | A closed authored suspect set | `[T FWP §2.3, self-graded HIGH]` |
| **Hades / Spelunky** | Rooms assembled from authored chunks under hard constraints (a guaranteed path; reward and encounter budgets); Hades hangs authored dialogue on run state by priority | Constraint-checked assembly: reject or repair a level with no path | Hades: authored lines selected by state make repetition read as progress | Spatial generation only; no social causality | `[M]` — not in the tree |

### 1.3 What the literature in the tree adds

- **The target is perceptual variety, not combinatorial variety** (Compton, `P01`): list the properties of a
  good and a bad artifact first, star the deal-breakers as constraints, then pick the method. A generator
  whose outputs are "mathematically distinct yet perceptually samey" has failed without breaking.
- **Judge a generator by its range** (Smith & Whitehead, `P02`): sample it, measure a few global metrics,
  plot the density, and read the holes and biases. It shows a distribution, not coverage.
- **Generate-and-test is the general form** (Togelius et al., `P03`): the two hard decisions are how
  content is represented and how its quality is evaluated.
- **Replayability is not the justification** (Smith 2014, `P04`): only one payoff of generation cannot be
  supplied by a large authored pool. For Valoria that payoff is *content that is consistent with a world
  state no author saw*: the supporting cast of a realm whose seats, debts and grudges came from play.
- **Sifting, not steering** (Felt, Winnow, Select the Unexpected; Ryan via Short): simulate, then pick
  storyful sequences by pattern, preferring the statistically rare match. A sifter is a reader, so it is
  lawful under AX-1 where a drama manager is not.
- **Dramatic situations as the mid-level authoring unit** (Lessard & Paré-Chouinard, `E04`) and **tension
  measured before any story is generated** (Kybartas et al., `E05`): a world can be scored for conflict
  potential at design time. This is the basis of the story-possibility check in §5.
- **Indexical storytelling** (Fernández-Vara, `G04`): a story built from traces physically connected to
  past events. This is the detective precedent stated as theory.
- **The apparatus was silent** on what share of autonomous acts the world refuses
  (`00_README.md`, first application). That is the quantity a prologue's yield depends on (§2.4).

### 1.4 Convergences and nulls

**Convergent findings (three or more independent sources each):**

1. *Simulate first, then read.* Shadows of Doubt (the murder happens inside the simulation before the
   player arrives), Dwarf Fortress (legends), Kenshi and Mount & Blade (a world already in motion),
   Fernández-Vara (traces), Ryan (curation). The generated thing that becomes a story is a *residue*.
2. *Cast shapes onto whoever the state supplies.* Shadows of Doubt (the same case with different people),
   Wildermyth (roles filled by query, the story skipped when no one fits), Blade Runner (randomised
   culprit), storylets (prerequisites). An authored shape binds by query, never by name.
3. *A small, named, remembered cast beats a large one.* RimWorld (12 against 200), Wildermyth, CK3's kin
   labels. Depth of simulation the player cannot perceive is waste (Sylvester; Adams' "one layer below").
4. *Constraints plus rejection keep a generated world coherent.* Compton, Togelius, Hades/Spelunky `[M]`,
   the tree's own FW Q6 ruling (a solvability precondition at generation, never maintained against the sim).
5. *Pacing is selection over state.* RimWorld, Left 4 Dead, Wildermyth's suppression, Sunless Sea's gate.

**Nulls (no shipped game or read source solves it):**

- **N1. A generated crime with a person's own motive.** Shadows of Doubt uses six archetypes; Blade Runner
  an authored suspect set; Pentiment deliberately has no culprit. No precedent derives motive from a
  simulated person's goals and grievances and then has the act committed by that person's own choice.
- **N2. A generated mystery whose verdict is fallible and drawn.** Every precedent with a culprit grades
  the answer against truth or does not answer at all. None resolves accusation and judgment by draws
  whose odds are set by held evidence, with a wrong conviction as a lasting world fact.
- **N3. Witnesses who lie for their own reasons in a generated case.** Shadows of Doubt's 2018 design
  names it; the tree could not verify it shipped (`R5` open items).
- **N4. Pacing without a director.** Every pacing precedent uses a non-person selector. Valoria's AX-1
  refuses one. No source shows churn sustained by persons' acts alone over a long game; the WR audit
  measures the opposite today (beginnings plentiful, escalation and endings refused).
- **N5. Seed stability across versions.** Shadows of Doubt's seeds broke at a version change. No source
  describes a remedy; the kit's keyed draws (§4.0) are a design answer, untested.
- **N6. Measured story quality of a generator.** Qud's coherence is author-judged; RimWorld's claims are
  unmeasured; the apparatus's `rater` and `player` rows have never been applied to a run.

## 2. Valoria as it stands: generated, authored, missing

### 2.1 What the build does (`engine/season/harness/populated.py::build_realm`, `:1014-1993`)

| layer | source | read by the build | drawn? |
|---|---|---|---|
| realm, 3 duchies | literals at `:1083`, `:1128` | yes | no |
| 17 territories, 37 settlements | canon `systems/settlements/valoria_geography_v30.yaml` (`provinces:`, `settlements:`) | `type`, `territory`, `faction` only | no |
| quarters and buildings (60 communities, 211 hearths) | `engine/season/venues.yaml` by settlement type | yes | no: one stamp per type |
| sites | `SITE_YIELD` kinds, one of each producing kind per settlement; one dwelling per hearth; one garrison per settlement, all at full `condition_scale` | yes | no |
| cast: 46 persons | `engine/season/cases/NPC*.yaml` through `npcs.yaml` and `references/npc_registry.yaml` | name, institution, home, want, concerns, pursuits | pursuits only as a fallback draw that is unreachable on today's data (`:1334-1344`) |
| cohorts: 37 | `cohorts.yaml`, one row per settlement, `weight: 2` each | yes | no |
| seats, goals, acquaintances, arms | `offices.yaml`, `goals.yaml`, faction co-membership, `rosters.yaml: arms_at_build` (empty) | yes | no |

Probe P1 (§12): `build_realm(0)`, `(1)`, `(2)` give equal rungs, persons, names, pursuits, attributes,
sites and conditions, stores and offices. The only differences are the stored `world_seed` and the ids of
two `hold` tenures (minted by a seed-keyed hash). 83 persons; 0 hold an attribute in the shipped arm
(`cast_attributes=False`); 37 of 37 settlements carry the site signature `(garrison, harbour, seam)` with
empty stores. **The seed is an input to the dice and to nothing in the world.**

### 2.2 Differentiation that canon already authors and the build does not read

The geography file carries, per settlement, `stats: [P, D, O]` (Goldenfurt `[2, 0, 2]`) and a description
of its defining tension; per territory, `fort_level`, `spiritual_weight`, `proximity_calamity`,
`starting_pros`, a terrain row, water, radiation bands and `poi_catalog` (counts of resource, secret,
remnant and anomaly points of interest, "discovery via Survey"). Of these the season code reads
`fort_level` (the mass-battle wrapper, `seam/wrappers/mass_battle.py:242-266`) and terrain and water
(battle fields). The build reads none of them. The first step of differentiation is therefore not
generation at all: it is reading canon (the SE lane's `07_SE_ground_and_granaries.md`, CP-T08-02).
Generation's part is the *instance within the canon band* and the *placement* canon leaves open (where
a territory's one secret lies, which settlement is short this year).

### 2.3 What is missing, by the list in the charge (cited, not redone)

| missing | evidence | owner of the finding |
|---|---|---|
| 37 identical settlements; no scarcity; no population dynamics | "37 settlements are stamped identically… produce about twenty-one times what they eat" | `audits/07_SE_audit.md` §0, F-SE-01..04; P1 here |
| persons with no attributes, no lineage, no history | 0 of 83 hold an attribute (P1); `Person` carries no birth or kin field; one cast row authors `stats:` (`build_realm` docstring, `:1019-1027`) | `audits/02_CHAR_audit.md`; P1 here |
| the corpus is one template run 143 times | `harness/corpus_run.py:467-662`, F-CORE-02 | `audits/01_CORE_audit.md`; `12_ARCS_adjudication.md` §2.2 |
| cases with no detective trail | one covert kind (`rosters.yaml: covert_kinds: ["record.forged"]`); `examine` never forms; `reconstruct` writes nothing; no accusation executes; 0 trails found in computed play | `audits/08_FI_audit.md` §0; `D_T06.md` rows 2, 8, 12, 16; `19_LACUNA_…` §0 |
| no world generation carrier beyond the roster | `ED-WR-0011` (ruled 2026-09-13: "World-gen NPC count, for now, is just the 46 NPCs we built. We will return much later"; season-tick generation: none); hole register H-05 and its neighbour on what demands an individuation (`hole_register.yaml:108`, `:584`) | WR lane |
| openings and decks held | CL-OPEN: design RATIFIED (ED-IN-0305), build HELD on `-10` M26; CR-80 (the strife deck) HELD on CL-OPEN's build; CL-EVENTS commits (3), (4): the Tensions receiver, shipped off | `workplans/valoria_master_workplan_v11_part12.md:14-16, :184` |
| no past | no Event precedes tick 0; every ledger is empty of anything older than the build | P2 here |

### 2.4 What a prologue would yield today (probe P2)

Two seasons of the shipped realm, no player: seed 0, 28 s, 37,646 Events; seed 1, 31 s, 34,194 Events
(about 0.17 s per person-season in Python). Story-bearing kinds: `record.forged` 31 and 34 (the one covert
deed that executes and leaves a findable trail), `finding.made` 120 and 122, `record.created` 231 and 252,
`duty.taken` 26 and 0, `tenure.closed` 0 and 3, `matter.determined` 0 and 1, `person.died` 0 and 0. So a
prologue is affordable and already leaves forgeries with true trails in every world; it does not yet
leave a death, a theft, a broken oath or a lost field, because the verbs that would are refused nearly
every time (`audits/09_WR_audit.md` §0: `challenge` 0 of 476). **The prologue's value is bounded by the
verb build-out (`proposals/14_VERBS_*`), which is why it is sequenced after it in §8.**

## 3. Constraints the kit must satisfy

| constraint | source | consequence for the kit |
|---|---|---|
| No deterministic resolution; seeded replay is allowed | `AUDIT_BRIEF.md` standing rule | every generator choice among lawful alternatives is a keyed draw with table weights; no argmax, no "the best candidate gets the seat"; eligibility checks may be fixed |
| The world moves by itself in exactly three ways (matter, bodies, fading); every other clock was wound by a nameable act | `architecture/meta/01_AXIOMS.md` AX-5, T-c | no event director; no storylet fired by a clock; "storms" are draws inside the MATTER motion; everything else is opened by a person's act |
| A threshold may change what can be chosen; it may never produce an outcome | T-b | a card or seed never carries an outcome, a date or a firing condition |
| "A world-generation roster is not a clock and is lawful; a population that grows on its own is not"; CENSUS individuation is demand-driven only | AX-5 text; `04` PART E row 9 | generating persons at build is lawful; mid-game persons arrive only by a demand an act produced; the same generator serves both |
| Nothing becomes permanent without an author | AX-6 | the generator's tables are the author; every generated fact traces to a table row and a draw key |
| A card is a world-generation draw, read once at build, by no step of the season loop | plan text B10-18:183 (cited in `02_P1_templates.md` §3) | the default churn design uses build-time pools only; an in-act docket is decision D-3 (§11) |
| Closed authored cast of 46 "for now" | `ED-WR-0011` (RULED, provisional by its own terms) | a generated supporting cast overwrites it: decision D-1 (§11) |
| Arcs have no carrier; scripted hooks and sequences are allowed, whole arcs are not | `ED-IN-0225`; FW §11.1 correction | an authored arc enters as cards with role queries and staged goals, never as a script |
| Solvability is a generation-time precondition plus emergent erosion, never maintained against the sim | FW §2.3 correction (Jordan's ruling) | the solvability check runs once, after the prologue |
| No verifier of a conclusion against truth | knowledge-model axiom (`D_T06.md` rows 3, 12) | the game never grades a case; only harness instruments compare to truth |
| Nobility by deed; noble conquest: king, then first Duke of Hafenmark, then first Duke of Varfell, by accomplishment in the secession war | `INSTITUTIONS_BRIEF.md` fixed points | the three founding deeds are pinned scenario facts, never drawn; a generated holder holds by a deed or by a contestable inheritance of one |
| A fact the engine uses lives where code reads it; `systems/**/*.md` is never an input | CLAUDE.md §0.05 | every table is YAML under `engine/season/`; no generator reads prose |
| No special-cased entity or outcome | CLAUDE.md §0; `04` PART D row 27a | a table row keyed to a named faction or person is a *scenario declaration* and lives in the declared scenario block, nowhere else |
| One code path | `AUDIT_BRIEF.md` standing requirement | the playable generated case runs `build_realm` and the season loop, not a fixture world |
| Philosophy P-01..P-15 | `canon/` | generated content asserts nothing about world truth that canon owns (the Thread, the Calamity, founding history); see D-4 for the Thread-bearing families |

## 4. The procedural-generation kit

One sentence each, then the detail: **G0** one keyed draw; **G1** the frame is canon and is not generated;
**G2** ground and endowment drawn inside canon's bands; **G3** population from ground; **G4** the cast in
three tiers through one person generator; **G5** seats filled by persons' acts, weighted by deed; **G6** a
prologue: the real loop run before play; **G7** case seeds: armed motives, committed by persons, leaving
the trails their deed kind leaves; **G8** churn: storms inside MATTER, openings from pools, arrivals by
demand; **G9** names and texts by grammar. Everything is switched, with the present world as the control
arm (`variable: off` reproduces today's hashes).

### 4.0 G0 — the draw

- **Generator.** No new RNG. `engine/season/state/ids.py::H(world_seed, tick, subject_id, purpose)`
  (blake2b; "`purpose` must be unique per DRAW") is the draw owner; world generation calls it as
  `H(world_seed, 0, <entity key>, "worldgen:<generator>:<field>:<attempt>")`.
- **Why keyed and not sequential.** A sequential stream makes every draw depend on how many draws came
  before, so adding one table row re-rolls the world (the seed instability Shadows of Doubt reports,
  null N5). A key per (generator, entity) confines a table edit to the entities it touches.
- **Never an outcome.** A draw picks among alternatives the tables weight. Where state should make one
  alternative likelier (a richer house likelier to hold the seat), state moves the weight; the draw still
  decides.
- **Commensurate.** Weighted choice uses integer weights; graded quantities use the engine's own scales
  (`condition_scale`, stores units, cohort `weight`, the pursuit weights, the attribute block's ranks).

### 4.1 G1 — world frame: canon, not generated

The map (17 territories, 37 settlements, adjacency, terrain, water, passes, radiation bands) is canon and
is read, never drawn. A generated map would be a different game and would orphan every authored place;
answered by canon (ladder step 3), not escalated. What varies between worlds is the *state on the map*.

### 4.2 G2 — ground, endowment and scarcity

- **Generates:** per settlement, which producing sites exist, each site's starting condition, starting
  stores, garrison condition; per territory, where its points of interest lie (canon gives the counts) and
  its climate profile (base rates the MATTER draws of §4.8 read).
- **Inputs:** canon `stats: [P, D, O]`, `starting_pros`, `fort_level`, the terrain row, `water`,
  `poi_catalog`; the SE lane's table `rosters.yaml: site_endowment` (its one owner of which producing
  kinds a territory's ground gives), extended with an `optional:` map of kinds with weights and a
  `spread`; bands by `P` for stores and by `D` for garrison condition in `worldgen.yaml: ground`.
- **Constraints:** a site kind only where its ground allows (a harbour needs water adjacency; a seam needs
  a resource point or mountainous terrain); the canon triplet fixes the band, the draw fixes the value
  inside it; conservation (stores are non-negative integers in existing kinds).
- **Draws:** `H(seed, "worldgen", "endowment", settlement_code, site_kind)`.
- **Validation:** V1 every settlement has at least one food-yielding site or a neighbour with surplus;
  V2 the *scarcity bar*: at least `bars.deficit_settlements` settlements whose expected yield is under their
  cohort's draw and that border a surplus settlement (trade and want are both possible).
- **Data:** `rosters.yaml: site_endowment` (the SE lane's table; no second endowment table) and
  `engine/season/worldgen.yaml: ground, climate, bars` (new, typed, read by
  `engine/season/data/worldgen.py`); canon geography unchanged.
- **Depends on:** `proposals/07_SE_ground_and_granaries.md` (`endowment_mode: uniform | ground`,
  CP-T08-02), which authors the endowment per territory with no draw. This kit adds a third mode,
  `drawn`: the same rows, plus a keyed draw over each row's `optional:` kinds and a spread on stores and
  condition. With no `optional:` and `spread: 0`, `drawn` equals `ground`.
- **Tuning:** `site_endowment`'s optional kinds and weights; the bands and spreads; the scarcity bar.

### 4.3 G3 — population

- **Generates:** each settlement's cohort weight (from type and the drawn prosperity), cohort pursuits (the
  territory temperament rows `cohorts.yaml: temperaments` already supply alpha and beta), cohort stance
  seeds toward the holder (from canon's Order stat and the settlement's tension).
- **Constraints:** weight is an integer on the existing `Person.weight`; no growth rule here (growth is
  the SE lane's survivor S-SE-1 and `07_SE_population_regrowth_B.md`, at MATTER).
- **Validation:** V1 a cohort per settlement; V2 at least `bars.aggrieved_cohorts` cohorts with a negative
  stance toward a seat-holder who can be petitioned.
- **Depends on:** `proposals/07_SE_population_census.md` (the one writer of `(Person, weight)`).

### 4.4 G4 — the cast: three tiers, one person generator

| tier | who | count | source | cost in play |
|---|---|---|---|---|
| A · principals | the 46 authored persons and faction heads | 46 | `npcs.yaml`, `references/npc_registry.yaml` (authored; a row here always wins) | full chooser |
| B · supporting cast | generated at build to fill structural roles: kin of principals (spouse, heir, sibling, a living parent), a keeper per serving building (a priest, a factor, a reeve, a captain), a local seat-holder per settlement once local seats exist, a rival per contested seat, a creditor or debtor per principal with wealth pursuit | table `cast_quota` by settlement type; default Seat 6, City 5, Cathedral-City 5, Fortress-City 4, Town 3, Fortress 2, Village 1 → 12 + 10 + 5 + 4 + 45 + 4 + 14 = **94**, plus kin, capped at `cast_cap` | drawn | full chooser; so the realm goes from 83 to about 180 acting persons and a Python season from about 14 s to about 30 s |
| C · the many | cohorts (`weight > 1`), individuated one at a time when an act demands a person (`person.demanded` → `person.individuated`, `04` PART E row 9) | 37 cohorts | drawn *at the demand*, by the same generator | none until individuated |

The three tiers are the tree's own Two-Tier Generation (`investigation_systems_v30.md` System 1, intent
only), Shadows of Doubt's cheap-unless-near simulation and RimWorld's small named cast, on carriers that
exist. **One generator, two call sites** (build, and CENSUS individuation) is the one-code-path rule
applied to people.

**What `generate_person(seed, key, slot) -> PersonPlan` draws, in order, each keyed:**

1. *Slot* (given, not drawn): the role being filled (kin of X; keeper of building B; claimant to seat S),
   which fixes home, institution and the anchor relation.
2. *Heritage and name:* heritage from the home territory's culture weights; name from the heritage's
   grammar (G9), refused on collision with canon or cast.
3. *Born:* an age band from the slot (an heir is younger than the parent by at least `min_parent_age`),
   written to the existing `Person.born` as a negative season count.
4. *Lifepath:* origin × formation × vocation rows (table `lifepaths`), the "History" key the ratified
   dossier design already names (`02_P1_templates.md` §1: "expands into the fields above at build and is
   never stored"). Each row adds to the attribute block and to practice keys.
5. *Capabilities:* the sum of lifepath rows, plus a keyed spread, written through the one capability
   surface (`proposals/02_CHAR_capability_definitions.md`, `01_CORE_capability_authoring_surface.md`,
   `10_DICE_capability_axiom_map.md`). The generator defines no capability; it references definitions.
6. *Convictions and pursuits:* weights over the fifteen pursuits from the territory temperament and the
   institution's creed; then the **deviation draw** (table probability, default 1 in 3): one pursuit is
   re-drawn from the opposite end of the local distribution. This is the tree's Tier-2 deviation roll made
   a table value: the orthodox believer in the Thread-aware valley, the Crown clerk who wants liberty.
7. *Relations:* the anchor relation from the slot, then up to `relations_per_person` more drawn among
   persons within reach (same settlement, same institution, kin of kin): kin, patron and client, rival,
   creditor and debtor, old comrade, old enemy. Each is written as a stance row and a firsthand claim on
   existing carriers (`proposals/02_CHAR_relations_have_a_ground.md`). A relation with a negative stance
   carries a *ground* (the claim says why), so a later reader can find the grievance.
8. *Goals:* none invented. A person's ambitions come from role-bound goal rows on the seat, body or
   faction they sit in (`goals.yaml`), and from cards (G7, G8) that bind to them by query.
9. *Knowledge:* up to `seed_claims` firsthand claims about their own relations and place (the dossier's
   "up to 12 seed claims"); nothing about anyone they have no channel to.

- **Constraints:** canon name reservation; the naming gate; `04` row 27a (no table row keyed to a proper
  noun outside the scenario block); a generated person never holds a principal's seat at build; kin ages
  consistent; every person has a home, at least one pursuit and at least one relation.
- **Validation:** V1 the above; V2 the *tension bar*: at least `bars.rival_pairs` pairs with opposed top
  pursuits who share a venue or an institution (Kybartas et al.'s tension, counted, not plotted).
- **What it does not do:** it does not generate a personality the chooser cannot read. Every drawn field
  has a reader today or in a cited proposal; a field with no reader is left out (Adams: "one layer below").

### 4.5 G5 — institutions and seats, filled by deed

- **Today:** 33 seats, all held by principals (`offices.yaml`: 18 appointed, 8 elected, 6 unspecified, 1
  inheritance). No local seat exists (no mayor, reeve, parish priest, guild factor, captain of a
  garrison), which is why a village has nobody to petition.
- **Generates:** nothing at the top. Local seats are *role templates instantiated per settlement type*
  (table `local_seats`: post, rung kind, remit, conferral, the conferring seat), the P1 dossier's "local
  Mayor seat" generalised. Their first holders are filled in the prologue by the conferring seat-holder's
  own `confer` (appointed) or by the body's election (elected), each a draw.
- **At a build with no prologue** (the control and fast arms): a keyed weighted draw over eligible
  candidates, weights from *deed standing*; never the top-ranked candidate by rule.
- **Deed standing** is a query, not a stored rank (T-a: an aggregate cannot be stored), and it is each
  viewer's own: the institution lanes define it as `person_q.accomplishment(viewer, candidate)` over the
  deed claims in the viewer's ledger ("There is no world-level rank", `audits/15_INSTITUTIONS_COLONIAL.md`
  §5; the Byzantine lane's §6 gives the rule and "the Roll", a Record of the founding settlement; the
  Venice lane's §5.3: "the roll is by warrant, not by blood"). This kit defines no rank. It consumes that
  query (the conferrer's reading of the candidates sets the weights) and generates its inputs: deeds in
  the prologue, pedigree Records, and the claims that carry them.
- **The fixed points, pinned:** the secession war's three founding deeds are scenario declarations (the
  institution lanes' "three seeded founders and deeds"), minted at build as Records (the Roll) with
  hearsay-grade claims in the realm's ledgers, in the order Jordan stated: the first king, then the first
  Duke of Hafenmark, then the first Duke of Varfell. They are never drawn. Invariant V1: no generated
  pedigree Record at build carries a deed the tables weight above the third founding deed. What play may
  do is another matter: a new accomplishment can raise or unseat a house, by acts.
- **Inheritance is contestable by construction:** an heir holds a claim "my house holds by my
  grandfather's deed" whose source is a Record, not an Event the heir witnessed. A rival may challenge
  the Record (`construe`, `forge`, a hearing). The generator makes sure at least `bars.contested_seats`
  seats have a second eligible person with a goal row toward them.

### 4.6 G6 — the prologue: history simulated forward

- **What it is:** after the build draws the realm, the *real* season loop runs `prologue_seasons` seasons
  (default 4, one year) with every person on the ordinary chooser and no player. Play begins on the
  resulting world. Nothing is renumbered: play starts at tick `4 × scenes`, and every `since` and `when`
  stays true.
- **Why:** it is the only lawful way to give a world a past under AX-1 and AX-6 (every past fact has an
  author: the person whose act it was). It is the Shadows of Doubt and Dwarf Fortress method, and it costs
  no new mechanism: `harness/populated.py::run` is the code.
- **What it leaves:** Events with causes, claims with provenance and decay, stance moved by experience,
  seats conferred, obligations sworn and broken, records made and forged, findings, and (G7) committed
  covert deeds. The player's first season is somebody else's fifth.
- **Pre-history beyond the prologue** (parents, the secession war, a house's old feud) is *tradition*,
  not simulated: Records (pedigree rolls, charters, a chronicle) and hearsay-grade claims whose source is
  the Record. This is the Qud method used only where Qud's authors say it holds (accounts met as
  artefacts) and labelled as such (`E15.Q2`: the design says which causes are recorded and which are
  tradition). A tradition can be false, forged or contested, which is the point under nobility by deed.
- **Constraints:** no second simulation at a coarser cadence (two ladders for one quantity is an S defect;
  aging and birth are unbuilt). Depth beyond one year is decision D-2.
- **Draws:** the loop's own. **Validation:** V2 after the prologue (§5) and the solvability check (G7).
- **Cost:** about 14 s per season for 83 persons in Python (P2); about 30 s at the tier-B cast. Four
  seasons at build is one to two minutes in the oracle; it is a load-time cost in the port, and a world
  can be saved after its prologue.
- **Honest limit:** today's prologue leaves forgeries and little else (§2.4). Its yield rises with the
  verb build-out, not with this kit.

### 4.7 G7 — cases: armed motives, true trails

**The adaptation.** Shadows of Doubt picks a killer and simulates the murder. Valoria may not pick an
outcome (T-b; scripting drift). So the kit generates the *conditions* of a wrong and lets a person's own
choice commit it:

1. **A case seed is a card** in the one world-card schema (§4.8): `eligible` (a build query over persons
   and relations that must bind: *motive*: a debt past term, a rival for a seat, a stance at or below a
   floor with a ground; *means*: a capability at or above a rank, or a held office with the remit;
   *opportunity*: shared venue or residence), `roles` (doer, wronged, and optionally a beneficiary and an
   accomplice, each bound by query), `goal_rows` (a role-bound goal on the doer whose object is the
   wronged person, the seat, the record or the store, with a stance), and at most one seeded claim (what
   the doer knows that makes the deed thinkable). No outcome, no date, no firing condition.
2. **The deed is the doer's act.** During the prologue (or in play) the doer's chooser weighs the goal
   like any other; if chosen, the ordinary verb resolves by draw (`forge`, `conceal`, `seize`,
   `sabotage`, `fight`, `lie`, `destroy_record`, and others as the verb lanes build them). It can fail,
   be witnessed, be half-done, or never be attempted. A world where the seed did not fire has a resentful
   debtor and no crime, which is also a situation.
3. **The trail is what the deed kind leaves.** The Event log is the trace store: every Event is kept with
   its causes (the equivalent of Shadows of Doubt saving every object). `rosters.yaml: covert_kinds`
   already declares which deed kinds leave a findable trail (`epistemic.trail_of`); it has one member.
   Each new member is a roster line once its verb emits. The kit adds a per-kind **leaving pattern** to
   that roster (data): which channels a deed of that kind deposits to (co-located witnesses; a Record
   altered; stores changed; a body changed; a Site's condition changed; a tenure closed) and how fast the
   world-side trail fades (`fade_per_season`, a modifier on the inquiry's obstacle that grows with the
   trail's age; state sets the odds, the inquiry's draw sets the finding; never a cut-off). This is the
   precedent's "signature evidence pattern", keyed to the *act* and not to a killer archetype.
4. **Reading it is the fieldwork verbs', by draws:** `examine` a Site (once it forms:
   `08_FI_07_shortest-playable-case.md` §2), `interview` and `interrogate` holders
   (`08_FI_06_testimony-names-a-hand.md`), `research` Records, `surveil`, then a committed conclusion
   (`19_LACUNA_conclusion_is_a_committed_assertion.md`), evidence cited in a hearing
   (`08_FI_05_evidence-interface_B.md`, `12_ARCS_cited_evidence.md`), a verdict by draw
   (`19_LACUNA_verdict_ladder_and_reversal.md`). The kit builds none of these; it supplies what they read.
5. **Solvability, once.** After the prologue the generator (which may read truth; no person may) checks
   each committed covert deed for a *reachable chain*: from a seat whose remit includes `open_case` or
   `determine` and whose scope covers the place, through formable inquiry candidates (a holder of a
   claim about the Event who can be reached; a Site or Record on its trail), to a claim that names the
   doer. The world must hold at least `bars.reachable_deeds` such deeds or it is redrawn. The check is
   never run again: evidence then erodes, witnesses die and lie, and a case may become unsolvable in play
   (the FW §11.1 ruling: precondition plus emergent erosion).
6. **No case object, no grade.** The case exists in the world when a seat-holder's `open_case` opens it.
   Nothing in the game compares a conclusion to truth. A wrong conviction stands until someone's act
   overturns it.

- **Families** (each a pool; rows are data): forged title; embezzled levy; stolen relic or record;
  poisoned well or ruined store (`sabotage`); a killing in a quarrel; a broken oath concealed; a hidden
  heir; smuggling past a toll; a false accusation (a seed whose doer's goal is to have the wronged person
  condemned: the case *is* the lie). The Thread-bearing families (a practitioner's concealed working) wait
  on D-4.
- **Constraints:** a seed binds only to a motive that exists in the drawn realm (no motive, no card);
  never names a person; the doer may be a principal (an authored person can be guilty in one world and
  innocent in the next).
- **Tuning:** pool rows, `seeds_per_realm`, the leaving patterns, the fade rates, `bars.reachable_deeds`.

### 4.8 G8 — events and world churn

Three sources. None is a director (null N4 stands; §11 D-3 says what that costs).

1. **Storms: draws inside MATTER.** Weather, yield, wear, illness and spoilage are the licensed motion.
   The kit's part is a per-realm **climate profile** drawn at build (each territory's base rates inside
   its canon terrain band), so the bad land is a different land in each world; the per-season draw with
   memory is `proposals/09_WR_B_weather_with_memory_and_the_year.md` and CL-EVENTS's force-weather row. A
   storm's odds read state (last season's weather, the season of the year, site condition); its result is
   a graded draw; what persons do about it is theirs.
2. **Openings: one world-card schema, four families.** CL-EVENTS's Tensions cards, CL-OPEN's set pieces
   (ratified design: "drawn from pools at world build, opened only by a person's own act"), CR-80's
   strife deck and G7's case seeds are the same object: `id, family, source, eligible, attach, roles,
   goal_rows, seed_claim, opens_with`. The kit specifies that one schema and one loader, so three held
   positions land on one receiver. A world draws `k` cards per family from pools of at least `k²` (the
   ratified sizing: expected overlap between two worlds under one). Selection weight reads the drawn
   realm (a card whose roles bind to a tenser pair is likelier), which is "draws depend on state" without
   a clock.
3. **Arrivals: demand-driven individuation through G4.** When an act demands a person who does not exist
   (a `dispatch` to a clerk, a `recruit`, a `confer` on a vacant local seat with no candidate), CENSUS
   individuates one from the place's cohort. With G4 at that call site the new person arrives with a
   lifepath, a deviation, relations into the place and, with table probability, a card bound to him. New
   blood with new wants, authored by the demand.
4. **Succession churn** needs no generator: G4's kin and G5's contested seats mean a death (bodies motion)
   opens a contest among people who already exist.
5. **Re-arming in play** is the open question (D-3): build-time pools are finite and a long game spends
   them. The lawful extension is a docket read *inside a seat-holder's `convene`* (the card carries no
   date and no outcome; the draw is authored by the convener's act, so T-c holds); it amends plan text
   B10-18:183 and B10-19:95 and so is Jordan's.

### 4.9 G9 — names, texts and flavour

- **Names:** a replacement grammar per heritage (given name, byname, patronymic or toponym) in
  `engine/season/worldgen_names.yaml`; draws keyed by person; refused on collision with
  `references/names_index.yaml`, the cast, or the deprecated-name list (the naming gate still runs).
  Settlements are canon and are never renamed. Generated buildings take their type name plus the
  settlement's (the present rule).
- **Texts:** a Record's body and a chronicle line are rendered from the Record's `subject_matter` and the
  Event's `changes` and `causes`; a rendered cause is always a recorded cause, and a tradition is marked
  as said, not known (`E15.Q2`). The chronicle is the WR lane's (`09_WR_B_chronicle_that_tells.md`); this
  kit owns only the name grammar and the Record templates for generated documents (pedigree, charter,
  letter of debt, levy roll).
- **Flavour** (physique, speech, a house device) is colour read by nothing; it lives in the same file,
  outside the hash only if a `colour:` block is declared display-only, and is the last batch.

## 5. Validation: a world that can be rejected, and a bar that can fail

| tier | when | what | where | on failure |
|---|---|---|---|---|
| **V1 invariants** | at build, before anything is minted | ladder legality; every settlement has a building, a dwelling and a cohort; every seat-holder eligible; ages consistent; every person has home, pursuit, relation; every goal row and card role binds; no name collision; founding order; non-negative stores | the loader and `worldgen.draw` (a refusal, the licensed form: "the loader's refusal per data family") | raise, naming the row: a table defect, never redrawn around |
| **V2 story possibility** | at build (structural) and again after the prologue | counts of armed situations against `worldgen.yaml: bars`: deficit settlements beside surplus; aggrieved cohorts; rival pairs; contested seats; debts with a term; secrets (a claim held by one person that another's goal would act on); after the prologue, reachable covert deeds | `worldgen.possibility(w) -> dict` | redraw with `attempt + 1` in every key, up to `max_attempts` (default 8); then raise. The rejection rate is reported; above one in five the tables are wrong and are edited, since rejection bends the distribution |
| **V3 the story bar** | a harness run, never at a player's build | over N seeds × S seasons: the chain reading (`harness/chronicle.py --chains`, CR-69, "the one owner of CL-OPEN's variety reading"); the variety instrument specified in the ratified design (`02_P1_templates.md` §1: mean pairwise Jaccard of chain signatures, and the stock share); an expressive-range table over world metrics (scarcity index, contested seats, cast size, relation density, reachable deeds) | `engine/season/harness/` | the batch does not close |

**Controls every V3 reading carries:** the same seed twice reads identical; `variable: off` is the floor
(today's world); the dice-only arm (same world, different dice seed) gives the spread generation must
exceed; an empty-pool arm gives an equal hash. **Two-sided falsifier** (the ratified one): a generator
fails if it does not lower mean similarity between worlds by more than the dice-only spread, *or* if it
raises the stock share.

**What validation is not.** It is not a guard on process (CLAUDE.md §0.1 pt 5): every check sits on the
path that builds the game's world or on the instrument that closes a batch. It is not a drama manager:
it runs before play and never again. It is not a quality measure: null N6 stands, and no reading here
says a story is good; the bar counts whether the conditions and the chains exist.

## 6. Authoring surfaces, and the split between generated and authored

**What Jordan edits to change the texture of the world** (all YAML, all read by code, all with a control arm):

| file | what it changes | example edit |
|---|---|---|
| `rosters.yaml: site_endowment` (the SE lane's) · `engine/season/worldgen.yaml: ground, climate` | how rich, how uneven, how harsh | widen `spread` on the stores band: more famine years, more trade |
| `… · cast_quota`, `cast_cap`, `relations_per_person`, `deviation` | how crowded, how entangled, how many misfits | deviation 1 in 3 → 1 in 2: more hidden sympathisers |
| `… · lifepaths` | what kinds of people there are | add `formation: scriptorium novice` with its attribute rows |
| `… · local_seats` | which small offices exist | add a toll-keeper at every river Town |
| `… · bars` | how much trouble a world must hold to be accepted | `contested_seats: 3 → 5` |
| `… · prologue_seasons` | how deep the past is | 4 → 8 |
| `engine/season/world_cards.yaml` | openings: tensions, set pieces, strife seeds, case seeds | add a case family row; change `seeds_per_realm` |
| `engine/season/rosters.yaml: covert_kinds` | what a deed leaves and how fast it fades | `record.forged: fade_per_season` |
| `engine/season/worldgen_names.yaml` | how the world sounds | a new byname list for Varfell |
| `engine/season/npcs.yaml`, `references/npc_registry.yaml`, `offices.yaml`, `goals.yaml` | the authored principals (unchanged surfaces) | pin a person, a seat, a goal |
| `engine/season/worldgen.yaml: scenario` | what is pinned in *this* scenario: founding deeds, named holders, any proper-noun row | the only place a table row may name a faction or person |

**The tuning loop** is one command: `python -m engine.season.harness.worldgen --seed N --sheet` prints the
drawn realm as dossiers (each settlement, seat and person on one page, the drawn fields beside the live
queries, per the ratified dossier report) and the V2 counts; `--range N` prints the expressive-range
table over N seeds. A table edit is seen in seconds without a season run (Adams: "adjust a parameter and
see the response in a short loop").

**The split.**

| stays authored | is generated |
|---|---|
| canon: the map, the factions, the Thread, the Calamity, history to the secession war and its three founding deeds | the state on the map: endowment, climate, points of interest, stores |
| the 46 principals: names, convictions, seats, cited wants | their kin, rivals, creditors, keepers, clerks: the supporting cast |
| the top 33 seats and their bodies | local seats and their first holders (by persons' acts) |
| set-piece arcs, as cards with role queries and staged goals | which cards a world draws, and who is cast in the open roles |
| capability definitions, verbs, procedures | each generated person's ranks, through lifepaths |
| the names of places and principals | everyone else's names; documents; pedigrees |
| nothing about what happens | nothing about what happens: outcomes are persons' acts and draws |

**How an authored arc plugs into generated context.** An arc is authored as one or more cards plus a
ladder: named roles are pinned to principals; open roles ("a rival", "the clerk who keeps the roll", "a
witness") are queries that bind to generated persons at build (Wildermyth's casting: most important role
first; a mandatory role that cannot bind means the card is not drawn, and the sheet says so); the arc's
stages are `goal_stages` rows (`proposals/12_ARCS_arcs_as_staged_goals.md`). The arc then runs on a
realm with kin, debts and neighbours it did not have to author, and differs between worlds by who was
cast and what the prologue did to them. The provided corpus's per-case setup blocks
(`01_CORE_case_setup_and_beats.md`, `12_ARCS_case_on_the_realm.md`) are the same idea from the harness
side: a case's `setup:` becomes a card's `eligible` and `roles`, and the case runs on the realm rather
than on a template world.

## 7. Resolutions (inconsistencies, gaps, unclear passages)

| # | item | resolution, decided | ladder step | carried by |
|---|---|---|---|---|
| R-21-01 | Four held or proposed card receivers (Tensions, CL-OPEN set pieces, CR-80 strife deck, case seeds) with four schemas | One `world_cards` schema and one loader; each is a `family` | 5 (one owner per operation) | `21_PROCEDURAL_D_world_cards_and_churn.md` |
| R-21-02 | `build_realm` takes a seed and draws nothing from it | The variable layer is a declared arm, `variable=`; `off` ships until each batch flips its own switch as a declared mover | 4 (the `foreign`, `guards`, `cast_attributes` precedent) | `21_PROCEDURAL_A_worldgen_tables_and_ground.md` |
| R-21-03 | Canon geography's `stats`, `starting_pros`, `poi_catalog` are read by nothing in the build | Read them (the SE lane's proposal), then draw inside their bands | 3 (canon answers it) | `07_SE_ground_and_granaries.md`; `21_…_A` |
| R-21-04 | `npcs.yaml` header: "Inventing an NPC in this file would be exactly the fabrication ED-WR-0011… avoid", against a generated cast | Generated persons never enter `npcs.yaml`; they are minted from tables with a draw key (AX-6: the table is the author). The ruling's count is D-1 | 5, and escalated for the count | `21_PROCEDURAL_B_cast_and_seats.md` |
| R-21-05 | "Trace" as a new carrier versus the Event log | No new carrier: the Event log and `covert_kinds` are the trace store; add leaving pattern and fade to that roster | 4 (FI-03's precedent) | `21_PROCEDURAL_C_prologue_and_case_seeds.md` |
| R-21-06 | Solvability: "the generator guarantees a chain" against "never a constraint maintained against the sim" | Checked once after the prologue; never again | 1 (FW §11.1's correction supersedes the bare invariant) | `21_…_C` |
| R-21-07 | Killer archetypes (the precedent) against the scripting-drift rule | The evidence pattern is a property of the deed kind; motive is the doer's own goal row | 5 | `21_…_C` |
| R-21-08 | Pre-history: simulate generations or invent them | Tradition as Records and hearsay claims, labelled; one simulated year | 5 for the default; depth is D-2 | `21_…_C` |
| R-21-09 | `Person.born` is 0 for all 83 and `heritage` is unset for 79 | Tier B writes both; principals' values are authoring owed in the registry (content, not this kit) | 3 | `21_…_B` |
| R-21-10 | The world builder lives under `harness/` though it builds the shipped world | Out of this lane: placement is a Layer-1 question for `layer-conformance`; the kit adds a pure `data/worldgen.py` and leaves `build_realm` where it is | 5; listed for the CORE lane | none here |
| R-21-11 | A director for pacing (RimWorld) against AX-1 | Refused by axiom. Churn comes from MATTER draws, drawn openings, arrivals and succession; a drought is measured (V3), not prevented | 3 | `21_…_D` |
| R-21-12 | `deviation` as "d6, 5–6" in the archived design | A table probability drawn through G0; no die notation in data | 5 | `21_…_B` |
| R-21-13 | Seed stability under table edits | Keyed draws; adding a row never re-rolls unrelated entities; shown by a probe in batch 0 | 5 | `21_…_A` |

## 8. Implementation plan

Proposals (each `## Status: PROPOSED`, exact edits inside):

- `proposals/21_PROCEDURAL_A_worldgen_tables_and_ground.md` — batches PG-0, PG-1
- `proposals/21_PROCEDURAL_B_cast_and_seats.md` — batches PG-2, PG-3
- `proposals/21_PROCEDURAL_C_prologue_and_case_seeds.md` — batches PG-4, PG-5
- `proposals/21_PROCEDURAL_D_world_cards_and_churn.md` — batches PG-6, PG-7
- `proposals/21_PROCEDURAL_E_names_and_texts.md` — batch PG-8

| batch | what | files and keys | gate (execution artifact) | cost | needs first |
|---|---|---|---|---|---|
| **PG-0** | the switch, the loader, the sheet, the range table, keyed-draw stability | new `engine/season/worldgen.yaml` (empty tables, `variable: off`), `engine/season/data/worldgen.py` (`load`, `draw`, `possibility`), `harness/populated.py::build_realm(variable=)`, new `harness/worldgen.py` (`--sheet`, `--range`) | `variable=off` hash EQUAL at seeds 0, 1, 2; the probe of §12 P1 as a test that *fails* once a table is filled (worlds must then differ); adding a dummy row changes no other entity's draw | small build | nothing |
| **PG-1** | ground, endowment, climate profile, points of interest | `rosters.yaml: site_endowment` gains `optional:` and `spread`; fixture `endowment_mode` gains `drawn`; `worldgen.yaml: ground, climate, bars`; `build_realm` site and store minting reads the plan | 20 seeds: all pass V1 and V2; distinct settlement signatures per world ≥ 10 (today 1); the scarcity index differs across seeds by more than zero and its range is printed; control `spread: 0` equals the SE ground arm's hash; 3 seasons × 3 seeds: at least one `exchange.made` or `requisition.taken` or hunger band crossing per world (today none) | small build | `07_SE_ground_and_granaries.md` (CP-T08-02, CR-22) |
| **PG-2** | the person generator, tier B, relations | `worldgen.yaml: cast_quota, lifepaths, relations, deviation`; `data/worldgen.py::generate_person`; `build_realm` cast step; CENSUS call site | 20 seeds: cast size inside the cap; 0 name collisions; every generated person acts at least once in 2 seasons; cross-person acts naming a generated person > 0; two worlds share under half their generated relation pairs by role; the chooser separates generated persons (Kendall reading as in the CHAR audit) | design-first for D-1, then small build | `02_CHAR_capability_definitions.md`, `01_CORE_capability_authoring_surface.md`, `02_CHAR_relations_have_a_ground.md`, `07_SE_population_census.md` |
| **PG-3** | local seats; pedigree Records as the inputs of deed standing; the founding deeds are the institution lanes' rows, read here | `worldgen.yaml: local_seats, pedigrees`; `offices.yaml` unchanged at the top; the founders and the Roll from `15_INSTITUTIONS_COLONIAL_D_accomplishment.md` and `15_INSTITUTIONS_BYZANTINE_A_dignities_and_the_roll.md` | each world has a local seat-holder per settlement after the prologue, conferred by an act (the `confer` Event cites the conferring seat); over 20 seeds the same seat is held by different persons in at least half the worlds (a draw, not a rule); founding order invariant holds in all | small build | `06_FA_seat_terms_and_turnover.md`, `06_FA_seat_terms_by_body_B.md`, `14_VERBS_BINDING_C_turnover.md`, the institution lanes' deed-standing query |
| **PG-4** | the prologue | `build_realm(prologue=N)`; `worldgen.yaml: prologue_seasons`; world save after prologue | the story inventory per seed after 4 seasons (chain count and kinds histogram, CR-69) is non-empty in every world and differs between worlds beyond the dice-only arm; ledger contents predate play; same seed twice EQUAL | small build | PG-1..3; yield depends on `14_VERBS_*` and `09_WR_B_draws_not_thresholds.md` |
| **PG-5** | case seeds, leaving patterns, fade, solvability | `world_cards.yaml: family: case`; `rosters.yaml: covert_kinds` gains per-kind `leaves` and `fade_per_season`; `worldgen.possibility` gains `reachable_deeds` | **the detective gate**: over 20 seeds, (a) at least one seeded deed is committed by its doer's own act in at least half the worlds, and in none by anything else; (b) an NPC seat-holder with `open_case` opens a case on a generated deed and reaches `determine` by draw in at least one world in four, with the wrong person named in some (reported, not hidden); (c) the player-proxy (`harness/play_surface.py`) seated as an investigator, choosing only among formable candidates, reaches a committed conclusion; its right, wrong and unsolved rates are printed against a uniform-random proxy (the floor) and a seeds-off realm (the control) | design-first, then small build | `08_FI_07`, `08_FI_06`, `08_FI_05_evidence-interface_B`, `19_LACUNA_*`, `14_VERBS_PHYSICAL_A_custody_and_force`, `14_VERBS_PHYSICAL_C_looking`, `14_VERBS_SOCIAL2_C_case_question_confession` |
| **PG-6** | one card schema; build-time pools for the other three families | `world_cards.yaml` (`tension`, `setpiece`, `strife`); `data/world_cards.py`; `build_realm(cards=)` | empty pools hash EQUAL; over 20 seeds the variety instrument's mean similarity falls by more than the dice-only spread and the stock share does not rise; share of drawn cards opened by a person's act within 4 seasons is printed (the known risk: unopened bundles) | small build | CL-EVENTS commits (3), (4); CL-OPEN's release (M26); CR-80 |
| **PG-7** | arrivals through G4; the docket if D-3 says so | `loop/census.py` individuation calls `generate_person`; optionally a `docket` read in `convene` | a demanded person arrives with relations into the place and acts; with the docket on, openings per season after season 8 do not fall to zero (today's build-time pools would) against the docket-off control | small build; docket design-first | PG-2; D-3; `14_VERBS_BINDING_B_sittings.md` |
| **PG-8** | names and document templates | `worldgen_names.yaml`; Record templates | 1,000 generated names: 0 collisions, 0 naming-gate hits; duplicates within a world under a stated rate | edit | PG-2 |

**Order and why.** PG-0 first because every later gate needs the switch and the sheet. PG-1 before PG-2
because people are drawn *into* differentiated places (a creditor needs a rich town). PG-3 before PG-4
because the prologue is what fills local seats. PG-4 before PG-5 because a case is a deed committed in
the prologue. PG-6 can land beside PG-4 once CL-OPEN is released. PG-5 is the last of the core because it
has the most dependencies outside this lane; if the FI and LACUNA proposals have not landed, gate (a)
alone can close PG-5a (deeds committed, trails true, reachable by structure) and (b), (c) wait.

**What is playable alone, and when.** After PG-1: a settlement-scale scenario on a realm with want.
After PG-4: a realm with a past. After PG-5: *the generated inquiry* (§9).

## 9. Playable standalone: the generated inquiry

- **Entry (to build; no such scenario exists today):** the player-proxy of `harness/play_surface.py` and
  `headless.py`, seated on a realm built with `variable=on, prologue=4, cards=on`: the same `build_realm`,
  the same loop (one code path), no fixture world.
- **Situation:** the player-proxy holds a local seat with `open_case` in a settlement where the
  solvability check found a reachable deed. He is not told which, or that there is one.
- **Choices:** the fieldwork verbs on formable candidates only; whom to believe; when to commit; whether
  to bring it to a hearing.
- **Consequence:** a determination that binds a person (or the wrong person); stance and standing move;
  the doer, if free, still has his goal.
- **End:** a determination, a dropped case, or the trail fading past use.
- **Missing today:** everything PG-5 depends on in the FI, LACUNA and VERBS lanes; the kit supplies the
  world and the truth.

## 10. Interfaces

| the kit consumes | from | real today? |
|---|---|---|
| canon ground | `valoria_geography_v30.yaml` | file exists; unread by the build |
| capability definitions and the attribute block | CHAR, CORE, DICE proposals | proposed; CR-20 carrier built, shipped off |
| relations as stance row plus claim | `02_CHAR_relations_have_a_ground.md` | proposed |
| the season loop, the chooser, WITNESS, `trail_of`, `covert_kinds` | `engine/season/` | built and executed |
| deed standing | institution lanes | designed |
| inquiry verbs, conclusion, hearing, verdict | FI, LACUNA, SC, VERBS lanes | mostly proposed |
| weather with memory | `09_WR_B_weather_with_memory_and_the_year.md` | proposed |

| the kit emits | to | 
|---|---|
| differentiated sites, stores, cohorts | SE (the kernel finally has something to account for) |
| a supporting cast with kin, debts and rivals | CHAR (distinguishable people), FA (contested seats), SC (parties with grounds) |
| committed deeds with true trails; reachable-deed counts | FI (something to find), SC (something to try) |
| bound cards | ARCS (arcs cast on a realm), WR (openings to chronicle) |
| the sheet and the range table | GO (what a new-game screen can show: the seed and its world sheet) |

## 11. Decisions for Jordan (survivors of the five-step ladder)

- **D-1 · The cast: 46, or 46 plus a generated supporting cast.** `ED-WR-0011` is ruled "for now… we
  will return much later". *Option A:* keep the closed authored cast; generation covers ground, cards and
  cases among the 46 and the cohorts. A small, fully authored drama; every culprit is a principal; kin
  and rivals must be hand-authored or absent. *Option B:* tier B as in §4.4 (about 94 generated persons
  plus kin, capped). A populated realm in which a village has a reeve and a debtor; doubles the season's
  cost; the player cannot know every face. **Recommended: B, with `cast_cap` as the dial**, because
  cases, succession and local seats all need people the corpus does not hold.
- **D-2 · Depth of the past.** *Option A:* one simulated year, everything older as tradition (Records and
  hearsay). Cheap; contestable pedigrees; no simulated ancestors. *Option B:* a generational pass (births,
  aging, deaths, successions at a year cadence) before the fine year. Legends in the Dwarf Fortress sense;
  needs aging and birth built, and a second cadence the engine does not have. **Recommended: A now.**
- **D-3 · Re-arming in play.** *Option A:* cards are read at build only (plan text B10-18:183 stands).
  Churn after the pools are spent comes from storms, arrivals and succession; a long game may run dry, and
  V3 will show it. *Option B:* a docket read inside a seat-holder's `convene` (no date, no outcome; the
  draw is the convener's act), with repeat suppression. Institutions keep producing business; amends
  B10-18:183 and B10-19:95 (not an axiom). **Recommended: B, after PG-6 shows whether A runs dry.**
- **D-4 · Thread-bearing generation.** 49 of the 143 provided cases turn on the Thread
  (`12_ARCS_adjudication.md` §1). *Option A:* the kit generates no Thread content until the substrate
  ruling (`12_ARCS_substrate_as_ground.md`, Options A and B there) is made; practitioner cases stay
  authored. *Option B:* generate thread sensitivity and concealed workings as a case family now, on the
  existing `thread_sensitivity` field. Risks asserting world truth canon owns. **Recommended: A.**
- **D-5 · A wrong world.** *Option A:* a world that fails V2 after `max_attempts` raises and the player is
  given the next seed. *Option B:* the bars are advisory and any V1-valid world is playable, with the
  sheet showing what it lacks. A is a curated game; B admits quiet worlds. **Recommended: A for the
  default mode, B behind a setting.**

## 12. Evidence log

| id | command | seed, span | outcome |
|---|---|---|---|
| P1 | scratch `probe_seed.py`, `probe_seed2.py` (`build_realm(s)` for s in 0, 1, 2; field-by-field comparison) | seeds 0–2, build only, `PYTHONHASHSEED=0` | rungs, persons, names, pursuits, attributes, sites, conditions, stores, offices EQUAL; 2 `hold` tenure ids and `world_seed` differ; 83 persons, 0 with attributes; 37 of 37 settlements `(garrison, harbour, seam)`, stores `{}`; content hashes differ (`600d8b271474`, `87a285ee2523`, `6c44d18d6a58`) because the hash folds the seed-keyed ids |
| P2 | scratch `probe_prologue.py` (`populated.run(2, seed)`) | seeds 0, 1; 2 seasons | 28.1 s, 37,646 Events; 30.6 s, 34,194 Events; `record.forged` 31, 34; `finding.made` 120, 122; `person.died` 0, 0; ledger sizes 171–535 and 156–548 |
| P3 | scratch census of `offices.yaml`, geography and built persons | build, seed 0 | 33 seats, all held; conferral: appointed 18, elected 8, none 6, inheritance 1; settlement types Town 15, Village 14, Seat 2, Fortress 2, City 2, Fortress-City 1, Cathedral-City 1; 14 distinct canon `stats` triplets; `Person.born` 0 for 83 of 83; `heritage` unset for 79; 0 Events at build |
| W1–W14 | web: 5 searches, 12 fetches on Shadows of Doubt | — | page bodies read: itch.io DevBlog #15 (2019-04-24), #28 (2021-10-01), #30 (2022), devlog index; snippets: DevBlog #10, #13, #2, Wireframe, Edge; blocked or empty: colepowered.com #2, #8, #10; whynowgaming.com; indiedb.com; pcgamer.com; video-only: #18, #23 |

Scratch output: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PCG/`.
Not run: `pytest`; any season run longer than two seasons; `corpus_run` (cited from the CORE and ARCS audits).
`[UNVERIFIED]`: plan text B10-18:183 and B10-19:95 are quoted as `02_P1_templates.md` §3 quotes them, not
opened at their lines; `-10` M26 was not located by grep and is cited as the workplan index states it.

## 13. Provided arcs and characters — adjudication for this lane

Generation owns no arc mechanism; it owns the *context* an arc runs in. The ARCS lane's table
(`12_ARCS_adjudication.md` §3–§5) stands; this adds the generation edge only.

| need class (ARCS lane's mechanism) | cases (count there) | represented today? | what generation changes | proposal | gate |
|---|---|---|---|---|---|
| M-CASE: the case's own people, seats, records, dates | 143 | no (one template world) | a case's `setup:` becomes a card's `eligible` and `roles`, cast on the realm; open roles bind to generated persons | `21_…_D`; `12_ARCS_case_on_the_realm.md` first | the case's roles bind in at least one seed in two; where a mandatory role never binds, the sheet names it |
| kin, heirs, rivals, creditors an arc assumes | the succession, debt and feud arcs | no (0 kin; 0 debts at build) | tier B and relations | `21_…_B` | an heir exists for every inheritable seat in every world |
| a concealed wrong that precedes play | the reveal and trial arcs | only forgeries | case seeds in the prologue | `21_…_C` | the detective gate (a) |
| scarcity an arc turns on (famine, toll, levy) | the Feldmark and Goldenfurt arcs among others | no | endowment and climate | `21_…_A` | hunger or exchange occurs in computed play |
| the Thread as substrate | 49 | no | nothing (D-4) | none | — |

Soonest: the scarcity arcs (after PG-1 and the SE proposals), then succession and feud arcs (PG-2, PG-3),
then reveal arcs (PG-5).

## 14. Capability authoring surface — generation's part

(a) *Where generation takes a capability as input:* nowhere today (no person is generated). In the kit:
lifepath rows add to the attribute block and practice keys; a case seed's *means* predicate reads a
capability rank; deed standing reads Events, not capabilities.
(b) *Data-driven today:* the one authored `stats:` row through `data/cast.py::attributes_of` (CR-20,
shipped off). Everything else is absent rather than hard-coded.
(c) *Target shape:* a lifepath row names capabilities **by the id the one definition table gives them**
and a delta on that capability's own scale; the generator validates each id against the definition table
at load and refuses an unknown one. The single file for definitions is the CHAR and CORE lanes' to name
(`02_CHAR_capability_definitions.md` takes no side between the two candidate paths); the generator's
tables live in `worldgen.yaml: lifepaths` and hold references only.
(d) *RPG axioms implemented:* lifepath character creation (origin, formation, vocation: the Burning Wheel
and Traveller tradition), point bands by age, a deviation or quirk roll, background as the source of
skills. *Lacking, and a designer would expect it:* advancement during the prologue (a person who worked a
year should be better at it: `04` F.6 says "a character never improves at anything"; the `train` verb
exists and its refusal rate is high), and aging.
(e) *Proposals:* `21_PROCEDURAL_B_cast_and_seats.md` §3 (lifepaths), after the CHAR and CORE definition
proposals.

