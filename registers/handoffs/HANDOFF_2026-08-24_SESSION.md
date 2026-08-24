# MASTER SESSION DOCUMENT — 2026-08-24

**Supersedes the earlier version of this file.** It is the single entry point for what happened, what
it means, and what to do next. Two executable plans sit beside it and are referenced by name; do not
read them until §6 tells you to.

---

## 0. STOP — the state of `main`

**PR #329 was merged at `dcf38ef`, carrying a deliberately unfinished engine port. `main` is RED.**

| | |
|---|---|
| `main` head | `dcf38ef` (squash of #329 — its title still reads "⚠ DO NOT MERGE AT HEAD") |
| canon mass-battle engine | **on `main`** — 33 files at `systems/mass_battle/sim/`; `tests/sim/mass_battle/` is gone |
| `tests/valoria` | **22 failures** — the port's tail |
| blocking validators | green (verified in real CI diff mode) |
| `engine/tests` | 2055 passed **locally**; **never confirmed green on a runner** — fail-fast cancelled it every time |

**A red `main` is the one thing CLAUDE.md licenses work on with no milestone trace** — §0's max-effort
amendment names it: *"a red `main`, which blocks everything and traces to nothing."* Fixing it is
sanctioned for any session, immediately, without asking.

**Start here:** confirm `engine/tests` green on a runner. If the campaign suite is genuinely fine,
all 22 are test-side expectations and the port is sound. If it is not, the port has a real defect and
everything below re-prioritises.

---

## 1. THE THROUGHLINES

Seven patterns, each with more than one instance, each costing real work this session. **These are
the reason to read this document.** The plans are downstream of them.

### T1 — Discriminators that do not discriminate

**Eight instances.** A classifier, filter, or predicate gets built, trusted, and used to drive a bulk
operation or publish a number — while separating something *other than* what its name claims.

| what it claimed to separate | what it actually separated | cost |
|---|---|---|
| work items about code | what a row **cites** (it matched the `source:` field) | culled 149 rows incl. the hub-and-bus gap itself. Reverted. |
| answered vs open questions | whether the row's **work** finished | cleared 17 rows; one was `ratified` while its code still said "held for Jordan". Reverted. |
| emitting module | tree layout vs **logical** contract names | published "0 of 60 declared emissions happen" |
| the emitter's module | a parent directory swallowing a sibling | battle Keys attributed to a module that never emits |
| the emitter | the first **claimed ancestor** — i.e. a caller | laundered an unclaimed emitter onto a bystander |
| declared Key types | dotted strings, silently dropping `{type: "*"}` | 13 phantom drift findings |
| stale path references | the **slash-form**, missing the `os.path.join` component form | CI red on a job I had declared fixed |
| what CI checks | **one commit** (`HEAD~1..HEAD`) vs CI's **whole branch** (`origin/main...HEAD`) | four wrong predictions in a row |

**THE LESSON.** *Name the predicate by what it actually separates, then find one case on each side it
must get right, and check those two by hand before it drives anything.* Every one of these had a
counterexample findable in minutes. None was looked for, because **every one of them was plausible.
Plausibility is the failure mode, not carelessness.**

**COROLLARY.** *A discriminator demonstrated wrong must not drive a bulk operation, and the revert is
total.* The 17 rows were all reverted though only 2 were proven wrong — the predicate that selected
all 17 is what failed.

### T2 — Checks that cannot observe the failure they exclude

§0.1 pt 2, recurring five times:

- A test asserted the **announcement dict** the code writes for itself, while the state it announced
  never moved — green over a dead ratified mechanic.
- A guard asserted "the attributed module binds a path" — **true of the very module the bug
  mis-attributed to**, so it was green over the exact bug it was written for.
- A triage fell back to wildcard consumers when nothing declared a type, making the failure branch
  **unreachable** — the tool reported its hard floor MET.
- A floor sat behind `hasattr()` on a function that did not exist — it had **never executed**.
- My own local gate runs diffed one commit while CI diffed twelve — `no changed files, nothing to
  check` read as a pass.

**THE LESSON.** *Write the mutation before the assertion.* State the one-line change that must turn
the guard red, apply it, confirm. **And never assert on a value the code under test produced about
itself** — assert on the state it changed.

### T3 — Optimising the measurement instead of the thing

- The handoff recommended wiring an emitter **because it would move `observed` 3 → 4** — without
  checking whether the number could be moved *honestly*. It cannot: every candidate needs invented
  payload or is unreachable.
- "108 declared / 13 matched" was **circular** — for a wildcard module, `matched == observed` by
  construction. The number could not fail.
- A key-log golden stayed at **exactly 187** while an emitter inside it went to zero. The total was
  stable; the composition had collapsed.

**THE LESSON.** *Before publishing a coverage or conformance number, ask what would make it go DOWN.
If nothing can, it measures that the plumbing ran.* And **never take an action whose justification is
that it moves a metric** — that is how an instrument starts lying.

### T4 — A predicate is not a licence where a ruling already decided

I recommended culling `test_vacuous_assertion_check.py` in a document I had **already committed**. A
standing Jordan ruling keeps it, recorded verbatim at the call site
(`.github/workflows/valoria-ci.yml:246-250`), and `ci_checks_registry.yaml:34` independently marks it
the file's **only** `layer: L2` row — already classified as the deliberate exception.

A read-only critic applied §0.1 pt 5 correctly *in the abstract* and never asked whether the artifact
was ruled. I relayed it without asking either.

**THE LESSON.** *CLAUDE.md §0's five-test ladder puts "superseded by a later ruling" FIRST for exactly
this reason. Run test 1 before applying any predicate.* A correct predicate applied over a ruling is
still wrong.

### T5 — The graded surface is not the played surface (§0.3's T2 term)

| | lines |
|---|---|
| `tests/valoria` — what a session is graded on | 29,602 |
| `engine/tests` — what actually executes the game | 4,060 |

**Seven to one.** ~36% of `tests/valoria` (~51 files, ~10,800 lines) has *apparatus* — a tool,
registry, ledger, doc, or another test — as its subject.

**This session's own output ran 11:1 apparatus-to-game** (+904 `tools/`, +436 `tests/valoria`, +120
game code) in a session whose subject was centralizing the game.

