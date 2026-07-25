# Combat Engine — Four-Dimension Read-Only Audit + Remediation (INFILL)

Prose companion to `combat_four_dimension_audit_index.md` (the skeleton: method summary, finding roster, batch
ledger). This file carries the evidence, the reasoning, and the per-batch remediation record. It is the **detail
home** for the ED-PC-0034.. sequence — the register (`references/id_reservations.yaml`) and the lane ledger keep
only skeleton pointers here, per CLAUDE.md §4's co-filing convention (Jordan, 2026-07-24: "skeleton and infill").

## 1. Why this audit, and what it is not

The engine had just absorbed a five-ED arc in one session (ED-PC-0029..0033: arrest-impulse, true-time reach edge,
closed-phase disengage, percussion→stamina, penetration threshold, stale-grip fix). That is a lot of new mechanism
landing fast on a system whose stated philosophy is emergence-from-primitives. The charter was therefore not "does
it pass" — it does; the suite is green — but **"what did we accumulate?"** along four axes where a fast-moving
engine silently rots: designer fiat, dead wires, internal contradiction, and balance pathology.

Producing and checking are different jobs (CLAUDE.md §0). Each auditor was `fable`-tier, **read-only**, and blind
to the others' reasoning — structural independence, not merely instructed independence. Each was additionally
directed (Jordan, mid-run) to cover **all directions and conditionals**: every `if/elif/else`, all four armour
tiers, every use-mode branch, and both signs of every differential term — enumerate the conditional space rather
than sample it. That directive earned its keep: three of the accepted findings (F3's skill>1 sign flip, F12's dead
shear branch, F1's first-engagement-vs-later divergence) exist **only** in a branch the common path never visits.

Every finding below was re-verified by hand against the code before acceptance. This matters: the repo's own
anti-fabrication gate is known-leaky (CLAUDE.md §7), and an auditor's confident prose is not evidence. Two reported
findings were **downgraded on verification** and are not carried as defects (see §6).

## 2. What the audit found, in one paragraph

The engine is in better shape than its churn rate would predict. The derivation core — mass model, MoI/PoB, grip
kinematics, affordances, mode selection — is genuinely emergent and has repeatedly retired its own fiat with
ledgered adversarial audits; the self-tagging discipline (`[FIAT]`/`[SIM-CALIBRATE]`/`[ASSERTED]`) is real; the
sign conventions that matter are consistent between definition and consumer; and every provenance citation spot-
checked resolved to a real, matching ledger entry. What has accumulated is (a) a thin rim of **outcome-level fiat**
in the wrapper that overrides or bypasses the emergent σ-machinery, (b) ~5% of the config surface as **dead
scaffolding**, some of it leaking into the Godot-facing typed contract, (c) a **prose layer lagging a fast code
layer**, and (d) a balance surface dominated by **two structural threshold discontinuities** that make win-rate
nearly a step function and that no amount of per-weapon tuning can reach around.

## 3. The finding that reframes the balance work (F16/F17)

The single most consequential result is that the off-plate reach over-buff (F18) — which the previous session tried
and failed to tune down toward Jordan's ~0.75 target — is **not a tuning problem at all**. Two thresholds dominate:

**F16 — the first-actor race is a sign discontinuity.** `wrapper.py` selects `aggressor = max(actors, key=ready)`,
and `ready` resets to 0 at every close. The marginally faster weapon is therefore *strictly first* in every burst,
and that ordering compounds with `ATTACKER_BIAS` (F14) and the Vor snowball. Measured: a jian holds a **+1.5%**
close-tempo edge over an arming sword and converts it into a **2:1 action economy** (679 vs 342 closed rolls over
150 fights). The clean proof is an ablation on a synthetic arming clone: stepping mass **1.18 → 1.20 kg**
(close_tempo Δ = 0.0002) steps the win-rate **57.2% ↔ 41.6%**, flat on either side. This one mechanism explains
most of the otherwise inexplicable 8–78% scatter among near-identical one-handed swords.

**F17 — the `closed = (gap ≤ 0.3)` latch is a cliff.** A synthetic reach ladder (N=600/rung) reads 51/48/51/55% at
gaps 0.00–0.28 and then **63.8% at gap 0.32** — a +9pp step across two centimetres — rising to the ~93–95% cap by
gap 1.5, after which the gradient is spent. Live confirmation: katana (gap 0.22 → starts closed) 28.7% vs tachi
(gap 0.44 → starts open) 62.5%, on otherwise near-identical records; goedendag (reach 6.29) 80.0% vs mace (5.14)
17.8%, the same weapon concept on opposite sides of the cliff.

Together these explain F18's identity erasure: **26 weapons with reach ≥ 6.5 all sit at 92–97% at none/light/medium
(mean 94.3, σ = 1.2)** — a spear is statistically indistinguishable from a greatsword. Reach is currently a *binary
trait*, not a graded property, and the `REACH_W` medium fade visibly does nothing. This is why the previous
session's four independent levers (`STOPHIT_CHANCE`, stop-hit commitment, `REPRESENT_BASE`, a closed-measure crowd
penalty) each failed to reach 0.75 without breaking the guisarme@heavy floor: they were all trying to move a value
that is set by which side of a threshold a weapon lands on. **Batch 4 must fix the thresholds before any reach
re-tune is meaningful.**

