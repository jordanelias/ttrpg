# Social Contest — Consolidation & Integration Proposals (v2)

## Status: PROPOSED — CIP-0..CIP-15 filed. **Needs Jordan: CIP-3, CIP-7b, CIP-9b, CIP-12, CIP-15**
## Date: 2026-08-06 (v2 same day) · Lane: SC
## IDs: ED-SC-0023 (programme), ED-SC-0024 (duality refinement), ED-SC-0027 (requirements + tracks), ED-SC-0028 (adversarial audit + corrections)
## Depends on: `audit/2026-08-06-social-contest-three-lens-audit/` — `00`–`06`
## Method: four read-only Fable precedent lenses, then two analysis lenses, then **three adversarial critics** who
## broke four claims in the companion document (record: `06`). Opus authorship throughout, per CLAUDE.md §10.

---

## §0 — How to read this

### 0.1 The governing result

Four independent precedent lenses converged on one principle from opposite ends (Lens B from Burning Wheel's
failure; Lens D from Into the Breach versus Ubisoft open-world design):

> **Two configurations of one engine are distinct scenes if and only if (i) a competent player's best action
> sequence differs between them — the parameters change *policy*, not just expected value — and (ii) the player
> can tell, before acting, which configuration they are in.**
>
> Fail (i) and you shipped a reskin. Fail (ii) and you shipped noise.

**Verb collapse and the thrice-flagged interface gap are the same principle from two sides.** That is why CIP-5
and CIP-10 are load-bearing rather than polish, and why every proposal carries a legibility clause.

### 0.2 The instrument — how a verdict in this document is graded

Added in v2. The v1 programme and its companion both used a duplication test that, on audit, was **not decidable**
and was **applied to a moving target**: kills were graded against the kernel *as built*, rescues against the
architecture *as proposed*. That asymmetry rescues anything by hypothesising a future reader, and it did (record:
`06` §2, finding 8).

> **Two riders bind every consolidation verdict below.**
> 1. **Name the system the verdict is graded against** — kernel as built, or programme as proposed. Never mix
>    them inside one table.
> 2. **Name the consumer.** A cut must show that nothing reads the removed state *today*. A rescue must name an
>    existing reader **or** the numbered proposal that creates one. A rescue that names neither is a wish.

### 0.3 Corrections to our own prior documents

Each changed a recommendation we had already made. C-1..C-7 are carried from v1; C-8..C-12 are new in v2.

**C-1 — the anti-collapse principle was necessary, not sufficient.** Burning Wheel's manoeuvres *did* alter
different state and collapsed anyway, because the win condition cashed every change into one currency. **Corrected:
verbs stay non-dominated iff the best verb varies per decision-instant with observable changing state, *and* the
close contains no common scalar into which all effects convert at fixed rates.**

**C-2 — our kernel does not satisfy it.** Every win condition reads `s.adv` (`resolver.py:52-145` ✓); Standing and
Room feed `Readiness`, which multiplies into the gain that *becomes* `adv` (`:314-316` ✓). One scoring scalar plus
one orthogonal terminal — the fault/clinch catalogue (`:438-442` ✓), the seed of a second currency.
*Refined in v2:* `VoteAtClose` also reads juror `discipline` as bench-weight (`:109-140` ✓), so the correct
statement is that no win condition reads any *contest* state but `adv`.

**C-3 — M2 Scope is not a safe borrow.** Lens C returns a hard NULL: no published game mechanises
principal-repudiation of an agent's live over-mandate commitment. The mandate *gate* is well precedented; the
repudiation *branch* is not. CIP-7 splits on that seam.

**C-4 — "no opposition model" undersold what exists.** The Church action chain is a genuine fixed ordered agenda
gated on Mandate thresholds, and `fixed_lean` is a hardcoded red line. What is missing is memory, patience and a
voiced reason — not belief.

**C-5 — CIP-2 cited a fabrication.** Document 4 retracts document 3's warrant × attack matrix as "invented rather
than derived … formatted to look rigorous." The three-attack taxonomy is sourced; **the warrant-keyed vulnerability
assignments are WITHDRAWN and stay withdrawn.** The tell was in our own text and nobody followed it.

**C-6 — the story model does not fix it.** `acceptance = h(coverage, coherence)` is a fixed scalarizer: C-1's defect
one level down. Its real value is as a theory of *how the adjudicating mind scores*.

**C-7 — the Klei refutation hits our kernel.** Our loop is structurally a stationary, always-full action menu
resolving through a random roll into a single scoring scalar. What cards fixed decomposes to **non-stationarity of
the per-turn decision problem**, of which a persistent claim board is the second carrier — no deckbuilder required.

**C-8 (NEW) — "the contest is sealed off from the world" was false.** The companion document's headline claim, and
mine. A second path is live by default: `mc_v18.py:148-151` ✓ runs `parliamentary_bridge` every season
(`ECHO_TRANSPORT` default ON — Jordan, 2026-07-08, "the baseline campaign"); `_derive_vote`
(`parliamentary_bridge.py:82-97` ✓) **generates a topic from world pressure**; `parliamentary_vote.py:206-216` ✓
writes back to `world.factions`. The falsifier that catches this was published in that document and never run.
**The surviving claim, which is the one this programme acts on:** the personal-scale Bout kernel is sealed — its
entire interface is two integers (`scene_dispatch.py:298, 306-307` ✓) — and the parliamentary path, while it
carries a topic and writes back, is a Mandate-pool roll, not the agôn: no evidence, no claim record, no rhetoric
crosses it either. **It is also the working precedent for CIP-5** (§CIP-5).

**C-9 (NEW) — "no new primitive" was false for the ledger, and CIP-1 was already right.** The companion claimed the
audience→world channel needed no new primitive. It does: `ledger_add` treats `Reputation` as `SINGLE_VALUED` **by
kind, ignoring `key`**, deleting every prior Reputation tag on insert (`ledger.py:31-32, 50-53` ✓); tags live on one
`Settlement` (`:14-16` ✓), so there is **no holder dimension** and factions hold no ledger. CIP-1(a) and (c) already
proposed exactly the mount points and the collision fix — the error was the companion's, not the programme's. **Two
gaps remain open even under CIP-1** and are added to it in v2: a *holder* dimension, and a carrier for **reach**.

**C-10 (NEW) — the warrant axis survives, and the matrix is not merely smaller, it is unnecessary.** See CIP-2.

**C-11 (NEW) — the duality claim needs CIP-9b, and the two-output close depends on it.** Fork A is RULED: "auto =
the contest kernel run headless, played = the same kernel run interactively … consistent by construction"
(`auto_manual_resolution_duality_v1.md:75` ✓), and §6 makes matched-input consistency the hard constraint
(`:61-65` ✓). So a two-output close either changes nothing in expectation — and `04`'s wasted-attention charge
returns on two scalars instead of one — or lets the player steer a trade-off the auto policy does not, which is
**mode-shopping in consequence space, the exact exploit §6 prevents.** CIP-9b is the escape and it is unratified.
**CIP-14 is therefore conditional on CIP-9b, not merely sequenced after it.**

