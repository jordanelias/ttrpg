# Personal combat — completion plan v4 (research-led, iteratively tuned)

## Status: PROPOSED (2026-07-30). Supersedes the SEQUENCING of `combat_execution_plan.md` §7, `combat_remediation_plan.md` §8, and `session_retrospective_and_plan_v3.md` §5. Their *content* stands.

Written under two Jordan rulings of 2026-07-30:

1. **"You have permission to refer to historical data, martial treatises/traditions and HEMA."**
2. **"I do not need to make decisions on concepts that are factually available upon investigation."**

The second is the structural one. It says the ⚖ list is **too long** — it has been used as a place to
park questions that research or measurement can settle. This plan's first job is to shrink it.

---

## §0 Re-classification: what was never Jordan's to decide

Every open ⚖ item and every N-item from v3, sorted by whether it is answerable by investigation.

| id | item | verdict | how it gets settled |
|---|---|---|---|
| ⚖1 | M6 direction: re-anchor vs non-saturating | **ALREADY SETTLED BY MEASUREMENT** | a `min(1,·)` cap can only ever penalise, so re-anchoring cannot help a population that is already losing. Shipped as ED-PC-0051. Close the fork. |
| ⚖2 | should armour cost the wearer, in which channel | **RESEARCHABLE** | measured locomotor/metabolic cost of harness (W1) |
| ⚖3 | is disposition a real trade or is aggression just good | **RESEARCHABLE** | Silver's true/false times + Vor/Nach; settled by ablation (W6) |
| ⚖4 | is 35/53 non-participation at plate correct | **RESEARCHABLE — and the question is mis-framed** | Harnischfechten does not ask "can a cut beat plate" (it cannot). It asks "what does a swordsman DO in harness" — half-sword, gap-thrust, Mordhau, ringen. The defect is not the 35; it is that their **alternatives are unmodelled** (W2) |
| ⚖5 | carry context | **RULED 2026-07-29** | executed; N/A |
| ⚖6 | off-hand scope + priority | **RESEARCHABLE** (scope), scheduling is trivial once scoped | I.33, Marozzo, Capo Ferro: the companion arm is not optional equipment in the civilian context, it is the configuration (W3) |
| ⚖7 | is the roster-wide thrust-lean wanted | **RESEARCHABLE, and the carry frame dissolves it** | the thrust-lean is *correct* in the rapier-era civilian duel and *wrong* on the battlefield. It was only ever a single global question because context did not exist. Now it does (W5) |
| ⚖8 | typed weapon record vs untyped dicts | **RULED BY THE ARCHITECTURE DIRECTIVE** | "strict compliance with code architecture complete with primitive-based process and centralized values" selects typing. Executes as W7 |
| N1 | `CLOSE_ENGAGE_M` value | **RESEARCHABLE — and it should not be a free constant at all** | it is a BODY measure and the engine already has `L0`. Derive it (W0) |
| N3 | `point_concentration` ⟂ `curvature` confound | **RESEARCHABLE** | blade typology + in-roster template (W4) |
| N2, N4–N9 | texture debt, layering guard, orphaned ref, MB digest, ledger caps, midnight stamp | **all mechanical** | W8/W9 |

**Genuinely Jordan's, and only these three:**
- **J1** — *feel*: should a duel be decided in 2–3 exchanges or 8–12? Nothing in history fixes lethality pacing for a game.
- **J2** — *scope*: is the grid tactical layer this quarter's target, since it re-homes reach entirely.
- **J3** — *content*: which traditions get authored curricula, and in what order.

Everything else below is investigation, not consultation.

---

## §1 Architecture compliance — the rules every work package below is bound by

Non-negotiable, from CLAUDE.md §8 and `consolidation_v1` §2.3, plus two this session earned:

1. **One physical fact, one primitive, one owner.** No fact charged twice. This session's live
   examples: mass is charged by `wield_heft`/`agility`/`recoverability_factor`/`_recovery_mode_commitment`
   and must not be charged a fifth time; `_puncture_adef` and `wound_impairment` were extracted because
   the same expression had 2 and 4 copies.
2. **Derive from primitives; never gate on a threshold that hides a body constant.** ED-PC-0053's whole
   lesson. If a constant compares against a scale that includes `L0`, it is a fiat gate wearing a
   derivation's clothes.
3. **Centralised values.** Every tunable in `config.py`, exported, round-trip-checked. No inline
   literal. M16's 127 inline literals are a live violation.
4. **Bounded, dimensionless inputs for any scaling term** — NEW, earned this session. Three terms;
   `S_g` (units) and `I_g` (~1000× span) both mis-scaled, `curvature` ([0,1]) could not. **Every
   scaling term ships a range assertion on its multiplier.**
5. **Ablatable.** Every lever must be switchable to zero and reproduce the prior engine exactly.
6. **Grounding tag on every constant**: `[ATTESTED]` (treatise/measurement, cite it),
   `[ASSERTED — first-principles]` (physics reasoning), or `[SIM-CALIBRATE]` (fitted). Mixing these up
   is how `thrust_factor`'s "correctly collapse toward 0" survived.

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
5. **SWEEP** — **mandatory sensitivity sweep over the constant's plausible range**, reported as a
   table. This is the step that was missing from ED-PC-0053 and it is why `CLOSE_ENGAGE_M` cannot now
   prove it wasn't tuned. A non-monotone response is a finding, not noise.
