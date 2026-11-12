# WR-30-B — regimes: who believes whom, read as bodies that form, grow, split and end

## Status: PROPOSED

Source: `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` F-30-04, F-30-05. Reference only (`CLAUDE.md` §0.05). Lane WR; owner files IN's (`engine/season/queries/world_q.py`, `engine/season/harness/storybar.py`).

Composes on, and restates none of: `20_NARRATIVE_A_stands_for.md` (the one reading of "held": stood for; its fixture `held_reading`), `20_NARRATIVE_D_his_own_side.md` (a faction's `creed:` row; the own-side occasion), `20_NARRATIVE_E` edit 3 with `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` (the one emitter of `conviction.moved`), `20_NARRATIVE_F` (class G5), `08_FI_02_rumour-that-travels.md`, CR-79 (the credit term, landed), CR-104 (`influence_rung`).

**The word.** *Regime* here is the tree's ruled sense (`strife-00` R13, R17): an assemblage of institutions with commensurate modes of understanding and behaving. It is not who rules (that is the era's RULE, `30_WR_A`) and not who fights whom (strife, `30_WR_C`). A regime answers one question: **whose word does a person take.**

## What it changes in `engine/season/` at runtime

Nothing. Commit 1 adds a world reading with no consumer in the loop; commit 2 a harness block; commit 3 one row in `30_WR_A`'s condition table (a reading). Every hash EQUAL. The mechanism by which a regime acts stays the one that is built: `loop/witness.py::_credit` (`:240`) at the telling, and it stays out of the decision field (`ED-IN-0352`: "REGIME conditions belief at WITNESS … and is not read into the field").

## The problem, with evidence

- A regime exists in code as a pairwise sign and nothing else: `world_q.commensurate(w, a, b)` (`:5317`) and `Fixtures regime_gain` (`data/fixtures.py:1086`). No function says which regimes the realm holds, who is in one, which seats it holds or how far it reaches, so none can be seen to form, grow, split or end.
- `20_NARRATIVE_A` (its E-N01) measured the sign as one value: −1 for 1,031 of 1,035 pairs of convinced persons at `build_realm(0)`, because "held" is read as above zero. Under "stood for" the same data gives 130 / 779 / 126 and six distinct sets that follow the authored factions. That proposal repairs the reader; nothing yet reads the result as bodies.
- `world_q.incompatible_span` (`:5350`) printed `True` for all three strands in this lane's run (seed 0, two seasons; audit §12, P-1), which is the base rate `20_NARRATIVE_A` describes.
- Convictions move in play (6, 8 and 8 persons in four seasons at seeds 0 to 2, `audits/20_NARRATIVE_CHURN.md` F-NARR-08), silently and for the same persons at every seed (`audits/23_STORY_ENABLEMENT.md` S-64), so a regime's membership does change and no reading shows it.

## The resolution, decided

**A regime is a creed set with seats.** A person's creed set is the affiliations he stands for (`world_q._held` under `20_NARRATIVE_A`'s reading). Persons with the same creed set are one body. The body is a **regime** while at least one of its members holds a seat, and a **persuasion** when none does (R13: a regime is institutions; a belief with no office is not yet one). Persons who stand for nothing are in none. Ladder step 3 (`strife-00` §5, A4: "the regime a person stands in is his own held affiliations and the institutions he holds seats in") for the definition; step 4 (`flows_in`: a recomputed reading with no consumer in the loop) for its form.

| a regime's life | what it is, as a change in the reading | the drawn events that cause it (owner) |
|---|---|---|
| **forms** | a creed set gains its first seated member | a seat conferred on, or won by, one who stands for it (`confer`, `succeed`: `14_VERBS_BINDING_C`); a seated person comes to stand for it (below) |
| **grows** | more persons, more seats, a higher reach (the highest `influence_rung` among its seats, CR-104) | a person talked round (`argue`, drawn: S-59); a cause heard and taken up (`commit` on `propositions_heard`); a crisis of faith that folds a broken creed into one he stands for (`conviction.moved`, drawn: A-24); credit along its own lines (L4: its tellers are believed, so its account spreads) |
| **splits** | one creed set becomes two, each with seats | some of its members gain or lose an affiliation the others do not: a crisis, a persuasion, a scar on one element of the creed (`_scar_witnesses`) |
| **merges** | two creed sets become one | conversion only: the members of one come to stand where the others stand. An institutional union of two creeds (a concordat that makes two incompatible affiliations compatible) is **not established** in the tree: `data/affiliations.py::INCOMPATIBILITY` is authored data and no act writes it. Not proposed |
| **is unseated** | its last seated member loses his seat or dies; it reads as a persuasion | a death, a strip (A-35), a lost seat (A-58) |
| **ends** | nobody stands for the set | deaths and conversions |

