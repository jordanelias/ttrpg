# 03 · THE SURFACE — the interface through which a player engages the game world

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Method: authored on **`opus`** per `CLAUDE.md` §10 — *"competing-considerations judgment; large-context synthesis … and the verify/judge stage that gates a result."* Not `fable`: §10 rules that tier **read-only audit / planner / guardrail, never synthesis or artifact authorship**, and this file is an artifact. Its adversarial pass was run against the tree, not against a sibling document.
## Scope: `ED-IN-0232`, lane **IN**. Every `path:line` below was opened with `sed -n` in this session before it was written. Its primary source — the analyse stage's D3 — self-reported eight invented addresses and a critic found sixteen wrong, so **no citation was carried forward unopened.** The repairs are the appendix.
## §0.2 grade: **`paper`.** Nothing here executes. §C.4 says what would move it and what the cheapest step is.

---

> **`04_CODE_ARCHITECTURE.md` §C.11, which is the clause this file exists to apply — and it refuses
> the obvious formulation by name:**
>
> *"⚠ **THE OBVIOUS FORMULATION IS WRONG AND MUST BE REFUSED BY NAME.** 'The player is not an actor,
> so `AX-2` does not reach them' fails immediately: **the player CONTROLS a person.** For an NPC,
> `choose` is the decision procedure; **for a player character the player IS the decision
> procedure**, so anything shown before they declare is shown inside a decision in the only sense
> `AX-2` cares about. A split on **who is looking** breaches the axiom."*
> — `architecture/meta/04_CODE_ARCHITECTURE.md` §C.11, lines 758-762
>
> **And Jordan's requirement, which is the measure:** *"Players need to have an interface with which
> to engage with the game world."*

Two sentences, and between them the whole problem. The interface is **required** and it is **inside a
decision**. There is no seat from which a surface may look at the world; there is only a person, what
they hold, and the arithmetic of what they hold.

⚠ **THE MEASUREMENT THAT SHOULD BE READ BEFORE ANY DESIGN CLAIM BELOW.** Run 2026-09-17,
`engine.season.harness.populated.build_realm(0)` at tick 0:

| measured | value |
|---|---|
| rungs · persons · offices · sites · propositions | 375 · 46 · 19 · 74 · 54 |
| **claims in all 46 ledgers** | **0** |
| `Record`s in the world | **0** |
| `w.dates` · `w.docket` · `w.crossings` | **0 · 0 · 0** |
| sites with anyone present at their rung | **0 of 74** |
| questions produced by `questions_for` across all 46 persons | **81 — every one `need` (Q4). Zero `date_due`, zero `claim_landed`, zero `band_crossed`** |

**The surface renders claims. There are no claims.** Every cell of every surface, for every person in
the corpus, is in the UNHELD state. That is the honest opening fact, it is stronger than *"nothing has
rendered a pixel"*, and it is why §C.4's cheapest step is the one it is.

---

# PART A · THE CLAIM

## A.1 · What a surface is a function of — the Render Law, attacked, and rebuilt

### A.1.1 · The law as the analyse stage proposed it

> ### ~~THE RENDER LAW~~
> ~~**A surface is a function of `(Person, View)` and takes no `World`.** This is enforceable by
> parameter list rather than by discipline, and the engine already does it for the chooser. The
> renderer is a second consumer of `assemble(person, question) -> View` — the same constructor, the
> same cap `K`, the same refusal.~~
>
> ⛔ **WITHDRAWN 2026-09-17, ON FOUR ATTACKS THAT ALL LANDED.** Kept in place per `CLAUDE.md` §4's
> correction convention, because the law's *intent* survives and its *mechanism* does not, and a
> reader who sees only the replacement will re-derive the same error. The replacement is A.1.3.

The law is **true of `choose` and false of the renderer**, and the difference is not a technicality —
it is four separate facts, each of which alone breaks the parameter-list argument.

### A.1.2 · The four attacks, each with the line that settles it

**Attack 1 · A `View` cannot carry a surface, because it is capped at twelve BUILT claim ids.**

`View.__slots__` is `("holder", "claim_ids", "question")` and the constructor refuses more than `k`
ids (`engine/season/state/carriers.py:217-220`). `k` is the fixture `view_k=12`
(`engine/season/data/fixtures.py:177`), read at `engine/season/loop/deliberate.py:69` and passed to
`assemble` at `:109`. And the ids are **built, not filtered** — `view_ids` returns *twelve of a
200-claim ledger* under one of three declared rules, and its own docstring says the choice of which
twelve is open:

> *"⚠ #353 SUPPLIES K AND NEVER SUPPLIES WHICH K, and 'built, not filtered' says what a View is
> NOT. `H-09` gives `K = 12`; nothing in the chain says which twelve of a 200-claim ledger a person
> brings to a question, and taking the last k — which every revision before `W5` did silently — is
> an invention."*
> — `engine/season/decision/questions.py:79-84`

**Not one of the four surfaces is derivable from twelve ids.** A place with nine sites, a ledger view
with thirty rows, a seat with six remit acts and nineteen executors, a scene with four figures — each
exceeds the cap on its own. A renderer handed a View would draw a twelfth of a person's knowledge and
call it their perceptual horizon.

