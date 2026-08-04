# Valoria Fork — Plan of Record

## Status: PROPOSED (ED-IN-0124, 2026-08-03). Jordan-vetoable throughout.
## Class: A — substrate/architecture. **Nothing here ratifies on merge**, and §10 states the forcing
## mechanism that keeps that from becoming an indefinite hold (the ED-1094 failure this document was
## reproducing).
## Version: v3 — executable rewrite. Supersedes the 2026-08-02 draft (16 CONFIRMED-WRONG on an
## independent critic pass) and the 2026-08-03 amended draft, which accreted a rolling execution diary
## and carried nine defects of its own. §12 records both, because the failure mode recurs.

---

## 0. What this rewrite changed, and why you should trust it more than its predecessor

Two independent read-only Fable-5 passes ran against the working tree — one adversarial critic
(steelman → logic → process → 34-row fidelity table), one architectural reasoner. Neither could write.
Between them they found the previous draft's numbers largely sound and its **structure** unsound. The
corrections, each verified against files before being applied here:

| # | The draft said | The tree says | Where |
|---|---|---|---|
| 1 | "3 of 27 modules execute" as the headline | Four *more* modules marked `deferred` are **observed executing** — `faction_state` 498 calls, `territorial_piety` 229, `peninsular_strain` 30, `scene_slate` 12 | `audit/2026-08-03-session-oddities.md` G2 |
| 2 | W4: "0 of 324 `sim_params` records carry provenance" | `citation_coverage` = **cited 84 · uncited 240 · assumption-grade 8** — the field exists and is populated | `engine/engine_params/sim_params.json` |
| 3 | `WEAPONS` lives in `combatant.py` | It is at **`weapons.py:74`** | verified |
| 4 | "46 of 56 key types have both a producer and a consumer; 10 dead" | **47 and 9** — `meta.legacy_event` is in both the no-producer and no-consumer sets and was double-counted | `tests/valoria/test_key_graph.py:45,51-56` |
| 5 | §6.2 "`Faction.L` already reconstructs" | **It does not.** The manifest note and HEAD commit `6f5ada6` both retract this | `wiring_manifest.yaml:112-122` |
| 6 | ED-MB-0043 "**RESOLVED** 2026-08-03 by Jordan (PR #274)" | The ledger entry is dated **2026-07-26**, `needs_jordan: true`, with the two-trees fork open in `follow_on`. **Zero** register hits for the ruling. `CURRENT.md` still lists it held | `registers/editorial_ledger_mb.jsonl:6` |
| 7 | I3: "the 14 units with no code" | `no_code_declared` measures **contract-pointer absence**, not code absence. Its members include `mass_battle` (28 + 5 modules of engine) and `faction_politics` | `references/execution_map.json:30-45` |
| 8 | W0 built a fork-readiness scan from scratch | **`tools/build_fork.py` already exists** (21 KB) — carry/leave as data, runtime-closure classification, and a seeded campaign run with the source repo scrubbed from `sys.path`. The plan never cited it | `tools/build_fork.py` |
| 9 | "autoload is a leaf" (inherited from CLAUDE.md §3) | `engine/autoload/game_state.py` imports **downward** into `systems.*` at function-local sites (`:257`, `:365`, …); acyclic only by import-time laziness | verified |

**Items 1–7 are corrections to claims. Item 8 is a whole tool the plan duplicated in prose. Item 9 is
an architecture fact that changes what the Godot autoload becomes.** The pattern is unchanged from §12:
every one was a true observation carried one inference too far, and every one was cheap to check.

**The structural change.** The previous draft had become a *third* current-state surface, disagreeing
with `wiring_manifest.yaml` and `HANDOFF_IN.md` about `Faction.L` on the same day. A proposal holds
**decisions, pointers and holds**. The rolling execution log moves to `registers/handoffs/HANDOFF_IN.md`,
which already duplicated most of it.

---

## 1. Reading order (~11k words; budget one read)

| # | Read | What you get wrong without it |
|---|---|---|
| 1 | `CLAUDE.md` §0, §0.1, §5, §8 | The currency protocol, the five measurement checks, and that every rule lives once |
| 2 | **`references/wiring_manifest.yaml`** | Build/godot/port_rank/parity for 27 modules + 8 adapters. **Read it with §3's caveat** — it is analysis-derived and wrong about at least four modules |
| 3 | `systems/_architecture/holonic_container_doctrine_v1.md` §1–§2 | That `Key IN → resolver → OUT` is CANONICAL and frozen, and a second interface dialect is a named forbidden failure |
| 4 | `godot/godot_conversion_strategy_v1.md` Parts V–VIII | Gate-0's five preconditions, the Stage-1 spine, the per-module ritual. **Do not write a port plan without this** |
| 5 | `tools/build_fork.py` | That the fork's assembly is already implemented as a tool. Read the code, not a description of it |
| 6 | This document | The Python-side Stage 0 the strategy assumes |

