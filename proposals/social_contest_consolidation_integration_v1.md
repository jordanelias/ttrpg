# Social Contest — Consolidation & Integration Proposals (v1)
## Ten proposals, each grounded in acclaimed precedent

## Status: PROPOSED — CIP-1..CIP-10 filed for ratification; CIP-3, CIP-7b and CIP-9b need Jordan
## Date: 2026-08-06 · Lane: SC · IDs: ED-SC-0023 (program), ED-SC-0024 (duality-constraint refinement)
## Depends on: `audit/2026-08-06-social-contest-three-lens-audit/` (findings, comparison, working records)
## Method: four read-only Fable 5 precedent lenses (record spine · argument loop · opposition & authority ·
## consolidation & legibility) per CLAUDE.md §10; Opus synthesis. Precedent claims are model-knowledge,
## not searched — see §0.3 on how that constrains what may be ratified from this document.

---

## §0 — How to read this, and what it corrects

### 0.1 The governing result

Four independent precedent lenses converged on one principle, arrived at from opposite ends. Lens B
derived it from Burning Wheel's failure; Lens D derived it from the difference between Into the Breach
and Ubisoft open-world design. Stated once:

> **Two configurations of one engine are distinct scenes if and only if (i) a competent player's best
> action sequence differs between them — the parameters change *policy*, not just expected value — and
> (ii) the player can tell, before acting, which configuration they are in.**
>
> Fail (i) and you shipped a reskin. Fail (ii) and you shipped noise — a policy difference the player
> cannot see reads as randomness, not as a different institution.

The consequence that reorganises this whole programme: **Constraint C1 (verb collapse) and the
thrice-flagged interface gap are the same principle observed from two sides.** The uploads treat them as
separate problems — a mechanics problem in §4 and an unclosed gap in the audit trail. They are one
problem. That is why CIP-5 and CIP-10 are load-bearing rather than polish, and why every proposal below
carries a legibility clause instead of deferring it.

### 0.2 Four corrections to our own prior documents

Recorded before the proposals, per §0.1 discipline, because each changes a recommendation we already made.

**C-1 — My anti-collapse principle was necessary but not sufficient.** `00_synthesis.md` §2.2 states that
options must "differ in what they CHANGE about the state, not in magnitude." Lens B refutes the
sufficiency using Burning Wheel against itself: Avoid, Obfuscate, Feint and Incite *do* alter different
state (defence pools, obstacles, tempo) and collapsed anyway, because the win condition cashes every
state change into **one currency** (Body of Argument). Every verb acquires an exchange rate; the two best
rates dominate. **Corrected principle:** verbs stay non-dominated iff the best verb varies per
decision-instant with observable changing state, **and** the close contains no common scalar into which
all verb effects convert at fixed rates. CIP-2 exists because of this correction.

**C-2 — Our kernel does not already satisfy the corrected principle.** Lens B credited Model B with four
currencies. It does not have them. Every win condition — `ThresholdRace`, `TallyAtClose`, `ProofBar`,
`GraceThreshold`, `PersuasionTrack`, `VoteAtClose` — reads `s.adv` and nothing else
(`resolver.py:52-145`); Standing and Room feed `Readiness`, which *multiplies into the gain that becomes
`adv`* (`:314-316`). They are inputs that convert, not currencies that score. The kernel has **one
scoring scalar plus one orthogonal terminal condition** — the fault/clinch catalogue, which ends a bout
regardless of `adv` (`:438-442`). That clinch path is the seed of a second currency and the only thing in
either model that does not cash into the track.

**C-3 — M2 Scope is not the safe borrow I called it.** `02_system_vs_proposals_overview.md` §VII ranks
M2 Tier A ("adopt; no substitute exists"). Lens C returns a hard NULL on its central branch: **no
published game implements mechanised principal-repudiation of an agent's over-mandate live commitment** —
an instrument that goes live, the counterparty acts on it, and the agent's own principal later disavows
it while the counterparty keeps what was transferred. The nearest cousins all fail on timing
(authorisation refused *before* effect — Suzerain, CK council) or on actor (the principal reneging on its
own promise, not disavowing an agent — EU4/CK3 call-to-arms). The mandate *gate* is well precedented; the
repudiation *branch* is historically grounded (treaties signed *sub spe rati*) and mechanically unshipped.
CIP-7 splits the proposal along exactly that seam.

**C-4 — "No opposition model" undersold what exists.** Lens C found the Church's action chain
(`faction_action.py:294-312`) is a genuine fixed, ordered agenda gated on Mandate thresholds, and
`faction.fixed_lean:20` is a hardcoded red line. What is missing is **memory, patience, and a voiced
reason** — not belief. This materially cheapens CIP-6.

### 0.3 Epistemic status of the precedent claims — read before ratifying anything

