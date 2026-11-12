# FA-B3 — which seats end on a clock: terms by body, from the design's own tenure rules; and the two heads the roster omits

Reconciled: 2026-11-12, U5d closure — folded **A-36**, **A-35** and **A-15**. Edit 3's sentence for CR-37 ("deposition is the turnover of a life seat") excludes the Confessor: nobody judges him, so his seat ends by death or resignation only and no deposition occasion is offered for `off_confessor`. Every other Church officer's turnover is the head's strip by a resistible draw (A-35; `15_INSTITUTIONS_PAPACY_B_patronage_election_discipline.md` item 4, un-held); the Löwenritter stay unstrippable until edit 4's `head_seat` row for `off_grand_master` lands, after which the same basis reaches them. A-15 makes "emptied by death" a live route for the life seats, so this file's rule (a term only where the body rotates) no longer leaves them permanent.

## Status: PROPOSED

Source: `audits/06_FA_audit_addendum_B.md` C-6, F-FA-16, §B6.1 R-25, R-26; evidence E-B1, E-B2.
**Supersedes, in content only,** the first authoring named in `06_FA_seat_terms_and_turnover.md` ("the
eight `elected` rows at `term: 8`"). That file's mechanism (a `term:` key on an `offices.yaml` row,
read by `_eff_confer`; a malformed term refused; a ban scoped to its seat) is unchanged and is this
file's dependency.

## What it changes in `engine/season/` at runtime

1. Once the first lane's mechanism lands: three seat rows carry a term, not eight. A termed seat's
   `hold` matures at MATTER and the seat falls vacant; the others end by death, release, revocation or
   the removal by a body the plan schedules (CR-35, CR-37).
2. `faction_q.head` answers for two more factions (the Löwenritter and the Restoration Movement).
   This moves any run in which a `survey` of either executes (the `faction_sheet` Record copies the
   view), a declared mover.

## The problem (evidence)

- The eight `elected` rows of `offices.yaml` (addendum E-B2): `off_duke_varfell`, `off_confessor`,
  `off_commune_rep_hm`, `off_guild_comptroller`, `off_senior_jarl_west`, `off_skald_chief`,
  `off_military_jarl`, `off_restoration_leader`.
- What the archived design says of each seat's tenure (intent and vocabulary only, `CLAUDE.md` §0.05):

| seat | design's tenure | where |
|---|---|---|
| Confessor | elected by the College; holds until death, incapacity or a crisis of faith; the College may depose after a crisis | `faction_politics_v30` §1.4 Standing 7, §1.4c; Part 6 §6.2 |
| Duke of Varfell | first among the Jarls; removed by an incapacity assessment (three of five Senior Jarls), reinstated if he recovers | §1.3 Standing 7; §1.3a |
| Senior Jarl of the West, Military Jarl | raised on a vacancy or by agreement of the region; voted out only by the Assembly ("rare — requires unanimity minus one") | §1.3 Standing 5 and 6 |
| Skald-Chief | keeper of the oral law; his death is "a secondary succession crisis" | §1.3c |
| Guild Comptroller | sits on a rotating Guildmaster Council; "no single leader … a collective by design" | `factions_personal_v30` §8.6; `faction_politics_v30` §2.5 |
| Commune Representative | not described; the Hafenmark ladder's council seats are held by vote and lost by a vote of no confidence | §1.2 Standing 3 |
| Restoration Leader | "No formal leader — a movement" | `factions_personal_v30` §8.8 |

- So a blanket term on the elected rows would empty the Confessor's and the Duke of Varfell's seats
  every two years, which no layer of the design intends, while the one body the design does rotate has
  two seats.
- `rosters.yaml: factions.head_seat` (`:2062-2066`) names four seats. At `build_realm(0)` the view's
  `head` is `None` for five of ten factions (addendum E-B1). Two of the five have an authored seat that
  is plainly the head's: `off_grand_master` and `off_restoration_leader` (E-B2).

## The resolution, decided