**Attack 2 · The `View` is the wrong SHAPE, not merely the wrong size.** The cap exists because
`choose` answers *one question with a bounded working set* — that is what `assemble`'s own
`InstrumentDefect` message says the parameter is for (`questions.py:36-42`). A surface answers *what
do I know*, which is the ledger, unbounded. Widening `k` for the renderer would make the renderer's
`View` a different object from the chooser's under one name, which is `CLAUDE.md` §4's idempotence
trap exactly.

**Attack 3 · `assemble` is 4-ary, and the renderer's read list is longer still.**
`assemble(p, question, k, rule)` — `engine/season/decision/questions.py:22`. Live callers pass three
(`deliberate.py:109`). And `04 §C.3` types the whole DELIBERATE seam's IN side as **six things**, not
two:

> *"**In:** a frozen `PersonInterior`, a `View` of ids, two scalars, an int, `Question[]`, and the
> verb table's *declarations* — `requires` evaluated as **not known-false from the person's own
> claims.**"*
> — `04 §C.3`, lines 566-567

`04 §A.2`'s module table says the same from the other side: `decision/` **may read**
*"`PersonInterior`, `View`, `Sensation`, `budget`, `Question[]`, the table's declarations"*
(`architecture/meta/04_CODE_ARCHITECTURE.md:154`). So even the chooser is not a function of
`(Person, View)`. **The law mis-stated its own exemplar.**

**Attack 4 · UNHELD is a negative fact over the whole ledger, and a capped View cannot express it.**
The three-state cell's most valuable state — *"the bin at Gelbgrund · you have never looked"* —
asserts **no claim anywhere in this person's ledger matches `(subject, predicate)`**. Twelve ids
selected by a `recent` rule cannot distinguish *I hold nothing about it* from *it was not among the
twelve*. The one reader that answers the question correctly is `LedgerReader`, which scans the whole
list and returns `UNKNOWN` when nothing matches (`engine/season/queries/person_q.py:82-100`) — and it
takes **the ledger**, not a View.

**And two more reads the law's enumeration omitted.** `provinces_of` and `footprint` are
`World`-first resolver functions: `provinces_of(w, rung_id)` walks every `hold` Tenure over
territories in a subtree (`engine/season/queries/world_q.py:345-397`) and `footprint(w, faction)`
unions *"the rungs it holds, plus the rungs its members sit in"* (`:254-272`). The analyse stage drew
both on the place surface — as a coalescence of territory outlines and as boundary-versus-occupancy —
while asserting the renderer takes no `World`. Those are god-state reads. They are not in the
replacement law's licence list and the marks they were drawn for are withdrawn in A.3.4.

### A.1.3 · The replacement — THE SURFACE LAW, three licences, enumerated and closed

> ### **THE SURFACE LAW**
> **A surface is a function of `(PersonInterior, Ledger, Sensation, Reads)` where `Reads` is a
> CLOSED, ENUMERATED list of three licensed kinds and nothing else.** Every displayed fact resolves
> to one of the three, and the list below is the whole of it. A fourth kind is a design change and
> needs a ruling, not a panel.
>
> | licence | what it admits | why it is not privileged access | grade |
> |---|---|---|---|
> | **L-1 · my own ledger** | every `Claim` I hold, with `source`, `when`, `confidence`, `round` | it is mine. `04 §B.2`'s `F8` carve-out admits a resolver-side read of **the actor's own ledger and no other** (`verb_table.yaml:651`) | **STRUCTURAL** — `LedgerReader` takes `claims`, not a `World` (`person_q.py:79-80`) |
> | **L-2 · `Sensation`'s two scalars** | `subsistence` and `standing`, and nothing else | *"EXACTLY TWO SCALARS, and it is the ONLY bridge from world truth into `choose`"* (`carriers.py:161-162`); `sense` is *"the ONE non-decision function permitted a World"* (`deliberate.py:465-466`) | **CONVENTION** — `04` grades the two-scalar rule *"convention — the named residual risk"* (`carriers.py:174-176`) |
> | **L-3 · state I am an endpoint of** | a `Tenure` whose subject or object is me; the remit of a seat I hold; the establishment I employ; my own `capability`, `convictions` and `stance` | an edge is not a fact about the world, it is half of me. This is already a witness channel's predicate: `_ch_witness_key` admits `pid` where a live `knot` has `pid` at either end (`epistemic.py:336-341`) | **MECHANICAL** — by path scan; no type forbids it |
>
> **And the ARITHMETIC of any value drawn from L-1..L-3 is owed, by `04 §C.11`:**
> *"The engine owes the ARITHMETIC of what the character already holds, and nothing else"*
> (`04 §C.11`, line 765), through `explain(p : PersonInterior, v : Value) -> Derivation` — *"person_q.
> NO World parameter"* (`:775`). The derivation is *"assembled from the holder's own `Claim` rows —
> their `source`, `confidence` and `when` — and from nothing else"* (`:780-781`).