**C-12 (NEW) — the programme carried three unreconciled "second currencies."** CIP-12 (attribution), CIP-1's
record-*kind* shape, and the companion's room-impression channel were derived independently and never compared. An
anti-collapse condition that licenses a new output currency per document is collapsing in the other direction.
CIP-12 in v2 is the reconciliation, and it needs Jordan.

### 0.4 Epistemic status — read before ratifying anything

**Precedent claims** are model knowledge, no web access, tagged `[HIGH]`/`[MED]`/`[LOW]` at source; only `[HIGH]`
and `[MED]` propagate. Three binding consequences: reception claims are softer than mechanism claims; a NULL over
one model's knowledge is not proof of absence (Lens C's Q5 null is load-bearing for CIP-7 and is worth one human
check); survivorship bias runs one way — failed consolidations that never shipped are invisible.

**Classical claims** (new in v2) are the same class and worse: doctrine confidence is generally high, **locator
confidence is MEDIUM at best.** No chapter or section number in this document may enter a ratified doc without a
human text check. One correction already: **burden of proof is practice-level Roman law contemporaneous with
Quintilian, not treatise doctrine in Aristotle/Cicero/Quintilian** — CIP-3 says so rather than implying pedigree.

**Measured versus proposed.** Claims marked ✓ were verified against the working tree by the author or a critic
(~25 citations were re-checked by two independent critics with zero misquotes). Everything else is design.

---

## §1 — The requirements this programme must satisfy

From Jordan, 2026-08-06. The programme is graded against these, not against its own internal tidiness.

| | Requirement | Owner |
|---|---|---|
| **C1** | **HOW one argues** — appeal × temporal orientation (nine ways to make the same point) | **CIP-13** |
| **C2** | **WHAT one argues** — rung · warrant · the claim and its status | **CIP-2**, CIP-15 |
| **C3** | **WHY one argues** — the end pursued; its divergence from the adjudicator's | **CIP-5** (declared in the writ) |
| **C4** | **HOW effectively** — faculty · preparation · credibility slope **and** intercept | CIP-4, **CIP-1** (intercept) |
| **P1** | **WHAT KIND of contest** | CIP-0, CIP-15 |
| **P2** | **WHO adjudicates** | CIP-6, CIP-11 |
| **P3** | **HOW adjudication occurs** | **CIP-3**, CIP-11 |
| **P4** | **HOW audience impacts** — characters, adjudicator, **and the world after** | **CIP-14** |
| **W1** | How salient topics enter | **CIP-5** |
| **W2** | How an inquisition presents its case | **CIP-7c** |
| **W3** | What evidence and proof are | **CIP-2** (cross-lane FI) |
| **W4** | What is relevant | **CIP-13** |
| **W5** | What the audience carries out | **CIP-14**, CIP-12 |
| **W6** | How much this adjudicator's judgment weighs | **CIP-1** (reach), CIP-14 |
| **W7** | What the room and bench already think | **CIP-1** (priors), CIP-6 |

**Coverage gap, stated:** C3 is the requirement with no partial implementation anywhere in the kernel. CIP-5 gives
it a home; whether it carries mechanical consequence is fork §4.7.

---

## §2 — The proposals

Each carries **Problem · Basis · Proposal · Consolidates · Risk · Falsifier**. Risk classes: **EVIDENCED**
(recombination of shipped, mostly-praised mechanics), **CONDITIONAL** (evidenced but gated on a stated test or a
`[MED]` reception claim), **NOVEL** (no published precedent — prototype before spine status).

### CIP-0 — The canonical head describes the engine that runs
**EVIDENCED (doc hygiene) · prerequisite to everything**

`social_contest_v30.md` specifies a loop with no engine; the kernel runs a loop with no canonical prose. Rewrite
§§3–5 to describe the kernel — stasis grounds, appeals, reserve, dossiers, faults and clinches,
readiness/resonance/leak, pressure — demote Model A's exchange algebra to a historical note, and move
per-proceeding difference into the config rows that already exist.

*v2 addition:* the head must describe the **reduced** architecture — eight in-bout tracks, two config surfaces
(Venue, hearer), one ledger interface. A preference vector that never moves during a bout is **configuration, not
state**; that single rule demotes three things the companion had called tracks.

**Falsifier.** A reader given only the head should predict the outcome distribution of a seeded bout.

### CIP-1 — The Record spine: the world interface, both directions
**EVIDENCED · highest value-to-cost in the programme**

**Problem.** Every wired agôn output is a stat delta; one arc-scoped boolean is the only thing guarding a later
transition. And nothing feeds *in*: the credibility intercept slot exists with no producer (`resolver.py:182-193` ✓).

**The reframing finding (Lens D).** Asked what carries Church Tribunal's identity apart from Guild Arbitration if
both become config rows: *the sameness risk is already realised, and not by the config rows.* When everything
downstream is a scalar, two proceedings **are** the same scene however bespoke their resolution. **Distinct
proceedings mean distinct emittable record types.** Consolidation is *less* risky after CIP-1, not more.

**Proposal.**

*(a) Mount points.* Add `ledger: list` to `Faction` and to the contest `Body`. `ledger.py`'s functions are free
functions over a plain list; `Settlement` merely holds one — additive, not a refactor.

*(b) Fields.* Extend `LedgerTag` with `source` (event id + human-readable cause — the field that makes a record
read as memory; you cannot narrate `("Grudge","varfell",1.0)`), `parties` (holder and bound), `uses`/consumable,
`superseded_by`.

*(c) Fix the latent bug.* `ledger_add` replaces in place on `(kind,key)` (`ledger.py:50-57` ✓). Intended for
`Reputation`; for a `Precedent` it is a silent history-eater.

*(d) **NEW in v2 — the two gaps C-9 exposed.*** **Holder dimension:** `Reputation` is `SINGLE_VALUED` by *kind*,
ignoring `key`, so it cannot express "the bench thinks X of you" alongside "the room thinks Y." W7's six priors
need `D[holder][object]`; that is a schema change, not a free compose. **Reach:** `key` and `ttl` give identity and
lifetime, not *which ledgers hold a tag*. W6's authority effect — a king's precedent binds widely, a governor's
locally — has **no carrier today**. Both are **SE-lane changes** and are marked as such below.

*(e) Emission.* Close emits a `Precedent` on a Decisive/Total band; a `Debt` for an Obligation; a `Grudge` on
violation; **and a record for the loser, priced by margin** — a narrow loss leaves a larger citable residue than a
rout.

*(f) Consumption — ship at least one consumer per kind, simultaneously.* Restore the `tribunal.py` prerequisite;
make Let It Ride enforceable; give Recall's "named precedent" an engine-side verifier; let faction stance read the
ledger.