**No plan in the corpus addresses this, and two say so explicitly.** The execution order's own
sharpest line: **"no game regression can currently red CI."** The Stop hook was emptied, which deleted
the apparatus-facing grade **without installing a game-facing one**. T2 is now vacuum, not fixed.

**THE LESSON, and it is the hardest one here.** *An instrument that measures the game is still
apparatus.* §0.1 pt 5's load-bearing predicate licenses building it; it does not make building it game
work. This session produced one game fix and a great deal of measurement about why more is not wired.

### T6 — Deduplication is real; wiring is at zero

What the directive asked for versus what happened:

**Done — measured, not claimed:**

| | before | after |
|---|---|---|
| Conviction rosters | 3 incompatible (9 / 8 / 13) | 1 |
| mass-battle engines | 2 (campaign ran the smaller) | 1 |
| degree ladders (MB) | 2, held equivalent *by measurement* | 1 |
| real import cycles | 3 | 2 |
| `sys.path` seams to the engine | 42 test files | 0 |
| owners of engine randomness | 7 scattered `random.*` | 1 |

**Not done:** the emit side is at **zero**. 60 declared emit edges, **3 observed, 0 matched**. 31
edges belong to modules that have code and emit nothing; none was wired. `Faction.adjust` bypasses
the bus at **30 of 31** call sites.

**And the reason matters more than the number** — see §3, W1.

### T7 — The relay works, and it is cheap

Four Fable-5 critics against this session's published claims, then three planners and an independent
antagonist against *their* output. Result: **four confident, well-cited recommendations killed — two
of them mine, one already committed to the repo.**