The four lenses had no web access. Every precedent claim is model knowledge, tagged `[HIGH]` / `[MED]` /
`[LOW]` at source. This document propagates only claims tagged `[HIGH]` or `[MED]`, and marks where a
proposal leans on a `[MED]`.

Three consequences that bind ratification:

1. **Reception claims are softer than mechanism claims.** "Feature X exists in game Y" is reliable;
   "players found X trivialising" is recalled community consensus with no citation available. CIP-2's
   Fork B recommendation leans partly on such a claim (the DXHR augmentation discourse) and is therefore
   marked conditional.
2. **A NULL over one model's knowledge is not proof of absence.** Lens C's Q5 null is load-bearing for
   CIP-7. Before Jordan rules on M2, that null is worth one human check against negotiation-game
   literature. It is cheap and it de-risks the single largest novel mechanic in the programme.
3. **Survivorship bias runs one way.** Lens D found no case where engine-side consolidation with
   policy-distinct, legible parameters produced sameness — but failed consolidations that never shipped
   are invisible to this method. Treat the discriminating test as a strong heuristic, not a proof.

Two items were **rejected on inspection** rather than used, which is the discipline working: Dragon Age II
(reused environments = content budget, not systemic consolidation) and Mass Effect 2 (broadly successful
streamlining; the criticised loss was build diversity, a decision-structure loss, not scene sameness).
Using either as an anti-consolidation argument would have been a category error.

---

## §1 — The proposals

Each carries: **Problem · Precedent basis · Proposal · What it consolidates or integrates · Cost ·
Risk class · Falsifier.** Risk classes are **EVIDENCED** (recombination of shipped, mostly-praised
mechanics), **CONDITIONAL** (evidenced but leaning on a `[MED]` reception claim or a stated gate), and
**NOVEL** (no published precedent found — prototype before spine status).

---

### CIP-0 — The canonical head describes the engine that runs
**Risk: EVIDENCED (doc hygiene) · Prerequisite to CIP-1..10**

**Problem.** `social_contest_v30.md` specifies a resolution loop with no engine; the kernel runs a
different loop with no canonical prose. They overlap only at the Persuasion Track's band thresholds. Every
proposal below is unwritable against a head that describes a game we did not build.

**Proposal.** Rewrite §§3–5 to describe the kernel's loop — stasis grounds, appeals, the reserve economy,
evidence dossiers, faults and clinches, readiness/resonance/leak, pressure — and demote Model A's exchange
algebra to a historical note. Move all per-proceeding difference into the config rows that already exist
in `modes.PROCEEDINGS`.

**What it consolidates.** ~300 lines of special-casing; the three-model structure collapses to one
described model plus a deprecated stub scheduled for deletion.

**Falsifier.** After the rewrite, a reader given only the head should be able to predict the outcome
distribution of a seeded bout. If they cannot, the rewrite failed.

---

### CIP-1 — The Record spine, and the discovery that it is the *identity* mechanism
**Risk: EVIDENCED · The highest value-to-cost item in the programme**

**Problem.** Every wired contest output is a stat delta. One arc-scoped boolean is the only thing that
guards a later transition anywhere in the loop.

**Precedent basis.** Lens A across Nemesis, CK3 Hooks, EU4 casus belli, Oath's Chronicle, Fallen London
qualities, Pentiment, Wildermyth, TI4 laws, King of Dragon Pass. Lens D independently, from the
consolidation side.

**The finding that reframes this proposal.** Lens D, asked what carries Church Tribunal's identity apart
from Guild Arbitration if both become config rows, returned something sharper than expected:

> The sameness risk is **already realised, and not by the config rows**. When everything downstream is a
> scalar, the two proceedings *are* the same scene regardless of how bespoke their resolution is. Distinct
> proceedings mean distinct **emittable record types**.

So the Record is not only the memory fix. It is the mechanism by which consolidation is safe at all. That
inverts the usual objection: consolidating proceedings onto one engine is *less* risky after CIP-1, not
more.

**Proposal.**

*(a) Mount points.* Add `ledger: list` to `Faction` and to the contest `Body`. `ledger.py`'s functions are
already free functions over a plain list (`ledger_add(ledger, tag)`), and `Settlement` merely holds one —
so this is **additive, not a refactor**. No ledger exists outside settlements today (verified).

*(b) Four fields, from what recurs across every precedent.* Extend `LedgerTag`:

| Field | Why | Precedent |
|---|---|---|
| `source` — event id + human-readable cause | **The field that makes a record read as memory rather than as a stat.** You cannot narrate `("Grudge","varfell",1.0)` | Nemesis (the orc recites what happened), CK opinion modifiers, KoDP advisors, Disco Elysium |
| `parties` — holder and bound | A Grudge with no aggrieved party and a Debt with no creditor cannot be invoked by the right entity, nor transferred on succession — which §6.1's own interruption rule already requires | CK3 hooks, Burning Wheel compromise |
| `uses` / consumable | TTL cannot express "discharged by being used" | CK3 weak vs strong hooks, EU4 claim spent by conquest |
| `superseded_by` | See the bug below | TI4 laws repealed by later vote |

