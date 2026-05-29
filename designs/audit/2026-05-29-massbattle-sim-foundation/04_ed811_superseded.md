# ED-811 — Engagement Damage Formula: Resolution Package

**Date:** 2026-05-29
**Task type:** audit (Mode A — formula validation) · `valoria-mechanic-audit`
**Scope:** `mass_combat` Phase 5 Engagement damage
**Status:** analysis complete — **awaiting Jordan decision** (which damage model is canonical). Commit blocked (B6); staged inline for manual push.
**Intended repo path:** `designs/audit/2026-05-29-ed811-engagement-formula/ed811_engagement_formula_resolution.md`

---

## Verdict

ED-811 as filed is **under-scoped**. It assumes the multiplicative `×(1+Power)` model and only asks *net vs margin*. The real defect is a **two-model contradiction in canon** that no prior pass reconciled (the 2026-05-28 NERS verdict read the doc body "via index only" and params "truncated after 11k" — it never saw §A.7's additive formula). The two canonical models scale damage on **different stats** and are mutually exclusive:

- **Model A (weapon-additive)** — design doc §A.7 Phase 5 step 5: `damage = max(0, net_hits + weapon_modifier − DR)`, crit at net ≥ 3 *doubles the weapon modifier* (step 6). Uses **Dmg Mod**; no Power term. Also stated in params `PARAMS-GAP-05/PP-194`.
- **Model B (quality-multiplicative)** — params `PP-233` core formula + worked example: `damage = successes × (1 + Power)`. Uses **Power**; no Dmg Mod; DR folded into H, not subtracted at the damage step.

**Additive appears in two canonical places (incl. the design doc itself). Multiplicative appears in one (params).** SIM-MB-04's `INTERPRETATION-01` used a *third* model — `margin × (1+Power) − DR` — which exists in **no** canonical engagement procedure; it was synthesized from the params phrasing while ignoring §A.7. That synthesis is the source of FINDING-1 (one-turn kills).

The empirical result is the kicker: **the design doc's own §A.7 formula does not produce the doc's own stated "3–6 turn" battles.**

---

## Evidence (all force-read this session — SHA-fresh, verified vs HEAD)

| Source | Says | Model |
|---|---|---|
| `mass_battle_v30.md` §A.7 Phase 5 step 4–5 | `net = off_succ − def_succ`; `damage = max(0, net + weapon_modifier − DR)` | **A (additive)** |
| `mass_battle_v30.md` §A.7 Phase 5 step 6 | crit (net ≥ 3) → *weapon modifier doubled* | **A** (crit rule is incoherent under multiplicative) |
| `params/mass_combat.md` PARAMS-GAP-05 / PP-194 | `Size loss = max(0, net_hits + Dmg_Mod − DR)` | **A** |
| `params/mass_combat.md` PP-233 core + worked example | `damage = successes × (1 + Power)`; worked ex uses **gross** successes, both sides parallel, DR folded into H | **B (multiplicative)** |
| `params/mass_combat.md` PP-245 | TTRPG Dmg Mod = ⌈BG ÷ 2⌉ — *"BG unscaled collapses battles to one exchange; scaled produces multi-exchange"* | calibration lever for **A** |
| `tests/sim/sim_mass_battle_SIM-MB-04.md` INTERPRETATION-01 + FINDING-1 | implemented `margin × (1+Power) − DR`; got 29-dmg one-shots | **neither** (synthesized hybrid) |

Two further consequences of the split:
- **DR applies at different points.** Model A subtracts DR at the damage step. Model B (PP-233) folds DR into `H = min(Discipline,Command) + DR`, so DR raises each Size's Health cost instead. You cannot mix them without double-counting or zero-counting DR.
- **The stat that scales damage differs.** A keys on the **weapon** (Dmg Mod); B keys on **unit quality** (Power). This also bears on ED-822 (composition balance): Volley already uses Power-only (PP-503); if Engagement keys on Power-multiplicative too, ranged vs melee balance shifts materially. ED-811 and ED-822 are entangled.

---

## Empirical battle-length (Mode A — single-engagement MC, N=200k, TN7 p=0.4)

Constants cited: net = off−def (§A.7 s4); A crit doubles Dmg Mod (§A.7 s6); Dmg Mod TTRPG Cav+3/HI+2/Levy+1 (PP-245); melee DR Medium/HeavyCut=3 (§A.4). "rounds-to-kill" = def_HP / E[damage per engagement], single attacker, volley excluded — a lethality comparator, not full battle dynamics.

```
                              MU1 Cav→HI (HP16)      MU2 HI↔HI (HP20)      MU3 2D Levy (HP7)
model                 E[dmg]  rounds  1-shot%   E[dmg] rounds 1-shot%   E[dmg] rounds 1-shot%
A  additive (doc)      0.87    18.4    0.0       0.24   83.1   0.0       1.00    7.0    0.0
B  margin×(1+Power)    2.20     7.3    0.6       1.60   12.5   0.0       0.48   14.7    0.0
C  gross×(1+Power)     5.37     3.0    2.5       5.37    3.7   0.0       0.80    8.7    0.0
D  net×Power           1.48    10.8    0.0       1.06   18.8   0.0       0.24   29.4    0.0
```

Target per §A.1 design note: **3–6 turns** for matched forces.

**Reads:**
- **A (the doc's literal formula) is far too weak.** At canonical Dmg Mods, the weapon modifier ≈ DR, so additive damage ≈ net hits, which averages ~0 in a contested roll. 18–83 rounds. The doc's own target is unreachable with the doc's own formula + PP-245 mods.
- **B (sim) is moderate-mean, fat-tailed.** E[dmg] is low-ish (slow average), but the multiplier turns rare high-margin rolls into 29-dmg one-shots (0.6% per single engagement; higher with heavy-offence splits / multiple attackers — which is what SIM-MB-04 hit). The problem is *unbounded variance*, not mean lethality.
- **C (PP-233 worked example) is the only model in the 3–6 window** (3.0 / 3.7 rounds), with a modest one-shot tail. Note: my MC subtracted DR at the damage step for C, which PP-233 would *not* (DR is in H) — so C is actually slightly faster than shown (~2–2.5 rounds). DR-via-H is the real absorber.
- **D is too slow.**

---

## Candidate resolutions

Each is a real option; none is prescribed (project-owner decision). The choice is two coupled questions: **(Q1) does engagement damage scale on the weapon (Dmg Mod, additive) or unit quality (Power, multiplicative)?** and **(Q2) is Phase 5 a contested roll (net = off−def) or parallel (each side's own successes)?**

| # | Model | Hits 3–6 turns? | One-shot risk | Canon fidelity | Opens a sub-gap |
|---|---|---|---|---|---|
| **R1** | Adopt PP-233 **parallel-gross** `own_off_gross × (1+Power)`, DR via H | Yes (~2–4) | Low | Matches params worked example; **contradicts §A.7 net/crit** | **What does Defence allocation do?** Under parallel-gross, splitting to Defence only lowers your own offence — it must be given an absorbing role (reduce incoming hits, or add to H), currently undefined |
| **R2** | Keep §A.7 **contested-additive**, **recalibrate Dmg Mod upward** (toward BG/un-scale, or guarantee Dmg Mod > DR) | Tunable to 3–6 | None | **Highest** — preserves contest, crit rule, weapon-keying | Requires a Dmg-Mod recalibration pass + re-sim; PP-245's ÷2 was meant to *lengthen* battles and over-corrected |
| **R3** | Contested-**margin × (1+Power)** with a **cap** = defender current Size (sim FINDING-1 opt b) | Yes | Eliminated by cap | Keeps Power-keying + contest | Cap is inelegant (NERS-E / A5 apparatus risk); a hard cap is a threshold cliff |
| **R4** | Contested **net × Power** (drop the +1; sim FINDING-1 opt a) | No (too slow) | None | Partial | Doesn't reach target; would still need a mod bump |

**My read (not a decision):** the contest structure (net = off−def) is what breaks both extremes — it makes additive average ~0 and gives the multiplier a fat tail. Two clean paths:

- If you want **generalship/quality to scale damage** (consistent with the "generalship dominates" axiom and with Volley's Power-keying): **R1**, and define Defence's absorbing role. This hits the target with the least tuning and aligns Engagement with Volley.
- If you want **weapons to matter at the damage step** and to preserve §A.7's contest + crit rule exactly: **R2**, accepting a Dmg-Mod recalibration + re-sim.

R3 only if you specifically want to keep the sim's current model and just stop the one-shots. R4 is dominated.

Whichever is chosen, the **losing model's text must be struck** to end the contradiction: pick A or B, then reconcile §A.7 step 5–6 ⟷ params PP-233 ⟷ PARAMS-GAP-05 so all three state one model, and fix `sim_mass_battle_SIM-MB-04.py` (and the v22 lineage) to match.

---

## Staged editorial entry (NOT committed — B6; for manual push)

```yaml
# canon/editorial_ledger.jsonl  (append; assign ID on commit)
{"id":"ED-811","status":"open","type":"formula_contradiction","severity":"P1",
 "system":"mass_combat",
 "title":"Engagement damage: two canonical models (weapon-additive vs quality-multiplicative) unreconciled",
 "summary":"WIDENED from prior 'net vs margin' framing. mass_battle_v30 §A.7 Phase 5 step 5 specifies ADDITIVE damage = max(0, net_hits + weapon_modifier - DR) with crit doubling the weapon modifier (step 6). params PP-233 core specifies MULTIPLICATIVE damage = successes x (1+Power) (DR folded into H). PARAMS-GAP-05/PP-194 restates the additive model. The two models key on different stats (weapon Dmg Mod vs unit Power), apply DR at different points, and disagree on contest structure. SIM-MB-04 INTERPRETATION-01 used a synthesized margin x (1+Power) - DR present in neither, producing one-turn kills (FINDING-1).",
 "empirical":"MC N=200k TN7 p=0.4: doc additive = 18-83 rounds-to-kill (too slow; Dmg Mod ~= DR cancels); sim margin-mult = fat-tailed one-shots; PP-233 gross-mult = 3.0-3.7 rounds (only model in the doc's 3-6 turn target).",
 "resolution_required":["Jordan: choose damage-scaling stat (weapon Dmg Mod additive | unit Power multiplicative) and contest structure (contested net | parallel gross)","R1 adopt PP-233 gross-mult + define Defence's absorbing role | R2 keep §A.7 additive + recalibrate Dmg Mod + re-sim | R3 margin-mult + Size cap | R4 net x Power","Strike the losing model's text across §A.7 step5/6, params PP-233, PARAMS-GAP-05 so all state one model","Fix sim_mass_battle_SIM-MB-04.py + v22 lineage to match"],
 "interacts_with":["ED-822 (Volley/Engagement composition — engagement stat-keying changes ranged-vs-melee balance)","ED-872 (no Pool Floor — small-pool damage interacts with the chosen model)","PP-245 (Dmg Mod scaling is the R2 lever)"],
 "surfaced_by":"ed811_engagement_formula_resolution 2026-05-29 (full force-read of §A.7 + MC)",
 "Citations":["designs/provincial/mass_battle_v30.md §A.7","params/mass_combat.md PP-233/PARAMS-GAP-05/PP-245","tests/sim/sim_mass_battle_SIM-MB-04.md FINDING-1"]}
```

---

## Confidence & limits

- `[CONFIDENCE: high]` on the contradiction itself — three canonical expressions read in full this session, SHAs verified fresh vs HEAD.
- `[CONFIDENCE: high]` on the MC direction (additive-too-slow / gross-mult-hits-target / margin-mult-fat-tailed). Die rule sanity: E[succ/die @TN7]=0.4.
- `[CONFIDENCE: medium]` on absolute rounds-to-kill — single-attacker engagement proxy; **excludes** Volley pre-damage, multi-unit/combined engagements (ED-823), formation Def bonuses, and Discipline-penalty pool shrinkage over a real battle. A full multi-turn sim (re-gate to `simulation`, `h.sim_gate()`) would refine magnitudes but is unlikely to overturn the ordering.
- Did **not** re-run the full SIM-MB-04 battle engine; read its report + cited §A.7 directly.
- Freshness: all four `mass_combat` files confirmed fresh (declared SHA == HEAD). The bootstrap's 1 stale source is **not** a mass-battle file.

## Recommended next step

If you pick **R1 or R3**, the natural follow-on is a **full multi-turn re-sim** (proper `simulation` gate) of the chosen model across the SIM-MB-04 scenarios to confirm 3–6 turns *with* Volley + formations + combined attacks — which also lets ED-822 (composition) and ED-823 (combined-attack) be re-tested on the corrected base, since both were explicitly "blocked until base damage is fixed" (SIM-MB-04 FINDING-2/4). If **R2**, the follow-on is a Dmg-Mod recalibration pass first.
