# Combat Engine — Wiring Inventory, State-Graph Map & Cross-Module Compliance Audit

**Date:** 2026-07-23 · **Subject:** `systems/combat/combat_engine_v1/` (the canonical continuous PC resolver)
**Author:** PC-lane audit node + 3 fan-out reconnaissance agents (§0 method). READ-ONLY audit; **no engine
code changed.** Every claim traces to one of four independent, cross-validated evidence sources:

| # | Source | Method | What it establishes |
|---|---|---|---|
| E | **Runtime coverage trace** (`scratchpad/coverage_trace.py`) | `sys.setprofile` over a 22-weapon × 4-armour × 4-tradition + grappler fight matrix | *What actually executes* — 120/142 functions fire; 22 classified |
| G | **Engine's own state-graph self-test** (`state_graph.py`) | ships in-repo; edge-closure + dynamic-coverage | authoritative dead-branch flags |
| D | **State-graph + data-model agent** (sonnet) | read `state_graph.py`, `combatant.py`, `module_contracts.yaml` | nodes/edges, attribute→derived→per-beat chain, mechanic↔node bindings |
| C | **Cross-module compliance agent** (opus) | read all 8 resolution modules adversarially | single-owner / scripting-drift / grounding / emergence |
| B | **Design-promised-mechanics agent** (sonnet) | read `combat_v30`, `combat_design_v1`, `combat_c4_draft`, `phase4_5_plan`, `ability_armature`, `tradition_decomposition` | what *should* be wired + absent list |

**Headline:** the engine is **substantially wired and doctrine-compliant in its live math** (name-free
emergent resolution, clean additive σ-composition), with a well-defined frontier of **inert-but-wired
scaffolding** (K=0 levers, ability hooks) and **design-promised-but-unbuilt** mechanics (ranged combat
entirely, the abilities-as-access schema, Phase-4a game theory, the scene envelope). Six genuine dead/vestigial
functions and a handful of single-owner/grounding hazards are itemised in Part 4.

---

## PART 1 — WIRING INVENTORY (what executes, empirically)

**Coverage: 120 of 142 engine functions fire in the fight matrix; 22 never fire.** Every one of the 22 is
classified below by *why* — only **6 are genuine dead/vestigial code**; the rest are correctly bake-time,
diagnostic, inert-by-design, or rare-path.

### 1.1 The live resolution spine (fires every beat — the load-bearing core)

Top call-frequency (from E), in dependency order:

- **Weapon-physics substrate** (read every beat): `at_circumstance`/`at_grip`/`derive` (cached),
  `_gather_len`, `grip_travel_max`/`grip_choke_max`, `percussion_authority`, `reversed_grip_percussion`.
- **Resolution kernel** (`core.py`): `resolution_pool` → σ-assembly → `resolve` (μ-shift, roll-boost not
  Ob-shift) → `thrust_authority` → `_transmit` → `coupling` → `damage` → `strike`.
- **Mechanics layer** (`combat_systems.py`, the 69-fn mass): `reach_base`, `wield_heft`, `reading`,
  `poise_factor`/`clamp_poise`, `clamp_initiative`, `balance_eff`, `select_mode`←`afforded_heads`←
  `_mode_elements`←`element_afforded`, `close_efficacy`/`close_unwieldiness`, `_recovery_mode_commitment`,
  and the σ-functions `attack_sigma`/`defence_sigma`/`reach_sigma`/`initiative_sigma`/`armor_defeat_sigma`
  → `assemble_net_sigma`.
- **Abilities hook** (`ability_primitives.py`): `ability_factor`/`eff_cw` fire ~82k times — **live but
  inert-by-default** (return 1.0 with no authored ability; see 1.4).
- **Driver** (`wrapper.py`): `fight`/`engagement`/`_emit`/`_init_live` — the state-graph executor.

### 1.2 The 22 non-firing functions — full classification

