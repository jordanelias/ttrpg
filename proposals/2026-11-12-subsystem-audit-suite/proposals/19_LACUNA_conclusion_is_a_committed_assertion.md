# 19 · LACUNA · 2 — A conclusion is a committed assertion, its support bound, the world answering later

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-22) — the graded `reconstruct` row does not write a Proposition: the loader refuses a band-keyed `writes:` with no `contests:`, and an inquiry takes no prize. It deposits the conclusion to its maker, and the committed assertion is his `utter` carrying `cites`, stored as `Proposition.support` (`U5c_FI_residue.md` §7). Edits 1 and 4 stand; the gates are read with "a Proposition uttered after a winning `reconstruct`". A lost draw states nothing (decision register D-45, taken A).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.6 row (VIOLATES edits 2–3; edits 1 and 4 CONFORM), §7, §7b-12, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-11i, ledger S-21; `unified/U1_GLOSSARY.md` *party*; `unified/U3_CONFLICT_LEDGER.md` C3-C16; `unified/U3_DEPENDENCY_ORDER.md` node B11). The body follows its head: **edits 2 and 3 are deleted** (`reconstruct`'s row keeps `writes: []` and its emissions are `U5c_FI_residue.md` §7's; `_eff_reconstruct` is not written; the loader refuses a band-keyed `writes:` with no `contests:`, `data/verbs.py:848-851`, `04` §B.13 invariant 12); R-19-04's band table now sets what the `concluded:` claim deposited to the maker shows, and the Proposition is uttered by his `utter` carrying `cites`; edit 5 is applied (by FRES §7) and marked so; edit 1's `[UNVERIFIED]` grep is done; `Proposition.support`'s departure from `04` §B.6/§B.9 is named (C3-C16); `graded_inquiries` → `graded_tasks`; "patient" → counterparty; named tests; lands-it and tier.

**Lands in batch:** B11 (`U5c_FI_residue.md` §2 row 10). **Depends on:** `U5c_FI_residue.md` (B11), `08_FI_03_playable-inquiry.md` (B11), `14_VERBS_SOCIAL2_B_a_word_with_content.md` §1 (B25; typed `utter`), B07 (`graded_tasks`).

## Status: PROPOSED (design-first in its value-space and `record` halves; the carrier edits are small)

Carries `audits/19_LACUNA_investigation_to_proceedings.md` §4.4 and resolutions R-19-03 to R-19-05. Builds
on `08_FI_03_playable-inquiry.md` §3 (which it amends at one point, below) and `08_FI_07_shortest-playable-case.md`
§1. Precedent: Lacuna's Case Sheet (DigiTales devlogs, 2020, page read: *"many channels out, few channels
back in"*; the Sheet *"does not ask how they arrived at the conclusion"*; single-shot; not told whether
right; wrong answers cascade). `D_T06.md:56` records the gap: *"No hypothesis carrier: a person cannot state
a conclusion the world later answers."*

## What this changes in `engine/season/` at runtime

`reconstruct` keeps `writes: []` (47 / 45 / 54 folded acts at `build_realm(0..2)` with zero product today,
`08_FI_03` problem) and gains a product by deposit: at WITNESS its maker receives a `concluded:` claim naming
the doer his own ledger names (`U5c_FI_residue.md` §7). The committed conclusion is his `utter` of that held
claim: a `Proposition` naming a doer, opening the maker's `hold` (the body `_eff_utter` already has), carrying
the ids the concluder cited as its `support`. `commit` to it is an ordinary, existing act. A person who holds the concluder's Proposition and
later holds a firsthand cell contradicting it re-grades the concluder in `record`. A declared hash mover in
every world where `reconstruct` folds; a control arm (`conclusion_product: off`) keeps today.

## The problem (evidence)

1. `reconstruct` has a value-space gap (K-37) and writes nothing; `utter` and `commit` exist and run
   (`verb_table.yaml`: `utter` writes `Proposition.exists`; `commit` requires *"the Proposition exists
   (immutable, §14)"*, writes `Tenure.since`, emits `commitment.made`; `release` closes it, emitting
   `commitment.ended`).
