# Open oddities — everything measured this session and left unresolved (2026-08-03, ED-IN-0123)

## Status: RECORD. Not a work plan, not a proposal. Every entry below was **measured**, and the
## measurement is stated so the next reader can re-run it rather than trust it. Nothing here is
## inferred from a docstring; where a docstring was the source, that is called out as the defect.

Written at session close so these stop living in one session's context. Grouped by what a reader
would be doing when they hit each one.

---

## A. Gates that misreport

| # | Oddity | Measured |
|---|---|---|
| A1 | **`All Gates Green` counts *cancelled* jobs as failures.** So it goes red on any push that supersedes a running build, with no defect behind it. Nine wakes this session resolved to this or to A2. | `needs.json` shows `unit-tests: cancelled` → `FAILED (not success)` |
| A2 | **`main` is CI-red (9 tests), so every PR's aggregate is red.** A real regression and the background are indistinguishable. | Ran the 8 locally on `main`'s head `80918f6d` with no branch changes: same 8 fail; the 9th (`byte_exact_cell_mode`) skips locally, runs in CI (ED-MB-0061) |
| A3 | **`ci_co_file_checker` rule 3 fires on the canon mass-battle engine's own source.** Any edit under `tests/sim/` — including a comment-only one — demands a `coverage_matrix.md` update. It fires because the CANON engine is misfiled under `tests/`. | A comment-only edit to `config.py` tripped it; digest verified byte-identical (`ccdf7d09…`) before and after |
| A4 | **`freshness_gate` has ~12 stale `canonical_sha__` pins** and is report-only until refreshed. | CLAUDE.md §8; `python3 tools/freshness_gate.py --update` |
| A5 | **`test_gauge_invariants` XPASS count varies run to run.** Not flaky code — a statistical test whose own docstring says an XPASS at n=24 is a prompt to re-measure at n=60, not evidence of a fix. | 1 vs 2 xpassed across identical local runs |

## B. Registry / contract data

| # | Oddity | Measured |
|---|---|---|
| B1 | **`mass_battle`'s contract has `sim_module: None`** — the only `build: live` module with no code pointer at all. Distinct from the 13 units that use the string `"none"`. | `references/module_contracts.yaml`; the pointer you'd write depends on the unresolved canon-vs-live tree |
| B2 | **Only 10 of 27 contracts declare a file `sim_module`;** 3 more declare a directory. 14 declare nothing (all `design`/`deferred` — correct, they have no code). | `tools/build_execution_map.py` reality_check |
| B3 | **`social_contest`'s pointer is narrower than its own code.** `systems/social_contest/sim/contest/` excludes `parliamentary_vote.py`, a *sibling* of `contest/`, which accounts for **276 calls** that therefore attribute by path guess. CLAUDE.md §3 slice 7 says that file does belong to social_contest. | Reported, deliberately **not** edited: a canonical-registry change on a session's judgement for 276 calls of attribution |
| B4 | **36 unwired fork files have no contract pointer at all** — they cannot be joined to a build state. | `FORK_MANIFEST.json` |
| B5 | **One contested scalar:** `CI (Church Influence)` is claimed as owned state by BOTH `ci_political` and `territorial_piety`. | 37 owned scalars across 35 units, 1 contested — `references/execution_map.json` §4 |
| B6 | **2 key types have no producer; 8 have no consumer.** A type with no producer cannot fire; one with no consumer means nothing reacts. | 46 of 56 types have both — `execution_map.json` |
| B7 | **`references/key_graph.json` contains a key type literally named `*`.** Noticed while reading the schema; never investigated. Possibly a wildcard row, possibly a parse artifact. | `keys["*"]` with `consumers: [articulation_layer, fieldwork_knots]`, `producers: []` |

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
| E2 | **The fork carries BOTH mass-battle trees**, deliberately. Canon at `systems/mass_battle/canon/`. Blocked on `degree`: canon returns `{winner, turns, phases}`, the caller needs `{attacker_wins, degree, *_size_pct}`, and `degree` has no canon mapping | Picking one silently would design that ruling by implication |
| E3 | **225 `.md` against 206 `.py`** even after `LEAVE` was enforced. The remainder is subsystem design documentation, carried on purpose — but the fork is **process-prose-free, not prose-free**, and that distinction should not be blurred | `find` over the assembled tree |
| E4 | **Only 58 of 206 carried files are reachable from `engine.mc_v18`.** The other 148 are tests, oracles, canon-awaiting-wiring and unwired subsystems — the backlog, not detritus | `FORK_MANIFEST.json` |

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
