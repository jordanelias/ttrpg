# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. **Nothing surfaces this file automatically** — the
SessionStart banner that used to relay "Next actions" was retired 2026-08-21 with the rest
of the session machinery (ED-IN-0194), and `CLAUDE.md` §0.3 records the result of the
experiment it was the instrument for. Read this file, and your lane's, yourself.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## ⚠ CURRENT — 2026-09-04, PR #368 (read this first; the 2026-08-27 section below is still true of `main`)

**The season loop can branch now, and the interesting number is how little.** Forking every
mechanical decision in the ARC/NPC corpus and following three decisions on: at session start
**2,403 forks changed nothing downstream**. Now the world diverges **100%** of the time and later
decisions diverge **~4%**. That gap is the result.

Concretely: `move` and `transfer` execute for the first time (650 and 702 across the corpus,
previously refused in every world), and success-vs-failure now leaves a trace a person can read —
the fold records *what it looked at* rather than *that it said no*.

**Full detail, the four retractions, and the open questions: `registers/handoffs/HANDOFF_IN.md`,
top section.** The short version a cold session needs:

- **Degree of success reaches nothing.** `_degree_for_writes` is hardcoded `None`, no verb declares
  `writes_by_degree`, `Event.degree` is never assigned, and the bands are unruled (`H-98`). A partial
  and an overwhelming success are identical today. Jordan asked for this next (W-E, 2026-09-04).
- **Ripple is throttled by design**: `assemble` takes ONE question per person per season and all
  three `H-54` arms return one; nothing accumulates in a person; cross-person transmission measures
  **zero**. Every term damps.
- **Two rulings wanted**: the undeclared content-hash tiebreak that decides which question a person
  answers, and `H-111` — whether a failure should occasion a decision.
- **Method**: producer → independent `valoria-critic` → fix pass, five items, a real defect found
  **every** time. Do not skip the critic half.

---

## ⚠ CURRENT — 2026-08-27 (read this first)

**`main` IS GREEN, and so is PR #334's head.** Measured 2026-08-27 at `d7578a6`:
`pytest tests/valoria -q -n auto` **1772 passed, 23 skipped, 15 xfailed**; `pytest engine/tests`
**1030 passed, 5 xfailed**; contest kernel suite **389/389**; `tools/valoria_local.py` all gates
passed; CI **All Gates Green**, including `Sim Reference Regression` — the campaign-gate that
ED-IN-0198 un-inerted, now completing in ~6m30s under its raised 20-minute cap.

### What landed 2026-08-27, and the one thing that moved output

Four commits. **Three were byte-identical and that was the point of each.** The evidence trail is
`registers/session_records/2026-08-27/` — two campaign captures and what they measure — and the
instrument is `tools/campaign_output_probe.py`, promoted out of `/tmp` where it had spent the
session licensing three commits.

| ED | what | output |
|---|---|---|
| **ED-IN-0199** | `engine/autoload/engine_clock.py` exists. `propagation_spec_v1.md` §O.1 has said since 2026-07-02 that engine_clock owns the tick composition; the module did not exist, `season.run_season` held the ordering, and the scheduler's two phase calls sat *inside* the ACTION phase's body. `next_tick()` left the scheduler in `_PHASE_ACTION` for all of accounting, and `keys.py` defers an `apply` on exactly that condition. | **identical** |
| **ED-SC-0031** | The ninth degree ladder — `sigma_leverage.degree`, the one the 2026-08-12 census missed — migrates to `dice_engine.degree_from_net`. | **MOVED** |
| **ED-SC-0032** | The injection seam: `dice_engine.BandExtension`. The contest's de-saturation rule leaves the engine for the subsystem that owns it and is injected by its wrapper. | **identical** |
| **ED-PC-0057** | The 40% covert-plate-killer ceiling is **abolished** (Jordan: *"stop arbitrary fiat capping"*). No replacement threshold. | n/a (test-only) |

