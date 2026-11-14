# SC · DICE — the social contest redesigned, part 5: the fold map into workplan v12, and what was not decided

## Status: PROPOSED (the fifth part of `2026-11-14-social-contest-redesign.md`; read that file's head first; reference under CLAUDE.md §0.05, nothing reads it at runtime; applied by stage 3, a Sonnet lane, and deleted with the suite when v12 is adopted)

---

## F. The fold map

Paths: `wp` is `proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12/workplan_v12_`; line numbers are those read
on 2026-11-14 at `1257a4a` and are a guide: every edit is located by its quoted text or its handle. An action is one of
ADD (new text), EDIT (the quoted text changed or extended), REPLACE (an item's step or body), DELETE, RENAME (scripted),
NONE (already true in the tree). The plan is edited; no code is.

### F.1 The new batch, and its place in the graph

| what | action | where | text |
|---|---|---|---|
| the batch's part | ADD a file | `wp` + `part18_cont2.md` (after BA1's `part18_cont.md`, before B12a's `part19.md`: reading order is execution order) | a head in the form of `wp part22.md:1-11` (title "part 18, continued again: Batch B24p-sc-proceeding"; Status PROPOSED; "Written against" the tree at `1257a4a`; "What this part holds"; "Words"; "Paths", with **RD** = `proposals/2026-11-14-social-contest-redesign.md` and its parts); then, copied whole: part 3 of this proposal from the line `## Batch B24p-sc-proceeding` to its end, and part 4 from `### B24p.13` to the row `STOP. Batch B24p-sc-proceeding closes here` |
| why S12 | — | — | it needs the drawn attributes (B01a, landed), the skill surface and `pool_of` (B04), the one continuous sampler, the obstacle roster and the signed channel (B05), the keyed `Draw` (B06) and the rooms an act is heard by (B07). Those close at S9. B09 runs alone at S10 and B10 follows it; S12 is the first step with parallel lanes, and B24 (S13) is the first batch that needs it. It comes before every batch that sets a social setting: B24.37, B24a, B27, B28, B98 |
| why before B24 | — | — | B24 builds the hearing as a sitting of exchanges. Under R6 that run is the proceeding's, so it is built once, here, with the six roles in it, and B24 adds the evidence board, the issue ladder, the faults, the ballots' leans and the played decider to the same entry. Building B24 first would write a second loop and then rewrite it |
| the calibration batches | — | — | B05.22 and B05.23 calibrate the single roll at S7, before this batch can exist. They stand for the single-roll verbs and for the dials the fight shares (`pool_add`, `pool_floor`, `opposition_rate`, `difficulty_ob`); for the influence verbs they are PROVISIONAL and B24p.23 re-reads them (F.3). Moving them here would strand B05's second half, which gates on B05.23 (wp `part8.md:53`) |

### F.2 The head parts

| file : anchor | action | text |
|---|---|---|
| `wp` + `.md`, the id-block table (the row `B24-sc-hearing \| SC \| ED-SC-0045..0047`, `:413`) | ADD a row after B24a's | `\| B24p-sc-proceeding \| SC \| ED-SC-0054..0056 (1+2) \| H-856..H-909 (49+5) \|` `[ASSUMPTION: the table's last allocated ids are ED-SC-0053 and H-855 — basis: its B28 and B99 rows; the applier reads the table's last row and the "next_free after B00" sentence and continues from them]` |
| the same file, the sentence *"`next_free` after B00, as this table leaves it"* | EDIT | `SC 54` → `SC 57`; `H-855` → `H-909` |
| the same file, the parts table (the row `B24-sc-hearing \| workplan_v12_part22.md`, `:491`) | ADD a row before B12a's | `\| B24p-sc-proceeding \| workplan_v12_part18_cont2.md \|` |
| `wp` + `part2.md`, the batch table (the row `B24-sc-hearing \| SC \| W13 \| S13`, `:130`) | ADD a row before it | `\| B24p-sc-proceeding \| SC \| W12 \| S12 \| 0 \| 18_cont2 \| 24 (B22 R1 +.99) \| MOVER (behaviour 4) \| 14 \| B00, B01, B01a, B02, B03, B04, B05, B06, B07 \|` |
| the same table, B24's row | EDIT | its gates cell gains `, B24p` |
| `wp` + `part2.md`, the step table (`\| S12 \| BA1 (IN), B11 (FI), B15 (PC), B21 (FA) \|`, `:74`) | EDIT | `\| S12 \| B24p (SC), BA1 (IN), B11 (FI), B15 (PC), B21 (FA) \|` |
| the same file, the merge-order rows for S12 (`:253-256`) | ADD a row first; EDIT the four | `\| S12 \| B24p \| 15, 19, 20, 23 \| — \| — \| B24p.99 \| 1 of 5 movers \|`; `1 of 4` → `2 of 5`, `2 of 4` → `3 of 5`, `3 of 4` → `4 of 5`, `4 of 4` → `5 of 5` |
| the same file, the close table (the row `B24-sc-hearing \| 22_cont:263`, `:203`) | ADD a sibling row | in B24's form, the cells read off the new part (the line of its STOP row; its UNDECIDED count 4) |
| `wp` + `part2_cont2.md`, the id table's copy (`:539`) | ADD the same id row | as the first row of this table |
| every head table that chains batches by file with `→` (the file census, the serial-edge table) | EDIT, by script | in each chain for `roll.py`, `sigma.py`, `queries/inputs.py`, `arrangements.yaml`, `data/arrangements.py`, `rosters.yaml`, `data/fixtures.py`, `verb_table.yaml`, `module_contracts.yaml`, insert `B24p` immediately before `B24` (or before `BA1` where the chain has it and no `B24`); add a chain `harness/pairs.py: B01a → B24p` |
| `unified/DECISIONS_ANSWERED.md` | ADD rows, the next free `A-` numbers | one row per ruling R1 to R6 and R10 of `2026-11-14-social-contest-jordan-rulings.md`, Jordan's words as quoted there, consequence: this proposal and Batch B24p |

### F.3 Existing items: replace, delete or edit

**B01a and B05.**

| handle | action | exact edit |
|---|---|---|
| B01a.06 | NONE | amended for J-12 and landed (`1257a4a`); COL §4 item 8 is closed |
| B05 batch block, `UNDECIDED` (U-11) | EDIT, append | `The flatness of the argument's curve is answered by Batch B24p-sc-proceeding: an influence verb is a proceeding whose speech reads six attributes, each on its own operand (RD §B). This batch's calibration of those verbs is PROVISIONAL until B24p.23.` |
| B05.21 | EDIT, append to step 1's `standard` sentence | `⚠ Re-keyed by B24p.05 and B24p.07: the member's operand becomes the speaker's shortfall of Grace against the level's demand (`standard_demand`, RD §B.5 a), not the level's bare size; until B24p it reads as written here, at step 0.` |
| B05.22 | EDIT, append to INSTRUCTION | `PROVISIONAL for the influence verbs (`tell`, `lie`, `speak`, `argue`, `interrogate`): B24p.23 re-points each C-row that reads a social roll between persons to the abridged proceeding under `conversation` and re-reads it as the middle bin of a curve.` |
| B05.23 | EDIT, append to INSTRUCTION | `The values set here stand for the single-roll verbs and the fight's read of the pair. For the influence verbs they are the interim B24p.23 re-reads; `standard`'s row values set here are re-set there as demands on Grace.` |
| B05.24 | EDIT the rule sentence's last clause | from *"a verb that hands its act to a subsystem (a fight, a field) names none, and the subsystem reads him by its own rule."* to RD §D.4's sentence: *"... a verb that hands its act to a subsystem (a fight, a field, a proceeding) names none, and the subsystem reads him by its own rule; a verb that influences a person by words is such a verb, and its row says which proceeding it opens and whether in full or abridged."* |
| B05.24 | EDIT step (2) | *"(32 brute, 31 efficacy, 4 hand-off rows)"* gains: `; of the 31, six (`argue`, `tell`, `lie`, `speak`, `interrogate`, `determine`) are hand-offs to the social subsystem by R3 and R6 and carry their `governing:` cells only as an interim, until B24p.19 (five) and B24.08 (`determine`)` |
| B05.25 | EDIT, append to step 1 | `The cells of `argue`, `tell`, `lie`, `speak`, `interrogate` and `determine` are an INTERIM (R3, R6, RD §D.4): B24p.16 writes their `proceeds:` cell beside them, B24p.19 deletes `governing:` and `opposed_attribute:` on the first five, B24.08 on `determine`.` |
| B05.25 | EDIT step 3's kind rule | after *"(c) the exemption (its prize's `person_inputs` is `own`)"* add: `or, from B24p.16, a `proceeds:` cell` |

