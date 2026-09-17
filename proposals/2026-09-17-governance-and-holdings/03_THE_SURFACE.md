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

The law is **true of `choose` and false of the renderer**, and the difference is not a technicality —
it is four facts, each of which alone breaks the parameter-list argument.

| # | attack | the line that settles it |
|---|---|---|
| **1** | **A `View` cannot carry a surface: it is capped at TWELVE claim ids.** The constructor refuses more than `k` (`engine/season/state/carriers.py:217-220`); `k` is the fixture `view_k=12` (`engine/season/data/fixtures.py:177`), read at `engine/season/loop/deliberate.py:69` and passed at `:109`. **Not one of the four surfaces is derivable from twelve ids** — a place with nine sites, a ledger view with thirty rows, a seat with nineteen executors, each exceeds it alone. A renderer handed a View would draw a twelfth of a person's knowledge and call it their perceptual horizon | *"⚠ #353 SUPPLIES K AND NEVER SUPPLIES WHICH K … nothing in the chain says which twelve of a 200-claim ledger a person brings to a question, and taking the last k — which every revision before `W5` did silently — is an invention"* — `engine/season/decision/questions.py:79-84`. The ids are **BUILT, not filtered** |
| **2** | **Wrong SHAPE, not merely wrong size.** The cap exists because `choose` answers *one question with a bounded working set* — which is what `assemble`'s own `InstrumentDefect` says the parameter is for (`questions.py:36-42`). A surface answers *what do I know*, which is the ledger, unbounded. Widening `k` for the renderer would make the renderer's `View` a different object from the chooser's **under one name** | `CLAUDE.md` §4's idempotence trap: a word must yield the same meaning read cold in a later session |
| **3** | **`assemble` is 4-ary, and even `choose`'s IN side is six things — so the law mis-stated its own exemplar.** `assemble(p, question, k, rule)` at `questions.py:22`; live callers pass three | *"**In:** a frozen `PersonInterior`, a `View` of ids, two scalars, an int, `Question[]`, and the verb table's *declarations*"* — `04 §C.3`, lines 566-567. And `04 §A.2`'s module table gives `decision/` the same six as its read scope (`:154`) |
| **4** | **UNHELD is a negative fact over the WHOLE ledger, and a capped View cannot express it.** *"the bin at Gelbgrund · you have never looked"* asserts **no claim anywhere in this ledger matches `(subject, predicate)`**. Twelve ids chosen by a `recent` rule cannot distinguish *I hold nothing* from *it was not among the twelve* | the one reader that answers correctly is `LedgerReader`, which scans the whole list and returns `UNKNOWN` on no match (`engine/season/queries/person_q.py:82-100`) — **and it takes the ledger, not a View** |

**And two reads the law's enumeration omitted, both of which it then drew surfaces from.**
`provinces_of(w, rung_id)` walks every `hold` Tenure over territories in a subtree
(`world_q.py:345-397`) and `footprint(w, faction)` unions *"the rungs it holds, plus the rungs its
members sit in"* (`:254-272`). The stage drew both — a province as a coalescence of outlines, title as
boundary against presence as occupancy — **while asserting the renderer takes no `World`.** Those are
god-state reads; the marks they were drawn for are withdrawn at A.3.3.
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
and is dealt with at A.3.3, where it costs the design its single most load-bearing display.
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

⚠ **THE STRUCK-AFFORDANCE DISPLAY COLLIDES WITH THE UI CORPUS, AND I RULE IT RATHER THAN IGNORE IT.**
Oath II is *"**Only surface UI elements the character can use**"* (`valoria_ui_ux_v4_1.md:63`) and its
violation test 1 is *"Does the UI display a control for a **capability** the character does not currently
have …? If yes → FAIL"* (`:65`). **It does not apply:** test 1's referent is a *capability* gate, and
`eligibility_kinds` is `[own, remit, hold, presence]` with the note *"⚠ `capability` IS NOT AND MUST NEVER
BE A MEMBER … 'capability supplies dice and GATES NOTHING'"* (`rosters.yaml:152-160`). The struck
affordance's gate is an **eligibility** clause — a public fact about an office — not a hidden capability.
Oath II survives; its worked example has no referent in this model.

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
> Cited to `world_q.py:439-552` for the sources, `carriers.py:259-260` for the closure,
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

### A.3.2 · The three readings a critic found unreachable — answered, with no new object

**1 · COMPARING TWO PLACES.** Both places are subjects in one ledger, so the comparison is person-side
and adds no read. What looks missing is a **pairing vocabulary** — `agreement` pairs by predicate over
`person_predicates`, and there is no `place_predicates` roster. **One is not needed, because the
vocabulary is derived rather than authored:** the `W-B` observation deposit writes claims in
`LedgerReader`'s own namespace — *"`stores:<kind>` / `condition` / `contain.path:<to>` / `claim.held` /
`exists:<kind>` / a relation stem"* (`witness.py:220-221`) — and *"These claims are in that namespace by
construction, because the Observation's predicate is derived from the cell"* (`:225`).

> **[DESIGN] The comparison is `agreement`'s shape with both arms re-bound: `pair(claims about A, claims
> about B)` over the predicates present in BOTH, with the unpaired ones named as why it is thin.** *You
> hold `stores:grain` for both, four seasons apart. You hold `condition` for Erzbach's harbour and
> nothing for Gelbgrund's.* One derived list, zero rosters — **and the honest output of a two-place
> comparison is usually a report about the reader**, which is `AX-2` rendered as a feature.

**2 · A POLICY'S COMPLIANCE ACROSS A PROVINCE.** The axis is wrong, and correcting it dissolves the
problem. `issue`'s requires cell is verbatim *"scope enumerates executors, not places (§37.1)"* and its
`scale_note` reads *"a Dispensation's `scope` enumerates executors — §37.1 — so its reach is the domain
the issuer governs"* (`verb_table.yaml:258, 261`). A policy has no provincial axis: **it has a list of
people.**

> **[DESIGN] Group the executor list by where I last heard each man was — and `residence` is already a
> declared `person_predicate` (`rosters.yaml:281`), so the key is a claim I hold about him, never
> `home_of`** (resolver-side, `world_q.py:150-170`). The unplaced go in a named bucket: *"three men you
> cannot place."* The provincial shape is an artifact of my knowledge of my own staff, which is what a
> governor actually has.

⚠ **Free of new objects, not free of work.** `establishment_of` reads *"the named persons the office
employs. Finite, contested, durable"* (`world_q.py:399-400`) and *"HOW MANY PERSONS AN OFFICE EMPLOYS IS
`H-34`, GRADED `assumption`, AND IS NOT SUPPLIED HERE"* (`:407-408`); and the world has 19 offices and
**0 `Record`s**, so there is no dispensation to be compliant with.

**3 · FINDING A PERSON YOU HAVE NOT MET.** `opening_set`'s clause 3 is `subject in referents(q)`
(`options.py:48`), so **the reachable subjects are the referents of my questions and nothing else.** A
person nobody has mentioned is not a referent and cannot be acted on — which is the axiom, not a gap.
Three routes make a stranger a referent:

| route | mechanism | live? |
|---|---|---|
| somebody tells me about them | Q2 — `(c.subject,)` is the referent (`world_q.py:494`), and a `told_by` claim's subject is a person id | **the only live one**, and it is the answer: *you find a person by asking someone* |
| they are a matter on a docket I sit on | Q1's referents are the docket's matters (`:479-480`) | dead — `w.dates` is 0, and `calendar()` writes `Date.fired` with no `emits=` so Q1's provenance walks nowhere (`world_q.py:571-579`) |
| I swear something about them | Q4's referent is `(prop.subject,)` (`:527-528`) | one effect body away (A.2.2) |

**And `interview` is formable AND resolvable** (`verb_table.yaml:643-657`; `own`; requires only *"the
person questioned exists"*), so a player may interview someone they have never met, provided somebody
mentioned them. ⚠ Its own row records what the precondition canon *wants* and cannot have: *"a witness is
someone who HOLDS a claim on the matter, and `04 §B.2`'s corrected `F8` carve-out admits a resolver-side
ledger read for THE ACTOR'S OWN ledger and no other … existence is the strongest clause the grammar
admits here"* (`:651`). **That is `AX-2` refusing to tell you whether the man you are about to question
knows anything**, and it is right.

### A.3.3 · What the place surface must NOT draw, and the one display this costs the design

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
  `footprint` and `provinces_of` — resolver-side (`world_q.py:254-272`, `:345-397`), **not in the licence
  list** (A.1.3). The distinction `footprint` records, *"Holding is title; presence is reach"*
  (`:257-258`), is real and is exactly what a player cannot see from outside. The surface draws what my
  claims say: *the banner on the gate at Erzbach, per the carter, last spring.*
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

---

## A.4 · POLICY AS A SURFACE

> Jordan: *"Policies aren't just a number added to a roll, but a way to change or impact how a governed
> rung functions."*

The engine's primitive settles the shape and it is quoted exactly, because the whole section rests on
one requires cell:

```
- verb:        "issue"
  scale:   "province"
  scale_note: "a Dispensation's `scope` enumerates executors -- §37.1 -- so its reach is the domain the issuer governs"
  stratum:     "binding_decision"
  eligibility: ["remit:issue"]
  requires:    "scope enumerates executors, not places (§37.1)"
  writes:      ["Dispensation.exists"]
  emits:       ["dispensation.issued"]
  grade:       "ruled"
