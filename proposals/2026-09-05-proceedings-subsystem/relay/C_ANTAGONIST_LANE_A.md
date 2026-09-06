> ## RELAY STAGE C · ANTAGONIST, LANE A — `opus`, structurally read-only
> ## Status: **PROPOSED (2026-09-06). NOTHING HERE RATIFIES ON MERGE.**
>
> **Lane: the two theses and Positions 1–7.** Dispatched with the agonist's OUTPUT and not its
> reasoning, against the working tree. Ran as `valoria-critic`, whose agent definition grants
> `Read, Grep, Glob` and no write tool — so this critic **could not** have edited what it audited,
> whatever its prompt said (`CLAUDE.md` §10). It did not see stage D and stage D did not see it.
>
> **Three of its attacks FAILED and are reported as failures** — the rope-as-`requires` attack on
> P7, P5's own falsifier run by hand, and the engine plumbing of P4. That is the property that makes
> its kills worth believing; a critic that never reports a survival is manufacturing.
>
> ⭐ **Its Item 1 is the most valuable finding of the whole exercise, and it is a finding against
> THIS DIRECTORY rather than against the agonist.** It refused to take `14_THE_WORLD_IN_THE_ROOM.md`
> on trust, read the code, and found the measurement stale. **Verified by hand in adjudication before
> being acted on** — see `17_PLAYABILITY.md` §C.2 and §H.1.
>
> ⚠ **It over-claims in one direction and the adjudication says where** (§C.2): *"a deposited claim
> demonstrably changed what a person did"* is true of one recorded firing that the surrounding code
> comment is in the act of excluding, and the write half remains a declared-open item.

---

## ITEM 1 · THE TWO THESES (`AGONIST_CONVERSIONS.md:15-39`) · **BROKEN**

**THE ATTACK I RAN.** I refused to take `14_THE_WORLD_IN_THE_ROOM.md:185` on trust and read `belief_contradicts` in the tracer the agonist says it read.

`/home/user/ttrpg/proposals/2026-09-01-season-loop-tests/tracer/shape.py:3835-3843`:

> `⚠ W-A: IT ASKS THE VERB'S OWN TYPED CELL, NOT A ROSTER. **The previous version filtered on `predicate in PERSON_PREDICATES and value is False`** ... `H-116` then measured the consequence: over 4,800 deposited claims the two vocabularies were DISJOINT ... **The predicate is DERIVED from the form now**`

and the body, `shape.py:3860-3861`:
```python
return evaluate(row.requires_typed, LedgerReader(p.ledger),
                binding_of(p.id, operands)).value is False
```

**WHAT IT SHOWED.** Thesis B's "break" — *"`belief_contradicts` fires only on `predicate ∈ PERSON_PREDICATES ∧ value is False` … **0 of 4,800 claims can fire**"* (`AGONIST_CONVERSIONS.md:36-38`) — is a **verbatim description of the superseded implementation**. It is the `H-116` measurement of the code `W-A` deleted. Corroborating evidence that the loop is live, all in the same file:
- `shape.py:724-725` — `observed` is attached to every Event; *"that is `W-B` (`H-122`), **landed 2026-09-04**"*.
- `shape.py:1847` — `observation_deposit_mode="actor"` is the **live default**, not the control.
- `shape.py:5887-5891` — reads are attached *"TO SUCCESS AND REFUSAL ALIKE … it is **the only read whose value can make `belief_contradicts` fire**"*.
- `shape.py:1265-1274` — a **measured firing**, seed 0, NPC-088, at mode `actor`, 2026-09-04: *"The person then **declines `tell` for a season** on a belief the fold would have admitted."*

A deposited claim demonstrably changed what a person did. The agonist's asserted severance is stale by two days at the time of writing, and `06_RESOLUTION.md:185-189` names this exact defect class (*"a fact about the tree stated as timeless, which is `G.3.3`'s named defect"*) in the very directory under review.

