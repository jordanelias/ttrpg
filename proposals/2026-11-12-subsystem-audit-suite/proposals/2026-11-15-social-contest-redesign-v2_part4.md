# SC — the social contest redesigned, v2, part 4: the NERS pass, the cuts and the overturned cuts, the plan corrections, the questions, the one table of the second fix pass

## Status: PROPOSED (the fourth part of `2026-11-15-social-contest-redesign-v2.md`; read that file's head first; reference under CLAUDE.md §0.05, nothing reads it at runtime)

---

## E. The NERS pass (as it stands after the second fix pass; figures are part 3's and §K's and are not repeated here)

`[SELF-AUTHORED — bias risk]`, by `skills/ners/SKILL.md`; three critic passes and one premise-check are folded in.
Each row: the cut, what the game can no longer do, who decides what and what he sees, and the verdict.

| object | cut it, and | the decision; what he sees | verdict |
|---|---|---|---|
| a track per person | no split room, no divided bench, no partial seat | which body to speak to; mood, odds | N holds |
| the point, the answer, the issue ladder with its stasis weights | nothing said refers to what was said; a concession is only surrender; every rung is argued alike | answer, raise or descend; their point | N holds: the accused answers, the questioner asks, a descent buys the next rung's ground and always costs |
| `silence_cost`, the `silence` cell and the burden (A-145) | silence under a charge is free; an unargued charge carries at the bench's odds; regime means nothing to a silent man | speak or hold his tongue, knowing what silence means here and what happens if nobody speaks (both on the card) | N holds for both sides (the largest open item of the first pass is closed) |
| `temper_break`, the heat that cools (A-146, A-136) | a rattled man may always take refuge in silence; provoking pays nothing; a short-tempered man is born broken | whether to provoke; a menu without rest | N holds; nobody breaks unprovoked |
| the press, its object, the rattle, `reactance`, `wear` | the man cannot be attacked, or is attacked on nothing | the point or the man, and on what | N holds; a press bites by how the matter bears on what he holds; pressing no longer crowds out argument (part 3 §B) |
| `relevance`, `k`, `gap` (Reason) | what is said need not be to the point; a scholar and an orator are one build; office weighs nothing | which ground; answer the point; whom to face | N holds, each on its own arm |
| `frame` and `perceived`, the believed reading of each listener (Attunement) | everyone knows what moves each listener, what each option is worth, and how sharp the judge is | which ground, framed on what, trusted how far | N holds |
| `heard`, relative to the man opposite (Presence) | a quiet man is heard by a crowd as well as an orator | the room to choose | N holds; no longer tilts a gallery against whoever speaks |
| `esteem` (Grace) | conduct and respectability mean nothing; a gracious man has no composure in hand when pressed | venue and opponent | N holds; above the occasion's standard it is headroom against rattles |
| `weary`, the opposition (Will) | effort is free; nobody can be shaken | turns to prepare | N holds |
| the hold (`drift`) (Focus) | Focus has no speaker role | none of his own | N holds **only under pull**, and modestly (decided, §F) |
| `validation` (adjudicator's Reason) | a polished unsound speech fools every judge alike | who sits decides how to argue | N holds |
| `wF` (adjudicator's Focus) | irrelevance sways every judge alike | | N holds on the filter of wandering; **the theatre half is CUT** (false N-line, as the first pass warned) |
| insincerity deducted; discomfort read by `discern` (adjudicator's Attunement) | a liar and a nervous honest man look like anyone, or alike | say what I hold | N holds; an honest nervous man is no longer marked as a liar |
| `awe` (adjudicator's Presence and station) | a commoner is as composed before a duke as before a peer | which forum; whom to send | N holds |
| reception, rulings only (adjudicator's Grace) | a verdict is received by its rightness alone; a brute judge pays nothing | for a played judge: how to carry his office | N holds; right and wrong are read from the record, not from his lean |
| the bearing reading, `start`, conflict and recusal, `credit`, items, the witness | every person is his attributes; nothing the world holds can be shown; a judge's conflicts net to zero | stake, forum, what to bring, whom to seat | N holds |
| arrangement (`tilt`), its price, the weak party's acts | every forum is neutral; a rig is free if secret; a loser has nowhere to go | how hard to rig; accept, contest or go elsewhere; appeal | N holds; each rig level is best somewhere |
| context rows | | lawful forum; what silence means; what may be shown; which ground to reach for | strife holds; era and regime act on PLAY (decided, §F; question 1) |
| the own-case rule for a party who decides | a noble's speech is dead air, or inverts his Reason | whether to speak before ruling | N holds where he has a stake; within noise for a party with nothing at stake |
| the disposal rows, the `Card`, the fold's one table, the acts after and the season driver | an outcome is a band; rules learnt by losing; the world forgets nothing or remembers everything | after a loss, what next | N holds |

**E, last.** Records 12 to 10 (`Present`, `Rite`, `Item`, `Sitting`, `Point`, `Cond`, `Beat`, `View`, `JudgeView`,
`Outcome`); moves 6 to 4; ends 6 to 3; draws 6G+11 an exchange, stated once and asserted, and one a decider.
**Settings 55** (53 before the redesign; the second pass cut one and added two, each for a named finding) **and the
fold's 24 coefficients, now counted** (they were hard-coded). The pass deleted more than it added: the theatre half
of Focus, the declared close's veto step, `yield_track`, the rig's turn cut and its secrecy discount, negotiation's
inert `reply: must`, discomfort as a ploy, interest as insincerity, the reset on conceding. *Legibility:* the
ground, frame, press object, concession, silence and the burden, his standing, weariness, awe and temper are on the
view; the card now says what happens if nobody speaks and when it closes; how each adjudicator weighs him is seen
only as the room moving.

```
MUST BE STATED AS A LIMIT
  - B17 in part: no view-only in-sitting policy beats taking the top worth by more than noise (question 2)
  - the speaker's Focus acts only under pull and modestly; Will is silent at the rally as at the tell
  - a party who decides with nothing at stake: his argue against rest is within noise in a two-turn audience
  - conceding the whole matter before a bench is best nowhere by the sitting's own reckoning (decided, §F)
  - contesting a tilted forum is the weak party's best act only at the highest stakes with no other forum
  - the cast debate stays press-heavy: a diplomat with no case attacks what the orator wants (character, not rule)
  - the venue's formality scales silence's contempt within noise; the station term carries it
MAY BE CLAIMED, HAVING SURVIVED
  - the five causes C1 to C5 are fixed at the cause, each symptom re-measured (§K)
  - every clause of R1, R11, A-141 to A-146 has a carrier with a measured slope and a control, except those above
  - silence under a charge and an unpressed charge are priced and on the card; a broken temper cannot rest
  - a verdict's reception is a separate axis from its rightness, and rightness is read from the record
  - regard, legitimacy and standing are bounded, fade and recover; twelve seasons show no runaway
GRADE: paper, with a running model (sc_model_v2/v8_out.txt). Nothing in the tree runs it.
```

---

## F. Decisions taken by the ladder

| # | decision | rung |
|---|---|---|
| 1 | the ploy is carried by `insincerity` on `argue` and `press`; `deceive` and `divert` are not restored | 5 (their clauses are carried once; A-140 restores only a sole carrier) |
| 2 | the decider's three are weights in his own track; no draw | 5 |
| 3 | no judging pool | 2 |
| 4 | a conviction is never written by a proceeding | 3 (`04:251`, A-92) |
| 5 | one live point a side; the parts of a speech, inoculation, a self-contradiction rule are not built | A-130 (game first) |
| 6 | deliberation among deciders (N10) is not built | 1 (A-14) |
| 7 | fit is symmetric about the middle of the scale and reads the matter | 5 |
| 8 | `bench` draws the presiding seat alone; `declared` every seat, and carries by the quorum-th best | 4 (RD §C.8, B24.11); C5 for the quorum |
| 9 | the rally is deliberative; epideictic has no row | 3 |
| 10 | `consequence` is pathos, `evidence` alone is logos | 3 (`NP:27-28`) |
| 11 | a final concession by anyone but the bearer or a party who decides sets the room as far against him as the close carries and the bench still draws | 1 (A-14) with HEAR_B's rule that an end is never a verdict |
| 12 | `Sitting.tracks` stays in the value as the running sum | 5 (resume without replay) |
| 13 | `conversation` and `questioning` close on the man addressed; `negotiation` keeps consent; an `audience`'s seat may be the other party and decide | 1, 3, 4 |
| 14 | **the burden**: the bearer of a matter the other side must answer pays as silence does while no point of his stands; an unargued charge lapses, and the card says so (`unargued`) | 3 (A-145: silence is "refusal to engage in proceedings", which the bearer's silence is) and 5 (one rule with A-145, not a second) |
| 15 | an answer is offered only to a point that stands and is bounded both ways by how far it stands | 5 (a failed answer confirms a point; it does not make a new one) |
| 16 | Presence is heard relative to the man opposite, as esteem is | 5 (S: one methodology for the two relative operands) |
| 17 | a party who decides hears his own case with his own Reason and Will | 3 (A-144: the validating Reason is the adjudicator's; the brief's C2) |
| 18 | "keeping his temper" is being below `temper_break`; the temper is this sitting's heat against what Will and Grace carry; it cools | 3 (A-136, A-146's words) |
| 19 | a rig's price is `rig_price x tilt^2`, whoever is in the room; the rig no longer cuts turns | 5 (a closed court is a known sign; the turn cut harmed the arranger's own case) |
| 20 | the arranger's side is his own where he is a party; resentment and rig-grounds of appeal follow the side the tilt worked against | 5 |
| 21 | a yield by the bearer drops the matter; by a party who decides it is his giving way | 5 (nothing is left to decide; consent's rule) |
| 22 | "wrong" is against the merits as the record shows them | 5 (the judge's lean is partiality, priced separately) |
| 23 | a Grace-7 judge is never a brute; station and respectability are each on 0..1 | 3 (A-144(6): "little grace") |
| 24 | discomfort is never read as insincerity; it scales how a rattle moves an attuned listener (`discern`) | 3 (A-144: perceive "comfort/discomfort AND sincerity/insincerity", two things) |
| 25 | the theatre half of the adjudicator's Focus is cut; the clause is carried by the deduction of what is off the point | 5 (no slope; one carrier per clause) |
| 26 | Will is the resisting attribute, not one of A-144's judging five | 1 (A-137) |
| 27 | the speaker's Focus carries R1's clause where something pulls, and says so on the card (`unrest`) | 3 (R1: "not being pulled away") |
| 28 | Will is silent at the rally as at the tell (no one to rattle him; staying power rarely reached in three turns) | 4 (A-138's precedent) |
| 29 | surplus Grace above the occasion's standard is composure in hand against rattles; it earns nothing at a quiet tell | 3 (R1 Grace: "remaining composed in face of difficulties") |
| 30 | negotiation's `reply: must` is cut (consent already prices stalling: no deal) | 2 (the cell was inert) |
| 31 | `interrogation` names Jordan's "interrogation for information" (a questioning); the polity's inquisition is an `examination`; a `tribunal` is a panel; `stakes` is renamed `gravity` | 3 (Jordan's own list), CLAUDE.md §4 (one word, one thing) |
| 32 | era and regime act on PLAY (which ground, whether to rest, what to show, which rite exists), not by a term in the close | 5, with question 1 |
| 33 | the forum's time is the measure of when those who decide are ready | 5 (a second closing rule adds a threshold and an end for no decision a player makes) |
| 34 | a played adjudicator rules at the close only | A-130 and 5 (a bench move is a second interface for one role; the judge who must question is a party who decides) |
| 35 | conceding the whole matter before a bench is kept though best nowhere by the sitting's reckoning: it is the broken timid man's act (A-136) and a player's confession | 1 (A-136 "the timid give way"; A-14) |
| 36 | the venue's formality in silence's contempt is kept (within noise) | 3 (the A-145 record's "grows with the venue's standard") |
| 37 | a false item comes from his own false word (read from what he knows) or a forgery `[HOOK]` | 5 |
| 38 | a seat with a conflict at `recuse_at` steps down where another can sit; a party who sits does not (he judges by choice and is seen) | 3 (A-131 "partial and seen to be"; A-139) |
| 39 | a passing word (effort 0) nobody watches runs abridged (`form="auto"`) | 3 (R6) |

---

## G. The cuts, and the cuts overturned (A-140)

**Overturned** (each removed the only carrier of a ruled clause; restored as the simplest carrier on existing
structures):

| cut | the clause it served | restored as | cost |
|---|---|---|---|
| `accounts`, the `eased_by` operands, the host's `rank_gap` | R1 Reason: *"account for opponent's factual circumstances like resources office influence"* | `gap` | one setting |
| `resolve`, per-speaker `effort` | R1 Will: *"keep arguing your case"* | `weary` | three settings, one number of state |
| `esteem`, `respect_step` | R1 Grace: *"seen as respectable"* | `esteem`, derived | one setting, none net |
| `heard_step`, `heard_floor` | R1 Presence: *"listened to"* | `heard`, now relative | two settings |
| the opponent's dispositions in the reading | R1 Attunement: *"reading their intent"* | `View.intent` | one normal |
| `sense` as a level added to a speech | R12 Reason: *"does it make sense"* | `validation` | none |
| sincerity read from stake alone | R12 Attunement: *"sincere or a ploy"* | `believes` in `insincerity`; a false item from his own word | one field |

**Cuts that stand** (no ruled clause lost): the four person records into one; the judging pool; `Decider.lean`
and a regard step at the ballot; `moved_by`, the `read:` cells, `fit_body`, `misfit_level`, `sore_gain`; `proofs`
as a source and roster; `proof_weight`, `reason_bias` and the audience-kinds table; `attention`, `delivery_step`;
`mark_shame`, `cover_step`; `shield_step`, `resist_step` at the ballot; the steadiness draw; `break_at` and the ends
`broken`, `struck`, `adjourned`; `strikes`; `divert`, `deceive`; the ballot sources and the detection draw; the
clamp; `presumes`, `scripted`, `order`, `written_only`; `case_rows`; `press_at`; `reading_kept`; the disposals
`mutual` and `none`; five rows as kinds; the weighting by ground class (`q`); the turning-away charge (`evade`);
the view's per-ground believed fit, aim and strain; the reading as a pool draw; the expected-move field; `elicit`;
the policy's bonus for the proof; `sense_level`; `manner_step`; the restated primitives table. **Cut in the second
fix pass** (each: what it carried, and that nothing ruled is lost): the theatre half of Focus (`swayed`: no slope;
the clause is carried by the filter of wandering); `yield_track` (a number standing for "wholly against him": the
close's own leverage ceiling says it); the rig's turn cut (it harmed the arranger's case as much as the other's);
the rig's secrecy discount (a shut door hides nothing); the declared close's veto step (a quorum is a majority, not
a veto); negotiation's `reply: must` (inert: consent prices stalling); discomfort inside the ploy deduction (it
marked honest nervous men as liars; discomfort keeps its own rule); interest and bond inside insincerity (arguing
against one's interest is not lying); the reset on conceding an issue (it improved the conceder's standing); the
grievance a failed tell or rally filed against nobody; reception minted by tells, rallies and a party's own
decision.

---

## H. The plan-item corrections (ordered; none applied)

Files: `p22` = `workplans/valoria_master_workplan_v12_part22_b24p.md`, `p22c` = `_b24p_cont.md`, `p8`, `p8c`, `p9`,
`B22` = `..._part22.md`, `B22c`, `p34`, `p35c` = `..._part35_cont.md`.

1. **`p8c` B05.14, `p8` B05.25, B05.10** (A-137): the opposition of a row contested against a person is
   `opposed_ob(opposing attribute + score)` at `MU_PER_DIE`; the subject-side levels on `opposed_attribute` are
   deleted; B05's calibration then sets the difficulty cell to A-79's centre (0.8 reads 25 % carried in the model).
2. **`p22` B24p.01**: `grounds` lose `read:`; `proceeding_moves` is `argue`, `press`, `concede`, `rest` with
   `effect`; ends `budget`, `rested`, `yielded`; add `matters` (absorbing `proofs`); delete `case_rows`.
3. **`p22` B24p.02**: the ten records of part 2 (`Present`, `Rite`, `Item`, `Sitting`, `Point`, `Cond`, `Beat`,
   `View`, `JudgeView`, `Outcome`) with `Input`'s one invariant and its keyed refusals; `Cond` carries `heat`;
   `Beat` carries `left` and `caught`; `Input.state` is a whole `Sitting`.
4. **`p22` B24p.03**: each row names its cells, `weighs` (stasis) and `gravity` (renamed from `stakes`) among them;
   add `context` and `disposal` blocks (the `yield` disposal for questioning); a row declares who adjudicates
   through `close` (a party may be among them); the loader refuses only a row that can seat one character in every
   role; delete `audience_kinds`, `presumes`, `strikes`, `order`, `reason_bias`, `base_disposal`; the aliases:
   `legal_trial`, `tribunal` (a panel: `close: declared`), `arbitration` on `trial`; `parliamentary_debate`,
   `council_of_state`, `excommunication_deliberation` on `debate`; `inquisition_hearing` and `examination` (the
   polity's) on `inquisition`; **`interrogation` on `questioning`** (if the tree's `interrogation` row is the
   polity's inquisition, it is renamed `examination` in the same item); negotiation's `reply` is `may`.
5. **`p34` B32.15** (`acclamation`): `close: consent` on the `rally` structure, with no `order` key.
6. **`p22` B24p.04, B24p.05**: the 55 settings at controls and the fold's table; the obstacle roster gains `weary`
   and `standing`; the old leverage sources and the four-tuple are deleted.
7. **`p22` B24p.06** (held under attack): `person_q.bearing`, `care`, `tie` (a shared faction counts), `conflict`,
   `strain_carried`, `takes_side`, `effort_of`, `false_items`; the builder reads the speaker's **own** ledger for
   items and `believes`, never `world_q.proofs` or `world_q.reception`.
8. **`p22` B24p.07 to .10**: one item, the exchange (**6G+11** normals, stated once as `DRAWS_PER_EXCHANGE`).
9. **`p22` B24p.11**: order; three ends; the policy with the heat-based temper; the burden; **resume** by
   `cond.spoken`, a `yielded` sitting refused, the issue reached kept.
10. **`p22` B24p.12**: the close of part 2 §D (`declared` by the quorum-th seat; a yield that is a decision); believed
    odds from the chooser's reading; the card's odds as what a sitting where nobody speaks delivers.
11. **`p22c` B24p.13** (the builder; corrected). `world_q.judging_set` returns person ids; the authority filter
    reads `w.offices[office].faction` and `authorities.by_faction` (not `gate.seat_faction`). The builder also takes
    the arranger and `rig` (no turn cut), applies context, recuses a conflicted non-party seat, offers the false
    word, seats who comes to oppose, chooses the form (`auto`), returns the `Card`.
12. **`p22c` B24p.14** (corrected). `degree_of` returns on `settled_margin` at `:262-263` before any other branch;
    the `declared` close no longer needs a veto, so no edit to `degree_of` is needed for it.
13. **`p22c` B24p.15** is deleted; the arrangement reaches the builder as operands of `open_case` and `convene`.
14. **`p22c` B24p.16, .19** (held): `seat/contest.py` takes the proceeding entry for any row carrying `proceeds:`;
    `lie` is `argue` with the liar's own false word as its item.
15. **`p35c` B28.34, B28.35, B28.10**: as before (the hearer's ties and stake in `fit` and `start`; the teller's seat in
    `gap`; the self-plea keeps its accuser).
16. **`p22c` B24p.20, .22**: the `ending` stores the beats and the `Sitting`; B24p.22 deposits what the beats show
    (`caught` for `hypocrite`, one temper claim, a bystander's `heard`).
17. **`p22c` B24p.17, .18, .21, .23**: readings and role tests re-pointed at part 2 §C.3 and §C.6, each gated on a
    positive arm with the ruled sign and "setting off reads exactly 0"; a role's gate is per type reading (A-138).
18. **`B22` B24.03, B24.08, `B22c` B24.30**: `issues` lists rungs of `issue_rungs`, with their stasis weights; a
    negotiation's `accept` is a concession under `concede: accepts`; a questioning's yield is the questioned man's
    accept, and a confession accepted or a charge laid on it is `determine`'s separate step.
19. **New, `B27` and `B33`** (regard, legitimacy, standing, strife): every write is `bounded`, fades between seasons,
    and a strife moves only by what a sitting resolved; the acts after a sitting (`after`) write the docket, and
    the season loop convenes it (appeals before another authority, grievances, adjourned matters, other forums).

---

## I. Questions for Jordan (two survive the ladder)

1. **Regime and era.** Requirement 8 says they "will impact". As built, both act on PLAY: a regime decides which
   rites are lawful, what proof is admitted, what the occasion asks of Grace and what silence means (under a
   commune the charged side rests far more often; under a crown, silence costs him dearly), and the era changes
   which ground a speaker reaches for. Neither moves who wins a spoken contest between men with nothing at stake.
   Options: (A) accept that as their impact (as built); (B) give each regime a term in the close itself (its
   `difficulty` or `gravity` by kind of matter), which would make the same case harder to carry under one regime
   than another.
2. **Play within a sitting that the view does not hand over (B17).** Choices now matter in every played rite, and a
   sharper reader wins more; but within one exchange the shown worth is close to the answer, and the skill the view
   does not give lives before and around the sitting (forum, rig, what to bring, effort, appeal, provoking).
   Options: (A) accept that (the sitting rewards reading and preparation); (B) add one in-sitting decision with
   hidden information, for example *whom he addresses* in a room that decides by a quorum (the swing seat, read
   from his believed view of each seat), at the cost of a second axis on every option.

The first pass's question 2 (speaking against silence for the side not charged) is answered by the ladder: the
burden (§F 14) and Presence relative to the man opposite (§F 16).

## J. What was not verified

- Nothing in the tree runs this design; the plan edits of §H were not applied.
- One battery, `checks_v8.py`, n = 300 an arm unless stated: every figure in these files is from it. Not in it: a
  crowd changing bench rows, the hostile magnate, several speakers a side, a calibration over random pairs.
- The premise-check runners' probes (`pc_run1` to `pc_run4`) were adapted, not re-run as they stand: their findings
  are re-measured by `fix2/*.py` on the current API; the model as it stood is kept in `fix2/before/` for a control.
- The season driver is the model's own minimal loop, not the season loop; its reckonings (the weak party's and the
  loser's worths) are labelled assumptions in units of the fold's writes.
- Not opened: `05_SC_evidence_and_rebuttal_B.md`, the 2026-10-24 character-layer proposals beyond their head,
  `30_WR_*`, the institutions proposals, `28_SCENE_ACCESS`, strife-flows, `write_matrix.yaml`, H-80, P10, R-35,
  HEAR_B; `04` only at `:127` and `:251`.

---

## K. The second fix pass: every item of the premise-check, and how it ended

FIXED: the probe re-run, before and after (before: the premise-check's own figure, on the model in `fix2/before/`;
after: `v8_out.txt`, seed and n as there). CUT: what it carried, and that nothing ruled is lost. DECIDED: the rung
(§F row). An item marked **(open)** is stated with its reason; none is silently dropped.

K_TABLE_PLACEHOLDER
