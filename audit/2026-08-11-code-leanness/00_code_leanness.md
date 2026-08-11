# Code leanness — findings, corrections, and the merged consolidation plan (ED-IN-0159)

## Status: REFERENCE — observation with evidence; nothing ruled, nothing executed

## Date: 2026-08-11 · Lane: IN (cross-cutting) · Baseline: `ff9e3e3` (post-#302, post-#304)

**Mission** (Jordan, 2026-08-11): *"make this project as lean as possible without sacrificing
mechanisms"*, where lean means **fewer files to continually track, review, edit and audit** — not
fewer bytes. Scope is **code**: `tools/`, `.githooks/`, `skills/*/scripts/`, `engine/`,
`systems/*/sim/`, `tests/`, and the `.py` under `audit/`. Registers, logs and lane files are out of
scope — chunking those is fine.

**This is a full rewrite.** It supersedes every earlier revision of this document (`ed732f5`,
`cbc7da9`). Findings are stated **once, in final adjudicated form**, with retractions inline rather
than in an appendix; the plan is **one current plan**, not a plan plus a list of amendments.

**Provenance of the findings below.** Three passes, deliberately different in kind:

1. **This session (Opus, Bash)** — the duplication census over `tools/`.
2. **A `valoria-critic` read-only pass (Fable, Read/Grep/Glob)** — attacked pass 1 as prior art.
3. **PR #304** (merged `655c9c5`), an independent session auditing all 115 `systems/` modules, plus a
   second `valoria-critic` pass reconciling it against passes 1–2.

Passes 2 and 3 each **overturned findings from pass 1**. Those overturns are §2 and are the most
useful part of this document.

**Instrument.** `duplication_census.py`, beside this file. Every quantitative claim here is
reproduced by it; a number it cannot reproduce is withdrawn. It **self-invalidates** (exit 1) if the
Status readers ever agree, if `params_tables.yaml` loses its original-path key, if any cited
`params/` path starts resolving, or if `next_free` falls behind its lane.

**Verification at this baseline.** `pytest tests/valoria` 1775 passed / 23 skipped / 14 xfailed /
1 xpassed · `valoria_local --staged` all gates passed · `ci_claim_provenance_check` OK ·
`validate_ed_citations` 0 violations · `build_engine_atlas --check` current.

---

## 1. Findings

Population for §1.1–1.3: **118 `.py` modules** under `tools/`, `tools/observability/`,
`tools/sim_harness/`, `.githooks/`, `skills/*/scripts/`. **State the denominator when quoting these**
— §2.2 explains why.

### 1.1 The shared libraries exist, are correct, and were never adopted

| library | owns | imported by |
|---|---|---:|
| `tools/ci_common.py` | changed-file/diff plumbing, `read_text`, sim-reference roots | **11 / 118** |
| `tools/observability/obs_core.py` | ledger read, lane roster, `STATUS_RE`, needs-Jordan vocab, JS-bundle writer | **9 / 118** |
| `tools/names.py` | naming-gate primitives | **9 / 118** |
| `tools/registry.py` | register access | **2 / 118** |
| `tools/pathres.py` | alias resolution over `restructure_ledger.md` | **1 / 118** |

The problem is not an absent abstraction. `obs_core` was built precisely to end this — its header
documents the five primitives it consolidated — and it reaches 8% of the tooling.

### 1.2 Primitive re-implementation

| primitive | independent implementations |
|---|---:|
| repo-root / path anchoring | **53**, in **15 distinct spellings** |
| YAML register load (`yaml.safe_load`) | **44** |
| staged/changed-file listing | 10 |
| `## Status:` parsing | 9 |
| the 9-lane roster | 9 |
| `restructure_ledger.md` parsing | 9 mention it; **4 genuinely parse it** (§2.3) |
| editorial-ledger read | 8 |
| `id_reservations` read | 8 |
| token estimation (`len//4`) | 6 |
| `PP-NNN` / `ED-NNN` regex | 6 |

Top repo-root spellings: `os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` x24 ·
`Path(__file__).resolve().parents[1]` x6 · `os.path.dirname(os.path.abspath(__file__))` x5 ·
`os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))` x4 · eleven more, 1–4 each.
`ci_common` already computes it — as `_REPO`, **underscore-private**, so it is not offered.

### 1.3 Where the duplicates disagree — the consistency cost, measured

Duplication that agrees is cost; duplication that disagrees is a defect. I tested for divergence
rather than assuming it.

**(a) `## Status:` — five live regexes, disagreeing on real files.**

| parser | pattern |
|---|---|
| `dashboard_data` | `^#{1,3}\s*Status:` — needs a hash, no space before the colon |
| `build_identifier_census` | `^##\s*Status:` — **exactly two** hashes |
| `ci_generation_consistency` | `#{0,3}\s*Status\s*:` |
| `obs_core.STATUS_RE` | `^#{0,3}\s*Status\s*:` — the canonical one |
| `build_incompleteness` | `#{0,4}\s*Status\s*:` + a status vocabulary |

Across **557 tracked `.md`**: **205 carry a Status line · 198 read identically by all five ·
7 DISPUTED.** The disputed set has been **stable at exactly 7 across four re-runs** spanning two
merges:

- `workplans/valoria_master_workplan_v6.md` — **the live steering surface**
- `systems/ui/valoria_ui_ux_v4.md` · `references/restructure_ledger.md`
- `engine/sim_reference_CONVENTIONS.md` · `systems/combat/combat_engine_v1/README.md`
- `skills/valoria-simulator/SKILL.md`
- `audit/2026-08-06-social-contest-three-lens-audit/sources/03_consolidation.md`

Six are invisible to **both** `dashboard_data` and `build_identifier_census`. The failure is silent:
the dashboard renders a corpus omitting the master workplan's status and reports no error. **This is
the residue after `obs_core` already consolidated this primitive** — its header records the
divergence it fixed (a GO-lane undercount, disagreeing Status regexes), and it re-grew.

