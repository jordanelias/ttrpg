> **SUPERSEDED 2026-06-03** by `AUDIT_RECONCILED.md` (the master). Retained as history — do not follow
> independently. Its HIGH headline (finding 1, `resist` inert) was empirically refuted and reconciled to
> "scale-fragile, MEDIUM"; its Smoothness "cliff" (finding 4) and Necessary "fail" were corrected. See the
> reconciled master for the adjudicated findings and the empirical evidence.

---

# Full Audit — Social Contest Engine + Faction Adapter (2026-06-03)

**Verdict.** A well-structured engine with a clean venue-determined core, carrying one live logic
bug (an inert mechanic in the faction adapter), one Lesson-1 role-conflation, one Smoothness cliff,
an unbounded author input, and an accretion of computed-but-unused mechanics. NERS: **N partial-fail ·
R partial · S partial · E partial.** Nothing is fatal to the design; the failure surface is fixable
and mostly localised to the adapter and three engine choices.

`[SELF-AUTHORED — bias risk]` I built this system. The standing incentive is to relabel its flaws as
"intended" — to call the role-conflation a "master variable," the Partial→0 collapse "binary by
design," the uncapped evidence weight "author freedom." Where intent is genuinely undetermined I say
so and leave it to Jordan; I do not use "intended" to retire a finding. Each item below is grounded to
`file:line` from a full re-read this session, not from memory of having written it.

Method: full re-read of all seven modules; the `valoria-resolution-diagnostic` pipeline (decompose →
stress points → effect curves → loops → intent → triage) plus the six lessons and the N/R/S/E verdict;
then a code-architecture pass (import graph, the two standing open items, type discipline, duplication).

---

## Severity-ranked findings

### 1 — `resist` is inert in `coalition_vote` (live bug) · HIGH
`faction.py:128-134`. The §10 high-Stability-abstainer resistance is computed (`resist = min(2, abst)`)
and applied as `s.adv[A] = max(0, roll_net(pool_A) - resist)` and the same for B. `PersuasionTrack`
reads **only the difference** `adv[A] - adv[B]` (`resolver.py:67`). Subtracting the same constant from
both sides leaves the difference unchanged, so in the common case (both rolls ≥ `resist`) **`resist` has
zero effect on the outcome.** In the edge case (one roll below `resist`, clipped by `max(0,·)`) it
produces an *asymmetric* floor-shift toward the clipped side — the opposite of the comment's stated
intent ("shrinks both pools' effect / adds resistance"). The intended effect — pull the track toward the
committee band — requires scaling the difference or moving `start`, not subtracting from both pools.
The mechanic neither resists symmetrically nor compresses toward centre. Verified by tracing the
arithmetic twice. **Fix:** apply resistance to the difference or to `scale`/`start`, e.g. shrink
`scale` or pull `start` toward 5 as `abst` rises; or drop the line and document abstention as
mandate-removal only.

### 2 — `Standing` carries three roles (Lesson 1, conflation) · MEDIUM
One variable feeds three mechanisms that a designer would want to tune independently:
- `SelfGating.licit` reads `standing.v` to gate "hard" attacks (`resolver.py:184`);
- `Readiness.of` reads `standing.frac()` to scale argument gain (`resolver.py:152`);
- `Resonance.leak` reads `standing.frac()` to shift the role↔character blend (`resolver.py:149`).

You cannot change how much standing licenses an attack without also changing how hard arguments land
and how far the judge drifts toward character — the Lesson-1 symptom. **Intent undetermined:** the
contest may *want* standing as a single master rapport variable. But the independent-reviewer reading
is that "license to attack," "credibility that makes arguments land," and "pull on the judge's
character" are three causal jobs sharing one dial. **Fix or ratify:** either split (e.g. a separate
`authority` for gating vs `rapport` for readiness/leak) or record the master-variable design as an
explicit decision so the coupling is intentional, not incidental.

### 3 — Engine-level evidence potency is unbounded in `weight` · MEDIUM
`resolver.py:181` advances by `item.weight * factor` with `readiness=False`, and `_advance`
(`resolver.py:153`) multiplies `MERIT_SCALE · magnitude · res · 1.0 · jitter · bias` with **no ceiling
on `weight`**. A single weight-3 item yields ≈ a maximum (Overwhelming) argument's gain, readiness-free;
a weight-10 item is a one-move blowout. The faction adapter self-disciplines (`case()` caps at
`strong=(1.6,1.2)`, `faction.py:33`), but the **engine imposes no cap** — balance rests entirely on
author-set weights, an author footgun rather than a player exploit. The Lesson-2 reading: a single input
with unbounded, non-uniform impact. **Fix:** clamp effective evidence contribution (soft-cap weight via
the same `tanh` armature, or cap the per-item `adv` delta), so author error degrades gracefully.

