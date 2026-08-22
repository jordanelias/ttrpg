# Execution order — the return to the game, as steps a session can perform

## Status: PROPOSED — **merging this PR RATIFIES the step ordering** (ED-1094, and the flip is co-located here rather than left to an unprompted follow-up, which is the failure ED-1083 recorded). Two items are **HELD** for explicit sign-off and are named in §5: **S3 ends the §0.3 banner experiment** (Wave 3 deletes `session_status.py`, which *is* the banner — Jordan's 2026-08-21 ruling governs, but the experiment ends rather than pauses), and **S8 Half B's provisional `score/2` wiring**, which reads a roster Q1 has not ruled on. Execution order requested by Jordan, 2026-08-21.

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

## 0. If you are a session with no memory, read this section and then §3's first `state: next` step

### THE BOARD — current as of 2026-08-22. If this table and a step's own `state:` disagree, the step wins.

| step | state | subject | layer |
|---|---|---|---|
| S1 make the load-bearing claim true | **done** 2026-08-21 | descriptor roster → engine | L1 |
| S2 culling waves 1+2 | **done** 2026-08-21 | apparatus removal | — |
| S3 wave 3 + green the suite | **done** 2026-08-21 | apparatus removal | — |
| S4 wave 5, untrack the generated layer | **done** 2026-08-22 `f84692c` | apparatus removal | — |
| **S5 contracts-as-registration** | **NEXT** | **the engine** | **L0** |
| S6 wave 6 + FORK semantics + ledger cap | blocked-by S5 | apparatus + provenance | — |
| S7 wave 4's residue: extraction | blocked-by S6 | audit corpus | — |
| S8 M1 juncture 1 | half-done; **Half B SUSPENDED** by Jordan | **the engine** | **L0** |
| S9 cross-repo residue | blocked-by attaching `jordanelias/valoria-game` | port | — |
| S10 errors become numbers | **unblocked**, not gating | **the engine** | **L0** |

**Take S5.** It is the first step in the rail whose subject is the game rather than the apparatus,
and the whole cull existed to get here. S10 is unblocked and may be taken if Jordan directs it, but
**do not take it ahead of S5 or S8 by rail-default** — it does not move `0/7`.

**The depth rule binds every step, including any you invent.** §3a rules the tooling at **three
layers** — L0 grow · L1 harden · L2 cap · **L3 never** — and
`references/ci_checks_registry.yaml` carries `layer:` and `posture:` on every row so you meet the
model where the tools are declared. Before you add any gate, tool, or test, name its layer. If the
answer is L3 — if its subject is another guard — you have found the loop `CLAUDE.md` §0.3 diagnoses,
and the answer is no.

**Your work is one step.** Take the first step in §3 whose `state:` is `next`. Do that step, run its
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
   means the behaviour executes. Every gate in §3 is a command with an observable result. Run it.
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
unreachable step early converts a working session into a blocked one. Cross-repo work is **S9**, and it
opens by attaching the repo.