`audit/2026-07-30-mb-session-retrospective/00_lessons.md` (guardrails G13–G21, and why `main` is
CI-red) is **required for anyone touching the MB lane** and optional otherwise. The previous draft
listed it as mandatory while also banning the corpus it lives in; that contradiction is resolved here
in favour of scoping it.

**Orient by execution.** Every one of these works today:

```bash
python3 tools/wiring_map_check.py --check      # 27/27 modules · 8/8 adapters · tags resolve
python3 tools/wiring_map_check.py --work-list  # the ranked port order. THE work-list
python3 tools/build_fork.py --out /tmp/fork --verify-only   # fork assembly + self-containment
python3 tools/review_core.py --check           # repo-state verdict vs review_baseline.yaml
python3 tools/export_engine_params.py --check  # combat oracle → JSON round-trip (blocking)
python3 tools/export_sim_params.py --check     # 324 constants, drift gate
```

**Do NOT read** the ~339k lines of process/audit markdown. `engine/params/*.md` in particular — 43
files — has **zero readers** in `engine/` or `systems/` (positive control: the same grep in `tools/`
returns 20+ files, so the method finds what exists). Reading it to learn "the values" teaches a layer
nothing executes.

**The one procedure that matters.** Before asserting something does not exist, run a positive control:
search for something you *know* exists, by the same method, and confirm the method finds it. Every
significant error in this plan's history was a false absence derived from a proxy. Both Fable passes
caught themselves with it this session — a first `engine/params` count of 14 (top-level glob; the
recursive glob finds 43) and a first `WEAPONS` grep in the wrong file.

---

## 2. The thesis, rebuilt on trace facts

**The Godot port has a detailed, dependency-ordered strategy. The Python side does not.**

Gate-0's precondition G0.5 — *a module ports only from canonical/ratified sources, and halts on any
value untraceable to a cited source* — presupposes a Python side ready to be ported from. Nobody has
planned the stage that makes that true. Jordan's principle 5 (*"100% runnable in Python, then port"*)
names it. **That is Stage 0, and it is this document's only real contribution.** Everything else is
assembly over primitives that already exist.

The previous draft argued this from the manifest's `build` labels. Those labels are contested (§3), so
the argument is rebuilt on facts that survive any classification dispute — all four measured, none
label-dependent:

1. **A seeded campaign dispatches 29 scene slots. All 29 are `contest`. Zero combat.** Nothing in the
   engine can queue a personal combat, so `personal_combat` — port rank 0, the golden path, 75%
   covered, with a GDScript port — is unreachable from the loop.
2. **554 typed values are extracted and essentially none reach anything that runs.** Every terminus is
   a test, a dashboard, or the producer itself. The repo is producer-heavy and consumer-empty.
3. **The campaign's hottest path by three orders of magnitude runs on a tree that is not canon** —
   `systems/mass_battle/sim` (5 modules), while the 28-module `tests/sim/mass_battle` is canon.
4. **14 of 27 modules are `godot: no-oracle`** — there is nothing to port from — and 2 are marked
   `retire`, so **the live roster is 25, not 27**. This count is a direct field read, not a verdict.

> **Reconciling with the tool.** `wiring_map_check --summary` reports over modules AND adapters
> together — 35 units: `deferred:11 · design:9 · gated:6 · stub:4 · unwired:3 · live:2`. Modules alone
> are 27 because modules are the conversion units (one contract = one unit = one parity target).
> Adapters contribute the other 8. Both are correct; they count different populations.

---

## 3. The manifest is the work-list and it is wrong in known places

This section exists because the previous draft leaned on `wiring_manifest.yaml` for its headline while
the *same session's* own oddities register contradicted it — and the draft cited that register for a
different fact two sections later.

- **G2: four modules classified `deferred` are observed executing** (`faction_state` 498 calls,
  `territorial_piety` 229, `peninsular_strain` 30, `scene_slate` 12). Presence is hard evidence;
  the manifest is wrong about these four, not the trace.
- **G7 bounds how far that generalises:** the `by_contract` trace channel can attribute only **5 of 27**
  modules, because most contracts declare no code file. **Every zero is "not attributable at this
  seed", never "dead."** G2's positives stand; no negative may be inferred from the same instrument.
- The manifest is dated `as_of: 2026-07-29` and is analysis-derived. `--check` validates that tags
  *resolve* and vocabulary is legal — **not that verdicts are true.**

**Consequence for Stage 0's metric.** The `build` states are *not* a monotone ladder. `personal_combat`
is `unwired` yet real, 75%-covered and gd-ported; several `deferred` modules run and resolve nothing;
nothing forces `stub` before `gated`; a module can be `live` while resolving nothing. And "every module
reaches `live` or `gated`, and `--summary` reports it" **is satisfiable by editing the YAML.**

