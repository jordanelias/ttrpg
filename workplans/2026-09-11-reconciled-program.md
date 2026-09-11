# THE RECONCILED PROGRAM — every live item, in one order, across every lane

## Status: PROPOSED (ED-IN-0215)
## Owner: infrastructure / cross-cutting (IN lane)
## Supersedes: nothing outright. It becomes the SINGLE OWNER OF THE ORDER across all lanes,
## which `workplans/2026-09-11-arc-sequence-spine.md` (ED-IN-0212) owned for the IN-lane engine
## work alone. Unit CONTENT stays with its owners: `2026-09-09-r-execution-plan.md` (U5–U10),
## `2026-09-09-layer1-conformance-plan.md` (G1–G4), `proposals/2026-09-05-proceedings-subsystem/`
## (the proceedings build order). Detail per position is in `_part2`.

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
| **SUPERSEDED BY `architecture/`** | greenfield v1+v2 · valoria-from-scratch · ideal · ideal-v2 · unified-code-shape · shape-tracer · holonic-architecture · throughlines · integration · authoritative-architecture · arc-reachability · play-space-coverage · pr350-archive-recovery · governance-corpus-rebuild. **Each names its own successor in its own status line** |
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

Measured across 14 `registers/editorial_ledger*.jsonl`: **1,268 rows · 158 `needs_jordan: true` ·
108 of those `status: open`.** `ED-IN-0208` pinned 151/105 on 2026-09-10, so **the queue grew by 7
flagged and 3 open in the week that measured it, and nothing was closed.**

### 2.1 The closures, by test (`CLAUDE.md` §0's ladder)

| test | count | ids | the citation that closes them |
|---|---|---|---|
| **1 superseded** | 23 | `ED-FA-0018/0027-0034`, `ED-SE-0031-0044` | ED-IN-0204 Decision 1 — every row's `Target:` is a layer no longer retained |
| **1** | 6 | `ED-FA-0010/0013c/0014/0015/0016/0035` | same |
| **1** | 9 | `ED-SE-0002/0013/0014/0015/0017/0045/0046/0047/0048` | same; `engine/season` reads no geography file at all |
| **1** | 4 | `ED-IN-0030/0048/0049/0050` | the scale bridge is Layer 1 now — `04 §B.7:330` |
| **1** | 8 | `ED-IN-0062/0070/0066/0073/0148/0151` + 2 REMEDIATION | dockets over the evacuated `designs/audit/` tree and the transitional 27-module driver |
| **1** | 4 | `ED-1051`, `ED-1043`, `ED-MB-0065`, `ED-IN-0123/0124` | port target is `port/` from the season loop (`04:137`); the 08-24 port settled which MB tree is canon **by execution** |
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

## 3. THE SEQUENCE — 27 positions, all lanes

Detail per position — INSTRUCTION, LAYER, COMPLIANCE CLAUSE, OBSERVABLE/FALSIFIER, TIER — is in
**`_part2` §8**. This table is the order and nothing else.

