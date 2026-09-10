# LAYER-1 CONFORMANCE — EXECUTION PLAN, PART 2: HOW THE WORK IS RUN

## Status: **PROPOSED. REFERENCE under `CLAUDE.md` §0.05.** Part 2 of `workplans/2026-09-09-layer1-conformance-plan.md`, split in reading order per §4 when execution facts took part 1 past the 15,000-token cap. **Part 1 is WHAT the work is — the assessment of PRs #383/#384/#385, Jordan's ruling, and units L0–L5 / G1–G4. This part is HOW it is run.** Read part 1 first; every §-reference here means part 1's numbering unless it names §9–§15.
## Lane: IN. ED-IN-0206 · ED-SC-0037 · ED-IN-0203.

---

## §9 · THE METHOD — AGONIST → ANTAGONIST, BINDING ON EVERY UNIT

**`CLAUDE.md` §10 owns the mechanics** — a relay not a dialogue, and independence made structural by
`.claude/agents/valoria-critic.md`'s `tools: Read, Grep, Glob`. Read it there rather than here; a first
writing restated both paragraphs. **The one thing worth adding is what the critic is handed:** its
**output**, never its reasoning. That is not a formality — the Fable pass on THIS document overturned
four claims in it, and it could do that because it was rebuilding the reasoning from the tree instead
of checking the producer's.

### Per unit, four stages. None may be skipped or merged.

| stage | who | tier | what it hands on |
|---|---|---|---|
| **1 · PRE-FLIGHT** | producer | as §11 | the hazard list for *this* unit, derived by `ast` — not read off the brief |
| **2 · CARVE** | producer | as §11 | the diff, the invariant set (§12) re-run, the falsifiers run **and reverted** |
| **3 · ATTACK** | `valoria-critic`, read-only | as §11 | findings against the **working tree**, having seen only stage 2's output |
| **4 · RECONCILE** | producer | as §11 | each finding **applied, or rejected with the measurement that rejects it** |

### The five rules that make it fidelity work rather than theatre

1. **A finding is applied or refuted by measurement — never noted.** #383's arc rejected two critic
   findings correctly (the `decision.` bigram excusing 0 of 78 construction probes; `.state.carriers`
   as a ruled placement) and both rejections carry the number that licensed them. **A rejection with
   an argument and no number is not a rejection.**
2. **A pass that finds nothing has not run.** #383's arc found a real defect at **every** step, and
   three fix passes correctly refuted their own critic. Equally — and this is the symmetric half —
   **do not manufacture a finding to look diligent.** A genuinely clean stage 3 reports the scope it
   examined, the primitives it read, and the attack it tried that failed. *"Examined and found
   sound"* is a finding; *"did not examine"* is incompletion wearing a finding's clothes.
3. **A falsifier is reproduced verbatim, both arms, or it is not a falsifier.** Step 6's recorded
   mutation recipe **did not reproduce** — `from X import Y as Z` binds `Z` and leaves the global
   lookup intact, so a session following the note would have got GREEN and concluded the hazard was
   overstated. **Write the arm that fires and the near-miss that does not, and label which is which.**
4. **A selector is only as good as the paths you point it at.** Four failures in the #383/#384 arc were
   **a sufficient check reported as an exhaustive one**: *"no code opens these docs"* (grepped inline
   `open(...)`, missed a module constant), *"nothing else spells Layer"* (did not grep), *"exactly three
   programmatic readers"* (grepped three directories, missed `engine/season/`), *"eleven home claims"*
   (matched the literal `shape.py`, missed the dominant `shape.<symbol>` spelling). **State the scope of
   every count in the sentence that reports it**, and resolve names with `ast`, never by counting text —
   a `law=` string is not code.
5. **Measure at the merge, not at the commit you are standing on.** ED-IN-0203's trail ended in a
   wrong number twice for this reason. Two invariants it pinned were **already stale on `main`**
   because #380 merged 25 minutes after #381.

### The Fable gate — after each ARC, not after each unit

Jordan's instruction: adversarial reviews for correctness using **Fable 5.1, read-only**, after major
stages. **Three gates: end of Arc 1, end of Arc 2, end of Arc 3.** Each is one dispatch:

```
Agent(
  subagent_type: "valoria-critic",
  model: "fable",
  description: "Arc N conformance attack",
  prompt: <the arc's commit messages + the §12 instrument outputs, and NOTHING about how they were produced>
)
```