Ladder step 3 (answered by a design document, for intent; the code owner is the row): **a seat ends on
a clock only where its body rotates.** Everywhere else the design's turnover is removal by the body
that seated the holder, and that is already owned (CR-35 the election arm, CR-37 deposition) or is the
recall of the first lane's `06_FA_decree_binds.md`.

The unit is the design's own: a year of four seasons (the "year-arc" of every ladder obligation; the
annual Assembly; the annual renewal of an alliance or an embargo). No source gives a term length, so
the number is an assumption with a sweep.

## Exact edits, by owner

**1. `engine/season/offices.yaml`** (the one owner of a seat's standing facts), after the first lane's
edits 1 to 5 have landed:

- `off_guild_comptroller`: `term: 4`.
- the Guild leader's row, if the first lane's `06_FA_remit_grant_by_row.md` authors it
  (`off_guild_leader`): `term: 4`.
- `off_commune_rep_hm`: `term: 4` `[ASSUMPTION; medium; Jordan to correct; revert: null — the design
  does not describe this post]`.
- every other row: no `term:` key. A comment on the eight `elected` rows' header states the rule: a
  term is authored only on a seat whose body rotates.

Each value `[ASSUMPTION; medium; Jordan to correct; revert: no `term:` keys]`, swept `{4, 8}`.

**2. Nothing in code.** The loader, `Office.term`, `_eff_confer` and `_req_confer` are the first
lane's.

**3. The plan (owner: the plan), one sentence on CR-37's entry:** deposition is the turnover of a life
seat, and its first occasions are the three the design names for Varfell (§1.3a): a holder absent from
his body's sittings, a holder in custody, a holder whose seat's writs go unanswered. Each is a fact
the tree can already read (`sittings_before`, `restrained`, the first lane's addressed-writ reader);
none is built here.

**4. `engine/season/rosters.yaml: factions.head_seat`** (the one owner of whose holder heads a
faction): add `"Löwenritter": off_grand_master` and `"Restoration Movement": off_restoration_leader`.
Add a `headless:` note naming the Guilds as headless by design (a council) and Altonia and Schoenland
as WR's content. `data/rosters.py` already refuses a seat id the offices file lacks
[UNVERIFIED: that the loader checks membership; if it does not, the check is one line beside
`OFFICES_REMIT_UNRULED`'s].

## Gate (execution artifact)

- Realm, seeds 0 to 2, twelve seasons, with the first lane's mechanism: `term.matured` on the Guild
  seat's `hold` at least twice per seed; the count of `tenure.opened` on that seat afterwards read and
  reported (it may be 0 until `confer` is chosen for a reason; the first lane's `06_FA_office_capabilities.md`
  and the vacancy occasion are what move it). No `term.matured` on the Confessor's, the Duke of
  Varfell's or a Jarl's `hold` in any run.
- `build_probe.py` (addendum E-B1) re-run: `head` is a person for the Löwenritter and the Restoration
  Movement and still `None` for the Guilds.

## Falsifier

- Control: with no `term:` key the twelve-season hash equals the pre-item hash.
- A life seat that matures: the gate's second sentence, read on every seed.
- Mutation for edit 4: name a seat id the offices file lacks and the load fails.

## What it does not do

It does not make the realm's cast turn over. Three termed seats in one body are a small generator; the
first audit's finding that power does not change hands (F-FA-02) is answered mostly by the recall and
by removal by a body, which this file points at and does not build. It authors no rotation for
Parliament, because the tree seats no parliament (addendum §B3.2).

## NERS reading

- **N.** Top-down, a ruler's seat does not expire under him. Bottom-up, a guild's officers are
  returned or replaced on a year. Laterally, the Church and Varfell keep the tenure their own
  succession designs assume. Remove it and either nothing rotates or everything does.
- **R.** Customizable by one key on a row; the difference between a collective and a monarchy becomes
  visible in who is still in office after three years. Complete at the extreme: a faction with no
  termed seat is exactly today's.
- **S.** One clock (`Tenure.term`, MATTER), the one sworn service already uses.
- **E, last.** Three data values and two roster lines.

## Cost class

Edit (data). Two declared movers (the termed rows; `head_seat`). Depends on
`06_FA_seat_terms_and_turnover.md`.
