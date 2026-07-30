# Personal combat — completion plan v4.1 (research-led, iteratively tuned)

## Status: PROPOSED (2026-07-30). Supersedes the SEQUENCING of `combat_execution_plan.md` §7, `combat_remediation_plan.md` §8, and `session_retrospective_and_plan_v3.md` §5. Their *content* stands.

Written under two Jordan rulings of 2026-07-30:

1. **"You have permission to refer to historical data, martial treatises/traditions and HEMA."**
2. **"I do not need to make decisions on concepts that are factually available upon investigation."**

The second is the structural one. It says the ⚖ list is **too long** — it has been used as a place to
park questions that research or measurement can settle. This plan's first job is to shrink it.

**v4.1 (this revision)** is the product of a read-only Fable 5 adversarial pass against v4, whose
findings I then verified by hand rather than accepting. Eight of its findings were confirmed and are
addressed below; one was itself wrong and is corrected; one led to a **new defect** neither v4 nor the
critic had. Full record in §7 — including the two places v4 was not merely imprecise but asserted a
grounding it did not have, which is the exact failure mode this whole arc exists to stop.

---

## §0 Re-classification: what was never Jordan's to decide

**The hazard of this section, stated first (v4.1).** Re-labelling a ⚖ item "researchable" does not
delete the decision — it **relocates it into an acceptance criterion I author**. "Research settles it"
is only honest if the *goal* was already fixed. So the rule for every RESEARCHABLE row below:
**the acceptance criterion is stated up front, in the work package, and is Jordan-vetoable before the
work starts.** Research settles the *number*; it does not get to settle what counts as success.

| id | item | verdict | how it gets settled |
|---|---|---|---|
| ⚖1a | M6 *direction*: re-anchor vs non-saturating | **SETTLED BY MEASUREMENT** | a `min(1,·)` cap can only ever penalise, so re-anchoring cannot help a population already losing. Shipped as ED-PC-0051. Fork closed. |
| ⚖1b | the **katana anchor** for `CUT_REF_NATIVE=1.00` | **JORDAN'S — still open** | ED-PC-0051 ships `needs_jordan: true` and says so in terms: the penalty side flips greatsword and hook_sword to prefer their *point* unarmoured, "a consequence of the katana anchor de-rating everything beneath it, and the anchor choice is Jordan's to confirm or move." v4 folded this into ⚖1 and silently ratified it. **Split out; returned.** |
| ⚖2 | should armour cost the wearer, in which channel | **RESEARCHABLE** | measured locomotor/metabolic cost of harness (W1) |
| ⚖3 | is disposition a real trade or is aggression just good | **RESEARCHABLE** | Silver's true/false times + Vor/Nach; settled by ablation (W6) |
| ⚖4 | is the plate non-participation figure correct | **RESEARCHABLE — and the question is mis-framed** | Harnischfechten does not ask "can a cut beat plate" (it cannot). It asks "what does a swordsman DO in harness" — half-sword, gap-thrust, Mordhau, ringen. The defect is not the count; it is that their **alternatives are unmodelled** (W2). *The count itself is a measurement, not an estimate — see §0.1.* |
| ⚖5 | carry context | **RULED 2026-07-29** | executed; N/A |
| ⚖6 | off-hand **scope** + priority | **JORDAN'S — returned** | v4 called this researchable. It is not, and v4's own J2 conceded the point: the treatises settle *what a companion arm does*, they cannot settle *how much of the configuration space this quarter builds*. Scope is a budget question. **W3 is specified below but does not start until scoped.** |
| ⚖7 | is the roster-wide thrust-lean wanted | **RESEARCHABLE, and the carry frame dissolves it** | the thrust-lean is *correct* in the rapier-era civilian duel and *wrong* on the battlefield. It was only ever a single global question because context did not exist. Now it does (W5) |
| ⚖8 | typed weapon record vs untyped dicts | **RULED BY THE ARCHITECTURE DIRECTIVE** | "strict compliance with code architecture complete with primitive-based process and centralized values" selects typing. Executes as W7b |
| N1 | `CLOSE_ENGAGE_M` value | **NOT derivable from what exists — see W0** | v4 claimed `L0` supplies the body scale. **That is false and is retracted (§0.2).** |
| N3 | `point_concentration` ⟂ `curvature` confound | **RESEARCHABLE** | blade typology + in-roster template (W4) |
| N2, N4–N9 | texture debt, layering guard, orphaned ref, MB digest, ledger caps, midnight stamp | **mechanical** | W8 (PC lane) / §6 (other lanes) |

