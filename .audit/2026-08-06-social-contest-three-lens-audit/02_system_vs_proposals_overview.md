# Social Contest — Current System vs. the Political-Mechanics Proposals
## An orientation and comparison document

## Status: PROPOSED — orientation companion to `00_synthesis.md`; no design text changed
## Date: 2026-08-06 · Lane: SC · IDs: reads on ED-SC-0017..0022
## Audience: someone deciding what to keep, cut, and adopt — not someone auditing what is broken.

---

## How to read this

`00_synthesis.md` is a findings register: it says what is wrong, ranked, with falsifiers. **This
document is the map.** It describes both bodies of work on their own terms, weighs each, measures
how much they actually overlap, and says what each contributes that the other does not.

Three things it deliberately does differently from the audit:

1. **It describes the current system as a design**, not as a defect list. The audit's job was to
   attack; a fair comparison has to first say what the thing *is*.
2. **It takes the proposals' own self-criticism seriously.** All three uploaded documents carry
   honest audit trails naming their own weaknesses. Those weaknesses are load-bearing here — a
   proposal's known gap is a cost of adoption, not a footnote.
3. **It runs the one test upload 3 asked for and could not run itself** (§6). That document closes
   with: *"I performed both the original expansion and this contraction; I am the wrong process to
   judge whether the 31 demoted primitives lost anything real. Test by attempting to configure a
   scene the old primitives supported and the new schema cannot express."* Valoria is a better test
   case than its own predecessors, because Valoria has a **running kernel** to test against rather
   than prose. §6 runs it.

---

## Part I — The current system

### 1.1 What it is, in one paragraph

The Valoria social contest is a **personal-scale rhetorical resolution system** that also carries a
faction-scale auto-resolve, wired into a campaign through a domain-echo bridge. A contest is a
sequence of exchanges between two sides before an adjudicator, resolved on the shared σ-leverage dice
substrate, banded at close into a five-way outcome (Total / Decisive / Compromise / Decisive /
Total). Eight named proceedings configure it — Formal Contest, Grand Contest, Royal Audience, Church
Tribunal, Guild Arbitration, Casual Dispute, Private Negotiation, Personal Appeal — differing in
exchange count, role symmetry, adjudicator type, audience resistance, and track start. It is
explicitly **three-mode** (TTRPG §§1–9, Board Game §10, Hybrid §11), a legacy of the design's
tabletop origin, being carried into a no-GM videogame.

### 1.2 The structural fact that governs everything else

The subsystem is **three resolution models under one name**. This is not a criticism here, just the
shape you must hold to read anything else:

| | **Model A — the canonical prose** | **Model B — the promoted kernel** | **Model C — the legacy stub** |
|---|---|---|---|
| Lives in | `social_contest_v30.md` §§1–12 | `systems/social_contest/sim/contest/` | `contest_legacy_stub.py` |
| Unit of play | a paired **exchange** (both sides declare, then compare) | a **move** drawn from a budget, sides alternating | a single pooled compare |
| Resolution | compare successes → margin vs audience resistance → track moves | per-move reception roll → readiness/resonance-weighted gain accrues to `adv` → banded at close | pool compare → track walk |
| Losing costs | strain → Face → Rattled (−1D cumulative) | reserve depletion → forced yield → **2 yields = clinch loss** | nothing persistent |
| Choice surface | genre × orientation (4 Styles), Recall/Corroborate/Prep/Findings, Momentum, forfeits | appeal (ethos/pathos/logos) × stasis ground; advance / hard / shift / support / evidence / rebut / pass | none |
| Information | Appraise reads the audience and the judge in 4 bands | hidden evidence weights, hidden judge armature, banded Appraise reveal | none |
| Status | **CANONICAL** | the thing that actually runs | **DEPRECATED**, still on the package API |

The two designed models **overlap nowhere except the Persuasion Track's band thresholds.** Every
mechanic named in Model A's §4 is absent from Model B, and every mechanic Model B resolves on is
absent from the canonical head.

### 1.3 Inventory — what the current system actually contains

