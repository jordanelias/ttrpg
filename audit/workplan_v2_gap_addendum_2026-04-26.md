# Workplan v2 — Gap Addendum
**Generated:** 2026-04-27 · session token `8ca3fffeaca3bb9c`
**Companion to:** `valoria_workplan_v2.md`
**Purpose:** Items still missing after the v2 rewrite, surfaced by a deeper repo audit.

---

## §1 Critical findings — promote to F1

### G1 · `Meta.gd L9: var game_mode: int = Enums.GameMode.TTRPG`

**Severity:** Critical — beyond F1.3 in scope.

The autoload literally defaults to TTRPG mode at runtime. The v2 workplan's F1.3 (strip GameMode enum) covers Enums.gd L44 and Constants.gd's 5 mode-branched constants, but does not catch this: the *live runtime state* of every running game starts in TTRPG mode. Any code path that branches on `Meta.game_mode` is currently in TTRPG branches, not videogame branches.

**Action:** F1.3 must include a full grep of `Meta.game_mode` references across all 60 systems/ files and 32 scenes/ files. Each branch evaluated: keep the videogame path, delete the others. The variable itself eliminated.

### G2 · valoria-game has zero CI

**Severity:** High — structural data-cohesiveness risk.

ttrpg has comprehensive CI (`.github/workflows/valoria-ci.yml`, 7.4KB, 7 jobs: syntax-check, register-sizes, hooks-verifier, co-file-check, editorial-check, integrity, compliance-check). valoria-game has no `.github/` directory at all.

This explains MISSING-07 from the original review: tests "have never been run" because no automation forces them to run. Every Godot commit ships unverified.

**Action — new F1.8:** Author `valoria-game/.github/workflows/godot-ci.yml`. Minimum: Godot headless test runner on push/PR. Eventually: GUT framework integration, scene-load smoke tests, parity tests against sim verification ledger.

### G3 · `compliance_check.py` exists and isn't being run

**Severity:** Moderate — process gap.

The bootstrap output reports "compliance_check.py not found — skipping (pre-Phase 0)" but the file exists at `tools/compliance_check.py` (21KB, fully functional with `check_all()` and `validate_commit()` modes). It uses `references/atomization_rules.yaml` and is wired into the CI workflow.

So compliance_check is:
- Present in tools/
- Referenced by CI (which would block bad commits at PR)
- Not being run at orchestrator bootstrap (the bootstrap-time call fails or the lookup path is wrong)

The v2 workplan's M.5 ("deploy compliance_check.py — move from pre-Phase 0 → Phase 0") understates this. The tool is deployed. The orchestrator's bootstrap check is the gap.

**Action — replace M.5:** Investigate orchestrator bootstrap's compliance_check lookup. Either it's looking at wrong path, or there's a missing `atomization_rules.yaml` it can't load, or the integration was never finished. Fix integration. Move from "tool exists but unused at bootstrap" to "bootstrap runs check_all()."

### G4 · Naming collision: two unrelated "A-02"s

The session log refers to "A-02 NPCTrajectoryEvaluator stub" (the Μ-β violation). Meta.gd L62 contains `## A-02: Enforce autoload dependency order at runtime.` — the autoload ordering assertion. These are two different issues both named A-02.

**Action:** When wiring F1.1 (NPCTrajectoryEvaluator), search the codebase for "A-02" and disambiguate. Add a more specific tag (e.g., "NPC-A-02" vs "AUTOLOAD-A-02") to prevent silent fix-confusion.

---

## §2 Skills infrastructure — entire layer absent from workplan

The v2 workplan addresses `skills/valoria-orchestrator/` only. The repo has **11 skills**:

| Skill | Likely status | Workplan implication |
|---|---|---|
| valoria-orchestrator | Active (used every session) | Already covered |
| valoria-canon-guard | Active (philosophy compliance) | **Needs PP-672 update** — should now cite throughlines_meta.md as canonical vetting authority |
| valoria-mechanic-audit | Active (consistency checking) | **Needs PP-672 update** — N→Ω→Μ→М→Τ→Q protocol should be its frame |
| valoria-editorial-register | Active | Should reference vetting_gate from PP-674 |
| valoria-compiler | Likely active | Per-mode compilation may be obsolete post-videogame-only collapse |
| valoria-atomizer | Active (PP-673 renamed it) | Already updated per PP-673 |
| valoria-simulator | Active (sim sessions) | Already updated per PP-673 |
| valoria-arc-generator | Status unknown | Needs audit |
| valoria-chunker | Status unknown | Needs audit |
| valoria-combat-simulator | Status unknown | Needs audit |
| valoria-dice-model | Status unknown | Needs audit |

