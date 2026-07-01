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
| **Branch** | `design/scene-combat-v1` **UNMERGED** — a large grounded body of work awaiting ratification. |

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
- Once Tracks 1-2 leave the oracle grounded + single-sourced + guarded: **ratify and merge** (bank the work; stop the
  branch drifting). Then **re-export `combat_config.gd` from the canonical oracle** (close the ED-1050 drift) — the
  port's one module finally matches. *Do this before building new layers (Lesson 5: the oracle must be consistent).*

### Track 4 — BUILD FORWARD (on the stabilised, grounded foundation) — design-gated, Jordan's calls
- **REARCHITECTURE P4 — abilities-as-ACCESS** (= WS-4's other half): replace the +/* modulator with access-not-modifier,
  the 7 phase-slots, the point-buy affinity budget, the learning-gate ("can't half-sword/compás untrained"); this also
  resolves the dormant `eff_cw`. Emergent (Lesson 3).
- **WS-4/WS-5 §C residual** — the channel-leverage calibration so each paradigm is decisive in *its* context (currently
  spanish broad-strong / chinese broad-weak). Design-laden.
- **REARCHITECTURE P5 — contact axis** (clinch/disengage/choke; consumes the dead `clinch`).
- **WS-7 multi-combatant envelope** — ratify ED-911, then build the `resolve_scene` wrapper.

## Recommended sequence (the strategic through-line)

**Consolidate before building.** The session's core lesson is that unguarded, ungrounded, or one-sided changes slip in
and the oracle drifts. So: **Track 1 → Track 2 → Track 3 (merge + re-export)** first — get the engine to a grounded,
single-sourced, guarded, port-consistent, *merged* state. **Then Track 4** (abilities / §C / contact / WS-7) on that
stable foundation, each grounded + guarded. Building new layers on an inconsistent oracle would repeat the mistake this
session had to unwind.

**Immediate next step:** Track 1a (the adef-consistency lever) — it's the smallest, closes the one open thread from the
gap game, and its grounded+guarded pattern is the template for Track 2.