**Substrate and resolution (Model B, live and strong):**
δσ σ-leverage kernel single-sourced with combat (`M_MAX = 1.5σ` tanh soft-cap, TN7, μ 0.40 / σ 0.80
per die, parity-tested, numpy-free) · a stasis ladder (FACT < DEFINITION < QUALITY < JURISDICTION <
CONSEQUENCE < FEASIBILITY) with upward-only reframe moves · the Aristotelian appeal axis
(ethos/pathos/logos) crossed with temporal register in a 3×3 `RhetoricalWeights` matrix · a
resonance/leak model (how much a proof moves *this* judge here, blending institutional role with
personal character as discipline falls) · `Readiness` and `Room` (built support gating how well
appeals land) · a `Reserve` per-move stamina economy · hidden-weight evidence dossiers with
per-source exhaustion and diminishing corroboration · a Nyāya-derived **fault/clinch defeat
catalogue** (barred device, self-contradiction, evasion, silence) configured per venue · institutional
and public `Pressure` · five win-condition families (ThresholdRace, TallyAtClose, ProofBar,
GraceThreshold, PersuasionTrack, VoteAtClose incl. weighted-by-standing Panel).

**Design surface (Model A, canonical, largely unimplemented):**
Four Styles on a genre × orientation grid · CLASH/REINFORCE/CROSS/TIE interaction algebra · audience
resistance and its erosion · three trackers (Concentration, Face, Persuasion Track) · Doubt Markers ·
Appraise's four-band reveal · Recall/Corroborate/Prep/Findings bonus dice · Momentum spend · forfeits ·
first-to-speak · Obligations and Wager Obligations · Chain Contests · Succession Contests · the Heresy
Investigation lifecycle · the Excommunication Tribunal · the Parliamentary Stay · Thread-in-contest
riders · the BG Parliamentary Vote and the Hybrid mode.

**Cross-scale wiring (live):**
`ECHO_TRANSPORT` default ON · a per-season faction-scale parliamentary vote emitting a composed Domain
Echo (band gates magnitude, genre selects stat/channel — ED-SC-0002) · a personal-scale play-out via
scene dispatch · territory-transfer motions · the Auto/Manual Resolution Duality doctrine with its
`E[auto] ≈ E[played]` constraint.

### 1.4 What is genuinely good here

Stated plainly, because a comparison that only lists faults is useless:

- **The substrate is better than anything the proposals offer.** The uploads specify resolution as
  *"roll = standing modifier + eff modifier"*. Valoria has a calibrated, single-sourced, parity-tested
  σ-leverage engine with a principled saturating cap, shared with combat. This asymmetry is large and
  runs entirely in the current system's favour.
- **The fault/clinch catalogue is a real idea the proposals lack entirely.** Losing because you evaded
  the question twice, or contradicted yourself, or over-reached beyond your standing, is a
  *procedural* defeat condition. Nothing in P1–P45 or M1–M14 has it. It is also correctly built as
  configuration: which faults are fatal is a property of the institution.
- **The appeal × tense resonance model** (a proof lands differently on a judge depending on what kind
  of proof it is, what tense the question is in, how disciplined the judge is, and how much ethos the
  speaker has built) is a richer model of *how persuasion works* than the proposals' warrant schemes,
  which model only *how a claim can be attacked*.
- **Evidence with hidden weights, per-source exhaustion, and diminishing corroboration** is a clean,
  single-owner concealed-value primitive that the doc's four separate bonus dice are a worse
  reimplementation of.
- **Eight proceedings already collapsed to config rows in code.** The kernel independently arrived at
  the discipline upload 3 argues for.
- **The Succession Contest** is a genuine selection mechanism — the thing upload 2 names as its own
  largest gap.
- **Anti-fabrication discipline.** Every kernel constant carries a `[SEED]` tag or cited provenance.
  The proposals have research citations; they have no mechanism preventing a number from being
  invented.

### 1.5 What is wrong with it

Summarised from the audit; full detail and citations in `00_synthesis.md`.

- **The canonical spec describes a game that does not exist**, and the game that exists is
  undocumented. A designer reading the head learns the wrong system.
- **Everything ratified at Stage 3 is unreachable in production** — no path can express a Style choice.
- **No record spine.** Every wired output is a stat delta; one arc-scoped boolean is the only thing
  that guards a later transition. The design's own headline promise ("not just a stat change") is
  precisely what it cannot deliver.
- **Verb collapse.** The four Styles reduce to one meaningful bit plus a dominated bit; two of seven
  exchange verbs are strictly dominated; on 7 of 8 proceedings genre carries no mechanical weight.
- **The contest is decided at setup** — an uncapped bonus stack gives the prepared side p ≈ 0.93 on
  exchange 1, and p ≈ 0.62 of a one-exchange total victory.
- **~16 residual GM-fiat points** in a no-GM engine, including "Reputation shift (GM-set magnitude)"
  and "Inquisitor sets exchange count", which have no rule anywhere.
