# Workplan v12 — part 16, continued: Batch B11-fi-readers, positions B11.17 to B11.22

## Status: PROPOSED (the continuation of part 16 of workplan v12, `V12_STRUCTURE_part2.md` §4.1; drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05)

The batch block's head, the position table, its UNDECIDED line and the words and paths of these items are the part's main file. Written against `aa31fd2`, as the main file is.

### B11.17 — `Record.ttl` and everything that exists only for it, deleted · `08_FI_04` §4 with `17_CENSUS_REST_1` D2 · BUILD · HASH MOVER(encoding)
- SOURCE: `proposals/08_FI_04_small-edits.md` §4, first bullet (the second is B03's, C3-L8); `proposals/17_CENSUS_REST_1_deletions.md` D2 (U3 §4.1 row 11); D-04 (a field leaving a hashed carrier is an encoding mover); closes R-24, ID-13's `ttl` row, H-86 (irrelevant, ladder step 2), H-259's lapse.
- ADVANCES: none of the nine; a writ lapses by its own stages (one ladder, not two).
- INSTRUCTION, one commit (U3 §4.1 row 11: D2 "lands with it"):
  1. `08_FI_04` §4, copied: "**`Record.ttl`** has no reader. Delete the field and its `write_matrix.yaml` row (ID-13). A writ's end is its last declared stage maturing: `issue` already winds stages (`_declared_stages`) and MATTER matures them; `comply`'s cell gains 'the writ's last stage has not matured'." The field is `engine/season/state/carriers.py::Record.ttl` (`ttl: Optional[int] = None`); the matrix row is `engine/season/write_matrix.yaml`'s `kind: "Record"`, `field: "ttl"`, `steps: [MAT]`.
  2. `17_CENSUS_REST_1` D2's table, copied, each by symbol (CIP part 2 §5 note 2: no line numbers after B03a):
     | # | dependant | exact edit |
     |---|---|---|
     | 1 | `rosters.yaml: conditional_emission_rows`, whose one value is `"Record.ttl"` | delete the roster |
     | 2 | the exemption branch in the gate, `state/world.py` (`conditional = roster("conditional_emission_rows")` and the `and f"{record_kind}.{fieldname}" not in conditional` clause) | delete the comment block and the clause; the D22 refusal then applies to every MATTER row with a declared kind, which is H-12 as ruled |
     | 3 | `record.expired` in `EVENT_KINDS` | nothing to edit: it is derived from the matrix row and leaves with it (`data/verbs.py::derive_event_kinds`) |
     | 4 | `harness/probes.py` (the probe that writes `(Record, ttl)`), `loop/matter.py` (a comment citing the roster), `tests/test_season_shape.py` (`assert "Record.ttl" in roster("conditional_emission_rows")`) | delete the probe and the assertion; reword the comment to cite H-12 directly |
  3. `engine/season/hole_register.yaml`: H-86 closed as irrelevant, its `cite:` gaining this commit; H-259 closed by the lapse rule.
  4. The `comply` cell's conjunct is a typed `requires_typed` clause on the writ's stages, read through the existing stage reader `[ASSUMPTION: the conjunct's form — basis: the source names the condition, not its stem; the producer opens `issue`'s `_declared_stages` and MATTER's maturing and writes the conjunct on the stem they already use, or stops and names the missing stem]`.
- WHERE: `engine/season/state/carriers.py` (`Record.ttl`); `engine/season/write_matrix.yaml` (the `Record`/`ttl` row); `engine/season/verb_table.yaml` (`comply`'s cell); `engine/season/rosters.yaml` (`conditional_emission_rows`, deleted); `engine/season/state/world.py` (the emission gate's exemption clause); `engine/season/harness/probes.py` (the `(Record, ttl)` probe, deleted); `engine/season/loop/matter.py` (one comment); `engine/season/tests/test_season_shape.py` (one assertion deleted); `engine/season/hole_register.yaml` (H-86, H-259).
- TESTS: `test_season_shape.py`'s `Record.ttl` assertion deleted; new in `engine/season/tests/test_fi_small_edits.py`: `test_a_writ_stops_admitting_comply_after_its_last_stage` `[ASSUMPTION: test name; the item creates it]` (a hand-built world with a writ whose last stage matures within two seasons: `comply` admitted before, refused after; red before step 1's cell) and `test_a_declared_row_with_no_emission_still_raises_d22` (D2's gate: "a MATTER write on a declared row with `emits=None` still raises `Forbidden('… D22')`").
- FALSIFIER and CONTROL: D2's: "a second row needs the exemption; then item 2's deletion fails that row's MATTER write at the first season of `harness/populated.run(1, 0)`. (Checked statically: `(Site, condition)` declares two kinds and its writer names one on every write …)." A reader of `Record.ttl` the grep missed shows as an `AttributeError` at import. Control: the behaviour tallies (`corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's] seed 0's `DEGREES RESOLVED` and executed-verb tallies) equal to the previous item's reading except for `comply` on lapsed writs (D-04: an encoding mover's control is tallies-equal, never hash-equal).
- GATE: `python -m pytest engine/season/tests/test_season_shape.py engine/season/tests/test_fi_small_edits.py -q` → pass; `python -c "from engine.season.harness.populated import run; run(1, 0)"` (D2's `populated.run(1, 0)`) → completes; `git grep -n "conditional_emission_rows\|\.ttl\b" engine/season -- '*.py' '*.yaml'` → no hit naming the field (a comment citing H-12 kept); H-259's reading at two seasons, seeds 0 to 2 (eight seasons in the source; A-114): the writ stops admitting `comply` after its last stage wherever one matures, the count quoted, and the planted test above where none does; realm hash after one season at seed 0 → moved (field name in the encoding: `state/world.py::_object_head`, `_encode_into`).
- HASH MOVERS: encoding: `Record`'s field list enters `World.content_hash()` (D-04), every world with a Record; behaviour: `comply` on a lapsed writ. B11.99's re-pin, said "encoding and behaviour".
- DEPENDS ON: EXISTS-IN-TREE `state/carriers.py::Record` (`ttl`), `write_matrix.yaml` (`Record`, `ttl`), `rosters.yaml: conditional_emission_rows`, `state/world.py` (the exemption clause), `harness/probes.py` (the `(Record, ttl)` probe), `data/verbs.py::derive_event_kinds`, `verb_table.yaml` `comply`; `loop/effects_information.py::_declared_stages` (`:177`, `issue`'s stage winder; its body not opened by this lane).
- GLOSSARY: none (no term changes: a writ's lapse is already "its last stage maturing").
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B11's producer; `Item: B11.17`, `[skip ci]`.

### B11.18 — the knots oracle draws only from a seeded generator · `08_FI_04` §5, first bullet · BUILD · HASH EQUAL
- SOURCE: `proposals/08_FI_04_small-edits.md` §5, first bullet, and "Falsifiers" ("For §5's knots edit"); closes R-14 (part).
- ADVANCES: none of the nine; nothing is drawn unseeded (the oracle the port validates against, CLAUDE.md §7).
- INSTRUCTION, copied, by symbol: "**`systems/fieldwork/sim/knots.py`.** [the module docstring] *'Canon source: systems/fieldwork/reference/knots_v30.md'* → *'Intent (archived, not canon): knots_v30.md'*. [In `form_knot`]: delete the `random.Random()` fallback and raise when no `rng` is supplied (an unseeded draw in an oracle). `form_knot`: return `None` when `actor_a == actor_b`. The module-level registry stays: it is an unplugged oracle, and the season's knot is a Tenure."
- WHERE: `systems/fieldwork/sim/knots.py` (the module docstring; `form_knot`'s `rng` fallback and its first lines).
- TESTS: `engine/tests/test_knots_ed912.py` (exists; it passes `rng=random.Random(seed)`): unchanged and green; new in it, `test_form_knot_with_no_rng_raises` and `test_a_knot_with_oneself_is_none` `[ASSUMPTION: test names; the item creates them]`.
- FALSIFIER and CONTROL: "`engine/tests/test_knots_ed912.py` must still pass with an explicit `rng` (if it relied on the fallback, the test was drawing unseeded)." Control: realm hash after one season at seed 0 equal to the previous item's (the oracle is not in the season).
- GATE: `python -m pytest engine/tests/test_knots_ed912.py -q` → pass; realm hash (`HASH READING`) at seed 0, one season → equal.
- HASH MOVERS: none ("§5 moves none").
- DEPENDS ON: EXISTS-IN-TREE `systems/fieldwork/sim/knots.py::form_knot`, `engine/tests/test_knots_ed912.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `medium`.
- LANDS IT: B11's producer; `Item: B11.18`, `[skip ci]`.

### B11.19 — the `fieldwork` contract row says what is registered and what is unplugged · `08_FI_04` §5, third bullet · BUILD · HASH EQUAL
- SOURCE: `proposals/08_FI_04_small-edits.md` §5, third bullet; closes R-16.
- ADVANCES: none of the nine; a reader of the contract is told what the module is.
- INSTRUCTION, copied: "**`references/module_contracts.yaml`, the `fieldwork` module row**. Split what it describes: the registered entry `fieldwork.find` (typed in, typed out, no state) and, separately marked UNPLUGGED, the knots oracle's tracks and gates, so a reader of the contract is not told the module holds an Evidence Track." The row is the `- module: fieldwork` entry (its key, re-keyed from `fieldwork_knots` at v9 FI-02, unchanged); the composition row `fieldwork.find` is not edited.
- WHERE: `references/module_contracts.yaml` (the `fieldwork` module row).
- TESTS: none new; the covering readers are the tests `grep -rl module_contracts tests/valoria engine` names, run once.
- FALSIFIER and CONTROL: the export or a composition check reads a changed `fieldwork.find` row; the row still names an Evidence Track as held. Control: `engine/engine_params/composition.json` byte-identical.
- GATE: `python tools/export_composition.py --check` → exit 0; `git diff --stat -- engine/engine_params` → empty.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B03 (CI-03) and Batch B03g (GO-11), which edit the same file earlier; EXISTS-IN-TREE `references/module_contracts.yaml` (`fieldwork`, `fieldwork.find`), `tools/export_composition.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `medium`.
- LANDS IT: B11's producer; `Item: B11.19`, `[skip ci]`.

### B11.20 — the two unwritten FI ledger rows, and the handoff's pointer · `08_FI_04` §5, fourth bullet · BUILD · HASH EQUAL
- SOURCE: `proposals/08_FI_04_small-edits.md` §5, fourth bullet ("verified by grep; settled"); `registers/handoffs/HANDOFF_FI.md` (its rows naming ED-FI-0009 and ED-FI-0002 "NOT written"); closes R-17.
- ADVANCES: none of the nine; the ledger records what was built.
- INSTRUCTION, copied: "**`registers/editorial_ledger_fi.jsonl`.** Write the two rows `HANDOFF_FI.md` names as unwritten (ED-FI-0009's FI-01 build; ED-FI-0002's FI-02/FI-03 build) and correct the handoff's pointer: ED-FI-0002 lives in `registers/editorial_ledger_fi_archive.jsonl`." Each row is a superseding row of its existing id (`supersedes_row: true`), status `resolved`, its description the built state the handoff records (ED-FI-0009: "FI-01 BUILT `6d94d9d3`"; ED-FI-0002: "BUILT with FI-02 (B-O closed `90f80bfa`; landed `b3ddc693`, EXIT tests `8c85349f`)"), and its open residue named as the handoff names it; the frozen archive file is not edited (CLAUDE.md §3). `HANDOFF_FI.md`'s ED-FI-0002 pointer is re-pointed to the archive file and its "NOT written" clauses are removed.
- WHERE: `registers/editorial_ledger_fi.jsonl` (two appended rows); `registers/handoffs/HANDOFF_FI.md` (two rows' pointer and wording).
- TESTS: none new.
- FALSIFIER and CONTROL: a row with a new id (the ids exist); an edit to `registers/editorial_ledger_fi_archive.jsonl`. Control: `validate_ed_citations.py` exit 0 before and after.
- GATE: `python tools/validate_ed_citations.py` → exit 0; `python tools/currency_consistency_check.py` → exit 0; `git diff --stat -- registers/editorial_ledger_fi_archive.jsonl` → empty.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `registers/handoffs/HANDOFF_FI.md` (the ED-FI-0009 and ED-FI-0002 rows), `registers/editorial_ledger_fi.jsonl`, `registers/editorial_ledger_fi_archive.jsonl`.
- GLOSSARY: none.
- IDS: none new (rows for ED-FI-0009 and ED-FI-0002).
- COST and TIER: edit; `sonnet`, `medium`.
- LANDS IT: B11's producer; `Item: B11.20`, `[skip ci]`.

### B11.21 — the witness step imports nothing from `decision/` · `08_FI_04` §6 (D-74) · BUILD · HASH EQUAL
- SOURCE: `proposals/08_FI_04_small-edits.md` §6 ("Decided (D-74, taken B: fix the witness code, not Layer 1)"); closes R-26, audit §11 item 2 (code half).
- ADVANCES: none of the nine; `04` §A.2's `loop/witness` row holds for the code.
- INSTRUCTION, copied: "**the two `decision/` imports are removed from the code**. `loop/witness.py` imports `ledger_weigh` and `refracted_confidence` from `decision/options.py`; both functions move to `queries/person_q.py` (person-side, World-free arithmetic over a holder's own ledger and interior), `decision/options.py` re-imports them from there (`04` §C.3: `decision/` imports `person_q`), and `witness.py` imports them from `queries/person_q.py`, so it imports nothing from `decision/` `[ASSUMPTION: the target module; basis: the 'per-holder projection a `queries/` function builds' this section first named, and `04` §C.3's import rule]`. The three reads no refactor removes (the driver's `findings` store, older Events by id, the ledger id set) are listed for an amendment text to `04` §A.2's `loop/witness` row, drafted by the unification stage and applied only by Jordan; nothing in `04` is edited here." The three reads are named in the batch PR body's held-back list (Layer 1 text, `V12_STRUCTURE_part3.md` §8.2).
- WHERE: `engine/season/decision/options.py` (`ledger_weigh`, `refracted_confidence` moved out; one import added); `engine/season/queries/person_q.py` (the two functions, bodies unedited); `engine/season/loop/witness.py` (its import line); `engine/season/tests/test_fi_small_edits.py`.
- TESTS: "named test (new): `engine/season/tests/test_fi_small_edits.py::test_witness_imports_nothing_from_decision` (a source scan of `loop/witness.py`)", red before the edit.
- FALSIFIER and CONTROL: a moved function whose body changed (a diff of the bodies, moved byte for byte); `queries/person_q.py` importing `decision/`. Control: "the same content hash at seeds 0–2 before and after"; the `decision/` and `queries/person_q.py` path scan of `tests/test_season_shape.py` stays green (no `World` in scope).
- GATE: `python -m pytest engine/season/tests/test_fi_small_edits.py -k imports engine/season/tests/test_season_shape.py -q` → pass; realm hashes (`HASH READING`) after one season at seeds 0, 1, 2 → equal to the previous item's readings.
- HASH MOVERS: none ("§6's refactor none (gate)").
- DEPENDS ON: V12 B11.14 (the same file's deposit edits, in order); EXISTS-IN-TREE `decision/options.py::ledger_weigh` (`:1570`), `::refracted_confidence` (`:1671`), `loop/witness.py`'s `from ..decision.options import ledger_weigh, refracted_confidence`.
- GLOSSARY: none.
- COST and TIER: small build (a move); `sonnet`, `high`.
- LANDS IT: B11's producer; `Item: B11.21`, `[skip ci]`.

### B11.22 — a telling carries the hand that did the deed · `08_FI_06` edits 1–4, 6, 7 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/08_FI_06_testimony-names-a-hand.md` "The resolution, decided", "Edits, by owner" 1–4, 6, 7, "Gate", "Falsifier" (edit 5, the slant text, is FRES §6's and landed in B11.09); FRES §2 row 7 ("`08_FI_06`; then `16_PESSIMIST_FI_A` edit 4"); closes F-FI-11, R-36, R-38.
- ADVANCES: R-07; FI standalone; precondition of B24's `08_FI_05` and B25's CP-T06-05.
- INSTRUCTION, copied:
  1. "**`engine/season/state/carriers.py::Said`** gains one optional member, `pairing`, default `None`: the `Seen` value the teller pairs with the deed he is passing on (as he holds it, with whatever terms his channel showed). Keyword-only, so every existing construction is untouched. `Said` rides the Act's payload; no ledger carrier gains a field."
  2. "**`queries/person_q.py::said_of`.** The pool for `subject` becomes: the claims whose subject it is, **and** `attributed_deeds(claims, subject)` (the one owner of 'which of a holder's claims are about what this person did'). A witness asked about K can now say `(V, person.died, True)`. When the picked claim is of a `PAIRED_KINDS` kind and `deed_doer` over the teller's own ledger names a doer, the returned `Said` carries that sighting as `pairing`. A told deed the teller holds with a told pairing passes the same pairing on, so the hand survives a retelling."
  3. "**`loop/witness.py`, the told deposit.** After the told deed claim, where `_held.pairing` is not `None`, deposit one told `seen` claim on the same subject with the same `when`, `lap`, source and **chain**, through the same guard, refraction and credit. At `Partial` the copy withholds `who` (the lossy copy's own rule, and `rosters.yaml: finding_terms`' precedent: *a partial finding withholds the hand*), so a garbled report says that it happened and not who."
  4. "**`queries/person_q.py::_seen_index`** returns a third index, told sightings keyed by `(subject, when, lap, chain)`. **`deed_doer`** answers a told deed from that index and only from it: a told deed is paired with a sighting told on the same chain at the same deposit, never with the hearer's own sightings. The existing refusals stand unchanged (no `who`, two different `who`, a stratum the kind's rows do not carry). `attributed_deeds`, `suffered_deeds`, `deed_doers` and `paired_deed_term` drop their own `c.chain` exclusions for paired kinds and ask `deed_doer`; a told paired deed lands in `deeds_judged`'s `told` half, as every told deed does. `legitimacy`'s caveat is deleted with the limit."
  6. "**`engine/season/data/fixtures.py`:** `told_pairing`, `off` (control, today) / `on`; ships `on` when the gate reads." The flip is this item's last step, after the gate's `on` readings, in the same commit.
  7. "**`engine/season/hole_register.yaml`:** one row for the limit as measured (it has none), closed by this position." Its id from B11's H block, slot 1.
  "**Not built here, named.** Saying a *false* hand (the deed lie, H-198 rule (ii)) … is design-first …, so it is left out." (H-198 with M9 is a held MISSING-DEP entry of the intake.)
- WHERE: `engine/season/state/carriers.py` (`Said.pairing`); `engine/season/queries/person_q.py` (`said_of`, `_seen_index`, `deed_doer`, `attributed_deeds`, `suffered_deeds`, `deed_doers`, `paired_deed_term`, `legitimacy`'s docstring); `engine/season/loop/witness.py` (the told deposit); `engine/season/data/fixtures.py` (NEW `told_pairing`); `engine/season/hole_register.yaml` (one new row, closed); NEW `engine/season/tests/test_told_pairing.py`.
- TESTS: in the new file, written first and read red at `on` (no member): "`test_a_telling_carries_the_hand`, `test_a_retelling_keeps_the_chain`, `test_a_partial_telling_withholds_it`, `test_the_witness_asked_about_the_doer_says_the_death`, `test_off_arm_is_todays_reading_and_hash_equal`"; the falsifier's "`test_a_hearers_own_sighting_is_never_the_told_ones`" and "`::test_an_unpaired_telling_names_nobody`". The method is the `g6` tests' (`engine/season/tests/test_told_by_channel.py`: "Through the real fold and the real WITNESS barrier on a hand-built world").
- FALSIFIER and CONTROL: "A hearer who holds his **own** sighting of a different person acting on V in that lap must name that person from his firsthand claim and K from the told one, and never K from his own sighting. Planted failure: key the told index without the chain; that test must go red. A second: a told deed with no pairing (the teller's own pairing was ambiguous) must still name nobody." Control: "`off`: every reading above is today's (`()`, `None`), and `build_realm(0..2)` one-season hashes are equal to the base" `[ASSUMPTION: `Said` is not reached by `World.content_hash()` — basis: it rides the Act's payload, and the hash folds state collections and Event frames `(E, id, kind, emitted_at, degree, causes)`, `state/world.py::content_hash`'s docstring; the `off` arm's hash-equal reading observes it, and a moved `off` hash stops the item as an undeclared encoding mover]`.
- GATE: "W witnesses K kill V; W tells J; J tells L. `on`: `deed_doers(J.ledger, {kinds: [person.died]}, J)` and the same for L read `('K',)`; L's claims carry the chain `(W, J)`; `attributed_deeds(J.ledger, 'K')` yields the deed; J's `regard` for K moves by the `told` half. `on`, the telling at `Partial`: J holds the death and names nobody. W, asked about K, says the death (the `said` on his Act is `(V, person.died, True)` with a pairing). `off`: every reading above is today's": `python -m pytest engine/season/tests/test_told_pairing.py engine/season/tests/test_told_by_channel.py -q` → pass; realm hashes (`HASH READING`) at seeds 0 to 2, one season, `off` → equal to B11.21's readings; then, shipped `on`, at seed 0 → moved or equal (quoted: "in `build_realm` that is rare today (0 and 1 deaths by a hand in three seasons at seeds 0 and 1)").
- HASH MOVERS: "At `told_pairing: on` (declared); none at the control": every world where a paired deed is told. B11.99's re-pin.
- DEPENDS ON: V12 B11.09, B11.10, B11.21; EXISTS-IN-TREE `carriers.py::Said` (a `NamedTuple`), `person_q.py::said_of`, `::_seen_index`, `::deed_doer`, `::attributed_deeds`, `::suffered_deeds`, `::deed_doers`, `::paired_deed_term`, `::legitimacy`, `PAIRED_KINDS`.
- GLOSSARY: "pairing": the sighting of who did a deed that a teller passes on with the deed itself (plain English: the two go together); row added, owner `Said.pairing`.
- NAMES: the source's `round` (the `(subject, when, round, chain)` key, "the same `when`, `round`") → `lap` (B04, PCR-4: `Claim.round` → `Claim.lap`); "in that round" → "in that lap".
- IDS: H, block slot 1 (edit 7's row).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B11's producer; `Item: B11.22`, `[skip ci]`.

Last item written by this lane: B11.22. The second half (lane A17) continues from B11.51 and writes B11.99 and the boundary row `STOP. Batch B11-fi-readers closes here`.
