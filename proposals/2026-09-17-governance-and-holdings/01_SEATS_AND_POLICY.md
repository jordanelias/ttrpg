# 01 · SEATS AND POLICY — governance and management at every rung, hearth to realm

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` · id: **ED-IN-0231**. Grade under `CLAUDE.md` §0.2: **`paper`** — nothing in this file
## executes, PART C.5 says what would move it, and no row here may be cited as done.
## Method: authored at tier **`opus`** (`CLAUDE.md` §10 — *competing-considerations judgment,
## multi-doc synthesis*), against the working tree at 2026-09-17. Reconciliation of the disagreements
## this file settles was a read-only `fable` stage; the per-rung and engine-fit analyses were `opus`.
## Citation discipline: `architecture/meta/04_CODE_ARCHITECTURE.md` is cited **`04 §Letter.Number`**
## and never `04:NNN` — its line numbers have drifted twice. Every `path:line` below was opened at
## that line in this session; the appendix lists the citations I found wrong in my own sources and
## repaired.

---

> **Jordan, on what a policy is:** ***"Policies aren't just a number added to a roll, but a way to
> change or impact how a governed rung functions."***
>
> **Jordan, the keystone:** ***"They impact emergence."*** And: *"a change to how a rung functions
> will likely have impacts on rungs below it. A provincial policy on farming taxation may end up
> impacting a hearth, you know?"*
>
> **Jordan, on the player:** *"a player whose character can govern a settlement would like to be able
> to explicitly set policies or advance a project to build something."*
>
> **And the architecture clause this file exists to apply**, `04 §B.7`, whose grade is MECHANICAL:
> *"**purview is asked of the seat exercised, not the actor** — `Act.via : SeatId?`; every purview
> walk uses `via.scope`. **A regent has the seat's purview**."*

---

# PART 0 · THE CONFORMANCE DIVISION, AND IT IS THE SPINE OF THIS FILE

**Most of the seat model below is already ratified Layer 1 and merely unbuilt.** It is not this file's
invention and this file claims no novelty for it. `04 §B.7` ships the `Seat`; `04 §A.3` rows 5, 7, 8,
11, 12, 13, 14, 15 ship eight of the deletions; `04 §B.8` retires `Tenure.payload` in favour of
`term?`; `04 §B.9` gives `Act` its `via`; `01 §E.2.5` rules the council. **A proposal that restates
ratified architecture as a proposal is worse than useless — it invites a session to re-decide a
settled thing.** So every section below carries one of three words, and the three lists are here, in
front, so a reader can skip the first list entirely.

## §0.1 · The three lists

**CONFORMANCE — RATIFIED Layer 1, UNBUILT in the engine. Nothing here is proposed; it is owed.**

| item | the ratified clause | the engine as measured |
|---|---|---|
| one `Seat` type, no `Title` type | `04 §B.7` call 1 | `Office` (`engine/season/state/carriers.py:481-549`) plus a title/body `Forbidden` at `:537-544` |
| **no `is_title` branch anywhere** (ID-4) | `04 §B.7` call 1; `01:443` | the branch runs: `engine/season/loop/predicates.py:252` |
| **`establishment` is a Query over `oblige`, not a field** | `04 §B.7` call 2; `01 §E.2.5`'s own correction | a field (`carriers.py:491`), read at `engine/season/queries/world_q.py:413`; empty on all 19 offices |
| **`judging_set_rule` deleted from `Rung`** | `04 §B.7` call 3; `04 §A.3` row 7 | still in the whitelist: `carriers.py:568-569` |
| **purview is asked of the seat exercised, not the actor** | `04 §B.7`, grade MECHANICAL | asked of the actor's *post string*: `predicates.py:144-155` |
| `Tenure.term?` replaces `payload?` | `04 §B.8` | `payload` still declared (`carriers.py:59`) with a live matrix row |
| `Act.via : SeatId?` | `04 §B.9`; `04 §C.2` F3 | absent from the `Act` the engine folds |
| the write gate admits **four** Tenure-write bases and a conferral opener matches none | `04 §C.2` F3, verbatim | `confer` and `revoke` both write `Tenure.until` on somebody else's edge |
| `hold.subject : Person` only | `04 §A.3` row 12; `04` PART D row 14 | 16 of 35 live `hold` Tenures have a **faction** subject (measured, §0.2) |
| `budget` never includes an `office_bonus` | `04 §A.3` row 15 | `engine/season/decision/budget.py:56-57` pays one per live `hold` |
| `Petition` and `Dispensation` are **kinds of `Record`** | `04 §A.3` row 11 | both are write-matrix kinds with **no carrier** (`carriers.py` has no such class) |
| succession is the holder's disposition, not the place's | `04 §A.3` row 8; `01:1233-1238` | `succeed`'s subject is still a `Rung` (`architecture/holonic_ARCHITECTURE.md:542`) |
| a council is **one seat, many holders via `oblige`** | `01 §E.2.5` | `Office.binds` has **one occurrence in the whole package** — its own declaration (`carriers.py:488`) |
| `Act` persists resolver-side | `04 §A.3` row 13 | no act store |
| the explanation contract: the engine owes the arithmetic of what the character already holds | `04 §C.11` | — |

**EXTENSION — consistent with ratified Layer 1, unratified, and this file's actual proposal.**

| item | what it rests on |
|---|---|
| **the policy instrument**: a `dispensation` `Record`, held by its issuer, whose reach is the issuing seat's (§A.7) | `04 §A.3` row 11; `04 §B.4/B.5`; `holonic_ARCHITECTURE.md:538`; `engine/season/loop/effects.py:262-289` |
| **`in_force(w, rung, clause)`** — the nearest-ancestor walk up `contain`, plus a `reach` operand (§A.8) | `world_q.py:48` `parent_of`; the same ascent `predicates.py:105-140` and `world_q.py:416-437` already walk |
| **the seven clauses**, three as step readers and four as `requires` conjuncts (§A.9) | `rosters.yaml:1086-1122` (seven forms, closed); `engine/season/data/requires.py:542` (`all`) |
| **the conferral claim** — `remit:` evaluated person-side from the holder's own ledger (§A.6) | `options.py:107-169`; `engine/season/loop/witness.py:175`; `01:100-103` (AX-2) |
| **a `record_kinds` roster**, so `Record.kind` is declared rather than matched (§A.7.4) | `01:443` (ID-4); `effects.py:285`'s `d.get("kind") or "text"` |
| **the delivered/demanded gap as a band on a Query**, changing options and never outcomes (§A.13) | `01:631-645` (ID-17 → `T-b`); `01:1332-1340` (breach *is* the sworn/performed gap) |
| **Q5 `purview`** — a fifth question source, claim-gated (§A.15) | `rosters.yaml:250-270` (`question_sources`, open, ordered); `predicates.py:105-140` |
| **a matter condition on the shipped stage maturation**, and `stage.stalled` on its else branch (§A.12) | `engine/season/loop/matter.py:64-109` |
| **`sworn(policy) = members(w, terms)`** — not a new Query, the shipped one (§A.7.3) | `world_q.py:200-211` |

**DEPARTURE — needs a ruling. There is exactly one, and it is PART C.6's RR-1.**

| item | why it cannot be answered by the five gates |
|---|---|
| **policy collision: does the NEARER policy or the HIGHER rank win?** | nothing in the tree decides which policy a step reads, because no step reads one. Two defensible options, materially different games. PART C.6 |

**And one ruling already queued elsewhere:** `ED-SE-0051` (`references/id_reservations.yaml:257` —
*"the bound on the demographic loop — matter only, or matter plus hearth capacity; needs_jordan"*)
belongs to **`02_THE_BUILT_WORLD.md`**, not here. It is named so a reader does not look for it in this
file and conclude it was dropped.

## §0.2 · What I measured, today, rather than quoted

Run 2026-09-17 against this working tree: `build_realm(0)` from `engine/season/harness/populated.py`,
`resolvable_verbs()` from `engine/season/loop/driver.py:72`, and
`predicates.under_purview` over every live seat-hold.

```
rungs 375   persons 46   offices 19   propositions 54 (OUGHT 52, HOLDS 2; 6 carry `scope`)
tenures     contain 373  commit 86  hold 35        records 0        dates 0   docket 0
hold subjects   person 19 · NON-PERSON 16          hold objects  office 19 · rung 16
offices: conferral None ×19 · revocation None ×19 · upkeep None ×19 · establishment [] ×19
         binds "members_by_admission" ×19 (the dataclass default, and its only occurrence)