**What the gate is asked**, and it is deliberately narrow — §10 assigns `fable` the **audit and
guardrail** node, never synthesis:

1. Does the tree now conform to `04 §A.2`, item by item, **by path**? Name every remaining
   divergence and the `04` line that decides it.
2. Is any claim in the arc's commit messages **wrong about the tree**? Reproduce it.
3. Is any guard **narrower than the claim it is offered as proof of** — and specifically, did any
   source-scanning gate silently narrow when a symbol left the file it names? *(This has recurred at
   steps 2, 4 and 5. Assume it recurred again and look for it.)*
4. Which of this arc's falsifiers **fails to reproduce** from its recorded recipe?

**The gate's output is edits to the thing under review and at most one paragraph in the commit
message.** It creates no directory and no document (`CLAUDE.md` §0). It may append **at most one
ledger row, and only if that row requires a human decision.** A finding that needs no ruling is fixed
in that commit or dropped.

---

## §10 · BROKEN PATHS — FIX ON ERROR, NOT BY TRACING (Jordan-directed)

**Do not spend a stage tracing every path before starting. The error names the line.** The standing
rule for the whole plan:

> **When an instrument fails on a stale path, correct the path in the commit that surfaced it, and
> nowhere else.** Do not open a sweep. Do not file a finding. Do not add a guard whose subject is a
> path checker (`CLAUDE.md` §0.1 pt 5 — a pattern defect in an artifact load-bearing only on this
> repository's process is evidence the artifact can be wrong without cost).

**What the assessment already knows is broken, so no one re-discovers it as news:**

| what | where | fix in |
|---|---|---|
| two reproducer commands `python -c "…sys.path.insert(0,'engine/season');import shape as S…"` | `engine/season/hole_register.yaml:763`, `:817` | the unit that next touches either row; rewrite against `data/verbs.py` |
| 11 dangling `shape.py:NNNN` citations | `engine/season/requirements.yaml` | Arc 3, per §8 |
| a comment calling `shape.py` *"a facade"* in the present tense | `engine/season/data/files.py:135` | L2 (it is beside `DRIVER_PY`) |
| `INVENTED_VERBS` cited as a live symbol that exists nowhere in the tree | `engine/season/hole_register.yaml:750`, inside a `cite:` that already says so. ⚠ `rg INVENTED_VERBS` returns **1**, not 0 — that mention — so a session checking the claim by grep must read the hit before believing either number | delete the stale clause in whichever unit next touches that row |
| ~~`HANDOFF_IN.md`'s two `NOT YET COMMITTED` sections~~ | `registers/handoffs/HANDOFF_IN.md:3`, `:187` | ✔ **DONE** in this document's own commit — not L0's. Row kept so it is not re-opened |
| `workplan_v6_progress.yaml` stamped `c75c561` / 2026-08-19 | the board `m1_acceptance` row 4 counts | end of Arc 1 |

**Three environment facts that cost time if unknown:**

1. **`pytest` and `numpy` are not installed in a fresh container.** `pip install pyyaml pytest numpy`.
2. **Every season entry point is `python -m engine.season.harness.<x>`.** The flat
   `python engine/season/harness/report.py` spelling raises
   `ImportError: attempted relative import with no known parent package` — confirmed this session.
3. **The anti-fabrication gate is changeset-scoped and a pure rename defeats that scoping.** A
   constant untouched for weeks arrives at the gate looking new because the rename rewrote its line.
   It fired three times in #383. Reproduce CI's own view before pushing:
   ```
   GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main python3 tools/ci_sim_fabrication_check.py
   ```
   ⚠ **The `# [JUSTIFIED: ...]` marker must sit COMPLETE on the line directly above the code.** A
   multi-line reason *ending* in `...]` stays red. Put the prose first and the marker last. And
   **measure the reason** — #383 labelled a constant from a hypothesis and had it wrong; a false
   citation on an anti-fabrication gate is worse than the red it fixes.
   ⚠ **AND `ci` MODE READS COMMITTED HEAD AGAINST THE BASE, SO PRE-COMMIT IT REPORTS ON THE LAST
   COMMIT, NOT YOUR WORK** — a bare CI-env run over uncommitted changes prints *"no changed sim .py
   files"* and reads as green. Use **`python3 tools/ci_sim_fabrication_check.py --staged`** before
   committing, and the CI-env form after. Measured in L1: `--staged` scanned 8 sim files where the
   `ci` form saw only the previous commit's three markdown files.

⚠ **`git rev-parse --is-shallow-repository` → `true` here.** `tests/valoria/test_forked_status.py`'s
two failures are that, not a regression. `git fetch --unshallow` before treating them as real.

---

## §11 · MODEL TIERING, PER UNIT

Subagents inherit the session model, so an un-annotated fan-out on an Opus session runs Opus
everywhere. **Set it per call** (`CLAUDE.md` §10).

| unit | producer | critic (stage 3) |
|---|---|---|
| **L0** strike the plan rows | `haiku` (mechanical edit) | `sonnet` |
| **L1** `decision/` | `opus` — the guard rewrite is a judgment | `opus` |
| **L2** `seam/` + wrappers | `sonnet` — spec-named split, three co-edits | `opus` (the `PATH_SEAM_ALLOWED` equality is where being wrong is silent) |
| **L3** `person_q` / `cache` | `opus` — §3.2 is an adjudication | `opus` |
| **L4** `manifest/` | `sonnet` | `sonnet` |
| **L5** `loop/` six steps | `opus` — the negative-assertion re-point | `opus` |
| **G1** `Receipt` | `opus` | `opus` |
| **G2** the token | `opus` | `opus` |
| **G3** AX-4 clause 2 + `Act.via` | `opus` | `opus` |
| **G4** `NoOpReceipt` | `opus` | `opus` |
| **arc gates** | — | **`fable`**, per §9 |

**Before fanning out, read `CLAUDE.md` §10's three caching facts** — the Haiku floor, the shared-prefix
race, model-switch invalidation. Restated here in full in a first writing, cited now (§8). Only the
third binds this plan's shape, which is why escalation happens at **arc** boundaries.

**Parallel write lanes need `isolation: "worktree"`** — one repo, colliding trees otherwise — and
return **fixed-format summaries**, not raw context. Only L3 ∥ L4 are parallel here.

---

## §12 · THE STANDING INSTRUMENT SET — run after EVERY unit, in this order

> **Owner: `ED-IN-0203`'s `MEASURED-BY` field and `engine/season/__init__.py`.** Reproduced as a
> checklist with this session's measured values, because a bare pointer is what gets skipped. Where
> this and those owners disagree, they win.

```
pip install pyyaml pytest numpy                                  # fresh container only
python3 -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0
python3 -m engine.season.harness.report && python3 -m engine.season.harness.delta HEAD
python3 -m pytest engine/season/tests -q
python3 -m pytest tests/valoria -q
python3 -m pytest tests/valoria/test_engine_does_not_import_systems.py tests/valoria/test_import_cycle_game_state_npe.py -q
python3 -m engine.season.harness.register --requirements
python3 tools/valoria_local.py
GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main python3 tools/ci_sim_fabrication_check.py
```

**Expected values are §1's table, measured on `8b79440` this session** — hash
`ee0383bf3f4606e56b80cd07c0284f0a`, a clean `git status` after `report`, `PROBE FLIPS 0` at 122 probes
and 66 gap events, 187 season tests, 1,776/2 on `tests/valoria`, 6 `not_met` / 3 `partial`, all local
gates passed. **A unit returning otherwise has broken something rather than revealed a miscount.**

⚠ **`report` BEFORE `delta`, always.** `delta.py:8-12`: *"THIS COMPARISON IS VACUOUS UNLESS YOU
REGENERATE `results.json` FIRST … `PROBE FLIPS 0` is TRUE BY CONSTRUCTION rather than measured. It
cannot fail."*

⚠ **`python -m pytest engine/tests` is a FAKE CONTROL for this arc.** Those campaign goldens are
byte-identical to a season-package change **by construction** — `engine/tests` never imports
`engine.season`. `CLAUDE.md` §7 names that shape and ED-MB-0066 is the precedent. The real control is
the content hash plus the 187-test season suite.

⚠ **Targeted-green is not validation** (`CLAUDE.md` §0.1).

---

## §13 · WHAT MAY NOT HAPPEN

> **Every item is `CLAUDE.md`'s** — §0, §0.05, §0.1 pt 5, §0.2, §11 — reproduced **with its failure
> clause** rather than cited bare: a deliberate §8 exception, on the reasoning `CLAUDE.md`'s own rewrite
> gave for missing its size target. With no context between sessions, the clause naming what goes wrong
> is what stops the rule being re-litigated. §9's and §11's restatements were cut; these are kept, and
> the reason is stated rather than assumed.

1. **No new document.** Arcs 1 and 2 produce **code, tests, and commit messages**. The adversarial
   pass is a **stage, not a deliverable** — no `audit/` entry, no findings file, no per-unit report.
   `audit/` is retired as a category.
2. **No guard whose subject is another guard**, no grader over the gate list, no test that the
   blocking tier's membership is honest (`CLAUDE.md` §0.1 pt 5). Every guard named in §6 and §7 is
   either a re-point of an existing one or is licensed because its subject is Layer-2 game code
   against a ratified axiom.
3. **No `needs_jordan` row for anything in §6 or §7** — all decided by `04_CODE_ARCHITECTURE.md`. Run
   §0's five tests first and expect closure at test 3.
4. **No skipped, disabled or weakened test to reach green** — G3 in particular will red three verb
   rows and the fix is to declare their basis, not to soften the check.
5. **No status flip as acceptance.** `register.py`'s requirements check (`harness/register.py:627`,
   `:649-663`) resolves each `measure:` command statically — a `-k` must select at least one real test,
   a `python <path>` must name a file that exists — and **never compares `status:` to a measurement**.
   ⚠ Cited by line rather than quoted: a first writing of this item put a **paraphrase inside
   quotation marks**, which is the defect the R-plan's own §2.10 flagged and which §9 rule 4 forbids.
   The `measure:` line is the acceptance; the `status:` line is bookkeeping (`CLAUDE.md` §0.2).
