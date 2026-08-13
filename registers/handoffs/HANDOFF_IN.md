# Handoff — IN (Infrastructure / Cross-Cutting)

## THE SEPARATION WORK LIST (W1–W10) — written down 2026-08-04 (ED-IN-0135)

**Why this is here.** The W-list existed only in a review transcript and a chat reply. The ED-IN-0132
gate asks each milestone's reviewer to check *fidelity to plan*, and a reviewer correctly reported it
could not: the plan was not in the tree. A gate that cannot be checked is ceremony. So:

| # | Work | Precondition | Falsifier | Tier | State |
|---|---|---|---|---|---|
| W1 | Carry the 9 MB failures as `xfail(strict)`, citing ED-MB-0061 | none | `pytest tests/valoria` → 0 failed / 9 xfailed | sonnet | **DONE** ED-IN-0140 |
| W2 | Truth-surface sweep (keep-set cutoff, plan residuals, `keys.py` 44→55) + doc↔tool pin | none | `test_keep_set_doc_cutoff_matches_the_tool`, mutation-verified | haiku/sonnet | **DONE** ED-IN-0134 |
| W3 | **Deletion rehearsal** in a scratch worktree | ~~W1~~ | *is* the falsifier of every static prediction made so far | sonnet + opus verdict | **DONE** ED-IN-0144 |
| W4 | `key_type_registry.md` → JSON; repoint readers; regenerate `.tres` | **R1 done** (ED-IN-0135) | round-trip byte-exact; mutate-one exits 1; `.tres` byte-compared; `test_key_substrate` exact-roster | sonnet + opus on schema | ready |
| W5 | Weapons → typed JSON; regenerate GDScript | Jordan confirm | 53 exported; generated `.gd` has no `reach/weight/spd/handling` | sonnet | ruling |
| W6 | ~~`engine/params` census + demotion~~ → **capture + EVACUATION** | none | 43/43 files byte-identical in the YAML capture; `--check` blocking in all four wiring points; positive control on the losslessness guard | haiku + opus | **DONE** ED-IN-0139 |
| W7 | Deletion slices, one root per commit | W1, W3, W9, Jordan sign-off | 4 gates green per slice | sonnet + critic gate | ruling |
| W8 | `handoff_atomize` first run | **2** Jordan calls | `--check` exit 0 + `test_handoff_structure` | sonnet | ruling |
| W9 | Replace frozen `AUDIT_CUTOFF` with citation-based retention | Jordan ruling | `--check` total; new count pins | sonnet | ruling |
| W10 | Ratchet re-record | W7 | `scope_ratchet --check` exit 0 | sonnet | open |

**Independent, parallelisable now:** W1, W2, W4, W6. **Chains:** W1→W3→W7→W10; W9→W7's audit slice.

**Filed residuals from the W2 gate review** (none block W4 after R1):
- **R4 — `references/restructure_ledger.md` must invert BEFORE the first evacuation slice.** It is an
  alias registry parsed at runtime by **two** tools — `broken_dependency_checker:106` and
  `ci_claude_workflow_paths:38`. (I relayed "four" from the review without checking:
  `build_incompleteness:363` merely *excludes* the filename from a scan, and the `evacuation_plan`
  hits were my own comment and print string. Corrected here; the R4 conclusion is unchanged, its
  blast radius is half what I stated.) Keep-set §8 item 2 requires **every deletion commit to write a
  new alias row into it**. A hand-edited `.md` that blocking CI machine-reads, about to take one write
  per slice, is the highest-blast-radius format violation in the tree. Not a W4 dependency; a W7
  dependency.
- ~~**R5** — evacuate rule for `engine/params/history/` (8 files) + `threadwork_superseded.md`~~ —
  **RESOLVED by ED-IN-0139**, and by the broader rule rather than the special case R5 asked for: the
  whole of `engine/params/` evacuates, so superseded params prose is not surviving on a blanket keep
  rule because there is no longer a keep rule to survive on.
- The `:443` correction in the fork plan is spliced mid-sentence; tidy if that doc is touched again.

**W6 gate review (ED-IN-0132 pass, verdict COMPLETE-WITH-RESIDUALS).** Six actionable findings, all
taken, none disputed. The two that matter as *pattern*, not incident:
- **F1 — a claim's guard was weaker than the claim, and the two were weak in the SAME way.** The
  exporter read text-mode `errors='ignore'`; the falsifier verified with the identical read. Two lossy
  reads that agree with each other are not evidence about the file. This is §0.1 point 2 in a form I
  had not seen before: not a missing assertion, a *matched pair* of assertions blind to the same thing.
  **Generalise it:** whenever a test verifies X by re-deriving X the same way the code derived it, the
  test measures agreement, not truth. **SWEPT (§0.1 point 5), and the other two exporters are clean —
  for a reason worth stating rather than a lucky one.** Neither `export_key_types.py` nor
  `export_engine_params.py` uses `errors=`, and more importantly neither *claims* fidelity to a file's
  bytes: their claim is "the committed artifact agrees with what the single loader/config produces",
  and agreement is exactly what they assert. The defect needed a claim about the SOURCE (byte-identical
  to 43 `.md`) checked by a derivation that shared the source-reading path. So the rule to carry is
  narrower and sharper than "exporters are suspect": **when a claim is about bytes on disk, the check
  must read those bytes independently of the producer.**
- **F3 — a positive control covering only one branch, described as covering both.** The control planted
  an omission; the ledger said it planted "a mismatch". A control that does not exercise the branch
  carrying the claim is decoration, and describing it as stronger than it is makes the decoration
  load-bearing. Four content mutations added.

**Provenance census (2026-08-04, scratch measurement — carry into W7).** Jordan asked whether we
needed to flatten contested files to find `.md`-vs-code value conflicts. **We did not, and there is
no conflict problem**: a (identifier, number) census over kept prose produced a "conflict" bucket
that sampling showed to be artifact (3 read, 2 provably false — `block_size`'s `0` came from the
prose sentence `Size = 0`; `base_pool`'s `1` is the pool FLOOR in `max(1, base_pool − penalties)`).
Co-occurrence on a line is not an assertion, and no amount of heuristic sharpening fixes that.

What the sampling found instead is the real relationship, and it is not competition: **the engine
holds the value and cites the doc as its ORIGIN** — `BLOCK_SIZE = 100  # [canonical:
systems/mass_battle/mass_battle_v30.md §A.3]`. Jordan's ruling ("design docs are just information
only at this point. real values live in engine") is already implemented as a code convention.

**The number W7 needs: 112 provenance citations in `engine/`+`systems/`+`tools/` `.py`; 58 (52%)
target an EVACUATING doc, 54 target a kept one, 0 unresolvable.** The 58 are `params/core.md` (23),
`params/mass_combat.md` (15), `modifier_system_spec.md` (10), `params/factions.md` (6),
`params/threadwork.md` (2), `audit_sim_mb_06_v14.md` (2). All become fork references, which Jordan
authorised ("provenance can cite to a fork") — so they do NOT block the slice, but the slice must
land the alias rows.

⚠ **METHOD WARNING, and the third instance on this branch.** The first run of that census reported
**0** citations targeting evacuating docs. It matched LITERAL paths, and `params/core.md` only
reaches `engine/params/core.md` through the restructure alias map — so the largest affected group
scored zero. Same defect class as the `audit/scripts/` phantom (ED-IN-0133) and the split-path
reader miss (ED-IN-0128). **Any scan over this corpus that does not resolve aliases is wrong by
default, not occasionally.** Resolve through `restructure_ledger` (or at minimum a basename
fallback) before reporting a path-based count.

**Filed by W6 (ED-IN-0139) — carry into W7:**
- **The params gate must die with its source.** `export_params_constants.py --check` re-derives from
  `engine/params/`, so the deletion commit must ALSO remove it from `.github/workflows/valoria-ci.yml`,
  `tools/valoria_local.py`, `references/ci_checks_registry.yaml` and
  `tests/valoria/test_gate_coverage.py::EXPECTED_COMMANDS`. Deliberately strict — there is no
  vacuous-pass-on-absent-source path — so forgetting is loud. Same commit, four files.
- **`ci_co_file_checker.py` rule 4** targets `engine/params/{basename}.md` (`:90-91`). It loses its
  target tree in the same slice; retire or re-aim it there.
- **The `engine/params` slice has 30 blocking readers and 2 split-path readers** as measured by
  `python3 tools/evacuation_plan.py --slice engine/params`. Most are mentions in comments and
  docstrings rather than loads — the scan is a substring scan over whole files — but the two
  split-path hits (`tools/ci_formula_prose_check.py` and its test) are real: that checker walks
  `engine/params/**/*.md` as its live corpus and needs a decision, not a re-point. Triage belongs to
  the slice, not to the capture.


## 2026-08-04 (late) — STATE AS OF `9c0a616`. Read this before resuming.

**Why this section exists: the record had stopped nine commits short of the tree.** A process
review (Fable-5, read-only) found this file had zero mentions of `pathres`, the identifier census,
the known-red register or ED-IN-0140/0141/0142, and still marked W1 open after ED-IN-0140 executed
it. Six commits carried no ledger entry at all, so their findings lived only in commit messages —
which no tool reads. **This is the exact defect this session spent the day prosecuting in others**
(the "none for infrastructure" ruling that reached no file). Reconciled here.

**Tracked file count: 3,144 at branch point → 3,018 now.** 164 files deleted (the audit
working-paper join). The W7 deletion slices have NOT run.

### What landed since the last handoff update
- **ED-IN-0140 — W1 DONE.** 9 known-red MB tests carried as `xfail(strict=True)` from one register
  (`tests/valoria/conftest.py`), falsifier in `test_known_red_register.py` (count pinned at 9, stale
  ids fail, every entry must cite ED-MB-0061). **W3 is therefore unblocked** and is the next step.
- **ED-IN-0141 — the audit ruling's second clause + the join.** `R-AUDIT-INFRA` evacuates
  infrastructure-lane audit units (dominant cited `ED-<LANE>` tag); `AUDIT_KEEP_OVERRIDE` holds
  `emergent-narrative-engine` by Jordan's explicit ruling. `tools/join_audit_workings.py` verifies a
  byte-exact round-trip before purging. Kept audit `.md` 493 → 119.
- **ED-IN-0142 — two gate defects.** A generated-sidecar exemption in `validate_ed_citations`
  (the census QUOTES citations; it does not make them), and `build_test_register.py --check`, which
  exited 0 unconditionally and so never gated — it drifted 3× in one session, CI catching it each
  time. Now diffs, wired in **five** places (the workflow, `valoria_local.py`,
  `ci_checks_registry.yaml`, `test_gate_coverage.EXPECTED_COMMANDS`, and its own falsifier —
  I had been calling it four-way in three commit messages).
- **`tools/pathres.py`** — the single owner for path-reference extraction / alias resolution /
  file-I/O tracing, extracted from `ci_claude_workflow_paths` + `evacuation_plan`. Net removal:
  the alias ledger had **four** independent parsers. `Resolution` is an object, not a string, and
  raises on `bool()` so a caller must say which question they are asking. CLI: `resolve | scan |
  pipeline`. 25 canaries in `test_pathres.py`, each binding one branch to one named defect.
  ⚠ `pipeline` is a **LOWER BOUND** — dynamic paths are invisible and guessing is forbidden.
  **Migration steps 2–8 of the guardrail plan are NOT done**: four parsers still live, and
  `broken_dependency_checker` must migrate at `max_hops=1` or the refactor silently loosens a
  blocking gate.
- **`tools/build_identifier_census.py`** — per-subsystem `_identifier_census.yaml` + a roll-up.
  ⚠⚠ **NOT SAFE TO CULL DOCUMENTS FROM.** Two antagonist rounds found: `engine_clock` marked BUILT
  off a local variable in a tool whose docstring says it is unauthored; a filter of mine erasing
  each doc's own headline mechanic with no audit trail; a dead alias pass advertising an
  enforcement that never ran. Fixed, but the real-mechanic fraction of UNRESOLVED still runs 0%
  (threadwork, victory) to ~75% (settlements), and parameter rows inflate the count 2–3× over
  distinct design decisions. Read `dropped_as_not_a_mechanic` before concluding anything is absent.
- **RULED (Jordan, 2026-08-04): `prose-writer` stays** — `R-SKILL-PROSE` in `evacuation_plan.py`.
  Canon narrative stays on main and this is the skill that authors it.

### Correction to R4 above, which the LEDGER still gets wrong
ED-IN-0135's entry says `restructure_ledger.md` is "parsed at runtime by **FOUR** tools". It is
**two** (`broken_dependency_checker:106`, `ci_claude_workflow_paths:38`); I relayed a reviewer's
count into the ledger without checking it. Corrected in this file when found, but the ledger row is
append-only and still carries FOUR — treat this section as the correction of record.

### Open rulings for Jordan
1. **Contest gate packets** (7 audit units citing no ED). Kept because the lane classifier abstains;
   but they are records of *how a decision was made*, which "none for infrastructure" would evacuate.
2. **Nested `.json` working tiers** in kept audit units — the join was markdown-only, so
   `ners-qualitative-audit/01_workings/` still holds ~30 JSON dossiers beside its joined file.

### The trajectory signal, stated so it can be checked against me
The tree re-grew 2,999 → 3,018 after the one deletion commit. **Within three commits of this
section, one must either run W3 or land a W7 slice that takes `git ls-files` below 3,018 with the
four gates green.** Three more commits of instruments with a non-decreasing tracked count confirms
this has become a tooling programme rather than a separation.

## W3 DELETION REHEARSAL — EXECUTED 2026-08-04 (ED-IN-0144). Read before any W7 slice.

Ran the partition for real in a throwaway worktree: **1,724 files deleted, 3,003 → 1,279 tracked.**
Then ran every blocking validator and the shipping gate against the result. This is the falsifier
for every static prediction the planner had made, and **it broke four gates, only one predicted.**

| gate | result | fix |
|---|---|---|
| `pytest tests/valoria` | **DOES NOT COLLECT** | see below — the headline finding |
| `export_params_constants --check` | red | PREDICTED; retire it in the params slice commit |
| `ci_claude_workflow_paths` | 34 DEAD | `.claude/wf_*.js` name evacuated audit units + params docs |
| `broken_dependency_checker` | 28 broken, 26 under `designs/` | live ledger entries whose EVIDENCE evacuates |
| `freshness_gate` | 21 | `canonical_sources` pins into evacuated docs |

### THE HEADLINE FINDING: a third reader blind spot, and the worst kind
`tests/sim/gauge_mb.py` is classified EVACUATE. Two KEPT shipping-gate tests do **`import
gauge_mb`** — a bare module name. Neither scan could see it: `readers()` greps for the path string
(never appears), `joined_path_readers()` looks for constructed paths (there is no join). The
dependency exists only as a name resolved through `sys.path` at runtime.

**Deleting it does not fail a test. It stops `pytest tests/valoria` COLLECTING AT ALL** — the whole
shipping gate becomes unrunnable, which is strictly worse than a red test and was invisible to
every static prediction. Only executing the deletion found it.

`module_import_readers()` added, wired BLOCKING into `--check`, and made **transitive** — one hop
was demonstrably the wrong answer: keeping `github_ops.py` immediately made its two imports
load-bearing, and reporting one hop per run turns a dependency closure into whack-a-mole where a
partially-kept import chain is exactly as uncollectable as none. A false positive was killed before
reporting (`import engine` resolves to the top-level PACKAGE, not `tests/sim_framework/engine.py`).

### OPEN, and the reason `--check` is currently RED
`tools/compliance_check.py:76` — a **BLOCKING CI gate** — does `import github_ops`, and that chains
`github_ops -> index_bootstrap -> regenerate_file_index` plus `valoria_hooks`: **four files under
`deprecated/` that live CI transitively depends on.** CLAUDE.md §8 records that tools importing
`github_ops` were retired for exactly this reason; `compliance_check` itself was never cleaned up.
Two ways out and they are not equivalent — removing the dead orchestrator import kills the whole
chain, keeping four `deprecated/` files as a permanent exception does not. **Do not paper over this
with keep-rules.** It is the cleanest available test of whether `deprecated/` can actually leave.

Three modules were given keep rules (`R-IMPORTED-MODULE`) because their readers are legitimate:
`tests/sim/gauge_mb.py`, and `descriptor_registry.py` / `github_ops.py` under `deprecated/`.

## 2026-08-03 — Fork Plan of Record rewritten to execute after two read-only Fable-5 passes (ED-IN-0124)

**This section is now the fork plan's execution log.** The proposal had become a *third* current-state
surface, disagreeing with `wiring_manifest.yaml` and this file about `Faction.L` on the same day. The
rewrite moves the rolling diary here and leaves the proposal holding decisions, pointers and holds.
If you are resuming fork work, read `proposals/valoria_fork_plan_of_record_v1.md` §7 for the sequence
and this section for state.

**Method.** Two structurally independent Fable-5 agents, `Read/Grep/Glob` only — no Write, no Edit, no
Bash — per §10's "make independence structural, not declared". One critic (steelman → logic → process →
34-row fidelity table), one architectural reasoner. Nine corrections landed, each re-verified against
the tree by the orchestrator before being applied.

**The nine.** (1) The `3 of 27` headline was contradicted by the same session's own
`audit/2026-08-03-session-oddities.md` G2 — four `deferred` modules observed *executing* — which the
draft cited two sections later for a different fact; thesis rebuilt on four label-independent trace
facts, with G7's bound stated (`by_contract` attributes only 5 of 27, so a zero is never "dead").
(2) `sim_params` publishes `cited 84 / uncited 240`, not the claimed zero provenance — the plan
contradicted itself between its W4 and E5 rows. (3) `WEAPONS` is at `weapons.py:74`. (4) Key-graph
arithmetic 46→**47** / 10→**9** (`meta.legacy_event` double-counted). (5) `Faction.L` "already
reconstructs" retracted to match the manifest and HEAD `6f5ada6`. (6) The ED-MB-0043 canon ruling is
**unregistered** — filed as a governance repair, not silently fixed. (7) `no_code_declared` measures
contract-pointer absence, not code absence; its members include two whole engines. (8) **`tools/build_fork.py`
already exists** and the plan wrote prose around it; running it is now step 1. (9) `autoload is a leaf`
is false — `game_state.py` imports downward into `systems.*` at function-local sites.

