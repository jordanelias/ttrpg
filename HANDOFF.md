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

**Only two items still need Jordan**, and neither was on this agenda: **ED-IN-0187's two HELD
degree sites** — `combat_engine_v1/core.py` (migrating collides with the ratified plate invariant)
and `sigma_leverage.degree` (whether the ruling overrides a deliberate pool-aware bar).

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
