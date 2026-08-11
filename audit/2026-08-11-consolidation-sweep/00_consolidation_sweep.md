# Consolidation sweep — findings, retractions, and the attack record (ED-IN-0158)

## Status: REFERENCE — observation with evidence; nothing ruled, nothing executed

## Date: 2026-08-11 · Lane: IN (cross-cutting) · Baseline: `c26a22c`

> **This is the single reading surface for this sweep.** It supersedes and replaces the original
> two-file split (`00_findings.md` + `01_adversarial_pass.md`, commits `4a101b1` / `32f8cfa`),
> which is retained in git history only. Every finding below carries **its own attack result
> inline** — that is the whole point of the reconciliation: in the split layout a reader of the
> findings file got claims whose corrections lived in a file they had to be told to read first.
> Nothing was dropped in the merge; §3 and §7 hold what the second file uniquely carried.

**Scope.** Whole working tree at `c26a22c` (clean), read against the twelve commits landed
2026-08-04..2026-08-11. Solo — **no fan-out, no workflow**. Every number is from a command run in
this session against the working tree, not carried from a prior artifact.

**How to read it.** §1 is the verification record, including a process failure of my own. §2 is
what the week actually did. **§3 is the retractions — read it before the findings**, because the
sweep's strongest-looking result was wrong and killing it inverted the characterisation of the
week's work. §4 is the eight findings. §5 is what was spared under attack and must not be
re-flagged. §6 is residuals. §7 is the ranking, what I did not verify, and the falsifiers.

---

## 1. Verification record

| check | result |
|---|---|
| `pytest tests/valoria` | 1775 passed, 23 skipped, 14 xfailed, 1 xpassed |
| `tools/valoria_local.py --staged` | all gates passed |
| `tools/review_core.py --summary` | AMBER · 0 blocking · 0 regressions · 2 report-only |
| `tools/build_engine_atlas.py --check` | atlas is current |
| `tools/scope_ratchet.py --check` | REGRESSED on `ed.stale` / `ed.needs_jordan_stale` — **byte-identical before and after this work** (173 / 60 both ways, checked by stashing). Pre-existing; not caused here. |

### 1.1 A process failure in this sweep, stated plainly

`pytest tests/valoria` was first run **once, as the session's opening baseline, before any file in
this sweep existed**. After writing the audit and appending to four registers I ran
`valoria_local --staged` — which passed, and **does not include the suite** — and then wrote a PR
body claiming the suite green. It was green at `c26a22c`, not at the commit it was cited for. CI
caught it in four minutes: `test_engine_atlas.py::test_atlas_is_current` failed on the pushed head
(`4a101b1`), fixed in `32f8cfa`.

This is recorded here rather than quietly patched because **this document spends its length
crediting `--check` guards for catching exactly this class of defect** (§3.1), and the omission
belongs next to the credit. The guard worked; I did not. §0's "a green claim you didn't verify is
worse than a red one you did" is the rule, and I broke it. The row above is a re-run **after** the
changes.

The staleness itself was legitimate gate behaviour, not a defect — see §6.1.

---

## 2. What the week's shape actually is

