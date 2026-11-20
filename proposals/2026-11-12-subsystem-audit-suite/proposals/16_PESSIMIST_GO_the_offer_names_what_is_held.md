# GO — the offer names what the seat holds: a goal's seat-holders are read from the ledger, and a creation row shows the seat

Reconciled: 2026-11-12, U5d closure — folded **A-32** and **A-33**. Seat changes ship realm-wide (A-32, with presence, jurisdiction and telling built as the test arm), so the build-time deposit of public seats' holders as record-channel claims agrees with the shipped reach. A death is not learned with the seat (A-33): a goal's `seat_holders` may name a holder the person does not yet know is dead, and the offer must not correct him. §4's creation row lists a cohort as a cohort; whether a cohort may be played is not ruled; under A-56 a played cohort would be offered the heavy moves only.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 (CONFORMS: `creation_sheet` takes its
reader as a parameter so `decision/` names no World), §2 (A-32, A-33, A-56: folded at the head; nothing further), §7/§7b
(the gate's count named in an existing harness, tests, tier); U3 B34, §6.2 (`probe.py` is not in the repository). No body
text changed beyond the gate and the cost lines.

## Status: PROPOSED

Lands in batch: **B34** (IN/CHAR), after `11_GO_player_surface_contract_B.md` (B34; its `Situation.holdings` is the pair
shape §4 reuses). Depends on: `seats_named`, `LedgerReader.latest_about`, `harness/populated.py`'s acquaintance deposit
(exist).

Carries F-PES-GO-03 and F-PES-GO-10 of `audits/16_PESSIMIST_GO.md` (§2.1, §1.5). Lanes IN, CHAR (the
owner files are `queries/world_q.py`, `harness/populated.py`, `decision/sheet.py`); GO is the lane
that measured it, at the player's surface. Read at `826b747`. Reference only (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

1. A goal whose object is `seat_holders` forms its standing question on the holders **the person's
   own ledger names**, not on the live `hold` Tenures of the World. A person who has never learned
   who holds a seat has no question about its holder until he learns.
2. The world builder deposits, for each seat a goal names, a record-channel claim of who holds it in
   the ledgers of the persons who would have heard, each by a draw.
3. `CreationRow` gains two fields. No act changes.

Items 1 and 2 are a declared hash mover (ledgers at build, and the questions formed from them).

## The problem, with evidence

`probe.py base {0,1,2} 2` (`runs/PES_GO/`; every person seated on the sheet; control: hash equal to
the automated run). For each offered row, the ids it names were tested against a generous closure
of what the person could know: every id in any claim he holds, every Tenure he is party to, and
every party to a Tenure on a thing he is tenured on (his household and settlement).

| | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| rows offered | 45,520 | 45,581 | 45,355 |
| occurrences of a **person** named through a classed referent and outside the closure | 160 | 191 | 194 |
| deliberations with at least one row naming an id outside the closure (all routes) | 105 of 774 | 90 of 783 | 76 of 771 |

The worked case, the same in all three seeds: Carin Vedel (`p_npc_088`, restoration movement, a
workshop in settlement 026) holds three acquaintance claims. Her first question is
`q:need:goal_restoration_evade_capture` with referents `p_npc_004` and `p_npc_038` (the Senior
Inquisitor and the Cardinal Justice, in the cathedral of settlement 036), and her offer carries
`train`, `tend`, `forgive`, `challenge`, `sabotage`, `surveil` … on each.

The owner says what it does (`queries/world_q.py:2847-2859`): `seat_holders` is "the persons now
holding any listed seat (a live `hold`, `w.tenures` order), so the referent FOLLOWS A SUCCESSION"
and "IS A WORLD READ WITH NO CLAIM BEHIND IT". It cites ED-IN-0292 (2) as its precedent. That
precedent's closing row (`registers/editorial_ledger_in.jsonl:74`) took the opposite answer: "a
vacancy reaches a person as a claim deposited through the channels, not as a world stamp; AX-7
(`01_AXIOMS.md:113-120`) prohibits the engine's resolution being handed into belief unmediated". So
this is not a new design call. It is a later site that did not follow an answer already taken.

At the player's surface the cost is specific: the menu names a new office-holder the moment he is
seated, before any channel has told the seat; and `View`'s guarantee ("a person decides from their
own claims", `state/carriers.py:504-509`) is true of the View and false of the Question beside it.

Creation: `creation_sheet` at seed 0 returns 83 rows, 37 of them cohorts, with `capability`
non-empty on 2, `attributes` on 0. The Inquisitor and the fugitive show the same `capability`. The
row carries no office, place, faction or goal.

## The resolution, decided

Ladder step 1 (ED-IN-0292 (2), closed 2026-10-26) for the read; step 4 (the record channel's
existing deposit shape; `intent_disclosure`'s keyed chance, H-190) for the seeding; step 4 (SURF-B's
`Situation.holdings`) for creation.

### 1. `_goal_referents`, kind `seat_holders` (`queries/world_q.py`)

Old (the kind's branch): the subjects of live `hold` Tenures on the listed seats, in `w.tenures`
order. New: for each listed seat, the person `p`'s own ledger names as its holder, by the reader
`seats_named` already is (`world_q.py:3146`: "THE SEATS `p` HAS BEEN TOLD OF … the Offices among
`person_q.ledger_names(p.ledger)`"), extended to return the holder his latest claim on that seat
names (`LedgerReader.latest_about`, the one comparator). A seat he
holds no such claim on contributes nobody. He may be wrong: a claim naming a dead or replaced
holder forms a question about that person, which the fold then refuses or the world then corrects;
that is R-08 working.

### 2. The seed (`harness/populated.py`, beside the acquaintance claims it already writes at `:646`)

For every seat named by any loaded goal's `seat_holders`, and every person, one keyed draw
(`draw(pid, f"knows_holder:{seat}")`) against a chance read from one new fixture block:

```
# data/fixtures.py
holder_known_chance = {"same_settlement": 0.95, "same_faction_or_goal": 0.9, "elsewhere": 0.5}
```

`same_faction_or_goal` is a person whose own `commit` Tenures include a goal naming that seat or the
faction the seat belongs to. On success the builder deposits the claim the record channel deposits
for a `hold` opening (source `told_by`, empty `chain`), dated before tick 0. The values are
`[ASSUMPTION; medium; Jordan to correct; revert: 1.0 everywhere, which reproduces today's referents]`.
No chance is 1.0: a fugitive who has not heard who the new Cardinal Justice is exists in some seeds,
and that is a story (the standing rule: state sets the odds, the draw decides). After build,
successions reach ledgers by the channel that already carries them (`tenure.closed` reached 82 of 82
persons in the tick of a death at seed 2; that certain reach is listed for WR and CORE in the audit,
F-PES-GO-06, and is not changed here).

### 3. The docstring

`goal_referents`' `⚠ seat_holders IS A WORLD READ …` paragraph is replaced by one sentence: the
kind reads the person's own ledger, per ED-IN-0292 (2).

### 4. `CreationRow` (`decision/sheet.py`)

```
@dataclass(frozen=True)
class CreationRow:
    id: str; name: str
    cohort: bool                 # Person.is_cohort
    capability: Mapping; pursuits: Mapping; conviction: Mapping; attributes: Mapping
    holdings: tuple              # ((tenure kind, object id), ...): his own live Tenures, the same pairs
                                 # SURF-B's Situation.holdings defines, from the same reader
def creation_sheet(persons, holdings_of) -> tuple     # holdings_of: person id -> tuple; the caller's reader
```

`decision/` still names no World: the caller, which already holds the persons, passes the reader
(CHAR's `OwnStateReader` when it lands; until then `harness/play_surface.py` builds the mapping
host-side from `w.tenures`, as `harness/military_menu.py` does for an army). Creation happens before
the first season and shows the seat's own state, so no knowledge rule is touched.

## Exact edits, by file and owner

| file | owner | edit |
|---|---|---|
| `engine/season/queries/world_q.py` | IN | `_goal_referents`' `seat_holders` branch; `seats_named` returns the named holder; the docstring |
| `engine/season/harness/populated.py` | IN | the seed draw and deposit |
| `engine/season/data/fixtures.py` | IN | `holder_known_chance`, with its register row |
| `engine/season/decision/sheet.py` | IN | `CreationRow.cohort`, `.holdings`; `creation_sheet`'s second parameter |
| `engine/season/hole_register.yaml` | IN | H-203's `cite:` gains the seed; the new fixture's row |

## The gate (execution artifacts)

`probe.py base` was lane scratch, not in the repository; its count is committed as a reading of
`python -m engine.season.harness.interactions` (exists) and as NEW
`engine/season/tests/test_seat_holders_from_ledger.py`: `test_goal_referent_reads_own_ledger`,
`test_all_chances_one_reproduces_todays_referents` (gate 2), `test_creation_sheet_marks_cohorts_and_holdings`
(gate 4), `test_unheard_holder_forms_no_question_until_a_deposit_names_him` (gate 3's story). Command:
`python -m pytest engine/season/tests/test_seat_holders_from_ledger.py -q`.

1. The count inside `harness/interactions.py` at seeds 0–2, two seasons:
   occurrences of a person named through a classed referent and outside the closure = **0**.
2. Control, exact: with every chance set to 1.0, the set of `need` questions and their referents
   returned by `questions_for` for every person at tick 0 equals today's.
3. At the shipped chances, over seeds 0–9: the share of persons with a `seat_holders` goal who hold
   no claim on any of its seats at build is neither 0 nor more than a quarter (the draw is a draw);
   and at least one such person forms the question later in the run, after a deposit names the
   holder (the story the change makes possible).
4. `creation_sheet` at seed 0: 37 rows with `cohort=True`; the Inquisitor's row carries
   `("hold", "off_senior_inquisitor")` and the fugitive's does not.
5. One re-record of the seeded goldens, said plainly.

## The falsifier

A person whose offer names a seat-holder he holds no claim about (gate 1 above zero). A run in
which the seeded claims make every person know every holder (the draw is decoration). A goal that
never forms for anyone at the shipped chances (the seed is too thin and ambition dies).

## NERS reading (§0.06; E last)

- **N.** Cut the world read and what dies is NPC initiative at tick 0 for those who drew no claim;
  the seed restores it for most and leaves a remainder who must learn, which is a possibility the
  game lacked. Top-down (AX-7), bottom-up (the View's rule), lateral (the same rule `vacancies` was
  answered with) and from the player's side (the menu is not a news channel) agree.
- **R.** The no-player half gains a story: someone acts on a stale belief about who holds a seat.
- **S.** One methodology for "who does he think holds it": the ledger, as for every other belief.
- **E.** One branch re-pointed at an existing reader, one seed loop, two fields.

## Cost class

Edit plus a small build; one re-pin. Tier: `sonnet`, effort `high`; the three chances are an `opus`-or-Jordan
judgment (marked ASSUMPTION). Hash movers declared: ledgers at build and the questions formed from them (every
seeded world); one re-pin in B34. Lands it: B34, order §4 (hash-equal) → §1 and §3 → §2 with the fixture and its
register row (id from `references/id_reservations.yaml` `next_free`) → the re-pin.