| # | handle | lane | one line | ruling? |
|---|---|---|---|---|
| 1 | **CLOSE-PASS** | IN | flip the ~97 rows of §2.1 with their citations; the queue reads ≤ 12 | — |
| 2 | **RET-SC** | IN/SC | execute the ruled `systems/social_contest/` retirement; relocate the demote-only rule first | — |
| 3 | **G1a** | IN | act store · `Receipt` · `state/gate` · `log.append` assertion · the ruled `Record.matured` write | — |
| 4 | **G1b** | IN | delete `Event.subject`; read the actor through `causes[] → state/acts` | — |
| 5 | **G2** | IN | one `Token`, minted in `loop/driver` only; **42** `.write(` sites | — |
| 6 | **G3** | IN | `NotYours` at the gate · `Act.via` · purview through `via.scope` | — |
| 7 | **G4** | IN | `NoOpReceipt`; the effect contract finalised; 11 effects rewritten once | — |
| 8 | **H-98** | IN/PC | the combat seam returns a `Margin`, not a winner; the fourth band gets a producer | — |
| 9 | **PC-SURRENDER** | PC | promote §11.4 Yield/Disengage into `combat_engine_v1/` | — |
| 10 | **U5 / R-07** | IN | `stance_delta`; `Person.stance` written; `stance.moved` | — |
| 11 | **U6** | IN | the first R-01/R-02 measurement | — |
| 12 | **H-62-rest** | IN | writers for `scar`, `axis_count`, `convictions` | — |
| 13 | **W28-cast** | IN | author the `cast:` blocks (**0 of 143 today**) and their reader, same commit | — |
| 14 | **U7-own** | IN | the eight `own`-eligibility verbs, in antonym pairs; distinct operands; `Candidate.why` | — |
| 15 | **Record-kind fold** | IN | Petition/Dispensation become kinds of `Record`; then `petition` + `carry` | — |
| 16 | **H-84** | IN | one verb that moves a Record to another person | — |
| 17 | **U8 / R-06b** | IN | `ambitions(p)`, `build_at` from the cast | — |
| 18 | **PROC-A** | SC | re-host the stress suite (its tracer is **gone**); `judging_set`; `arrangements.yaml` | — |
| 19 | **U7-remit** | IN | `levy`, `establish`, `open_case`, `determine`, `issue` | — |
| 19b | **U7-disp** | IN | `comply`, `evade / defy`, `refract` | **ED-IN-0210** |
| 20 | **U9 / R-04** | IN | faction-scale queries; 44 re-scales; the 10 world cases | — |
| 21 | **U10** | IN | the second measurement; `measured:` from instrument output only | — |
| 22 | **PROC-B** | SC | the proceedings provider; the composed obstacle with a ceiling; THE BAR | — |
| 23 | **PART-E-0/2** | IN | typed ids with an owned `H`; the ONE loader's remaining invariants | — |
| 24 | **SE-BUILD** | SE | settlements P1–P4 | **ED-SE-0051** + acceptance |
| 25 | **MB-GOLDEN** | MB | apply the golden-mode ruling; fix three flags whose defaults contradict their comments | **ED-MB-0061/0016** |
| 26 | **GO-VERSION** | GO | record the ruled version; ED-1050's deferred re-export; then held H6 | **the Godot version** |
| 27 | **WR-SCOPE** | WR | build or retire threadwork | **ED-WR-0010** |