**BA1.**

| handle | action | exact edit |
|---|---|---|
| BA1.13 | EDIT, append to INSTRUCTION | `A row carrying `proceeds:` (B24p.16) is corrected in that cell (the row it opens and the form, RD §D.1), through `_check_proceeds`; it has no `governing:` to correct.` |
| BA1.13 | EDIT `DEPENDS ON` | add `V12 Batch B24p-sc-proceeding (merged first in S12: B24p.16, B24p.19)` |

**B24 (the hearing).** Its batch block gains `GATE: Batch B24p-sc-proceeding` after `GATE: Batch B11-fi-readers`.

*Scripted renames*, over `wp part22.md`, `part22_cont.md` and every later part and head part that names them (`grep -rl` each old string under `master/workplan_v12/`):

| old | new |
|---|---|
| `social_contest.hearing` | `social_contest.proceeding` |
| `modules/social_contest/hearing.py`, then any remaining `hearing.py` | `modules/social_contest/proceeding.py`, `proceeding.py` |
| `` `hear` ``, `hear(`, `::hear` | `` `proceed` ``, `proceed(`, `::proceed` |
| `HearingInput`, `HearingTurnView`, `HearingOutcome` | `ProceedingInput`, `ExchangeView`, `ProceedingOutcome` |
| `hearing_input` | `proceeding_input` |
| `hearing_moves`, `hearing_faults` | `proceeding_moves`, `proceeding_faults` |
| `` `Seat(id, pool, modifier, lean)` ``, `` `Seat.lean` ``, `` `Seat` `` (backticked, in `part22*.md` only) | `` `Decider` ``, `` `Decider.lean` ``, `` `Decider` `` |