| Function(s) | Class | Verdict |
|---|---|---|
| `geometry.{bake, cut_factor, thrust_factor, gap_precision, percussion_concentration, can_halfsword_thrust}` | **BAKE-TIME** | WIRED. Run at weapon construction (`weapons.py:815 _geo.bake(...)`); outputs baked into the record, read live via `w['gap']` etc. Profiler started post-import. |
| `weapon_physics.{hand_guard, blade_guard, _guard_catch_raw}` | **BAKE-TIME** | WIRED. Baked at `weapons.py:902-903`; **values consumed live** in `defence_sigma` (parry `combat_systems.py:237`, wind `:242`, bind `:753`). The guard/hilt-catch mechanic *is* active. |
| `weapon_physics._head_elements` | **BAKE-TIME (cached)** | WIRED. Called in `derive` (`:198`), but `derive` has a `_derived` cache (`:152-154`) so the loop runs once at bake; the 318k live `derive` calls are cache hits. |
| `weapon_physics.armour_defeat_mode` | **DIAGNOSTIC** | Not-fight-path *by design* — `weapon_physics.py:23` marks it "diagnostic-only"; the live armour-defeat path is the gap-game (`adef_cap`/`coupling`). |
| `capabilities.{capability_table, markdown_table}` | **REPORTING** | Table generators for docs/self-test, not resolution. Correct. |
| `capabilities.{allowed, _affords_point}` | **DESIGN-TIME VALIDATOR** | The capability GATE runs only in the self-test, *not* the live fight (which reads baked geo flags via `select_mode`). ⚠ a second, name-keyed source of truth — see Part 4 §2. |
| `combat_systems.disrupt_resist_p` | **WIRED, RARE PATH** | Wired at `wrapper.py:297` (the riposte+disrupt branch); the matrix simply rarely hit that branch. Live. |
| `combat_systems.{stamina_max, conc_max}` | **VESTIGIAL ACCESSOR** | "thin accessor (back-compat)" returning `c.stamina_max`/`c.conc_max`; the value's sole owner is the combatant. Benign dead code — removable. |
| `core.effective_ob` | **DEAD (documented)** | `resolve` deliberately bypasses it — the μ-shift docstring (`core.py:48-51`) explains Ob-shift distorted the degree bands. Vestigial display-only wrapper. |
| `combat_systems.can_choke` | **ORPHAN** | 0 callers. The choke is driven by `grip_target`. Dead predicate. |
| `ability_primitives.kit` | **ORPHAN** | 0 callers. The ability-KIT assembly is not wired (abilities are inert — 1.4). |
| `traditions.profile` | **ORPHAN / superseded** | 0 real callers (only comments); superseded by `traditions.preferred`/`familiarity`. |

### 1.3 Genuine dead/vestigial set (6, all removable or documentable)
`core.effective_ob`, `combat_systems.can_choke`, `combat_systems.stamina_max`, `combat_systems.conc_max`,
`ability_primitives.kit`, `traditions.profile` — plus a dead **field** `Combatant.ready` (D-agent finding:
declared `combatant.py:128`, reset `wrapper.py:24`, but the live tempo bookkeeping uses a wrapper-local
`ready` dict — the attribute is shadowed and never read). None affects behaviour; all are cleanup candidates.

### 1.4 Wired-but-inert (the deferral frontier — present, composed, numerically switched off)
- **The 6 K=0 morphology levers** (U3/U5/U7): `edge_lines`/`spine`/`grab_hazard`/`facing_pref`/
  `choke_counterbalance`/`phi_grip`-choke → their consumers, all `× K=0`. Fire every beat, contribute zero.
  (See the U9 capstone + adversarial review: grounded, situational, byte-identical, activation deferred.)
- **The abilities layer** (`eff_cw`/`ability_factor`): the *hook* is live (82k calls) but returns 1.0 —
  no ability *content* authored. Same pattern: wired substrate, absent payload.
- **The Contact axis** (`contact.grab_available/grab_sigma/grab_outcome`): BUILT and **reachable at runtime**
  (grab functions fire in the matrix), but the tradition-weighting of the grab menu (injection point
  `contact.axis`) is not yet wired (G-test + D-agent + B-agent all concur: "BUILT, not activated, M-11").

---

## PART 2 — THE STATE GRAPH (annotated with mechanics + primitives/attributes/derived scores)

