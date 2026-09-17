<!-- Permitted by CLAUDE.md §0's narrow exception (RULED by Jordan, 2026-09-17). THE TEST: does this
     create work for a future session? No — it is a closed record of what was reconciled on
     2026-09-17 and why, about documents that already exist in this directory. Every item is resolved;
     the one that is not (RR-3) is carried in 04_BUILD_ORDER.md's ruling ledger, which owns it. This
     record dies when the suite it judges dies. -->

# The unification divergence ledger — 2026-09-17

Four documents were authored **in parallel** from one plan. Four simultaneous readings of a spec are
not one design, and the differences are invisible to each author by construction. This pass found 21
divergences, resolved each on evidence, repaired ~24 citations by opening them, and wrote
`00_THE_DESIGN.md` as the unified statement.

⚠ **This file is a transcript of the pass's findings, captured for reading.** It is not a repository
document and was never committed as one: the repairs went into the four files (struck-and-kept) and
`00_THE_DESIGN.md` is the deliverable.

## The ledger

| # | category | what diverged | files | how it was resolved |
|---|---|---|---|---|
| 1 | contradiction | `create_record` hold-mint addresses | 01 vs 02 | **Measured**: body `:262-290`, Record write `:284-285`, S13 comment `:286-287`, `add_tenure` `:288-289`. 02 right; 01 repaired at five sites |
| 2 | contradiction | "a building **IS** a hearth" against 02's "**stands on** one" | 03 vs 02 | 02 owns the ontology; 03's two sites struck and corrected. The zoom cut survives on the ladder, not on the sentence |
| 3 | contradiction | 03's policy surface reads `Office.establishment` — a field 01 **deletes** (`ARCH §B.7` call 2) and which is **empty on 19 of 19** | 03 vs 01 | The read becomes the Query over `oblige`. 03 corrected at two sites including its central "executors + blind spots" display |
| 4 | contradiction | `inferred`'s producer: `thread_read` (04) against the `post_remit` channel (03) | 04 vs 03 | 03 governs — `thread_read` is unresolvable and `ARCH §C.6` is ratified. 04's item struck and rewritten, its Arc-2 flag dropped |
| 5 | contradiction | "a policy is a **named list of people**" against "executors **computed, never enumerated**" (`holonic §37.3`) | 03 vs 01 | 01 governs; 03's three sites struck to "its reach resolves to people" |
| 6 | contradiction | the Q3 blocker: presence 0/74 (02) against "the crossing never fires" (04) | 02 vs 04 | **Re-measured**: first crossing at MATTER **pass 21**; corpus worlds **do** co-locate. 04 right — the crossing binds everywhere, presence is populated-only |
| 7 | contradiction | 04's own repair, "723 is `transfer`'s count, not `work`'s" | 04 vs the tree | **04's repair was itself WRONG.** `test_season_shape.py:7279` records *"`work` 723 refusals with no execution"*. 723 is the per-verb corpus candidate count; struck in 04 |
| 8 | ruling drift | 04 said "two surviving… nothing else"; 03 said "the ONE item that needs Jordan" | 04/03/README | **RR-3 registered** and marked the weakest, carrying 03's own counter-argument. README lists all three |
| 9 | ruling drift | 01 and 04 each listed a **different** nine closed requests | 01/04/README | Five common, **thirteen in union**. 04 §C.5 made the single owner; 01 §C.6 becomes a pointer |
| 10 | contradiction | "one emission rule, three uses" — two different triples | 03 vs 01/04 | 01 owns; 03 restated, with the `ttl` lapse kept as a named fourth |
| 11 | vocabulary | `works` / *a work* / *a project* | 01 rules; 02+03 drifted | `works` everywhere — 14 sites in 02, 10 in 03; the ruling promoted to suite-binding |
| 12 | vocabulary | `04 §X` and `01:NNN` **collide with this suite's own file numbers** — and `04_BUILD_ORDER.md` really does have a `§A.3` | all | **`ARCH`/`AX` prefixes introduced**, 217 occurrences renamed, declared in `00`, the README and every header |
| 13 | vocabulary | `D-1` meant **four** different things; `L−1` meant three; inside 03 `L-1` meant **both** a read licence and a loop | all | Prefixed `SP-/BW-/SU-/BO-n`; loops `SP-L±n`/`BW-L±n`/`SU-Ln`; licences stay `L-1..L-3` |
| 14 | vocabulary | `reach` — a declared operand (01) against the ordinary word (03) | 01/03 | Both senses named explicitly in 03 §A.4 |
| 15 | grade | "policy-effects readout cannot be built" — STRUCTURAL (01) against measured MECHANICAL (03) | 01/03 | Split: STRUCTURAL inside `choose`, **MECHANICAL on the surface** (`port/` does not exist; the scan has four holes) |
| 16 | grade | `hold`-never-a-Site — "CONVENTION today" (02) against "nothing" (04) | 02 | → **NOTHING** |
| 17 | grade | `ED-SE-0051` graded **STRUCTURAL** — a category error | 02 | → "not a grade: RR-2" |
| 18 | duplication | the `hold`-guard §0.1-pt-5 argument; `fort_level`/`facility_tier`; the commons `share`; RR-1 | 02/04, 01/04 | Owners marked; 04 reduced to pointers plus a build step |
| 19 | orphan | 02's header cites "§D.9" — no such section | 02 | → §D.15, plus a falsifier |
| 20 | counts | the verb figures | all | **Re-measured, all confirmed**: 38 rows / 18 resolvable / 28 formable / 13 both / 10 formable-by-nobody / 9 `binding_decision` (2 `own`) / 11 `@effect_for`. 01's "not resolvable" list had 15 of 20 — completed |
| 21 | counts | producerless RES rows — 9, 10 or 11 across the corpus | 04 + tree | **Re-measured: 10** of 40 rows. 04 right; `write_matrix.yaml`'s own header is stale **both ways** |

## Citations repaired (~24, each opened)

**04 was wrong on:** the `restore` row and its formula, its own note line, `w.crossings.append` (three
sites), the `add_tenure` kind check (three sites), R7 (three sites), `Rung.__setattr__`.
**01 was wrong on:** `title_domain` — it lives in `data/rosters.py:459`, **not** `predicates.py`, so a
session deleting "four helpers in one file" would have found three — plus the `requires_forms` note,
an `AX` range, `holonic:1290`, and the Q1/Q2/Q4 gate lines.
**02:** `site_kinds` values, `hold_force`. **03:** `question_sources`, `band_floors`.

⚠ **Three of 04's wrong lines sat inside its own "opened and found CORRECT" list** — false
verifications, now struck.

## The one thing it could not resolve

**RR-3's status is contested inside `03` itself.** §A.7.1 measures `scale_transitions_v30.md` as
binding nothing — two `## Status:` lines, a retire set, zero `.py` references — while §C.3 escalates
on its `CANONICAL` line. Registered as the suite's third surviving ruling request and **marked the
weakest**, with both halves stated, rather than being closed or split down the middle.
