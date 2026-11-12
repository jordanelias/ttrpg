# INSTITUTIONS · PAPACY — the Church of Solmund as persons in seats under procedure

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 — where this file's names, homes or shapes differ from that ledger, the ledger governs: world-gen instruments live in `engine/season/instruments.yaml: seeded`, and the writ forms `avoid`, `withhold`, `render` are the forms `avoidance`, `interdict`, `tithe` of that file's `forms:` (X-01, X-02); a certificate carries `recites`, not `attests: n`; the archive holds the containment charter and the first king's consecration, and the two ducal papers are `homage` instruments in the chancery (X-03, X-05, X-08); §2.2's stated limit (a dead founder's deeds are nobody's) is answered by the chain term of `legitimacy` down the seat's holders (X-06; R-17 closed); the election's middle outcome is the one tally's `matter.undetermined` (X-15); the believer's decline and the lift of duty are read through `forborne` and `excused` (X-29, X-31). Of §13: items 1 and 2 are the synthesis's §10 items 2 and 3; item 3 is closed there; item 4 is its §10 item 1 and §4.6. Every finding below stands.

Re-grounded: 2026-11-12 against the tree's own research (Jordan: *"Research should have been found in /research or /proposals"*). What changed: (1) of the twenty-four `[M]` marks in §3, nine now carry a tree source at `path:line` for the claim itself, eleven carry one for part of it or for the mechanism (the named particular staying memory-grade), and four stay memory-grade whole, each with the search that found nothing (§15.2; map: `unified/RESEARCH_MAP_INSTITUTIONS_A.md` §2, §4); (2) six statements are corrected where the tree differs (§15.3): **who elects the Confessor under the rule in force** (two seats of one arm, not four Cardinals), the Venetian Interdict's ending, the Templars' suppression, the date of the two-thirds rule inside the tree, the archived design's College of Prelates and off-stage Holy See, and the conclave's enclosure having been suspended; (3) fourteen mechanisms the research describes and this design lacked are added in §15.4, with the executable plan in `proposals/15_INSTITUTIONS_PAPACY_grounding_mechanisms.md`; (4) the §14 null on the game-precedent suite is closed by a search (§15.5); (5) what remains memory-grade is §15.6. No finding of this file is deleted; marks are amended in place and the additions are §15.

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
`offices.yaml` section of world-gen instruments, goal rows, seat rows, three emitted Event kinds on
existing verb rows (`ban.opened`, `detention.opened`, `election.inconclusive`), one fixture
(`penance_weight`) and one typed `terms` roster for a writ (avoid, withhold, render). Every outcome named
is a draw on the one ladder (§6).

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
Two things in the present code and plan are fixed functions. The declared tally (F-PAP-09) is corrected
by its owner, the SC lane's ballot draw (`13_SC_draw_for_unrolled_contests.md`; determinism sweep C-14):
each member's ballot is drawn, his commits its odds; proposal B composes on that and adds only the pass
mark as a share and a graded count. The effect of a sanction on third parties is this lane's (proposal D:
each addressee's answer to a writ of avoidance is his own draw; an oath is never dissolved by rule). Listed for the owning lanes,
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
decree of 1059 gave it to the cardinal bishops `[M → TREE research/social_contest_procedures/04_decision_procedure_catalog.md:101: "cardinals only since *In nomine Domini* (1059)"; the narrowing to cardinal *bishops* stays memory-grade]`; 1179 (*Licet de vitanda*) fixed **two-thirds of the
cardinals** and admitted no appeal, because there was no superior to appeal to `[M → TREE ibid.: "two-thirds required since Lateran III (1179)"; "absolutely no appeal" is Lateran IV c. 24. The decree's name stays memory-grade. The tree disagrees with itself on the date: research/governance/political_hierarchy_standing.md:316 puts two-thirds "under *Ubi periculum*, 1274"; the catalogue's 1179 is the sourced one]`; 1274 (*Ubi periculum*),
after a vacancy of nearly three years, added enclosure: the electors shut in one room, their food reduced
after three days and again after eight, their revenues suspended while the see was vacant (the tree has this
at `governance_modes.md:295`) `[RE-GROUNDED: the catalogue (ibid. :101) has the rations "cut on the fourth and ninth days" and adds what this paragraph lacked: the rule was "suspended in 1276 and reinstated in 1294". The electors lifted their own enclosure within two years. The suspension of revenues stays memory-grade]`. The intricacies that matter for play:

- **Three lawful modes**: scrutiny (a ballot), compromise (the body delegates the choice to a few of its
  number when it cannot agree), and acclamation. After a scrutiny an elector could switch his vote to a
  leading candidate (*accessus*) `[M → TREE ibid. :101: the three modes are Lateran IV c. 24's; *accessus* ran "until the dean disallowed it in 1903". The same entry gives the crowns' exclusive, "from about 1600 … once per conclave", and :103 the canonists' *sanior et maior pars*, under which "the loser could claim to be the sounder part"]`.
- **Capitulations**: from the mid-fourteenth century the electors swore, before voting, a pact binding
  whoever was chosen (share revenues with the college, call a council, limit creations). The elected pope
  usually repudiated it `[M; stays memory-grade: no file treats electoral capitulations. The tree's sourced cousin is Venice's ducal promise, "re-drafted and *lengthened* at every single accession" by a standing magistracy and checked by a posthumous audit (research/governance/governance_modes.md:325-330)]`. A pact made by electors and broken by the winner is a standing grievance.
- **Factions were made by appointment.** A pope created cardinals; his creatures voted as a bloc under his
  cardinal-nephew after his death. The college was the dead pope's patronage, facing the next one.
- **The vacancy was dangerous.** The treasury was looted, offices lapsed, the city rioted, and outside
  powers pressed (1378: a mob demanding an Italian; the same electors later declared their own election
  void for fear and chose another, `conflicts_power_struggles.md:272`).
- **No removal.** A pope could resign (1294) and could not be judged, except, canonists held, for heresy.
  That one exception is the hinge of every schism and council.

### 3.2 The curia: government by document

The pope governed a continent he never saw by letters. The organs `[M; RE-GROUNDED in part. TREE: the chancery's letter form and its entry into the papal chancery (research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:242-253); petitions, where "who carried the petition (proctors, intercessors, well-placed patrons) shaped its success" and "royal petitions and papal/canon-law petitions ran in parallel systems" (:305-307); curial offices bought as toll-posts (research/rise_to_power_roster_system_research_v1.md:493-497); a prelate's appointment fees financed by a banker and repaid from an indulgence drive (:498-501); the curia's hand in a dynastic marriage (research/governance/political_hierarchy_standing.md:176-177). Stays memory-grade: the step-by-step chancery chain and priority by date; annates, common services and *spolia*; the Penitentiary; the Rota; the Consistory; judges-delegate]`:

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