- **~300+ lines of special-casing** the design's own composition discipline forbids, and which the
  code has already refuted by collapsing proceedings to rows.
- **No opposition model.** Factions have no aims, no memory, no patience, and no concede move — so the
  AI cannot obstruct for a reason or relent for a reason.
- **Three-mode legacy.** TTRPG/BG/Hybrid tripartition is a tabletop inheritance carried into a
  single-player videogame, and it is a live source of duplicated specification.

---

## Part II — The proposals

Three documents, in dependency order. They are not three views of one thing; they are a **pipeline**,
and each supersedes the previous one's mechanics while preserving its research.

### 2.1 Upload 1 — *Political Mechanics for a Renaissance-Inflected Videogame*

**What it is:** a research-to-primitives document. §2 gathers historical mechanisms arranged by what
the institution *does* (selection, deliberation, adjudication, oversight, territorial governance,
diplomacy); §3 surveys what existing games model and where they fail; §4 is a catalogue of **45
primitives** (P1–P45) in seven families; §5 assembles four scenes from them; §7 is a self-audit
landing eleven findings; §8 is a gap register.

**Its strongest contributions:**
- **Stasis theory as a state machine.** The Ciceronian four-stasis scheme is *inherently ordered*, so
  the gate is a state machine that already exists rather than one imposed on the material.
- **Constraint C1**, derived from Burning Wheel's documented *Duel of Wits* collapse: if manoeuvres
  differ only in damage output, players find the two highest-damage ones and stop. This is the single
  most useful finding in the document, and it is empirical, not theoretical.
- **P7's three-attack structure** (Undermine / Rebut / Undercut, from Prakken's structured
  argumentation over Dung's framework) as the answer to C1: the correct verb depends on the *claim's
  structure*, so no verb dominates.
- **P16 Recorded Defeat** (*senatus auctoritas*) — a motion that carried, was stripped of force, and
  remains fully citable. A real Roman category, nearly free to implement, present in no surveyed game.
- **P41 Scaled Compromise** — the winner concedes in proportion to what winning cost. Twenty-plus
  years in print and in play; the documented complaints about Burning Wheel never touch this rule.
- **P33 Decree with Compliance**, evidenced by the capitulary record repeating its own prohibitions —
  documentary proof that promulgation ≠ enforcement.

**Its own declared weaknesses** (§7, and they are honest):
A1 — the stasis-gate system is unproven and its C1 fix *actually lives at the content layer*, not the
mechanical one. A3 — 45 primitives is a designer's vocabulary presented as a player's. A4 — P18's
parameters are Victoria 3's and do not transfer. A5 — there is no resource economy. A6 — per-body
Standing multiplies state with no presentation answer. A7 — P24's "spend decision at every widening"
is empty. A8 — Aristotle is used decoratively. A9 — P45 Shared Loss is a multiplayer solution. Plus
three structural blind spots it names and cannot fix: turn-based scene-bounded play is *assumed*, there
is **no interface thinking at all**, and there is **no player-fantasy check**.

### 2.2 Upload 2 — *State Graphs — Eight Systems*

**What it is:** eight state machines (Court, Tribunal, Inquisition hearing, Negotiation, Parliament,
Settlement management, Territorial governance, Diplomacy) written in the P1–P45 vocabulary, followed by
a **computed** interrogation — an incidence matrix, tier assignment, role-stability check, pairwise
Jaccard similarity, a call graph, and five throughlines — with the script included.

**Its strongest contributions:**
- **It is computed, not asserted.** The overlap analysis was derived by script from the encoded graphs.
  That makes its findings falsifiable in a way design prose usually is not.
- **Three clusters, and they are not the ones the brief assumed:** Adjudication (Court/Tribunal/
  Inquisition, J 0.52–0.76), Administration (Settlement/Territory, J 0.67), Exchange
  (Negotiation/Diplomacy, J 0.52) — sharing only Standing and the Record. Negotiation ↔ Settlement is
  J = 0.07, and the document is right to call that an honest boundary rather than manufacture unity.
- **Negotiation is a subroutine, not a peer system** — three inbound calls, none outbound. This
  reframes the whole category.
- **The record spine (T1)** — every system terminates in a Record, and the chain *closes* only when a
  Record from one playthrough **guards a transition** in another. This is the sharpest single idea in
  the entire proposal set.
- **Role stability as a validation instrument:** 18 of 22 shared primitives hold one role across all
  systems, and each of the four shifts carries design weight. A vocabulary where the same word does the
  same job everywhere is a real vocabulary.
