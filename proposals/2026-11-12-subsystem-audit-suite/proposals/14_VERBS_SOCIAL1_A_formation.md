# VERBS SOCIAL1 · A — form only what can be done: believed co-location, and `covenant` on a Proposition

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-19) — `believed_with` and the `with_belief_window` fixture are not added: the one reader of believed co-location is `person_q.present_persons` (`08_FI_02_rumour-that-travels.md` edit 5; fixture `telling_hearers`). R-WITH, the reading conjunct by conjunct, stands. A refusal on the `with` conjunct teaches its actor (decision register D-46; `U5c_VERBS_residue_and_governance_owner.md` §3).
Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head line applied to the body (`unified/work/R4_READ.md` §1.5, 7b.6; U5c C-19): "The resolution, decided" item 1 and edits 1 to 3 are replaced (no `believed_with`, no `with_belief_window`; formation reads `person_q.present_persons` under `08_FI_02`'s `telling_hearers` fixture); the gate's control is that fixture's `known` arm; U3 batch B11, R4 7b.0 block. This file adds no draw.

## Status: PROPOSED

Lands in batch: B11 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), after `08_FI_02_rumour-that-travels.md` edit 5 in the same batch.
Depends on: `08_FI_02_rumour-that-travels.md` edit 5 (`person_q.present_persons`, the `telling_hearers` fixture; MISSING in the tree until it lands); `02_CHAR_offer_what_can_be_done.md` (B10: the one decline this reading sits inside).
Lane: SC. Tier (R4 7b.0 (1)): `sonnet` producer, effort `medium`; one `opus` read of the before/after refusal table. Test file: `engine/season/tests/test_vm_s1_a_formation.py` (the planted-failure arms and the `aperture 2 s` reading as functions).

Batch S1-A of `audits/14_VERBS_SOCIAL1.md` §14. Written under `VERBS_BRIEF.md` (FAMILY = SOCIAL1).
Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12). Reference only
(CLAUDE.md §0.05); not ratified by being written. Read at `84d2a02`.

## What it changes in `engine/season/` at runtime

Which Candidates form. (1) A person stops forming an act whose `with` conjunct names someone his own
recent firsthand claims do not place with him (`argue`, `lie`, `give`, `challenge`; and by the same
conjunct `tell`, `fight`, `accept`, `capture`). (2) `covenant` stops forming on referents that are not
Propositions. No effect, band, write or draw changes. The fold's `with` stays WORLD-ONLY. A declared hash
mover wherever those Candidates formed.

**Standing rule (`AUDIT_BRIEF.md`, *"we do not do deterministic"*):** this batch decides only whether an
act may be *attempted* — formation, the rule's own carve-out. It resolves no outcome. Every outcome of
these verbs is drawn, in batches S1-B..D (`audits/14_VERBS_SOCIAL1.md` §0.6).

## The problem, with evidence

`aperture 2 0` (`scratchpad/runs/VERBS_PHYSICAL/aperture_2_0.txt`, realm, two seasons, `PYTHONHASHSEED=0`):

| verb | attempted | refused | deciding read |
|---|---|---|---|
| `argue` | 41 | 31 | `with=False` 31 |
| `lie` | 22 | 16 | `clause:hearer` 16 (the `with` conjunct) |
| `give` | 19 | 18 | `with=False` 17 |
| `challenge` | 84 | 84 | `with=False` 13 (after lane A removes `exists:Person` 65 and `dispute=False` 6) |
| `covenant` | 10 | 10 | `exists:Proposition=0` 10 |

