# Part C — evaluation

## Status: **PROPOSED (2026-09-10). HELD BACK IN FULL** — see `00_INDEX.md`. Continues in `04_EVALUATION_part2.md`.

**Instrument.** `skills/ners/SKILL.md`, run in full: §2's N-line ledger and its three verdicts, §3's
five disqualifiers, the meta-rule at `:137-144`, §4's C1–C5, §5's ratio with the §5.1 denominator and
the §5.2 watchlist, §6's four R tests with the per-seat gain/cost tables, §7's six-direction coverage
plus *pauses correctly* and *calculations consistent in methodology*, §8 against the set's own declared
disciplines, and §9's self-audit. Instrument B is not run: no proposal in the set resolves by a draw.

**Every locus below is the tree at `ccc3f2a`.** The set was authored against `8b79440` and
`ED-IN-0203`/`ED-IN-0206` landed between the two, so the proposals' own `driver.py:<N>` and
`decision.py:<N>` citations resolve to nothing. The content survived the move and is re-verified at its
new home; the map is in §0.

---

## §0 · Where the code the set argues from actually lives

`engine/season/loop/driver.py` is **260 lines** and binds six step modules at `:241-253`.
`decision.py` is a package. Nothing below is a change of substance — every relocated claim was re-read
at its new locus and holds — but a builder following the set's line numbers opens the wrong file.

| the set cites | the content is now at |
|---|---|
| `driver.py:415-436` (the larder draw) | `matter.py:145-166` |
| `driver.py:425` (`wt * len(eaters)`) | **`matter.py:155`**, verbatim |
| `driver.py:431-436` (starvation refused) | `matter.py:161-166` |
| `driver.py:413` · `:418` · `:406-411` · `:458-460` · `:485-490` | `matter.py:143` · `:148` · `:136-141` · `:188-190` · `:215-220` |
| `driver.py:1371-1383` (CENSUS writes nothing) | `census.py:25-37` |
| `driver.py:651-655` (the actor check) | `deliberate.py:152-156` |
| `driver.py:856-865` (a verb with no effect raises) | `resolve.py:233-242` |
| `driver.py:319` · `:343-348` | `matter.py:46-50` · `matter.py:76-78` |
| `decision.py:165, 890` | `budget.py:56-60`, `options.py:35-104` |
| `decision.py:183, 228` (clause 3) | `options.py:48, 93` |
| `decision.py:208-214` (clause 4 polarity) | `options.py:73-79` |
| `decision.py:298-302` (`urgency` inert) | `choose.py:52-55` |
| `world_q.py:217-221` (Q3) | `world_q.py:219-223` — and **the +2 shift is the whole file**: Q2 `:176, 195-197` → `:178, 196-199`; `lateral` `:126-130` → `:128-132`; `commit_count_guard` `:116-124` → `:118-126`; `single_holder_counter` `:89-114` → `:91-116`; `presence` `:152-154` → `:154-156` |
| `rosters.yaml`, `verb_table.yaml`, `write_matrix.yaml`, `hole_register.yaml` | `engine/season/<name>.yaml`, not `engine/season/data/` |

**Q3 is the one relocation that is also a change, and it does not reach P1.** `world_q.py:219-223`
now admits everyone present at a crossing — `if who == p.id or (at is not None and p.id in
presence(w, at))`. But `at` comes from `w.sites.get(who)`, and **P1 appends person-keyed crossings**
`(p.id, verb, before, after, ev.id)`, for which `w.sites.get(<a person id>)` is `None`. The second
disjunct collapses and only `who == p.id` fires. **So the broadcast is live for site crossings and
dead for P1's**, and both of P1's halves are still open: the referent is `(what,)`, a verb name, and
nobody but the crossing person is asked. The tree's own comment at `world_q.py:203-208` records this
same site-id-against-person-id confusion as a defect it already shipped once.

---

## §1 · The verdict

**The set is `paper` in all seven proposals, and two of the seven do not load.** Under `CLAUDE.md`
§0.2 nothing here is done, and that is the honest grade for a design document; what distinguishes the
seven is *how far each is from an execution artifact*, and the distances are very different.

| | verdict | the execution step that is the whole difference |
|---|---|---|
| **P1** | `paper` — buildable | a declared collapse rule for a per-kind shortfall, then a test on `p.body` with a control arm that can actually be fed |
| **P2** | `paper` — buildable, unobservable through the corpus | `W29`; the falsifier needs `3 × band_seasons` seasons and `corpus_run.py:65` clamps a case at 6 |
| **P3** | `paper` — **two writes are refused by the gate, and its one demand kind is authored-only** | matrix step edits *and* a driver the social gate accepts; neither is declared |
| **P4** | `paper` — **refuses at load** | three table corrections before either verb can be attempted |
| **P5** | `paper` — one object refuses at load | `EFFECTS["commit"]`; the loop needs a primitive the set correctly declines to smuggle |
| **P6** | `paper` | `EFFECTS["repudiate"]`; the cost it claims is unreachable by any computed act |
| **P7** | `paper` | `EFFECTS["issue"]` plus a writes-cell edit; compliance is unreachable until `H-84` or `H-71` |

