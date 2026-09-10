# Part A — the primitive base, from the code

## Status: **PROPOSED (2026-09-10). HELD BACK IN FULL** — see `00_INDEX.md`.

Every `file:line` below was opened. Root is `/home/user/ttrpg/`. Where a claim is about a rule rather
than a line of code it carries its axiom, theorem, idiom or register-row id. This part describes what
**is**; `02_` and `03_` propose.

---

## §1 · What the primitives actually are today

### §1.1 The containment ladder is complete and addressable

`engine/season/rosters.yaml:89-92` —
`rung_kinds: [person, hearth, community, settlement, territory, province, duchy, realm]`, `open: true`.
The title ladder is already keyed to it (`rosters.yaml:562, 595-611`, "TOTAL OVER `rung_kinds`",
Jordan 2026-09-02): `King/Queen → realm · Duke/Duchess → duchy · Count/Countess → province · Lord →
territory · Mayor → settlement · Community Leader → community · Family Head → hearth · Individual →
person`. That is Stage 2's *"rank is the ordinal of a seat's domain in the containment roster"*
(`architecture/meta/02_HIERARCHIES.md`) already sitting in data, requiring no second scale.

`Rung` is a plain class with a whitelist (`engine/season/state/carriers.py:510-511`):
`{id, kind, stores, sites, records, dates, stake, envelope, transmission, judging_set_rule, yield}`.
`__setattr__` raises on anything else at `:531-538`, citing S10.1; the constructor raises on
undeclared kwargs at `:527-529`. So **the no-social-aggregate rule is live in code, not asserted** —
`r.morale` and `r.unrest` raise. `stores`/`sites`/`records`/`dates`/`stake`/`envelope` initialise
empty at `:520-522`.

### §1.2 The matter economy runs

`engine/season/loop/driver.py::matter` draws subsistence from each rung's larder (`:415-443`), credits
`yield` scaled by `Site.condition / condition_scale × season_factor` (`:444-476`), wears every Site
(`:479-497`) and emits `condition.band_crossed` on a real floor crossing (`:511-528`). The tables are
data: `site_yield` (`rosters.yaml:923-950` — harbour `{grain 40, salt 30}`, seam `{ore 50, timber 10}`,
body `{}`), `band_floors` (`:952-976` — harbour `{bulk_shipping 800, fishing 100}`, seam
`{deep_mining 700, surface_gleaning 50}`, body `{full_operations 800, limited 500, withdrawal_only
100}`), `subsistence_weight` `{grain: 2, salt: 1}` (`:703-719`), `matter_kinds`
`[grain, salt, timber, ore, coin]` (`:675-686`).

Two facts worth carrying. First, `site_yield`'s note is careful about what is invented and what is
not: the quantities are an injected default with row `H-93` and a three-point sweep
`[declared, uniform, none]`, **but the scaling is not invented** — a worn place produces less *without
a second wear concept*, and yield is keyed on the Site rather than the rung *"because the rung has no
quantity that could fall."* Second, `none` is declared as the control arm: with every cell zero the
economy has no source and every store depletes monotonically.

**Timber, ore and coin are stored and never eaten** (`rosters.yaml:713-716`) and nothing else consumes
them. Three dead matter kinds.

### §1.3 The population primitive is two objects, and the code has both declared and neither running

**The envelope.** `Rung.envelope` is declared (`carriers.py:510-511, 521`), matrix-registered at
`engine/season/write_matrix.yaml:287-293` —
`(Rung, envelope) · steps [MAT, CEN] · class MATTER · social false · by DR-1 · emits envelope.changed`
— and exercised by exactly one probe, `engine/season/harness/probes.py:1532-1544` (W9), which sets a
literal `[100, 200, 150, 60]`, adds 5 to index 0 through the gate at MATTER, and asserts 105. Layer 1
defines it as `Envelope := packed per-band counts` (`architecture/holonic_ARCHITECTURE.md:372`) and
rules:

