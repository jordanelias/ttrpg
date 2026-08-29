# 02 — Character generation: life paths, caste and heritage, beliefs and flaws

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) · v1 `02` (archived) ·
## canon: `systems/characters/character_generation_questionnaire_v30.md` (CANONICAL) ·
## `systems/factions/faction_politics_v30.md` (CANONICAL, PP-660) ·
## `systems/characters/conviction_taxonomy_v30.md` (PP-684) · `systems/npcs/character_canon_v30.md`
## (PROVISIONAL) · `systems/npcs/npc_relational_graph_v30.md` (PP-724) ·
## `systems/_architecture/campaign_architecture_v30.md` · `systems/overview/clock_registry_v30.md`
## Produces: entities of kind `person`, the `edge` entities that attach them, and their form
## Scope: change **A** (identity/form split, applied to people) and change **F** (caste, heritage,
## beliefs, virtues and flaws). The caste **gate** is `04`'s; presences are `07`'s; the Slate is `10`'s.
## Continues in: [`02_character_generation_part2.md`](02_character_generation_part2.md) — §§8–11

**Every number in this document is a shape proposal, not a ledger constant**, unless it is cited to
canon by `path:line` — in which case it is canon's number and this document neither owns nor may
change it. This document introduces **no new registry file, no new stored primitive, no new Tag
kind, no new Key type, and no in-play player verb.**

**This document is in two parts, in reading order** (`CLAUDE.md` §4): **part 1** — the problem, caste
and heritage, the stage ladder, the grant vocabulary, edges and Knots, beliefs, flaws (§§1–7).
**[Part 2](02_character_generation_part2.md)** — determinism and totality, the player-facing surface,
the module contracts and the property audit (§§8–11). Section numbers run continuously across both.

---

## Overrides

Per the suite's one hard rule (`00 §5.3`): listed, tiered, argued. A silent override is the corpus
disease this suite exists to stop.

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **C-1** | **The delta spec's own five-stage ladder** (`Origin · Childhood · Formation · Entry · Career`), and v1 `02 §2`'s four one-shot pipeline stages | this suite's own spec, beaten by **ratified canon** | `character_generation_questionnaire_v30.md` is **`## Status: CANONICAL`** (`:2`, accepted 2026-05-08) and already ships a four-stage life path — **Origin → Formation → Vocation → Catalyst** (`:43`, `:45`) — with a table naming exactly what each stage produces (`:55-58`). Re-deriving a fifth vocabulary beside it is `00 §1`'s under-distilled failure. **Canon's four are adopted verbatim.** §3.1 |
| **C-2** | **`traits.virtues`** in the person's form bucket (delta spec §2.1; `01 §1.1`) | this suite's own `01` | **Virtue is Conviction #12 of the thirteen** (`conviction_taxonomy_v30.md:40`, separated from Utility at `:49` and Warden at `:54`). A parallel virtue trait is a second object for one job, and a flat bonus on a person — the shape `01 §4.3` refuses. **Cut; `traits` ships `flaws` only.** §7 |
| **C-3** | v1 `02 §2.4`'s *"at least two edges, both carrying a `disposition` gauge"* | this suite's own v1, corrected by `01` | The gauge half is cut by `01 §7.3` (O-3): a stored NPC↔NPC disposition is an aggregate over edge strengths, and no aggregate is written. Generation attaches **PP-724 edges** and derives disposition. The *count* survives and rises. §5 |
| **C-4** | The person's normative form table in `01 §1.1` gains **`beliefs`** | this suite's own `01` | §6. A creed-Belief is a proposition a person holds, canon caps the active set, and dropping one is exactly a form transition. **Net field count is unchanged**: C-2 removes one member, this adds one. |
| **C-5** | **`faction_politics_v30 §3.3`'s halved public Renown and §3.4's `+1 Ob` Initiation Duty for Southern Einhir** (`:670-676`, `:679-690`) | **ratified canon** (CANONICAL, PP-660) — the strongest tier, so the strongest argument | Both are **modifiers on the actor**. A flat `Ob` shift is worth ~1.8× more to a small pool than a large one (`01 §6`), so canon's caste penalty is *harsher on the weak* — a competence tax a strong character buys out of; and a halved rate is multiplicative **and invisible**. **What canon protects — the stigmatised caste pushed off the visible path onto the covert one (`:677`) — is kept and made stronger**, re-expressed as an option-set difference: a different duty row, and public-deed candidates that do not reach the Slate absent a sponsor. §2.4 |

**Not overridden, deliberately — recorded because deciding *not* to override is also a decision.**
`faction_politics_v30 §3.2`'s **gating matrix** (`:655-668`) and **§3.5's Disposition seeds**
(`:692-721`) are adopted **whole**, because a gate on an option set and a seeded starting value are
already the shapes this suite argues for (§2.4 makes that case rather than asserting it). **PP-724's
six edge kinds** are adopted for `01 §7.2`'s reason: six period-grounded types with per-type semantics
and a decision log beat any taxonomy re-derived here. **Canon's Knot gate** (`01 §7.5`) is obeyed
including its cap — the alternative is a generator manufacturing Thread-constituted bindings the
Thread layer never sanctioned. **v1's bounded log-odds conditioning, entropy floor, determinism
substream and totality** are carried with their reasoning intact; what changes is that they run **once
per stage**, which makes the entropy floor *more* load-bearing (§3.5).