**Three findings outrank everything else in the set.**

**One — the political half cannot be reached by a person's own deliberation, and the set does not say
so as a whole.** P5 declares its own loop unreachable and prices the repair honestly. P6 and P7 make
the same class of claim — a superior notices a defection, an issuer notices defiance — and neither
declares it. The mechanism is one theorem: a claim enters a person's question set only if its subject
is that person or an object of one of their live tenures (`world_q.py:178, 196-199`), and **a person id
enters that set only through a live `tie`, `knot` or `oblige`** — none of which has an effect.
(`succeed` looks like a fourth and is not: a Tenure is filed under its subject and only when that
subject is a person, `world.py:257`, and `succeed`'s subject is a Rung, so it lands in `_unowned` and
never appears in anyone's `p.tenures`.) `EFFECTS` registers exactly ten verbs (`effects.py:91-406`: confer, revoke, convene, move,
work, create_record, destroy_record, kill/wound, utter, transfer). So no computed act can put a person
id where another person's questions would find it. **Every "an NPC notices and responds" claim in
P5–P7 is unreachable for the same reason, at the same line.**

**Two — five objects across the set have no reader, and three of them are counted as contributions.**
`population()` (P2), `faction_value` and `faction_q.resolve` (P5), and `suspicion` (P7). Under `ID-13`
each is the defect the set itself files against `Sensation.standing` in `01_PRIMITIVE_BASE.md` §2. P2
and P5 mark theirs `[GAP: no consumer]` and still count them in *Adds* and in "New primitive? None";
P7 marks nothing, and asserts a reader that cannot see it — `stance_toward` reads `p.stance` rows and
never the ledger (`choose.py:40-49`).

**Three — the set adds vocabulary and deletes almost nothing, which is the meta-rule's own test.**
*A fix that adds a system has failed*; the remediation standard is *three edits, two of them deletions,
and the vocabulary got shorter.* Counted across seven proposals: **two verb rows, six effects, three
rosters, roughly twelve fixtures, five Queries, one Record kind, one `band_floors` row, seven LOOP
rows — and one deletion**, a refusal comment at `matter.py:161-166`. Vocabulary is longer by more
than twenty names. Three of the five Queries are the dead carriers above. The one true collapse the
set contains — Dispensation folded into `Record` — is the only move that shortens anything, and it is
narrated rather than spelled.

**What the set is, stated plainly.** It is a correct and unusually well-grounded reading of what the
substrate lacks, carrying four substrate proposals that would work once their table cells are right,
and three political proposals that are **a substrate for politics rather than politics** — three
authored verbs whose execution can be tested, one Query that computes, and one typed cell on a sound
precedent. That is worth having. It is not what the set's own index claims.

---

## §2 · The set read together

### 2.1 The loop register does not close where the set says it does

`00_INDEX.md` claims four amplifying loops, three damping, and that every `+` names an existing `−`.
Against the tree:

| loop | sign | bound | holds? |
|---|---|---|---|
| P2 · births | `+` | P1's `fed_ratio` | **yes** — at steady state `fed_ratio → yield/draw` and births fall toward zero. A real Malthusian bound |
| P3 · individuation | `+` | scene budget · the grown band · de-individuation | yes, and P2-fed |
| P4 · sites → yield → stakes → sites | `+` | wear (`rosters.yaml:698-701`) | **for Sites only.** Wear closes a *Site*. **Nothing closes a Rung**, so the rung count has no bound at all |
| P5 · commitment | `+` | — | declared dead by the proposal itself |
| P1 · dearth | `−` | — | yes, and it is the set's only live damping term |
| P6 · repudiation | `−` | — | unreachable: no computed `revoke` (`H-71`), no person-subject route into a question |
| P7 · defiance | `−` | — | unreachable, same two reasons |

**Three live `+`, all substrate. One live `−`, and it is starvation.** Nothing political damps
anything by a person's own choice, because no political candidate forms. The set ships amplifiers
whose only computed damping is hunger and wear.

### 2.2 Three denominators for one population — an S-methodology defect

*Calculations consistent in methodology* is a NERS test, not an adjective, and one quantity is computed
three ways across the set:

