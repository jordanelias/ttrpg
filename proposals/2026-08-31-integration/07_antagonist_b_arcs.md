# 07 — ANTAGONIST FINDINGS, LANE (b): THE ARCS INTEGRATION PROPOSAL
## Status: ADVERSARIAL REVIEW (2026-08-31). Verdict **SOUND-WITH-CORRECTIONS**.
## Relay: the critic received `05_integration_b_arcs.md` and the working tree, and NOTHING else.
## Read-only tools (Read, Grep, Glob) — independence is structural, not declared.
## Brief: `proposals/_session_provenance/2026-08-29-to-31/PART2_ANTAGONIST_BRIEF.md`

---

## VERDICT

**SOUND-WITH-CORRECTIONS.** The citation base is **unusually clean** — the critic verified ~45
`file:line` claims verbatim and found **two** substantive misreads. The recount is correct. Both P-2
retractions are real, complete, and correctly scoped.

But three things need repair: **AR-1's central "already false" argument fails on two of its three
examples**; **I-A-1's stated compliance guard is contradicted by `10` §4.2**; and **the amendment
edits the restatement rather than the binding original.**

---

## A. STRUCK — five

**S-a · AR-1's three-example argument is a ONE-example argument.**
Claimed: `stores(h)`, `base(H_mine)` and `transport_cost` are all primary physical state at a place
and none is a stake, judging set or date.
- **`base(H_mine)` falls.** It is state on a **holding**, and `04:32` says of `holdings`: *"this is the
  hearth's **stake**, and stakes are what containers hold."* A property of a declared stake, not
  non-stake state.
- **`transport_cost` falls.** `13:179` indexes it on a **route** — an edge between a place and the sea.
  **It is not at a container at all**, so it cannot demonstrate a container holding a forbidden thing.
- **`stores(h)` survives**, on text the proposal did not cite: `04:31` justifies it on
  integral-of-history grounds while `04:32-33` separately label `holdings` and `seat` as stakes.
The amendment still stands (see §D), but *"the table is already false about three shipped objects"* is void.

