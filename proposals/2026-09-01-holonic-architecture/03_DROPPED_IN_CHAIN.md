# 03 · WHAT THE CHAIN DROPPED — #337 → #352

## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.** Nothing here runs.
## Scope: **PR #337 → #352 only** (`00_ADJUDICATION.md` §0).

---

## §1 · WHAT THIS IS, AND WHAT COUNTS AS "DROPPED"

A thing is **dropped** if it was decided, ruled, endorsed or measured somewhere in #337–#352, and a
**later document in the chain** either contradicts it without saying so, restates the question as
open, omits it while restating the surrounding material, or promises to carry it and does not.

**The test that does the work is the fourth field: name the later file and section that restates the
surrounding material WITHOUT the thing.** A suspicion that cannot name that is not a finding, and is
discarded. Twenty-four survived it; sixteen more were checked and rejected (§5).

> **The chain names this failure at its own head.** #351's body: *"the suite reproduces at its own
> HEAD the failure five lanes documented, that **a ruling and a landed edit are different events**"* —
> the `opening_set` overturn landed in `08` and `15` and **not** in `07` §3.2. **That case is item 1
> below, still true at `a1b0a4e`.**

### §1.1 Verification, stated plainly

The sweep was produced by a read-only Fable pass over the chain. **Four items were re-verified by hand
in this session before being reported, chosen as the ones this proposal would act on. The rest are
reported at sweep strength and are marked as such** — they name a file and section, so each is cheap
to check, and none should be treated as measured until someone does.

| # | verified how | result |
|---|---|---|
| **1** | `grep opening_set` across `07`, `08`, `15` | **CONFIRMED.** `08:74` types it `Candidate[]` and says *"**NOT `Act[]`**"*; `15:250` row 13 overturns *"`opening_set` returns Acts"*; **`07:137` still reads `opening_set : (Person, View) -> Act[]`** |
| **14** | `grep -c 'Event :='` across all nineteen #350 files | **CONFIRMED. Zero.** The head defines no `Event` record anywhere |
| **17** | `grep -c 'contract tree\|ED-IN-0200'` across all nineteen #350 files | **CONFIRMED. Zero** |
| **20** | `grep -c 'memberless\|banner nobody'` in #351's `04_UNIFIED_SHAPE.md` | **CONFIRMED. Zero** — the finding is in #351's archive-recovery half and not in its unified shape |

### §1.2 One scope distinction that changes what an item obliges

Several items are in-chain documents dropping something whose *subject* is a pre-#337 document
(items 17, 18, 23, 24, 25). **The drop is in-chain and the finding stands** — one chain document said
it, a later one lost it. **But under `00` §0 a pre-#337 document is not authority**, so re-landing is
not automatic: **these are questions the chain must answer on merit, not debts it owes.** They are
marked ⚖ below.

---

## §2 · THE FIVE THAT BEAR ON THIS PROPOSAL

Ranked by what they change in `00`–`02`.

### D-14 · The `Event` record, and its mapping onto the Key — **never written, and dropped from the open list** ✔verified

#345 `01` §7 (7) carried as open: *"`Event`'s record beyond id and degree band — resolved in this
suite by composing Event onto the executing `Key`, but **the field mapping is unwritten**."* #350
`02` §10 restates that open list — seven of eight items carried or closed — **and omits this one.**
**The head defines no `Event :=` anywhere.** #351's tracer then invented one, with `causes=[]`, which
is the `A4` finding.

> **What it changes here:** `00` §C3 says the key system is the head's Event log and gives the
> holonic rule for what crosses a rung boundary. **That rule is stated over an object with no
> record.** This is the single cheapest thing in the whole census and the one this proposal most
> needs: **write `Event :=` and map it field-by-field onto the Key shape.** One record, one table.

### D-17 · The contract-tree discharge and its licensed guard — **dropped by the head** ✔verified ⚖

#345 `04` §3 specified it — *"one validated parent, three leaves … generated … blocking `--check`
round-trip"* — and `07` §5 licensed that round-trip as **one of exactly two guards**. #350's
twelve-step execution path, which otherwise restates #345 `07` §3, **has no contract-tree step**, and
its guard list restates the licensed set with only a generic "exporter round-trip for any new
authored registry."

