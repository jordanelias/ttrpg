# `systems/` Python architecture audit — differencing all modules, contracts and scripts

## Status: REPORT — RATIFIES NOTHING. No ED allocated, no `## Status:` line flipped, no code changed.

**Scope:** every `.py` file under `systems/` (115 files, 25,116 LOC), plus `engine/` where the
layering question required it. Three axes, per the request: (A) architecture compliance,
(B) consolidation opportunity, (C) erroneous work.

**Date:** 2026-08-11 · **Lane:** IN (cross-cutting) · **Tree state:** `c26a22c`, working tree clean.

---

## 0. Method, and its honest limits

Mechanical first, then hand-verified. Instruments used, in order of precedence:

1. **Existing repo tooling, reused not reimplemented** (§8 invariant): `tools/dead_primitive_census.py`,
   `tools/ci_module_shape_check.py`, `references/module_contracts.yaml`,
   `registers/mechanics_index.yaml`, `references/names_index.yaml`.
2. **An AST pass** over all 153 `systems/`+`engine/` modules: import graph, def/ref graph,
   function-body structural fingerprints, and a set of *idiom probes* (RNG strategy, clamping,
   rounding, state shape, Key access, config source).
3. **`pyflakes`** for genuine defects.
4. **A state-quantity write census** — for each mechanic quantity, every assignment site and whether
   it is bounded at the write.
5. **Import-smoke execution** of all 115 modules.

**Limits, stated rather than implied.** The fingerprinting is structural, so a duplicate that was
*re-typed* with different constants does not group. Reference detection is AST+string, which
over-counts use (biasing toward "alive"), so the dead lists are dead under a *generous* definition.
The token-clustering vocabulary comes from the repo's own registries, which skew to proper nouns —
the state-quantity census (§3.3) is the sharper instrument and is what the consolidation findings
rest on.

**Three claims I checked and had to withdraw** — recorded because a report without its negative
results is not falsifiable:

- *"The degree-string dialect mismatch silently no-ops at the cross-scale echo seam."* **False.**
  `scene_dispatch.py` hand-derives capitalised literals at each boundary from ints/verdicts; no
  subsystem degree string is passed through. The divergence is real, the live bug is not.
- *"`compute_degree` drives conquest outcomes despite being labelled narrative-only."* **False.**
  `resolve_mass_battle` derives its `degree` from size-percentage thresholds, independently. The
  label really is inert. (It is, however, a *ninth* degree derivation — see §3.1.)
- *"61 modules have no test coverage."* **Wrong measurement.** It counted dotted-path references only,
  and `combat_engine_v1` is imported bare after a path insert. The corrected figure is **26**.

---

## 1. Verdict in one table

| Axis | Finding count | Severity |
|---|---|---|
| A. Architecture compliance | 5 classes | 1 high, 2 medium, 2 low |
| B. Consolidation | 4 classes | 2 high, 2 medium |
| C. Erroneous work | 5 classes | 1 high, 2 medium, 2 low |

**The headline is not any single defect.** It is that the corpus shows exactly the signature you
predicted: *many sessions, each internally coherent, composing badly.* The clearest measurement of
that is §3.1 — **one canonical rule ("what degree of success is this?") has nine implementations in
five mutually-incompatible return vocabularies**, every one of them individually well-documented and
correctly cited. No session did anything wrong locally. The rule has no owner, so each session
authored a local one.

| Subsystem | files | LOC | pyflakes | dead fn/const | governed stubs | untested | `sys.path` |
|---|--:|--:|--:|--:|--:|--:|--:|
| combat | 29 | 8,188 | 30 | 5 | 0 | 5 | 18 |
| social_contest | 20 | 7,050 | 41 | 9 | 5 | 10 | 0 |
| factions | 18 | 2,652 | 17 | 12 | 9 | 7 | 0 |
| mass_battle | 6 | 2,392 | 20 | 4 | 0 | 3 | 0 |
| threadwork | 9 | 1,409 | 15 | 22 | 2 | 4 | 0 |
| settlements | 8 | 1,018 | 2 | 15 | 0 | 4 | 0 |
| world | 6 | 745 | 5 | 10 | 3 | 3 | 0 |
| overview | 8 | 597 | 5 | 1 | 3 | 4 | 0 |
| characters | 5 | 555 | 0 | 8 | 1 | 4 | 0 |
| fieldwork | 5 | 504 | 3 | 8 | 6 | 3 | 0 |
| **TOTAL** | **115** | **25,116** | **138** | **94** | **29** | **26** | **18** |

