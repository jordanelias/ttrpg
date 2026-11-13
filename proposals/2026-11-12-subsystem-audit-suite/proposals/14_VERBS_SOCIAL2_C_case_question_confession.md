# 14 · VERBS · SOCIAL2 · C — a case with a charge, a speech that enters by degree, a question the questioned answers, a confession on file, a telling whose odds the hearer sets

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-12, C-21, C-29) — §2's `speak` bands yield to `19_LACUNA_admission_rides_the_citing_draw.md` (entry) and `05_SC_evidence_and_rebuttal_B.md` (answer). §3 owns the `interview` row, over `13_SC_draw_for_unrolled_contests.md`'s; `19_LACUNA_questioning_has_an_approach_and_a_cost.md` supplies `approach` as levels. The tables `tell_obstacle`, `interview_obstacle` and `interrogate_obstacle` are folded into the one roster (`U5c_SC_one_obstacle_form.md` §2); a tie is a `favour` level and custody is the `custody` source (§3 there).
Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head applied to the body (`unified/work/R4_READ.md` §1.6, §2, 7b.6): `band_entry` is deleted and `task_fraction` read (C-23, U1 D-U1-11l: the values were identical); the `tell_obstacle`, `interview_obstacle` and `interrogate_obstacle` tables are deleted and their entries become OBS members or leverage sources (C-21; `unified/U3_CONFLICT_LEDGER.md` C3-C10: what favours the roller is a level — `custody`, `favour`, `proofs`, `approach` — never an obstacle subtraction); `proof_obstacle_step` becomes OBS §3's `proof_level` (`proof_step` deleted); `obstacle_default` (deleted, C-04) becomes the composer's stand-in; A-63/A-64 (C3-C13: `interview` occupies the interviewee; `speak` is a sitting, not a visit); A-81, A-30, U3 batch B25 and C3-Y10, R4 7b.0 block. A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (1); "trained score/rank" → skill score (3); "talent" → attribute or governing attribute (1).

## Status: PROPOSED

Lands in batch: B25 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), co-landing with `_SOCIAL2_A` and `_B` (C3-Y10: this file adds its kinds before S2_A's kind lists commit).
Depends on: `05_SC_evidence_and_rebuttal_B.md` and `05_SC_playable_hearing_B.md` (B24); `19_LACUNA_admission_rides_the_citing_draw.md`, `19_LACUNA_questioning_has_an_approach_and_a_cost.md` (the `approach` source); `08_FI_02_rumour-that-travels.md` edit 5 and `08_FI_06_testimony-names-a-hand.md` (B11); `14_VERBS_SOCIAL2_A` (B25); `U5c_SC_one_obstacle_form.md` §2–§3 (B05; `dissent` lands with `_SOCIAL2_B`); `18_DETERMINISM_task_draw_for_uncontested_verbs.md` item 2 (B07: `task_fraction`).
Lane: SC. Tier (R4 7b.0 (1)): `sonnet` producer, effort `high`; §2's and §3's draws `opus`; one `opus` read of the ten-seed band tables. Test file: `engine/season/tests/test_vm_s2_c_case.py` (one function per gate line).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the actor's skill score (A-6); the governing attribute as levels (A-7); a wound a level against the roll (A-8); the opposition is the counterparty's skill score through `opposed_ob` (A-79, D-U1-02). Draws: `H(w.world_seed, w.tick, <actor id>, "<verb>.<prize>")` for `speak`, `interview`, `interrogate`, `tell` (A-30). An `interview` debits the interviewee's scene for the round (A-63); precedence by rung, appointments and the waiting petition are `28_CORE_scene_access_A`–`C`'s (A-64; C3-C13); `speak` is a sitting, not a visit. **A-81:** `speak`'s Failure writes the `disclosed` stage; `interview.declined` is deposited to both parties; `interrogate`'s Failure is witnessed by the prisoner and the interrogator (a claim of the Event to each).

Carries `audits/14_VERBS_SOCIAL2.md` §3 (`open_case` content), §5 (`speak` bands and evidence), §6
(`tell` odds), §7 (`interview` prompt), §8 (`interrogate`). Batch S2-C. Depends on S2-A, on CR-61 (the
docket item names its case file), on FI-02 edit 5 (`present_persons`) and FI-06 (`said_of`'s widened
pool), and on the SC lane's carriers (SC-P3B's hearing; the case file's stages).

**Designed to the standing rule** (`AUDIT_BRIEF.md`, Jordan 2026-11-12: *"we do not do
deterministic"*): every outcome here that could go either way for the people in the fiction is a draw
whose odds come from the evidence held and cited, the actor's skill and the venue. Where the cited
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
*(Head line: §2's entry yields to `19_LACUNA_admission_rides_the_citing_draw.md` and its answer to
`05_SC_evidence_and_rebuttal_B.md`; where the bullets below and those files differ, those files govern.)*

- **Odds.** `seam/wrappers/sigma.py`: cited items whose kind the arrangement row admits enter as the
  `proofs` leverage source (OBS §3), one `proof_level` per whole unit of weight standing for the speaker's
  side, the weight by remove from FI-05B's table (`teller_weight`'s hop discount, the one owner); items
  already entered on the case file for the other side are the same source's defender levels. *(W3-4a,
  C-01/C3-C10: not an obstacle modifier; `proof_obstacle_step` is not added — the level unit is
  `proof_level`.)* No item adds an outcome; each moves the odds.
