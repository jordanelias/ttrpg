# 13 — Handoff: build order, impact classes, controls, and what not to do

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · every document `01`–`12` · `audit/2026-08-08-world-churn-audit/03_causal_model.md`
## · `engine/substrate/keys.py` · `engine/autoload/game_state.py` · `systems/_architecture/key_type_registry_v30.md`

This document is the only one in the suite that is **about the other twelve**. It carries no
mechanism of its own. If a rule appears here that appears nowhere else, that is a defect in this
page, not a thirteenth system.

## Overrides

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **O-13.1** | v1 `10`'s build order, which sequenced by **document number** | this suite's own v1 | ordering by document number is ordering by authorship convenience. The order below is dependency-derived and, where the tree has already adjudicated one, adopts it |
| **O-13.2** | the assumption — mine, in the delta spec — that this suite's build order is **greenfield** | this spec's own framing | it is not. `audit/2026-08-08-world-churn-audit/03_causal_model.md` §1 already adjudicated a build order across five competing lenses, and §2 establishes an ordering *hazard* that is a property of the engine and binds whatever the design says. §2 below adopts both |

---

## 1. The finding that reframes this handoff

**The causal model is not missing. It is declared and unemitted.**

`03_causal_model.md` §0 measures the corpus's own propagation graph at **46 nodes, 139 edges**. Of
the 94 module-to-module `emits_consumes` edges, **43 are flagged `notional` by the tool that built
the graph**, and **only 7 of 94 are carried by a Key type with any live emitter**. Two independent
instruments agree: `wiring_map_check --summary` reports **`live: 2` of 27 modules**, and
`trace_execution_phases --seed 42 --seasons 40` shows **no npcs, characters, fieldwork, threadwork or
combat calls at all across forty seasons**.

**This suite is therefore not building a world from nothing. It is specifying what should be emitted
on edges the corpus already committed to.** Two consequences bind every phase below:

1. **A declared edge with no rule content is decoration.** `01`'s W-6 already forbids declaring a
   `consumes:` row with no rule behind it. This page extends that to the build: **a phase is not done
   when its contracts are declared. It is done when something executes** (`CLAUDE.md` §0.2).
2. **Prefer wiring an existing declared edge to minting a new one.** `09`'s author demonstrated the
   payoff: three of the four project Key types he needed **already existed** under ED-935, and only
   formation was missing. `00 §9.2`'s table was wrong about its own cost. Check the registry before
   proposing a type.

---

## 2. The ordering hazard, which is not ours to argue with

`03_causal_model.md` §2: **casualty writeback before the fiscal edge is actively destabilizing.**
Losers cannot rebuild, the mil-advantage multiplier steers the stronger side toward more conquest, and
the canonical occupier damper dies in a clamp. **Build writeback first and the sim degenerates to
first-mover extermination.**

⚠ **One of that audit's two supporting facts is now stale, and the conclusion survives by a different
route.** It argued *"`Faction.adjust` floors at 0.5, so a depleted faction musters for free."* Verified
2026-08-29: `engine/autoload/game_state.py:153-180` now reads per-stat bounds from the registry, and two
Jordan rulings of **2026-08-23** — *"Legitimacy is a base"* and *"Influence can be 0"* — leave **all six
declared stats flooring at 0**. `UNDECLARED_FLOOR = 0.5` survives only as the fallback for undeclared
stats.

**The hazard is real anyway, and the correct statement is stronger:** the muster pool is
`faction.Mil + math.floor(faction.W / 2)` (`systems/factions/sim/faction_action.py:549`, tagged
`[canonical: ED-FA-0009 (FA-2)]`). At `W = 0` a faction still musters on `Mil` alone. **Wealth is a
discount on muster, never a gate.** So the dependency the audit named holds; the sentence to carry
forward is *"Wealth gates nothing"*, not *"the clamp floors at 0.5"*.

**Anyone re-deriving this ordering from the audit's own wording will assert a false fact about the
engine.** That is the general lesson of this section: **an audit's ENGINE claims rot at the speed of
the engine.** Re-verify every one before citing it.

---

## 3. Impact classes