**The ED-SC-0031 move is not a balance result.** Six of eight campaigns change winner at n=8;
`tools/balance_oracle.py` at n=120 per arm shows max |z| = 0.80 against a 1.96 threshold. Six
goldens were re-pinned on that basis. Full table in the session record.

### ⚠ POST-MERGE AUDIT (2026-08-27) — "are all decisions logged, ratified and propagated?"

Asked after #334 merged. **The answer was no, in three ways**, all now fixed. Recording the
result rather than only the fix, because each is a class this repo will hit again.

1. **A DUPLICATE ED ID SHIPPED.** The ceiling abolition was filed as `ED-PC-0041`, which had been
   allocated on 2026-07-29. `next_free` for PC read **57**; I filed 0041. CLAUDE.md §4 says read
   `next_free` and allocate THAT — never max+1, never a number you reasoned to. Renumbered to
   **ED-PC-0057** and propagated. **Nothing in CI cross-checks a lane's allocated ids against its
   pointer**, which is why a merged PR carried it; the audit was a one-line Python script.
2. **TWO JORDAN RULINGS WERE RECORDED NOWHERE.** A grep for their own words returned zero files:
   *"one faction write mechanism"* and *"key contracts and module contracts etc need to be
   explicitly defined in a centralized hierarchical manner"*. Both were given in the same
   conversation as "one degree ladder", which drew four commits. **The shape to watch: a ruling
   delivered alongside another, and satisfied by the tree's current state, is the one that gets
   silently dropped** — nobody decides against it, it just never becomes a work item.
   → **ED-FA-0038** (executed: the faction-write ruling was already substantially true, so what
   landed is the guard that was missing) and **ED-IN-0200** (ruled, NOT executed, filed `open`).
3. **PRE-EXISTING, NOT MINE, RECORDED NOT FIXED:** six duplicate ids in the IN ledger
   (`0012, 0013, 0016, 0029, 0149, 0162`, all July–August). CLAUDE.md §4 documents 0012/0013;
   the other four are undocumented. Not touched — the ED-306 precedent §4 cites says merged
   ledger lines are not rewritten unilaterally.

**The one gap left open by this audit:** no gate checks ledger ids against `id_reservations.yaml`.
A ~10-line test would have caught (1) and (3). It is not written here because minting a guard is
governed by §0.1 pt 5's predicate, and an id-allocation checker is load-bearing on this
repository's process rather than on the game — the predicate's own worked-example exclusion. The
honest disposition is that this class recurs and is cheap to detect, and that the predicate says
not to mint the guard. **Flagged for Jordan as a genuine tension, not resolved by me.**

### THE HIGHEST-VALUE WARNING FROM THIS SESSION

**ED-SC-0032 broke `tools/balance_oracle.py` and nothing caught it.** Moving `degree` out of the
engine left the oracle's arm reading `SL.degree`, so the default invocation raised AttributeError.
That is the instrument CLAUDE.md §7 names as *the* campaign-level balance control, and the one
whose n=120 run had licensed the previous commit's six golden re-pins — disabled by that commit's
own successor, found by an adversarial pass rather than by anything automated.

**The cause generalises and is the thing to carry forward: a deliberately-uncalled instrument has
no freshness relationship to the code it measures.** The oracle is not a CI gate on purpose (240
campaigns, ~13 min) and that is still right — but "not a gate" was silently doing the work of "not
tested at all". `tests/valoria/test_balance_oracle_arms.py` now constructs both arms and asserts
they band differently; it runs zero campaigns and costs milliseconds. **If you add another
deliberately-uncalled instrument, add its liveness test in the same commit.**

### Cross-lane items now OPEN