A written, taught, universal law (Gratian's collection and the decretal collections after it `[M; Gratian stays memory-grade. The written procedure below is TREE: Tancred's *Ordo iudiciarius*, c. 1216: *libellus*, *litis contestatio*, "two witnesses = full proof", confession, *positiones* (research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:289), with the tree's own caution that the skeleton was not sourced to a primary text (research/social_contest_procedures/02_inquisition_heresy_procedure.md:15)]`) with a
graded court system: archdeacon, the bishop's official, the metropolitan, Rome; appeal suspended the
sentence. Jurisdiction ran by **person** (every cleric, in any matter: *benefit of clergy*) and by **matter**
(marriage and legitimacy, wills, oaths and perjury, tithes, usury, sacrilege, heresy), on anyone's land.
Procedure was written: a libel, a formal joining of issue, articles put to witnesses examined in private,
publication, sentence. Proof was graded: two eyewitnesses or a confession made full proof; one witness,
documents and common repute (*fama*) made half-proofs. Three ways to start a case: **accusation** (a named
accuser who bore the penalty if he failed), **denunciation**, and **inquisition** (the judge proceeds on
*fama* by his own office; general from 1215 `[M → TREE research/social_contest_procedures/02_inquisition_heresy_procedure.md:15: Lateran IV c. 8's three routes, the accuser's written charge, the accused's sight of "the charges, the witnesses' names and testimony", the notary's record (c. 38); compurgation at :65]`). An accused of good repute could clear himself by oath
with oath-helpers. Kings fought the boundary case by case: criminous clerks (Clarendon 1164 and Becket),
writs prohibiting church courts from lay matters, statutes against appeals and provisions from Rome
(England, 1350s), and finally concordats in which the king named bishops and the pope instituted them
(Bologna 1516; the Spanish crown's patronage) `[M; RE-GROUNDED in part. TREE: Clarendon cc. 3, 7 and 8 (criminous clerks; no tenant-in-chief excommunicated and no land interdicted "unless the king or his justice is first asked"; appeals end with the king), benefit of clergy narrowed by statute, and *De heretico comburendo* (ibid. :64-67); the crown-named Spanish tribunal with appeal to Rome cut (:44); the Venetian lay assessors who hold the arrest and execution gates (research/social_contest_procedures/01_venice_procedure.md:129-131). Stays memory-grade: the writs of prohibition, the English statutes of the 1350s, Bologna, the Spanish patronage of sees]`.

### 3.4 Excommunication and interdict as political weapons

- **Excommunication** was a sentence, in grades. The minor form barred the sacraments; the major form put
  a person outside the community: no one might eat, trade, pray or deal with him, he could not sue, testify,
  hold office or a benefice; after a year unreconciled he was suspect of heresy `[M; stays memory-grade as stated (the grades and the year). The tree has the adjacent facts: excommunicates barred as witnesses in ordinary canon law, and officials excommunicated if they did not carry out a relaxation within five days (research/social_contest_procedures/02_inquisition_heresy_procedure.md:26, :33)]`. It followed three
  warnings (*monitions*) or fell automatically on certain acts. Contumacy, failing to answer a citation,
  was itself ground for it, which is how absent parties were reached. From 1418 only a person **denounced
  by name** had to be shunned `[M; stays memory-grade: no file holds the 1418 rule. The sourced cousin is the imperial ban, with "a contagion clause punishing anyone who shelters the target" and teeth only "as strong as" its enforcement (.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:79, HRE-6 at :192)]`: the sanction bound third parties only once published.
- **Its force was other people's compliance.** In England the bishop certified an obstinate excommunicate
  to the royal chancery after forty days and the king's officers arrested him `[M; the forty-day certification stays memory-grade. The dependence on the secular arm is TREE: the 1401 statute under which "sheriffs and mayors must attend when the diocesan requires", so that "relaxation became a compulsory duty of royal officers at the bishop's call"; and its reverse, Philip IV ordering his seneschal "no longer to obey inquisitors' commands to arrest", after which arrests "which had been taking place every week" stopped (research/social_contest_procedures/02_inquisition_heresy_procedure.md:67, :71)]`: the secular arm.
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
  the clergy to go on officiating, expelled those who obeyed Rome, and won `[M → TREE research/social_contest_procedures/01_venice_procedure.md:155-170, corrected: not "won". The Republic's *protesto* of 6 May 1606 declared the censures null and ordered services kept; "most clergy and orders obeyed Venice; the Jesuits, Capuchins and Theatines resisted" and were expelled; **France mediated**; a French cardinal took custody of the two priests on 21 April 1607 and the interdict was lifted; "Venice keeps its laws"; the Jesuits stayed banned. The tree could not verify the settlement's terms beyond the handing over of the prisoners. England 1208-14 is TREE research/fa_se_historical_precedent_research_v1.md:148; the interdict after the hanging of the Archbishop of Pisa, 1478, is research/governance/conflicts_power_struggles.md:257; the merchant clause of Florence 1376 stays memory-grade]`. Mitigations multiplied
  until an interdict was an inconvenience. Overuse was the decay.
- **Absolution** required satisfaction or security for it; great cases were reserved to the pope, which
  brought the penitent, or his proctor and his money, to the curia.

### 3.5 Councils

A general council was called by the pope and legislated with him. The fourteenth-century crisis turned it
into a rival: when two and then three lines of popes each held a valid-looking election, the only body
that could judge the head was a council, called by cardinals and princes (Pisa 1409, Constance 1414-18,
`conflicts_power_struggles.md:272`). Constance voted **by nation**, not by head, to cancel the Italian
majority, declared that a council holds its power directly and binds a pope, and ordered councils at fixed
intervals `[M; voting by nation and the two decrees stay memory-grade. TREE has Constance forcing "all three claimants to resign or be deposed" as "an extraordinary, one-off supra-conclave mechanism" (research/governance/conflicts_power_struggles.md:272), its trial of Hus under a broken safe-conduct and the Bohemian nobles' refusal of its summons (research/social_contest_procedures/02_inquisition_heresy_procedure.md:89), and a council deposing an emperor "with no immediate practical effect" (research/governance/political_hierarchy_standing.md:240)]`. Basel sat for eighteen years, deposed a pope and elected the last antipope. Popes answered
by treating with kings directly (the concordats) and by forbidding appeal from a pope to a future council
(1460 `[M; stays memory-grade, with Basel]`). The appeal to a council remained every aggrieved king's threat.

### 3.6 Investiture, patronage, benefices, simony

- **The proprietary church.** A lord who built and endowed a church owned it and appointed its priest; a
  king did the same with bishoprics, handing over ring and staff. The reformers named three evils: simony
  (buying office), clerical marriage (which made benefices heritable), lay investiture. The quarrel of
  1075-1122 ended in partition, not victory (`governance_modes.md:208-215`): the Church gave the spiritual
  symbols, the ruler the lands and rights; elections were held in the ruler's presence.
- **Election, licence, assent.** A cathedral chapter elected its bishop, with the king's licence to elect
  and his assent after; the king held the lands of a vacant see and took their revenue (regalian right),
  so a king profited by delay `[M; the regalian right over a vacant see stays memory-grade. TREE: a prince-bishop "selected by cathedral chapter" (.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:81) and the capture of such a chapter before the vacancy, "College seats owed" that count "only if/when a vacancy fires" (HRE-2, :188; kept at the closure, tier3_proposal_status_closure.md:96)]`.
- **Advowson.** The patron of a parish presented a clerk; the bishop instituted him. Presentation was
  property: inherited, sold, sued for in the king's court (the tree names it: FASE research). The office was
  the Church's, the gift of it a layman's.
- **The benefice.** An office with an endowment (glebe, tithe, fees). With cure of souls it required
  residence; without, it was income. Pluralism (several at once), non-residence, the hired vicar on a
  fraction of the income, *commendam* (the revenues of an abbey given to an outsider), and appropriation
  (a monastery as perpetual rector) turned benefices into a currency for paying officials and kin `[M; RE-GROUNDED in part. TREE: the plural hold bought on credit (research/rise_to_power_roster_system_research_v1.md:498-501); benefices "calcifying into heritable property" (research/governance/political_hierarchy_standing.md:20, :180); and, inside Valoria, the unfilled benefice as a place with "no priest, so … no channel" (proposals/2026-08-30-play-space-coverage/03_seasons_church.md:314-321). *Commendam* and appropriation stay memory-grade]`.
- **Provision and reservation.** From the thirteenth century the pope provided to benefices directly and
  reserved whole classes to himself; *expectatives* promised the next vacancy. The curia became the
  market for careers, competing provisions for one living were litigated in the Rota, and the local patron
  or chapter often simply installed its own man. Whether a papal provision *took* depended on the ground.
- **Simony** never ended; it changed form: fees, compositions, services, loans, the sale of curial
  offices as a public debt. The line between a fee and a price was what reformers and satirists argued over.

### 3.7 Income: tithes and indulgences

The tithe was a tenth of produce owed to the parish, divided in theory among bishop, clergy, fabric and
poor, in practice largely captured by monasteries and lay impropriators; disputes over it filled the church
courts `[M; the fourfold division and its capture stay memory-grade; that tithes were church-court business is TREE research/fa_se_historical_precedent_research_v1.md:147, and an order's branches paying a share upward (*responsions*) is research/proactive_governance_scale_research_v1.md:79]`. Above it sat the papal levies of §3.2. Indulgences began as remission for crusaders, were
extended to those who paid for one, to jubilee pilgrims, to the dead; preaching them was farmed to
licensed collectors, and the proceeds were often pledged in advance to a banker against a prelate's debt
for his own appointment fees `[M → TREE research/rise_to_power_roster_system_research_v1.md:498-501 (Albrecht of Brandenburg's purchase of Mainz, after MacCulloch): a financier "fronts the dispensation cost", the debtor's conduct bends "toward whichever move maximizes Treasury flow to the Financier", and the failure is contagion from "the Fuggers' exposure to the Habsburg/papal debt web". The earlier history of indulgences stays memory-grade]`. The system's revenue and its discredit came from the same act.

### 3.8 The orders and their autonomy

- **Monastic**: each house self-governing under a rule and an elected abbot; reform came by federation:
  one mother-house whose abbot ruled dependent priories and which was **exempt from the local bishop and
  subject to the pope alone** (the Cluniac pattern), or a general chapter of all abbots with mutual
  visitation (the Cistercian) `[M → TREE for the Cistercian form: the *Carta Caritatis*, an "annual General Chapter & Visitation" in which the inquiry is turned "inward" on "a *branch head*" (research/proactive_governance_scale_research_v1.md:72, a self-labelled sketch on Wikipedia); a unified monastic rule imposed by synod, 816-817 (research/governance/governance_modes.md:166). The Cluniac pattern stays memory-grade]`.
- **Mendicant**: mobile preachers organised in provinces under an elected general, licensed by the pope to
  preach, confess and bury in any diocese, in competition with the parish clergy for souls and fees.
- **Military**: knights under vows with their own priests, lands and banks, exempt from bishops and tithes,
  answerable to the pope. The Templars were destroyed in 1307-12 by a king who owed them money, using
  the Church's own inquisitorial procedure and a compliant pope `[M → TREE research/social_contest_procedures/02_inquisition_heresy_procedure.md:50-56, corrected. The lever was "heresy, the one exception to the Order's immunity"; the Inquisitor of France was "Philip's confessor", "a church office held by a crown man"; the pope was not simply compliant: he "suspended the inquisitors (Feb 1308)", set a papal commission to hear the Order's defence, and was overtaken when a provincial council burned 54 defenders as relapsed ("Retraction made relapse, which silenced the defenders"); the Order ended in 1312 "by administrative act, not verdict", its goods going to the Hospitallers less 200,000 livres the king took as costs. Control: "Aragon and Portugal found no fault; Cyprus acquitted all 76 at first". The king's debt to the Order stays memory-grade]`: exemption protects an order from
  bishops, not from the power that protects it.

Exemption was the papacy's standing army inside every diocese and every bishop's standing grievance.

### 3.9 Inquisition

Papal inquisitors, mostly friars, commissioned from the 1230s to proceed by *inquisitio* against heresy
`[M → TREE ibid. :21-36 for this whole subsection, stage by stage: papal inquisitors "from 1231"; a month of grace; citation by the parish priest; names withheld, with the safeguard that the accused may name his mortal enemies and "if the accuser is among them the charge fails"; coercion from *Ad extirpanda* (1252) and its evasions, yet "no torture in d'Ablis's register, one case in Fournier's"; a *consilium* of thirty to eighty men consulted "on the abstract case without the name", "usually followed, and milder"; the public sermon; the sentences and their scale (leads); confiscation, on which "Sources conflict". What the tree adds is in §15.4 items 6 to 9]`. Procedure: arrival and sermon; a **period of grace** in which voluntary confession earned light
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
came late `[M; RE-GROUNDED in part. TREE: the cardinal-legate "with full powers in the name of the Pontiff", beside a lay Rector, formally recallable, and the Romagna legation split when it grew too heavy (.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:113, IT-5 at :211); a nuncio at Venice from 1544 who sat on the Holy Office's bench (research/social_contest_procedures/01_venice_procedure.md:129-130). Procurations and the refusal of entry stay memory-grade]`. Kings refused legates entry, or demanded that only a native archbishop hold the legation.

### 3.12 Schism and anti-popes

A schism needed a doubtful election and a power that preferred the doubt. Emperors installed anti-popes
after deposing popes (1080, 1159); a double election in 1130 was decided by which kings recognised whom;
1378 split Europe along existing alliances into *obediences*, each with its own college, curia and tax
collectors `[M; RE-GROUNDED in part. TREE: an emperor "installing antipope Clement III" (research/governance/governance_modes.md:212); 1378 as a split of the electors themselves, "structurally unresolvable dual sovereignty" (research/governance/conflicts_power_struggles.md:272); the ruler's counter-lever of sponsoring "a rival claimant up the *same* religious ladder" so that every later check must "resolve which co-signer counts" (research/rise_to_power_roster_system_research_v1.md:536); the Schism's "asymmetric obediences" (research/fa_se_historical_precedent_research_v1.md:306). 1130, 1159 and the subtraction of obedience stay memory-grade]`. Ways out, in the order tried: both resign, both submit to arbitration, a council. Kings
used the interval: *subtraction of obedience* withdrew a kingdom's church from both claimants and left its
revenues with the king.

### 3.13 The relation to secular rulers

The theory moved from two powers each supreme in its sphere, to the spiritual judging the temporal *by
reason of sin*, to a claim of direct lordship that kings answered with force (Anagni, 1303) `[M; the three-stage theory and Anagni stay memory-grade. TREE has the same king's quarrel with Boniface VIII as his motive for checking the inquisitors (research/social_contest_procedures/02_inquisition_heresy_procedure.md:71), the maximal claim itself in the *Dictatus Papae* (research/governance/governance_modes.md:210), and the limit of the claim: a ruler who took the imperial style "without a Rome coronation", "a deliberate rupture that decoupled imperial legitimacy from papal ratification for good" (:190)]`. The
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

---

## 4. Adaptation to Valoria: what is kept, what is changed, and why

### 4.1 Keep / change

| historical mechanism | kept as | changed, and why |
|---|---|---|
| apex elected by a college, two-thirds, enclosed | the Confessor's seat filled by the Church's own bench (CR-35) under a `conclave` row with `quorum_share: [2, 3]` | a commitment does not decide: each elector's ballot is a draw whose odds his commitments set (the SC lane's ballot; standing rule). The four Cardinals are also the heads of the four arms, so an election is a contest among the Church's own departments, which is truer to Valoria's four-Cardinal structure than a college of courtiers. `[RE-GROUNDED, corrected: under CR-35's rule the bench is "the live seats of the vacant seat's faction whose grant carries `determine`", and at build only `off_cardinal_justice` and `off_senior_inquisitor` carry it (map §5, E-M1). The plan says so: "only the Cardinal of Justice and the Senior Inquisitor elect the Confessor, so three of the four Cardinals do not vote; an authored electors list is AX-6's alternative and is Jordan's content" (workplans/valoria_master_workplan_v11_part12.md:366), docketed "CONFIRMED AT THE DEFAULT" (proposals/2026-11-04-content-parameters-docket/11_workplan_owed.md:53). The contest "among the Church's own departments" is therefore not what the row gives today. §15.3 C-1]` |
| government by rescript; the curia's fee-taking chain | the `dispensation` Record and `petition`, issued through a seat, answered by `comply` / `evade / defy` / `construe` | the clerk-by-clerk chain is **not** modelled as offices. It is carried as what it did: delay (a sitting is a season), cost (stores moved by `transfer` to the seat's rung) and the proctor (an advocate, `interposed: person`). A chain of seven seats that each stamp one paper is overhead with no choice in it (NERS-E against N: nothing dies if cut) |
| jurisdiction by person and by matter | CR-60's `scope:` (the bench's ground) plus goal rows that say which deeds the Church acts against | jurisdiction by *matter* is not a gate. A Church bench may hear whatever is docketed before it; what it *seeks* is set by its goals (`deed_doers`), so a contest of jurisdictions is two benches each docketing the same person, which is what happened |
| three ways to open a case | CR-60's two rites (accusatorial, inquisitorial); `petition` then `open_case`, or `open_case` on the bench's own claim | denunciation folds into accusation with the accuser concealed (`conceal`), no third rite |
| excommunication, minor and major | the `ban` (legal exclusion, existing) and a published writ of avoidance (social exclusion, a `dispensation`) | no automatic sentence. *Latae sententiae* is a fixed function of state and is refused by the standing rule; every sentence is a determination |
| release of subjects from their oaths | CR-88's duty decline does not bar a person who has complied with a writ of avoidance from his own `release` of his tie to the excluded man; whether he takes it is his own score | never a dissolution. An oath ends only by its owner's `release` |
| interdict | a writ addressed to the Church's own seat-holders in a place, withholding the services the engine models: `tend`, alms (`transfer`), teaching (`train`), judging | the rites themselves are not modelled, so the interdict withholds what the Church does that the engine can see. Canon makes exactly these the Church's hold on the realm: *"hospitals, charities, dispute resolution"* (`canon/03_canonical_timeline.md:68`) |
| absolution, penance, reservation | `pardon` through the seat that is the ban's object (existing rule), after a termed `oblige` of the penitent | reservation is already the engine's rule: only the sentencing seat closes its own edge |
| lay investiture and its settlement | `may_fill` as built lets a lord with purview fill a Church seat on his ground; a seat row's `patronage:` says whether that is lawful there | the settlement is data per seat, not a realm-wide rule: Himmelenger's seats are the Church's own, a see on ducal ground is contestable |
| benefice | a seat plus the stores of its rung it may `requisition` and `transfer` | no separate "living" object. Title and grant are already two things in the engine (a `hold` on an Office, stores on a Rung) |
| tithe; annates; indulgences | a standing writ from the Cardinal of Prudence to the sees; each see's `requisition` and `transfer` | annates and indulgences are **not adopted**: annates is a second levy on the same flow; indulgences sell a metaphysical good the simulation must not price (canon guard, §4.2). The cut costs the Reformation's trigger; Valoria's own trigger is the Thread truth |
| exempt orders | a house whose head is sworn (`oblige`) to the head seat, so the head seat's purview runs through it (the oblige clause) | none: this is the existing primitive, and the Löwenritter's oath to the throne is its precedent |
| inquisition and its register | `open_case` by the Senior Inquisitor's bench; `interview`, `interrogate`, `research`; the case file (CR-61) as a Record that outlives the case | torture is not a verb. Pressure is custody (`detain`) and the `interrogation` row |
| temporal power | Himmelenger and the Church's holds; the `theocracy` ending; CR-89's band triggers | the Papal States' vicariate system is left to the lane that designs holdings; the Church's seizure is CR-89's and CR-91's |
| legates | a seat the Confessor founds on another's ground with a term (`establish`, FA-P3); the Archbishop's Representative is the resident form | procurations become the legate's `requisition` on the ground he is sent to |
| schism | a second head seat founded by a dissenting part of the bench, persons re-committing | a faction is a Proposition plus its commits, so a schism is the general split, not a Church rule. Design-first (§11 batch 6) |
| councils | a `general_council` row whose bench is every Church seat granting `determine` | whether it can judge the Confessor is Jordan's (§13) |
| anointing | the `consecration` row and its `resolution` | it confers nothing; §2 |

