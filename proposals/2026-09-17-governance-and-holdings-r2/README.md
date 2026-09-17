# Governance at every rung, and the built world — ROUND TWO

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` (cross-cutting), with `SE` for `04`. Ids: **`ED-IN-0233`**, **`ED-IN-0234`**, **`ED-IN-0235`**, **`ED-SE-0053`**.
## Grade under `CLAUDE.md` §0.2: **`paper`** for every document. **Nothing in this suite has run.** `05` §A.4 item 1 is the first thing that would.
## Supersedes: **`../2026-09-17-governance-and-holdings/`** — round one, left standing with banners and struck where overturned. Ledger rows appended for `ED-IN-0231`, `ED-IN-0232` and `ED-SE-0052`.
## ⚠ **Written FROM round one's own terminal NERS verdict, not over it.** `../2026-09-17-governance-and-holdings/AUDIT_VERDICT.md` is the input to this suite. The limit it graded hardest — that the policy instrument was a **DEPARTURE** from `holonic_ARCHITECTURE.md` §37.3 rather than an extension of it — is why `02` exists at all. ⚠ **The map of its nine limits to this suite's answers is below, and it is not nine for nine.**

---

> **Jordan, on the remit:** *"I do not want this work to be constrained by existing work. I want the
> best possible design ideas and concepts, and we can modify code accordingly."* · *"Your remit is to
> develop the most NERS-positive work possible."*
>
> **And the sentence this round is built on, which arrived after round one was written:** *"the player
> must have the sanctity of their choices/actions/decisions preserved in terms of the contents of
> those choices/actions/decisions themselves — the worldly churn is in how those contents are received
> and acted upon by others."*
>
> Round one put the churn in the CONTENTS. That is the single error from which most of its other
> findings follow, and it is filed here as **`RR-P`**, a candidate seventh axiom.

## The five questions, and the one-line answers

| Q | answer | owner |
|---|---|---|
| **1 · how a decision reaches a person** | **Two question sources, not four-plus-one.** `claim_landed` over one Query `reach(w, p)`, plus `need`. Dates and crossings become claims like everything else; `date_due` and `band_crossed` are deleted — **measured at 0 questions each after a populated season.** Purview is a TERM of reach, never a fifth source. | `01` |
| **2 · how authority descends** | **Two channels, both people-borne, and no broadcast.** THE WRIT: a `Record` of kind `dispensation`, minted by `issue`, physically carried and handed by `give` — verbatim or not at all. THE WORD: a `told_by` claim spread by `tell`, lossy at `Partial`. One deposit rule makes a held document a held belief. **Compliance is the executor's own act, and MATTER reads no policy.** | `02` |
| **3 · how matter reaches people** | **It does not move to them; they draw up the ladder.** One Query `nearest_store(w, rung, kind)`; the shortfall crosses the gate into `Person.body`; bodies cross band floors as sites do; death at 0 reuses the kill cascade. **Matter still moves only by `transfer`.** | `04` |
| **4 · how a seat becomes fillable** | **Bases are VALUES on the seat, read by two predicates, and the content is an authored table.** `conferral ∈ {confer, determine, succeed}` — a set already ratified **twice**, at `ARCH §B.7` and `AX` ID-14. `revocation ∈ {purview, holdings, none}` as conjunct sets. The `is_title` branch and the title helpers go; `confer` also mints a `commission` Record, so the holder BELIEVES his remit. | `03` |
| **5 · how the object count comes down** | **Net −17 engine objects: 39 removed against 22 added.** ⚠ **Not the −20 the plan projected — three WORSE, and `05` says exactly what the plan miscounted.** Vocabulary 24 terms in against 17 out. Round one's eight proposed Queries are withdrawn. | `05` |

## The documents

| file | owns | id |
|---|---|---|
| **`01_ATTENTION_AND_REACH.md`** | Q1 — `reach`, `place_of`, the fold of two dead sources, and why purview is a term | `IN` · `ED-IN-0233` |
| **`02_THE_WRIT_AND_THE_WORD.md`** | Q2 — the two channels, and **`RR-P`**, the principle | `IN` · `ED-IN-0234` |
| **`03_SEATS_AND_CONTENT.md`** | Q4 — the bases as values, the two predicates, and the 29-seat table. Carries **`RR-B`** | `IN` · `ED-IN-0235` |
| **`04_MATTER_AND_WORKS.md`** | Q3 plus works and founding — the larder ladder, the body write, the `works` Record | `SE` · `ED-SE-0053` |
| **`05_LEDGER_AND_BUILD.md`** | Q5 — the deletion ledger, the engine changes per file, the build order, the ruling ledger, the NERS pre-commitment | `IN` · `ED-IN-0233` (shared with `01`) |
| **`probe_reach_questions.py`** | the instrument behind `01` §0.2(d)'s `561 → 1632`. Re-runnable, gates nothing, dies with this suite | — |

## Conventions, binding on all five

- **`ARCH`** = `architecture/meta/04_CODE_ARCHITECTURE.md`, cited **`§Letter.Number`** and never by line — its line numbers have drifted twice. **`AX`** = `architecture/meta/01_AXIOMS.md`. **`holonic`** = `architecture/holonic_ARCHITECTURE.md`, cited `holonic §NN.N`.
- A bare **`01`–`05`** means a file in THIS directory, never the architecture's sections of those numbers.
- `path:line` is used for `engine/` files only, and every one was **opened at that line** before it was written. Each file's appendix lists the citations its author found wrong in their own sources and repaired — `03` repaired 26, `05` repaired 19.
- Falsifier prefixes are per file: `AR-n` · `WW-n` · `SC-n` · `MW-n` · `LB-n`.
- The multi-season construction is **a `works`** — never *a work*, never *a project*.
- Corrections are **struck and kept** in place: `~~old~~ → new`. Nothing is silently replaced.

## What is HELD BACK — which is everything, and this is the loud call-out `CLAUDE.md` §2 requires

**`ED-1094` makes a merge ratify a PR's `PROPOSED` contents by default. That default is refused here, in full.** Merging this PR ratifies **nothing**: no `## Status:` line flips, no ledger `status` or `needs_jordan` field changes, and `CURRENT.md` is untouched. Every document is `paper` and every design claim is a proposal.

