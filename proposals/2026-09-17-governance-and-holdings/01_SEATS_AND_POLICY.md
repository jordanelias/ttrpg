# 01 · SEATS AND POLICY — governance and management at every rung, hearth to realm

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` · id: **ED-IN-0231**. Grade under `CLAUDE.md` §0.2: **`paper`** — nothing in this file
## executes, PART C.5 says what would move it, and no row here may be cited as done.
## Method: authored at tier **`opus`** (`CLAUDE.md` §10 — *competing-considerations judgment,
## multi-doc synthesis*), against the working tree at 2026-09-17. Reconciliation of the disagreements
## this file settles was a read-only `fable` stage; the per-rung and engine-fit analyses were `opus`.
## Citation discipline: `architecture/meta/04_CODE_ARCHITECTURE.md` is cited **`ARCH §Letter.Number`**
## and never `ARCH:NNN` — its line numbers have drifted twice. Every `path:line` below was opened at
## that line in this session; the appendix lists the citations I found wrong in my own sources and
## repaired.
## ⚠ **UNIFIED 2026-09-17 (`00_THE_DESIGN.md`).** Suite-wide: **`ARCH`** = `architecture/meta/04_CODE_ARCHITECTURE.md`,
## **`AX`** = `architecture/meta/01_AXIOMS.md` — a bare `01`/`02`/`03`/`04` now always means a file in
## THIS directory, which is what ~~`04 §B.7`~~ and ~~`01:443`~~ collided with. This file's falsifiers
## are **`SP-n`** and its loops **`SP-L±n`**; a sibling's carry that sibling's prefix. The multi-season
## project is **a `works`** (§A.12), never *a work* or *a project*. Reconciliation edits are struck in
## place, never deleted.

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
> **And the architecture clause this file exists to apply**, `ARCH §B.7`, whose grade is MECHANICAL:
> *"**purview is asked of the seat exercised, not the actor** — `Act.via : SeatId?`; every purview
> walk uses `via.scope`. **A regent has the seat's purview**."*

---

# PART 0 · THE CONFORMANCE DIVISION, AND IT IS THE SPINE OF THIS FILE

**Most of the seat model below is already ratified Layer 1 and merely unbuilt.** It is not this file's
invention and this file claims no novelty for it. `ARCH §B.7` ships the `Seat`; `ARCH §A.3` rows 5, 7, 8,
11, 12, 13, 14, 15 ship eight of the deletions; `ARCH §B.8` retires `Tenure.payload` in favour of
`term?`; `ARCH §B.9` gives `Act` its `via`; `AX §E.2.5` rules the council. **A proposal that restates
ratified architecture as a proposal is worse than useless — it invites a session to re-decide a
settled thing.** So every section below carries one of three words, and the three lists are here, in
front, so a reader can skip the first list entirely.

## §0.1 · The three lists

**CONFORMANCE — RATIFIED Layer 1, UNBUILT in the engine. Nothing here is proposed; it is owed.**

| item | the ratified clause | the engine as measured |
|---|---|---|
| one `Seat` type, no `Title` type | `ARCH §B.7` call 1 | `Office` (`engine/season/state/carriers.py:481-549`) plus a title/body `Forbidden` at `:537-544` |
| **no `is_title` branch anywhere** (ID-4) | `ARCH §B.7` call 1; `AX:443` | the branch runs: `engine/season/loop/predicates.py:252` |
| **`establishment` is a Query over `oblige`, not a field** | `ARCH §B.7` call 2; `AX §E.2.5`'s own correction | a field (`carriers.py:491`), read at `engine/season/queries/world_q.py:413`; empty on all 19 offices |
| **`judging_set_rule` deleted from `Rung`** | `ARCH §B.7` call 3; `ARCH §A.3` row 7 | still in the whitelist: `carriers.py:568-569` |
| **purview is asked of the seat exercised, not the actor** | `ARCH §B.7`, grade MECHANICAL | asked of the actor's *post string*: `predicates.py:144-155` |
| `Tenure.term?` replaces `payload?` | `ARCH §B.8` | `payload` still declared (`carriers.py:59`) with a live matrix row |
| `Act.via : SeatId?` | `ARCH §B.9`; `ARCH §C.2` F3 | absent from the `Act` the engine folds |
| the write gate admits **four** Tenure-write bases and a conferral opener matches none | `ARCH §C.2` F3, verbatim | `confer` and `revoke` both write `Tenure.until` on somebody else's edge |
| `hold.subject : Person` only | `ARCH §A.3` row 12; `ARCH` PART D row 14 | 16 of 35 live `hold` Tenures have a **faction** subject (measured, §0.2) |
| `budget` never includes an `office_bonus` | `ARCH §A.3` row 15 | `engine/season/decision/budget.py:56-57` pays one per live `hold` |
| `Petition` and `Dispensation` are **kinds of `Record`** | `ARCH §A.3` row 11 | both are write-matrix kinds with **no carrier** (`carriers.py` has no such class) |
| succession is the holder's disposition, not the place's | `ARCH §A.3` row 8; `AX:1235-1239` | `succeed`'s subject is still a `Rung` (`architecture/holonic_ARCHITECTURE.md:542`) |
| a council is **one seat, many holders via `oblige`** | `AX §E.2.5` | `Office.binds` has **one occurrence in the whole package** — its own declaration (`carriers.py:488`) |

**EXTENSION — consistent with ratified Layer 1, unratified, and this file's actual proposal.**

| item | what it rests on |
|---|---|
| **the policy instrument**: a `dispensation` `Record`, held by its issuer, whose reach is the issuing seat's (§A.7) | `ARCH §A.3` row 11; `ARCH §B.4/B.5`; `holonic_ARCHITECTURE.md:538`; `engine/season/loop/effects.py:262-289` |
| **`in_force(w, rung, clause)`** — the nearest-ancestor walk up `contain`, plus a `reach` operand (§A.8) | `world_q.py:48` `parent_of`; the same ascent `predicates.py:105-140` and `world_q.py:416-437` already walk |
| **the seven clauses**, three as step readers and four as `requires` conjuncts (§A.9) | `rosters.yaml:1086-1122` (seven forms, closed); `engine/season/data/requires.py:542` (`all`) |
| **the conferral claim** — `remit:` evaluated person-side from the holder's own ledger (§A.6) | `options.py:107-169`; `engine/season/loop/witness.py:175`; `AX:100-103` (AX-2) |
| **a `record_kinds` roster**, so `Record.kind` is declared rather than matched (§A.7.4) | `AX:443` (ID-4); `effects.py:285`'s `d.get("kind") or "text"` |
| **the delivered/demanded gap as a band on a Query**, changing options and never outcomes (§A.13) | `AX:631-645` (ID-17 → `T-b`); `AX:1332-1340` (breach *is* the sworn/performed gap) |
| **Q5 `purview`** — a fifth question source, claim-gated (§A.15) | `rosters.yaml:250-270` (`question_sources`, open, ordered); `predicates.py:105-140` |
| **a matter condition on the shipped stage maturation**, and `stage.stalled` on its else branch (§A.12) | `engine/season/loop/matter.py:64-109` |
| **`sworn(policy) = members(w, terms)`** — not a new Query, the shipped one (§A.7.3) | `world_q.py:200-211` |

**DEPARTURE — needs a ruling. There is exactly one IN THIS FILE, and it is PART C.6's RR-1.**
⚠ **Unified 2026-09-17: the SUITE carries three, not one.** RR-1 (here), **RR-2** =
`ED-SE-0051`'s capacity arm (`02` §A.7, already queued), and **RR-3** = `03` §C.3's departure from
`scale_transitions_v30.md`, a `## Status: CANONICAL` head. `04` §C.4 is the single owner of the
surviving list and `04` §C.5 of the closed one; this file owns RR-1's argument and nothing else.

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
resolvable_verbs(): 18 of 38.  NOT resolvable, ALL TWENTY (re-measured 2026-09-17): carry · commit ·
         comply · determine · establish · evade/defy · exchange · forge · issue · kill/wound · levy ·
         oblige · open_case · petition · refract · repudiate · restore · succeed · thread_read · tie/knot
         person-side formable (an `own` alternative): 28.  BOTH formable and resolvable: 13 (see `03` §A.2.1)
binding_decision rows: 9.  SEVEN are `remit:`-only; TWO — `release`, `succeed` — are `own`.
```

**Five of those numbers are load-bearing on what follows and none is in any source document in this form.**

1. **Every one of the nineteen seats has an empty `conferral` and an empty `revocation` basis** — and
   `_req_confer` refuses an office with no conferral basis (`predicates.py:181-182`), `_req_revoke` one with
   no revocation basis (`:234-235`). **So no seat in the built world can be conferred or revoked, and the
   reason is not `remit:` — it is two empty strings.** A plan that fixes the eligibility model and not the
   content fixes nothing.
2. **Sixteen of nineteen seat-holders have purview over nothing, including their own seat's rung**, because
   `titles_held` filters on `title_domain(post) is not None` (`predicates.py:151-152`) and sixteen posts —
   *Chief Parliamentary Clerk*, *Cardinal Justice*, *Royal Marshal*, *Skald-Chief* — are not on the
   eleven-name `titles.domains` roster (`rosters.yaml:755-766`). **`ARCH §B.7`'s MECHANICAL invariant,
   measured in the negative: purview is read off a post STRING, so every non-title seat governs nothing.**
3. **`records 0`.** Not one `Record` exists in the built world, which is why §A.7's instrument is `paper`
   and not `partial`.
4. **`issue`, `commit`, `petition`, `determine` and `repudiate` are all unresolvable, for different
   reasons** — which matters for sequencing. `issue`'s `requires` cell *"is NOT a predicate at all but a
   constraint on the well-formedness of the Act"* (`hole_register.yaml:763`), whereas `commit` and
   `repudiate` carry **typed** cells and lack only an `@effect_for` body (`effects.py` registers eleven:
   confer · release · revoke · convene · move · work · create_record · destroy_record · kill/wound · utter ·
   transfer).
5. **`dates 0` and `docket 0`.** `(Date, due_at)` is written only by `convene`
   (`write_matrix.yaml:93-100`), `convene` is `remit:convene`, and `remit:` declines person-side
   (`options.py:163-165`). **One blocked disjunct; the whole venue layer downstream.**

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
one site (`world_q.py:413`) and is **empty on all nineteen offices**, and `ARCH §B.7` call 2 *rejects the
field* in favour of a Query over `oblige`. A decay channel on either is a mechanism riding two dead
fields, one of which the architecture deleted. **The replacement is §A.13: a band on a
delivered-versus-demanded Query, which changes which options a subject sees and never an outcome.**

---

# PART A · THE CLAIMS, EACH WITH ITS VERDICT

Every subsection is a candidate/owner/verdict table closed by a `> ### RULED:` line citing the clause
that decides it. A verdict of **CONFORMANCE** means *this was decided; build it*. **EXTENSION** means
*this is the proposal*. **DEPARTURE** means *do not build it until Jordan rules*.

## §A.1 · THE SEAT — one type, and Layer 1 already shipped it

`ARCH §B.7`, verbatim:

```
Seat := ( id, post, body?, scope? (null = a cluster), remit(acts[], binds)
        , conferral  -- which ACT fills it: confer by <seat> | determine by <judging seats> | succeed
        , revocation -- which seat may revoke, and the CONJUNCTS
        , upkeep, dates[], exists )
NEVER:   who holds it · who serves it · a modifier of any kind
```

| candidate | who owns it? | verdict |
|---|---|---|
| a `Seat` type distinct from a `Title` type | `ARCH §B.7` call 1 | **CONFORMANCE.** *"There is no `Title` type"*; a title and an ordinary office are two **values** of `revocation.conjuncts`. The engine's `Office` is the Seat and the title/body `Forbidden` at `carriers.py:537-544` is the symptom |
| `domain : RungId[]` — a SET of rungs, so one Lord holds several territories in one seat | proposed by the per-rung analysis | **REFUSED.** `ARCH §B.7`'s `scope?` is singular. Purview is the `contain` closure of `scope` plus the holder's own `hold` Tenures, and `predicates.py:105-140` already walks a **disjunction over every seat the actor holds** — *"authority over a holding is authority from ANY title the actor holds"* (`:127-129`). A Lord with three territories holds three seats and the disjunction covers him. A set-valued field also breaks rank: `max(ordinal(kind(d)))` over a Count's territories computes **territory**, which inverts Jordan's *"rank is not headcount"* (`rosters.yaml:706-709`) |
| `remit : (act, scope?)[]` — a scope per act | proposed by the per-rung analysis | **REFUSED in v1.** `ARCH §B.7` pairs `acts[]` with one `binds`, and no seat in the draft roster needs *this act here and that act there*. A Duke who may `issue` across the duchy and `confer` in one province **establishes a sub-seat** for the second, which is `ARCH §B.7`'s own delegation row (`establish` → `confer` → `revoke`). CONVENTION-grade question, PART C.2 |
| `binds : TenureKind` — the relation over which the bound set is computed | `ARCH §B.7`'s `remit(acts[], binds)` | **CONFORMANCE, and the reader is missing.** MEASURED: `binds` occurs once in the whole package, its own declaration (`carriers.py:488`), on the dataclass default `"members_by_admission"` for all nineteen offices. `ID-13` (`AX:489`) makes that *"not a weak field but one that does not exist, wearing a schema's clothes"* |
| `establishment` as a stored list | `ARCH §B.7` call 2 | **CONFORMANCE: delete the field.** *"A set of persons on a seat is two homes for one fact. A person joins by `oblige : Person → Seat` and leaves by `release`."* And `ARCH §B.7` names the cost of keeping it: *"establishment size as a number nobody can source"* |
| `judging_set_rule` on `Rung` | `ARCH §A.3` row 7 | **CONFORMANCE: delete.** *"decision-shaped state on a container."* `world_q.judging_set` already raises `Unspecified` rather than reading it (`world_q.py:146-148`) |

