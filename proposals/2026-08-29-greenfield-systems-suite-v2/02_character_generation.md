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

**Every number in this document is a shape proposal, not a ledger constant**, unless it is cited to
canon by `path:line` — in which case it is canon's number and this document neither owns nor may
change it. This document introduces **no new registry file, no new stored primitive, no new Tag
kind, no new Key type, and no in-play player verb.**

---

## Overrides

Per the suite's one hard rule (`00 §5.3`): listed, tiered, argued. A silent override is the corpus
disease this suite exists to stop.

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **C-1** | **The delta spec's own five-stage ladder** (`Origin · Childhood · Formation · Entry · Career`), and v1 `02 §2`'s four one-shot pipeline stages | this suite's own spec, beaten by **ratified canon** | `systems/characters/character_generation_questionnaire_v30.md` is **`## Status: CANONICAL`** (`:2`, direction accepted 2026-05-08) and already ships a four-stage life path — **Origin → Formation → Vocation → Catalyst** (`:43`, `:45`) — with a per-stage derivation table naming exactly what each stage produces (`:55-58`). Re-deriving a fifth-stage vocabulary beside it is `00 §1`'s under-distilled failure: two objects doing one job. **Canon's four are adopted verbatim as the creation ladder.** §3.1 |
| **C-2** | **`traits.virtues`** in the person's form bucket (delta spec §2.1; `01 §1.1`) | this suite's own `01` | **Virtue is Conviction #12 of the thirteen** (`systems/characters/conviction_taxonomy_v30.md:40`; the taxonomy separates it from Utility at `:49` and from Warden at `:54`). A parallel virtue trait is a second object for one job, and it would be a flat bonus on a person — the shape `01 §4.3` refuses. **Cut. `traits` ships `flaws` only.** §7 |
| **C-3** | v1 `02 §2.4`'s *"at least two edges, both carrying a `disposition` gauge"* | this suite's own v1, corrected by `01` | The gauge half is already cut by `01 §7.3` (O-3): a stored NPC↔NPC disposition is an aggregate over edge strengths and no aggregate is ever written. Generation now attaches **PP-724 edges** with per-kind semantics and derives disposition. The *count* survives and rises. §5 |
| **C-4** | The person's normative form table in `01 §1.1` gains **`beliefs`** | this suite's own `01` | §6. A creed-Belief is a proposition a person holds, canon caps the active set, and dropping one is exactly a form transition. **Net field count is unchanged**: C-2 removes one member, this adds one. |

**Not overridden, deliberately.** The **caste × ladder gating matrix** (`faction_politics_v30 §3.2`,
`:655-668`, CANONICAL) is **cited and handed to `04`**, not restated with adjustments. **PP-724's six
edge kinds** are adopted as `01 §7.2` adopted them. **Canon's Knot gate** (`01 §7.5`, reading
`systems/fieldwork/knots_v30.md`) is obeyed, including its cap; generation may not bypass it. **v1
`02`'s bounded log-odds conditioning, entropy floor, determinism substream and totality property**
are carried with their reasoning intact (`00 §... delta §9` items 1 and 4 in spirit), because the
critique did not touch them — what changes is that they run **once per stage** instead of once.

**Out of scope, and named so the seam is visible.** A general **epistemic layer** — machine-comparable
propositions held per agent with graded confidence and provenance, so two characters can disagree
about a fact of the world — is a **Phase-2 corpus item and is not designed here.** §6 ships only the
**creed-Belief** canon already names, and says where the seam is.

---

## 1. The problem, restated after the critique

v1 `02` satisfied four requirements — total, conditioned, non-uniform, deterministic — and it did so
by drawing a person **once**. The critique's root cause 1a is that this makes a character an
outcome rather than a history: two people with the same drawn numbers are the same person, and
nobody can *become* someone, in generation or in play.

Three things change, and only three:

| | v1 | v2 |
|---|---|---|
| **shape** | one conditioned draw over a person space | a walk over **stages**, each conditioning the next |
| **where capability lives** | `identity.capability` — and identity was unwritable, so nobody advanced | `form.capability`, moved only by a declared transition (`01 §2`) — so a career **is** the mechanism |
| **what setting contributes** | nothing; caste, heritage, Church and Movement were absent | **identity** fields with a ratified gate elsewhere, and stage rows conditioned on them |

Everything else about v1 `02` was right and is carried.

**Two claims this document will not make.** It does not claim the generator *expresses* the setting —
`00 §0.1`'s scope limit binds here. And it does not claim canon supplies more than it does: §2.2
records, plainly, an axis the setting names and does not populate.

---

## 2. Identity: caste and heritage

### 2.1 Caste — three values, ratified, ascribed at birth

`identity.caste ∈ {northern_einhir, central_einhir, southern_einhir}`, read from canon, not defined
here (`systems/factions/faction_politics_v30.md:647-649`, CANONICAL, PP-660):

| value | canon says | `:line` |
|---|---|---|
| **Northern Einhir** | Varfell highlands, Hafenmark, Crown heartland; unstigmatised; **baseline low TS**; full Church penetration; the "default" cultural position | `:647` |
| **Central Einhir** | Valorsmark core, Hafenmark lowlands; unstigmatised; central cultural position | `:648` |
| **Southern Einhir** | Southernmost-adjacent territories; stigmatised; **higher baseline TS**; **lower Church penetration**; structurally excluded from the post-war settlement — economically suppressed, culturally pressured, ethnically targeted by Church enforcement | `:649` |

