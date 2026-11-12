# PAPACY-B — who fills a Church seat, how the Confessor is chosen, and who may strip a Cardinal

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
3. Under a `declared` row the vote stops being a pass mark. The check becomes *can the body sit*; the
   share of the bench voting for and against becomes the content of the `reception` term of the
   determination's roll. A declared mover wherever a declared determination executes (in the realm today:
   none; in `test_cr34_declared_disposal.py`: its refusal arms are re-read as odds arms).
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

### 3. The vote sets the odds; the body's presence is the check

- **Check (eligibility):** a declared row may carry `quorum: <int>` (today) **or** `quorum_share: [n, d]`.
  The sitting can be held when the number of bench members holding a live vote *for or against any
  disposal of this matter* is at least `n/d` of the bench present (`judging_set` at the venue, counted as
  distinct persons). It asks whether the body has engaged, not which way.
- **Odds:** for a determination under a declared row, `reception` reads
  `(for − against) / bench`, in `[-1, +1]`, times `reception_gain`: `for` is CR-34's tally (live commits to
  the OUGHT whose subject is the party and whose predicate names the disposal, or, for a `hold`-disposing
  row, the seat); `against` is the live commits to a Proposition the `incompatible` roster pairs with it
  or, for a `hold`-disposing row, to the same OUGHT about another candidate. This is the *"bench's public
  commits"* the SC lane's term already names as its source; it replaces the deed-sum only on declared
  rows. No obstacle term is added.
- **Bands** (the verb lane's one shape; SC-P4's band-keyed `disposes:`): Overwhelming and Success open the
  `hold`; Partial opens it with `provisional_term` (a contested election, lapsing unless a later sitting
  confirms it); Failure dismisses that candidacy (SC-P6), the seat stays vacant, other petitions stand.
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
7. `engine/season/queries/world_q.py`: `declared_votes` returns `(for, against, bench)`; the `vote`
   conjunct of `determine` reads the row's `quorum` or `quorum_share` against `for + against`;
   `reception` (or SC-02's re-sourced reader) takes the declared branch above.
8. `engine/season/arrangements.yaml: excommunication_deliberation`: `quorum: 2` → `quorum_share: [2, 3]`
   `[ASSUMPTION; revert: quorum: 2]`.
9. (HELD) the `head_of_faction` roster member, rule and seven row values.

## Gate

Hand-built, real fold, `PYTHONHASHSEED=0`:

- `patronage`: the King's `confer` on a vacated `off_cardinal_prudence` → refused at `may_fill`; the
  Confessor's → admitted and rolled. With the key deleted from the row the King's is admitted (control).
- Election: four electors, the Confessor's seat vacated, one candidate's petition docketed under
  `conclave`. Arm A: one elector voting for, one against, two silent → the sitting cannot be held (2 of 4
  engaged is under two-thirds). Arm B: three for, none against. Arm C: two for, two against. B and C each
  run over 200 seeds: both show all four bands; P(seat opened) is higher in B than in C; the exact odds
  are printed from the module's own distribution (no sampling claim rests on the 200).
- Realm control: `build_realm(0)` one and two seasons, base hash, with no row declaring `patronage` and
  the `conclave` row absent.

## Falsifier

Arms B and C giving the same band distribution (the vote would still be a pass mark). A seat declaring
`[own_faction]` filled through a seat of another faction. A provisional hold that never lapses.

## NERS reading

N: cut `patronage` and the Church is a royal department (today) or, with a blanket same-faction rule, no
lord can ever invest a bishop; cut the vote-as-odds and a conclave is a threshold. R: a player who is an
elector chooses whom to commit to and when to move the election; a candidate canvasses commits by
`argue`; a faction with a third of the bench can keep the chair empty and pays for it. With no player the
arms each back their own. S: one `may_fill`, one tally owner, the SC obstacle unchanged; `quorum_share`
and `quorum` are one check in two units. E (last): one seat key, one arrangement key, one row, against
the investiture contest, the long vacancy and the contested election they buy.

## Cost class

Small build (1-8). Item 9: edit, after Jordan.
