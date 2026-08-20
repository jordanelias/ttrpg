# Return to the game — the corrected plan

## Status: PROPOSED — plan of record requested. Supersedes the *sequencing* of `2026-08-18-next-session-handoff.md`; does NOT supersede `2026-08-18-culling-plan-v1.md` (still RATIFIED, absorbed here as Act E) or the diagnosis in `2026-08-18-breaking-the-recursion.md` (still the causal account, corrected in §2).

## Date: 2026-08-20 · Lane: IN (cross-cutting) · ED: none allocated

No ED row is filed for this document. Under `CLAUDE.md` §0 as amended 2026-08-19, a row is warranted
only when it requires a human decision; this plan's decision requests are §7, and they are addressed
to Jordan in this file rather than through the ledger. (`registers/editorial_ledger_in.jsonl` also
still has ~108 tokens of headroom under a blocking cap — ED-IN-0185 Q5, overdue, unchanged.)

**Binding premise, RULED by Jordan 2026-08-20:**

> **`systems/` should stem from `engine/` and `references/`.**

That is not a slogan in this document. It is the acceptance test for Act C, and §1.C measures exactly
how far the tree is from it.

**Authority, granted by Jordan 2026-08-20:** *"Permission to change CLAUDE.md, CI, skills, tools and
other measures that may prevent overhaul from being effected."* Acts A–D exercise that grant. Where a
step edits a blocking gate, the step says so and names its own falsifier.

---

## Method — how this plan was produced, and what that buys

Three **read-only** Fable-5 auditors ran in parallel against the working tree, each receiving the
session's *claimed output* and not its reasoning (the agonist→antagonist relay, `CLAUDE.md` §10;
structural independence via `.claude/agents/valoria-critic.md` — `Read, Grep, Glob`, no write tools).
Lanes: recursion-break efficacy · guardrail depth · centralization and modularity. Opus reconciled
and wrote this plan, and independently verified four further facts (§1.D) that none of the three had
been pointed at.

**Three of the session's own claims were softened or overturned by the auditors, and the corrections
are carried below rather than dropped.** That is the point of the relay. They are marked ⚠.

---

## 0. The one-paragraph answer

**The automated loop is severed. The agent-mediated loop is now mitigated at every carrier the
auditors could find. Neither of those is what is stopping game development.** What is stopping it is
that **`engine/` and `references/` are load-bearing on tools and on prose, and load-bearing on the
game nowhere** — the design repo exports five parameter files that the Godot project does not read a
single byte of, the port's ~90 constants are hand-transcribed with no comparer, `references/` is
loaded at runtime by zero modules in either repo, and `engine/` imports *upward* from `systems/` in
five places so the dependency direction the premise asserts is currently reversed. Meanwhile the game
repo's CI has been **red on `main` since 2026-05-04** and nothing in either repo reports it. The work
is therefore not more doctrine. It is: make the game's gates real and green (Act B), make `engine/` +
`references/` the actual root the premise says they are (Act C), and only then consolidate and cull
(Acts D, E) — because consolidating apparatus before the game has a spine is the loop wearing a new
hat.

---

## 1. What the audits established

Every row is CONFIRMED against the working tree with a file:line, unless marked PLAUSIBLE (a judgment)
or ⚠ (a correction to something this session previously asserted).

### 1.A — Recursion: what was actually still generating

| # | Finding | Status |
|---|---|---|
| A1 | **A second cron survived.** `.github/workflows/dashboard.yml` ran a *daily* `cron: '17 6 * * *'` executing the exact two generators removed from `audit-refresh.yml` — `vector_audit.py --emit-findings` and `build_incompleteness.py` ("whole-tree scan for every stub/null/missing/excluded/unverified thing"), publishing a fresh manufactured-work feed every morning, unattended. Severing one workflow and leaving the other running severed nothing. | **FIXED this session** — see §3.A0 |
| A2 | **An eighth and ninth standing ledger-append order survived** the 2026-08-19 sweep of seven `SKILL.md` files: `valoria-resolution-diagnostic/SKILL.md:272` ("P1/P2/P3 canonical-gap findings append to `registers/editorial_ledger_<lane>.jsonl` — commit gate") and `valoria-module-adjudicator/SKILL.md:148` (same, plus a write into the dissolved `designs/audit/` tree). Both unconditional, neither gated on `needs_jordan`. | **FIXED this session** — see §3.A0 |
| A3 | ⚠ **The banner does not print "only" the game block.** `tools/session_status.py:131-133` prints two apparatus pointer commands and `:135-153` prints up to 12 lines of `HANDOFF.md`'s "## Next actions", which the Stop hook (`session_handoff_reminder.py:14`) nudges each session to write. Session prose → next session's banner, no human between. Today that channel carries the game directive, so it currently *amplifies* the fix — but the §0.3 experiment is confounded: a null result would partly measure `HANDOFF.md`'s content, not the banner reduction. | OPEN — §3.A1 |
| A4 | **The one game signal wired into CI is satisfiable by writing.** `review_core.py:114-115` adds `m1.acceptance` and `valoria-ci.yml:404-411` runs `review_core --check` inside the *required* compliance-check job, so a regression genuinely reds CI. But its two failing rows are `stub_invocations` (awaiting a ruling, `review_baseline.yaml:81-83`) and `m1_junctures`, which counts `state: done` strings in a hand-edited YAML (`m1_acceptance.py:295-302`, self-declared at :317). **Seven one-word board edits green the banner's verdict *and* drive the CI ratchet 2→1.** | OPEN — closed by Act B/C, not by more doctrine |
| A5 | `audit-refresh.yml` is genuinely `workflow_dispatch`-only; the 7 `SKILL.md` strips, the board rewrite, the 34 `FORK:c9b0a86` rows and the compile ratchet are all present as claimed. | CONFIRMED |
| A6 | `tools/audit_registry.py` still exists and works; only a sentence forbids restoring the mandatory append. Prose control over a live mechanism. | ACCEPTED — §4 |

