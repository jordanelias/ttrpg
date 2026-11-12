# PAPACY-GROUNDING — what the tree's own research adds to the Church design: an ordered plan

## Status: PROPOSED (an executable plan for a later session; ratifies nothing; nothing here is built)

Source: `audits/15_INSTITUTIONS_PAPACY.md` §15 (the re-grounding of 2026-11-12);
`unified/RESEARCH_MAP_INSTITUTIONS_A.md` §2 to §5. Composes on `15_INSTITUTIONS_PAPACY_A` to `_F` as
reconciled by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-02, X-15, X-29, X-31, X-33). It adds no
verb, no carrier, no tenure kind and no stored quantity. It amends one pass test, lets two existing
arrangement keys stand on one row, adds one eligibility clause, one emitted Event kind, and the rest
is content, gates and readings.

Research is tier 3 (`research/00_INDEX.md` §1). A citation below says why a shape is worth building,
never that a behaviour is correct (CLAUDE.md §0.05). Every figure in the sources is a lead.

## What it changes in `engine/season/` at runtime

| item | change at runtime | when absent |
|---|---|---|
| 1 the election at the electorate in force | a declared row with a share can no longer carry on zero ballots; `conclave` needs two fors; a candidate casts no ballot on his own candidacy | PAPACY-B's test as written: an election in which every elector abstains is carried |
| 2 the interdict as a deed of its issuer | `issue` of an instrument of form `interdict` also emits `interdict.laid`, which hearers judge by their own pursuits | an interdict is judged as any other writ |
| 3 absolution by a third authority's settlement | `pardon`'s favourable `evidence` gains a second source | penance is the only favourable evidence |
| 4 an exemption that lapses | an exempt house's `oblige` to the head seat is termed | the oath stands for ever |
| 5 to 8 gates, readings, content and design-first notes | none | — |

Items 5 to 8 change nothing at runtime and say so.

## The problem (evidence)

1. **The design's election assumes four electors; the rule in force gives two.** Audit §4.1: "an
   election is a contest among the Church's own departments". CR-35's bench is "the live seats of the
   vacant seat's faction whose grant carries `determine`". At `build_realm(0)` (map §5, E-M1) the
   Church seats carrying `determine` are `off_confessor`, `off_cardinal_justice` and
   `off_senior_inquisitor`. With the chair vacant, two men of one arm elect. The plan records it and
   records the question as confirmed at the default: "only the Cardinal of Justice and the Senior
   Inquisitor elect the Confessor … an authored electors list is AX-6's alternative and is Jordan's
   content … Default in force: the rule" (`workplans/valoria_master_workplan_v11_part12.md:366`;
   ED-IN-0301 at `_part4.md:222`). This is ruled and is **not re-raised**; the design is made correct
   at the electorate it will actually meet.
2. **At a small bench PAPACY-B's pass test fails.** Its edit 7: `fors * d >= n * (fors + againsts)`.
   With no ballot cast (every elector draws Partial, an abstention), `0 >= 0` holds and the candidate
   is carried. With two electors, one for and one abstaining is `3 >= 2`: carried by one man.
3. **The appointment cycle has no root.** "The Confessor confers the Cardinals, and the Cardinals in
   conclave confer the Confessor … If the Confessorate empties, the Church has no lawful way to fill
   it, and no lawful way to fill the seats that would make the conclave lawful"
   (`proposals/2026-08-30-play-space-coverage/03_seasons_church.md:600-603`, `:658-668`). With item 1's
   electorate the cycle is shorter still: the Confessor appoints the two men who elect his successor.
   The audit's E-1 saw a dead Cardinal go unreplaced.
4. **Fourteen mechanisms in the tree's research were not in the design** (audit §15.4), among them
   the interdict's backfire, settlement by a third authority, the mortal-enemies reply, retraction as
   relapse, the five ways a place resists a Church bench, and the consecration that a ruler does
   without.

## The resolution, decided, in landing order

### Item 1. The election at the electorate in force (amends PAPACY-B; lands with it)

*Sources.* The conclave's rules and their repeal, the bar on self-election "from 1621", and the
canonists' *sanior et maior pars* (`research/social_contest_procedures/04_decision_procedure_catalog.md:101-103`);
the cycle (problem 3); the plan (problem 1).

*Decided.*

