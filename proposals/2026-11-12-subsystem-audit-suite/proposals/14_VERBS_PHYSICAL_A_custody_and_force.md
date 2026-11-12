# VERBS · PHYSICAL · A — custody and force: `arrest`, `capture`, `fight`, `accept`

## Status: PROPOSED

Batch P-A of `audits/14_VERBS_PHYSICAL.md` §10.3. Carries that file's §1 to §4 and §0.6 (the standing
rule). Lands after lane A (`03_PC_duel_chain_reach.md`) and FA-P2 (`06_FA_remit_grant_by_row.md`).
Reference only (CLAUDE.md §0.05). Authored by Opus completing a Fable lane cut off by the usage limit
(2026-11-12).

## What it changes in `engine/season/` at runtime

1. Officers form `arrest` on persons named by warrants **addressed to them and heard of**, as well as
   warrants they hold. The licence for `arrest` and `seize` is read by one owner (A1).
2. `capture` forms only on persons, and only under a `war` or `crime` context. Its custody goes to the
   court whose warrant it enforces (A2).
3. `fight` loses its `duel` context. Its terms follow the context, and a felled party's death is a draw
   in the seam (A3).
4. `accept` forms on challenges addressed to the person and heard of (A4).

Declared movers: every realm and spine pin in which these formations occurred (`capture`'s 26
formations, `accept`'s 37, the arrest stamp's new referents). Every season `fight` and `accept`
scene that ends in a felling under `death` terms (A3 item 3 adds draws). The corpus pins of the 13
`fight` scenes.

## The problem (evidence)

`aperture 2 0` (realm, two seasons; `scratchpad/runs/VERBS_PHYSICAL/aperture_2_0.txt`):

- `arrest` formed 1, attempted 0.
- `capture` formed 26, attempted 12, executed 0, refused 12 (`with` 7, `exists:Person` 3,
  `individual` 2).
- `fight` formed 0 (H-row at `hole_register.yaml:5321`: every `violence_context_of` reading `None` over
  three seeds).
- `accept` formed 37, refused 27 of 27 on `exists:challenge=0`.

Corpus: 13 `fight` scenes, 8 `Felled`. F-PC-04: a plain fight kills in 200 of 200.

## The resolution, decided

See the audit §1.3, §2.3, §3.3 and §4.3. Summary: one addressed-Record reader serves warrants and
challenges. `capture` gets the ruled violence decline. `fight`'s terms follow its context, and death is
drawn. The duel is `accept`'s alone.

## Exact edits, by owner

### A0 — the shared primitive (`engine/season/queries/world_q.py`)

```python
def addressed_records(w: World, p: Person, kind: str) -> tuple[str, ...]:
    """Live Records of `kind` whose addressee key (`RECORD_CONTENT["addressee"]`) is `p.id` and whose id
    `p`'s own ledger names (`person_q.ledger_names`), sorted. A Record addressed to a man who has not
    heard of it is not his business. The one owner of "addressed to him and heard of", read by the
    warrant stamp (A1) and the challenge stamp (A4). Resolver-side, read-only (`detainees_held`' shape).
    No mint, so ED-IN-0292 (1) stands."""
```

### A1 — `arrest`

| file (owner) | edit |
|---|---|
| `engine/season/queries/world_q.py` | add `warrants_for(w, actor, prisoner) -> tuple[str, ...]`: dispensations whose `terms` (via `record_sourced_operands`' `subject` key) is `prisoner` and that `actor` holds (`_held_warrants`' body, moved here from `loop/effects_information.py:948`) **or** that are in `addressed_records(w, actor_person, "dispensation")`, in tenure order then id. |
| same | add stamp term `warrants_heard(w, p)`: the persons named by `addressed_records(w, p, "dispensation")`, stamped in `_stamped` (`:3836`) under `Person`. |
| `engine/season/loop/effects_information.py` | `_eff_arrest` and `_eff_seize`: replace `_held_warrants(w, a.actor, a.verb, prisoner)` with `warrants_for(w, a.actor, prisoner)`. Delete `_held_warrants`, since nothing else calls it `[verify by grep at landing]`. Docstrings: name the addressee half and cite this file. |
| `engine/season/decision/options.py` (`:255-266`) | `warranted` is the union of today's held-claims set and the person's `warrants_heard` stamp, read off `q.referents_for("Person")` where `addressed_records` put them. Pass the stamp through the Question, not the World (AX-2). |
| `engine/season/verb_table.yaml`, row `arrest` | `requires_typed_note`: replace *"`arrest` forms only on a `subject` a HELD dispensation's `terms` names"* with *"…a dispensation he holds, or one addressed to him that he has heard of (`world_q.warrants_for`, `14_VERBS_PHYSICAL_A`), names"*. Add `payload_note`: the act's payload carries `warrant` (the Record id the effect licensed on), written by `_eff_arrest` on its Event for the reason trail. No other column changes. |

### A2 — `capture`

| file | edit |
|---|---|
| `verb_table.yaml`, row `capture` | add `referent_class: Person` and `referent_class_note: "14_VERBS_PHYSICAL_A A2: the challenge repair of 03_PC_duel_chain_reach (REM-28's precedent). Removes the exists:Person refusals. [ASSUMPTION; medium; revert: delete the column]"` |
| `rosters.yaml: violence_contexts` | add the line `capture: [war, crime]`. In the note, add: *"`capture` (14_VERBS_PHYSICAL_A): ED-IN-0337 applied to the second violent row; no `duel` (a duel is `accept`'s), no `defence` (a man defending himself does not take prisoners)."* |
| `loop/effects_combat.py::_eff_capture` (`:334`) | the `detain` object is `issuing_seat(w, rid)` of the first `rid` in `warrants_for(w, a.actor, captive)` that passes `_may_close_custody`. Otherwise it is `a.via`, as today. Docstring: "custody goes to the court whose warrant it is: `arrest`'s rule, one owner". |

