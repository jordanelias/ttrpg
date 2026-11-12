# HAPPENINGS-B — the throne is never stranded: the two royal dignities get a basis, and more than one title may claim

## Status: PROPOSED

Source: `audits/22_HAPPENINGS.md` §1.5 rows 9 and 10; F-PES-FA-01, F-PES-FA-11 (`audits/16_PESSIMIST_FA.md`);
F-PES-GAME-08. Lane FA (owners: `offices.yaml`, `rosters.yaml: successions`, `state/gate.py`).
Reference only (`CLAUDE.md` §0.05).
Binds on, and does not redo: `14_VERBS_BINDING_C_turnover.md` (VB-C: `succeed` is a draw; Partial is a
provisional hold), `15_INSTITUTIONS_BYZANTINE_E_accession_recall_and_the_crowd.md` (the claim's odds: the
title and the deed presumption as terms; a step against the claimant per living rival),
`15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md` (the founders' deeds; Hafenmark's heir title),
`16_PESSIMIST_FA_A_dismissal_survives_the_king.md` edit 1 (Valorsmark passes with the crown),
`06_FA_remit_grant_by_row.md` R-16 (the consort's remit is empty while the King lives).

## What it changes in `engine/season/` at runtime

1. The Queen's and the Princess's seats can be refilled (today: by nothing, ever).
2. A vacant inherited seat may be claimed by the holder of **any** title its `successions` row lists, not
   one. Each claim is VB-C's draw. The list is who may try; it is not an order and gives no one the seat.
3. With the King and the heir both dead, the throne is still claimable: by the consort, and by the heads
   of the two houses founded with the crown.

Movers: none at build (no seat is vacant). After a royal death: `succeed` forms for more persons, a
declared mover of any run that contains one.

## The problem (evidence, cited)

- `offices.yaml:245, 271`: `off_widow_regent` (post "Queen") and `off_princess` are `conferral: null`.
  `state/gate.py::FILLED_BY[None]` is the empty set: nothing fills them. The Princess's row's own source
  line calls it *"one of the two Royal Family succession seats"*; no succession reads it.
- `rosters.yaml: successions` is `{off_king: off_heir}`; its note: *"one title deep (the heir's own title,
  closed by his claim, passes to nobody)"*.
- This lane's run (`runs/HAPPEN/king_2.json`): at seed 2 the King dies in the fourth season by his
  Spymaster's `capture`; `off_king` and `off_duke_valorsmark` close. The duchy is then fillable by nothing.
- F-PES-GAME-08, premise 2.1 link 8 (run `x2b_death_detail.py 0 1 4 p_npc_020,p_npc_031`): with the King
  and the Prince dead *"the throne, the duchy and the heir's seat stay vacant for all four seasons …
  the realm does not notice it has no King"*.
- F-PES-FA-11: the FA lane's R-16 empties the consort's remit while the King lives, which removes the
  only other seat able to name an heir; *"with King and heir dead nobody is ever King"*. It asks for a
  fallback and writes none.
- The standing rule names *"the ruled-in `succession` rules wherever the tree resolves an heir by a fixed
  order"* as a case to repair. One title deep with a certain claim is the fixed order of length one.

## The resolution, decided

| # | decision | ladder step |
|---|---|---|
| 1 | The Queen's and the Princess's seats are **titles conferred by the Crown**: `conferral: appointed`, `off_heir`'s shape. A consort is made by a marriage and a princess is recognised; both are acts of the throne, and both titles end with their holder | 4 (`off_heir`, v10 IN-61: *"the heir is a TITLE, designated by an ordinary `confer`"*) |
| 2 | A `successions` value is a **set of titles**, any of whose holders may claim. Eligibility only (`AUDIT_BRIEF.md`: *"eligibility … checks that decide whether an act may be attempted at all"* are not outcomes). Who gets the seat is the draw | 5; 3 for the reading of RS-27 (*"the heir still has to claim"* is silent on who else may) |
| 3 | The throne's set: the heir, the consort, the Princess, and the heads of Hafenmark and Varfell. This is Jordan's fixed point in data: the crown and the two houses were won together, in an order of accomplishment, so when the royal line fails the houses are the claimants. The **order is not written here**: it enters each claim's odds through the founders' deeds (SYN-B) as BYZ-E's presumption term | 3 (`INSTITUTIONS_BRIEF.md`, Jordan 2026-11-12) |
| 4 | A regency is not a new mechanism: it is the consort's claim landing at Partial, which VB-C already makes a termed, provisional hold | 4 (VB-C's Partial) |

## Exact edits, by owner

