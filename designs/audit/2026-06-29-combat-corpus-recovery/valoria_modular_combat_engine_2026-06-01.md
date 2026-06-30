# Valoria — Modular Combat Engine (rewrite)
**2026-06-01 · architecture rewrite of the combat harness**

> Per Jordan: rewrote the monolithic harness as a **wrapper around the state graph** with a core-engine module +
> per-system modules, where A/B attacker/defender identity is owned once and routed into every subsystem
> automatically. Initialization is the only toggle. This structurally eliminates the recurring role-inversion bug
> class (every major bug this session — frame-mapping, degree-inversion — came from tangled A/B handling).
> `[CONFIDENCE: high — validated to reproduce the corrected engine's results exactly]`

## Why the rewrite (bottom-up from the failures)
Every serious bug this session shared one root: **A/B roles + σ-channels tangled in one 100-line function**, where a
single mis-bound variable silently inverts an outcome. The frame-mapping bug (swapped positional args vs fixed dict
keys) and the degree-inversion bug both hid for multiple turns because nothing was isolated or testable. A modular
wrapper makes both impossible/trivially-caught.

## Architecture
```
combat_engine/
  core.py       — canonical resolution (effective_ob, degree, roll) + armour-aware damage (D1). No A/B knowledge.
  combatant.py  — Combatant object: built ONCE, identity never swapped. Holds stats, weapon vector, derived
                  values, live state, and a `skills` dict (mastery-stack + set bonuses). Roles are OBJECTS.
  config.py     — ALL tunable seeds in one place (Class-C). One edit point for the joint re-tune.
  systems.py    — subsystem modules, uniform contract: pure fns of (aggressor, defender, state, cfg[, rng]).
                  reach · tempo · stamina · concentration · strength-handling · endurance-fatigue · defense modes.
                  NO subsystem ever sees raw 'A'/'B'.
  wrapper.py    — CombatWrapper/driver: owns the state graph (closing→engagement→separation) and the A/B identity.
                  Assigns aggressor/defender ONCE per beat, passes Combatant objects to every subsystem. Role flips
                  are object swaps (frame-safe). fight() is the pipeline: pass A, B, toggle init → run.
```

## The pipeline (Jordan's design)
`fight(A, B, cfg, rng)` — define two Combatants, the wrapper does everything else: resets, initializes live state,
runs the bout loop, assigns roles per beat, calls each subsystem in the correct aggressor/defender slot, resolves,
flips roles on riposte, handles inter-bout recovery. **Only initialization (stats/weapon/armor/skills) is toggled.**

## Validation — reproduces the corrected engine exactly
- **Differentiator (mastery dominant):** History 4v3 **65%**, 6v3 **91%**, Reading 5v3 **100%**. ✓
- **Reach:** spear>dagger **87%**, longsword>dagger **70%**. ✓
- **Armour:** plate>naked **100%**, cut>plate **0%** (cuts useless vs plate). ✓
- **Mirror 49%.** ✓
- **Skill-stacking WORKS:** an equipped footwork+dodge skill set beats untrained same-stats **86%** — the
  mastery-stack / set-bonus mechanic is functional out of the box (skills bias their axes via the `skills` dict).

## Carried-forward balance items (the joint re-tune — now easy in the modular structure)
Same as pre-rewrite (logic ported exactly): **poleaxe vs plate 0%** (slow weapon starved by the 3-exchange cap —
armour-defeat triad fix), **equal-value Str 54 / Agi 46 / End 51 spread 34** (exchange cap favors Str power over Agi
tempo), **longsword vs rapier** balance. All are now single-module / single-config edits rather than surgery on a
monolith.

## Files
`combat_engine/{core,combatant,config,systems,wrapper}.py` — `/home/claude/`. (The old `sg_harness.py` is superseded;
keep for reference until the modular engine is fully re-tuned.)

## Next (ordered)
1. **Joint balance re-tune** in `config.py`: armour-defeat (poleaxe MUST beat plate — give slow weapons per-blow
   weighting or an armour-defeat resolution that doesn't need many swings, via `SLOW_WEAPON_IMPACT_K`); equal-value
   Str/Agi/End→~50; weapon roster spread.
2. **Concentration baseline-consistency** term is wired (FOCUS_CONSISTENCY_K) — validate it.
3. **Multivariate skill + set-bonus system** — foundation works (demo 86%); formalize the equippable skill catalog
   per axis (approach/footwork/grip/reading/cutting/thrusting/parry/bind) + set bonuses.
4. Jordan: differentiator steepness (H6v3=91%, Reading~100% — intended ceiling?).

## Not committed
Lanes ignored per directive; all staged. The modular engine is a clean foundation for the remaining tuning + the
skill system, and maps directly to a Godot combat-manager + system-resolver structure.