> *"Births add weight at the youngest band; deaths remove it. **Birth is envelope weight, not a
> `create`.** The envelope is written at MATTER and reconciled at CENSUS. It has **no ledger, no
> stance and no act**. The cohort acts; the envelope does not. Conflating them produces a design in
> which demography can choose."* (`:401-406`)

§25 lists *"envelope weight | births and deaths"* as a MATTER write (`:860`) and *"bodies, ageing,
natural death | one of the three licensed clocks"* (`:854`); §30's matrix row has envelope weight
writable at MATTER and CENSUS (`:1040`). **Nothing in the loop writes or reads it.**
`driver.py:413` says so in the MATTER step's own words — *"BODIES AND TRAVEL ARE STILL NOT BUILT"* —
and `census()` at `driver.py:1371-1383` writes nothing and declares that it writes nothing.

**The cohort.** `Person.weight: int = 1` (`carriers.py:351`); `< 1` raises (`:382-383`); the class
docstring reads *"A COHORT IS A PERSON AT weight > 1. ONE CLASS"* (`:348`). Probe P21
(`probes.py:679-696`) runs a weight-40 crowd through the same `choose` and the same resolver. Matrix
row `(Person, weight) · [CEN] · MATTER · emits weight.changed` (`write_matrix.yaml:217-223`).
**No writer anywhere.** Two readers, both harness: `probes.py:119` (the `SUBSIST` divisor) and `:691`
(P21's branch).

### §1.4 `Faction` is a view, and the view resolver does not exist

Layer 1: `Faction := (proposition, members[], holdings[], seats[], head?)`, built at a barrier, owns
nothing, never `Act.actor`, never a `hold` subject (`architecture/meta/01_AXIOMS.md:1037-1051`;
`architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md:22-49`).
`architecture/meta/04_CODE_ARCHITECTURE.md:427` names the resolver: `faction_q.resolve(w, prop) ->
Faction`. **`engine/season/queries/` contains only `readers.py` and `world_q.py`**, and
`grep -rn "faction_q\|class Faction" engine/season --include=*.py` returns nothing. **The ratified
view has no resolver.**

What exists is its raw material: `commit` Tenures (`engine/season/harness/headless.py:81` seeds one by
hand), `hold` on Rungs as holdings (`engine/season/loop/predicates.py:59-70`, carrying Jordan's
"duchy in their holdings" ruling), and `Office.faction`/`Office.body` resolved at construction and
refused if unknown (`carriers.py:442-472`).

### §1.5 The lawful aggregate machinery exists and the aggregates do not

`engine/season/queries/world_q.py:47-69` — `parent_of`, `descendants` (iterative, with a visited set,
because the reference graph is cyclic on purpose), `r1_aggregate` (compute-on-demand over containment
descendants). `:71-87` `aggregate_guard`, the volunteered half. `:116-124` `commit_count_guard`, *"the
DETECTING half: it looks at the rows, not at a flag"*, raising on any ended edge in a sum. `:89-114`
`single_holder_counter`, which raises for want of the closed axis registry L3 clause 1 requires.
`:149-154` `presence`. `:157-253` `questions_for` — Q1 `date_due` · Q2 `claim_landed` · Q3
`band_crossed` · Q4 `need`.

**No function computes a commitment share, a population, a faction value or a compliance share.**

### §1.6 The verb table has 32 rows and six execute

`engine/season/requirements.yaml:196-206` (R-05): `create_record, move, speak, tell, transfer, utter`
execute; 20 carry no predicate and no effect; `work` is attempted and always refused.
`EFFECTS` (`engine/season/loop/effects.py:92-406`) defines ten: `confer, revoke, convene, move, work,
create_record, destroy_record, kill, utter, transfer`. **Any other verb with a non-empty `writes:`
raises `Unspecified` at `driver.py:856-865` — including `commit`** (`verb_table.yaml:97-111`, writes
`Tenure.since`) **and `repudiate`** (`:402-412`, writes `Tenure.until`).

Eligibility is `own · remit · hold · presence`, never `capability` (`rosters.yaml:131-143`;
`driver.py:662-679`). The operand vocabulary is closed on
`[actor, subject, from, to, site, kind, amount, floor]` (`rosters.yaml:868-881`), and its note says
that closure *"is what stops the grammar becoming a second resolver."* `requires_forms` is closed at
seven: `existence · scalar_threshold · contain_path · cardinality · relation · own_ledger · basis`.

### §1.7 Founding and building have matrix rows and no verbs

`(Rung, exists) · [RES] · ACTS · social true · emits rung.founded` (`write_matrix.yaml:294-300`,
`by:` cell *"W2/H-41 — founding a hearth"*); `(Site, exists) · [RES] · emits site.built` (`:322-328`).
**No verb writes either.** `F.20` / `H-41` (`hole_register.yaml:462-471`), `H-105` (`:1384-1393`), and
Layer 1's own summary: *"the world only decays — nothing is ever founded or built"*
(`04_CODE_ARCHITECTURE.md:61-62`).

### §1.8 The budget is scenes, and it already varies by office

`engine/season/decision.py:124-167` —
`budget = k + offices × budget_office_bonus − body_band_penalty − legs × budget_leg_penalty`, floored
at 1. `scene_budget = 5` (`engine/season/data/fixtures.py:171`, ruled by Jordan 2026-09-02);
`budget_office_bonus = 1` (`:348`). `deliberate` refuses an over-budget return rather than truncating
it (`driver.py:599-604`).

### §1.9 The corpus has exactly one settlement-scale case

`grep -rhoE "^\s*scale:\s*\S+" engine/season/cases | sort | uniq -c` → realm 48 · faction 47 ·
person 37 · world 10 · **settlement 1** · one malformed.

The one is **NPC-083, Hedda Kronvald** (`engine/season/cases/chain/NPC2.yaml:96-139`) — governor of a
five-adjacency chokepoint, whose seven `season_requires` are Goldenfurt's pillars verbatim (a bounded
budget; a method choice; a Directive answered comply/bargain/defy; Needs independent of the Directive;
durable marks surviving succession; actor-versus-actor conflict; a self-adjusting pressure) and whose
eighth row concedes that the whole thing *"is itself an unratified proposal explicitly gated on a
settlement registry that does not yet exist in the engine."*

