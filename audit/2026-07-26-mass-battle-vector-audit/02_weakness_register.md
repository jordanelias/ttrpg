# Mass battle — vector audit, all modules / all directions (ED-MB-0043)

**Date:** 2026-07-26 · **Lane:** MB · **Scope:** the mass-battle system across every structural
graph the observatory can build — prose citation, throughline, Μ, patch co-affect, engine
Key-propagation, code import, formula-dependency, pointer, generation-currency, cross-scale ripple,
and engine-vs-prose reconciliation.

## §0 — Validation outcome and confidence framing

`vector_audit` v3 **VALIDATED 2/3** structural properties at both L0 and L1 (the publish gate is
≥2/3). Findings below are therefore publishable **as leads, not verdicts** — the standing framing for
this instrument.

Three scope disclosures, stated up front because each one bounds a whole class of finding:

1. **Corpus layer.** L0 (curated `canonical_sources` slice) and L1 (whole design tree) were both run.
   L1 extends corpus breadth and the **cite graph only** — the throughline/mu/key graphs and the
   token universe are registry-derived and identical at every layer, and the P1/P2/P3 thresholds are
   calibrated on L0 and were **not** re-validated at L1.
2. **The instrument was partly blind when this audit started, and two of its blind spots were fixed
   mid-run** (§1). Every pre-fix number in earlier runs of this apparatus is scoped to a corpus that
   excluded all simulation code.
3. **Agreement between narrow instruments is not triangulation when they share a blind spot.** §3
   documents a finding that three tools independently "confirmed" and that the authoritative graph
   refutes.

---

## §1 — The instrument was blind (found by running it; fixed in this commit)

### F1 — `structure_audit` G_code scanned a deleted tree for five days · **FIXED + guarded**

`CODE_ROOTS = ('sim', 'tools')`. `sim/` was **deleted 2026-07-21** (ED-IN-0071 P4 continuation, the
sim/ hollow-out). From that commit until this one, the observatory's code-architecture layer covered:

| | modules |
|---|---|
| `tools/` | 88 |
| simulation code (engine + every `systems/*/sim/`) | **0** |

Every G_code finding published in that window — import cycles, cut-vertices, orphans — was scoped to
a corpus containing **no engine code at all**, and the register's own prose described the 88 as
"real code modules". Nothing failed, because the failure mode of a dead scan root is an *absent
finding*, which no assertion on the output can observe.

**Fixed:** `CODE_ROOTS = ('engine', 'systems', 'tools')`. Coverage 88 → **248 modules**
(engine 21, systems 111, tools 88, tests/sim/mass_battle 28).

**Guarded:** `test_code_roots_all_exist` asserts on the *configuration* (every root exists on disk),
because the defect is unobservable from results. Mutation-verified: reverting `CODE_ROOTS` to
`('sim','tools')` fails it. Per CLAUDE.md §0.1 #5 this is a pattern defect — correct when written,
broken by a change elsewhere — so it gets one owner and a recurrence guard, not a one-off edit.

### F2 — the obvious fix would have injected 28 false orphans · **FIXED + guarded**

Adding `tests/sim/mass_battle` as a root made its 28 modules visible with **0 resolved edges**: the
package inserts `tests/sim` on `sys.path` and imports itself as top-level `mass_battle.*`, while the
collector names it `tests.sim.mass_battle.*`. Nothing matched, so the entire live engine would have
landed in the orphan list.

**Visible-but-edgeless is strictly worse than unscanned** — it reads as a measured emptiness. Added
`sys_path_aliases()`; internal edges 0 → **66**. Guarded by
`test_sys_path_alias_resolves_live_mass_battle_internal_edges`.

*This is the §0.1 #4 control in practice: the first result was favourable to a conclusion I was
already forming (“the live engine is isolated”), and it was an artifact. The conclusion survived —
but only because it was re-measured, not because it was re-asserted.*

### F3 — `pointer_audit` default sim root was the deleted tree · **FIXED, measured effect nil**

Default was `root/'sim'`; repointed to `root/'systems'`. **The `sim_literals` surface still scores
0/0** — and that is an *honest* zero, not a second blindness: A17's scanner matches literal
`stat_deltas={...}`/`impact_vector={...}` dict keys, and the one live call site passes variables
(`stat_deltas={er.affected_stat: er.delta}`), as its own docstring already documents. Reported
because a fix with no measured effect must be labelled as such.

### F4 — the same dead root persists in five more places · **FILED, not fixed**

Out of scope for an MB audit (CLAUDE.md §0.1 #5: sweep what the task is load-bearing on, file the
rest), but each is the same class:

