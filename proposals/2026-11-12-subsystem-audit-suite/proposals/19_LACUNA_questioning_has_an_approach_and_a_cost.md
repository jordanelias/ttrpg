# 19 · LACUNA · 4 — Questioning has an approach and a cost: tone moves the odds, and the questioned learn they were asked

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-12, C-18) — `press` subtracts from no obstacle (Jordan, A-25): it is one `press_level` for the questioner in the engagement draw and one against the questioned person's answering `lie` (`U5c_SC_one_obstacle_form.md` §3, source `approach`). The `interview` row is `14_VERBS_SOCIAL2_C_case_question_confession.md` §3's; this file supplies its `approach`.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.6 row (CONFORMS after the head's rewrite), §2 row R-19-10, §7, §7b-12, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` ledger P-03, R-25, S-08; `unified/U1_GLOSSARY.md` *approach*; `unified/U3_DEPENDENCY_ORDER.md` node B26). The body follows its head: R-19-10's `press_ob` (an obstacle that **falls** for a truthful answer, a subtraction A-25 forbids) is replaced by `press_level` leverage (one level for the questioner in the engagement draw and one against the questioned person's answering `lie`; OBS §3, source `approach`; fixture `press_level`, first value `minor`, control `None`), and `press_ob` is dropped from the edits and the gate; the choice key is **`questioning`** (`calm` | `press`), not `approach`, which names the PC lane's set in the same `choice_sourced` roster (U1 ledger P-03, S-08; the leverage source keeps the name `approach`); named tests; lands-it and tier.

**Lands in batch:** B26. **Depends on:** `14_VERBS_SOCIAL2_C_case_question_confession.md` §3 (B25; the `interview` row), plan position CP-T06-05 `[PL]`, `U5c_SC_one_obstacle_form.md` §3 (B05; the `approach` source).

## Status: PROPOSED (small; depends on CP-T06-05, the questioned person answering by his own act)

Carries `audits/19_LACUNA_investigation_to_proceedings.md` §4.2 and resolutions R-19-10, R-19-11.
Precedent: Lacuna tracks an agreeable or aggressive tone toward witnesses as a run-wide counter (T19 §LA §3,
§7, V3 gamepretty; its effect on play is not established); Lacuna's dialogues are single-play and a clue
can be lost by a wrong choice or order (Colbus devlog, page read: *"each dialog can only be played a single
time"*; T19 V3 a-to-jconnections). The tree already carries the approach as a planned payload key (VCD row 9,
`proposals/2026-10-03-verb-coverage-and-gap-fill.md:776`, `:2442`: *"a non-operand payload key on
`interview` and `interrogate`, read by the effect or the obstacle; the subject's `regard` … is its
reader"*); `D_T06.md:59` records it as LACKS.

## What this changes in `engine/season/` at runtime

`interview` and `interrogate` gain a `questioning` key (`calm` | `press`; default `calm`, the control)
chosen from Candidates; at `press` it adds named levels for the questioner and against the questioned
person's answering `lie` (never an obstacle subtraction), and moves his regard of the questioner. Every admitted `interview` deposits to the questioned person a claim that he was
questioned, by whom and about whom. Declared hash mover wherever either verb folds (19 / 8 / 19
`interview` at `build_realm(0..2)`, `08_FI_03`).

## The problem (evidence)

1. `interview` reads nothing from the interviewee and carries no approach; it emits `finding.made` and
   writes `[]` (`verb_table.yaml`, `interview`); no interview-specific deposit to the interviewee exists
   (`grep interview` over `loop/witness.py` and `loop/effects_information.py`: no hit; an absence by grep,
   `[UNVERIFIED]` that WITNESS's general presence deposit does not already give the subject a `seen` of the
   act — the gate's control reads it first).
2. Lacuna's single-play rule is a lock; in Valoria a lock is presentation, but the *risk* behind it — you
   cannot question a suspect without telling him what you suspect — is fiction and is absent. A guilty
   person in Valoria cannot learn he is suspected, so he never flees, forges cover or lies ahead of time
   because of a question.

## The resolution, decided

**R-19-10 · Questioning is a chosen key that moves odds, never outcomes.** `questioning ∈ {calm, press}` on
`interview` and `interrogate`, `rosters.yaml: choice_sourced` (both values formed as Candidate variants, so
a player and the chooser pick from the same list; the key is `questioning`, not `approach`, which is the PC
lane's key in the same roster). Effects, all on the leverage channel (A-25: nothing lowers an obstacle) and
written to the roll's `levels`:
- `press`: one `press_level` for the questioner in the engagement draw, and one `press_level` against the
  questioned person's answering `lie` (CP-T06-05's `tell` / `lie`; pressure makes a lie harder to hold), by
  the leverage source `approach` (`U5c_SC_one_obstacle_form.md` §3); the questioned person's regard of the
  questioner falls by one `regard` step (the stored half, `queries/person_q.py:424`), a told deed of the
  questioning that others may hold;
- `calm`: no level; no regard change.
`press_level` is a fixture (`LEVEL_SIGMA` name; first value `minor`, sweep `None` / `minor` / `moderate`,
control `None`; U1 ledger R-25). No outcome is set by the approach: a pressed liar still lies successfully
sometimes. Ladder step 3 (VCD row 9 is the design;
`regard` is the named reader).

**R-19-11 · The questioned learn they were asked.** Every admitted `interview` / `interrogate` deposits
to its subject one firsthand claim `(questioner, questioned_about, <the act's question subject>)` with the
act's `when`, through WITNESS's existing observation deposit (`observation_deposit_mode`, at the
counterpart). The subject's chooser then reads it as any held claim: a guilty person holding *"I was asked
about the forging"* forms `conceal`, `forge`, `lie`, flight (`move`) or `tell` (warning an accomplice) by the
ordinary rows. This is Lacuna's single-play rule translated: not *"you cannot ask twice"* but *"asking
teaches the asked"*. Ladder step 5.

## Exact edits, by owner

1. `engine/season/verb_table.yaml` — `interview`, `interrogate`: a payload key `questioning` declared in the
   row's `requires_note` as non-operand; `emits` unchanged.
2. `engine/season/rosters.yaml: choice_sourced` — `questioning` for both rows, values `calm`, `press`.
3. `engine/season/seam/wrappers/sigma.py` — the `approach` member of `ADVANTAGE_SOURCES` reads the act's
   `questioning` value and returns the `press_level` lists (the questioner's on the engagement draw; one
   against the answering `lie`).
4. `engine/season/loop/witness.py` — the counterpart observation for `interview` / `interrogate`
   (one predicate `questioned_about`, added to `rosters.yaml: person_predicates`).
5. `engine/season/data/fixtures.py` — `press_level` (`press_ob` is not created).

## Gate (execution artifacts)

On `inquiry_world(seed)` with CP-T06-05 landed, seeds 0-199, `PYTHONHASHSEED=0`:
- a planted guilty interviewee questioned `press` lies successfully in a share strictly lower than
  questioned `calm`, and strictly above 0;
- after one admitted `interview`, the interviewee holds `(questioner, questioned_about, X)`; in the
  following season, the share of guilty interviewees who fold `conceal`, `forge`, `lie` or `move` is above
  the same share with the deposit off (control), and the share of innocent ones is not;
- `press` lowers the interviewee's `regard` of the questioner by one step; `calm` leaves it.
Control: `questioning` absent (`press_level` `None`) and the deposit off reproduce the base content hash.
Named tests (new, `engine/season/tests/test_questioning.py`): `test_pressed_lies_succeed_less_but_above_zero`;
`test_the_questioned_learn_they_were_asked`; `test_guilty_react_to_being_asked_and_innocent_do_not`;
`test_press_lowers_regard_one_step_and_calm_does_not`; `test_press_lowers_no_obstacle` (the `terms` are equal
across `calm` and `press`; only `levels` differ).

## Falsifiers

- If `press` changes the lie's success share to 0, the term is a lock, not odds.
- If an obstacle term differs between `calm` and `press`, a favourable term was subtracted (A-25).
- If guilty and innocent interviewees react identically to being questioned, the deposit is not read by
  the chooser, or nothing they hold makes the question threatening.

## NERS reading

- **N**: without it, questioning is free and safe, so the dominant play is to question everyone; with it,
  whom to ask, when, and how hard is a choice. Diagonal: the subject's reaction feeds the investigator's
  next finding (a cover forged after a question is a new trail).
- **R**: tone becomes a lever with a price; NPC suspects respond to being suspected with no player present.
- **S**: odds through the one leverage channel; disclosure through the one deposit; regard through its one
  owner.
- **E**, last: one key, one term, one predicate, against a questioning with no consequence for anyone.

## Cost class

Small build, after CP-T06-05 (B10-14). Lanes: FI (rows, deposit), CHAR (chooser variants, regard).

**Lands it and tier.** The B26 batch, an FI `valoria-author` session on `sonnet` (`high`), closed by B26's
`methodology-close` once. **Hash movers.** Wherever `interview` or `interrogate` folds once the key or the
deposit is on (declared).
