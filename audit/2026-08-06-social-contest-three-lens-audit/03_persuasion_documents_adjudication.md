# Documents 4 & 5 — Adjudication, Retraction, and Disposition

## Status: PROPOSED — findings filed; amends CIP-2 and ED-SC-0021 · ID: ED-SC-0025
## Date: 2026-08-06 · Lane: SC
## Method: three read-only Fable 5 adjudication lenses (Klei/interaction · the matrix retraction ·
## primitive triage) per CLAUDE.md §10; Opus synthesis. Sources now preserved at `sources/`.

---

## §0 — Why this document exists

Two further documents in the series arrived after `00_synthesis.md`, `02_system_vs_proposals_overview.md`
and `proposals/social_contest_consolidation_integration_v1.md` were filed. Document 5 is the newest.

They do not add to that work. **They undermine parts of it**, and the parts they undermine are ones I
recommended. Three findings, in descending order of consequence.

---

## §1 — The retraction: we endorsed a fabrication (P1, NEW)

**Document 4 retracts document 3's warrant × attack matrix in its own opening**, describing it as
"the one piece of the prior design that was invented rather than derived … correctly identified in the
last audit as fabricated and formatted to look rigorous."

**Our filed work endorsed it.** `00_synthesis.md` §5 Fork B recommends "warrant × attack, decisively";
`02_system_vs_proposals_overview.md:235` lists §6.2 among upload 3's "strongest contributions"; CIP-2 is
built on it.

**And the sharpest part — the tell was in our own text.** `02_system_vs_proposals_overview.md:118`
observes that the proposals "have no mechanism preventing a number from being invented." Nobody
followed that sentence to §6.2. This repo makes anti-fabrication a core discipline (CLAUDE.md §0) and
we imported a fabricated payoff table into a recommendation without checking its provenance. Doc 4
credits "the last audit" with catching it; **that audit was not ours.**

### 1.1 What was actually fabricated — the distinction that saves most of CIP-2

| Layer | Status |
|---|---|
| **The three-attack taxonomy** (Undermine / Rebut / Undercut) | **SOURCED** — Prakken's structured-argumentation trichotomy over Dung's frameworks, and it belongs to *upload 1's P7*, not upload 3. Cited twice in our own corpus |
| **The warrant-keyed vulnerability assignments** (WITNESS→Undermine-strong, DOCUMENT→Undercut-strong, …) | **UNSOURCED.** No repo surface records a citation for any assignment. A quantified matrix crossing warrant types with Prakken attack types is not a published result anyone has been able to name |

So the verb set survives; the payoff table does not.

### 1.2 Collateral: the 40% authoring invariant

The "no attack kind optimal for more than ~40% of the claim draw" check is part of the §6.2 apparatus.
It is cited in **five places** across our filed work (`00_synthesis.md:383,387-388`;
`02_…overview.md:236,444`; `…v1.md:570`) as an imported, checkable standard. Its provenance is now
orphaned. **It survives only relabelled as our own `[SEED]` threshold** — which is legitimate under this
repo's conventions, but must be labelled as such rather than cited.

### 1.3 Does the story model fix what the matrix was supposed to fix? No.

Document 4 offers the story model (Pennington & Hastie: coverage, coherence, uniqueness) as the sourced
replacement. Adjudicated against our own corrected principle C-1:

`acceptance = h(coverage, coherence)` is **a fixed scalarizer**. Inside `h`, coverage and coherence
convert at fixed rates — which is exactly C-1's defect one level down, and structurally identical to
what C-2 already found in our kernel, where Standing and Room feed Readiness which multiplies into the
gain that becomes `adv` (`resolver.py:314-316`). `confidence = k(uniqueness)` is a genuine second output
**only if something distinct consumes it** (e.g. confidence gating verdict *band* or record *strength*
while acceptance gates *direction*).

**Verdict: the story model does not satisfy C-1 by construction.** It satisfies it only under an
implementation discipline its own encoding does not force. Adopting it would not solve CIP-2's problem;
the corrected principle would have to be imposed *on* it, exactly as on the warrant table.