**(c) Something must move `0/7` before more architecture lands.** Thirteen commits have landed since
the last one that changed how the game plays (#311). `CLAUDE.md` §0.3 declares the empty banner a
running experiment whose method is *change nothing else and watch one session*; one session has now
run and it wrote 1,022 lines of apparatus and zero lines of game. **S8 is the game commit**, and it is
marked unblocked throughout rather than queued behind the architecture, because the experiment needs a
data point in the other direction more than the architecture needs another week.

⚠ **This constraint is NOT yet satisfied, and saying so is the point of writing it down.** S1, S2 and
S3 have all landed and none of them changed how the game plays; `0/7` is unmoved. S8 is a two-line
change to `sigma_leverage.py:284` plus a classification, and it has been available since S3 greened
the suite. If the next session takes S4 instead, that is a choice, not a dependency.

**(d) Cull by DEPENDENCY, not by phase — corrected 2026-08-21 on Jordan's ruling
("we can't break out of recursion without culling").** The first draft of this document put every
cull last, inheriting "cull last" wholesale from the culling plan's own sequencing. That was wrong,
and measuring it showed why: the waves are not one thing. **Wave 5 — untracking generated data,
~126,000 lines — is independent of every architectural step here**, because nothing in `engine/` or
`systems/` reads any of it. It is also the wave that most directly attacks the loop, which is the
part the phase-ordering obscured: this session added *one* document to `proposals/` and thereby
churned the glossary, the test register and the identifier census, and failed a blocking gate on the
glossary. That is the generator running on generated data, and no amount of doctrine reaches it.
So Wave 5 is now **S4**, ahead of the remaining architecture — and waves 1-3, which S5 rewires around,
ran first at S2/S3 because they were what made the tree inconsistent.

What genuinely must wait is narrower than "culling": **Wave 6** touches apparatus that S5
(contracts-as-registration) rewires, and collapsing the remaining consolidations before S5 has settled
what dispatches what is how the previous eight consolidation plans failed. That stays late, at **S6**.

---

## 2. The target state, in one paragraph

**One pattern, applied everywhere, and nothing outside it.** An *authored surface* under
`references/` (or a single Python owner) is cooked by *one exporter* in `tools/` behind a blocking
`--check`, into *one artifact* under `engine/engine_params/`, read by *one leaf* under
`engine/substrate/`. Nothing else parses the authored surface; nothing else reads the artifact;
`systems/` and the Godot port consume the leaf. Four instances already run:

| authored surface | exporter | artifact | leaf reader |
|---|---|---|---|
| `references/descriptor_registry.yaml` | `export_descriptors.py` | `descriptors.json` | `substrate/descriptors.py` |
| `references/module_contracts.yaml` › `composition_roles:` | `export_composition.py` | `composition.json` | `substrate/composition.py` |
| `systems/_architecture/key_type_registry_v30.md` | `export_key_types.py` | `key_types.json` | `substrate/keys.py` |
| `combat_engine_v1/config.py` | `export_engine_params.py` | `combat_engine_v1.json` | the port |

`composition.py` is the shape the rest must copy, and it is worth stating why it works: the engine
names a **role**, the registry names the **module**, and the exporter **imports every declared target
at export time behind a blocking gate** — so import-by-string cannot fail late, and `systems` stays
out of `engine`'s import graph. That is "injectable code"; `descriptors.py` is the same trick for
"injectable definitions". Everything below either extends this pattern, or deletes something that
competes with it.

---

## 3. The steps

Each step: goal, precondition, exact files, the change, an executable gate, the commit subject, an
explicit do-not.

---

### S1 — Make the load-bearing claim true · `state: done` (2026-08-21)

Two-stage registry-driven roster check + an end-to-end falsifier that runs the real exporter over a
doctored registry copy; `NESTED_BASELINE = 16` added to the inversion ratchet so indenting a seam is
net-zero rather than progress. Mutation-verified both ways. C2 marked PARTIAL in the plan of record.

### S2 — Culling waves 1 + 2 · `state: done` (2026-08-21)

76k lines retired; rebased onto PR #325. Four corrections to the ratified plan, all measured:
`engine/engine_params/*.json` are **runtime inputs** and are excluded from wave 5 (removing
`descriptors.json` makes `import engine.autoload.game_state` raise); `tag_normalizer.py` is **not**
a zero-caller leaf and was restored; `review_core.py` was the only carrier of `m1.acceptance` into
CI and it is rewired report-only; `wiring_manifest.yaml` is **deferred, not deleted**, because S5
folds it into the registration table. Carve-outs per Jordan's ruling: `m1_acceptance.py`, both §0.1
guards, `test_known_red_register.py`.

S2 left the suite red at 42 failures, every one a test whose subject it deleted. **S3 cleared them:
1,622 passed / 0 failed.**

---

### S3 — Wave 3, and green the suite · `state: done` (2026-08-21)

**Goal:** no tool errors, no missing pointers, no orphans. This is the step that pays for S2.

**Precondition:** none. Jordan ruled Wave 3 runs, **keeping `.claude/agents/valoria-critic.md`**.

**Delete.** `ci_gate_coverage.py` — first rewrite `valoria_local.py` to drop `--ci` (its lines
23–143) and sever `broken_dependency_checker.py:33`'s import of it · `ci_hooks_verifier.py` —
**only after** confirming `tests/valoria/test_no_polling_triggers.py` independently asserts all seven
deny-list primitives (culling plan §5.3; that test is KEPT regardless) · `ci_wf_harness_check.py` +
`tools/wf_harness.js` + `ci_claude_workflow_paths.py` + `.claude/wf_*.js` · `single_owner_check.py` ·
and the session/process machinery: `session_status.py`, `session_handoff_reminder.py`,
`session_open_work.py`, `handoff_atomize.py`, `workplan_status.py`, editing `.claude/settings.json`
hooks in the same commit.

**KEEP `.claude/agents/valoria-critic.md`.** It is a standalone agent definition; with the `wf_*.js`
scripts gone it is invoked through the Agent tool directly. Nothing else references it, so it costs
one file and preserves the read-only critic posture that caught S1's falsified claim.

**Tests deleted with their subjects.** `test_gate_coverage` · `test_blocking_tier_is_honest` ·
`test_wf_harness` · `test_wf_harness_check` · `test_single_owner_check` · `test_handoff_structure` ·
`test_handoff_dispatch_validity` · `test_retired_tree_apparatus` · `test_retired_tree_scanner` ·
`test_session_open_work`.

**Then repair, do not delete, the tests whose subject only PARTLY died.** These are the rest of the
42 and each needs a decision, not a sweep: `test_ci_common` and `test_ci_common_primitives` lose
their `build_apparatus_registry` / `obs_core` / `dashboard_data` rows and keep the others;
`test_stubwire` already lost its `review_core` third in S2; `test_vector_audit` and
`test_structure_audit` lose their `build_incompleteness` rows. `test_engine_atlas` and
`test_flow_skeletons` are **not** apparatus casualties — they are stale artifacts and stale anchors,
fixed by S4's regeneration and by re-tracing anchors respectively.

**⚠ THIS ENDS THE §0.3 BANNER EXPERIMENT, and that must be said out loud in the commit.** Wave 3
deletes `session_status.py`, which *is* the banner. The culling plan's own standing rule was "Wave 3
does NOT run while the §0.3 experiment is live — it edits the surface under test." Jordan's ruling of
2026-08-21 is newer and governs, but the experiment ends rather than pauses, so **amend §0.3 in the
same commit** to record that it ran for one session and what that session did, instead of leaving
doctrine describing an instrument that no longer exists.

**Replace the banner with nothing, deliberately.** A new session orients from `CLAUDE.md` §1 and
`HANDOFF.md`, which is what those files are for. Do not write a smaller banner; that is the loop.

**Gate.**
```
python3 -m pytest tests/valoria -q                    # 0 failed — the whole point of this step
for t in $(grep -oE "tools/[a-z_0-9]+\.py" .github/workflows/valoria-ci.yml | sort -u); do
  [ -f "$t" ] || echo "DEAD: $t"; done                # empty
python3 tools/broken_dependency_checker.py            # Total broken: 0
python3 tools/valoria_local.py --staged               # exit 0, no missing-script skips
```
The second and third lines are the "no missing pointers / no orphans" acceptance, and they are the
reason this step is not finished when the suite goes green.

**Also fix here, because they are exactly the class this step is named for:** the one broken path
`broken_dependency_checker` still reports — `tools/dashboard_data.py`, cited by live ledger entry
`ED-IN-0069` — and `.githooks/pre-commit` if it names anything retired.

**Commit:** `[cleanup] Culling wave 3: retire the wiring-checkers and session machinery, and end the §0.3 banner experiment (ED-IN-0194)`

**Do not:** delete `valoria-critic`, `test_no_polling_triggers`, `test_known_red_register`, or
either §0.1 guard. Do not write a replacement banner.

---

### S4 — Wave 5: untrack the generated data · `state: done` (2026-08-22, `f84692c`)

**Goal:** no read/write failures from generated artifacts; end the document tax.

**Measured:** one added `proposals/` file dirtied **21 glossary files and 16 census files**, all
freshness-gated and blocking. `references/glossary/` (75,829 lines) already went in S2 because its
generator did.

**Remaining targets.** `systems/*/_identifier_census.yaml` (15 files, 26,292) ·
`references/identifier_census.json` · `references/{execution_map.json, EXECUTION_MAP.md,
execution_trace.json}` · `references/{engine_atlas.json, ENGINE_ATLAS.md}` ·
`references/{CONTRACT_INDEX.md, KEY_INDEX.md}` · `references/key_graph.json` ·
`references/definitions/definitions.yaml` + the 4 vocab views.

**EXCLUDED, and this is the commensurability boundary — do not untrack these:**
`engine/engine_params/*.json` and `params_tables.yaml`. They are **runtime inputs**, read at import
by `substrate/{descriptors,keys,composition}.py`, `autoload/{sigma_leverage,dice_engine}.py` and
`cross_scale/echo_transport.py`. Untrack them and a fresh clone does not import. Proven in S2.

**The gate flip IS the work.** Each freshness check that diffs a *committed* copy against a fresh
build (`vocab_store --check`, `definitions_store --check`, `test_engine_atlas`,
`build_identifier_census --check`) flips to **build in CI, do not diff a committed copy**. One
deliberate pass, gate by gate. A gate left diffing an untracked file fails permanently and gets
deleted by the next session, which loses the check.

**Regeneration order is not arbitrary — the glossary was built FROM the census:**
`build_execution_map` → `build_engine_atlas` → `build_identifier_census` → the exporters. Re-run each
`--check` after.

**Hard gate (culling plan §5.5):** `validate_ed_citations.py:368` reads the identifier census.
Detach it or confirm it degrades safely **before** untracking, or valid `ED-` citations risk reading
as fabricated.

**Gate.** `git ls-files | xargs wc -l` falls by ~35,000 further; suite green with no generated file
committed; and the falsifier — **add a throwaway `proposals/*.md`, run the suite, observe zero
generated-file churn and no red gate**, then delete it.

**Commit:** `f84692c [cleanup] Culling wave 5 (S4): untrack the generated layer, and replace five
staleness gates with one build gate` — 25 files untracked, **38,156 tracked lines** removed.

⚠ **Do not quote a 566,731 → 370,340 figure as this STEP's result.** That −196,391 span is the whole
BRANCH's cull (waves 1, 2, 3 and 5 together); S4 alone is the 38,156 above, which is what this step's
gate at `:242` predicted ("~35,000"). The two were reported together to Jordan on 2026-08-22 in a way
that read as one number for one step; corrected here so the next reader does not inherit the
conflation.

**RESULT, including where this step DEVIATED from the instruction above.**

*The gate flip was not a flip.* The instruction said each `--check` that diffs a committed copy
"flips to **build in CI, do not diff a committed copy**". Executed literally that keeps five
near-identical tests alive as a rule about a file nobody wrote — the duplication §8 forbids. What
landed instead: **one** owner of "every builder runs and leaves its artifacts"
(`tests/valoria/test_generated_layer.py`), with per-artifact **determinism** staying in each
artifact's own file because nothing in the first claim can observe it. The staleness failure class
was DELETED — saying otherwise would have been the dishonest half of the change.

  ⚠ **"deleted, not reworded" was overdrawn as a description of the FILES, and is narrowed here.**
  The *failure class* was genuinely deleted. But only three of the five tests disappeared: two were
  rewritten in place into determinism tests that say so in their own docstrings
  (`test_execution_map.py` "This WAS `test_map_is_current`", `test_key_graph.py` "This WAS
  `test_graph_is_current`"), and `test_definitions_store.py` still carries its original name
  `test_store_is_current_and_parity_holds`. Those rewrites make a different, still-falsifiable claim
  — which is the point — but three-of-five is not five-of-five.

*`build_identifier_census --check` was REMOVED from CI, not flipped.* It compares a fresh
re-derivation against files git no longer carries; left in the blocking `validators` job it would
have red `main` on the first push. Removed from `tools/valoria_local.py` in the same commit.

*THE FOUR VOCAB VIEWS ARE KEPT TRACKED — the instruction above is not followed. ⚠ THE FIRST REASON
THIS SECTION ORIGINALLY GAVE WAS FALSE AND IS RETRACTED (2026-08-22, adversarial pass).* It claimed
two blocking CI validators "read them". They do not:

  * `tools/ci_naming_check.py:60-75` lists all four in its **EXCLUDE** tuple — it deliberately skips
    them, so their absence changes nothing.
  * `tools/validate_ed_citations.py` lists them in `PROVENANCE_PATHS`, which only classifies a file
    the tree walk already found; an absent one is skipped.

  Measured, not reasoned: with all four moved off disk, `validate_ed_citations.py` and
  `ci_naming_check.py` both exit **0**. The claim was a pattern-match on the filenames appearing in
  both validators' source, and it was used to justify deviating from a ratified instruction — the
  worst place to put an unverified reason.

  **The decision stands, on the two reasons that survive:**

  1. **`tests/valoria/test_vocab_store.py` is the real guard, and it is in the BLOCKING pytest
     suite.** Same measurement: with the views absent it fails 2 of 4 (`test_views_are_generated_stamped`
     among them). So untracking really would put a blocking gate's input outside a clean checkout —
     the §5.5 hazard — just not via the validators originally named.
  2. **They do not carry the document tax.** They generate from `references/definitions/vocab_source.yaml`,
     an AUTHORED file, so they churn when vocabulary changes and never on an unrelated prose edit.
     The wave-5 criterion is *generated · never authored · churns on unrelated edits*; the views fail
     the third clause.

  Their only former runtime consumer, `tools/observability/build_lexicon.py`, went in wave 1, which
  is presumably why the instruction assumed they were free to drop.

*`trace_execution_phases.py` was ADDED to the layer*, first and despite costing ~9.5s. Omitting it
does not fail — both consumers report an absent input — it makes every subsystem read as "not
observed at this seed", which is the false-absence error the tracer's own docstring warns about,
reached by a fixture instead of by a reader.

*A FIFTH DEVIATION, UNDECLARED UNTIL THE ADVERSARIAL PASS FOUND IT (2026-08-22).* The instruction at
`:234-236` gives a regeneration order: `build_execution_map` → `build_engine_atlas` →
`build_identifier_census` → the exporters. The fixture implements a different one: `trace` →
`key_graph` → `execution_map` → `atlas` → `contract_index` → `census` → `definitions`. The fixture's
order is the CORRECT one — the instruction's omits `key_graph`, which **three** builders read
(`build_contract_index.py:68`, `build_engine_atlas.py:57`, `build_execution_map.py:212`), and omits
that `build_engine_atlas` additionally reads `execution_map.json` (`:58`). Running the instruction's
order literally would hand two builders an absent input.

So the deviation is an improvement, and it is recorded here for the reason the other four are: a
plan whose executor silently re-orders its steps is a plan the next reader cannot trust. Note also
that `conftest.py`'s own comment undercounted these edges as "two builders read `key_graph.json`" —
corrected in the same commit.

*THE BUILD GATE'S JUSTIFICATION, STATED NARROWLY.* `tests/valoria/test_generated_layer.py` was
defended to Jordan as clearing §0.1 pt 5's load-bearing predicate. **It does not, and that defence is
withdrawn.** The generated layer is load-bearing on process only: it has zero readers in `engine/`
(proven by import), it crosses into no export, no port and no `needs_jordan` queue. Under the letter
of the predicate — the one that forbade `test_gate_coverage.py` — this test would not be minted today
on its own merits.

What actually licenses it is narrower and sufficient: **S4's ratified instruction mandated a build
gate** ("The gate flip IS the work", `:236-241`), and the change is a net **5 → 1** reduction of an
existing guard surface, not a fresh mint. Recorded rather than quietly dropped, because CLAUDE.md
§0.3 names apparatus-guard minting as the loop's generator (T3) and a session executing the
anti-loop plan is the last place that should go unexamined. `test_the_layer_is_not_vacuous` is
additionally a guard-on-a-guard by shape — four lines, defensible floor, but the shape §0.3 indicts
at depth five, and nobody said so until now.

**Hard gate (§5.5) — CLEARED, by measurement.** `validate_ed_citations.py` EXCLUDES the generated
sidecars rather than reading them, so it degrades safely. Verified by running it, and every other
blocking validator, with all 25 files moved off disk: `broken_dependency_checker`,
`ci_claim_provenance_check`, `compliance_check`, `ci_co_file_checker`, `freshness_gate`,
`ci_vetting_check`, `ci_register_size_check`, `ci_names_consistency`, and all five export `--check`
round-trips — all green. `engine.autoload.game_state` and `engine.mc_v18` also import cleanly with
the layer absent, which is the no-runtime-reader claim proven rather than asserted.

**Gate — MET.** Full suite from a simulated clean checkout (every artifact deleted first):
**1628 passed, 23 skipped, 15 xfailed, 0 failed**. And the stated falsifier ran: a throwaway
`proposals/*.md` was added, the suite run, and the tracked churn was **zero** — against 16 dirtied
census files before this commit.

**Two pre-existing defects fixed in passing.** `tools/valoria_local.py:113` cited "the note in
valoria-ci.yml" as the mitigation for a three-instance pattern; ED-IN-0176 named that note and never
wrote it, so the recorded remedy for a recurring defect was a dangling reference. It is written now.
This shrinks the CI-only-validator residual from four to three; it does not resolve it, and nothing
guards it — `test_gate_coverage.py` was the test that failed on a fifth instance and it went in
wave 3.

---

### S5 — Finish the centralization: one pattern, everywhere · `state: next`

**Goal:** centralized definitions and injectable code, consumed by wrappers and systems. This is the
step the whole programme exists to reach.

**5a — Finish the seam inversion.** PR #325 lowered the ratchet 5 → 3 via `composition.require`.
Remaining: `engine/cross_scale/parliamentary_bridge.py` (3 imports) **and the lateral duplicate of
the same seam at `systems/factions/sim/parliamentary_transfer.py:54`** — one seam owned twice. Add
its role to `composition_roles:`, resolve through `require()`, delete both imports, lower
`BASELINE_TOTAL` 3 → 0 in the same commit. Then the 16 function-local imports the `NESTED_BASELINE`
ratchet pins, `game_state.py`'s eleven first.

**When `BASELINE_TOTAL` hits 0:** delete `test_the_documented_cycle_is_still_real` **and correct
`CLAUDE.md` §3 in the same commit** — that test exists solely to stop §3's "acyclic, autoload is a
leaf" being restored while the code contradicts it.

**5b — Give the hardcoded rosters an authored surface.** `engine/autoload/game_state.py` still
carries `MULTS` (:46), `ALL_PLAYABLE_15` (:41), `STARTING_OWNER` (:48), `STARTING_STATS` (:55),
`STARTING_GARRISON` (:95) as literals with no authored source. These are **world data**, not code.
Author them into `references/` (a `world_initial_state.yaml`, or rows on an existing registry), cook
them by the same pattern, and delete the literals. This closes C2's remaining two thirds.

**5c — Fold `wiring_manifest.yaml` into `module_contracts.yaml`,** as the culling plan directs and S2
deferred. One registry, two blocks (`composition_roles:`, `modules:`), one exporter each. Then
`wiring_map_check.py` retires into `export_composition --check`.

**5d — Implement `per_stat_floors` (ED-IN-0029, ratified 2026-07-08, never implemented).**
`Faction.adjust` applies a blanket 0.5/7.0 to every stat while the registry declares Influence floor
1 and the rest 0, and none of its 32 callers overrides it. Wire `descriptors.faction_bounds()`.
**This moves the seeded goldens** — its own commit, delta measured and explained, per §0.1 pt 4.

**5e — The invariant, made enforceable.** One test, game-subject, replacing the retired
`single_owner_check`: *every file under `engine/engine_params/` has exactly one exporter that writes
it and exactly one leaf under `engine/substrate/` that reads it, and no other module parses its
authored surface.* Derive both sides from the tree, not a hand list. This is the guard that keeps the
pattern from decaying back into ad-hoc readers, and it earns its existence under §0.1 pt 5 because
its subject is the bridge the port is generated against.

**Gate.**
```
grep -rE "^(from|import)\s+systems[.\s]" engine --include=*.py | grep -v engine/tests   # empty
python3 -m pytest tests/valoria/test_engine_does_not_import_systems.py -q  # BASELINE_TOTAL 0
python3 -m pytest engine/tests -q      # unmoved, EXCEPT the 5d commit, whose delta is recorded
for e in engine/engine_params/*; do echo "$e"; done  # each has one exporter + one leaf reader
```

**Commit:** one per sub-step. `[infrastructure] S5c: module_contracts.yaml becomes the single registration table`, etc.

**Do not:** invent a second registry; special-case a subsystem in `scene_dispatch.py`; or fold 5d
into any other commit.

---

### S6 — Wave 6 consolidations, FORK semantics, and the ledger cap · `state: blocked-by S5`

**6b before 6a** — 6b's tombstones gate 6a, and `deprecated/archives/editorial*` is read by
`validate_ed_citations.py`; delete it before the tombstone list lands and **every valid `ED-`
citation reads as fabricated** (culling plan §5.2). Then 6f, then 6c.

**FORK semantics first, then the call sites (D1).** Three surviving sites give three different
answers about the same ledger row: `pathres.py:184-191` returns a `FORKED` status,
`broken_dependency_checker.py:164` returns `FORK:<ref>:<original-ref>`, `ci_claude_workflow_paths.py`
has no FORK handling and resolves a forked file to `None`. Decide what a FORK row resolves to, once,
then port. ⚠ `pathres.resolve(max_hops=1)` claims to reproduce `bdc` exactly and does **not**
reproduce its pairing format, which `bdc`'s caller checks — a drop-in port silently changes output.

**Naming trio is a two-of-three merge (D2):** merge the `ci_names_check` facade; leave
`ci_names_consistency` standalone (different invariant, and it hard-requires PyYAML which the
register-size validators deliberately avoid). **D4 is struck** — `bdc` absorbing `freshness_gate` is
aggregation, not deduplication.

**Unblock the ledger.** `registers/editorial_ledger_in.jsonl` has ~108 tokens of headroom under a
blocking cap, which means **no lane can file a row at all** (ED-IN-0185 Q5, overdue). Raise, split,
or accept — Jordan's call, §4 Q8. Also resolve the duplicate `ED-IN-0194` at lines 50-51.

**Re-home what `scope_ratchet` was measuring.** It reported REGRESSED on `ed.stale` (199 vs 76) and
`ed.needs_jordan_stale` (83 vs 21) up to its deletion and nothing reports them now. Those are
**ledger** facts. If they are watched again, the instrument is a ledger-subject one — not a
five-ceiling repository ratchet.

---

### S7 — Wave 4's residue: extraction, not culling · `state: blocked-by S6`

**16 of the 17 "delete outright" units are already gone** (#323 took them; residue 1,870 lines).
`audit/` still holds 79,085 lines and that is almost entirely the **~33 game-subject working papers
the plan requires to be EXTRACTED first** — their surviving conclusions belong in `systems/` heads or
`proposals/`, the workings do not. Named explicitly by the plan: the mass-battle stress-test
octagon/rotation/geometric-contact models, `narrative_engine_design_v2_churn.md` (**RATIFIED and
`CURRENT.md`-referenced — it must MOVE, not fork**), the contest gate packets, the world-churn audit
(backs 9 open Jordan decisions), the degree-reband delta, the degree-vocabulary census.

**This is authorship work on game subjects and should be scheduled as such**, not as a wave. Nothing
under `engine/` or `tools/` opens a file in `audit/` — every mention is a docstring citation
(measured 2026-08-21) — so the fork-ref move is safe once extraction is done. One blocker the plan
names is already clear: `test_fork_divergence.py` was deleted in `4ab18df`.

---

### S8 — M1 juncture 1 · `state: half-done; Half B SUSPENDED` (2026-08-21)

> **HALF A LANDED.** `sigma_leverage.roll_net_continuous` no longer rounds its pool. Six goldens
> re-recorded against `tools/balance_oracle.py` at n=120 per arm — no faction shifts significantly,
> so the goldens moved from RNG divergence, not balance. Combat's byte-exact goldens were the
> control and did not move (749 of 749 combat calls are integral).
>
> **HALF B SUSPENDED by Jordan, 2026-08-21, flagged for later systems work** — and the
> classification is why. It was expected to find fixed literals to convert. It found three OPPOSED
> sites that already derive Ob from a target faction's score and DISAGREE with each other:
> `coronation_renewal_ob` is `floor(L/2)+1` (already the ruling), `tribunal` is `L*0.5` under formal
> grounds and full `L` otherwise, `parliamentary_transfer` is `L+2` — stated as canon in its own
> design doc. So the board's claim that `score/2` is "wired NOWHERE" is false, and reconciling the
> three would overwrite ratified canon and collapse tribunal's two-tier mechanic.
>
> Full classification and the two damage arguments: `registers/handoffs/HANDOFF_FA.md`. The three
> conventions are pinned by `tests/valoria/test_faction_obstacle_conventions.py` so none drifts
> while the question is suspended; when a ruling lands, that file is where it gets recorded.
>
> ⚠ NOT STUBBED, deliberately. These resolvers run in live campaigns: `stub_resolve`-ing them would
> move the seeded goldens AND push `m1_acceptance` row 1 — which requires ZERO stub invocations on
> the M1 path and currently fails at 2 — further from passing. Suspension is a flag on the
> QUESTION, not a hole in the engine.

> **PROMOTED TO `next`, and the promotion is the point.** This document's §1(c) says *something must
> move `0/7` before more architecture lands*. S1, S2 and S3 landed; none of them changed how the game
> plays; `0/7` is unmoved. A read-only audit put it plainly: the plan's mechanical rail said "take the
> first step whose `state:` is `next`" while `next` pointed at **more culling**, so the rail and the
> stated priority pointed in opposite directions and the rail would have won by default.
>
> That is not a scheduling detail. It is the T2 mechanism `CLAUDE.md` §0.3 describes — the next step
> being whatever the board says, rather than whatever the milestone needs — reproduced inside the
> document written to escape it. Resolved by one word of bookkeeping, which is what it always cost.

**Half A, fractional pools — and it is NOT a dormant bug.** Measured 2026-08-21: a 4-season seeded
campaign makes 40 calls to `roll_net_continuous` and **20 already pass a fractional pool** (4.3, 4.6,
4.9, 5.3, 5.5, …), every one silently rounded.

The instrument, because a number without one is not a measurement (§0.1 pts 3-4) and the first
version of this paragraph shipped without it — re-run it before trusting the 20/40:

```python
import sys, collections; sys.path.insert(0, '.')
from engine.autoload import sigma_leverage as SL
seen, real = collections.Counter(), SL.roll_net_continuous
def spy(pool, tn=SL.TN_STANDARD, rng=None):
    seen['frac' if float(pool) != round(float(pool)) else 'int'] += 1
    return real(pool, tn, rng=rng)
SL.roll_net_continuous = spy
from engine import mc_v18; mc_v18.run_campaign(seed=20260819, max_seasons=4)
print(seen)          # -> Counter({'frac': 20, 'int': 20}) on 2026-08-21
``` `sigma_leverage.py:284` does
`max(1, int(round(pool)))` while `dice_engine.continuous_engine_sample` already accepts fractional
input and says so at `dice_engine.py:92`. Replace with `max(1.0, float(pool))` — the canonical pool
floor survives, the quantisation goes. **Do not touch `roll_net` at :273**, the discrete path.

⚠ `systems/combat/combat_engine_v1/core.py:56` routes through the same function, so personal combat
is in the blast radius **by construction**; whether its pools are fractional is not yet measured.
Measure before editing, because the byte-exact golden-modes CI job pins it.

**Half B, the `score/2` obstacle — begins as a classification, not an edit.** The FA surface has two
obstacle sites, both fixed literals: `faction_action.py:540` (`ob = 1`, Muster) and `:562` (`ob = 2`,
Govern). Neither is obviously in scope: the ruling's antecedent is "rolled against a character or
faction" and both are rolls against the world. Enumerate every FA resolver, label each **opposed** or
**unopposed**, wire `score/2 + modifiers` into the opposed set only, against the six-field roster the
code implements (provisional — Q1 gates which roster is canonical, not the arithmetic). **If the
opposed set is empty, say so and stop** — that is a finding, and it converts Half B into a question.

**Two declared holds you must not touch:** `combat_engine_v1/core.py:77` (fixed `DECISIVE_OB = 3`,
entangled with the guandao/plate collision) and `sigma_leverage.degree` (ED-IN-0187).

**Gate.** A seeded FA probe whose recorded outcome **differs** from the same seed before the change,
with the golden delta explained. If nothing differs, Half A did not take effect.

---

### S9 — Cross-repo residue · `state: blocked-by attaching jordanelias/valoria-game`

**Most of this act is already done** and the earlier plan is stale on it. In `valoria-game`: PP-665
finished, **CI green for the first time since 2026-05-04**, the masked `Verify Solmund naming` step
executed for the first time ever (and was itself red, fixed in the same commit), and Act C1's
**reader half shipped** — `tools/check_constants_parity.py`, `resources/generated/game_constants.json`
(the first `.json` that repo has ever contained), and a `Constants Parity (vs design oracle)` CI job.

**What remains: B2 and B3.** B2 — harden the compile ratchet: assert the project actually finished
loading before comparing counts; path-anchor the `res://tests/` exclusion, which currently drops any
line containing `GdUnitTestSuite` anywhere; compare error **sets**, not counts, so "fix five, add
five" fails. Godot 4.3 downloads through the proxy, so this is locally measurable — 84 errors
reproduce exactly, 63 of them `Cannot infer the type of X`. B3 — make one GDScript test execute;
gdUnit4 vendoring is 403 through the proxy, so the fallback is a `tests/run_all.gd` `SceneTree`
script over the pure-logic classes.

---

---

## 3a. How deep the tooling goes — THREE layers, and L3 is zero code (Jordan asked 2026-08-22)

Jordan proposed a model — L0 game code · L1 compliance · L2 verification · L3 holistic wrapper — and
asked how many layers this repository actually needs. **The answer is three, and the fourth slot is
filled by a stage rather than by code.** This section governs every step above and below it: a step
that would add a rung is refused here, not debated later.

**One correction to the model before it can be used: it classifies CHECKS, not FILES.** Applied
per-file it misclassifies, and the misclassification is not hypothetical — `tools/export_descriptors.py`
is simultaneously a **build step of L0** (its output `engine/engine_params/descriptors.json` is a
runtime input; delete it and `engine.autoload.game_state` will not import) and an **L1 gate** in
`--check` mode. `broken_dependency_checker` is L1 for path resolution and L2 for its registry↔CI
join. `m1_acceptance` is L1 in rows 1-2 and process bookkeeping in row 4.

| layer | what lives there | posture |
|---|---|---|
| **L0** | `engine/`, `systems/*/sim/`, `engine/substrate/`, the `engine_params/*.json` runtime inputs — **and runtime instrumentation the engine or the port consumes** | grow |
| **L1** | compliance over L0 and canon: the blocking validators with game subjects, the five export `--check` round-trips, both pytest suites, the goldens, `m1_acceptance`, `balance_oracle` | **harden, do not grow** |
| **L2** | small and enumerable; admitted only where an L1 gate's failure would be **silent and game-costly**, and each **mutation-verified at introduction** | cap |
| **L3** | **zero code** | never build |

**Why L2 terminates, and it is not because of a rule.** An L2 guard closes its own loop when it is
*mutation-shaped*: plant the defect, assert red. `tests/valoria/test_field_golden_pins.py:16-18`
records exactly that. You do not need an L3 test to know such a guard works — running it against the
planted mutation **is** the evidence, and evidence is an artifact (§0.1 pt 3), not another file that
itself needs guarding. Where an L2 guard is mutation-verified at birth, the regress bottoms out in
execution rather than in code.

**Why L3 is never mintable on the merits.** L3's subject is always an L2 guard — apparatus — and
§0.1 pt 5 rules that load-bearing is **not transitive** through apparatus.

**But the predicate leaks, so the cap does independent work.** Both live depth-3 artifacts exist
*despite* the predicate: one rides an explicit Q6 exemption, and the other is
`test_generated_layer.py::test_the_layer_is_not_vacuous`, whose predicate defence this very document
withdraws two sections up — and which shipped anyway on a "ratified instruction mandated it"
carve-out. §0.3's depth-five stack was built by **flawless** application of a judgment rule. Judgment
rules admit exemptions; exemptions compound. So: **the predicate governs admission, and the depth cap
is the backstop the predicate cannot provide about itself** — because "does this test's subject import
or scan another test or tool?" is mechanically checkable in review, and therefore exemption-resistant.
**As a review criterion, NOT as `ci_depth_check.py`** — a gate enforcing the gate-depth cap would be
the joke writing itself.

**L3 has already been built four times here and retired four times**, each time measured:
`review_core.py` + `review_baseline.yaml` (twelve signals, eleven of them apparatus),
`scope_ratchet.py`, the observability generators, the SessionStart banner. Each was a holistic surface
over everything below it; each, per §0.3, **defined the next session's work** — the T3 loop closing.
A new L3 wrapper recreates them under a new name, and §0.3 already answers it: *"Do not build a
replacement… test T2 instead."* The only L3 that legitimately survives is not code — it is the
fresh-context adversarial stage and Jordan's rulings, which by the §0 amendment **cannot accrete
artifacts**.

**Where runtime observability sits: L0** — which is what licenses S10 above and exempts it from the
cap. The precedent is already in the tree: `KeyLog` (`engine/substrate/keys.py:336`) is append-only,
deterministically serialized, consumed at runtime by `mc_v18.py:313`, and is the surface the Godot
port's key-log parity validates against. Telemetry the engine emits and the port must reproduce is
**oracle surface**, no more subject to a tooling depth cap than `dice_engine.py` is. The boundary test
comes from the corpse of the counterexample — the retired `tools/observability/` tier died because its
feeds *"had no runtime consumer in `engine/` or `systems/`"* (§8). So one line decides every future
component: **does the engine, the port, or a Jordan decision consume it at runtime?** Yes → L0. No →
that is the retired tier again.


### The orchestrator question, ruled (Jordan, 2026-08-22: "L2 requires an orchestrator")

**It does, and it already exists — and naming it correctly is what stops it becoming L3.**

`tools/valoria_local.py` is the orchestrator. Its docstring states the property that keeps it safe:
*"ONE VALIDATOR, MANY CALLERS: this orchestrator shells the authoritative validators; it never
re-implements a rule."* **A dispatcher that holds no rule has no subject, so it occupies no rung and
cannot deepen the stack.** `tools/ci_common.py` is the same shape: shared primitives, no subject.
Neither is L1, L2 or L3 — they are plumbing, and plumbing is not a layer.

⚠ **THE LINE AN ORCHESTRATOR MUST NOT CROSS.** Dispatching is plumbing; **aggregating verdicts is
L3.** The moment an orchestrator scores, ratchets, or rolls its children's results into a single
repo-wide judgement, it has become `review_core.py` — which did exactly that across twelve signals,
eleven of them apparatus, and was retired for it. The operational rule: **add a validator to the
list; never add a summary of the list.**

This is also why `valoria_local`'s report-only tier is correct as built. It *prints* which
report-only checks failed and returns 0 — surfacing without judging. A version that folded those into
a pass/fail score would be the crossing.

### The keying is now IN THE TREE, not just in this document

`references/ci_checks_registry.yaml` carries `layer:` and `posture:` on all 32 rows as of
2026-08-22, with the vocabulary defined in its own header block — so the next session meets the model
where the tools are declared, not only here (§4's "define it in both places" rule: prose AND the code
that invokes it).

Measured at keying: **31 rows are L1/harden, exactly 1 is L2/cap** (`ci_vacuous_assertion_check.py`,
whose subject is the assertions inside `tests/valoria` + `engine/tests`). **No row is L0** — a gate is
never the game. The remainder of L2 is not in that file because it is **tests, not tools**:
`tests/valoria/test_field_golden_pins.py`, `test_pytest_marker_discipline.py`, the known-red register
in `conftest.py`, `broken_dependency_checker`'s registry-coverage function, and the export
falsifiers. **Any new L2 member, wherever it lives, needs a mutation check in the same commit** — that
is what makes it terminate in execution instead of in a further guard.

### Three findings this analysis surfaced that need Jordan, not a session

1. **There is a depth INVERSION on `main` right now.** `tools/ci_vacuous_assertion_check.py` (L2) runs
   in `validators-report`, which is `continue-on-error: true` — it **cannot fail the build**. Its test
   `tests/valoria/test_vacuous_assertion_check.py` (L3) runs inside the **blocking** unit-tests job.
   The depth-3 guard is enforced while the depth-2 tool it guards is advisory. Verified against
   `.github/workflows/valoria-ci.yml:236` and `:351`.
2. **`level:` in `references/ci_checks_registry.yaml` is close to information-free, and the worst case
   is a game signal.** Measured: **12 of 32 `level: 5` rows cannot fail CI** — ten wired to
   `validators-report`, two (`balance_oracle.py`, `build_identifier_census.py`) with an empty
   `ci_job`. **`m1_acceptance.py` is among them.** That is §0.2's instrument, the one game-subject
   signal, and it means **no game regression can currently red CI.** The registry admits this at
   `:329-337`. This is an L1 hardening debt and it is the most consequential item on this page.
3. **The `level:` ladder's own source document does not exist.** `ci_checks_registry.yaml:10` cites
   `project-architecture-valoria-v2_2.md`; it resolves nowhere on `main` and has no
   `references/restructure_ledger.md` row. The taxonomy is a dangling reference by this repo's own
   standard.

---

### S10 — Errors become numbers: the caught-exception channel · `state: unblocked`

Independent of S5–S9. **Do not take it ahead of S5 or S8 by rail-default** — it does not move `0/7`,
and §1(c) still binds. Requested by Jordan 2026-08-22: *"record and identify how, why, where and when
errors occur."*

**Goal:** a caught exception on the campaign path becomes a counted, asserted-zero fact — never only
stderr text, never a dropped string.

**Measured 2026-08-22, by READING each construct in context rather than counting token hits.** That
method distinction is load-bearing here: the first census of this surface was produced by grep and
**two of its three headline numbers were wrong**, in the direction that would have justified more
apparatus.

  * *"12 silent-failure sites"* is **4**. Seven of the twelve are the identical benign
    `sys.stdout.reconfigure(encoding='utf-8')` console shim inside `if __name__ == '__main__':`
    blocks; one is an unreadable-file skip in a dead-code scanner that raises loudly if nothing was
    read. The four real ones are cross-subsystem seams —
    `systems/social_contest/sim/contest_legacy_stub.py:247`, `systems/threadwork/sim/opposing.py:255`,
    `systems/fieldwork/sim/knots.py:354` and `:367` — where one `except (ImportError, AttributeError): pass`
    wraps **both the late import and the effect call**, so a genuine `AttributeError` inside
    `apply_conviction_scar` / `apply_coherence_delta` / `social_success` / `sustain_knot` is swallowed
    identically to a missing module. All four write game state: Conviction scars, coherence, knot
    strain, momentum grants. This is §0.1 pt 1's exact shape — correct when written, silently a no-op
    once a callee changes.
  * *"31 `NotImplementedError` stubs"* is **2 live `raise`s**, one of them an abstract base with three
    concrete subclasses defined below it, the other a stub with zero production callers. The rest are
    comments recording the OI-17 conversion into `engine/substrate/stubwire.py` — **45 live
    `stub_resolve(` call sites**, already counted per-campaign into `CampaignResult.stub_hits` and
    already consumed by `m1_acceptance` row 1 (which honestly FAILs at 2). **The stub-telemetry half
    of this ask is built and consumed; do not rebuild it.**
  * *"28 raises, 0 asserts"* is not a gap. 26 of the 28 are `engine/substrate/keys.py`'s typed
    `KeyValidationError` (invariants 1-8) and `TerminationBreach`; the other two are leaf readers
    failing fast on a missing cooked artifact. **Typed raises are strictly better than `assert`,
    which `-O` strips. The substrate raises loudly — the gap is one layer up, in what the driver does
    with what it catches.**

**The actual error surface is two swallow points in the driver layer, and one of them already knows
it.** `engine/mc_v18.py:137-144` catches faction-action exceptions and prints to stderr — its own
comment says *"it must NOT be swallowed SILENTLY either (audit ED-IN-0074 D7)"* and then counts it
nowhere. A resolver that raises **before consuming RNG** (an `AttributeError` on a renamed field —
precisely the fractional-pools class) leaves the RNG stream unchanged, every seeded golden green, the
faction silently inactive, and the only trace is stderr nothing reads.
`engine/cross_scale/scene_dispatch.py:372-374` turns a resolver crash into
`out["reason"] = f"resolver raised: {e!r}"`, which flows into `report["deferred"]` and is **dropped**
at `mc_v18.py:149-150`, which reads only `["dispatch"]["resolved"]`. A resolver crash is currently
indistinguishable from a designed deferral in every consumed output.

**The change.**

(a) `CampaignResult` gains `faction_action_errors`, `scene_resolver_errors`, `scene_deferrals` (int
defaults). `mc_v18.py:139` increments a world attribute beside the kept stderr print;
`scene_dispatch.py:372` sets `out["error"] = True` beside the existing reason; `dispatch_scenes`
counts it; `mc_v18.py:149` folds the count instead of dropping the report. **Mirror the
`accord_drift_probe_hits` idiom** (`mc_v18.py:312`, `getattr(world, ..., 0)`) — that is this repo's
ratified shape for "record a defect without fixing it", and it already has a dedicated consumer test.

(b) At the four seams: the `try` covers **the import only**; `ImportError` routes to
`stubwire.stub_resolve` naming the seam (reusing the single owner, counted into `stub_hits` which m1
row 1 already reads); the effect call moves **outside** the `try`, so a real bug in the callee raises
again.

(c) `m1_acceptance.row_invariant_violations` moves `blocked` → `partial`: over the probe season it
already runs, assert both new counters are 0 and report `len(KeyLog.stat_vocabulary_warnings)`. Keep
`unblocked_by` naming the full N-seed sweep that remains.

(d) `mc_v18.__main__` gains `--seed / --seasons / --dump PATH`: one campaign, then the `KeyLog`
serialization, every `CampaignResult` field, and the per-scene reports **including the deferral and
error reasons currently dropped**. Written **only when asked**. Never by default, never committed —
S4 just untracked the generated layer and a default-written run record regrows it.

**Consumers, named, because §0.3 demands it.** Zero-assertions in
`engine/tests/test_mc_v18_regression.py` + `test_f7_smoke_oracle.py` (blocking CI) · `m1_acceptance
--summary` (Jordan's instrument) · `stub_hits` → m1 row 1 · the `--dump` file's consumer is the human
who invoked it, and later the port's V.2 recorded-draw replay harness.

**Determinism argument — the thing most likely to be got wrong.** No site constructs, seeds or draws
from any `Random`; the additions are integer increments and dict keys. No new Key is emitted, so
`content_hash()` — m1 row 2's instrument and the port's master parity check — cannot move. No
golden-compared value derives from touched state (`run_batch` reads `r.winner` and `r.battle_count`
only). The four seams are unreachable at the golden seeds, so (b) removes no RNG consumption either.
`out["error"] = True` is set only on the exception path, which `return`s at `:374` before the
echo-transport block, so it can never reach `emit_scene_echo`.

**Gate — and the falsifier IS the gate.**

```
python -m pytest engine/tests -q            # green, ZERO golden re-records
python3 tools/m1_acceptance.py --summary    # row 2 hash unchanged; row 5 now `partial`, measured 0
```

then inject a pre-RNG crash into `faction_action` and observe **the goldens stay green while the new
counter and its assertion go red**. That asymmetry is the whole point of the step: it exhibits, as
its birth certificate, the defect class the entire existing gate surface is structurally blind to.
Then `--dump` the same seed twice and `cmp` the files.

**Commit:** `[simulation] S10: caught exceptions on the campaign path become counted, asserted-zero
telemetry; un-swallow the four cross-subsystem seams (Jordan 2026-08-22)`

**Do not:** `import logging` anywhere in `engine/` or `systems/` — it is a second event channel beside
`KeyLog` and a second counter channel beside `CampaignResult`, so §8 forbids it, and GDScript has no
analog the strategy doc specifies · add a default-written or tracked run artifact (S4's boundary) ·
build per-module instrumentation for the 27 dark modules — **you cannot log what does not execute**,
their burn-down instrument is `test_pipeline_reach`'s XFAIL manifest and their census is
`trace_execution_phases`, both of which exist · emit any Key from the error path (an error-Key moves
`content_hash` and every determinism row; if error events ever belong in the KeyLog that is a design
decision for the contract-registered `audit` module, `references/module_contracts.yaml:535`, and it
is Jordan's, not this step's) · fold any of this into an S5 sub-step's commit.

**Falsifier for the whole programme, recorded in advance.** If after two months the counters have only
ever been read by the tests asserting they are zero — no red assertion ever fired on a real defect, no
`--dump` ever invoked to diagnose a run, row 5's slice never influenced a commit or a ruling — **then
this layer was apparatus, and the response is to delete the `--dump` flag and the row-5 slice.** It is
confirmed the first time a golden-green commit turns a counter non-zero. The near-term test is
concrete: S5d (`per_stat_floors`) and any S8 Half B ruling both edit resolvers on the live campaign
path, and those are exactly the commits where a pre-RNG `AttributeError` would today ship green.

## 4. What this order deliberately does not do

- **It does not add a step for the review that produced it.** No `test_plan_compliance`, no progress
  register for the steps, no findings document. §0.1 pt 5 forbids the first two and §0 forbids the
  third. The `state:` fields in §3 are the whole bookkeeping surface and they are edited in place.
- **It does not re-litigate the diagnosis.** `proposals/2026-08-18-breaking-the-recursion.md` is
  still the causal account and the amendments in `CLAUDE.md` §0/§0.1/§0.2/§0.3 are live doctrine.
  The review behind this document confirmed the mechanism and disputed only whether the fix had
  reached the game yet.
- **It does not treat the apparatus as the enemy.** The export discipline — authored surface, one
  exporter, cooked artifact, single runtime reader, blocking round-trip — is correct and S4 adds a
  fifth instance of it. The failure mode this order guards against is not building apparatus; it is
  building apparatus that terminates in nothing, and every gate above asks what consumes the thing.

---

## 5. Rulings that gate steps

| Q | Question | Blocks | Where the evidence is |
|---|---|---|---|
| **Q1** | **The faction-stats roster.** Five surfaces disagree; `L` is written by 32 `.adjust()` call sites and declared nowhere in the registry. Is Legitimacy a base faction descriptor or derived like Mandate? | S2 Half B's final form; S4's roster deletion; S6's divergence list. **S2 proceeds provisionally against the coded six-field roster** — the banner authorises this. | `HANDOFF.md:209+`; ED-FA-0004 |
| **Q1b** | **The ratified floors nobody implemented.** ED-IN-0029 (2026-07-08) floored Influence at 1 and the rest at 0. `Faction.adjust` has applied a blanket 0.5/7.0 ever since and no caller overrides it. Wire them, with the golden delta measured? | S4's final commit | `export_descriptors.py` `unimplemented.per_stat_floors` |
| **Q2** | **Name the tenth attribute.** You ruled ten on 2026-08-14; the registry ships nine, and `Constants.gd:28` already declares `ATTRIBUTE_COUNT = 10`. The game is ahead of canon. | closing the `pending_tenth` sentinel | `CLAUDE.md` §5 |
| **Q3** | **Godot 4.3 or 4.6?** `project.godot:11` and CI pin 4.3; `CLAUDE.md` and `godot/` say 4.6. | what the compile ratchet's 84 means | 2026-08-20 plan §1.D5 |
| ~~Q4~~ | **RULED 2026-08-21 — `test_gate_coverage.py` is DELETED with `ci_gate_coverage.py` in S3.** Superseded by the ruling below: Wave 3 runs, and the gate-coverage pair is a Wave 3 target. Local-green may now drift from CI-green; that risk is accepted, and the four `export_*` round-trips it protected are individually blocking in CI regardless. | — | §3 S3 |
| **Q5** | `registers/editorial_ledger_in.jsonl:50-51` — two rows share id `ED-IN-0194` with conflicting `needs_jordan`. Reported 2026-08-19, unruled. | ledger integrity | — |
| ~~Q6~~ | **RULED 2026-08-21 — KEEP both guards.** `ci_claim_provenance_check.py` and `ci_vacuous_assertion_check.py` stay, and `CLAUDE.md` §0.1 stays intact with them. They are the one place doctrine is mechanised rather than merely asserted; the load-bearing predicate is overridden here deliberately, and the exemption is recorded rather than silent. | — | culling plan §5.6, held 2026-08-18 → ruled |
| ~~Q7~~ | **RULED 2026-08-21 — Wave 3 RUNS, `valoria-critic` is KEPT.** `.claude/wf_*.js`, `wf_harness.js`, the wiring-checkers and the session machinery go; `.claude/agents/valoria-critic.md` survives as a standalone agent definition, invoked through the Agent tool now that the workflow scripts are gone. Structurally-independent adversarial review therefore survives the wave that was written to end it. ⚠ **The cost this ruling carries: Wave 3 deletes `session_status.py`, so the §0.3 banner experiment ENDS.** S3 amends §0.3 in the same commit. | — | culling plan §5.7, held 2026-08-18 → ruled |
| ~~m1_acceptance~~ | **RULED 2026-08-21 — CARVED OUT of Wave 1, kept.** Wave 1 as ratified deleted it; §0.2 made it the definition of `done` one day after that ratification. | — | §3 S2 |
| ~~Q8~~ | **RULED AND EXECUTED 2026-08-21 — "merely fiat made trying to get work done."** Caps raised 50k→120k (live lane ledgers) and 150k→250k (their archives). The reported "~108 tokens of headroom" was itself STALE — measured 45,998/50,000, about four rows — and had been re-cited for six days without re-measurement. The duplicate `ED-IN-0194` was split (second row → `ED-IN-0195`, `next_free` 195→196), and a scan found **nine more duplicate-id groups nobody had reported**, five conflicting on `status`; all reconciled into declared parts without renumbering, because those ids are cited across the corpus. | — | `tools/ci_register_size_check.py:102-124` |

**The two that gated how deep the cull goes are now answered.** Q6 and Q7 had been held since
2026-08-18; Jordan ruled both on 2026-08-21 and the answers are recorded above rather than left as
open rows, so no later session re-opens a settled question. **No ruling now blocks a step in this document.** Q8 was the last one and it was ruled and executed
on 2026-08-21. Q1/Q1b/Q2/Q3 remain open but gate only the FINAL form of work that proceeds
provisionally; S4 through S9 need no answer from Jordan to begin.

Q1, Q1b, Q2 and Q3 are the 2026-08-20 plan's §7 queue, unchanged and still open. That plan's own
Q4 (ED-SC-0003/0004/0005 — 0004 has two contradictory live implementations; read ED-SC-0017 first,
it argues 0005 is already ruled) hard-blocks **M1 juncture 3**, and its Q8/Q9 (`accord_range`,
`coherence_bands` — two state models for one field, twice) gate port semantics. None of those are
reached by any step here, so they stay queued there rather than being restated.

---

## 6. Provenance

Produced 2026-08-21 from a read-only adversarial review of `c9b0a86`, `4ab18df` and `1e4c6f4`
(PRs #322, #323, #324) against the working tree at `1e4c6f4`. Seven findings; the two that changed
this order are the falsified load-bearing claim (S1) and the ratchet's inverted incentive (S1). The
measurements behind §1(c) — line deltas per commit, the count of commits since the last
behaviour-changing one, and the 72/170 and 5-vs-16 seam counts — were taken on that checkout and are
reproducible from it.

Supersedes **§5 of `proposals/2026-08-20-return-to-game-plan-v1.md` only**. That document remains the
authority on what each act is and why, and its §1 findings tables are the evidence base this order
assumes.