*(g) The intercept.* Persistent *auctoritas* — Cicero and Quintilian's *vir bonus*, as against Aristotle's
in-speech ethos — is the ledger read at contest open, feeding `standing_start`. **Not either/or: intercept and
slope.** Prior passes treated these as a contradiction to resolve; the corpus names both because both exist.

**The integration point is one dataclass.** `DomainEchoResult` carries only
`fires/affected_faction/affected_stat/delta/timing/notes` — mechanically why Projection became a stat delta. But
the `Key` at `echo_transport.py:412-427` already assembles `payload{scene_id, outcome, participants}` and a
populated `causes[]`. **Provenance and parties are already computed and then discarded at that boundary.** Adding
`records: list[LedgerTag]` alongside `stat_deltas` closes it.

**Seven rules imported from precedent, each binding:** guard on the consumer, story on the record · costed
bypasses, not walls · scarce-and-heavy or numerous-and-aggregated, never numerous-and-individually-gating · cap by
slot structure, not advisory · prefer discharge the player witnesses · supersession-by-later-proceeding makes
discharging a record itself a playable contest · **a record with no truth value is still a record** — the world
remembers what was *ruled*.

**Anti-pattern hit twice already:** a record kind shipped without a producer/consumer pair (`world.casus_belli` has
readers and no producer; Obligations have a prose consumer and no engine). A third would poison the concept.

**Cross-lane:** (a), (d) touch **SE**. *Observation, not a ruling.*

**Falsifier.** There must exist a seeded campaign trace where a contest outcome in season N changes *which branch
fires* — not merely which number moves — in season N+k. No trace ⇒ the spine is inert.

### CIP-2 — The close weighs a claim graph; warrant schemes carry their own attacks
**CONDITIONAL (two sweeps, unrun) · the real content of Fork B**

**Problem.** Four Styles produce identical state changes differing only in one upside-only scalar (≤0.5σ), so the
grid collapses to two viable picks. And arguments never answer each other: each move adds independently to `adv`
(`resolver.py:315-316` ✓).

**Basis.** The read-then-match family has no surviving instance under our constraints. DXHR is the closest analogue
and *worked*, but on three props we lack: bespoke content consumed once `[HIGH]`; per-beat line variation, so the
mapping was line→response not person→response `[MED]`; and a purchasable perfect read, after which the discourse
consensus is that the debates were solved `[MED]`. **When the read is purchasable, the choice degrades to a
prompt.** DXHR never faced an AI opponent playing it twice; we do. Alpha Protocol's escape — refuse to grade the
answer `[HIGH]` — is real but unavailable at a verdict; what is importable is the *placement*: ungraded payoff
belongs at the outcome layer, not the verdict.

**Proposal, restated and strengthened in v2.**

> **The contest close must consume claim-graph state — which claims stand, which premises are severed, which pairs
> the body must weigh — NON-FUNGIBLY, and not only the accumulated scalar.** A second dimension scalarized into the
> first at a fixed rate is not a second currency.

Promote what we already have: the fault/clinch catalogue is the one thing that does not cash into `adv` (C-2).
Generalise it from a terminal condition into a **second scored dimension**, with the venue's `DefeatCatalogue`
deciding how the two compose. Griftlands is the shipped evidence that this survives an AI opponent and heavy
replay, because its arguments *do things while they stand* `[MED]`.

**C-10, the v2 advance — the withdrawn matrix is not needed at all.** An argumentation scheme is not a tag on a
proof; it is a triple — **premise pattern · conclusion pattern · critical questions**, the recognised ways to
challenge it. Argument from expert opinion is challenged by asking whether the source is an expert *in this field*,
whether experts agree, whether they are biased; sign, precedent, consequences and analogy each carry their own list.

> **A scheme defines its own attack surface. There is no warrant × attack matrix to author.**

The matrix retracted under C-5 was solving a problem that **does not exist once warrants are schemes rather than
tags**. Undermine/Rebut/Undercut become the three *structural positions* an attack occupies (premise, conclusion,
inference); the scheme's critical questions supply the content. This also gives the engine a way to present attacks
without prose — the moves available against a standing claim **are** that claim's critical questions — and it
bounds authoring cost **per scheme**, a small closed set, rather than per (warrant × attack) pair.

*Sourcing:* Toulmin's layout and Walton's schemes are **modern argumentation theory, not A/C/Q** — a descendant of
the *topoi* and of dialectic's regulated challenge. **Ours-by-adoption**; every number a `[SEED]`.

**W3 — what evidence *is*, and where it comes from.** Aristotle's ***atechnoi pisteis*** are proofs *not furnished
by the art*: laws, witnesses, contracts, oaths — the orator does not make a contract more probative, only chooses
when to produce it. **So the kernel's hidden fixed weight is the classical definition being honoured, not a
simplification** (`primitives.py:282-310` ✓). Three gaps, all world-facing: **no producer** — every `EvidenceItem`
in the tree is a hand-authored literal, and `systems/fieldwork/sim/investigation.py` is entirely stubs ✓; **no
apparent-versus-true split**, so forgery is unrepresentable; **no provenance**, which is what makes an attack bite
differently. *The case you can make should be the case you did the work for.* **Cross-lane: FI. Observation.**

**Consolidates.** The orientation bit (dominated contest-wide) and the Doubt Marker (unimplemented, currently
shipped inverted) both retire into attack structure.

**Falsifier — two sweeps, AI-vs-AI best-response over judge and venue distributions.** (1) If Style-pick entropy
under the armature alone stays high (no Style above 40% pick rate), the armature suffices and this proposal is
wrong. (2) Implement the three attacks as pure `adv` deltas and re-run; precedent predicts collapse to the two best
exchange rates. If entropy stays high anyway, the claim-graph condition is unnecessary and CIP-2 reduces to a verb
swap. **Neither has been run. Do not ratify CIP-2 without them.** *(v2 note: the companion document adopted the
scheme apparatus while dropping this condition. The condition is reinstated and binds the schemes too.)*

### CIP-3 — Burden as a Venue field
**EVIDENCED · NEEDS JORDAN (Fork A, ED-SC-0020)**

Applied to our eight proceedings, the discriminating test sorts the parameters cleanly: burden / win-condition
family changes what you maximise (variety-bearing); the fault catalogue changes which moves are safe
(variety-bearing so sharply it currently kills a shipped policy, bug F4); proof weights are variety-bearing
*conditional on clause (ii)*; and **`track_start` bias (Church 6 vs 5) changes only expected value —
sameness-bearing.** That last row is Fork A stated in precedent terms.

**Proposal.** One `burden` field on `Venue` ∈ {ACCUSER, RESPONDENT, LOWER_STANDING, NONE}, with stall semantics at
close. Retire `ProofBar`, `GraceThreshold`, the two biased starts, the `use_tracker` tri-state. **Keep the
Persuasion Track** — its compromise band is the one thing burden does not give.