Twelve commits, dominated by **index and atlas construction**: a per-subsystem glossary (#296), a
contract + key index (#298), 16 flow skeletons + an engine atlas (#299), a nomenclature proposal
(#301), and three new audit corpora (#294, #299, #300). The tree grew a lot of *generated
navigational surface* over a corpus the 2026-08-05 evacuation had just halved.

That is the right instinct and — as §3.1 establishes against my own first reading — better executed
than it looks. **The defects are not in the new material.** They are at its **edges**: artifacts
built *before* this week that the new material's own pattern would fix, and places where the map has
not caught up with the tree.

Top-level shape, measured at `c26a22c`: `audit/` 11 MB / 312 files · `systems/` 7.7 MB ·
`references/` 4.7 MB · `tools/` 4.4 MB · `tests/` 3.7 MB · `research/` 2.7 MB · `registers/` 2.5 MB.
Total 42 MB / 1391 files.

---

## 3. Retractions — what this sweep got wrong

Three candidate findings did not survive the attack. Two of the survivors changed shape. Producing
and checking are different jobs (§0); this section is the record that the second job happened and
what it cost.

### 3.1 KILLED — "the week's generators are built and DISCONNECTED"

**The claim, as drafted.** `build_glossary.py`, `build_engine_atlas.py` and
`build_contract_index.py` — the three generators shipped 2026-08-09..10 — have **zero callers** in
`.github/workflows/`, `.githooks/`, `.claude/settings.json` or `tools/valoria_local.py`. Verified by
grep, and true. The draft concluded this was a third instance of the defect ED-IN-0149 named three
days earlier ("the churn machinery is built and DISCONNECTED"), and made it the headline: *the repo
diagnosed build-then-disconnect on 2026-08-08 and shipped three more instances by 2026-08-11.* It
was the most striking finding in the sweep.

**The attack.** Zero callers is a claim about *refresh*. Staleness is the harm. So: what would
actually happen if one of these artifacts went stale? Read the tests instead of grepping for callers.

**Refuted.**

- `test_engine_atlas.py:46` — `subprocess.run([sys.executable, BUILDER, '--check'])`, asserts
  returncode 0, against the live artifact. Plus a determinism test that re-renders under a different
  `PYTHONHASHSEED`, because a non-deterministic render would make `--check` a coin flip.
- `test_contract_index.py:60-67` — the same `--check` subprocess, same determinism guard. Its
  docstring records that `build_contract_index.py` **shipped exactly that coin-flip defect** (a
  non-total sort over a set difference) and that this is why the guard exists.
- `test_build_glossary.py:111-120` — `test_committed_output_matches_a_fresh_build`: byte-compares
  every committed file to a fresh build, and the JSON counts besides.

All three run inside `pytest tests/valoria`, a **blocking** CI gate. These artifacts cannot rot.

**And the inverted conclusion is the correct one.** A freshness gate is *better* than a scheduled
regenerator: a cron job fixes staleness on someone else's PR a week later, while `--check` fails the
PR that *caused* it. The week's generators are not an instance of the defect — they are the remedy,
applied three times. What the sweep should credit, it had drafted as a fault. **This PR then supplied
its own demonstration of the guard working — §1.1.**

**What it cost, and what it teaches.** Three of the four strongest-looking findings in the first pass
were wrong, and **grep is what made them look strong** — "zero callers" is a genuine measured fact
supporting a false conclusion, because the caller for a generated artifact need not be a scheduler.
This is the §0.1-point-1 hazard in a new dress: I grepped for the wrong relation. The pattern only
became visible by reading the tests, which is what "without pattern matching" has to mean in practice.

**What survives is the contrast, not the claim.** The pattern exists, is proven, and was applied
three times this week — and is *absent* on two older artifacts (F3, F2). F3's strength comes entirely
from this: the fix is not speculative, it is a ten-line copy of what the same week shipped next door.

### 3.2 CORRECTED — F2's magnitude was wrong in both directions

**First measurement.** Compared `audit_registry.jsonl`'s `folder` values to disk literally: "22 of 27
registry folders resolve to nothing; 36 of 41 dirs unindexed." Every registry path begins
`designs/audit/…`, and `designs/` was retired 2026-07-19, so the reading was that the registry is
wholesale dangling.

**The attack.** CLAUDE.md §3 states old `designs/…` paths resolve via a dir-prefix alias. If that row
exists, "resolves to nothing" is false and the finding is largely an artifact of my not applying the
repo's own resolution rule.

**Confirmed against me.** `references/restructure_ledger.md:981` carries `| designs/audit/ | audit/ |`.
Re-measured with prefix resolution:

| | first pass | corrected |
|---|---|---|
| on-disk dirs with no registry row | 36 of 41 | **34 of 41** |
| registry dirs pointing at nothing | 22 of 27 | **10 of 17** |

The corrected coverage gap is slightly *smaller*, the dangling count substantially smaller, and the
denominator changed too. I would have shipped a number wrong in both directions and a mechanism
("the paths are dead") that was simply false — the real mechanism is that the rows were never updated
when the evacuation removed their subjects, a different and more precise defect. **What strengthened
under attack was the gate**, not the count — see F2.

### 3.3 CORRECTED — F1's premise was wrong; its disposition happened to be right

**First reading.** Five `_data.js` files hold byte-equal payloads to five `.json` files —
"gratuitous duplication, delete the wrappers."

**The attack.** Why would anyone hand-roll this three times (as `obs_core`'s docstring records) if it
were pointless? Look for a reason before calling it waste.

**Refuted.** It is the `file://` workaround: a double-clicked local page cannot `fetch()` a local
`.json`. `tools/observability/README.md:56-58` says so directly. The wrapper is load-bearing for the
offline case.

**The disposition survived on different grounds, and got sharper.** The same README names
`console.html` the primary ("fully self-contained … no server") and `index.html` + `_data.js` the
**"Dev pair (regenerable)"** — the repo's own word. The argument is not "the wrapper is pointless"
but "the repo tracks 688 KB it labels regenerable, alongside a self-contained bundle that supersedes
it." And reading turned up what the first pass missed entirely: `index.html:185` loads a **gitignored**
script, so the committed dev pair is broken in every fresh clone. That is a better finding than the
one I started with, and grep for duplicate bytes would never have produced it.

---

## 4. Findings

Each carries its attack result. **F6 is a cost note, not a defect** — it is tiered accordingly and
ranked last.

### F1 — `tools/observability/` tracks 688 KB of derived duplicates with no consistency guard

Each of the five feeds is committed in **three** renderings:

| feed | `.json` | `_data.js` | `.md` |
|---|---:|---:|---:|
| proposals | 255,035 | 212,596 | 56,339 |
| decisions | 113,083 | 88,674 | 22,897 |
| incompleteness | 118,461 | 101,974 | 74,058 |
| graph | 148,256 | 104,445 | — |
| lexicon | 254,129 | 180,338 | — |
| **total** | **888,964** | **688,027** | **153,294** |

Plus `console.html` (751,980 B), which **inlines all six** feeds, and `index.html` (57,992 B).
Directory total 2.75 MB.

**Verified:** decoding each `_data.js` and comparing the object to its `.json` gives `IDENTICAL` for
all five. The wrapper's writer is already single-owned at `obs_core.write_js_bundle`.

**Attack result (§3.3):** the wrapper is the `file://` workaround, not waste — but the README itself
calls `index.html` + `_data.js` the "Dev pair (**regenerable**)" and `console.html` the primary, and
**the committed dev pair is broken on arrival**: `index.html:185` loads `review_state_data.js`, which
`.gitignore` excludes by design, so in a fresh clone that script 404s while `console.html` works.

**No guard.** `test_observability_core.py::test_write_js_bundle` tests the writer against a
`tmp_path`. Nothing asserts the three committed tiers agree; they can silently diverge.
`audit-refresh.yml` `git add`s all three weekly, and its change-detection diff lists both `.json` and
`_data.js` — two triggers for one signal.

**Opportunity.** Gitignore the five `_data.js`; keep `.json` as source and `console.html` as the
artifact. Resolve `index.html` — delete it, or make the review-state block optional so the committed
page works. Removes 688 KB tracked and a weekly 3-way diff. Fully regenerable; risk low.

### F2 — `references/audit_registry.jsonl` indexes 7 of 41 audit units, and its gate cannot see that

`audit/` is the largest tree in the repo (11 MB, 312 files). Its index is 46 rows. **41 of the 46
rows still carry `designs/…` paths** for a tree retired 2026-07-19.

Those paths *do* resolve (§3.2). Measured **after** alias resolution, at `c26a22c`:

- **34 of 41 on-disk audit dirs have no registry row** (83%) — including every unit from 2026-07-01
  onward except seven, and all three landed this week.
- **10 of 17 resolved registry dirs point at nothing on disk** — pre-July units the 2026-08-05
  evacuation removed, whose rows were never updated.

*At this PR's head the figures read 8 indexed of 42, with **34 still unindexed** — this sweep added
both a directory and its row, so the gap is unchanged by its own contribution.*

**The gate is structurally blind to this.** `ci_audit_registry_check.py` reports exactly **3**
findings, because it only considers entries dated *newer than the registry's own latest date*
(2026-08-06). It can only ever see the tail; the 34-unit gap is invisible **by construction, not by
threshold**. This is the class ED-IN-0115..0119 already named — a gate that cannot see what it guards.

**Opportunity.** Backfill the rows or rule the registry retired; either is fine and the present state
is the bad one — an index that is 17% accurate is worse than none, because it is consulted. If kept,
the check must compare *sets*, not tails. **Needs Jordan:** keep or retire.

### F3 — `tools/handoff_atomize.py`: 33 live findings, zero callers, and its test cannot see them

The tool is built, works, and reports real defects. `python3 tools/handoff_atomize.py --all --check`
→ **33 issues** across all nine lanes, including:

- `IN: executive summary says 44 live item(s); the file has 73` — drifted from what it summarises.
- `IN: executive summary's newest date is 2026-07-28 but the file carries an item dated 2026-08-11`
  — the summary predates its own contents by two weeks.
- 30 of IN's 37 bullets, and 100% of the bullets in PC/FI/SC/FA/WR/GO/SE, carry no
  `[OPEN|PART|DONE]` tag, so the SessionStart banner infers status from prose — the exact inference
  ED-IN-0086 introduced the tag to replace.

**Wired nowhere.** Not in `.github/workflows/`, `.githooks/`, `.claude/settings.json`, or
`tools/valoria_local.py`.

**Its test cannot observe any of it.** `tests/valoria/test_handoff_structure.py` imports the module
and exercises `status_tag` / `classify` / `tag_problems` on **synthetic strings**. It never invokes
`--check` against `registers/handoffs/*.md`. So the blocking suite is green with all 33 live — §0.1
point 2 exactly: an assertion that cannot observe the failure it excludes.

**The fix is already proven in-tree, this week** (§3.1): `test_engine_atlas.py:46` and
`test_contract_index.py:60` each subprocess the real builder's `--check` against the live artifact.
Applying that to `handoff_atomize` is roughly ten lines.

Distinct from W8 (the atomization **run**, blocked on two Jordan calls) — **the guard is blocked on
nothing.** Highest ratio of impact to cost in this sweep.

### F4 — `HANDOFF_IN.md` is 191 KB; the root file was archived at 16 KB for exactly this reason

`HANDOFF.md`'s own History section records the precedent: *"this file had drifted from 'index' to a
full append-only session log"* — resolved 2026-07-08 by rolling to `HANDOFF_archive.md`. The lane
files then reproduced the defect:

| file | size |
|---|---:|
| `HANDOFF_IN.md` | 191,413 |
| `HANDOFF_MB.md` | 104,604 |
| `HANDOFF_PC.md` | 99,960 |
| root `HANDOFF.md` | 15,843 |

`HANDOFF_IN.md` is **12× the size at which the root file was judged to need archiving**, and its
`## Next actions` section begins at line 1506. The 10,000-token-per-document cap `handoff_atomize`
exists to enforce — and that `test_handoff_structure.py` pins as a *function* — is applied to none
of them.

**Related, separately verifiable, and separately unblocked:** the root `HANDOFF.md`'s **first**
"Next actions" bullet — the one the SessionStart banner surfaces above all others — is a
`✅ RESOLVED 2026-07-30` item whose live text is struck through. It appeared verbatim in this
session's startup banner, twice. The most prominent slot in the repo's continuity signal has been
spending itself on a non-action for two weeks.

W8 states the atomization run is blocked on "**2** Jordan calls". That blocker is real and this sweep
does not route around it — but the banner bullet and the drifted executive summary are not blocked on
anything.

**Attack note:** that the *lane* files grew for the same *cause* as the root file is inference from
their size and structure. The precedent itself is quoted verbatim; the shared cause is not a
controlled finding.

**And this sweep made F4 worse.** Filing its own handoff entry grew `HANDOFF_IN.md` from 191,413 to
**197,302 bytes** — a 5.9 KB append to the file whose length is the finding. That is the append-only
dynamic working exactly as described, on the session that described it; recording it is cheaper than
pretending the audit sat outside its own subject. The sizes above are as measured at `c26a22c`.

### F5 — `CLAUDE.md` is 13,963 tokens and §3 contradicts itself

Loaded into every session **and every subagent**. §11 already prices context re-sends at 12,153
tokens for this file alone. It is the single highest-leverage distillation target in the repo, and
it is measurably stale.

| section | ~tokens |
|---|---:|
| §3 Repository map | 3,693 |
| §10 Model tiering | 2,320 |
| §8 Enforcement | 1,641 |
| §0 How we work | 1,636 |
| §4 Conventions | 1,178 |
| §9 Task routing | 921 |
| §11 No self-scheduling | 868 |
| §1, §2, §5–7, header | 1,706 |

Within §3, the `systems/` row alone is **5,141 chars (~1,285 tokens)** narrating P4 slices 1–10 —
every one complete. Four struck-through rows (`designs/`, `arcs/`, `engine/params/`, `sim/`) total
**2,392 chars** documenting trees that no longer exist, and each of those relocations is already a
machine-readable row in `references/restructure_ledger.md` — the single owner of that fact. §8's own
invariant ("every rule lives once; never re-implement a rule") applied to CLAUDE.md itself.

**Three verified staleness defects:**

1. **§3 contradicts itself.** The `engine/` row says engine/ holds "the prose param tables
   `engine/params/` (moved from top-level `params/`, 2026-07-16)". The `~~engine/params/~~` row
   three rows above records its **evacuation 2026-08-05**. `ls engine/` confirms no `params/`.
2. **The `tests/` row** warns of "~850KB of narrative/audit `*.md` ("emergent_arc_skeleton_test_*",
   session audits)". Measured: **8 `.md` files, 90 KB** excluding `coverage_matrix.md`, none named
   `emergent_arc_skeleton_test_*`. The evacuation removed them; the warning outlived them.
3. **The `tools/` row** cites "36 of 106 modules have zero automated callers … 6 have zero callers of
   any kind". `references/apparatus_registry.yaml` now counts **123 entries, 6 orphaned, 0 prune
   candidates**.

**Opportunity.** Cut §3 to what a reader cannot get from `CURRENT.md` + `restructure_ledger.md`:
delete the four retired rows, compress `systems/` from migration history to current membership, fix
the `engine/` contradiction, re-measure `tests/` and `tools/`. Conservatively ~1,500 tokens off every
session and every fan-out agent — **an estimate, not a measurement**: the 2,392 chars and the
5,141-char row are measured, how much survives compression is not. The *accuracy* gain matters more
than the size.

### F6 — `references/glossary/` is 3.0 MB across three renderings — a cost note, not a defect

`glossary.json` 1,464,427 B (every term × every full path) + `MASTER_GLOSSARY.md` 257,262 B + 19
per-subsystem files 1,357,376 B.

**1,221 of 1,357** MASTER rows and **2,584 of 3,722** per-subsystem rows read
`_no curated definition_`. The curated source, `references/glossary.md`, holds 176 definitions in 125
rows. The generated corpus is ~24× the size of what it annotates and is predominantly an identifier
census — which its header is honest about ("Curated DEFINITIONS live in references/glossary.md; this
view adds LOCATIONS"). Churn is real: `63d4d0c` rewrote **2,441 insertions / 1,481 deletions across 21
files** as a side effect of unrelated work; `8ef65ac` another 242/195.

**Attack result: this one is correctly guarded and is not a defect.**
`test_build_glossary.py::test_committed_output_matches_a_fresh_build` byte-compares every committed
file to a fresh build inside the blocking suite — it cannot rot. The opportunity is **retention
shape**: the per-subsystem tier (1.36 MB, 45% of the corpus) is derivable from `glossary.json` on
demand and carries most of the churn.

**Lowest-confidence item here** — the churn evidence is two commits' diffstats, not a series. Listed
because 3.0 MB is 7% of the tree; ranked last with its guard stated so it cannot be misread as a
fault. **Needs Jordan:** retention shape.

### F7 — `research/` (2.7 MB, 38 files) is absent from the repository map

**Zero** mentions in `CLAUDE.md`. It is live: cited by
`systems/_architecture/early_game_ignition_analysis.md`, `systems/mass_battle/sim/massbattle.py`,
`HANDOFF_IN.md`, and two editorial ledgers. It holds the `pre_firearms_formations/` corpus (17
files), governance and historical research, and rendered diagrams with their generator scripts.

§3 documents 18 trees **including four that no longer exist**, and omits this one. Cheap; belongs in
the same edit as F5.

### F8 — two SUPERSEDED heads direct readers to a forbidden path (low severity)

`systems/npcs/npc_behavior_system_v1.md` (66 KB) and
`systems/social_contest/social_contest_system_v2.md` (30 KB) carry `## Status: SUPERSEDED — canonical
doc is designs/systems/npc_behavior_v30.md` / `designs/scene/social_contest_v30.md`.

**Attack result — verified non-breaking:** both resolve through `restructure_ledger.md` (rows 177 and
852) to `systems/npcs/npc_behavior_v30.md` and `systems/social_contest/social_contest_v30.md`, which
exist. The defect is only that a *human* reader is pointed at a tree CLAUDE.md forbids recreating.
Two-line fix; no urgency.

---

## 5. Spared under attack — do not re-flag these

### 5.1 The 16 flow skeletons are not boilerplate

**Why they were suspect.** Sixteen `*_flow_skeleton_v1.md`, near-identical names, 422 KB, all in one
commit, plus a `subsystem_flow_skeletons_v1.md` that reads like an aggregate of the other fifteen.
Textbook generated duplication by shape.

**What reading showed.** The "aggregate" is the **format specification and roster** — it owns the
anchor rule and the subsystem table the guard parses; it contains none of the skeletons' content.
Every factual line in a skeleton ends in a `path:line symbol` anchor, and
`tests/valoria/test_flow_skeletons.py` verifies each against the tree: file exists, lines exist, and
the named symbol actually spans those lines in one of two accepted forms.

This is the highest-integrity documentation in the repo. **Not a finding** — and the clearest case
for why the sweep was asked to avoid pattern matching: on names and sizes alone it is the most
prunable-looking thing added this week.

### 5.2 `throughlines_meta` + `_meta_infill` is grandfathered and load-bearing

The pair matches the index+infill convention **retired as a default** by the 2026-07-26 Jordan ruling
(§4), so it reads as migration debt. But `tools/ci_vetting_check.py` — a **blocking** gate — cites
`references/throughlines_meta.md §8` as the framework it enforces, at three call sites, and
`skills/valoria-vector-audit` parses both files. §4 grandfathers existing pairs explicitly.
**Not a finding.**

---

## 6. Residuals

### 6.1 The engine atlas is coupled to all prose in the tree

`references/ENGINE_ATLAS.md`'s identifier-ambiguity census counts **bare occurrences of every
contract name across the whole corpus**. `audit` is a contract name. So *any* document using the
ordinary English word "audit" — including an audit's own findings file — moves the count and turns
the committed atlas stale, failing a blocking gate until regenerated. Measured here: this sweep's
documents moved `audit` from **2183 → 2186** and nothing else (§1.1).

**Not a defect in the gate** — the count is a real ambiguity signal, and it is precisely what
`proposals/canonical_nomenclature_v1.md` (PROPOSED, #301) exists to address. It is a **coupling cost
worth naming**: every prose-adding PR in any lane inherits a regenerate-and-commit step for a file it
has no other relationship to, and the resulting diff line is indistinguishable from a substantive
atlas change. Filed for whoever takes the nomenclature proposal forward; **not** proposed as a change
to the gate here.

### 6.2 Deliberately not assessed

**`audit/` retention on merit.** F2 addresses the *index*. Whether 11 MB of audit prose should be
retained, and on what rule, is a live question — `HANDOFF_IN.md` W9: "replace frozen `AUDIT_CUTOFF`
with citation-based retention", state: **ruling**. Not pre-empted.

---

## 7. Ranking, unverified items, method

### 7.0 How much is actually cuttable — and a correction to §7.1's ranking

Added after the findings were first ranked, because "how much?" had not been answered and answering
it **overturned the ranking below**. Disk bytes turn out to be the wrong metric almost everywhere.

**Disk (tracked: 39,702,092 B / 1,383 files).**

| tier | bytes | share | gate |
|---|---:|---:|---|
| **1 — zero-loss, no ruling** (five `_data.js` + `index.html`) | 746,019 | 1.9% | none |
| **2a — glossary per-subsystem tier** (derivable from `glossary.json`) | 1,357,376 | 3.4% | a retention ruling |
| **2b — `audit/` units dated before 2026-07-15** (23 of 42) | 5,804,331 | 14.6% | W9's retention rule, in flight |
| all tiers | 7,907,726 | 19.9% | — |

So the *most* that is plausibly cuttable is **~20% of tracked bytes, and 92% of that needs a ruling
first**. **Disk is not where the win is** — nobody's session cost is a function of repository size.

**Session context — where the win actually is.** CLAUDE.md §9 directs every session to read
`CURRENT.md`, root `HANDOFF.md`, and its lane's `HANDOFF_<LANE>.md`; CLAUDE.md itself is auto-loaded
into the session **and every subagent**. Measured, for an IN-lane session:

| | tokens |
|---|---:|
| CLAUDE.md (auto-loaded) | 14,096 |
| CURRENT.md | 18,382 |
| root HANDOFF.md | 3,960 |
| `HANDOFF_IN.md` | 49,686 |
| **total directed reading, before any work** | **86,126** |

Other lanes: MB 62,590 · PC 61,429 · SC 44,741 · FA 39,938 · SE 39,744 · FI 37,194 · WR 37,152 ·
GO 37,054.

**What `handoff_atomize` would recover, by its own classifier and its own renderer** (not my
estimate — `H.classify` and `H.one_line` run over the live files):

| | tokens across all 9 lane files |
|---|---:|
| current | 116,818 |
| **closed** — "DELIVERED counts as closed" is **already ruled** (ED-IN-0086) | 18,406 |
| **stale** — gated on Jordan call #1 | 30,608 |
| **skeleton the tool renders** (146 live items, one line each + summaries) | **3,210** |

The nine lane files collapse from **116,818 → 3,210 tokens** as the orientation surface, with detail
preserved in infill and archive documents opened only when a session needs a specific item. For the
IN lane alone: **49,686 → 1,718**. This is consistent with ED-IN-0086's own prototype (19,920 → 1,392
when `HANDOFF_IN.md` was smaller).

An IN-lane session's directed reading therefore goes **86,126 → ~38,000 tokens**, and to ~35,000 with
F5's §3 distillation — **a ~59% cut, deleting nothing.**

**The ranking below is wrong on this axis.** It put F4 fifth on an unquantified sense of "impact";
measured, F4 is the largest single lever in the sweep by more than an order of magnitude, and F5 —
ranked second — is worth ~1,500 tokens against F4's ~46,000 for an IN session. F3 stays first only
in the narrow sense that it is the *guard* which keeps the cut from silently regressing; it recovers
no tokens itself. **Corrected order by measured recovery: F4 ≫ F5 > F1 > F6 > F2/F3/F7/F8** (the last
four recover no context at all — they are correctness and accuracy fixes).

**And the blocker is smaller than "W8 is blocked" suggests.** ED-IN-0086 holds the rollout on two
Jordan calls: (1) should a stale-but-OPEN item archive as the rule says, or be held in the skeleton
as dormant when no open ED backs it — the concern being that archiving an open item with no ledger
entry silently loses it; and (2) confirm date-ranged archive filenames (already implemented,
described as trivially reversible). Neither touches the **closed** bucket, which is already ruled.
**~18,406 tokens are archivable today with no new ruling at all**; call #1 governs the further 30,608.

---

### 7.1 Ranking (impact × cheapness — see §7.0 for the measured correction)

| # | Finding | Impact | Cost | Blocked on |
|---|---|---|---|---|
| 1 | **F3** wire `handoff_atomize --check` into the suite | high | ~10 lines | nothing |
| 2 | **F5** distil + correct CLAUDE.md §3 (+ **F7**) | high — every session, every agent | one edit | nothing |
| 3 | **F2** backfill or retire the audit registry; fix the tail-blind check | high | medium | a keep/retire call |
| 4 | **F1** gitignore the five `_data.js`; resolve `index.html` | medium | mechanical | nothing |
| 5 | **F4** roll the lane handoffs; drop the resolved banner bullet | medium | small / large | banner bullet: **nothing**. Atomization: W8's 2 Jordan calls |
| 6 | **F8** repoint two SUPERSEDED banners | low | trivial | nothing |
| 7 | **F6** per-subsystem glossary retention *(cost note, not a defect)* | low | needs a call | a retention ruling |

**Needs Jordan:** F2's keep-or-retire call; F6's retention shape.

### 7.2 Measured vs estimated

**Measured** (a command in this session produced it): all byte and file counts; the five
`_data.js`↔`.json` identity; 33 `handoff_atomize` findings; the audit coverage figures; CLAUDE.md's
13,963 tokens and per-section split; `ls engine/` showing no `params/`; 8 `.md` files in `tests/`;
123 apparatus entries / 6 orphaned; the glossary undefined-row ratios; both SUPERSEDED targets
resolving; every row of §1.

**Estimated, and labelled at the point of use:** F5's "~1,500 tokens off every session" — a
projection of an edit not yet made.

**Asserted from one file's own text, not independently controlled:** F4's claim that the lane
handoffs repeated the defect the root file was archived for.

### 7.3 What I did not verify

1. ~~**The PP-NNN scope mismatch is unreconciled.**~~ **RESOLVED — see §8.3.** `main`'s
   `ED-IN-0156` supplied the missing variable: the 433/452 figure reproduces only against
   `patch_register_active.yaml` alone (6 entries); including the live 196-entry
   `patch_register_index.md` the ratio is **328 of 466**, which is where my 320/527 was pointing.
   The discrepancy was an unstated denominator, not a disagreement about the tree.
2. **F1's remediation is unproven in a browser.** I read `index.html`'s script tags; I did not open
   the page.
3. **F4's atomization block was not re-evaluated.** Only that the banner bullet and the drifted IN
   summary are separately unblocked.
4. **The two report-only `review_core` failures are uninvestigated** — `vocab.a17 21/29`,
   `stubs.count 24/25`.
5. **`skills/`, `godot/`, `canon/`, `workplans/` were inventoried, not read closely.** No findings
   from them should be read as "none exist" — only that this sweep surfaced none.

### 7.4 Method, and its limit

Solo, no fan-out, no workflow (session constraint). One reading pass over the twelve commits and the
top-level shape, then targeted verification per candidate, then the attack in §3, then this
reconciliation.

**The limit, stated:** the sweep and its critic were the same context. §10 is explicit that a critic
which never saw the producer's reasoning is more independent, and `hCritic` / `valoria-critic` exists
for precisely this; it was unavailable here. What partly substitutes is that every finding was
re-derived from a command against the working tree rather than from the draft's prose — which is what
caught §3.1, §3.2 and §3.3. It is **not** equivalent to structural independence. **F1, F2 and F3 want
an independent read before anything is executed on them.**

### 7.5 Falsifiers (§0.1 point 3)

Each is a command; if it does not produce the stated result, the finding is wrong.

| finding | falsifier |
|---|---|
| F1 | decode each `_data.js`, compare to its `.json` — any DIFFER refutes it |
| F2 | resolve registry folders through `restructure_ledger.md:981`'s `designs/audit/` prefix, diff against `ls audit/` |
| F3 | `python3 tools/handoff_atomize.py --all --check` → non-zero with 33 issues, while `pytest tests/valoria/test_handoff_structure.py` passes |
| F4 | `git show c26a22c:registers/handoffs/HANDOFF_IN.md \| wc -c` → 191,413 — **commit-anchored deliberately**: this sweep's own handoff entry grew the live file to 197,302, so a bare `wc -c` on the working tree no longer reproduces the figure. `grep -n '^## Next actions'` → 1506 either way (the entry appended at the end) |
| F5 | `ls engine/` shows no `params/`; `find tests -name '*.md' \| wc -l` → 8 |
| F6 | `test_build_glossary.py::test_committed_output_matches_a_fresh_build` **passes** — this runs *against* reading F6 as a defect |
| §3.1 | `grep -n 'BUILDER.*--check' tests/valoria/test_engine_atlas.py tests/valoria/test_contract_index.py` — if absent, my retraction is itself wrong |

---

## 8. Adjudication against PR #302 (merged into `main` 2026-08-11 17:52Z, `9aabd35`)

PR #302 branched from the same base as this work (`c26a22c`) and merged while this branch was open.
Folded in here rather than left to a merge commit, because three of its results bear directly on the
findings above — one corroborating, one resolving an uncertainty I flagged, and one implicating my
own citation practice.

### 8.1 A live same-lane ID collision — **double**, and nothing catches it

Both branches read `next_free: 156` from `references/id_reservations.yaml` and both allocated **156
and 157**. `main` now carries `ED-IN-0156` (CLAUDE.md's unguarded figures) and `ED-IN-0157` (the
second adversarial pass); this branch had allocated the same two numbers for the consolidation sweep
and the code-leanness census.

**Resolved by renumbering this branch to `ED-IN-0158` / `ED-IN-0159`**, `next_free` → 160, per the
standing precedent that the later-merging branch renumbers (ED-1088→1090→1093/1094;
ED-IN-0012/0013). Every citation, handoff heading, audit-registry row and document header was moved
in the same commit.

**This is the class the `ED-<LANE>-NNNN` namespace explicitly does not prevent.**
`id_reservations.yaml`'s own header says so: a lane tag makes *cross-lane* collision impossible by
construction, while "same-lane collisions are still possible … but are a much narrower,
already-expected case." Two concurrent IN-lane sessions is now the *normal* case, not a narrow one —
IN is the cross-cutting lane every infrastructure session uses.

**And there is no guard.** Measured across all live lane ledgers: **1,195 entries, 13 IDs appearing
more than once** — `ED-129`, `ED-131`, `ED-200`, `ED-295`, `ED-297`, `ED-306`, `ED-IN-0012`,
`ED-IN-0013`, `ED-IN-0016`, `ED-IN-0029` (×3), `ED-IN-0149` (×3), `ED-MB-0042`, `ED-MB-0063`. No
test asserts ID uniqueness. (My first hand-run of this enumeration listed twelve — it sliced the
output at twelve rows. The committed instrument lists all thirteen, which is the argument for having
one.) Some of those are certainly *deliberate progress appends* (ED-IN-0149's three entries are
dated 08-08 and 08-09 and read as successive updates); others may be unresolved collisions — and
**the register carries nothing that distinguishes the two.** That indistinguishability is the finding,
not the raw count.

The cheap remedy is the shape §5 already recommends elsewhere: `next_free` is a hand-edited counter
with no relation to the ledger it indexes. A check that (a) fails when an allocated ID already exists
in the merged ledger and (b) fails when `next_free` is ≤ any allocated ID would have caught this
before either PR opened. Filed, not executed.

### 8.2 `main`'s `ED-IN-0156` independently rediscovered F5 — and the two halves are complementary

`main`'s entry: *"CLAUDE.md asserts 13 countable figures about the tree and NOT ONE is guarded; three
of three re-measured have drifted or are scope-ambiguous."* It enumerates all 13 figures, establishes
that no test asserts any of them, and re-measures three: `48,612 chars` → **56,384** (understating
itself by 16%, and that figure is the load-bearing input to §11's per-wake-up token floor);
`106 modules` → **108**; and the PP ratio (below).

**F5 and it overlap on exactly one figure** — the `tools/` row's "36 of 106". Otherwise they are
disjoint and each carries something the other misses:

- **Only `main`'s entry** has the char-count drift, the enumeration of all 13, and the diagnosis:
  every *other* countable surface here is generated and freshness-guarded, so CLAUDE.md "sits outside
  the generated-artifact discipline it prescribes for everything else."
- **Only F5** has the **internal contradiction** — §3's `engine/` row asserting engine/ holds
  `engine/params/` while the struck row three above records its evacuation and `ls engine/` confirms
  it is gone — and the `tests/` row's "~850KB of narrative `.md`" against a measured 8 files / 90 KB.

Two sessions, same day, same file, arriving from different directions. **No retraction is owed on
either side.** F5's remedy (distil §3, delete the four retired rows) and `main`'s remedy (a guard that
fails when a figure drifts) are the two halves of §0.1 point 5 — one owner, and a guard that fails on
recurrence — and should land together.

### 8.3 `main`'s `ED-IN-0156` **resolves** the uncertainty §7.3 item 1 flagged

§7.3 recorded that my scan found **320 of 527** distinct `PP-NNN` unresolvable while CLAUDE.md §0
claims **433 of 452**, and stated plainly that mine "neither confirms nor refutes" that figure
because the scan roots differ.

`main`'s entry supplies the missing variable: **scope**. The 433/452 figure reproduces *only* if the
universe is `registers/patch_register_active.yaml` alone (6 entries). Including
`registers/patch_register_index.md` — a live register surface carrying 196 entries — the same
measurement gives **328 of 466, i.e. 70% unresolvable rather than 96%**. My 320/527 was measuring
against both registers, which is why it landed near 328/466 and nowhere near 433/452.

**So §7.3 item 1 is closed:** the discrepancy was never a disagreement about the tree, it was an
unstated denominator. CLAUDE.md §0's warning is "directionally right and overstated by ~26 points"
(`main`'s wording, and I agree with it). §7.3 item 1 should be read as resolved, not open.

### 8.4 #302's process lesson converges with §1.1

#302 records: *"a verifier launched beside the work rather than before the commit that ships it
produces a review that lands after the merge."* Its two critics returned after PR #300 had merged, so
two of their findings shipped and needed a second branch to correct.

§1.1 of this document records the sibling failure: a suite run *before* the work rather than after it,
producing a green claim that belonged to a different commit. **Same defect, opposite end of the same
axis — verification performed at the wrong time relative to the commit it certifies.** Two independent
instances in one repository on one day is a pattern, not two accidents, and neither is fixed by
resolving to be more careful. The generalisable form: *a verification is only evidence about the
artifact it ran against.* Both cases are cheap to guard mechanically (a pre-push hook that re-runs the
suite on the exact HEAD being pushed; a merge gate that refuses while a launched critic is
outstanding) and neither is guarded today.

### 8.5 #302's "cite the id, never the line" applies to this audit — anchors corrected

#302's G-17/G-20 finding: citing `editorial_ledger_in.jsonl:57` is structurally unstable, because the
entry moved to `:54` and then `:50` as the ledger was appended to and archived. Its rule: **cite the
id, never the line, in an append-and-archive register.**

Applied to my own work: this document and the code-leanness census cite
`references/restructure_ledger.md:720`, `:981`, and rows 177 / 852. **All four still resolve
correctly** — re-checked after this merge — but `restructure_ledger.md` is in exactly the flagged
class: its own W7 requirement is that *"every deletion commit writes a new alias row into it."* The
anchors hold today by luck, not by construction.

Where the row has no id to cite, the stable citation is its **content**:

| was cited as | stable form |
|---|---|
| `restructure_ledger.md:720` | the row `` `params/` → `engine/params/` `` |
| `restructure_ledger.md:981` | the row `` `designs/audit/` → `audit/` `` |
| `restructure_ledger.md:177` | the row `` `designs/systems/npc_behavior_v30.md` → `systems/npcs/npc_behavior_v30.md` `` |
| `restructure_ledger.md:852` | the row `` `designs/scene/social_contest_v30.md` → `systems/social_contest/social_contest_v30.md` `` |

Line anchors into **code** are not affected and are not changed — `test_flow_skeletons.py` verifies
that class against the tree on every run, which is precisely the guard the register rows lack.

### 8.6 What #302 does not change

Its substance is the world-schema register (G-17's report-only framing, an 18-vs-19 lens denominator,
the ED-IN-0153 falsifier correction). **None of it touches F1–F4 or F6–F8**, the code-leanness census,
or the §5 plan. No finding above is withdrawn or weakened by the merge.