> **Stage 0's exit condition is therefore two-part and the second part is not optional:** a module is
> promoted only when (a) `--summary` reports it `live`/`gated` **and** (b) **its `parity` target passes**
> — key-log parity, typed-export round-trip, state read, or data, per the field the manifest already
> assigns. Part (b) is what makes the metric resistant to G13's null-system failure ("if doing nothing
> scores well on your metric, the metric cannot validate a change").

**Repair task (unblocked, mechanical):** re-derive the four contested `build` verdicts from the trace
and correct the manifest, with `tests/valoria/test_execution_map.py` extended to fail when a module
observed executing is classified `design`/`stub`. That guard is the §0.1-point-5 requirement — one
owner for the classification, and a check that fails on recurrence.

---

## 4. Code-first: where the authority boundary sits

"Code-first" is not one regime here. Applying one uniformly is why the previous draft proposed
inverting the combat oracle — which would destroy the design record interleaved with it.

**`config.py` is not a table; it is a table interleaved with its own justification** — retirement
history, unit-rescale derivations, and `[SIM-CALIBRATE]` grades sit inline with the constants.
Inverting it either destroys that commentary or forces it into a parallel prose doc that will drift.

| Artifact | Role | Why |
|---|---|---|
| `config.py` + `core.py` (combat oracle), all `systems/*/sim`, `engine/` | **SOURCE (code)** | The oracle carries its own design record. ED-1050 already ratifies this direction: oracle-first, the port regenerates |
| `data/key_types.json`, `data/weapons.json` (post-inversion), `module_contracts.yaml`, `wiring_manifest.yaml` | **SOURCE (data)** | Content and registries, no commentary entanglement |
| `combat_engine_v1.json`, `sim_params.json`, `key_graph.json`, `EXECUTION_MAP.*`, every `.tres`, every generated Python view | **GENERATED** | Each carries a `_generated` header; the convention already exists in both exporters |
| Subsystem design `.md`, doctrine, the regenerated param tables | **DOCUMENTATION / conversion input** | Authoritative *only* where no code pair exists (principle 7) |

**Prose is not deleted.** 14 modules are `no-oracle`; for them the prose is the only spec that exists.
It is demoted from runtime authority, not from the repo.

### 4.1 The inversion target the plan never named

`engine/substrate/keys.py:179` is a **loader/validator over a markdown file**, and its docstring says
so: *"The registry markdown is the single source of truth (CLAUDE.md §8 'every rule lives once'); this
class parses it at load time rather than duplicating the 44-type roster in code."* The repo already
treats one prose file as runtime data — parsed by regex, at load, in Python. Meanwhile
`godot/skeleton/data/key_types/*.tres` (4 files) is a **hand-made shadow** of the same roster.

Godot cannot sanely replicate a markdown parser. This is the clearest inversion in the tree and it is
first in the sequence: `key_type_registry_v30.md` → `data/key_types.json` (SOURCE) → Python
`TypeRegistry` loads JSON · `.tres` cooked from JSON · the markdown table regenerated as documentation.
Semantics do not change; `keys.py`'s existing parser already defines the schema.

---

## 5. The centralized-value layer — mechanism, guard, gate

**Source format: JSON.** Both live pipelines already emit JSON with `schema_version`, sorted keys and
byte-exact `--check` gates; Godot parses JSON natively with no plugin surface; YAML adds a runtime
dependency the fork does not have and canonical byte-stable YAML is harder than
`json.dumps(sort_keys=True)`. **`.tres` is a cooked target, never the authority** — Godot Resources are
the right runtime representation and the wrong source representation, because the Python sim cannot
read them without inverting the oracle direction.

**Provenance as a ratchet, not a per-edit gate.** `export_sim_params.py` already promotes a trailing
comment into a typed `citation` + `citation_grade` and publishes `citation_coverage`. Keep it. CI fails
only when `uncited` **increases** or an existing citation is deleted. Changing a cited value's number
is an ordinary commit — the PP/ED it cites is where the change is justified. Only a *new uncited* value
trips the gate. Current baseline: **cited 84 · uncited 240 · assumption-grade 8 · total 324.**

### 5.1 The guard — and why the morale template does not transfer

CLAUDE.md §0.1 point 1 is precisely on point: when a getter starts reading a new source while setters
still write the old one, **every writer silently becomes a no-op.** The inversion creates exactly that
hazard. The previous draft's falsifier ("round-trip CI red on a hand-edit of a generated view") guards
edits of *extracted* values and does nothing about the **new bare constant** added straight to Python
that never enters the table. That is half a guard.

`tests/valoria/test_morale_write_sweep.py` is named as the template, and its *shape* does not transfer:
morale's hazard is runtime writers, so it sweeps assignments by regex. Inverted constants have **no
legitimate runtime writers at all**. Two layers instead:

1. **Import-time immutability.** The generated view exposes `types.MappingProxyType` (dict tables) or a
   frozen dataclass (records). A runtime write then raises `TypeError` **loudly** rather than
   succeeding-and-doing-nothing — the exact inversion of the morale defect. `config.CFG` is a plain
   mutable dict today. Legitimate runtime variation keeps its one existing owner, the `effective_params`
   overlay in `mc_v18`, which composes *on top of* the frozen base and never mutates it.
2. **An AST tripwire against new bare source constants**, reusing `export_sim_params.build()`'s existing
   module-scope `ast.Assign` walker. For every *governed* file — a per-module allowlist,
   field-parameterized exactly like `_CELL_OWNED`, so inverting a new module means adding one key — any
   module-scope numeric literal assignment whose name is not in the generated-view manifest **fails**
   with *"this value belongs in `data/<module>.json`."*

What **does** transfer from the morale template, and must be copied verbatim: an `allowed` set with a
stated reason per exemption, and a **`test_the_guard_itself_can_fail`** positive control that plants a
synthetic bare constant in a parsed string and asserts the walker flags it. A guard that cannot fail
advertises a protection that does not exist.

### 5.2 The gate and its falsifier

One command, `tools/cook.py --check`, three checks per inverted table: (i) source → regenerate Python
view → byte-equal to committed; (ii) regenerate `.tres` → byte-equal to committed; (iii) schema-validate
source (types, ranges, `schema_version`, citation ratchet).

**Falsifier** (§0.1 point 3): a test that copies the committed generated view, mutates exactly one
value, and asserts the checker exits 1 — and symmetrically mutates one *source* value and asserts drift
is reported against the stale view. `export_engine_params.py --check` is the working precedent and is
missing exactly this: CI being green does not prove the check *can* go red.

---

## 6. Architecture — what may be built without a ruling

**The container shape is frozen and is not this plan's to change.** The holonic doctrine fixes
`Key IN → resolver → OUT`; guardrail 2 forbids a second interface dialect. The v1 draft's
`orchestrator.resolve()` channel stays withdrawn.

### 6.1 The dependency direction, corrected

The claim "subsystems depend upward on `engine/`; autoload is a leaf" is three-quarters true.
`engine/substrate` is a pure leaf. But **`engine/autoload/game_state.py` imports downward into
`systems.*`** at function-local sites (`:257`, `:365`, …) and its dataclass fields are annotated with
subsystem state types (`CoherenceState`, `TreatyRecord`, `InsurgencyRecord`, …). It is acyclic only
because the imports are lazy.

The real architecture is four layers — **substrate → autoload services → subsystems → orchestrator**
(`cross_scale` + `mc_v18`) — with the orchestrator legitimately on top. That survives the fork *except*
`game_state`: `World` knowing every subsystem's state type is exactly the coupling that, ported
naively, makes the Godot `GameState` autoload preload every subsystem Resource. **Reversible fix, no
ruling required:** invert to registration — each subsystem registers its state slice with `World` at
boot. That also serves save/load. Falsifier: the seeded `key_log_hash` is byte-identical across the
refactor.

### 6.2 What is genuinely gated is narrower than the doctrine's text

The doctrine (2026-07-02) calls the propagation spec "the highest-value unauthored canon." **It is no
longer wholly unauthored:** `engine/substrate/keys.py:16-32` cites `propagation_spec_v1.md` with
*ratified* termination guards — cascade-depth cap + emissions-per-tick cap (Theorem B), B1
no-synchronous-re-entry, and OF-7 deferred-apply at the accounting boundary, all RATIFIED 2026-07-07
under ED-IN-0026.

So the gate is **downward *Key* delivery only (ED-1006)**. Downward *function-call* orchestration
already exists canonically — `mc_v18` → systems, and the `action_callback` port seam. The plan must not
widen ED-1006 into a general prohibition on top-down control flow; that would block work no ruling
covers.

**Buildable now, no ruling:** the upward Key spine over `Faction.adjust`'s call sites; the `World`
state-registration inversion; a `Character` dataclass whose attributes are a **dict keyed by
`descriptor_registry.yaml`** (the 9-vs-10 roster is canon; the dataclass is reversible if the roster is
data rather than fields); the mass-battle canon adapter.

### 6.3 The two mass-battle trees

`tests/sim/mass_battle/` (28 modules) has **zero** imports of `engine`/`systems` — fully self-contained
— so re-homing is import-clean, and `build_fork.py` already re-homes it as `systems/mass_battle/canon/`
while carrying the live 5-module tree beside it. That is the structural resolution's first half.

