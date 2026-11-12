# Workplan v12 — part 13, continued: Batch B10-character, positions B10.67 to B10.99, and the boundary row

## Status: PROPOSED (the continuation of `workplan_v12_part13.md`, `V12_STRUCTURE_part2.md` §4.1's `_cont` rule; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

Words, paths and the batch's head contributions are the first file's (`workplan_v12_part13.md`). The position table there lists every position below.

---

### B10.67 — nine comment pointers corrected · `17_CENSUS_C1A_02` C1 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_C1A_02_wires_and_corrections.md` "C1", its Lands line ("Lands in batch: B10 (C1, W3, …)"); F-C1A-02; UNDECIDED 4 of the first file.
- ADVANCES: none of the nine; reading cost (a pointer that names a moved symbol).
- INSTRUCTION: first step: open each site below by its old text (no line numbers: B03a's `CI-02` rewrote comments in every file before this batch, CIP part 2 §5 note 2) and drop from this commit any site whose old text is gone, naming it in the commit body. Then, the source's table, "Old text → new text":

  | site (file) | old | new |
  |---|---|---|
  | `data/rosters.py` | `` `loop/effects.py::_eff_build` `` | `` `loop/effects_founding.py::_eff_build` `` |
  | `data/arrangements.py` | `` `loop/effects.py::_eff_determine` `` | `` `loop/effects_information.py::_eff_determine` `` |
  | `queries/world_q.py` | `` `loop/effects.py::_eff_migrate` `` | `` `loop/effects_migration.py::_eff_migrate` `` |
  | `data/fixtures.py` | `` `loop/effects.py::_eff_oblige` and `_eff_transfer` `` | `` `loop/effects_governance.py::_eff_oblige` and `loop/effects_economy.py::_eff_transfer` `` |
  | `queries/faction_q.py` | `` `loop/effects.py::_eff_survey` `` | `` `loop/effects_information.py::_eff_survey` `` |
  | `epistemic.py` | `` `shape.py::SeasonDriver::_fold::ev` `` | `` `loop/resolve.py::_fold`, its `ev` `` |
  | `epistemic.py` | `` emitted in `shape.py::SeasonDriver::matter` `` | `` emitted in `loop/matter.py` `` (the source's `(:127)` dropped: a line number) |
  | `epistemic.py` | `` (`tests/test_obligees.py`, through the real fold and WITNESS) `` | `` (the test that showed it, `tests/test_obligees.py`, was dropped at `FORK:217340fc`, ED-IN-0314) `` |
  | `epistemic.py` | `` `test_obligees.py::test_17a_the_channel_reads_the_obligee_set_through_establishment_of` `` | the same name followed by `` (dropped with its file, `FORK:217340fc`) `` |

  "And one that follows deletion batch D1: `seam/__init__.py:26`, 'with the `PATH_SEAM_ALLOWED` member and `files.COMBAT_SEAM_PY` renamed in the same commit' → 'with the `PATH_SEAM_ALLOWED` member renamed in the same commit'" — only if B03's D1 deleted `files.COMBAT_SEAM_PY` (on the tree read `data/files.py` still defines it; if it is still there at this item's open, this row is dropped and named).
- WHERE: `engine/season/data/rosters.py`, `data/arrangements.py`, `queries/world_q.py`, `data/fixtures.py`, `queries/faction_q.py`, `epistemic.py`, `seam/__init__.py` (comments only).
- TESTS: none (comments).
- FALSIFIER and CONTROL: a corrected pointer names a symbol `git grep` does not find. Control: the AST of every edited file equal before and after (comments only; `CI-02`'s check, B03a).
- GATE: "re-run the resolver scan; the nine sites resolve": for each new pointer, `git grep -n "def <symbol>" engine/season/<file>` → one line; `git grep -n "loop/effects.py::\|shape.py::SeasonDriver" engine/season -- '*.py'` → none of the nine old texts (other hits are not this item's: `harness/headless.py`, `harness/arms.py`, `state/carriers.py` carry the same stale form and are listed in the commit body for B03a's owner, not edited here); the realm hash at seed 0, one season → equal to `B10.66`'s.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B03a (`CI-02`); EXISTS-IN-TREE `loop/effects_founding.py::_eff_build`, `loop/effects_information.py::_eff_determine`, `::_eff_survey`, `loop/effects_migration.py::_eff_migrate`, `loop/effects_governance.py::_eff_oblige`, `loop/effects_economy.py::_eff_transfer`, `loop/resolve.py::_fold`, `loop/matter.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high` (the source: "sonnet / high (C1, W3, the gates)").
- LANDS IT: B10's producer; `Item: B10.67`, `[skip ci]`.

### B10.68 — the cast loader refuses a faction cell it cannot have read whole; `defects` deleted · `17_CENSUS_C1A_02` W3 with `17_CENSUS_C1A_01` D1's `defects` row · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_C1A_02_wires_and_corrections.md` "W3", "Dependency edges" ("`W3` lands in B10 with deletion batch D1's `defects` row (moved from B03 for that reason)"); `proposals/17_CENSUS_C1A_01_deletion_batches.md` D1 row `engine/season/data/cast.py` `def defects` ("its paren check moves into the loader (proposal 02, W3), landed in the same commit"); the source's audit `audits/17_CENSUS_C1A.md` (its head: F-C1A-02 to F-C1A-07).
- ADVANCES: none of the nine; a corrupted registry cell is refused at load (CLAUDE.md §0.05, "the loader's refusal per data family").
- INSTRUCTION: "**Edit** (`engine/season/data/cast.py::_rows`, after `_CACHE` is built; `defects` is deleted by D1 in the same commit):
  ```python
  for cid, r in _CACHE.items():
      raw = str(r.get("faction") or "")
      if raw.count("(") != raw.count(")"):
          raise Unspecified(
              f"{cid}: faction cell {raw!r} has an unbalanced parenthesis", "references/npc_registry.yaml",
              needs="the cell quoted, so an unquoted `#` is not read as a comment",
              law="ID-5 -- refuse, don't default: a truncated cell resolves to a faction with its seat lost")
  ```"
  Then delete `data/cast.py::defects` (`grep -rn "cast\.defects" engine modules systems tools tests --include=*.py` first: D1's own grep; no caller on the tree read). If B03's D1 item already deleted `defects`, this item lands the loader check alone and says so.
- WHERE: `engine/season/data/cast.py` (`_rows`; `defects` deleted); NEW `engine/season/tests/test_cast_faction_cell.py` `[ASSUMPTION: test file name; the item creates it — E-3]`.
- TESTS (new file, written before the edit and read red): `test_an_unbalanced_faction_cell_is_refused` (the source's falsifier: "A fixture registry with `faction: Crown (Seat` loads without raising"), planted through a temporary registry path; `test_the_shipped_registry_loads` `[ASSUMPTION: names — E-3]`.
- FALSIFIER and CONTROL: "A fixture registry with `faction: Crown (Seat` loads without raising." Control: the shipped registry loads (it "has no such cell: `defects()` returned none of that class").
- GATE: `python -c "from engine.season.data import cast; print(len(cast.load()))"` → prints the row count (46 on the tree read); `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_cast_faction_cell.py -q` → pass; the realm hash at seed 0, one season → equal to `B10.67`'s.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `data/cast.py::_rows`, `::defects`, `gaps.Unspecified`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B10's producer; `Item: B10.68`, `[skip ci]`.

### B10.69 — the beneficiary arm's closing gate · `17_CENSUS_C1A_02` W4 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_C1A_02_wires_and_corrections.md` "W4" ("Carried by `02_CHAR_scar_cap_and_regard_unit.md`'s Addendum (C-U5a-16, C3-K3): no separate edit … the gate below is the census row's closing gate, run in B10 after the Addendum lands"); C3-N7 (67 rows).
- ADVANCES: R-06 (an NPC who helps those he regards is a distinguishable person; the arm is reachable, unswitched).
- INSTRUCTION: no code edit (the arm, the roster member `beneficiary` in `rosters.yaml: stance_polarities` and `Fixtures.stance_polarity` staying `"declared"` are the first half's Addendum item). This item lands the census row's closing test if the Addendum item did not: "(b) At `stance_polarity="beneficiary"`, for one person holding regard for A and none for B, a candidate of a row with `beneficiary: to`, bound to A, scores above the same candidate bound to B (a test in `tests/test_governance_build.py`, beside `test_lb6d_the_column_resolves_on_candidates_the_engine_actually_forms`)". First step: `grep -n "beneficiary" engine/season/tests/test_governance_build.py`; if a test of (b)'s shape is already there, this item is its reading only and commits nothing (its reading goes in `B10.70`'s commit body).
  (Patched: P-15, resolved at the merge.) The first half's Addendum item (B10.11) writes `test_regard_unit.py`'s two tests and no beneficiary test, so this item is the one owner of W4's (b) test and writes it; there is no duplicate to drop.
- WHERE: `engine/season/tests/test_governance_build.py` (one test: `test_the_beneficiary_arm_scores_a_regarded_beneficiary_higher` `[ASSUMPTION: test name; the item creates it — E-3]`).
- TESTS: the one above, green on the Addendum's tree at the planted arm; read red with the arm's branch reverted.
- FALSIFIER and CONTROL: "(a) the hash moves at the control; (b) the two candidates score equal, so the arm reads nothing." Control: "(a) At the shipped arm, a seeded one-season `content_hash` at seeds 0-2 equals the hash before the commit."
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_governance_build.py -q -k beneficiary` → pass; the realm hash at seeds 0 to 2, one season → equal to `B10.68`'s.
- HASH MOVERS: none ("the flip is design-first"; DIALS line of the first file).
- DEPENDS ON: V12 the first half's `02_CHAR_scar_cap_and_regard_unit` Addendum item (`_stance_arm`'s `beneficiary` branch, `regard_sign`, `stance_scale`); EXISTS-IN-TREE `decision/choose.py::beneficiary_of`, `::_stance_arm`, `engine/season/tests/test_governance_build.py`.
- GLOSSARY: none.
- COST and TIER: edit (one test); `sonnet`, `high`. "W4's flip, when a sweep is read, is opus (a balance judgment)" — not here.
- LANDS IT: B10's producer; `Item: B10.69`, `[skip ci]`.

### B10.70 — inside tier 1, an unmet need is attended first · `01_CORE_unmet_need_is_attended_first` · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/01_CORE_unmet_need_is_attended_first.md` "The resolution", "Edit", "Gate" 1–4, "Falsifier"; F-CORE-20. U3 §1.2 orders it after `02_CHAR_goal_lean_on_its_own_question` (its row: "needs `02_CHAR_goal…` ✓"); the source's "with and before" is its gate 2, which reads both.
- ADVANCES: R-07 (a recorded shortfall reaches the person who can answer it); the famine's upward half.
- INSTRUCTION (copied): "In `key()`, the tier-1 return `(1, 0.0) + tie` becomes `(1, -need) + tie`, where `need` is the held claim's value when its predicate's stem is `data/requires.py::SHORTFALL_PREDICATE` (the one name of an unmet-need claim; MATTER writes it, `decision/options.py::_from_shortfall_claim` reads it) and `0.0` otherwise. The stem is read from its owner; no predicate is spelt at the site. The docstring's LIMIT sentence is replaced by the rule. `[ASSUMPTION; medium; Jordan to correct; revert: (1, 0.0)]`." The tier-1 return on the tree read is `if any(r in mine for r in q.referents): return (1, 0.0) + tie` in `queries/world_q.py::attention_key`'s `key`; the held claim is `held_by_id.get(q.about)` (already read above it). The LIMIT sentence is "magnitudes inside tier 1 are not ranked (LIMIT)".
- WHERE: `engine/season/queries/world_q.py` (`attention_key`, its `key` and docstring); NEW `engine/season/tests/test_attention_key.py`.
- TESTS (new file, written before the edit and read red): "`test_a_shortfall_claim_sorts_first_larger_first_in_tier_one` (a hand-built holder with two shortfall claims of 8 and 15 and a routine `stores.changed` claim, all tier 1: the 15 first, then the 8, then the routine one) and `test_tier_two_order_is_unchanged`."
- FALSIFIER and CONTROL: "The unassisted steward still never receives the shortfall question at any of three seeds (the edit does nothing), or relief appears in the control world whose steward holds nothing (the edit is not what carries it)."
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_attention_key.py engine/season/tests/test_in57_attention_tiers.py -q` → pass; gate 1 at two seasons (four in the source's run; A-114): `for s in 0 1 2: PYTHONHASHSEED=0 python -c "from engine.season.harness import scarce; r = scarce.run(2, seed=$s, name_the_question=False); print([x['asked'] for x in r['seasons']])"` → the steward's deliberations include the shortfall question in the season after it is recorded at each seed; gate 2 ("with both, a claim-sourced `transfer.made` to the hungry town at two or more of the three seeds, and none with the steward's `hold` removed (`scarce.build(steward_holds=False)`, the harness's own control)"): the same command with `w=scarce.build($s, steward_holds=False)` as the control arm, both readings quoted; the realm hash at seed 0, one season → moved.
- HASH MOVERS: "Every world in which a tier-1 holder holds a shortfall claim (declared; re-pinned once with B10)". Gate 3's re-record ("`corpus_run` seed 0 and a two-season `build_realm(0)` hash are re-recorded in `engine/season/tests/_realm_goldens.py`") is `B10.99`'s re-pin.
- DEPENDS ON: V12 the first half's `02_CHAR_goal_lean_on_its_own_question` item (gate 2); EXISTS-IN-TREE `queries/world_q.py::attention_key`, `data/requires.py::SHORTFALL_PREDICATE`, `decision/options.py::_from_shortfall_claim`, `harness/scarce.py::run`, `::build`; V12 Batch B02 (`_realm_goldens.py`).
- GLOSSARY: none.
- COST and TIER: edit (one line and a docstring), hash mover; `sonnet`, `high`.
- LANDS IT: B10's producer; `Item: B10.70`, `[skip ci]`.

### B10.71 — a goal's last stage opens a mandatory question; a want he believes met raises no `need` question · `12_ARCS_arcs_as_staged_goals` with `U5a_CHAR_owed_amendments` §3 (a) · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/12_ARCS_arcs_as_staged_goals.md` "Resolution (decided)" 2–5, "Edits, by owner", "Gate", "Named tests"; its head lines (A-47, A-16, A-24; R-B: item 5's `org.person` is NOT accepted); `proposals/U5a_CHAR_owed_amendments.md` §3 (a); rulings A-47, A-48; U3 §1 item 11 ("with `U5a_CHAR_owed_amendments` §3"); UNDECIDED 3 of the first file.
- ADVANCES: R-07 (a resolve armed by what a person learns); R-06 (a want can be kept).
- INSTRUCTION (copied):
  1. `engine/season/data/goals.py`: "refuse an `opens:` value outside the two; nothing else (item 5's `org.person` is NOT accepted …)." The key is "`opens: mandatory | ordinary` (default `ordinary`; head line, A-47: the last stage's question is mandatory, it opens a scene and decides nothing)", on the `goal_stages` row (`GoalStages` gains `opens: str = "ordinary"`). "A stage never names a verb, an act, a subject or an outcome. It names a predicate over the holder's ledger and a lean": the loader refuses a stage key outside `{id, term, predicate, pursuits}` (`test_a_stage_naming_a_verb_or_outcome_is_refused_at_load`).
  2. "The one formation site that reads `opens:` is `world_q.questions_for`'s ordering (`Question.mandatory`), also read by `30_WR_A` commit 3." `state/carriers.py::Question` gains `mandatory: bool = False` (a Question "is not in `World._STATE_COLLECTIONS` and is never hashed", its docstring, so no encoding mover); `questions_for` sets it on the `need` question of an ambition whose goal's row has `opens: mandatory` and whose `current_stage` is that row's last stage, and orders mandatory questions first, ahead of `attention_key` `[ASSUMPTION: the ordering site — basis: the source's "read at the one formation site", A-47 "it cannot be passed over for another"; revert: no `mandatory` field]`. It decides nothing: which act he takes is still the chooser's draw.
  3. §3 (a), owner `engine/season/queries/world_q.py::questions_for` (Q4): "the standing `need` question for a commitment is not raised while the holder's **own ledger** reads the committed Proposition's content as true. Scope: Propositions whose content is a typed predicate the ledger reader can evaluate (the rung goals AM-B-09 narrowed aim states to; a stage predicate of `goal_stages` once authored). A want with no evaluable content is unchanged. A want he believes met and that is not met is then a false belief at work, which is intended." The tree already skips the question where `aim_state(w, p, …) == "met"` (CP-T02-03); the ledger reading is added beside it (a need is not raised when either reads met) `[ASSUMPTION: both kept — basis: the reading that changes less; CP-T02-03's comment "a MET aim … has no work to ask for"]`.
  `goals.yaml`'s `goal_stages:` rows: none shipped here but ARC-47's (`B10.73`); the cast's others are per-case content (DIALS line).
- WHERE: `engine/season/data/goals.py` (`GoalStages.opens`, the refusals); `engine/season/state/carriers.py` (`Question.mandatory`); `engine/season/queries/world_q.py` (`questions_for`: the mandatory mark, its order, the ledger reading of Q4); NEW `engine/season/tests/test_staged_goals.py`; NEW `engine/season/tests/test_wants_end.py`; `unified/U1_GLOSSARY.md` (a row *mandatory question*).
- TESTS: in `test_staged_goals.py` (written before step 1 and read red): `test_no_stage_rows_is_hash_equal`; `test_the_last_stage_opens_a_mandatory_question_and_decides_nothing` (a planted two-stage row with `opens: mandatory`, its last stage armed by a planted held claim: the need question is first and `mandatory`; the act taken varies over seeds); `test_a_stage_naming_a_verb_or_outcome_is_refused_at_load`. `test_arc47_on_arm_off_arm_and_lie_arm` is B39's (UNDECIDED 9). In `test_wants_end.py`: `test_a_met_rung_goal_raises_no_need_question` (green before the edit through CP-T02-03; kept as the control) and `test_a_believed_met_want_raises_no_need_question` `[ASSUMPTION: name — E-3]` (a holder whose ledger reads the content true while `aim_state` reads open: no `need` question), red before step 3.
- FALSIFIER and CONTROL: "Run the on-arm with the stage rows deleted: if the beat still occurs at the same rate, the stages decide nothing" (read at B39 with ARC-47's case). §3: "With (a) alone: `need` questions for met rung goals fall to 0 and the hash of a world with no met goal is EQUAL." Control: no stage row, no believed-met want: the realm hash equal.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_staged_goals.py engine/season/tests/test_wants_end.py -q` → pass; the realm hash at seed 0, one season → moved only where a holder believes a want met (declared), recorded.
- HASH MOVERS: "(a) where a goal is met" (§3) — every world where a holder's ledger reads his want true and `aim_state` does not; none from `opens:` with no stage row. Declared; B10's re-pin.
- DEPENDS ON: EXISTS-IN-TREE `data/goals.py::GoalStages`, `::_goal_stages`, `queries/world_q.py::questions_for`, `::current_stage`, `::aim_state`, `::ambitions`, `rosters.yaml: goal_stage_terms`, `state/carriers.py::Question`; V12 the first half's `02_CHAR_goal_lean_on_its_own_question` item (the reader of the active stage's `pursuits`).
- GLOSSARY: new row *mandatory question*: "a question a person may not pass over for another (A-47); it opens a scene and decides nothing"; owner `Question.mandatory`.
- COST and TIER: edit plus a small build; `sonnet`, `high` (the source: "a WR/IN `valoria-author` session on `sonnet` (`high`)").
- LANDS IT: B10's producer; `Item: B10.71`, `[skip ci]`.

### B10.72 — a want can be laid down, and whether it was kept is read · `U5a_CHAR_owed_amendments` §3 (b) · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/U5a_CHAR_owed_amendments.md` §3 (b), "Gate", "Falsifier", "Falsifier, added"; D-48 precedent; `audits/25_GROUNDING_ENGINE.md` G-19 (`release` admits one's own commit); F-PES-CHAR-07.
- ADVANCES: R-06 (a character's wants end: "243 and 226 commitments live after three seasons at seeds 0 and 1, 0 ever ended").
- INSTRUCTION (copied): "(b) Owner `engine/season/verb_table.yaml` (`release`), `decision/options.py`, `queries/world_q.py`: `release` on his own `commit` forms as an ordinary Candidate (it admits one's own commit today: G-19, verified at `data/rosters.py:526`) and keeps its **one** emission, `commitment.ended`. Whether the released want was **kept** is a reading computed where read (the D-48 precedent, ladder step 4): `world_q.commitment_kept(w, tenure) -> bool`, true when the closed `commit` Tenure's Proposition content was held true in the releaser's own ledger at the closing Event's tick. A row-keyed emission whose key is a condition on the actor's ledger is neither a Degree nor a refusal clause, and the loader refuses it (`04` §C.4, §B.13 invariant 12), so it is not built. The person closes his own edge (T-m); nothing closes it for him." First step (SITE): read whether an own `commit` forms as a `release` Candidate on this tree (`opening_set` over a hand-built holder of one `commit`) and record it in the commit body; if it forms, the edit is `commitment_kept` alone; if not, the `decision/options.py` referent source for one's own `commit` is the edit, as the `release` row's `requires:` already admits it.
- WHERE: `engine/season/queries/world_q.py` (`commitment_kept`); `engine/season/decision/options.py` (only if the SITE step finds `release` unformed); `engine/season/tests/test_wants_end.py`.
- TESTS (in `test_wants_end.py`, written before the edit and read red): `test_commitment_kept_reads_the_releasers_own_ledger`; `test_release_has_one_emission`.
- FALSIFIER and CONTROL: "0 commitments end at three seeds (the candidate never ranks: the lean is F-CHAR-01's and the goal-lean proposal lands first)"; "a `commit` whose releaser's ledger did not hold the content true is read kept." Control: `release`'s emission set unchanged (one kind).
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_wants_end.py -q` → pass; "Realm, seeds 0–2, three seasons" read at two (A-114): `commitment.ended` Events above zero, `commitment_kept` true for at least one and false for at least one, and the count of live commitments no longer monotone — read at `B10.99` on the closing tree, seeds 0 to 2, two seasons, each count quoted with `checked >= 3`; a zero at two seasons is reported as a zero, not a pass.
- HASH MOVERS: "(b) wherever the candidate forms". Declared; B10's re-pin.
- DEPENDS ON: V12 `B10.71`; EXISTS-IN-TREE `loop/effects_governance.py` (`release`'s effect, `commitment.ended`), `loop/predicates.py` (`release`), `data/rosters.py` (G-19's line).
- GLOSSARY: none ("kept" in its ordinary sense).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B10's producer; `Item: B10.72`, `[skip ci]`.

### B10.73 — ARC-47's stage row drafted · `12_ARCS_arcs_as_staged_goals` resolution 1 · CONTENT · HASH MOVER(behaviour)
- SOURCE: `proposals/12_ARCS_arcs_as_staged_goals.md` "Resolution (decided)" 1, "Edits, by owner" (`goals.yaml`); D-19 (authored values drafted early, landed at their batch, ratified at its merge, ED-1094); INCOMPLETE (CONTENT: "stage rows are per-case content", `unified/U4_DOCUMENT_STATUS.md` §3.4).
- ADVANCES: R-07 (ARC-47's beat chosen when enough is heard); its gate is B39's (UNDECIDED 9).
- INSTRUCTION: draft (at the batch's open; no engine time) and land here, after `B10.71`'s loader accepts `opens:`, one `goal_stages:` row in `engine/season/goals.yaml` for the source's example: "ARC-47 and NSC-08 (Ehrenwall): the Löwenritter's existing goal `goal_lowenritter_throne_security` gets a stage row whose first stage is the default lean and whose later stages require, each, a claim in her own ledger of a kind the case names (a seizure she has heard of, the heir's turning, territory lost). Each stage shifts the goal's `pursuits` lean. The demand she issues is an ordinary seat act that the later lean makes rank; nothing fires." The row carries a `source:` quoting the case need it stands for, `term:` values from `rosters.yaml: goal_stage_terms` (never decreasing), each stage `predicate` a typed cell the loader builds person-side, and `opens: mandatory` on the row (A-47: its last stage's question). Every value is `[ASSUMPTION; status: seed]` and listed in the batch PR body for Jordan's correction (D-19). No stage names a verb, an act, a subject or an outcome.
- WHERE: `engine/season/goals.yaml` (`goal_stages:`, one row).
- TESTS: `test_staged_goals.py`'s three stay green with the row shipped (the loader accepts it).
- FALSIFIER and CONTROL: the loader refuses the row (a predicate asking a WORLD-ONLY stem, a term off the roster). Control: the row removed, the realm hash returns to `B10.72`'s.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_staged_goals.py -q` → pass (the shipped file loads with the row); the realm hash at seed 0, one season → moved where Ehrenwall's lean changes (declared), recorded.
- HASH MOVERS: Ehrenwall's choices wherever a stage arms; declared; B10's re-pin.
- DEPENDS ON: V12 `B10.71`; EXISTS-IN-TREE `goals.yaml` `goal_lowenritter_throne_security`, `data/goals.py::_goal_stages`.
- GLOSSARY: none.
- COST and TIER: content; drafting `opus`, landing `sonnet` (D-19's pattern in §2.2's BA1 row).
- LANDS IT: B10's producer; `Item: B10.73`, `[skip ci]`; the PR body lists the row's values for Jordan.

### B10.74 — arm D2 of the own-act screen, read at three seeds · A1-05, V9-11 · READING
(No body: a reading quoted at the close, `V12_STRUCTURE_part2.md` §5.3. Its text is Reading 1 of the `## Readings` block below. Its dependency, re-checked at this tree as §5.6 asks: arm D2 is built — `queries/world_q.py::attention_key`, the comment "CR-10, arm D2 (A1-05): the own-act screen demotes a tier-0 echo and tiers 2 and 4 as ever, and SPARES a tier-1 one", and `engine/season/tests/test_in57_attention_tiers.py::test_a_tier_1_own_act_claim_is_spared_the_screen_and_tier_0_and_2_are_not`. What remains of the entry is its three-seed reading, which "Reopen[s] if a three-seed reading reverses D2's R3 figures".)

### B10.75 — intent reconciliation · H-191 · BLOCKED (CHAR: a shipped `intent_disclosure` above 0 and a reader pairing an intent claim with the act; no proposal builds either)
- What the pointed row is: `engine/season/hole_register.yaml` H-191; owner "decision/options.py -- `record`'s pairing step, at the field-less `ABSENT: H-191 intent reconciliation` marker; `H-183`'s `unblocks:` names it" (E7 §Carry-forward line 227).
- Missing (E7, copied): "a shipped `intent_disclosure` above 0 (ships 0, `data/fixtures.py`) and a reader pairing an intent claim with the act. No proposal builds either. Owner: CHAR (B10), with `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds.md` as the nearest neighbour."
- Gate when unblocked: the register row's own; nothing is built here. The row stays `absent`; `V12_STRUCTURE_part3.md` §8.2 lists it among the nine blocked entries.

### B10.76 — the deed lie · H-198, M9 · BLOCKED (FI, B11: a deposit that can hold a deed claim False; CHAR: the reader that pairs it)
- What the pointed row is: H-198, owner "`queries/person_q.py::said_of`, at the field-less `ABSENT: H-198 deception` marker" (E7 §Carry-forward line 231); merged with M9 and E4's §2 deed-lie row (the intake §1: "IN (CHAR), held, MISSING-DEP").
- Missing (E7, copied): "a deposit that can hold a deed claim False and a reader that pairs it (the row's trigger). `08_FI_06_testimony-names-a-hand.md:87` names it and does not build it. Owner: FI (B11) for the deposit, CHAR (B10) for the pairing."
- Gate when unblocked: the row's trigger fires (a False deed claim deposited); the pairing is then an item of the batch that fired it, or `STOPPED` if B10 has closed (`V12_STRUCTURE_part3.md` §7.9). Listed in §8.2's blocked entries.

### B10.77 — pursuit weights that do not sum to one: kept, and named as decisiveness · ER-JF10 · POINTER
- What the pointed item does: the first half's `02_CHAR_resolve_and_temper` resolution 1 item keeps the spread of `projected_axes` lengths and names it (`person_q.decisiveness(p)`, "the length of `projected_axes(p)`"; "The sixfold spread is KEPT and NAMED, not normalised away"). ER-JF10 ("pursuit weights not normalised (Saemund 1.31)", E3 Block 12) is answered there (UNDECIDED 6 of the first file).
- Files and symbols: `queries/person_q.py::decisiveness`, `data/cast.py::pursuits_of` (unchanged).
- Gate: at `B10.99`, one line in the close's commit body: the 46 cast rows' weight sums (`python -c "from engine.season.data import cast; print(sorted(round(sum(cast.pursuits_of(r).values()), 2) for r in cast.load().values()))"`) beside `decisiveness` for the same persons, so the two readings are on one tree.

### B10.78 — H-185 and H-191 left to their owners · DEF-12 · POINTER
- What the pointed rows do: DEF-12 ("H-185 (authored OUGHT's `predicate` does nothing) and H-191 (intent reconciliation read by nothing)", E4 line 4366: "deferred to owners; not M1") is two hole-register rows. H-185 is settled DONE-IN-CODE (`master/GAP_REGISTER_EVALUATION_part2.md` row E7:83: "`Proposition.predicate` kept as a declared non-causal label … nothing is owed"); H-191 is `B10.75`, BLOCKED.
- Files: none. Gate: none of its own (each row's).

### B10.79 — `requisition` in computed play · the B10-16 gates, IN-52 and `requisition` entry (AM-E-21) · POINTER (B12c.30 to B12c.34; was BLOCKED (SE: H-163 limit 3(a), unowned) until A-116, 2026-11-12)
- Reconciled 2026-11-12 (A-115/A-116 lane): Jordan answered the lift (A-116, J-02: a report up the chain typically; reach down the residence ladder selectable per seat). Its build is B12c.30 (the `larder_reach` key), B12c.32 (the believed stock), B12c.33 (`residence`) and B12c.34 (the flip; gate: an issuing seat is offered a larder in `build_realm(0)` at seed 0, two seasons, and `requisition.taken` quoted at seeds 0–2). Nothing lands in B10. The text below is the entry as it stood.
- What the pointed entry is (E5 Block C12, copied): "no position makes `requisition` execute in computed play; the owner is none. The seat channel carries only MATTER-recorded reads, and the realm records no shortfall after season 1 … no channel gave any issue-granting holder a settlement-larder claim (H-163 limit 3(a): `larders_in_purview` returned `()` in 766 of 766 calls). Until a position takes H-163 limit 3(a) (**[GAP: unowned]**), CP-T08-06's compliance reader, CP-T08-07's collection, CP-T08-08's refill and IN-52's flip are credited on hand-built worlds only … which lift to build (a seat-channel level report, or residence-ladder reach) is a design choice with different information games … asked as M17."
- Where its work lands when unblocked: the SE lane's batch that carries IN-52 (B12a to B12c, the intake's SE heading); nothing in B10. `V12_STRUCTURE_part3.md` §8.2 lists it ("the B10-16 gates entry (SE)").

### B10.80 — CR-93's build · HELD (trigger: `B10.51` merged)
- When `B10.51`'s design merges (ED-1094), its build items are written from it into the next batch that edits `decision/` (v11: "its builds slot by R8 into the next batch sharing `decision/`"), each a declared mover of every seeded choice. No work here; at B10's expunge this row leaves for the held list (D-18).

### B10.81 — CR-95's build · HELD (trigger: `B10.52` merged)
- When `B10.52`'s design merges, its combat half and its social half are written into the next batch that edits their files (the social half after SC-02's re-source, B24); "(1)'s data edit a MOVER wherever a resisting person has authored Spirit; each build declared". Leaves for the held list at the expunge.

### B10.82 — the risk and horizon terms and the M36 columns · HELD (trigger: `B10.53` merged)
- CL-PERSON's build less the stored offsets (`B10.58`): the intake's settled line, "the build stays held on M35-M37, M40 as v11 states". When `B10.53` merges, its terms are written into "the next batch sharing `decision/`" (E5 Block D4), "EQUAL at neutral values; a declared mover once a value is authored". Leaves for the held list at the expunge.

### B10.83 — the cast's pools differ or not: B10's reading · `IS-B2-CHAR-06` reading (2) · READING
(No body. Its text is Reading 2 of the `## Readings` block. `IS-B2-CHAR-06` names B10's close among its three: "three readings, quoted at the close of B05, B10 and `BA1-cast-content`, each against the one before".)

## Readings

Each reading is taken once, at `B10.99`, on the closing tree, `PYTHONHASHSEED=0`, and quoted in the close's commit body with its tree (`reading @<sha>`).

**Reading 1 (`B10.74`; A1-05, V9-11).** Source text, copied byte for byte from `master/eval/E3.md` Block 5: "The screen exists by the user's ruling ED-IN-0294 (`editorial_ledger_in.jsonl:69`, opened), whose stated problem is a claim about the person's AMBITION subject that his own act occasioned, ranking in TIER 0. Arm D2 (tier-1 echoes spared, tier-0 still demoted) is that scope exactly; D1 restores the no-screen failure the ruling exists to stop (80.4 % own-act echoes, per the J.2 row). Measured on one seed only. `[ASSUMPTION; medium; Jordan to correct]` (a reading of a ruling's scope)"; revert: "screen every tier (as built at IN-57). Reopen if a three-seed reading reverses D2's R3 figures." The entry's gate: "a 3-seed reading (R3 figures) with tier-1 echoes spared". Command: `for s in 0 1 2: PYTHONHASHSEED=0 python -m engine.season.harness.corpus_run $s` → the NPC lane's `check R3: n of N pass` line at each seed; then the same three runs in a scratch arm (not committed) with the screen applied to every tier (the revert the source names) → its three `check R3` lines. Expected: D2's figure at or above the every-tier arm's at two or more of the three seeds; a reversal at two or more is reported as the reopen the source names, not fixed here.

**Reading 2 (`B10.83`; `IS-B2-CHAR-06` (2)).** Source text, copied from `master/instructions/IS_B2_SC_FI_CORE_CHAR_part2.md` `IS-B2-CHAR-06`: "(1) `aperture 4 0` POOLS ROLLED, the line *"two actors at different pools"* per rolled verb (`U5a_capability_home_and_two_inputs.md` Part B gate 4); (2) `python -m engine.season.harness.decision_spread --persons` (distinct pools across the cast); (3) `IS-B2-CORE-04` row 11's share of non-top choices. Expected: (1) stays "no" in the shipped realm at B05 and B10 (the mechanism is in, the content is not) and reads "yes" at the content batch; the batch that expects otherwise says why." Taken here: (2) and (3) on the closing tree against B05's close (`reading @<sha>`, never re-taken), and (1) at two seasons (`aperture 2 0`; four in the source, A-114). "A reading taken on a tree whose `aperture` `CONTROL` line reads unequal is void."

### B10.99 — re-pin and close readings · E-1; `IS-A-12` · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; `IS-A-12` (the `reading:` records); `01_CORE_unmet_need_is_attended_first.md` gate 3; D-04.
- ADVANCES: the conjuncts the batch head's REQUIREMENT line names (`V12_STRUCTURE.md` §2.2's B10 row: R-07.d; re-read R-06.c–d, R-07.b, R-08.c), read and recorded; `status:` not edited (A-114).
- INSTRUCTION, in order:
  1. Re-record, once, every pin any item of the batch moved (both halves): the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one pin file) at seeds 0 to 2, and the `corpus_run` seed-0 and two-season `build_realm(0)` hashes (`01_CORE_unmet_need` gate 3: "said plainly as re-records; the values are read on the batch's base, not typed here"), read against the first half's open reading (`reading @<batch-start-sha>`). The commit says: "re-pin: encoding (`Person.manner_offset`, B10.58) and behaviour (the first half's movers; B10.59, B10.60, B10.65, B10.66, B10.70, B10.71, B10.72, B10.73)".
  2. Take Readings 1 and 2, `B10.54`'s gate (d), `B10.72`'s two-season counts and `B10.77`'s sums line, each quoted in the commit body.
  3. Write the named conjuncts' `reading:` records in `engine/season/requirements.yaml` (`IS-A-12`: the readings, not the status).
- WHERE: `engine/season/tests/_realm_goldens.py`; `engine/season/requirements.yaml` (`reading:` records only); any other pin file a covering test names (the first half's items name theirs).
- TESTS: every test file either half added or edited stays green; no test changes but the pins.
- FALSIFIER and CONTROL: a pin moves that no item declared (stop: an undeclared mover is a defect of the item that moved it, found by bisecting the batch's commits on the seed-0 hash); the tallies an encoding-only item declared equal (`B10.58`) differ.
- GATE: the BATCH GATE of the head, with this half's additions: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_voices.py engine/season/tests/test_choice_alignment.py engine/season/tests/test_contest_decider.py engine/season/tests/test_manner_offsets.py engine/season/tests/test_offer.py engine/season/tests/test_relations.py engine/season/tests/test_rival_teller.py engine/season/tests/test_self_knowledge.py engine/season/tests/test_cast_faction_cell.py engine/season/tests/test_governance_build.py engine/season/tests/test_attention_key.py engine/season/tests/test_in57_attention_tiers.py engine/season/tests/test_staged_goals.py engine/season/tests/test_wants_end.py -q` → pass; `python tools/export_npc_roster.py --check` → exit 0; `python tools/ci_sim_fabrication_check.py` → exit 0; `python -m engine.season.harness.register --check` → exit 0; `python -m engine.season.harness.register --requirements` → nine lines, quoted; `python tools/m1_acceptance.py --summary` → its verdict line, quoted; the realm hashes at seeds 0 to 2 (two seasons at most) → the re-pinned values; the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch touches engine core and registries: the full gates, the one full-suite run, CLAUDE.md §0.4); the glossary rows this half edits (*voice*, *room*, *manner*, *relation ground*, *self-knowledge*, *mandatory question*) read against the code they point at (`STAGES.md`, "The glossary always matches" rule 2): a mismatch fails the close; the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; `status:` is not edited (`IS-A-12`).
- HASH MOVERS: the re-pin itself (every movement declared above).
- DEPENDS ON: every position of the batch; V12 Batch B02 (`_realm_goldens.py`, `IS-A-12`'s record form).
- GLOSSARY: none (each row was edited in its item's commit).
- COST and TIER: reading and a re-pin; `sonnet`, `high`; the readings against their expected values read by `opus` at the close's terminal critique.
- LANDS IT: B10's producer; `Item: B10.99`; **not** `[skip ci]` (the batch's last `Item:` push, which opens BATCH-CLOSE; the skill, CI cadence).

| STOP. Batch B10-character closes here |
