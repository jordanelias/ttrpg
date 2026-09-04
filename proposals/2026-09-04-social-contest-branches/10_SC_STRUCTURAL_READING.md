# 10 · SC STRUCTURAL READING — the kernel, top-down and bottom-up, for a rebuilder

## Status: **READ-ONLY STRUCTURAL READING, 2026-09-04. Nothing ratifies on merge. This file is the only artifact; no other file in the repository was created or edited.** Branch `claude/social-contest-system-review-dn2y5d`, HEAD `e44c6093`.
## Grade of the subject under `CLAUDE.md` §0.2: **one path executes — `build_contest` → `Bout.resolve` → a win-condition — and it reaches 38 % of the package's functions and 21 % of its runtime lines. Everything else is declared, tested-in-isolation, or dead.** The measurements licensing that sentence are in §0.4 and §1.5, and they are reproducible from the scripts named there.

---

## §0 · Scope, method, reading log, coverage

### §0.1 What this is, and the two scope narrowings that shaped it

This is not a defect report for a system in maintenance. Jordan narrowed the brief twice mid-flight:

1. **Not the repository's fifteen subsystems** — "all systems" meant the social contest's *own* systems: agôn as built, the three unbuilt branches, and the kernel's component modules. `07_TOPDOWN_BOTTOMUP.md` misread that and is parked.
2. **"Ignore the seams. I am rebuilding a lot."** — `engine/cross_scale/scene_dispatch.py`, `parliamentary_bridge.py`, `echo_transport.py` and the kernel↔campaign wiring are **out of scope**. A defect there is about to be overwritten.

So this document answers a different question from `06_SYSTEM_AUDIT.md`, which measured the subsystem **as the campaign drives it**. This one measures it **as a rebuilt seam would meet it**: what the public API can reach at all, what is load-bearing, what is duplicated, what is dead, and what the four games actually require. Where the two measurements differ, §3 says why — they are on different bases and both are true.

**Excluded and why:**

| excluded | reason |
|---|---|
| `engine/cross_scale/*` (dispatch, echo, parliamentary bridge) | Jordan: being rebuilt. Findings I had already made are one line each in Appendix A, uninvestigated further. |
| Every other subsystem's internals | out of the original brief. |
| The repository's general apparatus (`tools/`, CI, ledgers) | out of the original brief; `CLAUDE.md` §0.1 pt 5's load-bearing predicate would forbid a guard there anyway. |
| `research/`, the v30 snapshot, `social_contest_v30.md`'s unbuilt sections | `06_SYSTEM_AUDIT.md` §11 already has the row-by-row prose-vs-code table; re-deriving it would be duplicated work, and under §0.05 it is reference either way. |

### §0.2 Method

Read every `.py` under `systems/social_contest/` at least once; opened every anchor I cite. Where a claim is a **count** it carries the script that produced it. Where a claim is **executed** it says so and shows the output. No `pytest` was run. Nothing under the repo was written except this file.

Three disciplines applied throughout, because this session has a measured failure rate on each:
- **Check the assertion, not the prose above it.** Applied to `_kernel_tests.py:1578`, `:182`, and `armature.py:229` — all three turned out to be cases where the comment claims a property the code does not have. §4 D7 is the sharpest.
- **Every load-bearing claim carries a `path:line symbol` anchor I opened myself.** Inherited claims are labelled as inherited and re-verified or marked unverified.
- **A null result is a complete answer with its trail.** §6.

### §0.3 Reading log (in order)

1. `SESSION_BRIEF.md` (1,055 lines) and `SC_INVENTORY.md` (744 lines) — treated as maps, not authority. Every anchor I depend on was re-opened.
2. `05_RECONCILIATION.md` in full; `06_SYSTEM_AUDIT.md` in full.
3. **Every `.py` in `systems/social_contest/`**: `contract.py`, `primitives.py`, `resolver.py`, `wrapper.py` and `modes.py` and `policy.py` and `faction.py` and `degree_extension.py` in full; `armature.py` `:185-451`, `rhetoric.py` `:88-235` + `:399-460`, `dictionaries.py` `:260-340` + `:585-765`, `appraise.py` `:60-177`, `narrative.py` `:25-115` + `:157-170`, `agon_harness.py` `:1-115`, `contest/__init__.py` in full, `contest_legacy_stub.py` `:54-205`, `parliamentary_vote.py` `:40-220`, `parliamentary_stay.py` (grep + docstring), `_kernel_tests.py` selectively (`:15-30`, `:180-195`, `:440-510`, `:1570-1600`).
4. `00`–`04` branch proposals: section maps in full; `01_SPINE.md` §2 change list in full; `02`/`03`/`04` §7.1–§7.2 reuse ledgers in full.
5. `CLAUDE.md` §0, §0.05, §0.1, §0.2, §3, §4, §8. `engine/autoload/dice_engine.py:40-140` (`DEGREE_ORDINAL`, `BandExtension`).
6. Executed: four tracer/probe scripts (§0.4), plus five direct arithmetic probes quoted inline.

### §0.4 Execution artifacts (read-only w.r.t. the repo; scripts in the session scratchpad, not committed)

| script | what it drives | headline |
|---|---|---|
| `kernel_reach.py` | `build_contest(5,5,venue=P)` × 8 proceedings × 3 tracker states × 121 policy pairs = **1,452 resolutions**, under `sys.settrace` | 148 of 236 defs never called (incl. tests) |
| `kr3.py` / `kr4.py` | the same plus dict side-specs with evidence, all four adjudicator types, prebuilt `Venue`s covering all seven win-conditions × `allow_rebuttal` × `split_standing` × `Pressure`, plus the three stub games and `mechanics_selftest()` | **179 non-test defs; 66 (36.9 %) reached by the thinnest call; 68 (38.0 %) by any contest call; 111 (62.0 %) unreachable through the contest API at any argument** |
| `lines.py` | the same sweep with a line tracer, modules imported *before* the tracer attaches | **377 / 1,799 runtime executable lines = 21.0 %** in `sim/contest/` excluding tests+harness |
| inline `python -c` probes | win-condition return vocabularies and tie conventions; `Resonance.effective` vs the resolver's inline rule; `narrative.classify` on a band string; proceeding→win-condition map | §1.2, §4 D6, §1.4 |

⚠ **The 21.0 % and the audit's 35.6 % are not in conflict.** Mine excludes import-time definition lines (the tracer attaches after import); the audit's counts them as hit and says so (`06_SYSTEM_AUDIT.md` §14.2). Mine is a lower bound on reach, the audit's an upper bound, and the truth is between them. Cite whichever matches your basis and say which.

### §0.5 COVERAGE TABLE — depth actually reached, per component

| component | depth | what I read / ran |
|---|---|---|
| `contract.py` | **full** | all 77 lines; every field traced to its reader |
| `primitives.py` | **full** | all 310 lines; every mutator's call sites grepped; `Resonance.effective` executed against the resolver's inline rule |
| `resolver.py` | **full** | all 469 lines; the six win-conditions executed for return vocabulary + tie convention; `_apply` branch-by-branch |
| `wrapper.py` | **full** | all 448 lines; `MECHANICS` statuses counted by execution; every `Contest` field's readers grepped |
| `modes.py` | **full** | all 577 lines read; proceeding→venue→win-condition map executed for all 8 |
| `policy.py` | **full** | all 60 lines; all 11 policies traced through `_apply` |
| `degree_extension.py` | **full** | all 139 lines; the duplicate call-shape confirmed against `resolver.py:307` |
| `faction.py` | **full** | all 154 lines; the split table, `band_of`, `coalition_vote` all read |
| `narrative.py` | **full** | all 170 lines; `classify` executed on both vocabularies |
| `appraise.py` | **full** | all 177 lines |
| `armature.py` | **partial** | `:185-451` in full (axes, `STYLE_AXIS`, `ArmaturePosition`, `dsigma`, `position_of`, `ArmatureConfig`). `:1-184` is a 184-line provenance essay — skimmed, not line-audited |
| `rhetoric.py` | **partial** | `:88-235` (genre maps, CR4) and `:399-460` (`orientation_channel`, `cr5_self_backfire`) read; `EPIDEICTIC_COMPRESSION` (`:270-`) and `CR5_ORIENTATION_CHANNEL` (`:393-`) located, contents not audited |
| `dictionaries.py` | **partial** | `:260-340` (interaction types), `:585-765` (proceedings crosscheck, panel closure) in full; `STYLES_TABLE`/`ADJUDICATORS_TABLE`/`FACTION_BOOSTS`/`DOUBT_MARKER` located and structurally classified, cell contents not individually verified |
| `_kernel_tests.py` | **surface** | 1,727 lines. Read `ck()`, the succession checks, the RES_FLOOR check, the imports block. **Its 389 checks were not individually audited** — the single largest gap in this reading |
| `agon_harness.py` | **partial** | `:1-115` (the docstring + the five WORKAROUNDs, which are the design content) read in full; the 400-line interactive body skimmed |
| `contest/__init__.py` | **full** | all 135 lines |
| `contest_legacy_stub.py` | **partial** | `:54-205` (constants, result shapes, `resolve_exchange`, `run_contest` head). The §9 belief/momentum tail skimmed |
| `parliamentary_vote.py` | **full** | `:40-220`, the whole resolution |
| `parliamentary_stay.py` | **surface** | docstring + grep for writers/callers only. 106 lines, zero callers, 0 lines hit in any sweep |
| **agôn as built** | **full** | §2.14 |
| **negotiation branch** | **partial** | `02_NEGOTIATION.md` section map, §7.1–§7.2, §5.3 summary; not the full 670 lines |
| **inquiry branch** | **partial** | `03_INQUIRY.md` section map, §7.1–§7.2; not the full 703 lines |
| **consensus branch** | **partial** | `04_CONSENSUS.md` section map, §7.2; not the full 669 lines |
| **spine** | **partial** | `01_SPINE.md` §2 change list in full (D1–D9, A1–A3); §1.1–§1.9 via the reconciliation's verdicts |

---

## §1 · TOP-DOWN — what only a whole-kernel view shows, ranked by what a rebuilder needs

### §1.1 The kernel is four fifths declaration and one fifth engine, and the split is not where the file names suggest

Line accounting, `wc -l`, `__pycache__` excluded:

| tree | lines | note |
|---|---|---|
| `systems/social_contest/` total `.py` | **7,306** | 21 files |
| `sim/contest/` (the kernel package) | **6,705** | 16 files |
| of which `_kernel_tests.py` + `agon_harness.py` | **2,249 (33.5 %)** | test and harness code shipped inside `systems/`, not under `tests/` |
| the four modules a contest actually executes in — `contract` + `primitives` + `resolver` + `policy` | **916** | plus `degree_extension` (139) = **1,055** |
| the two configuration modules — `modes` + `dictionaries` | **1,342** | mostly typed prose; §1.5 measures how much executes |
| the unreachable Stage-3 layer — `armature` + `rhetoric` + `appraise` | **1,152** | 0 % of runtime lines under any public-API call (§1.5) |
| the adapter/router — `wrapper` | **448** | 33.9 % of runtime lines |
| output/adapter modules with no path — `narrative` + `faction` | **324** | 0 % |

**What a rebuilder should take from this:** the resolution atom is **about a thousand lines**, it is coherent, and it is not the thing that needs rebuilding. The other 5,700 lines are configuration, provenance essays, a second test suite, and three subsystems that cannot be reached from the front door.

### §1.2 The win-condition family is two families sharing an abstract base

`resolver.py:52-147` declares six subclasses of one ABC. Executed (`python -c`, seed 1, `adv = {a: 6.0, b: 1.0}` and a 0–0 tie):

| class | anchor | fires mid-contest? | winner vocabulary | 0–0 tie at close |
|---|---|---|---|---|
| `ThresholdRace` | `:54` | **yes** | `a` / `b` / `draw` | `draw` |
| `ProofBar` | `:67` | **yes** | `a` / `b` — **never `draw`** | **`b`** (the defender) |
| `GraceThreshold` | `:74` | **yes** | `a` / `b` — **never `draw`** | **`b`** (the non-petitioner) |
| `TallyAtClose` | `:62` | no | `a` / `b` / `draw` | `draw` |
| `VoteAtClose` | `:98` | no | `a` / `b` / `draw` | (stochastic) |
| `PersuasionTrack` | `:81` | no | **`A_total` / `A_decisive` / `committee` / `B_decisive` / `B_total`** | `committee` |

Three facts a rebuilder needs and no single class shows:

1. **Two disjoint return vocabularies.** Five subclasses return a side label; `PersuasionTrack` returns a band string. `Bout.resolve:466` reconciles them only by `"draw" if w == "draw" else "win"` — it never inspects which vocabulary it got. Every downstream consumer must therefore know which win-condition its venue carries. **`narrative.classify` does not know, and is wrong because of it** (§1.4).
2. **Two firing schedules with no declared marker.** `ThresholdRace`/`ProofBar`/`GraceThreshold` can end a bout mid-budget; the other three cannot. Nothing on the ABC says which kind a subclass is; `Bout.resolve:462` calls all six with `closing=False` and relies on three of them returning `None`.
3. **Three tie conventions.** `draw`; silently-to-the-defender; `committee`. `ProofBar`/`GraceThreshold` awarding the tie to a side is *correct design* (a burden of proof unmet is a defence win) — but it is a **burden rule hidden inside a terminal**, and it is the same rule `03_INQUIRY.md` §5.2 wants to promote to a `burden` field on `PROCEEDINGS`. Two homes for one idea, one of them not yet built.

`01_SPINE.md` A2/A3 proposes `WinCondition.margin()` with a per-subclass `SUCCESS_UNIT` as the reconciliation. That is the right shape and the reconciliation upheld its incommensurability argument (`05_RECONCILIATION.md` §5). What the spine does **not** address, and a rebuilder must: **the winner vocabulary is still two vocabularies after `margin()` lands**, because `margin()` is added *beside* `resolve()`, not instead of it.

### §1.3 `Adjudicator.discipline` carries two meanings, and `Panel` carries four aggregation rules

`discipline` is a single `float` on a frozen dataclass (`contract.py:30`). It is read in two places with two different semantics:

- `resolver.py:323` — `Resonance.leak(self.adj.discipline, ...)`: **resistance to character-leak**, i.e. how much this judge sticks to the venue's proof register rather than its own taste. For a `Panel` this is the **mean** (`contract.py:47`).
- `resolver.py:133` — `weights = [... getattr(m, "discipline", 0.0) for m in members]`: **the juror's bench-weight**, i.e. institutional rank. Per member, **summed**.

`resolver.py:111-115`'s own docstring performs the redefinition explicitly — *"the juror's institutional rank/rigor on this bench"*. Under `CLAUDE.md` §4's *idempotent in meaning* test this is the failure case: one word, two meanings, and the next reader derives whichever the call site suggests. It is also the reason ED-1057's ratified `weighted_by_standing` rule is behaviourally inert on every bench the code can build (`06_SYSTEM_AUDIT.md` L6.1, re-verified: every factory in `modes.py` builds homogeneous members, so equal weights reduce the weighted majority to a head count).

`Panel` aggregates its members **four different ways in one class**: majority for `learned` and `hostile` (`contract.py:43-45`), mean for `discipline` (`:47`), mean for `character` (`:48-51`) — and a fifth rule lives outside it, `ArmaturePosition.mean` (`armature.py:286-297`), a second hand-written mean whose docstring says it "mirrors `Panel.character()`". A rebuilder wanting one bench abstraction has to pick one of these and re-derive the other four.

### §1.4 The band vocabulary is already wrong at a consumer — executed

`narrative.classify` (`narrative.py:83-100`) computes `wsign = 1 if winner == A else -1` at `:92`. A `PersuasionTrack` band string is never `A`, so **every band verdict is classified as though side B had won.** Executed:

```
classify("A_total",  "win", leads=[1,1,1], margin=0.5, lc=0, late=False) -> CLEAR_WIN
classify("a",        "win", leads=[1,1,1], margin=0.5, lc=0, late=False) -> ROUT
```

Same bout, same lead history, same margin — the shape changes because the *winner token* came from the other vocabulary. And end-to-end (`random.seed(7)`, `build_contest(7, 2, venue="formal_contest")`, `record=True`):

```
verdict tuple: ('committee', 'win')
render: [NAIL-BITER] 2% separated them at the close, decided only at the wire;
        committee edged it on accumulated pressure.
```

`narrative` is dead today (§1.5), so this is latent — but it is the **worked example of what §1.2's vocabulary split costs a consumer**, and any rebuilt seam that wires narration inherits it. `Chronicle.margin` (`narrative.py:44`) is additionally a *fourth* margin notion — the winner's share of combined advantage — alongside the track position, the raw `adv` lead, and the ballot gap.

### §1.5 Dead surface, measured against the public API rather than against the campaign

This is the measurement a rebuilder needs and that the campaign-based audit could not give, because the campaign exercises one proceeding and one policy. **Driving every proceeding, every tracker state, every policy pair, every adjudicator type, dict side-specs carrying evidence, and prebuilt `Venue`s covering all seven win-conditions × `allow_rebuttal` × `split_standing` × `Pressure`:**

| tier | definition | defs reached |
|---|---|---|
| **T1** | `build_contest(int, int, venue=<proceeding>)` + `resolve_contest` — what a thin seam reaches | **66 / 179 (36.9 %)** |
| **T2** | any `build_contest` + `resolve_contest(game='agon')` call I could construct | **68 / 179 (38.0 %)** — T2 adds exactly **two**: `Dossier.best` and `Dossier.present`, unlocked only by the dict side-spec's `evidence=` |
| **T3** | unreachable through the contest API at **any** argument | **111 / 179 (62.0 %)** |

Never reached at any argument, by module (non-test defs, `never/total`):

```
agon_harness.py     13/13     appraise.py          3/3      armature.py        10/10
narrative.py         6/6      faction.py          11/11     rhetoric.py         8/8*
modes.py            26/32     dictionaries.py      5/6      primitives.py       5/27
resolver.py          4/20     degree_extension.py  3/5      wrapper.py          1/13
contest_legacy_stub  3/3      parliamentary_stay   2/2      parliamentary_vote  3/3
contract.py          0/5      policy.py            0/12
```

`*` four of `rhetoric`'s eight become reachable only via `wrapper.mechanics_selftest()`, which builds a `Bout` **directly** with `armature=` — see §1.6.

Runtime-line coverage under the same sweep (`lines.py`, import-time lines excluded): **377 / 1,799 = 21.0 %**, with `armature` `rhetoric` `appraise` `narrative` `faction` all at **0.0 %** and `dictionaries` at **1.0 %**.

**What a rebuild should not carry forward, with the reason it is dead:**

| surface | lines | why dead | resurrect by |
|---|---|---|---|
| `agon_harness.py` | 522 | zero callers anywhere (re-confirmed); its five WORKAROUNDs are the useful residue, not the code | keeping the WORKAROUND list as a requirements note |
| `_kernel_tests.py` | 1,727 | not dead, but it is a **second test suite living in the production tree**, run as a subprocess by `engine/tests/test_contest_kernel.py:72-78` against a pinned count `_KERNEL_EXPECTED = 389` (`:93`) | deciding whether a rebuild keeps a self-counting script or moves to pytest |
| `contest_legacy_stub.py` `build_argue_pool`/`resolve_exchange`/`run_contest` | ~180 of 268 | zero callers; `contest/__init__.py:24` names a caller path (`sim/cross_scale/scene_dispatch.py:105`) that does not exist | nothing. **Keep only `:67-71`'s five `PERSUASION_*` constants** — `parliamentary_vote.py:45-51` imports exactly those |
| `parliamentary_stay.py` | 106 | zero callers; 0 lines hit in any sweep | `03_INQUIRY.md` wants it (the venue challenge). It is *built and uncalled*, not missing |
| `faction.py` | 154 | zero production callers; `succession`/`coalition_vote`/`vote` reached only by `_kernel_tests.py` | `succession`'s split table is what `02_NEGOTIATION.md` wants to lift — **and §4 D-note says do not lift it unchanged** |
| `modes.py` venue library `:66-325` + `ContestedMode` + `proceeding_mode` + `CANONICAL_PROCEEDINGS` | ~300 | `proceeding_venue:567` builds `Venue(budget=budget, win=win, **o)` and `build_contest:133` passes no `**o`, so all 8 proceedings inherit `resolver.Venue`'s dataclass defaults | one parameter at one call site — see §1.7 |
| `narrative.py` | 170 | `summarize` has no caller on any contest path even with `record=True` | wiring a consumer; fix `classify` first (§1.4) |
| `appraise.py` + `armature.py` + `rhetoric.py` | 1,152 | `build_contest` has **no `armature=` parameter** (`wrapper.py:110-111`) and `_resolve_agon:215-216` passes none | **not just the parameter** — see §1.6 |
| `dictionaries.py` everything but `panel_win_condition` | ~700 | typed prose with no resolution consumer; `derive_interaction:310` is labelled *"the ONE canonical typed lookup … do not re-implement"* and **nothing implements it once** | the resolver has no interaction model at all (§1.8) |
| 97 `params/contest.md` citations | — | the cited file does not exist; `references/restructure_ledger.md:768` resolves it into the evacuated `engine/params/` tree | counted per file: `dictionaries` 41, `rhetoric` 14, `wrapper` 14, `_kernel_tests` 9, `modes` 9, `primitives` 4, `resolver` 3, `appraise` 3 |