This is not a local error. It is load-bearing on: the Thesis B "break" itself; Position 8's create-half (`:511-513`); the residue (`:955-957`, *"the sixth route … is measured-severed at `H-72`"*); and the refusals table (`:891`, *"the provocation's payoff | `H-72`, **measured** | nothing here"*). The honest state is narrower and better: the reader shipped, the write side is a **rostered arm** (`rosters.yaml:337` — `none / actor / total`), and depositing into *another* person's ledger is `total` — a data value, not a lane-blocking theorem.

**Thesis A, separately.** *"Thirteen of twenty binaries reach it [the obstacle]"* (`:20`) is contradicted by the agonist's own cost lines: **six of its thirteen positions add zero obstacle terms** — P4 (`:282`), P6 (`:397`), P7 (`:461`), P11 (`:693`), P12 (`:745`), P13 (`:799-800`). The obstacle is not "the one lawful sink"; it takes 6 of 13. And the thesis's own headline case is a category it does not name: the genre binary is neither a row value nor a `requires` conjunct — see Item 2.

**SEVERITY: fatal** for Thesis B (a false claim about the tree, cited to a line that repeats it, propagating to four downstream sites and to the document's stated ceiling on what is buildable); **material** for Thesis A (a countable overstatement, falsified by the document's own tables).

---

## ITEM 2 · POSITION 1 — aptness (`:47-114`) · **BROKEN**

**THE ATTACK I RAN.** Three separate probes.

**(a) The premise.** P1 (i) asserts *"today the Candidate never forms and the turn buys nothing"*. `13_ADVERSARIAL.md:85`, in the design's own PART C — *what survived, with the attack that failed*:

> `speak`'s `requires` does not gate Candidate formation on world truth | attacked as an `AX-2` breach; **the attack fails against the design's actual behaviour** — Candidates form from the interior and `requires` is checked at RESOLVE, so a player who *believes* there is an occasion forms it and gets a **witnessed refusal**. **Only the sentence was wrong; the design was right**

Confirmed in code: `shape.py:5863-5866` returns `ev(row.emits_on_refusal …)` — a refusal **emits**. `04_VERBS.md:78` gives `speak` `emits_on_refusal: ["speech.unheard"]`.

**(b) The delivery channel is self-defeating.** P1 (ii) puts the aptness reading in `Event.observed` "with no schema touched". `shape.py:5843-5861`:
```python
# `W-B`. THE READS THIS ACT'S PRECONDITION MADE, ON EVERY EVENT THE ACT EMITS.
verdict = Verdict(UNKNOWN, ())
...
    return [Event(..., degree=_degree, observed=verdict.observed) for k in kinds]
```
`verdict` is rebound **only** by the `requires` block (`shape.py:5869-5893`). `Event.observed` carries **precondition reads and nothing else**. P1's whole move is to *delete the conjunct from `requires`* — which removes the read from `verdict.observed` and therefore from `Event.observed`. To deliver it anyway needs a new channel from the seam's obstacle composition into the fold's Event — a carrier under another name, which the "+0 fields, +0 Event kinds" line does not count.

**(c) The conjunct being deleted does not exist.** `04_VERBS.md:62-66` — `speak`'s `requires_typed` is a **single clause** (`form: existence, of: subject, kind: DocketItem`), no `all:`. The genre rule lives only in prose at `04_VERBS.md:157`. Under `CLAUDE.md` §0.05 that is reference, not mechanism. So "ONE CONJUNCT REMOVED" (`:56`, `:91`) is a prose edit with zero schema effect, and the position is a **net +1 obstacle term and +2 magnitudes** with nothing subtracted.

**(d) A false cite.** `:67` — `# rung_kinds is ORDERED`. `rosters.yaml:89-92`:
```yaml
rung_kinds:
  source: "#353 §10 — the containment ladder. `contain : Rung → Rung`, one parent"
  open: true
  values: [person, hearth, community, settlement, territory, province, duchy, realm]
```
That is the **territorial containment ladder**, not the stasis ladder (`procedural → conjecture → definition → quality`, `05_PROCEDURE.md:80`), and it carries **no `ordered:` key** — compare `strata` (`rosters.yaml:128`) and `question_sources` (`:176`), which declare it. The agonist's own declared input has the correct cite: `relay/A_FABLE_INTERROGATION.md:229` says *"the rung roster is ordered (`03:228-229`)"*, and `03_PARAMETERS.md:228` is `LADDER := ( id, rungs: [ (name, concedes, track) ] ) -- ORDERED`. The agonist **downgraded a correct citation from its input into an incorrect one by matching on the word "rung"**.