**Genuinely Jordan's:** ⚖1b, ⚖6, plus —
- **J1** — *feel*: should a duel be decided in 2–3 exchanges or 8–12? Nothing in history fixes lethality pacing for a game.
- **J2** — *scope*: is the grid tactical layer this quarter's target, since it re-homes reach entirely.
- **J3** — *content*: which traditions get authored curricula, and in what order.

### §0.1 The plate figure, measured rather than quoted

v4 said "35/53". The corpus elsewhere says 38. Both are wrong. Measured at HEAD `8a054d0`:

| | value |
|---|---|
| weapons that **cannot decide a fight at heavy armour** | **36 / 53** |
| instrument | `systems/combat/combat_engine_v1/workbench/armour_participation.py --update` |
| fixture | `tests/valoria/data/combat_armour_reference.json` (`generated_at_sha` `e54234e`) |
| at session start (`f03357d`) | 34 / 53 |

It went **up** by two over the session, and **no weapon became able to decide** — the movement is
entirely weapons losing a marginal capability, not gaining one. That direction is worth knowing before
W2 sets a target. The corpus's 38 is stale; §3.8's "record the SHA" rule exists for exactly this.

### §0.2 Retraction: `L0` is not a body measure

v4's W0 said the engine "already carries the fighter's own scale in `L0`" and proposed deriving
`CLOSE_ENGAGE_M` from it. **Checked, and it does not hold:**

- `L0 = 4.0` is in **reach-points**, not metres. Converted through `REACH_GEOM_SCALE = 0.635/0.30`,
  it reads **1.89 m** — not an arm, not a body dimension, a fit anchor.
- `Combatant` carries **no anthropometry at all**. A search of its fields for any body dimension
  returns only `armor`. There is nothing to derive from.

Deriving a "body-scale" constant from `L0` would have re-introduced **precisely the fiat gate
ED-PC-0053 removed** — a threshold sitting on a scale that includes `L0` and calling itself a
derivation. That is the same defect, one layer up, and I proposed it in the plan that documents it.

