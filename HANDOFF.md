# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## History

Full narrative for the work below (2026-06-24 through 2026-07-02) moved to
`registers/handoffs/HANDOFF_archive.md` (2026-07-08, token-efficiency pass) — this file had drifted from
"index" to a full append-only session log. Nothing was deleted, only relocated; the archive is
frozen, do not resume work from it.

Per-lane continuity now lives in `registers/handoffs/HANDOFF_<LANE>.md`, using the same 9 lane codes as
the `ED-<LANE>-NNNN` editorial namespace (`ED-IN-0001`, `CLAUDE.md` §3). This file is the
**index** plus genuinely cross-cutting items — read the lane file(s) relevant to your session
before starting work, and keep your own updates scoped to your lane's file (or this one, only
for cross-cutting items).

| Lane | Subsystem | File |
|---|---|---|
| `MB` | Mass battle | `registers/handoffs/HANDOFF_MB.md` |
| `PC` | Personal / scene combat | `registers/handoffs/HANDOFF_PC.md` |
| `FI` | Field investigation | `registers/handoffs/HANDOFF_FI.md` |
| `SC` | Social contest | `registers/handoffs/HANDOFF_SC.md` |
| `FA` | Faction actions | `registers/handoffs/HANDOFF_FA.md` |
| `WR` | World | `registers/handoffs/HANDOFF_WR.md` |
| `IN` | Infrastructure / cross-cutting | `registers/handoffs/HANDOFF_IN.md` |
| `GO` | Godot conversion | `registers/handoffs/HANDOFF_GO.md` |
| `SE` | Settlements | `registers/handoffs/HANDOFF_SE.md` |

**Why the split:** the ID-collision incidents that motivated `ED-<LANE>-NNNN` (two same-session
concurrent-allocation collisions on the flat sequence within one PR — see `ED-1094`'s ledger
entry) are the same failure class that makes one shared `HANDOFF.md` a merge-collision magnet
once multiple lane-sessions run concurrently. This is a **partial, deliberate exception** to the
repo's earlier "one continuity surface" consolidation (`deprecated/session_machinery/` retired
per-topic session-log files because they rotted independently) — the difference is this split is
keyed to the SAME lane taxonomy the ID system already enforces, not an ad-hoc per-topic split,
and this root file remains the one stable SessionStart entry point.

**Full detail on the split itself, and every historical decision predating it, is filed at
`registers/handoffs/HANDOFF_IN.md`'s Decisions log** — this root file does not duplicate that history.

## Next actions

_Cross-cutting items only — lane-owned work lives in `registers/handoffs/HANDOFF_<LANE>.md`.
Rewritten 2026-08-14 (ED-IN-0189): this section had opened with a blocker resolved 2026-07-30 and
carried nothing newer than July, while being **the only section the SessionStart banner reads**.
Everything struck from it was already recorded in `HANDOFF_IN.md` or the ledgers; nothing was lost,
and the July narrative is in `git log HANDOFF.md`._

### ▶ RUN THIS (2026-08-19) — `workplans/return_to_game_queue.yaml`

**The Return-to-Game program. It is an executable queue, not a plan to read.** Open the queue file,
read the block at the top, take the first `state: pending` step whose precondition holds **on disk**,
run it through `.claude/wf_return_to_game.js`, commit, write the state back, and stop when your
context is degrading. There is nothing to ask anyone.

**▶ NEXT PENDING STEP: `S2` — arm the acceptance oracle.** Its precondition is `none`. S3/S4 need S1;
S5 and S7 are independent; S6 needs S2; S8 needs S0.