**WHAT IT SHOWED.** P1 buys strictly *less* than the design already has. Today a genre-mismatched speech is a witnessed Event fanned out to every ledger in the room — which `04_VERBS.md:167` argues is the mechanism (*"An inapt move refused is an Event, fanned out to everyone present … The player is **witnessed committing a category error** … and it is how they learn"*), and which P1 never mentions. Under P1, mode `actor` (`rosters.yaml:337`, forced by `P-05` at `10_LOOPS_AND_GAPS.md:51`) delivers the reading **to the speaker alone** and the room gets a band. P1 replaces a public reading with a private one, calls that "`AX-2` paying rather than being paid" (`:85`), and charges +1 term and +2 magnitudes for it.

**SEVERITY: fatal.** A false statement of current behaviour, refuted in the reviewed directory's own survival table; a delivery mechanism the position's own edit destroys; a miscited roster; and a net information loss. It is the agonist's rank-1 position and the anchor of the "build these three first" commit (`:867`).

---

## ITEM 3 · POSITION 2 — finding strength (`:118-188`) · **BROKEN**

**THE ATTACK I RAN.** I traced the value source to the fields it names.

P2 (ii) 1: *"A bench told the matter firsthand and recently finds **strongly**; a bench that has it at third hand through `chronicle` finds **weakly**"*, from `band(max{c.confidence : c.subject == matter})`.

`14_THE_WORLD_IN_THE_ROOM.md:166`: `chronicle → told_by, **at the teller's confidence**`. The channel does not attenuate confidence. The agonist **quotes this correctly in its own Position 11** (`:670`: *"chronicle → whoever is later told, **at the TELLER'S confidence**, possibly false"*) and then contradicts it here. The discriminator the design supplies is `Claim.source` (`rosters.yaml:119` — `[firsthand, told_by, inferred, firsthand_via_knot]`), which P2 does not read.

Consequently P2's falsifier (`:172-178`) is **circular**: it *plants* "one holding a `firsthand` claim at high confidence, one holding the same claim `told_by` at low", i.e. it hand-installs the correlation the mechanism was supposed to produce. It tests that `band(max(·))` is a function.

Second probe: *"`Claim.confidence` (`shape.py:2157`) **gains its first reader outside eviction**"* (`:138`). `shape.py:1303-1309`, `LedgerReader.read`:
```python
if best is None or (c.when, c.confidence) > (best.when, best.confidence):
```
`confidence` is already a live reader in the ledger's most-recent-then-most-confident tiebreak. The claimed `ID-13` closure is not one.

Third: `max` over a **capped, eviction-ranked** ledger (`14:165`, eviction on `(confidence, recency)`) evicts the *low*-confidence claims, so `max` is near-invariant — a bench holding one claim and a bench holding fifty return the same band.

Miscite: P2 (ii) 1 cites `04_VERBS.md:172` for `writes: ["Tenure.degree"] # ⚠ UNCHANGED from the live row`. That text is at `04_VERBS.md:195`; line 172 is unrelated prose about `register fit`.

**WHAT IT SHOWED.** The *hole* P2 identifies is real and well found — `determine` declares no `contests:` (`04_VERBS.md:186-198`; confirmed by `13_ADVERSARIAL.md:80`, *"grep `contests:` → **one row**"*), so it writes a degree it cannot compute. But the filler is wrong: it reads the wrong field, its fiction is refuted by the design's own channel table, and its falsifier cannot fail. It is also pre-registered by the agonist's declared input at `relay/A_FABLE_INTERROGATION.md:235` (B-7: *"`Tenure.degree` on the finding is written … and unread … **Cost: 0 — a reader for a dead field**"*).

**SEVERITY: material.** The diagnosis survives; the mechanism and its instrument both fail. Not fatal because the position is separable — the appeal-obstacle reader could be rebuilt on `Claim.source` without touching anything else.