**Legibility clause (mandatory).** Near-NULL: no acclaimed videogame renders formal burden of proof as a
first-class UI object; Ace Attorney enacts it diegetically. Synthesis, not lift: render burden as **gravity on the
track** — a visible token on the burdened side plus an animated one-step slide against the holder on every stalled
exchange. "Silence convicts" becomes watchable.

**Pedigree, corrected (C-4 of §0.4).** *Onus probandi* is **Roman legal practice**, contemporaneous with
Quintilian; status theory discusses which side must establish what, but the treatise warrant is thin. Say so.

**Falsifier.** A player shown only the contest screen must be able to say who loses if both sides stop talking.

### CIP-4 — Setup advantage as δσ under the cap we already ratified
**EVIDENCED · closes ED-SC-0005 with no new number**

Recall +2D, Corroborate +1D, Prep +1D and Findings +2D stack uncapped; with Momentum the prepared side wins
exchange 1 at p ≈ 0.93 and takes a one-exchange Total Victory at p ≈ 0.62. Retire the four flat dice into the
`Dossier` — which already has per-source exhaustion, diminishing corroboration and a hard cap — and route the
residue through δσ under CR6's existing `M_MAX = 1.5σ` tanh cap. **CR6 already ratifies that setup advantages
"accumulate as δσ, tanh soft-capped"; the flat pool dice violate the subsystem's own ratified substrate.**
ED-SC-0005 asks Jordan to invent a ceiling that was ratified months ago.

*Also retired here:* **Momentum-as-purchasable-successes.** No classical function — buying assent is precisely what
the art of persuasion is not — and no demonstrated play function.

**Legibility.** XCOM's itemised decomposable modifier list `[HIGH]`, plus the board-game rendering: the marker's
position *is* the stacked advantage, with the cap drawn as compressing segments near the rail. **A stacked deck the
player can see is drama; one they cannot see is unfairness.**

**Falsifier.** Re-run the stacking arithmetic; P(win exchange 1) for a maximally prepared side must fall from 0.93
into a band Jordan accepts, and no legal combination may exceed 1.5σ.

### CIP-5 — The writ: the question, the stakes, the dials, and the end pursued
**EVIDENCED · absorbs W1 and C3**

**Basis — Blades in the Dark.** The strongest "one resolution move, parameterised" precedent in tabletop, and the
load-bearing device we had missed: **the parameterisation is spoken aloud before the roll.** The roll is
deliberately uniform *so attention stays on the dials.* Adopting the math without the announcement ritual takes the
half that does not carry the variety. **Basis — Burning Wheel's Statement of Purpose**, plus a forcing null:
*there is no functioning no-GM game that determines the meaning of an outcome after resolution.* With no GM the
Statement of Purpose is **forced** — stakes must be machine-representable data before the dice.

**The writ**, emitted at open:

1. **The question** — and **W1: where it comes from.** Today the question is `venue.start_ground`, a constant per
   proceeding (QUALITY for seven of eight, `modes.py:59-61` ✓). **We already have the working pattern in our own
   code** (C-8): `_derive_vote` raises a motion from world pressure — lowest-Stability faction proposes,
   highest-Mandate defends. Generalise *that* to the agôn: a topic is raised by an expiring Precedent, a Grudge
   with a claimant, a Debt called in, a clock running out. **A topic the world did not raise should not be
   arguable.** This is the Roman formulary shape — the praetor's formula fixes the question and the judgment
   options before the *iudex* hears `[MED]`.
2. **The stakes** — the *draft text of the Record* this contest will emit, validated for scope at open. The
   Statement of Purpose is literally the pending `Precedent` or `Debt` (ties CIP-5 to CIP-1 and CIP-7).
3. **The dials** — burden placement, which faults are fatal here, exchange budget, the venue's legal texture.
4. **The coarse read** — the Appraise band, rendered as a sentence, not a vector.
5. **The declared compromise axes** — what a partial outcome means *here*. Our Compromise band currently says "GM
   narrates partial outcome proportional to final position" — GM fiat in a no-GM engine. Pre-declared axes are what
   make Scaled Compromise executable rather than aspirational.
6. **NEW in v2 — the end pursued (C3).** Each side declares the *topos* it argues from — the advantageous, the
   just, the honourable, the pious. Its divergence from the adjudicator's governing end is the one place a
   speaker-side value axis becomes mechanical: arguing from an end this judge does not hold is *available but
   expensive*. **Whether it carries mechanical consequence or is flavour is fork §4.7** — it is the only
   requirement with no partial implementation to fall back on.

**What it integrates.** The variety mechanism (dials are the scene), the legibility mechanism (the player sees
which configuration they are in), the no-GM stakes fix, W1's topic channel, C3's home, and the Record's entry
point. **One object, six problems** — the largest consolidation in the programme.

**Falsifier.** Show a player two writs from different proceedings with the roll math hidden. If they cannot say
which room they are in and what losing costs, the writ is not working.

### CIP-6 — Opposition: memory before intelligence
**EVIDENCED, except one component NOVEL**

Factions cannot obstruct across seasons and cannot concede; `faction_action.py:220` is a single weighted
`rng.random()` per season with no cross-season state. **The finding that makes the fix cheap:** no shipped faction
AI in any surveyed game achieves "obstruct then relent" via lookahead — Victoria 3, CK, EU4, Frostpunk, Total War
all fake planning with **threshold predicates over persisted accumulators**, and it is enough, because the *player*
supplies the narrative of intent. **State and predicates, not a planner.**

Add to `Faction`: `aims` (2–3, visible — SMAC agendas, Civ VI public agendas); `redLines` (unbuyable, announced,
structurally bypassable — Vic3's unbuyable stances, praised; **inert until a side-payment verb exists to refuse**,
so sequence after CIP-8); `threat` (accumulator, **magnitude concealed, structure shown**, probed by truthful
banded reads — **NOVEL in the concealment**); `patience` (capability gate plus accumulator — CK ultimatums fire on
*power* crossing a threshold, not on anger duration); `aim.expires_with` (dies with its holder).

**What makes a faction feel like it believes something** — four parts, and SMAC is the usual answer because it has
all four: disposition reads **public policy or record state, not a gift ledger**; the preference is **immutable**
(no payment moves the agenda, only the offending state); the AI **pays for its belief**; and **the reason is voiced
at the moment of obstruction**, in character. The fourth is the cheapest and most valuable addition here. A
concealed number plus a silent refusal is Civ VI, read as caprice; a concealed number plus a truthful stated reason
is poker with table talk, and it plays.

**W7 — and this is where the priors live.** "Disposition reads public record state" *is* the ledger. Six priors:
three objects (character · faction · question) × two holders (bench · room). Orthogonal — a judge may respect you,
distrust your order, and have pre-judged the question. **Disposition is not taste:** taste weights the appeal
(CIP-13), disposition biases reception. A judge can love logos and hate you. Storage is CIP-1(d).