**Action — new F2.13:** Skills audit. For each skill, determine: (1) still in use? (2) PP-672/673/674 propagation needed? (3) reference videogame_mode_spec.md for mode-collapse implications? Skills that frame work in TTRPG/BG/Hybrid distinctions are stale.

---

## §3 Test corpus — 34 sim files, 28+ unaccounted for

`tests/sim/` contains 34 sim test files. The v2 workplan references `sim_var_01–06` (6 files) for V2 deterministic regression. The remaining **~28 files** are unaddressed:

- `sim_x_01` through `sim_x_36+` series — narrative test scenarios
- `sim_x26r/x27r/x28r` — protocol redesign tests
- `sim_x29_30_31_32_cross_mode_b`, `sim_x33_34_35_36_batch_c` — cross-mode batches

**Question:** Are these regression cases the Sim S2/S3 sessions should reproduce? Or are they historical record of past test sessions? Or design exploration that never became canon?

**Action — new V2 prerequisite:** Triage all 34 sim files. Classify: (a) regression target (sim must reproduce); (b) historical record (no action); (c) design exploration with surviving findings (extract to editorial ledger). Currently the v2 workplan treats only sim_var_01–06 as regression targets without justifying why the others are not.

---

## §4 Player-side mechanics — entire domain absent

The v2 workplan covers NPCs (T-23, T-25, 7 named NPCs) extensively. Player character mechanics are **completely absent**:

| Player-side area | Status | Workplan coverage |
|---|---|---|
| Player character creation (attributes, Histories, Beliefs, Inspirations) | params/core.md L100-128 — extracted to Constants.gd | Mechanically present, no UX path |
| Player progression (Standing 0–7, Rank ladders, Caste) | designs/systems/faction_politics_expanded_v1.md (944 lines) | Not in workplan; design_sync flagged "Phase 5+ implementation needed" |
| Player Piety Track (personal-scale) | designs/scene/conviction_track_v30.md | Not in workplan |
| Player threadwork (TS, Coherence, Knot formation) | params/threadwork.md, threadwork_v30 §5 | V2 covers mechanically; player-UI absent |
| Player faction alignment | Meta._player_faction_id exists | No selection UX |
| Tutorial / first-time experience | — | Absent |

**Action — new C5 bucket:** Player Character Domain. Subsume Standing 0–7 system (faction_politics_expanded_v1), conviction track UX, threadwork player UX, character creation flow, tutorial path. Currently this entire domain is implicit — present in design docs, not in execution plan.

---

## §5 Save format versioning

The v2 workplan's C3 covers DA-01/02/03 (save/load order, card_hand state, NarrativeState deserialize). It does not cover save format versioning.

When DA-02 lands, the SaveData schema changes (card_hand moves out). Existing save files become unreadable. There is no save migration strategy.

**Action — add C3.4:** Save schema versioning. Implement `SaveData.version: int`. Migration handler dispatched on load. Document the version-bump policy: Class C parameter changes do not bump; Class B/A schema changes do, with migration written before bump.

---

## §6 Music / sound / shaders — empty directories, undeclared content domain

`assets/audio/`, `assets/sprites/`, `assets/portraits/`, `assets/backgrounds/`, `assets/map/`, `assets/ui/` are all `.gitkeep` only. `shaders/` is empty.

The v2 workplan acknowledges UI directories are empty (`scenes/ui/persistent/`, etc.) but treats audio/visual content as out-of-scope. This is correct for the orchestrator — assets aren't authored via GitHub API — but the *content domain itself* is undeclared.

**Action — add to C2:** Asset content domain declaration. Specify what categories of content the project requires (background music, ambient, UI SFX, combat SFX; territory portraits, NPC portraits, faction crests; map backgrounds; UI iconography; thread visualization shaders). This is a *catalog* item, not an authoring item — defining the surface area before content production starts.

---

## §7 Localization, accessibility, settings menu

Godot has built-in `tr()` for localization and a settings system. Neither appears in any workplan or design document.

**Action:** Decision needed (Authority-tier or out-of-scope?):
- Localization scope: English only? Multilingual?
- Accessibility: colorblind mode, audio sliders, key remapping, reduced motion, font scaling?
- Settings menu: where in the scene tree, what settings exposed?