2. `state/carriers.py:969` `Proposition` has `id, mood, subject, predicate, value, when, scope`; nothing on
   it says why its utterer believes it, so a bench, a rival and the chronicle cannot read the reasoning.
3. `decision/options.py:1727-1767` `record(p, teller, fx)` pairs a teller's told cells against `p`'s
   firsthand cells; a concluder who has told nobody anything is never scored, however wrong his conclusion
   proves. `08_FI_03` §3 leaves this to *"the design pass"* and CR-83.
4. `08_FI_03` §3 grades `reconstruct` *"`Failure` utters nothing; `Partial` utters it without the hand"*,
   and leaves the choice among several named doers undecided.

## The resolution, decided

**R-19-03 · The carrier.** A conclusion is the existing `Proposition` (mood `HOLDS`), uttered by `utter`,
plus one new optional member, `support: tuple[str, ...] = ()` — the claim ids and Record ids the utterer cited, each refused at
the cell before the draw if he does not hold it (FI E-1's rule, reused). Immutable with the Proposition.
No case object, no truth flag, no verifier (2026-08-18 Q5 kept). Ladder step 4 (precedent: FI E-1's
`cites` operand; `_eff_utter`'s maker's hold).

**R-19-04 · The draws.** `reconstruct` is graded on the task route (`rosters.yaml: graded_tasks`, renamed from
`graded_inquiries` by 18-A, D-U1-11i). Its band sets what the `concluded:` claim deposited to its maker shows
(read off `rosters.yaml: finding_terms`), and so what his later `utter` can say:

| band | the deposited `concluded:` claim | what `utter` can then commit |
|---|---|---|
| `Failure` | none (`finding.none`); the act is witnessed (others saw him puzzling), as today | nothing |
| `Partial` | the deed with the hand withheld (`subject` the counterparty or Record) | a Proposition of the deed with no hand, `support` as cited |
| `Success` | the deed **and** the hand | a Proposition naming the doer |
| `Overwhelming` | as `Success`, at full confidence | as `Success` |

*Which* doer, when `person_q.deed_doers` over his own ledger names several, is the chooser's choice among
Candidate variants (one per named doer, each scored with its support over distinct origins,
`LedgerReader._support`). For an NPC the choice is sampled, so a less-supported suspect is sometimes named.
Nothing wrong is ever deposited by the roll (K-37 kept): a wrong conclusion comes from a wrong ledger (a
lie, a borrowed name, a drifted report) or from the chooser picking the weaker name.

**R-19-05 · The world answers later, through `record`.** The concluder is a teller of his own conclusion:
for a holder `p` of a `HOLDS` Proposition uttered by `u` (by WITNESS or by telling), the Proposition's
cell `(subject, predicate, value)` is paired in `record(p, u, fx)` exactly as a told cell is, against
`p`'s firsthand cells, by `_pair`. No second arithmetic, no new store. Ladder step 3: `08_FI_03` §3 names
this pairing as the design pass's choice and CR-83 as its home; step 5 decides it: a concluder who is not
paired is a teller with a free pass, which makes concluding costless.

**Irreversibility.** The Proposition cannot be withdrawn. The commitment can be `release`d; the release is
an Event others witness (`commitment.ended`), and every holder of both reads the concluder as having held
and abandoned it. What that costs in regard is `deeds_judged`'s, unchanged. This is Lacuna's *"no
takebacks"* translated: not a lock, a witnessed retreat.

**Who learns.** Those present at the utterance (WITNESS's existing deposit for `proposition.uttered`); then
whoever is told; and the whole room when the Proposition's support is cited before a bench
(`19_LACUNA_admission_rides_the_citing_draw.md`).

## Exact edits, by owner

1. `engine/season/state/carriers.py::Proposition` — `support: tuple = ()` after `scope`. Checked: the 13
   non-test constructions under `engine/season` (`grep -rn "Proposition(" --include=*.py`) are positional up
   to `when` or keyword, so a trailing defaulted member moves none; the frozen dataclass's `__eq__` changes
   only for propositions that carry support (none today). **Layer 1, named at the site:** `04` §B.6/§B.9 list
   no `support` on a Proposition; the member is a departure named in the docstring with its two readers
   (`record`, the board) under B4's third disposition, and `04` is not edited (C3-C16). `_eff_utter` stores it
   from the act's `cites`, and `cites` joins `rosters.yaml: choice_sourced` for `utter`.
2. **Deleted** (VIOLATES `04` §B.13 invariant 12; the loader refuses a band-keyed `writes:` with no
   `contests:` on a route row). `reconstruct` keeps `writes: []`; its emissions are `U5c_FI_residue.md` §7's
   (`conclusion.reached` at Partial and above, `finding.none` at Failure).
3. **Deleted.** `_eff_reconstruct` is not written; the Proposition is minted by `utter`'s own effect.
4. `engine/season/decision/options.py` — (a) `reconstruct` Candidate variants: one per doer named by
   `deed_doers(p.ledger, goal.object, p.id)` for a held case goal, each with `cites` = the claims that name
   him; (b) `record`: the `told` set gains `p`'s held `HOLDS` Propositions uttered by `teller`, mapped to
   their cell, behind fixture `record_concluders` (control `0`).
5. `08_FI_03_playable-inquiry.md` §3 (FI lane, text): **applied** (W3-2 rewrote that section to FRES §7's two
   acts, which carries this file's R-19-04 and the bound support); its last bullet's pairing question is
   answered here by R-19-05.

## Gate (execution artifacts)

On `inquiry_world(seed)` (`08_FI_03` §1), seeds 0-19, four seasons, `PYTHONHASHSEED=0`:
- a Proposition is uttered after a winning `reconstruct` in more than zero runs (today `reconstruct` deposits
  nothing), every one carrying a non-empty `support` whose ids the utterer held at the act;
- across the 20 seeds, at least one conclusion names the Event's actor and at least one names someone else
  (`08_FI_03` §3's gate, kept);
- with a planted ledger naming two doers at support 0.9 and 0.3, an NPC concluder names the weaker in a
  share strictly between 0 and ½ over 200 seeds;
- `record_concluders` 1: a holder who later examines the scene and holds the firsthand contradiction reads
  `record(p, concluder) < 1.0`; at `0` it reads `1.0` (control).

Named tests (new, `engine/season/tests/test_conclusion.py`): `test_a_conclusion_is_uttered_with_a_held_support`;
`test_some_conclusion_names_a_non_actor`; `test_an_npc_names_the_weaker_suspect_in_a_share_strictly_between_0_and_half`;
`test_record_re_grades_a_concluder_only_at_record_concluders_one`; `test_reconstruct_row_with_banded_writes_is_refused`
(planted, the import fails).

## Falsifiers

- If every conclusion names the true actor over 20 seeds, nothing can mislead and the wrong conclusion is
  still unrepresented.
- If `support` ever carries an id the utterer did not hold at the act, the refusal is not wired.
- If `record` moves for a concluder whose Proposition the holder never held, the pairing reads a ledger it
  may not.

## NERS reading

- **N**: without it an investigation has no outcome (the scale reads `in_loop: False` in the requirements
  file, `08_FI_03`), and proceedings receive accusations from nowhere. Top-down a detective game is a
  conclusion; bottom-up `utter`, `commit`, `hold`, `_pair` exist; lateral a concluder is a teller; diagonal
  the support is what the bench weighs.
- **R**: which suspect, on which support, and when (concluding early on thin support versus waiting while
  the forger acts); without a player, NPC investigators conclude wrongly and are found out by others.
  Complete at its extremes: an empty ledger cannot conclude; a single named doer is a forced choice.
- **S**: one mint, one pairing rule, one roll owner; the conclusion enters proceedings as an ordinary held
  Proposition.
- **E**, last: one field, one row's writes, one Candidate family, one pairing extension, against a scale
  with no product.

## Cost class

Small build (carrier, `utter`'s `cites`); design-first for the Candidate scoring weights (CHAR's chooser) and
the `record` extension's sweep (CR-83). Lanes: FI (deposit), CHAR (chooser, `record`), IN (carrier).

**Lands it and tier.** The B11 batch, after FRES §7, an FI `valoria-author` session on `sonnet` (`high`); the
design read for edit 4's weights on `opus`; one `methodology-close`. **Hash movers.** Wherever `reconstruct`
folds and its maker utters (declared); `record_concluders` 0 is the control.
