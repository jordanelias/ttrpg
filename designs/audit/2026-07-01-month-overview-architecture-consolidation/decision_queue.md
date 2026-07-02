# Jordan Decision Queue — 2026-07-01

## Status: LIVE — the single consolidated list of gated decisions as of this session

Everything below is **surfaced, not decided**. The consolidation session touched none of
these outcomes. Ordered roughly by how much downstream work each unblocks.

## Scene combat (Track 2 + phases)

1. **wt/spd cost-path de-leak** (`combat_engine_v1/core.py:55`, `systems.py:46`) — candidate
   roughly doubles spear damage. Measurement harness + roster-wide before/after delta report
   prepped in `designs/audit/2026-07-01-scene-combat-track2-decision-prep/` (PR #51).
2. **`WP.reach()`/`WP.authority()` vs `systems.reach_base`/`wield_heft` single-source home**
   (`weapon_physics.py:193,205`) — comparison doc of what each side computes prepped (PR #51).
3. **Scene-combat Phase 4a (game-theoretic layer) / 4b (abilities-as-access) / 4c
   (channel-leverage §C) / Phase 5 (contact axis) / WS-7** — full plan at
   `designs/scene/combat_engine_v1/phase4_5_plan_v1.md`; none started; design-laden.
4. **ED-1042** — wound-model spec-vs-code drift ruling (open since 2026-06-24).
5. **ED-1050 residual** — re-export RESIST/GAP_EXPOSURE/gap-game logic to
   `weapon_resource.gd`/`strike_module.gd`; Key-log parity stays known-red until done.

## Mass battle / simulation

6. **Coordinate-field flip (field-ON)** — unratified candidate behind default-OFF toggles;
   gauge OFF 5/13 → ON 4/13 with new H2/H9 divergences (PR #45).
7. **`orchestration.py` decomposition Stages 3-6** (ED-1043) — each stage gated.
8. **Sim degenerate win-share** — a seeded batch yields one faction ~87%, two at 0%, and
   nothing flags it; balance tuning + a wider regression oracle are design calls.
9. **`sim/` vs `tests/sim/` vs `tests/sim_framework/` rename** — documented collision,
   high blast radius (PR #49).

## Godot conversion

10. **The strategy doc's 8-item open register** (`designs/audit/2026-06-10-godot-conversion-strategy/`)
    — downward Key delivery (ED-1006), Python end-state, faction-stat inversion, Key runtime
    form (needs K8), autoload ruling, first module target, D6 Church 4/4-vs-5/5, standing
    dockets. All unruled as of 2026-07-01.
11. **Gate-0 preconditions** — KeyStore v2 (valoria-game frozen since 05-04), spine base
    classes, RNG service, K8 performance verdict. None executed.
12. **ED-1051** — module-contract closure priorities: 10/27 modules doc:null (start with
    `engine_clock`, the temporal spine), 11/27 resolvers [ASSUMPTION]-grade.

## Canon / editorial

13. **Attribute-roster ratification** — `descriptor_registry.yaml` 9-attribute roster IN
    FLUX; alias folds (Cognition→Acuity, Spirit→Will) are Jordan-vetoable; `agg.*`
    placeholders await the R7/derived-stats §14 migration decision. The names_index mirror
    added this session is warn-tier only, pending this ruling.
14. **`needs_jordan` ledger items** — the open set in `canon/editorial_ledger.jsonl`
    (includes ED-1051; NPC naming; ID-collision reconciliations).
15. **contest_rebuild Stage 1+ gates** — each stage ratified individually (Gate 0 ratified
    2026-06-30; ED 1055-1079 / PP 800-809 reserved).
16. **`contest.py` fabrication-debt triage** — 19 uncited constants block the J-31
    terminology propagation into code.
17. **values_master.yaml successor** — quarantined this session (step 6); decide: port the
    generator to working-tree reads and regenerate, or retire it in favour of typed
    engine-params exports (step 8's discipline) as coverage grows.

## Orchestration / workflow (new this session)

18. **Propagation-spec authorship** — the holonic doctrine
    (`designs/architecture/holonic_container_doctrine_v1.md`, PROPOSED) names the
    cross-scale propagation contract (aggregate-up/distribute-down transform, ordering &
    determinism, termination/convergence guarantee) as the highest-value unauthored canon:
    it feeds conversion-register #1 (downward Key delivery) and the `engine_clock` gap
    (ED-1051). Top-tier judgment work; needs a Jordan go + lane slot (workplan v5 §3 docket).
19. **Agent-Teams / subagent-roster adoption** — the ingested workflow spec (§6-§7)
    prescribes promoting recurring roles into `.claude/agents/` only on recurrence; none
    created this session. Decide if/when a standing conformance-scanner or emergence-auditor
    role has recurred enough to earn a definition.
20. **Doctrine ratification** — `holonic_container_doctrine_v1.md` itself is PROPOSED,
    Jordan-vetoable.

## Housekeeping

21. **Stale merged branches** (`design/scene-combat-v1`, `origin/scene-combat-track2-cleanup`)
    — deletion offered, not performed.