### 1.B — Guardrails: where a wrong game change passes every gate

| # | Finding | Status |
|---|---|---|
| B1 | **Cross-repo constants have no comparer — the worst hole.** `valoria-game` contains **zero `.json` files**. All ~90 numbers in `systems/util/Constants.gd:7-95` are hand-transcribed. The `--check` gates verify *oracle → JSON*; **nothing verifies JSON → `.gd`.** A session can change any game constant in either repo and no gate compares them. | OPEN — §3.C1 |
| B2 | **Zero GDScript tests execute anywhere.** `valoria-game/tests/*.gd` (14 files) are excluded from the ratchet count (`godot-ci.yml:87-88`) and gdUnit4 is not vendored, so no `.gd` test has ever run in CI. The port↔oracle discipline of `CLAUDE.md` §6 (the ED-1050 defect class) has **no executing guard at all**. | OPEN — §3.B3 |
| B3 | **`params_tables.yaml` has no integrity guard.** Its generator was retired with `engine/params/`, making the 43-table capture hand-edit-only, and no CI tool reads it for checking. A silent edit is unobservable. | OPEN — §3.C4 |
| B4 | ⚠ **`CLAUDE.md` §7 is stale: full `mc_v18` campaigns DO run in CI.** `valoria-ci.yml:321` runs `pytest engine/tests`, which executes 50-season campaigns at n=2/seed-0 (`test_mc_v18_regression.py:15`) and n=8/seed-42 (`test_f7_smoke_oracle.py:16`), pinning exact win-share/winners/battles. What is genuinely missing is the n≥100 balance oracle the f7 file itself demands (`test_f7_smoke_oracle.py:8`) and any control on golden *re-pinning*. | CORRECT §7 — §3.D5 |
| B5 | **The compile ratchet can be held at 84 while the project gets worse.** It counts, it does not identify: fix five errors, add five, "OK: held at 84". Move a broken script under `res://tests/` and its errors vanish via the exclusion; the second filter drops any line containing `GdUnitTestSuite` **regardless of path**. And the falling branch has no "did the project actually finish loading" assertion — a crash that makes the grep match nothing reads as improvement. | OPEN — §3.B2 |
| B6 | `systems/characters/sim/` has **zero tests anywhere**, and `test_f7_smoke_oracle.py:23-24` pins `insurgencies_formed`/`npcs_generated` at **0**, so `systems/world/sim/npe.py` and `insurgency_pipeline.py` can be arbitrarily broken and stay green. | ACCEPTED (deferred; the zero-pin trips when a bridge lands) |

### 1.C — The premise: `systems/` does not currently stem from `engine/` + `references/`

| # | Finding | Status |
|---|---|---|
| C1 | **`references/` is not load-bearing at runtime — the central finding.** No `engine/` or `systems/` module loads `module_contracts.yaml` or `descriptor_registry.yaml`; every runtime hit is a comment or docstring (`engine/autoload/game_state.py:106`, `stubwire.py:59`, `substrate/__init__.py:11`). Their only machine readers are apparatus (`ci_names_consistency.py:45`). The rosters code actually runs on are **hardcoded twins** in `game_state.py` (`MULTS`, `ALL_PLAYABLE_15`, the `fac.*` keys). | OPEN — §3.C2 |
| C2 | ⚠ **The dependency direction is inverted, and `CLAUDE.md` §3's "acyclic, autoload is a leaf" is false.** `engine/` imports `systems/` at top level in five places: `engine/mc_v18.py:37-38` (factions, overview), `engine/cross_scale/echo_transport.py:58` (settlements), `engine/cross_scale/parliamentary_bridge.py:64-66` (factions, social_contest ×2). **Autoload is not a leaf**: `engine/autoload/game_state.py:260,368-420` imports seven subsystems' state classes. Package-level cycle: `systems/factions/sim/faction_action.py:42` imports `engine.autoload.game_state` while `game_state.py:384` imports `systems.factions.sim.treaty`. Function-local imports hide it from import-time crashes; they do not remove it. | OPEN — §3.C3, and CORRECT §3 of CLAUDE.md |
| C3 | **Lateral `systems/`→`systems/` imports are widespread**, including a mutual cycle. factions→settlements (`faction_action.py:43`), factions→mass_battle (`:452`), factions→social_contest (`parliamentary_transfer.py:54`, `parliamentary_action.py:41`), overview→settlements+world (`accounting.py:45-51`), world→settlements (`insurgency_pipeline.py:116`), fieldwork→characters (`knots.py:349`), **fieldwork↔threadwork** (`knots.py:364` ↔ `opposing.py:245`). The parliamentary seam is owned twice — once in `engine/cross_scale/parliamentary_bridge.py:64-66` and again laterally in `systems/factions/sim/parliamentary_transfer.py:54`. | OPEN — §3.C3 |
| C4 | **The three-file tax.** Adding or rewiring any subsystem today requires coordinated edits to `engine/autoload/game_state.py:368-420`, `engine/cross_scale/scene_dispatch.py:233-352` (hardcoded per-subsystem dispatch), and `engine/mc_v18.py:37-38`. That is the recurring cost on exactly the game-code commits §0.2 demands. | OPEN — §3.C3 |
| C5 | Contract counts verified: **27 modules, 10 `doc: null`, 11 `[ASSUMPTION]`-grade resolvers** in `references/module_contracts.yaml`. | CONFIRMED |

