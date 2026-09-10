# Settlements · Factions · Populations · Management — a proposal set

## Status: **PROPOSED (2026-09-10). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

⚠ **ED-1094 does NOT apply to this set, and the exception is stated here rather than assumed.**
Merging a PR normally ratifies its `PROPOSED` contents by default. **Nothing in these six files
ratifies on merge.** Every proposal below is a design object for Jordan to accept, amend or refuse;
several would change what the game *is*, and one (`E-1`, `05_COLLISIONS_AND_RESIDUE.md` §4) is a
genuine escalation where two defensible answers lead to materially different games. Landing this
directory changes no `## Status:` line, no ledger row, no `CURRENT.md` row and no code.

## What this is

Jordan, this session: develop multiple proposals for settlements, factions, populations and
management that stem from the **most current code**, incorporate the repository's own research and
reference corpus and an uploaded nine-game systems teardown, take a **bottom-up, primitives-based**
approach, and are compliant with **Layer 1** (`architecture/`, RATIFIED ED-IN-0204) — then evaluate
each for how it fits the game and what it does to gameplay and emergent narrative. Goldenfurt was
added as a reference mid-session.

**How it was produced.** A read-only Fable 5.1 pass developed and evaluated the proposals against the
working tree, briefed from five independent read-only harvests (the settlements corpus, the factions
corpus, the population question, the research corpus, the machine-read registries) and a sixth over
`proposals/`. This write-up is the Opus synthesis of that pass. An independent adversarial critic —
structurally read-only, holding this document and not the reasoning behind it — checked it against
the tree; `05_COLLISIONS_AND_RESIDUE.md` §6 records what it found and what changed.

**Division of labour, stated because `CLAUDE.md` §10 rules on it.** §10 reserves the `fable` tier for
*"read-only audit · planner · orchestrator · guardrail — NOT synthesis or artifact authorship."*
That is the shape used: Fable analysed, specified and evaluated; Opus authored; a read-only critic
attacked. There is precedent for the seat — `architecture/meta/04_CODE_ARCHITECTURE.md` records that
it was itself *"Produced by a read-only Fable 5.1 synthesis."*

## Read in this order

| file | what it holds |
|---|---|
| `00_INDEX.md` | this — the ask, the finding, the seven proposals in one table, what is held back |
| `01_PRIMITIVE_BASE.md` | **Part A** — what the settlement / faction / population primitives actually are in the code today, what is declared-but-dead and under which defect class, and eight corrections to the brief that produced this set |
| `02_PROPOSALS_SUBSTRATE.md` | **Part B, P1–P4** — dearth reaches the body · the bodies clock · individuation is a refusal · founding and building |
| `03_PROPOSALS_POLITICS.md` | **Part B, P5–P7** — the commit share and the faction view · forswearing costs · a dispensation is a document |
| `04_EVALUATION.md` | **Part C** — NERS per §0.06's definitions, gameplay impact in concrete seasons, emergent narrative traced through the mechanism, and cost stated as Layer 1 states costs |
| `05_COLLISIONS_AND_RESIDUE.md` | **Part D** — the Goldenfurt collision table resolved mechanic by mechanic · ratified rulings in conflict · the `Field`/`Gauge` adjudication · the one genuine escalation · what could not be established · **§6, the rulings of 2026-09-06 and the hole they expose** · the loop register as it would stand · the adversarial pass |

> ### ⚠ **READ `05_` §6 BEFORE ANY OTHER PART OF THIS SET.**
> `references/design_rulings_2026-09-06.md` — eight Jordan rulings given **the day after Layer 1 was
> ratified** — was found after this set was drafted, and it moves three things. **R7, flagged there as
> the decisive ruling, ratifies the set's whole approach** (*"no magnitude carrier is admitted at any
> scale. Every aggregate is DERIVED, none is PUSHED"*) **and names what the set is missing:**
> *"`H-62` is unavoidable and first-rank. Nothing moves until a verb writes an interior."* **`H-62` is
> tier 0, grade `absent`, and this set proposes nothing for it.** **R6** adds the second half:
> *"propagation without reaction is a chronicle, not a game"* — and this set is almost entirely
> **producers**. **R2** rules the ratified refusals **instrumental rather than terminal**, each to be
> *"justified against these five [properties] or changed"* — and §6.1 scores this document against that
> honestly, including where it defers to an axiom instead of arguing.

## The finding, in one paragraph

