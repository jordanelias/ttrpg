# THE PLAN — governance · settlements · behaviour: every live item, in one order, across every lane

> **RENAMED 2026-09-18 (`ED-IN-0254`), on Jordan's instruction.** It was
> `workplans/2026-09-11-reconciled-program.md`, and the date was the problem: *"2026-09-11 is
> misleading as if anything is sorted by date, then it will appear old."* A creation date on the
> LIVING plan reads as staleness, and `CLAUDE.md` §4 already says a filename cannot carry currency —
> *"Only `CURRENT.md` and a head's `## Status:` line can tell you what is current."*
> **Both old paths resolve** through `references/restructure_ledger.md` via `tools/pathres.py`
> (verified `ALIASED`), so every citation in the frozen registers and the 09-17 suites still points
> here. **Prose still calling this "the reconciled program" means this file.**

## Status: **RATIFIED 2026-09-12 (ED-IN-0215). AMENDED 2026-09-18 (`ED-IN-0253`) INTO THE SINGLE PLAN, ON JORDAN'S INSTRUCTION** — *"I need one single clearly defined plan"*, and his choice of option (b): fold the governance build order in, land the contested-ownership commit, stop maintaining two. ⚠ **THE CONTESTED-OWNERSHIP NOTE IS RESOLVED AND THIS IS THE COMMIT IT ASKED FOR.** It read: *"§0's claim to be the single owner of the ORDER across all lanes is contested — `workplans/2026-09-11-arc-sequence-spine.md` positions 2–15 remain independently actionable, and `valoria_master_workplan_v7.md` §6 records that the collision is open and needs a commit rather than a paragraph."* **§3 is now the only ORDER in the repository.** The spine, the governance build order and the gather's amendment are subordinated by header line to this file and own CONTENT only. ⚠ **STILL SCOPED:** the 2026-09-12 merge ratified §3's order and §1's supersession verdict and nothing else; §5's rulings and §7's held-back items are untouched here. ⚠ **§3 WAS RE-SEQUENCED, which §8 previously declined to do** — *"the sequence is RATIFIED and this session did not re-sequence it"*. That restraint was right without an instruction and is superseded by one. **No existing position number changed**; new rows use the lettered sub-position convention (`13b`, `19b`, `ED-IN-0242`) so no citation in the tree dangles, and §3.4 maps every folded item. ⚠ **AMENDED 2026-09-25 (`ED-IN-0270`): §3.1 RE-SEQUENCED INTO FOUR PHASES, AND §3.2's GOVERNANCE · SETTLEMENT · NPC ROWS CORRECTED IN PLACE**, each correction dated. The source was a read-only planning pass over the tree at `534a2bc` + `952dc21`. The same amendment covers `§3.9` (the file census and hard serial edges), `§5` items 11–13 with its NOT-JORDAN table, and `_part2`'s lettered entries. It was then corrected by an antagonist pass. **No existing position number changed.** **What a merge carrying it ratifies (ED-1094):** §3.1's phase order, as the ORDER. §5's NOT-JORDAN rows ratify only as *which ladder step answers each question, and which candidate gets attacked*. They are **never ratified as the answer**, which is decided at its position with the code in front of it.
## Owner: infrastructure / cross-cutting (IN lane)
## Supersedes: nothing outright. It becomes the SINGLE OWNER OF THE ORDER across all lanes,
## which `workplans/2026-09-11-arc-sequence-spine.md` (ED-IN-0212) owned for the IN-lane engine
## work alone. Unit CONTENT stays with its owners: `2026-09-09-r-execution-plan.md` (U5–U10),
## `2026-09-09-layer1-conformance-plan.md` (G1–G4), `proposals/2026-09-05-proceedings-subsystem/`
## (the proceedings build order), and — ADDED 2026-09-17 (`ED-IN-0242`, on Jordan's instruction
## to fix the gap) — `workplans/2026-09-13-work-order.md`, which owns the detail of positions
## 13, 13b, 14, 15, 19, 19b and 20 and carries the item -> position mapping. That content lived
## in root `HANDOFF.md`, a continuity index, so it was absent from this list and a trim nearly
## deleted it as duplicated. Detail per position is in `_part2`.

**Why this exists, in Jordan's words:** *"reconcile all plans, open items, findings and other work
flagged over the past week that has not been addressed yet … evaluate what has been superseded
followed by orchestrating the idealized sequence of tasks to be performed. Instructions will be
assigned to each task, and code compliance with Layer 0/1/2 will be enforced."*

**How it was produced.** Three read-only finders (Haiku ×2, Sonnet ×1) inventoried the plan surface,
the register surface and every deferral named in the 31 merge commits of 2026-09-04..11. Two
read-only **Fable 5.1** nodes then adjudicated supersession and sequenced the result — the planner
and audit node, never synthesis (`CLAUDE.md` §10, RULED). This write-up is Opus's, from the same
ruling. Every load-bearing count below was re-run by the author against the tree; **five agent
claims were overturned that way and are marked ✗ where they were wrong.**

**Base commit: `2d5ec4e`.** ⚠ The tree moved under this work: PR #394 merged at 07:44:18Z, mid-pass,
while every agent above was reading `c275a9b`. Their "PR #394 is open" is stale, not wrong.

---

## 0. WHAT THIS DOCUMENT IS, AND THE ONE THING IT IS NOT

It is an **order**, with an instruction per position and the Layer-0/1/2 clause each position must
satisfy. It executes nothing. Under `CLAUDE.md` §0.05 it is **reference**: delete it and the game
behaves identically, which is the correct standing for a plan.

**It is NOT the queue closure.** §2 finds ~97 of the 108 open `needs_jordan` rows closable with
citations. Those closures are **position 1**, not this commit. Landing 97 status flips inside a
planning PR is precisely what `CLAUDE.md` §2 forbids — *"Never bundle a hard design call into a
routine PR"* — and each closure asserts a question is dead, which is a design call. §7 holds it back.

---

## 1. THE SUPERSESSION VERDICT — the plan surface

`workplans/` holds 14 files; `proposals/` holds 376 `.md` in 19 clusters; `architecture/` holds 20,
all RATIFIED. **279 of the 376 proposal files are untouched since 2026-09-01.**

### 1.1 Two rulings do almost all of the superseding

| the ruling | what it kills |
|---|---|
| **ED-IN-0204 Decision 1** — *"only the repository's systems for social contests, personal combat and mass battles to be retained"* | the entire 2026-08-25 → 2026-09-01 design chain (17 proposal clusters), and every FA/SE mechanic row whose `Target:` is `faction_politics_v30.md` or `settlement_layer_v30.md` |
| **ED-SC-0033** (Jordan, 2026-09-06) — *"this subsystem obviously owns all social contests"* + *"orphaned social contest code: retire it"* | `proposals/2026-09-04-social-contest-branches/`, `social_contest_consolidation_integration_v1.md`, and 17 SC ledger rows that are all questions about the retired kernel |

### 1.2 Disposition

| disposition | documents |
|---|---|
| **LIVE** | the spine (ORDER, positions 2–15) · r-execution-plan +`_part2` (CONTENT of U5–U10 only) · layer1-conformance-plan +`_part2` (Arc 2 content; Arc 1 SPENT) · unblocking-strategy (analysis; M1–M6 unexecuted) · `proposals/2026-09-05-proceedings-subsystem/` · `proposals/2026-09-10-settlements-factions-populations/` · the MB/PC proposals (dormant, retained lanes) |
| **SPENT** | both shape-decomposition plans · season-loop-execution-plan (record only — `requirements.yaml:367` and `verb_table.yaml:578` cite its `:647` closure) · post-adoption §4 · `_session_provenance/` (73 files) · the 08-18..08-24 legacy plans |
| **SUPERSEDED BY `architecture/`** | greenfield v1+v2 · valoria-from-scratch · ideal · ideal-v2 · unified-code-shape · shape-tracer · holonic-architecture · throughlines · integration · authoritative-architecture · arc-reachability · play-space-coverage · pr350-archive-recovery · governance-corpus-rebuild. ⚠ **MOST name their own successor, not all — the antagonist pass sampled three and broke the claim on all three.** `2026-08-31-throughlines.md:3` names no successor at all; `governance-corpus-rebuild/README.md` has no `## Status:` line to name one in; and `2026-09-01-holonic-architecture/README.md` names its successor in a callout rather than a status line — **and that callout says the opposite**: *"Read this document first — it is still where the architecture is argued"*, with *"Parts I–VI here are RIGHT and the successor inherits them whole."* That one is superseded **as a build target only**; its reading instruction stands. §7 item 2's hold-back rests on self-declaration, so it does not cover these three |
| **DEAD** | `workplans/README.md` — its enforcing tool `ci_workplan_pointer_check.py` was retired in culling wave 2 and zero `POINTER_*.md` exist |
| **SPENT + DEAD, and it says so itself** | `return_to_game_queue.yaml` — its own header reads *"⛔ SUPERSEDED 2026-08-19. DO NOT RESUME THIS QUEUE."* ⚠ **But its replacement pointer is itself stale**: *"WHAT TO READ INSTEAD: the SessionStart banner"* (retired; §0.3 forbids rebuilding one) *"then … CLAUDE.md §0.2. Your work is the current M1 juncture"* (the retired board). Its `jordan_docket` D1/D3/D5/D6/D7 and held H1–H4 are SPENT; **H5 and H6 survive** |
| **SUPERSEDED IN SUBSTANCE, RECORD NOT FLIPPED** | `workplan_v6_progress.yaml` — **6 of its 7 M1 junctures target layers ED-IN-0204 did not retain**; only j4 (PC R3) is in a retained system. Yet `CLAUDE.md:95-96` binds session work to *"an open M1 juncture"*, §9 calls `m1_acceptance.py --summary` *"the only reading §0.2 accepts"*, and that tool reads this board. **`valoria_master_workplan_v6.md`** — superseded by `architecture/PLAN.md` + `requirements.yaml` |
| **UNRESOLVED** | `2026-08-15-character-and-faction-stats-and-progression.md` — the attribute roster has had no owner since PR #370 closed unmerged on 2026-09-06 with **no superseding row and its content nowhere in the tree** |

### 1.3 Ratification debt, measured

**200 files repo-wide carry a `## Status: PROPOSED`-family line; 162 of them in `workplans/` +
`proposals/` + `architecture/`.** ✗ Three earlier counts in this session's own chain (129, 133, 168)
were all wrong: the dominant recent spelling is **bolded** — `## Status: **PROPOSED … HELD BACK IN
FULL**` — and a `^##+ *Status: *(PROPOSED|…)` regex misses every one of them. Use
`^##+ *Status: *(\*\*)?(PROPOSED|PROPOSAL|provisional)`.

Four merges in the last week landed content **HELD BACK FROM RATIFICATION-ON-MERGE IN FULL** (#365,
#373, #388, #389). ED-1094 makes merge *equal* ratification by default, and §2 requires the exception
be loud **and** rare. Four in seven days is the exception becoming the rule.

---

## 2. THE QUEUE — 108 open, ~97 closable, ~11 real

Measured across 14 `registers/editorial_ledger*.jsonl`: **1,269 rows · 158 `needs_jordan: true` ·
108 of those `status: open`, spread over exactly 8 files** — which is why position 1's instruction
says eight. `ED-IN-0208` pinned 151/105 on 2026-09-10, so **the queue grew by 7
flagged and 3 open in the week that measured it, and nothing was closed.**

### 2.1 The closures, by test (`CLAUDE.md` §0's ladder)

| test | count | ids | the citation that closes them |
|---|---|---|---|
| **1 superseded** | 23 | `ED-FA-0018/0027-0034`, `ED-SE-0031-0044` | ED-IN-0204 Decision 1 — every row's `Target:` is a layer no longer retained |
| **1** | 6 | `ED-FA-0010/0013c/0014/0015/0016/0035` | same |
| **1** | 9 | `ED-SE-0002/0013/0014/0015/0017/0045/0046/0047/0048` | same; `engine/season` reads no geography file at all |
| **1** | 3 | `ED-IN-0030/0049/0050` | the scale bridge is Layer 1 now — `04 §B.7:330`. ⚠ **`ED-IN-0048` was swept into this batch and does not belong**: its subject is a `canonical_sources.yaml` registration gap for `conviction_track` / "Piety Track", not scale transitions. It shares a filing date with its neighbours and nothing else. It closes under **ED-SC-0033** with the rest of the SC cluster, and the antagonist pass caught it using position 1's own falsifier |
| **1** | 8 | `ED-IN-0062/0070/0066/0073/0148/0151` + 2 REMEDIATION | dockets over the evacuated `designs/audit/` tree and the transitional 27-module driver |
| **1** | 5 | `ED-1051`, `ED-1043`, `ED-MB-0065`, `ED-IN-0123`, `ED-IN-0124` | port target is `port/` from the season loop (`04:137`); the 08-24 port settled which MB tree is canon **by execution** |
| **1 via ED-SC-0033** | 17 | `ED-SC-0003/0004/0005/0015/0016/0017/0019/0020/0021/0023/0024/0025/0026/0027/0028/0029/0030` + docket D5 | every one is a question about the retired kernel |
| **2 irrelevant** | 10 | `ED-IN-0069/0085/0086/0092/0103/0156/0158/0042/0195`, `ED-MB-0009` | subjects retired — `dashboard_data.py`, `handoff_atomize.py`, `.claude/wf_*.js`, the thirteen `CLAUDE.md` figures |
| **3 doc-answered** | 3 | **`ED-IN-0113 §A` / docket D1**, `ED-IN-0159`, `ED-PC-0056` | see 2.2 |
| **4 precedent** | 1 | `ED-634` | the names are in live use across `npc_registry.yaml`, `cases/NPC4.yaml`, `faction_politics_v30.md` |
| **5 architecture** | 3 | `ED-885`, `ED-MB-0008`, `ED-SC-0015` | one citation edit; §0.05 (*"the code is the formula"*); the pinned default |
| **reclassify** | 10 | `ED-507/508/595-599/601/602/610` | authorial content backlog, not decisions |

### 2.2 The one worth reading twice

**`ED-IN-0113 §A`** was filed as *"the one artifact only Jordan can author, and the reason the 94-item
`needs_jordan` queue cannot drain."* Jordan then authored it — `CLAUDE.md` §0's five tests and §0.05,
*"CODE IS THE MECHANISM. PROSE IS REFERENCE … If canon and code disagree, decide and then CHANGE THE
CODE."* Metaphysical canon is `.md` and is therefore reference; the fork is answered. **Nobody went
back and closed the row.** That is the queue's pathology in one item: it is large because closures
were never written down, not because the questions are hard.

### 2.3 The hypothesis, tested

*Legacy rows are disconnected from the game; rows minted by recent work are load-bearing.* **Holds,
with a refinement.** 105 of 108 open rows predate ED-IN-0204. Cross-referenced against every
mechanism surface, only **`ED-IN-0214`** (`requirements.yaml:410`) and **`ED-IN-0211`**
(`loop/predicates.py`) are cited from a file that runs — both minted 2026-09-10/11 by U3 and the
verb-table build. **The refinement:** the discriminator is *minted by executed code*, not *recent*.
`ED-SE-0051` is September, design-minted, cited by nothing that runs, and behaves like a legacy row.

⚠ This **falsifies `ED-IN-0208`'s headline** (*"not one of the 151 is cited by an instrument"*) — but
it was true when filed on 2026-09-10 and both falsifying citations landed in `c275a9b` the next day.
A measured half-life of one day, and the thing that falsified it was the game work itself.

---

## 3. THE SEQUENCE — THE SINGLE PLAN

**This table is the only ORDER in the repository.** Detail per position is in `_part2` §8 and in the
CONTENT owners named in this file's header. Nothing else in the tree may carry an order.

**Three columns decide how you read a row.** `STATE` is execution-bound per `CLAUDE.md` §0.2 — `DONE`
means the behaviour runs and something ran it, never that a document exists. `GATE` names what the row
waits on: a position, or Jordan, or nothing. **A row whose `GATE` is `—` is buildable today.**

| `STATE` | meaning |
|---|---|
| **DONE** | it runs, and the evidence is named in §3.3 |
| **DONE·INERT** | the code landed and does not yet affect the game. **§0.2 does not count this as done** |
| **OPEN** | buildable; `GATE` says what if anything it waits on |
| **BLOCKED** | a named position must land first |
| **JORDAN** | a decision or authored content is owed, named exactly |

**Numbering.** No existing position number changed. Rows folded in from the governance build order and
the gather take **lettered sub-positions** on the position they belong to, per the `13b`/`19b`
convention (`ED-IN-0242`). §3.4 maps every old build-order item number to its position so no citation
in the tree dangles.

---

### 3.0 · THE PER-STEP CADENCE — RULED by Jordan, 2026-09-18

*"at end of each step i expect a /code-review and /simplify to run followed by fixes then a forward
sweep to see how it impacts stuff"*

**One step = one position (or sub-position) = one commit.** Five phases, in order, every time:

| # | phase | what it is |
|---|---|---|
| 1 | **BUILD** | the position's change, and nothing else. No widening. |
| 2 | **`/code-review`** | the native fresh-context reviewer, which never saw the reasoning. Read the findings, then **apply** them. Verify each before applying — a review finding is a bug report, not a verdict. |
| 3 | **`/simplify`** | reuse · simplification · efficiency · altitude. Quality only; it does not hunt bugs. |
| 4 | **FORWARD SWEEP** | below — the phase with the least established meaning, so it is defined rather than named. |
| 5 | **CLOSE** | `tools/valoria_local.py --staged`, the lane validator, **the full suite ONCE** (`§0.4` — it is a shipping gate, and the unit being shipped is this commit), then the `[scope]` commit citing its `PP`/`ED`. |

⚠ **`§0.4` IS NOT SUSPENDED BY THIS CADENCE.** `/code-review` and `/simplify` are not pytest. The
inner loop stays the one file covering the edit; the full suite runs once, at phase 5. A step that
re-runs the suite after each fix pays 3.5× for the same verdict.

**FORWARD SWEEP — the definition, because it is a coinage and `§4` requires it survive the session
reset.** *What did this change reach that nobody asked it to?* Five checks, each with an artifact:

1. **The instruments.** `python -m engine.season.harness.register --requirements` · `corpus_run` ·
   `python tools/m1_acceptance.py --summary`. **Did any row move, and is every move the intended
   one?** An unintended move is the finding.
2. **The hole register.** Did this close, narrow or widen a row — and does its falsifier now behave
   as the row predicts? A row whose falsifier did NOT flip when the code says it should have is the
   most valuable thing this sweep can catch.
3. **The call sites.** Grep the changed symbol's callers, not its declaration (`§0.1` pt 3 row two:
   *a roster existing is not a roster being used*).