### §1.6 The armature is unreachable for a second, deeper reason than the missing parameter — and a rebuilder must know it

Everyone has recorded that `build_contest`/`resolve_contest` take no `armature=` (`agon_harness.py:71-76` "WORKAROUND 3"; `01_SPINE.md` A-list; `06_SYSTEM_AUDIT.md` §13.2). **Adding the parameter would not by itself make the armature reachable.**

`ArmatureConfig.positions` is `{id(adjudicator-or-member) → ArmaturePosition}` (`armature.py:429`), consumed at `armature.py:393-395 position_of` as `positions.get(id(m), ...)` / `positions.get(id(adjudicator), ...)`. The key is **CPython object identity**. Consequences, all structural:

1. **The caller cannot compute the key before `build_contest` runs.** `build_contest:151` constructs the adjudicator itself (`CANONICAL_ADJUDICATORS[adj_type]()`), and `modes.panel:456-461` mints five fresh `Adjudicator` objects per call. A caller building an `ArmatureConfig` in advance has no id to key on. The only working order is *build the adjudicator, then the config, then the Bout* — which is exactly what `wrapper.py:410-412` does inside the self-test and what `agon_harness.py` does with WORKAROUND 3.
2. **It is not serialisable.** An `id()` is meaningless across processes, which makes the armature un-exportable to `engine/engine_params/` and un-portable to Godot (`CLAUDE.md` §5).
3. **An id is recyclable.** `positions` holds ints, not references, so a collected `Adjudicator` can free its id for a later object and a stale config would silently match the wrong judge.

`Adjudicator` is `@dataclass(frozen=True)` (`contract.py:24`) and therefore hashable with value equality — which is presumably *why* `id()` was chosen (two identical judges on a bench would collapse to one dict key). That is a real problem and `id()` is the wrong answer to it. **A rebuild needs a per-adjudicator identity that is a value, not an address** — a seat index on the `Panel`, or an `adjudicator_id` field. This is the single highest-leverage structural change in the Stage-3 layer, and it is not on any branch's change list.

### §1.7 One parameter at one call site is the whole distance between the venue library and the venues in play

`modes.py:536-567 proceeding_venue` builds `Venue(budget=budget, win=win, **o)` at `:567`. `build_contest:133` calls `proceeding_venue(proc_name, use_tracker=use_tracker)` — **no `**o`**. So every one of the eight `PROCEEDINGS` rows inherits `resolver.py:150-166 Venue`'s defaults: proof `.30/.30/.40`, equal tense weights, `DefeatCatalogue()` defaults, `Pressure()` none, `allow_rebuttal=False`, `split_standing=False`, `base_ob=2.0`.

Executed for all eight (`proceeding_venue` vs `build_contest`, win-condition class and budget):

```
casual_dispute      TallyAtClose    budget=1   adj=Adjudicator
church_tribunal     PersuasionTrack budget=5   adj=Adjudicator
formal_contest      PersuasionTrack budget=3   adj=Panel        (crowd)
grand_contest       PersuasionTrack budget=5   adj=Panel        (crowd)
guild_arbitration   VoteAtClose     budget=3   adj=Panel
personal_appeal     TallyAtClose    budget=1   adj=Adjudicator
private_negotiation TallyAtClose    budget=3   adj=Adjudicator
royal_audience      PersuasionTrack budget=3   adj=Adjudicator
```

**So the eight canonical proceedings differ in exactly four live fields**: `budget`, win-condition class, adjudicator factory, and (for `church_tribunal` only) `start_ground`. `roles` has **zero readers** outside `_kernel_tests.py`; `resistance` is read only by `_derive_resistance`, whose output is carried on `Contest.resistance` and read by nothing that resolves (`wrapper.py:75-79` says so itself and downgrades the `MECHANICS` row to `PARTIAL` at `:337`); `track_start` is discarded for `guild_arbitration` because the panel branch overrides the win-condition; `tracker`/`tracker_mode` are consumed by `_use_tracker` and then, for a panel proceeding, thrown away (`modes.py:552` computes `tracker_on` and the `panel` branch at `:553-555` takes precedence).

A rebuilder gets the ~260 lines of designed venues — per-venue proof registers, fault catalogues, `ProofBar`/`GraceThreshold` terminals, `Pressure` — back by threading one `**o`. That is worth stating plainly because three branch proposals are written as though new venue *fields* were needed; mostly what is needed is for the existing ones to arrive.

### §1.8 The kernel has no interaction model, and the typed dictionaries describe one

`social_contest_v30.md` §4 Step 4 specifies CLASH / REINFORCE / CROSS / TIE: compare the two orators' successes head-to-head, margin minus resistance, strain. `dictionaries.py:283-308 INTERACTIONS_TABLE` types all four rows with their conditions, resolutions and strain formulas, and `:310-323 derive_interaction` implements the structural derivation and declares itself *"the ONE canonical typed lookup for the derivation; do not re-implement."*

**The resolver never compares the two sides at all.** `_apply` (`resolver.py:341-438`) is per-side; each side's reception is rolled independently against `base_ob` (`:302,:307`) and accumulates into its own `state.adv[side]` (`:335`). There is no margin, no comparison, no strain — and `strain` appears nowhere in any `.py` in the package outside these table strings. `derive_interaction` has zero callers on any resolution path (grep: `wrapper.py:287` puts it in `_SYMBOLS`, `wrapper.py:342` marks it `WIRED`, `agon_harness.py:464` prints it as flavour, `_kernel_tests.py:973-975` tests it directly).

**This is the largest single design decision a rebuilder faces**, and neither `06_SYSTEM_AUDIT.md` nor the four branch documents put it as a choice: *does the rebuilt contest resolve by two independent accumulations (what the code does) or by a head-to-head comparison (what canon, the typed dictionaries and the `MECHANICS` registry all describe)?* Under `CLAUDE.md` §0.05 the code is the mechanism and the prose is reference — so the honest statement is that **the interaction model does not exist**, and 1 of the 21 `WIRED` `MECHANICS` rows names a function that no resolver calls. It is not a defect to be patched; it is a fork.

### §1.9 `WIRED` means "the symbol resolves", and for three rows it means "fires in a Bout the public API cannot build"

Executed: `MECHANICS` has **25 rows — 21 `WIRED`, 3 `STUB`, 1 `PARTIAL`.**

`mechanics_selftest` (`wrapper.py:435-448`) does two things: it asserts every `WIRED` row's `fn` resolves to a symbol (`:443-444`), and it calls `_stage3_resolution_invocation_check` (`:377-432`), which genuinely **runs the resolver** and confirms the three Stage-3 rows change an outcome. That check is good work and it is honest about why it exists (`:378-382`: *"symbol-resolvability alone let a DEAD function pass the WIRED gate"*).

But it proves the Stage-3 mechanics fire **in a `Bout` it constructs directly with `armature=`** (`:412`, `:423`), and my sweep proves **no `build_contest`/`resolve_contest` call can construct such a `Bout`** (§1.5, §1.6). So:

- `adjudicator_armature`, `cr4_stasis_genre`, `cr5_self_gating` are `WIRED` **at the kernel and unreachable at the API**.
- Eight more `WIRED` rows (`styles_table`, `interaction_types`, `derive_interaction`, `adjudicators_table`, `faction_boosts`, `proceedings_table`, `face_tracker`, `three_trackers`) point at tables and aliases with no resolution consumer.
- The registry already knows how to say this: `audience_resistance` was downgraded to `PARTIAL` at `:337` for being *"derived but not plumbed into resolution"* — **the identical condition the three Stage-3 rows are in at the seam.** One word, applied inconsistently. `CLAUDE.md` §4's idempotent-in-meaning test again.

### §1.10 State: what persists, what does not, and the one field written around its owner

Inside the kernel there is **no persistent state at all**. `Standing`, `Reserve`, `Room`, `FaultState`, `Dossier`, `ContestState`, `Bout.live`, `Bout.log` are all constructed in `Bout.__init__` (`resolver.py:239-270`) and die with the `Bout`. `Contestant` is an immutable spec the `Bout` never mutates (`:180-195`). The only writes that leave the package are `parliamentary_vote.py:214`'s `world.factions[dominant].adjust("L", ...)` — and that is the faction-scale vote, not the contest.

**Consequence for a rebuilder, stated plainly: the kernel is a pure function of (spec, venue, adjudicator, policies, RNG state).** That is a genuine strength and it is why `05_RECONCILIATION.md` §7's "nothing here is a reason to rebuild `agon`" is right. It also means every consequence question — records, precedents, obligations, grudges — is a *seam* question, which is the layer being rebuilt.

One violation, latent: **`Reserve.cur` is written around its own mutators.** `primitives.py:53-56` gives `Reserve` `spend()` and `regroup()`; `resolver.py:362` assigns `c.reserve.cur = min(c.reserve.max, c.reserve.cur + Reserve.COST["evidence"])` directly to refund an evidence spend that found nothing to present. This is `CLAUDE.md` §0.1 pt 1's read/write-asymmetry shape — a second write path a future change to `Reserve` would silently miss. It is reachable only through the dict side-spec's `evidence=` (T2), so it is latent, and it is a one-line fix (`Reserve.refund(kind)`).

### §1.11 Keys: the subsystem constructs none

Re-verified by grep: **zero `Key(` constructions, zero `KeyLog` references and zero `.emit(` calls exist anywhere in `systems/social_contest/`.** Every Key the subsystem is credited with is built at the seam. Under the narrowed scope that is the whole of the Keys axis: **a rebuilt seam owns the Key vocabulary entirely, and the kernel imposes no constraint on it except the shape of what `Bout.resolve` returns** — which is §1.2's two-vocabulary union, and is the one thing a Key payload would have to encode.

---

## §2 · BOTTOM-UP — one subsection per component

Each: **owns / reads / emits / executes vs declared-and-dead.**

### §2.1 `contract.py` (77 lines) — the only module with no dependencies, and the right shape

