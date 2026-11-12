# FI — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Subsystem: fieldwork, investigation, epistemics, information, witness. Lane tag `FI` (with the `IN`
epistemic work the dossier files here). Written head-first (brief, "write early"); later sections were
appended as the reading and the probes completed. Every execution reading below carries its seed and season
count; `PYTHONHASHSEED=0` throughout. Scratch output: the session scratchpad, `runs/FI/`.

## 0. Verdict

[written last; see the end of §0 once the probes are in]

## 1. What it is, as coded

**Three layers, one of which is the game's whole information model.**

1. **The witness barrier** — `engine/season/loop/witness.py::witness` (bound onto `SeasonDriver`, barrier 4).
   Input: the round's `Event[]`. For each Event it asks `epistemic.observers_for` who is admitted and by
   which channel, then deposits, into each admitted person's OWN `Person.ledger` through the write gate
   (`w.write("claim_ledger", token, …, emits="claim.deposited")`), up to six kinds of `Claim`:
   (1) an event-kind claim per subject `claim_subjects` names (`predicate = e.kind, value = True`);
   (2) one claim per `Observation` the fold made, in the `requires` vocabulary (`stores:<kind>`,
   `condition`, …), to the actor alone at the shipped `observation_deposit_mode`;
   (3) one `seen` claim whose value is `epistemic.Seen(stratum, marks, who, why)`, terms masked per channel;
   (4) a `content:<kind>` claim to whoever came to hold a Record this tick;
   (5) for `news.told`, the told claim — the `Said` the teller fixed at CHOOSE, lossy at `Partial`
   (`_told_value`), source `told_by`, `chain = teller's chain + (teller,)`, confidence refracted
   (`_refract`) and credited by shared regime (`_credit`);
   (6) the found deposit (`_found_claims`) for a graded inquiry that uncovered a covert deed's trail.
   It then evicts over `ledger_cap` through the gate. It owns no state but the ledger writes.
2. **The channel and knowability rules** — `engine/season/epistemic.py`: the five `_ch_*` predicates
   (`co_located`, `witness_key`, `document_key`, `chronicle`, `post_remit`), built into `CHANNEL_PREDICATES`
   from `rosters.yaml: witness_channels`; `observers_for` (one strongest channel per person);
   `claim_subjects` (what a deposit is about); `Seen` and its term readers; `trail_of` / `holds_trail`
   (what an inquiry can still uncover); and `belief_contradicts` — the single place a person's own ledger
   can refuse a candidate (§F1 clause 4), called by bare name from `decision/options.py::opening_set`.
3. **The information verbs** — `engine/season/loop/effects_information.py` (records, propositions,
   matters: `create_record`, `issue`, `give`, `forge`, `survey`, `conceal`, `seize`, `petition`, `carry`,
   `open_case`, `determine`, `convene`, `argue`, `utter`, …) and the six investigation acts as
   `verb_table.yaml` rows (`examine`, `interview`, `research`, `surveil`, `thread_read`, `reconstruct`),
   whose graded band reaches the registered module `modules/fieldwork/find.py` through the `inquiry`
   composition role (`seam/wrappers/fieldwork.py`).

Beside these: `queries/person_q.py` (the ledger readers — `LedgerReader`, `said_of`, `regard`,
`ledger_names`, `drifted`, `deeds_judged`), `queries/inputs.py` (the typed input records a host builds for a
module entry), and `systems/fieldwork/sim/knots.py` (a Knot lifecycle oracle the season loop does not call).

**How a decision reads it.** `loop/driver.py::_questions_at_barrier` calls
`queries/world_q.py::questions_for(w, p, since)` for every person at barrier 2 — a RESOLVER-SIDE function that
takes the `World` — and hands the `Question[]` to `loop/deliberate.py`, which builds a `View`
(ids + questions + one `odds` callable) and calls `choose(p, v, s, ask_budget)`. `decision/` names no `World`
(the `View.__getattr__` raises `Forbidden`). So what a person may act on is: his own `Person` (ledger,
`tenures`, body, pursuits), the `Question[]` the projection built for him, and `Fixtures`.

[execution evidence appended in §1a below]