**Caste is identity and is never written** (`01 §1.1`, normative). That is not a modelling
convenience: a caste a person could change is not a caste. What is mutable is how institutions
**treat** it, and that lives in a registry where it can be read, argued with and reformed —
`faction_politics_v30 §3.2`'s matrix, which `04` applies.

Canon already puts caste at character creation and calls the choice structural, not a difficulty
setting: *"A Southern Einhir character facing the Crown is not playing a harder version of the same
game — they are playing a different game"* (`systems/_architecture/player_agency_v30.md:475`, `:484`).

### 2.2 Heritage — what canon supplies, and what it does not

`identity.heritage` is declared by `01 §1.1` as a field distinct from caste. **This document
populates it from canon and records that canon populates it thinly.** Measured, not recalled:

- Canon uses *"heritage"* as a **synonym for caste** in every person-level use found
  (`canon/03_canonical_timeline.md:80` *"Northern Einhir heritage"*; `:144` *"Southern Einhir
  heritage"*; `faction_politics_v30:237` *"Northern Einhir heritage"*).
- **Altonia is a colonial overlay, not a person-level lineage.** The three provinces are *"Altonian
  colonial administrative overlays, not indigenous nations"* (`systems/world/worldbuilding_v30.md:213`),
  and what canon names is **residue to be expelled** at the *institutional* level (`canon/03_canonical_timeline.md:144`)
  plus one foreign node, Schoenland (`systems/settlements/settlement_layer_v30.md:435`).
- **No canonical Altonian-descended person category exists.** A grep over `systems/` and `canon/` for
  *Altonian descent / heritage / residue / settler* returns exactly one hit, and it is
  institutional, not personal.

**So heritage ships as a lineage field with two populated sources and no invented third:** the caste
lineage canon already names, and `origin_node` where that node is foreign or Altonian-connected. **A
fourth caste value or an Altonian-descent category would be canon authorship, not design**, and this
suite proposes no canon. Recorded as a **WR-lane gap**, not filled: *is heritage a second axis, or is
it caste's own name?* If it is the same axis, `01 §1.1` should drop one field.

⚠ **The field is kept anyway, and the reason is not tidiness.** `01 §1.1` is normative and lists
both; a document that quietly ships one field where the substrate declares two is the shape
divergence this suite claims immunity to. The honest move is the field plus the gap.

### 2.3 Where the gate lives, and why it is published

**This document sets no caste modifier and no caste gate.** The ratified matrix — twelve ladder rows
× three castes (`faction_politics_v30:655-668`) — is applied at **`pm.candidates`** (`04`), which is
the eligibility gate and therefore the right and only place. `02`'s contribution is to make the
matrix's *input* exist: a person whose caste is a first-class immutable identity field, disclosed.

Three canon shapes `04` will need, cited here so `04` does not re-derive them:

| shape | canon | why it matters to generation |
|---|---|---|
| the gate is **asymmetric by design**, not a penalty table | `:642` — *"the caste is reproduced through institutional design, not through individual intent"* | a generated Southern Einhir is not "weaker"; they are **routed** |
| **the Warden ladder is favourable to the most stigmatised caste** | `:667`, `:636` — *"the Wardens are, effectively, the resistance infrastructure for the caste system's victims"* | the TS baseline `02` seeds (§4) is *why*. The mechanism must express this, not merely permit it |
| **Riskbreakers and Niflhel are favoured or caste-blind** | `:663`, `:666` | covert paths are structurally open where overt advancement is structurally closed |

**Disclosure: the caste gate is the suite's one ruled exception** (`00 §6` principle 5; `01 §8`). It
is an *input*, published in full — a player must be able to see that a candidate was excluded on
caste. Concealing it would make the system's central injustice invisible, which is the opposite of
the design intent canon states.

*Emergent possibility lost if caste were form rather than identity, or if the gate were a modifier:*
the game's central social injustice becomes a difficulty slider, and the covert ladders lose the
reason they exist.

### 2.4 Church of Solmund and the Restoration Movement — birth **biases**, it does not **gate**

Two canonical institutions reach a person at generation, and they reach them by three different
routes. **None of the three is a new mechanism**; each is a composition on something `01` or `07`
already owns.

| route | primitive | how caste enters | canon |
|---|---|---|---|
| **what you were taught is true** | `truth` gauge — canon's own 0–5 oscillating meter, **5 = Solmund orthodoxy, 0 = Thread-truth acceptance**, and canon says it *"varies by background"* | Northern = full Church penetration; Southern = lower Church penetration (`:647`, `:649`) | `systems/overview/clock_registry_v30.md:71`; the Origin stage derives *"starting Truth"* (`questionnaire:55`) |
| **what you can perceive** | `thread_sensitivity` gauge (`01 §5.2`; 0–100 hard cap) | Northern baseline low, Southern baseline higher (`:647`, `:649`) | `clock_registry_v30.md:72`; Origin derives *"TS baseline"* (`questionnaire:55`) |
| **who you already know inside them** | a PP-724 **edge** to a local post-holder, weighted by the birth place's `presences{}` (`07`) | the Church's and the Movement's reach at a place is a presence level, not a person's caste — caste enters through *where people of that caste are born* | `01 §7.2`; `07 §4` |

**The Movement's affiliation bias is ratified and asymmetric**, and it belongs in the conditioning
distribution rather than in a branch: Northern Einhir **ideologically suspect** · Central
**variable** · Southern **ideologically favoured — the RM's base is Southern Einhir**
(`faction_politics_v30:668`). The Church's is the mirror (`:660`), with one caste-neutral exception
branch canon names explicitly.

**The worked case, and it is the reason §6 exists.** The Movement holds a proposition that canon
states is **false**: *"RM does not believe threadwork is real. Threadwork is folklore to RM"*
(`systems/_architecture/campaign_architecture_v30.md:57`) — and canon states the revision, with
three declared outcomes: **Embrace** (integrate), **Denial** (hold and be disadvantaged), **Schism**
(the movement splits) (`:71-75`). Read against this suite's primitives that is not three special
cases. It is one belief crossing a band, and its third outcome is **a bloc** (`06 §3`). Generation's
only job is to make the belief exist on the right people — which is §6.

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
| **Vocation** | History tag, skills, **Belief #1 generation**, content-access assignment | `:57` |
| **Catalyst** | arc-initiating event, Goal, final Conviction calibration, **possible starting Scar** | `:58` |

**Career is the fifth and it is not a creation stage.** Canon's ladder ends at Catalyst — *"your
story begins"* (`:45`). A career stage is the same row shape walked **in play**, once per `N`
seasons of holding a post. That is the delta spec's requirement satisfied at **no new mechanism**
(§3.4), and it is why 1a is fixed rather than papered over.

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

**Why two rows and not one.** The transition is *how a person's shape may change* and belongs with
every other transition, where a single grep answers "what can move a person's life stage". The grant
table is *what the world contains* and belongs with project kinds, event rows and the caste matrix.
Merging them would put a vocabulary and a catalogue in one file — the failure ED-IN-0200 names.

**A stage row is data.** Adding a stage, a flaw or a belief proposition is a row, never a branch
(`00 §6` principle 3). Nothing in this design names a faction, a place or a person.

### 3.3 Age gates the stage count, and that is the whole of the age model

`identity.birth_season` is immutable; `form.life_stage` is not. Current age is
`season_now − birth_season`, **derived**, never stored — an age field would be an aggregate with a
setter, and no aggregate is ever written (`01 §2.1`).

A person generated *now* walks every stage whose gate their age satisfies, in order. A person
generated at a young age has walked two stages; one generated old has walked four plus several
career stages, **and the stages they walked are why their capability, edges and flaws look as they
do**. Nothing else in the design needs an age concept.

> `AGE_FORMATION`, `AGE_VOCATION`, `AGE_CATALYST`, and `N` (career-stage period in seasons) are
> **shape proposals with no canon backing found**. They are declared in `form_registry.yaml` gates,
> not buried, and each carries the **reachability bar** below.

**Reachability bar, both directions** (`00`'s standing requirement on any declared rate): at the
oldest generated age the world admits, the career-stage count must be **bounded** — otherwise
capability ratchets without limit and an old NPC is unbeatable by construction; and at the youngest,
at least **two** stages must have been walked — otherwise a young person is an unconditioned draw
and §3.1's whole argument evaporates for exactly the population the world makes most of.

### 3.4 Career advance in play is the **same module**, not a second one

The elegance test (`00 §1`, under-distilled: *two objects doing one job*) refuses a `cg.career`
module. There is one stage walker, `cg.stage` (§10), and it has two callers:

| caller | when | gate it satisfies |
|---|---|---|
| `cg.demand` → the generation loop | a person is created | age |
| the accounting boundary | a person has held a post for `N` seasons | age **and** service |

Both paths run the identical registry row, take the identical form transition, emit the identical
`form.transitioned` Key, and are therefore ranked by the Slate identically. **A promotion and a
backstory are the same object seen at different times**, which is the strongest form of `00 §6`
principle 8 (one engine, several entry points) this suite can offer for people.

⚠ **This reads state at the boundary; it is not a scheduled reaction.** `01 part 2 §9.3` (**J-N**):
the substrate has **no cross-season emission carry** — `next_tick` raises on a non-empty queue. A
career stage fires because the person **is** `N` seasons into a post at the boundary, never because
something was posted to them earlier. If J-N rules for reactive chains, this paragraph is what to
revisit; nothing else here changes.

### 3.5 Conditioning runs once per stage — v1's arithmetic, carried

v1 `02 §2.2`'s condition-then-reify pipeline is unchanged in substance and is now **layered**: stage
`k`'s output is part of stage `k+1`'s conditioning input. Both bounds survive and both matter more
now, because conditioning applies four-plus times instead of once:

```
logit_i = logit(prior_i) + clamp( Σ_c w_c · signal_c(i), −Δ_MAX, +Δ_MAX )      # bounded log-odds
p_i     = softmax(logit)_i
p'_i    = (1 − ε)·p_i + ε/n          ⇒  p'_i ≥ p_floor for every i             # entropy floor
```

**Additive log-odds, not multiplicative factors**, for the same reason `01 §5.3` keeps budget out of
the pool: a multiplicative factor is worth far more to a category already likely than to one in the
tail, so a unit of conditioning would not move the distribution by a consistent amount. That is the
non-uniformity the kernel rules out, appearing in a categorical draw.

**The entropy floor is the load-bearing one under layering, and its bar is now stricter.** Composing
`S` conditioning steps composes the drift; without a floor applied **at every stage**, a person from
an extreme place converges to a single archetype by Vocation and every Southern frontier character
is the same character — which reads to a player as authored, and is precisely the failure
conditioning exists to avoid.

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

**Every granted field must be load-bearing on at least one resolution branch, and the consuming
module is named before the field is added.** Carried from v1 `02 §2.3` unchanged, because it is the
gate that stops a generator becoming a characterisation engine: a field nobody reads will be cited
as flavour and will never change an outcome. Current consumers: capability is the pool of every roll
(`01 §6`); convictions rank a post-holder's option set (`05 §3`); edges are read by appointment,
patronage, succession and defection; flaws emit candidates (`10`); beliefs gate what a person will
argue and can be argued out of (§6); TS gates Knot formation and the Warden ladder
(`01 §7.5`; `faction_politics_v30:667`); Truth is canon's own piety meter.

---

## 5. Edges and Knots at generation

### 5.1 Six edge kinds, adopted from PP-724 — v1's enum is cut

`01 §7.2` cut v1's six-member `relation` enum and this suite's own draft table, superseded by
`systems/npcs/npc_relational_graph_v30.md` (PP-724, Class A, PROVISIONAL), which ships six canonical
NPC↔NPC edge types with per-type formation, strain, break and decay rules and a decision log
(`:46-56`). **Generation adopts them and adds nothing:**

`sworn-bond` (symmetric) · `liege-vassal` (liege→vassal) · `kinship` (symmetric; asymmetric
parent→child) · `patronage` (patron→client) · `rivalry` · `feud` (hereditary), strengths 1–3.

**A person is born owing someone something, and leaves generation entangled.** v1 required at least
two edges (one upward, one lateral) and was right; v2 requires **at least one edge per walked
stage**, which for a full ladder is at least four, mapped to what canon says each stage produces:

| stage | edge canon names | kind |
|---|---|---|
| Origin | *"family situation, first relationship"* (`questionnaire:55`) | `kinship` (and a second where the family is a household with a head) |
| Formation | *"mentor/teacher"* (`:56`) | `patronage` — the mentor is the patron; ordered, so read from the other end it *is* the client relation (`01 §7.2` refuses a `client` row) |
| Vocation | *"what you do"* — a trade, a post, a chapter | `liege-vassal` or a second `patronage`; a peer `sworn-bond`; or a `rivalry` where the conditioned draw put two people on one rung |
| Catalyst | *"what changed everything"* (`:58`) | `rivalry`, or `feud` where the stage's precedent tag names a lineage |

**Disposition is stored for PC↔NPC and derived for NPC↔NPC** (`01 §7.3`, PP-724 `:331-345`). A
generated NPC↔NPC pair therefore gets **no disposition gauge** — C-3. That is not a loss: it removes
a stored aggregate the write rule forbade, and PP-724 derives the value from edge state.

**Rivalries and feuds are escalation tracks, not strain tracks** (PP-724 `:674`, cited in `01 §7.2`).
A generated rivalry is not a weak feud; a stage may grant either, never one as a magnitude of the
other. **Kinship does not break by strain** (`:334-340`) — a generated family survives estrangement,
which is why the Origin edge is durable enough to still matter at Catalyst.

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
   requires Thread contact, and canon says TS is *"0 for non-practitioners"*
   (`clock_registry_v30.md:72`) with a **higher baseline in Southern Einhir populations**
   (`faction_politics_v30:649`, `:667`). Nothing in this document arranges that. It falls out of two
   ratified facts meeting, which is what change F was for: **the caste system is legible in who has
   Knots at all**, and that is also why the Warden ladder is open to the caste the rest of the
   system closes.
3. **A candidate that fails the gate is not discarded** — the stage's fallback is a strong edge of a
   PP-724 kind. A person who *could not* form a Knot with the person who mattered to them at
   fifteen has a `sworn-bond` and a Precedent tag instead. That is a better character than a
   silently-dropped seed, and it costs one line in the stage row.

*Emergent possibility lost if knot candidates were cut from generation:* every Knot in the game
would be one the player made in play, so the Thread layer would arrive at the start of the campaign
with no history and nobody would have already lost one.

---

## 6. Beliefs — what a person thinks is true, and how it is contested

### 6.1 Beliefs are not Convictions, and canon keeps them apart

**Convictions are what a person values; beliefs are what they think is true.** Canon carries both
and does not merge them: the thirteen-Conviction taxonomy is one object (`conviction_taxonomy_v30.md`,
PP-684), and a Belief is another — *"Per-NPC sheets carry 1–3 Beliefs as first-person quoted
strings"* (`systems/npcs/character_canon_v30.md`, §6.1 region, PROVISIONAL) with its own revision
rule at §6.2 (`:192`).

⚠ **Tier, stated honestly:** `character_canon_v30.md` is **`## Status: PROVISIONAL — pending
ratification`** (`:6`). It is the best statement of the belief object in the tree and this document
composes on it; it is **not** ratified canon and a later ruling may move it.

**A measured tree fact that makes this section necessary rather than decorative.** The belief object
already exists in code and **nothing produces it**: `beliefs.add_belief` has no callers and
`beliefs.revise_belief` is uncalled (`systems/characters/characters_flow_skeleton_v1.md:30-31`), and
`create_world` leaves `convictions`/`beliefs` as empty dicts *"not populated during world-gen"*
(`:92`). The missing producer is **character generation**. That is the gap `02` closes.

### 6.2 The composition — no new primitive, no new tag kind

| part | primitive | leaf |
|---|---|---|
| **which propositions this person holds** — the active set, `≤ 3` | `form.beliefs` on the person (C-4) | 4 — form transition |
| **how firmly** | a `credence.<proposition>` **Gauge** per held proposition | 1 — gauge deposit, provenance required |
| **what the proposition is** | a **row** in `references/content_registry.yaml` | data, not a branch |
| **what happens when one is given up** | a `Precedent` **Tag** — canon's Scar | 2 — tag append |

**Why a Gauge and not a Tag.** `01 §3.1` closes the Tag enum at six and demands a two-part argument
for a seventh; this design **does not open it**. A belief needs the two things a Tag deliberately
lacks and a Gauge structurally has: a **rest value** — the prior the person's origin supplies, so an
unreinforced belief drifts back toward what their caste, place and institution ambiently teach —
and **geometric decay toward it** (`01 §5.1`), which is exactly the right dynamics for conviction in
a proposition and exactly the wrong dynamics for salience-of-a-memory.

**Why the gauge-count objection does not apply here, though it killed gauge-per-memory.** `01 §3.2`
refused a Gauge per Memory because the count grows with everything anyone ever saw. **Beliefs are
capped at three per person by canon**, not by a parameter this document chose. That difference —
a cited bound versus an unbounded ramp — is the whole of the argument, and if canon's cap moves, this
decision must be re-examined rather than tuned.

**Canon's own precedent for the shape.** The `truth` track is already a 0–5 oscillating gauge whose
poles are two competing accounts of what is true — *"5 = Solmund orthodoxy, 0 = Thread-truth
acceptance"* — that *"varies by background"* and whose players *"see qualitative bands only"*
(`clock_registry_v30.md:71`). A belief gauge is that shape, generalised to a registry of propositions.

### 6.3 Revision — canon owns *when*, this document owns *where it is stored*

`character_canon_v30 §6.2` states three **conjunctive** conditions for revision: a decisive contest
outcome against the holder; the winning argument used the holder's primary or secondary Resonant
Style; the argument **specifically engaged the Belief**. Then: *"Old Belief → permanent Scar. New
Belief forms."*

**This document does not redesign that and does not weaken it.** The mapping is one line:

> Canon's three conditions are the **gate on a revising-magnitude deposit**. The gauge's declared
> band is what fires the **form transition** that drops the proposition from the active set and
> appends the Precedent tag. Ordinary evidence deposits move credence and never fire anything.

Two properties follow that a bare flag would not have. **A belief can be worn down and still held** —
credence below the band is a person who is losing an argument over seasons, which is the state the
setting is full of. And **the transition is a gate, never a roll** (`01 §2.2`): the uncertainty was
in the contests that moved the gauge, and re-rolling at the threshold charges for it twice.

**Reversibility and hysteresis.** Dropping a proposition is `reversible: false` — canon says the old
Belief becomes a permanent Scar, and a person may later come to hold the *same* proposition again,
which is a **new** row with a new provenance chain and the Scar still on the sheet. **No hysteresis
band is required or permitted**, because there is no reversible pair (`01 §2.3`).

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

**No branch names the Restoration Movement.** That is `00 §6` principle 2 satisfied on the case most
likely to tempt a special case.

*Emergent possibility lost if beliefs were cut:* nobody could be **persuaded** — only outfought,
outvoted or outbid — and an institution founded on a false premise could never discover it.

**Out of scope, stated once.** A general epistemic layer — machine-comparable propositions held per
agent with graded confidence and provenance, so two characters can *compare* what they believe — is a
Phase-2 corpus item and is not designed here. §6 ships the creed-Belief canon already names. If that
layer lands, `credence` and its confidence field are candidates to be **one field**, and the correct
outcome is a cut, not a synthesis that keeps both.

---

## 7. Flaws — and why there are no virtues

### 7.1 Virtues are cut (C-2)

**Virtue is Conviction #12 of the thirteen** (`conviction_taxonomy_v30.md:40`). A virtuous person is
a person with a high Virtue weight, plus the Precedent tags recording what they actually did. A
parallel `virtues` trait list would be a second object doing that job — `00 §1`'s under-distilled
failure — and, worse, it would be a **flat bonus attached to a person**, the shape `01 §4.3` refuses
because a flat shift is worth systematically more to a small pool than a large one.

**`traits` therefore ships `flaws` only**, and `01 §1.1`'s schema should drop the `virtues` member
unless another document populates it.

### 7.2 A flaw declares when it binds, and it must open something

Canon has no formal flaw mechanic, but it has the **shape**, authored per NPC:
`systems/npcs/npc_roster_v30.md:165-173` ships a summary table whose columns are **Compromise ·
AI Flaw · Key Consequence** — the condition, the bias, and what it costs *and buys*. One row is the
whole argument: *"PROCEDURALIST (slow) → Investigations +1 season **but Overwhelming**"* (`:170`).
The flaw is a different way of doing the job, not a subtraction from it.

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

1. **A flaw never touches the option set and never touches the odds.** It is not a remit filter — that
   would break ED-IN-0201 clause 2, which says the person shapes *which* action from the **same**
   option set with the same information (`00 §5`, `01 §4.3`). It is not a modifier — `01 §6` keeps
   modifiers in σ-space and reserves them for properties of the *target*. **A flaw emits a
   candidate**: when its predicate holds, a situation arrives. That is `00 §2.3` point 3 exactly —
   new objects add situations, not verbs — and it is why this document adds **zero player verbs**.
2. **A flaw that only subtracts is a debuff, not play.** Every row declares `opens` as well as
   `emits_candidate`, or it does not ship. The canon precedent above is the test case, and the
   reachability bar is: **the `opens` candidate must be reachable in a seeded campaign**, or the
   flaw is a penalty wearing a costume.
3. **A flaw is challengeable, and challenging it is a scene, not a purchase.** `challenge` names a
   form transition whose gate is a **resolved scene outcome**, not a spend. Passing tempers or
   retires the trait; it emits `form.transitioned` like every other transition, so the world notices
   that this person is not who they were.

**Where flaws come from.** A stage row (§4) or a Conviction Scar taken in play — canon's Catalyst
stage already produces a *"possible starting Scar"* (`questionnaire:58`), and canon's own Scar ladder
(`character_canon_v30 §6.3`) is what escalates them. Generation seeds; play accumulates; the
challenge transition is the only way down.

*Emergent possibility lost if flaws were cut:* nobody could be **reliably** wrong in a way another
actor can anticipate and exploit, so there would be nothing to know about a person that is worth
knowing.

---

## 8. Determinism, totality, and the two properties v1 got right

Carried from v1 `02 §4-5`, unchanged in substance, restated because they now cover a **loop**:

```
substream = Random( H(campaign_seed, "cg", tier_node, faction, ordinal, stage_index) )
```

`stage_index` is the only addition, and it is required: without it a person walking four stages would
consume four draws from one position and re-phase every later person. **The generator draws from its
own substream, never the shared campaign stream** (P0-2), so population size cannot re-phase any
other consumer of randomness.

**Generation is total.** For any well-formed demand, the ladder returns a person; there is no failure
branch and no "no suitable candidate". Ill-formed demands are **load-time validation errors**. This is
what lets ED-IN-0201's gate be a precondition rather than a trap: a faction's head post can always be
filled by *someone*; whether that someone is any good is the game.

**Totality now has a second obligation, because stages can fail their gates.** A stage whose gate does
not hold is **skipped, not retried** — and skipping is a legitimate outcome, not an error: a person
who never had a Formation is a person who never had a mentor, and the world should be able to make
one. **What may never be skipped is Origin**, which is where identity is fixed. Falsifier below.

⚠ **A guard that counts generator calls does not observe any of this.** Carried from v1: a population
guard must read the **person store**, because a call counter is invisible to a loader, a restore, or
any other path that constructs people without going through the generator.

---

## 9. The player-facing surface — counted against `00 §2`'s budget

**`02` spends zero of the whole-game single-digit verb budget.** Character generation is where a deep
game most often explodes its surface, and canon has already ruled the opposite way: *"the player
never sees Conviction weights, Self-Other values, or cultural template assignments"*
(`questionnaire:32`); *"a personality-and-competence simulation where the player never touches a stat
sheet"* (`:24`).

| what the player is asked | how many | how often |
|---|---|---|
| scenario questions across the four creation stages, **12–16 total**, canon's number (`questionnaire:43`) | 12–16 | **once per character**, ~10–15 minutes (`:47`) |
| a response to a **challenge** situation a flaw or a belief put on the Slate | `10`'s 3–5, inherited | when the Slate ranks it in — never pushed by this document |
| **in-play verbs added by this document** | **0** | — |

| what the player never touches |
|---|
| a stage row, a conditioning distribution, a `Δ_MAX`, a `p_floor`, an entropy floor |
| a capability number, a conviction weight, a credence value, a TS or Truth number (**bands only** — `clock_registry_v30.md:71`) |
| a flaw's `binds_when` predicate, a belief's revision band, an age gate's threshold — **triggers are hidden** (`01 §8`) |
| the caste **matrix** — but its **verdict on a named candidate is published in full** (`04`; `00 §6` principle 5) |
| whether a knot candidate passed canon's gate — they experience the relationship, not the roll |

**Substrate objects: 4 creation stages + N career stages · 1 grant vocabulary of 8 members · 6
adopted edge kinds · flaw rows · belief propositions · 2 identity fields. Surface: 12–16 one-time
questions, 0 verbs.** The substrate table is longer than the surface table, which is the ratio
`00 §2.3` point 4 requires.

**The 12–16 questions are not a verb and the distinction is load-bearing.** A verb is a thing a
player selects from a menu **every season**; the budget is about recurring cognitive load. A
one-time authoring interface that the player never revisits costs the *learning* budget once and the
*per-season* budget never. If that argument is rejected, the correct response is to shorten canon's
question set — not to move the derivation onto the player.

---

## 10. Module contracts

`00 §7`'s shape, with the v2 `form:` and `transitions:` fields. **Five modules; four are v1's, and
`cg.stage` is the only addition** — it is where change A lands for people.

```yaml
- module: cg.demand
  parent: character_generation
  class: substrate
  scales: [personal]
  tier: null
  resolver: gate
  remit: []                       # not player-invocable; raised by other modules
  budget: null
  consumes:
    - {type: post.vacant, from: [pm.vacancy]}     # → raises one demand per vacant post
  emits: []
  state: []
  form: []
  transitions: []
  disclosure: []

- module: cg.condition
  parent: character_generation
  class: substrate
  scales: [personal, settlement]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits: []
  state: []                       # pure; consumes no RNG and stores nothing
  form: []
  transitions: []
  disclosure:
    - {of: distribution, inputs: published, presentation: band, trigger: hidden}

- module: cg.stage                # NEW (v2). Walks ONE stage row. Two callers: generation, boundary.
  parent: character_generation
  class: substrate
  scales: [personal]
  tier: null
  resolver: gate                  # age/service gate; the CONTENT is cg.draw's derivation
  remit: []
  budget: null
  consumes: []                    # reads state at the boundary — never a posted emission (J-N)
  emits:
    - {type: form.transitioned, terminal: false}
  state:
    - {name: person.life_stage,  bucket: entity, writable: true, owner: cg.stage}
    - {name: person.capability,  bucket: entity, writable: true, owner: cg.stage}
    - {name: person.traits,      bucket: entity, writable: true, owner: cg.stage}
    - {name: person.beliefs,     bucket: entity, writable: true, owner: cg.stage}
    - {name: credence,           bucket: gauge,  writable: true, owner: cg.stage}
    - {name: tag,                bucket: tag,    writable: true, owner: substrate.ledger}
  form:
    - {entity_kind: person, field: life_stage}
    - {entity_kind: person, field: capability}
    - {entity_kind: person, field: traits}
    - {entity_kind: person, field: beliefs}
  transitions: [stage.*, belief.retire, flaw.challenge]     # from references/form_registry.yaml
  disclosure:
    - {of: person.life_stage, inputs: published, presentation: exact, trigger: hidden}
    - {of: person.traits,     inputs: published, presentation: exact, trigger: hidden}
    - {of: credence,          inputs: published, presentation: band,  trigger: hidden}

- module: cg.draw
  parent: character_generation
  class: substrate
  scales: [personal]
  tier: null
  resolver: derivation            # a draw from a declared distribution, not a contest
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: entity, bucket: entity, writable: false, owner: substrate.entity}
  form: []
  transitions: []
  disclosure:
    - {of: person.capability_provenance, inputs: published, presentation: exact, trigger: hidden}

- module: cg.attach
  parent: character_generation
  class: substrate
  scales: [personal]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits:
    - {type: person.generated, terminal: false}
    - {type: edge.formed,      terminal: false}
  state:
    - {name: edge,               bucket: entity, writable: true,  owner: substrate.entity}
    - {name: thread_sensitivity, bucket: gauge,  writable: true,  owner: cg.attach}
    - {name: truth,              bucket: gauge,  writable: true,  owner: cg.attach}
    - {name: tag,                bucket: tag,    writable: true,  owner: substrate.ledger}
  form: []
  transitions: []                 # a knot CANDIDATE is submitted to canon's gate; no transition here
  disclosure:
    - {of: thread_sensitivity, inputs: published, presentation: band, trigger: hidden}
    - {of: truth,              inputs: published, presentation: band, trigger: hidden}
```

**Two contract facts worth stating rather than leaving to be inferred.** No module here declares a
`budget:` — generation is not an action economy, and a budget that bought characters would be the
modifier-shaped currency `01 §5.3` refuses. And `cg.stage` is the **only** module in this suite
declaring `form: person.capability`, so the set of things that can move a person's competence is a
grep over one field — which is the entire point of the fourth write leaf being declared rather than
free (`01 §2.4`).

**Key types used: `form.transitioned`, `person.generated`, `edge.formed` — all three already declared
in `00 §9.2`. This document appends none**, which matters because P0-1 (`references/rendering_dispositions.yaml`)
is unexecuted and appending a type while it is would be the drift that precondition exists to stop.

---

## 11. Property audit

### 11.1 Engine class — and the scope gate, honoured

**Nothing in this document rolls.** A conditioned categorical draw is not the continuous engine, and
every transition here is a **gate** (`00 §6` principle 4). Per `00 §... delta §10`'s rule — *do not
manufacture a NERS verdict for a module that does not roll* — the four qualitative properties are
diagnosed against the generator directly, and where a property is about resolution it says so rather
than being scored.

The one roll in this document's blast radius is **canon's Knot formation roll**, which canon owns
(`01 §7.5`, `knots_v30.md:76-83`). It is cited, not designed, and it is not audited here.

| property | verdict | reasoning and falsifier |
|---|---|---|
| **P-i** legible odds | **pass, scoped** | The player does not choose against this draw, so predicting its odds is not a decision they make. What P-i requires here is that the *result* be legible: `capability_provenance`, the conditioning inputs and every caste verdict are published (`01 §8`; `04`). **Falsifier:** a test asserting every `cg.*` state row carries a disclosure block and none sets `trigger: published` |
| **P-ii** uniform leverage | **pass** | §3.5 — additive log-odds with a bounded shift; a unit of conditioning moves the distribution by the same amount wherever it lands. The multiplicative form fails this and is the version not built. **Falsifier:** apply a fixed signal to a tail category and a head category and assert the log-odds delta is identical |
| **P-iii** bounded, monotonic | **pass, with the layering caveat** | Capability moves one axis by at most one band per stage and is clamped; conviction reweights sum into the declared band; `Δ_MAX` bounds conditioning and `p_floor` bounds degeneracy. **The caveat is real:** these bounds were proved for ONE application in v1 and now apply `S` times. **Falsifier:** §3.5's terminal-distribution test, plus a test asserting no generated capability exceeds `descriptors.ATTRIBUTE_CEILING` after the longest reachable ladder |
| **P-iv** graded, recoverable | **pass** | §8 — generation is total, and the load-bearing event (can a required post be filled) cannot fail. Stage skipping is graded, not all-or-nothing. **Falsifier:** a test asserting every well-formed demand returns a person, and that `Origin` is present on **every** person in a seeded world |
| **P-v** right engine | **pass** | Not a contest, so neither canonical resolver applies; a draw from a declared distribution is the right tool, and a contested roll here would be a resolution where the answer is a construction. Every *transition* is a gate because the uncertainty was upstream |

### 11.2 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| demand → generation → post filled → (later vacancy) → demand | demands are raised only by vacancies and scenes, both bounded by the map; satisfying a demand **removes** it | **not a gain loop** (carried from v1) |
| stage `k` → conditions stage `k+1` → … | the stage ladder is finite and age-gated; `reversible: false` on every stage transition means no cycle exists | **bounded by construction** |
| career stage → capability up → better outcomes → post retained → career stage | `N`-season period; one axis by one band per stage; `ATTRIBUTE_CEILING` clamps | **positive feedback, bounded above. Gain UNMEASURED** — nothing has run a campaign long enough to observe whether an incumbent becomes unbeatable before the ceiling binds. §3.3's upper reachability bar is the guard, and it is unverified |
| belief evidence → credence → revision → Scar → conviction shift (`character_canon §6.3`) → new belief | active set ≤ 3 by canon; canon's own Scar ladder terminates at "3+ — crisis" | **gain UNMEASURED**, and the escalation is canon's, not this document's |
| flaw binds → candidate → scene → challenge → transition | the Slate's scene budget (`10`) bounds how many ever reach the player; `challenge` is `reversible: false` | **bounded by the Slate**, which is why P0-5 orders `10` before F |

### 11.3 What this document depends on that could move

| dependency | tier | if it moves |
|---|---|---|
| `character_canon_v30.md` (the belief object, the `≤3` cap, the revision conditions) | **PROVISIONAL** | §6's cap loses its citation and becomes a parameter — at which point the gauge-per-belief decision must be re-argued against `01 §3.2`, not tuned |
| `npc_relational_graph_v30.md` (PP-724) | Class A, **PROVISIONAL** | §5.1's kinds change; the *container* does not (`01 §7.3`) |
| `faction_politics_v30.md §3.2` | **CANONICAL** | `04`'s gate changes; `02` is unaffected — it supplies the input, not the rule |
| Key **consumption** (`cg.demand`'s `consumes:` row) | **J-O** open | `cg.demand` becomes a boundary read over vacant posts. Nothing else here consumes a Key |
| cross-season latency | **J-N** open | §3.4's career gate is written as a boundary state read precisely so it survives either ruling |

### 11.4 N / R / S / E

**Necessary** — a game gated on people existing cannot omit the thing that makes people, and the
belief object already in the tree has **no producer** (`characters_flow_skeleton_v1.md:30-31`, `:92`).
**Robust** — the two failure directions are each bounded by a declared parameter with an arithmetic
check, and the layering that v2 adds is the one place that robustness is *weaker* than v1's, which
§11.1 P-iii says rather than hides. **Smooth** — one pipeline for authored and generated characters,
one substream, one stage walker serving both creation and career, one attribute roster read from the
registry, zero attributes and zero convictions named literally. **Elegant** — four stages adopted
from canon rather than invented, one grant vocabulary of eight members, one new module, **no new
registry file, no new stored primitive, no new Tag kind, no new Key type, and no in-play verb**.

### 11.5 The weakest claim in this document, named

**That a belief belongs in a Gauge.** It rests on canon's `≤3` cap, and that cap is **PROVISIONAL**.
If the cap moves — or if a later layer wants propositions held by *every* person about *many* facts —
the gauge-per-belief count grows exactly the way `01 §3.2` refused for memories, and the correct
response is to re-derive credence at read from tag data rather than to raise a limit. The falsifier
is cheap and should be run before any belief content is authored: **count `credence` gauge instances
in a seeded world and assert the per-person count is `≤ 3` and the world total is `≤ 3 × persons`.**
