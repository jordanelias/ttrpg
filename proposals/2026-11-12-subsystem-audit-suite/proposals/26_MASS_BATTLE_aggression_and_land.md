# MB · the battle's side of the land ruling: which end state passes the land, and what the field does not decide

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §2 rows A-65/A-66 and `U3_CONFLICT_LEDGER.md` C3-L12 (a win does not pass the land by itself: the aggressor forms `seize`, occupies without seizing, or withdraws; the uninvited rescuer chooses among the same; §2's and §3's "passes" rows and the rescuer paragraph rewritten; the field's fold writes no title), A-67/A-68/A-70 (§2's `Drawn` bullet: each army returns at once to its station), A-68/A-85 (§3: an unopposed entry onto held land is tolerated or aggression by a draw on the parties' own state modified by the realm's strife; leave is one input to it), A-70 (§4 rewritten as the plain reading, not as this lane's open reading), A-74 (§5: a march may also be thought of on a claim or grievance), C3-L7 (the intro's "gate basis `conquest`" is withdrawn: seats pass by the existing revocation and claim bases); the "Open, named" items 1–4 marked answered; test 9 (tests, lands-it, tier; `Depends on:` / `Lands in batch:`). The FA owner (`U5d_FA_land_and_seats_pass_on_a_won_march.md`, R3) is cited, not edited. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "province" → "territory" (glossary *territory*).

**Depends on:** `04_MB_headcount_grade_and_scale.md` (B17: the `Drawn` band and its re-homing); `04_MB_manager_battle_one_resolver.md` §1 (B20); `U5d_FA_land_and_seats_pass_on_a_won_march.md` (B23, the title owner); `14_VERBS_MATERIAL_D_paper.md` §6 (`seize`, the carrier of A-66's seizure, C3-L12); the faction lane's reader of a claim or grievance as an occasion to march (A-74, R3).
**Lands in batch:** B23 (`B23-land`, FA), after `14_VERBS_MATERIAL_D` §6 and before RES-V §2–§3 and UMR §2.

## Status: PROPOSED

Lane MB. Carries Jordan's rulings **A-57** and **A-58** (`unified/DECISIONS_ANSWERED.md:69`, `:71`,
2026-11-12; D-20 superseded, `:87`) for the mass-battle march and result design; row R-10 of
`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`.

