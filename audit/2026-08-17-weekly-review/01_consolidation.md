# Consolidated outstanding-item register + corrections to `00_findings.md`

## Status: REFERENCE — observation with evidence; nothing ruled, nothing executed

## Date: 2026-08-17 · Lane: IN (cross-cutting) · ED-IN-0194

**Method.** Three Fable-5 `valoria-critic` agents ran read-only and concurrently, blind to each other
(no Write, no Edit, no Bash — independence is structural, CLAUDE.md §10): one adversarial pass over
`00_findings.md` receiving it as *output, never reasoning*; one independent interrogation of the
fifteen commits `d36498f`..`f2fc307`; one exhaustive outstanding-item census. Per §10 the audit tier
does not author — this document is written by Opus from their reports.

⚠ **Every claim below that changes a conclusion was re-verified by execution before being written
here.** Two agent claims were wrong or half-wrong and are recorded as such in §1.4 and §2.6. An agent
report is evidence, not a verdict.

---

## 0. What changed as a result of the audit

`00_findings.md`'s eleven findings and five throughlines were all **CONFIRMED** against the tree by an
independent critic that re-derived every `file:line` itself. Four things were nonetheless wrong or
missing, and one of them was the document's headline number.

| # | Correction | Direction |
|---|---|---|
| **X1** | TL-1's "overwhelmingly apparatus" — **REFUTED by measurement** | my claim was wrong; the true finding is sharper |
| **X2** | The "433 of 452 PP citations" figure is **stale**; the current measurement is 531 of 537 | repeated a superseded number from CLAUDE.md |
| **X3** | The "ninth ladder" lesson is **misattributed** — those ladders were on `main` three days earlier | the tree's own filed lesson is wrong, and I passed it on |
| **X4** | Four categories present in my own instrument output and never reported | omission, no disclosure |

---

## 1. Corrections

### 1.1 X1 — TL-1's headline was an uncontrolled number, and it was wrong

The critic named this as the single claim it would bet against, on the correct grounds: it was the
only load-bearing figure in the document with **no reproducing instrument on disk**, and "the great
majority is apparatus" is a judgment word carrying a throughline's thesis with no measurement behind
it. That is §0.1 point 4 — *a number without a control is not a measurement, in either direction* —
applied to my own headline. The critic could not measure it (no Bash). I could, so I did.

**Measured over `d36498f~1..f2fc307`, 97,609 lines of churn (+82,021 / −15,588):**

| share | churn | files | category |
|---:|---:|---:|---|
| **53.8%** | 52,545 | — | **machine-generated artifacts** |
| 14.1% | 13,785 | 65 | `systems/` + `engine/` — design and engine |
| 12.2% | 11,947 | 42 | `audit/` prose |
| **11.9%** | 11,643 | 110 | `tools/` + `skills/` + `tests/` — **apparatus proper** |
| 8.0% | 7,689 | 32 | everything else |

Within `references/` (57.0% of the week on its own), **94.4% is generated artifacts** and 5.6% is
hand-authored. `references/glossary/glossary.json` **alone is 43,419 lines = 44.5% of the entire
week's diff**, rewritten in **8 of the 15 commits**.

**So "overwhelmingly apparatus" is false.** Hand-authored apparatus is 11.9%, and the design/engine
surface received *more* churn than tooling did. The corrected finding is more useful than the one it
replaces:

> **The diffstat is nearly meaningless as a measure of work on this repository, because more than
> half of it is one generated file being rewritten.**

This independently explains an observation `HANDOFF_IN.md:66-71` recorded separately and did not
connect: two sibling branches collided on 18 files "over nothing," **every one a regenerated
artifact.** The regeneration churn *is* the merge-conflict surface. See §4 for the disposition
question this raises.

**What survives unchanged:** TL-1's actual thesis — that the ratchet regressed while the window
shipped — is independently corroborated by two earlier, non-self measurements: 173/60 at
`audit/2026-08-11-consolidation-sweep/00_consolidation_sweep.md:34`, and +115/+56 in a prior handoff
entry. Only the diffstat characterisation was wrong.

### 1.2 X2 — the PP-citation figure I quoted is superseded

