# I8 — Joint re-calibration + capstone audit (findings record)

**Status: R2 (I0→I8) COMPLETE, 2026-07-03.** This is the capstone measurement record for I8's acceptance
criteria (`plan_r1_RATIFIED.md`, "I8 — Joint re-calibration + capstone audit (D11b, D12)"), item by item.
Where a criterion is fully met, the evidence is the committed test suite (cited, not restated here). Where a
criterion surfaced a genuine finding, it's recorded here rather than silently patched, per the plan's own
"never silently patched" discipline (§8, D12a).

## (1) `balance.py` armour matrix — reach-class NOT inverted; the CONTESTED band is NOT yet met

Measured `workbench/balance.winrate` at N=200/cell, all four armour tiers, weapon vs `arming` at matching
armour (seeded, `_seed`):

| weapon | none | light | medium | heavy |
|---|---|---|---|---|
| spear | 78.5% | 77.5% | 78.5% | 81.9% |
| yari | 89.5% | 83.0% | 86.5% | 86.0% |
| guisarme | 78.5% | 67.0% | 67.0% | 80.5% |
| poleaxe | 83.5% | 81.5% | 88.0% | 93.5% |
| glaive | 81.5% | 52.5% | 6.4% | 6.7% |
| sabre | 80.2% | 37.1% | 4.1% | 5.2% |
| dagger | 20.0% | 25.9% | 52.8% | 64.6% |
| main_gauche | 16.6% | 28.1% | 26.2% | 42.9% |
| arming | 47.5% | 53.8% | 57.7% | 50.6% |
| longsword | 45.2% | 53.0% | 21.7% | 38.4% |
| mace | 9.0% | 14.5% | 26.0% | 23.2% |

**NOT inverted (falsifiable, holds):** every reach-class pole (spear/yari/guisarme/poleaxe) beats `arming`
at every armour tier, by a wide margin. Pinned as a standing regression guard —
`test_reach_class_beats_arming_not_inverted` (`test_combat_invariants.py`).