```
— `engine/season/verb_table.yaml:256-266`, transcribed whole

**A policy is a named list of people who must do something.** Not a modifier, not a territory-wide
flag. That single fact supplies the compliance mechanic, the evasion mechanic, the visibility mechanic
and the political mechanic, because a list of people is a thing with faces.

### A.4.1 · ⚠ AND THE CARRIER DOES NOT EXIST — not as a stub, as nothing

`issue` writes `Dispensation.exists`. There is no `Dispensation` class anywhere under `engine/`, and
the tree reports this about itself:

> *"Kinds the instrument models as DICTS rather than classes — `Date`, `DocketItem`, `Petition`,
> **`Dispensation`**, `ConveningCondition` — cannot be checked at all and are reported separately, so
> the number is never mistaken for a clean bill."*
> — `engine/season/state/carriers.py:608-610`, the docstring of `matrix_rows_without_a_field`

So the policy-follows-whom problem is **worse than undesigned**: `matrix_rows_without_a_field` cannot
even say whether a Dispensation has a `scope` field, because the kind is not a modelled thing. The
verb row's own `writes_note` records the same defect from the grammar side: *"— (a Dispensation is not
a state write — §37.3) || ⚠ W3, ON THE W2 AUDIT: as `petition`. Part E's '(a Dispensation is not a
state write)' is the bypass §1.4 hole 4 names, not a licence for one"* (`:266`). **A write that is not
a write, into a kind that is not a class.** Said at the top of this section rather than in the grade,
because every display below renders a field of an object that has no fields.

The reconciled repair is sibling 01's, not this file's: a policy becomes a `Record` of kind
`dispensation`, which gives it `rung`, `ttl`, `stages`, `forgery_quality` and `subject_matter`
(`carriers.py:421-445`) and makes it a thing at a place that can be read off a wall. **This file
designs the surface on that carrier and says so, rather than designing on the dict.**

### A.4.2 · The declaration surface — the edit, the executors, and the list of its own blind spots

**Three fields, and the third is the honest one.**

1. **The edit, stated as a sentence and certain.** A policy edits a floor, an eligibility or a date —
   never a modifier. The pre-commit display shows the **rule** before and after, and this is the one
   thing on the whole surface that may be shown with certainty, because it is a statement about the
   rule and not about the world. ⚠ For the floor arm, "before and after" is a statement about
   `band_floors` cells whose keys are site uses (A.3.3), so what it can show is *which uses leave*, not
   which verbs.
2. **The executors, as people.** Drawn from `establishment_of(office)` — *"the named persons the office
   employs. Finite, contested, durable"* (`world_q.py:399-400`) — admissible under **L-3**. Each
   renders as a person with what I last heard of them and when. *This is where the interface becomes a
   game:* you are not setting a rate, you are choosing which of six men will carry it, knowing three of
   them well and two not at all.
3. **THE LIST OF ITS OWN BLIND SPOTS.**

   > *This names nine men. You hold current word from three. From four you have heard nothing since
   > spring. Two you have never met.*

   Computed from the ledger alone — `L-1` — and it is more useful than any outcome projection, because
   it tells the player the shape of their own ignorance **before** they spend a season on it. It is also
   what makes a governor's play feel like governing: you are placing a bet on people you partly know.

**And what may never appear here: an outcome projection.** No *68% chance*, no *likely result: Partial*.
The engine runs one world; there is no distribution to read off. A pre-commit percentage would be
`CLAUDE.md` §0.1 pt 4's *"a number without a control is not a measurement"* rendered as a UI
affordance. What the surface may show is the precondition as **my own belief with its provenance**, and
the machinery for that is already built and person-side:

| verdict | what the surface says | the line |
|---|---|---|
| holds | *"this needs eight measures in the bin. You believe there are eleven — you looked, last season."* | `evaluate` returns `Verdict(value, observed)` and `observed` is *"the same triple a `Claim` carries"* (`data/requires.py:83-96`, `:411-427`) |
| known-false | the candidate **does not appear at all** | *"This returns True only when the person HOLDS A CLAIM THAT CONTRADICTS the requirement"* — `epistemic.py:64-66` |
| **UNKNOWN** | *"this needs eight measures in the bin. **You do not know what is in the bin.**"* — and the act is still offerable | *"Having no belief either way is NOT a contradiction, so the Candidate forms, the person acts on a false premise, and the fold refuses them"* — `epistemic.py:65-67` |

⚠ **`evaluate` lives in `engine/season/data/requires.py`, not in `epistemic.py`** — the analyse stage
cited the wrong file for its own best display, and that is one of the two wrong-FILE errors in the
appendix. `epistemic.py:61-101` is `belief_contradicts`, which *calls* it.

### A.4.3 · Compliance — four states, and SILENCE MUST NOT READ AS COMPLIANCE

`comply` (`verb_table.yaml:130-142`) and `evade / defy` (`:220-232`) are verbs with `own` eligibility,
so compliance emits, evasion emits, and both are witnessed by whoever the fan-out admits. That gives a
standing-list row four states:

| state | ledger condition | how it draws |
|---|---|---|
| **complied** | I hold a claim of a `comply` by this executor | a mark, with its source and date |
| **evaded** | I hold a claim of an `evade / defy` | a mark, with its source and date |
| **silent** | no claim about this executor since the dispensation issued | ⚠ **not the same as complied.** An explicit gap with its duration |
| **contradicted** | two claims, disagreeing | a split cell (A.3.1) |

**⚠ SILENCE BEATING REFUSAL IS THE `skills/ners/SKILL.md` §6 DEFECT SEEN FROM THE READING SIDE, AND IT
IS A DESIGN FAILURE RATHER THAN A BALANCE NOTE.** Wherever two options reach one outcome and only one
emits an event, the silent one dominates, because events are the only thing costs can attach to. Run as
a dominance table at the seat where dominance was most likely:

| a governor's act, intent *"my order is being obeyed"* | gain | cost |
|---|---|---|
| go and look | a firsthand claim, current | 1 scene + a journey |
| dispatch an establishment member | a told_by claim, one remove | a man, for a season |
| wait for a petition | a told_by claim, self-selected | **nothing** |
| assume the silence is compliance | a belief | **nothing, until it is wrong** |

Rows 3 and 4 cost nothing, which is the decaying-cost dominance shape. ⚠ And — measured at A.2.1 —
**row 2's verb cannot be formed by any person**, `dispatch` being `remit:`-eligible, so the one row
that costs a man and a season is also the one row that does not exist. **Without the lapse emission,
R-CHOICE FAILS at every governor's seat**, and with it the table has no dominant row.

> **[DESIGN] ONE EMISSION RULE, THREE USES — and the carriers all exist.** A standing date that comes
> due unmet emits; a dispensation reaching its `ttl` emits; a declared stage whose term passes
> unmatured emits. `Date.due_at`/`fired` are read at `world_q.py:476`; `Record.ttl` is a field
> (`carriers.py:430`); `Record.stages`/`matured` are fields and `matured` is a direct Jordan ruling
> transcribed at `carriers.py:432-445`. **The governor learns his order was ignored because a date
> passed, not because a counter stopped.**

⚠ **AND THE PREREQUISITE IS A SILENT WRITE THAT IS ALREADY REGISTERED.** `calendar()` writes
`Date.fired` through the gate **with no `emits=`**, so *"no Event in any log carries a date id"* — *"a
CALENDAR-class silent write of exactly the shape the gate refuses at MATTER"* (`world_q.py:571-576`).
`write_matrix.yaml` declares `date.fired` and nothing emits it. So the lapse rule is not one sentence:
it is **make CALENDAR emit first**, which *"would put a new Event in every log and move every hash"*
(`:578-579`). Priced, not waved at.

### A.4.4 · Reading a government off a room — four channels, and three of them are broken

`01_AXIOMS.md` §ID-17 **refuses the word `regime`** — *"it is a coinage for a thing `band` already
covers, and it arrives carrying a governance model this design does not have"* (`:647-649`) — so this
reads *a government*, per `CLAUDE.md` §4's word rule. Four channels a player standing in a settlement
could read it from, with the honest state of each:

| channel | what it would show | live? |
|---|---|---|
| **1 · the missing use** | a market with no `exchange`, a wharf with no shipping | ⚠ **BROKEN.** `verbs()` has no loop caller and returns site uses, not verb rows (A.3.3). And `exchange` is formable but **not resolvable** |
| **2 · who is standing where** | an executor at the granary door *is* the policy embodied | ⚠ **BROKEN in the corpus.** `presence` is resolver-side; the reading is the `co_located` claim it deposits — and **0 of 74 sites has anyone present at its rung** (measured) |
| **3 · what is nailed to the door** | a `Record` at the rung, and it can be a forgery | ⚠ **BROKEN, and worse than reported.** `examine`'s typed cell is over a **`Site`**, explicitly: *"`Site` rather than `Record` per the block comment's reading of `:315-322`"* (`verb_table.yaml:636`). **No verb's precondition admits a Record**, `forge` is formable but **not resolvable**, and the world holds **0 Records** |
| **4 · what the people say** | `interview` | **LIVE.** Formable and resolvable (A.3.2) |

⚠ **The forgery reading survives on a different verb than the analyse stage named.**
`Record.forgery_quality` is a real field (`carriers.py:428`) and it is written by TWO rows —
`forge` (`verb_table.yaml:247-255`, **not resolvable**) and `create_record` (`:166-175`, `grade: ruled`,
**resolvable**, `writes: ["Record.exists", "Record.stages"]`). So the live route to a document is
`create_record`, and `forgery_quality` defaults to `0` on it. **A posted dispensation can be a forgery
in principle and cannot be one today**, and that matters because channel 3 is the only channel that can
make a player *confidently wrong about the law*.

**So one of four channels is live, and it is the one that runs through a person.** Which is the right
answer for a game with no GM, and it is the same answer A.6 reaches from above: **everything a player
learns about government, they learn from somebody.**

### A.4.5 · Who it hurt — the docket, legibly biased; and the false calm

`AX-2` forbids a welfare readout and any *"who is worse off"* panel is one. What a seat-holder has is
**petitions**, `own`-eligible with *"no dedup, no cap, no per-venue limit (§26.3)"* (`verb_table.yaml:399`).
So the honest rendering of *"who did this hurt"* is **the docket, unfiltered, with the places that have
sent nothing visibly sending nothing** — *eleven petitions, nine from Gransol and the two towns on the
road; nothing from the four villages in the west.* A place that never petitions is either content or
unreachable and the seat-holder cannot tell which: a real question with a real cost to answer.

⚠ **AND THIS SURFACE MUST BE ABLE TO SHOW A FALSE CALM.** The coverage suite's sharpest finding about a
duke is that his reform **"suppresses the grievance that would have reported the failure"**
(`proposals/2026-08-30-play-space-coverage/08_coverage_matrix.md:136`). **From above, a working policy
and one that has silenced its victims produce the identical display** — a row of complied-per-the-reeve.
The interface must not "fix" that with a sentiment indicator. The only way to tell them apart is to go,
and **that is the game.** Anything else is a dashboard over god-state wearing a period frame.

> ### RULED: a policy is a NAMED LIST OF PEOPLE, and its surface is the edit plus the blind spots.
> **Cited to `verb_table.yaml:256-266`, verbatim: `requires: "scope enumerates executors, not places
> (§37.1)"`.** `Dispensation` has **no dataclass** (`carriers.py:608-610`), so the surface is designed
> on sibling 01's `Record`-of-kind-`dispensation` carrier and says so. Compliance has **four** states
> and **silent ≠ complied**; the distinction requires the lapse emission, which requires CALENDAR to
> emit first (`world_q.py:571-579`). A government is read off a room through **four channels of which
> one is live**, and `regime` is a refused word (`01_AXIOMS.md:647-649`).

---

## A.5 · PROJECT AS A SURFACE

### A.5.1 · A half-finished work renders FREE, and the rendering is the mechanism

`Site.condition` *"is PRIMARY STATE, a FIXED-POINT INT (S48), and it GATES VERBS (S12.1)"*
(`carriers.py:412-413`). So **a Site below every floor affords nothing**: a half-built granary is a place
you can stand in and cannot use, drawn as **a place with no affordances**, with the uses it *will* have
struck. **A player reads "not finished yet" off the fact that there is nothing to do here.** No progress
bar, and none available.