- **[PC — the big one] Derive Ob from the DEFENDER.** Jordan, 2026-08-15: Ob is *"their
  corresponding score/2 plus whatever specific modifiers exist for them in that instance"*, and
  `DECISIVE_OB` is dead. The sequence is settled and is the opposite of the obvious one: **derive
  Ob first, THEN combat's bands migrate.** This is genuine new mechanism, it is the last declared
  HOLD in `tests/valoria/test_degree_ladder_single_owner.py`, and it is what makes guandao reach
  47.5% on its own merits. The fiat ceiling that stood in its way is gone. See `HANDOFF_PC.md`.
- **[IN] §4.1's drain topology is NOT implemented.** `engine_clock.run_tick` calls
  `run_accounting` RAW — the shape `propagation_spec_v1.md` §4.1 explicitly names as its rejected
  earlier draft ("that was unbounded"). Bounded today only because accounting emits no Keys.
  Closing it is Phase E and is blocked on **R-1** (the D.6 double-count) and **R-4** (ORD-3
  observer ordering). See `HANDOFF_IN.md`.
- **[IN] ~38 flow-skeleton `file:line` anchors were re-based +5** when `module_contracts.yaml`
  grew a composition role. That preserves each anchor's existing offset and nothing more. An
  adversarial sample of 23 found **12 already stale** by larger, non-uniform offsets. **Nothing in
  CI validates a `.md` anchor's CONTENT** — `test_flow_skeletons` checks only symbol proximity.
  Repairing them is bounded but separate; a partial repair would present the unsampled remainder
  as verified.
- **[FA/WR] The parliamentary bridge's shut-out set has taken three values** under three unrelated
  mechanic changes (`{'Hafenmark'}` → `set()` → `{'Church'}`). That is evidence the property
  "the spine can eliminate a faction" tracks the seed, not the spine. Only ever measured at
  n=8/seed-42. Settling it needs the n≥100 arm.
- **[SC] The seam has exactly one consumer.** `PoolDesaturation` is the only `BandExtension` in
  the tree, so its contract ("veto the top band, nothing else") is proven by hostile probes rather
  than by a second real user. Expect that power to be what comes under pressure when a second
  subsystem wants an extension; widen it by ruling and ledger entry, never by convenience.

### Rulings received 2026-08-27, all executed or accepted

Recorded verbatim in the `RULINGS` block at `tests/valoria/test_degree_ladder_single_owner.py`,
which is now the single home for the degree-ladder rulings — it exists because ED-SC-0032 nearly
deleted its own authority (removing the HELD entry that was the *only* in-tree record of the
ruling authorising its shape).

1. *"so plan to resolve it then if you know what to do!"* → the injection seam. **Executed.**
2. *"yes accept. if you don't have enough dice you don't have enough dice"* → a pool-2 contest can
   never resolve Overwhelming. **Accepted, settled, not to be re-raised.**
3. *"dude guandao not being able to hit 47.5% on its own merits is fucked up. stop arbitrary fiat
   capping"* → the 40% ceiling. **Abolished**, and it **overrode a sequencing objection I had
   raised** — recorded rather than dropped, because the objection was about convenience and the
   ruling is about whether the thing should exist.

---

## Prior — 2026-08-25

**`main` IS GREEN.** Measured 2026-08-25 at `571ae14`: `tests/valoria` **1723 passed, 23 skipped,
15 xfailed, 0 failed**; `engine/tests` **2055 passed, 5 xfailed**. Both measured twice, by two
independent sessions, agreeing.