Source of truth: `state_graph.py` STATES (data + tested). The engine's own self-test **PASSES** all 7 checks
(edge-closure, entry/terminal reachability, emit-legality, dynamic coverage) — with **2 dead-branch flags**.

### 2.1 Node → edge map (with emitted trace events)

```
FightInit ─▶ EngagementInit ─▶ {Approach, AwaitTempo}
  [emit fight_start]              [emit turn_start, engagement_start]

  ┌─────────────── inner engagement loop (per beat) ───────────────┐
  Approach   ─▶ {Approach, AwaitTempo, Felled, Separation}   [emit approach, stophit]
  AwaitTempo ─▶ {Exchange, AwaitTempo, Approach}             [tempo gate; no own emit]
  Exchange   ─▶ {Bind, Riposte, HitLanded, Contact, AwaitTempo, Felled, Separation}
                                                             [emit commit, read, mode, roll, outcome]
  Bind       ─▶ {HitLanded, Riposte, Contact, Felled}
  Riposte    ─▶ {AwaitTempo, Contact, Felled}
  HitLanded  ─▶ {AwaitTempo, Contact, Felled}
  Contact    ─▶ {AwaitTempo, Separation}                    [emit contact]   ← BUILT, tradition-weighting unwired
  └────────────────────────────────────────────────────────────────┘

  Felled     ─▶ Decided        [emit engagement_end]
  Separation ─▶ InterTurn      [emit separation, engagement_end]
  InterTurn  ─▶ {EngagementInit, Unresolved}                (recovery between turns)
  Decided    ─▶ UpsetCheck ─▶ FinalResult   [emit fight_result]  (TERMINAL)
  Unresolved ─▶ FinalResult
```

**Dead-branch flags (G-test, authoritative):** of the 4 `SEPARATION_REASONS`, only `burst_ceiling` and
`clean_defence` fire; **`beat_exhaustion` and `collapse` (stamina≤-4) NEVER fire** across the sweep — their
`return None` sites are likely unreachable (the 2026-06-09 map already flagged the stamina-collapse abort).
Action per the test's own guidance: give them a reachable trigger, demote to a documented guard, or delete.

### 2.2 Primitive → attribute → derived-score chain (the data model)

**RAW ATTRIBUTES** (`combatant.py:93-101`): `strength, agi, end, cog, att, spirit, focus, history` (physical/
mental stats) + `disp` (temperament 1-7, behavioural). ⚠ CLAUDE.md §5: the 9-attribute roster is **IN FLUX**
at the registry level; do not bind Godot fields yet.

**DERIVED STATS** (computed once, hosted on the Combatant so "core/systems CONSUME, never recompute"):

| Derived | Formula (source) | Feeds from |
|---|---|---|
| `pool` | `max(5, history+6)` (`combatant.py:118`) ⚠ **duplicates** `core.resolution_pool` (Part 4 §1) | history |
| `wound_interval` | `round(end + base + SPI_WI_W·spirit)` (`:35`) | end, spirit |
| `max_wounds` | `min(end//2+1, 3)` (`:30`) | end |
| `health_full` | `round(wi·(max_wounds+1) + STR_HEALTH_W·strength·end)` (`:40`) | end, spirit, strength |
| `stamina_max` | `STAMINA_PER_END·end + STAMINA_PER_SPIRIT·spirit` (`:45`) | end, spirit |
| `conc_max` | `CONC_FOCUS·focus + CONC_SPIRIT·spirit` (3F+2S, ED-902) (`:142`) | focus, spirit |

Note: the *bulk* of derived combat math (`reading`, `reflex`, `disp_lean`, `leverage`,
`recoverability_factor`, …) is **not** hosted on the Combatant — it is computed fresh each call in
`combat_systems.py` from the raw attributes. (A composition choice, not a defect; flagged for map completeness.)