**The repository does not lack a population design. It has two, in independent proposal lineages,
and they agree with ratified Layer 1.** `Rung.envelope` is *packed per-band counts*
(`architecture/holonic_ARCHITECTURE.md:372`), matrix-registered at
`engine/season/write_matrix.yaml:287-293`, and Layer 1 rules that *"Births add weight at the youngest
band; deaths remove it. Birth is envelope weight, not a `create`… **The cohort acts; the envelope does
not**"* (`:401-406`). A cohort is a `Person` at `weight > 1`, one class, no subclass
(`engine/season/state/carriers.py:348`). What is absent is not the primitive but **the dynamics, the
writers and the consumers**: no verb writes `Rung.envelope`, nothing writes `Person.weight`,
`census()` writes nothing and says so (`engine/season/loop/driver.py:1371-1383`), and `mortality` has
zero hits in any `.py` in the tree. The same shape holds one layer up: the ratified ruling that
*"factions… need to hold PEOPLE, and it is the number of people and the weight of their positions
that carry the value of that faction"* (`systems/settlements/reference/scale_hierarchy_v1.md:83-93`,
RATIFIED 2026-07-13) has had its arithmetic written twice and executed never, and the `Faction` view
Layer 1 specifies has **no resolver in `engine/season/queries/`**. So this set proposes almost no new
vocabulary. It proposes producers.

## The seven proposals

Ordered by what they build on. All seven land in `engine/season/` — the tree Layer 1 governs. None
lands in `systems/*/sim/` (retire-set, pre-Layer-1). **None adds a carrier, a `Tenure` kind, an
eligibility kind, a step, a write class or a `Sensation` scalar.**

| | proposal | starts from | adds | loop |
|---|---|---|---|---|
| **P1** | **Dearth reaches the body** — the subsistence shortfall writes `(Person, body)` and emits | `write_matrix.yaml:161-167`; `driver.py:415-436` computes the shortfall and discards it | one write site on an existing row; two arithmetic fixes | **−** damping |
| **P2** | **The bodies clock** — ageing, births and deaths move `Rung.envelope` at MATTER | the `(Rung, envelope)` row; `holonic:401-406`; `driver.py:413` *"BODIES… STILL NOT BUILT"* | one roster (`envelope_bands`), three fixtures, one MATTER pass, one Query | **+** bounded by P1 |
| **P3** | **Individuation is a refusal** — `person.demanded` and the CENSUS mint | `driver.py:1371-1383`; `F.1`; `H-51`; `F.30` | one roster (`demand_kinds`), a CENSUS body on rows that exist | **+** bounded by scenes and the grown band |
| **P4** | **Founding and building** — `found` writes `(Rung, exists)`, `build` writes `(Site, exists)` | two existence rows with **no producer**; `F.20` *"the world only decays"* | two verb rows, two effects | **+** bounded by wear |
| **P5** | **Risk of revolt is a Query** — `commit_share`, the `commit` effect, the faction view | `09_WORKED_EXAMPLES.md:89-91` and `:174` *"not computed anywhere"*; `world_q.py:53-124` | two Queries, one effect, the resolver Layer 1 named and the code lacks | **+** bounded by scenes, presence, repudiation, decay |
| **P6** | **Forswearing costs** — `repudiate`'s effect, as `commit`'s declared closer | `verb_table.yaml:402-412`, which writes `Tenure.until` and raises | one effect | **−** damping |
| **P7** | **A dispensation is a document** — `issue` produces a Record; compliance is a contest per executor | `F.15` *"the entire downward mechanism has no executable content"* | one `Record` kind, one roster of terms, effects for verbs that exist | **−** damping |

**Four amplifying loops, three damping, and every `+` names an existing `−` as its bound.** That is
the point of the set. `ID-16` states the hole it fills: *"A model in which every loop is negative
CONVERGES — season 40 resembles season 30 — and convergence is not a design goal, it is what happens
when a design has no other ideas"*, and *"this design is made almost entirely of refusals… and every
one of them is a damping term."* Measured against the live register, that is exactly right:
`engine/season/hole_register.yaml` carries four `LOOP` rows, of which the two signed `+` are
`H-102` — whose own `default:` cell reads *"UNDER THIS INSTRUMENT'S OWN FIXTURES IT CANNOT AMPLIFY AT
ALL"* (`:1352`) — and `H-112`, a defect bounded by an `if`. **There are zero operative amplifying
loops in the game world today.**

## The one acceptance case that already exists

`engine/season/cases/chain/NPC2.yaml:96-139` — **NPC-083, Hedda Kronvald**, governor of a
five-adjacency chokepoint. It is the corpus's **only** `scale: settlement` case (against realm 48,
faction 47, person 37, world 10), and its seven `season_requires` are Goldenfurt's pillars verbatim:
a bounded budget, a method choice, a Directive answered by comply/bargain/defy, Needs independent of
the Directive, durable marks surviving succession, actor-versus-actor conflict, and a self-adjusting
pressure. Its eighth row says the whole thing *"is itself an unratified proposal explicitly gated on
a settlement registry that does not yet exist in the engine."* **Four of NPC-083's seven `season_requires` are met, two are met in vocabulary only, and one is
refused with its price.** ⚠ **The first draft scored it "six of seven met" and the adversarial pass
overturned that on the set's own disclosures.** **Need 3** (`NPC2.yaml:107-109`) asks for a directive
answerable comply/negotiate/defy *"with **repeated defiance accumulating toward a threshold that
eventually forces a reckoning**"* — and P7 refuses exactly that second half (*"no threshold recalls
anyone; a person with the remit **chooses** `revoke`"*), by **the same `T-b` argument used to refuse
need 7**. **Need 2** (method choice) is met in vocabulary only: its re-expression ends *"effects for
`exchange` and `levy` are `W31`"* — unbuilt, and not proposed here, which under §0.2 is not met. The refused one is need 7, self-adjusting pressure
(`05_COLLISIONS_AND_RESIDUE.md` §1 row 1).