### 4 — The `deg ≥ 2` gate collapses Partial into Failure (Smoothness cliff) · MEDIUM
`resolver.py:191`: advancement happens only on `deg >= 2`. The engine resolves four degrees
(`engine.py:32-37`), but the contest maps `{Failure:0, Partial:0, Success, Overwhelming}` — a **Partial
argument advances nothing, identical to a Failure.** Two consequences: (a) the Failure/Partial
distinction the engine computes is **unused** in the contest (a Necessary violation too — see NERS-N);
(b) it sharpens the low-faculty penalty, since low-faculty speakers draw more Partials (the pool/Ob math
in NERS Phase 3) and now get nothing for them. This is the one genuinely accidental-looking cliff (the
intended win/defeat thresholds are exempt — see Lesson 6). **Fix or ratify:** give Partial partial
credit (e.g. `deg==1 → _advance(0.5)`) for a graded, smoother reception; or record that Partial-yields-
nothing is deliberate.

### 5 — §5.5 rebuttal consequences and Sacred Veto are not modelled · MEDIUM
`faction.py`. The adapter maps the *vote shape* (proposer vs target argue before each voter, voters cast
Mandate-weighted), but not §5.5's rebuttal-roll consequences — Overwhelming rebuttal negating motion
costs, proposer Mandate −1, target Stability +1 — nor a true Sacred Veto. Veto is modelled only as
`fixed_lean='no'` (`faction.py:20,41`): a faction that always votes no, **not** an override that blocks
the motion regardless of tally. This is documented adapter scope, but the gap should be explicit:
the adapter demonstrates the engine in the §5 *vote* context; it is not a full §5.5 implementation.
**Fix or ratify:** implement the §5.5 consequence table and a true veto, or state that §5.5 resolution
stays in the canonical faction layer and the adapter is shape-only.

### 6 — `coalition_vote` small-coalition variance (Lesson 3/4) · MEDIUM
`faction.py:132-133`: `roll_net(max(1, pool_A))` uses the **mandate sum as the raw dice count**, floored
at 1. A 1–3-mandate coalition rolls 1–3 dice and the net is read through the hard `PersuasionTrack`
bands — small roll into thresholds, the Lesson-3/4 risk. Large coalitions (pool ≥ ~8) are fine (healthy
pool). The band-clock mitigates but does not remove the volatility. **Intent undetermined:** a small
coalition arguably *should* be volatile at BG scale. **Fix or ratify:** floor the dice at a healthy pool
(e.g. `max(5, pool)`) decoupled from mandate, or accept the coarseness and document it.

