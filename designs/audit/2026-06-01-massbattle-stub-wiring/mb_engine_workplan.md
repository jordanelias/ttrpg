# Mass-Battle Engine — Comprehensive Workplan
**Date:** 2026-06-01 · **Engine:** `tests/sim/sim_mb_sigma.py` @ `7cfa44d5` · **Spec:** `designs/provincial/mass_battle_v30.md` (v4.8)
**Inputs:** the architecture+completeness audit (`1a525127`, `…/mb_engine_completeness_audit.md`) + Jordan directives 2026-06-01.
`[SELF-AUTHORED — bias risk]` engine is largely my own; phases stated as an independent reviewer; all mechanical magnitudes Jordan-vetoable, no canon edited without the editorial workflow.

**Two standing directives this plan encodes:**
- **D-A (priority):** modularize the engine into a container/package FIRST.
- **D-B (canon):** *eliminate general death as a consequence of mass battle — capture at worst, never automatic character elimination.* Jordan's explicit canon-structure decision (design authority); implemented via the editorial workflow, not contested.

**Method gate (every phase):** bottom-up from canon + engine → top-down validation (historical precedent / the C1–C7 + H/R gauge) → `PER_CELL=0` byte-exact toggle-off → commit. Canon edits go through `safe_commit` with `canonical_sources.yaml` co-file + an `editorial_ledger.jsonl` ED entry. Stage work; never one mega-block (wall-clock).

---

## SEQUENCING (dependency-ordered)

```
P-A  Modularize (refactor; behaviour-frozen)        ← FIRST (D-A). Unblocks clean landing of all later work.
 └─ P-B  General-death → capture (canon + engine)   ← D-B. Small; lands in the new mb_orchestration module.
     └─ P-C  Declared formation/tactic layer         ← closes 5 of 6 audit GAPs + most PARTIALs. Biggest coverage gain.
         ├─ P-D  Two-stage general EVENT (capture-only)  ← depends on P-B semantics + P-C declaration layer.
         ├─ P-E  Terrain / environment layer          ← independent; gated on "do battles need non-flat ground?"
         └─ P-F  Speed-into-combat (S1) + vectorized penetration (S4)   ← the original Phase-1/2 (still open).
P-G  Cleanup/retire (S7/S8/S9) + deep formula-consistency audit   ← LAST.
```

P-A is a hard prerequisite for clean execution of P-C/P-D (new surfaces should land in modules, not grow the monolith). P-B is independent of P-A in principle but is small and best done just after, in the new structure. P-E and P-F are independent of each other.

---

## P-A — MODULARIZE INTO A CONTAINER (FIRST; behaviour-frozen)

**Goal:** split the ~2,640-line monolith into an importable package along its four existing seams, with a thin wrapper and a mechanics registry. **Zero behaviour change** — the entire phase is verified by byte-exact `PER_CELL=0` (and PER_CELL=1 numeric-identity on the gauge).

**Target structure** (`tests/sim/mass_battle/`):
| Module | Owns (functions already in the monolith) |
|---|---|
| `geometry.py` | `*_cells`, `oriented_pattern`, `cell_facing`, `octagon_angle`, `_support_along_vector`, `atom_max_width`, `cells_to_orig_coords`, `support_engage_frac`, `cell_speed`, facing helpers |
| `resolution.py` | `roll_pool`, `compute_degree`, `_sigma_softcap`, `_sigma_net_boost`, `_morale_sigma`, `_charge_shock_sigma`, the σ-head constants (`SIGMA_*`, `MORALE_*`) |
| `percell.py` | `_ColBlock`, `build_column_grid`, `_engaged_cols`, `distribute_casualties`, `_fatigue_sigma`, `_envelopment_sigma`, `_defender_depth`, `update_stamina`, all `PC_*` constants |
| `orchestration.py` | `Subunit`, `Unit`, `find_contacts`, `assign_targets`, `resolve_cross_side_contention`, `resolve_engagements(_cascading)`, `volley_phase`, `run_battle`, `run_multi_turn_battle`, `run_multi_unit_battle`, pursuit/recall/rally/reform, phase hooks |
| `config.py` | all module-level tunables, single source; env-var reads centralized |
| `engine.py` | thin wrapper: imports the above, exposes the public API the gauge uses, defines `MECHANICS` registry |

**`MECHANICS` registry** (the troubleshooting win): `name → {fn, toggle_env, canonical_source, status}` for every mechanic in the audit table. Enables: one place to see what exists, per-mechanic enable/disable, and a self-test that asserts every canonical mechanic has a registry row (turns the audit into an executable check).

**Steps (staged commits):**
1. Create `tests/sim/mass_battle/` package; move geometry + resolution + percell + config (pure-ish, fewest cross-refs first). Each module commits with a passing import smoke-test.
2. Move orchestration; resolve circular refs via the config module + dependency-injection where a percell fn needs a resolution fn.
3. Write `engine.py` wrapper + `MECHANICS` registry; point a shim `sim_mb_sigma.py` at `from mass_battle.engine import *` (back-compat: `gauge_mb.py` keeps working unchanged).
4. **Verify:** `PER_CELL=0` gauge byte-exact to `7cfa44d5`; `PER_CELL=1` gauge numerically identical (H1–R3 + C1–C7). Registry self-test green.
5. Update `gauge_mb.py` ENGINE path (or keep the shim); update `coverage_matrix.md`; commit.

