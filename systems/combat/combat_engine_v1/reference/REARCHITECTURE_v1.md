# Combat engine — re-architecture blueprint v1

**2026-06-29 · synthesised from the recovered corpus (7 archives, 41 files) mapped against the live engine by a
6-cluster audit (`designs/audit/2026-06-29-combat-corpus-recovery/`). Class-C, Jordan-vetoable.**

## The complaint, restated
The engine works but its *layering* is wrong: the **wrapper conflates itself with the engine** (it assembles
σ inline), **weapon primitives are scattered** (hand-set `spd`/`wt`/`closes_poorly`/`pob_frac` live next to true
primitives), **subsystems read as if not weapon-gated**, and **geometry is split** from the primitives. The fix is
not new mechanics — the corpus confirms the repo is *ahead* of most of the proposed work (μ-shift, P_auth,
continuous damage, channel removal all landed). The fix is **clean layers + wiring the single-source derivation
that already exists but is unwired.**

## The target — six layers, one direction of dependency

```
L0  WEAPON PRIMITIVES   weapon_physics.py + geometry.py + combatant.WEAPONS
      primitives ONLY {mass, head_len, grip_len, pommel_kg, wclass, hilt, hands, hand_guard,
        blade_guard, reach_adj, clinch, head} + geometry {curvature, point_concentration,
        cross_section, edge_keenness, strike_concentration}.
      ONE derivation -> PoB, MoI, static_moment, authority, agility, reach, heft, {parry,dodge,wind},
        percussion/puncture. Runs once at build (the geometry.bake idiom).
        v
L1  CORE ENGINE         core.py  (wraps the ratified Lane-C r1/r8/m1 — ED-900/904)
      resolution ONLY: resolve (μ-shift), degree, roll_net, pool, coupling/transmit, damage/strike.
      No A/B, no orchestration, no weapon-physics derivation.
        v
L2  WEAPON-GATED        systems.py (pure subsystems) + capabilities.py (the gate registry)
    SUBSYSTEMS            bind/wind/half-sword/percussion/puncture/lunge/reach/measure/clinch/disengage.
      each names its state-graph node + the affordance that gates it (hard gate = availability;
      effectiveness above the gate is CONTINUOUS).
        v
L3  WRAPPER             wrapper.py (orchestrate ONLY) reading state_graph.py (control-flow as data)
      owns the phase loop, A/B identity, ALL mutation. Calls L1 + L2 and applies returned deltas.
      Computes NO σ of its own.
        v
L4  TRADITIONS          tradition.py — cognitive-mode selection-bias (preferred-node imposition +
                          familiarity). NOT a channel-weight scalar (removed 2026-06-29).
        v
L5  ABILITIES           the tradition-primitive layer. "Abilities are basically tradition primitives"
      (Jordan): a tradition is a BUNDLE of ability primitives exactly as a weapon is a bundle of
      physical primitives. An ability = learned ACCESS to attempt a graph transition (never a +X dial);
      effectiveness emerges from L0 physics × the fighter's competence. 7 phase-slots + a point-buy
      affinity budget + the learning-gate ("can't wind/half-sword/compás untrained").
```

The symmetry that organises L0 and L5: **weapon = Σ physical primitives ; tradition = Σ ability primitives.**

## Where the live engine violates this (the worklist)