4. **Figures the change just made stale.** Any `measured:` block, `cite:` field, handoff or plan row
   quoting a number this step moved. **This is the defect this repository pays for most** — `§0.1`
   pt 3 row four — and a sweep that skips it hands the next session a confident wrong number.
5. **The goldens.** Did anything output-moving change, and was a re-record INTENDED? `§7`: nothing
   verifies a golden re-pin was deliberate, so say so plainly when one happens.

**The sweep's output is edits plus at most one paragraph in the commit message** (`§0`'s
adversarial-pass bound). It creates no document and no directory. A finding that needs no ruling is
fixed in that commit or dropped.

### 3.1 · ⭐ START HERE — the build order, in four phases (RE-DERIVED 2026-09-25, `ED-IN-0270`)

**What this replaced, and why.** The previous START HERE named `13b` (DONE 2026-09-18), then `2`
(RET-SC), then `3`→`7` as one block. Its first item was spent, its third carried the collision `§3.4`
warns about (below), and none of it reflected what landed after 09-18. It is kept verbatim as `§3.1a`,
because it is the record of what `13b` bought. **What follows was re-derived by a read-only pass over
the tree at `534a2bc` (2026-09-24) plus the G1b partial since committed as `952dc21`, from the `GATE`
column and the file census in `§3.9`.**

⚠ **SCOPE — the governance · settlement · NPC positions only:** `4`–`7a`, `8`–`12d`, `13b`–`13f`,
`15`–`19c`, `21`, `24`–`24f`. Positions `1`, `2`, `13`, `14`, `17`, `20`, `22`, `23` and `25`–`27` were
not re-derived; their `§3.2` rows stand as written, and nothing below re-orders them. Position `18`
appears only as a hard dependency of `18a` and `19`.

**THE STATE THE PHASES START FROM — stated first, because three `§3.2` rows said otherwise until this
pass:**

- **`G1a` (position `3`) is DONE** — `ED-IN-0258`, 2026-09-19: `state/acts.py`, `state/gate.py`,
  `state/log.py`, `state/attribution.py`.
- **`G1b` (position `4`) is PARTIAL.** Every production READER except the content hash is off
  `Event.subject` — `ED-IN-0258` (G1a's `attribution.py` + `epistemic.py`'s three) and `ED-IN-0269`
  (`last_emission_of` and `witness.py`'s shipped `actor` branch; committed `952dc21`, PR #429). What
  remains is apparatus, not design: `_part2` position 4. `H-107` is the register row.
- **`13b` (`H-71`) is DONE IN BOTH HALVES** — the holder's own (`ED-IN-0255`, 09-18) and others'
  (`ED-IN-0267`, 09-24).

**PHASE α — cheap, gate-free, and NOT on the G-block's contended lines. THIS IS WHAT IS NEXT.**

| # | position | why here |
|---|---|---|
| 1 | **`13f`** `establish` gets an effect | gates `13e`. One small effect (accept that G4 rewrites it) AND an evaluable precondition — without one the fold raises on it. Reconciles the `(Office, remit)` matrix key with `Office.remit_acts` first. Decides snapshot-vs-mirror with the effect in front of it — **a §0 test-5 answer, not Jordan's** (`§5`) |
| 2 | **`13e`** one reading of the remit | two one-line edits once `13f` has fixed the semantics. Removes a `CLAUDE.md` §8 violation three independent lanes rediscovered |
| 3 | **`13d-i`** offices as data | rosters + two predicates + four deletions. The cheapest remaining `R-05` move (`§3.8b`), and a precondition of G3's basis walk (`§3.9` edge 3). ~~and of `18a`'s `conferral_path` deletion~~ ⚠ **CORRECTED 2026-09-25:** `conferral_path` is an ancestry walk. It is superseded by `13d-ii`'s purview walk, `descendants(w, seat.rung)` (i.e. by G3), and not by these rosters (`_part2` 18a) |
| 4 | **`24d-i`** the dwelling substrate | **RULED 2026-09-25** (`ED-SE-0055`, `§3.6`). Data + `build_realm` only. It moves every populated-realm hash, so it lands ALONE and before the G-block's controls rather than interleaved with them. ⚠ **It lands at its CONTROL arm:** `wear_per_season` 0 and an empty `band_floors` cell for `dwelling`. With non-zero wear, dwelling crossings would reach every hearth's residents through Q3's `presence` branch, and `11a`'s identity control would stop being an identity. At wear 0 no crossing fires. It is not silent, though: each dwelling still emits one `condition.worn` per season. So it is labelled **DONE·INERT** only if claims and questions measure unmoved (`_part2` 24d-i). The `capacity` Query (`24d-ii`) waits for its first caller in phase γ |

**PHASE β — the write discipline, serial, before ANY further effect body.** Every position in γ and δ
adds effect bodies (`7a`, `15`, `16`, `17a`, `19`, `24e`, `10`), and G4 rewrites whatever exists. So β
goes first, and the effects are written once.

| # | position | why here |
|---|---|---|
| 5 | **`4` G1b — finish** | the probe/harness migration, then the field deletion and a DECLARED hash move. Blocks `11a` (`§3.9` edge 1) |
| 6 | **`5` G2** | **36** gate sites (re-measured, `§3.9`), the `_rehome()` disposition, the two scans. Hash stationary |
| 7 | **`6` G3** | `Act.via`, `NotYours`, the four bases plus the conferral opener. Absorbs `13d-ii` (purview) and build-order item 15 |
| 8 | **`7` G4** | only after its PRE-FLIGHT on `work`'s deferred accumulator (`§3.9` edge 9). Rewrites 12 effects once (the 11, plus `13f`'s) |

**PHASE γ — governance and settlement content, post-G4, in dependency order.**

| # | position | why here |
|---|---|---|
| 9 | **`11a`** REACH | after G1b's deletion (edge 1) |
| 10 | **`11b`** CALENDAR-EMIT | observable on the corpus's planted `d_forced` dates, with no ad-hoc plant |
| 11 | **`15`** Record-kind fold | the largest item; `16`, `15c`, `15b`, `7a`, `19b` and `24e` hang off it |
| 12 | **`16`** ≡ `15a` GIVE | r2 dependency 5 → 6 |
| 13 | **`15c`** content operands | r2 dependency 5, 6 → 7. Also widens the operand vocabulary `13f`, `19` and `19b` need |
| 14 | **`15b`** lossy tell | r2 dependency 5 → 8 |
| 15 | **`7a`** commit effect | its aperture is open only now: BO-10 names build-order items 5 / 7 / 8, which are `15` / `15c` / `15b` |
| 16 | **`17a`** obligees | after `7a`, and after `13e` (same function) |
| 17 | **`18`** PROC-A | SC lane and outside this pass, but a hard dependency: it BUILDS the `judging_set` that `18a` would delete and `19` consumes |
| 18 | **`18a`** field deletions | twelve, not thirteen — `Tenure.payload` is live |
| 19 | **★** re-measure | per holder. The populated-realm instrument it needs does not exist (`§6`) |
| 20 | **`19`** U7-remit | `levy`'s typed cell · `open_case` · `determine` over `judging_set` · `issue` via `15` |
| 21 | **`19b`** U7-disp | after `15`/`15c` AND the `ED-IN-0210` ruling (`§5` item 2) |
| 22 | **`24e`** works & founding ~~, carrying `24d-ii`~~ | ⚠ **CORRECTED 2026-09-25: `found` is not `capacity`'s caller.** `found`/`build` mint the hearth and the dwelling that `capacity` counts, so they are how capacity GROWS, not an act it refuses. RR-2 reasons it this way: *"found is the throttle"* means the lever, not the subject (`_part2` 24e) |
| 23 | **`19c`** MIGRATE, **carrying `24d-ii`** | `capacity`'s only caller in scope — a migrate into a rung at capacity refuses — so the Query lands here. Carries the `travel_leg` fix |
| 24 | **`24f`** territorial subsistence | design before code. It must precede any `body_step` pick, and it touches `matter.py` after G2 has settled it |

**PHASE δ — the behaviour layer.**

| # | position | why here |
|---|---|---|
| 25 | **`10`** U5 stance | after G4. `tell` only (`speak` has no degree to key on); a `names_index` entry for `stance`; no byte-identity control, declared |
| 26 | **`11`** U6 | prior 100 % at `2x3` |
| 27 | **`8`** H-98(b) | the wound-count edge to data; (a) has no subject today |
| 28 | **`9`** PC-SURRENDER | after the build-or-strike decision (`§5` item 12) and a PC id-block release |
| 29 | **`12b` / `12c` / `12d`** | Jordan authors the cells; then ONE R6-atomic landing. ~~The `(Person, conviction)` carrier and the confliction Query can be prepared before the cells~~ ⚠ **CORRECTED 2026-09-25:** that carrier and Query land IN the cells commit and with a reader, never ahead of it. A carrier prepared before its values is `ID-13`'s shape, the one `24d-ii` is held to (`_part2` 12b) |
| 30 | **`12`** remainder | `axis_count` vs the count-scar, and a `pursuits` trigger — architecture and design answers first |
| 31 | **`21`** U10 | after `20`; the R3 baseline named first |

⚠ **`8`/`9` AGAINST THE CELLS COMMIT IS "EITHER ORDER, NEVER INTERLEAVED"** (`§3.9` edge 10). Both
touch the `kill / wound` row and the combat wrapper that `ED-IN-0261`'s verb split re-cuts. The cells
are Jordan's and their arrival is unscheduled, so whichever is ready first lands first. ~~The table
above lists `8`/`9` first only because they are buildable today.~~ ⚠ **CORRECTED 2026-09-25:** the
table lists `8` first because it is buildable today. **`9` is not buildable:** its row is **JORDAN**
(build-or-strike, `§5` item 12) and it needs a PC id-block release first. **THE COST OF THIS ORDER:**
whichever of `8`/`9` lands before the cells, the verb split then re-touches the same row and wrapper
a second time. The read-only planning pass behind this amendment named that rework when it gated `9`
on the split. The cost is accepted because the cells are unscheduled. If they arrive first, `8`/`9`
land after them and the cost is not paid.

⚠ **`§3.4`'s COLLISION, RECURRING IN THIS FILE'S OWN START HERE.** The old item 3 closed: *"This is
what position `15`'s `Act.via` work waits on."* `Act.via` is build-order **ITEM** 15, which is
**position `6`** (`§3.4`: *"15 → `6` — absorbed into G3"*). Position `15`, the Record-kind fold, has
`GATE: 11a` and does not wait on the G-block. Its real Arc-2 exposure is the same as `7a`'s: it adds
effect bodies that G4 rewrites. Phase γ settles it by placing `15` after G4.

---

### 3.1a · THE PREVIOUS START HERE — kept as `13b`'s record (DONE 2026-09-18)

**1. Position `13b` — H-71's remit grant.** Tier 0, `grade: absent`, `owner: unassigned`. Today
`person_side_eligible` (`engine/season/decision/options.py:107`) reaches its `remit` branch, emits a
`TRACE.note` and falls through to `return False`, so **every governance verb is unformable
person-side even where the actor holds the office whose remit names the act.** Its falsifier is
already in the tree and goes RED the day the hole closes:
~~`test_no_person_can_choose_a_governance_verb_and_h71_is_why`~~ → **renamed `test_a_holder_can_now_choose_the_governance_verbs_their_office_grants` when `13b` closed the hole 2026-09-18**. **No ruling needed** — `CAT-6` ruled
arm 2, which decoupled this from the Record-kind fold, so the old dependency on position 15 is spent.

⚠⚠ **IT IS NOT A ~2-LINE READ, AND THE PLAN SAID SO UNTIL THE CODE WAS OPENED (2026-09-18).** The
build order's *"a ~2-line read of `Tenure.payload`"* describes **one half of a two-half arm.** H-71's
own sweep, arm 2, verbatim: *"THE GRANT RIDES ON THE TENURE — **`confer` writes** the office's remit
acts into the `hold` Tenure's `payload`, **and `person_side_eligible` reads** them there."*

**The read alone ships another `DONE·INERT`.** With no writer, the payload is absent on every live
`hold` Tenure, the new branch admits nobody, and the falsifier stays green while the code looks
finished — the exact shape `3b` is in (§3.3). **So `13b` is: the `confer` effect writes the grant,
the eligibility branch reads it, and the falsifier flips. Three things, one commit.**
`write_matrix.yaml:336-342` licenses `Tenure.payload` at `[RES] ACTS`, which is where `confer`'s
effect runs, so the write is licensed where it needs to be.

✅ **BUILT 2026-09-18 (`ED-IN-0255`), AND THE UNLOCK WAS MEASURED RATHER THAN QUOTED.** Both halves
landed: `World._grant_remit` writes the grant at `add_tenure` (the one writer, so every mint path
carries it — the effect alone would have shipped inert), `Tenure.granted_acts` owns the payload
shape, and `person_side_eligible` reads the holder's own state. `choose` still receives no `World`.

**WHAT IT BOUGHT, AND IT IS SMALLER THAN THE ROW PROMISED.** The `unblocks:` nine is correct — nine
rows carry a `remit:` alternative — but exactly **one** entered the corpus executed set: `dispatch`,
in **1 of 89** live worlds, because only **3 of 143** cases seat a granting office (NPC-008,
NPC-033, NPC-038, via `apply_rescale` overlays rather than `build_at`). **No requirement row moved**:
`R-05` is still `not_met` and THE NINE still reads met 1 / not_met 4 / partial 4. `issue` is granted
in all three worlds and does not execute, and **why is not established** — a null, not a diagnosis.

