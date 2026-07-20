# Reconciled Audit — Social Contest Engine + Faction Adapter (MASTER, 2026-06-03)

**This is the single master.** It supersedes `FULL_AUDIT.md` (committed `a306c3c`) and `AUDIT_CRITIQUE.md`.
Both remain in git history; neither should be followed independently. Where the two disagreed, this
document records the reconciled finding with evidence — and holds the *critique* to account as much as the
audit.

**Reconciled verdict.** A well-architected engine that is largely sound: **NERS — N pass · R partial ·
S pass · E partial** (bar stated below). The residual issues cluster in Robustness — the faction
adapter's `resist` mechanic is silently inert at scale, and the engine's evidence channel is both
readiness-free and uncapped — plus minor Elegance wrinkles. The original audit overstated severity (a
false HIGH, a mis-mapped Smoothness cliff, a too-harsh Necessary fail); the critique corrected those but
overshot toward leniency on Robustness by retracting the `resist` finding wholesale instead of re-scoping
it. The truth sits between them.

`[SELF-AUTHORED — bias risk]` Three layers of it: I built the system, audited it, and critiqued the
audit. The reconciliation is where the temptation is to declare the matter settled and stop scrutinising.
The specific things I am incentivised to miss now: (a) that the critique, in its relief at refuting a
wrong finding, swung too kind on `resist`; (b) that "reconciled" can become a synonym for "averaged" —
splitting the difference rather than measuring. I measured (the empirical section is load-bearing) and I
re-derived each verdict from the evidence, not from the midpoint of the two prior documents.

**Method (per the document-consolidation discipline).** Collate the two documents with provenance →
reconcile each disputed finding against evidence (measuring where measurement is cheap) → consolidate into
this master, marking the superseded pair. Empirical runs are seeded and reproducible.

---

## Reconciliation ledger (the findings that changed)

Each row: what the audit said → what the critique said → the reconciled finding, with evidence.

### R1 — `resist` (faction.py:128-134) — reconciled: **scale-fragile · MEDIUM**
- *Audit (finding 1, HIGH):* "inert — cancels in the `PersuasionTrack` difference."
- *Critique (C1):* "refuted — it works, pulling toward committee; the finding is wrong."
- *Reconciled:* **both partial.** Measured, seeded, abstainer count the only variable:
  - small pools (pro=10/anti=8): committee `0.338 → 0.433` as `resist` 0→2 — **works**;
  - large pools (pro=30/anti=28): committee `0.205 → 0.205`, identical — **inert**.
  `resist` subtracts a constant from both sides; the track reads only the difference, so it cancels
  *unless* the `max(0,·)` floor clips a side. It clips often when `roll_net` means (≈ pool·0.4) are
  comparable to `resist` (small coalitions) and never when they dwarf it (large coalitions). So the audit's
  algebra was correct only in the large-pool regime it did not realise it had assumed; the critique's
  measurement was correct only in the small-pool regime it happened to test. The mechanic **functions in
  the common small-coalition case but silently stops working as coalitions grow**, and the size of its
  committee-pull is an unparameterised side effect of the floor, not a designed quantity. This is a real
  Robustness/scaling defect (fails at the large-pool extreme). **Fix:** parameterise the pull — scale the
  difference or move `start` toward 5 as abstention rises — so it is intended and scale-stable.

