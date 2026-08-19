# Execution Plan — the fifteen rulings of 2026-08-18

## Status: PLAN — derived from RULED decisions, not itself a design proposal. Nothing here re-opens a ruling. No `.py` touched by this document; every claim carries file:line and is marked MEASURED or JUDGMENT.

**Date:** 2026-08-18 · **Lane:** FI (with named IN / PC / SC / FA / SE dependencies) · **IDs:** none allocated
**Sources:** `proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md` §13 (Q1–Q9) · `proposals/2026-08-18-epistemic-propositions-and-provenance.md` §10 (P1–P5)
**Method:** a read-only trace produced the census and the dependency reasoning; the four highest-leverage claims were then re-verified independently before being written here (§9).

---

## §1 THE FIVE BLOCKERS — what cannot start, and whose call each is

Nothing below is a rediscovered question. Each is a **new** blocker created or exposed *by* the rulings.

| # | Blocker | Blocks | Owner |
|---|---|---|---|
| **B1** | **The content-address hashing rule is unspecified.** If two agents hash the same claim differently, comparison, contradiction and corroboration all fail *silently*. | All implementation of P1/P2/P3 (Holdings), the Case Board, and — transitively — R6's generation-time condition tables | Jordan / IN |
| **B2** | **The faction-stat roster is unruled** (`HANDOFF.md:130-160`): declared 5 vs coded 6, Mandate-as-L, and Influence on 1–7 while every other stat is 0–7. HANDOFF states the consequence directly: *"the faction stat roster **is** the faction obstacle surface."* A 0–7 stat yields obstacles 0–3.5; the 1–7 inconsistency decides whether a faction can present a **zero** obstacle. | Every faction-side R1 site — tribunal, parliamentary transfer, and the four ambiguous faction obstacles | Jordan / FA |
| **B3** | **The opposed-roll class is unruled — and this is the one I most want ruled.** See §3.3. | R1 for personal combat strikes and every mass-battle engagement | Jordan |
| **B4** | **R2's divergence test has not been run** (the condition attached to the Q2 ruling). | Any fieldwork or Lattice **pool** authored with claimed numbers | FI — executable analysis, should run early |
| **B5** | **R10's spawn-default and forgetting rules are unruled**, and the NPE's generation policy does not exist. | *Seeding* population-scale Holdings (schema can proceed without it) | Jordan / FI |

---

## §2 THE EXECUTION SEQUENCE

