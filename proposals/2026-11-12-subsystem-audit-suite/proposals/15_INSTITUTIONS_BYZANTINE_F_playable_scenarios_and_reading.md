# INST-BYZ-F — two playable scenarios on the one runner, the digest lines that make them legible, and the band reading

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-04, X-22, X-30, X-32) — a scenario is a case file (a delta on a base, its set-up acts in `setup.prehistory` folded under the pinned roll), played by FA's runner and read by one report (`15_INSTITUTIONS_SYNTHESIS_D_first_playable.md` §1): `roga` and `chancery` are case files with `base: spine`, not situations written in `governance_spine.py`; this file's seven digest lines and `bands=N` are lines and an option of `harness/institution.py`; the `roll` line reads `certificates`; stores are in `default_store_kind`; the control arms are `task_draw_arm` and the pinned roll, not `procedure_draws`. The two scenarios, their endings and their gates stand, and `roga` on the realm is the first cut of the integrated playable. Every finding below stands.

Re-grounded: 2026-11-12 (audit §18) — the scenarios do not change; the report gains five readings, each with the condition under which it fails (`15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md` item 3): who stayed away, what the hand took, the servant after the reign, what he kept, the lord who outgrew his minister. Two nulls are recorded for this file's premise: of the four policy and court sims the tree verified, none rolls a governance act to fail except partly one (`research/game_precedent_suite/tables/R9_policy_court_sims.md:8-18`), so the drawn court has no shipped precedent; the stipend by title does (`tutorials/T13_koei.md:78`).

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_BYZANTINE.md` §10, §13; the standing requirement of `AUDIT_BRIEF.md`
(each subsystem playable alone, one code path, integrated). Batch F. **Extends**
`06_FA_playable_scenario.md` (FA-P4: `play`, `situation`, `digest`, `offered` in
`harness/governance_spine.py`) and `06_FA_shortest_loop_B.md`; it edits neither and adds no runner.
Depends on proposals A and B for `roga`, C for `chancery`. Ratifies nothing.

## What it changes in `engine/season/` at runtime

Nothing on the game path. Two situations, seven digest lines, two end conditions and one option on
the instrument FA-P4 turns into a scenario runner. No file under `loop/`, `state/`, `queries/`,
`decision/` or `data/` changes; a run's `content_hash` equals the same seasons run through
`populated.run` with the same chooser (FA-P4's control, unchanged).

## The problem (evidence)

- Nothing lets a player enter the court, the fisc or the chancery and face a choice (FA audit
  F-FA-07: "there is no FA scenario, digest or end condition"). FA-P4 supplies three situations
  (`vacancy`, `order`, `succession`) and FA-B4 a fourth (`recall`); none turns on money owed or on a
  paper waiting.
- No instrument prints who is owed what, which terms matured, which papers sit in whose hand, or how
  a drawn procedure came out. `aperture` prints a funnel per verb (formed, attempted, executed,
  refused) and no bands.
- The standing rule makes every reading of a procedure a distribution. One seed is a trajectory
  (`CLAUDE.md` §0.1 pt 4).

## The resolution, decided

Ladder step 5: the pieces are FA-P4's; a second runner would be the second code path the standing
requirement forbids. Each situation is made at tick 0 by the game's own effects through the gate,
never by a branch on an id, so the scenario plays a world the loop can produce (FA audit §9's stated
risk). Set-up acts resolve under `procedure_draws: off` so the situation is the same at every seed;
play resolves under `on`.

## Exact edits (all in `engine/season/harness/governance_spine.py`)

**1. `situation("roga")`.** On `build(seed)`'s thirteen seats, with the player at `lr_realm`'s seat:

| set-up act (in order) | by | makes |
|---|---|---|
| `establish` × 4 at the realm rung, rows `dignity: 4, 3, 3, 2`, `upkeep: 3, 2, 2, 1`, `body: null`, faction `faction x` | the Sovereign's seat | four dignity seats |
| `transfer` of 1 unit of `coin` from his hearth to the realm rung, then `oblige` to the Sovereign's seat | each of the two Dukes | two real deeds (`transfer.made`) the Sovereign holds claims of; two termed oaths (`oblige_term`: mature in season 4) |
| `transfer` of 2 units of `coin` to the realm rung, and no oath | the Count of chain `a` | a larger deed that no dignity cites, by a man not sworn |
| `confer` of the grade-4 and one grade-3 seat, each citing that Duke's gift | the Sovereign's seat | two dignities held, two vacant |
| stores | the three gifts; the builder's endowment for the duchies | the realm rung holds 4 against a first-year bill of 5; each duchy rung holds 6 |

`[UNVERIFIED]` that `_req_establish` accepts the two new row keys as founding operands (a computed
`establish` "carries no operands today", `offices.yaml:79`; `06_FA_office_capabilities.md` moves
founding content to data). If it does not, the four rows are authored in `governance_spine.yaml`
under a `dignities:` list the builder mints, which is data and no branch. `[UNVERIFIED]` that a
spine person's hearth holds `coin` to give; if not, the endowment seeds it.

*What the player is shown each season* (FA-P4's `offered`, grouped by remit act, plus the digest):
the bill and when it falls; the fisc; each sworn man, his grade, his term's maturity and his regard
as the player's own ledger gives it; the persons whose deeds the player holds and who hold no
dignity; the candidates `requisition` (per duchy, with the amount his shortfall claim names),
`transfer` (per payee), `confer` (per vacant row and known deed).

**2. `situation("chancery")`.** The spine has no body. One `office_bodies` member is needed for a
hand; `faction x`'s fixture cannot invent one (`governance_spine.yaml`'s own header: an invented
body "FORGES canon"). So the hand is a seat (proposal C, edit 1): the Sovereign's row gains
`passes_through: [{seat: lo_territory_a}]` in the situation's world, and the player is the Lord of
chain `a`. Set-up: the Sovereign `issue`s three writs at tick 0 (to the Count of `a`, the Count of
`b`, and the Mayor of `a`); the Mayor of `a` files a `petition` addressed to the Sovereign.

*Shown:* each paper in his hand, its maker, its addressee, its terms, its age and the season it
returns; his scene budget. *Chosen:* which to `carry` (a draw each), which to leave.

**3. `digest` gains seven lines**, each read off `w.log`, `w.tenures`, `w.records` and `Rung.stores`
for the season, in FA-P4's reader:

```
fisc        <rung>: coin 2 · bill due this year 5 · shortfall 3
sworn       renewed 1 · matured 1 · live 3            (per paying seat)
collected   rendered 0 · taken 1 · partial 1 · resisted 0   (per place)
dignities   held 2 of 4 · conferred 1 · declined 0 · provisional 0
hands       entered 2 · held over 1 · returned by a clerk 0 · returned by the clock 1   (per body or seat; busiest hand 0.67)
roll        entries 3 (+0)
accession   claimed 0 · unrecognised 0 · provisional 0 ;  recall  closed 0 · defied 0
```

A line whose subject does not exist in the world is omitted (the spine has no Roll).

**4. Two end conditions**, each a Query over Tenures, beside FA-P4's three:

- `court_lapsed`: of the terms ever sworn to the player's seat, more than half have matured unpaid.
- `court_kept`: the season count is reached and none has.

**5. `play(..., bands=N)`.** With the auto chooser and `bands=N`, the scenario is run at seeds
`0..N-1` in both arms of `procedure_draws`, and for each drawn verb (`confer`, `revoke`, `carry`,
`requisition`, `succeed`) the frequency of each band is printed beside the control arm's. It asserts
nothing: it is a reading, and it is the only place this suite's gates take a rate from. No test file
is added for it (§0.1 pt 5: the instrument's subject is the game's draws, and its output is read by
a person deciding a tuning value).

## Gate (execution artifacts)

1. A scripted callback that pays nobody ends `roga` on `court_lapsed`; one that taxes both duchies
   each season until paid ends it on `court_kept` at some seeds and not at others (collection is
   drawn), and the seeds are reported; the auto chooser prints a non-empty digest in every season.
2. A scripted callback that carries nothing ends `chancery` with every writ returned by the clock
   and, where the Sovereign's `revoke` then forms and draws Success, on FA-B4's recall; one that
   carries everything it can shows entered, held-over and returned papers across seeds.
3. `content_hash` after eight seasons of `roga` under the auto chooser equals the same world run
   through `populated.run` with the same chooser.
4. `play("roga", bands=200)`: for `requisition` and `confer`, no band is empty and none exceeds 0.9
   in the `on` arm; the `off` arm is a single band.

## Falsifier

Remove the stipend rows' `upkeep`: the `fisc` line's bill reads the default and `court_lapsed` is
unreachable at the scripted non-payer if the default is 0; the scenario then has no stakes, which the
gate reports as a failure. Plant a situation built by direct assignment (a `hold` appended without
the gate): gate 3's hash comparison fails.

## The standing requirement, point by point

| point | `roga` | `chancery` |
|---|---|---|
| a situation | a bill larger than the fisc, a year to meet it, a deed unhonoured | papers in hand, more than a budget covers |
| real choices | whom to tax, whom to pay, whom to honour | which to enter, which to leave |
| choices change what happens | terms renew or mature; places remember | orders become answerable, return, or lapse |
| consequences | a matured oath takes a man and his people out of the seat's purview | the issuer's regard, then his recall |
| an ending | `court_lapsed`, `court_kept`, FA's three | recalled, kept, FA's three |
| one code path | the season loop on the spine through `play_surface` | the same |
| integrates | `requisition`, `transfer`, `confer`, `oblige`: the loop's own writes | `issue`, `carry`, FA's three answers |
| no GM | the bill, the bands and the endings are Queries | the same |

## NERS

N: without a scenario the court is not a game (the standing requirement); without the digest its
outcomes are not legible; without the band reading no gate on a draw is a measurement. R: both
scenarios turn on a choice under scarcity; both run with no player (the control arm). S: one runner,
one digest reader. E, against that: two situations, seven lines, two Queries, one option.

## Cost class

Small build, harness only.