| Site | Consequence |
|---|---|
| `tools/ci_quantity_vocabulary_check.py:145` — `--sim-root` default `<repo>/sim` | **A CI gate** scanning a deleted directory. `review_core` currently reports `[fail] vocab.a17 29/29` — all 29 from the contract surface; the sim surface contributes nothing. |
| `registers/mechanics_index.yaml` | 11 distinct dead `sim_module:` paths across 19 entries |
| `tools/audit_staleness.py:69` | `sim/` in `scope_prefixes` — staleness never triggers on sim changes |
| `tools/observability/build_decisions.py:57`, `tools/workplan_status.py:71`, `tools/build_apparatus_registry.py:169` | dead `sim` sweep dir / prefix |
| `tests/sim/mass_battle/test_persubunit_stress.py:17` | inserts `<repo>/sim` on `sys.path` |

---

## §2 — The mass-battle system is two disjoint code graphs

Measured on the repaired G_code (F1+F2), so these numbers are the first correct ones.

| | `tests/sim/mass_battle/` | `systems/mass_battle/sim/` |
|---|---|---|
| modules | 28 | 6 |
| LOC | ~10,503 | ~2,382 |
| internal import edges | 66 | 3 |
| **external importers (production code)** | **NONE** | `systems.factions.sim.faction_action` |
| **imports from `engine/` or `systems/`** | **NONE** | — |
| commits since the other tree last moved | **10** | 0 |
| wired into `faction_action` | no | **yes** (`faction_action.py:349`) |

The tree carrying all current development has **zero production importers** and shares **no code**
with the engine core — not the Key substrate, not the autoload registry, not a single engine
primitive. It is reachable only from `tests/valoria/` (35 test modules) and `audit/…-stress-test/`
probes. The tree that *is* wired into the campaign has not been touched in 10 MB commits.