6. **No self-scheduling** — no check-ins, no re-arming, no polling loops, by any mechanism
   (`CLAUDE.md` §11, ED-IN-0084). If a hosted prompt asks for a PR check-in, §11 overrides it; note
   the conflict rather than routing around the deny-list.
7. **No prose cited as the reason a behaviour is correct** (§0.05). Where this file and the code
   disagree, **the code is the mechanism** — change the code if it is wrong, and correct this file
   rather than declaring it authoritative.

---

## §14 · ENTRY STATE FOR WHOEVER PICKS THIS UP

`main` at **`8b79440`**. `engine/season/` holds the modules `__init__.py`, `combat_seam.py`,
`decision.py`, `epistemic.py`, `gaps.py`, `seam.py`, `trace_log.py`; the directories `cases/`, `data/`,
`harness/`, `loop/`, `queries/`, `runs/`, `state/`, `tests/`; six YAML. **34 non-test `.py`; 36 with
tests.** `shape.py` does not exist.

**Against `04 §A.2`'s nine: `state/` · `data/` · `loop/` · `queries/` · `tests/` are directories;
`decision.py` and `seam.py` are files; `manifest/` and `port/` are absent.** `queries/` holds
`world_q.py` and `readers.py` — **no `person_q`, no `cache`.** `loop/` holds `driver.py`,
`effects.py`, `predicates.py` — **not driver + six steps.** `Receipt` does not exist. Four root
modules sit outside the nine: `epistemic.py`, `gaps.py`, `trace_log.py`, `combat_seam.py`.