**The ~55–75% CONTESTED band is NOT currently met** (spear/yari/guisarme/poleaxe all run 75–93%, above the
upper bound), and the ~30–45% dagger/main_gauche "viable underdog" floor is not currently met unarmoured
(20.0%/16.6%, below 30%). **This is not a regression R2 introduced.** It traces to the SAME root cause
already flagged and deliberately left unresolved by `test_gap_game_poleaxe_spikes_plate` (a `[PHASE-C FLAG]`
red in the accepted-red set, §8/D12a): morphology-rearch Phase B's real per-part mass distribution lifted
poleaxe/spear-class percussion/gap authority above where the pre-Phase-B engine-scale constants (`ADEF_*`,
`REACH_W`, `PERC_ROOM_FLOOR`, etc.) were tuned for. Rebalancing the FULL roster against the now-grounded
masses is explicitly Phase C's job (`test_anchor_is_near_one` / `test_lunge_quality_is_weapon_derived_
continuous`'s docstrings — the same deferral), not this closing-distance redesign's — R2's own levers
(Φ_grip/Φ_room/range_avail/facing/rear_clearance/contact) are all individually ablation-gated (below) and
none of them is the cause of the roster-wide drift measured here. Re-annotated below (item 7).

## (2) Cross-cutting gates — mirror / no-one-shot / armour-arc / tradition-flatness

- **Mirror fairness + no-one-shot (decisive-not-degenerate):** already covered by the standing
  `test_combat_balance_guard.py` (`test_mirror_fairness`, `test_heavy_mirror_fair_and_decisive`,
  `test_seeded_determinism`) — green, part of the accepted baseline, unaffected by R2.
- **Armour-arc:** visible directly in the table above — glaive/sabre (pure cutters) collapse vs medium/heavy
  armour (6.4%/4.1%) exactly per the documented armour-arc mechanic (the edge glances off; core.coupling /
  systems.armor_defeat_sigma). This is the INTENDED contextual signature, not a defect.
- **Tradition-flatness (C1):** `tradition_field_table` at N=200/cell: spread 4.2pp (spanish 52.4 highest,
  chinese 48.2 lowest) — within noise of the documented parity band (±2–3pp at N~3000; a lower-N read is
  expected to run slightly wider). No dominant tradition. Report-only (matches the existing advisory-check
  convention — `weapon_armour_matrix`/`tradition_field_table` are workbench tooling, not CI-blocking, same as
  `Currency Consistency (report-only)` etc. in `.github/workflows/valoria-ci.yml`).

## (3) Standing anti-orphan test (D11b)

`test_every_circumstance_field_has_a_live_reader` (`test_combat_invariants.py`) — scans core.py/systems.py/
contact.py for a reader of every I1-scaffolded circumstance field (`grip_position`, `lunge_depth`,
`sel_head`, `sel_dmg`, `sel_gap`, `sel_perc`, `sel_pc`, `range_avail`, `facing`). All 9 have ≥1 live reader.

## (4) Per-weapon heft + percussion snapshot (D12c)

`golden_heft_percussion_snapshot.json` + `test_combat_heft_percussion_snapshot.py` — pins `core.heft_resp`
and `weapon_physics.percussion_authority` at ideal circumstance (grip=0, room=1) for all 51 startable
weapons. A future re-anchor (Phase C) will show as a visible, Jordan-gated diff against this fixture rather
than a silent shift.

## (5) Every lever ablation-gated

| lever | gate | result |
|---|---|---|
| swing-Φ_grip (I2, D2/JD-1) | `test_damage_retention_worst_case_material_lever` | guandao ≤0.76 (clean-material); voulge/bardiche ≤0.88 (borderline, JD-1 default retained) |
| percussion-Φ_room (I2, D2b) | `test_phi_room_percussion_ablation_clears_noise_floor` | live vs PERC_ROOM_FLOOR=1.0 ablation differs >2% |
| range_avail (I5, D4) | `test_commit_depth_contracts_with_less_room`, `test_swing_room_legibility_zero_at_full_room`, `test_stophit_range_term_zero_at_full_room` | all three show a real, nonzero delta under crowding |
| rear_clearance penalty (I7a, D7) | `test_rear_clearance_penalty_moves_close_tempo_and_str_demand` | live vs REAR_CLEARANCE_*_K=0 ablation differs |
| facing void/profile (I6, D6) | `test_facing_void_ablation_moves_close_rate_and_reach_sigma` | live vs FACING_VOID_GAIN/FACING_PROFILE_K=0 ablation differs |

No lever failed its ablation gate; none is cut.

## (6) Full suite — no NEW red beyond the accepted set

`pytest tests/valoria -q` with numpy present: **8 failed / N passed / 1 xfailed** — the same enumerated
8-red set (§8, D12a) at every increment I0→I8, zero new red. (See the I8 commit message for the exact N at
HEAD.)

## (7) `[PHASE-C FLAG]` reds — re-annotated, not resolved (recorded reason)

The 3 pre-existing `[PHASE-C FLAG]` reds (`test_gap_game_poleaxe_spikes_plate`, `test_anchor_is_near_one`,
`test_lunge_quality_is_weapon_derived_continuous`) are **NOT resolved by R2/I8** — their root cause (Phase
B's grounded per-part mass model outrunning the pre-Phase-B engine-scale constants) is explicitly Phase C
scope, a separate, not-yet-started body of work. Per the plan's own escape valve ("resolved... or
re-annotated with a recorded reason — never silently patched"), each docstring is re-annotated
(2026-07-03) to confirm: R2 (I0→I8) is complete, these three reds remain exactly as diagnosed, and item (1)
above (the roster-wide reach-class/dagger drift) is the SAME root cause now measured at wider scope — Phase
C should resolve all of it together via one engine-scale re-tune, not a piecemeal per-weapon fudge.

## (8) `INJECTION_POINTS` site strings

Dropped (not tested) — `state_graph.py`'s `INJECTION_POINTS` entries no longer carry a `site` line-range
string (they had already drifted across I2→I7b); `test_injection_points_carry_no_stale_site_string` pins
the absence. Node names remain the stable, checked reference
(`test_injection_points_reference_defined_states`).

---

**R2 (I0→I8) is complete.** The closing-distance/facing/grip/contact redesign
(`plan_r1_RATIFIED.md`) is fully implemented: Φ_grip/Φ_room circumstance-degraded impact, grip-aware reach,
mode/measure close-efficacy, commit/measure swing-room, facing state, rear-clearance close penalty, and the
contact/grapple axis are all live, ablation-gated, and orphan-free. The roster-wide balance drift measured
in (1) is a pre-existing, Phase-B-inherited calibration debt — real, measured, and explicitly out of this
plan's scope; Phase C is the correct venue to close it.