- **S2 Tribunal is the hinge** — highest shared surface, the only cycle in the call graph, and
  therefore what to build first.

**Its own declared weaknesses:** the encoding and the graphs were produced by the same process, so a
primitive could be recorded as present because it *belongs* there conceptually. The document names the
`M` (modifier) cells as the weakest and its own P1/P31 frequency counts as **upper bounds**. It also
concedes that none of S5's numeric parameters are tuned.

### 2.3 Upload 3 — *Consolidation — From Research to Encodable Systems*

**What it is:** the document that makes the other two buildable. It audits them under a new constraint
(single player, one character whose authority varies), then performs a **distillation: 45 primitives →
14 mechanisms + 31 configurations**, verified by script for exhaustiveness and non-overlap. It adds a
four-resource economy, data schemas, fourteen resolution functions, three loops replacing eight graphs,
and a faction opposition model replacing the deleted P45.

**Its strongest contributions:**
- **The separation rule:** *a mechanism is code that takes inputs and branches; a configuration is a row
  in a table. If it can be written as a table row, it is not a mechanism.* This single rule dissolves
  most of the apparent complexity in both prior documents.
- **M2 Scope** — the mandate/limits/PROVISIONAL-binding/repudiation spine. Its argument is that single
  player removes the opponent's cunning as the tension source, and what replaces it is *whether you can
  deliver what you promise*. This is the only thing in the corpus that gets **more** interesting without
  a human across the table.
- **M3 Concealed Value as the unifying object** — the hidden evidence array, the declared-vs-true yield
  gap, and a negotiator's private reservation value are one object in three costumes. The clusters share
  a **noun**, not a verb.
- **`gate(burden)` with four values yields four scenes**, and **negotiation is the gate with
  `burden = NONE`** — not a metaphor, a parameterisation.
- **The warrant × attack vulnerability table** (§6.2) as the operational form of C1, plus a checkable
  **40% authoring invariant**.
- **The opposition model** (§9): per-faction aims, **unbuyable red lines**, a private threat assessment
  that is itself a concealed value, a concession curve, and patience. It replaces a global lose-condition
  with "obstruction ends *for a reason*", and makes a crisis a negotiating window rather than a timer.
- **Aims expiring with their holder** as the pacing device.

**Its own declared weaknesses:** every numeric parameter is `[UNTUNED]`; the interface gap is flagged for
the third consecutive document and remains untouched; the claim corpus's 40% invariant is stated and not
enforced; the inquisitorial array must be *authored to be inferable* with no procedural substitute and no
authoring guidance; and whether any of it is fun is *"unanswerable from inside"*. Most importantly, it
names the test it could not run — the one §6 below performs.

---

## Part III — Merits and issues, side by side

| | **Current system** | **The proposals** |
|---|---|---|
| **Resolution substrate** | ✅ Calibrated, single-sourced, parity-tested δσ engine with a principled saturating cap, shared with combat | ❌ Essentially absent — "roll = standing modifier + eff modifier" |
| **Model of persuasion** | ✅ Appeal × tense × judge-discipline resonance with leak — models *how* a proof lands | ⚠️ Models only how a claim can be *attacked*; no reception model |
| **Anti-collapse** | ❌ Styles differ only in the magnitude of one upside-only scalar — C1's exact failure signature | ✅ Attack types differ in *what they change about the argument*; ⚠️ but the fix lives at the content layer, self-admitted |
| **Defeat conditions** | ✅ Procedural fault/clinch catalogue, venue-configured | ❌ Absent entirely |
| **Memory across scenes** | ❌ Every output is a stat delta; nothing guards a later transition | ✅ The record spine (T1) is their sharpest idea |
| **Authority / who may bind** | ❌ A personal win binds a whole faction with no check | ✅ M2 Scope, argued specifically for our constraints |
| **Opposition model** | ❌ Memoryless; the AI cannot concede — concession is not a move | ✅ Aims / red lines / concession curve / patience |
| **Information economy** | ⚠️ Two concealed-value instances exist but do not compose; probes have no cost or persistence | ✅ M3 + M4 unify it; ⚠️ but no decay model tested |
| **Config-not-mechanism discipline** | ✅ In code (proceedings are rows); ❌ not in the doc (~300+ lines of special-casing) | ✅ The separation rule, applied exhaustively and script-verified |
| **Economy** | ⚠️ Reserve exists; no currency, no favours, no side payments | ✅ Four resources with three rules that make it an economy rather than four counters |
| **Numbers** | ✅ Calibrated where live, `[SEED]`-tagged where not; anti-fabrication enforced | ❌ Every parameter `[UNTUNED]`, some borrowed at the wrong scale |
| **Interface** | ❌ Not specified | ❌ Not specified — flagged in all three documents and never addressed |
| **Proven in play** | ❌ Never played | ❌ Never played |
| **World integration** | ✅ Threadwork, Convictions, factions, Domain Echo, scale transitions | ❌ None — the proposals are world-agnostic |
| **Selection / investiture** | ✅ Succession Contest with graduated splits | ❌ Named as the corpus's largest gap |

