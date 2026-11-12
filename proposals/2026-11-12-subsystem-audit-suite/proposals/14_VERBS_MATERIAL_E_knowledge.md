# 14 · VERBS · MATERIAL · E — `research` that teaches what it read, `reconstruct` that concludes

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-22, C-24) — §2: `observes:` is a flat list, not keyed by Degree; `finding_terms` owns which reads a band deposits (`U5c_FI_residue.md` §8). §3: `reconstruct` writes nothing and deposits its conclusion to its maker; the Proposition is his `utter` (`U5c_FI_residue.md` §7).
Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head applied to the body (`unified/work/R4_READ.md` §1.2, 7b.4): `research`'s `observes:` is flat and `finding_terms` owns the band (C-24); `reconstruct` is an inquiry (writes nothing; its `Proposition.exists` bands, `conclusion.stated` and the `[UNVERIFIED]` matrix pair are struck; the conclusion is deposited to its maker and the Proposition is his later `utter`, C-22, `19_LACUNA_conclusion_is_a_committed_assertion.md`; U1 S-21); the `evidence` subtraction becomes the `proofs` leverage source (C-01, A-25; C3-C10's rule); `graded_acts` → `graded_tasks` (D-U1-11i); the `present_at` `[UNVERIFIED]` confirmed at the tree (`queries/world_q.py:4574-4577` resolves a Site or a Rung only, so the Record branch through `place_of` is needed); A-81 for `finding.none` (C3-C11), A-30, U3 batch B26, R4 7b.0 block.

## Status: PROPOSED