### 1.D — What Opus verified independently

| # | Finding | Status |
|---|---|---|
| D1 | **`valoria-game`'s CI has been red on `main` since 2026-05-04.** Every `godot-ci.yml` run in the repo's history concluded `failure` (runs `25349663369`, `25349831513` on main; `32221555262`, `32229960921`, `32296379167` on branches). On the newest run the compile ratchet, enum check and lint passed and **`Naming Consistency` failed** — step *"Verify Yrsa Vossen naming"* FAILURE, step *"Verify Solmund naming"* **SKIPPED**. PP-665 renamed Maret Vossen → Yrsa Vossen; 12 live `.gd` sites still say `maret_vossen` (`autoload/Meta.gd:159-164`, `systems/data/ArcEvaluatorRegistry.gd:39,97-99`, `systems/npc/NPCLocationTracker.gd:43`, `resources/data_types/RestorationMovementData.gd:17`) plus `resources/instances/characters/primary/maret_vossen.tres` and `.../triggers/vossen_heresy.tres`. **A red gate has been masking a second gate that has therefore never executed once.** | OPEN — §3.B1 |
| D2 | **The export bridge is generated and ingested by nobody.** `tools/export_engine_params.py`, `export_key_types.py`, `export_sim_params.py` produce `engine/engine_params/{combat_engine_v1,key_types,sim_params,value_pointer_links}.json` + `params_tables.yaml`, each with a blocking round-trip. A grep across all of `valoria-game` for any of those names returns **zero**. The only runtime `FileAccess`/`JSON.parse` sites in the game are scene telemetry (`autoload/SceneTimer.gd:301,320`, `systems/util/TimeAggregator.gd:28,34`). | OPEN — §3.C1 |
| D3 | **No ttrpg tool targets the game clone.** `grep -rl "valoria-game" tools/ .github/ skills/` matches only `tools/dashboard_data.py` and observability blobs. `valoria-game/docs/design_sync.md` is a hand-written 2026-05-04 snapshot. | OPEN — §3.C1 |
| D4 | **The game already disagrees with the registries, and is sometimes ahead of them.** `Constants.gd:28` declares `ATTRIBUTE_COUNT = 10` — the roster Jordan ruled 2026-08-14 — while `references/descriptor_registry.yaml` still ships **nine** with the tenth unnamed. `Constants.gd:85-86` declares `FACTION_STAT_MIN=0 / MAX=7`, a **fifth** variant of the faction-stat roster that `CLAUDE.md` already records as disagreeing across four surfaces. `Constants.gd:43-45` (`COMBAT_POOL_BASE=3`, `_AGI_MULT=2`, `_MINIMUM=5`) is a **fourth** definition of Combat Pool. No gate observes any of this. | OPEN — §3.C1, §7 |
| D5 | **Godot version conflict.** `valoria-game/project.godot:11` declares `features=("4.3")` and CI pins the 4.3 binary, while `CLAUDE.md`'s header and `godot/` docs say **4.6**. One of the two is wrong; a 4.3 binary parsing a 4.6-authored tree can mis-count the ratchet. | OPEN — §7 (Jordan) |

---

## 2. The corrected model — what is actually left of the loop

`CLAUDE.md` §0.3's three terms hold, with one correction and one addition:

- **T3, the generator.** Its *automated* arm is now fully severed: after §3.A0 there are **zero `cron:` entries in the entire repository**. Its *agent-mediated* arm ran through nine prompt-level standing orders; all nine are now removed. What remains is A6-class: the mechanisms still exist and only prose forbids their unconditional use. That is the honest residual, and §4 says why it is accepted rather than "fixed" with another guard.
- **T1, the amplifier.** Reduced to one game block, **plus** a `HANDOFF.md` relay the session writes at Stop (A3). The §0.3 experiment is therefore not the clean single-variable test it claims to be.
- **T2, the reward.** Still the deepest term, and **unchanged by any of this session's work**. A session is graded at Stop on clean tree · handoff · board · no regression. `m1.acceptance` was wired in to give it one game-facing signal, and A4 shows that signal is greenable by editing seven words in a YAML file. **T2 is not closed by doctrine; it is closed by Act B and Act C, because an execution artifact cannot be written.**
- **T4, newly named — the asymmetry of attention.** The design repo runs 36 validators green while the game repo has been red for three and a half months (D1) and nothing anywhere reports it. Every gate this project owns points at the artifact that is *not* the deliverable. This is the term the plan below actually attacks.

---

## 3. The plan

Ordering rule: **nothing in Acts D or E starts until Act B is green and Act C1 exists.** Consolidating
and culling apparatus while the game has no spine is the loop with better manners.

### ACT A — finish severing the generator

#### A0. DONE THIS SESSION (recorded here so the plan is honest about its own starting state)
1. `.github/workflows/dashboard.yml` — daily `cron` removed; the `vector_audit --emit-findings` and
   `build_incompleteness.py` steps removed. `tools/dashboard_data.py` degrades gracefully (both
   readers return `available: false` with a note at `:1125` and `:1175`), so the cards read "not
   generated". **Repo-wide `cron` count is now 0.**
2. `skills/valoria-resolution-diagnostic/SKILL.md` and `skills/valoria-module-adjudicator/SKILL.md` —
   the two surviving unconditional ledger-append orders removed and replaced with the §0 rule (fix it
   or drop it; at most one row, `needs_jordan: true` only). The adjudicator's write into the dissolved
   `designs/audit/` tree removed in the same edit.
   Verified: `ci_hooks_verifier` "enforcement architecture intact"; `ci_claude_workflow_paths` 166
   referenced / 0 dead; all three workflow YAMLs parse.

