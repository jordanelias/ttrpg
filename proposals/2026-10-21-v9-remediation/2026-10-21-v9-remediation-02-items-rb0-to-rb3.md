# v9 remediation proposal, part 2: items: RB-0 to RB-3

## Status: PROPOSED. Merging this file ratifies nothing: every item, ask and edit below is HELD BACK (ED-1094's loud exception). Jordan ratifies or adopts item by item, as edits to the v9 parts it names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2: one active plan per lane). On adoption its items become v9 positions and these files are deleted with a `FORK:` row. **Home of v10 positions** since the v10 adoption (`ED-IN-0299`): this file holds the full spec of the v10 positions whose plan row names it (rows: `workplans/valoria_master_workplan_v10_part3.md` §1; handles: `workplans/valoria_master_workplan_v10_part12.md` §1; where `workplans/valoria_master_workplan_v10_part13.md` amends a home, the amendment governs), and is deleted with a `FORK:` row when its last position lands (v10 head §9 step 6).
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. It moves no row of THE NINE; a row moves only on its own `measured:` block.
## Parts, in reading order: `2026-10-21-v9-remediation-01-verdict-and-coverage.md` → `2026-10-21-v9-remediation-02-items-rb0-to-rb3.md` → `2026-10-21-v9-remediation-03-items-rb4-rb5-and-index.md` → `2026-10-21-v9-remediation-04-asks-edits-measurement-and-risks.md`.

## 2. The items, batched

**Field key, used on every item.** `closes` · `R` (rows moved, and which way) · `class` (a/b/c/d) · **`Layer`** (what it
binds · the 04 row / invariant / axiom touched · seam crossed? · the one owner of the rule) · `change` (files, lines, the
edit) · `falsifier` (with its control) · `verify` (the narrowest command) · `hash` · `gates` · `tier` · `revert`.

