# Dossier — Lane SC (Social Contest) — Pessimist Subtractive NERS Audit

**Audit:** `designs/audit/2026-07-08-pessimist-action-audit/`. **Method:** Sonnet reconcile-dossier,
read-only. **Cardinal rule applied throughout:** every verdict below judges the action **as if built
exactly as specified**; build-state (wired/stubbed/unported) is recorded only as `build_state_note`
routing metadata and never enters a verdict.

---

## 0 · Reconciliation intro

**Sources reconciled:** `sim/personal/contest/dictionaries.py` (Style×4 / Proceeding×8 / Adjudicator×4 /
Interaction×4 typed surface); `designs/scene/social_contest_v30.md` §§1–11 (full read); the
Agôn-only-built vs Negotiation/Inquiry/Consensus-prose-only divergence (`sim/personal/contest/wrapper.py`
GAMES registry vs `HANDOFF_SC.md`'s "build all four deliberative games" Stage-4 charge);
`designs/audit/2026-07-01-contest-player-interaction/player_interaction_walkthrough_v1.md`;
`references/module_contracts.yaml` (`social_contest` module row); and — because this lane has already
been audited in unusual depth in the last two weeks — the standing corpus of prior work: the
2026-07-04 NERS-qualitative audit (`dossier_social_contest.json`, `hunt_social_minmax.md`,
`refute_four-games-collapse-one-pattern.md`) and the 2026-07-05 Fable-5 subsystem audit (RATIFIED,
PR #80 — `dossier_playability.md`, `fable5_social_contest_audit_v1.md`), plus `HANDOFF_SC.md`'s
live P0/P1 docket (ED-SC-0002..0010) and `designs/audit/2026-07-07-unaddressed-areas-audit/
resolution_plan_v1.md` (Stratum B/C/D contest-package rows).

**Prose/code divergence (the charter's explicit reconciliation instruction):** the v30 prose and the
corpus's own stated intent (workplan #39/LA-19, HANDOFF_SC.md) describe **four deliberative games** —
Agôn (adversarial contest), Negotiation (ZOPA bargain), Inquiry (truth-convergence), Consensus
(holdout/assent) — sharing one setup grammar (venue/adjudicator/genre/stakes) but meant to diverge in
*interaction shape* (walkthrough §4). The code object (`wrapper.py` GAMES registry) currently wires
only `agon`; `negotiation`/`inquiry`/`consensus` are typed STUB rows that raise `NotImplementedError`.
Per the cardinal rule this divergence is **not itself a verdict input** — it is Stage-4 build debt,
already tracked (HANDOFF_SC.md "NEXT: Stage 4"). What this audit *does* adjudicate is the **design
object** (item 17 below): judged as specified today (UI-divergence sketches, no resolution-math
commitment), does the four-games design intent actually earn four different mechanics, or does it risk
delivering one mechanic in four costumes? That is a legitimate as-if-built question the prior audits
raised (hunt L-F) and then partly walked back (refutation: P2, deliberate, tracked) — this dossier
takes a position on it below, sharpened toward a concrete Stage-4 gate rather than leaving it as an
open observation.

**Method note on reuse:** where the 2026-07-04/07-05 audits already did rigorous as-if-built analysis
of a mechanic (Appraise's boost-read solvability, Recall's stacking, Obscuring's dominance risk, the
four-games flatness), this dossier does not re-derive that analysis from scratch — it cites it,
confirms it still holds against the current working tree, and renders the **subtractive** verdict the
prior audits were not chartered to render (they logged findings/severities; this audit's job is to say
KEEP/REFINE/DISTILL/PRUNE/CUT).

---

## 1 · Per-action analysis

### 1. Style — Precedent (Memory × Revealing)
**Design intent:** an orator cites a settled, verifiable fact openly, building standing while advancing
the merits track (`dictionaries.py` STYLES_TABLE; v30 §2 Step 3 / §4 Step 2).
**As-if-built:** models the single most load-bearing Renaissance forensic-rhetoric dynamic — citing
precedent/settled record in open assembly (Cicero's *status coniecturalis*/forensic register). Genuinely
cross-scale: a Precedent win feeds Domain Echo (Mandate+1 in the cited domain) and Obligations, i.e. a
personal-scale rhetorical choice produces a traceable-but-not-fully-anticipable strategic consequence
(Ω-a). Q-elegant: "cite the record openly" restates in one read; no hidden interaction.
**Verdict: KEEP.** N passes (forensic citation is the paradigm dynamic, not fantasy imposition); Ω-a/d
pass (cross-scale Domain Echo, pays its cost — forgoes Obscuring's Doubt-Marker upside); Q-elegant passes.
- criterion: N (forensic citation, load-bearing) · calibration: KNOWN-TRACKED · direction: top-down
- intent_gate: DELIBERATE · severity: P3 · retires_downstream: ""

### 2. Style — Vision (Projection × Revealing)
**Design intent:** an orator argues openly for a future outcome (deliberative/pathos-and-logos register).
**As-if-built:** the Projection-genre mirror of Precedent — models the equally real Renaissance
dynamic of open deliberative argument (policy proposal, not fact-finding). Feeds the Projection-genre
Domain Echo (+1D on the first Domain Action pursuing the argued outcome) — a clean, distinct cross-scale
hook from Precedent's Mandate bump, so the two Revealing styles are not redundant with each other despite
sharing an orientation (different genre → different Domain Echo payload, per v30 §6 table).
**Verdict: KEEP.** Same reasoning as Precedent, mirrored on the Projection genre; not duplicate coverage
of Precedent because the genre axis changes both the CROSS/CLASH/REINFORCE derivation against a
Memory-genre opponent and the Domain-Echo payload.
- criterion: N / Ω-a · calibration: KNOWN-TRACKED · direction: top-down
- intent_gate: DELIBERATE · severity: P3 · retires_downstream: ""

### 3. Style — Suppression (Memory × Obscuring)
**Design intent:** burying inconvenient settled history; a win plants a Doubt Marker on the opponent
instead of advancing the track; a move that lands nowhere costs the mover their own Face (CR5).
**As-if-built, judged against the design's own specified fix, not the current wiring:** the corpus's
own prior hunt (`hunt_social_minmax.md` L-C) correctly identifies that *without* the Terminal-Doubt rule,
Suppression is strictly dominated by Precedent in every single-exchange proceeding (EV of an unconsumed
marker = 0 with no next exchange) — a genuine Ω-d dominance failure **if judged against a design that
stops at the un-terminaled Doubt Marker.** But the design does not stop there: `dictionaries.py`
DOUBT_MARKER_FIELD fully specifies a terminal-value rule split by resolution mechanism (banded vs raw
tally), closing exactly this dominance gap, and CR5 additionally taxes a *failed* Obscuring move against
the mover's own Face. Judged **as the design specifies it** (ED-1060's terminal-value branch, the
best-grounded of the two recorded alternatives and the one the design table actually writes out in
full), Suppression is a genuine two-sided bet: win, and you deny the opponent forward motion while
planting a lasting −2 against them; fail outright, and you pay from your own standing. That is
Ω-d non-dominance done honestly, not flavor-only.
**Verdict: KEEP**, with a flagged dependency — Jordan's ED-1060 pick between (a) terminal-value
[assumed here] and (b) gate-Obscuring-out-of-single-exchange changes which of these two readings is
"as specified"; this audit's KEEP holds for reading (a). This is a **routing note, not a verdict
input** — the choice is Jordan's design authority (N/Ω tier), not something this audit adjudicates.
- criterion: Ω-d (non-dominance, once terminal value is specified) · calibration: KNOWN-TRACKED (ED-1060)
- direction: bottom-up · intent_gate: UNDETERMINED (open Jordan fork on which branch is "the design")
- severity: P2 · retires_downstream: ""

### 4. Style — Insinuation (Projection × Obscuring)
**Design intent:** implying an unstated future consequence; same Doubt-Marker/CR5 mechanics as
Suppression, on the Projection genre.
**As-if-built:** identical reasoning to Suppression (item 3), mirrored onto Projection. Not duplicate
coverage of Suppression for the same genre-axis reason Vision isn't duplicate of Precedent.
**Verdict: KEEP** (same ED-1060 dependency as item 3).
- criterion: Ω-d · calibration: KNOWN-TRACKED (ED-1060) · direction: bottom-up
- intent_gate: UNDETERMINED · severity: P2 · retires_downstream: ""

### 5. Appraise (§4 Step 1)
**Design intent:** a per-exchange Attunement+Recall roll on a 4-band ladder that reveals two distinct
things at once: (a) which axis the dominant faction/adjudicator boosts, and (b) — once the Stage-3
Adjudicator Armature is engaged — a coarse register of the adjudicator's hidden Conviction vector.
**As-if-built:** these two reveal-channels do not have the same standing under N/Ω. Channel (b), the
armature read, is genuinely load-bearing: the armature's exact per-axis weights are *never* fully
revealed by design (v30:177, "no band ever reveals the judge's exact per-axis weights"), so choosing a
Style against it stays a bet under uncertainty at every band — a real Q-robust three-viable-approaches
mechanic. Channel (a), the audience/faction-boost read, is **not** a genuine bet even fully realized:
the boost is a deterministic function of public world-state (which faction is dominant; the Guilds case
is itself a deterministic function of the adjudicator's own already-computed ethos/pathos/logos
character, per `guilds_boost_for()`). A player who simply memorizes the 7-row Faction Boosts table (v30
§2 Step 3) — public canon, not hidden GM knowledge under the no-GM mandate — never needs to roll for
channel (a) and is never worse off for skipping it (`hunt_social_minmax.md` L-B, confirmed against the
current dictionaries.py). That is the N-Abstractable failure mode: an existing, already-legible
mechanism (public faction identity) covers the dynamic Appraise's channel (a) claims to earn through
play. Folding channel (a) into passive/free knowledge (the audience boost is simply shown at setup,
same as the walkthrough already shows Venue/Adjudicator type) loses no real decision — the player was
never actually blind to it — while sharpening the one remaining roll (armature-only) into a cleaner,
one-read mechanic: "Appraise reveals what moves this judge, in coarsening detail; nothing else is
worth spending the beat on."
**Verdict: REFINE.** Strip the audience/faction-boost reveal function from Appraise (surface it as free
setup-screen knowledge, matching how Venue/Adjudicator type are already free); keep and sharpen the
armature-read function, which passes N/Ω/Q cleanly on its own. This is a Q-elegant/N-Abstractable
finding on one *half* of a compound mechanic, not a case for cutting Appraise itself.
- criterion: N-Abstractable (channel a) / Q-robust (channel b protected) · calibration: KNOWN-UNTRACKED
  (hunt L-B logged the underlying solvability; no ED proposes this specific split-and-simplify fix)
- direction: lateral · intent_gate: NOT-INTENDED (the corpus explicitly engineered the armature side to
  resist exactly this solved-lookup failure — `armature.py`/Appraise partial-reveal boundary — so the
  boost-channel's *un*-protected redundancy reads as an oversight, not a deliberate design choice, on
  the boost half specifically)
- severity: P2 · retires_downstream: ""

### 6. Corroborate (§4 Step 2b)
**Design intent:** a declared coalition member may back the primary orator before the roll for +1D,
risking 1 strain on failure; Ob differs by Knot-sharing status.
**As-if-built:** models coalition-building in assembly politics — a real, load-bearing Renaissance
dynamic (patronage networks backing a speaker). Genuine cost (own strain risk) for genuine benefit
(ally's pool). Feeds the same cross-scale Obligation/Domain-Echo chain as the primary Argue roll, so it
inherits Ω-a. Distinct from the Coalition-structure setup action (item 15) — this is the per-exchange
tactical layer on top of that setup, not a duplicate of it.
**Verdict: KEEP.**
- criterion: N / Ω-d · calibration: KNOWN-TRACKED · direction: lateral
- intent_gate: DELIBERATE · severity: P3 · retires_downstream: ""

### 7. Recall citation (+2D, §4 Step 3) and 8. Pre-Contest Preparation (§9.1, incl. Findings citation)
Grouped: both are player actions that buy Argue-pool dice from a source **outside** the genre/audience
+2D cap, and both are implicated in the same design-intrinsic asymmetry.
**Design intent:** Recall — cite a specific, verifiable claim for +2D, "available in either genre,"
binary (v30 §4 Step 3); once-per-source in Grand Contest (ED-617) but explicitly retained per-exchange
in Formal Contest. Pre-Contest Prep — deliberate prep time before a contest for +1D (or +1D and a
lowered Appraise TN on Overwhelming), stacking with Findings citation (fieldwork Evidence Track, up to
+2D, F-TRANS-11) for up to +3D on Exchange 1.
**As-if-built:** each of these, taken alone, is N-grounded (citing evidence, preparing a case, and
importing fieldwork Findings into a contest are all real, load-bearing Renaissance-politics dynamics —
this is not fantasy imposition, and Findings-citation is a genuinely good cross-lane (FI→SC) hook, worth
protecting on its own). The design-intrinsic problem is structural, not about any one bonus's existence:
the genre+audience-boost dimension is explicitly capped at +2D combined (v30:85, "maximum +2D... minimum
+0D"), but Recall/Corroborate/Prep/Findings are not subject to any combined cap and stack freely
(`hunt_social_minmax.md` L-A: a Formal-Contest Exchange 1 pool can run base+8D from these sources alone,
sustained +5D/exchange thereafter). This is the textbook Ω-d/М-6 cost-hidden shape: the game visibly
enforces a payment for one class of bonus (genre/audience — capped, "every action pays what it buys")
while leaving a structurally identical class of bonus (preparation/citation) uncapped, so the actual
governing constraint on Argue-pool size is "how many bonus sources did you remember to invoke," not the
attribute roll the whole system is built around. It also fails Q-elegant on its own terms: the core rule
("genre+boost capped at +2D") is *not* restatable after one reading once a player also has to remember
that Recall/Corroborate/Prep/Findings live outside that cap — an "except when X" the design doesn't
itself flag as an exception (Q-elegant's own checklist item: "external dependencies enumerated; 'except
when X' flagged and justified" — this one isn't).
**Verdict: REFINE** (both items, same fix). The individual actions (cite Recall; prepare) are sound and
should not be cut — the fix is a single global stacking cap mirroring the existing +2D genre/audience
ceiling, so "how much total non-attribute bonus can enter one roll" has one legible number instead of an
unbounded sum of memorized exceptions. This is exactly what the corpus's own P0 docket already flags
(KU-1) but leaves as an open decision; this audit gives it a concrete default (cap the combined
Recall+Corroborate+Prep+Findings stack at a stated ceiling, analogous in spirit to the existing +2D
genre/boost cap) rather than leaving "whether to cap it" open.
- criterion: Ω-d (cost-hidden) / Q-elegant (unflagged exception) · calibration: KNOWN-TRACKED (KU-1,
  Fable-5 SC audit P0 docket; hunt L-A)
- direction: bottom-up · intent_gate: NOT-INTENDED (the genre/boost cap's own existence shows the design
  *intends* a ceiling on non-attribute bonus stacking; the omission on the citation/prep side reads as
  an asymmetric gap, not a deliberate two-tier design)
- severity: P2 · retires_downstream: "P0 spec-reconciliation docket item KU-1 (Recall/Corroborate/Prep/
  Findings global stacking cap — `fable5_social_contest_audit_v1.md` §6 P0 row; `resolution_plan_v1.md`
  Stratum C, C-RESPESS-2..5, ED-SC-0004-adjacent). This dossier converts KU-1 from an open 'whether to
  cap' question into a concrete recommended default, narrowing what Jordan needs to rule on."

### 9. Forfeit — Regroup (§4 Step 5)
**Design intent:** forfeit the exchange, no argument, no strain, Track +1 to opponent, Concentration
restores to max.
**As-if-built:** a genuine stamina-management tradeoff — the correct move when a losing streak threatens
Spent, at the real cost of ceding ground on the merits track. Q-robust: one of (at minimum) three live
approaches at Step 5 (continue / Regroup / Concede), each with a different resource profile. N-grounded:
recessing/regrouping mid-proceeding is a real deliberative-body practice.
**Verdict: KEEP.**
- criterion: Ω-d · calibration: KNOWN-TRACKED · direction: bottom-up
- intent_gate: DELIBERATE · severity: P3 · retires_downstream: ""

### 10. Forfeit — Concede a Point (§4 Step 5)
**Design intent:** forfeit the exchange, take 1 strain, Track +1 to opponent, gain +1D next exchange.
**As-if-built:** distinctly differentiated from Regroup by resource axis (spends Face-strain for tempo,
rather than banking Concentration) — not duplicate coverage of Regroup. Models the real tactic of
yielding a minor point to bank rhetorical momentum. Genuine tradeoff, pays its cost (opponent gains
ground on the track either way; the two options differ only in which of your own resources you spend to
get out of the exchange).
**Verdict: KEEP.**
- criterion: Ω-d · calibration: KNOWN-TRACKED · direction: bottom-up
- intent_gate: DELIBERATE · severity: P3 · retires_downstream: ""

### 11. Practitioner Weaving in Contests (§9.3, R-65)
**Design intent:** a TS≥30 practitioner may declare Thread-weaving bonus dice (floor(TS/30), max +3D),
visible to all observers, risking a Church Heresy Investigation and a post-exchange Coherence check.
**As-if-built:** this is the strongest cross-scale exemplar in the lane. It couples a personal-scale
tactical choice directly to the Thread substrate (Μ-γ, the game's core ontology — not fantasy
imposition, it *is* the ontology) and to an autonomous institutional response (Ω-c: the Church's
reaction fires regardless of whether the player wants it to, per the Certainty-indexed table in §9.4b).
The declared, observable nature of the bonus (must declare before rolling, visible to all) means the
risk/reward is fully legible pre-commit — Q-robust passes cleanly (three approaches: don't Weave / Weave
and risk detection / Weave and try to conceal per threadwork §2.3). Genuinely pays its cost: raw power
for institutional/narrative risk, not a free lunch.
**Verdict: KEEP** — this is a model case for what "passes N+Ω+Q under adversarial attack" looks like in
this lane; protect it explicitly as Stage-4/wiring work proceeds (the zero-thread-hooks build state is
routing metadata only, per the cardinal rule — not grounds for any subtraction here).
- criterion: Ω-a/Ω-c (cross-scale, autonomous consequence) · calibration: KNOWN-TRACKED
- direction: diagonal · intent_gate: DELIBERATE · severity: P3 · retires_downstream: ""

### 12. Thread Operations Between Exchanges (§9.4, incl. §9.4b Adjudicator Thread Response)
**Design intent:** a practitioner may initiate a Thread operation between exchanges; a temporal-axis
conflict against the contest's primary genre routes co-movement to Persuasion Track shift (±1); the
adjudicator autonomously responds per their Certainty tier, up to suspending the proceeding and firing a
Heresy Investigation.
**As-if-built:** same reasoning as item 11, one level up — this is the mechanism by which the *contest
itself* becomes porous to the wider Thread substrate mid-play, and the adjudicator's tiered, Certainty-
indexed autonomous response (C5 corrupted/suspended vs C2-0 no response) is exactly the "autonomous
agents continue generating consequential events regardless of player action" clause (Ω-c) done with
real texture rather than a flat trigger.
**Verdict: KEEP.**
- criterion: Ω-a/Ω-c/Μ-δ · calibration: KNOWN-TRACKED · direction: diagonal
- intent_gate: DELIBERATE · severity: P3 · retires_downstream: ""

### 13. Obligation-naming (post-contest, §6.1)
**Design intent:** the winning side of a Decisive Formal/Grand Contest names one specific, verifiable,
achievable commitment the loser must honor; tracked as a clock; violation has faction-Mandate,
Stability, and Reputation consequences; can target settlements; blocks NPC-faction actions that would
violate it for its duration.
**As-if-built:** this is the single clearest N-pass in the whole lane — extracting binding political
concessions from a defeated rival is *the* paradigm Renaissance-leadership dynamic the whole subsystem
exists to model, and the mechanic is maximally cross-scale by construction (Ω-a: a personal-scale
rhetorical win produces a traceable Mandate/Stability/NPC-behavior consequence at faction/settlement
scale that the player can trace but not fully predict how the NPC will navigate around). Dramatic
legibility is a one-sentence read from game-state by design ("who owes what, by when, what happens if
they don't"). Not duplicate of Domain Echo (which is automatic and un-negotiated); Obligation is the
player-authored, specific-commitment layer on top.
**Verdict: KEEP** — an exemplar action; protect explicitly.
- criterion: N / Ω-a · calibration: KNOWN-TRACKED · direction: diagonal
- intent_gate: DELIBERATE · severity: P3 · retires_downstream: ""

### 14. Wager Obligation (§6.1 extension, incl. §6.1.1 edge cases)
**Design intent:** a future-conditional variant of Obligation-naming, valid only in Grand Contests
(Projection genre + Consequence Resonant Style), with a bespoke resolution table (condition met/not
met/partial) plus five further hand-specified edge cases (counterparty death, institutional collapse,
structural impossibility, PC-death-holding, PC-death-owing — ED-778).
**As-if-built:** the underlying dynamic (extending present trust against a future deliverable — a
marriage alliance, a deferred tribute, a conditional truce) is real and load-bearing, not edge-case by
historical grounding. The problem is narrower: **almost none of the five §6.1.1 edge cases are actually
about the future-conditional nature of a Wager** — "counterparty dies/incapacitated before resolution,"
"counterparty's faction institutionally collapses," "PC dies holding/owing an obligation" are all
scenarios that can happen to an **ordinary** (non-Wager) Obligation exactly as written (any Obligation
has a duration during which the obligated party could die or their faction could collapse), yet the
corpus only specifies death/collapse/succession handling for the Wager variant. That is the N-
Abstractable failure mode applied to a design's own internal scope, not to an external mechanic: a more
general "Obligation interrupted by counterparty death/institutional collapse/PC succession" rule (which
the existing `generational_transition_v30` TRANSFER/RESET machinery already mostly supplies, per the
Wager section's own citations) would cover ordinary Obligations *and* Wagers with one rule instead of
building the death/collapse/succession apparatus twice (once implicitly-absent for plain Obligations,
once explicitly bespoke for Wagers). Only "condition becomes structurally impossible" (the third
edge case) is genuinely Wager-specific (a plain Obligation has no future condition to render impossible).
**Verdict: DISTILL.** Keep Wager Obligation as a named variant (it earns its place on N/Ω merit), but
fold the death/institutional-collapse/succession edge-case handling into a single general Obligation-
interruption rule that both plain and Wager Obligations inherit, leaving Wager's own bespoke surface to
just the one genuinely condition-specific case (structural impossibility) plus its distinct
resolution-table shape (met/not-met/partial vs plain Obligation's simple violation trigger). This loses
no decision the player currently has — the five edge cases already resolve by reusing
`generational_transition_v30`'s existing TRANSFER/RESET rules; distilling collapses duplicated
specification, not duplicated player choice.
- criterion: N-Abstractable (self-duplicated scope, not external duplication) · calibration: NEW
- direction: backwards · intent_gate: NOT-INTENDED (ED-778's own edge cases lean on generic
  generational-transition machinery already built for all Obligations — the Wager-only framing of
  §6.1.1 reads as scope creep from the motivating stress-test case, not a deliberate restriction)
- severity: P3 · retires_downstream: ""

### 15. Coalition — declare Side, nominate Lead per exchange (§9.2)
**Design intent:** each orator declares Side A/B at setup (no switching); each side nominates one Lead
per exchange (rotatable); non-lead members may Corroborate; Concentration is a shared pool.
**As-if-built:** models real deliberative-body structure (a faction fields its strongest available
voice each round, without pretending individual coalition members are interchangeable — the shared
Concentration pool and per-exchange Lead rotation genuinely differ from a solo contest's single-track
resource management). N-grounded (parliamentary coalition dynamics); the ratified ED-297 coalition-
dominance-by-intent decision (params "Coalitions mechanically dominate solo advocacy by intent") is
itself an as-if-built Ω judgment already made by Jordan, not something this audit reopens — Coalition
dominating solo is DELIBERATE, cited and closed.
**Verdict: KEEP.**
- criterion: N / Ω-d (ratified asymmetry) · calibration: KNOWN-TRACKED (ED-297) · direction: lateral
- intent_gate: DELIBERATE · severity: P3 · retires_downstream: ""

### 16. Proceeding/venue initiation (player-controlled subset: Personal Appeal, Private Negotiation,
Casual Dispute)
**Design intent:** for these three of the eight proceedings, the player is the one who proposes/
initiates the proceeding ("Appealer proposes," "Initiator proposes," symmetric); the other five
(Formal/Grand Contest, Royal Audience, Church Tribunal, Guild Arbitration) are institutionally imposed
on the player by narrative circumstance.
**As-if-built:** this is deliberately thin by construction, not a design failure — for the
player-initiated subset, "which proceeding to start" is really "what kind of conversation is this"
(narrative framing), and Q-robust's three-approaches bar applies to the *contest itself*, not to the
antecedent choice of walking up to someone privately vs. filing a formal appeal. It is not exploitable
as a dominant strategy either: the player mostly cannot venue-shop across the institutionally-imposed
five, and the three self-initiated proceedings differ enough in stakes/resistance/tracker-mode (v30 §2
Step 5 table) that picking among them is itself a real, if lightweight, choice (a Personal Appeal is a
one-shot high-variance plea; a Private Negotiation is a longer, tracker-optional bargain).
**Verdict: KEEP** as necessary connective/setup structure — not a target for subtraction; its thinness
is proportionate to what it is (a framing choice, not the contest's decision core).
- criterion: N / Q-robust (proportionate) · calibration: KNOWN-TRACKED (dossier_social_contest.json
  decision_points, "meaningful: thin") · direction: forwards
- intent_gate: DELIBERATE · severity: P3 · retires_downstream: ""

### 17. Selecting a deliberative game (the four-games meta-choice: Agôn / Negotiation / Inquiry /
Consensus) — PROSE-OBJECT judgment (prose/code divergence per charter instruction)
**Design intent:** each proceeding is meant to route to one of four differently-shaped deliberative
games — Agôn's zero-sum track, a ZOPA-style bargain (Negotiation), a belief-convergence process
(Inquiry), a per-assenter holdout roster (Consensus) — sharing setup grammar but diverging in
interaction shape (walkthrough §4) and, presumably, in resolution mathematics.
**As-if-built, judged against what is actually specified today (not against Stage 4's eventual code):**
the corpus's own hunt (L-F) found, and the corpus's own refutation confirmed as still-true-but-lower-
severity, that the *currently authored* differentiator across venues is thin: only the doubled Argue-
pool attribute (Cog/Cha/Att), the stasis-primary genre, and the ≤0.50σ armature leverage vary; the
underlying resolution shape (CLASH/REINFORCE/CROSS/TIE against a banded or tally track) is one substrate
for every proceeding. The walkthrough's §4 sketch for the other three games commits only to **divergent
UI widgets** (an offer-bracket panel, a belief-alignment meter, a per-assenter roster) — it does not
commit to divergent **resolution mathematics** (ZOPA/BATNA-range arithmetic, a convergence metric,
weighted-holdout accounting). A UI reskin over the same CLASH/REINFORCE/CROSS/TIE math would be
N-Duplicate-coverage wearing four costumes — the same load-bearing dynamic (rhetorical exchange moving
a scalar track toward a winner) modeled four times with cosmetic differences, not four different
Renaissance political dynamics (adversarial contest, bargaining, truth-finding, consensus-building
genuinely are four different real dynamics and each earns its own existence on N-merit — the risk is
specifically that the *design commitment* as written today does not yet bind Stage 4 to build the
actual differentiating math, only the differentiating skin).
**Verdict: REFINE.** Do not cut any of the four games — each passes N cleanly as a distinct historical
dynamic and this is exactly the kind of differentiation the North Star wants. The refinement is a
**design-commitment gap**: Stage 4's specification should be tightened, before agonist effort is spent
building it, to require a stated distinct **resolution mechanism** per game (not merely a distinct
screen), with an explicit test that the four games are not reducible to the same CLASH/REINFORCE/CROSS/
TIE math with relabeled variables. This is the single highest-leverage pessimist catch in this lane: it
is upstream-of-realization scope-shaping exactly as the charter intends — cheap to fix now (tighten one
acceptance criterion before Stage 4 starts), expensive to fix after four UIs have been built over one
mechanic.
- criterion: N-Duplicate-coverage (risk, contingent on Stage 4's resolution-math choices) / Ω-d
  · calibration: KNOWN-TRACKED (hunt_social_minmax L-F, refuted-to-P2-deliberate-tracked; HANDOFF_SC
  Stage-4 entry)
- direction: top-down · intent_gate: DELIBERATE (Stage 4 is a planned, ratified-sequence future build —
  the gap is in how tightly its acceptance criteria are currently written, not in whether it's intended)
- severity: P1 · build_state_note: "Stage 4 (four-games build) is the corpus's own next planned step per
  HANDOFF_SC.md; nothing here is a claim that Stage 4 doesn't exist yet — the finding is about what
  Stage 4's definition-of-done should require before it starts, independent of build state."
- retires_downstream: "Stage 4 four-games build acceptance criteria (`HANDOFF_SC.md` 'NEXT: Stage 4'
  entry; `resolution_plan_v1.md` Stratum C/D contest package, C-RESPESS-2..5 / ED-SC-0004/0006/0009).
  This dossier's REFINE narrows Stage 4's definition-of-done to require a distinct resolution mechanism
  per game (not just a distinct UI widget), pre-empting a Duplicate-coverage build before agonist effort
  is spent authoring Negotiation/Inquiry/Consensus mechanics that might otherwise just reskin Agôn."

### 18. BG Parliamentary Vote declaration — Side A/B/Abstain, declare genre (§10)
**Design intent:** at the board-game/strategic scale, each faction declares a side (or abstains) and
one genre; resolution is a single combined-Mandate-pool roll with lobbying-derived starting-Track
offset (capped to the compromise zone, ED-621).
**As-if-built:** this is the deliberate strategic-scale abstraction of the same underlying political-
contest dynamic — not duplicate coverage of the personal-scale contest, but its necessary zoom-out
counterpart (mirroring how personal combat has a mass-battle abstraction). Purely strategic-scale play
(no Hybrid escalation) is, by construction, Ω-b-thin (no personal-scale transformation) — but the
Hybrid Contest (§11) exists precisely as the ratified bridge for when personal-scale color is wanted,
and the lobby-cap (ED-621, "lobbying cannot predetermine a vote") already closes the obvious Ω-d
dominance risk (out-lobby the vote before it happens). The dual pure-strategic/hybrid-escalation design
is the intended shape, not an oversight.
**Verdict: KEEP.**
- criterion: N / Ω-a (via Hybrid bridge) · calibration: KNOWN-TRACKED · direction: diagonal
- intent_gate: DELIBERATE · severity: P3 · retires_downstream: ""

---

## 2 · Lane summary

Of 18 enumerated player-available actions in the SC lane, **12 KEEP** cleanly as-if-built — including
three genuine exemplars worth naming explicitly (Obligation-naming, Practitioner Weaving, Thread
Operations Between Exchanges) that demonstrate this lane's best cross-scale design when judged on
intent rather than build state. **2 style cards (Suppression/Insinuation) KEEP contingent** on Jordan's
still-open ED-1060 terminal-value ruling — a design-authority fork this audit flags but does not
resolve. **3 REFINE**: Appraise's audience-boost channel is N-Abstractable (a solved public lookup
masquerading as an earned read) riding alongside a genuinely load-bearing armature-read channel that
should be kept and sharpened; the Recall/Corroborate/Prep/Findings bonus stack is Ω-d cost-hidden
relative to the genre/audience-boost cap the design itself already enforces, and this dossier converts
the open KU-1 question into a concrete recommended cap; and — the highest-severity (P1) finding in the
lane — the four-games design commitment risks N-Duplicate-coverage if Stage 4 ships four UI skins over
one resolution mechanism, so this dossier recommends tightening Stage 4's acceptance criteria to require
distinct resolution math per game before that stage's build effort starts. **1 DISTILL**: Wager
Obligation's bespoke edge-case apparatus mostly duplicates what a general Obligation-interruption rule
(reusing existing generational-transition machinery) would already cover for any Obligation, Wager or
not — fold it down to the one genuinely Wager-specific case. **No CUT verdicts** were reached in this
lane: every enumerated action, judged as specified rather than as built, earns its place on N/Ω/Q merit;
the subtractive value this dossier adds is entirely in tightening specifications (REFINE/DISTILL)
before further build effort compounds an existing asymmetry (the stacking cap) or risks a new one (the
four-games resolution-math gap), not in removing any action outright.