> ### **RULED: the seat model is `ARCH §B.7`, entire, and this file adds nothing to it.**
> Cited to `ARCH §B.7` (three calls, four invariants) and `ARCH §A.3` rows 5, 7, 12, 14, 15. The two
> shape changes the analysis stage proposed — a set-valued domain and a per-act remit scope — are
> **refused here**, each on a clause of `ARCH §B.7` rather than on cost. The work owed is a **reader
> for `binds`**, a **Query for `establishment`**, and the deletion of four helpers (§B.2).

⚠ **A struck claim, kept in place.** ~~*A prince-bishopric cannot be spelled, so the title/body
refusal must be deleted for canon's sake.*~~ The refusal at `carriers.py:537-544` is a **content**
problem, not a shape one: under `ARCH §B.7` a person may hold a title seat **and** a body seat, because
`hold` is 1-per-object and not 1-per-person (`holonic_ARCHITECTURE.md:538`; enforced at
`world_q.py:138-144`), and `under_purview` is *"a DISJUNCTION over the seats"* (`predicates.py:127-129`).
Exclusivity, where a setting wants it, is refused at `confer` by a `cardinality` or `relation` conjunct
once `Act.via` lands — not by a constructor that refuses a true thing to prevent a false one.

## §A.2 · PURVIEW IS ASKED OF THE SEAT EXERCISED — and here is what not doing it costs

| candidate | who owns it? | verdict |
|---|---|---|
| purview read off the **actor's post string** (today) | `predicates.py:144-155` `titles_held`, filtering `title_domain(o.post) is not None` | **CONFORMANCE defect.** MEASURED today: 3 of 19 posts are on the ladder, so **16 of 19 seat-holders have purview over nothing, including their own seat's rung** |
| purview read off `Act.via.scope` | `ARCH §B.7`, grade **MECHANICAL**; `ARCH §B.9`'s `Act := (id, actor, via : SeatId?, …)` | **CONFORMANCE.** *"A regent has the seat's purview"* — which is the whole of `AX §E.2.1`'s requirement, *"THE TITLE AND THE GOVERNING MUST BE SEPARABLE"* (`AX:1367`) |
| a `via.scope` sub-field distinct from `Seat.scope` | nothing | **REFUSED.** Nothing licenses a second scope. `via` names the seat; the seat carries the scope |

> ### **RULED: `ARCH §B.7`, MECHANICAL — purview is asked of the seat exercised, and `Act.via` is how the
> seat enters the act.** The three consequences are not separate items: the `is_title` branch
> (`predicates.py:252`) goes, because the two rules become two values of `revocation`
> (`rosters.yaml:718-724` carries Jordan's own two rules verbatim); `titles_held` and
> `highest_title_rank` go with it (`predicates.py:144-164`), and `title_domain` with them — ⚠ **line
> repair, 2026-09-17: `title_domain` is NOT in `predicates.py`.** ~~`predicates.py:144-164`~~ for that
> one; it is **`engine/season/data/rosters.py:459`**, and `predicates.py:151-152` is its call site. A
> session deleting "four helpers in one file" would have found three; and the write gate
> gains the clause `ARCH §C.2` F3 says it needs, since **a conferral-basis opener matches none of the
> four admitted bases** and *"so does `confer`, today"*.

## §A.3 · CONFERRAL AND REVOCATION ARE DECLARED BASES, NOT CODE PATHS

`AX:1495-1498` is the corpus's sharpest sentence on this and it is quoted rather than paraphrased:

> *"§D.6 gives an Office a **`conferral`** field — 'the basis, **per office**' — which is exactly the
> slot that distinguishes *the Duke names him* from *the burghers elect him* from *it passes to the
> eldest*. **Delegation does not need a delegation mechanism. It needs the `conferral` basis to be
> specified**, and that field has been on the Office since #353 carrying nothing."*

| candidate | who owns it? | verdict |
|---|---|---|
| `conferral ∈ {confer by <seat>, determine by <judging seats>, succeed}` | `ARCH §B.7`'s own list | **CONFORMANCE**, and MEASURED empty on 19 of 19 (§0.2) |
| a fourth basis `warrant` for the Realm's consecration | proposed by the per-rung analysis | **EXTENSION of the judging-set door, not a fourth basis.** A consecration is `determine` by a judging set whose members' seats lie **outside** the consecrated seat's containment path, so what must widen is the *door* — `ARCH §B.7` call 3's *"the seats whose remit covers the matter at that venue"* plus a venue admission test — and not `conferral`'s value set |
| `revocation ∈ {purview, purview+holdings+rank, none, term}` | `ARCH §B.7` call 1 (*"two **values** of `revocation.conjuncts`"*); Jordan verbatim at `rosters.yaml:718-724` | **CONFORMANCE.** The three-term conjunction for a title already runs at `predicates.py:254-274`; what is wrong is that it is reached by **branching on the post string** at `:252` instead of reading a declared value |
| `H-91` — `remit:revoke` NECESSARY (Part E) versus purview SUFFICIENT (Jordan) | `predicates.py:276-286` registers the conflict in place | **CLOSED, and it dissolves rather than compromising.** `remit:revoke` is the **actor's** side (*may this seat take this kind of act?*); the basis is the **target's** side (*what does emptying THIS seat require?*). Two conjuncts, two owners, no over-refusal. A seat whose basis is `none` is unrevocable however broad the remit; a seat with a `purview` basis is unrevocable by someone whose remit lacks `revoke` however wide the purview |
| `term` as a revocation basis | `ARCH §B.8`'s `term? (matures_at, declared_by : ActId, closer)`, *"Replaces payload?"* | **CONFORMANCE**, with `ARCH §B.8`'s own caveat quoted: *"the basis resolves against the Seat — `Seat.revocation` is authoritative and `term.closer` names a basis, not a second authority"* |
| an `abolish` verb, because a seat that can be created and never destroyed is an unenumerated permanence | `AX:185-224` (AX-6); `AX:506-527` (ID-14) | **EXTENSION, and it is owed rather than wanted.** `(Office, exists)` is already a `[RES]`/ACTS row emitting `office.established` (`write_matrix.yaml:126-132`); it gains `office.abolished`. `release` closes a **Tenure**; abolishing a seat destroys the **Seat**, and ID-14's load-time check is over tenure kinds, so it cannot see this |

> ### **RULED: two declared fields, four values each, and no branch.** Cited to `ARCH §B.7` call 1,
> `ARCH §B.8`, and Jordan's two revocation rules at `rosters.yaml:718-724`. **H-91 closes here** under
> `CLAUDE.md` §0 gate 5: two conjuncts with two owners is the reading the architecture obviously
> wants, and no ruling is needed to see it. `abolish` is escalated to nobody — AX-6 already requires
> it.

## §A.4 · THE COUNCIL IS ONE SEAT — and the one thing genuinely open is where a member's grant lives

| candidate | who owns it? | verdict |
|---|---|---|
| a council is N seats | — | **REFUSED.** `AX:1477`: *"a council \| **one seat, many holders** \| ⚠ **not N seats.** `hold` is **1-per-object** (§D.8), so a council is **one seat whose membership is a Query over `oblige`**"*. Enforced in code: `world_q.hold_force` raises on a second live `hold` (`world_q.py:138-144`) |
| a council is one seat whose members `oblige` to it | `AX §E.2.5` | **CONFORMANCE.** `oblige : Person → Person \| Office, many` (`holonic_ARCHITECTURE.md:541`) already admits the edge |
| a `veto_holders` list on a venue | proposed by the design stage's own first draft | **REFUSED, and this is a free cut.** A block is one bench member `repudiate`ing their commit; below quorum `determine` is refused and emits `determine.refused`. A veto field would make blocking **free and anonymous**, where a `repudiate` is an act, is witnessed, and puts the blocker's name in every ledger the fan-out reaches |
| quorum as a stored tally | — | **REFUSED.** Quorum is a `cardinality` conjunct over live `commit` edges to the disposition — one of the seven forms (`rosters.yaml:1114`), with `needs: [subject, from, to]` |
| **where a council member's grant lives** | unowned | ⚠ **OPEN, and I am NOT escalating it — see below** |

⚠ **The grant fork, and why it does not survive `CLAUDE.md` §0's five gates.** The analysis stage
filed it as a `needs_jordan`: if a member's authority rides on a `hold` payload, a council member — who
`oblige`s rather than holds — has no grant and can form no `remit:` candidate; so either the grant
rides on the `oblige` edge too (one fact, two homes by edge kind) or `hold` relaxes to
many-per-object. **Both arms are answered by gate 3 and gate 1 together, and the answer is neither
arm.** `ARCH §B.8` retires `payload?` in favour of `term?` — so **there is no payload to put a grant on**,
and the fork's premise is dead. §A.6 puts the grant nowhere at all: what a person may do by virtue of a
seat is a **claim in their own ledger about that seat**, and a council member's claim of the seat's
remit is deposited by the same witness step that deposits a sole holder's. `hold` keeps 1-per-object,
`oblige` carries no payload, and the fork closes.

> ### **RULED: one seat, membership a Query over `oblige`, quorum a `cardinality` conjunct, a block a
> `repudiate`.** Cited to `AX §E.2.5` (`AX:1477`), `ARCH §B.7` call 2, `world_q.py:138-144` and
> `rosters.yaml:1086-1122`. The grant fork **closes at gate 3** on `ARCH §B.8` and is not escalated.

## §A.5 · SUCCESSION IS A DISPOSITION OF THE HOLDER

`AX:1230-1239`, opened at the line: *"`succeed` — its subject is a `Rung`, and a Rung cannot act… **So
it has an owner that cannot author**"*, and the repair: *"succession is a disposition of the holder, not
a property of the place… **A pointer the place owns is a pointer nobody can change; a pointer the
holder owns is an act of politics**, which is what succession is."*

| candidate | who owns it? | verdict |
|---|---|---|
| `succeed : Rung → Person` | `holonic_ARCHITECTURE.md:542`, still | **CONFORMANCE defect.** `ARCH §A.3` row 8 re-subjects it: *"`succeed : Person → Person`, owned by the holder"*, and `ARCH §B.8`'s type line carries it verbatim |
| a three-branch succession-contest table | the superseded hearth design | **REFUSED, and nothing is lost.** A `follow:` clause is a predicate; a predicate selecting **exactly one** claimant resolves the vacancy date; **selecting none or many leaves the date unresolved, and it re-fires.** The third branch — *"the seat is held by whoever physically holds it and the contest re-opens at every standing date… This is open war"* — **is what an unresolved date is** |
| a `follow:` clause may name a person | the uniformity rule (§A.9.3) | **ADMITTED, narrowly, and the licence is named rather than hidden.** Naming your heir **is** the content of the rule. The uniformity rule binds clauses that condition **other people's** options; a clause whose scope is the issuer's own seat is not one |
| `succeed` is unformable person-side | — | **⛔ FALSE.** MEASURED: `succeed` is `own`-eligible (`verb_table.yaml:494`) and carries a typed `relation` cell (`:496-499`). It lacks only an `@effect_for` body |

> ### **RULED: `ARCH §A.3` row 8 — succession is the holder's own `succeed` Tenure, and the vacancy
> date is where it is contested.** One mechanism spans the whole ladder: **a duchy's succession crisis
> and a squabble over a miller's cottage run the same clause, the same date and the same
> selects-≠-1 rule**, which is `ID-7` (`AX:444`) paying for itself at the widest separation of scales
> the game has.

## §A.6 · THE COMMISSION — `H-71` closes person-side, from the holder's own ledger

**The blocker, read at the line.** `options.py:107` is `person_side_eligible`, and its docstring names its
own declines: *"`remit:<act>` — `H-71`, NEW. Needs the OFFICE's `remit_acts`… the person owns the tenure and
the office owns the remit. **Unlike `budget`'s collision there is no relocation available: two holders of
one office share one remit**, so it is not the person's state to move"* (`:119-124`). The `remit` branch is
`:163-165`, the `presence` branch `:166-168`; both `TRACE.note(...)` and fall through to `return False`.

| candidate | who owns it? | verdict |
|---|---|---|
| widen `choose`'s signature to take a `World` | — | **REFUSED, structurally.** `ARCH §C.3`: *"`decision/` imports `person_q` and `data/`. **It does not import `state/`, `world_q` or `loop/`**"*, and `ARCH §A.3` row 1 gives the reason: *"the only thing making no World in scope checkable by path rather than by reading bodies"* |
| the grant on `Tenure.payload` | the 2026-09-16 sweep's arm 2 | **REFUSED — retired.** `ARCH §B.8`: `term?` *"Replaces payload?"* |
| the grant on `Tenure.conferrer` | the design stage's own carrier | **REFUSED — gone.** `carriers.py:48-56`: *"WHAT CONFERRED a Tenure is the opening Act… A field here would be a second home for a fact the act already holds — `ID-2`"* |
| **the conferee's own ledger carries a claim of the seat's remit, deposited at the conferral** | the conferee (`carriers.py:382`) | ⭐ **EXTENSION, ADOPTED.** `remit:<act>` person-side = *the actor's ledger carries a live claim that they hold seat `S`, and a claim that `S`'s remit contains `<act>`*. The `confer` Event's payload carries the seat's `remit.acts`; WITNESS deposits each observer's own claim (`witness.py:175`: `src = "firsthand_via_knot" if via_knot else "firsthand"`), and the conferee is present by construction |

**Why this is better than a wider signature and not merely cheaper.** `AX-2` is honoured rather than dodged
— `AX:102-103`: *"A person decides from what they hold, and what they hold may be false. There is no view of
world truth available inside a decision — not capped, not filtered: **absent**"* — and a claim about a seat
is the person's own state. **Authority stays on the seat:** what is in the ledger is a *belief about* it,
deciding only what a person **attempts**, while `_eligible` at RESOLVE reads the World and the seat. **The
gap between the two readings is the mechanism, and it runs both ways:**

| the belief says | the world says | what happens |
|---|---|---|
| permitted | permitted | the act resolves |
| permitted | forbidden | **refused**, and `emits_on_refusal` fires — *so he learns* |
| forbidden | permitted | **he never tries, and nobody ever learns.** A struck law goes on governing because its subjects still believe it |
| forbidden | forbidden | nothing, and correctly |

Row 3 needs no mechanism at all, and a man holding a **forged** commission is row 2 — `forge` writes
`Record.forgery_quality` (`carriers.py:428`), he attempts the act in good faith, and RESOLVE refuses it
because RESOLVE asks the seat.

⚠ **`presence:<rung>` is the same repair with a different cause, and must not be scheduled as one item.**
`options.py:166-168` is the branch; its reason is the docstring at `:124-129`, *"the ARGUMENT IS A
PLACEHOLDER naming a kind of rung rather than an id"* — `H-75`, not `H-71`. ⚠ **Verified 2026-09-17,
because the code disagrees with itself:** the `TRACE.note` string at `:167` still says `H-33`, and the
docstring at `:126-129` records that `H-33` was BUILT and the citation went stale. `H-75` is the live
reason and the TRACE string is the stale artifact. The repair is the actor's own live `contain` Tenure, which `containing_rung_of`
(`options.py:172`) already reads without a World.

> ### **RULED: the grant is a CLAIM, not a field** — `ARCH §B.8` (no payload), `carriers.py:48-56` (no
> conferrer), `AX:102-103` (AX-2), `witness.py:175` (the producer). **This is the row that opens everything
> else:** until `remit:` is evaluable person-side nobody can `convene`, so no `Date` is created, so Q1 forms
> for nobody, so no seat is ever asked about its own assembly — which is why `dates 0 · docket 0` is a
> measurement about **one blocked disjunct** and not about the calendar. Falsifier:
> `test_no_person_can_choose_a_governance_verb_and_h71_is_why` goes **red** and is rewritten as the control
> — *a seat whose remit lacks the act forms no candidate.*