**Regime, faction and strife are three partitions and they cross.** A faction is whom a person is committed to (`world_q.faction_of`); a regime is what he holds true; a side is where he stands in one strand. The crossings are where the story is:

| crossing | reading (owner) | what it produces |
|---|---|---|
| a faction holding two regimes (the Crown's party: two orthodox, one Restoration among eleven, `20_NARRATIVE_D`) | per faction, the creed sets of its members (this proposal, commit 2) | a member asked what he thinks of his own side (`20_NARRATIVE_D`); the Split (A-46) |
| a regime spanning two factions | per regime, its factions | news and causes that cross a border of allegiance and are believed; an alliance has ground |
| a strand between regimes or inside one | `incompatible_span` (`:5350`), which discriminates once `20_NARRATIVE_A` lands | between: two accounts of the same deeds, each believed by its own (class G5); inside: a quarrel over what its own terms require |

**A regime and the era.** The era's RULE has a **ruling regime**: the creed set of the head seat's holder. A change of ruling regime is a change of RULE, and so an era turn: a new holder who stands elsewhere, or a sitting holder whose creed moves (`conviction.moved` on him). `[ASSUMPTION; medium; Jordan to correct; revert: drop the row; a ruler's conversion is then of the era and does not end it]`. Each regime holds its own account of the era: its members estimate the holder's `legitimacy` (`person_q.py:537`) from the deeds they hold, and which deeds they hold firmly is set by whom they credit. The engine holds no account as the true one (`strife-00` §5); `30_GO_F` names an era for a person by his own regard for the holder he believes rules.

**What is not done.** No regime is stored. No person is assigned a regime: he has a creed set and the reading groups. No term enters `decision/`. `rank` (H-181) stays dormant (`ED-IN-0352`'s FORBIDDEN list). A person does not read another's convictions: `commensurate` is computed resolver-side at the telling and reaches him only as how firmly the claim is held.

## Instructions to code

Tier: second (sonnet); no judgment node. All commits hash EQUAL.

**Commit 1.** `engine/season/queries/world_q.py`, after `incompatible_span` (`:5353`).

```python
class Regime(NamedTuple):
    creed: frozenset      # the affiliations its members stand for (`_held`'s reading)
    persons: tuple        # ids, sorted
    seats: tuple          # office ids its members hold (live `hold`), sorted
    factions: tuple       # `faction_of` over its members, sorted, None dropped

def regimes(w: World) -> tuple:
    """Every non-empty creed set among living persons, as a `Regime`, most persons first, then by sorted
    creed. A body with no seat is a persuasion (`seats == ()`). Recomputed; stores nothing; no consumer
    in the loop (T-a). Reads `_held`, so it follows `Fixtures held_reading`."""

def regime_relation(a: frozenset, b: frozenset) -> int:
    """-1 / 0 / +1 between two creed sets: `commensurate`'s rule over sets (`_strains`; a shared member
    or a recorded `false` pair). `commensurate` is rewritten to call it, so the rule has one body."""
```

`commensurate` (`:5317-5336`) keeps its signature and its two early returns and calls `regime_relation(ha, hb)`. Test, `engine/season/tests/test_strife_credit.py` (the covering file): `test_commensurate_and_regime_relation_agree_on_every_pair_of_the_built_realm` (all pairs, `assert checked >= 1000`), `test_regimes_partition_the_convinced` (every person with a non-empty creed set is in exactly one), `test_a_body_with_no_seat_reads_as_a_persuasion`.

**Commit 2.** `engine/season/harness/storybar.py`: `--regimes`, on the existing `on_season` hook (`drive`, `:288`), printing per season:
- `regime <creed> persons=<n> seats=<n> reach=<rung kind or -> factions=<…>` per body (`reach` prints `n/a (no influence_rung)` until CR-104 lands);
- `relations: strained=<n pairs> allied=<n> apart=<n>`;
- `moved: <pid> <from creed> -> <to creed> by <Event kind or 'no Event'>` for each person whose creed set differs from the last snapshot, and the derived words `formed`, `unseated`, `split`, `ended` for bodies (set comparison between two snapshots; bookkeeping);
- `credit: hearer regime x teller regime -> n told claims, mean credited confidence` over the season's `claim.deposited` Events with a teller (the "who believes whom" table);
- per faction, its members' creed sets; per strand (when `--strands` data is present), `between` or `inside`.
Test, `engine/season/tests/test_storybar.py`: `test_regimes_block_reads_a_planted_conversion_as_a_move` (a planted `conviction.moved`; with the Event removed the line reads `by no Event`), `test_regimes_block_moves_no_hash`.

**Commit 3.** One row in `30_WR_A` commit 4's `ERA_CONDITION_READERS` siblings: `era_turns` treats a `conviction.moved` whose subject is the head seat's holder and whose before and after creed sets differ as a rule turn. Lands with `16_PESSIMIST_CHAR_A` (the emitter); before it the row is `n/a`. Test in `tests/test_strife_flows.py`: `test_a_rulers_conversion_ends_the_era`.

## The gate (execution artifacts)

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 4 --arms off off --regimes
python -m pytest engine/season/tests/test_strife_credit.py engine/season/tests/test_storybar.py -q   # covering files, at the close
```

Expected, on the shipped engine (`held_reading: any`): the block prints **seven** bodies at season 0 of seed 0, one of them holding 32 persons (`20_NARRATIVE_A`'s E-N01), and the credit table has one populated sign. With `held_reading: stands`: **six** bodies, 20 persons in none, relations among convinced pairs 130 / 779 / 126, and the credit table populated in all three signs at two seeds or more of three. With `16_PESSIMIST_CHAR_A` landed, over five seeds and six seasons: a `moved` line at two seeds or more, and the set of persons who move not equal at every seed.

## The falsifier, and its control

- A person in two bodies, or a convinced person in none: the partition is wrong.
- `moved` lines identical at every seed with the crisis drawn: membership is written into the build (S-64 stands).
- Control arm `held_reading: any`: the block must reproduce the one-body reading. If it prints six bodies there, the block is not reading `_held`.
- Control arm `regime_gain 0`: the credit table's mean confidence must be equal across signs (within the seed spread); if it is not, the table is reading something other than the credit term.

## Dependencies

`20_NARRATIVE_A` (for a reading that discriminates; commit 1 lands without it and reads today's one body). `16_PESSIMIST_CHAR_A` for movement. CR-104 for `reach`. Feeds: `30_WR_C` (between or inside), `30_WR_E` (shapes E-07 to E-09), `30_GO_F`, CR-97.

## Layer 1

`04` §A.2 (`queries/` owns nothing): kept, **STRUCTURAL**. AX-2 and AX-7 (no person reads the World or another's interior): kept, **STRUCTURAL**; the reading is the observer's and the harness's. `01_AXIOMS.md:719-721` refuses `regime` in the governance sense; R17 lets the word stand in this one; the identifier `Regime` is defined at its declaration, as `CLAUDE.md` §4 asks: **CONVENTION**. ID-16: no loop added (L4 is declared by CR-98).

## NERS reading

- **N.** Without it "regimes form, merge, split and end" has no observable, and the credit term's effect is one number in a fixture. Holds top-down (the realm's bodies of belief), bottom-up (one conversion moves one person between bodies), laterally (FA's factions and WR's strands are read against it). Narrowed: it adds no mechanism; the mechanism is CR-79's and `20_NARRATIVE_A`'s.
- **R.** A king who converts changes the age; a faction that holds two regimes has a fault a player can find. Complete: a realm with no convictions prints no body and says so.
- **S.** One rule for a pair and for a set (`regime_relation`); the block rides the hook the other story readings ride.
- **E, last.** One grouping and one table against the only way to see whose word is taken. High.

## Cost class

Small build (commits 1, 2); edit (commit 3).