**PER-BEAT MUTABLE STATE** (the wrapper writes each beat): `grip_position` (`grip_target`), `range_avail`
(`range_utilization`), `facing` (`facing_target`), `sel_head/sel_dmg/sel_gap/sel_perc/sel_pc/sel_eff`
(`select_mode`), `lunge_depth` (`lunge_quality`), `stamina` (`act_cost`/recovery), `conc` (drain/recover),
`initiative` (the Vor/Nach signed state — decay/steal/overcommit), `poise` (kuzushi — `poise_regen`/breaks),
`weapon` (mutable mid-fight via the half-sword auto-switch `halfsword_target`).

### 2.3 Mechanic ↔ node ↔ primitive binding (condensed; full detail in D-agent output)

| Node | Mechanics fired | Reads |
|---|---|---|
| **EngagementInit** | `reach_base` (measure) | grip, weapon reach |
| **Approach** | `disp_lean`, `poise_regen`, `grip_target`, `range_utilization`, `facing_target`, `select_mode`, `reach_threat`, `approach_displace`, `close_rate`, `stophit_sigma`→`strike` | disp, agi, stamina, weapon reach/head, armour-defeat |
| **AwaitTempo** | `weapon_tempo`/`close_tempo`, `reopen_prob`, `init_hold_decay` | agi, fatigue, reach_threat |
| **Exchange** | `commit_depth`, `lunge_quality`, `act_cost`, `mental_fatigue`, `reach_sigma`, `init_emphasis_sigma`, `consistency`, `read_contest`(←`reading`/`reflex`/`legibility`), `attack_sigma`/`defence_sigma`/`armor_defeat_sigma`/`initiative_sigma`→`assemble_net_sigma`, `indes_steal_amount`/`counter_select`, `resolution_pool`→`resolve`→`strike`, `overcommit_exposure`, `impose_node` | full attribute set + live stamina/conc/initiative/poise + per-beat sel_*/grip/range/facing |
| **Bind** | `bind_sigma` (leverage+tactile+strength+`blade_guard` catch), `init_steal_factor`, `bind_dominance_p`→`strike` | blade_guard, leverage, strength, eff_cw(leverage) |
| **Riposte** | `disrupt_resist_p`, `counter_success_prob`→`strike` (graze), role-flip | conc |
| **HitLanded** | `clamp_initiative` (Vor gain/loss), `clamp_poise` (break), `apply_wound`→WoundTracker | health_full, cumulative_damage |
| **Contact** | `leverage`, `reflex` (slip-inside), `grab_available`/`grab_sigma`/`grab_outcome` gated on `opening_created` | strength, leverage, grab affinity |
| **Separation** | 4 reasons (2 dead — §2.1) | stamina, exchange count |
| **InterTurn / UpsetCheck** | stamina/conc recovery, `UPSET_FLOOR` clamp | stamina_max, conc_max |

### 2.4 Tradition injection points (where methodology plugs into the graph — 9, all reference-valid)
`approach.measure`, `reopen.measure`, `exchange.commit`, `exchange.read`, `exchange.mode`,
`exchange.bind_entry`, `exchange.counter`, `burst.continuation`, `contact.axis`. **Status:** the *hooks* are
built and tested; the generic branch is live; the **per-tradition biasing of each branch is largely unwired**
(only the imposition gate + familiarity + equal-affinity-budget landed — WS-4). This is the single largest
"present hook, absent content" surface after the K=0 levers.

---

## PART 3 — DESIGN-PROMISED BUT ABSENT (the wiring gaps)

Mechanics the design corpus promises for which **no engine function exists** (B-agent, cross-checked). These
split into "out-of-scope by design" (cross-system / scene-layer / TTRPG-only) and "in-scope but unbuilt".

### 3.1 In-scope, unbuilt (real gaps for a complete PC engine)
- **Ranged combat — entirely absent.** No projectile, reload, ranged-DR (`combat_v30.md:268-277`), cover-DR,
  or stress-friendly-fire (PP-720) function anywhere. `combat_engine_v1` is a **melee-only 1v1 duel resolver**.
- **Abilities-as-access schema** (`phase4_5_plan §254-266`): the 7 phase-slots + point-buy affinity budget +
  learning-gate + ~55-entry access catalogue + trigger/cost/prereq schema — **NOT STARTED**. `ability_primitives`
  only exposes the old `eff_cw` +/× modulator (inert, 1.4).