### A3 — `fight` (and the scene for `capture`/`accept`)

| file | edit |
|---|---|
| `rosters.yaml: violence_contexts` | `fight: [war, crime, defence]` (drop `duel`). Note: *"`duel` dropped (14_VERBS_PHYSICAL_A A3): the challenger holds every challenge he issues, so the context licensed him to attack under lethal terms without acceptance; a duel is `accept`."* |
| `rosters.yaml` | new roster `context_terms` (`duel_terms`' shape): `war: death`, `crime: yield`, `defence: yield`. Loader: each key a `VIOLENCE_CONTEXT_READERS` name, each value a `duel_terms` value, refused at import otherwise (`data/verbs.py`, beside `WARRANT_SOURCED`'s check). |
| `decision/options.py::opening_set` | when the violence decline admits a referent, record the context name on the Candidate's payload as `context`. The payload key is new and goes on the closed payload-key roster `[name the roster at landing: the one `posture` and `term` live in]`. |
| `seam/wrappers/combat.py::combat_input` | terms = `duel_terms[verb]` if present, else `context_terms[payload["context"]]` if present, else `death`. One path (CP-T03-09's `terms` path). |
| `seam/wrappers/combat.py` (after the scene, before typing the result) | **the mortal-wound draw**: for each party with `felled` true, one roll through the one roller (`10_DICE_one_roller_one_fraction_rule.md`): pool = his body band before the felling (`band_floors` over `Person.body_ceiling`), obstacle = `Fixtures.mortal_wound_ob[terms]` plus named modifiers (the `tend` key of a co-located ally, SE). Failure: `felled` stays true (dies). Partial: `felled` false, `wounds = max_wounds` (left for dead; the lasting mark follows, CP-T03-07). Success and better: `felled` false, wounds as scene. The private per-round stream (`03_PC_duel_round_and_approach_B.md` §1) supplies the draw. |
| `data/fixtures.py` | `mortal_wound_ob: {death: <swept>, yield: <swept>, blood: <swept>}`, swept, `H-` row for its source. The shipped values are chosen by the gate's sweep, not written here. |
| `engine/season/tests/test_cr87_violence_contexts.py` | re-point the duel positive control to `accept` (A4). Assert `fight` does **not** form for a challenger on his own challenge. |
| `verb_table.yaml`, row `fight` | `writes_source_note`: append *"the per-party `felled` is the seam's AFTER the mortal-wound draw (14_VERBS_PHYSICAL_A A3): a felling is not a death with certainty (standing rule, 2026-11-12)."* No band, cell or kind changes. |

### A4 — `accept`

| file | edit |
|---|---|
| `queries/world_q.py` | stamp term `challenges_heard(w, p)` = `addressed_records(w, p, CHALLENGE_KIND)`, stamped under `Record` in `_stamped`. |
| `verb_table.yaml`, row `accept` | `referent_class_note`: replace the sentence beginning *"⚠ A CHALLENGE IS MINTED INTO THE CHALLENGER'S HAND"* through *"…until H-229's `give` reaches the realm."* with *"A challenge is minted into the challenger's hand. The challenged forms `accept` on it once he has heard of it (`world_q.challenges_heard`, 14_VERBS_PHYSICAL_A A4); the cell asks nothing of holding."* |

### Order of landing

A0, then A1 (one commit: the reader, the stamp, both effects, the formation). Then A2. Then A4, then
A3 (the `duel` drop must not land before A4, or no route to a duel exists in between). The mortal draw
in A3 may land alone, first, since it is independent of reach.

## Gate (execution artifacts)

The audit's §1.7, §2.7, §3.7 (including the standing-rule gate) and §4.7, as four test files under
`engine/season/tests/`. Plus `aperture 2 0` and `aperture 2 1` before and after, quoted in the commit:
`capture` refusals on `exists:Person` equal 0, `accept` refusals on `exists:challenge` equal 0, and
`arrest` and `capture` formed and attempted as measured.

## Falsifier

The planted failures named in each gate: revert to `_held_warrants`, delete the `capture` roster line,
restore `duel`, bypass the mortal roll, and return `()` from `challenges_heard`. Each must turn its test
red. The control `mortal_wound_ob` at an unreachable value must reproduce 200 of 200 deaths in the
F-PC-04 probe.

## NERS reading

- **N.** It turns custody, hostages, duels and survivable violence from built-but-unreached into play.
  Cut test per verb: audit §1.9 to §4.9.
- **R.** Beaten survivors exist (resentment, ransom, pardon, return). Courts hold people. The no-player
  half produces crimes, arrests and feuds.
- **S.** One addressed-Record reader. One licence owner for `arrest`, `seize` and `capture`'s custody.
  One terms path. One roller for the mortal draw.
- **E (last).** Two readers, two stamps, two roster lines, one roster, one draw, against four verbs
  brought into play. High.

## Cost class

Build: two `world_q` readers and two stamps, an effect edit in two modules, one seam draw, one fixture,
roster lines. Declared re-records of the season pins named above.