*(c) Fix a latent bug this exposes.* `ledger_add` **replaces in place** on `(kind, key)` collision
(`ledger.py:54-57`). For `Reputation` that is intended. For a `Precedent` it is a silent history-eater: a
later ruling on the same matter would erase the earlier one rather than supersede it — destroying exactly
the citable record the whole proposal exists to create.

*(d) Emission.* Contest close emits: a `Precedent` on a Decisive/Total band; a `Debt` for an Obligation
(Compact was already ruled a Debt subtype, ED-IN-0046 D3); a `Grudge` on violation. **And a record for the
loser, priced by margin** — a narrow Track-4 loss leaves a larger citable residue than a Track-1 rout.

*(e) Consumption — ship at least one consumer per kind, at the same time.* Restore the `tribunal.py`
prerequisite that was cut as "not yet ported"; make Let It Ride enforceable; give Recall's "named
precedent" an engine-side verifier; let faction stance read the ledger.

**The integration point is one dataclass.** `DomainEchoResult` carries only
`fires / affected_faction / affected_stat / delta / timing / notes` (`domain_echo.py:50-57`) — that is
mechanically why the Projection channel became a stat delta. But the vehicle already exists one layer up:
the `Key` emitted at `echo_transport.py:412-427` already assembles `payload{scene_id, outcome,
participants}` and a populated `causes[]`. **Provenance and parties are already being computed and then
discarded at the `DomainEchoResult` boundary.** Adding a `records: list[LedgerTag]` alongside
`stat_deltas` closes it.

**Rules imported from precedent, each binding on the implementation:**

1. **Put the guard on the consumer, the story on the record.** Requirements live on the verb (the
   `ledger_has` idiom we already have); narration lives on the tag.
2. **Costed bypasses, not walls.** EU4 permits war without a casus belli at heavy cost. A bypassable guard
   reads as politics; an absolute one reads as a menu lock. Our Obligation-violation path already has this
   shape for players.
3. **Scarce-and-heavy, or numerous-and-aggregated — never numerous-and-individually-gating.** This is the
   line between Nemesis (readable) and CK's opinion-modifier lists (the community's standing joke).
4. **Cap by slot structure, not by advisory.** ED-619's "cap active Obligations at 3" is a GM guidance
   note in a no-GM engine. Nemesis caps by hierarchy slots. Make it structural.
5. **Prefer discharge the player witnesses** — event-discharge, discharge-on-use, or supersession. Silent
   TTL sweep should never be a load-bearing record's only exit; memory that evaporates unobserved reads as
   a bug, not as forgetting.
6. **Supersession-by-later-proceeding is the parliamentary expiry** — and it makes *discharging the record
   itself a playable contest*, which gives Chain Contests something durable to chain besides a track
   position.
7. **A record with no truth value is still a record.** Pentiment's authority acts regardless of
   correctness; the world remembers what was *ruled*. Do not couple tags to a hidden ground-truth check.

**Anti-pattern we have already hit twice:** a record kind shipped without a producer/consumer pair.
`world.casus_belli` has readers and no producer; Obligations have a prose consumer and no engine. A third
instance would poison trust in the ledger concept itself.

**Falsifier.** After CIP-1, there must exist a seeded campaign trace in which a contest outcome in season
N changes *which branch fires* — not merely which number moves — in season N+k. If no such trace can be
produced, the spine is inert and we have built the anti-pattern a third time.

---

### CIP-2 — The close weighs a claim graph, not only a scalar
**Risk: CONDITIONAL (see §0.3 note 1) · This is the real content of Fork B**

**Problem.** Our four Styles produce identical state changes differing only in one upside-only scalar
(≤0.5σ), so the grid collapses to two viable picks.

**Precedent basis.** Lens B, and it changes what the fork is about.

The read-then-match family — pick the approach matching the interlocutor's revealed type — has **no
surviving instance under our constraints**. Deus Ex: Human Revolution is the closest published analogue to
our adjudicator armature and it *worked*, but only on three props we lack: each debate was bespoke content
consumed once `[HIGH]`; the opponent's lines varied per beat, so the mapping was line→response rather than
person→response `[MED]`; and the perfect read cost an augmentation slot, after which the discourse
consensus is that the debates were solved `[MED]`. **When the read is purchasable, the choice degrades to
a prompt.** DXHR never had to survive an AI opponent playing it twice; we do.