**What does NOT seed this.** `FactionBoost`'s seven-faction table maps *faction → the argument-style a room
dominated by that faction rewards* (`dictionaries.py:386-442` ✓). It contains no holder, no valence, no opinion
*about* anyone. It is **crowd-profile data (CIP-14) plus ethical-mode vocabulary**, not `D[holder][faction]`. The
companion document rescued it into the wrong track; recorded here so the error is not repeated. The die stays dead
— it has **no resolution consumer at all** in code; the +1D is prose-level.

### CIP-7 — Authority, split along the seam precedent supports
**7a EVIDENCED · 7b NOVEL, NEEDS JORDAN · 7c EVIDENCED (new)**

**Problem.** A personal-scale win binds an entire faction with no check that the character could bind anyone, and
the only exit is breach. Meanwhile `faction_politics_v30.md` *consumes* Obligations in its demotion table — a
consumer for an object that does not exist.

**CIP-7a — the mandate gate. Adopt.** `bind(actor, body, terms)`: if `terms.within(mandate.limits)` → BOUND.
Precedent is solid — Suzerain's constitution, CK crown-authority levels, John Company's offices. And it makes risk
*computable*: enumerate the bodies and offices a deliverable touches plus the actor's standing in each, and
`repudiationRisk` is arithmetic over data we already have.

**CIP-7b — the repudiation branch. Do not spine it yet.** A PROVISIONAL binding the counterparty acts on, later
disavowed by the actor's own principal, with the counterparty keeping what was transferred, has **no published
implementation**. Historically excellent (*sub spe rati*; Versailles), mechanically untested. We would move from no
authority model to an authority model with no published precedent in one step, on the mechanic upload 3 calls the
spine of the design. **Paper-prototype first; run the human literature check named in §0.4.**

**CIP-7c — the institutional party (NEW, W2).** An inquisition is not a person with a different portrait. It
differs in four measurable ways: **(a) ascribed versus earned standing** — the office carries authority the officer
did not earn; **(b) a dossier assembled over time** rather than owned at scene start; **(c) a mandate** bounding
which rungs it may reach — jurisdiction as precondition, not rung; **(d) institutional consequence on defeat** —
the institution's Reputation moves, not only the inquisitor's.

*(a) has a primitive already:* `split_standing` separates ascribed **Rank** from earned **Credit**
(`resolver.py:200-214` ✓), default off, no venue enabling it. **But it is coupled, and the companion missed this:**
Rank's one distinct in-bout consumer is `SelfGating.licit` (`primitives.py:219-220` ✓), which gates the `hard` verb
that CIP-13 kills as strictly dominated. **So `split_standing` cannot be rescued *and* have its only consumer
deleted.** If 7c is built, Rank needs a consumer that is not `hard` — the natural one is (c), the mandate bound. If
7c is not built, `split_standing` is excess. Its fate is coupled to this proposal, not independent of it.

**Cross-lane:** (d) touches **FA**. *Observation.*

### CIP-8 — Fold negotiation into the gate, gated on `settle()` existing
**CONDITIONAL — the gate is the whole proposal**

`gate(burden = NONE)` is only the **front half**. Upload 3's own S4 row terminates in `settle()` — reservation
values, offers and counters, side payments, instruments, scaled compromise — a genuinely separate mechanism the
gate hands off to. Fold without building settle and precedent predicts negotiation-as-menu, the flat one-shot
diplomacy of most 4X games `[MED]`. The positive precedent is Griftlands: negotiation *can* share an engine, but it
earned distinctness by owning **its own persistent state vocabulary** `[MED]`. Our kernel already agrees —
`modes.py:13` says the genuinely different sub-systems "remain scaffolds," and `NegotiationMode` is stub-wired with
"win = agreement in the overlap": reservation values, named and unbuilt.

**The gate.** `burden = NONE` is ratifiable as *the* negotiation implementation **when and only when** an
offer/counter/side-payment verb set and a reservation-value ConcealedValue are in the move vocabulary. Before that,
the fold is a rename and should be described as one.

**Where the concede verb goes.** Mid-argument AI concession as a *move* is thinly evidenced; compromise-as-band is
universal. Precedent places it as an **inter-exchange settlement offer**, not a new in-loop move class.

### CIP-9 — Retire the tripartition; refine the fidelity constraint
**9a EVIDENCED · 9b NEEDS JORDAN — and CIP-14 now depends on it**

**CIP-9a.** Football Manager does not keep three rulebooks for full match, commentary and instant result — one
engine, three views `[MED]`; our Auto/Manual doctrine already ratified "one engine at two fidelities." The
TTRPG/BG/Hybrid tripartition is a tabletop inheritance that duplicates specification and changes no mechanics to
remove. A free cut.

**CIP-9b — refine `E[auto] ≈ E[played]`.** Right in intent (anti-mode-shopping), underspecified in its baseline. In
Football Manager a watched match diverges from an unwatched one exactly by the manager's live interventions, and
that divergence is the **skill premium** through the same verb set `[MED]`. Total War is the cautionary pole: two
resolvers held by calibration, and the community finds the seam `[MED]`. **Proposed refinement:** measure `E[auto]`
against **AI-vs-AI played**, not expert play, and treat player skill above that baseline as a feature rather than a
calibration violation. Canon already says the auto path "resolves through NPC AI."

**v2 — this is now load-bearing, not a refinement.** Per C-11, CIP-14's two-output close is *unsound* under the
constraint as ratified: either it changes nothing in expectation, or it is mode-shopping in consequence space.
**CIP-9b is the precondition for CIP-14, and ratifying CIP-14 without it would install the exploit §6 exists to
prevent.**

Two precedent notes to carry: FM achieves parity **by construction** (views of one simulation) rather than by
calibration — the shape Fork A already chose, and should not drift from; and XCOM 2 ships **no** auto-resolve
`[HIGH]` because its outcome surface is high-dimensional. **Auto-resolve is viable only where the outcome surface
is low-dimensional** — which is a direct constraint on how much per-scene state CIP-2 and CIP-14 may generate.

### CIP-10 — The legibility layer
**EVIDENCED for three surfaces; the fourth is a synthesis**

Clause (ii) of the governing principle, i.e. half the variety mechanism — not polish.

| Surface | Pattern |
|---|---|
| **(a) The record** | Obra Dinn's book `[HIGH]`, Frostpunk's Book of Laws, CK3's hooks panel — diegetic, auto-populated, cross-linked, and critically **it visibly banks**: a `LedgerTag` should change state the instant it starts guarding a transition. "This Precedent is now citable in Guild Arbitration" is Obra Dinn's ink-fill moment |
| **(b) The adjudicator read** | Disco Elysium's skill voices `[HIGH]` + Ace Attorney's penalty meter `[HIGH]`: surface internal numbers as *characters who speak* — "Empathy: the Inquisitor has stopped listening." **Do not use CK3's exact-number tooltip** — an exact read collapses the concealed-value game the kernel is built on |
| **(c) The stacked advantage** | XCOM's itemised breakdown `[HIGH]`: aggregate always decomposable on demand, but **the top-level summary must carry the read**; Vic3's standing criticism is that tooltip archaeology substitutes for legible top-level design `[MED]` |
| **(d) The burden** | Near-NULL. Gravity on the track. **Synthesis, not lift** |