**Recommendation:** Defer to post-P milestone. But declare as known-deferred so the absence is intentional, not oversight. Add as **C6 (Out-of-band, post-P)**.

---

## §8 Build / release / distribution

`valoria-game/project.godot` exists (1KB). No `export_presets.cfg`. No platform targets. No release strategy. No version-tag policy on the repo.

The project has substantial code (~250KB GDScript) but no path from "code in main branch" to "playable build a tester can run."

**Action — new bucket B · Build (post-P, parallel to C):**
- Define platform targets (Windows? macOS? Linux? Web?)
- Create export presets
- Define release versioning (matches v30 baseline?)
- Decide: is there a beta/playtest distribution channel?

This need not be done now, but it should exist as a declared domain in the workplan so it isn't a surprise later.

---

## §9 ms_budget.md propagation sweep

ED-731 (2026-04-20) renamed `rs_budget.md` → `ms_budget.md`. The file rename was done. **References to `rs_budget` across other docs were not necessarily updated.**

A `grep -r 'rs_budget'` across the repo would identify residual references. The v2 workplan doesn't include this propagation sweep. It is mechanical, low-effort, and currently invisible.

**Action — add to F2:** F2.14 — `rs_budget` → `ms_budget` reference propagation sweep. Likely 5–20 instances across design docs.

---

## §10 Tools state — 23 tools in `tools/`, status unspecified

`ttrpg/tools/` contains 23 Python tools and 1 JSX (editorial-review browser tool). Many are CI/orchestration. Statuses uncatalogued:

| Tool | Confirmed active |
|---|---|
| atomizer.py, doc_index_gen.py, index_gen.py, compliance_check.py | Yes (in CI) |
| ci_*.py (5 files) | Yes (CI workflow) |
| broken_dependency_checker.py, patch_propagation_checker.py, freshness_gate.py | Yes (integrity job) |
| coverage_matrix.py, valoria_collator.py, valoria_bulk_fix.py | Status unknown |
| extract_proper_nouns.py, extract_values.py, propagator.py, find_references.py, verify_cuts.py | Status unknown |
| editorial_review/valoria-editorial-review.jsx | Browser tool — purpose unclear |
| model_router.html | AI model routing — purpose unclear |

**Action — add to F2:** F2.15 — Tools inventory. For each tool: in-use / archive-candidate. Skills audit (G2 above) intersects.

---

## §11 Branching / git hygiene

Every commit appears to land directly on `main`. No branching strategy documented. No PR workflow. No protected branch rules.

For a one-developer project this is fine. For project completion (the request frames "best practice for project completion"), this is at-risk:

**Action — best practice declaration:** Document current policy: "single-developer project, all commits to main, CI enforces gates externally." This is acceptable but should be explicit. If beta/playtest distribution arrives (G7/B), branch protection should follow.

---

## §12 Scenario / campaign content

The v2 workplan's V2 covers victory conditions across 8 factions. It does not cover **campaign scenarios** — the actual playable narratives. Examples that should exist:

- "Default" campaign (which year does it start? Which faction is player-aligned by default?)
- Tutorial campaign (small map, scripted introductions)
- Historical scenarios (re-enact a known peninsular conflict)
- What-if scenarios (Niflhel never dissolved, Crown Einhir uprising succeeded, etc.)

This is content authoring, distinct from mechanics. None of it is designed.

**Action — declare as out-of-scope until post-P milestone.** Add as **C7 (Campaign Authoring, post-P)**. Acknowledge the gap; defer execution.

---

## §13 Performance budgets

Godot is performant but not infinite. The simulation loop touches:
- 17 territories × 8 factions × N officers/locals/companions = potentially hundreds of NPCs per season
- TrackerRegistry "~50+ types across all scopes"
- Per-season: NPC trajectory evaluation (currently F1.1 stub), faction AI decisions, clock advance, threshold dispatch, deferred consequence flush

**Action — declare and defer:** Performance budgets needed at some point. Frame rate target (60 FPS minimum), save file size limit, memory ceiling, season-tick latency target. Probably defer to first time profiling reveals an issue, but declare as a known-deferred concern.

---

## §14 Backup / disaster recovery

Git is the source of truth. The PAT is in `/mnt/project/VALORIA_PAT`. If the PAT is compromised, the repos can be force-pushed to. If main branch is corrupted, recovery requires git reflog + manual reconstruction.

