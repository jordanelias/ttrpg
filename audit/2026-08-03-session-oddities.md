# Open oddities — everything measured this session and left unresolved (2026-08-03, ED-IN-0123)

## Status: RECORD. Not a work plan, not a proposal. Every entry below was **measured**, and the
## measurement is stated so the next reader can re-run it rather than trust it. Nothing here is
## inferred from a docstring; where a docstring was the source, that is called out as the defect.

Written at session close so these stop living in one session's context. Grouped by what a reader
would be doing when they hit each one.

**Two kinds of entry, never mixed.** Sections A–H and P are **measured facts** — each carries the command
or file that produced it, so re-run rather than trust. Section J is **open questions** — each states
what would answer it and what it is blocked on. A question is not a finding; do not cite J as if it
were a measurement. Section K records what was deliberately left undone.

**Read J first if you are picking up the fork.** Several measured entries are downstream of a single
unanswered question (J1), and resolving it retires them without any of them being "fixed".

---

## A. Gates that misreport

| # | Oddity | Measured |
|---|---|---|
| A1 | **`All Gates Green` counts *cancelled* jobs as failures.** So it goes red on any push that supersedes a running build, with no defect behind it. Nine wakes this session resolved to this or to A2. | `needs.json` shows `unit-tests: cancelled` → `FAILED (not success)` |
| A2 | **`main` is CI-red (9 tests), so every PR's aggregate is red.** A real regression and the background are indistinguishable. | Re-measured 2026-08-03 at merge-base `f09984e6` (== `origin/main`), as a paired control: the **same 9 selectors give an identical `7 failed, 2 passed, 1 skipped` on an unmodified `origin/main` worktree and on this branch**. The branch adds nothing. (Earlier reading of "8 fail locally" was against the older head `80918f6d`.) |
| A3 | **`ci_co_file_checker` rule 3 fires on the canon mass-battle engine's own source.** Any edit under `tests/sim/` — including a comment-only one — demands a `coverage_matrix.md` update. It fires because the CANON engine is misfiled under `tests/`. | A comment-only edit to `config.py` tripped it; digest verified byte-identical (`ccdf7d09…`) before and after |
| A4 | **`freshness_gate` has ~12 stale `canonical_sha__` pins** and is report-only until refreshed. | CLAUDE.md §8; `python3 tools/freshness_gate.py --update` |
| A5 | **`test_gauge_invariants` XPASS count varies run to run.** Not flaky code — a statistical test whose own docstring says an XPASS at n=24 is a prompt to re-measure at n=60, not evidence of a fix. | 1 vs 2 xpassed across identical local runs |
| A6 | **`test_conditional_withdraw_fires_when_enemy_closes` passes locally and fails in CI — on `main`'s own code.** So `main`'s CI-red set (9) is larger than its local-red set (7) for two *different* reasons: `byte_exact_cell_mode` skips locally, and this one genuinely diverges. A local green on an MB test is therefore not evidence CI will be green. | Local `-p no:randomly`, both trees: passes. CI job 91817241826 (`gw3`, xdist): `stance=='retreat'` holds, `yielding is False` — the order fired but only half its behaviour applied |

## B. Registry / contract data