**One rule across all four, from Blades:** the read is announced **before commitment**, not revealed in a
post-mortem. CIP-5 is the delivery vehicle.

### CIP-11 — Deliberation: extend the ballot we already ratified
**EVIDENCED**

Adopt N10 as an **extension of `VoteAtClose`**, not a replacement: retain the first-ballot sample per member
instead of aggregating immediately; add influence rounds where majorities apply informational *and* normative
pressure while minorities apply informational only; add acceleration and a momentum lock whose one reversal event
is the first crossing to the minority. The ratified weighted-by-standing threshold (ED-1057) becomes the count rule
*inside* deliberation, unchanged. Today's `VoteAtClose` is formally a **degenerate zero-round N10**.

**The real blocker.** `ContestView` exposes the audience as two booleans, and `Panel` **averages** member
`discipline` and `character()` during the bout (`contract.py:42-51` ✓). We author individual minds — the inquisitor
is `char_ethos=0.20, char_pathos=0.15, char_logos=0.65` — and discard them exactly where they would matter.
Per-member exposure is the prerequisite. *(Note: `VoteAtClose` already ballots per member at the terminal
(`resolver.py:131-142` ✓) — the averaging is an in-bout loss, not a total one.)*

**Falsifier.** A contest must exist in which persuading one *named* juror before the ballot changes the verdict,
and the player can identify which juror that was.

### CIP-12 — The second currency, reconciled
**CONDITIONAL · NEEDS JORDAN (new in v2: this is the reconciliation C-12 demands)**

**The problem this now solves is ours.** Three candidates for "the second output" were derived independently and
never compared: **attribution** (does the target believe the decision was their own), **record kind** (which
`LedgerTag` a close emits), and **room impression** (what the audience thinks of you afterwards). Shipping all
three would be an anti-collapse condition licensing a new currency per document.

**Ruling proposed — they are one axis and two mechanisms, not three currencies:**

- **Record kind is not a currency.** It is the *shape* of the emission, selected by band and by who was bound. It
  has no independent magnitude to trade against.
- **Attribution and room impression are the same quantity read by two parties** — what the *bench* concluded about
  you versus what the *room* concluded. Under CIP-1(d)'s holder dimension that is literally one table with two
  holder rows. **One currency, two holders.**

**So the second currency is: what the people present now believe about you** — recorded per holder, priced by
margin, consumed strictly post-close.

**Why this answers C-2 where the story model does not.** Its value realises in a *different subsystem at a
different time* — breach probability, `Grudge` magnitude, opposition patience — so no close-time exchange rate can
be fixed. And it is anti-correlated with `adv`-maximal play at the margin: the merits-maximal line (public
crushing) is plausibly attribution-minimal. **A currency you sometimes buy by not spending the other is exactly
C-1's signature.**

**Two binding constraints.** Consumers must be **strictly post-close** — wire it as an additive close-time term and
it collapses into the scalar like everything else. And ground it on the **ELM durability leg (T0/T1), never the
Guiguzi paraphrase**, which document 5's own B1 tier-floors at T2.

**Falsifier (new).** Falsified if any rule converts this currency into `adv`, or the verdict into it, at a fixed
rate. **A guard is required, not merely a falsifier** (§0.1 point 5): a registry-style test over the conversion
sites, on the `_CELL_OWNED` template. **Not yet written — open work, named as such.** *Residual the guard does not
cover:* whether the two axes re-converge two hops downstream through `domain_echo` into common faction scalars is
unexamined. **Cross-lane FA/SE. Observation.**

### CIP-13 — The decorum operator: content-dynamic weighting
**EVIDENCED (as a consolidation) · NEW in v2 · net removal of machinery**

**Problem — Jordan, 2026-08-06:** *"Each venue will have its own weighting for rhetorical style that is dynamic to
the specific content being adjudicated in that phase. It is not a 1:1 mapping as that is too simple and obviates
the actual complexities of argument."*

Today `venue_w = role()[appeal] × R[appeal][tense] × tense_weight()[tense]` (`resolver.py:170-176` ✓), and its
**only** content input is `tense = Stasis.tense(ground)` (`:303` ✓), a fixed 6→3 lookup (`primitives.py:16-17` ✓).
Two different disputed *facts* weight logos identically, because the engine cannot see the claim — only its tense
token. A static appeal×tense matrix and a static venue triple are each **one-place functions of something that
classically takes two arguments.**

**Proposal — one owner, built from a primitive that already exists.** Generalise the existing binary relevance gate
— `Stasis.relevant` (`primitives.py:21` ✓) and `Dossier.available` (`:300-301` ✓) — from `{0,1}` to **graded**, and
it absorbs `RhetoricalWeights`, the venue tense trio, **and** CR4's +1D into a single owner. Three static objects
become one function. This is W4's answer too: graded relevance makes relevance **contestable**, which is the
classical *critical question*.

**C1 — temporal orientation becomes an orator's choice.** `Stasis.TENSE` is deleted; the move carries its own
orientation; the venue weighs the *combination* against the live content. You can argue future consequences in a
forensic case — the *koina* of past-fact and future-fact are common to all three genres. This dissolves the live
DEFINITION past-versus-present incoherence **by construction**: the rung stops carrying a tense at all. *(Falsifier
run: `Stasis.tense`'s only non-test reader is the weight path ✓ — the deletion is clean.)* **This is a proposal,
not a finding:** the two axes become independent because we propose to make them so.

**Classical framing, and it is not decoration.** Two lenses reached this slot from opposite directions — a salience
function `f(proof-type × appeal × temporal, live question, judge)` from Quintilian's status theory and *Rhet.*
I.15's **conditional** treatment of each inartistic proof; and ***decorum***, fitness between speech and (speaker,
subject, hearer, occasion). **They are the same slot reached from two directions, not the same object** — `f` has
no speaker and no occasion argument. But the point stands: **a 1:1 venue→style table is *anti*-decorum**, because
decorum is defined by taking more than one argument.

**One asymmetry the operator must preserve.** An item's *weight* stays engine-fixed and hidden (the atechnic rule,
CIP-2); only its *relevance to the live question* is graded. **A judge does not make a ledger more authentic — they
decide whether it bears.** Different quantities; the operator must not merge them.