| | who is counted |
|---|---|
| `mouths(r)` (P1) | named eaters **+ the envelope** at `r` |
| `population(w, r)` (P2) | envelope + persons over `descendants` |
| `commit_share` denominator (P5) | persons over `descendants`, **envelope excluded** — `presence` returns persons only (`world_q.py:154-156`) |

The envelope eats, is counted as a mouth, and cannot revolt. P5's exclusion has Layer 1 behind it —
§10.3, the envelope does not act — but **P5 never says it chose it**, and the consequence is a
denominator no player can see: a town of three named persons and two hundred envelope "turns" at two
commitments.

### 2.3 Three death sites for one class

A singleton dies at MATTER on `(Person, exists)`; a cohort shrinks at CENSUS on `(Person, weight)`; the
envelope dies at MATTER on `(Rung, envelope)`. `Person` is one class by construction
(`carriers.py:348`), and P1 takes the CENSUS path explicitly to avoid a one-line matrix edit. Calling
it swept does not cure a methodology split — **the sweep's own `MAT` arm is the fix.**

### 2.4 One fixture name, two index sets

`mortality[band]` is indexed by **body-condition band** in P1 (the only band a cohort Person has,
`rosters.yaml:973-976`) and by **age band** in P2. `CLAUDE.md` §4 requires a term to yield the same
meaning read cold in a later session. This one does not.

### 2.5 A per-kind shortfall collapsed to a scalar, twice, undeclared

`short` is `dict[kind → int]` (`matter.py:158-159`) — the loop is over the weights registry, per matter
kind. `Person.body` is one `int` (`carriers.py:367`). P1's `deficit_p = short × weight(p) / mouths(r)`
and P2's `fed_ratio = 1 − short/draw` both need a dict-to-scalar rule and neither declares one. The
set's own `§3.2` discipline forbids exactly the fungible summing the collapse would perform.

**And the shipped fixture makes this immediate rather than theoretical.** In `tiny_world` no rung holds
salt (`probes.py:72-73`), so `short` is non-empty at every rung every season today. Under P1 as
written, every hearth-dweller and the King lose body every season, and P1's stated control arm —
*"stores ≥ draw → no `body.changed`"* — is unreachable on the corpus fixture.

### 2.6 Everything emitted at CENSUS is unwitnessable

WITNESS runs before CENSUS (`driver.py:215-216`), so P2's envelope reconciliation and P3's
`person.individuated` / `individuation.refused` are emitted where nobody can perceive them. The repair
is **not** free: Layer 1 puts individuation at CENSUS by design (`04_CODE_ARCHITECTURE.md:161`,
`holonic:1019`), so moving the emission is an amendment, not a relocation.

### 2.7 What `H-62` does to the political half

`choose` scores `Σ convictions × alignment + stance_toward + urgency` (`choose.py:105-109`). No verb
writes `convictions` or `stance` (`hole_register.yaml:715-717`), and `urgency` is inert by construction
(`choose.py:52-55`). **Every person's preference order over `(verb, subject)` is a world-gen constant**,
and what varies season to season is only which candidates the question machinery hands them. Given
that: nobody's own scoring can make them betray a commitment, no NPC repudiation can arise from a
changed conviction, and a compliance contest is a lookup on a fixed vector. R7 calls `H-62` first-rank
and unavoidable; the set names it as a hole and then makes claims that require it closed.

---

## §3 · P1 · Dearth reaches the body

### N — six directions

**NARROWED.** Today `short` is a `TRACE.note` (`matter.py:158-166`); `budget()` reads `p.body`
(`budget.py:58, 73-75`) and only `_eff_kill` writes it (`effects.py:357-371`). The step *a shortfall
reaches a person's state* has no carrier without P1, and N holds there.

| direction | verdict |
|---|---|
| top-down | **narrowed** — stated over `levy`, which has a prose `requires`, no typed cell and no predicate, so the fold raises `Unspecified` (`resolve.py:189-200`). Narrowed to `transfer`, the one executing extraction |
| bottom-up | **narrowed** — the question reaches those present; beyond the hearth it needs a further act by a further person |
| vertical | **holds** — `budget.py:58` subtracts `body_band_penalty` |
| diagonal | **narrowed to expressible** — a cell recruiting in a starving hamlet needs `commit` candidates no uncommitted person can form |
| lateral | **holds** |
| horizontal | carried by P5, which does not carry it |

**Restated N-line:** *cut P1 and a shortfall at a rung can never change what a person present there may
choose, or is asked about. Everything beyond that hearth is a further act by a further person.*

### False N-lines — none, and one claim that is false as filed