Second half: an adapter in `faction_action`'s shape, mapping canon's return to the
caller's `{attacker_wins, degree, *_size_pct}`. ⚠ **Corrected 2026-08-04 (ED-IN-0125): the return shape
stated here was wrong.** `{winner, turns, phases}` is the `kind='single'` path; **the caller uses
`kind='multi'`, which returns `{winner, battle_turns, log, a_loss_final, b_loss_final}`** — see
`audit/2026-08-03-session-oddities.md` §H, which superseded this shape *before* this document was
rewritten and was copied in anyway. Three of the caller's four fields map mechanically.
**`degree` is the blocker** — canon has no four-band
degree and it drives the territorial outcome. **Partially unblocked 2026-08-04 (Jordan, C2):** mass
battle occurs **on a map**, and the loser of the scene is whoever **loses more units or has their
settlement captured** — that supplies `attacker_wins` and constrains the ladder to a
unit-differential/objective-capture basis, but does not fix the four band edges. Build the adapter **now**, with `degree_map` as a
**required argument with no default**. That is this repo's own established pattern for unruled canon:
`keys.py:27-30` makes the OF-CAP termination caps required constructor args precisely so *"no fabricated
constant enters the repo."* Engineering proceeds; the canon slot stays loudly empty.

Migration falsifiers: (i) the canon tree's byte-exact goldens stay green across the re-home (a pure path
move on a self-contained tree); (ii) with the swap flag OFF, seeded `key_log_hash` and `keys_emitted`
are byte-identical to pre-migration; (iii) with it ON under a candidate map, an A/B seeded-campaign
distribution **report** — not a gate — until Jordan rules.

---

## 7. The sequence

**First move: run `tools/build_fork.py` to completion and make its checks the fork's CI job zero.**

The tool exists, encodes carry/leave as data, classifies every file by runtime-closure relation, and
proves self-containment by running a seeded campaign with the source repo scrubbed from `sys.path`. It
is defended against the two obvious alternatives: *close `Faction.L` first* loses, because any pre-fork
measurement must be re-verified against the assembled tree anyway — doing it inside the fork binds its
falsifier to the tree that ships; *invert the params first* loses, because the inversion's round-trip
gates need a CI home and the fork's CI is that home. It is also the cheapest move, and it converts "the
fork is self-contained" from a claim into a test result — which is the whole lesson of §12.

| # | Work | Exit condition (falsifier) | Gated? |
|---|---|---|---|
| **1** | Fork assembly + CI job zero. Carry the 9 attributed MB failures as `xfail(strict, reason="ED-MB-0061")` | `build_fork.py --verify-only` green: escape scan clean, contract coverage reported, seeded campaign runs standalone. Aggregate CI green with zero non-xfail reds | no |
| **2** | Invert `key_type_registry_v30.md` → `data/key_types.json`; `TypeRegistry` and the `.tres` both load it | `cook.py --check` byte-exact both ways; the mutate-one-value test exits 1 (§5.2); the 4 hand-made `.tres` are regenerated and byte-compared | no |
| **3** | Export `WEAPONS` (`weapons.py:74`) to typed JSON; regenerate the GDScript weapon resource from it | 53 weapons exported; the generated `.gd` schema contains no `reach`/`weight`/`spd`/`handling` | **confirmation only** |
| **4** | Route `Faction.adjust`'s keyless call sites through Key emission; `World` state-registration inversion | `test_faction_l_reconstruction`'s strict xfail turns XPASS; `key_log_hash` byte-identical across the `World` refactor | no |
| **5** | MB canon adapter, `degree_map` required-no-default; `Character` dataclass with roster-as-data | Canon goldens green post-re-home; flag-OFF `key_log_hash` byte-identical | no (contents are C2/C4) |
| **6** | `sim_params` inversion, **per module**, ratchet-gated | `uncited` never increases; the AST tripwire fails on a planted bare constant (§5.1) | per-value collisions only |
| **7** | Repair the four contested `build` verdicts; extend `test_execution_map.py` to fail on observed-executing-but-classified-dead | The extended test fails against today's manifest, passes after correction | no |
| **8** | Canon queue, prepared with reversible stubs | §9 | **yes** |

**Item 3 is not a design ruling.** The previous draft queued the weapon cook behind Jordan. Exporting
the oracle and regenerating the port from it *is* ED-1050 compliance — the rule is "never let a port
correct its oracle in-place", and this is the compliant direction. It needs confirmation that the
retired-field removal is wanted, not a design decision. What the draft got right and must stay right:
**cooking `.tres` in the current schema would fabricate `reach` and `weight` for 53 weapons into a model
the oracle retired** — `config.py:7` records reach as derived from geometry, `0 of 53` weapons carry the
categorical fields, and yet `strike_module.gd:110` still computes on `w.reach == "long"` and
`combat_config.gd:84` still branches on `weapon.weight == "heavy"`. Oracle first, then cook.

