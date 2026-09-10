# Unblocking strategy — everything category D calls a blocking ruling

## Status: PROPOSED

**Lane:** IN · **Author:** session of 2026-09-10 · **Governs:** nothing. Reference under `CLAUDE.md` §0.05.
**Supersedes:** nothing. **Record:** `ED-IN-0208` — ⚠ **renumbered from `ED-IN-0207` at merge.** PR #390
took 0207 on `main` while this branch was open; per `CLAUDE.md` §4 the later-merging side renumbers, and
that is this one. **Cites:** `ED-IN-0204` (ratified 2026-09-05), `ED-1094`, `workplans/return_to_game_queue.yaml` §S8.

---

## §0 · Verdict

**Almost nothing is blocked on Jordan, and the queue that looks like the blockage is not connected to the
game.**

Three measurements, each reproducible from the command given:

1. **Of the 151 `needs_jordan` rows, not one is cited by any instrument that measures the game.**
   `engine/season/requirements.yaml`, `engine/season/hole_register.yaml` and
   `workplans/2026-09-09-r-execution-plan.md` cite **eight** ED ids between them — `ED-061`, `ED-IN-0185`,
   `ED-IN-0202`, `ED-IN-0203`, `ED-IN-0204`, `ED-IN-0205`, `ED-MB-0066`, `ED-SC-0033`. **Seven carry
   `needs_jordan: false`; `ED-061` carries no `needs_jordan` field at all** (`editorial_ledger_archive.jsonl`
   has none, across all 492 rows), so for that one the claim is *absence*, not a recorded `false`.
2. **Of the six *holes* the NINE block on — `H-62`, `H-65`, `H-94`, `H-98`, `H-111`, `H-116` — exactly one
   is a question only Jordan can answer, and its own row says it unblocks nothing.** Two are graded
   `assumption` (a default is already taken), one `measured`; `H-98` records a Jordan ruling *already given*
   (2026-09-03, executed by `W-E` 2026-09-04) and `H-62` records a **shape supplied by a document**, #358
   rev.2 §C.4/§F.20a — and its own `cite:` still ends *"a human decides"*. Read `H-62` as build work on
   `requirements.yaml:277`'s authority, not on its own row's.
   ⚠ **This claim is scoped to holes and covers about half the blocker set.** `blocks:` also names eight
   W-items — `W-F`, `W10`, `W10-core`, `W13`, `W17`, `W23`, `W26`, `W27` — and this document does not say
   whether any of them needs a ruling. Do not read the headline as if it did.
3. **`register.py --check` fails on `G6` for fifteen rows.** That is not a queue of Jordan's decisions
   either — and, per `architecture/PLAN.md:689-694`, it is **not a queue to close by running the ladder**:
   *"closing them by ladder would be inventing closures for holes whose answer is a table nobody has built
   yet. **Each building item must set its rows' grades as it lands.**"* The fifteen are discharged by the
   items that build what they are missing, not by a pass over them.

