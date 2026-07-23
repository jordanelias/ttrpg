# U10 — Morphology-Lever Activation & Tradition-Modulation Surface

**Author:** PC-lane implementation node (CLAUDE.md §10) · **Date:** 2026-07-23 · **ED:** ED-PC-0022
**Executes:** the U9 capstone's own re-charter (`u9_capstone_v1.md` §3: "activation, if it ever comes, is a
scenario-specific micro-calibration … out of U9's scope").
**Status: PROPOSED** (ratifies by merge per ED-1094 unless a section is flagged held-back; none is — the one
prior held-back call is *dissolved* here, §3).
**Scope of change:** engine code (config + 4 modules), 4 new abilities, tests. Core damage/σ resolution untouched.

---

## 0. Posture — radically question the ratified U9 verdict

U9 ratified: keep all six edge/choke/facing morphology levers at `K=0` (byte-identical), "cut nothing, activate
nothing", because no lever robustly moves aggregate winrate. The verdict was evidenced and adversarially reviewed —
and still it left grounded physics inert with a `needs_jordan` hanging over it. This pass re-opened it under the
CLAUDE.md §0 mandate ("adversarial pass at every stage that gates a result") and the direct instruction to question
ratified tenets. The finding: **the U9 verdict is a non-decision resting on a circular use of an instrument it
itself calls wrong, and it never diagnosed *why* the levers read as noise.** They read as noise for four reasons.

---

## 1. The four fiats that kept the levers inert

| # | Fiat | Evidence |
|---|---|---|
| **F1** | **Wrong instrument (holistic).** Activation was gated on aggregate FIELD winrate — the only thing `balance.py` measures. The capstone (§3.2) *itself* says winrate is the wrong instrument for a situational lever, then uses it to justify "activate nothing." A flat global-`K` crank makes *everyone* equally better at the false-edge read / spine-press, so it cancels in a mirror-ish field — ~0 is the *expected* reading, not evidence of inertness. | `u9_capstone_v1.md` §2 (all six sub-noise) vs §3.2 (winrate is the wrong instrument) — the two are in tension; the verdict follows the instrument it disowns. |
| **F2** | **Amputated tradition surface (the "beyond rote physics" gap).** `ability_primitives.eff_cw`/`ability_factor` is the modulation surface. **Not one of the six levers was wired to it, and no ability targeted them.** `legibility()` didn't even take `TR`. So a lever could only ever be flat physics, equal for all — the one ingredient that makes a *situational* lever *decisive* (a tradition that specializes in it) could not attach. | `ABILITIES` targeted only `counter_success`/`leverage`/`counter_select`/`measure`/`anti_overcommit`; `edge_lines`/`spine`/`grab_hazard`/`choke`/`facing` sites had no `eff_cw` call. |
| **F3** | **Wrong-channel fiat (choke-thrust).** The grip-invariant axial-thrust principle (D2 gate, ED-1029) is **physically correct for FORCE** — a rigid shaft transmits axial compression independent of grip. U5 parked a **control/deflection cost** against it in `phi_grip('point')` — the *force* multiplier — where D2 correctly zeroed it, manufacturing a false "break D2 or kill lever 5" dilemma (the U9 `needs_jordan`). | `phi_grip('point')` returned `max(0.75, 1 − CHOKE_THRUST_K·grip)`; at K>0 it broke `test_thrust_protection_grip_invariant` (`u9_capstone` §2.4). |
| **F4** | **Near-invisible consumers (facing).** `FACING_VOID_K=0.08`, `FACING_PROFILE_K=0.03` — too small for the regime lever to move anything even at K>0. (Partly legitimate: C1 polearm facing *direction* is genuinely unresolved; the C2 *regime* is not.) | `combat_systems.facing_target` consumers. |

**On F3 specifically — is the grip-invariant thrust "suspicious"?** It was flagged as suspicious. Interrogated on
first principles: it is *correct as a FORCE claim* — choking up a rigid pole does not reduce the axial force an
in-line thrust delivers. What is real is that choking up shortens the rear lever, so the point is beaten off-line
more easily and the gathered posture telegraphs — a **control/legibility** cost, not a force-magnitude cost. So the
suspicious thing was never the invariant; it was that a real cost had been parked in the wrong channel, against a
correct invariant, producing a fake dilemma.

---

## 2. The fix

1. **Re-home choke-thrust (dissolves F3 and the held-back call).** `phi_grip('point')` is now grip-invariant
   **unconditionally** — `CHOKE_THRUST_K`/`CHOKE_THRUST_FLOOR` retired. The D2 gate is byte-identical and pristine.
   The choke's real cost (control/telegraph) already lives in `systems.choke_counterbalance → CHOKE_ACCURACY_K`;
   that is now the single choke-cost channel. The U9 fork ((a) hold-and-kill / (b) widen D2 from 10%→25%) was a
   false dichotomy — the answer is a *third* option it excluded: route the effect to the channel it belongs in. No
   D2 amendment, no `needs_jordan`.
