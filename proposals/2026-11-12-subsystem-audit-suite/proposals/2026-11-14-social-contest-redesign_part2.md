# SC · DICE — the social contest redesigned, part 2: the proceeding types as data, and the verbs

## Status: PROPOSED (the second part of `2026-11-14-social-contest-redesign.md`; read that file's head first: its markers, short names and status sentence apply here; reference under CLAUDE.md §0.05, nothing reads it at runtime)

---

## C. The proceeding types

R4: *"proceedings ... have different types based upon what is at stake, what factions are involved, what the venue is, who
the adjudicators are, who the audience is, how and what kind of arguments/speeches are presented and in what order, what
system is used to render a verdict, etc; from heresy trial to parliamentary debate to private negotiation to rallying a
crowd etc"*.

### C.1 The catalogue is `arrangements.yaml`, extended

The tree's own claim is *"a proceeding is just defined parameters"* (`arrangements.yaml:6`; R-12, COL A19). Nine rows are
seeded and loaded by one loader with a closed key set (`data/arrangements.py:73-77`); most keys have no reader (INT §G.1).
The redesign adds no second catalogue. It gives the unread keys their reader (the proceeding), adds five keys, two
`disposal` values, two blocks beside `arrangements:` and four rows.

| R4's parameter | key (existing or NEW) | read by, after the build |
|---|---|---|
| what is at stake | `disposes`, `disposal_reach` (existing); the `stakes` obstacle term sized by `stakes_ob` (B05.21) | `_eff_determine` (today); the ballot's obstacle (A.5) |
| what factions are involved | **`authority`** NEW: a member of `rosters.yaml: authorities` (`parties`, `polity`, `church`, `guild`, `none`): whose force the proceeding carries (R-34, COL A27) | `world_q.row_for_case` (C.6); B24a.04's conjunct in `may_determine` (§F) |
| what the venue is | `venue_min_rank` (existing, unread); `standard` (B05.21) | `row_for_case` (a row is open only to a seat whose rung is at least that kind); B.5 (a) |
| who the adjudicators are | `disposal` (existing; two values NEW: `hearers`, `exchange`), `bench_basis`, `quorum` | `sigma.py::proceeding_input` (who is a `Decider`); the close (A.5) |
| who the audience is | `floor` (existing, unread): who MAY attend; the kind of audience is computed from who is there (C.5) | `proceeding_input` → `Room` |
| what kind of speeches, in what order | `order` (existing, unread); **`rite`** NEW: a row of the `rites:` block (the moves each side may make, the faults); **`exchanges`** NEW: `[min, max]` in one sitting | `proceed` (A.5); `ProceedingType.moves` |
| what system renders the verdict | `disposal`; **`presumes`** NEW: `for`, `against` or `none`: which side the proceeding presumes for before a word is said; **`strikes`** NEW: how many off-topic speeches a side is allowed | the close (A.5); B.1 |
| what proof is admitted | `proofs` (existing; B05.21's admission filter is its reader) | `world_q.proofs` (B05.21 step 5) |
| how the venue weighs the speaker's case against his carriage (R11) | **`reason_bias`** NEW: a number in `[-1, 1]`, in tenths: the venue's lean of every speech's dice toward Reason (+) or Presence (−), added to the speech's content weight (RD §B.2 a) | `ProceedingType.reason_bias` → `_speech_input` |

The six new keys: `rite`, `exchanges`, `authority`, `presumes`, `strikes`, `reason_bias` (the sixth added for R11,
2026-11-14; its per-row values are RD §B.2 a's venue table, at control 0 on every row until B24p.23). B05.21 adds `standard` and B24a.03 adds
`appeal_to`; B24.09 planned `rite` and now finds it (§F). The keys this design gives no reader (`bench_basis`,
`records_dissent`, `term_required`, `interposed`, `disposal_reach`) stay B27.16's to keep or delete by its own rule.

`presumes` is P9 (the burden sits differently in each forum) and v30's biased track (`:105-116`: a Church Tribunal starts
at 6) carried as levels: at the close the presumed side takes `level(presumption_level)` for it (setting, control `None`,
shipped `minor` `[ASSUMPTION; Jordan to correct]`). It is not B24.09's `bears:` (who must prove each issue), which stays
the rite's.

### C.2 The loader's checks (`data/arrangements.py`)

Added to `_load_arrangement`, each refusing at import and naming the row (the file's own pattern, `_refuse_not_in`):

1. `_ARRANGEMENT_KEYS` gains the six keys; `_DISPOSAL_VALUES` gains `hearers` and `exchange`.
2. `rite` names a row of `rites:`; `authority` is an `authorities` member; `presumes` is one of `for`, `against`, `none`;
   `strikes` is a whole number at least 0; `exchanges` is two whole numbers with `1 <= min <= max`; `reason_bias` is
   present on every row (closure: every proceeding type has a venue bias), in `[-1, 1]` and a whole number of tenths.
   Its pair in `data/rosters.py` (B24p.01): every `content_classes` row has `w_reason` in `[0, 1]`, a whole number of
   tenths; every `grounds` row names a `content:` class; every `proceeding_moves` row with `draw: true` and
   `ground: false` names one, and no other row does (closure: every kind of speech has exactly one content class).
3. Closure across keys: `disposal: exchange` requires `exchanges: [1, 1]` and is refused on a seeded row (it is produced
   only by `abridged`, C.6); `disposal: hearers` requires `bench_basis: none` and `disposes: none`; `order: scripted`
   requires a rite whose `moves` differ by side; a rite's move outside `rosters.yaml: proceeding_moves` is refused; a
   one-speaker rite (no moves for `against`) requires `order` `free` or `written_only`.
4. `rites:` rows: keys `id`, `moves` (a map `for` / `against` / `bench` to a list of move ids), `faults` (a list; empty
   until B24.03 rosters them); B24.09 adds `bears` and `disclosed` (§F).
5. `audience_kinds:` rows: keys `id`, `attention`, `distraction`, `proof_weight`; exactly the four ids of C.5; `attention`
   and `distraction` at least 0; `proof_weight` in `[0, 1]`.
6. A pure function `abridged(row) -> dict` (C.6).

### C.3 The rows

Thirteen rows after the build: the nine, with their new cells, and four new ones (**bold**). Every new cell is
`[ASSUMPTION; Jordan to correct]`; the existing cells are unchanged (`arrangements.yaml:99-307`). `standard` shows the
value B24p.23 sets; B05.21 ships every row `plain`.

| row | authority | `venue_min_rank` | standard | `floor` | `order` | exchanges | rite | `disposal` | presumes | strikes | `disposes` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **`conversation`** | parties | hearth | plain | closed | alternating | [1, 3] | `contest` | hearers | none | 0 | none |
| **`questioning`** | parties | hearth | plain | closed | scripted | [1, 4] | `questioned` | hearers | none | 0 | none |
| **`rally`** | none | hearth | plain | open | free | [1, 3] | `address` | hearers | none | 0 | none |
| **`audience`** | polity | settlement | demanding | admitted | free | [1, 2] | `address` | bench | against | 0 | oblige |
| `negotiation` | parties | hearth | plain | closed | alternating | [1, 3] | `contest` (B24.30: `mutual`) | mutual | none | 0 | oblige |
| `arbitration` | parties | hearth | routine | closed | alternating | [2, 3] | `contest` | bench | none | 2 | oblige |
| `legal_trial` | polity | settlement | demanding | open | rank | [2, 5] | `contest` (B24a.04: `accusatorial`) | bench | none | 2 | detain |
| `tribunal` | polity | settlement | demanding | admitted | rank | [2, 4] | `contest` | bench | none | 2 | ban |
| `interrogation` | polity | hearth | plain | closed | scripted | [1, 4] | `questioned` | bench | for | 1 | detain |
| `inquisition_hearing` | church | settlement | hard | closed | scripted | [1, 5] | `questioned` (B24a.04: `inquisitorial`) | bench | for | 1 | ban |
| `excommunication_deliberation` | church | settlement | hard | closed | rank | [1, 3] | `contest` | declared (quorum 2) | for | 0 | ban |
| `parliamentary_debate` | polity | duchy | demanding | open | rank | [3, 5] | `contest` | bench, to be `declared` (below) | none | 0 | Record |
| `council_of_state` | polity | duchy | demanding | closed | rank | [2, 3] | `contest` | bench | none | 0 | Record |

Notes on the rows.

- **`conversation`** is the default type of talk between two persons with nothing docketed: v30's Casual Dispute and
  Personal Appeal (`:105-116`), PK's K1 dyadic influence (COL A25). The hearer is the one decider and is balloted for
  himself. Its abridged form is `tell` and `lie` (C.6).
- **`questioning`** is Jordan's *"interrogation for info"* (R6). It is not the existing `interrogation` row, which is a
  bench disposing a `detain` (*"the questioner decides, and the subject cannot win"*, `arrangements.yaml:215`) and stays
  for `determine`. Under `questioning` the one questioned is the decider: whether he gives way is his own ballot, with
  his marks and a yield counted as levels (A.5). `interrogate` and, when B25.14 draws it, `interview` call it.
- **`rally`** is R4's *"rallying a crowd"*, absent from the tree (INT §G.3). One speaker; the floor is open; every hearer
  present is a decider and is carried or not for himself. A cohort is a person at weight above one
  (`state/carriers.py:775`), so a crowd needs no new carrier. Sources: K/'s `public_oration` venue (`modes.py:166-179`);
  PROC's unseeded `public debate`; preaching (COL I13). It disposes nothing: what a carried hearer does next is his own
  act, so R-21 (a standing is no stake, COL §8 row 12) holds.
- **`audience`** is a petition or plea before one seat: PROC's unseeded `audience / embassy`, PK's K4, v30's Royal Audience.
  `presumes: against` and a `demanding` standard carry N17 (supplication: the form matters, and a refusal costs the one who
  refuses, which B27 may give its write). Its `order` becomes `written_only` when the matter is a filed petition nobody
  speaks to (C.6).
- **`parliamentary_debate`** keeps `disposal: bench` until a `determine` can open something under a `Record`-disposing
  row (`arrangements.yaml:265-271`: `_eff_determine` declines a `Record`). B24a.01 builds the count that licenses an
  owner's act (CR-58) on B21c's `resolution` Record; §F gives it the flip to `declared` with a quorum of a majority of the
  seats. Until then a debate runs its exchanges and closes on the presiding seat's ballot.
- **Heresy** is not one row: the investigation's sittings are `questioning` (the interrogation of a suspect each season,
  v30 §7.3 `:449-460`), the trial is `inquisition_hearing`, the sentence is `excommunication_deliberation`. The lifecycle
  across seasons (its eight closure conditions, COL A11) is the case file's, not the type's: §G.
- **`reason_bias`** (R11) is not a column of the table above: its thirteen values are RD §B.2 a's venue table (a court
  +0.2; a formal bench or closed council +0.1; private talk and a plea before one seat 0; an open assembly −0.1; a crowd
  −0.3), each `[ASSUMPTION; Jordan to correct]`, every row at 0 until B24p.23. `abridged` copies it, as it copies the venue.