Worth recording as its own finding: `config.py:176` calls `L0` "the fighter's own arm" in prose. **That
comment is quantitatively false** and is where I got it. It is the third instance this arc of *the
corpus asserting a grounding it does not have* (after `geometry.py`'s "correctly collapse toward 0" and
`close_unwieldiness`'s "pure morphology"). Fix the comment as part of W0.

---

## §1 Architecture compliance — the rules every work package below is bound by

Non-negotiable, from CLAUDE.md §8 and `consolidation_v1` §2.3, plus two this session earned.

1. **One physical fact, one primitive, one owner.** No fact charged twice.

   **v4.1 correction, and it found a live defect.** v4 wrote that mass is charged by four things —
   `wield_heft`, `agility`, `recoverability_factor`, `_recovery_mode_commitment` — "and must not be
   charged a fifth time." That enumeration is wrong in both directions:
   - `recoverability_factor` **composes** `_recovery_mode_commitment` (the latter was extracted *from*
     the former). One owner plus one composer, not two charges. Correct count of distinct consumers of
     `I_g`: **three** — tempo, overcommit-recovery (`wrapper.py:261`), and `defense_affinities`.
   - **But `weapon_tempo` charges `I_g` twice inside one function**: `wield_heft` at
     `combat_systems.py:101` (the `WEIGHT_PEN`/`HANDS_COMMIT` penalty) *and* the
     `TEMPO_RECOVER_K·tanh(_recovery_mode_commitment(…))` term at line 110. Two independent
     MoI-derived penalties on the same output. That is a candidate double-count sitting in the
     single most-consumed function in the engine. **Flagged, not fixed — new item W8c.**

   Also live: `_puncture_adef` and `wound_impairment` were extracted this session because the same
   expression had 2 and 4 copies.
2. **Derive from primitives; never gate on a threshold that hides a body constant.** ED-PC-0053's
   lesson — and §0.2 is the proof it is easy to violate while quoting it.
3. **Centralised values.** Every tunable in `config.py`, exported, round-trip-checked. No inline
   literal. M16's 127 inline literals are a live violation.
4. **Every scaling term ships a *named, mutation-verified safety property*** — REVISED in v4.1.

   v4 said "bounded, dimensionless inputs for any scaling term." **That rule is false as written and
   the engine refutes it twice.** `wield_heft` returns an unbounded power-law ratio
   `(I_g/REC_I_REF)**WIELD_HEFT_EXP`; `contact_moment_edge` returns an unbounded log-ratio. Both are
   correct, both shipped, and the second was built *this session* — so v4's rule would have rejected
   ED-PC-0052. The real requirement is dimensional coherence plus **a property that is named in the
   docstring and killed by a declared mutation**, one of:
   - *antisymmetry* (`contact_moment_edge`: swapping sides negates it — this is what prevents the
     ED-PC-0045 sign pathology),
   - *scale-invariance* (a log-ratio is immune to the unit of moment),
   - *saturation* (`tanh`, as `weapon_tempo`'s recovery term does over a ~0.2–68 raw span),
   - or *a measured range over the actual roster*, reported, not assumed.

   "Bounded" was a generalisation from one session's two mis-scaled terms (`S_g` in units, `I_g` over a
   ~1000× span). The failure in both cases was **an unexamined range**, not an unbounded one.
5. **Ablatable — and ablation must be *stream-identical*, not merely equal-in-mean.** See W8d: the
   engagement loop's RNG stream is order-dependent, so a lever that draws makes `K=0` a *different
   experiment*, not a control. This is a strengthening of the rule, not a restatement.
6. **Grounding tag on every constant**: `[ATTESTED]` (treatise/measurement, cite it),
   `[ASSERTED — first-principles]` (physics reasoning), or `[SIM-CALIBRATE]` (fitted). Mixing these up
   is how `thrust_factor`'s "correctly collapse toward 0" survived — and how §0.2 happened.

---

## §2 The research spine — which source answers which question

**Sourcing discipline, because this repo has already caught one fabricated citation:** every source
below is a *candidate to verify at point of use*. No figure enters a constant until the citation has
been checked and the `PP/ED` recorded. A named author is not a verified number.

| question | source class | specific candidates |
|---|---|---|
| what a swordsman does in harness | armoured-combat treatises | Fiore, *Fior di Battaglia* (1409) — half-sword, abrazare, poleaxe; *Le Jeu de la Hache* (c.1400); Talhoffer (1467); Ringeck/von Danzig Harnischfechten glosses |
| the companion arm | civilian systems | Royal Armouries **I.33** (c.1300) sword-and-buckler; Marozzo, *Opera Nova* (1536); Capo Ferro (1610) and Fabris (1606) for rapier-and-dagger |
| measure, tempo, the times | Silver, *Paradoxes of Defence* (1599) — true/false times, the four governors; Capo Ferro on *misura* | already partly wired (`true_time_edge`) |
| cost of wearing harness | experimental physiology | Askew/Formenti/Minetti, locomotion in replica 15th-c harness (*Proc. R. Soc. B*) — **verify the figures before use** |
| swing/thrust kinematics | sports biomechanics | Cross & Nathan; Fleisig — already the grounding for `agility`'s exponent |
| blade geometry typology | arms scholarship | Oakeshott typology for cross-section/taper; used to settle N3's tip data |
| **the close measure** | **anthropometry, and it is not in the engine** | **W0 — no existing primitive supplies this (§0.2)** |

---

## §3 The iterative testing protocol — the part both prior plans lack

Both originals treat measurement as a **gate** ("run the suite, check the golden"). This session proved
that is insufficient: three batches passed every gate and achieved nothing, and one constant landed at
a balance optimum without anyone intending it. Tuning, physics and biomechanics need a **loop**, not a
checkpoint.

**Every tunable or physical term follows this cycle, and the artifacts are the deliverable:**

1. **GROUND** — name the source and the tag (§1.6). If `[SIM-CALIBRATE]`, say what it is fitted to.
2. **PRE-REGISTER** — write the predicted direction *and magnitude* into the test docstring **before
   measuring**. ED-PC-0054's prediction failed and that failure is the most informative line in it.
3. **BUILD RED-FIRST** — guard before fix; observe the specific red value.
4. **MUTATE** — run every declared mutation. Two of eight guards this session were decoration until
   the mutation was actually run.
5. **SWEEP** — **mandatory sensitivity sweep over the constant's plausible range**, at a **declared
   resolution**, reported as a table. This is the step missing from ED-PC-0053 and it is why
   `CLOSE_ENGAGE_M` cannot now prove it wasn't tuned. A non-monotone response is a finding.
6. **ABLATE** — measure with the term at zero, same seeds, paired, **and assert the ablated run is
   stream-identical to the pre-change engine** (§1.5, W8d).
7. **TEXTURE + AGGREGATE** — report both. A term can move 122/212 armour cells and no field ordering.
8. **RECORD THE SHA** the measurement was taken at. Every field number this session went stale within
   one batch — including v4's own plate figure (§0.1).

**Termination rule — REVISED in v4.1.** v4 said "iterate 2→7 until the sweep is flat within noise."
That rule **cannot terminate for exactly the constants that motivated it**: a sensitive constant is by
definition one whose sweep is *not* flat, so the rule loops forever precisely where it is needed. The
correct rule:

> **Sweep once, at a declared resolution, and report it. The sweep is the deliverable, not a filter.**
> If the response is flat, say so and take any value in the flat region. If it is not flat, the
> curve — with its optimum marked — goes to Jordan and **he rules the value**. Re-running the sweep at
> finer resolution is permitted; re-running it *after moving the constant toward a field target* is the
> tuning §0 forbids.

A target-shaped optimum is a **disclosure**, not a destination.

---

## §4 Work packages, in dependency order

Each carries: grounding · the primitive it adds or fixes · its falsifier · acceptance.
**Acceptance criteria are Jordan-vetoable before the package starts (§0).**

### W0 — `CLOSE_ENGAGE_M`: sweep, disclose, rule *(N1)* — REWRITTEN in v4.1
v4 proposed deriving this from `L0`. **Retracted (§0.2): `L0` is a 1.89 m reach-point fit anchor and
`Combatant` has no anthropometry.** There is no primitive to derive from, and inventing a derivation
from `L0` would re-commit ED-PC-0053's defect. Three honest options, in order of preference:
- **(a)** Add **real anthropometry** as a new primitive (fighter height/reach on `Combatant`, with
  `CLOSE_ENGAGE_M` a function of it). This is the correct fix and is a *package*, not a constant — it
  touches character generation and the Godot contract. Scope it before committing to it.
- **(b)** Sweep the constant per §3.5, publish the curve, **Jordan rules the value**, and tag it
  `[SIM-CALIBRATE]` honestly rather than dressing it as derived.
- **(c)** Do nothing and leave it disclosed.
· *Falsifier:* the sweep must show whether 0.45 sits at a balance optimum. If it does, that is
disclosed as a coincidence-or-not, and (b) becomes mandatory over (c).
· *Also in this package:* correct `config.py:176`'s false "L0 = the fighter's own arm" comment.

### W1 — Armour costs the wearer *(⚖2)* — **PROMOTED to first behavioural package**
Currently armour is **free**: it defends and costs nothing. Verified — no stamina, fatigue, or
encumbrance channel reads the armour class anywhere. Attested cost is metabolic/locomotor, so the
channel is **stamina/fatigue** (`wrapper.py`'s existing `stamina` drain), not tempo — tempo already
prices mass, and §1.1 now shows it may price it *twice*.
**Why first:** it is the one package that is unambiguously a *missing cost on a currently free
resource*, which is the session's central lesson (v3 §1). W3 is not (see below).
· *Falsifier:* an armoured fighter must lose a *long* fight it wins short.
· *Acceptance:* heavy armour is a genuine trade at some fight length; sweep reports the crossover.

### W2 — Harnischfechten: model the alternatives, not the cut *(⚖4, reframed)*
36/53 weapons cannot decide a fight at plate (§0.1). **That is historically correct and is not the
defect.** The defect is that the documented responses are absent or unreachable: half-sword (partly
present), gap-thrust (present), **Mordhau** (present but weak), **ringen/grapple in harness** (contact
axis exists; `COVERAGE_GAP['partial']` is plumbed with no caller).
· *Falsifier:* a longsword in harness must have a *non-zero* path to victory that is not its edge.
· *Acceptance:* the 36 shrinks because alternatives became reachable — **not** because cuts started
defeating plate. Re-measured with the §0.1 instrument, SHA recorded.

### W3 — The companion arm *(⚖6 — BLOCKED until Jordan scopes it)* — **demoted in v4.1**
Historically the civilian configuration, not an accessory. Three effects on **existing** terms, per the
proposal §13.2: buckler → `coverage='partial'` (already plumbed, no caller); parrying dagger → defender
parry affinity; paired → contact axis.

**v4 called this "the rapier's real counterweight" and ordered it third. Both claims are weak and are
corrected here.** W3 is a **benefit** package, not a cost package: it adds capability to a
configuration. And the weapon best served historically *and* mechanically by a parrying dagger is the
rapier — so the most likely outcome of W3 is that **rapier-and-dagger becomes the new outlier**. Its
v4 falsifiers ("rapier-and-dagger must beat lone rapier", "the four off-hand weapons must leave the
bottom tail") are both benefit-shaped: they are satisfied by making things stronger, which is what v3
§1 warns against. Honest framing: W3 is worth building because the configuration is historically
correct, **not** because it will fix the rapier.
· *Real falsifier (v4.1):* the **civilian spread must fall**. If rapier-and-dagger simply replaces
rapier at the top and the spread is unchanged or wider, W3 did not do the thing it was scheduled for,
and that must be reported as a failure rather than absorbed as "the off-hand works."
· *Blocked on:* ⚖6 scope ruling.

### W4 — Tip data: retire the curvature double-count *(N3)*
`point_concentration` correlates **−0.729** with `curvature`; `thrust_factor` then penalises curvature
*again*. shamshir pc **0.08**, below an axe. In-roster template exists: **szabla, curv 0.30 / pc 0.60**.
· *Falsifier:* corr(curvature, pc) must fall toward 0 after re-authoring; the curved family must gain a
real (if precision-gated) thrust. · *Acceptance:* one penalty, one place. **Then re-measure ED-PC-0054
(N4), whose effective size rides on this correlation.**

### W5 — Context-conditioned balance *(⚖7 dissolved)*
The thrust-lean is right in the civilian duel and wrong on the battlefield; it was one global question
only because context did not exist. Build the per-context field instrument against the ruled carry
taxonomy. · *Acceptance:* balance is asserted **per context**, and the raw matchup table stays spiky.

### W6 — Disposition as a real trade *(⚖3)*
Silver's true/false times: aggression that seizes the initiative is good, over-commitment is punished.
Both halves must be live. · *Falsifier:* ablation — if max aggression wins at every commit level, it is
not a trade.

### W7 — Architecture *(⚖8 ruled, M16/M17/M18)* — **SPLIT in v4.1**
v4 scheduled the whole of W7 second, arguing "every behavioural package below it adds constants, so
doing it later means doing it to a larger target." The argument is sound for *mechanical* work and
unsound for *schema* work: W2/W3/W4 will each add or change weapon fields, so a typed record frozen
before them gets churned by all three. Split accordingly:

- **W7a — mechanical, runs SECOND.** M18's god-module split (`combat_systems.py`, now **80 fn /
  1059 SLOC** — I grew it by 3 this session; the register records 76/944) and M16's 127 inline
  literals into `config.py`. Neither depends on what fields a weapon has. · *Acceptance:* no module
  over ~500 LOC; every constant in `config.py`, exported, round-trip-checked.
- **W7b — typed weapon record, runs AFTER W2/W3/W4.** By then the field set is known. · *Acceptance:*
  ⚖8 satisfied; the Godot contract regenerates from the typed record.

### W8 — Guard and audit debt *(N2, N5, + two new in v4.1)*
- **W8a** — texture measurement owed for ED-PC-0052 and ED-PC-0054 *(N2)*.
- **W8b** — layering/acyclicity guard: nothing currently prevents `weapon_physics` importing upward or
  a cycle forming *(N5)*.
- **W8c — NEW.** The `weapon_tempo` double-charge of `I_g` (§1.1). Audit whether `wield_heft`'s penalty
  and the `TEMPO_RECOVER_K·tanh(_recovery_mode_commitment)` term are pricing the same physical fact.
  · *Falsifier:* if they are independent, ablating one must leave the other's roster ordering intact.
- **W8d — NEW, and it gates §3.6 for every package above.** `wrapper.py` (496 lines) is the
  engagement loop: ~30 sequential `rng.random()` draws, **stream-order-dependent short-circuits**
  (line 93 documents one explicitly — "represent_p==1.0 draws NO rng"), and latched state (`closed`,
  `bind`, `ready`). **Consequence: any new lever that draws RNG reshuffles the stream for everything
  downstream, so a `K=0` ablation is a different experiment, not a control.** Every paired-seed
  measurement in this plan depends on an instrument nobody has audited. · *Acceptance:* a guard that
  asserts an ablated run is **stream-identical** (same draw count and order) to the pre-change engine,
  plus a documented ordering/latch map of the loop. **Do this before W1's ablation, not after.**

---

## §5 Ordering

**W0 → W7a → W1 → W8d → W4/N4 → W2 → W6 → W5 → [W3 when scoped] → W7b → W8a/b/c.**

Changes from v4, each with its reason:
- **W1 replaces W3 as the lead behavioural package.** W1 is a missing *cost* on a free resource; W3 is a
  *benefit* that may worsen the very outlier it was scheduled to fix (§4 W3). The session's central
  lesson was: look for missing costs on dominant quantities.
- **W7 split; only W7a keeps the second slot.** The "do it before the target grows" argument holds for
  the module split and literal centralisation, not for a schema that W2/W3/W4 will churn.
- **W8d moves early**, ahead of every package whose acceptance rests on paired ablation. It is the
  instrument, and the instrument is unverified.
- **W3 is unscheduled**, pending ⚖6.

---

## §6 Out of scope for this PC-lane plan

**Cross-lane items, routed rather than executed here** (CLAUDE.md §4 lane-scoping; v4 folded these into
its own W9, which would have made a PC plan touch three lanes):
- **MB lane** — the byte-exact digest is **environment-unstable**: `main` and this branch both fail
  it, but CI fails `cell_mode` while a local run fails `unit_mode`. That is a platform float-determinism
  difference, not a merge effect, and it means the MB byte-exact gate does not currently mean what it
  says. Raised on PR #273; belongs to MB.
- **IN lane** — the per-lane archive cap default (three lanes crossed 50k in a week and each was added
  by hand: `tools/ci_register_size_check.py:117`); the midnight-rollover currency-stamp regression.
- **PC lane, kept:** the orphaned `CLOSE_EFF_GAP_REF` anchor → folded into W0.

Also out of scope:
- **No closed-phase LEVERAGE/DAMAGE rework.** Reach is ruled to the grid layer. Four levers swept, every
  fix broke `guisarme@heavy`.
- **No re-tuning to hit a field target.** §3's termination rule forbids it.
- **No new benefit channels on weak weapons** without a measured throughput argument (v3 §1) — which
  now explicitly includes W3.

---

## §7 v4.1 revision record — the adversarial pass

A read-only Fable 5 `valoria-critic` was run against v4 (structural independence: `Read/Grep/Glob`
only, and it never saw the reasoning that produced v4). **Its findings were verified against the
working tree before being accepted**, which mattered: one was itself wrong, and one verification turned
up a defect neither v4 nor the critic had.

| # | critic finding | verified? | disposition |
|---|---|---|---|
| 1 | ⚖6 re-classification wrong — scope is not factual, and v4's own J2 concedes it | **yes, by reading v4 against itself** | ⚖6 returned to Jordan; W3 blocked |
| 2 | ⚖1 "close the fork" silently ratifies the katana anchor the ledger holds `needs_jordan` | **yes** — ED-PC-0051 `needs_jordan: true`, text: "the anchor choice is Jordan's to confirm or move" | split into ⚖1a (settled) / ⚖1b (returned) |
| 3 | W0 is hand-waving and would re-introduce the fiat gate ED-PC-0053 removed | **yes** — `L0`=4.0 reach-points = **1.89 m**; `Combatant` has no anthropometry | W0 rewritten; §0.2 retraction |
| 4 | §1 rule 4 (bounded inputs) overstated; would have rejected ED-PC-0052 | **yes** — `wield_heft` (unbounded power-law) and `contact_moment_edge` (unbounded log-ratio) are shipped counter-examples | rule 4 restated as *named, mutation-verified safety property* |
| 5 | W3 is not "the only cost package"; W1 is the cleaner one, and W3's falsifiers are benefit-shaped | **yes** — no armour cost channel exists anywhere; W3's falsifiers are all "X must get stronger" | W1 promoted, W3 demoted and re-described |
| 6 | W7-second risks schema churn from W2/W3/W4 | **yes**, on the schema half only — the module-split half is churn-free | W7 split into W7a (second) / W7b (after W4) |
| 7 | §3's convergence rule cannot terminate for the sensitive constants that motivated it | **yes** | termination rule replaced: sweep once, report, Jordan rules |
| 8 | omission — `wrapper.py`'s RNG-ordering/latch blind spot appears nowhere in W0–W9 | **yes** — 496 lines, ~30 draws, an explicitly stream-conditional gate at line 93 | new **W8d**, scheduled *before* the first ablation |
| 9 | W9 folds MB/IN items into a PC plan | **yes** | §6 routes them out |
| 10 | the mass-charging enumeration is overstated | **partly — and the real finding is worse** | `recoverability_factor` composes `_recovery_mode_commitment`, so the count is 3 not 4 — **but `weapon_tempo` charges `I_g` twice in one function**. New **W8c** |
| 11 | *(implied)* the plate figure should be 38 | **no — the critic is wrong too** | measured **36/53** at `8a054d0`; 38 is stale, 34 at session start (§0.1) |

**The critic's own most useful observation**, and it is retained as §0's opening rule: re-labelling a ⚖
item "researchable" relocates the decision into an acceptance criterion the author writes. That is not
a defect in any one row — it is a defect in the *move*, and the fix is that acceptance criteria are
declared up front and vetoable.