**Also retired here:** the **`hard` verb.** Byte-identical to `advance` after the gate, costs 5 Reserve against 3
(`primitives.py:51` ✓), risks an immediate barred-device clinch, and `agon_harness.py:327` sells it as "a bigger
swing" — **strictly dominated with false UI copy.** Its classical name is *auxesis*, amplification, a **magnitude**
operation it does not perform. Amplification is the one *koinon* with no owner anywhere in the tree; its home is
CIP-5's stakes dials, not a verb variant.

**The liability, priced.** Mechanism count falls; **parameter count rises sharply** — `f` is a large authored
surface replacing twelve `[SEED]`s. **An explicit cell-count bound and a day-one structural check are part of this
proposal, not a follow-up** — the discipline CIP-2's Fork B had and this would otherwise lack.

**Falsifier.** Falsified if any consumer needs `tense` as *stored* state independent of the live rung and of a
move-chosen orientation; and falsified as a *consolidation* if the authored cell count exceeds its declared bound.

### CIP-14 — The audience as a party: taste, pressure, and memory
**CONDITIONAL on CIP-9b · NEW in v2 · the programme's headline, and its most conditional item**

**Problem — Jordan, 2026-08-06:** audiences press on the characters *and* on the adjudicator, *and* "carry out
their impressions of the characters after the social contest in the world in terms of reputations/respect/feelings."

**Two of three channels are already wired**, which is the good news and was verified: → character, `Room` feeds
`Readiness` (`resolver.py:314` ✓); → adjudicator, `Pressure` feeds `_bias` (`:291-293` ✓) **and raises `leak`**
(`:304-305` ✓), so a public gallery loosens the judge from the institutional standard toward personal character.
**→ world: absent.**

**Proposal.**

*(a) The crowd has taste (Q3).* `Room` is two per-side capped floats built only by pathos (`primitives.py:232-236`
✓) — taste-free approval. Give the venue a **crowd profile**: what *this* room finds convincing, distinct from the
bench's. **A config row, not a track** — it does not move during a bout. Once the gallery has taste distinct from
the bench, **playing to the crowd and playing to the judge become different actions**, and the gap is playable.
Classical, not modern: *thorubos* is crowd clamour with its own preferences, and *Rhet.* III.1's claim that
delivery has most power before crowds only means anything if crowds weigh differently from benches `[MED]`.

*(b) The room remembers (W5).* At close, the room's impression of each speaker emits to the ledger, **bounded by
presence** — only factions with someone in the room learn anything. That is the classical *fama*, and it makes *who
attends* a decision. Storage and holder dimension: CIP-1(d). Currency: CIP-12.

*(c) The bench presses back (W6).* **Corrected from the companion:** I claimed `Adjudicator` has "no authority of
any kind" and that pressure is "a one-way arrow into the bench." Both were overstated — juror `discipline` is
explicitly repurposed as bench-weight, "institutional rank/rigor" (`resolver.py:109-118` ✓, ED-1057), and
`SelfGating.licit` gates a contestant's move on `adj.learned`/`hostile` (`:357` ✓). **What is genuinely absent is
cross-contest authority** — a king versus a regional governor. Its interesting consumer is not difficulty but
**reach**: a king's ruling emits a Precedent that binds widely and lasts; a governor's is local and expires. That
carrier does not exist and is CIP-1(d).

**The result, and its condition.** Verdict and reputation route through different profiles to different consumers,
so **you can lose the case and win the room.** That is a real choice-shape — argue to win, or argue to be seen —
and it would supply the foundational choice `04` found missing.

**It is conditional on four things, and v1 stated none of them:**
1. **CIP-9b ratified** (C-11). Without it the two-output close is either inert in expectation or an exploit.
2. **Bench taste and room taste authored to diverge.** If they never do, the choice is a content dependency wearing
   a mechanic's clothes — exactly the caveat CIP-2's Fork B carries and this must carry too.
3. **A reputation economy with stakes comparable to the verdict** — the unbuilt ledger work of CIP-1(d).
4. **CIP-12's ruling**, so this is one currency with two holders rather than a third.

**Falsifier.** Falsified if any two of the six prior cells are always equal across authored content — then the 3×2
is symmetry aesthetics, not structure. Falsified as a *choice* if a sweep shows the argue-to-win line is also
argue-to-be-seen-optimal in >90% of authored venues.

### CIP-15 — The question substrate: rung vocabularies, and genre decomposed
**EVIDENCED · NEW in v2 · net removal of machinery · NEEDS JORDAN (collides with ED-1062 and CR4)**

Two cuts against the same doc-side grid, both retiring stored axes into venue configuration.

**(a) Per-venue rung vocabularies.** The gate is classical and free; the **six-rung total order is a category
error** — four forensic *staseis* (questions about an act already done, plus a procedural escape) welded to two
deliberative grounds into one order (`primitives.py:14` ✓). The symptom was found independently: JURISDICTION is
ruled *pre-merits* yet sits fourth, reachable only mid-merits and outrankable by CONSEQUENCE. **One gate mechanism;
rung vocabulary as a config row** — forensic {conjecture, definition, quality}; deliberative {feasibility,
advantage, honour}; negotiation {existence, definition, valuation, authority}. The CONSEQUENCE/FEASIBILITY merge
becomes within-vocabulary housekeeping, with the classical seam named: *can we* (the *koinon* of the possible)
versus *should we* (advantage) genuinely differ, and reopen if `settle()` needs a "you cannot deliver this"
challenge.

**(b) *Translatio* extracted.** The one classical move whose subject matter *is* a contextual dimension. Canon
already picked the clean horn — "if circumstances change enough to shift the adjudicator type … the current contest
ends and a new contest begins" (`social_contest_v30.md:39` ✓) — while the kernel implements *neither* horn: nothing
consumes a JURISDICTION win as a forum change, and `parliamentary_stay.py` has **zero campaign callers** ✓. Make it
a pre-merits window that terminates and re-instantiates.

**(c) Genre decomposed.** Genre is a projection of `hearer_role × question_tense × verdict_standard`. Classically it
is derived from the hearer's role and the question's tense — **an advocate in court does not choose to be
deliberative** — and mechanically CR4 already makes it a function of stasis, with genre inert on seven of eight
proceedings. Epideictic returns **for free** as a venue row (spectator hearer, no verdict) rather than needing a
third genre. **Caveat, and it is ours:** CIP-13 deletes `Stasis.TENSE`, so `question_tense` must be re-founded on
the venue's temporal weights, not on a rung tag — the kill survives on the independent argument, the decomposition
needs its middle term rehomed.

**Falsifier.** Falsified if any consumer reads genre for something not recoverable from the three parents. Two
independent passes found none; a third finding one kills it.

---

## §3 — Sequencing, and the add/cut ledger

### 3.1 Add/cut ledger — stated because the standing criticism is that this programme grows