**Layer 1 properties every `engine/season/` item keeps** (the user's binding requirement). Each item's Layer field says
which it touches. One standing self-check per batch is in §2.7.

| property | where Layer 1 states it | how an item keeps it |
|---|---|---|
| a person-side function takes no `World` | 04 §A.2 (`decision/`: "NO World in scope"; `person_q`: "a `PersonInterior` snapshot only"), PART D rows 2, 41, 42; AX-2 | no item adds a `World` parameter or import under `decision/` or to `person_q`. Stamps (REM-21) live in `queries/world_q.py`, called by the loop at the barrier. The person side receives only ids carried as classes, as IN-53 D1 already does |
| one loader per data family | 04 §B.13 (ID-12, ID-5, ID-13: "read at load by **one** loader"); §C.8-10 ("a value lives in one file, read by one loader") | `verb_table.yaml` is read only by `data/verbs.py::_load_verb_table`; `rosters.yaml` only by `data/rosters.py`. A new column or class is validated there, never re-parsed elsewhere |
| no tree-wide guard | `CLAUDE.md` §0.05 ("NO TREE-WIDE GUARD IS LICENSED"), §0.1 pt 5 | every new check is a load-time or construction-time refusal on one data family (the `check_effects` precedent), or a test of one behaviour |
| no Layer −1 | `CLAUDE.md`'s layer section | no item writes a rule about how rules are followed. Layer 0/1 text changes are proposed text for Jordan (§4.2) |
| `engine/` resolves modules by role | `CLAUDE.md` §3; `engine/substrate/composition.py`; `PATH_SEAM_ALLOWED` shrink-only | REM-31 and REM-32 reach `modules/combat` and `modules/mass_battle` only through the existing composition rows and `seam/wrappers/*`. No item adds an import of `systems/` or `modules/` under `engine/`. Its execution artifact is `tests/valoria/test_engine_does_not_import_systems.py::test_importing_every_engine_module_pulls_in_no_subsystem` |

**Items that would breach 04 or an AX as first drafted, and how each was redesigned (none goes to Jordan):**
1. REM-21 as first drafted put a `Site` stamp in `decision/options.py`. That breaches PART D row 2 (a decision reads world
   truth): `opening_set` cannot ask what kind an id is. **Redesigned:** the stamp is `world_q`-side at the barrier, the
   IN-53 D1 shape.
2. REM-29 as first drafted widened `places_named` to drop full rungs before formation. That hands the person world truth
   (capacity) they do not hold (AX-2; R-08 "not omniscient"). **Redesigned:** capacity becomes a typed conjunct that the
   fold refuses on and the refusal's read rides `Event.observed`. This is 04 §C.4's scarcity channel ("`transfer`'s
   `stores >= amount`, checked against the folded world"), and the person learns by failing (the W-B precedent).
3. REM-27 as first drafted filtered `march` targets by a literal `settlement`. That breaches PART D row 28 (a branch on a
   rung-kind member). **Redesigned:** the stamp reads `rosters.yaml: march_target_kinds`, the roster
   `loop/sides.py:84` already enforces, so the stamp and the ENCOUNTER refusal cannot disagree.
4. REM-40 as first drafted declared `act.ineligible` in `rosters.yaml`. That is a third kind source D-25 does not admit
   ("or the derived roster is not derived", 04 §F.20b). **Redesigned:** per-verb eligibility-refusal kinds, F.20b's
   first option.
5. **(rev. 2, C-01)** REM-15 as first drafted set the copied World's `world_seed`. That changes every id
   (`state/ids.py:16-19`, 04 §A.2 `state/ids`) and every `q.id` tiebreak, so its falsifier could not separate a draw
   effect from an id-keying effect (`CLAUDE.md` §0.1 pt 2). **Redesigned:** only the chooser's draw factory takes the
   draw seed.
6. **(rev. 2, C-02)** REM-41 as first drafted measured only seeded runs. Those never reach S27.4's `attempt.refused`, so
   its "no raise" falsifier was vacuous on that path. **Redesigned:** REM-40 declares the S27.4 kind, and REM-41's
   measure-first step runs `engine/season/tests`.
7. **(rev. 2, C-10)** REM-10 as first drafted changed `attribute`'s iteration and tuple. That changes five callers, one of
   them a test that hands it a one-act stub. **Redesigned:** a sibling over one shared body.

---

### 2.1 RB-0 · PLAN — v9 text only (paper; no code, no hash)

**Placement:** P3 §B.0 R5 ("EDITS only under … a record file"), a lane that merges first because RB-1's re-take readings
quote it. **Lanes:** 1. **Tier:** Sonnet producer (`valoria-author`, writes to the named v9 parts), Opus `valoria-critic`
on REM-01, REM-05 and REM-06, the three edits that change what a `met` asserts. **Budget:** ~60k working (P2 by section,
P3 §B rows, P5 §J.2).

**REM-01 · Make v9's unmeetable count true.** closes F-A (count), edit 1. R: none moves; the plan stops overstating M1.
class (a). Layer: binds the agent (the plan); touches no 04 row; no seam; owner = P1 §1 and P2's preamble.
change: P1:191 and P2:38, text in §4.1 (E-1, E-2). falsifier: after the edit, the count stated in P1:191 equals the number
of rows in P2's summary table (`:22-32`) whose `earliest met` cell is "none under v9" or "not before …" with no position
named, plus the rows marked conditional. Control: the same count taken on the base text reads two, and P2:30 already names
a third, so the old text fails it. verify: `grep -n "cannot read .met" workplans/valoria_master_workplan_v9*.md`. hash:
none. gates: none. revert: restore the two sentences.

**REM-02 · R-05's scope, denominator and missing rows.** closes F-D (a), F-K 5, edit 4 (rows, 44/45), edit 5 (scope),
the R-05 half of F-B (`restore`, `transfer` untracked). R: R-05 unchanged in status; its table becomes able to show the
two regressions. class (a). Layer: binds the agent; reads 04 §B.13's derived roster only as vocabulary; no seam; owner =
P2 §R-05. change: P2:227-231 (44/45 → 46, scope sentence, the 21 → 17 → 16 trend); a `restore` and a `transfer` row in
the table at `:233-257`; a caveat that "never attempted" rows read under REM-10's repaired instrument from RB-1 on (§4.1
E-3, E-4). falsifier: each figure in the new rows reproduces from `SP/aperture_2_0.txt` lines 119 and 129 (realm) and
223, 233 (spine) at HEAD `b70b5af`, PYTHONHASHSEED=0; a figure that does not reproduce is struck. Control: the old row
text "realm: only `restore` executes (19)" fails the same check (27/0). verify: `PYTHONHASHSEED=0 python -m
engine.season.harness.aperture 2 0` (the baseline horizon; §5). hash: none. gates: none. revert: the text.

**REM-03 · R-04's section: re-read the scales owners and schedule IN-46/IN-47.** closes edit 2 (plan half), edit 10,
F-H (a), finding 2's pointer. R: R-04 toward `met` (every `scales:` row gets an owner). class (a). Layer: binds the
agent; no 04 row; owner = P2 §R-04's scales table and P3 §B.1. change: (i) re-read each `scales:` row's `in_loop:` at
HEAD (`engine/season/requirements.yaml:70-189`) and name the owner whose EXIT supplies its execution artifact (investigation
→ FI-01's three graded inquiries, executing `research` 6 in the realm, `SP/aperture_2_0.txt:118`); (ii) replace P2:182's
"only `restore` executes (19)" with the HEAD reading (`restore` 0/27, `migrate` 1/118, `transfer` 1/47) and name REM-22
and REM-29; (iii) P2:200 and :209: "build: none" becomes "build: RB-3 (REM-30, REM-31)"; P3 §B.1 gains the two build rows
(§4.1 E-5, E-6); (iv) add the pointer "three scale vocabularies: H-89, J.2 rank 5" as a YAML comment beside
`engine/season/requirements.yaml:52-53` (C-14). That file is a Layer-2 registry `register --requirements` reads; a comment
there changes no field it validates, and P3 §B.0 R5 ("a record file") admits it. Every other part of REM-03 lands in
`workplans/valoria_master_workplan_v9_part2.md` and `_part3.md`. `register --requirements` must exit 0 after the edit.
falsifier: every one of the seven `scales:` rows names a position whose EXIT names an execution artifact; a row naming
none is the failure and stays "named residue". Control: on the base text two rows name none (P2:177, :181). verify:
`grep -n "named residue" workplans/valoria_master_workplan_v9_part2.md`. hash: none. gates: none. revert: the text.

**REM-04 · R-07's section: deaths, `chronicle`, and what conjunct 3 needs.** closes F-I (a), edit 9 (C2), edit 3's
referent half, C9. R: R-07 toward `met` (conjunct 3 gains an owner: REM-27). class (a). Layer: binds the agent; owner = P2
§R-07. change: P2:341 and :354 (§4.1 E-7): (i) conjunct 3 needs a `Won` or `Lost` field, since `Unopposed` writes no
stance (`verb_table.yaml:707-709`), and its owner is REM-27; G3's value does not gate it (C9); (ii) H-209 (a dead victim's
claim never becomes a question) is named as R-07's contributor at IN-12 step 5 (B-R), its `owner:` in
`hole_register.yaml:4514`; (iii) conjunct 1's `told_by` rests on `epistemic._ch_chronicle`, which H-214 keeps until the
`<rung kind>` reach channel lands, and that channel is a candidate M2 gate (P8:135). Any position that deletes the channel
first re-reads R-07 conjunct 1 in the same commit. falsifier: R-07's `met` text names an owner for each conjunct; the
H-209 sentence cites the hole row by id. Control: the base text names "no position is invented" (P2:30). verify: `grep -n
"H-209\|H-214" workplans/valoria_master_workplan_v9_part2.md`. hash: none. revert: the text.

**REM-05 · R-06 and R-08: make the `met`s able to see the draw and the vectorless (rev. 2, C-11).** closes F-C
(c, text half), edit 6 (text). R: **R-06 ↓ from a false `met`** (it gains a reported conjunct and a visibility conjunct);
**R-08 vis** (its realm reading over vectored persons). class (a) for the text; the threshold is (b) → JQ-1. Layer:
binds the agent. It touches 04 T-l (`04:123`, "a cohort is a Person at weight > 1; one `Person` class") and AX-2 (the
reading is harness-side). Owner = P2 §R-06 and §R-08.
**The two readings of R-08's `met`, stated (C-11).**
- Literal (P2:381): "every tie … is between candidates with equal *nonzero* score". A vectorless person's all-zero tie
  breaks it.
- Gloss (same sentence): "(the draw breaks only true indifference)". An all-zero field IS true indifference.
- **The gloss is taken, at ladder step 4, on G-1's precedent (P2:385), extended BY ANALOGY (rev. 3, critique 2 §2): G-1 is about an UNCELLED VERB, and this applies it to a VECTORLESS PERSON. The Opus critic on REM-05 is the check on that analogy:** a candidate's zero with no celled reason "is not
  a tie the person has a reason to break". So the 37 cohorts do not break R-08. They break R-06's STATEMENT ("robustly
  built with goals"), and that is where they are counted. The draft's stricter reading is withdrawn.
change (§4.1 E-8, E-9):
(i) R-06 `met` gains two conjuncts. The fourth is **reported, not thresholded until JQ-1 is answered**:
`decision_spread --decisions` prints, over vectored persons at seeds 0-2, the share where `pursuit` decides against the
share where the draw outvoted a strict top (REM-12). The fifth is **gated by ED-IN-0296 (2)**: every acting person
carries a pursuit vector, or the row names the persons declared out of scope. At HEAD 37 of 83 do not.
(ii) R-08 `met`'s sample adds the realm's **vectored** persons through `decision_spread`; vectorless persons are excluded
by the gloss.
falsifier: the R-06 fifth conjunct, read on HEAD's realm, reads FALSE (37 vectorless, `SP/zero_persons.py`); if it reads
true, it is mis-written. The R-08 realm conjunct must be able to read false: a planted vectored person whose celled
candidates tie at zero reds it. Control: the corpus `p_a` sample reads as P2:381 does today. verify: REM-12's command
(§5 M-3). hash: none. gates: REM-12 for the reading; the text can land first. tier: Sonnet producer, Opus critic (it
changes a `met`). revert: the text.

**REM-06 · R-09's third conjunct: a grade that changes something.** closes F-F (a), edit 8. R: R-09 away from a `met`
satisfiable by `speak`'s empty bands; toward an honest one. class (a). Layer: binds the agent; touches 04 §C.4 F6 and
PART D row 30a ("a contest whose outcome changes nothing"); owner = P2 §R-09. change (§4.1 E-10): the conjunct becomes
"`corpus_run`'s per-verb DEGREES line (REM-13) shows a non-combat verb besides `tell` resolved at ≥ 2 bands **whose
`writes_at(band)` differ** (`data/verbs.py:379`)". The live candidate is contested `determine` (SC-03b, landed
`d855576b`); `speak` cannot satisfy it while all four bands write `[]` (`verb_table.yaml:948-951`). falsifier: read on
HEAD it is FALSE unless `determine` resolves at two differing bands in the corpus; `speak` alone never satisfies it.
Control: the old conjunct, read on the same run, is satisfiable by `speak`. verify: `python -m
engine.season.harness.corpus_run` after REM-13. revert: the text.

**REM-08 · §J.2 and the ask-then rows.** closes edit 7, edit 3's value half, F-E (b), F-J (b), F-C (b). class (a)
for the text; each question is (b). Layer: binds Jordan's queue (agent text); owner = P5 §J.2. change: one new ranked row
(JQ-1), rank 1 amended (JQ-2), the CELL-VALUE ask-then row's number annex (JQ-3), one ask-then row at REM-32 (JQ-4), and the RB-0 ask on the design holds (JQ-5) (§3
drafts them; §4.1 E-12). falsifier: each row cites the ladder result for steps 1–5; a row missing one fails `CLAUDE.md` §0.
Control: grep shows H-187, H-188, H-200 and H-208 in 0 v9 parts at HEAD (counted this session). verify: `grep -c
"H-200\|H-208\|H-187\|H-188" workplans/valoria_master_workplan_v9_part5.md` ≥ 4 after. revert: the text.