**Recommendation — best practice:**
- Periodic full-repo clone backup (weekly?)
- PAT rotation policy
- `main` branch protection (even for solo dev): require status checks pass, require linear history. The CI exists; protection isn't enabled.

**Action:** Add as M.9 — main branch protection rules + PAT rotation reminder.

---

## §15 Editorial review browser tool

`tools/editorial_review/valoria-editorial-review.jsx` (15.7KB) — purpose undocumented in tools/README.md. JSX suggests browser-based UI. Possibly a tool for non-technical review of editorial decisions.

**Action — minor F2 item:** Verify whether this tool is in-use, who uses it, and whether it should be referenced in any skill. If unused, archive.

---

## §16 The "atoms_pending" content stream

`references/atoms_pending/2026-04-25/_consolidated/02_solmund_cultural_guide.md` was the source of the Solmund T-A..T-E throughlines (PROVISIONAL). The path implies an entire content-staging pipeline:

- `atoms_pending/` = content waiting for canonization
- Date-stamped folders = batches
- `_consolidated/` = post-processing

The workplan addresses A4 (Solmund T-A..T-E) but does not address the broader **atoms_pending pipeline**. Are there other pending atom batches? What's the canonization process? Who decides when atoms_pending content moves to canonical?

**Action — add to F2:** F2.16 — atoms_pending pipeline audit. List all pending batches. Define canonization process. Currently invisible.

---

## §17 Consolidated additions to the workplan

| Bucket | Additions from this addendum |
|---|---|
| **F1** | F1.3 expanded to grep all `Meta.game_mode` references; F1.8 valoria-game CI; G3 compliance_check integration fix; G4 A-02 disambiguation |
| **F2** | F2.13 skills audit; F2.14 rs_budget propagation; F2.15 tools inventory; F2.16 atoms_pending pipeline audit |
| **C** | C3.4 save versioning; C5 Player Character Domain (new); C6 localization/accessibility (declared, deferred); C7 campaign authoring (declared, deferred) |
| **B** | New bucket: Build/Release/Distribution (declared, deferred) |
| **M** | M.9 branch protection + PAT rotation |
| **V** | Sim corpus triage (34 files → regression / historical / extract) |
| **(declared/deferred)** | Performance budgets; asset content domain catalog; backup policy; editorial-review.jsx purpose verification |

---

## §18 Severity-ordered TL;DR

**Must add to F1 immediately:**
1. **G1.** `Meta.game_mode = Enums.GameMode.TTRPG` at autoload — runtime defaults to TTRPG mode despite videogame-only collapse. F1.3 must extend to runtime grep.
2. **G2.** No CI in valoria-game. Every Godot commit ships unverified. F1.8 add CI workflow.
3. **G3.** compliance_check.py exists, not running at bootstrap. M.5 was misframed.

**Add to V2 prerequisites:**
4. 34 sim files in tests/sim/ — only 6 referenced as regression. Triage the other 28.

**Add to F2:**
5. Skills audit — 11 skills, only orchestrator addressed. PP-672/673/674 propagation needed.
6. ms_budget.md rename propagation across docs.
7. Tools inventory (23 tools, statuses unspecified).
8. atoms_pending pipeline audit.

**Declare new bucket — Player Character Domain (C5):**
9. Standing 0–7, Rank ladders, conviction track UX, threadwork player UX, character creation, tutorial. Currently absent from workplan despite extensive design coverage.

**Declare new bucket — Build/Release (B):**
10. Platform targets, export presets, versioning policy. Currently no path from main branch to playable build.

**Declare and defer (acknowledge, not execute):**
11. Save format versioning (C3.4)
12. Localization/accessibility (C6)
13. Campaign authoring (C7)
14. Performance budgets
15. Asset content domain catalog
16. Branch protection / PAT rotation (M.9)

**The big-picture omissions:** v2 workplan is correct about *infrastructure* and *mechanical verification* but was implicitly scoped to those domains only. The **player-facing domains** (character mechanics UX, asset content, campaigns, build/release, settings, accessibility, localization) were absent. They should be at least *declared* even if deferred — to prevent surprise emergence in 6 months.

A workplan that doesn't acknowledge an entire content authoring domain isn't wrong, but it isn't complete either. The act of declaring "C5 Player Character Domain — deferred to post-P milestone" is the difference between a complete-deferred workplan and an incomplete-implicit one.