~~**`main` IS RED** … **22 `tests/valoria` failures on `main`**~~ — that block stood here from
2026-08-24 and was falsified by the very next commit: `571ae14` (PR #331) fixed the port-tail
failures and did not update this file. So the repo's front door — the file CLAUDE.md §1 tells every
session to read second — kept directing work at a `main` that was already green. Struck rather than
deleted, because the failure mode is the thing worth seeing: the tip commit fixed it and the
continuity file never learned.

✅ **THE RUNNER CAVEAT IS SOLVED, AND THE CAUSE WAS NOT FAIL-FAST.** `engine/tests` had never once
completed on a CI runner, and the reason was mundane: **`sim-regression` carried
`timeout-minutes: 5` while the suite takes ~6m15s** (375-383s, measured four times on 2026-08-25).
The job was killed mid-run every time, deterministically. GitHub reports a timeout kill as
`cancelled` rather than `failure`, and `All Gates Green` then fails on "not success" — which is how
this got read as "fail-fast cancelled it every run" and stayed unexamined.

It was never fail-fast, and no push was racing it: on PR #333 the cancellation reproduced three
times, once with no push in the window and `origin/main` unmoved, always at ~5m15s. The 16-minute
cap that made the timeout look impossible belongs to `unit-tests`, a different job.

A §0.1 point 5 pattern defect — correct when written, broken because something else changed. The
step's own comment said "~20s", true when the cap was set; the mass-battle port grew the suite by
two orders of magnitude and nothing re-derived the cap. Raised to 20 minutes (ED-IN-0198), ~3x the
measured runtime. **This means the campaign-level regression gate has been inert since the suite
outgrew the cap — every merge in that window shipped without it.**

**The master record is `registers/handoffs/HANDOFF_2026-08-24_SESSION.md`** — throughlines, warnings,
loose ends, and the order to work in. Read it before anything else. Two executable plans sit beside
it (`proposals/2026-08-24-completion-plan-v1.md`, `proposals/2026-08-24-error-regions-v1.md`); the
master document says when to open them.

**Before running any gate locally** — a bare local run diffs ONE commit while CI diffs the whole
branch, so a local green can be vacuous:

```sh
git fetch origin main && export GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main
```

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

**▶ THE STEP TO TAKE: `proposals/2026-08-21-execution-order-v1.md` §3, first step whose `state:` is
`next`.** Written 2026-08-21 at Jordan's request. It is **not** a tenth planning surface: it replaces
§5 (Sequencing summary) of `proposals/2026-08-20-return-to-game-plan-v1.md` and nothing else — that
document is still the authority on what each act is and why. If you are about to write a new plan
instead of taking a step, that is the loop; take the step.

`state: next` is **S7 — wave 4's residue: extraction, not culling** (the `audit/` corpus: ~33
game-subject working papers whose surviving conclusions belong in `systems/` heads or `proposals/`).
S6 closed 2026-08-23.

⚠ **This line was stale for three steps** — it said S4 while S4, S5 and S6 had all landed. The
execution order's own `state:` fields are the authority when this file and a step disagree, and a
memoryless session that trusted this pointer would have re-done finished work. Re-read the step's
own `state:` before starting.

**S6 closed with five of six pieces landed and 6c RECLASSIFIED, not skipped.** `deprecated/` no
longer exists (its 26 frozen ED-ledger fragments relocated to `registers/archive/` — 25 of them
parsed, the `.md` index walked and skipped as before — universe unchanged at 1,264 ids); a `FORK:` row has one meaning, `FORK:<ref>:<path>`; the naming trio is two.
Four of S6's six instructions were wrong when measured, and one would have cut a blocking gate's
population 63 → 7 entries while reporting green. Read the plan's S6 RESULT before S7.

⚠ **6c (slim the handoffs) DID NOT RUN, and the reason binds anyone who tries it.** Its headline —
"≥75% of `HANDOFF_IN.md` is narrative about completed work" — measures at **21%** corpus-wide, and
that 21% cannot be swept either: **12 of 17 sections marked `[DONE]`/`[RULED]`/`EXECUTED` carry
open, held or `needs_jordan` items inside them**, as does `HANDOFF_archive.md`, whose own header says it is "not a
continuity surface" and which carries "Residual for Jordan: 13 needs_jordan". **The disposition
markers in this corpus do not mean what they say.** Pruning it is adjudication work, not a culling
wave — the same correction this document's S7 already applies to `audit/`.

