# FA — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-35, L-10) — §15 (d): `comply` and `evade / defy` carry alignment cells (settled by parse); §14's pool-reader path corrected to `seam/wrappers/pool.py::faculty`. No finding changed.

## Read at: 601e715 (working tree)

Subsystem: factions, governance, offices, war and diplomacy (dossier `06_FA.md`): lane FA, and the IN
positions that build the governance slice. Every reading names its command, seed and season count in §12.
`[UNVERIFIED]` marks what was not checked. Proposals this audit carries are under
`proposals/2026-11-12-subsystem-audit-suite/proposals/06_FA_*.md` and are PROPOSED, not ratified.

## 0. Verdict

**Not yet: FA as coded is a sound skeleton and not yet a basis for emergent political narrative.** The
skeleton is right and is hard to break: authority is a property of the seat exercised (`Act.via`), a faction
is a derived view with no verbs and no stored state, the preconditions and the write gate ask one set of
predicates, and no entity or outcome is special-cased in code. What is missing is force and turnover. In
computed play authority neither binds anyone nor changes hands: in the realm over three seasons at seeds 0,
1 and 2, 91 decrees were issued and none was held, obeyed or defied by an addressee; no seat was conferred,
revoked or inherited; every faction's member, seat and holding counts and its head were the same at the end
as at the build except for one death at each of seeds 1 and 2; and no two factions were at war (E-5). **The single largest obstacle
is that the governance acts that execute (`issue`, `dispatch`, `convene`) are emission-only, so they
produce claims that other persons attend to with generic verbs, while the acts that redistribute power
(`confer`, `revoke`, `succeed`, a determination's disposal, a declaration of war) either do not execute in
computed play or do not exist as verbs.** R-01 and R-02 hold through governance in the weak sense (a decree
or an order becomes the occasion of other persons' later acts) and fail in the strong sense the charge
asks about (nothing another person later decides is conditioned on what the decree said).

## 1. What it is, as coded

**There is no FA module.** FA is not a registered module under `modules/` (which holds `combat`,
`fieldwork`, `mass_battle`, `settlements`, `social_contest`) and no `composition_roles:` row in
`references/module_contracts.yaml` targets one. It is a slice of the season loop itself (`engine/season/`,
Layer 2):

| piece | file | what it is |
|---|---|---|
| nine effects | `engine/season/loop/effects_governance.py` | `confer` (`:58-142`), `succeed` (`:145-182`), `establish` (`:185-247`), `release` (`:250-298`), `revoke` (`:301-354`), `pardon` (`:368-396`), `convene` (`:411-458`), `oblige` (`:461-507`), `requisition` (`:510-549`). Each returns a `Change` (named subjects and a `perform` closure) that the write gate applies; none calls `w.write`; none holds state. |
| eight untyped preconditions | `engine/season/loop/predicates.py` | `_req_confer` (`:115-179`), `_req_succeed` (`:182-196`), `_req_establish` (`:313-425`), `_req_release` (`:428-456`), `_req_oblige` (`:466-525`), `_req_revoke` (`:566-615`), `_req_dispatch` (`:618-624`), `_req_convene` (`:627-673`). Each asks the gate's own predicates, imported from `state/gate.py` (`:44-46`), so a precondition cannot admit what the gate refuses. |
| the authority predicates | `engine/season/state/gate.py` | `seat_hold` (`:345-367`), `purview_reaches` (`:386-461`, containment plus the oath clause), `REVOCATION_RULES` (`:617-618`), `REVOCATION_DISPOSAL` (`:653-654`), `FILLED_BY` (`:697-698`), `may_claim` (`:770-786`), `may_revoke` (`:830-842`), `may_fill` (`:845-865`), `death_subjects` (`:1819-1832`). Three import-time totality checks refuse a basis with no rule. |
| the faction view | `engine/season/queries/faction_q.py` | `Faction` (`:84-95`), a frozen five-field view (`proposition`, `members`, `holdings`, `seats`, `head`) built by `resolve` (`:98-113`); `head` (`:116-156`), `holdings`, `purview`, `superiors`, `subordinates` are functions. Never a field of `World`, never `Act.actor`. Membership is a live `commit` (`world_q.py:2027-2038`). |
| data the loop opens at runtime | `engine/season/offices.yaml` (31 seats, 2 foreign seats, the `titles.domains` ladder), `arrangements.yaml` (nine proceedings rows, six speech kinds; loader `data/arrangements.py`), `rosters.yaml` (`remit_acts`, `conferral_bases`, `revocation_bases`, `successions`, `factions.head_seat`), `goals.yaml` (organization goals; loader `data/goals.py`), `data/affiliations.py` (affiliation checks, the `incompatible` half-matrix, the verb × affiliation table) | content and closed sets. |
| fixture and instruments | `governance_spine.yaml` and `harness/governance_spine.py` (a regular 13-seat world), `harness/obligee_report.py`, `harness/heir_hears.py`, `harness/aperture.py`, `harness/interactions.py`, `harness/strife.py` | readers; none is on the game path. |

**The rule the code implements.** *A faction does not act* (`predicates.py:85-88`). A faction is a
Proposition persons `commit` to; a faction's act is a person's act through a seat; its holdings are its
members' `hold` edges; its treasury is `Rung.stores` at the seat's rung (`effects_governance.py:538-544`).

**How the loop reaches it.** A person holding a seat carries that seat's `remit_acts` as a snapshot on the
`hold` Tenure (`Tenure.granted_acts`). `decision/options.py::opening_set` forms a `remit:<act>` candidate
only for a holder whose grant names the act; `decision/choose.py` stamps `via`; RESOLVE asks the row's
`requires` (a typed cell or a predicate above), runs the effect, and the gate admits each Tenure edge under
a named basis. Six remit acts gate nineteen of the table's 67 rows (E-2):

| remit act | verbs it opens |
|---|---|
| `issue` | `issue`, `covenant`, `requisition`, `seize` (and `transfer`'s seat alternative) |
| `dispatch` | `dispatch`, `march`, `capture`, `arrest`, `raze`, `marshal`, `surrender` |
| `determine` | `determine`, `open_case`, `pardon`, `interrogate` |
| `confer` | `confer`, `establish` |
| `revoke` | `revoke` |
| `convene` | `convene` |

`release`, `oblige`, `succeed`, `commit`, `comply`, `evade / defy`, `construe`, `petition` and `survey` are
`own`-eligible.

**State it owns.** None. It writes `Tenure` edges (`hold`, `oblige`, `ban`, `detain`), `Office` rows,
`w.dates` and `Rung.stores`, all through the gate.

**Execution evidence (seed and season count in §12).**

- `python -m engine.season.harness.governance_spine` prints a census and runs no season: 13 offices, 13
  seated persons, 26 rungs, place depth 6 (E-1).
- `aperture 2 0` (E-3), realm, 83 persons, 33 seated, control hash EQUAL. Seat-gated rows that executed:
  `convene` 12, `dispatch` 12, `issue` 19 of 26, `march` 13, `open_case` 7 of 15, `establish` 1 of 8.
  Never attempted though formed: `confer` (formed for 5 persons), `revoke` (5), `pardon` (8), `arrest`
  (1). Never formed: `succeed`, `interrogate`, `marshal`, `surrender`. Attempted and always refused:
  `determine` 2, `covenant` 10, `seize` 9, `raze` 14, `capture` 12, `requisition` 1. Among the `own` rows:
  `oblige` 26 of 26 executed, `commit` 65 of 65, `petition` 20 of 20, `release` 0 of 15, `comply` 0 of 33,
  `evade / defy` 0 of 5, `construe` 0 of 7. `tenure.opened`, `tenure.closed`, `succession.claimed`,
  `compliance.given`, `compliance.withheld`, `matter.determined` and `requisition.taken` are among the 102
  declared kinds never emitted.
- The FA probe (E-4, E-5) over the spine (seeds 0 to 4, four seasons) and the realm (seeds 0, 1 and 2,
  three seasons) is the source of the verdict's figures and of F-FA-01, F-FA-02 and F-FA-04.
- `heir_hears --seeds 0 1 2 --seasons 4`: at seeds 0 and 1 the throne was not vacated; at seed 2 it was
  vacated in season 4 and the living heir heard of it; control clean at every seed (E-6).

## 2. Steelman

Ranked by the weight each bears.

1. **Authority through the seat, asked once.** `Act.via` names the seat exercised; `seat_hold` refuses a
   `via` the actor does not sit in; every purview walk goes through the seat's rung. The preconditions
   import the gate's predicates instead of copying them, so the fold refuses and emits where the gate would
   otherwise raise. *Attack:* find a precondition that reads the actor instead of the seat, or a copy of a
   gate rule. I read all eight predicates and the nine effects against `gate.py`; none does. `_req_establish`
   is deliberately stricter than the gate by one case and says so (`predicates.py:356-360`). **Holds.**
2. **A faction is a view, and nothing can make it more.** `Faction` is frozen and built per call; `faction_q`
   writes nothing; an import-time check ties the `faction_sheet` Record's keys to the dataclass fields
   (`faction_q.py:225-245`). *Attack:* grep the non-harness Python under `engine/season/` for an entity or
   faction literal that selects a branch. The hits in `loop/`, `state/`, `queries/`, `decision/` and
   `data/requires.py` are all in comments (E-9). **Holds**: the scripting-drift test passes at the code
   level (§5.3 for the data level).
3. **Closed sets with total mappings.** `REVOCATION_RULES`, `REVOCATION_DISPOSAL`, `FILLED_BY` and
   `successions` are refused at import unless total over their rosters (`gate.py:622-629`, `:657-681`,
   `:705-729`, `:746-767`), so a new basis cannot land without its rule. *Attack:* a basis value reachable
   with no rule. Only a hand-mutated `Office` reaches one, and `_req_revoke` and `_eff_revoke` refuse it.
   **Holds.**
4. **Vassalage is an oath the vassal owns, not a stored parent.** `purview_reaches`' oath clause reads a
   live, non-imposed `oblige` from a seat-holder (`gate.py:422-461`), so detachment is the swearer's own
   `release` or an unpaid term maturing. *Attack:* does anything in computed play release such an oath?
   `commitment.ended` and a released seat-oath are both absent in every run here; the mechanism is right and
   unexercised. **Holds as mechanism; narrowed as behaviour.**
5. **Succession is a claim, not a script.** The heir is a title; one `succeed` act opens every vacant seat
   the title passes and closes the title in the same write (`effects_governance.py:145-182`), and a death
   names the seats it vacates so witnesses hold claims about them (`gate.py:1819-1832`). *Attack:* does a
   seeded season exercise it? In four seasons the throne was vacated at one seed of three (seed 2, in the
   last season), and there the living heir was handed a question naming it (E-6). **Holds, and the hearing
   link is observed once; the claim itself was not read, because the run ended with the vacancy.**
6. **The plan already owns most of what is missing.** B10-17 and B10-17b schedule `declare`, alliance and
   peace, the election arm, nomination, deposition, the casus-belli gate, the clocks and duty of office.
   *Attack:* are those positions reachable in computed play once built? Several state themselves that they
   land hand-built only (CR-35's and CR-37's REACH paragraphs, owner H-80). **Narrowed**: the plan builds
   mechanisms faster than it builds the occasions that would make a person choose them (F-FA-02).

## 3. Adversarial findings

Worst first. "Falsifier" is the observation that would have shown the claim wrong, and its outcome.

### F-FA-01 · blocks R-04 and R-02 through governance · a decree binds nobody and reaches nobody as a writ

- **Claim.** An executed `issue` mints a `dispensation` into its issuer's own hand and stops. The addressee
  never holds it, so `comply`, `evade / defy` and `construe` never form on it; and if a writ is hand-placed
  on the addressee, obeying and defying write nothing.
- **Evidence.** `queries/world_q.py:3234-3260`: a writ is minted to its maker, the writ-to-addressee mint was
  refused (ED-IN-0292 (1)), and it "reaches its addressee only by a `give`". `verb_table.yaml`: `comply`,
  `evade / defy`, `construe` carry `writes: []`. `give` executed once in two realm seasons (E-3).
- **Falsifier and outcome.** One writ held by an addressee, or one `compliance.given` or
  `compliance.withheld`, in any run. Spine, seeds 0 to 4, four seasons: 19 writs, 0 held by an addressee, 0
  persons with a non-empty `writs_held` (E-4). Realm, seeds 0, 1 and 2, three seasons: 29, 21 and 41 writs,
  none held by an addressee, 0 compliance events of either kind (E-5). `aperture 2 0`: `comply` attempted 33,
  refused 33 on `exists:dispensation=0` (formed on other Records); `evade / defy` 5 of 5; `construe` 7 of 7
  (E-3). The hand-placed case is H-260's reading (20 seeds, not re-run here).
- **What does propagate.** `dispensation.issued` is a `binding_decision` kind, so `_ch_chronicle` deposits it
  on every living person (`epistemic.py:649-673`); other persons' later acts cite it as their occasion (40,
  59 and 68 acts at realm seeds 0, 1 and 2), led by `create_record`, `reconstruct`, `tell`, `train`, `move`,
  `challenge`. No act among them reads the decree's terms.
- **Touches.** R-04 (a decision at realm scale that decides nothing below it), R-02, R-05 (`comply`,
  `evade / defy`, `construe`).
- **Narrative consequence.** Authority has no force and defiance has no face. The governor who complies,
  bargains or defies (case NPC-083, `core`) cannot occur.
- **Minimal fix.** Proposal `06_FA_decree_binds.md`: the terms of a public writ reach its addressees as a
  content claim through the channel that already tells them it was issued; `comply` and its siblings form on
  a writ the person's own ledger names him an addressee of; the issuer's suspicion of a subordinate is a
  fold over his own claims of defied and obeyed writs, as Jordan ruled the accountability loop (D5, D6, E11;
  §5.2), and at a threshold it becomes the recall occasion, which is the general motive `revoke` lacks
  (CR-54). No stored state is added.

### F-FA-02 · blocks R-04's turnover · power does not change hands in computed play

- **Claim.** No seat is filled, stripped or inherited by a computed act at the horizons measured, and the
  faction view is static.
- **Evidence and falsifier.** A `tenure.opened` or `succession.claimed` Event, or a changed faction tuple.
  Realm seeds 0, 1 and 2, three seasons: `tenure.opened` 0 at every seed, `succession.claimed` 0; faction
  view (members, seats, holdings, head) identical build to end for all ten factions at seed 0, and at seeds
  1 and 2 but for the Church, which lost one member and one seat to a death; the dead man's seat
  (`off_cardinal_prudence`) was still vacant when each run ended; one `commitment.ended` at seed 2 (E-5). Spine, five seeds, four seasons: no
  office changed holder (E-4), and on the spine none can, because its offices declare no basis (E-10), so
  the realm is the evidence. `aperture 2 0`: `confer` formed for 5 persons and attempted 0; `revoke` the
  same; `succeed` formed 0 (E-3). The register records one computed `confer` at one seed in four seasons, a
  self-conferral (H-207's cite; not re-run).
- **Why.** Four causes, each with an owner. (a) *Vacancies are rare*: two seat-holders died in nine realm
  seasons over three seeds; no computed `confer` declares a term (H-290); `revoke` is ruled not driven
  (H-207 (A)).
  (b) *The question slot*: under `question_aggregation_rule: first` a landed claim sorts ahead of a `need`,
  and 690 of 774 deliberations answered a `claim_landed` question (E-3). (c) *Selection*: `confer` scores
  below the conferrer's other candidates on pursuit alignment alone (H-207's cite); nothing in `decision/`
  reads that the actor holds an office with a vacancy beneath it. (d) *Mechanisms without occasions*: the
  election arm, nomination and deposition are scheduled as hand-built routes whose computed reach waits on
  H-80.
- **Touches.** R-04, R-05 (`confer`, `revoke`, `succeed`), R-06.
- **Narrative consequence.** No rise, no fall, no succession crisis, no election. The cast at season N is the
  cast at build, less the dead.
- **Minimal fix.** Proposal `06_FA_seat_terms_and_turnover.md` (a seat's term as data on its `offices.yaml`
  row, read by `_eff_confer` when the act declares none, so elected and appointed seats fall vacant on a
  clock the world already runs); the defiance occasion of F-FA-01; CP-T09-06 and CR-35 as planned. The
  question slot is CORE's (H-54) and is cross-listed, not re-decided here.

### F-FA-03 · degrades narrative, R-04's aperture · the military verbs are open to clerks, by an unruled placeholder

- **Claim.** `march`, `capture`, `arrest`, `raze`, `marshal` and `surrender` are eligible to 26 of the 33
  seated persons because `dispatch` is kept on every loop-built seat by `offices.yaml: meta.remit_unruled`,
  not because any row grants it; and the one seat no row authors holds every remit act.
- **Evidence.** `offices.yaml:104-123` (the header's own account: 22 of 29 authored seats, "identical rows
  diverge by BUILD ROUTE") and `:139-146`; `harness/populated.py:1723-1740`. `aperture 2 0` PER HOLDER
  (E-3): the 13 marches that emitted `march.declared` were made by `p_npc_007` (the Guilds' economic
  representative), `p_npc_037` (Lord Treasurer), `p_npc_071` (Legal Advisor) and `p_npc_074` (Skald-Chief);
  the King, both dukes, the Royal Marshal, the Military Commander and the Military Jarl were offered `march`
  and did not attempt it. `p_npc_084` ("guild leader@None") reads `grant [confer, convene, determine,
  dispatch, issue, revoke] · eligible 67 of 67`, the same aperture as the King.
- **Falsifier and outcome.** A march by a seat whose row names `dispatch`. None of the four marchers' rows
  does (`off_guild_comptroller`, `off_lord_treasurer`, `off_legal_advisor_hm`, `off_skald_chief`).
- **Touches.** R-04, R-06 (a post means nothing if every post can march).
- **Narrative consequence.** War is waged by whoever's ranking happens to pick it. A marshal is not
  distinguishable from a treasurer by what he may do.
- **Minimal fix.** Proposal `06_FA_remit_grant_by_row.md`: delete `remit_unruled`; each row names `dispatch`
  or does not (the `foreign_seats` rows already do); author a row for NPC-084's seat. J-8 asked whether
  `dispatch` is a remit act at all; this keeps it one and answers only which seats hold it.

### F-FA-04 · degrades narrative · war has no producer and draws no response

- **Claim.** No verb declares a war, no computed act makes `at_war` true, and marches are answered by
  nobody.
- **Evidence and falsifier.** `declare` is not among the 67 rows (E-2). `at_war` over every faction pair at
  the end of every probe run: empty (E-4, E-5). Realm seed 0, three seasons: 29 `march.declared`, 3
  `army.arrived`, 3 `field.unopposed`, 1 `field.lost`, and 0 later acts by other persons citing any of them;
  seed 1: 12, 5, 5, 1, and 1 such act; seed 2: 13, 6, 6, 3, and 8 (E-5). No `field.won` in any run; every
  arrival was unopposed.
- **Touches.** R-04, R-01 (a march that propagates to nobody), R-05 (`declare`).
- **Narrative consequence.** Armies move through a realm that does not notice. There is no war to join, end
  or avenge.
- **Minimal fix.** Already owned: CP-T09-02 (`declare`), CP-T09-03 (alliance and peace), CR-91 (the claim a
  march needs). One edit this audit adds to CP-T09-02's exit: its teeth are counted on a *response* (a later
  act by a person of the target's faction citing the declaration or the arrival), not only on an arrival.

### F-FA-05 · degrades narrative · an officer's choices do not read his office

- **Claim.** A seat-holder's ranking of seat-gated verbs is scored exactly as a private person's.
- **Evidence.** `grep -n -i "faction\|office\|duty" engine/season/decision/choose.py` returns only the two
  `seat_of` calls that stamp `via` (E-9). Organization goals exist (`goals.yaml`, 493 lines;
  `data/goals.py`) and reach a deliberation as a `need` question of class `org goal` in 2 of 774
  deliberations (E-3). CR-88's entry states the same diagnosis.
- **Falsifier and outcome.** A term in the chooser's score that reads the actor's seat or its faction's
  expected pursuits. Absent in `decision/choose.py`; `goals.expected` is read by `world_q.opinion_of` and the
  goal scorer in `world_q.py` (`:3062`, `:3944-3959`), which reach choice only through a question that is
  rarely the one answered.
- **Touches.** R-06, R-04.
- **Narrative consequence.** Kings and copyists differ in what they may attempt, not in what they want from
  their station. Duty, betrayal and the vacancy a lord ought to fill have no weight.
- **Minimal fix.** CR-88 (B10-17b) owns duty. Nothing is added here beyond the defiance and vacancy
  occasions in the two proposals above, which give an office-holder something specific to his office to
  decide about.

### F-FA-06 · degrades narrative · orders and sittings are announcements

- **Claim.** `dispatch` writes nothing ("it names a person; their own choose decides",
  `effects_governance.py:28-30`); `convene` puts a date on the calendar and summons nobody (H-297).
- **Evidence and falsifier.** A later act by the person ordered that the order's content constrains; a
  determination at a convened sitting. Realm seed 0: 14 `order.given`, 91 later acts by others citing one,
  led by `create_record`, `challenge`, `lie`, `utter`, `tell`; 17 `date.scheduled`, 12 `date.fired`, 0
  `matter.determined`. Seed 1: one `matter.determined` (E-5).
- **Touches.** R-04, R-02. Primary owner of the sitting half is SC (H-163, H-279); cross-listed.
- **Minimal fix.** CP-T09-08 (`dispatch` sends an obligee to a place) as planned; for sittings, SC's
  proposals. Not re-decided here.

### F-FA-07 · blocks "playable alone" · there is no FA scenario, digest or end condition

- **Claim.** Nothing lets a player, or a headless proxy, enter a governance situation, see the choices a seat
  opens, and see what a choice did.
- **Evidence.** `harness/governance_spine.py:249-251` prints a census. **On the spine no seat can be filled,
  stripped or claimed at all:** `build` constructs every office with no conferral and no revocation basis
  (`:155-156`), so all thirteen read `(conferral None, revocation None)` and `may_fill` is false for a Duke
  over the Count beneath him (E-10). The fixture built to observe a decision travelling down a ladder
  cannot observe an appointment. `governance_spine.yaml:96-110` still says the two bases have "no
  code-readable owner yet"; `rosters.yaml` has owned both since `13d-i`. `harness/play_surface.py` supplies
  the dispatch seam and no scenario. No instrument prints per season who holds what, which writs stand
  unanswered, or who is banned. `world_q.endings_reached` exists (`:2619`) and no governance run reads it as
  an end.
- **Minimal fix.** Proposal `06_FA_playable_scenario.md`; §9.

### F-FA-08 · degrades (completeness at the extremes) · two hand-built inputs end the season instead of refusing

- **Claim.** A malformed `term` on a `confer` raises `InstrumentDefect` out of the fold
  (`effects_governance.py:50-54`; H-290); two live holders on one office turn a refusal into an uncaught
  `NotYours` (H-133).
- **Why it matters now.** Both are unreachable from a computed act. A player seat is not a computed act:
  `play_surface.py` states it does not validate what a callback returns beyond DELIBERATE's own checks, so
  the first is reachable the day a client offers a term. [UNVERIFIED: whether DELIBERATE's checks refuse a
  malformed payload key before the fold; not traced.]
- **Minimal fix.** `_req_confer` asks the term's shape and refuses (in `06_FA_seat_terms_and_turnover.md`).
  H-133 stays registered: nothing produces two live holders, and a guard on an unproduced state is
  unverifiable.

### F-FA-09 · hygiene · the contract file describes a faction the code retired

- **Claim.** `references/module_contracts.yaml` carries `faction_state` (`:127`, state "faction stats 1-7"),
  `faction_politics` (`:797`, "Standing", "Coup posture") and their neighbours, in the retired Key-registry
  vocabulary, each with `doc:` pointing into `.designs/`. No code under `engine/season/` or `modules/`
  implements them; `tools/build_engine_atlas.py:179` names the two. The live FA contract (a view, acts
  through seats) is in no contract row and no composition role.
- **Resolution.** §6.2 row R-09.

### F-FA-10 · hygiene · unreached query surface in `faction_q`

- **Claim.** `superiors` and the standalone `holdings` have no caller outside tests; `purview` and
  `subordinates` are called only by `harness/interactions.py:123-127`; `head`'s `Tenure.degree` branch has no
  writer (the module's own docstring says so).
- **Evidence.** `grep -rn "\.superiors(\|\.subordinates(\|faction_q\.holdings(\|\.purview(" engine/season
  --include=*.py` less tests: the two harness lines (E-9).
- **Resolution.** §6.2 row R-10.

### F-FA-11 · hygiene · two names say the opposite of what the thing does

`dispensation` names an order by the word for an exemption (H-262); the verb `oblige` binds only the actor
(H-298). Resolution in §6.2 rows R-11 and R-12.

### F-FA-12 · hygiene · two register rows describe a tree that no longer exists

H-230 says IN-61 is unbuilt and no claim names a vacated seat; H-206 says the office half of a death is
unbuilt. `_eff_succeed`, `successions` and `death_subjects` are in the tree. §6.1.

## 4. Code matters

**Ownership and duplication.** Good. The seat-authority rules live once in `state/gate.py` and are imported
by name. `_closing` is shared by `release` and `revoke`. `office_named_by` and `office_founded_by` are each
read by a precondition and its effect. One duplication survives by design and is declared:
`faction_q.purview` is the set form of `purview_reaches` and misses the oath clause (its docstring says so;
CR-09 routes `own_purview`, not this). `revoke` does not use `office_named_by` and reads `payload['office']`
alone (`predicates.py:209-213`), so a computed `revoke` is refused at its first clause by construction; that
is the ruled state, and it means the row forms candidates that can only be refused (5 persons, E-3).

**Dead or unreached code.** F-FA-10. Also `arrangements.yaml`'s `appeal_basis`, `disposal_reach`,
`records_dissent` and `venue_min_rank` are validated and read by nothing (H-281; SC's file,
`05_SC_arrangement_rows_that_bind.md` in the sibling lane addresses it).

**Contract and seam fidelity.** FA has no seam to be faithful to. Against
`architecture/meta/04_CODE_ARCHITECTURE.md`: §B.6.1's view (`:308`), `at_war` as a Query (`:460`), PART D
rows 1, 47 and 48 are met. `at_war` is defined in `world_q` and re-exported (`faction_q.py:76`) to avoid an
import cycle, and says so. One non-conformance is recorded in the tree and not FA's to resolve: a dead
person's edges are deleted with him against `04:360`'s never-deletion (H-206's cite), which is why a
finished world under-reports obligees and holders (`obligee_report.py:24-29`).

**Determinism.** Tenure ids are `H(world_seed, tick, actor, salt)`; `_eff_oblige` salts on the act id to
avoid a same-tick collision. `aperture`'s control arm reproduced the measured arm's hash (E-3). One residue
is registered: a same-`to` re-conferral through two seats in one tick could mint a duplicate hold id (H-207's
cite, unreached).

**Test strength.** Sampled by test name and by grep, not read in full (`test_governance_build.py` is 3,119
lines; §12 lists what was sampled). The governance tests are mutation-minded: the IN-31, IN-53 and IN-61
files carry planted failures and controls, and the import checks are exercised by monkeypatching the
mappings. The weakness is uniform and declared by the tests themselves: every assertion about `confer`,
`revoke`, `succeed`, `determine`'s disposal, a term and a ban is on a **hand-built act**. `test_in31`'s exit
on the built realm places the King's holdings by hand. So the suite proves the mechanisms resolve and cannot
observe that play never reaches them, which is F-FA-02. No test should be added to assert a realm count
(rule V2 in `obligee_report.py`); the instruments are the right place, and the scenario of §9 is the missing
execution artifact.

**Performance.** `purview_reaches` collects swearers once per call and walks `w.tenures`; it is asked on
every purview precondition. Not measured here. `aperture 2 0` ran in 1 m 56 s wall on a contended machine.

## 5. Design matters

### 5.1 Where intent, ruling and code agree

Ruled items accepted as binding and found implemented: a faction does not act; membership is `commit`;
authority is asked of the seat exercised (ED-IN-0256 (4)); conferral bases `appointed · elected · annex` and
`inheritance` (ED-IN-0256 (2), IN-61); revocation by `rung_above_same_faction` or `rung_above_in_holdings`,
`null` for the seven Church and Löwenritter seats (Jordan, 2026-10-11 and 2026-10-12); an appointed seat
revoked costs a permanent ban (2026-10-21); a computed `revoke` is not driven by a special case (H-207 (A));
`question_aggregation_rule` stays `first`; the writ-to-addressee mint is refused (ED-IN-0292 (1)); vassalage
is derived from an oath, never a stored parent (IN-40).

### 5.2 Where they disagree, and what it costs

| disagreement | which the game follows | cost |
|---|---|---|
| Part E's `comply` cell asks for a claim of the writ's terms in the actor's own ledger; the built formation asks him to hold the paper (`writs_held`) | the code | no addressee is ever offered `comply` (F-FA-01) |
| canon: an elected seat is filled by its electors; code: all three bases fill by a plain `confer` (H-292, `gate.py:697-698`) | the code | an election is an appointment; CR-35 owns the change |
| case NPC-032: the queen consort has no action economy of her own; `offices.yaml: off_widow_regent` grants her the King's full remit while he lives | the code | the built realm contradicts the character it is meant to simulate (§13) |
| H-21: a faction's treasury is matter at the rung or office that holds it; code: one pot per rung (H-352) | the code | two factions seated on one rung spend one purse; unreached in play today |
| 04 §B.6.1 and §F.34: the head resolves from `Tenure.degree`; code: `head_seat` data (CR-86) with the degree branch kept first and unreachable | the code | none in play; a reader of 04 expects a derivation nothing writes |
| ruled intent (D5, D6 and E11, ED-IN-0046 and ED-IN-0047; `.designs/…/governance_consolidation_v1.md` §6, `governance_play_redesign_v1.md` §1.4): a Directive is answered by Comply, Bargain or Defy; a Defy adds to a suspicion signal, capped one a season, reduced by sustained compliance, and at a threshold the superior recalls, audits or replaces. Code: the answers write nothing; no suspicion; no recall | the code | the one accountability loop Jordan ruled does not exist in the engine (F-FA-01); the proposal builds it as a fold |
| archived design (`faction_succession_split_v30.md` §2, PROVISIONAL): any faction's leader lost opens a contest unless a sole heir stands well; near-peer claimants split the realm. Code: one `successions` row (the throne); the first valid claim wins; nothing splits | the code | NPC-052 and NPC-081 cannot occur; CR-35 owns the contest, nobody owns the split |
| archived design (`faction_politics_v30.md` §1.0a, ED-776): demotion is graded (one rank, several, dismissal with a lasting mark, an appeal). Code: a revocation costs a ban or nothing, and there are no ranks (CR-32 transcribes names and order only) | the code | a fall is binary; R-06 scopes the ban, which is the nearest built thing to a graded fall |
| ruled 2026-07-13 (ED-FA-0001, as quoted in `governance_consolidation_v1.md` §6): four starting factions, the rest emergent. Code: ten roster members, with the Restoration Movement, the Löwenritter and the Guilds seated at build | the code, under the later roster ruling of 2026-09-02 (H-99) | the emergence the earlier ruling asked for has no producer (IN-30 stopped). [UNVERIFIED: ED-FA-0001's last ledger row was not opened] |
| ruled doctrine (ED-SC-0013, `auto_manual_resolution_duality_v1.md`): one engine at two fidelities; a slate of specific events; a budget of scene actions; what the player does not attend resolves through the NPC chooser | the code agrees in shape (`play_surface`, the scene budget) | none; it is the ground for §9's one code path |

### 5.3 The scripting-drift test, applied

*Is faction behaviour generated from persons' acts, or scripted?* Three levels.

- **Code.** Generated. No branch on an entity or outcome (steelman 2). Faction readings are Queries over
  persons' edges.
- **Data.** Rule-as-data, not outcome-as-data: `successions: {off_king: off_heir}` says which title passes
  which seat; `head_seat` says whose holder heads a faction; `offices.yaml` rows say what a seat may do.
  None says what will happen. One content device deserves its name: a faction creed's `subject` is its
  leader (`rosters.yaml: faction_leaders`), so every member's standing question is about the leader. That is
  a seeded occasion, not a scripted outcome.
- **Planned.** CR-89's band triggers are the place the test must be applied when they are built. A row of
  the form "above band B, members of faction F gain a pursuit weight on verbs V" conditions a choice and
  passes. A row that mints an act, or that fires for a named seat because of who sits in it, fails. The
  entry already says "through an existing term" and "no row names a person or seat"; the Church head's
  `declare` at CI ≥ 60 must be an option that becomes scoreable, never an act the clock performs. Jordan's
  rulings (ED-IN-0341, ED-IN-0343 to ED-IN-0345) license the clock and are not re-raised.

The honest reading of today's tree is that faction behaviour is neither scripted nor generated: it is
absent. Persons act; the sum of their acts does not yet amount to anything a faction could be said to do.

### 5.4 NERS readings (definitions `CLAUDE.md` §0.06; E last)

- **The seat-authority model** (seat, remit grant, purview, bases). N: holds top-down (a ruler's reach),
  bottom-up (a hearth head governs by the same ladder), lateral (two seats on one rung), diagonal (oath
  purview across factions); cutting it loses regency, vassalage and every refusal that names a reason. R:
  customizable by data; complete at its extremes except F-FA-08. S: one methodology for every seat-gated
  verb. E, against that: six remit keys buy nineteen verbs, which is legible; the cost is that `dispatch`
  carries all force (F-FA-03). **Survives.**
- **The decree triple as built** (`issue`, then `comply` / `evade / defy` / `construe` writing nothing). N:
  fails from below (the addressee is never offered it) and laterally (no other mechanic reads the outcome).
  R: no strategic choice, since both answers cost nothing. S: does not pause or hand over to anything. **Fails
  the cut as built; what dies is not the verbs but their emptiness** (F-FA-01).
- **`remit_unruled`.** N: removable with no loss to play; it exists to avoid a ruling. E: one line that makes
  identical rows grant differently by build route. **Dies** (F-FA-03).
- **The permanent ban on an appointed seat revoked.** N: it is the only cost a fall carries. R: complete only
  if a ban has a scope; today any seat is barred `[ASSUMPTION]` and existing seats are untouched (H-294).
  **Survives; its scope is decided in §6.2 R-06.**
- **`faction_q`'s six-member surface.** E fails for `superiors` and standalone `holdings`: overhead no
  caller pays for. **Two members die** (F-FA-10).

### 5.5 Design that exists only as prose

War and peace as acts (CP-T09-02, -03); the casus belli (CR-91); the clocks (CR-89); duty of office
(CR-88); election, nomination, deposition (CR-35 to CR-37); delegation without a hold (IN-48, built and
reverted against Layer 1); the trade demand (FA-01's clause); every row of FA-03 and FA-07 (held,
reference). None is game.

## 6. Hole-register and workplan disposition, and resolutions

### 6.1 Disposition

| item | listed | verified | evidence | action |
|---|---|---|---|---|
| H-21 | ruled, open? | closed (answered by design document) | treasury is `Rung.stores` at the seat's rung, `effects_governance.py:538-544` | none; H-352 carries the residue |
| H-41 | closed? | closed | `_eff_establish`; `office.established` 1 at realm seed 0 (E-5) | none |
| H-70 | assumption | open as a swept fixture | `decision/budget.py` (not re-measured) | none; CHAR's |
| H-90 | ruled | open in part | ladder and purview built; Parliament and delegation unbuilt | CR-35 to CR-37, IN-48 |
| H-91 | absent | **closed by precedent** | §6.2 R-05 | re-grade the row at the next FA commit |
| H-108 | absent | half closed | `Act.via` built; delegation without a hold reverted (IN-48) | §11 item 2 bears on it |
| H-133 | measured | open, unreached | no builder makes two live holders | none (F-FA-08) |
| H-144 | measured | **closed** | CR-25 took option (b): `predicates.py:403-410` | re-grade the row |
| H-99 | ruled | closed | `Office` carries `body` and `faction`; `office_faction` refuses | none |
| H-101 | absent | closed for the office scale, by assumption | IN-40's oath clause, `gate.py:422-461` | CR-09 for the set form |
| H-156 | measured | open; CORE's | scene tax; `raze` 14, `capture` 12, `covenant` 10 always refused (E-3) | cross-listed |
| H-158 | assumption | open | no computed act pays upkeep; not re-measured | none here |
| H-161 | assumption | open; SC's | `bench_quorum` 1 | SC |
| H-163 | measured | open; SC's | `matter.determined` 0, 1 and 0 at realm seeds 0, 1 and 2 (E-5) | SC |
| H-206 | absent, closed? | **stale: the office half is built** | `gate.py:1819-1832` names each seat `hold` a death closes | rewrite the row's head (R-13) |
| H-207 | absent, closed? | open as selection | `confer` formed 5, attempted 0 (E-3) | F-FA-02 |
| H-252 | measured | open | `establish` 7 refusals and `release` 15, all `no-read` (E-3) | route the two bare `False`s through `_refuse` (R-14) |
| H-260 | measured | open | F-FA-01 | `06_FA_decree_binds.md` |
| H-262 | measured | open | name | R-11 |
| H-281 | measured | open; SC's | four keys unread | sibling proposal |
| H-290 | measured | open | F-FA-02, F-FA-08 | `06_FA_seat_terms_and_turnover.md` |
| H-292 | measured | open | `FILLED_BY["elected"]` is `{conferral}` | CR-35 |
| H-294 | measured | open | ban bars openings only | R-06 |
| H-297 | measured | open; SC's | `convene` summons nobody | SC |
| H-298 | measured | open | name | R-12 |
| H-352 | measured | open; not shown reached | `requisition.taken` 0, 1 and 6 at realm seeds 0, 1 and 2 (E-5); which rungs received them was not read | R-07 |
| H-100 | ruled | closed | `REVOCATION_DISPOSAL` | none |
| H-217 | measured | open | no `succession` row | CR-35 |
| H-230 | measured | **stale: both limits lifted** | `_eff_succeed`, `successions`, CP-T02-02's seat ids, `death_subjects` | rewrite the row's head (R-13) |
| H-353 | measured | open | an heir who never committed would act for a faction he is not a member of | R-08 |
| CP-T09-01 to -09, CR-09, CR-32, CR-35 to CR-37, FA-01 | BUILD | open, unbuilt | no `declare`, `retain`, `conspire` row (E-2) | as planned; one edit to CP-T09-02's exit (F-FA-04) |
| CP-T09-06 | EDIT (data) | open | `off_duke_valorsmark.conferral` is `null` in `offices.yaml:206` where the card says it replaces `appointed` | the card's "replacing `appointed`" is wrong about the present value; the edit is `null` → `inheritance` |
| CR-54 | DESIGN-FIRST | open | no design file | `06_FA_decree_binds.md` §4 supplies a candidate motive |
| CR-88, CR-89, CR-91 | B10-17b | open | unbuilt | §5.3 states the test CR-89's rows must pass |
| FA-03, FA-07 | HELD · LEAVE | reference | not built, not scheduled | leave |
| `HANDOFF_FA.md` row 3 | open | **irrelevant** | it orders authoring into a quarantined `.designs/` file that v9 schedules none of | delete the row (R-15) |

### 6.2 Resolutions

Each row is decided. "Step" is the rung of the five-step ladder that decided it.

| id | inconsistency, gap or unclear passage | resolution | step | carried by |
|---|---|---|---|---|
| R-01 | A writ reaches no addressee; `comply` requires holding it while Part E's cell requires only a claim of its terms | a public writ's terms reach its addressees as a content claim; `comply`, `evade / defy`, `construe` form on a writ the person's ledger names him an addressee of | 3 (Part E's own cell), then 5 | `06_FA_decree_binds.md`; §11 item 1 |
| R-02 | Obeying and defying change nothing (H-260); the verb table says the consequence waits on a suspicion carrier | the consequence is ruled (D5, D6, E11): suspicion accrues per defied season, falls with compliance, and at a threshold the superior recalls. Built as a person-side fold over the issuer's own claims (`suspicion_of`), never stored, and a recall occasion that carries the subordinate and his seats | 1 (ED-IN-0046, ED-IN-0047; the carrier question superseded by ED-IN-0343 to ED-IN-0345) | `06_FA_decree_binds.md` |
| R-03 | `revoke` has no motive and reads no `subject` (CR-54) | the defied-writ occasion is the general motive; `revoke` reads its office through `office_named_by` and declares `referent_class: Office`, `referent_named: true` | 4 (CR-54's ratified reading of H-207 (A)) | `06_FA_decree_binds.md` |
| R-04 | J-8: which seats hold `dispatch`; `off_npc_084` has no row and every remit act | `dispatch` stays a remit act; a seat holds it only if its row names it; `remit_unruled` is deleted; NPC-084's seat gets a row | 4 (the `foreign_seats` rows; IN-64's precedent) | `06_FA_remit_grant_by_row.md` |
| R-05 | H-91: is `remit:revoke` necessary when purview is sufficient | necessary. Every remit verb is admitted by grant AND basis (`_seat_grants` then the basis, `gate.py:370-375`); the 2026-09-02 purview sentence was superseded by ED-IN-0256 (3) and the 2026-10-12 holdings ruling, which decide the basis and leave the grant to the row. A duke who should revoke is a duke whose row names `revoke`; all three do | 1, then 4 | this table |
| R-06 | H-294 and two `[ASSUMPTION]`s: a ban's scope and reach | scope: the banning seat's purview (the edge's object is that seat; a ban that bars every seat ignores its own object). Reach: openings only. Closing the banned man's existing holds would strip seats `may_revoke` protects, including ruled-`null` ones | 5 | `06_FA_seat_terms_and_turnover.md` edit 6 |
| R-07 | H-352: one purse per rung | keep one store carrier (`Rung.stores`); a seat may name a `treasury:` anchor on its `offices.yaml` row, default its own rung; built only once a computed `requisition` lands on a rung seating two factions | 5 | this table (shape only; no proposal until reached) |
| R-08 | H-353: a seat's faction and a holder's membership are two records | leave them two. A holder outside the faction is staff, which `world_q.leaders` already says; `_eff_succeed` and `_eff_confer` mint no `commit`, because membership is the person's own act (AX-1) | 3 (`leaders`' own docstring), 4 | this table |
| R-09 | F-FA-09: contract rows for a retired faction | delete `faction_state` and `faction_politics` rows' `state:`, `emits`/`consumes` and Key-vocabulary fields in the commit that re-points `tools/build_engine_atlas.py:179`; keep one line per name saying the faction is `queries/faction_q.py`'s view and has no contract. [UNVERIFIED: the full reader set of the `modules:` list; `manifest/registry.py:55-58` parses it] | 2 (the subject was retired at `29b`; Key substrate by ED-IN-0232) | `06_FA_hygiene.md` |
| R-10 | F-FA-10: unreached `faction_q` members | delete `superiors` and the standalone `holdings`; keep `purview` and `subordinates` (the interaction instrument reads them); keep `head`'s degree branch, which Layer 1 names, and say at the site that it is unreachable | 5 (ID-13) | `06_FA_hygiene.md` |
| R-11 | H-262: `dispensation` | rename the Record kind and Event kind to `writ` and `writ.issued`, the word the code already uses (`writs_held`, "writ" in every note); a declared hash mover | 4 (`refract` → `construe`, `levy` → `requisition`) | `06_FA_hygiene.md` |
| R-12 | H-298: the verb `oblige` binds the actor | rename the VERB to `swear` (the code's own word: `sworn_to`); the Tenure kind stays `oblige`, which Layer 1 names | 4 | `06_FA_hygiene.md` |
| R-13 | H-206 and H-230 are stale | prepend each row with what landed and where; keep the measured history | 1 | `06_FA_hygiene.md` |
| R-14 | H-252: which clause refused a `confer` or an `establish` | each `return False` in `_req_confer` and `_req_establish` becomes `return _refuse("<clause>", ids)`, the trace-only helper `_req_release` already uses; no hash moves | 4 (`_req_release`, `_req_revoke`) | `06_FA_hygiene.md` |
| R-15 | `HANDOFF_FA.md` row 3 | delete; ED-FA-0021 stays ratified as intent | 2 | `06_FA_hygiene.md` |
| R-16 | the queen consort holds the King's remit | `off_widow_regent.remit_acts: []` while the King lives; a regency is a termed `confer` or the heir's claim | 3 (case NPC-032; the registry post "Widow Regent if Almud eliminated") | `06_FA_remit_grant_by_row.md` |
| R-17 | no computed act declares a seat's term; a malformed term raises | the term is the seat's, on its row; `_eff_confer` reads the act's term, else the row's; `_req_confer` refuses a malformed one | 5 | `06_FA_seat_terms_and_turnover.md` |
| R-18 | CP-T09-06's card misstates the present value | the edit is `null` → `inheritance` | 3 (the file) | this table |
| R-19 | no FA scenario, digest or end | one harness entry on the spine through `play_surface`; a per-season governance digest; three end conditions | 5 | `06_FA_playable_scenario.md` |
| R-20 | "registered module" against a subsystem that Layer 1 rules has no verbs | not resolved here, by the brief's instruction | none | §11 item 2 |
| R-21 | Church and Löwenritter seats are strippable by nobody, and three provided characters must be removable | not resolved here: it would overwrite a ruling | none | §11 item 3 |

Twenty-one rows; nineteen decided, two named and left.

## 7. Research transfer

Read: `research/00_INDEX.md` (outline), `research/by_lane/README.md` (full), `by_lane/FA_faction_actions.md`
§0, §1.2, §2.2, §2.3 in full and §7, §8, §10 by row head, `game_precedent_suite/dispositions/D_T09.md` rows
1 to 20, and targeted searches of `research/governance/`, `fa_se_historical_precedent_research_v1.md` and
`proactive_governance_scale_research_v1.md`. Not read in full: see §12. The FA lane file is dated
2026-10-16 and is stale where the tree moved (it says `head()` is always `None` and `covenant` is unbuilt;
both changed).

**Changes what to build.**

- *A faction's act is a person's act* (T-FA-1: Layer 1, Old World's ruler goals, the ruler and officer seats
  of the RTK line). Convergent and already the architecture. It argues against answering the standing
  requirement with a faction module that acts (§11 item 2).
- *A mechanism engineered not to fire is indistinguishable from one that does not exist* (EU4's estates
  loyalty floor; T-FA-5). This is the lane's most transferable finding and it describes F-FA-01 and F-FA-02
  exactly. It sets the gate for every proposal here: an execution count in a seeded run, never a hand-built
  pass.
- *Removal is graded by how the seat was won and leaves a residual* (T-FA-3; Ottoman, Florentine, Han and
  Tokugawa demotion ladders). Built as `REVOCATION_DISPOSAL`. The research's own counter-case (Liang Ji)
  means the generalization is a shape, not a rule; it supports R-06's choice that a ban is scoped rather
  than total.
- *Fixed terms and re-legitimation at each succession* (the Golden Bull's electors; Venice's oath at entry
  and audit at exit). Transfers as shape only, and it is the precedent for R-17: an office that falls vacant
  on a clock is the cheapest generator of politics the corpus shows. No number transfers.
- *Capitularies read aloud by the count and the missi* (`governance_modes.md` §1.4 to §1.5). A decree was
  public by proclamation and its enforcement was a second, inspecting act. That is the shape of R-01 (terms
  public to those the decree reaches) and R-02 (defiance noticed by the issuer, acted on separately).
- *The appointed governor* (D1 null, narrowed by `13G`: the delegate recurs and is the defection vector; its
  bookkeeping is the trap). Supports leaving IN-48 held until a delegate has something to defect with.
- *Empires in Arms' political phase* (declarations, calls to allies, peace as dated steps). The nearest
  analogue for CP-T09-02 and -03; single title; shape only.

**Decorative, or tried and not transferred.**

- Fiscal stance, muster financing, tax farming (`fa_se`): plausible, unverified, phrased as faction stats
  the code refuses. Nothing to take until `requisition` executes.
- Victoria 3's law enactment and CK3's vassal contracts: no law object and no upward tax in this tree
  (D_T09 row 2 records the inversion: upkeep flows down).
- Skyrim guild ladders, the 75% consolidation threshold, the 90% treaty lapse: unsourced numbers.
- The `power_base` typology (rise-to-power): built once as a roster and deleted unread; do not rebuild.
- CK2's priced truce breach: the one case in hand for K-FA-2; it waits on a covenant that something reads.

**From `.designs/` and `.audit/` (referents, never authority).**

- The Directive and its three answers, the suspicion signal and the recall are the archived settlement
  design's (`.designs/systems/settlements/reference/governance_play_redesign_v1.md` §1.4), consolidated and
  ruled in `.designs/systems/_architecture/reference/governance_consolidation_v1.md` §6. This is the referent
  behind `comply`, `evade / defy` and case NPC-083, and it changed this audit's resolution R-02 from "no
  counter" to "the ruled accrual, as a fold".
- `.audit/2026-07-12-governance-compendium/43_directive_types.md` lists a typed Directive enum (Extract,
  Tax, Suppress, Install, Host, Cede) and proposes five more. In code a writ's `terms` name whatever its
  issuer's question named; which acts a writ may order is H-44's and stays open. Lead, not finding.
- The same consolidation records two old findings that are now **false or moot**: that legitimacy and
  popular support are "declared-but-inert in `sim/`" (that tree is dissolved; in the season loop
  `person_q.legitimacy` is a Query over claims), and that the governance engine is "biased toward negative
  death-spirals" (measured on a card deck and a predicate sweep the season loop does not contain). Neither
  is repeated here.
- Its method note is worth keeping: two harnesses with two jobs, one for whether a season plays and one for
  whether the distribution is healthy. §9's scenario is the first; `aperture` and `strife` are the second.
- The archived faction design is a statistics-bearing faction (Wealth, Military, Influence, Stability,
  Mandate; a Standing matrix; eight casus-belli sources; a 90 to 95 per cent treaty lapse per arc;
  `faction_systems_overview_v30.md` §2 to §4). Layer 1 refused the stored aggregate, so none of it is a
  specification. It remains the vocabulary FA-07 holds and the source of CR-91's grounds (four, against the
  design's eight).

**Nulls.**

- **No source in the corpus treats formal obedience without execution** (a search of `research/` for the
  Castilian formula returns nothing; Levi's quasi-voluntary compliance is the nearest, at theory level). The
  comply / defy / construe triple therefore rests on Jordan's rulings and Part E, not on precedent.
- **No surveyed game models a belief in transit** (T-FA-9, one research line). Valoria already sits in that
  cell, which is why the chronicle channel's broadcast to everyone alive is a regression against the game's
  own distinguishing property; CR-29 owns it.
- **No source grounds a sole territorial victory** (T-FA-4). Not FA's to decide; it bears on the end
  condition in §9, which is why that proposal ends a scenario on holds and seasons, not on conquest.
- **Treaty enforcement beyond reputation has no game case.**

## 8. Best path forward

In order. Steps 1 to 4 make FA run well alone; 5 to 8 make it compose.

| # | change | file (owner) | gate (execution artifact) | unblocks | cost |
|---|---|---|---|---|---|
| 1 | Grants by row: delete `remit_unruled`; rows name `dispatch`; a row for NPC-084's seat; the consort's remit emptied | `engine/season/offices.yaml`; `data/rosters.py` (`OFFICES_REMIT_UNRULED` goes); `harness/populated.py::authored_remit` | `aperture 2 0` PER HOLDER: every `march` attempt is by a seat whose row names `dispatch`; `p_npc_084` no longer reads 67 of 67 | R-04, R-06 | edit (declared hash mover) |
| 2 | A decree's terms reach its addressees; the triple forms on an addressed writ; the defied-writ occasion; `revoke` reads `subject` | `loop/witness.py` (content deposit), `queries/world_q.py` (`writs_held` → `writs_addressed`; the occasion), `verb_table.yaml` (`revoke`), `loop/predicates.py`, `loop/effects_governance.py` | spine, seeds 0 to 4, four seasons: at least one `compliance.given` and one `compliance.withheld` by an addressee; after a withheld one the issuer's next question set carries the defier's seat as an `Office` referent; control arm (the deposit off) reproduces today's hash | R-04, R-02, R-05 (`comply`, `evade / defy`, `construe`, `revoke`) | small build |
| 3 | Seat terms as data; malformed term refuses | `offices.yaml` (`term:`), `data/rosters.py` loader, `loop/effects_governance.py::_eff_confer`, `loop/predicates.py::_req_confer` | realm, seeds 0 to 2, twelve seasons, once the elected rows are termed: `term.matured` on a seat `hold` at least once per seed, and the count of `tenure.opened` on a matured seat read and reported; `term: null` everywhere reproduces the pre-item hash | R-04, R-05 (`confer`) | small build |
| 4 | The scenario, the digest and the end conditions | `harness/governance_spine.py` (`play`), reading `harness/play_surface.py` | a scripted-callback run ends on each of the three conditions; a run with the auto chooser prints a non-empty digest; no engine file changes and `content_hash` is unmoved by the digest | the standing requirement | small build |
| 5 | B10-17 close one as planned (`declare`, alliance and peace, occupation), with CP-T09-02's exit counted on a response | plan | `aperture` and `strife` as the card states, plus one later act by a target-faction person citing the declaration | R-04, R-01, R-05 | as planned |
| 6 | B10-17 close two (`ladders`, election, nomination, deposition), CP-T09-06's data edit | plan | as the cards state; the election's computed reach stays H-80's | R-04 | as planned |
| 7 | B10-17b (claims, clocks, duty), with §5.3's test applied to each trigger row | plan | CR-90's reading, on against off | R-04, R-06, R-02 | design-first |
| 8 | Hygiene: stale rows, dead members, the two names, the contract rows | as R-09 to R-15 (`06_FA_hygiene.md`) | `register --check`; the two renames are declared movers | none of THE NINE | edit |
| 9 | Vocations for `determine`, `interrogate`, `arrest`; a seat's optional `vocation:`; the conferee ranked; founding content as data (`06_FA_office_capabilities.md`) | `rosters.yaml` (`verb_capability`, `vocation_attribute`), `offices.yaml`, `decision/choose.py`, `loop/predicates.py` | EQUAL at ship; two judges of unequal `judgment` differ over 200 seeds, with an equal-holding control | R-09, R-06 | small build |

Step 1 comes first because every later reading of the military verbs is otherwise taken on a placeholder.
Step 2 before 3: a term that empties a seat is only interesting once the seat's holder had orders to obey.

## 9. Playable standalone and integrated

**The requirement.** Each subsystem plays alone, conforms to Layer 1, and integrates with the loop.

**What exists.**

| element | state |
|---|---|
| entry point | none that plays. `python -m engine.season.harness.governance_spine` prints a census |
| fixture | `governance_spine.build(seed)`: 13 seats, 13 persons, two chains under one realm, every seat holding the full default remit and **no conferral or revocation basis** (E-10), one faction with no members (`faction x`; its `members` is empty, E-4) |
| choice surface | exists in mechanism: `harness/play_surface.py::dispatching_chooser` hands a named person's deliberation to a callback with the same `(p, v, s, ask_budget)` the chooser sees; `opening_set` computes the offered candidates. Nothing presents them |
| outcome legibility | none. Refusals are Events with a kind; three predicate rows record no reason (H-252). No digest says who holds what |
| stakes | a seat can be lost only by death or a hand-built `revoke`; a decree costs nothing to ignore; a treasury is rarely touched |
| end condition | none read. `world_q.endings_reached` exists |
| instrument | `aperture` (funnel), `interactions` (who did what to whom), `obligee_report`, `heir_hears` |

**What is missing, point by point.**

1. *A scenario seed.* The spine is a shape with no situation: no vacancy, no order outstanding, no rival
   claim. `06_FA_playable_scenario.md` adds three situations as data on the existing builder's output, each
   made by the game's own effects at tick 0 (a vacant seat under the player's purview; a writ addressed to
   the player; an oath the player's vassal may release), never by a branch on an id.
2. *A choice surface.* The callback prints the seat-gated candidates grouped by remit act, with the refusal
   clause where the last attempt was refused. This is presentation in the harness; it reads only what
   `choose` is handed (AX-2).
3. *Legible outcomes.* A per-season digest read off `w.log` and `w.tenures`: seats opened and closed and by
   whom, writs issued and answered, bans, oaths taken and released, stores moved by requisition.
4. *Stakes.* Arrive with steps 2 and 3 of §8: an order that can be defied and noticed, and a seat that ends.
5. *An end condition.* Three, each a Query: the player holds no seat; the scenario's season count is
   reached; `endings_reached` is non-empty.

**One code path.** By construction, and by ruled doctrine (ED-SC-0013: one engine at two fidelities, a
slate of specific events, a budget of scene actions, the unattended resolved by the NPC chooser): FA's
standalone game is the season loop on a small world with one person's choices supplied by a callback. No FA code exists outside the loop, so no fork can arise. The risk
is the opposite: harness situation-building must go through effects and the gate, or the scenario plays a
world the loop cannot produce.

**Layer 1 as a registered module.** FA is not one and, read against PART D rows 1 and 47, cannot hold verbs
or state as one. The standing requirement and the ruling conflict; §11 item 2 names the conflict and the two
readings and does not choose.

**Integration.** FA's edges to the loop are the loop's own writes. Zoom in: a `march` hands to
`modules/mass_battle` through its composition role, a `determine` or `arrest` to `modules/social_contest`,
`capture` to `modules/combat`; those edges execute (E-3: `field.unopposed`, contested `determine`). Zoom
out: nothing a battle or a hearing decides is read back by a governance verb as a reason (no claim on a
ground from a won field until CR-91; no seat opened by a determination until CR-35).

**Ordered work.** §8 steps 1 to 4.

## 10. Interfaces

| with | FA consumes | FA emits | real or designed |
|---|---|---|---|
| CORE (loop, gate, witness) | `Act.via`, the write gate's bases, WITNESS's channels, `questions_for`'s occasions (`vacancies`, `writs_held`, `sittings_before`) | Tenure edges, Office rows, dates, `tenure.*`, `office.established`, `order.given`, `dispensation.issued` | real (E-3). The chronicle channel broadcasts every binding decision to everyone alive, which is CORE's to replace (CR-29) |
| CHAR | pursuits, stance, regard, `legitimacy` (`person_q.py:537`), organization goals as OUGHT Propositions | seat grants that widen `opening_set`; the office bonus in the scene budget (H-70) | real for the grant and the budget; `legitimacy` and `goals.expected` reach a choice in 2 of 774 deliberations (E-3) |
| SC | `determine`'s contest, arrangements, the docket | `convene`'s dates, `open_case`, the disposal Tenures (`oblige`, `ban`, `detain`), `pardon` | real for `convene`, `open_case` and one `matter.determined` in nine realm seasons over three seeds; the disposal `hold` (election) is designed |
| MB | a resolved field | `march` through `remit:dispatch`; the mustered set from `commit` members | real: 29 and 12 `march.declared`, fields unopposed (E-5) |
| PC | `capture`, `arrest`'s contest | the warrant an `arrest` reads | `capture` 0 of 12 and `arrest` 0 attempted (E-3): designed in play |
| SE | `Rung.stores`, rungs, sites | `requisition` (`requisition.taken` 0, 1 and 6 at seeds 0, 1 and 2), `establish`, `seize`'s rung half, upkeep through `transfer` | real, and seed-dependent; `rung.seized` 0 at every seed |
| WR | canon names through `names_index.yaml`, the cast | the foreign faction's two seats | real at build; the trade demand is unbuilt (FA-01) |
| FI | findings as claims | `survey`'s faction sheet (17 `faction.surveyed` at seed 0; one later act by another person cites one) | real, inert downstream |
| DICE | the contest seam's roll for `determine`, `arrest`, `interrogate` | nothing | real; every pool rolled was 2 (E-3), §14 |

## 11. Survivors for Jordan

Three. Each survived the five steps.

**1. Is a decree public, or is it paper?** ED-IN-0292 (1) refused minting a writ into its addressee's hand
("just say no for now"), and the built formation then required the addressee to hold it, so none is ever
answered. Two defensible games:

- *(A) Proclaimed.* The terms of an `issue`d writ are public to whoever learns it was issued, and an
  addressee may answer it without holding the paper. Authority is legible and cheap; defiance is public; a
  decree cannot be lost, intercepted or forged in transit. This is `06_FA_decree_binds.md` as written, and
  it mints no hold, so it does not undo the ruling's text.
- *(B) Delivered.* Only a held writ binds; the issuer or a messenger must `give` it. Orders become
  logistics: they can miss, be stolen, be forged, arrive late. Richer and much costlier: it needs a delivery
  occasion and a `give` that executes at range (one execution in two realm seasons today).

The proposal takes (A) for `issue` and keeps (B)'s shape for `covenant`, whose note already says it "must
not be read as a public writ". If Jordan's "no" meant that an addressee should not learn a writ's terms
unheld, (A) is wrong and the fix is a delivery occasion.

**2. The standing requirement against Layer 1, for FA.** "Every subsystem must be … a registered module
(typed input, typed outcome, no held state, reached by composition row)" and PART D rows 1 and 47 ("an
institution acts" is refused; a faction field that outlives a barrier is refused), with ED-IN-0283's
"factions … in_loop: False … THIS SCALE HAS NO CODE OF ITS OWN". Named, not resolved:

- *(A) FA is the loop's own verbs.* Its standalone game is a scenario over the season loop (§9). One code
  path by identity; no module; the requirement is read as met by the scenario.
- *(B) A `modules/governance` of pure functions* (the authority predicates, the succession and election
  tallies) reached by composition rows. It would put the write gate's own rules behind a string-resolved
  role, which `04` does not describe, and gives a second home to rules that today live once in
  `state/gate.py`.

The games do not differ; the architectures do. It is listed because the two instructions are both Jordan's.

**3. Church and Löwenritter seats that nobody can strip.** Ruled `null` on 2026-10-11 for seven seats
because no same-faction seat stands on their parent rung. Provided cases NPC-038 (the Cardinal of Justice
removed on exposure, `core`), NPC-004 and NPC-070 need those seats removable by something other than death.

- *(A) Keep `null`.* An institution's officers leave only by death, resignation or a bench's ban (which bars
  new seats and does not unseat). The Church is unpurgeable from inside; those arcs end by violence or not
  at all.
- *(B) A third revocation basis, `head_of_faction`*: the holder of the faction's `head_seat` may strip a seat
  of that faction. The Confessor disciplines Cardinals; a general rule over existing data. The Church becomes
  an institution with internal politics, and the Löwenritter stay unstrippable until a head seat is authored
  for them.

## 12. Evidence log

All with `PYTHONHASHSEED=0`, at `601e715`, outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/FA/`. The machine was
shared with the other lanes (load average near 30), so long runs were kept few.

| id | command | seed · seasons | outcome |
|---|---|---|---|
| E-1 | `python -m engine.season.harness.governance_spine` | 0 · none | census: 13 offices, 13 persons, 13 held, 13 seated, 13 granted, 26 rungs, place depth 6 (`governance_spine.txt`) |
| E-2 | a `python -` probe over `VERB_TABLE`, `resolvable_verbs()`, `REQUIRES_PREDICATES`, `REMIT_ACTS` | n/a | 67 rows, 66 resolvable, six remit acts; eligibility, emits and writes of the governance rows; no `declare` row |
| E-3 | `python -m engine.season.harness.aperture 2 0` | 0 · 2 | realm 83 persons, 33 seated, acts 1529 = 1529, control hash EQUAL; spine 13 persons, acts 186 = 186, EQUAL; per-holder and per-verb figures as quoted (`aperture_2_0.txt`) |
| E-4 | `fa_probe.py spine 4 0 1 2 3 4` (read-only; in the scratchpad) | 0 to 4 · 4 | 19 writs, 0 held by an addressee, 0 compliance events; no office changed holder; no vacancy; `at_war` empty; hashes `1d424f49b174`, `993400462d45`, `882acd633a5b`, `c64f969d974c`, `07c0454d0507` (`probe_spine_4.txt`) |
| E-5 | `fa_probe.py realm 3 0 1 2` | 0, 1, 2 · 3 | seed 0: 29 writs, 0 held by an addressee; deaths 0; `office.established` 1 (left vacant); faction tuples identical; `at_war` empty; hash `52ff67bc45c5`. Seed 1: 21 writs, 0 held; 1 death (the Cardinal of Prudence; his seat vacant at the end); `matter.determined` 1; `requisition.taken` 1; Church (7, 7, 1) → (6, 6, 1); hash `26d2091b144c`. Seed 2: 41 writs, 0 held; the same death and vacancy; `requisition.taken` 6; `commitment.ended` 1; hash `b95552898d9a` (`probe_realm_3.txt`) |
| E-6 | `python -m engine.season.harness.heir_hears --seeds 0 1 2 --seasons 4` | 0, 1, 2 · 4 | seeds 0 and 1: 20 heir question sets each; throne vacated: none. Seed 2: throne vacated in season 4 with the heir alive; heard by a living heir: yes; vacated but unheard: none. Control 0 at every seed; exit 0 (`heir_hears_4.txt`). The instrument does not read whether the heir then claimed |
| E-7 | `python -m engine.season.harness.corpus_run`, **the CORE lane's run of the same command on the same tree**, read from its scratch output; not re-run here because nine lanes were running it at once | 0 · per case | 143 cases; 23 of 67 verbs executed; `confer`, `convene`, `dispatch`, `establish`, `march`, `oblige`, `open_case`, `pardon`, `requisition`, `revoke`, `seize`, `succeed` among 30 "foldable but never even attempted"; `comply`, `construe`, `covenant`, `determine`, `evade / defy`, `survey` only refused; NPC RUNS and ARC ENDS both NOT-COMPUTABLE |
| E-8 | `run_cases.load_cases` over the corpus, filtered by need text | n/a | 143 cases, 972 needs, 69 marked UNCLEAR; the FA-bearing needs listed in `fa_cases.txt` and grouped in `fa_case_mech.txt` |
| E-9 | `grep` for entity literals in non-harness Python; for `faction\|office\|duty` in `decision/choose.py`; for callers of the `faction_q` members and `at_war` | n/a | entity literals in comments only; `choose.py` reads `seat_of` twice; callers as stated in F-FA-10; `at_war` read at `world_q.py:3703` and `:5150` |

E-10: a `python -` probe on `governance_spine.build(0)`: all thirteen offices read `(conferral None,
revocation None, binds members_by_admission)`; `has_conferral_basis(lo_province_a)` is False and
`may_fill(lp_duchy_a, lo_duchy_a, lo_province_a)` is False.

Stopped and discarded: a second `aperture 4 0` and an `aperture 4 1` of my own (the CORE lane was already
running `4 0`; neither had produced output). Nothing in this audit rests on a four-season `aperture` reading.

**Read in full:** the nine code files of the dossier; `loop/predicates.py`; `state/gate.py:345-470` and
`:617-866`; the 26 primary hole rows and H-100, H-217, H-230, H-353 at their register lines; the B10-17 and
B10-17b cards; the part-4 entries for CR-09, CR-32, CR-35 to CR-37, CR-54, CR-88 to CR-91; `HANDOFF_FA.md`;
`HANDOFF.md`; `AUDIT_BRIEF.md`; both dossiers; `CASE_BRIEF.md`.
**`.designs/`, read end to end, with long lines truncated** (each line cut at 300 to 520 characters, so the
tails of long table cells and paragraphs were not read):
`_architecture/reference/governance_consolidation_v1.md`, `auto_manual_resolution_duality_v1.md`;
`factions/reference/faction_systems_overview_v30.md`, `faction_succession_split_v30.md`,
`faction_politics_v30.md` §1.0 to §1.0d and its index. **Outlined by heading only:** the other twelve
faction documents the dossier lists. **Followed as a referent:** `settlements/reference/
governance_play_redesign_v1.md` §1.4 (by search). **Not read:** `faction_layer_v30` and its parts,
`faction_canon_v30`, `faction_behavior_v30`, `faction_state_authoring_v30`, `factions_personal_v30`,
`ci_political_v30`, `franchise_v30`, `treaty_expiration_v30`, `parliamentary_transfer_v30`,
`baralta_crown_claim_v30`, `fractional_province_ownership_v30`, `political_dynamics_keys_migration_v30`,
`governance_type_registry_v1`, `factions_flow_skeleton_v1`, `fail_forward_pp177`, `varfell_path_b_v30`, the
rest of `faction_politics_v30` (the rank ladders), and fifteen of the seventeen cross-cutting documents. The
instructions to read these arrived after the audit's reading budget was largely spent; the findings above do
not rest on them, and CR-32's ladder transcription and CP-T09-03's treaty work should not be taken as
checked against them here.
**`.audit/`, read:** `2026-07-12-governance-compendium/00_index.md` in full and `43_directive_types.md`
§1.1 to §1.4. **Not read:** the compendium's other eight files and
`2026-07-09-comparative-governance-research/`.
**Sampled, not read in full:** the 22 test files (names and greps); `harness/aperture.py` past its docstring;
`world_q.py` (the functions cited); H-101 past its first forty lines; the governance proposals (Status lines;
IN-48's head; `reasons-to-convene` §0 to §2); the FA research file's §3 to §6, §9; the three
`research/governance/` bodies, `rise_to_power`, `proactive_governance`, the companion parts, `THROUGHLINES.md`
and `00_COMPARATIVE_ANALYSIS.md` (searched, not read).

## 13. Provided arcs and characters — adjudication

**Scope and method.** The corpus is 143 cases and 972 needs, 69 of them marked UNCLEAR by their extractor
(E-8). A need is adjudicated here when the mechanism it turns on is a seat, a faction, an order, a
succession, a removal, an oath or a war. Needs that turn on a clock, a vote, a contest, a settlement's
economy or a person's interior are cross-listed to the lane that owns them. "Represented" means *reached in
a run*, not declared: the evidence column cites E-3 to E-7. In the corpus worlds themselves (E-7) no seat
lifecycle verb is even attempted, and the instrument reports NPC RUNS and ARC ENDS as NOT-COMPUTABLE, so no
case is simulated end to end today in any lane's sense; the table says what stands between each need and a
run.

| case | need (short) | hardness | represented today? | evidence | change required | owner | proposal | gate |
|---|---|---|---|---|---|---|---|---|
| NPC-083 | the authority above issues a seasonal order she may comply with, bargain down or defy; repeated defiance forces a reckoning | core | **no** | 91 writs, none held or answered (E-5); `comply` 0 of 33 (E-3) | terms reach the addressee; the triple forms; a defied writ is the issuer's occasion | FA (CORE for `witness.py`) | `06_FA_decree_binds.md` | spine, seeds 0-4, 4 seasons: ≥1 `compliance.given`, ≥1 `compliance.withheld`, then the defier's seat among the issuer's referents |
| NPC-083 | a limited, renewing per-season budget across a menu of administrative acts | core | **yes** | `decision/budget.py`: base plus one per live `hold`, less wounds and travel; the menu is her seat's grant (E-3 PER HOLDER) | none | CHAR / FA | — | — |
| NPC-083 | each administrative act resolvable by several methods that hand influence to different internal factions | core | no | no method operand on any governance row | a settlement-management design | SE | — | SE's |
| NPC-008 | an office makes changing the governing body harder purely by being held | core | no, and **wrongly stated against the architecture** | `04` §B.7: a seat adds no verb and no modifier | restate: a reform needs a Record only he holds, or his seat's confirmation (CR-36's `resolution`) | SC / FA | — (CR-36) | CR-36's exit |
| NPC-008 | removing him interrupts the function until the office is refilled | important | partly | a vacant seat grants nothing; nothing refills it (F-FA-02) | terms and the vacancy occasion | FA | `06_FA_seat_terms_and_turnover.md` | a `tenure.opened` after a `term.matured` on the same seat |
| NPC-038 | members of his branch may act above a threshold only with his authorization | core | mechanism yes, play no | `arrest` needs a held warrant issued through another seat (`may_warrant`); `arrest` formed 1, attempted 0 (E-3) | none in FA; a warrant must reach its bearer (the same delivery question as R-01) | FA / SC | `06_FA_decree_binds.md` (the content route covers a warrant's addressee) | one computed `arrest.made` |
| NPC-038, NPC-004, NPC-070 | exposure or failure removes the office-holder, with downstream damage | core | **no** | their seats' `revocation` is `null` (ruled) | a ruling | Jordan | — | §11 item 3 |
| NPC-020 | acts taken in the leader's name diverge from his intent, and he learns afterward | core | weakly | an order writes nothing and the ordered person chooses freely; the King learns by claims (91 later acts cite an `order.given`, E-5) | `dispatch` that sends (CP-T09-08); delegation (IN-48) is held against Layer 1 | FA | — (plan) | CP-T09-08's exit |
| NPC-020, NPC-070 | a standing army reassesses its loyalty in stages, up to ceasing to obey | core | carrier yes, behaviour no | the Grand Master's `oblige` to `off_king` (`offices.yaml:196`) extends the Crown's purview; no such oath was released in any run | duty and the betrayal reading | FA / CHAR | — (CR-88) | CR-88's exit; then a seeded `release` of that oath |
| NPC-020, NPC-031 | a designated heir is a real status before succession; the throne passes by claim | important | **mechanism yes; the claim unobserved** | `successions`, `_eff_succeed`; the throne vacated at one seed of three in 4 seasons, and the heir heard it (E-6); `succession.claimed` 0 in every probe run (E-5) | a vacancy early enough to watch the claim | FA | `06_FA_playable_scenario.md` (the succession situation) | the scenario run: `succession.claimed` after the King's seat is released |
| NPC-020, NPC-050, NPC-081 | a succession contested among parties with different bases of claim | core / important | no | the first valid claim wins; no `succession` arrangement row (H-217) | the election and contested-succession arm | FA / SC | — (CR-35) | CR-35's exit; computed reach is H-80's |
| NPC-050 | a campaign toward a higher seat attemptable only when the seat is weak and the realm unstable; a failed attempt costs standing and cannot be repeated for a time | core | no | no claim on a held seat; no Turmoil | claims (CR-91), deposition (CR-37), the clocks (CR-89) | FA | — (plan) | CR-90's reading |
| NPC-052 | his successor undetermined among qualified claimants; the domain may split | core | no | `off_duke_varfell` is `elected` and fills by plain `confer` (H-292) | CR-35 for the election; a split of a rung is unowned | FA; SE / WR for the split | — | CR-35's exit |
| NPC-032 | a consort with standing and no action economy of her own | core | **contradicted** | `off_widow_regent` grants `[issue, determine, confer, revoke, convene]`; she reads `eligible 67 of 67` and executed `convene` and `dispatch` (E-3) | empty her remit while the King lives | FA | `06_FA_remit_grant_by_row.md` | `aperture 2 0`: her seat-gated row reads `-` throughout |
| NPC-003, NPC-041 | a movement leader with influence before any seat; standing acquired by steps | core | partly, and against the case | she is seated at build (`off_restoration_leader`); no emergence | an emerged faction founded by a creed (IN-30, stopped) | FA / WR | — (IN-30, CR-39) | IN-30's exit |
| NPC-036, NPC-072, NPC-082 | a command post materially affects what the faction can do | core | **not distinguishable** | 26 of 33 seats may `march`; the marchers were a treasurer, a legal advisor, a guild representative and a skald (E-3) | grants by row | FA | `06_FA_remit_grant_by_row.md` | every `march` attempt is by a seat whose row names `dispatch` |
| NPC-037, NPC-013 | a treasury post moves the faction's material resources | core | partly | `requisition.taken` 0, 1 and 6 at seeds 0-2 (E-5); one purse per rung (H-352) | R-07 when reached | FA / SE | — | — |
| NPC-034 | one person is the sole lawful conduit for a second institution's authority on the first's ground | core | **structure yes, content no** | purview is the seat's rung: his Church seat at `T1` is the only Church seat reaching Crown ground, and its remit is `[]` | name `issue` on his row so his seat can write the warrant | FA (content) | `06_FA_remit_grant_by_row.md` | a hand-built warrant issued through his seat admits an `arrest` at `T1`; through any other Church seat it is refused |
| NPC-073, NPC-074, NPC-084 | a council seat casts a distinct position on faction policy | core | no | `determine` 0, 1, 0 executed (E-5); the vote conjunct is hand-built only (CR-34) | SC's hearing; H-80 | SC | sibling `05_SC_*` | SC's |
| NPC-089 | a frontier governor chooses among probe, pressure and invasion | core | partly | she may `march` and `issue` (E-3: `issue` executed); no demand, no declaration | the trade demand (FA-01), `declare` (CP-T09-02) | FA | — (plan) | the cards' exits |
| NPC-090 | a treaty constrains what trade officials may change | core | no | `covenant` 0 of 10 (E-3); nothing reads a covenant | CP-T09-03 | FA | — (plan) | its exit |
| ARC-40 | a head of state forced to act, abdicate or be replaced | core | abdication yes, forcing no | `release` of his own `hold` is lawful (`_eff_release`); `release` 0 of 15 in the realm (E-3) | the forcing is CR-89's; replacement is CR-37's | FA | — (plan) | CR-90 |
| ARC-R18 | a formal vote that neither coalition wins, with consequences | core | hand-built only | CR-34's `vote` conjunct refuses below quorum | SC's | SC | sibling | SC's |
| ARC-17, ARC-04 | a superior's response to a subordinate's disloyalty; trust eroding from inaction | core | no | F-FA-05 | CR-88; the defied-writ occasion gives the superior something to respond to | FA / CHAR | `06_FA_decree_binds.md` | as row 1 |
| ARC-01, ARC-03 | a quantity that moves purely from the *absence* of any act | core | no, and **wrongly stated against a ruling** | ED-IN-0345: a clock is an accumulation of world events; a clock that moves with no event stays cut (CR-89's WHAT) | restate on events that already mark inaction: a petition's or a seat's `term.matured` (542 at realm seed 0, E-5) | FA / CORE | — (CR-89) | CR-89 commit (1) |
| ARC-45, NPC-012 | a diplomatic demand suppressed while an intermediary withholds signals | core | no | no demand exists | FA-01's clause after CR-29 | FA / CORE | — (plan) | FA-01's exit |

**Needs wrongly stated** (three kinds). *Against the architecture*: NPC-008's passive office modifier.
*Against a ruling*: ARC-01 and ARC-03's absence-driven drift. *Against the built content*: NPC-032 and
NPC-003, where the realm seats a character the case says holds no powers or no seat. A fourth kind is the
extractor's own: fourteen FA-bearing cases carry an UNCLEAR need that says no goal, remit or territory was
authored (NPC-071, -034, -035, -036, -037, -039, -041, -072 to -074, -081, -082, -084, -085); those are
content debts on `references/npc_registry.yaml` and `offices.yaml`, not engine gaps.

**What FA can bring up soonest, in order.**

1. **NPC-083, the governor under orders** (and the order half of NPC-020, ARC-17): after
   `06_FA_decree_binds.md`. Artifact: the spine scenario with the player as a territory's lord and the
   auto chooser above him; a season in which a writ addressed to him is answered either way and the issuer's
   later question set names him. No other lane is needed but CORE's review of the witness edit.
2. **NPC-036, -072, -082 and NPC-032, -034, the posts that mean something**: after
   `06_FA_remit_grant_by_row.md`. Artifact: `aperture 2 0` PER HOLDER. No dependency.
3. **NPC-031 and the succession half of NPC-020**: the mechanism is in the tree; it needs a vacancy.
   Artifact: the scenario's succession situation (the King `release`s; the heir's `succeed` executes; a
   control with the heir banned refuses). No dependency.
4. **NPC-008's refill and every "who is next in the chain" need (NPC-070, NPC-006, NPC-009)**: after
   `06_FA_seat_terms_and_turnover.md`. Depends on CORE's question slot (H-54) only for how often, not
   whether.
5. **NPC-052, NPC-081, NPC-050's contest**: after CR-35 (B10-17 close two). Depends on SC (the declared
   disposal and the docket's arrangement, H-80).
6. **NPC-070's Split, ARC-40, NPC-050's campaign**: after B10-17b. Depends on CHAR (CR-83, IN-70) and CORE
   (CR-29).

## 14. Capability authoring surface

**(a) Where FA takes a character capability as input.**

| point | what is read | from where | code |
|---|---|---|---|
| aperture: which seat-gated verbs a person may form | the grant on his `hold` (`Tenure.granted_acts`) | `offices.yaml: seats[].remit_acts`, snapshotted at seating | `World._grant_remit`; `decision/options.py::opening_set` |
| authority: whether the act is admitted | the seat's rung, basis fields and oaths | `offices.yaml` (`rung`, `conferral`, `revocation`), `rosters.yaml` (`conferral_bases`, `revocation_bases`, `successions`) | `state/gate.py::may_fill`, `may_revoke`, `may_claim`, `purview_reaches` |
| action economy | one more scene per live `hold`; fewer for wounds and travel | `Fixtures budget_office_bonus`, `band_floors`, `budget_leg_penalty` | `decision/budget.py` |
| the pool of a contested governance act (`determine`, `arrest`, `interrogate`; `capture`; `march`'s field) | the actor's held capability key for the verb's vocation, else the vocation's attribute, else `pool_default` | `rosters.yaml: verb_capability` (verb → vocation), `vocation_attribute` (vocation → one of the ten `references/descriptor_registry.yaml: attributes`), `Person.capability`, `lifepath_templates` | `seam/wrappers/pool.py::faculty` (`:78`; `sigma.py:105` re-exports it) |
| the score of a governance candidate | pursuits against the verb's alignment cells; held affiliations against the verb × affiliation table | `rosters.yaml` tables (`alignment`, `affiliation_engagement`, `incompatible`) | `decision/choose.py`; `data/affiliations.py::engagement` |
| what a revocation costs | the seat's conferral basis | `state/gate.py::REVOCATION_DISPOSAL` | `_eff_revoke` |
| whom to seat | nothing about the candidate: the conferee is any living person the conferrer knows, tied on score, lowest id first (H-207's cite) | — | `decision/options.py::operand_bags` |

**(b) Data-driven, hard-coded or doubled.**

- *Data-driven and single-owned:* the grant, the bases, the budget magnitudes, the alignment and affiliation
  tables, the vocation chain.
- *Data-driven and empty for FA:* `verb_capability` has rows for `tell`, `speak`, `argue`, the three
  inquiries, `fight`, `accept` and `capture`, and **none for `determine`, `arrest`, `interrogate` or
  `march`**. So no person's ability changes the outcome of any judgment, arrest or interrogation: each rolls
  `pool_default` (2). In the realm run no governance verb reached a roll at all, and every pool the seam did
  roll for other verbs was 2 with no two actors differing (E-3, POOLS ROLLED).
- *Rule in code, by declared precedent:* `REVOCATION_RULES`, `REVOCATION_DISPOSAL`, `FILLED_BY`
  (`gate.py:617`, `:653`, `:697`): the roster names the basis, Python holds the rule, an import check keeps
  them total. Acceptable: these are rules, not capabilities.
- *Content constants in code:* `FOUNDER_KEEPS`, `FOUNDED_CONFERRAL`, `FOUNDED_REVOCATION`
  (`predicates.py:255-257`): what a founded office is granted. These are content and belong on
  `offices.yaml` beside `titles:`.
- *Possibly doubled:* which remit act licenses which gate basis is spelt in the verb row's `eligibility:`
  and again as `WARRANT_ACT`, `SEIZURE_ACT`, `MUSTER_ACT`, `CESSION_ACT`, `BENCH_BASIS` in `gate.py:260-342`.
  [UNVERIFIED: whether a load check ties each constant to its row.]

**(c) Target shape, for FA.** FA needs no capability system of its own. The owner exists:
`rosters.yaml: verb_capability` and `vocation_attribute`, over the attribute registry, read by `faculty`.
What a capability definition must say for FA to use it, and where:

1. *A verb says which vocation it draws on* (`verb_capability`, existing). FA needs rows for its contested
   verbs. The chain is closed both ways, so each new vocation also needs its `vocation_attribute` row.
2. *A seat says which vocation its post calls on* (new, one optional key `vocation:` on the `offices.yaml`
   row, validated against `data/verbs.py::VOCATIONS`). It gates nothing. It is read in one place: ranking
   the candidates for a `confer`, where today the choice is positional.
3. *A capability says how it is gained from service* (existing owner: `train` and the `practice` addend).
   FA asks only that exercising a seat's contested verb counts as practice of that verb's vocation, which
   the practice rule already does for any verb with a `verb_capability` row once (1) is authored.

**The interface FA states for the holistic merge:** `faculty(person, verb) -> pool` and its opposition twin
stay the only readers of capability at a roll; `vocation_of(seat) -> vocation | None` is the one new read,
and it feeds a candidate's score, never admission. FA reads no attribute by name anywhere.

**(d) The axioms, in the tradition's vocabulary.**

Implemented:

- *Position is a permission, not a statistic.* An office grants a fixed list of actions (a class feature
  list); skill plays no part in whether a decree, an appointment or a dismissal is lawful.
- *Skill supplies dice and never access* (ruled: "capability supplies dice and gates nothing").
- *Action economy scales with station and shrinks with wounds.*
- *An item as a key:* a warrant licenses an arrest; a writ is what one obeys.
- *A status condition:* `ban` and `detain` are conditions with a source and a remover (`pardon`).
- *Bonds with upkeep:* an oath of service costs its seat per term and lapses unpaid.
- *Opposed rolls* for the contested governance verbs.

Lacking, where a designer would look for it:

- No leadership, command, statecraft or judgment skill touches any governance outcome (b).
- No advancement from holding office: a term as a judge teaches nothing.
- No rank within a faction: `decision/options.py::rank` reads 0 for every pair (H-181); CR-32 owns ladders.
- No qualification for a post, even as a preference: the conferee is positional.
- No loyalty value that play reads (`data/cast.py`'s loyalty weights goal rows at build and nothing after).

Contradicted, deliberately, and a designer should be told: there is no faction sheet of statistics. A faction
has no attributes, no treasury of its own and no morale; every such figure is a Query over persons, and the
`faction_sheet` Record is a frozen copy of that Query.

**(e) Proposals, ordered.**

1. `06_FA_office_capabilities.md`: the four `verb_capability` rows and their `vocation_attribute` rows; the
   optional `vocation:` key on a seat and its one reader; `FOUNDER_KEEPS` and its two siblings moved to
   `offices.yaml`. The vocation names and their attributes are Jordan's content and are proposed as
   assumptions.
2. Nothing further in FA. Rank is CR-32's; duty is CR-88's; the merged authoring file is the holistic
   stage's.

## 15. The NPC and chooser surface in FA

The statement of the intent, reconciled from code and ruling, is the CHAR lane's
(`audits/02_CHAR_audit.md`; its intent section was not yet written when this audit closed and is cited, not
read). What follows is only what FA's own code shows.

**(a) What FA needs of an NPC and of the chooser.** *Who decides:* always a person, never a faction; a
governance act is the seat-holder's own, through `make_chooser`. *On what information:* his View and ledger,
plus three standing occasions that stamp referents onto the question he answers: vacant seats he may fill
(`world_q.vacancies`), writs he holds that name him (`writs_held`), matters before a sitting he sits on
(`sittings_before`). *With what temperament:* the verb's alignment cells against his pursuits, and the
verb × affiliation table against his held affiliations. *At what budget:* the scene base, plus one per seat
held, less wounds and travel. *With what visible reasons:* a refusal Event keyed by clause for a typed row;
nothing for the three predicate rows (H-252); the chooser's deciding term only through the `interactions`
instrument. FA additionally needs, and does not have: a reason to fill a vacancy, a way to choose whom to
seat, a reason to obey or defy, and a response to a rival's march (F-FA-02, F-FA-01, F-FA-04, F-FA-05).

**(b) One interface for player and NPC.** Yes. `harness/play_surface.py::dispatching_chooser` hands a named
person's deliberation to a callback with the arguments the chooser receives, and
`decision/sheet.py::development_space` lets a player rank and select from the candidate set and refuses an
index outside it, so through that space a player in a seat is offered exactly what an NPC in it is. FA has
no second path. One asymmetry to keep closed: a hand-built act may carry payload keys no computed act can
(`term` on a `confer`, `office` on a `revoke`, the overlay keys of an `establish`); a client that builds
acts instead of picking candidates would have a wider aperture than any NPC. The two proposals that move
those keys onto data and onto `subject` (R-17, R-03) close most of it.

**(c) Rules FA hard-codes where the chooser should decide.** None branches on an entity. Four are
tie-breaks or stamps that act as rules:

- the conferee: every `confer(seat, to=*)` candidate ties on score, so the lowest-id known person is seated
  and the conferrer himself is last (H-207's cite);
- the founded post: where a rung kind has two titles the first in authored order is taken, so a computed
  founding always mints the King, the Duke, the Count (`predicates.py:281-282`, `:304`);
- a vacancy is stamped from a world fact with no ledger channel (`vacancies` reads whether a seat is held),
  so an NPC knows a seat is empty without having heard it; the tree records the tension with AX-7 (H-207's
  cite) and leaves it;
- every binding decision is deposited on everyone alive (`_ch_chronicle`), so no NPC is ignorant of a
  decree; CR-29 owns the replacement.

**(d) What would make an officer characterful, and legible afterwards.** *Characterful:* the choice to obey
or defy read from his regard for the issuer and the issuer's legitimacy (`person_q.legitimacy` exists;
`comply` and `evade / defy` do carry alignment cells, one on each of the seven axes of `rosters.yaml: tables: alignment: cells`, and none in `pursuit_projection` [GROUNDED, 25 G-35, by parse]); the choice of whom
to seat read from his regard for each candidate and the seat's vocation; the weight of a vacancy or an
unanswered order read from his office's goals (CR-88). *Legible:* the clause that refused a `confer` or an
`establish` (R-14); the digest of §9; the occasion an act cites, which already exists and which the
defied-writ occasion would make specific ("he revoked the reeve because the reeve defied the grain writ").

**(e) Missing, as proposals.** `06_FA_decree_binds.md` (the obey-or-defy decision and the issuer's response);
`06_FA_office_capabilities.md` (ranking the conferee); `06_FA_hygiene.md` R-14 (the refusing clause);
`06_FA_playable_scenario.md` (reasons shown to a player). Duty is CR-88's and is not duplicated.
