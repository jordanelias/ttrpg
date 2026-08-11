# Consolidation sweep — prune / distil / deduplicate opportunities (ED-IN-0156)

## Status: REFERENCE — observation with evidence; nothing ruled, nothing executed

**Scope.** Whole working tree at `c26a22c` (clean), read against the twelve commits landed
2026-08-04..2026-08-11. **No fan-out, no workflow** — solo, by reading. Every number below comes
from a command run in this session against the working tree, not from a prior artifact.

**Baseline established first:** `pytest tests/valoria` → 1775 passed, 23 skipped, 14 xfailed,
1 xpassed (588.9s). `review_core --summary` → AMBER, 0 blocking, 0 regressions, 2 report-only.

**Read `01_adversarial_pass.md` next.** It records three findings this sweep produced and then
killed, and the corrections it forced on two that survived. The killed ones were the
strongest-looking findings in the first pass.

---

## What the week's shape actually is

Twelve commits, dominated by **index and atlas construction**: a per-subsystem glossary (#296), a
contract + key index (#298), 16 flow skeletons + an engine atlas (#299), a nomenclature proposal
(#301), and three new audit corpora (#294, #299, #300). The tree grew a lot of *generated
navigational surface* over a corpus that had just been cut in half by the 2026-08-05 evacuation.

That is the right instinct and mostly well-executed. The defects are not in the new material. They
are at its **edges**: the artifacts built *before* this week that the new material's own pattern
would have fixed, and the places where the map has not caught up with the tree.

Top-level shape, measured: `audit/` 11 MB / 312 files · `systems/` 7.7 MB · `references/` 4.7 MB ·
`tools/` 4.4 MB · `tests/` 3.7 MB · `research/` 2.7 MB · `registers/` 2.5 MB. Total 42 MB / 1391 files.

---

## F1 — `tools/observability/` tracks 688 KB of derived duplicates with no consistency guard

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
Directory total: 2.75 MB.

**Verified:** parsing each `_data.js` and comparing the decoded object to its `.json` gives
`IDENTICAL` for all five. The `_data.js` is `window.VALORIA_X = <the json>;` — a one-line wrapper
whose writer is already single-owned at `obs_core.write_js_bundle`.

**The wrapper is not gratuitous** — it is the `file://` workaround (a double-clicked page cannot
`fetch()` a local `.json`). But the README names `console.html` as the primary ("Fastest — fully
self-contained, works offline with no server") and `index.html` + `_data.js` as the **"Dev pair
(regenerable)"**. The repo commits the regenerable secondary anyway.

**And the committed dev pair is broken on arrival.** `index.html:185` loads
`review_state_data.js`, which `.gitignore` excludes by design. In any fresh clone that script 404s
while `console.html` works.

**No guard.** `test_observability_core.py::test_write_js_bundle` tests the writer against a
`tmp_path`. Nothing asserts the three committed tiers agree; they can silently diverge.
`audit-refresh.yml` `git add`s all three tiers weekly, and its change-detection diff lists both
`.json` and `_data.js` — two triggers for one signal.

**Opportunity.** Gitignore the five `_data.js` (derived, one command to rebuild); keep `.json` as
source and `console.html` as the artifact. Resolve `index.html` — delete it, or make the
review-state block optional so the committed page works. Removes 688 KB tracked and a weekly
3-way diff. Risk low; fully regenerable.

---

## F2 — `references/audit_registry.jsonl` indexes 7 of 41 audit units, and its gate cannot see that

`audit/` is the largest tree in the repo (11 MB, 312 files). Its index is 46 rows. **41 of the 46
rows still carry `designs/…` paths** for a tree retired 2026-07-19.

Those paths *do* resolve — `references/restructure_ledger.md:981` carries the
`designs/audit/ → audit/` dir-prefix row. Measured **after** alias resolution:

- **34 of 41 on-disk audit dirs have no registry row** (83%), including every unit from
  2026-07-01 onward except seven, and all three landed this week.
- **10 of 17 resolved registry dirs point at nothing on disk** — pre-July units removed by the
  2026-08-05 evacuation whose rows were never updated.

**The gate is structurally blind to this.** `ci_audit_registry_check.py` reports exactly **3**
findings, because it only considers entries dated *newer than the registry's own latest date*
(2026-08-06). It can only ever see the tail; the 34-unit gap is invisible to it by construction,
not by threshold. This is the failure class ED-IN-0115..0119 already named — a gate that cannot
see what it guards.

**Opportunity.** Backfill the rows or rule the registry retired; either is fine, the present state
is the bad one — an index that is 17% accurate is worse than none, because it is consulted. If it
is kept, the check needs to compare *sets*, not tails.

---

## F3 — `tools/handoff_atomize.py`: 33 live findings, zero callers, and its test cannot see them

The tool is built, works, and reports real defects. `python3 tools/handoff_atomize.py --all
--check` → **33 issues** across all nine lanes, including:

- `IN: executive summary says 44 live item(s); the file has 73` — the summary has drifted from
  what it summarises.
- `IN: executive summary's newest date is 2026-07-28 but the file carries an item dated
  2026-08-11` — the summary predates its own contents by two weeks.
- 30 of IN's 37 bullets, and 100% of the bullets in FI/SC/FA/WR/GO/SE/PC, carry no
  `[OPEN|PART|DONE]` tag, so the SessionStart banner infers status from prose — the exact
  inference ED-IN-0086 introduced the tag to replace.

**Wired nowhere.** Not in `.github/workflows/`, not in `.githooks/`, not in
`.claude/settings.json`, not in `tools/valoria_local.py`.

**Its test cannot observe any of it.** `tests/valoria/test_handoff_structure.py` imports the
module and exercises `status_tag` / `classify` / `tag_problems` on **synthetic strings**. It never
invokes `--check` against `registers/handoffs/*.md`. So the suite is green with all 33 live —
§0.1 point 2 exactly: an assertion that cannot observe the failure it excludes.

**The fix is already proven in-tree, this week.** `test_engine_atlas.py` and
`test_contract_index.py` each `subprocess` the real builder's `--check` against the live artifact;
`test_build_glossary.py::test_committed_output_matches_a_fresh_build` byte-compares every committed
file to a fresh build. Applying that pattern to `handoff_atomize` is roughly ten lines.

**Highest ratio of impact to cost in this sweep.**

---

## F4 — `HANDOFF_IN.md` is 191 KB; the root file was archived at 16 KB for exactly this reason

`HANDOFF.md`'s own History section records the precedent: *"this file had drifted from 'index' to
a full append-only session log"* — resolved 2026-07-08 by rolling to `HANDOFF_archive.md`.

The lane files then reproduced the defect:

| file | size |
|---|---:|
| `HANDOFF_IN.md` | 191,413 |
| `HANDOFF_MB.md` | 104,604 |
| `HANDOFF_PC.md` | 99,960 |
| root `HANDOFF.md` | 15,843 |

`HANDOFF_IN.md` is **12× the size at which the root file was judged to need archiving**, and its
`## Next actions` section begins at line 1506 of the file. The 10,000-token-per-document cap that
`handoff_atomize` exists to enforce (and that `test_handoff_structure.py` pins as a *function*) is
not applied to any of them.

**Related, and separately verifiable:** the root `HANDOFF.md`'s **first** "Next actions" bullet —
the one the SessionStart banner surfaces above all others — is a `✅ RESOLVED 2026-07-30` item
whose live text is struck through. It appeared verbatim in this session's own startup banner. The
most prominent slot in the repo's continuity signal has been spending itself on a non-action for
two weeks.

`HANDOFF_IN.md`'s W8 row states the atomization run is blocked on "**2** Jordan calls". That
blocker is real and this sweep does not route around it — but the banner bullet and the drifted
executive summary are not blocked on anything.

---

## F5 — `CLAUDE.md` is 13,963 tokens and §3 contradicts itself

This file is loaded into every session **and every subagent**. §11 already prices context
re-sends at 12,153 tokens for this file alone. It is the single highest-leverage distillation
target in the repo, and it is measurably stale.

Composition:

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
machine-readable row in `references/restructure_ledger.md` — the single owner of that fact. §8's
own invariant ("every rule lives once; never re-implement a rule") applied to CLAUDE.md itself.

**Three verified staleness defects:**

1. **§3 contradicts itself.** The `engine/` row says engine/ holds "the prose param tables
   `engine/params/` (moved from top-level `params/`, 2026-07-16)". The `~~engine/params/~~` row
   three rows above says it was **evacuated 2026-08-05**. `ls engine/` confirms no `params/`.
2. **The `tests/` row** warns of "~850KB of narrative/audit `*.md` ("emergent_arc_skeleton_test_*",
   session audits)". Measured: **8 `.md` files, 90 KB** excluding `coverage_matrix.md`, and none
   is named `emergent_arc_skeleton_test_*`. The evacuation removed them; the warning outlived them.
3. **The `tools/` row** cites "36 of 106 modules have zero automated callers … 6 have zero callers
   of any kind". `references/apparatus_registry.yaml` now counts **123 entries, 6 orphaned,
   0 prune candidates**.

**Opportunity.** Cut §3 to what a reader cannot get from `CURRENT.md` + `restructure_ledger.md`:
delete the four retired rows, compress `systems/` from migration history to current membership,
fix the `engine/` contradiction, re-measure `tests/` and `tools/`. Conservatively ~1,500 tokens
off every session and every fan-out agent, with the *accuracy* gain mattering more than the size.

---

## F6 — `references/glossary/` is 3.0 MB across three renderings of one dataset

`glossary.json` 1,464,427 B (every term × every full path) + `MASTER_GLOSSARY.md` 257,262 B
+ 19 per-subsystem files 1,357,376 B.

**1,221 of 1,357** MASTER rows and **2,584 of 3,722** per-subsystem rows read
`_no curated definition_`. The curated source, `references/glossary.md`, holds 176 definitions in
125 rows. The generated corpus is therefore ~24× the size of what it annotates, and is
predominantly an identifier census rather than a glossary — which the header is honest about
("Curated DEFINITIONS live in references/glossary.md; this view adds LOCATIONS").

Churn is real: commit `63d4d0c` rewrote **2,441 insertions / 1,481 deletions across 21 files** as a
side effect of unrelated work; `8ef65ac` another 242/195.

**This one is correctly guarded and is not a defect.**
`test_build_glossary.py::test_committed_output_matches_a_fresh_build` byte-compares every committed
file to a fresh build inside the blocking suite — it cannot rot. The opportunity is **retention
shape, not correctness**: the per-subsystem tier (1.36 MB, 45% of the corpus) is fully derivable
from `glossary.json` on demand, and it is the tier carrying most of the churn. Flagged as cost, not
as a fault. Lowest confidence item here; listed because 3 MB is 7% of the tree.

---

## F7 — `research/` (2.7 MB, 38 files) is absent from the repository map

Zero mentions in `CLAUDE.md`. It is live: cited by
`systems/_architecture/early_game_ignition_analysis.md`,
`systems/mass_battle/sim/massbattle.py`, `HANDOFF_IN.md`, and two editorial ledgers. It holds the
`pre_firearms_formations/` corpus (17 files), governance and historical research, and rendered
diagrams with generator scripts.

§3 documents 18 trees **including four that no longer exist**, and omits this one. Cheap to fix;
belongs in the same edit as F5.

---

## F8 — two SUPERSEDED heads direct readers to a forbidden path (low severity)

`systems/npcs/npc_behavior_system_v1.md` (66 KB) and
`systems/social_contest/social_contest_system_v2.md` (30 KB) carry `## Status: SUPERSEDED —
canonical doc is designs/systems/npc_behavior_v30.md` / `designs/scene/social_contest_v30.md`.

**Verified non-breaking:** both resolve through `restructure_ledger.md` (rows 177 and 852) to
`systems/npcs/npc_behavior_v30.md` and `systems/social_contest/social_contest_v30.md`, which exist.
The defect is only that a *human* reader is pointed at a tree CLAUDE.md forbids recreating.
Two-line fix; no urgency.

---

## Ranking (impact × cheapness)

| # | Finding | Impact | Cost | Blocked on |
|---|---|---|---|---|
| 1 | **F3** wire `handoff_atomize --check` into the suite | high | ~10 lines | nothing |
| 2 | **F5** distil + correct CLAUDE.md §3 | high (every session, every agent) | one edit | nothing |
| 3 | **F2** audit registry: backfill or retire; fix the tail-blind check | high | medium | a keep/retire call |
| 4 | **F1** gitignore the five `_data.js`; resolve `index.html` | medium | mechanical | nothing |
| 5 | **F4** roll the lane handoffs; drop the resolved banner bullet | medium | small / large | banner bullet: nothing. Atomization: W8's 2 Jordan calls |
| 6 | **F7** add `research/` to §3 | low | trivial | nothing |
| 7 | **F8** repoint two SUPERSEDED banners | low | trivial | nothing |
| 8 | **F6** per-subsystem glossary retention | low | needs a call | a retention ruling |

**Nothing here is executed.** Every item is an observation with evidence; which are defects and
which are deliberate is a per-lane call.