**L-3 is the clause the withdrawn law had no slot for, and it is why the law had to be rebuilt
rather than patched with an exception list.** The analyse stage found the hole and named it — *"a
`knot` Tenure is world state I am an endpoint of … the Render Law as written has no slot for my own
edges"* — and proposed carrying it as an exception. An exception list to a law stated as *takes no
`World`* is the law abandoned while its sentence stands, which `CLAUDE.md` §0.05's test catches: if
the law were deleted, would the surface behave differently? No — the surface would behave exactly as
the exception list says. **So the exception list IS the law.** Stating it as three positive licences
makes the grade per licence honest (one STRUCTURAL, one CONVENTION, one MECHANICAL) where a single
"BY TYPE" claim was STRUCTURAL for all three and true for none.

**What is NOT licensed, and is refused by name.** Any `World`-first function in
`engine/season/queries/world_q.py`: `presence`, `verbs`, `footprint`, `provinces_of`, `density`,
`sovereign_fraction`, `establishment_of`, `judging_set`, `home_of`, `occasioned_by`, `hold_force`,
`lateral`. Every one carries `TRACE.query(..., "resolver")` on its first line, which makes the
refusal **observable rather than asserted**: a renderer that reached one would appear in the trace as
a resolver query, and the falsifier in PART D is exactly that scan.

⚠ **THREE of the twelve are the hard cases, and two of them are surfaces the analyse stage drew.**
`establishment_of` reads the Office's own `establishment` field (`world_q.py:399-415`) — admissible
under **L-3**, because a seat I hold is state I am an endpoint of, and *"the named persons the office
employs"* are people I hired. `verbs(w, site, floors)` is **not** admissible under any of the three
and is dealt with at A.3.5, where it costs the design its single most load-bearing display.
`presence(w, rung)` is not admissible either — and the repair is narrow: **presence at my OWN rung is
a fact I observe by standing there, so the surface reads it as a claim that `WITNESS` deposited**,
never as the query. That is not a softening: `_ch_co_located` is the channel that puts the room in my
ledger, and the corpus's 0-of-74 presence measurement means the room is empty today anyway.

### A.1.4 · Candidates for what the surface is a function of

| candidate | who owns it | verdict |
|---|---|---|
| `(Person, View)`, enforced by parameter list | the analyse stage's Render Law | **REFUSED.** Four attacks land (A.1.2). The `View` is capped at twelve **built** ids; UNHELD is a negative fact over the whole ledger; `assemble` is 4-ary and `04 §C.3`'s IN list is six things |
| `(Person, View)` as an aspiration **plus an enumerated exception list** | the analyse stage's own fallback, and the reconciliation's first option | **REFUSED, and this is the interesting refusal.** An exception list to a law of the form *takes no X* is the law deleted with its sentence kept. It also grades three different things STRUCTURAL when one is CONVENTION and one is MECHANICAL |
| `(PersonInterior, Ledger, Sensation, Reads)` with `Reads` closed at three positive licences | **this file** | **ADOPTED.** Each licence carries its own grade and its own citation; the refusal is observable in `TRACE` rather than asserted |
| a `RenderState` object built at a barrier, like `queries/cache` | nobody — proposed and refused here | **REFUSED.** `04 §A.2` gives `queries/cache` *"barrier indexes … at a barrier only"* with **any store** as its read scope (`:153`). A render cache built from that scope is god-state with a lifetime |
| whatever the Godot scene tree finds convenient | — | **REFUSED.** `04 §A.2`: `port/` is *"the Godot shell; nothing under it is simulation"* (`:137`). A shell that reads the world is simulation |

> ### RULED: the withdrawn law's INTENT is kept and its MECHANISM is replaced.
> **`AX-2` is not enforced on the renderer by a parameter list. It is enforced by a closed,
> three-member read licence whose violations are observable in `TRACE`, and it survives for the
> renderer as DISCIPLINE plus a scan — which is exactly what the withdrawn law claimed to replace.**
> Said plainly because the analyse stage's strongest sentence was *"the alternative — a renderer that
> **may** see the world and is asked not to — is `AX-2` as a code review comment,"* and that sentence
> is **right**, and the honest position is that the code review comment is what we have, with a
> grade of MECHANICAL and a named scan, not STRUCTURAL. `AX-2` itself:
> `architecture/meta/01_AXIOMS.md:100-103`; the axiom's own note on why it is axiomatic, `:105-107`.

---

## A.2 · THE HARD EDGE — the surface is built around ATTENTION, not capability

**The interface can only offer what the engine raises a question about.** `questions_for` has four
sources and nothing else, and `Question.__post_init__` refuses a fifth at construction:

> *"§F1 — a question is produced by these sources and by nothing else. V2 said THREE and was wrong by
> one; the roster is where a fifth would be argued for"*
> — `engine/season/state/carriers.py:259-260`

| # | source | the asker | the engine's condition, at the line |
|---|---|---|---|
| Q1 | `date_due` | **an institution** — a calendar with my name in it | a `Date` at/past `due_at`, unfired, whose holder is me or something I hold — `engine/season/queries/world_q.py:476-480` |
| Q2 | `claim_landed` | **a person** — news about me or mine | `(c.when, c.round) >= floor and (c.subject == p.id or c.subject in mine)` — `:491-494` |
| Q3 | `band_crossed` | **the world** — a threshold crossed where I stand | `if who == p.id or (at is not None and p.id in presence(w, at))` — `:517-518` |
| Q4 | `need` | **myself** — a standing commitment | a live `commit` Tenure whose object is an OUGHT `Proposition` — `:524-528` |
| Q5 | `purview` | **a place I answer for** — proposed by the reconciliation, not built | a crossing or landed claim at a rung under `under_purview(seat)`, claim-gated. One row on an OPEN ordered roster (`engine/season/rosters.yaml:249-270`) |