Alpha Protocol's escape hatch — **refuse to grade the answer**, so every stance branches into playable
consequences and being disliked has its own perks `[HIGH]` — is a real structural alternative but is
unavailable at a verdict. A tribunal has bands. *What is importable is the placement*: ungraded payoff
belongs at the **outcome layer** (the compromise band and the loser's Record), not at the verdict.

And the decisive correction (C-1): Burning Wheel's manoeuvres already differed in what they changed, and
collapsed anyway, because one currency priced them all.

**Proposal.** Adopt warrant × attack as the verb set, keep the armature as seasoning — **and add the
condition without which the fork changes the nouns and keeps the failure**:

> **The contest close must consume claim-graph state — which claims stand, which premises are severed,
> which pairs the body must weigh — and not only the accumulated scalar.**

Concretely, promote what we already have. The fault/clinch catalogue is the one thing in the kernel that
does not cash into `adv` (C-2). Generalise it from a terminal condition into a **second scored dimension**:
a contest closes on both the merits scalar *and* the standing of the claim graph, with the venue's
`DefeatCatalogue` deciding how the two compose. Upload 3's own `attack()` spec already says this —
"REBUT → both claims stand; body weighs them at resolution" — and Griftlands is the shipped evidence that
it survives an AI opponent and heavy replay, because its arguments *do things while they stand* `[MED]`.

**What it consolidates.** The orientation bit (dominated contest-wide) and the Doubt Marker (unimplemented,
and currently shipped inverted — CR5's cost half is wired while its entire upside is not) both retire into
attack structure.

**Cost.** Moderate. `EvidenceItem` already carries ground + appeal + hidden weight; `rebut` already exists
behind a venue flag. Adding `warrant` and splitting `rebut` into three kinds extends existing types.
Claim-graph state at close is the genuinely new engineering.

**Falsifier.** Two sweeps, both AI-vs-AI best-response over judge and venue distributions:
1. If Style-pick entropy under the armature alone stays high (no Style above 40% pick rate), the armature
   is sufficient and this proposal is wrong.
2. Implement the three attacks as pure `adv` deltas and re-run. Precedent predicts collapse to the two
   best exchange rates. If entropy stays high anyway, the claim-graph condition is unnecessary and CIP-2
   reduces to a verb swap.

**Neither sweep has been run. Do not ratify CIP-2 without them** — they would be the first actual evidence
anyone in this corpus has produced on the question.

---

### CIP-3 — Burden as a Venue field, replacing an EV-only parameter
**Risk: EVIDENCED · NEEDS JORDAN (this is Fork A, ED-SC-0020)**

**Precedent basis.** Lens D's test adjudicates Fork A directly. Applied to our eight proceedings:

| Parameter | Clause (i) — changes policy? | Verdict |
|---|---|---|
| Burden / win-condition family | Yes — changes what you maximise | variety-bearing |
| Fault catalogue (`allow_rebuttal`, `evasion_strikes`) | Yes — changes which moves are safe | variety-bearing (so sharply it currently kills a shipped policy, bug F4) |
| Proof weights | Yes — but only if Appraise surfaces them | variety-bearing **conditional on clause (ii)** |
| **`track_start` bias (Church 6 vs 5)** | **No — changes only expected value** | **sameness-bearing** |

That last row is the argument for Fork A stated in precedent terms. Our biased track starts are exactly
the parameter class that fails the test. Replacing them with a burden token **moves the row from the
sameness side to the variety side** — which is the same conclusion the audit reached from the mechanics
side ("a handicap changes expected value; it cannot express *silence convicts*"), now independently
supported.

**Proposal.** One `burden` field on `Venue` ∈ {ACCUSER, RESPONDENT, LOWER_STANDING, NONE}, with stall
semantics at close. Retire `ProofBar`, `GraceThreshold`, the two biased starts, and the `use_tracker`
tri-state machinery. **Keep the Persuasion Track** — its compromise band is the one thing burden does not
give, and ED-SC-0002 already composes band-as-magnitude with genre-as-channel.

**Legibility clause (mandatory — clause (ii)).** Lens D reports a near-NULL here: **no acclaimed videogame
renders formal burden of proof as a first-class UI object.** Ace Attorney is the nearest, enacting it
diegetically — the judge rules against the defence unless it produces something *now*. The synthesis, and
it is a synthesis rather than a lift: render burden as **gravity on the track** — a visible token on the
burdened side, plus an animated one-step slide against the burden-holder on every stalled exchange. That
makes "silence convicts" literally watchable.

**Falsifier.** After CIP-3, a player shown only the contest screen must be able to say who loses if both
sides stop talking. If they cannot, clause (ii) is unmet and the field is noise.

---

### CIP-4 — Setup advantage as δσ under the cap we already ratified
**Risk: EVIDENCED · Closes ED-SC-0005 with no new number**

**Problem.** Recall +2D, Corroborate +1D, Prep +1D and Findings +2D stack uncapped; with Momentum, the
prepared side wins exchange 1 at p ≈ 0.93 and takes a one-exchange Total Victory at p ≈ 0.62.

**Proposal.** Retire the four flat dice into the `Dossier` — which already has per-source exhaustion,
diminishing corroboration and a hard cap, i.e. every property they hand-legislate separately — and route
the residue through the δσ leverage channel under CR6's existing `M_MAX = 1.5σ` tanh cap.

**Why no new number is needed.** CR6 already ratifies that setup advantages "accumulate as δσ, tanh
soft-capped", and the kernel already enforces it. The doc's flat pool dice **violate the subsystem's own
ratified substrate** on precisely the channels KU-1 flags. ED-SC-0005 asks Jordan to invent a ceiling that
was ratified months ago.

**Legibility clause.** XCOM's pattern: the aggregate is always decomposable into a signed, itemised
modifier list on demand `[HIGH]`. Plus the board-game rendering, which is better here than any videogame
one — the track marker's position *is* the stacked advantage, with the saturating cap drawn as visibly
compressing segments near the rail. **A stacked deck the player can see is drama; one they cannot see is
unfairness.**

**Falsifier.** Re-run the stacking arithmetic post-change. P(win exchange 1) for a maximally prepared side
against an unprepared one should fall from 0.93 into a band Jordan finds acceptable, and no combination of
legal setup actions should exceed the 1.5σ ceiling.

---

### CIP-5 — The writ: stakes and dials announced before the roll
**Risk: EVIDENCED · New — in neither the uploads nor the audit**

This proposal did not exist before the precedent pass. It emerged from two lenses converging.

**Precedent basis — Lens D on Blades in the Dark.** The strongest "one resolution move, parameterised"
precedent in tabletop. Asked what carries the felt difference between scenes when the mechanic is
identical, Lens D confirms fiction and consequence-severity — and adds the load-bearing device we had
missed: **the parameterisation is spoken aloud before the roll.** The GM declares position and effect;
the player may negotiate the dials or trade one for the other before committing. The roll is deliberately
uniform *so that attention stays on the dials*. The dials are the scene. **Adopting Blades' math without
its announcement ritual takes the half that does not carry the variety.**

**Precedent basis — Lens B on Burning Wheel's Statement of Purpose.** Stakes are declared before the
mechanics run; the dice decide who gets it, not what "it" is. And a forcing null: *there is no functioning
no-GM game that determines the meaning of an outcome after resolution.* That job is always done by
pre-authored script or by a human at the table. **With no GM, the Statement of Purpose is not a
nice-to-have; it is forced** — the stakes must be machine-representable data before the dice.

**The synthesis.** Those two are the same object. A contest opens by emitting a **writ**:

1. **The stakes** — the *draft text of the Record* this contest will emit, validated for scope at open
   (which ties CIP-5 to CIP-1 and CIP-7: the Statement of Purpose is literally the pending `Precedent` or
   `Debt`).
2. **The dials** — burden placement, which faults are fatal here, exchange budget, the venue's legal
   texture.
3. **The coarse read** — the Appraise band on the adjudicator, rendered as a sentence, not a vector.
4. **The declared compromise axes** — what a partial outcome means *here*.

That fourth item closes a hole the audit found and did not fix. Burning Wheel's compromise works at a
table because a human improvises its content. Our Compromise band currently says "GM narrates partial
outcome proportional to final position" — GM fiat in a no-GM engine. Pre-declared compromise axes are what
make P41 Scaled Compromise executable rather than aspirational.

**What it integrates.** The writ is simultaneously the variety mechanism (clause i — dials are the scene),
the legibility mechanism (clause ii — the player sees which configuration they are in), the no-GM stakes
fix, and the entry point for the Record. One object, four problems.

**Falsifier.** Show a player two writs from different proceedings with the roll math hidden. If they cannot
say which room they are in and what losing costs, the writ is not doing its job.

---

### CIP-6 — Opposition: memory before intelligence
**Risk: EVIDENCED, except one component marked NOVEL**

**Problem.** Factions cannot obstruct across seasons and cannot concede. `faction_action.py:220` is a
single weighted `rng.random()` draw per season with no cross-season state.

**The precedent finding that makes this cheap.** Lens C: **no shipped faction AI in any surveyed game
achieves "obstruct then relent" via lookahead or planning.** Victoria 3, CK, EU4, Frostpunk, Total War —
all of them fake planning with **threshold predicates over persisted accumulators**, and it is enough,
because the *player* supplies the narrative of intent. So the fix for our memorylessness is **state and
predicates, not a planner.**

And per C-4, we are further along than the audit said: the Church chain is already a fixed ordered agenda,
and `fixed_lean` is already a red line.

**Proposal.** Add to `Faction`:

| Field | Precedent | Risk |
|---|---|---|
| `aims` — 2–3, **visible** | SMAC agendas, Civ VI public agendas, Vic3 ideology | EVIDENCED |
| `redLines` — unbuyable, announced, structurally bypassable | Vic3's unbuyable stances (praised); CK3 buyability (the C3 critique) | EVIDENCED — but **inert until a side-payment verb exists to refuse**; sequence after CIP-8 |
| `threat` — accumulator; **magnitude concealed, structure shown**, probed by truthful banded reads | EU4 coalition decay, Vic3 radicalism | **NOVEL in the concealment** — see below |
| `patience` — capability gate + accumulator | CK ultimatums fire on *military power* crossing a threshold, not on anger duration; Vic3 radicalism | EVIDENCED |
| `aim.expires_with` — dies with its holder | Old World, Kremlin's ageing Politburo, CK death-resets | EVIDENCED |

**What makes a faction feel like it believes something** (Lens C, four parts, and SMAC is the usual answer
because it has all four): the disposition function reads **public policy or record state, not a gift
ledger**; the preference is **immutable** (no payment moves the agenda, only the offending state); the AI
**pays for its belief**, running its preference even when suboptimal; and **the reason is voiced at the
moment of obstruction**, in character. That fourth is the cheapest and most valuable single addition here.
A concealed number plus a silent refusal is Civ VI, which was widely read as caprice. A concealed number
plus a truthful stated reason is poker with table talk, and it plays.

**Integration with CIP-1.** Rule 1 above says disposition should read *public record state*. That is
exactly the `LedgerTag` ledger — a faction whose stance reads Precedents and Grudges closes the loop the
record-spine trace shows dead-ending.

**The NOVEL component, flagged.** Concealing the willingness scalar and making probing it the play has no
published precedent in a single-player political sim. The known mitigation — truthful banded probes plus
voiced structural reasons — is exactly the pattern our own kernel already uses for evidence weights, so we
are not inventing the mechanism, only its application. Prototype the probe channel before committing.

---

### CIP-7 — Authority, split along the seam precedent actually supports
**Risk: 7a EVIDENCED · 7b NOVEL — NEEDS JORDAN**

**Problem.** A personal-scale contest win binds an entire faction with **no check that the character could
bind anyone**, and the only exit is breach. Meanwhile `faction_politics_v30.md` *consumes* Obligations in
its demotion table — a consumer for an object that does not exist.

**CIP-7a — the mandate gate. EVIDENCED; adopt.**
`bind(actor, body, terms)`: if `terms.within(mandate.limits)` → BOUND. Precedent is solid — Suzerain's
constitution as a gate on what you may do at all, CK crown-authority levels, John Company's offices where
most ventures require cooperation you do not personally hold. And precedent makes the risk *computable*
rather than a vibe: if the deliverable enumerates which bodies and offices it touches, and the actor's
standing in each, then `repudiationRisk` is arithmetic over data we already have.

**CIP-7b — the repudiation branch. NOVEL; do not spine it yet.**
This is C-3. A PROVISIONAL binding the counterparty acts on, later disavowed by the actor's own principal,
with the counterparty keeping what was transferred, has **no published implementation** in Lens C's
knowledge. It is historically excellent (*sub spe rati*; Versailles) and mechanically untested.

The risk is sharpened by our position: we would move from **no authority model** to **an authority model
with no published precedent** in one step, on the mechanic upload 3 calls the spine of the whole design.

**Recommendation.** Ship 7a. Paper-prototype 7b before it becomes load-bearing — which is upload 3's own
prescribed method for exactly this class of uncertainty. And run the one human literature check named in
§0.3 note 2 first; it is cheap and it either de-risks the largest novel mechanic in the programme or
confirms we are genuinely first.

---

### CIP-8 — Fold negotiation into the gate, gated on `settle()` existing
**Risk: CONDITIONAL — the gate is the whole proposal**

**Precedent basis.** Lens D is blunt: `gate(burden = NONE)` is only the **front half**. Upload 3's own S4
row terminates in `settle()` — reservation values, offers and counters, side payments, instruments, scaled
compromise — which is a genuinely separate mechanism the gate merely hands off to. Fold the proceeding
*without* building settle and precedent predicts the grey-engine outcome: negotiation-as-menu, the flat
one-shot diplomacy of most 4X games, where deals are outcome comparisons rather than a process `[MED]`.

The positive precedent is Griftlands: negotiation *can* share an engine, but it earned its distinctness by
owning **its own persistent state vocabulary** — arguments as targetable entities, resolve instead of
health `[MED]`. Our own kernel already agrees: `modes.py:13` says "Genuinely different sub-systems (dyadic
counsel, negotiation, ceremonial) remain scaffolds", and `NegotiationMode` is stub-wired with the docstring
"win = agreement in the overlap" — i.e. reservation values, named and unbuilt.

**Proposal, stated as a testable gate.** `burden = NONE` is ratifiable as *the* negotiation implementation
**when and only when** an offer / counter / side-payment verb set and a reservation-value ConcealedValue
are in the move vocabulary. Before that, the fold is a rename and should be described as one.

**Where the concede verb goes.** Lens C rates a mid-argument AI concession *move* as thinly evidenced —
compromise-as-outcome-band is universal, concession-as-in-loop-move is not. Precedent places it as an
**inter-exchange settlement offer** (the S4 subroutine), not a new in-loop move class. This also corrects
the audit's §4.4 item 3, which proposed it as a move in the kernel vocabulary.

---

### CIP-9 — Retire the tripartition; refine the fidelity constraint
**Risk: 9a EVIDENCED · 9b NEEDS JORDAN (amends ratified doctrine, ED-SC-0024)**

**CIP-9a — retire the three-mode TTRPG/BG/Hybrid framing.** Football Manager does not keep three rulebooks
for full match, commentary and instant result — one engine, three views `[MED]`. Our own Auto/Manual
doctrine already ratified "one engine at two fidelities." The tripartition is a tabletop inheritance that
duplicates specification and changes no mechanics to remove. No precedent argues for keeping it.

**CIP-9b — refine `E[auto] ≈ E[played]`.** Lens D supplies a correction to a *ratified* constraint, so it
is filed for Jordan rather than folded in.

The constraint is right in intent (anti-mode-shopping) but underspecified in its baseline. In Football
Manager a watched match diverges from an unwatched one exactly by the manager's live interventions, and
that divergence is legitimate — it is the **skill premium**, expressed through the same verb set `[MED]`.
Total War is the cautionary pole: two separate resolvers held together by calibration, and the community
finds and exploits the seam `[MED]`.

**Proposed refinement:** the parity harness should measure `E[auto]` against **AI-vs-AI played**, not
against expert play, and treat player skill above that baseline as a feature rather than a calibration
violation. Our canon already says the auto path "resolves through NPC AI" — so this is arguably making
explicit what was meant.

Two further precedent notes worth carrying: Football Manager achieves parity **by construction** (views of
one simulation) rather than by calibration, which is the shape Fork A already chose and should not drift
back from; and XCOM 2 ships **no** auto-resolve `[HIGH]` because its outcome surface is high-dimensional —
a fabricated permadeath is unacceptable. **Auto-resolve is viable only where the outcome surface is
low-dimensional.** Our five-band close plus echo deltas plus record emissions qualifies. Keep it that way:
the more per-scene state a played contest generates, the harder honest auto-resolution becomes.

---

### CIP-10 — The legibility layer
**Risk: EVIDENCED for three of four surfaces; the fourth is a synthesis**

**Problem.** Flagged in all three uploads and our own audit; closed by none. Per §0.1 this is not polish —
it is clause (ii) of the discriminating principle, i.e. half the variety mechanism.

| Surface | Precedent | Pattern |
|---|---|---|
| **(a) The accumulated record** | Return of the Obra Dinn's book `[HIGH]`, Frostpunk's Book of Laws, CK3's hooks panel | Diegetic, auto-populated at observation, cross-linked — and critically, **it visibly banks**: entries change state the instant they become verified. A `LedgerTag` should visibly change state when it starts guarding a transition. "This Precedent is now citable in Guild Arbitration" is Obra Dinn's ink-fill moment |
| **(b) The adjudicator read** | Disco Elysium's skill voices `[HIGH]` + Ace Attorney's penalty meter `[HIGH]` + Blades' pre-commitment announcement | Surface internal numbers as *characters who speak*: "Empathy: the Inquisitor has stopped listening." Delivers a coarse read without printing the vector. **Do not use CK3's exact-number tooltip here** — an exact read collapses the concealed-value game the kernel is built on |
| **(c) The stacked advantage** | XCOM's itemised shot breakdown `[HIGH]`, Into the Breach / Slay the Spire outcome previews `[HIGH]`, Victoria 3's nested tooltips `[MED]` | Aggregate always decomposable into a signed itemised list on demand; the **top-level summary must carry the read**, tooltips carry the audit. Vic3's standing criticism is that tooltip archaeology substitutes for legible top-level design |
| **(d) The burden** | Near-NULL — no acclaimed videogame renders it as a first-class UI object; Ace Attorney enacts it diegetically | Gravity on the track: a token on the burdened side, an animated slide against them on every stall. Flagged as **synthesis, not lift** |

**One rule across all four, from Blades:** the read is announced **before commitment**, not revealed in a
post-mortem. That is why CIP-5 (the writ) is the delivery vehicle for most of this layer.

---

## §2 — Sequencing

Ordered by dependency and by shared surface, not by interest.

| Wave | Items | Rationale |
|---|---|---|
| **0** | Bug batch (ED-SC-0022), CIP-0 | Mechanical; F1 is the difference between Stage 3 existing and not existing in the product. Nothing else is writable against the current head |
| **1** | **CIP-1** (Record), CIP-4 (δσ stack) | CIP-1 is the highest value-to-cost item *and*, per Lens D, the precondition that makes consolidation safe. CIP-4 closes an open Jordan item with no new number |
| **2** | CIP-5 (the writ), CIP-10 (legibility) | Together they close clause (ii). CIP-5 consumes CIP-1's record as its stakes object |
| **3** | CIP-3 (burden — needs Jordan), CIP-6 (opposition memory) | CIP-3 retires the EV-only parameters; CIP-6 is cheap once CIP-1 gives factions a record to read |
| **4** | CIP-2 (claim graph) **after both sweeps**, CIP-7a (mandate gate) | CIP-2 is the largest engineering item and must not precede its evidence |
| **5** | CIP-8 (negotiation, gated on settle), CIP-9 | The Exchange cluster is the largest genuinely-new design; CIP-9a is a free cut whenever |
| **Held** | CIP-7b (repudiation) | Paper-prototype first; human literature check before Jordan rules |

---

## §3 — Risk register

The distinction that matters most, stated in one place.

**EVIDENCED — recombination of shipped, mostly-praised mechanics:** CIP-0, CIP-1 (all of it), CIP-3,
CIP-4, CIP-5, CIP-6 except the concealment component, CIP-7a, CIP-9a, CIP-10 (a)–(c).

**CONDITIONAL — evidenced but gated on a stated test or leaning on a `[MED]` reception claim:** CIP-2
(needs both sweeps; leans partly on the DXHR discourse), CIP-8 (gated on `settle()`), CIP-9b (amends
ratified doctrine).

**NOVEL — no published precedent found; prototype before spine status:** CIP-7b (principal repudiation of
an agent's live over-mandate commitment) — the headline risk, and the piece upload 3's entire
"can you deliver what you promise" thesis leans on; CIP-6's concealed threat magnitude; CIP-10(d)'s burden
rendering.

**Two nulls that are good news:** no shipped faction AI uses lookahead, so CIP-6 is predicates over state
rather than a planner; and Lens D found no case of engine-side consolidation with policy-distinct legible
parameters producing sameness — subject to the survivorship caveat in §0.3.

---

## §4 — What this programme does not address

Stated plainly so the gaps are not mistaken for coverage.

- **Whether any of it is fun.** Unanswerable from inside, as all three uploads concede. Upload 3's
  prescription remains the right next move and costs almost nothing: prototype the contest loop on paper
  with twenty claims and four bodies before writing more code.
- **The Exchange cluster as genuinely new design.** CIP-8 gates the fold; it does not design `settle()`.
- **The claim corpus.** CIP-2's anti-collapse property is a content dependency. The authoring invariant
  (closed visible domains, discriminating-chain reachability, the 40% distribution cap, guess-resistance
  ratio) is script-checkable in its structural clauses — but whether a clue's *prose* conveys its
  structured content to a human is certifiable only by playtest. Any pipeline claiming that part is
  automated is overclaiming.
- **Godot binding.** The descriptor roster is in flux; nothing here should bind fields yet.

---

### Audit trail

`[READ: the three audit documents in full; ledger.py, registry.py, resolver.py, primitives.py, modes.py,
dictionaries.py, policy.py, faction.py, wrapper.py, armature.py; domain_echo.py, echo_transport.py,
faction_action.py, season_manager.py, game_state.py; auto_manual_resolution_duality_v1.md; the four
uploads. Repo claims re-verified by the orchestrator at the file:line given.]`

`[METHOD: four read-only Fable 5 precedent lenses (valoria-critic — Read/Grep/Glob only), disjoint
mandates, no web access; Opus synthesis at max effort. Model tiering per CLAUDE.md §10 — fable on the
read-only reasoning nodes, Opus on authorship, which is the ruled split.]`

`[SELF-AUTHORED — bias risk] The lenses were briefed by the orchestrator that synthesises them, and the
briefs named specific precedents — so a finding may be present because the brief pointed at it. Two
mitigations were applied and both fired: the briefs required per-claim confidence tags (which surfaced
that the Fork B recommendation rests partly on a [MED] reception claim), and required NULL results
(which produced the single most decision-relevant output in the pass, Lens C's Q5). Residual risk is
concentrated in reception claims, which no lens could verify.`

`[NULL: no published precedent for mechanised principal-repudiation (CIP-7b); none for a concealed
willingness scalar probed as play (CIP-6); none for burden-of-proof as first-class UI (CIP-10d); none for
an AI conceding mid-debate as a discrete move (relocated in CIP-8); no shipped faction AI using lookahead;
no published game stating E[auto] ≈ E[played] as an explicit constraint (CIP-9b is ours).]`

`[CONFIDENCE: high — the corrections in §0.2, the repo integration points (all re-verified), and the
consolidation/cut recommendations. medium — the precedent-derived design verdicts, which are argued from
cases and inherit their sources' confidence tags. low — any estimate of implementation effort.]`

`[PASS-3: four precedent lenses run with disjoint mandates and required nulls; their outputs corrected
three of our own prior recommendations (§0.2) rather than confirming them; risk classes separate the
evidenced from the untested; two forks and one doctrine amendment held for Jordan rather than bundled.]`
