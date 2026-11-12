# PAPACY-B — who fills a Church seat, how the Confessor is chosen, and who may strip a Cardinal

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-15) — the three outcomes this file gives a hold-disposing declared row are the one tally of every `declared` row (carried at the pass mark; undetermined and still docketed when fors exceed againsts short of it; otherwise dismissed and re-petitionable), and the kind emitted by the middle outcome is `matter.undetermined` (`election.inconclusive` is not added). Each member's ballot also carries `obligation`, `regard` and `evidence` as terms, scaled under a sealed room, per `15_INSTITUTIONS_VENICE_A_obligation_and_the_ask.md`. `patronage:`, `patronage_bases`, `conclave` and `quorum_share` stand as written and are the kit's. Every finding below stands.

## Status: PROPOSED (item 4, `head_of_faction`, is held for Jordan: it overwrites a ruling of 2026-10-11)

Source: `audits/15_INSTITUTIONS_PAPACY.md` F-PAP-02, F-PAP-03, F-PAP-09; §6 rows P-1, P-2, P-9; §12 R-2,
R-3, R-6, R-9; §13 items 1 and 3. Composes on CR-35 (the `election` gate arm, the `hold` disposal, the
electorate), on `audits/14_VERBS_BINDING.md` §0.2 (the `confer` and `revoke` draws) and on the SC
obstacle (`05_SC_obstacle_difficulty_and_modifiers_B.md`). Batch 2.

## What it changes in `engine/season/` at runtime

1. A seat row may declare `patronage:`. With no row declaring it, nothing moves (hash EQUAL). With the
   seven Church rows declaring `own_faction`, a Crown or Löwenritter seat's `confer` on a Church seat is
   refused at `may_fill`, and the Confessor's is admitted wherever the seat stands. A declared mover for
   `confer` formation on those seats (`world_q.vacancies` stops offering them to seats that may not fill).
