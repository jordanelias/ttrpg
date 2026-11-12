# 19 · LACUNA · 2 — A conclusion is a committed assertion, its support bound, the world answering later

## Status: PROPOSED (design-first in its value-space and `record` halves; the carrier edits are small)

Carries `audits/19_LACUNA_investigation_to_proceedings.md` §4.4 and resolutions R-19-03 to R-19-05. Builds
on `08_FI_03_playable-inquiry.md` §3 (which it amends at one point, below) and `08_FI_07_shortest-playable-case.md`
§1. Precedent: Lacuna's Case Sheet (DigiTales devlogs, 2020, page read: *"many channels out, few channels
back in"*; the Sheet *"does not ask how they arrived at the conclusion"*; single-shot; not told whether
right; wrong answers cascade). `D_T06.md:56` records the gap: *"No hypothesis carrier: a person cannot state
a conclusion the world later answers."*

## What this changes in `engine/season/` at runtime

`reconstruct` stops writing nothing (`verb_table.yaml`, `reconstruct.writes: []`; 47 / 45 / 54 folded acts
at `build_realm(0..2)` with zero product, `08_FI_03` problem). It utters a `Proposition` naming a doer and
opens the maker's `hold` (the body `_eff_utter` already has), carrying the ids the concluder cited as its
support. `commit` to it is an ordinary, existing act. A person who holds the concluder's Proposition and
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

**R-19-03 · The carrier.** A conclusion is the existing `Proposition` (mood `HOLDS`) plus one new optional
member, `support: tuple[str, ...] = ()` — the claim ids and Record ids the utterer cited, each refused at
the cell before the draw if he does not hold it (FI E-1's rule, reused). Immutable with the Proposition.
No case object, no truth flag, no verifier (2026-08-18 Q5 kept). Ladder step 4 (precedent: FI E-1's
`cites` operand; `_eff_utter`'s maker's hold).

**R-19-04 · The draws.** `reconstruct` is graded by `graded_inquiries` as now. Its band sets what the
Proposition can say:

| band | product |
|---|---|
| `Failure` | nothing uttered; the act is witnessed (others saw him puzzling), as today |
| `Partial` | a Proposition of the deed with no hand (`subject` the patient or Record, `value` the deed kind), `support` as cited |
| `Success` | the deed **and** the hand: the Proposition names the doer |
| `Overwhelming` | as `Success`, and the concluder's own claim of it is deposited at confidence 1 |

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

1. `engine/season/state/carriers.py::Proposition` — `support: tuple = ()` after `scope`, keyword-only in
   practice (every existing construction is positional up to `when` or keyword; `[UNVERIFIED]`: grep the
   constructions before landing; the frozen dataclass's `__eq__` changes for propositions that carry
   support, none today).
2. `engine/season/verb_table.yaml` `reconstruct` — `writes` keyed by band: `Failure: []`, `Partial` /
   `Success` / `Overwhelming`: `[Proposition.exists, Tenure.since]` (the maker's hold, as `utter`'s
   receipt rule names it); `emits`: `Failure: [finding.none]`, else `[proposition.uttered]`; `requires`
   unchanged (`own_ledger` of the subject); `cites` added to `rosters.yaml: choice_sourced` for this row.
   `writes_note` records that the act's product is a belief-bearing utterance, not a finding.
3. `engine/season/loop/effects_information.py` — `_eff_reconstruct` calls `_eff_utter`'s body (no second
   mint) with mood `HOLDS`, the band's cell, and `support` from `payload["cites"]`.
4. `engine/season/decision/options.py` — (a) `reconstruct` Candidate variants: one per doer named by
   `deed_doers(p.ledger, goal.object, p.id)` for a held case goal, each with `cites` = the claims that name
   him; (b) `record`: the `told` set gains `p`'s held `HOLDS` Propositions uttered by `teller`, mapped to
   their cell, behind fixture `record_concluders` (control `0`).
5. `08_FI_03_playable-inquiry.md` §3 (FI lane, text): replace *"Graded through the existing
   `graded_inquiries` route: `Failure` utters nothing; `Partial` utters it without the hand."* with *"Graded
   by `graded_inquiries` per `19_LACUNA_conclusion_is_a_committed_assertion.md` R-19-04; the choice among
   several named doers is the chooser's, sampled for an NPC; the support is bound on the Proposition."*
   Its last bullet (*"the design pass decides whether the same pairing scores the concluder"*) is answered
   by R-19-05.

## Gate (execution artifacts)

On `inquiry_world(seed)` (`08_FI_03` §1), seeds 0-19, four seasons, `PYTHONHASHSEED=0`:
- `reconstruct` deposits a Proposition in more than zero folded acts (today zero), every one carrying a
  non-empty `support` whose ids the utterer held at the act;
- across the 20 seeds, at least one conclusion names the Event's actor and at least one names someone else
  (`08_FI_03` §3's gate, kept);
- with a planted ledger naming two doers at support 0.9 and 0.3, an NPC concluder names the weaker in a
  share strictly between 0 and ½ over 200 seeds;
- `record_concluders` 1: a holder who later examines the scene and holds the firsthand contradiction reads
  `record(p, concluder) < 1.0`; at `0` it reads `1.0` (control).

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

Small build (carrier, row, effect); design-first for the Candidate scoring weights (CHAR's chooser) and
the `record` extension's sweep (CR-83). Lanes: FI (row, effect), CHAR (chooser, `record`), IN (carrier).