- **Phase-4a game-theoretic layer** — Bayesian-signaling read, mixed-strategy feint, Stackelberg-timing
  initiative, within-fight threat-memory/adaptive-bias — **NOT STARTED** (informal substrate only).
- **Disengage / cavazione** (Italian bind-refusal), **Nachreisen** (pursuit-on-recovery), **body-void
  counter** — the "concrete-mechanics queue", not built.
- **Balance channel 80% suppressed** — `balance_eff` wired at only 1 of 5 intended sites (D-agent/B-agent via
  `tradition_decomposition_v1.md:142`).
- **Named tradition techniques** (Meisterhäue, Versetzen/Absetzen, Kiriotoshi, Zanshin, Compás,
  Ángulos/círculo, Four Governors, Suki/metsuke, Maai; Chinese `burst_extend`, Filipino `flow`) — **candidate
  only**, no functions.
- **Staged incapacitation** — the engine resolves only binary `felled`; no Stage-1 (Down/stabilise) / Stage-2
  (Dying) / Medicine-roll distinction (`combat_v30.md:109-111`).

### 3.2 ⚠ Dead ability lever with a live-labelled contradiction (real finding)
**`seize` / `vorschlag` / `sen_no_sen`** (pre-contact seizure): the ability table labels them **"live"**, but
B-agent found their **consumer was cut 2026-06-05** — they "do nothing when equipped"
(`ability_armature.md:47`, self-contradiction flagged in-doc). This is a genuine wiring rot: a mechanic
advertised as wired whose sink no longer exists. Worth an editorial-ledger entry.

### 3.3 Out-of-scope by design (correctly absent from the 1v1 engine)
Scene envelope / N-vs-M (`scene_combat_design_v1.md`, gated on ED-911), Fibonacci group bonus, Zone Collapse,
Rescue/Momentum/Multi-Engagement, Mass-Combat interface, Thread-in-combat, Combat-World-Bridge, Fieldwork
transitions — all live in *other* subsystems or the unbuilt scene layer. The discrete TTRPG action menu
(Full Guard/Dodge/Feint/Take-a-Breath/Establish-Distance/Stunt) is **deliberately dissolved** into the
continuous approach/pool/commit model (feint-as-attack, WS-5) — not a gap, a design choice.

### 3.4 Doc-consistency flags (for the editorial lane, not the engine)
- **Stamina formula conflict:** `combat_v30.md:302` (`Endurance×5`) vs `combat_design_v1.md:286`
  (`End+History+1−armour`) — the two design docs disagree; the engine follows a *third* form
  (`STAMINA_PER_END·end + STAMINA_PER_SPIRIT·spirit`).
- **Combat Pool defined 3 ways** (CLAUDE.md §5) — reconciled in code to `max(5, history+6)` but see Part 4 §1.
- **Yield/Surrender/Disengage (§11.4)** present in `combat_design_v1` but dropped from `combat_v30`'s index.

---

## PART 4 — CROSS-MODULE COMPLIANCE (primitives/emergence + physics/biomechanics)

### 4.1 Emergence & name-freedom — STRONG PASS (the doctrine working)
- **No `if weapon == '<name>'` branch exists anywhere in the 8 resolution modules** (C-agent, grep-confirmed).
  The live math is entirely name-free; weapon behaviour *emerges* from derived properties (`gap_precision`,
  `head_len`, `pob_frac`, `hands`, `wclass`, edge/spine counts). The poleaxe's spike-vs-plate selection, the
  half-sword affordance, the Mordhau precondition — all gate on **physical primitives**, not identity.
- **The σ-pipeline composes cleanly**: `attack_sigma`/`defence_sigma`/`reach_sigma`/`initiative_sigma`/
  `armor_defeat_sigma` each return an additive δσ; `assemble_net_sigma` sums them to one scalar → `core.resolve`
  shifts the *roll* (not the Ob). Mirror-stays-50 is structural, not patched. **This is the single-owner /
  compose-from-primitives doctrine upheld.**
