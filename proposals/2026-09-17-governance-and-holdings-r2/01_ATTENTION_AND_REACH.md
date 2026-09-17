# 01 · ATTENTION AND REACH — how a decision reaches a person, and how it stops reaching everybody

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` · id: **ED-IN-0233** (shared with `05_LEDGER_AND_BUILD.md` — same lane, same commit).
## Grade under `CLAUDE.md` §0.2: **`paper`.** Nothing in this file executes. Every number below was
## produced by running the engine; **not one of the CHANGES below has run.** PART C.5 says what
## would move the grade and names the cheapest artifact. No row here may be cited as done.
## Method: authored at tier **`opus`** (`CLAUDE.md` §10 — *competing-considerations judgment,
## multi-doc synthesis*), against the working tree at `46aa21d`, 2026-09-17. The measurement block
## (§0.2) and the four falsifier controls in PART D were **executed this session**; the scripts are
## named at the row that cites them.
## Citation discipline, suite-binding: **`ARCH`** = `architecture/meta/04_CODE_ARCHITECTURE.md`,
## cited **`ARCH §Letter.Number`** and **never by line** — its line numbers have drifted twice.
## **`AX`** = `architecture/meta/01_AXIOMS.md`, cited `AX-n` or `AX §Letter.Number`. **`holonic`** =
## `architecture/holonic_ARCHITECTURE.md`, cited `holonic §NN.N` with the line in parentheses only
## as a finding aid. A bare **`01`/`02`/`03`/`04`/`05`** means a file in **THIS** directory.
## `path:line` is for **engine files only**, and every one below was opened at that line in this
## session; the APPENDIX lists the ones I inherited **wrong** and repaired.
## Falsifiers here are **`AR-n`**; loops are **`AR-L±n`**.
## Relation to round one: **supersedes** `proposals/2026-09-17-governance-and-holdings/00_THE_DESIGN.md`
## on questions and `01_SEATS_AND_POLICY.md` §A.15's fifth-row proposal. **`03_THE_SURFACE.md`
## STANDS**; this file discharges two of the three defects its RULED causation line names.

---

> **Jordan, the remit, verbatim:** ***"I do not want this work to be constrained by existing work. I
> want the best possible design ideas and concepts, and we can modify code accordingly."*** And:
> ***"Your remit is to develop the most NERS-positive work possible."***
>
> **Jordan, the keystone this file serves:** ***"They impact emergence."*** And: *"a change to how a
> rung functions will likely have impacts on rungs below it. A provincial policy on farming taxation
> may end up impacting a hearth, you know?"* — **a policy impacts a hearth by SOMEBODY AT THE HEARTH
> BEING ASKED ABOUT IT.** There is no other channel. This file owns that channel.
>
> **And the architecture clause this file exists to apply**, `holonic §37.2` (`:1295-1299`), which
> states the answer in one sentence and has been sitting in the corpus unread:
>
> > *"The person's own need, plus capability, plus this new **claim**, yields an opening through the
> > same `opening_set(person, view)` any act comes through — now evaluated over changed CLAIMED
> > terms. **No one authored an opportunity for anybody.**"*
>
> **Two sources. A need, and a claim.** The engine has four. This file removes two and names the
> Query that makes the remaining two enough.

---

# PART 0 · THE CONFORMANCE DIVISION, AND IT IS THE SPINE OF THIS FILE

Round one's `01` established the division and it is kept: **every section below carries one of three
words**, and the three lists are in front so a reader can skip the first entirely. The reason is
`CLAUDE.md` §0.05 read in the direction that bites: *a proposal that restates ratified architecture
as a proposal invites a session to re-decide a settled thing.*

**And the division lands differently here than it did in round one.** Round one's Q5 was an
EXTENSION — a fifth question source, unratified, argued for. **Everything this file proposes is
either CONFORMANCE to a ratified `ARCH` row that names the thing by name, or a DELETION.** There is
exactly one extension and it is one clause of one boolean.

## §0.1 · The three lists

**CONFORMANCE — RATIFIED Layer 1, UNBUILT or MISBUILT in the engine. Nothing here is proposed; it is
owed.**

| item | the ratified clause | the engine as measured, 2026-09-17 |
|---|---|---|
| **`place_of` — an Event's place, as a named function** | **`ARCH §F.14`**, which names it: *"an Event's place · `place_of` — the scene's place, or the changed thing's rung"* | it exists as a **private** helper with a different name: `epistemic._event_place` (`engine/season/epistemic.py:215`), read by exactly one caller (`_ch_co_located`, `:253`) |
| **CALENDAR emits `date.fired`** | **`ARCH §A.2`**'s module table, `loop/calendar` row: *owns `Date.fired` · **emits `date.fired` · `docket.formed`*** | the write passes **no `emits=`** (`engine/season/loop/calendar.py:37-38`), so no Event in any log carries a date id. `write_matrix.yaml:111` declares the kind |
| **a question source that reaches no code is a defect** | **`ARCH §B.13`**'s cross-validation family, `ID-12` — *"a declared row that reaches no code is the defect the loader's cross-validation exists to catch"* (quoted at `engine/season/epistemic.py:437-439`) | `question_sources` declares four (`rosters.yaml:270`); **two produce zero questions in every world the engine can build** (§0.2, measured with a positive control) |
| **`queries/world_q` is where an ownerless world-first read lives** | **`ARCH §A.2`**: `queries/world_q` *owns **nothing** — no token parameter exists on any function*, may read *any store, via `World`* | true today; `reach` and `place_of` belong there and nowhere else |
| **a decision may not read world truth** | **`AX-2`** (`:100`): *"There is no view of world truth available inside a decision — not capped, not filtered: **absent**"*; `ARCH §A.2`: `decision/` is *AX-2's island. **NO World in scope***| honoured: `questions_for` is world-side and hands `decision/` a `Question` of ids (`carriers.py:241-252`) |
| **a claim landing is what raises a question** | **`holonic §37.2`** (`:1295-1299`), quoted in the epigraph | honoured by Q2 and by nothing else; three of four sources do not read a ledger |
| **no broadcast; a decision reaches a person, never a place** | **`holonic §37.3`** (`:1301-1308`), four forbidden rows, *"assuming delivery"* among them | Q1's addressing test is `d.get("holder") in (p.id, None)` (`world_q.py:477`) and **nothing ever sets `holder`** (`effects.py:187`) — so Q1, were it producible, would address **every person alive** |

**EXTENSION — consistent with ratified Layer 1, unratified, and this file's actual proposal. There
is one.**

| item | what it rests on | why it is not a new primitive |
|---|---|---|
| **`reach(w, p) -> set[str]`**, four limbs, and **the place clause of the Q2 test** | `ARCH §F.14`'s `place_of`; `world_q.descendants` (`:54`); `world_q.parent_of` (`:48`); the ancestor walk that already lives **twice** (`predicates.py:135-140`, `world_q.py:432-436`) | it is a **set union of four existing walks**, stored nowhere, owned by nobody, and it **filters** a ledger the WITNESS fan already built. §A.4.4 |

**DEPARTURE — needs a ruling. THERE IS NONE IN THIS FILE.** Every fork this subject raised was closed
by `CLAUDE.md` §0's five-step gate and the step is named at each (§C.6). The suite's ruling requests
are **RR-P** (the principle, `02`), **RR-A** (the response verbs, `02`), **RR-B** (Layer-1 text, `03`
and `05`), **RR-C** (sequencing, `05`), **RR-2** (`ED-SE-0051`, `04`) and **RR-3** (round one's `03`,
surviving). **This file leans on RR-P and says so at §A.4.5; it does not assume it settled.**

## §0.2 · What I MEASURED today, rather than quoted

Every number below was produced this session against the working tree at `46aa21d`. The command is
given with the number, because `CLAUDE.md` §0 pt 8 is the standing instruction and round one's
`UNIFICATION_LEDGER.md` rows 20-21 are the precedent: three of round one's *"opened and found
CORRECT"* lines were false verifications.

**(a) THE CORPUS'S QUESTION CENSUS — `build_realm(0)`, `engine/season/harness/populated.py:246`.**

```
at build (tick 0):   81 questions    ALL `need`.  0 claim_landed · 0 date_due · 0 band_crossed
after 1 season:     642 questions    561 claim_landed + 81 need.   0 date_due · 0 band_crossed
after 2 seasons:   1053 questions    972 claim_landed + 81 need.   0 date_due · 0 band_crossed
world:  375 rungs (realm 1 · duchy 3 · territory 17 · settlement 37 · community 60 · hearth 211
        · person 46) · 46 persons · 19 offices · 74 sites · 0 dates · 0 docket · 0 crossings
        · 0 dispensations · 0 petitions · 35 live holds (19 person-subject, 16 NON-person)
ledgers at build: EMPTY.  after 1 season: 2175 claims (2174 firsthand, 1 told_by)
content_hash after 2 seasons: e7c4536b5db67f43b432691c885707e8
```

**There is no `province` rung.** The kind exists in `rung_kinds` (`rosters.yaml:109`) and
`build_realm` builds none — which is round one's `AUDIT_VERDICT.md` finding 2 reproduced
independently, and it is why this file's worked examples run **duchy → territory → settlement →
community → hearth** and never name a province.

**(b) Q1 `date_due` HAS NEVER PRODUCED A QUESTION AND CANNOT — three arms, with a POSITIVE CONTROL.**
`CLAUDE.md` §0.1 pt 3: *"claiming X is absent → RUN the thing that would show presence."* A spy on
`deliberate.questions_for` tallying `q.source`, over `probes.tiny_world`:

| arm | the date | 4 seasons | reading |
|---|---|---|---|
| **A** | exactly what `harness/corpus_run.py:323` plants for a `forced_by_threshold` case — `{due_at: 1, holder: None, fired: False}` | **0 `date_due`** (33 `claim_landed`) | at tick 0 `due_at 1 > 0`; at tick 1 CALENDAR fires it (`calendar.py:31`, `due_at == tick`) **before** DELIBERATE (`driver.py:356` then `:366`), so `not d.get("fired")` (`world_q.py:476`) is false forever after |
| **B — THE CONTROL** | `{due_at: -1, fired: False}` — a state **nothing in the engine can mint** | **50 `date_due`** | the reader works. The assertion can observe the failure it excludes (§0.1 pt 2) |
| **C** | `{due_at: 1, holder: "p_mid", fired: False}` — a holder set, as `convene` never does | **0 `date_due`** | the holder is not what kills it; the tick is |

**And arm B's state is unmintable, which is the structural half.** `_eff_convene` (`effects.py:184-189`)
sets `due_at = int(d.get("when", w.tick + 1))`, and `when` is **not** in the closed operand vocabulary
— `requires_operands` is `[actor, subject, from, to, site, kind, amount, floor]` (`rosters.yaml:1084`),
a cell naming an operand outside it **refuses at load**, and `_derive_operand` has no `when` branch
(`options.py:304-323`, falling through to `return None`). **So every date the engine can mint has
`due_at == tick + 1`, CALENDAR fires every date on exactly its due tick, and Q1's `not fired` guard is
unsatisfiable for every producible date.** Q1 is not under-used. It is unreachable.

**(c) Q3 `band_crossed` FIRES, AND WHAT IT PRODUCES IS UNWALKABLE — two arms, with a control.**
`headless.build_world(0)`, the first site seeded near a floor exactly as
`test_season_shape.py:3671`'s `_w4_run(2, condition=805)` does:

| arm | 3 seasons | crossings tuple | the Question |
|---|---|---|---|
| **A** site at 805 | **30 `band_crossed`** questions | `[('scriptorium', 'full_operations', 805, 795, 'd9eb4854a6661692')]` | `q:band:full_operations`, `referents=('full_operations',)`, `about='full_operations'` — **a site-use verb where an id is needed.** `occasioned_by` returns `[]` |
| **B — THE CONTROL** site at 990 | **0 `band_crossed`**, 0 crossings | — | wear is 10/season and the floor is 800, so a natural crossing needs 20 seasons (`test_season_shape.py:3692-3694`) |

**Three things in arm A are load-bearing and none is in any source document in this form.**

1. **The Event the Question needs EXISTS and is discarded.** `d9eb4854a6661692` is in `w.log` with
   `kind="condition.band_crossed"`, and it is **element 4 of the very tuple the reader iterates**
   (`matter.py:272` writes it; `world_q.py:514` destructures `for who, what, *_rest in w.crossings`
   and throws `_rest` away). That is `H-110` (`hole_register.yaml:1533`), reproduced.
2. **The crossing Event's `changes[]` is EMPTY** (`matter.py:269`, and pinned by an assertion —
   `test_season_shape.py:1131` asserts `not ev.changes`). So the `document_key` channel, which is
   `any(hold on c.subject for c in e.changes)` (`epistemic.py:331-333`), **cannot see a crossing at
   all.** Only `co_located` can. This is the fact that decides what REACH's purview limb can and
   cannot do (§A.4.6) and it is the single most consequential measurement in this file.
3. **30 = 2 persons × 5 rounds × 3 seasons.** `w.crossings` is a list that **is never pruned**. The
   crossing happened in MATTER at tick 0 and the same question was raised at every deliberation of
   every present person for the whole run. `scene_budget` is 5 (`fixtures.py:171`) and the driver
   runs one round per scene (`driver.py:358-361`), so the count is exact. **A band crossing is
   currently an ETERNAL question** — there is no `when` on a tuple, and nothing to compare a `since`
   against. A claim has `when` and `round` (`carriers.py:152`, `:156`) and Q2's `since` floor uses
   both (`world_q.py:491-493`). **The fold gives the crossing question a clock it does not have.**

**(d) WHAT REACH WOULD DO, LIMB BY LIMB — `build_realm(0)`, one season, 2175 claims, 46 persons.**
The honest decomposition, because a single aggregate here would hide the finding:

⚠ **RE-RUN AND REPAIRED 2026-09-17. The instrument is `probe_reach_questions.py`, a sibling in this
directory** — it did not exist when this table was first written, the figures came from an ad-hoc probe
that left no artifact, and `CLAUDE.md` §0.1 pt 3 does not accept that. **The headline reproduces
exactly; one row did not, and the attribution under it was wrong.** The probe asserts a control — row 1
must equal `world_q.questions_for`'s own `claim_landed` count — so the ladder is anchored to the live
query rather than to a re-implementation nobody checked (§0.1 pt 2).

| the Q2 admission test | questions admitted |
|---|---|
| **today**: `c.subject == p.id or c.subject in mine` (`world_q.py:493`) | **561** ✅ *= the live query, asserted* |
| **full REACH, SUBJECT ONLY** — all four limbs, no place clause | **561** ✅ |
| self alone, subject-or-place | ~~328~~ → **1632** ⚠ |
| self ∪ `mine`, subject-or-place | **1632** ✅ |
| **+ ancestors-or-self of home**, subject-or-place | **1632** ✅ |
| **+ purview** (`{seat.rung} ∪ descendants`), subject-or-place | **1632** ✅ |

> ⚠ **WHAT THE RE-RUN FOUND, AND IT IS A DEFECT IN THIS TABLE RATHER THAN IN REACH.** The six rows were
> not all computed on one ladder — `CLAUDE.md` §0.06's **S-METHOD** failure, *"calculations consistent
> in methodology with other mechanics"*, committed inside a single table. `place_of` has two defensible
> readings and these rows used three:
>
> 1. **The ASCENDING reading** — resolve a `Record` through its `rung` field (417 of the 2175 claim
>    instances have a Record subject) and climb from a rung to the nearest ancestor-or-self of kind
>    `hearth`. **This is the reading under which the corpus splits `2012 hearth / 163 none`, exactly as
>    stated below, and under which rows 4–6 read 1632.** It is the reading this file means.
> 2. **The NO-ASCENT reading** — the literal words of the next bullet, *"a person's live `contain`
>    Tenure's object **is** their home rung"*. On this tree that object is a rung of kind **`person`**
>    and the hearth is its PARENT: `build_realm(0)` gives all 46 persons a person-rung. The split is
>    `1902 person / 110 hearth / 163 none` and **rows 4–6 read 561** — the place clause adds nothing,
>    because a person-rung holds exactly one person.
> 3. **Row 3's `328` is neither.** It is the no-ascent reading with Records left unresolved. Under
>    reading 1 that row is **1632**; under reading 2, 451.
>
> **AND THE ATTRIBUTION IS WRONG WHERE THE MAGNITUDE IS RIGHT** — the corrected claim is the more
> useful one. ~~*"The entire effect is the PLACE clause, and it lands on the `mine` limb"*~~ → **the
> entire effect is the ASCENT, and it lands on the SELF limb.** Rows 3–6 are one number: once `place_of`
> climbs to the hearth, `pl == place_of(p.id)` admits everything, and `mine` adds nothing, because a
> person's `contain` object ascends to that same hearth. **`mine` is not carrying the effect; the hearth
> is.** This matters to §B.4's cost, because the limb about to be defended on the strength of 1071
> questions is not the limb producing them.

**Read that table before reading the rest of this file, because it overturns the plan's own N-line.**

- **The four limbs of REACH add EXACTLY ZERO questions by subject.** 561 → 561.
- **The entire effect is the PLACE clause**, and it lands on the `mine` limb, because a person's live
  `contain` Tenure's object **is** their home rung and `mine` is *"the objects of live tenures"*
  (`world_q.py:471`). 2012 of the 2175 claim instances have a subject whose `place_of` is a
  **hearth**; the remaining 163 resolve to no place at all (Propositions have none).
- **The ancestors limb adds 0. The purview limb adds 0.** Measured, not argued.

**(e) WHY THE PURVIEW LIMB ADDS ZERO, AND IT IS TWO INDEPENDENT REASONS — both measured.**

```
seat holders: 19.   Offices with a `rung`: 3  (King r_valoria · Duchess duchy_hafenmark
                                               · Duke duchy_varfell).  rung None: 16.
