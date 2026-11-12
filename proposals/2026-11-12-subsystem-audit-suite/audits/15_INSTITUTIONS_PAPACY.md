# INSTITUTIONS · PAPACY — the Church of Solmund as persons in seats under procedure

## Status: REFERENCE (a design and plan in proposal form; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: 84d2a02 (working tree)

Lane: the papacy and Rome, and religious institutions generally, adapted to Valoria's Church of Solmund
(`INSTITUTIONS_BRIEF.md`, FAMILY=PAPACY). Every reading names its command and seed in §14. `[UNVERIFIED]`
marks what was not opened; `[M]` marks a historical statement written from memory (the sourcing floor:
the shape is the finding, the date or figure is a lead). Proposals this file carries are
`proposals/15_INSTITUTIONS_PAPACY_A…F_*.md`, all PROPOSED, none ratified by being written.

Two instructions arrived from the orchestrator during the work and are obeyed throughout:
Jordan's fixed point on legitimacy (the crown and the two ducal houses were won by conquest in the secession
war, in the order king, first Duke of Hafenmark, first Duke of Varfell; §2), and the standing rule
*"we do not do deterministic"* (every consequential outcome is a draw; §6 states each procedure's draw).

---

## 0. Verdict

**The engine already holds the right skeleton for a Church and almost none of its force: seven seats at one
city, a creed, four bodies, three hearing rows and a goal to root out heresy, with no reach beyond
Himmelenger, no memory, no income, no election, no discipline and no sanction that has ever opened in
computed play.** In three seasons at seeds 0 and 1 the seven Church seats made 113 resolved acts
(`issue`, `covenant`, `open_case`, `establish`, `convene`, `pardon`, and, through the testing remit,
`raze` and `seize`), 22 of them `open_case`; they determined one matter and opened no `ban` and no
`detain`; a Cardinal who died at seed 1 was not replaced (E-1). At build the Church's purview and every Church bench
stop at `terr_T9`; the Crown's seats may lawfully fill every Church seat including the Confessor's, and
nobody may strip one; no person is sworn to a Church seat; the world holds two Records, both `works`, so
the founding deeds of the crown exist nowhere a person could read, cite, forge or burn; and the Confessor
himself is housed in a market in `terr_T1`, outside his own bench's ground (E-2).

**The single largest obstacle is that the Church has no way to act at a distance through persons.** A
historical church is a machine for projecting one seat's will across other men's land by four means:
local seats it fills (sees and benefices), documents it issues (rescripts, citations, sentences), courts
whose jurisdiction follows the person and the matter rather than the ground, and the compliance of
believers who are not its officers. The engine has a primitive for each (a seat anchored on a rung; the
`dispensation` Record with `comply` / `evade / defy` / `construe`; `determine` under an arrangement row;
`commit` to the faction's Proposition and `Person.conviction`). None is connected for the Church. The
design below connects them and adds **no verb, no stored quantity, no carrier and no tenure kind**. It
adds one seat-row key (`patronage:`), one arrangement key (`quorum_share:`), three arrangement rows, one
`offices.yaml` section of world-gen instruments, goal rows, seat rows and one typed `terms` form for a
writ of avoidance. Every outcome named is a draw on the one ladder (§6).

**On Jordan's fixed point** the tree already agrees and the engine already has the instrument: canon says
the crown is a *deed-monarchy, Church-consecrated* (`canon/03_canonical_timeline.md:78-92`, `:104`), and
`queries/person_q.py::legitimacy` (`:537`) is each person's own windowed sum of the holder's deeds he has
heard of. What is missing is the keeper: deeds fade from ledgers (34,837 `claim.decayed` Events in three
seasons, E-1) and nothing retells them. **The Church's office toward a conquest-founded crown is to keep,
certify and retell the ledger of deeds, and its leverage is that it can decline to.** §2.

---

## 1. What the tree holds

### 1.1 Code (the mechanism)

| fact | owner | reading |
|---|---|---|
| Seven Church seats: `off_confessor` (`elected`, `[issue, determine, confer, revoke, convene]`), four Cardinals (`appointed`), `off_senior_inquisitor` (`[determine]`), all anchored `{territory: "T9"}`; `off_archbishops_rep` at `{territory: "T1"}` with `remit_acts: []`. All seven `revocation: null` by ruling (Jordan, 2026-10-11) | `engine/season/offices.yaml:356-445` | opened |
| Five Church bodies: `Holy See`, `Cardinal of Fortitude / Justice / Prudence / Temperance`; their notes name portfolios (Templars; Inquisitors and adjudication; tithes, charities, land; universities, monasteries, archives) which nothing reads | `rosters.yaml: office_bodies` (`:2219-2224`, `:2277-2282`) | opened |
| Head seat `off_confessor`; role template `ecclesiastical`; leader NPC-021 | `rosters.yaml: factions.head_seat`, `role_templates.by_faction`, `faction_leaders` | opened |
| Hearing rows: `tribunal`, `inquisition_hearing` (`disposes: ban`, `bench`), `excommunication_deliberation` (`disposal: declared`, `quorum: 2`, `disposes: ban`, `disposal_reach: realm`) | `engine/season/arrangements.yaml:201-285` | opened |
| Restraints `detain` and `ban`: openers `arrest` / `determine` / `revoke`; closer `pardon`; a banned person is not seated and not admitted to service | `rosters.yaml: tenure_kinds` note; `loop/effects_governance.py:101`; `loop/predicates.py:500` | note opened; code lines by grep |
| A bench judges a person **present in its ground**: `may_determine` = grant carries `determine` ∧ party is another person ∧ `sits_over(seat, home_of(party))`, and `sits_over` reads `scope_rung` | `state/gate.py:899-978` | opened |
| Purview: a seat reaches its own rung and descendants, **and the ground of every seat whose holder owes it a live `oblige`** (the oblige clause, IN-40) | `state/gate.py:386-431` | opened |
| Who may fill a seat: any seat the actor holds, other than the seat itself, whose purview reaches the seat's rung; no faction clause | `state/gate.py::may_fill` (`:845-866`) | opened |
| Legitimacy is one person's own estimate: stance toward the holder plus his pursuits' reading of the holder's deeds in his recent claims | `queries/person_q.py:537-563` | opened |
| Church goals: orthodoxy; **root out heresy, read as "whoever a churchman knows to have done a deed the shared vow column engages"**; suppress the Restoration; per-body goals (Inquisitors, Templars, tithes, learning) | `engine/season/goals.yaml:140-156`, `:226-290` | by grep, lines opened in excerpt |
| The vow column: `utter`, `tie / knot`, `commit`, `confer`, `oblige`, `establish` engage every affiliation positively; `evade / defy`, `destroy_record`, `forge` negatively; `thread_read` violates `solmund_orthodoxy` | `rosters.yaml: affiliation_engagement` (`:3706-3772`) | opened |
| Affiliations `solmund_orthodoxy`, `inner_tradition` (both under concern `church`), `thread_truth`, `einhir_restoration`, `altonian_civics`, scale 0-5 | `engine/engine_params/descriptors.json: affiliation_roster` | opened |
| Ending `theocracy`: the King's seat held by a person who coheres under the Church; not a victory | `rosters.yaml: endings` (`:3466-3477`) | opened |
| Venues serving the Church: cathedral, chapter house, scriptorium, almonry, chapels; canonical seat S-036 Himmelenger | `engine/season/venues.yaml:68-147` | by grep |
| Strife code CH "Religious sanction": no verb, no kind, `gap:` | `harness/strife_moves.yaml:90` | opened |

### 1.2 Canon and Jordan's word (the world)

- The Church formed over two centuries from a catalysed interpretive community; Solmund did not found it.
  Its anti-threadwork theology is emergent, not conspiratorial (`canon/03_canonical_timeline.md:44-50`).
- Altonia contained it by accommodation: the cathedral city Himmelenger (T9) with tax-exempt lands,
  educational rights, archival authority and charity, in exchange for quiescence; *"the cage became a
  school"* (`:54-68`). The Church is cross-border: Altonia has a Solmundan minority (`:64`).
- The secession war made a commander king by deeds; **the Church consecrated him**: *"victories are evidence
  of divine favour … The Church's support is the price the Crown pays for legitimacy, and the price the
  Church charges for switching from Altonian accommodation to Valorian alliance"* (`:78-84`). The settlement:
  crown first among equals, ducal authority not overridable, the Church co-sovereign (`:86-106`).
- The deed-presumption is rebuttable; Almud *"has not personally earned the deed-claim — inherits the
  presumption his father created"* (`:92`, `:117`).
- Jordan, 2026-09-18: *"cardinal is a post / king is a post / confessor is a post"*; *"Confessor governs
  the Church tho"*; *"they are super weird in that they don't have territories at first"*
  (`rosters.yaml:387-395`). Jordan, 2026-10-04: *"ratcheting of Church as faction until it attempts to
  seize lands and become a theocracy"* (`rosters.yaml:3471`). Clocks are folds of the log and belong to the
  game (ED-IN-0343 to 0345, as the plan records them at CR-89).

### 1.3 Design intent (ARCHIVED-NOT-CANON; vocabulary only)

`faction_canon_v30.md` Part B (Church sheet, `:567-737`): four-Cardinal structure; inspiration *"Avignon
papacy + medieval Inquisition + Counter-Reformation"*; Excommunication (strips Church contacts, bars
office, a failed attempt makes a martyr; reversal by Grand Debate or a new Confessor); the Consecration
Triangle (Almud, Baralta, Himlensendt); arcs Zealot / Crisis of Faith / Confrontation, with *"the vacuum
may be worse — Cardinal of Justice or Fortitude may seize control"*. `worldbuilding_v30.md` §3: Cardinal
Independence Check, Jarnstal Drift, Klapp Awakening, Olafsson exposure, Prudence Crisis (charities
collapse, the Restoration fills the gap), excommunication reversal by Penance / Grand Debate /
Banishment, the suppressed practitioner-witness tradition and Seam Texts. `ci_political_v30.md`: Church
Influence 0-100 with bands and a Mass Seizure. Each of these is a counter, a card or a threshold; the plan
has already translated the counters (CR-89: CI as a fold; FA-07's second round: Piety Track as the share
of a territory's residents committed to the Church's Proposition, Church Attention as each seat-holder's
own attention). This lane translates the *procedures*.

### 1.4 What the plan already schedules (composed on, not redone)

| position | what it gives this design |
|---|---|
| CR-35 (B10-17) | an elected seat is filled by its faction's bench through `determine` under `election` / `succession` rows (`disposal: declared`, `disposes: hold`); the King's `confer` of the Confessor's seat is refused once the elected narrowing ships; its own falsifier is the Confessor's election |
| CR-36 | `nominated` basis; a `resolution` Record minted by `determine` under a `disposes: Record` row |
| CR-37 | the throne stripped by the Holy See's `revoke` on a held `resolution` (`joint_concurrence`) |
| CR-60 (B10-18c) | a `scope:` key so a Church bench may judge realm-wide while acting only where its `rung` reaches; `authority.by_faction`; two rites, accusatorial and inquisitorial |
| CR-51, CR-63 | the warrant and the church-custody branch; appear / evade / defy as verb rows |
| CR-74 | the CH strife signature, or the missing carrier named |
| CR-88, CR-89 | duty of office and its lift by grievance; Church Influence as a fold with band triggers |
| verb lane `audits/14_VERBS_BINDING.md` §0.2 | `confer`, `revoke`, `succeed`, `pardon`, `establish`, `issue` become contested draws with one shape (Partial = provisional; Failure = nothing written, re-attemptable) |
| SC lane | the obstacle as difficulty plus named terms (`05_SC_obstacle_difficulty_and_modifiers_B.md`); tuning tables (`13_SC_tuning_tables.md`); band-keyed `disposes:` (SC-P4); acquittal (SC-P6); cited evidence (SC-P8, ARCS 04) |
| FA lane | a decree binds as the addressee's choice (FA-P1); `dispatch` by row (FA-P2); seat terms (FA-P3, FA-B3); §11 item 3 (Church seats nobody can strip) |

### 1.5 Findings from this lane's probes

| id | severity | finding | evidence |
|---|---|---|---|
| F-PAP-01 | blocks R-01, R-04 for the Church | The Church acts and judges only inside `terr_T9`: `purview_reaches(off_confessor, r)` and `sits_over(<any Church bench>, r)` are False for `terr_T1`, `terr_T6`, both duchies and the realm. 9 of 83 persons stand under T9. CR-60 answers the judging half only | E-2 |
| F-PAP-02 | degrades narrative | Himmelenger lies inside the realm rung, so every Church seat is fillable through a Crown seat (`may_fill` True for `off_king`, `off_widow_regent` on all six T9 seats, and for fourteen Crown and Löwenritter seats on the Archbishop's Representative). CR-35's narrowing reaches the one `elected` row; the six `appointed` rows stay royal appointments. Canon calls the city sovereign | E-2; `state/gate.py:845-866` |
| F-PAP-03 | degrades narrative | No Church seat can be stripped by anyone (`may_revoke` empty for all seven); a Cardinal leaves by death only (FA §11 item 3, not yet ruled) | E-2 |
| F-PAP-04 | hygiene (content) | The Confessor's roster row has `institution: null`, `home: b_s_003_market`, a market under `terr_T1` (`npcs.yaml:192-200`); the head of the Church is not at the Church and not under any Church bench | E-2; the row |
| F-PAP-05 | blocks R-02 for sanction | No sanction opens in computed play: 0 `ban`, 0 `detain` Tenures after three seasons at seeds 0 and 1; `case.opened` 7 and 11, `matter.determined` 0 and 1 | E-1 |
| F-PAP-06 | blocks the fixed point | No Record of any deed, charter or attestation exists (`records by kind: {'works': 2}`); the secession deeds and their order are in no ledger and no document | E-2 |
| F-PAP-07 | degrades narrative | No oath or instrument joins Crown and Church: 0 `oblige` edges to a Church seat; the three to `off_king` are the two dukes and the Grand Master | E-2 |
| F-PAP-08 | degrades narrative | The Templars' Cardinal commands by accident: `off_cardinal_fortitude`'s row grants `[issue, convene]`; marching, arrest and capture come from the unruled `dispatch` every loop-built seat keeps, which FA-P2 removes. After FA-P2 the Church's military arm commands nothing | `offices.yaml:382-393`; E-1 (remit read at build) |
| F-PAP-09 | degrades narrative; R-09 | The declared tally is a fixed function: `determine` under `excommunication_deliberation` is admitted when live votes ≥ `quorum`, and the vote count then plays no part in the odds (`world_q.declared_votes`, `:737-763`). Under the standing rule the count must set odds, not decide | the function, opened |
| F-PAP-10 | hygiene | `excommunication_deliberation`'s header calls it *"a body disposing of a person who is not there"*; `declared_votes` takes its bench from `judging_set` at the party's place and `may_determine` requires the party in the bench's ground, so the row cannot run on an absent party today | `arrangements.yaml:253`; `gate.py:975-978`; `world_q.py:752-757` |

---

## 2. Jordan's fixed point: a conquest-founded crown and the Church that consecrated it

### 2.1 Where the tree says it, and where it disagrees

| statement | where | agreement with Jordan's word |
|---|---|---|
| the first king was the war's decisive commander; authority *"entirely earned through wartime deeds"*, no blood claim | `canon/03_canonical_timeline.md:78-80` | agrees |
| ducal families *"earned proximity to power through Secession-era service"*; the Baralta ducal status *"earned through wartime deeds"* | `:90` | agrees for Hafenmark; **silent on the order** (king, Hafenmark, Varfell) |
| the coalition was *"primarily northern"*, the south *"geographically peripheral and culturally stigmatised"*; the caste follows *"the south's exclusion from the war coalition's leadership"* | `:76`, `:96` | **tension, named**: Jordan ranks the first Duke of Varfell third in accomplishment. Third of three is consistent with a lesser part; *exclusion from leadership* is not consistent with a ducal house founded by conquest. Jordan's word governs the world: Varfell's founder fought and won, and ranked last; the caste is the grievance of a house whose deeds were certified third |
| the Duke of Varfell is *"first among the Jarls, not a monarch"*, `conferral: elected` | `offices.yaml:226-237` | **tension, named**: a house founded by conquest and a seat filled by the Jarls' vote. Both can hold: the first Duke's deed made the ducal seat; the Jarls choose who sits in it. The engine's row stands (the code governs the engine); the founding deed attaches to the seat's first holder and his line's claim is one candidacy among the Jarls' |
| the throne passes by `inheritance` to the holder of the heir's title, who must claim it | `offices.yaml:187-198`, `:252-263`; `rosters.yaml: successions` | agrees with *"inherits the presumption"*; says nothing of the deed |
| Deed-presumption enforced by *"the Coup Counter and Motion of No Confidence"* | `canon/…timeline.md:92` | the counters are refused by Layer 1; the plan's replacements are CR-37 (deposition by motion and concurrence) and each person's `legitimacy` estimate |
| Almud is the founder's son; the founder died in a hunting accident, perpetrator undefined | `:114-117`, `:175` | agrees; a standing mystery the deed ledger makes playable (§9) |

No file states the order of accomplishment. It is a new world fact and needs an owner code reads
(proposal C: three world-gen instruments).

### 2.2 The design: rank is a ledger of deeds, and the Church keeps the ledger

What the engine already does: a deed is an Event; a witness holds a claim of it; `legitimacy(p, holder,
window)` sums what `p`'s own pursuits make of the holder's deeds in `p`'s recent claims, plus `p`'s stored
stance toward him. Two persons with different ledgers read different legitimacy. Claims fade. So the
engine's own answer to *how is rank won by deed* is: by acts others witness or are told of, for as long as
they remember. That is the right primitive and this design changes none of it.

What a conquest-founded house therefore lacks, forty-five years on, is memory. Three things supply it,
all existing carriers:

1. **The attestation.** A Church bench, on a claimant's petition naming a seat, hears his deeds and
   determines. At Success the determining seat mints a `resolution` Record (CR-36's kind and site) whose
   terms name the seat and whose `to` names the claimant. That Record is the certificate: it is held (by
   the Church), it can be researched, copied, given, concealed, forged, seized, destroyed, and it is a
   proof of kind `record` in any later hearing that admits records (the `succession` contest of CR-35,
   the deposition motion of CR-37, the next consecration). The procedure is the arrangement row
   `consecration` (proposal C). **It is a draw**: pool the bench's, obstacle the row's `standard` plus
   `evidence` (the deeds cited and the answers standing against them) plus `reception`; §6 row P-3.
2. **The founding roll.** Three such Records exist at build, made at the settlement of 200 AG and kept in
   the Cardinal of Temperance's archive: the first king's, the first Duke of Hafenmark's, the first Duke
   of Varfell's, each attesting its house's deeds, the king's the longest and Varfell's the shortest
   (Jordan's order, carried as content: the number of attested deed entries per Record). A fourth
   instrument is the settlement charter: a `dispensation` issued through the throne, addressed to the
   Crown's officers, whose terms are the Church's liberties (immunity of Himmelenger and its lands, the
   schools, the archive). Proposal C, world-gen instruments.
3. **Commemoration.** A Church seat-holder who holds a living person's attestation tells that person's
   attested deeds (`tell`, `speak` in the epideictic genre) at sittings and feasts; hearers receive told
   deed claims with the teller in the chain, weighed by their regard for the teller (`teller_weight`,
   existing). Those claims are what refresh `legitimacy` in living ledgers. A holder the Church
   commemorates is renewed in every ledger the sermon reaches; one it is silent about decays to stance
   alone; a rival whose deeds it preaches rises. Nothing here is a rule about kings: it is `tell` from a
   held Record, chosen by the teller through the one chooser. ⚠ The limit, stated: a dead founder's deeds
   are no living person's deeds, so commemorating the founder moves nobody's `legitimacy` of the heir
   under the query as built. The founder's roll works in hearings (as a proof the heir's side cites) and
   the heir's standing in the street is his stored stance plus his own deeds. If the FA lane gives a
   *house* a carrier (a hearth rung as the subject of deed claims, which `decision/choose.py:68-71` already
   reads for a Rung), commemoration of the founder reaches the heir through one added term in
   `legitimacy`; this lane states the interface and does not add the term.

The questions the brief asks, answered in those terms:

| question | answer in the engine's units |
|---|---|
| what counts as a deed | any emitted Event kind that is not a refusal (`data/verbs.py::DEED_KINDS`); its worth to a judge is his own pursuits' alignment with the kind (`deed_term`). No second list |
| who certifies it | witnesses hold it firsthand; a Church bench certifies it into a Record by `determine` under `consecration`. Certification is a contested draw and can fail or be partial |
| what it costs to claim | a petition, a sitting (a season), the proofs brought, and exposure: the hearing is where a rival's contrary proof is cited (SC-P8). A failed petition is known (the chronicle channel) |
| how it passes to heirs | not at all by itself. An heir inherits stance (the *presumption*, a stored row) and the right to cite his predecessor's attestation as a proof at his own consecration. The founder's deeds are not the heir's deeds in any ledger |
| how it is renewed | by the heir's own deeds, witnessed or told, by his own consecration (which attests them into a Record), and by the Church's commemoration of them |
| how a rival's deed unseats it | by the same route in reverse: a rival with fresh deeds in many ledgers and an attestation of his own stands better in a `succession` contest and gives each elector, vassal and deposing bench better odds (the `evidence` and `reception` terms). No threshold fires; persons act on their own estimates |
| what the house owes | the charter's terms: the Church's liberties. Breach (an officer who judges, taxes or seizes in Himmelenger) is a deed the Church's goal acts against (proposal C goal row) |
| what the house is owed | consecration of its heirs when petitioned, and commemoration. Both are the Church's choices, hence its leverage |

**The Church as rival source of legitimacy.** The same archive and the same pulpit serve the Church's own
claim. The Consecration Triangle of the archived design becomes mechanical without a rule naming anyone:
Baralta's house holds the second attestation; if the throne is vacant or contested she petitions for
consecration; the Confessor's bench determines; his odds read her proofs (strong) and the bench's reception
of her (hostile: her goal is the Church's rival, `goals.yaml:314-324`). A Failure is the refusal that
*"cracks the settlement"*; a Partial is a provisional consecration (§6). The `theocracy` ending is the
limit case: a Church man with an attestation of his own.

**What this does not do.** Consecration confers no seat and gates no claim: the heir's `succeed` is the
engine's and stands. It moves no world quantity; there is no divine favour in the simulation (canon guard,
§4.2). It is a document and a telling, and their weight is what persons give them.

### 2.3 The standing rule, applied to this lane

Every procedure in §6 is stated as: an eligibility check (may the act be attempted), a pool, an obstacle
(difficulty plus named terms from the SC lane's closed roster), and four bands with a recoverable Failure.
Two things in the present code and plan are fixed functions and are corrected in this lane's proposals:
the declared tally (F-PAP-09; proposal B makes the vote share an obstacle term and keeps only *can the
body sit* as a check) and the effect of a sanction on third parties (proposal D: each addressee's answer
to a writ of avoidance is his own draw; an oath is never dissolved by rule). Listed for the owning lanes,
not edited: CR-35's *"the first valid claim wins"* and `quorum: 1` (IN/FA), and `succeed`'s certainty
(the verb lane has already made it a draw, `14_VERBS_BINDING.md` §0.2).

---

## 3. How it really worked

Sources: the tree's governance research where it covers the subject (`research/governance/governance_modes.md`
§3 Investiture, §4 Papal States, `:208-215`, `:293-296`; `conflicts_power_struggles.md` `:196-209`, `:270-277`;
`political_hierarchy_standing.md` `:30`, `:172-173`; `research/fa_se_historical_precedent_research_v1.md`
for advowson and interdict by name) and, for everything else, general knowledge of the standard
literature, written from memory and marked `[M]`. No figure below is offered as a tuning value.

### 3.1 The apex and how it was filled

The bishop of Rome was chosen, in the early centuries, by clergy and people, which in practice meant by
whichever Roman family or emperor held the city. The reform papacy took the choice away from both: the
decree of 1059 gave it to the cardinal bishops `[M]`; 1179 (*Licet de vitanda*) fixed **two-thirds of the
cardinals** and admitted no appeal, because there was no superior to appeal to `[M]`; 1274 (*Ubi periculum*),
after a vacancy of nearly three years, added enclosure: the electors shut in one room, their food reduced
after three days and again after eight, their revenues suspended while the see was vacant (the tree has this
at `governance_modes.md:295`). The intricacies that matter for play:

- **Three lawful modes**: scrutiny (a ballot), compromise (the body delegates the choice to a few of its
  number when it cannot agree), and acclamation. After a scrutiny an elector could switch his vote to a
  leading candidate (*accessus*) `[M]`.
- **Capitulations**: from the mid-fourteenth century the electors swore, before voting, a pact binding
  whoever was chosen (share revenues with the college, call a council, limit creations). The elected pope
  usually repudiated it `[M]`. A pact made by electors and broken by the winner is a standing grievance.
- **Factions were made by appointment.** A pope created cardinals; his creatures voted as a bloc under his
  cardinal-nephew after his death. The college was the dead pope's patronage, facing the next one.
- **The vacancy was dangerous.** The treasury was looted, offices lapsed, the city rioted, and outside
  powers pressed (1378: a mob demanding an Italian; the same electors later declared their own election
  void for fear and chose another, `conflicts_power_struggles.md:272`).
- **No removal.** A pope could resign (1294) and could not be judged, except, canonists held, for heresy.
  That one exception is the hinge of every schism and council.

### 3.2 The curia: government by document

The pope governed a continent he never saw by letters. The organs `[M]`:

- **Chancery**: drafted and sealed. A petition (*supplicatio*) came in by a proctor, a professional agent
  resident at the curia; a referendary summarised it; it was signed (*fiat*); **the date of signing fixed
  priority** among rival grants of the same thing; an abbreviator drafted the minute, a scriptor engrossed
  it, it was taxed, sealed with the lead *bulla*, registered, and released on payment. Each step was an
  office with a fee. Speed and outcome depended on the proctor, the fees and who spoke for the petitioner.
- **Camera**: money. Collectors in each province; *common services* due from every bishop and abbot the
  pope appointed and *annates* from lesser benefices (both a share of the first year's income); the
  *spolia* of dead prelates; tenths on clerical income for crusade, usually shared with the king who let
  them be collected; census from vassal kingdoms. Receipts moved by bankers' bills, not by coin.
- **Penitentiary**: absolutions and dispensations: from excommunication, from illegitimacy for orders, from
  the forbidden degrees for marriage. A dynastic marriage needed one, which gave the curia a hand in
  every alliance.
- **Rota**: the appeal court, judging on written records sent from the provinces; cases took years.
- **Consistory**: pope and cardinals together, for the great causes, the creation of cardinals and the
  provision of bishoprics.

The instrument that projected papal justice was the **rescript appointing judges-delegate**: a party
appealed or petitioned; the curia, unable to hear a local cause, commissioned two or three local clergy to
hear it by papal authority. Rome's jurisdiction thus ran everywhere without Rome being anywhere, and a
litigant who reached the curia first chose his own judges.

### 3.3 Canon law and its courts

A written, taught, universal law (Gratian's collection and the decretal collections after it `[M]`) with a
graded court system: archdeacon, the bishop's official, the metropolitan, Rome; appeal suspended the
sentence. Jurisdiction ran by **person** (every cleric, in any matter: *benefit of clergy*) and by **matter**
(marriage and legitimacy, wills, oaths and perjury, tithes, usury, sacrilege, heresy), on anyone's land.
Procedure was written: a libel, a formal joining of issue, articles put to witnesses examined in private,
publication, sentence. Proof was graded: two eyewitnesses or a confession made full proof; one witness,
documents and common repute (*fama*) made half-proofs. Three ways to start a case: **accusation** (a named
accuser who bore the penalty if he failed), **denunciation**, and **inquisition** (the judge proceeds on
*fama* by his own office; general from 1215 `[M]`). An accused of good repute could clear himself by oath
with oath-helpers. Kings fought the boundary case by case: criminous clerks (Clarendon 1164 and Becket),
writs prohibiting church courts from lay matters, statutes against appeals and provisions from Rome
(England, 1350s), and finally concordats in which the king named bishops and the pope instituted them
(Bologna 1516; the Spanish crown's patronage) `[M]`.

### 3.4 Excommunication and interdict as political weapons

- **Excommunication** was a sentence, in grades. The minor form barred the sacraments; the major form put
  a person outside the community: no one might eat, trade, pray or deal with him, he could not sue, testify,
  hold office or a benefice; after a year unreconciled he was suspect of heresy `[M]`. It followed three
  warnings (*monitions*) or fell automatically on certain acts. Contumacy, failing to answer a citation,
  was itself ground for it, which is how absent parties were reached. From 1418 only a person **denounced
  by name** had to be shunned `[M]`: the sanction bound third parties only once published.
- **Its force was other people's compliance.** In England the bishop certified an obstinate excommunicate
  to the royal chancery after forty days and the king's officers arrested him `[M]`: the secular arm.
  Against a king there was no secular arm, so the weapon was the next clause: **his subjects were released
  from their oaths** (Gregory VII against Henry IV, 1076; Innocent IV against Frederick II, 1245). That
  dissolved nothing by itself. It gave princes who already wanted to rebel a lawful reason, and it worked
  when they existed (the tree's own reading: `conflicts_power_struggles.md:196-209`,
  `political_hierarchy_standing.md:193-194`: *"inert until princes field troops"*) and failed when they did
  not. Canossa shows the counter: submission and absolution took the pretext away.
- **Interdict** suspended the public rites of a place or a people: no public mass, no church burial, bells
  silent; baptism and the penance of the dying were kept. It punished subjects for a ruler's act in the
  hope they would press him. England 1208-14; Florence 1376, where the sentence also declared Florentine
  merchants abroad and their goods fair prize, an economic weapon; Venice 1606-07, where the Senate ordered
  the clergy to go on officiating, expelled those who obeyed Rome, and won `[M]`. Mitigations multiplied
  until an interdict was an inconvenience. Overuse was the decay.
- **Absolution** required satisfaction or security for it; great cases were reserved to the pope, which
  brought the penitent, or his proctor and his money, to the curia.

### 3.5 Councils

A general council was called by the pope and legislated with him. The fourteenth-century crisis turned it
into a rival: when two and then three lines of popes each held a valid-looking election, the only body
that could judge the head was a council, called by cardinals and princes (Pisa 1409, Constance 1414-18,
`conflicts_power_struggles.md:272`). Constance voted **by nation**, not by head, to cancel the Italian
majority, declared that a council holds its power directly and binds a pope, and ordered councils at fixed
intervals `[M]`. Basel sat for eighteen years, deposed a pope and elected the last antipope. Popes answered
by treating with kings directly (the concordats) and by forbidding appeal from a pope to a future council
(1460 `[M]`). The appeal to a council remained every aggrieved king's threat.

### 3.6 Investiture, patronage, benefices, simony

- **The proprietary church.** A lord who built and endowed a church owned it and appointed its priest; a
  king did the same with bishoprics, handing over ring and staff. The reformers named three evils: simony
  (buying office), clerical marriage (which made benefices heritable), lay investiture. The quarrel of
  1075-1122 ended in partition, not victory (`governance_modes.md:208-215`): the Church gave the spiritual
  symbols, the ruler the lands and rights; elections were held in the ruler's presence.
- **Election, licence, assent.** A cathedral chapter elected its bishop, with the king's licence to elect
  and his assent after; the king held the lands of a vacant see and took their revenue (regalian right),
  so a king profited by delay `[M]`.
- **Advowson.** The patron of a parish presented a clerk; the bishop instituted him. Presentation was
  property: inherited, sold, sued for in the king's court (the tree names it: FASE research). The office was
  the Church's, the gift of it a layman's.
- **The benefice.** An office with an endowment (glebe, tithe, fees). With cure of souls it required
  residence; without, it was income. Pluralism (several at once), non-residence, the hired vicar on a
  fraction of the income, *commendam* (the revenues of an abbey given to an outsider), and appropriation
  (a monastery as perpetual rector) turned benefices into a currency for paying officials and kin `[M]`.
- **Provision and reservation.** From the thirteenth century the pope provided to benefices directly and
  reserved whole classes to himself; *expectatives* promised the next vacancy. The curia became the
  market for careers, competing provisions for one living were litigated in the Rota, and the local patron
  or chapter often simply installed its own man. Whether a papal provision *took* depended on the ground.
- **Simony** never ended; it changed form: fees, compositions, services, loans, the sale of curial
  offices as a public debt. The line between a fee and a price was what reformers and satirists argued over.

### 3.7 Income: tithes and indulgences

The tithe was a tenth of produce owed to the parish, divided in theory among bishop, clergy, fabric and
poor, in practice largely captured by monasteries and lay impropriators; disputes over it filled the church
courts `[M]`. Above it sat the papal levies of §3.2. Indulgences began as remission for crusaders, were
extended to those who paid for one, to jubilee pilgrims, to the dead; preaching them was farmed to
licensed collectors, and the proceeds were often pledged in advance to a banker against a prelate's debt
for his own appointment fees `[M]`. The system's revenue and its discredit came from the same act.

### 3.8 The orders and their autonomy

- **Monastic**: each house self-governing under a rule and an elected abbot; reform came by federation:
  one mother-house whose abbot ruled dependent priories and which was **exempt from the local bishop and
  subject to the pope alone** (the Cluniac pattern), or a general chapter of all abbots with mutual
  visitation (the Cistercian) `[M]`.
- **Mendicant**: mobile preachers organised in provinces under an elected general, licensed by the pope to
  preach, confess and bury in any diocese, in competition with the parish clergy for souls and fees.
- **Military**: knights under vows with their own priests, lands and banks, exempt from bishops and tithes,
  answerable to the pope. The Templars were destroyed in 1307-12 by a king who owed them money, using
  the Church's own inquisitorial procedure and a compliant pope `[M]`: exemption protects an order from
  bishops, not from the power that protects it.

Exemption was the papacy's standing army inside every diocese and every bishop's standing grievance.

### 3.9 Inquisition

Papal inquisitors, mostly friars, commissioned from the 1230s to proceed by *inquisitio* against heresy
`[M]`. Procedure: arrival and sermon; a **period of grace** in which voluntary confession earned light
penance and required naming others; denunciations; citation; interrogation under oath with the witnesses'
names withheld; detention as pressure; torture permitted from mid-century within limits that were evaded;
sentence at a public sermon: penances, crosses, prison, confiscation; the relapsed and the obstinate
*relaxed to the secular arm* to be burned, since the Church shed no blood. Its real instrument was the
**register**: depositions kept, indexed and cross-read for decades, so that one confession convicted a
village a generation later. Constraints: severe sentences needed the bishop's concurrence; confiscation
gave rulers an interest for and against; inquisitors were murdered, records burned, appeals carried to
Rome. In Spain the crown made it a royal council.

### 3.10 Temporal power

A band of central Italy held on the strength of Frankish donations (and a forged imperial one), governed
through rectors and legates, in practice by granting towns to the lords who already held them as *vicars*
for a yearly census, and by the great Roman families who also supplied cardinals
(`governance_modes.md:295`). Each pope's kin were endowed out of it. Its defence drew the papacy into every
Italian war and made the pope one prince among others, which cost the universal office its standing.

### 3.11 Legates and nuncios

A legate *a latere* carried the pope's person: he outranked every local prelate, held councils, heard
appeals, deposed, dispensed, and lived at the local clergy's expense (procurations), which made him as
hated as he was powerful. Lesser envoys collected money or carried one message; resident nuncios at courts
came late `[M]`. Kings refused legates entry, or demanded that only a native archbishop hold the legation.

### 3.12 Schism and anti-popes

A schism needed a doubtful election and a power that preferred the doubt. Emperors installed anti-popes
after deposing popes (1080, 1159); a double election in 1130 was decided by which kings recognised whom;
1378 split Europe along existing alliances into *obediences*, each with its own college, curia and tax
collectors `[M]`. Ways out, in the order tried: both resign, both submit to arbitration, a council. Kings
used the interval: *subtraction of obedience* withdrew a kingdom's church from both claimants and left its
revenues with the king.

### 3.13 The relation to secular rulers

The theory moved from two powers each supreme in its sphere, to the spiritual judging the temporal *by
reason of sin*, to a claim of direct lordship that kings answered with force (Anagni, 1303) `[M]`. The
practice was a bargain renewed each reign: the ruler needed anointing, literate servants, the Church's
courts for marriage and inheritance, and its silence; the Church needed protection, enforcement by the
secular arm, and leave to tax its own clergy. The Frankish case that canon cites as Valoria's model is the
clearest: a mayor who held the power asked the pope whether he who held it should have the title, was
elected by his magnates and **anointed**, and later gave the pope lands (`governance_modes.md:142`). The
anointing made nothing true; it supplied a reason that outlasted the army.

### 3.14 How it decayed, was corrupted, and was resisted

Decay: every instrument was over-issued (indulgences, interdicts, provisions, dispensations) until its
price fell. Corruption: offices and graces had prices; kin were endowed; the reformers' own remedy,
centralisation, concentrated the market. Resistance: by kings (statutes, concordats, national churches),
by councils, by cities (Venice), by clergy who did not publish a sentence, by subjects who preferred their
lord, by the excommunicate who simply lived with it, by dissenters who denied the keys altogether.

<!-- APPEND-POINT-2 -->
