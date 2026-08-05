# Repository Keep-Set — the code-first `main`

## Status: RULES RATIFIED (Jordan, in-session 2026-08-04, ED-IN-0125/0127). PER-DIRECTORY
## DISPOSITIONS PROPOSED — the four rulings below are Jordan's words; the table that applies them
## to 16 directories is this document's inference from them and is Jordan-vetoable row by row.
## Class: A — substrate/architecture. **No deletion is authorised by this document.** It defines
## the keep-set; execution is sequenced in §7 and gated on §8.
## Version: v1 — supersedes `tools/build_fork.py`'s `CARRY`/`LEAVE` as the partition of record.

---

## 1. The direction

**`main` is the code-first go-forward repository. The fork/archive receives the outdated prose.**

> "our *fork* is going to hold all the outdated largely-prose work that contaminates our code-based
> work" · "if we keep MAIN for our actual ongoing work, it's a lot cleaner going forward than with a
> fork" — Jordan, 2026-08-04

This is the **evacuate** arm of `audit/2026-08-03-session-oddities.md` §M, now ruled. It inverts what
every prior artifact assumed (that the fork receives the *code*). Consequences, each of which removes
work rather than adding it:

- History of the kept code survives. The `tests/sim/mass_battle` → `systems/mass_battle/canon` re-home
  (J2/J4) becomes a `git mv` that `--follow` traverses, not a copy that truncates history.
- CI, hooks, branch protection and PR history survive untouched.
- What left is one reviewable commit per slice — `git show` *is* the exhaustive list, versus a `LEAVE`
  list plus a manifest that was never in the repo (the E5 unfalsifiability defect).
- Reversal is `git revert`. Re-absorbing a missed file is not a hand-copy.
- No second repository is required: a `pre-evacuation-<date>` tag preserves everything. An archive repo
  is a browsing convenience.
- `git-filter-repo` (not installed), `git subtree split`, and the 11-roots/2-relocations path-rewrite
  cost all drop out of the plan entirely.

**J1 is registered reinterpreted** (ED-IN-0125). Ruled as "`main` does NOT keep moving after the fork"
under the extract framing, its referents swap here: the **archive** freezes, `main` continues.

---

## 2. The rule — three-way, and it cuts on *outdated*, not on *format*

The session's near-miss is worth stating, because the plan and §M both partitioned by format:

> Jordan's sentence discriminates on **outdated**, not on **prose**. Those axes disagree exactly where
> it is expensive.

| Prose | Disposition | Authority |
|---|---|---|
| **No code pair** — `canon/` P-01..P-14, the 14 `godot: no-oracle` module specs | **stays** | **authoritative — it *is* the spec** |
| **Has a code pair** — `systems/` design docs | **stays** | **information only**; code wins (principle 7 / ED-1050) |
| **Has a code pair that has SUPERSEDED it** — `engine/params/` | **evacuates** (2026-08-04) | see the amendment below |
| **Neither** — session audits, process ledgers, generated narrative, superseded proposals | **evacuates** | — |

> "current prose with no code pair stays (philosophical, specs of unimplemented) · prose with code pair
> is information only" — Jordan, 2026-08-04

**Two consequences that a format-based cut would have got wrong:**

