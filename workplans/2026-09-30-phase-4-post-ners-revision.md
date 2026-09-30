# Phase 4, revised — the NERS/Fable pass and what it changed

## Status: **ADOPTED 2026-09-30, ON JORDAN'S INSTRUCTION** — *"I asked for a NERS audit with findings
used to improve upon plan for Phase 4... build out the new version of this plan."* This document is
the new version, scoped exactly as instructed: it **supersedes `2026-09-28-the-plan-one-order-mc-v18-
retired.md`'s §2.3 (the Phase-4 rows only) and §3.4 (whole) and §5.1 items 14/15/16** — the Phase 4
table, its prose, and the three Jordan-roster items the NERS pass touched. **That document stays
CONTENT OWNER for everything else**: §0–§1 (what the document is, corrections to the 2026-09-28 brief),
§2.1–§2.2 (the supersession verdict, the Phase 1/pre-Phase-2 DONE ledger), §2.3's non-Phase-4 rows
(Phases 1–3), §3.1–§3.3 (Phases 1–3 themselves), §3.5–§3.7, §4 (the nine contradictions — none of which
Phase 4 reopens), §5.1's other ten items and §5.2, §6–§9. Nothing in those sections is restated here;
read them there.

## Owner: infrastructure / cross-cutting (IN lane), same as the document this supersedes.

## Produced by: the pipeline Jordan specified this session, in order —
1. **An Opus NERS pass**, effort max, run "objective neutral pessimistic," against `engine/season/`
   as shipped through Phase 2's close plus Phase 4's own design (this document's predecessor's §3.4).
2. **A Fable 5.1 read-only review** of that pass's findings against the rest of the workplan — Jordan's
   own framing: *"Fable 5.1 read-only permission to design what to code to fill in those gaps and
   resolve failures."* Fable corrected two of the Opus pass's own findings (below, §1.2), corrected
   eight `hole_register.yaml` rows' citations and scope, and specified the wording fixes applied to
   the predecessor document's §3.4 preamble and §5.1 items 14–16.
3. **Sonnet producers** (the `valoria-author` pattern) built what Fable's review called for and ran the
   settled per-subsystem-file streamline pass this session's own instruction required.
4. **This write-up**, restating Phase 4 with everything above folded in, per Jordan's explicit
   instruction to build the new version rather than leave the findings scattered across commits.

## Grade under CLAUDE.md §0.2: `paper` throughout — a plan, not an execution artifact. Every `DONE` row
below repeats cited evidence; the execution artifact is the thing cited, never this file.

---

## 1. What the NERS/Fable pass found, and what happened to each finding

**The headline result, stated plainly because it is not the one a NERS pass usually returns:** the
pass found no defect in Phase 4's *planned* engineering — positions `21` through `26` are unbuilt, and
you cannot NERS-audit code that does not exist. What it found were **latent gaps in Phase 1–3's already-
shipped mechanisms**, most of them already known and registered, several sharpened or corrected here.
None of them changes what a future Phase-4 position builds; several change what its builder must read
first so as not to inherit a wrong citation or an overstated claim. That distinction is the substance
of this section.

### 1.1 Findings that were fixed in code (commits `80903bf`, `eaf654c`, `006af44`, `33855cd3` — position
`20-ii`'s own build, done concurrently with the NERS pass and folding in Fable's two corrections below)

- **`faction_q.at_war` keyed on a scale-local `Proposition.predicate` string rather than the codebase's
  actual `mood`-keyed convention.** Fable's finding, not the Opus pass's (the Opus pass had flagged
  `at_war` as a false N-line on the theory it had no producer at all; Fable found a shipped producer,
  `_eff_utter`/`_eff_commit`, and narrowed the real defect to the type mismatch). Fixed: `WAR_MOOD =
  "WAR"`, matched against `Proposition.mood`.
- **`faction_q.head`'s docstring claimed "highest-graded"; the body did `graded[-1]` (last-write-
  order).** Fable's finding. Fixed to match the body (last-write-wins is the ruled semantics, `F.4`'s
  own reading) and the docstring corrected.