**Of the six defects the first round found, four were the instrument's model of the registry, not the
engine.** None came from the game.

**THE LESSON.** *Point an independent reader at the OUTPUT, never at the reasoning.* A critic that
never saw why you believe something is the only one that can tell you the belief is unfounded. This
is §10's agonist→antagonist relay and it earned its cost every time it ran.

---

## 2. WHAT THIS SESSION DID

**Rulings recorded** (now binding, in `CLAUDE.md`):
1. **§0.05 — code is the mechanism, prose is reference.** Test: *if this document were deleted, would
   the game behave differently?*
2. **§0 — `needs_jordan` is not a parking space.** Five-test escalation ladder.
3. **No `.md` sweeping unless prose is named** — enforced as a `PreToolUse` hook, not a paragraph.
4. **Unbuilt mechanic proposals are kept** — *"code that doesn't exist yet is still code to me."*
5. **Port `tests/sim/mass_battle` over `systems/mass_battle/sim`** — done, unfinished, merged.

**Shipped and green (through `d080a36`):**
- Conviction roster centralized to one owner through the established chain, **reviving a ratified
  mechanic that had been a silent no-op**: ED-912 §6.1's Scar hit an unknown-name branch and returned
  `magnitude=0` on every call while the caller reported success.
- `tools/export_module_contracts.py` + the cooked artifact — the contract interface, and the single
  owner of the directory→module binding nothing owned before.
- `tools/contract_runtime_conformance.py` — the first thing in this repo that asks the **engine** what
  it emits. Not wired into CI.
- The `.md` sweep hook, with 12 tests pinning that it is *wired*, not merely present.

**The port (merged, unfinished):** 11,342 lines moved; determinism preserved via a new single owner of
engine randomness (the canon engine drew from global `random` at 7 sites — porting as-is would have
made the goldens **unpinnable**, not merely moved); the strategic adapter carried over field-for-field
so the golden delta is attributable to the resolution model alone; six campaign goldens re-recorded.

---

## 3. WARNINGS — carry these forward

**W1. The emit-side gap is NOT a wiring backlog.** Six candidates checked; **none is both cleanly
emittable and campaign-reachable.** One is reachable but the engine has **no mission concept**; the
rest are unreachable behind ruled deferrals, or their registry contract contradicts a ruling, or —
the case that survived two rounds of attack — the module **refuses by design** to guess the payload
(`echo_transport.py:278-283`: *"rather than a guessed settlement"*; the fallback map was deliberately
deleted). **Do not emit any of them to move `observed` 3 → 4.** It would move the number and make the
instrument lie.

**W2. `declared == observed` is the WRONG completion target for the bus.** 29 edges are an authoring
backlog and unobservable; **a centralized carrier is scored `ownership_mismatch` forever**, so driving
that to zero would *dismantle the hub the directive asked for*; and `observed` is seed-conditional.
The right DONE is in the completion plan §II.2.

**W3. §0.05 has a limit, and I got it wrong in a way a later session will repeat.** It resolves
doc-vs-**code**. It does **not** resolve doc-vs-doc where the code implements *neither* value, and it
**cannot** resolve code-vs-code. I filed 20 ledger rows as "answered by §0.05"; 3 of 3 spot-checked
were misfiled.

**W4. Ledger status is not a discriminator — but do not overcorrect into doctrine.** A row can be
`ratified` for the work it did while holding an unanswered escalation. **The flag was already there**
(`needs_jordan: true` beside `status: ratified`), so no "code outranks ledger" rank rule is needed or
supported. Check the code as *practice*; don't invent a hierarchy.

**W5. Local gate runs are vacuous unless you set the CI env.** `ci_common._diff_args` reads the
environment: CI diffs `origin/main...HEAD`; a bare local run diffs `HEAD~1..HEAD`; `--staged` sees
only staged files. **Always:**
```sh
git fetch origin main && export GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main
```