**The pattern is clean and it is worth naming:** the current system is strong exactly where the
proposals are weak — *substrate, calibration, reception modelling, procedural defeat, world coupling* —
and weak exactly where the proposals are strong — *memory, authority, opposition, information economy,
and the discipline that keeps a rules document from sprawling*. That is close to the ideal condition for
adoption, and it is the reason the recommendation below is *selective composition* rather than either
"keep ours" or "adopt theirs".

---

## Part IV — How much do they actually overlap?

### 4.1 Measured

Mapping all 45 primitives and all 14 mechanisms onto the live system:

| Verdict | P1–P45 | M1–M14 |
|---|---|---|
| Fully **present** in Valoria | **0** | 0 |
| **Partial** — the idea exists in some form | 13 | 7 |
| **Absent**, in-lane for social contest | 21 | 6 |
| **Absent**, belongs to another lane (settlements / world / factions) | 8 | 1 |
| **Contradicted** — Valoria does the opposite | 3 (P4, P10, P41) | 0 |

**Nothing maps cleanly.** That is the headline number and it cuts both ways: it means the proposals are
not a description of what we built, and it means adoption is real work rather than relabelling.

The three **contradictions** are the most informative rows, because a contradiction is a decision
someone already made:

- **P4 Immunity** — the proposals make it a config list (`Office.immunities`); we have it only as entity
  special-cases (the Church self-investigation shield, the Niflhel exclusion). Ours is scripting drift
  by our own §10 standard.
- **P10 Forum Challenge** — the proposals make *translatio* a costed in-scene move; our doc says an
  adjudicator-type change **ends the contest and starts a new one**. We foreclosed the verb.
- **P41 Scaled Compromise** — the proposals make the winner concede in proportion to what winning cost;
  we *reward* a clean winner (+1 Momentum on Total Victory) and narrate compromise by GM fiat.

### 4.2 Where the two bodies of work agree *independently* — the strongest signals

Convergence between processes that never saw each other is worth more than either alone:

1. **Config-not-mechanism.** Upload 3 derives the separation rule from first principles; our kernel had
   already collapsed all eight proceedings to table rows. Its claim that "S1 Court and S3 Inquisition
   differ in exactly two fields" is *empirically confirmed here* — our Excommunication Tribunal differs
   from Church Tribunal in three numbers and occupies twenty lines of bespoke prose.
2. **Build the political tribunal first.** Upload 2 computes S2 as the hinge (highest shared surface,
   the only cycle). Our most-built family is exactly that: `church_tribunal` + `tribunal.py` + §7.1/§7.3
   + the Stay. The sequencing instinct was independently correct.
3. **Verb collapse is the failure mode to design against.** Upload 1 derives C1 from Burning Wheel's
   documented history; our audit *measured* the same collapse in our own Style grid.
4. **Shared loss is invalid single-player.** Upload 3 deletes P45; we never had it. Convergent, and the
   correct answer is to keep not having it.
5. **A saturating cap on stacked setup advantage.** Upload 1's A5 identifies the unbounded-economy hole;
   our KU-1 identifies the same hole; and our CR6 had **already ratified the fix** (tanh, 1.5σ) before
   either audit ran.
6. **Overlapping competences are the mechanic, not a flaw.** Upload 1 §2.3 makes the Venetian
   observation; our eight proceedings with overlapping jurisdiction embody it.

### 4.3 Where they diverge, and who is right

