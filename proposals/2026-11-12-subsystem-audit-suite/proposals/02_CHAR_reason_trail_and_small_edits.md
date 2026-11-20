# CHAR — a reason a reader can follow, and the small edits the audit decided

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-05, §4) — Part A stands; the stored deciding term is `U5a_CHAR_owed_amendments.md` §5. B1 is the same edit as workplan IN-14's own narrowing of `offices` (holds with non-empty `granted_acts`) and lands once, there. Part C's two `requirements.yaml` `measured:` rewrites (R-06, R-08) land as those rows' `reading:` records (`01_CORE_requirements_reading_record.md` §1); its `decision/sheet.py` docstring row is the same edit as `U5a_CORE_owed_edits.md` §B row 10 and is carried here.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.2 row (Part A CONFORMS with a reader question; B1 AMBIGUOUS), §7, §7b-T; `unified/U3_CONFLICT_LEDGER.md` C3-L8, §9; `unified/U3_DEPENDENCY_ORDER.md` node B09, §6.3 (`explain`/`Derivation`)). Changed: **B1 is deleted** — `budget_office_bonus` is removed (C3-L8: `04` §A.3 row 15 refuses an office bonus in `budget`; carried by `U5a_CORE_owed_edits.md` §H), so the seat count is not read by `budget()` and nothing lands in IN-14 (the U5a line above is overtaken); Part A's sheet `terms` are read through `04` §C.11's named reader `person_q.explain(p: PersonInterior, v) -> Derivation` (built by the GO lane, B34) rather than copied from `score_terms`, so the sheet half moves to B34 and the hook half stays in B09; Part C's two `requirements.yaml` `measured:` rewrites land as `reading.does_not_show` (the head line, applied to the table); named tests, lands-it and tier.