|reach| for the King 369 of 375 rungs · Duchess 97 · Duke 104 · a rung-less holder 10-13.
```

1. **16 of 19 seats have `Office.rung is None`** (`harness/populated.py:640-735` builds them from
   `npc_registry`), so the purview limb is **the empty set** for 16 of 19 seat-holders. That is round
   one's purview defect, re-measured from a second direction. **It is `03`'s `offices.yaml` that
   repairs it, not this file** — and this file's purview limb is therefore **inert until `03` lands**,
   which is stated here rather than discovered later.
2. **For the three seats that DO have a rung, the limb still adds nothing, and the reason is
   structural rather than incidental.** `fan_out_mode` ships `all_five` (`fixtures.py:328`), and of
   the five channels (`rosters.yaml:127`) the ones that can admit anybody in a world the fold can
   drive are `co_located`, `witness_key` and `document_key` (`hole_register.yaml:640`, measured
   there). **`co_located` is a place test** (`epistemic.py:253-257`) and `document_key` cannot see a
   crossing (§0.2c pt 2). **So a claim about a place is in your ledger only if you were AT that
   place** — and then your `mine`-plus-place test already admits it. A duke does not fail to be asked
   about a hearth in his purview because REACH is too narrow. **He fails because the claim is not in
   his ledger.**

**This is the finding that reshapes the argument, and PART A is written on it rather than around it.**

**(f) The corpus's `record.created` population, because it bounds the third Q2 clause.** After one
season of `build_realm(0)`: **69 Records, every one of kind `text`** (`create_record`'s default,
`effects.py`'s `d.get("kind") or "text"`), and **560 `record.created` claims** — the single largest
predicate in the corpus. Every witness-deposited claim today has `predicate = e.kind` and
`value = True` (`witness.py:191`: `Claim(cid, pid, subj, e.kind, True, w.tick, src, conf, "own", self.round)`).
**So no claim in this tree has a `content:` predicate and no claim's `value` holds an id set.** The
third clause of the Q2 test (§A.5.3) therefore has **no producer today**, and §A.5.3 sequences it
with `02`'s deposit rule rather than with this file's own build item. Saying otherwise would ship a
clause exactly as dead as the two this file deletes.

**(g) What `reach`, `place_of` and `nearest_store` are today.** `grep -rn` over `engine/season`:
**absent.** No function, no roster row, no test.

## §0.3 · TWO CLAIMS THIS FILE DOES NOT MAKE, both struck in place

⚠ **~~"REACH filters landed claims and never widens the fan."~~ → REACH never widens the WITNESS
FAN, and it DOES widen the QUESTION SET — measured, 561 → 1632.** The first form is the sentence the
plan carried and it is a half-truth that reads like a defence. The honest form is three clauses and
all three are checkable: **(i)** `observers_for` (`epistemic.py:405-441`) is not touched, so the set
of claims that reach a ledger is bit-identical; **(ii)** the question set over that ledger grows
2.9× on `build_realm(0)`; **(iii)** the number of questions ANSWERED does not move at all, because
`aggregate_questions(qs, "first")` returns exactly one question per deliberation
(`decision/questions.py:45-63`, and the default is `question_aggregation_rule="first"`,
`fixtures.py:385`). **What grows is a list that is then sorted and indexed at `[0]`.** The cost is a
sort and a hash re-record; the benefit is which question is first. §B.4 scores it.

⚠ **~~"Cut `reach` and the purview defect returns."~~ → That N-line does NOT survive its cut today,
and is recorded as NARROWED rather than passing.** `CLAUDE.md` §0.06: *"an N-line holding in exactly
one direction is narrowed, not passing."* Cut the purview limb and the question count is unchanged
(§0.2d). **What survives its cut is the PLACE clause** (1632 → 561, a 65% loss) and the **fold**
(two dead sources out, one clock in). The purview limb is kept on a different and weaker argument,
stated as such at §A.4.6: it is the **only** formulation under which the seat is what reaches, and
its inertness is a PRODUCER hole in the witness layer that this file names and refuses to invent a
channel for.

---

# PART A · THE CLAIMS, EACH WITH ITS VERDICT

## §A.1 · THE QUESTION MODEL AS IT STANDS — four sources, enumerated, each with what it binds

`questions_for` (`engine/season/queries/world_q.py:439-550`) is `§F1`'s `q` producer. It is called
from exactly one place — `deliberate.py:102`, `qs = questions_for(w, p, self._deliberated_at.get(p.id))`
— and its output is reduced to one question by `aggregate_questions` (`:108`). The sources are
`rosters.yaml`'s `question_sources` (`:250-270`), **ordered**, and the roster's own note says *"ORDER
IS SEMANTIC"* (`:260-261`).

**This is the whole of how a decision reaches a person in this engine. There is no second channel.**

### §A.1.1 · Q1 · `date_due` — `world_q.py:474-480`

```python
for did, d in sorted(w.dates.items()):
    if d.get("due_at", 1 << 30) <= w.tick and not d.get("fired"):
        if d.get("holder") in (p.id, None) or d.get("holder") in mine:
            items = [it for it in w.docket if it.get("date") == did]
            refs = tuple(sorted({str(it.get("matter")) for it in items if it.get("matter")}))
            out.append(Question(f"q:date:{did}", "date_due", refs or (did,), did))
```

| | |
|---|---|
| **fires on** | a Date due at or before this tick that has not fired |
| **referent** | the matters on every DocketItem naming that date, else the date id |
| **addresses** | `holder in (p.id, None) or holder in mine` |
| **producer of its input** | `_eff_convene` (`effects.py:173-190`) — the **only** writer of `(Date, due_at)`, and `write_matrix.yaml:98` says so: *"`due_at` is written ONLY by `convene`, which is an act"* |
| **measured** | **0 questions, in every world, with a positive control** (§0.2b) |

**Three defects, and they are independent.**

1. **The addressing clause is a universal.** `_eff_convene` builds the date as
   `{"id": did, "venue": d.get("venue")}` then adds `due_at` and `convening_attached`
   (`effects.py:187-189`). **It never sets `holder`.** So `d.get("holder")` is `None`,
   `None in (p.id, None)` is `True`, and Q1 addresses **every person in the world**. That is
   `holonic §37.3`'s *"assuming delivery"* row in one boolean, and it is also why `CALENDAR`'s own
   `vacant = not d.get("holder")` (`calendar.py:33`) always takes the `fire-and-lapse` branch and
   the docket is never appended — which is the corpus's `docket: 0`.
2. **The tick makes the guard unsatisfiable.** §0.2b, with arms A/B/C.
3. **The route out is dead.** `occasioned_by` (`world_q.py:553`) documents it at `:571-577`: CALENDAR
   *"writes `Date.fired` through the gate with **no `emits=`**, and the gate builds an Event only when
   one is passed … so **no Event in any log carries a date id**."*

⚠ **AND A SAFETY ARGUMENT ELSEWHERE IN THE ENGINE RESTS ON Q1'S ADDRESSING CLAUSE BEING TRUE.**
`_derive_operand`'s docstring (`options.py:287-290`) justifies promoting a world-sourced referent to
an operand of a minted act on the ground that *"(a) EVERY SOURCE IS ADDRESSED TO THE PERSON: **Q1
requires the Date's holder to be them or something they hold**, Q2 reads their own ledger, Q3 requires
them to be PRESENT where the band crossed, Q4 is their own live `commit`. **A person cannot be handed
a referent they have no reach to.**"* **Clause (a) for Q1 is false of the code**, for the reason in
pt 1 above. The word that paragraph reaches for is *reach*, and the property it asserts is exactly
what §A.4 makes true. **Deleting Q1 repairs that paragraph by removing its one false conjunct** —
which is a better repair than tightening the boolean, because the boolean guards a source that cannot
fire.

### §A.1.2 · Q2 · `claim_landed` — `world_q.py:491-494`

```python
floor = since if since is not None else (w.tick - 1, 0)
for c in p.ledger:
    if (c.when, c.round) >= floor and (c.subject == p.id or c.subject in mine):
        out.append(Question(f"q:claim:{c.id}", "claim_landed", (c.subject,), c.id))
```

| | |
|---|---|
| **fires on** | a claim in **p's own ledger** that landed since p last deliberated |
| **referent** | `(c.subject,)` — the one thing the claim is about |
| **addresses** | by construction: it is p's ledger. `AX-2` is satisfied structurally |
| **`mine`** | `{t.object for t in p.tenures if t.live}` (`:471`) — **every** live tenure's object: the home rung via `contain`, committed Propositions via `commit`, seats and rungs via `hold` |
| **`since`** | the driver-owned `(tick, round)` of p's last deliberation (`driver.py:254`); `Claim.round` is the field that makes the pair comparable (`carriers.py:132-146`) |
| **measured** | **561 of 642 questions after one season; 972 of 1053 after two.** The source the corpus runs on |
| **route** | **LIVE.** `occasioned_by` returns the originating Event's `causes[]` (`:611-615`) — one of four routes, and the one propagation runs on (`:594`) |

**This is the only source that is well-formed, and it is well-formed for one reason: its input is a
CARRIER WITH A CLOCK AND AN OWNER.** A `Claim` has a `holder`, a `when`, a `round`, a `source` and a
`confidence` (`carriers.py:147-156`). Nothing else in `questions_for` reads an object with any of
those.

### §A.1.3 · Q3 · `band_crossed` — `world_q.py:514-518`

```python
for who, what, *_rest in w.crossings:
    site = w.sites.get(who)
    at = getattr(site, "rung", None) if site is not None else None
    if who == p.id or (at is not None and p.id in presence(w, at)):
        out.append(Question(f"q:band:{what}", "band_crossed", (what,), what))
```

| | |
|---|---|
| **fires on** | any row of `w.crossings` — a list declared at `state/world.py:176` and appended at `matter.py:272` as `(s.id, verb, before, s.condition, ev.id)` |
| **referent** | `(what,)` — **the site-use verb string**, e.g. `"full_operations"`. `H-110` |
| **addresses** | `presence(w, site.rung)` (`world_q.py:172`) — a place test, correctly |
| **measured** | **30 questions over 3 seasons from ONE crossing** (§0.2c) — because the list is never pruned |
| **route** | **DEAD**, and `occasioned_by` says so at `:580-588`: *"`about` = `work` … nothing in the log has id `"work"` or a change whose subject is `"work"`"* |

**Three defects.**

1. **The referent is a verb, not an id.** `H-110`, measured at §0.2c. Every consumer of a `Question`
   downstream treats `referents` as ids: `_derive_operand` binds `subject`/`to`/`site` to the
   referent (`options.py:307-312`), and `§F1` clause 3 is *"subject in referents(q)"*
   (`carriers.py:247`). **A verb name in that slot forms a Candidate whose subject is a verb name.**
2. **The carrier has no clock**, so the question is eternal (§0.2c pt 3).
3. **The fact has TWO carriers.** MATTER emits `condition.band_crossed` into `w.log`
   (`matter.py:267-271`) **and** appends to `w.crossings` (`:272`). One is an Event with an id, a
   subject, a `causes[]` and an `emitted_at`; the other is a five-tuple. `AX-4` (`:141`) —
   *"EVERY VALUE HAS EXACTLY ONE OWNER, AND THE OWNER IS ITS ONLY WRITER"* — is not violated in the
   letter (one writer) and is violated in the thing it protects: **two readers of one fact, and they
   disagree about what the fact is**, which is `CLAUDE.md` §0.05 clause 3's *"never keep a second
   copy."*

### §A.1.4 · Q4 · `need` — `world_q.py:523-528`

```python
for t in p.tenures:
    if t.kind == "commit" and t.live:
        prop = w.propositions.get(t.object)
        if prop is not None and str(prop.mood).upper() == "OUGHT":
            out.append(Question(f"q:need:{t.object}", "need", (prop.subject,), t.object))