---

## ITEM 4 · POSITION 3 — Partial costs (`:192-247`) · **WOUNDED**

**THE ATTACK I RAN.** I tried to run its falsifier on paper.

`:236-237` requires *"the third press's obstacle is strictly greater than the first's, **by exactly `2 × HELD_STEP`**"*. But `06_RESOLUTION.md:214-217` composes `reception` **from the hearers' own claims about the speaker**, and `06_RESOLUTION.md:368-373` states that every speech deposits regardless of band: *"WITNESS fans it out to everyone present **regardless of how it went**; each deposits claims into their own ledger."* After two Partials every hearer holds two more claims about the speaker, so the third obstacle differs by `2×HELD_STEP + Δreception`. **The equality can never hold in any run in which WITNESS fires — i.e. every run.** The falsifier is unsatisfiable, so nothing could show the position wrong.

Second probe: `write_matrix.yaml:47-50` lists `Person.stance` among the *"ELEVEN RES-stepped rows with no producing verb"*, and `:58-60`: *"**NO VERB IN THE 32-ROW TABLE WRITES ANY `Person` INTERIOR FIELD.** That is tier-0 `H-62`, and it means **every interior consequence is inert**."* So the "band that costs" costs nothing at the write site; the working half is the obstacle term alone.

Third: the `AX-4` closure P3 banks as a free extra (*"⚠ AND `writes` MUST NAME WHOSE STANCE, WHICH THE PROPOSAL DOES NOT"*, `:218-222`) is pre-registered in the agonist's own declared input, in the same words — `relay/A_FABLE_INTERROGATION.md:239` (B-11): *"⚠ **Whose `Person.stance` is written must be settled first (the actor's, or the row breaches `AX-4`)**"*. And B-13 (`:241`) already prices the position: *"a `partials so far in this run` fold is the same construction as `proofs told so far` … **Cost: one injected term**"*.

**WHAT IT SHOWED.** The construction is lawful and the `T-d` caveat is accurate — `shape.py:5858-5859` does set `Event.subject` to `a.actor`, exactly as `13_ADVERSARIAL.md:53` records. What fails is the instrument and half the payload. WOUNDED, not broken.

**SEVERITY: material.** An unfalsifiable-as-stated falsifier is disqualifying for a position whose whole defence is *"inject, declare, sweep"*; the inert-write half means the gradient is one term, not a term plus a write.

---

## ITEM 5 · POSITION 4 — advantage bought with an `oblige` (`:251-309`) · **BROKEN**

**THE ATTACK I RAN.** I priced the bargain.

**(a) The stated cost is false.** `:286`: *"The real cost is **a turn in the order, which is the scarcest thing in the room**."* `05_PROCEDURE.md:67-70`:

> ⚠ **THERE IS NO TURN LIMIT AND THERE MUST NOT BE.** A round cap would be a clock nobody wound (`AX-5`) … **The bound is the attendees' willingness to keep spending, and the term somebody declared.**

Turns inside a proceeding are **unbounded**, and the term half is unbuilt (`Tenure` has no `term`, `shape.py:2066-2091`, `P-04`). With `M_MAX = 1.5` (`sigma_leverage.py:104`) saturating at roughly two majors, the dominant line is: *open two obliges, then speak, every time*. Nothing inside the run prices it. The collapsed line is the position's own worked example run twice.

**(b) The debt is not binding.** `oblige`'s subject is the actor, and `release` is `eligibility: ["own"]`, `requires: "a live Tenure of the named kind whose subject is the actor"` (`04_VERBS.md:448-457`). So the debtor discharges himself, next season, unilaterally. `13_ADVERSARIAL.md:65` grades exactly this a defect: *"`release` is `own`, so it is **the obligor discharging himself** — repudiation, not clemency … **FORGIVENESS IS CURRENTLY INEXPRESSIBLE**."* The falsifier arm *"the `Tenure` persists into the next season's world"* (`:295`) is therefore satisfiable only if the player chooses not to take a free act.