**Myself · an institution · a person · the world · a place I answer for.** The set is closed along the
right axis, and that is the design position rather than a consolation: **what the player is offered is
what their character currently has cause to consider.** `AX-2` arriving at the option set, not at the
fact display.

### A.2.1 · And the closure is the good half. Here is the bad half, measured.

⚠⚠ **MEASURED 2026-09-17, and it is worse than the analyse stage reported, in the direction that
flatters.** The stage wrote that of the four routes by which a player *causes* a question, *"the only
one of the four the fold can actually carry is `dispatch`."* I re-ran both halves of that claim —
formability person-side, and resolvability by the fold — and they do not overlap:

```
python -c "from engine.season.loop.driver import resolvable_verbs; ..."
  verb table rows                                            38
  resolvable by the fold                                     18
  person-side formable (an `own` alternative in eligibility)  28
  BOTH formable and resolvable                               13
```

The thirteen, in full, because the list is the player's whole vocabulary today:
`create_record · examine · interview · move · reconstruct · release · research · speak · surveil ·
tell · transfer · utter · work`.

**Not one of the thirteen is an act of office.** Every `remit:`-eligible row declines person-side at
`engine/season/decision/options.py:163-165` — `remit:<act>` is *"unevaluable person-side (H-71, the
office's remit is not the holder's state)"* — so `confer`, `convene`, `determine`, `dispatch`,
`establish`, `issue`, `levy`, `open_case` and `revoke` form **no candidate for anybody**. And the four
routes to a new question:

| route to attention | verb row | person can FORM it? | fold can CARRY it? |
|---|---|---|---|
| send somebody | `dispatch`, `verb_table.yaml:197-208`, eligibility `remit:dispatch` | **NO** — `remit:` declines | yes |
| set a date | `convene`, `:155-165`, eligibility `remit:convene` | **NO** — `remit:` declines | yes |
| petition | `petition`, `:395-405`, eligibility `own`, *"no dedup, no cap, no per-venue limit (§26.3)"* | yes | **NO** — no effect body |
| swear | `commit`, `:115-129`, eligibility `own`, `grade: ruled` | yes | **NO** — no effect body |

> ⚠ **SO ZERO OF THE FOUR ROUTES IS BOTH FORMABLE AND RESOLVABLE, AND `dispatch` — the one the
> analyse stage banked — IS THE ONE NO PERSON CAN EVEN FORM.** The stage read the resolvability list
> and not the eligibility column, which is `CLAUDE.md` §0.1 pt 3's *"X works today"* failure: it
> opened the declaration and not the call site. Corrected here by running both gates over all 38 rows
> rather than checking the verb it had already chosen.

There are exactly **eleven `@effect_for` registrations** in the package — `confer · convene ·
create_record · destroy_record · kill/wound · move · release · revoke · transfer · utter · work` — and
the 20 unresolvable rows are the rows with no effect body plus `thread_read`, whose own row says why:
*"with no typed cell and no `REQUIRES_PREDICATES` entry this verb is NOT in `resolvable_verbs()`, so it
is a row that exists and cannot yet be attempted"* (`verb_table.yaml:697`).

### A.2.2 · The answer: the surface's primary control is CAUSING a question, and one of the five causes is one effect body away

A surface that renders the engine's Candidate list is a menu. The escape is not a fifth question
source bolted on for the player — it is that **four of the five askers are things a player can
CAUSE**, so the surface's top-level affordance is *making a matter askable*, in four shapes, and the
candidate list is what falls out.

| what the player does | which asker it manufactures | whose attention it buys |
|---|---|---|
| **send somebody** (`dispatch`) | their Q3 becomes my Q2 when they tell me | mine, at one remove and one season late |
| **set a date** (`convene`) | a Q1 for everyone in the judging set | everyone's, on a calendar |
| **petition** | a Q1 on somebody else's docket | a seat-holder's, unfiltered and undeduplicated |
| **swear** (`utter` then `commit`) | my own Q4, every season until it ends or I die | **mine, permanently** |

⚠ **AND THE CHEAPEST OF THE FOUR IS ONE EFFECT BODY, WHICH IS THE ONE RECOMMENDATION IN THIS SECTION.**
`utter` is **formable and resolvable today** (`verb_table.yaml:746-754`; eligibility `own`, requires
`—`, writes `Proposition.exists`, and `@effect_for("utter")` exists). `commit` is **formable, `grade:
ruled`, and lacks only an effect body** (`:115-129`; requires *"the Proposition exists (immutable,
§14)"*, writes `Tenure.since`). Its write is a Tenure whose subject **is** the actor, so by the
reconciliation's own Arc-2 rule it is not downstream of the Arc 2 gate. So:

> **The player can SAY what they want and cannot SWEAR to it, and the distance between those two is
> one `@effect_for("commit")`.** Once it lands, `questions_for`'s Q4 already reads it (`:524-528`) and
> the corpus's 81 standing questions prove the route carries — they are all Q4. **This is the one
> place where the surface's deepest affordance is also the cheapest build in the file.**