The strategic consequence: **stop treating the `needs_jordan` ledger as the blockage.** It is mostly stock —
151 rows at `916a0be`, 72% of them filed in one month (2026-07) — and none of it reaches the game.
⚠ **It is not entirely stock:** merging `main` into this branch brought **two rows filed today**
(`ED-SE-0051`, `ED-WR-0010`, from PRs #391 and #388), taking the queue to **153 / 106 open**. Both are
genuine escalations that would survive §0's five tests, which is the flow working as intended — but the
draft's *"nothing has entered since 2026-08-17"* was true of `916a0be` and is **false of the merged
tree**, and is corrected here rather than left standing. But the corrected reading of item 3 also removes the obvious replacement: **the hole register is
not a queue to work either.** Its `absent` rows close when the thing they are missing gets built. So the
unblocking work is neither queue — it is **executing what is already ruled**, and **re-measuring the
blockers that are asserted rather than observed.** Those are §4's M1 and M2, in that order.

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
| of those, **not `open` yet still flagged** | **46** |
| — of which `resolved` / `ratified` / `executed` | 43 |
| — of which `partial` (2) or `proposed` (1) | 3 |
| raw `needs_jordan: true` rows (not last-per-id) | 153 |

⚠ **"Terminal" and "not `open`" are not the same set, and §5's class 2 uses the wider one.** Three rows —
`ED-IN-0059` (`proposed`), `ED-IN-0147` and `ED-IN-0149` (`partial`) — are neither open nor finished. The
two `partial` rows go to class 1; `ED-IN-0059` sits in class 2 and is the one row there whose status does
not by itself close it.

**Filing dates at `916a0be`: 2026-06 → 14 · 2026-07 → 108 · 2026-08 → 29 · 2026-09 → 0.**
72% of the queue was filed in one month. ⚠ **On the merged tree the last bucket is 2, not 0** —
`ED-SE-0051` and `ED-WR-0010`, both 2026-09-10, arriving with PRs #391 and #388 while this branch was
open; totals become **1,261 rows / 1,244 ids / 153 flagged / 106 open**. Both belong in class 1.

`return_to_game_queue.yaml` §S8 measured **109 open** on 2026-08-19 against **105** today; its open count
reproduces to within four rows. ⚠ **Its 48 does not "move" to 46 — the two numbers are different
computations.** S8 derived 48 as *raw hits − open* (157 − 109); the same computation today gives
**153 − 105 = 48**, unchanged. The 46 above is *distinct ids − open*. Nothing happened in the tree; the
instrument changed.

Its bulk predicates re-run over the open set yield **A=37 · C=23 · B=5 · residue=40**. ⚠ **Predicate E was
not re-run** — it needs an evacuation test S8 paired with a `params_tables.yaml` check, and dropping it
silently would have hidden that A, C and B alone already partition the 105. **Predicate A has grown from
~10 to 37**; the plain reading is that rulings landed in the intervening three weeks and nobody swept them
back, but C's 32 → 23 and B's 14 → 5 have no such story and this document does not supply one.

**Reproduce these with:** last-row-per-id over `registers/editorial_ledger*.jsonl`, reading each row's
`needs_jordan`, `status` and `date`. **Every count in this document is pinned at `916a0be`: 1,256 rows /
1,240 distinct ids / 151 flagged / 105 open.** On the merged tree — `main` at `461809d` plus this
session's own two rows — it is **1,261 / 1,244 / 153 / 106**. The partition in §5 is stated at the pin;
the two new rows are class 1 and take it to 25/153.

### 1.2 The hole register

    python -m engine.season.harness.register --counts

    113 rows · absent 34 · assumption 45 · measured 16 · ruled 18
    tier 0: 44   tier 1: 69
    `absent` rows with no `cite:` (G6's floor): 15
    ARTIFACT 0 -- UNMET, on H-101, H-105, H-108, H-43, H-46, H-49, H-62, H-71, H-84, H-98

    python -m engine.season.harness.register --check

    R2: 6 violation(s)      G6: 15 violation(s)      R0 R1 R3 G8 G12 G13: ok

⚠ **`G6` is a PRESENCE check, and `--check` is not a CI gate.** `register.py:240-243` fails a row only
when `cite:` is empty, so **any non-empty string turns it green**; `valoria-ci.yml:376` runs
`--requirements`, not `--check`; and the module's own docstring says it *"grades no repository signal …
and has no CI job."* Treat `G6: ok` as a filing check, never as evidence a hole was answered.

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
| read by code? | no — prose fields in JSONL | by the **grader**, not the loop — `register.py` |
| cited by the NINE? | **never** | `blocks:` names six of them |
| what closing a row changes | a flag | `--check`'s output — **and nothing else**, since every `absent` row has an empty `site:` |
| §0.2 grade | bookkeeping | ⚠ **also not execution-bound.** `CLAUDE.md` §3: `hole_register.yaml` is *"mechanism for the grader, reference for the game"* |

Queue A is not worthless — it holds a genuine escalation channel and about twenty live design questions.
It is **mostly stock**: two rows entered on 2026-09-10 and the twenty-four days before that saw none, and
nothing in it reaches the season loop. Draining it buys a shorter list and Jordan's attention back. It does not move R-01..R-09.

Queue B is where the game's *unanswered questions* are recorded. It is **not** a work queue either, and an
earlier draft of this document treated it as one. `architecture/PLAN.md:689-694` — Layer 1, and the item
that actually ran the ladder on `V2`'s twelve rows on 2026-09-02 — settles it: the twenty-two rows `W0`
added *"are discharged **by construction** at `W2`/`W3`/`W5` rather than by the five tests"*, and closing
them by ladder *"would be inventing closures for holes whose answer is a table nobody has built yet."*

**So neither queue is the work.** What is left, and what §4 is built on: **execute what is ruled**, and
**re-measure what is merely asserted to block.**

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
| `[ASSUMPTION]`-grade resolvers | 13 / 27 | **11 / 27** |

⚠ **CORRECTED.** An earlier draft of this row said **1 / 27**, and built a claim on it — *"ED-1051 lost
twelve of its thirteen `[ASSUMPTION]` resolvers without anyone noticing"*. That was a **measurement
defect, not a finding**: the grade is a YAML **comment** on each `resolver:` line, and a `yaml.safe_load`
strips comments, so the count saw only the one instance that sits in a *value*. Eleven module-level
`resolver:` lines carry `# [ASSUMPTION]`, and `workplan_v6_progress.yaml:53` says so in words — *"the
`[ASSUMPTION]` grade **11 of 27 resolvers already carry**"* — in a file this document had open.
**`ED-1051` is modestly stale, not two-thirds resolved.** The `doc: null` half stands.

And `workplan_v6_progress.yaml:85`, on the row `ED-1051` supposedly gates: *"ED-1051 … gates only
RATIFICATION of the engine_clock contract, which is why `blocked_on` is null: **the work is not blocked,
the paperwork is.**"* ⚠ **That is true of that row and false of the board as a whole:** the same file
carries `blocked_on: "ED-1051 + strategy-doc register"` at `:148`, *"G0.1 Key.gd v2 once ED-1051 ruled"*
at `:149`, and `ED-1051` in `decisions_t0_open:` at `:180`. **Gate-0 is blocked on it; the engine_clock
emitter is not.**

---

## §4 · The strategy — six moves, ordered by unblocking power

⚠ **This section was reordered after an adversarial pass.** The first draft ranked *"run §0's five-test
ladder over the hole register"* as move 1. `architecture/PLAN.md:689-694` forbids exactly that, and the
draft cited `PLAN.md` §2.6's *"nobody ever ran that ladder"* without reading `:664`, where **`W1` ran it
on 2026-09-02**. The move is gone, not demoted.

### M1 · Execute what is ruled and unexecuted

**Why first:** it is the only move on this list whose output is game code, and `ED-1094` already says the
flip belongs *"in that same merge, not as a later step nobody triggers."* `CLAUDE.md` §0.2 ranks it above
everything else here by construction — a juncture is done when the behaviour executes.

Standing instances:

- **the `systems/social_contest/` retirement wave** — ruled 2026-09-06, measured at 47 files / 1.2 MB /
  20+ inbound sites, several read by blocking gates. Cross-lane, `isolation: worktree`;
- **`ED-IN-0204`'s consequence for the FA/SE/WR design surfaces** (§5 class 4);
- **the `engine_clock` emitter** at `workplan_v6_progress.yaml:85`, which *"needs no ruling"* — the
  consumer is built and passing, only the emitter is missing.

**Observable:** the files are gone, or the emitter fires and a test observes it. Not a document.

### M2 · Re-measure every named blocker before treating it as one

`H-94` records its own closure (`W-C`, 2026-09-04) inside a row still graded `assumption` and still named
in `R-05`'s `blocks:`. `ED-1051`'s `doc: null` count moved 11 → 9 unremarked. **A blocker older than a
month is a hypothesis, not a fact** — and, as §3(4) shows, a re-measurement is itself a place to be wrong,
so each one carries the command that produced it.

**Method:** for each entry in `blocks:` across `requirements.yaml`, re-run the row's own `measure:` command
and compare. Where a row carries no command, that is the finding. **This includes the eight W-items**,
which §0 item 2 deliberately does not speak for.

**Observable:** a diff in which `blocks:` shrinks. **Cost: low. Highest ratio of unblocking to effort on
the list.**

### M3 · Let each building item set its own rows' grades

The fifteen `G6` rows are **not** a work queue. `PLAN.md:689-694`: they *"are discharged by construction at
`W2`/`W3`/`W5`"*, and *"each building item must set its rows' grades as it lands."* The strategy for them
is therefore a **discipline attached to other work**, not a pass: when `W2`, `W3`, `W5` or any successor
lands, it re-grades the rows it answered and writes the citation.

⚠ **Do not "close" a `G6` row to make `--check` green.** `G6` fails only on an *empty* `cite:`
(`register.py:240-243`), so any string satisfies it, and `--check` is not a CI gate. That is precisely the
*satisfiable-by-writing* failure `CLAUDE.md` §0.2 exists to exclude.

### M4 · Drain the ED queue by class, never by grep alone

Six classes, §5. `S8`'s rule is not negotiable: **the predicates find candidates; a human-readable one-line
citation closes a row.** No row closes without naming its successor, its retired subject, its governing
document, its precedent, or its architectural reason. §5's worked example is the standing evidence for why:
two rows this document proposed to close both survived the attack.

### M5 · Put the residue to Jordan

§6 **is** that artifact — it exists already, in this document. There is no further deliverable; the move is
Jordan reading it and answering. Ranked last because it unblocks Jordan's queue, not the game — which is
`S8`'s own reasoning for placing the amnesty sweep last.

### M6 · Close the channel that refilled it

The queue did not form because sessions were lazy; it formed because **filing was free and closing was
nobody's job.** Two changes, neither requiring new machinery:

- **`ED-1094` at merge time.** A PR that lands a `PROPOSED` item flips the flag in the same merge. This is
  already the rule; it is simply not followed.
- **§0's gate before filing.** A row may be filed `needs_jordan: true` only after tests 1–5 have been tried
  and the attempt is recorded in the row.

⚠ **Do not build a guard for this.** §0.1 pt 5's predicate: a guard is earned only where the defective
artifact is load-bearing on the game or on a Jordan decision. The `needs_jordan` queue qualifies — but a
guard over *ledger prose* is the generator §0.3 names. **The enforcement is `ED-1094`, applied by whoever
merges.**

---

## §5 · Queue A, partitioned — six classes, first match wins

The partition is exhaustive and sums to 151.

| class | n | the test that closes it (`CLAUDE.md` §0) | what a closure must cite |
|---|---|---|---|
| **1 · escalate** | **23** | survives all five | — see §6 |
| **2 · terminal flag** | **39** | the row's own last status is `resolved`/`ratified`/`executed` | the row's own status + the PR that landed it |
| **3 · authorial** | **11** | none — genuinely Jordan's, and blocking nothing | reclassify, do not close |
| **4 · superseded by ED-IN-0204** | **39** | test 1 — the target subsystem was not retained | `ED-IN-0204`, 2026-09-05 |
| **5 · subject retired** | **10** | test 2 — every cited path has left `main` | the `FORK:` row, or the absent target, via `pathres` |
| **6 · hand pass** | **29** | unknown until read | per row |

### Class 2 — not `open`, yet still flagged (39)

Forty-six ids carry the flag on a row that is not `open`; three (`ED-MB-0039`, `ED-MB-0040`, `ED-MB-0041`)
hold a live FORK in `needs_jordan_detail` and four more hold one in prose (`ED-IN-0127`, `ED-IN-0147`,
`ED-IN-0149`, `ED-MB-0045`), so those seven go to class 1. **The remaining 39 break down MB 15 · PC 15 ·
IN 9**: the thirty mass-battle and personal-combat rows quote a Jordan directive verbatim and record the
code that executed it; eight of the nine `ED-IN-*` rows are completed audits and programmes (`ED-IN-0183`,
`ED-IN-0184`, `ED-IN-0187`). **The flag is residue from filing, not a pending question.**

⚠ **The ninth IN row is `ED-IN-0059`, and it is the one member of class 2 whose status does not close it:**
it is `proposed`, not `resolved`/`ratified`/`executed`. Read it; do not sweep it with the other 38.

⚠ **And two of the 46 are traps**, which is why they are in class 1 and not here: `ED-IN-0127` says
*"needs_jordan TRUE for its per-directory table only … vetoable row by row"*, and `ED-MB-0045` is a
six-lens audit whose findings need rulings.

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

Thirty-six rows cite no live path. **Class 5 is sized at 10, not 36**, because classes 1–4 take their
members first — 26 of the 36 are already superseded, authorial or escalated, and only the residue lands
here. **At least three of the thirty-six are live questions anyway** —
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

### A worked example — and the retraction it earned

**`ED-SC-0005`** — *"cap the Recall/Corroborate/Prep/Findings bonus-die stack; the cap value is Jordan's
design number"* — is one of three rulings `workplan_v6_progress.yaml:60` calls a **HARD** block on SC
Stage 4. An earlier draft of this document closed it on §0 tests 2 and 3, arguing that *"the four channels
are implemented, and they are not dice"*. **That closure is retracted. It was wrong, and its own falsifier
sat eight lines above the citation it used.**

- `systems/social_contest/sim/contest/resolver.py:300` — `pool = Pool.size(c.faculty) + max(0.0, pool_bonus)`,
  where `pool_bonus` is `CR4_PRIMARY_GENRE_POOL_BONUS = 1.0  # +1D` (`rhetoric.py:206`). **An integer
  bonus die is live in the kernel today.**
- `armature.py:70` says so explicitly: *"This is a SEPARATE channel from CR4's +1D: **CR4 is an integer
  POOL die** … the armature is a continuous δσ leverage."*
- `primitives.py:295` — `CORROB = (1.0, 0.7, 0.5, 0.35)`, applied **multiplicatively**. Corroboration is
  neither a die nor δσ.
- The prose stack the row was filed against is still live: `social_contest_system_v2.md:160` *"Recall
  bonus: +2D"*, `:153` corroborate *"+1D"*, `:311` *"floor(TS ÷ 30) (+1D at 30, +2D at 60, +3D at 90)"*.
- And the row's premise is not what the closure treated it as. `ED-SC-0005` says *"cap … **in prose BEFORE
  Stage 4 wires the channels**"* — "not yet built" is its stated reason for acting **now**, not a reason
  the question died. §0 test 2 does not reach it.

**What is actually there is a better finding than the closure was.** The four channels ride **three
different ladders** — an integer pool die (CR4), a continuous δσ under `soft_cap` (the armature), and a
hard-coded multiplicative tuple (corroboration). *"Calculations consistent in methodology with other
mechanics"* is `§0.06`'s **S** criterion, and three ladders for one quantity fails it. **`ED-SC-0005` is
not mechanically closable, and the cap value is the second question, not the first:** what should be
answered is which ladder the bonus channels ride. That is `§0` test 5 territory — an architectural call
with an obvious shape — and answering it makes the cap value follow.

⚠ **And the draft committed the very defect it accused the board of.** It read `workplan_v6_progress.yaml:61`
(*"the cap is ALREADY ruled … kernel M_MAX=1.5 tanh"*), correctly identified that a die count and a σ
soft cap are different quantities, and then **closed the row on the σ channel anyway.**

**`ED-SC-0003` is retracted too, and more simply: the collision reproduces.** The draft tested it against
`systems/overview/reference/clock_registry_v30.md:60`/`:87` — a document `ED-SC-0003` never cites. On the
surfaces the row *does* name, and on two it does not:

- `references/glossary.md:114` — *"⚠ NAMING: `social_contest_v30.md` calls this same debate tracker
  **Persuasion Track** — **unresolved** glossary↔social-contest name collision"*;
- `references/module_contracts.yaml:448` — *"NAME COLLISION (3-way) **[OPEN — Jordan]**"*, in the file
  this document re-measured for §3(4) and did not read for §5.

The one real finding available here is smaller: **the row's line pin has drifted.** `glossary.md:84` is now
a `### Thread Practitioner Stats` header; the entry moved to `:114`.

**Net: all three of SC Stage 4's "HARD" blockers stand.** `ED-SC-0004` was always real. `ED-SC-0003` and
`ED-SC-0005` survived the attack. The board at `:60` is right and this document was wrong about it —
which is the outcome §0's adversarial-pass rule exists to produce, and it is recorded here rather than
quietly dropped.

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
| **11** | Adopt the **doctrine amendments** to `CLAUDE.md` §0/§0.1, and keep or end structurally independent adversarial review? | docket **D6**/**D7** | **keep adversarial review.** `D7`'s own evidence is from 2026-08-19 (`ED-SC-0028`, `ED-IN-0159` §8, `ED-MB-0061` G19); the fresh evidence is **this document** — a read-only critic overturned four of its conclusions, including its #1-ranked move and both of its proposed closures | the only items that reduce **generation** rather than stock |

**Two arrived today and are not ranked above**, because they landed on `main` while this document was
being written: **`ED-SE-0051`** — *"the bound on the demographic loop: matter only, or matter plus hearth
capacity?"* (PR #391) — and **`ED-WR-0010`**, the threadwork applications proposal, `PROPOSED` and held
back from ratification-on-merge in full (PR #388). Both are class 1 by inspection.

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
- **No document may be the deliverable of a move**, with one declared exception. §0.2: a juncture is done
  when the behaviour executes — for M1 that is the retirement running and the emitter firing. **M5 is the
  exception and is named as one:** its artifact is §6, which already exists, and Jordan reading a sheet is
  not a behaviour this repository can execute.

---

## §8 · Sequencing and tiering

| order | move | tier (`CLAUDE.md` §10) | effort | why that tier |
|---|---|---|---|---|
| 1 | **M1** execute the ruled | `sonnet`, `isolation: worktree` for the retirement wave | `high` | 47 files, 20+ inbound sites, several read by blocking gates |
| 2 | **M2** re-measure the blockers | `haiku` finders → `sonnet` verify → `opus` on any row whose command is missing | `low`/`medium` | re-running a row's own command is deterministic extraction; **deciding what to do when there is no command is not** |
| 3 | **M4** classes 2, 4, 5 | `haiku` to nominate, `sonnet` to cite, `opus` on the seven traps | `medium` | the closure text is the deliverable, not the predicate |
| 4 | **M3** grade-as-you-build | — | — | a discipline on other items, not a task of its own |
| 5 | **M5** the sheet | — | — | §6 already exists; the move is Jordan answering |
| 6 | **M6** at merge | — | — | a habit, not a task |

**Adversarial pass, and it is not optional here.** M1 and M4 are exactly the shape where a producer marks
its own homework, and **this document is the demonstration**: a `valoria-critic` dispatched with its
conclusions and none of its reasoning overturned §3(4)'s central number, both of §5's proposed closures,
and §4's entire first move. Dispatch `subagent_type: "valoria-critic"` with the *closure citations only*.
The independence is structural — that agent definition grants `Read, Grep, Glob` and nothing else.

**Two traps that pass caught, worth carrying forward.** A `yaml.safe_load` **strips comments**, so any
count of a grade written as `# [ASSUMPTION]` reads zero — check the raw text, not the parsed object. And a
closure argued from one channel of a multi-channel mechanism is not a closure; read the sibling channels
first.

## §9 · Falsifiers

Each headline claim, and the observation that would kill it. Per §0.1 pt 3, a result with no named
falsifier has not been attacked — **and a falsifier that is never run is not one.** Two rows below are
marked FIRED, because an independent critic ran them and they killed the claim.

| claim | falsifier | outcome |
|---|---|---|
| the ED queue reaches no game instrument | an ED cited by `requirements.yaml`, `hole_register.yaml` or the R-plan carrying `needs_jordan: true` | **survived**, with one qualification: `ED-061` carries no such field, so seven of eight are a recorded `false` |
| one of six R-blocking *holes* is a genuine ruling | any of `H-62`, `H-65`, `H-94`, `H-98`, `H-116` whose row does not record an answer already given | **survived on five, narrowed on `H-62`** — its row records a document and still ends *"a human decides"* |
| `ED-1051` is stale | `module_contracts.yaml` showing 11 `doc:null` / 13 `[ASSUMPTION]` | **FIRED.** `[ASSUMPTION]` is 11, not 1 — the parser stripped the comments carrying it. §3(4) corrected |
| `ED-SC-0005` is closable | a live resolver adding bonus **dice** as a count to a contest pool | **FIRED.** `resolver.py:300` + `rhetoric.py:206` — `CR4_PRIMARY_GENRE_POOL_BONUS = 1.0  # +1D`. Closure retracted |
| `ED-SC-0003`'s collision does not reproduce | the collision named on a surface the row actually cites | **FIRED.** `glossary.md:114` calls it *"unresolved"*; `module_contracts.yaml:448` marks it `[OPEN — Jordan]`. Retracted |
| the ladder is the first move | Layer 1 saying otherwise | **FIRED.** `PLAN.md:689-694` forbids closing those rows by ladder; `:664` records `W1` running it in 2026-09-02. §4 reordered |
| the class partition is exhaustive | the six classes summing to anything but 151 | **survived** — 23+39+11+39+10+29 = 151 |
| class 5's predicate is safe to run alone | a row citing only dead paths that is nonetheless live | **survived as a warning** — three found (`ED-IN-0147`, `ED-SC-0005`, `ED-SE-0002`), which is why the predicate only nominates |

**What this strategy does not know.** `H-43`'s row says it is *partly discharged and stale*; the extent is
unmeasured here. Twenty of the 34 `absent` rows carry `unblocks: unmeasured`, so §4's ranking is by
*stated* consequence, not measured consequence — M2 is what would replace that with a measurement. The
eight W-items in `blocks:` are not characterized at all. The 29 rows in class 6 have not been read, and the
expectation that most fall to tests 1–4 is an expectation, not a finding. Predicate E was not re-run, and
C's and B's movement since 2026-08-19 has no explanation here.

**Provenance of the corrections.** §0 item 2/3, §1.1, §1.2, §2, §3(4), §4, §5's worked example, §6 Q11,
§7 and this section were rewritten after a read-only `valoria-critic` pass on the first draft. Every
overturn was re-derived against the tree by the author before being applied; none was taken on the
critic's word. Two of its findings were **not** adopted: its arithmetic objection to class 2's
`MB 15 · PC 15 · IN 9` (the breakdown reproduces — `ED-IN-0127` is in class 1, and the ninth IN row is
`ED-IN-0059` at `proposed`), and its reading that `ED-IN-0208` breaches §0's one-row cap (that cap governs
the **adversarial pass**; this work was requested by Jordan, and §0 names `workplans/` as outside the
gate). Both disagreements are recorded rather than resolved silently.