Every added object survives its walk. What does not survive is the claim that P1 *"makes `SUBSIST` and
the larder one arithmetic"*. P1 edits the larder only. `SUBSIST` (`probes.py:115-120`) still sums
`stores.values()` fungibly and divides by `p.weight`, ignoring `subsistence_weight`. After P1 the
larder honours both terms and `SUBSIST` honours one: **two methodologies remain, and P1 unifies the
two it touches.**

### The meta-rule, per object

The body write argues its way out — one site on an existing row, and it **deletes** a refusal comment.
The `len → Σ weight` change is an edit. The Q3 referent branch argues out as an edit to an existing
consumer, but **its specification lives only in an annotation**: the *Adds* bullet says the referent
becomes the containing rung id and carries no code, while the annotation admits a second
under-specification and does not close it. **The cohort CENSUS decrement does not argue out** — it is a
second death path for one class, taken to avoid a one-line matrix edit, and the meta-rule prefers the
edit.

### E — scored last, as a ratio

**E-OVERHEAD.** In: one write site, one branch, one arithmetic change, two fixtures, one LOOP row. Out:
one refusal comment. Verbs ±0. Vocabulary +4, −0 — **longer**.

**The denominator.** Two authored fixtures, and one hidden term that is the real cost: the dict→scalar
collapse above. The *value* of `k` is Jordan's; **the form is not** — as specified, `deficit_p`
multiplies a per-kind dict by a scalar.

**E-LEGIBILITY: pass, with a residual.** *No grain, fewer scenes, then a funeral* is predictable in
shape — monotone body loss, band-counted budget. The residual: a **salt-only** shortfall producing a
funeral is not intuitable from "no grain" until the collapse rule is declared.

**§5.2 watchlist.** The unification of the larder and `SUBSIST` is *incomplete* rather than
over-distilled; the collapse of per-kind shortfall to one body scalar is **kept at LOW confidence** —
it may be right, and nothing in the set argues for it.

### R

**R-COMPLETE — findings.** The dict→int signature. A contradiction inside P1: `body == 0` writes
`(Person, exists)` with no weight guard while a cohort's weight decrements at CENSUS, so a cohort at
body 0 is ruled two ways. `round(weight × mortality)` is 0 for any `weight < 1/(2·mortality)`, not only
weight 1. And the Q3 branch changes the referent for **site** crossings too — `world_q.py:223` builds
one `Question` shape for both — moving every existing corpus question that source produces, which P1
does not name.

**R-VARIETY — nil, and not a defect.** P1 is a clock.

**R-WORLD — hooks are thrown, and one is borrowed.** `body.changed` and `condition.band_crossed` are
MATTER emissions and reach WITNESS (`matter.py:273`). ⚠ **`condition.band_crossed` is not on
`(Person, body)`'s emission column** — that row declares `body.changed · person.died`
(`write_matrix.yaml:167`) and the crossing kind belongs to `(Site, condition)` (`:321`). P1 constructs
the Event by hand on the `matter.py:248-252` precedent, which bypasses the undeclared-kind refusal at
`world.py:275-291`, so it works — by borrowing another row's column, unremarked.
The emission chain constructs. The *story* does not: **"a hamlet empties itself" needs `move` with
`to ≠ home`**, and `to` binds the question's referent (`options.py:310`), which is the person's own
containing rung — so the formed act is a move to where they already stand.

**R-CHOICE — findings.** Seat: a person at a short hearth. Intent: *stop my body falling.*

| act | gain | cost |
|---|---|---|
| `transfer(from=Hh, to=Hh)` | **none** — `from` binds the actor's own containing rung (`options.py:316-317`), `to` binds the referent (`:310`), the same rung | 1 scene |
| `speak(Hh)` | a claim in hearth-mates' ledgers — they are hungry too | 1 scene |
| `move(to=Hh)` | none | 1 scene |
| do nothing | none | 0 |

**No row reaches the intent.** And the fed lord who could feed them needs a question whose referent is
that hearth; P1 gives him none, because he is not present there. The advertised choice — *spend grain
or spend scenes* — is on neither seat's table. Upper bound, per §6.2; and the act economy is the
denominator, per §6.3.

### S

| direction | carrier |
|---|---|
| top-down | `matter.py:148-173` + the P1 write; `transfer` executes, `levy` raises |
| bottom-up | the Q3 branch, for those present only |
| vertical | `budget.py:58` — carried |
| diagonal | uncarried — delivers blind |
| lateral | state differs; no seam reads across |
| horizontal | P5's, uncarried |

**Pauses correctly: pass** — the write is at MATTER before the freeze, read at DELIBERATE.
**Methodology: fails twice** — `SUBSIST` against the larder, and singleton death at MAT against cohort
death at CEN.

### Repairs, worst first