**W6. Goldens are change detectors, not correctness claims.** At n=2 and n=8 they cannot separate a
balance change from noise. Their job is *"did this move output, and did you know it would?"*
**Re-record a value pin without ceremony; NEVER re-record a *property* assertion without deciding
whether its claim is still true.** This session found two things a scalar pin could not see.

**W7. A cull must not mint a guard.** The negative control is in the completion plan §I.3: over the
whole cull, `git diff origin/main --stat -- tools/ tests/valoria/` must show **no new checker file**.

**W8. Two claims in the plan of record are wrong and will waste a session.** The culling plan says
*"tag, push the tag"* — **tag pushes are refused by this environment**; use an on-origin-main ref. And
`audit/2026-08-11-code-leanness/` is **deliberately exempt** for two independent reasons; "just fork
`audit/`" re-breaks what PR #323 stepped around.

---

## 4. LOOSE ENDS, TIED

| # | loose end | status / where it goes |
|---|---|---|
| 1 | **22 red tests on `main`** | licensed work, start with the 8-test `TypeError` cluster — the only one that might be a port bug rather than a stale expectation |
| 2 | **`engine/tests` never confirmed green on a runner** | fail-fast cancelled it every run. Confirm first — it re-prioritises everything |
| 3 | **`da.public_governance` went silent** at seed 42 after the port, while the key total stayed at 187 | real behavioural finding; 3 of the 22 red tests. FA lane |
| 4 | **"The spine can shut a faction out" stopped being true** | pinned two-sided with the open question recorded: real invariant, or artefact of the old resolution model? |
| 5 | **`SEED_BASE` defined twice** in the canon engine (1,000,000 vs 2,000,000) | surfaced by the exporter; one of the 22 |
| 6 | **Knot Pool formula** — ratified `+3, min 5`; code implements neither | ⚠ the **oracle** plays the wrong formula; the campaign plays none. Session-decidable, Jordan already ruled |
| 7 | **Knot-break "+1 to both partners"** — code scars one. Same gap covers 4 Composure | session-decidable |
| 8 | **`meta.knot_formed`** registry demands `Loose\|Medium\|Close`; ruled tiers are `Distant/Close` | registry stale by ruling. Second stale surface at `fieldwork_editorial.md:56` |
| 9 | **Two Key types no contract declares** (`scene.accord_echo`, `meta.cascade_cluster_event`) | `--check` exits 1 on them today |
| 10 | **`contract_runtime_conformance.py --check` wired nowhere** | under §0.05 an unwired instrument is not a mechanism |
| 11 | **`test_gauge_invariants.py:43-49` imports from an `audit/` unit by bare name** | found only by the antagonist; no cull plan named it. Repoint in whatever commit moves that unit |
| 12 | **154 `needs_jordan` rows** | the 17-row clearing was reverted in full. ~20–30 are genuinely Jordan's |
| 13 | **Churn engine** — RATIFIED, referenced by `CURRENT.md`, implemented nowhere | **not a conflict** — an unexecuted juncture. Moves to `systems/narrative/`, does not fork |
| 14 | **PC degree ladder held** at the pre-2026-08-14 model | Jordan's, and must go to him **with** the score/2 obstacle migration — the code says deciding them separately wastes the work |
| 15 | **255 of 420 sim constants uncited** inside `systems/` | instrument is `export_sim_params.py:244-246`; §0.05's "321" predates the port |
| 16 | **10 tools still parse `module_contracts.yaml`** directly | an exporter now exists; they are a migration backlog with a destination |
| 17 | **13×4 conviction-axis matrix cooked nowhere** | its first consumer is already written and waiting (`npe.py:314-323` calls its uniform draw a placeholder) |
| 18 | **`audit/` — 230 tracked files** | S7 unexecuted; needs no design, only execution |
| 19 | **`main`'s merge commit title reads "⚠ DO NOT MERGE AT HEAD"** | cosmetic, permanent, not worth a rewrite |