`engine/sim_reference_README.md` already flags this (ED-IN-0074 D5: "reconcile the two before
porting the mass-battle slice"). This audit adds the measurement and one consequence not previously
stated: **the live engine imports nothing from `engine/`**, so "reconciling the two" is not a merge
of two variants of the same code — there is no shared substrate to merge onto.

Compounding hazard: `tests/sim/README.md` declares that whole tree "frozen historical sim-run
output… not a place to add new sim code". Every code-layer instrument is configured to skip
`tests/`. The most actively developed engine in the repo sits where the tooling is told not to look
and the documentation says nothing lives.

**F5 sub-finding — import cycle + double cut-vertex in the wired tree.**
`systems.mass_battle.sim.massbattle ↔ systems.mass_battle.sim.units` is one of only 3 import cycles
in the repo, and *both* members are code cut-vertices.

---

## §3 — `scene_outcome.battle_concluded`: a correction, not a confirmation

Three instruments independently flagged it:

- `structure_audit` L2 → **dangling emit**, "no consumer" (canon-grade)
- `vector_audit` Mode E → sparse-context, 0 paragraphs, cite-degree 0; Mode H → **isolate**, degree 0 in all four graphs, status canonical
- `workbench` → card `wb-00aeffeb7f`, unspecced wiring, prose silent
- and `tools/observability/INCOMPLETENESS.md:146` already carries it as a live finding, with the
  mechanism explicitly unresolved ("check the register for the mechanism")

**All four are wrong about what it is, and they agree because they share a blind spot** — each reads
`module_contracts.yaml` without resolving against the Key Type Registry. The authoritative engine
graph (`tools/observability/build_graph.py`, which SKILL.md names as authoritative over
`vector_audit`'s narrower `build_g_key`) resolves it:

```
registered Keys matching /battle/  →  ['scene.battle_concluded']   ← one Key, not two
scene.battle_concluded : family=scene_outcome
                         emitters=[mass_battle]
                         consumers=[articulation_layer, faction_state, npc_behavior, piety_track]
```

`scene_outcome.battle_concluded` **is not a Key.** It is the *family name* of
`scene.battle_concluded`, entered a second time into `mass_battle`'s `emits:` list alongside the
real type. This is the ED-MB-0010 fabricated-emit class, still live and still unrecorded as such.

**Mechanism now identified** — this is the answer the Incompleteness Ledger row is asking for.
**Recommendation:** delete the `scene_outcome.battle_concluded` row from `references/module_contracts.yaml`
`mass_battle.emits`. One-line change; resolves one dangling emit, one Mode-E row, one Mode-H isolate,
one workbench card, and one ledger row simultaneously — because they are one defect counted five times.

**Not a defect (checked and cleared):** the narrow graphs list 3 consumers, the authoritative one
lists 4. The extra is `articulation_layer`, whose contract consumes `{type: "*", from: engine}` — a
wildcard that `build_l2()` documents itself as skipping. Correct behaviour of a disclosed
strict-subset measure, not an under-declared contract.

---

## §4 — The contract declares a battle engine with no inputs and no state

```yaml
mass_battle:
  consumes: []          # ← nothing
  state:    []          # ← nothing
  resolver: dice_pool
```

`ripple_audit`, run in **all directions across all four edge layers**
(`emits_consumes, derives, produces, reads`):

```
## downstream — a change to 'mass_battle' affects (5)
## upstream   — 'mass_battle' is built from (0)
```

Zero upstream in every layer. `mass_battle` is a pure source: the typed wiring says a battle takes no
inputs — not army composition, not terrain, not morale, not commander — and persists nothing.

Consequences that follow mechanically:

- **`formula_audit` and `pointer_audit` return zero MB rows.** Not filtered out — MB contributes no
  quantities to the dependency DAG and no identifiers to G_pointer, because `state`/`derivations` are
  empty. The entire value-scale tier of the observatory is structurally blind to mass battle, and
  will stay blind no matter how many times it is run.
- **262 UPPER-case constants** across the live engine; **40 (15%)** appear anywhere in
  `engine/params/` or `systems/mass_battle/*.md`. The remaining 222 have no prose surface at all.
- `resolver: dice_pool` describes the *design doc's* model, not the engine's (§5).

This is the single highest-value MB finding for the Godot port: §5/§6 of CLAUDE.md require every
number crossing into Godot to resolve through a contract, and mass battle's contract is empty.

---

## §5 — Design, params, and engine describe three different games

| Surface | Model |
|---|---|
| `systems/mass_battle/mass_battle_v30.md` | 7-phase turn; `Pool = min(Size,Command) + Command`; d10 vs TN; simultaneous damage |
| `engine/params/mass_combat.md` | same 7-phase structure; `last_updated: 2026-04-03`; header cites `designs/mass_combat/mass_battle_v30.md` — **a path that has never existed** (`designs/` is retired, and it was `designs/provincial/`) |
| `tests/sim/mass_battle/` (live) | continuous tick loop (`TICKS_PER_PHASE`); per-cell morale lattice with 8-neighbourhood break contagion; octagon facing as a damage-received multiplier (front 1.0× / flank 1.5× / rear 2.0×); Lanchester frontage exponents; stochastic rout break-points |

The engine's own code acknowledges the gap in-band — `orchestration.py:1663` carries
`# [canonical: mass_battle_v30.md §A.7 — 18-tick battle (3 phases x 6)]`, reconciling a *tick count*
to a doc that specifies *phases of dice rolls*.

`workbench` scores mass_battle at **0/4 engine edges co-mentioned in prose** — the lowest possible
responsiveness. Four open divergence cards, all `unspecced_wiring`, none resolved.

---

## §6 — Token-graph results (the quantized layer)

**Mode A — hubs.** `Mass Battle` and `Mass Combat` are both top-quintile in 3/4 graphs:

| token | cite | tl | mu | pp | scale (ripple) |
|---|---|---|---|---|---|
| Mass Battle | 147 | 8 | **0** | **0** | mechanic |
| Mass Combat | 147 | 9 | **23** | **0** | **province** |

**F6 — the two alias tokens diverge on their own metadata.** Same subsystem, and the impact query
returns an *identical* blast radius and the identical single surprising path for both — yet they
carry different Μ-degree (0 vs 23) and are classified at different **scales** (mechanic vs
province). One of those classifications is wrong and nothing reconciles them.

**F7 — `pp = 0` for both.** No patch in `patch_register_active.yaml` lists either token in its
`affects:` — the register contains zero case-insensitive matches for the subsystem at all. The most heavily-revised subsystem in the repo (43 ledger entries, 10 commits this
month) has **zero patch-register co-affect edges**. Mass-battle work is being recorded in the MB
editorial ledger and bypassing the patch register entirely.

**Mode B — implied-but-missing.** `Faction Layer ↔ Mass Combat`: 2 metadata graphs link them, **0
citations**. The one cross-subsystem edge that is actually wired in code
(`faction_action.py:349 → resolve_mass_battle`) is the edge the prose never states.

**Mode D — cascade sinks.** 612 chains terminate at each of Mass Battle / Mass Combat. Per this
mode's own disclosure these are **unverified leads** on a dense corpus, not confirmed gaps.

**F8 — the impact query saturates.** `--impact "Mass Battle"` reaches **268 of 275 tokens** with
exactly **1** flagged surprising. At this cite density undirected reachability cannot discriminate
— "everything is reachable from everything" is the honest reading, and the single surviving path
(`Mass Battle → Threadwork → Faction Succession Split → Fractional Province`) should be treated as a
threshold artifact, not a discovery. Reporting the instrument's non-result rather than dressing it
up.

**Instrument limitation observed:** `ripple_audit`'s node namespace holds modules and quantities but
**not Keys** — `--node "scene.battle_concluded"` returns `unknown node`. Keys exist only as edge
labels, so a Key cannot be the subject of a ripple query.

---

## §7 — Doc hygiene and currency

**F9 — 3 of 6 MB design docs carry no `## Status:` line**, so their currency cannot be resolved by
the method CLAUDE.md §4 mandates (`CURRENT.md` + the `## Status:` line — never the filename):
`mass_battle_v30_index.md`, `military_layer_v30.md`, `military_layer_v30_index.md`. `gen_audit`
independently flags two of the three as `no_status`.

**F10 — the canonical head is `WORKING DESIGN`, not `CANONICAL`.**
`mass_battle_v30.md` — the doc `CURRENT.md` names as the Mass battle head and that
`module_contracts.yaml` points `doc:` at — is marked `WORKING DESIGN`, while the *integration* doc
beside it is `CANONICAL`. The port's spec surface is the non-canonical one.

**F11 — `canonical_sha__*` pins are advisory only** (CLAUDE.md §1): the 6 MB pins in
`canonical_sources.yaml` are not verified against the working tree by any live tool. Not treated as
an integrity signal here.

**F12 — 21 of 43 MB ledger entries carry `needs_jordan`**, including the ED-MB-0039 envelopment fork
and the ED-MB-0041 adversarial-audit Tier-3 calls. Nearly half the lane's recorded state is blocked
on one person.

---

## §8 — Disposition table (forward-only discipline)

| # | Finding | Disposition |
|---|---|---|
| F1 | G_code scanned deleted `sim/` — 0 sim modules for 5 days | **FIXED + guarded** this commit (ED-MB-0043) |
| F2 | `sys.path` alias — 28 false orphans latent in the fix | **FIXED + guarded** this commit |
| F3 | `pointer_audit` dead sim root | **FIXED** this commit; measured effect nil, honest zero |
| F4 | Same dead root in A17 (CI gate), mechanics_index ×11, +4 tools | **FILED** → new `ED-IN` item; out of MB lane scope |
| F5 | Two disjoint MB code graphs; live tree has 0 production importers, 0 engine imports | **FILED** → extends ED-IN-0074 D5 with measurement; port-blocking |
| — | massbattle ↔ units import cycle, both cut-vertices | **FILED** under F5 |
| F–§3 | `scene_outcome.battle_concluded` is a family name, not a Key | **ACTIONABLE, 1 line** — delete the row from `module_contracts.yaml`; held for MB-lane sign-off rather than bundled into a tooling PR |
| F–§4 | `consumes: []`, `state: []` — contract declares no inputs, no state | **FILED, needs_jordan** — highest-value port blocker; 222/262 constants have no prose surface |
| F–§5 | Design / params / engine are three different models; params header cites a never-existent path | **FILED** — 4 open workbench cards, responsiveness 0/4 |
| F6 | Mass Battle vs Mass Combat: divergent mu-degree and scale class | **FILED** — vocabulary debt, one classification is wrong |
| F7 | `pp = 0` — MB work bypasses the patch register entirely | **FILED** |
| F8 | Impact query saturates (268/275); Mode-D 612 sinks | **NO ACTION** — instrument non-result, reported as such |
| — | ripple has no Key nodes | **NO ACTION** — documented limitation |
| F9/F10 | 3 docs without `## Status:`; head is `WORKING DESIGN` | **FILED** — blocks §4 currency resolution |
| F11 | SHA pins advisory | **NO ACTION** — known, CLAUDE.md §1 |
| F12 | 21/43 MB EDs need_jordan | **NO ACTION** — visibility only |

## §9 — What this audit could not see

Stated per the instrument's standing disclosure, and extended by what this run learned:

- **Behaviour.** These graphs see design/registry/import *structure*. A wrong number, a mis-tuned
  formula, a broken simulation is invisible. The 2026-07-22 stress-test corpus and the MB ledger are
  where behavioural defects live.
- **Contract↔code correspondence remains UNVERIFIED** (`structure_audit`'s own disclosed
  black-hole): the join is not name-based — 6/27 modules map by name; `mass_battle` ↔ `massbattle` is
  precisely one of the misses. Nothing in this run verified that the contract describes the code.
- **P1/P2/P3 were not re-validated at L1**; L1 numbers reuse L0-calibrated thresholds.
- **Everything `tests/` still hides.** F1's fix allowlisted exactly one path
  (`tests/sim/mass_battle`). Any other live code under `tests/` remains outside G_code, unmeasured
  and unenumerated by this audit.