### 1.2 Findings that were corrections to the Opus pass itself, made by Fable's independent review

- **`at_war` is not a false N-line in the strict sense claimed.** See 1.1 — a shipped producer exists;
  the actual defect was narrower (a type mismatch, not an absent mechanism).
- **The Opus pass's citations had drifted against the tree by the time Fable read them** (`20-ii`
  landed mid-pass), which is the ordinary hazard CLAUDE.md §0.1 pt 3 names for any claim not re-checked
  against a live working tree; Fable re-verified every citation it carried forward rather than
  inheriting the Opus pass's.

### 1.3 Findings registered as holes (latent, not blocking) — `hole_register.yaml`, corrected wording
applied in commit `30dc8c65`

These are properties of **already-shipped** Phase 1–3 mechanisms the pass measured and found under-
executing or ambiguously scoped. None blocks a Phase-4 position; several are exactly what a Phase-4
builder working the same subgraph (`22`, `22a`, `23` on the oblige/determine chain; `28-ii` on the
always-refused-verb accounting) needs to read accurately rather than re-derive.

| row | what it measures | corrected scope (this pass) |
|---|---|---|
| `H-156` | `commit`/`found`/`build`/`survey` crowd `release` out of scene budgets by always forming and always refusing; `migrate` and `levy` are two further instances of the same shape | corrected citation (`_eff_release`'s new location); the "six... plus `release`" wording, since `20-ii` moved `release` back into the executed set (it is no longer one of the always-refused eight — see §1.4) |
| `H-159` | `determine` never executes in any shipped world | mis-citation fixed (`H-165` limit 3 → `H-163`, the row that actually counts `determine`'s attempts) |
| `H-163` | `levy` forms and refuses; corpus form-rate | corrected from an implied universal-formation reading to the actual scope — formed only where a seat grants `remit:issue` |
| `H-168` | `migrate`'s decline is effect-body, non-decaying | added the explicit cross-reference distinguishing it from `H-156`'s decaying typed-cell shape |
| `H-172` | the `u2` discrimination-stamp test's assertion change | reworded from a self-contradictory "not weakened" framing to what the assertion actually does — pins the current measured identity, fires on divergence |
| `H-173` | the `oblige`/`determine` edge-typing gap (a sentence and a service job are the same Tenure kind to every reader) | mis-citation fixed (same `H-165`→`H-163` error); the "marker field" framing struck — Fable traced the opening act's recoverability through `causing_act`/`attribution.py` and found it already reachable without a new field, narrowing the live question to whether readers *should* distinguish a sentence from a service, not whether they *can*; the renewal-scope overstatement ("every live oblige") narrowed to match `_renewals`' actual soonest-first, payment-bounded behaviour |
| `H-174` | the presence/residence split's effect on `_renewals`' `home_of` clause | mis-citation fixed (`H-163`→`H-158`, the row that actually grounds `via` unreachability); item 2 (upkeep-target reading) demoted from a Jordan question to an answered one — `gate.py`'s own docstring already calls `home_of` the one owner of where a person is, which is the architecture's answer for this clause; item 1 (jurisdiction) stands as the live ruling it already was |

### 1.4 A correction with a direct Phase-4 accounting consequence

**The corpus's always-refused-verb count moved from nine to eight when `20-ii` landed**, discovered
mid-pass and corrected everywhere it was cited (`H-156`, the `H-163` levy paragraph, the `H-168` migrate
paragraph, and the predecessor plan's §5.1 item 14): `20-ii`'s 54 new scale-overlay cases include one
(`ARC-32`) where `release` now executes, moving it out of the always-refused set and back into the
executed set (16 verbs, not 15 — independently re-verified this session by a live `corpus_run`,
matching the pinned `ever` set in `test_season_shape.py:7351-7353` verb-for-verb). **Any Phase-4
position that cites the always-refused count (`28-ii`'s battle-execution work, in particular, since it
adds `march` to the executed set next) must cite eight, not nine, and must not assume `release` is
still crowded out** — `20-ii` already fixed that, incidentally, as a side effect of the corpus growing
from 89 to 143 worlds.

### 1.5 What retiring `mc_v18` buys, corrected (Fable's finding, already applied to the predecessor
document's §3.4 preamble in commit `30dc8c65` — restated here as the position this document's Phase 4
table inherits)

Retiring the spine is an **E gain** (one engine, one vocabulary — verified: no game code imports
`engine.mc_v18`, only three CI-blocking test files do). **It is not itself an S gain** — `mc_v18` has
no faction ladder to compare the season loop against, so there is no sibling calculation for the
retirement to bring into methodological line with. Whatever S this batch buys comes specifically from
`20-ii` (done), `20-iv` and `28-ii`'s second half (both below), not from the deletion. **And it has a
named cost**: deleting `mc_v18` removes the last campaign-scale regression oracle (`28-ii`'s hash pin
is a tripwire, not a balance instrument, and `tools/balance_oracle.py` was retired with no live
successor). This is not free, and it is not presented as free anywhere in this document.

### 1.6 The settled per-subsystem-file requirement, applied

Independent of the NERS pass, this session's own architectural requirement (*"each subsystem is
supposed to be a module... per subsystem files"*) was applied to `engine/season/loop/effects.py`
— 1954 undifferentiated lines holding all 26 verbs' write-side effects, the one file in `loop/` that
did not yet match `queries/`'s one-file-per-domain pattern. Commit `309a17d9` split it into six domain
siblings plus a shared-primitives module and a thin aggregator (table in §2 below); commit `a882cc32`
corrected eleven `hole_register.yaml` citations the split stranded at line numbers inside a file that
had shrunk from 1954 lines to 100. **§3 below gives every remaining Phase-4 position that touches an
effect body the correct target file**, so this does not recur.

---

## 2. State index — Phase 4 rows, current through this document (supersedes the predecessor's §2.3
for these rows only; its non-Phase-4 rows are unchanged and not restated)

| # | handle | lane | `STATE` | `GATE` | evidence |
|---|---|---|---|---|---|
| a | **`20-ii`** faction queries (U9/R-04) | IN | **DONE** | `★` ✓ | `80903bf`,`eaf654c`,`006af44`,`33855cd3`; 23 tests (`test_faction_q.py`+`test_scale_of_rung.py`), `harness.delta HEAD` → 0 flips, live `corpus_run` independently re-verified |
| — | **NERS/FABLE PASS** | IN | **DONE** | `20-ii` (concurrent) | this section; `hole_register.yaml` H-156/159/163/168/172/173/174 |
| — | **REGISTER/PLAN FIXES** | IN | **DONE** | NERS/FABLE PASS | `30dc8c65` |
| — | **EFFECTS-SPLIT** | IN | **DONE** | — (independent of the NERS pass; the settled modularity requirement) | `309a17d9`; 683 passed / 1 pre-existing failure (`engine/season/tests`, independently reproduced against both the split and the pre-split commit) |
| — | **CITATION-FIX** | IN | **DONE** | EFFECTS-SPLIT | `a882cc32` |
| b | **`21`** U10 | IN | **OPEN, PARTIAL** — items 1-2 done; item 3 (reconcile `workplan_v6_progress.yaml`) NOT attempted; a genuine upstream break in `wd_collect.py` leaves R-01/R-02 `not_met` | `20-ii` ✓ | `03de9d47` |
| c | **`28-ii`** (M6) successor goldens | IN | **DONE** — one disclosed, out-of-scope gap (corpus-organic reachability) | `28-i` ✓ | `013a5b1b` (see correction in `03de9d47`) |
| d | **`28-iii`** SPINE-DELETE | IN | **OPEN** (unblocked -- `28-ii` is DONE) | `28-ii` ✓ | — |
| e | **`20-iv`** d.1 + terrain/garrison | MB/IN | BLOCKED | `20-ii` ✓, `28-iii` | — |
| f | **`29a`** overview | IN | BLOCKED | `28-iii` (+ `27` for `ms_track`) | — |
| g | **`29b`** factions + `game_state.py` | IN | BLOCKED | `20-ii` ✓, `28-iii`, `29a` | — |
| h | **`29d`** world | IN | BLOCKED | `29b`, `10` | — |
| i | **`29c`** settlements | SE | BLOCKED | `29b`, `29d`, `24e` ✓, `24d-ii` ✓ | — |
| j | **`29f`**/`29e`** fieldwork/characters | IN | BLOCKED | `14`, `27` | — |
| k | **`2-ii`** RET-SC kernel | IN/SC | BLOCKED | `28-iii`, `29b`, `22` | — |
| l | **`22`** PROC-B | SC | **OPEN, PARTIAL** — steps 6,7,9,10 done (at `18`/`19`), step 8 built, steps 11 (partial)–16 open (the contest-resolution core) | `18` ✓, `★` ✓ | `a1282b02` |
| m | **`22a`→`23`→`22b`** | SC/IN | OPEN/BLOCKED | `22` (+`15d`,`17b`) | — |
| n | **`24g`** bodies clock + P3 | SE | BLOCKED | `24d-ii` ✓, `24f`'s cohort producer ✓, **JORDAN** (§5.1 item 8, unchanged) | — |
| o | **`24h`** S5 revolt/forswearing | SE/IN | BLOCKED | `20-ii` ✓; P7 **JORDAN** (§5.1 item 11, unchanged) | — |
| p | **`26`** GO-VERSION | GO | **JORDAN** (unchanged) | §5.1 item 9 | — |

Rows with no `evidence` cell are unbuilt; their GATE/dependency structure is unchanged from the
predecessor document because the NERS pass found nothing wrong with their plan — only §3 below adds
detail (the effect-file targets) that document did not yet need, because the split had not happened.

---

## 3. The revised Phase-4 build detail — per position, what changed for its builder

**Unless a subsection below says otherwise, a position's build content is UNCHANGED from the
predecessor document's §3.4** (same file list, same disposition, same reasoning) — re-read it there;
this section adds only what the NERS pass, Fable's review, or the effects split changed.

**b · `21` (U10).** No change. Not an effects-domain position (a measurement, `measured:` from
instrument output only) — no `loop/effects_*.py` file is touched.

⚠ **DISCLOSED, NOT "BOOKKEEPING DONE" (BATCH-CLOSE Phase-1 antagonist finding)**: U10 names three
items (`workplans/2026-09-09-r-execution-plan.md:1678-1700`); this position closed items 1 and 2
(`measured:` lines re-derived from instrument output; the `shape.py:NNNN` citation claim
retracted) but item 3 — reconcile `workplans/workplan_v6_progress.yaml` against what actually ran
— was NOT attempted. That file is still stamped `as_of: sha: "c75c561", date: "2026-08-19"`, and
this board is what feeds `tools/m1_acceptance.py`'s DOC-DERIVED **row 3 of 4**
(`ROWS = [row_stub_invocations, row_determinism, row_m1_junctures, row_invariant_violations]` —
`row_m1_junctures` is the third element and the only one the tool's own `collect()` note calls
DOC-DERIVED), not "row 4" as an earlier commit message on this branch (`013a5b1b`) described it.

**c · `28-ii` (M6).** No change to what it builds. **Effect-file target: `engine/season/loop/
effects_combat.py`** — `march` lives there now (with `fight`). ⚠ **STRUCK (`/simplify`, BATCH-CLOSE
Phase 2): this subsection originally predicted an `operands_for` arm landing in `data/verbs.py`/
`rosters.yaml`. No arm was needed** — see the BUILT bullet below; the prediction was wrong on both
the diagnosis and the file. **Accounting correction (§1.4): cite eight always-refused verbs, not
nine, and do not assume `release` is still crowded out of the scene budget** — `20-ii` already
returned it to the executed set.

⚠ **BUILT 2026-09-30, landed in commit `013a5b1b` (mislabeled — see the correction in commit
`03de9d47`'s message; the content is `28-ii`'s, verified byte-identical against the working tree
independently by both producers and by the orchestrator) — DONE, one disclosed, out-of-scope gap.**

- **The hash pin**: `engine/season/tests/test_build_realm_determinism.py` (new) — `build_realm(0)`
  through the real `SeasonDriver`/`make_chooser`, run twice, `content_hash()` compared byte-identical,
  plus a seed-0-vs-seed-1 divergence control. Neither existing candidate (`test_m1_acceptance_probe.py`,
  `test_r4_event_ids_are_unique...`) actually pinned `build_realm` — checked, not assumed. 2 passed.
- **`operands_for` needed no arm, and never did** (`decision/options.py::opening_set` —
  **CORRECTED per the BATCH-CLOSE Phase-1 antagonist reconciliation**: the first writing of this
  position added a march-specific referent-widening arm whose own justification was
  self-contradicting, and it has been reverted). Re-verified directly rather than assumed:
  `operands_for` already produced a non-empty operand dict for `march` (this half of the original
  diagnosis was correct); clause 3's PRE-EXISTING `q.referents` reading — no new code, no
  referent-kind filter — already forms a real `Candidate` whenever a Question names ANY
  Rung-kind referent, not only a settlement one. ⚠ **CORRECTED AGAIN, the layer-conformance
  ATTACK stage, BATCH-CLOSE Phase 2**: this bullet previously named "no `questions_for` SOURCE
  ever offers a settlement referent (measured: 0 of 81 referents in `build_realm(0)`)" as the
  actual, still-real blocker — that measured the wrong variable, since Candidate formation is not
  gated on referent kind. **The real reason `march` stays in the never-attempted set is
  UNMEASURED** (`hole_register.yaml` H-175); the retraction is not replaced with a different
  assumed cause. `test_march.py::test_a_real_chooser_forms_and_folds_a_march...` runs a real
  chooser (`make_chooser`/`pack_scenes`, not a hand-built `Act`) through the genuine
  RESOLVE→ENCOUNTER pipeline to a real `field.lost` (kind check only — the casualty-body
  assertions were dropped from this test in the same `/simplify` pass noted above), with
  `Act.via` read off the chooser's own derivation rather than hand-set. 10 passed.
- **`H-151`'s `cite:` corrected** to match: the "unreachable from the corpus either way" claim
  never held on close examination — a constructed `Question` reaches it through clause 3's
  pre-existing reading alone, no arm involved; the row's own scenario (same-faction march) is
  still not exercised by the NATURAL corpus, for the same UNMEASURED reason H-175 now names, not
  for the reason the old citation gave.
- **`test_combat_bridge_seam.py` confirmed to need no successor**, its three covering tests re-run
  (6 passed) — one citation drift caught and fixed directly rather than parked:
  `seam/wrappers/combat.py:203-208` had moved to `:195-201`; the stale citation in
  `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md:788` is corrected to match.
- **`test_f7_smoke_oracle.py`/`test_mc_v18_regression.py` deliberately left untouched**: read in full
  rather than trusting the plan's prediction that `VICTORY_THRESHOLD`/Hafenmark "die"/"close" here —
  they don't; both files are `28-iii`'s (SPINE-DELETE) own `FORK:` set, not this position's.

⚠ **THE DISCLOSED GAP, NOT CLOSED BY THIS POSITION**: the natural corpus (`build_realm(0)`'s own
organic Questions) never offers a settlement referent to anyone, so a real field battle reachable
from zero test-authored input is not demonstrated — only the chooser-formed one against a
constructed Question described above (BUILT bullet 2; genuinely chooser-formed as of the antagonist
correction, not corpus-organic). WHY the natural corpus never offers one is UNMEASURED
(`hole_register.yaml` H-175, `H-80`-adjacent but distinct) and was correctly left out of this
position's scope. Read against the retirement plan's own gate wording
(`PROPOSAL.md:104`: *"a battle executing from a real chooser-formed decision"*) **this now
satisfies the gate as written** — the chooser, not the test, forms the decision. `28-iii` is
accordingly unblocked.

**d · `28-iii` (SPINE-DELETE).** No change. No `loop/effects_*.py` file is touched (it deletes
`engine/mc_v18.py` and `engine/cross_scale/`, neither of which the split touched).

**e · `20-iv`.** No change to what it builds (terrain/garrison off `scale_of_rung`, `morale_start` from
season-native faction state). **If the `morale_start` wiring needs an effect-level change** (as opposed
to a pure `queries/` read, which is what the predecessor document's own candidate — members' `commit`-
Tenure degree — suggests it will be), that change lands in `effects_combat.py`, since morale is the
carrier `_scar`/`_eff_kill` already own there; this is stated as guidance for the builder, not as a
confirmed requirement, since the predecessor document's own candidate does not obviously need one.

**f–k · `29a`–`29f`, `2-ii`.** No change. These are deletions of `systems/*/sim/` trees and the
`mc_v18` kernel, not `loop/effects_*.py` builds — the split does not touch anything they delete or
depend on. `29b`'s deletion of `game_state.py` is unaffected: `proposals/2026-09-04-degree-sweep/
arm2_onramp.py:36`'s `from engine.season.loop import effects as _E` (the one external, non-CI importer
of the aggregator) reads `EFFECTS` via `getattr`, not any per-verb name, so nothing about the split
changes what that file can still reach once `game_state.py` is gone.

**l · `22` (PROC-B).** No change to the disposition (contradiction 3 stays resolved to the ceiling
candidate, per the predecessor document's §3.4). Not an effects-domain position in its own right — the
composed obstacle and `speak`'s bands are `decision/`-layer and `verb_table.yaml` work; `speak` itself
has no `_eff_speak` (it is one of the verbs the corpus's own accounting names as having no predicate/
effect at all, per the live `corpus_run` re-verified this session). **If `22`'s docketing work
(steps 11–16) needs an effect for `open_case`/`determine`'s continuation, both now live in
`effects_information.py`**, not a monolithic `effects.py` — read `_eff_open_case`/`_eff_determine`
there, alongside the shared oblige-term helpers (`_new_oblige_term`, `_oblige_term`) they call from
`effects_shared.py`.

⚠ **BUILD ATTEMPTED 2026-09-30, commit `a1282b02` — PARTIAL, NOT CLOSEABLE THIS ROUND.** Of PHASE 2's
sixteen steps (`21_RECONCILIATION.md:565-580`): **steps 6, 7, 9, 10 were already DONE**, shipped by
positions `18` (PROC-A) and `19` (U7-remit) under different handles, confirmed against the live code
rather than assumed. **Step 8 was BUILT** (documentation-only — `release`'s row already covered a
disposal `oblige` correctly; it was missing the citation of D-5's ruling for why that is the only
route, now added). **Step 7 carries a disclosed, pre-existing caveat**: `judging_set`'s `matter`
parameter is accepted but not yet load-bearing (`world_q.py:326-341`'s own docstring), since nothing
yet maps a docketed matter to a governing arrangement row.

**Steps 11 (partially), 12, 13, 14, 15, 16 are OPEN, and together constitute the proceedings
subsystem's actual contest-resolution core — a new provider module, an obstacle model, and
degree-keyed effects for `speak`/`determine` — not a routine addition.** Specifics, each verified
against the working tree:
- **Step 11**: C-1's mechanism (the disposal `oblige`, docket clearing, the write-gate clause) is
  fully built and tested at position `19`. **C-7's vote-quorum conjunct is not** — the `cardinality`
  requirement form has zero Python implementation (`data/requires.py:765-770` raises `SystemExit` on
  any cell that tries it; only `confer`/`revoke` use the sibling `basis` form). Building it needs a
  second referent (which Proposition is "the disposition" a bench member's `commit` targets) that no
  existing operand or Query derives, and `commit` itself never executes in computed play today
  (`H-156`) — a naive fix would make `determine` refuse unconditionally, regressing two currently-
  passing tests. Registered already at `H-161`; no new row added.
- **Step 12**: `speak`'s row is still the pre-existing stub (`verb_table.yaml:793`, `requires: "—"`,
  no typed cell); no `_eff_speak` exists anywhere in `loop/effects_*.py` (confirmed by grep, this
  document's own §1.4/§3 already noted this independently). The full target spec exists at
  `04_VERBS.md:59-80` but is coupled to step 13's manifest row (a `"contests: a matter"` prize needs a
  registered subsystem to resolve to, which does not exist until step 15's provider).
- **Step 13**: the two prize repoints (`rosters.yaml:1084-1106`) are already correctly marked
  `interim: true`, waiting on this step; the `rung=` fix (C-8) is real but has no reader to verify it
  against yet (nothing dispatches on `Scene.place`, which does not exist as a field — `place_of(w,
  event)` is the actual current owner of that fact, a citation correction to C-8 itself).
- **Step 14**: no obstacle-composition code exists anywhere in `engine/season/`. PHASE 0 already found
  `M-7` (the deprivation-floor candidate) FAILS when run — the redesign this step specifies (the
  ceiling candidate, injected and swept via `sigma_leverage`) is unbuilt, not merely untested.
- **Step 15**: no nested-run provider module exists; `chronicle` (to be deleted here) is still live
  (`rosters.yaml:399`, `epistemic.py:516`).
- **Step 16 (THE BAR)**: not attempted, and could not have passed — nothing exists yet for two seeded
  proceedings to run through.

**This is not a scope failure of the dispatch; it is the position's real size**, undiscovered until
built against rather than assumed from the plan's own one-line summary. `22`'s own gate for `2-ii`
(§2 above) is not met until this closes. Whoever resumes this position should treat steps 12–16 as
their own build, sized and possibly batched the way this document's §BATCHING guidance would size any
phase this large — not folded back into a single dispatch.

**m · `22a`→`23`→`22b`.** No change to the disposition. **`23`'s loader-invariant work should be aware**
that `data/verbs.py::_derive_openers_from_effects` no longer walks a single file — it walks
`data/files.py::effects_modules()`'s discovery of every `loop/effects*.py` sibling (the fix this
session's split required, §1.6). `23`'s own loader-invariant additions (invariant 4 widened, invariant
7) should follow that same "compute the corpus, never list it" pattern if they need to enumerate the
same file set, rather than re-deriving a hand-written list that will go stale the same way the pre-fix
version did.

**n, o, p · `24g`, `24h`, `26`.** No change; all three remain gated as the predecessor document has
them (two Jordan items unchanged, one Jordan position unchanged).

---

## 4. Jordan roster — items 14, 15, 16 only (supersedes those three items in the predecessor document's
§5.1; its other ten items and all of §5.2 are unchanged and not restated)

These three items were already corrected in place in the predecessor document by commit `30dc8c65`,
per Fable's review (§1.3 above gives the substance of each correction). They are not restated here a
second time — this section exists only to confirm, for the record, that the version currently in
`2026-09-28-the-plan-one-order-mc-v18-retired.md` §5.1 items 14–16 **is** the corrected version this
pass produced, not a stale one. Read them there.

---

## 5. What this document does not do

It does not re-architect any unbuilt Phase-4 position — the honest result of §1's audit is that none
needed it. It does not re-litigate the nine contradictions (§4 of the predecessor document) or the
Jordan roster's other ten items (§5.1) — the NERS pass did not touch them. It does not restate Phases
1–3, which are unchanged and whose own state is current in the predecessor document's §2.3. Anything
not named in §2–§4 above as changed should be read as unchanged there.