1. ~~**`engine/params/` is prose but current.**~~ **AMENDED 2026-08-04 (ED-IN-0139) — `engine/params/`
   EVACUATES.** Jordan: *"params .md are largely useless at this point and I want them gone. code
   should have superseded them all by now"*, and *"provenance can cite to a fork"*.

   The measurement below stands and is left intact, because it is what the amendment had to answer
   rather than something the amendment falsified: zero runtime readers in `engine/` or `systems/`
   (verified with a positive control that passes — the same method finds the real path constructions
   for `key_type_registry_v30.md` at `echo_transport.py:62` and `build_graph.py:50`; two earlier
   attempts at this measurement failed their control and were discarded rather than reported), but
   ~50 **provenance referents** from kept code, including the canon MB engine's core arithmetic
   (`orchestration.py:2438,:2546,:2553` — "Pool = min(Size,Cmd)+Cmd", "Damage = successes ×
   (1+Power)", all `[canonical: params/mass_combat.md PP-233]`).

   **The provenance referents were the whole objection, and the fork-citation ruling dissolves it** —
   an evacuated file is tagged and reachable, so a `[canonical: params/…]` citation still resolves.
   What the ruling does *not* dissolve is losing what the tables assert, so the disposition is gated
   on capture, not on trust: `tools/export_params_constants.py` writes
   `engine/engine_params/params_tables.yaml`, holding all **43 files byte-identically** alongside a
   structured table view (258 tables, 1,367 rows). Lossless **by construction** rather than by the
   parser being complete — and it is not complete: six files (index stubs, `history/`) yield no
   table at all, which is exactly the shape a silent loss would have taken. Falsifier:
   `tests/valoria/test_params_dump.py`, with a positive control.

   J11's premise ("the fork's biggest deletion") therefore holds after all, at 43 files / 584K —
   though `audit/` dwarfs it either way.
2. **`canon/` is prose with no code pair, and is therefore the *most* protected category, not the
   least.** The fork plan's own §4 already said so: *"the prose is the only spec that exists… demoted
   from runtime authority, not from the repo."*

**A second filter is required, because age alone fails.** `audit/2026-07-29-scenario-visualization/` is
**36 MB — 21 PNGs and an 11 MB HTML — and six days old**, so a pure two-week rule keeps it. Add:
**generated artifacts evacuate; their generators stay.** The four `.py` generators in that directory are
wanted (Jordan: "we need visualizations for mass battle and eventually grid-based scene combat on maps")
and arguably belong in `tools/`, not under `audit/`.

---

## 3. Why `CARRY`/`LEAVE` cannot simply be run backwards

**`CARRY ∪ LEAVE` does not partition the tree.** The neither-set is large and load-bearing:
`.github/`, `.githooks/`, `.claude/`, `tools/`, `tests/valoria/`, most of `references/`, `research/`,
`skills/`, and the root files `CLAUDE.md`, `CURRENT.md`, `HANDOFF.md`.

Under **extract** the neither-set defaults to *left behind* — harmless. Under **evacuate**, §M's literal
recommendation (*"`git rm` everything that is not in `CARRY`"*) **deletes it** — the entire enforcement
tier (CLAUDE.md §8), the shipping gate, and the session protocol. **That command must not be run.**

`LEAVE` also conflates two categories that only extraction merges:

1. **Prose contamination** — `audit/`, `arcs/`, most of `proposals/`, `deprecated/`. These evacuate.
2. **Source-repo infrastructure** — `tools/` (*"the fork re-derives what it needs"*) and `tests/valoria/`
   (*"engine/tests comes instead"*). Both rationales are **extraction-only**. Under keep-main,
   `tests/valoria/` is the shipping gate *and* the home of the fork plan's own falsifiers —
   `test_faction_l_reconstruction`, `test_key_graph`, `test_execution_map`,
   `test_public_governance_transfer_key`, `test_morale_write_sweep`. Evacuating them deletes the guards
   every step of the plan cites.

Hence: **this document, authored fresh.** `build_fork.py` survives in a reduced role — see §9.

---

## 4. The keep-set (measured 2026-08-04)

> ## ⚠ THE PARTITION OF RECORD IS NOW `tools/evacuation_plan.py` (ED-IN-0128).
> The table below is the **rationale**, not the authority. It was the authority for exactly one day,
> and a prose partition is the thing this session watched fail twice: `CARRY`/`LEAVE` read like a
> partition and were not one, and a proposal that duplicated live state became a *third* disagreeing
> current-state surface. Two surfaces drift; one owner does not. **Run the tool for the verdict:**
>
> ```
> python3 tools/evacuation_plan.py            # report + per-slice blocking readers
> python3 tools/evacuation_plan.py --check    # totality + contract guard (exit 1 on fail)
> ```
>
> **Current measurement: 3148 tracked files → 1691 KEEP / 33 RELOCATE / 1424 EVACUATE.**
> Do not quote a count from this document — it has been stale three times. Run the tool.
>
> **Deltas since this table was written**, all from Jordan's rulings later the same day:
> - **`dashboard/` AND `workplans/` are both KEPT** (was: evacuate). The coupling this banner
>   previously flagged as unresolved is **CLOSED** (ED-IN-0129): `dashboard_data.py` and
>   `workplan_status.py` keep their inputs, so neither retires and neither reads a deleted tree.
> - **A third verdict, RELOCATE.** Keep/evacuate cannot say *"this is ours but filed in the wrong
>   place"*. Six MB instruments move to `systems/mass_battle/workbench/` — four from
>   `audit/2026-07-29-scenario-visualization/` (`measure_colocation.py` is the standing measurement
>   behind ED-MB-0056/0059, not a session record) and two from
>   `research/diagrams/mass_battle_formations/`. Precedent: `systems/combat/combat_engine_v1/workbench/`.
>   Rendered output does not travel; it regenerates from the relocated source.
> - **"Streamlined" means the WORKING TREE** (Jordan). Clone/pack size is not a goal — see §11.
> - **A keep-rule in the first draft was 20× too broad** and is deleted: it kept *any* `.py` under
>   `audit/` (82 files) to save four visualisation generators. Ordering does the job instead.

| Keep | Size | Files | Basis |
|---|---|---|---|
| `canon/` | 156K | 7 (7 md) | prose, **no code pair** → authoritative spec |
| `engine/` | 1.6M | 89 (38 py) | code |
| ~~`engine/params/`~~ | ~~584K~~ | ~~43 md~~ | **EVACUATES** 2026-08-04 (ED-IN-0139) — captured verbatim into `engine/engine_params/params_tables.yaml` first |
| `systems/` | 6.7M | 326 (115 py, 206 md) | code + its design accompaniment |
| `tools/` | 4.3M | 125 (102 py) | infrastructure / compliance — **99 of 102 reachable** |
| `references/` | 1.5M | 42 | the registries the tools read (implied by "infrastructure") |
| `registers/` | 2.2M | 31 | see §5 — kept, but **restarted** |
| `research/` | 2.7M | 38 (32 md) | named by Jordan |
| `tests/valoria/` | 1.9M | 145 (**0 md**) | the shipping gate + the plan's falsifiers |
| `tests/sim/mass_battle/` | 872K | 28 py, **0 md** | **canon MB engine (J2)** — inside an otherwise-evacuating parent |
| `tests/sim/v32-combat-balance/` | 580K | — | the numpy-free parity oracle |
| `audit/` ≥ **2026-07-01**, renders stripped | — | all of July onward | Jordan widened the two-week rule to the calendar month (ED-IN-0129); ⚠ this is what makes the kept set 52% markdown — see §11 |
| `godot/` | 272K | 27 | the eventual `res://` root (CLAUDE.md §6) |
| `skills/` | 1.4M | 45 | **selectively** — see §6 |
| `.github/`, `.githooks/`, `.claude/`, `CLAUDE.md`, `CURRENT.md`, `HANDOFF.md` | — | — | the enforcement tier and session protocol |

| Evacuate | Size | Basis |
|---|---|---|
| `audit/` < **2026-07-01** + the lane buckets | — | pre-July; the lane buckets are undated so they evacuate too |
| generated renders (**keep the 4 generators**) | 36M | generated-artifact filter |
| `deprecated/` | 7.7M | history; the tag preserves it |
| `tests/sim/` (rest), `tests/stress/`, `tests/sim_framework/` | ~13M, 332 md | prose with neither code pair nor spec role |
| `arcs/` | 1016K | generated narrative content |
| `proposals/` — **selectively**, per §6 | 844K | most are neither |
| `engine/params/` | 584K, 43 md | **ADDED 2026-08-04 (ED-IN-0139)** — code superseded it; tables captured verbatim into `engine/engine_params/params_tables.yaml` first, provenance cites the fork |
| ~~`workplans/`, `dashboard/`~~ | — | **BOTH NOW KEPT** (ED-IN-0129). `workplans/` is the steering surface and carries its own status; `dashboard/` was ruled kept, and keeping `workplans/` closes the coupling that would have left `dashboard_data.py` reading a deleted input |

**Two structural facts the top-level view hides, and they are why the cut is per-file, not per-root:**
`engine/params/` is an evacuating sub-tree inside a keep root; `tests/sim/mass_battle/` is canon code
inside an evacuating root. Both directions occur, and each broke a scan that assumed the top-level
directory was the unit — see ED-IN-0139 for the two false-positive classes that surfaced when
`engine/params/` became the first sub-root evacuation.

---

## 5. `registers/` — kept, but restarted

> "we must start fresh for registers imo" — Jordan, 2026-08-04

**The constraint that shapes how.** **103 files under `engine/` + `systems/` cite `ED-` IDs inline**, and
`tools/validate_ed_citations.py` is a **blocking CI gate**; **30 tools read `registers/`**. A clean-slate
register makes all 103 citations dangle and takes the gate with them.

**Recommended mechanism (PROPOSED):** freeze the existing ledgers as a **read-only snapshot** at
`registers/archive/`, and open a fresh register for all new work. Old citations still resolve; new IDs
start clean; `validate_ed_citations` keeps its ground truth. The alternative — stripping ED citations out
of code — destroys the provenance chain and is not recommended.

**Seed the fresh register with what is still open, not with history.** The still-open set is small.

---

## 6. "Judicious" — the criterion is *subject*, not orphan status

**Measured: 99 of 102 tools are referenced** by CI, hooks, `.claude/`, or another tool. Only three are
not (`build_fork.py`, about to be repurposed; `gen_sigma_parity_goldens.py`, which regenerates a
committed golden — keep; `dead_primitive_census.py`). The dead-tool pruning already happened
(CLAUDE.md §8). **Orphan-hunting yields ~1 tool.**

The real cut is by subject: **a tool retires or re-scopes in the same commit as the tree it serves.**
Tools whose subject is evacuating: `audit_staleness`, `ci_audit_registry_check`, and the parts of
the observability suite that read `proposals/` (`build_proposals`) or the audit corpus
(`build_incompleteness`). ⚠ **Corrected (ED-IN-0129):** `dashboard_data` and `scope_ratchet` are NOT
on this list any more — `workplans/` and `dashboard/` are both kept, so their subjects survive. Same rule for skills: under "prose is information only",
`prose-writer` (676K — half the skills tree) and the editorial/workplan-workflow skills lose their
subject. `valoria-vector-audit` (416K) is the other large one.

**`proposals/` is per-file.** Must stay (load-bearing on kept code): `valoria_fork_plan_of_record_v1.md`
(⚠ it lives in `proposals/`, which `LEAVE` evacuates — a naive sweep deletes the plan governing the
sweep), `repo-reorganization-v1.md` (RATIFIED, execution pending), `pc_formation_system.md`,
`weapon_physics_and_concentration_model.md` §7, `mass_battle_fighting_withdrawal_v1.md`,
`multiunit_envelopment_plan.md`, the personal-combat curriculum. Evacuate: the four 2026-07-17/18
speculative-analysis docs (which self-declare "ratifies nothing"), `pessimist_ners_audit_v1.md`,
`2026-05-25-mechanics-integration-v3_1.md`, `2026-05-16-PC-4.4-unified-success-stress.md`. Already
superseded, no loss: `2026-05-16-faction-audit-followup-plan.md`, `mass_battle_shape_echelon_revamp.md`,
`stub_infill_plan.md`.

⚠ **A held-for-Jordan flag on an evacuated file must survive as a ledger entry, or evacuation silently
un-holds it** — a held item that is not on a register is not held.

---

## 7. Sequence

| # | Step | Reversible? |
|---|---|---|
| 0 | **Rulings first.** Direction + J1 reinterpretation registered (**done** — ED-IN-0125/ED-MB-0064) | n/a |
| 1 | **Register + correct.** The eight C-rulings; the false surfaces; the `--verify-only` guard (**done** — ED-IN-0125/0126) | pure additions |
| 2 | **Carry the 9 attributed MB failures as `xfail(strict)`, citing ED-MB-0061.** ⚠ **This must precede the first deletion** — `main` is CI-red and stays red through the migration, so a deletion-induced breakage would be indistinguishable from background | yes |
| 3 | **Tag `pre-evacuation-<date>`.** Everything after is `git revert`-able | n/a |
| 4 | **Measure before deleting:** the extended J11 (every table cited by kept code, not a 5-table sample); a reader-enumeration grep per candidate directory over `tests/valoria` + `tools/` | n/a |
| 5 | **Jordan rules the line per directory** against §4 | n/a |
| 6 | **Execute in slices, one root per commit** — each commit deleting the tree **plus its dedicated gates/tests plus its alias row** together. `pytest tests/valoria` + a seeded campaign green after every slice. Baseline re-record **last** | yes (revert) |

**Not reversible:** the archive's divergence once anyone commits to it; golden/baseline re-records once
superseding work lands on top; ledger rewrites (append-only — never).

### 7.1 The standing review gate — after EVERY milestone, not at the end (Jordan, 2026-08-04)

> **Every step above closes with an adversarial read-only Fable-5 review — steelmanned — for
> accuracy, logic, and fidelity to this plan.** A step is not complete until that review has run and
> its findings are either applied or explicitly refused with a reason.

**This is a cadence rule, and the cadence is the point.** CLAUDE.md §10 already requires the
agonist→antagonist relay and wires `valoria-critic` (`Read, Grep, Glob` only — independence that is
structural, not declared). What it does not say is *how often*. This does: **per milestone**, not
per programme.

**Why, from this programme's own record rather than from principle.** Three defects in the
separation work were found by adversarial passes and by nothing else, and each was invisible to the
instrument that had just been built and pronounced sound:

| Found by review | What it would have cost |
|---|---|
| The parity oracle was in the evacuate set | A committed golden with no source; a kept CI test unregenerable |
| `readers()` could not see split paths (`os.path.join(REPO, 'audit', …)`) | The blocking-reader counts that sequence the whole deletion were blind to an entire idiom — 45 readers missed |
| `deprecated/` holds 26 files of the BLOCKING ED-citation gate's universe | CI red on the first deletion commit, and the tempting fix destroys the anti-fabrication check |

Each was cheap to check and expensive to have acted on — the exact pattern the fork plan's §12
records and then re-committed. Reviewing only at the end would have caught all three *after* the
work they invalidate.

**Three properties the gate must keep, or it decays into ceremony:**
1. **Read-only by construction.** Route through `valoria-critic`, never a declared-read-only prompt —
   a sentence inside a prompt restricts nothing (ED-IN-0087).
2. **Steelman first.** The reviewer states the strongest case for the work *before* attacking it. A
   finding that only defeats a weak reading is noise, and "this is correct, here is the best argument
   for it" is a valid verdict.
3. **The reviewer's claims are checked too.** Reviews have been wrong here — one reported an ID
   reservation unbumped when it was bumped (it had read a mid-session snapshot). Verify before acting;
   an audit is evidence, not a verdict.

---

## 8. What goes red under mass deletion

Each needs its fix **in the same commit as the deletion**, which is the auditable-deletion property that
made §M prefer evacuation in the first place.

1. **`validate_ed_citations.py`** (blocking) — kept code cites EDs whose evidence lives in `audit/`.
   Needs: ledgers stay (§5), plus alias rows or tolerance for archived evidence paths.
2. **`broken_dependency_checker.py`** — live ledger refs into deleted paths. The mechanism already
   exists: longest-dir-prefix alias resolution in `references/restructure_ledger.md`. **One alias row
   per evacuated root, landed in the deletion commit.**
3. **`ci_co_file_checker.py`** — rule 4 loses `engine/params/` outright now that it evacuates
   (ED-IN-0139): the rule demands a params co-change when a `_v30` doc changes, and its target tree
   will not exist. Retire or re-aim rule 4 in the deletion commit, along with
   `export_params_constants.py --check`, which re-derives from that tree and cannot outlive it; rule 3
   (`coverage_matrix`) breaks on MB edits if the tests-prose corpus goes.
4. **`compliance_check --check-only` + `review_core.py --check`** — the scope ratchet will report a
   large delta (J13 already trips it). Re-record the baseline **after** the slices are final, with an
   explicit ED and a loud call-out.
5. **`canonical_sources.yaml` pins / `freshness_gate`** — ~12 pins already stale; prune the index per slice.
6. **SessionStart banner** (`session_status.py`, `workplan_status.py`) — reads root `HANDOFF.md` and
   `workplans/workplan_v6_progress.yaml`. **Evacuate `workplans/` and every session boots against a
   missing file.** Keep, or rewire the banner first.
7. **`tests/valoria/` itself** — any test reading an evacuated tree fails. Step 4's grep is the guard.
8. **`dashboard/` + `audit-refresh.yml` + `build_proposals.py`** — surfaces `proposals/` **by location**;
   retire or re-point in the same commit.

---

## 9. `build_fork.py`'s new role

It is **no longer the executor**. It survives as:

1. **The keep-set guard.** `contract_coverage()` — which takes no argument and reads the *source* repo —
   reinterprets cleanly as *"nothing with a contract or a stub may be evacuated"*, run against the
   post-deletion tree. Its docstring already states the trap it exists to catch: the tempting "minimal
   fork" of just the 58 runtime files would silently drop 14 units that have a contract but no code yet.
2. **The source of per-root rationale strings** for §4.

Its `--verify-only` empty-scan defect is fixed under ED-IN-0126 (`_scanned_py`, mutation-verified in
`tests/valoria/test_build_fork_scan_guard.py`).

---

## 10. Open calls

- **§5's archive-snapshot mechanism** for restarting `registers/` — recommended, not ruled.
- **Per-file dispositions in §6** for `skills/` and `proposals/`.
- **`godot/`'s four stale pre-`d+σ` docs** (ED-1054 banners) — evacuate individually, or keep with the
  port target? The unit of decision is the file, not the root.
- ~~**Where provenance authority migrates** if `engine/params/` is ever revisited~~ — **RULED
  2026-08-04 (ED-IN-0139).** It was revisited immediately: `engine/params/` evacuates, and *"provenance
  can cite to a fork"* (Jordan), so the ~50 `[canonical: params/…]` referents in kept code keep
  resolving against the evacuation tag rather than needing to be re-pointed. The typed layer
  (`engine/engine_params/sim_params.json` citation fields + the plan §5 ratchet) remains the natural
  successor for **new** provenance; migrating the existing citations onto it is optional cleanup, not
  a precondition of the deletion.

---

## 11. "Streamlined" means the working tree — and history rewriting is the wrong tool here

> "streamlined as in working tree. repo size irrelevant to me I think unless it impacts Claude code
> performance?" — Jordan, 2026-08-04

**It does not meaningfully impact it, and the deletion delivers essentially all the benefit.**

Measured: the pack is **51 MiB**; the working tree is **121 MB**. Deleting files removes them from the
tree while every byte stays in history, so a fresh clone is the same size afterwards. That sounds like
a gap and is not one, because the things that actually cost an agent are working-tree properties:

- **Search breadth.** Every `Grep`/`Glob` walks the *working tree* — 3,146 files today, ~1,155 after.
  History is never scanned.
- **Result dilution, which is the real cost.** Searching for a current fact today returns hits from 966
  stale audit markdowns. That is not a slowdown, it is a *correctness* hazard, and it is the documented
  mechanism behind several errors this session catalogued — including one of mine, where a `[DRIFT]`
  docstring naming a path retired 2026-07-21 was read as current state.
- **Context.** Only files actually read enter context. Pack size never does.

So evacuation fixes the expensive problem completely. A history rewrite would buy ~51 MiB of one-off
clone time and cost:

- **Every commit SHA in the repository changes.** This repo *cites SHAs* —
  `references/canonical_sources.yaml`'s `canonical_sha__*` pins, `freshness_gate`, and commit
  references throughout the ledgers. A rewrite invalidates all of them at once.
- `git-filter-repo` is **not installed**, and the operation is not `git revert`-able.

**Recommendation: do not rewrite history. Deletion plus a `pre-evacuation-<date>` tag is correct**, and
the tag is what makes the archive real. This is the reverse of the extract-era reasoning, where
history-preserving extraction needed `filter-repo` precisely *because* the code was moving to a new
repo; under keep-main the code never moves, so the problem disappears rather than being solved.