- **Owns:** side identity (`:7 A, B = "a", "b"`, `:8 other`), `Move` (`:10-14`), `FaultState` (`:16-22`), `Adjudicator` (`:24-35`), `Panel` (`:37-51`), `ContestView` (`:53-66`), `Pressure` (`:69-77`).
- **Reads:** `dataclasses` only. Its docstring's claim — *"Depends on nothing else in the package"* — is true, verified.
- **Executes:** all five defs reached (0/5 never).
- **Declared-and-dead:** `ContestView.evidence_available` (`:66`) is always 0 unless the caller uses the dict side-spec; `ContestView.can_hard` (`:59`) is exposed while `hard` is licit only before an unlearned or hostile bench (`primitives.py:216-217`), which no canonical proceeding builds.
- **For a rebuilder:** this is the module `01_SPINE.md` A1 correctly chooses as `ContestOutcome`'s home, precisely because it adds no import edge. It is also where §1.3's `discipline` ambiguity and §1.6's missing adjudicator identity have to be fixed — both are one field on a frozen dataclass here.

### §2.2 `primitives.py` (310 lines) — half genuine primitives, half compositions, one dead duplicate

- **Owns:** `Stasis` (`:11-25`), `Appeal` (`:27-29`), `Standing` (`:31-47`), `Reserve` (`:49-56`), `Face = Standing` (`:108`, an honest alias), `FaceScale` (`:132-149`), `TRACKERS`/`RETIRED_TRACKERS` (`:154-169`), `RhetoricalWeights` (`:184-206`), `Pool` (`:208-211`), `SelfGating` (`:213-220`), `Leverage` (`:222-230`), `Room` (`:232-236`), `Resonance` (`:238-251`), `Readiness` (`:253-260`), `DefeatCatalogue` (`:262-279`), `EvidenceItem` (`:282-289`), `Dossier` (`:291-310`).
- **Reads:** `engine.autoload.sigma_leverage.level` (`:9`) — one upstream call, for `Leverage.ONGROUND`.
- **Executes:** 22 of 27 defs.
- **Dead:** `Standing.strip` (`:36`, never called anywhere in the kernel — the module says so itself at `:83-85`), `FaceScale.face_max`/`face_current` (`:138`,`:144`), `Resonance.effective` (`:247`), `Resonance.tension` (`:250`). `Standing.strip_points` (`:37`) is armature-only.
- **The finding worth the section:** `Resonance.effective` is a **stale duplicate of the live reception rule with a numeric divergence**. Executed on identical inputs (`role={.30,.30,.40}`, `char={.34,.33,.33}`, `leak=0.4`, logos, past tense, default `Venue`):

  ```
  Resonance.effective(logos, role, char, leak)          = 0.372
  resolver._advance inline (1-leak)*joint + leak*char    = 0.420   (joint_weight = 0.48)
  ```

  The exported primitive predates `Venue.joint_weight` (`resolver.py:172-178`) and omits `RES_FLOOR`. It is re-exported publicly at `contest/__init__.py:58` and has zero callers. A rebuilder reading `primitives.py` to learn the reception rule learns the wrong one. **Delete it or make the resolver call it.**
- **The 100 named constants** (`SC_INVENTORY.md` §H, reproducible) live here and in `resolver.py`; every one either carries `[SEED]` or cites `params/contest.md`, which does not exist.

### §2.3 `resolver.py` (469 lines) — the engine, and the one module that is genuinely load-bearing