### C.4 Rites and moves

`rosters.yaml: proceeding_moves` (closed, ordered). B24.03 planned this roster as `hearing_moves`; it lands here with
the first six members and B24 adds its evidence and bench members to it (§F). Columns: `draw` (does the move roll a
speech), `capability` (the skill whose rank joins the case, B24.04's column), `resisted_by` (which attribute of the one
addressed feeds the `resist` source, B.6 d), `ground` (does the move take one).

| move | draw | capability | resisted_by | ground | effect |
|---|---|---|---|---|---|
| `argue` | yes | `argue` | will | yes | the track moves by the margin toward the mover, between `-track_clip` and `+track_clip` |
| `press` | yes | `argue` | will | yes | a landed press strikes the other side (B.6 a); a failed one costs the presser esteem |
| `divert` | yes | `argue` | will | no | a landed divert sets a pull on the other side's next speech (B.1) |
| `deceive` | yes | `deception` | attunement | yes | as `argue`, the content false; the mover carries a standing pull of `deceive_pull` (keeping a false story straight is a hold, B.1) |
| `concede` | no | — | — | no | the track moves `concede_step` toward the other side; the conceder's resolve rises by one (v30 Step 5, *Concede a Point*, `:238`) |
| `rest` | no | — | — | no | nothing |

