# FA-B1 — a war lives in the seats that wage it: whose word continues it, whose word ends it, and what a seat is told when its army stands on another's land

Reconciled: 2026-11-12, U5d closure — folded Jordan's answers. **A-20** rules option (B), the seats that wage it: the sentence "lands only on that ruling. Until then the code is unchanged" is discharged; edits 1–3 land as written and edit 4 (the Layer 1 text for `04:460` and D-48) is APPLIED (2026-11-12, A-97, node `L1-A20`). **A-57, A-58 and A-65 to A-70** (the land rulings) keep edit 6 as written and give it its meaning: a field writes presence, never title; an aggressor who wins on a march into land another holds stands there and chooses to seize (the title passes, and the seats that go with the land pass with it), to occupy without seizing (the holder's claim stands), or to withdraw; a rescuer on a third party's land chooses among the same three; an unopposed entry is read by a graded draw as a tolerated trespass (which occupies nothing and which the holder resents) or as aggression (A-68); on a draw both armies are back at their stations at once and the defender holds (A-67, A-68, A-70). Edit 6's widened occasion (the rungs his faction `occupies`, whatever their holder) is where the winner is offered the taking; "the taking is still `seize`'s … Nothing is written by the field" is the ruled form. Added by the rulings and carried in `U5d_FA_land_and_seats_pass_on_a_won_march.md`: `seize` carries the seats anchored on the place, and a faction standing there by the holder's leave does not occupy it. Edit 7 (a) stands (`at_war` enters no `requires`); a march into another's held land is a war act, so `fields_between` is the reader of it. R-22's "keep β" stands for the field's write.

Reconciled: 2026-11-12, wave 3 (W3-3) — the body follows the head (R3 §2): "The resolution"'s last paragraph and edit 4 now read "ruled A-20; Layer 1 text owed, not applied" (`OWED_TO_UNIFICATION.md` §A row "war lives in the seats"); no suite batch edits `04`. Edit 6 is restricted per A-68/A-85 (R3 §2): the occasion is an arrival the entry draw reads as aggression (`U5d_FA_land_and_seats_pass_on_a_won_march.md` D6) or a field the aggressor won, and the taking is the aggressor's chosen `seize` act (C3-L12). Batch split per U3 C3-Y1 (edits 1–3 in B21; edit 6 in B23); tier (R3 7b-0).

## Status: PROPOSED

Reconciled: 2026-11-12, A-97 (`unified/work/L1_APPLIED.md` §`L1-A20`, `unified/work/L1_PROPAGATION.md`): edit 4 is APPLIED by Jordan's amendment and dropped from the plan: `04:460` (§B.10–§B.12) now reads "over live `commit`s to a WAR Proposition by a holder of a seat of either party that may muster (A-20)", PART D row 48 (`04:1078`) says the same of the `commit` edges and of who writes peace, and F.32 (`04:1233`) is marked ANSWERED. The "owed, drafted, not applied" wording of the heads, "The resolution"'s last paragraph and edit 4 is rewritten to the applied state. `10_FACTIONS_AND_DEPLOYMENT.md:73` is amended to match (L1_APPLIED).

Lands in batch: edits 1–3 in B21 (FA governance; before `06_FA_levy_through_the_seat_B.md`, C3-D5); edit 6 in B23 (land), first in that batch (C3-Y1). Edit 4 is applied and lands in no batch (Layer 1, `04:460`); edits 5 and 7 are plan clauses and follow-ons.
Depends on: edits 1–3 on nothing proposed; edit 6 on `U5d_FA_land_and_seats_pass_on_a_won_march.md` D6 (the entry draw, B23) and `14_VERBS_MATERIAL_D_paper.md` §6 (`seize`, landed in B23 per C3-L12).

Source: `audits/06_FA_audit_addendum_B.md` F-FA-13, F-FA-14, §B4.2, §B6.1 R-22, R-23, R-32, §B6.2 item 1;
`architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md` §2, §3; `04_CODE_ARCHITECTURE.md` D-48, F.32, F.33;
plan positions CP-T09-02, CP-T09-03, CP-T09-04. Supersedes nothing; it amends two planned positions by
one clause each and is to land with or after CP-T09-02.

## What it changes in `engine/season/` at runtime

1. `at_war(a, b)` counts a live `commit` to a WAR Proposition only when the committer holds a seat of
   `a` or of `b` whose grant carries the muster act. Any other person's commit no longer keeps a war
   alive.