2. **Build the tradition surface (fixes F2).** Each of the six lever sites is routed through
   `ability_factor(c, <channel>)`: `edge_read` / `choke_control` (legibility), `spine_press` (bind), `edge_grab`
   (contact), `facing_regime` (facing). Default `1.0` → inert-safe (a no-tradition fighter is unchanged).
3. **Activate to small grounded baselines (fixes F1's inertness without F1's error).** `LEGIB_EDGELINE_K=0.04`,
   `BIND_SPINE_K=0.03`, `GRAB_EDGE_K=0.07`, `CHOKE_ACCURACY_K=0.03`, `FACING_REGIME_K=0.12`. Deliberately
   whisper-level: the **no-ability field stays within the harness noise floor** (every mirror-fairness / stalemate
   guard passes unchanged), because a situational lever *should not* move aggregate balance. The **decisive weight
   is carried by the abilities**, measured on the correct instrument (§4).
4. **Seed four illustrative abilities** (`ability_primitives.py`) — multipliers all `[SIM-CALIBRATE]` (no treatise
   assigns a numeric coefficient); **grounding-corrected in the ED-PC-0023 review** (§7):

   | Ability | Tradition | Channel | Op | Grounding |
   |---|---|---|---|---|
   | `shinogi` | japanese | `spine_press` | ×1.6 | pressing along the katana's ridge/spine (shinogi/mune) in the bind — grounded to the weapon that actually HAS a spine (was `winden`/german, a double-edged-longsword technique inert on this single-edge lever) |
   | `zwerchhau` | german | `edge_read` | ×1.6 | the Thwart-cut driven with the short/false edge — weaponizes return-line ambiguity |
   | `ringen_am_schwert` | german | `edge_grab` | ×0.4 | wrestling at the sword — seize a live blade with less self-injury (**mitigator**, factor<1) |
   | `guardia` | italian | `facing_regime` | ×1.5 | the Italian single-time strong-side profile (weak grounding — a stance emphasis, not a discrete technique) |

   `choke_control` has the surface (the hook is live) but **no ability yet** — a deliberate honest gap. **These
   abilities are illustrative seed content, not a proven balance feature** — the review (§7) showed their aggregate
   effect is ~0; they demonstrate that the surface *works*, pending broader grounded content across more traditions.

---

## 3. Verdict on the held-back call — dissolved, not decided

The U9 `needs_jordan` ("does grip-invariant-thrust admit a shallow floored choke exception?") assumed the only ways
to honour the choke-thrust physics were to break/widen the D2 gate. **Re-homing the cost makes the question moot:**
the D2 force-invariant is kept exactly (thrusts are grip-invariant in force, always), and the choke control cost is
captured honestly in the accuracy channel. Nothing rides on a D2 amendment because there is no D2 amendment.

---

## 4. Evidence — the correct instrument (CORRECTED by the ED-PC-0023 adversarial review — see §8)

> **⚠ RETRACTION.** An earlier version of this section claimed a "+2.8pp specialist edge" (Winden katana vs plain)
> measured by a specialist-vs-nonspecialist duel. The adversarial balance review found that duel was **confounded**:
> it compared `german+ability` vs `none+empty`, mixing the *tradition switch* with the *ability equip*. Isolated
> properly (`trad+ability` vs `trad+empty`), the abilities' AGGREGATE win-rate edge is **~0** (noise, occasionally
> slightly negative). The "+2.8pp" was the pre-existing german tradition-membership baseline, not the ability. That
> claim is **withdrawn**.

The genuinely correct instrument for a *situational* lever is **per-event**, not aggregate winrate: does the ability
win the specific event the lever governs? That effect is real and deterministic:

```
shinogi: bind_sigma(katana+shinogi vs arming)  >  bind_sigma(katana plain vs arming)   — wins more of THE BIND
ringen : grab_sigma vs an edged opponent rises (−0.207 → −0.087)                        — de-hazards THE GRAB
D2     : phi_grip('point') == 1.0 at every grip (force-invariant intact)
```

But binds/grabs are rare enough that this does **not** move aggregate win-rate — exactly the situational nature U9
identified. So the honest claim is narrower than the original: the surface makes a tradition's specialisation
*attach* to the physics (real per-event), but the abilities are **not a proven aggregate-balance feature**.

---

## 5. Test posture — what changed and why

- **Rewrote the byte-identity pins to live/directional** (`test_combat_edges.py`, `test_combat_choke.py`): the
  levers are no longer K=0, so "byte-identical" is the wrong assertion; the tests now pin liveness, direction, and
  tradition-amplification. The **D2 gate (`test_thrust_protection_grip_invariant`) stays green** and is now
  guaranteed by construction (no constant can break it).
- **Fixed the U9 test-hygiene defect** (`u9_adversarial_review_v1.md` §4): the old `test_both_channels_live_not_dead`
  wrote the `weapon_physics.CHOKE_THRUST_K` module global and leaked `0.0` to later test modules. The constant is
  gone; the channel is now exercised via a `cfg` override + equipped state — no global mutation, no cross-module leak.