**Lands in batch:** B09 (Part A's `watch` hook and the three harness repoints; B2; Part C); Part A's sheet `terms` in B34 with `11_GO_player_surface_contract_B.md`. **Depends on:** `01_CORE_requirements_reading_record.md` (B02, the `reading:` shape).

## Status: PROPOSED

Written by the CHAR audit lane (`audits/02_CHAR_audit.md`, §0A item (d), §6 table 2). Ratifies nothing.
Reference under `CLAUDE.md` §0.05.

## What this changes in `engine/season/` at runtime

Part A adds an observer hook to the chooser that is `None` by default and writes nothing: hash EQUAL.
Part B's code edits: B1 is deleted (C3-L8; the office bonus is removed by `U5a_CORE_owed_edits.md` §H); B2
(`pack_scenes`' `by_subject` arm) moves nothing at the shipped `greedy`; B3 (set-order sums) is in
`02_CHAR_resolve_and_temper.md`. Part C is text.

## Part A — the reason trail

**Problem.** After a decision nothing records why it was taken. `Act.reads` is empty for every act in
a seeded realm (H-343, register line 6312). §F1's `why` was cut from `Candidate` (`opening_set`'s
docstring: *"§F1's `why`: gone"*). What survives is the OCCASION: `pack_scenes` puts the question on
the `Scene` (`choose.py:716-746`), so an act cites what raised it. Which term decided, and whether the
draw overrode the score, is known inside `make_ranker` for the length of one call and then lost. Three
harnesses recover it by wrapping the chooser and scoring every deliberation a second time
(`decision_spread.play_season`'s `watched`, `interactions`, `aperture`), each in its own wrapper.

**Resolution (ladder step 5; the observer rule of `ED-IN-0225` is the constraint).** No carrier, no
field on `Act`, no Event. `make_chooser` takes one more optional argument:

```python
def make_chooser(fx, mint, verbs=None, draw=None, watch=None):
    # watch(p, q, ranked, terms, sampled) -> None, called once per deliberation after the order is
    # sampled and before it is packed. `ranked` is `score_order`'s list, `terms` the parallel
    # `score_terms` tuples, `sampled` `_sample_order`'s list. The chooser ignores its return value and
    # passes copies; a watcher that mutates changes nothing that is packed.
```

- `harness/decision_spread.py`, `interactions.py` and `aperture.py` pass a `watch` and delete their
  wrappers and their second scoring (one owner of "what the chooser saw").
- `decision/sheet.py::DevelopmentSheet` gains `terms`, parallel to `candidates`, so the player sees
  why each option ranks where it does. They are read through `04` §C.11's one reader of "the arithmetic of
  what the character already holds", `person_q.explain(p: PersonInterior, v) -> Derivation` (no World
  parameter), whose `Derivation` carries the same terms `score_terms` sums; not copied from the chooser.
  `explain` is built by the GO lane (`11_GO_player_surface_contract.md` §2, B34; U3 §6.3), so this half lands
  in B34.
- A chronicle reader (`harness/chronicle.py`, outside the simulation) can then print, for an act,
  the question that raised it, the deciding term (`decision_spread.attribute_top`'s rule, moved beside
  `score_order` so the rule has one owner under `decision/`) and whether the draw outvoted the score.

**Gate.** `watch=None` and a `watch` that records: equal `content_hash` at seeds 0–2 (the G2 spy
`test_g2_token.py` already asserts DELIBERATE mutates no store). `decision_spread --decisions` prints
the same deciding-term counts through the hook as through the wrapper (223 draw, 265 pursuit, 10
stance at seed 0, `main`'s reading). Named tests (new, `engine/season/tests/test_choose_watch.py`):
`test_a_recording_watcher_leaves_the_hash_equal`, `test_a_reordering_watcher_changes_no_act`,
`test_decision_spread_counts_equal_through_hook_and_wrapper`; the existing
`engine/season/tests/test_in62_decision_spread.py` stays green unedited.

**Falsifier.** A watcher that returns a reordered list changes no act: if the hash moves, the hook is
a steering surface and is wrong.

**NERS.** N: without it no one, player or reader, can say why a character acted, which is the
legibility cap `research/by_lane/NPC_npc_cast.md` T-NPC-8 names. R: a player's sheet that shows the
terms teaches the model. S: one observer for three instruments and the sheet. E: one argument replaces
three wrappers.

**Cost.** Edit.

## Part B — code edits decided in the audit's §6

| # | edit | owner | why (ladder step) | gate |
|---|---|---|---|---|
| B1 | **deleted** (C3-L8): `budget_office_bonus` is removed, so the seat count is not read by `budget()`; H-330's defect (a held survey sheet earning the bonus) goes with the bonus | `U5a_CORE_owed_edits.md` §H carries the edit (`decision/budget.py:58`, `data/fixtures.py:592`) | 1, 3: `04` §A.3 row 15 refuses an `office_bonus` in `budget` | `U5a_CORE_owed_edits.md` §H's |
| B2 | `pack_scenes`' `by_subject` arm orders subjects by first appearance in the ranked list, not `sorted(seen)` | `decision/choose.py:793-797` | 4: U4 removed the alphabet as a tie-break for verbs; this is the same defect for subjects on an unshipped arm | at `scene_packing_rule: by_subject`, renaming a subject id does not change which scene runs first (named test, new: `engine/season/tests/test_choose_watch.py::test_by_subject_packing_ignores_id_names`) |
| B3 | the three set-order sums iterate `_AXES` | see `02_CHAR_resolve_and_temper.md` edit 3 | 4 | hash EQUAL |

## Part C — text corrections at the owners (each a superseded sentence; ladder step 1)

| file | now reads | should read |
|---|---|---|
| `decision/options.py::project` docstring; `decision/choose.py` comment in `make_ranker` | *"thirteen conviction weights, in the four-axis basis"*; *"weights over the THIRTEEN ... four-axis basis"* | fifteen pursuits over seven bipolar axes (`ED-IN-0261`, the 2026-10-06 row) |
| `decision/sheet.py` module docstring | the design is *"PROPOSED and HELD BACK (ED-1094)"* | RATIFIED (Jordan, 2026-11-05, ED-IN-0349), as `proposals/2026-10-07-character-sheet-spaces.md`'s Status line reads |
| `data/cast.py` module docstring | *"31 a `territory`, 30 `goals`, 29 `stats`, 32 `ts`"* (keys present) | the non-null counts at this tree (`goals` 17, `stats` 1, `ts` 10, `lifepath` 5, `heritage` 4), or no counts |
| `engine/season/requirements.yaml` R-08 `disposition:` | cites `engine/season/decision.py::make_chooser` | `engine/season/decision/choose.py` (`make_ranker`, `score_order`) |
| `requirements.yaml` R-08 `measured:` head (lands as R-08's `reading.does_not_show`, `01_CORE_requirements_reading_record.md` §1) | *"NON-RATIONALITY DOES NOT EXIST ... a tie breaks ALPHABETICALLY"*, retracted four paragraphs later | open with the standing state: the order is sampled at `choice_temperature`; ties among equal non-zero scores are 4 of 498 readings; the residue is that the departure is realm-wide and not the person's (this audit's F-CHAR-02) |
| `requirements.yaml` R-06 `measured:` head (lands as R-06's `reading.does_not_show`) | *"What's missing is a READ over it (no `ambitions(p)` query anywhere)"*, retracted at position `17` in the same row | open with the standing state: `world_q.ambitions` exists; the residues are the correlated basis and that no term reads a goal once a question is formed (F-CHAR-01) |
| `hole_register.yaml` H-189 `default:` | *"whether a crisis fires within a season is not measured here"* | measured 2026-11-12, `build_realm`, two seasons: `Person.conviction` rewritten for 0 of 46 cast at seed 0 and 6 of 46 at seed 1 |
| `hole_register.yaml` H-237 | *"over 2 seasons at seed 0 there are 0 told claims with a chain"* | re-read 2026-11-12: 12 chained claims of 22,958 at seed 0, 5 of 21,469 at seed 1, none at two hops; `teller_weight` is reached, rarely |
| `CURRENT.md` character-model row | head `proposals/2026-09-20-pursuit-basis-worksheet.yaml` | the owners the worksheet's own header names (`references/descriptor_registry.yaml: pursuit_roster`, `axis_roster`; `engine/season/rosters.yaml: tables.pursuit_projection`, `tables.alignment`); then the worksheet is deleted with an exact-file `FORK:` row, as its header says it is once its values land. It lists `faith` and `warden`, which the 2026-10-06 row renamed |

None of Part C changes behaviour. The `requirements.yaml` and register edits change a row's text, not
its `status:`.

## Lands it and tier

Part A's hook, B2 and Part C: the B09 batch, an IN `valoria-author` session on `sonnet` (`high`), closed by
B09's `methodology-close` once. Part A's sheet `terms`: B34 with `explain`. **Hash movers.** None (control:
`watch=None`).
