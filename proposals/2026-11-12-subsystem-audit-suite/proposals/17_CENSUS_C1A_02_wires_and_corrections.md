# Census C1A · 02 — wires and text corrections for the season loop's core packages

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-16) — W4 and `02_CHAR_scar_cap_and_regard_unit.md`'s Addendum both edit `decision/choose.py::_stance_arm`, and are two facts about one term, not two terms: `regard_sign` is how the act treats its subject, `beneficiary:` is whom it is done for. At the arm `beneficiary` the term is `regard_sign(row) × regard(p, subject)` plus `regard(p, b)` where the row's beneficiary `b` is neither the subject nor the actor; the same clamp and `stance_scale` apply to the sum (`U5a_CHAR_owed_amendments.md` §2). W4 lands after the `regard_sign` column, so neither is counted twice.

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/U3_CONFLICT_LEDGER.md` C3-K3, C3-N7; `unified/U3_DEPENDENCY_ORDER.md` §3.1 and §4.1 rows 35-41; `unified/work/R5_READ.md` §2 row C1A_02:W4, §7 and 7b). Changed: (1) W4's three edits are carried by `02_CHAR_scar_cap_and_regard_unit.md`'s Addendum (B10), written once there (C-U5a-16, C3-K3); W4 keeps its problem, its gate and its NERS reading as the census row's closing reading, and makes no separate edit; (2) "68 rows" is 67 (C3-N7: 67 verb rows, the 68th `beneficiary:` match is the key `beneficiary_note:` at `verb_table.yaml:661`, re-verified by `grep`); (3) the dependency edges follow the batch order (D2 no longer waits for GO-B; W1 rides with GO-B in B34; each W2 verb's gate rides with that verb's batch); (4) tier named. Not changed: C1, W3 (complete, CONFORMS).

Depends on: `02_CHAR_scar_cap_and_regard_unit.md` Addendum (B10, carries W4); `U5a_CHAR_owed_amendments.md` §2 (B10). W1 rides with `11_GO_player_surface_contract_B.md` (B34); W2's gates ride with `14_VERBS_MATERIAL_C_works.md` (B12), `14_VERBS_BINDING_A_formation.md` (B21), `14_VERBS_MILITARY_A_movement.md`, `_C_the_muster.md`, `_D_the_order_of_battle.md` (B22) (`U3_DEPENDENCY_ORDER.md` §4.1 rows 35-41, SPLIT).
Lands in batch: B10 (C1, W3, and `17_CENSUS_C1A_01_deletion_batches.md` D1's `defects` row in W3's commit); W1's gate in B34; W2's gates in B12, B21, B22.
Tier: sonnet / high (C1, W3, the gates); W4's flip, when a sweep is read, is opus (a balance judgment).

## Status: PROPOSED

Author: census lane C1A. Audit: `audits/17_CENSUS_C1A.md` (F-C1A-02 to F-C1A-07). Read at b805fad.
Ordered by risk, lowest first: C1 (text), W3 (a loader refusal), W1 and W2 (wires other proposals
already carry; this lane adds the gate each row is closed by), W4 (a new arm on the ranker).

## What it changes in `engine/season/` at runtime

- C1: nothing (comments).
- W3: nothing on the shipped registry; a registry row whose faction cell has an unbalanced parenthesis
  refuses at load where today it loads.
- W1, W2: nothing from this lane. The wires are in the GO and VERBS proposals named below.
- W4: nothing at the shipped arm (the control). At the new arm, the ranker's second term regards the
  person an act is done for, where today it regards the act's subject on every row.

---

## C1 · nine comment pointers to code that moved or was dropped (mislabelled: correct)

Found by resolving every `` `file.py::symbol` `` in the partition's comments against `git ls-files`
(700 pointers, 12 unresolved, 9 confirmed at the site). Old text → new text:

| site | old | new |
|---|---|---|
| `data/rosters.py:796` | `` `loop/effects.py::_eff_build` `` | `` `loop/effects_founding.py::_eff_build` `` |
| `data/arrangements.py:31` | `` `loop/effects.py::_eff_determine` `` | `` `loop/effects_information.py::_eff_determine` `` |
| `queries/world_q.py:1702` | `` `loop/effects.py::_eff_migrate` `` | `` `loop/effects_migration.py::_eff_migrate` `` |
| `data/fixtures.py:1094` | `` `loop/effects.py::_eff_oblige` and `_eff_transfer` `` | `` `loop/effects_governance.py::_eff_oblige` and `loop/effects_economy.py::_eff_transfer` `` |
| `queries/faction_q.py:56` | `` `loop/effects.py::_eff_survey` `` | `` `loop/effects_information.py::_eff_survey` `` |
| `epistemic.py:460` | `` `shape.py::SeasonDriver::_fold::ev` `` | `` `loop/resolve.py::_fold`, its `ev` `` |
| `epistemic.py:490` | `` emitted in `shape.py::SeasonDriver::matter` `` | `` emitted in `loop/matter.py` (`:127`) `` |
| `epistemic.py:626` | `` (`tests/test_obligees.py`, through the real fold and WITNESS) `` | `` (the test that showed it, `tests/test_obligees.py`, was dropped at `FORK:217340fc`, ED-IN-0314) `` |
| `epistemic.py:631` | `` `test_obligees.py::test_17a_the_channel_reads_the_obligee_set_through_establishment_of` `` | the same name followed by `` (dropped with its file, `FORK:217340fc`) `` |

And one that follows deletion batch D1: `seam/__init__.py:26`, "with the `PATH_SEAM_ALLOWED` member and
`files.COMBAT_SEAM_PY` renamed in the same commit" → "with the `PATH_SEAM_ALLOWED` member renamed in the
same commit".

The effect split is real (`data/files.py::effects_modules` discovers the eight `effects*.py` files and
says the aggregator holds no effect body); `shape.py` no longer exists; `_fold` is at
`loop/resolve.py:343` and `matter` at `loop/matter.py:284`.

Gate: re-run the resolver scan; the nine sites resolve. No guard is proposed (a comment's accuracy is a
reader's discipline). Cost class: edit.

---

## W3 · the cast loader refuses a faction cell it cannot have read whole

**Problem.** `data/cast.py:408-423 defects()` reports two things and nothing calls it. One is not a
defect: a faction cell that resolves to no roster name (three rows today, all `Independent (...)`,
which `harness/populated.py:1312` treats as unaffiliated). The other is: an unbalanced parenthesis in the
cell, which the function's own text explains as an unquoted `#` eaten as a YAML comment, destroying a
seat number. That is corrupted input to `faction_of`, which feeds `populated`; it crosses into the
engine, so the loader's refusal is the licensed shape (`CLAUDE.md` §0.05, "the loader's refusal per data
family").