**This is the acceptance case for everything in `02_` and `03_`.**

---

## §2 · Declared-but-dead, with the exact defect class

| item | declared at | reader / writer | defect class |
|---|---|---|---|
| `Rung.envelope` | `carriers.py:510-521`; `write_matrix.yaml:287-293` | writer: probe W9 only; reader: none | `ID-13` — a field no resolver consults |
| `Person.weight` | `carriers.py:351`; `write_matrix.yaml:217-223` | writer: none; readers: two probes | `ID-13`, **plus a false provenance cell** (§3.2) |
| `Person.beliefs` | `carriers.py:356`; `write_matrix.yaml:154-160` | Layer 1 ordered it deleted — *"A BELIEF IS NOT A FIELD. IT IS A `commit` TO AN `OUGHT`"* (`01_AXIOMS.md:786-799`) | code carries a field the ratified schema struck |
| `Rung.stake` | `carriers.py:510, 521` | §D.2 calls it *"RETIRED as a dead row"* (`01_AXIOMS.md:816-820`) | same |
| `Rung.judging_set_rule` | `carriers.py:511, 526` | Stage 4 §B.7 *"deletes `judging_set_rule` from `Rung`"* (`01_AXIOMS.md:827-831`); `world_q.judging_set` raises (`:145-147`) | same; `H-32` |
| `Rung.sites` | `carriers.py:521` | *"a BACK-REFERENCE NOTHING MAINTAINS — empty for every rung in the corpus"* (`driver.py:448-451`) | dead index; `Site.rung` is the maintained side |
| `urgency()` | `decision.py:288-307` | added identically to every candidate — *"INERT BY CONSTRUCTION"* (`:298-302`) | **subsistence cannot change any decision** (`H-73`) |
| Q3 `band_crossed` | `world_q.py:199-221` | fed only by Site crossings (`driver.py:511-523`); its referent is a **verb name**, so `opening_set` forms nothing (`world_q.py:298-299`) | a live question source that produces no candidate |
| `Sensation.standing` | `carriers.py:136-180`; `decision.py:692-713` | supplied by `standing_of`; read by nothing in `score()` (`decision.py:341-345`) | computed, unconsumed |
| MATTER's decision row | `driver.py:316-320` | lists *"larders, yield"* as `not_implemented` while `:406-476` implements both | a stale register row — the defect `:312-315` itself complains of, one revision later |