**The consolidation delta is two-sided.** `build_incompleteness` **over**-matches the canonical owner
(0–4 hashes, leading whitespace tolerated). Collapsing onto `obs_core.STATUS_RE` therefore *adds*
documents to two parsers' view and can *remove* them from a third's. The migration test must assert
**both** directions, or the incompleteness census silently shrinks. (Found by the #304 reconciliation;
my first statement of this finding was one-sided.)

**(b) The 9-lane roster — 8 sites, agreeing today, diverged before.** Verbatim
`("MB","PC","FI","SC","FA","WR","IN","GO","SE")` in `ci_workplan_pointer_check`,
`broken_dependency_checker`, `handoff_atomize`, `validate_ed_citations`,
`currency_consistency_check`, plus `obs_core`'s canonical copy and two derived spellings. They agree
**now**; `obs_core`'s header records that one previously undercounted GO. **Adding a tenth lane means
editing 8 files.**

**(c) The TN-7 dice constants — and both audits' censuses were partial.** `MU_PER_DIE = 0.40` /
`SD_PER_DIE = 0.80` are hardcoded as **named constants** in `engine/autoload/sigma_leverage.py:100-101`
and `audit/2026-06-03-contest-groundup/engine.py`, and as an **unnamed tuple** `7: (0.40, 0.800)` in
`engine/autoload/dice_engine.py:56,60`, `tests/sim/v32-combat-balance/m1_dice_sigma_core.py:28` and
`sigma_leverage.py:75`. #304 independently found a sixth — the canon-twin `_SIG` at
`tests/sim/mass_battle/resolution.py:195` — which I missed, while it missed two I found. **The union
is ~7 sites; neither census was complete.** A grep for the constant *name* finds two of seven.
`m1_dice_sigma_core.py` is the frozen parity oracle — do not touch it (§6 item 8).

### 1.4 The provenance defect — 354 citations to paths that left the tree

Live `.py` files carry **354 citations of `params/…` paths across 74 files and 12 distinct paths**,
in the form `# [canonical: params/core.md §Expected Value (per die), TN7]` — the annotation the
anti-fabrication gate is built around, by which a constant in code names its authority.

| path | citations | | path | citations |
|---|---:|---|---|---:|
| `params/core.md` | 168 | | `params/threadwork.md` | 5 |
| `params/contest.md` | 102 | | `params/x.md` | 5 |
| `params/mass_combat.md` | 49 | | `params/combat.md` | 2 |
| `params/factions/stats_1_7_scale.md` | 10 | | 4 more | 1 each |
| `params/factions.md` | 9 | | | |

**Every one of the twelve is absent from the tree.** `params/` aliases to `engine/params/`, evacuated
2026-08-05 (ED-IN-0145) to fork ref `c451bcb`. So every constant in the executable model cites an
authority that is not in the repository.

**I first published this as "168 across 46 files" — 47% of the class.** I counted one basename and
called it the defect; the #304 reconciliation found `params/factions.md` also cited and also
evacuated, and widening the instrument found ten more paths. The instrument now measures the class and
fails if any path starts resolving.

**The remedy is in-tree and byte-faithful.** ED-IN-0139 captured all 43 param files into
`engine/engine_params/params_tables.yaml` (669 KB) *before* the evacuation, keyed by original path —
it literally contains `engine/params/bg/core.md:` as a key. Only the pointer is stale. This is
CLAUDE.md §0's PP-NNN disease one register down: the provenance layer of the code.

### 1.5 Dead code inside a blocking gate's file

`tools/compliance_check.py` calls **two functions that do not exist**: `_lazy_import()` at `:165` and
`check_all()` at `:306` (`grep -c 'def _lazy_import\|def check_all'` gives **0**). Executed:

```
$ python3 tools/compliance_check.py
  File "tools/compliance_check.py", line 306, in <module>
    violations = check_all()
NameError: name 'check_all' is not defined
```

The live CI mode (`--check-only --repo-state .`) is fully inline and unaffected — which is why this
survived — but the file is half dead-on-arrival, and it is a **blocking gate's** file. Its own
docstring at `:10` records them as leftovers of ED-IN-0145's excision.

### 1.6 Dead scope in blocking gates — one pattern, at least six instances

`compliance_check`'s dead branch is not isolated. Combining both audits' instances:

- `ci_co_file_checker.py:90` builds candidates under **evacuated `engine/params/`** — Rule 4 has
  examined zero items since 2026-08-05 (#304 D4).
- `atomization_rules.yaml:243-249` — the only skeleton/index policy rule targets **retired
  `designs/`**, so it matches nothing.
- `_check_index` reads `require_index_above` (`compliance_check.py:166`), a key absent from the policy
  file, whose rule uses `require_skeleton_above` (`:245`).
- `ci_editorial_checker`'s `arcs/` scope, `ci_naming_check`'s `engine/params` entry, and
  `ci_register_size_check`'s rows for evacuated files (#304 C2's sweep).

**Neither audit found the other's instances.** #304's C4 meta-guard — a vitality check that a blocking
validator's scope still matches something — is the recurrence guard for the whole class, and is the
single highest-value new item either plan contains.

### 1.7 Three dead or self-retiring tools

- **`index_gen.py`** — zero importers; only CI presence is `py_compile`; its sole artifact carries
  `<!-- auto-generated by index_gen.py — 2026-05-10T20:34:39Z -->`
  (`registers/patch_register_index.md:3`), untouched for three months.
- **`doc_index_gen.py`** — same profile; its **37 outputs** at `systems/**/*_index.md` have **no
  freshness guard of any kind**. The 37 files are **grandfathered by the 2026-07-26 ruling** — a
  Jordan call, not an edit. Retire the generator without deleting them.