- **Owns:** `roll_net` wrapper (`:28-32`), `VALID_KINDS` (`:34`), five `[SEED]` scalars (`:35-44`), `ContestState` (`:46-50`), the six win-conditions (`:52-147`), `Venue` (`:150-178`), `Contestant` (`:180-195`), `_Side` (`:197-236`), `Bout` (`:238-466`), `run` (`:468`, dead).
- **Reads:** `engine.autoload.sigma_leverage` (`roll_net`, `effective_ob`, `net_boost`), `engine.autoload.dice_engine` (`DEGREE_ORDINAL`, `degree_from_net`), `.degree_extension.CONTEST_DEGREE_EXTENSION`.
- **Executes:** 16 of 20 defs; 182 / 284 runtime lines (64.1 %) — the highest in the package.
- **The resolution atom, stated once so a rebuilder does not have to reconstruct it:** `Bout.resolve` (`:440-466`) runs `budget` exchanges; within each, A then B produce a `Move` from a read-only `ContestView`; `_apply` (`:341`) spends reserve, routes by kind, and for an argue move calls `_reception` (`:283`) → `roll_net(pool) + net_boost(lev, pool)` → `degree_from_net(..., extension, pool)` → an int 0-3; `_advance` (`:314`) turns that into `MERIT_SCALE · deg · res · rdy · U(1±JITTER) · bias` and adds it to `state.adv[side]`; the venue's `DefeatCatalogue` is checked **after every move** (`:457`) and the win-condition **at each exchange boundary** (`:462`) and once more closing (`:465`).
- **`support` is the free move.** `:349-351`: spend 2, `regroup()` +4, `build_ethos(1)` = +0.8 Standing, **no fault, no ground check, no relevance check, no reception roll.** At full reserve `regroup` clamps so it is net 0 reserve; below full it is net +2. Every one of the eleven shipped policies falls back to it at `reserve_frac < 0.3` (`policy.py:5`). A rebuilder should know that the kernel's only unconditional, cost-free, always-legal move exists and is what the whole policy set does under pressure.
- **Dead:** `run` (`:468`), `_Side.face_max`/`face_current` (`:230`,`:233`), `_Side.concentration` (`:225`). `ThresholdRace`/`ProofBar`/`GraceThreshold` are alive as classes and unreachable from `PROCEEDINGS` (§1.7). The move kinds `hard`, `shift`, `evidence`, `rebut`, `pass` are all implemented and none is issued by a policy that any canonical proceeding reaches without the dict side-spec or `allow_rebuttal`.
- **Three RNG draw sites** (re-verified, and the reason `01_SPINE.md` §1.8's single-site `rng` proposal was refuted): `:32` `roll_net`, `:334` `random.uniform` on every scoring event, `:139`/`:144` `random.gauss` per juror. `policy.py` imports no `random`.

### §2.4 `wrapper.py` (448 lines) — adapter + router + a registry that over-claims

- **Owns:** `_derive_resistance` (`:43-56`), `Contest` (`:59-88`), `_as_contestant` (`:91-107`), `build_contest` (`:110-196`), `_resolve_agon` (`:203-217`), `_stub` (`:220-234`), `GAMES` (`:236-245`), `resolve_contest` (`:248-264`), `_SYMBOLS`/`_resolve` (`:271-304`), `MECHANICS` (`:306-375`), `_stage3_resolution_invocation_check` (`:377-432`), `mechanics_selftest` (`:435-448`).
- **Executes:** 12 of 13 defs (only `_stub` unreached without `game=`); 76 / 224 runtime lines.
- **`Contest` carries five write-only fields.** Grepped for readers across `systems/`, `engine/`, `tools/`, `tests/`: `self.game` (`:71`), `self.stakes` (`:81`), `self.primary_attribute` (`:74`), `self.track_start` (`:80`), `self.resistance` (`:75`) are written at construction and read **only** by `agon_harness.py` (dead) — `adjudicator_type` and `primary_attribute` at `:221`,`:229`. `01_SPINE.md` D5 deletes `game`; the other four are the same shape and are not on its list.
- **`resolve_contest` has two return shapes** and says so (`:254-259`): `((winner, reason), bout)` for `agon`, a bare `stubwire.StubResult` for the three stubs. No caller passes `game=`, so the second shape is unreachable in production and the router is a switch with one position.
- **`build_contest` is where the venue library is lost** (§1.7) and where the armature cannot enter (§1.6).
- **A duplicate construction, executed:** `proceeding_venue:553-555` builds `panel_win_condition()` and `build_contest:181-190` rebuilds it via `dataclasses.replace` with `jurors=len(the_adj.members)`. For `guild_arbitration` both are a 5-juror weighted `VoteAtClose` (`PANEL_DEFAULT_JURORS = 5`, `modes.panel(size=5)`); the first is discarded. Two correct constructions, one dead.

### §2.5 `modes.py` (577 lines) — the venue library, and the configuration surface

- **Owns:** four groundup venue presets (`:66-82`), `VENUES` (`:84`), `ContestedMode` (`:87-113`), three institutional venues + modes (`:115-163`), `INSTITUTIONAL_MODES` (`:150`), six cross-cultural venues + modes (`:166-324`), `CROSS_CULTURAL_VENUES` (`:318`), the three SCAFFOLD classes (`:333-359`), the four canonical adjudicator factories (`:433-461`) and `CANONICAL_ADJUDICATORS` (`:463`), `ADJUDICATOR_PRIMARY` (`:426`), `CANONICAL_TRACK_START`/`CHURCH_TRIBUNAL_TRACK_START` (`:475-476`), `PROCEEDINGS` (`:485-519`), `_use_tracker` (`:521-534`), `proceeding_venue` (`:536-567`), `proceeding_mode` (`:569`), `CANONICAL_PROCEEDINGS` (`:577`).
- **Reads:** `engine.substrate.stubwire` (`:15`), `.contract`, `.primitives`, `.resolver`, and `.dictionaries` **lazily inside `proceeding_venue`** (`:554`, comment at `:549`) with the comment *"Lazy import breaks the dictionaries<->modes cycle"* — a deadlock workaround, not a cycle fix (`CLAUDE.md` §3 says exactly this about deferred imports).
- **Executes:** 6 of 32 defs; 25 / 219 runtime lines (11.4 %).
- **Declared-and-dead:** 26 of 32 defs, ~300 lines of designed venues, unreachable for the one-parameter reason in §1.7. `ContestedMode.play` (`:91`) has no production caller. The three SCAFFOLDs (`DyadicMode:333`, `NegotiationMode:342`, `CeremonialMode:351`) return `stubwire.StubResult` and are `engine/tests/test_pipeline_reach.py:847`'s subject.
- **For a rebuilder:** `NegotiationMode` and `CeremonialMode` are the pre-existing homes for two of the four games. `02_NEGOTIATION.md` builds `settle()` as a new terminal and does not reuse `NegotiationMode`; that is defensible (a terminal is not a mode) but should be a stated choice, not an omission.
- **`_use_tracker`'s tri-state** (`:521-534`) is the pattern `01_SPINE.md` §1.5 wants to generalise as `burden`. Note its cost: two fields (`tracker: bool`, `tracker_mode: str`) encode one three-valued fact, and `wrapper.py:52` parses a rule out of a label (`spec["resistance"].startswith("halved")`).

### §2.6 `policy.py` (60 lines) — the cleanest module in the package

- **Owns:** eleven policies and `POLICIES` (`:56-60`). Reads `.contract` and `.primitives` only. Imports no `random`.
- **Executes:** 12 of 12 defs; 35 / 53 runtime lines (66.0 %) — the highest ratio in the package.
- **For a rebuilder:** this is the correct shape for a decision surface — a pure `ContestView → Move` function, no resolver internals. The problem is not `policy.py`; it is that `ContestView` (`contract.py:53-66`) exposes neither the venue's proof weights nor the adjudicator's character, so the largest lever in the kernel (`Move.appeal`) has no information behind it. `narrative.venue_brief` (`narrative.py:157-170`) would supply exactly that and is never called.

### §2.7 `degree_extension.py` (139 lines) — the best-built module here, and it ships a copy of its own call

- **Owns:** `OVERWHELM_SIGMA` (`:46`), `overwhelm_bar` (`:49-57`), `PoolDesaturation` (`:60-82`), `CONTEST_DEGREE_EXTENSION` (`:87`), `owner_overwhelming_margin` (`:90-101`), `crossover_pool` (`:104-118`), `degree` (`:121-139`).
- **Reads:** `dice_engine.BandExtension`, `sigma_leverage.MU_PER_DIE`/`SD_PER_DIE`.
- **Executes:** `PoolDesaturation.may_overwhelm` only (2 of 5 defs).
- **Why it is the model:** `may_overwhelm` returns a `bool` consulted in one branch of the owner's ladder, so *"there is no signature by which this class could promote a band"* (`:16-18`) is a **structural** claim, not a convention — and `owner_overwhelming_margin` (`:90-101`) *reads the owner's bar by probing it* rather than retyping `3`, with the reasoning written down at `:91-96`. That is the discipline the rest of the kernel does not have.
- **The one blemish:** `degree()` at `:121-139` hard-wires `extension=CONTEST_DEGREE_EXTENSION`, while `resolver.py:307-308` uses the **injected** `self.degree_extension`. The module whose entire purpose is to make the ladder substitutable ships a non-substitutable copy of the same call. `tests/valoria/test_degree_ladder_single_owner.py:138` and `tools/balance_oracle.py:153` both read the hard-wired one.

### §2.8 `dictionaries.py` (765 lines) — typed prose, 1 % live

- **Owns:** `Genre`/`Orientation`/`Style`/`STYLES_TABLE`/`STYLE_BY_AXES` (`:60-136`), `DOUBT_MARKER*` (`:175-236`), `InteractionType`/`INTERACTIONS_TABLE`/`derive_interaction` (`:270-323`), `AdjudicatorType`/`ADJUDICATORS_TABLE` (`:337-385`), `FactionBoost`/`FACTION_BOOSTS`/`guilds_boost_for` (`:387-487`), `Proceeding`/`PROCEEDINGS_TABLE`/`_crosscheck_proceedings` (`:503-620`), `PANEL_AGGREGATION`/`PANEL_DEFAULT_JURORS`/`panel_win_condition`/`PANEL_CLOSURE` (`:685-764`).
- **Reads:** `.modes` at module level (`:45`) — the eager half of the `dictionaries ↔ modes` cycle.
- **Executes:** 1 of 6 defs (`panel_win_condition`); 3 / 297 runtime lines (**1.0 %**).
- **`PANEL_DEFAULT_JURORS = inspect.signature(_modes.panel).parameters["size"].default`** (`:697`). The intent — one bench-size literal, living once — is right; the mechanism makes a function signature a coupling surface, so renaming `panel`'s `size` parameter breaks `panel_win_condition` at import. A rebuilder should keep the intent and change the mechanism.
- **`derive_interaction` is §1.8's fork made concrete**: the one canonical implementation of a model the engine does not have.
- **`DOUBT_MARKER`** (`:201-235`) self-describes as `"DESIGN-TABLE COMMITMENT ONLY"` at `:229` while `MECHANICS` has no row for it and `rhetoric.py`'s prose claims it is wired. Reference, not mechanism.

### §2.9 `armature.py` (451 lines) — a well-shaped mechanism keyed on a memory address

- **Owns:** `ArmatureAxis` (`:191-204`), `STYLE_AXIS_PRIMARY`/`STYLE_AXIS_OFFAXIS` (`:228-229`), `_row` (`:231`), `STYLE_AXIS` (`:242-247`), `ArmaturePosition` (`:261-297`), `ARMATURE_MAX_DSIGMA` (`:336`), `_ALIGN_NORM` (`:343`), `style_axis_alignment` (`:346`), `style_axis_dsigma` (`:357`), `position_of` (`:374`), `ArmatureConfig` (`:414-451`).
- **Reads:** `engine.autoload.sigma_leverage.level` (`:146`), `.contract.Panel`, `.dictionaries.STYLES_TABLE` (via `rhetoric`).
- **Executes:** 0 of 10 defs under any public-API call; 0 / 92 runtime lines. Reached only by `mechanics_selftest` and `_kernel_tests.py`.
- **Two constants, two disciplines.** `ARMATURE_MAX_DSIGMA = _sigma_level("moderate")` (`:336`) genuinely reads the owner — a function call, so it cannot drift. `STYLE_AXIS_OFFAXIS = 0.15` (`:229`) carries the comment *"= resolver.RES_FLOOR value (reused, not fresh)"* and **`armature.py` never imports `RES_FLOOR`** (grep-verified: `RES_FLOOR` appears in `armature.py` only inside comments at `:225` and `:229`). Same claim, opposite implementations, in one module. See §4 D7 for what its guard does.
- **§1.6's identity defect lives at `:393-395` and `:429`.** It is the reason this module is 0 %.

### §2.10 `rhetoric.py` (524 lines) — CR4/CR5, and a table with two public names

- **Owns:** `_GROUND_TO_GENRE` (`:91-98`), `genre_of_ground` (`:101`), `STASIS_PRIMARY_GENRE` (`:142`), `STASIS_ROLE` (`:150-157`), `primary_genre_for` (`:160`), `is_pre_merits` (`:172`), `is_higher_order_reframe` (`:178`), `CR4_PRIMARY_GENRE_POOL_BONUS` (`:206`), `genre_of_style` (`:209`), `primary_genre_pool_bonus` (`:221`), `EPIDEICTIC_COMPRESSION` (`:270`), `orientation_channel` (`:399`), `cr5_self_backfire` (`:413`), `CR5_*` tables.
- **Executes:** 0 of 8 defs under any contest call; 4 reachable via `mechanics_selftest` only.
- **`STASIS_PRIMARY_GENRE = dict(_GROUND_TO_GENRE)`** (`:142`) is a shallow copy of the table `genre_of_ground` reads. Two public names, two dict objects, one content — **and two error contracts**: `genre_of_ground:108` uses `.get()` (unknown ground → `None`), `primary_genre_for:167-168` **raises** `ValueError`. A caller picks its failure mode by picking a name.
- **`is_pre_merits`** (`:172`) is what `03_INQUIRY.md` §7.1 calls "the Stay, already named in its own docstring" — correct, and it is one of the four `rhetoric` defs no argument reaches.
- **`cr5_self_backfire`** (`:413`) takes `(style_key, landed, my_standing)` — **no armature, no alignment** — confirming the consensus branch's refutation of the shape spec's antibody design (`SESSION_BRIEF.md` §11.4, re-verified by reading the signature).

### §2.11 `appraise.py` (177 lines) — a self-contained reveal ladder that re-declares the owner's

- **Owns:** `APPRAISE_FAILURE..APPRAISE_OVERWHELMING` (`:68-71`), `APPRAISE_REVEAL_BOUNDARY` (`:74-102`), `_STRENGTH_LOW`/`_STRENGTH_HIGH` (`:106-107`), `_dominant_axis` (`:110`), `_strength_band` (`:119`), `_AXIS_REGISTER` (`:132-137`), `appraise_armature` (`:140-177`).
- **Executes:** 0 of 3 defs; 0 / 60 runtime lines.
- **Two duplications, both small and both real.** `:68-71` retypes the degree ordinal 0/1/2/3, whose owner is `engine/autoload/dice_engine.py:48-53 DEGREE_ORDINAL`. `_AXIS_REGISTER` (`:132-137`) is a hand-derived third table whose own comment says it *"mirrors the Style→axis map in armature.STYLE_AXIS … read back to the orientation register"* — a derivation of `STYLE_AXIS` × `STYLES_TABLE.orientation`, written out by hand.
- **`APPRAISE_REVEAL_BOUNDARY`** is a design record in a dict, not a mechanism. Its content (partial reveal is self-enforcing; full reveal is self-undermining) is the most reusable *design* in this module and belongs in the branch documents, not in a runtime dict nothing reads.

### §2.12 `narrative.py` (170 lines) — a legibility layer, wrong at the vocabulary boundary

- **Owns:** `SHAPES` (`:25`), three `[SEED]` margins (`:30-32`, self-described as *"Eyeballed … NOT anchored"*), `_name` (`:35`), `Chronicle` + `render` (`:40-80`), `classify` (`:83-100`), `_per_exchange` (`:103`), `summarize` (`:112-154`), `venue_brief` (`:157-170`).
- **Executes:** 0 of 6 defs; 0 / 117 runtime lines, **even with `record=True`** — `resolve_contest`'s `record` parameter fills `Bout.log` and nothing consumes it.
- **Defect:** §1.4, executed. `classify:92` inverts on band strings.
- **For a rebuilder:** `venue_brief` (`:157`) is the missing half of §2.6 — the pre-contest cue that would give `ContestView`'s appeal choice something to be based on. It exists, it is 14 lines, and nothing calls it.

### §2.13 `faction.py` (154 lines) — an adapter that is a fourth resolver

- **Owns:** `Faction` (`:12-20`), `MOTIONS` (`:23-25`), `FORUM` (`:27`), `RESIST_DAMP` (`:28`), `case` (`:30`), `_adj` (`:37`), `_one_vote` (`:41`), `vote` (`:48`), `rate` (`:59`), `band_of` (`:68`), `rate_banded` (`:76`), `succession` (`:86-118`), `succession_rate` (`:120`), `coalition_vote` (`:128-148`), `coalition_rate` (`:150`).
- **Executes:** 0 of 11 defs; 0 / 99 runtime lines. Reached only by `_kernel_tests.py`.
- **`coalition_vote` (`:128-148`) is a resolver built out of the kernel's atoms without the kernel's loop**: it hand-builds a `ContestState` (`:143`), calls `roll_net` per side (`:144-145`) and runs `PersuasionTrack.resolve` (`:146`) with no exchanges, no faults, no policies, no stasis. `04_CONSENSUS.md` §7.2 offers to delete it and is right to.
- **`band_of` (`:68-74`) is a fourth banding rule** producing `pass`/`fail`/`committee` from a *vote share* against a motion threshold ± 0.06 — a different axis from every other band in the package.
- **`succession`'s split table (`:107`, `:117`) is verified defective and latent.** `leader = 'a' if t >= 5 else 'b'` awards a dead tie to A; `ratio = {4:0.60, 5:0.55, 6:0.50}[min(6,max(4,round(t)))]` is **anti-monotone on A's side** — A's share falls from 0.55 to 0.50 as A's advantage grows. Zero production callers, so latent (`05_RECONCILIATION.md` §6, independently verified three times). **`02_NEGOTIATION.md` proposes to lift this table for the settlement split; lifting it unchanged makes the defect live.**
- **`_kernel_tests.py:182` cannot observe any face of it**, verbatim and re-verified by me:
  ```python
  _o=FX.succession(4,4,NEUT); ck("succession split ratio canonical (§7.2.1)",
                                  _o[0]!='split' or _o[2] in (0.50,0.55,0.60))
  ```
  A disjunction satisfied vacuously whenever the outcome is not a split, and otherwise satisfied by any of the three canonical values regardless of which track produced it. `CLAUDE.md` §0.1 pt 2 exactly.
- **`reb_ob` has zero readers** (`:23-25`; grepped across the tree). A stored §5.5 Rebuttal Ob that nothing rolls.

### §2.14 `agon` as built — the game that executes

**What it is, end to end:** `build_contest(side_a, side_b, venue=<one of eight proceeding names>)` coerces each side to a `Contestant` (an int `faculty`, or a dict adding `standing_start`/`evidence`), resolves the proceeding's `budget`/win-condition/adjudicator from `PROCEEDINGS`, derives an audience resistance it then does not use, and returns a `Contest`. `resolve_contest` routes through a four-row `GAMES` table with one live row to `_resolve_agon`, which constructs a `Bout` and returns `((winner, reason), bout)`.

**What it genuinely delivers, and a rebuilder should keep:**
- A **pure**, seed-reproducible resolution with no persistent state (§1.10).
- **A single owner for the degree ladder**, with a structurally-bounded subsystem extension (§2.7) — the one seam in this package that earns the word STRUCTURAL.
- **Venue-configured defeat conditions** (`DefeatCatalogue`, `primitives.py:262-279`): which faults are fatal and at what count is a property of the institution, not of the resolver. This is the kernel's best idea and all four games use it.
- **A per-side accumulation with a pluggable terminal.** The critique's architectural verdict — *"the sigma resolver and the armature dot-product are the two universal primitives; alea, acclamation, consensus and negotiation are pluggable win-conditions on the same kernel; reject any fix that adds a parallel resolver"* — is correct about the resolver, and the resolver honours it.

**What it does not deliver, stated so a rebuilder is not surprised:**
- No interaction model (§1.8). No record of what happened beyond a `(winner, reason)` tuple. No strain, no momentum spend, no obligations, no chain contests. Face is monotonic-up unless the armature is on. The three trackers `TRACKERS` names are, in any reachable contest, one tracker that only decrements (`Reserve`), one that never moves (`Standing`), and one that is not the win condition for the panel proceeding.
- **Four resolvers coexist**: `Bout` (`resolver.py:238`), `run_parliamentary_vote` (`parliamentary_vote.py:125`), `coalition_vote` (`faction.py:128`), and the dead `run_contest` (`contest_legacy_stub.py:191`).

### §2.15 `contest_legacy_stub.py` (268 lines) — keep five constants, drop the rest

- **Owns:** `ARGUE_POOL_TN` (`:59`), `CONCENTRATION_MULTIPLIER` (`:63`), the five `PERSUASION_*` constants (`:67-71`), `RESISTANCE_DEFAULT` (`:75`), `CONTEST_FATIGUE_PENALTY` (`:80`), `ExchangeResult` (`:84`), `ContestResult` (`:98`), `build_argue_pool` (`:111`), `resolve_exchange` (`:132`), `run_contest` (`:191`).
- **All of it is re-exported through `contest/__init__.py:35-50`**, so importing the package for five integers pulls in every kernel module.
- **Executes:** 0 of 3 defs.
- **`CONCENTRATION_MULTIPLIER = 3`** is a formula struck by ED-901 and is still a public export (`__init__.py:42`, `:104`).
- **The `'A'`/`'B'` side vocabulary** (`:91`, `:103`) is the uppercase twin of `contract.py:7`'s `"a"`/`"b"`, and `parliamentary_vote.py:92` uses the uppercase one too. Both are exported from the same package `__init__`.

### §2.16 `parliamentary_vote.py` (220 lines) — a second resolver, matching its canon step for step

- **Owns:** ten `BG_VOTE_*` constants (`:54-73`), `_TRACK_FLOOR`/`_TRACK_CEIL` (`:74`), `GENRES` (`:76`), `Motion` (`:80`), `VoteDeclaration` (`:89`), `VoteResult` (`:97`), `_side_genre` (`:117`), `run_parliamentary_vote` (`:125-220`).
- **Reads:** `dice_engine`, `game_state.MULTS`, and the five `PERSUASION_*` constants from the package (`:45-51`).
- **Executes:** 0 of 3 defs under a contest call — it is a faction-scale entry point, reached through `composition.require('parliamentary_vote')`.
- **It is the one place where prose and code agree step for step** (`06_SYSTEM_AUDIT.md` §11, re-checked against `:141-208`), with the single exception that §10's *"Mandate −1 for one season"* is implemented as a permanent `adjust` at `:214`.
- **`VoteResult.starting_track: int = 5` (`:100`)** is a hardcoded default in the very module that imports `PERSUASION_TRACK_START_DEFAULT` at `:50` — see §4 D2.

### §2.17 `parliamentary_stay.py` (106 lines) — built, correct, uncalled

- **Owns:** three constants (`:37-39`), `StayResult` (`:43`), `invoke_stay` (`:54`), `resolve_stay_lift` (`:101`).
- **Writes nothing** — its docstring states the convention (`:19-21`: *"invoke_stay RETURNS the suspension … for the caller to apply"*) and grep confirms no `.adjust(` and no assignment to world state.
- **Zero callers anywhere; 0 lines hit in every sweep.** `03_INQUIRY.md` wants it as the venue challenge. It is the clearest case in the package of *a mechanism that is finished and merely unreferenced* — the cheapest thing a rebuilt seam could turn on.

### §2.18 `_kernel_tests.py` (1,727 lines) and `engine/tests/test_contest_kernel.py`

- A self-counting script (`ck()` at `:18-21` increments module-level `P`/`Fc`), seeded at `:15`, printing `RESULT: N passed, M failed` and exiting non-zero on failure. `engine/tests/test_contest_kernel.py` runs it as a subprocess and pins `_KERNEL_FLOOR = 151` (`:89`) and `_KERNEL_EXPECTED = 389` (`:93`).
- **It is the only executable specification of the Stage-3 layer**, because that layer is unreachable through the public API. A rebuild that changes the armature has no other observer.
- **The count pin is a coupling a rebuilder will trip immediately.** `01_SPINE.md` D8 already budgets −4; `04_CONSENSUS.md` §7.2 budgets ~−5 for deleting `coalition_vote`. Any deletion in §1.5's table moves 389, and that must be a deliberate same-commit edit.
- **Not audited check-by-check** — the largest gap in this reading (§0.5, §7).

### §2.19 The three unbuilt games — what each actually requires of the kernel

Read from the branch documents' own reuse ledgers and change lists, cross-checked against what the kernel provides.

| branch | what it needs that the kernel **already has** | what it needs that the kernel **does not have** | the shared requirement |
|---|---|---|---|
| **negotiation** (`02`) | `Bout`, `TallyAtClose`, `DefeatCatalogue`, `degree_from_net`; `private_negotiation` is already a `PROCEEDINGS` row with `TallyAtClose` and `budget=3` | a **terminal that divides rather than picks** — `settle()`; a share-by-degree table; a `Settlement`/`Refusal` return type. Its own §7.2 checked all six win-conditions and found none that divides, which my §1.2 table confirms: every terminal returns a side or a band | `WinCondition.margin()` |
| **inquiry** (`03`) | `ProofBar` (`resolver.py:67-72` — burden **and** the stall rule in six lines), `DefeatCatalogue`, the `Stasis` ladder, `Dossier`/`EvidenceItem`, `is_pre_merits`, `excommunication_court_venue`, `invoke_stay` | `burden` as a `PROCEEDINGS` field; `restricted` on `Venue`; **and, critically, a way to reach `ProofBar` and `inquisition_hearing_venue` at all** — §1.7's missing `**o` | `WinCondition.margin()` + the venue passthrough |
| **consensus** (`04`) | `VoteAtClose` (the ballot machinery), `Panel`, `DefeatCatalogue` (the antibody's only executing channel), `Grudge` in `settlements/sim/ledger.py` | a `unanimity_required` branch; **a per-member term on the ballot** (the critic's single recommended change — `resolver.py:139`/`:144` draw i.i.d. per juror with no per-member disposition, so the members are exchangeable and "the named holdout" is named by RNG order); `holdout_rounds` and `on_hung`, neither of which is a `Venue` field | `WinCondition.margin()` + a bench identity |

**Two of them need the same thing under different names, and this is the most useful cross-branch observation available:**

1. **A per-adjudicator identity that is a value.** Consensus needs it to name a holdout and to bind an antibody to a member; inquiry needs it (via `03`'s armature passthrough) to give the accused a judge to read. §1.6 shows the kernel's current answer is `id()`, which serves neither. **One field on `Adjudicator`/`Panel` closes both.**
2. **A burden convention.** Inquiry wants `burden` on `PROCEEDINGS`; but `ProofBar` and `GraceThreshold` already implement a burden — silently, as their tie convention (§1.2), with a `challenger`/`petitioner` parameter that inverts the sign (`01_SPINE.md` §1.2's "ADDED — the margin has no sign convention"). **The burden already has a home; it is inside two terminals and undeclared.** Promoting it to a field is right; a rebuilder should promote it *out of* those two classes, not alongside them.

**And one requirement all four games share that no branch owns:** §1.2's two winner vocabularies. `margin()` adds a numeric channel beside `resolve()`; it does not unify what `resolve()` returns. A rebuild that ships `ContestOutcome` (`01_SPINE.md` A1) should make the **winner** field one vocabulary, not keep `band` verbatim — though note that keeping `band` verbatim is precisely what makes the two campaign goldens a control (`SESSION_BRIEF.md` §11.6), so this is a real trade and not an oversight.

---

## §3 · WHERE THE TWO PASSES DISAGREE

### §3.1 Top-down says "the kernel is coherent"; bottom-up says "five of its modules cannot be reached"

The top-down view (§1.10, §2.14) finds a pure, single-owner, seed-reproducible resolution atom with a structurally-bounded ladder seam — genuinely good architecture. The bottom-up view finds that `armature`, `rhetoric`, `appraise`, `narrative` and `faction` — **1,476 lines, 33 % of the non-test kernel** — execute **zero** runtime lines under any call the public API can make.

**Resolution: both are true and the reconciliation is the finding.** The kernel is coherent *in the part that runs*, and the part that does not run is not incoherent — it is unreferenced. That distinction matters for a rebuild: this is not 1,476 lines of bad code to throw away, it is 1,476 lines of code that has never been integration-tested against anything but a purpose-built self-test. A rebuilder should treat it as **unvalidated, not wrong** — and should expect §1.4-class defects (a consumer written against the wrong vocabulary) to be the typical failure when it is finally wired.

### §3.2 Top-down says `MECHANICS` over-claims; bottom-up says `mechanics_selftest` is honest

§1.9 reads the registry and concludes `WIRED` is a word with two meanings. §2.4 reads `_stage3_resolution_invocation_check` and finds a genuinely rigorous check that *runs the resolver* and would fail if the armature stopped moving outcomes.

**Resolution: the self-test is honest about a `Bout`; the registry is dishonest about the API.** Both statements survive. The fix is not to weaken the self-test but to add its missing clause: *does a `Bout` carrying this mechanic exist on any path `build_contest` can produce?* Today the answer is no for three `WIRED` rows, and nothing asks.

### §3.3 Top-down ranks the venue library as the biggest loss; bottom-up ranks the armature identity

§1.7 says ~300 lines of designed venues are one parameter away. §1.6 says the armature is a redesign away, not a parameter away.

**Resolution: they are different sizes and the ordering matters for a build plan.** Threading `**o` through `build_contest` is a one-line change that unlocks `ProofBar`, `GraceThreshold`, per-venue `DefeatCatalogue`s and `Pressure` — which is most of what `03_INQUIRY.md` needs. The armature needs a value-typed adjudicator identity first, and every branch that assumes `armature=` alone suffices is assuming wrongly. **Do the venue passthrough first; it is cheap and it unblocks a branch. Do not schedule the armature as "add a parameter".**

### §3.4 Where I disagree with `06_SYSTEM_AUDIT.md`

- **Coverage.** Its 35.6 % and my 21.0 % are on different bases (§0.4) and neither is wrong. Its basis is the campaign; mine is the API. Cite the basis.
- **It calls `proceeding_venue` discarding the venue library "F1.1 — worst"** under Flexibility; I agree it is the largest *lost* surface but rank §1.8 (no interaction model) above it, because a missing parameter is a fix and a missing model is a fork.
- **It does not name §1.6.** Its F1.1/§13.2 both treat the armature as reachable-once-`armature=`-is-passed. My reading says the `id()` keying makes that false, and that is a disagreement about a fact, not an emphasis.
- **It does not name §1.4 or §4 D6.** Both are executed here.

---

## §4 · DEDUPLICATION LEDGER — every rule with more than one home *inside the kernel*

`CLAUDE.md` §8: *every rule lives once*. **Seventeen violations.** The session's prior finding — band thresholds owned three times, neutral start four — is **verified and extended**: the thresholds have two code homes (not three; the third was `faction.band_of`, which is a *different* rule, listed separately as D14), and the neutral start has **five**.

| # | the rule | home 1 | home 2 | home 3+ | status |
|---|---|---|---|---|---|
| **D1** | Persuasion bands **9 / 7 / 3 / 1** | `resolver.py:91-95` — bare literals inside `PersuasionTrack.resolve` | `contest_legacy_stub.py:67-70` — `PERSUASION_WIN_THRESHOLD` etc., re-exported at `contest/__init__.py:43-46`, consumed at `parliamentary_vote.py:200-208` | — | values agree today; **the kernel does not import the constants** |
| **D2** | neutral track start **5** | `modes.py:475 CANONICAL_TRACK_START = 5.0` | `contest_legacy_stub.py:71 PERSUASION_TRACK_START_DEFAULT = 5` | `resolver.py:86` (`PersuasionTrack.__init__(start=5.0)`) · `faction.py:142` (`5.0 + lobby`) · **`parliamentary_vote.py:100 starting_track: int = 5`** — a literal default in the module that imports the constant at `:50` | **five homes** |
| **D3** | the ED-621 lobby clamp **[4, 6]** | `parliamentary_vote.py:71-72` (`BG_VOTE_LOBBY_START_MIN/MAX`) | `faction.py:142` — `max(4.0, min(6.0, …))`, bare literals | — | two homes |
| **D4** | the **0–10** track clamp | `resolver.py:87` | `parliamentary_vote.py:74,196` (`_TRACK_FLOOR/_TRACK_CEIL`, self-flagged `[ASSUMPTION]`) | `contest_legacy_stub.py:180` | three homes |
| **D5** | the Persuasion-Track **scale** | `resolver.py:86` — `scale=1.5` | `faction.py:87` — `succession(scale=1.5)` | `faction.py:128` — `coalition_vote(scale=1.0)` | three homes, **two values** |
| **D6** | **the reception rule** | `primitives.py:247 Resonance.effective` — exported at `__init__.py:58`, **zero callers** | `resolver.py:326` — inline, with `joint_weight` and `RES_FLOOR` | — | **executed divergence: 0.372 vs 0.420 on identical inputs** (§2.2). The exported primitive is stale |
| **D7** | the de-saturation floor **0.15** | `resolver.py:35 RES_FLOOR = 0.15` | `armature.py:229 STYLE_AXIS_OFFAXIS = 0.15`, commented *"= resolver.RES_FLOOR value (reused, not fresh)"* — **and `armature.py` never imports `RES_FLOOR`** | `_kernel_tests.py:1579` asserts `_SAO == 0.15` — a **third** retyping | **the guard cannot observe the failure it excludes.** `_kernel_tests.py:450` imports `RES_FLOOR as _RF` and `:1579` does not use it. Change `RES_FLOOR` to 0.2 and the test still passes |
| **D8** | the **Argue Pool** | `primitives.py:208-211 Pool.size = max(5, faculty*2 + 3)` | `contest_legacy_stub.py:111-129 build_argue_pool = max(1, primary*2 + history + fatigue)` | — | both cite §3's *"(Primary × 2) + History"*; different floors, different third term |
| **D9** | the **degree ordinal 0/1/2/3** | owner: `engine/autoload/dice_engine.py:48-53 DEGREE_ORDINAL` | `appraise.py:68-71 APPRAISE_FAILURE..APPRAISE_OVERWHELMING` | — | retyped, not read |
| **D10** | the banding call `DEGREE_ORDINAL[degree_from_net(net, ob, extension=…, pool=…)]` | `resolver.py:307-308` — **injected** `self.degree_extension` | `degree_extension.py:138-139 degree()` — **hard-wired** `CONTEST_DEGREE_EXTENSION` | — | the module that exists to make the ladder substitutable ships a non-substitutable copy |
| **D11** | the stasis → genre table | `rhetoric.py:91 _GROUND_TO_GENRE`, read by `genre_of_ground:108` with `.get()` | `rhetoric.py:142 STASIS_PRIMARY_GENRE = dict(_GROUND_TO_GENRE)`, read by `primary_genre_for:167-169` which **raises** | — | two public names, two dict objects, **two error contracts** |
| **D12** | the Style → register map | `armature.py:242-247 STYLE_AXIS` (style → primary axis) | `dictionaries.py:90-136 STYLES_TABLE` (style → genre + orientation) | `appraise.py:132-137 _AXIS_REGISTER` (axis → Revealing/Obscuring), hand-derived from the other two by its own admission | three tables, one fact |
| **D13** | **bench aggregation** | `contract.py:43-45` majority (`learned`, `hostile`) | `contract.py:47-51` mean (`discipline`, `character`) | `armature.py:286-297 ArmaturePosition.mean` — a second hand-written mean · `resolver.py:133-141` weighted **sum** vs half-total | four rules, two independent mean implementations |
| **D14** | the token **`committee`** | `resolver.py:93` — `3 < t < 7` on a float track | `faction.py:68-74 band_of` — vote share within ±0.06 of a motion threshold | `parliamentary_vote.py:191` (zero-zero) and `:205` (`3 < int track < 7`) | three unrelated rules, one word |
| **D15** | **side identity** | `contract.py:7 A, B = "a", "b"` — the kernel and the composition roles | `contest_legacy_stub.py:91,103` — `'A'`/`'B'` | `parliamentary_vote.py:92` — `side: str # 'A' \| 'B'` | two case conventions, both re-exported from `contest/__init__.py` |
| **D16** | the panel win-condition construction | `modes.py:553-555 proceeding_venue` — `panel_win_condition()` | `wrapper.py:181-190 build_contest` — rebuilds via `dataclasses.replace` | — | executed: both yield a 5-juror weighted `VoteAtClose` for `guild_arbitration`; the first is discarded |
| **D17** | `Reserve.cur` | `primitives.py:55-56 spend/regroup` | `resolver.py:362` — bare assignment (the evidence refund) | — | §0.1 pt-1 shape; latent (T2-only) |

**How a rebuilder should read this table.** D1–D5 and D8 are *numbers* with two homes: cheap to fix, and the fix is to pick the owner and import it. D6, D10, D11, D16 are *rules* with two implementations: one of each pair is dead, and the dead one is the one a reader will find first. D7 is the pattern this repository keeps generating — a comment asserting a single source, a literal that is not one, and a guard that retypes the literal a third time. D12–D15 are *vocabulary* duplications and are the ones that will silently survive a rebuild, because each home is individually correct.

---

## §5 · ATTACKS I RAN THAT FAILED, REPORTED AS FAILED

| attack | how I ran it | result |
|---|---|---|
| `DefeatCatalogue.check` iterates `(A, B)` — does A-first ordering bias who clinches? | read `primitives.py:273` against `resolver.py:457`; traced the reachable fault states | **FAILED.** The check runs after **every** move, so a side at threshold clinches before the other can reach it. Both sides cannot be over threshold at one check. The ordering is inert. (Independently the audit measured 12,000 mirrors and found no side bias.) |
| Do `proceeding_venue` and `build_contest` disagree on any proceeding's win-condition? | executed both for all eight | **FAILED.** Identical for all eight. D16 is a duplicate construction, not a divergence. |
| Does `guild_arbitration`'s `tracker=True` produce a `PersuasionTrack` anywhere, contradicting the panel branch? | executed; read `modes.py:168-171` | **FAILED.** `tracker_on` is computed and the `panel` branch at `:169` takes precedence. The fields are dead, not contradictory. |
| Does `crowd` (a `Panel` subtype) accidentally trip `build_contest`'s panel branch and flip `formal_contest`/`grand_contest` to `VoteAtClose`? | executed all eight | **FAILED.** `wrapper.py:165` guards on `adj_type is None`, and a named proceeding's `adj_type` is `"crowd"`. Both stay on `PersuasionTrack`. The guard's own comment at `:162-164` predicted this and is correct. |
| Is `VoteAtClose` drawing random numbers on non-closing calls, desynchronising seeds? | read `:124-125`; counted draws | **FAILED.** `if not closing: return None` precedes every draw. |
| Do the Persuasion bands in `resolver.py:91-95` and the thresholds in `parliamentary_vote.py:200-208` disagree in value? | compared literals to constants | **FAILED.** 9/7/3/1 both sides. D1 is an ownership defect, not a value defect — and saying otherwise would have been the easy, wrong finding. |
| Is `STASIS_PRIMARY_GENRE` able to drift from `_GROUND_TO_GENRE`? | read `rhetoric.py:142` | **PARTLY FAILED.** It is a `dict()` copy taken at import, so the **values** cannot drift. The divergence is in the two readers' error contracts, which is what D11 claims — a weaker finding than the one I went looking for. |
| Does `mechanics_selftest` pass while the Stage-3 mechanics are dead? | read `:377-432`; ran it under the tracer | **FAILED.** It genuinely constructs Bouts and measures an outcome shift. It is honest. §1.9's finding is about the API boundary, not about the self-test. |
| Is `PersuasionTrack.resolve`'s band arithmetic asymmetric about 5? | read `:91-95`; checked the complementary intervals | **FAILED.** `≥9 / ≥7 / >3 / >1 / else` partitions symmetrically about 5. The asymmetry the session found is in `faction.succession`'s split table, not in the bands. |
| Does `_kernel_tests.py` contain the vacuous-in-loop assertion pattern §0.1 pt 2 names? | inherited from `SC_INVENTORY.md` §G3 (count: 0); spot-checked `ck()` at `:18-21` and the `:180-195` block | **NOT RE-RUN in full.** I verified the one instance that matters (`:182`, §2.13) and confirmed the `ck()` idiom, but did not repeat the 32-loop audit. **Reported as unverified, not as clean.** |

---

## §6 · NULL RESULTS — scopes examined and found clean, with the evidence of the look

| `[NULL:]` scope | evidence |
|---|---|
| `[NULL: Key construction inside `systems/social_contest/`]` | `grep -rn "Key(\|KeyLog\|\.emit(" systems/social_contest --include="*.py"` → nothing. Re-run this session. |
| `[NULL: persistent state written by the kernel package]` | every mutable object traced to `Bout.__init__` (`resolver.py:239-270`); `Contestant` verified write-once (`:180-195`); the only cross-package write is `parliamentary_vote.py:214` |
| `[NULL: module-level registry mutated after import]` | `GAMES`, `MECHANICS`, `PROCEEDINGS`, `POLICIES`, `TRACKERS`, `VENUES`, `STYLE_AXIS`, `INTERACTIONS_TABLE` — no assignment site outside definition; `wrapper.py:285,295` `_SYMBOLS.update` is import-time |
| `[NULL: a second `Bout`-like resolution loop inside `sim/contest/`]` | `coalition_vote` (`faction.py:128`) shares the atoms and has **no loop** — it is a single-shot; `run_contest` (legacy) has its own loop but is outside `contest/`. So: one exchange loop in the kernel package |
| `[NULL: a win-condition that mutates `ContestState`]` | read all six `resolve` bodies; all read `s.adv` and none assigns |
| `[NULL: policy reaching resolver internals]` | `policy.py` imports only `.contract` and `.primitives`; every policy takes a frozen `ContestView`. The decoupling its docstring claims is real |
| `[NULL: an unknown game / proceeding / adjudicator / move kind / appeal / ground reaching resolution silently]` | `wrapper.py:130,153,261`; `resolver.py:342,319,355,378` all raise `ValueError`. `modes._use_tracker:147-149` raises on an illegal opt-in |
| `[NULL: `degree_extension` able to promote a band]` | `PoolDesaturation.may_overwhelm` returns `bool` and is consulted in one branch (`dice_engine.py:95-135`). The STRUCTURAL claim at `degree_extension.py:16-18` is earned |
| `[NULL: research-sourced numbers in the kernel]` | every non-cited constant carries `[SEED]` or cites `params/contest.md`; none cites a historical source. Spot-checked `resolver.py:39-44`, `primitives.py:33,50,209,233,255-256`, `armature.py:228-229`, `narrative.py:30-32`, `appraise.py:106-107` |
| `[NULL: a fifth resolver hiding in `dictionaries.py` or `modes.py`]` | `panel_win_condition` returns a `WinCondition`; every `*_venue`/`*_mode` returns a `Venue`/`ContestedMode`. None resolves |
| `[NULL: `parliamentary_stay.py` writing world state]` | grep for `.adjust(` and for assignment: none. Returns a `StayResult` |
| `[NULL: a `params/contest.md` citation that resolves]` | `find . -iname "contest.md"` → nothing; no `params/` directory exists. 97 citations, all dangling |

---

## §7 · WHAT WOULD MAKE THIS READING WRONG

1. **`_kernel_tests.py` was not audited check-by-check.** 1,727 lines, 389 checks, and it is the **only** executable specification of the entire Stage-3 layer. If a meaningful fraction of those checks are the shape of `:182` — a disjunction satisfiable without testing anything — then my "unvalidated, not wrong" verdict on `armature`/`rhetoric`/`appraise` (§3.1) is too generous, and the honest verdict would be "unvalidated and untested". **This is the single most valuable follow-up available**, it needs no new tooling, and I did not do it.
2. **My reachability sweep drove the public API, not every possible caller.** A caller that constructs a `Bout` directly — `_kernel_tests.py`, `agon_harness.py`, `tools/balance_oracle.py`, and any rebuilt seam that chooses to — reaches more. The 62 % figure is *"unreachable through `build_contest`/`resolve_contest`"*, not *"unreachable"*, and every use of it in this document is phrased that way. If a rebuilt seam constructs `Bout`s directly, the figure is irrelevant to it.
3. **The line-coverage figure excludes import-time lines** and therefore understates reach for the table-heavy modules (`dictionaries` at 1.0 %, `contract` at 12.9 %) whose content *is* their definitions. §0.4 states the basis; a reader who quotes 21.0 % without it will be wrong about `contract.py`.
4. **`armature.py:1-184` and `rhetoric.py:236-398` were skimmed, not line-audited.** Both are long provenance essays; a mechanism buried in one of them would not appear here.
5. **The `id()` finding (§1.6) is read, not executed.** I did not construct the GC-recycling case. The three consequences follow from CPython semantics and from reading `position_of` and `ArmatureConfig`, and consequence 1 (the caller cannot compute the key before `build_contest` runs) is verified by reading `build_contest:151` and `modes.panel:456-461`. Consequence 3 (id reuse) is inference from language semantics, and I mark it as such.
6. **Self-review bias, marked as `SESSION_BRIEF.md` §8.6 requires.** This reading grades four proposals produced by the same session that produced this document. **An independent reviewer would add:** that §2.19's cross-branch observation ("two branches need the same identity field") is exactly the kind of unifying claim a reviewer of one's own work is biased toward, because it makes the four documents look more coherent than four independent authors would have made them; a genuinely independent reader should test whether consensus's "named holdout" and inquiry's "a judge to read" really are one requirement or two that I have merged for tidiness.
7. **Nothing here changes the grade.** Under `CLAUDE.md` §0.2 this document is **paper**. Its measurements executed; its recommendations have not.

---

## Appendix A · Out-of-scope observations, one line each, uninvestigated

Recorded because I met them before the scope narrowed, or while tracing something in scope. **None was investigated further; none is ranked; the seam ones are about to be rebuilt and should not be acted on from here.**

1. *(seam)* `scene_dispatch.py:337-342` maps `verdict` to `echo_degree` by comparing against `contest_side.a`/`.b` only, so **every `PersuasionTrack` band would fall through to `"Partial"`** — latent, because nothing sets `ctx["proceeding"]` (grep: the only two hits are `:290` and `:308`).
2. *(seam)* `echo_transport.py:198-208 _derive_degree`'s contest arm reads `result.get("total_victory")` — a field of the **retired** `contest_legacy_stub.ContestResult` shape (`:104`) that the promoted kernel's result dict does not carry — and `"draw"` is truthy, so a draw would derive `Success`.
3. *(seam)* `echo_transport.py:425-426` builds `participants` from `ctx["parties"]`, which the emergency-council path never writes back to `ctx`, so every live contest Key carries `participants: []`.
4. *(seam)* `scene_dispatch.py:315` cites `dictionaries._APPEAL_TO_GENRE`, a symbol that exists nowhere in the package (nearest real symbol: `rhetoric._GROUND_TO_GENRE`, `rhetoric.py:91`). Already recorded twice in earlier proposals.
5. *(registry)* `references/module_contracts.yaml`'s `social_contest` row declares four emitted Key types; three (`scene.dialogue`, `scene.insult`, `scene.threat`) have no producer anywhere and the one consumed type has no consumer.
6. *(registry)* `module_contracts.yaml:84-92`'s note claims three callers route `parliamentary_vote` through the composition registry; `systems/factions/sim/parliamentary_action.py:41-44` imports it directly.
7. *(FA lane)* Church Tribunal / Excommunication exist twice with no code edge — `modes.py:200-217,291-297` versus `systems/factions/sim/tribunal.py` and `excommunication.py`, which share no import.
8. *(cross-lane)* `systems/settlements/sim/ledger.py`'s Record primitive (`LedgerTag`, `ledger_add`, `ledger_sweep`) has zero references to or from `systems/social_contest/` in either direction; three branch documents want to compose on it.
9. *(tests)* `engine/tests/test_pipeline_reach.py:838` reads `wrapper.GAMES[g]["resolve"](None)` directly and dies with `GAMES`; `01_SPINE.md` D9 already budgets its deletion.
10. *(process)* `systems/social_contest/_identifier_census.yaml` (68 KB) is untracked by git — a leftover of a prior pytest fixture, not a repo surface.