| Question | Proposals | Valoria | Assessment |
|---|---|---|---|
| Is S9 Selection the biggest gap? | Yes — "the largest gap the interrogation found" | We have a Succession Contest with graduated split ratios | **Valoria is ahead.** The proposals' gap is not ours |
| Is play turn-based and scene-bounded? | Assumed silently; flagged as an unexamined blind spot | Confirmed — scene slate, exchanges, seasons | **Assumption holds for us.** A risk they named that does not bite here |
| What is the unifying object? | M3 Concealed Value (a noun) | The Persuasion Track (a scalar) | **Proposals are right.** Ours is an outcome measure mistaken for a substrate |
| How is a judge modelled? | Not at all — the body is a vote counter | Armature + resonance + leak + discipline | **Valoria is far ahead**, and this should not be given up |
| What does losing cost? | Body of Argument depletion; scaled compromise | Faults → clinch; a strain system that does not exist | **Split** — theirs is designed, ours is implemented, neither is complete |
| Is negotiation a system? | No — it is `gate(burden = NONE)` | Yes — a separate proceeding with a stubbed mode | **Proposals are right**, and the change is cheap for us |

---

## Part V — What to cut or consolidate in the current system

Ordered by ratio of lines removed to emergence lost. Full citations in `00_synthesis.md` §4.3.

### Tier 1 — pure deletion, nothing is lost

| Cut | Size | Why it is free |
|---|---|---|
| The **strain / Charisma-modifier / Focus-defence / Rattled** sub-economy | ~50 lines + 2 derived stats | Four stages of parallel arithmetic no engine has ever evaluated. Its role is already served by the kernel's fault/clinch catalogue and the CR5 Face strip |
| **`social_contest_system_v2.md`** + its index | 513 lines | Banner-marked ⛔ SUPERSEDED, sitting in the live subsystem folder, citing paths retired in 2026-07-19 |
| The **9 non-canonical venue presets** | ~200 lines | Zero callers, `[SEED]` constants, "Jordan assigns names" placeholders, inside a kernel under active rebuild. A reference doc preserves them |
| **Appraise channel (a)** — the audience-boost read | ~10 lines | Already ruled fold-to-setup-screen by ED-SC-0012. A deterministic function of public state is not a concealed value |
| **§12's stale apparatus** + 9 retired-path citations + one false code comment | ~30 lines | Propagation table names files deleted in 2026-07-19; a rename has been "pending user decision" since April |
| **Contest Fatigue** | 2 lines | Session-scoped in a game with no sessions; already dead since the stub left dispatch |
| **`CONCENTRATION_MULTIPLIER`** on the package API | 1 line | A formula struck by ED-901, still exported |

### Tier 2 — consolidation, one owner replaces several

| Consolidate | Onto | Effect |
|---|---|---|
| Recall +2D · Corroborate +1D · Prep +1D · Findings +2D | the kernel's `Dossier` / `EvidenceItem` | The Dossier *already* has per-source exhaustion, diminishing corroboration, and a hard cap — i.e. every property these four bonuses hand-legislate separately. Also cures "who verifies the citation" in a no-GM engine, and **dissolves ED-SC-0005's open number** |
| The faction/audience boost +1D | `Pressure` | `Pressure` is wired, continuous, and CR6-conformant; flat dice are what CR6 retires |
| Casual Dispute | Personal Appeal | Identical mechanically (1 exchange, no adjudicator, TallyAtClose); they differ in a role label. Roster 8 → 7 |
| §7.1 Excommunication Tribunal | a Proceeding row | Differs from Church Tribunal in three numbers; currently twenty lines of prose |
| §7.3's bespoke Heresy lifecycle | Clock + Record + the §6.1 interruption rule | ED-SC-0012's own generalization was never applied here — ~49 lines of hand-built state machine |
| Niflhel's bar and the Church shield | `Faction.parliamentary` + an immunity list | Entity special-cases where a config field already exists — scripting drift by our own standard |
| Terminal Doubt's banded/tally split | one rule on `adv` | The split exists only because two win-condition families expose different quantities; both share `adv` |
| Face's two scales, Concentration's three models, resistance's three representations | one owner each | Three name collisions currently maintained in parallel |

### Tier 3 — the structural cut

**Retire the three-mode tripartition.** TTRPG (§§1–9) / Board Game (§10) / Hybrid (§11) is a tabletop
inheritance. In a no-GM single-player videogame, §10 is the faction-scale auto-resolve and §11 is the
zoom-in — which is *exactly* what the Auto/Manual Resolution Duality doctrine already ratified as one
engine at two fidelities. Keeping all three framings duplicates specification and is a standing source
of divergence. This is the largest single simplification available to the document and it changes no
mechanics.

**Estimated total: ~800 lines off the live surface, of which perhaps 50 are lines a player would ever
have noticed.**

---

## Part VI — Running upload 3's own test

> *"Test by attempting to configure a scene the old primitives supported and the new schema cannot
> express."* — upload 3, audit trail