⭐ **THE REAL RESULT IS THE APERTURE, AND IT REFRAMES THE 09-17 SUITES' CENTRAL PREMISE.** Those
documents argue from *"10 of 38 verbs unformable person-side"* as a flat property. Measured now: a
holder seated on `off_duke` has **2 of 38** unformable; a person holding no office still has **10 of
38**. **The aperture was never shut — nobody was seated.** `00_THE_SEAM.md`'s *"the ranking cannot
discriminate verbs when 10 of 38 never form"* is a statement about an unpopulated office table, and
the aperture re-measurement gate below should re-take it per HOLDER, not per engine.

**2. Position `2` — RET-SC.** Ruled 2026-09-06 and unexecuted since. It is subtraction — 47 files,
1.2 MB — and it is the one position whose cost only grows, because 20+ inbound reference sites outside
the tree keep accruing and several are machine-read by blocking gates. Relocate the demote-only rule
first.

**3. Positions `3`→`7` — G1a, G1b, G2, G3, G4.** The write discipline and the Arc-2 gate: the act
store, `Receipt`, one `Token` across ~~33~~ **36** gate sites (re-measured 2026-09-25, `§3.9`),
`NotYours`, `NoOpReceipt`, the effect contract finalised. ⚠ **`4`→`5` is a HARD SERIAL EDGE** (§4) —
G1b deletes the `subject` parameter of `World.write` (~~`world.py:295`~~ now `world.py:467-472`) and G2
replaces that same signature's write class. `isolation: worktree` does not help; it defers the
collision to the merge. ~~**This is what position `15`'s `Act.via` work waits on, and it is the largest
single blocker in the plan.**~~ ⚠ **CORRECTED 2026-09-25: this sentence confused build-order ITEM 15
with position 15** — see the end of `§3.1`. G1a has since landed (`ED-IN-0258`) and G1b is partial.

---

### 3.2 · THE ORDER