**REM-09 · Scheduling edits: the remediation batches, the restorable rows, X4.** closes "six rows the fold cannot carry"
(plan half), NERS X4. class (a). Layer: binds the agent; owner = P3 §B and P1 §3's state index. change: (i) P3 §B.1 gains
RB-1 … RB-4's rows in v9's placement (§2.2-§2.5); (ii) IN-09 and IN-33's `BATCH: none` (P1:256, :266; P5:47, :114)
becomes RB-2b (REM-2B). **Their STATE is B and no batch is named, so a fully built v9 never restores `construe`, `evade /
defy` and `exchange`, and R-05 cannot clear its "no predicate/effect" class.** (iii) P7's MB/PC standing rows gain NERS
X4's park ("no new depth below the season seam until K-1 or M-6 is scheduled"). falsifier: P1 §3's state index has no row
whose STATE is `B` and whose batch is `none`, except those the index explains. Control: at HEAD, IN-09 and IN-33 fail it.
verify: `grep -n "| B | .*| none" workplans/valoria_master_workplan_v9.md`. revert: the text.

---

### 2.2 RB-1 · INSTRUMENTS — harness readings, hash-equal by construction

**Placement:** P3 §B.0 R5 (harness only) plus REM-14's one TRACE-only edit in `loop/predicates.py` (R9: no overlap, no
gate). It lands **before B-P** and must merge before B-Q, which edits `harness/corpus_run.py:875`, and before B-U, which
edits the STORY-BAR reader. **Lanes:** 2: {REM-10, REM-11, REM-13, REM-14} share `corpus_run.attribute`; {REM-12,
REM-15} are disjoint. **Tier:** Sonnet producers; one Opus `valoria-critic` on REM-12's classification and REM-15's
control, the two places where a mis-built instrument would mislead a Jordan ask. **Budget:** ~90k working. **Hash
expectation: EQUAL.** `World.content_hash()` at `build_realm(0)` and after `aperture 1 s` (s = 0, 1, 2) equals the
base commit's. The aperture control arm's own hash-equality line must still read equal. `runs/TRACE.txt` moves
(REM-14 adds lines); it is regenerated by `harness.report`, which is a declared non-game artifact, and `delta` must
print `PROBE FLIPS 0`.

**REM-10 · A sibling `attempts(w, n)` reads the act store; `attribute` is unchanged (rev. 2, C-10).** closes F-G,
finding 4, bucket B (C1, C7). R: R-05's reading moves sideways: contested verbs refused at admission move from "never
attempted" to "attempted and always refused", never toward `met`. class (c). Layer: harness. 04 §B.9 ("`Act`
persists, resolver-side") and PART D row 51 (a refused act is attempted: "the budget is debited at RESOLVE entry"). No
seam.
**One owner for the made/refused rule:** a private `_attribute_acts(w, acts, n)` holding today's body
(`corpus_run.py:775-786`).
change:
- `attribute(w, d, n)` keeps its signature and its `(act, made, refused)` tuple, and calls
  `_attribute_acts(w, d.resolved, n)`. **All five callers are untouched:** `aperture.py:161`, `corpus_run.py:819`,
  `soak.py:369`, `tests/test_fa01_head_seats.py:97` (which passes `SimpleNamespace(resolved=[a])` to attribute ONE act),
  and `tests/test_sc01_the_bar.py:161`.
- A new `attempts(w, n)` calls `_attribute_acts(w, tuple(w.acts), n)`. The act store holds every act from RESOLVE entry
  (`resolve.py:954`, before `_survives`, S27.4 and the contest branch).
- Two separate readers: `unrowed_acts(w)` (acts in `w.acts` whose verb is no table row; today `attribute` drops them
  silently, `:779-780`) and `foreign_kinds(w)` (logged kinds naming an act in `causes[]` that are in neither of its row's
  columns; `act.ineligible` lands here).
- Only `aperture.instrumented_season` and `run_case` (`:819`, R-05's class reading) switch to `attempts`. `aperture.py:13`'s
  docstring names the store.
falsifier, in `engine/season/tests/test_aperture.py`:
- A hand-built `speak` on a non-docket subject (refused at admission, `resolve.py:1012-1018`) and an uncontested refused
  act: `attempts` reports both attempted and refused. Mutation: point `attempts` at `d.resolved`, and the `speak`
  assertion reds.
- An act with verb `"zz_not_a_row"` placed in `w.acts`: `unrowed_acts == 1`.
- **Control:** `attribute` and `attempts` agree on every uncontested act, and `test_fa01_head_seats.py` stays green
  unchanged.
verify: `python -m pytest engine/season/tests/test_aperture.py engine/season/tests/test_fa01_head_seats.py -q`. Expected
reading: realm 2-season `ref` total moves from 761 toward the scan's 984; `unrowed` = 0. hash: equal. revert: the
sibling and the two readers.

**REM-11 · Aperture prints why each refusal refused, the post-admission refusals, and the kinds never emitted.** closes
the scan's "deciding read" table (§4 of the brief) as a repo reading; limit "F-B uses the last read"; "47 never emitted";
NERS G9. class (c). Layer: harness; 04 §C.4 ("`emit(row.refusal_for(failed_conjunct))`"), loader invariant 4; no seam;
owner = `harness/aperture.py::instrumented_season`. change: over each refusal Event of an attributed act, print per verb
(i) the failing clause where the row KEYS `emits_on_refusal` (`refusal_for`), else the last `Event.observed` read as
`stem:value`, marked `last-read`; (ii) a `post-admission` count, a refusal whose every observed read passed, which is
the write clause or `NoOpReceipt` (`resolve.py:489-494`); (iii) one line per world: declared kinds (`EMITTED_KINDS` ∪
the matrix's emission columns, read from their loaders) minus kinds in the log. **Keyed on the act (`d.act_of`, the
act store), never on a trace row's `act` column,** which is unreliable for WRITE and GAP rows (brief §4; C-09). (iv) (rev. 3, I-10) **one count line per emitted kind per world**, keyed by act through `d.act_of`. Aperture prints
per-verb att/ex/refusal kinds today (`aperture.py:155-169`), not emitted-kind counts. This line is what M-11 reads for
`field.won`/`field.lost` (R-07 conjunct 3); the scratch scan is not a repo instrument (§0.05). falsifier: `test_aperture.py` plants a
`restore` on a person id and asserts the line reads `exists:Site=0`, and a `migrate` into a full rung asserts
`post-admission` ≥ 1 (`test_migrate_capacity.py`'s world). Mutation: drop the `observed` read; both red. Control: the
realm 2-season totals reproduce the scratch scan's (`exists:*=0` 512, `post-admission` 244 by its WRITE-GAP count) to
within the acts REM-10 adds. If they do not, the scratch scan or the instrument is wrong, and the report says which.
verify: `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 0`. hash: equal. revert: the printing block.

**REM-12 · `decision_spread` splits the draw: tie against outvoted, and counts the vectorless.** closes F-C (c), edit 6
(instrument), limit "F-C on the harness slice". class (c). Layer: harness; reads `decision/choose.py`'s own ordering
(`CH.score_order`, `CH.sample_order`; "nothing is repeated", `decision_spread.py` docstring), so AX-2 is untouched; no
seam; owner = `harness/decision_spread.py::attribute_top` (`:174-205`). change: **additive, the `decider` label
unchanged** (`test_in62_decision_spread.py:103` and `:212` assert `"draw"`). Add `draw_kind` ∈ {`tie`, `outvoted`,
`None`}: `tie` when `margin <= EPS` and τ > 0; `outvoted` when the sampler's top is not the strict score top. Add
`field_zero`: every candidate's score, **less the candidate-independent `urgency` term**, is within `EPS` of 0 (C-06:
`urgency = subsistence / condition_scale`, `choose.py:238`, is nonzero in `--season` play and leaves with REM-44; the
`--decisions` slice reads `subsistence=0.0`, `decision_spread.py:174`). `read_decisions` and `play_season` (`--season`) print the split, the
outvoted margins' median against τ, and the count of persons whose every candidate scores 0. falsifier: two unit tests in
`test_in62_decision_spread.py`: a two-candidate tie at τ = 0.1 → `tie`; a strict top the planted draw reverses →
`outvoted`. Mutation: swap the two tests' order inside `attribute_top`; both red. Control: the `--null` arm (`uniform`
alignment, H-66) reads no `pursuit` (the existing `:212` test), and seed 0 reproduces 222 / 198 / 78 (`SP/draw_split.py`).
verify: `python -m pytest engine/season/tests/test_in62_decision_spread.py -q`, then `PYTHONHASHSEED=0 python -m
engine.season.harness.decision_spread --decisions` at seeds 0, 1, 2. hash: equal (it reads a built realm). revert:
remove the two keys and the print.