`00_findings.md` §6 repeated CLAUDE.md §0's "433 of 452 distinct `PP-NNN` numbers cited in live
surfaces resolve to no register on `main`," attributing it as a standing caveat. It is stale.
`ED-IN-0190` (`registers/editorial_ledger_in.jsonl`, 2026-08-14) measured **537 distinct PP ids
across 318 live files**, of which 6 resolve — i.e. **531 of 537**.

Both numbers now circulate. `CLAUDE.md:34` carries 433/452; `HANDOFF_IN.md:154` restates it; the
instrument that measured 531/537 shipped in the same window. **Two uncontrolled figures for one
quantity, in the governing document, is §0.1 point 4 in the surface that defines §0.1 point 4.**

Correct statement: **531 of 537**, per `ci_pp_frozen_check`'s census, superseding 433/452.

### 1.3 X3 — the "ninth ladder" lesson is misattributed, and the tree teaches it wrongly

`HANDOFF_IN.md` and `tests/valoria/test_degree_ladder_single_owner.py:11-16` both record #311's
generalisable lesson:

> *An audit instrument's ROSTER is a claim about the tree, not a measurement of it. The census was
> trusted because it was written down and re-runnable; it was still an undercount.*

That reads as instrument blindness. It was not. Both "newly discovered" ladders were **already
enumerated on `main`**, in a table merged three days earlier by #304
(`audit/2026-08-11-systems-python-architecture-audit/00_findings.md:184-194`):

| row | site | returns |
|---|---|---|
| **#2** | `engine/autoload/sigma_leverage.py:284` `degree` | `int` 0–3 |
| **#4** | `systems/combat/sim/combat.py:161` `_degree` | `'Failure'/'Partial'/…` |

They are rows **2 and 4 of 8** — the first two non-owner rows in the table. Not obscure, not
buried. The 2026-08-12 census simply did not consume the audit that had landed on `main` the day
before.

**The real lesson is different and more actionable: a later instrument in the same window did not
read the earlier instrument's committed output.** The filed lesson sends the next session to harden
rosters; the actual defect was that `main` already held the answer and nothing made anyone look.
Both statements are worth keeping — but the filed one is currently the only one, and it is the wrong
half.

### 1.4 X4 — four categories my own instruments produced and I did not report

All four are in output I generated and then read selectively. This is the more embarrassing class.

1. **Mode B omitted in full, without disclosure** — 28 implied-but-missing pairs
   (`vector_audit/02_weakness_register.md:28-49`). §4 of `00_findings.md` covers Modes A, D, E, F, G
   and H and silently skips B. Two of the omitted pairs link my own named 4/4 hubs:
   **`Mass Battle ↔ Settlement Layer`** and **`Faction Layer ↔ Mass Battle`** — metadata-linked in
   two graphs, zero citations between them.
2. **Two canonical Key types with zero structural presence** —
   `Key: mechanical.scene_exited` and `Key: mechanical.scene_skipped`, 0 paragraphs and cite-degree 0
   (`02_weakness_register.md:95-96`). I discussed the other four members of that exact 0/0 class and
   skipped these two.
3. **63 import orphans and 91 unverified CLI entry points** (`structure_register.md:7`) — I quoted
   the same scorecard line selectively and dropped both counts. The orphan list is dominated by the
   `systems.combat.combat_engine_v1.*` family, which is probably a scripts-on-path artifact (§3
   slice 8) — but making that determination is exactly the job a findings document has.
4. **`systems.social_contest.sim.contest._kernel_tests` is a top import hub** (in 0, out 16,
   `structure_register.md:161`) — a *test* module as a change-impact hub, inside the shipped package.

**Minor, corrected:** `valoria_local.py:243` not `:242`; the registry note at `ci_checks_registry.yaml:246`
not `:245`; and TL-5's blockquote is a paraphrase of the proposal's T6, presented as a quotation.

### 1.5 One agent claim I could not sustain

The commit-interrogation lens reported that `tools/observability/PROPOSALS.md` names five proposal
files that do not exist, and that `proposals/` holds 7 files. **`proposals/` holds 12, and all 10
files PROPOSALS.md names exist.** That half is refuted; recorded here because an agent report is
evidence, not a verdict, and this is what checking it is for.

