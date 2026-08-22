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

### S4 — Wave 5: untrack the generated data · `state: blocked-by S8`

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

**Commit:** `[cleanup] Culling wave 5: untrack generated data and flip the freshness gates to build-in-CI (ED-IN-0194)`

---

### S5 — Finish the centralization: one pattern, everywhere · `state: blocked-by S4`

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

### S8 — M1 juncture 1 · `state: next` (promoted 2026-08-21 — see below)

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