Every item below carries one. The class says what shipping it *does*, and it is the honest answer to
"is this done?"

| class | means | how it is checked |
|---|---|---|
| **DOC** | a document changed; no executable behaviour moved | a diff. **Never counts as a juncture being done** (`CLAUDE.md` §0.2) |
| **INERT** | code or a registry row landed, and nothing calls it | an import succeeds; no caller exists. Honest, and a real step — but say it |
| **MOVES** | observable behaviour changed | a seeded run differs, or a golden moves, or a new test fails without the change and passes with it |
| **RULING** | blocked on a human decision | named in `00 §5`, with what each branch costs |

⚠ **DOC is the default failure mode of this repository and of this suite.** Thirteen documents is
thirteen DOC items. **Nothing in this suite has moved a single byte of executable behaviour**, and
this page exists partly to say that plainly rather than let a completed suite read as progress.

---

## 4. Preconditions — what is blocked on what

| # | Precondition | Blocks | Class | State |
|---|---|---|---|---|
| **P0-1** | **`references/rendering_dispositions.yaml` must exist.** `key_type_registry_v30.md` §10 ratified it as a precondition on appending **any** new Key type | every new key type in `00 §9.2` | INERT once built | **open**. The gate is report-only today because the file it reads does not exist, which is why the precondition can be violated silently |
| **P0-2** | **`state.project_formed`** must be registered (G-29, `audit/2026-08-11-world-schema-gap-audit/01_gap_register_part2.md:281`) | `09 am.declare` | INERT | **open, and it is now the ONLY project type needed** — the other three are registered under ED-935 |
| **P0-3** | **`presence.<institution>` must declare floor and ceiling**, `≤ 12` at `05`'s current modifier bound | `05 act.contest_influence` passing `01 §6.1` | DOC | **CLOSED 2026-08-29.** `07 §4.1a` declares **floor 0, ceiling 7** — canon's own stat family, pool-commensurate by construction at `ceiling/2 = 3.5`, against the 12.49 its site admits. **The ~2× headroom is deliberate**: it anticipates P0-4's stricter opposed-site form so the choice will not need revisiting when that lands. Load-time check **L-7** |
| **P0-4** | **`01 §6.1` must carry the opposed-site (differential) envelope**, not only the one-sided one | every DO/BI site's gate verdict | DOC | **open**. Checking an opposed site one-sidedly is a **false pass** — the gate's own failure class |
| **P0-5** | `engine/engine_params/descriptors.json` declares **`prac.thread_sensitivity` with `ceiling: None`** against canon's 0–100 hard cap | three declaration-time guards are silently inert on it | MOVES when fixed | **open, FI/IN lane's row.** Verified 2026-08-29 |
| **P0-6** | the two new registries — `references/form_registry.yaml`, `references/content_registry.yaml` — plus their exporters and blocking `--check` | every form transition; every content row | INERT | **open** |

**Nothing appends a Key type until P0-1 exists.** Appending while a ratified precondition is
unexecuted is exactly the drift the precondition was ratified to stop.

---

## 5. The build order

Phases are dependency-ordered. **Within a phase, items are independent.** Each names its class and
the control that would show it wrong.

### Phase 0 — make the gates real (INERT, and cheap)

| item | why first | control |
|---|---|---|
| P0-6's two registries + exporters with blocking `--check` | every later phase writes rows into them; building them late means hand-editing what a generator should own | the round-trip `--check` fails on a hand-edit |
| `01 §6.1`'s commensurability gate as a **declaration-time** check, carrying **both** envelopes (P0-4) | it is the only guard in the suite that prevents a **dead mechanic that looks live** | a synthetic row targeting Thread Sensitivity (0–100) is **rejected**; one targeting a 0–7 stat **passes** |
| `references/rendering_dispositions.yaml` (P0-1) | unblocks every key type | the registry gate stops being report-only |

**Phase 0 ships no behaviour and is still the right first phase**, because every item is a guard that
makes a later phase's defect impossible rather than expensive. Each earns its existence under
`CLAUDE.md` §0.1 point 5's predicate: all three are load-bearing on **the game** (the exported params
and the engine's own resolution), not on this repository's process.