The consolidation cannot run this against prose. Valoria can run it against a **working kernel**. Here
is what the 14-mechanism schema **cannot express** about scenes our engine resolves today:

| Live Valoria mechanic | Expressible in M1–M14 + the 31 configs? | Verdict |
|---|---|---|
| δσ leverage with a tanh saturating cap | **No.** The schema's resolution is `roll = standing modifier + eff modifier` | **Lost** — and this is our best-calibrated asset |
| Appeal × tense resonance (`RhetoricalWeights` 3×3) | **No.** Warrant schemes classify *claims*; nothing models how a *proof type* lands on a *judge* in a *tense* | **Lost** |
| Adjudicator leak (a judge's institutional role blending into personal character as discipline falls, unlocked by the speaker's built ethos) | **No.** M3 could *hold* a judge's disposition; no mechanism consumes it this way | **Lost** |
| Fault/clinch defeat catalogue (evasion, silence, self-contradiction, barred device), venue-configured | **No equivalent.** `attack()` returns outcomes; there is no "you lost on procedure" | **Lost** |
| Institutional and public `Pressure` tilting resolution and raising judge susceptibility | **No.** Closest is Standing, which is a different thing | **Lost** |
| `Readiness` / `Room` — built support gating how well appeals land | **No** | **Lost** |
| Threadwork coupling (P-14 inseparability), Conviction Scars, Domain Echo | **No** — the proposals are world-agnostic | **Lost, expected** |
| Weighted-by-standing panel ballots with a degenerate-bench rule | Partially — `Selection.threshold` is close but not equivalent | **Degraded** |
| The Persuasion Track's five-band compromise outcome | **No.** `gate()` resolves binary per stasis; the compromise band has no home | **Lost** |

**The answer to upload 3's open question is therefore: yes, the demotion loses real things — but not
the ones it demoted.** The 31 configurations really were configurations; the distillation is sound on
its own terms. What it loses is everything about **reception** — how a specific proof lands on a
specific judge in a specific institution — because the proposals model *argument structure* and Valoria
models *persuasion*. Those are different objects, and Valoria's is the one a player experiences.

**This is the decisive finding for adoption strategy.** Adopting upload 3 wholesale would be an
amputation. Adopting its *organising discipline* (separation rule, single-owner composition, burden
parameterisation) plus its *missing objects* (Record, Scope, opposition model, reservation values)
while keeping our substrate is not.

---

## Part VII — What the proposals contribute

Ranked by value to Valoria specifically.

### Tier A — adopt; high value, low cost, no substitute exists here

1. **The Record (P16 / M10 / T1).** The proposals' sharpest idea, and for us it is nearly free: the
   primitive already exists single-owner at `systems/settlements/sim/ledger.py` as `LedgerTag`
   (`Precedent` / `Grudge` / `Debt` / `Reputation` / `Leverage`, durable across succession). What the
   proposals contribute is not the object — it is **the insight that the chain only closes when a
   record guards a later transition**. That reframing is what turns our Obligations from a stat nudge
   into politics, makes Let It Ride enforceable, gives Recall's "named precedent" an engine-side
   verifier, and gives the loser something to press with next season.
2. **M2 Scope.** Nothing in Valoria models whether a character may bind the body they speak for. Under
   no-GM single-player this is not a feature, it is the tension that replaces the missing human
   opponent. No cheaper source for this idea exists.
3. **The separation rule.** Our code already obeys it; our document does not. Adopting it as an
   editorial standard is what converts the ~300 lines of special-casing into config rows.
4. **`gate(burden)` as one parameter.** Replaces four win-condition classes, two biased track starts,
   and the tracker tri-state machinery with a single Venue field — and makes our already-`TallyAtClose`
   Private Negotiation literally *be* the negotiation case rather than resembling it.

### Tier B — adopt with a named condition

5. **The warrant × attack table.** Structurally the right anti-collapse device, and our kernel is ~80%
   of the way there (`EvidenceItem` already carries ground + appeal + hidden weight; `rebut` exists
   behind a venue flag). **Condition:** upload 1's own A1 is correct that this is a content dependency
   wearing a mechanic's clothes. Write the 40% authoring checker *before* the claims, and run the
   AI-vs-AI sweep before ratifying.
6. **The opposition model (§9).** Aims, unbuyable red lines, threat-as-concealed-value, concession
   curve, patience. **Condition:** this is FA-lane work as much as SC-lane; it needs a co-owner. But
   without at least aims and patience, our contest is an argument against a wall.