posts on the `titles` ladder: 3 of 19  (King · Duke · Duchess)
seat-holders with purview over their OWN seat's rung: 3 of 19
resolvable_verbs(): 18 of 38.  NOT resolvable: issue · determine · establish · levy · open_case ·
         petition · comply · commit · oblige · carry · refract · forge · succeed · restore · repudiate
binding_decision rows: 9.  SEVEN are `remit:`-only; TWO — `release`, `succeed` — are `own`.
```

**Five of those numbers are load-bearing on what follows and none of them is in any source document
in the form given here.**

1. **Every one of the nineteen seats has an empty `conferral` and an empty `revocation` basis.**
   `_req_confer` refuses an office with no conferral basis (`predicates.py:180-181`) and `_req_revoke`
   refuses one with no revocation basis (`predicates.py:234-235`). **So no seat in the built world can
   be conferred or revoked, and the reason is not `remit:` — it is two empty strings.** Any plan that
   fixes the eligibility model and not the content fixes nothing.
2. **Sixteen of nineteen seat-holders have purview over nothing, including their own seat's rung**,
   because `titles_held` filters on `title_domain(post) is not None` (`predicates.py:151-152`) and
   sixteen posts — *Chief Parliamentary Clerk*, *Cardinal Justice*, *Royal Marshal*, *Skald-Chief* and
   the rest — are not on the eleven-name `titles.domains` roster (`rosters.yaml:755-766`). This is
   `04 §B.7`'s MECHANICAL invariant measured in the negative: purview is read off a **post string**,
   so every non-title seat governs nothing.
3. **`records 0`.** There is not one `Record` in the built world. Everything below that rides on a
   Record rides on a carrier with no instance, which is why §A.7's instrument is `paper` and not
   `partial`.
4. **`issue`, `commit`, `petition`, `determine` and `repudiate` are all unresolvable** — and the cause
   differs per verb, which matters for sequencing: `issue`'s `requires` cell is not a predicate at all
   (`hole_register.yaml:763`: *"`issue`, `open_case` … are §F.24a's own finding that their cells are
   NOT PREDICATES AT ALL but constraints on the well-formedness of the Act"*), whereas `commit` and
   `repudiate` carry **typed** cells and lack only an `@effect_for` body (`effects.py` registers
   eleven: confer · release · revoke · convene · move · work · create_record · destroy_record ·
   kill/wound · utter · transfer).
5. **`dates 0` and `docket 0`.** `(Date, due_at)` is written only by `convene`
   (`engine/season/write_matrix.yaml:93-100`), `convene` is `remit:convene`, and `remit:` declines
   person-side (`options.py:163-165`). One blocked disjunct; the entire venue layer downstream.

## §0.3 · TWO CLAIMS THIS FILE DOES NOT MAKE, both struck in place

**⛔ STRUCK.** ~~*No person can form a governance verb at all.*~~ It is false as stated, and it was
stated that way in my own sources (`hole_register.yaml:1102` phrases the consequence that way, of a
different row). **Measured:** nine rows are `stratum: binding_decision` and **two of them —
`release` and `succeed` — are `own`-eligible**, so a person forms them today and `person_side_eligible`
returns `True` on the first `own` alternative (`options.py:143-144`). The true statement, and it is
narrower and sharper: **seven of the nine `binding_decision` rows are `remit:`-only, and `remit:` is
declined person-side (`options.py:163-165`), so those seven are unformable.** That is `H-71`
(`hole_register.yaml:795`), and §A.6 closes it.

**⛔ STRUCK.** ~~*A seat decays because its `upkeep` goes unpaid, its establishment releases itself,
and its reach falls.*~~ `Office.upkeep` has **no reader and no writer anywhere in
`engine/season/**/*.py`** — its sole occurrence is the declaration at `carriers.py:493` (the other
four hits are prose in a probe, an invariant and a test). `Office.establishment` is read at exactly
one site (`world_q.py:413`) and is **empty on all nineteen offices**, and `04 §B.7` call 2 *rejects the
field* in favour of a Query over `oblige`. A decay channel on either is a mechanism riding two dead
fields, one of which the architecture deleted. **The replacement is §A.13: a band on a
delivered-versus-demanded Query, which changes which options a subject sees and never an outcome.**

---

# PART A · THE CLAIMS, EACH WITH ITS VERDICT

Every subsection is a candidate/owner/verdict table closed by a `> ### RULED:` line citing the clause
that decides it. A verdict of **CONFORMANCE** means *this was decided; build it*. **EXTENSION** means
*this is the proposal*. **DEPARTURE** means *do not build it until Jordan rules*.

