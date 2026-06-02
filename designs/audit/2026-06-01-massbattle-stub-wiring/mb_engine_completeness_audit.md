# Mass-Battle Engine — Architecture & Mechanic-Wiring Completeness Audit

**Date:** 2026-06-01 · **Target:** `tests/sim/sim_mb_sigma.py` @ Phase-3 (`7cfa44d5`) · **Spec:** `designs/provincial/mass_battle_v30.md` (v4.8, 925 L)
`[SELF-AUTHORED — bias risk]` much of this engine is my own work; this audit actively hunts for what is *missing*, stated as an independent reviewer would. Verdict-first, no false balance.

---

## Q1 — IS IT A MODULAR WRAPPER-OVER-MODULES CONTAINER?

**No.** `sim_mb_sigma.py` is a **single ~2,640-line monolith** with **zero sibling-module imports** (verified: only stdlib `os/sys/math/random/...`). It contains ~50 top-level functions + 3 dataclasses (`Subunit`, `Unit`, `_ColBlock`), composed by direct in-file calls. The only "wrapper" is the test harness `gauge_mb.py`, which `exec(open(ENGINE).read())`s the whole file into its namespace — string-exec, not import; it runs the battery, it does not orchestrate modules.

So the engine is **function-modular inside one file**, not a **container of separately-loadable modules**. Jordan's intuition is correct: a module/container split *would* make editing and troubleshooting easier, because today:
- the file mixes **four concerns** in one flat namespace — geometry (cells/octagon/facing), the continuous σ-resolution head (`roll_pool`/`compute_degree`/`_sigma_net_boost`/the `_*_sigma` modifiers), the per-cell layer (`_ColBlock`/`build_column_grid`/fatigue/charge/envelopment), and the turn/battle orchestration (`run_battle`/`run_multi_turn_battle`/`volley_phase`/pursuit);
- every behaviour toggle is a module-level `PC_*` / `SIGMA_*` / `MORALE_*` constant read at exec time — there is no manifest, no registry, no per-mechanic on/off surface beyond scattered env vars;
- a test exercising one mechanic must `exec` the entire engine.

**Recommendation (PROPOSAL, not yet done):** extract along the four existing seams into a package — `mb_geometry.py`, `mb_resolution.py` (σ head), `mb_percell.py`, `mb_orchestration.py` — with a thin `mb_engine.py` wrapper that imports them, and a single `MECHANICS` registry mapping name → (function, toggle, canonical-source). This is a **refactor of execution structure only** (no mechanic changes), so it is a clean mechanical-tier task and would be byte-exact-verifiable against the current `PER_CELL=0` baseline. Not started; flagged for Jordan's go/no-go.

---

## Q2 — IS EVERY CANONICAL MECHANIC WIRED IN? — VERDICT: **NO (and that is partly correct)**

The engine is a **battle-resolution** simulator. Measured against the full `mass_battle_v30.md` Part A, it implements the **resolution core completely** but omits (a) several **named formations/tactics** that are real in-scope gaps, (b) the **two-stage general-death event**, and (c) the **campaign-layer** mechanics (supply, levy duration, reinforcement re-muster) which are correctly out of a battle engine's scope.

**Wiring is verified by symbol presence + live call-site (not from memory).** Status key: **WIRED** (implemented + called in the live flow) · **PARTIAL** (present but reduced/abstracted) · **GAP** (in-scope, absent) · **OUT** (out of battle-resolution scope).