A seventh column, `content:`, is set on `divert` alone (`procedural`): the one drawing move that takes no ground names
its own content class; every other drawing move speaks on a ground and takes the ground's class (RD §B.2 a, R11).

`deceive` is how a `lie` enters: the row's cell names the move (C.6), so no verb is named in the module. Its resistance is
the hearer's Attunement (B05.25's cell for `lie`: *"seeing intention in the moment"*, AR-30). `deceive_pull` and
`concede_step` are settings (control 0; shipped 0.5 and 1.0 `[ASSUMPTION; Jordan to correct]`).

`arrangements.yaml: rites:` (a new block; four rows here):

```yaml
rites:
  - {id: contest,    moves: {for: [argue, press, divert, concede, rest], against: [argue, press, divert, concede, rest], bench: []}, faults: []}
  - {id: address,    moves: {for: [argue, rest],                         against: [],                                     bench: []}, faults: []}
  - {id: questioned, moves: {for: [argue, press, rest],                  against: [argue, concede, rest],                 bench: []}, faults: []}
  - {id: plain,      moves: {for: [argue],                               against: [],                                     bench: []}, faults: []}
```

`questioned` carries v30's asymmetry (`:398-402`): the questioner may press and the one questioned may not, nor divert.
`plain` is the abridged form's rite; `abridged` swaps `argue` for the move the verb row names.