| Violation | Layer | Fix | Gate |
|---|---|---|---|
| `wrapper.py` assembles `net_sigma` inline (atk_sig−dsig−reach+adef+init+…), commit-Beta, read-logistic, overcommit, indes-steal | L3→L2 | move each into a named pure `systems.*` fn; wrapper sequences + applies | **behavior-preserving** (verify byte-identical) |
| `weapon_physics.py` is the thin one I wrote; the **canonical composite** (PoB/MoI from `{mass,head_len,grip_len,pommel_kg,wclass,hilt}`) is unmerged | L0 | merge recovered composite + `percussion_authority` + defense-affinities into ONE module; add `pommel_kg/wclass/hilt`; validate PoB ≤0.05cm | build-only (not wired yet) — safe |
| `core.p_auth` lives in the resolver | L1→L0 | move to `weapon_physics`; core consumes the scalar | behavior-preserving |
| `core.HEFT={'light':0,'heavy':3}` consumed live | L0 | route `heft ← authority` | **re-baseline** (§9) |
| `systems.GATE` 12×3 hand table consumed at `mode_sigma` | L0 | route `{parry,dodge,wind} ← weapon_physics` | **re-baseline** |
| `WEAPONS['spd']` read at `weapon_tempo` | L0 | route `agility ← 1/(1+MoI)` (fixes the staff) | **re-baseline** |
| `reach_base` categorical (`reach=='long'`+`HEAD_REACH`) | L0 | route `reach ← head_len+2H+reach_adj` | **re-baseline** |
| `armor_defeat_sigma` reads hand-set `percussion` | L2 | route to `p_auth` (DAMAGE branch already does) | re-baseline |
| `closes_poorly`, `wt`, hand `gap`, dead `seize` | L0/L5 | delete vestigial data | cleanup |
| abilities are old `+/*` MODULATORS, not ACCESS; no slots/budget/library | L5 | the abilities build (access-not-modifier + 7-phase slots + point-buy + learning-gate) | **build** |
| contact axis (clinch/disengage/choke) unbuilt | L2 | the one genuinely-missing subsystem (consumes dead `clinch`) | **build** |

## Phased execution

- **Phase 1 — L0 single source (foundation).** Consolidate the canonical `weapon_physics.py` (composite mass→PoB→MoI
  + percussion/puncture + defense affinities), add `pommel_kg/wclass/hilt`, strip `WEAPONS` toward primitives,
  validate (PoB ≤0.05cm; monotonicity; reproduces orderings). *Build-only — no live consumer switched yet.*
- **Phase 2 — L3 de-leak (behavior-preserving).** Move the inline σ-assembly out of `wrapper.engagement()` into pure
  `systems.*` functions; wrapper becomes sequence+apply. Verify **byte-identical** (same seed → same outcomes) + 26
  tests. Move `p_auth` → L0. *No balance change.*
- **Phase 3 — wire L0 consumers (re-baseline).** Route HEFT/GATE/spd/reach/percussion through `weapon_physics`; delete
  the hand tables. Re-baseline per spec §9 (mirror=50, no one-shot, tier spread) at each swap; calibrate the K_* gains.
- **Phase 4 — L5 abilities (build).** Ability-as-access + the 7 phase-slots + the point-buy affinity budget + the
  learning-gate + the access catalogue (from `combat_traditions_classes_ability_library`). Invariant: empty kit ==
  today, byte-identical.
- **Phase 5 — contact axis (build).** clinch / disengage / choke as weapon-gated subsystems (the convergent
  efficacy core; Italian rapier's disengage is the highest-value missing pole).

## Blocked on Jordan (do not resolve unilaterally)
- **D-A damage-scale** (Class-A canon): keep Health/WI fixed (uncapping → fast/lethal) vs rescale up. Gates the
  damage spine + pick-vs-plate magnitude.
- **pommel_kg singletons** — back-solved + physical, not specimen-measured; pull Fortner/Royal-Armouries if exact.
- **Affinity-budget build layer** — point-buy mix-and-match vs method-primary; declared vs emergent sets; synthesis.
- **K_\* calibration gains** (`K_REACH/K_HEFT/K_TEMPO/K_STRD/K_ACT`) — fit in the re-baseline, not asserted.
- **pick > mace vs plate** — ranking ratified, magnitude + canon row are Jordan's.
- **seize lever** — retire vs reroute (`vorschlag`/`sen_no_sen` are dead).
- **Reach-dominance** (r≈0.83) — intended (longer holds measure) or flatten weapon variety.

## Provenance
Recovered corpus + per-cluster analysis: `designs/audit/2026-06-29-combat-corpus-recovery/`. Canonical physics:
`weapon_physics_RECOVERED_composite_2026-06-22.py` + `weapon_physics_calibration_and_wiring_2026-06-22.md`.
Abilities: `2026-06-13-combat-bottomup/combat_ability_system_consolidated_master`. Resolver: Lane-C
`tests/sim/v32-combat-balance/` (ratified). Nothing here re-litigates the ratified r1/r8/m1 math.