### Phase 1 — the substrate (MOVES)

`01`'s four primitives, the form bucket, the four write leaves, `derive_ob`, the disclosure block.

**This is the phase that must not be skipped or fused with Phase 2.** Everything in `02`–`12` is a
composition of this page; if the primitives land alongside their first consumer, the consumer's needs
will bend them, and the suite's one architectural claim — *four stored kinds, four write leaves* —
stops being checkable.

| control | |
|---|---|
| the write-leaf sweep | a test in the shape of `tests/valoria/test_morale_write_sweep.py`, whose `_CELL_OWNED` registry is field-parameterised so each newly-owned field inherits the guard by adding one key. **This is the single most valuable guard in the whole plan** — it is the one that catches the read/write asymmetry class (`CLAUDE.md` §0.1 point 1) |
| AU-1 | no state name declared `writable: false` appears as a gauge id in `references/descriptor_registry.yaml` (`00 §7.1`) |
| hysteresis | every reversible form pair declares a band ≥ `H_MIN`; a seeded run shows no transition oscillating on a boundary |
| the gauge fixed point | `rest + a/λ` computed at load for every declared gauge; a gauge whose fixed point exceeds its ceiling is rejected **at load, not in a playtest** |

### Phase 2 — the fiscal edge (MOVES) — adopted from the adjudicated order

`03_causal_model.md` §1 ranks this first among *behaviour* edges on all three of its criteria, and §2
makes it a hard predecessor of anything that destroys force. **This suite does not re-adjudicate it.**

Concretely: `realized_income(s) = Prosperity × stance × compliance(q)`, the L/PS consume step, and the
`accrual.entitlement` channel `05 fa.muster` reads.

| control | |
|---|---|
| the control arm | `tools/balance_oracle.py` (240 campaigns, ~13 min, deliberately not a CI gate). **This is campaign-reachable, so both arms are genuinely different** — unlike a campaign-unreachable change, where running it would be a fake control (ED-MB-0066 is the worked example) |
| the falsifier | a seeded campaign in which a faction at `W = 0` musters at the same rate as one at `W = 8`. If it does, the fiscal edge is not connected |

### Phase 3 — people and posts (MOVES)

`03` population, `02` generation, `04` personnel. In that order: population bounds what generation
may produce, and generation supplies what personnel appoints.

| control | |
|---|---|
| the bound | the population count is a pure function of posts and places, checkable at load. A seeded 50-season run ends with the same bound it started under |
| no time-driven growth | `03` rejected in-play birth on exactly this ground; the falsifier is a run in which population rises with no post or place having changed |
| the caste gate | `04`'s matrix is `(institution, post_kind, caste)`. The falsifier is a candidate set that differs between two institutions at the same `post_kind` — if it never does, the key is too coarse and the Warden asymmetry has been erased |

### Phase 4 — places, then their management (MOVES)

`07` then `08`. `07` owns the object and its form transitions; `08` owns the one player verb.

| control | |
|---|---|
| the node graph never moves | the count of `place` entities and the `nodes:` list of `form_registry.yaml` are **identical before and after any seeded campaign**, regardless of how many `place_found` / `place_ruin` transitions fired. This is what makes `07`'s override of the fixed-35 rule safe |
| growth is reachable both ways | a seeded run contains at least one growth and at least one decay transition. A ladder that only ever climbs is not a ladder |

### Phase 5 — factions (MOVES)

`06` being, then `05` acting. Being before acting: `05`'s `appeal` reads `06`'s ethos and practice.

| control | |
|---|---|
| divergence is derived | no `divergence` value is ever written; the falsifier is a grep for an assignment |
| **the bloc gate** | **`06`'s author names this the one thing in his document worth a campaign measurement, and this plan agrees.** Three untuned thresholds at once, no canon precedent, and a loud degenerate failure: a `θ_coherence` set too loose makes "the bloc" just *everyone who disagrees* — an object with no position. Reachability bar: **≥2 distinct components at maximum divergence, none at low.** **If there is budget for exactly one campaign measurement out of this suite, spend it here** |
| collapse has an end | a seeded run in which a faction reaches the dissolution gate and dissolves. v1's dead end was an immortal seat node guaranteeing the *demand*; `06`'s C-4 keeps recoverability and removes the dead end |