⚠ And what carries it: a `band_floors` lookup with no loop caller, over a site-use vocabulary that is not
the verb table (A.3.3). **So "affords nothing" describes the design and not the running loop** — the
corpus's `work` acts refuse 723 of 723, *"because no referent it produces is a Site, which is a fact about
these worlds and not about the threshold"* (`verb_table.yaml:765`).

### A.5.2 · On the board — named terms struck through, never a percentage

A work's row shows its **stages as named terms**, read off `Record.stages: list[tuple]`
(`carriers.py:431`), with the matured ones struck:

> ~~the footings~~ · ~~the walls to the eaves~~ · **the roof** · the doors

**Not 60%.** Two reasons, and the second is binding. A percentage is an aggregate of incommensurable
things — stone, hands, seasons — answering no question a player has, where a named term answers the only
one they have: **what do I send next.** And ⚠ **a percentage mints a SECOND LADDER for one quantity**,
which `CLAUDE.md` §0.06's S clause calls a defect *"even when each is individually correct"*:
`Person.body` defaults to `DEFAULT_FIXTURES.get("condition_scale")` precisely because a bare literal
*"would be a second, silent copy of that scale"* (`carriers.py:388-392`). A completion bar is the third.

**The next term is what a person can supply** — *so many measures of stone; two men for two seasons* —
read off the term the act declared, never computed. `Record.stages` is written at RESOLVE, *"terms are
act-declared, never MATTER-advanced"*; `Record.matured` is Jordan's 2026-09-10 ruling, transcribed at
`carriers.py:432-445`, including that the code previously emitted `term.matured` **and applied no write
at all** — `ID-9` live. **The stall is the third use of the one emission rule** (A.4.3): *"The roof was
to be on by Michaelmas. Michaelmas has passed."* A date, not a number. `witness.py` records the sibling
gap in its own words — *"a claim leaving a ledger is a real state change that Part D gives no kind, so
nobody can witness a forgetting"* — the same shape, one object over.

### A.5.3 · Inheritance — you inherit the paper, not the claims

`succeed` is a verb and `hold` is *"1 PER OBJECT"* (`world_q.py:138-144`), so a work passes to a
successor — **and the successor inherits the `Record` and not the ledger.** He holds the paper and not
the knowledge. His row shows every stage, because the Record is a document, and shows **nothing** about
who was supplying it, whether the terms were really met, or where the stone went, until he goes and
looks.

> **[DESIGN] So the surface must distinguish, visibly and permanently, DOCUMENT-DERIVED from
> OBSERVATION-DERIVED facts**, because a stale or forged document says one thing and the site says
> another. Two marks, always different. This is the state a player will remember, and it is the one
> place in the design where a `Record`'s `forgery_quality` and a `Site`'s `condition` can openly
> disagree.

⚠ **AND IT IS UNREACHABLE IN THREE INDEPENDENT WAYS, EACH MEASURED.**

| what blocks it | the line |
|---|---|
| `succeed` is formable but **not resolvable** — no effect body | measured, A.2.1; 11 `@effect_for` registrations and `succeed` is not one |
| **no verb moves a `Record` to another person**, so the only holder of a Record is its maker | *"No verb in the resolvable vocabulary moves a RECORD to another person, so the only person holding a Record is still its maker … That is a PRODUCER hole with its own row and its own owner"* — `epistemic.py:311-316`, `H-84` |
| a `Record` has **no holder field** — it sits at a `rung` (`carriers.py:425-427`) | so "inheriting the paper" is inheriting the seat that reaches the rung, not the document. The document does not move |

**The consequence for the surface is the good one:** because the Record is at the RUNG, the successor's
document is *the thing nailed to the wall of the place he now answers for* — which is channel 3 of
A.4.4, and it means inheritance and reading-the-door are one mechanism rather than two. It also means
`destroy_record`'s `hold:<record>` eligibility declines person-side on a placeholder
(`options.py:159-160`), so **nobody can take the paper down**, which is a better-shaped hole than a
missing inheritance verb.

> ### RULED: a project's surface is its STAGES AS NAMED TERMS, and the site's own emptiness is the progress display.
> No percentage, on `CLAUDE.md` §0.06's S clause and `carriers.py:388-392`'s one-ladder rule.
> Inheritance renders **the paper, not the claims**, and the two-marks rule (document-derived vs
> observation-derived) is the design's answer. Blocked three ways, each named above rather than smoothed.

---

## A.6 · CAUSATION — the keystone, and it is a WORKSHEET, not a readout

> The chain: a provincial farming tax changes how settlements handle their yield → less is retained →
> a hearth's stores fall short → the people there have a narrower season → they choose differently.
> **Nobody authored the family's crisis.**

### A.6.1 · FROM BELOW — and the short larder emits NOTHING

The analyse stage wrote that a shortfall *"itself generates a `Question` whose referent is the hearth"*
and that the engine *"hands the interface the exact object the player needs."* **Opened and measured:
it does not.** `matter()` computes the draw, detects the shortfall, and deliberately emits nothing:

> *"⚠ A SHORTFALL EMITS NOTHING AND DECIDES NOTHING, on L5's rule: a threshold crossing **'MAY NEVER
> PRODUCE AN OUTCOME'**. Inventing starvation here would be the outcome L5 forbids … It is recorded so a
> run can be read."* — `engine/season/loop/matter.py:179-185`, whose whole response is a `TRACE.note`.
> The draw is `draw = {k: wt * len(eaters) ...}` at `:174`, over `eaters = world_q.presence(w, rid)` at `:169`.

**The crossing machinery covers `Site.condition` bands only** — `for verb, floor in sorted(floors.items()): if before >= floor > s.condition:` at `matter.py:261-262`, emitting
`condition.band_crossed` and appending `(s.id, verb, before, s.condition, ev.id)` to `w.crossings` at
`:272`. There is no band table over `Rung.stores`, so **a hearth going hungry raises no question at
all.** The three things that actually reach the player from below:

1. **The felt scalar.** `Sensation.subsistence` is one of the model's two, and `sense` is *"the ONE
   non-decision function permitted a World"* (`deliberate.py:465-466`), computed by an **injected
   formula** because *"no in-chain document supplies one"* (`:470-472`). ⚠ **So the one thing a hungry
   person feels is a number nobody has authored**, and it is a fixture, not a claim. **[DESIGN]** Render
   it as **quantity against NEED, never against a maximum**: *grain, eleven weeks; the season is
   thirteen.* The player does not need the number, they need to know they are short.
2. **The use that left.** If the settlement's store now moves only by the reeve's hand, the hearth's
   `transfer` out of it is gone. ⚠ Blocked at the bridge (A.3.3).
3. **The question** — which today does not fire, per 1 above and per H-110 below.

⚠⚠ **AND Q3's REFERENT IS NOT A PLACE — IT IS A SITE-USE STRING, WHICH IS WORSE THAN A WRONG ID.**
`questions_for` builds `Question(f"q:band:{what}", "band_crossed", (what,), what)` where `what` is the
crossing's **verb slot** — a site-use name like `bulk_shipping` — and discards the crossing Event's own
id, which is element 4 of the tuple (`world_q.py:514-518`). The register says so in its own words, and
counts the consequence:

> *"`band_crossed` — ⚠ **THIS ROUTE IS DEAD, AND IT IS NAMED DEAD RATHER THAN LEFT TO LOOK LIVE** …
> `what` is the crossing's **verb** — `"work"` — not an id, so the search below can never match:
> nothing in the log has id `"work"` or a change whose subject is `"work"`."* … *"⚠ **SO ONE OF FOUR
> ROUTES IS LIVE** — `claim_landed` … One is empty by design (`need`) and **two are dead**, each for a
> cause it does not own."*
> — `engine/season/queries/world_q.py:580-588`, `:594-596`, the docstring of `occasioned_by`

**`occasioned_by(w, q)` is the engine's own *why am I being asked this* query, and one of its four
routes walks.** That is the provenance of a question, and it is the surface's answer to the player's
first question about any pin. One in four.

### A.6.2 · FROM ABOVE — and the architecture has already ruled the answer

A governor is never present at the settlement whose granary is emptying. Q3's condition is
`if who == p.id or (at is not None and p.id in presence(w, at))` (`world_q.py:517`), and the docstring
says what that means: *"a crossing is a fact about a PLACE, and it becomes a person's question when
that person is THERE to notice it … A person elsewhere gets no question, which is L2 working"*
(`:506-509`). **Nothing asks him about a place he governs, and that is the axiom refusing to give an
absent man privileged access.** The route down and back is people.

⚠⚠ **AND `inferred` IS THE GOVERNOR'S CLAIM SOURCE, RATIFIED AT LAYER 1 SINCE 2026-09-05, AND NOTHING
WRITES IT. This is the best finding in the file and it closes three ruling requests at once.**

`04 §C.6` — *"WITNESS ↔ the ledgers — attribution is per channel, per witness"* — is a ratified table
assigning a **mint** to each of the five channels:

| channel | mints | `04 §C.6` line |
|---|---|---|
| `co_located` | the change claims, `firsthand` — **and**, if `causes` names an Act, an attribution claim read from the act store | `:732` |
| `document_key` | **the change claims only. No attribution** | `:733` |
| `witness_key` | change claims about self; via a knot, the partner's deposits, reusing the event id | `:734` |
| **`post_remit`** | **the change claims, `inferred`** | **`:735`** |
| `chronicle` | the change claims, `told_by` | `:736` |

> *"**Covert action then needs no flag:** an act performed where nobody is co-located has **no
> `firsthand` attribution anywhere**, and false attribution is a `tell` carrying a claim whose subject
> is the wrong person. **Rejected:** a global claim-subject rule, which gives a document holder an
> attribution they could not have seen."*
> — `04 §C.6`, lines 738-741

**`post_remit` is the office-holder's channel** — `_ch_post_remit` admits a person holding an office
whose `remit_acts` intersect the remits that could emit this Event kind
(`engine/season/epistemic.py:343-362`). So **a governor learning of an act in his own purview holds an
`inferred` claim about it, by ratified design.** That is *"late and distorted, through people"* built
into the claim's own `source` field, at no cost.

**MEASURED 2026-09-17: `"inferred"` appears in ZERO `.py` files anywhere in the repository** — not in
`engine/`, not in `tools/`, not in `tests/`. Its only occurrence as a value is the roster declaration
`claim_sources: [firsthand, told_by, inferred, firsthand_via_knot]` (`rosters.yaml:136`). That is
`ID-13` exactly — *"A DECLARED FIELD MUST REACH A READER, OR IT IS NOT DECLARED … it is a mechanism
that does not exist, wearing a schema's clothes"* (`01_AXIOMS.md:489-493`).

