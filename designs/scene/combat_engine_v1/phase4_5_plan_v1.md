# Scene-Combat Phase 3/4/5 Plan (recovered, with execution status)

**Provenance:** this document is a verbatim recovery of a Claude Code plan file that was never committed
to the repo — `perform-an-intensive-plan-jolly-llama.md` (authored 2026-06-29), itself built on top of
the v4 master plan `create-a-plan-for-fancy-yao.md` (authored 2026-06-28, "Scene Combat — Implementation
Plan (v4)", which defined the 7 requirements → WS-0..WS-8, the three co-equal access gates, and §C's
three binding gates — WS-0..WS-8 are substantially delivered in-repo; see `tradition_decomposition_v1.md`,
`engagement_psychology_recovered.md`, `REARCHITECTURE_v1.md`). Both source files live only under
`C:\Users\Jordan\.claude\plans\` on the authoring machine, not in git. Recovered into the repo 2026-07-01
because `designs/audit/2026-06-30-combat-grounding/forward_roadmap.md`'s "Track 4" summary — the only
place in the repo describing this remaining work — had compressed this plan to four bullets and, in doing
so, silently dropped the entire Phase 4a game-theoretic layer, the Workstream-0 grounding-ledger
deliverables, and the three named principles below. **Status annotations (bracketed, bold) have been
added at each section; the underlying plan text is otherwise unchanged from the source file.**

**Execution summary (2026-07-01):** Phase 3 → Gate 1 is **DONE and merged** (PR #40 `d4bf2af3`, PR #47
`8fbc4b66`). Phase 4 (all of 4a/4b/4c) and Phase 5 are **NOT STARTED** — confirmed by grep: zero hits for
Bayesian/Stackelberg/threat-memory/concentration-lapse/`clinch_sigma`/`disengage`/`choke` anywhere in
`designs/scene/combat_engine_v1/`. The Workstream-0 ledger deliverables (`sim_verification_ledger.json`,
`grounding_ledger.md`) were never materialized as files — the grounding *discipline* was applied ad hoc
during the percussion/armour/use-mode re-baseline (4 adversarial grounding workflows, see the
`combat-grounding-methodology` memory) but the literal ledger artifacts this workstream specifies do not
exist. Treat that as a still-open deliverable gap, not resolved by the ad hoc version.

---

## Context

`design/scene-combat-v1` is mid-flight in a **6-layer re-architecture** (`designs/scene/combat_engine_v1/REARCHITECTURE_v1.md`). L0 (weapon-physics derivation), L1 (core resolver), L2/L3 (de-leaked pure subsystems + thin wrapper) are **done**. The remaining work is:

- **Phase 3** — wire the derived L0 physics into the live consumers (the engine still reads hand tables: `GATE`, `spd`, `wt`, categorical `reach`, hand-set `percussion`) + **re-baseline**, including the armour-matrix defects. **[DONE + MERGED — PR #40/#47]**
- **Phase 5** — the **contact axis** (clinch / disengage / choke), the one genuinely-missing subsystem; consumes the dead `clinch` field; delivers the dagger grapple→gap-thrust finisher and the Italian cavazione. **[NOT STARTED]**
- **Phase 4** — **abilities-as-access** (7 phase-slots + point-buy affinity budget + learning-gate + access catalogue) + the **contextual-differentiation residual** (the C1 "only 2 distinct leaders / 5 contexts" gap), closed bottom-up via ability × weapon × state — **not** tradition weights. **[NOT STARTED]**

This pass also adds two cross-cutting mandates from the designer:

1. **Ground every computed quantity bottom-up** in physics / biomechanics / human anatomy / academic martial-arts scholarship — a **full per-quantity literature review** before each formula is fixed. No asserted `[SIM-CALIBRATE]` constant survives without a grounded derivation recorded in a verification ledger. This is *how* reach / choking / leverage / percussion / lunge / tempo / recovery should be **computed**, not tuned by feel.
2. **Treat the reading / feint / first-move / initiative layer game-theoretically**, mirroring the social-contest deliberative game — *formalize the implicit games*, skip cross-bout persistence, but add two **within-fight** dynamics: being struck biases the defender's read toward guarding that line (adaptive wariness), and a lapsed concentration raises the chance of choosing the wrong defence (bounded rationality under load).

**Why now:** the armour×weapon matrix (new instrument, already built) — a sweep across primitive-space — exposed three confirmed, adversarially-verified gaps in the primitive→behaviour derivation, surfacing at the {heavy, 2H, gripped-blade}, the {low-authority blunt}, and the {long-point} configurations (the longsword-, staff-, and spear-configs as sample points). They are symptoms of the un-wired physics and the missing contact axis — so the re-baseline, the grounding, and the game-theory layer are one coherent body of work, gated and audited phase by phase.

**Outcome:** a fully-wired, primitive-derived, academically-grounded, game-theoretically-coherent personal-combat engine where every weapon lands where its physics + the armour-mitigation matrix put it (balance ≠ symmetry), validated at each gate and merged phase by phase.

---

## Recall — the evidentiary base and the work this completes

This is **not a fresh design** — it completes the recovered/salvaged corpus under the re-architecture. The build draws on and finishes:

- **Recovered combat corpus** (`designs/audit/2026-06-29-combat-corpus-recovery/`, ~60 docs): `weapon_physics_RECOVERED_composite_2026-06-22.py` + `percussion_authority.py` (the L0 physics being wired); `weapon-typologies-differential-reference.md` + `martial_morphology*` + `historical-combat-manuals/` (historical/biomech evidence); **`attribute_mechanic_map.md` + `valoria_combat_derivations_tempo_recovery_reach_2026-06-01.md` + `valoria_character_sheet_personal_combat` (the CHARACTER-primitive derivations)**; `combat_engine_master_reference.md`; the `ners_audit_*` / `ners_stress_test_*` series (the adversarial-audit precedent + methodology).
- **Abilities design** (`designs/audit/2026-06-13-combat-bottomup/`, ~18 docs): `combat_traditions_classes_ability_library`, `combat_ability_system_consolidated_master`, the slot-system / gating-chain / phase-indexed-slots docs, `tradition_gate.py`, `combat_tradition_representation_alternatives` (the Phase-4 source of truth).
- **Armour/grappling ratified design** (`designs/audit/2026-05-29-combat-armature/`): the mitigation matrix, the three plate-counters, `grappling_system_design.md` (the Phase-5 contact-axis source).
- **Re-architecture blueprint** (`REARCHITECTURE_v1.md`, Phases 1–5) + HANDOFF "Next actions" (the residual it called "channel-leverage" — reframed here as bottom-up contextual differentiation, since there are no tradition weights; abilities-as-access; tunable magnitudes; ratify→merge) — this plan executes **Phases 3–5 + the residual**.
- **The master scene-combat plan (v4)** — `create-a-plan-for-fancy-yao.md` ("Scene Combat — Implementation Plan (v4)"), which defined the **7 requirements → WS-0..WS-8** (state-graph WS-1 · continuous morphology + affordance gates WS-2 · tradition decomposition WS-3 · representation re-architecture WS-4 · The Approach + feint-as-attack WS-5 · workbench WS-6 · multi-combatant WS-7 · balancing methodology WS-8). WS-0..WS-8 are substantially **delivered** on this branch; **this plan completes their unfinished tails:** WS-2's L0-consumer WIRING (Phase 3), WS-4's **abilities-as-access** (Phase 4b) + the **§C contextual-differentiation residual** (Phase 4c), and WS-5's **contact-pole** clinch/disengage/choke (Phase 5). From it this plan inherits: the **three co-equal access gates** (affordance ∧ mode-compat ∧ LEARNED), the **7 named phase-slots**, "**The Approach**" imposition contest, and the **§C three binding gates**.
- **Prior diagnosis (this session):** the weapon×armour matrix instrument + the adversarial red-team synthesis (`...jolly-llama-agent-a821f74e8bda4d92b.md` audit trail) — folded into Phase 3.

**The four primitive layers (point 2 — everything works from primitives):**
- **(C) Characters** — the 9 stats (`strength, agi, end, cog, att, spirit, focus, history, disp`, each 1–7) → derived figures (`reading, reflex, conc_max, stamina_max, balance_eff, wound-tracker/health/WI, pool`). Built in `combatant.py` + `r8_parity_harness`.
- **(W) Weapons** — morphological primitives (`mass, head_len, grip_len, pommel_kg, wclass, hilt, hands, head, guards, clinch` + geometry) → physics (`weapon_physics.py`).
- **(T) Traditions** — a tradition is **only a curriculum** (the bundle of learned ability-accesses it teaches) + **selection biases/tendencies** (preferred-node + familiarity). It carries **NO mechanical weight of its own** — there are no "channel weights." An action's efficacy comes from the **weapon's primitives × the applicable learned ability × the state**, never a top-down tradition multiplier. (`traditions.py` = curriculum/bias; `ability_primitives.py` = the accesses + their effectiveness-functions.)
- **(S) Systems** — the σ-spine and subsystems assembled from C/W/T (`systems.py`, `core.py`), orchestrated by the wrapper.

Workstream 0 grounds **all four**, not just weapons.

**Deferred (flagged, not in this scope):** WS-7 multi-combatant (designed, ED-911; engine is 1v1) — surface for a later pass unless you want it folded in. **[Still deferred; design doc exists at `designs/scene/scene_combat_v1/scene_combat_design_v1.md`, status DESIGN-ONLY, gated on ED-911 ratification.]**

---

## The 7 review lenses (applied at EVERY step and in each gate audit)

Every change — and the adversarial audit at each gate — is checked against all seven:

1. **Code architecture & the wrapper contract** — the 6-layer dependency direction holds (L0→L1→L2→L3→L4→L5, one-way); each function in its correct module (physics in `weapon_physics`, resolution in `core`, subsystems in `systems`, orchestration in `wrapper`, abilities in the L5 layer); no hand tables left. **The wrapper contract is inviolable:** every subsystem is a *pure function of role-objects* (`aggressor`/`defender`), computes a contribution, and **never mutates**; the **wrapper alone** sequences calls, owns ALL state mutation, and assembles nothing of its own (no σ-formula in the wrapper). All new state (e.g. the within-fight threat-memory) is **hosted on the `Combatant`** (like `initiative`/`poise`) and mutated only by the wrapper; its computation is a pure `systems.*` function. No subsystem ever indexes raw `A`/`B`.
2. **Data compliance** — every mechanical constant carries a `sim_verification_ledger.json` citation (anti-fabrication gate, `tools/ci_sim_fabrication_check.py`); ED entries filed in `canon/editorial_ledger.jsonl` for each design decision (`tools/validate_ed_citations.py`); register sizes + naming (Solmund) clean.
3. **Historical validation** — every behaviour matches the recovered corpus: `weapon-typologies-differential-reference.md`, the ratified armour table (`armour_validation_result.md`: blunt 3.0 / point 5.5-to-gaps / cut 6.2-deflected; plate's three counters), and the per-tradition decomposition.
4. **Physics / biomechanics / anatomy / math grounding** — every quantity derives from a documented physical/biomechanical model with a literature citation (Workstream 0), recorded in the ledger; the math is checked (units, monotonicity, limits). The grounding is **adversarially earned** — merit-tested, falsifiable, circularity-guarded; an honest `[ASSERTED — no source]` is preferred over a forced citation (see Workstream 0 discipline).
5. **Game-theoretic fidelity** — read/feint/commit/initiative behave as the games they model; the within-fight dynamics produce *bounded* effects; mirror stays ≈50.
6. **Bottom-up emergence & granularity** — behaviour rises from primitives through one derivation; never a per-weapon behaviour table, never a name-keyed special case, **never a per-weapon target.**
7. **No pattern-matching / top-down imposition / misplaced code** — no `if weapon=='longsword'` hacks, no scalar top-down dials, no formula in the wrong layer.

> **THE PRIMITIVE PRINCIPLE (overrides everything below).** A weapon — "dagger", "longsword", "spear" — is nothing but a **dictionary label for an aggregate of primitives** (`mass, head_len, grip_len, pommel_kg, wclass, hilt, hands, head, hand_guard, blade_guard, clinch, reach_adj` + geometry). Every fix, grounded formula, calibration coefficient, and target in this plan is expressed over **primitives and the derivations from them** — never over a weapon name. Weapon names appear in this document **only as emergent sampling points** to validate that the primitive-space behaviour is correct; they are never the thing we tune, target, or branch on. **If a change touches a weapon by name, sets a per-weapon win-rate target, or requires asking "what should weapon X do," it is wrong by construction** — the correct object is always the primitive configuration (e.g. *the {heavy, 2H, gripped-blade} region*, *a head that cannot defeat the tier's armour*, *low percussion-authority blunt*) and the formula that maps it to behaviour. Balance is validated across primitive-space; it is never set per weapon.

> **THE ATTACK–DEFENCE CONVERGENCE PRINCIPLE.** Attack and defence are **not a polarized axis.** They begin from a single point — the fighter's **stance + weapon relative to the opponent** (the measure/range/tempo/contact that "The Approach" sets) — and they **converge at their limits:** a successful *defence* is an attack that forces the opponent to retreat; a successful *attack* is a defensive manoeuvre that throws the opponent down. The **bound of success — the limit every action reaches toward — is the action that is simultaneously attack AND defence: it delivers threat WITHOUT receiving threat** (the single-time counter, the opposition-thrust that closes the line, the bind/wind that becomes the strike, the displace-and-step-inside). So the engine must **not** model offense and defence as opposite poles to trade off; every action emerges from the stance-point with a **threat-given** and a **threat-received (exposure)** component, and the highest-skill, dominant-strategy play **drives exposure toward zero while threat stays maximal** — convergence. This is the attractor the game-theory layer (4a) optimizes toward and the engine must reward; **seizing the initiative IS achieving threat-without-counter-threat.** The existing convergence mechanics (single-time counter, opposition, bind→strike, riposte, displace-inside) are the load-bearing expression of this, not edge cases — and the commitment=recovery axis is its physical face (deep commit buys threat-given at the cost of threat-received; the master's art is threat without that cost).

> **THE TRADITION-IS-NOT-A-WEIGHT PRINCIPLE.** A tradition imposes **nothing mechanical top-down — there are NO channel weights.** How a character acts is determined by their **STATE × their WEAPON × the applicable ABILITIES they have learned.** A tradition is only (a) the **curriculum** — which ability-accesses the fighter learned — and (b) a **selection bias / tendency** — which actions they are inclined to *attempt*. **Efficacy flows from weapon primitives + ability mastery + state — never from the tradition itself.** A master of Italian rapier is not "weighted toward measure"; they are **biased toward Italian actions** and succeed because the rapier + the learned accesses are effective in that state. Any per-tradition multiplier on the substrate is wrong by construction; the differentiation *between* traditions must **emerge** from their differing curricula interacting with weapons and states — exactly as weapon behaviour emerges from primitives (the two principles are the same shape, one layer up).

---

## Workstream 0 — The grounding spine: ground ALL FOUR primitive layers (per-quantity adversarial literature review)  → `sim_verification_ledger.json`

**[STATUS: PARTIALLY HONORED IN SPIRIT — the ledger files below were never materialized. The percussion/
armour/use-mode re-baseline (ED-1080, `designs/audit/2026-06-30-combat-grounding/`) applied an equivalent
adversarial-grounding discipline ad hoc via 4 independent grounding workflows (see the
`combat-grounding-methodology` memory), but no `sim_verification_ledger.json` or `grounding_ledger.md`
file exists in the repo. This is a still-open deliverable, not resolved by the ad hoc version. The tables
below reflect the ORIGINAL plan's scope — some rows are now grounded by that later work (e.g. percussion
authority, armour RESIST), others remain as specified in 2026-06-29.]**

**Do this first and in parallel; it is the substrate every later formula wires to.** For each computed quantity *in characters, weapons, traditions, and systems*, run a fanned-out, fact-checked, **adversarial** literature review (deep-research / academic MCP) → a derivation grounded in primitives + a ledger entry. Replaces every asserted `[SIM-CALIBRATE]` constant with a grounded form + a literature target — or an honest `[ASSERTED — no source]` / `[FIAT — designer-set]` (see the discipline below). Nothing is exempt because it "looks settled."

### W0-C — Character primitives (the 9 stats → derived figures)
The combatant is built from 9 attribute primitives; every derived figure (and its constant) is grounded or flagged. Sources: sports science / motor-control / physiology / cognitive-load literature + the salvaged `attribute_mechanic_map.md` / `valoria_combat_derivations_*` / character-sheet docs.

| Derived figure | Engine site | Grounding to pull (academic) | From primitives |
|---|---|---|---|
| **reading** `(cog+att)/2` | `systems.reading` | perception/anticipation; expert pattern-recognition in sport | cog, att |
| **reflex** `(2agi+att)/3` | `systems.reflex` | simple/choice reaction-time; attention→RT | agi, att |
| **conc_max** `3F+2S` | `combatant.derive_stats` | sustained-attention / cognitive-load capacity | focus, spirit |
| **stamina_max / fatigue** | `r8.stamina_max`, `Combatant.fatigue` | anaerobic capacity; fatigue→performance decrement | end, spirit |
| **balance_eff** (agi-governed) | `systems.balance_eff` | postural control / dynamic balance under load | agi (+skill, poise) |
| **wound-tracker / health / WI / max_wounds** | `r8.WoundTracker` | trauma physiology; haemorrhage/incapacitation thresholds (Montgomery & Tipton 2025) | end, spirit, strength |
| **handling / str_demand** | `systems.str_demand/handling_penalty` | grip/wield strength vs tool load; isometric capacity | strength vs weapon load |
| **str → damage impact** | `core.damage` | strike force vs body mass / strength | strength |

### W0-W — Weapon primitives (morphology → physics)

**[STATUS: substantially grounded by the later percussion/armour/use-mode re-baseline — percussion,
reach, and tempo rows below are now live via `weapon_physics.percussion_authority`/`agility`/`reach`,
though `WP.reach()`/`WP.authority()` themselves are `[BUILD-ONLY/DIAGNOSTIC]`, not wired — see the Track-2
residual in `HANDOFF.md`.]**

| Quantity | Engine site | Grounding to pull (academic) | Derived from primitives |
|---|---|---|---|
| **reach** | `systems.reach_base`, `weapon_physics.reach` | arm/stature anthropometry (reach≈0.65–0.75 m); museum blade-length distributions; Fiore/Silver measure-grammar | `head_len + 2H-extension + reach_adj` (length-units → m via `UNIT_M`) |
| **choke / close-unwieldiness** | `systems.can_choke`, `close_unwieldiness` | effective reach of a gripped-blade vs full form; moment-arm at grappling distance (~0.3 m) | `grip_len` threshold; `reach − CLOSE_REACH_REF` |
| **leverage / bind** | `systems.leverage`, `bind_sigma` | two-hand vs one-hand torque (force×lever-arm); blade Stark/Schwach stiffness; bind-force studies (Acta Periodica Duellatorum) | `grip/(grip+head)` ratio; 2H bonus; `blade_guard` |
| **percussion / impact-through-armour** | `weapon_physics.percussion_authority`, `core.coupling/_transmit`, `RESIST` | KE=½Iω²; blunt-force transmission through plate (FEA / ballistic-gel / Giuffra 2013 osteo) | `√mass · pob_frac` saturating; **scale plate transmit by p_auth** (FIX-1b) |
| **thrust vs cut** | `geometry.py`, `core.coupling` DELIVERY/RESIST | point pressure vs edge mechanics; Petri 2019 (point geometry ↔ expected armour); Montgomery & Tipton 2025 (haemorrhage delay) | `geometry` bake → gap/thrust/cut/perc_conc |
| **lunge** | `systems.lunge_quality` | lunge extension/recovery kinematics; rapier vs longsword recovery time vs MoI | non-linear lightness × hand-balance × 1H |
| **tempo / agility** | `systems.weapon_tempo`, `weapon_physics.agility` | angular acceleration α=τ/I → hand-speed vs tool inertia (bat-speed analogues, Acta rotational-dynamics) | `1/(1+K·MoI)`; replace legacy `spd` |
| **recovery / commit / overcommit** | `systems.recoverability_factor`, config `EXPOSE_*` | angular-momentum arrest time (Δω=τt/I); forward-moment "wants to continue"; neuromuscular deceleration | `mass^exp · pob_frac` non-linear; lunge/choke modifiers |
| **composite-mass + K_\* gains** | `weapon_physics.py` constants | wood/iron densities (sourced); museum PoB ranges; MoI calibration | the iron-on-wood model; K_\* fit to the literature targets, not asserted |

### W0-T — Tradition = curriculum + bias (NO channel weights; efficacy is ability × weapon × state)
**There are no per-tradition channel weights** — a top-down tradition multiplier is rejected. A tradition is **only** (a) a **curriculum** — which learned ability-accesses it teaches — and (b) **selection biases/tendencies** — which actions the fighter is inclined to *attempt* (the preferred-node imposition + familiarity). An action's **efficacy comes entirely from the WEAPON's primitives × the APPLICABLE learned ABILITY × the STATE**, never from the tradition. A master of Italian rapier is not "channel-weighted"; they are strongly **biased** toward Italian actions (disengage, mezzo-tempo, single-time counter), and those actions succeed because the **rapier's primitives + the learned ability** make them effective in that state. Ground each tradition's **curriculum + biases** against the martial-tradition research + primary treatises (Liechtenauer / Fiore / Fabris / Capoferro / Silver / Thibault) — what each school *teaches* and *prefers*, not a weight vector. The grounded mechanics live in the **per-ability effectiveness-functions** (ability × weapon × state → action efficacy; Phase 4b), not in a tradition layer.

**[STATUS: NOT STARTED — `tradition.py`'s live model is still the +/* channel-weight modulator this
principle rejects; `eff_cw` remains dormant per `forward_roadmap.md`.]**

### W0-S — System constants (the σ-spine + outcome mapping)
The constants that assemble C/W/T into behaviour (`ATTACKER_BIAS, COMMIT_SIGMA, INIT_*, READ_K, NEUTRALIZE_*, RECOVERY_TEMPO_K`, the degree bands, the within-fight-dynamics gains) are grounded where a real basis exists — the **d10 dice-model EV math + game theory** for the read/initiative spine (Phase 4a), the ratified resolver math (Lane-C r1/r8/m1, ED-900/904, **not re-litigated** — the grounded substrate) — and otherwise honestly flagged `[SIM-CALIBRATE]` / `[FIAT]`. The spine's attack/defence σ-terms are the two **components of one stance-rooted action** (Convergence Principle), not opposed poles; the convergence mechanics (single-time counter, opposition, bind→strike, riposte, displace-inside) are where they coincide and are load-bearing.

**Output:** `designs/scene/combat_engine_v1/sim_verification_ledger.json` (NEW, co-located) — one entry per constant: `{sim_variable, value, source (paper/treatise), section, quoted_basis, derived_formula, merit_verdict, falsifier}`. This single ledger satisfies **lens 2 (data compliance)** and **lens 4 (grounding)** simultaneously. Each quantity also gets a short grounding note appended to a new `designs/scene/combat_engine_v1/grounding_ledger.md`.

**[STATUS: NEITHER FILE EXISTS. This is the concrete, checkable gap — if picking up Workstream 0, start
here: either produce both ledger files from the grounding work already done (percussion/armour/use-mode),
or explicitly re-scope Workstream 0 as satisfied-in-spirit and strike this deliverable.]**

### Adversarial lit-review discipline (the lit review is itself audited — no forced or superficial grounding)
The literature review is **adversarial by construction**. For each quantity the workflow runs a *find* pass and then an independent *refute* pass; a grounding survives only if the refuter cannot break it. The discipline:

1. **Merit test before mapping.** First ask: does the academic concept *mechanistically govern this engine quantity*, or is it a surface analogy? Map only when the mechanism transfers (e.g., MoI→angular-acceleration→hand-speed is a real chain; "entropy"→combat-chaos is not). Record a `merit_verdict` per entry: `governs | partial | analogy-only`.
2. **Honest non-grounding beats a forced citation.** Where the literature genuinely does not support a formula (e.g., no study links sword MoI to a hand-speed constant), say so and mark the constant `[ASSERTED — no source; first-principles only]` rather than attaching a tenuous paper. An honest gap is a finding, not a failure.
2b. **When the data is absent, decide by fiat and flag it — never force.** If the adversarial review concludes the support genuinely does not exist (no adequate source, no falsifiable first-principles derivation), do **not** manufacture a value or a citation. Surface it as a **designer fiat decision**: mark the constant `[FIAT — designer-set; data absent]`, state the plausible range and the rationale, and let Jordan set it by decision. A flagged fiat is the honest terminus of a gap; a forced ground is a defect.
3. **Circularity guard.** Never cite a source the engine was reverse-engineered from as *independent* validation (the grounding-test's own caveat). Distinguish "the model was built to match X" from "X independently predicts the model."
4. **Source-tier discipline.** Use the differential reference's T0–T3 tiers; never rest a *contested* formula on T3 (enthusiast/AI-encyclopedia) — those navigate to primaries only. Confidence is flagged and is genuinely lower outside the European HEMA corpus.
5. **Falsifiability.** Each grounded formula records a `falsifier`: the measurement that would contradict it (e.g., "if recovery time were independent of PoB in motion-capture, the forward-moment model is wrong"). A grounding that nothing could falsify earns nothing.
6. **No reverse-fitting disguised as grounding.** A constant chosen to hit a win-rate target is `[SIM-CALIBRATE]`, full stop — it must not be dressed in a citation. Grounding flows source→formula→value, never value→hunt-for-a-paper.

The **same discipline applies to the game-theory mapping (4a):** adopt a game-theoretic structure (Bayesian signaling, mixed strategy, Stackelberg timing) only where it is *mathematically faithful and improves the model*, not because the label fits. A forced "this is just matching pennies" with no equilibrium consequence is rejected.

---

## Phase 3 — Wire L0 into live consumers + armour re-baseline  → **Gate 1**

**[STATUS: DONE + MERGED — PR #40 (`d4bf2af3`) + PR #47 (`8fbc4b66`), 2026-07-01. The Gate-1 adversarial
audit ran (7 lenses, 67 agents, 54 confirmed/5 refuted — see
`designs/audit/2026-06-30-scene-combat-gate1-audit/gate1_audit_report.md`); its residuals are tracked as
Track-2 items in `HANDOFF.md` (`wt`/`spd` de-leak, `WP.reach()`/`authority()` single-source decision),
NOT re-opened here.]**

### 3a. Fix the two confirmed code defects (no balance intent, pure correctness)
- **`weapon_physics.puncture_pressure` key mismatch** (`weapon_physics.py:91`): reads `strike_concentration`, but `geometry.bake()` renames it `perc_conc` → returns 0 for all weapons. Fix the key.
- **FIX-1b — blunt coupling scales with percussion authority** (`core.coupling` blunt branch, `core.py:80-88`): today `1.6 × (1−0.30)=1.12` for *every* blunt head, so a **wooden staff transmits through plate like a steel mace** (verified: staff fells plate in ~4.0 hits vs mace 3.1). Thread `p_auth` into the blunt transmit and scale by `(p_auth/8)` — **identical to the logic `systems.armor_defeat_sigma:175` already trusts** (`percussion/8`); the damage path simply missed it. Mace/poleaxe (p_auth 8) unchanged by construction; staff falls. Thread the arg via `core.damage:89` (already has `perc=`) and `core.strike:112` (already passes `p_auth`).

### 3b. Wire the derived physics into the live consumers (the re-baseline), then delete the hand tables
Each wiring swaps a hand table for the **grounded** derivation from Workstream 0. Behaviour-changing → re-calibrate per the methodology (`combat_balancing_methodology.md` §4 joint-fit) against the matrix + the grounding targets.

| Live hand read | → derived replacement | site |
|---|---|---|
| `GATE[weapon][mode]` (12×3 parry/dodge/wind) | `weapon_physics.defense_affinities(w)[mode]` | `systems.mode_sigma:144` |
| `w['spd']` | `weapon_physics.agility(w)` / `tempo_penalty(w)` | `systems.weapon_tempo:29` |
| `reach=='long'` + `HEAD_REACH` | `weapon_physics.reach(w)` | `systems.reach_base:13-14` |
| hand `percussion` | `weapon_physics.percussion_authority(w)` | `systems.armor_defeat_sigma:175` (damage path already via `p_auth`) |
| `wt` class / `core.HEFT` | `weapon_physics.authority(w)` / MoI heft | `core.heft_resp` |

Then **delete** `systems.GATE`, `config HEAD_REACH`, and the vestigial `weapons.py` fields (`reach`, `wt`, `spd`, `percussion`, `pob_frac`, `hand`) — weapons become pure primitives. Re-fit the `K_*` gains (`K_REACH/K_HEFT/K_TEMPO/K_STRD/MOI_AGILITY_K`) to the Workstream-0 literature targets, not to numeric convenience.

**[STATUS: `GATE` retired (`1dae44e8`); `reach`/tempo wired to geometry (`d069be7c`); `pob_frac`/`percussion`
fields removed (PR #47). `wt` and `spd` are NOT yet deleted — this is exactly the open Track-2 residual:
`core.py:55` still reads `w.get('wt')=='heavy'`, `systems.py:46` still reads `w['spd']`, live in parallel
with the derived `wield_heft` machinery. Balance-affecting roster-wide; needs Jordan's measured
before/after, not an autonomous flip.]**

### 3c. Corrections to the primitive→behaviour derivation (never per-weapon, A0-safe by construction)
Three adversarially-verified gaps in the FORMULAS that map primitives to behaviour (3/3 red-team). Each fix is on a derivation over primitives; the weapon names are **emergent sample points, not targets or branches**:

- **FIX-1 — the reach advantage decays with a head's inability to defeat the defender's armour-tier.** New pure helper `systems.reach_threat(longer, defender, cfg) → factor∈[floor,1]`, derived **entirely from primitives** via `armor_defeat_sigma` (a function of head / percussion-authority / gap) + `ADEF_W[armor]` + `ADEF_THRESHOLD`: a head that **cannot threaten the closer's armour-tier** loses its structural-reach edge. Multiply into `close_rate` (`wrapper.py:85`), `stophit_p` (`:91`), `reopen_prob` (`systems.py:276`). **A0-safe by construction:** `ADEF_W['none']=0` → factor ≡ 1.0 unarmoured. *Emergent (validation samples):* the long-low-armour-defeat region (spear-/staff-config) stops dominating the armoured approach; the high-authority-blunt and gap-thrust regions (mace-/poleaxe-/dagger-config) clear the threshold and are unaffected. The gain `REACH_DECAY_K` is calibrated so primitive-space behaviour matches the physical expectation, not to hit any config's number. **[STATUS: landed, `REACH_DECAY_K=0.35` in `config.py`, flagged `[FIAT — designer-set; deliberately LOW to avoid triple-counting]`. Superseded/subsumed in part by the later situational gap-game (`f7f7596f`) and the spear-fix finding (2026-06-30: approach-side dominance, not closed-reach — see `HANDOFF.md`).]**
- **FIX-2 — the gripped-blade FORM-STATE sheds the swing-heft cost.** The heft-cost terms (`WEIGHT_PEN`+`HANDS_COMMIT` tempo, `D_WT`/`D_2H` str-demand) model a *swung* mass; a gripped-blade (half-sword) form-state is a controlled, leveraged close technique, not a swing, so it must not pay swing-heft. Gate `HALFSWORD_HEFT_RELIEF` on the **gripped form-state primitive** (a `gripped` morphology flag on the gripped-blade record), mirroring the existing `grip=='choke'` relief — keyed on the **morphological form-state, never `wt`, never a weapon name**. *Emergent:* the {heavy, 2H, gripped} configuration holds vs plate instead of collapsing; non-gripped heavy-swing configs keep full heft; the form-state only exists when closed vs medium/heavy armour, so unarmoured behaviour is structurally untouched. Never touches damage. **Known limitation:** partial relief may be swallowed by the tempo cap/floor — budget one calibration iteration (relieve the tempo path fully and/or grant the gripped-point a small standing armor_defeat credit, both primitive-derived). **[STATUS: superseded by the Stage-2 continuous grip-position model (`baaa6d77`, `d3661936`) — `recoverability_factor` and `wield_heft` now derive continuously from `grip_position`/`at_grip` MoI rather than a discrete `HALFSWORD_HEFT_RELIEF` fraction. Probably moot as a standalone coefficient; flag for Jordan to confirm it's fully subsumed rather than silently dropped.]**
- **No third knob.** The {short, dual, cut} region's plate dominance is not its own defect — it is an artifact of the cut-and-thrust derivation collapsing at plate (`ADEF_CUT=-0.9`), so any non-pure-cutter wins by default. It self-corrects when the cut-vs-armour derivation is recalibrated in the joint fit. A region-specific dial here would violate the primitive principle.

### 3d. Joint-calibration order + invariants
Order (each re-measures the full `weapon_armour_matrix` *as a sweep across primitive-space*): **FIX-1b → FIX-1 → confirm the {short,dual,cut} region self-corrects → FIX-2 (iterate)**. Hold at every step:
- **Mirror ≈ 50** at every armour tier (any primitive config vs an identical one).
- **A0 column untouched** by the armour-keyed fixes (0-effect at `none` by construction — verify).
- **Emergent validation (sampled at named configs, never targeted):** the {high-authority-blunt} region rises decisively vs plate; the {pure-cut} region collapses vs plate; the {long-point} region falls once-passed but retains some gap-thrust; the {gripped-blade} region holds. Balance is the **shape of these arcs matching physics + history**, not any per-config win-rate.
- Final confirmation at **N≥1000/cell**.

**Gate-1 adversarial audit** (7 lenses) → file ED entries → ratify → merge. **[STATUS: DONE — see
`designs/audit/2026-06-30-scene-combat-gate1-audit/gate1_audit_report.md`; ratified and merged as PR #40.]**

---

## Phase 5 — Contact axis (clinch / disengage / choke)  → **Gate 2**

**[STATUS: NOT STARTED. Confirmed via grep: no `clinch_sigma`, `disengage`, or `choke` function exists
anywhere in `designs/scene/combat_engine_v1/`. The dead `clinch` field on weapon records (rapier 2 …
dagger 10) remains unconsumed.]**

Build the one genuinely-missing subsystem, grounded in `grappling_system_design.md` + Fiore *abrazare* / German *Ringen* / the rondel-to-gaps record, and the Workstream-0 grip/leverage/clinch biomechanics. Consumes the **dead `clinch` field** (rapier 2 … dagger 10).

- **New pure subsystem** (in `systems.py`, or a co-located `contact.py` if it grows): `clinch_sigma` / `disengage` / `choke` as weapon-gated functions, role-objects-in, contribution-out — same contract as the existing subsystems. Strength-dominant grapple σ (vs the leverage-dominant bind), gated by `clinch` + hands (2H grapples poorly) + `can_choke`.
- **Attach points** (already mapped): the **bind-entry injection point** (`exchange.bind_entry`, `wrapper.py:178-180`) for the Italian **cavazione/disengage** (the bind-refusal pole, today only a coarse `impose_node` flip); the **approach loop** (`close_rate`/`reopen_prob`) for clinch holding the close; `adopt_stance` gating choke on `clinch`.
- **Delivers the canonical plate-counter #3** (grapple → half-sword → rondel into the gaps) — which **resolves the dagger A3 design call**: the dagger's high vs-plate number stops being an un-modelled artifact and becomes the real grapple-finisher.
- **Capability gates** registered in `capabilities.py` (clinch/disengage as affordances; effectiveness continuous).
- **Ablation gate (lens 6, churn):** the contact axis must move outcomes beyond the noise floor or it is cut, per `combat_balancing_methodology.md §6`.

**Gate-2 adversarial audit** (7 lenses) → ED entries → ratify → merge.

---

## Phase 4 — Game-theoretic psychological layer + abilities-as-access + contextual differentiation  → **Gate 3**

**[STATUS: NOT STARTED, ALL THREE SUB-PHASES. This is the section that `forward_roadmap.md`'s "Track 4"
compressed to a single bullet ("abilities-as-ACCESS... Emergent") — that bullet covers only 4b below. 4a
(the entire game-theoretic layer) and 4c (the §C fix) had no corresponding mention at all in the
compressed roadmap prior to this recovery.]**

### 4a. Formalize the reading/feint/initiative games + the two within-fight dynamics

**[STATUS: NOT STARTED — zero code hits for Bayesian/Stackelberg/threat-memory/concentration-lapse.]**

Mirror the social-contest deliberative game (`designs/scene/social_contest_v30.md`, `sim/personal/contest.py`) onto the combat psychological layer, with the `valoria-dice-model` EV math as the payoff substrate. **Legible, bounded, no cross-bout scars.**

- **Read = Bayesian signaling** (`systems.read_contest`): the attacker's commit-depth/head is a hidden type; `legibility` is the noisy signal; the defender's `reading` is the inference. Formalize the posterior explicitly; keep it explainable.
- **Feint ↔ commit = mixed strategy** (`systems.commit_depth` + `legibility`): the disposition-skewed Beta is the attacker's mixed strategy; a strong read collapses it toward ~50% vs equal skill. Verify EV-consistency with `valoria_dice`.
- **Initiative = iterated Stackelberg / timing game** (`systems.initiative_sigma`, Indes steal): formalize first-move advantage + role-flip on sen-no-sen; keep tanh-bounded.
- **Convergence is the optimization target (the Attack–Defence Convergence Principle made operational).** Score every action on (threat-given, threat-received) from the stance-point; the **dominant strategy / equilibrium attractor is the convergent action** — threat without counter-threat (single-time / opposition / bind→strike / displace-inside). Seizing initiative = achieving convergence. This is **not** a new hand-coded reward: the existing mechanics already permit it; the audit check is that **emergent high-skill play trends toward convergent actions** and that exposure-free threat is the win condition the game-theory layer surfaces. The commitment=recovery axis is its physical substrate (threat-given vs exposure trade-off).
- **NEW within-fight dynamic A — struck → adaptive defensive bias.** When a defender is hit on a line (mode/head), their subsequent read/`mode_sigma` biases toward guarding that line — "increasingly wary of how they were struck." Implement as a **decaying per-defender threat-memory** over the attacker's recent *successful* lines that updates the read prior (Bayesian within-bout). Grounded in threat-conditioning / motor learning. Resets each engagement (no cross-bout persistence).
- **NEW within-fight dynamic B — concentration lapse → wrong option.** As the Focus+Spirit concentration tracker depletes, the defender's mode-selection grows noisier and biased toward **error** (picking the wrong defence even on a nominal read-win). Strengthen the existing `mental_fat` path into an explicit bounded-rationality term: low `conc` → rising P(suboptimal mode). Grounded in cognitive-load / decision-under-stress literature.
- Both dynamics are **bounded** and must pass the ablation gate (move outcomes, generate churn, not dominate).
- **Architecture (the wrapper contract):** the threat-memory is **live state hosted on the `Combatant`** (alongside `initiative`/`poise`/`conc`), reset per engagement, **mutated only by the wrapper**; the bias and the concentration-lapse error are **pure `systems.*` functions** of role-objects feeding `read_contest` / `mode_sigma`. No new state or σ-math in the wrapper itself.

### 4b. Abilities-as-access

**[STATUS: NOT STARTED — `ability_primitives.py` currently implements the 7 channel levers as a live
+/* modulator (`eff_cw`), not the access-gated schema below. Some scaffolding exists (a phase-slot +
prereq notion appears in the module's docstring) but the `trigger`/`cost`/`prereq` schema extension and
the ~55-entry access catalogue have not been built.]**

From the source docs (`designs/audit/2026-06-13-combat-bottomup/combat_traditions_classes_ability_library*`, `combat_ability_system_consolidated_master*`; `ability_armature.md`; `tradition_decomposition_v1.md`):
- **Schema extension** on `ability_primitives.ABILITIES`: add `trigger` (state-graph node/phase conditionality), `cost` (slot + per-use resource), `prereq` (affinity threshold). An ability = **learned ACCESS to attempt a graph transition**, never a `+X` dial; **efficacy emerges from the WEAPON's primitives × the character's MASTERY of the applicable ability × the STATE — not from the tradition** (the tradition is only the curriculum that granted the access + the selection bias). This is the operational form of "it is the ability and the weapon that allow a greater degree of success, not the tradition itself."
- **The 7 NAMED phase-slots** (v4 plan §D: **Approach · Reading · Feint[dissolved into Commit] · Commit · Defence · Bind · Counter**) + **point-buy affinity budget** — the **character's own** proficiency profile (how well *they* execute the accesses they've learned; a buildable per-fighter aptitude, like a skill), reusing the existing equal-total shape — **not** a tradition weight. Cross-check the slot taxonomy against the source docs (`combat_ability_slots_granular_phase_indexed`) and reconcile any naming drift.
- **The three CO-EQUAL access gates** (v4 plan §D): an access fires only when **affordance ∧ mode-compatibility ∧ LEARNED** all hold — a longsword *affords* winding, but you cannot Wind, do Spanish *compás*, or a naginata flourish without having **trained** it. The learning-gate (`can_equip(tradition, ability)` via the expanded `TRADITION_KIT`) is **co-equal** with the affordance gate (`capabilities.py`) and the mode-compatibility gate, not subordinate. A tradition is the **curriculum** that grants accesses + acts as decision-gates / biases / tendencies, never a flat multiplier.
- **Access catalogue** (~55 entries) → `access_catalogue.py` (NEW) or expanded `ABILITIES`.
- **Invariant:** empty kit == today, **byte-identical** (same seed → same outcomes). This is the load-bearing safety check.

### 4c. The contextual-differentiation residual (close the C1 gap — bottom-up, NO tradition weights)

**[STATUS: NOT STARTED — this is the same gap `forward_roadmap.md` calls the "§C channel-leverage
residual" (spanish broad-strong / chinese broad-weak, 2 leaders / 5 contexts). The fix described here is
more specific than the roadmap's one-line summary: it explicitly rejects tuning tradition weights (there
are none) and requires 4b's per-ability effectiveness-functions to exist first.]**

The C1 gap (only 2 distinct leaders / 5 contexts) is **not** closed by tuning tradition weights — there are none. It closes **bottom-up, from ability × weapon × state**: each tradition's **learned-ability set + the weapon's primitives + the state** must make that tradition's curriculum decisive in the context its abilities+weapon suit. An Italian-rapier build leads the rapier context because the **rapier's primitives + the Italian-taught accesses** (disengage / mezzo-tempo) are effective there; a German build leads the longsword context because the **longsword's primitives + the Winden access** dominate the bind. The work is **calibrating the per-ABILITY effectiveness-functions** (ability × weapon × state → action efficacy) and getting each tradition's **curriculum** right — the `eff_cw` gateway re-understood strictly as *the aggregate of the fighter's applicable learned abilities* (1.0 with none equipped; **the tradition contributes nothing through it**). The contextual differentiation must **emerge** from ability×weapon×state, never be imposed by a tradition multiplier. Bring `tradition_context_matrix` toward one-leader-per-context while the unconditional field stays flat (±2-3pp); clear **§C's three binding gates** (v4 plan §C, currently PARTIAL): (1) **beat the keep-bias baseline** on legibility AND vacuum-balance; (2) **imposition decoupled from any magnitude** (no double-count); (3) **every lever clears the ablation bar** or is cut (the `seize` precedent). Re-measure with `balance.py context`.

**Gate-3 adversarial audit** (7 lenses) → ED entries → ratify → merge.

---

## Final adversarial audit (capstone)

**[STATUS: NOT YET APPLICABLE — this capstone runs after Phase 4/5 land, per the sequencing below. The
Gate-1 audit (Phase 3's own gate) already happened and is a partial precedent; this capstone is broader
(whole-engine, all four primitive layers).]**

A comprehensive multi-agent audit across all 7 lenses, adversarially verifying the *whole* engine, not just the diffs:
- **Ablation re-verification** — every claimed effect (each fix, each new lever, each ability effectiveness-function, both within-fight dynamics) ablated; anything that doesn't move outcomes beyond the noise floor is cut (lens 6, the `seize` precedent).
- **Grounding-citation audit** — every constant traces to a real source in `sim_verification_ledger.json` *or* is honestly marked `[ASSERTED — no source]`; skeptics try to refute each derivation (wrong domain, cherry-picked study, formula doesn't follow from the cited physics, circular self-citation, value-fit-then-cited). A superficial or forced mapping is struck.
- **Architecture audit** — dependency direction, no hand tables, no misplaced code, no per-weapon special cases or per-weapon targets, the **wrapper contract** intact (pure subsystems, wrapper owns all mutation, no σ in the wrapper) across **all four primitive layers** characters/weapons/traditions/systems (lenses 1/6/7).
- **Historical audit** — the final weapon×armour matrix + tradition tables match the differential reference + ratified table (lens 3).
- **Game-theory audit** — mirror≈50 everywhere; empty-kit byte-identical; the within-fight dynamics bounded; the read/feint/initiative invariants hold; **convergent actions (threat-without-counter-threat) are the emergent high-skill attractor** — the Attack–Defence Convergence Principle is realized, not defeated by a polarity artifact (offense and defence are not a tradeoff axis in the resolved behaviour).
- **Completeness critic** — what's unverified, un-grounded, or un-cited, across all four primitive layers (characters/weapons/traditions/systems)? Did any salvaged-corpus design intent get dropped? Is any constant still a bare `[SIM-CALIBRATE]` that should be grounded or flagged `[FIAT]`?

Adversarial = independent skeptics prompted to *refute*; a finding survives only if the majority cannot break it.

---

## Verification (end-to-end)

- **Matrix:** `python workbench/balance.py armour 1000` → the arc shapes across primitive-space match the physical/historical expectation; mirror≈50; A0 untouched by the armour-keyed fixes; the {high-authority-blunt} region rises vs plate, {pure-cut} collapses, {gripped-blade} holds. **[Phase 3: verified at merge.]**
- **Tradition tables:** `python workbench/balance.py all` + `balance.py context` → unconditional spread ≤3pp; one leader per context. **[Phase 4c: not yet applicable — still 2 leaders/5 contexts per HANDOFF.]**
- **Unit tests:** `tests/valoria/test_combat_*.py` green (extend with: blunt-authority transmission, reach-threat decay A0-safety, half-sword form-scoping, contact-axis gates, empty-kit byte-identical, the two within-fight dynamics bounded). **[92 tests currently green; the Phase 4/5-specific extensions listed here do not yet exist.]**
- **Grounding ledger:** `tools/ci_sim_fabrication_check.py` passes against the new `sim_verification_ledger.json` (every constant cited). **[Ledger file does not exist — see Workstream 0 status above.]**
- **Compliance:** ED entries filed per phase; naming/register gates green; `python tools/valoria_local.py --staged` clean before each commit.
- **Byte-identical invariant:** empty-kit abilities run reproduces pre-Phase-4 outcomes on a fixed seed.

---

## Critical files

- **Engine:** `designs/scene/combat_engine_v1/{core.py, systems.py, wrapper.py, weapons.py, weapon_physics.py, geometry.py, config.py, capabilities.py}`
- **L4/L5:** `designs/scene/combat_engine_v1/{tradition.py, traditions.py, ability_primitives.py}` (+ NEW `access_catalogue.py`)
- **Contact axis:** `systems.py` (or NEW co-located `contact.py`)
- **Harness:** `designs/scene/combat_engine_v1/workbench/balance.py` (`weapon_armour_matrix` already added)
- **NEW:** `designs/scene/combat_engine_v1/sim_verification_ledger.json`, `grounding_ledger.md`
- **Compliance:** `canon/editorial_ledger.jsonl` (ED entries), `tools/ci_sim_fabrication_check.py` / `validate_ed_citations.py` (gates)
- **Grounding/precedent sources:** `designs/audit/2026-06-29-combat-corpus-recovery/weapon-typologies-differential-reference.md`, `designs/audit/2026-05-29-combat-armature/{armour_validation_result.md, armour_system_design.md, grappling_system_design.md, damage_model_design.md}`, `designs/audit/2026-06-13-combat-bottomup/*`

## Under-determined COEFFICIENTS (calibrate from primitives; fiat only where data is genuinely absent)
These are **coefficients on primitive-derived terms**, never per-weapon targets. Each is calibrated so emergent primitive-space behaviour matches the grounded physical/historical expectation; where Workstream 0's adversarial review finds no adequate data, the coefficient becomes a flagged `[FIAT — designer-set; data absent]`, never a forced value. The emergent matrix is the validator — we never ask "what should weapon X do."
- **`REACH_DECAY_K`** — strength of the (armour-defeat-deficit → reach-decay) coupling. Grounded if the biomechanics of "a non-piercing head cannot hold off a closing armoured man" support a magnitude; else fiat. **[RESOLVED: `REACH_DECAY_K=0.35` in `config.py`, flagged `[FIAT — designer-set; deliberately LOW to avoid triple-counting REACH_W]`.]**
- **`HALFSWORD_HEFT_RELIEF`** — fraction of swing-heft the gripped form-state sheds. Grounded against any half-sword-vs-full-swing tempo/effort data; else fiat on the fraction. **[PROBABLY MOOT — superseded by the continuous `grip_position` model (Stage 2, `baaa6d77`/`d3661936`); confirm with Jordan whether this coefficient is fully subsumed or was silently dropped.]**
- **Blunt-transmission authority exponent** — how steeply plate-transmission scales with percussion authority (the FIX-1b form). Grounded against blunt-force-through-plate data; else fiat on the exponent. **[Landed as part of the percussion/armour/use-mode re-baseline — `A_HANDS=0.25`/`B_ARC=0.04` biomech energy-credit form, see `HANDOFF.md` 2026-06-30 entry.]**
- **The {short, point} close-finisher** — not a coefficient: the grapple→gap-thrust region (the currently-unmodelled plate-counter #3) becomes *real* behaviour once the Phase-5 contact axis exists, rather than an emergent artifact. Until then its vs-plate number is explicitly an under-credit, flagged, not hand-corrected. **[Still applies — Phase 5 not started.]**
- **`HEFT_MASS_K`** — within-class continuous-mass heft gain; hold at its current value through this re-baseline, re-fit only with a full re-sweep. **[RESOLVED: `HEFT_MASS_K=0.15` in `config.py`, with an explicit calibration note (greatsword 1.20 vs longsword 1.00 heft; raising toward 0.30 needs a full re-sweep).]**