**Parked, with reasons (not positions):** VOCAB-BALLOT — its output is a document (§0.2), and three
of its four contested rows are settled by positions 5 and 8; rebuild it after those land.
PHIL-DEBT — the as-structure row owed at `canon/philosophy/00_standing.md:78`; content authoring,
blocks nothing. OLD-DRIVER — **drop** (§0.1 pt 5: its artifact is load-bearing only on this
repository's process, so *"accept the defect and write nothing"*). PC-COMBATPOOL — demoted to a
record defect: the code already has one owner at `combat_engine_v1/core.py:48-51`; two of the three
"definitions" are prose that dies at position 2. CANDIDATE-WHY — rides at 14.
`ED-MB-0044/0056/0057` — a hand pass, not a position.

**Record defects, which ride along with whatever position touches them and are never scheduled:**
`H-46` still `absent` after U3 landed · the `workplan_v6_progress.yaml` / `CLAUDE.md` §0,§9 /
`m1_acceptance.py` binding to the retired M1 board · `HANDOFF_META_ARCHITECTURE.md:3` reading
PROPOSED under a RATIFIED directory · `HANDOFF.md:463-469` naming S7 as *"THE STEP TO TAKE"* ·
the spine's spent §0 table · `ED-MB-0016`'s file cites pointing at paths the 08-24 port deleted ·
`ED-IN-0210` reading `status: ruled` while carrying an open fork.

---

## 4. PARALLEL LANES — named as a departure, because a spine was asked for

The existing spine serialises deliberately. These pairs are genuinely order-free; one order is still
picked, and the cost of serialising is stated rather than hidden.

| order-free pair | why | order picked, and why |
|---|---|---|
| 1 ∥ 3–7 | ledger JSONL vs `engine/season/state` — no shared file | 1 first: one session, and it makes §5 readable |
| 2 ∥ 3–7 | `systems/`, registries, `tests/valoria` vs `engine/season/{state,loop}`; the only shared file is `seam/wrappers/sigma.py`, which no G-unit touches | 2 first: ruled and unexecuted for five days |
| 4 ∥ 5–7 | the spine says so (`:61`) | 4 first, so its hash move rides G1a's |
| 8, 9 ∥ 3–7 | wrappers hold no token (`04:164`); `combat_engine_v1` is outside `04`'s scope | after G4, so their Events land once on the finished contract |
| 12 ∥ 13 ∥ 14 | disjoint but for `verb_table.yaml` (12 and 14 both edit it) | 12 → 13 → 14; 12 first because 14's contested closers reuse its degree-keyed rows |
| 18 ∥ 13–17 | `world_q.judging_set`, `arrangements.yaml`, the stress re-host touch none of their files | 18 immediately before 19, which consumes it |
| 23 ∥ 22 | ids/loader vs seam provider | 22 first: game before contract |

If any pair is actually run concurrently, use `isolation: worktree` (`CLAUDE.md` §10).

---

## 5. THE RULING BATCH — what actually needs Jordan

Ten items, ordered by what each unblocks. Each is answerable without reading a plan.

1. **ED-IN-0214 — the conviction matrix.** Nine of thirteen convictions point within 60° of one mean
   vector, so convictions differentiate a person's own options well and *different people* badly.
   Re-centring overwrites 52 cells that `conviction_axis_matrix_v30.md` §3 argues individually.
   **Re-centre, or keep the authored matrix?** Answer before position 11 — a later *yes* invalidates
   U6's number.
2. **ED-IN-0210's fork — is `comply` one verb or two?** Does an `issue`d dispensation and a
   `dispatch`ed order get answered by the same `comply`/`evade`/`refract` keyed on the ledger claim
   **(A)**, or does `dispatch` need its own obey/disobey pair **(B)**? Evidence leans A. Unblocks 19b.
3. **ED-SE-0051 + the settlements set.** (i) Bound the demographic loop by **matter only (A)** or
   **matter plus a hearth-capacity table per site kind (B)**? (ii) Accept P1, P3, P4 for build as
   proposed? Unblocks 24; P4 is `F.20`, which `04:61` says blocks the build outright.
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

---

## 6. WHAT THIS SEQUENCE DOES NOT COVER

- `[GAP: PART E step 12 (parallel DELIBERATE map) and D-41a's permutation falsifier — beside the critical path; no R-row moves on them]`
- `[GAP: the FA lane beyond OLD-DRIVER — superseded at step B; its subject is expressed by position 20's faction queries, not by systems/factions/]`
- `[GAP: proceedings PHASE 1/3/4 — position 22 covers the provider critical path only]`
- `[GAP: any GDScript grade — every compliance clause here is the Python grade; `04 §0:88-92` requires both where they differ, and no position targets GDScript before 26]`
- `[GAP: the 143-case count — results.json gives 46 NPC + 97 ARC, but a grep over cases/ finds 100 `id:` lines and chain/*.yaml does not parse with plain PyYAML. Position 13 must use the harness loader's count, not either of these]`
- `[GAP: tools/m1_acceptance.py rows 1 and 4 — a Layer-0 board reader; §0.1 pt 5 forbids re-tooling it, and the CLAUDE.md sentence binding to it rides at position 1]`
- `[GAP: 2026-08-15-character-and-faction-stats-and-progression.md — ownership UNRESOLVED since PR #370 closed unmerged; §5 item 7 is the only live question in it]`

---

## 7. HELD BACK FROM RATIFICATION-ON-MERGE (`CLAUDE.md` §2, ED-1094)

Merging this PR ratifies **the order in §3 and the supersession verdict in §1**. Four things are
explicitly held back and must not be read as ratified by the merge:

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

**Five agent claims overturned by the author against the tree**, recorded so they are not re-derived:
the `## Status: PROPOSED` count (**200 repo-wide / 162 in scope**, not 129, 133 or 168 — the regex
must tolerate bold); the spine's **33** `.write(` sites (an `ast` walk gives **42**, twenty of them in
`harness/probes.py`); ED-SC-0033's **47** files under `systems/social_contest/` (**46** today);
`H-83`'s *"no reader"* (`stratum_of` is live at `loop/resolve.py:588`, called from `:373`); and
`ED-IN-0208`'s headline (§2.3).