**Progress (2026-08-19, PR #323 on `claude/return-to-game-execution-74fdvc`):**

| step | state | outcome |
|---|---|---|
| **S0** | `done` | IN ledger 49,920 → **45,998** tokens (headroom 80 → 4,002); `gates:` populated; push scope verified. Zero overturns across 42 verdicts. CI green. |
| **S1** | `blocked` | Game compiles far better but not clean. Code landed as **jordanelias/valoria-game#2**. |
| S2–S8 | `pending` | — |
| S0-R1..R6, S1-R1..R7 | `blocked` | 13 residuals parked with `file:line` — never guessed, never silently fixed. |

- **The entire human ask is `jordan_docket:` — seven one-sentence questions, each with a
  recommendation**, down from 109 open `needs_jordan` rows. Answer D1 first if you answer only one;
  it is the multiplier that keeps the queue drained. **No step in the queue waits on any of them.**
- **Order matters and is load-bearing.** S1–S4 change what "done" means here from a document state to
  a program state. S5–S8 shrink things afterward. A cull or a reconcile run while `done` still means
  "a document exists" is the ninth consolidation plan.
- ⚠️ **S1 is `blocked`, and that is the honest verdict, not a failure.** A true fixed point was reached
  and verified byte-identically, so the "zero fixes applied this iteration" half of PASS holds;
  `errors.txt` is 97 lines, so the "empty" half does not. **Do not re-run S1's fix loop — it provably
  converges to exactly this state.** What remains is S1-R1 (needs a numeric ruling), S1-R2 (annotation
  work Group C scoped out) and S1-R4 (no CI compile job exists yet).
- ⚠️ **The `5 / 14 / 8` endpoint previously advertised here is UNREPRODUCED and now unretestable**
  (the scratch copy is gone). Measured like for like with fresh caches in both arms, Godot 4.3 against
  `valoria-game@5e01065`:

  | | failed-to-load | parse errors | broken scripts |
  |---|---|---|---|
  | excluding `res://tests/` | 41 → **14** | 156 → **63** | 61 → **21** |
  | including `res://tests/` | 54 → **27** | 169 → **76** | 74 → **34** |

  The old `54/169/61` baseline is itself **arm-mixed** — two including-tests numbers paired with one
  excluding-tests number. Always state the exclusion convention with the triple (S1-R5/S1-R6).
- ⚠️ **Two traps that cost real time this session.** (1) A warm `.godot` cache silently truncates the
  scan — 51 vs 235 gate-matching lines on an *identical* tree. Always `rm -rf .godot` first. (2) A
  leftover driver worktree under `.claude/worktrees/` falsely reds a blocking unit test, so the full
  suite reports 1 failed / 1932 passed for a reason unrelated to your diff (S0-R5). `git worktree
  remove --force <path> && git worktree prune`, then re-run.
- ⚠️ **`valoria-game` CI is not evidence.** Its `GDScript Lint` job reported **green on a tree with 97
  compile errors** — `find -exec` does not propagate exit status and the check never parses GDScript.
  Its `Naming Consistency` job is red on `main` too (12 pre-existing `maret_vossen` hits).

### ⭐ READ SECOND (2026-08-18) — `proposals/2026-08-18-next-session-handoff.md`

The recursion investigation (PR #319) and its Fable-5 adjudication (PR #321) are complete. That
handoff carries **six unblocked, verified actions that move the game**, the five items held for
Jordan, the findings not to re-derive, and the traps this session hit. Highest-leverage first:

- **Put a Godot compiler in CI.** In 3,728 commits nothing has ever checked whether the game
  compiles. It was compiled for the first time this session: five root causes plus one
  `project.godot` setting took it from 58 errors to 16, and 5 of 6 autoloads then load.
- **The "unnamed tenth attribute" is `Recall`** — named outright in this repo at
  `engine/engine_params/params_tables.yaml:9118`. Naming it lifts the "do not bind Godot fields
  yet" flag this banner prints every session. Jordan's call.
- **The `domain_actions` gap** — junctures 1–2, `blocked_on: None`, open since 2026-07-05 — is
  implemented as `valoria-game/systems/engine/DomainActionSystem.gd`, 276 lines.
- **The Key-type gap is exactly 20 rows**, a strict subset with zero drift, recounted twice.

⚠ **Do not open another audit of the apparatus.** The measured finding is that 78% of commits whose
subject line says consolidate/cull/prune/retire were **net line increases**.

### Ruled and landed — do not re-raise

- **Jordan's ruling session landed 2026-08-14 (PR #311, ED-IN-0187/0188).** The **degree ladder** is
  single-owned by `degree_from_net` in `engine/autoload/dice_engine.py` and reads the **margin**
  (net − ob): ≥3 Overwhelming, ≥1 Success, [0,1) Partial, <0 Failure. The Ob-scaled 2×Ob bar, the
  PP-232 floor and the Ob-20 exception are **ruled out**. **Faction actions roll d10** through
  `sigma_leverage`; the d6/4+ convention is gone. `CONQUEST_MIN_MIL` is deleted.
  ⚠ **Behaviour changed:** a roll clearing zero but falling far short used to read Partial and now
  reads Failure. Six seeded-campaign goldens moved, each re-recorded with its cause.
- **Mass battle: the canon question is CLOSED and has been since 2026-08-03 (J2).** Canon is
  `tests/sim/mass_battle/` (11,269 lines, ~30 modules — the big one). `systems/mass_battle/sim/`
  (2,385 lines) is retired but still runs the live campaign until `faction_action.py` migrates.
  J2 is recorded at `systems/mass_battle/sim/__init__.py`. **Five independent audit lenses re-raised
  this as open in August because `CURRENT.md` narrated the tension twice.** That narration is now
  deleted. If you find yourself about to file it again, read the `__init__.py` header first.

### The ruling agenda is CLOSED — ruled 2026-08-14, do not re-raise

**Corrected 2026-08-15 (ED-IN-0191).** This section previously listed Q1b/Q4/Q5/Q6/Q7 as *"open
and needing Jordan"*. **They were already ruled when it was written.** PR #312 (ED-IN-0185, flipped
`proposed` → `ruled`) records Jordan's verbatim answers; I wrote this section without them and
rebuilt the exact T5 trap the assessment had just named — a settled ruling re-surfaced as open
work, in the one section the SessionStart banner reads. The verbatim answers live in `ED-IN-0185`
and in the banner on `audit/2026-08-14-five-lens-repo-assessment/01_plan.md` §2. Read those, not a
paraphrase.

| Q | Ruling (Jordan, verbatim where short) | State |
|---|---|---|
| Q1a | CURRENT.md history: *"a delete. only include instructions to read most current commits, and where to read registers/logs/indexes"* | **EXECUTED** (ED-IN-0189) |
| Q1b | *"b generate, never hard code"* — the head-per-subsystem table | **RULED, not executed** |
| Q2 | *"3 or more is always overwhelming"*; a met-but-not-exceeded obstacle is a partial | bands **EXECUTED**; the **score/2 obstacle derivation is wired nowhere** — the largest outstanding piece |
| Q3 | *"d10 always using fractional dice and fractional obstacles, sigma leveraged"* | d10+sigma **EXECUTED**; ⚠ **fractional DICE are not implemented** — `roll_net_continuous` does `int(round(pool))`, so pools are still whole dice and only the *result* is fractional |
| Q4 | *"b"* — blanket-mark historical-resolves-at-fork, checker verifies format | vocabulary + freeze gate **EXECUTED** (ED-IN-0188, ED-IN-0190); the **433-citation sweep is not done** |
| Q5 | *"chunk as per a, just ensure you have a companion index for them"* — numbered continuation, full file frozen, **plus a companion index** | **RULED, not executed** |
| Q6 | *"restore"* — CLAUDE.md §5–§7; plus *"q6 active"* for the lane | lane **ACTIVATED** (ED-GO-0001); ⚠ **the §5–§7 restore is NOT done** — 327 dangling citations across 176 files |
| Q7 | *"it will be 10 attributes, and delete the code that blocks itself from being ported as that is stale"* | **RULED, not executed.** The roster ships **nine** today; **the tenth is UNNAMED** — naming it is the workshop, the count is not |

### Resolver architecture — RULED 2026-08-15

Jordan, in session. These close the two HELD degree sites and set the extension pattern.

- **ONE resolver for all d10 probability.** Rolls are adjusted by **standard deviation (sigma)** —
  that is our word; "volatility" is used nowhere. `engine/autoload/sigma_leverage.py` is the sigma
  surface, `engine/autoload/dice_engine.py` owns the ladder.
- **TN 7 — "a roll of 7 or higher is a success"**, equivalently "above 6". Both readings were in
  circulation; they are the same rule and the ambiguity is now closed at the owner. **No constant
  changed.** TN 6/7/8 (Controlled/Standard/Desperate) remains canon as a *situational* scale.
- **All weapons are TN 7** — "now that we have a physics engine". Weapon speed is carried by the
  physics (reach, mass, percussion authority, recovery), never by the TN. ⚠ The engine **already**
  did this (`core.py:46`, `TN = SL.TN_STANDARD`); the per-weapon TN 5–8 existed only in prose and is
  corrected.
- **Degree bands are universal.** Failure below Ob · Partial from Ob to Ob+1 · Success at Ob+1 or
  more · Overwhelming at Ob+3 or more. This is exactly what `dice_engine.degree_from_net` already
  implements, so **the ladder itself needs no change** — only the systems that bypass it.
- **No system keeps its own bands.** Where a system genuinely needs a modification, the **wrapper
  injects the engine** so the change is clean and visible — never a private re-banding.
- **`DECISIVE_OB` is dead** — *"stupid as hell … Ob should be determined by your opponent more than
  anything"*. Combat's fixed Ob of 3 goes; the obstacle becomes the opponent's **score/2 plus that
  instance's modifiers**.

**THE SEQUENCE MATTERS AND IS COUNTER-INTUITIVE.** Combat is *not* migrated bands-first. Derive Ob
from the defender **first**, then the owner's ladder applies directly. `core.py`'s own docstring
predicted this: calibrating against the fixed-Ob form first "would be work thrown away". Both HELD
entries in `tests/valoria/test_degree_ladder_single_owner.py` now record the ruling and this order;
delete a HELD entry when its migration lands, not before.

**Not yet executed:** the combat Ob derivation + band migration (PC lane, a real redesign with a
measured balance delta — Jordan: migrate, measure, **report before tuning**), and the
`sigma_leverage.degree` migration (flips `degree(3,3)` from 2 to 1, pinned by 151 groundup tests and
`_kernel_tests.py`). Also still open: **fractional dice** (`roll_net_continuous` does
`int(round(pool))`).

_(The two HELD degree sites that previously sat here as needing Jordan are **RULED** — see the
section above. Nothing on the ED-IN-0185 agenda is awaiting a decision.)_

### NEEDS JORDAN — faction stats (asked for 2026-08-15, evidence gathered, not ruled)

Jordan asked to rule faction stats and the session closed first. Everything needed to rule is below;
nothing was changed.

**The registry and the code disagree about what a faction *is*.**

| | Roster |
|---|---|
| `references/descriptor_registry.yaml` declares **5** | Influence (1–7) · Wealth (0–7) · Military (0–7) · Intel (0–7) · Stability (0–7) |
| `engine/autoload/game_state.py` implements **6** | `L` · `Sta` · `W` · `I` · `Mil` · `intel` |

The conflict is `L`. The registry's own note says **"Mandate is a size-weighted derived aggregate of
settlement L/PS — NOT a base attribute."** The code stores Mandate *as* the base scalar `Faction.L`.
That is ED-FA-0004, still open.

**Three things exist only in comments, never as code:** `Treasury`, the Mandate formula
`7T/(T+6)`, and the per-settlement L/PS → Mandate pipeline. `Faction` has `W` (Wealth) and no
Treasury; whether those are the same thing is undecided.

**The registry's cited source is gone** — `engine/params/factions/stats_1_7_scale.md` was evacuated
2026-08-05 (resolves at fork `c451bcb`).

**Why this now matters more than it did:** obstacles are ruled to be **score/2 plus modifiers**, so
the faction stat roster *is* the faction obstacle surface. A 0–7 stat yields obstacles 0–3.5, and
**Influence is 1–7 while every other stat is 0–7** — that inconsistency decides whether a faction can
present a zero obstacle.

**The calls:** (1) which roster — the declared 5, the coded 6, or another; (2) is Mandate a base stat
or derived from settlement L/PS; (3) does Treasury exist separately from Wealth; (4) is the scale
0–7 or 1–7, uniformly.

### Open and agent-executable — no ruling needed

- **The remediation plan's remaining tracks** (`audit/2026-08-14-five-lens-repo-assessment/01_plan.md`).
  Track A is done as of this commit. Still open: **B** (owner-in-code — `TN_STANDARD` has three live
  definitions and none in its owner `dice_engine.py`; the bare-RNG sweep; register
  `single_owner_check.py` in `ci_checks_registry.yaml`, whose absence makes CLAUDE.md §4 false as
  written), **C** (gate perimeter — `validate_ed_citations` cannot see `audit/`;
  `broken_dependency_checker` cannot see `engine/` at all), **D** (`tests/` governance — 159
  `sys.path.insert` across 131 files, no registry), **E** (godot status line, vocabulary entries,
  the `WI = End+6` transcription defect in `combat_reference_v1.md:218,347`).
- **The plan's binding rule, and it is the point:** a step may add a guard **only** in the same commit
  as a burn-down of the thing it guards, and every ratchet it touches must leave with a **lower**
  pinned maximum. If the guards land and the burn-downs do not, the plan has failed by its own
  standard.
- **The largest unimplemented piece of the #311 ruling:** obstacles as score/2 plus modifiers is
  **wired nowhere**.

### Standing state

- **M1 (one playable season) — 0 of 7 junctures done.** Junctures 1–2 have no owning design doc at
  all (`domain_actions`). Board: `workplans/workplan_v6_progress.yaml`, refreshed 2026-08-14.
- **Of the 25 commits before #311, 19 were IN-lane infrastructure.** The repo's own assessment of
  that period: *"instrumented the disease more than it cured it."* Weigh a new instrument against
  that before building one.
- **~121 ledger items are flagged `needs_jordan`** across the lanes (IN 29, SE 23, SC 17, FA 15,
  flat 14, PC 9, MB 8, FI 3, WR 1). Re-raising a settled one costs more than leaving one unruled.
- **ID protocol unchanged:** the flat `ED-NNNN` sequence is FROZEN at ceiling `ED-1096`. All new EDs
  are `ED-<LANE>-NNNN` from `references/id_reservations.yaml`'s `lane_ids` — read `next_free`,
  allocate, bump, co-commit. Never max+1.
