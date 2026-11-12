# 19 · LACUNA · 4 — Questioning has an approach and a cost: tone moves the odds, and the questioned learn they were asked

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-12, C-18) — `press` subtracts from no obstacle (Jordan, A-25): it is one `press_level` for the questioner in the engagement draw and one against the questioned person's answering `lie` (`U5c_SC_one_obstacle_form.md` §3, source `approach`). The `interview` row is `14_VERBS_SOCIAL2_C_case_question_confession.md` §3's; this file supplies its `approach`.

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

`interview` and `interrogate` gain an `approach` key (`calm` | `press`; default `calm`, the control) chosen
from Candidates; it moves the obstacle of the questioned person's answering act and, at `press`, his
regard of the questioner. Every admitted `interview` deposits to the questioned person a claim that he was
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

**R-19-10 · Approach is a chosen key that moves odds, never outcomes.** `approach ∈ {calm, press}` on
`interview` and `interrogate`, `rosters.yaml: choice_sourced` (both values formed as Candidate variants, so
a player and the chooser pick from the same list). Effects, all as obstacle terms on the questioned
person's answering act (CP-T06-05's `tell` / `lie`) and written to `Margin.terms`:
- `press`: the answer's obstacle for a **truthful** answer falls by `press_ob` (the questioned person is
  harder to stall) and for a `lie` rises by `press_ob` (pressure makes a lie harder to hold); the
  questioned person's regard of the questioner falls by one `regard` step (the stored half,
  `queries/person_q.py:424`), a told deed of the questioning that others may hold;
- `calm`: no term; no regard change.
`press_ob` is a NUMBER row (`fixtures`, proposed 0.5, sweep 0 / 0.5 / 1, control 0). No outcome is set by
the approach: a pressed liar still lies successfully sometimes. Ladder step 3 (VCD row 9 is the design;
`regard` is the named reader).

**R-19-11 · The questioned learn they were asked.** Every admitted `interview` / `interrogate` deposits
to its subject one firsthand claim `(questioner, questioned_about, <the act's question subject>)` with the
act's `when`, through WITNESS's existing observation deposit (`observation_deposit_mode`, at the
counterpart). The subject's chooser then reads it as any held claim: a guilty person holding *"I was asked
about the forging"* forms `conceal`, `forge`, `lie`, flight (`move`) or `tell` (warning an accomplice) by the
ordinary rows. This is Lacuna's single-play rule translated: not *"you cannot ask twice"* but *"asking
teaches the asked"*. Ladder step 5.

## Exact edits, by owner

1. `engine/season/verb_table.yaml` — `interview`, `interrogate`: a payload key `approach` declared in the
   row's `requires_note` as non-operand; `emits` unchanged.
2. `engine/season/rosters.yaml: choice_sourced` — `approach` for both rows, values `calm`, `press`.
3. `engine/season/seam/wrappers/sigma.py` (or the CP-T06-05 host, whichever builds the answering act's
   input) — the `press_ob` term, signed by whether the answer is `tell` or `lie`.
4. `engine/season/loop/witness.py` — the counterpart observation for `interview` / `interrogate`
   (one predicate `questioned_about`, added to `rosters.yaml: person_predicates`).
5. `engine/season/data/fixtures.py` — `press_ob`.

## Gate (execution artifacts)

On `inquiry_world(seed)` with CP-T06-05 landed, seeds 0-199, `PYTHONHASHSEED=0`:
- a planted guilty interviewee questioned `press` lies successfully in a share strictly lower than
  questioned `calm`, and strictly above 0;
- after one admitted `interview`, the interviewee holds `(questioner, questioned_about, X)`; in the
  following season, the share of guilty interviewees who fold `conceal`, `forge`, `lie` or `move` is above
  the same share with the deposit off (control), and the share of innocent ones is not;
- `press` lowers the interviewee's `regard` of the questioner by one step; `calm` leaves it.
Control: `approach` absent and the deposit off reproduce the base content hash.

## Falsifiers

- If `press` changes the lie's success share to 0, the term is a lock, not odds.
- If guilty and innocent interviewees react identically to being questioned, the deposit is not read by
  the chooser, or nothing they hold makes the question threatening.

## NERS reading

- **N**: without it, questioning is free and safe, so the dominant play is to question everyone; with it,
  whom to ask, when, and how hard is a choice. Diagonal: the subject's reaction feeds the investigator's
  next finding (a cover forged after a question is a new trail).
- **R**: tone becomes a lever with a price; NPC suspects respond to being suspected with no player present.
- **S**: odds through the one obstacle; disclosure through the one deposit; regard through its one owner.
- **E**, last: one key, one term, one predicate, against a questioning with no consequence for anyone.

## Cost class

Small build, after CP-T06-05 (B10-14). Lanes: FI (rows, deposit), CHAR (chooser variants, regard).