**S-b · I-A-1(iv): the stated compliance guard is not the guard.**
Claimed: *"`choose` has no `World` parameter and cannot see the field at all; persons learn a site's
condition only through `witness` and `Thread-Read`."*
`10` §4.2 (`:132`): *"Before any die is drawn, the resolver exposes the same inputs a player would need
to compute the table above (both pool sizes, **the obstacle interpretation**, nothing else)"*; `10` §5
(`:143`): the exposure happens *"At the point of declaration — before `roll` is called."* Since
`thread_condition(n)` is an **obstacle term**, the player gets a **pre-commitment read of true world
state that never passed through `witness`.** The sentence is **false as filed**.
⚠ This does **not** strike I-A-1: the leak is **pre-existing and doc-10-owned** (`10` §2.2 already
computes `resistance_pool` from sitting masters' true stances). It strikes **the guarantee** — the
object's stated guard is not the guard, and the real surface is unexamined.

**S-c · I-A-7: "two petitions and a dispensation before the same date are in conflict by construction."**
`01:450-451` actually reads: *"petitions and dispensations **addressing the same proposition** before
the same date are in conflict."* **Sharing a date is not sufficient; sharing a proposition is
required.** Since I-A-7 exists to separate a guaranteed half from an unmeasured half, over-stating
the guaranteed half is the error the change was written to prevent.

**S-d · I-A-2: "the proposal's ONE strictly-shrinking edit."**
Contradicted by the proposal's own text three lines apart — I-A-6(iii) *"a deletion; one worked example
shrinks"* (`:455`); I-A-5(iv) *"Nil, and it is the smallest edit in this proposal"* (`:411`). And *"the
vocabulary goes down by one term"* has **no stated basis**: three banned names leave, two structural
terms arrive. **A number with no instrument**, in a document bound by a §D that exists to stop exactly that.

**S-e · The recount's own citation is wrong.** exp-8's TRANSFORMED verdict is at
`03_arcs_41_55_and_emergent.md:389`, not `:391` (mid-paragraph). **The recount is right; its citation is
not — in the one paragraph whose entire warrant is that citations were checked by hand.**

---

## B. COMPLIANCE FAILURES — one repairable, one declared-not-violated

**CF-1 · AR-1 amends the RESTATEMENT and not the BINDING ORIGINAL. Repairable, and consequential.**
`11` §3's table is not the only home of the rule. `01_substrate.md:490-491`, inside §6 *What is
refused*, carries: *"**Container-level memory, ledgers, or councils that think.** Containers hold
stakes, judging sets and dates. **Persons hold everything else.**"* And `00_INDEX.md:28` declares `01`
*"the spine — binding on everything else."*
The proposal cites `01` §6 **twice** and never cites this bullet. **If AR-1 is granted as scoped, the
binding spine still refuses the object while the adjudication document permits it.**
It also narrows the "omission, not refusal" framing: `09:808` refuses *"a morale bar, unrest meter, or
**cohesion field stored on a container**"* — a **shape** refusal — and `01:490` refuses container state
beyond three kinds outright. **What the tree lacks is a refusal naming the Thread; a general refusal
covering the object's shape exists.** Omission survives **narrowly and on less than claimed.**

**CF-2 · R-1/R-2 are never tested — declared, not charged.**
`11:116-127`'s R-1 ends *"Compute-on-demand, never push, never store."* Read as a general clause it
forbids the object; read in context (R-1 quantifies over **aggregates over descendants**) it does not,
and `stores(h)` is the precedent. **The critic takes the latter.** But I-A-1's compliance argument runs
against §3 and §7 only and **never reaches R-1/R-2**, which the brief names.

**Checked and CLEARED:** the three signatures are untouched — `choose` acquires no `World`, `resolve`
no `Person`, `witness` unchanged and nothing accepts `[Person]` with one `Event`. All thirteen §7 rows
clear. §8's *"What must NOT be built"* is honoured — **no validator, guard, register or process
document**, and I-A-7 and §1.2 explicitly refuse the two places one would naturally be built.

---

## C. WEAKENED — seven

**W-1 · AR-1 → narrow to one example, plus one the proposal missed.** `04:34`'s `pointer` — *"three
separable transfer lists (name / seat / holdings)"* — is also not a stake, judging set or date.
**Two objects, not three.** (`banked_claims` is self-declared a standing date, so it is covered.)

**W-2 · AR-1's B-1/B-4 argument is contradicted by I-A-1's own mechanism.** B-1 and B-4 are quoted
**verbatim and correctly**. But AR-1 argues the object fails B-1 because *"it has no claimants"*, while
I-A-1(ii) routes `alter` collisions through `09:102`'s *"Conflicts route to the substrate's
`contest(container, prize, claimants)`"* — **two practitioners altering one site produce claimants by
construction.** Narrow to the limb that holds: it fails B-1 on **"allocated at standing dates."** The
conclusion survives on that limb.

**W-3 · AR-2a asks the WRONG CLAUSE for the ruling it wants.** The §8.3 quote and `13` §5's two fuses
are all verified. But §8.3 governs **clock-driven** quantities, and **AR-2b argues at length that the
proposed object is act-driven and needs no exemption from it.** So AR-2a requests a ruling on a clause
it has itself shown does not bind the object. **Its real content is a housing decision** — narrow to
*"file it in `13` beside the larder and the seam"*, and drop §8.3 as the instrument.

**W-4 · I-A-2 does not strictly shrink, and its falsifier is ONE-SIDED.** The edit converts two
categorical name-bans into a conditional structural test — **a stored revolt gauge read only inside
`resolve` and published as a band with no trigger point PASSES the promoted test** while being banned
by name today. And the offered falsifier tests only whether the test is too **strict**; **nothing tests
whether it is too permissive.** *That is the one-sided-scale defect S-12 indicts, reproduced by the
proposal that cites S-12.* Narrow to: keep the promoted test **in addition to** the named bans, and add
a permissiveness arm.

**W-5 · I-A-6's independence holds narrowly; its evidence is ONE arc, and P-2 is applied asymmetrically.**
All three lane-2 observations verified verbatim, and they genuinely **do not** trace to C-2's confound.
But **only arc 19 supports one-act** — arc 21 is a stated *cost* of it and the debate arcs are neutral
by the lane's own words — so **the base for part (a) is n=1, on an arc selected because its content is
"you can only save one faction"**, which could not have come out the other way. And lane 2 opens
*"The contradiction is real (D-2)"* and cites D-3 and D-6, so **it demonstrably read the gap report** —
the proposal applies exactly this P-2 discount to L-2 and **does not apply it here.** Narrow to: *the
contradiction is inherited, not rediscovered; the resolution rests on one arc.*

**W-6 · I-A-6(b) is a magnitude with no instrument, proposed for insertion into a design document.**
The *"factor-of-five tempo"* derives from arithmetic over one arc under a roster assumption lane 2
itself flags as decisive. **This is the one place the proposal comes closest to the count-to-rate
conversion §D forbids.** Narrow to a named uncertainty **with no factor in it.**

**W-7 · I-A-4's cost is over-stated for half its subject.** `09:684` lists containment nodes as
*"3 duchies · 14 provinces · 35 settlements **+ Himmelenger + Schoenland** · districts"* — **Schoenland
IS a containment node.** The ruling names "Altonia and Schoenland"; the cost applies to one. **The
price is smaller than stated** — which helps the change, and shows the cost paragraph was not checked.

---

## D. SURVIVED ATTACK — with the specific attack that failed

**I-A-1's three reuse claims — ALL THREE verified; no hidden mechanism found.**
`09:100` *"Every act declares `touches: {(object, mode)}`, mode ∈ `{read, alter, exclude}`"* verbatim —
`alter` exists unextended. `03:531` `**Thread-Read**(person|place|object)` — **the `place` argument is
already in the signature** and already yields *"prior configurations at a place"*; genuinely a getter
with no field. *Attack tried:* find a verb, phase, resolver or threshold silently required. `alter`
exists; P5 exists and is *"the only writing phase"*; `obstacle` is single-owner and takes any
`resistance_pool`; `13` §1's *"bands published, trigger points never"* applies unchanged. **None found.
The E-line holds.**

**The N-line survives a RULE-1 sweep WIDER than the proposal's own.** The critic additionally tested
`forestall` (fails — `supply()` is explicitly non-persistent, *"Nothing here is stored; it recomputes
each season"*), `granary_stock` (allocated by a named office-holder at a standing date — the shape the
proposal correctly rejects), and `season_factor(territory)` (weather). **Nothing in the suite is
simultaneously shared, place-held, persistent and act-degraded. The N-line stands.**

**The recount — re-derived from the SOURCE, not from the proposal's summary.** Both lists yield seven;
they differ by exactly one member; exp-8 is TRANSFORMED at `:389` and its prerequisite is a **leg of a
TRANSFORMED unit**; the tally at `:23` and the synthesis totals (1+2+7 = 10) are **unaffected**.
**The recount is correct and its preference for the second list is justified.** Only the line number is wrong.

**The ten-unit work-list composes.** 1 + 2 + 7 = 10. **Every blocker quote spot-checked is verbatim.**

**I-A-5, the dangling pointer — the falsifier RUN, not accepted.** `02:4` defers to *"doc 04 (Thread)"*;
`00_INDEX` names 04 *The Hearth and the Community*. **Two of three deferrals mispoint, exactly as
claimed.** The critic then **grepped the whole suite for `Thread` — 36 occurrences across 10 files —
and read every non-cited cluster.** `07` §7's `ts_gain` is entirely per-person from the holder's own
ledger. **No Thread-operations owner exists anywhere in the suite.** I-A-5 survives **as an
unconditional repair independent of I-A-1**, as it claims.

**Both P-2 retractions are real, complete and correctly scoped.** *Attack tried:* find a residual
sentence still trading on the retracted independence. **None found in either.** And the place-scoping
argument retains one genuinely non-seeded arc-side datum: `03:160-162`, *"MS is global, so the old arc
unravelled him peninsula-wide the season the band changed … more causal, more local"* — lane 3's own
note on arc 41, from no brief.

**I-A-3's falsifier — RUN against the tree.** *Attack tried:* find a mechanism that forces a position
with no person deciding and is not P1 metabolism. Checked `05` §8.1's re-arm (lowers a price, forces
nothing), `09` §7's confidence decay (a cost), `05` §3.2's lapse (*"Lapse is not an act by anybody — it
is the date passing"* — ends a petition, does not resolve the matter), `13` §5's fuses (change inputs,
not positions), `09` §12 (refusals only). **Nothing forces. The stated limit is TRUE.**