And document 4's own audit A2 concedes the deeper point: coverage/coherence/uniqueness are "not formally
defined" by Pennington & Hastie, so `g()`, `h()`, `k()` are the author's. **The invention moved from a
visible table into three function bodies where it is harder to see.** Both documents have the same
two-layer structure — sourced skeleton, invented quantification. The difference is *disclosure*: doc 4
discloses it in its own audit. Under this repo's regime that is precisely the licit/illicit line — an
invented number tagged `[SEED]` is legal working material; an invented number wearing a derivation is
fabrication.

The story model is nonetheless genuinely valuable for an unrelated reason: it is a theory of **how the
adjudicating mind scores**, which is the half our kernel models thinnest.

---

## §2 — The Klei refutation lands on our kernel (P1, NEW)

Document 4's finding A1 is the only piece of direct playtest evidence anywhere in this corpus. Klei
built conversation challenges as *spending resources to influence random rolls*, played it, found it
"a lot less fun than fighting," and replaced it with cards before shipping Griftlands.

**Adjudicated verdict: it hits our kernel squarely.**

Not element-for-element — three genuine differences exist (our `Reserve.spend` is an action *tax* rather
than a purchase of roll influence; evidence resolution is deterministic; the fault/clinch catalogue is a
real second terminal). But the *structure* Forbes describes is present: **a stationary, always-full
action menu resolving through a random roll into a single scoring scalar.** `VALID_KINDS` is a fixed
7-tuple offered every turn (`resolver.py:32`); every WinCondition reads `s.adv` (`:52-145`).

Three independent measurements converge: the audit's verb collapse, C-1/C-2's one-currency condition,
and the observable symptom that `logos_spammer` — the same move every turn, forever — is a viable
default sparring partner (`agon_harness.py:39`).

### 2.1 A live bug the refutation surfaced — F9

**`hard` is strictly dominated, and the UI misrepresents it.** It costs **5** Concentration against
`advance`'s **3** (`primitives.py:51`); after the `SelfGating.licit` gate the two verbs execute
**byte-identical code** — `deg = self._reception(...)` then `self._advance(...)` — with no kind-dependent
magnitude anywhere in `_apply` (`resolver.py:357-389`); and if the move is not licensed it is an
immediate barred-device clinch loss. The interactive harness nonetheless offers it as *"Press hard — a
bigger swing"* (`agon_harness.py:327`).

Spend more, get identically nothing, risk everything — wrapped in copy claiming otherwise. It is the
purest instance of A1's indictment, shipped inside our own verb set. Filed into the ED-SC-0022 bug batch
as **F9**.

### 2.2 What cards actually fixed — and why we do not need a deckbuilder

Decomposed: (a) randomized limited availability; (b) hand management / hedging; (c) persistent board
entities; (d) deckbuilding progression.

(a) and (c) are two implementations of **one operative property: non-stationarity of the per-turn
decision problem.** Cards inject it exogenously (a random hand); a persistent claim board generates it
endogenously (the correct verb depends on which claims stand). Our kernel has neither, which is why
constant policies are competitive. (d) carries none of the in-encounter fix and is the part that would
make us a deckbuilder — do not adopt it.