**(c) The permission is cited to a source that does not contain it.** `:275-277` — *"`R-18` … **permits named levels of the player's OWN advantage** (SKILL §11.5 P-i; `07:176-178`)"*. `07_THE_GAME.md:176-178` lists, as owed: ledger claims with source/confidence/when; which are firsthand; your own convictions and stances. Nothing about advantage levels. Two lines further, `07_THE_GAME.md:181` forbids **"anything from a resolver-side Query"** — and a σ-level assigned to an oblige is precisely a resolver-side derived magnitude. `SKILL.md:713` does support named levels as the legible form of advantage, but it is a diagnostic test the design deliberately fails (`07_THE_GAME.md:197`: *"A player at a trial will want to know how it is going, and cannot be told"*). The carve-out is inherited verbatim, citation and all, from `relay/A_FABLE_INTERROGATION.md:372`, including the phrase *"legible hand, illegible room"*.

**WHAT IT SHOWED.** The engine plumbing is correct and I could not break it — `net_boost` (`sigma_leverage.py:190-203`), `levels_to_net_sigma(aggressor=…)` (`:224-234`), `LEVEL_SIGMA` (`:97-102`) are cited accurately, and R-5/R-6 are genuinely avoided. But the channel's availability is not the agonist's finding (`06_RESOLUTION.md:271` states it, `R-6` demands it). The only novel content is the *price*, and there is no price: unbounded turns inside, a self-closable debt outside.

**SEVERITY: material.** A "devil's bargain" with no enforceable bargain is a free lunch on the one lever the design permits a player to see, and the visible magnitude is the one place where getting it wrong is loud rather than quiet (the position says so itself, `:308-309`).

---

## ITEM 6 · POSITION 5 — the ladder is two-way (`:313-360`) · **WOUNDED**

**THE ATTACK I RAN.** The position's own falsifier: *"Shows it wrong: the fold is filtered to the acting person's own emissions."* I ran it by hand. `00_DERIVATION.md:299-301`:
```
rung(run) := the lowest rung any emitted `matter.*` Event in THIS run has named
             -- a fold over the run's own emissions. Owned by nobody. Stored nowhere.
```
No filter, by person or otherwise. **That attack failed** — and the position is stronger than it states: `05_PROCEDURE.md:76-77` says the rung is *"held on the `commit` edge from the case's opener to the matter, in `Tenure.degree` (`00_DERIVATION.md` §B.2)"* — citing §B.2 as its authority while stating the **exact thing §B.2 retracted on five grounds** (`00_DERIVATION.md:275-302`, `13_ADVERSARIAL.md:51`). Sharpen, not soften.

**Two attacks that landed.**

**(a) The fold is band-blind, so the position's story is decorative.** All four `speak` bands emit `matter.*` (`04_VERBS.md:74-77`: `matter.carried / advanced / held / turned`). The fold reads *any* such Event's named rung. So A **failing** at conjecture moves the shared rung exactly as much as A landing Overwhelming. The collapsed line: the "raise you must see or give" (`:332-333`) and *"your opponent paid — their turn, their proof, their draw"* require the pusher to have **won**, and the mechanism does not read who won. The falsifier at `:349-353` plants an Overwhelming and would pass identically on a planted Failure — it cannot discriminate the position's claim.

**(b) The stated dependency on Position 1 is false.** `:340-344`: *"without **Position 1**, being pushed to a rung where your remaining speech kinds are inapt means your next act is **refused** rather than expensive … `B-1` and `B-14` must land together or neither should."* `04_VERBS.md:155-159` types the three aptness inputs separately: only the **genre** row carries *"a mismatch **fails `requires`**"*; the **rung** row's effect is *"`refute` is apt at conjecture and **empty** at quality"* — empty, not refused. And genre derives from the **bench's remit**, which is fixed for the proceeding and which moving down the rung ladder cannot change. **No rung movement can produce a refusal.** The stun-lock does not exist, so the coupling that drives the headline build order (`:873-875`, *"P5 is free and must ship with P1"*) is unfounded.

