# 14 · VERBS · SOCIAL2 · C — a case with a charge, a speech that enters by degree, a question the questioned answers, a confession on file, a telling whose odds the hearer sets

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-12, C-21, C-29) — §2's `speak` bands yield to `19_LACUNA_admission_rides_the_citing_draw.md` (entry) and `05_SC_evidence_and_rebuttal_B.md` (answer). §3 owns the `interview` row, over `13_SC_draw_for_unrolled_contests.md`'s; `19_LACUNA_questioning_has_an_approach_and_a_cost.md` supplies `approach` as levels. The tables `tell_obstacle`, `interview_obstacle` and `interrogate_obstacle` are folded into the one roster (`U5c_SC_one_obstacle_form.md` §2); a tie is a `favour` level and custody is the `custody` source (§3 there).

## Status: PROPOSED

Carries `audits/14_VERBS_SOCIAL2.md` §3 (`open_case` content), §5 (`speak` bands and evidence), §6
(`tell` odds), §7 (`interview` prompt), §8 (`interrogate`). Batch S2-C. Depends on S2-A, on CR-61 (the
docket item names its case file), on FI-02 edit 5 (`present_persons`) and FI-06 (`said_of`'s widened
pool), and on the SC lane's carriers (SC-P3B's hearing; the case file's stages).