### 7.1 Getting `main` green belongs at step 1, by attribution, not by fixing

The counter-position — *a red baseline with a fully bisected, attributed failure set carries more signal
than the plan credits* — is **correct about the failures and wrong about the channel.** The bisect
(ED-MB-0061: every failure restored by returning one named flag to OFF) is real signal and must be
preserved. But a red **aggregate** has zero marginal signal: a new regression is indistinguishable from
background.

`xfail(strict)` is the synthesis. Green aggregate restores marginal signal; `strict` means the moment a
ruling or a fix changes behaviour, XPASS fires and the record surfaces. This is explicitly **not**
re-pinning goldens to current behaviour, which the MB retrospective forbids in terms: *"re-basing before
fixing F1–F8 would bake nine defects into the definition of correct."*

> ## ⚠ C7 IS STRUCK — it was never an open question (ED-IN-0125, 2026-08-04). The paragraph below is
> ## preserved as the record of the error, not as a live question. **Do not re-open it.**
> Jordan had ALREADY ruled this a real defect (F1-class) on 2026-08-03 —
> `audit/2026-08-03-session-oddities.md:55` (D1) — and this document re-opened it the same day. It is
> also incoherent against canon: **PP-233 "Damage is simultaneous"**, implemented at
> `tests/sim/mass_battle/orchestration.py:1834,:1839,:2053,:2056,:2372,:2698`. Under simultaneous
> application a winner taking zero losses means the loser dealt zero damage — a damage-path defect,
> not a balance opinion. See §9 for the struck row and J9 for the live thread.

The underlying question is canon and is filed as **C7**: the failing tests are TRUE POSITIVES about a
real state — 60/60 battles ended in one turn, 42/60 with the winner taking zero losses. *Is a one-turn
rout with an untouched winner correct?* ~~Only Jordan can answer that.~~ **He already had.**

### 7.2 Track independence — the previous draft's claim was false in two places

It claimed "nothing in E depends on C except by position." Two counterexamples, both confirmed:

- **The 8 consumer-less key types.** `tests/valoria/test_key_graph.py:58-62` states that mapping
  unresolved consumers *"is a design decision, and guessing one is exactly the fabrication this repo's
  no-fabrication rule forbids."* Choosing a consumer **is canon**, and delivering a key downward into
  one touches ED-1006. Only the *defer* half is unblocked.
- **The contested `CI` scalar.** Both claimants — `ci_political` and `territorial_piety` — hold
  **CANONICAL** docs. Single-ownering it adjudicates between two canonical docs: a canon decision
  wearing engine clothes. It moves to §9.

**And one unmeasured premise remains, flagged rather than acted on.** Step 4 assumes routing
`Faction.adjust`'s sites through emission is behaviour-preserving plumbing. It may not be: Key emission
means deferred `apply` closures landing at the accounting boundary (OF-7), while the current writes are
immediate and mid-phase. Converting immediate writes to boundary-applied closures changes *when* state
is visible within a season, which changes trajectories, which churns goldens. **Settling measurement,
and it is required before the sweep:** route ONE site, diff the seeded winner and key composition. This
is the same one-site-first discipline that corrected the previous W1, applied to the work that
succeeded it.

---

## 8. Falsifier census — the honest accounting

CLAUDE.md §0.1 point 3 requires every result claim to ship the test that would have shown it wrong. The
previous draft carried ~13 exit conditions of which **2 were genuine falsifiers, and both were in waves
already executed** — the unexecuted future carried the unfalsifiable ones. Backwards.

| Class | Previous draft | This plan |
|---|---|---|
| Named test that can fail | 2 | 8 of 8 rows in §7 |
| Instrumented but defective | 3 | 0 |
| Restatement / escape-hatched | 5 | 0 |

The three patterns removed, and what replaced them:

- **"…or DEFERRED with a citation"** — any failure converts into a deferral, so nothing can fail.
  Replaced: deferral is now a *recorded decision with a named owner*, not an exit condition.
- **"uncited falls"** — a direction, not a target. Replaced by a **ratchet** (`uncited` may not
  increase), which a test can fail on a single commit.
- **"`--summary` shows those modules `live`"** — satisfiable by editing YAML. Replaced by the two-part
  condition in §3: classification **and** the module's own `parity` target passing.

One defect inherited and fixed: the previous E4 named *"`execution_map.json`'s contested count"* as its
falsifier. **No `contested` field exists in that JSON** — the count is computed into the generated
Markdown by `build_execution_map.py`. A falsifier pointing at a field that does not exist is not a
falsifier.

---

## 9. Held for Jordan — decisions only

The previous list ran to seven-plus items, three of which were reversible engineering calls in canon
clothing. **An over-long held list is itself a failure mode: it converts reversible decisions into
blocking ones.** Removed from the list and built instead, each with an explicit empty slot: the
`Character` dataclass (roster-as-data), the weapon export (ED-1050-compliant direction), and the CI
infrastructure fixes.

