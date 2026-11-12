# FA — pessimist audit: NERS, premise and emergent narrative, of factions, governance, offices, war and diplomacy

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 2eba83c (working tree)

Scope: `engine/season/loop/effects_governance.py`, `queries/faction_q.py`, `offices.yaml`,
`governance_spine.yaml`, `arrangements.yaml`, `data/affiliations.py`, the governance verbs, the
institutions fixed points (royalty by noble conquest; nobility by deed) and five premise sentences of rule.
The FA lane's audit and addendum (`audits/06_FA_audit.md`, `06_FA_audit_addendum_B.md`), the binding-verbs
lane (`14_VERBS_BINDING.md`), the four institutions lanes (`15_INSTITUTIONS_*`) and the game-level pessimist
(`16_PESSIMIST_GAME.md`) are cited, not redone. Everything measured here is new work unless a lane is named.
All runs `PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_FA/`.
`[UNVERIFIED]` marks what was not checked. Nothing here is the reason a behaviour is correct (`CLAUDE.md`
§0.05).

**§0 (verdict) is written last and placed first; if this file ends before §0 is filled, the lane was
interrupted and the sections below are the partial record.**

## 0. Verdict

*(placeholder: replaced when the runs of §1 to §3 are in; see the note above)*

## 1. NERS — the cuts, executed and read