Three consequences, all free and none of them new mechanism:

1. **An uttered proposition is a public act.** It emits `proposition.uttered` and is witnessed, so
   declaring an ambition deposits claims in whoever the fan-out admits. Ambition is information you
   give away.
2. **Others may commit to your proposition, and that IS a faction.** A faction is *"a Proposition plus
   its `commit` edges"* — `members(w, faction)` is the `commit` count (`world_q.py:200-211`; §14.2's
   own line, *"A faction IS a Proposition plus its `commit` edges"*, at `:181`). So the interface for founding a movement is: say the thing, and see who
   commits. No faction-creation screen, and none available: `04 Part D` row 1 makes an institution
   acting STRUCTURAL-impossible — *"the type has **no verbs**"* (`:930`).
3. **A commitment you cannot keep is a question you keep failing to answer.** Better than a quest log
   with a red cross, and it is Q4's own stated purpose — *"which is what makes an NPC with an ambition
   act in a quiet season"* (`:526-527`).

### A.2.3 · The named-absence rule — what the surface says about what it cannot offer

`AX-2` forbids explaining *why the world withheld an option*. What it permits is **naming the shape of
my own ignorance**, because that is arithmetic over my ledger. `04 §C.11` licenses exactly this and
draws the line precisely:

> *"**Hidden actors are hidden in their EXISTENCE, never in their ARITHMETIC.** 'Subsistence fell by 1
> from a cause you cannot name' is admissible, because the character can already see the fall; what
> they are additionally given is that it has an author they do not know. **A preview naming the author
> is a breach; one saying the effect is unattributed is not** — and the second is what makes
> investigation worth a scene."*
> — `04 §C.11`, lines 783-787

**One rule, no new object:** for anything the player cannot form, the surface names the one thing that
would make it formable — and all three cases are already traced by the engine.

| why I cannot form it | what the surface names | where the engine already traces it |
|---|---|---|
| the eligibility clause declined | *"by the remit of an office you do not hold"* | two `TRACE.note` declines, `options.py:164-165` and `:167-168`, plus the `hold:<kind>` placeholder decline at `:159-160` |
| an operand would not bind | the blank: *"you have nothing in mind to send"* | *"`operands_for` traces every decline, so the count is measurable rather than inferred from a verb's absence"* — `options.py:58-59` |
| **no question names this subject** | *"nothing has made you think about Gelbgrund. You have sent nobody, and nobody has come."* | **[DESIGN]** the complement of `questions_for`'s referent sets over what the player can see. One derived list, no carrier, no store |

⚠ **AND THE STRUCK-AFFORDANCE DISPLAY COLLIDES WITH THE EXISTING UI CORPUS, WHICH I RULE RATHER THAN
IGNORE.** `valoria_ui_ux_v4_1.md:63` states Oath II as *"**Only surface UI elements the character can
use**"*, and its violation test 1 at `:65` is *"Does the UI display a control for a capability the
character does not currently have (e.g., a Thread sight toggle on a TS 0 character)? If yes → FAIL."*
Read literally, that fails the display above. **It does not apply, and the reason is in the engine's
vocabulary:** test 1's referent is a **capability** gate, and `eligibility_kinds` is
`[own, remit, hold, presence]` with the roster note *"⚠ `capability` IS NOT AND MUST NEVER BE A
MEMBER … 'capability supplies dice and GATES NOTHING'"* (`engine/season/rosters.yaml:152-160`). The
struck affordance's gate is an **eligibility** clause — a public fact about an office anybody in the
world can know — not a hidden capability. Oath II survives; its worked example has no referent in this
model.

| candidate framing for the option set | who owns it | verdict |
|---|---|---|
| capability — *what this character is able to do* | `valoria_ui_ux_v4_1.md:63-65`, Oath II | **REFUSED.** `capability` *"GATES NOTHING"* and is forbidden from `eligibility_kinds` (`rosters.yaml:152-153`). There is nothing to render |
| the Candidate list — *what the engine computed for me* | `opening_set`, `options.py:35-104` | **REFUSED as the FRAME, kept as the content.** Rendering it alone is the menu failure mode, and it is bounded by one question's referents (clause 3) |
| attention — *what I currently have cause to consider*, with the four causes as player acts | **this file**, on the analyse stage's reframing | **ADOPTED** |
| a fifth question source for the player | refused by `Question.__post_init__` (`carriers.py:259-260`) | **REFUSED.** A fifth is a roster argument, and Q5 `purview` is the one under argument (sibling 01) — a seat's attention, not a player's |

> ### RULED: the frame is ATTENTION and the top-level affordance is CAUSING A QUESTION.
> **The four askers are `dispatch · convene · petition · commit`, all four are existing verbs, and
> today zero of them is both formable and resolvable (measured, A.2.1). The named cheapest repair is
> `@effect_for("commit")`, which makes the self-authored goal live and is unflagged by the Arc-2 rule.**
> Cited to `world_q.py:439-552` for the sources, `carriers.py:263-265` for the closure,
> `verb_table.yaml:115-129` and `:746-754` for the two halves of the swearing route.