| # | Oddity | Measured |
|---|---|---|
| B1 | **`mass_battle`'s contract has `sim_module: None`** — the only `build: live` module with no code pointer at all. Distinct from the 13 units that use the string `"none"`. | `references/module_contracts.yaml`; the pointer you'd write depends on the unresolved canon-vs-live tree |
| B2 | **Only 10 of 27 contracts declare a file `sim_module`;** 3 more declare a directory. 14 declare nothing (all `design`/`deferred` — correct, they have no code). | `tools/build_execution_map.py` reality_check |
| B3 | **`social_contest`'s pointer is narrower than its own code.** `systems/social_contest/sim/contest/` excludes `parliamentary_vote.py`, a *sibling* of `contest/`, which accounts for **276 calls** that therefore attribute by path guess. CLAUDE.md §3 slice 7 says that file does belong to social_contest. | Reported, deliberately **not** edited: a canonical-registry change on a session's judgement for 276 calls of attribution |
| B4 | **36 unwired fork files have no contract pointer at all** — they cannot be joined to a build state. | `FORK_MANIFEST.json` |
| B5 | **One contested scalar:** `CI (Church Influence)` is claimed as owned state by BOTH `ci_political` and `territorial_piety`. | 37 owned scalars across 35 units, 1 contested — `references/execution_map.json` §4 |
| B6 | **2 key types have no producer; 8 have no consumer.** A type with no producer cannot fire; one with no consumer means nothing reacts. **Now named** (2026-08-03): no producer = `*` (see B7) and `meta.legacy_event`. No consumer = `env.crisis`, `mechanical.era_transition`, `mechanical.season_change`, `mechanical.second_calamity`, `mechanical.settlement_captured`, `mechanical.theocracy_unification_declared`, `meta.legacy_event`, `state.settlement_revolt`. `meta.legacy_event` is on **both** lists — declared, produced by nothing, consumed by nothing. | 46 of 56 types have both — `references/key_graph.json` |
| B7 | **RESOLVED 2026-08-03 — `*` is a literal wildcard, and the graph builder does not know it.** `module_contracts.yaml` gives BOTH `articulation_layer` and `fieldwork_knots` `consumes: [{type: '*', from: engine}]`, meaning "any key". The key-graph builder treats `*` as a type name, so the graph gains a phantom 56th type with `producers: []` and `well_formed: false`. **The real defect is upstream:** "consumes everything" is not a subscription a Godot `KeyBus` can implement, and it means `fieldwork_knots`' actual input set is undeclared. `articulation_layer` additionally emits nothing, so in the graph it is a pure sink. | `references/key_graph.json` `keys["*"]`; `module_contracts.yaml` — the two `consumes` blocks |

## C. Prose that contradicts code

