# GO-30-F — the plot as the player is shown it: the marker, the stories, the news, the slate, the recap, what is coming, the end reveal, and the trail of reasons

## Status: PROPOSED

Source: `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` §5 (legibility), F-30-03, F-30-13. Jordan, 2026-11-12: *"methods to make the plot legible to player"*; A-48 (the slate is a list of questions for the player), A-49 (reveal only after the line ends), A-33 (a death's news apart), A-43 (a person at zero coherence is unknowable), A-47 (a threshold opens a mandatory scene), A-82 and A-83 (regimes shown as factions of opinion; the felt expectation of a circle). `ED-IN-0352` T2: *"procedurally generated emergent narratives that actually have legible plot points"*. Reference only (`CLAUDE.md` §0.05). Lane GO states the interface; the files are IN's and CHAR's.

Extends `11_GO_player_surface_contract_B.md` (five typed readings and one scene pair; this adds four readings in the same form and three fields to two of its rows) and composes on `09_WR_B_chronicle_that_tells.md` (the focalized telling), `20_NARRATIVE_E` (the year; a question's ground), `20_NARRATIVE_F` (the reign line), `01_CORE_reason_trail_in_the_act_store.md`, `02_CHAR_reason_trail_and_small_edits.md`, `U5d_WR_zero_coherence_unknowable.md`, `30_WR_A` (`era_known`), `30_WR_C` (a strand's subject), `30_WR_G` (the custom).

## What it changes in `engine/season/` at runtime

Nothing in the automated run: every addition is a reader that writes nothing, draws nothing and holds no token; the chooser reads none of them. `View` gains three slots the resolver fills. Every hash EQUAL. A played run gains the plot.

## The rule

**The player is shown what his person holds, and never more.** Every row below is computed from the person's own ledger, own state and own edges, plus a small World half the resolver hands down on the `View` (as `View.odds` is, `decision/sheet.py:40-41`). No reading here takes a `World`, except the end reveal, which is host-side and cannot be called in play. So the player may be wrong: he may serve a dead king (A-33), fear a war that is over (AX-7), believe a liar. That is the game, not a defect.

## What is shown, by surface

| surface | what the player sees | read from | what is withheld |
|---|---|---|---|
| **1. The marker** | the year and season; the era as his person holds it: who he believes rules, in what standing, and what troubles the realm; how old that belief is | `EraMarker` from `person_q.era_known` (`30_WR_A` commit 2), the year roster (`20_NARRATIVE_E` edit 1) | the true holder; conditions he has not heard of |
| **2. His stories** | the strands he holds, each named, with its place, its parties as he knows them, his own part, its last move and whether he reads it open or over; shown by rung up his own ladder, as many per rung as the rung holds (`flow_capacity`), the rest grouped under the one above | `StoryRow` from `flows_known`, `concluded_known`, `Strand.subject` (`30_WR_C`) | the world's strands; moves he holds no claim of; the side he cannot tell |
| **3. News and rumour** | what he learned since he last decided: each item with who told him, at how many removes, how firmly he holds it (a band, not a number), which of his stories it belongs to, and what he held before | `AccountRow` (`11_GO_B` §4) with two added fields | whether it is true; the teller's convictions (he sees only that he half-believes him) |
| **4. The slate** (A-48) | the questions before him in the order his own attention gives them, each with the ground that raised it, the story it bears on, and whether it must be faced; he picks which to attend within his budget; a mandatory one cannot be passed | `Situation.asked` (`11_GO_B` §1) with three added fields | questions the world would raise for one who knew more |
| **5. The recap** | at each season's turn, or when he sits down again: how the marker changed, which stories opened, turned or closed for him, what each of his own acts came to, who he learned had died or taken a seat (two separate lines, A-33), what waits on him, and how many changes he saw with no author | `Recap`, composed from surfaces 1 to 4 and `receipt` (`11_GO_B` §3) | everything he did not learn |
| **6. What is coming** | portents he can read from what he holds: a holder he believes failing; a due of his about to lapse; a petition of his kept waiting; an enemy with a place; unrest he has heard of where he lives; a story gone quiet; and what his circle would expect of the act in front of him | `PortentRow`, each citing the claims it is read from | any forecast the world could make. A portent is a reading of his beliefs and can be false |
| **7. The offer, with the pull** | on each candidate: its terms and believed odds (`11_GO_B` §2), and whether it goes with or against what he believes his circle does | `OfferRow.custom`: `with`, `against`, `none` | the weight itself |
| **8. Regimes, as factions of opinion** | for each person he knows: the side he is committed to, and how the player's person stands to what he has seen that person hold: *of your mind*, *apart*, *against* | read from his own claims of that person's deeds and commitments scored against his own stands | the other's convictions; any number |
| **9. The end reveal** (A-49) | after the line has ended and no continuation is taken: the eras as they were, with what ended each; every strand, concluded or not; and beside each, what the line believed against what was so: the lies believed, the deaths laid at the wrong door, the hands behind the unattributed | `reveal(w, line)`, host-side | n/a: this is the one omniscient view, and it is not a play surface |

**A person at low legibility** (A-43) appears in surfaces 2, 3 and 8 by his acts with no reason line and no standing (`U5d_WR_zero_coherence_unknowable.md`); nothing here predicts him.

## How a narrator reads why (the reason trail)

For any act, in order, each from a record that exists or is on file; items 1 to 7 are `audits/20_NARRATIVE_CHURN.md` §7.5's, and 8 to 10 are added here:

1. *when*: year, season, and the era **as the actor believed it** (`era_known` recomputed from his ledger at that tick);
2. *what reached him*: the question, its ground, and whether it was mandatory;
3. *why it mattered to him*: the pulls, recomputed person-side: a due unmet, the holder he believed sat there, his opinion of his side, his accord with the teller, the lean of his circle's custom;
4. *what he risked*: the odds as he believed them;
5. *how it fell*: the degree, and what the failure cost (`23_STORY_A`);
6. *who saw, who was told, who believed*;
7. *how it closed*: by act, by term or by threshold;
8. *which story it was a move of*, and what it did there: opened, joined, turned, concluded, revived;
9. *whether it turned the era*, and to what;
10. *what it left behind for the next act* (the write of `30_WR_D` §3): the grievance, the claim, the edge.

`harness/chronicle.py`'s line gains `era`, `story` and `left` beside `about` and `why`; the focalized render (`--focus`) prints 1 as the focalizer believed it, and the omniscient render is surface 9.

## The NPC and the AI chooser

The player and an NPC are the same kind of agent (`AUDIT_BRIEF.md`, the chooser charge). The chooser reads the same person-side state these surfaces render, through channels that exist; the surfaces add no input to it.

| what eras, regimes and strife give a chooser | channel (owner) | characterful because |
|---|---|---|
| what is on the table | `questions_for`'s stamps: `vacancies` (mandatory for one who may claim), `flow_stakes`, CR-100's within-stakes, the own-side creed | two persons hold different strands and so different stakes |
| in what order | `attention_key`: tiers, then `flow_capacity` order inside (CR-101's slot) | an NPC takes the first; a player triages (A-48) |
| toward whom | `regard`: stance, deeds judged, dues unmet, waiting, descent | each judges the same deed by his own pursuits |
| whose word | `_credit` by `commensurate` or `accord` | a fringe man half-believes |
| in what manner | `projected_axes` with the custom lean (`30_WR_G`) | his house leans him; he may still not go |
| at what odds | `View.odds`, `refused_before` | he learns from his own refusals, privately (D-46) |

Nothing in any subsystem hard-codes what an NPC does in an interregnum, a war or a famine: there is no era branch in `decision/`, and the rename falsifier of `30_WR_A` covers it.

## Instructions to code

Tier: second (sonnet); the port lane renders. All person-side readers live in `engine/season/decision/sheet.py` beside `Situation`, `Offer`, `account`; the host-side one in `engine/season/harness/play_surface.py` beside `receipt`. Land after `11_GO_player_surface_contract_B.md`.

1. **`state/carriers.py::View`** (`:456`): `__slots__` gains `strands`, `calendar`, `head_seats` (and `circle`, `30_WR_G`), each default `()`. The resolver fills them where it builds the View: `strands = world_q.flows_known(w, p)` (it needs the containment tree, so it is the World half), `calendar = (year, season_of_year)`, `head_seats = tuple(sorted(set(HEAD_SEAT.values())))`. `tests/test_season_shape.py`'s `EXEMPT_CEILING` counts the tuple once (its own comment) and is unmoved; if the count moves, re-pin and say so. A View with the new slots empty behaves as today.
2. **`decision/sheet.py`**:

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

   `portents` reads only: his claims of `body.changed` on `marker.holder` or on the believed holder of a seat among `v.questions`' referents (`failing`); his own termed edges whose term ends within one year of `v.calendar` (`due_lapsing`); his own petitions with a `visitor.kept_waiting` claim (`kept_waiting`); a believed holder he regards below 0 on a referent of his questions (`enemy_placed`); `person_q.stability(p, rung, window)` below 0 on a rung of his own ancestry that `v` names (`unrest`); a `StoryRow` not concluded whose `last.when` is older than the estimate window (`gone_quiet`). The closed roster `portent_kinds` is those six, in `rosters.yaml`. A portent with no basis is not emitted.
3. **Fields added to existing rows** (`11_GO_B`): `AskedRow.ground: Optional[str]` (`20_NARRATIVE_E` edit 2's `Question.grounds`), `AskedRow.mandatory: bool`, `AskedRow.story: Optional[str]` (the `StoryRow.id` whose subject or referents hold a referent of the question); `AccountRow.story: Optional[str]`, `AccountRow.firmness: str`; `OfferRow.custom: str` (`with` when the candidate's alignment dotted with `custom_of(p, v.circle, window)` is above 0, `against` below, `none` when he holds no custom). `firmness` bands are one function, `sheet.firmness(confidence, fx)`, cut at one third and two thirds of `Fixtures confidence_default` (100, `data/fixtures.py:263`). No banding of confidence exists in the tree (`descriptor_registry.yaml:204` rules `player_sees: bands` for affiliation intensity and says "band NAMES are unauthored"), so the three names and the two cuts are this file's `[ASSUMPTION; low; Jordan to correct; revert: show the number]`.
4. **Standing to another, surface 8**: `sheet.standing_to(p, other) -> str` in `("of_your_mind", "apart", "against", "unknown")`: over his own claims of `other`'s deeds whose kind engages an affiliation (`affiliation_engagement`), the sign of the mean of `conviction_stand(p, that affiliation)` times the cell's sign; `unknown` when he holds none. Person-side; it never reads `other`'s `conviction`.
5. **Names.** New data file `engine/season/telling.yaml` (authored for play, not canon; `meta.authority` says so, as `worldgen_names.yaml` does in `21_PROCEDURAL_E_names_and_texts.md`), read by `harness/chronicle.py` and exported for the port: `era_names:` rows keyed `(standing, first condition or none, regard band)` giving a template over `{holder}`, `{year}`; `story_names:` rows keyed `(opened_on kind, class of the first subject id)` over `{subject}`, `{place}`. The loader refuses a key outside the rosters and a template naming a field the tuple lacks. No template names a person, seat or faction (the rename falsifier). First content is one neutral template per key, e.g. `(vacant, none, *)`: "the empty seat, year {year}"; `(held, civil_war, ill)`: "the war against {holder}"; richer text is `21_PROCEDURAL_E`'s lane.
6. **`harness/play_surface.py::reveal(w, line) -> Reveal`**: `eras` (`world_q.flows_in(w).eras` with `opened_by`, `closed_by` and their codes), `strands` (world), and `held_against_true`: for each claim in the ledgers of `line`'s persons that names a doer, holder or death, the world's answer beside it (`state/attribution.py::actor_of` for a doer; live Tenures for a holder; `w.persons` for a death). Refuses (`Forbidden`) unless `world_q.endings_reached(w)` is non-empty or no person of `line` is alive, **and** the host passes `continuation=False`. `harness/chronicle.py`'s omniscient render is called only from here in a played run.
7. **`harness/chronicle.py::lines`** (`:128`): fields `era` (the era of the act's first Event by `era_turns`; under `--focus`, the focalizer's `era_known` at that tick), `story` (the world strand holding one of the act's Events; under `--focus`, his), `left` (the act's durable writes by `30_WR_D` §3's definition, as `kind:subject` pairs).
8. **Tests**: `engine/season/tests/test_rem30_character_sheet.py` (the covering file for `sheet.py`): `test_the_marker_names_the_holder_he_believes_not_the_one_who_sits`; `test_a_death_and_a_vacancy_are_two_recap_lines`; `test_stories_are_presented_by_capacity_and_the_rest_grouped`; `test_every_portent_cites_a_claim_he_holds`; `test_a_portent_can_be_false` (planted lie: the portent is emitted, and the world disagrees); `test_no_reader_in_sheet_takes_a_world` (the AX-2 path scan already covers `decision/`; this asserts the new functions' signatures); `test_standing_to_never_reads_the_other_s_conviction` (the other's vector changed, the answer equal). `engine/season/tests/test_in37_chronicle.py`: `test_reveal_is_refused_in_play`; `test_reveal_lists_a_believed_lie_beside_the_truth`. Each plants and asserts it asserted.

## The gate (execution artifacts)

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.chronicle --seed 0 --seasons 2 --focus <a seated pid>
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 4 --arms off off --stories --seat <pid>
python -m pytest engine/season/tests/test_rem30_character_sheet.py engine/season/tests/test_in37_chronicle.py -q
```

Expected: (1) `development_space` with `take_ranked` still reproduces the automated hash (`5ab73af2…` at seed 0, one season, `11_GO_B`'s control): the surfaces changed nothing; (2) a seated run prints, each season, a marker, at least the slate, and a recap whose `unattributed` count is printed; (3) the **seat test** (`23_STORY_D` `--seat`, S-73): of the stories the census counts in the world, the share one seat could follow from his own surfaces is printed per seed; today it is 0 (0 of 83 persons hold a strand after one season, audit §12 P-2), and the target after the carriers land is that at two seeds or more of three a seated head-seat holder follows at least one story from opening to close; (4) a reader who did not build the engine, given one season's recap for one seat, can say who rules, what is troubling the realm, and one thing that is coming (the reader test of `09_WR_audit_addendum_B.md` §3.8 step 6, applied to the recap).

## The falsifier, and its control

- A surface that differs for two persons with identical ledgers, edges and `View` halves: it read the World.
- The marker changing with no claim landing: it is reading live state.
- A portent whose basis is empty, or one that is never false across five seeds with lies in play: it is omniscient.
- `reveal` callable during play.
- Control: the unseated run's hash, equal with every surface computed for every person each season.

## Dependencies

`11_GO_player_surface_contract_B.md`; `30_WR_A` commit 2; `20_NARRATIVE_C` (`held_by`), `20_NARRATIVE_E` edits 1 and 2; `30_WR_C` commit 1a (`Strand.subject`); `30_WR_G` commit 5 for `OfferRow.custom` (before it the field reads `none`); `23_STORY_D` for the seat test. The port work is behind the port gate (B10-20); these are oracle readings.

## Layer 1

`04` §C.11 (hidden in existence, never in arithmetic; `explain`): kept, **STRUCTURAL**; a portent shows its basis, and a withheld value stays withheld. AX-2 and AX-7: every reader is person-side; the `View` carries ids and tuples, never a World (S18.1): **STRUCTURAL**, checked by the path scan. `View.__slots__`: a language construct, counted once by `test_season_shape.py`: **MECHANICAL**. A-49's refusal in `reveal`: **MECHANICAL** (its test). The text table is presentation: **CONVENTION**.

## NERS reading

- **N.** Without it the engine may produce a succession crisis that the player lives through as fifteen unrelated questions. T2 asks for legible plot points; a plot point nobody is shown is not legible. Holds bottom-up (each claim is filed under a story), top-down (the marker), laterally (one form for every subsystem's news), diagonally (the player's account against the reveal).
- **R.** Strategy needs a picture: who rules, what is open, what is coming, what is expected of me. The player matters by being able to be wrong and to find out. Complete: a person who holds nothing sees a marker reading `unknown`, no stories and no portents, and that is shown.
- **S.** Four readings in the contract's own form; bands where the registry already says bands; it pauses for a mandatory question and for nothing else.
- **E, last.** No new mechanism; nine surfaces from what a person already holds. High.

## Cost class

Small build (oracle readers and tests). The render is the port's.
