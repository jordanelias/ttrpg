# VERBS SOCIAL1 · A — form only what can be done: believed co-location, and `covenant` on a Proposition

## Status: PROPOSED

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

1. **R-WITH.** One person-side reader, `queries/person_q.py::believed_with(claims, other, now, window) ->
   bool`: True when the newest FIRSTHAND claim in `claims` that names `other` — a `seen` claim with
   `Seen.who == other`, a deed claim whose subject is `other`, or a told claim whose last teller
   (`chain[-1]`) is `other` (the three sources `known_persons` already reads, restricted to firsthand
   contact) — has `when >= now - window`. A firsthand claim is deposited by WITNESS only to persons present
   at the Event, so a recent one is the person's own evidence that `other` is near. `window` is the
   fixture `with_belief_window`. No world read (AX-2).
2. **Read by conjunct, never by verb.** In formation, for every row whose `requires_typed` carries a
   `relation` conjunct with `relation: with`, the conjunct's `of:` operand must be `believed_with` the
   actor: in `_person_bags`, a fanned person (`to`) failing it forms no bag; in `opening_set`, a referent
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

1. `engine/season/data/fixtures.py` — a scalar:
   ```
   with_belief_window=<ticks of one season>,   # S1-A R-WITH; H-<next>; swept: 0 (only same-tick contact),
                                               # one season (SHIPPED), None = unbounded (CONTROL: today's formation)
   ```
   The shipped value is read from the calendar's season length, not spelt (`loop/calendar.py` owns it);
   `[UNVERIFIED]` the name of that constant. A NUMBER row in `engine/season/hole_register.yaml` with the
   three-point sweep, allocated from `references/id_reservations.yaml`.
2. `engine/season/queries/person_q.py` — beside `known_persons`:
   ```python
   def believed_with(claims, other: str, now: int, window: "int | None") -> bool:
       """S1-A R-WITH: does the holder's own FIRSTHAND contact place `other` with him recently? ..."""
       if window is None:
           return True                      # the control: today's formation
       newest = max((c.when for c in claims or () if c.firsthand and _names_in_contact(c, other)),
                    default=None)
       return newest is not None and newest >= now - window
   ```
   `_names_in_contact` reads the same three sources and roster keys as `known_persons`
   (`KNOWN_PERSON_CLAIM`), restricted to `c.firsthand`; one helper both call, so the two cannot disagree on
   what a contact is.
3. `engine/season/decision/options.py` —
   - `_person_bags`: compute once per row `with_ops = row.with_operands()` (a new read-only method on
     `VerbRow`, `data/verbs.py`, returning the `of:` operands of its `relation: with` conjuncts; no verb
     name). In the `for who in people` loop, skip `who` when any fanned name is in `with_ops` and
     `not believed_with(p.ledger, who, now, fx.get("with_belief_window"))`.
   - `opening_set`: where a referent binds `subject`, skip it when `"subject" in row.with_operands()` and
     `believed_with` fails.
   - `now`: the deliberation's tick as the question or view carries it; `[UNVERIFIED]` which object holds
     it at formation. If neither does, the person's own latest claim tick (`max(c.when for c in
     p.ledger)`) is a person-side now and needs no world read.
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

- **Control:** `with_belief_window = None` reproduces the before hash byte for byte (the reader returns True
  and no bag is dropped). If it does not, the edit has moved something other than formation.
- **Planted failure:** a hand-built person whose only claim naming B is firsthand at tick 0, deliberating
  at tick `window + 1`, forms no `argue` to B; the same person with one firsthand claim at `window - 1`
  forms it. If the first arm forms, the conjunct is not being read.
- **The claim this could get wrong:** that firsthand contact implies co-location. If a firsthand claim can
  be deposited to someone not present (a channel that deposits remotely), the reader over-forms; check
  `loop/witness.py`'s firsthand deposit rule at landing and say so in the commit body.

## NERS reading

- **N:** top-down R-05 counts these verbs as not built out while most of what they form is refused;
  bottom-up the reader composes three existing claim sources; laterally one rule repairs eight rows by
  their conjunct. Removing it leaves ~80 refused acts per two seasons.
- **R:** adds no option; makes a person spend his scenes on people he believes are near. Complete at its
  extremes: window 0 forms only on same-tick contact; `None` is today.
- **S:** one reader, read by conjunct; the fold untouched, so world-only truth still decides.
- **E, last:** one function, one fixture, one row method and one class line against the largest
  dead-end share in the family.

## Cost class

Edit: one reader, two formation reads, one fixture, one row key. Declared re-record of the season pins that
carry these formations.