**The persistent-argument board is transferable independent of cards**, under two conditions:
*verb-coverage invariance* (every reachable board state must be reducible by generally-available verbs —
the lesson of Griftlands' documented eleven-turn deadlock) and *warrant diversity of the authored
corpus*. Our `EvidenceItem` already carries ground + appeal + hidden weight, and `rebut` already exists
behind a venue flag.

**Null, verified:** our kernel has no Griftlands-class deadlock. The bout is budget-bounded, every
WinCondition is total at close, and resource starvation cannot strand a side (a forced pass yields a
fault strike *plus* a regroup). Our failure mode is not eleven turns of nothing to do; it is eleven
turns of *the same thing* to do.

---

## §3 — Primitive inflation, and the re-distillation

Document 5's own independent-reviewer note says it: *"Fourteen mechanisms became fourteen plus eleven,
and now plus nine. The distillation of document 3 has been quietly undone."*

Re-running document 3's **own** separation rule over N1–N20 — *if it can be written as a row in a table,
it is not a mechanism* — recovers the discipline:

**20 N-primitives → 5 mechanisms.** N10 Deliberation · N5's inoculation half · N6 Anchor · N8 Escalation
(cross-lane) · N2 Story (a mechanism by form; rejected on merits). Fourteen of twenty are configuration,
duplicate, unspecified, or composition-wiring.

### 3.1 The short list — what genuinely earns a place

| Rank | Item | Composes onto | Why |
|---|---|---|---|
| 1 | **N10 Deliberation** | `VoteAtClose` + `Panel` | See §3.2. The highest-value item in twenty |
| 2 | **N16 Attribution** | CIP-1's record emission | See §3.3. A field, not a system |
| 3 | **N19 Composition wiring** | `Panel.members` | Prior play writes the bench. Near-zero mechanism cost; T1-citable (the *lex Aurelia* changed only who sat, after fifty years of contest) |
| 4 | **N3's durability half** | echo/record decay | The one thing doc 4's corpus-wide null says no surveyed game has |
| 5 | **N9 aims-on-members** | `Adjudicator` + CIP-6 aims | Feeds N10's influence channels. Content cost must be priced first |
| 6 | **N17 Supplication** | the `GraceThreshold` venue family | Half-built already; see §3.4 |
| — | N6 Anchor (T0), N7, N13 | earmarked behind `settle()` (CIP-8's gate) | Right mechanics, no machine to mount them on |

### 3.2 N10 is an extension of what we already ratified, not a replacement

`VoteAtClose` is a **one-shot terminal secret ballot**: per juror, `vote_A ⇔ sharpness·gap +
gauss(0,noise) > 0`, aggregated weighted-by-standing (bench weight = `discipline`, ratified ED-1057,
`resolver.py:122-145`).

N10 adds: **(1) first ballot** = exactly one sampling pass, *retained per-member instead of immediately
aggregated* — zero new state, a refactor of an existing loop; **(2) influence rounds** — majorities apply
informational *and* normative pressure, minorities informational only; **(3) acceleration** and
**(4) momentum with a first-crossing reversal** — parameters and a lock rule on that loop. The ratified
weighted threshold becomes the count rule *inside* deliberation, unchanged.

**Today's `VoteAtClose` is formally a degenerate zero-round N10.** That is the signature of an extension.

Two supporting facts from our own tree. `appraise_armature`'s four-band reveal (`appraise.py:140-177`)
pointed at `Panel.members[i]` instead of one adjudicator gives N10's "first defector is the highest-value
target" its read — same function, same ladder, no new information mechanic. And the deliberative-body
venue already flags cross-session verdict reversibility as strategic-layer-not-yet-built
(`modes.py:129-131`); N10's within-close momentum is its missing near-scale counterpart.

**The blocker is elsewhere and we should be honest about it:** `ContestView` — the read-only surface a
policy actually sees (`contract.py`) — exposes `audience_learned` / `audience_hostile` as *booleans*,
with no per-member view. And `Panel` **averages** member `discipline` and `character()` during the bout.
We author individual minds and then discard them at exactly the moment they would matter — including
fully-populated per-member character vectors (the inquisitor is `char_ethos=0.20, char_pathos=0.15,
char_logos=0.65`, `modes.py:286-288`) that `VoteAtClose` never reads.

### 3.3 N16 Attribution is the second currency C-2 asked for

Score **whether the target believes the decision was their own**, not whether they complied. Assessed
against C-1, it passes where coverage/coherence fail, for a structural reason:

1. **Its value realises in a different subsystem at a different time.** Merits pay at close; attribution
   pays downstream — breach probability of an emitted `Debt`, `Grudge` magnitude, opposition patience.
   A close-time exchange rate cannot be fixed, because attribution's price depends on state the close
   cannot see. That is the same argument C-2 accepts for the clinch path being a real second currency.
2. **It is anti-correlated with `adv`-maximal play at the margin.** The merits-maximal line — public
   crushing, maximal margin — is plausibly attribution-*minimal*. A currency you sometimes buy by *not*
   spending the other is exactly C-1's signature.
3. **It has consumers already on file.** CIP-1(d) prices the loser's record by margin; attribution
   refines it — a narrow loss the loser *owns* emits a smaller Grudge than a rout.

**Two binding caveats.** Wire it as an additive close-time term and it collapses into the scalar like
everything else; it stays a currency only if its consumers are strictly post-close. And its
observability is untested — a concealed attribution meter reproduces the Civ VI caprice problem CIP-6
itself warns about.

**Ground it on the ELM durability leg (T0/T1), never on the Guiguzi paraphrase** — see §3.5.

### 3.4 N17's stated fix is insufficient

Document 5's own B6 says supplication has no failure state, so optimal play is to supplicate constantly;
its proposed fix is that the form must match the community. That is necessary but **not sufficient**. It
prevents free supplication only if the right form is probe-discoverable, wrong-form failure costs Face,
**and repeat supplication scales its supplicant-side cost** — otherwise the strategy survives the moment
forms become learnable, because the recipient's refusal cost is unbounded while the supplicant's is flat.
The third leg is in neither B6 nor its fix.

We are half-built here already: `imperial_petition_venue` and `memorial_remonstrance_venue` are
`GraceThreshold` pleas judged by the sovereign's leaking character (`modes.py:219-279`). What is missing
is the recipient-side cost of public refusal — one record emission against the refuser, i.e. a CIP-1
consumer.

### 3.5 Canon versus design — a bar distinction that must be enforced

Document 5's own finding B1 is severe: the Guiguzi chapter list is a **publisher's table of contents**,
the doctrinal claims come from a database summary, the Han Feizi material from an encyclopedia rendering.
It states plainly that "every specific technique in N12–N16 rests on a paraphrase of a paraphrase," with
`[TIER-FLOOR: T2]`. B2 adds that the five-tradition table was "arranged, not derived."

**Must NOT be cited as historically grounded in any ratified Valoria doc:** N12–N16 as techniques;
N20's Roman advocacy characterisation (doc 5's own tag); N18's inflation narrative (contested — Ōkouchi
against Ogino, `[CONFLICT]` open); the five-tradition table. If a ratified text mentions the Chinese
tradition at all, it may cite only **Gentz's comparative thesis** — that European rhetoric is
forum-facing and the Guiguzi counterpart-facing — which is properly T1 and survives even if every
technique is misreported.

