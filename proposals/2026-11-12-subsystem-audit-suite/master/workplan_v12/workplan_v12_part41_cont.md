# Workplan v12 — part 41, continued: Batch B38-narrative-regimes, second half, from `B38.74` (`30_GO_F` with `IS-B3-GO-04`, `31_WR_C`, `U5d_SE_cohort_heavy_moves_and_caste`, `IS-B3-SE-02`; the Readings block; `B38.99`; the boundary row)

## Status: PROPOSED (the continuation of the part that holds `B38.51` to `B38.73`; a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

Words, paths and the hash note are the part's head's (the file this one continues). `S/` is `engine/season/`.

---

### B38.74 — the `View` carries what the surfaces read · `30_GO_F` instruction 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/30_GO_F_the_plot_as_the_player_is_shown_it.md` "The rule", "Instructions to code" 1, "Layer 1" (`strands` handed down is "the exception `View.odds` already is … **CONVENTION**"); `unified/U3_CONFLICT_LEDGER.md` C3-L4; rulings A-48, A-49, A-33, AX-2, AX-7.
- ADVANCES: R-04.c1 (the sheet, B34's) is not re-read here; none of the nine by itself; T2 of `ED-IN-0352` (legible plot points).
- INSTRUCTION (instruction 1, copied; line numbers dropped): "**`state/carriers.py::View`**: `__slots__` gains `strands`, `calendar`, `head_seats` (and `circle`, `30_WR_G`), each default `()`. The resolver fills them where it builds the View: … `loop/deliberate.py` computes them beside `odds=believed_odds_query(w, p)` and passes them to `decision/questions.py::assemble`, which constructs the `View` and gains three keyword parameters (default `()`): `strands = world_q.flows_known(w, p)` (it needs the containment tree, so it is the World half), `calendar = (year, season_of_year)`, `head_seats = tuple(sorted(set(HEAD_SEAT.values())))`. `tests/test_season_shape.py`'s `EXEMPT_CEILING` counts the tuple once (its own comment) and is unmoved; if the count moves, re-pin and say so. A View with the new slots empty behaves as today." `circle` is added only if the first half's `30_WR_G` commit 5 did not add it (one owner; read `View.__slots__` at the item's open and say which in the commit body). `year` and `season_of_year` are read from the year roster (`rosters.yaml: seasons_of_year`, `20_NARRATIVE_E` edit 1, Batch B12a).
- WHERE: `S/state/carriers.py` (`View.__slots__`); `S/loop/deliberate.py` (the `assemble` call); `S/decision/questions.py` (`assemble`'s three keyword parameters and the `View` construction); `S/tests/test_season_shape.py` (`EXEMPT_CEILING`, only if its count moves).
- TESTS: `S/tests/test_season_shape.py` → pass (unedited unless the count moves; the commit says which); `S/tests/test_rem30_character_sheet.py::test_no_reader_in_sheet_takes_a_world` is B38.75's.
- FALSIFIER and CONTROL: "A View with the new slots empty behaves as today": the realm hash at seed 0, one season, equal to B38.73's; a `View` that holds a `World` (S18.1; the AX-2 path scan).
- GATE: `python -m pytest S/tests/test_season_shape.py -q` → pass; realm hash at seed 0, one season → equal to B38.73's.
- HASH MOVERS: none (`View` is built per deliberation and is not in `World.content_hash()`'s collections; the chooser reads none of the new slots).
- DEPENDS ON: EXISTS-IN-TREE `S/state/carriers.py::View`, `S/decision/questions.py::assemble`, `S/queries/world_q.py::flows_known`, `S/data/rosters.py::HEAD_SEAT`; V12 Batch B34 (`11_GO_player_surface_contract_B.md`); V12 Batch B12a (the year roster); V12 the first half's `30_WR_G` commit 5 (`circle`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`; IN reviews `View` (the source's lands-it line).
- LANDS IT: B38's producer; `Item: B38.74`, `[skip ci]`.

### B38.75 — the marker, the stories, the portents, the recap, the added fields, and standing to another · `30_GO_F` instructions 2–4 · BUILD · HASH EQUAL
- SOURCE: `proposals/30_GO_F_the_plot_as_the_player_is_shown_it.md` "What is shown, by surface" (rows 1–8), "Instructions to code" 2, 3, 4, 8 (the `sheet.py` tests), "The falsifier"; rulings A-33, A-43, A-48, A-82, A-83, AX-2, AX-7; `U1_GLOSSARY.md` *band* row ("firmness is a **firmness grade**, not a band").
- ADVANCES: none of the nine; T2 (legible plot points), A-48 (the slate), A-82 (regimes as factions of opinion).
- INSTRUCTION (copied; the `round` of `EraMarker.as_of` is the lap, NAMES):
  1. "**`decision/sheet.py`**:
     ```python
     @dataclass(frozen=True)
     class EraMarker:
         year: int; season: int
         holder: Optional[str]         # era_known: who he believes holds the realm's head seat
         standing: str                 # rosters.yaml: era_rule_standings, or "unknown"
         conditions: tuple             # era_conditions he holds open strands of
         as_of: tuple                  # (when, round) of the newest claim the reading rests on
         regard: str                   # band of his regard for `holder`: "well" | "indifferent" | "ill"
     def marker(p, v) -> EraMarker

     @dataclass(frozen=True)
     class StoryRow:
         id: str                       # his strand's id (the claim that opened it)
         opened_on: str                # kind
         subject: tuple                # ids, sorted
         rung: Optional[str]
         parties: tuple                # persons he knows in it
         own: bool                     # one of its moves is his own deed (Claim.doer == p)
         last: Claim
         concluded: bool               # concluded_known
         slot: Optional[str]           # the rung on his ladder that presents it, or None (grouped)
     def stories(p, v) -> tuple[StoryRow, ...]

     @dataclass(frozen=True)
     class PortentRow:
         kind: str                     # rosters.yaml: portent_kinds
         subject: str
         basis: tuple                  # claim ids or own Tenure ids it is read from; never empty
         firmness: str                 # "firm" | "half" | "doubted"
     def portents(p, v) -> tuple[PortentRow, ...]

     @dataclass(frozen=True)
     class Recap:
         marker_before: EraMarker; marker_after: EraMarker
         opened: tuple; turned: tuple; closed: tuple     # StoryRow ids
         deaths: tuple; seats: tuple                     # AccountRow, kept apart (A-33)
         waits: tuple                                    # AskedRow that are mandatory, and his own appointments and waiting petitions
         unattributed: int
     def recap(p, v, since: tuple, before: EraMarker) -> Recap
     ```
     `portents` reads only: his claims of `body.changed` on `marker.holder` or on the believed holder of a seat among `v.questions`' referents (`failing`); his own termed edges whose term ends within one year of `v.calendar` (`due_lapsing`); his own petitions with a `visitor.kept_waiting` claim (`kept_waiting`); a believed holder he regards below 0 on a referent of his questions (`enemy_placed`); `person_q.stability(p, rung, window)` below 0 on a rung of his own ancestry that `v` names (`unrest`); a `StoryRow` not concluded whose `last.when` is older than the estimate window (`gone_quiet`). The closed roster `portent_kinds` is those six, in `rosters.yaml`. A portent with no basis is not emitted."
  2. "**Fields added to existing rows** (`11_GO_B`): `AskedRow.ground: Optional[str]` (`20_NARRATIVE_E` edit 2's `Question.grounds`), `AskedRow.mandatory: bool`, `AskedRow.story: Optional[str]` (the `StoryRow.id` whose subject or referents hold a referent of the question); `AccountRow.story: Optional[str]`, `AccountRow.firmness: str`; `OfferRow.custom: str` (`with` when the candidate's alignment dotted with `custom_of(p, v.circle, window)` is above 0, `against` below, `none` when he holds no custom). `firmness` grades (U1: not 'bands') are one function, `sheet.firmness(confidence, fx)`, cut at one third and two thirds of `Fixtures confidence_default` …. No banding of confidence exists in the tree …, so the three names and the two cuts are this file's `[ASSUMPTION; low; Jordan to correct; revert: show the number]`."
  3. "**Standing to another, surface 8**: `sheet.standing_to(p, other) -> str` in `("of_your_mind", "apart", "against", "unknown")`: over his own claims of `other`'s deeds whose kind engages an affiliation (`affiliation_engagement`), the sign of the mean of `conviction_stand(p, that affiliation)` times the cell's sign; `unknown` when he holds none. Person-side; it never reads `other`'s `conviction`."
  The rule (copied): "**The player is shown what his person holds, and never more.** Every row below is computed from the person's own ledger, own state and own edges, plus a small World half the resolver hands down on the `View` …. No reading here takes a `World`, except the end reveal".
- WHERE: `S/decision/sheet.py` (NEW `EraMarker`, `marker`, `StoryRow`, `stories`, `PortentRow`, `portents`, `Recap`, `recap`, `firmness`, `standing_to`; `AskedRow`, `AccountRow`, `OfferRow` fields); `S/rosters.yaml` (NEW `portent_kinds`, at the end of its family's block); `S/data/rosters.py` (its loader, `roster` route); `S/tests/test_rem30_character_sheet.py`.
- TESTS: in `S/tests/test_rem30_character_sheet.py` ("the covering file for `sheet.py`"), written before the edit and read red: `test_the_marker_names_the_holder_he_believes_not_the_one_who_sits`; `test_a_death_and_a_vacancy_are_two_recap_lines`; `test_stories_are_presented_by_capacity_and_the_rest_grouped`; `test_every_portent_cites_a_claim_he_holds`; `test_a_portent_can_be_false` ("planted lie: the portent is emitted, and the world disagrees"); `test_no_reader_in_sheet_takes_a_world` ("asserts the new functions' signatures"); `test_standing_to_never_reads_the_other_s_conviction` ("the other's vector changed, the answer equal"). "Each plants and asserts it asserted."
- FALSIFIER and CONTROL: "A surface that differs for two persons with identical ledgers, edges and `View` halves: it read the World"; "The marker changing with no claim landing: it is reading live state"; "A portent whose basis is empty, or one that is never false across five seeds with lies in play: it is omniscient". Control: "the unseated run's hash, equal with every surface computed for every person each season".
- GATE: `python -m pytest S/tests/test_rem30_character_sheet.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.chronicle --seed 0 --seasons 2 --focus <a seated pid>` (the pid read at the item's open from `--focus`'s own listing, named in the commit body) → each season a marker, the slate and a recap whose `unattributed` count is printed; realm hash at seed 0, one season → equal to B38.74's. The source's gate (1) ("`development_space` with `take_ranked` still reproduces the automated hash … `11_GO_B`'s control") read once here, `reading @<sha>` of B34's close.
- HASH MOVERS: none ("every addition is a reader that writes nothing, draws nothing and holds no token; the chooser reads none of them").
- DEPENDS ON: V12 Batch B34 (`decision/sheet.py::Situation`, `Offer`, `account`, `AskedRow`, `AccountRow`, `OfferRow`, `sheet.firmness`'s neighbours: `11_GO_player_surface_contract_B.md`); V12 B38.58 (`era_known`), B38.62 (`Strand.subject`), B38.74 (`View` slots); V12 the first half's `20_NARRATIVE_C` (`held_by`), `20_NARRATIVE_E` edit 2 (`Question.grounds`, B38.15) and `30_WR_G` commit 5 (`custom_of`; "before it the field reads `none`"); EXISTS-IN-TREE `S/queries/person_q.py::stability`, `::conviction_stand`, `S/queries/world_q.py::concluded_known`, `::flow_capacity`.
- GLOSSARY: new row *portent*: "a sign a person reads from what he holds that something is coming, which may be false, as an omen is"; owner `rosters.yaml: portent_kinds` and `decision/sheet.py::portents`; rejected: "forecast" (the world's knowledge). Row *firmness grade*: owner → `decision/sheet.py::firmness` (code) if the row exists, else a new row: "how firmly he holds a belief, named in three grades, as one holds a view firmly or half-believes it"; rejected: "band".
- NAMES: `EraMarker.as_of` "(when, round)" → "(when, lap)" (B04.01).
- COST and TIER: small build; `sonnet`, `high`; CHAR reviews `sheet.py` (the source's lands-it line).
- LANDS IT: B38's producer; `Item: B38.75`, `[skip ci]`.

### B38.76 — the names table, and the chronicle's era, story and what an act left · `30_GO_F` instructions 5 and 7 · BUILD · HASH EQUAL
- SOURCE: `proposals/30_GO_F_the_plot_as_the_player_is_shown_it.md` "How a narrator reads why" (items 1–10), "Instructions to code" 5 and 7; `unified/U3_DEPENDENCY_ORDER.md` §6.3 (`engine/season/telling.yaml`: "`09_WR_B_chronicle_that_tells.md` (uses it 'once that table exists') … `30_GO_F` (B38)"); `30_WR_D` §3 (the durable write, copied forward into `null_scenes`'s docstring by `B02.20`).
- ADVANCES: R-04.c1's chronicle line (`09_WR_B_chronicle_that_tells`, B36) gains the era and the story; none of the nine moves.
- INSTRUCTION (copied):
  1. "**Names.** New data file `engine/season/telling.yaml` (authored for play, not canon; `meta.authority` says so, as `worldgen_names.yaml` does in `21_PROCEDURAL_E_names_and_texts.md`), read by `harness/chronicle.py` and exported for the port: `era_names:` rows keyed `(standing, first condition or none, regard band)` giving a template over `{holder}`, `{year}`; `story_names:` rows keyed `(opened_on kind, class of the first subject id)` over `{subject}`, `{place}`. The loader refuses a key outside the rosters and a template naming a field the tuple lacks. No template names a person, seat or faction (the rename falsifier). First content is one neutral template per key, e.g. `(vacant, none, *)`: 'the empty seat, year {year}'; `(held, civil_war, ill)`: 'the war against {holder}'; richer text is `21_PROCEDURAL_E`'s lane." The port export is not built here: the source names no exporter, and none is created (`UNDECIDED` (9)); the loader is a reader in `harness/chronicle.py` `[ASSUMPTION: the loader's home — basis: "read by `harness/chronicle.py`"]`. The first templates are content, listed in the PR body for Jordan (D-19).
  2. "**`harness/chronicle.py::lines`**: fields `era` (the era of the act's first Event by `era_turns`; under `--focus`, the focalizer's `era_known` at that tick), `story` (the world strand holding one of the act's Events; under `--focus`, his), `left` (the act's durable writes by `30_WR_D` §3's definition, as `kind:subject` pairs)." `left` reads the definition where `B02.20` put it (`null_scenes`'s docstring and predicate), one owner.
- WHERE: NEW `S/telling.yaml`; `S/harness/chronicle.py` (`lines`; the `telling.yaml` loader); `S/tests/test_in37_chronicle.py`.
- TESTS: in `S/tests/test_in37_chronicle.py`, written before the edit and read red, `[ASSUMPTION: test names; E-3]`: `test_telling_refuses_a_template_naming_a_missing_field`; `test_no_telling_template_names_a_person_seat_or_faction` (the rename falsifier); `test_a_chronicle_line_carries_era_story_and_left`.
- FALSIFIER and CONTROL: a template that names an id (the rename falsifier); `left` listing a bystander's sighting alone (the definition is `30_WR_D` §3's). Control: harness and data only: realm hash equal.
- GATE: `python -m pytest S/tests/test_in37_chronicle.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.chronicle --seed 0 --seasons 2` → lines carry `era`, `story`, `left`; realm hash at seed 0, one season → equal to B38.75's.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `S/harness/chronicle.py::lines`; V12 B38.57 (`era_turns`), B38.58 (`era_known`), B38.64 (strand states), B38.75 (`firmness`, the regard band names); V12 `B02.20` (the durable-write predicate); V12 Batch B36 (`09_WR_B_chronicle_that_tells`, `--focus`).
- GLOSSARY: none (templates are presentation).
- COST and TIER: edit and data; `sonnet`, `high`; the first templates drafted `sonnet`, `medium` (neutral, one per key).
- LANDS IT: B38's producer; `Item: B38.76`, `[skip ci]`.

### B38.77 — the end reveal, gated on the run's ending · `30_GO_F` instruction 6 with `IS-B3-GO-04` · BUILD · HASH EQUAL
- SOURCE: `proposals/30_GO_F_the_plot_as_the_player_is_shown_it.md` "What is shown" row 9, "Instructions to code" 6 and 8 (the two reveal tests), "Layer 1" ("A-49's refusal in `reveal`: **MECHANICAL** (its test)"); `master/instructions/IS_B3_FA_SE_WR_GO_part2.md` `IS-B3-GO-04` (U4 G-14); rulings A-49 ("Shown only after the line ends and no continuation is taken"); C3-L4 ("`reveal` sits in `play_surface.py` beside the transcript runner"). U3 §2.2 row B38: "`IS-B3-GO-04` with `30_GO_F`": one item naming both (§5.5).
- ADVANCES: GO standalone (S5); A-49.
- INSTRUCTION: `30_GO_F` instruction 6, copied: "**`harness/play_surface.py::reveal(w, line) -> Reveal`**: `eras` (`world_q.flows_in(w).eras` with `opened_by`, `closed_by` and their codes), `strands` (world), and `held_against_true`: for each claim in the ledgers of `line`'s persons that names a doer, holder or death, the world's answer beside it (`state/attribution.py::actor_of` for a doer; live Tenures for a holder; `w.persons` for a death). Refuses (`Forbidden`) unless `world_q.endings_reached(w)` is non-empty or no person of `line` is alive, **and** the host passes `continuation=False`. `harness/chronicle.py`'s omniscient render is called only from here in a played run." `IS-B3-GO-04` (2), copied: "Its refusal reads the run's ending, not the realm alone: instruction 6 refuses 'unless `world_q.endings_reached(w)` is non-empty or no person of `line` is alive'; for a scenario world the first clause becomes 'the ending `scenarios.run` returned is not `None`', so a valley or a spine run can be revealed when it ends. Signature: `reveal(w, line, ending, continuation=False)`." The fidelity proposal's "one host-side reading" is this function; B34 built none (`IS-B3-GO-04`).
- WHERE: `S/harness/play_surface.py` (NEW `Reveal`, NEW `reveal`); `S/tests/test_play_surface.py` (B34's file).
- TESTS: `IS-B3-GO-04` (1), in `S/tests/test_play_surface.py`, written before the edit and read red: `test_reveal_is_refused_while_a_person_of_the_line_lives`; `test_reveal_is_refused_when_a_continuation_is_taken`; `test_reveal_returns_what_the_line_believed_beside_what_was_so` ("a planted lie believed by the seated person appears in `held_against_true` with the world's answer"). `30_GO_F` instruction 8's `test_in37_chronicle.py::test_reveal_is_refused_in_play` and `::test_reveal_lists_a_believed_lie_beside_the_truth` assert the same two claims and are not written: one owner, the instruction item's file (§5.6, the evaluation's rule 2; `UNDECIDED` (10)).
- FALSIFIER and CONTROL: "The three tests; `reveal` callable in play is `30_GO_F`'s own falsifier. Control: calling `reveal` leaves `content_hash()` equal (it writes nothing)."
- GATE: `python -m pytest S/tests/test_play_surface.py -q` → pass; the control (a call to `reveal` on an ended planted run, `content_hash()` before and after) → equal, asserted in `test_reveal_returns_what_the_line_believed_beside_what_was_so`.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B34 (`IS-B3-GO-02`, `B34.20`: the ending reaches the surface; `S/tests/test_play_surface.py`); EXISTS-IN-TREE `S/harness/play_surface.py`, `S/queries/world_q.py::endings_reached`, `::flows_in`, `S/gaps.py::Forbidden`, `S/state/attribution.py::actor_of` `[ASSUMPTION: present at the item's open — basis: named by the source; not opened by this lane]`; V12 B38.57 (`Era.opened_by`, `closed_by`).
- GLOSSARY: none (*reveal* is A-49's word).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B38's producer; `Item: B38.77`, `[skip ci]`.

<!-- A41 append point -->