Both (a)'s cost line and (b)'s dependency are pre-registered in the agonist's declared input at `relay/A_FABLE_INTERROGATION.md:242` (B-14), including *"**Cost: 0**. ⚠ needs `B-1` priced, or the loser's next speech at that rung is refused rather than expensive"* — so the false coupling was inherited rather than derived.

**SEVERITY: material.** The factual core survives and improves; the *game* claim (one player's spend landing on another's position) collapses because the mechanism cannot see a spend, and the build-order recommendation it anchors is unfounded.

---

## ITEM 7 · POSITION 6 — the terms as a burnable Record (`:364-421`) · **BROKEN**

**THE ATTACK I RAN.** I opened every verb row the position's table cites.

**(a) `carry` is the wrong verb.** `:392` claims *"`carry` | `verb_table.yaml:83` | the terms travel with a person. **Reach the person, reach the terms**"*. `verb_table.yaml:83-93`:
```yaml
  - verb:        "carry"
    stratum:     "social"
    eligibility: ["own"]
    requires:    "a Petition exists; costs budget like any act"
    requires_typed: { form: existence, of: subject, kind: Petition }
    writes:      ["DocketItem.matter"]
    emits:       ["petition.carried"]
```
`carry` carries a **Petition onto a docket**. It does not move a `Record` and cannot: `Record` (`shape.py:2411-2421`) has a `rung`, no holder, and no verb in the 32-row table relocates one. This is a match on the English word — the failure mode `CLAUDE.md` §0 names as the costliest in this corpus. (The design shares the error at `03_PARAMETERS.md:320`, which lists `carry` as conferring the clerk role; the agonist cites the YAML line directly, so it is charged here.)

**(b) The forge arm of the falsifier is unrunnable.** `:412` requires *"re-run with `forge` substituting `max_depth: 5`"*. `verb_table.yaml:229-237`: `forge` writes `["Record.exists", "Record.forgery_quality"]` — **not `Record.stages`**. `create_record` (`:152`) and `open_case` (`:370`) write `stages`; `forge` does not. There is nothing to forge.

**(c) The claimed debt payment is circular — this is the kill.** `:398-400`: *"⭐ **And it pays a debt rather than adding one:** `H-87`'s no-default `max_depth` currently has no lawful source at all, and this supplies one."* `shape.py:1848-1853`:

> `H-80`. #353 §13.1 says the ACT declares a Record's stages and their terms. §F1's Candidate is `(verb, subject, why)` and carries no operands, so **NO COMPUTED ACT CAN DECLARE ANY** — `(Record, stages)` is a Part D row **unreachable from the person's own decision**. These are the instrument's declared stand-in, swept …
> `record_stages_default=3,`

`Record.stages` is itself a fabricated constant. P6 relocates `H-87`'s invented `max_depth` into `H-80`'s invented `stages`. The debt is moved, not paid.

**(d) Two homes for one value.** `08_SEAM.md:13` and `:21` make `max_depth` a **parameter** of `seam.contest` and of `proceedings.run`. `00_DERIVATION.md:248`: *"**The cap is the CALLER'S, always**, and a default is a fabricated constant (`H-87`)."* A value `proceedings.run` also reads off a Record is a second owner — `ID-2`, the defect P13 invokes against `registers`.

**(e) Coverage.** `00_DERIVATION.md:286`: *"**five of the twelve games have no `open_case` at all** — negotiation, public debate, audience, interrogation, negotiation-by-envoys"*. In those five there is no case Record, so no cap, no named arbiter, no return day. This is objection 3 of the five that killed the `Tenure.degree` rung proposal, arriving unchanged.

**(f) Pre-registered.** `relay/A_FABLE_INTERROGATION.md:238` (B-10) already states the `Record.stages` reader *and* the `R-14` tension, and rules on it: *"**One of the two must move; that is a ruling, not an edit**"*. P6's route-around is its own (vi) concession, so I do not press further there.

**SEVERITY: material, verging fatal for the headline.** Two of the four verbs in its own mechanism table do not do what it says, its falsifier's second arm cannot execute, and its single strongest claim ("it pays a debt") is circular against the instrument.

---

## ITEM 8 · POSITION 7 — the advocate's rope (`:425-485`) · **WOUNDED**

