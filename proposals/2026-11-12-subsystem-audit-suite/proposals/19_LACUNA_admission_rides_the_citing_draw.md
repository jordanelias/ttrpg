# 19 · LACUNA · 1 — Admission rides the citing act's draw (the FI/SC conflict on entering evidence, decided)

## Status: PROPOSED

Carries `audits/19_LACUNA_investigation_to_proceedings.md` §5 and resolution R-19-02. Decides between
`08_FI_05_evidence-interface_B.md` E-2 and `05_SC_evidence_and_rebuttal_B.md` "The three operations"
(row **file**) by the standing rule (`AUDIT_BRIEF.md`, "we do not do deterministic"). Edits only those two
files' text (owned by the FI and SC lanes); no code is made to read `.designs/` or `.audit/`.

## What this changes in `engine/season/` at runtime

Nothing until SC's consumer is built (`05_SC_evidence_and_rebuttal_B.md` edit 4). Once built, it changes
which offered items reach the case file: with `cites` empty (the control) nothing moves; with citing on,
an item offered by a `speak` that grades `Failure` is recorded as excluded and does not enter `proofs`, and
one offered at `Partial` enters at half weight. No new roll: the band is the one the `speak` already draws.

## The problem (evidence)

The two files that build one interface disagree on one point:

| | `08_FI_05_evidence-interface_B.md` E-2 | `05_SC_evidence_and_rebuttal_B.md`, row **file** |
|---|---|---|
| when an offered item enters the case file | "When a `speak` that cites grades `Success` or better, the host appends one stage per cited item" | "a `speak` on a docketed matter carrying `cites` (the filing act; **any band**) … one `filed` stage per held, admitted item"; "Filing is bookkeeping … recorded without a roll" |
| draw? | yes (the speech's own band), but binary: Partial enters nothing | no |

SC's reading treats putting an item before the bench as an eligibility (he holds it; the row admits its
kind). The brief's carve-out is eligibility *"whether an act may be attempted at all"*. Whether the bench
receives an exhibit is not that: the act (the speech that offers it) has been attempted; whether the room
takes the paper is something that, for the people in the fiction, could go either way (benches refuse
exhibits, a witness is cut off, the paper is waved away). By the rule's own test, *"When in doubt, draw."*
FI's reading is a draw but wastes the `Partial` band, which the ladder exists to make recoverable.

## The resolution, decided

**Admission is read off the citing `speak`'s own band; no second roll; four results.** Ladder step 5
(what makes sense for the architecture), after steps 1-4 are silent (no ruling decides admission; the
proceedings design `04_VERBS.md` §B.1 gives `speak` four bands and no admission rule; the precedent in the
tree is `tell`, whose told deposit is graded by the telling's band at WITNESS):

| the citing `speak` grades | each cited, held, kind-admitted item | stage written to the case file | the told copy to the room (FI E-3) |
|---|---|---|---|
| `Failure` | **excluded**: does not count in `proofs` / `rebuttals` | `(tick, "excluded", side, Said or record id, act id)` | **still deposited**, through the told channel's own grading: the room heard it said even though the bench did not take it |
| `Partial` | **entered contested**, at half its derived weight | `(tick, "filed", side, rung, Said or record id, weight × ½, origin, act id)` | deposited |
| `Success` | **entered** at its derived weight | `filed`, full weight | deposited |
| `Overwhelming` | **entered**, full weight, and **marked first-heard** (the answering act's obstacle reads `answer_ob + 1` against it) | `filed`, full weight, `first: True` | deposited |

Unheld ids and kinds the arrangement's `proofs:` does not admit are refused before the draw (FI E-1;
eligibility, unchanged). An `excluded` stage is bookkeeping of what happened and is the record an appeal
cites (`19_LACUNA_verdict_ladder_and_reversal.md`: "an item wrongly excluded" is a ground).

The `Overwhelming` cell is the one invented number: `+1` on the answer's obstacle, a NUMBER row in
`fixtures` (`first_heard_ob`, proposed 1, three-point sweep 0 / 1 / 2, control 0). It gives the top band a
reason to exist in the room without making any item unanswerable (an answer at its own `Success` still
strikes it).

## Exact edits, by owner (text edits to the owning lanes' proposals; then the code those proposals name)

1. **`proposals/2026-11-12-subsystem-audit-suite/proposals/05_SC_evidence_and_rebuttal_B.md`** (SC lane):
   - In "Where this differs from FI's E-6, and why", replace the sentence *"Putting a held item on the case
     file is an act the citer may attempt (an eligibility: he holds it, the row admits its kind) and is
     recorded without a roll;"* with: *"Offering a held item is an act the citer may attempt (an
     eligibility: he holds it, the row admits its kind); whether the bench enters it is read off the
     citing `speak`'s own band (`19_LACUNA_admission_rides_the_citing_draw.md`): `Failure` excluded,
     `Partial` entered at half weight, `Success` entered, `Overwhelming` entered and first-heard;"*.
   - In "The three operations", row **file**, replace *"(the filing act; any band)"* with *"(the filing
     act; its band decides admission, per `19_LACUNA_admission_rides_the_citing_draw.md`)"* and *"one
     `filed` stage per held, admitted item"* with *"one `filed` or `excluded` stage per held, admitted
     item"*.
   - In "Exact edits" item 4, after *"writes `filed` stages for its admitted cites"* add *"(by band, as
     the admission table in `19_LACUNA_admission_rides_the_citing_draw.md`)"*.
   - Gate 1 gains: *"over 200 seeds the accuser's filing `speak` grades every band; `excluded` stages
     occur at `Failure` and only there, and `proofs` at close equals the sum of the band-scaled weights."*
   - The line *"`present` stays draw-free as filing"* is unchanged: presenting an entered item in a
     sitting is a move in the module, and its board effect is SC's.