2. Nothing else on the game path in the first commit. In every world the tree builds today no WAR
   Proposition exists (`build_realm(0)`: 70 Propositions, moods HOLDS and OUGHT only, addendum E-B1), so
   the realm, spine and corpus hashes are EQUAL. One test is re-recorded.
3. Edits 3 to 5 are clauses on positions the plan already schedules; each is named with its owner and
   none is built by this file's first commit.

## The problem (evidence)

- `queries/world_q.py:3594-3598`: `at_war` returns true if **any** live `commit` to a WAR Proposition
  naming the pair exists.
- Today a war is one person's edge. A dead person's edges are deleted with him (first audit §4), so a
  war ends by its declarer's death. Layer 1 records the opposite fear as an open gap, F.32
  (`04:1232`): "the declarer dies and the war can be ended by nobody … the repair is an edge subjected
  to *the seat's holder*, and the design has no Tenure that changes hands."
- CP-T09-02 (d) adds rallying: any member of either faction may `commit` to the war. CP-T09-03 (c)
  ends it "when no committer is left" (plan home file `:183-184`, `:229-231`). Together: peace needs
  every committer on both sides to release or die. One person anywhere keeps two factions at war, and
  CP-T09-02 (c) then keeps every enemy town in every officer's target set.
- Layer 1's own picture of war has two readings side by side (`10` §2): de jure, "the uttered war,
  persisting until somebody makes peace"; de facto, "the commitment share, which may be near zero";
  and the gap between them, "we are still at war, and nobody will muster". The code has one reading
  for both.
- A lost or won field writes bodies, stance rows and presence, and no holding or seat (`_eff_march`,
  `loop/effects_combat.py:532-536`: "a won field writes PRESENCE, never title"), though Layer 1's
  roster contract names the stakes as "`holdings` and `seats`, for what a defeat costs" (`10` §3).

## The resolution, decided

**De jure war is an act of office.** A war is live while someone who can order a muster for one of its
two parties is committed to it. Everyone else's commitment is the de facto share: how many will come.
This is ladder step 5, taken because it is the only reading that closes F.32 without the Tenure Layer 1
says it lacks: the commitment stays the person's own edge, and what changes hands is the seat, which
already changes hands. A successor decides the war by committing or not; a deposed or dead declarer's
commitment stops counting the instant he is unseated; rank-and-file zeal cannot prolong a war its
officers have ended. It also matches every referent the archived design gives for who makes war (a
Senator action by a faction's leadership, a War Authorisation by the seated; `faction_layer_v30` §3.2,
§5.4) and the plan's own choice that `declare` is `remit:dispatch`.

It narrows a ratified sentence (`04:460`: "over live `commit`s to a WAR Proposition"). Ruled A-20 (option
B, the seats that wage it); edits 1–3 land as written. The Layer 1 text that records the narrowing (edit 4)
is APPLIED (2026-11-12, A-97, node `L1-A20`): `04:460` carries the narrowed sentence.

## Exact edits, by owner

**1. `engine/season/state/gate.py`** (owner of what a seat licenses). One predicate beside
`may_muster`:

```python
def may_wage(w, person: str, faction: str) -> bool:
    """Does `person` hold a seat of `faction` whose grant carries MUSTER_ACT? `faction` is the
    Proposition id; `seat_faction` is the one owner of seat -> faction id."""
```

It is `any(_seat_grants(w, person, h.object, MUSTER_ACT) and seat_faction(w, h.object) == faction
for h in person's live holds on offices)`. It adds no rule: both conjuncts are `may_muster`'s first two
and its faction read.

**2. `engine/season/queries/world_q.py::at_war`** (owner of "is this war live"). The last line's test
becomes: a live `commit` to the Proposition whose subject `may_wage` for `p.subject` or for `p.value`.
The docstring's F.32 paragraph is replaced by the rule above. `enemies_heard` and the `strife`
instrument read `at_war` and need no edit.

**3. `engine/season/tests/test_faction_q.py::test_at_war_through_the_real_fold_utter_then_commit_then_release`.**
Its declarer is `world_q.members(w, "fac_valorsmark")[0]`; he must be chosen as a holder of a
Valorsmark seat whose grant carries `dispatch`, and the test gains its control (below).

**4. Layer 1 text (A-20): APPLIED 2026-11-12 (A-97, node `L1-A20`); no edit of any batch.** `04:460`'s
one-line contract and PART D row 48 (`04:1078`, the D-48 row) now carry "by a holder of a seat of either party
that may muster"; F.32 (`04:1233`) is answered by a pointer to this rule. (A spec that binds code is changed
with the ruling, never to match code that departed from it; `CLAUDE.md` §0.05.)