**THE ATTACK I RAN.** Three probes; the first failed, the other two landed.

**Failed attack (stated so this is a real verdict, not an absence).** I tried to show the rope must be a `requires` and therefore smuggles a gate. It does not: `commit`'s cell is `{form: existence, of: subject, kind: Proposition}` (`verb_table.yaml:101-104`), the rope is a separate Proposition, and no cell reads it. `:476-478`'s requirement that *"the act forms and resolves … the rope is not a `requires`"* is correct, and `Proposition` is genuinely `frozen=True` (`shape.py:2424-2427`).

**(a) It does not match the advocate it cites.** `:438` annotates its three acts *"→ `03_PARAMETERS.md:317`'s advocate, **exactly**"*. `03_PARAMETERS.md:317` defines the advocate as *"holds a `commit` to **another's disposition**, plus an `oblige` to that person"* — a commit to the principal's disposition **of the matter**. P7 substitutes a commit to a representation-Proposition. Either the advocate is not one under `03:317`, or a fourth act is required — and P7's cost table (`:461-462`) counts carriers, edge kinds, verbs, fields, Event kinds, keys, terms and magnitudes, but never **acts**. Position 4 counts the turn honestly (`:286`); Position 7 does not.

**(b) The seizable object points at a value the design deliberately does not store.** The rope names a rung (*"may concede to DEFINITION and no further"*, `:435`). The rung is a fold that *"Dies with the run"* (`00_DERIVATION.md:300-301`) and *"does not persist between seasons — A hearing adjourned and resumed next season **starts at the top of the ladder again**"* (`:309-311`, `P-22`). So a permanent, dated, frozen Proposition references an ephemeral quantity; producing the contradiction a season later requires re-deriving a rung that exists nowhere.

**(c) The seizure works for a human and for nobody else, and the position does not say so.** *"anyone holding both can produce it"* (`:451-453`) needs a comparator. `belief_contradicts` evaluates a verb's own `requires_typed` cell (`shape.py:3860`); nothing compares an emitted rung against a Proposition's value. The comparison is the player's reasoning. Position 11 makes exactly this concession for `knot` (`:686-687`: *"for a **player**, who is their own decision procedure … For an NPC, learning still reaches no choice"*); Position 7 omits it while claiming *"That is Blood on the Clocktower's mechanism … arriving with no deception subsystem"*.

**What survives.** The `Tenure.payload` declination is correct and correctly cited — `write_matrix.yaml:52-54`: *"`Tenure.payload` is REPLACED by `term?` (§B.8)"*. And presence-as-degrees is a real gradient built only from live rows. Pre-registered at `relay/A_FABLE_INTERROGATION.md:113` (B-5), which already names the letter and the debtor's `tell` as the missing degrees.

**SEVERITY: material.** The gradient survives; the seizure — which the position calls "the point" — is weaker in three named ways than stated, and the position's own (vi) already concedes it may be flavour.

---

# CROSS-CUTTING FINDINGS

**1 · The document is largely an elaboration of a read input, and one sentence says otherwise.** `AGONIST_CONVERSIONS.md:7-8` declares `FABLE_PLAYABILITY.md` as an input *"taken as established and … not re-derived"*. That file **does not exist on disk** — the only match in the tree is `/home/user/ttrpg/proposals/2026-09-05-proceedings-subsystem/relay/A_FABLE_INTERROGATION.md`, whose title line 20 is *"FABLE PLAYABILITY"*. Its §3.1 census maps one-to-one onto the thirteen positions **with the same costs**: B-1→P1 (`:229`, *"the `requires` conjunct on genre is removed … Cost: one injected Ob term, one data roster"*), B-13→P3 (`:241`, *"Cost: one injected term"*), B-14→P5 (`:242`, *"Cost: 0 … needs `B-1` priced"*), B-7→P2/P6 (`:235`), B-10→P6 (`:238`), B-11→P3's `AX-4` closure (`:239`), B-2→P10 (`:230`), B-4→P8 (`:232`), B-5→P7 (`:113`), B-16→P9 (`:244`), B-3/B-15→P13 (`:231`, `:243`), B-8→P12 (`:236`), B-20→P11 (`:128`). Its §4.2 is *"Duel of Wits' compromise scaled to what the winner lost"* — P2's item 3. Its §4.3 is *"the three levers an agonist should reach for first"*. Its §4.5 is *"the count"*.

