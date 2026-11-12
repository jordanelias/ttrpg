# 14 · VERBS · MATERIAL · E — `research` that teaches what it read, `reconstruct` that concludes

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-22, C-24) — §2: `observes:` is a flat list, not keyed by Degree; `finding_terms` owns which reads a band deposits (`U5c_FI_residue.md` §8). §3: `reconstruct` writes nothing and deposits its conclusion to its maker; the Proposition is his `utter` (`U5c_FI_residue.md` §7).

## Status: PROPOSED

Batch M-E of `audits/14_VERBS_MATERIAL.md` §18 (its §13, §14). Needs batch M-D (papers with content) and
M-A §2 (the renamed route, the failure rule). It **decides the bands and the row text** for two designs
the FI lane wrote and does not redo them: `08_FI_03_playable-inquiry.md` §2 (the `observes:` column) and
§3 (the conclusion), `08_FI_04_small-edits.md` §1 and §2 (the refusal's name; presence),
`08_FI_06_testimony-names-a-hand.md` (the pairing that travels). Reference under CLAUDE.md §0.05. Read at
`84d2a02`.

## 1. What changes in `engine/season/` at runtime

A researcher who wins his draw holds what the paper says and who keeps it, firsthand, without holding the
paper; a narrow win gives him a drifted reading. `reconstruct` is drawn, and at a winning band its actor
utters a Proposition stating what he concludes was done and, at Success or better, by whom. Declared hash
mover.

## 2. `research`

**Problem.** 71 / 95 / 67 attempted at seeds 0 / 1 / 2; 20 / 19 / 19 finds; a find deposits *a finding
was made* and, for a forged paper only, the found claim (0 at three seeds, `audits/08_FI_audit.md`
F-FI-03). The researcher never learns the content and need not be where the paper is (H-319).

| owner | edit |
|---|---|
| `verb_table.yaml`, `research` | below |
| `engine/season/data/verbs.py`, `loop/resolve.py::_fold` | FI-03 §2's `observes:` column as written, with one addition this proposal decides: the column is **Degree-keyed** like `emits:`, so a row says what each band teaches |
| `loop/witness.py` | the Observation deposit (the second deposit) already lands an Event's observations in the actor's ledger; a `content:` read is deposited as the `content:<kind>` claim a holder would get, **without** a `hold`; at a band the row marks `lossy` the value passes through `_told_value`'s drift |
| `queries/world_q.py::questions_for` | `research` forms on bare `Record`; SOCIAL2-A's `_stamped` must keep the `(id, Record)` pair beside `(id, Record.<kind>)` (`audits/14_VERBS_MATERIAL.md` §17.2) |

```yaml
  - verb:        "research"
    stratum:     "uncontested_material"
    eligibility: ["own", "presence:<site>"]
    beneficiary: "actor"
    referent_class: Record
    capability:  inquiry
    difficulty:  demanding        # SC-B: reproduces today's obstacle of 2; + `subject` (the Record's forgery_quality)
    requires:    "the record consulted exists, the researcher is where it is, and he is one person"
    requires_typed:
      all:
        - {form: existence, of: subject, kind: Record}
        - {form: relation,  of: subject, relation: present_at}     # FI-04 §2
        - {form: relation,  of: actor, relation: individual}
    writes:      []
    observes:
      Overwhelming: [{read: content, of: subject}, {read: held_by, of: subject}]
      Success:      [{read: content, of: subject}, {read: held_by, of: subject}]
      Partial:      [{read: content, of: subject, lossy: true}]
      Failure:      []
    emits:
      Overwhelming: ["finding.made"]
      Success:      ["finding.made"]
      Partial:      ["finding.made"]
      Failure:      ["finding.none"]
    emits_on_refusal: ["inquiry.refused"]                          # FI-04 §1
```

The found deposit (`loop/witness.py::_found_claims`, `modules/fieldwork/find.py`) is unchanged: on a
forged or covertly made paper it still adds the trail's terms by band. `[UNVERIFIED: that `present_at` is
answerable for a Record; FI-04 §2 says a Record is where its holder is (`world_q.place_of`), and the
`present_at` stem today resolves a Site or a Rung only (`queries/world_q.py:4574`), so the stem gains a
Record branch through `place_of`.]`

## 3. `reconstruct`

**Problem.** 84 / 91 / 113 attempted, 82 / 89 / 110 executed, each depositing only *a finding was made*
(H-218, H-315); the row is ungraded because *"no value space"* (K-37).

**Decided where FI-03 §3 left a design pass.**

1. *The value space* is `queries/person_q.py::deed_doer` over the actor's own ledger (with FI-06, a told
   deed carries its pairing, so hearsay can name a hand). New, World-free, beside `said_of`:

```python
def concluded_of(ledger, subject, fx) -> "Optional[Concluded]":
    """What the holder would conclude about `subject`: the newest deed claim he holds whose patient or
    object is `subject` (`attributed_deeds` / `is_deed`), the doer `deed_doer` gives it (or None), and the
    number of independent chain roots among his claims of that deed. None where he holds no deed claim on
    it, or already holds a Proposition he uttered concluding on it. `Concluded(deed, doer, roots)`."""