- **`ci_names_consistency.py`** — a self-declared migration babysitter (`:4-9`): it exists only while
  two registries carry mirror `name`/`canonical` fields, and says removing them is the follow-up.

**Keep `valoria_rename.py`** — it is the designated executor of
`proposals/canonical_nomenclature_v1.md:231`, and looks dead only through the same `py_compile`
artefact (§2.2).

### 1.8 Two blocking size-cap gates check the same files twice — and disagree on the cap

`compliance_check`'s CI mode walks every `.md`/`.yaml` against `atomization_rules.yaml` (`:257-284`).
`ci_register_size_check` enforces a hand-maintained `THRESHOLDS` dict, three of whose entries are read
*from that same file* precisely because they kept drifting (`:39-48`, recording three incidents,
ED-IN-0097). `tests/coverage_matrix.md`, `patch_register_active.yaml` and `module_contracts.yaml` are
size-checked **twice per CI run by two tools**.

**They disagree on the value** (#304 C9, verified): the gate says **15,000**
(`ci_register_size_check.py:70`), the policy file says **10,000** (`atomization_rules.yaml:169-170`),
and a **stale duplicate block** at `:231-232` says 5,000.

**Mechanism that must survive a merge:** the `.jsonl` caps are unique to `ci_register_size_check`
(`:81-125`; compliance's walk skips non-`.md`/`.yaml` at `:259`), and `ci_register_size_check` runs in
`valoria_local` while `compliance_check` deliberately does not (`ci_checks_registry.yaml:262` —
"local-green != compliance-green"). A merged gate must carry both or coverage regresses.

### 1.9 Two always-exit-0 tools sit in the blocking tier

`ci_audit_registry_check` ("Always exits 0 by design", `ci_checks_registry.yaml:113`) at
`valoria-ci.yml:132`, and `ci_supersession_check` ("ALWAYS return 0", `ci_supersession_check.py:66`)
at `:129`. Moving both to `validators-report` changes no behaviour and makes the blocking tier's
membership truthful. **Constraint (#304 C3):** the workflow edit and the registry `ci_job` flip must
be **one commit**, or `broken_dependency_checker` reds.

### 1.10 `ci_checks_registry.yaml` documents a file that does not exist

`valoria_hooks.py` is **absent from the tree** (`find` returns nothing), yet the registry — which
calls itself the single source of truth — references it **5 times**: its level-4 definition (`:14`),
its field definitions (`:21-22`), and an `in_session_hooks` section (`:345-428`, ~18 hooks, some
describing the ED-1084-retired checkpoint machinery at `:422-424`). Every `paired_hook:` field on the
live CI entries points into it. ~90 lines describing an enforcement level that does not exist.

### 1.11 The audit probe scripts are unpromoted instruments, not dead one-offs

I first listed the 42 `.py` under `audit/` as clean deletion candidates. Reading them refuted it.
**39 of 42 have path anchors that all resolve**; three are broken
(`wp_reach_authority_measurement.py`, `wt_spd_deleak_measurement.py` — both reaching for
pre-restructure `designs/scene/combat_engine_v1` — and `stageBC_test_obb_contact_toi.py`).

I executed one. `stress_battery.py` runs in ~110 s: **22 checks, 21 PASS, 1 FAIL** —
`[FAIL] mirror-match ~50% (N=400): worst dev=0.500 @ arming/heavy p=0.000`. A correctness-invariant
battery covering determinism, mirror symmetry, numerical sanity, attribute monotonicity, the upset cap
and bounded runtime **exists, runs today, reports a failure, and is in no CI job.**

**Class B is this mission's own tooling:** `flag_ablation.py` (leave-one-out per boolean flag —
*"a flag whose removal HURTS is load-bearing; a flag whose removal HELPS is actively costing the
result"*), `harness.py` (every factor to WIRED-LIVE / WIRED-SITUATIONAL / **DEAD**), `interaction.py`
(INDEPENDENT / MASKING / SYNERGY / ANTAGONISM), `reachability_sweep.py`. **The instrument that answers
"what can we cut without sacrificing mechanisms" already exists and is unrun** — and it measures
*behavioural* deadness, which §2.2 establishes is strictly better than the referential deadness both
of the repo's automated censuses attempt. CLAUDE.md §10's emergence-auditor candidate is blocked on
*"once ablation is runnable"*; it is.

### 1.12 `tests/valoria` — no duplicate modules found; ~40 repeated bootstrap blocks

A 15-of-153 adversarially-selected sample found **no superseded or duplicate-fact modules**: every
suspicious pair resolved to distinct, ED-cited, live purposes (three "pins" files guard three
different facts; three geometry files, three different EDs). The real duplication is boilerplate —
`conftest.py` is only the KNOWN_RED register (`:35-65`), so **32 files repeat an identical
`ENGINE = …combat_engine_v1` + `sys.path.insert` block**, at least 7 more repeat a `_SIM` block, and
~10 define local `_unit()` factories with differing defaults.

**The instrument to finish this exists**: `references/test_register.json` — 132 files / 1,186 tests
with a per-row "what it guards", generated and drift-gated blocking since ED-IN-0142. My "left out of
scope because pytest collection defeats the method" was true of *my* method, not of the repo's.

### 1.13 A forked copy of the resolution core

`audit/2026-06-03-contest-groundup/engine.py` (59 lines) reimplements the core resolver —
`MU_PER_DIE`, `SD_PER_DIE`, `OVERWHELM_SIGMA`, `eff_sigma`, `net_boost`, the ED-884/ED-934 mu-shift
semantics, the P-232 Ob floor — with constants hardcoded. It cites ED and P numbers, so a future
reader would reasonably treat its output as authoritative. Values match live today; nothing would
report it if they stopped.

---

## 2. Overturned — and what each error teaches

### 2.1 The four "possibly-uncalled" factions modules are reached; my ranking signal was invalid

I named `charter_liberties`, `home_sanctuary`, `hafenmark_equipment` and `infrastructure_reclamation`
as where to start tracing, on the strength of **two independent methods agreeing** they were uncalled
— invoking §10's rank-by-independent-rediscovery.

**All four are reached by a blocking test.** `engine/tests/test_pipeline_reach.py:749-755` lists them
in `_OI17_FULL_MODULE_ENTRYPOINTS`; `test_oi17_full_module_conversions_are_stub_wired` (`:767-779`)
asserts each resolves as `stub_wired`; re-run here, **1 passed**. All four are `stubwire.stub_resolve`
no-ops whose docstrings carry Jordan directives recorded nowhere else — `home_sanctuary.py:5` (the T9
Ob +4 / 12-season exit condition), `infrastructure_reclamation.py:5` (the attacker/defender pool
formula). **Deleting any fails CI and destroys design content.**

**The reasoning error matters more than the wrong answer.** Both methods were blind to *the same
thing* — `test_pipeline_reach.py` dispatches by **string module path**, invisible to an AST import
graph and to an `import X` grep alike. Independent rediscovery ranks only when the blind spots
*differ*; mine were correlated, so the agreement carried no information. I named this hazard one
section before walking into it.

### 2.2 Both of the repo's dead-code censuses are wrong — in opposite directions

- **`build_apparatus_registry.py:213-220`** tags a tool `ci:<workflow>` if its **basename appears
  anywhere in the workflow text**, and `:306-307` sets `orphaned=False` for any such tag. The
  syntax-check job is a bare `py_compile` list — so **being compiled counts as being invoked**.
  Confirmed: the registry reports `index_gen.py`, `atomizer.py`, `doc_index_gen.py` and
  `valoria_rename.py` as "Invoked by ci:valoria-ci.yml", while its *own* row 165 enumerating what that
  workflow actually invokes lists none of them. So **orphans are UNDERCOUNTED; cull candidates
  hidden.**
- **`dead_primitive_census.py`** has **no stub concept at all** (`grep stub_resolve` returns nothing),
  so it reports `stub_resolve` bodies as dead functions. #304 measured 8 of its 55 `systems/`-scoped
  "dead functions" to be exactly that; corrected figure **47**. So **deadness is INFLATED; false cull
  candidates produced.** (Its default scope is wider — `tests/sim/mass_battle` + `engine` + `systems`
  — and reports 72/48 today. Both figures are consistent; state the scope when quoting either.)

**Same defect class, opposite signs: each pattern-matches a proxy for the property it claims.** One
would have had us keep dead things, the other delete declared interfaces a ratchet exists to track.

**This invalidated a figure I published.** The consolidation sweep (ED-IN-0158) corrected CLAUDE.md's
stale "36 of 106 modules have zero automated callers" by citing "123 entries, 6 orphaned". The
staleness stands; **my replacement figure does not.** The honest statement is that **no valid orphan
count is currently computed by anything.**

**Hierarchy of evidence, for anyone acting on deadness:** behavioural (`harness.py`'s DEAD verdict)
beats hand-filtered referential (#304's corrected 47+39), which beats raw instrument output (both
invalid).

### 2.3 `pathres`'s "sole parser" claim is no longer false — withdraw the rhetorical charge

I wrote that `pathres.py` "declares itself the SOLE PARSER and is not", and invoked CLAUDE.md §8's
"a single-owner comment asserting a property the tree lacks is worse than no comment".

**The comment now reads honestly.** `tools/pathres.py:121-127`: *"**INTENDED** sole parser of
references/restructure_ledger.md, **not yet the actual one**. Four independent parsers still exist and
have not been migrated onto this module"* — and it names all four
(`broken_dependency_checker`, `ci_claude_workflow_paths`, and two `skills/valoria-vector-audit/`
modules), closing with *"'sole parser' is aspirational"*.

**The charge is withdrawn; the consolidation is still undone.** My "6 genuinely parse it" was also
high — three of my six only mention the filename (`build_incompleteness` *excludes* it from a scan;
`evacuation_plan`'s hits are a comment and a print string). **The real number is 4 to migrate.**

### 2.4 The instrument counted itself

Its source contains the literals `params/core.md`, `MU_PER_DIE` and `## Status:` **as the patterns it
searches for**, and it lives under `audit/` — so it counted itself as a citing module, a constant
hardcoding and a probe script, inflating three published figures by one each (172/47, 3, 42). Caught
only because the counts moved after a merge and the merge could not account for all of it.
Self-exclusion restored the originals. **A census that includes itself in its own population is a
measurement defect, not a rounding error.**

### 2.5 Refuted before publication — the editorial-ledger readers

A first pass flagged that of 15 ledger-reading modules only 5 read the lane files, implying ten tools
see pre-cutover flat IDs only. **Refuted on inspection**: most use the glob
`editorial_ledger*.jsonl`, which matches every lane file; my detector only recognised explicit lane
interpolation. Of three genuine suspects, `index_gen.py`'s mentions are in a docstring describing its
own superseded behaviour, `ci_claim_provenance_check.py`'s two filenames are a hardcoded
provenance-anchor map, and `currency_consistency_check.py` globs all lane files at `:152` while
documenting its flat-file limitation at `:129-130`. **No confirmed divergence.** Recorded because
CLAUDE.md §8 still describes that tool as having a "flat-file-only ledger reader" — now at best
half-true.

---

## 3. Adjudication of PR #304 — where it corrects me, and where I correct it

#304 (`655c9c5`) audited all 115 `systems/` modules (25,116 LOC) and shipped a divergence audit with
a 887-line remediation plan and its own verifier. **Its scope and mine are near-disjoint**, which is
the most important thing about it.

### 3.1 The two theses compose; neither refutes the other

#304's headline is that `systems/` has **no copy-paste problem** — 7 redundant copies in 25k LOC —
but an **idiom-divergence** problem. My thesis is that `tools/` is full of duplicated idioms. These
are not in tension: **the methods are mutually blind.** Structural function-body fingerprinting cannot
count one-line `REPO = …` assignments or `yaml.safe_load` calls; a token census cannot see sixteen
degree ladders that share no token. And #304's own lens 7 covered `tools/` and **corroborated me**
(12 duplicated rules, 23 walkers with bespoke exclusions).

**The corpus has both diseases, segregated by tree:** `systems/` diverges in *approach* (many
implementations of one rule, textually different); `tools/` duplicates in *text* (many copies of one
idiom, textually near-identical). Each session's method would have missed the other tree's disease.

### 3.2 The binding constraint this puts on my Phase 1

My "one owner per primitive" recipe is valid **only where the copies agree today** — repo-root, YAML
load, lane roster, token estimation, ID regex, where the expected delta is *none*. #304's degree
ladders **do not agree**: one rule has **16 producers, 6 vocabularies, 5 Overwhelming formulas**, and
four *incompatible* meanings of the parameter named `net` (raw successes / Ob pre-subtracted / opposed
margin / the opponent's roll), all typed `(int, int) -> str`. Nothing distinguishes them.

**There, folding is a behaviour change, not a cleanup** — it converts visible divergence into
invisible divergence. #304's `A7 LEAVE list` (six producers that look like copies and are not) must
survive any consolidation. A leanness-motivated merge of `sigma_leverage.degree` or
`faction_action._degree` would sacrifice mechanisms, which is the one thing the mission forbids.

### 3.3 Where #304 is wrong: `altonian_reinforcements` did **not** miss the stubwire sweep

#304 states `systems/mass_battle/sim/altonian_reinforcements.py` "missed the OI-17 stubwire conversion
sweep — it still raises where all ~19 siblings return a governed no-op," and plans its conversion.
**Verified against the tree, this is incorrect**, and both read-only passes accepted it.

`engine/tests/test_pipeline_reach.py:166` carries an `XFAIL_MANIFEST` row
`"altonian-reinforcements-handoff"`, kind **`accepted-handoff`**, reason: *"the ONE accepted
cross-session handoff (MB-owned file) — conversion is MB plan §12 I1, not this program's job (critic
F9: an IN exit criterion may not be hostage to another session's schedule)."* Line `:747` has the
OI-17 roster **explicitly exclude** it. And `test_only_accepted_handoff_still_raises_unconditionally`
(`:783-793`) asserts it **must still raise**, instructing that when MB converts it you *delete the
test and the manifest row rather than update the assertion*. **The test passes.**

**Acting on #304's item would break a green guard and cross a lane boundary.** The item is struck from
the merged plan. (#304's appendix separately marks the module `tested: Y` — true only under its
referenced-by-name definition; the function unconditionally raises. Do not read that Y as
exercised-green.)

### 3.4 Where #304 corrects itself, and figures not to quote

- **"Nine degree implementations"** (the PR headline) is **superseded by #304's own divergence audit**,
  which calls it *"materially incomplete — at least seven more exist"* and reports **16 producers**
  (`00_divergence_findings.md:50,59,191`). Quoting "nine" repeats a withdrawn claim.
- **Its location count is inconsistent three ways**: `00_divergence_findings.md:24` says "168/168 OK",
  `02_remediation_plan.md:5-6` says "196 locations, 196/196 verified", `verify_locations.py:6` says
  "these 400 sites". **The tsv has 196 data rows**, and I ran the verifier: **196 rows, 196 OK, 55
  groups.** The 196 figure is correct; the findings doc is stale.
- **Numeric coincidence:** "168" is both #304's stale row count and my `params/core.md` citation
  count. Unrelated. Do not merge them.
- `DISPATCH_COMBAT_BRIDGE` is cited at four different line numbers across four documents; the runtime
  default is `engine/mc_v18.py:79-81`.

### 3.5 Where #304 is better evidenced than me

- **The deprecated combat resolver.** I concluded "flag ratification, not a leanness edit, nothing to
  do." #304 found more: `tools/export_sim_params.py:36` **publishes the superseded model as typed
  truth** beside `combat_engine_v1.json`. Dropping `systems/combat/sim` from `SCAN_DIRS` and
  regenerating is **not blocked** on the flag ruling. My "nothing to do" was wrong.
- **Its stub framing matches mine from the other side**: it caught the *instrument* miscounting stubs
  as dead; I caught my own *methods* miscounting stubs as unreached.
- **The rng fallback.** 16 sites define "no rng supplied" in two non-equivalent ways. I proved the
  mechanism: under `random.seed(42)` twice, `random.Random()` yields 0.349522 then 0.678761
  (**not reproducible**); `random.random()` yields 0.639427 both times (**reproducible**).
  `engine/autoload/dice_engine.py` — the core dice resolver — uses the former. **This is my §1.2
  pattern one layer down, and there the copies disagree.**
- **36 `engine/` to `systems/` downward import edges**, contradicting declared upward-only layering —
  count verified exactly. Acyclicity is preserved by import *placement* (11 lazy in-function imports),
  not by structure.
- A **faction-roster literal duplicated 4x** (`game_state.py:51` owner; `mc_v18.py:323`,
  `npe.py:245,298`, `temperaments.py:72`) — my lane-roster pattern one layer down, **planned by
  nobody**.
- **`skills/valoria-dice-model/valoria_dice.py:45` is a live forked degree ladder** (no >=3 floor,
  Ob-10 not Ob-20) — cross-layer duplication between `skills/` and the engine, in neither plan.

### 3.6 A live confirmation of the sweep's F2, which my own commit caused

ED-IN-0158's F2 found `ci_audit_registry_check` structurally blind. #304 then added **two** audit
units; **neither is registered**; the gate reports **OK**.

Mechanism, `tools/ci_audit_registry_check.py:78`: `if date > max_registered_date` — **strictly
greater**. My registry row is dated 2026-08-11; both new units are dated 2026-08-11. They are
invisible. **The gate is not merely tail-blind — it is same-day blind, and every registration makes it
blinder** by advancing the max date. Registering an audit is the act that hides its same-day siblings.

---

## 4. The merged plan

**One plan, replacing both.** Three tracks. Steps within a track are ordered; **G** and **S** may run
concurrently in different lanes. Every step names the mechanism at risk, because "without sacrificing
mechanisms" is the binding constraint.

**Governing rule (from §3.2):** collapse to one owner **only where the copies agree today**. Where
they disagree, a ruling comes first and the merge is a behaviour change.

**Governing discipline (CLAUDE.md §8, already ruled):** every migration of a blocking gate ships with
its own expected-delta test. This is why the plan is ~20 small changes, not one refactor.

### Track G — gates and tooling (IN lane)

| # | step | depends on | mechanism at risk |
|---|---|---|---|
| **G1** | Excise `compliance_check.py`'s dead branch (`_lazy_import`, `check_all`, the interactive path); update `test_compliance_on_exceed_vocabulary.py:98-99` in the same commit | — | None — the live `--check-only` mode is inline |
| **G2** | **Dead-scope sweep as ONE pattern** (§1.6): retire `ci_co_file_checker` Rule 4, fix the three siblings, delete the `designs/` policy row, retire `atomizer`/`doc_index_gen`/`index_gen` to `deprecated/tools/` | G1 | Rule 4's co-change pressure — #304 argues three code-to-artifact gates now carry it. **The 37 `*_index.md` files are grandfathered (2026-07-26 ruling) — HELD, do not delete with the generator** |
| **G3** | Move the two always-exit-0 gates to `validators-report`; flip their registry `ci_job` rows **in the same commit**; prune the `valoria_hooks.py` ghosts (§1.10) | — | Split the commit and `broken_dependency_checker` reds |
| **G4** | Make `pathres` the owner: migrate the **four** parsers it names (§2.3); add #304's two-tier walk exclusions; fix the TREES roster 17 to 19 | — | `broken_dependency_checker`'s inclusion of `deprecated/` is **correct** — live ledger entries cite the ED archives, the anti-fabrication universe. The two-tier design preserves it deliberately |
| **G5** | **#304's C4 meta-guard** — a vitality check that every blocking validator's scope still matches something | G1, G2, G4 | None. If its first run reds on `review_core.py`, that is a finding |
| **G6** | Size caps, one sequence: adopt the policy cap and delete the stale duplicate block (`atomization_rules.yaml:231-232`), **then** merge the two gates | G2 | **The `.jsonl` caps and the local-tier coverage** (§1.8). The merged gate must carry both or coverage regresses |
| **G7** | The mechanical one-owner migrations — `REPO`, YAML load, `LANES`, `tokens()`, `ID_RE`, ledger read — each with an expected-delta test asserting **delta = none**; gates last | — | Any behaviour change here is a bug, not a delta |
| **G8** | **`STATUS_RE` to one owner.** The only intended behaviour change in Track G. Its test must name all 7 disputed docs **and assert both directions** (§1.3a) | G7 | A one-sided test lets the incompleteness census silently shrink |
| **G9** | Glob the syntax job **and** exclude that job from `invoked_by()` **in one commit**, with a test that a known-dead tool still reports orphaned | — | **Shipping the halves separately zeroes the orphan census** (§2.2; measured: basename-in-workflow goes 46/108 to 108/108) |
| **G10** | Repoint the provenance citations — **all 354 across 12 paths**, not just `params/core.md` — at `engine/engine_params/params_tables.yaml`; add a test that no live `.py` cites an evacuated path | after S1 (avoid double-touching lines #304's B1 rewrites) | None; the capture is byte-faithful |
| **G11** | Fix the 3 broken-anchor probes; wire `validate_ed_citations` locally; drop `systems/combat/sim` from `export_sim_params`'s `SCAN_DIRS` and regenerate (**unblocked**, §3.5); finish the `ci_names_consistency` migration | — | **Do not delete the deprecated resolver** — it is still the campaign default. Only its *export* presence goes |

### Track S — engine/systems correctness (#304's plan, adjudicated; FA/PC/MB/WR lanes)

Run in #304's own order (conventions and units before vocabularies): **A1** (pin the unpinned canon
ladder — precondition for everything), then **B1, B2, B3**, then **B7, B8**, then **B9**, **B10**,
**A2**, **A3, A4**, **A6**, **A8**, **A9**, **B5, B6**, **B11**.

Three adjudications applied:

- **B4 moves out of P0.** #304's sequencing table lists it as behaviour-preserving; its own body says
  "BLOCKED ON B0", and B0 is HELD. It goes behind the ruling.
- **The `altonian_reinforcements` conversion item is STRUCK** (§3.3). It is an accepted cross-session
  handoff with a passing guard; converting it is MB plan §12 I1's call, not this plan's.
- **Two items are added that neither plan had:** bind and guard the 4x faction-roster literal (§3.5),
  and disposition the forked degree ladder in `skills/valoria-dice-model/valoria_dice.py:45`.

### Track T — instruments

| # | step | depends on |
|---|---|---|
| **T1** | Land #304's **C6** fix (atlas probe under `tmp_path`; the no-test-writes-into-`systems/` guard) | — |
| **T2** | Promote the Class-A batteries into `tests/valoria/` as `xfail(strict)` citing an ED, marked slow | **T1 — mandatory.** They were written as free-standing scripts; promoting them into a `-n auto` suite without C6's guard reproduces the exact race C6 documents (6/6 repro on clean main) |
| **T3** | Promote Class B to a standing `tools/mechanism_census.py` — one owner over `flag_ablation` + `harness` + `interaction` + `reachability_sweep` | T2 |
| **T4** | **Run it.** Its output is an explicit input to the HELD rulings below | T3 |
| **T5** | One `conftest.py` path helper for the 32+7 bootstrap blocks; finish the `tests/valoria` same-fact analysis **via `test_register.json`**, not by hand | — |
| **T6** | Teach `dead_primitive_census.py` to exclude `stub_resolve` bodies (#304 8b); pair with G9's `invoked_by` fix — **same defect class, ship as one pattern fix** (§2.2) | G9 |
| **T7** | Pin or retire the forked resolution core (§1.13); coordinate with A3/A9 — same constant family | — |
| **T8** | Resume the `systems`/`engine` uncalled tracing **with string-path grepping** (§2.1) | T4 |

### Held for Jordan

#304's six (**#0** which `net`/`ob` convention is canonical — *blocks #1 and #2*; **#1** the
`faction_action` band shift and its `s == ob` dead zone; **#1b** the strategic layer resolving on
**d6 >= 4** rather than the canonical d10 engine; **#2** one owner for degree bands; **#7**
`standing`'s bounds; **#8** the 10 dead `infrastructure.py` constants), plus **the 37 grandfathered
`*_index.md` files** and **the `sim_harness` promote-or-retire call** (28 files).

**Recommendation: run T4 before ruling #1, #1b, #2 and #8.** The mechanism census prices exactly those
questions — how often the dead `s == ob` band actually fires in seeded campaigns, whether the 10
constants are behaviourally dead.

**On #7 specifically:** the leanness instinct — reuse the existing `contest.primitives.Standing` — is
**correctly refuted** by #304's B11: rebasing silently adds +5 to two dice pools and imports a
venue-local shape across scales. Its dedicated mutator is the mechanism-preserving answer. Keep that
reasoning; it is the clearest worked example of the mission's binding constraint.

### What this is worth

**Not a large file-count reduction.** Track G removes ~3 files; Track T *adds* an owner; the honest
ceiling is the `sim_harness` cluster plus whatever tracing confirms.

**It is a large edit-surface reduction** — the number of files you must touch to change one rule goes
53 to 1, 44 to 1, 8 to 1, 6 to 1, 5 to 1; adding a tenth lane goes from 8 edits to 1.

**And it closes four live defect classes**: seven documents whose status two tools cannot see; 354
constants citing an evacuated authority; dead scope in six blocking gates; and two dead-code censuses
that are both wrong in opposite directions.

---

## 5. Falsifiers

| claim | command |
|---|---|
| §1.1–1.3, §1.4, §1.7 | `duplication_census.py` — exits 1 if the Status readers agree, if a cited `params/` path resolves, if `params_tables.yaml` loses its key, or if `next_free` falls behind |
| §1.3a (7 disputed) | census §1.3a — union 205 / agreed 198 / disputed 7 |
| §1.4 (354/74/12) | census §2 |
| §1.5 | `python3 tools/compliance_check.py` gives `NameError: name 'check_all' is not defined` |
| §1.9 | `grep -n "ALWAYS return 0" tools/ci_supersession_check.py` gives `:66` |
| §1.11 | `cd audit/2026-07-22-combat-engine-stress-test && python3 stress_battery.py` gives 22 checks, 1 FAIL |
| §2.1 | `pytest engine/tests/test_pipeline_reach.py -k oi17` gives 1 passed |
| §2.2 | `grep -c 'stub_resolve' tools/dead_primitive_census.py` gives 0 |
| §2.3 | `sed -n '121,127p' tools/pathres.py` gives "INTENDED sole parser … not yet the actual one" |
| §3.3 | `pytest engine/tests/test_pipeline_reach.py -k altonian` gives **1 passed** (it must still raise) |
| §3.4 | `awk 'NF && $0!~/^#/' audit/2026-08-11-divergence-audit/01_locations.tsv | wc -l` gives 196 |
| §3.5 (rng) | `random.seed(42); random.Random().random()` twice differs; `random.random()` twice is identical |
| §3.6 | `python3 tools/ci_audit_registry_check.py` reports OK while two 2026-08-11 units are unregistered |

## 6. Still unmeasured

1. **Behavioural deadness, repo-wide.** `harness.py`'s DEAD/LOAD-BEARING classification has never been
   run as a census. It is the agreed superior instrument and the input to four HELD rulings. **No
   valid orphan count exists in either direction** (§2.2).
2. **`tests/valoria`** — 138 of 153 modules unread; the `test_register.json` same-fact query is
   identified but unexecuted.
3. **The 25 `systems/` + 19 `engine/` low-confidence uncalled candidates** — now requiring string-path
   grepping (§2.1), untraced.
4. **The mass-battle twin-engine constant diff** — `BATTLEFIELD_SIZE` 25 vs 51 found; the full
   constant-by-constant sweep is undone (ED-MB-0065 pending).
5. **The `stress_battery` mirror-match FAIL** — reported, undiagnosed. Blocks its xfail-with-ED
   promotion (T2).
6. **~21 tree-walkers and ~21 hardcoded size caps** — filed by both audits, swept by neither,
   deliberately (the ~100-constant precedent).
7. **Cross-layer duplication `tools`/`skills` against the engine** — one known instance
   (`valoria_dice.py:45`); nobody has asked the general question.
8. **The v32 keep-rule over-cover** — `evacuation_plan.py:164-165` keeps the whole
   `tests/sim/v32-combat-balance/` prefix while only `m1_dice_sigma_core.py` is named by consumers.
   **Do not act** until a `MEASURED-BY:` sweep confirms nothing cites the m2–r10 stations; moving a
   cited instrument turns `ci_claim_provenance_check` red.
9. **Every Track-G "expected delta: none" claim** — these are predictions. Each is exactly what its own
   migration test must establish.

---

## 7. The connectivity matrix — throughlines by shared vocabulary

**Method** (Jordan's, 2026-08-11): restrict to `.py` under `engine/` and `systems/`, build document
sets by term/value/name, and derive a throughlines matrix. Instrument: `connectivity_matrix.py`
beside this file. **Corpus: 127 modules across 15 subsystems, 33,021 LOC.**

**Why it sees what the other passes could not.** Every prior instrument in this session measured
*references*: an AST import graph, an `import X` grep, a token census. All three are blind to
coupling that no import expresses — which is precisely how §2.1's error happened. Shared vocabulary
is a different observable: two modules that both speak `TN_STANDARD` are coupled whether or not
either imports the other.

### 7.1 Definition collisions — 27 terms defined in more than one module

**8 constants whose values disagree.** The important ones:

| term | definitions | verdict |
|---|---|---|
| `CI_CEILING` | `100.0` (`factions/sim/excommunication.py`) vs `100` (`overview/sim/ci_track.py`) | one ceiling, two owners, float vs int |
| `CONVICTIONS` | `characters/sim/conviction.py` vs `world/sim/npe.py` | **the conviction roster duplicated across subsystems** — #304's faction-roster pattern at a second term |
| `WEAPONS` / `TRADITIONS` | the registry (`weapons.py`, `traditions.py`) vs a hardcoded list in `workbench/balance.py` | a canonical registry and a literal beside it |
| `GOLDEN_*` (3) | `test_f7_smoke_oracle.py` vs `test_mc_v18_regression.py` — win share 62.5 vs 100.0, battles-mean 35.5 vs 33.5 | two goldens under one name; plausibly distinct fixtures, worth a look |

`CLI` is a false positive (three unrelated locals).

**18 callables with competing owners.** `to_dict`/`from_dict` ×10 is a serialization protocol, not a
defect. The signal is `roll_net` (combat + engine.autoload + social_contest), `roll_pool`
(engine.autoload + mass_battle) and **`degree` (combat + engine.autoload)**.

### 7.2 A new finding: `TN_STANDARD` has two owners, and the copies AGREE

- `engine/autoload/sigma_leverage.py:79` — `TN_STANDARD = 7  # [canonical: params/core.md §TN Values]`
- `systems/threadwork/sim/operations.py:46` — `TN_STANDARD = 7  # Weave, Pull, Mend, Leap, …`

Same value; one carries a canonical citation (to an evacuated path — §1.4), the other carries none.
**Neither #304's fingerprinting nor my token census found this**; it needs the name-collision lens.
Because the values agree, this is a **clean single-owner candidate** under §4's governing rule —
a cleanup, not a behaviour change. Add it to plan step **G7**.

### 7.3 `degree` is a name collision with different signatures — #304's finding, reached independently

Four producers share the stem: `sigma_leverage.py:284 degree(net, ob, pool=None) -> int` ·
`combat_engine_v1/core.py:57 degree(net, ob)` · `dice_engine.py:94 degree_from_net(...) -> Degree` ·
`probabilities.py:25 degree_distribution(...)`. **The bare name `degree` resolves to two different
functions with different arities and return types.**

This is #304's "16 producers, four incompatible meanings of `net`, all typed `(int,int) -> str`,
nothing distinguishes them" — arrived at from name collision rather than from reading the ladders.
**Two methods with genuinely different blind spots agreeing is the signal §2.1 says is worth
ranking**, and this time the blind spots do differ. It reinforces that the #0 ruling gates any
consolidation here.

### 7.4 Cross-subsystem throughlines and hidden coupling

**292 (term, consumer) edges cross a subsystem boundary. 144 of them — 49% — have no import path
from consumer to producer.** The highest-value hidden edges, after filtering:

- **`degree`** — defined in combat + engine.autoload, used by **4** foreign subsystems that import
  neither: `engine.cross_scale`, `engine.tests`, `mass_battle`, `social_contest`. This is the
  consumer map for the #0 held ruling: whoever rules on the `net`/`ob` convention is ruling for these
  four.
- **`TN_STANDARD`**, **`PER_DIE`**, **`ACCORD_MAP`**, **`accounting_boundary`**, **`canonical_accord`**
  — substrate and dice vocabulary crossing boundaries without imports.
- **`DISPATCH_COMBAT_BRIDGE`** — the flag name is defined in `engine.tests` and used by `engine` and
  `engine.cross_scale`.

**Subsystem adjacency, top edges:** `engine.autoload ↔ engine.tests` 45 · **`combat ↔ social_contest`
40** · `engine.autoload ↔ factions` 31 · `engine.tests ↔ social_contest` 26. The
combat↔social_contest edge is the strongest between two *design* subsystems and matches the shared
resolution substrate both use.

### 7.5 The instrument's own false-positive class, caught on its first run

The first run reported `append` as vocabulary shared by **12** subsystems. It is `list.append`. The
bare-call pattern `\b([a-z_]{4,})\s*\(` was matching `x.append(`, `obj.strip(`, `.load(`. Fixed with a
`(?<![.\w])` guard plus a stop-list of stdlib verbs: **507 → 292 edges, 226 → 144 hidden.**

Residual noise is acknowledged, not hidden: `NOTE`, `STATUS`, `case`, `zero`, `weight`, `role` are
coincidental collisions, not throughlines. **§7.4's ranking is evidence for a reading order, never an
action list** — shared vocabulary is evidence of coupling, not proof of a call.

### 7.6 What it does not measure

It reads the **declared surface**, not behaviour. A term can collide by coincidence; a real call can
use no shared vocabulary at all. For behavioural deadness the instrument remains `harness.py`
(§1.11), which is strictly better and still unrun — plan step **T4**.