**REM-13 · `corpus_run` prints degrees per verb, which bands differ, and the emission-only class.** closes F-F (c), C6,
"thirteen emission-only rows". class (c). Layer: harness; 04 §C.4 F6 (`writes_at(degree)`), PART D row 30a, loader
invariant 12; no seam; owners = `run_case` (`corpus_run.py:864`, the degree count) and `data/verbs.py::VerbRow.writes_at`
(read, not edited). change: (i) `run_case` keys `degrees` by the verb of each graded Event's act, resolved through
`d.act_of` (the `storybar.read` precedent), and the summary prints `DEGREES RESOLVED BY VERB`; the old total line is kept
beside it; (ii) a static line `BANDS THAT DIFFER`: for each contested row, whether ≥ 2 bands' `writes_at` differ; (iii) a
static line `EMITS AND WRITES NOTHING`: rows whose writes are empty at every band and that have no `EFFECTS` body, each
tagged `deposit-only by ruling` where a ruling says so (`tell`, G1; the FI-01 inquiries, RS-21 item 1) or `untagged`.
**Decision rule carried to the owner, not decided here:** a row that is `untagged` and contested (`speak`) is 04 PART D
row 30a's defect in substance, so the SC lane owner of H-63 records it. [UNVERIFIED: H-63's current owner; B-N's
closing line names H-63 for `speak`'s empty bands.] falsifier: a test plants a two-verb world where `tell` grades Failure
and asserts `tell` alone is credited; a planted contested row whose bands differ prints `True`. Control: the per-verb
totals sum to the old `DEGREES RESOLVED` total on the same run. verify: `python -m pytest
engine/season/tests/test_in50_refusals_carry_the_occasion.py -q` (it imports `corpus_run`), then one `corpus_run`. hash: equal. revert: the three print blocks and the
key change.