Per-module detail: `appendix_module_table.md`.

**Note on stubs — how they are adjudicated in this report.** `stubwire.stub_resolve` is a *designed*
primitive: a typed no-op, visible to `review_core`'s `stubs.count` ratchet by construction. The 29
governed stubs **are debt** — each is an unimplemented mechanic awaiting canon — and they are counted
as such in the table above and tracked as open work.

They are, however, **required to exist, and are explicitly excluded from the consolidation and
culling axes of this audit.** A stub is not a duplicate of the thing it stands in for, and it is not
a cull candidate: deleting it removes the declared interface and the ratchet's visibility into the
pending work, which is the opposite of paying the debt down. **No finding in this report proposes
removing or merging a stub.** The two stub-related actions (§6 items 4 and 5) both *add* governance —
routing an ungoverned placeholder through `stubwire` so it becomes visible — and neither deletes
anything. C3 additionally **corrects** the repo's own dead-primitive census, which does *not* apply
this distinction and currently reports 8 stub bodies as dead functions.

---

## 2. Axis A — architecture compliance

### A1 · HIGH — a `DEPRECATED` module is the live default personal-combat path

`systems/combat/sim/combat.py` carries an unambiguous banner:

> `[DEPRECATED 2026-06-23 — superseded by combat_engine_v1 (ED-900/904; docket ED-1029).]` …
> `Retained for reference/history only — do NOT wire new game code through this file.`

`engine/cross_scale/scene_dispatch.py:273` imports and calls it:

```python
import systems.combat.sim.combat as combat
rr = combat.resolve_combat_round(parts, scene=ctx.get("scene"), rng=rng)
```

That call sits in the `else` branch of the `DISPATCH_COMBAT_BRIDGE` gate, and that flag is
**default OFF** (`engine/mc_v18.py:81`, confirmed in four places). So on every default campaign run,
personal combat inside a dispatched scene resolves through the superseded v30 model
(pool = Agi×2+History+3, multiplicative STR damage) rather than through the ratified
`combat_engine_v1` σ-engine. The deprecation banner and the runtime default disagree.

This is *knowingly* staged — the flip is blocker-tracked — but the current state is that the
canonical engine is the opt-in path and the deprecated one is the default.

### A2 · MEDIUM — `engine/` depends downward on `systems/`, contradicting the declared layering

CLAUDE.md's `engine/` row states per-subsystem sims *"depend UPWARD on this core (acyclic — autoload
is a leaf)."* Measured: **36 `engine/ → systems/` import edges**, of which 13 are in runtime
(non-test) modules and 5 are top-level (not lazy):

| edge | site |
|---|---|
| `mc_v18 → systems.factions.sim.faction_action` | `engine/mc_v18.py:37` (top-level) |
| `mc_v18 → systems.overview.sim.season` | `engine/mc_v18.py:38` (top-level) |
| `parliamentary_bridge → systems.factions.sim` | `:64` (top-level) |
| `parliamentary_bridge → systems.social_contest.sim.{contest,parliamentary_vote}` | `:65,:66` (top-level) |
| `echo_transport → systems.settlements.sim` | `:58` (top-level) |
| `game_state → {characters,factions,fieldwork,settlements,threadwork,world}` | 11 lazy, in-function |

Combined with `systems/factions → engine` (25 edges), this is a genuine bidirectional package
dependency, not a clean layering. The lazy in-function imports in `game_state.py` are the mechanism
that keeps it from being an import cycle at load time — i.e. the acyclicity is maintained *by import
placement*, not by structure. That is fragile: a future top-level hoist of any one of those 11 lines
turns a working tree into a circular import.

### A3 · MEDIUM — `combat_engine_v1` is a non-package script dir held together by 18 `sys.path` inserts

`systems/combat/combat_engine_v1/` is deliberately a "non-package scripts-on-path dir"
(documented in `systems/combat/__init__.py`). The cost is measurable: **18 of its 29 files mutate
`sys.path` at import**, including three that reach *out of the subsystem* into a frozen test tree:

```
workbench/balance.py:28       '../../../../tests/sim/v32-combat-balance'   # measurement harness
workbench/presets.py:18       '../../../../tests/sim/v32-combat-balance'
workbench/probabilities.py:14 '../../../../tests/sim/v32-combat-balance'
```

`tools/ci_module_shape_check.py` explicitly *excludes* `workbench/` from its cross-container
reach-in rule ("the measurement workbench reaches into the frozen v32 validation station BY
DESIGN"), so this is sanctioned rather than accidental. It remains the single largest obstacle to the
Godot port reading this subsystem as a module tree, and it is why `combat_engine_v1` cannot be
imported by any repo-wide tool without a path shim.

### A4 · LOW — five `systems/` subsystems have zero Python

`_architecture`, `articulation`, `npcs`, `ui`, `victory` are doc-only. Three of them
(`articulation_layer`, `victory`, plus `clock_registry`) carry **declared contracts** in
`references/module_contracts.yaml` with `status: extracted`. A contract marked *extracted* against a
subsystem with no implementation is a currency claim the tree cannot honour. (CLAUDE.md already flags
`characters`/`overview`/`victory` as "doc homes, not yet formalized 1:1 subsystems" — this is the
code-side measurement of the same gap.)

### A5 · LOW — 8 of 27 declared contracts have `doc: NULL`

`npc_memory`, `scene_slate`, `game_director`, `scene_timer`, `audit`, `domain_actions`,
`settlement_economy`, `engine_clock`, `scenario_authoring` declare edges with no backing document.
`structure_audit` already buckets these as "notional"; noted here only so the contract count (27) is
not read as 27 grounded contracts.

---

## 3. Axis B — consolidation

### B1 · HIGH — "degree of success" has nine implementations and five return vocabularies

This is the single most consolidatable thing in the corpus, and the cleanest example of the
multi-session divergence pattern.

| # | site | signature | Overwhelming bar | returns |
|---|---|---|---|---|
| 1 | `engine/autoload/dice_engine.py:94` `degree_from_net` | `(net, ob)` | `net ≥ 2·Ob ∧ net ≥ 3` | `Degree` enum |
| 2 | `engine/autoload/sigma_leverage.py:284` `degree` | `(net, ob, pool)` | pool-aware σ bar | `int` 0–3 |
| 3 | `systems/combat/combat_engine_v1/core.py:57` `degree` | `(net, ob)` | `net ≥ 2·Ob−0.5 ∧ ≥2.5` | `'fail'/'partial'/'success'/'overwhelming'` |
| 4 | `systems/combat/sim/combat.py:161` `_degree` | `(net)` — *opposed margin* | `net ≥ 3` | `'Failure'/'Partial'/'Success'/'Overwhelming'` |
| 5 | `systems/mass_battle/sim/massbattle.py:640` `compute_degree` | `(net, ob)` | `net ≥ 2·Ob ∧ net ≥ 3` | Capitalised strings |
| 6 | `systems/factions/sim/faction_action.py:97` `_degree` | `(net)` — *Ob pre-subtracted* | `net ≥ Ob+3` | Capitalised strings |
| 7 | `systems/threadwork/sim/operations.py:134` `_compute_degree` | `(net, ob)` | **`net ≥ Ob+3`** (additive) | Capitalised strings |
| 8 | `systems/threadwork/sim/opposing.py:87` `_degree_label` | `(net, ob)` | *none — 3 bands only* | `'Meets'/'Partial'/'Failure'` |
| 9 | `systems/mass_battle/sim/massbattle.py:1838` (inline) | size-% thresholds | `a≥0.75 ∧ b≤0.25` | Capitalised strings |

Three of these differ from canon in ways that change outcomes, not just labels. **Correction from an
earlier draft of this report, recorded because the first reading was wrong:** #4 and #6 do *not*
"ignore Ob". #4 bands an **opposed margin** (`net_hits = max(0, off_roll − def_roll)`,
`combat.py:216`) where no Ob exists at all; #6 receives a net with **Ob already subtracted**
(`net = _successes(pool, rng) − ob`, `:520`/`:542`). The divergences are subtler than that, and real:

- **#6 shifts every band by one against canon.** In raw successes `s` with objective `ob`, its
  bands are `s ≥ ob+3` Overwhelming / `s ≥ ob+1` Success / `s == ob` Partial / `s < ob` Failure.
  Canon (`dice_engine.py:94`, from `params/core.md §Degrees of Success`) is `s ≥ ob` → **Success**.
  So *exactly meeting the objective is a Success under canon and a Partial here* — and Partial is
  the one band with **no effect at all**: `_govern` (`:546`) rewards Overwhelming/Success and
  penalises Failure, so a roll landing exactly on Ob produces neither. Same dead band in `_muster`
  (`:523`). Whether that no-effect zone is intended is a design call, not something this report
  settles — but it is not what canon specifies.
- **#7 `operations._compute_degree` uses an additive `Ob+3` Overwhelming bar** where canon is
  multiplicative `2·Ob`. These agree only at Ob = 3. At Ob = 5 canon requires 10, this requires 8.
- **#6 is not even rolling the canonical die.** `_successes` (`:90`) is
  `sum(1 for _ in range(int(pool)) if rng.randint(1, 6) >= 4)` — a **d6 ≥ 4** pool, cited as
  "v17 strategic-scale resolution (M3)". The entire faction/strategic layer therefore resolves on a
  different dice system from the d10 engine every other scale uses, with no conversion documented at
  the seam. This is the largest single mechanical divergence in the corpus and it is *upstream* of
  the degree question.

#### B1a · The deeper divergence is the *calling convention*, not the return type

Return-vocabulary drift is visible at a glance. The input convention is not, and it is worse: across
the nine implementations, the parameter named `net` carries **four incompatible meanings**, and the
parameter named `ob` carries **two**.

| convention | meaning of `net` | meaning of `ob` | sites |
|---|---|---|---|
| **raw net + threshold** *(canonical)* | successes rolled | difficulty threshold | #1 `dice_engine`, #2 `sigma_leverage`, #3 `core`, #7 `operations` (`:178`), #8 `opposing` (`:146`) |
| **Ob pre-subtracted** | successes **minus** Ob | *(absent)* | #6 `faction_action` (`:520`, `:542`) |
| **opposed margin** | `max(0, attacker − defender)` | *(absent)* | #4 `combat/sim` (`:216`) |
| **opponent's roll as Ob** | successes rolled | **the other side's net** | #5 `massbattle` (`:951`, `:1517`) |

Every one of these is locally sensible and locally documented. Together they mean that a degree
helper cannot be moved, shared, or reasoned about across subsystems without reading its call site
first — and that a refactor which "obviously" swaps one implementation for another will compile,
run, and silently produce different outcomes. There is no type, name, or test that distinguishes
them: they are all `(int, int) -> str`.

This is the concrete mechanism behind the many-sessions problem. A session inheriting `net` from its
own subsystem had no way to discover that the identifier meant something else one directory over.
**Any consolidation of §3.1 must fix the convention first and the vocabulary second** — folding the
return types while leaving four input conventions in place would convert a visible divergence into
an invisible one.

