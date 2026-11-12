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