---

## §3 · Eight corrections to the brief that produced this set

Recorded rather than quietly dropped, because a synthesis that inherits a wrong premise propagates it.
Corrections 1–6 are the read-only analyst's, against the orchestrating session's brief; 7–8 are its
corrections to my own mid-course messages.

**§3.1 · "Four bands" is a probe literal, not a Layer 1 fact.** The four numbers are W9's
(`probes.py:1537`). Layer 1 says only *"packed per-band counts"* (`holonic:372`); it names no band
count, no band semantics and no transition rule. **Age bands** are
`proposals/2026-08-31-ideal-v2/01_ARCHITECTURE.md:595` (`counts_by_age_band[]`) — PROPOSED, not
ratified. Any band roster is therefore this set's to propose and Jordan's to rule.

**§3.2 · `Person.weight` is NOT read by the loop's subsistence draw, and the matrix says otherwise.**
True of the harness fixture `SUBSIST` (`probes.py:114-119`, self-declared *"INJECTED… a harness
fixture"*). **False of the loop:** the larder draw at `driver.py:425` is `wt * len(eaters)` — a head
count. **A cohort at weight 200 eats as one person in every corpus world.** Worse, the matrix row's
own `by:` cell (`write_matrix.yaml:222`) and `H-49` (`hole_register.yaml:560`) both justify the row
with *"H-11's subsistence default reads it ('scaled by weight'), so every season touches it"* — a
claim the driver falsifies.

⚠ **And the divergence runs in both directions, which is sharper than "two arithmetics" and is the
form to carry.** The larder computes `draw = {k: wt * len(eaters) for k, wt in weights.items()}`
(`driver.py:425`) — it **honours `subsistence_weight`** (grain 2, salt 1) and **ignores
`Person.weight`**. `SUBSIST` computes `sum(stores.values()) * scale // max(1, p.weight)`
(`probes.py:119`) — it **honours `Person.weight`** and **ignores `subsistence_weight`**, summing matter
kinds as if fungible, which is the model choice its own docstring says it may not make. **Each honours
exactly the term the other drops.** That is the `S` defect §0.06 names — *"calculations consistent in
methodology with other mechanics"* — live today, and P1 closes it by making the larder the single
owner of both terms.

⚠ **One qualification, because the driver's own comment is easy to misread as the defect.** The
comment above `:425` cites `H-11` as *"draw from the containing rung's stores, **scaled by weight**"*,
and **that "weight" is the matter kind's `subsistence_weight`, which the line does honour.** The
falsified claim is not the driver's; it is the **matrix row's `by:` cell and `H-49`**, which read the
same phrase as `Person.weight` in order to justify the `(Person, weight)` row's existence.

**§3.3 · The two trees are not disjoint; the disjointness is one-directional with one seam.**
`engine/season/seam.py:191-211` lazily imports `engine.autoload.dice_engine` for
`degree_from_net`/`DEGREE_LABEL` — **the shared degree ladder, which is the one thing `T-k` says lives
once**. `combat_seam.py` reaches `systems/combat/` by path
(`[GAP: `combat_seam.py` was not opened; this second seam is `requirements.yaml:99-103, 286`'s claim,
not a read]`). No legacy module imports `engine.season`.

**§3.4 · Reading 09 §2's revolt chain is broken at four links, not one.** The chain at
`architecture/meta/09_WORKED_EXAMPLES.md:97-99` is *bad harvest → subsistence crosses a floor → that
person has a question → among their candidates is `commit`*. Measured: **(a)** a shortfall emits
nothing (`driver.py:431-436` is a `TRACE.note`); **(b)** Q3 reads Site crossings only, and its
referent is a verb name (§2); **(c)** `urgency` is inert; **(d)** `commit` has no effect and raises.
Only *"somebody uttered the proposition"* works, because `utter` executes.

⚠ **This overturns a claim the orchestrating session made and would otherwise have carried into this
document as fact.** The mid-course message asserted that a falling `stores/weight` fires the `need`
question. It does not: **Q4 `need` fires on a live `commit`-to-OUGHT** (`world_q.py:223-231`), never
on subsistence. The loop the orchestrator described is the loop P1 and P5 exist to *build*; it is not
one that exists.

**§3.5 · "No designed amplifying loop" is nearly right and the sharper form is worse.** `H-102`
(`hole_register.yaml:1345-1357`) **is** designed and signed `+`, and its own `default:` cell reads
*"UNDER THIS INSTRUMENT'S OWN FIXTURES IT CANNOT AMPLIFY AT ALL"* (`:1352`). `H-112` (`:1520-1532`) is
a defect bounded by an `if`. `G13` (`engine/season/harness/register.py:316-356`) validates shape only,
and its clause 3 is a **presence check** — *"any non-`none` string passes"* (`:329-333`) — which it
declares, along with the fact that it **cannot see a loop nobody declared**. So the accurate statement
is **zero operative amplifying loops**, and the gate will not catch a fabricated bound.

**§3.6 · On the orchestrator's three code facts.** The economy nouns exist as claimed, with the
addition that timber, ore and coin have no consumer. The `SUBSIST` socket is ruled — `sense : (Person,
frozen_world, subsistence)` (`driver.py:161-169`) — **but the loop does not close**, per §3.4; and the
fungibility divergence is real: `SUBSIST` sums `stores.values()` and ignores the declared
`subsistence_weight`. On the two scalars: confirmed, and `standing_of` exists person-side
(`decision.py:692-713`), so the second scalar is **supplied, not raising**, at HEAD.

**§3.7 · `PLAN.md` is paused, not superseded, and §8.1:1989 forbids a per-container clock.**
Everything in `02_` that moves the envelope does so inside the **one MATTER step over all rungs**,
exactly as wear is applied over all Sites at `driver.py:482-497` — the licensed `bodies` clock, not a
container scheduling itself (`T-i`, `01_AXIOMS.md:396-398`).

**§3.8 · What survives of the orchestrator's framing.** The reframing was right on its central point
and wrong on its mechanism: a population primitive is **not** the gap — it is designed in two
independent lineages and agrees with ratified Layer 1 — and what is absent is the **dynamics, the
writers and the consumers**. The mechanism by which the dynamics would close the revolt chain was
misstated (§3.4) and is corrected here.

---

## §4 · What this means for the proposals

Four things follow, and they shape everything in `02_` and `03_`:

1. **Almost no vocabulary is missing.** The rung kinds, the title ladder, the matter kinds, the site
   kinds, the yield and band tables, the two population objects, the four question sources, the four
   eligibility kinds, the seven `requires` forms and the eight operands all exist. What is missing is
   **producers**: writers for declared rows, effects for declared verbs, and Queries for declared
   views.
2. **The refusal machinery is real and will do the work.** `Rung.__setattr__` raises on a social
   aggregate; the write gate refuses an unmarked cell and a wrong-step token; `commit_count_guard`
   raises on an ended edge in a sum; the loader refuses an unknown roster key. A proposal that tries
   to store unrest does not get reviewed — it does not run.
3. **The instrument's own defaults are honest about being defaults**, and that is the licensed form
   for every number in this set: `ID-6` — inject it, name the site, sweep three points — with
   `site_yield`'s `none` control arm as the worked example of a sweep whose control arm can actually
   break the claim.
4. **There is exactly one settlement-scale case to be right about**, and it already asks for
   Goldenfurt's seven pillars. ⚠ **Four are met, two are met in vocabulary only, and one is refused
   with a price** — the honest score, corrected downward by the adversarial pass from an initial
   "six of seven". That is the shape of the whole set.