### Phase 6 — projects, events, and the Slate (MOVES)

`09`, `11`, then `10`. The Slate last: it ranks candidates, so it needs producers to exist.

| control | |
|---|---|
| **surfacing does not change outcomes** | `10`'s three invariance properties — fidelity-neutrality, baseline parity, order-neutrality — carried by one snapshot plus commutative effects plus a **per-candidate RNG substream**. A shared sequential stream would let attending one item silently re-roll every later one, which nothing would catch in play. **This is the load-bearing property of the entire change: if surfacing changes outcomes, the filter is a cheat** |
| the truncation bound | bounded and monotone, proved in `10`; the monotonicity turns on the exempt set being a **count cap**, not a score threshold |
| obstruction is real | `09`'s own weakest claim, and its falsifier is the right one: **a seeded campaign in which a project's progress falls after an unrelated actor's action, with no module having named the project.** If that never happens, every project is a timer with extra steps |
| event rows are reachable | for each row, a world state that fires it; and each row's effects perceivable through at least one of `10`'s five witness channels. **A row failing either direction is dead content and should be cut, not shipped** |
| `place_found` is not dormant | a seeded campaign in which a `found_settlement` project fires and `place_found` follows |

### Phase 7 — the seams (MOVES, and the smallest phase)

`12`. Units, treaty-as-edge, the deliberative body, terrain.

⚠ **Terrain into the force model cannot be built yet, and `12` says so.** Verified 2026-08-29:
**nothing in production constructs `ctx['factions']`** — the only writers are
`engine/tests/test_pipeline_reach.py:277,756` and `engine/tests/test_combat_bridge_seam.py:44`, all
hardcoding `("Crown","Church")`. Further, **no live trigger queues a `combat`-type scene at all**:
`evaluate_triggers` (`engine/cross_scale/scene_dispatch.py:77-101`) only ever fires `"contest"`, and
the single `queue_scene` call site passes only that. The whole `derive_parties` path is unreached from
the season loop, independent of the default-OFF flag.

**So `12 §3` is a design for a caller that does not exist.** That is a legitimate thing to ship as a
specification and an illegitimate thing to describe as connected. Do not widen `PATH_SEAM_ALLOWED` to
make it look connected; `12` priced that option and rejected it.

---

## 6. Guards, and the predicate each must survive

`CLAUDE.md` §0.1 point 5, as amended 2026-08-19: **a pattern defect earns a guard only if the
defective artifact is load-bearing on the game or on a Jordan decision.** A pattern defect in an
artifact load-bearing only on this repository's process is evidence **the artifact can be wrong
without cost** — delete it, or accept the defect and write nothing.

| guard | load-bearing on | verdict |
|---|---|---|
| the write-leaf sweep (Phase 1) | the engine's own state | **earns it** |
| the commensurability gate (Phase 0) | whether a mechanic resolves at all | **earns it** |
| the gauge fixed-point check at load | the engine's numbers | **earns it** |
| the registries' round-trip `--check` | the exports the Godot port ingests | **earns it** |
| the node-graph invariance test (Phase 4) | the adjacency graph the battle surface stands on | **earns it** |
| a guard that the thirteen documents stay cross-referenced | **this suite's own prose** | **FORBIDDEN.** Write nothing. If the cross-references rot, that costs a reader one grep |
| a guard on the `## Overrides` blocks' completeness | this repository's process | **FORBIDDEN**, same reason |

**The last two rows are the point of this section.** A suite that has just produced thirteen
documents is under maximum temptation to guard its documents. Every such guard would be apparatus,
and apparatus is what `§0.3` measured this repository generating at a 5.2:1 and then 10.8:1 ratio
against content.

---

## 7. Open rulings that gate work rather than describe it

Full list in `00 §5`. The four that actually block a phase:

| # | question | blocks |
|---|---|---|
| **J-N** | does the substrate get cross-season latency at all? Today it has none — `drain_tick` has **zero production callers**, `next_tick` **raises** on a non-empty queue, `DEFAULT_CASCADE_DEPTH_MAX = 0` | nothing in this suite, and that is deliberate: `09` and `11` verified independently that they need no latency and are **not blocked**. It blocks any *future* design that assumes a posted effect lands later |
| **J-O** | does the Key substrate deserve promotion from telemetry spine to churn engine at all? The alternative — Keys as an append-only causality log, churn driven at the boundary — *is never weighed anywhere* | identifies what to revisit if it rules the other way. `09` reports all four of its modules have empty `consumes:`, so that page is close to robust either direction |
| **the fourth rung** | canon says geography's *territory* **is** the province-tier node (`systems/settlements/settlement_layer_v30.md:151`), so canon has three rungs where the brief asked for four | `05`/`06` shipped three and made the mechanism rung-count-agnostic, so a fourth is **a registry row and zero design change**. Needs a ruling only if a distinct provincial overlay is wanted |
| **the seventh Tag kind** | `09` needs `Ambition`; `01 §3.1` closed the enum at six | `09 am.declare`. It is **not** a fifth stored kind — zero new gauges, entity kinds or registry files — but it overrides `01`'s closing sentence and Jordan should see it |

---

## 8. What not to do

Each of these was either attempted and caught in this suite, or is a failure the tree has already
paid for.

1. **Do not mark a juncture done on a document.** `CLAUDE.md` §0.2. Thirteen documents is thirteen
   DOC items and zero moved bytes.
2. **Do not propose a Key type without checking the registry.** `00 §9.2` proposed three that already
   existed. Cost of checking: one grep.
3. **Do not store an aggregate.** Every derived value in this suite — divergence, lineage, NPC↔NPC
   disposition, project progress, footing — is recomputed at read. v1 stored two of them and both
   were defects.
4. **Do not restate a shared check in a second document.** `05` found the commensurability hazard and
   still got its arithmetic wrong; so did I. The check lives at `derive_ob`'s single owner **because**
   two competent passes got it wrong independently.
5. **Do not special-case an entity or an outcome.** Scripting drift. Ethos is a weight on an option
   set every faction shares, never a bespoke branch for one faction.
6. **Do not add a second scoring function beside the Light Function.** Two mechanisms doing one job is
   the elegance failure, whichever one you wrote.
7. **Do not restore a SessionStart banner** (`CLAUDE.md` §0.3), **and do not self-schedule** (§11).
8. **Do not widen `PATH_SEAM_ALLOWED`** to make an unreached seam look connected.
9. **Do not let a cut remove an outcome silently.** Every cut in this suite names what now produces
   that outcome instead — `08`'s twelve verbs became one player verb plus substrate that runs whether
   attended or not. **A cut that moves an outcome under the hood is the win; a cut that deletes one is
   a loss and must be argued as such.**

---

## 9. Property audit

| claim this page makes | falsifier |
|---|---|
| the build order is dependency-correct | a phase whose control passes only because a later phase's code is present. Run each phase's control at that phase's head |
| Phase 2 precedes force destruction | a seeded campaign with casualty writeback and no fiscal edge that does **not** degenerate to first-mover extermination. If it doesn't, §2's hazard is overstated and the order can relax |
| every phase's control can fail | **each control must be shown to fail on a deliberately broken build before it is trusted.** A control that has never been red is not evidence (`CLAUDE.md` §0.1 point 2) |
| no guard here is apparatus-only | §6's table. A new guard whose subject is this suite's prose violates it |
| the suite is DOC-class today | `git log --stat` over `engine/` and `systems/` for this branch: **zero executable lines changed**. True as of this commit, and this row exists so that stops being true before anyone calls the suite done |

**The single weakest claim on this page:** that the phase boundaries are the *right* seams. They are
derived from the documents' declared dependencies, and those declarations were written by thirteen
authors who could not see each other's work. Two seams are load-bearing and were checked
(substrate-before-consumers, fiscal-before-writeback); the rest are plausible and unmeasured, and
Phase 3's internal order — population, then generation, then personnel — is the one I would expect to
move first on contact.