### 4.2 Canon guard (method of `skills/valoria-canon-guard`; constraints read at `canon/02_canon_constraints.md:42-56`)

| constraint | status | note |
|---|---|---|
| P-03 rendering is consciousness-performed; information asymmetry is the mechanic | PASS | consecration, sanction and commemoration act only on persons' ledgers, stances and choices. No rite changes a world quantity |
| P-04 monstrosity is ontological, not moral | PASS | the Church's benches judge persons' deeds; no rule assigns moral valence to a practitioner or a monstrous being. The Church's *belief* that they are deluded is a goal row and a conviction, never an engine fact |
| P-08 the epistemological barrier is inaccessibility, not suppression | PASS, with a guard | nothing here lets study, a trial, a seized text or an archive give a non-sensitive Thread-level knowledge; the archive holds Records whose content a non-sensitive reads as devotional (the Seam Texts' two readings stay FI's and WR's). The Church *reinforces* the barrier and is never its cause: burning the archive ends no barrier |
| P-13 the Forgetting is rendering failure | PASS | untouched |
| P-01, P-11, P-12, P-14 (co-movement of Thread operations) | not engaged | no Thread operation is added. An inquisitor's `thread_read` (NPC-004's hidden sensitivity) is WR's module |
| P-02, P-05, P-06, P-07, P-09, P-10, P-15 | not engaged | |
| GD-1 sole victory | PASS | `theocracy` stays an ending, not a victory |
| world truth: *"Solmund did not found the Church"*; consecration as *interpretation* | PASS | the design never makes divine favour true. Indulgences are refused for this reason: a priced remission would need the simulation to hold a fact about grace |

