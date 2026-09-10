# Unblocking strategy — everything category D calls a blocking ruling

## Status: PROPOSED

**Lane:** IN · **Author:** session of 2026-09-10 · **Governs:** nothing. Reference under `CLAUDE.md` §0.05.
**Supersedes:** nothing. **Record:** `ED-IN-0207`. **Cites:** `ED-IN-0204` (ratified 2026-09-05), `ED-1094`, `workplans/return_to_game_queue.yaml` §S8.

---

## §0 · Verdict

**Almost nothing is blocked on Jordan, and the queue that looks like the blockage is not connected to the
game.**

Three measurements, each reproducible from the command given:

1. **Of the 151 `needs_jordan` rows, not one is cited by any instrument that measures the game.**
   `engine/season/requirements.yaml`, `engine/season/hole_register.yaml` and
   `workplans/2026-09-09-r-execution-plan.md` cite seven ED ids between them — `ED-061`, `ED-IN-0185`,
   `ED-IN-0202`, `ED-IN-0203`, `ED-IN-0204`, `ED-IN-0205`, `ED-MB-0066`, `ED-SC-0033` — and **every one
   carries `needs_jordan: false`.**
2. **Of the six holes the NINE block on — `H-62`, `H-65`, `H-94`, `H-98`, `H-111`, `H-116` — exactly one
   is a question only Jordan can answer, and its own row says it unblocks nothing.** Two are graded
   `assumption` (a default is already taken), one is graded `measured`, and the two remaining `absent`
   rows each record a Jordan ruling *already given* that converted them from rulings into build work.
3. **`register.py --check` fails on `G6` for fifteen rows: `absent` holes on which §0's five tests were
   never run.** That is not a queue of Jordan's decisions. It is a queue of work nobody did.

The strategic consequence: **stop treating the `needs_jordan` ledger as the blockage.** It is stock —
151 rows, 72% of them filed in a single month (2026-07), none filed since 2026-08-17, and none reaching
the game. The blockage that matters is a different register with a different shape, and the instrument
that measures it already exists and already names its own failures.

---

## §1 · The measurement

Every number below re-derives from the tree at `916a0be`. Where a count differs from a count previously
recorded in the tree, the difference is stated rather than smoothed.

### 1.1 The ED queue

    registers/editorial_ledger*.jsonl        14 files · 1,256 rows · 1,240 distinct ids

An id's effective state is its **last** row, because the ledgers are append-only. By that reading:

| | count |
|---|---|
| distinct ids carrying `needs_jordan: true` | **151** |
| of those, `status: open` | 105 |
| of those, **terminal status yet still flagged** | **46** |
| raw `needs_jordan: true` rows (not last-per-id) | 153 |

**Filing dates: 2026-06 → 14 · 2026-07 → 108 · 2026-08 → 29 · 2026-09 → 0.**
Nothing has been added to this queue in twenty-four days, and 72% of it was filed in one month.

`return_to_game_queue.yaml` §S8 measured 109 open on 2026-08-19 against 105 today, and 48 terminal-flagged
against 46. **Its measurement reproduces.** Its four bulk predicates re-run today yield A=37, C=23, B=5,
residue=40 over the open set — predicate A has grown from ~10 to 37 because rulings landed in the
intervening three weeks and nobody swept them back. That growth is the whole diagnosis in one number.