---

## 5. WHAT IS GENUINELY JORDAN'S

Everything else is answerable by ruling, document, precedent, or architecture.

1. **ED-SC-0004** — the Argue-pool fork, two live formulas, explicitly reserved. *(A third option
   nobody had spotted: ED-FI-0005's ratified shape is the merge of the two candidates.)*
2. **ED-IN-0187 + the obstacle model** — the degree-ladder hold and the score/2 migration, **together**.
3. **The reachability deferrals** — whether campaign-scale world-gen may carry personal-scale actor
   fields. **This is what actually gates the emit side.**
4. **Whether to build the PP-686 mission mechanic at all.**
5. **ED-PC-0016** (half-sword auto-switch) and **ED-PC-0049** (`ADEF_POINT` 1.2 vs ~1.53).
6. **S8 Half B** — suspended; listed so nobody launders it into the cull.
7. **T5 / the graded surface** — nothing can move it without you. *"No game regression can currently
   red CI"* is the corpus's own finding, filed and never executed.

---

## 6. DIRECTION — the order to work in

```
0.  Confirm engine/tests green on a runner            ← re-prioritises everything
1.  Fix main's 22 (start: the 8-test TypeError cluster)   [licensed: red main]
2.  Knot Pool + both-partners                              [game code, unblocked]
3.  da.* registry row + the silent emitter                 [inside the 22]
4.  Registry hygiene: knot tiers, the 2 undeclared types
    → then wire contract_runtime_conformance --check into CI
5.  S7 — the cull, from tools/evacuation_plan.py, not the ratified prose
6.  Faction.adjust emit spine — one Key per EVENT, not per write
7.  Read side: 10 parsers, the axis matrix, the constants
8.  Queue drain, by lane, ≤20 rows/PR, every closure quoting disk evidence
9.  Compile the Jordan docket ONCE, with options and recommended defaults
```

**Why this order:** the two unblocked game fixes are cheap and verifiable; registry hygiene precedes
the cull because the cull's gates read those registries; the emit spine follows the cull because S7
changes what the conformance instrument sees; the drain goes last because the cull kills subjects
first, converting judgement calls into citations.

**Before any of it, always:** `git fetch origin main && export GITHUB_EVENT_NAME=pull_request
GITHUB_BASE_REF=main` (W5).

---

## 7. WHERE EVERYTHING IS

| document | what it is | read it when |
|---|---|---|
| **this file** | the master record — throughlines, warnings, loose ends, direction | first, always |
| `proposals/2026-08-24-completion-plan-v1.md` | executable how-to for the cull, centralization, doc-vs-code; **records four killed recommendations as killed** | before executing §6 steps 4–8 |
| `proposals/2026-08-24-error-regions-v1.md` | eleven error regions as plan items, with the lesson and files per region | when a defect smells familiar — it probably is |
| `scratchpad/closeout/` | `agonist_emit_reachability.md`, `reconciliation.md`, `antagonist_verdicts.md` | to see how a conclusion was reached, or contest it |

---

## 8. THE ONE-PARAGRAPH VERSION

This session deduplicated the largest duplications in the repo — three Conviction rosters to one, two
mass-battle engines to one, two degree ladders to one, three import cycles to two, 42 path seams to
zero — and revived a ratified mechanic that had silently been a no-op. It built the first instrument
that asks the engine what it actually emits, and that instrument's answer is **3 of 60**, which is the
real state of the hub-and-bus goal. It did **not** wire a single emitter, cull a single audit file, or
close a single doc-vs-code conflict; and the reason the wiring is at zero turned out to be structural
rather than lazy — no declared edge can be emitted honestly today. Against that, the session produced
eleven lines of apparatus for every line of game code, which is the pattern §0.3 named and which no
plan in this corpus addresses. **The most transferable thing it learned is that eight separate
discriminators, four confident recommendations, and five guards were each wrong in the same way:
they were plausible, and nobody checked one case on each side.**