**This file is not the owner of the title write.** That is
`proposals/U5d_FA_land_and_seats_pass_on_a_won_march.md` (the FA closure lane, same date), which was written
against the code at more depth than this lane read it and decides: aggression read from the act (the marching
seat's faction differs from the target's holder), one tail for the title (`_take_hold`, with the seats
anchored on the place, `seats_on`; *(W3-1, C3-L12, C3-L7:)* run by the aggressor's `seize` act after the win,
never by the field's fold, the seats passing through the existing revocation and claim bases, no `conquest`
basis), the kind `rung.taken`, leave as a live `covenant` (`world_q.passage_granted`). Nothing below restates or competes with those edits. An earlier draft of this
file designed them a second time, first with a declared purpose (withdrawn by A-58) and then with its own
readers; both drafts are gone. What remains is what only the battle side can say. Reference, not mechanism
(`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Nothing of its own. It fixes which of the field's end states the FA proposal's `Won` test will see once the
MB proposals land, so that the two sets of edits meet at one line.

## The rule, as ruled

On a march in force onto land another faction holds, **only an aggressor's win** can pass the land, and its
seats with it, and then only by his choice: he forms `seize` (title and seats pass), occupies without seizing
(his army holds the ground, the title stays), or withdraws (A-66). A draw or a defender's win leaves the
defender holding, and on a draw each army returns at once to its station (A-67, A-68, A-70). Ground no party holds is outside the
rule. The aggressor's purpose is read from the act; a casus belli or other act is context for legitimacy and
regard, not a precondition. Marked ASSUMPTION in the record: a march by the holder's leave is not aggression.

## The resolution, decided (battle side)

### 1. The resolver knows none of it

`modules/mass_battle/` receives no holder, no purpose and no leave, and its result carries none. A battle for
a territory and a battle on a road are the same call (ruling A-1). The season reads the band and its own
world. The falsifier is a `grep` for `hold`, `holder` or `leave` under `modules/mass_battle/`.

### 2. Which end state is the aggressor's win

Ruling A-3 reads the band off which side broke or conceded. With the MB proposals in the suite, the title
test `res.degree == WON` therefore means, and should be read by the FA edit as meaning:

| what happened in the field | band | the land |
|---|---|---|
| the defender routed and the aggressor did not | `Won` | **may pass**: the aggressor forms `seize` after the `Won` (title and seats pass), or occupies without seizing, or withdraws (A-66; C3-L12) |
| the defender **conceded** (a retreat line reached, a `withdraw`, a surrender) and the aggressor stands | `Won` (`04_MB_manager_battle_one_resolver.md` §1: `b_out and not a_out`) | **may pass**, as above. A fighting withdrawal saves the army and gives up the ground; this is the price the first MB audit asked a concession to have (`audits/04_MB_audit.md` §7, the priced exit) |
| the defender routed and then **rallied** at the end of the field | `Won`: "a rallied side is still the field's loser (it left the field)" (`16_PESSIMIST_MB_rout_has_two_exits.md`) | **may pass**, as above. Rally saves men, not the place |
| both sides out, or neither, when the bouts run down | `Drawn` | **stays with the defender** (A-58) |
| the aggressor routed or conceded | `Lost` | stays; the defender takes nothing of the aggressor's by winning |
| several bouts (`26_MASS_BATTLE_cell_scale_and_time.md` §3) | the band of the **last** bout | read once, at the scene's end; a drawn first bout passes nothing and decides nothing |
| `besiege` met by a garrison | `Invested` | stays; a later surrender is the FA proposal's decision 7 |
| nobody opposed the march | `Unopposed` | not a won battle; the rulings do not speak; today's write stands (FA decision 8) |

- The `Drawn` band's write (`04_MB_headcount_grade_and_scale.md`): bodies fall by each side's share and
  *(W3-1, A-67, A-68, A-70)* each army returns at once to its station, the aggressor's to where the march
  began, the defender's to its own base, carrying its losses and fatigue (A-69).
- `Won` after a **pursuit** (the amended pessimist proposal) changes nothing here: pursuit and the taking of
  prisoners happen inside the same fold; the title is written later, if at all, by the aggressor's `seize`.

### 3. Relief and pursuit across a border, by the ruling's own words

Classed from the act, with nothing declared; the test is the FA proposal's (holder other than the marcher's
faction). *(W3-1, A-68, A-85, A-76:)* whether an entry onto another's held land counts as aggression is not a
fixed class: an unopposed entry is tolerated but disliked when the realm's working bench stands in for a
functional parliament (A-76) and the parties are at peace, and is aggression when tension or strife is enough,
a draw on the two parties' own state (regard, grievances, a live war, a working bench) modified by the realm's
strife level (A-85). Leave (`covenant`, `passage_granted`) is one input to that draw. The owner of the draw is
the FA lane (`U5d_FA_land_and_seats_pass_on_a_won_march.md`); the table below gives the battle side only:

| the march | holder of the ground | leave | on `Won` |
|---|---|---|---|
| against a neighbour's land and its defenders | another | no | the aggressor may form `seize` (A-66) |
| onto one's own land, against an intruder | own | — | nothing to take (defence, or relief of one's own) |
| into an ally's land, asked, against the ally's enemy | another | yes | nothing passes (relief by leave) |
| through another's land by agreement | another | yes | nothing passes (passage) |
| after a beaten enemy onto land a third party holds, unasked | another | no | the uninvited rescuer **may** occupy, by his own choice, with every repercussion following from choosing to or not (A-65); he chooses among `seize`, occupy, withdraw as an aggressor does (A-66) |
| onto ground nobody holds | none | — | outside the rule |

*(W3-1, A-65.)* The fifth row is answered by Jordan: the rescuer's occupation is his choice, not an automatic
transfer, and its repercussions are drawn through the existing acts, regard and war rules. Today no such
field can form: `sides_of` fields the holder's faction as the defender, and the PHYSICAL lane's
`march_defender` forms a field against a non-holder only on the marcher's own land
(`14_VERBS_PHYSICAL_B_field_and_ruin.md` B1); the row is unreachable until allied relief exists, and nothing
is built for it here.

### 4. Consent, battle side (A-70's plain reading)

The FA proposal reads leave as a live `covenant` between a seat of each faction
(`world_q.passage_granted`). A-70 dropped the two "leave" framings as questions and the plain reading is taken
(`[ASSUMPTION, reversible: A-70's own marking]`); two things follow for the field and are proposed to that
owner, not built here:

- **An attack is an attack whoever invited the attacker.** A guest who marches on the holder's own force is
  an aggressor by the act; leave covered his entering, not his attack, and regard's owner reads the broken
  leave.
- **Standing on land by its holder's leave is not occupying it.** `occupying_faction` reads presence however it
  came about (`engine/season/loop/effects_shared.py:157-159`, a weakness the code names); `world_q.occupies`
  declines a faction for which `passage_granted` is true, so a guest cannot seize while his leave stands. One
  conjunct at the one owner.

### 5. A march need not wait for a war

A-58: a casus belli is "not a precondition". The PHYSICAL lane forms `march` only against a faction the
marcher knows he is at war with (`fields_in_reach`). That is a rule about when a person thinks of marching,
not about whether the act is lawful, and it keeps formation bounded. *(W3-1, A-74:)* a march may also be
thought of on a claim or grievance against the holder, once the faction lane names the acts that count and
gives them a reader (a dependency on R3's faction proposals); a known enemy stays one occasion among two; a played or hand-built march on a
neighbour needs only a Rung (`requires_typed` is unchanged there). What is then owed, and is FA's
(`06_FA_war_lives_in_seats_B.md`, whose reconciliation already says "a land-taking march is a war act"):
`sides_of` must field the holder as the defender when the two are not yet at war, and the fold must leave
them at war afterwards. Named, not designed.

## Exact edits (MB's only)

| file (owner) | edit |
|---|---|
| `engine/season/seam/ladder.py::field_degree` | none beyond the suite's: it returns the band. The table of section 2 is its reading, stated once in its docstring so the FA edit's `WON` test and the MB bands cannot drift |
| `engine/season/loop/effects_combat.py::_eff_march` | the order inside the `Won` fold: casualties and pursuit, then arrival (the army on the ground, occupying); no title write (C3-L12): the aggressor's scene continues with `seize`, occupy or withdraw (A-9, A-66) |
| `engine/season/seam/wrappers/mass_battle.py::resolve` | with several bouts, returns one band for the scene (the bout loop is inside the module, `26_MASS_BATTLE_cell_scale_and_time.md` §3) |

## Open, named (not assumed)

1. *(Answered, A-68, A-85: tolerated-or-aggression by a draw; FA's owner.)*
2. *(Answered, A-67, A-68: immediately back at its station.)*
3. *(Answered, A-65: the rescuer's choice.)*
4. *(Answered, A-70: dropped as questions; the plain reading is §4.)*
5. Whether a walled place should pass on a won field outside its walls, or only when its `Invested` band
   ends. The pages read say places usually changed hands by terms or a storm after the field
   (`research/historical/mass_battle_maneuver_sequences_grounding.md` §11); research does not settle a
   ruling, and the ruling's words are followed.
6. To whom the seats pass, and the rest of the FA proposal's own "not decided" list, which is that file's.

## Gate (execution artifacts)

The FA proposal's five arms are the gate for the write. Added for the battle side, on the same world:

1. A defender who concedes at his retreat line with his army two-thirds whole: `Won`; no tenure moves in the
   field's fold; the aggressor's `seize` then passes the land.
2. A defender who routs and rallies: `Won`, his `rallied` flag set; the same as row 1.
3. A six-bout field drawn at the last bout: no tenure moves and both armies are at their stations; a field
   drawn at bout 1 and won at bout 3: one band, and at most one `seize` after it.
4. `git grep -n "holder\|passage_granted\|hold_force" modules/mass_battle` prints nothing.

**Tests (W3-1).** `engine/season/tests/test_march.py::test_won_writes_no_title_in_the_fold`,
`::test_seize_after_won_passes_land_and_anchored_seats`, `::test_drawn_last_bout_moves_no_tenure`; gate 4's
grep in the commit body. **Hash movers:** none of its own (the FA proposal's). **Lands:** an IN-lane
implementation session under `/methodology-execute` with MB and FA review; edit class, `sonnet`.

## Falsifier

A title written before the last bout; a title on `Drawn`; a title written in the field's own fold rather
than by `seize`; the module reading who holds the ground.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** From the campaign: winning a field for land now lets the winner take it, so the two lanes' edits must agree on
  what "won" is; this is that agreement. From the defender: holding to a draw keeps the land, and conceding
  loses it, which gives the retreat line a price. Cut section 2 and a rally or a concession is read one way
  by the field and another by the title.
- **R.** Three ways to lose a territory (broken, withdrawn, surrendered) and one way to keep it short of
  winning (the draw).
- **S.** One band, read once; the resolver untouched.
- **E, against that.** No new mechanism: a table in a docstring and an order of writes.

## Cost class

Edit, with the FA proposal and after the `Drawn` band.
