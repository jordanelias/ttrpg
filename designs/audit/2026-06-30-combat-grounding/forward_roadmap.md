# Scene-Combat — Forward Roadmap (2026-06-30, post-Gate-1)

**Status:** planning / orchestration (Class-C, Jordan-vetoable). Folds the un-superseded parts of the origin **WS-0..WS-8
plan** + the **REARCHITECTURE_v1** L0-L5 phases + the **Gate-1 audit** residuals into one prioritized forward plan,
shaped by this session's lessons. Continuity: git history + `HANDOFF.md`; grounding: `combat-grounding-methodology` (memory).

## Context

This session reviewed the scene-combat work, found the Phase-2/3 de-leak was incomplete and percussion authority was
double-derived, and — on Jordan's direction — turned the fix into a fully evidence-grounded weapon×armour×technique
re-baseline (9 commits, `250eefd7`→`2668c747`, all gates green, branch unmerged). That work exposed *how* the corpus
accrues debt, which is the real input to this roadmap.

## Lessons this session → operating principles (apply to every future change)

1. **No change without a regression guard.** The prior de-leak shipped incomplete because *nothing tested behaviour
   preservation* (no mirror/determinism/byte-identical guard existed). Every change now runs the WS-8 methodology +
   the behavioural guards (`test_combat_balance_guard.py`); a re-baseline states its seeded before/after.
2. **Ground, don't pick.** Derive every constant from physics / biomechanics / treatises / materials and
   *adversarially* fact-check it (the workflows refuted fabricated citations + over-claims). No menu-picking, no
   flooring to a sim-fit. `[SIM-CALIBRATE]`/`[DESIGN]`/`[FIAT]` must be *flagged*, never disguised as measured.
3. **Behaviour emerges from primitives — no name tables.** `poleaxe`/`mace`/… are primitive bundles; modes and
   effectiveness derive. The primitive-law purge is not finished (see Track 2).
4. **Single-source is pervasive, unfinished debt.** The "ONE derivation" goal is not met; a quantity derived twice
   *will* drift (percussion authority did). Sweep the remaining duplicates.
5. **Changing one resolution path means checking its parallel.** Damage ↔ sigma (the gap-game's adef-consistency
   finding), and oracle ↔ Godot port (`combat_config.gd` drift). A one-sided change creates a silent contradiction.
6. **Capture provenance.** The load-bearing v4 WS plan was never in the repo; this roadmap + the grounded design doc
   close that.

## Where we are (workplan layers + state)