**Adoptable as game design on merit, sourcing irrelevant or replaceable:** N16 (re-grounded on ELM),
N10, N19 (T1, genuinely citable), N17 (Koziol T1, with the regional caveat), N6 (T0), N3-durability.

This repo's posture — every kernel constant `[SEED]`-tagged or cited — makes the distinction enforceable
at ratification. An N16 record field needs no historical citation; a design paragraph claiming "the
Guiguzi teaches X" does, and currently cannot have one.

### 3.6 The reject list, unhedged

**N2 Story** as a resolution object (invented function bodies, uncosted per-mind content, would displace
a calibrated parity-tested reception engine, and its interaction model is the shape Klei abandoned) ·
**N14 Reverse Scale** as specified (a save-scum trigger in single-player; neither inferable nor
survivable, and doc 5 answers neither horn) · **N15** as a global inversion of the information economy
(a T2 paraphrase rewriting the premises of our entire Appraise design; the venue-scoped fault variant may
be deferred as one config row) · **N18's inflation** (an undefined global trust value on a contested
reading) · **N11's register ladder** (unevidenced by doc 4's own A11; the effect already exists
continuously in `Venue.joint_weight`) · **N4's Cialdini lever map** (per-mind susceptibility tables with
no consumer) · **N12 as a primitive** (our existing hidden-state economy restated as doctrine).

---

## §4 — Two further gaps worth recording

**Deception has no representation.** `EvidenceItem` is `(ground, weight, appeal)` with weight as the
engine's hidden *true* value (`primitives.py:282-289`). There is no apparent-vs-true split, so **forgery
is unrepresentable**: a forged document can only be encoded as genuinely good evidence, and therefore can
never be exposed — there is nothing to expose. Note this is distinct from CIP-1's rule 7 ("a record with
no truth value is still a record"), which governs *outputs* and is correct. The gap is on *inputs*. And
the reframe worth carrying: for a Renaissance political game a high-coverage false story is arguably the
*player fantasy*, not the failure mode — what is missing is the exposure mechanic, without which
deception collapses back into "just good evidence."