- The one genuine name-membership predicate in executable code is `capabilities.py:36` (`name in
  HALFSWORD_FORM/BASE`) — but it lives in the **diagnostic** layer, not the resolution path (§1.2), and mirrors
  the emergent `affords_halfsword`. **Scripting-drift risk if it ever feeds resolution; harmless today.**

### 4.2 Single-owner / duplication — SEVERAL HAZARDS
| Sev | Finding | Evidence |
|---|---|---|
| **MED** (latent) | **Pool formula lives twice and disagrees on fractional input.** `combatant.pool=max(5, history+6)` (no rounding) vs `core.resolution_pool=max(5, int(round(history))+6)`. **Verified:** history 3.4 → 9.4 vs 9; 3.6 → 9.6 vs 10. Dormant only because History is integer-default today; the live resolve uses core's owner, `c.pool` caches the other. | `combatant.py:118`, `core.py:30-32` |
| **HIGH** (doc-vs-reality) | **`config.py`'s "all tunable coefficients in ONE place" is false** — ~60+ SIM-CALIBRATE/FIAT knobs live as module globals outside CFG (`core.py:63-216`, `combat_systems.py:286-356`, `weapon_physics.py:52-665`). A single-source file owning a fraction of the seeds misleads any re-tuning pass. | C-agent, multiple |
| **MED** | **The "steel-hammer authority ≈ 8" anchor is triplicated** as 3 independent literals: `core.PERC_AUTH_REF=8.0`, `weapon_physics.PERC_CAP=8.0`, `config.ADEF_PERC_REF=8.0` — conceptually locked, nothing enforces equality; a Phase-C re-fit desyncs them silently. | `core.py:142`, `weapon_physics.py:54`, `config.py:62` |
| **MED** | **`damage()` blunt branch hardcodes `3.0*(perc/8.0)`** duplicating `HEFT_HEAVY=3.0` and the 8.0 anchor as bare literals; the `perc` default is written as int `8` in one signature, float `8.0` in the other. | `core.py:251,264` |
| **LOW** | `point_concentration` read through two parallel paths (`w['geometry'][...]` vs baked `geo[...]`); `stamina_max`/`conc_max` name collision across 3 scopes (§1.2). | C-agent |

### 4.3 Grounding (physics/biomechanics) — HONEST, but thin at the CFG layer
- **Genuinely grounded** (cite a real first principle, quoted in-docstring): the `RESIST` armour table
  (**Alan Williams, *The Knight and the Blast Furnace*** — per-cell joule figures), `PERC_2H_HANDS=0.25`
  (**Oh et al. 2022** measured 2H/1H force ratio), `AGILITY_EXP=0.25` (**Cross & Nathan 2009 / Fleisig 2002**
  handle-axis swing studies), `energy_credit` (**Nathan 2003** constant-power bat-MOI), `thrust_authority`
  (**Fiore/Talhoffer** half-sword lever, direction grounded), `reversed_grip` (HEMA — **direction** grounded,
  magnitude honestly `[FIAT]`). **~6 mechanics carry citations; the model is honest about labelling fiat as
  fiat.**
- **The CFG layer is ~entirely bare tuning knobs.** Of ~200 CFG keys, effectively **zero** carry a physics
  derivation — provenance is ledger cites (PP/ED/"Jordan <date>") + `[SIM-CALIBRATE]`/`[FIAT]`. **The physics
  lives in the `weapon_physics`/`core` derivation layer; CFG is the tuning surface.** This is defensible and
  self-declared, but the ratio (6 grounded : ~240 bare) is the true state of "reliance on physics".
- **⚠ One semantic inversion** (verified): `GAP_EXPOSURE={'none':1.0,'cloth':0.85,'mail':0.90,'plate':0.90}`
  — the thrust-accessible-gap fraction is listed **higher for plate than cloth**, physically backwards (a soft
  gambeson should be ~fully accessible). Masked by a `max()` in `_transmit` so it doesn't bite today, and
  self-flagged `[SIM-CALIBRATE]` with the value fit to a *selection outcome* (the poleaxe hammer→spike flip),
  not to gap geometry — "the tail wagging the dog". `core.py:105`.