1. Take the matrix edit P1 declines — `(Person, weight) · [MAT, CEN]` — and put cohort death in the same
   `body == 0` rule. **Deletes** the CENSUS path: one class, one death site.
2. Declare `k` per matter kind, or declare the collapse. One fixture shape.
3. Move the Q3 branch out of the annotation and into the specification, and state that site-crossing
   referents move with it.
4. Restate the unification as a limit: the larder is one arithmetic; `SUBSIST` is a second until deleted.

---

## §4 · P2 · The bodies clock

### N — six directions

**NARROWED.** Top-down holds: the envelope today is a `W9` literal that never moves
(`probes.py:1553`), so without P2 nothing about a rung's population changes across forty seasons.
Bottom-up is **asserted** — nothing in P2–P4 promotes a rung's *kind*, so "a hearth grows into a
community" has no carrier. Vertical is **false in that direction**: it rests on `population()`, which
nothing reads, and a loss nothing observes is not a loss. Diagonal, lateral and horizontal route
through individuated persons committing or moving, and the envelope never commits.

**Restated N-line:** *cut P2 and the count a rung's larder must feed changes only by `move` and by
death, and P3's grown band is a constant forever.*

### False N-line — `population()`

**Disqualifier 2's mirror: no reader.** The proposal writes `[GAP: no consumer]` and says it is *named
rather than shipped* — and then stands it in *Adds*, counts it in "New primitive? None… one Query", and
lists it in the index. §3.1's second evasion, *it costs no code*, is refused: it is authored, named and
counted. Under `ID-13` it is a dead carrier of exactly the kind the set files against
`Sensation.standing`. **Delete it from *Adds*;** it is a one-line `r1_aggregate` on the day a consumer
exists.

**Watchlist (§5.2).** `envelope_bands` is **kept at MEDIUM confidence** — P2 could run on positional
bands with a `fertile_band` index, and the only named read is `envelope[grown]`; what the roster
protects is the design's ability to say *which band reproduces*, on the `strata` precedent
(`rosters.yaml:121-129`).

### E

**E-OVERHEAD.** In: one roster of three names, **four** fixtures, one MATTER pass, one Query, one
reconciliation write, one LOOP row. Out: nothing. Vocabulary +9, −0.

P2 declares **three** fixtures and uses four — `k′` appears in the deaths formula and is never
declared.

**The denominator:** an authored band inventory plus four authored rates; the same undeclared
dict-to-scalar collapse as P1, here in `fed_ratio`; and, if `E-1` lands on the capacity arm, a fifth
table.

**E-LEGIBILITY — partial.** *Fed towns grow, then they are hungry* is legible only if the player sees
`envelope.changed`; expression is unbudgeted, and the CENSUS reconciliation emission is unwitnessable.

### R

**R-COMPLETE — findings.**

- `fed_ratio` is undefined over kinds.
- **Bound (ii) is misfiled.** `mortality[elder] = 1.0` caps a *lifespan* at `bands × band_seasons`; it
  does not bound a *population*. If `fertility × (seasons in grown) × survival > 1` the envelope grows
  until bound (i) bites. Bound (i) is the real one and it holds.
- **Co-location is never stated.** The larder is per rung (`matter.py:148-150`) and `presence()` is
  direct containment (`world_q.py:154-156`). `W9` puts the envelope on the settlement while
  `tiny_world`'s persons are at the hearth (`probes.py:103-106, 1552-1553`). P2 never says which rung
  kind carries an envelope — so a settlement envelope eats the settlement's stores alone, P2's own
  "203 mouths" arm never arises, and an envelope at a rung with no stores starves at `fed_ratio = 0`
  while the hearths below it are full.

**R-WORLD — envelope waves are emergent and witnessable at MATTER.** Hooks are thrown. The link from
the crowd's hunger to a named person depends on the co-location rule above.

**R-CHOICE — not scorable**, and the precondition is named: the seat P2 offers is *found or feed*, and
`found` does not load.

### S

Top-down reaches the envelope only through `fed_ratio`, which is P1's. Bottom-up is carried by
`mouths(r)`. Vertical has a carrier with no reader. **Lateral is uncarried and the proposal says
otherwise**: `move` moves a `Person` (`effects.py:162-199`), never envelope weight, so *"migration is
`move`"* is false for the unnamed.

**Pauses correctly: pass.** **Methodology: pass with a note** — bodies-before-larders honours
`holonic:846`; `fed_ratio` is last season's while the draw is this season's, which is one quantity at
two ticks in one formula, declared and defended on the `matter.py:136-141` precedent.

### Repairs