**S8 Half A LANDED — the game moved.** `sigma_leverage.roll_net_continuous` no longer rounds its
pool, so Jordan's 2026-08-14 fractional-dice ruling is implemented rather than half-implemented. Six
goldens re-recorded against `tools/balance_oracle.py` (NEW — the n>=100 control
`engine/tests/test_f7_smoke_oracle.py:8` has demanded since it was written): 120 campaigns per arm,
no faction shifts significantly, so the goldens moved from RNG divergence and not from balance.
Combat's byte-exact goldens are the control and did not move.

**S8 Half B SUSPENDED 2026-08-21 by Jordan — flagged for later systems work. Do not wire it.**
The classification found the board's claim that `score/2` is "wired NOWHERE" to be FALSE: of three
OPPOSED sites, `coronation_renewal_ob` already implements `floor(L/2)+1`, `tribunal` implements it
under formal grounds, and only `parliamentary_transfer` contradicts it — with `L+2` stated as canon
in its own design doc. Reconciling them would overwrite ratified canon and collapse tribunal's
two-tier resistance mechanic. Classification: `registers/handoffs/HANDOFF_FA.md`. Pinned against
drift by `tests/valoria/test_faction_obstacle_conventions.py`.

✅ **RESOLVED 2026-08-22 — the tag is no longer load-bearing, so the blocker is gone rather than
outstanding.** This warning used to read: push `refs/tags/cull-2026-08-21-pre-waves-1-3` before this
branch merges, because the ledger's FORK rows pointed at `421cff2` and would dangle otherwise. The
tag push had returned HTTP 403 from this session's credential, so the blocker was real.

It is closed by re-pointing rather than by pushing. All **83** `FORK:` rows in
`references/restructure_ledger.md` now name **`1e4c6f4`**, which is `origin/main`'s own tip —
`git merge-base --is-ancestor 1e4c6f4 origin/main` succeeds, so squash, rebase and merge-commit all
leave every row resolvable. The tag remains a nice-to-have, not a precondition.

⚠ **AND THE HALF THIS WARNING PREVIOUSLY MISSED, now also closed.** Re-pointing the ledger fixed the
ledger and nothing else: **twenty-eight further citations of `421cff2` were still live on eight
tracked surfaces** — `CLAUDE.md` §8, `CURRENT.md` ×2, this file, fourteen rows of `tools/README.md`,
and three *game-design* flow skeletons (`systems/settlements/` ×10, `systems/fieldwork/`,
`systems/ui/`). `421cff2` is a **branch-local rebase commit** — `git branch --contains` names only
this branch — so a squash-merge annihilates it and dangles every one of those, which is exactly the
fabricated-provenance failure PR #288 caused once already.

All twenty-eight are re-pointed to `1e4c6f4`, verified byte-identical at both refs
(`git rev-parse 421cff2:<path>` == `git rev-parse 1e4c6f4:<path>` for a sample of six) and present
there. **Zero live citations of `421cff2` remain.** Found by an adversarial read-only pass, not by a
tool: nothing in the tree distinguishes a squash-mortal ref from a durable one, and that gap is still
open — the lesson is that re-pointing a ledger is not the same as re-pointing the corpus that cites
the same ref.

**There is no SessionStart banner.** Wave 3 retired it; `CLAUDE.md` §0.3 records the experiment's
result. Orient from `CURRENT.md`, this file, and the execution order. Do not build a replacement.

_Cross-cutting items only — lane-owned work lives in `registers/handoffs/HANDOFF_<LANE>.md`.
Rewritten 2026-08-14 (ED-IN-0189): this section had opened with a blocker resolved 2026-07-30 and
carried nothing newer than July, while being **the only section the SessionStart banner reads**.
Everything struck from it was already recorded in `HANDOFF_IN.md` or the ledgers; nothing was lost,
and the July narrative is in `git log HANDOFF.md`._

### ▶ THE DELIVERABLE (2026-08-19) — build the game; `done` means it runs