**REM-14 · The predicate rows trace the clause they refused on.** closes "refusals with no read recorded" (`release`
39, `revoke` 5, `dispatch` 11, `convene` 3, and `march` at ENCOUNTER). class (c). Layer: **Layer 2 code
(`loop/predicates.py`), hash-neutral.** TRACE is observation (`trace_log`), not a store `World.content_hash()` folds
(`state/world.py:1338-1350`). 04 §C.4 "a refusal emits, never raises" is unchanged; no seam; owner = each `_req_*` body
(`predicates.py:304, :401, :442, :449`) and `loop/sides.py:84` for `march`. change: before each `return False`, one
`TRACE.decision(..., chose="refuse", ...)` naming the clause, in `report.py`'s cluster-key form (`"<clause> -> <ids>"`,
the `_decline_ascent` precedent at `effects_migration.py:62-66`). **Not chosen:** returning a `Verdict` with observed
reads. That would deposit claims through WITNESS and move the hash and the game (`observation_deposit_mode`). H-65
already names typing each row as the structural fix. falsifier: a test refuses a hand-built `release` of a Tenure the
actor does not own and asserts the trace holds the clause; mutation: delete the line → red. Control: `content_hash`
equal on the same seeded run with the trace on and off. verify: `python -m pytest engine/season/tests/test_g3_not_yours.py -q` (it drives `_req_release`; the
other three predicates' covering files are `test_revocation_in_holdings.py` and `test_stress_proceedings_rehost.py`). hash: equal; `runs/TRACE.txt` regenerated (declared). revert: the trace lines.

**REM-15 · A chain-level reading for R-09: vary only the chooser's draw on one built world (rev. 2, C-01).** closes F-E
(c), finding 7, R-09's "the ROLL, not the CHAIN" (`requirements.yaml:1361`). class (c). Layer: harness. 04 §A.2's
`state/ids` row (`04:162`: the mint `H(seed, tick, subject, purpose)` reads `world_seed`) and PART D row 35. No engine
change, no seam. Owner = `harness/storybar.py::drive` (`:163-182`; rev. 3, D-09).
change: a `--draw-seeds` arm. Build `build_realm(base_seed)` once and deep-copy it per draw seed. **Only the chooser's
draw factory takes the draw seed:** `draw_factory(draw_seed, lambda: w.tick)` at `storybar.py:174`. `w.world_seed`
and the act-id `mint` (`:171`) are left unchanged, so every id, every question's `q.id` tiebreak (`rosters.yaml:579-583`)
and every event id stays keyed as in the base run until the sampler picks differently. Print, per draw seed, the
cross-person chain-depth distribution and the multiset of verb-sequence chains from each first act.
**Residue, recorded in the arm's docstring and in R-09's `measured:` line:** every draw outside the chooser's factory
stays keyed to `w.world_seed`. That includes the contest seed (`seam/wrappers/combat.py:222`) and the weather draw
(`queries/world_q.py:864`). So the arm shows that **choice** makes chains vary on one world. It does not vary the rolls,
and it says nothing about roll-driven chain variance. **Second residue (rev. 3, I-12):** the chooser's draw has a second
consumer, `declare_intents` (`decision/choose.py:478-482, :495-497`). It is inert at the shipped `intent_disclosure = 0.0`
(`data/fixtures.py:773`), so the τ = 0 control below holds only at that fixture value, and the arm records the value it
ran at.
falsifier:
- The same draw seed twice → identical output (determinism control).
- Two draw seeds → ≥ 1 differing chain.
- A planted chooser that ignores its draw (τ = 0 via the fixture) → no difference across draw seeds. So the arm can fail,
  and a difference cannot come from id keying, because ids are keyed to the unchanged `world_seed`.
verify: `python -m pytest engine/season/tests/test_storybar.py -q`. hash: equal (it reads). revert: the arm.

**REM-16 · The re-take: baseline at the base commit, three seeds, relayed figures re-run.** closes limits (one run, one
seed; relayed figures), G9, edit 11's measurement, and brief 23's IN-71 note (C-09). class (c). Layer: a run, plus
record edits in **`engine/season/requirements.yaml`** (C-14: the `measured:` paragraphs of R-01, R-02, R-05, R-06 and R-08,
admitted by P3 §B.0 R5 as "a record file"; `register --requirements` validates them and must exit 0). change: no code;
the readings go in each batch's commit body and in those `measured:` paragraphs. IN-71 replaced the h9 test's rate
assertion with "what still observes the arm" (B-X body, `[RELAYED]`), so the re-take also records whether that arm's
observable still reads above its control. **Rev. 3 (I-07): REM-07 is folded in.** This item also lands E-11 (P2:24-25
names the re-takes) in `workplans/valoria_master_workplan_v9_part2.md`. The `11` command (36 `wd_chunk` cells + `wd_collect`,
P2:437-443) runs exactly twice: M-7 (RB-1) and M-10 (RB-2b's close). The protocol is §5 M-1 … M-6. Each relayed figure is re-run by the command that
produced it, or recorded as "not reproducible by a named command" with the reason: THE BAR (`engine/season/tests/
test_sc01_the_bar.py` and its sweep), FI-03's trail (the B-O test named in `46ec000`), IN-72's 0 of 11 (the B-X probe),
`chronicle` 879 → 0 (`told_holders` in `corpus_run`'s CLAIMS line with the channel off), obstacle 842/844 (`roll.py`'s
`obstacle` over the corpus). hash: none. tier: Haiku through `valoria-measure` for the runs, batched; Sonnet to read
them.

---

### 2.3 RB-2a and RB-2b · FORMATION AND SCARCITY — the verb cluster, split in two (rev. 3, I-08; declared movers)

**Placement:** P3 §B.0 R1 (both edit `verb_table.yaml`, `rosters.yaml` and count/set pins), as two serial V batches
**after B-P merges** (B-P edits `data/` loaders) and **before B-Q** (B-Q edits the same verb files and
`decision/options.py`). Precedent: B-K was a refused-verbs V batch of its own, and B-W landed its hash-neutral half
before its mover. Each serialises with B-U on `queries/world_q.py` under P3 §C.2's merge rule: whichever merges second
re-runs its hash control on the merged tree.

| | RB-2a · FORMATION | RB-2b · REACH, SCARCITY, RESTORES |
|---|---|---|
| members | REM-21 → REM-22 → REM-23 → REM-24 → REM-25 → REM-2C | REM-26 → REM-27 → REM-28 → REM-29 → REM-2A → REM-2B |
| why the cut falls here | every member shares REM-21's registry and the `Site`/`Proposition`/`Person`/`Record` own-referent stamps | three movers with distinct stop rules (REM-27's field and `RUNG_REMIT_ACTS` widening, REM-29's grammar stem, REM-2B's restores, which need `git fetch --unshallow`) |
| gate | RB-1 merged; B-P merged | RB-2a merged |
| base reading | `aperture 1 s`, s = 0, 1, 2, on RB-2a's base commit (M-2) | `aperture 1 s`, s = 0, 1, 2, on RB-2b's base commit (M-2b) |
| critic (Opus) | REM-21 (the shared primitive), REM-2C (it widens a shared class) | REM-27 (a shared class and a derived set), REM-29 (a grammar stem) |
| budget | ~95k whole / ~65k working | ~110k whole / ~70k working; both within P3 §B.1's ⚠ line |
| exit | `aperture 1 s` per item; `register --requirements` | the same, plus the R-01/R-02 `11` re-take (M-10, the E15 precedent) |

**Lanes:** none (serial; every item edits `verb_table.yaml`). **Tier:** Sonnet `valoria-author` per item;
`methodology-close` at each batch close. **Hash: MOVERS, one per item commit, each declared.** Pins re-recorded:
`test_season_shape.py`'s executed and always-refused sets, `results.json` (via `report && delta`), and any seeded realm
hash pin a test holds. `engine/tests` goldens are equal by construction, since they never import `engine.season`
(`skills/layer-conformance/SKILL.md`, "Not controls").

**REM-21 · One stamper registry, three new classes, and the question's own referents.** closes F-B's primitive (C5).
R: none by itself (**hash-equal**: no row declares a new class yet). class (a)/(c). **Layer:** Layer 2 code. 04 §A.2:
`queries/world_q` is "World first" and owns nothing; `decision/` receives ids and classes only; PART D row 2 (no world
truth in a decision); AX-2. It crosses no seam. **One owner:** a `STAMPERS` registry in `queries/world_q.py`, filled by a
`@stamps("<Class>")` decorator, the house shape of `@requires_predicate` and `@effect_for`. change:
(i) decorate the existing stampers in their current `added` order, so `questions_for`'s output is byte-identical: `Office`
→ `vacancies` + `seats_named`, `Record` → `writs_held`, `Rung` → `places_named` + `larders_in_purview`
(`world_q.py:2251-2259`).
(ii) `questions_for` stamps only the classes some row declares: `DECLARED_CLASSES`, derived in `data/verbs.py` the way
`RECORD_REFERENT_KINDS` is (`:1316-1328`), so no class literal lives at the stamp site.
(iii) `rosters.yaml: referent_classes` (`:586`) gains `Site`, `Proposition` and `Person`. Each is a carrier type name, as
the roster's note requires, and its note is written in the same commit (`CLAUDE.md` §4, define coinage).
(iv) One new stamper body, shared by the three: `own_referents_of_class(w, q, cls)`. It stamps each delivered question's
OWN plain referents whose `World.class_of` is `cls` onto that same question. `class_of` (`state/world.py:362`) returns
`Person`, `Site` and `Proposition` for those collections (`_entity_stores`, `:385-387`; verified for rev. 2, C-15). It
adds no standing occasion, so a person who knows fifty people does not form fifty petitions.
(iv-b) **One global dedup (C-15).** `Question.__post_init__` refuses an `(id, class)` pair carried twice
(`state/carriers.py:503-506`), and today's splice dedups pairwise only (`world_q.py:2254-2256`). The registry therefore
emits each `(id, class)` pair at most once per question, keeping the first in registration order. This is the order the
hash-equality falsifier pins. It covers REM-27's `fields_named` beside `places_named`, and an own-referent stamp beside a
head stamp.
(v) `manifest/registry.py` gains `check_stampers()`, the `check_effects` precedent (`:599`): every class a row declares
has a stamper, or `SeasonDriver` construction refuses naming the row. That is one refusal on one data family, not a
tree-wide guard.
**Rejected, with the reason:** (a) giving every plain referent its class for every row. That widens `migrate`,
`requisition`, `confer`, `oblige` and `comply` onto plain referents their notes measured and stopped. (b) A per-row
`referent_source:` column. That adds a second column for one choice (shape divergence); it is built only if REM-25's or
REM-27's measured cross-formation cost requires it (§6 K4).
falsifier: (1) Hash-equality test: `build_realm(0)` and `aperture 1 0` hashes equal the base commit's with the registry in
and no row declaring a new class. Mutation: reorder two stampers; the hash moves. (2) `check_stampers` refuses a planted row
declaring `Site` with the `Site` stamper unregistered. (3) The loader still refuses an undeclared class
(`data/verbs.py:655`). (4) Two stampers emitting one Rung for one question produce one pair and no `Forbidden`.
Mutation: drop the dedup; `Question` refuses. verify: `python -m pytest engine/season/tests/test_in53_vacancy_need.py -q` plus the new test file
`engine/season/tests/test_referent_class_stamps.py` (one file; it holds REM-21 … REM-27's falsifiers). revert: one commit;
the four bespoke stampers return to inline calls.

**REM-22 · `restore`, `work` and `examine` form on a Site only (rev. 3 adds `examine`, D-04).** closes F-B (`restore`
0/27, `work` 82/82), UNKNOWN `work` condition, P2:182, and `examine`'s 65 realm refusals on `exists:Site`
(`verb_table.yaml:1170-1176`: `existence` of `site` kind `Site`; att 0 in aperture, `SP/aperture_2_0.txt:101`, because the
refusals happen at admission). `examine` is R-05's "attempted and always refused in the corpus since IN-57" row (P2:252). R: **R-04 toward `met`** (settlement management regains an executing verb, if one executes); R-05:
`restore` and `work` leave "always refused" only if they execute. Otherwise they move to "never attempted", **sideways,
declared, not progress**. class (a). Layer: data (`verb_table.yaml`) read by its one loader; 04 §C.3 (`requires`
evaluated as "not known-false"; formation is the decision's); no seam; owner = the rows' `referent_class:` column plus
REM-21's `Site` stamper. change: `verb_table.yaml:873` (`restore`), `:1326` (`work`) and `:1165` (`examine`) gain `referent_class: Site`
and a `referent_class_note:` in the five rows' house form: "MEASURED before the class: formed on every referent …;
refused every time; those formations stop", with this session's figures and REM-11's base reading. falsifier
(`test_referent_class_stamps.py`): a question carrying a person and a Site forms `restore` on the Site only; a hand-built
person present at a worn Site executes `restore` through the real fold (DONE-test, P1 §0.5). Mutation: delete the
column; the first assertion reds. Same pair for `examine`: a question about a person and a Site forms `examine` on the
Site only, and a hand-built examiner present at a Site reaches FI-01's graded route. Control: REM-11's base reading, `restore`
`exists:Site=0` 27 and `examine` 65 (realm, 2 seasons). After: `exists:Site=0` = 0 for all three by construction.
**`examine`'s class move is declared:** it leaves "always refused" only if it executes. Its remaining refusals are
`present_at` (a learnable state, except that `finding.none` is not deposited, DEC-12). The measured residue is recorded, not fixed: `work` on a `dwelling` or `garrison`
Site still refuses `condition=UNKNOWN` (S12.1, `resolve.py:243-266`; [UNVERIFIED] until REM-11 shows it).
**ED-IN-0297 is untouched:** `work` still advances only a works. verify: the test file, then `PYTHONHASHSEED=0 python -m
engine.season.harness.aperture 1 <s>` for s = 0, 1, 2. hash: **mover**, declared (three rows' formations). revert: delete the three columns.

**REM-23 · `commit` forms on a Proposition only.** closes F-B (`commit` 66/0, all `exists:Proposition`). R: R-05
sideways or forward, as REM-22. class (a). Layer: as REM-22. change: `verb_table.yaml:128` gains `referent_class:
Proposition` and its note. **Interaction, declared:** IN-57's own-act screen (ED-IN-0296 (3)) is why `commit` left the
executed set. The class does not answer that ask. It removes only the 66 wrong-kind formations, and the commit body says
so. falsifier/control: as REM-22, on a Proposition referent. verify: as REM-22. hash: mover. revert: the column.

**REM-24 · `petition` forms on a Person only.** closes F-B (`petition` 32 refused on `exists:Person`; 16 executed).
R: R-04 (proceedings feed) unchanged or forward; R-05 unchanged class (`petition` executes). class (a). Layer: as
REM-22. Its counterparty is `to`, and `to` is the referent in a cell that binds no `subject` (`data/requires.py:612`), so
the class binds `to`. change: `verb_table.yaml:816` gains `referent_class: Person` and its note. falsifier: a question
about a rung and a person forms a petition to the person only. **Control that it does not regress:** `petition` executed
≥ 16 at the base, realm, 2 seasons; after, read at `aperture 1 s`. A fall in executions is reported, not hidden. If
executions fall because petitions formed on rungs were reaching a person through another route, revert (stopping rule).
hash: mover. revert: the column.

**REM-25 · `carry`, `found`, `build` form only on a Record the person holds.** closes F-B (`carry` 33/0 on `exists:petition`,
`found` 24/0 and `build` 19/0 on `exists:works`). R: R-05 **sideways**. `found` and `build` will form on nothing until
ED-IN-0297 is answered, because no computed act declares a works. They move "always refused" → "never attempted", and
the plan says so rather than calling it progress. class (a). Layer: as REM-22; one class, `Record`, shared with `comply`.
change: (i) the three rows gain `referent_class: Record`. (ii) The `Record` stamper widens from `writs_held` to `writs_held
∪ records_held_for_holding_rows`: the Records on the person's live `hold` edges whose kind is the `existence` kind of a
Record-classed row whose cell also asks `held_by` of `subject` (derived in `data/verbs.py` beside
`_record_kinds_answered`, `:552-563`; no verb name). (iii) `comply` keeps its addressee test, because its cell has no
`held_by` conjunct. **The cost the class sharing creates, measured not assumed (the H-163 precedent):** `comply` may now
form on a held petition and refuse `exists:dispensation`, and `carry` on a held writ. **Stopping rule:** if the
wrong-kind refusals REM-11 counts over these four rows do not fall below the base (`carry` 33 + `found` 24 + `build` 19
= 76, realm, 2 seasons; re-read at `aperture 1 s`), revert REM-25 and record the residue. **`give` is excluded (C4)** and
handed to B-R's `give` + Rung step with its base reading (24/0, `exists:Record` 23). falsifier: a person holding a
petition forms `carry` on it and the fold executes it on a hand-built world; a person holding none forms no `carry`.
Mutation: drop the `held_by` derivation; the first assertion reds. hash: mover. revert: the columns and the stamper term.

**REM-2C · `research` forms only on a Record the question is about (rev. 3, new; D-04, I-02 NARROWED).** closes
`research`'s 110 realm refusals, all `finding.none` at admission on `existence` of `subject` kind `Record`
(`verb_table.yaml:1213-1216`; att 6 in aperture, `SP/aperture_2_0.txt:118`). R: **R-05** sideways (`research` executes
6 today, so it stays executed). The scene slots freed move other verbs, declared. class (a).
Layer: data plus REM-21's registry. 04 §A.2 (`queries/world_q` World-first, owns nothing), PART D row 2 (the decision
receives ids and classes only), AX-2. No seam. Owner = `research`'s `referent_class:` column plus one term in the
`Record` stamper.
**The stamp, and why not the critique's:**
- Critique 2 proposed a ledger-named Record stamp. That puts every Record the person has heard of on the `Record`
  class, and `comply` (`referent_named`) and REM-25's three held-Record rows share that class.
- Taken instead: REM-21 (iv)'s own-referent body for `Record`, which carries the delivered question's own plain
  referents whose `class_of` is `Record`. `research` then forms on the document the question is about, which is what
  its untyped formation does today, minus the non-Records.
change: `verb_table.yaml:1208` gains `referent_class: Record` and its note; the `Record` stamper gains the own-referent
term, deduped by REM-21 (iv-b).
[UNVERIFIED]: how `research`'s `presence:<site>` eligibility binds once `subject` is classed. `site` binds the referent
by `_derive_operand`'s rule (`decision/options.py:845-849`). The hand-built falsifier observes it.
**Shared-class cost, measured (H-163 precedent):** `comply`, `carry`, `found` and `build` may now form on a question's own
Record referents. **Stopping rule:** the wrong-kind refusals REM-11 counts over the five Record-classed rows (`research`,
`comply`, `carry`, `found`, `build`) at `aperture 1 s` must fall below the RB-2a base (realm 2-season reference:
`research` 110 + `carry` 33 + `found` 24 + `build` 19 + `comply`'s base). Otherwise revert REM-2C and record the
residue. The structural answer is then the per-row `referent_source:` column (K4), at the batch critic's step-5 read.
falsifier: a question about a person and a Record forms `research` on the Record only. A hand-built researcher holding a
claim on the Record reaches FI-01's graded route through the real fold. Mutation: delete the column; the first assertion
reds. Control: the base reading (110 `finding.none` at admission). hash: **mover**, declared. tier: Sonnet producer, Opus
critic (it widens a shared class). revert: the column and the stamper term.

**REM-26 · `move`: measure, then class it or leave it.** closes `move`'s 19 `NoOpReceipt`s (the §10 ladder,
`effects_migration.py:62-66`), 21 `contain.path` refusals and 7 UNKNOWN reads. class (a)/(c). Layer: as REM-22. change:
**measure first** with REM-11 at `aperture 1 s`: which of `move`'s refusals are on a non-Rung referent. The base scan says
the 7 UNKNOWN `contain.path` reads are, and the 19 ladder no-ops are Rungs off the ladder. Decision rule, read off the
measurement and not the verb: the non-Rung share is fixed by the question's-own-referents stamper (REM-21 (iv)), not by
`places_named`, so `move` keeps moving toward the thing asked about. **This needs the per-row `referent_source:` column
REM-21 rejected, because `Rung`'s stamper is a standing occasion. So:** if the non-Rung share is the 7 alone, leave
`move` unclassed (7 learnable refusals) and record it. If larger, put the column question to the batch's Opus critic
with the measurement (ladder step 5) and build it only if it passes. falsifier: the reading reproduces the scan's 7/21/19
split at seed 0 over 2 seasons. hash: none (measure); mover only if built. revert: n/a.

**REM-27 · `march` reaches a field.** closes edit 3 (referent half), F-A's R-07 conjunct 3, F-H's fields (`field.won`,
`field.lost`, `army.arrived` emitted 0 times in both worlds). R: **R-07 toward `met`** (conjunct 3) and **R-04 toward
`met`** (the mass-battle `scales:` row). class (a). [CONFIDENCE: low] that one seeded realm fights a `Won`/`Lost` field
even when `march` forms on settlements, because a held settlement of another faction must be in the marcher's ledger.
Layer: data and `world_q`; PART D row 28 (no branch on a rung-kind member), so the stamp reads
`rosters.yaml: march_target_kinds` (`:907`, `data/rosters.py:840`), the roster `loop/sides.py:84` enforces. Seam: none
added; the field still enters through `seam/wrappers/mass_battle.py` and its composition row. Owner = a `Rung` stamper
term `fields_named(w, p, told)`: Rungs the marcher's own ledger names whose kind is in `MARCH_TARGET_KINDS`, offered only
to a holder of a seat granting `march`'s `remit:` act (the `RUNG_REMIT_ACTS` derivation, `data/verbs.py:1330-1340`).
change: `verb_table.yaml:694` gains `referent_class: Rung` and its note; the `Rung` stamper gains the term, deduped by
REM-21 (iv-b), since a settlement can be both a place he could settle and a field. **Collision:** B-T's IN-52 edits the same
`march` row (P3 §B.1, B-T). REM-27 lands first, and IN-52 re-runs its hash control on the merged tree (§C.2). **Shared-class
cost, measured (H-163 precedent):** `migrate` and `requisition` may form on settlement rungs, and `march` on places and
larders. **The derived widening (rev. 3, D-06):** `RUNG_REMIT_ACTS` is derived from every `remit:` alternative on a
`Rung`-classed row (`data/verbs.py:1330-1340`). Classing `march` (`remit:dispatch`, `verb_table.yaml:697`) widens it
`{issue}` → `{issue, dispatch}`, so `larders_in_purview` starts offering larders to dispatch-holding seats (25 eligible in
the realm, `SP/aperture_2_0.txt:98`) and `requisition` forms on them. The cost is named, not prevented. Stopping rule as
REM-25: total wrong-target refusals over the three rows must fall against the base, **and `requisition`'s formed count is
read before and after** (base 13 formed, realm 2 seasons, `:117`). If it rises with no rise in executions, revert.
falsifier: (1) hand-built: a seated marcher told of a defended settlement of another faction forms `march` on it, and the
fold reaches `Won` or `Lost` through ENCOUNTER, writing `Person.stance` (`verb_table.yaml:709-710`). Mutation: drop the
stamp term; no march forms. (2) Realm reading, recorded and not required (P1 §0.5): `field.won` + `field.lost` at
`aperture 1 s`, s = 0, 1, 2. If 0, R-07 conjunct 3 stays unmet and the residue is named (which link failed: formed,
offered, attempted or ENCOUNTER). Control: base 0 in both worlds. hash: mover. revert: the column and the term.

**REM-28 · The verbs whose refusals need a reading before a fix: `survey`, `forge`, `convene`, `release`, `dispatch`,
`requisition`, `revoke`.** closes `survey`/`forge` `Record.exists` no-ops (realm 79, spine 7), `convene` (H-163),
`release` 39, `dispatch` 11 (its predicate is "the named person exists", `predicates.py:442-445`), and (rev. 3, I-05) R-04
conjunct (1)'s two refused zero-verbs: `requisition` 4 `requisition.unauthorized` (`SP/aperture_2_0.txt:117`) and
`revoke` 5 (`:120`; `_req_revoke`, `predicates.py:401`, traced by REM-14). `requirements.yaml:811-812` says no current
instrument shows their deciding conjunct; REM-11 and REM-14 make it a repo reading. **R:** R-04 (vis on conjunct (1), ↑
only if a KIND failure is found and classed), R-05. class (c) then (a). Layer: as REM-22 if a column is
added. change: read REM-11 (classes of the refused referents) and REM-14 (the predicate clause) at `aperture 1 s`.
**Decision rule, categorical, no threshold:** a refusal whose deciding read is a KIND failure is a formation defect, by
IN-53's precedent ("refused every time; those formations stop"). (a) If one class covers every referent the row can
succeed on, class it as REM-22 does. (b) If the row's valid referents span several classes (`survey`'s sheet is drawn
for persons, rungs and Propositions; `_mint_sheet`'s docstring, `effects_information.py:578-582`), the single-class
column cannot express it. Record the residue, and do not build a list-valued column without a ruling at step 5 by the
batch critic. A refusal whose deciding read is a learnable STATE (`present_at`, `stores`, a held Tenure) stays: it is the
scarcity channel working. falsifier: per verb, the decision and its reading in the commit body. hash: none unless (a)
applies (then a mover per row). revert: per row.

**REM-29 · `migrate`'s capacity becomes a conjunct the person can learn from.** closes `migrate` 116 `NoOpReceipt`s
(`effects_migration.py:200-206`; realm 25 → 91 across two seasons, so the refusals are repeated, not learned). R: R-05
`migrate` (1/118) may stay at low executions but stops re-forming; R-01/R-02 re-take owed. class (a). [ASSUMPTION;
medium] that the repetition is the missing read and not a stamping defect: **measure first** the share of season-2
`migrate` refusals that repeat a season-1 (actor, destination) pair. If the share is low, stop. **Layer:** the closed
grammar's stems (`data/requires.py::REQUIRES_STEMS`, `:775-778`), described by 04 §F.24a. 04 §C.4 says scarcity is "checked
against the folded world" as the fold's conjunct, and inv. 4 says "every failable clause has a refusal kind". The capacity
test inside the effect body is a hidden conjunct. Precedent for a plan position adding a stem: `with` (T4, ED-IN-0282)
and `audience` (B-Y, IN-59 (b)). Owner of the rule: ONE function `has_room(w, person, dest)` in `queries/world_q.py`,
read by `WorldReader.read` for the new stem and by `_eff_migrate`. The effect's own capacity branch becomes a call to it
and is not kept as a second copy. **The person-side route (rev. 2, C-08), corrected.** The stem is NOT ledger-derived: `LEDGER_DERIVED_STEMS` is
`{"claim.held"}` (`data/requires.py:867`). `room` is a `CELL_STEMS` member (`:805`), as `stores` and `contain.path` are.
The route is the observation channel: the fold's `Verdict.observed` rides the refusal Event; WITNESS deposits it into the
actor's own ledger at the shipped `observation_deposit_mode: actor` (`hole_register.yaml:1627`, the W-B record);
`LedgerReader.read` answers the stem from that claim; §F1 clause 4 (`epistemic.belief_contradicts`) declines the next
formation. The precedent that this route fires is that "every clause-4 drop in the whole corpus … is the verb `move`
refusing on a `contain.path:<person>` belief" (`hole_register.yaml:368` cite, re-read for rev. 3; the post-exclusion
"13, all `move`" measurement is at `:1627`). [UNVERIFIED]: `LedgerReader.read`'s exact
branch for a deposited cell-stem claim. It is settled by the falsifier below, which observes the decline itself.
**Stale-belief consequence, stated (AX-2 permits it):** a deposited `room:<dest>=False` persists after the rung empties,
until a later deposit about the same `(dest, room)` cell or eviction replaces it. A migrant can therefore wrongly avoid a
place with room, which is the "what they hold may be false" AX-2 licenses. No `World` reaches `person_q`. change: `REQUIRES_STEMS` + `room`; `migrate`'s cell (`verb_table.yaml:730`)
gains a named conjunct `room` of `to` with a keyed refusal (`migrate.refused`); the `has_room` owner; the
`_eff_migrate` call. falsifier (`test_migrate_capacity.py`, extended): into a full rung the first `migrate` is refused
with `Event.observed` carrying `room:<dest>=False`; at the next deliberation the same person forms no `migrate` to that
rung. Mutation: drop the deposit; he re-forms. Control: the existing capacity tests still refuse, and a rung with room
still admits. hash: mover. revert: the stem, the conjunct and the owner (the effect branch returns).

**REM-2A · `transfer`: find what moves nothing.** closes `transfer` 1/47 (realm), 0/6 (spine), 46 `stores` refusals and
30 `NoOpReceipt`s (~29 "`perform()` moving nothing"; 1 "names a side that is no rung", `effects_economy.py:210-214`).
class (c), then (a) only if the cause is one owner's defect. Layer: a reading (harness, REM-11's owner); any fix lands at
the cause's one owner. If that is the operand vocabulary, it is `rosters.yaml: requires_operands`, H-94's, behind its
loader. 04 §C.4: "`transfer`'s `stores >= amount`, checked against the folded world" is the scarcity channel working, not
a defect. No seam. [UNVERIFIED]: the cause. Candidate, from the suite (V.2.2):
`record_sourced_operands` gives `transfer` no `kind`/`amount`, so a fixture default meets a store that holds less.
change: measure, in REM-11's reading at `aperture 1 s`, `amount` against `stores` on each refusal, and the operand source
of `kind`/`amount` (`_derive_operand`'s branch, `decision/options.py:817-877`). **No fix is designed here.** If the cause is
the fixture default, the owner is the operand vocabulary (H-94) and it goes to v9's IN-10 lineage as a named residue. If
it is a defect in one function, fix it there. falsifier: the reading names one cause for ≥ 1 refusal per class
(`stores`, no-op). hash: none (measure). revert: n/a.

**REM-2B · Restore IN-09 (`construe`, `evade / defy`) and IN-33 (`exchange`).** closes "six rows the fold cannot carry"
for three of the six; P1 §0.5's "restorable" left with no batch (REM-09). R: **R-05 toward `met`**: three rows leave "no
predicate/effect". class (a). Layer: data and effects (`verb_table.yaml`, `rosters.yaml`, `loop/effects_information.py`);
04 §C.4's one fold; loader inv. 4 (keyed refusals); `exchange`'s operands are reserved to H-94's roster
(`rosters.yaml: requires_operands`), so no operand is coined outside it. No seam. change: `git fetch --unshallow`
(`CLAUDE.md` §2: the checkpoints are unreachable in a shallow clone), then restore `a1c83e62`, `60073e75` (IN-09) and
`ad2f930f..b5c4685d` (IN-33). Re-run their hand-built proofs. **Not required:** a realm execution (P1 §0.5). Required:
the declared trajectory move. IN-33 was reverted because "its refused attempts moved the seed-0 trajectory", and that
move is now a declared mover. falsifier: the checkpoints' own (P5:51, :118). hash: mover. gates: before B-V (IN-33 is
FA-01 content's carrier [ASSUMPTION], P1 §3). revert: `git revert` the restore.

---

### 2.4 RB-3 · SCALE BUILDS — R-04 conjunct (3) and the mass-battle form

**Placement:** by P3 §B.0 R4/R7, as IN-46/IN-47's entries say (P4:35, :42). **RB-3a (REM-30)** opens after B-S merges
(`state/carriers.py` is serial with B-S) and runs beside B-Y. **RB-3b (REM-31)** opens after B-Y merges (it edits
`modules/combat/wrapper.py`, `fight.py` and `seam/wrappers/combat.py`, which B-Y edits). **REM-32** rides B-T's tail after
IN-52 (both edit `modules/mass_battle/`).
**Entry (rev. 4: D-2 RULED yes, Jordan, 2026-10-21):** the builds proceed in file order with no Jordan gate. **[ASSUMPTION;
medium; Jordan to correct]** Both designs stay PROPOSED and held under ED-1094's loud exception (`CLAUDE.md` §2) until
Jordan ratifies them. Each build PR body lists **both** designs as held back, so the merge that lands the code does not
ratify the prose. Each design keeps its `## Status: PROPOSED` line. Jordan can release the holds separately (JQ-5,
optional). Revert: Jordan says a build merge ratifies its design, and the PR bodies drop the held-back line. **Tier:** Opus producer (contract closure
across a seam), Opus critic. **Budget:** IN-46 ⚠ ~150k (combat files); IN-47 ~100k.

**REM-30 · Build IN-47, the character-sheet management space.** closes edit 2 (build), F-A R-04 (one of two rows).
R: **R-04 toward `met`**: the `character creation / development / chronicling` row gains an execution artifact. class
(a). Layer: 04 §A.2 ("a module with no token cannot write"; `decision/` owns nothing), AX-2, AX-4; the design's own
falsifier is that no space writes a `Person` field outside an act's fold. No seam; owners per the design's review at B-H
(`proposals/2026-10-07-character-sheet-spaces.md`, `## Review at B-H`). PR body: the design is listed as held back
(D-2). change: per the design: `decision/` (the
player's development space acts into the chooser slot, `loop/driver.py:355`) and `state/carriers.py`. falsifier (P4:42):
a creation arm switched off reproduces the pre-build hash; a planted space writing a `Person` field directly fails
`test_decision_package_never_names_world_anywhere_under_it` (`test_season_shape.py:2939`). hash: mover where the arm is
on, by outcome. revert: the build's commits.

**REM-31 · Build IN-46, the grid mode's suspension at ENCOUNTER.** closes edit 2 (build), F-A R-04 (the other row),
DEF-2's one handoff on a row's path (SM-6). R: **R-04 toward `met`**. class (a). Layer: 04 §C.1 (the driver is the only
caller of a step; tokens; barrier 3 shared with ENCOUNTER), §C.5 (the seam: a read-only projection, no token, a `Margin`
back), PART D rows 19-24, 35 (no new draw moves unrelated goldens). **Seam crossed: yes**, through the existing combat
composition row and `seam/wrappers/combat.py`. No new import of `modules/` from `engine/`; `PATH_SEAM_ALLOWED` untouched.
Owner = `proposals/2026-10-07-grid-mode-suspension.md` (`## Re-read at B-L`). change: `loop/driver.py`,
`seam/wrappers/combat.py`, `modules/combat/wrapper.py`, `fight.py` per the design. falsifier (P4:37): AUTOMATED and
PLAYABLE-with-scripted-choices-equal-to-the-chooser's end at one `content_hash`; a differing scripted choice moves it; a
suspension that consumes a draw or mints a token twice reds the first.
**Added for rev. 2 (C-09, brief 24):** the human callback runs inside DELIBERATE's per-person map
(`loop/deliberate.py:116`, `w._in_parallel_map = True`), and nothing specifies how it blocks. Under PLAYABLE, a scripted
callback that blocks for the player's person must leave the run order-independent. 04 PART D row 41a's permutation
falsifier is run with the callback on: shuffle the order in which persons are deliberated, and the `Scene` SET and the
season hash are identical. Mutation: a callback that writes shared state reds it. Control: the same permutation with
PLAYABLE off.
Plus `test_importing_every_engine_module_pulls_in_no_subsystem`. PR body: the design is listed as held back (D-2). hash: **declared MOVER (rev. 3, D-02).** P4:34: "the build gives `fight` `march`'s ENCOUNTER/Declared pair …
deferring every fight moves the hash of any seeded season that fights, so the build re-records the seeded goldens and
says so". Every seeded season that fights re-pins, with old → new in the commit body (K1). **Control, kept:** AUTOMATED and
PLAYABLE-with-scripted-choices-equal-to-the-chooser's end at one `content_hash` on the post-build tree. A failure there is
a defect, never a re-pin. revert: the build.

**REM-32 · G3's form: one weight→troop conversion at `massbattle._weighted_unit`.** closes F-A R-07's G3 form, finding
18's "no weight→troop conversion". R: R-04 (mass-battle row) toward a contestable field; R-07 not gated (C9). class (a)
for the form; the value is JQ-4 (b). Layer: `modules/mass_battle/` (a module half; 04 §A.2's adapter row: "nothing,
ever" written); PART D row 38 (a constant comes from a register row, never the keyboard). Seam: the existing mass-battle
composition row. Owner = `_weighted_unit`. change: the conversion as one named fixture, **shipped at the value that
reproduces today's `_SEASON_FORCE_POWER = 4`** (`modules/mass_battle/massbattle.py:196`; `:183` is `command=4`), so the hash is equal and the value is Jordan's to
move (JQ-4). falsifier: NERS G3's: `test_march.py`'s hand-built `Resolution("Won")` (`:254-275`) is replaced by a real
fold reaching `Won` under a fixture value above the shipped one; at the shipped value the season force still routs on
contact (the disclosure at `massbattle.py:198-207`), recorded. **Register row (rev. 3, critique 2 §3; 04 PART D row 38):**
the fixture is injected by name from one new `engine/season/hole_register.yaml` row (kind NUMBER, `owner:` Jordan, the
weight→troop value; `unblocks:` JQ-4), appended in this commit, so loader invariant 11 has a row to read. hash: equal at the shipped value. revert: the fixture.

---