Cause of the first four: `person_q.known_persons` names everyone the person has ever seen or heard from;
`decision/options.py::_person_bags` fans `to` over all of them; `with` is WORLD-ONLY
(`data/requires.py: WORLD_ONLY_STEMS`) and the refusal is never deposited (`known_persons`' docstring), so
the same refused act is formed next round. Cause of the fifth: the `covenant` row declares no
`referent_class`, so it forms on the question's plain referents (persons, rungs).

## The resolution, decided

1. **R-WITH.** *(W3-4a, C-19: the reader is not this file's.)* The one person-side reader of "who I believe
   is with me" is `queries/person_q.py::present_persons(p.ledger, p.id)` (`08_FI_02_rumour-that-travels.md`
   edit 5), under its fixture `telling_hearers`; a person whose newest firsthand claim at a place is
   `absent` drops out of it (`U5c_VERBS_residue_and_governance_owner.md` §3). No world read (AX-2). This
   file adds no second reader and no second fixture.
2. **Read by conjunct, never by verb.** In formation, for every row whose `requires_typed` carries a
   `relation` conjunct with `relation: with`, the conjunct's `of:` operand must be in `present_persons` of
   the actor: in `_person_bags`, a fanned person (`to`) failing it forms no bag; in `opening_set`, a referent
   bound to `subject` failing it forms no Candidate. Where CHAR-OFFER (`02_CHAR_offer_what_can_be_done.md`)
   has landed, this is one reading inside its one decline; until then, it is one helper in
   `decision/options.py` called at those two sites.
3. **`covenant` is classed `Proposition`** — `argue`'s and `commit`'s class, the rung-4 repair of
   `03_PC_duel_chain_reach.md` (REM-28's precedent).
4. **R-KIND is lane A's** (`03_PC_duel_chain_reach.md` edit 4). This batch only records that it repairs
   `comply` (33 `exists:dispensation=0`), `evade / defy` (5) and `carry` (9 `exists:petition=0`); no edit.

The fold is unchanged: a man whose sighting is stale but within the window, or who is simply wrong, is
still refused by the world. That refusal is information he does not receive today (decision D2 in the
audit file, for Jordan).

## Exact edits, by owner, in landing order

1. *(W3-4a: the `with_belief_window` fixture is withdrawn, C-19.)* No fixture is added here: the window
   and its control are `08_FI_02`'s `telling_hearers` (`known` is the control arm that reproduces today's
   formation).
2. *(W3-4a: `believed_with` is withdrawn, C-19.)* No reader is added to `queries/person_q.py`; formation
   calls `present_persons(p.ledger, p.id)` once per deliberation (`08_FI_02` edit 5).
3. `engine/season/data/verbs.py` and `engine/season/decision/options.py` —
   - `VerbRow.with_operands()` (new, read-only, `data/verbs.py`): the `of:` operands of the row's
     `relation: with` conjuncts; no verb name.
   - `_person_bags`: compute once per row `with_ops = row.with_operands()` and once per deliberation
     `near = present_persons(p.ledger, p.id)`. In the `for who in people` loop, skip `who` when any fanned
     name is in `with_ops` and `who not in near`.
   - `opening_set`: where a referent binds `subject`, skip it when `"subject" in row.with_operands()` and
     the referent is not in `near`.
4. `engine/season/verb_table.yaml`, row `covenant` — add after `beneficiary_note:`:
   ```yaml
       referent_class: Proposition
       referent_class_note: "S1-A (`proposals/2026-11-12-subsystem-audit-suite/proposals/14_VERBS_SOCIAL1_A_formation.md`): the terms are an uttered Proposition (the cell's second conjunct), so the row forms only on one -- `argue`'s and `commit`'s class, REM-28's precedent for `convene`. MEASURED before: `aperture 2 0` 10 of 10 refused `exists:Proposition=0`. [ASSUMPTION; medium; Jordan to correct; revert: drop both keys.]"
   ```
5. `engine/season/hole_register.yaml` — on the rows that record the `with` refusals for `tell`/`give`
   (`H-229`'s cite names `give` unreached): a dated line naming this batch; no row is closed by it.

Nothing in `modules/`, the seam, the fold or any effect changes.

## Gate (execution artifact)

`python -m engine.season.harness.aperture 2 s`, s = 0, 1, `PYTHONHASHSEED=0`, before and after, quoted in
the commit body:
- `argue` `with=False`, `lie` `clause:hearer`, `give` `with=False`, `challenge` `with=False` each fall by at
  least half;
- `covenant` `exists:Proposition=0` = 0 and `covenant` attempted ≥ 1 (else say so: the class may leave
  seated persons with no Proposition referent, which is then the next link);
- the `ex` column of each of the five, reported as measured.

## Falsifier and control

- **Control:** `telling_hearers: known` (`08_FI_02`'s control arm: `present_persons` returns every known
  person) reproduces the before hash byte for byte, no bag dropped. If it does not, the edit has moved
  something other than formation.
- **Planted failure:** a hand-built person whose ledger places B elsewhere (B not in `present_persons`)
  forms no `argue` to B; the same person whose newest firsthand claim places B with him forms it. If the
  first arm forms, the conjunct is not being read.
- **The claim this could get wrong:** that firsthand contact implies co-location. If a firsthand claim can
  be deposited to someone not present (a channel that deposits remotely), the reader over-forms; check
  `loop/witness.py`'s firsthand deposit rule at landing and say so in the commit body.

## NERS reading

- **N:** top-down R-05 counts these verbs as not built out while most of what they form is refused;
  bottom-up the reader composes three existing claim sources; laterally one rule repairs eight rows by
  their conjunct. Removing it leaves ~80 refused acts per two seasons.
- **R:** adds no option; makes a person spend his scenes on people he believes are near. Complete at its
  extremes: `telling_hearers`' narrowest arm forms only on present contact; `known` is today.
- **S:** one reader (FI's), read by conjunct; the fold untouched, so world-only truth still decides.
- **E, last:** one row method, two formation reads and one class line against the largest dead-end share
  in the family.

## Cost class

Edit: one row method, two formation reads, one row key. Declared re-record of the season pins that
carry these formations.