> **What it changes here:** `01_THE_CONTRACT_HIERARCHY.md` is a **re-land plus a level set**, and it
> should say so louder than it does. The transport was already specified and already licensed; what
> went missing is a step and a guard row. ⚖ Its pre-#337 subject is not authority, but **#345's spec
> is in-chain and needs no external warrant.**

### D-20 · A memberless faction still holds territory — **found and not carried, inside #351** ✔verified

#351's archive-recovery half: *"a `Proposition` may be a `hold` subject and is never destroyed, so a
dissolved faction leaves territory held by a banner nobody carries, **uncontestable because the holder
can never appear at a venue**"* — against `03_OWNERSHIP.md` §1.1's *"Nothing is lost … a faction
collapses when people leave, with no dissolution mechanism."* **#351's own `04_UNIFIED_SHAPE.md` §4.1
restates the carriers and the seven Tenure kinds with no rule.**

> ⚠ **THIS IS A DIRECT COUNTER-CASE TO `00` §C4 AND IT IS ADMITTED THERE RATHER THAN ARGUED AWAY.**
> C4 rests on *"an edge is not a ratchet: an edge can be destroyed, and `Tenure.until` is what makes
> its destruction a fact."* **The Proposition-held `hold` is the exception: nothing destroys it,
> because its subject cannot die.** The `commit` count still falls, so C4's monotonicity argument
> survives for aggregation — **but "a faction collapses when people leave" is false while the `hold`
> edge outlives the faction.** The proposed rule: a Proposition-held `hold` becomes **contestable at
> the Rung's venue when `presence(w, prop, rung) = 0`**, or `until` is written when the last `commit`
> reaches zero — declared as a seam, the way `(Tenure, until)` already is.

### D-13 · Five of #345's blocking gaps fell out of the head's open register; one came back as new