**The load-bearing half stands and is worse than the refuted half.** PROPOSALS.md declares itself
*"One deduplicated, lane-partitioned view of every unratified work item in flight"* and **omits both
of the window's own proposal documents** — `2026-08-15-character-and-faction-stats-and-progression.md`
(status: *PROPOSED — DESIGN-ONLY, HELD FOR JORDAN*) and `2026-08-16-system-scores-census.md`. See
§2.6: that held document deliberately allocated **no ED**, on the stated theory that `proposals/` is
surfaced *by location*. The location register does not show it. A held item that is on no register is
not held; it is forgotten.

---

## 2. New findings from the audit (F12–F19)

Continuing `00_findings.md`'s numbering.

### F12 — the recurrence guard cannot see the ladder form that motivated it

`test_degree_ladder_single_owner.py`'s docstring claims its source sweep means *"a ladder that nobody
enrolled still fails something"* (`:14-16`). Measured against the actual regex:

```
bands detected by _PRODUCES_BAND in an integer-band ladder : 0
bands detected in the real engine/autoload/sigma_leverage.py : 0
```

`_PRODUCES_BAND` (`:343`) matches only quoted band literals and `Degree.X` members. `sigma_leverage.degree`
**returns integers 0–3** — and it is *the ninth ladder*, the one whose discovery caused this guard to be
written. It passes today only because it is hand-listed in `HELD`, i.e. by roster membership, not by
detection. A new `return 0..3` ladder lands undetected.

The module's own comment half-admits this (`:331-335`, explaining that adding an obstacle term would
make the detector miss `sigma_leverage`) while the docstring above it claims the opposite. **This is
the exact defect the file was written to fix — a guard weaker than its own docstring — committed
inside the fix for it, for the second time in the same file's history.**

Everything else about that file is exemplary. This hole is not.

### F13 — `ci_supersession_check` cannot fail, is listed as blocking, and is empty of the one event it exists for

Three defects composing into one:

1. `CLAUDE.md:401` lists supersession in the **authoritative/blocking** CI tier.
2. `references/ci_checks_registry.yaml:242-246` records `ci_job: validators-report` and states
   *"every return in `main()` is 0 and `:66` says so explicitly, so it could never gate"* — demoted
   **by this very window** (#306, G3, ED-IN-0159 §1.9, 2026-08-12).
3. `ED-IN-0187` — the window's single supersession event — appears **zero times** in the register it
   reads.

So `00_findings.md`'s F5 understated the problem. The handoff says *"no new tool is needed, only the
data."* **What is missing is the data *plus any forcing mechanism*:** even once the entries land, the
tool exits 0 unconditionally. The degree ladder is invisible to the supersession apparatus in both
directions, and the governing document says it is guarded.

### F14 — `references/glossary/` is a concordance called a glossary, and the name is why nobody questioned its size

Applying §4's two ruled tests to `glossary.json` as instantiated:

| measure | value |
|---|---|
| terms | 2,083 |
| **with `definition: null`** | **1,902 (91.3%)** |
| snake_case code identifiers (e.g. `a_casualties`, a local Python variable) | 1,853 (89.0%) |
| appearing in exactly one file | 974 (46.8%) |
| `census` + `locations` share of payload | **88.2%** |
| **`definition` share of payload** | **1.3%** |

**Idiomatic in choosing — FAIL.** A glossary is terms *with definitions*. An index of a corpus's
principal terms with their locations is a **concordance** — ordinary English, standard outside this
repo, exactly correct. The generator's docstring states the concept in words — *"What it could never
do by hand is answer **where does this term actually appear?**"* — and does not use the word. §4 says
*coin nothing that a plain word already covers*; this is the more damaging variant, **an existing
word reused for a different existing concept**, because a coinage at least makes a cold reader stop.

**Idempotent in meaning — FAIL.** Cold read yields *the file where terms are defined*. The file is
91.3% definitionless engine identifiers.

**Three aggravating factors:**
- **The name collides with itself in one namespace.** `references/glossary.md` is the curated
  authority (*"canonical reference for all term expansions"*, 27 KB, with definitions);
  `references/glossary/` is the generated concordance (3.9 MB). A file and a directory, same name,
  same parent — and the payload is at `references/glossary/glossary.json`, the word appearing **twice
  in one path meaning two different things**.
- **The correct definition exists only where a reader arrives last.** `MASTER_GLOSSARY.md`'s header
  gets it exactly right — *"Curated DEFINITIONS live in references/glossary.md; this view adds
  LOCATIONS"* — but a reader meets the name in the directory, the filename and 20 `GLOSSARY_*.md`
  files first.
- **`build_glossary.py` has zero entries in `references/ci_checks_registry.yaml`** — the same defect
  as F6b, on a second tool. §4 names that registry as a required definition site *precisely because
  it is machine-read and cannot silently rot*. The one correct definition lives in a Python docstring.

**Why this is not a naming quibble.** Called a glossary, 2.1 MB reads as a big vocabulary. Called a
concordance, the obvious question surfaces at once: *why is a derived occurrence index tracked in
git?* It has a generator, a staleness gate and no hand-edits. It is build output — and tracking it is
what made one file 44.5% of the week's diff (X1) and the dominant merge-conflict surface.

**In fairness to the instrument, its reason to exist is sound:** `glossary.md`'s content was last
swept **2026-04-30** and its maintainer was retired 2026-06-28. A curated glossary with no live
maintainer is a real rot pattern. The tool is justified; the **name** and the **tracking** are not.

**A finding buried inside it:** **278 terms are registered across the five source registries and
appear in no scanned design doc at all** (`MASTER_GLOSSARY.md:7` — 2,083 terms, 1,805 located).
Registered vocabulary with no corpus presence — the same class as the four Mode-H isolates, at 70×
the count, and surfaced by no instrument as debt.

### F15 — the repo cannot state how many items need Jordan; four instruments give four answers

| figure | source | definition used |
|---|---|---|
| ~121 | `HANDOFF.md:186` | flag count, includes flags on ratified/resolved rows |
| 114 | SessionStart banner / `session_status.py` | banner's own reader |
| 128 | `tools/observability/PROPOSALS.md:8` | "need your decision" across kinds |
| 110 | this census | `needs_jordan: true` **on open-status rows only**, last-row-wins |

None is pinned; no two share a definition. The mechanism is real and specific: `needs_jordan: true`
survives on **ratified and resolved** rows in the PC lane (ED-PC-0015..0021, 0047, 0049..0055) and MB
(0043, 0045), so any counter that ignores final status overcounts. This is the headline number of the
repo's central bottleneck (TL-3), and it is unowned.

### F16 — three authority surfaces carry statements the tree contradicts

- **`HANDOFF_MB.md:18`** — *"⛔ `main` IS CI-RED (16 failures) as of `94bb902`. READ ED-MB-0061
  BEFORE ANY MB WORK."* Measured today: `tests/valoria` **1933 passed / 0 failed**; the regime is now
  9 strict xfails under a count pin. The banner is ~2.5 weeks stale and is the **first thing** an MB
  session reads.
- **`HANDOFF.md:89` (Q6)** — *"the §5–§7 restore is **NOT done** — 327 dangling citations across 176
  files."* `CLAUDE.md:290` says restored 2026-08-15 (ED-IN-0193) and `editorial_ledger_in.jsonl`
  records ED-IN-0193 `resolved`. Root HANDOFF's ruling table is stale on Q6's execution bit.
- **`CLAUDE.md:366`** — *"10/27 modules have `doc: null`."* Measured: **9** — `faction_politics` and
  `miraculous_event` were fixed in place. (The nine: `npc_memory`, `scene_slate`, `game_director`,
  `scene_timer`, `audit`, `domain_actions`, `settlement_economy`, `engine_clock`, `scenario_authoring`.)

Add `HANDOFF_IN.md:3-72`'s PORT NOTE, which instructs a merge already executed. Four surfaces, same
class as TL-4: the repair landed on the instances the last assessment named, not on the pattern.

### F17 — `#301`'s PROPOSED status is a defect by the window's own precedent

`proposals/canonical_nomenclature_v1.md:3` still reads *"PROPOSED — not ratified"*, allocates no ED
(`:5`), and holds Phase 0 for Jordan (`:269-271`). ED-1094 makes merge ratify unless the hold is
loud. Here the *rulings* are loudly held but the **plan itself** was never flipped — and this same
window ruled on exactly that shape: **ED-IN-0173** records Jordan confirming that the alias plan's
identical "PROPOSED — RATIFIES NOTHING" status was a defect, flipped to *"RATIFIED AS PLAN OF RECORD,
holds stay held."*

Applying the precedent, this Status line is a defect, not a hold. Compounding: **no ED means no
`needs_jordan` docket row**, so its only register surface is PROPOSALS.md — which §1.5 shows is
incomplete.

### F18 — `ED-IN-0187`'s `needs_jordan` flag now asks a different question than its title

The entry carries `status: executed, needs_jordan: true`. Both held sites were **ruled on 2026-08-15**,
so the flag no longer covers what the title asks. What it *does* still cover is the reband
consumer-recalibration question (`HANDOFF_IN.md:161-170`) — real, but unstated on the entry.

An ambiguous flag on a ruled entry is precisely the T5 re-raise trap the 08-14 banner was built to
prevent, reproduced inside the entry that closed the agenda.

### F19 — the reband's design consequence is measured, unratified, and already shipped

181 of 600 cells moved **Partial → Failure (30.2%)**, scaling with Ob. Three consumer tables pay
differently for those bands: `domain_echo` (−1 to the acting faction's own stat), `zoom_in_out`
(+1 Ob on the next scene), `DAMAGE_BY_DEGREE` (0 instead of 1). Six seeded goldens and three
byte-exact field digests were re-recorded to match.

The instrument exists (`audit/2026-08-14-degree-reband-consumer-cost/reband_delta.py`) and
**reproduces the number but cannot fail**. So a 30% shift in outcome distribution is in the shipped
engine, correctly recorded, and never ratified as a design choice.

---

## 3. Consolidated outstanding-item register

Every item from all three lenses plus `00_findings.md`, de-duplicated, on two axes:
**Blocked on** (JORDAN — needs a ruling · EXECUTION — ruled or uncontroversial, merely undone ·
UNKNOWN) × **Guarded** (a named automated check fails if it stays undone).

Sorted so the items that **rot silently** come first. That ordering is the point of the table: an
unguarded item does not announce itself, and 39 of the 45 rows are unguarded.

### 3.1 JORDAN × UNGUARDED — needs a ruling, nothing will remind anyone

| # | Item | Home |
|---|---|---|
| 1 | **Faction stat roster — 4 calls**: roster (registry declares 5, `game_state.py` implements 6), Mandate base-vs-derived (`Faction.L`), Treasury-vs-Wealth, 0–7 vs 1–7 scale. Now the faction *obstacle* surface, since obstacles are ruled score/2 | `HANDOFF.md:130-160`, ED-FA-0004 |
| 2 | **ED-1051 `engine_clock` ratification — the last T0 item.** Blocks M1 J6, M3 G0, and GO-lane Gate-0 entry | `module_contracts.yaml:865-884` |
| 3 | **SC fork backlog**: ED-SC-0003/0004/0005 (P0, gates M1 J3), 0015, 0016, 0019, 0020/0021; 0027's 14 forks, 0028's 18, 0029's 10; CIP-3/7b/9b/12/15 | `HANDOFF_SC.md:271-328` |
| 4 | **Godot**: 8-item strategy register (10 `[OPEN]`), K8, first-module target, Gate-0 preconditions — none executed; `valoria-game` frozen since 2026-05-04 | `HANDOFF_GO.md:40-53` |
| 5 | **Q7 — the tenth attribute is UNNAMED.** Count ruled = 10; roster ships 9. Gates OPT-AV-1, `repo_state_armature` P5, and all Godot field binding | `HANDOFF.md:90`, `descriptor_registry.yaml` |
| 6 | **F19 reband consumer recalibration** — 30.2% of cells moved band; three consumer tables unratified | `HANDOFF_IN.md:161-170` |
| 7 | ED-IN-0151 decisions (a)–(d): articulation edges, dead-prose modules, 8 consumerless keys, 9 scale transitions. *The indexes were built precisely to unblock this* | `editorial_ledger_in.jsonl` |
| 8 | ED-IN-0113 decision policy (canon precedence) + 5 unfixed adversarial findings | `POINTER_2026-07-31_m1_program_scaffolding.md:46-54` |
| 9 | #304's six HELD items (incl. #0 `net`/`ob` naming, gating the degree family 16→1) + 37 grandfathered `*_index.md` + `sim_harness` promote-or-retire + alias-plan A1 semantics | `HANDOFF_IN.md:3378-3382` |
| 10 | MB: golden mode-matrix ruling (pre-re-base), `ROUT_CASCADE_FRAC`, withdrawal default-flips, ED-MB-0008/0009/0016/0044/0056/0057 | `HANDOFF_MB.md:1165-1173` |
| 11 | ED-MB-0065 J2 disposition — WITHDRAW / DEFER / EXECUTE-WITH-SCOPE; needs a `faction.Mil → Unit` spec first | `HANDOFF_MB.md:1177-1209` |
| 12 | FA: ED-FA-0013 (Sack tone), 0018 (Examination Ladder), BYZ-1/HAB-2 — 15 needs-Jordan entries | `HANDOFF_FA.md:149-164` |
| 13 | SE: ED-SE-0002 (Accord/Order stacking contradiction *between two canonical heads*), 0013/0014/0015/0017 — 23 needs-Jordan entries | `HANDOFF_SE.md:165-166` |
| 14 | PC: JD-2/3/5/6/7/8, Track-2 single-source-target, §C channel-leverage calibration, §11.4 Surrender/Disengage (*live spec, no implementation*), ED-911/WS-7 | `HANDOFF_PC.md:946-999` |
| 15 | W5 (weapons→JSON), W7 (deletion slices), W8 (`handoff_atomize`), W9 (AUDIT_CUTOFF retention) | `HANDOFF_IN.md:288-293` |
| 16 | FI/WR: ED-FI-0006/0007/0008 (wound contradiction ×2 + a P-06 violation), ED-WR-0008 | lane ledgers |
| 17 | #315 progression S1–S7 + §15.5 blocking calls | `proposals/2026-08-15-…md:§15.5` |
| 18 | ED-1090 span-of-control; ED-IN-0030 phantom "debt scene"; ED-885 citation confirm; ED-507/508/634 authorial content | flat ledger |
| 19 | DP-1..DP-4 decision packets — ⚠ home paths are pre-restructure `designs/audit/…`; **on-disk existence unverified** | workplan §5 `:355` |

### 3.2 EXECUTION × UNGUARDED — ruled or uncontroversial, merely undone

| # | Item | Home |
|---|---|---|
| 20 | **Q2 score/2 obstacle derivation — "wired nowhere," the largest outstanding piece.** Gates both degree holds; every fixed-Ob calibration done before it is rework | `HANDOFF.md:85` |
| 21 | **Q3 fractional dice** — `roll_net_continuous` does `int(round(pool))`; 3 sites | `sigma_leverage.py:273,284`; `core.py:52` |
| 22 | **ED-IN-0187 → 4 registers** (~30 min) — and per F13 the receiving checker cannot fail even once filled | `HANDOFF_IN.md:83-87` |
| 23 | **5 dead `POINTER_*.md` targets** + `review_core.py:136` phantom path + the false "10 target(s) resolved" summary | F1, F2 |
| 24 | **`domain_actions` doc authoring** — M1 junctures 1–2 have no owning document, while it is a Mode-A hub in 3 of 4 graphs (cite 141) | ED-FA-0002 |
| 25 | Remediation Track B: `dice_engine.TN_STANDARD` owner (2 live defs + `roll_pool`'s hardcoded `tn=7`; the committed plan prescribes a symbol that does not exist); bare-RNG sweep; **register `single_owner_check` in `ci_checks_registry.yaml`** | `02_remediation_plan.md:582` |
| 26 | Track C gate perimeter: `validate_ed_citations` blind to `audit/`; `broken_dependency_checker` blind to `engine/` | `HANDOFF.md:168-169` |
| 27 | Track D: **159 `sys.path.insert` across 131 test files**, `conftest.py` does no path setup, 18 `_load` helpers, 34 hand-rolled `spec_from_file_location` | five-lens T6 |
| 28 | Track E vocabulary + **`WI = End+6` transcription defect** | `combat_reference_v1.md:218,347` |
| 29 | Progression-found defects: **live crash `units.py:230` (`CELL_PATTERN_FN` unbound)**; strategic mass battle geometrically degenerate (`massbattle.py:1866-1894`); **threadwork History inert** (`operations.py:156` — `min(3, history+3)`, zero marginal value); duplicate non-equivalent `roll_pool`; `tribunal.py:119,122` double-rounds; conviction 9-vs-13; **Standing has four live ranges** | `HANDOFF_IN.md:3418-3423` |
| 30 | `drain_tick` has zero producers — the first scheduling subscriber raises; `public_citation` rupture unfireable | `HANDOFF_SC.md:281-283` |
| 31 | **`module_contracts.yaml:749/757` prose-in-identifier** → 6 instrument rows across two independent tools (F4) | F4 |
| 32 | Q1b generated CURRENT.md head table; Q4 PP sweep (**531/537**, X2) | `HANDOFF.md:84` |
| 33 | FA/SE ratified-text authoring: ED-FA-0020/0021+E11/0022/0023; SE Za/Ordenanza; B12 propagation | `HANDOFF_FA.md:113-139` |
| 34 | **L/PS wiring (E5) — "the single highest-priority open item in this entire thread."** Spec exists (`lps_wiring_v1.md`, PROPOSED); `lps_inert_check` was 100/100 red, report-only | `HANDOFF_SE.md:130-140` |
| 35 | 9 key types with no consumer (`env.crisis`, `mechanical.season_change`, `era_transition`, `second_calamity`, `settlement_captured`, `theocracy_unification_declared`, `state.settlement_revolt`, +1); **`meta.legacy_event` has neither producer nor consumer** | `EXECUTION_MAP.md:114-171` |
| 36 | **F14 glossary/concordance**: rename + the track-or-untrack decision; 278 registered terms with no corpus presence | F14 |
| 37 | **F16 stale banners** ×4: MB CI-RED, HANDOFF Q6, `CLAUDE.md:366` 10-vs-9, `HANDOFF_IN.md:3-72` PORT NOTE | F16 |
| 38 | **F15** — pin one `needs_jordan` definition and one owner | F15 |
| 39 | **X4's four unreported categories**: Mode B's 28 pairs, 2 zero-presence Key types, 63 orphans / 91 CLI entries, `_kernel_tests` as import hub | §1.4 |
| 40 | ED-IN-0148/0149/0150/0158/0159 umbrellas; M2 S1 fork-1 remap + fork-2 strike; ED-PC-0006 calibration; LB-24 read-routing bug | lane ledgers |

### 3.3 Guarded — a mechanism exists

| # | Item | Guard | Strength |
|---|---|---|---|
| 41 | ⛔ **Q5 ledger chunking — NO LONGER PENDING, IT IS OVERDUE.** See §4 Q-D | `ci_register_size_check` 50,000-token **blocking** cap; **108 tokens of headroom** | **The deadline passed during this session** |
| 42 | 2 HELD degree-site migrations (combat Ob-first; sigma_leverage injection) | `test_degree_ladder_single_owner.py:187` fails **on resolution** | Partial — fails on landing, **nothing fails on delay**; and F12 shows the sweep half is blind |
| 43 | 9 KNOWN_RED MB defects | strict xfail + `EXPECTED_KNOWN_RED = 9` count pin + stale-entry falsifier | **Strong** — fixing one forces the count down |
| 44 | Pipeline wiring gaps (world-npcs, world-knots, accord-echo, combat-bridge) | strict, live-introspected, **self-lifting** xfails | **Strong** |
| 45 | H4/H11 −3.8σ asymmetry; over-lethality (~85% vs 15–30% band); RC-5 gauge rows; scope_ratchet burn-down | non-strict xfails (`test_gauge_invariants.py:63,102`); `scope_ratchet` report-only | **Weak** — non-strict xfails can silently xpass; the ratchet records REGRESSED and cannot act |

### 3.4 Double-counting — one problem wearing several IDs

Recorded so the next reader does not treat one item as six:

1. **Score/2 Ob + fractional dice + both HELD sites** = one ruling family (ED-IN-0187 / Q2 / Q3).
   Rows 6, 20, 21, 42 are the same program.
2. **ED-1051** = T0 register row = M1 J6 `blocked_on` = M3 G0 blocker = GO Gate-0 = `module_contracts.yaml:884`
   doc:null hold = `decisions_t0_open`. **One decision, six surfaces.**
3. **ED-MB-0061** = ledger entry = MB's ⛔ banner = 9 KNOWN_RED rows. The "16 failures" and "9 xfails"
   framings are the same defect set at two dates.
4. **Faction stats** = root HANDOFF needs-Jordan block = ED-FA-0004 = `descriptor_registry` vs
   `game_state.py` = the subject of both August proposals.
5. **J2 mass battle** = ED-MB-0065 = `test_j2_mass_battle_seam` = ED-IN-0127/0128 keep-pins.
   ⚠ **The canon question is CLOSED** (Jordan, 2026-08-03). Five audit lenses have now re-filed it as
   open; this register is not the sixth.
6. **PP citations** = CLAUDE.md §0 = ED-IN-0147 = Q4 = ED-IN-0190 — and X2 shows the figure itself
   forked into two.
7. **ED-IN-0103 centralization** = open ledger entry = a dead pointer target = interlock warnings
   inside two other pointers.

---

## 4. The four questions this consolidation puts to Jordan

Not new work — the smallest set of decisions that unblocks the largest number of rows above.

**Q-D. Where do new IN ledger entries go?** ⛔ **This one is not a question about the future.**
`00_findings.md` filed F11 this morning at ~1,100 tokens of headroom under a **blocking** cap.
Filing the consolidation's own ledger entry **hit the cap** — `50,048 / 50,000`, the commit refused —
and the entry had to be cut back twice. **The file now stands at 49,892 with 108 tokens of headroom,
which is less than any entry anyone will write.** The next IN session is blocked before it starts.

The finding demonstrated itself inside the session that reported it, which is the strongest evidence
available that Q5 was mis-triaged as "not started" rather than "overdue." The sanctioned action is
recorded at `ci_register_size_check`'s own output — *archive WHOLE settled ids to the `_archive`
file, never individual rows* (the ED-IN-0112 incident: the ledgers are append-only, so an id's
effective status is its LAST row, and moving only the resolved row silently reverts it). **What is
not decided, and is the actual ruling needed:** Q5's companion-index shape, and **which file new
entries land in afterwards** — the archive is already the larger file (131,302 tokens) and the
pre-cutover convention made it the primary allocation surface for ED-IN-0160..0182. Chunking that
does not answer that reproduces the problem one file over.

Three more registers are over 85%: `module_contracts.yaml` 87%, `editorial_ledger_in_archive.jsonl`
88%, `tests/coverage_matrix.md` 94%.

**Q-A. Does the concordance stay in git?** (F14, X1, row 36.) It is 44.5% of the week's diff, the
dominant merge-conflict surface, and correctly named it would never have been tracked. Untracking is
a one-line `.gitignore` change plus a CI-artifact step; renaming touches 20 generated files, a
directory, a generator and a staleness gate. Both are cheap now and get more expensive monthly.

**Q-B. Who owns the ratchet burn-down?** (Row 45, TL-1, L5 — open since 2026-07-28.) `ed.stale` is
198 against a ceiling of 76 and rising. Until someone owns it, every audit adds rows to §3 and
nothing removes them — and this document is itself an instance of that.

**Q-C. Which one `needs_jordan` number is real?** (F15.) Four instruments, four answers, no shared
definition. It is the headline metric of the repo's stated central bottleneck.

## 5. Coverage — what this consolidation does not cover

Stated because a tidy register that silently dropped a surface would be worse than an honest gap.

- **`HANDOFF_IN.md` (280 KB, ~3,433 lines) was not exhaustively enumerated.** The census read ~600
  lines plus the section map; `## Pending` (802–1532) and `## Next actions` (1779–2242) — ~1,190 lines
  — were **not extracted item-by-item**. Items living only there are missing from §3.
- **`HANDOFF_PC.md` lines 47–855, `HANDOFF_SC.md` 7–224, `HANDOFF_FA.md`/`HANDOFF_SE.md` 11–107,
  `HANDOFF_MB.md` 30–1146** were sampled, not enumerated.
- **76 bare-`open` flat ledger IDs** are enumerated by ID, not described.
- **`PROPOSALS.md`'s FA/SE/WR/IN/GO sections** were not read (mitigated: their ledgers were censused
  directly). Master workplan §2–§4 and Appendices A/B not itemised.
- **Key producer/consumer sets** were taken from the generated `EXECUTION_MAP.md` / `KEY_INDEX.md`
  rather than re-derived from the registry plus code — staleness there propagates into row 35.
- **DP-1..DP-4 packet files**: on-disk existence unverified (row 19).
- **Frozen `tests/sim/` trees** were checked only via the DECLARED_ADAPTERS registry, not swept.
- **No campaign balance was executed** — no CI job runs `mc_v18`; §7's gap is unchanged.
- **`godot/`** was reached by no instrument here, as it was by four of five lenses on 2026-08-14.