### 1.2 The hole register

    python -m engine.season.harness.register --counts

    113 rows · absent 34 · assumption 45 · measured 16 · ruled 18
    tier 0: 44   tier 1: 69
    `absent` rows with no `cite:` (G6's floor): 15
    ARTIFACT 0 -- UNMET, on H-101, H-105, H-108, H-43, H-46, H-49, H-62, H-71, H-84, H-98

    python -m engine.season.harness.register --check

    R2: 6 violation(s)      G6: 15 violation(s)      R0 R1 R3 G8 G12 G13: ok

**Zero of the 34 `absent` rows carries a usable `default:`, and zero names a `site:`.** An `absent` hole
is therefore not "a decision awaiting an answer" — it is a place where the design has no value *and* no
declared point of entry for one. And **the `owner:` column almost never says Jordan.** It says *the
resolver (Part E)*, *the design (a static registry)*, *unassigned*, or a module path. One row —
`H-101` — names Jordan in its `unblocks:` text.

### 1.3 The control, and the falsifier

A zero result is worthless without a control. The three game-measuring surfaces **do** cite EDs (§0 item 1
lists them), so "zero `needs_jordan` ids" is a measurement, not an artifact of citation-free files.

**Falsifier:** if any ED cited by `requirements.yaml`, `hole_register.yaml` or the R-execution plan were
`needs_jordan: true`, §0 item 1 would be false. Checked, one id at a time: all eight are `false`.

---

## §2 · The two queues, and why only one of them is the blockage

| | **Queue A — the ED ledger** | **Queue B — the hole register** |
|---|---|---|
| size | 151 rows | 34 `absent` + 45 `assumption` |
| what a row is | a question filed by a past session | a place the design has no value |
| read by code? | no — prose fields in JSONL | **yes** — `engine/season/harness/register.py` |
| cited by the NINE? | **never** | `blocks:` names six of them |
| what closing a row changes | a flag | `--check`'s output, and a verb's resolvability |
| §0.2 grade | bookkeeping | execution-bound |

Queue A is not worthless — it holds a genuine escalation channel and about twenty live design questions.
But it is **stock with no flow**: nothing has entered it since 2026-08-17, and nothing in it reaches the
season loop. Draining it buys a shorter list and Jordan's attention back. It does not move R-01..R-09.

Queue B is where the game is blocked, and it is where §0's five-test ladder was **never run** — G6 says so
by name, on fifteen rows, in the output of a command.

---

## §3 · Four corrections to the category-D listing I gave you

Three of the four "live blockers" I named do not survive contact with the tree.

**(1) The undeclared content-hash tiebreak is NOT a ruling, and the tree already said so.**
`engine/season/requirements.yaml`'s `R-08` carries a `disposition:` field, landed by **PR #384**
(`cb28ec9`) — a session other than this one — which reads, verbatim:

> ⚠ AN EARLIER DRAFT OF THIS ROW FLAGGED `needs_jordan: true` AND WAS WRONG TWICE … (1) It described the
> CANDIDATE tie as broken by "an undeclared content-hash tiebreak". It is not; it is alphabetical …
> (2) That question tiebreak is ALREADY DISPOSED … recorded closing at §0 step 4 on `H-54`'s precedent with
> `needs_jordan` FALSE. Re-surfacing it as open is the ED-IN-0185 failure CLAUDE.md §0's five tests exist to
> prevent … **What remains open here is not a ruling but BUILD WORK: W26 and `H-62`.**

I re-surfaced it anyway. **G1 is not waiting on a ruling.** Whether `§F1` clause 4's corpus firing is a
property or an accident is a question §0 test 5 answers — it has an obvious engineering answer (a
demonstration that depends on which act a tiebreak happened to select is not a demonstration) and it
should be taken, not escalated.

**(2) `H-111` is real and blocks nothing.** Its own `unblocks:` field: *"nothing — it is a question about
what the world SHOULD do, and both answers run."* Correctly listed, correctly inert.

**(3) The `systems/social_contest/` retirement wave is not blocked — it is ruled and unexecuted.**
`CURRENT.md`: *"orphaned social contest code: retire it"*, ruled 2026-09-06, measured at 47 files / 1.2 MB
/ 20+ inbound sites, *"ruled and NOT executed"*. That belongs under execution, not under rulings.

**(4) `ED-1051`'s own numbers are two-thirds stale, and the board already knows the work is not blocked.**
Re-measured today against `references/module_contracts.yaml`:

| | ED-1051 (2026-07-02 addendum) | today |
|---|---|---|
| `doc: null` modules | 11 / 27 | **9 / 27** |
| `[ASSUMPTION]`-grade resolvers | 13 / 27 | **1 / 27** |

And `workplan_v6_progress.yaml:85`, on the row `ED-1051` supposedly gates: *"ED-1051 … gates only
RATIFICATION of the engine_clock contract, which is why `blocked_on` is null: **the work is not blocked,
the paperwork is.**"*

---

## §4 · The strategy — six moves, ordered by unblocking power

### M1 · Run §0's five-test ladder on the hole register's fifteen G6 rows

**Why first:** it is the only move on this list whose completion is observable by running a command, it is
the exact work `CLAUDE.md` §0 describes, and `PLAN.md` §2.6 already found that *nobody ever ran that
ladder*. Fifteen rows, each graded `absent` with an empty `cite:` — H-41, H-43, H-44, H-45, H-47, H-48,
H-49, H-50, H-51, H-52, H-56, H-57, H-58, H-59, H-61. Two are Tier 0 (H-43, H-49), and **H-43's own text
says it is partly discharged and stale.**

**Method, per row:** run tests 1→5 in order; write the answer and its citation into `cite:`; re-grade only
if the ladder produced a value. A row that survives all five stays `absent` and **acquires a `cite:` saying
which of the five it survived** — which is itself the discharge of G6, because G6 asks that the ladder was
run, not that it succeeded.

**Observable:** `register.py --check` prints `G6: ok`, or prints a smaller violation list with the
remainder named. **Falsifier:** a row whose `cite:` does not name a successor, a document, a precedent or an
architectural reason has not had the ladder run on it, and the check should keep failing.

**Do not** re-grade a row to `ruled` on the strength of prose. §0.05: the grade `ruled` means a decision
exists; it does not mean the code carries it.

### M2 · Re-measure every named blocker before treating it as one

`ED-1051` lost twelve of its thirteen `[ASSUMPTION]` resolvers without anyone noticing, and `H-94` records
its own closure inside a row still graded `assumption` and still named in `R-05`'s `blocks:`. **A blocker
older than a month is a hypothesis, not a fact.**

**Method:** for each item in `blocks:` across `requirements.yaml`, and for each `absent` hole carrying a
`cite:`, re-run the row's own measurement command and compare. Where the row carries no command, that is
the finding.

**Observable:** a diff on `requirements.yaml`/`hole_register.yaml` in which `blocks:` shrinks. **Cost:** low.
**This is the highest ratio of unblocking to effort on the list**, because three of the six holes blocking
the NINE are already answered inside their own rows.

### M3 · Execute what is ruled and unexecuted

Ruling without execution is the repository's characteristic failure, and `ED-1094` already says the flip
belongs *"in that same merge, not as a later step nobody triggers."* Standing instances:

- the `systems/social_contest/` retirement wave (ruled 2026-09-06; 47 files; cross-lane);
- `ED-IN-0204`'s consequence for the FA/SE/WR design surfaces (§5 class 4);
- the `engine_clock` emitter at `workplan_v6_progress.yaml:85`, which *"needs no ruling"*.

### M4 · Drain the ED queue by class, never by grep alone

Six classes, §5. The rule that keeps this safe is `S8`'s and it is not negotiable: **the predicates find
candidates; a human-readable one-line citation closes a row.** No row closes without naming its successor,
its retired subject, its governing document, its precedent, or its architectural reason.

### M5 · Put the residue to Jordan on one sheet

§6. Ranked by what answering buys, with a recommendation on every line, so the whole thing is answerable in
one sitting rather than accreting for another two months.

### M6 · Close the channel that refilled it

The queue did not form because sessions were lazy; it formed because **filing was free and closing was
nobody's job.** Two changes, both already licensed and neither requiring new machinery:

- **`ED-1094` at merge time.** A PR that lands a `PROPOSED` item flips the flag in the same merge. This is
  already the rule; it is simply not followed.
- **§0's gate before filing.** A row may be filed `needs_jordan: true` only after tests 1–5 have been tried
  and the attempt is recorded in the row. A row that does not say which of the five it survived is not an
  escalation; it is a note.

⚠ **Do not build a guard for this.** §0.1 pt 5's predicate: a guard is earned only where the defective
artifact is load-bearing on the game or on a Jordan decision. The `needs_jordan` queue qualifies — but the
guard that would enforce M6 is a guard over ledger prose, which is the generator §0.3 names. **The
enforcement is `ED-1094` at merge, applied by whoever merges.**

---

## §5 · Queue A, partitioned — six classes, first match wins

The partition is exhaustive and sums to 151.

| class | n | the test that closes it (`CLAUDE.md` §0) | what a closure must cite |
|---|---|---|---|
| **1 · escalate** | **23** | survives all five | — see §6 |
| **2 · terminal flag** | **39** | the row's own last status is `resolved`/`ratified`/`executed` | the row's own status + the PR that landed it |
| **3 · authorial** | **11** | none — genuinely Jordan's, and blocking nothing | reclassify, do not close |
| **4 · superseded by ED-IN-0204** | **39** | test 1 — the target subsystem was not retained | `ED-IN-0204`, 2026-09-05 |
| **5 · subject retired** | **10** | test 2 — every cited path has left `main` | the `FORK:` row, via `pathres` |
| **6 · hand pass** | **29** | unknown until read | per row |

### Class 2 — terminal flag (39)

Forty-six ids carry the flag on a terminal row; three (`ED-MB-0039`, `ED-MB-0040`, `ED-MB-0041`) hold a live
FORK in `needs_jordan_detail` and four more hold one in prose, so those go to class 1. The remaining 39 break down **MB 15 · PC 15 · IN 9**: the thirty mass-battle and personal-combat rows quote a Jordan
directive verbatim and record the code that executed it; the nine `ED-IN-*` rows are completed audits and
programmes (`ED-IN-0183`, `ED-IN-0184`, `ED-IN-0187`). **The flag is residue from filing, not a pending question.**

⚠ **Two of the 46 are traps and must be read, not swept:** `ED-IN-0127` says *"needs_jordan TRUE for its
per-directory table only … vetoable row by row"*, and `ED-MB-0045` is a six-lens audit whose findings need
rulings. Both are in class 1.

### Class 4 — superseded by ED-IN-0204 (39)

Jordan, 2026-09-05, verbatim: *"This is now the new system with **only the repository's systems for social
contests, personal combat and mass battles to be retained.** All work in /engine is retained as well at this
moment."*

Twenty-three of these 39 are a single batch filed 2026-07-09 from one historical-precedent research pass —
`ED-FA-0018`, `ED-FA-0027`–`0034` and `ED-SE-0031`–`0044`, each of the form *"mechanism X, grounded in Y. Target: the
faction/settlement layer."* **The layer they target was not retained.** The question as posed is therefore
unanswerable, which is test 2 exactly.

**What dies is the row, not the idea.** The honest closure text is: *"Closed — the target design surface was
not retained (ED-IN-0204, 2026-09-05). The mechanic, if wanted, re-enters as a verb against
`engine/season/verb_table.yaml`."* Note the asymmetry the closure must respect: `engine/season/` runs the
settlement scale today; **it does not run the faction scale** — `R-04` measures 44 of 143 cases
unrepresentable at faction scale. So an SE mechanic has a door to walk back through and an FA mechanic does
not, yet.

### Class 5 — subject retired (10), and the caveat that governs classes 4 and 5 both

`tools/pathres.py` over the structural fields only (`source`, `canonical_source`, `citations`, `files`,
`artifacts`) — never over `description`, which yields nonsense — with a positive and a negative control run
first:

    ALL_FORKED 26 · ALL_DEAD 10 · HAS_LIVE 104 · NO_PATH 11

Thirty-six rows cite no live path. **At least three of the thirty-six are live questions anyway** —
`ED-IN-0147` (four held items) is cited by the M1 board, and `ED-SC-0005` and `ED-SE-0002` by the master
workplan, while the audit directory each names sits at a fork ref. **This is why the predicate may not
auto-close.** It says *"the paperwork behind this row left `main`"*, which is a reason to read the row, not
a reason to close it.

### Class 3 — authorial (11)

`ED-507`, `ED-508`, `ED-595`–`599`, `601`, `602`, `610`, `634`: NPC arc profiles, POI catalogues, Crown
inner-circle names. Several say *"Requires user approval"* outright. These are Jordan's, they are not
questions, and **they belong to content authoring that has not begun.** Reclassify them out of
`needs_jordan` — which `CLAUDE.md` §0 defines as *"Jordan is the only person who can answer this"* — and
into whatever the content lane calls its backlog. Closing them would be false; leaving them flagged makes
the queue look like a decision backlog when a seventh of it is a writing assignment.

### A worked example, because a method without one is an assertion

**`ED-SC-0005`** — *"cap the Recall/Corroborate/Prep/Findings bonus-die stack; the cap value is Jordan's
design number"* — is one of three rulings `workplan_v6_progress.yaml:60` calls a **HARD** block on SC
Stage 4.

Test 3 (answered by a design document) and test 5 (answered by the architecture), run against the code:

- `systems/social_contest/sim/contest/armature.py:62` — *"Face, corroboration, prep, commit-spend) accumulate
  as **δσ, tanh soft-capped**, uniform probability impact"*;
- `resolver.py:7` and `primitives.py:293` — corroboration carries **diminishing returns**;
- `engine/autoload/sigma_leverage.py:104` — `M_MAX = 1.5`; `:141` — `soft_cap(net) = M_MAX·tanh(net/M_MAX)`.

**The four channels are implemented, and they are not dice.** The +ND stack the row asks Jordan to cap does
not exist in the kernel; the quantity those channels feed is capped by a saturating function that is already
in the engine and already cited to `modifier_system_spec.md §3.1`. The row is closable on test 2 — its
subject was never built and the ruled model (`ED-IN-0187`: *"d10 always using fractional dice and fractional
obstacles, sigma leveraged"*) does not contain a die-count channel to cap.

⚠ **And the board's own hedge reached the right answer by the wrong argument.** `:61` says to read
`ED-SC-0017` because *"it argues the cap is ALREADY ruled … kernel M_MAX=1.5 tanh"*. A bonus-die count and a
σ soft cap are **different quantities** — treating `M_MAX` as the answer to *"how many bonus dice"* is the
methodology inconsistency `§0.06`'s S criterion names. The row closes because **the channel is σ, not
because 1.5 is the cap.**

**One of SC Stage 4's three hard blockers is not a ruling.** `ED-SC-0003` is a second candidate: the
collision it describes does not reproduce in `systems/overview/reference/clock_registry_v30.md`, which
carries *Piety Track (PT), 0–5, per territory* at `:60` and *Persuasion Track, 0–10, per contest* at `:87` —
two names, two referents, no collision — while the third surface it cites, `params/bg/core.md`, is `FORKED`.
**`ED-SC-0004` is real** and stays on the sheet: two contradictory implementations are simultaneously live
and the floor moves 1 → 5, which erases a measured regime. That is two defensible options leading to
materially different games.

---

## §6 · The decision sheet — what genuinely needs Jordan, ranked by what answering buys

Twenty-three rows reach class 1. They collapse to **eleven questions**, because the seven-item
`jordan_docket` in `return_to_game_queue.yaml` already absorbed several of them and each carries a
recommendation.

| # | question | home | recommendation | what answering unblocks |
|---|---|---|---|---|
| **1** | **Which Godot version does the port target?** | `CLAUDE.md` head | none — this cannot be settled by any document, by rule | **the entire GO lane and the compile ratchet.** `project.godot` and the game repo's CI pin one version; `godot/` documents another; a binary of the wrong version mis-counts the ratchet |
| **2** | Ratify **CIP-1, the Record spine**, with CIP-9b as its rider? | `ED-SC-0023`/`0026`/`0024`, docket **D5** | **(a) ratify** | the largest single drain: *"needs no new primitive, no new number and no sweep"*; one yes moves the whole SC C-cluster into scheduled work |
| **3** | Does metaphysical canon (P-01..P-15) outrank measured behaviour, or split? | `ED-IN-0113` §A, docket **D1** | **(c) split** — constraints supreme, numbers subordinate | **the multiplier.** It converts every future queue item into a self-executing default instead of a fresh question |
| **4** | The kernel's canonical **Argue-pool formula** | `ED-SC-0004` | none — genuinely two games | SC Stage 4, P4 calibration, `ED-IN-0013`'s re-verdict, and any Godot export of the contest |
| **5** | Is the tenth attribute **Recall**, and are the Spirit/Will and Cognition/Acuity folds inverted? | `references/descriptor_registry.yaml:39-59`, docket **D2** | **(a) yes to both** | descriptor binding into Godot. (a) is a registry-only edit; (c) is a breaking rename across 13 `.gd` + 22 `.tres` + 19 `.py` |
| **6** | After F1–F8, **which flag configuration defines the mass-battle golden**? | `ED-MB-0061`, docket **D4** | **(a) all-ON single global re-base** | MB has had no trustworthy baseline since 2026-07-30. Also resolves `ED-MB-0016`'s friction flip |
| **7** | **J2** — re-issue, withdraw or scope which mass-battle tree is canon? | `ED-MB-0065`, docket **D3** | **(a) withdraw** — the 2026-08-04 keep-set already kept the tree | ends a record that asserts a deletion which never happened |
| **8** | The three MB **Tier-3 design calls** — depth, envelopment, cavalry, Command, rout band, yield | `ED-MB-0039`/`0040`/`0041` | (B) staged behind a flag for envelopment; the rest are a calibration pass with bands fixed | MB historical fidelity; each is explicitly *"not executed unilaterally"* |
| **9** | Ratify `combat_reference_v1.md`; promote **Surrender/Disengage** into `combat_engine_v1/`? | `ED-PC-0056` | (a) ratify; (b) promote — it is live spec with no implementation | PC lane's head |
| **10** | `ED-IN-0147`'s four held items — **SS5-SS7 disposition · Crown Mil 4.0 vs 5.0 · the PP citation universe · MB J2** | `ED-IN-0147` | H2 is not a judgment call: `ED-809` settled it at 5.0 and the code contradicts it | 327 citations across 176 files (H1); an anti-fabrication gate that half-exists (H3) |
| **11** | Adopt the **doctrine amendments** to `CLAUDE.md` §0/§0.1, and keep or end structurally independent adversarial review? | docket **D6**/**D7** | keep adversarial review — the record shows critics overturning committed claims repeatedly, including twice in this session | the only items that reduce **generation** rather than stock |

**Blocking nothing, answer at leisure:** `H-111` (does a refusal propagate as news — *"both answers run"*),
the eleven authorial rows of class 3, `ED-IN-0148`(b) and `ED-IN-0149`'s nine Tier-3 items.

---

## §7 · What this strategy does not license

- **No new tool, no new guard, no new registry, and nothing added to `audit/`.** §0.1 pt 5's predicate
  forbids a guard whose subject is another guard, and §0 retires `audit/` as a category. Every instrument
  this strategy needs — `register.py --check`, `pathres.py`, `validate_ed_citations.py`,
  `m1_acceptance.py` — already exists.
- **No auto-close.** `S8`'s rule stands: *"the greps must never auto-close anything above bucket C."*
  A predicate nominates; a citation closes.
- **No re-grading a hole to `ruled` on prose.** §0.05: a `## Status:` line is not a mechanism.
- **No new `needs_jordan` rows out of this work.** §0 caps the adversarial pass at *"at most one ledger row,
  and only if that row requires a human decision"*. A finding that needs no ruling is fixed in the commit
  or dropped.
- **No document may be the deliverable of a move.** §0.2: a juncture is done when the behaviour executes.
  For M1 the executing thing is `register.py --check`; for M3 it is the retirement actually running.

---

## §8 · Sequencing and tiering

| order | move | tier (`CLAUDE.md` §10) | effort | why that tier |
|---|---|---|---|---|
| 1 | **M2** re-measure the blockers | `haiku` finders → `sonnet` verify | `low`/`medium` | re-running a row's own command is deterministic extraction |
| 2 | **M1** the five-test ladder ×15 | `sonnet` per row, `opus` on Tier-0 rows and on any row reaching test 5 | `high` | tests 1–4 are lookup; test 5 is a judgment that gates a result |
| 3 | **M4** classes 2, 4, 5 | `haiku` to nominate, `sonnet` to cite, `opus` on the seven traps | `medium` | the closure text is the deliverable, not the predicate |
| 4 | **M3** execute the ruled | `sonnet`, `isolation: worktree` for the retirement wave | `high` | 47 files, 20+ inbound sites, several read by blocking gates |
| 5 | **M5** the sheet | `opus` | `max` | this is the artifact Jordan reads |
| 6 | **M6** at merge | — | — | a habit, not a task |

**Adversarial pass:** M1 and M4 are exactly the shape where a producer marks its own homework. Dispatch
`subagent_type: "valoria-critic"` with the *closure citations only* — never the reasoning that produced
them — and have it try to find the successor that does not say what the closure claims. That independence
is structural: the agent definition grants `Read, Grep, Glob` and nothing else.

**Do not fan out M1 in parallel across all fifteen rows.** Several share a subject (`H-47`, `H-48`, `H-50`
are all *"a 54 fold-in with no Part D row"*), and three independent answers to one question is how the
tree acquired two ladders for one quantity in the first place.

---

## §9 · Falsifiers

Each headline claim, and the observation that would kill it. Per §0.1 pt 3, a result with no named
falsifier has not been attacked.

| claim | falsifier |
|---|---|
| the ED queue reaches no game instrument | one ED cited by `requirements.yaml`, `hole_register.yaml` or the R-plan carrying `needs_jordan: true` — checked, all eight are `false` |
| one of six R-blocking holes is a genuine ruling | any of `H-62`, `H-65`, `H-94`, `H-98`, `H-116` whose row does not record an answer already given — read; each does |
| `ED-SC-0005` is closable | a live resolver that adds bonus **dice** as a count to a contest pool — searched `systems/` and `engine/`; the channels resolve as δσ under `soft_cap` |
| `ED-1051`'s numbers are stale | `module_contracts.yaml` showing 11 `doc:null` / 13 `[ASSUMPTION]` — measured 9 and 1 |
| the class partition is exhaustive | the six classes summing to anything but 151 |
| class 5's predicate is safe to run alone | a row citing only dead paths that is nonetheless live — **three found** (`ED-IN-0147`, `ED-SC-0005`, `ED-SE-0002`), which is why the predicate only nominates |

**What this strategy does not know.** `H-43`'s row says it is *partly discharged and stale*; the extent is
unmeasured here. Twenty of the 34 `absent` rows carry `unblocks: unmeasured`, so the ranking in §4 is
by *stated* consequence, not by measured consequence — M2 is what would replace that with a measurement.
The 29 rows in class 6 have not been read, and the estimate that most fall to tests 1–4 is an expectation,
not a finding.