## §A.1 · THE SEAT — one type, and Layer 1 already shipped it

`04 §B.7`, verbatim:

```
Seat := ( id, post, body?, scope? (null = a cluster), remit(acts[], binds)
        , conferral  -- which ACT fills it: confer by <seat> | determine by <judging seats> | succeed
        , revocation -- which seat may revoke, and the CONJUNCTS
        , upkeep, dates[], exists )
NEVER:   who holds it · who serves it · a modifier of any kind
```

| candidate | who owns it? | verdict |
|---|---|---|
| a `Seat` type distinct from a `Title` type | `04 §B.7` call 1 | **CONFORMANCE.** *"There is no `Title` type"*; a title and an ordinary office are two **values** of `revocation.conjuncts`. The engine's `Office` is the Seat and the title/body `Forbidden` at `carriers.py:537-544` is the symptom |
| `domain : RungId[]` — a SET of rungs, so one Lord holds several territories in one seat | proposed by the per-rung analysis | **REFUSED.** `04 §B.7`'s `scope?` is singular. Purview is the `contain` closure of `scope` plus the holder's own `hold` Tenures, and `predicates.py:105-140` already walks a **disjunction over every seat the actor holds** — *"authority over a holding is authority from ANY title the actor holds"* (`:127-129`). A Lord with three territories holds three seats and the disjunction covers him. A set-valued field also breaks rank: `max(ordinal(kind(d)))` over a Count's territories computes **territory**, which inverts Jordan's *"rank is not headcount"* (`rosters.yaml:706-709`) |
| `remit : (act, scope?)[]` — a scope per act | proposed by the per-rung analysis | **REFUSED in v1.** `04 §B.7` pairs `acts[]` with one `binds`, and no seat in the draft roster needs *this act here and that act there*. A Duke who may `issue` across the duchy and `confer` in one province **establishes a sub-seat** for the second, which is `04 §B.7`'s own delegation row (`establish` → `confer` → `revoke`). CONVENTION-grade question, PART C.2 |
| `binds : TenureKind` — the relation over which the bound set is computed | `04 §B.7`'s `remit(acts[], binds)` | **CONFORMANCE, and the reader is missing.** MEASURED: `binds` occurs once in the whole package, its own declaration (`carriers.py:488`), on the dataclass default `"members_by_admission"` for all nineteen offices. `ID-13` (`01:489`) makes that *"not a weak field but one that does not exist, wearing a schema's clothes"* |
| `establishment` as a stored list | `04 §B.7` call 2 | **CONFORMANCE: delete the field.** *"A set of persons on a seat is two homes for one fact. A person joins by `oblige : Person → Seat` and leaves by `release`."* And `04 §B.7` names the cost of keeping it: *"establishment size as a number nobody can source"* |
| `judging_set_rule` on `Rung` | `04 §A.3` row 7 | **CONFORMANCE: delete.** *"decision-shaped state on a container."* `world_q.judging_set` already raises `Unspecified` rather than reading it (`world_q.py:146-148`) |
| `upkeep` | `04 §B.7`'s field list | **CONFORMANCE (it is declared), NO MECHANISM (it has no reader).** §0.3 |