---

## A.3 · THE SURFACES — the cut re-attacked, and the three readings a critic found unreachable

Nine candidates entered; four survive. The cut is kept, and each survivor now names a **recorded
collision** rather than a convenience — which is what makes it a cut and not a preference.

| candidate surface | who owns the claim that it is needed | verdict |
|---|---|---|
| **THE PLACE** — one surface, any rung | the containment ladder itself | **KEPT.** Cut it and there is no presence, no `co_located` witnessing, no site option set, and the cohort/person distinction that *is* a governor's blindness has no surface. `Person` docstring: *"A COHORT IS A PERSON AT weight > 1. ONE CLASS (S9.1)"* (`carriers.py:373`) |
| **WHAT I KNOW** — the ledger, three ways | `L-1`, and `Event.causes[]` | **KEPT.** A causal chain crosses places and seasons, so it cannot live on a place; and two disagreeing sources have nowhere else to display |
| **THE SEAT** — a post's working surface | `H-71`, a recorded collision with **no relocation available** | **KEPT, NARROWED.** The docket could live at the place and the standing list in the ledger; what cannot move is the **remit** — *"two holders of one office share one remit, so it is not the person's state to move"* (`options.py:121-123`). **The narrowed N-line is: the seat exists because an OFFICE is a third thing, neither person nor place.** The docket and standing list sit on it as placement, not justification |
| **THE SCENE** — a resolution in progress | `Claim.round` | **KEPT at MEDIUM confidence.** `round` is a real second clock — *"the scene tick subdivides a season into rounds … `when` still says WHICH SEASON … `round` says WHICH ROUND WITHIN it"* (`carriers.py:131-136`) — and `round` is *"THE ONLY CARRIER FIELD `U2` ADDS, AND THE ONLY ONE IT MAY ADD"* (`:131`). But a scene is also always *somewhere*, so this may be one unification short. Reported at MEDIUM, not banked |
| four typed layers — Peninsula / Province / Settlement / Scene | `valoria_ui_ux_v4_1.md:339-345` | **CUT, FREE.** A building **is** a `hearth` and a quarter **is** a `community` — *"Neither is a new kind: the ladder already had both and the corpus never used either"* (`engine/season/venues.yaml:21-25`). Zoom is `parent_of` / `descendants` (`world_q.py:48,54`) |
| a docked, priority-sorted Scene Slate | `valoria_ui_ux_v4_1.md:295-303`, with a 12-entry overflow rule and a `+N more` expander at `:299` | **CUT, FREE.** A `Question` carries `referents` (`carriers.py:251`) and every referent has a place, so the list's content is already spatial, and the ordering is already computed by `questions_for`'s own sort (`world_q.py:548-549`). **What survives is a camera control**, not a surface: *show me my questions* |
| a character sheet of attributes and derived stats, plus a Codex with four knowledge states | `valoria_ui_ux_v4_1.md:977-1001` and the Codex at `:1003-1019` | **CUT, FREE.** `standing_of` **is** the gap between told-about-me and my own firsthand claims about me (`options.py:443-464`), so the sheet's most important row is already a two-set comparison over the ledger. What did not die: **my own capability, shown as bands, because it is mine** — one panel on the self filter |
| a cutscene queue with priority tiers and a no-nesting clause | `valoria_ui_ux_v4_1.md:153-162` | **CUT, and it falls out of A.7 rather than standing on its own N-line.** Claims land at WITNESS and WITNESS is a barrier, so there is nothing to nest |
| a policy register and a projects board, separately | the analyse stage's own first list | **CUT, FREE.** From the surface's side both are *a thing I set running, with named persons, that reports back late and partially*. The differences are **columns** — compliance states for one, stage terms for the other. Both specified separately at A.4.3 and A.5.2 |

### A.3.1 · The cell law — four states, and the fourth is NOT computed today

| state | ledger condition | how it draws |
|---|---|---|
| **HELD** | a claim exists whose `(subject, predicate)` this cell is | the value, plus source · age · confidence |
| **STALE** | a claim exists and its `when` is old, or its `confidence` has decayed | the value, dimmed, age foregrounded — *"eleven measures, per the reeve, two seasons back"* |
| **UNHELD** | no claim anywhere in this ledger matches | a **named absence** — *"the bin at Gelbgrund · you have never looked"* |
| **CONTRADICTED** | two claims match and disagree | a **split cell**, both shown, neither marked false |

Three readings, each load-bearing, and the third is a correction to the analyse stage:

- **CONFIDENTLY WRONG must stay indistinguishable from CONFIDENTLY RIGHT.** The surface never marks a
  claim false. `AX-2`'s own note says why it is axiomatic: *"the axiom that makes a false conclusion
  indistinguishable from a true one to the person holding it, which is the condition every deception
  mechanism in the game rests on"* (`01_AXIOMS.md:105-107`). A correctness mark deletes every deception
  mechanism in the game at once.
- **UNHELD is not NOTHING THERE.** A place drawn with no people in it means *I hold no claim about who
  is there*, and the label says that, not "empty".
