# MB · the battle's side of the land ruling: which end state passes the land, and what the field does not decide

## Status: PROPOSED

Lane MB. Carries Jordan's rulings **A-57** and **A-58** (`unified/DECISIONS_ANSWERED.md:69`, `:71`,
2026-11-12; D-20 superseded, `:87`) for the mass-battle march and result design; row R-10 of
`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`.

**This file is not the owner of the title write.** That is
`proposals/U5d_FA_land_and_seats_pass_on_a_won_march.md` (the FA closure lane, same date), which was written
against the code at more depth than this lane read it and decides: aggression read from the act (the marching
seat's faction differs from the target's holder), one tail for the title (`_take_hold`, with the seats
anchored on the place, `seats_on`), a gate basis `conquest`, the kind `rung.taken`, leave as a live `covenant`
(`world_q.passage_granted`). Nothing below restates or competes with those edits. An earlier draft of this
file designed them a second time, first with a declared purpose (withdrawn by A-58) and then with its own
readers; both drafts are gone. What remains is what only the battle side can say. Reference, not mechanism
(`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Nothing of its own. It fixes which of the field's end states the FA proposal's `Won` test will see once the
MB proposals land, so that the two sets of edits meet at one line.

## The rule, as ruled

On a march in force onto land another faction holds, **only an aggressor's win** passes the land, and its
seats with it. A draw or a defender's win leaves the defender holding. Ground no party holds is outside the
rule. The aggressor's purpose is read from the act; a casus belli or other act is context for legitimacy and
regard, not a precondition. Marked ASSUMPTION in the record: a march by the holder's leave is not aggression.

## The resolution, decided (battle side)

### 1. The resolver knows none of it

`modules/mass_battle/` receives no holder, no purpose and no leave, and its result carries none. A battle for
a province and a battle on a road are the same call (ruling A-1). The season reads the band and its own
world. The falsifier is a `grep` for `hold`, `holder` or `leave` under `modules/mass_battle/`.

### 2. Which end state is the aggressor's win

Ruling A-3 reads the band off which side broke or conceded. With the MB proposals in the suite, the title
test `res.degree == WON` therefore means, and should be read by the FA edit as meaning:

| what happened in the field | band | the land |
|---|---|---|
| the defender routed and the aggressor did not | `Won` | **passes, with its seats** |
| the defender **conceded** (a retreat line reached, a `withdraw`, a surrender) and the aggressor stands | `Won` (`04_MB_manager_battle_one_resolver.md` §1: `b_out and not a_out`) | **passes**. A fighting withdrawal saves the army and gives up the ground; this is the price the first MB audit asked a concession to have (`audits/04_MB_audit.md` §7, the priced exit) |
| the defender routed and then **rallied** at the end of the field | `Won`: "a rallied side is still the field's loser (it left the field)" (`16_PESSIMIST_MB_rout_has_two_exits.md`) | **passes**. Rally saves men, not the place |
| both sides out, or neither, when the bouts run down | `Drawn` | **stays with the defender** (A-58) |
| the aggressor routed or conceded | `Lost` | stays; the defender takes nothing of the aggressor's by winning |
| several bouts (`26_MASS_BATTLE_cell_scale_and_time.md` §3) | the band of the **last** bout | read once, at the scene's end; a drawn first bout passes nothing and decides nothing |
| `besiege` met by a garrison | `Invested` | stays; a later surrender is the FA proposal's decision 7 |
| nobody opposed the march | `Unopposed` | not a won battle; the rulings do not speak; today's write stands (FA decision 8) |

- The `Drawn` band's own write stands as the first MB lane proposed it: bodies fall by each side's share,
  nobody arrives (`04_MB_headcount_grade_and_scale.md`). A-58 settles the land on a draw and says nothing of
  where the aggressor's army then stands; "nobody arrives" is that proposal's choice and is kept.
- `Won` after a **pursuit** (the amended pessimist proposal) changes nothing here: pursuit and the taking of
  prisoners happen inside the same fold, before the title is written.

### 3. Relief and pursuit across a border, by the ruling's own words

Classed from the act, with nothing declared; the test is the FA proposal's (holder other than the marcher's
faction, and no leave):

| the march | holder of the ground | leave | on `Won` |
|---|---|---|---|
| against a neighbour's land and its defenders | another | no | the land and seats pass (aggression) |
| onto one's own land, against an intruder | own | — | nothing to take (defence, or relief of one's own) |
| into an ally's land, asked, against the ally's enemy | another | yes | nothing passes (relief by leave) |
| through another's land by agreement | another | yes | nothing passes (passage) |
| after a beaten enemy onto land a third party holds, unasked | another | no | **aggression against the holder**: by the ruling's words a march in force into territory another holds "counts as a march to take land", and a win on it passes the land |
| onto ground nobody holds | none | — | outside the rule |

The fifth row is the FA proposal's decision 6 and this lane agrees it is what the ruling says. It has a
consequence worth seeing before it is built: **an uninvited rescuer who beats the invader takes the land he
rescued.** Today no such field can form: `sides_of` fields the holder's faction as the defender, and the
PHYSICAL lane's `march_defender` forms a field against a non-holder only on the marcher's own land
(`14_VERBS_PHYSICAL_B_field_and_ruin.md` B1). So the row is unreachable until allied relief exists, and when
it does the one question to put to Jordan is whether the land passes when the army beaten on it was not the
holder's. It is recorded here, not decided, and nothing is built for it.

### 4. Consent (the record's ASSUMPTION), battle side

The FA proposal reads leave as a live `covenant` between a seat of each faction
(`world_q.passage_granted`). Two things follow for the field and are proposed to that owner, not built here:

- **Leave covers entering, not fighting one's host.** A guest who marches on the holder's own force and wins
  has won a battle against the land's holder; whether the standing covenant then shields him from the ruling
  is not stated. This lane's reading is that it does not (the holder consented to his presence, not to his
  attack), and that regard's owner reads the broken leave. `[ASSUMPTION; Jordan to correct]`
- **Presence by leave should not be occupation.** `occupying_faction` reads presence however it came about
  (`engine/season/loop/effects_shared.py:157-159`, a weakness the code names). An invited ally standing on a
  friend's land holds the licence `seize` asks for. If `world_q.occupies` declined a faction for which
  `passage_granted` is true, the guest could not seize while his leave stands and could the moment it ends.
  One conjunct at the one owner.

### 5. A march need not wait for a war

A-58: a casus belli is "not a precondition". The PHYSICAL lane forms `march` only against a faction the
marcher knows he is at war with (`fields_in_reach`). That is a rule about when a person thinks of marching,
not about whether the act is lawful, and it keeps formation bounded; a played or hand-built march on a
neighbour needs only a Rung (`requires_typed` is unchanged there). What is then owed, and is FA's
(`06_FA_war_lives_in_seats_B.md`, whose reconciliation already says "a land-taking march is a war act"):
`sides_of` must field the holder as the defender when the two are not yet at war, and the fold must leave
them at war afterwards. Named, not designed.

## Exact edits (MB's only)

| file (owner) | edit |
|---|---|
| `engine/season/seam/ladder.py::field_degree` | none beyond the suite's: it returns the band. The table of section 2 is its reading, stated once in its docstring so the FA edit's `WON` test and the MB bands cannot drift |
| `engine/season/loop/effects_combat.py::_eff_march` | the order inside the `Won` fold: casualties and pursuit, then arrival, then the FA proposal's title tail. No MB write follows the title |
| `engine/season/seam/wrappers/mass_battle.py::resolve` | with several bouts, returns one band for the scene; the title tail is reached once |

## Open, named (not assumed)

1. An `Unopposed` entry onto held land: no ruling. Today's presence, then `seize`.
2. Where a drawn aggressor's army stands afterwards.
3. Section 3's fifth row, when it becomes reachable.
4. Section 4's two readings of leave.
5. Whether a walled place should pass on a won field outside its walls, or only when its `Invested` band
   ends. The pages read say places usually changed hands by terms or a storm after the field
   (`research/historical/mass_battle_maneuver_sequences_grounding.md` §11); research does not settle a
   ruling, and the ruling's words are followed.
6. To whom the seats pass, and the rest of the FA proposal's own "not decided" list, which is that file's.

## Gate (execution artifacts)

The FA proposal's five arms are the gate for the write. Added for the battle side, on the same world:

1. A defender who concedes at his retreat line with his army two-thirds whole: `Won`, the land passes.
2. A defender who routs and rallies: `Won`, the land passes, his `rallied` flag set.
3. A six-bout field drawn at the last bout: no tenure moves; a field drawn at bout 1 and won at bout 3: the
   title is written once.
4. `git grep -n "holder\|passage_granted\|hold_force" modules/mass_battle` prints nothing.

## Falsifier

A title written before the last bout; a title on `Drawn`; the module reading who holds the ground.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** From the campaign: winning a field for land now takes it, so the two lanes' edits must agree on
  what "won" is; this is that agreement. From the defender: holding to a draw keeps the land, and conceding
  loses it, which gives the retreat line a price. Cut section 2 and a rally or a concession is read one way
  by the field and another by the title.
- **R.** Three ways to lose a province (broken, withdrawn, surrendered) and one way to keep it short of
  winning (the draw).
- **S.** One band, read once; the resolver untouched.
- **E, against that.** No new mechanism: a table in a docstring and an order of writes.

## Cost class

Edit, with the FA proposal and after the `Drawn` band.