7. **P41 Scaled Compromise.** Directly replaces a GM-fiat line with a formula, and prices ugly wins.
   **Condition:** interacts with the Fork B decision, since it is the natural cost side of an
   attack-structure system.

### Tier C — valuable framing, no immediate build

8. **The three clusters and the call graph.** Tells us that the missing Exchange cluster (S4 as a
   *callable subroutine*) is why our Church Tribunal cannot end in a negotiated abjuration, why conquest
   cannot be bargained, and why the Wager Obligation is an instrument with no machine to produce it.
   Diagnostic value now; build later.
9. **M3 as the unifying noun.** We have two concealed-value instances that do not compose. Unifying them
   is the second-cheapest structural improvement after the Record.
10. **P10 Forum Challenge / forum-shopping as the primary navigation verb.** Our forums genuinely
    differ, so shopping would pay — and `build_contest` already takes a `venue=` parameter.

### Tier D — do not adopt

11. **P45 Shared Loss.** Upload 3 deletes it and is right. We never had it. Keep it that way.
12. **The 45-primitive presentation.** Upload 1's own A3 concedes it is a designer's vocabulary
    presented as a player's. Take the primitives; leave the taxonomy.
13. **P18's parameters.** Victoria 3's numbers at a nation-state scale over a century. Our own A4
    equivalent already applies.
14. **The upload substrate.** We have a better one.

---

## Part VIII — What this implies, in one page

**Keep:** the σ substrate, the appeal × tense resonance model, adjudicator leak and discipline, the
fault/clinch catalogue, `Pressure`, evidence dossiers, the Persuasion Track's compromise band, the
Succession Contest, the proceedings-as-rows discipline the code already has, and the anti-fabrication
constants regime.

**Cut:** ~800 lines — the strain sub-economy, the superseded twin document, the non-canonical venue
presets, the dominated forfeits, Terminal Doubt's split, the entity special-cases, the stale apparatus,
and (structurally) the three-mode tripartition.

**Consolidate:** four bonus dice onto the Dossier · the audience boost onto `Pressure` · two proceedings
into one · two bespoke sections into config rows · three name collisions onto one owner each.

**Adopt:** the Record and its guard semantics · M2 Scope · the separation rule as editorial standard ·
burden as a Venue parameter. Then, conditionally: warrant × attack, the opposition model, scaled
compromise.

**The one-sentence version:** *Valoria built a better engine than the proposals describe and a worse
memory than the proposals require* — so the work is not to replace the system but to give it a record,
an authority model, and an opposition that can change its mind, while deleting the parallel rules
document that four stages of implementation quietly left behind.

**What neither body of work has, and what will decide whether any of this is good:** an interface model
and a played prototype. All three proposals flag the interface gap and none closes it; our audit finds
the same. Upload 3's final recommendation is the right one and it costs almost nothing — *prototype the
contest loop on paper with twenty claims and four bodies before writing more code.*

---

### Audit trail

`[READ: all three proposal documents + interrogate.py in full; social_contest_v30.md + infill + index;
the full sim/contest/ kernel; the cross-scale bridges; settlements ledger/registry; the NERS audit
charter. Derived from the three-lens audit filed in this directory, whose verification log is at
00_synthesis.md §1.]`

`[NEW IN THIS DOCUMENT — not in 00_synthesis.md: the measured P/M overlap counts (§4.1); the
independent-convergence list (§4.2); the divergence adjudication (§4.3); and §6, which runs the test
upload 3 names as the one it could not run. §6's conclusion — that the consolidation would cost Valoria
its entire reception model — is the argument for selective rather than wholesale adoption and did not
exist before this pass.]`

`[SELF-AUTHORED — bias risk] The same session produced the audit this document synthesises. §6 is the
part most exposed: I am assessing whether a schema can express mechanics I have just spent a session
reading, and "cannot express" is harder to prove than "does not currently express". The claim is
specifically that M1–M14 plus the 31 named configurations contain no consumer for a reception-side
weighting; a reader who can point to one falsifies it.`

`[CONFIDENCE: high — the inventory of both systems, the overlap counts, and the cut/consolidate list
(each item traced to a file:line in 00_synthesis.md). medium — §6's expressibility verdicts and the
Tier A/B/C/D ranking, which are design judgments. low — any estimate of effort.]`

`[PASS-3: both bodies of work described on their own terms before being compared; convergences
separated from agreements-by-construction; the proposals' self-declared weaknesses treated as adoption
costs; one original test run and reported. Two forks (ED-SC-0020, ED-SC-0021) remain Jordan's and are
not decided here.]`