**Risks/guards:** `gauge_mb.py` uses `exec(open(ENGINE).read())` — the shim must preserve the exact public names it relies on (`make_unit` deps: `Subunit`, `Unit`, `SIDE_A_START_ROW`, `run_battle`, `run_multi_turn_battle`, `ANCHOR_MAP` is gauge-side). Inventory the gauge's used symbols first. **Acceptance = byte-exact**; any diff is a refactor bug, not a tuning question.
**Effort:** L (large surface, low conceptual risk). **Autonomous.**

---

## P-B — GENERAL DEATH → CAPTURE (D-B; canon edit + minor engine)

**Directive:** mass battle never automatically eliminates a character. A general/officer is, at worst, **incapacitated and/or captured**. Removes the "killed" outcome from battle entirely.

**Bottom-up — the three canon sites that currently kill a character in battle:**
1. **A.5 General two-stage death** (L260-263): Stage 2 = "killed", −2 Morale, Command=0, uncommanded.
2. **A.4 morale triggers** (L193-201): "General killed (Stage 2): −2 … −2 general kill" wording + the −5 max-loss clarification.
3. **§D.2 Officer death** (L867) + **companion-officer combat death** (L878): `1d20 ≤ Size lost → officer killed`; companion "killed in battle → departure scene as combat death".

**The change (canon, Jordan-directed):**
- A.5 Stage 2 → **"incapacitated → captured/incapacitated"**: keep the *command* effect (−2 Morale outside cap, Command=0, uncommanded — a downed/captured general still stops commanding) but rename the outcome from *killed* to *incapacitated; captured if the field is lost*. The character survives.
- A.4: reword "General killed" → "General incapacitated (Stage 2)"; the −2/uncapped morale effect and the −5 max stay (mechanically identical; only the lethal semantics drop).
- §D.2: the `1d20` officer roll → an **incapacitation/capture** roll, not death. Companion-officer "combat death" departure scene → a **capture/wounded** scene (the companion is removed from the field, not killed).
- **Add** a short canonical paragraph: *"No mass-battle mechanic kills a player or named character. The worst battlefield outcome for a general/officer is incapacitation and (if their side loses the field) capture. Death of a named character, if it ever occurs, is a narrative/world-layer event, never an automatic battle result."*

**Engine implication (minor):** the engine only ever applied the **−2 morale effect** (L2163) — no elimination code exists. So P-B in the engine = relabel the comment/semantics and (when P-D wires the event) implement *capture state*, not death. Nothing to delete.

**FLAGGED — Jordan/world-layer decision (do NOT invent):** *what a captured general/officer actually triggers* — ransom, imprisonment, escape/rescue arc, Disposition/relationship effects, return-to-play conditions. No prisoner/ransom mechanic exists in canon today (verified: none in `canonical_sources.yaml`). P-B defines the *battle outcome* (capture, not death); the **capture consequence is a separate design decision** to be specified before P-D can fully wire it. The workplan records this as `[OPEN — Jordan: capture consequence / ransom system]`.

**Editorial mechanics:** edit `mass_battle_v30.md` (co-file `references/canonical_sources.yaml` REQUIRED by the design-doc co-file hook) + an `editorial_ledger.jsonl` ED entry recording the Stage-2/officer-death reframing and its Jordan-directive provenance. Commit scope `editorial`.
**Effort:** S (canon-text + 1 engine comment). **Jordan-directed** (canon authority); the *capture consequence* is `[OPEN]`.

---

## P-C — DECLARED FORMATION / TACTIC LAYER (closes 5 of 6 GAPs + most PARTIALs)

**Goal:** make the canonical formations and tactics **first-class declarable objects** carrying their specific dice rules, instead of being proxied by stance/shape. This is the single biggest completeness gain.

**Bottom-up — the canonical objects to add (A.6 + A.8):**
| Object | Canonical rule (mass_battle_v30) | Engine mapping |
|---|---|---|
| Shield Wall | −1D Off / +2D Def; cannot advance; negate one declared flank/turn | formalize from current `hold`-stance proxy; add the +2D Def + flank-negation as explicit modifiers |
| Wedge | +2D Off / −1D Def; negated by Shield Wall | attach to Arrowhead geometry as an Off/Def modifier + the SW-negation interaction |
| Skirmish | cannot be flanked; −1D vs Heavy | NEW; immunity flag + matchup modifier |
| Column | cannot engage; +1 Speed tier; movement-only | NEW formation state (distinct from per-cell `col_grid`) |
| Reserve | cannot engage; commits Phase-3 of next turn | NEW; turn-delayed commit |
| Feigned Retreat | disengage; pursuer Discipline Ob1; re-engage next turn w/ flank; Cmd Ob2 to recognise | NEW tactic; the Hastings model — composes with pursuit + the cavalry shock |
| Ambush | first engagement: defender no Defence allocation | NEW tactic |
| Concentration | all sub-units one target; Fibonacci cap | formalize from `assign_targets` |
| Hammer & Anvil | Shield Wall holds + Fast envelops | NEW combined tactic; its ingredients now exist (hold-brace + cavalry shock + wheel) |