- ⚠ **CONTRADICTED IS A NEW READING, NOT A DISPLAY OF SOMETHING COMPUTED — and the analyse stage
  claimed the opposite.** It wrote: *"This is not an addition: `agreement(told, own)` already pairs
  claims by predicate and returns `(agreements, disagreements, paired)`. The disagreement count is
  computed; the interface displays what is computed."* **Opened and measured:** `agreement` has exactly
  **one caller in the entire tree** — `standing_of` at `options.py:463` — which filters
  `c.subject == p.id` on both sides, and pairs only over `PERSON_PREDICATES`, a five-value roster
  (`rosters.yaml:281`: `[heritage, grade, church_standing, office, residence]`). So the pairing exists
  **only for claims about oneself, over five person predicates.** Nothing computes disagreement about a
  bin, a site, a policy or another person's whereabouts. `LedgerReader._best` does return *"most recent,
  then most confident"* and leaves the loser in the list (`person_q.py:82-96`), so the split cell is
  **readable** — it is one derived enumeration over the ledger, no store, no field. It is an addition
  of one reading, and it is counted as one in PART B rather than smuggled as free.

### A.3.2 · Reading 1 of 3 the critic found unreachable — COMPARING TWO PLACES

**The problem.** *Is Gelbgrund worse off than Erzbach?* Both places are subjects in one ledger, so the
comparison is person-side and adds no read. What is missing is a **pairing vocabulary**: `agreement`
pairs by predicate over `person_predicates`, and there is no `place_predicates` roster.

**And one is not needed, because the vocabulary is derived rather than authored.** The `W-B`
observation deposit writes claims in the `requires` namespace — `LedgerReader`'s own vocabulary is
*"`stores:<kind>` / `condition` / `contain.path:<to>` / `claim.held` / `exists:<kind>` / a relation
stem"* (`engine/season/loop/witness.py:220-221`), and those predicates are **derived from the verb's
typed cell**, not from a roster: *"These claims are in that namespace by construction, because the
Observation's predicate is derived from the cell"* (`:225`).