> ### **RULED: the seat model is `04 §B.7`, entire, and this file adds nothing to it.**
> Cited to `04 §B.7` (three calls, four invariants) and `04 §A.3` rows 5, 7, 12, 14, 15. The two
> shape changes the analysis stage proposed — a set-valued domain and a per-act remit scope — are
> **refused here**, each on a clause of `04 §B.7` rather than on cost. The work owed is a **reader
> for `binds`**, a **Query for `establishment`**, and the deletion of four helpers (§B.2).

⚠ **A struck claim, kept in place.** ~~*A prince-bishopric cannot be spelled, so the title/body
refusal must be deleted for canon's sake.*~~ The refusal at `carriers.py:537-544` is a **content**
problem, not a shape one: under `04 §B.7` a person may hold a title seat **and** a body seat, because
`hold` is 1-per-object and not 1-per-person (`holonic_ARCHITECTURE.md:538`; enforced at
`world_q.py:138-144`), and `under_purview` is *"a DISJUNCTION over the seats"* (`predicates.py:127-129`).
Exclusivity, where a setting wants it, is refused at `confer` by a `cardinality` or `relation` conjunct
once `Act.via` lands — not by a constructor that refuses a true thing to prevent a false one.

## §A.2 · PURVIEW IS ASKED OF THE SEAT EXERCISED — and here is what not doing it costs