> ## ⚠ ALL EIGHT RULED 2026-08-04 (Jordan) — registered as ED-IN-0125 / ED-MB-0064.
> **Two of the eight were never decisions.** C5 and C7 are STRUCK: each converted a recorded *absence*
> into a prohibition, and one of them re-opened a ruling Jordan had given the same day. That is a
> defect in this document, not a question he failed to answer. The "Prepared how" column below was
> also **false in three rows** — it asserted three artifacts that do not exist in the tree — and is
> replaced by a measured "State in tree" column.

| # | Decision | RULING (2026-08-04) | State in tree (measured) |
|---|---|---|---|
| **C1** | **What triggers a personal combat?** `evaluate_triggers` emits only `contest`, so nothing queues a fight | **Field investigation, mass battle, AND scene contest can all trigger it — and it can also be invoked directly.** Four entry points, not the single escalation hook this document offered | `engine/cross_scale/combat_bridge.py` is the already-built seam (OI-01, ED-IN-0091) |
| **C2** | **The mass-battle `degree` mapping.** Canon has no four-band degree; it drives the territorial outcome | **Mass battle occurs ON A MAP; the loser of the scene is whoever loses more units or has their settlement captured.** Supplies `attacker_wins`, constrains the ladder to unit-differential/objective-capture. Band edges still unruled | ⚠ **Adapter NOT built.** `degree_map` appears nowhere in code. §6.3 says "build it now"; the old cell claimed it was done |
| **C3** | **`engine_clock`** — `doc: null` temporal spine, ED-1051 | **It stands.** It is the season counter **plus** the accounting boundary — the moment deferred Key effects land | `TickScheduler` (`engine/substrate/keys.py:404`) calls itself "the engine_clock-shaped emission seam"; close by pointing `doc:` at CANONICAL `propagation_spec_v1.md` |
| **C4** | **The attribute roster** — 9 vs 10 (OPT-AV-1) | **TEN — 3/3/3 plus Spirit.** Jordan flagged this as *not fully settled*, so it stays reversible | ⚠ **`Character` NOT built.** No such dataclass in `engine/` or `systems/`. Build it with attributes as a `descriptor_registry`-keyed dict so the roster is data |
| ~~**C5**~~ | ~~ED-1006 — downward Key delivery~~ **STRUCK — not a decision** | **Keys work all directions.** Scaling back and forth — faction actions ↔ scenes, mass battles ↔ duels, all scene information transported to impact the world — is a defining mechanism. ED-1006 recorded a **gap** ("scale_transitions SS3 has NO top-down Key-delivery rule"), which this document read as a gate | ⚠ **"Upward spine built" was false, and "upward" is the wrong frame.** `engine/cross_scale/` implements bidirectional transport and `ECHO_TRANSPORT` is **default ON**; but 30 of `Faction.adjust`'s 31 call sites emit no Key. Built and live, bypassed at 30/31 sites |
| **C6** | **`da.territorial_transfer`**, or ratify that `da.public_governance` + `target_territory_id` implies an ownership change | **No** — do not mint a new type. **The owner of territory is keyed** | `target_territory_id` at `key_type_registry_v30.md:200`; falsifier `tests/valoria/test_public_governance_transfer_key.py` |
| ~~**C7**~~ | ~~Is a one-turn rout with an untouched winner correct?~~ **STRUCK — already ruled** | **Jordan ruled it a real defect (F1-class) on 2026-08-03** — `audit/2026-08-03-session-oddities.md:55` (D1). This document re-opened it the same day at §7.1 ("Only Jordan can answer that"). It is also incoherent against canon: **PP-233 "Damage is simultaneous"** | Implemented at `orchestration.py:1834,:1839,:2053,:2056,:2372,:2698`. Under simultaneous application a zero-loss winner in 42/60 is a **damage-path defect**. Live thread: **J9** — does one rout fix green all nine red MB tests? |
| **C8** | ~~The contested `CI` scalar — `ci_political` vs `territorial_piety`~~ | **Not one scalar — a category error.** **Church Influence is a GLOBAL peninsula-wide tracker** that gates behaviours and actions (e.g. the mass-seizure attempt). **`territorial_piety` is a per-territory stat** for how religious that territory is, and it **feeds** CI | `ci_track.py:2` "Church Influence (CI) **world-track**" (PP-412); `mass_seizure.py:107` `_church_influence(world)`; `key_type_registry_v30.md:563` fires Mass Seizure at CI 100. ⚠ The "two CI generators" claim filed this session is **RETRACTED** — one generator, one stale docstring (`ci_track.py:18-23`) |