- **`percussion-through-plate` is explicitly FIAT** — "no melee-speed behind-plate data exists; magnitude is
  FIAT" (`core.py:107-115`). Honestly labelled.

### 4.4 Emergence-by-deferral & shape divergence
- **HIGH (characterisation):** ~7 primitives are wired-but-K=0 (§1.4) — the "emergent" surface *looks* richly
  composed but ~7 of its inputs are switched off. Defensible as staged landing (the U9 capstone adjudicated
  this deliberately), but an audit fact: their emergent behaviour has never load-borne a single fight.
- **MED — shape divergence:** the mode-selection `sel_*` bundle is a 5-then-6 **positional tuple** manually
  unpacked at each site (`combat_systems.py:448,542,579`) — re-growing exactly the positional fragility that
  `core.strike` was refactored to a keyword chokepoint to *eliminate*. A named record would restore the idiom.
- **MED — scale-local import dialect:** the `sys.path.insert + bare import core` non-package idiom diverges
  from every other `systems/<sub>/sim/` package; it's the scar tissue of the `import systems` collision (the
  slice-8 rename). Works, but it's a local convention the rest of the corpus doesn't share.

### 4.5 Module-vs-module comparative scorecard (quantitative)

Every module scored against the *same* axes so they can be ranked against each other. Metrics are measured
(grep over the source): **grounded** = in-code references to a physics/biomechanics/HEMA first principle
(Williams/Oh/Nathan/Cross/Fleisig/Fiore/rigid-body/joule/treatise); **bare** = `[SIM-CALIBRATE]`/`[FIAT]`/
`[ASSUMPTION]` tuning tags; **name-branch** = weapon-NAME membership tests in *executable* lines.

| Module | LOC / defs | grounded | bare-knob | name-branch | Single-owner role | Grade |
|---|---|---|---|---|---|---|
| `geometry` | 96 / 6 | 13 | **0** | 0 | OWNER of gap/thrust/cut/perc factors; pure bake | **A** — small, pure, grounded, zero knobs |
| `core` | 293 / 11 | 19 | 2 | 0 | OWNER of pool/resolve/coupling/damage; RESIST=Williams joules | **A-** — exemplary grounding; ≈8.0 anchor + damage literals dup'd |
| `weapon_physics` | 756 / 37 | **40** | 25 | 0 | OWNER of heft/percussion/agility; reach-diagnostic labelled | **A-** — the physics heart; densest grounding, honest fiat; biggest knob load (physics-shaped) |
| `combat_systems` | 950 / 69 | 22 | 17 | 0 | OWNER of reach_base/wield_heft/the σ-functions | **B+** — name-free across 950 LOC (impressive); 2nd tuning surface; `sel_*` positional-tuple shape-divergence lives here |
| `combatant` | 151 / 17 | 3 | 0 | 0¹ | HOSTS derived stats ("consume, never recompute") | **B+** — clean host, ledger-cited; **the one single-owner violation (pool dup) lives here** |
| `wrapper` | 371 / 4 | 4 | 0 | 0 | orchestrator / state-graph executor | **B** — plumbing; hosts the 2 dead separation branches + dead `ready` field |
| `contact` | 78 / 4 | 4 | 2 | 0 | consumer (reaches through `S.WP` — cycle-break smell) | **B** — clean idiom, built-not-fully-activated |
| `ability_primitives` | 79 / 4 | 4 | 0 | 0 | the `eff_cw` hook | **B-** — hook wired, content absent (inert 1.0); `kit` orphan here |
| `traditions` | 61 / 3 | 4 | 0 | 0 | tradition profiles | **C+** — thin; `profile` orphan/superseded |
| `config` | 191 / 0 | 17² | 13² | 0 | the CFG knob store (~200 constants) | **C+** — honest tuning surface, but "single-source" docstring is false (~60 knobs leak to module globals) |
| `capabilities` | 169 / 4 | 5 | 0 | **1** | a 2nd, name-keyed source of truth for half-sword | **C** — the weakest emergence link: the sole executable name-gate (`:36`), quarantined to the diagnostic layer |