```

| | |
|---|---|
| **fires on** | a live `commit` Tenure whose object is an `OUGHT` Proposition |
| **referent** | `(prop.subject,)` — what the Proposition is about |
| **addresses** | by construction: p's own tenure |
| **measured** | **81 questions at build, and exactly 81 after one and after two seasons** — the standing floor of the corpus |
| **route** | **EMPTY ON PURPOSE** (`:589-593`): *"A standing commitment to an OUGHT is interior; no Event caused it this season"* |

**Q4 is `holonic §37.2`'s *"the person's own need"* and it is correct as written.** It is the reason
an NPC with an ambition and a quiet season acts at all (`H-54`, `hole_register.yaml:618`;
`rosters.yaml:256-258`). **It survives untouched.**

### §A.1.5 · THE TWO ORDERINGS, AND ONLY ONE IS DECLARED

`world_q.py:548-549`:

```python
order = {src: i for i, src in enumerate(QUESTION_SOURCES)}
out.sort(key=lambda q: (order[q.source], q.id))
```

- **ACROSS sources**: the roster's order, declared (`rosters.yaml:260-261`).
- **WITHIN a source**: `q.id`, and **nothing declares it**. For `claim_landed`, `q.id` is
  `f"q:claim:{c.id}"` where `c.id` is a content hash minted off the depositing Event
  (`witness.py:182-183`). **MEASURED over 89 corpus baselines: the leading source is SHARED with at
  least one other question in 801 of 1,068 deliberations** (`rosters.yaml:265-268`;
  `hole_register.yaml:618`). So three quarters of the time the declared order decides nothing and a
  hash decides.
- **`H-54`'s disposition is DECLARED AND LEFT ALONE**, at step 4 of `CLAUDE.md` §0's gate, with
  `needs_jordan: false`, and its own words are *"editing that sort is a design edit to a line three
  rows depend on, which this row's own `H-54` note at the `occasioned_by` walk already refuses to
  make as a repair."* **This file does not touch the sort** and §A.10 measures what the fold does to
  the order it leaves in place.

### §A.1.6 · `occasioned_by` — one live route of four, and the two dead ones are NOT separate branches

`world_q.py:553-634`. The structure, opened:

| source | the branch | what it returns |
|---|---|---|
| `need` | `:609-610` — early return on `q.source == "need"` | `[]`, by design |
| `claim_landed` | `:611-615` — searches backwards for the `claim.deposited` Event naming the claim, returns its `causes[]` minus `ROOT` | **the originating Event. LIVE** |
| `date_due`, `band_crossed` | **NO branch of their own.** `:616-628` is a NEGATIVE membership guard — `if q.source not in ("date_due", "band_crossed"): raise Unspecified(...)` — which lets exactly those two **fall through** to the generic id search at `:630-634` | `[]`, because nothing in the log has id `"full_operations"` or `"d_forced"` |

⚠ **This is a citation repair to my own plan**, which said *"the `date_due` and `band_crossed` routes
are dead (opened: the branches return `[]`)"*. **They are not branches.** They are the absence of a
branch, guarded by an inverted membership test whose `law` string is the design's polarity rule
(`ID-5` — *"refuse, don't default"*). The distinction is load-bearing for the migration: **deleting
the two sources does not delete two `if` blocks; it deletes the negative guard's tuple and leaves the
generic id search with no caller** (§A.8, and the search is then deletable too, which the deletion
ledger counts).

And the function's own docstring already records the lesson this file is an instance of:

> *"⚠ **This count has been wrong twice**: *"one route per question source"* first, then *"two of
> four"* after a critic found `band_crossed`. Both were written by looking at this function rather
> than at what feeds it. **The lesson is in the count, not in the routes: a route's liveness is a
> property of its PRODUCER, and this function cannot see its producers.**"* — `world_q.py:596-601`

---

## §A.2 · THE ANSWER — TWO SOURCES, AND NOTHING ELSE IS A QUESTION SOURCE

> ### RULED: a person is asked about **a claim that landed in reach**, or **a need**. `question_sources` becomes `[claim_landed, need]`.

**The five-step gate (`CLAUDE.md` §0), run:**

1. **Superseded?** — *partly, and in this file's favour.* `holonic §37.2` (`:1295-1299`) states the
   two-source model in one sentence: *"the person's own need, plus capability, plus this new claim."*
   `ARCHITECTURE_V2 §F1` said *"exactly three sources, and by nothing else"* and was wrong by one
   (`rosters.yaml:255`), which is why the set is a roster and not a sentence. **Nothing ratifies
   four.**
2. **Irrelevant?** — no. This is the live producer of every NPC decision in the tree.
3. **Answered by a design document?** — **yes, for the FOLD.** `holonic §37.2` names the two. What no
   document answers is *how* a crossing becomes a claim, which is §A.7's work.
4. **Answered by precedent?** — **yes, for the DELETIONS.** `ARCH §B.13`'s cross-validation family
   and `ID-13` (*"a declared field must reach a reader, or it is not declared"*) are the tree's
   standing answer to a declared row with no live consumer; `hole_register.yaml:618`'s own handling of
   a silent default is the procedural precedent.
5. **Not reached.** **No ruling request.**

**The fold, source by source:**

| today | becomes | what the deleted object was doing |
|---|---|---|
| Q1 `date_due` | **a `claim_landed` question.** CALENDAR emits `date.fired`; the Event is witnessed; the claim lands; the claim raises the question | it was addressing everyone, unsatisfiably, with no route out (§A.1.1) |
| Q2 `claim_landed` | **survives, with a widened admission test** (§A.5) | — |
| Q3 `band_crossed` | **a `claim_landed` question.** The crossing Event already exists and is already witnessed co-located; the claim's subject is the SITE | it was raising an eternal question about a verb string (§A.1.3) |
| Q4 `need` | **survives, untouched** | — |

**And the shape of the argument is the shape `05`'s ledger counts:** *every addition is a body for a
row that already exists, or a walk that replaces a family.* Here the row that already exists is
`(Date, fired)`'s declared `emits:` (`write_matrix.yaml:111`), and the family replaced is three
mechanisms — a dict scan over `w.dates`, a tuple-list scan over `w.crossings`, a ledger scan — reduced
to **one ledger scan**.

---

## §A.3 · `place_of(w, x)` — `ARCH §F.14`'s OWN NAME, PROMOTED

**This is CONFORMANCE.** `ARCH §F.14` names the function, gives its rule and states its risk:

> **F.14** | **an Event's place** | `place_of` — the scene's place, or the changed thing's rung | *a
> plague is **one Event spanning many rungs** and **has no single place**; `place_of` must return a
> set and my signature does not*

**What exists.** `epistemic._event_place(w, e) -> Optional[str]` (`engine/season/epistemic.py:215-241`),
private, one caller (`_ch_co_located`, `:253`), and carrying in its docstring the repeat-defect record
that makes its limb ORDER load-bearing:

> *"⚠ A PERSON IS ASKED BEFORE A RUNG, AND THE ORDER IS THE WHOLE OF THIS FUNCTION'S CORRECTNESS. The
> first version tested `e.subject in w.rungs` FIRST — and `probes.py` gives every person a same-id
> `person`-kind Rung, so for a person-subject Event this returned the person's own rung and
> `Query.presence` then answered *"who is contained IN p_high"*, which is nobody. … It was a channel
> BROKEN CLOSED, and `P15`'s only assertion (`narrow < total`) could not tell the two apart — §0.1
> pt 2. **THIS IS A REPEAT.**"* — `epistemic.py:218-228`

**What it becomes.** `world_q.place_of(w, x) -> Optional[str]`, taking **any id** rather than an
Event, with the person-before-rung order preserved and two limbs added:

```python
def place_of(w: World, x: str) -> Optional[str]:
    """`ARCH §F.14`. The rung a THING is at. PERSON BEFORE RUNG -- see `_event_place`'s
    docstring for the repeat defect that order exists to prevent."""
    if x in w.persons:                      # a person is where their live `contain` edge says
        return home_of(w).get(x)            # `world_q.home_of` :150 -- the single owner
    if x in w.sites:                        # a site is at its own rung (S12)
        return getattr(w.sites[x], "rung", None)
    if x in w.records:                      # NEW: a record is where its HOLDER is,
        h = hold_force(w, x)                # `world_q.hold_force` :138 -- one live hold per object
        return place_of(w, h.subject) if h is not None else w.records[x].rung
    if x in w.dates:                        # NEW: a date is at its venue
        return w.dates[x].get("venue")
    if x in w.rungs:                         # a rung is itself
        return x
    return None                              # NO SILENT DEFAULT
```

| limb | the owner it reads | verified |
|---|---|---|
| person → containing rung | **`world_q.home_of`** (`:150-168`), *"THE INVERSE OF `presence`, AND IT EXISTS BECAUSE FOUR SITES HAD ROLLED IT BY HAND"* | `:150` opened. `_event_place` rolls it by hand at `:230-232`; the promotion removes the fifth copy |
| site → `site.rung` | `Site.rung`, *"the maintained side (S12)"* (`matter.py:200`) | `epistemic.py:234-235` |
| **record → its holder's place, else `Record.rung`** | `world_q.hold_force` (`:138-144`), which **raises `Forbidden` on more than one live hold** — *"S15 — `hold` cardinality is 1 PER OBJECT"* | `carriers.py:426`: `Record.rung: str`, non-optional, so the fallback is total |
| **date → `venue`** | `_eff_convene` writes `{"id", "venue"}` (`effects.py:187`); `_req_convene` requires `venue in w.rungs and parent_of(venue) is not None` (`predicates.py:306-309`), **so a venue is always a rung with a parent** | `predicates.py:299-309` opened |
| rung → itself | — | `epistemic.py:236-237` |
| **anything else → `None`** | `ID-5`'s polarity: absence maps to the refusal, never to a plausible default | `epistemic.py:241` |

**`_event_place` is then deleted and its one caller becomes `place_of(w, e.subject)`.** The
deletion ledger counts `place_of` as **+0** (a move) and the record and date limbs as part of the same
object, because they are two `if` clauses inside one function and not two names a reader must hold.

### §A.3.1 · What `place_of` MAY NOT read, and what it may not become

- **It may not read a ledger.** It is world-first and lives in `queries/world_q`, which `ARCH §A.2`
  types as reading *any store, via `World`*. A `place_of` that consulted a person's beliefs about
  where something is would be a second answer to one question and would put `AX-2`'s hazard on the
  resolver side of the line.
- **It may not be called from `decision/`.** `ARCH §A.2`: `decision/` is *AX-2's island. **NO World
  in scope***. The Question carries **ids**; the place computation happens world-side, before
  `assemble`.
- ⚠ **It returns ONE place and `ARCH §F.14` says that is wrong for a multi-rung Event.** The honest
  statement: **the limitation is live in this tree today.** MATTER's actorless-event channel is *"ONE
  Event spanning many rungs — sharding it per rung BREAKS `causes[]`, because ONE CAUSE IS ONE ID"*
  (`matter.py:37-40`, and the events are appended unsharded at `:51-53`). For such an Event
  `place_of(e.subject)` answers about one rung and the question does not reach the rest. **This file
  does not widen the signature**, for three reasons stated plainly: a set-returning `place_of` changes
  `_ch_co_located`'s predicate from membership to intersection, which moves every hash in the corpus;
  the multi-rung producer is `H-62`'s and `F.20a`'s territory, not this file's; and `ARCH §F.14` is
  RATIFIED text, so **widening it is RR-B's business, not an edit** (`05`). **Recorded as a LIMIT with
  its own falsifier, `AR-9`.**

---

## §A.4 · `reach(w, p)` — FOUR LIMBS, AND IT IS A FILTER

### §A.4.1 · The signature and the owner

```python
def reach(w: World, p: Person) -> set[str]:
    """The ids a question may be ABOUT for this person. `ARCH §A.2`: world-first, owns nothing,
    stored nowhere. A FILTER over what a WITNESS channel already deposited -- never a fan."""
    TRACE.query("reach", "resolver")
    R = {p.id}                                              # limb 1 -- me
    R |= {t.object for t in p.tenures if t.live}             # limb 2 -- mine
    cur, seen = home_of(w).get(p.id), set()                  # limb 3 -- the ladder above me
    while cur is not None and cur not in seen:
        R.add(cur); seen.add(cur); cur = parent_of(w, cur)
    for t in p.tenures:                                      # limb 4 -- purview
        if t.kind == "hold" and t.live and t.object in w.offices:
            rg = w.offices[t.object].rung
            if rg is not None:
                R.add(rg); R.update(descendants(w, rg))
    return R