### C.5 The room: who is present, and what kind of audience they are

`arrangements.yaml: audience_kinds:` (a new block; four rows). The kind is computed, never authored on a type:

```
audience_kind = crowd    if the hearers' summed weight >= crowd_at        (setting; shipped 12 [ASSUMPTION; K/'s crowd of 15])
              = gallery  if there is at least one hearer
              = bench    if there is at least one decider who is not a hearer
              = none     otherwise
```

| kind | attention | distraction | proof_weight | reading |
|---|---|---|---|---|
| `none` | 0 | 0.5 | 0.5 | two people talking: everything is heard; any talk wanders a little |
| `bench` | 2 | 0.25 | 0.75 | judges attend to proof and interrupt (N3, high elaboration) |
| `gallery` | 4 | 0.5 | 0.5 | onlookers: a speaker must hold them |
| `crowd` | 5 | 1.0 | 0.25 | a mass goes by manner and is easily lost (N3, low elaboration; K/ `public_oration`'s pathos .50) |

At control the three columns read 0, 0 and 0.5 on every row; the table shows B24p.23's values, each `[ASSUMPTION; Jordan
to correct]`. This is COL I06 (route by audience) and §8 row 10 decided for R4: the audience is a concept, as a computed
property of the room, with one row per kind and no stored popularity.

Who the hearers are: the persons the act is heard by (`sigma.py::audience_of`, B07.04, the plan's one owner of *"rooms an
act is heard by"* `[UNVERIFIED: its signature, read through wp part22.md:46]`), less the speakers and the bench, and by the
row's `floor`: `closed` admits none; `admitted` admits those holding a seat whose scope holds the venue `[ASSUMPTION: the
basis when the row names none — basis: `_parse_floor` admits a bare `admitted`, `data/arrangements.py:118-133`]`; `open`
admits everyone present at the venue's rung (`world_q.presence`, `:1523`).

### C.6 How a type is chosen when a verb calls the subsystem

Today no computed case names a row (`effects_information.py:417-426`: *"WHICH arrangement a computed case is heard under
is NOT DERIVED here -- no source exists"*). Two data tables and one function close it.

**1. The verb row says how it proceeds.** A new verb-row cell, `proceeds:`, on every row that calls the subsystem (D):

```yaml
proceeds: {row: conversation | questioning | rally | audience | negotiation | docket, form: full | abridged, move: <move id>}
```

`row: docket` means the docket item's own row. `move` is the move an abridged form makes (default `argue`). The loader
(`data/verbs.py`) refuses a `proceeds:` whose row is not an arrangement id or `docket`, whose move is not rostered, or
on a row whose prize's module entry is not `social_contest.proceeding`.

**2. A cell may be conditioned on who is addressed.** `proceeds:` may be a list of `{when: ..., row: ..., form: ...}`
entries, first match taken, over a closed `when` roster of two keys: `hearer: cohort | person` (the addressed person's
`is_cohort`, `state/carriers.py:881-889`) and `docketed: true | false`. So `argue` reads
`[{when: {hearer: cohort}, row: rally, form: full}, {row: conversation, form: full}]`: arguing to a cohort is addressing
a crowd `[ASSUMPTION: no new verb for a rally — basis: a cohort is a person at weight above one, and `argue` already binds
`to` over persons; reversible by adding a row]`.

**3. A computed case names its row.** `rosters.yaml: case_rows` (ordered; first match) and
`world_q.row_for_case(w, seat, matter) -> str`, called by `_eff_open_case` and `_eff_carry` when the act declares no
arrangement:

```yaml
case_rows:
  - {when: {authority: church,  matter: person},                                  row: inquisition_hearing}
  - {when: {authority: polity,  matter: proposition, seat_at_least: duchy},       row: parliamentary_debate}
  - {when: {authority: polity,  matter: person,      bench: several},             row: legal_trial}
  - {when: {authority: parties},                                                  row: arbitration}
  - {when: {matter: record},                                                      row: audience}
  - {when: {},                                                                    row: arbitration}
