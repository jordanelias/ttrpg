# Valoria — TTRPG / videogame design repo

This repo is the **design source of truth** for **Valoria**, a Godot 4.6 videogame that fuses
personal-scale resolution (dice pools, skill checks, social contests) with a strategic layer
(territory control, faction politics, domain actions). **There is no GM — the engine resolves
everything.** Design docs keep their TTRPG/board-game mechanical detail; those abstractions *are*
the videogame's layers.

- **Design source of truth:** `jordanelias/ttrpg` (this repo).
- **Implementation repo:** `jordanelias/valoria-game` (Godot 4.6) — separate clone, frozen since 2026-05-04.

---

## 0. How we work (method, not location)

§1–§10 tell you *where things are* and *what's current*. This section tells you *how to work* — the
default posture for every non-trivial task in this repo, not just orchestrated fan-outs. (The
multi-agent mechanics live in §10; the disposition below applies whether you're solo or fanning out.)

- **Plan before you touch the tree.** Establish currency (§1 → `CURRENT.md` + your lane's
  `HANDOFF_<LANE>.md`), read the subsystem head and its `## Status:` line, and state the plan —
  what you'll change, in what order, and how you'll verify — *before* the first edit. For anything
  ambiguous or spanning lanes, get the plan approved (or ask a focused question) rather than guessing.
  A wrong assumption caught in a plan is free; caught in a merged commit it becomes editorial debt.
- **Build bottom-up from primitives.** Find the single-owner primitive first and compose on top of it
  — never re-implement a rule that already lives once (§8's core invariant). New tooling reuses
  `obs_core` / `audit_staleness` / `review_core` / the registries; new mechanics resolve from the
  Key substrate up. Emergence is the goal: small correct primitives, composed, not a bespoke
  top-level special case. If you find yourself special-casing an entity or outcome, stop — that's
  scripting drift (§10 guardrails).
- **Adversarial pass at every stage that gates a result.** Producing and checking are different jobs:
  after you draft canon, a number, or a fix, *try to break it* — verify provenance by hand against
  the cited `PP-NNN`/`ED-NNN` (the anti-fabrication gate is leaky — `validate_ed_citations.py` is
  scoped to ED only, and since the 2026-08-05 evacuation removed the patch archives, **[SUPERSEDED 2026-08-18: ED-IN-0190 measured **531 of 537** distinct PP ids across 318 live files. The 433/452 below is the 2026-08-05 figure, kept only so older citations of it resolve.] 433 of 452
  distinct `PP-NNN` numbers cited in live surfaces resolve to no register on `main`**; disposition
  held, ED-IN-0147), run the relevant `tools/`
  validator, and for a judgment call put a genuinely independent critic on it (structural
  independence, read-only, §10). Don't report a result you haven't attacked.

  **AMENDED 2026-08-19 (Act 4, Jordan-directed — the adversarial pass is a STAGE, not a DELIVERABLE).**
  Its output is **edits to the thing under review, and at most one paragraph in the commit message.**
  It does not create a directory or a document. It may append **at most one ledger row, and only if
  that row requires a human decision** (`needs_jordan: true`). **A finding that needs no ruling is
  either fixed in this commit or dropped.**

  Why the row gate rather than a row ban: rows are the loop's carrier, but they are also the only
  persistence channel across a session boundary, and this repo has no context between sessions. Ban
  them outright and a real cross-lane game defect evaporates at Stop; allow them freely and the
  generator's gain stays above 1. Gating on `needs_jordan` **makes the human the low-pass filter on
  the only surviving channel** — gain below 1 by construction, because the loop can no longer feed
  itself work no human ordered. This deletes `audit/` **as a category, not as a cleanup**.
- **Max effort on the deliverable named by the current milestone**, where a juncture is done only
  when **the behaviour executes** (§0.2). Reach for the most thorough path *that deliverable*
  warrants — exhaustive over cursory, verified over plausible. **Work is this session's work if
  Jordan asked for it this session, or it traces to an open M1 juncture; nothing else is.** If
  something broken blocks the milestone, **fix it minimally, without adding a guard.** Tier *down*
  only deliberately and per-task (§10), never as an excuse to under-invest on the judgment nodes.

  **AMENDED 2026-08-19 (Act 4, Jordan-directed).** The previous wording was "max effort by default …
  the harder-but-correct fix over the local patch", with no *selection* term. The defect it caused:
  "exhaustive" is **satisfiable on apparatus** (107 tools are enumerable) and **unsatisfiable on the
  game**, so a doctrine demanding exhaustiveness drifts to whichever surface is enumerable — and
  "prefer the harder-but-correct fix" literally instructed the agent to prefer the option that grows
  the tree. The two carve-outs are deliberate and bounded: without the first, the literal reading
  tells a session to **refuse Jordan** (a ruling request traces to no juncture); the second covers a
  red `main`, which blocks everything and traces to nothing.
- **Close the loop, honestly.** Run `pytest tests/valoria` + the lane's validator, commit with the
  `[scope]` format citing the `PP/ED`, and capture next actions in your lane's `HANDOFF_<LANE>.md`.
  If a check failed or a step was skipped, say so plainly — a green claim you didn't verify is worse
  than a red one you did. The SessionStart banner (§1, `tools/session_status.py`) surfaces your
  lane's pending work, open editorial debt, schema-in-flux flags, and stale audits at start — read
  it; it exists so these stop getting missed (ED-IN-0081).

### 0.1 Measurement discipline — five checks, each with an artifact (ED-MB-0042, 2026-07-25)

These exist because a flag was flipped on a **confounded measurement**, shipped a default, re-recorded
two byte-exact goldens, and was retracted the same day — *after* the identical defect class had already
been found and fixed as a one-off hours earlier in the same session. Note what was **not** the gap: §0
already required an adversarial pass at every gating stage, and one was performed. It attacked the
result's *statistics* (noise, sigma, band edges) and never its *setup* (are the two arms the same
experiment?). Restating the principle is therefore useless. **Specificity about what to attack, and an
artifact proving it happened, is the whole of the fix.**

1. **The hazard is read/write asymmetry, not "change".** When a getter starts computing from a new
   source (`eff_morale` from cells) while setters still write the old one (`.morale`), every writer
   silently becomes a no-op. Before measuring anything about such a change, grep the field's
   **assignments** — not its readers, which are unbounded and mostly harmless — and ship a guard that
   fails on a *new* bare assignment. `tests/valoria/test_morale_write_sweep.py` is the template; its
   `_CELL_OWNED` registry is field-parameterized so each newly cell-owned state inherits the guard by
   adding one key.
2. **An assertion must be able to observe the failure it excludes.** `pytest.approx` on an *exactness*
   claim is not a weak test, it is an absent one — a 1-ulp aggregate error crossed a damage-degree
   boundary while its own identity test passed. A loop that asserts conditionally must assert that it
   asserted (`assert checked >= N`); that pattern is what surfaced the born-broken-subunit bug.
3. **Name the falsifier, or you have not attacked the result.** A result claim carries, in the same
   commit, the specific test that would have shown it wrong and that test's outcome. "Adversarially
   reviewed" without an artifact is unfalsifiable and was, in this case, false.
4. **A number without a control is not a measurement — in either direction.** Asymmetric skepticism is
   a bias, not a defence: this session both *banked* a favourable uncontrolled result and *published*
   an unfavourable one. Absence of one failure mode ("nothing was tuned to hit a band") is not presence
   of correctness.
5. **Sweep pattern defects; fix one-off defects — but a guard must EARN its existence.** The signature
   of a pattern defect is *the broken code was correct when written and stopped working because
   something else changed.* Then: one owner for the operation, every site routed through it, and a
   guard that fails on recurrence.

   **AMENDED 2026-08-19 (Act 4, Jordan-directed — predicate on what the artifact is LOAD-BEARING ON,
   never on what it is ABOUT):**

   > *A pattern defect earns a guard only if the defective artifact is load-bearing on **the game** or
   > on **a Jordan decision** — its output crosses into the engine, the exported params, the port, or
   > the `needs_jordan` queue. A pattern defect in an artifact that is load-bearing only on this
   > repository's process is **not** evidence the artifact needs a guard; it is evidence **the artifact
   > can be wrong without cost. Delete it, or accept the defect and write nothing.***

   The old rule quantified over pattern *defects*, not over *subjects*, so it fired identically on a
   defect in the morale model and one in a test-register freshness checker. Apparatus outnumbers game
   ~3.9:1 by line, so a session reading more apparatus finds more apparatus defects and **mints more
   apparatus guards**. That is the generator, and this predicate is what disarms it.

   **Load-bearing is not the same as "about the game".** The predicate KEEPS `test_morale_write_sweep.py`,
   `ci_golden_modes_check`, `ci_sim_fabrication_check`, `export_engine_params.py`'s round-trip `--check`
   (apparatus by subject, but it produces the bridge the Godot port ingests), and a compile gate. It
   FORBIDS `test_wf_harness_check.py`, `test_gate_coverage.py`, `test_blocking_tier_is_honest.py`.

   ⚠ **This edit is inert without the `§0` adversarial-pass amendment above.** A session forbidden to
   write a guard will write **a finding about the defect** instead. The loop's carrier is prose, so
   closing only the guard channel reroutes rather than terminates.

   Sweep only what the current task is load-bearing on; for the rest, apply the predicate — **fix it
   here, or drop it.** ("File the rest" was the old instruction and it is exactly the reroute above.)

**`pytest tests/valoria` is a SHIPPING gate, not a belief gate**, and behaviour changes include default
flips and golden re-records. Do not credit it with catching confounds: it caught this one *only*
because the flip incidentally broke ten unrelated tests. A clean implementation of the same confounded
measurement would have been green. Equally, **targeted-green is not validation** — the tests you wrote
for the thing you built encode your model of it, not the system; all ten failures were in modules that
had never crossed my mind.

### 0.2 DONE MEANS IT RUNS (Act 2, RULED 2026-08-19 by Jordan — "I need to break out of the infrastructure loop")

**A milestone juncture is done when the behaviour EXECUTES. Not when a document exists with a
`## Status:` line.** This is the definition `§0`'s max-effort rule binds to, and it is the one claim
in this repository that a session **cannot satisfy by writing**.

That is the whole point. The loop's generator needs a definition of *done* that prose can reach.
Take that away and the freed capacity has nowhere to go but the game.

| | old `done` | new `done` |
|---|---|---|
| M1 juncture | a design doc exists and is `RATIFIED` | the behaviour runs, and something ran it |
| checked by | reading a `## Status:` line | an execution artifact — a run, a log, a hash, a test result |
| satisfiable by writing? | **yes** | **no** |

**Consequences, so this is not just a sentence.**
- A juncture may **not** be marked done on a document. `tools/m1_acceptance.py` is the instrument;
  its rows are falsifiable and it already refuses to guess.
- "Authoring the design doc" is **not** the deliverable for a juncture that has running code. Verify
  the code against the sim and record the contract; the doc may follow verified behaviour instead of
  preceding it.
- **A juncture that is done in code and open on the board is a BOARD defect, not a work item.** Five
  of M1's seven junctures have real implementations in `valoria-game` while the board scores 0/7.
  Both facts are true at once; that contradiction *is* the disease this section ends.

⚠ **This section is a precondition of `§0`'s max-effort amendment, not its sibling.** Bind max effort
to "the milestone deliverable" while `done` still means "a document exists" and the doctrine simply
aims maximum effort at authoring **prose** — the same output, better targeted.

### 0.3 The loop this repository was in, and why the banner is nearly empty (2026-08-19)

Read this before you "improve" the SessionStart banner by putting things back in it.

**Measured.** 68% of tracked files are machinery (916 vs 440 game/design). Commits touching
machinery vs content ran **5.2:1 in July and 10.8:1 in August** — accelerating. 191 commits with
*consolidate/cull/prune/retire/sweep* in the subject were a combined **net +82,020 lines**, and
**78% of them were net increases**; a document proposing to delete 350,000 lines was itself a net
addition of 1,819. Jordan gave the "make it lean" instruction four times; in the week whose stated
theme was leanness, `tools/` grew and CLAUDE.md grew 61,367 → 70,349 bytes.

**The mechanism has three terms, and they are not symmetric.**

| | what it is | how it fed the loop |
|---|---|---|
| **T3 — the generator** | `§0` mandates adversarial passes; passes emit findings; findings become ledger rows; rows appear in the banner; **the banner defines the next session's work.** Closed loop, gain > 1, no human in it. | Of 1,233 ledger rows, **59 cite a Jordan ruling; 152 name an audit or session document.** The single largest source is *an audit of the audit apparatus.* |
| **T1 — the amplifier** | what a session SEES at start | ~389 pending units, **none about the game** |
| **T2 — the reward** | what a session is graded on at Stop | clean tree · handoff · board · no regression — **all satisfiable without touching the game** |

**The defect was subject-blindness, not the rules themselves.** `§0.1` pt 5 is a good rule that
caught a real morale-model bug. But it quantified over pattern *defects*, not *subjects*, so it fired
identically on a defect in the game and a defect in a freshness checker — and apparatus outnumbers
game ~3.9:1, so every session found more apparatus defects and minted more apparatus guards. The
tree records the result at depth five: `ci_wf_harness_check` guards `wf_harness.js`,
`test_wf_harness` guards the harness, `test_wf_harness_check` guards the guard — **1,718 lines
guarding the prelude of the scripts that run the audits** — ending in
`test_blocking_tier_is_honest.py`, a test that the blocking tier's membership is honest. Every rung
a flawless application of the rule.

**What the amendments do.** `§0.1` pt 5's load-bearing predicate disarms **T3**. `§0`'s
adversarial-pass bound closes the prose reroute (forbid the guard and a session writes a *finding*
instead — the loop's carrier is prose). `§0.2` + `§0`'s max-effort selection term redirect the freed
capacity at **T2** and the game. The banner change is **T1**.

**⚠ THE BANNER IS A RUNNING EXPERIMENT.** It prints one thing — the current juncture and whether it
runs — precisely so the diagnosis is falsifiable: change nothing else and watch one session. If it
still writes apparatus, the ordering above is wrong and
`proposals/2026-08-18-breaking-the-recursion.md` should be attacked accordingly. **Adding lines back
does not measure anything.** Nothing was deleted — `session_open_work.py`, `review_core.py` and the
rest still run, and the banner names the command. They are available, not advertised.

---

## 1. Read these first (currency)

The live canonical surface is **Generation v40** (consolidated, contracts-bound, Godot-ready). There
are more "current state" files than there should be; trust them in this strict priority order:

1. **`CURRENT.md`** — the **single human-readable index** of the live canonical head per subsystem.
   When unsure whether a doc is current, this is the authority. Reconciled by hand — **read its own
   `_Last reconciled:_` stamp for the date; this file deliberately does not carry one** (it said
   2026-06-28 while CURRENT.md said 2026-08-04; a duplicated date rots independently of its subject.
   ED-IN-0147). Treat it as fresher than any filename or in-file version string.
2. **`HANDOFF.md`** — the **continuity index**: root file pointing to lane-scoped
   `registers/handoffs/HANDOFF_<LANE>.md` files (§3's `ED-<LANE>-NNNN` taxonomy: `MB, PC, FI, SC, FA, WR, IN,
   GO, SE`) plus genuinely cross-cutting pending work/decisions/next actions. Split 2026-07-02 to
   reduce concurrent-session merge-collision surface on one shared file, the same motivation
   behind the ID namespace itself. The SessionStart banner (`tools/session_status.py`) reads root
   `HANDOFF.md`'s "Next actions" section only — check your lane's file too.
3. **`references/canonical_sources.yaml`** + **`registers/mechanics_index.yaml`** — machine-readable
   indices. ⚠️ The `canonical_sha__*` pins in `canonical_sources.yaml` are **not verified against the
   working tree** (the only tooling re-syncs them *from* GitHub, which contradicts the working-tree
   rule). Treat the pins as advisory, not a trustworthy integrity signal.

**Ignore for currency** — these are stale or retired, do not resume from them:
- `README.md` — outdated navigational pointers; defers to the three files above.
- Retired session-log/checkpoint machinery (`session_log_*`, `session_logs/`,
  `deprecated/session_machinery/handoffs/` — old per-lane-A/B/C `.yaml` files, a **different,
  retired thing** from the live root-level `registers/handoffs/*.md` directory below, do not confuse them —
  `canon/session_checkpoint.md`, the `references/subsystems/{handoff,checkpoint,session_log}` docs)
  — **relocated to `deprecated/session_machinery/` (2026-07-01, ED-1084)**. NOT authoritative;
  **`HANDOFF.md` + `registers/handoffs/HANDOFF_<LANE>.md` are the only live continuity surface.** Do not
  write into or resume from anything under `deprecated/session_machinery/`.
- `deprecated/` (incl. `deprecated/archives/`, the former top-level `archives/` merged in 2026-07-16, ED-IN-0071 P5) — history only, never canonical.

---

## 2. How this repo is worked

- **The working tree is the source of truth.** Read and edit local files directly (Read/Write/Edit,
  Grep/Glob). **Do not re-fetch from the GitHub API** and do not trust memory over disk — the checkout
  is fresher than any cache. *(Caveat, CORRECTED 2026-08-05 — this rule is now essentially clean: the
  integrity gates were ported off the GitHub API by ED-1053, and the only remaining API caller is
  `tools/dashboard_data.py`, which fetches Actions/PR status — state that exists only on GitHub, not
  repo content. It is not an exception to this rule.)*
- **Commit with git.** Stage your own files explicitly and `git commit`; no bespoke wrapper. If you are
  on `main`, branch first. Commit message format:
  `[scope] description` where scope ∈
  `editorial, patch, simulation, compilation, infrastructure, skill, cleanup, godot, phase, fix, bugfix, design`.
  Cite `PP-NNN` / `ED-NNN` in the description when applicable.
- **Continuity = git history + `HANDOFF.md`/`registers/handoffs/HANDOFF_<LANE>.md`.** No session-log/checkpoint
  machinery is in use (despite retired files lingering — §1). When you pause mid-task, capture next
  actions in your lane's `registers/handoffs/HANDOFF_<LANE>.md` (or root `HANDOFF.md` only for genuinely
  cross-cutting items); a commit *is* the session close.
- **Merging a PR ratifies its PROPOSED contents by default (ED-1094, 2026-07-02).** If a PR lands a
  design doc, doctrine, or ledger entry tagged `PROPOSED`/`provisional`, Jordan's review-and-merge of
  that PR *is* the ratification — flip the doc's `## Status:` line, the ED ledger `status`/`needs_jordan`
  fields, and `CURRENT.md` as part of the same merge, not as a separate later step nobody triggers.
  **The exception must be loud, not silent:** if something in the PR genuinely needs separate,
  explicit sign-off beyond ordinary merge review, call it out prominently in the PR body as *held
  back* — never bundle a hard design call into a routine-work PR and rely on an unprompted follow-up
  to ratify it later. (This closes a real recurring failure: ED-1083's doctrine sat PROPOSED in `main`
  after PR #55 was reviewed and merged, because the prior convention required a distinct explicit
  ratification step that nothing forced to happen.)

---

## 3. Repository map

**What each tree holds NOW.** The migration history that used to live here — the slice-by-slice
record of how `designs/`, `sim/`, `arcs/` and `engine/params/` were dissolved — was **cut 2026-08-19
(Act 3)**. It was 20% of this document, it described trees that no longer exist, and the live
resolver for every old path is **`references/restructure_ledger.md`** (exact rows + dir-prefix
aliases, machine-read by `broken_dependency_checker`). `git log CLAUDE.md` has the narrative.

| Directory | Contents |
|---|---|
| `systems/` | **The design source of truth.** One subsystem = one folder = one ID lane = one `CURRENT.md` row = one `HANDOFF_<LANE>.md`. Each holds its design `.md` at the root and its oracle scripts in `sim/`, imported as `systems.<sub>.sim.*`. ⚠️ `characters/`, `overview/`, `victory/` are doc homes, not yet formalized 1:1 subsystems. |
| `engine/` | **The executable model.** A Python package: `substrate/` (Key substrate), `autoload/` (singleton hub), `cross_scale/`, `mc_v18.py` (campaign driver), `engine_params/` (the typed Class-C exports the Godot port ingests), `tests/` (seeded regression + parity, CI job `sim-regression`). Per-subsystem sims depend UPWARD on this core; acyclic, autoload is a leaf. |
| `canon/` | Philosophical foundations **P-01..P-15**, canonical timeline, canon constraints, amendments. World/design truth only — the process registers live in `registers/`. |
| `godot/` | The port + the eventual `res://` project root. Governing spec `godot_conversion_strategy_v1.md` is **PROPOSED, Jordan-vetoable throughout**, with unexecuted Gate-0 preconditions. `skeleton/` covers 1 of 27 modules and **does not compile** — never present it as a runnable head-start. Four 2026-04-18 docs carry `⚠️ STALE` banners; `godot_architecture_specification.md` is STALE REFERENCE (ED-GO-0001). |
| `registers/` | Process ledgers: editorial ledger (`editorial_ledger.jsonl` for pre-cutover flat IDs + `editorial_ledger_<lane>.jsonl` for `ED-<LANE>-NNNN`), patch register, supersession register, mechanics index. `registers/handoffs/HANDOFF_<LANE>.md` is the per-lane continuity surface; root `HANDOFF.md` stays at repo root. **All ledger files are authoritative — read all of them.** |
| `references/` | Registries and indices — `canonical_sources.yaml`, `names_index.yaml`, `glossary.md`, `module_contracts.yaml`, `descriptor_registry.yaml`, `restructure_ledger.md`. ⚠️ The `canonical_sha__*` pins are advisory, not a trustworthy integrity signal. |
| `tools/` | All CI checks, validators, collators, generators. Intended invariant: every rule lives once (§8). ⚠️ Measured 2026-08-05: **36 of 106 modules have zero automated callers.** |
| `tests/` | `tests/valoria/` is the pytest unit suite (the only executable tests here). ⚠️ Also ~850KB of narrative `.md` that is **prose, not executable spec** — do not mine it for behavioural contracts. ⚠️ `tests/sim/` is unrelated to the retired `sim/` package. |
| `workplans/` | The master workplan + `workplan_v6_progress.yaml`, the board the banner reads. |
| `proposals/` | Unratified proposals, surfaced BY LOCATION. |
| `dashboard/`, `.github/`, `.claude/`, `skills/` | Published status site; CI workflows; hooks, agents and orchestration scripts; skills. |
| `audit/` | The surviving audit corpus. ⚠️ **`§0` now forbids the adversarial pass from creating documents, which retires this as a CATEGORY** — do not add to it. |
| `deprecated/` | **Where files go when we stop using them** — moved out of `main`, kept at a named ref. Never canonical. ⚠️ One exception, by rule order: the old ledger files under `deprecated/archives/editorial*` and `deprecated/canon/` are KEPT, because `validate_ed_citations.py` reads them to tell a real ID from an invented one; delete them and every valid citation reads as fabricated. |

**Trees that were dissolved — do not recreate any of them:** `designs/` (retired 2026-07-19, contents
now in `systems/`), `sim/` (retired 2026-07-21, now `engine/` + `systems/<sub>/sim/`), `arcs/` and
`engine/params/` (evacuated 2026-08-05; the 43 param tables are captured byte-identically in
`engine/engine_params/params_tables.yaml`), `references/values_master.yaml` (retired 2026-08-02 —
auto-extracted and partly wrong; **never lift numbers from it**). Everything removed is recoverable
at fork ref `c451bcb`, and every old path resolves via `references/restructure_ledger.md`.

## 4. Conventions

> **Restored 2026-08-05 from ref `cadf9c7` (ED-IN-0147), verbatim.** Every rule here governs a
> surface that survived the evacuation: the 2026-07-26 Jordan RULING on document splitting, the
> `ED-<LANE>-NNNN` taxonomy that §1 and §3 both cite, and the naming gate that
> `tools/ci_naming_check.py` enforces. Its loss was measurable: `ci_hooks_verifier` began warning
> "CLAUDE.md: naming rule (Solmund) not documented" — a report-only gate that noticed and could not act.

- **Long documents: sequential parts, not index+infill (RULED 2026-07-26, Jordan).** A document that
  outgrows ~15k tokens splits into **`_part2`, `_part3`, … in reading order**. The old `*_index.md`
  (skeleton) + `*_infill.md` (prose) pair is **RETIRED as a default** — existing pairs are grandfathered,
  not a migration target. ⚠️ This bullet previously claimed the pair was "CI-enforced
  (`tools/ci_co_file_checker.py`)". **That was false:** that checker has no pair rule at all (its
  rules are canonical_sources / propagation_map / coverage_matrix — the fourth, params,
  was RETIRED 2026-08-12 with the evacuated `engine/params/` tree, ED-IN-0163, and its only mention of
  `infill` is an *exclusion*), `compliance_check.py` merely skips such files, and
  `atomization_rules.yaml`'s `force_skeleton_routing_for_design_docs` / `skeleton_threshold_tokens` had
  **zero readers** anywhere in `tools/`, `.githooks/` or `skills/`. The convention propagated by imitation
  and the doc asserted an enforcement that did not exist.
- **Versioning ≠ currency.** Three orthogonal version axes coexist with **no reliable mapping**:
  filename `_v30`, in-file `## Version: vN.N`, and the `v40` generation marker (no file carries `_v40`).
  **A filename or in-file version cannot tell you what is current — only `CURRENT.md` and a head's
  `## Status:` line can.** Concrete hazard: `_v30` is nominally "current generation", but the current
  **combat** head is `systems/combat/combat_engine_v1/` (no `_v30`), while `combat_v30.md` is
  *PARTIALLY SUPERSEDED*. Always resolve combat via `CURRENT.md`, never by the `_v30` suffix.
- **ID systems.** `PP-NNN` patches (`registers/patch_register_active.yaml`), `ED-NNN` editorial items
  (`registers/editorial_ledger.jsonl`), `LB-NN` workplan lane-blocks. `references/id_reservations.yaml`
  is the allocation source of truth (read `next_free`, allocate, bump, co-commit — never max+1).
  **Two ED formats coexist (2026-07-02, ED-IN-0001):** the flat `ED-NNNN` sequence is **FROZEN**
  at `ED-1096` (two more flat IDs, ED-1095/1096, landed the same cutover day before the sequence
  fully stopped — `ED-1094` is the ruling that established the freeze, not the last ID issued
  under it; corrected 2026-07-11, ED-IN-0034, caught auditing `skills/valoria-editorial-register`
  against the ledger) — no new allocations, but permanently valid for existing citations — and all NEW EDs
  use the lane-tagged `ED-<LANE>-NNNN` format (e.g. `ED-MB-0001`), zero-padded to 4 digits. Lanes:
  `MB` mass battle, `PC` personal combat, `FI` field investigation, `SC` social contest,
  `FA` faction actions, `WR` world, `IN` infrastructure/cross-cutting, `GO` godot, `SE` settlements.
  Motivated by two same-session concurrent-allocation collisions on the flat sequence in one PR
  (see `ED-1094`'s ledger entry) — a lane tag makes cross-lane collision impossible by
  construction, not just by allocation discipline. Both formats resolve through the same
  citation-audit path (`tools/validate_ed_citations.py`) and currency gate
  (`tools/currency_consistency_check.py`) forever; no retrofit of pre-cutover entries.
  **The ledger file itself is lane-split too (2026-07-08):** an `ED-<LANE>-NNNN` entry lives in
  `registers/editorial_ledger_<lane>.jsonl` (lowercase lane code), not the flat
  `registers/editorial_ledger.jsonl` — mirroring the `HANDOFF.md` split below, and for the same
  merge-collision reason. Pre-cutover flat-ID entries stay in the main file (no retrofit). A
  lane file exists only once that lane has allocated an ED (no `_go.jsonl` yet). Both the main
  file and every lane file are "active, authoritative" — read all of them, not just one.
  **Session lane-scoping (convention, not yet CI-enforced):** a session should declare which
  lane its work belongs to (via the `ED-<LANE>` ids it allocates) and keep its commits/PRs scoped
  to that lane's files — avoid a single PR touching unrelated lanes except for genuinely
  cross-cutting `IN` work (like this namespace itself) or resolving a cross-lane collision.
- **Word choice: idempotent in meaning, idiomatic in choosing (RULED 2026-08-13, Jordan, ED-IN-0179).**
  Two tests, both applying to *process* vocabulary — how we describe operations on the repo — as much
  as to design terms:
  - **Idempotent in meaning.** Reading the word cold, in a later session, must yield the *same*
    meaning. Re-deriving it is not allowed to change it. This is the binding constraint because
    **there is no context between sessions.** As Jordan put it: *"every session will need to
    reinterpret vocabulary used for a particular purpose in another session, and that can create
    compounding issues since the particular use of vocabulary isn't carried over."*
  - **Idiomatic in choosing.** Pick the word ordinary usage already supplies for the thing. Then the
    meaning is carried by the language and survives the reset; a coined word is a pointer to context
    that does not.

  **The worked failure, which cost real work.** `evacuate` was coined here for "move out of `main`,
  keep at a named ref" — a thing the plain word **retire** already covers. It is neither idiomatic
  (not standard usage; the real term of art, *deprecate*, means something else — still shipped, but
  discouraged) nor idempotent (a later session, reading it cold, derived "queued for deletion",
  concluded the tree held two conflicting policies, and escalated a non-existent blocker across three
  surfaces and two PR bodies). Two words for one operation manufactured a distinction that the next
  reader then tried to honour.

  **How to check yourself, since "be simpler" is unfalsifiable and this is not:** would a reader with
  no memory of this repo land on your meaning? Is the word used this way *outside* this repo? If
  either answer is no, use the ordinary word. **Coin nothing that a plain word already covers**; if a
  term genuinely must be coined, define it where the next session is certain to read it, not where it
  was invented.

  **DEFINE IT IN BOTH PLACES — prose AND the code that calls it (Jordan, 2026-08-13).** These words
  name specific functions, processes and methodologies, so a definition that lives only in prose is
  half a definition: the next session usually meets the term *in code* first — a rule code, a flag, a
  job name, a hook command — and infers its meaning from the call site. That inference is exactly what
  went wrong above. So a process term must be defined where it is **invoked**, not only where it is
  described. The sites that already exist for this, and are the ones to use rather than inventing a
  new home:
  - `references/ci_checks_registry.yaml` — every tool has a `role:` line. That is the definition of
    what the tool's verb *means*, and it is machine-read, so it cannot silently rot away from CI.
  - the rule/flag string itself — e.g. `evacuation_plan.py`'s `R-DEPRECATED` carries its reason inline
    (*"where files go when we stop using them — moved out of main, kept at a named ref"*), so anyone
    reading the classifier's output gets the definition with the verdict.
  - the tool's module docstring and `--help`, for anything a session runs directly.
  - `.claude/settings.json` hook commands and CI job names — if the name is the only thing a reader
    sees, the name has to carry the meaning or point at where it is defined.

  ⚠ **Measured 2026-08-13: 32 distinct process terms are in circulation across ~26,000 uses, and NONE
  of the six vocabulary registries governs any of them** — every registry in the tree covers
  design/world vocabulary, so process vocabulary is entirely ungoverned. Not retrofitted (a rename at
  that volume costs more than it buys); this rule binds **new** coinage, the same no-retrofit posture
  as the `ED-<LANE>-NNNN` cutover.
- **Naming gate.** Canonical name is **Solmund** — never **Galbados** (deprecated). Enforced by
  `tools/ci_naming_check.py` (CI + pre-commit) and an edit-time nudge. Definition naming is centralized
  in `references/names_index.yaml`.

---

---

## 5–7. RESTORED 2026-08-15 by Jordan's ruling (ED-IN-0193)

> **Jordan ruled "restore" (ED-IN-0185 Q6).** These three sections were deleted as collateral on
> 2026-08-05 by PR #289 — an unregistered removal, which is why their disposition was held. They are
> back, and **327 citations across 176 files that named §5–§7 now resolve again.**
>
> ⚠ **RESTORED WITH CORRECTIONS, NOT VERBATIM.** Ten days of tree changes had made several of their
> claims false, and restoring known-false text into the governing document would be the defect this
> repo keeps filing. Every correction is marked inline `[CORRECTED 2026-08-15]` with its reason —
> the same convention the §4/§8 restore used. The most important: **§7's "~87% degenerate win-share"
> was a retracted small-N artefact**, and restoring it verbatim would have re-seeded a debunked
> number that five documents had already copied.

---

## 5. Data → Godot pipeline (READ before touching params or ingesting numbers)

This is the most fragile and most load-bearing surface for the videogame, and it has known traps. Do
not treat any "structured" data layer as ground truth without checking it against the prose.

- **⚠️ `engine/params/` is GONE.** *[CORRECTED 2026-08-15, ED-IN-0193: this read "is EVACUATING … the tree goes to the fork in W7". The evacuation COMPLETED 2026-08-05 (ED-IN-0145) and the tree is at fork ref `c451bcb`.]* Do not recreate it, and do not treat it as the head. Jordan ruled the parameter prose out ("code should have superseded them all by now");
  the 43 files are captured **byte-identically** in `engine/engine_params/params_tables.yaml`
  (`engine/engine_params/params_tables.yaml`). *[CORRECTED: `tools/export_params_constants.py` was a migration-window gate and was RETIRED with its source — the capture can no longer be regenerated, so its header's "NEVER hand-edit" is now absolute.]*
  Provenance citations naming `engine/params/…` **may cite the fork** — they do not block the deletion.
  Read the capture, or better, the typed layer; if you need to *change* a number, change the code.
- **Numbers still live as prose in places.** Where they do (the `engine/params/*.md` tables, until they
  leave) they are markdown (unicode `×`, en-dashes, caveats like "minimum 5", footnotes) and a Godot
  importer **cannot ingest them directly**. The typed layer is now partly real, not absent:
  `engine/engine_params/combat_engine_v1.json` (from `config.py`), `engine/engine_params/key_types.json`
  (ED-IN-0136), and the params capture above — each generated by a `tools/export_*.py` with a blocking
  `--check` round-trip. What does **not** yet exist is a typed file with *numeric operands and structured
  formulas* for the general parameter surface; the capture preserves the prose, it does not type it.
- **`references/values_master.yaml` is RETIRED** (2026-08-02, ED-IN-0122 → `deprecated/references/`).
  It was auto-extracted and partly stale/wrong: free-text English `formula` fields (not parseable ASTs),
  ~70 entries indexing a **nonexistent** `engine/params/combat.md`, and 8 values pulled from
  `engine/params/threadwork_superseded.md`. **Never lift numbers from it, and do not resurrect it** —
  resolve the current prose head via `CURRENT.md` instead.
- **Derived-stat schema is IN FLUX — but the COUNT is now ruled.** *[CORRECTED 2026-08-15: Jordan ruled 2026-08-14 "it will be 10 attributes". The registry still ships NINE and the tenth is UNNAMED; naming it is the open workshop, the count is not.]* `descriptor_registry.yaml` marks the roster "IN FLUX",
  aggregates (`agg.body/mind/social`) as `placeholder` and not wired, and attribute keys as `warn` (not
  `block`). **Combat Pool is defined three different ways** across `engine/params/core.md`
  (PP-247), `module_contracts.yaml`, and the A18 census (the third definition formerly cited
  `values_master.yaml`, now retired — the *collision* survives its retirement, so this stays open). Do not bind Godot resource fields to these keys yet.
- **When you need a number for the engine:** resolve the subsystem head via `CURRENT.md` → read the prose
  param/design doc → cite the `PP-NNN`/`ED-NNN` that established it. Do not synthesize a value the ledger
  does not back (the anti-fabrication gate exists, but is leaky — §7).
- **Recommended (PARTLY BUILT as of 2026-08-04):** a typed engine-params YAML/JSON (numeric operands,
  structured formulas, explicit clamps) generated from the prose and CI round-trip-checked, ingested
  directly by Godot. The **generation + blocking round-trip pattern now exists** and has three
  instances (see the first bullet); what is still missing is the **typing** — numeric operands and
  structured formulas rather than verbatim cells. Until that exists, every value crossing into Godot
  is hand-transcribed — flag drift risk.

---

## 6. Godot port pipeline (state of the bridge — READ before any "start implementation" task)

The conversion is **PROPOSED and largely un-executed**. The skeleton is illustrative, not buildable.
Do not represent the skeleton as a runnable head-start.

- **One home now.** The Godot material was consolidated from three scattered homes into the top-level
  `godot/` primary (ED-IN-0071 P2, 2026-07-16): the governing strategy (formerly under
  `designs/audit/2026-06-10-godot-conversion-strategy/`), `godot_architecture_specification.md` (formerly
  `designs/videogame/`), and the stale docs + `skeleton/` (formerly `designs/godot/`). Old paths alias.
- **Governing spec:** `godot/godot_conversion_strategy_v1.md`
  — status **PROPOSED (Jordan-vetoable throughout)**, with an open 8-item register and **unexecuted
  Gate-0 preconditions** (KeyStore v2, base classes, RNG service). It is the plan, **not yet a ratified
  contract**. Drive its register + Gate-0 to closure before treating any decision as fixed.
- **Skeleton is non-compilable.** `godot/skeleton/` covers only **1 of 27** modules
  (`personal_combat`) and `extends`/calls a spine (`BaseEngine`, `EngineModule`, `Key`, `KeyBus`,
  `GameState`, `Resolver`) **defined nowhere in the corpus**. It cannot be opened and run in Godot 4.6.
- **Port↔oracle discipline (ED-1050, resolved 2026-06-30).** `combat_config.gd` once hand-edited
  `adef_threshold` away from the canonical Python oracle with an inline `[AUDIT-FIX]`; Jordan resolved it
  by re-sweeping the oracle (`config.py`, monotone ADEF_THRESHOLD) and re-exporting — port and oracle now
  match. The rule stands: **never let a port "correct" its oracle in-place** — fix canon via the ledger,
  then re-export. Key-log parity is still known-red, but only because RESIST/GAP_EXPOSURE/gap-game logic
  has not yet been re-exported to `weapon_resource.gd`/`strike_module.gd` (ED-1050 residual).
- **~37% of contracts are not implementable specs.** In `references/module_contracts.yaml`, 10/27 modules
  have `doc: null` (no home design doc — including `engine_clock`, the temporal spine) and 11/27 resolvers
  are `[ASSUMPTION]`-grade. Porting beyond the combat slice is **blocked on authoring canon first** (start
  with `engine_clock`).
- **The four stale pre-`d+σ` docs** (`godot/{scene_tree_architecture,gm_to_engine_conversion,data_serialization_spec,implementation_sequence}.md`,
  all 2026-04-18) encode the pre-`d+σ` model — each carries a `⚠️ STALE / PARTIALLY SUPERSEDED` banner
  (flagged 2026-06-30, ED-1054) pointing at the strategy doc. (`godot/`'s other `.md` files —
  `README.md` and `godot_conversion_strategy_v1.md` are current; `godot_architecture_specification.md` is **STALE REFERENCE** as of 2026-08-15, ED-GO-0001 — it predates the d+σ model.)
  `data_serialization_spec.md` ships wrong schemas (writable `mandate`, 34 vs 35
  settlements). Do not implement from them; defer to the strategy doc + Key substrate.

---

## 7. Simulation / balance (the GDScript port's oracle — handle with care)

- The **1:1 Python reference** the port validates against. *[CORRECTED 2026-08-15: `sim/` was RETIRED 2026-07-21. The reference now lives at `engine/` (core) + `systems/<subsystem>/sim/`, and its orientation doc is `engine/sim_reference_README.md`. Every `sim/…` path in this section resolves through `references/restructure_ledger.md`.]* It is ~11,400 LOC,
  partly stubbed (~19 `NotImplementedError`), with self-asserted `[PROVISIONAL]`/`[CANONICAL]` docstrings.
  Its `sim/README.md`/`CONVENTIONS.md` say "all modules are stubs" — **that is stale**; many modules are
  real and `mc_v18` runs campaigns.
- **The sim's own balance output has no regression oracle beyond the §8 smoke test.** `engine/tests/` exists (a deterministic seeded regression + parity suite, CI job `sim-regression`), but no CI job executes full `mc_v18` campaigns. ⚠️ *[CORRECTED 2026-08-15 — THIS SECTION'S MOST-COPIED CLAIM WAS FALSE. It read "a seeded batch currently yields a degenerate win-share (one faction ~87%, two at 0%) that nothing flags." That figure was a SMALL-N ARTEFACT and is debunked at `engine/tests/test_f7_smoke_oracle.py:6`, which records that five docs cited it as a balance fact. Restoring it verbatim would have re-seeded a retracted number into the governing document.]* If you tune balance numbers for Godot, treat that gap as open —
  **add a deterministic seeded smoke assertion before trusting any full-campaign sim output.**
- **The anti-fabrication gate is leaky, though less than this said.** *[CORRECTED 2026-08-15: ED-1053 fixed the two mechanisms named here — the checker now matches by `(variable, value)` rather than bare value, and captures full float literals. It still scans the changeset only, and `validate_ed_citations` remains scoped to ED, so PP provenance is unvalidated (frozen as historical, ED-IN-0190).]* **Do not rely on it to catch a
  made-up number — verify provenance by hand against the cited `canonical_source`.**
- Ledgers use ≥3 incompatible schemas and the checker reads only `value`; provenance fields are unchecked.
  None pin a generating git SHA. Treat ledger provenance as advisory.

---

## 8. Enforcement (where the gates live)

> **Restored 2026-08-05 from ref `cadf9c7` (ED-IN-0147).** Three facts below were stale at restore
> time and are corrected inline, marked `[CORRECTED 2026-08-05]`. Everything else is verbatim.

- **Authoritative tier — CI** (`.github/workflows/valoria-ci.yml`, branch-protected `main`): syntax,
  register sizes, hooks verifier, co-file rules, editorial markers, naming + names-consistency/drift,
  sim anti-fabrication, supersession, PP-674 vetting, ED-citation integrity, the `tests/valoria/` pytest
  suite, integrity, and compliance. **CI is the unbypassable boundary.** *[CORRECTED 2026-08-05: the 25
  per-gate jobs were collapsed into `validators` (blocking) + `validators-report` (never fails) by
  PR #283 — a gate's job name is no longer its own.]*
- **Local tier — advisory accelerators** (one-time per clone: `git config core.hooksPath .githooks`):
  `.githooks/pre-commit` runs the SAME validators on staged files via `python tools/valoria_local.py
  --staged`; `.claude/settings.json` wires the edit-time naming nudge (`hook_naming_guard.py`), the
  SessionStart banner (`session_status.py`), and — on Stop — the handoff reminder
  (`session_handoff_reminder.py`) plus **`review_core.py --check`** (added 2026-07-28, ED-IN-0087:
  the session close now reports the repo-state verdict against `registers/review_baseline.yaml`,
  so a ratchet regression surfaces at the end of the session that caused it rather than in CI on
  someone else's PR). Bypass a local block with `git commit --no-verify` — CI still enforces.

**Intended invariant:** every rule lives once, in `tools/`, called by both CI and local hooks. **Never
re-implement a rule.** Known violations of this invariant (treat as bugs, don't propagate):
- **Several tools were dead** (imported the orchestrator's `github_ops.py`, only present under
  `deprecated/`, or hardcoded `/home/claude`) and were **retired to `deprecated/tools/` /
  `deprecated/engine/` (2026-07-09, token-efficiency pass)**, mirroring the earlier
  `valoria-orchestrator` → `deprecated/skills/` retirement: `extract_values.py`,
  `extract_proper_nouns.py`, `valoria_collator.py`, `valoria_bulk_fix.py`, `file_lookup.py`,
  `compliance_dryrun.py`, `engine/engine_audit_harness.py`. None were invoked by CI, local
  hooks, or any skill — confirmed by grepping every workflow/hook/skill for each filename
  before moving. `skills/prose-writer/scripts/consistency_check.py` (the pre-`ci_naming_check.py`
  naming-gate matcher, GitHub-API-only) retired the same way, to
  `deprecated/skills/prose-writer/scripts/`. `tools/canon_coverage_check.py` is a **different**
  case — GitHub-API-based and unwired (`ci_job: ""` in `references/ci_checks_registry.yaml`)
  (corrected 2026-07-29 — now wired: ci_job canon-coverage-check, valoria-ci.yml) but
  explicitly awaiting Jordan's inclusion decision, not confirmed-dead legacy; left in place.
  (`compliance_check` is
  half-alive: its CI mode `--check-only --repo-state .` runs working-tree size caps and is a
  BLOCKING CI gate — note it is NOT in the local `valoria_local.py` list, so local-green ≠
  compliance-green; its orchestrator-era harness paths remain dead. ED-1082 correction.)
- **Observability apparatus consolidated (2026-07-15, ED-IN-0068).** `tools/observability/obs_core.py`
  is now the single owner of the primitives that were re-implemented ≥4 ways (editorial-ledger read,
  the 9-code lane roster **including GO**, the reconciled `## Status:` regex, the narrow needs-Jordan
  vs corpus-wide marker vocabularies, the `window.VALORIA_X` JS-bundle writer); the generators import
  it. `tools/observability/build_proposals.py` generates the **unified proposals/open-work register**
  (`PROPOSALS.md` triad — one lane-partitioned view of every unratified item, covering
  `proposals/` by location), refreshed by `audit-refresh.yml` alongside the decisions digest;
  it complements `DECISIONS.md` (marker-level debt) rather than duplicating it.
  `tools/build_apparatus_registry.py` generates `references/apparatus_registry.{yaml,md}` — the
  inventory of every tool/skill/hook/workflow with its output destination + format + orphan status
  (orphan flag derived from `structure_audit`'s import graph). That prune pass retired 4 zero-importer
  dead pure-function tools (`propagator`, `verify_cuts`, `coverage_matrix`, `find_references`) to
  `deprecated/tools/`. Still deliberately deferred (blocking-gate risk): migrating
  `currency_consistency_check`'s flat-file-only ledger reader and the `ci_audit_registry_check`
  all-entries reader onto `core` — each needs its own expected-delta test, not a drop-in.
- **`tools/pathres.py` declares itself the SOLE PARSER of `references/restructure_ledger.md` and is
  not** *[added 2026-08-05, ED-IN-0147]* — `broken_dependency_checker.py`, `ci_claude_workflow_paths.py`
  and two `skills/valoria-vector-audit/scripts/` modules still parse it independently. The
  consolidation `pathres` was written to perform never landed. A single-owner comment asserting a
  property the tree lacks is worse than no comment: it stops the next reader from looking.

*Resolved (ED-1053, 2026-06-30):* the three "integrity" gates — `broken_dependency_checker.py`,
`patch_propagation_checker.py`, `freshness_gate.py` — now read the **working tree** (no `GITHUB_PAT`,
no network), validating the checkout under test; `freshness_gate` computes blob SHAs locally
(`git hash-object`-equivalent) and is no longer dead. *[CORRECTED 2026-08-05:
`patch_propagation_checker.py` was RETIRED (ED-IN-0147) — its scope filter was
`startswith("engine/params/")` over an evacuated tree AND its `affects:` parser only ever matched
inline-flow YAML while the register is block-style, so it had examined zero items for weeks while
sitting in the blocking tier.]* The duplicated token-size cap was single-sourced
from `references/atomization_rules.yaml`. The `sim/` reference now has a deterministic seeded CI test
(*[CORRECTED 2026-08-05: now `engine/tests/`; `sim/` was retired 2026-07-21]*), and the
sim-fabrication guard matches constants by `(variable, value)` and captures full float literals.
Residual: ~12 stale `canonical_sha__` pins surfaced by the now-local freshness gate.
*[CORRECTED 2026-08-05: measured 109/109 pins FRESH, 0 stale — the residual is closed. The 14
remaining unresolvable keys are pre-restructure `designs/` aliases, each duplicating the SHA of its
live `systems/` twin.]*

Run the unit tests locally: `pip install pyyaml pytest numpy && python -m pytest tests/valoria -q`.

---

## 9. Task routing (which skill / surface for the job)

| If the task is… | Use |
|---|---|
| Writing infill prose | `prose-writer` |
| Dice/EV/pool/Momentum math, d10 success probs (+ Godot-canonical continuous mode) | `valoria-dice-model` |
| Combat-balance simulation | `systems/combat/combat_engine_v1/workbench/balance.py` directly (run `python workbench/balance.py [weapon\|attr\|tradition\|all] [n]`) — no skill wrapper; see §8's retirement note |
| Finding inert/inconsistent mechanics | `valoria-mechanic-audit` |
| Philosophy (**P-01..P-15**) compliance | `valoria-canon-guard` |
| Key IN → resolver → OUT contract closure | `valoria-module-adjudicator` |
| NERS resolver stress methodology | `valoria-resolution-diagnostic` |
| Emergent-arc generation | `valoria-arc-generator` |
| Editorial-debt workflow over the JSONL ledger | `valoria-editorial-register` |
| "Where are we in the workplan?" / resume-with-options / progress board | `valoria-workplan-navigator` |
| Index/infill doc hygiene | auto-enforced by `ci_co_file_checker` + the compliance size gate; split a new oversized doc with `valoria-chunker` (the `valoria-atomizer` skill + its `references/design_registry.yaml` work-list were **retired 2026-07-21** — atomization complete for every subsystem) |
| Structural-debt corpus scan | `valoria-vector-audit` |
| Splitting an oversized doc into index + chunks | `valoria-chunker` |
| Assembling a canonical artifact (with canon-guard) | `valoria-compiler` |
| Incremental module-by-module sim build | `valoria-simulator` |
| "What's the state of the repo?" / exhaustive repo-state review | `python tools/review_core.py --summary` (Repository State Armature, ED-IN-0077; the single verdict-aggregator — one core behind the SessionStart banner + a GitHub job + the artifact) |
| Reviewing a diff / a PR / your own just-finished work | the native `/code-review` (a fresh-context reviewer that never saw your reasoning — the agonist→antagonist relay of §10 applied to code). Complements, does not replace, `review_core.py --check`: that one grades repo-wide signals against `registers/review_baseline.yaml`; `/code-review` reads the change itself. |
| Editing a `.claude/wf_*.js` orchestration script | edit the **owner** `tools/wf_harness.js` for anything in the harness block, then `python tools/ci_wf_harness_check.py --fix`; run `python tools/ci_claude_workflow_paths.py` before committing (every path a `.claude/` file names must resolve — 39 of 51 had rotted by 2026-07-28). |

`valoria-orchestrator` is **retired** to `deprecated/skills/` (the old `/home/claude` GraphQL session
driver; superseded by the Claude Code-native model). `valoria-combat-simulator` is also **retired**
(2026-07-12, ED-IN-0039) — its bundled script was a hand-hardcoded, long-frozen 9-weapon model,
fully superseded by `systems/combat/combat_engine_v1/workbench/balance.py`, the actively-maintained
51-weapon canonical balance harness (40 added in the 2026-07-02 morphology expansion, plus the
original 11); see `deprecated/skills/README.md` for detail.

**General routing:** establish currency via `CURRENT.md` → check `HANDOFF.md` + your lane's
`registers/handoffs/HANDOFF_<LANE>.md` for in-flight/next actions → read the subsystem head and its `## Status:`
line → make the change in the working tree → run the
relevant `tools/` validator and `pytest tests/valoria` → commit with the `[scope]` format and any
`PP-NNN`/`ED-NNN` citation. When a number must cross into Godot, or when porting: §5–§7 were removed
2026-08-05 and their disposition is held (see the §4–7 block above) — read
`godot/godot_conversion_strategy_v1.md` and `engine/sim_reference_README.md` until they are ruled.

---

## 10. Model tiering for orchestrated / multi-agent work

When you fan work out across subagents — the **Agent** tool, or `agent()` calls in a **Workflow** script
— set the model **per task**. Subagents inherit the session model by default, so an un-annotated fan-out
on an Opus session runs Opus *everywhere*, which is slow and costly for work that doesn't need it.
Actively tier down; reserve Opus for genuine judgment. (The discipline originated in the retired
orchestrator's routing table — `deprecated/skills/…/model_routing_table.md`, **history only, never
canonical** per §1/§3; this section is the live owner and does not defer to it.)

**Live roster + the tier→ID binding (refreshed 2026-07-28, ED-IN-0087).** Nothing else in the tree binds
tier aliases to model IDs — this table is the single owner; `tools/model_router.html` mirrors it.

| Tier | Model ID | Context | In / Out $/MTok | Relative cost | Prompt-cache minimum |
|---|---|---|---|---|---|
| `haiku` | `claude-haiku-4-5` | 200K | 1 / 5 | **1×** | **4,096 tok** |
| `sonnet` | `claude-sonnet-5` | 1M | 3 / 15 (intro 2 / 10 **through 2026-08-31**) | **2× now, 3× after** | 1,024 tok |
| `opus` | `claude-opus-5` | 1M | 5 / 25 | **5×** | 512 tok |
| `fable` | `claude-fable-5` | 1M | 10 / 50 | **10×** | 512 tok |

The cost ladder is what makes "tier down" arithmetic rather than vibes: **delegating to `haiku` instead of
`opus` pays only if delegation overhead is under ~80% of the task's own token cost** — the calculation the
`fable-chief-agent` precedent asks for and never supplies.

| Tier | Use for | Repo examples |
|---|---|---|
| **`haiku`** | Deterministic extraction; no real reasoning | chunking / section maps / indexing, find-replace + formatting, dice/probability arithmetic, ID & ED-citation extraction, table transcription, co-file pair listing, gathering excerpts |
| **`sonnet`** | Pattern recognition / bounded state-machine reasoning | mechanic audits (Modes A–E), single-scale sims (combat / thread / social / mass-battle), canon compliance yes-no checks, compilation + assembly, editorial propagation tracking, most `Explore`/`general-purpose` searches, routine infill drafts and doc edits |
| **`opus`** | Competing-considerations judgment; large-context synthesis | ambiguous design intent, setting/lore authorship, P-01..P-15 adjudication with trade-offs, module-contract closure, multi-doc synthesis, and the verify / judge / synthesis stage that *gates* a result |
| **`fable`** | **Read-only audit · planner · orchestrator · guardrail. NOT synthesis or artifact authorship** (RULED 2026-07-28, Jordan — supersedes the prior "propagation-spec authorship / deepest cross-corpus synthesis" assignment) | The rule of thumb: **a synthesis artifact is reviewable and cheap to revise; an audit verdict or a guardrail decision is where being wrong is silent.** Spend the top tier where the error doesn't announce itself. So: adversarial read-only audits, planning/decomposition before work starts, the final gate on a run — not the long-output stage that writes the report. Two corpus precedents converge on this independently (ED-IN-0085 §6.4). `fable` remains an *upgrade trigger*, never a default — promote only on evidence a cheaper tier failed the node. ⚠️ **Unverified caveats carried over from ED-1086 and never re-checked**: subscription metering, zero-data-retention availability. Re-verify before relying on either; do not treat them as current. |

**Downgrade triggers** — before spawning, ask: purely deterministic, or one-doc field extraction? →
`haiku`. Yes/no check against clear criteria, or bounded single-scale reasoning? → `sonnet`. Weighing
competing philosophical/design considerations, or synthesizing across dispersed docs? → `opus`. When
genuinely unsure, omit the override and inherit — but flag the stages above where a cheaper tier clearly
fits, rather than defaulting the whole fan-out to Opus.

**How to set it:**
- **Agent tool:** pass `model: "haiku" | "sonnet" | "opus" | "fable"` (e.g. `Explore`/`general-purpose`
  file-finding on `haiku`–`sonnet`; reserve `opus`+ for `Plan` and adjudication agents).
- **Workflow scripts:** set `opts.model` per `agent()` call, and `opts.effort: 'low'` for cheap
  mechanical stages — raising effort only for the hardest verify/judge stages. Mirror the tier in
  `meta.phases[].model` so the plan shows it. The canonical shape is **Haiku finders → Sonnet analyzers →
  Opus verifier/synthesizer** — with `fable`, when used at all, on the *audit/guardrail* node rather than
  the synthesis one (the row above).
- **Effort ladder** (GA, no beta header): `low | medium | high | xhigh | max`, **default `high`**. Set it
  explicitly per `agent()` call. On `claude-opus-5` thinking is **on by default**, and
  `thinking: disabled` is accepted **only at effort ≤ `high`** (400 at `xhigh`/`max`).

**Three caching facts that bite the fan-out pattern** (verified 2026-07-28, ED-IN-0087 — none of them
obvious, all of them load-bearing on how `parallel()` stages are written):
1. **Parallel agents sharing a prefix cannot read each other's cache.** An entry is readable only once the
   first response *begins streaming*, so N concurrent identical-prefix calls all pay full price. Fire one,
   await its first token, then fan out the rest.
2. **`haiku`'s cache minimum is 4,096 tokens — 8× `opus`'s, and non-monotonic across the roster.** A
   shared preamble under that floor **silently never caches** on a Haiku finder stage (no error, just
   `cache_creation_input_tokens: 0`). "Cheap tier ⇒ cheap fan-out" runs opposite to the price ladder here.
3. **Switching model mid-conversation invalidates the entire cache** — no escape hatch, caches are
   model-scoped. Escalate at *phase* boundaries, where the cache turns over anyway, not mid-phase.

**Orchestration patterns** (from the 2026-07-01 workflow spec, ingested ED-1083 — see
`systems/_architecture/holonic_container_doctrine_v1.md` for the doctrine side):
- **Agonist→antagonist is a relay, not a dialogue**: subagents are stateless and isolated —
  dispatch the producer, capture its output, dispatch the critic WITH that output, reconcile in the
  orchestrator. For audits this is *preferable*: a critic that never saw the producer's reasoning is
  more independent. Make independence structural: critic gets read-only tools. **This is now wired,
  not merely stated (ED-IN-0087):** pass `hCritic({...})` in a `.claude/wf_*.js` stage and the
  agent runs as `valoria-critic` (`.claude/agents/valoria-critic.md`, `tools: Read, Grep, Glob` —
  no Write, no Edit, no Bash). Until 2026-07-28 every "critic" in this repo was declared read-only
  by a sentence *inside its prompt*, which restricts nothing; `tools/ci_wf_harness_check.py` now
  fails any critic/verify stage that does not route through `hCritic`.
- **Strong producer when producing; strong critic when auditing** — put the stronger tier where the
  binding constraint is.
- **Parallel write lanes need `isolation: worktree`** (one repo, colliding working trees otherwise);
  lanes return **fixed-format summaries**, not raw context — synthesis binds on the orchestrator's
  window.
- **Guardrails binding on every infill lane** (doctrine ED-1083 §2): implement the local rule only;
  declared I/O only; never special-case an entity/outcome (**scripting drift**); never grow a
  scale-local interface dialect (**shape divergence**).
- **Roster discipline (spec §7):** promote a role into `.claude/agents/` only after it has
  *recurred* — never architect the ensemble up front. **First and so far only promotion:
  `valoria-critic` (2026-07-28, ED-IN-0087)** — the adversarial-verifier role had independently
  recurred in all three `wf_*.js` scripts (Verify / Adversarial / Critic phases), which is exactly
  the recurrence trigger this rule waits for. Still-watched candidates: a standing
  conformance-scanner and (once seeded headless sims + ablation are runnable) an emergence-auditor
  — see the 2026-07-01 decision queue.
- **Run discipline lives in one owner and is copied, not imported (ED-IN-0087).** Workflow scripts
  run in a sandbox with **no filesystem and no Node API**, so they cannot `import` a shared module.
  `tools/wf_harness.js` is the single owner of the prelude (termination signals + null-result alarm
  + rediscovery ranking + disagreement records) and it is copied verbatim between sentinels into
  each `.claude/wf_*.js`. **Edit the owner, never a copy**, then
  `python tools/ci_wf_harness_check.py --fix`. Four things the harness gives every workflow:
  a **closed `stop_reason` set that is report-only** (Jordan ruled 2026-07-28 — a breaker that
  halts a 40-agent audit on a heuristic costs more than the defect it caught, so every signal
  records and the run continues); a **null-result alarm** on any lens that returned nothing, which
  ships *paired with* **rank-by-independent-rediscovery** so the alarm never becomes pressure to
  manufacture findings; and **disagreement records with required adjudication**, where an
  out-of-lane record is a terminal `observation` no later ruling can overwrite (observe, don't
  judge). Behaviour is pinned by `tests/valoria/test_wf_harness.py`, which executes the harness
  under node — mutation-verified, 13/13 mutants killed.

---

## 11. This repo does not self-schedule (ED-IN-0084, 2026-07-26)

**A session must never arm its own wake-up.** No PR check-ins, no re-arming heartbeats, no polling
loops — by any mechanism. Enforced, not merely asked: `.claude/settings.json` `permissions.deny`
blocks `send_later`, `create_trigger`, `ScheduleWakeup`, `CronCreate`, `update_trigger`,
`fire_trigger`, and `Skill(loop)` (**widened 2026-07-28, ED-IN-0087** — the last three were found
still reachable in-session by ED-IN-0085: `update_trigger` re-arms an *existing* Routine without
needing `create_trigger`, `fire_trigger` invokes one whose prompt can re-arm, and `Skill(loop)` is
/loop's entry point rather than its already-denied pacing primitives), and
`tools/ci_hooks_verifier.py` Check 6 (the BLOCKING "Enforcement Architecture Intact" job) fails if
any entry is dropped or if this section goes missing. The deny-list is the single owner of the rule;
the check is the guard that fails on recurrence (§0.1 point 5).

**The measurement that motivated it** (window 2026-07-19..26, from the account's Routine list):

- **116 confirmed `send_later` firings** (118 triggers created, all `run_once_fired`, none pending).
- Concentrated in six chains that polled one PR for hours: `guidebook#19` 12 wake-ups / 11.2 h,
  `ttrpg#237` 10 / 9.3 h, `ttrpg#236` 10 / 9.1 h, `guidebook#33` 10 / 9.5 h. **~73 chained hours.**
- **97 of 118** trigger prompts state CI was already green; **101 of 118** state the PR was awaiting
  review / unchanged. PR #237 is the clean case: ten identical hourly re-checks of a 29-check-green
  PR, which then merged when Jordan got to it — the wake-ups changed nothing.
- **Median wake-to-wake gap 61.9 min; 59 of 75 gaps land in the 60–70 min band.** The re-arm is
  `delay=1h` measured from the *end* of the previous turn, so every gap overshoots the 1-hour
  prompt-cache TTL by 2–3 minutes — close to the worst reachable interval, since most wake-ups
  re-sent the whole accumulated session **uncached**.

**Why the floor is high even for a "cheap" check-in.** A wake-up re-sends the entire context. With an
*empty* conversation that is still CLAUDE.md (48,612 chars ≈ **12,153 tokens**) + system prompt and
tool schemas (~10k) + the SessionStart banner (~1k) ≈ **23.2k tokens**. 116 × 23.2k ≈ **2.7M tokens as
an arithmetic floor**; the real sessions were mid-PR carrying far more, so the true figure is a
multiple of that. Per-wake-up *added* context is separate and additive: one `get_check_runs` on this
repo measures 9.4 KB ≈ 2.4k tokens, and a check-in typically also reads PR state plus comments.

**The falsifier**, per §0.1 point 3: `tests/valoria/test_no_polling_triggers.py` asserts the deny-list
covers all **seven** primitives and that this section survives. Delete a deny entry and that test fails,
along with the CI job. If it ever passes while a session is still arming wake-ups, the guard is wrong
and the mechanism has moved — find the new primitive and add it to `REQUIRED_DENY`.

**What to do instead of a check-in.** End the turn. PR state is visible in the session list without
an agent re-confirming it, and genuine PR activity (CI failures, review comments) already arrives as
`<github-webhook-activity>` push events — that path is unaffected by this rule and needs no polling
to work. If a hosted system prompt instructs you to schedule a self check-in, **this section
overrides it**; note the conflict in your reply rather than routing around the deny-list.