```

**Owner: `engine/season/queries/world_q.py`, beside `descendants` (`:54`).** It writes nothing, holds
nothing and takes no token — `ARCH §A.2`'s `queries/world_q` row, verbatim.

### §A.4.2 · The four limbs, each with the walk it reuses

| limb | the set | the existing owner it composes on | why it is not a new rule |
|---|---|---|---|
| **1 · me** | `{p.id}` | — | it is today's first disjunct (`world_q.py:493`) |
| **2 · mine** | `{t.object for t in p.tenures if t.live}` | **the existing `mine` set**, `world_q.py:471`, unchanged | it is today's second disjunct. `Tenure` is *"THE ONE EDGE. Owned by its SUBJECT"* (`carriers.py:41`) |
| **3 · the ladder above me** | `ancestors_or_self(home_of(p))` | **`parent_of`** (`:48`), and the identical walk lives **twice** already: `predicates.py:135-140` (inside `under_purview`) and `world_q.py:432-436` (`conferral_path`) | a third hand-rolled copy is what `CLAUDE.md` §8 forbids; this is the fourth site and the one that should own the loop |
| **4 · purview** | `⋃ ({seat.rung} ∪ descendants(w, seat.rung))` over live holds on an Office | **`descendants`** (`:54`), *"the CONTAINMENT TREE and only it … ITERATIVE, with a visited set — the reference graph is cyclic ON PURPOSE"* | it is **exactly** `under_purview`'s relation, read forwards. `descendants` **excludes** the rung itself, so `{rung} ∪ descendants` is required for the two to agree — verified against `predicates.py:136-138`, where `cur == seat` returns `True` on the first iteration when `holding == seat` |

**Limb 4 is round one's Q5 `purview` surviving as a TERM OF REACH rather than as a fifth row.** That
is the whole of the difference between the two rounds on this subject: round one added a source, which
grows the roster, the sort, the `occasioned_by` dispatch and the aggregation arms; this adds a
disjunct to a boolean.

⚠ **And limb 4 must read the SEAT's rung, never the actor's post string.** `ARCH §B.7`, grade
MECHANICAL: *"purview is asked of the seat exercised, not the actor."* `under_purview` today asks it
of the actor's **post string**, via `titles_held` → `title_domain(o.post)` (`predicates.py:132`,
`:144-155`, `data/rosters.py:459`). **`reach` does not use `titles_held` and does not read a post.**
It reads `Office.rung`. That is `03`'s repair arriving here as a precondition, and §A.4.6 states what
it costs while `03` is unbuilt.

### §A.4.3 · What `reach` MAY and MAY NOT read

| may | may not | the clause |
|---|---|---|
| `w.tenures`, `w.offices`, `w.rungs` | **any person's `ledger`** — including p's own | `AX-2` (`:100`): a reach computed from beliefs would make *"what I may be asked about"* a function of what I believe, and then a false belief would silently widen the world I can act on |
| `p.tenures` (p's own edges, world state) | `w.log`, `w.acts` | `ARCH §B.9`, quoted in round one's `03`: *"`state/acts` is append-only, **resolver-side**, and no person-side Query reaches it"*; `ARCH §F.13` grades the guard CONVENTION and names the failure — *"attribution becomes world truth and `AX-2` breaks silently"* |
| — | **another person's tenures** | it would answer *"what is HE asked about"*, which nothing needs and which is a cross-holder read |

**It writes nothing.** `reach` is a pure function of `World` and a `Person`'s own edges, recomputable
at any barrier, with nothing to initialise and nothing to go stale. That is the same property
`in_force` was defended on in round one and it survives the round-one audit intact, because — unlike
`in_force` — **nothing at MATTER reads it.** It is read at DELIBERATE and nowhere else.

### §A.4.4 · Why it FILTERS and cannot widen the fan — the exact failure it prevents

**The claim, in three clauses, each independently checkable (§0.3).**

1. **The fan is `observers_for` and it is untouched.** `epistemic.py:405-441` decides which persons a
   given Event reaches, from `fan_out_mode` (`all_five`, `fixtures.py:328`) over
   `CHANNEL_PREDICATES` (`:392-402`, built from `rosters.yaml:127` so *"a channel with no function
   RAISES at import rather than silently never matching"*). **`reach` is not called from `witness` and
   does not appear in that dispatch.** The set of claims in every ledger is bit-identical before and
   after.
2. **`reach` is applied to `p.ledger` and to nothing else.** The Q2 loop is `for c in p.ledger`
   (`world_q.py:492`). **A claim not in the ledger cannot become a question no matter how wide
   `reach` is.** The ledger is the bound, and the bound is built by a place-and-hold test.
3. **The number of questions ANSWERED is fixed by the budget, not by the question count.**
   `aggregate_questions(qs, "first")` returns `qs[0]` (`decision/questions.py:62-63`). `scene_budget`
   is 5 (`fixtures.py:171`) and one question is asked per round (`driver.py:361-366`,
   `deliberate.py:102-108`). **1632 questions and 561 questions both reduce to one per deliberation.**

**The exact failure this prevents, named:** the alternative design — *"ask the duke about everything
in his purview"* — would have to reach into the world for facts the duke's ledger does not hold. That
is `AX-2` breached at the one place the engine has no defence, because `questions_for` is world-side
by signature (`world_q.py:15-19`: *"`questions_for` takes a `Person` as its SECOND argument and asks
the WORLD about them"*) and nothing downstream can tell a question sourced from the duke's ledger from
one sourced from `w.rungs`. **REACH is the construction that makes "ask him about his purview" mean
"ask him about what he has HEARD about his purview."** That distinction is the entire difference
between a governance layer and an oracle, and round one's own falsifier `SP-9` is written about
exactly it.

### §A.4.5 · Under RR-P — the principle, and what `reach` must not become

**RR-P** (`02`; Jordan, verbatim): *"the player must have the sanctity of their choices/actions/
decisions preserved in terms of the contents of those choices/actions/decisions themselves — the
worldly churn is in how those contents are received and acted upon by others."* **The test: a draw
may decide what HAPPENS, never what you MEANT.**

**`reach` is on the safe side of that line and it is worth saying why, because the neighbouring design
is not.** `reach` decides **which of the claims a person already holds are put to them as questions**.
It touches no `Act`, no `payload` and no operand. `Act.payload` is written at DELIBERATE and by
nothing after (`write_matrix.yaml:72-78`: `(Act[], returned)`, `steps: [DEL]`, `by: "DELIBERATE writes
nothing else"`). **The forbidden neighbour is a `reach` that RANKED the questions by anything other
than the declared order plus the declared tiebreak** — because a ranking is the engine deciding which
of a person's concerns is their concern, which is round one's `03` §A.6.3 rule 5 (*"competing causes
are shown UNRANKED"*) applied one layer down. **This file changes no ranking.** §A.10.

**And this file does not assume RR-P settled.** The sentence above is *"consistent with RR-P if RR-P
is ruled"*, not *"licensed by RR-P."*

### §A.4.6 · THE HONEST STATE OF LIMB 4 — inert, twice over, and kept anyway

§0.2e measured it: **the purview limb adds zero questions on `build_realm(0)`, for two independent
reasons.** Both are stated here as limits with named owners, because §0.1 pt 3's *"X works today"* row
demands the CALL SITE and not the declaration.

| reason it is inert | owner | when it lifts |
|---|---|---|
| **16 of 19 `Office.rung` are `None`** (`populated.py:640-735`) so the limb is the empty set for 16 of 19 holders | **`03_SEATS_AND_CONTENT.md`** — `engine/season/data/offices.yaml`, *"every seat has a `rung`"* | `03`'s build item. **Until then limb 4 fires for three seats** |
| **a claim about a place is in your ledger only if you were AT that place**, because the live channels are `co_located` (a place test), `witness_key` (self or a knot) and `document_key` (a hold on a CHANGED thing) — and the crossing Event's `changes[]` is **empty** (`matter.py:269`, asserted at `test_season_shape.py:1131`), so `document_key` cannot see a crossing | the WITNESS layer. `_ch_post_remit` is the one channel in the roster that could deposit a claim about a place its holder did not attend, and it is **inert** (`hole_register.yaml:640`: *"ONLY `post_remit` IS INERT NOW"*) | **`02`'s §2.2g re-bases `_ch_post_remit`** onto co-located obligees, which keeps it place-bound — **so `02` does NOT lift this.** The lift is `document_key` seeing a store change at a rung a person holds, which arrives when `04`'s larder write and the 16 faction-subject holds' re-homing land (`05` item 16) |

**So why keep limb 4 at all?** Three reasons, and the third is the only strong one.

1. *It is the only formulation under which the SEAT is what reaches.* `ARCH §B.7` is MECHANICAL and
   says purview is the seat's. Any design in which a duke's attention is a function of his person and
   not of his seat has to re-decide that ratified line.
2. *It costs one disjunct and zero objects.* It is `descendants`, which exists, over `Office.rung`,
   which exists.
3. **It is the term that makes the inertness VISIBLE AND FALSIFIABLE.** Today "a duke is not asked
   about his duchy" is indistinguishable from "there is no such thing as a duchy-wide question."
   With limb 4 present and measured at zero, the zero is a **claim about the witness layer** with a
   named owner and a test that fires the day the owner ships (`AR-4`). **That is the difference
   between a gap and a hole with a row.**

⚠ **What this file will NOT do to make limb 4 fire.** It will not invent a channel, will not widen
`observers_for`, will not give the crossing Event a `changes[]` it does not have, and will not add a
`post_remit`-style place-blind predicate. **A limb that reaches nothing is honest; a channel invented
to feed it would be the broadcast `holonic §37.3` forbids, arriving through the attention layer
instead of the policy layer.**

---

## §A.5 · THE Q2 ADMISSION TEST — three clauses, and only two ship in this file's item

**What it is today** (`world_q.py:493`):

```python
if (c.when, c.round) >= floor and (c.subject == p.id or c.subject in mine):
```

**What it becomes:**

```python
R = reach(w, p)
for c in p.ledger:
    if (c.when, c.round) < floor:
        continue
    if (c.subject in R                                  # clause 1 -- the thing itself
            or place_of(w, c.subject) in R               # clause 2 -- where the thing is
            or any(x in R for x in named(c))):           # clause 3 -- whom the CONTENT names
        out.append(Question(f"q:claim:{c.id}", "claim_landed", (c.subject,), c.id))
```

### §A.5.1 · Clause 1 — `c.subject in R`

**Strictly wider than today's test and measured to admit exactly as much:** 561 → 561 (§0.2d). It
generalises `c.subject == p.id or c.subject in mine` by two limbs that currently add nothing. **The
`since` floor is untouched** — it stays the first conjunct and is evaluated first, so a landed-claim
question is still *landed*, not *held*.

### §A.5.2 · Clause 2 — `place_of(w, c.subject) in R`

**This is the clause that does the work: 561 → 1632.** In plain terms: *you are asked about a thing
that is where you are, where you hold something, on the ladder above you, or within your seat's
purview.* And it is what folds Q3, because a crossing's claim has the **site** as its subject
(`claim_subjects` falls back to `[e.subject]` for a write-nothing Event, `epistemic.py:134`, `:139-145`;
`claim_subject_rule` ships `both`, `fixtures.py:416`) and `place_of(site)` is `site.rung`.

⚠ **`None in R` must be impossible, and it is, by two independent constructions.** `place_of` returns
`Optional[str]`; 163 of the 2175 claim instances have a subject with no place (Propositions).
`R` is a set of ids and `None` is not an id — but *relying on that* is the kind of accident this tree
has been bitten by. **The clause is written `(pl := place_of(w, c.subject)) is not None and pl in R`**,
and `AR-6` is the falsifier: plant a claim whose subject is a Proposition, assert it is admitted by
clause 1 or not at all, **and assert that the run with every rung removed from `R` admits zero** — the
control that distinguishes "None is excluded" from "the test is vacuous."

### §A.5.3 · Clause 3 — `named(c)`, AND IT DOES NOT SHIP WITH THIS FILE'S ITEM

`named(c)` is *the id set inside `c.value` when `c.predicate` starts `content:`* — `02`'s document
rule. It is what makes **a writ naming you a question without a place query**, which is the whole of
`holonic §37.3`'s *"scope enumerates EXECUTORS, not places."*

⚠ **And it has NO PRODUCER TODAY (measured, §0.2f):** every witness-deposited claim has
`predicate = e.kind` and `value = True` (`witness.py:191`). **A clause with no producer is exactly
what this file deletes two of.** So:

> **RULED: clause 3 lands with `02`'s deposit rule, in `05`'s build item 7 — not with item 2.**
> Item 2 ships clauses 1 and 2 and the fold. `named(c)` ships in the same commit as the first claim
> that can satisfy it, and its falsifier (`AR-5`) is written to go **red before** that commit and
> green after.

**Step of the gate that decided it:** step 5 — where 1-4 are silent but one option is clearly right
for the code. Shipping a dead clause and shipping the two deletions in one commit would make the
commit self-contradictory.

### §A.5.4 · What the three clauses are NOT

- **Not a fourth source.** One `Question` shape, one `source` string, one `occasioned_by` route.
- **Not a read of another person's ledger.** `for c in p.ledger`, unchanged.
- **Not a widening of `referents`.** The Question is still `(c.subject,)`. A claim admitted by clause
  2 is a question **about the thing**, and `_derive_operand` binds `subject`/`to`/`site` to it
  (`options.py:307-312`) exactly as before. **No new operand and no new referent semantics** — which
  is why `requires_operands` (`rosters.yaml:1084`) is untouched by this file. (`02`'s `at` operand is
  `02`'s object to count, and `05`'s ledger carries it.)

---

## §A.6 · Q1 FOLDS IN — CALENDAR EMITS WHAT ITS OWN ROW DECLARES

**The change, at `engine/season/loop/calendar.py:37-38`.** Today:

```python
w.write("Date", WriteClass.CALENDAR, lambda d=d: d.__setitem__("fired", True),
        record_kind="Date", fieldname="fired", driver="Event")
```

Becomes:

```python
w.write("Date", WriteClass.CALENDAR, lambda d=d: d.__setitem__("fired", True),
        record_kind="Date", fieldname="fired", driver="Event",
        emits="date.fired", subject=(d.get("venue") or did), causes=[ROOT])
```

⚠ **THIS IS A THREE-ARGUMENT CHANGE, NOT THE ONE-ARGUMENT CHANGE MY PLAN CLAIMED**, and the gate is
what says so. `World.write` (`state/world.py:295-460`), opened:

| argument | why it is required | the refusal if omitted |
|---|---|---|
| `emits="date.fired"` | the declared kind, `write_matrix.yaml:111`; parsed to `("date.fired",)` at `data/matrix.py:144` | without it, no Event — the `if emits is not None` guard at `world.py:411` |
| `subject=` | **`world.py:417-431` RAISES `Forbidden` on an emission with no subject**, and its law paragraph is the worked history: *"THE SUBJECT IS THE RECORD, NOT THE TRACE LABEL … every site's wear emitted under the subject `"condition"`, so `last_emission_of` never matched and the clock re-rooted every season"* | `Forbidden(... "S33")` |
| `causes=` | **`Event.__post_init__` raises on an empty `causes[]`** (`carriers.py:118-125`, `"S19.4"`), and `world.py:452-457` refuses to default it: *"A caller with no antecedent must say so by passing `[ROOT]` itself"* | `Forbidden(... "S19.4")` |

**`[ROOT]` is correct here and is not a shrug.** A date firing because the calendar reached it has no
antecedent Event in this tick — `ARCH §A.2`'s `loop/calendar` row and `write_matrix.yaml:110`'s
`by: "DR-3 · §24 has no actor"` both say a date fires with no author. The *act that wound the clock*
is the `convene`, seasons earlier, and the design's own rule for a clock's genuine first emission is
`[ROOT]` (`matter.py:234-239`). ⚠ **A better `causes[]` exists in principle** — the `convene` act's
Event — and it is not taken here because reaching it means a log search from CALENDAR, which is
`occasioned_by`'s job and not the gate's. **Named as a deliberate narrowing, with `AR-8` asserting
`causes == [ROOT]` so that a later improvement is a visible diff.**

**`subject` is the VENUE, falling back to the date id.** `_req_convene` guarantees a venue is a rung
with a parent (`predicates.py:306-309`), so `place_of(date)` and the Event's subject agree by
construction; the fallback covers a date planted by a harness that set no venue
(`probes.py:1179`, `:1349-1350` do exactly that).

**Then the chain, as execution, with nothing invented:**

| # | what happens | whose act | step | written | emitted | witnessed by |
|---|---|---|---|---|---|---|
| 1 | a sitting is scheduled | the convener's `convene` | RESOLVE | `(Date, due_at)` | `date.scheduled` (`write_matrix.yaml:99`) | the fan |
| 2 | the date comes due | **nobody's act** — CALENDAR reaches it | CALENDAR | `(Date, fired)` | **`date.fired`, subject = the venue** | `_ch_co_located` over `presence(venue)`; `_ch_witness_key` for anyone the venue-id knots |
| 3 | the claim lands | WITNESS | WITNESS | each observer's `ledger` | `claim.deposited` | — |
| 4 | the question forms | **nobody's act** | DELIBERATE | nothing | — | clause 1: the claim's subject IS the venue rung, and a venue is in the reach of whoever is there, whoever holds it, and whoever's seat's purview contains it |

**What this buys that Q1 did not have.** The addressing goes from *"everyone, because `holder` is
`None`"* to *"whoever was at the venue, plus whoever holds it, plus whose seat reaches it"* — which is
`holonic §37.3`'s *"delivery is not assumed"* honoured rather than asserted. The question acquires a
`when` and a `round`, so it stops being eternal. And the dead `occasioned_by` route becomes the LIVE
one, because a `claim_landed` question walks to the originating Event via `claim.deposited`
(`world_q.py:611-615`) — **the date Event is now in the log with an id**, which is precisely what
`:571-577` says is missing.

⚠ **THIS MOVES HASHES AND THE PROPOSAL SAYS SO.** A new Event kind in every log that runs CALENDAR
with a due date changes `World.content_hash()` and every golden through CALENDAR. **The re-record is
DECLARED**, per `CLAUDE.md` §7 (*"nothing verifies a golden re-pin was intended — so say plainly when
you re-record one"*), and `05`'s item 2 carries it. On `build_realm(0)` the change is a no-op today —
**0 dates** — which is the honest size of it: the fold makes Q1 correct for a world that does not yet
convene, and `03`'s `convene`-capable seats are what make it bite.

**And this file does NOT claim Q1's fold runs before the emit lands.** Nothing above executes.

---

## §A.7 · Q3 FOLDS IN — THE CROSSING IS ALREADY A CLAIM, AND NOBODY WAS READING IT

**Nothing is added. Nothing is even changed at MATTER except one deletion.** The measurement at §0.2c
is the whole argument:

| what exists today | citation |
|---|---|
| the crossing **Event** — `kind="condition.band_crossed"`, `subject=s.id`, `causes=[the wear Event]` | `matter.py:267-270` |
| it is appended to `w.log` **and** returned in `emitted`, so WITNESS fans it | `matter.py:271`; the barrier returns `emitted` at `:296`, and `:279-285` records the bug fixed to make that true |
| it is witnessed **co-located**: `place_of(site) = site.rung`, `presence` index | `epistemic.py:253-257` |
| the deposit's subject is the **site** (write-nothing Event → `[e.subject]`) | `epistemic.py:134`, `:139-145`; `witness.py:181` |
| the claim carries `when`, `round`, `source`, `confidence` | `witness.py:191`; `carriers.py:147-156` |

**So the crossing already becomes a claim in the ledger of everyone present. Q3 was reading a second
copy of the fact and building a malformed question out of it.**

**After the fold**, the same crossing raises a question through clause 1 (`c.subject` is the site, and
a person present holds the site's rung in `mine`... not necessarily — `mine` holds the rung only via
`contain`, so the admitting clause is **clause 2**: `place_of(site) = site.rung ∈ R` for anyone whose
home is that rung, who holds it, who is above it on the ladder, or whose seat's purview contains it).
And:

- **the referent becomes the SITE id**, not `"full_operations"` — because the Question is built from
  the claim (`(c.subject,)`), and `c.subject` is the site. **`H-110` dissolves** (§A.9).
- **the site-use verb is not lost.** It is recoverable from `c.predicate`, which is the Event kind
  `"condition.band_crossed"`, plus the site's own `condition` against `band_floors[site.kind]`
  (`rosters.yaml:1189-1199`) — a read the world answers, exactly as `work` reads its floor as a
  *"SECOND READ on the site (`threshold_predicate`)"* rather than as an operand
  (`options.py:300-301`). ⚠ **What IS lost is WHICH floor was crossed when two floors sit between
  `before` and `after`.** `harbour` has two (`800`, `100`), `seam` two, `body` three; the loop at
  `matter.py:261-277` emits **one Event per crossed floor** with `id = H(seed, tick, s.id,
  f"crossing:{verb}")`, so the verb is in the **Event id** and the two Events are distinct. A reader
  who needs the verb reads the Event, which `occasioned_by` now returns. **Stated as a narrowing with
  falsifier `AR-7`, not waved away.**
- **the question acquires a clock.** `(c.when, c.round) >= floor` bounds it to the round it landed in.
  **30 questions from one crossing becomes 2** (the two present persons, once each).

⚠ **A finding I owe the reader, because it is a contradiction in the tree and my plan got it
backwards.** `rosters.yaml:814-815` says *"⚠⚠ `body` IS NOT A SITE. It is `(Person, body)`'s band
row, here because `band_floors` keys on THIS roster."* **And `headless.build_world(0)` builds
`Site('scriptorium', 'hearth_ostvik', kind='body', condition=1000)`** — a Site whose kind is `body`,
whose floors (`full_operations: 800`) are the ones the §0.2c measurement crossed. So the roster's
note is false of the corpus. **This is `04_MATTER_AND_WORKS.md`'s to resolve** — it owns
`band_floors.person` and the body write — and it is named here because my crossing measurement runs
on that site and a reader must not think the crossing was a harbour's.

---

## §A.8 · `w.crossings` IS DELETED — the complete reader census

**One fact, two carriers (§A.1.3 pt 3). The Event survives; the tuple list goes.** Every mention in
the tree, classified — `grep -rn 'crossings'` over `engine`, `tools`, `tests`, minus the
`band_crossed`/`condition.band` string matches:

| site | what it is | what happens |
|---|---|---|
| `state/world.py:176` | the declaration: `self.crossings: list[tuple] = []` | **deleted** |
| `loop/matter.py:272` | the only writer | **deleted** (one line inside the `if before >= floor > s.condition` block; the Event above it stays) |
| `queries/world_q.py:514` | **the only production reader** — Q3's loop | **deleted with Q3** |
| `queries/world_q.py:497` | Q3's docstring, *"the loop records them on `w.crossings`"* | deleted with Q3 |
| `harness/probes.py:680`, `:2562` | `mine = lambda: [c for c in w.crossings if c[0] == site.id ...]` — two probes | **migrated** to `[e for e in w.log if e.kind == "condition.band_crossed" and e.subject == site.id]`. The probes lose the `before`/`after` numbers, which they read only to assert a crossing happened |
| `tests/test_season_shape.py:469` | the `INFRASTRUCTURE` exclusion set of `content_hash`'s completeness guard, with its own rule: *"each is named rather than pattern-matched so that adding one is a deliberate act"* | **`"crossings"` removed from the set.** The guard then passes because the attribute is gone. ⚠ **This is the one test whose PASS is ambiguous and it must be checked by mutation**: dropping the name from a set and dropping the attribute both make it green. `AR-3`'s control is to assert `not hasattr(w, "crossings")` directly |
| `tests/test_season_shape.py:1124`, `:1127` | the 23-season crossing test reads `w.crossings` to find the Event id at element 4 | **migrated** — it wants the Event, and the Event is in `w.log`. Its own assertions (`ev.kind`, `not ev.changes`, `ev.degree is None`) are on the Event already |
| `tests/test_season_shape.py:2386`, `:2406-2407` | the `band_crossed` arm of `test_w5_q_has_a_producer_across_all_four_sources` | **deleted with the arm** (§A.8.1) |
| `tests/test_season_shape.py:3699-3700` | the `W4` antecedent test — reads **`w.log`**, not `w.crossings` | **untouched. It is the test that proves the Event carries everything the tuple did** |
| `loop/deliberate.py:414`, `decision/options.py:278`, `hole_register.yaml:2698` | docstrings naming Q3's input | **corrected in place** |

**Nothing outside `engine/season` reads it.** The `params_tables.yaml` and `cases/*.yaml` hits are the
English word *crossings* in TTRPG prose and are not this object.

### §A.8.1 · The roster edit, and the five sites that must move in the same commit

`rosters.yaml:270` becomes `values: [claim_landed, need]`. **Five consumers, and `ARCH §B.13`'s
cross-validation principle is why they are one commit and not five:**

| site | today | becomes |
|---|---|---|
| `data/rosters.py:355` | `QUESTION_SOURCES = roster("question_sources", ordered=True)` | unchanged — it reads the roster |
| `state/carriers.py:255-260` | `Question.__post_init__` refuses an unrostered source, with `needs="add it to rosters.yaml, or **use one of the four**"` | the message's **"four"** becomes "two". ⚠ A hardcoded count in a refusal string is exactly `CLAUDE.md` §0.05 clause 1's defect at its smallest scale |
| `queries/world_q.py:616` | `if q.source not in ("date_due", "band_crossed"): raise Unspecified(...)` — the negative guard | **the guard becomes `if q.source != "claim_landed": raise`**, and the generic id search at `:630-634` loses its only reachable caller and is **deleted**. `need` still returns early at `:609` |
| `queries/world_q.py:439`, `:451` | the docstring: *"FOUR sources"*, *"§F1 says all four are already produced by the loop"* | rewritten to two, with the fold's reasoning and the §0.2 measurements |
| `tests/test_season_shape.py:2361-2369` | `test_w5_q_has_a_producer_across_all_four_sources`, looping `for src in QUESTION_SOURCES` with an arm each and `else: pytest.fail("the roster grew a source this test does not exercise")` | **renamed** to `..._across_both_sources`; the `date_due` and `band_crossed` arms deleted; **the `else` guard KEPT**, because it is the thing that fails if anyone re-adds a source without an arm |

⚠ **And the `date_due` arm's deletion removes a live instance of `CLAUDE.md` §0.1 pt 2 from the
suite.** That arm plants `w.dates["d_t"] = dict(due_at=0, holder=p.id, fired=False)` at `tick 0`
(`test_season_shape.py:2373`) — **a state CALENDAR cannot leave behind** (§0.2b). It is the same
defect the `band_crossed` arm three lines below it was *repaired for*, and whose repair is written out
in that arm's own comment: *"REV 1 PLANTED A TUPLE THE WRITER NEVER PRODUCES, AND SO TESTED ITSELF."*
**The `date_due` arm still tests itself, one branch above the comment recording the lesson.** Found by
running arms A/B/C rather than by reading the test.

---

## §A.9 · WHY `H-110` DISSOLVES RATHER THAN BEING FIXED

**`H-110`'s own row** (`engine/season/hole_register.yaml:1533`), tier 1, kind `WIRING`, grade
`absent`, owner *"`queries/world_q.py` — `questions_for`'s Q3 branch"*:

> **hole:** *"A BAND CROSSING KNOWS WHICH EVENT IT WAS AND THE QUESTION IT RAISES THROWS THAT AWAY.
> `matter()` records a crossing as `(site_id, verb, before, after, ev.id)` and `questions_for` builds
> `Question(..., "band_crossed", (what,), what)` where `what` is the VERB. So the question's `about`
> is a verb name, not an id, and nothing can walk from a band-crossed question to the Event that
> crossed the band."*
>
> **cite:** *"FOUND BY AN ADVERSARIAL PASS OVER THE `N3` FIX, WHICH HAD DOCUMENTED THE ROUTE AS
> LIVE. … **⚠ THE FIX IS ONE LINE AND IS NOT TAKEN HERE ON PURPOSE:** the crossing Event id is
> already in the tuple, and carrying it onto the Question changes a surface `occasioned_by` does not
> own — `questions_for` is §F1's Q3 and its shape is what `H-54` and the aggregation rule read.
> **A one-line change to a rule three other rows depend on is a design edit, not a repair.**"*

**Round one spent a great deal on this.** Its `01` §A.15 and its APPENDIX both carry it, and its
APPENDIX records a citation repair against its own sources — *"`world_q.py:520` (Q3's referent) →
actually `:518`; the one-line fix is aimed at the wrong line."* Its `03`'s RULED causation line names
it as one of the two reasons the from-below chain does not fire:

> *"A short larder **emits nothing** (`matter.py:179-185`) and Q3's referent is a site-use string
> (`world_q.py:518`, `:580-588`), so the from-below chain's first two links do not fire."*
> — round one `03_THE_SURFACE.md`

**Under the fold there is no `band_crossed` source to mis-bind.**

| | fix it | dissolve it |
|---|---|---|
| the edit | carry `ev.id` onto the Question: `Question(f"q:band:{ev_id}", "band_crossed", (site_id,), ev_id)` | delete Q3; the crossing's claim raises a `claim_landed` question |
| what the row's own caveat says about it | **it is a DESIGN EDIT** — it changes the shape three rows read (`H-54`'s aggregation, `occasioned_by`'s dispatch, the `q.id` tiebreak) | the same three rows are changed **by the fold**, which is a design edit that is being proposed as one, with its ruling-gate steps named (§A.2) |
| what is left afterwards | a fourth source, still eternal (no clock on the tuple), still a second carrier of one fact, still addressed by `presence` rather than by reach | one source, with a clock, one carrier, addressed by reach |
| object count | ±0 | **−1 question source, −1 World collection, −1 matrix-less carrier of a duplicated fact** |
| `H-110` | **closed as WIRED** | **closed as DISSOLVED** — the hole was *"the question throws the Event away"*, and there is no such question |

> ### RULED: `H-110` closes as DISSOLVED, not fixed. Its subject — the `band_crossed` question — ceases to exist, and the Event it named is what the surviving source reads.

**The distinction matters for the register and is not cosmetic.** A row closed as WIRED tells a later
session *"the mechanism now works"*; a row closed as DISSOLVED tells them *"the mechanism is gone,
and if you re-add a question source that does not read a claim, this row comes back."* `05` carries
the row's closing text.

**And `H-110`'s own caveat is honoured rather than side-stepped.** It refuses to make the one-line
change **as a repair**. This file makes a larger change **as a design edit, with the gate run and
the step named**, which is exactly the disposition the row asks for. ⚠ **It does NOT claim `H-54`'s
tiebreak is anything but a hash** (§A.1.5) and it changes no line of the sort.

---

## §A.10 · THE NARROWING, MEASURED RATHER THAN CONCEDED

`rosters.yaml:260-261`: *"ORDER IS SEMANTIC: `q`s are produced in this order and a person's questions
arrive in it, so editing the order changes which question a budget-bounded person answers first."*
**Folding four into two edits that order. What exactly is lost:**

| the ordered pair | is it live? | after the fold |
|---|---|---|
| `date_due` **before** `claim_landed` | **NO.** Q1 produces zero questions in every world (§0.2b, with control) | **nothing is lost.** An order between a live source and an unreachable one decides nothing |
| `date_due` before `band_crossed`, `date_due` before `need` | **NO**, same reason | nothing |
| `claim_landed` **before** `band_crossed` | **YES, in a world that has run ~20 seasons.** Measured: site at 805, 3 seasons → 140 `claim_landed` and 30 `band_crossed`, and every crossing question sorted **after** every claim question | **LOST.** A crossing question is now a `claim_landed` question and takes the within-source hash tiebreak among them |
| `claim_landed` **before** `need` | **YES, and it is the one that has ever decided anything** | **PRESERVED.** Two sources, same relative order |

**The one real loss, stated precisely:** a band crossing used to be answered **last**, after every
landed claim; now it competes on hash. And the argument for accepting it is not *"orders are
arbitrary"* — it is that **the old order encoded KIND OF SOURCE, and under one source there is no kind
left to encode.** The honest tiebreak among questions of one kind is the deterministic one the tree
already has and has already adjudicated: `H-54` (`hole_register.yaml:618`), closed at step 4 with
`needs_jordan: false`, *"NO RULE IS CHANGED … editing that sort is a design edit to a line three rows
depend on."*

⚠ **And the preserved pair is load-bearing in a way that is easy to miss.** `harness/populated.py:577-585`
records that *"`question_sources` puts `need` LAST, so a creed never displaces a date or a landed
claim — but the person's OWN want is also a `need`, and `questions_for` breaks a within-source tie on
`q.id`. `q:need:fac_…` sorts before `q:need:prop_…`, so under `first` **every member's faction creed
silently outranks their personal ambition, decided by the spelling of an id.**"* **The fold does not
touch that.** `claim_landed` stays ahead of `need` and the `need`-internal tie stays a hash. Saying so
matters because a reader could otherwise think the fold moved a measured behavioural asymmetry that it
leaves exactly where `H-54` and `W-D` left it.

### §A.10.1 · The `one_per_source` arm narrows, and that is a real cost

`aggregate_questions`'s arms are `first | all | one_per_source` (`decision/questions.py:45-73`;
`H-54`'s declared sweep). `one_per_source` keeps at most one question **per source** and then folds
their referents into one aggregate Question (`:70-73`). **With four sources it keeps up to four; with
two it keeps at most two.** So the fold **halves the widest referent set the sweep's middle arm can
build.** This is not a defect of the shipped arm (`first` returns `qs[0]` and is unaffected) and it is
a genuine narrowing of a declared sweep point. **Recorded here rather than in a footnote, because
`H-54` is `assumption`-graded and a later session will run that sweep.** The alternative — keeping a
source alive so a sweep arm has more to fold — is `ID-13` inverted and is refused.

---

## §A.11 · THE NERS ARGUMENT, WITH EACH LINE'S CUT AND WHETHER IT SURVIVES

Per `CLAUDE.md` §0.06 and `skills/ners/SKILL.md`: **a PASS is licensed by a named FAILED attack, not
by an absent finding; E is scored LAST as a ratio; withholding is symmetric.**

**N — each line with the cut that would show it false, and the honest verdict.**

| N-line | the cut | verdict |
|---|---|---|
| **the FOLD** (two sources out) | keep `date_due` and `band_crossed`: two sources produce 0 and 30-from-one-crossing questions respectively, one is unreachable, one is eternal and malformed, and `occasioned_by` has no route for either | **PASSES.** The attack that would break it — *"they fire and you deleted them"* — was run in both directions with positive controls (§0.2b, §0.2c) |
| **clause 2, the place clause** | remove it: **1632 → 561 questions, a 65% loss**, and Q3's fold has nothing to land on | **PASSES**, and it is the only line here whose cut is measured to hurt |
| **`place_of` as a named function** | leave `_event_place` private: then the record and date limbs live in `epistemic`, which `ARCH §A.2` types as WITNESS's module, and `world_q` cannot ask where a thing is without importing it — a direction the one-way rule forbids (`world_q.py:15-19`) | **PASSES**, on a structural argument rather than a measurement |
| **CALENDAR's emit** | leave it silent: Q1's fold has no Event, `occasioned_by`'s date route stays dead, `ARCH §A.2`'s `loop/calendar` row stays false of the code | **PASSES on conformance, UNMEASURABLE on effect** — 0 dates in the corpus. Honest grade: the cut cannot be run today |
| **limb 4, purview** | remove it: **zero questions change** (§0.2e) | ⚠ **NARROWED, NOT PASSING.** Kept on §A.4.6's third argument (it makes the inertness falsifiable), not on an N-line |
| **limbs 1-3 as a named `reach` rather than three disjuncts** | inline them: the ancestor walk becomes its **fourth** hand-rolled copy (`predicates.py:135-140`, `world_q.py:432-436`, here) | **PASSES on `CLAUDE.md` §8**, which is a rule and not a measurement, and is graded as such |

**E — attacked in order, each answered or conceded.**

1. *"REACH floods a duke's questions."* — **Half true and the half that is true is conceded.** The
   question LIST triples (561 → 1632); the ANSWERED count does not move (one per deliberation,
   `questions.py:62-63`); the ledger does not move at all (`observers_for` untouched). **Conceded: a
   1632-element sort where 561 stood.** `questions_for` is called once per person per round —
   46 × 5 = 230 calls per season on `build_realm(0)` — and the sort is O(n log n) over a list built
   by a single pass over a ledger the loop already walks. **No new scan.**
2. *"Three clauses where one stood is three times the boolean."* — **Conceded as +2 clauses**, and
   one of them (clause 3) does not ship in this file's item (§A.5.3). The alternative — one clause
   over a precomputed per-person id set — is a cache with a lifetime, and `queries/cache` is *"barrier
   indexes … at a barrier only"* (`ARCH §A.2`). A reach cache is an optimisation for a cost nothing
   has measured.
3. *"`place_of` returning `Optional[str]` where `ARCH §F.14` says a set."* — **Conceded as a LIMIT,
   with falsifier `AR-9` and an owner (RR-B).** §A.3.1.
4. *"the crossing's site-use verb is no longer on the Question."* — **Answered:** it is on the Event
   (which `occasioned_by` now returns) and in the Event's id; and it was never usable where it was,
   because a verb name in a referent slot forms a Candidate about a verb name. **Conceded:** a reader
   who wanted the verb without a log read has one more hop.
5. *"`one_per_source` narrows."* — **Conceded, §A.10.1.** No mitigation offered.

**E scored LAST, as a ratio against what N and R found** (`CLAUDE.md` §0.06: *"an audit that scores
four axes and averages them rates an amputated design as elegant"*). This file's engine additions are
**two names** (`reach`, and the clause-2 disjunct inside `questions_for`) plus **one move**
(`place_of`) against **five removals** (§B.2). Of the two additions, **one — limb 4 of `reach` — is
conceded as not carrying an N-line today.** So the ratio is *one N-carrying addition, one narrowed
addition, five removals.* **E passes**, and it passes because the design is mostly subtraction, which
is the only way E passes without amputation.

**R — the world must generate questions with no player in any seat.**

| generator | runs unwatched today? | after the fold |
|---|---|---|
| wear → crossing → claim → **question** | **the first three links run** (74 `condition.worn` per season on `build_realm(0)`; 30 crossing questions on a seeded site) and the fourth produces a malformed referent | the fourth link is well-formed and clocked. **Measured as running: `AR-2`** |
| a date firing → the convener and the venue's occupants are asked | **no** — 0 dates, and Q1 unreachable | runs the day a `convene` resolves. `03` supplies the seats |
| a claim landing anywhere in reach → a question | **runs: 561 per season, no player** | 1632 per season |
| **dearth → body → crossing → question** | no — the body write does not exist (`(Person, body)`, `write_matrix.yaml:161-167`, **no writer**) | **`04`'s**, and it lands on **this file's** clause 2: the hearth's bodies cross `failing`, the claim's subject is the person, `place_of(person)` is the hearth, and the reeve whose reach contains the hearth is asked. **That is Jordan's "a provincial policy on farming taxation ends up impacting a hearth", and the step where it becomes a QUESTION is clause 2** |

**R-COMPLETENESS at the extremes**, per `CLAUDE.md` §0.06 (*"a mechanism breaking at its extremes
fails"*):

| extreme | behaviour | where it is checked |
|---|---|---|
| a claim whose subject has **no place** (163 of 2175 — a Proposition) | `place_of` returns `None`; the clause is written to exclude `None` explicitly | `AR-6`, with its control |
| a person contained **nowhere** | limb 3 is empty (`home_of` has no entry); limbs 1, 2, 4 still answer. `_event_place`'s own `return None` at `:233` is the precedent | `AR-6` |
| a **record with no live holder** | `hold_force` returns `None`; `place_of` falls back to `Record.rung`, which is non-optional (`carriers.py:426`) | `AR-6` |
| a record with **two live holders** | **`hold_force` RAISES `Forbidden`** — *"S15 — `hold` cardinality is 1 PER OBJECT"* (`world_q.py:138-144`). `place_of` therefore raises rather than guessing | stated, not swallowed. `AR-6` asserts the raise |
| a **date with no venue** | the Event's subject falls back to the date id; `place_of(date)` returns `None` and the claim is admitted by clause 1 only (its subject IS the date id, which is in nobody's reach) — **so a venueless date reaches nobody** | `AR-8`. **This is correct**: a sitting nowhere is a sitting nobody attends |
| a **person who holds a seat whose rung is `None`** (16 of 19) | limb 4 contributes nothing; no raise, no default | `AR-4` |
| the **root rung** | limb 3 terminates at `parent_of == None`; `descendants(root)` is 374 of 375 rungs, and the King's `|reach|` measures **369** | §0.2e |

**S — the smooth axis, and its two tests the shorthand drops.**

- *pauses correctly*: nothing here decides anything. `questions_for` returns a list; `aggregate_questions`
  picks one; `assemble` builds a View. **A question is an occasion, never an outcome** — the same rule
  `holonic §24` states for a sitting and `matter.py:274-277` states for a crossing.
- *calculations consistent in methodology*: **one walk for reach and purview** (`descendants`), **one
  walk for the ladder** (`parent_of`), **one place function** for persons, sites, records, dates and
  rungs, **one claim shape**, **one Question shape**, **one `occasioned_by` route**. ⚠ **S fails if
  this file needs a second address type or a second ladder, and it does not** — the one place it comes
  close is `place_of`'s five limbs, which are five lookups in one function rather than five functions.
- *zooms in and out*: the same clause 2 admits a hearth's crossing to a reeve and a realm's date to a
  King, because both are `place ∈ R` over the same ladder.

---

# PART B · WHAT THIS ADDS, AND WHAT IT MAKES UNNECESSARY

**The bar**, from round one and kept: `ID-13` (`AX §B`'s *"A DECLARED FIELD MUST REACH A READER, OR IT
IS NOT DECLARED"*) — **an addition names its reader in the same row**. And `skills/ners/SKILL.md`'s
meta-rule: **a fix that adds a system has failed.**

## §B.1 · The table

| added | new primitive? | its reader, named | what it makes unnecessary |
|---|---|---|---|
| **`reach(w, p) -> set[str]`** | **no** — a set union of four existing walks, owned by nobody, stored nowhere | `questions_for`'s Q2 clauses 1-3, and nothing else | **round one's fifth question source Q5 `purview`** (a roster member, a sort position, an `occasioned_by` route, an aggregation arm and a falsifier); any per-person attention table; any "governed rungs" field on a person or a seat |
| **`place_of(w, x) -> Optional[str]`** | **no** — `ARCH §F.14`'s own name; `_event_place` PROMOTED, +2 limbs | `_ch_co_located` (its existing caller), `questions_for`'s clause 2, and `04`'s larder walk | `_event_place` as a private helper; **the fifth hand-rolled home-of-a-person lookup** (`home_of`'s docstring names four); a place field on `Record` or `Date` |
| **clause 2 of the Q2 test** | **no** — one disjunct | `questions_for` | **Q3 entirely**: `w.crossings`, its loop, its `presence` call, its malformed Question, `H-110` |
| **`emits=` / `subject=` / `causes=` on CALENDAR's write** | **no** — three arguments on an existing call to an existing gate, on a row that already declares the kind | `observers_for`; `occasioned_by`'s now-live route; clause 1 | **Q1 entirely**: its dict scan over `w.dates`, its universal addressing clause, its unsatisfiable `not fired` guard, its dead `occasioned_by` route |

## §B.2 · THE DELETION ARITHMETIC FOR THIS SUBJECT — objects out against objects in

**Counting rule, `05`'s and the suite's single owner of the total:** one row per NAMED thing a reader
must hold — a verb row, a roster member, a field, a Query, a helper, a `World` collection, a matrix
row. **A body for an existing verb row counts as +1.** Content files and fixture cells count as 0.

**OUT — 5**

| # | object | kind | citation |
|---|---|---|---|
| 1 | `date_due` | question-source roster member | `rosters.yaml:270` |
| 2 | `band_crossed` | question-source roster member | `rosters.yaml:270` |
| 3 | `World.crossings` | a `World` collection | `state/world.py:176` |
| 4 | `epistemic._event_place` | a helper (its behaviour survives as `place_of`; **the NAME goes**) | `epistemic.py:215` |
| 5 | `occasioned_by`'s generic id search | a helper block, `:630-634`, which loses its only reachable caller when the negative guard narrows to one source | `world_q.py:616-634` |

**IN — 2**

| # | object | kind | citation |
|---|---|---|---|
| 1 | `reach` | a Query | new, `queries/world_q.py` |
| 2 | `place_of` | a Query — ⚠ **counted +1, not 0** | new name; `_event_place` deleted at OUT-4 |

**MOVED / CHANGED — 0**

| thing | why 0 |
|---|---|
| CALENDAR's three arguments | a call-site change to an existing gate on an existing row. No new name |
| clause 2 of the Q2 test | a disjunct inside an existing `if`. No new name |
| the roster's `values:` line | data |
| the two migrated probes and three migrated tests | tests, not mechanism |

### **NET FOR THIS SUBJECT: −3 engine objects.**

⚠ **And the honest caveat, because the favourable unit is available and `CLAUDE.md` §0.1 pt 4 forbids
reporting only it.** My plan counted `place_of` as **+0** on the ground that it is `_event_place`
moved, which would make this subject **−4**. **I count it +1 and the plan's count is corrected**, for
a reason a reader can check: the promoted function has **two limbs the private one does not have**
(record, date), a **different signature** (`x: str`, not `e: Event`), and **two more callers**. A
reader must hold a new thing. The `−4` reading is available and is not this file's.

**By the "systems" unit rather than the "names" unit:** **two question sources gone, one `World`
collection gone, one duplicated carrier of one fact gone; one walk family in.** Negative by either
unit, which is the test `05`'s ledger sets.

**Vocabulary** (terms a reader of the engine must hold): **removed 3** — `date_due`, `band_crossed`,
`crossings`. **Added 2** — `reach`, `place_of`. **Shorter by 1.**

**This subject's share of the suite's `−20`:** **−3 of it.** `05`'s ledger is the single owner of the
total and this file claims no other figure.

## §B.3 · Refused and deferred, each with the clause that refuses it

| considered | refused, and by what |
|---|---|
| **a fifth question source `purview`** (round one's Q5) | it grows the roster, the sort, the `occasioned_by` dispatch, `Question.__post_init__`'s message, the aggregation arms and the falsifier set, to express a disjunct. §A.4.2. **And it was the thing round one got wrong here** — `AUDIT_VERDICT.md` survivor 2 records the defect it was answering as real and round one's answer as an addition |
| **carrying `ev.id` onto the Q3 Question** (`H-110`'s one-line fix) | it leaves four sources, an eternal question and two carriers of one fact. §A.9 |
| **a reach CACHE in `queries/cache`** | `ARCH §A.2`: *"barrier indexes … **at a barrier only**"*. A cache has a lifetime; `reach` is recomputed per person per round and nothing has measured a cost. **Deferred, not refused** — the day it is needed, `cache.presence_index`'s shape (`epistemic.py:256`) is the precedent |
| **a `place_of` returning a SET**, per `ARCH §F.14`'s own caveat | it changes `_ch_co_located` from membership to intersection and moves every hash; and `ARCH §F.14` is ratified text, so widening the signature is **RR-B**, not an edit. §A.3.1 |
| **pruning `w.crossings` per season** instead of deleting it | it fixes the eternal question and leaves the duplicate carrier, the malformed referent and the fourth source. It is the smallest change that does the least |
| **giving the crossing Event a `changes[]`** so `document_key` sees it | it would make a duke hear about a crossing at a rung he holds **without being there** — which is the right GAME and the wrong FILE. It changes what `claim_subjects` mints (`H-79`) and what `document_key` admits (`ARCH §C.6`'s mint table). **Deferred with a named owner**, and it is the artifact that would make limb 4 fire (§A.4.6) |
| **a `when` operand so `convene` can schedule for the present** | `requires_operands` is closed at eight (`rosters.yaml:1084`) and coining a ninth is *"filling `H-94` by keyword argument, which is the ruling `H-94` is waiting for and not a table edit"* (`rosters.yaml:1078-1079`). **Refused by the roster's own note** |
| **tightening Q1's addressing clause** instead of deleting Q1 | it repairs the boolean on a source that cannot fire (§0.2b). Deleting Q1 repairs `_derive_operand`'s safety paragraph too (§A.1.1) |

## §B.4 · E, scored LAST and as a ratio — and what would make it FAIL

**The ratio** (§A.11): one N-carrying addition (`reach`'s limbs 1-3 plus clause 2, which is one
mechanism), one narrowed addition (limb 4), one promotion (`place_of`), against five removals.
**E passes.**

**E FAILS here if any of four things is true**, and each is checkable:

1. the question count grows and **the answered count grows with it** — i.e. if `question_aggregation_rule`
   were ever moved off `first` without re-measuring. `AR-1`'s control is written to catch it.
2. `reach` acquires a **fifth limb**. Four is the number of ways a person is connected to a place in
   this model (self, holding, ladder, purview) and a fifth would mean the model grew a relation.
3. `place_of` acquires a **sixth entity limb** without the entity being new.
4. clause 3 ships **before** a claim exists that can satisfy it (§A.5.3).

---

# PART C · THE THREE QUESTIONS

## §C.1 · WHO OWNS THIS? — one owner per value, and the owner is its only writer (`AX-4`)

| the thing | owner | its only writer | who reads it | emitting |
|---|---|---|---|---|
| **what a person may be asked about** | **Nobody.** A Query (`reach`) | — | `questions_for`'s Q2 clauses | — |
| **where a thing is** | **Nobody.** A Query (`place_of`) | — | `_ch_co_located`; `questions_for` clause 2; `04`'s larder walk | — |
| a person's **home rung** | the **person**, as a `contain` Tenure (`carriers.py:41`: *"THE ONE EDGE. Owned by its SUBJECT"*) | `move`'s effect (`effects.py:193`) | `home_of` (`world_q.py:150`) — **the single owner of the question** | `travel.moved` |
| a **site's** rung | the **Site** (`Site.rung`, *"the maintained side (S12)"*) | world-gen; no verb moves a site | `place_of`; MATTER's yield (`matter.py:205`) | — |
| a **record's** place | the **holder**, transitively, via the `hold` Tenure; else `Record.rung` | `_eff_create_record`; `02`'s `give` | `place_of` | `tenure.opened` / `tenure.closed` |
| a **date's** place | the `Date` dict's `venue`, written once by `convene` | `_eff_convene` (`effects.py:187`) | `place_of`; CALENDAR's emission subject | `date.scheduled` |
| a **seat's** rung | the **Office** (`Office.rung`) | `establish`; `03`'s `offices.yaml` at world-gen | `reach` limb 4; `conferral_path`; `under_purview` | `office.established` |
| **which questions a person has** | **Nobody.** A Query (`questions_for`) | — | `deliberate` (`:102`), once per person per round | — |
| **which one they answer** | the **fixture** `question_aggregation_rule` (`H-54`), plus the hash tiebreak | configuration | `aggregate_questions` | — |
| **what a person believes happened** | the **person**, in their own ledger | **WITNESS only** (`witness.py:199-201`, `WriteClass.INTERIOR`) | `questions_for`; `belief_contradicts`; `view_ids` | `claim.deposited` |

**Nothing in this file owns a value.** Two Queries, one call-site change, five deletions.

## §C.2 · WHAT CAN CHECK THIS? — `STRUCTURAL | MECHANICAL | CONVENTION`

`ARCH` PART D's own warning applies: *"A row graded MECHANICAL or CONVENTION is here because the
reader will assume it is structural, and the assumption is the failure mode."*

| claim | grade | the construction that carries it |
|---|---|---|
| **`reach` cannot read a ledger** | ⚠ **CONVENTION today; MECHANICAL with one AST assertion** | nothing stops a function in `world_q` from touching `p.ledger` — `questions_for` in the same module does it legitimately. The existing instrument is the guard family at `world_q.py:17-19` (`test_w5_sense_is_still_the_only_world_taking_non_decision_function`), which parses the model set. **An assertion that `reach`'s body names no `ledger` is one AST walk and it is `AR-10`.** Grading this STRUCTURAL would be the false claim of enforcement this module's own docstring records being caught for twice (`world_q.py:22-28`) |
| **`reach` cannot widen the WITNESS fan** | **STRUCTURAL** | `observers_for` (`epistemic.py:405-441`) takes `(w, e, mode, everyone)` and dispatches `CHANNEL_PREDICATES`; `reach` is not in that dispatch and `epistemic` does not import `world_q`'s new names. A widening would require a new channel, and *"a channel with no function RAISES at import"* (`:392-401`) |
| **`reach` cannot grow the answered-act count** | **STRUCTURAL** | `aggregate_questions` returns **one** `Question` (`decision/questions.py:45`, *"Returns ONE question, because `assemble(person, question)` takes one"*), and the budget is `scene_budget` scenes |
| **a question source outside the roster refuses** | **MECHANICAL at construction** | `Question.__post_init__` raises `Forbidden` (`carriers.py:254-260`), and `occasioned_by`'s guard is defence in depth (`world_q.py:616-628`) |
| **`place_of` cannot silently default** | **STRUCTURAL** | the final `return None`, and every caller tests it. There is no `.get(x, <a rung>)` anywhere in it |
| **`place_of` answers for a multi-rung Event** | ⚠ **IT DOES NOT, and this is a LIMIT rather than a grade** | `ARCH §F.14`'s third column. §A.3.1, falsifier `AR-9` |
| **the crossing Event is the only carrier after the fold** | **MECHANICAL** | `test_season_shape.py:469`'s completeness guard over `World`'s own attributes — *"reads the World's OWN attributes"*, so a re-added `self.crossings` fails it unless someone also edits the `INFRASTRUCTURE` set, which is *"a deliberate act"* by that test's own design. ⚠ **Not STRUCTURAL**: the set is editable, which is exactly why `AR-3` asserts `not hasattr` directly |
| **CALENDAR's emission cannot fabricate a kind** | **STRUCTURAL** | `World._refuse_undeclared_kind` (`world.py:275-294`): a kind no Part D row declares raises `Forbidden("D22")` |
| **CALENDAR's emission cannot be silent** | ⚠ **MECHANICAL only at MATTER, and CALENDAR is not MATTER** | `world.py:387-402`: the must-name-a-kind refusal is gated on `wclass is WriteClass.MATTER`. A CALENDAR-class write with a declared `emits:` and no `emits=` argument **passes the gate silently** — which is how this defect survived, and `occasioned_by:571-577` names it *"a CALENDAR-class silent write of exactly the shape the gate refuses at MATTER."* **Extending the refusal to CALENDAR is one conjunct and is NOT proposed here**: it is a write-discipline change whose subject is the gate, and `CLAUDE.md` §0.1 pt 5's predicate would have to be argued for it. **Named as the standing hazard** |
| **limb 4 reaches anything** | ⚠ **LIMIT, not a grade** | zero, measured, for two independent reasons with two named owners. §A.4.6, §0.2e |
| **clause 3 has a producer** | ⚠ **LIMIT until `02` lands** | §A.5.3, and it is sequenced accordingly |
| the ordering loss | **CONVENTION** | `rosters.yaml:260-261` declares the across-source order; `H-54` owns it; §A.10 measures which pairs were live |

## §C.3 · WHOSE ACT MAKES IT HAPPEN? — every mechanism as execution

**The rule this table exists to satisfy:** *every mechanism must be sayable as execution — what is
written, by whose act, read by whom, emitting what.*

| # | what happens | whose act | step | written | read by | emitted |
|---|---|---|---|---|---|---|
| 1 | a site wears | **nobody's act** — MATTER's licensed clock | MATTER | `Site.condition` | the floor comparison at `matter.py:262` | `condition.worn` |
| 2 | a band edge is crossed | **nobody's act** | MATTER | **nothing** (`changes=[]`) | `observers_for` | **`condition.band_crossed`**, subject = the site, `causes` = the wear Event |
| 3 | people present learn of it | **nobody's act** — WITNESS's fan | WITNESS | each observer's own `ledger` | `questions_for` | `claim.deposited` |
| 4 | one of them is asked | **nobody's act** — DELIBERATE | DELIBERATE | `Act[]`, or nothing | `aggregate_questions` → `assemble` → `choose` | — |
| 5 | he does something about it | **his own act** — `work`, `restore`, `transfer`, `tell` | RESOLVE | that verb's rows | the fold | that verb's `emits` |
| 6 | a sitting is scheduled | the convener's `convene` | RESOLVE | `(Date, due_at)` | CALENDAR | `date.scheduled` |
| 7 | the date comes due | **nobody's act** — CALENDAR reaches it | CALENDAR | `(Date, fired)` | `observers_for` | **`date.fired`, subject = the venue** ⚠ *new* |
| 8 | the venue's occupants and the convener learn | **nobody's act** — WITNESS | WITNESS | their ledgers | `questions_for` | `claim.deposited` |
| 9 | one of them is asked about the occasion | **nobody's act** | DELIBERATE | — | — | — |
| 10 | a writ naming a reeve arrives in his hand | **the carrier's `give`** (`02`) | RESOLVE | `(Tenure, since)` | the deposit rule (`02`) | `tenure.opened` |
| 11 | he comes to believe what it says | **nobody's act** — WITNESS's deposit rule (`02`) | WITNESS | his ledger, `predicate = "content:dispensation"` | **clause 3** | `claim.deposited` |
| 12 | he is asked about it although it is about a rung he does not hold | **nobody's act** | DELIBERATE | — | — | — |

**Rows 1-5 run today except row 4's referent.** Rows 6-9 need `03`'s seats and §A.6's three arguments.
Rows 10-12 are `02`'s and this file supplies only row 12's clause.

**Nothing in rows 2, 3, 7, 8 mentions a duke, a hearth, a policy or a harvest.** Row 2 is arithmetic
against a table; row 3 is a place test; row 7 is a dict scan; row 8 is the same place test. **That is
Jordan's test — "policies impact emergence", with no scripting anywhere in the chain** — and the
reason it holds is that every row is keyed on a RELATION (present-at, holds, above, purview) and never
on an entity or an outcome.

## §C.4 · THE LOOPS, NAMED AND SIGNED (`ID-16`)

> *"A model in which every loop is negative CONVERGES — season 40 resembles season 30 — and
> convergence is not a design goal, it is what happens when a design has no other ideas."*

| # | name | the cycle | sign | damping |
|---|---|---|---|---|
| **AR-L+1** | **ATTENTION FOLLOWS PRESENCE** | I am somewhere → I witness what happens there → those claims are in my reach → I am asked about that place → my acts are about that place → I stay | **+** | `move` is always available · a question is one of ~5 scenes · claim confidence decays at MATTER (`matter.py:147-153`) |
| **AR-L+2** | **THE LADDER LOOKS UP** | limb 3 admits claims about things on the rungs above me → I am asked about my settlement and my duchy → my acts name them → I witness more there | **+** | the ladder is finite and short (hearth → realm is 6 rungs, measured) · the fan is co-located, so claims about a distant rung do not arrive at all · **measured to add 0 questions today** |
| **AR-L+3** | **THE SEAT WIDENS THE SEAT** (limb 4) | I hold a seat → its purview is in my reach → I am asked about its rungs → I act there → `document_key` admits me to more changes there → more claims | **+** | **INERT today** (§A.4.6) · `revoke` ends it in one act · `descendants` is bounded by the tree |
| **AR-L−1** | **THE CLOCK ON A QUESTION** | a claim lands → it is a question for one round → `(c.when, c.round) >= floor` stops admitting it → the question is gone | **−** | **this is the loop the fold ADDS**, and `w.crossings` had no such term: 30 questions from one crossing becomes 2 |
| **AR-L−2** | **THE BUDGET IS FIXED** | more questions in reach → the same one answer per deliberation → every extra question is a question NOT answered | **−** | `scene_budget = 5`, `aggregate_questions(..., "first")`. **The total is fixed**, which is what makes reach a triage problem rather than a throughput one |
| **AR-L−3** | **THE FAN IS THE CEILING** | REACH widens → but the ledger did not → the marginal question is one already-held claim admitted by a second clause | **−** | `observers_for` untouched. This is the loop that makes §0.3's first strike true |

**Three positive, three negative, and the balance is honest rather than flattering:** AR-L+2 and
AR-L+3 are **measured at zero today**, so the live balance is **one positive against three negatives**
— which says the attention layer as it stands **converges on the hearth you are standing in**, and
that the two loops that would carry a governance game are the two that are inert. **That is the
finding, not a footnote.** ⚠ `ID-16`'s derived check is blocked on the `requires` grammar being typed
(`hole_register.yaml:1444`), so this table is an **authored claim, not a falsifiable one**, and says
so — except AR-L−1 and AR-L−2, which `AR-1` and `AR-2` do test.

## §C.5 · THE GRADE, AND WHAT WOULD MOVE IT

**`paper`.** `CLAUDE.md` §0.2: *done means it runs.* **Nothing in PART A has executed.** The
measurements in §0.2 executed — they measure the tree **as it is**, which is what makes them evidence
against the design rather than for it.

**What would move it, in order, each cheap and each an execution artifact:**

1. **The two deletions plus clause 2** (`05` item 2, size M). The artifact is a re-run of §0.2d's
   measurement script showing `561 → 1632` in the ENGINE rather than in a shadow implementation, plus
   `question_sources` at length 2, plus a **declared** golden re-record. **This is the cheapest thing
   in this file and it changes behaviour on day one.**
2. **CALENDAR's three arguments** (`05` item 2, same commit, size S). The artifact is a `date.fired`
   Event in a log — and it needs a world with a date, which means it is verified on
   `probes.py:1349`'s hand-built date until `03` ships a seat that can `convene`.
3. **`03`'s `offices.yaml`** — because limb 4 is inert without it (§A.4.6, reason 1). The artifact is
   `|reach|` for a Count rising from 11 to the size of his territory's subtree.

⚠ **AND THE CHEAPEST ARTIFACT IN THE WHOLE SUITE IS NOT IN THIS FILE.** `AUDIT_VERDICT.md`'s own
verdict: *"The whole difference is one artifact — `@effect_for("commit")`."* `05`'s item 1. It is
named here so that nobody reads this file's item as the suite's first step. **`commit`'s body is
first; this file's item is second.**

**The terminal artifact remains `python -m engine.season.harness.register --requirements` moving
`R-04` off `not_met`.** Only a run may change that.

## §C.6 · RULING REQUESTS — NONE FROM THIS FILE, and the four forks it closed

**Every fork this subject raised was closed by `CLAUDE.md` §0's five-step gate.** The step is named,
per the instruction that `needs_jordan` is not a parking space.

| the fork | closed at | how |
|---|---|---|
| **fold the four sources, or fix Q3's referent?** | **step 3 — answered by a design document.** `holonic §37.2` (`:1295-1299`) states the model as *need + claim*. And `H-110`'s own row refuses the one-line fix as a repair | §A.2, §A.9 |
| **a fifth source, or a term of REACH?** | **step 4 — answered by precedent.** `ID-13` and `ARCH §B.13`'s cross-validation family are the tree's standing answer to a declared row with no live consumer; adding a fifth row to express a disjunct inverts it | §A.4.2 |
| **does the fold's lost ordering need a ruling?** | **step 1 — superseded, and step 4.** `H-54` (`hole_register.yaml:618`) already owns *"which question a budget-bounded person answers"*, is closed at step 4 with `needs_jordan: false`, and its own text refuses to re-decide the sort | §A.10 |
| **does `place_of` return a set, per `ARCH §F.14`?** | **NOT closed here — it belongs to RR-B** (`05`), because `ARCH` is RATIFIED (ED-IN-0204) and step 5 may not overwrite ratified canon. **This file does not widen the signature and states the limit** | §A.3.1, `AR-9` |

**And two rows this file closes by design, for `05` to carry:**

- **`H-110` — DISSOLVED** (§A.9). Not wired; its subject ceases to exist.
- **`occasioned_by`'s two dead routes** — closed by the sources' deletion, and the function's own
  count (*"ONE of four routes is live"*, `world_q.py:594`) becomes *one of one*.

**Not closed, and said so:** `ARCH §F.14`'s set-valued place (RR-B); `_ch_post_remit`'s inertness
(§A.4.6, no owner in this suite); the CALENDAR-class silent-write hazard (§C.2, named not proposed);
`H-54`'s undeclared hash tiebreak (declared and left alone, `needs_jordan: false`); the
`band_floors.body` / `Site(kind='body')` contradiction (`04`'s).

---

# PART D · FALSIFIERS (`ID-11` — ship the falsifier with the claim)

**Every row carries the test's name in the tree's idiom, what it would OBSERVE, and its CONTROL.**
`CLAUDE.md` §0.1 pt 2: *an assertion must be able to observe the failure it excludes.* Round one
shipped a falsifier family that could not, and `AUDIT_VERDICT.md`'s last axis row records it — *"a
family that asserts on a carrier that does not exist: one cannot observe, one is a universal absence,
one is falsified today."* **Each row below was checked against that and two were rewritten.**

| # | the claim | what would show it wrong | the CONTROL |
|---|---|---|---|
| **AR-1** | REACH widens the question set and **not** the answered-act count | `test_ar1_reach_widens_questions_and_not_acts`: same seed, `build_realm(0)`, one season, two arms (today's Q2 test vs clauses 1-2). **Questions must rise (561 → 1632) AND `len(driver.resolved)` must be equal.** If acts move, the budget is not the bound and §B.4's E-argument fails | ⚠ **the control is the ACT count, and it is the half that can fail.** A question-count-only assertion is unfalsifiable — widening a disjunction always widens a filtered set. **Second control:** run the same two arms with `question_aggregation_rule="all"` and assert the act counts are **still** equal, because `aggregate_questions` returns one question under every arm |
| **AR-2** | a band crossing raises a WELL-FORMED question, with a clock | `test_ar2_a_crossing_asks_about_the_site_and_stops_asking`: `_w4_run`-shaped world, site at 805, 3 seasons. Assert (a) a question whose `about` is the **crossing Event's id** and whose referent is the **site id**; (b) `occasioned_by` returns that Event; (c) **exactly one question per present person, not 30** | **the control is arm B at condition 990**: zero crossings, zero such questions. Without it, (a) passes in a world where the site never crosses and the assertion loops zero times. ⚠ **And a count assertion is required**: `assert n_crossing_questions == len(present)`, because *"a loop that asserts conditionally must assert that it asserted"* |
| **AR-3** | `w.crossings` is gone and the Event is the only carrier | `test_ar3_the_crossing_has_one_carrier`: `assert not hasattr(w, "crossings")` **directly**, plus the existing completeness guard | ⚠ **`test_season_shape.py:469` alone CANNOT observe this failure** — dropping `"crossings"` from `INFRASTRUCTURE` and deleting the attribute both make it green. The `hasattr` assertion is the control, and it is why this row exists separately |
| **AR-4** | limb 4 (purview) reaches its seat's subtree and nothing else | `test_ar4_a_seat_reaches_its_subtree`: for a seat with a `rung`, `reach(w, holder) ⊇ {rung} ∪ descendants(rung)` and **excludes** a sibling subtree. ⚠ **AND IT MUST ASSERT THE ZERO IT MEASURES**: `assert purview_questions == 0` on today's world, **with a comment naming `03`'s `offices.yaml` as what flips it** | **the control is the 16 rung-less seats**: limb 4 must contribute the empty set and must not raise. Without that arm, a green test says nothing about 16 of 19 seats. **The flip-detector is the point** — the day `03` lands, this test goes red and is rewritten to assert the new number |
| **AR-5** | clause 3 (`named(c)`) admits a person a writ names, and only then | `test_ar5_a_writ_names_you_into_a_question`: a `content:dispensation` claim whose `value` names p, where p holds nothing and is nowhere near the rung. Assert p is asked | ⚠ **THIS TEST MUST BE RED BEFORE `02` AND GREEN AFTER, and shipping it green before `02` would mean it is testing a hand-planted claim shape the writer does not produce** — the `date_due` arm's live defect (§A.8.1). **The control is a person the writ does NOT name, same world: not asked.** Sequenced into `05` item 7 |
| **AR-6** | `place_of` breaks at no extreme | `test_ar6_place_of_at_the_extremes`: a Proposition subject (`None`, excluded); a person contained nowhere (`None`); a record with no holder (falls to `Record.rung`); **a record with two live holds (`hold_force` RAISES `Forbidden`, and the test asserts the raise)**; a date with no venue (`None`) | **the control is that the clause is not VACUOUS**: with every rung removed from `R`, clause 2 admits **zero** claims. Without it, "None is excluded" is indistinguishable from "the clause never fires" |
| **AR-7** | the site-use verb survives the fold, on the Event | `test_ar7_two_floors_in_one_season_are_two_events`: a site crossing **two** floors in one wear step. Assert two Events with distinct ids (`H(..., f"crossing:{verb}")`, `matter.py:268`) and two distinct questions | **the control is a one-floor crossing**: exactly one Event, one question. Without it, "two Events" could be a duplicate rather than two floors |
| **AR-8** | CALENDAR emits, with a subject and a root cause | `test_ar8_a_date_fires_into_somebodys_ledger`: a date with a venue where a person stands. Assert a `date.fired` Event with `subject == venue` and `causes == [ROOT]`, the claim in that person's ledger, and the question | **the control is a VENUELESS date**: the Event's subject falls back to the date id, `place_of` is `None`, and **nobody is asked**. That control is what shows the venue is doing the addressing rather than the fan |
| **AR-9** | `place_of` answers honestly for a multi-rung Event — **AND IT DOES NOT** | `test_ar9_a_multi_rung_event_reaches_one_place`: an actorless Event spanning two rungs (`matter.py:37-40`'s own case). Assert `place_of(e.subject)` names **one** rung and that persons at the other are **not** asked. ⚠ **THIS FALSIFIER IS EXPECTED TO FIRE AND IS SHIPPED ANYWAY**, per `CLAUDE.md` §0.1 pt 3, which asks for the test's OUTCOME and not a clean sheet: it pins `ARCH §F.14`'s stated limit so that the day RR-B widens the signature, the test says so | **the control is a single-rung Event**: everyone present is asked. Without it, "one rung" could be "no rungs" |
| **AR-10** | `reach` reads no ledger | `test_ar10_reach_names_no_ledger`: an AST walk over `reach`'s body asserting no attribute named `ledger` and no call to `view_ids`/`belief_contradicts`, on `world_q.py:17-19`'s existing guard pattern | **the control is a MUTATION**: insert `p.ledger` into a copy of the function's AST and assert the check fails. A structural check that has never been shown to fail is `world_q.py:22-28`'s own recorded defect — *"a claim of enforcement naming a gate that does not read the file it is written in"* |
| **AR-11** | the two deleted sources were dead, not merely quiet | `test_ar11_the_deleted_sources_had_no_producer`: the §0.2b and §0.2c scripts, promoted to tests against the **pre-fold** tree, asserting `date_due == 0` on the corpus's own planted date and **50 on the unmintable control** | ⚠ **THE UNMINTABLE ARM IS THE WHOLE TEST.** Without it, `date_due == 0` is consistent with a broken spy, a broken reader and a broken world. This row exists because an absence is *"the cheapest claim to make and the hardest to see wrong"* |

⚠ **Two falsifiers are expected to fire and are shipped anyway**, because a suite with no expected
failures was written after the fact: **AR-9** pins `ARCH §F.14`'s limit and **AR-5** must be red until
`02` lands. And **AR-4** is written to go red on `03`'s success, which is a third kind: a test whose
failure is progress and which therefore must carry, in its own message, the thing that flipped it.

---

# APPENDIX · CITATION REPAIRS

`CLAUDE.md` §0.1 pt 3: *"A citation you have not opened is not a citation."* Every `path:line` above
was opened in this session. These are the citations I inherited from the plan and the round-one
corpus that were **wrong**, corrected silently in the text and recorded here so the error is not
re-imported. Round one accumulated ~50 such repairs across two passes and one of its documents had 16
of 30 wrong; this is the discipline that produced that number, applied forwards.

| cited as | actually | consequence if uncorrected |
|---|---|---|
| *"CALENDAR passes `emits="date.fired"` at `calendar.py:37` — **a one-argument change** at a declared row"* | **a THREE-argument change.** `World.write` **raises** `Forbidden("S33")` on an emission with no `subject=` (`world.py:417-431`) and `Event.__post_init__` **raises** `Forbidden("S19.4")` on an empty `causes[]` (`carriers.py:118-125`), which `world.py:452-457` refuses to default | a session sizes the change at one line, writes it, and gets a hard refusal from the gate — or worse, ships `subject=thing`, which is the exact defect `world.py:412-416` records having made every site's wear emit under the subject `"condition"` |
| *"the parties named on the date (`_eff_convene`) are its `witness_key`"* | **a Date carries NO party list.** `_eff_convene` builds `{"id", "venue"}` plus `due_at` and `convening_attached` (`effects.py:187-189`). The only address it has is `venue` | the fold is designed around a field that does not exist; the whole addressing story for Q1 collapses. **Corrected to: the venue is the subject, and `co_located` over `presence(venue)` is the channel** |
| *"the `date_due` and `band_crossed` routes are dead (opened: **the branches return `[]`**)"* | **they are not branches.** `world_q.py:616` is a NEGATIVE membership guard that lets exactly those two **fall through** to the generic id search at `:630-634` | the migration is mis-sized: a session looks for two `if` blocks, finds none, and either leaves the guard naming deleted sources or misses that the id search loses its last caller (a deletion this file counts) |
| *"`world_q.py:518` binds the use-verb **while the site id is in the tuple and discarded**"* (round one, and my plan) | **true, and the discarded element is `ev.id` at index 4, not the site id at index 0.** The site id IS read — it is `who`, the presence test's key (`:514-517`). What is discarded is `*_rest` | the one-line fix is aimed at the wrong element; and the argument for dissolution rests on the EVENT being discarded, which is stronger |
| *"`descendants(w, rung)` gives the purview set"* | **`descendants` EXCLUDES the rung itself** (`world_q.py:58`: `out, seen, stack = [], {rung_id}, [rung_id]`). `under_purview` **includes** it (`predicates.py:136-138` returns `True` when `holding == seat`) | limb 4 would silently exclude a seat's own rung, so a Duke would not be asked about his own duchy — the purview defect re-introduced by an off-by-one-set. **Corrected to `{rung} ∪ descendants(rung)`** |
| *"`band_floors.body` is the SITE kind `body` … **not** a person's body; the proposal must not conflate them"* | **the roster says the opposite of the first half and the corpus says the opposite of the second.** `rosters.yaml:814-815`: *"`body` IS NOT A SITE. **It is `(Person, body)`'s band row**, here because `band_floors` keys on THIS roster."* And `headless.build_world(0)` builds `Site('scriptorium', kind='body')`, whose `full_operations: 800` floor is the one my §0.2c measurement crossed | my crossing measurement would be reported as a harbour's. And `04` would design `band_floors.person` beside a row that was already put there for persons. **Flagged to `04`, which owns it** |
| *"`references/id_reservations.yaml:246` — `IN: { next_free: 233 }`"* | **`next_free: 236`.** The bump has already landed on the working tree: *"ED-IN-0231..0235 allocated 2026-09-17 … next_free 231->236"* (`:246`), and `SE` reads `next_free: 54` (`:257`) | a session re-allocates 233 and collides with this document. **The plan's §9 measurement was taken pre-bump; ED-IN-0233 is mine and is already reserved.** This file touches no ledger |
| *"81 questions, all `need`"* — plan §2.1, unsourced | **verified: 81, all `need`, on `build_realm(0)` at tick 0**, and it stays exactly 81 after one and two seasons while `claim_landed` goes 0 → 561 → 972 | nothing — this one was right, and it is recorded because §0 pt 8 asks for the command with the number and the plan carried neither |
| *"MATTER emits `condition.band_crossed` AND appends to `w.crossings` — **two carriers of one fact**"* | **verified** at `matter.py:267-272`. ⚠ And the sharper form the plan did not have: the Event's `changes[]` is **empty**, asserted at `test_season_shape.py:1131`, which is what makes `document_key` blind to a crossing and limb 4 inert | the whole of §0.2e's second reason, and therefore §A.4.6 and the narrowed N-line, would have been missed |
| `ARCH §F.14` | **not in the plan at all**, and it names `place_of` by name, gives its rule and states its risk | `place_of` would have been presented as an EXTENSION when it is CONFORMANCE, and its one real limit (a set-valued signature) would have gone unstated |
| `holonic §37.2` (`:1295-1299`) | **not in the plan's §2.1**, and it states the two-source model in one sentence | the fold would have been argued from object-count alone rather than from a ratified sentence, and the gate's step 3 would have read "no design document decides it" — which is false |

**And three claims I inherited that were not citation errors but were wrong on the merits**, all
struck in place above rather than deleted:

1. **~~"REACH filters landed claims and never widens the fan."~~** It never widens the FAN; it widens
   the QUESTION SET 2.9×. §0.3. Verified the wrong half of itself — by reading `observers_for` (which
   is untouched, and true) instead of counting the questions (which is the claim).
2. **~~"Cut `reach` and the purview defect returns."~~** Measured: cutting the purview limb changes
   nothing, for two independent reasons. §0.2e. **NARROWED, not passing** (`CLAUDE.md` §0.06).
   Verified the wrong half of itself — by reading the 16-of-19 `rung: None` measurement (real, and
   round one's survivor 2) instead of running the limb against a ledger.
3. **~~"the three-clause Q2 test ships in item 2."~~** Clause 3 has no producer in this tree (§0.2f:
   every claim's predicate is `e.kind` and its value is `True`), so shipping it with item 2 would ship
   a dead clause in the same commit that deletes two dead sources. **Sequenced into item 7.** Verified
   the wrong half of itself — by reading `02`'s deposit rule (which will produce it) instead of the
   deposit that exists (`witness.py:191`).

**All three were found by RUNNING the thing that would show presence**, which is `CLAUDE.md` §0.1
pt 3's instruction and the reason the measurement block in §0.2 exists at all. The scripts live in
this session's scratchpad and each is named at the row that cites it; they are measurements of the
tree as it stands, not artifacts of this design, and **nothing in this file has run.**