```

The `when` keys, each read from an existing carrier: `authority` is the opening seat's (`authority.by_faction` over the
seat's faction, `state/gate.py`'s `seat_faction`); `matter` is the class of the docketed subject (a person, a
`Proposition`, a `Record`: a carried petition); `bench` is `one` or `several` by `len(judging_set(w, venue, matter))`
(`world_q.py:642`); `seat_at_least` is a `rung_kinds` member compared with the kind of the seat's rung. `row_for_case`
skips a row whose `disposes` is not disposable (`DISPOSABLE_KINDS`, the wedge `_eff_open_case` already refuses, `:427-431`)
and a row whose `venue_min_rank` is above the seat's rung, so no row is named that `determine` would decline. The last
row is today's path made explicit: an undeclared determination disposes an `oblige` (`_disposal`,
`effects_information.py:693-698`), and `arbitration` disposes `oblige`. Every cell is `[ASSUMPTION; Jordan to correct]`;
which cases go where is content (P11's rule: the plan builds the mechanism and the rows it must).

**4. The abridged form of any row.** `data/arrangements.py::abridged(row, move) -> dict` returns the row with `order:
free`, `exchanges: [1, 1]`, `disposal: exchange`, `rite: plain` (its one move replaced by `move`), `strikes: 0`,
`presumes: none`, and every venue and audience key unchanged. So a `tell` in a kitchen is `abridged(conversation)`, and a
`speak` at a sitting is `abridged(<the sitting's row>)`: one speech, weighed by that room's standard, audience and bench,
with no ballot. One rule, applied to any row; no abridged rows are seeded.

### C.7 How factions, venues, adjudicators and audience bind

Each binding reads a carrier that exists; none adds a field to `World`.

| part | bound from | by |
|---|---|---|
| the type | the verb row's `proceeds:`; the docket item's `arrangement` (`world_q.docketed`, `:208`) | `world_q.proceeding_row(w, act)` → `(row id, form, move)` |
| the venue | the act's rung, which is the actor's place (`loop/sides.py:171-172`); for a docketed matter the rung of the sitting's Date | `proceeding_input`; the row's `venue_min_rank` gates row choice (C.6), `standard` the speech (B.5) |
| the factions | the row's `authority`; the seats' factions (`seat_faction`); each party's own faction (`world_q.faction_of`, `:2550`) reaches a speech only as B28.35's obstacle operand, eased by Reason (B.2 c) | `row_for_case`; B24a.04's conjunct |
| the adjudicators | `bench`, `declared`: `judging_set(w, venue, matter)`, each seat a `Decider` with his judging pool (`pool.faculty` on `determine`'s skill), his seat's `modifier` (B05.20), his `lean` (B24.02's commit term, B24.11's per-member count); `mutual`: nobody (consent is a move, B24.30); `hearers`: the one addressed (the `against` speaker, or the cohort an address is made to) and every hearer the floor admits (C.5), each with the base pool; `exchange`, `none`: nobody | `proceeding_input` |
| the audience | C.5 | `proceeding_input` → `Room` |
| the speakers | `loop/sides.py::sides_of`: the actor and the row's opponent operand (`resolve.py:812-815`); for a self-plea the accuser, else the presiding seat (B28.35's rule, kept) | `proceeding_input` |
| the topic | the act's `subject` where the opponent operand is `to` (`argue`, `tell`, `lie`: the Proposition or claim), the docket matter for `speak` and `determine` (INT C.1) | `proceeding_input` → `ProceedingInput.topic` |

`Decider.pool` for a hearer or a party is `pool_of(untrained, 0, pool_add, pool_floor)`: a person judging for himself
brings the base and no skill. `Decider.lean` for a hearer is his regard for the speaker
(`person_q.stance_toward(hearer, speaker)`, clamped at `STANCE_MAX`, times `regard_step`: the favourable half as sigma
for, the hostile half against), read from the hearer's own interior as OBS member 7 reads it; no ledger is read (F8).

### C.8 Jordan's seven, as the catalogue resolves them

| what Jordan named | row | sides and order | deciders and close | what makes it its own kind |
|---|---|---|---|---|
| heresy trial | `inquisition_hearing` | inquisitor (`for`) and accused; scripted; 1 to 5 exchanges | the presiding church seat's ballot; presumed for the charge; one strike | the accused may not press or divert; a `hard` standard; `disposes: ban` |
| parliamentary debate | `parliamentary_debate` | speakers by rank; 3 to 5 exchanges; open floor | the presiding seat until B24a.01's flip, then every seat's ballot against a quorum | a gallery or crowd in the room; no proofs admitted (`proofs: []`); a `demanding` standard |
| private negotiation | `negotiation` | two parties alternating; 1 to 3 exchanges; closed | nobody is balloted: agreement is the other party's `accept` (B24.30); an impasse is an ending | no bench, no audience: `attention` 0, so delivery and Reason carry it |
| rallying a crowd | `rally` | one speaker; 1 to 3 exchanges; open | every hearer for himself | `proof_weight` 0.25, `attention` 5: Presence carries it; a misread crowd costs (B.3) |
| interrogation for information | `questioning` | questioner and questioned; scripted; 1 to 4 exchanges; closed | the one questioned | the questioner presses; marks and a yield are the levels of the close; Will is the defence |
| a trial | `legal_trial` | parties by rank; 2 to 5 exchanges; open | the presiding polity seat | `proof_weight` 0.75; two strikes; B24's exhibits and issue ladder land on this row |
| the abridged auto proceeding | `abridged(row)` | one speaker, one exchange, no decider | the exchange's own margin | `tell`, `lie` under `conversation`; `speak` under the sitting's row |

### C.9 What of the kernel's catalogue is carried before B24.33 deletes it

COL §4 item 6: B24.32's ten checks carry none of K/'s proceeding parameters. By row of what K/ holds (COL A02, A15 to
A18), and where it goes:

| K/ holds | carried as | not carried, and why |
|---|---|---|
| eight proceedings' exchange counts and role structures (`modes.py:485-515`) | `exchanges`, `order`, `rite` on the rows of C.3 | the track's banded thresholds (7, 3, 9, 1): the close is a ballot on the one ladder |
| four adjudicator types (`dictionaries.py:337-386`) | `disposal` and the computed audience kind; the primary attribute per type becomes `proof_weight` (N3) | a primary-attribute table: R1 fixes what each attribute does; the audience changes how much it counts |
| venue proof weights, ethos / pathos / logos (`modes.py:66-85`) | `proof_weight`, one number per audience kind | three weights per venue: COL §8 row 17, decided for *not fields* (the grounds a person is moved by are his own, B.3) |
| win conditions `ProofBar`, `ThresholdRace`, `TallyAtClose`, `GraceThreshold`, `VoteAtClose` | the close by `disposal`; `presumes`; `stakes` | thresholds on a tally: each would be a second resolver beside the ladder |
| fault catalogues: evasion strikes, yield strikes, barred devices, contradiction | `strikes` (evasion); the `yielded` and `broken` ends; B24.03's faults | barred devices: no device roster exists |
| six cross-cultural venues (`modes.py:157-325`) | `rally` (public oration), `inquisition_hearing`, `excommunication_deliberation`, `audience` (imperial petition) | secret council and memorial remonstrance: no ruling asks for them; rows a designer can add with no code |
| the armature and Appraise | B.3 | — |
| Face, Reserve, Stasis (`primitives.py:11-56`) | `SideState.esteem`, `.resolve`; the topic and issue | Reserve's per-move costs: resolve counts exchanges |

§F adds one check to B24.32 (the four rows of C.3 that came from K/ load and run a sitting) so the deletion's own
falsifier sees the catalogue.

---

## D. The verbs

R3: *"argue/speech/etc verbs should all be calling the social contest/proceedings subsystem as they all concern
influencing people"*. R6: `tell`, `lie`, `speak` are abridged. R7: a brute function does not roll; *"the exception is if
the verb calls into being a subsystem"*.

### D.1 The sixteen influence verbs (INT §D), routed

| verb | route today (INT §D) | route after | `proceeds:` cell | why |
|---|---|---|---|---|
| `argue` | `a proposition`, one roll, Presence | **full form** | `[{when: {hearer: cohort}, row: rally, form: full}, {row: conversation, form: full}]` | persuading someone of a proposition is the contest itself; with no effort spent it is one exchange and the hearer's ballot |
| `tell` | `a standing`, one roll, Focus | **abridged** | `{row: conversation, form: abridged}` | R6 |
| `lie` | `a standing`, one roll, no attribute | **abridged** | `{row: conversation, form: abridged, move: deceive}` | R6; the hearer resists with Attunement (C.4) |
| `speak` | `a matter`, one roll, Focus, the bench's room | **abridged**, under the sitting's row | `{row: docket, form: abridged}` | R6; B24.08 keeps `speak` a single filing act, which the abridged form is |
| `interrogate` | `a proposition`, one roll, Reason | **full form** | `{row: questioning, form: full}` | R6 names *"interrogation for info"* among the full kinds |
| `covenant` | no roll; writes a Record, `covenant.offered` | **full form**, when B28.13 opens the negotiation with it | `{row: negotiation, form: full}` | offering terms is the opening of a negotiation (B28.13, B24.30); until then the row is unchanged |
| `interview` | no roll; a prompt (K-36) | **full form**, when B25.14 draws it | `{row: questioning, form: full}` | questioning a free person is the same type; he may rest and leave |
| `petition` | no roll; writes a Record | **stays a brute function** (filing) | none | the filing cannot be done well or badly; the persuasion is where the matter is heard (`speak`, or the `audience` row a carried petition is docketed under) |
| `open_case` | no roll; dockets | **stays a brute function**; it now names the row (C.6) | none | a seat's act; its efficacy is `determine`'s |
| `challenge` | no roll; a challenge Record | **stays as B28.06 draws it** | none | a declaration answered by the other's `accept`; the fight is combat's (R9) |
| `construe` | no roll | **stays B25.16's** (FI) | none | a reading of terms, not an address to anyone |
| `issue` | brute | **stays a brute function** | none | R7; whether it is obeyed is the receiver's `comply` or `evade / defy` (B28.03) |
| `dispatch` | brute | **stays a brute function** | none | R7 |
| `order_unit` | no roll | **stays a brute function** | none | R7; obedience in the field is `27_MB_A`'s draw |
| `give` | no roll | **stays B28.02's** | none | handing something over addresses nobody's belief |
| `forge` | no roll | **stays a material act** | none | the forgery's quality opposes an inquiry later (`roll.py:180-182`) |

Counts: 5 call the subsystem now (`argue`, `tell`, `lie`, `speak`, `interrogate`), 2 when their own items land
(`covenant`, `interview`), 9 do not. The three commanding verbs are decided against being influence: an order compels
by standing and R7 says a brute function rolls nothing; what is in question is the receiver's obedience, which is his own
drawn act (INT §F item 6, decided).

### D.2 The five other verbs the social roll deals (INT §D.2)

| verb | after | why |
|---|---|---|
| `determine` | the close of a full proceeding under the docket's row: `proceeds: {row: docket, form: full}`; its prize `a verdict` names `social_contest.proceeding` (B24.08, renamed in §F) | the verdict is the ballot of the one who determines, with the sitting's track as levels (A-14). It is not a brute function: the act calls the subsystem (R7's exception). INT §F item 8, decided |
| `arrest` | stays a single roll on `social_contest.roll` with B05.25's averaged cells | laying hands on someone is not influence by words (INT E-19); B05.24's Q1 keeps its prize question |
| `examine`, `research`, `surveil` | stay single rolls on `social_contest.roll` | inquiries into a Site, a Record or a Rung: nobody is addressed |

### D.3 The verb rows' cells to edit (`engine/season/verb_table.yaml`)

| row | cells removed | cells written | at |
|---|---|---|---|
| `argue`, `tell`, `lie`, `speak`, `interrogate` | `governing:`, `opposed_attribute:` (B05.25's interim cells), at B24p.19 | `proceeds:` as D.1 | B24p.16 (written), B24p.19 (read; the interim cells deleted) |
| `determine` | `governing:`, `opposed_attribute:` | `proceeds: {row: docket, form: full}`; `contests: a verdict` | B24.08 (the cell and the prize together, §F): until then it stays the single roll |
| `covenant`, `interview` | none | `proceeds:` as D.1 | B28.13, B25.14 (§F) |
| every row with `proceeds:` | — | `capability:` stays (B04.03): the proceeding reads it for the abridged move's skill | — |

`rosters.yaml: contest_subsystems.prizes`: `a standing`, `a proposition`, `a matter` keep `module_entry:
social_contest.roll` as the default and gain `proceeding_entry: social_contest.proceeding`; `seam/contest.py` takes the
second for a verb row carrying `proceeds:` (B24p.19); `a verdict` (B24.03) names the proceeding in `module_entry` itself. So `arrest`, which shares `a standing` with `tell`, keeps the single
roll with no prize split `[ASSUMPTION: a second entry on the prize row over a new prize — basis: a new prize would move
every `tell` and `lie` row's `contests:` cell and the write gate's prize roster for no gain; `manifest.check_contest_prizes`
(`references/module_contracts.yaml:56`) checks the second cell as it checks the first]`.

### D.4 The averaged-pool rule (B05.24, B05.25) reconciled

The 2026-11-13 rule has three kinds of verb: (a) brute, (b) efficacy with one to three attributes averaged, (c) a hand-off
whose subsystem *"reads the person by its own rule"*, with (c) reserved for `fight`, `accept`, `capture`, `march`
(wp `part8.md:288-302`). R3 and R6 put the influence verbs in (c): they call a subsystem, and R7 itself exempts such a
verb from the averaged pool. So:

| part of B05.24 / B05.25 | disposition |
|---|---|
| the three kinds, and the loader's rule that a row takes exactly one | **stays**; (c) is recognised by a `proceeds:` cell as well as by a prize of `person_inputs: own` |
| `brute:` rows never roll; `test_a_brute_verb_twice_on_one_state_is_one_outcome_and_no_draw` | **stays** |
| `governing:` (one to three, averaged), `governing_mean`, `governing_score`, `rank`, fractional pools | **stays** for every single-roll verb: `arrest`, `examine`, `research`, `surveil`, `carry`, `conceal`, `tie / knot` and the material, field and governance task rows |
| `opposed_attribute:` | **stays** for a single-roll verb contested against a person (`arrest`); **replaced** for the influence verbs by the `resist` source, which reads the addressed person's Will, or his Attunement for a `deceive` (B.6 d) |
| the social rows' cells: `argue` = mean(Presence, Attunement, Reason); `speak` = mean(Presence, Reason, Grace); `tell` = mean(Reason, Attunement); `lie` = mean(Attunement, Reason, Grace); `interrogate` = mean(Attunement, Presence); `determine`'s cell | **replaced** by `proceeds:`: five rows at B24p.16 and B24p.19, `determine` at B24.08. They ship as B05.25 writes them until then (the single roll needs a pool in between) and are an interim |
| *"`speak` moves to (c) by its prize row ... when the hearing scene's nested run is built"* (`2026-11-13-verb-governing-attributes.md` §2.8) | **replaced**: five move at B24p.19 and `determine` at B24.08, each by its own cell |
| Attunement averaged into `argue`'s dice (*"Jordan 2026-11-13 puts it in the roll"*) against ED-IN-0350 (COL §8 row 2) | **decided for ED-IN-0350 and R1**: Attunement reaches the roll through the choice it informs (B.3), which is *in the roll's outcome* and not in its dice |
| B28.34 and B28.35's persuasion terms | **kept and re-homed**: each term is an operand or a level the host passes on `Speaker.operands` and `Speaker.levels`; the two the roles already carry (the teller's reason and attunement) are struck from that list (§F) |

One sentence for B05.24's rule, replacing its last clause: *"... a verb that hands its act to a subsystem (a fight, a
field, a proceeding) names none, and the subsystem reads him by its own rule; a verb that influences a person by words is
such a verb, and its row says which proceeding it opens and whether in full or abridged."*