#### A1. Close the banner's second channel — **or** stop calling the experiment single-variable
`tools/session_status.py:135-153` relays `HANDOFF.md`'s "## Next actions" into the banner.
**Do exactly one of these, in one commit, and say which in the commit message:**
- **(a) preferred** — drop the relay; print instead a single line: `HANDOFF.md "Next actions": N lines — read it if you are resuming.` The banner then carries no session-authored prose at all and §0.3's "change nothing else" becomes true.
- **(b)** — keep it, and amend `CLAUDE.md` §0.3 to state that the experiment has two variables and that a null result does not falsify the ordering.
Falsifier: `tests/valoria/test_session_status_banner.py` (if absent, this is the one new test Act A
earns — its subject is what a session *sees*, which is T1, and T1 is load-bearing on whether game work
happens; under §0.1 pt 5 that is a Jordan-decision-adjacent artifact, so state that justification in
the test's docstring or do not write it).

#### A2. Retire the last executable driver pointing at the superseded queue
`.claude/wf_return_to_game.js:358` still holds `const QUEUE = 'workplans/return_to_game_queue.yaml'`
and its header (`:3`) says it "Executes ONE step" of a queue whose own file says **DO NOT RUN THE
DRIVER**. Prose guarding a live mechanism — the exact pattern §0's correction retracts.
- Move `.claude/wf_return_to_game.js` to `deprecated/claude/` and delete the queue's "HOW TO RUN IT"
  section, **or** repoint the driver at `workplans/workplan_v6_progress.yaml`. Prefer the move: the
  board is not a step queue and pretending it is re-creates the thing being retired.
- Same commit: run `python tools/ci_claude_workflow_paths.py` (every `.claude/` path must resolve)
  and `python tools/ci_wf_harness_check.py`.

### ACT B — make the game's gates real and green

**This act is the T4 fix. It is game work. It comes before every consolidation.**
Branch: `claude/return-to-game-s1-compile` in `jordanelias/valoria-game` (PR #2 open).

#### B1. Turn `main` green — finish PP-665
Twelve `.gd` sites plus two `.tres` files still say `maret_vossen` (D1). In one commit:
1. Rename the identifier `maret_vossen` → `yrsa_vossen` across `autoload/Meta.gd:159-164`,
   `systems/data/ArcEvaluatorRegistry.gd:39,97-99`, `systems/npc/NPCLocationTracker.gd:43`,
   `resources/data_types/RestorationMovementData.gd:17`.
2. `git mv resources/instances/characters/primary/maret_vossen.tres .../yrsa_vossen.tres` and update
   every `.tres` `ext_resource` path that points at it (grep `maret_vossen` across `*.tres` — do not
   assume only the one file references it).
3. Grep `Maret Vossen` in display strings and dialogue; the CI pattern matches the spaced form too.
4. **Do not touch `maret_uln`** — a different character; the rename is Vossen-only.
5. Verify locally with the gate's own command:
   `grep -rn "Maret Vossen\|maret_vossen" --include="*.gd" --include="*.tres" .` → empty.
**Done-condition:** the `Naming Consistency` job goes green **and its second step actually executes
for the first time** — check the job's step list, not just the job conclusion. If "Verify Solmund
naming" then fails, that is a real finding that has been invisible since May; fix it in the same PR.

> ✅ **EXECUTED 2026-08-20** — `valoria-game` commit `4f6e2c6`. All 12 `.gd` sites and both `.tres`
> files renamed; canonical form verified against `references/names_index.yaml:242` rather than
> assumed. **The prediction held: the masked gate was also red.** Once step 3 was allowed to pass,
> step 4 would have failed on `docs/conversion_ledger.md:157` — a historical migration row naming
> the deprecated token as data. Excluded by basename on the same rationale as `ci_naming_check.py`'s
> `EXCLUDE` list, not by directory, so a real use elsewhere still fails. The Yrsa step was widened to
> `*.tres` in the same commit: the data layer had been slipping a gate the code layer could not.

#### B2. Harden the compile ratchet against B5's three evasions
Edit `/workspace/valoria-game/.github/workflows/godot-ci.yml`, step "Open the project headless and
count errors":
1. **Load sentinel before comparing.** After the run, assert the log shows the editor actually
   started and finished scanning; abort with a distinct message if not. Without this, a crash that
   produces no matching lines reads as "errors fell — lower the baseline", and a compliant session
   ratchets toward a vacuous 0.
2. **Tighten the exclusion.** `grep -v "GdUnitTestSuite"` currently drops that string *anywhere*,
   including game code. Replace with a path-anchored exclusion only (`^res://tests/`), and delete
   even that in B3 once the tests run.
3. **Identify, don't just count.** Write the sorted, path-normalised error *signatures* to
   `errors.txt` and commit a companion `.godot-compile-errors` list; fail if the *set* changed even
   when the count did not. This is what closes "fix five, add five".
Falsifier, stated in the commit: re-run the job on the unchanged tree — it must still report 84 and
green; then locally introduce one new parse error in a non-test `.gd` and confirm the job fails on the
**set** comparison rather than the count.

#### B3. Make one GDScript test execute
Currently zero `.gd` tests run anywhere (B2/§1.B). gdUnit4 vendoring is blocked (403 through the
proxy — retry once; if it fails again, do not spend the act on it):
- **Fallback that needs no dependency:** add `tests/run_all.gd`, a `SceneTree` script that
  instantiates the handful of pure-logic classes with no scene dependencies (`Constants`,
  `RollContext`, `RollResult`, `ObModifier`, `PoolModifier`), asserts a few known values, and exits
  non-zero on failure. Add a CI step after the compile job:
  `./Godot_v4.3-stable_linux.x86_64 --headless --path . -s tests/run_all.gd`
- Drop the `res://tests/` exclusion from the ratchet in the same commit **only for the files that now
  run**; leave gdUnit4-dependent suites excluded with a comment naming the 403.
**Done-condition:** a CI step whose failure is caused by GDScript behaviour, not by parsing.

### ACT C — make `engine/` + `references/` the root the premise says they are

**This is the architecture act and the answer to "centralization and modularity".** Each step composes
on a primitive that already exists rather than inventing one.

#### C1. Cross-repo constants parity — the single highest-value guard in this plan
Closes B1(hole), D2, D3, D4 at once. It is apparatus by subject and **load-bearing on the game** by
output, which is exactly the distinction `CLAUDE.md` §0.1 pt 5 draws — so it earns its existence.
1. In `jordanelias/ttrpg`, add `tools/export_game_constants.py` following the shape of
   `tools/export_key_types.py` (ED-IN-0136) — the fourth instance of the generate + blocking
   `--check` round-trip pattern. It emits `engine/engine_params/game_constants.json`: a flat
   `{NAME: value}` map assembled from the *single owners* of each value —
   `systems/combat/combat_engine_v1/config.py`, `engine/autoload/game_state.py`, and the sim params
   already captured in `sim_params.json`. **Emit only names that have a single owner in Python.**
   Every name it cannot source is written to a `"_unsourced"` list in the same file — that list is
   the honest measurement of how much of the game has no oracle, and it is expected to be large on
   day one.
2. Commit `game_constants.json` into `valoria-game` at `resources/generated/game_constants.json`
   (the game repo has zero `.json` files today; this is the first).
3. Add `valoria-game/tools/check_constants_parity.py` (~60 lines, no Godot binary): regex-parse
   `const NAME: type = value` from `systems/util/Constants.gd`, compare **by key** against the JSON,
   and fail on any key present in both with different values. Keys only in `.gd` are reported, not
   failed (that is the `_unsourced` frontier). Wire it as a new `godot-ci.yml` job.
4. **Expected first result: RED, and that is the deliverable.** `ATTRIBUTE_COUNT`, the faction-stat
   bounds and Combat Pool (D4) will disagree. Do **not** "fix" them by editing `Constants.gd` to
   match — three of those are open design questions (§7). Land the guard with the known-divergent
   keys in an explicit `KNOWN_DIVERGENT` list, each entry naming the ED or ruling that will close it,
   and a test asserting that list can only **shrink**. Same ratchet discipline as
   `.godot-compile-baseline`.
5. Delete `valoria-game/docs/design_sync.md`'s claim to be the sync record, or repoint it at this
   mechanism. A hand-written 2026-05-04 snapshot is not a bridge.

#### C2. Make `references/` load-bearing at runtime
Today `descriptor_registry.yaml` and `module_contracts.yaml` are read by apparatus only (C1 in §1.C),
while the rosters code runs on are hardcoded twins in `engine/autoload/game_state.py`.
- Add `tools/export_rosters.py` + blocking `--check` (fifth instance of the same pattern) generating
  `engine/engine_params/rosters.py` — a generated module holding the attribute roster, the faction
  stat roster and their bounds, sourced **from `references/descriptor_registry.yaml`**.
- Change `engine/autoload/game_state.py` to import from the generated module and **delete** the
  hardcoded `MULTS` / `ALL_PLAYABLE_15` twins. The registry becomes the writer; code becomes the
  reader. That is the premise, executed.
- Blocked-on for the attribute roster: Jordan's tenth attribute is unnamed (§7-Q1). Generate the nine
  that exist plus an explicit `PENDING_TENTH` sentinel so the generator is not blocked on the ruling;
  the sentinel's presence is itself the reminder.

#### C3. Invert the dependency direction — registration-driven seams
This is the ONE architectural change the modularity audit named, and it is what makes the premise
structurally true rather than aspirational.
- **Target:** `engine/` never names a `systems.*` module. Today it does in five places
  (`mc_v18.py:37-38`, `cross_scale/echo_transport.py:58`, `cross_scale/parliamentary_bridge.py:64-66`)
  and `engine/autoload/game_state.py:260,368-420` imports seven subsystems' state classes.
- **Mechanism:** add a registration point in `engine/substrate/` — each `systems/<sub>/sim/` registers
  its resolver and state class at import; `engine/cross_scale/scene_dispatch.py:233-352`,
  `engine/mc_v18.py` and `game_state.py` consume the registry instead of importing by name. The
  registry's **legal roster is loaded from `module_contracts.yaml`** via C2's export — so an
  unregistered or undeclared subsystem is an error, not a silent gap.
- **Do this incrementally, one seam per commit, goldens green each time.** Suggested order, cheapest
  first: (1) `echo_transport` (one import), (2) `mc_v18` callbacks, (3) `parliamentary_bridge` —
  and in the same commit delete the lateral duplicate at
  `systems/factions/sim/parliamentary_transfer.py:54`, which owns the same seam a second time,
  (4) `game_state` state classes, (5) `scene_dispatch`.
- **The falsifier is cheap and belongs in the same commit as step 1:** a test asserting
  `engine/**/*.py` contains no top-level `import systems.` / `from systems.` — parameterised so each
  seam is removed from an allow-list as it lands, and the allow-list can only shrink. This guard's
  subject *is* the game's architecture, so it earns existence; without it, step 5 will silently
  re-import.
- **Lateral `systems→systems` (C3 in §1.C) is a separate, later sweep.** Fix the mutual cycle
  `fieldwork↔threadwork` (`knots.py:364` ↔ `opposing.py:245`) first, because a cycle is the only one
  of these that can produce a real import-order bug. The rest are debt, not defects.

#### C4. Pin the params capture
`params_tables.yaml` is hand-edit-only and unguarded (B3 in §1.B). Add
`tests/valoria/test_params_capture_pin.py` asserting `sha256(engine/engine_params/params_tables.yaml)`
equals a pinned digest. It is frozen by design, so any edit must consciously move the pin. Load-bearing
under the predicate: it *is* the exported-params surface the port ingests.

### ACT D — centralization, with two of five rows corrected

Only start after B is green. Each row below is a §8 "every rule lives once" repair.

- **D1. `pathres.py` becomes the actual sole parser — but the finding is sharper than "four parsers".**
  The row *grammar* agrees across all five sites; **FORK semantics disagree three ways**:
  `pathres.py:184-191` returns a `FORKED` status; `broken_dependency_checker.py:164` returns the
  string `FORK:<ref>:<original-ref>`; `ci_claude_workflow_paths.py:110-149` has **no FORK handling at
  all** and resolves a forked file to `None`. Same ledger, three different answers about the same row.
  Fix the *semantics* first (decide what a FORK row resolves to, once), then port the call-sites.
  ⚠ Implementer caveat: `pathres.resolve(max_hops=1)` claims (`pathres.py:165`) to reproduce `bdc`
  exactly and **does not** reproduce its `FORK:<ref>:<ref>` pairing format, which `bdc`'s caller
  checks — a drop-in port silently changes output. Sites: `pathres.py`,
  `broken_dependency_checker.py:108-117,142-165`, `ci_claude_workflow_paths.py:105,110-149`,
  `skills/valoria-vector-audit/scripts/vector_audit.py:418-430`, `.../workbench.py:70-79`.
  `gen_audit.py:355,631` already composes correctly — leave it.
- **D2. Naming trio — SOFTENED to a two-of-three merge.** `ci_names_check.py:16-18,28-37` already
  imports `ci_common`, `names` and `ci_naming_check` — it is a *facade*, not a duplicate rule, and
  merging it buys an entry point, not a deduplication. `ci_names_consistency` checks a genuinely
  different invariant (mirror-field equality between `names_index.yaml` and
  `descriptor_registry.yaml`/`proper_noun_registry.yaml`). Two costs to price before merging:
  the blocking/report-only split is caller-side (`valoria_local.py:156-157`) so a merged exit code
  must multiplex severities; and `ci_names_consistency` hard-requires PyYAML (`:26-30`) while the
  register-size validators deliberately avoid it — merging pulls PyYAML into the blocking naming gate.
  **Recommendation: merge the facade, leave `ci_names_consistency` standalone.**
- **D3. `compliance_check` absorbs `ci_register_size_check` — CONFIRMED, one hard precondition.**
  Both enforce one rule from one source (`ci_register_size_check.py:13-39` and
  `compliance_check.py:193-206` both read `max_tokens` from `references/atomization_rules.yaml`).
  But register sizes are locally **blocking** (`valoria_local.py:160`) while `compliance_check` is
  deliberately absent from the local list (`valoria_local.py:226`, still true). **Add
  `compliance_check` to `valoria_local.py` in the same commit** or local-green silently loses register
  caps.
- **D4. `broken_dependency_checker` absorbing `freshness_gate` — OVERTURNED. Do not do it.** The
  culling plan's justification ("both walk `canonical_sources.yaml`") conflates two invariants: `bdc`
  checks *referenced paths exist* (`:94-99`); `freshness_gate` checks *pinned blob OIDs match content*,
  LF-normalised, and has a **writer** mode `--update` (`:4-28`). No shared rule body exists to
  deduplicate — this is aggregation, not §8 consolidation — and merging blurs a read-only checker with
  a pin-writer. **Strike this row from the culling plan.**
- **D5. One owner of M1 state.** Board readers: `session_status.py:57`, `m1_acceptance.py:71`,
  `workplan_status.py:29`, `scope_ratchet.py:331,365`. Handled by A2 (retire the driver); the
  remaining queue references (`tests/valoria/test_m1_acceptance_probe.py:1,103`, `m1_acceptance.py:11`)
  are prose citations and are fine as history.
- **D6. Correct the three false/stale claims the audits found in `CLAUDE.md`** — in one commit, with
  the evidence inline: §3's "acyclic, autoload is a leaf" (false, C2 in §1.C); §7's "no CI job executes
  full `mc_v18` campaigns" (stale — `valoria-ci.yml:321` does, at n=2 and n=8; the real gap is the
  n≥100 balance oracle and the unguarded golden re-pin); and the Godot **4.6 vs 4.3** conflict (§7-Q3).

### ACT E — the remaining culling waves (`2026-08-18-culling-plan-v1.md`, still RATIFIED)

Unchanged in content; the ordering below was already adjudicated and is restated so it is not
re-derived. **Starts only after Act B is green.**
1. **6b before 6a** (6a's flip list is computed from 6b's result).
2. **Wave 1 with `tools/m1_acceptance.py` carved out** — §0.2 made it the instrument one day after the
   plan was ratified; culling it would delete the gate that says `done`.
3. **Wave 5 with the flip list regenerated**, adding `systems/*/_identifier_census.yaml` (~24,598
   lines) which the plan omitted.
4. **Wave 2**, then **6f**, then **6c**.
5. ⛔ **Wave 3 does NOT run** while the §0.3 banner experiment is live — it edits the surface under
   test. Revisit after one session's evidence.
6. **D4 above is struck from the plan** (`culling-plan-v1.md:344`).

---

## 4. What NOT to do — the failure modes this plan is exposed to

- **Do not write a guard whose subject is this plan.** No `test_plan_compliance`, no
  `check_acts_executed`, no progress register for the acts. `CLAUDE.md` §0.1 pt 5 forbids it and the
  tree already records what happens at depth five.
- **Do not "fix" A6 with a mechanism.** `tools/audit_registry.py` still works and only prose forbids
  its unconditional use. Building a gate to enforce a prose rule about not generating findings is the
  loop's exact shape. Accept the residual; the tripwire is that the appends are visible in `git log`.
- **Do not resolve C1's expected red by editing `Constants.gd`.** Three of the divergences are open
  design questions. A guard whose first act is to erase the disagreement it found has measured nothing.
- **Do not start Act D or E early because they are enumerable.** That preference — apparatus work is
  finite and satisfying, game work is not — is the mechanism `CLAUDE.md` §0.3 measures.
- **Do not re-derive an inventory.** `references/apparatus_registry.yaml`,
  `references/ci_checks_registry.yaml`, `references/restructure_ledger.md` and the two 2026-08-18
  proposals already hold them. Cite; do not rebuild.
- **Do not schedule a check-in.** `CLAUDE.md` §11; seven denied primitives; the rule overrides any
  hosted instruction to the contrary.

---

## 5. Sequencing summary

| Order | Act | Gate that says it is done |
|---|---|---|
| 1 | A0 | ✅ done — 0 crons repo-wide; 9/9 standing append orders removed |
| 2 | A1, A2 | banner carries no session prose (or §0.3 amended); no executable driver targets the retired queue |
| 3 | **B1** | `godot-ci.yml` green on `valoria-game` `main` for the first time since 2026-05-04, with the Solmund step *executed* |
| 4 | B2, B3 | ratchet compares error **sets**; ≥1 GDScript test executes in CI |
| 5 | **C1** | a parity job exists, is red on a `KNOWN_DIVERGENT` list that can only shrink, and the game reads its first `.json` |
| 6 | C2, C4 | `game_state.py` has no hardcoded roster twin; `params_tables.yaml` is pinned |
| 7 | C3 | `engine/**` contains no top-level `import systems.`; allow-list can only shrink |
| 8 | D1–D6 | one FORK semantics; one register-size owner; three CLAUDE.md corrections landed |
| 9 | E | waves in the order above; wave 3 held |

**The `m1_acceptance` verdict is not the gate for any row above.** It is doc-derived on the row that
aggregates (A4). Each row's gate is an execution artifact of its own.

---

## 6. What this plan does not solve

- **T2 is only half-addressed.** Acts B and C give the Stop-time grade something it cannot satisfy by
  writing, but the Stop hook itself still grades clean-tree/handoff/board. Rewriting the reward is a
  Jordan decision, not an agent one, and it is deliberately not attempted here.
- **`m1_acceptance` row 4 stays doc-derived** until a per-juncture execution artifact exists — which
  is true for none of the seven today. Acts B and C produce the first two.
- **The n≥100 balance oracle is still absent** (B4), and the golden re-pin path is still uncontrolled.
- **`systems/characters/sim/` still has zero tests** and `npe.py`/`insurgency_pipeline.py` are pinned
  at 0 (B6). Deferred deliberately: that code is unreachable until a bridge lands, and the zero-pin
  trips when one does.

---

## 7. Jordan's queue — the rulings that gate work above

| Q | Question | What it blocks | Where the evidence is |
|---|---|---|---|
| **Q1** | **The faction-stats packet** — the roster disagrees across **five** surfaces now: `descriptor_registry.yaml:103-111` (5 stats, Influence 1-7), `engine/autoload/game_state.py:101-111` (6), `canonical_registry.md:113` (Wealth/Military 1-7), `generation_sourcebook_v1.md:34` (a fourth), and **`valoria-game/systems/util/Constants.gd:85-86` (`MIN=0/MAX=7`, a fifth)**. ED-FA-0004 open. | M1 junctures 1 and 4; the `score/2` obstacle derivation; C1's `KNOWN_DIVERGENT` list; C2's roster export | `HANDOFF.md:209+` — still "NEEDS JORDAN … not ruled" |
| **Q2** | **Name the tenth attribute.** You ruled "it will be 10 attributes" (2026-08-14); the registry ships nine and `valoria-game/systems/util/Constants.gd:28` already declares `ATTRIBUTE_COUNT = 10`. The game is ahead of the registry. | C2's roster generator (it ships a `PENDING_TENTH` sentinel until then, so it is not fully blocked) | `CLAUDE.md` §5 |
| **Q3** | **Godot 4.3 or 4.6?** `project.godot:11` says `4.3` and CI pins the 4.3 binary; `CLAUDE.md` and `godot/` say 4.6. | the meaning of the compile ratchet's 84 | §1.D5 |
| **Q4** | **ED-SC-0003 / 0004 / 0005** — all `status: open`, `needs_jordan: true`. 0004 (the canonical Argue-pool formula) has two contradictory live implementations. ⚠ Before treating 0005 as a third item, read ED-SC-0017: it argues the bonus-die cap is already ruled by canon and enforced in code. | M1 juncture 3, hard-blocked | `registers/editorial_ledger_sc.jsonl` |
| **Q5** | **A1's choice** — drop the banner's `HANDOFF.md` relay, or keep it and amend §0.3? | Act A1 | §3.A1 |
| **Q6** | `registers/editorial_ledger_in.jsonl:50-51` — **two rows share id `ED-IN-0194`** with conflicting `needs_jordan`. Reported 2026-08-19, not ruled. | ledger integrity | — |
| **Q7** | `registers/editorial_ledger_in.jsonl` has ~108 tokens of headroom under a blocking cap (ED-IN-0185 Q5). Raise the cap, split the file, or accept that IN cannot file. | any future IN row | `culling-plan-v1.md` preamble |

---

## 8. Provenance

Produced 2026-08-20 on branch `claude/return-to-game-execution-74fdvc`. Three read-only Fable-5
auditors (recursion efficacy · guardrail depth · centralization/modularity), each given the session's
claimed output and not its reasoning, each with `Read, Grep, Glob` only. Opus reconciled, verified
§1.D independently, and wrote this. Auditor corrections carried rather than dropped: the banner claim
(A3), the `mc_v18` CI claim (B4), and the `freshness_gate` merge (D4) — one softened, one stale, one
overturned.