- **Entry.** New `_eff_speak(w, a, res)`: appends to the case file one band stage `(tick, "band:<degree>",
  a.id)` and, per cited item, `(tick, "proof:<kind>", ref, weight × task_fraction[degree], a.id)`, reading
  the one share table `rosters.yaml: task_fraction` (1 / 1 / 0.5 / 0; W3-4a: `band_entry` held the same
  values under a second name and is deleted, C-23). At Failure only a `(tick, "disclosed", refs, a.id)`
  stage: the room heard what he cited and did not credit it.
- **Answering.** An answering `speak` carries `answers: [<stage index>]` (SC-P8 edit 3's operand). Each
  answered stage whose item the answering citation contradicts (one owner of *pairs and disagrees*,
  `decision.agreement`) gives the answerer `proofs` levels for the answering item's weight. By the answerer's band: Ov / Su append `(tick, "struck", idx, a.id)` (weight 0);
  Pa append `(tick, "weakened", idx, a.id)` (weight halved); Fa append `(tick, "answer_failed", idx,
  a.id)`, and the failed answer is itself an entered item against the answerer at half weight. A
  non-contradicting answer adds no modifier and still draws (a bare denial can succeed; it is harder).
- **Counting** is `world_q.hearing`'s (SC-P8 edit 4): the sum of standing weights, which `determine`
  reads as an obstacle modifier — odds, never the verdict.
- Fixtures: none of this file's own; `proof_level` is OBS §3's (control `None`, today), and the entry
  share is `task_fraction` (its control arm for this reader: entry off, `0` at every band, today).

### §3 `interview`: a draw to engage, then the questioned answers by his own act

- `verb_table.yaml` `interview`: `contests: "a standing"`; `counterparty: subject`; `writes:` `[]` at
  every band (the product is a deposit and a question; no world cell moves); `emits:` Ov
  `[interview.asked, interview.pressed]`, Su `[interview.asked]`, Pa `[interview.asked,
  interview.disclosed]`, Fa `[interview.declined]`; `emits_on_refusal: {present: [interview.refused]}`.
  `finding.made` / `finding.none` leave the row (the inquiry roster's `finding.made` row then claims only
  graded inquiries).
- `rosters.yaml: verb_capability`: `interview: "inquiry"`; `contest_subsystems.prizes`: `a standing` is
  already routed. Obstacle, through the one composer: `difficulty` + `opposition` (the interviewee's
  skill score) + `rank_gap` (OBS member 6) + `regard` (member 7, the subject's hostile stance toward the
  asker); a `tie` of the asker to the subject is a `favour` level for the asker (OBS §3). *(W3-4a: the
  private table `interview_obstacle` is not added, C-21.)*
- `rosters.yaml: question_sources`: new source `asked` (ordered after `claim_landed`, before `need` —
  a person asked a question attends to it; `attention_key` reads the order).
- `queries/world_q.py::questions_for`: for each `interview.asked` claim in the person's own ledger
  deposited this tick, one Question `q:asked:<claim id>`, source `asked`, plain referents `(on,)`, about
  the claim. The topic `on` is the interview act's operand: the subject of the asker's question's `about`
  claim, else the interviewee (derived in `_derive_operand`, no free choice).
- `decision/options.py::operand_bags`: on a Question of source `asked`, the `to` fan of `tell` and `lie`
  is the asker alone (read from the `about` claim's value, own ledger). The interviewee's chooser forms
  `tell`, `lie` or neither; his answer is that verb's own draw. At `interview.pressed` the questioner's
  press enters the answering act as the `approach` source (OBS §3: one `press_level` against the
  questioned person's answering `lie`), for this tick only (read off the claim, not held state; the source
  is `19_LACUNA_questioning_has_an_approach_and_a_cost.md`'s).
- `loop/witness.py`: no edit. `interview.asked`, `interview.pressed` and `interview.disclosed` deposit on
  those present like any Event (the interviewee among them, by the `with` conjunct); at
  `interview.disclosed` the deposit also names the asker's own question's `about` claim, so the
  interviewee learns why he was asked.

### §4 `tell`: the odds the hearer sets

- *(W3-4a, C-21: the `tell_obstacle` table and its fixture are not added; its entries are the one
  roster's.)* A telling's obstacle, through the one composer: `difficulty` + the stand-in or the hearer's
  `opposition` + `dissent` (OBS member 13: the teller's own ledger holds the hearer as believing the
  contrary on the cell; landed with `_SOCIAL2_B`) + `rank_gap` (member 6); a `tie` of the teller to the
  hearer is a `favour` level (OBS §3); a venue term from `venues.yaml` only where the SC lane lands one as
  a member. FI-02 edit 6 is answered by this composition: an ordinary telling to a friend is likely,
  never certain. Control: each member at its control step (today).

### §5 `interrogate`: a confession on file, by degree

- `verb_table.yaml` `interrogate`: `writes:` Ov / Su / Pa `[Record.stages]`, Fa `[]`; emits unchanged.
- `loop/predicates.py::_req_interrogate` clause 3: the charge may be the docket item's petition **or its
  case file**, both through `ABOUT_KEYS` (one owner); no other change.
- New `_eff_interrogate(w, a, res)`: appends `(tick, "proof:confession", <event id>, weight, a.id)` to
  the matter's case file, weight `task_fraction[degree]` (Ov / Su 1.0, Pa 0.5). Closes `H-226` by route (b)
  for this row: the fold runs the effect because the band now writes.
- Odds, as levels for the interrogator (A-25; C3-C10): the standing weight of items already on the case
  file against the prisoner is the `proofs` source; custody is the `custody` source (OBS §3: one
  `custody_level` per season held, soft-capped) — custody wears a man down, and still he may withhold.
  *(W3-4a: `interrogate_obstacle.custody_per_season` (−1 per season) is not added; nothing lowers the
  obstacle.)*
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
and break cases. S: one carrier, one ladder, the told channel; evidence enters as leverage exactly as
every other favourable circumstance does, so the hearing's arithmetic is the contest's. E, last: one
record kind, three effects that append stages, no private odds table, against three verbs that today
write nothing.

## Cost class

Small build each; §2 design-first only for the `proof_level` value (OBS §3's; a sweep, not a ruling).