**Why nothing writes it, located exactly.** `witness()` builds its fan as
`[(pid, e, mode) for e in events for pid in observers_for(w, e, mode, everyone)]` —
`engine/season/loop/witness.py:104-105`. **The third element is the fan-out MODE, not the channel**,
and the loop that consumes it binds it to a variable named `channel` (`:167`). So the channel that
admitted each person is discarded before the deposit, and `src` has only two arms:
`src = "firsthand_via_knot" if via_knot else "firsthand"` (`:175`). `epistemic.py:320-321` says the same
from the other side: *"`observers_for` discards which channel admitted a person, and `claim_subjects`
under the default `both` rule starts from `e.subject`, the actor — a `document_key`-only witness learns
WHO ACTED."*

> ### **SO THREE OF THE ANALYSE STAGE'S FIVE RULING REQUESTS ARE NOT RULING REQUESTS. They close at
> step 1 of `CLAUDE.md` §0's ladder — superseded by `04 §C.6`, RATIFIED 2026-09-05 (ED-IN-0204).**
>
> | request as filed | disposition |
> |---|---|
> | **R-2** — *"the interface is `inferred`'s producer"* | **CLOSED, superseded.** `04 §C.6:735` gives the producer: the `post_remit` channel. The interface is a *consumer*. The reconciliation's alternative — an effect of `thread_read` — is refused on measurement: `thread_read` is **not resolvable** and its own row says why (`verb_table.yaml:697`, `H-85`), so it would put the producer on a verb nobody can attempt |
> | **R-4** — *"a document witness learns THAT the record changed, not who"* | **CLOSED, superseded.** `04 §C.6:733`: `document_key` mints *"the change claims only. No attribution."* Already ruled |
> | **R-5** — *"attribution per witness"* | **CLOSED as a REQUEST, OPEN as a CONFORMANCE DEFECT.** `04 §B.9:398` types `Event := (id, kind, changes[], causes[], emitted_at, degree?)` with **no `subject`**, and `04 Part D` row 9 grades *"an Event with an actor, target or subject"* **STRUCTURAL** (`:938`). **The built carrier has `subject: str` (`carriers.py:94`)** and the fold sets it to the actor — which `01_AXIOMS.md` §T-d records: *"every ledger in the world reads 'I hold that `<actor>` did `<kind>`', certainly and identically … `T-d` is currently a naming convention, not a mechanism"* (`:324-330`). Nothing needs ruling; the code is out of conformance with a ratified row |
>
> **And the repair is ONE wiring change with a three-tuple slot already waiting for it:** carry the
> channel through the fan instead of the mode, and dispatch `src` off `04 §C.6`'s table. It needs
> `observers_for` to return `(pid, channel)` pairs rather than pids, because its `any(...)`
> short-circuits per person (`epistemic.py:280-282` warns about exactly this) — so a person admitted by
> two channels needs a precedence. **That precedence closes at step 5 and is not escalated:** `04 §C.6`
> says *"A witness who was present saw who did it; a witness who holds the changed document saw only
> that it changed"* (`:726-728`), so a witness admitted by both saw who did it — **the union, with the
> strongest channel deciding attribution.** Obvious for the code; recorded, not asked.

### A.6.3 · The worksheet — five rules, and rule 1 is what makes it a worksheet

`Event.causes` is required and non-empty by construction — `__post_init__` raises and *"`[ROOT]` makes
the empty list unrepresentable rather than merely discouraged"* (`carriers.py:120-124`). So there is a
real DAG spanning seasons and rungs. **And the surface may not walk it.** `04 §C.11` forbids it in
terms: the derivation *"may NOT walk `causes[] → state/acts → Act.actor` — that path reaches the
attribution `T-d` forbids, is resolver-side, and `F.13` grades its guard `CONVENTION`"* (`:779-780`).
And `04 §B.9` closes the other door: *"`state/acts` is append-only, **resolver-side**, and no
person-side Query reaches it"* (`:413-414`).

> **[DESIGN] FIVE RULES.**
> 1. **The worksheet is built from the player's own claims, never from the DAG.** `causes[]` is the
>    spine of what the ENGINE did; it guarantees a real chain exists to be wrong about. It is not the
>    worksheet's data and it is architecturally barred from being it.
> 2. **A link is drawn only where the player holds a claim whose subject is that link's subject.** No
>    claim, no link — **a gap, with the named unknown that would close it.** *Between the reeve's order
>    and the short bin there is something you have not looked at: what the settlement store held at
>    Michaelmas.* This is `04 §C.11`'s *"the effect is unattributed"* licence at chain scale (`:785-787`).
> 3. **Every drawn link carries its claim's `source`, `when` and `confidence`.** A chain of firsthand
>    observations looks different from a chain of one man's word.
> 4. **NO AGGREGATE CONFIDENCE NUMBER ON THE CHAIN.** There is one world and no second arm, so a
>    number here is `CLAUDE.md` §0.1 pt 4's *"a number without a control"* rendered as an affordance —
>    **worse than showing nothing**, because it implies a precision the model does not have.
> 5. **Competing causes are shown UNRANKED, and the player ranks them by spending scenes.** If the
>    player holds a claim about a hard winter *and* a claim about the reeve's order, both stand side by
>    side with their sources and ages and **no ordering**. Ranking them would be the engine deciding a
>    person's conclusion, which is precisely what clause 4's docstring forbids for candidates
>    (`options.py:74-81`) and holds equally here.

**And closing a gap is an act, on a verb that is formable AND resolvable.** `reconstruct`
(`verb_table.yaml:704-717`): eligibility `own`, requires `own_ledger of subject` — *"the actor holds a
claim on the subject"* — `grade: ruled`, `writes: []`, `emits: ["finding.made"]`. It is one of the
thirteen (A.2.1). ⚠ And its own row already names the missing half, which is the DEGREE and not a
field: *"canon wants more than a claim here: `:278` makes a FAILED Reconstruct produce a plausible but
WRONG conclusion the player acts on. A Claim carries `value` and `confidence`, so the carrier exists —
what is missing is the degree that would decide which to mint"* (`:713`). **So the thing that makes a
player's conclusion durably wrong is a degree on an existing resolvable verb, and the claim it mints is
`inferred` via the channel `04 §C.6` already assigns.** Two halves of one mechanism, both ratified,
neither built.

### A.6.4 · What going to look actually deposits — and it is not what you looked at

⚠ **The deepest finding against the investigation surface, measured.** All five fieldwork verbs —
`examine`, `interview`, `research`, `surveil`, `reconstruct` — carry `writes: []`. Their Events
therefore have empty `changes[]`, and `claim_subjects` under the default `both` rule falls back to the
actor:

> *"An Event that wrote nothing has an empty `changes[]`, so every claim deposited from one was minted
> about **the actor** … §F1's Q2 admits a claim whose subject is the holder or something the holder
> holds, so **a claim about the actor can never raise a listener's question**: the news arrived in a
> form nobody could act on. Measured before this line existed: `R3` = 0 of 30 on the NPC lane, 0 of 59
> on ARC."*
> — `engine/season/epistemic.py:139-145`

And the event-kind claim is `Claim(cid, pid, subj, e.kind, True, ...)` — **predicate = the event kind,
value = `True`** (`witness.py:191`). So examining a granary deposits *"I hold that `<me>`
`finding.made` = True"*, not *"the bin holds eleven."*

**The quantity arrives through the OTHER deposit, and only for reads a precondition actually made.**
The `W-B` loop mints one claim per read the fold performed, from `Verdict.observed`, in the `requires`
namespace — *"`stores:<kind>` / `condition` / `contain.path:<to>` / `claim.held` / `exists:<kind>` / a
relation stem"* (`witness.py:205-208`, `:220-221`). Which means, per verb:

| act | what its precondition reads | so what you learn |
|---|---|---|
| `examine` a site | `existence of site kind Site` **and** `relation present_at` (`verb_table.yaml:627-635`) | that it exists and you were there. **Not what is in it** |
| `work` a site | `condition >= floor(verb)` | **the site's condition** |
| `transfer` grain | `stores(hearth(giver), kind) >= amount` | **what is in the bin** |

> **SO THE ONLY WAY TO LEARN A QUANTITY IS TO LEAN ON IT.** Not one of the five investigation verbs
> reads a number. You find out what the bin holds by trying to move eleven measures out of it and being
> refused — which makes A.6.5's refusal display not a consolation screen but **the primary epistemic
> instrument in the game.** This is either the best accident in the model or the design's sharpest hole,
> and it is not this file's to rule: it is `H-94`'s operand and the five rows' `requires_typed` cells.
> **Recorded as measured, with the three rows above as the evidence.**

### A.6.5 · The refusal display — the most important screen in the game

`Event.observed` is *"what the fold read to reach that event — a tuple of `Observation`, the same triple
a `Claim` carries … `changes[]` is what the act WROTE; `observed` is what it READ, **and a refusal
writes nothing and reads everything**"* (`carriers.py:99-110`, field at `:117`).

> **you believed** the bin held eleven — *your own eyes, last season*
> **the bin holds** three

Two rows and nothing else. That is the moment the player learns the world is not what they thought,
stated in the only terms that are honest: their belief with its provenance, beside what the world said
when they leaned on it. Everything in A.6 exists to make that moment legible, and the data for it is
already on the Event — **and person-side too**, because `evaluate` returns `Verdict(value, observed)`
before the act is ever formed (`data/requires.py:411-427`), so the belief half of the display is
available pre-commit and the world half only after.

⚠ **And the who-did-it row cannot be drawn honestly, and that is now a CONFORMANCE statement rather
than a limit.** `04 §B.9` and `04 Part D` row 9 make an Event with a subject STRUCTURALLY impossible; the
carrier has one; the fold sets it to the actor; WITNESS deposits every claim with it. Until the ratified
shape is built, **the surface renders WHAT CHANGED honestly and renders WHO DID IT as a claim whose
source is manufactured.** Stated as a limit, not designed around.

> ### RULED: causation is a WORKSHEET over the player's own claims, and `causes[]` is the ENGINE's spine, not the worksheet's.
> Barred from the DAG by `04 §C.11:779-780` and `04 §B.9:413-414`, not merely by preference. A short
> larder **emits nothing** (`matter.py:179-185`) and Q3's referent is a site-use string
> (`world_q.py:518`, `:580-588`), so the from-below chain's first two links do not fire. From above,
> `04 §C.6:735` already rules that the `post_remit` channel mints `inferred` — **closing R-2, R-4 and
> R-5 as requests** — and the repair is to carry the channel through `witness.py:104-105`'s fan instead
> of the mode. **No aggregate confidence number, competing causes unranked.**

---

## A.7 · SCALE TRANSITIONS — and the eight triggers, re-tabulated honestly

### A.7.1 · The document's own state, before its content is judged

`systems/_architecture/reference/scale_transitions_v30.md` is the ratified spine, and three facts about
it are load-bearing:

- **It carries TWO `## Status:` lines** — `:6` *"CANONICAL"* and `:8` *"DESIGN — canonical for scale
  transitions and mode bridging"*. `CLAUDE.md` §4: currency is resolved via `CURRENT.md` and a head's
  `## Status:` line, and a head with two of them resolves nothing by itself.