**I-A-4's tiebreak.** *Attack tried:* find a suite path by which an actorless pressure is expressible.
`06:33` types `ProhibitionTerm` under a Dispensation whose issuer is a person holding office; `14:220`
makes conferral `admit()`; `09` §6 refuses a leader as a modifier; the minting list and generation rule
verified verbatim. **The nearest expressible thing is a claim with a faction referent — which the
proposal itself names and correctly bounds to "Altonia is massing", not "Altonia acts". No second path
found.**

---

## E. WHAT THE PROPOSAL MISSED — seven

1. **`01:490-491` — the SAME ownership rule, in the binding spine, uncited.** CF-1. The single most
   consequential omission: the amendment does not reach the document `00_INDEX` calls binding on
   everything else.
2. **`04:29-36` — the state table AR-1 needed.** §1.1 is where the suite adjudicates what is a stake.
   It **kills** `base(H_mine)` as an example and **supplies** the replacement (`pointer`).
3. **`13` §5's two slow fuses have NO PHASE TO RUN IN.** `09:56-58` restricts P1 SETTLE to metabolism
   and enumerates it: larders, production, wounds, ageing, travellers. **Ore depletion and silt accrual
   are in no phase**, yet both say *"every season"*. **The precedent AR-2a leans on is itself unwired** —
   the same defect class as the `doc 04` pointer, one document over, and directly load-bearing on AR-2a.
4. **`10` §4.2 / `10:180` — the pre-roll obstacle exposure.** S-b. The surface a compliance argument for
   a new obstacle term must clear, and the one the guarantee talks past.
5. **`09:684` — Schoenland is a containment node.** W-7.
6. **Citation ambiguity.** Bare `03:NNN` denotes **two different documents** in this proposal —
   `03_knowledge_telling_investigation.md` and `03_arcs_41_55_and_emergent.md`. In a document whose
   method is checkable citation, that costs the next reader a grep.
7. **An unstated cost.** The E-line says *"one stored field"*, but the object also puts a **new term
   into `resistance_pool` for every Thread act at every site**, and `10` §2's obstacle is computed per
   attempt. Small, and unstated — **the field is not the whole of the object.**