6. **ABLATE** — measure with the term at zero, same seeds, paired.
7. **TEXTURE + AGGREGATE** — report both. A term can move 122/212 armour cells and no field ordering.
8. **RECORD THE SHA** the measurement was taken at. Every field number this session went stale within
   one batch.

**Convergence rule:** iterate 2→7 until the sweep is flat within noise *or* the pre-registration
matches. **Do not iterate the constant to chase a target** — that is the tuning §0's ruling forbids.
If the sweep shows a target-shaped optimum, that is a *disclosure*, not a destination.

---

## §4 Work packages, in dependency order

Each carries: grounding · the primitive it adds or fixes · its falsifier · acceptance.

### W0 — Derive `CLOSE_ENGAGE_M` from the body *(closes N1; unblocks nothing, but repays the worst debt)*
The close measure is anthropometric, and the engine already carries the fighter's own scale in `L0`.
**Make it a derived body primitive, not a free constant** — grappling measure is where the hands can
reach the opponent's body, i.e. a function of arm length, which `L0` already encodes.
· *Falsifier:* the sensitivity sweep (v3 §3.1) must be re-run against the derived value; a body-derived
measure that lands on the same balance optimum is a genuine coincidence and must be shown, not assumed.
· *Acceptance:* `CLOSE_ENGAGE_M` disappears from `config.py` as a free tunable.

### W1 — Armour costs the wearer *(⚖2)*
Currently armour is **free**: it defends and costs nothing. Attested cost is metabolic/locomotor, so
the channel is **stamina/fatigue**, not tempo (tempo is already priced by `wield_heft` — do not charge
mass a fifth time, §1.1). · *Falsifier:* an armoured fighter must lose a *long* fight it wins short.
· *Acceptance:* heavy armour is a genuine trade at some fight length; sweep reports the crossover.

### W2 — Harnischfechten: model the alternatives, not the cut *(⚖4, reframed)*
35/53 weapons cannot decide a fight at plate. **That is historically correct and is not the defect.**
The defect is that the documented responses are absent or unreachable: half-sword (partly present),
gap-thrust (present), **Mordhau** (present but weak), **ringen/grapple in harness** (contact axis
exists; `COVERAGE_GAP['partial']` is plumbed with no caller). · *Falsifier:* a longsword in harness
must have a *non-zero* path to victory that is not its edge. · *Acceptance:* the 35 shrinks because
alternatives became reachable — **not** because cuts started defeating plate.

### W3 — The companion arm *(⚖6, and the rapier's real counterweight)*
Historically the civilian configuration, not an accessory. Three effects on **existing** terms, per the
proposal §13.2: buckler → `coverage='partial'` (already plumbed, no caller); parrying dagger → defender
parry affinity; paired → contact axis. · *Falsifier:* rapier-and-dagger must beat lone rapier; the four
weapons currently measured without an off-hand (`main_gauche`, `paired_short`, `hook_sword`,
`cinquedea`) must leave the field's bottom tail. · *Acceptance:* civilian spread falls **and** the
rapier's outlier status falls with it.

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

### W7 — Typed weapon records + numeric centralisation *(⚖8 ruled, M16/M17)*
The architecture directive selects typing. Absorbs M16's 127 inline literals. **Schedule before further
behavioural batches**, with **M18** (`combat_systems.py`, now 80 fn/1059 LOC — I grew it) split in the
same pass. · *Acceptance:* every constant in `config.py`, exported, round-trip-checked; no module over
~500 LOC.

### W8 — Guard debt *(N2, N5)*
Texture measurement owed for ED-PC-0052 and ED-PC-0054; layering/acyclicity guard (nothing currently
prevents `weapon_physics` importing upward or a cycle forming).

### W9 — Process *(N6–N9)*
Orphaned `CLOSE_EFF_GAP_REF` anchor; MB byte-digest environment instability (MB lane); per-lane archive
cap default; the midnight-rollover stamp regression.

---

## §5 Ordering

**W0 → W7 → W3 → W4/N4 → W2 → W1 → W6 → W5 → W8 → W9.**

Rationale, and it differs from v3: **W7 moves to second.** v3 put the architecture work sixth. But every
behavioural package below it edits token-keyed branches and adds constants, and this session grew the
god-module by three functions while doing exactly that. Doing W7 after W3/W4 means doing it to a larger
target. The register's own M15-before-M6/M7/M9 argument applies with more force now.

**W3 stays the highest-value behavioural package** — it is the only one that is a missing *cost on the
dominant thing* (v3 §1), and its hook is already built.

---

## §6 What this plan does NOT do

- **No closed-phase LEVERAGE/DAMAGE rework.** Reach is ruled to the grid layer. Four levers swept, every
  fix broke `guisarme@heavy`.
- **No re-tuning to hit a field target.** §3's convergence rule forbids it.
- **No new benefit channels on weak weapons** without a measured throughput argument (v3 §1).