1. **The pass test needs a vote for.** A row with `quorum_share: [n, d]` is carried only when
   `fors >= max(1, quorum)` **and** `fors * d >= n * (fors + againsts)`. That an election with no
   vote for it elects nobody is arithmetic by definition, not an outcome rule.
2. **`quorum` and `quorum_share` may stand on one row.** `quorum` keeps the code's meaning (fors
   needed, a head count: synthesis X-15) and is the floor; `quorum_share` is the pass mark. PAPACY-B
   edit 6 said "exclusive with `quorum`"; that clause is withdrawn.
3. **`conclave` ships `quorum: 2` beside `quorum_share: [2, 3]`.** Ladder step 4, precedent: the
   Church's one built declared row, `excommunication_deliberation`, ships `quorum: 2`
   (`engine/season/arrangements.yaml`). Nobody is made Confessor by one man's ballot.
   `[ASSUMPTION; medium; Jordan to correct. Revert: omit `quorum`; the floor is then 1 and the last
   elector names the Confessor.]`
4. **A candidate casts no ballot on his own candidacy.** An eligibility clause in the ballot loop
   (who may cast), not a result. It matters at once: the Cardinal of Justice is one of the two
   electors.
5. **What follows, stated so the scenario can show it.** Under the rule in force: a candidate from
   outside the Justice arm (NPC-039 Klapp, NPC-040 Jarnstal, the standing candidates of audit §10)
   needs both electors; the Cardinal of Justice as candidate can gather one ballot and so cannot be
   carried while the floor is two; with either elector's seat vacant no election is lawful, and only
   a Confessor can fill it. That is the cycle of problem 3 reached by persons' deaths, and it is the
   opening the audit's §9 item 12 describes (a crown's pressure, or a rival seat; not a council:
   D-51 rules that nobody judges the Confessor and drops the council). No
   rule is added to break it. Who may call a sitting is already data: `convene` is on
   `off_cardinal_justice` and `off_cardinal_fortitude`.
6. **PAPACY-B's gate is restated.** Its "four electors" are hand-built: the test plants `determine`
   on four seats of one faction on the spine fixture and says so. A second arm runs the built
   realm's own two electors.

*Exact edits.*

| # | file | edit |
|---|---|---|
| 1 | `engine/season/data/arrangements.py` (PAPACY-B edit 6) | `quorum_share` lawful only on `disposal: declared`; **may be combined with `quorum`** |
| 2 | `engine/season/loop/effects_information.py`, the ballot loop of `13_SC_draw_for_unrolled_contests.md` edit 3 (PAPACY-B edit 7) | pass test: `fors >= max(1, row.get("quorum", 1)) and fors * d >= n * (fors + againsts)`; before casting, skip a seated member who is the party of the docketed petition |
| 3 | `engine/season/arrangements.yaml` | the `conclave` row gains `quorum: 2` |
| 4 | PAPACY-B's gate text | "four electors" → "four hand-built electors (the spine fixture; `determine` planted on four seats)"; add the built-realm arm below |

*Gate (execution artifacts, `PYTHONHASHSEED=0`).*

- **Zero ballots.** Hand-built, every elector's draw pinned to Partial: the candidacy is not carried
  (before the edit it is). This is the planted failure of the present text.
- **The built electorate.** A case file of PAPACY-F's shape (`base: realm`) whose one set-up act
  is the Confessor's `release`, and a petition by NPC-039. 200 seeds: the seat opens in some and not all;
  the exact probability is printed from the two ballots' odds. With `off_senior_inquisitor` also
  vacated: the seat opens in no seed and the report prints "no lawful election: 1 elector".
- **The candidate's ballot.** A petition by the Cardinal of Justice's holder: his ballot is not
  cast in any seed.
- *Control.* The `conclave` row absent: base hash.

*Falsifier.* A candidacy carried with fewer fors than the floor. The same outcome in every seed for
a given set of commitments. A sitting on the built realm that counts a ballot from a seat without
`determine`.

*Cost.* small build; lands inside PAPACY-B's batch 2.

### Item 2. The interdict cuts both ways (amends PAPACY-D; lands with it)

*Sources.* "The weapon works by making the *populace* miserable so that it pressures the *ruler*;
but prolonged use bred resentment against the clergy itself and confiscations flowed the other way —
a genuinely two-edged instrument" (`research/fa_se_historical_precedent_research_v1.md:148`); the
per-season backfire of SE-8 (`:288`); the retired sim's failed excommunication, "Church `L −1`,
target `L +1` (sympathy)" (`research/cross_scale_action_catalogue_v1.md:123`).