| § | Canonical mechanic | Status | Evidence / note |
|---|---|---|---|
| A.3b | Battlefield geometry (per-shape cells, anchor) | WIRED | `line/arrowhead/horseshoe/gapped_line/refused_flank_cells`, `oriented_pattern` |
| A.4 | Size (TroopCount) continuous depletion | WIRED | `hp_max`, `distribute_casualties`, continuous-size model (header G-3) |
| A.4 | Power → combat pool | WIRED | `roll_pool`, pool from Power |
| A.4 | Discipline (mult tiers, broken) | WIRED | `disc_mult` (≥5/≥3/≥1), `discipline_check_phase` |
| A.4 | Command (generalship dominance) | PARTIAL | command in the morale/erosion denominator (L221-224); ECP `min(Size,Command)+Command` **not** explicit |
| A.4 | Morale value + graded effect | WIRED | `_morale_sigma` (du Picq graded), `morale_start` |
| A.4 | Morale triggers (size<50%/<25%, flanked-and-lost, allied rout, idle) | PARTIAL | size-threshold + flank + erosion present; not all 8 enumerated triggers are discrete (idle-army, allied-rout-same-zone abstracted) |
| A.4 | Morale cap −3 / Cascade Phase | WIRED | `MORALE_PHASE_CAP=3`, applied in `morale_check_phase` |
| A.4 | Encirclement exception (cap removed) | WIRED | encirclement path in morale handling |
| A.4 | Speed tier (Slow/Standard/Fast) | WIRED (combat=PARTIAL) | `Unit.speed` wired to **pursuit**; **combat** closing-speed = **S1/Phase-1 gap** (per-cell cavalry mult exists, canonical tier not yet in combat) |
| **A.5** | **Two-stage general death (incap → killed)** | **GAP** | only the *continuous* generalship effect exists; the **event** (Stage 1 −1 morale/Cmd halved; Stage 2 −2/Cmd=0/all uncommanded) is not triggerable |
| A.6 | Line | WIRED | default formation |
| A.6 | Shield Wall (+2D Def, cannot advance, negate flank) | WIRED (proxy) | `stance=='hold'` (cannot advance) + the Phase-3 brace gate; **named formation + the "+2D Def / negate one flank" rule** are proxied via stance/discipline, not a discrete formation object |
| A.6 | Wedge (+2D Off / −1D Def) | PARTIAL | shape exists (`Arrowhead` ≈ wedge geometry); the **Off/Def dice modifier + "negated by Shield Wall"** rule not explicit |
| **A.6** | **Skirmish (cannot be flanked, −1D vs Heavy)** | **GAP** | absent |
| A.6 | Column (cannot engage, +1 speed) | PARTIAL | `col_grid` is per-cell columns (different concept); the **Column *formation*** (movement-only, +1 speed tier) is not a selectable formation |
| **A.6** | **Feigned Retreat** | **GAP** | absent (and it is the canonical counter to Envelopment + the Hastings model) |
| A.6 | Reserve (commits next turn) | PARTIAL | reserve-depth concept in the per-cell rotation; the **Phase-3-commit Reserve formation** is not a discrete turn-delayed commit |
| A.7 | Battle turn / phase structure | WIRED | `run_battle` (3-phase / 18-tick), `phase_boundary` |
| A.7 | Volley phase (ranged fire pre-movement) | WIRED | `volley_phase`, `_roll_volley_pool` |
| A.7 | Manoeuvre / closing / contact | WIRED | `advance_cells`, `find_contacts`, `_momentum_speed` |
| A.7 | Engagement / exchange resolution | WIRED | `resolve_engagements`, `compute_degree`, σ head |
| A.7 | Cascade-phase strict ordering | WIRED | `resolve_engagements_cascading`, `_cascade_depth_key` (tip-first) |
| A.8 | Envelopment (requires Fast) | WIRED | per-cell wheel/wrap (`PC_WHEEL`, `_envelopment_sigma` dormant but wrap active via `PC_ENVELOP_MOD`) |
| **A.8** | **Ambush (first engagement: defender no Defence)** | **GAP** | absent |
| A.8 | Concentration (all sub-units on one target) | PARTIAL | target assignment exists (`assign_targets`); the **Fibonacci-cap Concentration tactic** is not a discrete declared tactic |
| A.8 | Refused Flank | WIRED | `RefusedFlank` shape + `PC_REFUSE` refusal logic |
| **A.8** | **Hammer & Anvil** | **GAP** | absent as a named tactic (its *ingredients* — holding anvil + Fast envelop — now exist via stance + cavalry shock, but it is not a declarable combined tactic) |
| A.9 | Environmental modifiers (terrain/forest) | **GAP** | comments only; no terrain object, no "Cavalry→Standard in forest", no flanking-impossible terrain |
| A.10 | Thread operations in battle | PARTIAL | `threadwork_check` phase hook exists but is a stub (no thread mechanics resolved) |
| A.12 | Rout (Morale 0, cannot fight back) | WIRED | `.routed`, `rout_resolution` |
| A.12 | Pursuit (Fast only, Size loss) | WIRED | `pursuit_damage` (Fast-gated) |
| A.12 | Recall (Command Ob 2) | WIRED | `recall_check` |
| A.12 | Morale Cascade (rout → adjacent Discipline check) | WIRED | `discipline_check_cascade` |
| A.13 | Between-turn recovery (morale/discipline) | WIRED | `between_turn_recovery` |
| A.13 | Reinforcement re-muster between **battles** | OUT | campaign layer, not a battle engine |
| A.14 | Campaign supply / foraging | OUT | campaign layer |
| A.14 | Levy service duration | OUT | campaign layer |
| Part B | Board-game resolution | OUT | videogame uses the strategic-layer abstraction (PI `<design_doc_framing>`); not a sim target |
| Part D/E | World-bridge consequence scenes, accounting | OUT | post-battle world layer, not resolution |
| — | **Per-cell layer** (density/depth, casualty distribution, depth-damped fatigue, octagon facing, charge puncture, **Phase-3 moral shock**, wheel/wrap/pocket) | WIRED | the experimental `PER_CELL=1` layer, all increments + Phase-3, present and called |

