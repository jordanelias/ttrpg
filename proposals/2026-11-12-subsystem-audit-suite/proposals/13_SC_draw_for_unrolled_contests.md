# SC — every contest draws: a roll for negotiation, questioning, docketing, the ballot and the appeal

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-07, C-11, C-12) — of the five rolls here, three yield and two stand. Negotiation: acceptance is not the offerer's roll; it is the accepter's own sampled `commit` (`05_SC_negotiation_scene.md`; `14_VERBS_SOCIAL1_B_documents_and_obedience.md` §3), because one person's roll cannot open another's edge (`04` D-10a). Questioning: the `interview` row is `14_VERBS_SOCIAL2_C_case_question_confession.md` §3's. Docketing: `carry`'s draw is `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` §1's, and `open_case` on one's own bench is a remit act and is not drawn. The ballot stands, owned by the hearing's close (edits 3 and 4 yield to `U5c_SC_proceedings_residue.md` §6; Jordan, A-14). The appeal stands as `19_LACUNA_verdict_ladder_and_reversal.md`'s, on new grounds only (A-39).

## Status: PROPOSED

Written by the contest-interrogation lane (`audits/13_SC_contest_interrogation.md` §4 cells 8–11, §8
R-7, R-8) under the standing rule Jordan set on 2026-11-12 (`AUDIT_BRIEF.md`, *"We do not do
deterministic!!!!!"*): every consequential outcome resolves by a draw with a graded, recoverable result;
state sets the odds, the draw sets the outcome. Ratifies nothing; reference under `CLAUDE.md` §0.05.

## What it changes in `engine/season/` at runtime

Five contest types that resolve today as a fixed function of state get the one social roll
(`modules/social_contest/roll.py`), through routes the tree already has, with band maps on their verb
rows. Every act of these verbs that executes today now draws and can come out four ways. A declared
mover for every world in which they execute (in the realm: `petition`, `carry`, `open_case` and
`interview` execute every season; `covenant` is formed and only refused today, so its draw is reached
once the refusal is cleared by the SOCIAL verb lanes). Eligibility and `requires:` stay checks: who may
attempt the act is unchanged.

## The problem, with evidence

1. **Negotiation.** `covenant` (`verb_table.yaml`: `stratum: social`, no `contests:`) offers terms and
   emits `covenant.offered`; acceptance is not resolved at all, and `exchange` is uncontested. The
   `negotiation` arrangement row (`disposal: mutual`) is read by no roll (audit §1.1).
2. **Questioning.** `interview` (`own`, uncontested) emits `finding.made` with no resistance from the
   witness; `interrogate`, the bench's questioning, rolls (audit §1.2, degenerate cell 8).
3. **Docketing.** `petition` mints a Record and `carry` / `open_case` put a matter on the docket with
   certainty (SC audit §1); whether a room takes up a matter could go either way and never does.
4. **The ballot.** On a `disposal: declared` row the outcome is `world_q.declared_votes`: a count of live
   commits — a verdict by count.
5. **The appeal.** Four arrangement rows carry `appeal_basis: determine`; no verb reads the column, so a
   verdict is final by construction.

Each is a thing that could go either way for the people in the fiction, and each is decided by state
alone.

## The resolution, decided

One roll, one composition (SC-B's terms and `13_SC_tuning_tables.md`'s tables), routed by what exists:
an act against a **person** contests a prize (the prize-row path through `loop/sides.py::sides_of`, so
the counterparty's score, regard and the room are read exactly as for `tell` and `argue`); an act with
**no person against it** takes the graded route (`rosters.yaml: graded_inquiries`, the path `research`
uses: `provider: social_contest`, `module_entry: social_contest.roll`, no prize). No new resolver.

| contest | verb row edit | route | pool (capability key) | obstacle terms (T1 level + …) | bands (writes / emits) |
|---|---|---|---|---|---|
| negotiation | `covenant`: `contests: "a proposition"` | prize, counterparty = the row's `counterparty` | `argue` | `routine` + counterparty's score/2 + **terms' cost** (his pursuits against the uttered terms: `person_q.pursuit_lean` summed over what the terms commit him to, × `proof_step`, the evidence unit) − regard | Overwhelming / Success: `covenant.accepted` (the commit is written as offered); Partial: `covenant.countered` (a counter-offer Proposition at half the concession, his to accept by his own `covenant`); Failure: `covenant.refused` |
| questioning | `interview`: `contests: "a standing"` | prize, counterparty = the witness | `inquiry` | `plain` + witness's score/2 − regard (a friendly witness talks) | Overwhelming / Success: `finding.made` (as today); Partial: `finding.partial` (the claim at half confidence); Failure: `finding.none` |
| docketing | `carry`, `open_case`: graded route | graded, subject = the bench's rung | the actor's `copying` | `routine` + the room's `standard` (T2) − reception (the bench's regard for him) | Overwhelming / Success: the item is docketed (today's write); Partial: docketed at the next sitting (the date one season later); Failure: `case.declined` (nothing docketed; the petition Record stands, so he may carry it again) |
| the ballot | `determine` on a `declared` row | each seated member's ballot is a draw by that member: his `determine`-capability pool against `plain` + the room's standard, with his live commits on the matter (`declared_votes`' own read, per member) as favour (−) or hostility (+) at `proof_step` per commit | that member's | as stated | each ballot's band is his vote: Success+ for, Failure against, Partial abstains; the row's `quorum` counts the fors. The count is arithmetic; each vote is a draw |
| appeal | `determine` with `payload.appeal: <prior disposal>` on a row whose `appeal_basis` is `determine` | prize, as `determine` | the appellant's `copying` | the original row's T1 level + `standard` + **one level** (`routine` → `demanding`: an appeal climbs against a standing verdict) − evidence | Success+: the prior disposal Tenure is closed; Partial: its term is halved; Failure: it stands |

Two rules hold across the table:

- **The draw sets the outcome; the counterparty's choice sets whether there is a contest.** A
  counterparty may still decline to negotiate (not answer), which is his act formed by the chooser; an
  offer once made resolves by the draw. This keeps the person-side decision (CHAR's chooser, AX-2) and
  removes the deterministic acceptance.
- **Evidence and pursuit costs are terms on the draw, never a gate.** The terms' cost and a cited item
  shift the obstacle; neither fixes the band (the standing rule's *"not 'evidence enters when presented'"*).

### Outside this lane, listed for the owning lanes

- The binding acts (`issue`, `confer`, `revoke`, `pardon`, `release`, `surrender`, `establish`): *"a decree
  binds"* is the rule's own case — `audits/14_VERBS_BINDING.md` / the INSTITUTIONS brief.
- `comply`, `evade / defy`, `construe`, `conceal`: `audits/14_VERBS_SOCIAL1.md` / `SOCIAL2.md`.
- SC's played hearing: *present* and *answer* resolve with "no draw: the heavier stands"
  (`audits/05_SC_audit_addendum_B.md` B4.2) and the strike in `05_SC_evidence_and_rebuttal.md`: the SC
  lane's to give a draw (G-65).

## Exact edits, by owner

1. `engine/season/verb_table.yaml`: `covenant` and `interview` gain `contests:` and band-keyed
   `emits_by_degree` / `writes_by_degree` as tabled; `carry` and `open_case` gain band maps; `determine`
   gains the `appeal` operand (`requires_operands`) and the appeal's band map; each row gains its
   `difficulty:` (`13_SC_tuning_tables.md` T1).
2. `engine/season/rosters.yaml`: `graded_inquiries` gains `carry` and `open_case` (the existing route;
   the roster's name is now wider than "inquiries" — renaming it is a separate edit and not proposed
   here); `verb_capability` gains `covenant: argue`, `interview: inquiry`, `carry: copying`,
   `open_case: copying`; new emitted kinds `covenant.accepted`, `covenant.countered`, `covenant.refused`,
   `finding.partial`, `case.declined` on the emitted-kind roster with their WITNESS deposit modes.
3. `engine/season/loop/effects_information.py`: the `covenant`, `carry`, `open_case` and `determine`
   effects read the band (as `_eff_determine` already reads it for `Tenure.degree`); the ballot loop over
   seated members on a `declared` row calls `seam.contest` once per member with that member as actor
   (the per-member generator `H(seed, tick, member, "ballot:<matter>")`, `04 PART D row 35`).
4. `engine/season/queries/world_q.py::declared_votes`: returns each member's commit count (his odds
   operand) instead of the total; the total becomes the count of Success-or-better ballots.
5. No change to `modules/social_contest/roll.py`: every new act is one more record on the one roll.

## Gate (execution artifacts)

- Exact: for each new row, `odds_of` mode (a) on a planted act returns four non-zero-sum bands, and
  no cell of the audit's planted grid gives P(Failure) 0 or 1.
- Realm, `build_realm(0)` and `(1)`, two seasons, `PYTHONHASHSEED=0`: the tap (`realm_tap.py`) shows
  rolls for `interview`, `carry`, `open_case`; `case.declined` and `finding.partial` occur at least once
  across the two seeds; the docket length differs from the base commit (declared mover).
- A planted `declared` sitting of five members with commits 3 for / 2 against, run at 200 seeds: the
  matter carries in some seeds and fails in others (the count is not the verdict).
- Determinism: same seed, same hash, twice.

## Falsifier

Any of the five contest types whose outcome, over 200 seeds of one planted state, takes a single value.

## NERS reading

- **N**: a negotiation that can be won or lost, a witness who may or may not talk, a court that may not
  take the case, a vote that can surprise and a verdict that can be overturned: remove the draw and each
  is a script.
- **R**: the no-player half gains five sources of reversal; every outcome is graded (Partial gives a
  counter-offer, a delayed hearing, a half-finding), so failure is recoverable rather than a dead end.
- **S**: one roll, one ladder, one obstacle composition; the ballot is many draws of the same kind, not a
  second resolver; eligibility stays a check everywhere, as for every other verb.
- **E** (last): five band maps and two routes that already exist, against five contest types that become
  legible as chances with reasons.

## Cost class

Small build per row (data plus four effect bodies); the ballot loop is the one new piece of host code.
Lanes: SC (rows, effects), IN/CORE (rosters), FA (the `declared` rows), FI (`finding.partial`).