- **It is 344 lines with an `_index.md` + `_infill.md` sibling pair**, i.e. a grandfathered
  index/infill split that §4 retires as a default.
- **It is in the retire set and holds zero `.py`.** `engine/season/requirements.yaml:60-63` names this
  as the worked case for keeping such a tree: *"it is kept because 'the document IS the spec' — and this
  is the worked case for why that rule matters: the spec the adopted system must satisfy lives in a tree
  the ruling marked superseded. Superseded means the LOOP must express it. It never meant the
  requirement goes away."* **So it is cited here for intent and for the requirement it carries, and it
  binds nothing at runtime** (`CLAUDE.md` §0.05).

### A.7.2 · All eight Mandatory Zoom In Triggers, re-tabulated — THE CONDITION COLUMN GOVERNS

⚠⚠ **THE ANALYSE STAGE CUT FOUR AND KEPT FOUR, AND ITS TABULATION IS WRONG SIX WAYS. Two of its PASSes
were granted by reading the Scene-Content column where the Condition column governs — asymmetric
withholding, which `skills/ners/SKILL.md`'s method forbids — and two of its cuts fall on triggers that
are presence-conditioned and fine as written.** §4.3.2's table is
`| Trigger | Condition | Scene Content |` at `scale_transitions_v30.md:129-138`. Re-run on the
**Condition** cell only, all eight:

| # | trigger | the CONDITION cell, verbatim | honest verdict | analyse stage said |
|---|---|---|---|---|
| 1 | Settlement Revolt | *"Player is in a province containing a settlement at Order 0"* | ⚠ **SPLIT, and the cut does NOT hold as stated.** *"Player is in a province"* **is** a presence condition, at province grain — coarser than Q3's site grain but not absent. What fails is `Order 0`, a settlement **aggregate** the player can hold no claim about, which `Rung` refuses to store (`carriers.py:586-587`). **Repair: keep the presence condition, replace the aggregate with a crossing.** Fine as written on the half the stage attacked | ⚠ cut — *"province-membership, not presence"* |
| 2 | Heresy Investigation Target | *"Player is the target of an active Heresy Investigation"* | ✓ **UPHELD AND SHARPENED.** The channel is `co_located` — the Inquisitor arrives and is in the room. `_ch_co_located` (`epistemic.py:244-259`) is its predicate, and under `04 §C.6:732` that channel mints `firsthand` **plus** an attribution claim | ✓ kept |
| 3 | Faction Leader Removal | *"Player's faction leader is assassinated, overthrown, or incapacitated"* | ⚠⚠ **PASS WRONGLY GRANTED.** The stage quoted *"The player witnesses **or learns of** the event directly"* and marked it ✓ — **that sentence is in the SCENE CONTENT column** (`:133`), not the condition. The **condition** is a world-state fact about another person with **no presence and no learning clause at all.** It is the clearest `AX-2` breach of the eight | ✓ kept, on the wrong column |
| 4 | Mass Battle at Settlement | *"a mass battle targets a settlement in the player's current province"* | ⚠ **FINE AS WRITTEN.** *"the player's current province"* is presence at province grain, exactly as row 1. No aggregate is named. **The cut is refused** | ⚠ cut — *"same defect as revolt"* |
| 5 | Companion Arc Trigger | *"A companion's arc branch trigger fires (npc_behavior §5.2)"* | ⚠⚠ **PASS WRONGLY GRANTED, same error as row 3.** The stage quoted *"the companion's transformation scene plays out with the player present"* and wrote *"presence is in the condition"* — **it is in the Scene Content cell** (`:135`). The condition is an NPC's interior state firing, which is another person's interior | ✓ kept, on the wrong column |
| 6 | Knot Partner in Crisis | *"An NPC Knotted to the player reaches Conviction crisis (Scar count ≥ 3)"* | ✓✓ **UPHELD AND SHARPENED, and it is the best row in the table.** A live `knot` Tenure is **L-3** state — I am an endpoint. `_ch_witness_key` is its predicate (`epistemic.py:336-341`) and `firsthand_via_knot` is its claim source, minted at `witness.py:175`. **The one licensed non-local channel, and it is a FEELING:** the claim has no detail. Render a pin with a name and no content, in the direction of the person | ✓✓ kept |
| 7 | Stability Crisis | *"Player's faction Stability drops to ≤ 2 at Accounting OR drops by ≥ 2 in a single Accounting"* | **CUT HOLDS.** An aggregate no person can hold a claim about, and `Rung.__init__`'s law names *legitimacy* and *unrest* in the same breath (`carriers.py:586-587`). There is no carrier to read and no claim to render | ⚠ cut |
| 8 | Rank Advancement Recognition | *"Player's Standing crosses a rank threshold … AND Formal Recognition Event conditions are met"* | **CUT HOLDS.** `standing_of` is a **gap computed from the ledger** with no threshold event (`options.py:443-464`), and the row's own cell flags its attached mechanic undefined: *"(⚠ 'debt scene' mechanic undefined — no such concept in faction_politics_v30.md; needs Jordan: author it or strike the clause — ED-IN-0016 residual, tracked ED-IN-0030)"* (`:138`) | ⚠ cut |

**Score: 2 cuts hold · 2 cuts refused (presence-conditioned, fine as written) · 2 upheld and sharpened ·
2 PASSes wrongly granted off the Scene-Content column · 1 of the 8 split (row 1, half-and-half).** So of
the stage's eight verdicts, **two were right for the right reason, two were right and under-argued, and
four were wrong** — and the four wrong ones divide evenly into over-cutting and over-passing, which is
why the error is not a bias in one direction but a **method** failure: it read whichever column
supported the verdict it had.

### A.7.3 · §4.3.3's five Priority-1 World-State triggers — never audited, audited here

`scale_transitions_v30.md:142-152`. The analyse stage did not touch them.

| trigger | the CONDITION cell | verdict |
|---|---|---|
| Clock Band Transition | *"Any global clock (MS, CI, IP) crosses a band threshold"* | **CUT.** A global clock is an aggregate nobody holds. `Rung` refuses it; there is no carrier |
| NPC Conviction Crisis | *"Any NPC with Disposition ≥ +1 has Scar count ≥ 2"* | **CUT.** Another person's interior, read directly. `AX-2`'s hardest breach after row 3 above. The knot case (row 6) is the licensed version of this and is already in the table |
| Treaty Proposed or Broken | *"Any faction proposes, ratifies, or breaks a treaty involving the player's faction"* | **CUT as a trigger, KEPT as content.** A treaty is an act; its reaching me is Q2. `04 Part D` row 1 makes the faction-as-actor framing STRUCTURALLY impossible (`:930`) |
| Territory Control Change | *"Any territory adjacent to the player changes controller"* | ⚠ **NARROWED, not cut.** *"adjacent to the player"* is a presence-adjacent condition, which is the closest of the five to licensable. But the CHANGE is a `hold` Tenure turning over elsewhere. **Repair: the trigger is the claim about the change landing, and the new banner on the gate is what deposits it** |
| Warden Emergency | *"RS ≤ 40 and the player has WR ≥ 1 or has met Edeyja"* | **CUT.** A global clock again, conjoined with a personal fact. The personal half is L-3; the clock half has no carrier |

**Four cuts, one narrowed.** And the replacement for all thirteen triggers is the same and costs
nothing: **a trigger is a claim landing in my ledger — `questions_for`'s Q2, already built and already
the condition (`world_q.py:491-494`) — and PRIORITY falls out of the claim's `source` rather than from
an authored ordering:**

| source | urgency, and why | v4.1 equivalent |
|---|---|---|
| `firsthand` | it is happening in front of me | Priority 0 |
| `firsthand_via_knot` | I feel it and cannot place it | Priority 0, and the one channel that crosses distance |
| `told_by` | a person is standing here telling me | Priority 1 |
| `inferred` | I worked it out — and it comes from `post_remit`, which is my own office reporting to me (A.6.2) | mine, and therefore lowest and most durable |

**The eight-row table's CONTENT survives untouched** — what the scene is, what the choices are. That is
design, and it is good design. Its **trigger and priority logic** is free, because the channel computes
both. ⚠ This is a departure from a **CANONICAL** document and is therefore the one thing in this file
that would need Jordan even though nothing in `engine/season/` implements a trigger table.

### A.7.4 · Pausing correctly — the barriers, and no modes

`CLAUDE.md` §0.06's S clause requires that a system *"pauses correctly when other systems or scales are
called for."* The engine supplies the answer and the interface should take it rather than inventing a
phase machine: the season is **six barriers** — `calendar · census · deliberate · matter · resolve ·
witness` — and the tick advances after WITNESS.

> **[DESIGN] THREE RULES, replacing a 14-state machine and a cutscene queue.**
> 1. **The player may only be interrupted at a barrier.** Nothing arrives mid-resolution. This is
>    v4.1's atomic scene rule — *"no saves mid-resolution. Once a roll starts, reload goes to the most
>    recent phase or scene boundary — never mid-roll"* (`valoria_ui_ux_v4_1.md:114`) — **re-grounded**: a
>    barrier is the only place the world is consistent, so it is simultaneously the save point, the
>    interrupt point and the render point. **The mandatory-interrupt problem then dissolves**: a trigger
>    is a claim landing, claims land at WITNESS, WITNESS is a barrier. No queue, no priority table, no
>    nesting rule.
> 2. **The season does not advance while the player holds unspent scenes** — unless they decline the
>    rest, which is itself a choice with consequences. `Scene.PLAIN_COST = 1` and the unit is Jordan's
>    ruling, *"5 scenes for a character to play per season"* (`carriers.py:287-290`, `:325`).
> 3. **Handing off to another subsystem is a barrier event.** `contests: <prize>` is a real column and
>    *"if set, routes to the seam at RESOLVE (§39)"* (`verb_table.yaml:271-273`), so the surface can show
>    **before** commitment that this act will be resisted and what is at stake — and the scene returns a
>    **degree**, which the interface reports rather than recomputes.

**And no modes.** The three-mode table — TTRPG / Hybrid / Board Game — exists so a tabletop group can
decide what tonight is. **There is no group and no GM, and nothing in `engine/season/` implements a
mode.** What the mode table genuinely carries is a **time base**, and the engine has that distinction
without a switch: `Scene` is the budgeted unit and runs in rounds; `Rung.stores` and `Date`s turn over
per season. **Near the ground you spend scenes; high up you spend seasons — and it is the same surface,
because the rung you are at decides which clock you are on.**