1. Delete `population()` from *Adds*.
2. State the co-location rule — *the envelope lives at the rung whose stores it eats* — as a load check.
3. Declare `k′`; declare the collapse rule shared with P1.
4. Re-file bound (ii) as a lifespan cap and let bound (i) carry the population.
5. Rename `mortality[band]` against P1's.

---

## §5 · P3 · Individuation is a refusal

### N — six directions

**NARROWED to one member, and that member is authored-only.** `dispatch` has a live predicate
(`predicates.py:261-265`), so its refusal is *producible* — but its eligibility is the single
alternative `["remit:dispatch"]` (`verb_table.yaml:183`), and `remit:` is declined person-side
(`options.py:163-169`). **No person can form a `dispatch` candidate in any world.** That is the same
`H-71` mechanism that kills `revoke`, `issue` and `levy` elsewhere in this evaluation, and
`hole_register.yaml:804` measures it: *"9 of 32 verbs cannot be formed person-side — 8 remit-ONLY, plus
`levy`."* So P3 stands under §7's theorem exactly as P5 does, and unlike P5 it does not say so.
Bottom-up is asserted — a crowd producing a spokesman needs `carry`, which does not execute. Vertical
holds. The rest route through verbs that do not execute.

**Restated N-line:** *cut P3 and a refused `dispatch` at a rung with an envelope can never produce a
person.*

### False N-lines — three of the four roster members

`demand_kinds` is proposed with four members. Walked one by one:

| member | verdict |
|---|---|
| `dispatch.refused` | **survives, ambiguously.** The same kind is emitted on ineligibility (`resolve.py:159`) and on precondition failure (`:201-206`), and the untyped path leaves `observed=()` — so CENSUS cannot tell a King without the remit from a King naming nobody |
| `levy.refused` | **disqualifier 2 — no producer, and it dies twice.** Its eligibility is `["remit:issue", "presence:<rung>"]` (`verb_table.yaml:334`) and **both alternatives decline person-side** (`options.py:163-168`), so no candidate forms and the fold is never reached; were it reached, `levy` has no typed cell and no predicate and would raise `Unspecified` at `resolve.py:189-200`. P3's falsifier asserts an Event that cannot be emitted |
| `petition` at an empty rung | **disqualifier 2.** `petition` writes `Petition.exists` with no effect, so it raises. And `emits_on_refusal: []` (`verb_table.yaml:384`) means it has **no refusal kind of its own** — the fold falls back to the generic `act.refused` (`resolve.py:206`), which fires for every refused verb in the table, so CENSUS reading it would mint on any refusal anywhere |
| a Named operand | **disqualifier 2.** Nothing resolves a subject *inside* a cohort; a cohort is one id (`carriers.py:348-351`) |

So `incomplete: {have: n, target: 9}` has **n ≤ 1**, and that one is ambiguous. The roster is a name
for an unshipped composition — §3.1's first evasion — and survives only as a one-member roster.

**And the mint does not satisfy the demand that caused it.** The demanded subject
(`predicates.py:264-265`) is not the id P3 mints, which is `H(seed, tick, r, "individuated:" + event.id)`.
A repeated `dispatch` to the same absent name mints a **new stranger every season** until the grown
band is spent.

### The gate refuses two of the mint's three writes

P3 says it is *"a CENSUS body on rows that already exist"*. That is true of the rows and **false of the
steps**:

| write | steps | social | at CENSUS |
|---|---|---|---|
| `(Person, exists)` | `[MAT, RES, CEN]` | false | **admitted** |
| `(Rung, exists)` — the person-rung | `[RES]` | true | **`Forbidden`** (`world.py:326-343`) |
| `(Tenure, since)` — the `contain` edge | `[RES]` | true | **`Forbidden`**, and again at `:351-357` because the driver is not an `Act` |

`F.30` requires exactly these three writes in the same CENSUS write, so the collision is Layer 1's
matrix against Layer 1's `F.30` — but **P3 inherits it unnamed**, declares no matrix edit, and its
compliance table has no gate row for either write.

⚠ **And a matrix step edit would not be enough.** The second gate is step-independent:
`world.py:352-357` raises on `social and driver != "Act"` whatever the step column says, and **both
rows are `social: true`**. A CENSUS write is driven by the loop — `04_CODE_ARCHITECTURE.md:161` gives
`loop/census` the MATTER token — not by an act. So admitting CEN on those rows leaves the write still
refused. `driver` is a caller-supplied string nothing validates, so an implementer *could* pass
`driver="Act"` at a barrier where no act occurred; that is the shape of the real cost, and it is a
larger thing to ask for than a step column. **This is P3's actual price and nothing in the set names
it.**