⚠ **The tree's own test says the same thing and scopes it correctly**, which is worth quoting so a
later session does not "discover" §0.3's correction twice. `test_season_shape.py:5011-5013`:
*"⚠ SEVEN OF THE EIGHT, NOT ALL EIGHT. `succeed` is eligible by `own` and IS offerable — it is the one
governance verb a person can choose."* And `:5005-5006`: *"it goes red the day `H-71` closes, which is
exactly when the claim becomes true."*

---

## §A.7 · THE POLICY INSTRUMENT — a dispensation Record, held by its issuer

**The instrument in two lines.** *A policy is a `Record` of kind `dispensation`, scoped to a rung,
naming one clause and one `OUGHT` Proposition as its terms, opened by `issue` through a seat, and held
by the issuer as an ordinary `hold` Tenure. It is in force while a living person holds it; it is read
by a walk up `contain`; and striking it, letting it lapse and re-issuing it are three different acts
with three different prices.*

### §A.7.1 · Three dead carriers, struck in place

The design stage's carrier was ~~`Tenure(subject = issuer, object = terms : PropositionId,
kind = "hold", conferrer = the seat exercised, payload = {scope, clause, terms_operands})`~~ and **every
field after `kind` is gone or taken**:

| the field | why it cannot carry this |
|---|---|
| ~~`conferrer`~~ | **deleted 2026-09-03**, `carriers.py:48-56`, on `ID-2`: *"WHAT CONFERRED a Tenure is the opening Act… A field here would be a second home for a fact the act already holds."* `ARCH §B.8` deletes it in the type on the same day and the same ground |
| ~~`payload`~~ | **retired** by `ARCH §B.8`: `term? (matures_at, declared_by : ActId, closer)` *"Replaces payload?"*. The matrix row `(Tenure, payload)` survives (`write_matrix.yaml`, emits `tenure.payload_set`) and is on the deletion list, not the build list |
| ~~`Proposition.scope`~~ as "the rung a policy binds" | **taken.** `Proposition.scope` is declared (`carriers.py:477`) and **written and read today**: `populated.py:491-492` mints five faction creeds as `Proposition(fid, "OUGHT", lead_pid, "carries the creed of", fac_name, 0, scope=template)`, where `template` is a ROLE TEMPLATE. MEASURED: 6 of 54 propositions carry `scope`. A policy defined as *"an OUGHT whose scope is a rung"* would put two meanings on one live field |

### §A.7.2 · The carrier that works, and it is already implemented for a different kind

`ARCH §A.3` row 11 folds `Petition` and `Dispensation` into **kinds of `Record`** — and MEASURED, neither
has a dataclass: `carriers.py` declares `Record`, `Proposition`, `Site`, `Office`, `Rung`, `Person`,
`Tenure`, `Claim`, and no `Dispensation` and no `Petition`. Both are nonetheless **write-matrix kinds**:
`(Dispensation, exists)` is `[RES]`/ACTS emitting `dispensation.issued` (`write_matrix.yaml:112-118`),
and `issue` writes it (`verb_table.yaml:262`). **So `issue` writes a field of a type that does not
exist**, and `ID-13`'s mirror image applies: a write with no carrier is as dead as a field with no
reader.

**Fold it, and the effect body is already there.** `effects.py:262-290` (`_eff_create_record`):

```
w.records[rid] = Record(rid, d.get("rung") or a.actor, d.get("kind") or "text",
                        subject_matter=d.get("subject_matter"), stages=stages)     # :284-285
w.add_tenure(Tenure(H(...), a.actor, rid, "hold", since=w.tick))                   # :288-289
```

⚠ **Line repair, 2026-09-17.** ~~`:285` / `:287`, body `:262-289`~~ → the body is **`:262-290`**, the
`Record` write **`:284-285`**, the S13 comment **`:286-287`** and `add_tenure` **`:288-289`**. `02`
carried the right numbers and this file carried a one-line drift; re-measured for the unification.
With the comment at `:286-287` stating the shape this instrument needs, already ruled: *"S13: possession is
a `hold` Tenure owned by the holder, never a field on the Record. **The maker holds what they made
until they part with it.**"*

| operand | its home | why that home and not another |
|---|---|---|
| **scope** (the rung) | `Record.rung` | the field's declared meaning is *a Record at a rung* (`carriers.py:426`), and `effects.py:285` already sets it from the act |
| **clause** (one of seven) | `Record.kind`, or `subject_matter` beside it | §A.7.4 |
| **terms** (a PropositionId, mood `OUGHT`) | `Record.subject_matter` (`carriers.py:429`, `Any`, set at creation and never after) | `AX:1327-1331`: *"**AN OATH IS AN UTTERANCE. WHAT IS OWED IS THE `OUGHT` PROPOSITION IT UTTERS.**"* The terms are immutable (`Proposition` is `frozen=True`, `carriers.py:467-470`), so renegotiation is a new utterance and a new edge — *which is what renegotiation is* |
| **reach** (`near` \| `all`) | `Record.subject_matter` | §A.8, and it is the operand RR-1 turns on |
| **a declared term** | `Record.ttl` | `(Record, ttl)` is `[MAT]`/MATTER emitting `record.expired`, and `rosters.yaml:773-782` exempts the non-terminal decrements from emitting. **This is `T-n` for nothing** — ⚠ *and it is not built: `ttl` is decremented at `harness/probes.py:1599` and in a test, and NOWHERE in `loop/`* |
| **the issuing SEAT** | the opening `Act`'s `via` | `ARCH §B.9`: `Act := (id, actor, via : SeatId?, verb, refs, payload, terms?, scene)`, and `ARCH §A.3` row 13: **`Act` persists**, resolver-side. Same argument that deleted `conferrer` |

**Nothing about the issuer is a field on the policy.** Who holds it is the `hold` Tenure; who issued it
is the opening act; what it says is a Proposition somebody uttered at a venue and can be quoted,
disputed and misreported.

### §A.7.3 · `sworn(policy)` is not a new Query — it is the shipped one

> **`sworn(policy) = members(w, policy.terms)`**

`world_q.members` (`world_q.py:200-211`) returns *"Everyone with a LIVE `commit` to this Proposition"*
and filters `t.subject in w.persons`. A policy's terms are an `OUGHT` Proposition, and `commit : Person
→ Proposition, many` (`holonic_ARCHITECTURE.md:540`) is *"faction membership"*. **A policy nobody swore
to is a scrap of parchment; a policy the burghers swore to is a charter, and the difference is a `len()`
over an existing function.** MEASURED: 86 live `commit` edges over 52 `OUGHT` Propositions in the built
world, so the edge is dense today.

Two consequences, and the second is the whole of the historical *dedizione* result:

1. **The sworn set does not end when the issuer dies.** The `hold` ends; the commits do not. So the rule
   is still uttered and still sworn-to, and **a successor who declines to re-issue it is declining people
   who are on record.**
2. **Negotiated submission is a `commit` with terms.** A territory joins a province by committing to the
   province's Proposition *on terms that keep its own nearer policies in force* — which §A.8's nearness
   rule gives for free, with nothing negotiated in code and no treaty object.

⚠ **Naming, corrected in place.** ~~`entrenchment`~~ is **not** the word for this. The tree already has
`entrenchment(h, H) = min(1, seasons_held/60)`, which measures how long a **holder** has held a thing
(collated from the superseded hearth design; cited for intent only). Two ladders for one word is
`CLAUDE.md` §4's idempotence trap and an **S** defect. The subjects differ — a holder's tenure versus a
rule's consent — so both survive under two words, and the consent quantity is **`sworn`**: an ordinary
English word in its ordinary sense.

### §A.7.4 · `Record.kind` is a free string today, and that is an `ID-4` hazard

MEASURED: `effects.py:285` defaults `Record.kind` to `d.get("kind") or "text"`, and **there is no
`record_kinds` roster** (`grep record_kinds engine/season/rosters.yaml` → nothing). So `dispensation`,
`petition` and `works` cost no roster row — **and a reader that filters `rec.kind == "dispensation"` is
matching a word, which is precisely `ID-4` (`AX:443`): *"Declare, don't route… bind a case to what it
exercises by an authored declaration, never by matching words in it"*, whose cost that line gives as
*"six recurrences in this chain."***

> ### **RULED: a `record_kinds` roster lands with the fold, or the fold ships `ID-4`'s defect.**
> One roster, `open: true`, whose members are the kinds `ARCH §A.3` row 11 already owes
> (`dispensation`, `petition`) plus `works`, with the loader refusing an unrostered kind on the
> pattern `Office.__post_init__` already uses for `remit_acts` (`carriers.py:508-512`). **This is the
> one roster this file asks for**, and it is asked for because the alternative is a string comparison
> in a resolver.

> ### **RULED: the policy is a `Record`, its possession is a `hold`, its content is an uttered
> `OUGHT`, and its seat is `Act.via`.** Cited to `ARCH §A.3` rows 11 and 13, `ARCH §B.4/B.5`, `ARCH §B.9`,
> `AX:1327-1331`, `holonic_ARCHITECTURE.md:538`, and the effect body at `effects.py:262-290`.
> **Carriers added: zero. Verbs added: zero. Rosters added: one.**

### §A.7.5 · `scope` carries two senses, and §37.3 forbids one of them — handled, not dodged

`holonic_ARCHITECTURE.md:1280-1305` (§37.1–§37.3) declares
`Dispensation := (id, issuer, proposition, scope, terms[])` and then **forbids** *"a `scope` that
enumerates places"*, on the ground that it would delete *"office-clusters with `rung? = null`, which
have no place"*. The same section states the rule this design must honour:
**"SCOPE ENUMERATES EXECUTORS, NOT PLACES"** and *"a published dispensation does not apply — it lands as
a compliance contest, per relevant Rung."*

**The two senses are already in the ratified material and they are not in conflict once separated:**

| the word | on this object | means |
|---|---|---|
| `scope` | a **Seat** (`ARCH §B.7`) | a rung — *"`scope?` (null = a cluster)"* |
| `scope` | a **published dispensation's reach** (`holonic_ARCHITECTURE.md:1290`) | the **executors** it lands on |

> ### **RULED: a policy names ONE rung or NONE, and the executor set is computed, never enumerated.**
> A policy whose issuing seat has a rung scope names that rung or a rung under it, and `in_force`'s walk
> computes who is reached. A policy issued through a **cluster** seat (`Office.rung is None` — MEASURED:
> **16 of 19 offices**) names no rung at all: its reach is the seat's `binds` set, which does not travel
> by `contain` at all. §37.3 is honoured because **the Record enumerates no places** — it names at most
> one, and the reach is a Query.
>
> ⚠ **And the cluster half has no reader**, because `binds` has none (§A.1). So `in_force` covers the
> vertical direction today and the **diagonal** one — a guild's rule reaching its members wherever they
> stand — is **unbuilt and named as unbuilt** (PART C.2, LIMIT).

## §A.8 · `in_force` — ONE WALK, AND IT IS THE WHOLE CASCADE

> **`in_force(w, rung, clause) -> policy | None`**
> *The nearest ancestor-or-self live policy conditioning `clause` — unless a farther one declares
> `reach: all`, in which case the farther one.*

```
in_force(w, r, clause):
    chain = [r, *ancestors(w, r)]                  # parent_of in a loop: world_q.py:48
    live  = [p for p in dispensations(w) if p.clause == clause
                                        and held_by_a_living_person(p)     # matter.py:73-75's rule
                                        and p.rung in chain]
    far   = the highest p in `live` declaring `reach: all`
    near  = the first p in chain order
    return far or near or None                     # ID-5: None is a REFUSAL, never a default
