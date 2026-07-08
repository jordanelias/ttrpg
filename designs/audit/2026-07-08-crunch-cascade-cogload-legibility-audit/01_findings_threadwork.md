# Threadwork — Findings (adversarially verified)

**Canonical head:** `designs/threadwork/threadwork_v30.md` (+ `thread_horizontal_integration_
spec.md`) + `params/threadwork.md`.

## 1. Tracker inventory

**MS/RS naming split — confirmed and worse than previously scoped.** `threadwork_v30.md:782`
(the Part Five header) reads "RENDERING STABILITY (WORLD TRACK)" while `threadwork_v30.md:784`
(its own first subsection, two lines later) reads "What Mending Stability Measures" — **the
canonical head contradicts itself.** `params/threadwork.md` uses bare "RS" 25 times, zero spelled-
out "Mending Stability." The co-filed `thread_horizontal_integration_spec.md` uses "RS" 12 times,
zero "MS" — the CURRENT.md-designated canonical *bundle* is internally split, not merely split
against params. Tracked at `canon/editorial_ledger.jsonl` (ED-WR-0002, open, direction decided
"MS wins," execution not done).

**Correction on the starting-value question:** the producer flagged `threadwork_v30.md:840`
("MS ~72") vs. `params/threadwork.md:141` ("60") as a second, separate live numeric disagreement.
The critic pass found this is **already adjudicated**: `params/threadwork.md:141` and
`clock_registry_v30.md:16` both explicitly state "resolves 60-vs-72 → 60." What remains open is
narrower: `threadwork_v30.md:840` is simply an unpropagated stale straggler, and there's a
separate *lore-layer* item (`ms_trajectory_v1`'s derivation of 72 at 245 AG) still marked
"reconciliation pending Jordan" — that's the genuinely open residual, not the flat disagreement
originally described.

Other trackers: Thread Sensitivity 0–100; Coherence 10→0 (practitioner-only); Thread Fatigue
5–35 (nominally specified, **100% unimplemented in sim**); Three-Axis Ob (Depth/Breadth/Distance,
three separate lookups per roll). **"Knot Strain" is used for two unrelated mechanics** — the
opposing-ops penalty (+1/+2 Ob) and the −5..+5 relationship bond-strain gauge — sharing an
identical name with no disambiguation. **"Thread Debt" is referenced twice with no formula,
accrual rule, or home section anywhere in either doc.**

## 2. Interaction chain map

- **The Leap and most Thread mechanics are a "total island" at the execution layer** —
  `sim/thread/operations.py`'s `attempt_leap` has no `mc_v18.py`-campaign-reachable path (it does
  have one caller, `sim/thread/collective.py:93`, but that caller itself has zero external
  importers, and `mc_v18.py` contains zero thread references — the critic pass corrected the
  producer's looser "zero callers" phrasing to this more precise chain).
- **Mass Battle §A.10 self-contradiction, confirmed:** the War-scale row states auto-cost "−2/op"
  then, in the following prose, "the Coherence cap (−1/operation)... applies. No additional
  surcharge" — a genuine −2-vs−1 contradiction, tracked open (ED-1010, correct location:
  `canon/editorial_ledger.jsonl:178`, not the mis-cited line 396 the producer inherited from a
  stale dossier).
- **A residual "RS x3" line survives unreconciled:** `params/threadwork.md:250` (PP-653, dated
  *after* the general ×3-multiplier strike) still reads "RS x3. Temporal not x3" for the
  opposing-ops mass-battle sub-case — no ED ticket reconciles this against the general strike.
  Either an orphaned fossil or a deliberate unlabeled carve-out; currently indistinguishable.
- **MS/RS threshold-band consequences (spontaneous Gaps, Mandate loss, Faction Fracture) are
  unimplemented anywhere** — only the numeric track itself (`sim/peninsular/ms_track.py`) exists;
  `rs_track.py`/`sim/thread/rendering.py` are dead stubs.