## 4. The second systemic split (F19/F20/F21)

The **damage path and the `adef_cap` path disagree about armour**. Three symptoms, one cause:

- **Covert plate-killers.** partisan (93.2% of 73% decided), ranseur (90.8%/76%), guandao (90.2%/68%) are as
  decisive at plate as a poleaxe (94.9%/97%), while spear/yari/guisarme correctly stalemate. Measured per-success
  hit damage vs heavy: partisan 6, guandao 6, ranseur 4 ≈ poleaxe 7 — versus spear/yari/guisarme at **1** — even
  though the broad-bladed weapons have *lower* gap precision (partisan 0.47 vs spear 0.72) and *lower* `adef_cap`
  (0.176 vs 0.288). The damage path rewards head mass / cut magnitude through plate where the σ path correctly says
  they cannot defeat it. A narrow spear point seeking a gap better than a broad partisan blade is the physically
  correct ordering, and the engine inverts it. This also silently undercuts ED-PC-0033's own story ("at plate the
  gap-defeaters earn their presentations") — these three earn theirs through a damage-model leak, not presentation.
- **jian/tsurugi plate paradox.** A 0.6–0.8 kg civilian sword is the third-best plate class after longsword/estoc
  (94.8% of a 36%/19% decided residue) off a **0.04-point** gap-cap grading edge over the arming sword, amplified
  by the crowd gate and the same damage path.
- **The flat `ADEF_CUT = −0.90` cutter cliff.** One constant for every cut regardless of mass or keenness, so a
  bardiche cleave and a sabre slash are graded identically. A padded gambeson turns a falchion into an **8%**
  weapon vs an arming sword — its light-tier deficit (1.2) is larger than a *spear's deficit at plate*. The
  sparr_axe (90.0 → 20.3 light→medium) and bardiche (92.0 → 45.4) cliffs are this same defect carried by reach.

## 5. Batch 1 — remediation record (ED-PC-0034)

Three genuine correctness defects, all verified before and after.

**F1 — `represent_measure_p` read stale/native `sel_head` + grip.** The ED-PC-0033 crowd gate is evaluated at
*engagement start*, outside the per-beat loop that refreshes `sel_*`. So it read whatever the **prior** engagement's
closed phase left behind — or, on the very first engagement, nothing, falling back to the bare **native** head.
Consequence, measured: a multi-mode weapon whose native head is a cutter was read as maximally crowded on
engagement 1 and quite differently thereafter — katana **0.000 → 0.274**, guisarme **0.092 → 0.236**, hook_sword
**0.000 → 0.425**, guandao **0.000 → 0.038**, for the identical matchup. That is precisely the state-carryover
defect class ED-PC-0033 had just fixed for `grip_position`, reintroduced one call up the stack — the audit's
sharpest catch, and in code written the same session.

*Fix:* the gate now derives the mode it is asking about, purely and locally. Since the question is "what would this
weapon present at **open** measure?", the geometry is pinned explicitly — `select_mode(..., grip=0.0, room=1.0)`
(full extension, nothing gathered) — rather than read from live state. `select_mode` gained optional `grip`/`room`
overrides following the **JD-9 idiom `reach_base` already uses** (`None` = read live, explicit = pin for a
hypothetical), which keeps both existing wrapper call sites byte-identical. Verified path-independent: **0 of 24**
weapon×tier cells drift after adversarially corrupting *every* live circumstance field (`sel_head`, `sel_gap`,
`sel_perc`, `sel_pc`, `sel_eff`, `grip_position`, `range_avail`). Note the first attempt fixed only `sel_head` and
still drifted for the poleaxe (0.494 → 1.000) because `select_mode` itself reads live grip internally — the
override closes that too.