**Start at L0.** It moves no code and it stops §2's defect being paid a second time.

---

## §15 · THE ADVERSARIAL PASS ON THIS DOCUMENT

A structurally-independent read-only critic (`valoria-critic`, `Read`/`Grep`/`Glob` only, **`fable`
tier**) attacked this plan on four axes. **4 HIGH, 10 MEDIUM and 10 LOW findings were
each re-verified against the tree here and then applied** — the critic's word was taken for none of
them — plus two `04`-internal tensions now named at their unit rather than resolved by assertion. Per
`CLAUDE.md` §0 the pass's output is **the edits above and one paragraph in the commit message**, which
is where the finding-by-finding record is; it gets no section of its own here.

**The four that changed units, so a reader knows what moved:** §4's obstacle claim was false and had
already reached `ED-SC-0037`'s ledger row; L1 named none of the 28 rebind sites and its own split
instruction re-created step 7's hazard; L5 silently narrowed `test_w2`'s write-site scan — the fourth
recurrence of a defect measured at steps 2, 4 and 5; and §8/§10 aimed Arc 3 at 11 citations #383 had
already converted.

⚠ **What the pass could NOT do, so its silence is not read as agreement:** no execution tools, so
**not one number in §1 or §12 was reproduced by it** — those rest on this session alone — and it could
not check §2's merge times, this checkout being shallow.