Not renamed: `headless --world hearing`, `build_hearing`, the test files `test_sc_hearing_*.py`, the word *sitting*, `closing_odds`, `sitting_exchanges` (a hearing is a proceeding before a bench, and these name the hearing).

| handle | action | exact edit |
|---|---|---|
| B24.03 | REPLACE step 1's roster sentence | `proceeding_moves` exists (B24p.01) with `argue`, `press`, `divert`, `deceive`, `concede`, `rest`. This item ADDS the rows `present`, `answer`, `impugn` and the bench's `rule`, `adjourn`, each with B24p.01's cells and an `effect` of its own (`exhibit`, `answer`, `impugn`, `rule`, `adjourn`, added to the loader's closed set); creates `issue_rungs` and `proceeding_faults` as written; and gives `concede`'s row `descends: true` (on a type with an issue ladder a yield also descends one rung) |
| B24.03 | EDIT step 2 | the prize row `a verdict` keeps `module_entry:` (renamed) and needs no `proceeding_entry` (B24p.19 falls back to `module_entry`) |
| B24.04 | EDIT | the `capability:` column exists (B24p.01); this item writes the map form on `argue` and `answer` and `argue` on `impugn`, and the loader's map refusals |
| B24.05 | REPLACE step 1 | `Speaker`, `Decider` (HEAR_B's `Seat`), `ProceedingInput`, `ExchangeView`, `Exchange`, `ProceedingOutcome` exist (B24p.02). This item adds the record `Exhibit` as HEAR_B gives it and, each with a default so B24p's callers are unchanged: `ProceedingInput.exhibits`, `.bears`, `.admits`; `ExchangeView.board`, `.hand`; `Exchange.exhibit`, `.target`, `.entered`, `.struck`, `.fault`; `ProceedingOutcome.standing`, `.faults` (HEAR_B's `ballots` is `verdicts`). The settings HEAR_B put on the input (`proof_level`, `answer_step`, `answer_ob`, `fault_step`) travel in `ProceedingInput.dials` |
| B24.06 | REPLACE steps 1 and 2 | `proceeding.py` exists with `proceed`, `closing_odds` and the run (B24p.11, B24p.12): order, view, decide, record, stop, close are not rewritten. This item adds to `_exchange` the effects `exhibit`, `answer`, `impugn`, `rule`, `adjourn` and the rung's descent on a `yield` (HEAR_B's tables), the four faults, and to `_ballot_input` the board: one `proof_level` per whole unit of net standing weight and `fault_step` levels. Standing arguments are already the track (B24p.10): **`argument_step` is not created; it is `track_step`** |
| B24.06 | EDIT TESTS | `test_hear_with_no_exhibits_is_todays_roll` becomes `test_a_sitting_of_no_exchanges_is_todays_roll`: with `ProceedingType.exchanges == (0, 0)` the presiding seat's ballot equals `roll` on `determine`'s record for the same key |
| B24.06 | DELETE step 4 | the composition row exists (B24p.12) |
| B24.07 | EDIT | strike `argument_step` from the settings (and its H row: four rows, slots 1 to 4); the batch block's `DIALS AT CONTROL` and `IDS` lines likewise (`H 9`) |
| B24.08 | EDIT, append | `determine` also gains `proceeds: {row: docket, form: full}` and loses B05.25's interim `governing:` and `opposed_attribute:` in this commit (RD §D.2, §D.3) |
| B24.09 | REPLACE steps 1 and 2 | `rites:`, `_RITE_KEYS` and the row key `rite:` exist (B24p.03). This item adds `bears` and `disclosed` to `_RITE_KEYS`; the row `default` in the map form `{moves: {for: [argue, press, divert, concede, rest, present, answer, impugn], against: [the same], bench: [rule, adjourn]}, faults: [the four], bears: {…}, disclosed: true}`; and re-points `arbitration`, `legal_trial`, `tribunal`, `parliamentary_debate`, `council_of_state`, `excommunication_deliberation` from `rite: contest` to `rite: default`. `questioned` gains `present` and `answer` for both sides and `bench: [rule, adjourn]`. The sentence about a `None` arrangement goes: no computed case has one after B24p.15 |
| B24.10 | REPLACE step 1's first sentence and step 3 | `proceeding_input` and the provider path exist (B24p.13, B24p.14). This item adds to the builder: the case file's stages as exhibits; `bears`, `faults`, `admits` from the rite and the row; `state` read back from the case file for a resumed sitting; SC-02's commit term as `Decider.lean`; the engagement read; and the switch: at `sitting_exchanges` 0 a `determine`'s type is built with `exchanges (0, 0)`, so no exchange runs and the close is today's draw (gate 1). It passes the decider: `host.deciders.get("social_contest.proceeding")` for a played person, else B24.13's |
| B24.11 | EDIT step 3 | the veto is `sigma.act_margin`'s (B24p.14); this item fills `Decider.lean` from `declared_votes_by_member` and deletes the `vote` conjunct as written |
| B24.12 | EDIT, append to (1) | the cost terms gain: a mark taken and esteem lost in the room (RD §B.5, §B.6), each read off `ExchangeView.own` |
| B24.13 | EDIT step 1 | the decider returns a `Choice`: the move by `key="hearing_move"` over `proceeding_moves`, and the ground by a second key `argument_ground` over `rosters.yaml: grounds`, each ground scored on the believed values in `ExchangeView.read` (never the true ones) |
| B24.14 | EDIT | the Event's `ending` is written by B24p.20; this item adds the case-file copy (`Record.stages`) and the `stages` write on `determine`'s row |
| B24.29 | REPLACE the draw's probability | the chance that the deposited sign is the true one is `acc` of the viewer's reading (B24p.08: his Attunement and his `insight` rank against the seat's Grace), deposited by B24p.22's path. `bench_read_base`, `insight_gain` and the `bench_reading` uses row are not created (one reading, one ladder: CLAUDE.md §0.06 S); H slots 9 and 10 are returned. Gate 2 is read at Attunement 2 and 5 |
| B24.30 | EDIT step 1 | `offer` and `accept` are rows of `proceeding_moves` with effects `offer`, `accept`; under `mutual` nobody is balloted (B24p.12), so *"skip the closing draw and the ballots"* is already the entry's behaviour; the rite row `mutual` is in B24p.03's map form and `negotiation` moves from `rite: contest` to it |
| B24.32 | EDIT check 8 | the `STOPS IF` goes: `Decider` carries `moved_by`, so a trait moves one seat's ballot odds through the `fit` source; UNDECIDED (6) is closed |
| B24.32 | ADD check 11 | `test_sc_proceeding_data.py::test_the_rows_carried_from_the_kernel_load_and_run_a_sitting`: `rally`, `inquisition_hearing`, `excommunication_deliberation` and `audience` each load and `proceed` returns an outcome under them (RD §C.9): the deletion's falsifier now sees the catalogue (COL §4 item 6) |
| B24.33 | EDIT step 3 | the `persuasion_track` row is already deleted (B24p.12); the rest stands |
| B24.35 | REPLACE step 2 | the four uses rows are NOT written. The four `when` functions of step 1 are kept and feed `Speaker.backed: tuple` (the grounds whose condition holds for this act; default every ground), a field this item adds; `proceeding.LEVERAGE["fit"]` counts a ground's positive fit only when the ground is in `backed`. So a ground must be chosen AND backed (a cited record for `evidence`, a held consequence, the hearer's creed, regard of at least 3), and one owner sizes what a ground is worth (`fit_level`). Test (b) reads the `fit` source |
| B24.37 | EDIT | `argument_step` and `insight_gain` leave the sentence of settings that stay at control |
| B24.41 | EDIT INSTRUCTION | items (3) and (6) are built for the room by B24p.07 and B24p.18 and the design cites them. Item (1) has its carrier: the `ending`'s per-side marks and esteem (B24p.20), which WITNESS deposits; the design decides what regard does with them. Items (2), (4), (5) stand |

**B24a, B25, B27, B28, B32, B33.**

| handle | action | exact edit |
|---|---|---|
| B24a.01 | ADD a step | when a `determine` can open a `resolution` Record under a `Record`-disposing row, `parliamentary_debate` takes `disposal: declared` and `quorum: majority` (the loader admits the literal; `act_margin` reads it as more than half of the verdicts) `[ASSUMPTION; Jordan to correct]` |
| B24a.04 | EDIT | `rosters.yaml: authorities.by_faction` and the row key `authority:` exist (B24p.01, B24p.03); this item adds `scope:` on offices and the conjunct in `may_determine`, which reads `authority:`. The two rites are rows in the map form: `accusatorial` = `default`; `inquisitorial` = `questioned` with the evidence and bench moves and `disclosed: false`. `legal_trial` → `rite: accusatorial`; `inquisition_hearing` → `rite: inquisitorial` |
| B25.14 | EDIT, a pointer for the FI lane | when `interview` is drawn its row takes `proceeds: {row: questioning, form: full}` (RD §D.1); OBS's `approach` source (`press_level`) is the `press` move and is not a second lever `[UNVERIFIED: B25.14's body was not opened]` |
| B27.05 to B27.08 | EDIT B27.05 | `_eff_argue` receives `topic` and, under a `hearers` disposal, runs once per verdict (B24p.20); B27.07's lost argument reads the act's own band |
| B27.16 | EDIT step (2) | readers landed for `order` (B24p.11), `floor` (B24p.13), `venue_min_rank` (B24p.15) and the five keys of B24p.03: they are kept and cited |
| B28.10 | EDIT | the `commitment` member's roster row carries `bound: host` and `eased_by: reason` (B24p.05) |
| B28.13 | EDIT, append | `covenant` takes `proceeds: {row: negotiation, form: full}` |
| B28.34 | EDIT INSTRUCTION (1) | each point is decided onto the proceeding's input: a teller's point a level on `Speaker.levels`, a hearer's point an operand on `Speaker.operands` with its `eased_by` cell. Two points are struck as already carried: the teller's reason (RD §B.2) and attunement (RD §B.3). *Knowledge of the other person* is `Speaker.accounts` (B24p.13), which this design may narrow per term |
| B28.35 | EDIT steps 1, 2, 4 | the builder is `proceeding_input`; the self-plea's `against` speaker is the accuser, else the presiding seat (the rule is unchanged) |
| B32.15, B33.18, B33.23 and any later item that seeds an arrangement row | EDIT | the row carries the five keys of B24p.03 (`rite`, `exchanges`, `authority`, `presumes`, `strikes`) or the loader refuses it; `acclamation`: `rite: address`, `exchanges: [1, 1]`, `authority: none`, `presumes: none`, `strikes: 0` |

### F.4 The dials at control, for B98

B98's batch block gains `GATE: Batch B24p-sc-proceeding`. Three positions are added at B98's next free handles:

| setting | set by | target reading |
|---|---|---|
| the forty-six settings of RD §B that B24p.23 sets | B24p.23; **re-read by B98** on the finished realm with `pairs proceeding`, each against its three-point sweep | the BATCH GATE's role readings of B24p (each of the six keys a SLOPE off 0 in at least one type; no DOMINANT above 0.90) |
| `reading_kept` | B98 (flip to on) | B24p.22's falsifier: a kept reading is right more often at Attunement 6 than at 2 and never certain; the ledger's growth per season quoted |
| `presumption_level`, `strike_level` | no batch | none stated: B98 writes each `BLOCKED (design: no target reading)` unless Jordan gives one |

### F.5 Hash movers, the re-pin, the ids

- **Movers**: B24p.15 (behaviour: a computed docket item names a row), B24p.19 (behaviour: five verbs resolve through the proceeding), B24p.20 (behaviour and encoding: the `ending`; a cohort addressed is moved hearer by hearer), B24p.23 (behaviour: the roles on). Every other position is EQUAL and says how that is read.
- **Re-pin**: once, at B24p.99 (Jordan, R10: *"we can re-pin after it's been built"*). B24's re-pin at B24.99 is then read against B24p's after-reading through the S12 merges.
- **Ids**: ED-SC 1 (B24p.16); H 49 as drafted, H 50 after R11 (B24p.04's `speech_blend` pointer row; the plan's block, `wp part22_b24p.md` `IDS:`, is the owner). B24 returns three H slots (B24.07's `argument_step`, B24.29's two).

### F.6 The twenty-two contradictions (COL §8): which side wins

| # | the thing | wins | why |
|---|---|---|---|
| 1 | is reading the room an attribute | R1: Attunement reads it | the latest ruling; PROC's four things read are kept as what the reading returns (RD §B.3) |
| 2 | Attunement's place in `argue` | ED-IN-0350 and R1: it informs the choice | the 2026-11-13 averaged cell (B05.25) is the interim; R1 restates the choice-side sense |
| 3 | which attribute is primary | none is | R1 gives each attribute its own operand; the audience's `proof_weight` changes how much case and manner count (N3). v30's per-adjudicator primary and B05.25's mean are both replaced |
| 4 | who speaks first | the row's `order`; `for` opens under `alternating` | v12 already takes `order` (B24.06); the opener is `[ASSUMPTION]` |
| 5 | where composure lives | Grace (the cost of a mark) and Will (whether one is taken) | R1; v2's and v30's Charisma buffer and P4's Spirit-and-Focus faculty are replaced |
| 6 | genre: chosen, derived, refused or priced | priced, never refused (R-16) | a ground is chosen and priced by its fit and, from B24.35, its backing; no genre key is read |
| 7 | the issue ladder's rungs | HEAR_B's four (B24.03) | unchanged |
| 8 | how a panel decides | A-14: a draw on each voter | the standing weight survives as the seat's `modifier` level |
| 9 | appeal | R-35 and A-39 | resolved before this proposal |
| 10 | is the audience a concept | R4: yes | as a computed kind of the room (RD §C.5); the reductive audit's *"audience dies"* is refused |
| 11 | how many kinds of proceeding | as many rows as the data holds | thirteen after B24p; a kind is a row, never code |
| 12 | public display | R-21 stands, and R4's rally is built beside it | a rally disposes nothing: each hearer is moved for himself |
| 13 | what one exchange is | R6: one speech, one draw; a proceeding is a run of them | v30's interaction algebra and the kernel's bout retire with the kernel |
| 14 | the opposed obstacle | A-79 (0.4 a point) | B05's; the proceeding composes through `roll.obstacle` |
| 15 | what excommunication disposes | `ban` (the row's assumption) | unchanged |
| 16 | does office add to a roll | A-12: yes, one level | it reaches a speech on `Speaker.levels` and a ballot as `Decider.modifier` |
| 17 | ethos, pathos, logos | *not fields* | what moves a person is his own (RD §B.3); the room has one `proof_weight` |
| 18 | genres: two or three | neither is carried | irrelevant after B24.33 (ladder step 2): the style system that needed them retires |
| 19 | does a lie need a mechanism | yes (B28.11) | in a proceeding it is the `deceive` move |
| 20 | does a detailed denial help | open | Jordan's (D-7); nothing here depends on it |
| 21 | Face and standing | S-7: never stored | esteem lives in one sitting; what persists is read from Events |
| 22 | a panel's default size | none | dies with the kernel; a bench is `judging_set` |

### F.7 The questions that survive the ladder, with the plan's default meanwhile

Two. Each overwrites the letter of a ratified ruling, which CLAUDE.md §0 reserves to Jordan. **J-SC-1 is ANSWERED**
(Jordan, 2026-11-14, R11: *"argument dice is Presence and/or Reason depending upon content of argument and venue"*):
neither option as written; the dice are a blend of Reason and Presence weighed by the content class of the speech and
the venue's `reason_bias` (RD §B.2 a), and ED-IN-0350's letter is superseded by his own later words.

| # | question | option A (the default this proposal builds) | option B | what differs in play |
|---|---|---|---|---|
| J-SC-1 (**ANSWERED, R11**: a blend, RD §B.2 a) | **What are the dice of an argument?** ED-IN-0350 (ratified 2026-11-05) says `argue`'s pool attribute is Presence; R1 (2026-11-14) says Reason *constructs* the argument and charisma is *delivery*. | Reason is the dice; Presence is the share heard and the leverage of delivery, and is the larger slope in an open room (RD §B.2, §B.4) | Presence is the dice; Reason is leverage (proofs and the account of the other side) | under A a bench is won by the better case and a crowd by the better speaker; under B the better speaker has the wider swing everywhere and a learned, graceless speaker has no home ground. One cell decides it: which attribute `_speech_input` passes to `pool_of` |
| J-SC-2 | **Does the wrong kind of argument cost, or only fail to help?** v30's armature (ratified at Gate C, ED-1062) says a misaligned style *"simply forgoes the boost"*. | the target's worst ground costs (`misfit_level` `moderate`): reading people matters because misreading them hurts (RD §B.3) | never a penalty (`misfit_level` `None`) | under A Attunement's slope is about twice what it is under B in the scratch probe, and a bold speaker who cannot read a room loses rooms; under B the worst a poor reader does is argue plainly |

Everything else the sources left open was closed by the ladder and is marked where it is decided: the Will and Grace
split (RD §B.5), the commanding verbs (RD §D.1), `determine`'s roll (RD §D.2), consent under `mutual` (RD §A.5), the
rally with no new verb (RD §C.6), a mark carried out of the room (RD §A.2, on v30's rule). The cells that are content and
Jordan's to correct, none of them blocking: the four `read:` cells of `grounds`, `case_rows`, `authorities.by_faction`,
the new cells of RD §C.3, the audience table, and every shipped setting.

---

## G. What this proposal did not decide, and why

1. **The heresy investigation across seasons** (COL A11, A13: the phases, the eight closure conditions, one investigation
   a target, the Parliamentary Stay). The types exist (`questioning`, `inquisition_hearing`,
   `excommunication_deliberation`) and a case file can carry a sitting's state to the next (RD §A.2). The lifecycle is a
   rule about the case file and the calendar, B24a.05's and B27's ground, and no ruling of 2026-11-14 speaks to it.
2. **Deliberation among deciders** (N10; COL J12): the first ballot, pressure from the majority, the one reversal. Every
   ballot here is one independent draw on its voter (A-14, B24.11). Rounds of balloting would be a new `disposal` value
   and one function, and its form has more than one defensible shape; it was not asked for.
3. **What a proceeding leaves beyond its record and the moved pursuits**: attribution (N16), obligations, the domain echo
   and thread co-movement (COL K02, K03), regard from esteem and marks. B27 and B24.41 own what is written; this proposal
   delivers the operands they need (the topic, the per-hearer bands, the `ending`).
4. **Several speakers on a side** (coalitions, corroboration, an advocate; COL D15, D17). `speakers` is a tuple and
   `rank` orders any number, but what an ally adds was not designed; B24a.08 has *self or advocate*.
5. **Manner as a choice** (the register matrix, frank speech's four conditions, the parts of a speech; COL C12, H03, E11,
   N11). Grace is a shortfall against a standard, and a speech is one draw. A chosen register or a slot budget would be a
   second choice per exchange; R1 does not ask for it.
6. **Anchoring and trading across issues in a negotiation** (N6, N7, P39 to P41). B24.30 and B27.14 hold the offer and the
   bundle.
7. **Chamber violence, chain contests, thread use before an adjudicator** (COL D18, E10, D19). None is touched;
   `prac.thread_sensitivity` has no reader here.
8. **Pricing an unknown hearer** (INT E-13). The believed odds stay `None` without a claim on the hearer's skill score
   (B24p.14). A chooser that cannot price `argue` forms it less; whether that is right is B10's and B28's.
9. **`challenge`**. Left as B28.06 draws it; B28.06's body was not opened.
10. **The shipped values.** Every one is an assumption sized on a scratch probe of the formulas, written for this proposal
    and not repository code. The probe's two-sided run used a simplified close (one decider, no hearers). The readings
    that decide are `pairs proceeding` on the built module (B24p.21, B24p.23).
11. **Not opened, and marked where relied on**: B07.04's `audience_of` signature; B04.07's `Person.traits` shape; the final
    names of B04.24's and B05's symbols (`pool_of`, `opposed_ob`, `even_line`, `obstacle_operands`) as built;
    `manifest/registry.py`'s path for `check_contest_prizes`; the faction ids `authorities.by_faction` maps; the columns of
    the head tables in `wp .md` and `part2.md` beyond the rows quoted; B10's edit set (the S12 placement); B25.14 and
    B28.06; whether any seed forms an `argue` today (INT §F item 9). No probe ran the season loop.
12. **The primitives not used.** Of P1 to P45 the design cites P1, P5, P9, P11, P17 and, through M3, the evidence family;
    the procedure, selection and enforcement families (P12 to P38) are the institutions batches' (B32, B33, B40). Of N1 to
    N20 it cites N1, N3, N4, N5, N8, N9, N11, N12, N17, N20; N2 (the story model), N10, N13 to N16, N18 and N19 are not
    mechanised here, for the reasons in items 2, 3 and 5 or because the 2026-08-06 adjudication rejected them as specified.