**What changed structurally, beyond the corrections.** Falsifier census: the draft had 2 genuine
falsifiers across ~13 exit conditions and **both were in already-executed waves** — the unexecuted
future carried the unfalsifiable ones. All eight rows in the new §7 name a test that can fail. Stage 0's
exit condition is now two-part (classification **and** the module's `parity` target passing), because
the old one was satisfiable by editing the YAML. The value-inversion guard is two-layer
(import-time immutability + an AST tripwire on new bare constants) since the morale template's shape
does not transfer. The held list shrank from seven-plus to eight real decisions by converting three
reversible engineering calls out of it. ED-1006's scope narrowed to downward *Key* delivery only, with
`keys.py:16-32` as evidence that the propagation spec's termination guards were ratified 2026-07-07.

**Next actions.**
- **Step 1 is `python3 tools/build_fork.py --out <dir> --verify-only`.** Do not re-derive the fork's
  carry/leave in prose again — read the tool. Treat its carry list as possibly stale w.r.t. ED-MB-0043
  (§11 item 4) and read it against §6.3 before trusting it.
- **Governance repair, blocking the ED-MB-0043 claim:** either file the MB-ledger entry naming the PR
  and flip `CURRENT.md`, or the "canon tree ruled" claim reverts to *held*. Right now the ruling exists
  only inside a PROPOSED proposal, and a session following `CURRENT.md ≻ proposal` will correctly
  conclude the fork is still open.
- **Before any `Faction.adjust` sweep:** route ONE site and diff the seeded winner + key composition.
  Emission means deferred `apply` at the accounting boundary (OF-7) while the current writes are
  immediate and mid-phase — that is a behaviour change, not plumbing, until measured otherwise.
- **The eight C-items in §9 each need their own ED with `needs_jordan: true`** so they reach the
  SessionStart Jordan docket. A held item that is not on a register is not held; it is forgotten.

## 2026-08-02 — The repointed-path pattern, guarded (ED-IN-0122, PR #284) + a planning failure worth recording

**Landed.** A seventh gate reporting clean over nothing: `ci_formula_prose_check.DEFAULT_CENSUS`
still named `designs/`, retired 2026-07-19, so it printed "_No formula prose-drift found in scope._"
for 14 days. Repointed → **88 census rows, 49 formula-bearing, 14 CENSUS_DRIFT**. `load_census()`
now returns `(rows, problem)`: its three failure modes were indistinguishable downstream from a
genuinely empty census, and the report rendered all four identically. Also repointed
`dashboard_data.HANDOFFS_DIR` → `registers/handoffs/` (blind 17 days; measured against the blind
value as a control: files **1 → 11**, `build_needs_decision()` items **2 → 7** — five decision
markers across FA/IN/PC/SC absent from the published dashboard), plus two dead paths stamped into
generated artifacts.

**The deliverable is the guard, not the repoints.** `canon_coverage_check` had been repointed for
the identical defect on 2026-08-01 with no guard written; two repoints and no guard is the pattern
going unlearned (§0.1 point 5). `tests/valoria/test_tool_input_paths_resolve.py` AST-scans every
module-level path constant in `tools/` (69 cases, 1 documented output exemption). AST not grep is
load-bearing: comments/docstrings are not in the parsed statement tree, so the many legitimate
`designs/` prose citations that CLAUDE.md §3 routes through the alias map are excluded **by
construction**. Mutation-verified **9/9**, and two mutants survived the first draft — a
`/`-separator filter excluded single-segment constants (i.e. missed the very
`canon_coverage_check` defect it is named after), and a value-based head-gate cannot see a
constant repointed to a typo. The guard then found the `dashboard_data` defect itself.

**INDEPENDENT REDISCOVERY — this was already filed.**
`audit/2026-07-29-centralization-single-owner/01_orchestration_plan_v1.md` §1 row 8 already
specifies exactly this: *"`ci_formula_prose_check.py` scans a **non-zero** census … with a guard
asserting `rows > 0`."* I found and fixed it without reading that row. Two independent
rediscoveries rank the finding as real; it also means the CSO program's §1 row 8 is now partly
satisfied and should be updated rather than re-executed.

**The planning failure, recorded because it is the reusable lesson.** I authored a consolidation
plan (v1), had it attacked, rewrote it (v2), had it attacked again — and **both versions'
worst defect was the same one level up: re-deriving an architecture and then a program that
already exist, better-attacked than mine.** Verified by execution after the second critique:

| I proposed | Reality |
|---|---|
| "wire `definitions_store --check` into CI, one line, not currently wired" | **Wired four ways incl. blocking.** `review_core.py:59` registry row `definitions.parity`, graded against `review_baseline.yaml`, run by `review_core --check` in `compliance-check`, which `ci-summary` requires. Live signal: `verdict pass, returncode 0, baseline 0, regressed false`. Would have built a **second owner of one rule** (§8) |
| "promote `LANE_PATH_PREFIXES` to `obs_core`" | `obs_core.py:35` **already re-exports it**; four generators consume it |
| "generate `lane_assignments.yaml` from the 9-lane table" | **Prohibited merge** — A/B/C write-lanes are a different concept (`lane_assignments.yaml:17-23`) |
| "extend the ED-IN-0122 guard to registry globs" | `test_retired_tree_apparatus.py:704` **already does it**; and a YAML glob has no AST, so the extension is structurally impossible in that host |
| "the JSON export's zero weapons is a *documented* scope guard" | **My own overcorrection**, taken from a prior critic at face value. The guard is against parsing *prose*; `weapons.py` is typed Python and would be *included*. The exclusion is just `derive()` hardcoding `config` + `core` |

**Standing conclusion for the next IN session: do not author another consolidation plan.**
`ED-IN-0103` (`audit/2026-07-29-centralization-single-owner/`, PROPOSED, three passes / six critics
/ 65 findings) already covers this ground, including `references/lane_ownership.yaml` as the single
lane owner (§1 row 6, file still absent) and the census guard above. Execute *that*.

**Settled by execution, for whoever picks up the weapons work:** `json.dumps(WEAPONS)` **succeeds**
post-bake, so extending `export_engine_params.py` to the weapons table is feasible (a critic flagged
it as possibly blocked by import-time mutation; it is not). Counts: **53 entries = 51 canonical + 2
`base=` half-sword variants** (`longsword_halfsword`, `estoc_halfsword`), matching CLAUDE.md §9's
51-weapon harness; **2 of them have a hand-made `.tres`**, so **49 canonical weapons have no
generated artifact**. This is PC/GO-owned — filed, not swept.

**Filed, not fixed (currency defect in a RATIFIED substrate doc):**
`systems/_architecture/repo_state_armature_v1.md:4` says "Phases 3 & 5 **HELD BACK**", but §5 line
112 says "**P3 — vocab fold (COMPLETE, ED-IN-0078** … Jordan-authorized 2026-07-20)", and
`tools/vocab_store.py` + 4 `# GENERATED by tools/vocab_store.py` register views exist on disk. The
Status line appears stale. Not an IN drive-by — it is a ratified-doc status flip.

**Also filed:** `ci_claim_provenance_check` reads `description` + `provenance` only, so the field
literally named `measured_by` is invisible to it (it failed my own ED-IN-0122 entry for this).
Widening the blob would re-scope every lane's entries and needs its own expected-delta measurement.

## 2026-08-01 — Four gates that could not see what they guard (ED-IN-0115..0119, PR #284)

**The pattern, four times over.** Each gate was correct when written and stopped working because
something else moved — the `sim/` (2026-07-21) and `designs/` (2026-07-19) retirements, and the
2026-08-01 job collapse. §0.1 point 5, and none of them announced itself.

| Gate | Claimed | Measured |
|---|---|---|
| `ci_sim_fabrication_check` (blocking) | guards the port's oracle (§7) | **0 of 117** oracle files matched |
| `validate_ed_citations` (blocking) | scans canonical surfaces | **45** of **293** files in its own mandate |
| `run.dispute()` in 5 of 8 `wf_*.js` | an adjudicable disagreement | every dispute keyed `'?'` |
| `scope_ratchet` registry row | `ci_job: validators-report` | nothing in CI invoked it |

**Measuring the fix before shipping it is what found the expensive halves.** Repairing
`is_sim_file` alone would have dragged **642** pre-existing uncited constants into a blocking gate
and walled off MB and PC; the same measurement showed the whole-file scan was never viable in its
original scope either (**2,283** in `tests/sim`). Deriving the citation walker from `SCAN_PREFIXES`
starved that function's *other* caller — ED universe **1167 → 1107**, 110 valid citations turned
`NONEXISTENT` — caught against a `git stash` control, not by reading the diff.

**Three defects were found by tripping them, not by looking for them:** the `--fix` offset bug
(surfaced by growing the harness owner), the `compiles_only` comment bug (my own comment took
`validators-report` from 10 parsed commands to 0 — `--ci` would have stopped running ten validators
and reported success), and my unallocated `ED-IN-0118`, caught by the citation gate I'd just fixed.

**Also closed: ED-IN-0045 item 1**, filed 2026-07-12. `tests/hooks/` held 12 files no CI job ran; 10
failed at collection (retired `valoria_hooks`/`github_ops`, `/home/claude` paths), zero could ever
have passed. Retired with greps recorded. **27 tests now run in CI that never ran**, including
`test_ed_citation_integrity.py` — 26 tests for `validate_ed_citations.py`'s pure core, which that
tool's own docstring points at. `references/scope_vocabulary.md` advertised a **drift guard that did
not exist**, and real drift had accumulated behind the claim (12 commit scopes in CLAUDE.md §2 vs 11
in the doc — `design`). Replacement written first, shown to fail on the live drift, then the doc fixed.

**The adversarial relay earned its cost (§10).** A read-only critic that never saw my reasoning
found **six** defects in my own repairs, all re-verified by execution before acting: a FALSE PASS on
quoted keys; a **silent narrowing** that dropped 14 audit-session sims while the docstring said
"removing coverage is not this fix's job"; a launderable count-keyed ratchet (now keyed by five
exact `(path, id)` pairs); a join that went silent on import failure and skipped compiles-only jobs;
a latent contract-widening channel; and — caught by CI, not review — the restored basename rule
flagging this fix's own guard file. **11 mutants planted, 11 killed; two survived their first round,
both §0.1 point 2 inside my own tests.**

### Third adversarial pass (ED-IN-0120) — four MORE false passes, in the fixes above

Requested explicitly after the branch was declared done twice. Self-attack plus a read-only critic
that never saw the reasoning. **Four of the six were false passes in gates this branch had just
repaired**, which is the part worth remembering: the first two passes each concluded the work was
sound, and each was wrong.

1. **Deleting a citation passed.** Added-line scoping let a changeset remove a
   `# [canonical: ...]` line and report OK over the now-uncited constant — the diff has no `+`
   lines, so everything became "carried". Under the whole-file scan it replaced, that commit was
   red. My claim "added-lines scoping is not a weakening" was FALSE for this class.
   `ci_common.get_removed_lines()` closes it.
2. **`run.critiqued` had the identical defect, eight lines from the one I fixed.** Called with a
   single array in all five wave scripts, so `produced` was `undefined` and the starvation signal
   could never fire. The dispute fix closed one *instance* of a pattern, not the pattern; arity is
   now derived from the owner for every `run.*` method.
3. **A row could claim any pytest-only job** (`unit-tests`), laundering exactly as `syntax-check`
   did before the compiles-only branch closed that one — one job over from the defect the join was
   built for.
4. **The quoted-key fix re-opened its own hole one typo wide** — `'layer-disputed':` matched
   neither branch and vanished. Also: spread passed unanalysed, and a unicode key *crashed* a
   blocking validator.
5. **The join shipped with no test at all.** A mutation sweep deleted the entire branch with
   everything green. The same sweep then caught two more untested branches of mine.
6. **Third recurrence of one bug:** a new scanner read prose about a call as a call. Fixed for
   `_dispute_calls`, then `compiles_only`, then reappeared. Comments are now blanked **once**,
   where `body` is derived.

**Corrected claim:** my declared narrowing said three files lost coverage; against `origin/main` it
is **two** — the third is a file this branch created. Re-measured across all 3,117 tracked files:
169 → 268, those two the complete lost set.

**15 mutants, 15 killed** — two survived the first sweep, both mine, both previously tested only ad
hoc. **The lesson is not that the work is now clean.** Three passes found defects in the same code;
the honest prior is that a fourth would find more, and the value came from attacking rather than
from re-reading.

### NEXT ACTIONS

- **Awaiting Jordan, not self-ratified:** `OPEN_AS_BASIS` over-fires on provenance prose. The 10
  deferred findings are mostly changelog parentheticals plus one `DRAFT FOR RULING` status line
  citing its own open ED by design. Narrowing a blocking gate's semantics to lower a number I
  produced is the §0.1 point-4 bias, so the heuristic is untouched and ratcheted instead.
- **Not burned down, now visible:** 2,925 pre-existing uncited constants (642 oracle + 2,283
  `tests/sim`). `ci_sim_fabrication_check --full` lists them.
- **PC-lane, recorded not taken:** `systems/combat/combat_engine_v1/` is a canonical oracle outside
  the fabrication gate, and `test_sim_fabrication_scope.py` is circular w.r.t. it (expectation
  derived from the same owner). Closing it needs a PC call plus a `ci_common` root-list edit.
- **MB-lane, surfaced not chased:** `test_obb_primitive::test_cellbox_from_helper_matches_constructor`
  is order-dependent (passes deterministic, fails randomized);
  `tests/sim/mass_battle/test_persubunit_stress.py` has 1 failing case;
  `tests/sim/territory_registry/test_registry_ledger.py` fails collection.
- **MB-lane — `test_per_cell_break_subsumes_the_body_level_one` is BIMODAL on CI. Two byte-exact
  states, and this note was revised twice before the data supported it.** Observed deltas, all
  byte-identical within their mode:

  | commit | delta | mode |
  |---|---|---|
  | `main` @ base | `14.711105983695994` | A |
  | `e585aa5` | `14.711105983695994` | A |
  | `873a5c0` (docs-only) | `28.536271554655265` | B |
  | `9482eb9` (docs-only) | `14.711105983695994` | A |
  | `d960f80` (docs-only) | `28.536271554655265` | B |

  **Two byte-exact values means two DETERMINISTIC paths**, selected by something that varies between
  CI runs and is constant locally — not noise, and not a stochastic spread. Docs-only commits sit
  either side of every transition, so no code change is involved.

  **Ruled out by measurement, not by argument** (each of these was a live hypothesis, and each is
  dead): *environment-dependence* — refuted the moment mode A returned on the next run; *hash-order*
  — `PYTHONHASHSEED` 0–7, no effect; *worker count* — `-n auto`, `-n 2`, `-n 4`; *suite context* —
  3 full-suite `-n auto` repeats; *test isolation* — alone and with module siblings. **11 local runs
  across every configuration tried produced mode A every time.** Mode B has never been reproduced
  outside GitHub's runners.

  **Two framings were published and withdrawn before this one:** "environment-dependent" (killed by
  the 4th data point) and "rare non-reproducible excursion" (killed by the 5th, which was
  byte-identical to the 3rd). Both were filed on too little data. The §0.1 point-4 lesson is the
  one that keeps applying: a number without a control is not a measurement in EITHER direction, and
  a cautious-sounding claim is not exempt.

  **Verdict is unaffected in both modes** — 14.7 and 28.5 both exceed the 10.0 threshold, and the
  test fails identically on `main`. Nothing here is caused by or blocks PR #284.

  **MECHANISM LOCATED — the instrument cannot tell the two apart (adversarial re-audit, 2026-08-01).**
  `_mean_loser_casualties` (`tests/valoria/test_stochastic_rout.py:92`) appends to `loser` ONLY when
  the battle has a decisive winner, then returns `statistics.mean(loser)`. A draw is silently
  skipped, so **the mean is taken over a variable-length list and nothing records its length**. That
  is CLAUDE.md §0.1 point 2 verbatim — "a loop that asserts conditionally must assert that it
  asserted" — in MB's own measurement instrument.

  **Proven:** the list is conditionally appended and unguarded; locally both arms average **16/16**
  samples (`PC_STOCHASTIC_ROUT=False` → 10 A-wins / 6 B-wins, `True` → 12/4), so an
  `assert len(loser) == n` would pass today and costs nothing to add.
  **NOT proven, and deliberately not claimed:** that mode B is caused by a lower sample count. That
  needs the reference environment, which I do not have. Two overclaims were already made and
  withdrawn on this anomaly; this one stops at what was measured.
  **Why it is still the right next step:** whatever drives mode B, this instrument cannot
  distinguish "the engine changed" from "fewer battles were decisive" — a 55.5 → 69.5 shift is
  exactly what dropping several low-casualty decisive samples would produce. Adding the count
  assertion discriminates between those two on the very next CI run, for one line, and turns an
  unfalsifiable anomaly into a measurement. Do that before arguing a golden re-base from either
  magnitude.

- **Known blind spot worth closing:** `valoria_local --ci` computes a different changeset than CI's
  `GITHUB_BASE_REF` mode, so **local-green is not CI-green** for changeset-scoped validators. That
  gap is what let the sixth defect reach CI. Reproduce CI locally with
  `GITHUB_BASE_REF=main GITHUB_EVENT_NAME=pull_request`.
- **Audit staleness needs NO action** (checked, not assumed): `audit-refresh` cron is weekly Mondays
  06:00 UTC, last successful run 2026-07-27, next due 2026-08-03. The banner warnings are normal
  inter-refresh drift; ED-IN-0099 already measured the feed near-stationary and proposes inverting
  the metric.
- **This file is 27k tokens, over the 20k `[WARN]`** — as are `HANDOFF_MB` and `HANDOFF_PC`. The
  archive convention the per-lane *ledgers* already use is the fix; still unapplied.

## 2026-07-31 — M1 program scaffolding RATIFIED (ED-IN-0112); residuals filed (ED-IN-0113)

**Landed and wired (PR #277).** Scope ratchet (`tools/scope_ratchet.py` + `registers/scope_baseline.yaml`,
CODEOWNERS-gated), season acceptance gate (`tools/m1_acceptance.py`), dashboard program panel
(`build_program`/`renderProgram`), `valoria_local.py --ci` (all 31 CI validators in one command, list
derived from the workflow via `ci_gate_coverage.jobs()`), and the shipping-gate parallelisation.

**Numbers, measured not projected.** `unit-tests` 387s -> 180.7s in CI (2.15x; 3.02x locally),
failure/pass/skip counts byte-identical both sides. Whole-run wall clock ~428s -> ~220s.

**The scaffolding is now EFFECTIVE, which it was not when first built.** An adversarial critic
(valoria-critic, read-only) found the ratchet had no executing caller except its own tests. It is a
report-only row in `valoria_local`'s table (pre-commit AND CI) and registered in
`ci_checks_registry.yaml`. **No new CI job was added** — the repo has 34 and that is the problem this
instrument measures.

**What the critic cost, and why it was worth dispatching.** 13 findings, 4 of 9 claims refuted, 8
fixed. Two were landmines: a zero-headroom ratchet asserted inside the BLOCKING pytest suite (the next
ED anyone filed would have broken the build for an unrelated author), and a split-ledger guard whose
glob never matched the largest ledger while four ids were split in it. G19 — dispatch the critic
*before* the claim leaves the session — is the lesson, and it landed on this session specifically.

**What stopped a worse mistake.** The planned `unit-tests` split by `-m "not sim"` is FORBIDDEN:
`pytest.ini`'s ONE RULE calls a `-m` filter there a shipping-gate coverage cut and
`test_pytest_marker_discipline.py` fails on it. Reading the rule before building is why this shipped
parallelisation instead of a coverage cut wearing a speedup's label.

**OPEN — ED-IN-0113, needs Jordan.** The decision-policy precedence fork (134-ruling precedent mine
attached: mechanical canon demonstrably subordinate to measured grounding; the metaphysical-canon tier
is UNESTABLISHED and deliberately not invented), plus five unfixed critic findings.

**Cross-lane note.** `main` remains CI-red on the documented F-series (ED-MB-0061 §3.1b, 10 on CI).
Nothing in this program touches it, and the golden re-base that clears it is gated on Jordan's
golden-mode-matrix ruling.

Lane-scoped continuity for the `IN` (infrastructure/cross-cutting) lane, per the
`ED-<LANE>-NNNN` namespace (`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention.
Root `HANDOFF.md` is the index; see it for the global "Next actions" pointer and cross-lane
items. `IN` is also the catch-all for genuinely cross-cutting repo-governance work (ID systems,
CI gates, canon-currency reconciliation) that doesn't belong to any one subsystem lane.

## Executive summary

- Lane state 2026-07-28: 44 live items.
- Hot: `.claude/` apparatus + run discipline just landed (ED-IN-0087/0088/0089); two of its
  assumptions are unverified and tagged [PART].
- Blocked on Jordan: handoff archive-vs-dormant call (ED-IN-0086).
- Known debt: 28 untagged bullets; same-lane ED collisions unaddressed by design.

## Pending

- **[OPEN] ED-IN-0149 — world-churn audit: the machinery is built and DISCONNECTED (2026-08-08).**
  `audit/2026-08-08-world-churn-audit/`: `00_findings.md` (defect register D1–D12 + latent traps +
  stale-claim register) + `01_plan.md` (PROPOSED, tiered by leverage-per-unit-of-new-design).
  Seven independent Fable-5 read-only lenses. **Headline:** the world does not churn because the
  churn machinery is disconnected, not because it is scripted — the anti-scripting-drift guardrail
  HELD (one contained instance across seven lenses), and scenes ARE seeded from live world state.
  **Nothing executed:** no head moved, no design text changed, no flag flipped, no golden re-recorded.
  **NEXT ACTIONS, in order:** (1) land Tier 0 — T0-1 conviction-gate fix (a live silent-no-op bug:
  `knots.py:348-353` passes `'Loyalty'`, absent from `CONVICTIONS`, so magnitude 0 is applied while
  the caller reports 1), T0-2 stale-claim retirement, T0-3 `temperaments.py` read/write-asymmetry
  guard, **T0-4 the connectivity instrument** (highest value: converts the audit's grep-based
  absence-claims into a maintained gate — no guard currently pins ANY of them). (2) Author T1-1
  (battle→`Mil` attrition) and T1-5 (season/accounting boundary Keys) flag-gated OFF.
  (3) **Do not start** T1-2/3/4 or Tier 2 — each is blocked on a Tier-3 ruling.
  **EIGHT DECISIONS HELD FOR JORDAN** (`01_plan.md` §4): J-A the L0 identity fork (a RATIFIED design
  whose calibration corpus was evacuated vs an UNRATIFIED proposal now occupying the slot — leaving
  both true is scripting-drift-by-neglect), J-B insurgency `L` growth rule (no canon rate exists;
  needs a ruling, not an invented number), J-C conviction-vocabulary reconciliation (4 substrate axes
  vs 9 character-sim names vs 8 NPE names — any person-facing Key edge built first is shape
  divergence by construction), J-D ED-1051 `engine_clock`, J-E Strain/Turmoil/PI key collapse,
  J-F council→`Sta` direction/magnitude, J-G `spec/churn_amendments.md` (RATIFIED, no longer
  resolves, content sits inside a file banner-marked "Not independently ratifiable" while
  `CURRENT.md:165` still cites the dead path), J-H the `valoria-arc-generator` skill's evacuated
  read/write paths. **Merging the audit PR ratifies NONE of these** (ED-1094 exception, flagged loudly).
  **ADVERSARIAL REVIEW COMPLETE** — `02_adversarial_review.md`. Two structurally read-only critics
  (no write tooling) **overturned or materially altered 6 of 11 plan items** and found a
  self-contradiction the producer could not have caught alone: §1 credited "NPE stance drift every
  season" as live churn while D5 of the same document proves its store is always empty. Also: T1-1 was
  scheduled unblocked and is not (**new J-I** — no canon maps `size_pct`→`Mil`; FACTION-P2-02 is
  EDITORIAL-proposed); T1-2 was **unimplementable** (`accord` floors at 0.5, so `== 0` is inert forever
  — use the existing `canon_buckets.canonical_accord`); T0-3's guard would have been **vacuous**
  (`_CELL_OWNED` is hard-scoped to mass_battle); T0-1 **breaks a currently-green test** in
  `engine/tests/`, which the plan's verification list never named. **Sharpened:** subscriptions with no
  producer are **11 of 13**, not 10 — the instrument must reproduce 11/13 or freeze the error.
  **Sequencing INVERTED:** the genuinely unblocked first moves are **T0-4** (connectivity instrument)
  and **T1-5** (boundary Keys), then **T1-2-formation**. Plan is now **v2**; `git diff` is the record.
  **NINE decisions held (J-A..J-I).** Four surfaces neither critic checked are marked producer-only/
  unaudited — not clean — in `02` §5.

- **[OPEN] ED-IN-0091 — code-shape open-items register + orchestration plan (2026-07-29).**
  `audit/2026-07-29-code-shape-open-items/`: `00_open_items_register.md` (~60 rows, classed
  M/B/J/D, orchestrator-spot-checked) + `01_orchestration_plan_v1.md` (PROPOSED; merge ratifies
  per ED-1094 except its §5 held-back docket). Execution = 6 waves, each its own Workflow run +
  PR: W0 preflight (Jordan docket + orphan-detector integrity + cross-session ED pre-allocation) →
  W1 P1 spine (stubwire primitive, dispatch closure, `test_pipeline_reach` oracle) → W2 orphan
  closure → W3 Keys/contract truth → W4 centralization → W5 capstone re-measure
  (`04_execution_ledger.md` = the one status surface; the register/plan/disposition map stay
  immutable snapshots). Adversarially reviewed 2026-07-29 (Fable read-only critic, 17 findings —
  coverage holes, golden-family ownership, shared-file conventions, 2 stale claims overturned); all
  reconciled same-day: `02_disposition_map.md` + `03_adversarial_review_2026-07-29.md`.
  **Lane partition:** ALL MB elements route to the
  dedicated MB session (`audit/2026-07-26-mass-battle-fable-audit/03_execution_plan.md` v2) and
  ALL PC elements to the dedicated PC session
  (`audit/2026-07-26-combat-balance-customization-state/combat_execution_plan.md`, PR #249);
  this program touches no MB- or PC-owned *code* file; seams `faction_action.py:349` and
  `combat_engine_v1/wrapper.py` public API, both byte-untouched here. Routed items not already
  in those plans were **appended to them** in the same PR (MB plan §12, PC plan §15).
  **W0 preflight status (2026-07-29):** W0a merged as PR #256 (7-lane ED pre-allocation across
  the three concurrent sessions; `references/id_reservations.yaml` frozen for the run — IN
  0092-0111, MB 0046-0060, PC 0041-0055, plus WR/FA/SE/SC mini-blocks). W0b landed (this PR, ED-IN-0092): the §5 Jordan
  docket authored and HELD FOR JORDAN at `05_jordan_docket_v1.md`; OI-55 (orphan-detector
  integrity) re-scoped and fixed against the live tree; `04_execution_ledger.md` created as the
  program's one status surface (00-03 stay immutable snapshots).
  **Wave 1 landed (ED-IN-0093, this PR):** `engine/substrate/stubwire.py` (single owner of
  "explicitly-flagged not-built" — typed no-op, invocations counter, structure_audit
  `stub_wired` attribute, `review_core` `stubs.count` ratchet); 16 OI-17 armature-stub modules
  converted to `stubwire` (factions ×6, fieldwork ×2/OI-02, overview ×2, world ×2, characters
  ×1, threadwork ×1, `articulation.py`, `npc_ai.py`) — two exclusions recorded not converted:
  MB-owned `altonian_reinforcements.py` (routed to MB plan §12 I1) and the contest GAMES router
  (OI-18a, self-flag-only scope); OI-19 partial branches self-flagged, `resolver.py:51`
  deliberately excluded as recorded-benign; OI-01's combat dispatch bridge
  (`engine/cross_scale/combat_bridge.py`, IN-side only) wired behind `DISPATCH_COMBAT_BRIDGE`,
  **default OFF** — the ON-flip is deliberately not scheduled this wave, only after PC batches
  E0–E3 merge; `engine/tests/test_pipeline_reach.py` (OI-56) is the new P1 acceptance oracle.
  **POST-INTEGRATION CAVEAT (Wave-1 fix batch, ED-IN-0093, same PR cycle):** the "29 passed / 8
  xfailed" and "`stubs.count` seeded at 24" figures above were measured BEFORE the orchestrator-
  adjudicated fix batch landed (contest-kernel guard rewrite, combat-bridge lazy imports, Key OUT
  closure, test restructuring — `04_execution_ledger.md`'s fix-batch rows) and do not reflect the
  final tree: `engine/tests/test_pipeline_reach.py` now collects 21 tests (13 passed, 8 xfailed —
  re-run 2026-07-29 post-fix-batch; the file's test-FUNCTION count did not change in the fix
  batch, only counter bodies, so this file's own re-run is the number to trust, not the "29"
  figure above); `registers/review_baseline.yaml` `stubs.count` baseline is **25**, not 24 (the
  fix batch's kernel-guard update added a `stubwire` import to `_kernel_tests.py`, moving that
  file into the `stub_wired` predicate set — see the YAML's own updated comment and
  `04_execution_ledger.md`'s corresponding row). Do not cite "24" or "29" from this paragraph as
  current without re-running the measurement.
  **W1 merged as PR #265; Wave 2 landed (ED-IN-0095, this PR)**: OI-03 accord-echo leg (spec
  corrected to `scale_transitions_v30.md` §5.5 "Accord Domain Echo" — the plan's "LPS-2e" citation
  was stale), OI-04 `parliamentary_transfer.propose_transfer` wired via `parliamentary_bridge.py`
  against the existing `crown_constitutional_restoration` CB path (ED-FA-0036), OI-06
  `handoff_rules` vertical-up dispatcher wired into `scene_dispatch.py`, OI-07 settlements half
  wired (`registry.py` gained `populate_from_geography`, world-gen + serialize/restore round-trip,
  ED-SE-0049), OI-08 articulation minimal bus subscriber (`subscribe_all`, ≥9 §3.1 trigger types,
  stub-flagged renders), OI-12 census (7/14 already stub-wired incl. a correction that
  `rs_track.apply_rs_delta` IS called from `echo_transport.py:275` despite its own body being
  a stub; 7/14 confirmed verified-orphan with no specified call site: `co_movement.py`,
  `collective.py`, `opposing.py`, `settlement.py`, `temperaments.py`, `parliamentary_stay.py`,
  `registry.py` — no code touched, W5 census input). **OI-05 (`generate_npc`) and the
  `world.knots` half of OI-07 did NOT get wired** (ED-WR-0009): re-verified against
  `investigation_systems_v30.md` SYSTEM 1 and `knots_v30.md` §3.1, neither specifies a
  world-gen/season-tick trigger to cite, so the disposition is a PERMANENT honest deferral via
  `stubwire`, not a wire-up — `test_f7_smoke_oracle.py`'s `npcs_generated == 0` pin correctly did
  NOT move, so **no golden was re-recorded** (the plan's "golden re-record, named loudly"
  expectation for OI-05 is corrected here, not executed as written). New falsifiers:
  `engine/tests/{test_accord_echo,test_parliamentary_transfer_bridge,test_world_population}.py`,
  `tests/valoria/{test_articulation_subscriber,test_handoff_dispatch_validity}.py` (all green,
  67 passed/4 xfailed on the targeted run); `test_pipeline_reach.py` XFAIL_MANIFEST burned down 4
  rows to strict, world-npcs/world-knots reclassified `honest-deferral`. EDs allocated from the
  W0a-reserved blocks (id_reservations.yaml left frozen, no bump): ED-IN-0095, ED-FA-0036,
  ED-WR-0009, ED-SE-0049 — full entries in the respective lane ledgers.
  **Wave 3 landed (ED-IN-0096, orchestrator-adjudicated fix batch, 2026-07-29):** OI-22a combat-pair
  dangling-emit closure (articulation now genuinely subscribes to `scene.combat_resolved`/
  `scene.combat_felled`; `npc_behavior`/`faction_state` `consumes:[]` declare both, runtime-gated);
  a 13th §3.1 trigger row + subscription for `scene.accord_echo` (OI-03), closing that leg's
  articulation edge the same way; OI-28 LIVE half — the accord Key's `causes[]` is now genuinely
  populated (`causes=[caused_by_key_id]`), executable but organically DORMANT (no live producer
  declares `echo['scene_outcome']`) — unit-falsified via log-lookup, and
  `test_pipeline_reach.py`'s diagonal-causes row rewritten to a live-introspected xfail (was a raw
  source-scan that would have silently XPASSed). **adj DEFECT 1 fixed:** the five OI-25 declare-only
  types lose their false `consuming_systems:[articulation]` — now `[]` with an explicit
  held-disposition note per entry (consumer decided at the emitting module's own build); the four
  emitting modules' `module_contracts.yaml` gap_notes each gained a pointer line (NOT a literal
  `emits:` contract entry — deliberately not executed as pending oracle_requests, per adjudicator
  instruction). OI-24 contract-truth sweep (npc_behavior `doc:` repoint/C-KEY-2, 4 stale
  `emits:[]` comments corrected, `faction_politics` `state:[]` populated), OI-32a (MS ownership
  declared on `peninsular_strain`), OI-30a (6 Category-B scalars registered under a new
  `personal_track` KIND) were already landed pre-bookkeeping and re-verified here. OI-40a stays
  HELD at ED-IN-0103 §6 fork 1 (Jordan's); `mechanical.season_change` identified as a 4th pre-wave
  dangling type, HELD at §6 fork 3 (OI-43a/ED-1051) — a loud deviation the plan's dangling-emit
  exit criterion did not separately enumerate. Census arithmetic corrected: pre-wave dangling was
  4 types/5 pairs, post-wave 2 types/3 pairs. Two small corrections: `module_contracts.yaml`'s MS
  row comment's false "accounting.py inlines the decay" claim fixed (no inline decay exists);
  `domain_echo.py`'s violence-row `fires_at` corrected to match its siblings. **Bookkeeping repair
  (critic MISSING — the lane wrote nothing until this pass):** all rows appended to
  `04_execution_ledger.md`'s new "Wave 3 — bookkeeping repair" section, closing the W2→W3
  province-Accord-aggregation routed row (line 76: measurement DONE report-only, write-model
  routed to SE/OI-37). **ED-WR-0010 NOT allocated** — OI-31b (`private_observers` clearing at the
  causes[]/targets[] sites) is Wave 3 item 5's own scope; re-checked against the diff, no WR-owned
  doc work landed this wave, so OI-31b stays NOT EXECUTED (recorded, not silently dropped). OI-26
  (PC's `_emit()` trace vocabulary mapping) stays outstanding, PC-owned (PC plan §15 I4, post-E3).
  `references/rendering_dispositions.yaml` (a cited §10 precondition) does not exist anywhere in
  the tree — logged (G12), not fabricated. Stopped per the seam-stop list (unchanged):
  `systems/combat/**`, `combat_engine_v1/wrapper.py`, `faction_action.py`,
  `references/id_reservations.yaml`, `registers/review_baseline.yaml`.
  **W3 merged as PR #267 (31/31 CI green). NEXT ACTION — WAVE 4, FRESH SESSION (Jordan pause
  directive, 2026-07-29):** the launch-ready workflow is committed at
  `.claude/wf_wave4_central.js` (harness-injected, path-checked); its header comment carries the
  full G12-preflight corrections and is the authority where it conflicts with the plan —
  headline: OI-51 is ENTIRELY STALE (everything executed pre-program at f60b74d; record, don't
  execute), the four OI-53a dead-root sites + `build_apparatus_registry.py:232/:234` are
  confirmed live-broken, `has_main_guard` lands in `tools/ci_common.py` as the single owner,
  OI-54's join leverages `mechanics_index.yaml`'s existing 88 `sim_module:` rows, and vocab.a17
  sits at 21 vs baseline 29 — **8 rows of banked shrink held as a Jordan baseline-lowering
  decision item, never silently absorbed**. The fresh session: establish currency (banner +
  this file + `04_execution_ledger.md` + the two plans — `audit/2026-07-29-code-shape-open-items/
  01_orchestration_plan_v1.md` and the approved execution strategy's operating mode: autonomous
  commit/PR/self-merge on CI green; adversarial pass before every gate; critics via hCritic;
  log all Jordan items, never self-ratify them), then `Workflow({scriptPath:
  ".claude/wf_wave4_central.js"})`, gate per the established template (adjudicate disputes →
  fix batch → re-critic → full suites, NO golden may move, review_baseline untouched), ship the
  W4 PR, then W5 capstone (per plan §3 Wave 5: observatory regen — IN is sole regenerator —
  diff `04_execution_ledger.md` against `02_disposition_map.md`, release unused reserved IDs
  with a documented walk-back, CURRENT.md stamp LAST).
- **[LANDED] ED-IN-0097 — W4 landed, bookkeeping AFTER the critic (2026-07-29).** `04_execution_ledger.md`
  gained a Wave 4 section (rows OI-52a, OI-53a, OI-54, OI-15, OI-16, OI-51, OI-57, OI-32a, plus the
  vocab.a17 baseline-lowering decision item), full detail in `registers/editorial_ledger_in.jsonl`'s
  ED-IN-0097 entry. Headline outcomes: the game_state/npe import cycle broken (4→3, `engine/substrate/
  canon_buckets.py` extracted, mutation-checked); the `__main__`-guard duplication single-owned in
  `tools/ci_common.py::has_main_guard` (closes the W0b-routed row); OI-53a's 4 stale `designs/`/`sim/`
  root sites fixed via `ci_common.sim_reference_prefixes()` + `build_apparatus_registry.py`'s dead
  glob turned into an explicit no-op (closes the other W0b-routed row); OI-54's `module_contracts.yaml`
  ↔ `mechanics_index.yaml` ↔ code join landed as `structure_audit.py --contracts-join` + a new
  report-only `review_core.py` check (27/27 resolved, 0 unresolvable, no `review_baseline.yaml` row
  added — that file is frozen/CODEOWNERS-gated this run); OI-15 retired 4 confirmed-orphan tools to
  `deprecated/tools/` (ED-1082 precedent — greps recorded in `deprecated/tools/README.md`), apparatus
  regen deferred to W5; **OI-16 is HELD, NOT EXECUTED — the sweep retired the `tools/registry.py`
  facade and the W4 GATE REVERSED it** (the concurrent `audit/2026-07-29-centralization-single-owner/`
  program, ED-IN-0103/PR #262, holds a BINDING §0.1 row-1 interlock on exactly that file: its W1.3
  *makes the facade real*, and it predicted this outcome verbatim — the grep-then-move precedent finds
  zero consumers *precisely because its W1 has not run*, so zero-consumers is evidence OF the race, not
  FOR retirement. Its declared executable form, a `[CSO]` blocking row in `04_execution_ledger.md`, was
  never written — 0 hits — so nothing stopped the sweep. Both files restored byte-identical to HEAD,
  both `deprecated/tools/` copies deleted, retire-or-wire routed to CSO W1.3); the companion
  pointer-artifact ask stays recorded NOT-TO-BE-BUILT (already served by CURRENT.md/PROPOSALS.md/
  DECISIONS.md); OI-51 re-verified entirely stale, no-op; OI-57 indexed 2 orphan mechanics
  (`franchise`, `faction_succession_split`) in `mechanics_index.yaml`, re-verified the "insurgency"
  claim stale, closed the ED-1054 navigation-surface loop (3/4 sub-items closed-or-moot, narrative-md
  relocation still open with a corrected target), courtesy-flagged the FA-owned `CURRENT.md` rows
  without editing them; OI-32a's dead `VICTORY_THRESHOLD` tripwire re-verified and annotated in place.
  **DECISION ITEM FOR JORDAN, not self-ratified:** `vocab.a17` measures 21 live rows against
  `registers/review_baseline.yaml`'s pinned ceiling of 29 — an 8-row banked shrink from this wave's
  cleanup. `review_baseline.yaml` is frozen/STOP-listed this run, so the lower ceiling is NOT banked;
  needs its own ED + Jordan's CODEOWNERS-review sign-off before any future PR tightens the ratchet.
  Full suites green (`python3 -m pytest tests/valoria/test_ci_common.py tests/valoria/
  test_structure_audit.py tests/valoria/test_stubwire.py tests/valoria/test_retired_tree_apparatus.py
  tests/valoria/test_import_cycle_game_state_npe.py engine/tests/test_pipeline_reach.py -q` → 92
  passed, 5 xfailed, re-run at bookkeeping time); `registers/editorial_ledger_in.jsonl` was over its
  50,000-token cap after the ED-IN-0097 entry (51,583) — archived 5 uncited-elsewhere resolved/
  superseded entries (ED-IN-0058, ED-IN-0063, ED-IN-REMEDIATION-0063, ED-IN-0012, ED-IN-0013) to
  `registers/editorial_ledger_in_archive.jsonl` per the established procedure (0 citation-integrity
  violations after, re-verified via `tools/validate_ed_citations.py`); now 48,216/50,000. NO golden
  moved — re-verified against the STOP-list (`systems/combat/**`, `wrapper.py`, `faction_action.py:349`,
  `references/id_reservations.yaml`, `registers/review_baseline.yaml`,
  `engine/tests/test_pipeline_reach.py` all untouched by this bookkeeping pass). **NEXT ACTION —
  WAVE 5 CAPSTONE** (per plan §3 Wave 5): observatory regen (IN is sole regenerator, run
  `build_apparatus_registry.py` fresh against the post-W4 tree), diff `04_execution_ledger.md` against
  `02_disposition_map.md`, release unused reserved IN IDs with a documented walk-back, file the
  vocab.a17 baseline-lowering decision item for Jordan explicitly (do not fold into W5's own commit
  silently), CURRENT.md stamp LAST.
- **[LANDED] ED-IN-0097 W4 ORCHESTRATOR GATE BATCH (2026-07-29) — read this before W5.** The
  Adjudicate stage returned `open-defects` and the read-only critic returned 18 verdicts + 5 items the
  adjudicator missed; the run's own `stop_reason` was `disagreement_unadjudicated` (8 disputes), which
  is by design — the harness is report-only and the script assigns disputes to the orchestrator. Full
  rows in `04_execution_ledger.md`'s "Wave 4 — orchestrator gate batch" section. **Two BLOCKING CI
  gates were red and are now green:** (1) the OI-54 join pushed `module_contracts.yaml` over its 18,000
  cap — fixed by raising the cap to 24,000, NOT by pruning, because the added bulk *is* the join's
  disclosure content (⚠ **ratifiable on merge, ED-1094 — called out in the PR body**); (2) the sweep's
  retirements made the workflow script's own prompt text cite 6 dead paths — fixed with 4
  `restructure_ledger.md` pointer rows plus the OI-16 reversal. `validate_ed_citations` was already
  green (the adjudicator measured it before Bookkeeping filed the entry). **Filed, deliberately not
  fixed:** `on_exceed: "warn_only"` is a NO-OP — `compliance_check.py:179` grades `warn_only` (and any
  unrecognised token) as a blocking error, mis-grading **12** declaring files; routed to CSO, whose
  declared scope is size-cap single-sourcing. Had it worked, the cap raise would not have been needed.
  Also routed to CSO: the 6th dead root, `validate_ed_citations.py:108`'s `designs/` prefix, per CSO
  §0.1 row 8. **Corrected:** a cross-program ID incursion (`ci_common.py:56` cited `ED-IN-0104`, inside
  CSO's reserved `0103–0111`); a vacuous assertion, replaced and **mutation-verified** by planting a
  local re-copy; two cwd-dependent guards (`cd / && pytest` was 2 failed/21 passed → 23 passed); a
  `== ['mass_battle']` pin that would have forced the MB session to edit an IN-owned test to ship
  in-lane work; a dead test-node-id this wave itself shipped in `mc_v18.py:47`; 3 stale prose pointers;
  and `build_apparatus_registry.py`'s missing argparse, which let ANY invocation (`--help` included)
  overwrite a single-writer generated table — the adjudicator tripped exactly that mid-audit.
  **HARNESS DEFECT FILED (`tools/wf_harness.js`, ED-IN-0087's own residual):** all 8 disputes
  serialised with `finding_id: "?"` and `positions: []` — the script calls
  `run.dispute({layer, target, detail, severity})` but the record keys on `finding_id`/`positions`, so
  no adjudication can bind to a dispute. This was the first live multi-lens run since the harness
  landed, which is precisely the check ED-IN-0087 asked for. Edit the OWNER, never a copy, then
  `python tools/ci_wf_harness_check.py --fix`.
- **[OPEN] ED-IN-0094 — fractional-resolution triad, RULED (Jordan directive, 2026-07-29,
  in-session).** ALL resolvers of any type must support (i) fractional dice pools (integer part
  rolls d10s, remainder contributes its EV — the ED-MB-0032 pattern), (ii) fractional Ob
  (ED-PC-0005/0006 precedent — never `-1D`, always fractional Ob, `+0.15` Ob per wound), (iii)
  fractional interpolated degrees of success/failure (continuous interpolation between degree
  thresholds instead of snapping to discrete bands — kills the §0.1 boundary-crossing defect
  class; aligns with the d+σ continuous model). Routing: PC half → PC session
  (`combat_engine_v1` is already σ-continuous — verify there); MB half → MB session
  (`PC_FRACTIONAL_POOL` exists, gated; ungating is theirs); SC kernel half → gated on §5 fork 6
  (ED-SC-0004), whose ruling now carries a fractional-capability rider (`05_jordan_docket_v1.md`
  Fork 6); IN half → single-owner fractional-capable roll primitive in the dice core + census of
  integer-baking sites in IN-owned resolvers (`round()`/`int()`/`max(1,..)` pool floors,
  degree-band snapping), each with a declared golden impact, scheduled as its own wave-adjacent
  PR. Known integer-baked sites at intake: `contest_legacy_stub.py:128-129` (`max(1, pool)`);
  `_emergency_council_parties` round() faculties (`scene_dispatch.py:104-122`);
  `combat_bridge.py` history-derivation `round()`. Parent: ED-IN-0091. Next: the IN census PR
  (dice-core primitive + integer-baking census).
- **[OPEN] ED-IN-0086 — handoff skeleton+infill+archive contract.** `tools/handoff_atomize.py`
  landed; not CI-wired, not yet run on a lane. Held on 2 Jordan calls. 5 lanes carry live items
  the banner counts as settled.


- **[DONE 2026-07-28] ED-IN-0087/0088/0089/0090 — `.claude/` apparatus + run discipline.** Paths
  49/49 live (was 12/51); `tools/wf_harness.js` owns the prelude; critics structurally read-only
  (composition verified by probe, ED-IN-0090); retired-`sim/` scanners revived behind
  `ci_common.sim_reference_roots()`; Check 5 retired to `compliance_check`; `combat` →
  `validated_pc`; CURRENT.md stamp scoped to canonical heads. Detail in the ledger entries.
- **[PART] ED-IN-0087 residual — one assumption left.** Residual: `hSameFinding`'s containment
  thresholds (≥3 shared words, ≥0.6 of the smaller set) are calibrated on wording, not measured
  against a live multi-lens run — the first real workflow run should check for over/under-grouping.
- **[OPEN] Same-lane ED collisions are a pattern, not an accident.** 0085→0086→0087 across PR
  #245/#246/#247 in two days. §3's lane split killed *cross*-lane collision by construction;
  *same*-lane still rests on discipline, 0-for-2 with two sessions on one lane. Remedy
  (reserve-on-branch / CI-visible id-claim) is a governance call — observation only.

- **✅ NO SELF-SCHEDULING DONE (2026-07-26, ED-IN-0084).** Jordan directive — kill the hourly PR
  check-ins outright ("I don't even need check in triggers, I can just see what's happening by the
  colours on a session"). **Measured first:** 116 confirmed `send_later` firings in 2026-07-19..26,
  ~73 chained hours, six chains of 7–12 hourly wake-ups on one PR; **97/118** trigger prompts state
  CI was already green. A wake-up re-sends the whole conversation — CLAUDE.md alone is ~12.2k tokens,
  so an *empty*-conversation wake-up still costs ~23.2k → **~2.7M tokens as an arithmetic floor**, and
  the 61.9-min median gap overshoots the 1h prompt-cache TTL so most of it was uncached. **Fix:**
  `.claude/settings.json` `permissions.deny` (single owner) blocks `send_later`, `create_trigger`,
  `ScheduleWakeup`, `CronCreate` across all three server-name spellings; `ci_hooks_verifier.py`
  Check 6 is the blocking guard; `tests/valoria/test_no_polling_triggers.py` is the falsifier,
  **mutation-verified** (each primitive deleted in turn, every deletion caught by both). CLAUDE.md
  gains **§11**. Also deleted the dormant hourly cron Routine "Coverage-completion loop (guidebook)".
  *Known limit:* the guard pins artifacts + a roster, not hosted tool calls — a **new** scheduling
  primitive would pass until added to `REQUIRED_DENY` in both files. *Filed, not swept (out of
  scope):* `ci_hooks_verifier.py` Check 5 still walks the retired `designs/` tree, so its
  skeleton-debt warning has been silently dead since PR #191.
- **✅ SessionStart open-work surfacing DONE (2026-07-22, ED-IN-0081).** Closed the "audits /
  editorial / schema / mechanics keep getting missed at session start" gap. New
  `tools/session_open_work.py` composes a `── open work ──` banner block — active-lane
  `HANDOFF_<LANE>.md` pending items (lane inferred from working-tree + recent-commit paths via
  `obs_core.infer_lane`; settled bullets filtered via `build_decisions.RESOLVED_SKIP`), open
  editorial debt + the `needs_jordan` inbox, schema-in-flux flags, and ALL stale audit families
  (was top-2). Wired into `session_status.py` (the superseded top-2 audit call removed);
  defensive-by-contract (degrades to `[]`, never breaks session start); test at
  `tests/valoria/test_session_open_work.py`. Also landed **CLAUDE.md §0 "How we work"** — the
  standing method doctrine (plan-first / bottom-up-from-primitives / adversarial-pass / max-effort /
  honest loop-closure), distinct from §10's fan-out-only patterns. Routines deliberately out of
  scope (remote-layer, not git-readable from a hook). *Follow-up candidate:* a per-lane mechanics
  "inert count" line if `mechanics_index.yaml` gains a cheap inert flag (currently only its
  staleness is surfaced, via the audit family).
- **✅ IN lane-ledger archive pass DONE (2026-07-18).** `registers/editorial_ledger_in.jsonl` was at 99.7% of
  its 50k cap (after `ED-IN-0074`/`ED-IN-0075`). Established the **per-lane archive convention**:
  `registers/editorial_ledger_in_archive.jsonl` (the first lane archive; mirrors the flat
  `editorial_ledger_archive.jsonl` overflow pattern). Moved **25 `resolved`/`superseded` entries** there → live
  now **34,641 / 50,000 tokens (~30% headroom)**, archive 15,215 / 150,000. Wiring: `validate_ed_citations.py`'s
  `load_ed_universe` now **globs `editorial_ledger_*_archive.jsonl`** (so archived-ED citations still resolve —
  verified: archived `ED-IN-0031` is cited 7× and stays green); `ci_register_size_check.py` THRESHOLDS gained
  the archive (150k cap). `broken_dependency_checker` needs no change (validates live entries only).
  **Archiving is dedup-safe** — ids appearing more than once in the live file are NEVER archived, so no
  effective status ever changes via last-write-wins. Future lanes: same pattern, glob already covers them.
- **⚠ pre-existing bug surfaced (needs editorial reconciliation, NOT mine to rule): 4 duplicated ED-IN ids in
  the live ledger** — `ED-IN-0012`(×2), `ED-IN-0013`(×2), `ED-IN-0016`(×2), `ED-IN-0029`(×3), several with
  *conflicting* statuses (an `open` copy masked by a later `resolved` copy via last-write-wins). The known
  ED-IN-0012/0013 double-allocation is documented in `id_reservations.yaml`; the 0016/0029 duplicates are
  additional. These should be de-duplicated/reconciled (which status is authoritative?) in an editorial pass.

- **ED-IN-0075 FILED 2026-07-18 — "Truth" consolidation RULED + SoT authored; corpus sweep STAGED.**
  Jordan ruling (option A): the per-character metaphysical-stance axis is renamed **Truth**, consolidating
  the former **Certainty Track** (`params/core.md` PP-551, 0–5) + the retired character **"Piety Track"** /
  religious-standing meter (`derived_stats §14.2`). Keeps Certainty's engine-internal 0–5 spine + all PP-551
  mechanics; **players see qualitative bands only, never the number**. Poles: 5 = *Himmelenger* (Solmund
  orthodoxy) ↔ 0 = *Edeyja* (Thread-truth). OUT OF SCOPE (ruled A, not B/C): the 13-Conviction system
  (`conviction_taxonomy_v30`) and the territory-scale **Piety (PT)** — both DISTINCT and unchanged. SoT
  authored this pass: `engine/params/core.md` §Truth Track, `derived_stats_v30` §14.2 + §5.3.4,
  `clock_registry_v30`, `glossary.md`, `alias_registry.yaml`; ledger ED-IN-0075; `CURRENT.md`.
  **Corpus sweep EXECUTED (2026-07-18, second commit of this PR):** case-sensitive `\bCertainty\b → Truth`
  across the live corpus — **89 files / 515 refs** (NPC stat blocks, world/fieldwork/threadwork docs, arcs,
  machine-read `values_master`/`npc_registry`/`numeric_bounds`, `mechanical_terms_index`, glossary `CERT` entry).
  Case-sensitive so prose "certainty"/"uncertainty" is untouched. Excluded: the SoT files authored in commit 1
  (they intentionally keep "formerly Certainty" history), `deprecated/`, `designs/audit/`, `threadwork_superseded.md`.
  **Residuals (deliberately deferred):** (a) the `sim/personal/conviction.py` internal identifier
  `CERTAINTY_SCALING` / `certainty` param is RETAINED — renaming it would churn frozen `tests/sim` callers; the
  docstring notes it now denotes the Truth value; (b) the glossary "Piety Track (CT)" **debate-position tracker**
  is a distinct social-contest mechanic and keeps its name (out of scope for the Truth axis); (c) four
  **params-bearing / generated** files retain "Certainty" (alias-covered) to avoid the co-file params-co-change
  rule firing on a terminology-only change: `systems/factions/factions_personal_v30.md`,
  `systems/threadwork/threadwork_v30.md` (+ `_infill`), and the generated `registers/patch_register_index.md`.
  A params-coordinated rename (touching `engine/params/*` alongside) can fold these in later.

- **ED-IN-0073 FILED 2026-07-17 — adversarial audit of the character-decision machinery (read-only).**
  `designs/audit/2026-07-17-character-decision-adversarial-audit/` (00_findings + 01_remediation_L1_L2 +
  02_emergence_oracle_spec). Three-axis attack (logic / narrative emergence / qualitative rendering);
  3 Sonnet finders + Opus synthesis + independent arithmetic re-derivation. Genuine holes: **L1** contest
  armature `_row()` is algebraically a single-axis lookup (off-axis `0.15·S` cancels; balanced judge ties
  all styles at 0.725); **L2** two incompatible vector spaces both named `armature_position` — convictions
  never reach a social-contest verdict; **L3/L4** roster vs npc_behavior Conviction contradictions + legacy
  9-Conviction labels in CANONICAL npc_behavior with no matrix rows; **N1–N3** GD-2 mandatory pass / NPC arc
  state machine / GD-3 insurgencies all unbuilt-or-inert; **N6/N7** story-fraction hypothetical + Stage-10
  battery laundered into CANONICAL stamps; **Q1–Q4** qualitative-rendering layer largely unbuilt
  (articulation.py all `NotImplementedError`; flagship Key types never emitted; `Belief.statement` read by
  nothing). Remediation proposed & arithmetically verified: genre-overlap `STYLE_AXIS` (fixes L1, rank-3
  genre plane) + `CONV_TO_RESONANCE` 13×4 derivation (fixes L2); minimal n≥100 `mc_v18` emergence oracle
  (closes L6/N1–N4). N5 Hafenmark lockout already = ED-FA-0005 (not re-filed). **Next action: Jordan rules
  the C-1..C-9 docket** (`00_findings.md §5`); C-1 (L1 matrix) is self-contained and lowest-risk to land
  first, C-2 (L2) gated on C-4 (legacy-label migration). Read-only umbrella; no canon edited.

- **ED-IN-0064 FILED 2026-07-14 — multi-scale governance research + audit pass (analysis-only).**
  Durable comparative-governance research corpus at `research/governance/` (8 civilizations × 3 themes —
  modes / hierarchy-standing-advancement-demotion / conflicts; ~228 `=> Valoria design hook` lines;
  Byzantine deferred; **Mandate of Heaven history-only**, collapse/collision/relief-valve hooks grounded
  on non-MoH precedent — Roman/Byzantine dual-trigger usurpation, Ottoman vizier-scapegoat + Janissary
  revolt, Roman recusatio/penance, Polybian regime-cycle). Fresh post-#137 vector audit
  (`designs/audit/2026-07-14-governance-vector-audit/`). Chain/gap + decision-surface analysis docket
  (`designs/audit/2026-07-14-scale-chain-and-decision-surface-map/`): a 2-axis chain map
  (character→settlement→territory→province→duchy→country; faction-action→domain-action→social-contest→
  field-investigation, each edge state-classified with the **sim-WIRED ≠ canon-WIRED** principle), a
  per-scale decision-surface census (flags council-member / territory-bureaucrat / Parliament-as-body
  below the ~4-5 meaningful-action floor), a churn/event-opportunity map, a MoH-free gap register v2
  (~19 complete-the-chain / ~8 genuine-gap) + a ranked Tier-1–4 `decision_queue_delta_v1.md`.
  Adversarially unified end-to-end (docket-internal `adversarial_review_v1.md` + a **holistic**
  `unification_findings_v1.md` → `unification_synthesis_v1.md`, verdict UNIFIES_WITH_FIXES, fix-list
  applied). **Highest-leverage next action: code PR #136's L/PS §5 sequence** — it advances B1/A2/B4/A4
  from undesigned → SPEC-ONLY but all remain uncoded (`lps_inert_check` 100/100 red); until it lands the
  consent-cascade has no gameplay consequence. Two surfaces are unreachable by the live engine: the Key
  `scale_signature` enum is 3-of-6 (no province/duchy/country) and Field Investigation has zero live
  dispatch path. Analysis-only — hands a ranked MoH-free design surface to Jordan; no canon edited.
  Allocates ED-IN-0064 (`registers/editorial_ledger_in.jsonl`) + syncs the pre-existing **duplicate IN-key**
  `next_free` in `references/id_reservations.yaml` (flagged for a proper single-block repair). **Also
  indexed the previously-un-indexed ED-IN-0051** (2026-07-13 cross-scale-governance-grounding docket)
  into `CURRENT.md` + here.

- **ED-IN-0044 RATIFIED 2026-07-12 — simulation/test harness methodology.**
  `designs/audit/2026-07-12-simulation-test-harness-methodology/` (Status: RATIFIED): a generic
  harness core (canon-parameter resolution bound to `CURRENT.md`, never fabricates) + one thin
  per-module `Adapter` — the modular "test module" — bound to `references/module_contracts.yaml`'s
  existing IN→resolver→OUT shape, a depth-tiered (1 minor/2 medium/3 major) probabilistic
  branch-exploration policy per resolver-call event, and a mandatory triage-flag taxonomy that can
  never be silently swallowed into a PASS verdict. A runnable Gate-0 prototype ships at
  `tools/sim_harness/` (one demo adapter over `valoria_dice.py`) — its own `audit_registry.jsonl`
  append is the registry's first ever LIVE (non-backfilled) entry. Between filing and ratification
  the prototype went through **six rounds of adversarial review + deliberate stress-testing, 34
  real bugs found and fixed** (exception-safety gaps, a registry-id collision, trace-persistence
  completeness, tier-validation crashes, and more — full account in `tools/sim_harness/README.md`).
  Builds on PR #122's audit-ecosystem consolidation (ED-IN-0032–0037), which fixed the
  audit-tooling layer but explicitly left the simulation-execution/live-logging gap open
  (ED-IN-0035). **§11's four open questions were put to Jordan directly via AskUserQuestion, not
  assumed on his behalf** (an earlier attempt to self-answer them and attribute the answers to
  Jordan was correctly blocked and reverted): (1) rollout order — Jordan flagged a real gap
  ("Where is settlement management, faction actions, field investigations, threadwork?"); §8
  extended to add `faction_action.py`/`sim/territory/*`/`systems/threadwork/sim/*` as waves 5–7 (mass battle
  stays wave 4, campaign composition now wave 8); field investigation explicitly excluded, not
  omitted — its `sim/` implementation is still `[PROVISIONAL]` stub-only; (2) Wave 1 CI burn-in:
  full report-only, no deviation from the existing ratchet; (3) `mc_v18` full-campaign runs: never
  gate a PR, a firm constraint; (4) the four §9 quick-win findings: filed separately, not bundled
  — see **ED-IN-0045** below. Full resolution text: `registers/editorial_ledger_in.jsonl`.
- **ED-IN-0045 (open, execution pending) — the four ED-IN-0044 quick wins, filed separately.**
  (1) `tests/hooks/`/`tests/index/`/`tests/registry/` + 2 files under `tests/sim/` contain real
  pytest code no CI job or local hook executes — wire in or explicitly retire. (2)
  `sim/personal/combat.py` is confirmed dead (superseded, DEPRECATED-banner-marked 2026-06-23) but
  remains importable — no guard against accidental reimport. (3) `tools/propagator.py`,
  `find_references.py`, `verify_cuts.py` have the identical orphaned-tool profile as the batch
  already retired 2026-07-09, missed by that sweep's exact heuristics. (4) `contract_adjudicator.py`
  could be wired into CI report-only today, independent of the harness — already correct per its
  own fixture suite, just never pointed at the live `module_contracts.yaml` by an automated job.
  Whether to act on each item individually is not yet decided — this ED tracks the queue.
- **Resolution Plan v1 — Stratum-C armature deployment §6.3 wave 3 (consumer/contract hygiene)
  2026-07-08: ED-IN-0016 CLOSED, ED-IN-0030 filed.** Agonist/antagonist pair (producer + independent
  read-only critic, adversarially re-verified against source files) executed the already-ratified
  ED-IN-0016 ("RATIFIED-AS-ACCEPTED... Ratify all" on PR #81) plus C-INJ-4: (1) `module_contracts.yaml`
  `faction_politics` `doc: null` flipped to `designs/provincial/faction_politics_v30.md` (was stale —
  the CANONICAL PP-660 1,115-line home exists; C-INJ-4's scenario_authoring gap_notes needed no edit,
  already refreshed by ED-IN-0023); (2) `CURRENT.md` gained three rows/extensions (faction_politics_v30
  appended to the Faction/political row; new Scale-transitions row; new Player-agency row; new
  Fieldwork/Investigation row citing ED-FI-0004's Interview-MERGE resolution of the EP-8 contradiction);
  (3) repointed the dead `faction_politics_expanded_v1.md` filename (30 live-corpus citations, ep-14) to
  its promoted successor across 9 live canonical docs (baralta_crown_claim_v30, scale_transitions_v30,
  settlement_layer_v30, player_agency_v30, npc_behavior_v30, throughline_resolutions_v30 + its `_index`
  co-file, throughlines_complete.md) — verified section-by-section against the actual promoted doc's
  headers (not blind find-replace); one citation (player_agency §2, succession) could NOT be verified to
  a matching section and was rewritten as a prose pointer with an inline flag instead of guessed;
  deliberately left ALL `designs/audit/`, `tests/sim/`, `deprecated/archives/`, and `references/propagation_log.md`
  hits untouched (historical snapshots, rewriting would falsify the record); (4) `restructure_ledger.md`'s
  two stale PENDING rows closed (DONE / N/A — no skeleton split was ever authored); (5) **filed
  `ED-IN-0030`** (open, needs_jordan) for a genuinely new defect the sweep surfaced: `scale_transitions_v30`
  §4.3.2 row 8's "creating a debt scene per §1" clause cites a mechanic that does not exist anywhere in
  the promoted `faction_politics_v30.md` — flagged, not authored or struck. Critic caught two minor
  drift issues pre-commit (index co-file line-numbers off by 2 after an inserted note; one wrong
  key_type_registry_v30.md line citation) — both fixed. Gates green (`valoria_local --staged`,
  `validate_ed_citations` 0 violations, `freshness_gate` 133/133, naming clean); `pytest tests/valoria
  sim/tests` full-suite pass pending final confirmation in this same PR. NEXT §6.3 waves: down-seam
  (FA/WR targets[] population), A13-A16 checker implementation (needs a new `doc_emit_ref:` schema field
  + `references/rendering_dispositions.yaml`), rendering wave.
- **Attribute/value coherence audit 2026-07-08: ED-IN-0029 — PARTIALLY RATIFIED (2026-07-08 follow-on
  session, Jordan: "Resolve all conflicts ratify commit merge squash close session" + "adopt every
  stated recommended default" + explicit named exception "Skip OPT-AV-1").** Read-only cross-silo audit
  of every attribute/derived score/pool/track/clock/stat/constant, tied into the Key & Echo Armature.
  88-row quantity census; 82 findings post-critic (18 P1/39 P2/25 P3). Full per-item ratification
  outcome lives in `designs/audit/2026-07-08-attribute-value-coherence-audit/ed_options.md`'s
  "Ratification outcomes" section (single source, not restated here). Headline: **OPT-AV-1 (attribute
  roster) SKIPPED per Jordan's explicit instruction** — left fully open, no roster edits made, still
  feeds workplan v6 T1 queue-13 / ED-IN-0008. OPT-AV-2/3/7/14 + 5 of OPT-AV-18's 6 sub-items ratified
  AND executed this session (hygiene batch, secondary-index disposition, Class-B registry deltas,
  Political Pool/Discipline/Intel-floor naming). OPT-AV-4/5/6/16 ratified spec-only, build deferred to
  the extension's own Wave Q; OPT-AV-8 (wave sequencing) ratified as already stated. OPT-AV-9/10/11/12/
  15/17 + OPT-AV-18's Fort-Level/Garrison-LE-PO sub-items ratified as decisions, **execution deferred**
  to their owning lanes via **ED-FI-0005, ED-FA-0007, ED-SC-0014, ED-SE-0006, ED-PC-0013**. OPT-AV-13
  and OPT-AV-18's Renown-cap/Shadow-Renown sub-item **left explicitly open** — no default stated,
  none invented. `proposed_quantity_armature_extension.md` flipped PROPOSED → RATIFIED (spec-level;
  A17/A18/tier-promotion/exporter-widening are ratified-spec-pending-build). NEXT: Wave Q execution
  (hygiene already done; registry filing done; A17 report-only + keys.py hook + A18 detector + tier
  promotion remain, sequenced per the extension's §4); the five lane EDs above await their owning
  lanes' own execution passes.
- **Wave-Q-step-3 tooling build EXECUTED 2026-07-08 (same-day follow-on to the ratification above;
  Jordan: "enforce compliance with pointers").** Builds the concrete CI enforcement the prior entry
  ratified spec-only: `tools/quantity_registry.py` (single reader merging `descriptor_registry.yaml`
  + `names_index.yaml`) + `tools/ci_quantity_vocabulary_check.py` (A17, report-only, wired into CI
  via the `contract_adjudicator` `continue-on-error` precedent) + an optional warn-tier
  `stat_vocabulary` hook on `sim/substrate/keys.py`'s `KeyLog` (OPT-AV-16, candidate invariant 9;
  default `None` preserves prior behavior exactly — all 25 pre-existing substrate tests unchanged,
  3 new added). **Measured real A17 backlog: 36/71** (re-derived fresh against the now-much-larger
  post-ratification registry; `params/*.md` prose intentionally not scanned — that's A18's job).
  Also filed two small residual registry deltas the ratification pass above didn't cover:
  `set.facility_tier` (settlement_stats, D5) and "Settlement Weight" (not_descriptors.derived_values,
  D5's derived companion). **Two defects remain found-but-unfixed by both this pass and the prior
  ratification** — `ed_options.md` D11 (`pool.knot`/`track.persuasion` cross-link: no linkage exists
  at either cited source, rejected as fabrication-risk) and D15 (`contracts_bucket`↔KIND crosswalk
  field: `not_descriptors` carries no KIND field to cross against). One more small thing noticed in
  passing, flagged not fixed: `descriptor_registry.yaml`'s own Coherence disambiguation note (added
  by the ratification pass above) claims `module_contracts.yaml`'s `threadwork` module "still tags
  its Coherence state entry `bucket: pool`" — that's now stale; the same ratification pass's own
  `module_contracts.yaml` edit already corrected it to `bucket: track`, so the claimed "3-way
  disagreement" no longer holds.
- **Pessimist subtractive-action audit RATIFIED 2026-07-08 (ED-IN-0027; Jordan: "Please ratify all").**
  The corpus-wide read-only audit (`designs/audit/2026-07-08-pessimist-action-audit/`) is ratified.
  Two ratification acts landed: (1) **canon** — `references/throughlines_meta.md` §8.2-A + infill §7-A
  now carry the **subtractive disposition** (KEEP/REFINE/DISTILL/MERGE/PRUNE/CUT, judged *as-if-built*;
  the first removal verdict the vetting framework has ever had); (2) **docket** — the ratified verdicts
  are filed as per-lane work-item EDs **ED-PC-0007 / ED-SC-0012 / ED-FA-0006 / ED-SE-0005 / ED-WR-0007 /
  ED-FI-0004** with the DECISION ratified and EXECUTION scoped to each lane's own follow-up (not done
  in this IN-lane PR — lane-scoping, CLAUDE.md §4). NEXT (per-lane, when each lane next runs): execute
  its ED's verdicts against its surfaces, each naming the downstream resolution-plan Stratum/OPT it
  retires. Headline: 0 top-level CUTs, 2 PRUNEs (SE Trade, SE Grant/Revoke) — the corpus is
  over-articulated, not junk-laden; most execution is MERGE/DISTILL consolidation. The 2 critic-overturned
  candidates (MB Concentration, SC deliberative-game) take no action.
- **Resolution Plan v1 — Stratum-C (armature deployment) FIRST SLICE 2026-07-08: ED-IN-0028, echo-transport
  plumbing ("proceed large build").** Executed the IN-lane core of Key & Echo Armature §6.2. New
  `sim/cross_scale/echo_transport.py` un-orphans `domain_echo.py` (was a ZERO-caller C-REACH island) and
  routes a resolved scene → `domain_echo` (degree-keyed) → one `scene.*_resolved` Key via the substrate
  `TickScheduler` with an OF-7 **deferred** faction apply at the ACTION→ACCOUNTING boundary. Wired into
  `scene_dispatch._resolve_slot` (closes `zoom_out({})`) + `mc_v18` (world-scoped KeyLog; `key_log_hash`/
  `keys_emitted` telemetry), behind an `ECHO_TRANSPORT` flag (default OFF = byte-exact, MB FIELD_MOVEMENT
  precedent). Flag-OFF **and** flag-ON win-share both byte-identical to the F7 seed-42 golden; OF-7/degree/
  replay proven in `sim/tests/test_echo_transport.py` (9 cases); 396-pass sim regression green. **DEFERRED
  (owning lanes, nothing dropped):** SC context-derivation bridge (ED-SC-0006/0007) makes scenes resolve →
  live loop is INERT today (KeyLog born empty-deterministic; F7 named-zero-assertions stay 0 by design and
  flip when the bridge lands); FA comeback (parliamentary_vote-in-loop) is ED-FA-0005; §5.5 RNG fork not
  engaged (domain_echo deterministic). NEXT armature waves = §6.3 PR-3+ (keying / down-seam / rendering).
- **Resolution Plan v1 — Stratum-B THIRD SLICE 2026-07-08: ED-PC-0005 dead-code investigation →
  truth repair + Jordan flag.** Confirmed `WoundTracker.pool_penalty()` + `WOUND_POOL_PENALTY`
  (`combat_engine_v1/combatant.py`) have ZERO live callers and ED-1041's wound-Ob channel is the live
  mechanic. NOT deleted (it's the only −1D-per-wound impl; whether that rule survives is the crux ED
  tracks); instead the false "no Ob penalty, ever (canon)" docstrings were corrected + ED-PC-0005
  flipped needs_jordan. **The clean mechanical Stratum-B tail is now exhausted** — remaining items
  (ED-PC-0005 reconciliation, ED-SC-0011 contest dispatch, C-TW-3/4/6/8, armature echo-wiring) need a
  ruling or a large build; surfaced for Jordan, not forced.
- **Resolution Plan v1 — Stratum-B SECOND SLICE 2026-07-08: knots.py ED-912 rebuild (C-TW-12
  CLOSED).** `sim/personal/knots.py` rebuilt onto the bidirectional −5..+5 gauge (TIER_RANGE/
  TIER_START; rupture +5; −5 Tempered Close-only absorb-once; break/betrayal Disposition −3;
  positive-strain Close-break Scar) matching the doc side; pinned test
  `sim/tests/test_knots_ed912.py` (7 cases; knots had zero coverage). Closes ED-FI-0003's sim
  residual; ED-WR-0005 still carries C-TW-3 + C-TW-4/6/8/10/11. F7/seed-0 goldens unmoved (island).
- **Resolution Plan v1 — Stratum-B oracle-to-canon FIRST SLICE 2026-07-08.** The ruled, low-risk
  sim truth-alignment deferred from Stratum A (resolution_plan_v1.md §9). **ED-871 CLOSED
  end-to-end** — `systems/threadwork/sim/operations.py` `attempt_mending` cost −1 → 0 + Mending exempted from
  the blanket Partial/Failure penalty (all degrees net 0), with a pinned test
  `sim/tests/test_thread_mending_ed871.py` (threadwork had zero coverage). **CI-75 dead constant**
  `CI_PHASE_TRANSITION=75` removed from `sim/peninsular/ci_track.py` (CI75-9, under the
  already-resolved ED-IN-0025). F7 + seed-0 goldens unmoved (island/dead-code). ED-WR-0005 stays
  open (progress-noted): C-TW-3 (Leap), C-TW-4/6/8/10/11, knots.py C-TW-12 remain.
- **Resolution Plan v1 — PR-2 F7 smoke oracle LANDED 2026-07-08 (ED-IN-0021 → resolved).**
  `sim/tests/test_f7_smoke_oracle.py`: the "born guarded" campaign regression the U-4 lesson
  demanded (no balance claim without an oracle + n≥100). Pins the n=8/seed-42 golden (Varfell
  87.5% — the historical small-n artifact, labelled NOT balance), named zero-assertions
  (scenes_resolved / insurgencies_formed / npcs_generated = 0 — the islands; designed to TRIP when
  the transport waves land), the Hafenmark elimination-lockout (ED-FA-0005), the VICTORY_THRESHOLD
  dead-param regression (C-EMERGE-8), and a wall-time ceiling. Added minimal additive telemetry
  (`game_state.World.scenes_resolved` + 3 `CampaignResult` fields; no behaviour change, seed-0
  golden unmoved). Runs in CI via "Sim Reference Regression" (pytest sim/tests). Landed **ahead of**
  the armature echo wiring (baseline-first); the wiring is PR-2's remainder. See resolution_plan_v1.md §8.
- **Resolution Plan v1 — Stratum-A truth-reconciliation FIRST PASS EXECUTED 2026-07-07 (this branch,
  `claude/fable5-audit-resolution-plan-r6kzsa`).** Executes the doc/registry/ledger core of Stratum A;
  `designs/audit/2026-07-07-unaddressed-areas-audit/resolution_plan_v1.md` §7 has the full
  finding→fix execution log. EDs flipped `resolved`: ED-FI-0003 (OPT-6 knots ED-912 propagation),
  ED-IN-0022 (OPT-7 registry hygiene), ED-IN-0023 (OPT-8 consumer closure), ED-IN-0024 (OPT-14
  addenda), ED-IN-0025 (OPT-17 C-VERIFY notes), ED-SE-0004 (OPT-16 anti-orphaning), ED-PC-0004
  (OPT-15 ED-1042 flips + the **ED-PC-0005** residual re-file). Kept `open` with a progress note:
  ED-FA-0004 (OPT-1 — `[PRE-LPS-1/PORT-BLOCKING]` banners placed, LPS-1 sim impl = Stratum B),
  ED-WR-0005 (OPT-5 — ED-871 doc side done, sim + C-TW-3.. = Stratum B). Also executed the U-6
  CI-75→CI-100 supersession + fork-2 ARC-T04 strike (doc side), and DISAMBIGUATED the half-done
  ED-IN-0012/0013→0019/0020 renumber (U-11 — the ratification appended the new rows but never re-id'd
  the old edge-playability rows; now `status: superseded` + `renumbered_to`, physical row-dedup left
  to Jordan). **Deferred (loud):** all behavior-changing sim edits (`operations.py`, `ci_track.py`,
  `knots.py`, dead `pool_penalty`) = Stratum B; genuine needs-Jordan calls (anchoring cadence cap,
  CI75-1 seizure trigger, CI75-11 GD-1 checklist, knots §6.2 Coherence-loss) flagged in place, not
  decided. New id: **ED-PC-0005** (id_reservations PC next_free 5→6).
- **Unaddressed-areas comprehensive audit — DELIVERED 2026-07-07 (ED-IN-0017, this PR;
  deliverable 1 of 2).** 14 evidence clusters (incl. Jordan-directed pessimist NERS + pessimist
  resolver reviews) + 4 gap-closure agents + 5 independent refuters; every cluster's Honest-gaps
  section dispositioned per Jordan's directive. Deliverables at
  `designs/audit/2026-07-07-unaddressed-areas-audit/` — verdict-first report, finding_status,
  `ed_options.md` (17 candidates, **deliberately UNFILED — Jordan picks**; OPT-1/2/4/10/14 and
  the armature §5 docket are needs_jordan), and **`resolution_plan_v1.md`** — the comprehensive
  bottom-up + top-down resolution program (armature-FIRST sequencing override per Jordan;
  contract deployment + enforcement ladder; v40 re-authoring license operationalized; ecosystem
  tooling bindings; full finding→fix→lane→stratum→gate table). Headlines: the faction oracle implements the
  pre-LPS-1 superseded model; threadwork is a total island; live contests resolve through the
  deprecated raw-dice stub; the ~87% win-share is a small-n artifact riding an elimination
  lockout (n=100: 56/36/7/1); the Turmoil victory gate is permanently vacuous; ED-871/fork-2/
  ED-912/fork-11 rulings only partially executed; conviction_track_v30 still runs the superseded
  CI-75 model (unpropagated supersession, refuter-upgraded).
- **Key & Echo Armature v1 — DELIVERED 2026-07-07 (ED-IN-0018, this PR; deliverable 2 of 2,
  needs_jordan = its §5 fork docket).** `designs/architecture/key_echo_armature_v1.md` (seam
  contracts + Echo Matrix all-directions/all-scales + §3 registry deltas + A13-A16 conformance
  specs + the consolidated §5 docket — **merge does NOT ratify §5**) + the first executable Key
  substrate (`sim/substrate/keys.py`, 24 tests) + `tests/contracts` wired into CI. Staging:
  PR-2 = flag-gated echo wiring + the F7 smoke oracle; PR-3+ = per-lane shaping waves (armature
  §6.3). The §5 docket consolidates: OF-D6/OF-3/OF-7/OF-B1/RNG-COLLISION/ORD-3/ORD-4/OF-CAP,
  ED-SC-0002, ED-SE-0002, the ED-IN-0012/0013 double-allocation renumber (ledger lines 597-600),
  CI 75-vs-80, ER-2 band-discipline scope, contest live-dispatch.

- **Unaddressed-areas audit + Key & Echo Armature — RATIFIED 2026-07-07 (Jordan: "Perform
  consolidated ruling pass? I want to ratify all and get to work on this" — ED-IN-0026, same
  branch/PR, before merge).** Rules the armature's full §5 fork docket (16 rows — see
  `key_echo_armature_v1.md` §5 Ruling Log) and files all 17 `ed_options.md` candidates as EDs
  (`ED-FA-0004/0005`, `ED-IN-0019/0020/0021/0022/0023/0024/0025`, `ED-WR-0004/0005/0006`,
  `ED-FI-0003`, `ED-SE-0003/0004`, `ED-PC-0003/0004`, `ED-SC-0011`, `ED-MB-0004`; see
  `ed_options.md`'s Disposition table for the design-call ruling baked into each). Headlines:
  OF-7/OF-B1 ADOPTED — `sim/substrate/keys.py`'s `TickScheduler` now defaults both flags ON
  (propagation_spec_v1.md and key_substrate_v30.md amended to record the ratification; 25/25
  substrate tests + full 120-pass `tests/valoria` suite re-verified, no regressions); the
  ED-IN-0012/0013 double-allocation (§5.10) EXECUTED via the `ED-IN-0019`/`ED-IN-0020` renumber;
  the ER-2/Overwhelming band-discipline fork (§5.12, the one genuine no-default fork besides the
  renumber) ruled toward the symmetric-unification direction, execution deferred to `ED-PC-0003`;
  the A15 process extension (§5.16) landed in `key_type_registry_v30.md` §10, which also picked
  up a header CANONICAL/PROVISIONAL split correction found while editing the same file.
  `ED-SC-0002`/`ED-SE-0002` (§5.8/5.9) deliberately left unruled — pre-existing SC/SE-lane forks,
  out of this IN-lane pass's scope per CLAUDE.md §4's session-lane-scoping convention. Citation
  integrity + currency checks re-verified clean (`validate_ed_citations.py` 0 violations,
  `currency_consistency_check.py` clean, adjudicator baseline unchanged at 21/65).
- **Edge-playability audit — RATIFIED IN FULL 2026-07-05 (Jordan: "Ratify all", post-merge
  instruction on PR #81; merged as #81, ratification batch on the restarted branch).** Seam-level
  complement to PR #77: ~60 edges, 8 sonnet clusters, Fable-verified V1–V22. Deliverables at
  `designs/audit/2026-07-05-edge-playability-audit/` (all statuses now RATIFIED): report
  (verdict "the seams are the old GM's chair, still empty"; EP-1..EP-11 P1s, ep-12..ep-31 P2/P3
  register, SIG-1..4), grounding, dossiers + verification log. **All 10 §7 remediation items
  FILED 2026-07-05:** `ED-IN-0012` registry×rendering sweep · `ED-IN-0013` GM-token sweep of the
  handoffs (**renumbered 2026-07-07 to `ED-IN-0019`/`ED-IN-0020` respectively — armature §5.10,
  see the ratification entry below; `ED-IN-0012`/`ED-IN-0013` now mean the SC-audit batch content
  only**) · `ED-IN-0014` key the silent emitters (settlement/ci_political/era) · `ED-IN-0015`
  seam-feedback authoring convention · `ED-IN-0016` index the joints (CURRENT.md rows +
  faction_politics doc:null flip) · `ED-SE-0002` Accord/Order stacking ruling (**needs_jordan**:
  the ruling itself) · `ED-FA-0002` strategic-turn surface / domain_actions home doc ·
  `ED-FA-0003` BG victory-params re-export · `ED-FI-0002` counter-espionage loop · `ED-WR-0003`
  ambient-fabric window + Appraise Revelation (ED map also in the report §7 addendum;
  id_reservations bumped; SE/FA/FI/WR handoffs cross-referenced). P2/P3 register items without a
  §7 ED are ratified-as-findings, drawable for future allocations against the report. The five
  IN items execute in this lane; workplan-v6 sequencing applies.

- **Qualitative NERS audit (North-Star) — DELIVERED 2026-07-04, awaiting Jordan review (PR #77,
  branch `claude/ners-audit-fable5-9cpfdz`).** Corpus-wide qualitative audit (playability /
  cohesiveness / interdependencies / emergent narrative / threadwork-at-every-juncture), 55-agent
  adversarial workflow (12 dossiers + 5 degenerate-play hunters + 7 lenses; every carried finding
  refuted-or-confirmed with an intent gate). Deliverables at
  `designs/audit/2026-07-04-ners-qualitative-audit/`: `ners_qualitative_audit_v1.md`
  (verdict-first, throughlines-tree organized; 5 confirmed findings F-1..F-5 + 2 corpus signals
  S-1 register back-propagation blindness / S-2 steering-surface fragmentation),
  `strategic_judgments.md` (J-1..J-15: playable-season milestone, Gate-0-before-more-combat-depth,
  transport-seam closure, collision-engine detector, anti-drift + roadmap governance),
  `ed_options.md` (E-1..E-12 drafted candidates, **deliberately NOT filed** — Jordan picks and
  allocates per id_reservations protocol; merging PR #77 ratifies nothing). Follow-ups if adopted:
  E-2/E-3/E-7 are the recommended first three; GAP-1 = investigation lane never audited (E-12);
  32 deferred-unverified P2 candidates in `01_workings/deferred_unverified.json`.
- **Qualitative NERS audit (North-Star) — RATIFIED-AS-ACCEPTED 2026-07-05 (Jordan post-merge
  instruction on PR #77).** Corpus-wide qualitative audit (playability / cohesiveness /
  interdependencies / emergent narrative / threadwork-at-every-juncture), 55-agent adversarial
  workflow. Deliverables at `designs/audit/2026-07-04-ners-qualitative-audit/` (all statuses now
  RATIFIED): audit v1 (5 confirmed findings F-1..F-5 + corpus signals S-1/S-2),
  `strategic_judgments.md` (J-1..J-15), `ed_options.md`. **All 12 ED options FILED 2026-07-05**
  (forks resolved to audit defaults — E-1 adopt governance redesign; E-4 per-subsystem
  walkthrough policy; E-8 MS wins MS/RS): `ED-SE-0001`, `ED-IN-0003..0008`, `ED-WR-0001/0002`,
  `ED-PC-0001`, `ED-SC-0001`, `ED-FI-0001` (map in ed_options.md addendum; id_reservations
  bumped). ED-IN-0003 (convergence detector) + ED-IN-0004 (articulation triggers) are acceptance
  criteria of the **2026-07-05 emergent-narrative-engine design effort (IN FLIGHT, this branch)**
  — see `designs/audit/2026-07-05-emergent-narrative-engine/` once landed. Remaining filed items
  execute in their own lanes.

- **Emergent Narrative Engine design v1 — DELIVERED 2026-07-05, awaiting Jordan review (PR #78).**
  25-agent design workflow (4 dossiers → 3 architects → 3 judges + synthesis → 5 refuters → 5
  spec sections → 3 capstone verifiers → critic) + full remediation. Result: **the Arc-Vector
  Engine with a Subordinate Director** (B won all judge lenses; six layers,
  detect-then-schedule-then-render), closing ED-IN-0003 (L2 convergence detector) + ED-IN-0004
  (L5 render completion incl. the four ED-681 thread beats, worked) by construction. Deliverables
  at `designs/audit/2026-07-05-emergent-narrative-engine/`: `narrative_engine_design_v1.md`
  (head doc: architecture, staging, determinism, 9 open forks), `integration_with_ners_audit.md`
  (crosswalk), `00_grounding/` (charter with Jordan's four key considerations + C1–C7),
  `01_workings/spec_sections/s1..s5` (normative chapters incl. the ARC-S07 capstone trace,
  factionless mini-trace, effect-bearing COLLISION-B trace). **9 [OPEN — Jordan] forks — esp.
  fork 8 HELD BACK (director tension-curve subtract-only reverses charter language; not
  self-ratified by merge)**; forks 1–2 (Coup-Counter remap; ARC-T04 strike-or-author) block
  Stage 1. Corpus defects surfaced for follow-up: Coup Counter STRUCK but live in 6 register
  entries; ARC-T04 dangling; Torben Loyalty range register-vs-clock_registry conflict.

- **Narrative engine v2 "THE CHURN ENGINE" + Master Workplan v6 + steering reconciliation —
  RATIFIED IN FULL 2026-07-05 (Jordan: "Ratify commit merge all"; ED-IN-0009/ED-IN-0011;
  PR #78 merged). All stated fork defaults adopted incl. F-F/fork-8; fork 10's faction
  count = ED-FA-0001 (open, needs_jordan). Originally delivered as:** v2
  (`narrative_engine_design_v2_churn.md` + `spec/churn_amendments.md`, supersedes-in-part v1)
  reorganizes the engine around Jordan's churn critique: generator-not-corpus (templates ×
  binding, 138 register arcs = validation set), two-layer forecast (Layer A analytic — the M1
  ship, hard gate; Layer B seeded ensemble behind named preconditions incl. F7/F8), **the
  Light Function** (pruning-as-authorship; invariants i–iv; forecast severed from casting and
  actor-invisible per the adversarial pass), claim-grammar interface (a requirements input
  ADDING four SC sub-systems — shapes the SC lane's), load factorization (no runtime LLM;
  bake headline ~1,200–2,700 units under fork-6 default), kernel/data/wrapper modularity
  (nothing hard-baked; R-F1/R-F2/R-HB/R-CL/R-AI/R-RL). Five-refuter pass
  (`01_workings/refute_v2_*.md`) fully applied; survivors = forks 10–11 + fixture F8. **⚠️
  F-F/fork-8 (the Light-Function weight set + subtract-only discipline) is HELD BACK from
  merge-ratification — needs explicit Jordan sign-off.** Grounded by two dossiers
  (`01_workings/dossier_forecast_tractability.md`, `dossier_combinatorial_census.md`).
  **Workplan v6** (`workplans/valoria_master_workplan_v6.md`, ED-IN-0009): M1/M2/M3
  milestones, IN spine, per-lane sequencing, tiered T0/T1/T2 decision register (no status
  fields), governance incl. the ED-PC plan-text-label rule. **ED-IN-0006 EXECUTED**:
  roadmap_state → `deprecated/references/` (banner), v5 → `deprecated/archives/workplans/` (banner
  fixing its J-38 contradiction), decision-queue items 1–3 refreshed + queue demoted to
  dated snapshot, CURRENT.md rows updated (workplan v6 + new Narrative-engine row),
  `lane_assignments.yaml` repointed. Next IN actions live in v6 §2. **⚠️ F-F/fork-8 note
  below is superseded by the ratification above.**

- **Ecosystem-review Top-5 residuals not covered by their own lane.** Filed 2026-06-30 as
  ED-1050..1054 (full report: `designs/audit/2026-06-30-ecosystem-adversarial-review.md`).
  ED-1050 (combat parity oracle) lives in `registers/handoffs/HANDOFF_PC.md` (RESOLVED, one residual
  left). This lane owns the rest:
  - **ED-1051 — module-contract gaps, `needs_jordan`.** `references/module_contracts.yaml`
    has 11/27 modules `doc:null` (grew from the originally-filed 10/27) and 13/27 resolvers at
    `[ASSUMPTION]` grade (grew from 11/27) — re-measured 2026-07-02, docket adjudication
    ED-IN-0002. `engine_clock` (the temporal spine, highest-priority module) now has a
    CANDIDATE home doc — `designs/architecture/propagation_spec_v1.md` (ED-1093, CANONICAL) —
    its `gap_notes` explicitly keep `doc:null` unflipped until this entry is ruled. Authoring
    is effectively done for `engine_clock`; only ratification/ordering remains for it, plus the
    other ~10 modules and 13 resolvers untouched. Also tracked at `decision_queue.md` item 12.
  - **ED-1052 — typed engine-params layer for Godot ingestion, still open.** No scope/fence
    decision made. A narrower path was found and executed (2026-07-01): `tools/export_engine_params.py`
    serializes the LIVE `combat_engine_v1/config.py` Class-C oracle directly to
    `engine/engine_params/combat_engine_v1.json` (blocking CI round-trip check),
    sidestepping the settled-vs-in-flux dilemma without deciding the broader
    `params/*.md`-prose-parsing question (its own docstring is explicit it does NOT parse
    prose). A prior attempt (PR #37) asserting a Combat Pool formula as authoritative was
    REVERTED — that's the trap to avoid: type only what's genuinely settled, or mirror the
    live oracle mechanically. Also tracked at `decision_queue.md` items 17 and 24.
  - **ED-1054 — navigation surface, partially done, narrowed 2026-07-02 (ED-IN-0002); re-verified
    2026-07-29 (Wave 4 mechanical sweep, OI-57).** Retired-session-file relocation to
    `deprecated/` is DONE (via ED-1084). Re-checked against the current working tree: (a) the
    ~850KB of narrative markdown mislabeled as tests (`tests/emergent_arc_skeleton_test_2026-04-17_batch*.md`,
    `tests/sim_framework/session_audit_2026-04-19.md`) is **still unrelocated, and its cited
    target is now stale** — `designs/audit/` no longer exists (retired to `audit/` per
    CLAUDE.md §1/§3, ED-IN-0071 P4/P5); the live target would be `audit/` or
    `deprecated/archives/`. This half stays genuinely OPEN, target corrected. (b) The other two
    targets are MOOT, not done: `sim/README.md`/`sim/CONVENTIONS.md` no longer exist — `sim/`
    was retired wholesale 2026-07-21 (CLAUDE.md §3's `sim/` row), superseded by
    `engine/sim_reference_README.md`/`engine/sim_reference_CONVENTIONS.md`, so there is nothing
    left to regenerate under the old paths. `tools/README.md`'s four previously-missing entries
    (`currency_consistency_check.py`, `ci_module_shape_check.py`, `export_engine_params.py`,
    `validate_ed_citations.py`) are now all PRESENT (verified by grep 2026-07-29) — that sub-item
    is CLOSED. Net: ED-1054 is 3/4 closed-or-moot; only the narrative-md relocation (a) remains,
    with a corrected target. Also tracked at `decision_queue.md` item 25.
  - **ED-1053 RESOLVED 2026-06-30** (see Decisions below).

## Decisions

- 2026-07-12 — **Skills-ecosystem staleness remediation, "Phase 7" (ED-IN-0044..0042) — continues
  the 2026-07-11 audit-ecosystem batch (ED-IN-0032..0037) this file's Pending/Decisions log never
  got an entry for; note that gap here rather than backfilling the missing history.** Jordan asked
  for a cohesive update of all skills plus a gap scan. A 3-agent parallel audit of all 15 live
  skills against CLAUDE.md's current architecture found: three skills independently pointed P1/P2
  findings at the FROZEN flat `registers/editorial_ledger.jsonl` instead of the live lane-split files
  (`valoria-mechanic-audit`, `valoria-module-adjudicator`, `valoria-resolution-diagnostic` —
  ED-IN-0044); `valoria-compiler` had four independent breaks including a nonexistent gate field
  and an orphaned `compilation/` output path (ED-IN-0044); and `valoria-combat-simulator`'s
  bundled script was a fully superseded parallel implementation (a frozen 9-weapon 2026-03-31
  model vs. the live 51-weapon `combat_engine_v1/workbench/balance.py`), retired to
  `deprecated/skills/` after Jordan confirmed via AskUserQuestion (ED-IN-0045). Also, per Jordan's
  explicit confirmation: `valoria-dice-model` gained the canonical continuous (Godot-mode)
  resolver alongside the legacy discrete one, validated against the existing Monte Carlo
  implementation (ED-IN-0040). Closed one cheap ecosystem gap: PP-NNN allocation had no
  documented protocol despite `id_reservations.yaml` already reserving PP blocks the same way as
  ED — added to `valoria-editorial-register` (ED-IN-0041). Deferred gaps (Godot port-readiness
  tracking, session lane-scoping enforcement, `compliance_check.py` local-hook integration, missing
  sim↔port parity tooling) filed as `ED-IN-0042`, `needs_jordan: true` — see
  `designs/audit/2026-07-12-skills-ecosystem-audit/skills_ecosystem_audit_v1.md` for full detail
  and the per-gap suggested shape.
- 2026-07-09 — **Follow-on token-efficiency pass: dead GitHub-API tools retired, observability
  register re-capped, two stale size warnings resolved.** Jordan: "What other steps can we take to
  increase token efficiency... How often are we calling in from GitHub needlessly instead of just
  looking at local cloned repo?" then "All please, but carefully." A subagent traced every
  GitHub-API code path in the repo first: **zero live-invoked tools touch the GitHub API** — the
  ED-1053 migration to working-tree reads is complete for every gate CI/hooks actually run. What
  remained was dead code that only *looked* live, independently re-verified (grep for each
  filename across every workflow/hook/skill/Python import) before touching anything:
  - **Retired to `deprecated/tools/` / `deprecated/engine/`** (mirroring the existing
    `valoria-orchestrator` → `deprecated/skills/` precedent, not hard-deleted):
    `extract_values.py`, `extract_proper_nouns.py`, `valoria_collator.py`, `valoria_bulk_fix.py`,
    `file_lookup.py`, `compliance_dryrun.py`, `engine/engine_audit_harness.py`. Also
    `skills/prose-writer/scripts/consistency_check.py` (the GitHub-API-only naming-gate predecessor
    `tools/ci_naming_check.py` itself documents as superseded) → `deprecated/skills/prose-writer/scripts/`.
    Fixed the two `references/ci_checks_registry.yaml` rows that asserted a live pairing to two of
    these (`abbreviation_registry_gate` → `valoria_collator.py`, `forbidden_token_gate` →
    `consistency_check.py`) — both pairings were already stale/never wired, confirmed by grep.
    **`tools/canon_coverage_check.py` deliberately left in place** — GitHub-API-based and unwired
    too, but its own registry entry says `ci_job: ""  # not yet wired — Jordan to decide`, a
    pending-decision status, not confirmed-dead legacy.
  - **Dead single function removed in-place** (file itself is live): `fetch_full()` in
    `skills/valoria-vector-audit/scripts/vector_audit.py` — a GitHub Contents API helper with zero
    callers, vestigial from before the read-path rewrite (LB-22). Removed with its now-unused
    `urllib.request`/`base64`/`json` imports; file still compiles.
  - **`tools/observability/DECISIONS.md` re-capped**: was 59,085 tokens (4x its 15k
    `atomization_rules.yaml` cap) purely from `build_decisions.py`'s `PER_CAT_CAP=60` truncation
    setting being too generous — nothing reads the .md for completeness (console.html and any
    programmatic consumer read the uncapped `decisions.json`, unchanged). Dropped `PER_CAT_CAP` to
    12 and regenerated; file is now ~6.3k tokens. (Regeneration also re-swept the current corpus,
    surfacing the counts have drifted since the file's one prior commit — expected, not a bug.)
  - **Two other standing `compliance_check` size warnings resolved**, not by pruning content but by
    fixing the governance that was wrong: `references/module_contracts.yaml` (~14.4k tokens) was
    hitting the generic 10k `**/*.yaml` catch-all with no policy ever written for it despite being a
    genuinely comprehensive, actively machine-checked 27-module registry (CLAUDE.md §6 already notes
    it's expected to grow, not shrink) — raised its explicit cap to 18k, `warn_only`, same treatment
    as `canonical_sources.yaml`/`mechanical_terms_index.md`. The attribute/value coherence audit's
    `02_census/quantity_census.yaml` (~18.5k tokens) is a self-declared frozen evidence artifact
    ("QUARANTINE-NOTE: not a registry, not canonical truth") hitting the same catch-all with nothing
    to act on — given `on_exceed: skip`, scoped to that one file (not a blanket `designs/audit/`
    exemption). `compliance_check.py --check-only --repo-state .` now reports 0 warnings, 0 errors
    (previously 3 standing warnings).
  - Model-tiering gap noted but **not code-fixed**: of three persisted Workflow scripts in
    `.claude/` (git-tracked, each a provenance record of one already-executed audit —
    `wf_attribute_coherence.js`, `wf_combat_critique.js`, `wf_social_contest_critique.js`), only the
    first shows real haiku/sonnet/opus/fable tiering per CLAUDE.md §10; the other two have almost no
    `model:` overrides. These are historical run records, not reusable named workflows (no
    `.claude/workflows/` dir exists) — editing them now wouldn't change any past cost and would
    misrepresent what actually ran, so left as-is. The actionable form of this finding is: apply
    §10 tiering when *authoring* the next heavy audit/critique workflow, not a retrofit here.
  - Verified: `compliance_check.py --check-only --repo-state .` (0/0), `ci_register_size_check.py`,
    `ci_hooks_verifier.py` (dead-tool `/home/claude` warnings dropped from 6 files to the expected
    remainder), `ci_naming_check.py`, `currency_consistency_check.py`, `validate_ed_citations.py`
    (0 violations), `broken_dependency_checker.py` (clean), full `tests/valoria` suite — all green.
- 2026-07-08 — **Second HANDOFF atomization pass + editorial-ledger lane split.** Jordan: "Make it
  so that handoffs are by lane, not just a giant document. Break up handoffs and editorial register
  for that reason because they should be atomized for better management." Two changes:
  (1) root `HANDOFF.md`'s "## Next actions" section still carried ~9k tokens of lane-owned bullets
  (mass battle, PC, IN, SC) despite the 2026-07-02 lane split below — every one was cross-checked
  against its lane file first (most were already duplicated there verbatim) and dropped rather than
  re-copied; the two genuine gaps found (R2 capstone finding, J-36) were backfilled into
  `HANDOFF_PC.md`/`HANDOFF_IN.md` before trimming root. Root is now ~95 lines / ~1.6k tokens, only
  cross-lane content. (2) `registers/editorial_ledger.jsonl` (404 live entries, ~150k tokens, previously
  ungoverned by lane) split the same way: the 115 entries whose id already declares a lane
  (`ED-<LANE>-NNNN`) moved to their own `registers/editorial_ledger_<lane>.jsonl`; the 289 pre-cutover
  flat-ID entries stayed put (no retrofit, same precedent as the ID-namespace cutover itself). Main
  ledger dropped from ~150k tokens (at its own cap) to ~90k. Updated
  `tools/validate_ed_citations.py` (reads main + all lane files as "active") and
  `tools/broken_dependency_checker.py`'s `check_editorial_ledger` (same — the lane-tagged third of
  live entries would otherwise silently stop being checked for broken paths, the exact failure class
  ED-1081 already fixed once) and `tools/ci_register_size_check.py` (per-lane caps). Verified:
  `validate_ed_citations.py` 0 violations, `broken_dependency_checker.py` clean,
  `ci_register_size_check.py`/`compliance_check.py --check-only` clean, `currency_consistency_check.py`
  clean, full `tests/valoria` suite green.
- 2026-07-07 — **Consolidated ruling pass on the Key & Echo armature §5 docket + ed_options.md
  (ED-IN-0026).** Jordan: "Perform consolidated ruling pass? I want to ratify all and get to work
  on this" — exercising, before merge, the ratification authority PR #85's body had deliberately
  held back. Per-row disposition lives in `key_echo_armature_v1.md` §5's Ruling Log (16 rows) and
  `ed_options.md`'s Disposition table (17 filed EDs). Two rows were genuine no-default forks
  needing an actual pick: the ED-IN-0012/0013 renumber (executed) and the ER-2/Overwhelming
  band-discipline direction (ruled, execution deferred). Two rows (ED-SC-0002, ED-SE-0002) were
  explicitly left to their owning lanes rather than ruled from this IN-lane pass. See the Pending
  entry above for the full headline list.
- 2026-07-02 — **HANDOFF.md split into per-lane files, matching the `ED-<LANE>-NNNN`
  nomenclature.** Jordan: "Handoffs need to have the same tagging nomenclature. There are
  different handoffs for different lanes." Root `HANDOFF.md` is now a thin index + genuinely
  cross-cutting "Next actions" pointer; each lane (`MB, PC, FI, SC, FA, WR, IN, GO, SE`) gets
  its own `registers/handoffs/HANDOFF_<LANE>.md` carrying that lane's Pending/Decisions/Next-actions.
  Motivation is the same one behind the `ED-<LANE>-NNNN` split itself: reduce concurrent-session
  merge-collision surface on shared continuity files. Note this partially reverses an EARLIER,
  deliberate consolidation (`deprecated/session_machinery/` retired per-topic session-log files
  in favor of one `HANDOFF.md`, because fragmented files rotted/went stale) — the difference
  this time is the fragmentation is keyed to the SAME lane taxonomy the ID system already
  enforces, not an ad-hoc per-topic split, and `tools/session_status.py`'s SessionStart banner
  still reads one root file so there's still a single "start here" surface, just a thinner one.
  `tools/session_status.py` unchanged (still greps root `HANDOFF.md`'s one `## Next` heading).
- 2026-07-02 — **`ED-<LANE>-NNNN` lane-tagged editorial namespace created (`ED-IN-0001`, PR #67,
  merged); D1-D5 adjudication docket reconciled (`ED-IN-0002`, PR #69, merged).** PR #58 hit two
  same-session concurrent-allocation collisions on the flat `ED-NNNN` sequence within one PR
  (`ED-1088`→`1090`; then `1089`/`1090`→`1093`/`1094` — see `ED-1094`'s own entry). Jordan: new
  EDs use `ED-<LANE>-NNNN` (9 lanes: `MB` mass battle, `PC` personal combat, `FI` field
  investigation, `SC` social contest, `FA` faction actions, `WR` world, `IN` infrastructure,
  `GO` godot, `SE` settlements — `SC`/`PC` deliberately disambiguated after a first draft
  proposed `SC` for both; a proposed `PY` python lane was dropped as not a real subsystem). Flat
  `ED-NNNN` is FROZEN at `ED-1094`, permanently valid, never retrofitted.
  `references/id_reservations.yaml` gained per-lane `next_free` counters;
  `tools/validate_ed_citations.py` and `tools/currency_consistency_check.py` extended to
  recognize both formats; `CLAUDE.md` §3 documents the format plus a new, not-yet-CI-enforced
  session-lane-scoping convention. Separately, Jordan pasted an uncommitted local adjudication
  docket (D1-D5, drawn from the 2026-06-30 ecosystem review's `needs_jordan` subset) for
  relevance-checking against the current tree; verdicts folded into the ED-1050/1051/1052/1054
  entries above (this file) and `registers/handoffs/HANDOFF_PC.md`.
- 2026-07-02 — **Merge-ratifies-by-default convention adopted (ED-1094); ED-1083 doctrine
  ratified; J-38 propagation spec ratified (ED-1093).** Jordan: merging a PR ratifies its
  PROPOSED/provisional contents by default unless the PR body explicitly holds an item back
  for separate review — closes a real recurring gap where PR #55 was reviewed and merged but
  `holonic_container_doctrine_v1.md` (ED-1083) sat PROPOSED in `main` afterward because the
  prior convention required a distinct explicit ratification step nothing forced to happen.
  Applied same-day: ED-1083 flipped provisional → ratified; doctrine `## Status:` line
  PROPOSED → **CANONICAL**; `CURRENT.md` gained an Architecture/Holonic-doctrine row;
  `decision_queue.md` item 20 struck resolved; `CLAUDE.md` §2 documents the standing rule.
  **Applied a second time to J-38 itself, same PR (#58):** rather than land the propagation
  spec as PROPOSED and rely on "ratifies on merge" text (which would repeat the exact ED-1083
  failure mode this convention exists to close), the flip to CANONICAL was pre-staged in the
  PR — `designs/architecture/propagation_spec_v1.md` `## Status:` line PROPOSED → **CANONICAL**,
  ED-1093 ledger entry `status` → `ratified`, `decision_queue.md` item 18 struck resolved. A
  whole-session Fable review (triggered after the ED-1088 ID-collision reconciliation) caught
  this risk plus stale cross-references before merge. Scope: governs future PRs; does not
  retroactively reopen closed decisions or ratify anything a PR explicitly holds back and flags
  loudly as such.
- 2026-07-01 — **Month-overview + architecture-consolidation session executed** (12+ commits,
  ED-1081..1087; overview + execution/reconciliation logs + the frozen 23-item Jordan decision
  queue at `designs/audit/2026-07-01-month-overview-architecture-consolidation/`). Landed:
  LB-21 round-3 ID re-block · two silently-dead enforcement pieces revived
  (`broken_dependency_checker` ledger check; non-executable tracked pre-commit hook) · CLAUDE.md
  §6 falsified claims corrected (ED-1050/ED-1054 states) · holonic container doctrine v1
  **PROPOSED** (`designs/architecture/holonic_container_doctrine_v1.md`, ED-1083 — Jordan-vetoable)
  from the ingested 2026-07-01 workflow spec · Combat Pool collapsed to `max(5, History+6)` across
  every live stale site (ED-1084) · `values_master.yaml` QUARANTINED · names_index v2 (proper-noun
  fold; mirror 23→83) · session-log machinery → `deprecated/session_machinery/` · combat engine
  runtime **numpy-free** (σ-kernel via `sim.autoload.sigma_leverage`; state kernel engine-owned;
  ED-1085) with new container-hygiene guard · **first typed Godot params artifact**
  (`engine/engine_params/combat_engine_v1.json`, blocking round-trip CI; ED-1052 seed) ·
  contract-conformance CI (report-only; ED-1051 backlog surfaced per-PR) · CLAUDE.md §10 fable
  tier + relay patterns; workplan **J-38** (propagation-spec authorship) docketed ·
  `currency_consistency_check` self-updating recency gate (CI + SessionStart banner; ED-1087) ·
  freshness pins refreshed + gate flipped **blocking** (LB-23 residual closed). Three scope
  defaults adopted Jordan-vetoable (values_master quarantine-not-regenerate; Godot seed included;
  freshness flip). Rulings made: **none** — everything gated sits in the decision queue.
- 2026-06-30 — **ED-1053 resolved: working-tree integrity port + sim oracle.** Ported the three
  "integrity" gates off the GitHub API to the working tree (no PAT/network): `broken_dependency_checker`
  and `patch_propagation_checker` now `os.walk`/read locally (both green against the checkout);
  `freshness_gate` computes git blob SHAs locally (verified identical to `git hash-object`) and checks
  119/131 `canonical_sha__` pins (12 stale → report-only). Dropped `GITHUB_PAT` from the CI integrity job.
  Hardened `ci_sim_fabrication_check`: full float-literal capture + `(variable,value)` matching close the
  value-collision / float-split holes (corpus blast kept to +~200 latent, changeset-scoped; `tools/`
  excluded from sim-classification). Added the first `sim/` test — `sim/tests/test_mc_v18_regression.py`
  (deterministic seeded `run_batch(n=2,seed=0)`: determinism + golden + bounded smoke) — and a new
  'Sim Reference Regression' CI job wired into All-Gates-Green. Updated CLAUDE.md §8.
- 2026-06-30 — **Adversarial ecosystem review + safe fixes.** Ran a 72-agent verification workflow
  (6 audit dimensions × 2 skeptical lenses); 24 findings survived, headline items hand-spot-checked.
  Rewrote `CLAUDE.md` into a Claude-Code-optimized operating manual (numbered sections, currency
  priority, data→Godot pipeline, port state, known-defect callouts). Filed the report under
  `designs/audit/` and the Top-5 as ED-1050..1054. **Re-blocked IDs** (`references/id_reservations.yaml`
  v2: round-1 A/B/C exhausted+overrun to ED-1042; round-2 block D = ED 1050-1099 / PP 800-829, next_free
  ED-1081, after contest_rebuild reserved 1055-1079 + combat at 1080). **Safe code/doc fixes applied:** single-sourced the patch-register size cap
  (`ci_register_size_check.py` 20k→policy 15k; register is ~5k); RETIRED banners on
  `references/subsystems/{handoff,checkpoint,session_log}_subsystem.md`; flipped
  `canon/session_checkpoint.md` `status: active`→`retired`; STALE banners on the four `godot/*.md`
  specs; rewrote `README.md` to defer to CLAUDE/CURRENT/HANDOFF. **Not done (needs Jordan / re-sweep):**
  the parity-oracle balance values (ED-1050) and the Gate-0/contracts authoring (ED-1051).
- 2026-06-29 — **ED-citation integrity: full reconciliation (292 → 0; gate now BLOCKING).** Diagnosed the
  292 report-only violations: 286 `NONEXISTENT` from **dual ledger-of-record drift** (design docs minted ED
  numbers in inline `[EDITORIAL:]` tables never migrated to the JSONL), 6 `OPEN_AS_BASIS` (2 of them validator
  false positives). Fixed 3 validator defects (`tools/validate_ed_citations.py`): active-ledger precedence
  over stale archives, loud-parse + regex-salvage of 7 malformed archive YAMLs, and same-line basis scoping
  (table-row bleed). **Registered 91 grounded entries** (36 resolved / 12 provisional / 30 open / 13
  needs_jordan) — each verified against its citing doc by per-batch subagents (anti-fabrication). Repointed
  the ED-814→ED-907 phantom and reworded open/provisional over-claims to `pending`. Dropped `continue-on-error`
  on the `ed-citations` CI job + added to `ci-summary` needs. Report:
  `designs/audit/2026-06-28-ed-citation-triage/02_reconciliation.md`. **Residual for Jordan:** 13 needs_jordan
  items (NPC naming ED-634/595–602/610, ED-885 ratification ID); ID collisions ED-408–411/413/417/647.
- 2026-06-28 — **Editorial-ledger relevance triage.** Deep per-item verification of all **93 unresolved**
  entries (82 open + 10 provisional + 1 deferred) against the live working tree, in 6 read-only cluster
  passes. Result: **37 still relevant** (25 real open work + 12 NEEDS_JORDAN), **56 stale**. Applied via
  Workflow D: **31 struck** (21 superseded by later canon — esp. the mass-battle per-cell/Lanchester
  re-architecture + the 2026-06-22 `net-(Ob-0.5)` continuity fix; 10 `[PROPOSED:…]` migration residue),
  **25 resolved** (open-but-done — decision had landed, row never closed). Unresolved queue 93→37.
  ED-citation violations dropped 315→292 as a side effect. Report:
  `designs/audit/2026-06-28-editorial-relevance-triage/relevance_triage.md`. **Residual for Jordan:** 12
  NEEDS_JORDAN items (NPC naming ED-649/650/651, deferrals ED-644/788, design-intent gates
  ED-879/893/911/920/924/1033/1036); three of these (644/649/893) are the OPEN_AS_BASIS citations still
  holding the ED-citation validator report-only.
- 2026-06-28 — **Open-session unification + LB-22 closed.** Reviewed every `origin` session branch;
  six were already squash-merged into main (#14–#21), one (`claude/github-ci-environment-review` = PR #18)
  carried genuinely-unmerged work, and `claude/refresh-state-3m7nL` (abandoned 04-20 pre-migration line
  carrying the retired `session_checkpoint`/`session_log` harness) was excluded from the merge. Unified
  PR #18's **net-new** half (the LB-22 backlog) onto main — its already-landed half (12 skills +
  coverage_matrix, via #16) was kept at main's version, no re-litigation. **LB-22 done:** `valoria-orchestrator`
  retired to `deprecated/skills/`; `valoria-vector-audit` read-path rewritten; `ci_hooks_verifier.py`
  Check 4 flipped to **blocking for `skills/`** (`tools/` stays WARN pending the API→disk port). PR #18
  closed as superseded. `ci_register_size_check.py` taken from #18 (importable, no-PyYAML, ships the
  drift-guard test) with #22's `names_index.yaml` threshold line re-added; `lane_assignments.yaml`
  owns-globs repointed to `deprecated/`.
- 2026-06-28 — **Master Workplan v5** authored (`designs/audit/2026-06-28-recent-work-orchestration/`),
  reconciling the post-v4 work (06-12→06-28) into one register and superseding v4. Roadmap +
  lane_assignments repointed to v5. Ledger verified live: **713** entries / 0 duplicate IDs / ED 1042.
  (v5 de-staled this pass to live HEAD; PRs #16–#22 reconciled — see its §0/§10.)
- 2026-06-24 — Migrated the Claude↔GitHub automation to a Claude Code-native model:
  retired the `/home/claude` GraphQL/cache/session harness; gates now live once in `tools/`
  and run in CI (authoritative) + local hooks/`.githooks` (advisory). See the migration PR.
- 2026-07-01 — **Workplan sprawl cleanup.** `workplans/` was dead (both files pre-dated v3/v4)
  while the live master workplan kept spawning in a fresh one-off `designs/audit/<date>-*/` folder each
  revision, so `CURRENT.md` had to manually chase it. Relocated v5 into `workplans/` (now the
  one live home — see its `README.md`); archived the two dead files to `deprecated/archives/workplans/`. Repointed
  `CURRENT.md`, `references/lane_assignments.yaml`, `references/roadmap_state.yaml`, and v5's own §0
  commit-path note. Frozen historical versions (v4 in `designs/audit/2026-06-11-orchestration/`, v3 in
  `2026-06-10-master-workplan-v3/`) were left in place intentionally — they're bundled with sibling
  audit artifacts and CURRENT.md already documents them as frozen records, not lost ones. Separately,
  flagged (not moved) the `sim/` vs `tests/sim/` vs `tests/sim_framework/` naming collision — three
  distinct-purpose directories, not duplicates; disambiguated via README notes in each rather than a
  path rename, since `tests/sim/` is path-matched by `ci_sim_fabrication_check.py`/`atomization_rules.yaml`/
  `lane_assignments.yaml` and a rename would need to update all three.

## Next actions

- **[OPEN — BLOCKED ON JORDAN] Canonical nomenclature plan written (2026-08-11).**
  `proposals/canonical_nomenclature_v1.md` — plan only, **no ED allocated, nothing renamed, nothing
  ratified**. It executes the "Dotted-namespace nomenclature" item held under ED-IN-0152 below,
  now with the axis question answered by Jordan's own worked examples (`npc.almud_almqvist`,
  `settlement.piety_track`, `world.invasion_pressure`).
  - **The headline is that this is an ADOPTION problem, not a rename problem.** The dotted
    namespace already exists in `names_index.yaml` (113 keys). Measured: of the 51 non-proper-noun
    keys, **16 appear nowhere outside the generated registries, 32 only in tooling/tests, and 3 in
    engine code or a design doc** — and one of those three (`substrate.key`) is most of the real
    adoption. So the scope is "plug in a layer nobody wired", not "rewrite 10k references".
  - **Three namespace axes are live and mutually contradictory**: kind (`clock.ip`, `set.legitimacy`
    — `names_index`), event-domain (`scene.*`/`state.*` — the 56 Key types), owner/scale (Jordan's
    examples). Recommendation: **owner/scale governs entities + owned state, event-domain is kept
    unchanged for Keys, kind is retired.** Keys are the control group that proves the thesis
    (median 24 hits vs contract names' median 131) — §0.1 point 5 says do not sweep what works.
  - **Four rulings are Jordan's and the plan deliberately does not pre-empt them:** (a) `piety_track`'s
    owner — Jordan's example says `settlement.`, `module_contracts.yaml:253` files it under
    `characters`, and `conviction_track_v30.md:31` calls it per-**territory**; the three disagree
    independently of this proposal; (b) whether Key types take a `key.` prefix (recommend: no);
    (c) contract names — full rename vs citation-form-only (recommend: citation-form only);
    (d) freeing `world.` from its 62 proper nouns so `world.invasion_pressure` can exist.
  - ⚠ **BLOCKER FOUND WHILE PLANNING, not yet fixed — `tools/valoria_rename.py` covers almost
    nothing.** Its `SCOPE_DIRS = ('designs', 'params', 'references', 'canon')`: `designs/` was
    retired 2026-07-19 (ED-IN-0071 P4/P5) and `params/` evacuated 2026-08-05 (ED-IN-0145), so two
    of its four roots no longer exist — and `iter_files()` does `if not os.path.isdir(d): continue`,
    so they vanish with **no error and no warning**. `systems/`/`engine/` were never added and
    `.py`/`.json` are not in `EXTS`. Measured coverage: **67 files in scope, 270 live design-corpus
    files missed, 261 `.py` missed, 41 `.json` missed.** The repo's designated "change once"
    executor would silently rewrite a fraction of the corpus and report success. Same defect class
    as the gates-reporting-clean-over-nothing trio (ED-IN-0147/0148) and the `build_glossary`
    silent-coverage defects (ED-IN-0150): a reader quietly covering a fraction of its source, correct
    when written, broken by a tree move. **Fix + guard is a Phase-1 prerequisite; no phase can be
    trusted until a test fails on an absent configured root.**

- **[OPEN] ED-IN-0152 — subsystem flow skeletons exist for all 15 `systems/` folders (2026-08-10).**
  `systems/<x>/<x>_flow_skeleton_v1.md`, format + roster single-owned by
  `systems/_architecture/subsystem_flow_skeletons_v1.md`, guarded by
  `tests/valoria/test_flow_skeletons.py`. Structure only — entry points, ordered flow, IN/OUT,
  state, seams, traced gaps — built from **code**, not design prose. **Ratifies nothing:** no head
  moved, no status flipped, no contract edited.
  - **What they are for next.** The Godot port's conversion unit is one module contract
    (`godot/godot_conversion_strategy_v1.md` Part IV.3) and its ritual wants a flatten artifact per
    module; the 2026-06 flatten artifacts are scattered and stale. These are that category of
    object, rebuilt uniformly and guarded against rot.
  - **The gaps are the finding, and they are observations, not proposals.** Each subsystem's §7
    carries evidenced absences (declared-but-unimplemented, stubbed, unreachable, default-off, or
    code↔contract divergence). Several are corroborated by lanes that never saw each other — the
    `world.clocks['Turmoil']` victory gate was found independently by the `victory` and `overview`
    traces. **None of them is dispositioned here.** Deciding which are defects and which are
    deliberate deferrals is per-lane design work, not IN's call.
  - **Known guard blind spot, stated not implied:** the anchor check catches wrong file, wrong
    function, wrong symbol and out-of-function drift, but NOT line drift *within* the named
    definition. Measured, not assumed — see the test docstring.
  - **[HELD FOR JORDAN — NOT ratified by merging this PR] Dotted-namespace nomenclature for
    canonical identifiers.** Jordan raised it in-session: every canonical name should carry a
    greppable prefix — `contract.victory`, `settlement.`, `npc.`, `scores.` — so a region can be
    found by searching for it instead of re-derived by heuristics. **The evidence is now measured**
    rather than asserted, in `references/ENGINE_ATLAS.md` §5 (generated, so it stays current):
    - **Key types already satisfy the rule by construction** — dotted and distinctive, median
      **24** occurrences corpus-wide. Nothing to change.
    - **Contract names do not** — median **131**, worst `audit` at **2,162**, `mass_battle` 2,085,
      `social_contest` 1,953, `victory` 1,911. They are ordinary English words, so a search returns
      prose and unrelated identifiers. **Zero** qualified (`contract:<name>`) uses exist anywhere.
    - The repo already has the convention in embryo: `_identifier_census.yaml` uses `key:` / `py:`
      prefixes, and `stubwire.stub_resolve(module, symbol, reason)` is the same idea — a
      machine-findable declaration with structured payload, which is why stub sites are the one
      gap class that never needs re-discovering.
    **Why this is held and not done:** a rename touches 27 contract names across ~10k references
    and every generated artifact that joins on them. A cheaper variant preserves the names and
    mandates only the *citation form* (`contract.victory` when referring to the contract in prose
    or comments) — additive, nothing renames, and the atlas already measures adoption. Choosing
    between full rename and citation-form-only is a Jordan call; **nothing here implements either**.
  - **SECOND PASS RUN 2026-08-10 — independent re-derivation, method-disjoint from the first.**
    The skeletons were built by grep-driven code tracing. To test whether that method's blind
    spots were *the artifact's* blind spots, a second pass re-derived the same subjects under an
    inverted constraint: **no grep, no pattern matching, files read whole**, agents forbidden from
    opening the skeletons, sourced from the declarative surfaces (`module_contracts.yaml`,
    `mechanics_index.yaml`, `canonical_sources.yaml`, `CURRENT.md`) and the 2026-08-06 corpus
    vector audit's structural graph, then diffed.
    - **Result: ~168 claims independently rediscovered; 4 contradictions; 3 outright errors in the
      shipped files, all corrected.** The errors were: threadwork §7 asserting state was "not
      schema-migrated" when the migration landed 2026-05-19 (and contradicting its own §2);
      settlements' `Contracts:` header listing Python modules rather than contract names; and
      factions labelling the govern branch a "fallback" when it is unconditional.
    - **Two of the second pass's own claims were WRONG and must not be re-propagated:**
      `sigma_leverage`/`dice_engine` are NOT dead — they are imported by combat, social_contest
      and five faction modules; the agent that called them orphans had a scope that excluded
      combat. And overview IS present in the execution trace
      (`by_contract["loop.s3"]["peninsular_strain"]`); the agent read `by_subsystem_path` only.
      Recorded here because a plausible-sounding dead-module claim is exactly the kind of thing
      that gets copied forward.
    - **Method note worth keeping:** the two passes agreed on nearly everything *reachability*-
      related and disagreed mainly where a claim rested on a **registry** rather than on code.
      Grep tracing is strong on "what calls what" and weak on "what was declared and never
      built"; reading the contracts whole is the opposite. Neither alone is sufficient.
  - **FILED, not swept (§0.1 point 5).** Standing rule 5 was applied to *comparison thresholds*
    (gate predicates) across the corpus. **Effect magnitudes** — Coherence/MS deltas, ±Ob
    adjustments, deck sizes — were left in place. They are constants by the spec's own preamble
    and arguably in scope, but sweeping them touches all 15 files for marginal gain and would
    widen a task that was load-bearing only on the gates. One deliberate inconsistency, recorded
    rather than hidden.
  - Follow-up available if wanted: fold the §7 gap rows into a single cross-subsystem register so
    the absences can be ranked in one place instead of fifteen. Not done — it is a judgment surface
    and would need a lane owner.

- **THE CONTRACT + KEY INDEXES ARE READABLE NOW (2026-08-10, ED-IN-0151). Jordan review pending.**
  `references/KEY_INDEX.md` (55 key types by family) and `references/CONTRACT_INDEX.md` (27 modules,
  IN → resolver → OUT + owned state, gates, derivations, loops) are generated by
  `tools/build_contract_index.py` from `key_graph.json` + `module_contracts.yaml` +
  `wiring_manifest.yaml`, with the A1–A12 verdicts **imported** from `contract_adjudicator.py`.
  Both open with a review queue. Freshness, link integrity and coverage are pinned by
  `tests/valoria/test_contract_index.py` (mutation-verified, 3/3).
  - **The backlog is much smaller than its row count.** 41 of the 42 under-declared key edges are
    one missing declaration — `articulation_layer` as a consumer — and the adjudicator's 20 A6
    violations span 9 module pairs. Genuinely open: 1 key nobody produces (`meta.legacy_event`),
    8 nobody consumes, **0 contradictions**, 8 modules with neither doc nor code.
  - **Four decisions are Jordan's, and the indexes deliberately do not pre-empt them:** (a) is
    `articulation_layer` a declared consumer of ~41 key types or a substrate observer the contracts
    should not enumerate; (b) do `player_input` / `echo_transport` / `all subscribing systems`
    become modules or stay unresolved prose; (c) which of the 8 consumerless keys are legitimately
    terminal; (d) the 9 missing scale-transition declarations.
  - `build_key_graph.py` now emits `family` per key (schema_version 1 → 2, additive) — parsed in the
    sole registry parser, because the dotted prefix is not the family (`scene.*` spans two).
  - **Independently re-derived (same session), and every figure reproduced exactly.** A second
    parser sharing no code with the generator — registry walked line-by-line with string methods
    instead of regex, contracts re-reconciled from `yaml.safe_load`, A6/A8 recomputed from the rule
    as authored, rendered docs re-checked by character-scanning rather than the committed test's
    regex — returned identical figures throughout (55 types + identical family filing, 27 modules,
    1/8/0, 42 edges split 41 `articulation_layer` + 1 `player_input`, 20 A6 across the same 9 pairs,
    2 A8, 491 anchor links resolving, 55/55 + 27/27 coverage). The authority tally is the one number
    where a naive independent count is *expected* to differ, and the difference was predicted before
    running: 13 declared-and-existing sim modules + the 1 `mass_battle` declared-absent exception =
    14 code / 5 prose / 8 none.
  - ⚠ **NEW, unrelated to the above and NOT fixed here — needs a call.** `key_type_registry_v30.md`
    §1 declares `type_id: <family.subtype>` as the first field of every entry; **0 of 55 entries
    carry it**, the `###` heading holds the identity instead. The generator is right to key off the
    heading, but §1 documents a field absent from the corpus it governs, so a validator written to
    §1 matches nothing. Left alone deliberately: that file is Class A canonical and the fix (correct
    §1, or add the field to 55 entries) is a ruling, not a cleanup.

- **THE FORK IS BUILT AND RUNS (2026-08-03, ED-IN-0123, PR #286). Start here.**
  `python3 tools/build_fork.py --out <dir>` assembles it and **runs a seeded campaign inside it
  with the source repo off `sys.path`** — self-containment is a subprocess exit code, not a claim.
  Current: **206 .py · 225 .md · zero path escapes · every contract unit carried · RUNS**
  (`{"winner":"Crown","keys":6,"hash":"c2da4723","battles":1}`).
  - **Structure comes from the module graph, not a hand-drawn line.** `runtime` = the transitive
    closure from `engine.mc_v18`: **58 of 206 files**. The rest is `subsystem_unwired` 69,
    `canon_unwired` 28, `oracle` 25, `test` 15, `workbench` 11 — written to `FORK_MANIFEST.json`.
  - **The unwired 69 are the backlog**, joined to contracts so they read as one: `personal_combat`
    15 (`build=unwired`), `social_contest` 14 (`gated`), `threadwork` 1, `miraculous_event` 1
    (`stub`). 36 have **no contract pointer** — that gap is mechanical to close.
  - **Two guards, both mutation-verified.** Contract coverage (drop `systems/` from CARRY → 27
    contracted/stub units reported left behind) and the escape scan.
  - **It deliberately does NOT decide the mass-battle tree.** Both are carried; canon lives at
    `systems/mass_battle/canon/`. Blocked on `degree` — **exact shapes in
    `audit/2026-08-03-session-oddities.md` §H**, which corrects the summary written here first: the
    `{winner,turns,phases}` return is the `kind='single'` path, but the caller uses `kind='multi'`,
    which returns `{winner, battle_turns, log, a_loss_final, b_loss_final}`. Three of the caller's
    four fields map mechanically; **`degree` does not exist in canon at all** — the live engine
    synthesises it from a hardcoded ladder with an uncited `0.50`. Porting means *authoring* that
    rule, which is a design ruling, not an adapter.

- **⚠ READ `audit/2026-08-03-session-oddities.md` BEFORE RESUMING.** Extended 2026-08-03 into the
  session-independent record of what is actually known: sections A–H and P are **measured** (each
  carries the command that produced it), **section J is 13 open questions** — each with what would
  answer it and whether it is blocked on Jordan or on measurement — and K records what was left
  undone on purpose. Three things there that change how you'd plan:
  - **§G — the three registries disagree.** `module_contracts` (keys + code pointer),
    `wiring_manifest` (build state) and a real execution trace do not describe the same 27 modules.
    Four modules marked `deferred` are **observed executing**, including `faction_state` at 498
    calls, whose pointer is the boot spine. Only **2 of 27** are `live`. `victory` is one of the
    two, runs 384 calls, and declares **zero keys in and zero out**.
  - **§E5 corrects three of my own rows.** E3/E4/B4 cite `FORK_MANIFEST.json`, which
    `build_fork.py` writes *into its output tree*. The fork was never committed, so those counts
    have **no artifact in this repo** and fail this record's own standard. **J12 is the 5-minute
    fix** and is the cheapest open item on the list.
  - **§J9 is the most promising unexplored thread in the MB lane.** If the rout fires too early
    (D1, which Jordan ruled a real defect), that alone would explain several of the nine red tests
    — `conditional_orders`, `dg2_yield_residuals`, `stochastic_rout` all need the battle to last
    long enough for a trigger to fire. Nobody has checked whether one fix greens all nine (J8).

- **RESOLVED 2026-08-04 (ED-IN-0125) — the direction is INVERTED. `main` is the go-forward repo.**
  ~~UNRESOLVED, and it decides the fork's mechanics: does `main` keep moving after the fork?~~
  The question was posed under the EXTRACT framing, where "the fork" meant a new **code** repo built
  by copying `CARRY` into an empty tree. Jordan ruled the opposite operation: **the fork/archive holds
  the outdated largely-prose work; THIS repo stays as the code-first go-forward repo.** So the
  one-way-build objection below is dissolved rather than answered — nothing is ever rebuilt from
  `main` into the archive, so `rmtree` cannot clobber anything, and no history-preserving extraction
  is needed at all. `git-filter-repo`, `git subtree split`, and the 11-roots/2-relocations path-rewrite
  cost all drop out of the plan. The archive is this repo's history at an evacuation tag; a browsable
  archive repo is a convenience, not a requirement.
  ⚠ **J1 is registered REINTERPRETED, not verbatim** (ED-IN-0125): its literal wording — "`main` does
  NOT keep moving after the fork" — would, read under the new framing, freeze the go-forward repo. The
  thing that freezes is the **archive**; `main` continues.
  ⚠ **`build_fork.py`'s `CARRY`/`LEAVE` must NOT simply be run backwards.** `CARRY ∪ LEAVE` does not
  partition the tree, and the neither-set (`.github/`, `.githooks/`, `.claude/`, `tools/`,
  `tests/valoria/`, most of `references/`, `research/`, `skills/`, `CLAUDE.md`, `CURRENT.md`,
  `HANDOFF.md`) defaults to *kept* under extract and *deleted* under evacuate. `LEAVE` also carries two
  extraction-only rationales — `tools/` "the fork re-derives what it needs" and `tests/valoria/`
  "engine/tests comes instead" — which under keep-main would delete the enforcement tier, the shipping
  gate, and the fork plan's own falsifiers. **The keep-set is authored fresh; see
  `systems/_architecture/repository_keep_set_v1.md`.**

- **I1 (get `main` green) is CANON-BLOCKED, measured not assumed.** 60/60 identical 1200v1200
  battles end in ONE turn; the winner takes ZERO losses in 42/60. That is why
  `own_strength_fires_when_attrited` cannot fire — the subunit never reaches 90%. Jordan ruled
  2026-08-03 that this is **not** correct behaviour, so F1 is a real engine defect — but fixing it
  is MB-lane engine work, and the retrospective's Phase 0 forbids re-pinning thresholds first
  ("re-basing before fixing F1–F8 would bake nine defects into the definition of correct").
  Two corrections to the bisect's causal story are recorded in the plan §6.4: the flag toggle works
  by shifting the RNG stream (across 40 seeds: A zeroed 20, B zeroed 19 — no side bias), and
  `b_pool: 0` is the RESULT of routing, not the cause.

- **Filed, not acted on:** `tests/sim/mass_battle/config.py` ships `PC_CELL_MORALE` default `'1'`
  under a comment reading "RETRACTED to OFF 2026-07-25". Git settles it — `584c683a` set `'0'`,
  `94bb9022` (PR #271) flipped it to `'1'` and left the comment. **Do not fix it from an IN-lane
  PR**: touching anything under `tests/sim/` trips `ci_co_file_checker` rule 3, which demands a
  `coverage_matrix.md` update for a comment edit. That gate fires on the CANON engine's own source
  because the engine is misfiled under `tests/` — re-homing it is fork assembly, not a gate fix.

- **W0/W1 of the fork plan are DONE (2026-08-03, ED-IN-0123). W2 is Jordan's, so the next
  unblocked engineering is the W1 residue + W3.** State, measured not asserted:
  - **Path-literal escapes out of `engine/`+`systems/`: 10 → 6, and 0 runtime.** The one runtime
    escape was `engine/autoload/registry.py` (read `registers/mechanics_index.yaml` from inside
    the autoload hub, zero callers) — deleted. The remaining 6 are `test_pipeline_reach.py`
    (reaches `skills/`, `audit/` — it tests repo bookkeeping and belongs in `tests/valoria`, not
    the engine suite) and 4 in `combat_engine_v1/workbench/`. **That is the next W0 cleanup.**
  - **The parity oracles are now a committed table** (`engine/tests/goldens/sigma_leverage_parity.json`,
    1,758 rows, generated by `tools/gen_sigma_parity_goldens.py`). 761 → 1,926 executing
    assertions, zero skips, numpy dependency gone.
  - **`save_replay_premise` is `partial`, not closed**, and the two open items are named in the
    manifest: `mass_seizure.py:292` never fired on the measured seed (untested, not proven
    clean — **find a seed that exercises it**), and `Faction.L`'s evidence is thin because values
    saturate to the 0.5/7.0 clamps, leaving 1 of 4 factions informative. **A clamped rebuild
    agrees with a clamped actual regardless of the deltas** — any future L-reconstruction claim
    must report off-boundary count or it is not a measurement.
  - **W0's `combat_engine_v1` packaging item was STRUCK, not done.** Measured: flat `sys.path`
    import works and coverage reports 17 files at 75%. The plan had inferred an importability
    defect from a campaign-scoped zero-rows observation, which is a WIRING fact belonging to W3.
  - **Two traps for the next session, both of which cost me a wrong answer here.** (1) An AST scan
    for attribute assignments cannot see `Faction.adjust()`, which writes via
    `setattr(self, stat, val)` — 31 call sites route through it and the grep found zero. (2)
    `run_campaign(max_seasons=N)` is shadowed by `effective_params['CAMPAIGN_SEASONS']`, so a
    season sweep passing `max_seasons` varies nothing; pass it in `params`.
  - **A green suite is not evidence unless you check it reaches the path.**
    `test_parliamentary_bridge` pins the Key log on seed 42, and seed 42 fires the new emitter
    zero times — recorded as `test_the_pinned_golden_seed_cannot_see_this_path` so it stops
    reading as coverage.

- **⚠ `build_decisions.LANE_PATH_PREFIXES` should be a DERIVATION, not a 133-row table
  (2026-08-01, found by the gate crawl; rot repaired, design NOT fixed).**
  Measured: **60 of 136 rows matched no tracked file** — 35 named `designs/audit/…` (retired
  2026-07-19) and the rest `designs/…`/`sim/…` paths moved by the same restructure. Lane
  attribution had been silently degrading for weeks, because `infer_lane`
  (`build_decisions.py:264`, re-exported as the single owner at `obs_core.py:35`) returns `None`
  when nothing matches, and an honest `None` is indistinguishable from "this file genuinely has
  no lane" — `None` is *deliberately* also the correct answer for cross-lane files, so rot and
  correct abstention cannot be told apart by construction. **Blast radius is wider than
  `DECISIONS.md`:** `build_proposals.py`, `build_incompleteness.py` (where `None` becomes the
  literal `"unassigned"`), `build_graph.py` and `session_open_work.py` all consume it. Repaired to 0 dead rows and pinned by
  `test_lane_path_prefixes_all_match_something` (mutation-verified).
  - **The repair is not the fix.** CLAUDE.md §3's RULED §2a already states *one subsystem = one
    folder = one ID lane*. That makes lane **derivable** from `systems/<subsystem>/` — about nine
    rows — instead of enumerated across 133. Hand-enumerating what a rule derives is a §8
    single-owner violation, and it is why the table rots on every tree move.
  - **It also enumerates individual audit directories**, which is the same defect one level worse:
    wiring in a general tool that names one specific dated audit folder. Those rows exist because
    an audit's lane was not otherwise recoverable; under §2a it is, from the subsystem the audit
    concerns.
  - **Watch the collision when doing this:** `references/lane_assignments.yaml` is the OLD A/B/C
    write-concurrency lanes, and its own header warns it is "a DIFFERENT, OLDER concept" from the
    9-lane `ED-<LANE>` namespace. `build_decisions.py` reads that file AND hand-maintains the
    9-lane table. Whoever consolidates must not merge the two concepts.

- **⚠ `references/id_reservations.yaml` is at 14,263 / 15,000 tokens — 737 of headroom, on the file
  EVERY lane must edit to allocate an ED (2026-08-01, ED-MB-0063 residual).** Roughly two
  allocations from a BLOCKING `register-size-check` failure that would stop every lane at once.
  Surfaced by the new approaching-cap WARN in `ci_register_size_check.py`, which found it on its
  first run; nothing was reporting it before.
  - **The cost is concentrated, not diffuse.** Line 226 is a single comment of **10,738 chars
    (~2,685 tokens — 18% of the whole file's cap)** recording the provenance of the ED-IN-0064
    DUP-KEY repair, a defect that is already neutralized. Lines 225/236/195/197 add ~3.1k, 3.1k,
    2.5k and 2.5k chars of lane-comment prose. Line 111 (the MB lane) is 4,126 chars.
  - **DO NOT simply delete line 226.** Checked before recommending it: the `ED-IN-0064` ledger entry
    is about the **governance research corpus**, an entirely different item — the dup-key repair's
    prose exists ONLY in that comment. Cutting it destroys provenance rather than relocating it.
    It needs a home first (a companion archive doc, or a purpose-filed ledger entry), then the cut.
  - **The MB lane line (111) is the easy one and is already sanctioned.** Jordan ruled the PC lane
    to "SKELETON ONLY … ONE SHORT LINE per ED. Prose lives in `registers/editorial_ledger_pc.jsonl`"
    (2026-07-24, CLAUDE.md §4). MB never got that treatment and its prose *is* already duplicated
    in `editorial_ledger_mb.jsonl`, so condensing it is a pure de-duplication with an existing
    ruling behind it.
  - **Deliberately NOT executed in the session that found it** (§0.1 #5 — sweep only what the task
    is load-bearing on, and file the rest): this is a 2,685-token provenance relocation on the
    highest-contention file in the repo, done at the end of a long session, with the concurrent-
    allocation collision history that created the lane namespace in the first place. It wants its
    own scoped PR, not a tail-end sweep.

- **WS0 Structural Observatory + WS1 registry reader (2026-07-13/14, ED-IN-0057..0063)** — the five
  Tier-0 audit scripts (`skills/valoria-vector-audit/scripts/{vector,structure,pointer,formula,gen}_audit.py`)
  and the read-only facade `tools/registry.py` (+ `references/registry/README.md` &
  `pointer_debt_worklist.md`, both **PROPOSED**) are built, merged (PRs #132/#135/#137), and
  hardened by two adversarial passes (a partial Fable-5 audit + a 5-critic holistic pass,
  `designs/audit/2026-07-14-holistic-unification/`). **Open, Jordan-gated decisions surfaced there:**
  (1) **`ED-IN-0059` pointer-debt worklist Category B** (register the genuinely-unregistered scalars —
  Wounds/Turmoil/Accord/etc., each needs a canonical key + home-doc verification) and **Category C2**
  (whether npc_behavior's `beliefs`/`concerns`/`projects`/`arc state` are registry quantities at all);
  (2) whether the observatory gets a **non-gating CI refresh job** that persists scorecards (it is
  runnable now but wired nowhere — `audit-refresh.yml` deliberately does not run it); (3) `settlement_layer`
  derivation `Legitimacy / Popular Support` (module_contracts.yaml) is a Mandate-feedback drift loop with
  **no `bucket:` tag** — is it a `derived_value` or a track-write? These are the concrete "needs_jordan"
  items a resuming session must not silently skip.

- **Governance Type Registry (2026-07-13)** — `designs/architecture/governance_type_registry_v1.md`
  inventories every governance/politics/hierarchy/faction/geography type across the corpus (4 parallel
  survey passes + this session's generation-methodology work), classified FLAG vs. VECTOR, cross-scale
  throughlines named (§3), 5 same-name/different-scale naming collisions surfaced unresolved (§2.8),
  and a grounded (not ratified) proposal for a `Field`/`Gauge` substrate primitive extending
  `key_echo_armature_v1.md` to cover continuous VECTOR state — closing the OF-3 `decay()` fork
  (deferred 2026-07-07, `key_echo_armature_v1.md §5.2`) generically instead of per-track. **Read this
  before authoring any new cross-scale accumulation/propagation/decay mechanic** — it names two
  working templates (MS's hysteresis+falloff, Π's homeostat clamp) to generalize from rather than
  re-deriving. OF-3's `decay()` fork itself is still Jordan's to rule.

_(Reserved-ID state healthy as of 2026-07-02: LB-21 executed, then the `ED-<LANE>-NNNN` cutover
(ED-IN-0001) froze the flat sequence at `ED-1094`. `references/id_reservations.yaml`'s `lane_ids`
section is now the live allocation source for all NEW EDs — read `next_free` for your lane,
allocate, bump, co-commit; never max+1.)_

- **START HERE — month-overview + consolidation (2026-07-01), doctrine + propagation spec now
  RATIFIED (2026-07-02).** The month's comprehensive review, the consolidation
  execution/reconciliation logs, and the **single consolidated 23+2-item Jordan decision queue**
  live at `designs/audit/2026-07-01-month-overview-architecture-consolidation/` (see
  `decision_queue.md` first — every gated item below is indexed there). **Doctrine ratification**
  (ED-1083, `designs/architecture/holonic_container_doctrine_v1.md`) and **J-38 propagation-spec
  authorship** (ED-1093, `designs/architecture/propagation_spec_v1.md` — supplies `engine_clock`'s
  candidate home doc; the `doc:null`/[ASSUMPTION] grade stays unflipped until ED-1051 is
  separately resolved) are both **CANONICAL** as of PR #58 (ED-1094 merge-ratifies-by-default).
  The propagation spec's own §5 carries its ranked open items (OF-7/OF-B1 amendments, D.6/OF-D6
  double-count, `decay()` spec, RNG-MODEL-COLLISION, cap constants, ORD-3/ORD-4) — ratification
  did not resolve these, only fixed the spec's home-doc status. Remaining highest-leverage queued
  decisions: the values_master regenerate-vs-retire call, the duplicate compilation homes, and
  item 19 (Agent-Teams/subagent-roster adoption).
- **Done this pass:** unified PR #18's net-new into main → **LB-22 complete** (orchestrator retired to
  `deprecated/skills/`; `valoria-vector-audit` read-path rewritten; `ci_hooks_verifier` Check 4 blocking
  for `skills/`). Earlier passes already landed the coverage_matrix single-source + 12-skill boilerplate
  strip (#16) — kept at main's version during the unify.
- **LB-22 residual (small):** `tools/` analysis utilities still carry `/home/claude` refs (WARN tier in
  `ci_hooks_verifier`); flip the `tools/` scope to blocking only after the GitHub-API→working-tree port
  (`freshness_gate`, `broken_dependency_checker`, `compliance_check`, `extract_*`, `valoria_collator`,
  `valoria_bulk_fix`). `valoria-orchestrator`'s old `tests/registry/test_descriptor_registry.py` import
  is dead (reads `/home/claude/…`, not CI-collected) — left as-is.
- **CI debt blocking-flips (LB-23) — reconciled 2026-07-01 (ED-1082):** `validate_ed_citations`
  is **already blocking** (since 2026-06-29, 0 genuine violations — the old "flip once triaged"
  action here was stale). `freshness_gate`'s remaining report-only step is being closed by the
  month-overview consolidation itself (pin refresh + blocking flip as its final commit); the
  optional K-2 SHA-split (115 `canonical_sha` fields → `references/canonical_freshness.yaml`)
  is a refactor that can follow independently, no longer a precondition.
- **`ci_political_v30` read-routing (LB-24):** raw file ~26k but tracked read returns 0
  (index-routes). Tooling/routing bug, not a faction-content decision — cross-referenced in
  `registers/handoffs/HANDOFF_FA.md` since the file itself is faction/political content.
- **Ledger-status reconciliation (LA-23, Lane A — mostly done):** flipped ED-841/842/912 `open`→`resolved`
  and filed the never-written ED-938/ED-939 (backfilled from #13; artifacts verified). Dropped the
  report-only `validate_ed_citations` count 748→731. **Residual:** ED-914 left `open` — its mechanical
  parts remain (PP-719 record-or-strike; dead `fieldwork_design_v1` parent-path refs in `params/bg/core.md`,
  `designs/scene/fieldwork_v30.md`, `designs/scene/fieldwork_godot.md` — cross-referenced in
  `registers/handoffs/HANDOFF_FI.md`).
- **The new `ED-<LANE>-NNNN` namespace's own residual (from ED-IN-0001's PR body):** the
  session-lane-scoping convention (`CLAUDE.md` §3) is documented but not yet CI-enforced —
  detecting which lane a PR's file changes belong to and flagging mismatches is real follow-up
  work, not built yet.
- **J-36 — Key-bus closure for the 6 off-bus writers**, gated on the distillation report's deferred
  adversarial pass. Design-tier docket item awaiting Jordan; see also `registers/handoffs/HANDOFF_SC.md`'s J-31
  (social-contest deliberative-game findings) — the two were tracked together in root `HANDOFF.md`
  before the 2026-07-08 per-lane content split.

- **Observatory Remediation Program filed (2026-07-14, ED-IN-0066 — renumbered off the #139 ED-IN-0065
  collision, PROPOSED)** — `designs/audit/2026-07-14-gameplay-subsystem-observatory/remediation_plan_v1.md`:
  the resolve-everything plan over ED-IN-0064's findings, **incorporating PR #139** (its landed observatory
  integrity fixes; its needs_jordan items as D15/D16; the G_pointer keyed-rate 21.8% baseline; the
  head_pointers.yaml + REPO_MAP.md action in P2). **Next action: Jordan rules the Phase-1 decision docket
  (D1–D16)**; P0 (instrument hardening, net of #139: the G_code __init__ HIGH, banner_classify tie-break,
  contract↔code join, direction_audit.py) can start in parallel, IN lane. Program structure ratifies on
  merge; every D-row stays needs_jordan.

- **Incompleteness Ledger + audit de-cull (2026-07-22, PR #205)** — the vectorization apparatus'
  core purpose is to **SURFACE WHAT IS MISSING**; it had been silently culling (a 16-system
  `SKIP_SYSTEMS` denylist + four length/threshold floors) to stay "signal-heavy" — the exact
  opposite. Fixed: (1) every cull is now a *surfaced, reasoned exclusion*
  (`vector_audit.audit_exclusions()`); (2) new `tools/observability/build_incompleteness.py` —
  the absorb-everything **Incompleteness Ledger** (`INCOMPLETENESS.md` / `incompleteness.json` /
  `_data.js`) scanning the whole tree for every stub/null/missing/excluded/unverified thing,
  surfaced as the dashboard's **Missing** face; (3) doctrine enshrined in
  `skills/valoria-vector-audit/SKILL.md` (⛔ SURFACE, NEVER CULL) so it survives context loss.
  **Next action (pending Jordan design call):** Stage F — wire the 7 island modules + 11 doc:null
  contracts. BLOCKED honestly: the design docs don't speak in the Key vocabulary, so any IN/OUT
  edge is *inference*, not extraction. Do NOT fabricate contract edges into the source of truth;
  author them grounded (e.g. re-point the 3 stale `designs/` doc paths first: `victory`,
  `clock_registry`/overview, `territorial_piety`→`conviction_track`) and mark any inferred edge
  `[ASSUMPTION]`, held back loudly per CLAUDE.md §2. `engine_clock` (ED-1051) + `domain_actions`
  (ED-FA-0002) need canon before their edges are real.

- **"Extend audit in all directions" — trace-completeness pass (2026-07-22, PR #205, in flight).**
  Working most→least impactful with an **adversarial pass at the end of each direction**:
  - **Dir #1 (DONE)** — `discover_unregistered_candidates`: name-level ontology match over the
    whole design corpus (folding + expanded stopwords; critic caught a substring-unsound first cut
    at ~50% noise → rebuilt to 39 high-signal). Feeds the ledger's `unregistered_term` face.
  - **Dir #2 (DONE + reconciled)** — the two observatories now TALK: `vector_audit --emit-findings`
    writes `tools/observability/audit_findings.json` (its UNIQUE cross-graph Mode-B implied-missing +
    Mode-H isolates), the Incompleteness Ledger surfaces them. TWO adversarial passes. Final state
    (commit 68a29955): **retain-and-flag, never cull** — the feed emits EVERY finding with a
    `filtered`+`filter_reason` flag (hub×hub Mode-B, Key-token Mode-H); the ledger consumes the
    unfiltered subset. Every implied-missing row carries a `primary_doc` back-link; every isolate
    links to the REGISTRY that defines it (source→registry map). Isolate text states the STRONG,
    accurate signal (max-deg ≤1 across all four graphs, no design-prose home) — the 2nd critic
    caught the 1st fix *softening* it. `audit_staleness` `vector-audit`+`npc-audit` families
    repointed to live artifacts; scope corrected to the real L0 inputs (systems/engine/canon/arcs/
    audit/references + registers/patch_register_active.yaml — the pp-graph source). Schema
    handshake (`schema_version==1`) self-surfaces a mismatch. Doctrine in SKILL.md.
  - **Dir #3 (DONE, commit 7cb3d432)** — broadened the **throughline graph** from a second registry
    source: `throughlines_complete.md`'s POST-ATOMIZATION `**Systems:**` lines (`parse_throughlines_
    complete` + `build_g_throughline(extra_rows=…)`, opt-in). MEASURED before adopting: +2
    implied-missing, +1 legit hub (Player Agency), 0 new isolates, no blob. The doc's INTERACTION
    MATRIX was measured + REJECTED (20/21 pairs interact → dense, 149/181 edges redundant, would
    inflate Clocks/MS hubs). The **μ graph is NOT extended** — no clean second Μ-mode source
    (`silo_overlap_matrix.yaml` is a frozen snapshot; the complete doc has no μ data). A critic is
    auditing #3 now.
  - **Dir #5 (DONE, commit c0f913e6) — "why not key propagation too" (Jordan steer).** Folded the
    engine **Key-propagation graph** into the audit as a 5th structural graph: `build_g_key` reads
    `module_contracts.yaml`'s emit→consume flow (the IN→resolver→OUT wiring the Godot engine runs),
    projected to token level (system↔system via shared Keys + keytype↔system). Now Mode-A hubs /
    Mode-B implied-missing / Mode-H isolates triangulate **design intent against engine data-flow**.
    MEASURED: hubs 11→16 (the +5 are genuinely engine-central; Domain Actions being a doc:null
    contract that's heavily wired is itself signal), implied-missing +1, isolates 11→9. **RETIRED
    the Mode-H Key-token filter** — the audit now SEES the Key graph, so wired Key tokens resolve
    for real and the ones that stay isolated (e.g. `Key: scene_outcome.battle_concluded`, a
    dangling/misnamed Key no module emits) SURFACE as honest gaps. A critic is auditing #5 now.
    **Adversarial pass reconciled (commit follows):** the critic verified all deltas (hubs 11→16,
    isolates 11→9, deterministic, backward-compat, 18/18) and caught two MED issues, both fixed:
    (1) **honesty** — I had mislabeled `Key: scene_outcome.battle_concluded` as "a Key no module
    emits"; it is EMITTED by mass_battle (`module_contracts.yaml:473`, a known naming-drift
    `[OPEN — Jordan]`) but CONSUMED by nothing = an **orphan/dangling emit** (deg 1). Fixed the
    ledger text (now reports the structural fact + points to the register for mechanism, asserts no
    cause), SKILL.md, the emit note, and the test; (2) **`_keytype_token` hardened** to only map to
    `Key:`-named tokens (no future broad system pattern can steal a key-type mapping). Also documented
    the 2 `faction … (cross-module → faction_state)` isolates honestly — they are `derivations:` outputs
    (real settlement→faction flows) the typed emit/consume graph structurally can't see.
    **DRY FOLLOW-UP (tracked, MED, NOT yet done):** `build_g_key` re-parses `module_contracts`
    emit/consume that `tools/observability/build_graph.py` (+ `structure_audit.py`'s `dangling_emit`)
    already own — §8 "every rule lives once". They're deliberately different projections (token-level
    narrow vs system/key/scalar rich) and agree on system↔system edges today (latent, not diverging),
    so I DID NOT force a risky refactor: build_graph reads a richer normalized graph, and consuming its
    generated `graph.json` would create an audit-refresh ordering hazard (graph.json regenerates AFTER
    emit-findings). The clean fix is to lift the shared module-level emit/consume parse into ONE owner
    both import — deferred as its own change with an expected-delta test. Comment in `build_g_key`
    now states the narrowness + names build_graph.py as authoritative (no more "mirrors build_graph").
  - **Dir #4 (pending, now lowest priority)** — L1-layer validation calibration: P3's absolute
    `n_cite_edges≥100` bar is trivially met at L1's larger corpus; make it scale-relative. Already
    honestly DISCLOSED as "L0-calibrated, not re-validated for L1", so the gap is surfaced not hidden.

---

## [OPEN] ED-IN-0148 — post-evacuation vector audit + the GM Resolution Register (2026-08-06)

`audit/2026-08-06-vector-audit/`. First corpus-wide vector audit since `c492de9` (2026-07-22) — a
baseline predating the fork inversion, the evacuation and the CLAUDE.md restoration.

**The deliverable is `05_gm_resolution_register.md`.** `systems/_architecture/videogame_mode_spec.md`
§3 defines a "GM Decides" Resolution Register with five types and states it "is not exhaustive here —
each design doc should be audited for GM references". That audit had never run. It has now: **84
occurrences / 22 files, 67 live**, all dispositioned — 30 OPEN design decisions, 6 RESOLVABLE
(rule already stated, only the attribution needs removing), 12 ALREADY RULED by spec §1's
`"GM tracks" → Engine tracks` row, 16 DISCARD per §4, 3 non-defects.

**Next actions, cheapest first:**
1. **Sweep the 12 C-rows and 6 B-rows — zero design risk**, clears 18 of 67. C is documentation lag
   against a ruling that already exists; B strips attribution from rules the docs already state in full.
2. **Currency-check A1 before designing it.** `CLAUDE.md` §4 records the combat head as
   `combat_engine_v1/` with `combat_v30.md` *PARTIALLY SUPERSEDED* — A1.1's unbounded Stunt `+N`
   may already be resolved in the engine and merely stale in prose.
3. **Three design calls held for Jordan:** A3.1 (social-contest format table), A4.1 (the nine
   political axes, explicitly "not tracked numerically"), A2.1 (MS threshold consequence generation).

**Four instrument defects filed, not worked around** (detail in the ledger entry):
- Mode C reports **97.5% of cite-edges as "notional"** — guaranteed by construction at L1.
- **The TF-IDF graph is inert**: sklearn-present and sklearn-absent runs are byte-identical
  everywhere except a `degrees.json` block nothing consumes — and absent sklearn it writes zeros
  rather than nothing, so "not computed" is indistinguishable from "genuinely zero".
- `structure_register`'s inline claim that a nonzero contract-UNDECLARED count "is itself a
  regression, not a pre-existing gap" is **false for its only row** — `mass_battle` never had a
  `sim_module` field (verified at `f03357d`).
- `review_baseline`'s `stubs.count` seeds a **ceiling** while `review_core` compares for **equality**,
  so 24/25 is red by construction and no IN action can green it.

**Cross-lane, for MB:** **J2 is registered but not executed.** J2 (2026-08-03) ruled
`systems/mass_battle/sim/` "retired, not kept alongside"; all five modules are still present and
still load-bearing (`massbattle ↔ units` is one of three import cycles, both cut-vertices). Either
execute the deletion or correct the CURRENT.md stamp — currently it reads resolved.
### ED-IN-0149 — world-churn audit: master synthesis landed (2026-08-09)

`audit/2026-08-08-world-churn-audit/06_master_synthesis.md` is the **capstone and the reading
surface** for this audit; the six prior documents remain authoritative for their detail. It carries
the reconciliation (including the retraction-and-its-withdrawal), the consolidated churn model, the
architecture ruling, the P0–P5 programme, and Part VIII's record of 24 adversarial corrections.
`topology_probe.py` ships beside it as the re-runnable falsifier for every topology figure.

**Read Part VII.0 first.** The programme's load-bearing assumption — that the Key mesh deserves
promotion from telemetry spine to churn engine at all — is filed as **J-O** and can invalidate
P1–P5 wholesale. Settle it before building anything in P1+.

**Next actions**
- **J-O** and **J-N** are new and blocking; **J-A** re-gated onto P0-3, **J-H** narrowed to P2-2.
  Fourteen decisions held in total (J-A..J-L, J-N, J-O).
- **J-M is RULED** (Jordan, in session, 2026-08-09): *"local actors should be NPCs."* P4-1 is
  unblocked — seed Local Actors through the NPC path into `world.npcs`, with
  `settlement_layer_v30.md §4.5` supplying the count, per-type table and profile. **Cross-lane:
  echo this into `HANDOFF_SE.md` and `HANDOFF_WR.md`.** It raises the urgency of **J-C**, since each
  Local Actor carries one Conviction and three incompatible vocabularies compete to supply it.
- **P0-6 (Accord unit guard) needs no ruling — it is the cheapest real win available.** One owner
  (`canon_buckets.canonical_accord`) exists; at least three live sites bypass it and
  `settlement.py:120` runs a fourth `math.floor` dialect. Write it **with an allowlist**; several
  literal comparisons are deliberate.
- **P0-3 must pin Turmoil's UNIT, not just its writer** — the registry says 0–10, `PS_MAX` is 6.0,
  and the first strain-shock pass will write it. That is the Accord defect visible in advance.
- Two live defects remain **unfixed by design** (read-only audit): the victory Accord gate at half
  its canonical height, and the conviction gate's double silencer.

---

## [OPEN] ED-IN-0150 — generated per-subsystem glossary + master term index (2026-08-08)

`references/glossary/` — 19 per-subsystem glossaries, `MASTER_GLOSSARY.md`, `glossary.json`.
Generator: `tools/observability/build_glossary.py`. **1,537 terms, 1,350 located, 0 refused.**

**Division of authority — do not collapse these:**
- `references/glossary.md` = **curated definitions**, hand-written, still authoritative. 176 terms
  have a definition only because a human wrote one there.
- `references/glossary/` = **locations**, generated. Never hand-edit; re-run the tool after doc moves.

Composed on five existing registries (§0: no term list is invented), including
`tools/build_identifier_census.py` — which was a zero-caller tool and now has a caller.

**Three silent-coverage defects in the tool, found by auditing its output rather than its exit
code.** Each is now pinned by a test in `tests/valoria/test_build_glossary.py`:
1. `descriptor_registry` read field names that file doesn't use → contributed **zero** terms while
   still being advertised as one of five sources. Guard `_assert_every_source_contributes()` now
   fails the build on any dead source (mutation-verified).
2. The `glossary.md` table parser required ≥4 columns → read **31 of ~130 rows** (93 are 3-column).
3. `MIN_TERM_LEN=3` refused **MS, CI, IP, PI, TS, CP, TD, RS, DD** — the repo's nine most-used
   abbreviations. Floor is now 2, uppercase-only, with breadth measured before lowering it.

All three are the same shape: *a reader quietly covering a fraction of its source* — the class this
repo found three times in one week as gates reporting clean over nothing.

**Deliberate scope calls:**
- Markdown is the compact reading surface (one row per term); `glossary.json` carries every path.
  The first cut emitted 5.2 MB with one file at 414 KB — a concordance, not a glossary.
- **No JS bundle** (Jordan, 2026-08-08): it duplicated `glossary.json` byte-for-byte and nothing in
  `dashboard/` loads any of the five sibling `*_data.js` files. `test_no_js_bundle_is_emitted` pins
  this — add a consumer before re-adding the file.
- Staleness is **report-only** (`tools/audit_staleness.py` family `glossary`), not a blocking
  `--check`: the output is a function of every `.md` in five roots, so a blocking gate would redden
  CI on most doc PRs. `--check` exists for local use.

**Next actions:**
1. **176 of 1,537 terms have a definition.** The generated views mark the rest
   `_no curated definition_` — that list is a ready-made work queue for `glossary.md`.
2. **186 terms are registered but located nowhere** in the scanned corpus (see MASTER's "Registered
   but not located"). Each is a stale registry entry, a moved doc, or code-only vocabulary — worth
   a triage pass.
3. The 7-vs-9 attribute-roster conflict between `glossary.md` and `descriptor_registry.yaml` is
   **still unresolved** and now visible in the generated output.

**Size, stated rather than slipped:** 10 of the 20 generated files exceed `compliance_check`'s
15k-token warn threshold — `MASTER_GLOSSARY.md` 62k, `GLOSSARY__architecture.md` 38k,
`GLOSSARY_factions.md` 32k. Compliance stays green (warnings, 0 errors) and this is the established
shape for generated reference tables (`engine/engine_params/params_tables.yaml` is 165k,
`references/restructure_ledger.md` 26k). It is nonetheless a real tension with §4's
"split at ~15k into sequential parts" rule. Not split, deliberately: a master index you must first
guess the part of is not an index. If Jordan wants them split, the natural cut is alphabetical
ranges in the generator, not hand-editing the output.

- **[OPEN] ED-IN-0153 — world-schema gap register: 50 rows, 13 needing a Jordan ruling (2026-08-11).**
  `audit/2026-08-11-world-schema-gap-audit/` — a three-axis agonist→antagonist interrogation of the
  ratified entity ladder, 19 domain lenses, and the individuation/authoring surface against the Key
  type registry and the module contracts. 17 agents, 0 errors, `stop_reason: completed`, 61 disputes
  recorded and 0 left unadjudicated. **Ratifies nothing:** no head moved, no status flipped, no
  contract or registry edited.
  - **The verdict is that the schema cannot express the ratified ladder, and it breaks at two seams.**
    Vertically: `scale_hierarchy_v1` is ratified at Country > Duchy > Province > Territory > Settlement
    while the substrate enum is four values with no national/duchy/country member, `provincial` appears
    in 0 of 55 key entries, and the B12 Territory tier collapses back into the same 17 T-codes it was
    meant to sit beneath. Horizontally, hardest at the faction rung: **no key type announces a faction
    coming into or going out of existence at any tier**, found by four lanes across all three passes.
  - **On individuation the answer is worse and simpler:** the schema mostly cannot distinguish two
    instances of anything it does carry. Every per-province authoring field the geography file supplies
    has zero code readers; `institutional_culture` — the one scalar meant to individuate faction
    behaviour — is read by no Python and authors the same value for three of six factions; and the
    genuinely faction-unique behaviours are dispatched by `faction.name` string equality while a
    capability map that would do it as data sits unread in `mechanics_index.yaml`.
  - **8 of the register's proposals are structurally ungovernable today** (G-17): §10 forbids appending
    any key type without `references/rendering_dispositions.yaml`, which does not exist. Whoever picks
    this up should expect to author that file first, or get a ruling that waives it.
  - **Read `02_verdict_and_residuals.md` before acting on any row.** Three producer claims were
    overturned; **two proposals would have caused damage if executed** and are flagged rather than
    silently dropped — notably a templar-siting fix resting on a false "T9 is highest of all 17" claim
    (T15 is higher, verified by full census).
  - **Both standing holds were honoured, not routed around:** the scale-vocabulary conflict is recorded
    as *additional evidence* for ED-IN-0103 fork 1, and no rename was proposed (ED-IN-0152).

- **[OPEN] ED-IN-0154 — `hRediscover` zeroes the corroboration signal it exists to compute (2026-08-11).**
  Found by ED-IN-0153 **in that run's own instrument**: 75 findings → 75 groups, every `rediscovery`
  value 1. `hSameFinding` gates on first-cited-file equality *before* comparing content words, so two
  lanes describing one gap through different citations never group. The owner's own comment predicts
  this failure for the exact key and the remedy inherited it. **Not fixed** — `tools/wf_harness.js` is
  copied into every workflow script and needs an expected-delta test, not a drop-in edit. **The guard
  is the deliverable:** a fixture of two paraphrases citing different files must group to 2, or the
  pattern recurs invisibly. Note the existing suite is green and mutation-verified and did not catch
  this, because it pins that `signal()` never throws — not that grouping groups.

- **[OPEN] ED-IN-0155 — the Key bus's own emit-coverage figure is stale prose in a guard file (2026-08-11).**
  `tests/valoria/test_key_graph.py:4` states *"MEASURED 2026-08-02: 55 key types declared, 1 emitted
  anywhere in the codebase"*. **No assertion in that file tests it** — its assertions cover
  producer/consumer presence, the `KNOWN_NO_PRODUCER`/`KNOWN_NO_CONSUMER` ratchet, name well-formedness
  and graph size. And it has drifted: measured this session, **4 real `sched.emit()` call sites emit
  5 distinct type_ids** — `scene.accord_echo`, `scene.contest_resolved`, `scene.combat_resolved`
  (all three via OF-7 `apply=`, all three write state) plus `da.public_governance` and
  `scene.battle_concluded` (deliberately log-only, byte-exact goldens). Live coverage is **5/55**, not
  1/55. Reachability was confirmed by caller tracing, not assumed.
  - The defect class is the corpus's most familiar one, occurring **inside a guard file**: a dated
    measurement in prose, rotting independently of its subject, with nothing that fails when it drifts.
  - **Filed rather than silently corrected** because the ED-IN-0153 audit repeated the stale figure
    before measuring it. The adjacent *"16 direct Python imports"* and *"47 dotted key names"* figures
    in the same docstring were **not** re-measured — do not cite them without measuring.
  - **The guard is the deliverable, not the edited sentence.** A test must COMPUTE live emit coverage
    and fail when it changes without the recorded figure changing with it — composing on the
    `KNOWN_NO_*` ratchet already in that file. ⚠ Caution for whoever writes it: a naive grep for
    `apply=` over the four emit lines returns **4, not 2**, because two of the comments contain the
    literal string `NO apply=`. I made that exact mistake this session and caught it on re-read.
  - Map of the whole bus — declared topology, live emit ledger, subscriber wall, 12 broken
    throughlines, and where the 8 proposed keys attach:
    `audit/2026-08-11-world-schema-gap-audit/04_key_io_and_propagation_map.md`.
  - **ADVERSARIAL PASS ON THE WRITE-UPS (2026-08-11), and it changed them.** Two read-only
    `valoria-critic` agents attacked `03_discussion.md` and `04_key_io_and_propagation_map.md` for
    fidelity and accuracy. **Twelve claims were overturned or materially softened, and every one is
    corrected in place with a ⚠ marker rather than quietly dropped** — the pattern of *how* a synthesis
    drifts from its own sources is a finding in its own right (`03` §6.1). The ones worth knowing:
    - **`04` §2.3 was backwards.** It said 5 of the 8 consumerless keys are declare-only registrations
      "where the emit exists". **DECLARE-ONLY means the emit does not exist** — the registry says so
      verbatim (`key_type_registry_v30.md:1251`, *"zero live emit calls"*). It also credited the wrong
      ED: the registrations are **ED-IN-0014**; ED-IN-0096 is the later correction that emptied
      `consuming_systems`. The error reversed the conclusion — those five are *more* debt-shaped, not
      less — and contradicted `04`'s own §3.2.
    - **`03` §5 miscounted the scripting drift, by the exact error it was arguing against.** It
      reported "8 sites of `.name == 'Crown'…'`". Six are assertions in
      `engine/tests/test_parliamentary_action.py`; production sites are **2**. G-16's concept-level
      census is the right one and is **larger — 5 sites across 3 comparison idioms** (`.name ==`,
      `t.owner ==`, `initiator ==`) in 4 modules. Substituting a literal string count for a concept
      census is pattern-matching on the term, CLAUDE.md §0's costliest named error.
    - **`03` §3 inverted the A6 reading.** `scale_transitions_v30.md` §12.4 is headed *"Known
      down-seams (Lane-B implementation targets)"* — **enumerated open debt, not a non-defect.**
    - **`03` §3's NPE claim had no instrument.** "Two generated NPCs differ on every axis" is
      unsupported: stance is territory-keyed so same-territory NPCs match, and the deviation die flips
      **one** axis. A number-shaped claim with no control, inside the section citing §0.1 point 4.
    - **`04` §5 said six of eight proposed keys land in `state_transition`; it is seven**, and the
      family is *not* the smallest (`environmental` 4, `da_outcome` 5). Also: the registry's §9
      **logical** count for that family is 9, not the join's 7 — the flattering figure was used.
    - **Roster error in `04` §2.1, on 4 of 27 rows.** `echo_transport` and `player_input` are **not
      contract modules** (`key_graph.json` files them under `unresolved_references`), while
      `campaign_architecture` and `clock_registry` **are** modules with **zero key edges**. The total
      of 27 survived only because the two errors cancelled.
    - **`fieldwork_knots` also declares the `{type: "*"}` wildcard** (`module_contracts.yaml:387`), so
      the articulation wildcard question is **two** decisions, not one.
    - **G-19 was grouped with G-18 as a do-now correction.** It is a **Class A supersession** and held
      item 14 of 17 — exactly the misclassification that would have produced an unratified change.
    - **G-17's blocking framing was overstated.** §10's A15 is **report-only today**, so appends are
      *governed and unrecorded*, not mechanically refused.
    - **Two substrate qualifications** `04` §7 had to accept: the registry loader carries a live parser
      defect (`engine/substrate/keys.py:294`), and the **cascade path has never run** —
      `schedule_emission` (`keys.py:525`) has zero production callers and `DEFAULT_CASCADE_DEPTH_MAX=0`
      would raise `TerminationBreach` if it did. "No defect in the substrate" was too strong.
    - **Two counts I fixed before the critics reached them**, recorded because self-check found them
      first: "~140 consume edges" → **125** (the doc's own table summed to 125 two lines above), and
      "60 findings across 12 lanes" → **75** (60 was the nine-lane interim, silently dropping the
      entire individuation pass).
    - **Uncorrected, flagged:** the "19 domain lenses" denominator — `00`'s own enumeration lists
      **18**. Inherited from the original request and never reconciled. `03` §9 now says so.
    - **A defect in `02` the critics found and I did not fix:** it says "all 39 state rows" where the
      register says 40 twice and a census returns **40**. Left as-is and recorded here, because `02`
      is the synthesis stage's own return value and editing it would falsify the record of what the
      run produced.

- **[PART] ED-IN-0153 second-pass correction — two defects survived the first adversarial review
  and shipped in PR #300 (2026-08-11).** The audit's two critics returned after the merge had already
  landed; most of their verdicts were applied in `92b700f` before merge, but two were not, and both
  are now corrected on a fresh branch (a merged PR cannot carry follow-up work).
  - **G-17 was misframed in the very document that cites it.** `03_discussion.md` §8 said *"nothing in
    the key half of this register can proceed until this is answered or waived"* — the exact
    overstatement the G-17 row was written to correct. `key_type_registry_v30.md:1287-1291` has A15
    enforce the `rendering_dispositions.yaml` precondition **report-only** against the existing 55-type
    roster, flipping to blocking only *"once the file exists and the backlog is at zero"*. Appends
    today are **governed and unrecorded, not mechanically refused.** ED-IN-0153's own entry carried the
    same overstatement (*"structurally cannot append"*) and is corrected in place. The real obligation
    is narrower and shippable: each `propose_key` row carries its rendering-disposition row as a
    **co-artifact**, plus regeneration of the GENERATED `engine/engine_params/key_types.json`.
  - **The lens list enumerates EIGHTEEN, and the whole unit said 19.** Not an execution error — an
    error in the original decomposition: Jordan's brief named 17, `history` split into personal and
    world to make 18, and 19 was asserted without counting. Inherited by `00` §2, `03` §2, `02` §4's
    coverage denominator, the ED-IN-0153 title/description, and 4 sites in
    `.claude/wf_world_schema_gaps.js`. All corrected; the coverage shortfall itself is unaffected
    (~14 lenses visible in findings, denominator 18).
  - **ED-IN-0153's `falsifier` field still carried the prediction ED-IN-0154 falsified** — that
    rediscovery "under-reports and cannot over-report". It reported nothing. Annotated in place rather
    than deleted, and ED-IN-0154 added to its citations.
  - **Process note worth keeping:** both critics were launched read-only and returned *after* the PR
    merged. A review that lands after the merge is still a review — it just costs a second branch.
    Launch the verifier before the commit that ships the thing it verifies, not beside it.

- **[OPEN · needs Jordan] ED-IN-0156 — CLAUDE.md asserts 13 countable figures about the tree and
  NOT ONE is guarded (2026-08-11).** Found while adversarially checking the ED-IN-0153 residual *"no
  cited PP number was provenance-verified"* — the check confirmed the residual and then found a
  larger defect behind it.
  - **No test asserts any of the 13.** `ci_hooks_verifier`'s CLAUDE.md checks (2 and 6) assert the
    **presence of prose** — the commit path is documented, §11 survives — never a number. The file
    reads as guarded while every factual claim in it is unprotected.
  - **Three of three re-measured are wrong or scope-ambiguous.** `48,612 chars` → actually **56,384**
    (a 16% understatement, and that figure is the load-bearing input to §11's per-wake-up token
    floor); `106 modules` in `tools/` → **108**; and `433 of 452` PP-unresolvable reproduces **only**
    against `patch_register_active.yaml` alone (6 entries; 460/466 today). Include
    `registers/patch_register_index.md` — a live register on `main` with **196 entries** — and it is
    **328/466, 70% not 96%**. The scope is unstated, so the number is not merely stale, it is
    **unreproducible without knowing which registers count**.
  - **The residual it came from is now answered.** ED-IN-0153 cites 11 distinct PP numbers; **6
    resolve** (2 active, 4 index). The 5 that do not — PP-687, PP-510, PP-519, PP-723, PP-688 — are
    **evacuation casualties, not fabrications**: each is heavily cited across the live tree (PP-687 in
    29 files, PP-688 in 17, PP-723 in 11), so their entries went to fork ref `c451bcb`.
    `tools/validate_ed_citations.py` has **no PP handling at all**, so neither case is caught.
  - **Why this file and not the others.** Every other countable surface here is GENERATED and
    freshness-guarded — ENGINE_ATLAS, KEY_INDEX, CONTRACT_INDEX, the glossary, apparatus_registry.
    CLAUDE.md is hand-written instructions, so it sits outside the generated-artifact discipline it
    prescribes for everything else, while being the one document every session reads as authority at
    SessionStart. §0.1 point 5 names the remedy and the file does not apply it to itself.
  - **Proposed fix, held for Jordan — not new machinery.** A test that recomputes each asserted figure
    and fails on disagreement, in the ratchet shape `test_key_graph.py` already uses. Figures too
    expensive to recompute should stop being asserted and cite their generator instead. Any fix must
    also **state each figure's scope**.
  - ⚠ Filed by a session that had itself repeated `433 of 452` earlier the same day without measuring
    it. That is the cost being described, not a hypothetical one.

- **[OPEN] ED-IN-0157 — second adversarial pass: the ED-IN-0153 RESIDUALS were themselves unverified
  claims (2026-08-11).** The first review checked what the register *asserted*; nobody checked `02` §4,
  the list of what the run never did. Record: `audit/2026-08-11-world-schema-gap-audit/05_second_adversarial_pass.md`.
  - **`existing_tracking`, 22 "none found" rows checked:** G-19 and G-36 **overturned**, G-25/G-44/G-13
    softened, 17 upheld. G-19 is the sharpest — `supersession_register.yaml:227-230` registers PP-632's
    struck Knot tier model, and **the row's own Evidence field quotes the pointer its tracking field
    denied**. The sharpening beats the overturn: that register's `files_to_recheck` **omits**
    `key_type_registry_v30.md`, which is the nameable mechanism by which the struck enum survived into
    the generated `key_types.json`.
  - **The reverse error is worse than "none found", because a citation looks verified. Four found.**
    G-49 cites a line that says the **opposite** (*"is consumed, not orphaned"*); G-44/G-45 cite OI-37
    at `HANDOFF_SE.md`, which contains **zero** occurrences of it — inherited verbatim from a stale code
    comment without opening the cited file; G-17/G-20 cite a **line anchor into a JSONL ledger** that
    has since moved twice. **Cite the id, never the line** — an append-and-archive ledger renumbers.
  - **Every flow-skeleton and code anchor opened matched verbatim.** The failures cluster entirely in
    ledger/handoff line anchors and one reversed prose read. That is a usable rule for the next auditor.
  - **"Unread, not clean" is right in direction, wrong in detail** — `world history`, victory and npcs
    all produced findings; the residual was true of lane *labels* and false of subject matter.
  - **Seven unfiled gaps found in the unread surfaces, recorded as OBSERVATIONS not filings** (several
    straddle lane boundaries; the G-33 precedent says that is not IN's call). Sharpest: **`echo_transport`
    emits the combat keys and has no row among the 27 contracts** while the registry names it an emitting
    system elsewhere; `World.threadcut_beings`/`comovement_deck` are built-and-unowned with the threadwork
    contract explicitly disclaiming them; and **victory's fallback winner-decision is inline in
    `mc_v18.py:276-286`** — in every campaign not decided by GD-1, the outcome is computed by a formula no
    contract owns.
  - ⚠ **N-4 exposes a scoping defect in held decision 5**: it asks whether the 7-member
    `not_descriptors.tracks` block is swept and never mentions the structurally identical **21-member
    `derived_values` block on the line above**. Ruling on one and not the other special-cases a block —
    the same objection G-05 raises to promoting Renown alone. **Jordan should be asked about both blocks.**
  - ⚠ **STILL UNVERIFIED, and it is the residual that matters most:** nothing in this unit has been
    verified **by execution**. The campaign run to confirm `04` §3.2's emit ledger empirically was begun
    and not finished; every emit and reachability claim remains static analysis. Both critics were
    read-only and could not run a test. **No third pass has been run** — two passes found ~14 then ~12
    defects, which is not evidence of convergence.

---

## [OPEN] ED-IN-0158 — consolidation sweep: 8 opportunities, 3 candidate findings killed (2026-08-11)

**One document:** `audit/2026-08-11-consolidation-sweep/00_consolidation_sweep.md`. Whole-tree
read-only sweep at `c26a22c` for prune / cut / refine / distil / dedup / aggregate / consolidate
opportunities, read against the twelve commits of 2026-08-04..11. Solo — no fan-out, no workflow.
**Nothing executed.**

Reconciled from an original `00_findings.md` + `01_adversarial_pass.md` split (superseded, git
history only — `4a101b1`, `32f8cfa`): in that layout a reader of the findings got claims whose
corrections lived in a file they had to be told to read first. **Every finding now carries its
attack result inline**; §3 holds the retractions, §7.5 the falsifiers.

**What the attack killed (§3.1).** The draft's strongest finding was that `build_glossary`,
`build_engine_atlas` and `build_contract_index` — all shipped this week, all with **zero callers**
in CI / hooks / `valoria_local` — were three fresh instances of the defect ED-IN-0149 had named
three days earlier. Grep supported it. Reading the tests refuted it: each is invoked by a blocking
pytest that runs the real builder's `--check` or byte-compares committed output to a fresh build.
**The conclusion inverts** — a freshness gate is *better* than a scheduled regenerator, because it
fails the PR that caused the staleness instead of someone else's a week later. Credit, not fault.
What survives is the **contrast**: the pattern was proven three times this week and is absent on
the two artifacts below.

**Unblocked, cheap, ranked:**

1. **F3 — `handoff_atomize` has 33 live findings and its test cannot see them.** `--all --check`
   exits non-zero on all nine lanes: IN's executive summary claims **44 live items when the file
   has 73**, and is dated 2026-07-28 while the file carries an item from **2026-08-11**; 30 of IN's
   37 bullets carry no `[OPEN|PART|DONE]` tag, so the banner infers from prose — the inference
   ED-IN-0086 introduced the tag to replace. Wired into nothing.
   `tests/valoria/test_handoff_structure.py` exercises `status_tag`/`classify`/`tag_problems` on
   **synthetic strings** and never invokes `--check` against `registers/handoffs/*.md`. §0.1 point 2.
   **The fix is a ~10-line copy of `test_engine_atlas.py:46`.** Distinct from W8 (the atomization
   *run*, blocked on 2 Jordan calls) — the guard is not blocked on anything.
2. **F5 — CLAUDE.md, 13,963 tok, §3 contradicts itself.** The `engine/` row says engine/ holds "the
   prose param tables `engine/params/`"; the struck `~~engine/params/~~` row three rows above
   records its 2026-08-05 evacuation; `ls engine/` confirms no `params/`. Also measured stale: the
   `tests/` row's "~850KB of narrative/audit `*.md`" (**8 files, 90 KB**, none carrying the named
   prefix) and the `tools/` row's "36 of 106 modules" (apparatus_registry: **123 entries, 6
   orphaned**). Four struck rows (2,392 chars) restate relocations `restructure_ledger.md` already
   owns machine-readably — §8's invariant applied to CLAUDE.md itself. Paid on every session **and
   every subagent**.
3. **F2 — `audit_registry.jsonl` indexes 7 of 41 units and its gate is tail-blind.** After
   resolving the `designs/audit/ → audit/` prefix (`restructure_ledger.md:981`): **34 dirs
   unindexed, 10 rows dangling** at subjects the evacuation removed. `ci_audit_registry_check.py`
   reports **3**, because it filters to entries newer than the registry's own latest date — blind
   by construction, ED-IN-0115..0119's class. Needs a keep-or-retire call.
4. **F1 — 688 KB of committed derivatives, no consistency guard.** Five `_data.js` decode
   byte-equal to their `.json` (all five verified), beside a 752 KB `console.html` that inlines all
   six feeds. The README calls the `index.html`+`_data.js` pair "Dev pair (**regenerable**)" and
   `console.html` the primary. `index.html:185` loads `review_state_data.js`, which `.gitignore`
   excludes — **the committed dev pair is broken in every fresh clone.** No test asserts the three
   tiers agree.
5. **F4 — the lane handoffs repeated the defect the root file was archived for.** `HANDOFF_IN.md`
   **191 KB** vs the root file's 16 KB at archiving; `## Next actions` starts at line **1506**.
   Separately and *not* blocked on W8: the root `HANDOFF.md`'s first Next-actions bullet — what the
   SessionStart banner surfaces above all else — has been a struck-through `✅ RESOLVED` item since
   2026-07-30, and appeared verbatim in this session's banner.

**Also filed:** F7 `research/` (2.7 MB, live, **zero** CLAUDE.md mentions while §3 documents four
trees that no longer exist); F6 glossary retention (3.0 MB, three renderings — **flagged as cost,
not defect**: it is correctly guarded); F8 two SUPERSEDED heads pointing at `designs/` paths
(verified resolvable, non-breaking).

**Spared under attack, recorded so they are not re-flagged:** the 16 `*_flow_skeleton_v1.md` (every
line anchored `path:line symbol` and verified against the tree by `test_flow_skeletons.py`; the
"aggregate" is the format spec + roster, not a concatenation) and the `throughlines_meta` +
`_meta_infill` pair (retired convention, but `ci_vetting_check.py` — blocking — reads it as its
framework; §4 grandfathers it). Both pattern-match as prunable and are load-bearing.

**Needs Jordan:** the F2 keep-or-retire call, and F6's retention shape.

**Method limit, stated:** sweep and critic shared one context — not the structural independence
§10 asks for (`hCritic`/`valoria-critic` was unavailable). Every finding was re-derived from a
command against the working tree rather than from the draft's prose, which is what caught the three
retractions, but that is not equivalent. **F1/F2/F3 want an independent read before execution.**
Unverified, listed in §7.3: the PP-NNN scope mismatch (my 320/527 neither confirms nor refutes §0's
433/452 — different scan roots), F1's remediation untested in a browser, and the two report-only
`review_core` failures (`vocab.a17`, `stubs.count`).

**Two self-implicating items the document records rather than hides.** (1) A **process failure**:
`pytest tests/valoria` was run once as the session's opening baseline, *before any file in this
sweep existed*; `valoria_local --staged` was run after the edits and does not include the suite, so
a PR body claimed a green that belonged to `c26a22c`. CI caught it in four minutes
(`test_engine_atlas.py::test_atlas_is_current`, fixed in `32f8cfa`) — the guard worked, I did not.
(2) **This entry grew `HANDOFF_IN.md` from 191,413 to ~197 KB**, worsening F4 on the session that
filed it; the append-only dynamic operating on its own describer. Both are in §1.1 and §F4.

**Residual filed, not proposed (§6.1):** `ENGINE_ATLAS.md`'s ambiguity census counts bare
occurrences of every contract name corpus-wide, and `audit` is one — so any document using the
ordinary English word turns the committed atlas stale (measured: 2183 → 2186 from this sweep alone)
and every prose-adding PR in any lane inherits a regenerate-and-commit step for a file it has no
other relationship to. Correct gate behaviour; the signal `proposals/canonical_nomenclature_v1.md`
(#301) targets. Not proposed as a change to the gate.

---

## [OPEN] ED-IN-0159 — code-leanness census + a 4-phase consolidation plan (2026-08-11)

**One document:** `audit/2026-08-11-code-leanness/00_code_leanness.md`. Scoped by Jordan: *"as lean
as possible without sacrificing mechanisms"*, lean = **fewer files to track/review/edit/audit**, and
**"my concern is with code"** — registers/logs/lane files explicitly out of scope. Population: 118
`.py` under `tools/`, `.githooks/`, `skills/*/scripts/`. **Nothing executed.**

- **[OPEN] The abstractions exist and were never adopted.** `ci_common` 11/118 · `obs_core` 9/118 ·
  `names` 9/118 · `registry` 2/118 · **`pathres` 1/118 — while declaring itself the SOLE PARSER of
  `restructure_ledger.md`, which 6 modules parse.** Re-implementation: repo-root **53 sites in 15
  distinct spellings**, YAML register load 44, Status parsing 9, lane roster 9, ledger read 8,
  `id_reservations` 8, token estimation 6, ID regex 6.
- **[OPEN] The duplicates disagree — measured, not assumed.** Five live `## Status:` regexes over 551
  tracked `.md`: union 200, intersection 193, **7 DISPUTED** — named in full, including
  `workplans/valoria_master_workplan_v6.md` (the live steering surface) and
  `systems/ui/valoria_ui_ux_v4.md`. Six are invisible to **both** `dashboard_data` (needs a hash, no
  space) and `build_identifier_census` (exactly two hashes). Silent failure. **This is the residue
  after `obs_core` already consolidated this exact primitive** — it re-grew.
- **[OPEN] 166 citations of `params/core.md` across 47 live files**, a path that does not exist:
  `params/ → engine/params/` (`restructure_ledger:720`), evacuated 2026-08-05 (ED-IN-0145). Every
  constant in the executable model cites an absent authority — CLAUDE.md §0's PP-NNN disease, one
  register down. **Remedy is in-tree and byte-faithful:** ED-IN-0139's
  `engine/engine_params/params_tables.yaml` is keyed by original path.
- **[OPEN] The audit probe scripts are unpromoted instruments, not dead one-offs** — I had them as
  deletion candidates until I read them, and that was wrong. 38 of 41 anchors resolve;
  `stress_battery.py` **executes today: 22 checks, 21 PASS, 1 FAIL** (mirror-match p=0.000 at
  arming/heavy), in no CI job. **Class B is this mission's own tooling:** `flag_ablation.py`
  (leave-one-out per boolean flag — load-bearing vs actively costing), `harness.py` (every factor →
  WIRED-LIVE / WIRED-SITUATIONAL / **DEAD**), `interaction.py` (INDEPENDENT/MASKING/SYNERGY/
  ANTAGONISM), `reachability_sweep.py`. **The instrument that answers "what can we cut without
  sacrificing mechanisms" already exists and is unrun** — and it measures *behavioural* deadness,
  strictly better than the referential deadness an import graph sees. **§10's emergence-auditor
  candidate is blocked on "once ablation is runnable"; ablation is runnable — that blocker is stale.**
- **[OPEN] `audit/2026-06-03-contest-groundup/engine.py` is a fork of the resolution core**
  (`MU_PER_DIE`/`SD_PER_DIE`/`OVERWHELM_SIGMA`/`net_boost`, ED-884/ED-934 semantics, P-232 floor) with
  constants hardcoded. Matches live today; nothing would report it if it stopped.

**Plan (§5), ordered by risk.** Phase 0, no judgment required: glob the syntax-check job (**it names
32 of 108 `tools/*.py`**), repoint the 166 citations, fix 3 broken anchors. Phase 1: one owner per
primitive as **~8 individually-tested migrations into `ci_common` re-exporting `obs_core`** — *not* a
fourth library — cheapest-first, gates last, because §8 already ruled each gate migration needs its
own expected-delta test. **1.6 is the one with a real delta:** collapsing `STATUS_RE` makes the 7
disputed docs visible, and the test must name all 7. Phase 2: promote the batteries to
`tests/valoria/` as `xfail(strict)` and the Class-B instruments to a standing
`tools/mechanism_census.py`, then **run it — its output is the input to any cut decision**. Phase 3:
uncalled code, where **the deliverable is a guard, not a delete list**.

**Honest accounting:** this is **not** a large file-count reduction — Phase 1 removes ~0 files, Phase
2 adds an owner, Phase 3's ceiling is ~15 `sim_harness` files plus whatever tracing confirms. It is a
large **edit-surface** reduction (53→1, 44→1, 8→1, 6→1, 5→1; adding a lane goes 8 edits → 1), plus
one closed correctness class and one closed provenance class.

**Three orphan measurements DISCARDED for method defects** (§7, recorded so they are not re-derived):
the AST import graph cannot dot-resolve `combat_engine_v1`'s bare imports and called
`wrapper` an orphan while `combat_bridge.py:141` calls it; 156 of 249 "never imported" are
pytest-collected test files; the "ten ledger readers miss the lane files" flag was my detector failing
to recognise the `editorial_ledger*.jsonl` glob. **No delete list is reported anywhere in this audit** —
only tracing candidates. Four `systems/*/sim/` modules (`charter_liberties`, `home_sanctuary`,
`hafenmark_equipment`, `infrastructure_reclamation`) have two-method agreement and are where tracing
starts.

**Needs Jordan:** the `sim_harness` promote-or-retire call (28 files), and whether Phase 2's
`mechanism_census` should gate or merely report.

**[OPEN] ED-IN-0159 §8 — Fable-5 read-only second pass. It overturned two of my findings.**

A `valoria-critic` (Read/Grep/Glob only) was given both audits as prior art to attack; every
load-bearing claim was re-run with Bash here.

- **The four "possibly-uncalled" factions modules are REACHED** —
  `engine/tests/test_pipeline_reach.py:749-755`, oi17 test passes. All four are `stub_resolve` no-ops
  carrying Jordan directives found nowhere else. **Phase 3.1 is CLOSED, not started.** The reasoning
  error is the lesson: both my methods were blind to the *same* thing (string-path dispatch), so
  "two independent methods agreed" carried no information.
- **`apparatus_registry`'s orphan count is an undercount by construction** —
  `build_apparatus_registry.py:213-220` treats basename-in-workflow as invocation, and the syntax job
  is a `py_compile` list, so being compiled counts as being invoked. **ED-IN-0158's F5 used that
  number to correct CLAUDE.md; the staleness stands, my replacement figure does not.**
- **Folding it in broke my own plan:** Phase 0.1 (glob the syntax gate) would take basename-in-workflow
  from 46/108 to 108/108 and silently zero the orphan census. Amended — both halves in one commit.
- **New, confirmed, all re-run:** `compliance_check.py` calls `_lazy_import()` (:165) and `check_all()`
  (:306), **neither defined** — `python3 tools/compliance_check.py` raises `NameError`, dead code in a
  **blocking gate's** file; the index+infill apparatus is inert three ways; two blocking size-cap gates
  check the same files twice; two always-exit-0 tools sit in the blocking job;
  `ci_checks_registry.yaml` references `valoria_hooks.py` **5 times** and that file does not exist.
- **Reframed:** the mass-battle dual engine is already ED-MB-0065 awaiting a ruling (nothing new);
  personal combat's duplicate resolver is flag-gated design, not a leanness edit.
- **`tests/valoria`:** no duplicate-fact modules in a 15-of-153 sample; 32 files repeat one path
  block. The instrument to finish it is `references/test_register.json` — which I did not know to use.

**Next:** §8.9 lists the amended plan (0.1 amended; 0.4/0.5/0.6/1.9/1.10/1.11/2.5 new; 3.1 closed).
**Do not act on F10** (the v32 keep-rule over-cover) until a `MEASURED-BY:` sweep confirms nothing
cites the m2–r10 stations — moving a cited instrument turns `ci_claim_provenance_check` red.

**[OPEN] ED-IN-0159 — FULL REWRITE after PR #304 (2026-08-11).** Both audit documents rewritten so
each states its findings once, in final form, and **one merged 3-track plan** (in
`audit/2026-08-11-code-leanness/01_plan.md`) now replaces this audit's earlier plan, the sweep's ranking,
**and** #304's 887-line remediation plan. Adjudicated by a second Fable-5 read-only pass; every
load-bearing claim re-verified with Bash.

- **My biggest figure was 47% of its class.** The provenance defect is **354 citations across 74
  files and 12 distinct evacuated `params/` paths** (`contest.md` 102, `mass_combat.md` 49,
  `factions/stats_1_7_scale.md` 10, `factions.md` 9, +7 more) — **not 168 across 46**. I counted one
  basename and called it the defect. The instrument now measures the class and exits 1 if any cited
  path starts resolving.
- **The two theses compose.** #304 finds `systems/` has *no* copy-paste problem (7 copies in 25k LOC)
  but an idiom-divergence one; this audit finds `tools/` full of duplicated idioms. **The methods are
  mutually blind** — and #304's own lens 7 covered `tools/` and corroborated this audit.
- **Binding constraint on Phase 1:** one-owner collapse is valid **only where the copies agree
  today**. #304's degree ladders carry **four incompatible meanings of `net`** under one
  `(int,int)->str` signature; folding there converts visible divergence into invisible divergence.
  Its **A7 LEAVE list must survive**.
- **I correct #304 on one item.** `altonian_reinforcements` did **not** miss the OI-17 sweep: it is
  `test_pipeline_reach.py:166`'s **accepted-handoff** manifest row, excluded from the roster at
  `:747`, and `test_only_accepted_handoff_still_raises_unconditionally` (`:783`) asserts it **must
  still raise** — it passes. **STRUCK** from the merged plan; acting on it breaks a green guard and
  crosses a lane boundary. Both read-only passes accepted the claim; only execution caught it.
- **Do not quote from #304:** its "nine degree implementations" headline (its own divergence audit
  supersedes it — **16 producers**), or its location count (inconsistent 168/196/400; the tsv has
  **196** rows and its verifier runs 196/196, 55 groups).
- **#304 is better evidenced than me on the deprecated combat resolver** —
  `export_sim_params.py:36` publishes the superseded model as typed truth, and dropping it from
  `SCAN_DIRS` is **not blocked** on the flag ruling. My "nothing to do until ratification" was wrong.
- **Both dead-code censuses are wrong, in opposite directions** — `build_apparatus_registry` counts
  `py_compile` as invocation (undercounts orphans); `dead_primitive_census` has no stub concept
  (inflates deadness). **No valid orphan count exists in either direction.** Ship the two fixes as one
  pattern fix (plan G9 + T6).
- **Also withdrawn:** the `pathres` "false sole-parser claim" charge — `pathres.py:121-127` now says
  "INTENDED sole parser … not yet the actual one" and names the four remaining parsers. The
  consolidation is still undone; the rhetorical charge is not.

**Held for Jordan:** #304's six (#0 the `net`/`ob` convention **blocks #1 and #2**; #1, #1b the
strategic layer's d6>=4, #2, #7 `standing` bounds, #8), plus the 37 grandfathered `*_index.md` files
and the `sim_harness` call. **Run plan T4 (the mechanism census) before ruling #1/#1b/#2/#8** — it
prices exactly those questions.

**[OPEN] ED-IN-0159 — the plan is chunked, and the audit cap is 30k (Jordan, 2026-08-11).**
*"Chunk the plan instead of cutting content from plan. Threshold can be 30k for these."*

- **`audit/2026-08-11-code-leanness/01_plan.md`** is now the **plan of record** — three ordered
  tracks reconciling this session's two audits, #304's 887-line remediation plan, and the
  centralization directive. `00_code_leanness.md` keeps the evidence and points at it.
- **`references/atomization_rules.yaml` gains one row**: `audit/**/*.md` → `max_tokens: 30000`,
  placed above the `**/*.md` catch-all because `_match_rule` is first-match. **Single owner** —
  deliberately *not* a second cap in `ci_register_size_check`'s `THRESHOLDS`, which already carries
  three rows single-sourced from this file because they kept drifting (ED-IN-0097), and where the
  two gates still disagree on the register cap (15,000 vs 10,000 — §1.8, plan step G6).
- Verified: both documents match the new rule (30,000), `CURRENT.md` and the other non-audit files
  still match the 15,000 catch-all — the change is scoped, not global.

**[PART] ED-IN-0160/0161/0162 — the consolidation plan of record is being EXECUTED (2026-08-12, PR #305).**

Plan: `audit/2026-08-11-code-leanness/01_plan.md`, Track G, in the order its §8.4 sets.

- **G7 DONE** — `tools/ci_common.py` is now the single import surface for `tools/`: repo root, 9-lane
  roster, token estimation, PP/ED id regexes. `obs_core` **re-exports** all of them, so its nine
  consumers are byte-identical. The layering direction (primitives *below* the observability tier, not
  in it) is forced by the dependency graph — `obs_core` → `build_decisions` → PyYAML + a corpus sweep
  at import time, and stdlib-only blocking gates need only the tuple. Heavier primitives re-export
  **lazily** via PEP-562 `__getattr__`; a subprocess test asserts `import ci_common` still pulls in
  neither `obs_core` nor PyYAML. Measured: adoption 11/118 → **60/118**, repo-root 53 → 24, roster
  9 → 3, tokens 6 → 5, **zero** unmigrated repo-root definitions left in `tools/`.
- **G8 DONE** — one owner for `## Status:`; four compiled regexes in the tooling tier → **one**.
- **G1 DONE** — `compliance_check.py`'s dead check/report half excised (111 lines), co-change test
  updated in the same commit as the plan required.

**FOUR CORRECTIONS TO THE PLAN, each measured, each with a falsifier:**

1. §8.1's `id_reservations read | 8 → 1` had **nothing to collapse** — zero modules load that file;
   its 8 are *mentions*. No reader was shipped: an abstraction with no caller is the defect
   ED-IN-0149 named.
2. One of §1.3a's **five** diverging Status parsers **does not exist**. `dashboard_data._STATUS_RE`
   went when `obs_core` was built; the pattern survives only in `obs_core`'s *historical comment*.
   The census read a comment describing a past state as a present one, so every
   "invisible to: dashboard_data" cell in the disputed table is wrong.
3. The G8 delta is **one-sided, not two-sided**. Nothing is removed from any parser;
   `ci_generation_consistency` never diverged from the owner at all (206 docs, 0/0).
4. The divergence that mattered was the **window**, not the regex. `STATUS_HEAD_LINES = 80`, chosen
   by measuring SUPERSEDED reclassifications: 12 lines flips 2, 40 flips 0, 80 flips 0, whole-doc
   flips 1.

**Two mechanisms nearly lost, both caught by tests the plan required:** a first-Status-line-wins
helper silently dropped `systems/factions/faction_canon_v30.md` (two contradictory `## Status:` lines,
6 and 7) from the incompleteness feed — a one-sided test would have passed; and
`test_no_module_actually_loads_id_reservations` **counted itself**, §2.4 reproduced one section from
where the trap is documented.

**[OPEN] ED-IN-0162 — a stale generated artifact feeds a freshness-gated one.**
`references/identifier_census.json` + the 16 `systems/*/_identifier_census.yaml` were last built
**2026-08-04**; the docs they index changed 08-08 and 08-10 (regenerating = 9,773 lines). **Nothing
gates them** — no CI job, no `valoria_local` entry, no `--check` test — while `references/glossary/`
**is** built from them (1,243 of its 1,537 terms) and **is** gated. The glossary's `--check` can only
prove it matches its inputs, never that its inputs match the tree. Fix: regenerate, then add the
`--check` gate on the `test_engine_atlas.py:46` pattern.

**NOT ratified, still held for Jordan:** #304's six (**#0** the `net`/`ob` convention — gates the
degree family 16→1, `roll_net` 3→1, `roll_pool` 2→1 — plus #1, #1b, #2, #7, #8), the **37
grandfathered `*_index.md` files**, and the **`sim_harness` promote-or-retire call** (28 files, and
12 of G7's 24 residual repo-root sites are in that cluster — they are deliberately unmigrated).

**Two DOCUMENT defects surfaced and deliberately NOT fixed** (other lanes' content, not
infrastructure): `workplans/valoria_master_workplan_v6.md` — the live steering surface — carries no
conventional `## Status:` line at all, and `systems/ui/valoria_ui_ux_v4.md` bolds its. The G8 test
asserts both are **still invisible** and fails when either is fixed, so neither can rot unnoticed.

**[PART] ED-IN-0163 — G2 IS HALF-DONE AND ITS SECOND HALF NEEDS JORDAN.** Five dead-scope retirements
landed. The generator-retirement half names `deprecated/tools/` as its landing site — removed by the
2026-08-05 evacuation, pinned `evacuate` by `test_evacuation_plan.py:98`, and forbidden as a destination
by `:166`. **Jordan must rule** the retirement mechanism for dead tools post-evacuation. Do NOT re-execute
G2; do NOT force the move.

**[DONE] ED-IN-0164/0165 — two rounds of adversarial review over this branch's own work.** Fourteen claims
refuted and fixed, including a guard that was vacuous for every `def`-defined export (found by THREE
independent passes), a gate whose coverage archiving silently shrank (22 → 47 entries, still green), a
dead policy row the dead-scope sweep itself created, a roster figure wrong on concept, a fifth surviving
`## Status:` window, and a 5-line rationale copy-pasted into 54 files. **20 mutants now killed** where the
branch had run none against the repo's own mutation standard.

**Next in the plan:** G3, G4, G5, G6, G9, G10, G11, G12, G13, then Track T. **G2 is blocked on Jordan.**
Track S is #304's engine/systems work in other lanes and is mostly gated on **#0**. Track S is #304's engine/systems work in FA/PC/MB/WR lanes and is mostly gated on **#0**.


## [DONE] ED-IN-0166/0167/0168 — Track G continued: ED-IN-0162 executed, G3, G9 (2026-08-12)

Plan: `audit/2026-08-11-code-leanness/01_plan.md`. **Landed: G1 · G3 · G7 · G8 · G9.**
**Still blocked: G2's second half (Jordan, ED-IN-0163). Not started: G4, G5, G6, G10, G11,
Track S, Track T.** The plan's `## Status:` line is reconciled to match, and its claim that
"G12, G13" were not started is **corrected — those steps do not exist**; Track G ends at G11.

- **ED-IN-0166 — ED-IN-0162 CLOSED.** The census was regenerated (15 subsystem files + the
  roll-up, 9,798 lines) and the glossary rebuilt from it (**1,537 → 2,065 terms**). Confirmed the
  finding against the tree first: the committed combat census listed **SEVEN docs**, five of them
  deleted by the 08-08 5→1 consolidation, and knew nothing of `combat_reference_v1.md` or the
  08-10 flow skeleton. **Two corrections to ED-IN-0162**: there are **15** subsystem census files,
  not 16; and the `--check` it prescribed wiring in **returned before comparing the roll-up**, so
  the gate it asked for would have been blind to the artifact it names first. Tool fixed, then
  gated (`tests/valoria/test_identifier_census.py`, 7 tests, 2/2 mutants killed).
- **ED-IN-0167 — G3.** Two structurally-unfailable tools left the blocking job; registry `ci_job`
  flipped in the same commit. **`valoria_local.py:162,172` already had both report-only**, so the
  tiers had disagreed for months and the stricter-looking one was wrong. The `valoria_hooks.py`
  ghost tier (level 4, `paired_hook`, the 19-entry `in_session_hooks` section — **124 ghost lines** — 89 for the section, 35 `paired_hook` lines — **zero
  code consumers** (the file goes 479 → 373, a net 106, after ~18 lines of tombstone)) is deleted, along with `broken_dependency_checker`'s check (d), which had been
  `os.walk`-ing the **entire repo on every run of a blocking gate** since the 08-05 evacuation to
  rediscover the file was gone. Guard: `test_blocking_tier_is_honest.py`, 6/6 mutants killed,
  **no allowlist needed — 20/20 blocking tools can fail and all 5 that cannot are report-only** (first published as 17/6; both wrong, corrected under ED-IN-0169).
- **ED-IN-0168 — G9, both halves in one commit.** The compile gate covered **32 of 108** tools;
  globbed. `invoked_by` no longer counts compilation as invocation. **Orphans 7 → 11**,
  **prune candidates 0 → 2**, exactly §2.2's predicted +4. Half B's measured delta today is
  **zero** and is recorded as zero (§0.1 point 4) — its job is the recurrence case, which is
  *executed* rather than argued by
  `test_naming_every_tool_in_the_compile_gate_does_not_zero_the_census`.

**MY FIRST G9 IMPLEMENTATION WAS WRONG, AND THE INSTRUMENT CAUGHT IT RATHER THAN A REVIEW.**
`strip_compile_only_steps` began as one multiline regex and swallowed the whole `validators-report`
job — because that job's `run:` mentions `py_compile` **inside a comment**. It reported 13 orphans
and 2 prune candidates, of which `mechanics_index_gen` and `ci_workplan_pointer_check` were FALSE.
That is `test_gate_coverage.py::test_a_comment_mentioning_py_compile_does_not_zero_a_jobs_command_list`
reproduced **one file away from the test that names it** — the ED-IN-0161 "instrument counted
itself" shape, third instance in three commits. Rewritten as a line scanner with an explicit
`_INVOKES` guard; a second over-reach (comment-skipping step-end swallowing the next job's banner)
was found by the same route. Final strip removes exactly 6 lines. **The over-reach direction is now
tested at least as hard as the under-reach one**, because only the over-reach produced a false
finding.

**NEXT, in dependency order.** **G4** (make `pathres` the actual sole parser — four parsers, plus
the two-tier walk exclusions and the TREES roster 17→19) and **G6** (size caps: adopt the policy
cap, delete the stale duplicate block, then merge the two gates — the merged gate MUST carry the
`.jsonl` caps *and* the local-tier coverage or coverage regresses) are both unblocked and
independent. **G5** (the vitality meta-guard) depends on G1+G2+G4 and so is still gated on G2's
Jordan call. **G10** waits on Track S's S1. **G11** is unblocked. Note that G5's meta-guard must
encode ED-IN-0163's anticipatory rule or its first run demands deletion of every correct
forward-looking policy row — and the **25 zero-match rows** ED-IN-0164 recorded are its triage
input, deliberately left untouched.

**HELD FOR JORDAN, unchanged by this pass:** #304's six (**#0** the `net`/`ob` convention, which
gates the degree family 16→1 — plus #1, #1b, #2, #7, #8), the **37 grandfathered `*_index.md`
files**, the **`sim_harness` promote-or-retire call**, and **G2's retirement destination**
(ED-IN-0163). The plan's own recommendation stands: **run T4 (the mechanism census) before ruling
#1/#1b/#2/#8** — it prices exactly those questions behaviourally, and it already exists and has
never been run.

---

## [DONE] ED-IN-0173/0174/0175 — Wave 1+2: the merge's own compliance debt, and G2 CLOSED (2026-08-13)

**Session shape.** Jordan asked for the backlog partitioned into what needs no ruling, then ran as
three PRs: **1+2 here**, 3 alone, 4+5 together.

### G2 IS DONE — and the guard conflict everyone predicted does not exist

Jordan ruled *"Dead files get moved to deprecated."* (**ED-IN-0171**), resolving **ED-IN-0163**.
`atomizer`/`doc_index_gen`/`index_gen` → `deprecated/tools/`. **The 37 grandfathered
`systems/**/*_index.md` outputs are untouched and still HELD** — the generator retires, not its
artifacts.

**The result worth carrying forward is a refutation of my own prior record.** ED-IN-0171 stated —
and the wave plan handed to me repeated — that `tests/valoria/test_evacuation_plan.py:166` forbids
the destination, so executing the ruling *requires* amending a pinned guard. It does not.
I made the move and ran the suite **before** editing anything: **32/32 pass, unamended.** `:166`
binds `p['moves']`, the destinations the `evacuation_plan` **tool** computes from its own
relocation rules; a `git mv` never populates that dict. `:98`'s pin still holds, and is in fact the
same verdict the moved files now receive — `('evacuate', 'R-DEPRECATED', 'history — the evacuation
tag preserves it')`, which was never a contradiction of the ruling: preserved-as-history *is* the
disposition.

**The generalisable bit, and it cuts against a habit this lane has been rewarded for.** CLAUDE.md
§0.1 point 3 says name the falsifier. The failure here was subtler: the falsifier *was* named, in
ED-IN-0171, and then **not run before preparing to edit the thing it guards**. A predicted red is
not evidence. Had I "carefully, deliberately, flagged-not-routed-around" narrowed that pin, I would
have weakened a guard for a conflict that never existed and left a tombstone explaining it. **Run
the guard against the change before you touch the guard.**

### Two defects the previous merge created, both mine

- **ED-IN-0173** — `audit/2026-08-12-alias-index-consolidation/00_plan.md` cited `ED-IN-0173` while
  `id_reservations.yaml` read `next_free: 173`. Cited, never allocated; the register would have
  handed 0173 to the next unrelated allocation — precisely the collision the lane namespace exists
  to prevent. Allocated retroactively (173 → 176). The plan's `## Status:` is **flipped to RATIFIED
  as plan of record** per ED-1094 (Jordan confirmed the flip was mine to make); **Phase A1's five
  semantics questions stay HELD** — ratifying a plan is not ratifying the rulings it requests.
- **ED-IN-0174** — why the BLOCKING anti-fabrication gate missed it, and **the obvious answer is
  wrong**. Everyone's reading, mine included, was "`validate_ed_citations` excludes `audit/` by
  mandate" via `WORKING_PREFIXES`. **A fix aimed there would have landed and changed nothing.**
  `SCAN_PREFIXES` (:120) is `('canon/','designs/','systems/','references/')` — live `audit/` is
  never *selected*, so the mandate exclusion never gets the chance to apply. Measured: the gate
  prints `Scanning 285 doc(s)`, none under `audit/`.
  **Not fixed by widening scope** — the mandate is right on its merits (an audit citing an *open* ED
  is normal), so widening trades a blind spot for false positives on a blocking gate. The new guard
  `tests/valoria/test_audit_plan_ids_are_allocated.py` checks the one property always wrong
  regardless of status: citing a number nobody allocated. Verified to fail on the pre-fix tree.

**Header scope is evidenced, not assumed.** A full-text sweep of 1,143 files returned five hits and
**all five were artifacts** — including `HANDOFF_IN.md:667`, which flagged the sentence
"**ED-WR-0010 NOT allocated**", i.e. the text documenting the non-allocation. Co-occurrence of a
token is not an assertion; a `## Date:` header is a structured claim. That measurement is why the
guard is narrow.

### Filed, not fixed

- **Two more dead-scope instances, in the provenance gate itself** — `WORKING_PREFIXES` names
  `designs/audit/` and `SCAN_PREFIXES` names `designs/`, and `designs/` was retired 2026-07-19.
  ED-IN-0159 §1.6's pattern inside the gate that guards provenance. **Triage input for G5.**
- ⚠ **The IN ledger has run out of archivable slack.** It was at **49,628 / 50,000 (99.3%)** on
  arrival — one entry from a blocking red for whoever committed next, unrelated to their change.
  Archiving every settled id (5 of them: 0163, 0169, 0170, 0171, 0172) only reaches **46,560
  (93%)**, because **44 of the remaining entries are `open`**. The archive remedy is exhausted;
  the next IN session hits a hard wall and cannot archive its way out. This needs a real
  disposition — burn down open entries, split the lane file, or raise the cap with an explicit ED
  — and it is not a next-session-discovers-it-the-hard-way problem.
- **`build_engine_atlas` is order-coupled to prose edits, and the gate is blocking.** Its
  "bare occurrences" table counts identifier hits across the whole repo, so editing *this handoff*
  invalidated a freshly-regenerated atlas and cost a full 10-minute suite run to discover. Working
  rule until it is fixed: **make every prose edit first, regenerate generated artifacts last.**
  This is the generated-artifact gap G6 should absorb — "split the document" is not an available
  remedy for a file no human writes.
- `scope_ratchet` reports **REGRESSED** on `ed.stale` (+115) and `ed.needs_jordan_stale` (+56).
  Pre-existing and not touched here; it is the same open-entry backlog as the row above, seen from
  the other side.

### NEXT, in dependency order (revised by this pass)

- **G5 is now unblocked** — G1+G2+G4 was its stated dependency and **G2 is closed**; only G4
  remains. Feed it the two dead-scope instances above plus ED-IN-0164's 25 zero-match rows. It must
  encode ED-IN-0163's anticipatory rule or its first run demands deleting every correct
  forward-looking policy row.
- **G4 folds into alias-plan Phase A2** — do it once, there, and only after **Wave 3** executes the
  five-parser FORK divergence the alias plan currently asserts from reading rather than running.
- **G6 correction.** The §1.8 finding needs restating before execution: coverage_matrix /
  patch_register / module_contracts are **already single-sourced**, so that half is closed. The
  surviving disagreement is `references/propagation_map.md` at **three** values — gate hardcodes
  `15_000`, `atomization_rules.yaml:164` declares `10000`, and the stale duplicate block at `:230`
  says `5000`. Also absorb the generated-artifact gap: caps apply where "split the document" is not
  an available remedy.
- **G11 unblocked**, four independent sub-items, all re-verified live this session: `systems/combat/sim`
  still in `export_sim_params.SCAN_DIRS`; `validate_ed_citations` in CI (`valoria-ci.yml:127`) but
  **absent from `tools/valoria_local.py`**; 3 broken-anchor probes; the `ci_names_consistency`
  migration.
- **G10 is not executable** and its stated dependency is itself a plan defect: it reads "after S1",
  but **Track S has no S1** — the parenthetical means #304's **B1**. It waits on other lanes.

**HELD FOR JORDAN, unchanged:** #304's six (**#0** `net`/`ob`, gating the degree family 16→1, plus
#1, #1b, #2, #7, #8), the **37 grandfathered `*_index.md` files**, the **`sim_harness`
promote-or-retire call**, and **alias-plan Phase A1's five semantics**. **G2's destination is no
longer on this list** — ruled and executed. The plan's standing recommendation is unchanged: **run
T4 before ruling #1/#1b/#2/#8**; it prices exactly those questions and has never been run.
