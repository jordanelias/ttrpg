# 16 · PESSIMIST · FI · B — A paper its holder knows is false is not read as true

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 (CONFORMS), §7/§7b (edit 4 located, tests,
tier); U3 B26, §6.2 (`p3b_knows.py`, `p3_forgery.py` are not in the repository); U1 D-U1-01 and architecture §4 (what is
not training reaches a roll as a named level, never a die: the "one more die" in "Not edited here" restated as a level).
Changed: edit 4's location, the gate, one sentence of "Not edited here". A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "training" for the rank → skill score (1).

## Status: PROPOSED

Lands in batch: **B26** (FI). Depends on: `08_FI_05_evidence-interface_B.md`, `19_LACUNA_admission_rides_the_citing_draw.md`
(B24) and `18_DETERMINISM_notice_is_a_draw.md` (B11) for what makes a holder know; the edits themselves read only
`COVERT_KINDS` and the holder's ledger (exist).

Carries `audits/16_PESSIMIST_FI.md` F-PES-FI-03 (§2.3) and the correction to addendum B's C-3 (§2.2).
Compatible with `08_FI_05_evidence-interface_B.md` (a forgery "cites at full weight until someone cites
a finding of it") and `19_LACUNA_admission_rides_the_citing_draw.md`; it supplies the person-side half
those two assume and no proposal builds: what the *holder* does once he knows.

## What this changes in `engine/season/` at runtime

1. A person whose own ledger holds a covert-kind claim on a Record (he saw it forged, or found it so)
   stops reading operands and names off that Record's content.
2. A sheet key that is present and empty forms no candidate (today the operand binds the paper itself).

Declared hash mover only for worlds in which a holder of a forged Record also knows it is forged: none
in the shipped realm at seeds 0 to 2 over three seasons (0 of 52, 57 and 40 forgeries left their
forger's hand), so the shipped hashes do not move until a forgery travels.

## The problem, with evidence

`p3b_knows.py` (tiny world, shipped fixtures; the forger's `forge`, `move` and `give` are real acts):

| holder | knows it is forged? | candidates | of them, addressed to the forger off the sheet's `head` |
|---|---|---|---|
| a clerk who watched the forging, then is handed the sheet | yes: `(paper, record.forged, True)` firsthand, and the sighting naming the forger | 116 | 19 |
| the same clerk, those claims deleted from his ledger (control) | no | 116 | 19 (the same candidates) |
| the Duke, before examining it | no | 193 | 28 |
| the Duke, after his own `Success` find (`(paper, record.forged)` and `(forger, record.forged)` held) | yes | — | 21; the content claim is unchanged at confidence 100, `firsthand` |

`p3_forgery.py`: on a surveyed (genuine) sheet whose `head` is `None`, the same candidates form with
`to` bound to the Record's own id (`interview … to <paper>`, `move … to <paper>`, `challenge … to
<paper>`): 12 and 16 such candidates for the two receivers, every one of which the fold must refuse.

Owners. `decision/options.py::_content_answer` is the one reader of `rosters.yaml:
record_sourced_operands`; its two channels are `_from_content_claim` and `held_record_claims`.
`queries/person_q.py::ledger_names` reads a content claim's `ABOUT_KEYS` value into the set of names a
person has heard of. None of the three asks whether the holder believes the paper. The content claim's
subject is the paper, so `LedgerReader` has no cell on which a contradicting claim could outrank it.

## Resolution, decided

Disbelief is a reading of the holder's own ledger: a Record he holds a covert-kind claim on is
*doubted*, and a doubted Record's content answers nothing for him. It is not a draw: the draw was the
examination that found the forgery, or (once `18_DETERMINISM_notice_is_a_draw.md` lands) the notice that
saw it made. Others are unaffected until he tells them or cites it.

Ladder: step 4. `epistemic.holds_trail` already treats *"he holds `(s, e.kind, True)` on the written
thing"* as "he knows of this deed"; `rosters.yaml: covert_kinds` is the data that says which kinds mean
"this paper is not what it says". The same test, read where the content is read.

## Edits, by owner

1. **`engine/season/queries/person_q.py`**, one reader beside `ledger_names`:
   `doubted(claims) -> frozenset`: the subjects of held claims whose predicate is a `COVERT_KINDS`
   member (`data/rosters.py`) with a true value. Person-side, World-free; reads the holder's own ledger
   (AX-2). Kinds come from the roster, so a covert kind that does not write a Record adds ids no content
   claim has, and changes nothing.
2. **`engine/season/decision/options.py::held_record_claims`** and **`::_from_content_claim`**: a
   content claim whose subject is in `doubted(p.ledger)` is skipped (computed once per call).
3. **`engine/season/queries/person_q.py::ledger_names`**: its content branch skips the same claims, so a
   name he knows only from a paper he knows is false is not a name he has heard.
4. **`engine/season/decision/options.py`, the record-sourced operand derivation** (`_derive_operand`'s
   `held=` channel): where `record_sourced_operands` maps the operand to a key and that key's value is
   `None` or an empty list, the bag is not formed. The one reader of the roster is
   `decision/options.py::_content_answer` (`:948` on 2026-11-12; `key = RECORD_SOURCED_OPERANDS.get(...)` at
   `:959`) and the answerable set `_RECORD_ANSWERABLE` (`:970`); the fallback that binds the Record's own id is
   found before editing by `rg -n "_content_answer\|_RECORD_ANSWERABLE" engine/season/decision/options.py` and
   reading each call site: the edit is at the call site that substitutes the Record id when `_content_answer`
   returns `None`.

Order of edits: 1 → 2 → 3 (hash-equal in shipped runs) → 4 (the mover), one commit each.

## Not edited here, named

- **"Someone who knows better" as odds.** The premise asks that the reader's knowledge raise his chance
  of detection. Today `research`'s pool is `seam/wrappers/pool.py::faculty(w, p, verb)` plus
  `POOL_ADDENDS`, each `add(w, p, verb)`: no addend can see which Record is examined, so none can ask
  whether the examiner holds a second paper of the same kind about the same subject that says otherwise
  (`person_q.ABOUT_KEYS` is the key that would pair them). That is a named level for *comparing two
  papers* (a leverage source; what is not the roller's skill score reaches the roll as a level, never a die,
  U1 D-U1-01), and it needs the act in the source's signature; `10_DICE_advantage_sources_for_the_arcs.md`
  is where advantage sources are being gathered. Named for DICE; no edit here.
- **What a forgery says.** `_eff_forge` writes the forger in as `head` for every forger (F-FI-10;
  `08_FI_02` §4 item 9 leaves it a declared default).

## Gate (execution artifact)

The probes were lane scratch (not in the repository, U3 §6.2). Written first as NEW
`engine/season/tests/test_doubted_paper.py`: `test_holder_who_saw_the_forging_forms_no_candidate_off_the_sheet`,
`test_control_ledger_without_the_claims_forms_them`, `test_empty_sheet_key_forms_no_bag`,
`test_ledger_names_skips_a_doubted_paper`. Command: `python -m pytest engine/season/tests/test_doubted_paper.py -q`;
then `report` / `delta HEAD` (hash equal through edit 3). The scratch readings, once committed as those tests:

`p3b_knows.py`, unchanged: row 1 reads 0 candidates addressed off the sheet and row 2 (control) reads
19; row 4 reads 0. `p3_forgery.py`: 0 candidates with `to` equal to a Record id on the surveyed sheet.
The shipped realm's content hash at seeds 0 to 2, three seasons, is unchanged by edits 1 to 3 (no holder
doubts a held paper there); edit 4 moves it and says so.

## Falsifier

A person who holds `(paper, record.forged, True)` and a candidate of his whose operand was read off
that paper's content, in any world.

## NERS reading

N: the forged key is the forgery's whole effect (`_FORGED_SHEET_KEY`); a holder who cannot stop
believing it makes detection pointless, so the reader of doubt is necessary to `forge`, `research` and
the found deposit at once (lateral), and to a hearing's struck exhibit (diagonal: the citer who knows is
then lying by citing). R: a holder now has a real choice after a find: keep the paper and say nothing,
tell, or cite the finding. S: one test (`holds a covert-kind claim on the thing`) shared with
`holds_trail`; no second vocabulary. E, last: one reader, three call sites, no field, no table.

## Cost class

Edit. Lane FI. Tier: `sonnet`, effort `high`. Hash movers declared: none for edits 1-3 at seeds 0-2; edit 4
moves every world where a sheet key is empty (re-pinned once in B26). Lands it: B26, after
`19_LACUNA_questioning_has_an_approach_and_a_cost.md`, before `16_PESSIMIST_FI_D`.