⚠ **THE HONEST STATEMENT OF WHERE THIS FAILS TODAY, run 2026-09-17.**
`python -m engine.season.harness.register --requirements` → **met 1 · not_met 4 · partial 4**, with
`R-04 not_met`: *"54 of 143 cases are UNREPRESENTABLE — 44 at faction scale, 10 at world scale. The loop
runs at person, settlement and realm only"* (`requirements.yaml:286-292`). And the requirement this
section is designing against names **eight handoff rules** — *"Personal→Thread, Personal→Faction,
Personal→Scene (Contest), Scene→Faction (Domain Echo), Thread→Faction, and three more … **The loop
implements none of them**"* (`:55-58`). **So the scale transition designed here is designed against a
loop that does not yet span the scales it transitions between.** Stated, not hidden.

> ### RULED: zoom is CONTAINMENT, pausing is THE SIX BARRIERS, and a trigger is a CLAIM LANDING with priority off its `source`.
> **The eight-trigger cut is re-tabulated: 2 cuts hold · 2 refused · 2 upheld and sharpened · 2 PASSes
> withdrawn** (`scale_transitions_v30.md:129-138`, Condition column). §4.3.3's five are audited for the
> first time: **4 cut, 1 narrowed** (`:142-152`). The departure from a CANONICAL document is the one
> item in this file that needs Jordan, and it is recorded in PART C, not asserted here.

---

# PART B · WHAT THIS ADDS, AND WHAT IT MAKES UNNECESSARY

**The bar is `01_AXIOMS.md` §ID-13** — *"A DECLARED FIELD MUST REACH A READER, OR IT IS NOT DECLARED. A
column, flag or axis that no resolver consults is **not a weak mechanism — it is a mechanism that does
not exist**, wearing a schema's clothes. And it fails silently in the one direction that flatters:
everything it would have refused is permitted"* (`:489-493`). ⚠ The reconciliation also cited `04 Part D`
row 1 as this bar; **row 1 is *"an institution acts"*** (`:930`), a different claim. ID-13 is the bar and
`04` §F.24a's closure argument is its companion; corrected here.

### B.1 · What this file ADDS — four things, and none of them is a carrier

| # | addition | new primitive? | what it costs |
|---|---|---|---|
| 1 | **THE SURFACE LAW** — `(PersonInterior, Ledger, Sensation, Reads)`, `Reads` closed at three licences | **no.** A read licence is a rule about which existing functions a module may call. Its enforcement is a `TRACE` scan, which the queries already emit (`TRACE.query(..., "resolver")` on every one) | one scan, one test (PART D, D-1) |
| 2 | **The fourth cell state, CONTRADICTED** | **no store, one new READING.** `LedgerReader._best` already leaves the losing claim in the list (`person_q.py:82-96`); the enumeration over matching claims is derived. ⚠ Counted as an addition, not smuggled as free — `agreement`'s only caller is `standing_of` and pairs only claims about oneself over five predicates (A.3.1) | one derived list |
| 3 | **The named-absence rule** — every absence in the option set names the one thing that would make it formable | **no.** Three cases, two already traced by the engine (`options.py:58-59`, `:159-160`, `:164-168`); the third is the complement of `questions_for`'s referent sets | one derived list |
| 4 | **The two-marks rule** — document-derived facts render permanently distinct from observation-derived | **no.** It is the `source` field, read (`rosters.yaml:136`), and `04 §C.6`'s per-channel mint table is where the distinction is already declared | zero |

**And four things this file asks for that are NOT its additions**, because a ratified row already owns
them and the work is wiring:

| asked for | owner | status |
|---|---|---|
| `@effect_for("commit")` | `verb_table.yaml:115-129`, `grade: ruled` | RATIFIED-BUT-UNBUILT. Unflagged by the Arc-2 rule: its Tenure's subject is the actor |
| the channel carried through `witness()`'s fan, and `src` dispatched off the five-row mint table | `04 §C.6:730-736` | RATIFIED-BUT-UNBUILT. Closes `inferred`'s producer, the document asymmetry and attribution together |
| CALENDAR emits, then the one lapse rule with three uses | `write_matrix.yaml`'s `date.fired` row; `world_q.py:571-579` | a registered silent write. Priced: *"would put a new Event in every log and move every hash"* |
| `Event.subject` deleted; attribution per witness | `04 §B.9:398`, `04 Part D` row 9 (STRUCTURAL), `01_AXIOMS.md:324-330` | **a conformance defect, not a design question** |

### B.2 · What this file MAKES UNNECESSARY