| candidate | who owns it? | verdict |
|---|---|---|
| purview read off the **actor's post string** (today) | `predicates.py:144-155` `titles_held`, filtering `title_domain(o.post) is not None` | **CONFORMANCE defect.** MEASURED today: 3 of 19 posts are on the ladder, so **16 of 19 seat-holders have purview over nothing, including their own seat's rung** |
| purview read off `Act.via.scope` | `04 §B.7`, grade **MECHANICAL**; `04 §B.9`'s `Act := (id, actor, via : SeatId?, …)` | **CONFORMANCE.** *"A regent has the seat's purview"* — which is the whole of `01 §E.2.1`'s requirement, *"THE TITLE AND THE GOVERNING MUST BE SEPARABLE"* (`01:1367`) |
| a `via.scope` sub-field distinct from `Seat.scope` | nothing | **REFUSED.** Nothing licenses a second scope. `via` names the seat; the seat carries the scope |

> ### **RULED: `04 §B.7`, MECHANICAL — purview is asked of the seat exercised, and `Act.via` is how the
> seat enters the act.** The three consequences are not separate items: the `is_title` branch
> (`predicates.py:252`) goes, because the two rules become two values of `revocation`
> (`rosters.yaml:718-724` carries Jordan's own two rules verbatim); `titles_held`,
> `highest_title_rank` and `title_domain` go with it (`predicates.py:144-164`); and the write gate
> gains the clause `04 §C.2` F3 says it needs, since **a conferral-basis opener matches none of the
> four admitted bases** and *"so does `confer`, today"*.

## §A.3 · CONFERRAL AND REVOCATION ARE DECLARED BASES, NOT CODE PATHS

`01:1495-1498` is the corpus's sharpest sentence on this and it is quoted rather than paraphrased:

> *"§D.6 gives an Office a **`conferral`** field — 'the basis, **per office**' — which is exactly the
> slot that distinguishes *the Duke names him* from *the burghers elect him* from *it passes to the
> eldest*. **Delegation does not need a delegation mechanism. It needs the `conferral` basis to be
> specified**, and that field has been on the Office since #353 carrying nothing."*

| candidate | who owns it? | verdict |
|---|---|---|
| `conferral ∈ {confer by <seat>, determine by <judging seats>, succeed}` | `04 §B.7`'s own list | **CONFORMANCE**, and MEASURED empty on 19 of 19 (§0.2) |
| a fourth basis `warrant` for the Realm's consecration | proposed by the per-rung analysis | **EXTENSION of the judging-set door, not a fourth basis.** A consecration is `determine` by a judging set whose members' seats lie **outside** the consecrated seat's containment path, so what must widen is the *door* — `04 §B.7` call 3's *"the seats whose remit covers the matter at that venue"* plus a venue admission test — and not `conferral`'s value set |
| `revocation ∈ {purview, purview+holdings+rank, none, term}` | `04 §B.7` call 1 (*"two **values** of `revocation.conjuncts`"*); Jordan verbatim at `rosters.yaml:718-724` | **CONFORMANCE.** The three-term conjunction for a title already runs at `predicates.py:255-274`; what is wrong is that it is reached by **branching on the post string** at `:252` instead of reading a declared value |
| `H-91` — `remit:revoke` NECESSARY (Part E) versus purview SUFFICIENT (Jordan) | `predicates.py:276-286` registers the conflict in place | **CLOSED, and it dissolves rather than compromising.** `remit:revoke` is the **actor's** side (*may this seat take this kind of act?*); the basis is the **target's** side (*what does emptying THIS seat require?*). Two conjuncts, two owners, no over-refusal. A seat whose basis is `none` is unrevocable however broad the remit; a seat with a `purview` basis is unrevocable by someone whose remit lacks `revoke` however wide the purview |
| `term` as a revocation basis | `04 §B.8`'s `term? (matures_at, declared_by : ActId, closer)`, *"Replaces payload?"* | **CONFORMANCE**, with `04 §B.8`'s own caveat quoted: *"the basis resolves against the Seat — `Seat.revocation` is authoritative and `term.closer` names a basis, not a second authority"* |
| an `abolish` verb, because a seat that can be created and never destroyed is an unenumerated permanence | `01:185-224` (AX-6); `01:506-527` (ID-14) | **EXTENSION, and it is owed rather than wanted.** `(Office, exists)` is already a `[RES]`/ACTS row emitting `office.established` (`write_matrix.yaml:126-132`); it gains `office.abolished`. `release` closes a **Tenure**; abolishing a seat destroys the **Seat**, and ID-14's load-time check is over tenure kinds, so it cannot see this |

> ### **RULED: two declared fields, four values each, and no branch.** Cited to `04 §B.7` call 1,
> `04 §B.8`, and Jordan's two revocation rules at `rosters.yaml:718-724`. **H-91 closes here** under
> `CLAUDE.md` §0 gate 5: two conjuncts with two owners is the reading the architecture obviously
> wants, and no ruling is needed to see it. `abolish` is escalated to nobody — AX-6 already requires
> it.

## §A.4 · THE COUNCIL IS ONE SEAT — and the one thing genuinely open is where a member's grant lives

| candidate | who owns it? | verdict |
|---|---|---|
| a council is N seats | — | **REFUSED.** `01:1477`: *"a council \| **one seat, many holders** \| ⚠ **not N seats.** `hold` is **1-per-object** (§D.8), so a council is **one seat whose membership is a Query over `oblige`**"*. Enforced in code: `world_q.hold_force` raises on a second live `hold` (`world_q.py:138-144`) |
| a council is one seat whose members `oblige` to it | `01 §E.2.5` | **CONFORMANCE.** `oblige : Person → Person \| Office, many` (`holonic_ARCHITECTURE.md:541`) already admits the edge |
| a `veto_holders` list on a venue | proposed by the design stage's own first draft | **REFUSED, and this is a free cut.** A block is one bench member `repudiate`ing their commit; below quorum `determine` is refused and emits `determine.refused`. A veto field would make blocking **free and anonymous**, where a `repudiate` is an act, is witnessed, and puts the blocker's name in every ledger the fan-out reaches |
| quorum as a stored tally | — | **REFUSED.** Quorum is a `cardinality` conjunct over live `commit` edges to the disposition — one of the seven forms (`rosters.yaml:1114`), with `needs: [subject, from, to]` |
| **where a council member's grant lives** | unowned | ⚠ **OPEN, and I am NOT escalating it — see below** |

⚠ **The grant fork, and why it does not survive `CLAUDE.md` §0's five gates.** The analysis stage
filed it as a `needs_jordan`: if a member's authority rides on a `hold` payload, a council member — who
`oblige`s rather than holds — has no grant and can form no `remit:` candidate; so either the grant
rides on the `oblige` edge too (one fact, two homes by edge kind) or `hold` relaxes to
many-per-object. **Both arms are answered by gate 3 and gate 1 together, and the answer is neither
arm.** `04 §B.8` retires `payload?` in favour of `term?` — so **there is no payload to put a grant on**,
and the fork's premise is dead. §A.6 puts the grant nowhere at all: what a person may do by virtue of a
seat is a **claim in their own ledger about that seat**, and a council member's claim of the seat's
remit is deposited by the same witness step that deposits a sole holder's. `hold` keeps 1-per-object,
`oblige` carries no payload, and the fork closes.

> ### **RULED: one seat, membership a Query over `oblige`, quorum a `cardinality` conjunct, a block a
> `repudiate`.** Cited to `01 §E.2.5` (`01:1477`), `04 §B.7` call 2, `world_q.py:138-144` and
> `rosters.yaml:1086-1122`. The grant fork **closes at gate 3** on `04 §B.8` and is not escalated.

## §A.5 · SUCCESSION IS A DISPOSITION OF THE HOLDER

`01:1229-1238`, opened at the line: *"`succeed` — its subject is a `Rung`, and a Rung cannot act… **So
it has an owner that cannot author**"*, and the repair: *"succession is a disposition of the holder, not
a property of the place… **A pointer the place owns is a pointer nobody can change; a pointer the
holder owns is an act of politics**, which is what succession is."*

| candidate | who owns it? | verdict |
|---|---|---|
| `succeed : Rung → Person` | `holonic_ARCHITECTURE.md:542`, still | **CONFORMANCE defect.** `04 §A.3` row 8 re-subjects it: *"`succeed : Person → Person`, owned by the holder"*, and `04 §B.8`'s type line carries it verbatim |
| a three-branch succession-contest table | the superseded hearth design | **REFUSED, and nothing is lost.** A `follow:` clause is a predicate; a predicate selecting **exactly one** claimant resolves the vacancy date; **selecting none or many leaves the date unresolved, and it re-fires.** The third branch — *"the seat is held by whoever physically holds it and the contest re-opens at every standing date… This is open war"* — **is what an unresolved date is** |
| a `follow:` clause may name a person | the uniformity rule (§A.9.3) | **ADMITTED, narrowly, and the licence is named rather than hidden.** Naming your heir **is** the content of the rule. The uniformity rule binds clauses that condition **other people's** options; a clause whose scope is the issuer's own seat is not one |
| `succeed` is unformable person-side | — | **⛔ FALSE.** MEASURED: `succeed` is `own`-eligible (`verb_table.yaml:493`) and carries a typed `relation` cell (`:496-499`). It lacks only an `@effect_for` body |

> ### **RULED: `04 §A.3` row 8 — succession is the holder's own `succeed` Tenure, and the vacancy
> date is where it is contested.** One mechanism spans the whole ladder: **a duchy's succession crisis
> and a squabble over a miller's cottage run the same clause, the same date and the same
> selects-≠-1 rule**, which is `ID-7` (`01:444`) paying for itself at the widest separation of scales
> the game has.

## §A.6 · THE COMMISSION — `H-71` closes person-side, from the holder's own ledger

**The blocker, read at the line.** `options.py:107` is `person_side_eligible`, and its docstring names
its own two declines: *"`remit:<act>` — `H-71`, NEW. Needs the OFFICE's `remit_acts`… the person owns
the tenure and the office owns the remit. **Unlike `budget`'s collision there is no relocation
available: two holders of one office share one remit**, so it is not the person's state to move"*
(`options.py:119-124`). The `remit` branch is `:163-165`; the `presence` branch is `:166-168`; both
`TRACE.note(...)` and fall through to `return False` at `:169`.

| candidate | who owns it? | verdict |
|---|---|---|
| widen `choose`'s signature to take a `World` | — | **REFUSED, structurally.** `04 §C.3`: *"`decision/` imports `person_q` and `data/`. **It does not import `state/`, `world_q` or `loop/`**"*, and `04 §A.3` row 1 says why the module boundary exists: *"the only thing making no World in scope checkable by path rather than by reading bodies"* |
| put the grant on `Tenure.payload` | the 2026-09-16 sweep's arm 2 | **REFUSED — the field is retired.** `04 §B.8`: `term?` *"Replaces payload?"*. Building on `payload` builds on a field the architecture deleted |
| put the grant on `Tenure.conferrer` | the design stage's own carrier | **REFUSED — the field is gone.** `carriers.py:48-56` records the deletion and its reason: *"WHAT CONFERRED a Tenure is the opening Act, in an append-only log with `causes[]`. A field here would be a second home for a fact the act already holds — `ID-2`"* |
| **the conferee's own ledger carries a claim of the seat's remit, deposited at the conferral** | the conferee, in their own ledger (`carriers.py:382`) | ⭐ **EXTENSION, ADOPTED.** `remit:<act>` person-side = *the actor's ledger carries a live claim that they hold seat `S`, and a claim that `S`'s remit contains `<act>`*. The `confer` Event's payload carries the conferred seat's `remit.acts`; WITNESS deposits each observer's own claim of it (`witness.py:175`: `src = "firsthand_via_knot" if via_knot else "firsthand"`), and the conferee is present by construction |

**Why this is better than a wider signature, and not merely cheaper:**

- **`AX-2` is honoured rather than dodged.** `01:102-103`: *"A person decides from what they hold, and
  what they hold may be false. There is no view of world truth available inside a decision — not
  capped, not filtered: **absent**."* A claim about a seat is the person's own state.
- **Authority stays on the seat.** What is in the ledger is a *belief about the seat*, and it decides
  only what a person **attempts**. `_eligible` at RESOLVE reads the World and the seat.
- **The gap between the two readings is the mechanism, and it runs both ways.**

| the belief says | the world says | what happens |
|---|---|---|
| permitted | permitted | the act resolves |
| permitted | forbidden | **refused**, and `emits_on_refusal` fires — *so he learns* |
| forbidden | permitted | **he never tries, and nobody ever learns.** A struck law goes on governing because its subjects still believe it |
| forbidden | forbidden | nothing, and correctly |

Row 3 needs no mechanism at all, and a man holding a **forged** commission is row 2: `forge` writes
`Record.forgery_quality` (`carriers.py:428`; `write_matrix.yaml`'s `(Record, forgery_quality)` row
emits `record.forged`), he attempts the act in good faith, and RESOLVE refuses it because RESOLVE asks
the seat.

⚠ **`presence:<rung>` is the same repair and it is listed separately because its cause is different.**
`options.py:166-168` declines because *"the ARGUMENT IS A PLACEHOLDER naming a kind of rung rather than
an id"* — `H-75`, not `H-71`. The repair is the actor's own live `contain` Tenure, which
`containing_rung_of` already reads without a World (`options.py:172`). **Do not schedule the two as one
item.**

> ### **RULED: the grant is a CLAIM, not a field — `04 §B.8` (no payload), `carriers.py:48-56` (no
> conferrer), `01:102-103` (AX-2), `witness.py:175` (the producer).** This is the row that opens
> everything else: **until `remit:` is evaluable person-side nobody can `convene`, so no `Date` is ever
> created, so Q1 forms for nobody, so no seat is ever asked about its own assembly** — which is why
> `dates 0 · docket 0` is a measurement about *one blocked disjunct* and not about the calendar.
> Falsifier: `test_no_person_can_choose_a_governance_verb_and_h71_is_why` goes **red** and is rewritten
> as the control — *a seat whose remit lacks the act forms no candidate.*