The vocabularies are `Degree` enum / `int` / lowercase / Capitalised / `Meets`-3-band. Nothing
currently breaks, because every cross-scale seam hand-translates (see §0's withdrawn claim). But
`domain_echo.compute_domain_echo` keys on Capitalised strings and returns
`fires=False, notes=["Unknown degree '<x>'"]` on a miss — it **fails silently, not loudly**. So the
translation layer is the only thing standing between this divergence and an invisible no-op.

**Consolidation:** one owner (`dice_engine.degree_from_net`) + thin per-surface adapters where a
genuinely distinct contract exists (#2 documents its own case well and should survive as a named
variant, not a copy). #4/#6/#7/#8 are candidates for deletion-and-delegate.

### B2 · HIGH — 16 sites each independently define "no RNG supplied", and they are not equivalent

The repo is a seeded-simulation corpus, so this is a reproducibility surface. Two incompatible
fallbacks are in use:

```python
engine/autoload/dice_engine.py:68     if rng is None: rng = random.Random()   # fresh, OS-seeded
systems/mass_battle/sim/massbattle.py:631   _r = rng if rng is not None else random   # module global
```

`random.Random()` is **not** affected by `random.seed(42)`; the `random` module is. Measured
directly:

```
random.seed(42) reproducibility of the no-rng-supplied path:
  engine/autoload/dice_engine.roll_pool  -> reproducible: False   sample [2, 1, 0]
  systems/mass_battle/.../roll_pool      -> reproducible: True    sample [-1, 3, -1]
```

*(That is the falsifier for this finding, per §0.1 point 3: if both had printed `True`, the claim is
dead.)*

Related, same root: **5 bare `random.*` module calls** in code that otherwise threads `world.rng`:

| site | note |
|---|---|
| `systems/mass_battle/sim/units.py:299` | `random.randint(1,10)` in `resolve_internal_collisions` — **latent**: `massbattle.py:1206` records it as "implemented but not invoked". A determinism hole pre-baked into code awaiting wiring. |
| `systems/threadwork/sim/co_movement.py:83` | `random.shuffle(cards)` fallback branch |
| `systems/social_contest/sim/contest/resolver.py:137,142,315` | `random.gauss`/`random.uniform` — **deliberate and documented**: the 151 seeded kernel tests rely on the module-level stream, and `scene_dispatch.py:320` reseeds/restores around it. Not a defect; noted so the sweep is complete. |

`massbattle.py` carries a `[BUG FIX 2026-05-20 — non-determinism 03ce9c79]` note recording that this
exact class of bug already bit once. There is no guard preventing recurrence — which is §0.1 point 5's
test (*if you cannot write the guard you have not understood the pattern*).

### B3 · MEDIUM — quantity ownership is split, and `standing` has no owner at all

Write census over `engine/autoload/game_state.py`'s `Faction` dataclass:

- `L`, `Sta`, `W`, `I`, `Mil`, `accord`, `pt` all route through clamped mutators —
  `adjust()` (`:124`, floor 0.5 / ceiling 7.0, divides by `MULTS[stat]`), `adjust_accord()`,
  `adjust_pt()`.
- **`standing: int = 0` (`:114`) has no mutator, no `MULTS` entry, and no bound anywhere in the
  tree.** It is mutated raw at **10 sites**, all in `systems/factions/`:

```
crown_initiative.py:97,115,118,166,176,253,266,269   crown.standing += 1 / -= 1 / += 2 / -= 2
absolution.py:85            church.standing -= 1
parliamentary_transfer.py:311   holder_fac.standing -= 1
```

Meanwhile `systems/social_contest/sim/contest/` has a first-class `Standing` primitive with a
`START` and scale-binding (`resolver.py:207`, `wrapper.py:92`). So the same named concept is a
bounded primitive in one subsystem and an unbounded raw int in another.

Aggregate clamp-at-write rates across the census: `Accord` 4/29, `Mandate` 0/9, `standing` 0/13,
`ci` 3/19, `ms` 4/28, `pt` 1/13. Most of those are constant *definitions* rather than mutations
(the census counts both), so the ratio is not directly a defect rate — but `standing`'s 0/10 on
genuine mutations is.

### B4 · MEDIUM — exact duplicates worth folding

Structural fingerprinting found few exact clones (**5 groups / 7 redundant copies**) — this corpus
duplicates *approaches*, not text. The real ones:

| copies | functions | verdict |
|---|---|---|
| 2 | `factions/sim/mass_seizure.py:120 _church_is_prominent_for_seizure` ≡ `overview/sim/ci_track.py:78 _church_is_prominent` | **Fold.** 18 lines, logically identical, both cite PP-534 Self-Control Rule. Two copies of one canon rule in two lanes. |
| 2 | `combat_engine_v1/workbench/{balance,build_levers}.py _wilson` | Fold into a workbench util. |
| 2 | `overview/sim/ms_track.py:59 apply_ms_baseline_decay` / `:73 apply_ms_delta` | Same file, same shape — parameterise. |
| 2 | `factions/sim/treaty.py:162` / `settlements/sim/registry.py:210` `reset_registry` | Same name, same job, two registries — a shared reset protocol is the fix. |

Also: `reset_all` (3 defs), `get_state` (2), `roll_net` (3), `roll_pool` (2), `resolve` (2),
`main` (2) — same public name, different modules. `roll_pool` is the substantive one:
`massbattle.py:631` re-implements the d10 face rule inline (`f==1: −1; tn≤f≤9: +1; f==10: +2`)
that `dice_engine._die_result` owns. The two currently agree; nothing keeps them agreeing.

---

## 4. Axis C — erroneous work

### C1 · HIGH — `net == 0 → 'Partial'` in `faction_action._degree`

Restated here because it is a *correctness* defect, not only a divergence. See §3.1 #6. It makes the
`elif deg == 'Failure'` arm at `faction_action.py:547` unreachable for a zero net, and it is on the
seasonal campaign path (`faction_take_action`).

### C2 · MEDIUM — `altonian_reinforcements.py` missed the stubwire conversion sweep

OI-17 converted the "Pass 2l armature stub" family from unconditional `raise NotImplementedError` to
the governed `stubwire.stub_resolve` no-op. Every sibling was converted — `ip_track`, `rs_track`,
`restoration_movement`, `npe`, `miraculous_event`, `companion`, `treaty`, `tribunal`,
`home_sanctuary`, `charter_liberties`, `varfell_*`, `infrastructure_reclamation`,
`hafenmark_equipment`, `fieldwork`, `investigation`, `rendering`, `modes`, `dictionaries`,
`wrapper`. **One was not:**

```python
# systems/mass_battle/sim/altonian_reinforcements.py:21
def invoke_altonian_reinforcements(world: GameState):
    raise NotImplementedError("... — Pass 2l armature stub")
```

It therefore **crashes** where its siblings return a typed no-op, and it is invisible to the
`stubs.count` ratchet. Its docstring also cites `sim/autoload/dice_engine` and `sim/peninsular/ip_track`
— both retired paths (`sim/` was retired 2026-07-21).

### C3 · MEDIUM — 94 dead primitives, concentrated in `threadwork` and `settlements`

From `tools/dead_primitive_census.py`: **55 dead functions + 39 dead constants** in `systems/`.

⚠ **The census does not distinguish stubs from dead code, and this correction matters.** 8 of those
55 "dead functions" are `stub_resolve` bodies — `advance_disposition`, `advance_evidence`
(`fieldwork.py:46,54`), `apply_response_matrix`, `evaluate_dialogue_lattice`
(`investigation.py:46,38`), `check_calamity_threshold` (`rendering.py:37`),
`check_phased_occupation_threshold` (`ip_track.py:37`), `check_rm_emergence_trigger`
(`restoration_movement.py:38`), `check_sanctuary_active` (`home_sanctuary.py:37`). These are
**pending work, not cull candidates**, and must not be actioned from the census output.

**Corrected figure: 47 genuinely dead non-stub functions + 39 dead constants.** Anyone working the
census output should apply the same filter — an uncorrected read would propose deleting eight
declared interfaces that the ratchet exists to track. Densest: `threadwork` 22, `settlements` 15,
`factions` 12. `settlements/sim/infrastructure.py` alone
has 10 dead constants — the entire religious-building yield table (`PT_GAIN_CHAPEL`,
`ORDER_GAIN_CHURCH_INSTALL`, `CI_GAIN_TEMPLAR`, `RELIGIOUS_BUILDINGS`, …) is defined and never read.
That is a designed mechanic that was authored and never wired, not a leftover.

### C4 · LOW — three deliberate hooks bypass the stub owner

Stubs are wanted; these are wanted too but are *ungoverned*, so `review_core`'s ratchet cannot see
them:

```
massbattle.py:293 rally_check()      "Empty hook — rally lands in a future cycle (G-7)."   body: pass
massbattle.py:297 reform_check()     "... (G-8)."                                          body: pass
massbattle.py:301 threadwork_check() "... (G-9)."                                          body: pass
```

Routing these through `stubwire.stub_resolve` would put G-7/8/9 on the same tracked surface as every
other pending mechanic, at no behavioural cost. (`units.py:218 halt_before_enemy` is a *disabled*
mechanism — "v11: over-run correction disabled" — not a stub; correctly excluded.)

### C5 · LOW — 138 pyflakes findings, of which the actionable subset is small

Breakdown after inspection: ~95 are unused imports (`tradition.py` alone re-exports 11 names it never
uses; `combat_engine_v1/workbench/*` imports `numpy` in 4 modules that never call it, after the
ED-1085 numpy de-leak). 6 are `f-string is missing placeholders`. 4 are assigned-never-used locals.

The `undefined name 'GameState'` hits (`ip_track.py:29,37`, `rs_track.py:28`,
`restoration_movement.py:30,38`) are **benign at runtime** — all three modules carry
`from __future__ import annotations`, so the annotation is never evaluated. They would break
`typing.get_type_hints()` and any annotation-reading Godot export path, which is the only reason to
fix them.

**12 `except: pass` blocks** (8 in `combat_engine_v1`, 2 in `fieldwork/sim/knots.py`, 1 each in
`contest_legacy_stub.py` and `threadwork/sim/opposing.py`). The two in `knots.py:353,366` wrap
cross-subsystem lazy imports (`characters.sim.conviction`, `threadwork.sim.coherence`) — so a real
import error in either dependency is swallowed and the mechanic silently degrades.

---

## 5. What is *not* wrong

Recorded so the report is not uniformly negative and so the good patterns are protected:

- **All 115 modules import cleanly.** Zero syntax errors, zero import failures.
  (`contest/_kernel_tests.py` calls `sys.exit()` at module scope, which kills any repo-wide
  import-walker — but that is by design: `engine/tests/test_contest_kernel.py:74` runs it as a
  subprocess, and CI runs `pytest engine/tests`. Its 385 assertions do execute.)
- **`ci_module_shape_check` passes** — no unsanctioned container reach-ins in runtime code.
- **Provenance discipline is genuinely strong**: 117 `[canonical: …]` / `PP-` / `ED-` provenance tags
  across the subsystems, and the density is highest exactly where the numbers matter (combat 35,
  social_contest 33).
- **Cross-subsystem coupling is low**: only 12 `systems→systems` import edges outside `engine`, and
  the cross-lane ones (`factions→mass_battle`, `fieldwork→characters`) are lazy in-function by
  deliberate convention.
- **The duplication rate is very low** — 7 redundant copies in 25k LOC. The problem is divergence of
  approach, not copy-paste.

---

## 6. Ranked disposition (all PROPOSED — none executed)

| # | Action | Axis | Cost | Risk |
|---|---|---|---|---|
| 0 | **Rule on the four `net`/`ob` calling conventions before any degree consolidation** | B1a | design | none to decide; blocks 1–2 |
| 1 | Resolve `faction_action`'s one-band shift + the no-effect `s == ob` zone | C1 | 1 line | **behavioural** — moves seasonal outcomes; needs golden re-record + Jordan |
| 1b | Rule on the strategic layer's **d6 ≥ 4** pool vs the canonical d10 engine | B1 | design | large if unified |
| 2 | One owner for degree bands + named adapters; retire #4/#6/#7/#8 | B1 | medium | behavioural for #7 (Ob+3 → 2·Ob) |
| 3 | Single owner for the no-rng fallback + a guard test | B2 | small | none if the chosen default is `random` (matches most sites) |
| 4 | Convert `altonian_reinforcements` to `stubwire`; fix its retired-path citations | C2 | small | none |
| 5 | Route G-7/8/9 hooks through `stubwire` | C4 | small | none |
| 6 | Fold `_church_is_prominent` to one owner | B4 | small | none |
| 7 | Decide `standing`'s bounds + give it an `adjust`-family mutator | B3 | small | needs a canon call on the bound |
| 8 | Disposition the 10 dead `infrastructure.py` constants: wire or cut | C3 | medium | design call |
| 8b | Teach `dead_primitive_census.py` to exclude `stub_resolve` bodies | C3 | small | none — removes 8 false cull candidates |
| 9 | Narrow the 12 `except: pass`, starting with `knots.py:353,366` | C5 | small | none |
| 10 | Strip unused imports / dead numpy | C5 | trivial | none |

**Items 1, 2, 7 and 8 are design calls and are HELD for Jordan** — each changes resolved outcomes or
requires a canon bound that does not exist. Items 3–6, 9, 10 are mechanical and could land as a
routine `[fix]`/`[cleanup]` PR per lane.

---

*Instruments and raw dumps for this audit are reproducible from the method in §0; no generated
artefact is committed beyond this report and its appendix.*