**Designed to the standing rule** (`AUDIT_BRIEF.md`, Jordan 2026-11-12: *"we do not do
deterministic"*): every outcome here that could go either way for the people in the fiction is a draw
whose odds come from the evidence held and cited, the actor's capability and the venue. Where the cited
SC and FI documents state a fixed rule (SC-P8 edit 3: *an answer STANDS when it contradicts*; edit 2:
*entered at Success*; FI-05B E-6), this proposal reads it as a modifier on a draw and grades the result.
SC-P8 is being corrected by another lane; this proposal is written to the draw and does not wait for
that correction's text.

## What this changes in `engine/season/` at runtime

An `open_case` case file carries the party, the opener's charge and (when the SC lane lands it) the
arrangement. A `speak` that cites held items moves its own odds by them and enters them on the case file
at a weight graded by its band; an answering `speak` may strike or weaken an entered item by its own
draw. An `interview` is a draw for the subject's engagement and, when it engages, raises a question the
interviewee answers by his own `tell` or `lie`. An `interrogate` at a winning band enters a confession on
the case file at a graded weight. A `tell` always draws, at odds the hearer's believed position sets.
Fixtures at their controls reproduce today; declared hash movers wherever these verbs execute.

## The problem (evidence)

`audits/14_VERBS_SOCIAL2.md` §0.3: the case file is kind `text` with no content
(`loop/effects_information.py:436`); `speak` writes `[]` at every band (`H-63`) and the room reads
nothing from it but the hearers' ledgers; `interview` is ungraded and its `finding.made` finds nothing
(`rosters.yaml:3295`); `interrogate` writes `[]` at every band (`H-226`); `tell` succeeds 2 / 1 / 0 times
a season at seeds 0 / 1 / 2 (FI-02's table; probe). `corpus_run` lists `speak`, `interview`,
`interrogate` as emitting and writing nothing.

## The resolution, decided

One carrier (the case file, a `Record`), one mechanism (the existing contested route: pool, obstacle as
difficulty plus modifiers, the four-band ladder), and one deposit channel (WITNESS's told deposit, gated
by band). No verifier, no item that decides a case. Ladder: step 3 (FI-05B and SC-P8 for the carriers,
CP-T06-05 for the interview), step 1 (the standing rule supersedes their fixed rules), step 5 for the
odds tables.

## Exact edits, by owner

### §1 `open_case`: the case file carries the charge

- `rosters.yaml: record_kinds`: new kind `case: [terms, charge, arrangement]`; `person_q.ABOUT_KEYS`
  gains `case: terms` (the one owner of "what a document is about", so `_req_interrogate` clause 3 and
  `ledger_names` read a case file with no new code path).
- `verb_table.yaml` `open_case`: `requires_typed` gains `{form: own_ledger, of: subject, conjunct:
  charge}` (named, so the Candidate carries `said`: the opener's own claim about the party, by
  `person_q.said_of` with FI-06's pool, which prefers his attributed deeds). Refusal key `charge:
  [case.refused]`.
- `_eff_open_case`: mint kind `case` with content `{terms: matter, charge: <said as a dict>, arrangement:
  <payload or None>}` instead of `text` with none; the docket item names the case file (CR-61's key).
  Opening is a remit act and is not drawn: whether the case is won is `determine`'s draw.

### §2 `speak`: evidence sets the odds, the band sets what enters

- `verb_table.yaml` `speak`: `writes:` Ov / Su / Pa `[Record.stages]`, Fa `[Record.stages]` (the
  disclosure stage); `emits` unchanged (the four `matter.*` kinds). `writes_note` replaced: *the case
  file records each sitting's band and what entered at what weight*.
- The operand `cites` (FI-05B E-1, unchanged: ids of held claims or held Records, refused before the
  draw if not held).
- **Odds.** `seam/wrappers/sigma.py::contest_input`: the room term `proofs` is the sum, over cited items
  whose kind the arrangement row admits, of `rosters.yaml: proof_obstacle_step[kind]` × the item's
  weight by remove (FI-05B's table; `teller_weight`'s hop discount, the one owner), applied as an
  obstacle modifier in the speaker's favour; plus, for each item already entered on the case file for
  the other side, the same against him. No item adds an outcome; each moves the obstacle.
- **Entry.** New `_eff_speak(w, a, res)`: appends to the case file one band stage `(tick, "band:<degree>",
  a.id)` and, per cited item, `(tick, "proof:<kind>", ref, weight × band_entry[degree], a.id)` with
  `rosters.yaml: band_entry: {Overwhelming: 1.0, Success: 1.0, Partial: 0.5, Failure: 0.0}`. At Failure
  only a `(tick, "disclosed", refs, a.id)` stage: the room heard what he cited and did not credit it.
- **Answering.** An answering `speak` carries `answers: [<stage index>]` (SC-P8 edit 3's operand). Each
  answered stage whose item the answering citation contradicts (one owner of *pairs and disagrees*,
  `decision.agreement`) is a modifier in the answerer's favour of `proof_obstacle_step` × the answering
  item's weight. By the answerer's band: Ov / Su append `(tick, "struck", idx, a.id)` (weight 0);
  Pa append `(tick, "weakened", idx, a.id)` (weight halved); Fa append `(tick, "answer_failed", idx,
  a.id)`, and the failed answer is itself an entered item against the answerer at half weight. A
  non-contradicting answer adds no modifier and still draws (a bare denial can succeed; it is harder).
- **Counting** is `world_q.hearing`'s (SC-P8 edit 4): the sum of standing weights, which `determine`
  reads as an obstacle modifier — odds, never the verdict.
- Fixtures: `band_entry` (the table above; control: all 0, today), `proof_obstacle_step` (control 0).

### §3 `interview`: a draw to engage, then the questioned answers by his own act

- `verb_table.yaml` `interview`: `contests: "a standing"`; `counterparty: subject`; `writes:` `[]` at
  every band (the product is a deposit and a question; no world cell moves); `emits:` Ov
  `[interview.asked, interview.pressed]`, Su `[interview.asked]`, Pa `[interview.asked,
  interview.disclosed]`, Fa `[interview.declined]`; `emits_on_refusal: {present: [interview.refused]}`.
  `finding.made` / `finding.none` leave the row (the inquiry roster's `finding.made` row then claims only
  graded inquiries).
- `rosters.yaml: verb_capability`: `interview: "inquiry"`; `contest_subsystems.prizes`: `a standing` is
  already routed. Obstacle: `obstacle_default` plus `rosters.yaml: interview_obstacle` (rank gap per
  rung; the subject's `regard` of the asker below zero +1; a `tie` −1).
- `rosters.yaml: question_sources`: new source `asked` (ordered after `claim_landed`, before `need` —
  a person asked a question attends to it; `attention_key` reads the order).
- `queries/world_q.py::questions_for`: for each `interview.asked` claim in the person's own ledger
  deposited this tick, one Question `q:asked:<claim id>`, source `asked`, plain referents `(on,)`, about
  the claim. The topic `on` is the interview act's operand: the subject of the asker's question's `about`
  claim, else the interviewee (derived in `_derive_operand`, no free choice).
- `decision/options.py::operand_bags`: on a Question of source `asked`, the `to` fan of `tell` and `lie`
  is the asker alone (read from the `about` claim's value, own ledger). The interviewee's chooser forms
  `tell`, `lie` or neither; his answer is that verb's own draw. At `interview.pressed` the answering act's
  obstacle carries `rosters.yaml: interview_obstacle.pressed` (−1) for this tick only (read off the
  claim, not held state).
- `loop/witness.py`: no edit. `interview.asked`, `interview.pressed` and `interview.disclosed` deposit on
  those present like any Event (the interviewee among them, by the `with` conjunct); at
  `interview.disclosed` the deposit also names the asker's own question's `about` claim, so the
  interviewee learns why he was asked.

### §4 `tell`: the odds the hearer sets

- `rosters.yaml`: new `tell_obstacle` table read by `sigma.py::contest_input` for the `a standing` prize
  when the verb is a telling row (keyed by row column `telling: true`, not by name): `unopposed: 1`;
  `contrary_believed: <obstacle_default>` (the teller's own ledger holds the hearer as believing the
  contrary on the cell); `tie: -1`; `rank_gap_per_rung: +1`; venue modifier from `venues.yaml` where the
  SC lane lands one. FI-02 edit 6 is answered by this table: an ordinary telling to a friend is likely,
  never certain.
- Fixture `tell_obstacle` (control: `obstacle_default` everywhere, today).

### §5 `interrogate`: a confession on file, by degree

- `verb_table.yaml` `interrogate`: `writes:` Ov / Su / Pa `[Record.stages]`, Fa `[]`; emits unchanged.
- `loop/predicates.py::_req_interrogate` clause 3: the charge may be the docket item's petition **or its
  case file**, both through `ABOUT_KEYS` (one owner); no other change.
- New `_eff_interrogate(w, a, res)`: appends `(tick, "proof:confession", <event id>, weight, a.id)` to
  the matter's case file, weight `band_entry[degree]` (Ov / Su 1.0, Pa 0.5). Closes `H-226` by route (b)
  for this row: the fold runs the effect because the band now writes.
- Odds: `sigma.py::contest_input` for this row adds the standing weight of items already on the case
  file against the prisoner (in the interrogator's favour) and `rosters.yaml: interrogate_obstacle.
  custody_per_season` (−1 per season held, floor at the roster's minimum) — custody wears a man down,
  and still he may withhold.
- `rosters.yaml: verb_capability`: `interrogate: "inquiry"`.

## Order of landing

§1 (after CR-61) → §5 (reads §1's kind) → §2 (after SC-P3B's carriers) → §4 (independent) → §3 (after
FI-02 edit 5 and S2-A edit 5).

## Gate (execution artifact)

On FI-03 §1's `inquiry_world` and SC-P3's `build_hearing` world, extended as FI-05B's gate is (one forged
Record, one examiner), seeds 0–9, `PYTHONHASHSEED=0`:
- §1: every case file has `charge` equal to a claim its opener held at the act.
- §2: with cited items the speaker's success rate rises against the same world with `cites` empty (a
  control on the same seeds; the difference is the evidence's effect on the odds); all four bands occur
  across seeds; at Pa the entered weight is half; an answering `speak` with a contradicting item strikes
  more often than one without, and neither always.
- §3: across seeds the interviewee forms `tell` or `lie` to the asker in the interview's tick at ≥ 1 seed,
  and `interview.declined` occurs at ≥ 1 seed; the asker then holds the answer with the interviewee on its
  chain.
- §4: in `build_realm(0..2)` one season, `news.told` / (`news.told` + `news.untold`) rises above the
  baseline (2/6, 1/13, 0/2) and stays below 1.
- §5: with one planted `detain` and a case file, `interrogate` executes; at planted `Success` one
  `proof:confession` stage at weight 1.0, at planted `Partial` at 0.5, at planted `Failure` none.
- Control: every fixture at its control reproduces the pre-edit content hash.

## Falsifiers

- If any band outcome above occurs at every seed of ten under the shipped odds (or never), the odds are
  degenerate: the standing rule is not met, whatever the code says.
- An answer citing an item with the same value adds no modifier; if it strikes more often than a bare
  denial, the contradiction read is wrong.
- A cited item the speaker does not hold is refused before the draw.
- If any step reads a ledger other than the actor's own, the case file is not carrying the `Said`.

## NERS reading

N: the hearing, the inquiry and the custody room are where the detective precedent lives (L.A. Noire's
cited item, Ace Attorney's contradiction); without these edits they are rolls with nothing on file. R:
what to cite, what to answer, whom to question, whether to lie when asked; with no player, NPCs build
and break cases. S: one carrier, one ladder, the told channel; evidence enters as odds exactly as every
other modifier does, so the hearing's arithmetic is the contest's. E, last: one record kind, three
effects that append stages, four small odds tables, against three verbs that today write nothing.

## Cost class

Small build each; §2 design-first only for the `proof_obstacle_step` values (a sweep, not a ruling).