**5. CP-T09-02 (d), one clause (plan edit, owner the plan):** rallying stamps the war for every member
as written; the entry states that a rallying commit is de facto and does not keep the war alive.

**6. CP-T09-04 (d), one clause (plan edit; closes R-22).** The planned standing term offers a holder of
a seat granting `issue` the `uncontrolled` rungs in his purview where his faction is mustered. Widen
the rungs to those his faction `occupies` (`world_q.occupies`, the one owner of occupation) whatever
their holder, **restricted to an occupation that is aggression**: either the field on that ground was won
by his faction as aggressor (A-57, A-58), or the unopposed entry was read as aggression by the entry draw
(`U5d_FA_land_and_seats_pass_on_a_won_march.md` D6; A-68, A-85). An unopposed entry read as a tolerated
trespass (a calm realm, a working bench, the parties at peace) occupies nothing in this sense and offers
no taking (A-68: tolerated, disliked); presence by the holder's leave is not occupation (A-70). Then the
taking is the aggressor's chosen `seize` act (C3-L12: seize, occupy without seizing, or withdraw, A-66),
licensed as CP-T09-04 (b) states, with the seats anchored on the place passing in the same act (C3-L7).
Nothing is written by the field.

**7. Follow-ons, named and not built here.**
(a) *A field's place in a war (R-32, F.33).* `at_war` does not enter any verb's `requires`. A Query
`faction_q.fields_between(w, a, b)` over the log returns the `march` band Events fought between the
two factions; whether an Event retains which faction defended is [UNVERIFIED] (the result dict's
`parties` carries members, not factions), so the shape is stated and the build waits on that read.
(b) *The commander who lost.* The first lane's `suspicion_of` fold counts defied writs. A lost field
ordered through a subordinate's seat is the other reason a superior replaces him; it is one more
claim kind in that fold and is added there, after an answered writ and a fought field are both
observed in computed play.

## Gate (execution artifact)

A hand-built chain on `build_realm(0)` through the real fold, run as the test of edit 3 and printed by
a five-line probe:

1. a Valorsmark holder of a `dispatch` seat utters WAR(Valorsmark, Guilds) and commits: `at_war` True
   both ways (today's assertion, unchanged);
2. he `release`s that seat's `hold`, his `commit` still live: `at_war` False;
3. an unseated Valorsmark member commits to the same Proposition: still False;
4. a second holder of a `dispatch` seat, of either faction, commits: True; he releases his commit: False.

Realm reading after CP-T09-02 lands: at seeds 0 to 2, the count of WAR Propositions that are live at
the end of the run against those whose every *seated* committer released or lost his seat; a war still
live with no seated committer is the failure this proposal exists to remove and must read 0.

## Falsifier

- Control: with the `may_wage` conjunct removed, steps 2 and 3 read True. If they read False without
  the edit, the test is not observing the rule.
- Mutation: ask `seat_hold` without the grant (drop `MUSTER_ACT`): a seated treasurer's commit then
  keeps the war alive and step 3's variant with a treasurer reddens.
- Hash: realm, spine and corpus one-season hashes EQUAL before and after edits 1 to 3.

## What it does not do

It adds no verb, no stored flag and no Tenure. It does not gate `march` on war (the plan's "a march
needs no war" stands). It does not build a de facto share reader; when one is wanted it is the count of
live commits, already in the world.

## NERS reading

- **N.** From above, a ruler's war passes to his heir as a decision. From below, a soldier's zeal is
  not a state of war. Laterally, the same seats that send armies are the ones whose word starts and
  ends the sending. Diagonally, a vassal sworn to a seat at war is not thereby at war: his own seat
  decides. Remove it and the planned war either dies with one man or never ends.
- **R.** Strategy: killing or unseating the war party is a route to peace; a succession is a diplomatic
  event. With no player, wars end by depositions and deaths as well as by treaties. Complete at the
  extremes: no seated committer, no war; a faction with no muster seat cannot be at war by its own
  word.
- **S.** One methodology with `may_muster`, `may_seize` and `may_warrant`: seat, grant, faction.
- **E, last.** One predicate and one conjunct. Against what N and R find, small.

## Cost class

Edit (ruled, A-20). Declared mover of one test. Depends on CP-T09-02 for any computed reading.
Tier: `sonnet` (R3 7b-0).