**The per-mind story model is unaffordable as authored content, but an affordable path exists.** Eight
proceedings, default 7-juror benches, a 15-member crowd preset; per-mind plausibility would mean authored
world knowledge per juror per evidence item, order-of-100 judgments per template, recurring procedurally
so no amortisation. But the kernel already runs a miniature per-mind reception model —
`Adjudicator.character()` blended against venue role by `leak` (`resolver.py:304-307`) — with per-member
character vectors already authored and **unused at ballot time**. Consume what we already write.

---

## §5 — Disposition of filed work

| Filed item | Disposition |
|---|---|
| **CIP-2 core condition** ("the close must consume claim-graph state, not only the scalar") | **STANDS, strengthened.** It rests on C-1, C-2 and the clinch-generalisation argument — none of which cite §6.2. Restate one notch stronger: consumed **non-fungibly**, not merely consumed |
| **CIP-2's "adopt warrant × attack as the verb set"** | **SPLIT.** The three-attack taxonomy stands (Prakken-sourced). The **warrant-keyed vulnerability assignments are WITHDRAWN** |
| **The 40% invariant as an imported checkable standard** | **REWRITE** as our own `[SEED]` threshold |
| **CIP-2's orientation/Doubt-Marker consolidation** | STANDS — depends on the taxonomy only |
| **CIP-2's two falsifier sweeps** | **STANDS, upgraded from prudence to necessity.** With the payoff table gone, sweep 2 is now the only path to evidence that the taxonomy alone anti-collapses |
| **Fork B / ED-SC-0021** | **SOFTEN + ANNOTATE.** Survives as "three-attack claim-graph close, conditional on the sweep"; must record that its cited §6.2 was retracted by its own successor and that the fork was written blind to doc 4 |
| **New: CIP-11 Deliberation** | N10 as an extension of `VoteAtClose`; requires the `ContestView`/`Panel` per-member exposure first |
| **New: CIP-12 Attribution** | N16 as a post-close-only field on CIP-1's record emission |
| **New: F9** | Added to the ED-SC-0022 bug batch |

---

### Audit trail

`[READ: all five source documents (now preserved verbatim at sources/); resolver.py, primitives.py,
policy.py, modes.py, contract.py, agon_harness.py, appraise.py, faction.py; our three prior audit
documents and the CIP proposal. Every repo claim re-verified by the orchestrator at the file:line given.]`

`[METHOD: three read-only Fable 5 adjudication lenses per CLAUDE.md §10 — fable on the read-only
adjudication nodes, Opus on authorship.]`

`[PROVENANCE FIX: one lens could not read the uploads and correctly reported that we had begun filing
EDs citing documents with no on-disk existence — the same failure mode ED-SC-0017 flagged for
params/contest.md, freshly created by us. The five sources are now preserved in-repo at sources/,
verbatim and clearly marked as non-canon.]`

`[SELF-AUTHORED — bias risk] This document corrects recommendations I made two passes ago. The specific
risk is over-correction: having been caught endorsing a fabrication, the temptation is to reject
everything from the same source. Mitigation: the disposition table is part-by-part, and CIP-2's
engineering content is retained where its support is independent of the retracted table. Residual risk
sits on §1.3's judgment that the story model is no better than the matrix — argued from its encoding,
not measured.`

`[NULL: no Griftlands-class deadlock in our kernel (termination total by construction); no kernel-side
spend-buys-roll path (the literal Klei shape exists only doc-side, as Momentum and flat bonus dice); no
deliberation loop anywhere in the kernel; no legibility field on Move; no attack-opponent-standing verb
in VALID_KINDS; no truth/falsity axis on evidence.]`

`[CONFIDENCE: high — the fabrication split, F9, the re-distillation counts, the N10-as-extension
verdict, and every repo citation. medium — the Klei verdict (structurally code-verified, but the *fun*
claim it inherits is one T2 developer interview and we have played nothing ourselves) and the N16
assessment. low — build-cost estimates.]`

`[PASS-3: three adjudication lenses with required nulls; the retraction traced to its layer (taxonomy
sourced, payoffs not); the corpus's own separation rule re-run to recover its distillation; one live bug
found and verified; the provenance gap our own filing created, closed.]`