Dependency-ordered. Each step names its edit sites, its gate (how we know it's done) and its guard (what fails on recurrence). Steps 1–5 are executable **today**.

| # | Step | Depends on | Gate |
|---|---|---|---|
| **1** | **R7 doc strikes** — two sites, §5.1 | — | P-06 canon test passes; no Coherence-on-threadcut phrasing survives |
| **2** | **R8 doc strikes** — nine sites, §5.2 | — | no `−1D`/`+1 Ob` wound phrasing outside the frozen historical docs |
| **3** | **R8 code change** — `combat.py:52` — **held separate, see §5.3** | 2 | campaign goldens re-recorded *with cause*, delta reported before tuning |
| **4** | **R1 doctrine homing** — record the discriminator at the owner, mark compliant sites | — | the "IMPLEMENTED NOWHERE" caveat gains a doctrine sentence; no behavior change |
| **5** | **R3 type split** — registry + 4 contract lines + export round-trip + supersession entry, §4 | 4 | `export_key_types.py --check` round-trip green; contract and registry agree |
| **6** | **R2 divergence test** — analysis, §6 | — | a stated verdict: distinct axis, or relabelling |
| **7** | **Vertical slice** — §7 | 5 | a seeded campaign organically queues, resolves and banks one finding |
| **8** | **B1 hashing rule** → **R13 predicate registries** (IN engine-evaluable, FI claim-only, promotion rule) | B1 | a hash spec with a stability test across agents |
| **9** | **`npc_memory` authoring** — contract delta, standalone Memory spec, **schema migration #4**, `state.proposition_revised` registration. R9/R11/R12 all land here | 8, 5 | round-trip serialize/restore of the three new registries |
| **10** | **R10 seeding** — §6.3, and note the guard that must be *deliberately* retired | 9, B5 | population holdings seeded; the pinning test replaced, not deleted |
| **11** | **R6 generator + erosion telemetry** | 8, 9 | generative test: a reachable chain exists at generation for N seeds |
| **12** | **R4 Lattice build** + REFINE voice lines (authored, editorial) | 6, 5, 9 | the "why this NPC responded" readout ships with the Matrix |
| **13** | **R1 heavy migrations** — combat defender-derivation first, then contest `base_ob`; faction sites wait on B2; opposed-roll waits on B3 | 4, B2, B3 | measured balance delta reported *before* any tuning |
| **14** | **R14** — nothing to execute; keep the fieldwork proposal one file | — | — |

**The shape worth noticing:** five steps are executable today and none of them touches the belief layer. The rulings did not create one big blocked project — they created a small unblocked one and a large blocked one, and the unblocked one is the slice.

---

## §3 R1 IN DETAIL — the obstacle doctrine

### §3.1 The docstring's claim is true (MEASURED)

`engine/autoload/dice_engine.py:118-123` states the score/2 derivation is *"IMPLEMENTED NOWHERE — every call site in the tree still passes a hand-set Ob."* Confirmed. Three sites are score/2-**shaped** by independent design; that is convergence, not implementation.

### §3.2 The census, three classes

**Class A — OPPOSITIONAL, must become score/2 (five sites):**

| Site | Now | Under the ruling |
|---|---|---|
| `systems/factions/sim/tribunal.py:116-122` | Ob = `accused.L` (full), halved only on formal grounds | base becomes L/2 — ⚠ **and the existing formal-grounds halving now duplicates the general rule.** Does it become L/4, or demote to a modifier? A ruling this creates |
| `systems/factions/sim/parliamentary_transfer.py:255-259` | `Holder.L + 2` | `L/2 + 2` — the file's own §5 sensitivity analysis was run at the full-score form |
| `systems/combat/combat_engine_v1/core.py:45,104` | `DECISIVE_OB = 3` fixed; its own docstring admits it "does not do at all" what the ruling requires | defender's score/2 + modifiers. **Defender-derivation first, band migration second** — the order is already ruled at `HANDOFF.md:115-119` |
| `systems/social_contest/sim/contest/resolver.py:155,288-289` | `Venue.base_ob = 2.0`; resistance never wired in (`wrapper.py:313-315`) | opponent score/2, venue demoted to modifier — the dormant resistance seam is where it lands |
| `systems/fieldwork/fieldwork_v30.md:353-355` | Concealment Ob = concealer's **rolled net** | concealer's score/2. **Doc-only, no code exists** |

**Class B — NON-OPPOSITIONAL, already the ruled shape (no change).** Threadwork's `DEPTH_OB`/`MENDING_OB`/`BREADTH_OB`/`DISTANCE_OB` (`operations.py:54-101`), collective's depth base + `LATTICE_FRACTURE_OB_PENALTY` (`collective.py:143-156`), `GREAT_WORK_FINAL_OB`, `ABSOLUTION_OB`, Muster/Govern, `RECALL_OB`/`MORALE_CASCADE_OB`, threadcut round penalties, and fieldwork's Depth table (`fieldwork_v30.md:31`, which the ruling explicitly preserves).

**Class C — ALREADY COMPLIANT.** `crown_initiative.py:189-190` Coronation = `floor(Church.L/2)+1`; fieldwork's Impress/Negotiate/Demand = `floor(NPC stat/2)+k`; `opposing.py:85` depth base + `floor(opponent_tps/2)`.

### §3.3 The ambiguity that must not be resolved silently — B3

**The opposed-roll class.** `systems/combat/sim/combat.py:163-172` documents it exactly: *"Strike is an OPPOSED roll, so the defender's result is the obstacle and it has already been subtracted."* Mass battle does the same — each side's Ob is the other side's net, floor 1.

These are maximally "defined against a character" — yet the obstacle is a **roll**, not a derived number. So R1 admits two readings:

- **Narrow:** R1 governs *static* obstacles; opposed rolls are a different resolution shape and are untouched.
- **Broad:** opposed rolls become static score/2 obstacles, and the roll-vs-roll model disappears from combat and mass battle.

The broad reading would invalidate the byte-exact mass-battle golden battery and change combat's fundamental shape. **This is genuinely Jordan's and I will not infer it.** Five further sites are ambiguous for narrower reasons: `mass_seizure.py:74-75` (`10 − PT − infra`, attribute-defined but inverse-linear), `council_solmund.py:27-33` (`floor(CI/30)+2`), `crown_initiative.py:46-59` (a *gap*/2, not a score/2), `FEIGNED_RECOGNIZE_OB`, and `KNOT_FORMATION_OB`.

### §3.4 What breaks when Class A migrates

Combat: the `golden_element_parity` / `golden_heft_percussion_snapshot` / `r3_identity_golden` family plus `test_combat_audit_pins.py` and `test_combat_balance_guard.py`. Contest: the 151-test groundup battery and `_kernel_tests.py`, which pin `sigma_leverage.degree(3,3) == 2` — that HELD entry in `tests/valoria/test_degree_ladder_single_owner.py` is deleted **only** when the migration lands. Faction: the seeded-campaign Key-emitter tests on `tests/valoria/_campaign.py`. Mass battle: the byte-exact digests, **but only under B3's broad reading**.

Fieldwork breaks nothing — its Depth table stands. **R1 de-risks fieldwork rather than costing it.**

---

## §4 R3 IN DETAIL — the type split

**No migration is needed, and this is the finding that makes the step cheap.** `scene.investigation_resolved` has **zero runtime**: no `.py` or `.gd` emits or consumes it; the single tree-wide hit is a description string at `tools/dashboard_data.py:823`. No Keys of the old type exist anywhere, so §10's "migration path for existing Keys" is satisfied vacuously.

The registry entry is itself the conflation — `key_type_registry_v30.md:880` reads *"Investigation, inquiry, **or trial** concluded."*

**Two types (names and payloads are JUDGMENT; the constraints are ruled):**

1. **Investigation finding** — emitted by `fieldwork_action`. **R5 imposes a hard payload constraint: no truth field.** No `correct: bool`, no engine verdict. Payload: `investigation_id, subject_id, asserted prop_id` (once R13 lands), `degree`, `support_refs`. `inconclusive` stays representable.
2. **Tribunal / inquiry verdict** — emitted by `faction_politics`, eventually `tribunal.py`. Keeps `finding: exonerated|guilty|inconclusive`, `sentence`, `public`. **An institutional verdict is allowed to be declarative** — R5 constrains player-facing truth, not court outcomes.

**One commit, four contract lines + the registry**, or contract-CI will see a type in `module_contracts.yaml` absent from the registry: `:91` (faction_state consumes), `:160` (npc_behavior consumes), `:448` (scene_slate emits), `:900` (faction_politics emits). Both consumers subscribe to **both** new types to preserve declared behaviour.

**Two procedural notes.** The `rendering_dispositions.yaml` precondition is **warn-only** — that file does not exist — but the disposition should be written anyway; the finding type inherits the Case Board's RENDERED-RICH answer. And §10 points at `canon/supersession_register.yaml`, which **does not exist**; the live path is `registers/supersession_register.yaml`. Downstream: §9's count 55→56, `export_key_types.py --check`, and the derived `key_graph.json` / `execution_map.json` / `engine_atlas.json`.

---

## §5 R7 AND R8 — complete edit-site lists

### §5.1 R7 — doc-only, two sites

No code implements the FAIL-marked model; `threadwork/sim/threadcut.py:9,23,127` already declares "no Coherence track per §6.3."

1. `systems/fieldwork/fieldwork_v30.md:529` — threadcut Coherence "drains at +0.5 per strain… at 0 the Knot collapses." The P-06 FAIL model verbatim (`canon/02_canon_constraints.md:15`).
2. `systems/fieldwork/knots_v30.md:279` — the same drain, citing fieldwork §5.6b.

Already compliant, do not touch: `fieldwork_v30.md:175`, `knots_v30.md:273-275` (the self-maintenance strain model, instability at 5), `threadwork_v30.md:900-901`, and the frozen historical `threadwork_v25_historical.md`.

**JUDGMENT, and it is a design choice the ruling does not settle:** the collapse trigger must re-derive from the strain track (the strain-5 instability model is the natural anchor). Someone has to draft that; the ruling only forbids the Coherence version.

### §5.2 R8 — nine stale doc sites

*−1D remnants:* `fieldwork_v30.md:104` (contradicts its own §2.2 at `:72`) · `combat_reference_v1.md:367` · `complete_systems_reference.md:132` · `canonical_registry.md:267` · `valoria_ui_ux_v4_1.md:661` · `valoria_ui_ux_v4.md:1182`.
*flat +1 Ob remnants:* `fieldwork_v30.md:141` and its index row `:846` · `scale_transitions_v30.md:113,307` (the code already does 0.15 citing the same ED) · `mass_battle_v30.md:345` · the UI docs at `valoria_ui_ux_v4_1_max_audit.md:98,452`, `valoria_ui_ux_v4.md:1442`, `valoria_ui_ux_v4_2_workplan.md:451`.

Already correct: `fieldwork_v30.md:72`, `threadwork_v30.md:159,217,238`, `derived_stats_v30.md:72,92` (the authoritative statement), `config.py:123`, `zoom_in_out.py:59,149`.

**The params capture holds a stale "+1 Ob per Wound" at `engine/engine_params/params_tables.yaml:5416-5423`** — and it is byte-exact with a retired generator, so it **cannot be regenerated and must not be hand-edited**. Follow the convention the tree already uses for exactly this (`dice_engine.py:130-137`): the correction lives at the owner, never in the capture.

### §5.3 R8 is a BEHAVIOUR change, not doc hygiene — and this is the trace's most consequential finding

`systems/combat/sim/combat.py:52` sets `WOUND_PENALTY_PER = -1` and applies it at `:130` (`pool += wounds * WOUND_PENALTY_PER`). **That module is live in the campaign** — `scene_dispatch.py:273` imports it as the scene-combat resolver.

So "+0.15 Ob per wound everywhere" converts a **dice-pool penalty into an obstacle penalty on a live path**. Seeded-campaign outcomes move; the `_campaign.py` Key-emitter tests move with them. Step 3 is therefore held separate from step 2 and carries the #311 discipline: **re-record goldens with cause, report the delta before tuning.**

**Two boundaries the ruling's word "everywhere" reaches further than its source did (JUDGMENT — flagged, not resolved):**
1. **Does R8 strike combat's `WOUND_DEF_OB = 0.25`?** ED-PC-0006 scoped +0.25 to combat's bilateral passive-defence channel specifically. My reading is that it stands and R8 is the active-roller rule — but "everywhere" is broader than that scoping, so it needs a word.
2. **Rattled is not wounds.** Contest made Rattled −1D deliberately while `fieldwork_v30.md:72` gives Rattled +1 Ob. Adjacent contradiction, *not* covered by R8.

---

## §6 `npc_memory` — what R9/R10/R11/R12 require

### §6.1 Disposition is triple-homed today, and R9 invalidates all three

- `module_contracts.yaml:397` declares "Disposition Track" as **`fieldwork_knots`'s own** state → moves to `npc_memory`.
- `registers/mechanics_index.yaml:303-308` points `disposition_track` at `systems/fieldwork/sim/fieldwork.py` → repoint.
- `knots.py:189-191` reads it duck-typed off actor objects (`disposition_with_<other>`, falling back to `.disposition`) → becomes an `npc_memory` query, and `apply_knot_loss`'s long-orphaned `disposition_set_to` consequence finally gets an owner to route to.

⚠ **The fieldwork proposal's own §6 draft contract says Disposition is "stored on `npe.NPC`". R9 supersedes that line.** Anyone executing from §6 verbatim will re-home it wrongly.

### §6.2 Serialization needs schema migration #4 (MEASURED)

`World` round-trips NPCs via hand-enumerated `to_dict`/`from_dict` (`game_state.py:302-305, 378-382`). New registries **do not ride along**. The tree has done this three times — migrations #1/#2 (2026-05-19) and #3 (2026-06-23) at `game_state.py:177-212` — each adding a world registry with an owning dataclass, the `_store(world)` router with module-level fallback, and hand-extended serialize/restore. Follow that precedent exactly.

⚠ **`world.beliefs` already exists** (`game_state.py:198`) holding *creed* Beliefs. The proposition store must not be conflated with it — the same distinction as `state.belief_revised` vs `state.proposition_revised`.

### §6.3 R10's population cost is currently pinned at zero **by a test** (MEASURED — and stronger than the trace stated)

`generate_npc` has **no automatic call site**: not at world-gen, not in the season tick. `mc_v18.py:175` records the deliberate omission. And it is **guarded**:

- `engine/tests/test_world_population.py:142` — `test_generate_npc_has_no_automatic_call_site_this_wave`
- `engine/tests/test_f7_smoke_oracle.py:162` — `assert npcs == 0, "npcs_generated is no longer 0 … update the golden"`

So R10's population scale is not merely unbounded-by-policy — **wiring NPC generation will fail two named tests by design.** That is the correct behaviour: those guards exist so generation is switched on deliberately rather than by drift. Step 10 must therefore *replace* them with a bounded-population assertion, never delete them.

---

## §7 THE VERTICAL SLICE — re-costed, and the rulings made it EASIER

| Ruling | Effect on the slice |
|---|---|
| **R1** | **Cost reduced.** The slice's obstacle is a site: Depth base + modifiers is now the *ruled* model, not a guess. No score/2 machinery — provided the slice has no active concealer, so keep contested investigation out |
| **R3** | **One prerequisite added:** the terminal Key must not be the type ruled for retirement. The finding-type registration becomes a slice prerequisite — executable today, and it does double duty |
| **R4** | **Lattice NOT pulled in**, *provided the slice stays dialogue-free.* The slice's roll is a site action, not an Interview. **Design constraint: no interview in the slice** — any NPC questioning drags in the REFINE voice lines, which are authored editorial content |
| **R5** | No build cost, one acceptance criterion: the Leverage tag is the *only* confirmation channel, so acting on the finding must produce a legible world response, not a readout |
| **R6** | Trivially satisfied — the fuse is hand-authored, so generation-time solvability holds by construction |
| **R9/R10** | **Avoided entirely** — consequence goes to the settlement ledger, not to Holdings, so the slice never touches the hashing blocker |

**Revised additions (five):** (1) one trigger definition + `"fieldwork"` in `evaluable` at `scene_dispatch.py:96`; (2) the resolver body replacing the stub, Ob = Depth base + modifiers, pool placeholder flagged pending B4; (3) **the `scene_dispatch.py:354` call-site fix — still required**, since `world` is not passed to `run_fieldwork_scene`; (4) the R3 finding-type registration, emitted with `causes` populated — **the slice becomes the first honest `causes` emitter outside `echo_transport.py:317`**; (5) the `ledger_add` Leverage write.

**Verdict: buildable, and net easier than before the rulings.**

---

## §8 A CORRECTION TO MY OWN HYPOTHESIS

Before the census I proposed that R1's expensive half would be the *non*-oppositional sites — that "base plus modifiers" is how every hardcoded Ob already works, but none of them **declare** the structure, so all would need to become legible as base + named modifiers.

**That was wrong, and the census says so.** A large share of the non-oppositional sites already declare the structure explicitly: `collective.py:143-156` is depth base + `LATTICE_FRACTURE_OB_PENALTY`; `operations.py:54-101` is a named table per scale; `infrastructure.py:57-66` has a dedicated `seizure_ob_modifier` channel; `zoom_in_out.py:33,87,149` is a modifier channel by construction. Class B is **already compliant**, not merely compatible.

The expensive half is Class A — five oppositional sites, three of them load-bearing on goldens — plus the six ambiguous ones. I reasoned from a handful of sites I happened to have seen rather than from the tree, and got the cost profile backwards.

---

## §9 FALSIFIERS

| Claim | Check | Ran? |
|---|---|---|
| score/2 is implemented nowhere | `dice_engine.py:118-123` + full obstacle-derivation census | ✅ (a helper under an unmatched name would falsify) |
| `combat.py`'s −1D wounds is live in the campaign, making R8 a behaviour change | read `combat.py:52,130` + `scene_dispatch.py:273` | ✅ **re-verified independently** |
| Strike is an opposed roll — the defender's *result* is the obstacle (B3 is real) | read `combat.py:163-172` | ✅ **re-verified independently** |
| `scene.investigation_resolved` has zero runtime → no migration | grep `.py`/`.gd` tree-wide — one description string at `dashboard_data.py:823` | ✅ **re-verified independently** |
| `generate_npc` has no automatic caller **and two tests pin it at zero** | grep all callers; read `test_world_population.py:142`, `test_f7_smoke_oracle.py:162` | ✅ **re-verified independently, and stronger than first reported** |
| Disposition is triple-homed | read contract `:397`, mechanics_index `:303-308`, `knots.py:189-191` | ✅ (trace) |
| Serialization is hand-enumerated; three migration precedents | read `game_state.py:170-215, 265-382` | ✅ (trace) |
| params capture holds a stale +1 Ob and cannot be regenerated | read capture `:5416-5423`; generator-retirement taken from a docstring, not re-verified | partial |
| The 151-test groundup count | cited from `HANDOFF.md:123`, **not re-counted** | ❌ |

**Explicitly JUDGMENT, not measurement:** the two new type names and payloads (§4); R7's replacement collapse trigger (§5.1); whether `WOUND_DEF_OB` survives R8 (§5.3); the R1 homing recommendation; the slice's "no interview" constraint (§7); and every dependency **edge** in §2 — the edges cite tree facts, but the ordering is design reasoning and should be attacked as such.

**The claim most likely to be wrong:** that step 5 (the R3 split) is cheap. It rests entirely on "zero runtime, therefore no migration." If a data-driven or GDScript emitter exists that the `.py`/`.gd` grep missed, the split acquires a migration path and stops being a same-day step.
