# Execution order — the return to the game, as steps a session can perform

## Status: PROPOSED — **merging this PR RATIFIES the step ordering** (ED-1094, and the flip is co-located here rather than left to an unprompted follow-up, which is the failure ED-1083 recorded). Two items are **HELD** for explicit sign-off and are named in §4: **Q4** (S5's disposition of `test_gate_coverage.py`) and **S2 Half B's provisional `score/2` wiring**, which reads a roster Q1 has not ruled on. Execution order requested by Jordan, 2026-08-21.

## Date: 2026-08-21 · Lane: IN (cross-cutting) · ED: none allocated

**What this is.** `proposals/2026-08-20-return-to-game-plan-v1.md` is the plan of record and stays
the authority on *what* the acts are and *why*. This document is the **order they run in and the
instructions for running them**, rewritten after a read-only adversarial review of PRs #322/#323/#324
found the most recent commit's headline claim to be false. It **supersedes §5 (Sequencing summary)
of the 2026-08-20 plan and nothing else.** Every act below is that plan's act, renumbered by
executability rather than by value.

No ED row is filed. Under `CLAUDE.md` §0 as amended 2026-08-19 a row is warranted only when it
requires a human decision; this document's decision requests are §4, addressed to Jordan here.

---

## 0. If you are a session with no memory, read this section and then §2's first `state: next` step

**Your work is one step.** Take the first step in §2 whose `state:` is `next`. Do that step, run its
gate, commit, update its `state:` to `done` with the evidence line, and stop. Do not read ahead and
do not "also fix" what you notice on the way — §1 explains why that instruction is load-bearing
rather than merely tidy.

**This file is not a queue that runs itself.** There is no driver, no chaining, no wake-up. A prior
program in this repository (`workplans/return_to_game_queue.yaml`) instructed memoryless sessions to
execute it unattended and had to be shut down for exactly that. `CLAUDE.md` §11 forbids a session
arming its own wake-up and the deny-list is CI-enforced. The chain here is one word from Jordan.

**The three things that will make you do the wrong work.** They are listed here because each one has
already happened in this repository, more than once:

1. **You will find an apparatus defect and want to guard it.** `CLAUDE.md` §0.1 pt 5 as amended:
   a pattern defect earns a guard only if the defective artifact is load-bearing on *the game* or on
   *a Jordan decision*. If it is load-bearing only on this repo's process — fix it here, or drop it.
   Do not file it. Filing it is the reroute, not the compromise.
2. **You will want to write the finding down.** The adversarial pass is a stage, not a deliverable.
   Its output is edits to the thing under review plus at most one paragraph in the commit message.
   At most one ledger row, only if it needs a ruling (`needs_jordan: true`).
3. **You will be tempted to mark a step done because the document says so.** `CLAUDE.md` §0.2: done
   means the behaviour executes. Every gate in §2 is a command with an observable result. Run it.
   Paste its output into the evidence line. A gate you did not run is a step you did not do.

---

## 1. The ordering thesis — read before proposing a different order

Four constraints produced this order, and a reordering that violates any of them will stall.

**(a) A false claim on `main` outranks a missing feature.** S1 exists because `1e4c6f4` shipped a
docstring, a commit message and a plan row all asserting that `references/descriptor_registry.yaml`
was load-bearing at runtime, and it was not. Every step after it cites that premise. Correcting a
statement the tree makes about itself is cheaper the earlier it happens and compounds if it does not.

**(b) The next step must be executable in THIS repository.** The 2026-08-20 plan puts Act B — turn
`valoria-game`'s CI green — third. That work is real and necessary, and a session started from the
SessionStart banner cannot begin it: this repository's GitHub scope is `jordanelias/ttrpg`, and the
game clone must be attached before a single line of it can be read. Any order that puts an
unreachable step early converts a working session into a blocked one. Cross-repo work is S6, and S6
opens by attaching the repo.