**RULED 2026-08-19 by Jordan: "I need to break out of the infrastructure loop in the repository."**
The doctrine amendments that terminate it are live in `CLAUDE.md` §0, §0.1 pt 5, §0.2, §0.3 — read
those first, because they change what you are allowed to produce.

**Your work is the current M1 juncture, and nothing else.** The banner prints it and whether it
runs. `done` means the behaviour executes (§0.2) — never that a document exists with a `## Status:`
line. `python tools/m1_acceptance.py --summary` is the instrument.

**Three rules that override the habit of this repository:**
1. **A finding that needs no ruling is fixed in this commit or dropped.** Not filed. The adversarial
   pass is a stage, not a deliverable — at most one paragraph in the commit message, and at most one
   ledger row, only if it needs a human (§0).
2. **A guard must be load-bearing on the game or on a Jordan decision** (§0.1 pt 5). A defect in an
   artifact that only this repo's process depends on means that artifact can be wrong without cost:
   delete it, or accept it and write nothing.
3. **Work is this session's work only if Jordan asked for it this session, or it traces to an open
   M1 juncture.** If something broken blocks the milestone, fix it minimally, without adding a guard.

**Do not open a new planning surface.** There are nine. The measured cost of the tenth is in §0.3.

---

**Program state (PR #323).** The Return-to-Game queue `workplans/return_to_game_queue.yaml` ran S0,
S1, S2 on 2026-08-19. It is **superseded as the steering surface**, is a **reference not a queue**,
and its own header now says so. Do not resume it; do not run its driver; **S7 is inert and must not
be executed** (it would prepend to the banner that §0.3 declares a running experiment).

**The 19 residuals are DISPOSITIONED, 2026-08-19 — they are not a backlog.** An earlier version of
this paragraph said "keep it for the measured facts and the 19 parked residuals", which read as live
work and was flagged by three independent audits as this commit's own doctrine violated by the
commit that installed it (§0: *a finding that needs no ruling is either fixed in this commit or
dropped*). Disposition:
- **14 carry `needs_ruling: false` → DROPPED.** They are apparatus findings about this repo's own
  machinery. Under §0 they had to be fixed here or dropped, and they are dropped. They remain
  readable in the file as history; **nothing may take them as work.** Do not re-file them.
- **5 carry `needs_ruling: true`** (S0-R1, S1-R1, S2-R1, S2-R2, S2-R4) → they are legitimate under
  the row gate, but they live in a workplans YAML rather than the `needs_jordan` ledger queue, which
  is a second uninstrumented home for human-decision items. Route them through Jordan's docket.
- What is worth keeping is the **measured facts**: the controlled compile numbers, the gate tier,
  the failure decoder.

| | | |
|---|---|---|
| **S0** | `done` | IN ledger 49,920 → 45,998 tokens; `gates:` measured; push scope live. |
| **S1** | `blocked` | Compile improved, not clean. Code in **jordanelias/valoria-game#2**. Do NOT re-run its fix loop — it provably converges to that state. |
| **S2** | `done` | `m1_acceptance` rows 1-2 now measured from a real probe season. Row 1 honestly **FAILs**. |

⚠️ **The compile numbers, measured like-for-like with fresh caches** (the advertised `5/14/8` is
unreproduced and now unretestable): excluding `res://tests/` **41/156/61 → 14/63/21**; including
them **54/169/74 → 27/76/34**. The old `54/169/61` baseline is itself arm-mixed.

⚠️ **Two traps that cost real time.** A warm `.godot` cache silently truncates the scan (51 vs 235
gate-matching lines on an identical tree) — always `rm -rf .godot` first. A leftover driver worktree
under `.claude/worktrees/` falsely reds a blocking unit test; it fired on four of four runs.

⚠️ **`valoria-game` CI is not evidence.** Its `GDScript Lint` job reported green on a tree with 97
compile errors; `find -exec` does not propagate exit status and it never parses GDScript.

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
  changed.** ~~TN 6/7/8 (Controlled/Standard/Desperate) remains canon as a *situational* scale.~~
  ⚠ **SUPERSEDED 2026-08-25 — Jordan, verbatim: "TN7 always. Never change TN anywhere ever."** There
  is no situational scale and no other TN. A varying difficulty is an **Ob**, never a TN. Enforced in
  code, not prose: `engine/autoload/dice_engine` raises on any other value, and
  `tests/valoria/test_tn7_always.py` fails on a re-introduction (ED-IN-0196, ED-MB-0066).
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

### ✅ PARTLY RULED 2026-08-23 — faction stats (asked 2026-08-15, ruled 2026-08-23)

> **Jordan ruled two of the four calls below. Read this box before the evidence, which is preserved
> as it stood when the question was asked.**
>
> * **Call (1) — which roster.** RULED: **"Legitimacy is a base."** `fac.legitimacy` is declared in
>   `references/descriptor_registry.yaml` and bound to the `Faction.L` field. The roster is **six**
>   on both sides; the 5-vs-6 disagreement below is closed.
> * **Call (4) — is the scale 0–7 or 1–7, uniformly.** RULED: **"Influence can be 0."** Uniformly
>   **0–7**. This supersedes ED-IN-0029's Influence floor of 1, so the inconsistency the evidence
>   below calls out as deciding "whether a faction can present a zero obstacle" is resolved — it can.
> * Jordan's rationale, which is what makes call (1) a change of model rather than a reversal:
>   *"now that we're using continuous, we don't have to worry near as much either as we can just
>   aggregate these stats as opposed to weird derivations."*
>
> **STILL OPEN — calls (2) and (3), and they are not touched by the above:**
> * **(2) is Mandate a base stat or derived from settlement L/PS.** Still derived. `fac.legitimacy`
>   is NOT Mandate, and the ruling does not make Mandate a base stat. ⚠ The code stores Mandate *as*
>   `Faction.L` in places (`parliamentary_bridge` still comments *"Mandate == Faction.L pre-LPS-1"*),
>   so what is settled is that the FIELD is a declared descriptor with declared bounds — not what
>   every call site writing it means. That conflation is ED-FA-0004 and is still open.
> * **(3) does Treasury exist separately from Wealth.** Untouched.
>
> Wired in `ca0ff0c`; supersessions recorded in `registers/supersession_register.yaml`.

The evidence below is preserved AS ASKED (2026-08-15) and is deliberately not rewritten — it is the
record of what was put to Jordan. Where it states the roster as 5 or Influence as 1–7, read the box
above.

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

### ⛔ WITHDRAWN 2026-08-19 — this section used to hand out apparatus work as "no ruling needed"

It listed tracks **B–E** of `audit/2026-08-14-five-lens-repo-assessment/01_plan.md` — owner-in-code
sweeps, gate-perimeter widening, `sys.path.insert` governance across 131 test files, vocabulary
entries — under the heading *"Open and agent-executable — no ruling needed"*. Every item is
audit-sourced work on this repository's own machinery, pre-authorised for any session that read
this file. That is precisely the T3 carrier CLAUDE.md §0.3 describes, sitting in the continuity
surface, and it is now excluded twice over: by §0's selection term (work is this session's work only
if Jordan asked this session, or it traces to an open M1 juncture — none of B–E does) and by §0.1
pt 5 (the artifacts are load-bearing only on process). **Do not take this work. Do not restore this
section.** The plan file still exists if a human ever wants it.

**One item from it survives, because it is the opposite of apparatus** — it is engine code on the
critical path of M1 juncture 1, which is why the board now names it as the increment:

- **The largest unimplemented piece of the #311 ruling:** obstacles as score/2 plus modifiers is
  **wired nowhere** (`engine/autoload/dice_engine.py:118-123` says so itself). Paired with
  fractional dice pools (`sigma_leverage.py:284` still does `int(round(pool))`). See the board.

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