**Edit** (`engine/season/data/cast.py::_rows`, after `_CACHE` is built at `:104`; `defects` is deleted by
D1 in the same commit):

```python
for cid, r in _CACHE.items():
    raw = str(r.get("faction") or "")
    if raw.count("(") != raw.count(")"):
        raise Unspecified(
            f"{cid}: faction cell {raw!r} has an unbalanced parenthesis", "references/npc_registry.yaml",
            needs="the cell quoted, so an unquoted `#` is not read as a comment",
            law="ID-5 -- refuse, don't default: a truncated cell resolves to a faction with its seat lost")
```

**Gate.** `python -c "from engine.season.data import cast; print(len(cast.load()))"` prints the row count
(the shipped registry has no such cell: `defects()` returned none of that class). **Falsifier.** A fixture
registry with `faction: Crown (Seat` loads without raising. Cost class: edit.

---

## W1 · the character sheet's spaces get a caller (carried by GO; this lane names the closing gate)

**Problem.** `decision/sheet.py` (`creation_sheet`, `seat`, `development_space`, `take_ranked`,
`chronicle`; ten census names in all) is imported by `tests/test_g2_token.py`,
`tests/test_rem30_character_sheet.py` and `tests/test_cr20_attributes.py` only.
`harness/play_surface.py` does not import it.

**Resolution.** No edit from this lane. `11_GO_player_surface_contract_B.md` extends the file (`Situation`,
`Offer`, `account`) and its gate (`:241-242`) is the entry
`python -m engine.season.harness.play_surface --seed S --person P --seasons K`, which seats `P` with
`take_ranked`. That entry is the wire for all ten names, and it runs the code path the tests already pin
(the control: seated with `take_ranked`, the `content_hash` equals the automated run's).

**The gate these census rows close on.** After GO-B lands:
`grep -n "from ..decision.sheet import\|from ..decision import.*\(seat\|development_space\|chronicle\|creation_sheet\)" engine/season/harness/play_surface.py`
returns a line, and the entry above exits 0 at seed 0 printing the same hash as the plain run.
**Falsifier.** The entry prints a different hash from the unseated run at the same seed (the seat changed
the world it was meant only to read). If GO-B is not accepted, the rows stay broken and the decision
reverts to this lane: delete `sheet.py` with its two test files, since R-06's "character creation,
development, chronicling" scale would then have no surface at all and the file would be describing one.

---

## W2 · six helper rows whose effects never ran (carried by VERBS; this lane names the closing gate)

| census row | effect(s) | corpus reading | proposal that names the verb |
|---|---|---|---|
| `loop/effects_army.py:34 _army`, `:45 _payload` | `recruit`, `form_unit`, `assign_troops`, `disband_unit`, `discharge_troops`, `order_unit` | never attempted | `14_VERBS_MILITARY_C_the_muster.md`, `14_VERBS_MILITARY_D_the_order_of_battle.md` |
| `loop/effects_combat.py:686 _siege` | `march` | never attempted | `14_VERBS_MILITARY_A_movement.md` |
| `loop/effects_founding.py:26 _works_named`, `:45 _made_by` | `found`, `build` | only refused | `14_VERBS_MATERIAL_C_works.md` |
| `loop/predicates.py:260 founded_office_id` | `establish` (precondition and effect) | never attempted | `14_VERBS_BINDING_A_formation.md` |

The proposals were matched by the verb's name in their text; this lane did not read them through
[UNVERIFIED that each makes its verb execute].

**INCOMPLETE (W2), blocked outside this file:** whether each named VERBS file makes its verb execute is
checked by the verbs rewrite lane (W3-4a) against those files; this file supplies only the closing gate
below, which each verb's batch runs (B12, B21, B22).

**The gate these rows close on.** `python -m engine.season.harness.corpus_run`: each verb above appears
under `VERBS THAT EXECUTED`. Today's line reads 23 of 67 executed, 13 only refused, 30 never attempted.
**Falsifier.** A verb leaves "never attempted" by being injected into a case rather than formed by a
person's chooser (scripting drift: the count moves and the game has not).

---

## W4 · `beneficiary:` is read where regard is read

**Carried by `02_CHAR_scar_cap_and_regard_unit.md`'s Addendum (C-U5a-16, C3-K3): no separate edit.**
The three edits below are the content that Addendum writes once, as one term (`regard_sign(row) ×
regard(p, subject)` plus `regard(p, b)` for a beneficiary who is neither subject nor actor; one clamp,
one `stance_scale`); they stay here as the census row's reading, and the gate below is the census row's
closing gate, run in B10 after the Addendum lands.

**Problem.** `verb_table.yaml` declares `beneficiary:` on 67 rows (one per verb row; the 68th `grep`
match is the note key `beneficiary_note:` at `verb_table.yaml:661`, C3-N7) ("who the act is taken for the good
of", `data/verbs.py:172-174`); the loader refuses a value outside `beneficiary_kinds` and an operand
beneficiary the row cannot carry (`data/verbs.py:789-811`); `decision/choose.py:281-319 beneficiary_of`
resolves it for a candidate. Only `tests/test_governance_build.py` calls that function. The ranker's
second term, `stance_term` (`choose.py:56-98`), reads regard for `c.subject` on every row, with the sign
flipped where the subject is the act's opponent. So an act done *to* a person and an act done *for* one
weigh the same, and the column that tells them apart is read by nothing.

**Resolution, decided** (ladder step 5; the two alternatives are deletion of the column, which six VERBS
proposals that author new `beneficiary:` values and `01_CORE_capability_authoring_surface.md:78` would
then contradict, and leaving it inert, which the brief excludes). The column joins the term it was
declared for, as an arm, by the code's own rule for a term whose effect on choice is unmeasured
("declare it, default it, sweep it", `choose.py:108, :149, :229`):

1. `engine/season/rosters.yaml: stance_polarities` gains the member `beneficiary`, with a note: regard is
   read for the person the row declares the act is for; an opponent row keeps `declared`'s reading.
2. `decision/choose.py::_stance_arm` (`:101`) gains the branch. For `stance_polarity == "beneficiary"`:
   - a row whose subject is its opponent (`options.subject_is_opponent`): `declared`'s value, unchanged;
   - otherwise `b = beneficiary_of(p, c)`; if `b` is `None` or `b == p.id`, the term is `0.0`; else
     `regard(p, b, fx)` through the same per-deliberation memo.
3. `Fixtures.stance_polarity` stays `"declared"` (`data/fixtures.py:963`). The arm ships declared and
   unswitched; the flip is a separate commit that carries its measurement.

Typed interface: unchanged (`stance_term(p, c, fx, memo) -> float`). Person-side only: `beneficiary_of`
takes a `Person` and a `Candidate`, no `World` (its docstring `:284-288`), so AX-2's by-path scan over
`decision/` is unaffected. One owner per fact: the column stays in `verb_table.yaml`, the arm's name in
`rosters.yaml`, the formula in `stance_term`.

**Gate.** (a) At the shipped arm, a seeded one-season `content_hash` at seeds 0-2 equals the hash before
the commit. (b) At `stance_polarity="beneficiary"`, for one person holding regard for A and
none for B, a candidate of a row with `beneficiary: to`, bound to A, scores above the same candidate bound
to B (a test in `tests/test_governance_build.py`, beside
`test_lb6d_the_column_resolves_on_candidates_the_engine_actually_forms`, `:1014`). **Falsifier.** (a) the hash moves at the control; (b) the two candidates score equal, so
the arm reads nothing.

**What this does not settle.** Whether the arm should ship switched on. That is a balance claim, and
`CLAUDE.md` §7 records that the campaign-level instrument has no live successor; `harness.arms` compares
n seeds over one mechanic and is the nearest thing. Until a sweep is read, the column is reachable and
unswitched, which is one step better than unread and one short of working. This is the item in this
proposal that the CHAR lane's ranker proposals (`02_CHAR_which_ground_moves_whom.md`) should absorb.

**NERS reading.** N: holds bottom-up (the column gets its reader) and lateral (regard already has this
term); top-down it is narrowed until the sweep, since no case in the corpus is known to turn on it.
R: an NPC who helps those he regards and not merely acts on them is a distinguishable person; the
no-player half gains favours and partiality as generated material. S: one term, one gain, one memo; no
second ladder for regard. E, last: one roster member and one branch against 67 rows of authored data
that today do nothing.

Cost class: small build (the branch, the roster member, one test), carried by the Addendum; the flip is
design-first.

---

## Dependency edges

`C1` none. `W3` lands in B10 with deletion batch D1's `defects` row (moved from B03 for that reason).
`W1` ← `11_GO_player_surface_contract_B.md` (B34). `W2` ← the four VERBS proposals (each verb's gate in
its own batch). `W4` = `02_CHAR_scar_cap_and_regard_unit.md` Addendum (B10); `02_CHAR_which_ground_moves_whom.md`
(B24) cites the arm, not a second regard term. Deletion batch D2 no longer waits for GO-B: it lands in
B03 and GO-B depends on it (`U3_DEPENDENCY_ORDER.md` §4.1 row 4, reversed).
