I have what I need. The probe empirically confirmed the one load-bearing interaction none of the four surfaces tested in isolation, and `HANDOFF_MB.md` shows R1/R3 are explicitly on RC-5's untriaged list with DG-1..DG-5 already ruled (so new gates start at DG-6). Here is the synthesis.

---

# Wave 2 Synthesis — Movement, Tactics, Reach, and Ranged Weaponry
## Mass-battle gauge investigation, chief-synthesizer report for Jordan

**Scope:** the four explicitly-requested surfaces — movement/pathing/routes, stances/tactics/orders, reach/targeting, ranged/volley. Feeds directly into **RC-5** (the 9-rows-failing triage in `handoffs/HANDOFF_MB.md`), which already lists **R1 and R3** among its untriaged rows. All findings below were independently adversarially critiqued; I report only what survived, with the corrections the critics forced, plus one new empirical result of my own.

---

## Executive summary

The two ranged rows (R1, R3) — the surfaces most directly in scope — are **both explained, and both are fundamentally harness-construction failures, not deep engine calibration failures.** But the "cheap fix" story has a sting in the tail that no single surface caught, which I verified empirically (see §A).

Three things are true at once:

1. **R1 (ranged wins 65% when it should lose 0-30%) is dominated by a one-parameter harness bug**: the "ranged" side is built with `troop_type='infantry'` (the default), so it inherits full infantry stats (4/5/6) instead of archers' (3/3/3). Setting `troop_type='archers'` flips R1 from ~65-70% to **0%**, inside the band. A genuine engine bug (volley fired from inside melee) contributes but is *not* the row-flipper.

2. **R3 (100% draw) is a deployment + stance construction bug**: both sides `hold` while spawned out of volley range, so nothing ever moves or fires. An already-shipped instruction (`kite`) resolves it — **but only if the units keep the default disc-5 stats.** The moment you also apply R1's "correct archers" fix (disc-3), a latent node-path movement bug re-freezes them. The two cheap fixes are mutually incompatible without an engine change.

3. **Speed and tactical behavior are the two stats/systems that were left behind by this session's troop-grounding work.** Power/discipline/morale got pushed down to the troop type (POOL_QUALITY_MODEL / DG-3/DG-4). **Speed did not** (no `speed` field in `TROOP_TYPE_STATS`; a single hardcoded binary cavalry multiplier). And **volley's combat pool did not get the POOL_QUALITY_MODEL treatment either** — that entire investment went into melee's `subunit_combat_pool` and never touched `fire()`. Both are the direct, nameable siblings of the gap Jordan already ruled on.

The tactical "strategy" layer is **real as architecture but ~80% decorative in practice** (details in §3).

---

## A. New empirical result — the R1 and R3 fixes collide (verified this session)

None of the four surfaces ran the combination a *fully corrected* R1/R3 would use. Each tested its own fix in isolation:
- The R3 "kite fix" was validated with **default** stats (discipline=5).
- The R1 "archers fix" uses discipline=3 but with **`hold`** (so the unit never needs to move).
- The node-path speed-floor bug was verified in isolation but never connected to the kite fix.

I ran the missing combination (`tests/sim/mass_battle`, live defaults, n=10/variant):

```
node-path step (cells/tick) for a Line body:
    disc=5 balanced   -> step=1     disc=3 balanced   -> step=0
    disc=5 aggressive -> step=2     disc=3 aggressive -> step=1
    disc=5 retreat    -> step=1     disc=3 retreat    -> step=0

R3 variants (n=10):
  (A) hold + default stats [baseline]     A=0  B=0  draw=10   (frozen — reproduces R3 failure)
  (B) kite + DEFAULT stats (disc=5)       A=8  B=2  draw=0    (resolves — reproduces critic's fix)
  (C) kite + CORRECT archers (disc=3)     A=0  B=0  draw=10   (RE-FROZEN)
```