**Design note:** these are **player declarations with fixed dice modifiers**, not emergent physics — which is exactly why the resolution-first engine under-covers them. They land naturally as a `Formation`/`Tactic` declaration on `Subunit`/`Unit` that injects σ-modifiers (uniform-impact, per the established σ-head discipline — NOT pool mods) at `resolve_engagements`.
**Validation:** each formation/tactic gets gauge rows asserting its canonical counter-relationship (Wedge>Line, Shield Wall>Wedge, Skirmish immune-to-flank, Feigned Retreat reproduces Hastings, etc.) against the A.6/A.8 counter-logic + historical precedent. `PER_CELL=0` byte-exact preserved (new layer is opt-in or default-off until validated).
**Effort:** L. **Autonomous** for mechanics; magnitudes Jordan-vetoable. Best landed in the P-A `orchestration`/new `tactics.py` module.

---

## P-D — TWO-STAGE GENERAL EVENT (capture-only; depends on P-B + P-C)

Wire the **general-as-event** the audit flagged (A.5) — but per D-B, as **incapacitation→capture**, never death. Stage 1 (incap: −1 morale, Command halved, Medicine Ob2 stabilize window) → Stage 2 (not stabilized: Command=0, −2 morale, **general captured if field lost**). Triggerable on the existing command/morale machinery; needs the `[OPEN]` capture-consequence decision from P-B to fully resolve the post-capture state.
**Effort:** M. **Jordan-gated** on the capture-consequence decision.

---

## P-E — TERRAIN / ENVIRONMENT LAYER (A.9)

The engine fights only on open ground. Add a battlefield-terrain modifier: forest → Cavalry reduced to Standard speed + flanking impossible; broken ground; high ground. Gated on Jordan's call: **do battles need to be fought on non-flat terrain in the videogame?** If yes, this is a real layer; if the strategic layer abstracts terrain, it may stay OUT.
**Effort:** M. **Jordan-gated** (scope decision).

---

## P-F — SPEED-INTO-COMBAT (S1) + VECTORIZED PENETRATION (S4)

The still-open original Phase-1/Phase-2 from the speed/facing workplan:
- **S1:** wire canonical `Unit.speed` (Slow/Standard/Fast) into **combat closing-speed** (today it feeds pursuit only; per-cell cavalry mult exists but the canonical tier isn't in combat). Canon gives speed no *direct* combat effect → route closing through the tier, don't invent. C1–C7 are the regression guard.
- **S4:** replace `_defender_depth` (mean col depth) with `_support_along_vector` along the charge vector, speed-scaled. C2/C6 braced-repulse + C7 rear-bypass guard against ahistorical dominance.
**Effort:** M each. **Autonomous.**

---

## P-G — CLEANUP / RETIRE + DEEP FORMULA-CONSISTENCY AUDIT

- Retire `_envelopment_sigma` (dormant `PC_ENVELOP_SIGMA=0`) if still redundant after P-C; reconcile superseded v14 items; fix the stale docstring (audit S7/S8/S9).
- Run `valoria-mechanic-audit` (formula consistency) over the now-modular engine to line-check every PARTIAL row's dice values against canon — the deeper pass this completeness audit explicitly deferred (`[CONFIDENCE: medium]` items).
**Effort:** M. **Autonomous.**

---

## OPEN DECISIONS FOR JORDAN (blocking the gated phases)
1. `[OPEN — P-B/P-D]` **Capture consequence**: what happens to a captured general/officer (ransom? imprisonment? escape arc? Disposition effects? return conditions?). No prisoner/ransom mechanic exists in canon. Needed before P-D fully resolves.
2. `[OPEN — P-E]` **Terrain scope**: do videogame battles use non-flat terrain, or does the strategic layer abstract it? Decides whether P-E is built.
3. `[RATIFY — Phase 3]` the 9 `PC_SHOCK_*`/`PC_CHARGE_SIGMA` magnitudes (commit `7cfa44d5`) — still awaiting ratify/veto; not blocking but open.
4. `[CONFIRM — P-C]` formation/tactic σ-magnitudes are Class-B sim-tunable; confirm the validation bands (A.6/A.8 counter-logic + precedent) are the right targets.

## EXECUTION NOTE
Recommended immediate next action on Jordan's go: **P-A**, staged as the 5 sub-commits above, each byte-exact-verified. P-B (canon reframe) can land in parallel as an `editorial` commit since it's text-plus-one-comment and independent of the refactor mechanics. Everything else waits on P-A landing + the open decisions.