```

| candidate | who owns it? | verdict |
|---|---|---|
| a stored per-rung effective-policy map | — | **REFUSED.** A stored aggregate with no owner is `T-a`, and `ARCH` PART D row 8 grades *"a stored aggregate"* STRUCTURAL at the type: *"no field slot; a Query is a function; a cache is driver-local."* A map also **goes stale**: a territory changing hands changes what is in force at every rung beneath it, that same season, and a map would need a reconciliation pass |
| a per-`(clause, rung-kind)` propagation table | — | **REFUSED as scripting drift.** The walk knows nothing about kinds. *The same function carries a ducal levy to a mine and a settlement quarantine to a wharf*, and there is no row anywhere naming taxation and hearths together |
| the walk | Nobody; computed | **EXTENSION, ADOPTED.** It is the ascent `predicates.py:105-140` and `world_q.py:416-437` already make, and `contain : Rung → Rung`, one parent (`holonic_ARCHITECTURE.md:539`) |
| `None` meaning "no policy, so the default applies" | — | **REFUSED.** `ID-5` (`AX:451`): *"Refuse, don't default… an absent roster raises rather than returning empty"*, whose named cost is *"a wear table that answers `20` for an unregistered kind — plausibly and wrongly, forever"* |

**Three properties, and the third is the design.**

1. **It is a Query, so it cannot go stale** (`T-a`). Nothing is told.
2. **It knows nothing about kinds** — one function, two lines of body, no pair table.
3. **NEARNESS DECIDES AND `reach` OVERRIDES IT.** A near policy displaces a far one not because it
   outranks it but because **the near seat's people are standing there.** The far policy is not void —
   it is *unenforced*, still in force, still citable, and its issuer may strike the near one through
   `T-o` if their remit reaches. **So quiet non-compliance needs no verb: ignoring a decree is the
   nearer policy existing.** That is `T-g`'s shape — *"another person's prior act refusing yours…
   nowhere; it is not a field and not a verb"* (`AX:377`) — at the institutional scale.

### §A.8.1 · What a policy lapsing costs, and the shipped line that gives it

`matter.py:73-78` is the whole mechanism and it is **already running**:

```
holder = next((t.subject for t in w.tenures
               if t.object == rid and t.kind == "hold" and t.live), None)
if holder is None or holder not in w.persons:
    TRACE.note(f"{rid} stage {label!r} did not mature: its winder is gone ...")
    continue
```

with the reason at `:61-64`: *"a half-made copy now correctly STOPS if the copyist is jailed, which the
MATTER-driven version gets wrong: A COPY THAT FINISHES ITSELF."*

> ### **RULED: one shipped predicate — *a Record's clock runs only while a living person holds it* —
> gives three results this design would otherwise have had to invent.** (a) A works stops when its maker
> dies. (b) **A policy falls out of force when its issuer dies**, because `in_force` requires a live
> hold. (c) Therefore **the first season of a reign is spent re-issuing what the successor wants to
> keep** — act by act, out of ~5 (`holonic_ARCHITECTURE.md:896-905`, RULED), in public, each one a
> choice he can be held to, and what he lets lapse **the sworn notice, because their commits did not
> lapse with the hold.** That is the medieval *confirmatio* arriving from a liveness check.

⚠ **And the same line is a LIMIT, stated rather than smoothed.** Because maturation requires a live
`hold`, **a Record cannot change hands today**: the only producer for a `hold` on a Record is
`_eff_create_record` (`effects.py:288-289`). `carry` writes `DocketItem.matter` and no hold
(`verb_table.yaml:110`); `confer`'s predicate reads `d.get("office")` and refuses anything else
(`predicates.py:177-179`). So *"a successor inherits a half-built thing"* is **unbuilt**, and the
smallest lawful route is widening `confer`'s object domain to the one `holonic_ARCHITECTURE.md:538`
already declares — `hold : Person → Office | Rung | Record | Proposition` — which is an EXTENSION to a
ruled predicate with a named cost, not a free reading.

### §A.8.2 · `reached` — and the measurement that changes what it can be made of

The design stage had ~~`reached(w, seat, rung) ⟸ a member of the seat's `establishment` is present at
`rung` this season, by a `dispatch` or a live `contain``~~. **Struck, on two measurements.**
`Office.establishment` is **empty on all nineteen offices** and `ARCH §B.7` call 2 rejects the field;
and `_req_dispatch` (`predicates.py:291-294`) is *two lines* — `return d.get("subject") in w.persons` —
so **the dispatched person need not be an establishment member at all today.**

> ### **RULED: `reach` is a declared operand on the policy, not a computed property of a dead field.**
> A superior who wants a farther rung to read his clause declares `reach: all` and pays for it in the
> act that issues it. Where an establishment Query over `oblige` later exists (§A.1), a *second*,
> cheaper route opens — presence bought one rung at a time — and it composes with this one rather than
> replacing it. **Stating `reach` as an operand is what makes the instrument buildable before the
> Query exists**, and it is the line RR-1 turns on.

## §A.9 · THE SEVEN CLAUSES, ONTO THE CLOSED SEVEN `requires` FORMS

**Jordan's test, taken literally:** *if a policy's entire effect could be expressed as a number added to
a roll, it is not a policy.* Each clause either **reorders an existing step**, **removes or admits a row
in somebody's option set**, or **creates or destroys a date**. None has a numeric term that reaches a
pool or an obstacle.

⚠ **The split, corrected in place.** ~~Three clauses are step readers and four are `requires`
conjuncts.~~ **Two** are read only by MATTER; **one** (`sit:`) has two readers; **four** gate an act.
The number that matters is not the split but **how many of the seven `requires` forms get used, and it
is three.**

| clause | what it RECONFIGURES | read by | form used | operands bound |
|---|---|---|---|---|
| **`draw:`** | the **order** in which the rung's `stores` are drawn against by the mouths in it | MATTER (`matter.py:168-175`) | — (the grammar is RESOLVE-side and cannot reach it) | — |
| **`spend:`** | what the rung's `yield` is **committed to before anything else** — a works' next stage, the store | MATTER | — | — |
| **`sit:`** | the rung's **own dates**: whether an assembly exists here at all, how often, what quorum, what convening conditions attach | CALENDAR — it writes `Rung.dates` and `(ConveningCondition, attached)` (`write_matrix.yaml:86-92`) — **and** gates `convene` | `relation` | `actor`, `subject` |
| **`levy:`** | **what this rung owes upward** — matter kind, share, and the date it is owed at | MATTER (the share leaving `stores`) and RESOLVE | `scalar_threshold` | `subject`, `kind`, `amount`, `floor` |
| **`admit:`** | **who may take an address here** — a settlement closed to incomers, a hearth that will foster | RESOLVE, on `move` | `contain_path` | `actor`, `subject`, `from`, `to` |
| **`bear:`** | **which verbs are eligible for whom at this rung** — who may carry arms, who may `work`, who may `transfer` out of the store | RESOLVE | `relation` | `actor`, `subject`, `site` |
| **`hear:`** | **whose demand can travel up** — who may enter, who may speak, who may only be spoken for | CALENDAR (docket formation) and RESOLVE, on `petition`/`speak`; **and it narrows Q1** (§A.15) | `relation` | `actor`, `subject` |

### §A.9.1 · Why there is no eighth form and no ninth operand — and this is the section a reviewer should attack first

`rosters.yaml:1086-1122` is the constraint, quoted at the line: *"⚠ **CLOSED AT SEVEN.** A cell naming a
form outside this roster **REFUSES AT LOAD**, because an eighth form is a new thing a precondition can
ask and that is a design change, not a table edit."* And two lines that make the fit possible:

- *"⚠ **CONJUNCTION IS NOT AN EIGHTH FORM.** … a cell may be written as `all: [<form>, <form>]`"* —
  implemented at `engine/season/data/requires.py:542-543`. So a clause conjunct is `all: [<the verb's
  own cell>, <the clause's cell>]` and costs no grammar.
- *"`needs:` is the closed set of operands a cell OF THAT FORM may reference — checked at load against
  `requires_operands`"* — and `requires_operands` is closed at **eight**: `[actor, subject, from, to,
  site, kind, amount, floor]` (`rosters.yaml:1084`).

> ### **RULED: `in_force` is a Query BEHIND the predicate, never an operand — and that is what keeps the
> instrument inside the closed grammar.** A clause cell binds **only the act's own operands**; the policy
> it tests against is **found by the walk**, not named by the cell. So no cell ever needs to name a
> dispensation, and no ninth operand is coined.

⚠ **This is not a convenience, it is the one place the operand roster genuinely bites, and the tree
already registered it.** `rosters.yaml:1078-1080`: *"It is the reason `comply` and `exchange` carry
`requires_typed: none` … the first needs a DISPENSATION and the second needs the counterparty's side of a
trade, and neither has a name here. **Coining one would be filling `H-94` by keyword argument, which is
the ruling `H-94` is waiting for and not a table edit.**"* And `hole_register.yaml:763`: *"three
(`comply`, `evade / defy`, `refract`) fit form 6 and are blocked on an OPERAND the closed
`requires_operands` roster has no name for — a Dispensation — **which is `H-94`**."*

**So the honest statement about the response side, which is a LIMIT and not a gap this design opens:**
`comply`, `evade`, `defy` and `refract` — the named verbs for answering a dispensation — are blocked on
`H-94` and **this design does not route through them**. Non-compliance is the nearer policy existing
(§A.8 pt 3); evasion is `transfer`, `move` and `forge`, all of which are `own`-eligible; the demand that
travels up is `petition`. **The instrument is buildable without `H-94` closing, and a session must not
schedule `H-94` as its precondition.**

### §A.9.2 · THE UNIFORMITY RULE — what keeps a clause from being a special case

> **A clause's terms are a PREDICATE over what the loop can already read off a person at that rung:
> their marks, their live `commit` edges, their presence, their `hold`s. A clause conditioning another
> person's options MAY NOT NAME A PERSON ID. An act that would issue one is refused and emits
> `issue.refused`** (`verb_table.yaml:264`, the row's declared refusal channel).

This is `ID-17` (`AX:631-645`) enforced **by the grammar** rather than by a reader noticing:
*"A suspension is a uniform rule, and its licensed form is a band on a Query"*, and the licensed form
*"is already in the vocabulary: `T-b`. A band on a Query **changes what may be chosen and never produces
an outcome**, and it applies to whoever crosses it."* Two things fall out:

1. **Scripting drift becomes unspellable in a policy.** You cannot write *"except Björn"*.
2. **Every policy has beneficiaries and burdened, and both are computable.** A predicate partitions the
   people at a rung. **Nobody authors "the guilds resent the grain law"** — the guilds are the set the
   predicate excludes, WITNESS deposits claims about the issuing Event in the ledgers the `hear:` scope
   reaches, and each person's own weighting inside `choose` does the rest.

⚠ **The one exception, named narrowly:** a `follow:` succession clause may name a person, because naming
your heir **is** the content of the rule (§A.5). The licence covers a clause whose scope is the issuer's
own seat and no other.

## §A.10 · THE CASCADE DOWN — one step, no propagation object, and the noise is already there

The governing canon is `systems/settlements/reference/scale_hierarchy_v1.md`, **`## Status: RATIFIED —
direct Jordan ruling, 2026-07-13`** (`:3`), §3 at `:43-46`: *"Dukes govern provinces and define
provincial governance type… **A noisy cascading throughline** descends from duchy governance through to
settlements **and vice versa**"*, and `:58`: *"plausibility/pressure flows down noisily, not
deterministically."*

**There is no cascade step and no cascade object.** There is MATTER, whose ordering at each rung two
clauses condition, and one walk that finds them.

```
MATTER at rung r:
  1. yield(r) -> r.stores                                   (Rung, yield) -- "only here"
  2. spend: = in_force(w, r, 'spend:')     the declared stage draws, in the order the clause names
  3. levy:  = in_force(w, r, 'levy:')      the share that leaves r.stores, held against the date
  4. draw:  = in_force(w, r, 'draw:')      mouths fed from r.stores IN THE ORDER the clause names
  5. short  = what step 4 could not cover  -> (Person, body)
