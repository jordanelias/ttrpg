# 06 — ANTAGONIST FINDINGS, LANE (a): THE NPC MATRIX INTEGRATION PROPOSAL
## Status: ADVERSARIAL REVIEW (2026-08-31). Verdict **UNSOUND**.
## Relay: the critic received `04_integration_a_npc_matrix.md` and the working tree, and NOTHING else —
## not the agonist's reasoning, not its prompt, not this session's history. Read-only tools (Read,
## Grep, Glob), so its independence is structural rather than declared.
## Brief: `proposals/_session_provenance/2026-08-29-to-31/PART2_ANTAGONIST_BRIEF.md`

---

## VERDICT

**UNSOUND.** Six of the ten changes rest on a claim that direct read of the cited line contradicts —
including **both changes the proposal nominates as its strongest** (I-4, billed "should be read
first"; I-1's leg 4, billed "the strongest of the four"). One change quotes a sentence that **does not
exist anywhere in the suite**.

This is a harder verdict than either Part 1 review returned (both were SOUND-WITH-CORRECTIONS), and
it is not a close call. It is recorded here unedited.

---

## A. STRUCK — seven claims that direct read contradicts

| # | struck claim | what the tree says |
|---|---|---|
| **S-A** | I-2: `referents(act)` = marks ∪ proposition ∪ **objects touched** ∪ place — "exactly `02` §3.1's four referent kinds, no new kind" | `02_the_person.md:226-227`: `referent ∈ Person \| Faction \| Proposition \| Place`. **"Objects touched" is not a referent kind** — no stance may be held toward an object, so the strong-stance test is a **type error**. And Person and Faction, two of the actual four, are ABSENT. I-2 reads **two** of four kinds and adds a fifth non-kind. The change claiming to add no referent kind **adds one**. |
| **S-B** | I-2: `act_salience` quantifies over `JS(act)`, "which `04` §4.1 already did" | `04_hearth_and_community.md:419`: `mark_salience` counts marks **any community member** holds a stance toward — the community, not `JS(act)`. Worse: `JS(act) = {p : hears(p,act)}` (`:400`), `hears` depends on `publicity ≥ θ(p)` (`:403`), and I-2 makes `publicity` depend on `act_salience` depend on `JS(act)`. **I-2 as specified is circularly defined.** |
| **S-C** | I-5: `02` §6's COMMITMENT/EXPOSURE blocks "emit a bare `urgency` and no proposition" — the change's *entire warrant* | `02_the_person.md:468`: `needs(person) → ranked [(kind, urgency 0..5, **referent**)]`, and `:486` iterates **"for each active proposition p of f"**, reading `p` at `:488`. The need signature **carries a referent** and COMMITMENT's referent IS a proposition. **I-5's headline defect does not exist.** A real but far narrower shape mismatch survives: `(kind, urgency, referent)` vs `05:22`'s `(proposition, urgency)`. |
| **S-D** | I-5: the EXPOSURE term "reads it through I-4's `exposure_est`, which is what makes I-4 a precondition of I-5" | **Two unrelated objects sharing a name.** `02:490-492`'s EXPOSURE ranges over **dispensation claims** whose scope contains the person's address (`01:174`: *"what a dispensation's terms do to your options"*). `07:151-153`'s `exposure(edge)` is the **covert-membership scalar**. Term-matching, not concept-matching. **I-4 is not a precondition of I-5**, and I-5's compliance paragraph is built on the collision. |
| **S-E** | I-10: "`07` §4 gives it *'the cheapest named cut in the game'*" | **THE QUOTATION DOES NOT EXIST.** Grepped `cheapest` across the suite: eleven hits, none is this sentence. `07:288`'s purchased row says *"money — the only basis whose cut is symmetrically available to any rich rival, which is why it never consolidates far."* "Cheapest" belongs to the **ideological** row (`:289`, "cheapest to fire") — **wrong row, invented words.** In a document whose own opening rule is *"A claim you cannot check is a claim you should strike"* (`:17`). |
| **S-F** | I-10: "a precondition is deleted and a name changes. Object count unchanged; the transfer already existed" | `13_material_life.md:260-267`: `settle_in_full` pays `owed+arrears`, `stores(h) -= owed+arrears` — **there is no credit side**; `convey` adds `stores(to) += q`. And `:264` says `settle_in_full`'s **defining property** is that *"`04`'s judging set never fires on it — no stance deposit, no inference drawn"*, while `convey` is *"witnessable, depositing a claim naming both parties"*. I-10 **adds an act with inverted deposit semantics** and repurposes the one act §8's N-line depends on being clean. |
| **S-G** | I-9: "a clause reusing a test already ruled elsewhere, verbatim. Nothing added" | `14_office_and_upper_rungs.md:204`: `exercise(o, claimant) = Σ_{n ∈ scope(o)} compliance_share(n, terms issued by claimant)`. A hearth seat **has no remit, issues no terms, has no scope** — so transplanted verbatim, `exercise` is **identically zero for every hearth head, always**, and every seat goes vacant at every second date. Independently: `15` B-4 (`:131-135`) ruled a hearth's routine reckoning **is not a standing date** — *"if it has no claimants, it is not a standing date"* — so **the unit the test counts does not exist at that rung**. The proposal's own falsifier tests the wrong failure mode. |

---

## B. COMPLIANCE FAILURES — five, none declared

**F-1 · §2's headline is false, twice, and §3 affirmatively asserts the opposite.**
*"No change adds an object, an act, a subsystem, a field on a person, or a stored value"* — I-10 adds
an act with a new credit side and a new deposit (S-F); I-2 adds a stance referent kind (S-A). Both
would need amendment requests; neither has one. **Repairable for I-2** (drop "objects touched");
**fatal as filed for I-10.**

**F-2 · A-1 / I-6: `convener` is NOT a Person field, and typing it as one breaks the vacancy model.**
`05_up_stroke.md:197-200`: *"`convener(container)` = **the office** named by the container's charter …
It is an ordinary **office** (doc 14 §1): conferred, revocable, **vacant-able**."* Typing it
`Person — REQUIRED, NON-OPTIONAL` makes a venue **unconstructible during exactly the interval
`14:200` designs for** (*"Between the vacancy and the date, the office has no holder"*) — including
the vacancy sitting `04:122` says the vacancy **emits**.
The proposal's supporting claim that *"`14` §5's nine current rows all name one"* is **false on direct
read** of `14:413-423`: **six of nine name a ROLE** ("its Cardinal" ×4, "the guild warden", "the
chapter master"); three name a person. And **the proposal's own text already refutes it** — I-7 cost 2
states *"canon names no guild warden and two Cardinalates are unfilled."*
⚠ **This is C-3's whole mitigation. As filed, I-6 ships the regression C-3 identified.**

**F-3 · I-6 widens `Venue.container` to admit an office, undeclared.**
Against `11_code_shape.md:29-31` — *"Parent–child in the module tree means containment in the world.
**Nothing else may be a parent of anything.**"* — and `14:361`, which says an office cluster has
*"**none.** It has offices and holders, not members."* This is the containment/alignment boundary
being softened. **Repairable** (name the field something that is not `container`), but must be declared.

**F-4 · I-6 misreads B-5 as licensing a containerless venue as a TYPE.**
`15_adjudications.md:144-146` ruled the venue framing *"**presentational** … a private negotiation is
**not** a rung mechanism."* Promoting it into a `Petition` type is precisely what B-5 **declined**.

**F-5 · I-1 deletes the only person-scale discharge of §7's anti-leverage row while claiming §7 is untouched.**
`11:219` forbids *"a personal effect on a group that is not a fraction of that group"*; `02:211-213`
discharges it — *"**That split** is also the anti-leverage rule … because **what they contribute is a
verb the container can now attempt**, sized to the container."* I-1 deletes the Reach-verbs paragraph
and asserts the anti-leverage sentence stays — but **its antecedent ("that split") and its mechanism
(the verb) are the deleted text.** After I-1, capability contributes only dice and doc 02 has no
account of fractional contribution. **Repairable, must be declared.**

---

## C. WEAKENED — seven

**W-1 · I-1: all four legs, three badly. Narrow to "`14` §8 / `02` §2.3's rank-5 clause creates a 3→5 advancement gap for rank-5-only verbs" — all that survives.**
- *Leg 1 falls.* `02:140-142` asserts uniqueness over *"something a person **cannot acquire**"*. Practice rank IS acquirable. No contradiction.
- *Leg 2 falls.* `02:186-187` keys advancement on *"an attempt at a **standard** above its rank"*, not a verb above its rank. Base verbs are ungated; only the **rank-5 clause** traps a ladder, and it traps **3→5, not 0→3**.
- *Leg 3 proves too much.* `01:124` is verified verbatim but is about **faction degree** and refuses an *authored tier field*. Applied as I-1 applies it, it would equally delete the TS ≥ 30 gate that `15` A-4 **kept by ruling**.
- *Leg 4, "the strongest," is the weakest.* `10:33` is verified verbatim and the negative claim (the source fixes never used it) is **true**. But `10:27` scopes the section: *"Document 02 supplies **Capability** … **This document owns the arithmetic that turns that into a die count**."* Doc 10 **disclaims the option set**. So this is **not** "two documents that already disagree" — **it is a design change.**
- *Cost 3's mitigation is refuted by arithmetic.* `10:76` triggers hard impossibility only at `Obstacle > 2×Pool`, `Obstacle = round_half_up(R/2)`. Unpracticed Pool 4 needs `R > 16`; Pool 7 needs `R > 28` — against a stated realistic pool range of **1–14**. **"Hopeless" is not expressible without a verb gate at any plausible resistance.**

**W-2 · I-4 survives on the `rarity` precedent ALONE; its "removes a read from a decision function" argument is unsupported. Narrow to a consistency edit.**
The precedent is **verified exactly and is the best-evidenced thing in the document** — `02:169`
*"the omission was a leak"*, `:171` *"readable by **no agent**"*, `:174-175` `rarity_est(…, observer)`.
All verbatim, and `07` §1.3 genuinely has no such split.
But the leak argument fails on its citation: `07:170-171` is the closed loop of **avowal**, where
`exposure` appears as **a consumer**, not the thing consumed. And `07:101-106`'s actual requisition
formula — `obstacle = base + burden − 2·w(d) − regard/2 − conviction_bonus` — **contains no exposure
term**, and is an **obstacle (a P5 input)**, not a P4 read. **I-4 is a good change; it is not a
compliance repair.**

**W-3 · I-7's rewrite misdescribes itself; the contradiction it names is real.**
Verified: `14:562` gives Vaynard *"one turn, ten acts"* against `09:33` *"exactly one act per season"*;
and `05:198` names the ducal **proxy**, not the Duke, as convener. §8 must be rewritten.
But the re-attribution table assigns **six of seven** acts to a Duke who has one — **five are not
re-attributed, they are deleted** — and *"Ten acts, nine actors, one Duke"* is asserted with no
derivation and is **not true of its own table**.
And the replacement argument is contradicted **78 lines later in the same document**: `14:91-93`
— *"**Seat items.** An office's standing dates consume **the holder's own hours**"* — is already an
office-scaled per-holder action capacity, i.e. **a fourth quantity**. So *"three quantities and
nothing else"* is already false and **the scaled-budget reading has a foothold in I-7's own refuting
text.** Narrow to: *`14` §8 contradicts `09` §1.1 and must be rewritten — the branch is not settled by `14` §1.*

**W-4 · I-2's "B-3's ruling survives intact" is false in general.** Under I-2 an unmarked neighbour
acting on a contested proposition reaches the same multiplier, so **the marked/unmarked gap closes on
exactly the acts that matter**. B-3 is a *relative* ruling; it is **eroded, not intact**. Unstated:
`04:781` names `mark_salience` as one of exactly **two implementations of caste** — deleting the name
requires a third consequential edit the proposal does not list.

**W-5 · I-5(b)'s range ruling is incomplete, and its costs price a change it does not make.**
The four-site collision is real and verified. But (i) re-ranging to `[0,1]` also requires rewriting
`02` §6's SUBSISTENCE and STANDING formulas (`round(5×…)`, `:473`, `:482`), omitted from the edit
list; (ii) `02:492`'s EXPOSURE urgency is **unbounded** with no normaliser, so `[0,1]` is
unenforceable there; (iii) costs 1 and 5 price `loss(h)`, `worth(p)`, `subsistence_floor(p)` — which
exist **only in `proposals/2026-08-30-fixes/03_the_missing_needs.md`, not in I-5's change block and
not in #342**. *The proposal is costing machinery it declines to carry.*

**W-6 · I-2's phase claim is off by one, harmlessly.** Publicity resolves at **P5**, not P6
(`04:396`, *"computed at resolve time"*). The **compliance conclusion is unaffected** — attacked from
the other side via `04:614` and it too resolves at a standing date, not P4. Correct the phase, keep
the conclusion.

**W-7 · Three mis-citations.** "place (`09` §1.4 stratum 1)" — `09:90` stratum 1 is **Movement**;
option availability is `09` §1.2 **P0**. "the claims the person holds (`03` §4.1)" — `03:368` §4.1 is
***"The empty view"***. And I-3's *"`01`'s promise that 'correction comes from collision with the
world'"* — the phrase appears **only in `15:230` and `09:830`, not in doc 01**.

---

## D. SURVIVED ATTACK — with the specific attack that failed

**I-3 — survives every attack, and is the only change the critic could not dent. UPHOLD AS FILED.**
Three attacks tried: (1) *A-6b might be superseded* — `15:282-316`, A-6b is the **latest** row and
explicitly supersedes A-6 on the testimony half while leaving the firsthand floor standing;
(2) *doc 03 might already carry the floor* — `03:336` is still exactly the flat product with the 0.05
clamp at `:345` and **no `max`**, precisely as A-6b predicts; (3) *the quotation might be trimmed
favourably* — `15:294-296` reads *"Carrying it into 03 is outstanding work, not a settled fact"*
**verbatim**. The proposal's own honesty about I-3's limits is **accurate**.

**The struck-claim discipline — survives.** The critic searched specifically for smuggling. **No
prevalence claim, no rate**, no use of "eleven of nineteen", "the most common result", "office points
the wrong way", or D-4's 56 probes as evidence. **Every appearance of a struck item is a refusal**:
S-3 closes the Knot finding rather than opening one; S-7 **declines** the residence-admission change;
the Almud discriminator is explicitly refused; E3 is dropped. *Attack tried and failed: looking for a
struck claim re-entering as an unattributed premise inside an N-line or a cost bullet.*

**§1.3 (Goldenfurt) — survives.** Attack: find a multi-parent affordance. `01:29-30`, `:37-43` are
unambiguous — single-parent is the derivation the substrate rests on, and a second belonging is
*forced into alignment on purpose*. **A settlement with two parents is data, not a design gap.**

**§1.4 (Knot gate) — survives.** Attack: find a document that wants the gate fixed. The opposite —
`02:725` asks in terms that *"otherwise the next reader will 'fix' the gate"*, and `15` A-4 ruled it
kept. **Correctly closed under P-2.**

**§4.2 — survives, and is the document's best judgment call.** Declining the residence change on S-7
plus admitted guessed coefficients, then noting `14:51-56`'s *"binds ∈ {members-by-admission,
persons-by-presence}"* means a settlement-scale gate **would collapse the rung's identity**.

**§5.5's recorded collision — survives, exactly right.** `02:153` `rank 0–5` against `10:33`
*"Practice ranges 0–7"* — both verbatim, both line numbers exact.

**The C-4 boundary — survives.** **No validator, guard, register, freshness checker or process
document anywhere**; §5.4 refuses even the compute instrument, quoting `11:243-245` verbatim. Nothing
in `engine/` or `systems/` is touched.

**§3's ownership-table claim — survives, narrowly.** A `Venue` is its own object with a `container`
**field** (`14:399-404`), not a field on a container, so A-1 does not give a container a fourth thing.
*The critic tried to break this and could not.* (F-3 is a different rule.)

---

## E. WHAT THE PROPOSAL MISSED — five, each pointable

1. **A THIRD `exposure` already exists, and it is a stored counter doc 07 explicitly refuses.**
   `03:577-578` — `exposure += extraction_weight` / `exposure −= cover_value`, *"carried as exposure
   **on the actor**"* (`:622`) — against `07:556`, which lists *"a stored exposure counter"* **in its
   refusal table**. A live cross-document collision **on I-4's own edit surface**, arguably an
   `11:214` violation. A **fourth** sense sits at `13:215`. Renaming 07's function without touching
   this guarantees an implementer collision.
2. **The view budget K collides, and it is load-bearing on I-3's falsifier.** `03:326`: `K = 7 + Focus`
   (8..14). `09:63`: *"Top **K = 12** claims by salience per person"*, reconfirmed `:689`. I-3's
   falsifier turns on "more than K". §5.5 records the rank-range collision and **misses this one, on
   the same surface**.
3. **`satisfaction(prop)` is already undefined in the formula I-5 exists to enable.** `05:28`:
   `reach(p, prop) = max over a of E[**satisfaction(prop)** | a]`. I-5 defines `unify`/`agree` for
   `unmet` and leaves `satisfaction(prop)` undefined **and now divergent** — so as filed it delivers
   two named functions **and** the unnamed assumption its own amendment request argues against.
4. **Doc 10's pool formula has no `thread_pool` term.** I-1 reproduces `pool = attr + rank +
   thread_pool` as *"`02` §2.3, unchanged"*, but `10:30` — **the document I-1 says owns the question** —
   gives `Pool = Attribute + Practice`, no Thread term. I-1 moves the whole of difficulty onto a
   quantity whose two owners disagree about its **terms** as well as its **range**.
5. **An unstated cost of I-8 that inverts a design claim.** `14:75-85` models a remit act as **one**
   act drawing its **pool** from the establishment. I-8 makes it two. That is not "a price on an
   existing act" — it **replaces §1.2's pool-substitution model**, which is the document's stated
   answer to why office is not a modifier.

---

## F. ORCHESTRATOR'S NOTE — the recurrence that matters

**S-E is a fabricated quotation.** Not a mis-citation, not a paraphrase drifting: words in quotation
marks, attributed to a named section, that appear nowhere in the corpus.

This is the **third** instance of that exact defect class in this session, in three different
producers: my own audit cited *"the event-class parity list"*, an object that exists only in my own
audit document; my gap report asserted a prevalence figure **inside a sentence claiming
hand-verification**; and now a lane invents a quotation while its own opening rule reads *"A claim you
cannot check is a claim you should strike."*

Three independent producers, same failure, same session. That is a property of how this work is being
produced, not three accidents — and it is the strongest available argument for the relay itself.
**Every one of the three was caught by a reader that did not see the producer's reasoning, and none
was caught by the producer.**