| # | Oddity | Measured |
|---|---|---|
| C1 | **`PC_CELL_MORALE` ships ON under a comment saying "RETRACTED to OFF 2026-07-25".** | Git settles it: `584c683a` set `'0'` (comment true), `94bb9022` (PR #271, 2026-07-29) flipped to `'1'` under the flags-ON directive and left the comment. **Do not fix from an IN-lane PR — see A3.** |
| C2 | **`test_stochastic_rout`'s docstring asserts `config.py:100, default '0'`.** Corrected 2026-07-29; PR #271 invalidated it hours later the same day. Its whole analysis assumes the flag ships OFF. | Code reads `'1'` |
| C3 | **`engine/params/*.md` — 43 prose tables — has ZERO readers** in `engine/` or `systems/`. Consumed only by drift-checkers. | Left behind by the fork; if any value there is canon the code does not hold, it is lost at the fork point. "No reader" is not "no value" |

## D. Engine behaviour

| # | Oddity | Measured |
|---|---|---|
| D1 | **Battles are one-turn routs with an untouched winner.** Jordan ruled 2026-08-03 this is **not** correct, so it is a real defect (F1-class), not a balance opinion. | 60 identical 1200v1200 Line battles: **60/60 end in 1 turn**; winner takes **zero** losses in **42/60**; loser's median loss 45.3% |
| D2 | **`Faction.L` does not reconstruct from the Key log.** 30 of `Faction.adjust()`'s 31 non-test call sites emit no Key. | Off-clamp horizons: 0/3, 0/3, 0/4; best 3/4. Falsifier `tests/valoria/test_faction_l_reconstruction.py` (strict xfail) |
| D3 | **`mass_seizure` is unreachable** — zero production callers, no owner write in 40 seeded campaigns. Its gate is not the obstacle: CI ≥ 60 met in **20/20** seeds, CI = 100 (the FORCED point, P=1) reached in **8/20**. A ratified mechanic whose trigger is routinely satisfied and which never runs. | Instrumented `Territory.__setattr__` |
| D4 | **No trigger anywhere emits a combat scene.** `personal_combat` (port-rank 0, the golden path) is unreachable for that reason, not because of a flag. | 29 scene slots per campaign, **all** `contest`; `evaluate_triggers` can only emit `contest` |
| D5 | **Flipping `DISPATCH_COMBAT_BRIDGE` ON changes nothing at all.** | Same 157 keys, same composition, same winner, byte-identical `Faction.L` and `Territory.owner` |
| D6 | **`run_campaign(max_seasons=N)` is silently shadowed** by `effective_params['CAMPAIGN_SEASONS']`. A season sweep passing `max_seasons` varies nothing — a control that controls nothing reads exactly like a control that does. | Cost me a four-horizon sweep that ran identically four times |
| D7 | **`world.battle_count` counts attacker VICTORIES, not battles.** | Seed 42: 62 battles resolved, 29 reported |
| D8 | **Two disjoint mass-battle trees, and the LIVE one is the stale one.** Canon (ED-MB-0043) is `tests/sim/mass_battle/` — 28 modules, `PC_*` flags in 12 files, CI goldens run its `bat.py`. The campaign imports `systems/mass_battle/sim/massbattle` — 5 modules, zero flags. **Every MB result is measured on a tree the campaign never executes.** | `faction_action.py:431` |

## E. The fork

| # | Oddity | Measured |
|---|---|---|
| E1 | **`build_fork.py` is a ONE-WAY build** (`rmtree` first). Re-running clobbers fork-side commits. Fine while the fork is a pure derivative; wrong the moment it diverges — which is the point of forking. | The open decision: does `main` keep moving? If yes, a GitHub fork with shared history is close to forced |
| E2 | **The fork carries BOTH mass-battle trees**, deliberately. Canon at `systems/mass_battle/canon/`. Blocked on `degree` — **see section H for the exact shapes**, which correct this row's earlier summary | Picking one silently would design that ruling by implication |
| E3 | **225 `.md` against 206 `.py`** even after `LEAVE` was enforced. The remainder is subsystem design documentation, carried on purpose — but the fork is **process-prose-free, not prose-free**, and that distinction should not be blurred | `find` over the assembled tree — **but see E5** |
| E4 | **Only 58 of 206 carried files are reachable from `engine.mc_v18`.** The other 148 are tests, oracles, canon-awaiting-wiring and unwired subsystems — the backlog, not detritus | `FORK_MANIFEST.json` — **but see E5** |
| E5 | **⚠ E3 and E4's numbers have no artifact in this repo.** `build_fork.py` writes `FORK_MANIFEST.json` *into its output tree* (`--out`, required, no default), and the fork was never committed — so `find . -name FORK_MANIFEST.json` returns nothing. By this record's own standard (§0.1 point 3) those counts are currently unfalsifiable. They are believed accurate; they are not checkable until someone re-runs the assembler. **B4's "36 unwired files with no contract pointer" has the same problem.** | `grep -n FORK_MANIFEST tools/build_fork.py` → one hit, line 399, inside the output writer |

---

## F. Errors this session made and caught — recorded because the CLASS recurs

Every one was a **false absence from a proxy**, and each was caught by reading output rather than
by a test going red. That is the pattern worth carrying forward, not the individual bugs.

1. **An AST scan for attribute assignments reported ZERO non-test writes to `Faction.L`.** False:
   `Faction.adjust()` writes via `setattr(self, stat, val)`, which no attribute-target scan can see
   — and 31 call sites route through it.
2. **`Faction.L` scored 4/4 reconstructed.** False: 3 of 4 factions sat exactly on a clamp, where a
   clamped rebuild agrees with a clamped actual regardless of the deltas. I flagged that risk in
   writing and banked the flattering number anyway.
3. **"mass_battle is 98.72% of the campaign."** True as compute, wrong as priority: ~60,000 calls
   per battle against ~7 per scene. Call count measures resolution granularity, not significance.
4. **Two static attributions of phase→module, both unfit** — per-file gave every `mc_v18` phase the
   same seven units; per-function gave almost nothing. Deleted rather than tuned to look plausible.
5. **A substring scan for `stat_deltas` counted a docstring mention as an emission.**
6. **A docstring scan counted every path MENTIONED in prose as a path USED by code** — 8 of the fork
   scan's first 11 "escapes".
7. **`engine/params/` in a LEAVE list collapsed to first-segment `engine`,** blacklisting the entire
   carried engine tree.
8. **A `.endswith('.py')` check reported 3 directory pointers as "no pointer",** nearly becoming a
   17-item work list that did not exist.
9. **A `LEAVE` list that never subtracted.** `engine/params` shipped in the fork anyway.
10. **A phase note written from a docstring, not the body.** `run_accounting` has six steps and
    never calls `settlement_layer`; the note said three and attributed it.

**The procedure that catches all ten:** before asserting something is absent, search for something
you *know* is present by the same method and confirm the method finds it.

---

## G. Contract ↔ manifest ↔ runtime — three registries that disagree about the same 27 modules

Measured 2026-08-03 by joining `references/module_contracts.yaml` (declares keys + a `sim_module`
code pointer), `references/wiring_manifest.yaml` (declares the build state), and
`references/execution_trace.json` (what a seeded campaign actually ran).

| # | Oddity | Measured |
|---|---|---|
| G1 | **The build state is not in the contracts file.** All 27 contracts have **zero** `build` field; the state lives only in `wiring_manifest.yaml`, joined by module name. Two files, one join key, no schema tying them — and a name-join is exactly what silently produced 9 `?` rows earlier this session | `sorted(mods[0].keys())` → no `build`; `wiring_manifest.yaml` has all 27 |
| G2 | **Four modules marked `deferred` are observed EXECUTING.** `faction_state` 498 calls, `territorial_piety` 229, `peninsular_strain` 30, `scene_slate` 12 — in one seeded campaign. Presence is hard evidence, so the manifest is wrong about these four, not the trace. `faction_state`'s pointer is `engine/autoload/game_state.py` — the boot spine itself | `by_contract` channel of `execution_trace.json` joined to manifest `build` |
| G3 | **Six modules whose build state says "no code" have a code file that exists.** The four above plus `piety_track` (`systems/characters/sim/conviction.py`, 0 observed) and `settlement_layer` (`systems/settlements/sim/settlement.py`, `design`, 0 observed — consistent with F10, `run_accounting` never calls it) | `os.path.exists(sim_module)` per contract |
| G4 | **Only 2 of 27 modules are `live`** — `mass_battle` and `victory`. Everything else: 10 `deferred`, 9 `design`, 3 `stub`, 2 `unwired`, 1 `gated` | `collections.Counter` over manifest `build` |
| G5 | **`victory` is `live`, executes 384 calls, and declares in=0 out=0 keys.** The module that decides the game ends participates in the key graph not at all. `territorial_piety` is the same shape (in=0, out=0) while executing 229 calls | contracts `consumes`/`emits` lengths |
| G6 | **`npc_behavior` is the largest contract in the corpus — 31 in, 11 out — and has no code and no doc.** `faction_state` consumes 25. The two heaviest declared interfaces are the two least implemented | contracts, sorted by `len(consumes)` |
| G7 | **The `by_contract` trace channel can only attribute 5 of 27 modules**, because most contracts have no file pointer. **Every zero in G2/G3 is therefore "not attributable at this seed", never "dead"** — the tool says so itself, and this is the false-absence trap that already burned this session ten times | `units observed: 5` |
| G8 | **`review_core.py --summary` prints tool paths that do not exist.** Line 130 builds the label as `"tools/" + argv[0].split("/")[-1]` — it hardcodes `tools/` and discards the real directory. `stubs.count` really lives at `skills/valoria-vector-audit/scripts/structure_audit.py`; the summary calls it `tools/structure_audit.py`, which is a 404. It sent me on a false hunt while writing this file. **One-line fix; deliberately not taken here** (see K) | `tools/review_core.py:130` vs `:72` |

## H. The mass-battle adapter, stated exactly (supersedes E2's summary)

E2 said "canon returns `{winner, turns, phases}`". **That was read off the wrong function.**
`resolve_battle` is a *router* (`tests/sim/mass_battle/engine.py:512`) and `{winner, turns, phases}`
is the `kind='single'` path. The default is `kind='multi'`, which returns something else entirely.
Corrected below — this is the actual C2 blocker and it is smaller than it looked.

| what | shape |
|---|---|
| **Caller needs** (`systems/factions/sim/faction_action.py:431-437`) | `attacker_wins`, `degree`, `attacker_size_pct`, `defender_size_pct` |
| **Live engine returns** (`systems/mass_battle/sim/massbattle.py:1847`) | exactly those four |
| **Canon, `kind='multi'`** (`orchestration.py:2408`) | `winner`, `battle_turns`, `log`, `a_loss_final`, `b_loss_final` |
| **Canon, `kind='single'`** (`orchestration.py:2172`) | `winner`, `turns`, `phases`, `tick_in_phase`, `a_stamina`, `b_stamina`, `a_hp_pct`, `b_hp_pct`, `a_morale`, `b_morale`, … |

Three of the four map mechanically: `attacker_wins ← (winner == 'A')`, and the two `*_size_pct`
plausibly `← 1 - *_loss_final`. **`degree` is the whole blocker, and it has no canon source at all** —
the live engine *synthesises* it from a hardcoded ladder (`'Success'` if `attacker_wins`; `'Partial'`
if `not unit_a.routed and a_size_pct >= 0.50`; else `'Failure'`). Canon's `multi` return does not
expose `routed`, and the `0.50` has no citation in that block. So porting the caller onto canon means
**authoring the degree rule**, not translating it. That is a design ruling, not an adapter.

## P. Shapes that block a Godot port regardless of which engine wins

| # | Oddity | Measured |
|---|---|---|
| P1 | **21 of 75 declared stat identifiers are English prose, not keys** — `'faction stats 1-7'`, `'card hands / cooldown'`, `'MS / IP / CI / Turmoil / Accord / Mandate / PV / PT reads'`, `'CV (per-territory Piety)'`, `'faction Mandate (cross-module → faction_state)'`. All 21 are in `module_contracts.yaml`. This is CLAUDE.md §5's "numbers live as prose" problem one level up: the **state field names** are prose too, so there is nothing to bind a Godot resource field to | `python tools/ci_quantity_vocabulary_check.py` — signal `vocab.a17`, 21/29, report-only |
| P2 | **`consumes: '*'` is unimplementable as a subscription** (B7). A `KeyBus` needs a type list | `module_contracts.yaml`, 2 modules |
| P3 | **`engine/params/*.md` — 43 prose tables, zero code readers** (C3). If the fork drops them, whatever canon they hold that the code does not is lost at the fork point | grep for readers in `engine/`, `systems/` |
| P4 | **Descriptor roster still IN FLUX**, aggregates unwired, Combat Pool defined three ways. Unchanged this session; restated because it gates the same binding step as P1 | CLAUDE.md §5; SessionStart banner |

---

## J. Open questions — what I could not answer, and what would answer it

These are **questions, not findings**. Each says what would settle it. Ordered by how much else
depends on the answer.

| # | Question | What would answer it | Blocked on |
|---|---|---|---|
| **J1** | **Does `main` keep moving after the fork?** | A ruling. If yes, `build_fork.py`'s one-way `rmtree` assembly (E1) is the wrong mechanism and a shared-history GitHub fork is close to forced; if no, the assembler is correct and simpler | **Jordan.** Everything in E depends on this |
| **J2** | **Which mass-battle engine does the fork wire to the campaign?** | The degree ruling in H. Until `degree` has a canon definition, the canon engine cannot be called by the existing caller without inventing the rule | **Jordan** (design ruling), not measurement |
| J3 | **Is `degree`'s `0.50` threshold canon or an artifact?** | Grep the `PP-NNN`/`ED-NNN` that established it. I did not do this — I read the code, not the ledger | Measurement. ~20 min |
| J4 | **Should `tests/sim/mass_battle/` be moved out of `tests/`?** | It is the canon engine misfiled under a test directory, which is *why* A3 fires on every edit to it. Moving it is a large rename touching goldens and CI paths | Ruling + a careful rename. This is the single highest-leverage cleanup for the MB lane |
| J5 | **Is the manifest wrong about the four executing `deferred` modules (G2), or is the trace attributing them too generously?** | Read the four call sites. Presence is hard evidence *that the file ran*; it is weaker evidence that the *contract's module* ran, since a file can host more than one concern | Measurement. ~1 h |
| J6 | **What is `meta.legacy_event` for?** | Declared, no producer, no consumer (B6). Either a planned hook or a leftover. `git log -S` on the type name would date it | Measurement. ~10 min |
| J7 | **Why does `test_conditional_withdraw_fires_when_enemy_closes` pass locally and fail in CI** (A6)? | CI shows `stance=='retreat'` with `yielding is False` — the order fired but applied half its behaviour. Suspects, untested: xdist worker interaction, an env flag set only in CI, or genuine order-dependence. Run the file under `-p xdist -n 4` locally first | Measurement. MB lane |
| J8 | **Do the 9 red MB tests represent one defect or several?** | They were treated as one background all session because they move together. Nobody has checked whether a single fix greens all 9. If they share a cause, the lane's backlog is one item, not nine | Measurement. MB lane, ~half a day |
| J9 | **Is D1 (one-turn routs, untouched winner) upstream of J8?** | Jordan ruled D1 a real defect. If the rout fires too early, several of the 9 — `conditional_orders`, `dg2_yield_residuals`, `stochastic_rout` — would fail exactly this way, because their assertions all need the battle to *last long enough* for a trigger to fire | Measurement, and it is the most promising thread in the lane |
| J10 | **What is `victory` supposed to consume?** (G5) It is `live`, it runs, and it declares nothing | Read `engine/autoload/victory.py` and write the contract. This is authoring, not discovery | Nobody — just undone |
| J11 | **Does the 43-table `engine/params/` corpus hold any value the code does not?** (P3/C3) | Sample ~5 tables, resolve each number against the code. If all agree, the corpus is safely droppable; one disagreement means it must be reconciled before the fork | Measurement. ~2 h, and it de-risks the fork's biggest deletion |
| J12 | **Do the fork's counts survive a re-run?** (E5) | `python tools/build_fork.py --out <path>` and diff `FORK_MANIFEST.json` against the numbers in E3/E4/B4 | Measurement. ~5 min, and it is the cheapest item on this list |
| J13 | **This branch trips the scope ratchet — raise the ceiling or retire the growth?** `tracked.files` +32 over ceiling, `audit.files` +1, `proposals.open` +1. The growth is real and deliberate (the fork assembler, the execution-map and trace tools, this record), not accidental. The ratchet is **report-only** — local gates pass — so nothing is blocked, but its own instruction is "retire the growth, or raise the ceiling with an explicit ED and a loud call-out (ED-1094)". **This row is that call-out.** I did not raise the ceiling myself: doing so silently is exactly what the ratchet exists to prevent | A ruling at merge time. `python tools/valoria_local.py --staged` reprints it | **Jordan**, at merge |

---

## K. Deliberately not done, and why

- **G8's one-line fix to `review_core.py:130`.** Correct and trivial. Not taken because this session
  was closing and an unrelated tool edit inside a docs commit is how scope leaks. Take it first next
  session; it costs nothing and stops the next reader chasing a 404.
- **B3's `social_contest` pointer widening.** Would re-attribute 276 calls on one session's judgement
  about a canonical registry. Wants a ruling, not a patch.
- **Anything in the MB lane.** Out of this session's lane (IN), and A3 means even a comment-only edit
  under `tests/sim/` demands a `coverage_matrix.md` co-change.
- **Re-pinning any threshold to green a test.** The retrospective's Phase 0 forbids it, and D1 being a
  confirmed defect makes it actively wrong here.

## L. Re-running everything in this file

```bash
# G — the three-way registry join (contracts × manifest × trace)
python3 -c "import yaml,json; ..."      # see G rows for the exact fields; all three files are in references/
# H — the four return shapes
sed -n '1840,1855p' systems/mass_battle/sim/massbattle.py
sed -n '2404,2416p' tests/sim/mass_battle/orchestration.py    # kind='multi'
sed -n '2170,2180p' tests/sim/mass_battle/orchestration.py    # kind='single'
# I1 — the prose stat identifiers
python tools/ci_quantity_vocabulary_check.py
# A2/A6 — the paired control that proves the CI red is the background
git worktree add /tmp/mainctl origin/main && cd /tmp/mainctl && python -m pytest -q -p no:randomly <the 9 selectors>
# J12 — the cheapest open item
python tools/build_fork.py --out /tmp/fork && cat /tmp/fork/FORK_MANIFEST.json
```