> **[DESIGN] The comparison is `agreement`'s shape with both arms re-bound: `pair(claims about A,
> claims about B)` over the predicates present in BOTH, with the unpaired predicates named as the
> reason the comparison is thin.** *You hold `stores:grain` for both, four seasons apart. You hold
> `condition` for Erzbach's harbour and nothing for Gelbgrund's.* One derived list; zero new rosters;
> **and the honest output of a two-place comparison is usually a report about the reader**, which is
> the correct answer and is `AX-2` rendered as a feature.

### A.3.3 · Reading 2 of 3 — A POLICY'S COMPLIANCE ACROSS A PROVINCE

**The axis is wrong, and correcting it dissolves the problem.** `issue`'s `requires` cell is verbatim
*"scope enumerates executors, not places (§37.1)"* and its `scale_note` says *"a Dispensation's `scope`
enumerates executors — §37.1 — so its reach is the domain the issuer governs"*
(`engine/season/verb_table.yaml:258, 261`). So a policy has no provincial axis: **it has a list of
people.** "Compliance across a province" is a grouping of that list.

> **[DESIGN] Group the executor list by where I last heard each of them was — and `residence` is
> already a declared `person_predicate` (`rosters.yaml:281`), so the grouping key is a claim I hold
> about each man, never `home_of`** (which is resolver-side, `world_q.py:150-170`). The unplaced
> executors go in a named bucket: *"three men you cannot place."* The provincial shape is an artifact
> of my own knowledge of my own staff, which is what a governor actually has.

⚠ **Free, in the sense that it needs no new object, and NOT free in the sense of working today.**
`establishment_of` reads *"the named persons the office employs. Finite, contested, durable"*
(`world_q.py:399-400`) and *"HOW MANY PERSONS AN OFFICE EMPLOYS IS `H-34`, GRADED `assumption`, AND IS
NOT SUPPLIED HERE"* (`:407-408`). And the world has 19 offices and 0 `Record`s, so there is no
dispensation to be compliant with.

### A.3.4 · Reading 3 of 3 — FINDING A PERSON YOU HAVE NOT MET

`opening_set`'s clause 3 is `subject in referents(q)` (`options.py:48`), so **the reachable subjects are
the referents of my questions and nothing else.** A person nobody has mentioned is not a referent and
cannot be acted on — which is correct, and is the axiom rather than a gap.

The three routes by which a stranger becomes a referent, and their live status:

| route | mechanism | live? |
|---|---|---|
| somebody tells me about them | Q2, `(c.subject,)` is the referent (`world_q.py:494`); a `told_by` claim's subject is a person id | **the only live one**, and it is the answer: *you find a person by asking someone* |
| they are a matter on a docket I sit on | Q1's referents are the docket's matters (`:479-480`) | dead — `w.dates` is 0 and `calendar()` writes `Date.fired` with no `emits=`, so Q1's provenance walks nowhere (`world_q.py:571-579`) |
| I swear something about them | Q4's referent is `(prop.subject,)` (`:527-528`) | one effect body away (A.2.2) |

**And `interview` is the verb, and it is formable AND resolvable** (`verb_table.yaml:643-657`;
eligibility `own`; requires only *"the person questioned exists"*). So a player may interview a person
they have never met, provided somebody mentioned them. ⚠ Its own row records what the precondition
canon *wants* and cannot have: *"a witness is someone who HOLDS a claim on the matter, and `04 §B.2`'s
corrected `F8` carve-out admits a resolver-side ledger read for THE ACTOR'S OWN ledger and no other …
So `own_ledger` cannot be pointed at the person being questioned, and existence is the strongest clause
the grammar admits here"* (`:651`). **That is `AX-2` refusing to tell you whether the man you are about
to question knows anything**, and it is right.

### A.3.5 · What the place surface must NOT draw, and the one display this costs the design

Three withholdings, each with the line that forces it:

- **No aggregate.** `Rung.__init__` refuses an undeclared field with the law quoted inline —
  *"a Rung owns NO social aggregate: no norms, no densities, no reputation, no unrest, no legitimacy.
  EVERY ONE IS A QUERY"* (`carriers.py:586-587`) — and `__setattr__` repeats it against assignment
  (`:589-595`). A number the model refuses to store must not be invented by the renderer. This kills
  the P/D/O node bars and the derived-settlement map's three stat bars outright. ⚠ The GRADE is not
  STRUCTURAL: `04 §B.3` rates the no-aggregate rule *"STRUCTURAL at the type … **CONVENTION at the
  schema edit** … **MECHANICAL against the accidental case, CONVENTION against the deliberate one**"*
  (`:240-244`). A session can add the field; what it cannot do is add one without a matrix row.
- **No faction colour fill, and no province outline.** Both were drawn by the analyse stage from
  `footprint` and `provinces_of`, which are resolver-side (`world_q.py:254-272`, `:345-397`) and are
  **not in the licence list** (A.1.3). The distinction `footprint` records — *"Holding is title;
  presence is reach"* (`:257-258`) — is real and is exactly what a player cannot see from outside.
  What the surface may draw is what my claims say: *the banner on the gate at Erzbach, per the
  carter, last spring.*
- ⚠⚠ **AND THE SITE OPTION SET — THE DESIGN'S MOST LOAD-BEARING DISPLAY — SURVIVES ONLY AS A CLAIM,
  BECAUSE THE QUERY IS RESOLVER-SIDE AND ITS VOCABULARY IS NOT THE PLAYER'S.** Two separate facts,
  measured:
  1. `verbs(w, site, floors)` is `World`-first and traced `"resolver"` (`world_q.py:133-136`). **And it
     has no caller under `loop/` — MEASURED 2026-09-17: five callers, all in
     `engine/season/harness/probes.py` (`:678, :683, :1509, :1515, :2241`), zero elsewhere.** The rule
     is ruled — `Site.condition` *"is PRIMARY STATE, a FIXED-POINT INT (S48), and it GATES VERBS
     (S12.1)"* (`carriers.py:412-413`) — the function exists, and nothing joins them.
  2. ⚠ **AND THE SET IT RETURNS IS NOT A SET OF VERBS.** `band_floors`' inner keys are **site-use**
     names, and the roster says so: *"The verb keys are SITE-USE verbs (what the site is good for at
     that condition), NOT verb-table rows"* (`rosters.yaml:1182-1183`). The live cells are
     `bulk_shipping`, `fishing`, `deep_mining`, `surface_gleaning`, `full_operations`, `limited`,
     `withdrawal_only` (`:1190-1200`). **None of the seven is a row in the 38-row verb table.** The
     verb table's own retraction note says it in terms (`verb_table.yaml:765`), and `WorldReader`
     substitutes `min(floors.values())` for `work` with the reading declared, because *"the site-USE is
     an operand neither the act nor `requires_operands` carries (`H-94`)"* (`world_q.py:702-730`).

  > **So there is no bridge from what a place AFFORDS to what a player may CHOOSE, and the analyse
  > stage's four best displays all cross that missing bridge**: the struck affordance, the verb that
  > left, the policy-as-floor-edit, and reading a government off a room. Stated here rather than in the
  > grade alone, because §0.1 pt 3 says the claim and its support are different objects.
  >
  > **[DESIGN] The repair is a site-use operand, not a display.** When `H-94`'s operand lands, a
  > `work` act names WHICH use it intends, `floors[use]` replaces the `min` substitution and *"the
  > reading collapses to the prose"* (`world_q.py:729-730`) — and at that moment a site-use becomes a
  > blank on a candidate sentence, which is where the player was always going to meet it. Until then
  > the place surface draws **site uses as claims** (*"they were still shipping bulk out of Erzbach at
  > Michaelmas"*), which is L-1 and is honest, and draws **no option set at all**.

> ### RULED: four surfaces, and the cut holds — but the place surface ships WITHOUT an option set.
> **The place · what I know · the seat · the scene.** The five cuts each name the existing carrier that
> makes them unnecessary. The cell law gains a fourth state, CONTRADICTED, counted in PART B as one new
> reading because `agreement`'s single caller is `standing_of` and pairs only claims about oneself
> (measured, A.3.1). **And the site option set is deferred to `H-94`'s operand rather than drawn from
> `verbs()`**, because the query is resolver-side, has no loop caller, and speaks a vocabulary with
> zero overlap with the verb table. Cited: `world_q.py:133-136`, `rosters.yaml:1182-1200`,
> `verb_table.yaml:765`, `carriers.py:412-413`.