## What is held back, and it is everything

Called out here because `CLAUDE.md` §2 requires anything needing separate sign-off to be named
*loudly* rather than bundled:

1. **The whole set is a design proposal.** No `## Status:` line flips, no ED row closes, no
   `CURRENT.md` row moves, no code changes on merge.
2. **`E-1` is a genuine escalation and the only one, and it is FILED as `ED-SE-0051`**
   (`needs_jordan: true`, `status: open`) so it survives the session boundary — whether the demographic loop is bounded by
   **matter alone** (a fed hearth grows until it cannot feed itself; Malthusian waves the player
   damps with grain) or **by matter plus hearth capacity** (Banished's housing lever; the player
   throttles growth by building). Two defensible options, materially different games, and Layer 1 is
   silent: §25 licenses the clock and names no bound. `05_COLLISIONS_AND_RESIDUE.md` §4 prices both.
3. **Every number in the set is `assumption`** with a named site and a three-point sweep, per `ID-6`.
   **No proposal here proposes a value.** The bands' count and names, `band_seasons`, `fertility`,
   `mortality[band]`, the body-loss coefficient, the founding stake, the `commit_share` floors — all
   swept, none ruled.
4. **Two proposals fix a defect by overturning a written refusal, and BOTH are named.** P1 requires
   `driver.py:431-436`'s refusal of starvation to be overturned as a misreading of `T-b` and L4.
   **P7 requires `verb_table.yaml:117`'s refusal of `{form: existence, of: subject, kind: Record}`
   for `comply` to be overturned** — the row's stated reason is that *"no in-chain document says"* an
   act's subject is the dispensation, and P7's whole move is to **make the dispensation an in-chain
   document** (a `Record` of kind `dispensation`), so the reason lapses rather than being waived. It
   does **not** coin an operand, which `rosters.yaml:873-876` reserves to the `H-94` ruling. §0.05
   says *"decide and then CHANGE THE CODE"* — both are stated as decisions, not slipped in. The
   asymmetry is itself a finding: the first draft flagged P1's overturn and missed P7's
   (`05_COLLISIONS_AND_RESIDUE.md` §8.1 finding 10).
5. **Eight measured claims in the brief that produced this set were wrong**, and they are corrected
   in `01_PRIMITIVE_BASE.md` §3 rather than quietly dropped — including one of mine that a synthesis
   would otherwise have carried forward as fact.
6. ⚠ **THE SET HAS A NAMED HOLE, AND IT IS THE ITEM JORDAN'S OWN RULING CALLS FIRST-RANK.** R7 holds
   that *"`H-62` is unavoidable and first-rank — nothing moves until a verb writes an interior"*, and
   `H-62` is **tier 0, grade `absent`**: no verb in the table writes any `Person` interior field, so
   convictions cannot move, `choose` scores against a constant, and `standing` has nothing to diverge
   from. **None of P1–P7 writes one** — P1 writes `Person.body`, which this set's own argument grades
   as read-off matter rather than interiority. **Stated as a gap rather than patched**, because the
   repair is a design object in its own right: the *shape* is already supplied by the `Degree`-keyed
   `writes` column, and what is missing is **which verbs write which axis at which degree**. That is
   the proposal this set did not make, and the honest place for a reader to start after it.

## What this set does not do

It does not bridge `engine/season/` to the legacy campaign (`engine/mc_v18.py` + `systems/*/sim/`).
That is `W28` + `W27`'s work (`architecture/PLAN.md:1583-1624`), and these proposals supply what
`PLAN.md` §4B.2 says re-scaling the 47 faction-scale cases does **not** buy: *behaviour*. It does not
propose a settlement registry, an AP economy, an event deck, a Directive cadence or a pressure meter —
`05_COLLISIONS_AND_RESIDUE.md` §1 says for each Goldenfurt mechanic whether it is re-expressed,
refused, or kept as evidence Layer 1 is missing something, and names the price of each refusal. And
it adds no guard, no register and no apparatus: `proposals/2026-08-25-throughlines-and-precedent/`'s
own closing rule — *"No new guard on the apparatus. No new register. No document whose existence
would count as progress"* — binds here too.

---

_Lane: cross-cutting. Touches SE (settlements), FA (factions), WR (world) and IN (the season loop and
Layer 1 conformance). **No ED ids are allocated**: nothing here ratifies, and
`references/id_reservations.yaml` is read at ratification, never at proposal time
(`next_free` at time of writing: SE 51 · FA 39 · WR 10 · IN 207)._