| deleted | what made it unnecessary |
|---|---|
| four typed UI layers, four scene classes, seven typed zoom transitions with durations and audio cues, and the province panel's separate existence | a building **is** a `hearth` and a quarter **is** a `community` (`venues.yaml:21-25`); zoom is `parent_of`/`descendants` (`world_q.py:48,54`) — **five objects for one** |
| the Slate dock, its 12-entry overflow rule and its `+N more` expander (`valoria_ui_ux_v4_1.md:295-303`) | `Question.referents` (`carriers.py:251`) makes the list spatial; `questions_for`'s own sort supplies the ordering (`world_q.py:548-549`). **One camera control survives** |
| the ten-attribute character sheet, the derived block, and the Codex with its four knowledge states and ● ◐ ○ 🔒 ladder (`:977-1019`) | `standing_of` **is** the gap (`options.py:443-464`); the Codex is the ledger with a different filter and its ladder is `confidence` + `source` re-spelled |
| the cutscene queue, its priority tiers and its no-nesting clause (`:153-162`) | claims land at WITNESS and WITNESS is a barrier (A.7.4). Nothing to nest |
| a policy register screen and a projects board | both are *a thing I set running, with named persons, reporting back late and partially*. The difference is **columns** |
| the nine-row right rail — GEN · RS · TC · IP · Framework Drift · Stature · Convictions · Obligations · Duty (`:319-329`, whose own audit's first finding is right-rail saturation at `:329`) | `Sensation` has **exactly two scalars** and is *"the ONLY bridge from world truth into `choose`"* (`carriers.py:161-162`). A global clock is an aggregate nobody holds |
| all three stat-bar schemes: P/D/O node bars, settlement stat bars, and a project completion percentage | `Rung.__init__`'s law (`carriers.py:586-587`); and the percentage would mint a second ladder for `Site.condition` (`:388-392`), which `CLAUDE.md` §0.06's S clause calls a defect *"even when each is individually correct"* |
| the three-mode table's **switch** (TTRPG / Hybrid / Board Game) | `Scene` runs in rounds, stores and dates turn over per season; the rung decides the clock. No mode exists in `engine/season/` |
| **six of the thirteen authored zoom triggers, and the trigger+priority logic of all thirteen** | a trigger is a claim landing (Q2); priority is the claim's `source`. 2 of 8 mandatory cut on their own merits, 4 of 5 Priority-1 cut (A.7.2-3) |
| the withdrawn Render Law's own **exception list** | the three positive licences replace it, and each carries its own grade (A.1.3) |
| ~~the analyse stage's R-2, R-4 and R-5 as ruling requests~~ | `04 §C.6:733, :735` and `04 §B.9:398` + Part D row 9 already rule all three (A.6.2). Three escalations closed at §0 step 1 |

### B.3 · The ratio, because E is scored LAST and as a ratio

`CLAUDE.md` §0.06: *"⚠ **E is never scored as an independent axis**: alone it is satisfiable by
amputation, so score it **last, as a ratio against what N and R found**."*

| | count |
|---|---|
| **new carriers · stores · gauges · guards · verbs** | **0 · 0 · 0 · 0 · 0** |
| new *readings* over existing state | **4** (B.1) |
| ratified-but-unbuilt rows this design depends on | **4** (B.1), each with its owner named |
| top-level surfaces | **4 + 3 chrome** (where I am · what I have left to spend · the season and the date) |
| objects deleted | 4 layers · 4 scene classes · 7 transitions · 1 slate dock · 1 overflow rule · 1 character sheet · 1 Codex · 1 cutscene queue · 2 boards · 9 rail rows · 3 stat-bar schemes · 1 mode switch · 6 authored triggers |
| **words coined** | **0.** The design speaks only in the engine's own nouns — rung, claim, source, confidence, question, candidate, operand, remit, establishment, stage, term, degree, band, barrier — which is `CLAUDE.md` §4's test. ⚠ And it **declines** one word the analyse stage used freely: `regime`, refused at `01_AXIOMS.md:647-649` |

**Verdict: PASS as a ratio — far below one primitive added per primitive removed. FAIL if scored
alone**, because on its own the four readings are indistinguishable from an amputation, and the honest
defence of the cuts is N and R, not E. Said here per §0.06.

---

# PART C · THE THREE QUESTIONS

## C.1 · WHO OWNS THIS?

⚠⚠ **NOBODY, AND IT IS MEASURABLE.** `04 §A.2` names **nine modules** (`:129-139`) and assigns the
surface's home: **`port/` — *"the Godot shell; nothing under it is simulation"*** (`:137`).

- **`engine/season/port/` DOES NOT EXIST.** Measured 2026-09-17: eight of the nine module directories are
  present under `engine/season/`; `port/` is absent.
- **`04 §A.2`'s own read-licence table (`:143-164`) has NO ROW for `port/`.** Every other module has one.
  So the surface's read scope is undeclared at Layer 1, which is why A.1.3 had to state it.
- **`systems/ui/` holds ten `.md` files and ZERO `.py`, `.gd` or `.tscn`**; there is no `ui` row in
  `references/module_contracts.yaml` and no `ui` row in `CURRENT.md`. Measured.

**So the ownership answer is a build item, not a person:** `port/` is created, `04 §A.2`'s table gains a
`port/` row whose *may read* column is A.1.3's three licences, and the surface lives there. Nothing else
in this file can be owned until that row exists.

| the object | its owner |
|---|---|
| the read licence (L-1..L-3) | `04 §A.2`'s module table, in a new `port/` row |
| the four cell states | the renderer, over `L-1`; no store anywhere |
| the five claim-source mints | **already owned** — `04 §C.6:730-736`. The consumer is `witness()` |
| the option set's content | `opening_set` (`options.py:35-104`). The surface renders; it never filters |
| the site-use vocabulary | `rosters.yaml: band_floors` + `site_kinds`, and the missing operand is `H-94` |
| the explanation of any displayed value | `explain(p, v) -> Derivation`, `person_q`, **no World** (`04 §C.11:775`) |

## C.2 · WHAT CAN CHECK THIS?

| claim | grade | the construction that checks it, or why nothing can |
|---|---|---|
| `choose` never receives a World | **STRUCTURAL** | `View.__getattr__` raises `Forbidden` with the law inline — *"L2 — choose never receives a World. NOT BY DISCIPLINE — BY TYPE"* (`carriers.py:233-237`); plus the AX-2-binds-by-path test named at `questions.py:9-11` |
| **the renderer reads only L-1..L-3** | **MECHANICAL** | a path/AST scan over `port/` for imports of `state/` and `world_q`, mirroring `decision/`'s. **NOT structural**, and the withdrawn law claimed it was. ⚠ And no such scan can exist until `port/` does |
| UNHELD is read from the whole ledger, never from a capped View | **MECHANICAL** | `LedgerReader` takes `claims` and returns `UNKNOWN` on no match (`person_q.py:79-100`). A test that a UNHELD cell survives `view_k=1` |
| the surface displays no aggregate | **MECHANICAL against the accidental case, CONVENTION against the deliberate one** — `04 §B.3:240-244`'s own grading, carried across rather than restated | `Rung.__setattr__` refuses an undeclared field (`carriers.py:589-595`); a renderer computing a mean of claims is not reached by it |
| a claim is never marked true or false | **CONVENTION** | nothing in the type system distinguishes a correctness mark from a source mark. The check is a reader, and PART D's D-4 is the falsifier |
| no percentage, no probability, no outcome projection | **CONVENTION** | same. `CLAUDE.md` §0.1 pt 4 is the reason and a reader is the enforcement |
| a trigger is a claim landing, not an authored row | **MECHANICAL** | Q2's condition is code (`world_q.py:491-494`). A test that no trigger table is read by the renderer |
| the sentence-with-blanks idiom | **CONVENTION** | `Candidate.operands` is a dict and `requires_operands` is closed at eight — `[actor, subject, from, to, site, kind, amount, floor]` (`rosters.yaml:1084`). Which blanks a sentence shows is presentation |

> ### **STRUCTURAL: none.** Said plainly, because it is the finding.
> Every surface-side claim in this file is MECHANICAL or CONVENTION. The one STRUCTURAL guarantee in the
> neighbourhood — `View.__getattr__` — protects `choose`, not the renderer, and A.1.2 shows the renderer
> cannot use the `View` that carries it. **`AX-2` survives for the surface as discipline plus a scan.**
> Claiming STRUCTURAL here would be `09_IMPOSSIBILITIES`' own failure mode: *"a guard that cannot observe
> what it guards."*

## C.3 · WHOSE ACT MAKES IT HAPPEN?

**Every state this surface renders is deposited by an act, and the actor is named.** The nine loops,
signed per `01_AXIOMS.md` §ID-16 — *"Every feedback path appears in the register with a direction. **A
model in which every loop is negative CONVERGES** … convergence is not a design goal, it is what happens
when a design has no other ideas"* (`:544-548`). ⚠ And ID-16's own representation — a cycle enumeration
over the write/read graph — **is BLOCKED** (`:556-560`), so these are declared and signed, not computed.

| # | loop | sign | whose act closes it |
|---|---|---|---|
| L-1 | act → WITNESS deposit → my ledger → a candidate narrowed or widened → act | **+** amplifying | the actor's. `belief_contradicts` reads the ledger (`epistemic.py:61-101`), so what I learn changes what I will attempt |
| L-2 | a wrong `inferred` conclusion → narrows my own option set → I attempt less → I learn less | **+** amplifying, and it is the design's only self-deception loop | **mine.** `reconstruct`, and the degree that decides right from wrong (`verb_table.yaml:704-717`, `:713`) |
| L-3 | `inferred` → `tell` → somebody else's `told_by` at my confidence → their options | **+** amplifying | the teller's. `tell` transmits the teller's own claim at the teller's own confidence (`witness.py:361-363`) |
| L-4 | `confidence` decays → `claim.decayed` → the cell goes STALE → I renew it or act on it stale | **−** damping | nobody's — MATTER's. This is the one loop with no actor, which is why it is the only one that ends |
| L-5 | a lapse emits → I hold a claim that my order was ignored → `revoke` or `issue` again | **−** damping | the seat-holder's, and the lapse rule is its precondition (A.4.3) |
| L-6 | `dispatch` → he is present → his Q3 → his `tell` → my Q2 → `dispatch` again | **+** amplifying, and it costs a man and a season each turn | the governor's, then the man's. Two actors, which is what makes it slow |
| L-7 | `utter` → `commit` → Q4 every season → acts toward it → claims that change what I want | **+** amplifying, unbounded until the commitment ends | **mine.** The only loop a player can start from nothing |
| L-8 | `work` → `Site.condition` rises → a floor crossed upward → a Q3 → more `work` | **+** amplifying — ⚠ **and today it fires DOWNWARD only.** `matter.py:262` tests `before >= floor > s.condition`; the upward arm needs `before < floor <= s.condition` | the worker's. Sibling 02's item |
| L-9 | a gap between delivered and demanded read as a **band on a Query** → `repudiate`/`defy`/`petition` appear in a subject's option set → the gap widens or closes | **−** damping | the subject's. `01_AXIOMS.md` §ID-17: *"A band on a Query **changes what may be chosen and never produces an outcome**"* (`:642-645`) — **never a legitimacy field** |

**Six amplifying, three damping.** ID-16's warning is satisfied: the model does not converge, and the
three dampers are decay, a lapse noticed, and a subject's own refusal — none of them a global governor.

⚠ **AND THE ONE ITEM IN THIS FILE THAT NEEDS JORDAN.** Not a mechanism: a **departure from a CANONICAL
document.** A.7 cuts six of thirteen authored zoom triggers and replaces the trigger-and-priority logic
of all thirteen, in `systems/_architecture/reference/scale_transitions_v30.md` — `## Status: CANONICAL`
at `:6`. Nothing in `engine/season/` implements a trigger table, so the cost of the departure is
editorial rather than mechanical (`CLAUDE.md` §0.05), **and it still overwrites a ratified reading, which
is `CLAUDE.md` §0's own test for a genuine escalation.** Two options, a recommendation, the cost of being
wrong:

- **(a) Adopt the claim-landing replacement.** Priority is the claim's `source`; the eight scene-content
  cells survive verbatim. **RECOMMENDED**, because four of the thirteen conditions name an aggregate no
  `Rung` may store and two more name another person's interior, so implementing the table as written
  requires the surface to tell a duke about an Order-0 settlement he holds no claim on — the axiom broken
  at the one place a player will notice.
- **(b) Keep the table and give each condition a claim gate.** Cheaper to argue and worse to live with:
  it keeps thirteen authored rows whose gates drift from the four question sources, which is `ID-12`'s
  defect with extra steps.
- **Cost of being wrong on (a):** the scene-content column is untouched either way, so the loss is the
  *authored ordering* — and `questions_for`'s own sort already decides ordering with a content hash as
  the within-source tiebreak (`world_q.py:548-549`, and the roster's note measuring 801 of 1,068
  deliberations where the hash decides). **So (a) trades one undeclared ordering for another**, and that
  is the honest statement of its cost rather than a claim that it is free.

**Everything else in this file closes at §0's steps 1-5 and is NOT escalated.** R-2, R-4 and R-5 close at
step 1 (superseded by `04 §C.6` and `04 §B.9`); the two-channel precedence closes at step 5; the
`thread_read`-versus-`reconstruct` producer choice closes at step 4 on `reconstruct`'s own row plus the
resolvability measurement; `Oath II` test 1 closes at step 3 on `eligibility_kinds`' roster note.

## C.4 · THE GRADE — `paper`, and what would move it

`CLAUDE.md` §0.2: *"A milestone juncture is done when the behaviour EXECUTES. Not when a document exists
with a `## Status:` line … satisfiable by writing? **no**."* Every measurement in this file, run
2026-09-17:

```
python -m engine.season.harness.register --requirements
  THE NINE:  met 1 · not_met 4 (R-01 R-02 R-04 R-05) · partial 4
  R-04 not_met: "54 of 143 cases are UNREPRESENTABLE — 44 at faction scale, 10 at world scale.
                 The loop runs at person, settlement and realm only."
  R-05 not_met: "all verbs must be built out"

resolvable_verbs() over VERB_TABLE      38 rows · 18 resolvable · 20 NOT
person-side formable (an `own` alternative)                        28
BOTH formable and resolvable                                       13
  create_record · examine · interview · move · reconstruct · release · research ·
  speak · surveil · tell · transfer · utter · work        — not one act of office
@effect_for registrations in the package                           11

build_realm(0) at tick 0
  claims in all 46 ledgers                                          0
  Records in the world                                              0
  dates · docket · crossings                                    0 · 0 · 0
  sites with anyone present at their rung                       0 of 74
  questions from questions_for across 46 persons     81 — every one `need` (Q4)

grep -rn '"inferred"' --include=*.py .                     no match, repo-wide
world_q.verbs callers          5, all harness/probes.py (:678 :683 :1509 :1515 :2241); 0 under loop/
engine/season/port/                                        does not exist
systems/ui/  10 .md · 0 .py · 0 .gd · 0 .tscn · no module_contracts row · no CURRENT.md row
```

**GRADE: `paper`.** Nothing here executes, and the honest statement is stronger than *"nothing has
rendered a pixel"*: **there is nothing to render.** Four of the four question sources reduce to one; the
player's vocabulary is thirteen verbs and none of them is an act of office; the ledgers are empty.

⚠ **AND THE CHEAPEST STEP OFF `paper` IS NOT THE ONE THE ANALYSE STAGE NAMED.** It ranked *"call
`verbs()` from the loop and draw one site's option set"* as the smallest first move. **Measured, that
step draws site-use labels that are not verb-table rows** (A.3.3), from a query that is not in the read
licence, at sites where 0 of 74 has anyone present — so it would produce a panel of `bulk_shipping` and
`fishing` beside a candidate list that shares no vocabulary with it. It is cheap and it is not
first-usable.

> **Ranked, three steps, cheapest first, each with its execution artifact:**
>
> 1. **`@effect_for("commit")`** — one effect body on a `grade: ruled`, `own`-eligible, already-formable
>    row whose Tenure subject is the actor. **Artifact:** a person `utter`s a Proposition, `commit`s to
>    it, and `questions_for` returns a `need` question about it next season — which the corpus already
>    proves carries, since all 81 of its questions are `need`. **This is the first thing in this file that
>    could be wrong in public.**
> 2. **Carry the channel through `witness()`'s fan** (`witness.py:104-105`) and dispatch `src` off
>    `04 §C.6:730-736`. **Artifact:** a run in which some ledger holds a claim whose `source` is
>    `inferred`, which is currently impossible anywhere in the repository. Closes R-2, R-4 and R-5's
>    mechanism in one edit.
> 3. **A renderer under a new `port/`** that takes `(PersonInterior, Ledger, Sensation)` and draws one
>    place at one rung from one ledger, with the UNHELD cells named. **Artifact:** the drawing, plus a
>    `TRACE` transcript containing zero `"resolver"` queries. Until that exists, every verdict above is
>    an argument about a text.

---

# PART D · FALSIFIERS (`01_AXIOMS.md` §ID-11 — ship the falsifier with the claim)

| # | claim | what would show it wrong |
|---|---|---|
| **D-1** | the renderer reads only L-1..L-3 | `test_the_surface_emits_no_resolver_query`: render one place for one person and assert the `TRACE` transcript contains **zero** entries tagged `"resolver"`. Every function in `world_q` emits one on its first line, so the test observes the failure it excludes. ⚠ It **cannot be written until `port/` exists**, which is the honest state of a MECHANICAL grade with no artifact |
| **D-2** | UNHELD is a negative fact over the whole ledger, not a gap in a capped View | `test_unheld_survives_a_view_cap_of_one`: set `view_k=1`, render a cell whose claim exists, assert it draws HELD. If it draws UNHELD, the surface is reading the View and the law is broken in the direction that looks like caution |
| **D-3** | CONTRADICTED is readable from the ledger with no new store | `test_two_disagreeing_claims_about_a_site_both_survive_best`: deposit two claims on one `(subject, predicate)` with different values, assert `LedgerReader._best` returns one **and** the enumeration returns both. If `_best` evicts the loser, the split cell needs a store and B.1 row 2 is wrong |
| **D-4** | the surface never marks a claim true or false | `test_no_claim_renders_a_correctness_mark`: render a ledger containing a claim the world contradicts; assert the rendered cell differs from a true claim's cell **only** in `source`, `when` and `confidence`. **Expected to be the first one a deadline breaks** |
| **D-5** | a policy is a named list of people, never a modifier | `test_no_rendered_policy_carries_a_numeric_term`: assert no display derived from a dispensation contains a number that is not a `requires_operands` member. If one appears, *"+N to a roll"* has returned |
| **D-6** | silence is distinguishable from compliance | `test_a_standing_date_passing_unmet_emits_once`, plus its control `test_a_date_met_emits_a_different_kind`. ⚠ **This one is expected to FIRE today**: CALENDAR writes `Date.fired` with no `emits=`, so the first assertion fails and the failure is the finding, not the test |
| **D-7** | a project's progress renders with no second ladder | `test_no_rendered_project_shows_a_percentage`: assert every stage display is a term string from `Record.stages`, and that no rendered value is a ratio of `Site.condition` to `condition_scale` |
| **D-8** | the worksheet is built from claims, never from `causes[]` | `test_the_worksheet_never_reads_the_act_store`: build a chain with a real `causes[]` DAG and a player holding two of its five claims; assert the worksheet draws two nodes and three gaps. If it draws five, it walked the DAG and breached `04 §C.11:779-780` |
| **D-9** | no aggregate confidence number on the chain | `test_no_chain_display_carries_a_scalar`: assert the worksheet's rendered fields are drawn from `{source, when, confidence}` per link and that no field is computed across links |
| **D-10** | competing causes are unranked | `test_two_candidate_causes_render_in_a_stable_arbitrary_order_with_no_rank_field`. ⚠ **The trap this test exists for:** a stable sort *is* a ranking to a player. The assertion is on the absence of a rank FIELD and on the presence of an explicit *"unranked"* mark, not on the order |
| **D-11** | a trigger is a claim landing and priority is the claim's `source` | `test_no_trigger_table_is_read_by_the_surface`, plus `test_a_knot_claim_renders_with_no_content`: a `firsthand_via_knot` claim must draw a named pin with no detail. If it draws a summary, the best row in the ratified table has been spent |
| **D-12** | `inferred` has a ratified producer and no writer | `test_inferred_is_declared_and_unwritten`, asserting the grep result repo-wide — **and it is written to GO RED**: when the channel is carried through the fan, this test fails and is rewritten as its own control (*a `post_remit`-only witness holds an `inferred` claim; a `co_located` one does not*) |
| **D-13** | the four question sources reduce to one on the corpus | `test_build_realm_produces_only_need_questions`: assert the source histogram over 46 persons at tick 0 is `{need: 81}`. **A pinned measurement, expected to change**, and when it changes the reason must be a build item and not a fixture edit |
| **D-14** | zero of the four routes to a new question is both formable and resolvable | `test_no_route_to_attention_is_both_formable_and_resolvable`, over `dispatch`, `convene`, `petition`, `commit`. **Goes RED on step 1 of C.4** and is rewritten as the control (`commit` passes; the other three still fail) |
| **D-15** | the site-use vocabulary and the verb table are disjoint | `test_band_floors_keys_are_not_verb_table_rows`: assert the intersection of `band_floors`' inner keys with `VERB_TABLE`'s verbs is **empty**. If it is ever non-empty, the bridge A.3.3 says is missing has been built and the option-set display is unblocked |

**And the falsifier for PART A's central claim, which is the one that must not be quietly satisfied:**
`test_the_surface_law_is_three_licences_not_a_parameter_list` — assert that the renderer's entry point
takes a `Ledger`, not a `View`, and that no test in the suite constructs a surface from a `View`. **If
that test can be made to pass by widening `view_k`, the law has been re-broken in the exact way A.1.2
describes, and the withdrawn version has come back under the new name.**

---

# APPENDIX · CITATION REPAIRS

`CLAUDE.md` §0.1 pt 3: *"A citation you have not opened is not a citation."* The analyse stage's D3
self-reported eight invented addresses and an independent critic found sixteen of roughly thirty wrong,
with a systematic two-to-six line drift and **two wrong-FILE errors**. Every `path:line` in this file was
opened with `sed -n` before it was written. The repairs, including the ones the reconciliation stage had
already listed and the seven this file found:

| cited as | actual | kind |
|---|---|---|
| `carriers.py:232-238` (the `View` refusal) | class at `:208`; `__getattr__` at `:233`; law text `:235-237`; the cap refusal at `:217-220` | drift |
| `carriers.py:249` / `:251` (`Question.referents`) | `:251` — confirmed | the reconciliation's repair, verified |
| `carriers.py:372` (COHORT) | `:373` | drift |
| `carriers.py:426` (`Record.stages`) | `:431`. `:428` is `forgery_quality`; `:430` is `ttl`; `:445` is `matured` | drift, **three fields off** |
| `carriers.py:428` (`Record.ttl`) | `:430` | drift |
| `carriers.py:429-441` (`Record.matured`) | comment `:432-444`, field `:445` | drift |
| `carriers.py:568-571` (`Rung.yield` docstring) | `:576-577`. `:568-569` is `_DECLARED` | drift |
| `carriers.py:588-591` (the no-aggregate law) | **two sites**: `__init__`'s refusal `:586-587`, `__setattr__`'s `:589-595`. The cited range straddles them | drift, and it obscured that the rule is a whitelist enforced twice |
| `epistemic.py:314` / `:325-337` (the document-witness asymmetry) | paragraph `:319-329`; the `R8.5` ratified line quoted at `:322-324` | drift |
| **`epistemic.py:60-101` for `evaluate`** | **WRONG FILE.** `evaluate` is `engine/season/data/requires.py:411-427`; `Verdict` is `:83-96`. `epistemic.py:61-101` is `belief_contradicts`, which calls it | **wrong file** |
| `world_q.py:509-516` (*"a crossing is a fact about a PLACE"*) | `:506-509` | drift |
| `world_q.py:518-521` (Q3's presence gate) | condition at `:517`; the append at `:518` | drift |
| `world_q.py:520` (Q3 append) | `:518` | the reconciliation's repair, verified |
| `world_q.py:198` (`c.subject == p.id`, quoted inside a verb-table note) | `:493`. The note in `verb_table.yaml:651` carries a stale address for a line that moved | drift, **in the tree, not in D3** |
| `rosters.yaml:109` (the containment ladder) | `rung_kinds` at `:105-108`, values at `:108` | drift |
| `rosters.yaml:816` cited as `band_floors` registering three site kinds | `:816` is `site_kinds`' `values:` line (roster at `:805-816`). **`band_floors` is at `:1175-1200`** and keys on it | right line, **wrong roster named** |
| `rosters.yaml:250-264` (`question_sources`) | `:249-270`, values at `:270` | drift |
| `valoria_ui_ux_v4_1.md:461` (the perceptual-horizon line) | `:462` | the stage's own repair, verified |
| `valoria_ui_ux_v4_1.md:70` (Oath II violation test 3) | `:67`. `:70` is blank; `:69` is Oath III's clause | the stage's own repair, verified |
| `valoria_ui_ux_v4_1.md:295-311` (the Slate dock) | `:295-303`; the overflow rule and `+N more` at `:299` | drift |
| `valoria_ui_ux_v4_1.md:248-290` (the nine-row right rail) | §2.7's principles at `:319-329`, with the saturation finding at `:329` | drift |
| `..._max_audit.md:569` (bridge mechanisms) | `:567` | the stage's own repair, verified |
| **`04_seasons_duchies.md:100-103`** (*"never publishes the depletion rate … discoverable only by investigation"*) | **`:119-120`.** `:100-103` is about a praefect she cannot revoke | drift, **19 lines** |
| `04_seasons_duchies.md:222-227` (the dredge-or-arm crossing point) | `:234` | drift |
| **`04_seasons_duchies.md:335-357`** (*"suppresses the grievance that would have reported the failure"*) | **WRONG FILE.** `08_coverage_matrix.md:136`, and again at `:268`. The phrase does not occur in `04_seasons_duchies.md` at all | **wrong file** |
| `10_SUPERSEDING.md:1216-1222` (damage removes an option) | `:1216-1225`; the money line — *"Degradation is legible without a gauge: you can see which verbs are missing"* — is at `:1225` and was outside the cited range | drift, and the cut lost the best sentence |
| `requirements.yaml:285-292` (R-04's 54 of 143) | `:286-292` | drift |
| `hole_register.yaml:1102` for `H-71` | `H-71` at `:795-800`; `:1102` is `H-91`'s `unblocks` quoting it | the reconciliation's repair, verified |
| **`04:NNN` line-number form, everywhere** | rewritten as `§Letter.Number` throughout this file, per `C14` §1.5 | form |

**Two claims of the analyse stage's that no repair fixes, because they are wrong about the tree rather
than about an address** — both corrected in place above, and both are `CLAUDE.md` §0.1 pt 3's *"X works
today"* shape:

1. *"`dispatch` is the only one of the four routes the fold can carry."* `dispatch` is
   `remit:dispatch`-eligible and therefore **forms no candidate for anybody** (A.2.1). The stage read the
   resolvability list and not the eligibility column.
2. *"The disagreement count is computed; the interface displays what is computed."* `agreement`'s only
   caller is `standing_of`, over five person predicates, filtered to claims about oneself (A.3.1). Nothing
   computes disagreement about anything else.

**And one claim of the reconciliation stage's**, corrected on measurement rather than on argument: it
routed `inferred`'s producer to an effect of `thread_read`. `thread_read` is **not resolvable** and its
own row says why (`verb_table.yaml:697`, `H-85`). `04 §C.6:735` already assigns the producer to the
`post_remit` channel, and `reconstruct` — formable, resolvable, `grade: ruled` — is the act that reaches
it (A.6.2-3).

---

**`## Status:` line repeated at the foot, because `CLAUDE.md` §2 makes a merge ratify PROPOSED contents by
default and this file's hold-back must be loud at both ends: PROPOSED (2026-09-17), HELD BACK IN FULL,
NOTHING RATIFIES ON MERGE. §0.2 grade: `paper`.**