```

**The chain is lines 3, 4 and 5 at three different rungs, reached by one walk.** A Count issues a
`levy:` through his provincial seat — *of the grain a rung produces, a fifth leaves at the harvest date*
— and has named no settlement and no hearth. At each settlement, step 3 calls `in_force(w, S, 'levy:')`
and the walk ascends `contain` to the province. At each hearth beneath, the same walk finds the same
clause **unless the settlement's own seat has issued a nearer one**. Step 4 draws mouths against a
smaller store; step 5's `short` writes bodies.

> **A named woman in a named house is thinner this season because of a sentence a man she has never
> heard of uttered in a chamber she has never seen. Nobody authored her crisis; it is lines 3, 4 and 5.**

⚠ **The bottom link is not mine and is not built.** `matter.py:168-175` computes
`draw = {k: wt * len(eaters) for k, wt in weights.items()}` and the shortfall is **discarded** — there
is no `(Person, body)` write in the barrier, and the file says so at `:170-172`: *"⚠ BODIES AND TRAVEL
ARE STILL NOT BUILT."* This design **owns steps 2 and 3 and the walk**; the built world's half — what a
place does with its yield and its stores — is `02_THE_BUILT_WORLD.md`'s. **The two meet at exactly one
signature: `in_force(w, rung, clause)` returning a clause row, and the MATTER body reading it.**

### §A.10.1 · WHERE THE NOISE IS — three sources, all pre-existing, none a modifier

1. **The yield is already a draw.** `yield(H, season) = base(H) × season_factor(territory) × (3 + d10)/8.5`
   (the superseded hearth design, cited for intent only). The policy sets the **share**; the world sets
   the **base**. *A fifth of a good harvest is a tithe; a fifth of a bad one is a famine.* Nothing was
   multiplied and nothing is predictable.
2. **The fold is ordered, and `order` is a Query.** *"The second claimant on an emptied granary gets a
   different Event"* is the write-matrix's own stated reason for `emits_on_refusal`
   (`verb_table.yaml:13-14`). **Which** hearth goes short is decided at resolution by who reached the
   store first, not by the policy.
3. **Whether the far clause is read at a rung at all is another person's choice** — `reach: all` is an
   operand somebody declared in an act out of ~5, and a `dispatch` is an act out of ~5. **This is the
   strongest noise source available, because it is not a die: it is a politics.**

⚠ **THE CHECK, STATED SO IT CAN BE RUN:** no clause in §A.9 has a term that reaches a pool or an
obstacle. `levy:` names a matter kind and a share of matter; `draw:` names an order; `sit:` names a date
and a quorum. **If a later session adds a clause with a numeric term that reaches `pool` or `Ob`, this
design has been broken and that clause is the break.**

### §A.10.2 · There is no policy-effects readout — and the absence is STRUCTURAL inside `choose`, MECHANICAL on the surface

Jordan: *do NOT give the policy-setter a readout of its effects.* **This design cannot give him one.**
`short` at a hearth is a resolver-side Query, and `AX-2` (`AX:100-103`) makes *"no view of world truth
available inside a decision — not capped, not filtered: **absent**."* A policy-effects panel is a
resolver-side Query rendered to a person, which is exactly the privileged access the axiom forbids —
and `ARCH §C.11` draws the only split that holds: **the engine owes the arithmetic of what the character
already holds, and nothing else.**

⚠ **Split by grade, 2026-09-17.** ~~"the absence is structural"~~ full stop was too strong. It is
STRUCTURAL **inside `choose`** — `decision/` cannot reach a `World` and the check is by path. It is
only **MECHANICAL on the surface**, because the renderer's home does not exist yet and the scan that
would catch it has four holes (`03` §C.2, §A.1.3). §C.2 carries both rows.

What the Count has instead is a ledger containing, three seasons later, a `told_by` claim of fading
confidence — `(Claim, confidence)` decays at MATTER (`matter.py:147-153`, emitting `claim.decayed`) — and
`causes[]` is **required and non-empty** (`holonic_ARCHITECTURE.md:676-686`), so when the reckoning fires
the chain back to his own clause **exists in the data and can be shown to him at the moment somebody
tells him, not before.**

## §A.11 · HOW IT COMES BACK UP — four channels, and the fourth fires a DATE

| # | channel | speed | the object | who pays |
|---|---|---|---|---|
| 1 | **EVASION** | same season | none — `transfer` the grain before the date, `move` out, `forge` a smaller holding, or simply not work the field | the evader, one act. **The governor never sees it, and it is the commonest channel** |
| 2 | **THE GAP** | slow, arithmetic | `delivered(levy, rung, season)` versus `demanded(levy, rung)` — two Queries, neither stored | nobody. §A.13 |
| 3 | **THE PETITION** | one date | `(Petition, exists)`, `[RES]`/ACTS, emits `petition.filed` | the petitioner, **one act of ~5**; then a seat-holder's own act to carry it up |
| 4 | **THE COLLISION** | when both signals hold | a **Date** | the seat that issued the `sit:` clause that attached the condition |

**Channel 4, precisely.** The **material** signal is `short` at the rung, or `condition.band_crossed` on
the bodies of the people in it. The **interpretive** signal is a live `commit` count, among the persons
in the subtree, to a Proposition that names the policy's terms as wrong — `density(w, rung, proposition)`,
already implemented as an R-1 aggregate over descendants (`world_q.py:276-294`). **Neither alone does
anything.** A starving quiet hearth starves. A well-fed faction with a grievance talks. **When both hold
at a rung, a convening condition fires a DATE there** — and `holonic_ARCHITECTURE.md:831` is exact about
what a date is: *"Dates come due. Dockets form. Option availability is recomputed. **NOTHING IS
DECIDED.**"*

Three things make this lawful rather than a threshold producing an outcome:

- **`T-b` is honoured.** The condition fires a date; who comes and what is decided is people choosing.
- **The convening predicate reads only what §24 permits** — `holonic_ARCHITECTURE.md:836-838`: *"A
  convening predicate may read only the holder's own state, **an R-1 compute-on-demand aggregate over
  its descendants**, or the calendar."* **Both signals are R-1 aggregates over descendants.** Checked
  against the rule, not asserted against it.
- **`T-c` is honoured, and this is the part that had to be got right.** Who wound this clock? **The
  `sit:` clause did.** `(ConveningCondition, attached)` is a `[CAL, RES]` row emitting
  `condition.attached` (`write_matrix.yaml:86-92`), written by an act.

> ### **AND HERE IS THE CONSEQUENCE THAT COSTS NOTHING, BECAUSE IT IS AN ABSENCE.**
> A rung whose seat never issued a `sit:` clause **has no venue**. Its grievance has no date to fire at
> and no channel to leave by. **So a governor who convenes nothing is not safe — he has closed the
> relief valve, and the grievance leaves by the only door left: a person's own act, against his body,
> needing no venue and no verb.** A governor's cheapest act is to convene nothing; it is also the one
> that kills him. That is a genuine strategic choice with no dominant option, and it is made of two
> absences.

### §A.11.1 · Where the founding constitution comes from, since `ID-5` forbids a default

`in_force` returning `None` is a **refusal**. So a world with no policies has no dates, no levies and no
admission gates — correct, and unplayable. The answer is the one `AX-5` already licenses: *"A
world-generation roster is not a clock and is lawful"* (`AX:176-180`). **World generation authors the
founding policies as ordinary rows** — `hold` Tenures by named historical persons, on `OUGHT`
Propositions they uttered, through seats they held. So the game begins with its constitution on the
table as ordinary policy rows: every one quotable, every one strikeable, and **every one with a dead
author whose hold ended when he died — which means every one of them was re-issued by somebody living,
and the interface can name who.**

## §A.12 · A WORKS — a Record with stages, and no new verb

⚠ **Naming, corrected in place — and this ruling binds the WHOLE SUITE (unified 2026-09-17).**
~~a *work*~~ collides with the live verb `work` (`verb_table.yaml:755`, *labour at a site*), and
~~a *project*~~ is a second name for the same thing. Under `CLAUDE.md` §4 — *coin nothing a plain word
already covers*, and a term must be idempotent read cold — the multi-season construction is
**a `works`** (ordinary English for a public construction), plural-as-singular, and the verb keeps
`work`. `02` and `03` were using *work* and *project* for it and are corrected in place.

| candidate | who owns it? | verdict |
|---|---|---|
| an `undertake` / `begin_work` verb | — | **REFUSED.** `create_record` is `own`-eligible, writes `Record.exists` **and** `Record.stages` (`verb_table.yaml:166-175`), and its effect body already mints the Record and opens the maker's `hold` (`effects.py:262-290`). Beginning a works is `create_record` with a `stages` operand — **and its eligibility being `own` is correct: a person may begin their own works.** The *seat* enters through `spend:` funding it and `Record.rung` placing it, never through a privileged verb |
| a progress counter on the `Rung` | — | **REFUSED, structurally.** `Rung.__setattr__` raises on any attribute outside its eleven declared fields (`carriers.py:568-569`, `:589-595`), with the law in the exception: *"L3 — every aggregate is a function, never a field."* A counter also cannot be inherited, cannot stall visibly and cannot be destroyed by an act |
| stages maturing at MATTER | **BUILT.** `matter.py:64-109` walks every Record's stages, checks the winder is a living holder, and writes `Record.matured` **through the gate**, emitting `term.matured` with `causes=[prior]` | **CONFORMANCE — and it runs today** |
| a matter condition on maturation, plus `stage.stalled` on the else branch | this design | **EXTENSION**, and it is one conjunct and one emission inside a loop body that already exists |

```
MATTER, per Record with an unmatured stage, at its own rung:
    want = the next unmatured stage
    if in_force(w, rung, 'spend:') commits the yield to this works
       and stores(rung, want.kind) >= want.amount:
           draw it · mature the stage · emit `stage.matured`
    else:  emit `stage.stalled`