*Decided.* PAPACY-D lets hearers judge a sentence through the kind `ban.opened`. An interdict has
no kind of its own, so the people of the place cannot hold it against the seat that laid it. The
`issue` row gains one emitted kind, `interdict.laid`, when the instrument's form is `interdict`
(synthesis X-02's form), attributed to the issuer; PAPACY-D's alignment cells gain a column for it
(first values as that proposal's `ban.opened` cells, `[ASSUMPTION; Jordan to correct]`). Each
resident who learns of it judges it by his own pursuits, weighted by what he lost (his own
shortfall claims, which PAPACY-D already has him hold). The lord's `seize` of Church stores on his
ground is the confiscation, an existing act; nothing is added for it.

*Exact edits.* `engine/season/verb_table.yaml: issue`: `emits` gains `interdict.laid` on the branch
whose instrument form is `interdict`. `[UNVERIFIED: whether the row's `emits` can branch on the
minted instrument's form. If it cannot, the effect `loop/effects_information.py::_mint_document`
appends the Event where it stamps the form, as PAPACY-D edit for `ban.opened` does for
`determine`.]` `engine/season/rosters.yaml: tables.alignment`: one column.

*Gate.* PAPACY-D's planted interdict, two arms over 200 seeds: with the kind, mean `regard` of the
place's residents toward the issuing seat-holder falls more where their shortfall is larger; without
it, it does not move. The lord's standing is read beside it: the design intends both to fall, by
different amounts for different persons. *Falsifier.* The Church's regard unmoved in both arms.

*Cost.* small build.

### Item 3. Absolution by a third authority's settlement (amends PAPACY-D; after the verb lane's `covenant`)

*Sources.* Venice, 1606-07: the two authorities contended until "France mediates; Cardinal de
Joyeuse takes custody of the two priests … interdict lifted; Venice keeps its laws"
(`research/social_contest_procedures/01_venice_procedure.md:167`); "In every row `appeal_basis` is
a different authority than the bench … it never rehears"
(`research/social_contest_procedures/02_inquisition_heresy_procedure.md:125`).

*Decided.* PAPACY-D's P-8 reads one favourable `evidence`: a matured termed `oblige` of the penitent
(penance). It gains a second: a live instrument made by `covenant` to which the sentencing seat is
a party and whose terms name the excluded person. The pardon is still the sentencing seat's act and
still a draw. `[UNVERIFIED: the terms a `covenant` instrument can carry; `covenant` has not executed
in a computed run (`workplans/valoria_master_workplan_v11_part2.md:23`: "`covenant` 0 of 41 executed"). The executor
opens `14_VERBS_BINDING`'s `covenant` row first; if a covenant cannot name a person, this item
waits.]`

*Gate.* A planted ban, three arms over 200 seeds (no evidence; penance matured; covenant held):
P(restraint ends) rises in the second and third arms and is neither 0 nor 1 in any.

*Cost.* small build.

### Item 4. An exemption that lapses, and visitation (amends PAPACY-E items 3 and 4; content)

*Sources.* Exemption got by petition, for which "the org owes ongoing **Debt** to the granting
faction (relitigable if Standing lapses)" while "Local authority loses jurisdiction/revenue"; the
general chapter and the inquiry turned inward on "a *branch head*"
(`research/proactive_governance_scale_research_v1.md:72`, `:80`; self-labelled sketches).

*Decided.* (a) The exempt house's `oblige` to the head seat is sworn with a term (the shipped
`oblige_term`), so exemption is renewed or lapses, and the see it was exempt from regains reach
when it lapses. (b) Visitation is not a verb: it is `interview` and `research` by a holder of the
head seat or of a Cardinal's seat at a see, and what he learns is the ground for P-9. One reading:
P-9 attempts preceded by such an inquiry against those that were not.

*Exact edits.* In PAPACY-E's exempt-house content row, the `oblige` is termed. No code.

*Cost.* edit (content).

### Item 5. Gates that need no edit (with PAPACY-C and PAPACY-D)

| gate | what it shows | source |
|---|---|---|
| **retraction as relapse** | a penitent who breaks the termed `oblige` of P-8 (his own `release` where the penance was his own oath; a failure to keep its terms where it was imposed, since D-54 bars a convict's own release) and is tried again: the second hearing's `evidence` includes the first case file (CR-61), and its odds differ from a first hearing's | "Retraction made relapse, which silenced the defenders" (`02_inquisition…:54`) |
| **the mortal-enemies reply** | under the inquisitorial rite, testimony from a concealed accuser toward whom the accused holds a hostile stance weighs less once the accused has named him; a dismissal on that ground is a deed of the accuser | "if the accuser is among them the charge fails and a false accuser faces life prison" (`02_inquisition…:28`). Depends on SC's evidence proposals reading the witness's relation to the party; if they do not, this is listed for the SC lane and not built here |
| **a larger room is a milder room** | the same case before `inquisition_hearing` (one determiner) and before `excommunication_deliberation` (the declared row): the share of sentences is lower in the second | the *consilium*, "usually followed, and milder" (`02_inquisition…:31`) |

### Item 6. Readings added to the scenario report (no game code; with PAPACY-F and after D)

| reading | computed from | source | it fails when |
|---|---|---|---|
| **seasons vacant, and who acted against the sitting** | ticks from the head seat's `tenure.closed` to its next `tenure.opened`; `evade / defy` by the sitting's venue-holder | the enclosure "suspended in 1276 and reinstated in 1294" (`04_decision…:101`) | every seed elects in one season, or none ever does |
| **the secular arm withheld** | Church benches' sentences needing an `arrest` by a seat with purview that was not made within N seasons | Philip IV's order "no longer to obey inquisitors' commands to arrest" (`02_inquisition…:71`) | no sentence ever needs another seat's act |
| **carried to another authority** | `petition`s by a party of a Church matter to a seat of another faction, and what that seat then did | "Carry it to another authority … a suspension; a royal commission" (`02_inquisition…:102`) | none in any seed |
| **the summons refused** | parties cited by a Church bench who were elsewhere at the sitting | Bohemia: "proceeding cannot reach them; ends in negotiation" (`:103`) | — (a count) |
| **a reign without the rite** | holders of a consecrable seat with no certificate, by seasons held; `legitimacy` readings toward them over time against consecrated holders | "a deliberate rupture that decoupled imperial legitimacy from papal ratification for good" (`research/governance/governance_modes.md:190`) | consecrated and unconsecrated holders read the same in every seed (the certificate is decoration) |
| **the tainted rite** | certificates whose determiner, or a doer of a deed they recite, later fell under a `ban`; holders' `legitimacy` before and after among persons holding both claims | "her condemnation implied a coronation by a heretic" (`02_inquisition…:60`) | — (a count; needs D) |
| **the appointer's men** | after a new Confessor, `revoke`s against seats the last one filled; stores those holders moved to their own rungs | "the extraction, not the office, survives" (`research/rise_to_power_roster_system_research_v1.md:304`) | no `revoke` by a new Confessor in any seed (PAPACY-B's item 4 is ruled yes: D-50) |

### Item 7. Design-first: the Crown's objection (cross-lane; nothing to build now)

*Sources.* The exclusive, "once per conclave" (`04_decision…:101`); the tree's own refined proposal,
"a **Crown-alone** Override hung on the Father Gustav Linder Crown-liaison channel"
(`.audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:120`); audit §14 had
listed the secular veto as decorative.

*Shape, for when it is designed.* No override and no veto. The Archbishop's Representative's seat
(`off_archbishops_rep`, NPC-034) states the Crown's objection to a candidate as an act electors
learn of; its weight is each elector's own `obligation` and `regard` toward the objector, which are
already per-member terms of the ballot (synthesis X-15). An elector who owes the Crown nothing
ignores it. The open design question is which existing act carries the objection on a declared row
(a counter-petition, or a `tell`), and that is the SC lane's. Cross-listed in
`15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md` (audit §18.4 item 10).

### Item 8. Content notes and referents (no edit)

- **Naming.** Do not name anything after the cardinal-nephew: "'Cardinal' is already the Church
  Standing-6 title" (`rise_to_power…:66`). The appointer's kin are simply persons he conferred.
- **A see has an archived name.** The archived Church ladder's territory-scale rung is the Bishop's
  Delegate, who "may conduct ecclesiastical trials in own territory"
  (`.designs/systems/factions/reference/faction_politics_v30.md:337`). Research and archive supply no
  canon name; the post's name on PAPACY-E's see rows is Jordan's.
- **Where a see is vacant there is no channel.** "Where a benefice is unfilled … there is no priest,
  so there is no channel" (`03_seasons_church.md:314-316`). PAPACY-D's publication and PAPACY-E's
  tithe both reach a place through the seat-holder there; the scenario for E should include one
  vacant see so that the difference shows. Under D-22 ("proclaimed": whoever learns a decree was
  issued knows its terms) the difference is in who learns of it and who is there to withhold or
  collect, not in who holds paper.
- **The preacher with no chair** (audit §15.4 item 13) is a roster row, Jordan's content.
- **The archived Holy See.** The archive made consecration wait on an off-stage Holy See
  (`faction_politics_v30.md:354`). The code has no such power and this plan adds none; audit §13
  item 2 asked about that hole and is answered: nobody (D-51).

## Rulings of 2026-11-12 that bear on this plan (`unified/DECISIONS_ANSWERED.md`)

| ruling | what it settles here |
|---|---|
| D-14 (A-14): a vote is "a draw on the voter, inside the presiding person's act" | item 1 is written on that shape: the tally is arithmetic over drawn ballots inside one act; the floor and the self-ballot clause are eligibility and arithmetic, not outcome rules |
| D-50 (A-35): the head strips an officer, by a resistible draw | PAPACY-B's item 4 is no longer held; item 6's "the appointer's men" reading is live |
| D-51 (A-36): nobody judges the Confessor; the council is dropped | PAPACY-E's item 5 and P-13 go; the appointment cycle of problem 3 therefore has no lawful exit, which raises the stakes of item 1's floor: `[ASSUMPTION; Jordan to correct]` stands on it |
| D-54 (A-37): a convict may not release an imposed service | item 5's retraction gate is worded for both a sworn and an imposed penance |
| D-22 (A-21): a decree is proclaimed | item 8's vacant-see note |
| D-13 (A-13): a seat may declare clerks, paper-hands and an exit audit | the Byzantine grounding plan's `audit_at_exit` content; nothing here |

The Cardinal electorate is not among them: it was confirmed at the default earlier (ED-IN-0301) and
is not re-raised.

## Order and dependencies

Item 1 inside PAPACY-B's batch (after CR-35 and the SC ballot). Items 2 and 3 inside PAPACY-D's
(after FA-P1, SC-P4, SC-P6; item 3 also after the verb lane's `covenant`). Item 4 with PAPACY-E.
Item 5 with C and D. Item 6 with F, growing as D lands. Item 7 waits on SC. Nothing here moves a
batch earlier.

## Falsifier for the plan as a whole

If, after items 1 to 3, the report of item 6 shows every seed electing in one season, no sentence
ever resisted, and consecrated and unconsecrated holders reading alike, then the Church is a set of
switches and the research transferred as names only.

## NERS (definitions `CLAUDE.md` §0.06; E last, as a ratio)

- *N.* Cut item 1 and the first playable Church scenario can be carried by nobody voting, or by one
  man; that is a defect at the electorate the game will run, from every direction (the candidate,
  the elector who abstains, the Crown reading the result). Cut item 2 and the interdict costs its
  issuer nothing, so it is always worth laying, which is the over-issue of audit §3.14 with no
  brake. Item 3 is narrowed: it holds top-down (a mediator's route) and has no bottom-up use until
  `covenant` executes.
- *R.* An elector's abstention now matters; a lord under interdict can wait for the people to turn
  on the bishop; a third seat can broker. With no player, vacancies lengthen and end by persons'
  acts, and the cycle of problem 3 can be reached and seen. Completeness: at zero or one elector
  nothing is carried and nothing breaks.
- *S.* One ballot (SC's), one tally (X-15), one pass test; the floor is the code's own `quorum`.
  One more deed kind judged through the one alignment table.
- *E, against that.* One clause in a pass test, one eligibility line, one row value, one emitted
  kind and one evidence source, against an election that cannot be carried empty, a sanction with a
  price, and a third way out of a sentence.

## What stays out

Everything in audit §15.6 is memory-grade and carries no edit. Sanctuary needs a venue term on
`arrest` owned by the verb lanes. Chapter capture is canvassing and needs no Church rule. The
franchise gated by church standing is content on an existing predicate. Nothing here reads `.audit/`
or `.designs/` at runtime; they are cited as referents only.