**Mechanism (confirmed by code at `hierarchy/units.py:836`):** `step = max(0, floor(base * disc_mult) + stance_mod)`. For a Line (`base`=1), discipline 3 (`disc_mult`=0.7), balanced (`stance_mod`=0): `floor(0.7) = 0`. The live `_node_advance` has **no fractional-velocity accumulator** — that carry (`_speed_accum`) exists only in the dead legacy path (`units.py:1109-1111`). So a correctly-statted archer (disc 3) under `balanced` computes step 0 and **can never close from its spawn to firing range.** `kite` cannot help a unit that physically cannot move.

**Consequence for the recommendations:** "fix R1 by making it archers" and "fix R3 with kite" cannot both be done *with historically-correct stats* until the node-path speed floor is fixed. This promotes a finding that all four producers rated "latent / currently invisible" into a **fix-blocking prerequisite.** This is the single most decision-relevant new result of the wave.

---

## 1. Ranked root-cause list (CONFIRMED findings only; REFUTED/unverifiable discarded)

| # | Root cause | Surface(s) | Bucket | Role in the current 7/20 | Confidence |
|---|---|---|---|---|---|
| 1 | **R1 built `troop_type='infantry'`, not `'archers'`** — inherits 4/5/6, not 3/3/3, because `build_unit` builds `Subunit` directly, bypassing the only `TROOP_TYPE_STATS`-reading constructor | ranged (also found by movement critic) | **harness-artifact** | **Flips R1** (65-70% → 0%, single param) | Very high (2 producers + critic, matching numbers) |
| 2 | **R3 `hold` + out-of-range deployment → literal zero-engagement** (0 volleys, 0 casualties, 20-turn draw) | movement, stances, ranged (all 3) | **harness-artifact** | **Explains R3** (100% draw / UNRESOLVED) | Very high (3 surfaces + critics, reproduced) |
| 3 | **Node-path speed floor**: `_node_advance` lacks the legacy fractional accumulator → any disc∈[3,5) unit is frozen at step 0 under `balanced`/`retreat` | stances (critic; missed by all producers) | **engine-defect** | Latent for current gauge, **but blocks the correct fix for #2** (proven §A) | Very high (I reproduced it) |
| 4 | **Volley/melee standoff-floor collision**: `VOLLEY_MIN_RANGE=2` == melee standoff `2.0`, so a ranged unit locked in melee fires a full **unreciprocated** volley every tick | movement | **engine-defect** | Contributes to R1 inflation; **not** the flipper (archers still lose 0/40 with it live) | High; critic found it **~3× worse** than stated (15-36% of max HP, not 5-12%) |
| 5 | **Speed is not troop-grounded** — no `speed` in `TROOP_TYPE_STATS`; only a hardcoded binary `troop_type in ('cavalry','mounted_archers')` → `PC_CAVALRY_SPEED_MULT` | all 4 | **design-tradeoff-needs-jordan** | Not a current flipper; **the headline answer to the grounding directive** | Very high (unanimous, 5 files cited) |
| 6 | **Tactics/behavior is not troop-grounded** — `ROLE_SPEC`/`role_allowed` 0% exercised; ~11-12 of ~15 instruction strings inert (byte-identical outcomes) | stances, movement, ranged | **design-tradeoff-needs-jordan** | Cross-cutting; the "is strategy real" answer (§3) | Very high (two independent instruction sweeps) |
| 7 | **Volley pool never got POOL_QUALITY_MODEL** — melee bakes `eff_size` into the dice pool; volley's `pool = max(1, eff_power − _vpen)` never does (numbers enter only post-roll) | ranged | **design-tradeoff-needs-jordan** | The melee/ranged asymmetry (§4) | High (confirmed) |
| 8 | **Frozen momentum / non-decaying `charge_pen`**: `cell_last_speed` freezes at nominal step, never decays; flat `charge_pen=3` applied every tick, not as a one-shot impulse | movement | **engine-defect** | Contributing to cavalry rows C1-C7; magnitude **unquantified** | High (critic reproduced constant 2.0/1.0 momentum) |
| 9 | **Reach ratification landmine**: `TROOP_TYPE_REACH={}` makes the recoil gate's reach-half a no-op; filling it "cavalry lance = long" flips currently-**passing** C2/C6 | reach | **design-tradeoff-needs-jordan** (partly already-disclosed) | Threatens 2 *passing* rows in future; **0 current failing rows** | High on mechanism; severity **demoted** by critic (see §6) |
| — | Minor / inert / cross-referenced (below the fold) | — | — | — | — |