| # | handle | lane | what runs | STATE | GATE |
|---|---|---|---|---|---|
| 1 | **CLOSE-PASS** | IN | flip §2.1's rows with their citations; the queue reads ≤ 12 | **OPEN** · partial | — ⚠ ship the fold-to-latest script as its instrument (§8.3) |
| 2 | **RET-SC** | IN/SC | execute the ruled `systems/social_contest/` retirement; relocate the demote-only rule first | **OPEN** | — |
| 3 | **G1a** | IN | act store · `Receipt` · `state/gate` · `log.append` assertion · the ruled `Record.matured` write | **DONE** | — ✅ **`ED-IN-0258`, 2026-09-19** — `state/acts.py`, `state/gate.py`, `state/log.py`, `state/attribution.py`; the execution artifact is `engine/season/tests/test_g1a_act_store_and_receipts.py`, inside the `engine/season/tests` run `952dc21` records (267 passed). ⚠ **This row read OPEN until 2026-09-25** |
| 4 | **G1b** | IN | delete `Event.subject`; read the actor through `causes[] → state/acts` | **OPEN** · partial | 3 ✅ — **every production READER except the content hash is off the field**: `ED-IN-0258` (`attribution.py`, `epistemic.py`'s three) and `ED-IN-0269` (`world.py::last_emission_of`, `witness.py`'s shipped `actor` branch; committed `952dc21`, PR #429). What remains is a probe/harness migration — the only `[ROOT]`-and-no-changes emitters are apparatus — then the deletion and a DECLARED hash move. No design decision. `H-107`; detail `_part2` position 4 |
| 5 | **G2** | IN | one `Token`, minted in `loop/driver` only; ~~33~~ **36** gate sites (re-measured 2026-09-25, `§3.9`); the `_rehome()` route the scan cannot see | **OPEN** | **4 — hard serial** |
| 6 | **G3** | IN | `NotYours` at the gate · `Act.via` · purview through `via.scope`. **Absorbs build-order item 15 (`Act.via` + F3)** and **`13d-ii`** (purview) | **OPEN** | 5 · ⚠ after `13d-i`, which rewrites the same two predicates (`§3.9` edge 3) |
| 7 | **G4** | IN | `NoOpReceipt`; the effect contract finalised; 11 effects rewritten once | **OPEN** | 6 ⚠ **A PRE-FLIGHT NO CONTENT OWNER NAMES (found 2026-09-25):** `work`'s delta is deferred to an accumulator (`loop/resolve.py:641-653`) and applied in a second write at `:653`, so a gate judging before/after at the effect's own write sees NO change for `work`, by construction. Decide where `NoOpReceipt` is judged for accumulated writes BEFORE `_eff_work` is rewritten, or `work` is refused forever. Architecture's answer, not Jordan's (`§5`). Every effect landed before G4 adds one to the rewrite |
| **7a** | **COMMIT-EFFECT** | IN | `@effect_for("commit")` — mint the Tenure the `commit` row already declares. ~12 lines. `commit` is Q4 `need`'s producer and all 81 `need` questions on the populated world are hand-minted today | **OPEN** | ~~—~~ **`15`, `15c`, `15b`** (the aperture, below; CORRECTED 2026-09-25, because `—` means buildable today and this row's own note said otherwise) · ⚠ **placement against G4 is a JUDGMENT, not a ruling:** writable today, but landing a new effect before G4 means G4 rewrites it. Build it before 7 only if you accept that. Trap: an effect body that touches nothing makes the fold emit the refusal — the body must return the object it opened. ⚠ **AND ITS APERTURE IS SHUT UNTIL `15`/`15c`/`15b` LAND** (added 2026-09-25): `01_THE_BUILD_ORDER.md` §7.2 measured `commitment.made 0 / refused 42` because no question source offers a Proposition referent, and BO-10 names build-order items 5 / 7 / 8 as what opens it. Built before them, its first run re-measures 0/42. `§3.1` places it after `15b`; detail `_part2` 7a |
| 8 | **H-98** | IN/PC | the general ladder branch's producer, and the wound-count band edges. ⚠ RESCOPED — see `_part2` | **OPEN** | 7 · ⚠ **(a) HAS NO FURTHER SUBJECT TODAY** (2026-09-25): only 2 of 38 verbs carry `contests:` (`ED-IN-0261` measured it), both already graded, and the one it adds (`accept`) is combat. **(b), the wound-count edge at `seam/ladder.py:133-135`, is the live half.** Never interleaved with the cells commit (`§3.9` edge 10) |
| 9 | **PC-SURRENDER** | PC | promote §11.4 Yield/Disengage into `combat_engine_v1/` | **JORDAN** | 7 · ⚠ **THE PC LANE FRAMES THIS AS A DECISION, AND THIS ROW DID NOT** (2026-09-25). `registers/handoffs/HANDOFF_PC.md`: *"Decide: a resolver in `combat_engine_v1/`, or strike the spec."* This row's *promote* is an ORDER placement — the 2026-09-12 merge ratified §3's order and nothing else (Status line) — so it does not answer that. `§5` item 12. Separately, the PC `ED-` id block is exhausted (`references/id_reservations.yaml:124`), so a release comes before anything is filed |
| 10 | **U5 / R-07** | IN | `stance_delta`; `Person.stance` written; `stance.moved` | **OPEN** | ~~—~~ **7** ⚠ **CORRECTED 2026-09-25 — this read `—` against `_part2`'s own *"not earlier than … contract (G4)"*:** an effect written before G4 is rewritten by it. ⚠ `stance` is one of five `Person` interior rows with **no specified trigger**; W-F is not started. ⚠ **But the field is NOT unwritten:** `harness/populated.py:596` appends `stance` rows at world BUILD, so a falsifier that looks for "any stance row" passes on the populated world with nothing built. Detail `_part2` 10 |
| 11 | **U6** | IN | the first R-01/R-02 measurement | **OPEN** | 10 |
| **11a** | **REACH** | IN | `reach` · `place_of` · two question sources deleted · `w.crossings` deleted · `occasioned_by` → one route | **OPEN** | S4 · **4 — after G1b's deletion** (`§3.9` edge 1): G1b rewrote where `epistemic._event_place` gets its id, and `11a` moves that function to `world_q.place_of`. Detail `_part2` 11a |
| **11b** | **CALENDAR-EMIT** | IN | CALENDAR `emits="date.fired"`, `subject=venue` | **OPEN** | 11a ⚠ **unobservable on the populated world** — `w.dates` is empty after a season because `convene` never forms. ~~**Plant a date or it proves nothing**~~ ⚠ **CORRECTED 2026-09-25: the corpus already plants one.** `corpus_run.build_at` adds `d_forced` (`due_at: 1`) to every case whose `ENDINGS_CLASSIFIED` ending is `forced_by_threshold` (`harness/corpus_run.py:320-325`), so LB-2c runs there with no ad-hoc plant. Detail `_part2` 11b |
| 12 | **H-62-rest** | IN | the remaining `Person` interior writers: `axis_count`, ~~`convictions`~~ `pursuits` (renamed `ED-IN-0268`), and the scar REBUILD ~~(`scar` is DONE — see §3.3)~~ | **BLOCKED** | ~~—~~ **`12b`/`12c` (the scar rebuild is R6-atomic with the cells), 7** · ⚠ **STALE TWICE UNTIL 2026-09-25:** `scar` ships at its control arm (`scar_step=0`, `H-128`, `data/fixtures.py:533`) AND `ED-IN-0261` rules its shape wrong — a COUNT per element, thresholds 1/2/3 on both tracks, written at RESOLVE over `observers_for`, not a float per axis. `(Person, axis_count)` has a matrix row and no field. Detail `_part2` 12 |
| **12b** | **6a — AFFILIATIONS** | IN | the affiliation roster + the incompatibility relation, as a table. `conviction` is a VECTOR; confliction is DERIVED, never stored | **JORDAN** | **R3 — the cells.** Then its VALUES derive through one owner edit. ~~no `engine/season/*.py` change~~ ⚠ **CORRECTED 2026-09-25, because this row contradicted itself:** `Person` carries no `conviction` field and no roster exists. So the `(Person, conviction)` carrier, its matrix row and a derived confliction Query are `.py` work. They land IN the cells commit with a reader, ~~prepared BEFORE the cells~~ never ahead of it (`ID-13`; `_part2` 12b) |
| **12c** | **6c — THE ~~THIRTEEN~~ FIFTEEN** | IN | ~~re-author the thirteen and their projection onto `memory · substantive · equity · selfish`~~ ⚠ **RE-BASED BY `ED-IN-0261` (2026-09-20): FIFTEEN pursuits over SEVEN bipolar axes** — 105 projection cells, plus the alignment re-cell over the verbs, authored on `proposals/2026-09-20-pursuit-basis-worksheet.yaml` | **JORDAN** | **R3 — the cells.** Atomic with 12b/12d: `_load_projection`/`_load_alignment` raise at module scope, so both tables must exist before first import. ⚠ **And with `ED-IN-0261`'s verb split** (`kill` + `wound`, `fight`, `challenge` → `accept`), which authors ALIGNMENT once rather than twice |
| **12d** | **6b — THE RENAME** | IN | rename the moral-value basis, which `STR-6` forces by reserving `conviction` | **OPEN** · partial | ⚠ **PARTIAL 2026-09-24 (`ED-IN-0268`): the season-side identifier rename landed BY HAND** — `Person.pursuits`, `pursuit_axes`, `data/pursuits.py`; `Person.marks` deleted. **The substrate owner is untouched** — `references/descriptor_registry.yaml:236` `conviction_roster` is still `count: 13`, and `rosters.yaml`'s `pursuits` still reads `from_descriptor:` it — and that half IS the cells' content, so it rides `12b`/`12c`'s one R6-atomic commit. The tool question is answered for the season side, by doing: ~~**restore `tools/valoria_rename.py` from `FORK:1e4c6f4`, or accept a hand sweep of 29 Python files / 308 occurrences / 51 YAML-JSON / 12 live `.md`.**~~ See §3.5 — the stated "it derives" mechanism does not exist |
| 13 | **W28-cast** | IN | author the `cast:` blocks and their reader, same commit | **OPEN** | — ⚠ use the harness loader's count, never a grep (§6's GAP) |
| **13b** | **H-71** | IN | ✅ the grant rides on the Tenure: `World._grant_remit` at `add_tenure` writes it, `Tenure.granted_acts` owns the shape, `person_side_eligible` reads it. Register re-graded `absent` -> `measured`; Artifact 0's tier-0 `absent` list 10 -> 9 | **DONE** | — bought **1 verb in 1 of 89 worlds** (`dispatch`), moved **no requirement row**, and re-measured the aperture to **2 of 38 for a holder / 10 of 38 for a non-holder**. Cost: a seated holder's 8 new verbs displace subsistence work (`work` 51->41, `release` 57->36) — see `24f`. ✅ **AND ITS OTHERS' HALF, 2026-09-24 (`ED-IN-0267`)** — `epistemic.claim_subjects` now expands a `hold`-Tenure receipt into (holder, office), so a witness learns who was seated on what. **Both halves DONE**; the closure is on `H-71`'s own row (`hole_register.yaml`, appended to `source:`) |
| **13e** | **ONE READING OF THE REMIT** | IN | route `_eligible` (`loop/resolve.py:56`) and `_ch_post_remit` (~~`epistemic.py:360`~~ `epistemic.py:413`, the read at `:446`) onto `t.granted_acts` instead of `w.offices[...].remit_acts`. Both already hold the Tenure, so it is a one-line edit at each site and needs no `World` in `choose` | **DONE** | ✅ **`ED-IN-0272`, 2026-09-26** — `loop/resolve.py`, `epistemic.py` (`_ch_post_remit`'s docstring corrected in place, historical W6 finding kept); `decision/options.py`'s reading was already correct and untouched. A pre-existing test (`test_the_revocation_branch_executes_in_the_fold_and_not_only_as_a_predicate`) hand-mutated an office's remit AFTER seating the actor — exactly the read/write asymmetry this position closes — and was found red by an antagonist pass, then fixed to seat with the remit already granted; the two stale docstrings this position's own fix left in the present tense (`state/world.py`, `test_h71_the_grant_is_a_snapshot_not_a_mirror`) are corrected too. Detail `_part2` 13e. ~~—~~ ~~**`13f`** (`§3.9` edge 2; CORRECTED 2026-09-25, because `—` means buildable today)~~ · ⚠ **the top finding of `13b`'s review, and THREE structurally independent read-only lanes have now rediscovered it separately** (§10's ranking signal; the third on 2026-09-19, which also found that `epistemic.py:350`'s *"the correct lookup ALREADY LIVES ONCE"* had been made false by `13b` and left standing — now corrected in place, and that paragraph now reads at `epistemic.py:420-436`). The predicate *does this holder have this remit* now has THREE readings over TWO stores, and ~~`epistemic.py:350-352`~~ the same paragraph already records the tree paying for this exact mistake once: *"Re-deriving it here was `CLAUDE.md` §8 broken one function apart, which is how it came out wrong."* That sentence is now false in the tree. ⚠ **Do `13f` first** — this makes the resolver snapshot-dependent, which is the semantics `13f` gates. ⚠ **A FOURTH reader is planned** (`budget()` counting `t.granted_acts`, `HANDOFF_IN.md`), so the falsifier is an AST scan, not two diffs. Detail `_part2` 13e |
| **13f** | **`establish` HAS NO EFFECT** | IN | `verb_table.yaml:229` declares `writes: ["Office.exists", "Office.remit", "Office.establishment"]` and **no effect is registered in `loop/effects.py`**. Build it, or strike the `writes:` cell | **OPEN** | — ⚠ **it gates a semantics that is currently undecided and was nearly decided by accident.** `establish` is the only act that would change an office's remit, so whether a remit change reaches SITTING holders (snapshot) or only future ones (mirror) arrives with this effect. `13b`'s first writing answered it from a test docstring; that was retracted. **Rule it here, with the effect in front of you.** `establish` is itself `remit:confer`-eligible, so it is one of the nine `H-71` unblocked. ✅ **DONE — `ED-IN-0271`, 2026-09-25** — `loop/effects.py`, `loop/predicates.py`, `state/world.py` (`_grant_remit`'s `force` parameter), `verb_table.yaml`, `write_matrix.yaml`; 23 tests in `test_governance_build.py`. Verified by an antagonist pass that caught the builder's own test-count claim was stale (the honest re-run is 290 passed across `engine/season/tests`, not 209-with-fixes) and closed two real coverage gaps. Three known limitations recorded, not fixed: an office with `rung=None` can't be re-remitted (correctly refused); the remit-change arm can't fire on any world built today; no authority clause yet exists on who may found or re-remit what. Detail `_part2` 13f. ⚠ **FOUND 2026-09-25: THE ROW/FIELD KEY IS BROKEN BEFORE ANY EFFECT RUNS** — `write_matrix.yaml`'s `(Office, remit)` has no carrier field (`matrix_rows_without_a_field()` lists it; the field is `Office.remit_acts`). Snapshot-vs-mirror has a candidate answer that is architecture's, not Jordan's (`§5`). ⚠ **AN EFFECT ALONE DOES NOT MAKE IT RUN:** `establish`'s `requires:` is prose with no typed cell and no predicate, so a hand-built `establish` raises `Unspecified` in the fold (`loop/resolve.py:164-176`) and `resolvable_verbs()` excludes it on that gate too (`loop/driver.py:96-98`). `13f` owes an evaluable precondition as well. With one, a planted act with a full payload executes. A computed one forms with no operands and must REFUSE until `15c` widens the operand vocabulary. It refuses through the fold's refusal path, never by letting `Office.__post_init__` RAISE inside RESOLVE, and it never half-constructs an office. ⚠ **`§5`'s candidate also needs `establish`'s `writes:` to declare `Tenure.payload`**, which it does not today (added 2026-09-25). Detail `_part2` 13f |
| **13d** | **10 — OFFICES** | IN | `offices.yaml` — bases as rostered values · both predicates rewritten · four title helpers + `is_title` + the `titles` roster deleted · ✅ **holders seated** · purview corrected. **SPLIT 2026-09-25 into `13d-i` and `13d-ii` below** | **OPEN** ⭐ · **1 of 5 done** | — its two build-order deps are spent (16 DONE, 4 REVERTED). ⚠⚠ **`13b` MADE THIS THE POSITION THAT UNBLOCKS GOVERNANCE, and it was not that before.** The remaining 8 of 9 remit verbs are now blocked by **office DATA, not by any mechanism**: `harness/populated.py:686` — *"EVERY OTHER OFFICE CARRIES `remit_acts: []`, WHICH IS A DECLARED ABSENCE"*, and only 3 of 143 corpus cases grant anything. Seating holders on offices with populated remits now grants them automatically, because the grant rides on the Tenure. **This is the cheapest remaining move on `R-05`**. ⚠ **PARTIAL 2026-09-19 — see `§3.8b`:** *holders seated* landed as the 13-seat generic spine (`engine/season/governance_spine.yaml`). Purview is still behind `Act.via` (position 6, Arc-2) and the `is_title` deletion is behind `ED-IN-0256` ruling (3) being BUILT. **Do not read this position as closed** |
| **13d-i** | **OFFICES AS DATA** | IN | `engine/season/data/offices.yaml`, read by `build_realm` · conferral (`appointed · elected · annex`, `ED-IN-0256` ruling (2)) and revocation (*"rung above of same faction"*, ruling (3)) as rostered values · `_req_confer` / `_req_revoke` rewritten on them · the four title helpers + `is_title` + the `titles` roster deleted · the title-in-a-body refusal RE-HOMED, not deleted | **OPEN** ⭐ | — **the actionable half, `§3.1` phase α.** A precondition of G3's basis walk (`§3.9` edge 3). ~~and of `18a`'s `conferral_path` deletion~~ ⚠ **CORRECTED 2026-09-25:** `conferral_path` is superseded by `13d-ii`'s purview walk, not by these rosters. ⚠ **r2 `03:1043-1056`'s roster VALUES are SUPERSEDED** (`conferral_bases: [confer, determine, succeed]`, `revocation_bases: [purview, holdings, none]`, which its 29 seats are authored on). Both lists predate `ED-IN-0256` rulings (2) and (3). r2 supplies the STRUCTURE (closed rosters, a basis per seat); the ED supplies the VALUES; mapping r2's seats onto them is the build's work. Closes `H-109`. Detail `_part2` 13d |
| **13d-ii** | **PURVIEW** | IN | purview asked of the seat exercised, per `ED-IN-0256` ruling (4) | **BLOCKED** | 6 — **absorbed into G3**, which rewrites every purview reader exactly once |
| 14 | **U7-own** | IN | the eight `own`-eligibility verbs, in antonym pairs; distinct operands; `Candidate.why` | ~~**OPEN**~~ **BLOCKED** | 12, 13 · ⚠ **TRANSITIVELY ON JORDAN (found 2026-09-25):** `12` now waits on the cells (`12b`/`12c`, `§5` item 11), so this does too. `§4` orders `12 → 14` because 14's contested closers reuse 12's degree-keyed rows. The re-gating of `12` did not carry forward to this row |
| 15 | **Record-kind fold** | IN | Petition/Dispensation become kinds of `Record`; `record_kinds` + its refusal; `issue`/`petition` bodies; 2 matrix rows and 2 `World` dicts deleted; the deposit rule; then `petition` + `carry`. **≡ build-order item 5 — SAME WORK, TWO NUMBERS (§3.5)** | **OPEN** | 11a. **The largest single item in the plan; everything in `15a`–`15c` hangs off it.** ⚠ **Its Arc-2 exposure is `7a`'s, not the G-block's** (`§3.1`): it adds effect bodies (`issue`, `petition`) that G4 rewrites, so `§3.1` lands it after G4. Detail `_part2` 15 |
| **15a** | **6 — GIVE** | IN | ~~`give` + body + `_req_give` + release-before-mint~~ **≡ position `16` — SAME WORK, TWO NUMBERS.** r2 `05_LEDGER_AND_BUILD.md`'s row 6 (`give` + body + `_req_give` + release-before-mint) carries *ratified position: **16***. **Merged 2026-09-25; the detail lives at `16`** — `§3.4`'s collision again | **BLOCKED** | 15 |
| **15b** | **8 — LOSSY TELL** | IN | `tell` at `Partial` deposits a lossy copy — and the teller's identity | **BLOCKED** | 15. A WITNESS-side deposit change, not a `writes:` change. Detail `_part2` 15b |
| **15c** | **7 — CONTENT OPERANDS** | IN | content-claim operands; Q2's third clause; the invariant statement | **BLOCKED** | 15, ~~15a~~ 16 (≡ `15a`). ⚠ **It is also what widens `requires_operands`**, which `13f`, `19`, `19b` and `24e`'s `found` need before a computed act can form. Detail `_part2` 15c |
| 16 | **H-84** | IN | one verb that moves a Record to another person. **≡ `15a` / build-order item 6 (merged 2026-09-25)** | **OPEN** | 15 |
| 17 | **U8 / R-06b** | IN | `ambitions(p)`, `build_at` from the cast | **OPEN** | 13 |
| **17a** | **9 — OBLIGEES** | IN | obligees co-located mint `inferred` · `oblige` body · `establishment_of` rewritten with a caller · `Office.establishment` deleted | **OPEN** | 7a, **13e** · `13e` first — both edit `_ch_post_remit`, which `17a` replaces (`§3.9` edge 4). Through `7a` it also waits on `15`/`15c`. Detail `_part2` 17a |
| 18 | **PROC-A** | SC | re-host the stress suite (its tracer is gone); `judging_set`; `arrangements.yaml` | **OPEN** | — |
| **18a** | **14 — FIELD DELETIONS** | IN | the ~~13~~ **twelve** field deletions — **NOT `Tenure.payload`, which `13b` made LIVE** (it carries the remit grant; `RULINGS.yaml` CAT-6 priced this) — + `conferral_path` (~~0 callers~~ **one caller, a test** — re-pointed, not deleted with it; `_part2` 18a) + the `judging_set` STUB | **OPEN** | 17a, ~~13d~~ ~~13d-i~~ **`13d-i` + `13d-ii`**, since r2 item 14 depends on item 10 whole (`05:1254`). The `conferral_path` half is `13d-ii`'s purview walk, i.e. G3 (CORRECTED 2026-09-25) · ⚠ **`judging_set` COLLIDES WITH POSITION `18`**, which BUILDS `world_q.judging_set(w, venue, matter)` for `19`'s `determine`. `18` lands first — the table's own order — so `18a` deletes only what `18` replaced (`§3.9` edge 5). Detail `_part2` 18a |
| **★ GATE** | **APERTURE RE-MEASUREMENT** | IN | **Fires ONCE, after `18a`. A measurement, not a build item, and NOTHING BELOW MAY BE SCORED BEFORE IT PASSES.** Re-take: verbs resolvable (was 18/38) · verbs unformable person-side (was 10/38, every governance verb) · claims by source (was `{firsthand: 2174, told_by: 1}`, `inferred: 0`) · questions by source. ⚠⚠ **RE-TAKE IT PER HOLDER, NOT PER ENGINE (changed by `13b`, 2026-09-18).** *"10 of 38 unformable"* was never a property of the engine — measured after `13b`: **2 of 38 for a person seated on `off_duke`, 10 of 38 for a person holding nothing.** A single number for this row is now a category error, and the suites that argue from the flat figure are listed in `§3.8`. **Then re-take `CAT-6`'s evidence block and `STR-4`'s conclusion against the new numbers — both are inferences from a shut aperture, and re-citing them is not re-taking them.** ⚠ **TWO GAPS, stated rather than filled (`§6`, 2026-09-25):** nothing runs the populated realm for formability (`test_the_generic_remit_seats_every_office_and_unblocks_the_nine` says so in its docstring), so until an instrument exists a per-holder re-take re-takes on the corpus only; and the claims and questions figures above are **2026-09-17 values**. `resolvable_verbs()` reads 19 at `952dc21`. Detail `_part2` ★ | **OPEN** | 18a |
| 19 | **U7-remit** | IN | `levy`, `establish`, `open_case`, `determine`, `issue` | **OPEN** · re-scoped | ⚠ **`13b` LANDED, so this is no longer blocked on it — and `13b` changed what it IS.** All five are now FORMABLE by a holder whose office grants them; none executes. `establish` has **no effect at all** (`13f`), and `issue` is granted in three corpus worlds and does not execute ~~for a reason **not yet established**~~ — ✅ **ESTABLISHED 2026-09-25:** `resolvable_verbs()` excludes `issue` on TWO of its gates — no effect behind a non-empty `writes:` (`loop/driver.py:99`), AND a precondition the fold cannot evaluate: `requires:` is prose, with no typed cell and no predicate (`:96-98`; a hand-built `issue` raises `Unspecified` at `loop/resolve.py:164-176`). Every corpus chooser is built on that set (`harness/corpus_run.py:420`). **Formable, and never offered.** `15` supplies the effect; the precondition is this position's. **The same two gates hold `establish`, `levy`, `open_case` and `determine`.** So this position is no longer "make them eligible" — it is "give them predicates, effects and operands". Still gated on ★ — and on 6 (`via`), `15`/`15c` (`issue`'s Record and every operand), and `18` (`determine`'s `judging_set`, SC lane) |
| 19b | **U7-disp** | IN | **BUILD the three response verbs** — `comply`, `evade \| defy`, and the third one pending its rename. ⚠ **THE FOLD IS REVERSED (`ED-IN-0210`, 2026-09-18).** Jordan, shown the consequence: *"i did not realize that meant deleting those verbs. i think that's wrong."* Nothing was ever deleted — the FOLD was ruled 09-17 and never executed — so this reverts to its original sense | **OPEN** | ✅ **NAMED `construe` (Jordan, 2026-09-18)** — he rejected `refract` (*"the wrong word to use for whatever it is tho"*) and picked from the ranked candidates. Renamed across `verb_table.yaml` (verb + `construal.impossible`, following `comply` -> `compliance.impossible`), `rosters.yaml`'s weight key, `epistemic.py` and the `A33` probe. **`refraction` SURVIVES as the phenomenon** — his own 2026-09-02 ruling holds the distortion is receiver-side and in *"the PREMISES AND RATIONALE"*, and its reasoning (*"the meaning of those actions are subject to interpretation - signified vs signifier"*) is construal itself. The premise is refracted BY the act of construing: cause and effect, not one thing twice. `terms.distorted` unchanged. `ED-IN-0210`'s open fork (*are `dispatch` and `comply` two sides of one thing?*) is UNCHANGED and is not closed by the reversal. ⚠ **AND IT WAITS ON `15` (+`15c`), WHICH THIS ROW DID NOT SAY** (2026-09-25): the operand is a dispensation, which is a `Record` kind only after the fold, and `requires_operands` has no name for one (`comply`'s own note in `verb_table.yaml`). Detail `_part2` 19b |
| **19c** | **MIGRATE** | IN/SE | a migration verb. ~~**Nobody in Valoria can relocate** — `move` is TRAVEL (a `travel_leg` Tenure alter) and `residence` is a contested claim predicate **with no writer**~~ ⚠ **PREMISE CORRECTED 2026-09-25:** `move` DOES re-home the actor's `contain` edge (`loop/effects.py:260-264`), so `home_of` changes on a move — the tree has ONE edge for where you are and where you live. What is missing is the distinction between them, and `residence` (a `person_predicates` member) still has **no producer** | **OPEN** | ~~—~~ **24d-i** (and `capacity`, `24d-ii`, as its throttle, which lands in this position's commit as its only in-scope caller) · the presence/residence split, which is architecture's once `24d` exists (`§5`). Opened by the 09-17 rulings. Ride-along: `travel_leg` accumulates forever. Detail `_part2` 19c |
| 20 | **U9 / R-04** | IN | faction-scale queries; 44 re-scales; the 10 world cases. **54 of 143 cases are unrepresentable today — 44 at faction scale, 10 at world** | **BLOCKED** | ★ |
| 21 | **U10** | IN | the second measurement; `measured:` from instrument output only | **BLOCKED** | 20 ⚠ `requirements.yaml` carries **four mutually inconsistent R3 figures** (~~`:142`, `:265`, `:333`, `:524`~~ **re-located 2026-09-25:** `:142` — 22/30 NPC, 34/59 ARC · `:172-177` — the same row's 30/30 and 54/59 before `ED-FI-0009` · `:263-267` — 50 → 84 of 143 · `:364-365` — 55 → 50 of 143, and U4's 56·55·59·59·48 · `:555` — unmoved at 84 of 143) with no stated baseline and **two denominators** (89 live worlds, 143 cases). Any position measuring propagation trips on this — fix it here: name the owner (`corpus_run`'s printed R3 line, the row's `measure:` at `:194`) and the denominator, then re-take |
| 22 | **PROC-B** | SC | the proceedings provider; the composed obstacle with a ceiling; THE BAR | **BLOCKED** | 18, ★ |
| 23 | **PART-E-0/2** | IN | typed ids with an owned `H`; the ONE loader's remaining invariants | **OPEN** | 22 |
| 24 | **SE-BUILD** | SE | settlements P1–P4. ⚠ **MIS-SIZED AS WRITTEN: P1 is DONE bar a number, P4 is now `24e`, and P2/P3 grew a ruled dependency.** Re-scope before starting | **OPEN** · partial | ✅ **P1/P3/P4 ACCEPTED FOR BUILD 2026-09-19** (`ED-SE-0054`); P2 is not in the acceptance. ⚠ P1's write site inherits `24f`'s open scale question. See `24d`, `24e` |
| **24d** | **SE-CAPACITY** | SE | `capacity(w, rung)` as a Query over the rung's dwelling Sites **with a FLOOR — never a fixture table** | **OPEN** | ✅ **RULED AND CLOSED 2026-09-19** (`ED-SE-0051`, §3.6); ungated. The blocker is that the mechanism has **zero code**: no `capacity` in `queries/`, and no `dwelling`/`houses`/`shelters` anywhere in `engine/season/`, where ~~`rosters.yaml:847`~~ `rosters.yaml:896` fixes `site_kinds` to three, one of which is not a site. ✅ **SUBSTRATE RULED 2026-09-25 (Jordan, `ED-SE-0055`): a `dwelling` SITE KIND** — `build_realm` mints one dwelling Site per hearth rung, and `capacity(w, rung)` queries descendant Sites of that kind. The literal reading of the ruling, taken at its stated cost: a new data family, and 211 new Sites in every populated world's content hash (`§3.6`). **Split into `24d-i` / `24d-ii` below** |
| **24d-i** | **DWELLING SUBSTRATE** | SE | `dwelling` added to `site_kinds`, plus the rows the loader then forces (`wear_per_season`, `band_floors`) · `build_realm` mints one `dwelling` Site per `hearth` rung | **OPEN** | — **`§3.1` phase α.** Data + world-gen; a DECLARED hash move on every populated world, landed alone, **at its control arm** (wear 0, no band floors), so no dwelling crossing fires. It is **DONE·INERT** only if claims and questions measure unmoved, because the dwellings still emit wear Events (added 2026-09-25). Detail `_part2` 24d |
| **24d-ii** | **CAPACITY** | SE | `capacity(w, rung)` over the dwelling Sites at the rung and its descendants, with a FLOOR held as a table keyed on site kind beside `band_floors` | **BLOCKED** | 24d-i · **lands in the same commit as its first caller** — ~~`24e`'s `found` throttle, or `19c`'s if that lands first~~ **`19c`'s `migrate`, its only caller in scope** (CORRECTED 2026-09-25: `found` GROWS capacity and is not refused by it — `24e`). A Query nobody calls is `ID-13`'s *"mechanism that does not exist, wearing a schema's clothes"*. ⚠ **The consumer RR-2 actually reasons about, births, has no builder anywhere in scope.** RR-2's floor is *"applied here to births"*, and nothing grows a population today (`_part2` 24d-ii) |
| **24e** | **12 — WORKS & FOUNDING** | SE/IN | `works` kind · `work` advances `stage` · `restore` body · `found` + body · `(Rung\|Site, exists)` get a producer. **This is `found` (P4), which the `ED-SE-0051` ruling names as THE THROTTLE.** ⚠ **Read that as RR-2 reasons it (2026-09-25):** capacity throttles POPULATION, and `found`/`build` are the LEVER that grows capacity, so `found` is not an act capacity refuses (`_part2` 24e). It answers `ARCH` `F.20` — *"the world only decays — nothing is ever founded or built"*, one of two gaps ~~`04:1082`~~ `04:1084` says *"block the build outright"*. It is also the R-half with no player in it (§0.06) | **BLOCKED** | 15, 15c (`found`'s operands), 24d-i (a `build`able `dwelling` kind). ~~— **and it carries `24d-ii`**: `capacity` is `found`'s throttle, so they land together.~~ CORRECTED 2026-09-25: it does not call `capacity`, so `19c` carries `24d-ii`. `_eff_work` advancing `stage` also inherits G4's accumulator pre-flight. Detail `_part2` 24e. ✅ **P4 ACCEPTED FOR BUILD 2026-09-19** (`ED-SE-0054`) — the acceptance does NOT unblock it; `found` still waits on the Record-kind fold, and `04_EVALUATION.md` grades P4 `paper` / **refuses at load** pending three table corrections |
| **24f** | **SUBSISTENCE IS TERRITORIAL** | SE | ⭐ **RULED 2026-09-18 (`ED-IN-0255`)** — *"subsistence/starvation should largely be an abstract/governance issue, and we can just have NPC synecdoches that just represent the overall population affected... i don't think having lords and guild members etc worry about subsistence is worthwhile"* · *"it's a territorial issue"*. Move the demographic loop off per-person eaters and bodies onto a TERRITORIAL quantity with population synecdoches | **OPEN** | ~~—~~ **5** (G2: it touches `loop/matter.py`'s subsistence pass, whose gate sites G2 rewrites; CORRECTED 2026-09-25, because `—` means buildable today) · ruled, unscheduled by any prior order. ⚠ **It re-opens `ED-IN-0247`**: `body_step` is a per-PERSON body write, and this ruling puts that SCALE in question, not just its magnitude. Answer the scale before picking the number. ⚠ **A CANDIDATE FOR WHO EATS (2026-09-25), from `carriers.py:447`'s one-class cohort** (*"A COHORT IS A PERSON AT weight > 1"*): `weight > 1` eats, `weight == 1` is exempt. That is a §0 test-5 answer, NOT Jordan's (`§5`). ⚠⚠ **AND AS THINGS STAND IT IS DEAD ON ARRIVAL, which the antagonist pass caught:** no built world mints a person heavier than 1. `build_realm`, `build_at` and the spine all construct `Person(pid, …)` at the default `weight=1` (`carriers.py:450`). The only heavier person is `probes.py:744`'s test crowd. So *"weight==1 exempt"* means **zero eaters on every built world**, which switches off `3a`/P1, and `§3.7` says *"nothing here licenses deleting working code"*. **The candidate needs a precondition first: something that mints the synecdoche cohorts, and a statement of what it mints them from** (`_part2` 24f). The NUMBER stays `ED-IN-0247`'s. Detail `_part2` 24f |
| 25 | **MB-GOLDEN** | MB | apply the golden-mode ruling; fix three flags whose defaults contradict their comments | **OPEN** | `ED-MB-0061/0016` — flags cleared. ~~both `superseded`~~ ⚠ **CORRECTED 2026-09-25:** `ED-MB-0061`'s last row is `superseded`, but `ED-MB-0016`'s is `status: open` with `needs_jordan: false` (`registers/editorial_ledger_mb.jsonl`, 2026-09-15). Its flag is cleared; the row is not superseded |
| 26 | **GO-VERSION** | GO | record the ruled version; ED-1050's deferred re-export; then held H6 | **JORDAN** | **the Godot engine version — UNRESOLVED, and `CLAUDE.md` forbids settling it by editing a document** |
| 27 | **WR-SCOPE** | WR | build or retire threadwork | **OPEN** | `ED-WR-0010` **ruled: threadwork IS IN SCOPE.** ⚠ Part 3 of the head and `systems/threadwork/sim/coherence.py` still implement the model `RULINGS.md` replaced |

---

### 3.3 · DONE — five items that landed 2026-09-17/18, with their evidence

**Folded in from the governance build order, which is now a CONTENT owner only.** `§0.2`: a row is
`DONE` because something ran it, not because a document says so. Execution artifact for all five:
`python -m pytest engine/season/tests/test_governance_build.py -q` → **25 passed in 6.78s**.

| build-order item | what landed | where | belongs to |
|---|---|---|---|
| **16** | `add_tenure`'s hold-object guard; the 16 faction rung-holds re-homed to persons. **A precondition, not a tidy-up** — `in_holdings` was false for every person over every rung, so a seat whose `revocation` is `"holdings"` refused every revocation forever *while looking like a working precondition* | `data/rosters.py`, `rosters.yaml`, `state/world.py` | `13d` |
| **3a** | `nearest_store` + the per-eater draw — **and it MEETS its demand**, which is rarer than landing. Season 1: 46 eaters short, 138 units. Season 2: 0 short. `stores.changed` 87 = 37 + 37 + **13 draws**, which is r2 §A.4's predicted counterfactual arriving as an observation | `queries/world_q.py:172`, `loop/matter.py:249` | `24` (P1) |
| **3b** | the body write · one shared `_crossings` owner · `remove_person` | `loop/matter.py:309-313`, `state/world.py:320` | `24` (P1) |
| **6d** | the `beneficiary:` column, all 38 rows, off a `beneficiary_kinds` roster with three loader refusals. 5,345 candidates, **3,796 (71.0%) resolve a personal beneficiary, ZERO declared-but-unresolved** | `verb_table.yaml`, `data/verbs.py`, `decision/choose.py` | `12` |
| **6e** | `(Person, scar[axis])` gets a producer — **the first write to any `Person` interior field in the tree** | `loop/effects.py`, `state/carriers.py` | `12` |

⚠ **~~TWO~~ THREE OF THE FIVE DO NOT AFFECT THE GAME YET, and `§0.2` does not let that pass as done.**
(The third, `6e`, added 2026-09-25 — last bullet.)

- **`3b` is `DONE·INERT`.** `data/fixtures.py:494` ships `body_step=0` as a **declared control**. With
  46 eaters short 138 units: `body.changed` 0, `person.died` 0, `w.crossings` 0, all 46 bodies at
  1000. **`ED-IN-0247` is `needs_jordan: true` for exactly one thing — the number — and it is a PICK, not a
  blank:** `fixtures.py:494` reads `body_step=0,  # H-125, swept 0 (control, SHIPPED) / 10 / 67`. The
  file says why it is Jordan's in its own comment — *"Choosing the number needs a world that stocks a
  larder — which is what makes this a design call rather than a default nobody looked at."* **One value
  off that sweep turns a built mechanism live.** ⚠ **And the other half of P1's crossing ask is missing**: `world_q.py:633-637`
  (CORRECTED 2026-09-20, `ED-IN-0260`; `:602-605` is Q2, and Q3 begins at `:615`)
  derives `at` from `w.sites.get(who)`, which is `None` for a person-keyed crossing, so the `presence`
  branch cannot fire — and `proposals/2026-09-10-settlements-factions-populations/02_PROPOSALS_SUBSTRATE.md:54-60`
  already specifies the repair (`at = parent_of(w, who)` when `who` names a person) — **a body falling is a Question for its owner alone, never for the hearth.**
- **`6d` is `DONE·UNWIRED`**, deliberately. `orient` has no producer, so wiring it into `score` would
  multiply a measured quantity by an unruled magnitude and move every golden for a weight nobody set.
- **`6e` is `DONE·INERT` — AND ITS SHAPE IS NOW RULED WRONG.** `data/fixtures.py:533` ships
  `scar_step=0` (`H-128`, swept 0 / 1 / 10) as the declared control, so the producer at
  `loop/effects.py:340` writes nothing. And `ED-IN-0261` (2026-09-20) rules scars a COUNT per element,
  thresholds 1/2/3 on both tracks, written at RESOLVE over `observers_for` — not the float per axis on
  the wounded party that this builds. It is rebuilt, not tuned: position `12`.

**Also landed and NOT a position:** the counterparty change (`ED-IN-0210` Ruling 1) — every person's
OUGHT now names a PERSON. Control 443 acts / 0 naming another person → shipped 692 acts / 256 naming
another person; distinct executed sets 25 → 43. Recorded in §8.1.

**REVERTED:** build-order item **4** (delete `budget_office_bonus`). Priced as a free cut; running it
showed **it starves the corpus**. A starvation floor is an alarm, not a saving. Do not re-propose it as
cheap.

**HELD:** build-order item **1** is *built and held* — its headline claim was measured false. It rides
at `7a` with that stated.

---

### 3.4 · THE MAPPING — every old build-order item number to its position

**Read this before citing any bare item number.** ⚠ **The two schemes collided, and that is the
strongest single argument for one plan:** build-order *item 16* is not position 16, *item 15* is not
position 15, and *item 5* and *position 15* were **the same work under two numbers**.
⚠ **IT RECURRED TWICE MORE, both found 2026-09-25 (`ED-IN-0270`):** `§3.1`'s old item 3 read build-order item 15
as position 15, and build-order item 6 (`15a`) is position `16` — one piece of work, merged below.

| build-order item | position | note |
|---|---|---|
| 1 | `7a` | built and HELD; headline claim false |
| 2a · 2b | `11a` · `11b` | 2b was **missing from the build order's first draft** and an independent critic found it |
| 3a · 3b | **DONE** (§3.3) | 3b inert |
| 4 | **REVERTED** | starves the corpus |
| 5 | **`15`** | ⚠ **same work as position 15 — merged, not duplicated** |
| 6 · 7 · 8 | `15a` · `15c` · `15b` | all hang off `15`. ⚠ **`15a` ≡ position `16`** — r2 `05_LEDGER_AND_BUILD.md`'s row 6 names *ratified position 16*; merged 2026-09-25, detail at `16` |
| 9 | `17a` | |
| 10 | `13d` | its deps are spent |
| 11 | **PARKED** | `CAT-6` arm 2 retired it as H-71's answer; whether the commission `Record` is wanted for other reasons is undecided |
| 12 | `24e` | the `found` throttle; `ARCH F.20` |
| 13 | **`19b`** | `RR-A` ruled FOLD — now a deletion |
| 14 | `18a` | |
| 15 | **`6`** | ⚠ absorbed into G3, which already names `Act.via` |
| 16 | **DONE** (§3.3) | |
| 6a · 6b · 6c | `12b` · `12d` · `12c` | all three JORDAN-gated on R3 |
| 6d · 6e | **DONE** (§3.3) | 6d unwired |
| 6f | **not scheduled** | the score function; needs 12b–12d's tables to have anything to dot against |
| 6g | ~~**not scheduled**~~ ✅ **DONE 2026-09-24** (`ED-IN-0267`) | ~~H-71's SECOND half — how another person comes to know or contest someone else's seat. **Open by the ruling's own words**, not by omission~~ The *know* half closed at the reader: `epistemic.claim_subjects` expands a `hold`-Tenure receipt into (holder, office). **Contesting a seat** — a verb that acts on the now-legible claim — is separate, unruled, and nobody's position yet (the commit's own words: *"No consumer verb built, and none is this item's"*) |
| the gather's `13c` · `19c` · `24a`–`24d` | `13b` · `19c` · `12b`–`12d`, `24d` | ⚠ the gather placed the conviction items at `24a`–`24c`, under SE-BUILD, which was wrong — they are position 12's siblings. Corrected here |

---

### 3.5 · THE ONE COST THIS AMENDMENT RE-PRICES

⚠ **`01_THE_BUILD_ORDER.md:1028` says of 6b: *"`references/names_index.yaml` is the TERMS owner; the
rename derives."* BOTH HALVES ARE FALSE, MEASURED.**

1. **The executor is retired.** `names_index.yaml:13-14` advertises `tools/valoria_rename.py`;
   `references/restructure_ledger.md:1525` is its `FORK:1e4c6f4` row. The tool that would derive the
   rename was deleted.
2. **`names_index.yaml` does not own the thirteen.** Its `conv.*` block is **seven** entries at
   `:105-111`, all `enforce: warn`. The real chain is `descriptor_registry.yaml:236` (`count: 13`) →
   `rosters.yaml:228` (`from_descriptor:`) → `descriptors.json`, behind the blocking `--check`.
3. **The 107-document arm has fallen to 12.** That figure was measured *before* `ED-IN-0231`
   quarantined `systems/`. Live count is **12**, with 66 quarantined. `01_THE_BUILD_ORDER.md:1028` and
   `RULINGS.yaml:1356-1357` both carry the stale number forward — `§0.1` pt 3 row four, **inflating
   6b nine-fold on its largest arm**.

**Net: `12b` and `12c` are cheap and DO derive** — Jordan's content, then one owner edit, no
`engine/season/*.py` change, because `decision/choose.py:358-360` resolves the tables by name.
**`12d` does not derive.** ⚠ **NARROWED 2026-09-25: "no `.py` change" holds for `12c`'s tables and
NOT for `12b`.** `Person` has no `conviction` field and confliction is a derived Query, so `12b` owes
a carrier and a Query, and they land in the cells commit (`§3.2`'s `12b` row).

---

### 3.6 · ~~`ED-SE-0051` IS RULED, AND FOUR SURFACES DISAGREE~~ — ✅ **CLOSED 2026-09-19**

`proposals/2026-09-17-governance-and-behaviour/RULINGS.yaml:1838-1844` carries `disposition: ruled`,
`ruled.by: "Jordan, 2026-09-17 (in session)"`:

> **MATTER PLUS HEARTH CAPACITY. A `capacity(w, rung)` QUERY over the rung's dwelling Sites, with a
> FLOOR — never a fixture table. `found` (P4, "found and build") is the throttle. SCOPED TO POPULATIONS.**

Its own `citation:` names `registers/editorial_ledger_se.jsonl:51`, so it is unambiguously this
question. Against that, the ledger read `open`/`needs_jordan`, `HANDOFF_SE.md`'s body said *"STAYS
OPEN"* in three places, and the r2 documents called the capacity arm *"recommended, not adopted"*.

✅ **JORDAN CLOSED IT 2026-09-19:** *"commit whatever se-0051 is"*. The ledger now carries a second
row under the id (`status: ruled`, `needs_jordan: false`) and `HANDOFF_SE.md`'s three claims are
corrections rather than assertions. **All four surfaces now agree with the ruling he gave on 09-17.**

⚠ **WHAT WAS ACTUALLY DECIDED IS THE SHAPE, NOT JUST THE ARM.** E-1's own text proposed the capacity
bound as *"a `hearth_capacity` fixture table per `site_kind`, adding no new primitive"*. Jordan took
the arm and **refused that shape**: a `capacity(w, rung)` **Query over dwelling Sites with a floor,
never a fixture**. A fixture would be a second home for a fact the Sites already carry (§0.05 cl.1),
and it would make capacity authored where the ruling makes it derived.

**`24d` is RULED AND UNGATED — and still not buildable, for a different reason.** The blocker was
never the answer; it is that the mechanism has ZERO CODE: no `capacity` in `engine/season/queries/`,
and no `dwelling`/`houses`/`shelters` anywhere in `engine/season/`, where `rosters.yaml`'s
`site_kinds` fixes three kinds one of which is not a site. `24e` (`found`, P4) is what makes the
throttle real and is blocked on position 15.

✅ **THE SUBSTRATE, RULED 2026-09-25 (Jordan, in session; `ED-SE-0055`).** The ruling's *"dwelling Sites"* had no
referent in the tree: `build_realm(0)` builds **74 Sites, all `harbour` or `seam`** — one per
producing kind per settlement (`harness/populated.py:370-374`, keyed on `SITE_YIELD`) — and the **211
buildings are `hearth`-kind RUNGS** (`:361`), not Sites. Two readings were put: **(a)** add a
`dwelling` site kind and have `build_realm` mint one per hearth rung, so `capacity(w, rung)` queries
the rung's descendant Sites of that kind; **(b)** read *"dwelling Sites"* as the hearth rungs already
built. (a) obeys the ruling's letter and costs a new data family and 211 Sites in every populated
hash; (b) obeys the tree and re-reads Jordan's word. **Jordan chose (a).** `24d` therefore splits:
**`24d-i`**, the substrate, buildable now (`§3.1` phase α); and **`24d-ii`**, the `capacity` Query,
which lands with its first caller (~~`24e`'s `found`, or `19c`~~ `19c`'s `migrate` — corrected
2026-09-25, `§3.2`'s `24d-ii` row). ⚠ **The ruling names `build_realm`, and it is not the only
builder of hearths.** `corpus_run.build_at` builds a `person`-scaled case's `hearth` rung
(`harness/corpus_run.py:209-211`) and seats its people in it (`:226-231`).
`harness/governance_spine.build` builds `lr_hearth_a` / `lr_hearth_b` (`governance_spine.py:126`;
`governance_spine.yaml:86-87`), and `probes.tiny_world` builds `Hh` (`harness/probes.py:73`).
Minted by `build_realm` alone, every one of those hearths reads the FLOOR. Whether the others mint
dwellings too is not in the ruling. `24d-i` decides it and says which. That decides whether capacity
can vary on any world `R-05` is scored on, and on the spine, where `19c`'s observable runs.

### 3.8 · FORWARD SWEEP AFTER `13b` — what closing one tier-0 hole did to the later positions

**Run 2026-09-18 under `§3.0` phase 4.** Each row is a change made above, not a note left here.

| position | what `13b` changed about it |
|---|---|
| **★ APERTURE GATE** | its premise. *"10 of 38 unformable person-side"* is **person-dependent**: 2 of 38 for a seated holder, 10 of 38 for a non-holder. Re-take it per holder; a single number is now a category error |
| **`13d` OFFICES** | ⭐ **promoted in value.** The remaining 8 of 9 remit verbs are blocked by office DATA, not by any mechanism — seating holders on offices with populated remits now grants them automatically. **Cheapest remaining move on `R-05`** |
| **`19` U7-remit** | **unblocked and re-scoped.** No longer "make them eligible" — all five are formable now and none executes. It is predicates, effects and operands |
| **`19b` U7-disp** | ⚠⚠ **A COLLISION — see below** |
| **`24f`** | its origin. The displacement `13b` caused is what produced the ruling |
| **`13e`, `13f`** | new, both opened by `13b`'s own review |

⚠ **AND THE APERTURE FIGURE IS LOAD-BEARING OUTSIDE THIS PLAN.** Four documents argue from the flat
*"10 of 38"*: `proposals/2026-09-17-governance-and-behaviour/00_THE_SEAM.md` (three times, including
*"the ranking cannot discriminate verbs when 10 of 38 never form"* and *"susceptibility cannot
calibrate on a channel that..."*), its `README.md`, and `RULINGS.yaml:1220` (*"from the aperture being
SHUT"*). **Those are PROPOSED records of what was measured then and are deliberately not rewritten**
— but an argument resting on a shut aperture needs re-taking against a seated holder, and the build
order's own instruction already says so: *"re-take #409's CAT-6 evidence block and STR-4's conclusion
against the new numbers. Both are inferences from a shut aperture. Re-citing them is not the same as
re-taking them."* That instruction now has a trigger.

---

### 3.8a · ~~THE COLLISION~~ — RESOLVED THE DAY IT WAS FOUND, AND THE SWEEP IS WHY

✅ **DISSOLVED 2026-09-18 (`ED-IN-0210`, reversal row).** The sweep below found that closing `13b`
bought `dispatch` while position `19b` was ruled to delete it. Put to Jordan; he reversed the FOLD:
*"i did not realize that meant deleting those verbs. i think that's wrong."* **The verbs stay**,
`19b` reverts to a build, and nothing needed undoing because the FOLD was never executed.

⚠ **THIS IS THE CLEAREST THING THE `§3.0` CADENCE HAS BOUGHT SO FAR, and it is worth saying why.**
The collision was invisible from either end: `RR-A` was ruled on 09-17 without knowing `H-71` would
close on 09-18, and `13b` was built without reading `RR-A`. **Only a forward sweep over the LATER
positions could see it** — and it surfaced a ruling taken after Jordan had said *"I don't remember"*,
which his own earlier ruling (09-15, *"the second option (no response verb) is REJECTED"*) had
already decided the other way. Two of his three statements now agree and the dissenting one was
explicitly taken without recall.

**What follows is the collision as first recorded, kept because the reasoning is the record:**

`13b`'s only measurable effect on the corpus was to put **`dispatch`** into the executed set — one
verb, in one of 89 worlds. Position **`19b`** carries `RR-A`, ruled **FOLD** on 2026-09-17:
*"`comply`, `evade | defy`, `refract` and `dispatch` go; compliance is the executor's own act."*

**So the ruled order deletes the one verb the tier-0 hole bought.** Both are correct as ruled, a day
apart, and neither knew about the other:

| | |
|---|---|
| **If `RR-A` stands** | `13b`'s measurable corpus effect drops to **zero**, and its value is entirely in what `13d` will make reachable. That is a defensible outcome — the mechanism is right and the corpus is what is thin — but it should be a decision, not a discovery |
| **If `dispatch` survives** | `RR-A` needs re-reading now that the verb forms person-side, which it could not when the fold ruling was made |

⚠ **The hole register saw this coming and nobody connected it.** `H-71`'s `unblocks:` names *"`levy`
whose other alternative is also unevaluable"* and `ED-IN-0210`'s open fork is *"are `dispatch` and
`comply` two sides of one thing?"* — **`dispatch` is the subject of both an open fork and a deletion
ruling.** Nothing is done here beyond recording it: `19b` is not re-scoped and `RR-A` is not
re-opened.

---

### 3.8b · FORWARD SWEEP AFTER `13d`-PARTIAL — what the generic spine did to the later positions

**Run 2026-09-19 under `§3.0` phase 4.** What landed is the **thirteen-seat generic governance
spine** (`engine/season/governance_spine.yaml` + `harness/governance_spine.py`), NOT all of `13d`.
Each row is a change made above, not a note left here.

⚠ **WHAT `13d` STILL OWES, STATED FIRST so the position is not read as closed.** Of its five
pieces — bases as rostered values · both predicates rewritten · the four title helpers + `is_title`
+ the `titles` roster deleted · **holders seated** · purview corrected — **only "holders seated" is
done.** Purview is behind `Act.via` (position 6, the Arc-2 gate) and the `is_title` deletion is
behind ruling (3) of `ED-IN-0256` being BUILT rather than merely ruled. The position stays **OPEN**.

| position | what the spine changed about it |
|---|---|
| **★ APERTURE GATE** | its **instrument**. `13b` made the aperture per-holder but left exactly ONE example to measure on (`off_duke`). There are now **13 holders at 7 distinct depths in one world**, so *"re-take it per holder"* has a population rather than an anecdote |
| **`13e` ONE READING OF THE REMIT** | its **test bed**. All 13 seats carry `granted_acts` from `remit_default`, so the two stores are guaranteed to agree today — which is exactly the world in which routing `_eligible` and `_ch_post_remit` onto `t.granted_acts` can be shown to change nothing, and then made to disagree deliberately |
| **`13f` `establish` HAS NO EFFECT** | its **evidence**. `_grant_remit` snapshots at `add_tenure`, and `test_h71_the_grant_is_a_snapshot_not_a_mirror` now has 13 seated holders to show it on. The snapshot-vs-mirror question `13f` must rule is now observable rather than argued from a docstring |
| **`17` U8 / R-06b** | **precedent, and a caution.** `build_at`-from-the-cast is a third builder. The spine's header argues at length why it is NOT a flag on `build_realm` — a regular census and an irregular one must not be one world — and `17` should inherit that argument rather than re-litigate it |
| **`18a` FIELD DELETIONS** | **partially unblocked.** It is gated on `13d`, which is still open. ~~— but its `conferral_path` deletion now has somewhere to point: `ED-IN-0256` records the ruled conferral vocabulary (**appointed · elected · annex**), so the deletion replaces a field with a ruled set rather than with nothing~~ ⚠ **CORRECTED 2026-09-25: this matched on the TERM, not the concept.** `conferral_path` is a Query, not a field. It is an ancestry walk (`world_q.py:539-555`), and r2 `05:450-451` names its successor as `descendants(w, seat.rung)`, the purview walk (`13d-ii`, G3). The ruled vocabulary fills the `Office.conferral` FIELD, which is `13d-i`'s |
| **`19c` MIGRATE** | its **observable**. Two disjoint chains sharing only the realm is the minimum world in which *relocation* is distinguishable from *travel* — a move from chain `a` to chain `b` crosses six containment edges and changes every ancestor but one |
| **`20` U9 / R-04** | ⭐ **materially cheaper.** `faction x` is the first faction whose whole extent is **declared and regular** — 13 offices across 7 rungs. Jordan's *"factions can be of any scale remember"* was a ruling with no fixture exercising it; it now has one, which is what the 44 faction-scale re-scales need to be written against |
| **`24f` SUBSISTENCE IS TERRITORIAL** | its **seats**. The ruling asks for *"NPC synecdoches that just represent the overall population affected"* at territorial scale. The spine has two territory rungs, each with a holder and a remit — the shape a synecdoche attaches to |

⚠ **ONE THING THE SPINE DOES NOT BUY, SAID PLAINLY.** It asserts **shape only**. Nothing propagates
along it yet; `test_the_generic_ladder_is_seven_deep_and_splits_once` says so in its own docstring,
because a green tick on a 13-seat census would otherwise read as evidence of a working channel.
Dissemination and aggregation remain **unmeasured** — the spine is the instrument, not the result.

⚠ **AND IT MOVED A HASH.** `faction x` is a roster member, so `harness/populated.build_realm` mints
a 9th Proposition and the authored realm's `content_hash()` went `8437fca…` → `df6bbb…` (54 → 55
propositions). **MEASURED, and nothing pins either value** — `corpus_run` compares a world against
its own replay, not against a stored digest, and `engine/tests` (sim-regression, 972 passed) is
green. Recorded because §7 says to say plainly when a golden could have moved.

---

### 3.7 · ⭐ SUBSISTENCE IS A TERRITORIAL ISSUE — RULED 2026-09-18 (`ED-IN-0255`)

**Jordan, verbatim:** *"subsistence/starvation should largely be an abstract/governance issue, and we
can just have NPC synecdoches that just represent the overall population affected? i don't think
having lords and guild members etc worry about subsistence is worthwhile"* and *"it's a territorial
issue"*.

**IT ARRIVED AS A CONSEQUENCE, WHICH IS WHY IT IS RECORDED HERE RATHER THAN FILED.** Closing `13b`
gave a seated duke eight formable governance verbs, and they displaced the only subsistence actor in
the canonical test world — because `world_q.presence(w, "S")` is `['p_high']` in every season, so
**the duke WAS the settlement's larder economy**. `test_w8`'s entire drain observable was *"the two
granted transfers whose `from` is `S` and whose `to` is not (`S -> p_high`, one grain each)"*. The
ruling says that model is not worth having, so the guard was **retired rather than re-pointed** — and
it could not have been re-pointed anyway: `p_low` and `p_mid` sit at the hearth `Hh`, never at `S`.

**WHAT IT CHANGES, and each is a row rather than a paragraph:**

| | |
|---|---|
| **`24f`** | the unit itself — the demographic loop moves to a territorial quantity with population synecdoches |
| **`24`, `24d`, `24e`** | re-scope. `3a`'s per-eater draw and `3b`'s per-body write are PERSON-scale, which the ruling moves. `24d`'s ruled `capacity(w, rung)` is already rung-scoped and is CONSISTENT with it |
| **`ED-IN-0247`** | ⚠ **re-opened at a deeper level.** It was *"pick `body_step` off the sweep 0/10/67"*. The ruling asks whether a per-PERSON body write is the right carrier at all. **Answer the scale before the number** — a value chosen for the wrong carrier is worse than none |
| **`test_w8`** | its non-vacuity guard is gone, deliberately, and the comment at the site is the pointer to rebuild it on the territorial quantity |

⚠ **WHAT THIS RULING DOES NOT SAY.** It does not retire the larder, `nearest_store` or the ladder —
`3a` is built, measured to meet its demand, and untouched. It says the *decision* about food is not a
lord's, and the *scale* is territorial. Nothing here licenses deleting working code.

---

### 3.9 · THE CONFLICT SWEEP — shared files and hard serial edges (2026-09-25, `ED-IN-0270`)

**What this adds, and why here.** `§4` gives a file census for the pairs it names, and until now
nothing gave one for the governance · settlement · NPC positions. `§3.1`'s phases are derived from
this section. It was taken by a read-only pass at `534a2bc` plus `952dc21`. ⚠ **Line numbers move;
re-derive a site by grepping its symbol, never by trusting a number written here.** One count was
re-measured when this was written up: **G2's gate sites are 36** — an `ast` walk over
`engine/season/**/*.py` minus `tests/`, `Call → Attribute attr == "write"`, grouped by receiver: `w` →
`harness/probes.py` 20 · `loop/matter.py` 8 · `loop/witness.py` 4 · `loop/calendar.py` 2 ·
`loop/resolve.py` 2; `TRACE` → 9, not gate sites. `§7`'s *"33 was right"* was right on the day; since
then MATTER gained item 3b's `body`/`exists` writes (`matter.py:309,322`), and WITNESS gained one.

**Shared files — the positions in scope that edit each.**

| file | edited by | consequence |
|---|---|---|
| `loop/effects.py` | `13f`, `7a`, `15`, `16`, `17a`, `19`, `24e`, `10`, `12` (scar), G4 (rewrites all) | every effect landed before G4 is rewritten by G4; every effect after is written once |
| `loop/resolve.py` | `13e`, G2, G3, G4, `19` | |
| `epistemic.py` | G1b (readers done), `13e`, `11a`, `17a`, `12` (the scar rebuild reads `observers_for`) | |
| `state/world.py` | G1b, G2, G3, `15`, `18a` | the `World.write` signature is where `4 → 5` collides |
| `loop/witness.py` | G1b (done), G2, `15`, `15b` | |
| `loop/matter.py` | G2, `11a`, `24f`, `24` (P1) | |
| `loop/calendar.py` | G2, `11b` | |
| `queries/world_q.py` | `11a`, `17a`, `18a`, `18` (PROC-A), `24d-ii`, `15c` | |
| `loop/predicates.py` | `13d-i`, G3, `19` | |
| `state/carriers.py` | G1b, G3, `15`, `18a`, `12`, `12b` | |
| `verb_table.yaml` | `13f`, `15`, `16`, `19`, `19b`, `24e`, `10`, `12`, `ED-IN-0261`'s verb split | |
| `write_matrix.yaml` | `13f`, `15`, `17a`, `18a`, `12`, `24e` | |
| `rosters.yaml` | `11a`, `13d-i`, `15`, `24d-i`, `24d-ii`, `10`, `12b`/`12c`, `8` | |
| `harness/probes.py` | G1b (its `Ev()` constructions), G2 (20 sites), `11a`, `15`, `18a` | |
| `harness/populated.py` | `13d-i` (`offices.yaml`), `24d-i`, `10` (construction-time stance) | |

**Hard serial edges — beyond `4 → 5`, which stands (`§4`).** Each is a shared function, a shared
row, or a produced-then-consumed symbol. `isolation: worktree` defers these to the merge; it does not
remove them.

1. **G1b's deletion → `11a`.** G1b rewrote where `epistemic._event_place` gets its id; `11a` moves the
   function to `world_q.place_of`. Never both in flight.
2. **`13f` → `13e`.** `13e` makes the resolver snapshot-dependent; `13f` decides the semantics.
3. **`13d-i` → G3.** Both rewrite `_req_confer` and `_req_revoke`: `13d-i` puts the bases in as
   rostered values, then G3 re-points the basis walk at `via.scope`. Or G3 does both — never in
   parallel.
4. **`13e` → `17a`.** Both edit `_ch_post_remit`. `13e` is one line; `17a` replaces the function.
5. **`18` → `18a`.** `18` BUILDS `world_q.judging_set(w, venue, matter)`, which `19`'s `determine`
   consumes; r2's item 14 deletes a STUB of the same name. **Picked: `18` first** — the table's own
   order — so `18a` deletes only what `18` has replaced.
6. **`15` → `19b`** (the operand); **`15` → `24e`** (`record_kinds`); **`15`/`15c` → `7a` → `17a`**
   (the aperture, BO-10).
7. **`24d-i` → `24e`, `19c`.** ~~`24d-ii` lands inside whichever of the two is first~~ `24d-ii`
   lands inside `19c`, its only caller in scope. `24e`'s `found`/`build` grow what it counts and
   do not call it (corrected 2026-09-25).
8. **`24f` → any `body_step` pick**, and any claim that P1 is done.
9. **G4's pre-flight → the `_eff_work` rewrite.** `work`'s deferred accumulator
   (`loop/resolve.py:641-653`) must be given a place where `NoOpReceipt` is judged first.
10. **The cells commit (`12b`/`12c`/`12d` + `ED-IN-0261`'s verb split) ↔ `8` and `9`.** Same
    `kill / wound` row and combat wrapper. Either order; never interleaved.
11. **`18a` must not delete `Tenure.payload`.** An edge against an old list rather than between two
    positions: the field went live under `13b`.

The plan rows these findings falsified are corrected in place above, each marked with its date.

---

**Parked, with reasons (not positions):** VOCAB-BALLOT — its output is a document (§0.2), and three
of its four contested rows are settled by positions 5 and 8; rebuild it after those land.
PHIL-DEBT — the as-structure row owed at `canon/philosophy/00_standing.md:78`; content authoring,
blocks nothing. OLD-DRIVER — **drop** (§0.1 pt 5: its artifact is load-bearing only on this
repository's process, so *"accept the defect and write nothing"*). PC-COMBATPOOL — demoted to a
record defect: the code already has one owner at `combat_engine_v1/core.py:48-51`; two of the three
"definitions" are prose that dies at position 2. CANDIDATE-WHY — rides at 14.
`ED-MB-0044/0056/0057` — a hand pass, not a position. **Build-order item 11** — retired as H-71's
answer by `CAT-6` arm 2. **Build-order 6f and 6g** — 6f needs `12b`–`12d` first; 6g ~~is H-71's open
second half~~ closed 2026-09-24 (`ED-IN-0267`, §3.4).

**Record defects, which ride along with whatever position touches them and are never scheduled:**
`H-46` still `absent` after U3 landed · the `workplan_v6_progress.yaml` / `CLAUDE.md` §0,§9 /
`m1_acceptance.py` binding to the retired M1 board · `HANDOFF_META_ARCHITECTURE.md:3` reading
PROPOSED under a RATIFIED directory · the spine's spent §0 table · `ED-MB-0016`'s file cites pointing
at paths the 08-24 port deleted · `ED-IN-0210` reading `status: ruled` while carrying an open fork ·
~~`CURRENT.md:31` reading *"DISTINCT and unchanged"* against `ED-IN-0251`'s R2~~ ✅ **FIXED
2026-09-19 — Jordan ruled *"Truth becomes Conviction"*** and the row carries the absorption · ⚠
`CURRENT.md`'s `_Last reconciled:_` stamp is **STILL at 2026-09-16 against 18 heads touched 09-18,
and was deliberately NOT bumped** when that row was flipped: bumping silences all 18 without
reading one, so the flip is a dated note beneath the stamp instead. **This defect is live** · **`R7` naming two live
rulings and two different `R3`s existing** (`ED-IN-0252` §4).

---

## 4. PARALLEL LANES — named as a departure, because a spine was asked for

The existing spine serialises deliberately. These pairs are genuinely order-free; one order is still
picked, and the cost of serialising is stated rather than hidden.

| order-free pair | why | order picked, and why |
|---|---|---|
| 1 ∥ 3–7 | ledger JSONL vs `engine/season/state` — no shared file | 1 first: one session, and it makes §5 readable |
| 2 ∥ 3–7 | `systems/`, registries, `tests/valoria` vs `engine/season/{state,loop}`; the only shared file is `seam/wrappers/sigma.py`, which no G-unit touches | 2 first: ruled and unexecuted for five days |
| ~~4 ∥ 5–7~~ **NOT order-free** | ⚠ **This row claimed order-freedom on the spine's authority (`:61`) rather than on a file census, and it is the one row where the files collide.** G1b rewrites `state/world.py`'s content hash and `loop/witness.py`'s whole `actor` mode; G2 rewrites gate call sites in **both** — and they meet inside one signature, `World.write`'s `def write(..., subject=None)` (~~`world.py:295`~~ `world.py:467-472` at `952dc21`), whose `subject` parameter G1b deletes and whose write class G2 replaces. `isolation: worktree` does not help: it defers a shared-file edit to the merge | **4 → 5 is a hard serial edge.** Every other row in this table carries a file census; this one now does too |
| 8, 9 ∥ 3–7 | wrappers hold no token (`04:164`); `combat_engine_v1` is outside `04`'s scope | after G4, so their Events land once on the finished contract |
| 12 ∥ 13 ∥ 14 | disjoint but for `verb_table.yaml` (12 and 14 both edit it) | 12 → 13 → 14; 12 first because 14's contested closers reuse its degree-keyed rows |
| 18 ∥ 13–17 | `world_q.judging_set`, `arrangements.yaml`, the stress re-host touch none of their files | 18 immediately before 19, which consumes it |
| 23 ∥ 22 | ids/loader vs seam provider | 22 first: game before contract |

If any pair is actually run concurrently, use `isolation: worktree` (`CLAUDE.md` §10).

**The file census for the governance · settlement · NPC positions, and eleven hard serial edges
beyond `4 → 5`, is `§3.9`** (added 2026-09-25, `ED-IN-0270`).

---

## 5. THE RULING BATCH — what actually needs Jordan

Eleven items, ordered by what each unblocks. Each is answerable without reading a plan.
⚠ **THREE WERE ANSWERED 2026-09-19 and are struck rather than deleted, so the count and the
order do not shift under a reader returning to this list:** item 3(i) (`ED-SE-0051`),
item 3(ii) (*"accept"* — P1/P3/P4, `ED-SE-0054`), and the `CURRENT.md:31` record defect
in §5's preamble (*"Truth becomes Conviction"*).
⚠ **AMENDED 2026-09-25 (`ED-IN-0270`), on the same rule:** item 1 is struck as superseded, and three
items are APPENDED as 11–13 rather than re-ordered in, so no number already cited moves. One question
never reached this list and is already answered: `24d`'s dwelling substrate, ruled 2026-09-25
(`ED-SE-0055`, §3.6).
**Below item 13 is the other half — the questions that are NOT Jordan's**, recorded so that no later
session re-escalates them.

0. **THE UNDECLARED CONTENT-HASH TIEBREAK — and this one is needed before position 3.**
   ⚠ **Added by the antagonist pass, which caught the first draft taking one of a pair and dropping
   the other.** `HANDOFF.md:256-257` names *"Two rulings wanted: the undeclared content-hash tiebreak
   that decides which question a person answers, and `H-111`"*. The draft took `H-111` (item 9) and
   said nothing about its sibling. That matters more here than anywhere, because **positions 3, 4, 5,
   6, 7, 20 and 22 all use hash stationarity or a named hash move as their control**, and `ED-IN-0206`
   records that the clause-4 corpus demonstration *"rests on one act selected by an undeclared
   content-hash tiebreak, so ANY change that moves the hash can extinguish it."* A control whose
   discriminator is a documented undeclared tiebreak is not a control (§0.1 pt 4).
   **Does this need you at all, or does §0 test 5 answer it — declare the incumbent tiebreak at the
   site and record it, rather than rule on it?** The tree has applied that remedy twice already
   (`H-54`, `H-122`). If test 5 answers it, it is position 3's first pre-flight step and not yours.
1. ✅ **~~ED-IN-0214 — the conviction matrix.~~ SUPERSEDED 2026-09-20 by `ED-IN-0261` (§0 test 1).**
   The basis this asks about no longer exists: thirteen convictions over four axes became FIFTEEN
   pursuits over SEVEN bipolar axes, with every cell re-authored on
   `proposals/2026-09-20-pursuit-basis-worksheet.yaml`. So *"re-centre, or keep the authored matrix?"*
   has no *keep* arm, and **the cells commit IS the re-centre** — no `14a` is inserted. What it
   asked for is item 11. ⚠ Its row still reads `status: open` / `needs_jordan: true`, and it sits in a
   FROZEN archive (`registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml:2504`, never
   edited), so the closure is a new row under the id in the live IN ledger — position 1's work. The
   question as it stood, kept for the record:
   Nine of thirteen convictions point within 60° of one mean
   vector, so convictions differentiate a person's own options well and *different people* badly.
   Re-centring overwrites 52 cells that `conviction_axis_matrix_v30.md` §3 argues individually.
   **Re-centre, or keep the authored matrix?** Answer before position 11 — a later *yes* invalidates
   U6's number.
   ⚠ **And a *yes* has no position to land in**, which the antagonist pass caught: arm (b) is a
   52-cell re-authoring that moves measured behaviour (distinct executed sets 40 → 27 on the same 89
   worlds when U3 landed). A *yes* returns to the sequencer and inserts **14a · MATRIX-RECENTRE**
   immediately before position 11, so its hash move lands before the measurement rather than after.
2. **ED-IN-0210's fork — is `comply` one verb or two?** Does an `issue`d dispensation and a
   `dispatch`ed order get answered by the same `comply`/`evade`/`refract` keyed on the ledger claim
   **(A)**, or does `dispatch` need its own obey/disobey pair **(B)**? Evidence leans A. Unblocks 19b.
   (`refract` is now `construe` — renamed 2026-09-18, `19b`'s row. And `19b` also waits on `15`/`15c`
   whichever way this goes, so the ruling is not the only thing between it and a build.)
3. ✅ **~~ED-SE-0051~~ ANSWERED 2026-09-19 — the settlements set's half (ii) remains.**
   (i) ~~Bound the demographic loop by matter only (A) or matter plus a hearth-capacity table per
   site kind (B)?~~ **RULED: the capacity arm — and NOT the shape this question offered.** Jordan
   took *matter plus hearth capacity* as a `capacity(w, rung)` **Query over the rung's dwelling
   Sites, with a floor, never a fixture table**; the *"hearth-capacity table per site kind"* the
   question itself proposed was refused, because a fixture is a second home for a fact the Sites
   already carry (§0.05 cl.1). `found` (P4) is the throttle, scoped to populations. Closed at the
   ledger with a second row under the id; `24d` is ungated and blocked only on `capacity` having
   zero code.
   ✅ **(ii) ANSWERED 2026-09-19: *"accept"*** (`ED-SE-0054`). **P1, P3 and P4 are accepted for
   build.** P2 is NOT in the acceptance — the question named three, and P2 is the loop `ED-SE-0051`
   just bounded. ⚠⚠ **P1's CARRIER IS STILL IN QUESTION AND THE ACCEPTANCE DOES NOT SETTLE IT:**
   P1 writes `(Person, body)` on every eater at a rung, and `ED-IN-0255` ruled subsistence
   TERRITORIAL — *"i don't think having lords and guild members etc worry about subsistence is
   worthwhile"* — which is P1's mechanism exactly. **P1's write site inherits `24f`'s open scale
   question**; build the shortfall reaching bodies, and settle whose body at `24f`. A session
   building P1 without reading `24f` builds the carrier that was ruled against.
   ⚠ Neither P3 nor P4 is buildable as it stands and `04_EVALUATION.md` grades both `paper`: P3 has
   two writes the gate refuses, P4 **refuses at load** pending three table corrections. Build
   details, not design questions — the first work of the position rather than a qualification.
4. **ED-MB-0061 + ED-MB-0016 — the mass-battle golden.** Re-base one global golden with every F1–F8
   flag **ON (A)**, or keep per-flag baselines **(B)**? Recommendation on record: A. Unblocks 25 and
   the three flags whose defaults contradict their own comments.
5. **The Godot version.** Target the version `project.godot` and the game repo's CI pin **(A)**, or
   4.6 as `godot/godot_conversion_strategy_v1.md:41` documents **(B)**? Unblocks 26, PART E step 13,
   ED-1050's deferred re-export, and held H6. `CLAUDE.md:9-12` forbids settling this by editing a doc.
6. **ED-WR-0010 — is threadwork in scope** after ED-IN-0204 retained only SC/PC/MB? Decides whether
   position 27 exists at all.
7. **D2 — the tenth attribute.** Is it `Recall`, and are the Spirit/Will and Cognition/Acuity folds
   inverted? **Inert for `engine/season` today** — it reads only the conviction roster from the
   registry, never attributes — so this is a registry edit that matters for Godot binding.
8. **Held H5 — the degree-ladder divergence** between `combat_engine_v1/core.py` and
   `sigma_leverage.degree`, held by explicit ruling 2026-08-14. Keep the hold, or name one owner?
   Blocks nothing; position 2 does not touch it.
9. **H-111 — does a refusal propagate as news?** Both answers run. Blocks nothing.
10. **VOCAB-BALLOT — deferred deliberately.** 13 one-word RATIFY rows, but its own header says
    *"DO NOT RULE ON THIS FILE YET … Rebuild before ruling"*, and positions 5 and 8 re-derive three
    of its contested rows. Do not put the current file in front of Jordan.
11. **`12b` / `12c` — the pursuit cells** (`ED-IN-0261`; added 2026-09-25). Fill the `set:` cells of
    `proposals/2026-09-20-pursuit-basis-worksheet.yaml`: 15 pursuits × 7 axes, plus the alignment
    re-cell over the verbs, including the split rows `kill`, `wound`, `fight`, `challenge` and
    `accept`. **This is the only authored CONTENT in the governance · settlement · NPC scope**;
    everything else in `12b`–`12d` derives from it in one R6-atomic commit. Jordan's own falsifier:
    the devout-Solmund / anti-Solmund `faith` pair must land far apart. Unblocks `12b`, `12c`, `12d`'s
    substrate half, the verb split and the scar rebuild (`12`); blocks nothing in phases α–γ.
12. **Position 9 — build or strike §11.4 Surrender and Disengage** (added 2026-09-25).
    `registers/handoffs/HANDOFF_PC.md` asks it in those words. `§3.2`'s row reads *promote*, but that
    is an ORDER placement, and the 2026-09-12 merge ratified §3's order and nothing else — so it does
    not close the question. Beside it, an administrative item that is not a design call: the PC
    `ED-` id block is exhausted and needs a release. **If strike**, position 9 leaves the order and
    nothing else moves.
13. **`ED-IN-0247` — `body_step`** (added 2026-09-25 so the batch is complete; already
    `needs_jordan: true`). A pick off the sweep 0 / 10 / 67 — **but only after `24f` has settled
    whose body carries it** (§3.7). A value chosen for the wrong carrier is worse than none.

**NOT JORDAN'S — answered by §0's ladder (recorded 2026-09-25, `ED-IN-0270`, so that no later session
re-escalates them).** Each carries a candidate answer or names who answers it. An antagonist attacks the
candidate; an attack that lands sends it back through the ladder, not to Jordan by default.

| question | ladder step | the answer, or where it is decided |
|---|---|---|
| **`13f` — does a remit change reach SITTING holders (mirror) or only future ones (snapshot)?** | 5 | Candidate: `_eff_establish` writes the office AND re-stamps the payload of every live `hold` on it, in the same act. `(Tenure, payload)` and `(Office, remit)` are both licensed `[RES] ACTS` rows, so the grant still changes only by an act (snapshot's property), sitting holders are reached (mirror's observable), and `choose` still takes no `World`. ⚠ **The licence reaches the act only if `establish`'s `writes:` declares `Tenure.payload`** (with `tenure.payload_set`). It does not today (`verb_table.yaml:229`), and that is a REQUIRES of the candidate. **Same step, same candidate:** an `establish` naming an office id that already exists is a REMIT CHANGE, not a refusal. It is the only act that writes `Office.remit`, so refusing it would leave no act able to change a remit. `_part2` 13f |
| **G4 — where is `NoOpReceipt` judged for `work`'s accumulated delta?** | 5 | G4's pre-flight: at the accumulator's write, per subject, carrying the contributing act ids — decided before `_eff_work` is rewritten. `_part2` 7 |
| **`12` — does `(Person, axis_count)` survive once scars are counts?** | 4 / 5 | The count-scar IS the counter: retire the `axis_count` row, or give it the field. Never build both. `_part2` 12 |
| **`24f` — who eats?** | 5 | Candidate: `weight > 1` (a cohort, `carriers.py:447`) eats; `weight == 1` is exempt — Jordan's *"lords and guild members"*. ⚠ **DEAD ON ARRIVAL until something mints cohorts** (attacked 2026-09-25): every built world holds only `weight == 1` persons, so this reads as zero eaters and switches off `3a`/P1. It is not taken until a cohort producer, and what it mints from, is named. The NUMBER is item 13. `_part2` 24f |
| **`19c` — what is the difference between presence and residence?** | 5 | Architecture, once `24d` exists: what `move` leaves behind against what `migrate` writes. `_part2` 19c |
| **`18a` against `18` — who owns `judging_set`?** | 4 | The table's own order: `18` builds it, then `18a` deletes only the stub. `§3.9` edge 5 |
| **`24d-i` — does `build_at` mint dwellings too, or only `build_realm`?** (and `governance_spine.build`, and `probes.tiny_world`) | 5 | Decided in `24d-i` and stated there. It decides whether capacity can vary on a corpus world, and on the spine, where `19c`'s observable runs. §3.6 |

---

## 6. WHAT THIS SEQUENCE DOES NOT COVER

- `[GAP: PART E step 12 (parallel DELIBERATE map) and D-41a's permutation falsifier — beside the critical path; no R-row moves on them]`
- `[GAP: the FA lane beyond OLD-DRIVER — superseded at step B; its subject is expressed by position 20's faction queries, not by systems/factions/]`
- `[GAP: proceedings PHASE 1/3/4 — position 22 covers the provider critical path only]`
- `[GAP: any GDScript grade — every compliance clause here is the Python grade; `04:79-80` states the Python and GDScript grades separately wherever they differ, and no position targets GDScript before 26]`
- `[GAP: the 143-case count — `len()` over results.json gives 46 NPC + 97 ARC, but a grep over cases/ finds 100 `id:` lines and chain/*.yaml does not parse with plain PyYAML. An antagonist re-derived ARC as 59 by grepping `"id": "ARC` and was wrong — the structural count is 97 — which is itself the evidence that this figure needs one owner. Position 13 must use the harness loader's count, not any of these]`
- `[GAP: tools/m1_acceptance.py rows 1 and 4 — a Layer-0 board reader; §0.1 pt 5 forbids re-tooling it, and the CLAUDE.md sentence binding to it rides at position 1]`
- `[GAP: 2026-08-15-character-and-faction-stats-and-progression.md — ownership UNRESOLVED since PR #370 closed unmerged; §5 item 7 is the only live question in it]`
- `[GAP (2026-09-25): no content owner for 13e, 13f or 24f beyond §3.2's rows and _part2's entries. 13e/13f have only epistemic.py:420-436 and test_h71_the_grant_is_a_snapshot_not_a_mirror's docstring; 24f has only §3.7. What _part2 now says is the whole of the specification]`
- `[GAP (2026-09-25): no instrument runs the populated realm for the ★ gate. corpus_run and register --requirements score the corpus only, and test_the_generic_remit_seats_every_office_and_unblocks_the_nine asserts formability, not execution, and says so]`
- `[GAP (2026-09-25): 19's determine has no judging_set until position 18 (PROC-A) lands — SC lane, outside the governance · settlement · NPC scope, and a hard dependency of it]`
- `[GAP (2026-09-25): the ★ gate's "claims by source" and "questions by source" figures are 2026-09-17 values. The instruments are harness.populated and questions_for (01_THE_BUILD_ORDER.md :190-205) — re-run, do not re-cite]`
- `[GAP (2026-09-25, ED-IN-0270): the birth-side consumer of capacity. RR-2 bounds POPULATION ("applied here to births"), and nothing in scope grows one. loop/census.py owns weight and envelope and writes nothing ("NO CLOCK GENERATES ANYTHING", :33), and the only envelope write is probe W9's (harness/probes.py:1639-1650). So 24d-ii's one in-scope caller is 19c's migrate, and the throttle the ruling describes has no subject yet. No position here builds one]`
- `[GAP (2026-09-25, ED-IN-0270): a producer of synecdoche cohorts. 24f's who-eats candidate needs weight > 1 persons on a built world, and none mints them (_part2 24f). Naming it is 24f's first step, not a scheduled position]`

---

## 7. HELD BACK FROM RATIFICATION-ON-MERGE (`CLAUDE.md` §2, ED-1094)

Merging this PR ratifies **the order in §3 and the supersession verdict in §1**. Six things are
explicitly held back and must not be read as ratified by the merge — items 5 and 6 were added by the
antagonist pass, which found two departures the first draft made silently:

1. **The ~97 queue closures of §2.1 are NOT applied.** They are position 1's commit. Each asserts a
   question is dead; bundling 97 such assertions into a planning PR is the anti-pattern §2 names.
2. **No `## Status:` line moves on any superseded document**, and no `CURRENT.md` row changes. §1 is
   a verdict about what a session should act on, not a retirement wave. The retirements it implies
   (`workplans/README.md`, the 17 superseded proposal clusters) want their own `FORK:` rows.
3. **The Arc-2 five-unit re-cut** (G1a/G1b/G2/G3/G4) remains the conformance plan's to absorb, per
   the spine's own §7.1. This document sequences it; it does not own it.
4. **Position 23's scheduling of PART E steps 0 and 2 is a departure from the spine**, which held
   them *"unscheduled by design"* (its §7.3). Jordan asked for everything sequenced, so they are
   sequenced — after the second measurement, where zero-yield contract work is hash-stable by
   construction. If the spine's non-scheduling was deliberate beyond its stated reason, this reverts.
5. ⚠ **Position 19b schedules `U7-disp`, which the spine placed OFF-spine — a second undeclared
   departure, caught by the antagonist pass.** Spine `:57`: *"**genuinely Jordan's** … **Do not
   schedule it until ruled.**"* Its §7.2 makes that placement conditional, returning the node to the
   spine *"between positions 10 and 11"* only **if** the fork turns out not to be genuinely Jordan's.
   §5 item 2 here affirms that it **is** genuinely Jordan's — which under the spine's own condition
   keeps it off-spine, and 19b contradicts that. It is given a position because Jordan asked for
   everything sequenced, and it is marked conditional on the ruling in both §3 and `_part2`. If the
   spine's placement governs, 19b reverts to off-spine and nothing else in the order moves.
6. ⚠ **`build_at`'s consumption of the `cast:` blocks moved from U8 to position 13**, which is a
   CONTENT move made by a document that claims to own only ORDER. The spine gives W28-cast *"author
   the `cast:` blocks"* and U8 *"`ambitions(p)` and `build_at` from the cast"*. Position 13 takes the
   reader on `04:124`'s no-unread-row grounds, and position 17 no longer claims it. Held back because
   the r-execution plan owns U8's content, not this file.

**Three agent claims overturned by the author against the tree**, recorded so they are not
re-derived: the `## Status: PROPOSED` count (**200 repo-wide / 162 in scope**, not 129, 133 or 168 —
the regex must tolerate bold); `H-83`'s *"no reader"* (`stratum_of` is live at `loop/resolve.py:588`,
called from `:373`); and `ED-IN-0208`'s headline (§2.3).

⚠ **AND TWO OF THE AUTHOR'S OWN OVERTURNS WERE THEMSELVES OVERTURNED BY THE ANTAGONIST PASS. Both are
recorded here rather than quietly corrected, because both are instances of named defect classes this
repo has paid for before.**

- **The spine's "33 `.write(` call sites" was RIGHT.** An `ast` walk counting `Call → Attribute →
  attr == "write"` returns 42, and the author reported that as an overturn. **Nine of the 42 have
  receiver `TRACE`** — `trace_log.py:116`, a different object with a different method — and **33 have
  receiver `w`**, the gate. Counting two APIs as one because they share a method name is
  term-matching on the name rather than the mechanism, which is the failure `CLAUDE.md` §8 records
  `pathres.resolve()` committing at scale. G2's scope is **33 gate sites**; whether the 9 tracer
  calls ride along is a separate question its pre-flight answers. ⚠ **36 at `952dc21`** — the same
  method, re-run 2026-09-25; MATTER and WITNESS gained sites since (`§3.9`).
- **ED-SC-0033's "47 files" was not wrong, and neither was the author's "46" — both are unstable.**
  `systems/social_contest/` reads 46 or 47 on `find` depending on `__pycache__` churn. The number
  that means anything to a `git rm -r` is **28 tracked** (`git ls-files`), of which 21 are `.py` and
  7 `.md`. A count that moves when nobody edits anything was never a measurement (§0.1 pt 4).

---

## 8. PROGRESS — 2026-09-13 (appended; the ORDER above is unchanged)

**Recorded here rather than by editing §3, because the sequence is RATIFIED and this session did not
re-sequence it.** Jordan, 2026-09-13: *"update that ratified workplan."*

### 8.1 · What landed

| | | evidence |
|---|---|---|
| **The told channel** — a telling now transmits its CONTENT, not only that it happened | `ED-IN-0222` | `loop/witness.py`; `told_by` claims 0 → 8 corpus-wide |
| **A populated world** — 46 named NPCs, 37 settlements, 60 quarters, 211 buildings, 26 inhabited | `ED-IN-0223` | `harness/populated.py`, `venues.yaml`, `npcs.yaml`, `tools/export_npc_roster.py` |
| **The milestone gate re-pointed at the head** — rows 1–2 probed `engine/mc_v18` for six days | `ED-IN-0226` | `tools/m1_acceptance.py` |
| **`mc_v18` deprecated in place**, shrink-only ratchet, 16 importers, none production | `ED-IN-0227` | `tests/valoria/test_mc_v18_is_deprecated.py` |
| **⭐ THE COUNTERPARTY** — every person's OUGHT now names a PERSON | `ED-IN-0210` Ruling 1 | `harness/corpus_run.py::build_at` |

**The counterparty change, measured through the season driver over the 27 NPC cases that build:**

```
control (rung subject)   443 acts     0 naming another person
shipped (person subject) 692 acts   256 naming another person
distinct executed sets    25 -> 43        verbs executing  11 -> 13
```

⚠ **IT IS NOT ONE OF THE 27 POSITIONS.** It is a new item, taken because it was the cheapest change
in the tree with the largest effect on the game and it executes a ruling Jordan had already made.
**It is not downstream of Arc 2** (positions 3–7) — it changes world CONSTRUCTION, not an effect, so
`ED-IN-0212`'s "the gate's signature IS the effect contract" does not reach it. Anything that writes
a verb's effect still is.

### 8.2 · The two costs it bought, as follow-on items

Neither is scheduled here; both are named so the next session does not rediscover them.

1. **`tell` collapses 57 → 10 executions (82%).** The transmission verb — `ED-IN-0222`'s own subject
   — fires far less once people have person-subject questions to pursue. Belief transmission got a
   channel and then lost most of its traffic in the same session.
2. **`travel.blocked` beliefs 6 → 192 (32×).** Root cause, from an adversarial pass: `build_at` seats
   all three people as `person`-kind rungs, `contain_ascends` requires **strict** ascent, so two
   `person` rungs tie and a `move` naming a person **always refuses**. A person-subject question
   should not mint a `move` candidate targeting a person — that is `decision/options.py`'s
   `_derive_operand`, and it is the fix, not the Proposition. (`move` still EXECUTES 17 → 73, so this
   is ledger noise rather than a dead verb.)

### 8.3 · Corrections to this document's own surrounding surfaces

- **§5's ruling batch: `ED-WR-0011` is CLOSED.** `registers/editorial_ledger_wr.jsonl` carries a
  second row under that id — `status: ruled`, `needs_jordan: false`, *"OI-05 RULED BY JORDAN,
  2026-09-13 … Season-tick generation = **none**, which is a RULING rather than a deferral."* That is
  Option A of the two the row itself drafted, i.e. the generator answer. `ED-SE-0051`/E-1 remains open.
- **`ED-IN-0210` keeps `needs_jordan` deliberately**, for its one live fork (*are `dispatch` and
  `comply` two sides of one thing?*), which `ED-IN-0211` records as surviving §0's five tests. A
  close-pass that clears it on "ruled + still flagged" deletes a live escalation — position 1 should
  skip it by name.
- **§2's queue figures have no instrument and four surfaces disagree.** 108/158 here (2026-09-11);
  151/105 then 153/106 in `HANDOFF.md`'s 2026-09-10 section; 41 / 51 / 77 by hand today depending on
  the predicate; 37 after folding append-only rows to the latest per id. **Position 1 should ship the
  fold-to-latest script as its instrument**, or the "queue reads ≤ 12" acceptance cannot be checked.
- **`requirements.yaml` carries FOUR mutually inconsistent R3 figures** (~~`:142`, `:265`, `:333`,
  `:524`~~ — the lines moved; re-located 2026-09-25 in position `21`'s row: `:142`, `:172-177`,
  `:263-267`, `:364-365`, `:555`) with no statement of which is the baseline. Any position measuring
  propagation trips on this.
