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