| | Removes | Adds |
|---|---|---|
| CIP-3 | `ProofBar`, `GraceThreshold`, two biased starts, `use_tracker` tri-state | one Venue field |
| CIP-4 | four flat dice, Momentum-as-purchase | nothing (uses ratified δσ) |
| CIP-9a | the three-mode tripartition | nothing |
| **CIP-13** | `RhetoricalWeights`, the venue tense trio, CR4's +1D, `Stasis.TENSE`, the `hard` verb and its gate | one graded function (large parameter surface — bounded, §CIP-13) |
| **CIP-15** | the six-rung total order, genre as a stored axis, Style/Orientation with it | config rows |
| CIP-0 | ~300 lines of head special-casing | nothing |
| CIP-2 | orientation bit, Doubt Marker | claim-graph state, warrant schemes |
| CIP-1 | nothing | ledger fields, mount points, holder dimension, reach |
| CIP-14 | nothing | crowd profile (config), fama emission |

**Three of the four v2 additions (CIP-13, CIP-15, and CIP-12's reconciliation) are net removals.** CIP-14 is the
genuinely additive one, and it is the most conditional item in the programme. That is deliberate: the companion
document was correctly judged net-additive against a pruning brief, and the repair is to make the *additions*
consolidations.

**Not reconciled, and it should be:** `04` ruled the irreducible primitive set is **eleven**. This programme has
never been counted against that ruling. **Fork §4.9.**

### 3.2 Waves

| Wave | Items | Rationale |
|---|---|---|
| **0** | Bug batch (ED-SC-0022), CIP-0 | Nothing else is writable against the current head |
| **1** | **CIP-1**, CIP-4, **CIP-13** | CIP-1 is the highest value-to-cost item and the precondition making consolidation safe; CIP-4 closes a Jordan item with no new number; CIP-13 is the largest single removal and unblocks C1/W4 |
| **2** | CIP-5 (writ), CIP-10 (legibility) | Together they close clause (ii); CIP-5 consumes CIP-1's record as its stakes object |
| **3** | CIP-3 *(Jordan)*, CIP-15 *(Jordan)*, CIP-6 | The EV-only and stored-axis retirements, plus opposition memory once factions have a record to read |
| **4** | CIP-2 **after both sweeps**, CIP-7a | The largest engineering item must not precede its evidence |
| **5** | CIP-9b *(Jordan)* → **then** CIP-12 *(Jordan)* → **then** CIP-14 | Strict order: CIP-14 is unsound before CIP-9b, and ambiguous before CIP-12 rules the currency question |
| **6** | CIP-8 (gated on settle), CIP-9a, CIP-7c | CIP-7c also settles `split_standing`'s fate |
| **Held** | CIP-7b | Paper-prototype; human literature check before Jordan rules |

---

## §4 — Forks needing Jordan

1. **CIP-3** — burden as a Venue field (Fork A, ED-SC-0020). 2. **CIP-7b** — the repudiation branch.
3. **CIP-9b** — amends ratified doctrine, and now gates CIP-14. 4. **CIP-12** — is the second currency one axis
with two holders, or three things? 5. **CIP-15** — collides with ED-1062 and CR4. 6. **Leak's destination** under a
noisy gallery: the judge's private character (today) or the room's taste? 7. **C3's scope** — is the declared end
mechanical or flavour? 8. **Reserve** — `support` costs 2, regains 4, *and* builds ethos (`primitives.py:51-52`,
`resolver.py:331-332` ✓): fix cost ≥ regain, or cut the resource. 9. **Reconcile the programme against `04`'s
eleven-primitive irreducible set** — never done. 10. **Adjudicator authority: level or gap?** The level effect is
recommended; the gap is *not* asserted — inventing a divergence term because it sounds right is the failure this
document is written against.

**Cross-lane commitments, marked as observations:** **SE** — CIP-1(d)'s holder dimension and reach carrier change
settlement-ledger semantics. **FI** — CIP-2's evidence producer requires `investigation.py`, currently all stubs.
**FA** — CIP-7c(d) and CIP-12's downstream. **Characters** — CIP-5(6)'s conviction hookup.

---

## §5 — What this programme does not address

- **Whether any of it is fun.** Unanswerable from inside. Prototype the contest loop on paper with twenty claims
  and four bodies before writing more code.
- **`settle()` itself.** CIP-8 gates the fold; it does not design the mechanism.
- **The claim corpus.** CIP-2's anti-collapse property is a **content dependency**. Structural clauses are
  script-checkable; whether a clue's *prose* conveys its structured content to a human is certifiable only by
  playtest. Any pipeline claiming that part is automated is overclaiming. **The same caveat now binds CIP-14(2).**
- **Godot binding.** The descriptor roster is in flux; nothing here binds fields.
- **The eleven-primitive reconciliation** (fork §4.9).

---

### Audit trail

`[METHOD: four read-only Fable precedent lenses, two analysis lenses (orthogonality/state-graph; duplication vs
classical warrant), then three adversarial Fable critics (valoria-critic — Read/Grep/Glob only, so independence is
structural rather than declared). Opus authorship. Model tiering per CLAUDE.md §10.]`

`[SELF-AUTHORED — bias risk] The lenses were briefed by the orchestrator that synthesises them, and the briefs
named specific precedents, so a finding may be present because the brief pointed at it. Mitigations that fired:
per-claim confidence tags surfaced that the Fork B recommendation rests partly on a [MED] reception claim; required
NULLs produced the most decision-relevant output in the pass (Lens C's Q5); and the v2 critics broke four claims
including the previous headline. Residual risk is concentrated in reception and classical-locator claims, which no
lens could verify.`

`[NULL: no published precedent for mechanised principal-repudiation (CIP-7b); none for a concealed willingness
scalar probed as play (CIP-6); none for burden-of-proof as first-class UI (CIP-10d); none for an AI conceding
mid-debate as a discrete move (relocated to CIP-8); no shipped faction AI using lookahead; no published game
stating E[auto] ≈ E[played] as an explicit constraint (CIP-9b is ours); no world producer of evidence anywhere in
our tree; no amplification owner anywhere in our tree.]`

`[CONFIDENCE: high — every file:line marked ✓ (~25 re-verified by two independent critics, zero misquotes); the
corrections in §0.3; the consolidation and cut recommendations. medium — precedent-derived design verdicts, which
inherit their sources' tags; the classical doctrine. low — classical locators; any implementation-effort estimate.]`

`[WHAT v2 CHANGED: five new corrections (C-8..C-12), of which C-8 retracts a headline claim and C-11 makes CIP-14
conditional on unratified doctrine; the requirements frame added as §1 and made the grading standard; the
consolidation instrument given two mandatory riders after audit found it licensed rescuing anything; CIP-2
strengthened by retiring the need for the withdrawn matrix rather than shrinking it; CIP-12 reframed from a
proposal into a reconciliation of three unreconciled currencies; three new proposals (CIP-13, CIP-15, and CIP-7c),
two of which are net removals; CIP-14 added carrying the headline result and all four of its conditions; an
add/cut ledger added because the standing criticism was growth.]`