**(c) Something must move `0/7` before more architecture lands.** Thirteen commits have landed since
the last one that changed how the game plays (#311). `CLAUDE.md` §0.3 declares the empty banner a
running experiment whose method is *change nothing else and watch one session*; one session has now
run and it wrote 1,022 lines of apparatus and zero lines of game. S2 is the game commit, and it is
second rather than fourth because the experiment needs a data point in the other direction more than
the architecture needs another week.

**(d) Cull by DEPENDENCY, not by phase — corrected 2026-08-21 on Jordan's ruling
("we can't break out of recursion without culling").** The first draft of this document put every
cull last, inheriting "cull last" wholesale from the culling plan's own sequencing. That was wrong,
and measuring it showed why: the waves are not one thing. **Wave 5 — untracking generated data,
~126,000 lines — is independent of every architectural step here**, because nothing in `engine/` or
`systems/` reads any of it. It is also the wave that most directly attacks the loop, which is the
part the phase-ordering obscured: this session added *one* document to `proposals/` and thereby
churned the glossary, the test register and the identifier census, and failed a blocking gate on the
glossary. That is the generator running on generated data, and no amount of doctrine reaches it.
So Wave 5 is now **S2**, ahead of the game work.

What genuinely must wait is narrower than "culling": Waves 1, 2, 3 and 6 touch apparatus that S5
(contracts-as-registration) rewires, and collapsing guard tiers before S5 has settled what dispatches
what is how the previous eight consolidation plans failed. Those stay late, at S6.

---

## 2. The steps

Each step carries: the goal it serves, its precondition, the exact files, the change, an executable
gate, the commit subject, and an explicit do-not. Sizes are the reviewer's estimate of the diff, not
a budget to fill.

---

### S1 — Make the claim on `main` true · `state: done` (2026-08-21)

**Goals served:** 3 (engine/references commensurate), 5 (gate depth).

**What was wrong.** `engine/substrate/descriptors.py:assert_faction_roster_is_covered` iterated
`FACTION_FIELD_MAP` — the artifact's copy of `FACTION_KEY_TO_FIELD`, a five-row dict hand-maintained
at `tools/export_descriptors.py:64` — and never `FACTION_STATS`, the registry-derived half. A
registry edit does not touch that dict, so the documented behaviour ("add a stat to the registry
without adding its field and the engine stops importing") could not occur. The repository's own
falsifier, `test_the_roster_check_can_actually_fail`, planted its failure in the same hand-maintained
dict, so it proved the function raises when handed a bad map and could not observe the claim being
false. `CLAUDE.md` §0.1 pt 2 applied one layer below the claim, green throughout.

**What landed.**
- `engine/substrate/descriptors.py` — the check is now two-stage over `FACTION_STATS`: stage 1 fails
  when a registry key is bound to no field, stage 2 when a bound field is not implemented. It returns
  the number of *registry* stats verified. The one-way property is now structural rather than
  incidental: the function never enumerates `implemented_fields`, only registry keys, so `L` cannot
  reach either stage and Jordan's open ruling stays Jordan's.
- `tests/valoria/test_descriptors_runtime.py` — the falsifier plants its failure in `FACTION_STATS`;
  a second test covers stage 2; and `test_a_registry_edit_breaks_the_engine_end_to_end` runs the real
  `tools/export_descriptors.py` over a doctored copy of the real registry and asserts the real check
  refuses it. That third test is the only one that would have caught this from a cold read.
- `tests/valoria/test_engine_does_not_import_systems.py` — `NESTED_BASELINE = 16` added beside
  `BASELINE_TOTAL = 5`. The top-level ratchet counted column-0 imports only, so the cheapest way to
  lower it was to indent an import into the function that used it: the metric read as progress while
  the cycle got harder to see. Counting both makes that move net-zero.
- `proposals/2026-08-20-return-to-game-plan-v1.md` — C2 marked **PARTIAL**; the three hardcoded twins
  are named as outstanding.

**Evidence (run, not asserted).**
```
$ python3 scratch/falsify.py          # fac.zeal added to a registry copy, real exporter, real check
  RESULT: assert RAISED — descriptor_registry.yaml declares faction stat(s) that nothing binds …
$ pytest tests/valoria/test_descriptors_runtime.py -q                    9 passed
$ pytest tests/valoria/test_engine_does_not_import_systems.py -q         7 passed
mutation, old map-driven check restored:   2 failed (both new falsifiers)  ← they kill the defect
mutation, one top-level import indented:   2 failed — "FELL 5 -> 4" AND "ROSE 16 -> 17"
```

**Residual, deliberately not closed here:** the runtime footprint of `references/` is still
`set.order`'s two bounds in `echo_transport.py`. `MULTS`, `ALL_PLAYABLE_15` and `STARTING_STATS`
remain hardcoded twins in `game_state.py`. That is C2's remaining two thirds and it belongs to S4.

---

### S2 — Untrack the generated data · `state: next` · culling Wave 5, ~126,000 lines

**Goals served:** the loop itself. This is the cull Jordan named as the precondition, and it is the
one with no architectural dependency.

**Precondition:** none. Nothing under `engine/` or `systems/` reads any target.

**Measured 2026-08-21, current tree:**

| target | lines | generator |
|---|---:|---|
| `references/glossary/` (21 files) | 75,829 | `tools/observability/build_glossary.py` |
| `systems/*/_identifier_census.yaml` (15) | 26,292 | `tools/build_identifier_census.py` |
| `references/test_register.json` | 12,638 | `tools/build_test_register.py` |
| `references/key_graph.json` | 2,840 | `tools/build_key_graph.py` |
| `references/execution_map.json` + `EXECUTION_MAP.md` + `execution_trace.json` | 2,675 | `tools/build_execution_map.py` |
| `engine_atlas.json` + `ENGINE_ATLAS.md`, `CONTRACT_INDEX.md`, `KEY_INDEX.md`, `definitions.yaml`, the 4 vocab views, `identifier_census.json` | ~6,000 | five builders |

**Why this is the cull that counts, stated as evidence rather than as a principle.** Adding one
477-line document to `proposals/` in the S1 commit regenerated three of these indexes, produced ~200
lines of diff churn in files no human wrote, and turned `pytest tests/valoria` red on
`test_build_glossary` until the glossary was rebuilt. The culling plan records the same failure twice
more: two sibling branches collided on 18 files "over nothing", every conflict a generated file and
zero in source; and three times in one session an edit to *prose* staled `engine_atlas.json` and
failed a blocking gate — once because the word "audit" appeared one more time in a comment.

**The gate flip this requires, and it is the whole of the work.** Several freshness checks operate by
diffing the *committed* copy against a fresh build (`vocab_store --check`, `definitions_store
--check`, `test_engine_atlas`, `test_test_register`, `test_build_glossary`,
`build_identifier_census --check`). Untracking means flipping each to **build in CI, do not diff a
committed copy**. One deliberate pass, gate by gate — **not a silent `git rm`**. A gate left diffing
an untracked file fails permanently and gets deleted by the next session, which loses the check.

**Two hard gates from the culling plan §5 bind here.**
1. **`engine/engine_params/params_tables.yaml` is NOT regenerable** — its 43 source docs were
   evacuated and `export_params_constants.py` exists nowhere in the tree. It is a **source, not an
   artifact**. KEEP TRACKED, excluded from this wave. (S6 pins it.)
2. **`validate_ed_citations.py:368` reads the identifier census.** Detach it or confirm it degrades
   safely before untracking `identifier_census.json`, or every valid `ED-` citation risks reading as
   fabricated.

**Gate.**
```
git ls-files | xargs wc -l | tail -1        # tracked-line total falls by ~126,000
python3 -m pytest tests/valoria -q          # green with NO generated file committed
touch a new proposals/*.md, run the suite   # no generated-file churn, no red gate
```
The third line is the falsifier: the defect being removed is *prose edit churns generated data*, so
the test is a prose edit that does not.

**Commit:** `[cleanup] Culling wave 5: untrack generated data, and flip the freshness gates to build-in-CI (ED-IN-0194)`

**Do not:** untrack `params_tables.yaml`; `git rm` without flipping the paired gate in the same
commit; or extend this into Waves 1/2/3/6, which S5 rewires.

---

### S3 — Move M1 juncture 1 · `state: after S2`

**Goals served:** the deliverable. This is the only step here that can change `0/7`.

**Precondition:** none. Both halves are named in the SessionStart banner and neither has been touched.

**Half A — fractional dice pools. This is a two-line change with a measured golden delta.**

`engine/autoload/sigma_leverage.py:284`, inside `roll_net_continuous`:

```python
effective_pool = max(1, int(round(pool)))       # ← the defect
return dice_engine.continuous_engine_sample(pool=float(effective_pool), tn=tn, rng=rng)
```

`dice_engine.continuous_engine_sample` **already accepts a fractional pool** — its docstring says
so at `dice_engine.py:92` ("Pool may be fractional (enables fractional Ob / TN modifiers)") and its
body does `mean = mu * pool; std = sigma * math.sqrt(pool)` with no rounding. The rounding is
imposed by the caller alone. Replace it with a pool **floor** that preserves canon and drops the
quantisation:

```python
effective_pool = max(1.0, float(pool))         # [canonical: params/core.md §Pool Floor (all systems)]
```

- **Do not touch `roll_net` at line 273.** That is the *discrete* d10 path; whole dice are correct
  there and `int(round())` stays.
- `systems/factions/sim/faction_action.py:_successes` carries a docstring that currently states this
  gap as unfixed and names it "worse than an unimplemented feature, because the call site asserted
  the opposite". Rewrite that paragraph to describe what the code now does. Leave the ED-IN-0187
  citation.
- **The goldens will move, and that is the measurement.** Under §0.1 pt 4 a number without a control
  is not a measurement: record the before and after of the seeded campaign goldens in the commit
  message, and say which direction and by how much. Re-record only after you can explain the sign.

**Half B — the `score/2` obstacle derivation. Do not begin by writing code.**

Jordan ruled 2026-08-14 that an obstacle rolled against a character or faction is *"their
corresponding score/2 plus whatever specific modifiers exist"*. `dice_engine.py:118-123` records the
ruling; `tools/export_descriptors.py`'s own audit records it as wired **nowhere**.

The FA surface has exactly two obstacle sites today, both fixed literals:
`faction_action.py:540` (`ob = 1`, Muster) and `:562` (`ob = 2`, Govern). **Neither is obviously in
scope**, because both are rolls against the world rather than against an opposing faction, and the
ruling's antecedent is "rolled against a character or faction". So the first deliverable of Half B is
a classification, not an edit:

1. Enumerate every FA action resolver and label each **opposed** (the roll's difficulty derives from
   a specific target faction or character) or **unopposed** (fixed difficulty).
2. Wire `score/2 + modifiers` into the opposed set only, reading the score from the roster
   `engine/autoload/game_state.py:Faction` actually implements — the six-field one. This is
   **provisional** and the banner authorises it: Q1 gates which roster is canonical, not the
   arithmetic.
3. Leave the unopposed set's literals alone and record the classification in the commit message. If
   the opposed set turns out to be empty, **say so and stop** — that is a real finding and it
   converts Half B into a question for Jordan rather than a code change.

**Two sites you must not touch.**
- `systems/combat/combat_engine_v1/core.py:77` — the personal-combat obstacle is a declared HOLD.
  It rolls against a fixed `DECISIVE_OB = 3` and carries opposition in `net_sigma`; deriving Ob from
  the defender moves band placement, which is entangled with the guandao/plate collision the same
  docstring records as Jordan's to resolve. `tests/valoria/test_degree_ladder_single_owner.py`
  records the hold.
- `sigma_leverage.degree` — the second declared hold (ED-IN-0187). Do not unify it here.

**Gate.**
```
python3 -m pytest tests/valoria -q                       # must be green
python3 -m pytest engine/tests -q                        # goldens: expect movement from Half A
python3 tools/m1_acceptance.py --summary                 # record the verdict before and after
```
Plus, and this is the row that matters: a seeded FA probe whose recorded outcome **differs** from the
same seed on `1e4c6f4`, with the delta explained. If nothing differs, Half A did not take effect.

**Commit:** `[simulation] M1 juncture 1: fractional pools reach the sampler, and the FA obstacle surface classified (ED-IN-0187)`

**Do not:** re-record a golden you cannot explain; add a guard for either change (both are game
subjects, so a guard is *permitted* — but neither is a pattern defect, and §0.1 pt 5 asks for a
pattern before a guard); or mark juncture 1 `done` on the board. S3 is what makes `done` mean
anything.

**Size:** Half A ~15 lines plus golden re-records. Half B unknown until the classification exists;
if it exceeds ~150 lines, stop and split.

---

### S4 — Give each juncture an execution artifact · `state: blocked-by S3`

**Goals served:** 4 (guardrails that can observe what they guard).

**Why.** `tools/m1_acceptance.py` row 4 — the row that aggregates "all seven junctures execute" —
counts `state: done` strings in `workplans/workplan_v6_progress.yaml`, a hand-edited board. Seven
one-word edits green it. The gate declares this itself, in its own output, unprompted
(`⚠ DOC-DERIVED`), which is the honest failure mode. But `review_core.py:114-115` carries
`m1.acceptance` into the **required** compliance CI job, so those seven word-edits also drive a
required ratchet from 2 failing rows to 1. That makes row 4 the one place left where prose moves a
hard gate — inside the gate whose purpose is to stop prose moving gates.

**What to build.** Follow rows 1 and 2, which are already execution-bound and cannot be written into
passing: row 1 runs a seeded `mc_v18` probe season and counts `stub_resolve` calls; row 2 runs the
same seed twice and compares `KeyLog.content_hash()`. Give each of the seven junctures one artifact
of that kind — a seeded run, a key-log hash, an emitted key, a probe result. Replace the string count
with the conjunction of the seven.

**Expect immediate greens, and do not suppress them.** Five of M1's seven junctures have real
implementations in `valoria-game` while the board scores 0/7. Both facts are true at once and
`CLAUDE.md` §0.2 names that contradiction a **board defect, not a work item**. A juncture that greens
the moment it is measured was always done; recording that is the point.

**Gate.** `python3 tools/m1_acceptance.py --summary` prints no `DOC-DERIVED` line, **and** editing
any `state:` in `workplan_v6_progress.yaml` changes no row's verdict. Demonstrate the second one by
editing the board, re-running, showing no change, and reverting.

**Commit:** `[infrastructure] M1 acceptance row 4 becomes execution-bound (CLAUDE.md §0.2)`

**Do not:** tighten the board, add a guard on the board, or delete row 4. The row is right; its
input is wrong.

---

### S5 — Contracts as the registration table · `state: blocked-by S4`

**Goals served:** 1 (engine → systems direction), 3 (commensurate), 6 (central definition → modular
apparatus). This is the highest-leverage step in the programme and the one that most repays care.

**The 2026-08-20 plan's C3 says "move seams to registration-driven composition" without naming the
registration source.** That is an invitation to invent one, and this repository does not need a new
registry. It has `references/module_contracts.yaml`: 27 modules, read by 30 tools, read at runtime by
**nothing**.

**The change.**
1. `tools/export_contracts.py` cooks `module_contracts.yaml` → `engine/engine_params/contracts.json`,
   with a blocking `--check`. Fifth instance of a pattern with four working precedents — copy
   `export_descriptors.py`'s shape, including its habit of *recording* what it cannot resolve rather
   than closing it.
2. `engine/substrate/contracts.py` is the sole runtime reader. stdlib only, a true leaf, reads the
   cooked artifact and never the YAML — the same discipline as `keys.py` vs `key_types.json` and
   `descriptors.py` vs `descriptors.json`.
3. `engine/cross_scale/scene_dispatch.py` dispatches by **registered resolver name** instead of its
   hardcoded per-subsystem branches (currently `:233-352`, including four function-local
   `systems.*` imports at `:273,287,351,352`).
4. Each `systems/<sub>/sim/` module registers itself against its contract entry.

**What this closes at once.** The remaining engine→systems seams invert, because `engine/` names a
table rather than a subsystem. `references/` becomes load-bearing on *dispatch* rather than on two
integers. The three-file tax — the coordinated edits to `game_state.py:368-420`,
`scene_dispatch.py:233-352` and `mc_v18.py:37-38` that adding any subsystem currently requires —
collapses to one registry row. And the 10 `doc: null` and 11 `[ASSUMPTION]`-grade contracts stop
being documentation debt and become runtime debt, which is the only kind this repository reliably
pays.

**It needs no new guard, and this is a design property rather than an economy.** A subsystem missing
from the table does not dispatch. The registry *is* the check. If you find yourself writing
`test_every_subsystem_is_registered`, the registration is not actually driving anything and you have
built a parallel index — stop and re-read step 3.

**Sequencing inside S4.** Land the exporter and reader first, with nothing consuming them, and prove
`--check` round-trips. Then convert dispatch one subsystem at a time, running `engine/tests` after
each. Goldens must not move — this is a mechanism change, not a behaviour change, and unmoved
goldens are the control that says so.

**Also finish C2 here**, since the twins and the dispatch table are the same problem: delete `MULTS`,
`ALL_PLAYABLE_15` and `STARTING_STATS` from `game_state.py` in favour of the cooked artifacts.
Wiring the registry's per-stat floors into `Faction.adjust` (ratified 2026-07-08 as ED-IN-0029,
never implemented, currently a blanket 0.5/7.0 over 32 call sites) **moves goldens** — give it its
own commit with the delta measured, exactly as `descriptors.py`'s docstring already says.

**Gate.**
```
grep -rE "^(from|import)\s+systems[.\s]" engine --include=*.py | grep -v engine/tests   # empty
python3 -m pytest tests/valoria/test_engine_does_not_import_systems.py -q  # BASELINE_TOTAL 5 -> 0
                                                                          # NESTED_BASELINE below 16
python3 -m pytest engine/tests -q            # unmoved, except the floors commit
python3 tools/export_contracts.py --check
```
When `BASELINE_TOTAL` reaches 0, delete `test_the_documented_cycle_is_still_real` **and correct
`CLAUDE.md` §3's "acyclic, autoload is a leaf" in the same commit** — that test exists to stop §3
being restored while the code contradicts it, and it is the only thing holding the correction.

**Commit:** `[infrastructure] Act C3: module_contracts.yaml becomes the dispatch registry`

**Size:** large. Expect several commits. Split at subsystem boundaries, never mid-conversion.

---

### S6 — Collapse the L3 rungs, run the dependent cull waves, and pin what is actually read · `state: blocked-by S5`

**Goals served:** 5 (gates at L2 at the deepest), 4, and the rest of the cull.

**This step now carries culling Waves 1, 2 and 6** (`2026-08-18-culling-plan-v1.md`, RATIFIED,
ED-IN-0194) — the ones that had to wait, because each removes apparatus that S5 rewires. Wave 5 ran
at S2. Their order inside this step is the culling plan's own, which was adjudicated and should not
be re-derived: **6b (tombstones) before 6a**, then Wave 1 (leaves), then Wave 2 (meta-gates, orphaned
by wave 1), then 6f, then 6c. **Wave 3 does not run** — see §4.

**Wave 4 (`audit/` → fork ref) is mostly already done, and what remains is not a cull.** Measured
2026-08-21: **16 of the 17 units the plan marks "delete outright, no extraction" are already gone**,
taken by #323's −97,454-line commit; the residue of that set is 1,870 lines. `audit/` still holds
79,085 lines, and that is almost entirely the **~33 game-subject working papers the plan requires to
be EXTRACTED first** — their surviving conclusions belong in `systems/` heads or `proposals/`, the
workings do not. That is authorship work on game subjects, not removal, and it should be scheduled as
such rather than as a wave. One blocker the plan names is already clear:
`tests/valoria/test_fork_divergence.py`, which imported from `audit/`, was deleted in `4ab18df`.

Measured 2026-08-20: 72 of 170 files in `tests/valoria` take a tool as their subject; 11 of 74 tools
take another tool as theirs. The deepest rungs are the three files `CLAUDE.md` §0.1 pt 5 already
names as forbidden — and all three are still present, and `test_gate_coverage.py` gained a row in
*both* of the commits that were supposed to end the loop, including the one that wrote the
prohibition. Either the doctrine names the wrong file or those commits violated it twice; leaving the
contradiction is worse than either resolution.

**The disposition, which needs Jordan's confirmation (§4):**
- `test_gate_coverage.py` — **narrow, do not delete.** Four of its rows cover the `export_*.py
  --check` round-trips that produce the Godot bridge, so it is transitively load-bearing on the game
  and wholesale deletion could let an export silently fall out of CI. Keep those four rows, drop the
  rest, and amend §0.1 pt 5 to name the narrowed file as *kept* with the reason.
- `test_wf_harness_check.py`, `test_blocking_tier_is_honest.py` — **delete.** Guard-of-guard with no
  path to the game.
- **Pin `engine/engine_params/params_tables.yaml`.** Two engine modules read it
  (`sigma_leverage.py`, `dice_engine.py`) and its generator was retired with `engine/params/`, so it
  is hand-edit-only with no integrity check — while three artifacts nobody reads
  (`game_constants.json`, `sim_params.json`, `value_pointer_links.json`) each have a blocking one.
  The protection is inverted relative to consumption; a content hash pinned in CI is enough.

**Gate.** No file in `tests/valoria` takes a test or a guard as its subject; `params_tables.yaml`
has an integrity check that fails on a hand edit — demonstrate it by making one.

**Commit:** `[cleanup] Collapse the guard tiers to L2 and pin the artifact the engine actually reads`

---

### S7 — Cross the repo boundary · `state: blocked-by S6, and by attaching the repo`

**Goals served:** 4, 3.

**Open by attaching `jordanelias/valoria-game`.** It is not in this session's scope by default and
nothing below can be read, let alone verified, until it is. Everything this repository records about
it is second-hand — including everything in this document.

Then, in order: finish **PP-665** (12 live `maret_vossen` sites named at §1.D1 of the 2026-08-20
plan) so `godot-ci.yml` goes green for the first time since 2026-05-04 **and the Solmund naming step
executes even once** — it has been SKIPPED behind a failing Yrsa step for months, so a gate nobody
has ever seen run is about to run; expect it to fail and budget for that. Then harden the compile
ratchet to compare error **sets** rather than counts. Then land
`valoria-game/tools/check_constants_parity.py`, the reader half of `game_constants.json`, so the
export bridge acquires its first consumer and the ~90 hand-transcribed constants in
`systems/util/Constants.gd` acquire a comparer.

**Gate.** `godot-ci.yml` green on `main`; the game reads its first `.json` from `engine_params/`;
the divergence list is red on a `KNOWN_DIVERGENT` set that can only shrink.

---

### S8 — Act D, and Act E's residue · `state: blocked-by S7`

Unchanged from the 2026-08-20 plan, **including its two corrections**: merge the `ci_names_check`
facade but leave `ci_names_consistency` standalone (D2), and D4 is struck — `broken_dependency_checker`
absorbing `freshness_gate` is aggregation, not §8 consolidation. Fix FORK **semantics** before
porting call sites (D1): three sites currently give three different answers about the same ledger row,
and `pathres.resolve(max_hops=1)` does not reproduce `bdc`'s `FORK:<ref>:<ref>` pairing format that
`bdc`'s caller checks, so a drop-in port silently changes output.

**Act E has no waves left to run here.** Wave 5 ran at S2; Waves 1, 2 and 6 ran at S6; Wave 4's
delete-outright set is already gone and its extraction half is authorship work on game subjects, to
be scheduled on its own; **Wave 3 does not run at all** without the ruling in §4. What remains under
Act E is the residue: confirming the culling plan's §5 hard gates all held, and closing
`registers/editorial_ledger_in.jsonl`'s ~108-token headroom problem (ED-IN-0185 Q5, overdue), which
currently means **no lane can file a ledger row at all**.

---

## 3. What this order deliberately does not do

- **It does not add a step for the review that produced it.** No `test_plan_compliance`, no progress
  register for the steps, no findings document. §0.1 pt 5 forbids the first two and §0 forbids the
  third. The `state:` fields in §2 are the whole bookkeeping surface and they are edited in place.
- **It does not re-litigate the diagnosis.** `proposals/2026-08-18-breaking-the-recursion.md` is
  still the causal account and the amendments in `CLAUDE.md` §0/§0.1/§0.2/§0.3 are live doctrine.
  The review behind this document confirmed the mechanism and disputed only whether the fix had
  reached the game yet.
- **It does not treat the apparatus as the enemy.** The export discipline — authored surface, one
  exporter, cooked artifact, single runtime reader, blocking round-trip — is correct and S4 adds a
  fifth instance of it. The failure mode this order guards against is not building apparatus; it is
  building apparatus that terminates in nothing, and every gate above asks what consumes the thing.

---

## 4. Rulings that gate steps

| Q | Question | Blocks | Where the evidence is |
|---|---|---|---|
| **Q1** | **The faction-stats roster.** Five surfaces disagree; `L` is written by 32 `.adjust()` call sites and declared nowhere in the registry. Is Legitimacy a base faction descriptor or derived like Mandate? | S2 Half B's final form; S4's roster deletion; S6's divergence list. **S2 proceeds provisionally against the coded six-field roster** — the banner authorises this. | `HANDOFF.md:209+`; ED-FA-0004 |
| **Q1b** | **The ratified floors nobody implemented.** ED-IN-0029 (2026-07-08) floored Influence at 1 and the rest at 0. `Faction.adjust` has applied a blanket 0.5/7.0 ever since and no caller overrides it. Wire them, with the golden delta measured? | S4's final commit | `export_descriptors.py` `unimplemented.per_stat_floors` |
| **Q2** | **Name the tenth attribute.** You ruled ten on 2026-08-14; the registry ships nine, and `Constants.gd:28` already declares `ATTRIBUTE_COUNT = 10`. The game is ahead of canon. | closing the `pending_tenth` sentinel | `CLAUDE.md` §5 |
| **Q3** | **Godot 4.3 or 4.6?** `project.godot:11` and CI pin 4.3; `CLAUDE.md` and `godot/` say 4.6. | what the compile ratchet's 84 means | 2026-08-20 plan §1.D5 |
| **Q4** | **S5's disposition.** Narrow `test_gate_coverage.py` to the four export round-trips and amend §0.1 pt 5 to name it as kept — or delete it and accept that local-green can drift from CI-green? | S5 | §2 S5 |
| **Q5** | `registers/editorial_ledger_in.jsonl:50-51` — two rows share id `ED-IN-0194` with conflicting `needs_jordan`. Reported 2026-08-19, unruled. | ledger integrity | — |
| **Q6 — HOW DEEP DOES THE CULL GO (a)?** `tools/ci_claim_provenance_check.py` and `tools/ci_vacuous_assertion_check.py` are **literal encodings of `CLAUDE.md` §0.1 points 3 and 2**. By this repository's own load-bearing predicate they are recursive — they audit ledger prose and test code, not the game — and two independent lenses flagged them. But **if they go, §0.1 must be struck in the same commit** rather than left pointing at deleted guards. Delete both and amend §0.1, or keep both and record the exemption? | culling plan §5 gate 6; the depth of S6 | `2026-08-18-culling-plan-v1.md` §5.6 — **held for you since 2026-08-18** |
| **Q7 — HOW DEEP DOES THE CULL GO (b)?** **Wave 3 ends structurally-independent adversarial review.** `.claude/wf_*.js` + `.claude/agents/valoria-critic.md` are layer 4 by the rule and should be deleted — and they are the mechanism that caught four errors in the culling-plan session's own work, and the read-only critic posture that caught the falsified load-bearing claim in S1. **The rule says delete; the evidence says it works.** | Wave 3, which is otherwise held indefinitely | `2026-08-18-culling-plan-v1.md` §5.7 — **held for you since 2026-08-18** |

**Q6 and Q7 are the two that gate how much of the recursion actually gets removed**, and both have
been held since 2026-08-18 without a ruling. Everything else in the cull can proceed without them;
neither the guards in Q6 nor the review apparatus in Q7 can be touched until they are answered.

Q4, Q6 and Q7 are named here. Q1, Q1b, Q2, Q3 and Q5 are the 2026-08-20 plan's §7 queue, unchanged and still open;
its Q4 (ED-SC-0003/0004/0005) and Q8/Q9 (`accord_range`, `coherence_bands`) gate junctures and port
semantics that no step above reaches, and stay queued there rather than being restated here.

---

## 5. Provenance

Produced 2026-08-21 from a read-only adversarial review of `c9b0a86`, `4ab18df` and `1e4c6f4`
(PRs #322, #323, #324) against the working tree at `1e4c6f4`. Seven findings; the two that changed
this order are the falsified load-bearing claim (S1) and the ratchet's inverted incentive (S1). The
measurements behind §1(c) — line deltas per commit, the count of commits since the last
behaviour-changing one, and the 72/170 and 5-vs-16 seam counts — were taken on that checkout and are
reproducible from it.

Supersedes **§5 of `proposals/2026-08-20-return-to-game-plan-v1.md` only**. That document remains the
authority on what each act is and why, and its §1 findings tables are the evidence base this order
assumes.