### Counts (battle-resolution scope only; OUT rows excluded)
- **WIRED: 22** · **PARTIAL: 8** · **GAP: 6**
- The 6 in-scope GAPs: **two-stage general death (A.5); Skirmish, Feigned Retreat (A.6); Ambush, Hammer & Anvil (A.8); terrain/environment (A.9).**
- The 8 PARTIALs are mostly *named-tactic / named-formation* abstractions — the underlying resolution effect exists, but the canonical **declarable formation/tactic with its specific dice rule** is not a first-class object.

---

## ROOT-CAUSE READING (why the gaps cluster)

The engine was built **bottom-up as a resolution physics** (geometry → σ exchange → per-cell dynamics), and it models the things that *emerge from positions and stats* extremely well. The gaps cluster in two places:
1. **Declared formations/tactics as first-class choices** (Skirmish/Feigned Retreat/Ambush/Hammer&Anvil/explicit Wedge/Column/Reserve rules). These are *player declarations with specific dice modifiers*, not emergent physics — so a resolution-first build naturally under-covers them. They are the bulk of the in-scope gap.
2. **The general-as-event** (A.5 two-stage death). The engine has generalship as a continuous denominator but no command-decapitation event.

Terrain (A.9) is a third axis the engine abstracts away entirely (flat field only).

**None of these are wiring bugs in what exists** — the resolution core, morale, rout/pursuit/cascade, ranged, and the entire per-cell + Phase-3 charge/shock layer are wired and validated. They are **missing surfaces**, not broken ones.

---

## RECOMMENDATION (priority order; all PROPOSAL, Jordan-gated)

1. **Declared-tactic/formation layer** (closes 5 of 6 gaps): add a formation/tactic declaration object carrying the canonical dice rules (Shield Wall +2D Def/negate-flank, Wedge +2D Off/negated-by-SW, Skirmish no-flank/−1D-vs-Heavy, Column movement-only, Reserve turn-delay; Ambush, Feigned Retreat, Hammer & Anvil, Concentration). Highest coverage gain; maps cleanly onto the existing stance/shape primitives.
2. **Two-stage general death** (A.5): a triggerable command-decapitation event on the existing command/morale machinery.
3. **Terrain layer** (A.9): a battlefield-terrain modifier (forest → Cavalry Standard + no-flank; broken ground), if battles are to be fought on anything but open field.
4. **Architecture refactor** (Q1): split the monolith into the 4-module package + `MECHANICS` registry — execution-structure only, byte-exact-verifiable. Do this *before or alongside* (1) so the new tactic layer lands in a clean module rather than growing the monolith.

**Confidence:** `[CONFIDENCE: high]` on the wiring status of every row (symbol + call-site verified against the committed engine). `[CONFIDENCE: medium]` on the WIRED-vs-canon *fidelity* of the PARTIAL rows — they resolve the effect but were not line-checked against each canonical dice value in this pass (that is a `valoria-mechanic-audit` formula-consistency run, a separate deeper audit).