### R2 — `Standing` feeds three mechanisms (resolver.py:149,152,184) — reconciled: **LOW (open elegance question)**
- *Audit (finding 2, MEDIUM):* role conflation; "cannot tune the three effects independently."
- *Critique (C4):* overstated — each effect has its own coefficient; independently tunable; drop to LOW.
- *Reconciled:* the critique is right on the mechanism. `SelfGating.MARGIN`, `Readiness.W_STANDING`, and
  `Resonance.ETHOS_UNLOCK` are separate dials; the three effects (gating, readiness, leak) *are*
  independently tunable. Only the *input* (standing's value) is shared. There is no tuning-coupling defect.
  What remains is a pure elegance question — is one variable feeding three mechanisms one conceptual role
  (accumulated authority, expressed three ways) or three jobs? Intent-undetermined; **Jordan's call**, not
  a defect.

### R3 — `deg >= 2` discards Failure/Partial (resolver.py:191) — reconciled: **LOW (design question)**
- *Audit (finding 4, MEDIUM):* an accidental Smoothness cliff (Partial→0).
- *Critique (C5):* mis-mapped — the gate is deliberate (Lesson-6 exempt); it is a Necessary concern
  (discarded gradation), not Smoothness.
- *Reconciled:* the critique correctly removes it from Smoothness (a deliberate gate is not an accidental
  cliff). But it is also **not a clear Necessary failure**: the contest adds no redundant apparatus; it
  merely *underuses* one output of the shared engine (the Failure/Partial distinction). It is a design
  choice with a UX consequence — a Partial argument advances nothing, indistinguishable from a Failure.
  The only live question: should Partial earn partial credit? **Jordan's call.** Severity LOW.

### R4 — evidence channel (resolver.py:181 + Dossier) — reconciled: **MEDIUM (corrected rationale)**
- *Audit (finding 3, MEDIUM):* evidence `weight` is uncapped at the engine level.
- *Critique (C6):* inconsistent — the engine trusts authors on every `[SEED]`; the real distinguishing
  property is that evidence is readiness-free.
- *Reconciled:* kept at MEDIUM, but for the corrected reason. Evidence is the **one channel that is both
  readiness-free** (intended — hard proof needs no rapport) **and uncapped in weight**. A missing ceiling
  alone would be consistent with the engine's general author-trust; the readiness-free-*and*-uncapped
  combination is what justifies a soft-cap on this channel specifically — it is the only move that bypasses
  the rapport economy every other move pays into, and it does so without bound. **Fix:** soft-cap the
  evidence contribution (the `tanh` armature, or a per-item `adv`-delta cap).

### R5 — engine-unused surface (primitives.py:64,84) — reconciled: **LOW (cleanliness, not dead code)**
- *Audit (finding 10, LOW-MEDIUM):* dead code — `Leverage` off-ground branch and `Resonance.tension`.
- *Critique (C7):* over-claimed — grep shows `tension` is unit-tested.
- *Reconciled:* `Resonance.tension` is engine-unused but **unit-tested** (`tests.py:50-55`) — covered, not
  dead. `Leverage`'s off-ground branch is engine-unreachable (`_reception` always passes `on_ground=True`)
  and not keyword-referenced in the suite. Engine-unused surface, LOW. Remove, or wire the off-ground
  branch into a venue that permits off-ground argument, or document as test-only.

---

## Findings carried forward unchanged (static; measurement-independent)

These the critique did not dispute and reconciliation confirms, re-ranked by impact / exposure /
irreversibility (per critique C3, which faulted the original's defect-clarity ranking):

**MEDIUM**
- **§5.5 rebuttal consequences + Sacred Veto not modelled** (faction.py). The adapter is vote-*shape*
  only; veto is a fixed-`no` vote, not an override. A boundary question — does §5.5 resolution stay in the
  canonical faction layer? — for **Jordan** to set.
- **Test suite unseeded, exits 0 on failure, and does not cover the behavioural findings** (tests.py;
  merges original finding 7 with critique C9). The verification layer cannot gate, is non-reproducible, and
  has no test pinning `resist`, the faculty curve, or the loop bound — which is precisely why the
  `resist` error went unexamined. **Fix:** seed; `sys.exit(1)` on failure; add behavioural tests.
- **`coalition_vote` small-coalition variance** (faction.py:132). A 1–3-mandate coalition rolls 1–3 dice
  read through hard bands. Note the coupling with R1: small pools carry this variance *and* are where
  `resist` works; large pools are stable *and* where `resist` dies. Mitigated by the band-clock; possibly
  intended BG-scale coarseness — **Jordan's call.**

**LOW**
- `_bias` multiplies hard evidence, not just argument (resolver.py:153) — pressure inflates documentary
  proof up to 1.9× (design question).
- Clinch (mid-exchange, A-first) vs win (boundary) turn-order asymmetry (resolver.py:197-203) — rare.
- Band logic duplicated between `PersuasionTrack.resolve` and `succession` (drift risk).
- Empty-evidence dodges the silence fault (resolver.py:178-179) — opportunity-costed.
- Stringly-typed `Move`/grounds (contract.py) — guarded at use, not at construction.
- `Panel` tie resolves to not-learned/not-hostile (contract.py:42-44) — edge.
- Local/redundant imports in faction functions — cosmetic.

---

## Empirical stress section (addresses critique C2 — the audit ran none)

Seeded, against the live modules.

**`resist` scale-dependence (R1).** committee fraction, `resist` 0 vs 2:
```
  small pools (10/8):  0.338 -> 0.433   (works)
  large pools (30/28): 0.205 -> 0.205   (inert)
```

**Faculty → reception (confirms the audit's Phase-3 claim).** Mean degree by faculty:
```
  1:1.60  2:1.96  3:2.49  4:2.63  5:2.73  6:2.80  7:2.86
  Δ:      +0.35  +0.53 | +0.14  +0.10  +0.07  +0.06
```
Steep through faculty 3 (the Ob 2→1 floor), flat thereafter — smooth, monotonic, canonical (the
σ-leverage soft-cap + Ob floor + degree cap). Not a defect; the inflection is at 3, not "~4" as the audit
estimated.

**Bounded-loop null (confirms Lesson 5).** Ethos-spam vs a maximally sympathetic low-discipline judge,
adv by budget: `10→22.8, 20→44.0, 40→84.8, 80→163.1` (sub-linear against an ×8 budget span), standing
pinned at the 10.0 cap. No acceleration → no runaway. The amplification is one-way (readiness/leak/res
scale the win tally; standing is built only from the readiness-independent reception degree) and fully
bounded.

---

## Reconciled NERS verdict

**Bar (stated, per critique C8):** a criterion **fails** if a MEDIUM-or-higher structural defect directly
violates it; **partial** if only LOW items, design-questions, or intended-but-imperfect mechanics bear;
**pass** if nothing material bears.

- **Necessary — PASS** (two LOW cleanup notes). The venue-determined design adds no redundant apparatus.
  Residual: engine-unused-but-tested surface (R5) and the underused Partial level (R3) — neither is gratuitous
  complexity. *(Corrects the audit's "partial-fail," which rested on the refuted `resist` bug and the
  over-claimed dead code.)*
- **Robust — PARTIAL.** Holds for the common case (bounded loops, healthy contest pools ≥5 dice), but two
  MEDIUM items bear at the extremes: `resist` fails at the large-pool extreme (R1), and the readiness-free
  evidence channel is uncapped (R4). *(Harsher than the critique's "pass-with-one-note": the critique
  under-weighted `resist`'s scale-fragility after retracting the inert claim.)*
- **Smooth — PASS.** The one alleged cliff (R3) is a deliberate, exempt gate; the faculty curve is smooth
  and monotonic (confirmed); all other thresholds are intended win/defeat lines. No material smoothness
  defect. *(Corrects the audit's "partial," which rested on the mis-mapped cliff.)*
- **Elegant — PARTIAL.** The wrapper-over-modules, single-source-of-truth, venue-determined core is
  genuinely elegant. Wrinkles: the `Standing` conceptual hub (R2, open question) and the duplicated band
  logic. No material defect. *(Agrees with both prior documents.)*

---

## Code architecture (unchanged by reconciliation)

Acyclic import graph (`engine`←stdlib only; `contract`←none; `primitives`←{contract,engine};
`resolver`←{contract,primitives,engine}; `modes`/`policy`/`faction` downstream). Single source of truth
(`ContestState.adv` only; no mirror). Clean spec/runtime split (`Contestant`/`_Side`). Open static items:
the unseeded/exit-0 suite and the clinch/win turn-order asymmetry.

## Open items (genuinely unresolved — not closed here)

- **Top-down corpus re-validation (critique C9c).** The venue-determined thesis — three genres keyed to
  who-judges / what-decided — has been spot-checked (fault severities ↔ nigrahasthāna) but not
  systematically re-validated against the founding rhetoric/oratory framework. Still open.
- **Full test-coverage map (critique C9a).** Which findings the 62 tests do and do not pin has not been
  enumerated beyond the `resist`/faculty/loop gap noted above. Still open.
- **Win-condition edge enumeration (critique C9b).** E.g. `ProofBar` lets the defender win only by timeout,
  creating a stall incentive that interacts with the silence-clinch. Not systematically explored.

## Recommendation (re-ranked by impact)

1. **`resist` (R1)** — parameterise the committee-pull so it is intended and scale-stable; today it
   silently dies at large coalitions.
2. **Evidence soft-cap (R4)** — bound the one readiness-free channel.
3. **Tests** — seed, exit non-zero on failure, add behavioural coverage (would have caught the `resist`
   error).
4. **§5.5 / veto boundary (carried)** — Jordan sets where adapter ends and canon resolution begins.
5. **Design questions for Jordan** — Standing-as-hub (R2), Partial-credit (R3), pressure-on-evidence.
6. **Cleanup** — engine-unused surface (R5), duplicated bands, turn-order symmetry, the LOW remainder.

No change to the canonical faction layer. This master is the document to work from; `FULL_AUDIT.md` and
`AUDIT_CRITIQUE.md` are superseded and retained only as history.