**The forcing mechanism (this is the ED-1094 repair).** "Nothing ratifies on merge" without a
forcing step is how ED-1083's doctrine sat PROPOSED in `main` indefinitely — the exact failure ED-1094
was written to close. So: **each C-item above is filed as its own ED entry with `needs_jordan: true`,
⚠ **CORRECTED 2026-08-04 (ED-IN-0125):** this sentence was present-tense for work that had not been
done — the same defect this document prosecutes in ED-IN-0124(f). What actually happened is better:
**all eight C-items were RULED by Jordan on 2026-08-04** and registered collectively in ED-IN-0125
(with C2's mass-battle content in ED-MB-0064), so per-item `needs_jordan` EDs would now double-register
settled decisions. The forcing mechanism was not needed because the ruling arrived first. Original
text follows.**
and appears on the SessionStart banner's Jordan docket until ruled.** A held item that is not on a
register is not held; it is forgotten. See §10.

---

## 10. Governance repairs this rewrite requires

Two defects where the previous draft became the *only* record of something the registers should hold.
Both are listed as required work, not silently fixed here, because one of them is a claim about a
ruling I cannot verify.

1. **The ED-MB-0043 canon-tree ruling is unregistered.** The draft stated it *RESOLVED 2026-08-03 by
   Jordan (PR #274), canon is `tests/sim/mass_battle/`*. The ledger entry is dated **2026-07-26**,
   `status: resolved` for the *vector audit*, with the two-trees fork open in its `follow_on` and
   `needs_jordan: true`. There are **zero** register hits for the ruling, and `CURRENT.md` still lists
   the fork as held. A session following the repo's own priority order (CURRENT.md ≻ a PROPOSED
   proposal) will correctly conclude the fork is still open. **Required: either file the MB-ledger
   entry naming the PR and flip `CURRENT.md`, or the claim reverts to "held."** This document now says
   *reported ruled, UNREGISTERED* — §6.3 is written so that it holds either way.
2. **ED-IN-0123's ledger entry asserts two claims this document retracts** — "four PATH-LITERAL
   escapes" (it was ten) and "the MB Track-F failure set is NON-DETERMINISTIC" (it is not; the constant
   +1 is a documented local-vs-CI skip). Append-only is correct, but with no follow-up entry an auditor
   reading by ED gets the retracted claims as current. **ED-IN-0124 files those corrections.**

---

## 11. Where this plan is most likely wrong

1. **Stage 0 may be larger than the fork.** Getting 25 modules to `live` is most of building the game.
   *Settling measurement:* size step 4 against the rank 0-1 modules, then extrapolate from actuals —
   and extrapolate from **corrected** denominators (§3), not the manifest's.
2. **Step 4 may be architecture, not plumbing** (§7.2). *Settling measurement:* the one-site trial,
   before the sweep.
3. **The 5 prose-authoritative modules may encode intent the code never implemented.**
   *Settling measurement:* per module, diff prose-declared `emits`/`consumes` against code.
4. **`build_fork.py`'s carry/leave list may be stale**, since it predates the ED-MB-0043 question. It is
   now load-bearing as step 1. *Settling measurement:* `--verify-only` on a clean checkout, and read its
   carry list against §6.3 before trusting it.
5. **The inversion may be slower than hand-transcription for the first two tables**, which is the honest
   case against §5. *Settling measurement:* time `key_types` end-to-end; if the cook step costs more
   than the drift it prevents on one table, stop at one and re-argue.

---

## 12. Why the previous drafts failed — recorded because it recurs

Two drafts, one failure mode, now instanced **nine more times** by an independent pass (§0).

- **v1 (2026-08-02)** proposed building a per-subsystem manifest **that already existed**, along with
  the headline finding, the character-layer gap and the violated save/replay premise. It reported "14
  homeless modules" by reading `subsystem: null` — six of those rows name a `doc:` **one field over**.
  The real number was 8; a decision rested on a figure inflated 1.75×.
- **v2 (2026-08-03)** fixed those, then wrote a prose plan around a fork-assembly tool it never
  discovered (`build_fork.py`), mislabelled `no_code_declared` as "no code" for units holding two whole
  engines, and reported a `citation` field as absent while the JSON published `cited: 84`.

**Every instance is a false absence derived from a proxy** — reading a field name instead of the field,
a label instead of the trace, a summary instead of the tool. v1's own §9 warned against exactly that,
by name, and the document containing the warning committed the error twice; v2 inherited the warning
and committed it four more times.

The operative rule, stated as a procedure because the principle demonstrably does not transfer:

> **Before asserting that something does not exist, run a positive control — search for something you
> know exists, by the same method — and only then report the absence.**

A rule that is stated but not executed is a rule that will be broken by the person who stated it. The
structural answer, and the reason §7 leads with running a tool rather than reading a manifest: **prefer
an instrument over an assertion at every step where one exists.** Every error above was cheap to check
and expensive to have acted on.