2. **`proposals/2026-11-12-subsystem-audit-suite/proposals/08_FI_05_evidence-interface_B.md`** (FI lane),
   E-2: replace *"When a `speak` that cites grades `Success` or better, the host appends one stage per cited
   item to the matter's case file"* with *"When a `speak` cites, the host appends one stage per cited item
   to the matter's case file, keyed by the speech's band: `excluded` at `Failure`, `filed` at half weight at
   `Partial`, `filed` at `Success` and `Overwhelming` (the last marked first-heard)
   (`19_LACUNA_admission_rides_the_citing_draw.md`)."* E-3 gains: *"The told deposit fires at every band
   the told channel deposits at, whether or not the item was entered."*
3. **Code, when SC builds it** (`engine/season/loop/effects_information.py`, the `speak` effect under its
   own token, SC `_B` edit 4): a per-band dispatch over the cited ids; `speak.writes` in
   `engine/season/verb_table.yaml` gains `Record.stages` at **all four** bands (today `[]` at every band,
   H-63), since `Failure` writes the `excluded` stage. `engine/season/data/fixtures.py`: `first_heard_ob`.
4. `modules/social_contest/evidence.py::Exhibit` (SC `_B` edit 3) gains `first: bool`; `standing` reads it
   only to hand the answer's obstacle term to the host (it rolls nothing, as now).

## Gate (execution artifact)

On `build_hearing(seed)` (`05_SC_playable_hearing_B.md` edit 9) with one accuser holding two firsthand deed
claims and a Record, `PYTHONHASHSEED=0`, seeds 0-199:
- all four bands of the filing `speak` occur; per band, the case file's new stages match the table
  (excluded at `Failure` only; weight halved at `Partial` only; `first` at `Overwhelming` only);
- at close, `proofs` equals the band-scaled sum, read off `Margin.terms`;
- every judge holds the told copies in every run where the told channel deposits, including the
  `Failure` runs;
- the share of runs in which the matter is determined against the accused is strictly between the
  shares with nothing filed and with every item force-entered at full weight (the admission draw is
  load-bearing in both directions).
Control: `cites` empty reproduces the base content hash.

## Falsifier

If any excluded item changes `proofs`, the band dispatch is wrong. If `Partial` and `Success` give the same
`proofs`, the half-weight cell is not read. If no `Failure` run carries a told copy, E-3 has been tied to
admission and the room is pretending not to have heard.

## NERS reading

- **N**: without it either an exhibit is certain once offered (a deterministic entry the standing rule
  forbids) or the `Partial` band does nothing in the room. Top-down a hearing admits and refuses; bottom-up
  the band already exists; lateral it is the told deposit's grading rule applied to the case file; diagonal
  an exclusion becomes an appeal's ground.
- **R**: a strong speaker gets his evidence in; a weak one may see it excluded and must find a second
  origin or a better advocate. No player needed: an NPC accuser's item is excluded and the bench hears his
  rival's.
- **S**: no second roll; the one band; the excluded stage is the same carrier as the filed one.
- **E**, last: one table keyed on the band already drawn, against two files that each got half of it.

## Cost class

Edit (two proposal texts), then a small build inside SC's consumer. Lanes: SC (owner of the consumer), FI
(E-2/E-3 text).