### 4.3 The nine requirements

R-01 propagation and R-02 consequence: a sentence, a consecration, a vacancy and an interdict each write
something another person later reads (a Tenure, a Record, a claim) and decides differently on. R-04
strategic acts: the head seat's appointments, sanctions, levies and legations are its management verbs.
R-05: no verb is added; twelve gain Church content. R-07/R-08: every effect on a third party passes
through that person's own ledger and conviction; a far parish may never hear of a sentence. R-09: every
procedure is a draw (§6).

---

## 5. The play-facing model: primitives

| primitive | exists as | Church use | new? |
|---|---|---|---|
| seat | `Office` on an anchor, with remit, conferral, revocation, binds | Confessor, Cardinals, Inquisitor, the Representative; sees; a legate's termed seat; an order's house | rows only |
| body | `office_bodies` | Holy See and the four arms | none added (a new body name is canon's to give) |
| procedure | an `arrangements.yaml` row | `conclave`, `consecration`, `general_council`; the three existing Church rows gain `standard:` (SC T2) | three rows; one key `quorum_share` |
| instrument | `Record` of a rostered kind | `dispensation` (charter, citation, sentence published, writ of avoidance, interdict, tithe writ), `petition`, `resolution` (CR-36: attestation, motion), the case file (CR-61) | one typed `terms` form (avoid / withhold); no kind |
| claim | `Claim` in a ledger; deed claims; content claims of a held Record | fama; the deed ledger; what a sermon tells | none |
| obligation | `oblige` Tenure with a term | an order's oath to the head seat; penance | none |
| patron-client edge | `oblige`; the conferrer of a seat (the creating act of a `hold`) | a Cardinal's creatures: the persons whose holds his `confer` opened, read off the act store when someone asks who made whom | none; a Query when a reader needs it |
| treasury | `Rung.stores`, moved by `requisition` / `transfer` | the tithe to Himmelenger's store; alms out of it | none |
| jurisdiction | `Office.rung` (acting), `Office.scope_rung` (judging, CR-60's `scope:`), the oblige clause | Himmelenger; sees; realm-wide judging; reach through sworn houses | none |
| sanction | `ban`, `detain`, closed by `pardon` | sentence; penance; absolution | two Event kinds on existing rows (`ban.opened`, `detention.opened`) |
| right of appointment | `may_fill` (purview) | Himmelenger's own seats; contestable sees | **one key**, `patronage:`, with a closed roster |
| world-gen document | none (the build mints only `works`) | the settlement charter; the three founding attestations | **one section**, `offices.yaml: instruments:` |

**Cut tests for the two new things.** `patronage:`: without it every Church seat is a royal appointment
(today, F-PAP-02) or, if `may_fill` simply gained a same-faction clause, no lay lord could ever invest a
bishop and the investiture contest could not occur; the key is what lets one seat be the Church's own and
the next be fought over. `instruments:`: without it no world begins with a charter, an attestation or a
standing writ, so every institution starts with no past, and Jordan's order of accomplishment has no
owner code reads (§0.05).

**Not added, and why.** A piety or influence number (refused by Layer 1 and already translated by the
plan); an `excommunicate` verb (it is `determine` under a row); an `interdict` verb (it is `issue`); a
`consecrate` verb (it is `determine` under a row); an `elect` verb (CR-35: an election is `determine`);
simony as a verb (it is a `covenant` and a `transfer` around a `confer`); a clergy flag on a person (a
cleric is a person holding or sworn to a Church seat, which `faction_holding` already answers).

---

## 6. Each procedure as a draw

One ladder (Overwhelming, Success, Partial, Failure), one pool reader, one obstacle
(`difficulty + opposition + standard + subject + stakes + hostile − favourable`, the SC lane's closed
roster; this lane adds **no term**). "Check" is an eligibility test that decides only whether the act may
be attempted. Draw shapes for `confer`, `revoke`, `pardon`, `establish`, `issue`, `succeed` are the verb
lane's (`14_VERBS_BINDING.md` §0.2); this table names the Church's rows and which existing terms carry
personality, affiliation, office, evidence and publicity.

| id | procedure | who acts, verb, venue | check | pool | obstacle terms | O / S | Partial | Failure (recoverable) | written; who reads it |
|---|---|---|---|---|---|---|---|---|---|
| P-1 | **Election of the Confessor** | each Church elector present casts a ballot under `conclave` (the SC lane's ballot draw, `13_SC_draw_for_unrolled_contests.md`), chapter house at Himmelenger, on a candidate's petition naming the seat | the seat is vacant; a docketed petition names it | each elector's own (`determine` pool) | per ballot: `plain` + the row's `standard` (demanding); his own live commits on the matter as favour or hostility (the SC ballot's odds operand) | fors ≥ two-thirds of ballots cast (`quorum_share: [2, 3]`): the candidate holds the seat; the division is recorded | fors a majority short of two-thirds: no election; the candidacy stays docketed for the next sitting (`election.inconclusive`) | fors not a majority: the candidacy is dismissed; the seat stays vacant; other petitions stand | `hold` Tenure; `tenure.opened`; the division where `records_dissent`. Every Church seat-holder (his superior changed), the Crown (whom it must treat with), the losers (grievance) |
| P-2 | **Appointment to a Church seat** (a benefice granted) | the Confessor (or, where `patronage` admits, a lay lord), `confer`, his own venue | conferral basis; `patronage` admits the seat exercised | conferrer's | `difficulty` routine; `reception` of the seat's body toward the conferee; `standing`; `opposition` the incumbent when displacing | seated | provisional | not seated, `appointment.resisted` | the `hold`; the conferee's grant. The losers; the other claimant to the gift |
| P-3 | **Consecration / attestation** | a Church bench, `determine` under `consecration`, cathedral, on the claimant's petition naming the seat | a docketed petition; the bench sits over the claimant (CR-60) | determiner's | `standard` demanding; `evidence` = the claimant's cited deeds and Records minus standing answers; `reception` of the bench toward him | a `resolution` naming seat and claimant, held by the determiner | a `resolution` whose terms attest half the cited entries (the first half in cited order) | none minted; `matter.dismissed`; he may petition again with more | the Record. Any later hearing that admits `record`; whoever researches or is told of it |
| P-4 | **Sentence of exclusion** | a Church bench, `determine` under `excommunication_deliberation` or `inquisition_hearing` | docketed; bench sits over the party | under `inquisition_hearing` the determiner's; under the declared row each member's ballot (the SC ballot draw), passing at two-thirds of ballots cast | `standard` (demanding / hard); `stakes` (`ban`); `opposition` the party's score; `evidence`; `reception`; `plea` if he appears and speaks; per ballot, the member's own commits | `ban` opened; O adds the pursuit move the row already writes | band-keyed (SC-P4): an `oblige` of the party to the bench (monition and penance), no exclusion | acquittal (SC-P6); a failed sentence is itself news (the martyr) | `ban` Tenure; `ban.opened` Event. `confer` and `oblige` (existing); every hearer's judgement of the **bench**, by his own lean times his bond to the excluded man (IN-58's paired rule) |
| P-5 | **Publication and avoidance** | a Church seat with `issue`, `issue`, to the faithful it reaches | authority; executors exist | issuer's | `regard`, `standing` (verb lane) | writ minted with `force` = band | force Partial | a dead letter | a `dispensation` whose terms are `{avoid: person, verbs: […]}`. Each addressee, as P-6 |
| P-6 | **A believer's answer** | each addressee, `comply` / `evade / defy` / `construe` | a claim of the terms is in his ledger (FA-P1) | his own (resolve; conviction as advantage through CHAR's ground rule) | `difficulty` by the writ's `force`; `regard` of him toward the excluded person as a hostile term (a tie makes shunning hard); `stakes` if he is sworn to him | shuns: declines the named verbs toward him while the ban lives; O also tells others | shuns in the open, deals in private (`conceal` forms) | defies; `compliance.withheld`, a deed the issuer's goal acts against | his own claim of his answer; the excluded man's options (who still trades, tends, serves) |
| P-7 | **Interdict** | the head seat or the Cardinal concerned, `issue`, to Church seat-holders and sworn in a rung | as P-5 | as P-5 | as P-5 | writ with terms `{withhold: [tend, transfer, train, determine], at: rung}` | weak force | dead letter | each addressee answers as P-6; residents' own claims of shortfall and untended harm (`stability`), then their regard for the ruler who caused it |
| P-8 | **Absolution** | the sentencing seat's holder, `pardon` | he sits over the penitent; the edge's object is his seat | his | `stakes` (the restraint), `standard`, `reception`; favourable `evidence` if a termed `oblige` of the penitent to that seat has matured (penance done) | restraint ends | commutation (the verb lane's shape) | `pardon.denied`; ask again | `ban.ended`. The same readers as P-4, reversed |
| P-9 | **Discipline of a Church officer** | the head seat's holder, `revoke` (basis `head_of_faction`, if ruled) | the basis | his | `regard`, `standing`, `stakes` (`hold`), `reception` of the seat's body, `opposition` the holder | unseated | unseated, no disposal | he holds, `revocation.resisted` | Tenure closed; a vacancy (P-2) |
| P-10 | **Appeal** | the party, `petition` to a higher Church bench; that bench, `determine` | the row's `appeal_basis`; CR-59 | appellate determiner's | `standard`; `evidence` including the first bench's case file; `reception` | the first disposal is closed | it is termed | it stands; the appeal is spent for that file | the first bench's standing with its superiors |
| P-11 | **The tithe** | Cardinal of Prudence, `issue` to the sees; each see-holder, `comply` by `requisition` then `transfer` | remit; stores cover | issuer's; each complier's | P-5's; P-6's with `stakes` the settlement's shortfall | rendered | part rendered | withheld | stores at the see's rung and at Himmelenger; alms capacity; the lord whose settlement was drawn on |
| P-12 | **Founding a see or sending a legate** | the head seat, `establish` on a rung his purview or `patronage` reaches | conferral basis; a rung | his | `reception` of the holding's seated persons, `standing` | founded with its row's remit | founded with half the remit | `office.unrecognised` | a new seat; a vacancy (P-2); the local lord's options |
| P-13 | **Council** | each Church seat granting `determine`, a ballot under `general_council` | a docketed motion | each member's | as P-1, `standard` hard | two-thirds of ballots cast: the `resolution` it was asked for | a majority short of it: the motion stays docketed | not a majority: dismissed | a `resolution`: the motion CR-37's shape needs |

No row decides by rank or seniority, and none by a count of prior commitments: where a body votes, each
ballot is a draw whose odds its caster's commitments set, and the count of drawn ballots is arithmetic.
The proofs, the venue's standard and the bench's disposition are terms; the die decides; a failure leaves
the matter re-attemptable or dismissed with the party free to return.

---

## 7. Verbs and contests

No new verb. Mapped to the 67 rows (`engine/season/verb_table.yaml`):

| verb | Church content it gains | owner of the row's build-out |
|---|---|---|
| `determine` | three rows (`conclave`, `consecration`, `general_council`); `ban.opened` / `detention.opened` earned per edge | SC; `14_VERBS_BINDING.md` §3; this lane's B, C, D |
| `confer` | the `patronage` clause in `may_fill` | `14_VERBS_BINDING.md` §1; this lane's B |
| `revoke` | `head_of_faction` basis (if ruled); `ban.opened` on its disposal | `14_VERBS_BINDING.md` §11; FA §11 item 3; B |
| `establish` | sees and legations as rows | `14_VERBS_BINDING.md` §5; E |
| `issue` | the avoid / withhold `terms` form | `14_VERBS_BINDING.md` §6; FA-P1; D |
| `comply`, `evade / defy`, `construe` | answers to a writ of avoidance, an interdict, the tithe writ | FA-P1; the social verb lanes; D |
| `pardon` | penance as favourable evidence | `14_VERBS_BINDING.md` §9; D |
| `petition`, `open_case`, `convene`, `speak`, `argue` | candidacy; consecration; accusation; appeal | SC; the social verb lanes |
| `oblige`, `release` | an order's oath; penance; a vassal leaving an excluded lord | the binding lane |
| `tell`, `research`, `create_record`, `give`, `conceal`, `forge`, `destroy_record`, `seize` | the archive and the deed ledger | FI; `12_ARCS_cited_evidence.md`; C |
| `requisition`, `transfer`, `tend`, `train` | tithe, alms, hospital, school: the services an interdict withholds | the material verb lane; SE |
| `covenant` | concordat; election capitulation; a simoniacal bargain | the binding lane |
| `arrest`, `interrogate`, `interview` | the Inquisitors' procedure | SC, FI |

Contests: every Church contest is a `determine` (prize `a proposition`, or `a seat` when it disposes a
`hold`) or one of the verb lane's contested binding acts. No new prize.

## 8. Tuning dimensions

All in the SC lane's tables (`proposals/13_SC_tuning_tables.md`); this lane supplies rows, not tables.

| dimension | where it enters | Church rows (first values, each `[ASSUMPTION; Jordan to correct]`; unit: `difficulty_levels` member) |
|---|---|---|
| venue | T2 `standard:` on the arrangement row; `venue_min_rank` | `conclave` demanding; `consecration` demanding; `general_council` hard; existing: `excommunication_deliberation` demanding, `inquisition_hearing` hard (T2's own values). Sweep: each ± 1 level in a planted hearing |
| personality | the determiner's and the answerer's pools; CHAR's ground rule (`02_CHAR_which_ground_moves_whom.md`) as advantage; pursuits in `deed_term` | no Church value; a hearer judges the bench for a sentence by his own lean on `deed:ban.opened` (alignment cells, proposal D) times his bond to the man sentenced |
| affiliation | `Person.conviction` through CHAR's advantage source; `opinion` of the Church in `reception` | none stored here |
| office | the governance vocation of the seat (FA-P6); `standing`; who may attempt (remit, `patronage`, `scope`) | seat rows |
| evidence | T5 `evidence` with the row's `proofs:` as admission filter | `consecration` admits `[record, testimony, oath]`; `conclave` `[]` (an election hears no proofs: it reads the vote); `general_council` `[record, testimony]` |
| publicity | the row's `floor` (open / closed) raising `standard` one level in T2's sweep; `disposal_reach`; the chronicle channel | `consecration` open (a public rite: its failure is public); `conclave` closed |
| season | none as a term (T-table R-6). Sittings are seasonal; a vacancy's cost accrues by what the vacant seat cannot do | none |

`quorum_share` (proposal B): unit, a ratio of ballots for to ballots cast; owner `arrangements.yaml`;
first value `[2, 3]`; sweep `[1, 2]`, `[2, 3]`, `[3, 4]`. It is arithmetic over drawn ballots.

---

## 9. Emergent narrative with no player

Each line: the story; the conditions; the instrument that could show it and could fail.

1. **The long vacancy.** The Confessor dies; the four arms each prefer their own; no candidate holds
   two-thirds; sittings fail; meanwhile nobody can appoint, discipline or absolve. Conditions: P-1's
   ballots falling short of two-thirds in successive seasons. Instrument: seasons from `person.died` of the
   holder to `tenure.opened` on `off_confessor`, per seed; it fails if every seed elects in one season
   (no politics) or none ever does (dead end).
2. **The contested see.** A see on ducal ground falls vacant; the Duke invests his man; the Confessor
   provides another; each `confer` displaces the other's with the incumbent as opposition. Instrument:
   count of `tenure.opened` on one seat with alternating `Act.via` factions; fails at 0.
3. **The sentence that makes a martyr.** A Failure at P-4 against a popular lord is told abroad as a deed
   of the bench. Instrument: mean `regard` of the party's bonded hearers toward the determining
   seat-holder before and after, for a failed and for a successful sentence, against a control with no
   sitting.
4. **The excluded king.** P-4 succeeds on a head of faction; P-5 reaches his vassals; each answers by his
   own draw; for one who complies the duty decline no longer bars his `release`, and those who already
   hold a grievance take it; those who do not, defy the writ or comply and stay.
   Instrument: `commitment.ended` / `tenure.closed` on `oblige` edges to his seats within N seasons of
   `ban.opened`, split by the releaser's prior grievance; it fails if release does not depend on prior
   grievance (the sanction would be a switch).
5. **Canossa.** The excluded man swears a termed `oblige` to the sentencing seat; at term the seat pardons;
   the vassals' added origin is gone. Instrument: `ban.ended` preceded by a matured `oblige` of the same
   person to the same seat.
6. **The interdict that fails.** A see-holder whose regard for his lord outweighs his duty defies P-7 and
   keeps the hospital open; the head disciplines him (P-9) or does not. Instrument: `compliance.withheld`
   by a Church seat-holder on a withhold writ.
7. **The refused consecration** (the Consecration Triangle). A claimant with the second-ranked roll
   petitions; the bench's reception is hostile; Failure. Instrument: `matter.dismissed` under
   `consecration` for a party who holds a seat or a claim to one.
8. **The burned roll.** Someone destroys or forges a founding attestation; the next contest is argued on
   testimony and copies. Instrument: `record.destroyed` or `record.forged` on an instrument of kind
   `resolution`, then the `evidence` term of the next hearing that would have cited it.
9. **The over-mighty arm.** A Cardinal's sworn house grows; he acts without the head; the head cannot or
   will not strip him (the archived *Jarnstal Drift* without a counter). Instrument: acts through a
   Cardinal's seat that a held writ of the Confessor forbids (`compliance.withheld` by a Cardinal).
10. **The inquisitor's file.** A case file kept for seasons convicts someone its first subject named
    (ARC-41, NPC-004). Instrument: a `determine` whose cited items include a Record created under an
    earlier matter.
11. **Theocracy by consecration.** With CR-89's bands, the Church attests one of its own and a succession
    contest goes to him. Instrument: `endings_reached` reports `theocracy`.
12. **Schism** (design-first). An election inconclusive for seasons, or carried by a margin the losers
    refuse; the dissenters found a second head seat; persons re-commit. Instrument: two live seats of post `Confessor` held under different faction
    Propositions.

---

## 10. Provided arcs and characters that depend on it

From `audits/12_ARCS_adjudication.md` (rows opened: ARC-21, ARC-36, ARC-37, ARC-41, NSC-04, NPC-039,
NPC-040; the M-table) and `engine/season/npcs.yaml` (wants read at the row).

| case | need (short) | hardness | represented today? | this design's carrier | proposal | depends on |
|---|---|---|---|---|---|---|
| ARC-21 The Excommunication | a formal contest with more than two outcome tiers, each a different consequence set; a failed challenge weakens the challenger | core | no: one consequence for three bands (SC F-SC-06) | P-4's band-keyed disposal; Failure as acquittal and news | D | SC-P4, SC-P6 |
| ARC-36 The Tithe That Fed the Enemy | an NPC optimising a levy; an investigative branch detecting the derivative marker | core | no levy route | P-11; the Inquisitors' `open_case` on a claim of where stores went | E | CP-T08-07, the material verb lane |
| ARC-41 The Inquisitor's Unravelling | rigorous documentation that later convicts its maker | core | no case file | the case file as a Record (CR-61); P-4 | D | CR-61 |
| NSC-04 the Church exposed | exposing an institutional actor's secret partnership | core | partial (`tell`, inquiry verbs) | a deed claim the Church's own discipline (P-9) or a council (P-13) acts on | B | FI-02 |
| NPC-038 Olafsson | a branch's named superior whose authorisation is a precondition above a severity threshold | core | no | a sentence of `ban` needs the declared row, whose bench he sits on and whose sittings he convenes; his removal (P-9) changes what the body does | B, D | FA §11 item 3 |
| NPC-013 Tormann | a repeatable seasonal action improving a faction-wide resource, scaling with the territories applied to | core | no | P-11: one writ, as many renders as there are sees | E | sees authored |
| NPC-034 Linder | the sole lawful conduit of a second institution's authority on the first's ground | core | structure yes, content no (FA §13) | his seat is the Church's one seat reaching `terr_T1`; with `issue` on his row (FA-P2) and `patronage: own_faction` he cannot be replaced by the Crown | A, B | FA-P2 |
| NPC-039 Klapp, NPC-040 Jarnstal | a Church figure as one of several standing candidates for a named seat | core (M-SEAT) | no election, no candidacy | P-1 and P-2: a candidate is a petitioner naming the seat | B, F | CR-35 |
| NPC-021 Himlensendt | faith privately challenged while the public role continues | core | CHAR's (conviction; M-REGARD) | this lane fixes where he lives and what his seat can do; the crack is CHAR's | A | CHAR |
| NPC-004 Haelgrund | an investigation concluding plausibly and wrongly, acted on as true | core | FI's | his bench acting on it (P-4) is what makes the error cost someone | D | FI-03 |

Soonest: NPC-034 and NPC-021 (content, proposal A); NPC-039 / NPC-040 (the playable scenario, F); ARC-21
after SC-P4 and SC-P6.

---

## 11. Implementation plan

Ordered by dependency. Each batch: what changes, where, the gate (an execution artifact), the falsifier,
cost class, what it waits on. Exact edits are in the proposal files.

| batch | proposal | what lands | owner files | cost | waits on | gate and control | planted failure |
|---|---|---|---|---|---|---|---|
| 1 | A `…_A_ground.md` | the Confessor housed at Himmelenger; `dispatch` on the Templars' Cardinal's row; the three realm `scope:` values; CR-74's carrier named (`ROLE_TEMPLATE_OF`) | `npcs.yaml`, `offices.yaml`, `harness/strife_moves.yaml` | edit | FA-P2 (for the `dispatch` row to matter); CR-60 (for `scope:`) | `probe_reach.py` re-run: the Confessor stands under `terr_T9`; after CR-60 a Church bench `sits_over` `terr_T1`. Control: rows reverted reproduce the base build hash | a `scope:` on a non-bench seat changes nothing (it must not widen acting reach) |
| 2 | B `…_B_patronage_election_discipline.md` | `patronage:` key and `may_fill` clause; `conclave` row with `quorum_share`; the three-outcome count for an election; `head_of_faction` (held for Jordan) | `rosters.yaml`, `offices.yaml`, `state/gate.py`, `arrangements.yaml`, `data/arrangements.py`, `loop/effects_information.py` | small build | CR-35; `14_VERBS_BINDING` C (the `confer` draw); the SC ballot draw (`13_SC_draw_for_unrolled_contests.md`) | hand-built, real fold: the King's `confer` on `off_cardinal_prudence` refused, the Confessor's admitted; an election with three electors committed for and one with two for and two against, 200 seeds each: different outcome distributions, neither 0 nor 1, all three outcomes seen. Control: no `patronage:` key reproduces the base hash | give every elector the same commits in both arms: the two distributions must coincide |
| 3 | F `…_F_playable_vacant_chair.md` | the first playable scenario | `harness/` situation and probe; no game code | small build | batches 1-2; FA-P4's vacancy situation; CR-88 or a planted question | a seeded run in which a vacancy is filled by a person's `confer` or stays open, with the reason trail; the same seed without the vacancy shows no conferral | remove `patronage` and the Crown's seat fills the chair first at some seed |
| 4 | C `…_C_consecration_and_deed_ledger.md` | `offices.yaml: instruments:` and its builder pass; the `consecration` row; the charter goal row | `offices.yaml`, `harness/populated.py`, `arrangements.yaml`, `goals.yaml` | small build | CR-36 (`resolution`, the Record disposal site); SC-P8 / ARCS 04 (cited Records) | build: four instruments exist, held by the Cardinal of Temperance's seat-holder, with the three attestations' entry counts in Jordan's order; a planted consecration hearing with and without the predecessor's roll cited gives different odds (exact, no draw) and both arms show all four bands over 200 seeds. Control: `instruments:` empty reproduces the base hash | cite a Record the row's `proofs:` does not admit: the `evidence` term must read 0 |
| 5 | D `…_D_sanction_and_absolution.md` | `ban.opened` / `detention.opened`; the avoid / withhold `terms` form and its person-side decline; alignment cells for `deed:ban.opened`; penance as favourable evidence; the CH signature | `verb_table.yaml`, `rosters.yaml`, `decision/options.py`, `loop/effects_information.py`, `harness/strife.py` | small build | FA-P1; SC-P4, SC-P6; CR-88; CR-60; CR-74's slot | planted: a `ban` through a Church seat reads CH and through a secular seat does not; after a published sentence, addressees' answers over 200 seeds include comply and defy for the same person at different draws, and the share complying rises with his conviction (two arms). Control: writ never issued, no decline forms | make the decline unconditional on the answer: every addressee shuns, and the gate's "both answers occur" goes red |
| 6 | E `…_E_sees_tithe_orders_legates_council.md` | see rows (content); the tithe writ; an exempt house; a legate's termed seat; `general_council`; schism | `offices.yaml`, `goals.yaml`, `arrangements.yaml` | content edit, then design-first (schism, council) | FA-P3 (terms); CP-T08-07 (standing levy); the material verb lane; Jordan (§13) | per item in the proposal | per item |

**Playable scenario (the standing requirement).** Batch 3, *The Vacant Chair*: a Cardinal's seat is empty
at Himmelenger. Seats a player may take: the Confessor (whom to appoint, whether to take a candidate's
offered covenant, whether to wait), a candidate (petition, canvass, bargain), the King (press a man of his
own where `patronage` admits it, or covenant with the Confessor). One code path: the harness situation
builds the realm, plants the vacancy and offers `play_surface`'s aperture; the acts are the season loop's.
End: the chair is held on a non-provisional hold, or three seasons pass. The second scenario, after batch
4, is *The Petition* (a claimant seeks consecration); the third, after batch 5, *The Sentence*.

**What the Church needs to run well alone versus to compose.** Alone: batches 1-3 (a Church whose seats
turn over by its own people's acts). To compose: batch 4 joins it to the crown and the dukes; batch 5 to
every believer; batch 6 to the settlements and the economy.

**Dependencies on other lanes, stated as edges.** CR-35 → B. CR-36 → C. CR-60 → A (scope), D (absent
party). FA-P1 → D (answers form). FA-P2 → A. FA-P3 → E (termed legation), D (termed ban). SC obstacle and
T-tables → B, C, D. SC-P4, SC-P6 → D. SC-P8 / ARCS 04 → C. CR-88 → D (the lift), F (selection). CR-89 →
none blocked; its band triggers gain real acts to weight once B-E exist. `14_VERBS_BINDING` C, D → B, D.

---

## 12. Inconsistencies, gaps and unclear passages: decided

Ladder steps: 1 superseded, 2 irrelevant, 3 answered by a design document, 4 by precedent, 5 by what the
architecture needs.

| # | item | resolution | step | carried by |
|---|---|---|---|---|
| R-1 | The Confessor's roster row seats him in a market in `terr_T1` with no institution (F-PAP-04) | row corrected: `institution: Church`, `home: b_s_036_cathedral`. The file is hand-editable by its own header | 3 (canon: the Confessor is at Himmelenger) | A |
| R-2 | Canon calls Himmelenger sovereign; the realm rung contains `terr_T9`, so Crown seats have purview there (F-PAP-02) | containment stays (GD-1 counts the territory; `theocracy` and `peninsular_sovereignty` read it). Sovereignty is carried where it bites: who may fill the Church's seats (`patronage: own_faction`) and the charter whose breach the Church acts against. Not a detached root | 5 (a detached T9 would remove a territory from GD-1's count and from every realm walk) | B, C |
| R-3 | CR-35 narrows `elected` seats only; the six `appointed` Church seats remain fillable by the Crown | `patronage:`, opt-in per row, default today's rule | 4 (precedent: `revocation: rung_above_in_holdings`, a per-row basis Jordan ruled when hierarchy alone was wrong) | B |
| R-4 | `excommunication_deliberation` is described as judging an absent person and cannot (F-PAP-10) | answered by CR-60's `scope:` once the three benches carry realm scope; the row's comment then holds. Until then the comment is false and says so | 1 (CR-60 supersedes) | A |
| R-5 | CR-74 asks for a property by which a seat is a church's, or the missing carrier named | the carrier exists: `data/rosters.py::ROLE_TEMPLATE_OF[<seat's faction>] == "ecclesiastical"`, reached from `Act.via` through `office_faction`. No faction is named in the signature. Kinds: `arrest.made` today; `ban.opened` / `detention.opened` once D lands | 3 (the roster is the design's own statement of what kind of institution a faction is) | A, D |
| R-6 | The declared tally is a verdict by count of commitments (F-PAP-09) | owned and corrected by the SC lane's ballot draw (each ballot drawn, commits as odds). This lane adds the share-based pass mark and the three-outcome count for an election, and does not build a second vote | 1 (superseded by `13_SC_draw_for_unrolled_contests.md`; determinism sweep C-14) | B |
| R-7 | The archived design reverses an excommunication by *"Grand Debate or new Confessor"*; the code closes a `ban` only through the seat that is its object | the code governs and already yields both: any holder of that seat may `pardon` (a new Confessor), and a hearing before it is the debate | 3 / code | D |
| R-8 | The archived Excommunication *"strips Circles bonus … −1 Legitimacy to each settlement"*; no such quantities exist | not carried. The sentence's weight is each hearer's own judgement of `deed:ban.opened` and his answer to the writ | 2 (the quantities were retired) | D |
| R-9 | *Cardinal Independence Check*, *Jarnstal Drift 0-3* (a private counter) | a Cardinal acting against a held writ of the Confessor is `evade / defy`; nothing counts to 3. The head's remedy is P-9 | 2 / 3 (Layer 1 refuses the counter) | B |
| R-10 | Church Influence, Piety Track, Church Attention | already translated by the plan (CR-89; FA-07's second round). This lane adds acts those folds will count, and no clock | 1 | none |
| R-11 | The canon timeline's *"exclusion from the war coalition's leadership"* against Jordan's ranking of Varfell's first Duke third | Jordan's word governs: the founder fought and ranked last. The canon sentence is owed an amendment by Jordan's hand; this lane edits no canon | 3 (Jordan's statement) | §13 item 4 (a note, not a question) |
| R-12 | `off_duke_varfell` is `elected` while the ducal house is conquest-founded | both stand: the deed founded the seat; the Jarls fill it. The founding attestation attaches to the seat's first holder | 5 | C |
| R-13 | Should the King be sworn (`oblige`) to the Confessor's seat at consecration? | no. Under the oblige clause that would give the Confessor purview over the whole realm (the papal-fief model). Canon says first among equals and co-sovereign; the bond is the charter and the attestation | 3 (canon) | C |
| R-14 | `off_cardinal_fortitude` commands only through the unruled `dispatch` (F-PAP-08) | its row names `dispatch` | 3 (the body's own note: *"Military. Knights Templar, enforcement"*) | A |
| R-15 | Indulgences, annates | not adopted (§4.1, §4.2) | 5 / canon guard | none |
| R-16 | Latae sententiae (automatic sentence) | refused: a fixed function of state | standing rule | D |
| R-17 | A dead founder's deeds and the heir's `legitimacy` | not joined here; the interface is stated (§2.2 item 3) for the lane that gives a house a carrier | 5 (one owner for *what a house is*; it is not the Church) | C, as a cross-lane request |

Resolutions decided: 17.

---

## 13. Decisions that survive to Jordan

Each survived the five steps: two defensible options that lead to different games, or an answer that
would overwrite a ruling.

1. **May the head of the Church strip a Church officer?** (FA §11 item 3; the seven seats are ruled
   `null`, 2026-10-11.) *(A) Keep null*: Cardinals leave by death; an over-mighty or exposed Cardinal can
   only be killed, outlived or sentenced without being unseated; the Church is a set of barons for life.
   *(B) `head_of_faction`*: the Confessor disciplines (P-9, a draw the officer can resist); the Church has
   internal politics, purges and the fear of them; NPC-038's removal on exposure becomes possible. This
   lane writes (B) in proposal B and ships it off.
2. **Can anyone judge the Confessor?** *(A) Nobody*: he leaves by death or resignation; a bad Confessor is
   answered by schism (a rival seat) or violence. *(B) A council with the Crown's concurrence*: the mirror
   of CR-37 (the throne is stripped by a motion and the Holy See's concurrence; the Holy See by a council's
   motion and the throne's). (B) makes Crown and Church each the other's check and gives the archived
   *Confrontation* arc a lawful route; (A) keeps the Church the one institution with no check, which is
   what makes Himlensendt *"the most dangerous person on the peninsula"*.
3. **Is lay investiture lawful on ducal ground?** *(A) `patronage: [purview, own_faction]` on sees*: the
   lord and the Confessor may each fill a see in the lord's land, and the investiture contest is a
   standing feature. *(B) `own_faction` everywhere*: the Church appoints all its own; lords contest it only
   by violence or by founding rival houses. (A) is this lane's content default for sees and (B) for
   Himmelenger's seats.
4. **Note, not a question:** `canon/03_canonical_timeline.md:76` and `:96` need Jordan's amendment to
   agree with the ranked order of accomplishment (R-11), and the three founding attestations' entry
   counts (proposal C: 5, 3, 2 as first values; only the order is Jordan's) are his to set.

---

## 14. Evidence log, research transfer, and what was not read

### Evidence

| id | command | seed · seasons | outcome |
|---|---|---|---|
| E-1 | `PYTHONPATH=. PYTHONHASHSEED=0 python <scratch>/runs/INST_PAPACY/probe_church.py 3 0 1` (builds the realm, runs `SeasonDriver` with the harness chooser, reads `w.acts`, `w.log`, `w.tenures`; writes nothing tracked) | 0, 1 · 3 | resolved acts through Church seats: 64 (seed 0), 49 (seed 1); `open_case` 14 and 8; `determine` attempted 1 and 3, resolved 0 and 1; `ban`/`detain` Tenures 0 and 0; `claim.decayed` 34,837 and 31,392; seed 1: `person.died` 1, `off_cardinal_prudence` vacant at the end. Output: `probe_church_3s_seeds01.txt` |
| E-2 | `… probe_reach.py` (build only) | 0 · 0 | rungs: 1 realm, 3 duchies, 18 territories, 38 settlements, 211 hearths; purview and bench table as F-PAP-01; `may_fill` and `may_revoke` lists as F-PAP-02, -03; `oblige` edges to Church seats `[]`; records `{'works': 2}`; persons under `terr_T9` 9 of 83; the Confessor's ancestry `b_s_003_market → set_s_003 → terr_T1`; `solmund_orthodoxy` held by 44 persons at levels 1-5. Output: `probe_reach_seed0.txt` |
| E-3 | YAML parse of `verb_table.yaml` (67 rows; emits, eligibility) and `rosters.yaml` value sets | n/a | `comply` emits `compliance.given`; `pardon` emits `detention.ended`, `ban.ended`; no row emits `ban.opened`; `release` domain includes `oblige`; `record_kinds` has no `resolution` yet |

Scratch directory: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/INST_PAPACY/`.
No pytest was run. No number above is a balance claim: E-1 is two seeds and is reported as counts, not rates.

### Research transfer

- **Changes what to build**: *Ubi periculum* as a check on sitting plus a cost that accrues by itself (the
  vacancy), not a ration counter (`governance_modes.md:295-296`); the two-signal reading of sanctions
  (`political_hierarchy_standing.md:193-194`, `conflicts_power_struggles.md:196-209`), which is why P-6 is
  each person's draw; the Concordat of Worms' bifurcated grant (`governance_modes.md:213-215`), carried as
  `patronage:` per seat; *"the roll, not the draw"* (capture at the eligibility list,
  `political_hierarchy_standing.md:323-324`), which is why the attestation, not the vote, is the thing
  worth forging; the benefice as title and grant apart (`:172-173`); the cardinal-nephew as a shadow
  hereditary track (`governance_modes.md:296`), carried as *who conferred whom*.
- **Decorative, or tried and not transferred**: the curia's chain of clerks as seats; indulgences;
  annates; the Papal States' vicariates; the secular veto in conclaves; voting by nation (Valoria's Church
  has four arms, not nations; the idea returns only if sees multiply).
- **Nulls**: the tree's game-precedent suite was not searched for a shipped game that models
  excommunication as third-party compliance rather than a stat penalty; none is claimed. The historical
  statements marked `[M]` are from memory and unverified against sources in this session.
  `[RE-GROUNDED: searched now (§15.5). The suite holds no such game: its religion rows are a scalar stock and a named layer. The null stands, as a finding. The `[M]` marks are resolved one by one in §15.2]`
- **Stale in the research**: the hooks are written in the retired Key idiom and against a stored Standing
  ladder; only their shapes were taken.

### Not read, or read in part

- `[SKIPPED: .designs/systems/factions/reference/faction_politics_v30.md — the 168 KB rank-ladder body
  (Church ladder, Inquisitor and Templar sub-ladders, dicasteries); read through its digest entry only]`
- `[SKIPPED: faction_layer_v30*.md, factions_personal_v30*.md, ci_political_v30.md bodies — digest
  entries only]`
- `[SKIPPED: research/governance/*.md in full — the passages on the papacy, investiture, schism and
  benefices were extracted by pattern and read; the rest through the digests]`
- `[SKIPPED: audits 05_SC, 06_FA, 07_SE, 02_CHAR in full — verdicts, the Church-bearing passages and the
  proposal heads were read; SC-P8's item-weight rule, FA-P1's body and the CHAR chooser statement were not
  opened, and each dependence on them is marked]`
- `[UNVERIFIED]`: whether `issue` admits an addressee outside the issuing seat's purview; whether the build
  admits an authored seat with no holder; `loop/effects_governance.py::_eff_release`'s witness of an ended
  `oblige`; CR-88's `grievance_against` (unbuilt). Each is named where the proposals rely on it.