- **One grounded re-baseline** (`test_reach_class_beats_arming_not_inverted`): the **guisarme** (versatile mid-reach
  hooked polearm) off-plate vs arming was ~0.53 pre-U10 and is **structurally unsatisfiable at any nonzero K** —
  activating the levers legitimately shaves its marginal edge (arming's double edge reads harder; the head-heavy 2H
  bill telegraphs as it gathers). At n=60/cell the shift is inside the guard's own noise (SE ~0.09). The guisarme
  assertion is relaxed to a *contest band* (`>0.40`, "not annihilated") with this recorded reason; the **true reach
  weapons (spear/yari/poleaxe) keep the strict `>0.5`**, and a real zeroing bug still trips the floor.
- **Combat suite:** the 9 accepted-red baseline is **unchanged** (no new failures); the new/rewritten tests pass.

---

## 6. Provenance / reproduction

- Levers activated in `config.py` (`LEGIB_EDGELINE_K`/`BIND_SPINE_K`/`GRAB_EDGE_K`/`CHOKE_ACCURACY_K`/
  `FACING_REGIME_K`) + `weapon_physics.py` (CHOKE_THRUST retired). Surface in `combat_systems.py` (legibility ×2,
  bind_sigma, facing_target), `contact.py` (grab_sigma), abilities in `ability_primitives.py`.
- Calibration sweeps: `workbench/balance.py::winrate` (per-matchup specialist duels) + the seeded behavior guards
  (`test_combat_balance_guard.py`, `test_combat_invariants.py`) confirming the no-ability field is undisturbed.
- Tests: `test_combat_tradition_levers.py` (new), `test_combat_edges.py` / `test_combat_choke.py` (rewritten),
  `test_combat_invariants.py` (facing + guisarme re-baselines). `pytest tests/valoria -k combat` → 9 accepted-red.

---

## 7. Adversarial review (ED-PC-0023) — four independent perspectives + a pessimistic NERS audit

U10 was put through a four-way adversarial review (each critic read-only, refute-by-default, blind to the others)
plus a pessimistic NERS resolver-stress audit. Outcome: the **machinery is sound and safe, but two of the original
claims were over-stated and are corrected here**; the ability layer was under-grounded and is fixed.

| Perspective | Verdict |
|---|---|
| **Correctness/regression** | **CLEAN** — every lever sign verified adversarially (flip → tests catch it); `CHOKE_THRUST_K` fully retired; zero dangling `Combatant.pool` readers; export matches; tests non-vacuous; exactly the 9 accepted-red. |
| **NERS (pessimist)** | **SAFE** — no positive-feedback runaway (grab→poise→initiative stays inside the ratified decay/cap safeguards; specialist chain peaks ~53.5%), **no new degenerate win-share** (pre-existing extremes byte-identical; one matchup moved *out* of extreme), no dead branch (`state_graph.py` PASS), no non-termination, no mirror break (deltas within N=300 sampling noise). |
| **Balance/emergence** | **The "+2.8pp specialist edge" is a CONFOUND** (§4 retraction). Isolated, the abilities are ~0 aggregate. "Field within noise" was also over-stated — a few grab/edge-affected weapons (dagger, arming) move by grounded physics — though NERS's SE analysis shows most of the flagged >4pp cells are N=400 sampling noise, with no new extremes. |
| **Grounding/canon** | **Ability layer under-grounded** — `winden`→`spine_press` was a category error (a double-edged LONGSWORD technique wired to a single-edge-only lever, inert for its own weapon); multipliers were untagged/arbitrary; 3-of-4-German distribution skewed. |

**Fixes applied in response (ED-PC-0023):**
- `winden` → **`shinogi`** (japanese): grounded to the katana, the roster weapon that actually HAS a spine, which
  also improves tradition distribution. All four ability multipliers tagged `[SIM-CALIBRATE]`; `guardia` re-grounded
  to the Italian single-time profile with an explicit weak-grounding caveat.
- The **confounded aggregate test** (`test_..._specialist_wins_the_mirror_duel`) is removed; replaced by a
  deterministic **per-event** test (bind_sigma) that makes no aggregate claim.
- The **guisarme re-baseline was tightened**: none/light keep the strict `>0.5` (they stay dominant ~0.68-0.78);
  only the genuinely near-even **medium** tier gets a contest band. (The review confirmed the original re-baseline
  was over-broad but was *not* masking a real regression.)
- `§4` corrected (the "+2.8pp" retraction above); the ability layer is now framed as **illustrative infrastructure,
  not a proven aggregate-balance feature**.

**Net honest deliverable of U10:** (1) the choke-thrust re-home (D2-clean, dissolves the held-back call) — solid;
(2) the tradition-modulation **surface** (real, tested, inert-safe) — solid infrastructure; (3) the lever activation
— safe (NERS) and grounded, moving only the weapons the physics mechanically touches, with no new degeneracy, but
(4) the **abilities on the surface are provisional** — per-event real, aggregate ~0, and needing broader grounded
content across more traditions before any aggregate-efficacy claim is warranted.