```

**Three things this buys that a progress bar does not.**

1. **THE STALL IS AN EVENT**, therefore witnessable, attributable and citable in an argument — *"the
   harbour you promised is three seasons stalled."* This is the repair `skills/ners/SKILL.md` §12
   prescribes in general form and step 4's own precedent: *"A lapse and a supersession **emit a
   witnessable event at the venue** … so this is one sentence, not a mechanism."* **A progress bar that
   simply fails to advance emits nothing and dominates by silence** (§12's gain/cost table: *say
   nothing* → *the matter dies, faster* → *no act, no event, no claim*).
2. **SABOTAGE NEEDS NO VERB.** The stage draws from `stores`. Empty the store — `transfer`, a `levy:`,
   or better, **a rival's `spend:` clause at a nearer rung committing the yield elsewhere** — and the
   works stalls *lawfully*. The saboteur never reads the works and has broken no rule.
3. **ONE EMISSION RULE, THREE USES.** `stage.stalled` when a stage's draw is short; `docket.lapsed` when
   a date passes unconvened; a stale cell on the surface. **One rule, and §A.15 finds it a second job:
   an emission becomes a Claim at WITNESS, and a claim landing about something you hold is Q2.**

⚠ **Two LIMITS, measured.** `Record.matured` is **one bool for the whole Record**
(`carriers.py:445`), so with N stages the first maturation sets a flag the others cannot distinguish
themselves from — a per-stage maturation needs a shape decision in `02`'s lane or a `stages` tuple that
carries it. And the works cannot be inherited today, for §A.8.1's reason. `skills/ners/SKILL.md` §12
step 5 is the model for saying so: *"Emitting the event makes burial visible; it does not make it
costly… the claim that may be made is **attributable**, and **punished** must be stated as a limit."*

## §A.13 · THE LEGITIMACY CHANNEL IS A BAND ON A GAP — never a field, and never `upkeep`

§0.3 struck the `upkeep` channel. The replacement is the instrument six civilizations supply
independently and the architecture already names:

> **`gap(seat, rung, season) = demanded(levy, rung) − delivered(levy, rung, season)`**, banded under
> `T-b`, **changing which options the seat-holder and his subjects see, and never producing an outcome.**

`AX:1340`, on `oblige` with `OUGHT` terms: *"**Breach is the sworn/performed gap** — a Query, banded
under `T-b` — rather than a boolean nobody authored."* And `ID-17`'s licensed form is exactly a band on a
Query (`AX:642-645`). So:

| band | what changes |
|---|---|
| delivering | nothing |
| short | the subject's option set gains `petition`; the holder's gains `dispatch` and `revoke` |
| chronically short | the subject's gains `repudiate` and `defy`; the holder's loses nothing — **and that asymmetry is the decay** |

**Nothing is stored, nothing decays on a clock, and no number is added to a roll.** A seat hollows out
because fewer of its clauses are read anywhere, which is `in_force` returning somebody else's row.

⚠ **`delivered` and `demanded` are both absent today.** The nearest existing Query is
`world_q.sovereign_fraction` (`world_q.py:297`), which measures something else. So this channel is
**EXTENSION, unbuilt, and dependent on `levy:` having a reader** — which is §A.10's step 3.

## §A.14 · LOSING A SEAT — six genres of downfall, from two declared fields and one persisted act

*Demotion severity keys to how the seat was won* — favour-derived seats face clawback and ruin,
kinship-derived seats face containment. The design stage hung that on ~~`Tenure.conferrer`~~, which is
**deleted**; it hangs instead on `conferral` × `revocation` plus the opening act, which is where
`carriers.py:48-56` says the fact already lives. `confer by <seat>` × `purview` is **ruin** — that seat
revokes, and whatever else it conferred goes with the seat. `determine` × `purview` at the body's own date
is **deposition**, delayable by not convening, which is the convener's power again. `succeed` × `none` is
**containment, not ruin** — nobody living may end it, and your hearth is still there. `confer` after an
`exchange` is **debt**: the seat is gone and the `oblige` edge is not. `confer` into a vacancy is
**usurpation** — `confer` succeeding when nobody was there to refuse. `determine` through an outside door
× `none` is **the realm's exposure**.

> ### **RULED: six genres from two declared fields and one persisted act, and no severity enum** — an enum
> is authored per office and drifts from how the seat was actually filled, where `conferral` is asserted at
> `establish` and the opening act cannot disagree with itself (`ARCH §A.3` row 13).

**And the route needing no mechanism: quiet obsolescence.** A seat whose clauses are never read — a nearer
clause always stands and nobody declared `reach: all` — is vacant in the only sense that matters, **before
any venue notices**. That is not a rule: **`in_force` never returns his row.** No `vacate_by_absence` verb,
because there is nothing to write.

## §A.15 · WHAT RAISES THE QUESTION — the gate between *resolvable* and *choosable*

**A mechanism nothing asks a person about is unplayable however well its row is written.** The producer
is `world_q.questions_for` (`world_q.py:439-550`) and it has exactly four sources, rostered at
`rosters.yaml:250-270`, whose note says *"ORDER IS SEMANTIC"*.

| | source | fires when | referent | the instruments it raises |
|---|---|---|---|---|
| **Q1** | `date_due` | a `Date` is due and unfired **and** `d["holder"] in (p.id, None)` or in `mine` (`world_q.py:474-480`) | the docket items' matters | `determine` · `convene` · a vacancy · a declared term lapsing |
| **Q2** | `claim_landed` | a claim landed since this person last deliberated **and** `c.subject == p.id or c.subject in mine` (`:491-494`) | the claim's subject | `commit` to a policy · `revoke` · **a stalled stage** · **a buried petition** |
| **Q3** | `band_crossed` | a crossing, for a person present at the site's rung (`:513-518`) | ⚠ **the VERB, not the site** — `Question(f"q:band:{what}", …)` at `:518`, where `what` is the crossing's verb. That is `H-110` (`hole_register.yaml:1533`), **the tree's finding and not this file's** | dearth reaching a body |
| **Q4** | `need` | a live `commit` whose object is an `OUGHT` Proposition — *standing, it recurs every season* (`:523-528`) | the Proposition's subject | **maintain / defend / amend a policy** · a vow · `repudiate` |

> ### **AND THE CHEAPEST RESULT IN THIS FILE: Q4 IS LIVE AND DENSE, AND A POLICY'S TERMS ARE AN `OUGHT`
> PROPOSITION.** MEASURED: 86 live `commit` edges over 52 `OUGHT` Propositions. **So everyone sworn to a
> policy is asked about it every single season, today, with nothing built.** Withholding is symmetric, so
> this is stated as loudly as the four dead things in §0.2.

### §A.15.1 · The gap, and it is Jordan's own distinction arriving as an unplayability

**Q1's and Q2's `mine` is `{t.object for t in p.tenures if t.live}` (`world_q.py:471`) — that is
HOLDINGS.** Jordan's ruling separates the three, verbatim at `rosters.yaml:696-704`: *"While a King/Queen
may have governing authority over the country, they do not necessarily have sovereign power of all
territories/provinces/duchies nor do they necessarily have all territories/provinces/duchies in their
holdings"* — and the code carries the two as separate functions, `in_holdings` (`predicates.py:60-103`)
and `under_purview` (`:105-140`).

> ### **SO THE QUESTION PRODUCER ASKS A GOVERNOR ABOUT WHAT HE OWNS AND NEVER ABOUT WHAT HE GOVERNS.**
> A Lord holding one manor and governing four settlements is asked about the manor. **Every governance
> act at a rung a seat covers but does not own is unformable, and no verb row can fix it.**

> **Q5 · `purview` — for each claim landing in the person's ledger whose subject is a rung `r`, if
> `under_purview(w, p.id, r)`, a Question with `r` as its referent.**

It is **Q2 with `under_purview` substituted for the holdings set**: one existing function — already the
single owner of *what does this person govern*, and already a disjunction over every seat they hold — one
disjunct, one roster row on an **open, ordered** roster.

| the attack | the answer |
|---|---|
| *"Q1 covers it — put a date on every governed rung"* | **Fails.** A date is an occasion somebody must have convened (`T-c`; `(Date, due_at)` is written only by `convene`, `write_matrix.yaml:93-100`), so this requires the governor to have already acted at a rung he is not being asked about. Circular |
| *"a PLACE should raise the question, not a seat"* | **Refused.** A place-raises-a-question source hands a person a question about a place independent of what they know, which is the privileged access `AX-2` forbids. Q5 fires **only on claims the person already holds** — a governor is never asked about a settlement he has heard nothing of |
| *"it will flood a King"* | **Fails, and the failure is the feature.** A King's Q5 set is every rung about which he holds a claim — and his claims are few, old and second-hand, so the set is **small and stale.** A mayor's is nearly everything under him, firsthand. **The fog is the question set**, and the same source produces the right density of business at every rung with no per-rung tuning |

**Scored honestly, over the eleven instruments a seat-holder has** — the six remit acts
`[issue, determine, confer, revoke, dispatch, convene]` (`rosters.yaml:111-119`, whose `source:` calls them
*"the CLOSED five remit acts, plus `convene`"* while the roster itself is declared `open: true` and its note
warns that *"adding a value here would close it by hardcoding"* — **and this file adds none**), plus `establish`, `petition`, `create_record` for a works, `commit`, and
`release`/`repudiate`, all `own`-eligible — **six become choosable the moment `remit:` is evaluable
person-side, and five need Q5**: `issue` at a governed rung, `revoke` there, `dispatch` (**reach is the
territory seat's whole instrument and nothing asks about it today**), `establish`+`confer`, and
`create_record` at a governed rung. **None needs a sixth source and none needs a verb.**

⚠ **A policy also conditions the question layer, and that is what makes *"a policy changes how a rung
functions"* literal.** `sit:` **writes the Dates** Q1 reads, so **a rung with no `sit:` clause asks
nobody anything.** `hear:` **conjoins Q1's person filter** — today a date with `holder: None` fires for
**everyone** (`world_q.py:477`), and under a `hear:` clause its items raise a question only for the
persons the clause admits. **So the same date asks a different set of people different things under two
regimes; the excluded are not blocked, they are not asked.** Two safeguards, both structural:

1. **`hear:` narrows Q1 only. Q2, Q3, Q4 and Q5 are untouched** — an excluded person still forms
   questions from their own claims, their own body, their own commitments and their own seats. **A regime
   can stop asking you; it cannot stop you wanting.**
2. **The exclusion is legible.** Under the uniformity rule a `hear:` clause is a predicate over marks,
   commits, presence and holds, so the surface can state *why* a matter is not on your list in the
   clause's own words — `ID-5`'s polarity at the interface: **name the reason, never silently return
   empty.**

## §A.16 · PER RUNG, HEARTH TO REALM — and one axis does most of the work

The ladder is `person < hearth < community < settlement < territory < province < duchy < realm`
(`rosters.yaml:106-109`) and the title ladder is **total** over it — Jordan, verbatim at
`rosters.yaml:741-744`: *"realm = king/queen, duchy = duke/duchess, province = count/countess, territory
= lord, settlement = mayor, community = community leader, hearth = family head, person = own autonomous
individual."* MEASURED in the built world: `hearth 211 · community 60 · person 46 · settlement 37 ·
territory 17 · duchy 3 · realm 1 · **province 0**`.

**What makes the rungs different is not scale.** As you climb, your clauses reach more people and **your
claims about them get coarser and older.** A person's knowledge of themselves is firsthand and current;
a King's knowledge of a hamlet is a second-hand cohort claim three seasons stale, *because that is what
is in his ledger*. That is `AX-2` plus the cohort rule — a cohort is a `Person` at weight > 1, never a
subclass (`carriers.py:408` raises on `Person.weight < 1`). **So the fog at the top of the ladder is
epistemically honest rather than a UI convenience**, and each seat gets a different **verb of attention**.

| rung · title | scope | won by | lost by |
|---|---|---|---|
| **person** · `Individual` | themselves | existing. `own` eligibility *returns `True` immediately* (`options.py:143-144`) | death only |
| **hearth** · `Family Head` | one household: its `stores`, its Sites, whoever is `contain`ed in it | the predecessor's `follow:` clause resolving to **exactly one** claimant at the vacancy date | death · `release` (abdication, `T-m`) · the date resolving to somebody else |
| **community** · `Community Leader` | a set of hearths inside one settlement, **or** a membership that cuts across places (`Office.rung` is optional — 16 of 19 offices are this case) | `determine` at the community's own date, with quorum over live commits — **an election, with no election mechanism** | the same date the other way; **or the sworn drifting**, leaving a seat over nobody |
| **settlement** · `Mayor` | the granary, the Sites, the gate, the court's date, every person present | `determine` (election) **or** `confer` (an appointed praefect) — **which one is a fact about that settlement, carried on `conferral`** | whichever party the basis names |
| **territory** · `Lord` | several settlements, and no granary worth the name. **Its instrument is where it sends people** | ordinarily `confer` — patronage, or purchased | `revoke` on purview alone |
| **province** · `Count` | the territories that cohere under one holder **right now** | `confer` — and the appointment is over a set that may evaporate | `revoke` from the duchy; **or the coalition dissolving, which takes the country and leaves the seat** |
| **duchy** · `Duke` | provinces, territories, settlements and every hearth beneath, **by the walk** | the predecessor's `follow:` clause. §A.5, unchanged | **not revocable — there is no living conferrer.** Only the realm's `T-o` strike (purview **and** holdings **and** strictly higher rank, `predicates.py:254-274`) or an unresolved vacancy date, which is open war |
| **realm** · `King`/`Queen` | the realm, and therefore every rung. **The widest remit and the thinnest reach per rung** | the `follow:` clause **plus an external warrant** — the one seat that cannot be filled from inside | not by revocation. By an unresolved vacancy date, by the gap hollowing the seat until nothing is read anywhere, or by a person's act |

| rung | decides (clauses) | opposed by | a season here is | drama with **no player present** |
|---|---|---|---|---|
| **person** | `bear:` `hear:` `spend:` `draw:` over themselves — *I will not carry arms; I eat after the children* | their own `need`, whose subsistence term is unbounded | binding your own future, and being trusted for it | two NPCs `commit` to one `OUGHT`; one forswears; the other now holds a firsthand claim that he did, and weights every later choice about him by it. **A friendship ends and nobody wrote it** |
| **hearth** | `draw:` (who eats first) · `spend:` · `admit:` (fostering in, turning a cousin out) · `bear:` | the members, who can `release`, `repudiate` or simply `move` — and the community above, whose `admit:` decides whether anywhere will take them | **triage with faces.** Five mouths, four portions, and the one you fed remembers | a Thin hearth's head draws against a cadet's portion; the cadet's own need drives him to the community's gate; the head's `draw:` clause is what his brother argues against at the quarter's sitting. **Cadet resentment, with no resentment stat anywhere** |
| **community** | `admit:` (who becomes one of us) · `hear:` (who may speak) · `bear:` (who may practise) · `sit:` · `spend:` | the **excluded**, who keep their `knot` edges — *an excluded member is a leak with no loyalty* — and the settlement above, whose wider clauses stand only where they reach | **the gate.** Deciding who becomes one of us, and being the reason a person's life changed | a master stakes his standing on a candidate and the bench refuses; his own claim about the bench turns hostile; his `commit` is one act from ending; if it ends, `sworn` falls and the warden's clauses become strikeable. **A rejected apprentice destabilises a guild seat three edges later** |
| **settlement** | `draw:` (**the granary in dearth — the most consequential clause in the game**) · `admit:` · `bear:` · `levy:` · `sit:` · `spend:` | the communities inside (nearer clauses) · the territory above (only where it reaches) · the people, through §A.11's four channels | **being besieged by your own arithmetic.** A dearth, a stalled works, eleven demands and a date that hears three | a praefect dies; the granary allocation date fires and allocates to nobody, because `in_force(w, S, 'draw:')` finds his dead clause's successor — **none** — and `ID-5` refuses rather than defaulting. The stock sits through a Hungry season and **nobody did anything wrong** |
| **territory** | `levy:` · `sit:` (an assize at a settlement he is not in) · `bear:`/`admit:` at territory scale — **and where to declare `reach`**, which is the real choice | the settlements' nearer clauses, which stand wherever he is not; a neighbouring Lord's `admit:` closing a road; the province above | **the fog.** You govern people you cannot see and find out you were lied to three seasons late | a claim in his ledger about a hamlet is `told_by` at fading confidence, formed two seasons ago; `(Claim, confidence)` decays at MATTER; **the picture degrades on a clock nobody winds** |
| **province** | `levy:` across territories · `sit:` (an assembly whose bench is the territory seats) · `admit:`-to-the-province | the territories, whose participation is a `commit` they may end | **waking to check whether you still have a country** | a territory's holder changes; `provinces_of` (`world_q.py:345`) recomputes; **the Count's clauses are in force and reaching nobody.** The best available portrait of a magnate in decline, and it costs nothing — the Query exists and `build_realm` builds **zero** provinces |
| **duchy** | everything a territory seat does at a wider scope, plus the one thing nobody below can do: **`establish` a sub-seat carrying a proper subset of his acts over a proper subset of his scope, then `confer` it** | the realm above; **and his own conferred governors**, who accumulate their own `sworn` | **your governors are your reach and your rivals** | a conferred governor's clauses are **nearer** than the Duke's, so where the governor stands, the governor's law is what the loop reads. *Delegation buys reach and manufactures a rival in the same act* |
| **realm** | `levy:` on duchies (who may refuse by simply being nearer) · `sit:` (Parliament) · the general-scope clause | **Parliament** — mechanically a community-shaped seat at realm scope whose bench is the seat-holders below | **issuing something true everywhere and enforced nowhere**, and choosing where to spend the one act that makes a sentence real | a King's `levy:` needs Parliament's `determine`; two of seven bench members are sworn to a counter-`OUGHT`; one `repudiate`s; quorum fails; the levy is refused. The gap widens; fewer of his clauses are read anywhere. **The realm hollows out over eight seasons with no battle and no authored event, and the blocker's name is in four hundred ledgers** |

**Where the evidence is thin, said plainly.** The historical corpus is **silent below settlement scale** —
two independent readers confirmed it with named searches (`grep -ni "hearth\|community\b"` over
`research/governance/political_hierarchy_standing.md` → **zero**). So **person, hearth and community are
derived or invented, not grounded**, and the only existing source for their numbers (appetite weights, the
2.5/1.0 cadet claim asymmetry, the five margin bands, the admission coefficient vector) is a design
document in a **superseded** tree, cited in this file for **intent only** and never as a value. §0.05:
*"A design document may not be cited as the reason a behaviour is correct."*

**And the one rung where two of Jordan's own rulings pull against each other: the province.**
`rosters.yaml:109` carries `province` as a `rung_kind` and `:760` gives it a `Count`, while the
2026-07-13 ruling implemented at `world_q.py:345-398` makes a province *"an emergent aggregation that
exists only while its constituent territories share a common faction holder"* and `build_realm` builds
**none**. **This file does not average over it.** The later ruling governs, `provinces_of` is the Query
that says *which* provinces currently cohere, and the `province` entry stays a declared kind the builder
does not instantiate — which is exactly why the Count is the one seat whose **scope** is recomputed every
season and the one seat that can outlive its own country.

---

# PART B · WHAT THIS ADDS, AND WHAT IT MAKES UNNECESSARY

**The bar.** `ID-13` (`AX:489`): *"A DECLARED FIELD MUST REACH A READER, OR IT IS NOT DECLARED"* — so an
addition must name its reader in the same row. And `ARCH` PART D row 1: a faction has a type and **no
verbs**, *"and a seat enters only through `Act.via`"* — so an addition may not be a new actor, a new
authority or a new modifier.

| added | new primitive? | its reader, named | what it makes unnecessary |
|---|---|---|---|
| **`in_force(w, rung, clause)`** | **no** — a function, owned by Nobody, stored nowhere | MATTER steps 2-4; four `requires` conjuncts; the `sit:`/`hear:` question filters | any propagation table; any stored per-rung policy map; a `governance_mode` enum (**a mode is a set of policies in force** — computable, nameable at the surface, owned by nobody) |
| **the `dispensation` `Record` kind** | **no** — `ARCH §A.3` row 11 already owes it; the effect body exists (`effects.py:262-290`) | `in_force`; `destroy_record`; `release` | `(Dispensation, exists)` writing a field of a type with no carrier; the five-family *Ledger of Consequence* (a struck policy's ended `hold` **is** precedent, readable forever) |
| **`reach: near \| all`**, one operand in `subject_matter` | **no** | `in_force`'s comparator | a `reached()` Query over a dead `establishment` field (§A.8.2) |
| **the seven clauses** | **no** — three forms of seven, `all:` conjunction already implemented (`requires.py:542`) | the steps in §A.9's table | fourteen design-only settlement verbs (Develop · Fortify · Keep Order · Hold Court · Levy · Survey · Sponsor · Treat · …), each of which built naively is **a button**: an act resolving instantly against a known number and writing a stat |
| **the conferral claim** (`remit:` person-side) | **no** — one claim predicate | `person_side_eligible` (`options.py:163-165`) | a widened `choose` signature; `Tenure.payload` as a grant carrier; the council grant fork (§A.4) |
| **`stage.stalled` · `docket.lapsed`** | **no** — two emission kinds on rows that exist | WITNESS, and therefore Q2 | a progress bar; a "neglect" counter; any claim that *witnesses can notice an absence* — **`witness` takes events, and an omission emits none** |
| **the gap band** | **no** — a band on a Query, `ID-17`'s licensed form | the option set at the burdened rung | `Office.upkeep` decay; a stored legitimacy or popular-support field; `veto_holders` |
| **Q5 `purview`** | **no** — one row on an open ordered roster, one disjunct reusing `under_purview` | `questions_for` | a place-based question source (which `AX-2` would forbid without careful gating, and the gating is the hard part) |
| **a `record_kinds` roster** | **no** — the pattern `remit_acts` already uses (`carriers.py:508-512`) | the loader | a string comparison in a resolver (`ID-4`) |
| **`sworn(policy)`** | **no** — it *is* `world_q.members` | the strike calculus; §A.11's interpretive signal | any count field on a policy |

**Carriers added: 0. Verbs added: 0. Eligibility kinds added: 0. `requires` forms added: 0. Operands
added: 0. Rosters added: 1. Emission kinds added: 2. Queries added: 3** (`in_force`, `delivered`,
`demanded`). **Objects deleted: fourteen** — `is_title` + `titles_held` + `highest_title_rank` +
`title_domain` (4 helpers — three at `predicates.py:144-164` + `:252`, and `title_domain` at `data/rosters.py:459`); `Office.establishment` as a field;
`Office.binds`'s absent reader is *filled*, not deleted; `judging_set_rule` from `Rung._DECLARED`;
`Tenure.payload` and its matrix row; `budget_office_bonus`; `Rung.transmission` (`ARCH §A.3` row 8); `veto_holders`; a co-signature
clause (**it is quorum with a different number**); an `open:` clause (`draw:` naming nobody, plus
`bear:`); a `work:` clause (a `bear:` scoped to the rung the Site sits at); `begin_work` as a verb.

### §B.1 · One deletion is a PRECONDITION of the policy instrument, not a tidy-up

`budget.py:56-57`, read at the line:

```
offices = sum(1 for t in p.tenures if t.kind == "hold" and t.live)
b = k + offices * fx.get("budget_office_bonus")
```

**It counts every live `hold`, whatever the object.** A policy is a `hold` on a Record. **So under this
design, unamended, issuing a policy buys you another act, and issuing ten buys you ten** — the sharpest
form yet of `H-92` (which records that the same line counts a possessed *book* as an office). `ARCH §A.3`
row 15 already refuses the line: *"`budget` includes an `office_bonus` → **refused.** A seat's capacity is
its establishment — more named persons, each with their own budget."*

> ### **RULED: delete `budget_office_bonus` before `issue` resolves, or the instrument pays for itself.**
> Cited to `ARCH §A.3` row 15 and `budget.py:56-57`. This also answers *"does holding three seats give you
> three times the acts?"* — **no; acts are the person's and seats give establishments**, which is the only
> reading under which a King's season differs in **kind** from a praefect's rather than in **count**.

### §B.2 · Refused and deferred, each with the clause that refuses it

| candidate | disposition | on what ground |
|---|---|---|
| `domain : RungId[]` (a set-valued seat scope) | **REFUSED** | `ARCH §B.7`'s singular `scope?`; the purview disjunction already covers the Lord; a set inverts rank (§A.1) |
| `remit : (act, scope?)[]` | **REFUSED in v1** | `ARCH §B.7`; `establish` a sub-seat instead |
| the grant on `Tenure.payload` | **REFUSED** | `ARCH §B.8` — `term?` *"Replaces payload?"* |
| the grant on `Tenure.conferrer` | **REFUSED** | deleted 2026-09-03, `carriers.py:48-56`, on `ID-2` |
| a policy as an `OUGHT` whose `Proposition.scope` is a rung | **REFUSED** | the field is live and means a role template (`populated.py:491-492`) |
| legitimacy decay on `Office.upkeep` | **REFUSED** | no reader anywhere; `ARCH §B.7` call 2 rejects the neighbouring field |
| a fifth `eligibility_kind` for policy | **REFUSED** | `options.py:137-142`: *"a fifth kind is a new way to make a verb unavailable and needs a ruling, not a table edit"* — a clause is a **conjunct** |
| an eighth `requires` form, or a ninth operand | **REFUSED** | `rosters.yaml:1092-1094` refuses at load; §A.9.1 shows none is needed |
| an `obstruct` verb; a `comply`/`ignore` pair for a policy | **REFUSED** | `T-g` (`AX:377`) — a prior act refusing yours needs no verb; the nearer clause existing **is** the non-compliance |
| a `governance_mode` / `power_base` enum | **REFUSED, and it was cut once already** | `rosters.yaml:86-92` deleted both for being unread. A mode is a bundle of clause values, and a bundle is a name for a configuration the clause table already expresses |
| a **works** inheriting automatically | **DEFERRED, and stated as unbuilt** | `matter.py:73-75` requires a living holder and nothing but `create_record` opens a `hold` on a Record (§A.8.1) |
| `Record.matured` per stage | **DEFERRED** | one bool per Record today (`carriers.py:445`) |
| the diagonal direction — a cluster seat's clause reaching its members | **DEFERRED, named** | `binds` has no reader (§A.1, §A.7.5) |

### §B.3 · E, scored LAST and as a ratio — and it FAILS if scored alone

`CLAUDE.md` §0.06: *"**E is never scored as an independent axis**: alone it is satisfiable by amputation,
so score it last, as a ratio against what N and R found."* **The ratio:** one roster, two emissions, three
Queries, one operand, one claim predicate, one question source **in**; fourteen objects **out**; zero
carriers, verbs, forms, operands and eligibility kinds added. **Vocabulary retired:** `AP`,
`FacilityTier`, Precedent/Grudge/Debt/Reputation/Leverage-as-tags, `veto_holders`, `judging_set_rule`,
`stake`, `is_title`, co-signature, `open:`, `work:`, `begin_work`, vow-as-object. **Vocabulary added:**
`policy`, `clause`, `sworn`, `in_force`, `reach`, `works`. **Legibility, the second E test —** *"allows
the player to intuit complex outcomes from simple choices"*: a policy is one sentence with two blanks
(the rung, the clause) and its consequence is the option set below it. **PASS as a ratio, under one
primitive added per primitive removed; and it would FAIL scored alone**, because the largest moves here
are deletions and an amputation always scores well on tidiness.

---

# PART C · THE THREE QUESTIONS

## §C.1 · WHO OWNS THIS? — one owner per value, and the owner is its only writer (`AX-4`, `AX:141`)

| the thing | owner | its only writer | who reads it | emitting |
|---|---|---|---|---|
| **possession** of a policy | **the issuer**, as a `hold` Tenure (`carriers.py:38-40`: *"THE ONE EDGE. Owned by its SUBJECT"*) | the opening act's effect (`effects.py:288-289`) | `in_force`'s liveness test; `release`; `destroy_record` | `tenure.opened` / `tenure.closed` |
| a policy's **terms** | the Proposition — immutable, `frozen=True` (`carriers.py:467-470`) | `utter`, once | every reader of the clause; `members()` | `proposition.uttered` |
| **which policy governs a rung** | **Nobody.** A Query | — | MATTER steps 2-4, four `requires` conjuncts, Q1's filters | — |
| `sworn(policy)` | **Nobody.** `world_q.members` over live `commit` edges | — | the strike calculus; §A.11's interpretive signal | — |
| the **issuing seat** of a policy | the opening `Act`'s `via` | the act, once | purview walks; the write gate's `T-o` clause | — |
| a seat's remit / conferral / revocation / binds | the **Seat** | `establish` | `_eligible`, `_req_confer`, `_req_revoke`, `bound_set` | `office.established` |
| **what a person believes their seat permits** | the **person**, in their own ledger (`carriers.py:382`) | WITNESS (`witness.py:175`) | `person_side_eligible` | per-person `Claim`, with `source` and `confidence` |
| the delivered/demanded gap | **Nobody.** Two Queries | — | the band that changes the option set | — |

## §C.2 · WHAT CAN CHECK THIS? — `STRUCTURAL | MECHANICAL | CONVENTION`

`ARCH` PART D's own warning applies: *"A row graded MECHANICAL or CONVENTION is here because the reader will
assume it is structural, and the assumption is the failure mode."*

| claim | grade | the construction that carries it |
|---|---|---|
| a policy cannot carry a modifier | **STRUCTURAL** | there is no numeric field on the Record a resolver reads as a bonus, and `Rung.__setattr__` raises on an undeclared attribute (`carriers.py:589-595`) |
| a clause cannot name a person | **MECHANICAL at load** | the clause cell is one of seven forms whose `needs:` is checked against `requires_operands`; a person id is not an operand of a predicate over marks/commits/presence |
| an eighth clause shape cannot ship | **MECHANICAL at load** | `rosters.yaml:1092-1094` — a cell naming an unrostered form **refuses at load** |
| a policy-effects readout cannot be built **inside `choose`** | **STRUCTURAL** | `ARCH §C.3` — `decision/` cannot import `state/`, `world_q` or `loop/`; `ARCH` PART D row 2 |
| a policy-effects readout cannot be built **on the SURFACE** | ⚠ **MECHANICAL, corrected 2026-09-17** | ~~STRUCTURAL~~ overstated it, and `03` measured why: the surface's home `engine/season/port/` **does not exist**, `ARCH §A.2`'s read-licence table has **no `port/` row**, and the `TRACE.query` scan that would catch a resolver read has **four holes** — `parent_of`, `judging_set`, `hold_force`, `occasioned_by` emit none. `ARCH §C.3` binds `decision/` by path; it does not reach a renderer. `03` §C.2, §A.1.3 |
| purview is asked of the seat and not the actor | **MECHANICAL** | `ARCH §B.7`'s own grade. **It is not structural and today it is violated in running code** (§A.2) |
| `in_force` cannot go stale | **STRUCTURAL** | it is a function; there is no field to initialise and forget |
| a policy lapses when its issuer dies | **MECHANICAL** | one liveness test, `matter.py:73-75`, and death's `until` write |
| the clause→form map is the right map | **CONVENTION** | three forms of seven, chosen; a reviewer may argue `hear:` is `own_ledger` rather than `relation` and the cost is one cell |
| Q5's position in the ordered roster | **CONVENTION** | `rosters.yaml:260-261` says *"ORDER IS SEMANTIC"* and that a budget-bounded person answers the earlier ones first. Q5 goes **after** `need`. ⚠ And the same note measures that within one source the tiebreak is a **content hash** — *"the leading source is SHARED with at least one other question in **801 of 1,068 deliberations**"* — so the roster's order decides the answer a minority of the time, and nothing declares the rest |
| **a cluster seat's clause reaching its members** | ⚠ **LIMIT, not a grade** | `binds` has no reader. The diagonal direction is unbuilt and this file does not claim it |

## §C.3 · WHOSE ACT MAKES IT HAPPEN? — every mechanism as execution

| # | what happens | whose act | step | written | emitted |
|---|---|---|---|---|---|
| 1 | the terms are said | a person's `utter` | RESOLVE | `Proposition.exists` | `proposition.uttered` |
| 2 | the policy is put in force | the holder's `issue`, `via` the seat | RESOLVE | `(Record, exists)` + `(Tenure, since)` | `dispensation.issued` · `tenure.opened` |
| 3 | the world is told, per person, differently | WITNESS's fan-out over five channels (`rosters.yaml:121-127`) | WITNESS | each holder's `ledger` | a per-person `Claim` with its own `source` and `confidence` |
| 4 | people swear to it, or to a counter-`OUGHT` | their own `commit` | RESOLVE | `(Tenure, since)` | `commitment.made` |
| 5 | the clause is read at a rung it never named | **nobody's act** — MATTER calls `in_force` | MATTER | `Rung.stores` | `stores.changed` |
| 6 | the shortfall reaches a body | **nobody's act** | MATTER | `(Person, body)` ⚠ **unbuilt** | `body.changed` · `condition.band_crossed` |
| 7 | somebody evades | their own `transfer` / `move` / `forge` | RESOLVE | `Rung.stores` · `Tenure` | `transfer.*` · `travel.moved` |
| 8 | somebody petitions | their own `petition`, one act of ~5 | RESOLVE | `(Petition, exists)` | `petition.filed` |
| 9 | the convener buries it | his `convene`, ordering the docket | CALENDAR | `(DocketItem, matter)` | **`docket.lapsed`**, `causes[]` naming his seat |
| 10 | both signals hold and a date fires | **the `sit:` clause's author wound this clock** | CALENDAR | `Date.fired` | `date.fired` — **an occasion, nothing decided** |
| 11 | a bench member blocks | his `repudiate` | RESOLVE | `Tenure.until` | `tenure.closed`, then `determine.refused` |
| 12 | the policy is struck | a superior's `revoke`, `via` a seat whose basis reaches | RESOLVE | `Tenure.until` | `tenure.closed` |
| 13 | the issuer repeals it | his own `release` (`T-m`, `own`-eligible) | RESOLVE | `Tenure.until` | `tenure.closed` |
| 14 | the issuer dies and everything he issued falls out of force | **nobody's act**; death's `until` write | MATTER | `Tenure.until` | `tenure.closed` |
| 15 | the successor re-issues what he wants to keep | **his** acts, out of ~5, in public | RESOLVE | as row 2, per policy | as row 2 |

**Nothing in rows 5 and 6 mentions taxation, farming, hearths or settlements.** Row 5 is a walk; row 6 is
arithmetic. That is the test Jordan set, and the clause being a matter share plus the carrier being
`contain` is what meets it.

## §C.4 · THE LOOPS, NAMED AND SIGNED (`ID-16`, `AX:544-549`)

*"A model in which every loop is negative CONVERGES — season 40 resembles season 30 — and convergence is
not a design goal, it is what happens when a design has no other ideas."*

| # | name | the cycle | sign | damping |
|---|---|---|---|---|
| **SP-L+1** | THE SWORN | `commit` edges → `sworn` is read by the strike calculus and the interpretive signal → the policy persists → its beneficiaries prosper → they commit | **+** | a commit is one act of ~5 · `repudiate` is always available (`T-m`) · **the issuer's death ends the hold** |
| **SP-L+2** | COMMISSION CONFIDENCE | his acts emit → WITNESS deposits claims about his remit → `person_side_eligible` reads them → his people carry his clauses further | **+** | `(Claim, confidence)` decays at MATTER (`matter.py:147-153`) · a refused act plants a contradicting claim |
| **SP-L+3** | THE FINISHED WORKS | stages mature → `work` writes `Site.condition` → band gates open verbs (`world_q.py:133-136`) → yield rises → the next stage matures faster | **+** | wear falls condition every season · stages compete with `draw:` in dearth · a finished thing is a thing to besiege |
| **SP-L−1** | THE GAP | stores → the gap Query → banded under `T-b`, it removes options → fewer acts reach the rung → the gap widens | **−** | it converges on **removal**, and removal is an event, not a fixed point |
| **SP-L−2** | PUBLICITY | he acts → hostile claims deposit → the bench's convictions are read at his next contested `determine` → a worse draw → more hostile claims | **−** | confidence decays · a `tell` chain distorts · claims are per-person, so the set is never unanimous |
| **SP-L−3** | THE SCARCITY FOLD | the ordered fold writes `stores` → the next act reads what its predecessors left → a different Event | **−** | bounded inside one season by construction |
| **SP-L−4** | WEAR | MATTER falls `Site.condition` → band gates close verbs → less yield → less to spend on repair | **−** | **SP-L+3 is the same edge with the opposite sign**, declared separately because their write steps differ |
| **SP-L−5** | REACH IS ZERO-SUM | declaring `reach: all` here spends the act that would have declared it there | **−** | the ~5 budget. **The total is fixed** |
| **SP-L−6** | THE LAPSE | a holder dies → every policy he held falls out of force → the successor re-issues out of ~5 → what he cannot reach lapses → fewer clauses in force anywhere | **−** | each re-issue is his own act, so the loop is **paid down by play** rather than by a rule |

**Four positive, five negative, none unbounded except one, named:** a rung where SP-L−1 and SP-L−4 both run hard
depopulates, and CENSUS cannot mint a person nobody's act demanded (`AX:174-184`). **So a rung can die and
stay dead.** That is recorded as intended and as the place a later tuning pass must look.
⚠ **`ID-16`'s derived check is blocked** on the `requires` grammar being typed
(`hole_register.yaml:1444`: *"one half of the cycle graph is data and the other is English"*), so this
table is an **authored claim, not a falsifiable one**, and says so.

## §C.5 · THE GRADE, AND WHAT WOULD MOVE IT

**`paper`.** `CLAUDE.md` §0.2: *done means it runs.* Nothing above executes. The first three things that
would move it, in order, each cheap and each an execution artifact:

1. **`remit:` person-side** (§A.6) — a run in which a `Candidate` with `verb == "issue"` appears in some
   person's option set and does not appear in a non-holder's. `dates: 0 → > 0` follows from it.
2. **A clause is READ** — flip one clause value, same seed, and `World.content_hash()` differs. *For every
   clause row, at least one world where flipping it changes the hash.* **A clause nothing reads cannot
   change a hash**, and this earns its existence under `CLAUDE.md` §0.1 pt 5 because its subject is the
   game.
3. **The cascade is NOISY** — the same two arms over ≥30 seeds, asserting the hearth's outcome is **not a
   function of the clause alone**: the distribution of `short` overlaps between arms while the means
   differ. **A deterministic cascade passes the reach test and fails this one; this is the row that
   distinguishes a design from a spreadsheet.**

The terminal artifact is `python -m engine.season.harness.register --requirements` moving **R-04** off
`not_met`, whose `measured:` line today reads *"54 of 143 cases are UNREPRESENTABLE… **The strategic layer
has no expression in this model**"* (`engine/season/requirements.yaml`, R-04). **Only a run may change
that sentence.**

## §C.6 · RULING REQUESTS — one, and it is the only DEPARTURE in this file

> ### **RR-1 · POLICY COLLISION: does the NEARER policy or the HIGHER rank win?**

When a hearth's `draw:` clause has a live row at the settlement and another at the province, which does
MATTER read?

| | **(a) NEAREST wins**, and a superior may declare `reach: all` to override | **(b) HIGHEST rank wins always** |
|---|---|---|
| the realm is | **feudal** — a King's law is real where he spends an act and nowhere else | **absolutist** — a decree is a decree |
| a subordinate ignores you by | **issuing his own clause**, which is a legible political act somebody can be blamed for | *nothing*; he cannot |
| negotiated submission keeping local statutes | **free** — the nearer clause is what the loop reads | needs a treaty object |
| the King's season is | choosing where to make one sentence real | issuing |
| the risk | the top of the ladder may feel powerless | the bottom of the ladder may feel scripted |

**Recommendation: (a) NEAREST, with a superior's `reach: all` override — subsidiarity by default and
centralism by act.** It makes the reach economy load-bearing, gives quiet non-compliance and negotiated
submission for nothing, keeps `T-c` satisfied (*the superior's reach is an act he took*), and matches
Jordan's own *"they do not necessarily have sovereign power of all territories."*

**Why it survives all five gates.** Not superseded — **nothing in the tree decides which policy a step
reads, because no step reads one.** Not irrelevant. No design document decides it: Jordan's revocation
ruling (`rosters.yaml:718-724`) governs *who may end a seat*, a different question. No precedent:
`under_purview` answers *may this actor act here*, not *whose rule applies*. And the architecture does not
obviously want either — both are expressible and both are one line. **The cost of being wrong is one
comparator line in `in_force` and no data migration**, said plainly because that is the honest price: the
design does not depend on the answer, **the feel of the game does**, and the two options lead to materially
different games — which is what makes this an escalation rather than an engineering call.

⚠ **THE CLOSED LIST MOVED, 2026-09-17, AND THIS IS THE STRIKE.** ~~This section listed *nine* closed
candidates, and `04` §C.5 listed a **different** nine — five in common, four unique to each, thirteen in
the union. Two lists of nine, both saying "nine", is exactly the drift a reader cannot see from inside
either file.~~ **`04` §C.5 is now the SINGLE OWNER of the closed list and carries the union of
thirteen.** The five candidates this file closes and `04` did not, now rows 10-13 there — **the council grant fork** (gate 3, `ARCH §B.8`
retires the payload), **H-91** (two conjuncts, two owners, §A.3), **`domain: RungId[]`**, **a per-act
remit scope**, and **a `governance_mode` enum** (`rosters.yaml:86-92`, cut once already for being
unread) — are now rows there with these citations. **Do not re-ask any of the thirteen; read `04` §C.5.**
**`ED-SE-0051` is queued as the suite's RR-2 and belongs to `02_THE_BUILT_WORLD.md`.**

---

# PART D · FALSIFIERS (`ID-11` — ship the falsifier with the claim)

| # | the claim | what would show it wrong |
|---|---|---|
| **SP-1** | a seat-holder can be offered a governance act from his own ledger | a run where `person_side_eligible` admits `remit:issue` for a person whose ledger carries **no** claim of the seat's remit — then the claim is not what is being read. Control: `test_no_person_can_choose_a_governance_verb_and_h71_is_why` (`test_season_shape.py:4992`) must go **red**, and if it stays green nothing changed |
| **SP-2** | a clause is a mechanism and not a field | for some clause row, **no** world in which flipping its value changes `World.content_hash()`. That clause has no reader and `ID-13` deletes it |
| **SP-3** | the cascade reaches a hearth | two arms, one seeded world, the province's `levy:` present and absent: if the settlement's `stores` and the hearth's `stores` are **equal** in both arms, the walk is not being called |
| **SP-4** | the cascade is noisy | the distribution of `short` at the hearth over ≥30 seeds being **disjoint** between arms, or the hearth's outcome being a function of the clause alone. Then it is arithmetic, not emergence |
| **SP-5** | the collision needs **both** signals | the date firing in the material-only arm **or** in the interpretive-only arm. Three arms are required; asymmetric skepticism is the failure mode here |
| **SP-6** | nearness decides and `reach` overrides it | a hearth reading the province's clause while a live settlement clause on the same clause exists and no `reach: all` is declared. ⚠ **This test is void until RR-1 is ruled**, and writing it before the ruling would pin the fork |
| **SP-7** | a policy lapses with its issuer | killing the issuer and finding `in_force` still returns his row. Conversely, if a policy survives him, `matter.py:73-75`'s liveness rule has been bypassed somewhere |
| **SP-8** | stalling and burying emit | `stage.stalled` or `docket.lapsed` absent from a log where a stage's draw was short or a date passed unconvened — or present with `causes[] == [ROOT]`, which would make them unattributable and defeat the point |
| **SP-9** | governing is choosable | `questions_for` returning a Q5 question about a rung the person **holds no claim about**. That is an oracle, not a question source, and it breaks `AX-2`. The positive half — a question about a rung he governs and does not hold — is the easier half and is not the control |
| **SP-10** | no clause reaches a pool or an obstacle | a clause row whose terms bind `amount` or `floor` **and** whose reader passes it to a contest. `levy:` binds `amount` legitimately (it is a share of matter); the falsifier is the **reader**, not the operand |
| **SP-11** | nothing added is a new primitive | a new carrier, verb, eligibility kind, `requires` form or operand appearing in the implementation of any row in PART B. The load-time refusals (`rosters.yaml:1092-1094`, `carriers.py:508-512`) are the instrument |
| **SP-12** | the instrument does not pay for itself | `budget(p)` rising when a person issues a policy. **This one is expected to FIRE against the tree as it stands** (`budget.py:56-57`), which is why §B.1 makes the deletion a precondition rather than a cleanup |
| **SP-13** | a policy's reach enumerates no places | a Record carrying a **list** of rungs, or a cluster seat's policy being found by the `contain` walk. §37.3 forbids the first; `binds` having no reader is why the second cannot even be attempted yet |
| **SP-14** | the conformance division is honest | any row this file calls CONFORMANCE that is **not** in `ARCH`, `AX` or `holonic_ARCHITECTURE.md` at the cited clause — or any row it calls EXTENSION that **is**. The check is to open the fifteen citations in §0.1's first table |

⚠ **Two falsifiers are expected to fire and are shipped anyway**, because `CLAUDE.md` §0.1 pt 3 asks for
the test's **outcome** and not for a clean sheet: **SP-12** fires against the current `budget`, and **SP-6**
cannot be written at all until RR-1 is ruled. A falsifier suite with no expected failures is a suite that
was written after the fact.

---

# APPENDIX · CITATION REPAIRS

`CLAUDE.md` §0.1 pt 3: *"A citation you have not opened is not a citation."* Every `path:line` above was
opened in this session. These are the citations I inherited from the analysis and design stages that were
**wrong**, corrected silently in the text and recorded here so the error is not re-imported.

| cited as | actually | consequence if uncorrected |
|---|---|---|
| `world.py:223` / `:197` / `:257` (`add_tenure`, `contain_ascends`, `_unowned`) | **`engine/season/state/world.py`** — there is no `engine/season/world.py` | a reader greps the wrong path and concludes the function is absent |
| `carriers.py:429` (`Record.stages`) | **`:431`**; `:429` is `subject_matter` | `subject_matter` is exactly the field the policy's operands ride on, so the two must not be confused |
| `carriers.py:557` (`Rung.sites` whitelisted) | **`:568-569`** — `_DECLARED`; `:557` is inside the docstring | a reader deletes the wrong line |
| `options.py:119-124` (the `remit:` decline) | the docstring reason is `:119-124`; the **branch** is **`:163-165`** and `presence` is **`:166-168`** | the decline is a branch, not a docstring, and the two are different edits |
| `predicates.py:190-210` (`under_purview`) | **`:105-140`**; `:144-155` is `titles_held` | the purview repair touches both, and only one of them is where the post string is matched |
| `predicates.py:246-270` (the three-term revocation conjunction) | **`:255-274`**, with the `is_title` branch at **`:252`** | — |
| `matter.py:265` (the band crossing) | **`:262`** — `if before >= floor > s.condition` | — |
| `matter.py:174` / `:145-166` (the larder) | the eaters read is **`:168`** and the draw is **`:174`**; there is no `(Person, body)` write in the barrier at all | a session schedules "the shortfall reaches the body" as an edit when it is an addition |
| `world_q.py:520` (Q3's referent) | **`:518`** | the one-line fix is aimed at the wrong line |
| `hole_register.yaml:1102` (H-71) | that line is **H-91's** `unblocks:` **quoting** H-71. H-71's own row is **`:795`** | citing a quotation as a source, which is how the "no person can form a governance verb" overstatement propagated (§0.3) |
| `holonic_ARCHITECTURE.md:829` / `:832-835` (§24) | the *"NOTHING IS DECIDED"* line is **`:831`** and the convening-predicate rule is **`:836-838`** | — |
| `ARCH:NNN` forms throughout | rewritten as **`ARCH §Letter.Number`** | `ARCH`'s line numbers have drifted twice; a section pointer survives an edit and a line number does not |

**And two claims I inherited that were not citation errors but were wrong on the merits**, both struck in
place above rather than deleted: *"no person can form a governance verb"* (§0.3 — seven of nine, not nine
of nine) and *"a seat decays through unpaid `upkeep`"* (§0.3 — the field has no reader and the
architecture rejects its neighbour). **Both were verified the wrong half of themselves:** the first by
reading the register's phrasing instead of the verb table, the second by reading a field's declaration
instead of its callers.
