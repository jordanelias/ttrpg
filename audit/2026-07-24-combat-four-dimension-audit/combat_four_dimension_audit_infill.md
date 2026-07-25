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

## 5.2 Batch 5.2 — the ED-PC-0039 review, and what it cost (ED-PC-0040)

The ED-PC-0039 adversarial review was dispatched with an explicit adversarial prior: *"this is the second consecutive
time a fix by this author on this exact code path introduced a new defect; assume the pattern continues until proven
otherwise."* It returned **half-stands, again**. Its verified-green list is real — the 806-test claim, the ×10.7 / 1.62
arithmetic, "defeaters untouched" by the clamp, the F7 argument-threading fix, the genuineness of the post-clamp K
sweep, and no data loss in the register compression. What follows is only what did **not** survive.

**S1 — the "restored participation guard" watched one weapon out of fourteen.** ED-PC-0039 claimed to have restored a
load-bearing plate guard. It asserted `decided[('poleaxe','heavy')] > 0.50`. The review killed `bec_de_corbin` +
`lucerne_hammer` + `goedendag` at plate simultaneously — three-quarters of the percussive defeater class going mute —
and the **full 806-test suite passed**. A guard on one member of a class does not guard the class.

*Fix (ED-PC-0040):* `test_plate_participation_tracks_armour_defeat_capability`, roster-wide and **primitive-derived**.
Membership is never listed: a weapon's capability is `max(adef_cap)` over every mode **and every grip it can reach in a
fight** — including its `HALFSWORD_FORM` target, which the wrapper swaps it into when closed vs medium/heavy. That last
clause is what makes the derivation honest; without it the estoc (base point cap 0.522) and the longsword (0.613) look
sub-threshold while being the two most decisive plate weapons on the board, because in a real fight they half-sword to
1.104 and 1.020. The measured partition is cleanly separated, which is why loose bounds still bite (n=200 vs arming):

| band | derivation | members | decided at plate |
|---|---|---|---|
| clears the tier | best-grip cap ≥ 0.9 | 13 (mace, goedendag, poleaxe, estoc(+halfsword), stiletto, lucerne, bec, rondel, longsword(+halfsword), dagger, misericorde) | 0.59 – 0.99 |
| marginal | 0.72 ≤ cap < 0.9 | 1 (main_gauche, 0.744) | 0.23 |
| well under | cap < 0.45 | 40 | 0.00 – 0.12 |

Three clauses: **forward** (every comfortable defeater settles > 35% — catches the class going mute), a **class-count**
clause (at most 2 of the 13 may drop below 50% — catches a partial die-off that a per-weapon floor would let through),
and the **converse** (nothing far below the threshold may settle ≥ 40% — catches a covert plate-killer). Mutation-verified:
the bec/lucerne/goedendag kill now fails with all three named in the message.

**S1b — the two mutations ED-PC-0039 cited are, at the decided-rate level, null; and saying otherwise was the error.**
Measured directly: zeroing the guisarme's plate damage takes its decided-rate 0.00 → 0.00 (it lands 517 nonzero strikes
in 1572 at plate but never accumulates a decision), and zeroing every long-lever point takes all of spear/yari/ji/
spetum/dangpa/bear_spear/guisarme 0.00 → 0.00. The *only* weapon either mutation observably moves is the **ranseur**
(0.12 → 0.00) — and the ranseur's plate participation is itself a defect (below). Building a guard that catches these
mutations would mean **guarding a defect into permanence**, so ED-PC-0040 does not. The correct statement, which
ED-PC-0039 should have made, is that capability-gating rendered those particular mutations behaviourally inert.

**S2 — a guard comment asserted something false about its own subject.** ED-PC-0039 justified the poleaxe floor with
"capability clears the tier *by construction*, so it cannot be satisfied by luck". Only statically true: the poleaxe's
blunt cap is 1.216 against a 0.72 threshold, but the cap it **realizes** turn-by-turn depends on the mode it selects
(mean ≈ 0.60), and the same commit's own K-sweep shows the poleaxe is *not* K-invariant (13 → 10 → 7 across K = 0/6/12),
directly contradicting the "by construction" framing. Comment corrected in place; the floor is empirical, not structural.

**S3 — the medium tier never round-tripped, and ED-PC-0039 made one weapon worse.** ED-PC-0038 called mail "a tier the
fix was never meant to touch". Measured share vs arming at medium, n=200, at the three commits:

| weapon | 88b86c7 (pre-0038) | 7e4e738 (0038) | HEAD (0039) | net |
|---|---|---|---|---|
| odachi | 0.67 | 0.44 | **0.26** | **−41pp** (0039 made it *worse*) |
| naginata | 0.82 | 0.57 | 0.57 | −25pp (clamp recovered nothing) |
| podao | 0.61 | 0.32 | 0.44 | −17pp (clamp recovered +12) |
| sparr_axe | 0.36 | 0.07 | 0.22 | −14pp (clamp recovered +15) |
| staff | 0.21 | 0.09 | 0.09 | −12pp (clamp recovered nothing) |
| changdao | 0.87 | 0.82 | 0.79 | −8pp |
| tachi | 0.37 | 0.36 | 0.31 | −6pp |
| greatsword / flamberge / katana / sabre / falchion / glaive | — | — | — | flat (≤2pp) |