Lands in batch: B26 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), after `14_VERBS_MATERIAL_D_paper.md` in the same batch.
Depends on: `08_FI_03_playable-inquiry.md` §2 (the `observes:` column), `08_FI_04_small-edits.md` §1–§2, `08_FI_06_testimony-names-a-hand.md`, `19_LACUNA_conclusion_is_a_committed_assertion.md` (all B11); `U5c_FI_residue.md` §7–§8 (`finding_terms`; R2's lane); `14_VERBS_MATERIAL_A_mending.md` (B12); `14_VERBS_MATERIAL_D_paper.md` (B26); `U5c_SC_one_obstacle_form.md` §3 (B05: the `proofs` source).
Lane: FI. Tier (R4 7b.0 (1)): `sonnet` producer, effort `high`; one `opus` read of the 20-seed `reconstruct` table (the judgment node: whether a wrong name occurs). Test file: `engine/season/tests/test_vm_mat_e_knowledge.py` (one function per §5 gate, on FI-03's `inquiry_world`).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the actor's trained `inquiry` score (A-6); talent as levels (A-7); a wound a level against the roll (A-8). Draws: `H(w.world_seed, w.tick, <actor id>, "research.task")`, `"reconstruct.task"` (A-30). **A-81:** `finding.none` is in `rosters.yaml: undeposited_kinds` today (WITNESS deposits nothing for it); under A-81 a failed inquiry still leaves the searcher his own firsthand claim that he looked and found nothing, `(subject, research.failed, True)` / `(subject, reconstruct.failed, True)`, deposited to the actor only (`observation_deposit_mode: actor`, `14_VERBS_MILITARY_A` edit 6's precedent; D-46), so he does not repeat the same search blind. The roster edit is the inquiries' general rule and is listed for the FI rewrite lane (`U5c_FI_residue.md`); these two rows depend on it.

Batch M-E of `audits/14_VERBS_MATERIAL.md` §18 (its §13, §14). Needs batch M-D (papers with content) and
M-A §2 (the renamed route, the failure rule). It **decides the bands and the row text** for two designs
the FI lane wrote and does not redo them: `08_FI_03_playable-inquiry.md` §2 (the `observes:` column) and
§3 (the conclusion), `08_FI_04_small-edits.md` §1 and §2 (the refusal's name; presence),
`08_FI_06_testimony-names-a-hand.md` (the pairing that travels). Reference under CLAUDE.md §0.05. Read at
`84d2a02`.

## 1. What changes in `engine/season/` at runtime

A researcher who wins his draw holds what the paper says and who keeps it, firsthand, without holding the
paper; a narrow win gives him a drifted reading. `reconstruct` is drawn, and at a winning band its actor
holds his own conclusion of what was done and, at Success or better, by whom; he commits to it publicly
only by a later `utter` (C-22). Declared hash mover.

## 2. `research`

**Problem.** 71 / 95 / 67 attempted at seeds 0 / 1 / 2; 20 / 19 / 19 finds; a find deposits *a finding
was made* and, for a forged paper only, the found claim (0 at three seeds, `audits/08_FI_audit.md`
F-FI-03). The researcher never learns the content and need not be where the paper is (H-319).

| owner | edit |
|---|---|
| `verb_table.yaml`, `research` | below |
| `engine/season/data/verbs.py`, `loop/resolve.py::_fold` | FI-03 §2's `observes:` column as written: a **flat** list (C-24). Which of the row's reads a band deposits, and which band marks a read `lossy`, is `finding_terms`' (`U5c_FI_residue.md` §8), keyed by degree there, not on the row *(W3-4a: the Degree-keyed column this file first proposed is withdrawn)* |
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
    observes:    [{read: content, of: subject}, {read: held_by, of: subject}]   # flat (C-24)
    # finding_terms (U5c_FI_residue.md §8): O and S deposit both reads; P deposits `content`, lossy; F none
    emits:
      Overwhelming: ["finding.made"]
      Success:      ["finding.made"]
      Partial:      ["finding.made"]
      Failure:      ["finding.none"]
    emits_on_refusal: ["inquiry.refused"]                          # FI-04 §1
```

The found deposit (`loop/witness.py::_found_claims`, `modules/fieldwork/find.py`) is unchanged: on a
forged or covertly made paper it still adds the trail's terms by band. *(Verified by W3-4a at
`queries/world_q.py:4574-4577`: the `present_at` stem resolves a Site or a Rung and answers `UNKNOWN`
otherwise.)* FI-04 §2 says a Record is where its holder is (`world_q.place_of`), so the stem gains one
Record branch through `place_of` (FI-04 §2's edit; this row depends on it).

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
3. *The roll.* It joins `graded_tasks` as an inquiry. Pool `inquiry`. Obstacle: difficulty `demanding`.
   Corroboration is **leverage for the roller, not an obstacle subtraction** (A-25, C-01): the `proofs`
   source (`U5c_SC_one_obstacle_form.md` §3) gives one level per independent root beyond the first
   (`Concluded.roots − 1`), soft-capped with every other level. Corroboration makes the conclusion easier to
   reach, which is need e2 of the arc adjudication.
4. *The product (W3-4a, C-22).* `reconstruct` writes nothing. At a winning band WITNESS deposits the
   conclusion to its maker as his own firsthand claim (content `{deed, patient, doer}` at Overwhelming and
   Success, `{deed, patient}` at Partial; the reads `finding_terms` names per band); the HOLDS Proposition
   exists only when he later `utter`s it with `cites` (`19_LACUNA_conclusion_is_a_committed_assertion.md`,
   the one mint of a committed conclusion). At Failure nothing is concluded (`finding.none`; the
   alternative is J-M2 of the audit's §19 and would change this band only).
5. *What it unlocks.* `rosters.yaml: terms_sourced` gains `petition: [<the conclusion's kind>]` so a
   petition forms from a held conclusion with its `terms` the named doer (`_eff_carry`'s documented
   route); a hearing may cite it (FI-05-B E-1 treats it as the citer's own claim, not a `record`).

```yaml
  - verb:        "reconstruct"
    stratum:     "uncontested_material"
    eligibility: ["own"]
    beneficiary: "actor"
    capability:  inquiry
    difficulty:  demanding        # + levels from the `proofs` source: one per independent root beyond the first
    requires:    "the actor holds a claim of a deed done to or about the subject, and is one person"
    requires_typed:
      all:
        - {form: own_ledger, of: subject, conjunct: holds}
        - {form: relation,  of: actor, relation: individual}
    writes:      []               # an inquiry (C-22): the conclusion is a deposit to its maker
    emits:
      Overwhelming: ["finding.made"]
      Success:      ["finding.made"]
      Partial:      ["finding.made"]
      Failure:      ["finding.none"]
    emits_on_refusal: ["inquiry.refused"]
```

`rosters.yaml: graded_tasks` gains `reconstruct`; the route note's sentence that `reconstruct` *"waits on
a value space nothing supplies"* is struck. *(W3-4a: the earlier `Proposition.exists` bands, the kind
`conclusion.stated` and the `[UNVERIFIED]` matrix pair are withdrawn with them.)*

## 4. Order of landing

1. FI-04 §1 (the refusal's name) and §2 (presence), if not landed.
2. `research` with the flat `observes:` and its `finding_terms` rows (FI-03 §2's column lands here for
   this row; `examine` and `surveil` take it in the PHYSICAL family's batch).
3. FI-06 (the pairing travels).
4. `reconstruct`.

## 5. Gate and falsifier

- **`research`.** FI-03's §2 gate on `inquiry_world`, seeds 0 to 2: a hearer's `record` of a liar reads
  1.0 before his `research` of the contradicting account and below 1.0 after a `Success`; at a planted
  `Partial` he holds a drifted value; at `Failure` nothing. Control: `observes:` empty reads 1.0
  throughout. Realm: no `research` executed by someone not where the paper is.
- **`reconstruct`.** FI-03's §3 gate over 20 seeds: a conclusion claim is deposited to its maker in more
  than zero folded acts (today 0 of 82 / 89 / 110); at least one run's conclusion names someone who is not
  the deed Event's actor and at least one names the actor; a `petition` forms from a held conclusion; a
  Proposition exists only after the maker's `utter` (CONC's gate); with two independent roots the share
  of winning bands is higher than with one, at the same pool (the `proofs` level).
- **A-81.** A planted `Failure` of either row leaves the actor's own `(subject, <verb>.failed, True)`
  claim; count of failed inquiries with zero durable writes, expected 0 once the `undeposited_kinds` edit
  lands.
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
half-conclusion that names no hand. S: one route, one ladder, one mint (`utter`); the refusal and the
failure are two kinds. E, last: one flat column and one retyped row, against the family's two most
executed verbs teaching nobody anything.

## 7. Cost class

`research`: small build. `reconstruct`: small build after FI-06. Lanes: FI (owner), SC, CHAR.