### 7 — Test suite is unseeded and exits 0 on failure · MEDIUM
`tests.py` (open item #6). The suite is stochastic without a fixed seed and does not `sys.exit(1)` on
failure, so CI cannot gate on it and runs are non-reproducible. For a system whose correctness claims
*rest on* the suite (62/62), this is the verification layer itself being unreliable. **Fix:**
`random.seed(<fixed>)` at top; collect failures and `sys.exit(1 if failed else 0)`.

### 8 — `_bias` inflates hard evidence, not just argument · LOW-MEDIUM
`resolver.py:153` applies `self._bias(side)` to **every** `_advance`, including the evidence path
(`resolver.py:181`). So institutional/public pressure multiplies the probative weight of documentary
proof by up to 1.9× for the favoured side (`INST_BIAS 0.6 + PUB_BIAS 0.3`). Defensible (a corrupt court
over-credits the favoured party's evidence too) but arguably pressure should sway *rhetorical reception*,
not the weight of hard proof. **Design question for Jordan**, not a clear defect.

### 9 — Clinch/win resolution have different turn-order semantics (#9) · LOW
`resolver.py:194-207`. The win-condition is resolved at the **exchange boundary**, after both A and B
act (`:203`) — symmetric. The clinch is checked **after each side's move**, and `DefeatCatalogue.check`
scans A before B (`primitives.py:107`) — so A's fatal fault is detected a half-step before B's. In an
exchange where both would clinch, A's preempts. Real but low-frequency asymmetry; matters only in
clinch-races. **Fix:** evaluate clinch at the boundary too, or break the A-first scan symmetrically.

### 10 — Computed-but-unused mechanics (Necessary) · LOW-MEDIUM
- `Leverage.net`'s off-ground branch (`primitives.py:64`) is never reached in the live engine —
  `_reception` always calls `on_ground=True` (`resolver.py:133`). Exercised only by unit tests.
- `Resonance.tension` (`primitives.py:83-85`) is defined and never called in the resolver.
- The Failure/Partial degree distinction is computed and discarded (finding 4).

None is load-bearing; together they are the main Necessary drag. **Fix:** remove, or wire the off-ground
branch into a venue that allows off-ground argument, or document them as test-only surface.

### 11 — Band logic duplicated · LOW
`PersuasionTrack.resolve` (`resolver.py:68-75`) and `succession`'s inline bands (`faction.py:103-106`)
implement the same `≥9 / ≥7 / 4-6 / ≤3 / ≤1` thresholds with slightly different inclusivity. Drift risk.
**Fix:** have `succession` call `PersuasionTrack.resolve` (as `coalition_vote` already does).

### 12 — Empty-evidence dodges the silence fault · LOW
`resolver.py:178-179`: presenting evidence with no relevant item refunds the spend and accrues **no**
`yields` fault — unlike `pass`/unaffordable moves (`:164-165`). A side can burn exchanges on empty
"evidence" without risking the silence-clinch. Opportunity-costed in race venues (the opponent advances),
so self-correcting, but the fault asymmetry is real. **Fix:** treat empty-evidence as a yield, or accept
the opportunity cost as sufficient.

### 13 — Stringly-typed `Move` and grounds · LOW
`contract.py:10-14`. `Move.kind/appeal/ground` are bare `str`, validated only at use
(`resolver.py:161,146,186`). Typos in a policy surface as runtime `ValueError`, not at construction.
**Fix:** enums or a `__post_init__` validator.

### 14 — `Panel` tie resolves to not-learned / not-hostile · LOW
`contract.py:42-44`: `sum(m.learned) * 2 > len` is False on an even split, so a 2-member panel with one
learned member is treated as **not** learned — lenient toward the self-gating bar. Edge case; document or
use `>=`.

### 15 — Local/redundant imports in faction functions · LOW
`faction.py:76,110,123,124,139` import inside functions; `coalition_vote` re-imports `PersuasionTrack`
already imported at module top (`:10`). Cosmetic.

---

## NERS diagnostic detail

**Phase 0 — components.** Dice-resolved: argument reception (`_reception → roll_net/degree`) and the §10
coalition pooled roll (`coalition_vote`). Deterministic accounting: advancement (`_advance`), evidence,
`_bias`, all win-conditions. Clock-driven: `PersuasionTrack` (banded track read at close), the per-voter
Mandate tally.

**Quantity classification.** Continuous resources: Standing, Reserve, Room, advancement. Discrete
accumulators: fault counters (`evasion`, `yields`), `PersuasionTrack` bands. Base parameters: faculty
(1–7), Mandate.

**Phase 1-2 — stress points / stakes.** Smallest contest pool: faculty 1 → `Pool.size = 5`
(`primitives.py:45`), the engine's lower edge for the Normal approximation. Smallest coalition pool:
1 mandate → `roll_net(1)`, extreme variance, deciding a banded verdict (finding 6). Evidence
corroboration floor 0.25 (`primitives.py:143`). All decide a verdict whose reversibility is venue-set.

**Phase 3 — effect curves.**
- *Impact uniformity:* faculty's marginal impact is **non-uniform** — steep over 1→4, nearly flat over
  4→7. At faculty ≥ ~3 the effective Ob floors at 1 (`OB_MIN`, `engine.py:23`) and the degree caps at 3,
  so added faculty only raises P(Overwhelming) modestly. This is the canonical σ-leverage soft-cap
  (`M_MAX·tanh`) plus the Ob floor plus the degree cap — **smooth, monotonic, and canonical**, not an
  accidental spike. Lesson-2 "equal-impact steps" is not strictly met, but the deviation is the intended
  elite plateau; not a defect.
- *Threshold cliffs:* the win/defeat thresholds (ThresholdRace `T`, ProofBar `bar`, GraceThreshold `bar`,
  PersuasionTrack bands, fault strikes) are deliberate clocks/bars — Lesson-6 exempt. The one
  *non-exempt* cliff is `deg ≥ 2` collapsing Partial→0 (finding 4).
- *Role conflation:* Standing's triple duty (finding 2).

**Phase 4 — loops.** `[NULL: feedback loops — examined, no undamped+unbounded loop.]` Ethos play →
`standing.build` → higher `standing.frac` → higher Readiness and higher leak → subsequent appeals land
harder. This looks like positive feedback, but it **does not close**: Readiness/leak/resonance scale the
*win tally* (`adv`), while `standing` is built only from the **reception degree** (`magnitude=deg`,
`resolver.py:156,192`), which is roll-driven and readiness-independent (`_reception`,
`resolver.py:131-135`). So no quantity that the loop amplifies feeds back into the quantity that drives
it. All resources are bounded — Standing cap 10 (`primitives.py:29`), Room cap 3 (`:69`), leak cap 0.9
(`:79`), Readiness ≤ 1 (`:94`) — and the win tally is bounded by the exchange budget. One-way
amplification, fully bounded. Lesson 5 satisfied.

**Phase 5 — intent.** Deliberate and sound: the venue-determined resolution, the σ-leverage compression,
the bounded amplification, the corpus-mapped fault severities (one-strike contradiction/barred =
nigrahasthāna; two-strike evasion/silence). Intent undetermined (flagged to Jordan): standing as master
variable (2), Partial→0 (4), small-coalition volatility (6), pressure-on-evidence (8).

**Six-lesson summary.** L1 (one role): **fail** — Standing (finding 2). L2 (uniform steps): **soft** —
faculty diminishing, but smooth/canonical, not a spike. L3 (dice on healthy pools): **pass for the
contest** (≥5 dice), **fail for the coalition adapter** (1-die floor, finding 6). L4 (small rolls through
a deep clock): the coalition path *does* route through the PersuasionTrack clock, partially mitigating
L3. L5 (no undamped+unbounded loop): **pass** (examined null above). L6 (no accidental stacked cliffs):
**pass except** the `deg ≥ 2` cliff (finding 4); intended thresholds exempt.

## NERS verdict

- **Necessary — partial-fail.** The architecture is largely necessary, but it carries one *inert* mechanic
  (`resist`, finding 1) and three *computed-but-unused* ones (off-ground branch, `tension`, the
  Failure/Partial distinction — finding 10/4). The inert mechanic is the material instance.
- **Robust — partial.** Core is robust: loops bounded, contest pools healthy, faults well-formed. Dings:
  uncapped evidence weight (3), small-coalition variance (6), and the `resist` bug (1).
- **Smooth — partial.** Mostly smooth (faculty curve is a smooth canonical plateau; thresholds are
  intended). One real cliff: Partial→0 (4).
- **Elegant — partial.** The venue-determined, wrapper-over-modules, single-source-of-truth design is
  genuinely elegant. Marred by Standing's triple duty (2) and the duplicated band logic (11).

## Code architecture

- **Import graph: acyclic (verified).** `engine` imports only stdlib; `contract` imports nothing internal;
  `primitives ← {contract, engine}`; `resolver ← {contract, primitives, engine}`; `modes ← {contract,
  resolver, primitives}`; `policy ← {contract, primitives}`; `faction ← {contract, primitives, policy,
  resolver}`. No cycle. `[NULL: import graph — acyclic.]`
- **Single source of truth:** `ContestState` holds only `adv`; standing/room/reserve live on `_Side`/Bout,
  no mirror to desync (the old finding #1, confirmed fixed).
- **Spec/runtime split:** `Contestant` (immutable spec) vs `_Side` (per-bout runtime) is clean and makes a
  `Contestant` safely reusable across bouts (`resolver.py:90-108`).
- **Open items:** #6 (unseeded tests / exit 0 — finding 7) and #9 (clinch turn-order — finding 9) remain
  open. Type discipline is stringly-typed but guarded (13). Minor duplication (11) and dead surface (10).

## Recommended order of work (minimal, scoped)

1. Fix `resist` (1) — it is a live bug in a shipped mechanic.
2. Seed the tests and exit non-zero on failure (7) — restore the verification layer.
3. Decide intent on Standing (2), Partial→0 (4), evidence cap (3) — these are Jordan's design calls;
   implement once decided.
4. Cleanup: dead surface (10), band duplication (11), clinch symmetry (9), the low-severity remainder.

No change should be made to the canonical faction layer; §5.5/veto fidelity (5) is a question of where the
boundary sits between the adapter and canon, for Jordan to set.