**G-19, the empty judging set**, is the one that matters here: it re-surfaces at #351 `04` §6.2 as
*"`judging_set_rule` is a named `Rung` field that no document specifies"* **without citing G-19**.
Also dropped: **G-01** (the question `q`'s producer — *"which is why 'evict lowest salience' was
uncomputable"*), **G-18** (establishment size), **G-27/28** (the exchange form).

> **What it changes here:** `00` §7 already names `judging_set_rule` as the hole in the upward half —
> **T5's *"filtered at a rung"* runs straight through it.** The census shows it has been open for two
> generations under two names, which is worth more than the fact that it is open. **G-01 is the
> sharper one for the holonic story**: a `question` nobody produces means `assemble(person, question)`
> and `view(person, question)` are both unsatisfiable, and those are how anything reaches a decider.

### D-19 · `disclosure:` as a schema column — neither adopted nor refused

#338's U-1 and #339's E-2 proposed a per-field disclosure block; #340 recorded it as one of the
things that **survived** into v2. #345 `01` §6 and #350 `02` §9's exclusion tables do not list it, so
it was neither carried nor cut — the principle survives as prose only.

> **What it changes here:** `01` §2.2's argument for `phase:` is that a per-module axis makes a
> whole class of question a row check. **A per-field `disclosure:` grade is the identical shape,
> beside the `social:` column that already exists** — and #352's forward doctrine §3 ruling
> (*"declare, don't route"*) is exactly the argument for it. **If `phase:` is right, this is right,
> and `01` should carry both or neither.**

---

## §3 · THE REST OF THE LIVE CENSUS

Sweep strength. Each names its source and the later section that lost it; none re-verified here.

| # | dropped | lost where | type | cost |
|---|---|---|---|---|
| **1** ✔ | `opening_set -> Act[]` overturned in `08`/`15`, still `Act[]` in `07` | `07` §3.2:137 | contradicted-silently | **one token** |
| **2** | R-11's ruling sentence still grants Momentum for aligned action; the paragraph beneath and `02` §5.5.2 delete the grant | `15`:144 | contradicted-silently | four words |
| **3** | `coin` enters as a MatterKind example, taking one side of a live fork the source refused to choose | `02` §2.2.2:205 | contradicted-silently | one line |
| **4** | the drain-topology prerequisite — *"prerequisite work for step 9, not a footnote to it"* | `13` §3/§4, zero "drain" | promised-and-not-carried | one row |
| **5** | the per-issue stance store the carrier must **absorb**, *"not sit beside"* | `13` §4 step 12 | promised-and-not-carried | one row |
| **6** | the **Exposure** collision (X-4) — two objects, one name; the head uses both senses | `04` §4; `02` §4.8–4.9 | omitted-in-restatement | rename + row |
| **7** | `transfer`'s `stores ≥ amount` precondition (mints from a negative larder) and restoration's mirrored form | `08` §3.2; `05` §2 | omitted-in-restatement | two lines |
| **8** | of four sized "small edits", E4 vanished and E3 landed as a duplication (`found` **and** `found_hearth`) | `07` §5.3; `08` §3.2 | omitted / contradicted | three lines |
| **9** | petition **multiplicity** — *"a person may put it to several offices"*, one of four tested enlargements | `02` §7.1; `06` §8 | omitted-in-restatement | sentence + row |
| **10** | petition **supersession** — *"relocation, not decay"*; only lapse-by-date survives | `02` §7.1; `08` §3.2 | omitted-in-restatement | act + clause |
| **11** | gating dormant-grievance clearance on the holder's own ledger — *"one clause, and it removes a broadcast"* | `06` §8 r15; `04` CALENDAR | omitted-in-restatement | one clause |
| **12** | `season_factor`'s *"likely answered by `11_world_events`"* — a read two generations promised; the file has no such thing | `02` §10 (9) | promised-and-not-carried | one line |
| **15** | `Coherence` — read in two places, owned in none, its fork gone from both escalation registers | `02` §2.1; `03` §1; `15` §3 | omitted twice | two rows + a ruling |
| **16** | the twelve named faults + stasis ladder, called *"the best-specified object in the document"* | `02` §7.2, §8 | praised-then-never-referenced | citation + row |
| **18** ⚖ | the ratified per-settlement Local Actor counts (~45–50 across 36) behind the person loader | `13` step 3; `04` CENSUS | omitted-in-restatement | one row |
| **21** | **per-Conviction scarring** — #351's own *"best idea in the archive"* and its own change C2 — absent from #351's change list. P4 blocks **7 arcs** | #351 `04` §4 | promised-and-not-carried (same PR) | row + a step choice |
| **22** | Jordan's two long-arc trajectories → twelve transitions, *"eleven of twelve work"*, **never became cases** | `12_TESTS`; #351 `cases/` | praised-then-never-referenced | twelve cases |
| **23** ⚖ | the hook grammar — *"we can script narrative hooks and sequences so long as we don't script entire arcs"* — against the head's threshold refusal | `06` §7; `05` §5.2 | contradicted-silently | paragraph or escalation |
| **24** ⚖ | the 3/4/5 scene-action model, against *"one act, universally"*; closed as *"reached independently by three routes"*, none of them it | `02` §8.1; `07` §4; `15` §3 | contradicted-silently | **already in flight** |
| **25** ⚖ | `Recall` as the tenth attribute — recorded by precedent, then *"this shape does not name the tenth"* | `02` §2.1.4; `15` §3 | contradicted-silently | verify, then a row |
| **26** | J-1 (*may a false belief determine an action outright?*) — answered by the architecture, never closed in any register | `15` §3 | answered-silently | one closing row |
| **27** | the Parliament Total Victory rider fork + its promised oracle run — unmentioned after #338 | nothing after #338 | promised-and-not-carried | one run or one sentence |

> **Item 22 deserves separate weight: those are the only Jordan-supplied acceptance cases in the whole
> range.** Two trajectories, decomposed into twelve transitions, one of them called *"the design at its
> very best"* — and **#351 built a case runner and ran neither.** Under `CLAUDE.md` §0.2 they are the
> nearest thing the chain has to an execution artifact for the whole shape.

---

## §4 · THE PATTERN, AND THE ONE CHEAP THING THAT WOULD STOP IT

**Fourteen of the twenty-four are `omitted-in-restatement` or `promised-and-not-carried`, and every one
of those was lost at a section that restates its neighbours.** That is the signature: **a document
rewriting a list loses the row it did not personally re-derive.**

> **The chain already knows the mechanism and wrote it down:** *"a ruling delivered alongside another,
> and satisfied by the tree's current state, is the one that gets silently dropped — nobody decides
> against it, it simply never becomes a work item because nothing wrote it down."*

**The cheap fix is the one `01_THE_CONTRACT_HIERARCHY.md` §4 already proposes for a different reason:
every open item becomes a ROW with a `grade:`, not a paragraph.** #350 `02` §10 is a register whose own
heading says *"stated so no later document can cite this one as though these were closed"* — **and five
of #345's gaps fell out of it anyway**, because a prose register is re-typed rather than inherited.
**Rows are inherited. Paragraphs are re-typed, and re-typing is where the losses are.**

---

## §5 · CHECKED AND REJECTED — recorded because rejections are the evidence the census is not noise

Sixteen candidates failed the fourth test. The most instructive:

- **"Damage removes an option"** — carried under another name: `verbs(w, site, c) = { v : condition(c) >= floor(v) }` **is** option removal by band. **A rename, not an absence** — and this is the repo's costliest error class, so it is listed first.
- **The `if R <= 1: return 0` fast path** — replaced and declared: *"an uncontested attempt routes to a GATE, never to an `Ob = 0` roll"*, RULED.
- **`capacity(date)` / `seat_items`** — `02` §8.1 deletes `seat_items` *"deliberately, not dropped"*. A stated resolution.
- **`03_knowledge_telling_investigation.md`** — never cited by filename, but `02` §5.3's fourteen forms, four sources and six acts match it. **Carried without attribution is not dropped.**
- **The playable-seat list** — closed, then explicitly re-scoped. Not silent.
- **Governance ripple substrate / Π homeostat** — **stale by ruling**: a homeostat on a social pressure is what Law 3 refuses.
- **`InsurgencyRecord.L` writer** — a stored `L` is what Law 3 forbids. Stale, not dropped.
- **#338's U-2/U-3/U-4** — carried as Law 3 + one act; `Person.ledger` + establishment; the seam's stated purpose.

Also noted once and deliberately not pursued: the CI aggregate still treats `cancelled` as failure,
deferred "to its own PR" by three separate PRs. **Apparatus, not design** — under `CLAUDE.md` §0.1
point 5 the disposition is fix in place or drop, and neither is this proposal's to do.

---

## §6 · TWO PROVENANCE DIVERGENCES THAT MAKE RULINGS UNFINDABLE

Neither is a dropped ruling; both are the class of defect that produces one.

- **#338's body says *"IDs allocated: none"* while its diff allocates `ED-IN-0201`.**
- **#343's body says #342 *"was closed unmerged"*; #342 merged as `57739a2`.**

**A ruling recorded only in a PR body that misstates the tree is a ruling nobody will find by grep** —
which is the mechanism §4 describes, one layer up.

---

## §7 · FALSIFIERS

| claim | what would prove it wrong |
|---|---|
| the four ✔ items | re-run the greps in §1.1. Each is one command and names its file |
| the twenty unverified items | open the named section. **An item whose named section does carry the thing is a false positive and should be struck here** — that is the intended failure mode of a sweep reported at sweep strength |
| §4 · the pattern is loss-at-restatement | an item lost at a section that does **not** restate its neighbours. Fourteen of twenty-four fit; the counter-examples are the contradicted-silently rows, which are a different mechanism |
| §4 · rows are inherited, paragraphs re-typed | a row-structured register in the chain that lost an entry the same way `02` §10 lost five |
| D-20 · the Proposition-held `hold` is C4's only exception | a second edge kind whose subject cannot be destroyed. `Proposition` is the only immutable identity-bearing kind in `02` §3, which is what makes this bounded |

**Standing weakness.** **Twenty of twenty-four items are reported at the strength of a single read-only
pass**, with no second lane and no execution. The census's own construction is the thing it warns
about: **a list re-typed from another document.** §1.1 marks what was checked; everything else is a
lead with an address, not a measurement.