¹ `combatant`'s single name literal is a *default parameter* (`weapon='arming'`), not a branch — emergence-clean.
² `config`'s "grounded"/"bare" counts are comment references, not derivations — CFG is bare *by design*.

**How the modules compare — the through-line:**
- **Emergence is uniformly strong.** Ten of eleven modules have **zero** weapon-name branches in executable
  code, including the 950-LOC `combat_systems`. The *only* name-gate is `capabilities.py:36`, and it lives in
  the diagnostic layer, not the resolution path. On the "never special-case an entity" axis the engine is
  near-exemplary; `capabilities` is the single module that regresses, and only in a non-load-bearing surface.
- **Grounding concentrates where it should.** The physics lives in `weapon_physics` (40) + `core` (19) +
  `geometry` (13) — the derivation layer — while `config` is honestly the tuning surface. The gradient is
  correct: the modules that *compute physical quantities* cite physics; the modules that *orchestrate* (wrapper,
  traditions, ability_primitives) don't need to and don't pretend to. No module fakes grounding it lacks.
- **Single-owner is upheld with three named exceptions.** Reach and impact-force each have exactly one live
  owner (`combat_systems.reach_base`, `weapon_physics.heft`), with the `weapon_physics` duplicates explicitly
  demoted to "diagnostic-only" (`weapon_physics.py:23`) — the CLAUDE.md-flagged reach fork is **resolved**. The
  live violations are narrow and itemised: the pool formula (`combatant` vs `core`), the ≈8.0 anchor
  (`core`/`weapon_physics`/`config`), and `config`'s false single-source claim.
- **The composition idiom is consistent** (σ-return contributions summed at `assemble_net_sigma`) with two
  local dialects: the `sel_*` positional tuple (`combat_systems`) and the non-package import path — both
  cosmetic, both in the "restore the idiom" bucket, neither a correctness risk.

---

## PART 5 — RANKED FINDINGS & RECOMMENDATIONS

**Genuinely broken / rot (fix or ledger):**
1. **`seize`/`vorschlag`/`sen_no_sen` advertised "live" but consumer cut** (§3.2) — file an ED; either
   re-wire the pre-contact-seizure sink or relabel the abilities dead. *Misleading-status rot.*
2. **Pool formula duplication with fractional-History divergence** (§4.2) — make `Combatant.pool` call
   `core.resolution_pool` (single-owner); latent today, a bug the moment History goes fractional.
3. **2 dead separation branches** `beat_exhaustion`, `collapse` (§2.1) — give a reachable trigger or delete
   (the engine's own test asks for this).
4. **6 dead/vestigial functions + `Combatant.ready` field** (§1.3) — cleanup pass.

**Grounding / correctness hazards (review):**
5. **`GAP_EXPOSURE` semantic inversion** (§4.3) — re-derive from gap geometry, not a selection outcome; the
   `max()` mask is fragile.
6. **The ≈8.0 percussion anchor triplication + config.py single-source claim** (§4.2) — single-source the
   anchor; correct or scope the CFG docstring.

**Frontier (design-gated, not defects — the "present hook, absent payload" surface):**
7. **Tradition per-branch biasing** at the 9 injection points (§2.4) — the largest wired-but-generic surface.
8. **The abilities-as-access schema + Phase-4a game theory** (§3.1) — NOT STARTED, the biggest unbuilt blocks.
9. **The K=0 levers** (§1.4) — activation deferred to scenario-specific calibration + the one Jordan grip-
   invariant-thrust ruling (U9 capstone).
10. **Ranged combat + staged incapacitation** (§3.1) — absent; decide if in-scope for `combat_engine_v1` or a
    sibling resolver.

**Shape / hygiene:**
11. `sel_*` positional tuple → named record (§4.4); non-package import dialect (accepted, noted).

**Overall verdict:** the live resolution engine is **doctrine-compliant and substantially complete for
melee 1v1** — emergent, name-free, cleanly composed, honestly grounded where it claims grounding. The gaps are
overwhelmingly **known frontier** (deferred activation, unbuilt tradition/ability/ranged layers), not silent
breakage. The genuine defects are small and itemised above.