Two distinct causes, and neither is the one ED-PC-0039 fixed. Staff and naginata were **never in the ADEF_CUT branch**
at all — they select `blunt` and `cut_thrust`, whose caps are positive (0.149, 0.244), so the clamp could not touch
them; their loss is ED-PC-0038's deficit knee operating as designed at a tier nobody re-baselined (medium threshold
0.45 lifts their `t` from 2.5 to 7.0 and 5.6). The odachi's further −18pp is **ED-PC-0039's own grip/room threading**:
the knee now reads the grip-corrected capability instead of the neutral-grip one, which is *more* correct and lowered
its per-strike damage 3.67 → 2.77. That is a defensible change with an undisclosed consequence — recorded here rather
than reverted.

**S5 — the covert plate-killer has a name.** ED-PC-0038's flagship claim was that capability now orders penetration.
ED-PC-0039 admitted the principle was "attenuated, not achieved" but understated the breadth. Concretely: the
**ranseur** (cap 0.284 vs a 0.72 threshold) still settles ~12% of its plate fights and **wins 100% of what it settles**;
`guandao` (cap 0.127) lands mean 2.76 per plate strike and `partisan` (0.171) 1.96 — against a `spear` with better
capability (0.288) at 0.22. The knee is a graded threshold *multiplier*, so a large enough raw magnitude still buys
through. This is F19's residual localised to specific weapons, and it is now guarded in the *direction* it must not
regress (converse clause above) while explicitly not guarded *away*.

**S8 — ED-PC-0038's ledger stated a result that is flatly false.** It recorded "spear/yari/estoc → 0" per landed hit at
plate. Measured at all three commits, the **estoc is the single most decisive plate weapon on the board**: it settles
99% of its plate fights, lands nonzero damage on 93% of its strikes, mean 12.84 — because it auto-half-swords to a
1.104 capability, the highest point capability in the roster. The spear is not 0 either (0.22 nonzero rate, mean 0.22 —
i.e. it occasionally finds a gap for 1). Only the yari is near-0 (0.19 / 0.19, same shape). Retracted in ED-PC-0040's
ledger entry; the original entry is left intact because the ledger is append-only.

**S4 — the clamp erased grading inside the class it rescued.** Flooring capability at 0 is right as a *floor* and wrong
as a *model*: every pure cutter now sits at exactly 0, so the knee cannot distinguish a bardiche from a shamshir. That
distinction is F21's job (mass/keenness grading of `ADEF_CUT` in the sigma path) and batch 6 must now carry it, because
0039 removed the only place it was — however wrongly — being expressed.

**S9 — the index overclaimed its own review record.** Commit `257d9a7` said batches 1–3 landed clean and "both reviews
so far returned stands, nothing reverted"; batches 4 and 5 had both half-stood by then. Corrected in the index, along
with "cutter class restored" → "un-annihilated, not restored" and "participation guard restored" → one weapon of
fourteen. `HANDOFF_PC.md` had not been updated since batch 3; updated.

**F24 — the new finding this follow-through surfaced: selection contradicts damage.** Instrumenting `core.strike` by
selected head at plate (20 fights/weapon, whole roster) shows `select_mode` repeatedly choosing a head that provably
cannot wound what is in front of it:

| weapon | selected head at plate | strikes | nonzero rate | mean damage |
|---|---|---|---|---|
| falchion | `point` | 46 | 0.00 | 0.00 |
| glaive | `point` | 59 | 0.00 | 0.00 |
| sabre | `point` | 56 | 0.00 | 0.00 |
| podao | `point` | 35 | 0.00 | 0.00 |
| podao | `curved_cut` | 10 | **1.00** | **2.40** |
| odachi | `blunt` | 68 | 0.01 | 0.01 |
| arming (reference) | `cut_thrust` | 146 | 0.76 | 1.20 |

The podao row is the clean demonstration: it selects the mode that does nothing 78% of the time, over its own mode that
works every time. Ten weapons land **literally zero** across the whole sample. And at *medium*, every 2H sword flips to
`blunt` (odachi 703/703 strikes) for a mean of 2.77 against the arming sword's 8.48 — an ōdachi choosing to pommel-strike
a man in mail rather than cut him, every single beat. This is the ED-PC-0038 defect class one layer up: 0038 reconciled
*damage* with *capability*, but *selection* is still keyed on afforded effectiveness with no reference to whether the
chosen head can defeat the armour it faces. **Deliberately not patched in ED-PC-0040** — it is a `select_mode` change
with golden-parity blast radius, and bundling it into a review-response commit is precisely the pattern that made
batches 4, 5 and 5.1 all half-stand.

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