**Six ruling requests reach Jordan** — `05` §C.4 is their single ledger, and each ran `CLAUDE.md` §0's five-step gate with the answering step named:

| | what it asks | why it cannot be taken by step 5 |
|---|---|---|
| **`RR-P`** | Jordan's principle as a candidate **`AX-7`**: the act is inviolate; the churn is in reception | axiom-shaped, would bind every subsystem, and no design document states it |
| **`RR-A`** | fold the four response verb rows (`comply`, `evade / defy`, `refract`, `dispatch`) | `ED-IN-0210` **ruled against** *"no response verb"* on 2026-09-15; step 5 may not overwrite a ruling. **Cost measured: one live verb and four dead rows** |
| **`RR-B`** | **eight** sentences in RATIFIED `architecture/` that this suite makes false — not the four the plan expected | `architecture/` is ratified (`ED-IN-0204`); one limb (`03`'s containment-derived rank) is a **game** change |
| **`RR-C`** | sequencing: the content work goes AHEAD of positions 3–7 of the ratified 27-position order | the program's ORDER is the ratified scope; step 5 cannot re-order it |
| **`RR-2`** | *(from round one, untouched)* `ED-SE-0051` — matter only, or matter plus hearth capacity? | the two arms are materially different games. **Gates no build item** |
| **`RR-3`** | *(from round one, untouched)* the zoom-trigger table | **still the weakest of the six**, as `03_THE_SURFACE.md` itself measures |

**`RR-1` is CLOSED** at step 2 — *irrelevant*, not answered. With no `in_force` walk and no place-keyed clause there is no site at which two policies collide; two writs naming one executor are two content claims in one ledger, and `agreement` already scores told-against-own. **The collision is the executor's, and his act resolves it.**

## Round one's nine limits, mapped — and it is not nine for nine

`../2026-09-17-governance-and-holdings/AUDIT_VERDICT.md` is the input to this suite, so the map is
owed rather than optional. **Three are answered by name; four die with the mechanism that raised them;
two are carried forward as live limits on THIS suite.** The distinction matters: a limit that dies
with its subject is not a limit that was reasoned away.

| # | round one's limit | disposition |
|---|---|---|
| **1** | the policy instrument's MATTER half is a **DEPARTURE** from `holonic §37.3`, not an extension | **ANSWERED BY NAME.** `02` §A and §B: no broadcast, no state write at a place, no place-enumerating scope, no assumed delivery. It is the reason `02` exists |
| **2** | the headline path **does not construct** — `build_realm` builds `province 0` and no `contain` chain names one | **ANSWERED, and hardened.** `01` §0.2 reproduces it; `05` adds pre-flight refusal **S15** — a seat whose `rung` names no Rung has zero purview *silently*, so item 10 must assert every seat's `rung` is in `w.rungs` |
| **3** | *"the share leaves `r.stores` at MATTER"* contradicts round one's own RULED line | **DIES WITH ITS SUBJECT.** MATTER reads no policy at all in round two, and matter still moves only by `transfer`. The correction was already struck into round one during unification |
| **4** | **`sit:` cannot create a date** — `(Date, due_at)` is `[RES]`, written only by `convene` | **DIES WITH ITS SUBJECT.** The seven place-keyed cells go, `sit:` among them (`02`'s own supersession line names it), and round one's channel 4 is withdrawn |
| **5** | **`draw: None` starves**, so the founding-policy inventory was mandatory | **DIES WITH ITS SUBJECT, and the real hunger is re-measured.** No `draw:` clause exists to be `None`. `04` answers the underlying fact instead: **211 hearths starve beside 4,810 units** |
| **6** | the uniformity rule **has no checker**, and there are **no free predicates** | **DIES WITH ITS SUBJECT.** There is no clause roster to be uniform about. ⚠ The finding's *substance* survives as a constraint on `02`'s terms-as-operands, and `05` §B.4 refuses a guard over it on `CLAUDE.md` §0.1 pt 5 grounds — *"if a column matters, give it a reader"* |
| **7** | **`ceiling = matured/declared`** reads a per-stage maturation `Record.matured: bool` cannot carry | **ANSWERED BY NAME.** `02` §C keeps `matured` whole-record and does not read a per-stage value off it |
| **8** | the conferral claim's deposit is a **NEW deposit rule**, not a ride on the existing channel | **CONFIRMED AGAINST ITSELF, twice.** `02` and `03` both verify it independently — the deposit's predicate is the **event kind** — and neither claims the free ride |
| **9** | same-`(rung, clause)` collision is an **unwritten branch** | **CLOSED BY CONSTRUCTION, which is also why `RR-1` closes.** `02` §C: there is no `(rung, clause)` key, so there is no branch to write |

**⚠ The two the suite carries forward as ITS limits, not round one's:** the `wear` × `restore` × yield
equilibrium is still **not player-computable** (round one `02` §B.4's own FINDING, kept), and the
E-OVERHEAD verdict is answered with a number that is **worse than projected** — net **−17**, not −20.

## What round one contributes, in one list — so nothing is re-argued

| kept | where it now lives |
|---|---|
| the **seat model**, `ARCH §B.7` entire — every clause opened and verified | `03`, verbatim, struck-and-kept where changed |
| **Surface Law `L-1..L-3`**, the **cell law** (HELD / STALE / UNHELD / CONTRADICTED), the **causation worksheet** | `../2026-09-17-governance-and-holdings/03_THE_SURFACE.md`, which **STANDS** |
| the **fabric and address ontology**, the `hold`-guard argument, `Rung.envelope` | `04`, by pointer, not re-argued |
| **a `works`** as the noun for the multi-season construction | suite-wide, from round one `01` §A.12 |
| the **purview defect**, re-measured from two further directions | `03` §A.2 and `01` §0.2(e) |
| the withdrawals of `fort_level`, `facility_tier`, `governance_modes`, `power_bases` | not re-added; the export check is blocking |

## What a reader should distrust, said here rather than discovered later

1. **Nothing has run.** `05` §A.4 item 1 is a single `@effect_for("commit")` body and it is the whole difference between this suite and an executable one. Two probes and one ladder inside `05` DID execute — they measure the **tree**, not the design, and they are labelled EXECUTED where they appear.
2. **Three of `03`'s ten falsifiers are RED on the current tree, deliberately.** They are written to fail now and pass when the content lands; a falsifier that cannot fail is `CLAUDE.md` §0.1 pt 2's absent assertion.
3. **`01`'s headline table was repaired after its own instrument was written.** The `561 → 1632` figure reproduces exactly (2.91×), but the six rows had been computed on three different readings of `place_of`, and the effect was attributed to the wrong limb. Both are struck and corrected in `01` §0.2(d). **This is what a claim looks like before it has an instrument**, and it is left visible on purpose.
4. **`01`'s purview limb is INERT until `03` lands.** 16 of 19 offices have `Office.rung is None`, so the limb is the empty set for 16 of 19 seat-holders. `01` says so in its own §0.2(e) rather than letting a reader find it.
5. **The build order reverses one edge against the plan.** Item 10 depends on item 16, because `in_holdings` is **False for every person over every rung** — all 16 rung-holds are faction-subject.