Therefore `AGONIST_CONVERSIONS.md:958-960` — *"The audit predicted **'up to 12'** independently … **I reached twelve from the other end, which is corroboration** and not comfort"* — is false. `A_FABLE_INTERROGATION.md:477` states `Ob terms | 5 | **up to 12** | **+7**`, the agonist read it, and reached 12 and +7. That is agreement with a read source presented as independent rediscovery, which is a `CLAUDE.md` §0.1 point 4 defect (a number with no control) applied to the document's own headline defence.

**2 · The `Event.observed` channel carries precondition reads only.** `shape.py:5843-5861`. This breaks P1 (Item 2b) and independently undercuts Position 12 — under `verdict_reasons: given`, `determine`'s `observed` would fan out *"a DocketItem exists and your seat has the basis"*, not the reasons. P12 flags a weaker version of this itself (`:764-770`); the sharper statement is that `observed` is **populated with the wrong content**, not empty.

**3 · Falsifiers that specify an exact obstacle delta cannot fire.** P3 (`:236-237`, *"by exactly `2 × HELD_STEP`"*) and P9 (`:584-586`, *"by exactly `2 × PASS_STEP`"*) both hold the obstacle constant except for their own term, while `reception` moves on every witnessed act (`06_RESOLUTION.md:214-217`, `:368-373`) and P9's control changes the presence set outright. Any position adding a term to a twelve-term composed obstacle needs an A/B on the *term*, not on the *total*.

**4 · Observations outside my lane — recorded, not ruled.** P13's `registers` grep is accurate (`rosters.yaml:238` is the English verb in an `H-76` note, the only hit) — but `00_DERIVATION.md:273` counts `register` among the five rosters the design already commits to adding, which P13 does not address. P11's chosen horn is `P-41`'s own already-stated first option (`10_LOOPS_AND_GAPS.md:99`: *"either a closed room's concessions reach the world some other way, or the catalogue's floors are wrong"*). P8's create-half rests on the same stale `H-72` claim as Thesis B (Item 1). I have not ruled on any of these.

---

# THE ONE POSITION I WOULD DELETE

**Position 1.** It is ranked first by the document (`:851`), it anchors the recommended first commit (`:867`), and it is the only position that is wrong in all four ways at once: its statement of current behaviour is refuted in the reviewed directory's own survival table (`13_ADVERSARIAL.md:85`); its zero-cost delivery channel is destroyed by its own edit (`shape.py:5843-5861`); the conjunct it removes is not in the row (`04_VERBS.md:62-66`); and it spends +1 obstacle term and +2 magnitudes to convert a *public* witnessed refusal into a *private* reading, deleting the mechanism `04_VERBS.md:167` identifies as how the player learns. Deleting it also frees Position 5, which is coupled to it only by a dependency that does not exist (Item 6b).

# THE ONE POSITION I COULD NOT BREAK

**Position 5's factual core** — *the rung fold as written is shared, not self-only, and `05_PROCEDURE.md:76-86` is what is wrong.* The attack that failed is the position's own stated falsifier, run by hand: I looked for a per-person filter on the fold and found none at `00_DERIVATION.md:299-301`, none in the four `speak` emission rows at `04_VERBS.md:74-77`, and no competing definition anywhere in the directory. The claim is not merely upheld but **sharpened**: `05_PROCEDURE.md:76-77` cites `00_DERIVATION.md` §B.2 as its authority while asserting the `Tenure.degree`-on-a-`commit`-edge model that §B.2 retracted on five grounds (`00_DERIVATION.md:275-288`) and that `13_ADVERSARIAL.md:51` records as retracted. That is a live internal contradiction in the design, worth fixing on its own, independent of everything the agonist built on top of it — and the fix is the prose retraction P5 asks for, at zero cost, without Position 1.