**Out of scope, and named so the seam is visible.** A general **epistemic layer** — machine-comparable
propositions held per agent with graded confidence and provenance, so two characters can disagree
about a fact of the world — is a **Phase-2 corpus item and is not designed here.** §6 ships only the
**creed-Belief** canon already names, and says where the seam is.

---

## 1. The problem, restated after the critique

v1 `02` satisfied four requirements — total, conditioned, non-uniform, deterministic — by drawing a
person **once**. Root cause 1a is that this makes a character an outcome rather than a history: two
people with the same drawn numbers are the same person, and nobody can *become* someone. Three
things change, and only three:

| | v1 | v2 |
|---|---|---|
| **shape** | one conditioned draw over a person space | a walk over **stages**, each conditioning the next |
| **where capability lives** | `identity.capability` — and identity was unwritable, so nobody advanced | `form.capability`, moved only by a declared transition (`01 §2`) — so a career **is** the mechanism |
| **what setting contributes** | nothing; caste, heritage, Church and Movement were absent | **identity** fields with a ratified gate elsewhere, and stage rows conditioned on them |

Everything else about v1 `02` was right and is carried. **Two claims this document will not make:**
that the generator *expresses* the setting (`00 §0.1`'s scope limit binds), and that canon supplies
more than it does — §2.2 records an axis the setting names and does not populate.

---

## 2. Identity: caste and heritage

### 2.1 Caste — three values, ratified, ascribed at birth

`identity.caste ∈ {northern_einhir, central_einhir, southern_einhir}`, read from canon, not defined
here (`systems/factions/faction_politics_v30.md:647-649`, CANONICAL, PP-660):

| value | canon says | `:line` |
|---|---|---|
| **Northern Einhir** | Varfell highlands, Hafenmark, Crown heartland; unstigmatised; **baseline low TS**; full Church penetration; the "default" cultural position | `:647` |
| **Central Einhir** | Valorsmark core, Hafenmark lowlands; unstigmatised; central cultural position | `:648` |
| **Southern Einhir** | Southernmost-adjacent territories; stigmatised; **higher baseline TS**; **lower Church penetration**; structurally excluded from the post-war settlement — economically suppressed, ethnically targeted by Church enforcement | `:649` |

**Caste is identity and is never written** (`01 §1.1`, normative) — not a modelling convenience: a
caste a person could change is not a caste. What is mutable is how institutions **treat** it, and that
lives in a registry where it can be read, argued with and reformed (§3.2's matrix, applied by `04`).
Canon already puts caste at creation and calls the choice structural, not a difficulty setting:
*"A Southern Einhir character facing the Crown is not playing a harder version of the same game — they
are playing a different game"* (`systems/_architecture/player_agency_v30.md:475`, `:484`).

### 2.2 Heritage — what canon supplies, and what it does not

`identity.heritage` is declared by `01 §1.1` as a field distinct from caste. **This document
populates it from canon and records that canon populates it thinly.** Measured, not recalled:
canon uses *"heritage"* as a **synonym for caste** in every person-level use found
(`canon/03_canonical_timeline.md:80`, `:144`; `faction_politics_v30:237`); Altonia is a **colonial
overlay, not a person-level lineage** — *"Altonian colonial administrative overlays, not indigenous
nations"* (`systems/world/worldbuilding_v30.md:213`) — and what canon names is institutional
*residue* (`03_canonical_timeline.md:144`) plus one foreign node, Schoenland
(`systems/settlements/settlement_layer_v30.md:435`). A grep over `systems/` and `canon/` for
*Altonian descent / heritage / residue / settler* returns one hit, and it is institutional.

**So heritage ships with two populated sources and no invented third:** the caste lineage canon names,
and `origin_node` where that node is foreign or Altonian-connected. **A fourth caste value or an
Altonian-descent category would be canon authorship, not design**, and this suite proposes no canon.
Recorded as a **WR-lane gap**, not filled: *is heritage a second axis, or caste's own name?* If the
same, `01 §1.1` should drop one field. The field is kept meanwhile because `01 §1.1` is normative and
lists both, and shipping one field where the substrate declares two is shape divergence.

### 2.3 Where the gate lives, and why it is published

**This document sets no caste gate.** The ratified matrix — twelve ladder rows × three castes
(`faction_politics_v30:655-668`) — is applied at **`pm.candidates`** (`04`), the eligibility gate and
therefore the only right place. `02`'s contribution is to make the matrix's *input* exist: a person
whose caste is a first-class immutable identity field, disclosed. Three canon shapes `04` will need,
cited so `04` does not re-derive them:

| shape | canon | why it matters to generation |
|---|---|---|
| the gate is **asymmetric by design**, not a penalty table | `:642` — *"the caste is reproduced through institutional design, not through individual intent"* | a generated Southern Einhir is not "weaker"; they are **routed** |
| **the Warden ladder is favourable to the most stigmatised caste** | `:667`, `:636` — *"the Wardens are, effectively, the resistance infrastructure for the caste system's victims"* | the TS baseline `02` seeds (§4) is *why*. The mechanism must express this, not merely permit it |
| **Riskbreakers and Niflhel are favoured or caste-blind** | `:663`, `:666` | covert paths are structurally open where overt advancement is structurally closed |

**Disclosure: the caste gate is the suite's one ruled exception** (`00 §6` principle 5; `01 §8`) — an
*input*, published in full, because a player must be able to see that a candidate was excluded on
caste. Concealing it would make the system's central injustice invisible, the opposite of the design
intent canon states.

*Emergent possibility lost if caste were form rather than identity, or the gate a modifier:* the
game's central social injustice becomes a difficulty slider, and the covert ladders lose their reason
to exist.

### 2.4 Caste is a **gate** and a **seed** — never a modifier (C-5)

Canon expresses caste four ways. **Two are the right shape and are adopted whole; two are the
leverage failure this suite rules out one level up, and are overridden.** Adopting all four because
they are ratified would import a defect the rest of the suite spends its arithmetic avoiding.

| canon mechanism | `:line` | verdict |
|---|---|---|
| **§3.2 rank-advancement gating** — `open / gated(named requirement) / closed(unless named exception)` | `:655-668` | **ADOPTED WHOLE.** A gate on an option set: it changes *which* rungs exist for this person, not how well they roll. `04` applies it verbatim |
| **§3.5 inner-circle Disposition floor** — starting Dispositions by caste (Central `+1`, Northern `+2` from the Southern column) | `:692-721` | **ADOPTED.** A starting value is a **seed**, not a modifier: deposited once at generation with provenance, then decayed and moved by play like any other deposit (`01 §5.1`) |
| **§3.4 Initiation Duty `+1 Ob` for Southern Einhir** | `:679-690` | **OVERRIDDEN** |
| **§3.3 Renown from public actions in Northern/Central territories halved** | `:670-676` | **OVERRIDDEN** |

**What the overridden two were protecting, and why it must survive.** Both encode something true and
central: the system's incentives push the stigmatised caste off the visible path onto the covert one
— canon says so in the same breath (`:677`, citing Gerik Strand's observation, and naming Warden,
Niflhel and RM as where they are driven). **That fact is not in dispute. The arithmetic is.**

- **`+1 Ob` is a flat obstacle shift on the actor's own roll**, worth systematically more to a small
  pool than a large one — `≈0.204σ` at pool 5 against `≈0.115σ` at pool 18 (`01 §6`; `01 §5.3`). So
  canon's caste penalty is ~**1.8× harsher on a weak character than a strong one**, inverting what a
  structural injustice should do: it becomes a *competence tax a strong character buys out of*.
  `01 §6` also reserves `derive_ob`'s `modifiers` for properties of the **target**, and caste is a
  property of the **actor** — the wrong argument slot as well as the wrong magnitude.
- **Halving a gain rate is multiplicative**, the same non-uniformity §3.5 rules out for conditioning,
  and it is **invisible**: a player never sees a rate they did not receive, failing the disclosure
  contract's *publish every input* half.

**The replacement protects canon's fact more strongly, not less.** Both become **option-set
differences** — where this suite puts every "the person changes what is available" (`01 §4.3`;
ED-IN-0201 clause 2):

| canon's effect | v2 shape | who owns it |
|---|---|---|
| Southern Initiation Duty is *harder* (`Ob 2 → Ob 3`) | the Southern candidate is offered a **different duty row** — the sponsored or covert route canon says they are pushed onto — whose obstacle `derive_ob` derives from **its own** target. Same odds arithmetic, a different thing to do | `04` (candidacy), `08` (the duty) |
| Southern public Renown *halved* | public-deed candidates **do not reach the Slate** at a Northern/Central place absent a sponsor; covert candidates do. The rate is untouched; **what is reachable** changes | `10` |

**This is harder on the player, not softer** — the test that it has not quietly softened the setting:
a halved rate can be ground out with volume, a route that is not offered cannot. And it is **legible**:
an unoffered route is disclosable under §2.3's ruled exception where a silently halved number is not.
What it loses is *granularity* — `+1 Ob` is a dial and a gate is not. A real cost, accepted, because
the dial is the part that misbehaves.

⚠ **Scope.** `02` owns the argument because `02` is where caste becomes a mechanical object; it does
**not** implement the replacement (the duty row is `04`/`08`'s, the Slate filter `10`'s). If either
declines, canon's version stands and this section is the record of why it should not.

### 2.5 Church of Solmund and the Restoration Movement — birth **biases**, it does not **gate**

Two canonical institutions reach a person at generation, by three routes. **None is a new
mechanism**; each composes on something `01` or `07` already owns.

| route | primitive | how caste enters | canon |
|---|---|---|---|
| **what you were taught is true** | `truth` gauge — canon's 0–5 oscillating meter, **5 = Solmund orthodoxy, 0 = Thread-truth acceptance**, which canon says *"varies by background"* | Northern full Church penetration; Southern lower (`:647`, `:649`) | `clock_registry_v30.md:71`; Origin derives *"starting Truth"* (`questionnaire:55`) |
| **what you can perceive** | `thread_sensitivity` gauge (`01 §5.2`; 0–100 hard cap) | Northern baseline low, Southern higher (`:647`, `:649`) | `clock_registry_v30.md:72`; Origin derives *"TS baseline"* (`:55`) |
| **who you already know inside them** | a PP-724 **edge** to a local post-holder, weighted by the birth place's `presences{}` (`07`) | institutional reach at a place is a presence level, not a person's caste — caste enters through *where people of that caste are born* | `01 §7.2`; `07 §4` |

**The Movement's affiliation bias is ratified and asymmetric**, and belongs in the conditioning
distribution rather than a branch: Northern **ideologically suspect** · Central **variable** ·
Southern **ideologically favoured — the RM's base is Southern Einhir** (`faction_politics_v30:668`).
The Church's is the mirror (`:660`), with one caste-neutral exception branch canon names.

**The worked case, and the reason §6 exists.** The Movement holds a proposition canon states is
**false** — *"RM does not believe threadwork is real. Threadwork is folklore to RM"*
(`systems/_architecture/campaign_architecture_v30.md:57`) — and canon states the revision with three
declared outcomes: **Embrace**, **Denial**, **Schism** (`:71-75`). Against this suite's primitives
that is not three special cases: it is one belief crossing a band, whose third outcome is **a bloc**
(`06 §3`). Generation's only job is to put the belief on the right people — which is §6.

---

## 3. The stage ladder

### 3.1 Four creation stages, adopted from canon; career stages continue them in play

```
   creation (age-gated, at world-gen or on demand)          in play
   ┌────────┐   ┌───────────┐   ┌──────────┐   ┌──────────┐  ┌──────────────┐
   │ Origin │──►│ Formation │──►│ Vocation │──►│ Catalyst │  │ Career ×N    │
   └────────┘   └───────────┘   └──────────┘   └──────────┘  └──────────────┘
    identity      capability      first post     the thing     one per N seasons
    is FIXED      + mentor        or trade       that changed  of holding a post
    here          edge                           everything
```

The four are canon's, verbatim (`character_generation_questionnaire_v30.md:45`), with canon's own
per-stage derivations (`:55-58`), reproduced because they are the contract this document composes on:

| stage | canon says it derives | `:line` |
|---|---|---|
| **Origin** | cultural template, **caste**, early Conviction seeding, **starting Truth**, **TS baseline**, **first Knot seed** | `:55` |
| **Formation** | Conviction weight calibration, skill direction, Self-Other initial setting, **second Knot seed** | `:56` |
| **Vocation** | History tag, skills, **Belief #1 generation**, content-access | `:57` |
| **Catalyst** | arc-initiating event, Goal, final Conviction calibration, **possible Scar** | `:58` |

**Career is the fifth and it is not a creation stage.** Canon's ladder ends at Catalyst — *"your story
begins"* (`:45`). A career stage is the same row shape walked **in play**, once per `N` seasons of
holding a post: the delta spec's requirement at **no new mechanism** (§3.4), and why 1a is fixed
rather than papered over.

*Emergent possibility lost if stages were cut and the draw made one-shot again:* two people with the
same numbers would be the same person, and nobody could become someone — in generation or in play.

### 3.2 A stage is two registry rows, in files that already exist

`00 §9` caps this suite at **two new registry files** and both are already declared. A stage adds
**rows, not files**, and it splits along exactly the line `00 §9.1` argues for — *vocabulary* versus
*catalogue*:

```yaml
# references/form_registry.yaml  — the transition (the fourth write leaf, 01 §2.2)
transition: stage.formation_to_vocation
entity_kind: person       field: life_stage
from: formation           to: vocation
gate: age_seasons >= AGE_VOCATION and life_stage == formation     # a GATE, never a roll
cost: []                  emits: form.transitioned
reversible: false         # nobody un-lives a stage; no hysteresis band is needed or allowed
class: substrate
```
```yaml
# references/content_registry.yaml — the catalogue: what this stage may grant
stage: stage.formation_to_vocation
conditioned_on: [caste, origin_node.form, prior_stage_output, faction.ethos]
grants:                    # every member is a leaf write; see §4 for the closed vocabulary
  capability:  {axes: 1..2, band: 1}
  conviction:  {reweight: 1}
  edge:        {kinds: [patronage, sworn-bond, rivalry], count: 1..2}
  flaw:        {p: conditioned, max: 1}
  belief:      {max: 1}
  knot_seed:   {candidates: 0..1}      # a CANDIDATE. Canon's gate decides. §5.2
  tag:         {kind: Precedent, count: 0..1}
```

**Why two rows and not one.** The transition is *how a person's shape may change*, so a single grep
answers "what can move a person's life stage"; the grant table is *what the world contains*. Merging
them puts a vocabulary and a catalogue in one file — the failure ED-IN-0200 names. **A stage row is
data**: adding a stage, a flaw or a belief proposition is a row, never a branch (`00 §6` principle 3),
and nothing in this design names a faction, a place or a person.

### 3.3 Age gates the stage count, and that is the whole of the age model

`identity.birth_season` is immutable; `form.life_stage` is not. Current age is
`season_now − birth_season`, **derived**, never stored — an age field would be an aggregate with a
setter, and no aggregate is ever written (`01 §2.1`).

A person generated *now* walks every stage whose gate their age satisfies, in order. A person
generated at a young age has walked two stages; one generated old has walked four plus several
career stages, **and the stages they walked are why their capability, edges and flaws look as they
do**. Nothing else in the design needs an age concept.

> `AGE_FORMATION`, `AGE_VOCATION`, `AGE_CATALYST` and `N` (career-stage period, seasons) are **shape
> proposals with no canon backing found**, declared in `form_registry.yaml` gates rather than buried.

**Reachability bar, both directions:** at the oldest generated age the world admits the career-stage
count must be **bounded**, or capability ratchets without limit and an old NPC is unbeatable by
construction; at the youngest, at least **two** stages must have been walked, or a young person is an
unconditioned draw and §3.1's argument evaporates for exactly the population the world makes most of.

### 3.4 Career advance in play is the **same module**, not a second one

The elegance test (`00 §1`, under-distilled: *two objects doing one job*) refuses a `cg.career`
module. There is one stage walker, `cg.stage` (part 2 §10), with two callers: **`cg.demand`'s generation
loop** when a person is created (gate: age), and **the accounting boundary** when a person has held a
post for `N` seasons (gate: age **and** service). Both run the identical registry row, take the
identical form transition and emit the identical `form.transitioned` Key, so the Slate ranks them
identically. **A promotion and a backstory are the same object seen at different times** — the
strongest form of `00 §6` principle 8 this suite can offer for people.

⚠ **This reads state at the boundary; it is not a scheduled reaction.** `01 part 2 §9.3` (**J-N**):
the substrate has **no cross-season emission carry** — `next_tick` raises on a non-empty queue. A
career stage fires because the person **is** `N` seasons into a post at the boundary, never because
something was posted earlier. If J-N rules for reactive chains, this paragraph is what to revisit.

### 3.5 Conditioning runs once per stage — v1's arithmetic, carried

v1 `02 §2.2`'s condition-then-reify pipeline is unchanged in substance and now **layered**: stage
`k`'s output is part of stage `k+1`'s conditioning input. Both bounds survive and matter more, because
conditioning now applies four-plus times instead of once:

```
logit_i = logit(prior_i) + clamp( Σ_c w_c · signal_c(i), −Δ_MAX, +Δ_MAX )      # bounded log-odds
p_i     = softmax(logit)_i
p'_i    = (1 − ε)·p_i + ε/n          ⇒  p'_i ≥ p_floor for every i             # entropy floor
```

**Additive log-odds, not multiplicative factors**, for the reason `01 §5.3` keeps budget out of the
pool: a multiplicative factor is worth far more to an already-likely category than to a tail one, so a
unit of conditioning would not move the distribution by a consistent amount — the kernel's
non-uniformity, appearing in a categorical draw.

**The entropy floor is the load-bearing one under layering, and its bar is now stricter.** Composing
`S` conditioning steps composes the drift; without a floor applied **at every stage**, a person from
an extreme place converges to a single archetype by Vocation and every Southern frontier character is
the same character — which reads as authored, the exact failure conditioning exists to avoid.

> **Reachability bar (per stage, not per person):** at the map's most extreme node, after **all**
> stages, every conviction, flaw and belief the catalogue admits must still have probability
> `≥ p_floor`. `Δ_MAX` and `p_floor` are **shape proposals**, declared in the exported params.
>
> **Falsifier.** An arithmetic test, no campaign run: drive every conditioning signal to its extreme,
> walk the full stage ladder, and assert the terminal distribution's minimum is `≥ p_floor` and its
> entropy is above a declared floor. If it is not, layering has eaten the entropy floor and §3.5 is
> wrong. Load-bearing on the game: the difference between a population and a cast of one.

---

## 4. What a stage may grant — a closed vocabulary of leaf writes

**Every grant terminates at one of `01 §2.1`'s four write leaves. There is no fifth.** This table is
the whole interface between a stage row and the substrate, and it is deliberately short.

| grant | leaf | bound | notes |
|---|---|---|---|
| **capability** | 4 — form transition on `form.capability` | one axis by at most one band per stage; clamped to `descriptors.ATTRIBUTE_FLOOR…CEILING` | **ratchets, never decays** (`01 §1.3`). **No attribute is named literally anywhere in this document** — the roster is nine with a ruled, unnamed tenth (`01 §1.2`), and a person gains it by regeneration |
| **conviction reweight** | 4 — form transition | one conviction per stage; weights sum into the registry's declared concentration band | names resolve through `descriptors.resolve_conviction`, which **raises** on an unknown name (`01 §1.2`). **No conviction is named literally either** |
| **edge** | entity creation + 2 | 1–2 per stage, kinds from PP-724's six (§5.1) | endpoints ordered where the kind is asymmetric |
| **flaw** | 4 — form transition on `form.traits.flaws` | at most one per stage | §7 |
| **belief** | 4 — form transition on `form.beliefs` | active set ≤ 3, by canon | §6 |
| **precedent tag** | 2 — tag append | provenance required, non-empty | what the person *did*, not what they are |
| **knot candidate** | nothing — it is a **proposal to canon's gate** | ≤ 2 across the whole creation ladder | §5.2. Generation never writes a Knot |
| **gauge seed** (`truth`, `thread_sensitivity`, `standing`, `exposure`) | 1 — gauge deposit | provenance required | the deposit's provenance is the stage's `form.transitioned` Key |

**Every granted field must be load-bearing on at least one resolution branch, and its consuming
module is named before it is added.** Carried from v1 `02 §2.3` — the gate that stops a generator
becoming a characterisation engine, since a field nobody reads gets cited as flavour and never changes
an outcome. Consumers: capability is the pool of every roll (`01 §6`); convictions rank a post-holder's
option set (`05 §3`); edges are read by appointment, patronage, succession and defection; flaws emit
candidates (`10`); beliefs gate what a person will argue and can be argued out of (§6); TS gates Knot
formation and the Warden ladder (`01 §7.5`; `faction_politics_v30:667`); Truth is canon's piety meter.

---

## 5. Edges and Knots at generation

### 5.1 Six edge kinds, adopted from PP-724 — v1's enum is cut

`01 §7.2` cut v1's six-member `relation` enum and this suite's own draft table, superseded by
`systems/npcs/npc_relational_graph_v30.md` (PP-724, Class A, PROVISIONAL): six canonical NPC↔NPC
edge types with per-type formation, strain, break and decay rules and a decision log (`:46-56`) —
`sworn-bond` · `liege-vassal` · `kinship` · `patronage` · `rivalry` · `feud`, strengths 1–3.
**Generation adopts them and adds nothing.**

**A person is born owing someone something, and leaves generation entangled.** v1 required at least
two edges (one upward, one lateral) and was right; v2 requires **one edge per walked stage** — at
least four for a full ladder — mapped to what canon says each stage produces:

| stage | edge canon names | kind |
|---|---|---|
| Origin | *"family situation, first relationship"* (`questionnaire:55`) | `kinship`, plus a second where the family is a household with a head |
| Formation | *"mentor/teacher"* (`:56`) | `patronage` — the mentor is the patron; ordered, so read from the other end it *is* the client relation (`01 §7.2` refuses a `client` row) |
| Vocation | *"what you do"* — a trade, a post, a chapter | `liege-vassal`, a second `patronage`, a peer `sworn-bond`, or a `rivalry` where the draw put two people on one rung |
| Catalyst | *"what changed everything"* (`:58`) | `rivalry`, or `feud` where the stage's precedent tag names a lineage |

**Disposition is stored for PC↔NPC and derived for NPC↔NPC** (`01 §7.3`, PP-724 `:331-345`), so a
generated NPC↔NPC pair gets **no disposition gauge** — C-3, which removes a stored aggregate the write
rule forbade. **Rivalries and feuds are escalation tracks, not strain tracks** (`:674`): a generated
rivalry is not a weak feud, and a stage grants either, never one as a magnitude of the other.
**Kinship does not break by strain** (`:334-340`) — a generated family survives estrangement, which is
why the Origin edge still matters at Catalyst.

### 5.2 Knots: generation proposes, canon disposes

Canon seeds Knots at creation — *"first Knot seed"* at Origin, *"second Knot seed"* at Formation
(`questionnaire:55-56`) — so a generated character **can** leave with more than one. But a Knot is
Thread-constituted and **is not one of PP-724's six** (`01 §7.5`); ED-POL-11 forbids conflating it
with patronage (`faction_politics_v30:1093`, cited at `01 §7.1` R-1). So:

> **A stage grants a knot *candidate*, never a Knot. The candidate is submitted to canon's own
> formation gate (`01 §7.5`, reading `systems/fieldwork/knots_v30.md`) and canon decides.** Every
> gate — Disposition, TS, capacity, uniqueness, Bonds — and the formation roll and its degree ladder
> are canon's, cited by `01`, invented by nobody here.

Three consequences, and the second is the interesting one:

1. **The cap is canon's and needs no counter.** `floor(Bonds/2) + 1` (`01 §7.5`, `knots_v30.md:70`)
   is a **gate counting the person's `knot` edges** — no stored count, nothing to drift.
2. **Most generated people leave with no Knot, and *which* people do is caste-legible.** Canon's gate
   requires Thread contact; canon says TS is *"0 for non-practitioners"* (`clock_registry_v30.md:72`)
   with a **higher baseline in Southern Einhir populations** (`faction_politics_v30:649`, `:667`).
   Nothing here arranges that — it falls out of two ratified facts meeting, which is what change F was
   for: **the caste system is legible in who has Knots at all**, and that is also why the Warden ladder
   is open to the caste the rest of the system closes.
3. **A candidate that fails the gate is not discarded** — the fallback is a strong PP-724 edge. Someone
   who *could not* form a Knot with the person who mattered to them at fifteen has a `sworn-bond` and a
   Precedent tag instead: a better character than a silently-dropped seed, at one line in the row.

*Emergent possibility lost if knot candidates were cut from generation:* every Knot in the game
would be one the player made in play, so the Thread layer would arrive at the start of the campaign
with no history and nobody would have already lost one.

---

## 6. Beliefs — what a person thinks is true, and how it is contested

### 6.1 Beliefs are not Convictions, and canon keeps them apart

**Convictions are what a person values; beliefs are what they think is true.** Canon carries both and
does not merge them: the thirteen-Conviction taxonomy is one object (`conviction_taxonomy_v30.md`,
PP-684); a Belief is another — *"Per-NPC sheets carry 1–3 Beliefs as first-person quoted strings"*
(`systems/npcs/character_canon_v30.md` §6.1) with its own revision rule at §6.2 (`:192`). ⚠ **Tier,
stated honestly:** that file is **`## Status: PROVISIONAL — pending ratification`** (`:6`) — the best
statement of the belief object in the tree, composed on here, but not ratified.

**A measured tree fact that makes this section necessary rather than decorative.** The belief object
already exists in code and **nothing produces it**: `beliefs.add_belief` has no callers,
`beliefs.revise_belief` is uncalled (`systems/characters/characters_flow_skeleton_v1.md:30-31`), and
`create_world` leaves `convictions`/`beliefs` as empty dicts *"not populated during world-gen"*
(`:92`). **The missing producer is character generation.** That is the gap `02` closes.

### 6.2 The composition — no new primitive, no new tag kind

| part | primitive | leaf |
|---|---|---|
| **which propositions this person holds** — the active set, `≤ 3` | `form.beliefs` on the person (C-4) | 4 — form transition |
| **how firmly** | a `credence.<proposition>` **Gauge** per held proposition, declared on a bounded **0–5** scale (part 2 §10.1) | 1 — gauge deposit, provenance required |
| **what the proposition is** | a **row** in `references/content_registry.yaml` | data, not a branch |
| **what happens when one is given up** | a `Precedent` **Tag** — canon's Scar | 2 — tag append |

**Why a Gauge and not a Tag.** `01 §3.1` closes the Tag enum at six and demands a two-part argument
for a seventh; this design **does not open it**. A belief needs the two things a Tag lacks and a Gauge
has: a **rest value** — the prior the person's origin supplies, so an unreinforced belief drifts back
toward what their caste, place and institution ambiently teach — and **geometric decay toward it**
(`01 §5.1`). Right dynamics for conviction in a proposition; wrong dynamics for salience of a memory.

**Why the gauge-count objection does not apply, though it killed gauge-per-memory.** `01 §3.2` refused
a Gauge per Memory because the count grows with everything anyone ever saw. **Beliefs are capped at
three per person by canon**, not by a parameter this document chose. A cited bound versus an unbounded
ramp is the whole argument — and if the cap moves, this decision is re-examined, not tuned.

**Canon's own precedent for the shape.** The `truth` track is already a 0–5 oscillating gauge whose
poles are two competing accounts of what is true — *"5 = Solmund orthodoxy, 0 = Thread-truth
acceptance"* — that *"varies by background"*, players seeing *"qualitative bands only"*
(`clock_registry_v30.md:71`). A belief gauge is that shape over a registry of propositions.

### 6.3 Revision — canon owns *when*, this document owns *where it is stored*

`character_canon_v30 §6.2` states three **conjunctive** conditions for revision — a decisive contest
outcome against the holder; the winning argument used their primary or secondary Resonant Style; the
argument **specifically engaged the Belief** — then *"Old Belief → permanent Scar. New Belief forms."*
**This document does not redesign or weaken that.** The mapping is one line:

> Canon's three conditions are the **gate on a revising-magnitude deposit**. The gauge's declared
> band fires the **form transition** that drops the proposition and appends the Precedent tag.
> Ordinary evidence deposits move credence and fire nothing.

Two properties follow that a bare flag lacks. **A belief can be worn down and still held** — credence
below the band is a person losing an argument over seasons, the state this setting is full of. And
**the transition is a gate, never a roll** (`01 §2.2`): the uncertainty was in the contests that moved
the gauge, and re-rolling at the threshold charges for it twice.

**Reversibility.** Dropping a proposition is `reversible: false` — canon makes the old Belief a
permanent Scar, and coming to hold the *same* proposition later is a **new** row with a new provenance
chain and the Scar still on the sheet. **No hysteresis band is permitted**: there is no reversible
pair (`01 §2.3`). ⚠ One objection recorded and not resolved, because it is an NPC-lane call: canon
scars **every** revision, so changing your mind on good evidence counts the same as being broken.

### 6.4 The worked case, end to end

The Movement's *"threadwork is folklore"* (`campaign_architecture_v30.md:57`) is one content-registry
row. A generated Movement-affiliated person holds it with a `rest` set by their origin's presences.
Thread phenomena become publicly visible; evidence deposits accumulate; canon's three outcomes
(`:71-75`) are not three branches but three reachable states of the same objects:

| canon outcome | what the substrate does | owner |
|---|---|---|
| **Embrace** | credence crosses the band → transition drops the proposition, Precedent tag appended, a new proposition enters the active set | this document |
| **Denial** | credence stays above the band under sustained pressure — the person is visibly, mechanically wrong, and the world can read it | this document |
| **Schism** | the faction's post-holders' credences split; the movement's `divergence` rises; a **bloc** forms | `06 §2`, `06 §3` |

**No branch names the Restoration Movement** — `00 §6` principle 2 satisfied on the case most likely
to tempt a special case.

*Emergent possibility lost if beliefs were cut:* nobody could be **persuaded** — only outfought,
outvoted or outbid — and an institution founded on a false premise could never discover it.

**Out of scope, stated once.** A general epistemic layer — machine-comparable propositions held per
agent with graded confidence and provenance, so two characters can *compare* what they believe — is a
Phase-2 corpus item, not designed here. §6 ships the creed-Belief canon already names. If that layer
lands, `credence` and its confidence field are candidates to be **one field**, and the right outcome
is a cut, not a synthesis keeping both.

---

## 7. Flaws — and why there are no virtues

### 7.1 Virtues are cut (C-2)

**Virtue is Conviction #12 of the thirteen** (`conviction_taxonomy_v30.md:40`). A virtuous person is
one with a high Virtue weight plus the Precedent tags recording what they actually did. A parallel
`virtues` trait list is a second object doing that job — `00 §1`'s under-distilled failure — and worse,
a **flat bonus attached to a person**, the shape `01 §4.3` refuses because a flat shift is worth
systematically more to a small pool than a large one. **`traits` ships `flaws` only**, and `01 §1.1`'s
schema should drop the `virtues` member unless another document populates it.

### 7.2 A flaw declares when it binds, and it must open something

Canon has no formal flaw mechanic but has the **shape**, authored per NPC:
`systems/npcs/npc_roster_v30.md:165-173` ships a table whose columns are **Compromise · AI Flaw ·
Key Consequence** — the condition, the bias, and what it costs *and buys*. One row is the whole
argument: *"PROCEDURALIST (slow) → Investigations +1 season **but Overwhelming**"* (`:170`). A flaw
is a different way of doing the job, not a subtraction from it.

```yaml
flaw: <id>                        # a row in references/content_registry.yaml
granted_by: [<stage row>, <scar>] # a life-path stage, or a Conviction Scar taken in play
binds_when: <predicate over gauges, tags, form and the situation>   # canon's "Compromise" column
emits_candidate: <candidate kind>          # what SITUATION arrives when it binds
opens: <candidate kind>                    # what becomes reachable that otherwise is not
challenge: <transition id>                 # the row that retires or tempers it
class: substrate
```

**Three rules, and the third is the one that keeps the design honest.**

1. **A flaw touches neither the option set nor the odds.** Not a remit filter — that breaks
   ED-IN-0201 clause 2, which says the person shapes *which* action from the **same** option set with
   the same information (`00 §5`, `01 §4.3`). Not a modifier — `01 §6` keeps modifiers in σ-space and
   reserves them for properties of the *target*. **A flaw emits a candidate**: when its predicate
   holds, a situation arrives. That is `00 §2.3` point 3 — new objects add situations, not verbs —
   and it is why this document adds **zero player verbs**.
2. **A flaw that only subtracts is a debuff, not play.** Every row declares `opens` as well as
   `emits_candidate` or it does not ship, with the reachability bar: **the `opens` candidate must be
   reachable in a seeded campaign**, or the flaw is a penalty wearing a costume.
3. **A flaw is challengeable, and challenging it is a scene, not a purchase.** `challenge` names a
   form transition gated on a **resolved scene outcome**, never a spend. Passing tempers or retires
   the trait and emits `form.transitioned`, so the world notices this person is not who they were.

**Where flaws come from.** A stage row (§4) or a Conviction Scar taken in play — canon's Catalyst
stage already produces a *"possible starting Scar"* (`questionnaire:58`) and canon's Scar ladder
(`character_canon_v30 §6.3`) escalates them. Generation seeds; play accumulates; the challenge
transition is the only way down.

*Emergent possibility lost if flaws were cut:* nobody could be **reliably** wrong in a way another
actor can anticipate and exploit, so there would be nothing to know about a person that is worth
knowing.

---