- **Knot formation/rupture — REFUTED finding, corrected.** The producer's claim that
  `sim/personal/knots.py` still runs the superseded pre-ED-912 model is **wrong as of today**: a
  same-day commit (PR #89, "Stratum-B: rebuild knots.py onto the ED-912 gauge, C-TW-12") landed
  the current ED-912 −5..+5 gauge; the old model survives only in a comment describing what was
  superseded. The producer inherited a stale finding from a 2026-07-07 dossier without re-checking
  same-day commits.
- **Thread Fatigue, the mechanism designed to rate-limit ops per contact window, has zero
  implementation** anywhere in `sim/thread` or `sim/personal/knots.py`.

## 3. Cascade check — the historical ×3 mass-battle drain

**Confirmed resolved, with one live residual.** The original ×3 multiplier (PP-192/225) is
archived and explicitly struck: "Individual Thread operation RS costs in mass battle are at full
TTRPG value (×1)... PP-225 (gains also ×3) is also struck." The design has moved to a bounded
additive drain model with genuine hard caps in at least three places (flat per-battle model,
per-op auto-cost tier, Substrate Saturation Counter hard-capped at −1/battle). **The
"campaign-ending by design, mitigated only by GM disclosure" characterization from the 2026-04-04
audit is stale — treat this as resolved.** The one live residual is the unreconciled
`params/threadwork.md:250` "RS x3" line noted above.

## 4. Cognitive load

Resolving one Relational-scale Weave requires touching ≈14 trackers and ≈10 decisions — genuinely
the richest, most multi-axis personal-scale action in the corpus (three-axis Ob alone is more
granular than anything else in the game). But one tracker — the world track — carries a pure
translation tax the others don't: every read of its post-op state requires silently reconciling
whether the source calls it MS or RS. That's not a game-relevant 10th decision; it's overhead
layered onto the single tracker with the *most* downstream consequences (faction Mandate, CV,
settlement Order, Revelation Curve) — a legibility tax disproportionate to its 1-of-14 share.

## 5. Legibility gaps (severity per critic-corrected verdict)

- **P1 — MS/RS naming split, confirmed and worse than previously scoped** (self-contradicting
  canonical head, internally-split co-filed spec). Direction decided (MS wins), execution
  incomplete.
- **P1 — No player-facing UI model for Thread ops exists**, combined with the total-island
  execution status — Thread is simultaneously the richest *designed* decision space and the least
  executable/player-facing subsystem in the corpus.
- **P2 — "Knot Strain" terminology collision** between the opposing-ops penalty and the bond-
  strain gauge.
- **P2 — "Thread Debt" is a dangling, undefined tracker.**
- **P2 — Residual "RS x3" at `params/threadwork.md:250`**, unreconciled against the general strike.
- **P3 — Hidden values without disclosure UI**, e.g. the RM-governance Thread-site bonus,
  deliberately "unlabeled in UI" by design — intentional, not a bug, but a second hidden-value
  class beyond MS/RS itself.
- **P3 — Dense philosophical jargon** (Amendment-01/02 vocabulary) with no player-facing glossary
  translation layer, notably dense given Thread's near-total absence of any UI model to translate
  through in the first place.

## Corrections applied from adversarial pass

1. **Knot formation/rupture "runs superseded model" — REFUTED.** Fixed same-day (PR #89); drop
   this finding entirely from any future citation.
2. **72-vs-60 MS starting value — downgraded from "open disagreement" to "resolved (→60), with a
   narrower unpropagated straggler at `:840` and a separate still-open lore-layer question."**
3. **ED-1010's ledger citation corrected** to `canon/editorial_ledger.jsonl:178` (the producer's
   inherited `:396` citation is impossible — the ledger is 386 lines total).
4. General note: this report's design-layer findings (the MS/RS split, the mass-battle
   contradiction, the total-island execution status) are all independently confirmed reliable;
   its main defect was inheriting stale ledger line numbers and one stale finding from a
   2026-07-07 dossier without checking same-day commits. Any downstream use of this report's
   citations should re-verify ledger line numbers before acting on them.