```

2. *It rides the act.* `opening_set` copies `concluded_of` onto the Candidate under `concluded`, as it
   copies `said`, and declines when it is `None`. The row's named `own_ledger` conjunct is the hook, as
   for `tell`. Where the ledger offers several doers the fan is `choice_sourced` (`reconstruct:
   [concluded]`), so a player and a chooser pick among the same candidates.
3. *The roll.* It joins `graded_acts`. Pool `inquiry`. Obstacle: difficulty `demanding`, less SC-B's
   `evidence` term at `proof_step` per independent root beyond the first (`Concluded.roots − 1`):
   corroboration makes the conclusion easier to reach, which is need e2 of the arc adjudication.
4. *The product.* At a winning band the effect utters a HOLDS Proposition through `_eff_utter`'s own body
   and `_makers_hold`: content `{deed, patient, doer}` at Overwhelming and Success, `{deed, patient}` at
   Partial. At Failure nothing is uttered (`finding.none`; the alternative is J-M2 of the audit's §19 and
   would change this band only).
5. *What it unlocks.* `rosters.yaml: terms_sourced` gains `petition: [<the conclusion's kind>]` so a
   petition forms from a held conclusion with its `terms` the named doer (`_eff_carry`'s documented
   route); a hearing may cite it (FI-05-B E-1 treats it as the citer's own claim, not a `record`).

```yaml
  - verb:        "reconstruct"
    stratum:     "uncontested_material"
    eligibility: ["own"]
    beneficiary: "actor"
    capability:  inquiry
    difficulty:  demanding        # − `evidence`: proof_step x (independent roots − 1)
    requires:    "the actor holds a claim of a deed done to or about the subject, and is one person"
    requires_typed:
      all:
        - {form: own_ledger, of: subject, conjunct: holds}
        - {form: relation,  of: actor, relation: individual}
    writes:
      Overwhelming: ["Proposition.exists"]
      Success:      ["Proposition.exists"]
      Partial:      ["Proposition.exists"]
      Failure:      []
    emits:
      Overwhelming: ["conclusion.stated"]
      Success:      ["conclusion.stated"]
      Partial:      ["conclusion.stated"]
      Failure:      ["finding.none"]
    emits_on_refusal: ["inquiry.refused"]
```

`[UNVERIFIED: the matrix pair `utter` declares for a Proposition's existence; the row reuses whatever
`utter`'s `writes:` names, and `conclusion.stated` joins that pair's `emits:` in the same commit, as
`faction.surveyed` did for `survey`.]` `rosters.yaml: graded_acts` gains `reconstruct`; the
`graded_inquiries` note's sentence that `reconstruct` *"waits on a value space nothing supplies"* is
struck.

## 4. Order of landing

1. FI-04 §1 (the refusal's name) and §2 (presence), if not landed.
2. `research` with the Degree-keyed `observes:` (FI-03 §2's column lands here for this row; `examine`
   and `surveil` take it in the PHYSICAL family's batch).
3. FI-06 (the pairing travels).
4. `reconstruct`.

## 5. Gate and falsifier

- **`research`.** FI-03's §2 gate on `inquiry_world`, seeds 0 to 2: a hearer's `record` of a liar reads
  1.0 before his `research` of the contradicting account and below 1.0 after a `Success`; at a planted
  `Partial` he holds a drifted value; at `Failure` nothing. Control: `observes:` empty reads 1.0
  throughout. Realm: no `research` executed by someone not where the paper is.
- **`reconstruct`.** FI-03's §3 gate over 20 seeds: a Proposition is uttered in more than zero folded
  acts (today 0 of 82 / 89 / 110); at least one run names someone who is not the deed Event's actor and
  at least one names the actor; a `petition` forms from a held conclusion; with two independent roots
  the share of winning bands is higher than with one, at the same pool.
- **Falsifiers.** A `content:` claim deposited with a `hold`. A conclusion naming a person the actor's
  ledger does not hold. A `reconstruct` formed on a subject he holds no deed claim about. FI-03's own:
  all 20 runs name the true actor (then nothing in the scenario can mislead).
- **Planted failure.** Compute `concluded_of` from the Event log instead of the ledger: FI-01's
  silent-change arm must move a candidate and go red.

## 6. NERS reading (E last)

N: the investigation scale is `in_loop: False` and has no outcome; without a conclusion nothing reaches a
bench from an inquiry. Top-down (R-05, R-07), bottom-up (a column, a copied operand, `utter`'s mint),
lateral (SC's `cites`, CHAR's `record`), diagonal (a player's conclusion and an NPC's are one
Proposition). R: three routes to a name (paper, place, testimony); a wrong name acted on; a
half-conclusion that names no hand. S: one route, one ladder, one mint; the refusal and the failure are
two kinds. E, last: one column keyed by band and one retyped row, against the family's two most executed
verbs teaching nobody anything.

## 7. Cost class

`research`: small build. `reconstruct`: small build after FI-06. Lanes: FI (owner), SC, CHAR.