| Layer | State |
|---|---|
| **WS-0..WS-8** (origin build) | WS-0,1,2,3,6,8 landed; **WS-4/WS-5 §C = PARTIAL** (imposition gate ships but only 2 distinct leaders / 5 contexts — the channel-leverage residual); **WS-7** design-only (gated on ED-911). |
| **REARCHITECTURE Phase 1-5** | P1-P3 (L0 single-source + de-leak + wire) largely done incl. this session; **P4 (L5 abilities-as-ACCESS) not started** (live model is still the +/* modulator; `eff_cw` dormant); **P5 (contact axis) not started** (dead `clinch` primitive). |
| **Gate-1 audit** | de-leak completed, cleanup landed, the grounded percussion/armour/use-mode re-baseline built; **residuals open** (below). |
| **Port bridge (§6)** | the combat slice is the one ported module and it **disagrees with its oracle** (`combat_config.gd` adef_threshold, ED-1050); needs re-export after the oracle stabilises. |
| **Branch** | **MERGED** (PR #40 `d4bf2af3` 2026-07-01T04:46Z; Track-2 cleanup PR #47 `8fbc4b66` 2026-07-01T06:48Z) — see `HANDOFF.md`. `design/scene-combat-v1` is now redundant. |

## The roadmap — prioritized tracks

### Track 1 — CLOSE the combat re-baseline (finish what's in flight) — *highest priority*
- **1a. adef-consistency lever** — unify `adef_cap`'s point branch with the gap-seeking so the spike's *control* matches
  its *damage* (Lesson 5). Grounded + guarded. Jordan-gated (it strengthens point weapons vs plate).
- **1b. File ED-1080+** for the grounded re-baseline (the deferred formal record; the designer-set flags travel with it).
- **1c. Test guards** the audit found missing (Lesson 1): a **heavy-tier** mirror case (the gap-game exposed a latent
  draw-driven heavy-mirror artifact `test_mirror_fairness` never caught); a wrapper-purity / single-source guard.

### Track 2 — FINISH the single-source / primitive-law purge (the "ONE derivation" the audit found unmet) — Lessons 2,3,4
- The remaining Gate-1 re-baseline residuals, each grounded + guarded: the **agility `min(1.0)` FIAT clamp** (flattens
  light-weapon dodge — ground it like the percussion credit); the **`wt`/`spd`** damage-path legacy reads; the
  **`WP.reach()`/`authority()`** vs `systems.reach_base`/`wield_heft` parallel derivations (pick the canonical home);
  **`ADEF_THRESHOLD` non-monotonicity** (ED-1050).

### Track 3 — RATIFY + MERGE scene-combat-v1, then RE-EXPORT the port config — *the consolidation gate*
- **Merge half DONE** (PR #40 `d4bf2af3` + PR #47 `8fbc4b66`, 2026-07-01 — bank the work, stop the branch drifting).
  Still open: **re-export `combat_config.gd` from the canonical oracle** (close the ED-1050 drift) — the port's one
  module finally matches. *Do this before building new layers (Lesson 5: the oracle must be consistent).* Low
  priority per CLAUDE.md §6 (the skeleton covers 1/27 modules and can't compile regardless).

### Track 4 — BUILD FORWARD (on the stabilised, grounded foundation) — design-gated, Jordan's calls

**Full detail (Workstream-0 grounding spine, 7 review lenses, 3 named principles, per-phase gates) lives in
`designs/scene/combat_engine_v1/phase4_5_plan_v1.md` — recovered 2026-07-01 from a local-only plan file that
this roadmap's own Lesson 6 claimed to have captured but hadn't (the compressed summary below had silently
dropped Phase 4a's entire game-theoretic layer). Read that doc before starting any of Track 4; the bullets
below are pointers, not the spec.**

- **Phase 4a — game-theoretic psychological layer** (`phase4_5_plan_v1.md` §4a): formalize read/feint/initiative
  as Bayesian signaling / mixed strategy / Stackelberg timing, plus two new within-fight dynamics (struck →
  adaptive defensive bias; concentration lapse → wrong-option error). **Never built; not previously documented
  in the repo.**
- **Phase 4b — abilities-as-ACCESS** (`phase4_5_plan_v1.md` §4b; = WS-4's other half / REARCHITECTURE P4):
  replace the +/* modulator with access-not-modifier, the 7 phase-slots, the point-buy affinity budget, the
  learning-gate ("can't half-sword/compás untrained"); resolves the dormant `eff_cw`. Emergent (Lesson 3).
- **Phase 4c — the §C contextual-differentiation residual** (`phase4_5_plan_v1.md` §4c; = WS-4/WS-5 §C): the
  channel-leverage calibration so each paradigm is decisive in *its* context (currently spanish broad-strong /
  chinese broad-weak). Design-laden.
- **Phase 5 — contact axis** (`phase4_5_plan_v1.md` Phase 5; = REARCHITECTURE P5): clinch/disengage/choke;
  consumes the dead `clinch` primitive.
- **WS-7 multi-combatant envelope** — ratify ED-911, then build the `resolve_scene` wrapper (design doc:
  `designs/scene/scene_combat_v1/scene_combat_design_v1.md`).

Each of Phase 4a/4b/4c/5 gates behind its own adversarial audit (Gate 3 for Phase 4, Gate 2 for Phase 5) per
`phase4_5_plan_v1.md` — do not treat the one-line bullets above as sufficient to start building from.

## Recommended sequence (the strategic through-line)

**Consolidate before building.** The session's core lesson is that unguarded, ungrounded, or one-sided changes slip in
and the oracle drifts. So: **Track 1 → Track 2 → Track 3 (merge + re-export)** first — get the engine to a grounded,
single-sourced, guarded, port-consistent, *merged* state. **Then Track 4** (abilities / §C / contact / WS-7) on that
stable foundation, each grounded + guarded. Building new layers on an inconsistent oracle would repeat the mistake this
session had to unwind.

**Immediate next step:** Track 1a (the adef-consistency lever) — it's the smallest, closes the one open thread from the
gap game, and its grounded+guarded pattern is the template for Track 2.