**Below-the-fold (CONFIRMED but not material to current divergence):** envelop wing **phase-2** contact stall (movement #7 — producer's "commitment never fires" was *refuted*; corrected to a post-commitment stall; mostly wave-1 envelopment territory); `_kite_goal` melee hold-band is dead code (`PC_KITE_STANDOFF=5 > far_bound≤1.5`) — latent; `cell_speed`'s `tier` parameter is dead code; the Order substrate exercises only 2 of 4 trigger kinds and is never chained (coverage gap); `nearest`-target flicker (real but bounded away from combat outcomes); `_find_contacts_field` has zero test coverage / `FIELD_CONTACT` never set to 1; `resolve_cross_side_contention` is a confirmed no-op with **no live speed-priority successor**; the legacy path-length budget is unbuilt and **not** load-bearing; three hand-rolled ranged penalty constants (`_vpen`, `RANGED_MELEE_SIGMA=-1.0`, legacy `//3`) are unit_type-keyed magic numbers rather than troop-derived.

---

## 2. Bucket discipline

- **harness-artifact (fix the gauge, not the engine):** #1 (R1 troop_type), #2 (R3 hold/deployment). These are the two that explain the two *failing* ranged rows.
- **engine-defect (safe to fix, old behavior ablation-gated):** #3 (node-path speed floor), #4 (volley/standoff collision), #8 (frozen momentum/charge_pen). Note #4's *magnitude* (the new floor) is itself a small ruling.
- **design-tradeoff-needs-jordan:** #5 (speed granularity), #6 (tactics grounding), #7 (volley pool formula), #9 (reach ratification).
- **already-disclosed (cite, don't re-litigate):** reach emptiness, `resolve_cross_side_contention` no-op, unbuilt path budget, legacy/node divergence, legacy maneuver code being unreachable. *Caveat:* the critics found two items the producers **mislabeled** as "already-disclosed" — the Order-substrate 2/4-trigger-kinds observation and the ROLE_SPEC caller-gating are **new** observations, and the config/orchestration comments calling ROLE_SPEC "INERT" are **stale/wrong** (engine Stage D already wired the construction-time gate).

**Process note:** producers coined non-canonical hybrid buckets ("already-disclosed-confirmed/refuted"); I have normalized everything to the four canonical buckets. One internal inconsistency to be aware of: the ranged surface bucketed the hand-rolled-penalty finding "engine-defect" while its own fix text says "not a functional bug… cleanup item" — treat it as design-coherence cleanup, not a bug.

---

## 3. Is "strategy" real, or decorative? — verdict

**Troop type now grounds STATS; it does not yet ground BEHAVIOR. The tactical layer exists as architecture but is largely decorative in the surface the gauge exercises.** This is corroborated across three surfaces and confirmed by every critic who checked it:

- **The role scaffold is genuinely wired but 0% exercised.** `TROOP_TYPE_ROLES` + `ROLE_SPEC` + `role_allowed` form a real construction-time gate (a `ValueError` on a troop-type/tactic mismatch, plus shape/instruction defaulting). But it only fires when a caller passes `role=`, and **no builder in the 20-row battery ever does** — every stance/instruction is a raw, unvalidated kwarg. The apparent historical fitness (cavalry envelop, ranged hold) is the **test author's own discipline, not an engine-enforced constraint.**
- **~11-12 of ~15 instruction strings are inert.** Two independent sweeps (assigning `pursue/harass/loose/screen/advance/lure/shoot_move/reserve/pin/charge` vs nothing) produced **byte-identical** winner/turn sequences. Only `brace`, `envelop`, `sweep`, `kite`, `yield` gate real behavior. The two most name-suggestive tags — **`hold` and `volley` — do nothing as instructions**; their apparent effect comes from *separate* fields (`stance`, `unit_type`) that `ROLE_SPEC` never sets. So `role='VolleyLine'` yields `stance='balanced'` with an inert `('volley','hold')` tuple — it does **not** produce a static shooter.
- **The orders/strategy substrate is real but barely used.** `check_orders` implements 4 trigger kinds with working logic, but `Order()` is constructed in exactly **2 places** in the whole package, using only 2 of the 4 kinds (`tick:`, `enemy_range:`), never chained. Multi-step battle plans are entirely unvalidated surface area.
- **Stance:** 4 values exist; only `hold`/`balanced` are used. `retreat`/`aggressive` are behaviorally real (retreat reverses the vector) but unexercised — and (critic addendum) under troop-grounded discipline, `retreat` *also* floors to step 0, so it is not the clean "differs in direction only" story the producer claimed.

**What this means:** a cavalry subunit and an infantry subunit given identical instructions today **fight with different dice but make identical maneuver decisions.** Jordan's own role scaffold proposes that troop type should gate the behavioral menu too; that half of the design is almost entirely unbuilt. This is the behavioral sibling of the stat-grounding gap — real, nameable, and half-finished, exactly as the brief hypothesized.

---

## 4. Melee vs. ranged pool-formula asymmetry — verdict

**POOL_QUALITY_MODEL was applied to melee only. The volley path was never brought under it.** The entire DG-3/DG-4 "bottom-up per-cell troop-density" investment (and the partition-invariance fix) went into `subunit_combat_pool`; `fire()` was never touched. Concretely:

- **Melee** (`core/exchange.py:110`): `raw = eff_power × eff_size × POOL_QUALITY_SCALE + …` — troop **numbers are inside the dice-pool count**, so they scale the discreteness and variance of the roll.
- **Volley** (`orchestration.py:1154-1166`): `pool = max(1, eff_power − _vpen)` — `eff_size` is **absent from the pool**. Numbers enter only *after* the roll, as a linear `K_SQUARE × eff_size` multiplier on net successes (Lanchester Square-Law, when enabled). Confirmed by trace: a shrinking archer's melee pool visibly shrinks tick-over-tick (5→4→3→2→1); its volley pool stays essentially flat (4→3).

So numbers scale melee's *roll* but only volley's *outcome magnitude*, post-hoc. This is a genuine, directive-relevant asymmetry — "troop × density × cells → power" is half-applied.

**The catch that makes this a Jordan ruling, not a silent fix:** volley *already* has a numbers term (`K_SQUARE × eff_size`) modeling the aimed-fire N² concentration effect. Folding `eff_size` into the base pool **and** keeping the post-roll `K_SQUARE × eff_size` would **double-count numbers** — once linearly in the pool, once quadratically after. Whether that's the intended reading of the Square Law is a design call. (Relatedly, `VOLLEY_TN=6` and `RANGED_DR_DEFAULT=2` are single global constants applied to every ranged type; the per-weapon `ARSENAL` distinctions exist but are disclosed as "NOT YET WIRED" — a third, lower-priority axis on which ranged is not troop/weapon-grounded.)

---

## 5. Recommended next actions

### (a) Safe, contained fixes — do now (ablation-gated, then `bat.py` byte-exact check before landing)

1. **R1: set `troop_type='archers'` on the ranged side in `gauge_mb.py`'s R1/R3 rows.** Single-parameter change, empirically flips R1 to pass. *(Feeds RC-5's R1 triage.)*
2. **Gate volley on true melee contact** (`d > standoff_from_reach(shooter, target)`, not merely `≥ VOLLEY_MIN_RANGE`) so a locked-in-melee archer stops firing — matches the existing "no volleying while yielding" precedent (DG-2). This is a genuine engine bug worth fixing regardless of R1. *(The exact new floor is a magnitude — confirm with Jordan; see DG-6c.)*
3. **Correct the stale comments** in `config.py`/`orchestration.py` that call `ROLE_SPEC`/`TROOP_TYPE_ROLES` "INERT" — the construction-time gate is wired. Cheap, prevents a future session mis-reading the state.

**Do NOT bundle the R3 fix into (a).** Fixing R3 "correctly" (archers + kite) requires the node-path floor fix first (§A) — that is a ruling, not a contained fix. See DG-6a.

### (b) Jordan-ruling decision points (proposed DG-6…DG-10; matching the DG-1..DG-5 / AskUserQuestion model)

- **DG-6a — Node-path speed floor (the fix-blocker).** Fixing R1 (archers, disc 3) and R3 (kite) with historically-correct stats is impossible while `_node_advance` floors disc-3 movement to 0. Options: **(i)** port the legacy fractional-velocity accumulator (`_speed_accum`) into `_node_advance` so disc-3 troops move at a realized ~0.7 cells/tick *(recommended — unblocks correct-stats rows and is the direction the grounding directive points)*; **(ii)** leave it, and require `aggressive` stance / disc≥5 for any moving non-cavalry row *(a hack — `aggressive` is doing accidental work)*; **(iii)** leave it, and keep R3 on default disc-5 stats *(accepts a permanent stat-correctness inconsistency between R1 and R3)*.
- **DG-6b — Speed granularity.** Should speed become a per-troop-type stat (a `speed`/multiplier column co-located with `TROOP_TYPE_STATS`), retiring the hardcoded binary cavalry check — mirroring the pool-formula ruling? Options: **(i)** add per-type speed multipliers now *(needs cited magnitudes — anti-fabrication: don't invent numbers)*; **(ii)** keep the binary cavalry flag, defer *(status quo)*; **(iii)** minimal: at least wire the dead `tier` parameter and/or `Unit.speed` into movement so quality has *some* effect.
- **DG-6c — Volley pool + Square-Law double-count.** Should volley's base pool fold in `eff_size` to match melee's POOL_QUALITY_MODEL? Options: **(i)** `eff_size` in base pool **and drop** the post-roll `K_SQUARE × eff_size` *(single-counts numbers)*; **(ii)** keep the post-roll multiplier, leave the base pool as-is *(status quo — accepts the melee/ranged asymmetry)*; **(iii)** both *(double-counts — flagged as likely wrong)*. Whichever, gate behind a new env-var default, byte-exact validated.
- **DG-6d — Reach ratification (before filling `TROOP_TYPE_REACH`).** Does a couched lance out-reach a set pike/spear wall in sustained contact, or the reverse? Options: **(i)** infantry-polearms get `REACH_LONG`, cavalry stays `SHORT` *(preserves the current C2/C6 repel for the right historical reason — Courtrai/Swiss precedent)*; **(ii)** cavalry lance = `REACH_LONG` *(historically defensible for the charge instant, but empirically flips C2/C6 to cavalry-wins and disables the reciprocal recoil)*; **(iii)** leave empty pending a dedicated reach design pass. **Do not treat filling this table as inert data entry** — it is a live behavioral lever.
- **DG-6e — `hold` semantics for ranged.** Should `stance='hold'` on a ranged body permit a one-time advance to its own effective range, then hold? Options: **(i)** yes — add advance-to-range-then-hold *(changes `hold` engine-wide)*; **(ii)** no — keep `hold` literal, require `kite` for closing *(then R3 must be rebuilt via kite — depends on DG-6a)*; **(iii)** add a distinct `VolleyLine`-style primitive.
- **DG-6f — Tactics grounding.** Retrofit the gauge to construct via `role=` (exercising `role_allowed`), and wire vs. de-scope the ~11 inert instruction strings? Options: **(i)** wire the historically-real ones (`screen`/`pursue`/`harass`) and route gauge rows through `role=`; **(ii)** de-scope `ROLE_SPEC` as aspirational, correct docstrings, stop advertising inert tags; **(iii)** status quo (raw kwargs, ungrounded tactics).

### (c) Needs more investigation before acting

- **Confirm the R1/volley fixes are `bat.py` byte-exact clean** and don't ripple into the other 18 rows — required before landing (a)(1)/(a)(2).
- **Quantify finding #8** (frozen momentum/`charge_pen`) contribution to the specific C1-C7 percentages — every surface left it unquantified.
- **C3 mirror asymmetry (60/40)** — unresolved by both the movement producer and its critic; likely wave-1 cascade-ordering, not a movement/tactics cause.
- **The `sweep` maneuver's transit behavior** — under-investigated relative to `envelop`.

---

## 6. Honest disagreements and unresolved tensions

- **R3 classification (the sharpest disagreement).** The movement producer called it *design-tradeoff-needs-jordan* ("no primitive exists; needs new engine work"). Its **own critic refuted that**, and the stances + ranged surfaces both bucketed it *harness-artifact* — `kite` already exists and resolves it. Consensus: **harness-artifact.** **But my probe (§A) adds the twist neither side saw:** the kite fix works *only* with the wrong (disc-5) stats; with correct archers stats it re-freezes. So R3 is a harness-artifact whose fix is **gated on an engine ruling (DG-6a)** — the movement producer's instinct that "something engine-level is missing" was directionally right, just for the wrong reason.
- **R1 "dominant cause" — two surfaces both claimed it.** Movement called the volley/standoff collision dominant; ranged called the troop_type mismatch dominant. **The troop_type mismatch is the true row-flipper** (single param → 0%; the volley collision alone leaves R1 near 50%). Both are real; the volley collision is a legitimate engine bug worth fixing on its own merits (and is ~3× larger in magnitude than its producer stated).
- **Reach finding severity.** Producer rated it "dominant-cause"; the critic demoted it — it affects **zero currently-failing rows**, and C2/C6 turn out to be the **same scenario constructed twice**. I side with the critic: it is a **future-ratification landmine**, not a current-divergence cause. (The C2==C6 duplication is itself a minor harness-quality wrinkle worth noting.)
- **Producer evidence errors the critics caught (don't trust the raw numbers):** the stances surface's R1 aggressive-stance figures ("18/30 → 9/30, worse") **do not reproduce** — a faithful run gives ~9-10/30 both ways (flat); only the qualitative "aggressive doesn't fix R1" conclusion survives. The movement surface's volley-damage magnitude skipped a ×3 scale factor (bug is *larger*, not smaller). The movement surface's envelop "commitment never fires" was **refuted** (it does fire; the stall is one phase later).
- **Unquantified by everyone:** the cavalry-row momentum/`charge_pen` effect on C1-C7 percentages, and whether C3's mirror asymmetry is movement- or cascade-driven.

---

**Key files** (all under `/home/user/ttrpg/`): `tests/sim/gauge_mb.py` (harness; R1/R3 at lines 229-232, `make_unit` at 82-114); `tests/sim/mass_battle/hierarchy/units.py` (`_node_advance` step floor at :826-838, `_kite_goal` at :753-786, no accumulator vs legacy :1109-1111); `tests/sim/mass_battle/core/exchange.py:110` (melee pool) vs `tests/sim/mass_battle/orchestration.py:1154-1166` (volley pool); `tests/sim/mass_battle/troop_types/registry.py` (`TROOP_TYPE_STATS` has no speed; `TROOP_TYPE_REACH={}`); `tests/sim/mass_battle/config.py` (`VOLLEY_MIN_RANGE=2`, `PC_CAVALRY_SPEED_MULT=2.0`, `STANCE_SPEED_MOD`, `ROLE_SPEC`). Probe: `/tmp/claude-0/-home-user-ttrpg/0c549f45-4808-5ede-8107-cdc37fd81a1f/scratchpad/probe_kite_floor.py`.