Two smaller signature faults: the mint draws *"the parent rung's marks"* and `Rung` has no `marks`
(`carriers.py:510-511`); and de-individuation folds any person with no `hold`, no `knot`, no live
Petition and no mention in another's ledger — **which on `tiny_world` is four of the five persons after
one quiet season**, leaving only the office-holder. The weight returns to an envelope that is `[]` at
every corpus rung, to an unspecified index.

### E

**E-OVERHEAD.** In: one roster (four declared, ≤1 live), one CENSUS body, one closer, **two undeclared
matrix step edits**, one LOOP row. Out: nothing. Vocabulary +4, −0.

**E-LEGIBILITY — fail.** The offered intuition is *act on a crowd and someone steps out of it*. The
outcome as specified is an anonymous id at an unspecified rung, and your dispatch refuses again next
season. The intuition contradicts the outcome shape.

### R

**R-WORLD — a dead seat.** A minted person has empty capability, an empty ledger (WITNESS precedes
CENSUS), no `commit` and no `hold`. `questions_for` yields nothing for them — Q1 needs a Date holder,
Q2 an own claim, Q3 presence at a crossing, Q4 a commitment — and under P3's own closer they fold at
the next CENSUS unless someone's ledger names them. **They exist for one season, ask nothing, and emit
one unwitnessable Event.**

**R-CHOICE — findings.** Seat: a governor. Intent: forty hands. `levy` raises; `oblige` has no effect;
`dispatch` repeated is one scene each and mints a stranger each time — dominant and pathological.

### Repairs

1. Delete `levy.refused`, `petition` and the Named operand from `demand_kinds`; ship `{dispatch.refused}`
   with `have: 1`.
2. **Mint the demanded subject's id**, not a fresh hash, wherever the act named one. One change closes
   the demand loop.
3. Price the gate honestly: the step edits are necessary and **not sufficient**, because both rows are
   `social: true` and the CENSUS driver is not an act. Say what the write is driven by.
4. Scope de-individuation to persons whose `(Person, exists)` was written at CENSUS, and define the
   band the weight returns to.
5. Delete *"the parent rung's marks"*.

---

## §6 · P4 · Founding and building

### N — six directions

**NARROWED, and it is the strongest N in the set.** The warrant is `R4` verbatim — *the world only
decays; `Rung.exists` and `Site.exists` have zero producers* — so P4 is ruled work rather than an
inference. Top-down is narrowed to `hearth` with `SE-9(a)` held. Bottom-up holds given a person with a
stake. Vertical holds. Lateral holds.

**Horizontal is false.** `found` writes `contain` and `succeed` and never `hold`, so after P4 a faction
still cannot make a holding.

**Restated N-line:** *cut P4 and no hearth and no Site is ever created after world-gen. A founder gains
an address and a succession pointer — not a holding.*

### False N-lines — none. But the rows do not load.

Neither `(Rung, exists)` nor `(Site, exists)` has any other producer, and the attack that `work` or
`restore` supply growth fails as the proposal says: those move `condition`, never existence. The
objects are necessary. **As transcribed they fail three times — once at load, twice at the point of
use:**

1. **`requires_typed: {form: amount, …}` — this is the load refusal.** `data/requires.py:549-554`
   raises `SystemExit` on a form outside `REQUIRES_FORMS`, and `requires_forms` is closed at seven —
   `[existence, scalar_threshold, contain_path, cardinality, relation, own_ledger, basis]`
   (`rosters.yaml:911`). **`amount` is not a form; it is an operand.** The cell P4 wants already exists,
   as `transfer`'s: `scalar_threshold · of: from · scalar: stores · key: kind · threshold: amount`
   (`verb_table.yaml:517-523`). The set's own §3.2 notes the forms are closed at seven and calls a new
   one a grammar addition; P4 uses an eighth without noticing.
2. **`kind: timber|ore`.** Disjunction is **deliberately absent** — `rosters.yaml:906-907` says so in
   terms, and calls a combinator no cell uses the dead carrier `ID-13` refuses. No loader check
   enforces it; the cell would simply mean something no reader implements.
3. **`eligibility: [presence:<rung>]` alone.** The `presence:` placeholder is declined at the fold
   (`resolve.py:73-88`) and person-side (`options.py:166-168`), so **nobody can attempt either verb.**
   `work` shows the shipped pattern: `["own", "presence:<site>"]` (`verb_table.yaml:542`).