**F2 — `overcommit_exposure` was not floored at 0, contradicting its own docstring.** The `max(0.0, …)` wrapped
only the first term, so an agile, disciplined fighter at shallow commit returned a **negative** exposure (−0.37
measured for an English `true_times` build at commit 2). The wrapper guards its initiative/poise loss with `if > 0`,
but fed the *un-floored* value straight into `RIPOSTE_ON_FAIL`/`RIPOSTE_ON_NEUTRALIZE` — so negative exposure
silently pushed the defender's riposte chance **below its configured base**, a mechanic the docstring said could
not exist. *Fix:* the floor wraps the whole expression. The physics: not over-committing means you are not *extra*
exposed; it should not make you harder to riposte than the base contemplates, and anti-overcommit is a *mitigation*
of exposure, not a bonus that can invert it. Verified ≥ 0 across 80 build/commit combinations.

**F3 — `contact.grab_sigma`'s edge hazard sign-flipped for trained grapplers.** The term reads
`GRAB_EDGE_K · hazard · (1 − skill('grab'))`, and skills are documented as *uncapped* ("positive = trained bonus").
For any grab skill > 1 the factor goes negative: seizing an opponent's **live double edge** bare-handed then
*improved* the grab, scaling with how sharp the grabbed blade is. *Fix:* the mitigation is clamped at 0 — a
highly-trained grappler is immune to the hazard, never rewarded by it. Verified monotone across skill 0 → 3.

**F4 — the tradition-lever texture instrument was under-powered, and it mattered.** Fixing F2 moved the
katana/arming cell 4/60 → 3/60 and tripped `test_levers_add_texture_without_shifting_balance` — *without touching a
single lever*. Investigation rather than re-baselining: the true divergence rate is **~12–13%** (measured n=200:
katana/arming 25/200, dagger/arming 26/200), so at n=60 the expectation is 7.5 with SE ≈ 2.6 — the old `>= 4` floor
sat about one SE below the mean, i.e. a knife-edge that any unrelated change to the RNG trajectory could trip, and
the docstring's claimed "observed ~16–28%" was never reproducible at that n. *Fix:* **raise** n to 200 (a stronger
instrument, ~4 s) and set the floor at a proportional 5% — roughly 2.5× margin below the true rate, while still
failing loudly if the levers go dead (which reads 0). This tightens rigour rather than relaxing the guard; the
isolation that established F2-not-a-lever as the cause is recorded above.

*Batch 1 result:* full `tests/valoria` suite green — **686 passed, 1 xfailed**, identical to the pre-batch baseline.
Balance impact is contained: the affected multi-mode cutters at plate are mostly attrition stalemates (katana 3%,
hook_sword 2%, odachi 3% decided), and guandao/guisarme remain where Batch 5 will address them on the merits.

## 6. Reported but downgraded on verification

Two auditor claims did not survive hand-checking and are **not** carried as defects. Recorded because a rejected
finding is as much a part of the audit record as an accepted one:

- **"Combat Pool is defined three incompatible ways"** (CLAUDE.md §5 states this as a live hazard). Verified: the
  live engine (`core.resolution_pool = max(5, History+6)`), `engine/params/core.md`, and
  `references/module_contracts.yaml` **agree**. Only the explicitly quarantined `references/values_master.yaml`
  diverges (and it diverges from *itself*, twice, under a nonexistent `engine/params/combat.md` path). The ledger
  was right and CLAUDE.md §5 overstates a resolved hazard — a documentation fix, not an engine defect.
- **`GAP_EXPOSURE` "near-flat / physically mislabelled"** was reported as fiat. It is `[SIM-CALIBRATE]`-tagged,
  which is exactly the repo's own standard for "structure grounded, magnitude fit to the harness", and its
  enumeration showed the intended monotone behaviour. The honest residual — that the *material* axis does little
  work because weapon-side `gap_prec` dominates — is real but is a naming overclaim, folded into F19's scope rather
  than carried separately.

## 7. Standing risk to watch

The heavy-tier decisive/stalemate classification now sits at the intersection of **three independently-tuned
mechanisms**: `thrust_authority` (PC-5), the `PEN_THR` heavy knee (ED-PC-0032, which scrubs sub-threshold damage
for everyone), and `percussion_stagger`'s stamina path (ED-PC-0031, which can decide a fight **without wounds** and
is therefore invisible to `PEN_THR`). The longsword's membership in the balance guard's `_DEFEATS_PLATE` set depends
on its half-sword thrust clearing the 6.5 knee, so any `PEN_THR`/`DMG_SCALE` retune can flip its classification and
trip the guard in either direction. Batches 5 and 6 both touch this intersection and must re-validate it explicitly.

Relatedly: ~29 of 51 weapons decide **fewer than 15%** of their fights at heavy. Raw win-share at that tier is
therefore actively misleading (a cell can read 1.00 on a handful of decided fights), and the eventual videogame
needs a presentation for "neither fighter could hurt the other for twelve bouts". All balance numbers in this audit
are reported as **win-share of decided + decided-rate** for that reason.