**1. `engine/season/offices.yaml`.** `off_widow_regent`: `conferral: null` → `appointed`; `revocation:`
stays `null`. `off_princess`: the same. Note on each: *"a title of the royal house, conferred through
`off_king` (`off_heir`'s shape, IN-61); HAPPENINGS-B."* `[ASSUMPTION; medium; Jordan to correct; revert:
null]`. No other key changes; R-16's remit edit is the FA lane's and composes.

**2. `engine/season/rosters.yaml: successions`.** The value shape becomes `{seat: [title, …]}`:

```yaml
values:
  off_king: [off_heir, off_widow_regent, off_princess, off_duchess_hafenmark, off_duke_varfell]
```

and, when PES-FA-A edit 1 and SYN-B edit 6 land, their rows in the same shape
(`off_duke_valorsmark: [off_heir]`; `off_duchess_hafenmark: [off_heir_hafenmark]`). The note's sentence
*"one title per seat"* becomes *"the titles whose holders may claim it; a list is eligibility, never an
order (HAPPENINGS-B)"*. `[ASSUMPTION; medium; Jordan to correct; revert: the single title]`.

**3. The loader and the seven readers of `SUCCESSIONS`, one meaning each** (eight sites, by grep at HEAD):

| site | today | becomes |
|---|---|---|
| `data/rosters.py:882` | `{str: str}` | `{str: tuple[str, …]}`; a bare string is read as a one-tuple, so the present row loads unchanged |
| `state/gate.py:743` (`has_filler`) | key present | unchanged |
| `state/gate.py:752-758` (`check_successions`) | value is a row id | every member is a row id; an empty list refuses |
| `state/gate.py:782` (`may_claim`) | the claimant holds *the* title | the claimant holds a title in the tuple `[UNVERIFIED: the body was read by grep, not opened]` |
| `state/gate.py:794` (`claimable_seats`) | seats whose title is his | seats one of whose titles is his |
| `decision/options.py:240` (`own_title_declines`) | `SUCCESSIONS.get(r) in held` | `any(t in held for t in SUCCESSIONS.get(r, ()))` |
| `loop/effects_governance.py:164` (`_eff_succeed`) | closes *the* title | closes the title the claimant claimed through, and only if it is a title that exists to pass a seat (`conferral: appointed`, empty remit). A duke who takes the throne keeps his duchy |
| `queries/world_q.py:3177` (`heir_title` tie) | the holders of the title | the holders of any listed title, in list order for the offer only |

**4. Request to VB-C and BYZ-E (not edited there).** BYZ-E's `favourable` term *"the claimant holds the
seat's `successions` title"* reads **the first listed title** as the designated one; holding a later one
earns no step. Its `hostile` term (*"one step per other person eligible to claim the same seat who is
alive"*) then has persons to count. That is the whole of how the heir is favoured and not certain.

## Gate (execution artifacts)

`engine/season/tests/test_in61_heir_hears_vacancy.py` (the file covering the claim), on the built realm
with the deaths planted through `_die`:

- **G1** King dead, heir alive, VB-C on, 40 seeds: the heir holds the throne at the end of four seasons
  in most seeds **and not in all**; in at least one seed another listed title's holder does, or the hold
  is provisional.
- **G2** King and heir dead, 40 seeds: the throne is held (fully or provisionally) at the end of four
  seasons in at least one seed and vacant in at least one. Today: vacant in all.
- **G3** the Queen's seat, vacated: a `confer` through `off_king` opens it. Today: `confer.refused`.
- Control: with the single-title row and VB-C off, G1 reads today's certain claim and G2 today's vacancy.

## Falsifier

Revert edit 2: G2 reads vacant at every seed. Pin `succeed` to Success: G1 reads the heir at every seed
and fails its *"not in all"*. Name a title id the offices file lacks: the import refuses.

## What it does not do

It does not write the claim's odds (VB-C, BYZ-E), seed the deeds that rank the houses (SYN-B), make
anyone want the throne (the chooser), or decide a minority. It does not rename `off_widow_regent`, whose
id describes a state the seat is not in while the King lives; the rename is churn across pins and is
left with FA.

## NERS reading

- **N.** Cut it and one death in the right place ends governance for the rest of the run. Top-down it is
  the fixed point's houses made claimants; bottom-up it is one roster value and its seven readers;
  laterally it is the Church's and Varfell's elections' sibling (a set of electors there, a set of
  claimants here).
- **R.** A succession with several possible winners is a strategy problem for a player in any of five
  seats, and a crisis the world produces unwatched. Complete at the extreme: every listed title vacant
  is the one case still stranded, and it takes five deaths.
- **S.** No new verb, basis or band; the list rides the claim's existing draw.
- **E, last.** Two row values and one roster shape.

## Cost class

Edit (data) plus one small build (the tuple at seven sites). Lands after VB-C's C3; edit 1 may land
alone at any time.