2. A `conclave` arrangement row. Hand-built until a computed docket names a row (CR-35's own REACH note).
3. A declared row may state its pass mark as a share of the ballots cast (`quorum_share`) instead of a
   head count (`quorum`), and a hold-disposing declared row grades the count into three outcomes. The
   ballot itself (each seated member's vote a draw, his commits its odds) is the SC lane's
   (`13_SC_draw_for_unrolled_contests.md`, row "the ballot"; determinism sweep C-14) and is not redone
   here. A declared mover wherever a declared determination executes (in the realm today: none).
4. Held: a third `revocation_bases` member.

## The problem (evidence)

- `state/gate.py::may_fill` (`:845-866`) asks purview and nothing about faction. At `build_realm(0)`
  (audit E-2) `off_king` and `off_widow_regent` may fill all six Himmelenger seats and fourteen Crown and
  Löwenritter seats may fill `off_archbishops_rep`; no Church seat may. CR-35 refuses the King's `confer`
  on `off_confessor` (an `elected` row) and leaves the six `appointed` rows as they are.
- No election exists: `off_confessor` is `elected` and `rosters.yaml: conferral_bases`' note says no act
  fills an elected seat. CR-35 builds the act with `quorum: 1`.
- `queries/world_q.py::declared_votes` (`:737-763`) returns a count; `determine`'s `vote` conjunct refuses
  below `quorum` and the count is then read by nothing. A bench at exactly quorum and a unanimous bench
  roll the same odds. Under the standing rule (*"no fixed rule decides a result by itself"*) the gate may
  decide only whether the act can be attempted.
- `may_revoke` is empty for all seven Church seats (E-2); NPC-038's `core` need is removal on exposure
  (FA audit §11 item 3).

## The resolution, decided

### 1. `patronage:` — the right of appointment as data on the seat

A closed roster `patronage_bases` and an optional seat key naming a **list** of its members. A seat may be
filled through a seat that satisfies **any** listed basis:

| member | rule (in `state/gate.py`, one owner, refused at import if a member has no rule) |
|---|---|
| `purview` | today's rule: `purview_reaches(via, off.rung)` |
| `own_faction` | `seat_faction(via) == faction_prop_id(off.faction)` (the seat exercised belongs to the faction the filled seat belongs to); no purview walk |

Absent key = `[purview]`, so every existing row keeps today's behaviour. `inheritance` and (after CR-35)
`elected` rows are untouched: `FILLED_BY` already takes them out of `confer`.

Content: the six `appointed` Himmelenger rows and `off_archbishops_rep` declare `patronage: [own_faction]`.
A see on ducal ground (PAPACY-E) declares `[purview, own_faction]`: the lord and the Confessor may each
fill it, each by the `confer` draw, each displacing the other's man with the incumbent as `opposition`
(the verb lane's shape). That is the investiture contest, as a standing feature of the row, not a rule.

### 2. `conclave` — the Church's election row

CR-35's `election` row specialised by data (a second row, not a second mechanism):

```yaml
  - id:               conclave
    disposal:          declared
    quorum_share:       [2, 3]      # NEW KEY, declared rows only: see 3
    bench_basis:        determine
    floor:              closed
    records_dissent:    true
    venue_min_rank:     settlement
    term_required:      false
    appeal_basis:       none
    interposed:         [procedure, ceremony]
    order:              rank
    proofs:             []          # an election hears no proofs: it reads the vote
    disposes:           hold
    disposal_reach:      realm
    standard:           demanding   # SC T2's key, when it lands
```

`[ASSUMPTION; medium; Jordan to correct; revert: the Confessor is elected under CR-35's generic
`election` row.]`

### 3. The ballot is drawn (SC's); the pass mark is a share; the count is graded

- **The ballot** is `13_SC_draw_for_unrolled_contests.md`'s: on a declared row each seated member's ballot
  is his own draw (his `determine` pool against `plain` plus the room's `standard`, his live commits on
  the matter as favour or hostility); Success or better is a vote for, Failure against, Partial an
  abstention. A committed elector usually votes as he committed and sometimes does not. This proposal
  adds nothing to it.
- **The pass mark as a share.** A declared row carries `quorum: <int>` (today) **or** `quorum_share:
  [n, d]`: the fors must be at least `n/d` of the ballots cast for or against (abstentions are not cast).
  A share survives a bench that shrinks through death or grows through new sees; a head count does not.
  The count is arithmetic on draws.
- **Three outcomes on a hold-disposing declared row** (an election), so that a narrow result is neither a
  win nor a dead end:

  | the count | outcome |
  |---|---|
  | fors ≥ `n/d` of ballots cast | the candidate holds the seat (CR-35's `hold` disposal); the division is recorded where `records_dissent` |
  | fors a simple majority, short of `n/d` | no election; the candidacy **stays on the docket** for the next sitting (the scrutiny was inconclusive); emits `election.inconclusive` |
  | fors not a majority | the candidacy is dismissed (SC-P6's `matter.dismissed`); he may petition again; other petitions stand |

- **Who is on the bench** is CR-35's (the live seats of the vacant seat's faction whose grant carries
  `determine`). `[ASSUMPTION; Jordan to correct: only electors present at the sitting's venue cast a
  ballot, so staying away is a way to withhold a vote; revert: every elector casts wherever he is.]`
- **What the vacancy costs** is not a counter: while the head seat is empty nobody exercises its `confer`,
  `revoke` or its bench, so the Church's own vacancies stay open and its sentences cannot be absolved.

### 4. (HELD) `head_of_faction`

`rosters.yaml: revocation_bases` gains `head_of_faction`; `REVOCATION_RULES["head_of_faction"]`: the seat
exercised is the `head_seat` of the faction the stripped seat belongs to. The six `appointed` Himmelenger
rows and `off_archbishops_rep` change `revocation: null → head_of_faction`. The strip is the verb lane's
`revoke` draw (the holder is the opposition; Failure: he holds, `revocation.resisted`). `off_confessor`
stays `null` (audit §13 item 2).

## Exact edits

1. `engine/season/rosters.yaml`: new roster after `binds_bases`:
   `patronage_bases: {open: false, values: [purview, own_faction], source: "PAPACY-B", note: "WHO MAY
   FILL A SEAT FOR SOMEBODY ELSE -- the seat's fourth rostered basis. The rule is behaviour and lives in
   state/gate.py::PATRONAGE_RULES."}`
2. `engine/season/state/carriers.py::Office`: field `patronage: tuple = ("purview",)`; `__post_init__`
   refuses a member off the roster (the `conferral` refusal's shape).
3. `engine/season/state/gate.py`: `PATRONAGE_RULES = {"purview": …, "own_faction": …}` with an import-time
   totality check beside `check_filled_by`; `may_fill`'s last line becomes
   `return any(PATRONAGE_RULES[b](w, w.offices[via], off) for b in off.patronage)`.
4. `engine/season/harness/populated.py::build_realm`: the seat overlay passes a row's `patronage:`.
5. `engine/season/offices.yaml`: `patronage: [own_faction]` on `off_cardinal_fortitude`, `…_justice`,
   `…_prudence`, `…_temperance`, `off_senior_inquisitor`, `off_archbishops_rep`.
6. `engine/season/arrangements.yaml`: the `conclave` row; `data/arrangements.py`: `quorum_share` added to
   `_ARRANGEMENT_KEYS` (the key-count test is re-recorded and says why), validated as two positive ints
   `n <= d`, lawful only on `disposal: declared`, exclusive with `quorum`.
7. `engine/season/loop/effects_information.py` (the ballot loop `13_SC_draw_for_unrolled_contests.md`
   edit 3 adds): the pass test reads the row's `quorum` (fors ≥ the integer) or `quorum_share`
   (`fors * d >= n * (fors + againsts)`); for a row whose `disposes:` is `hold` it applies the
   three-outcome table. `verb_table.yaml: determine` gains the emitted kind `election.inconclusive`.
8. `engine/season/arrangements.yaml: excommunication_deliberation`: `quorum: 2` → `quorum_share: [2, 3]`
   `[ASSUMPTION; revert: quorum: 2]`.
9. (HELD) the `head_of_faction` roster member, rule and seven row values.

## Gate

Hand-built, real fold, `PYTHONHASHSEED=0`:

- `patronage`: the King's `confer` on a vacated `off_cardinal_prudence` → refused at `may_fill`; the
  Confessor's → admitted and rolled. With the key deleted from the row the King's is admitted (control).
- Election (after the SC ballot lands): four electors, the Confessor's seat vacated, one candidate's
  petition docketed under `conclave`. Arm B: three electors committed for, none against. Arm C: two for,
  two against. Each over 200 seeds: all three outcomes of the table occur in at least one arm; P(seat
  opened) is higher in B than in C; neither is 0 or 1. The exact probability of each outcome is printed
  from the per-ballot odds (no sampling claim rests on the 200).
- Share against head count: the same bench with one elector removed: under `quorum_share: [2, 3]` the
  pass mark moves with the bench; under `quorum: 3` it does not (control).
- Realm control: `build_realm(0)` one and two seasons, base hash, with no row declaring `patronage` and
  the `conclave` row absent.

## Falsifier

Arms B and C giving the same outcome distribution (the commits would not be setting the odds). An
election decided the same way in every seed for a given set of commits. A seat declaring `[own_faction]`
filled through a seat of another faction. An inconclusive candidacy that leaves the docket.

## NERS reading

N: cut `patronage` and the Church is a royal department (today) or, with a blanket same-faction rule, no
lord can ever invest a bishop; cut the share and a conclave's pass mark is wrong the day a Cardinal dies;
cut the middle outcome and a near-miss is the same as a rout. R: a player who is an elector chooses whom
to commit to and when to move the election; a candidate canvasses commits by `argue`; a faction with more
than a third of the bench can keep the chair empty and pays for it. With no player the arms each back
their own. S: one `may_fill`, the SC lane's one ballot, the SC obstacle unchanged; `quorum_share` and
`quorum` are one pass test in two units. E (last): one seat key, one arrangement key, one row, against
the investiture contest, the long vacancy and the contested election they buy.

## Cost class

Small build (1-8). Item 9: edit, after Jordan.