Method: `skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06. A cut is free when nothing but the cut
thing's own bookkeeping differs. The FA lane's NERS readings (`06_FA_audit.md` §5.4) are cited; four of
its five "survives" are attacked here. **No draw to diagnose:** none of the nine governance effects takes a
draw (`effects_governance.py`: the `res` argument is unused in every one), so `resolution-diagnostic` has
no subject in FA's own code; the one draw met in the probes is `arrest` (2 of 2 `arrest.resisted`), which
is SC's and PC's.

### 1.1 The executed cuts (`pf3_cut.py`, seed 0, two seasons, four arms on one built world)

SHIPPED; **DRAW2** (the same world, the dice re-seeded: the noise floor, without which no arm difference is
a measurement, §0.1 pt 4); **NO_SEATS** (all 34 live seat-holds closed at build: nobody holds an office);
**NO_FACTION** (every live `commit` to a faction Proposition closed at build: nobody is a member of
anything).

| | SHIPPED | DRAW2 (noise floor) | NO_SEATS | NO_FACTION |
|---|---|---|---|---|
| acts attempted | 1,703 | 1,750 | 1,666 | 1,677 |
| executed | 919 | 1,023 | 962 | 829 |
| resolved by a draw | 121 | 156 | 182 | 122 |
| executed answers to another person's act | 156 | 167 | 135 | 160 |
| … whose antecedent is an FA act | 54 | 30 | 13 | 89 |
| persons at end | 83 | 83 | 83 | 83 |
| stores, realm total (grain / ore / salt / timber) | 2775 / 3663 / 2109 / 703 | the same | **the same** | **the same** |
| seat-gated verbs executed (`issue`, `dispatch`, `convene`, `march`, `open_case`, `establish`) | 19, 12, 12, 13, 7, 1 | 15, 7, 6, 4, 7, 0 | 0 (by construction) | 18, 11, 6, 17, 6, 1 |
| `oblige` executed | 26 | **0** | 0 | 55 |
| seat changes (`tenure.opened` / `succession.claimed`) | 0 / 0 | 0 / 0 | n/a | **1** / 0 (a founded lordship conferred) |
| executed-verb L1 distance from SHIPPED | 0 | **240** | 263 | **224** |
| state components that differ from SHIPPED (of 19 read) | 0 | 10 (bodies 5, stores on 6 rungs, stance 1, pursuits 2, residence 8, an office, dates, records) | 10 (the 34 holds by construction; conviction 6, pursuits 2, residence 7, an office, docket 14 → 5, dates 12 → 0); **bodies, stores per rung, stance, sites equal** | 11 (one more seat held, bodies 1, stores on 4 rungs, pursuits 1, residence 8, Propositions 199 → 169, docket 14 → 10); stance, conviction, sites equal |

`pf3_cmp.py` compares the arms' pickled projections; outputs `pf3_a_s0.txt`, `pf3_b_s0.txt`, `pf3_cmp_s0.txt`.

**Reading of NO_FACTION.** With nobody a member of any faction for two seasons, the realm differs from
the shipped realm by **less than the shipped realm differs from itself under other dice** (executed-verb
distance 224 against a noise floor of 240; fewer persons' bodies, stance and stores moved than in the
noise arm). Seats still issue, order, convene and march (17 marches against 13 and 4: a march needs no
faction); the one seat change in any arm happened here. What dies with membership is two verbs' subject
matter: `survey` (12 and 9 executed → 0: there is no faction to survey) and `forge` (31 and 30 → 0),
plus the creed Propositions' committers (Propositions 199 → 169). **"Faction" is a false N-line in
computed play: the cut is free but for one document kind and its forgeries.** Nothing a person decides in
two seasons is conditioned on which faction he, or anyone, belongs to, beyond what the dice alone move.

**Reading of NO_SEATS.** With every office in the realm empty for two seasons, the same 83 persons are
alive, the realm's stores are equal to the unit, and the totals of activity sit inside the spread between
two dice seeds of the shipped realm for acts executed (962 against 919 and 1,023) and about a fifth below
it for cross-person answers (135 against 156 and 167); its distance from the shipped realm in what
persons do (263) is the distance between two dice seeds (240), and its bodies and per-rung stores are
closer to the shipped realm's than the other dice seed's are. What the seats add is their own emissions: about a hundred acts in two seasons (`issue`,
`dispatch`, `convene`, `march`, `open_case`, `oblige`) that the same persons otherwise spend on
`create_record`, `utter`, `research` and `surveil`, and the 17 to 41 further answers other persons give to
those emissions (54 and 30 FA-antecedent answers against 13). **More of the realm is decided by a draw
without offices than with them** (182 against 121 and 156), because the acts offices open are undrawn and
the acts they displace (`research`, `surveil`) draw. The cut is therefore free in everything but paper:
no person, store, site or holding differs because the realm has a King. This is the game lane's X1
(agency cut) repeated one level down, and the control shows the instrument can see a difference when there
is one: `oblige` reads 26 against 0 between two dice seeds of one world.

**The noise floor is itself a finding.** Re-seeding the dice alone moves `oblige` 26 → 0, `march` 13 → 4,
`dispatch` 12 → 7 and `convene` 12 → 6. The FA lane's per-verb counts (its E-3, E-5) are single draws
from that spread; "13 marches by four clerks" is one seed's sentence.

### 1.2 Cuts by reading and probe: the false N-lines, and what survives only untested

| object | the FA lane's reading | attack | result |
|---|---|---|---|
| `Faction.head`, `rosters.yaml: factions.head_seat` (CR-86) | F-FA-16 proposes two more `head_seat` rows | grep the non-test readers of `.head`, `faction_q.head(`, `HEAD_SEAT`: `faction_q` itself, the `survey` Record's content, one instrument. `opinion_of`, the one decision-side reader of a faction's head, reads the creed Proposition's subject instead (`world_q.py:3055-3056`) | **false N-line: the cut is free.** Nothing that decides reads it. Adding rows to it (R-25) feeds a field with no reader; the repair is to make `opinion_of` read `faction_q.head` (§3, F-PES-FA-08) |
| the five-field `Faction` view | steelman 2, "holds" | non-test callers of `faction_q.resolve`: `effects_information.py:829` (`survey`) and nothing else | **narrowed**: the view is necessary for one verb's document. The seam that Layer 1 says receives it (`mass_battle` wrapper, "sides") reads `members` and `leaders` through `world_q`, not the view |
| `at_war`, the `WAR` mood | F-FA-04, C-1 | readers: `enemies_heard` and one instrument; true for 0 of 45 pairs in every computed run | free in computed play; under a hand-built declaration it changes `enemies_heard` for 1 person at the tick (P3.2) |
| `revoke`, two revocation bases, `REVOCATION_DISPOSAL`, the ban | "N: it is the only cost a fall carries. Survives" | enumerate its reachable domain (`pf1`): 6 seats, one stripping seat, which is unfillable; `pardon` refused through 33 of 33 seats; a computed `revoke` is refused at its first clause by construction (FA §4) | **survives only untested.** As built the family's whole domain is six seats for one man's lifetime; after his death the cut is free. Proposal PES-FA-A |
| `off_duke_valorsmark` | CP-T09-06's card | cut it (the King dies): no seat can strip any seat | load-bearing by accident: the realm's dismissal power is a second title nobody designed to carry it |
| `off_widow_regent`'s remit | R-16: empty it while the King lives | cut it (R-16), then kill King and heir: no seat can fill `off_heir`; nobody is ever King | load-bearing by accident: it is the only route by which the throne survives the heir. R-16 needs a fallback (§3, F-PES-FA-11) |
| `successions`, `succeed`, the claim basis | steelman 5 | propose the cut: the throne becomes `appointed`; no seat is above it, so nothing fills it | **true N-line.** A top seat needs a self-claim. It fails R at the extremes instead (§1.3) |
| `seat_hold` / `Act.via` (authority through the seat) | steelman 1, "holds" | five standing attacks by execution (P1.1) | **holds**; the attack tried is in §2.2 |
| `may_fill` | not attacked | enumerate fillers per seat | survives only untested: the Crown fills all 26 fillable seats |
| `commit` as membership | "ruled; implemented" | six joins and one leaving by execution (P4.3) | survives only untested: unilateral, free, and it moves holdings between factions |
| `oblige` (the verb an NPC executes most often among FA's) | steelman 4 | 26 executed at one dice seed, 0 at another; 75 in one season at seed 3 | what it buys in computed play is the obligee information channel; the oath clause in `purview_reaches` needs a swearer who holds a seat, not checked in these runs `[UNVERIFIED]` |

### 1.3 R at the extremes (completeness)

| extreme | what ran | result |
|---|---|---|
| a faction of zero members | every Hafenmark member leaves | view `0, 0, 0`, `head` still the Duchess: a head of nothing, and not a member |
| a faction that does not exist | `resolve("fac_does_not_exist")` | an empty view, no refusal; `at_war` between it and a person: true |
| a new faction | a clerk utters a creed, two persons commit | resolves as a view (2 members, 2 seats); not in the roster, so no head, no `leaders`, no `opinion_of` (which raises for an unrostered Proposition). It can be at war. Emergent factions are half-possible: countable, never regarded |
| a hundred factions | `resolve` over ten rostered factions: 5.0 ms a sweep; `at_war` over 45 pairs: 0.1 ms (698 tenures, 70 Propositions). `at_war` scans every Proposition for every pair | no cost problem at realm size; the scan is O(Propositions × tenures) per call and was not run at 100 `[UNVERIFIED]` |
| one seat-holder dies | P2.7 | 7 of 34 seats then empty for ever |
| the royal line fails | P2.7 | no King, for ever; Valorsmark headless |
| a cohort in a seat | P2.7 | a village is King |
| a person in two factions, or in the enemy's | P4.3 | admitted; the views double-count his holdings |
| a seat-holder in custody | P5 | governs unimpaired |
| cast cap 0, 1, 2, 5 | the game lane's X5 (cited): the loop runs; at cap 0 to 2 no office exists | FA is absent below a cast of five |

### 1.4 S: two ladders for one quantity (each is a defect even where each ladder is correct)

1. **Authority over a seat.** Filling asks purview at any depth (26 seats); stripping asks the rung
   directly above (6 seats). Appoint and dismiss are not opposites.
2. **Who is under a seat.** `issue` asks the person's residence; `confer` and `revoke` ask the seat's rung;
   `dispatch` asks nothing (`_req_dispatch`: "the named person exists"); a levy of stores asks the seat, a
   levy of men asks a Record (F-FA-15, cited). Proposal PES-FA-C.
3. **Who heads a faction.** `faction_q.head` (the head seat's holder) and `opinion_of` (the creed's
   subject, fixed at build).
4. **Who may undo a dismissal.** Dismissal is `remit:revoke`; its ban is lifted by `remit:determine` at the
   same seat; no seat that can strip holds both.
5. **Pauses correctly.** Nothing in FA pauses anything: a vacancy, a war and a detention suspend no act of
   the seat or the person concerned (a prisoner issues writs; a vacant throne's ladder goes on appointing
   through the Queen's seat).

### 1.5 E, last, as a ratio against what N and R found

The seat-authority model is legible (six remit keys, one `via`) and that judgement of the FA lane stands.
What N and R found changes the ratio for three objects. The dismissal family carries two bases, a disposal
mapping with import-time totality checks, a restraint kind and a pardon verb, to govern six seats until
one man dies: the overhead is large against what it delivers. The `Faction` view carries a `head`
resolution with a graded-commit branch nothing writes and a seat branch nothing reads. `at_war` carries a
ratified Query, a mood and a Layer-1 page for a state no computed act enters and no rule consults. None of
these should be amputated (E is not an independent axis); each needs its reader or its occasion built,
or it is overhead.

## 2. Premise audit

Method: `skills/premise-check/SKILL.md`, SLICE scope (the orchestrator named the sentences). The ordinary
account **O** below was written before any FA code file, registry or note was opened by this lane.
**Declared contamination:** the FA lane's audit §0 to §6 and addendum §B0 to §B2 had been read, so O is not
blind to the lanes' findings; it is blind to the code. O is written from the words and from genre
convention, and where a cell says what a player would expect, the lanes' findings were not used to lower the
expectation.

### 2.0 The ordinary account (O), written first

**P1. "A decree binds those under the seat."**

| link | plain sentence | O: what a player expects (a run could contradict each) |
|---|---|---|
| P1.1 | a seat exists and someone sits in it | only the sitter can decree through it; a stranger, a former holder and an empty seat are refused, visibly (E1) |
| P1.2 | the sitter issues a decree | one event, with an author, a seat, a time and **content** (what is ordered, of whom) (E2) |
| P1.3 | "those under the seat" | a definite set: the persons and seats below this seat's rung in its own ladder, not persons under another seat, not the issuer (E3). A count's decree reaches his county, not the realm |
| P1.4 | the decree reaches them | each addressee learns of it, with its content, at a pace the calendar allows; distance may delay it (E6) |
| P1.5 | "binds" | each addressee is thereafter under an obligation he can keep or break: obeying does the thing ordered; **breaking it is possible and costs something the issuer can see** (E4, E5). Under the standing rule, whether a given addressee obeys goes by his own choice and a draw, never by fiat |
| P1.6 | the world changes | the ordered thing happens where obeyed (stores move, a man is installed, a levy is raised) and does not where defied (E4 zero: no decree, no change) |
| P1.7 | it ends | revocation, expiry, the issuer's death or loss of the seat: the decree lapses or passes to the successor, one or the other, by a stated rule (E7) |
| P1.8 | neighbours | a stronger seat's decree outranks a weaker one's on the same matter; `revoke` undoes `issue` (E11) |

**P2. "A vacant seat is filled."**

| link | plain sentence | O |
|---|---|---|
| P2.1 | a seat falls vacant | by death, resignation, removal or term; the vacancy is an event others can learn of (E2, E10) |
| P2.2 | someone has the right to fill it | by the seat's rule: an heir inherits, a superior appoints, a body elects; a seat with no rule says so (E1) |
| P2.3 | that someone acts | **within a season or two**: a vacancy is the most urgent thing on a ruler's desk in any strategy game; an empty throne for years is a crisis, not a default (E6, [GENRE]) |
| P2.4 | candidates | more than one eligible person may exist; who gets it depends on standing, favour and a contest, and can go either way (standing rule) |
| P2.5 | the new holder holds | he has the seat's powers the day he sits; the old holder's do not linger (E7, E8) |
| P2.6 | a vacancy that is not filled costs | the seat's work stops: its decrees, its court, its levy (E12: a seat whose emptiness changes nothing is dead) |
| P2.7 | bounds | a seat with no eligible person; a realm with every seat empty; the last member of a body (E9) |

**P3. "A war is declared and fought."**

| link | plain sentence | O |
|---|---|---|
| P3.1 | someone with standing declares | a ruler or a body with war powers, not a clerk; the declaration names an enemy and (genre) a cause (E1) |
| P3.2 | the declaration is known | both sides learn they are at war; third parties can learn it (E10) |
| P3.3 | being at war changes what is allowed | hostile acts against the enemy become licit that were not in peace (E4); allies are called |
| P3.4 | forces are raised and sent | by those with authority over men and stores; raising costs (E8) |
| P3.5 | battles are fought | where armies meet; outcome by a draw weighted by strength, ground and command (standing rule) |
| P3.6 | battle results move the war | land, fortresses, prisoners, or the will to continue (E4). A battle that changes nothing but a casualty list is half a war |
| P3.7 | the war ends | by treaty, surrender, exhaustion or conquest; someone has the standing to end it; the end has terms (E6, E7) |
| P3.8 | zero case | no declaration, no war: attacking in peace is a distinct, worse act (E4 zero, E11) |

**P4. "A faction is the sum of its persons' acts."**

| link | plain sentence | O |
|---|---|---|
| P4.1 | a faction has members | a definite set of persons, each a member by his own standing act, each able to leave (E3) |
| P4.2 | "the sum" | what the faction has (land, men, money, seats, reputation) is the total of what its members have; what it did is the total of what they did. Nothing is credited to the faction that no member did (E8) |
| P4.3 | the sum responds to its terms | a member's gain is the faction's gain; a member leaving or dying lowers the sum; a faction of zero members is nothing (E4, E9) |
| P4.4 | others read the sum | other persons treat the faction as strong or weak, friend or enemy, by that sum; and the sum they see is what they could know, not the true total (E10) |
| P4.5 | the faction "acts" only through persons | a faction's war, policy or betrayal is traceable to named persons' acts; two members can pull opposite ways and the faction then shows a split, not an average (E2, [GENRE]: factions in strategy games have a stance) |
| P4.6 | a faction rises and falls | over a campaign the sums change rank; a faction can be destroyed or founded (E6, E9) |

**P5. "An officeholder who fails his duty is called to account."**

| link | plain sentence | O |
|---|---|---|
| P5.1 | an office has a duty | something definite the holder is expected to do or keep (hold court, pay the levy, obey orders, keep the peace), knowable from the office (E3) |
| P5.2 | the holder fails it | a failure is an observable fact about what he did or did not do in a period (E2) |
| P5.3 | someone notices | a superior, a body or the governed learn of the failure; an unobserved failure goes unpunished (non-omniscience) (E10) |
| P5.4 | "called to account" | a proceeding: summons, hearing, a finding that can go either way (standing rule), in a venue with standing over him (E1, E2) |
| P5.5 | a consequence | reprimand, fine, removal, ban, by degree; proportionate to the failure (E4) |
| P5.6 | the diligent are not punished | an officer who does his duty is not called; the difference between the two is visible (E4 zero) |
| P5.7 | who guards the guard | the top seat's failure is answerable by someone or explicitly by no one (E9) |

**P6 (institutions fixed point, Jordan 2026-11-12). "Royalty is by noble conquest: the first king had the
greatest accomplishment in the secession war, then the first Duke of Hafenmark, then the first Duke of
Varfell; nobility is by deed."**

| link | plain sentence | O |
|---|---|---|
| P6.1 | a secession war happened | the world records it: a dated event with participants (E2) |
| P6.2 | accomplishments in it are ranked | three ranked deeds, each attributed to a founder: king first, Hafenmark second, Varfell third (E3, E4 ordered levels give ordered results) |
| P6.3 | rank follows the deed | the crown and the two duchies exist *because of* those deeds; the present holders' standing descends from them and a person in the world can say so (E10) |
| P6.4 | nobility is by deed | a new great deed can ennoble; a house with no deeds for generations is weaker in legitimacy than one with fresh ones; rank is contestable by accomplishment (E4, E11) |
| P6.5 | heirs | what passes to an heir is the seat and a claim on the founder's standing, which he must keep up or lose (E7) |
| P6.6 | the order matters | Hafenmark outranks Varfell by the founding order in some observable way (precedence, the claim to the crown if the royal line fails) (E4) |

### 2.1 The notes' account (N), in aggregate

Read after O. The code's own notes say, taken together: a decree is a `dispensation` Record minted into
its issuer's hand, addressed by `to`, and reaches its addressee only by a `give`
(`effects_information.py:254-272`; `world_q.py:3234-3260`); its being issued is "a matter of record …
public to everyone by definition" (`epistemic.py:649-657`); obeying and defying are emission-only
(`verb_table.yaml`, `comply`'s `writes_note`). A seat is filled by a superior seat whose purview reaches it
and whose row grants `confer`, never by the heir's claim unless the basis is `inheritance`
(`gate.py:697-698`, `:845-865`); "a seat declaring no basis is filled by NOTHING" (`:691-692`); "first
valid claim wins" (`:782-783`). A revocation is admitted for the seat "on the rung DIRECTLY above"
(`:604-606`) and costs an appointed man a permanent ban that "lasts until his death"
(`effects_governance.py:328-329`). War is a `WAR` Proposition with a live `commit`; "`T-m` gives peace to
the declarer" (`world_q.py:3576-3578`). "A faction does not act"; its holdings are its members' `hold`
edges (`faction_q.py:84-113`). Duty of office is CR-88, unbuilt. The notes nowhere mention the secession
war, a founder, or a ranked deed.

N is honest about most of what follows; the three places where N and the run part company are marked **N≠R**.

### 2.2 The running code (R), and the verdicts

All at `build_realm(0)`; hand-built acts through RESOLVE (`harness/army_presets.py::_fold`); deaths through
the engine's own writer (PROXY for a natural death, the game lane's X2 method). Scripts `pf1_static.py`,
`pf2_premise.py`, `pf2b_followup.py`, `pf5_heads.py`; outputs beside them (§5). Each row names its control.

**P1. "A decree binds those under the seat." — FAILS at "those under", at "binds", and at its end.**

| link | what ran | verdict |
|---|---|---|
| P1.1 standing | the King through `off_king`: `dispensation.issued`. No seat: `issue.unauthorized`. A stranger naming `off_king`, the Clerk naming `off_king`, the Heir through `off_heir` (remit `[]`): `issue.unauthorized` each. The King resigns (`release`: `tenure.closed`) and issues again through `off_king`: `issue.unauthorized` | **holds**, 5 of 5 refusals visible and keyed |
| P1.2 act | one Event, author, seat, tick; content is `terms` (one referent) and `to` | holds as an event; the content says nothing a person could do (F-FA-18, cited) |
| P1.3 "those under the seat" | the purview conjunct was tried for every living individual as addressee. King: 42 of 45 admitted (the three refused live in the Altonian settlement). Royal Marshal (seat on T1): 15 admitted, of **eight factions**, including 2 members of Varfell, 2 of Hafenmark and 1 churchman. Duke of Varfell: **2 admitted, both members of the Restoration Movement; 0 of Varfell's five members, his own council included**. Restoration leader (T15): **0 of 45** | **fails**. "Under the seat" as run is *resident on the seat's ground*, not *below the seat in its ladder*. Cause, read off `pf2b` §6: the purview of `off_duke_varfell` (`duchy_varfell`) reaches the home of no Varfell member (they live in buildings of settlements s_002 to s_008), and likewise the Duchess of Hafenmark's reaches the home of none of Hafenmark's four, herself included. The Duke may appoint the Military Jarl (`may_fill` asks the SEAT's rung) and may not order him (`issue` asks the PERSON's place): two ladders for one quantity |
| P1.4 it reaches them | issued inside a season by the seat-holder (player callback), everyone else idle. King's writ: 83 of 83 persons hold a `dispensation.issued` claim after one season (46 individuals, 37 peasant cohorts), 82 `told_by`. **The Royal Marshal's writ (a territory seat): 83 of 83 likewise.** In both, the addressee does not hold the paper and it is not in his `writs_held` | **fails in both directions**: every person in the realm, peasants in another duchy included, learns in the same season that a territory officer issued something; the one person it is addressed to cannot answer it. No distance, no delay |
| P1.5 "binds" | paper placed in the addressee's hand (the issuer's `give` is refused; placed by a `hold` edge): `comply` → `compliance.impossible`; `evade / defy` → `compliance.impossible`; `construe` → `construal.impossible`; world state moved: nothing in all four arms (the fourth arm does nothing, the control). The precondition also wants the terms read into his ledger; with that added the FA lane's H-260 reading is that both answers write nothing | **fails** (cited: F-FA-01). New here: the issuer's own `give` of his own writ to his own Marshal is refused, so the one route N names is closed to the realm's top seat at build |
| P1.6 the world changes | no arm moved state | fails (follows from P1.5) |
| P1.7 it ends | the issuer dies: the Record still exists, **live holders: none; the heir does not hold it** | **fails**: a dead King's decrees are orphan paper, neither lapsed by rule nor inherited. (A dead person's edges are deleted with him, the non-conformance against `04:360` the FA lane cites.) |
| P1.8 neighbours | nothing ranks two writs on one matter; `revoke` closes seats, not writs; no verb withdraws a writ | fails by absence (read, not run: no row in `verb_table.yaml` closes a `dispensation`) `[UNVERIFIED by execution]` |

Genre: a strategy player would be surprised three times: that a duke cannot give an order to his own
marshal-equivalent; that the whole realm knows of a clerk-rank writ at once; that nothing whatever follows
from disobeying. Words: `dispensation` (the FA lane's R-11) and "purview".

**P2. "A vacant seat is filled." — FAILS for 7 seats for ever, and where it holds it holds by the wrong hand.**

| link | what ran | verdict |
|---|---|---|
| P2.1 vacancy | a death closes the dead man's seat-holds and names them (`tenure.closed` with the seats as subjects; game lane X2) | holds |
| P2.2 someone has the right | enumerated over all 34 seats (`pf1`, and again filtered by the remit grant): **7 seats can be filled by nobody once empty** (`conferral: null`, `has_filler` false): the Duchess of Hafenmark's, the Duchy of Valorsmark, the Queen's, the Princess's, the guild leader's (`off_npc_084`) and the two Altonian seats. Of the other 27, 26 are fillable by a seat whose row grants `confer`, and **`off_king` and `off_widow_regent` (the Queen consort) are among the fillers of every one of the 26** | **fails** for the 7. For the rest: the right exists, and it is the Crown's everywhere |
| P2.3 someone acts | the game lane's X2 (cited; outputs `PES_GAME/x2_death_s0.txt`, `x2b_*`): the King dies at seed 0; the heir's `succeed` lands a season later; over three seasons 43 `confer` attempts name the lost seats and all 43 are refused; `off_duke_valorsmark` is empty at the end. FA lane: `tenure.opened` 0 in nine seed-seasons | fails in computed play except the one claim |
| P2.4 candidates, by a draw | every `confer`, `succeed`, `revoke`, `pardon`, `establish` and `release` here returned the same Event at every attempt; none carries a degree (`effects_governance.py`: the `res` argument is unused in all nine effects; "the first valid claim wins") | **fails the standing rule** (cited: `18_DETERMINISM_SWEEP.md` C-07, C-11) |
| P2.5 the new holder holds | the heir's claim: `succession.claimed`, he holds `off_king`; the dead King's second seat (`off_duke_valorsmark`) does not pass: `successions` has one row and that seat has no basis; the new King's own `confer` of it on himself: `confer.refused` | partly holds. **N≠R**: `_eff_succeed`'s docstring says "the King who dies holding two such seats leaves both to one claim"; the King does die holding two seats and one of them passes |
| P2.6 an unfilled vacancy costs | see §1.1's NO_SEATS arm | (measured there) |
| P2.7 bounds | **the Rebel leader dies**: none of the three surviving members can take the seat (`confer.refused`, `succession.refused` each); the seats that may fill it are `off_king` and `off_widow_regent`; the King confers it on his Guard Captain: `tenure.opened`. **The Confessor dies**: each of the four Cardinals' `confer`: `confer.refused` (no row of theirs grants `confer`); the King confers the Confessor's seat on his Guard Captain: `tenure.opened`, and `faction_q` then reads the Guard Captain as head of the Church; the Queen consort confers it **on herself** through `off_widow_regent`: `tenure.opened`. **The Duchess of Hafenmark dies**: Hafenmark's head is `None`, `world_q.vacancies` names the seat for 0 persons, the King's `confer`: `confer.refused`. **The King and the heir die**: the Queen consort names herself heir (`tenure.opened`) and claims the throne (`succession.claimed`): she is King; or she names a peasant cohort heir and **the cohort claims the throne: `off_king` is held by `cohort_set_s_001`**; the Duchess of Hafenmark and the Duke of Varfell each try `succeed`: `succession.refused`. **King, heir and Queen die**: seats able to fill `off_heir`: none; persons able to claim `off_king`: none; Valorsmark is headless for the rest of the game | **fails**, each case by execution |

Genre: a player who knows any dynastic game expects the body that elects to elect and the next in line to
inherit. Here the insurgents' leader and the head of the Church are the King's appointments, a consort can
make herself pontiff, a peasant village can be King, and the second house of the realm ends with its first
death.

**P3. "A war is declared and fought." — FAILS at standing, at licence, and at the end; "fought" is the MB lane's.**

| link | what ran | verdict |
|---|---|---|
| P3.1 standing | `utter` mood `WAR` naming Hafenmark and Varfell, then the utterer's `commit`: `at_war` reads true when the declarer is an unseated person in no faction, **a peasant cohort**, the King (party to neither), the Chief Parliamentary Clerk, or the Duchess of Hafenmark. Control: false before, in every arm | **fails**: anyone alive puts any two factions at war |
| bounds | Hafenmark at war with itself: `at_war(A, A)` true. A war between a faction id that does not exist and a person: `proposition.uttered`, `at_war` true. A party of two clerks formed a minute ago (any Proposition with committers resolves as a `Faction` view) declares war on Valorsmark: true | fails (E9): the Query reads two strings |
| P3.2 it is known | at the tick of declaration `enemies_heard` is non-empty for 1 person of the 9 members of the two factions (control at peace: 0) | not judged from one tick; no season was run on it `[UNVERIFIED]` |
| P3.3 war licenses | `at_war` has two readers in non-test code: `enemies_heard` (`world_q.py:3703`) and `:5150` (an instrument's count); no `requires` cell asks it (`04` F.33, open). A march needs no war (FA lane: 29 marches at seed 0 with `at_war` empty) | **fails**: war is not a state that changes what may be done |
| P3.4, P3.5 | MB lane and FA addendum F-FA-15 (a levy belongs to whoever minted the army Record), cited | — |
| P3.6 battles move the war | FA addendum F-FA-13 (no field outcome touches a holding or a seat), cited | fails |
| P3.7 it ends | the declarer dies: `at_war` true → false; the `WAR` Proposition still exists. `release` by the declarer ends it (the tree's own test) | holds for a war of one; it ends by an accident of bookkeeping, not by anyone's decision (F-FA-14, cited) |
| P3.8 zero case | no declaration, a march is the same act | fails (follows from P3.3) |

**P4. "A faction is the sum of its persons' acts." — HOLDS as arithmetic, FAILS as a polity; and there are two heads.**

| link | what ran | verdict |
|---|---|---|
| P4.1 members | at build 43 of 83 persons are members of exactly one faction; **40 are members of none: all 37 cohorts (the whole population of the realm) and 3 individuals**. Valorsmark is 11 individuals holding 11 seats; Hafenmark 4; Schoenland 1 | the sum is over the court. The governed are in no sum |
| P4.2 "the sum" | `Faction` is members, holdings, seats, head. It sums **edges**, not **acts**: no field is a tally of what members did; no stores, men or reputation | holds for holdings and seats; "acts" is not in the view at all |
| P4.3 the sum responds | the Duke of Varfell leaves Varfell (`release`): members 5 → 4, seats 4 → 3, **holdings 4 → 0** (every Varfell holding was his own `hold`); he still holds the ducal seat; `head` is still him, a non-member. He joins Hafenmark (`commit`, no one's consent, no draw): Hafenmark's holdings 4 → 8 and its seats include `off_duke_varfell`. **The King joins the Restoration Movement** (the insurgents): `commitment.made`; the Movement now reads 3 seats and 6 holdings, the realm's. The Duchess of Hafenmark also joins Varfell without leaving Hafenmark: a member of two. Every member of Hafenmark leaves: members 0, seats 0, holdings 0, `head` the Duchess; the four seats are all still held | **holds as arithmetic and that is the defect**: membership is unilateral, free, unrefusable and undrawn, so one man's sentence moves a duchy between factions; the view cannot tell a defection from a clerical act |
| P4.4 others read the sum | non-test readers of `faction_q.resolve`: one, the `survey` verb's `faction_sheet` Record (`effects_information.py:829`). Readers of `Faction.head` / `head_seat`: none but that Record and an instrument. `opinion_of` reads a **different head**: the creed Proposition's subject, fixed at build. At build the two agree for 4 factions and differ for the Restoration Movement and the Löwenritter (`faction_q.head` is `None`, the creed names a living leader). After the King dies and the heir claims: `faction_q.head` is the new King; the creed still names the dead man, so `opinion_of` regards nobody as Valorsmark's head (mean opinion of Valorsmark over individuals 0.569 → 0.500) | **fails**: two ladders for one quantity, and the one that tracks the seat is read by nothing that decides |
| P4.5 a faction acts through persons | holds (the FA lane's steelman 2, not re-attacked) | holds |
| P4.6 rises and falls | FA lane: ten faction tuples unchanged build to end at three seeds | fails in computed play |

**P5. "An officeholder who fails his duty is called to account." — FAILS at every link; what exists is dismissal without cause, hearing, draw or remedy.**

| link | what ran | verdict |
|---|---|---|
| P5.1 a duty | `Office` has fields `binds, body, body_function, conferral, faction, id, post, remit_acts, revocation, rung, scope_rung, upkeep`; none is a duty. The word "duty" in the Event log (`duty.taken`, `duty.refused`) is an oath of service TO a seat (`oblige`), not a duty OF one | **fails**: there is nothing for an officer to fail |
| P5.2, P5.3 failure, notice | no predicate; nothing to observe | fails by absence |
| P5.4 a proceeding | at tick 0, the Marshal having done nothing: the King's `revoke` through `off_king`: `revoke.refused`; through `off_duke_valorsmark`: `tenure.closed`, degree `None`. No summons, hearing or draw | **fails**, and fails the standing rule |
| who may call whom | of 34 seats, **6 can be stripped by anyone, all six by one seat, `off_duke_valorsmark`, and none through `off_king`** (the rule is the rung *directly* above, `gate.py:485`, `:604-606`; the realm is two rungs above T1). That seat is one of the 7 unfillable ones. After the King dies and the heir claims: **strippable seats in the realm: none**; the new King's dismissal of the Marshal: `revoke.refused` | **fails**: the realm's whole power of dismissal is one man's second title and dies with him. Appointment reaches 26 seats at any depth; dismissal reaches 6 at depth one: opposites that do not act oppositely (E11) |
| P5.5 a consequence, by degree | the dismissed Marshal gets a `ban` (object `off_duke_valorsmark`, no term). The King reappoints him: `confer.refused`. The King pardons him: `pardon.refused`. **`pardon` tried through every one of the 33 held seats in the realm: 33 refused** (a pardon is exercised through the ban's object seat by a holder whose grant carries `determine`; `off_duke_valorsmark` grants `confer, convene, issue, revoke`). The Duke of Varfell offers him Varfell's elected Military Jarl seat: `confer.refused`; control, the same seat to the Clerk: `tenure.opened` | **fails**: one consequence, the maximum, in every case, irreversible by anyone, reaching every seat of every faction |
| P5.6 the diligent are spared | the run above IS the zero case: a blameless officer at tick 0 | **fails**: `revoke` reads nothing about the man |
| P5.7 who guards the guard | `off_king.revocation: null`; also null for the Confessor, the Cardinals, the Grand Master: explicit, ruled | holds as stated (ruled; §4) |
| custody | a `detain` edge on the Marshal (placed by hand; the three `arrest` attempts drew `arrest.resisted`, `arrest.unauthorized`, `arrest.resisted`): he issues a writ through his seat: `dispensation.issued`; he convenes a sitting: `date.scheduled` | a prisoner governs from his cell: restraint and office do not touch |

**P6. The fixed point: royalty by noble conquest; nobility by deed. — ABSENT from the engine. Zero of six links are represented.**

| link | what ran | verdict |
|---|---|---|
| P6.1 the war happened | `grep -rni secession` over `engine/`, `modules/`, `references/` (`*.py`, `*.yaml`): no hit. The built world's log at tick 0 is empty; no Proposition, Record, claim, person or office carries "secession", "conquest", "founder" or "consecrat" (the three "deed"/"accomplish" hits are two heresy goals and one character's creed about bureaucracy). Canon carries it (`canon/03_canonical_timeline.md:72-84`, `:194`) | **absent**: the world has no past |
| P6.2 ranked accomplishments | nobody at build holds an event-kind claim about anybody: `deeds_judged` is non-zero for 0 of 45 judges of the King, 0 of 45 of the Duchess, 0 of 45 of the Duke | **absent** |
| P6.3 rank follows the deed | regard at build: the King non-zero for 13 of 45 (authored stance rows), mean +1.31; **the Duchess of Hafenmark and the Duke of Varfell: non-zero for 0 of 45, the same reading as the Chief Parliamentary Clerk** | **fails**: the two ducal houses are indistinguishable in standing from a clerk |
| P6.4 nobility by deed | conferral bases: `appointed`, `elected`, `annex`, `inheritance`. No seat is filled, kept or lost by a deed; `regard` (the only reader of deeds) gates no governance predicate | **absent** |
| P6.5 heirs | the three founding seats declare `inheritance` (King), `null` (Hafenmark), `elected` (Varfell). Hafenmark's ends with its holder (P2.7) | fails for Hafenmark |
| P6.6 the order matters | the royal line fails: the Duchess of Hafenmark's `succeed`: `succession.refused`; the Duke of Varfell's: the same; neither can name himself heir (`confer.refused`); nobody is ever King (P2.7) | **fails**: the order king, Hafenmark, Varfell has no expression |

The four institutions lanes each design how the fixed point should be carried (`15_INSTITUTIONS_*`, each
with a "three seeded Secession deeds" or equivalent); this row is the execution baseline they build from:
today the count is zero, and the control (the King's 13 stance rows) shows the reader would have seen it.

### 2.3 Premises that failed, in one place

| premise | fails at | by execution |
|---|---|---|
| a decree binds those under the seat | "those under" (residence, not ladder; a duke reaches none of his own); "binds" (nothing follows); reach (the whole realm at once, the addressee never); its end (orphan paper) | `pf2` P1, `pf2b` §6 |
| a vacant seat is filled | 7 seats never; the Church's and the insurgents' heads by the Crown only; a consort or a peasant cohort can be King; no draw anywhere | `pf1`, `pf2` P2, `pf2b` §2, §3, §7 |
| a war is declared and fought | anyone declares for anyone, self-war included; war licenses nothing; ends by its declarer's death | `pf2` P3 |
| a faction is the sum of its persons' acts | the governed are in no faction; joining is free and unilateral; the view is read by one verb; two heads | `pf1`, `pf2` P4, `pf5` |
| an officeholder who fails his duty is called to account | no duty; no proceeding; dismissal reaches 6 seats through one unfillable seat; its ban is total, permanent and unpardonable by anyone | `pf2` P5, `pf2b` §1, §4, §5 |
| royalty by noble conquest, nobility by deed | not represented | `pf1` (c), `pf2b` §7 |