**Loader invariant 2 is declared and not implemented, and the violation is far larger than P4 says.**
The rule — *every matrix row with `RES` has ≥1 producing verb* — is real, and P4 cites it correctly at
`04_CODE_ARCHITECTURE.md:457`. What does not exist is any code that checks it: `verbs.py:204-304`
checks duplicate verb names, an untyped cell with no note, degree/emits band agreement, invariant 12
in both directions, `writes ⊆ MATRIX`, eligibility kinds, `scale` and `stratum` — and no producer
check. P4's own `[GAP]` about whether it fires resolves as **it cannot fire**, so P4 is a first
producer rather than the repair of a firing gate. And the scale: `hole_register.yaml:717` measures
**eleven** RES rows with no producing verb, six of them `Person` interior. P4 supplies two of eleven.

### E

**E-OVERHEAD.** In: two verb rows, two effects, one undeclared fixture (`condition = initial`), one
LOOP row. Out: nothing. Verbs **+2**, −0. Vocabulary +7, −0.

**The denominator:** an authored stake amount; `initial`; and `site_kinds` closed at
`[harbour, seam, body]` with a **required** row in two tables — `wear_per_season` and `band_floors`,
which raise on a missing kind (`fixtures.py:110-123`) — plus `site_yield`, checked only in the reverse
direction (`:125-129`), so a kind with no yield row loads and silently yields nothing
(`matter.py:188`). **Two required rows per new buildable kind, and one that fails quietly** — and the
quiet one is the one that matters.

**E-LEGIBILITY — pass.** *Grain in, a hearth out.*

### R

**R-VARIETY — real, and it is the first management choice in the set:** where to found, and what to
build.

**R-CHOICE.** Seat: a hearth-head with grain. Intent: *grow.*

| act | gain | cost |
|---|---|---|
| `found` | an address, a presence slot, a succession pointer — **and no yield without a Site** | 1 scene + the stake |
| `build` | a Site, and therefore yield | 1 scene + timber |

`build` dominates `found` for yield; `found` is worth a scene only for the slot it opens. That is a
real trade rather than a defect, and chain-founding is priced per scene.

**The Rung closer — sharpened.** P4 argues an empty hearth constrains nothing and grades the absence
CONVENTION. The grade is honestly said; **the argument under it is false.** `AX-6`'s defect is *a state
nobody can end* (`01_AXIOMS.md:394`) and no verb ends a Rung. Worse, the empty hearth **holds the
stake** in its `stores`: no eater draws there, and nobody present can `transfer` it out, because `from`
binds the actor's own containing rung. It is a **grain tomb** in an economy whose only source is yield.
And `w.rungs` grows monotonically while `sorted(w.rungs)` is walked every MATTER.

**Conservation — softened.** P4's regrade of `AX-4` to CONVENTION is right about `F10`, which weighs
its own probe season and never runs `found`. But P4's falsifier asserts *grain conserved across the
world*, and that **is** the named test the MECHANICAL grade requires. The compliance row was not
brought into line with the falsifier below it. Shippable; the grade is MECHANICAL on landing.

### S

**Pauses correctly: pass** — `uncontested_material` folds after `movement` and `binding_decision`.
**Methodology: pass** — `build` debits one side as a lawful consumption sink; `found` is two-sided.
Diagonal and the `presence` direction are uncarried until the eligibility cell is fixed.

**One half-write:** `holonic:371` makes `Rung.transmission` the field holding the `succeed` Tenure's id
(`carriers.py:523`). P4 writes the Tenure and never the field, so the pointer stays `None`.

### Repairs

1. Replace `form: amount` with `transfer`'s `scalar_threshold` cell. **This loads and does not finish
   the job:** `options.py:320-322` binds `amount` to the single global `default_transfer_amount` and
   `kind` to `store_kind_of(...) or default_store_kind`, so the founding stake becomes a transfer's
   default. The authored stake this evaluation charges to P4's denominator has no person-side channel —
   that is `H-94`'s remainder, and it is the substitution's real price.
2. Delete `timber|ore`; bind one `kind` from the referent, or ship two rows.
3. `eligibility: ["own", "presence:<rung>"]` — one word.
4. Take the `(Rung, exists) · [RES, CEN]` edit **P3 also needs** and de-found at CENSUS on zero presence
   and zero envelope, returning the stake to the parent. One edit closes P4's `AX-6` gap and P3's mint.
5. **`Rung.transmission` cannot be written as things stand** — `write_matrix.yaml` carries exactly five
   `Rung` rows (`dates`, `envelope`, `exists`, `stores`, `yield`) and no `transmission`, so declaring it
   in `found`'s `writes:` fails the load at `verbs.py:275-279` and writing it through the gate raises
   `Unspecified` at `world.py:321-324`. The field is on the class (`carriers.py:510-511, :523`) with no
   row behind it. Either add the matrix row, or drop the `succeed` edge and say the pointer is unset.

---

*Continues in `04_EVALUATION_part2.md` — P5, P6, P7, the substrate/politics seam, and what would
overturn each verdict.*
