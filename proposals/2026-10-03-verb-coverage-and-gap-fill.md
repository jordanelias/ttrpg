# Verb coverage and gap fill — the 44 verbs of `engine/season/verb_table.yaml`, what they reach, and what is missing

## Status: PROPOSED

> **SCOPE, STATED LOUDLY.** This document is **reference and a proposal** (CLAUDE.md §0.05): it resolves
> nothing at runtime, and if it were deleted the game would behave identically. **Merging the PR that
> carries it does NOT ratify any new verb, state, widening or cut in §6–§8**, notwithstanding the
> merge-ratifies default (ED-1094): each of those items carries its own decision and is **held back**
> until it is built in code, at its owner, with a test that executes it. Every grade proposed here is
> `assumption` or `absent`; none is `ruled`. A design document is never the reason a behaviour is
> correct — the code is.

- **Date:** 2026-10-03
- **Authorship:** Claude — orchestrating two read-only adjudication passes and seven extraction
  passes; written up in a separate authoring pass.
- **Lane:** IN (cross-cutting). No ID was allocated; no ledger row was written.

---

## 1. Purpose, method and limits

**Purpose.** Jordan asked for five things this session: an etymology and word-fit adjudication of each
of the 44 verbs in `engine/season/verb_table.yaml`; a comparative analysis isolating what each does in
this game; grouping into related sets with their relations to personal combat, social contest and the
plain instantiation of world facts; a hook proposal per verb; and the missing verbs and states, found by
comparing the table's reach against precedents and research and filled without conflicting with the
existing verbs, from faction- and office-scale acts down to granular person acts and events. This
document is that answer. It changes no code.

**Pipeline.** A fact sheet was extracted from the live table (loading `engine/season/data/verbs.py`'s
`VERB_TABLE`, `loop/effects.py`'s `EFFECTS`, `loop/driver.py`'s `resolvable_verbs()` and the raw YAML).
A read-only adjudicator, holding no write tool, adjudicated the 44 against the code (pass 1: etymology, fit, whether each
row earns its place, group, hook, falsifier, blocker). Seven extractors then harvested **707**
candidate acts: the repo's `research/` (80), its governance proposals (67), its narrative and play
proposals (80), the season loop's own measured demand — hole register, requirements, case needs (77) —
seven detective games (107), *Crusader Kings III* and *Romance of the Three Kingdoms* (107), and
governance history: parliaments, royal governance, the Venetian councils, church justice and the
inquisition, secular law and state intelligence (189). The adjudicator's pass 2 classified those against the 44's
reach and proposed states and new verbs. The authoring pass wrote this up, opened the cited sites listed in §10, and
corrected the reports where a citation did not say what they claimed.

**Limits, stated plainly.**

- The extractor tables were built partly from headings and greps, not full reads. Each extractor's own
  coverage notes name what it skipped; Appendix C carries one line per source. The material gaps:
  `research/` integration and game-companion volumes read in part (meta-analysis, not act catalogues);
  the proceedings subsystem's files 00–03, 06–08, 11–16 and 18–20 grepped only, and the
  governance-and-behaviour `RULINGS.yaml` not read; the 2026-09-03 corpus-rebuild proposal describes an
  *uploaded* corpus never verified against `main`; the 2026-08-30 coverage set and the term-ownership
  registry predate the 44-verb table (and the latter, the Key substrate's retirement); effect bodies and
  `witness.py` were grepped for event kinds only; case-need counts carry about ±2 from regex aid.
- Web facts about the games rest partly on **search snippets**: many review sites returned HTTP 403, and
  the Paradox wiki's Schemes, Council, Laws, Hooks and Court-positions pages would not load. *Lacuna* and
  *Tails Noir* are thinly sourced; *Pentiment*'s Acts II–III trial detail was not fetched. History rows
  rest on secondary summaries (mostly Wikipedia) read by a small model. Items the sources tag
  [UNVERIFIED] stay tagged here.
- The per-verb attempt/execution figures for the realm (written `att/ex` below) are **copied from
  `engine/season/requirements.yaml:674-676`**, which labels them as tree `23bea9da`, older than HEAD.
  They were not re-run.
- The adjudication passes are judgments over the extractor tables and the code sites they opened. They are not
  execution evidence, and nothing in this document is.

**Instruments and measurements.**

| measure | value | instrument | when, by whom |
|---|---|---|---|
| verbs defined | **44** | `len(VERB_TABLE)`, import only | 2026-10-03, re-run by the author |
| verbs admitted to the fold | **34** | `resolvable_verbs()` in `engine/season/loop/driver.py`; the ten not admitted are `carry`, `comply`, `construe`, `evade / defy`, `exchange`, `forge`, `repudiate`, `succeed`, `thread_read`, `tie / knot` | 2026-10-03, re-run by the author |
| verbs that executed | **17 of 44** — `create_record`, `examine`, `fight`, `give`, `interview`, `issue`, `move`, `petition`, `reconstruct`, `release`, `research`, `restore`, `speak`, `surveil`, `tell`, `transfer`, `utter` | `python -m engine.season.harness.corpus_run` (143 cases, seed 0, 2 min 58 s) | 2026-10-03, run by the orchestrator this session; not re-run by the author |
| attempted and always refused | **7** — `build`, `commit`, `found`, `levy`, `migrate`, `survey`, `work` | same run | same |
| foldable but never attempted | **10** — `confer`, `convene`, `destroy_record`, `determine`, `dispatch`, `establish`, `march`, `oblige`, `open_case`, `revoke` | same run | same |
| `write_matrix.yaml` rows written by no verb | **15 of 37** | read-only script: the union of every row's `writes:` (the list, or the values of a degree-keyed mapping) as `kind.field` strings gives 22, every one a matrix row; the 37 `rows:` entries not in that set are counted | 2026-10-03, author; agrees with the code-demand extractor |

Of the 15, ten are written by a non-act step or are immutable: `Act[].returned` (DEL), `Claim.confidence`,
`Record.matured`, `Record.ttl`, `Rung.yield` (MAT), `Date.fired` (CAL), `Person.claim_ledger` (WIT),
`Person.weight` (CEN), `Rung.envelope` (MAT, CEN) and `Proposition.*` (immutable). **Five are act-class
(RES) rows with no writer at all:** `Person.axis_count`, `Person.coherence`, `Person.pursuits`,
`Rung.dates` and `Tenure.degree`. Two proposals below would be first producers: `argue` for
`Person.pursuits` (§7.4) and the contested `determine` for `Tenure.degree`, if its bands are written there
(§7.5) [ASSUMPTION: basis — H-162 names `Tenure.degree` as the missing producer for a graded hearing].

---

## 2. Direction given in session

Stated by Jordan **in conversation on 2026-10-03, and NOT ledgered** — no ED id was allocated, so none of
these is a ruling of record. They are carried verbatim because the rest of this document is built on
them.

1. **Method.** *"we do etymology and comparative analysis and sets and everything else so that we can
   logically identify where we have coverage and the flexibility of what a verb should be able to do,
   and then based on our precedents and research and stuff we find where our gaps lie and what verbs
   fill the gaps without conflicting with others"*. §3 is the etymology, comparison and sets; §5 is the
   coverage; §7 is the gap fill, each new verb carrying a CONFLICTS axis against its nearest neighbours.
2. **Expectation.** *"I am expecting there to be gaps and missing coverage"* / *"so fill them"* / *"I
   think you just need to develop more verbs"*. §7 proposes fourteen new verbs and ten widenings.
3. **`kill` and `wound`.** *"kill and wound are verbs that handle outputs, which I think means they
   shouldn't exist as they just relay state changes? characters can not actively choose to kill or
   wound. they can choose to fight tho"*. The statement is hedged (*"I think"*). It agrees with the
   earlier ruling recorded at `engine/season/verb_table.yaml:442-448` (Jordan, 2026-09-27: *"a character
   can only attempt to kill or wound, never choose the outcome directly"*), on which the row was renamed
   `fight`. [ASSUMPTION: this direction **closes** the still-pending split of `fight` into `kill` and
   `wound` that the table records at `verb_table.yaml:446-448` and again at `:467` — basis: the
   direction names both as outputs that "shouldn't exist"; Jordan to correct if he meant otherwise.] The
   **other half** of the same pending note — `challenge` → `accept`, a two-sided duel — is a different
   question (whether a fight may be offered and taken) and this direction leaves it untouched.
4. **States.** *"we're also going to need states that can flag war and peace and alliances and treaties
   and stuff"*. §6 catalogues them.
5. **Church and Riskbreakers.** *"remember we have to hook into inquisitions with church as well as stuff
   for riskbreakers for espionage and law and stuff"* and *"as well as heresy and trials and stuff"*.
   The law-and-custody verbs (§7.1), the polity instruments (§7.2), the covert verbs (§7.3) and the
   Active Inquisition chain in §8.2 answer this.
6. **Altitude.** *"have to ensure we can cover from faction actions down to granular events that hook
   into season loop"*. §8.2 maps every faction action in `references/action_vocabulary.yaml` down to a
   person's act at a rung, and §8.3 maps the non-act mechanics to the season loop's own stages.

**Resolved names.** "Shadows of darkness" is *Shadows of Doubt* (Jordan confirmed in session). "Romance of
three kingdoms" is read as Koei's *Romance of the Three Kingdoms* game series [ASSUMPTION: basis — the
list is of games]. *Tails Noir* is the renamed *Backbone* (EggNut, published by Raw Fury), per the games
extractor's web check [UNVERIFIED: search snippet, not a primary page].

**One ruling binds every faction-scale row below.** There is no faction actor in this model: every
faction act is a person's act, taken by an office-holder through a seat (`Act.via`) at a rung. Where a
source says "the Church excommunicates" or "Parliament votes", this document reads it as a named holder
acting through a named seat. The tree already says so where code reads it: `engine/season/rosters.yaml:1026-1029`
— Layer 1 PART D rows 1, 8 and 14 forbid a faction that acts; a Faction is a type with no verbs, and its
holdings are a Query over members' `hold` Tenures.

---

## 3. The 44

### 3.1 Origin and fit

*Origin chain* abbreviations: OE Old English, ME Middle English, OF Old French, AN Anglo-Norman, MF Middle
French, L Latin, LL Late Latin, VL Vulgar Latin (\* = reconstructed), ML Medieval Latin, ON Old Norse.
*Earns*: YES = removing it loses a write or reader no other row supplies; THIN = present but the
consequence is unbuilt or duplicated; REDUNDANT-WITH = another row already does it. Groups are §3.2.

| verb | origin chain | root sense | what the row does | word fit | earns | grp |
|---|---|---|---|---|---|---|
| `build` | OE *byldan* ← *bold* 'dwelling' | raise a dwelling | mint a Site at condition 0 from a held works | FITS | YES — sole `Site.exists` producer | G9 |
| `carry` | AN *carier* ← LL *carricare* ← *carrus* 'wagon' | convey | put a held petition on a docket | STRAINED — reads as transport; plain: `lodge`, `present` (proposal) | THIN — effect declined | G4 |
| `commit` | L *committere* (*com-* + *mittere* 'send, put') | entrust | open a `commit` edge to a Proposition | FITS | YES — `ambitions` reads it | G7 |
| `comply` | It. *complire* ← L *complere* 'fill up' [UNVERIFIED: the Spanish/Catalan intermediate] | fulfil | answer a held dispensation; emission only | FITS | REDUNDANT-WITH writ-sourced `transfer` (proposal) | G5 |
| `confer` | L *conferre* 'bring together, bestow' | bestow | open a `hold` on a seat, close the incumbent's | FITS | YES | G7 |
| `construe` | L *construere* 'build up' → ME *construen* | interpret a text | a distorted reading of an instrument's terms | FITS (ruled rename, `verb_table.yaml:737`) | THIN — grade `absent` | G5 |
| `convene` | L *convenire* via OF *convenir* | come together | schedule a sitting: `Date.due_at` | FITS | THIN — the date fires vacant | G4 |
| `create_record` | L *creare* + *recordari* 'call to mind' via OF *record* | make a remembrance | mint a Record with declared stages and the maker's hold | FITS | YES — the one mint | G6 |
| `destroy_record` | L *destruere* via OF *destruire* | unbuild | delete a Record and every hold on it | FITS | YES — sole closer of `Record.exists` | G6 |
| `determine` | L *determinare* ← *terminus* 'boundary' | fix the bounds | dispose of a docketed matter by opening the party's `oblige` | FITS | YES | G4 |
| `dispatch` | It. *dispacciare* / Sp. *despachar*, root disputed [UNVERIFIED] | send off | emit `order.given`; write nothing | STRAINED — ordinary use sends, the row orders; plain: `order` (proposal) | THIN — no decision reads `order.given` | G5 |
| `establish` | L *stabilire* via OF *establir* | make firm | found an Office or change its remit | FITS | YES | G7 |
| `evade / defy` | *evade* L *evadere* 'go out'; *defy* OF *desfier* ← VL \**disfidare* 'renounce faith' | slip away / renounce allegiance | withhold compliance with a held writ | each word FITS; the ROW is a MISFIT — covert and open refusal share one `compliance.withheld` | THIN | G5 |
| `examine` | L *examinare* ← *examen* 'tongue of a balance' | weigh | study a Site one stands at | FITS | THIN | G11 |
| `exchange` | OF *eschangier* ← VL \**excambiare* | swap | two-sided stores move | FITS | THIN — no cell, no effect | G8 |
| `fight` | OE *feohtan* | strive, do battle | contest the body of a living person; the attempt only | FITS | YES — the one door to the duel engine | G1 |
| `forge` | L *fabrica* 'workshop' via OF *forge*; 'counterfeit' from the 14th c. | work metal; make falsely | mint a Record carrying `forgery_quality` | FITS | THIN — effect declined | G6 |
| `found` | L *fundare* ← *fundus* 'bottom' via OF *fonder* | lay a base | mint a Rung under its works' `at` | FITS | YES — sole `Rung.exists` producer | G9 |
| `give` | OE *giefan* (the *g-* from ON *gefa*) | hand over | close the giver's `hold` on a Record, open the receiver's | FITS | YES — the only Record mover | G6 |
| `interview` | MF *entrevue* ← *s'entrevoir* 'see each other' | a meeting | question an existing person | FITS | THIN | G11 |
| `issue` | OF *issir* ← L *exire* 'go out' | send out | mint a dispensation to an executor in purview | FITS | YES | G6 |
| `levy` | OF *levée* ← L *levare* 'raise' | a raising | move a rung's stores into the seat's rung | FITS | YES | G8 |
| `march` | F *marcher*, prob. Frankish [UNVERIFIED] | tread | send a mustered side against a settlement | FITS | YES | G2 |
| `migrate` | L *migrare* | change abode | re-home `contain` and `reside`, throttled by room | FITS | YES | G10 |
| `move` | L *movere* via AN | set in motion | re-home `contain` only | FITS | YES — presence | G10 |
| `oblige` | L *obligare* 'bind to' via OF *obligier* | bind | open an `oblige` edge with a term to a seat | FITS | YES | G7 |
| `open_case` | *case* ← L *casus* 'a falling' via OF *cas* | what befalls | mint a case file, docket the matter | FITS | YES | G4 |
| `petition` | L *petitio* ← *petere* 'seek; aim at' | a request | mint a petition Record from a rung to a person | FITS | YES | G6 |
| `reconstruct` | *re-* + L *construere* | build again | a finding from claims already held | FITS | THIN | G11 |
| `release` | OF *relaissier* ← L *relaxare* 'loosen' | let go | close one's own live edge of a releasable kind | FITS | YES | G7 |
| `repudiate` | L *repudiare* ← *repudium* 'divorce' | cast off | close one's own `commit` | FITS | REDUNDANT-WITH `release` (proposal) | G7 |
| `research` | MF *recercher* ← L *circare* 'go about' | search closely | consult an existing Record | FITS | THIN | G11 |
| `restore` | L *restaurare* via OF *restorer* | renew | raise a Site's condition toward its ceiling | FITS | YES | G9 |
| `revoke` | L *revocare* 'call back' | recall | close another's `hold` through a seat with a basis | FITS | YES | G7 |
| `speak` | OE *sprecan*/*specan* | say words | emit `speech.made` on a referent; no hearer, nothing said | STRAINED — speech has an audience; the row has none | REDUNDANT-WITH `tell` (proposal) | G12 |
| `succeed` | L *succedere* 'come after' via OF | follow in place | the holder designates an heir | STRAINED — the heir succeeds; the actor designates; plain: `designate` (proposal) | THIN — no reader, no heir operand | G7 |
| `surveil` | 20th-c. back-formation from *surveillance* ← F *surveiller* ← L *vigilare* | keep watch | observe a Rung one stands at | FITS | THIN | G11 |
| `survey` | AN *surveier* ← ML *supervidere* 'oversee' | look over | commission a faction sheet | FITS | YES | G6 |
| `tell` | OE *tellan* 'count, recount' | recount | tell a known present person what one holds, contesting their standing | FITS | YES | G3 |
| `thread_read` | OE *þrǣd* + *rǣdan* 'advise, interpret' | — | a finding gated on Thread Sensitivity ≥ 30 | FITS (canon term) | THIN — not admitted | G11 |
| `tie / knot` | *tie* OE *tīgan*; *knot* OE *cnotta* | bind | open a bond edge of kind `tie` or `knot` | each FITS; the ROW is a MISFIT — one opener cannot name its kind | THIN | G7 |
| `transfer` | L *transferre* 'carry across' | carry across | stores from the actor's rung to the referent; renews obligee terms via a seat | FITS | YES | G8 |
| `utter` | ME *uttren* ← *ūt* 'out', path via Middle Dutch [UNVERIFIED] | put forth | mint an immutable Proposition | FITS | YES | G12 |
| `work` | OE *weorc*/*wyrcan* | labour | alter `Site.condition` by a declared delta, else advance a works | MISFIT — labour produces; the row is `restore`'s rise under a floor | REDUNDANT-WITH `restore` in computed play (proposal) | G9 |

**Tallies.** Fit: 37 FITS, 4 STRAINED (`carry`, `dispatch`, `speak`, `succeed`), 1 MISFIT (`work`), 2 rows
whose words fit but whose row merges two acts (`evade / defy`, `tie / knot`). Earns: 25 YES, 15 THIN, 4
REDUNDANT-WITH. **No row is now named for an outcome** (`fight` replaced `kill / wound`); `succeed` is the
one row named for what happens to someone else rather than what the actor chooses, which is the ground
of the `designate` proposal and the same logic as direction 3.

### 3.2 Groups

Each grouping is true by a column, named in the last cell. Only three of the 44 reach a contest seam
today (`fight`, `march`, `tell`); the four proceedings verbs are social contest by lineage only; the six
findings are investigation, ruled not a contest; twenty-six rows instantiate world facts directly.

| group | members | relation to combat, contest, proceedings, world fact | the column that makes it true |
|---|---|---|---|
| **G1 Personal combat** | `fight` | personal_combat owns the prize (`rosters.yaml:1107-1110`); world facts only as the band's consequence | `contests: "the body"` (`verb_table.yaml:466`); degree-keyed `writes:` |
| **G2 Mass battle** | `march` | mass_battle through the `mass_battle.resolve_field` role, fought at ENCOUNTER (`rosters.yaml:1111-1130`); sides are armies; writes land on the losing side | `contests: "a field"`; `step: ENCOUNTER` on the prize row |
| **G3 Social contest** | `tell` | social_contest owns `a standing`, rolled by `sigma_leverage`, `interim: true` (`rosters.yaml:1131-1148`); the opponent is `to` | `contests: "a standing"` |
| **G4 Proceedings, uncontested** | `carry`, `convene`, `determine`, `open_case` | social contest by lineage: `a proposition` repoints to the proceedings provider when it lands (`rosters.yaml:1149-1153`); no member contests yet | `DocketItem.matter` on three; `Date.due_at` on `convene`; `remit:determine`/`remit:convene` |
| **G5 Writ answers and orders** | `comply`, `construe`, `dispatch`, `evade / defy` | none yet; H-36 rules construal receiver-side | `writes: []` on all four; `requires_typed: none` on three |
| **G6 Documents** | `create_record`, `destroy_record`, `forge`, `give`, `issue`, `petition`, `survey` | world fact; `issue` and `petition` feed G4 and G5 | `Record.exists` on six; `give` moves the two `hold` edges |
| **G7 Seats and bonds** | `commit`, `confer`, `establish`, `oblige`, `release`, `repudiate`, `revoke`, `succeed`, `tie / knot` | world fact | `Tenure.since/until/term/payload`, `Office.exists/remit_acts`; the tenure kind is the discriminant (`rosters.yaml:115`) |
| **G8 Matter** | `exchange`, `levy`, `transfer` | world fact | `Rung.stores` written twice by one `_shift` body |
| **G9 Ground and fabric** | `build`, `found`, `restore`, `work` | world fact | `Rung.exists`, `Site.exists`, `Site.condition`; `_rise` is the one formula |
| **G10 Movement** | `migrate`, `move` | world fact | stratum `movement`; `Person.travel_leg` and the `contain`/`reside` pairs |
| **G11 Findings** | `examine`, `interview`, `reconstruct`, `research`, `surveil`, `thread_read` | investigation, "its own kind — not a contest" (`rosters.yaml:1008`); it must not be made a contest to become gradeable (`:1031`) | `writes: []`, `emits: finding.made` on all six |
| **G12 Free speech acts** | `speak`, `utter` | `utter` is world fact (`Proposition.exists`); `speak` emits only | `requires: —`; empty `emits_on_refusal` |

### 3.3 Comparative clusters

| cluster | discriminating axis | verdict |
|---|---|---|
| `give` / `transfer` / `exchange` / `levy` | what moves, to whom: a Record's `hold` to a known present person; stores from the actor's rung to the referent; stores from a rung in purview to the seat's rung under `remit:issue`; both sides' stores (no cell) | `give`, `transfer`, `levy` EARN; `exchange` THIN — two `transfer`s survive its cut, losing only atomicity and the paired scarcity |
| `speak` / `tell` / `utter` | `utter` writes `Proposition.exists`; `tell` binds a hearer, contests a standing, carries `said`; `speak` binds, carries and contests nothing, and bystanders already hear a `tell` by presence (`verb_table.yaml:887`) | `utter`, `tell` EARN; `speak` REDUNDANT-WITH `tell` [CONFIDENCE: medium — `speak` executes 104–139 corpus acts across the re-pins recorded at `hole_register.yaml:3521`]. What dies with it: speech by someone who knows nobody, or holds no claim on the topic |
| `issue` / `petition` / `carry` / `open_case` | eligibility and direction: down a remit; up from a rung; `carry` and `open_case` both write `DocketItem.matter`, differing by eligibility (`own` vs `remit:determine`) and subject kind | `issue`, `petition`, `open_case` EARN; `carry` THIN — H-52's `own` alternative, scoped to petitions |
| the six findings | in code, only the `requires_typed` object class (Site, Person, Record, Rung, own claim, TS gate) | all six THIN until the degree producer exists (work item 4.5, `verb_table.yaml:982-989`). THIN is about consequence, not a cut: Jordan ruled the six built as six rows (`verb_table.yaml:950-952`) |
| `confer` / `establish` / `oblige` / `commit` / `succeed` / `tie / knot` | what is opened, and who reads it: `oblige` → `establishment_of`, `_ch_post_remit`; `commit` → `ambitions` → need questions; `knot` → `_ch_witness_key`; `tie` and `succeed` → nobody | `confer`, `establish`, `oblige`, `commit` EARN; `succeed`, `tie / knot` THIN |
| `release` / `revoke` / `repudiate` | whose edge: one's own of any releasable kind; another's `hold` through a seat with a basis; one's own `commit` — already inside `release`'s domain (`verb_table.yaml:748`) | `release`, `revoke` EARN; `repudiate` REDUNDANT-WITH `release`, provided `_eff_release` earns one event kind per closed edge kind (precedent `effects_governance.py:90-91`) so `commitment.ended` and its three alignment cells (`rosters.yaml:2158,2194,2232`) survive |
| `restore` / `work` | preconditions only (floor vs presence); one formula | `restore` EARNS; `work` REDUNDANT-WITH `restore` in computed play [CONFIDENCE: medium] |
| `move` / `migrate` | the `reside` edge and the capacity refusal | both EARN; `migrate` executes nowhere yet |
| `comply` / `evade / defy` / `construe` | none in code; the executed half of compliance is a `transfer` whose `to`, `kind`, `amount` come off the held writ (`decision/options.py:717-729`; `rosters.yaml:1571-1584`) | `comply` REDUNDANT-WITH the writ-sourced `transfer` for the one term shape built (H-44 names nine, none enumerated); `evade / defy`, `construe` THIN |
| `fight` / `march` | prize, sides, step, write target | both EARN |
| `create_record` / `forge` / `survey` | content source: verbatim; falsified with an unread quality; resolved at writing | `create_record`, `survey` EARN; `forge` THIN |
| singletons | `convene` — sole `Date.due_at` writer, but `date.fired` never reaches WITNESS; `dispatch` — writes nothing, read by channels and tests only; `destroy_record` — sole closer of `Record.exists`; `found`/`build` — sole producers of `Rung.exists`/`Site.exists` | `convene`, `dispatch` THIN; `determine`, `destroy_record`, `found`, `build` EARN |

### 3.4 REACH and NOT — the coverage baseline

*REACH* is what the row can do as built or as its cell reads; *NOT* is the nearest act it does not do and
which verb owns it. "unowned" marks a gap tested in §5.

| verb | REACH | NOT → owner |
|---|---|---|
| `build` | a held `works` planning a `site_kinds` member, at the rung it names | found a Rung (`found`); raise condition (`restore`); end a Site (unowned) |
| `carry` | a held petition → the docket | file (`petition`); docket by remit (`open_case`); forward, amend, drop (unowned) |
| `commit` | any existing Proposition — an OUGHT, a faction, a treaty, a motion; opens `commit` | utter (`utter`); duty to a seat (`oblige`); seat-to-seat fealty (unowned, H-101); a vote cast through a seat (unowned: needs `via`) |
| `comply` | a held writ; emission only | perform the terms (writ-sourced `transfer`); withhold (`evade / defy`); misread (`construe`) |
| `confer` | an Office, `to` a person, `remit:confer` via a seat with purview | found it (`establish`); strip (`revoke`); elect (basis exists, `rosters.yaml:1755`; no act casts the vote); heir (`succeed`); a term-limited seat (unowned: + `Tenure.term`) |
| `construe` | a held writ; a receiver-side reading | lie (`tell`, H-183); forge (`forge`) |
| `convene` | any rung above `person`; `remit:convene`; `Date.due_at`; adjourning is rescheduling (same verb) | docket (`open_case`/`carry`); decide (`determine`); summon a person (unowned) |
| `create_record` | any rostered kind, declared content and stages, the maker's hold | writs (`issue`); petitions (`petition`); sheets (`survey`); forgeries (`forge`); hand on (`give`) |
| `destroy_record` | a Record the actor holds or stands by | take from another (unowned); suppress a class of text (unowned); end a Rung or Site (unowned, H-166) |
| `determine` | a docketed Person in the bench's ground; opens the disposal `oblige`, clears the docket | grade a hearing (unowned, H-162); a sentence other than service (unowned, H-173); appeal (unowned); lift a disposal (the party's own `release`, §7.1) |
| `dispatch` | an existing person; `remit:dispatch`; `order.given` | a writ with terms (`issue`); muster (`march`); summons (unowned) |
| `establish` | a described Office at a rung; `remit:confer` | seat (`confer`); found a place (`found`); an office under an office (unowned, H-101); dissolve (unowned) |
| `evade / defy` | a held writ; withholding | flee (`move`); contumacy (unowned); renounce fealty (unowned) |
| `examine` | a Site stood at; physical trace | a person (`interview`); a document (`research`); a place over time (`surveil`) |
| `exchange` | two sides' stores | one-way (`transfer`); office sale (`exchange` + `confer`); ransom (unowned: custody) |
| `fight` | a living person; the attempt; prize the body | kill, wound (outcomes, direction 3); war (`march`); restrain or arrest (unowned); execute (unowned); challenge (pending, §9) |
| `forge` | a Record with `forgery_quality` | a true record (`create_record`); plant it (`give`); a false telling (`tell`) |
| `found` | a held works planning a `rung_kinds` member; strict ascent | Site (`build`); office (`establish`); league (unowned); charter (an `issue` kind) |
| `give` | a held Record `to` a known present person; the gate's handover covers every non-seat hold | stores (`transfer`); seize (unowned); cede a rung hold (WIDEN, §7.5) |
| `interview` | an existing person | interrogation under custody (unowned); covert watching (`surveil`) |
| `issue` | terms + `to` a person executor in purview | a documentless order (`dispatch`); an edict to a place (unowned — the cell refuses a rung); an instrument to a foreign seat (unowned); rescind (unowned) |
| `levy` | a rung in purview with stores → the seat's rung | tribute by term (`transfer`); a person's goods (unowned); muster (`march`) |
| `march` | a settlement; `remit:dispatch`; prize a field at ENCOUNTER; writes the losing side | siege (unowned); conquest or raid writes (unowned: the ruling is silent on the winner); muster (its own `sides_of`) |
| `migrate` | a rung with room; `contain` + `reside` | presence (`move`); exile another (unowned); relocate a court (unowned) |
| `move` | a rung up the ladder | residence (`migrate`); flight from custody (unowned) |
| `oblige` | a seat whose `binds` admits; own; with a term | seat-to-seat fealty (WIDEN with `via`); sentence (`determine`); hostage (unowned) |
| `open_case` | any matter at a place in purview; `remit:determine`; case file + docket | own docketing (`carry`); private accusation (a `petition` kind); appeal (the same verb, nested) |
| `petition` | terms, `to` a person, `from` a rung; own | docket (`carry`); writ downward (`issue`); accusation, demand, challenge (kinds of itself) |
| `reconstruct` | anything in one's own ledger | new information (the other five); decipher (`research`) |
| `release` | the object of one's own live edge, six kinds (`verb_table.yaml:748`) | another's edge (`revoke`); pardon (unowned); waive what is owed you (refused by D-5, `verb_table.yaml:757`) |
| `repudiate` | one's own `commit` | renounce fealty (unowned) |
| `research` | an existing Record | Site (`examine`); person (`interview`); a letter in transit (unowned) |
| `restore` | a Site stood at; raise to ceiling | a body (unowned); stake a works (`build`); damage (unowned) |
| `revoke` | an office via a seat with a basis | resign (`release`); excommunicate, outlaw (unowned); expel an obligee (unowned — and see §7.5); dissolve (unowned); depose a seat with no rung above (unowned: closed roster) |
| `speak` | a referent, nothing carried | a motion (`utter`); a seat's proclamation (unowned) |
| `succeed` | a held office or estate; heir unbound | seat (`confer`); regency (`confer` + term); inheritance at death (unowned) |
| `surveil` | a Rung stood at | a person over time (unowned, `verb_table.yaml:1084`); intercept letters (unowned); plant an agent (unowned) |
| `survey` | a faction, or a person under one, in one's own ledger | a rung (declined, H-169 limit 6: WIDEN); census (unowned); yield assessment (unowned) |
| `tell` | a topic in one's own ledger `to` a known present hearer; `said` | a public (presence covers bystanders); lie (WIDEN, H-183); move convictions (unowned, H-62) |
| `thread_read` | a TS-gated finding | threadwork (deferred, plan 27/29f) |
| `tie / knot` | a bond edge, partner unbound | marriage with terms (same + `transfer` + term); an alliance of seats (unowned) |
| `transfer` | own rung → a rung; `kind`, `amount`; renews obligees via a seat | Records (`give`); seizure (unowned); treaty tribute (needs a treaty state) |
| `utter` | an immutable Proposition | speech (`tell`); binding (`commit`); a seat's edict (unowned) |
| `work` | floor-gated advance of a works | wage labour (unowned); practice (unowned) |

### 3.5 Proposed cuts — none decided

Every verdict below proposes changing a row of the ratified table. None is decided here.

| verb | proposal | what dies | needs_jordan (failed step) |
|---|---|---|---|
| `speak` | cut, or give it `tell`'s `holds` conjunct | speech on a topic the speaker holds nothing about; 104–139 executed corpus acts shift | yes — step 4: §E3 table membership was itself ruled (`verb_table.yaml:442-455,949-960`). Settle first with a corpus run withholding `speak` |
| `repudiate` | fold into `release`, with one earned event kind per closed edge kind | `commitment.ended` unless re-earned by `release`; its alignment cells must be re-keyed | yes — step 4 |
| `work` | fold into `restore`, or give labour a produce write | nothing `restore` lacks in computed play | yes — step 4. Settle by grepping hand-built `work` acts with declared deltas |
| `comply` | compliance is the writ-sourced `transfer`, which earns `compliance.given` beside `transfer.made` | the row | yes — step 3: the triple *comply / evade\|defy / construe* is Jordan's (`verb_table.yaml:737`). One non-transfer term type under H-44 overturns the proposal |
| `evade / defy` | split only when a reader distinguishes covert from open refusal; the merged state reads `withhold` | — | yes — step 3, as `comply` |
| `exchange` | keep; THIN until the counterparty's operands exist | — | yes — step 5: `rosters.yaml:1562-1564` reserves coining those operands for H-94's ruling |
| `carry` | keep; build on `open_case`'s body, writing the petition's `Record.stages` | — | no — H-63 answered by precedent (`open_case` dockets its subject) |

---

## 4. Hooks for the existing 44

*Hook* is how a question forms the act and what it writes; *falsifier* is the observable that would show
it hooked. "Realm ex" means executions in `python -m engine.season.harness.aperture 4 0` (the populated
realm, four seasons, seed 0); the `att/ex` pairs quoted are from `requirements.yaml:674-676`, not re-run.
"Q2" is the question source that names a referent the person holds a claim about. Full blocks are in
Appendix A.

| verb | hook (route · rows) | why | falsifier | blocker · needs_jordan |
|---|---|---|---|---|
| `build` | a question whose referent is a `works` the actor holds · `Site.exists` | housing throttles migration (`effects_migration.py:140-149`) | leaves the always-refused pin (`test_season_shape.py:7624`); realm ex > 0 (65/0) | H-165 limit 2, carried as J-4 · no new row |
| `carry` | the petitioner holds his petition; on `open_case`'s body, writing the petition's `Record.stages` · `DocketItem.matter` | a complaint reaching a bench without a seat's leave | `test_record_kind_fold.py:119` (`..._and_carry_is_not`) flips | H-63, answered by precedent · no |
| `commit` | `_eff_utter` mints the utterer's `hold` on the Proposition, so Q2 can name it · `Tenure.since` | utter → commit → ambition → a quiet-season act | leaves the always-refused pin | H-156; a hold buys budget (`budget.py:57-58`) · no for the hook; H-156 (a)/(b) stays Jordan's |
| `comply` | executor holds the writ after `give`; the writ-sourced `transfer` earns `compliance.given` · `Rung.stores` ×2 | obedience with a trace, so defiance is legible by absence | `compliance.given` in `w.log` from `populated.run` with no hand-built act | H-44, H-94 · yes, if cut (step 3) |
| `confer` | office rides `subject`, conferee rides `to` via the known-person fan (`options.py:827-860`) · `Tenure.since/until` | patronage | realm ex > 0 (70/0) | no referent is a seat [GAP: whether `world_q.reach` admits an office id — not opened] · no |
| `construe` | WITNESS-side, not an act: the content deposit already reads per holder (`witness.py:40,523-540`) · none | misreadings that travel by document | two holders of one writ holding different `content:dispensation` values | H-36 magnitude half, H-44 · no |
| `convene` | pass CALENDAR's events into `witness()` (`driver.py:464`); `open_case` fills the fired slot's date · `Date.due_at`, `DocketItem.matter` | a sitting with a day people act toward | a `date.fired` claim in any ledger (`test_season_shape.py:4307-4316` pins 0) | H-163 limits 2, 4 · no |
| `create_record` | hooked; a computed act mints contentless `text` · `Record.exists`, `Record.stages` | documents to find, carry, forge, burn | corpus executed set; `test_works_founding.py:101` | H-80 · no |
| `destroy_record` | `give`'s shape, built and held (`verb_table.yaml:199`) · `Record.exists` | the only way a document vanishes | `test_u7_own.py:153` flips | H-75; held on H-156 · yes, no new row (H-156) |
| `determine` | a question whose referent is a docketed person in the bench's ground; direct via seat · `Tenure.since`, `DocketItem.matter` | a bench binding men with no player watching | realm ex (1/20); `test_u7_remit.py:278` | H-163 limit 2 (SC lane), H-162 · no |
| `dispatch` | hooked; the named person gets a claim about himself · none | a command the chronicle carries | leaves the never-attempted pin (`test_season_shape.py:8372`) | none · no |
| `establish` | operands outside the closed eight refuse; direct via seat · `Office.exists`, `Office.remit_acts`, `Tenure.payload` | institutions that grow | realm ex > 0 (19/0) | plan position `15c` · no |
| `evade / defy` | held writ; `evade` = no transfer before the term matures; `defy` = a public refusal · none | disobedience others see or miss | `compliance.withheld` from computed play | H-44, H-94 · yes, if split (step 3) |
| `examine` | hooked on a co-located Site · none | a clue that is somewhere | a `finding.made` claim with non-trivial value | work item 4.5 · no |
| `exchange` | needs the counterparty's `kind`/`amount`; `_shift` twice · `Rung.stores` ×2 | trade, scarcity paired both ways | `exchange.made` in `w.log` | H-94 · yes (step 5) |
| `fight` | hooked; any person referent but self · by band | the irreversible personal stake | `test_season_shape.py:12776`; corpus `DEGREES RESOLVED` | H-98; the deontological gate · no |
| `forge` | a faction the forger holds a claim on (`survey`'s cell); `survey`'s mint with perturbed content · `Record.exists`, `Record.forgery_quality` | a false sheet a rival acts on | `test_information_cluster.py:297` stops asserting that no act forges | H-169 limits 2, 5 (a consumer first) · no |
| `found` | as `build` · `Rung.exists`, `Tenure.since` | new hearths | realm ex > 0 (70/0) | H-165 limit 2 (J-4); H-166 · no new row |
| `give` | hooked; the known-person fan · `Tenure.until/since` | a writ reaches the hand that can deny it | `test_give.py:94-399` | none · no |
| `interview` | hooked · none | to be replaced by the Dialogue Lattice (`verb_table.yaml:1054`) | corpus executed set | work item 4.5; ED-FI-0004 · no |
| `issue` | hooked (realm 6/30, with `via`); terms = the executor · `Record.exists` | authority as paper | `test_u7_remit.py:460` | H-94; `15c` · no |
| `levy` | a question whose referent is a full larder in purview (a positive `stores.changed`) · `Rung.stores` ×2 | how a seat eats | realm ex > 0 (23/0); `test_u7_remit.py:201` | H-163 limit 3 · no |
| `march` | hooked in the realm (16/16), never in the corpus (H-175); seam at ENCOUNTER · `Person.body`, `Person.stance` | war that leaves grudges | `test_march.py:323`; leaves the never-attempted pin | H-175, H-149 · no |
| `migrate` | a destination channel: shortfall at home plus a positive `stores.changed` elsewhere in reach, or a founded hearth with room · as `move` | people who leave famine | leaves the always-refused pin | H-168 (H-94) · no |
| `move` | hooked · `Person.travel_leg`, `Tenure.until/since` | presence is the epistemic model | `test_migrate_capacity.py:153` | none · no |
| `oblige` | type clause 1 once a seat can be a referent [UNVERIFIED: whether `reach` admits an office id] · `Tenure.since`, `Tenure.term` | retinues | `test_obligees.py:282` flips; leaves the never-attempted pin | seat referents (H-94/H-54) · no |
| `open_case` | hooked (realm 7/28) · `Record.exists`, `Record.stages`, `DocketItem.matter` | grievances enter the institution | `test_u7_remit.py:246` | H-52 · already registered |
| `petition` | hooked; addressed to its own subject · `Record.exists` | the upward voice | `test_record_kind_fold.py:153` | H-94; closers unbuilt · no |
| `reconstruct` | hooked; a self-feeding loop is visible (`test_season_shape.py:3974-3977`) · none | synthesis that can be wrong | corpus executed set | the obstacle; work item 4.5 · no |
| `release` | a person-side decline in `opening_set` when the actor holds no releasable edge to the referent · `Tenure.until` | resignation, divorce, apostasy | refusals fall from 96% (`requirements.yaml:759-760`) | none · no |
| `repudiate` | cut; `_eff_release` earns a kind per closed edge kind | nothing new | `test_u7_own.py:42` DECLINED tuple shrinks | none · yes (step 4) |
| `research` | hooked · none | archives | corpus executed set | work item 4.5 · no |
| `restore` | hooked (realm 18/82) · `Site.condition` | towns that mend; walls before a march | `test_works_founding.py:237-282` | H-164, H-166 · no |
| `revoke` | office rides `subject`, as `confer` · `Tenure.until` | a lord unmaking a subordinate | realm ex > 0 (15/0) | seat referents; H-91 · no for the hook |
| `speak` | cut, or give it `tell`'s `holds` conjunct · none | — | leaves the executed set; `test_seen_claim.py:55` | none · yes (step 4) |
| `succeed` | heir via the known-person fan; a reader at the vacancy — but `conferral_bases` is closed at appointed/elected/annex (`rosters.yaml:1737-1755`) · `Tenure.since` | dynasties | a `person.died` followed by the heir's `hold` | ED-IN-0256 ruling (2) · yes (step 5) |
| `surveil` | hooked · none | the covert act canon prices (`rosters.yaml:2205`) | corpus executed set | ED-FI-0009; work item 4.5 · no |
| `survey` | hooked (realm 10/165) · `Record.exists` | a stake once something reads the sheet | `test_information_cluster.py:146,204` | H-169 limit 5 · no |
| `tell` | hooked · none (WITNESS) | rumour and the chain of tellers | `test_told_by_channel.py:1042` | `sigma`'s `REFUSED` raises an uncaught `Unspecified` (`resolve.py:585-590`) · no |
| `thread_read` | a per-person TS value and a gate stem; `knowledge_kinds` is the taxonomy half · none | P-08's barrier made mechanical | enters `resolvable_verbs()` | H-85; plan 27/29f · no |
| `tie / knot` | partner via the known-person fan; `tie`'s reader is `teller_weight`'s relation term; build as two rows · `Tenure.since` | telling knits people | `tie / knot` executes > 0 in `aperture 1 0` | H-182; `29f` owns `knot` · no |
| `transfer` | hooked · `Rung.stores` ×2, `Tenure.term` | relief, tribute, pay | `test_season_shape.py:9328`; `test_term_upkeep.py` | H-158 · no |
| `utter` | hooked but reaches nobody's questions; mint the utterer's `hold` · `Proposition.exists` (+ `Tenure.since`) | vows that bind the speaker | a `commit` executing on a `prop:` id in `populated.run` | H-92, the cost of a hold · no |
| `work` | fold into `restore`, or give labour a produce write · `Site.condition` | nothing `restore` lacks | leaves the always-refused pin | H-165 limit 2 · yes (step 4) |

### 4.1 Dependency order (pass 1)

1. **A second operand channel** beyond the question's one referent (`options.py:741-746`; H-94/H-54) —
   gates `confer`, `revoke`, `oblige`, `determine` (limit 2), `levy` (limit 3), `migrate`, `exchange`,
   `establish` (`15c`). This is the same enabler §8.1 needs for the new verbs.
2. `utter` mints a hold → `commit` binds → `ambitions`/need questions → `repudiate` folds into `release`.
3. `give` puts a writ in the executor's hand → `comply`, `evade / defy`, `construe` become formable →
   H-44 decides what compliance performs.
4. CALENDAR events reach WITNESS and `open_case` fills a fired slot → `convene` → `determine` (H-163
   limits 2, 4; SC lane).
5. The J-4 works channel → `found`, `build`, `work`; then the `work`/`restore` fold.
6. H-156's ruling → `destroy_record`'s held shape, `found`/`build` formation policy, `commit`'s cost.
7. A sheet consumer (H-169 limit 5) → `forge` → `destroy_record` as the burn.
8. `teller_weight`'s relation reader → `_eff_tie`; `knot` after `29f`.
9. A ruling on succession as a conferral basis → `succeed`'s heir operand and a reader at the vacancy.
10. The investigation degree producer (work item 4.5) → the six findings stop being one act with six
    preconditions; `thread_read` additionally waits on H-85.

---

## 5. Coverage

Pass 2 grouped the 707 candidates into 61 act families and classified each against §3.4:

- **COVERED** — an existing verb carries the family's central act, sometimes with a new Record kind as
  data (a `petition` of kind `accusation` is still `petition`);
- **WIDENED** — an existing verb carries it once one named reach widens (§7.5);
- **GAP** — no verb can; filled by a new verb (§7.1–§7.4);
- **OUTCOME** — the family names a result, not a choice; by direction 3's logic it is not a verb;
- **SYSTEM** — a property of a mechanism, a seam or a loop stage, not an act (§8.3).

**Counts, one primary class per family (author's recount):** COVERED 29 · WIDENED 9 · GAP 14, plus 1
deferred (threadwork) · OUTCOME 3 · SYSTEM 5 — 61 in all. Verbs: 10 widened, 14 new. [CORRECTION: pass 2
reported COVERED 31 · WIDENED 10 · GAP 14 + 1 · OUTCOME 3 · SYSTEM 6, but its WIDENED figure counts verbs
rather than families and it assigns no single class to the families it splits. Appendix B gives each
family one class and its evidence.]

| class | families (Appendix B numbers) |
|---|---|
| COVERED (29) | 1 question a person · 2 inspect a place, body or object · 3 read and decipher records · 5 evidence board · 6 denounce, accuse · 7 open an inquiry or impeachment · 8 summons, writ, warrant, charter · 11 confess, swear, abjure · 15 elect · 16 appoint, invest, ennoble · 17 depose · 18 resign · 23 muster · 31 spy, infiltrate, run informants · 33 expose, publish · 34 blackmail · 35 bribe, gift, subsidy · 36 court, marry · 39 trade, venality · 41 build, found, charter · 42 survey, census, visitation · 43 envoy, legate · 44 feast, coronation, progress · 49 claim, coup, revolt · 50 mediate, appeal, stay, adjourn · 51 recognise, endorse · 54 defect, poach · 55 challenge and accept · 57 regency through a seat |
| WIDENED (9) | 4 watch a place, tail a person (`surveil` → Person) · 9 hear, try, judge (`determine` contested) · 12 excommunicate, absolve (`determine` disposing `bar`) · 14 motion, debate, vote (`commit` through a seat) · 19 heir, regency (`confer` + term) · 20 homage, fealty (`oblige` through a seat) · 29 outlaw, banish (`determine` disposing `bar`) · 37 slander, rumour (`tell` with authored `said`) · 53 admit, expel (`revoke` closing an `oblige` — **withdrawn here**, §7.5; with it withdrawn, family 53 is COVERED by `oblige` and lapse, and WIDENED falls to 8) |
| GAP (14 + 1) | 13 edict, law, emergency (`proclaim`) · 21 declare war (`proclaim`, kind `war`) · 22 truce, peace, treaty, alliance, cession (`covenant`; cession by widened `give`) · 24 siege, blockade (`besiege`) · 26 arrest, custody, ransom, hostage (`detain`, `pardon`) · 27 interrogate (`interrogate`) · 28 execute (`execute`, needs Jordan) · 30 seize, confiscate, search (`seize`) · 32 cover identity, deniability (`conceal`) · 38 persuade, convert, preach (`argue`) · 40 borrow, distrain (`covenant` kind `debt` + `seize`) · 45 heal, rest (`tend`) · 46 train, educate (`train`) · 52 damage, raze (`sabotage`, `raze`) — and 47 thread operations, **deferred** to plan positions 27/29f (`verb_table.yaml:1103`) |
| OUTCOME (3) | 10 sentence (the disposal's kind; its parts are `oblige`, `detain`, `transfer`/`levy`, `execute`) · 25 conquer, raid, usurp (a won `march`) · 48 murder (a `fight` whose band is `Felled`, with `conceal`) — and, by direction 3, `kill` and `wound` |
| SYSTEM (5) | 56 privileged counsel · 58 combat and battle moves (inside the seams) · 59 negotiation moves (inside a bout) · 60 events (disaster, plague, dearth, mutiny, death, succession, heresy outbreak, clocks, endings) · 61 inner mechanics (§8.3) |

[NULL: all 61 families — examined for a family needing a fifth eligibility kind or a non-person actor;
none found. Every faction-scale row resolved to an office-holder's act through a seat.]

### 5.1 What each source contributed

What each source supplied that the others did not, and which gaps and states it stands behind. The
per-family evidence is Appendix B.

| source (rows) | distinctive contribution | gaps and states it backs |
|---|---|---|
| `research/` (80) | faction- and office-scale acts the setting's own research catalogued — sanctions put to a vote of factions, war declared with a compliance window, cession and tributary status, leagues, confinement and hostage-kin, the Riskbreakers' Shadow Renown and Deniability Debt meters — and nine event cards | `proclaim`, `covenant`, `detain`, `execute`, `pardon`, `conceal`; war, treaty, embargo, hostage |
| governance proposals (67) | the 25 provisional faction actions; the proceedings design (speech kinds as data, hearing, quorum, stay, appeal by nesting, interposition, dissent); the inquisition procedure of `proposals/2026-09-04-social-contest-branches/03_INQUIRY.md` (a 2–4-season case, one interrogation per season, a three-way verdict, an excommunication tribunal, abjuration, a parliamentary stay); Riskbreaker operations | the contested `determine`, `interrogate`, `seize`, `conceal`; excommunication, sentence; the faction map (§8.2) |
| narrative and play proposals (80) | the closers named and never built (waive, depose, fray, rescind, withdraw, abolish); the pursuit-basis worksheet's kill/wound and challenge/accept rulings; cover, planted evidence, infiltration, outlawry | `conceal`, `seize`, `train`; widened `tell`; the single outlawry carrier |
| season-loop demand (77) | what the running code and its registers say cannot be expressed, by hole id and case count: no custody kind; `church_standing` with no producer; a sentence read as a job (H-173); a graded hearing (H-162) and the four unseeded procedure games (`arrangements.yaml:16-21`); seizure (H-84); concealment (12 cases); recruiting (13); nothing raises `Person.body`; `Person.capability` retired; nothing ends a place (H-166) | `detain`, `seize`, `conceal`, `tend`, `train`, `raze`, `sabotage`, `argue`; custody, excommunication, sentence |
| detective games (107) | the investigation family confirmed in all seven; *Pentiment*'s church hearing, judgement and execution; *L.A. Noire*'s read of a lie and the charge; arrest in three games; evidence decay; the time budget. **Negative:** no warrant, covert identity or distinct confession act verified in any of the seven | `detain`, `interrogate`, `execute`; widened `surveil`; §8.3 |
| CK3 and RTK (107) | CK3: crime as a standing legal basis for imprisonment and revocation; imprison, torture, execute, ransom; hooks and blackmail; casus belli, war goals, truces; fealty and vassal contracts; excommunication and holy war — every act a character's, as Valoria rules. RTK XIV: the schemes line (sabotage, estrangement, incited defection), alliances, submission demands — there the force itself acts | `detain`, `execute`, `pardon`, `proclaim` (war), `covenant`, `sabotage`, `raze`; widened `oblige`, `tell`, `march` |
| governance history (189) | procedure, step by step: the parliamentary motion, division, supply, impeachment and prorogation; the royal writ, edict, homage and *diffidatio*, pardon, regency; Venice's lot-and-ballot election, quorum, the Ten, the *bocca di leone*, the Avogadori's suspension; church justice from denunciation and the edict of grace through citation, interrogation, torture under limits, sentence, abjuration, relaxation, confiscation, excommunication and interdict; secular warrant, arrest, bail, *habeas corpus*, ordeal, execution, informants, interception, double agents | the procedural spine of the Active Inquisition chain (§8.2); `detain`, `interrogate`, `seize`, `pardon`, `execute`, `proclaim`; widened `commit` (the vote) and `oblige` (homage); custody, excommunication, interdict, heresy declared, outlawry |

---

## 6. States

Every state below is an **output**: the choices that set them are `proclaim`, `covenant`, `determine`,
`detain`, `conceal`, `issue`, `commit` and `oblige`, and nothing names a state as a verb.

**Carrier rules the code already enforces.** An instrument is a `Record` of a rostered kind with **exact**
keys — `Record.__post_init__` refuses a key set that differs in either direction, and refuses an unlisted
kind; a Record kind may never also be a tenure kind (`rosters.yaml:164-215`). A standing between a person
and a seat is a `Tenure`. `tenure_kinds` is `open: true` (`rosters.yaml:101-115`), but every kind needs an
opener (loader invariant 6, `rosters.yaml:116`) and must either sit in `release`'s declared domain or be
excluded by `RELEASABLE_KINDS` (`engine/season/data/rosters.py:453`); the loader compares the two, so a
kind with no closer fails the load (`verb_table.yaml:754`). Parties are always seat-holders. "Reader"
names code; **ORPHAN** marks a state no code would read — §0.05's dead carrier — and a proposal here is to
ship no kind without its reader.

| # | state | carrier | parties | set / ended by | readers | duration · drama | instrument | status |
|---|---|---|---|---|---|---|---|---|
| 1 | **War** | Record kind `war` {terms: the casus-belli Proposition, at: the proclaiming seat's rung, against: a rung} | the proclaiming seat; the target rung's holding seat | set by `proclaim`; ended by a `peace` covenant between the same seats [GAP: the closing mechanism — reader-side precedence or `destroy_record` — is unspecified] | proposed `loop/sides.py::sides_of` (a march without a war is H-151's own-faction question), `_ch_chronicle`; **ORPHAN** until `sides_of` reads it | until peace · marches form between enemies, allies muster | `aperture` `march` counts split by war present/absent | GAP |
| 2 | **Truce** | `covenant` kind `truce` {terms, parties, at, until}; term as `Record.stages` (matures at MAT, `write_matrix.yaml:266-272`) | two seats | set by `covenant`; ends by maturation (no actor) or breach (a `march`) | proposed `sides_of` | the term · a truce lapsing on a fixed season | a `march` refused, or flagged as breach, between truced seats | GAP |
| 3 | **Peace / treaty / alliance / league** | `covenant` kinds `peace`, `treaty`, `alliance`; both holders `commit` through their seats to the instrument's Proposition | two or more seats | set by `covenant` + `commit`; ended by term or breach | proposed `mustered` (allies' persons join sides), `_renewals` (tribute as upkeep), `exchange` | term or breach · an ally's war pulls you in; lapsed tribute breaks a peace | allied persons appear in a `march`'s sides | GAP |
| 4 | **Vassalage / fealty** | `oblige` opened through a seat (widened `oblige`): seat A's holder obliged to seat B; term renewed by `transfer` upkeep (`verb_table.yaml:1149`) | two seats | set by `oblige`; ended by `release` (*diffidatio*) or lapse | `state/gate.py::purview_reaches` (H-101: "nothing can be under anything", `hole_register.yaml:1961`) | the term · unpaid fealty lapses and the ladder breaks | `purview_reaches` true across the two seats | GAP (H-101) |
| 5 | **Hostage** | a `custody` edge (13) under a `covenant` | the giving and receiving seats | set by `detain` under the covenant; ended by `pardon` on performance | proposed `sides_of` (the hostage's faction will not march) | the covenant's term · breach costs a life or a release | `sides_of` excludes the hostage's side | GAP |
| 6 | **Embargo** | `proclaim` kind `embargo` {at, against} | a seat; a target rung | set by `proclaim` | proposed: `exchange`/`transfer` across the two rungs refuse; **ORPHAN** until they do | until lifted · trade reroutes or starves | `transfer.refused` between the rungs | GAP |
| 7 | **Siege / blockade** | Record kind `siege` {at, by}, minted by `besiege` | the besieging seat; the besieged rung | set by `besiege`; ended by a won relief `march`, `destroy_record` by the besieger, or a covenant | proposed: MATTER subsistence draw at the rung, `transfer` into it, `move` paths | until relieved · a larder runs down with no actor | subsistence at the rung falls with no act | GAP |
| 8 | **Excommunication** | Tenure kind `bar` (person → Church seat), opened by `determine` under a Church arrangement whose `disposes:` names it (the key exists, `arrangements.yaml:97`) | the barred person; the Church seat | set by `determine`; ended by `pardon` | proposed `_req_oblige`/`confer` (a barred person cannot serve or be seated), `_ch_chronicle`; deposits the `church_standing` claim, which nothing produces today (`rosters.yaml:576`) | until pardon · clients' commits waver | a `confer` refused on a barred person | GAP |
| 9 | **Interdict** | `proclaim` kind `interdict` {at} | the Church seat; a place | set by `proclaim` | none — no rite verb exists to refuse; **ORPHAN** | until lifted · a town presses its ruler | — (ship only with a reader) | GAP |
| 10 | **Heresy declared** | a Proposition + `proclaim` kind `condemnation` {terms: the Proposition} | the Church seat; everyone committed to it | set by `proclaim` | proposed: `open_case`/accusation ground = a live `commit` to a condemned Proposition | standing · a quiet believer becomes accusable | an accusation whose ground is a condemned `commit` | GAP |
| 11 | **Accusation pending** | `petition` kind `accusation` {terms: accused, to: bench holder, from} + `DocketItem.matter` | accuser; accused; bench | set by `petition`, docketed by `open_case`/`carry` | the docket (exists) | until determined · a denunciation enters the docket | `DocketItem` naming the accused | COVERED (a kind) |
| 12 | **Warrant** | `issue` kind `warrant` {terms: person, to: executor, at} | the issuing seat; executor; the named person | set by `issue` | `detain`'s and `seize`'s precondition (an own-ledger `content:warrant`) | until executed or expired · the hand that holds it can act | `detain` executes on a held warrant | COVERED (a kind), once §8.1 separates terms from addressee |
| 13 | **Custody** | Tenure kind `custody` (prisoner → holding seat), opened by `detain`; the term is bail | prisoner; the holding seat | set by `detain`; ended by `pardon` or a second `detain` (transfer of custody — "relax to the secular arm") | proposed: `move`/`migrate` refuse, `sides_of` excludes, a `budget` floor | until released · a prisoner's faction petitions, ransoms or marches | `move` refused for a person in custody | GAP |
| 14 | **Outlawry** | a person: Tenure kind `bar` to the realm's seat, opened by `determine`. An organisation: `condemnation` (10) against its Proposition, since a faction's identity is a Proposition its members commit to | as carrier | `determine`; `proclaim` | proposed: `detain` eligibility widens to `own` against an outlaw | until pardon · anyone may seize | `detain` by a seatless person on an outlaw | GAP |
| 15 | **Sentence in force** | the disposal's **kind** — `oblige` (service), `custody`, `bar` — chosen by the arrangement's `disposes:` | convict; bench | `determine` | every reader of `oblige` sees a job today (H-173, `hole_register.yaml:3740`) | by kind · a sentence that reads as a sentence | two convicts under different kinds read differently by `_renewals` | GAP (H-173) |
| 16 | **Concealed identity** | Record kind `cover` {who, as}, held by the agent, minted by `conceal` | the agent | set by `conceal`; exposed when the Record is destroyed or a claim about it lands | proposed `state/attribution` (an anchor resolves to `as`), `seen` claims | until exposed · a Riskbreaker's act lands on a false name | an Event's anchor resolves to the cover id | GAP |
| 17 | **Exposure** | no new field — `exposure` is forbidden as an axis name (`rosters.yaml:490`): a Query over others' `seen` claims naming the agent (`known_persons`' source) | the agent; observers | no act writes it | the Query | rising with conspicuous acts · detection debt | the Query's count over a run | COVERED (as a Query proposal) |
| 18 | **Claim to a title** | Record kind `claim` {terms: seat or rung, from: basis}, minted by `create_record` or `forge` | claimant | `create_record`, `forge` | proposed `confer` (a claimant), `proclaim` war (casus belli), `commit` (recognition); **ORPHAN** until one reads it | standing · a forged pretext starts a war | a `war` Record whose terms name a claim | GAP |
| 19 | **Regency / delegation** | a `hold` with `Tenure.term` (widened `confer`); delegation already rides `Act.via` (`state/carriers.py:543-550`) | regent; the seat | `confer` | the gate's seat check (`loop/resolve.py:114-118`) | the term · a puppet ruler | an act executed `via` a held seat by a regent | COVERED |
| 20 | **Debt** | `covenant` kind `debt` {terms, to, from, amount, until} | creditor; debtor | `covenant`; ended by payment (`transfer`) or distraint (`seize`) | proposed `seize` (distrain), `transfer` renewal | the term · a lender's standing rises with a default | a `seize` whose ground is a lapsed debt | GAP |
| 21 | **Faction membership / recognition** | `commit` to a Proposition (exists; per pass 2, `loop/sides.py:65-68`) | member | `commit`, `release` | `sides_of`, `faction_q` | standing | — | COVERED |
| 22 | **Charter / privilege / exemption** | `issue` kind `charter` | the granting seat; grantee | `issue` | proposed `purview_reaches` exemption | standing · a free town outside a lord's reach | `purview_reaches` false across a charter | COVERED (kind); reader GAP |
| 23 | **Emergency / martial rule** | `proclaim` kind `emergency` {at} | a seat; a place | `proclaim` | none — **ORPHAN** | until lifted · uniform friction across a territory | — (ship only with a reader) | GAP |
| 24 | **Scheme** | a Proposition the conspirators `commit` to, plus `cover` Records; progress as `Record.stages` | conspirators | `utter`, `commit`, `conceal` | secrecy decay is SYSTEM (§8.3) | until discovered or done | — | COVERED (composed) |

### 6.1 Why `custody` and `bar` must be their own kinds — and what that touches

A disposal today is an `oblige`, and **by ruling a convict may release it himself**: `verb_table.yaml:757`
records that `determine`'s finding opens an `oblige` owned by the party it binds (proceedings C-1, RULED
A), so *"a convict can discharge his own penance"*, and that D-5 (Jordan, 2026-09-06, *"second-person
lever stays refused"*) leaves that the only route — *"no creditor verb, no `call_in`, no obligee-side
closer on an obligation exists or will"*. The code agrees: `_req_release` admits any live edge of a
releasable kind whose subject is the actor (`loop/predicates.py:338-340`). Custody built as an `oblige`
would therefore let a prisoner walk out by releasing it. Hence two new tenure kinds, excluded from
`RELEASABLE_KINDS` on the precedent of `contain` and `reside`, which are excluded because something other
than their holder ends them (`data/rosters.py:448-453`).

This narrows C-1 rather than contradicting it: a sentence of service stays a self-dischargeable `oblige`,
priced by reception as ruled; only physical custody and the two exclusions (Church, realm) become kinds
their holder cannot close. It follows that `pardon` may close `custody` and `bar` and **never an
`oblige`** (§7.1). [ASSUMPTION: D-5 governs obligations, not every edge a seat holds on a person — basis:
its own words, and `revoke`, which closes another's `hold` through a basis, coexists with it.] The four
procedure games the source left unseeded — interrogation, legal trial, tribunal, inquisition hearing —
were left out precisely because their `disposes:` tenure was an unresolved placeholder
(`arrangements.yaml:16-21`); `custody` and `bar` are candidate answers.

**New Record kinds proposed:** `accusation`, `case`, `warrant`, `summons`, `charter`, `edict`, `war`,
`truce`, `peace`, `treaty`, `alliance`, `debt`, `embargo`, `interdict`, `condemnation`, `emergency`,
`siege`, `cover`, `claim`. **New Tenure kinds:** `custody`, `bar`. No name appears on both lists.

---

## 7. New verbs

Fourteen rows, written table-ready in the table's own columns. Grade is `assumption` for thirteen and
`absent` for `execute`. Evidence is written out; the bracketed id is the extractor row, kept as a
courtesy. **None needs a new `remit_acts` value**: every remit eligibility below is `issue`, `determine`
or `dispatch`, already on the roster (`rosters.yaml:302`), so H-52's warning that adding a value would
close it by hardcoding is not engaged.

### 7.1 Law and custody

#### `detain`
*L* detinere *'hold back', via OF* detenir. **Fit:** FITS — it names a holding that lasts, which is what
the `custody` edge is; *arrest* (OF *arester* 'stop') names only the moment.

- **row:** stratum `contested_physical` · scale person · eligibility `remit:dispatch`, through a seat whose
  portfolio is enforcement (Knights of the Peace, "law enforcement"; Royal Investigators, "court
  prosecution", `rosters.yaml:1542-1543`) · beneficiary none · counterparty `subject`
- **requires:** `existence` of `subject` kind Person ∧ a held `warrant` naming the subject (an own-ledger
  `content:warrant` read)
- **writes · emits:** `Tenure.since`, new kind `custody` (prisoner → holding seat) · `custody.taken`;
  refusal `detain.refused`, `detain.unauthorized`
- **contests:** `a standing` (sigma, interim); Failure = refused, the subject got away [CONFIDENCE: medium
  — whether resisting arrest is a contest of standing or of the body; if the body, a Failure should hand
  off to `fight` rather than carry its own prize]
- **producer · composes:** Q2 on a held warrant (§8.1) · `issue` (warrant), `pardon`, `interrogate`,
  `execute`; states 12–14
- **CONFLICTS:** `fight` — axis: write row and prize (`detain` writes no body); `oblige` — axis:
  eligibility and counterparty (`oblige` is one's own and consensual)
- **falsifier:** `aperture 1 0` `detain` ex > 0; `move` refused for a person in custody
- **evidence:** *L.A. Noire* — Cole Phelps arrests a suspect [G1-67, memory-sure]; *Shadows of Doubt* — the
  player arrests a suspect the Enforcers will not chase, for the bounty [G1-90]; *Disco Elysium* — arrest as
  an RCM officer [G1-32, UNVERIFIED]; CK3 — imprison a criminal, at no tyranny cost when the crime is known
  [G2-47]; the English constable's arrest and watch and ward [H1-160]; the season loop has no custody kind
  (`rosters.yaml:115`) while NPC-088 needs "protected / exposed / arrested / dead" as a persistent fact
  and ARC-23 a capture instead of a death [C-05].
- **blocker · needs_jordan:** §8.1; the `tenure_kinds` addition and its `RELEASABLE_KINDS` exclusion (§6.1)
  · no

#### `interrogate`
*L* interrogare *'ask'* (inter + rogare). **Fit:** FITS; set apart from `interview` by custody and by what
is at stake.

- **row:** `social` · person · eligibility `remit:determine` via a seat · beneficiary actor · counterparty
  `subject`
- **requires:** `existence` of `subject` kind Person ∧ the subject in custody (a new stem, `relation of
  subject, held_in_custody`, or read at the effect)
- **writes · emits:** `[]` · pass 2: by degree `confession.made` / `finding.made` / `finding.none`;
  refusal `interrogation.refused`
- **contests:** `a proposition` (social_contest). Pass 2's ground: the Church Tribunal is accusatorial —
  "an Inquisitor investigating whether the accused committed an act" (`systems/social_contest/sim/contest/modes.py:37-52`),
  and `rosters.yaml:1031` bars only the six findings.
  [DISAGREE: `rosters.yaml:1031` forbids making investigation a contest so that it becomes gradeable — "forcing
  one mechanism's shape onto another because it is the one that exists". An `interrogate` whose degrees emit
  `finding.made`/`finding.none` is that route by another door. Keep the contest only if its outputs are the
  charge's disposition — `confession.made` (the accused concedes; `confession` is already a rostered proof,
  `rosters.yaml:1828`) or `confession.withheld` — and leave findings to the six. Both readings are kept.]
- **producer · composes:** Q2 on a docketed custody · `detain`, `open_case`, `determine` (which reads the
  `confession` proof)
- **CONFLICTS:** `interview` — axis: eligibility (remit vs own), the counterparty's state (held), the prize
- **falsifier:** the corpus `DEGREES RESOLVED` histogram (`harness/corpus_run.py:993`) gains this prize's
  bands
- **evidence:** *Disco Elysium* — pressing a subject (Half Light); a failed attempt locks dialogue
  [G1-22, snippet]; *L.A. Noire* — reading Truth / Doubt / Lie and accusing a lie with contradicting
  evidence [G1-64, G1-65]; the inquisitor's interrogation with a notary, witnesses' names withheld
  [H1-121]; torture under limits — once, bounded, no bloodshed, only where proof is "virtually certain"
  (*Ad extirpanda*) [H1-122]; the inquiry proposal's one interrogation scene per season, burden on the
  accuser, silence convicts (`proposals/2026-09-04-social-contest-branches/03_INQUIRY.md:176-193`)
  [P1-38]; the social-contest `inquiry` game is a stub whose source is "Church Tribunal / Inquisition"
  [C-01].
- **blocker · needs_jordan:** custody (state 13); torture is a fixture of the obstacle, not a verb · no

#### `seize`
*OF* saisir *'put in possession, take'* (cf. *seisin*), *from a Frankish or Medieval Latin legal root*
[UNVERIFIED]. **Fit:** FITS.

- **row:** `uncontested_material` · person/settlement · eligibility `remit:issue` via a seat, with a held
  warrant · beneficiary none · counterparty `to` (the holder)
- **requires:** `existence` of `subject` kind Record ∧ the actor does not already hold it (the grammar has
  no negation, so the effect declines a self-seizure)
- **writes · emits:** `Tenure.until`, `Tenure.since` — the holder's `hold` closes and the seat-holder's
  opens, under a new gate basis `seizure` = purview + warrant (`tenure_write_basis`, `state/gate.py:538`)
  · `record.seized`; refusal `seize.refused`, `seize.unauthorized`
- **contests:** none
- **producer · composes:** Q2 on a Record named in a held warrant · `issue`, `destroy_record` (burn it
  after), `levy` (the stores half)
- **CONFLICTS:** `give` — axis: consent and eligibility; `levy` — axis: object (Record vs stores)
- **falsifier:** realm ex > 0; a seat cannot seize a seat (in `test_give.py:285`'s style)
- **evidence:** the Cardinal of Justice's portfolio includes "text suppression" (`rosters.yaml:1536`), and
  NPC-088's copied text can be found and taken [C-08]; `give` is the only Record mover and it is
  consensual (H-84); confiscating a heretic's goods in thirds (*Ad extirpanda*; Spanish practice)
  [H1-132]; the index and seizure of copies [H1-134]; pursuivants searching premises and seizing papers
  on warrant [H1-175]; the Church's mass seizure of territory declared by an Archbishop (corpus-rebuild
  annex A, `:477-483`) [P1-14]; nationalising church lands and foreign charters [R1-12].
- **blocker · needs_jordan:** §8.1; the gate basis · no

#### `pardon`
*OF* pardoner *← ML* perdonare *'grant wholly'*. **Fit:** FITS.

- **row:** `binding_decision` · settlement · eligibility `remit:determine` via the seat that holds the
  disposal · beneficiary `subject` · counterparty —
- **requires:** a live disposal edge **of kind `custody` or `bar`** whose object is the exercised seat
  [CORRECTION: pass 2 left the kind open "over six kinds". An `oblige` disposal is self-releasable by ruling
  and D-5 bars an obligee-side closer of an obligation (§6.1), so `pardon` never closes an `oblige`. On
  this reading it follows `revoke`'s precedent — a seat closing another's edge under a basis — and does not
  touch D-5's object.]
- **writes · emits:** `Tenure.until` · `disposal.lifted`; refusal `pardon.refused`
- **contests:** none
- **producer · composes:** Q2 on the prisoner or the barred (the post-remit channel already deposits to
  those a seat binds) · `determine`, `detain`; states 8, 13–15
- **CONFLICTS:** `release` — axis: whose edge (another's, closed by the object; not one's own, closed by the
  subject); `revoke` — axis: edge kind (a disposal, not a `hold`) and basis (`may_determine`, not
  revocation)
- **falsifier:** a `custody` edge closes with `disposal.lifted` in `w.log` and the former prisoner's `move`
  is admitted the next season. [CORRECTION: pass 2's falsifier — `test_u7_remit.py:350`'s "already bound"
  refusal becoming re-openable — tests an `oblige` disposal and falls with the scope above.]
- **evidence:** the king's pardon, grace and remission, which by the Act of Settlement 1701 cannot bar an
  impeachment [H1-63]; the Great Council of Venice granting grace [H1-115]; absolution and reconciliation
  of a penitent [H1-128]; bail and *habeas corpus* as secular releases [H1-163, H1-173]; CK3 — grant a
  pardon, release or ransom a prisoner [G2-51]; reversing a verdict, restoring standing posthumously
  [R1-42]; reversing an excommunication by penance or a Grand Debate [P1-43].
- **blocker · needs_jordan:** the two disposal kinds (§6) · no

#### `execute`
*L* exsequi *'follow out', via OF* executer; *'put to death' is the late-medieval sense of carrying out a
sentence.* **Fit:** FITS as English — but it is the one proposal whose write is the outcome direction 3
says a character cannot choose.

- **row:** `contested_physical` · settlement · eligibility `remit:dispatch` via a seat · beneficiary none
  · counterparty `subject`
- **requires:** the subject in custody under a death disposal [GAP: no disposal kind carries "death";
  pass 2 names none]
- **writes · emits:** `Person.exists`, `Person.body`, `Tenure.until` (the kill cascade,
  `effects_combat.py:126-129`) · `person.died`; refusal `execute.refused`
- **contests:** none — which is the point, and the risk
- **composes:** `determine`, `detain`
- **CONFLICTS:** `fight` — axis: prize (none) and eligibility (remit)
- **falsifier:** a `person.died` with no `fight` act among its causes
- **evidence:** *Pentiment* — the condemned put to death after the Archdeacon's judgement [G1-13]; CK3 —
  execute a prisoner, raising dread [G2-49]; relaxation of a relapsed heretic to the secular arm, which
  burns him, because clerics may not shed blood (Lateran IV, canon 18) [H1-130]; the sheriff or hangman
  carrying out a sentence [H1-174]; fratricide, forced suicide, scapegoat execution [R1-36].
- **grade · needs_jordan:** `absent` · **yes** — step 5. Two defensible games: (a) judicial killing by
  fiat, a direct write; (b) death only through the combat seam, the prisoner's resistance near nil.
  Jordan's 2026-09-02 *"you can't just kill or wound"* (`verb_table.yaml:468`) concerned choosing an
  outcome inside a fight, not a sentence. **Direction 3, read literally, rules out (a)**; it was hedged and
  spoken about `kill` and `wound`, so this document does not treat it as deciding `execute`, and records
  that it leans to (b). Note also that under the `remit_default` test fixture every seated office holds
  every remit act (`rosters.yaml:304-310`), so `remit:dispatch` would open `execute` to every seat-holder
  in test worlds.

### 7.2 Polity instruments

#### `proclaim`
*L* proclamare *'cry out'*. **Fit:** FITS.

- **row:** `binding_decision` · province/realm (the seat's rung) · eligibility `remit:issue` via a seat ·
  beneficiary none · counterparty — (the addressee is a place, `at`/`against`; non-operand keys are read
  as declared, per pass 2 at `effects_information.py:85`)
- **requires:** `basis` of `subject`, purview — the place lies in the seat's purview; for `war` it must
  not (the conjunct keys on the kind)
- **writes · emits:** `Record.exists`, kinds `edict`, `war`, `embargo`, `interdict`, `condemnation`,
  `emergency` [CORRECTION: pass 2 also lists `outlawry`; dropped, §6 state 14] · `proclamation.made`;
  refusal `proclaim.unauthorized`, `proclaim.refused`
- **contests:** none
- **producer · composes:** a need question (an OUGHT about a place) or Q2 on a rung in purview; the
  chronicle broadcasts it, as a `binding_decision` (`epistemic.py:553-554`) · `covenant`, `march`,
  `detain`; states 1, 6, 9, 10, 23
- **CONFLICTS:** `issue` — axis: counterparty (`to` a person vs a place) and the executor conjunct (the
  `issue` cell refuses a rung, `verb_table.yaml:427`); `utter` — axis: eligibility (remit vs own) and
  Record vs Proposition
- **falsifier:** enters the corpus executed set; `told_by` claims appear (the 2026-10-03 corpus run
  found 0 of 418 person-instances holding one)
- **evidence:** the royal edict, *ordonnance* or proclamation — general rule by royal word, curbed by the
  Case of Proclamations 1610 [H1-54]; the inquisitor's edict of grace opening a 30–40-day window for
  self-denunciation [H1-117]; edicts, emergency decrees and royal warrants overriding an assembly
  [R1-43]; published proscription lists [R1-34]; the Crown's Policy Instrument [P1-60]; censure, embargo
  and outlawry in the faction roster [P1-11]; a state of emergency suspending ordinary rules [C-32]; a
  graded war posture [C-38]; CK3 — declare war on a casus belli, or a holy war [G2-08, G2-55]; war
  declared on a casus belli held as a record [P2-18].
- **blocker · needs_jordan:** a reader per kind (§6); ship no kind without one · no

#### `covenant`
*OF* covenant, *present participle of* convenir *'agree' ← L* convenire. **Fit:** FITS [CONFIDENCE: medium
— the root it shares with `convene` and its religious sense in a setting with a Church are the risks;
`pact` (L *pactum*) is the alternative].

- **row:** `social` · settlement and up · eligibility `remit:issue` via a seat (or `own`, for a private
  debt) · beneficiary `to` · counterparty `to` (the other seat's holder)
- **requires:** `existence` of `to` kind Person ∧ `existence` of `subject` kind Proposition (the terms are
  uttered first)
- **writes · emits:** `Record.exists`, kinds `treaty`, `peace`, `truce`, `alliance`, `debt`, with
  `Record.stages` as the term; acceptance is both holders' `commit` (widened) to the terms ·
  `covenant.offered`; refusal `covenant.refused`
- **contests:** none — acceptance is the counterparty's own act [UNVERIFIED: pass 2 cites ED-IN-0210
  ruling 2 for this two-sidedness; not opened]
- **producer · composes:** the known-person fan (`options.py:827-860`) over seat-holders the actor knows ·
  `utter`, `commit`, `transfer` (tribute renews), `march` (breach)
- **CONFLICTS:** `issue` — axis: purview (a writ reaches down; a covenant reaches across, so the authority
  conjunct is dropped); `petition` — axis: eligibility (a seat) and the two-sided commit
- **falsifier:** a `commit` by the addressee to the covenant's Proposition in `w.log`
- **evidence:** negotiating, ratifying or letting lapse a treaty, tribute or terms of surrender [R1-06];
  a league of towns [R1-15]; Treaty and Diplomacy in the faction roster, the Formal Crown Treaty being
  Crown-only [P1-07]; settlement as the split of a jointly created surplus, composing `utter` and `commit`
  (`proposals/2026-09-04-social-contest-branches/02_NEGOTIATION.md:36-50`) [P1-65]; CK3 — white peace,
  enforced demands, a purchased truce [G2-14]; RTK XIV — apply for or dissolve an alliance [G2-96]; five
  cases ask to conclude, renew or repair a binding agreement [C-40]; the Venetian Senate deciding war and
  peace [H1-99]; hostages exchanged as surety for a treaty [H1-75].
- **blocker · needs_jordan:** the `commit` widening; readers (states 2–4) · no

#### `besiege`
*be- + OF* sege *'seat' ← VL \**sedicum*: to sit down before. **Fit:** FITS [CONFIDENCE: medium — a siege
may be `march` repeated; if a standing Record at a rung finds no reader before a repeated ENCOUNTER does,
widen `march` instead].

- **row:** `contested_physical` · settlement · eligibility `remit:dispatch` via a seat · beneficiary actor
  · counterparty —
- **requires:** `existence` of `subject` kind Rung (`march`'s cell)
- **writes · emits:** `Record.exists`, kind `siege` {at, by} · `siege.laid`; refusal `siege.refused`
- **contests:** `a field`, only if opposed at ENCOUNTER (reusing `march`'s step; `Unopposed` = the siege
  stands)
- **producer · composes:** the `war` state and a referent rung · `march`, `proclaim`, `levy`; state 7
- **CONFLICTS:** `march` — axis: write row (a standing Record, not bodies)
- **falsifier:** MATTER subsistence at the besieged rung falls with no actor; realm ex > 0
- **evidence:** besiege, storm or take terms — circumvallation, starvation, parley
  (`research/historical/precedents_warfare.md:74-102`) [R1-29]; naval blockade in the faction roster
  [P1-03]; CK3 armies besieging holdings [G2-12]; muster, fortify or blockade as the non-march military
  acts the cases ask for [C-39].
- **blocker · needs_jordan:** readers in `loop/matter.py`, `_eff_transfer`, `move` · no

#### `raze`
*F* raser *'shave, scrape' ← L* radere. **Fit:** FITS.

- **row:** `contested_physical` · settlement · eligibility `remit:dispatch` via a seat
- **requires:** the Site or Rung exists and the actor's side holds the field (a siege, or a `march` won
  this season)
- **writes · emits:** `Site.exists` / `Rung.exists` to absent (the rows admit RES,
  `write_matrix.yaml:302-336`; `destroy_record` is the precedent on `Record.exists`) · `site.razed`,
  `rung.razed`; refusal `raze.refused`
- **contests:** none
- **CONFLICTS:** `sabotage` — axis: write row (existence vs condition)
- **falsifier:** `w.rungs` shrinks — H-166 limit 3, "nothing shrinks it" (`hole_register.yaml:3651`)
- **evidence:** H-166, "no verb ends a Rung or a Site" [C-60]; RTK XIV — demolish a building [G2-84];
  the *chevauchée* and scorched earth [R1-58]; razing a heretic's house [H1-132]; the townspeople burning
  Kiersau Abbey and its library in *Pentiment* [G1-17].
  [CORRECTION: pass 2 cites RTK's Hidden Poison (G2-89) for `raze`; it lowers development and public order
  and is cited under `sabotage` instead.]
- **blocker · needs_jordan:** H-166's own design order (cost, holder, closer) · no (H-166 carries its own
  record)

### 7.3 Covert

#### `conceal`
*OF* conceler *← L* concelare (*celare* 'hide'). **Fit:** FITS.

- **row:** `social` · person · eligibility `own` · beneficiary actor · counterparty —
- **requires:** —
- **writes · emits:** `Record.exists`, kind `cover` {who: subject, as} · nothing public — the one row whose
  success emission is withheld from `co_located`, a design choice to be named and settled against
  `witness_channels`' precedence (`rosters.yaml:398-405`), not assumed; refusal `conceal.refused`
- **contests:** none
- **producer · composes:** a need question of a covert seat-holder — the Riskbreakers, "Extralegal
  infiltration. Loyal to Valoria the concept, not institutions" (`rosters.yaml:1544`), a Löwenritter
  body (`:1505`) · `surveil`, `seize`, `fight`, `tell`; state 16
- **CONFLICTS:** `forge` — axis: what is falsified (a Record about oneself, read by attribution, not a
  document's content)
- **falsifier:** `state/attribution` resolves an Event's anchor to the cover id; `seen` claims name `as`
- **evidence:** Riskbreaker Identity and Deniability Debt 0–7 (corpus-rebuild annex A, `:1185`;
  `references/names_index.yaml:360`) [P1-48]; acting under cover so that an act emits nothing below a
  vantage threshold [P2-77]; twelve cases ask for concealment by an ongoing, lapsing effort [C-14] and five
  for deniable acts — NPC-005: "a clean act leaves no trace to her, her order or the Crown" [C-15]; the
  concealed-identity meters [R1-55]; concealing a source, hiding a death, delaying succession news
  [R1-52]; *Tails Noir* — sneaking past or hiding from guards [G1-77]; *Pentiment*'s town priest hiding the
  saints' origin as Mars and Diana [G1-18].
- **blocker · needs_jordan:** an attribution reader (`state/attribution.py`) · no

#### `sabotage`
*F* saboter (19th–20th c.) [UNVERIFIED: the clog etymology]. **Fit:** FITS as the plain word; it is a
modern coinage, a voice question for in-world labels, not for the row.

- **row:** `uncontested_material` · person · eligibility `own` + presence · beneficiary actor ·
  counterparty `to` (the fabric's holder; declined when the actor holds it)
- **requires:** `restore`'s cell (`verb_table.yaml:781-788`)
- **writes · emits:** `Site.condition`, negative, through the same accumulator · `site.damaged`; refusal
  `sabotage.refused`
- **contests:** none
- **CONFLICTS:** `restore`, `work` — axis: counterparty and sign
- **falsifier:** `Site.condition` falls at RESOLVE with an act among its causes
- **evidence:** RTK XIV's Hidden Poison — a target area's development and public order fall [G2-89];
  *Shadows of Doubt* — sabotaging or hacking security systems [G1-96]; seizing or burning property
  [P2-44]; sabotaging a works [P1-62]. [DISAGREE, kept: P1-62's source,
  `proposals/2026-09-17-governance-and-holdings/00_THE_DESIGN.md:373-382`, argues sabotage needs no verb
  because emptying a works' store or taking its plot already stalls it. That covers stalling a works; it
  cannot lower a built Site's condition, which no act does today.]
- **blocker · needs_jordan:** none named · no

### 7.4 Persuasion and the person

#### `argue`
*OF* arguer *← L* arguere *'make clear, prove; accuse'*. **Fit:** FITS.

- **row:** `social` · person · eligibility `own` · beneficiary actor · counterparty `to` (the hearer, by
  the known-person fan)
- **requires:** `existence` of `subject` kind Proposition ∧ `relation` of `to`, `with`
- **writes · emits:** by degree — Overwhelming and Success write `Person.pursuits` (the row's own "moved
  by argument", `write_matrix.yaml:186-193`); Partial and Failure write nothing · `argument.won`,
  `argument.lost`; refusal `argument.refused`
- **contests:** `a proposition` (social_contest, sigma interim)
- **producer · composes:** a need question (the actor's own OUGHT), fanned over hearers · `utter`,
  `commit`, `tell`
- **CONFLICTS:** `tell` — axis: subject kind (a Proposition vs any topic), prize, write row [CONFIDENCE:
  medium — pass 2's own open question: whether a conviction write should instead ride every successful
  telling]
- **falsifier:** `Person.pursuits` moves in a run — today a RES row with no writer (§1); H-62 gains a
  producer
- **evidence:** H-62 — three interior rows with no verb, "Part E carries no argument verb" [C-53]; CK3 —
  convert, or demand conversion, eased by low fervour [G2-52]; persuading one powerful listener [R1-62];
  preaching as an office-less authority [R1-69]; spreading piety [P1-16]; *Disco Elysium* — persuade,
  charm or bluff [G1-23]; RTK's debate between officers [G2-103]; moving and debating a motion in
  Parliament [H1-04, H1-05].
- **blocker · needs_jordan:** the pursuits delta's magnitude (an `assumption` fixture); `commit`'s
  Proposition referent (§8.1) · no

#### `tend`
*Aphetic form of* attend *← L* attendere *'stretch toward, heed'*. **Fit:** FITS. *Heal* (OE *hǣlan*)
names the outcome — the body rising — and is refused on direction 3's logic, as `kill` is.

- **row:** `uncontested_material` · person · eligibility `own` + presence · beneficiary `subject` ·
  counterparty —
- **requires:** `existence` of `subject` kind Person ∧ `relation` of `subject`, `with`
- **writes · emits:** `Person.body` upward (the row admits RES, `write_matrix.yaml:161-167`) ·
  `body.tended`; refusal `tend.refused`
- **contests:** none
- **producer · composes:** Q2 on a `body.changed` claim about a known person · `fight`, `march`
- **CONFLICTS:** `restore` — axis: kind (Person vs Site)
- **falsifier:** no code path raises `Person.body` today — its writers only lower it (`fight`, `march`,
  MATTER subsistence); one does
- **evidence:** six cases ask to heal or recover, in a fast partial and a slow full form (ARC-53, SCN-03,
  SCN-04, SCN-07, EMG-X7, SCN-LOOP-C) [C-48]; *Esoteric Ebb*'s short rest restoring hit dice and spell
  slots while the clock advances [G1-46].
- **blocker · needs_jordan:** none named · no

#### `train`
*OF* trainer *'drag, draw'; 'instruct' from the 16th c.* **Fit:** FITS — it covers self and pupil, where
*practise* covers only self.

- **row:** `uncontested_material` · person · eligibility `own` · beneficiary `subject` (self or pupil)
- **requires:** `existence` of `subject` kind Person
- **writes · emits:** `Person.capability` — a **retired** row (`write_matrix.yaml:386`), returned with its
  producer under the file's own discipline, "a row exists because a producer produces it" (`:383-384`) ·
  `capability.raised`; refusal `train.refused`
- **contests:** none
- **producer:** a need question
- **CONFLICTS:** none — no verb writes capability; `build_at` seeds it
- **falsifier:** `sigma._pool_of` varies by person (R-09's `partial`, `seam/wrappers/sigma.py:94-97`)
- **evidence:** "NOTHING creates or develops a person" (`requirements.yaml:71`) and the seam table's "no
  creation, no progression, no chronicle" (`rosters.yaml:1011`), with eight cases asking [C-49];
  practising to raise a capability [P2-34]; CK3 — educating a child [G2-06]; teaching a group in secret
  [P2-72, C-47].
- **blocker · needs_jordan:** a capability-key operand (H-94's shape) · no

**Cross-check.** `detain`, `seize`, `execute` and `pardon` share eligibility but differ by write row;
`proclaim` and `covenant` by counterparty; `besiege`, `raze` and `sabotage` by write row. No two share
write row, eligibility and counterparty. None depends on a pass-1 cut.

### 7.5 Widened reaches — and why no new verb

| verb | what widens | why a new verb was refused |
|---|---|---|
| `surveil` | subject kind Person: covert watching of a person over time (`verb_table.yaml:1084` names the person case as having no home) | the consequence and eligibility are the place case's. The typed grammar has an `all` form (`data/requires.py:858`) and no `any`, so one row cannot take "Rung or Person": a sibling row until a disjunction is ruled |
| `determine` | `contests: "a proposition"` (social_contest through the interim `sigma_leverage`, repointing to the proceedings provider, `rosters.yaml:1149-1153`); degree-keyed writes, convict and acquit as bands (H-162's successor — the first writer of `Tenure.degree`, if the band lands there); `disposes:` kinds `custody` and `bar` | the matter, bench, docket and eligibility are `determine`'s; a `try` or `judge` beside it would be a second act disposing the same docket item — shape divergence. Trial by battle and ordeal are the same act under an arrangement whose prize is `the body` |
| `commit` | a `remit:` alternative, so a vote is cast through a seat; `determine`'s quorum reads live commits (H-161's alternative); a Proposition named in a held covenant becomes a referent (§8.1) | a vote is a commitment to a motion — same edge, same reader; a `vote` verb would be a second opener of `commit` |
| `confer` | a `hold` carrying `Tenure.term` (regency, a term-limited seat) | same edge and basis; regency is a term, and `Act.via` already carries delegation |
| `oblige` | a `remit:` alternative so the edge opens through a seat: seat A's holder obliged to seat B (vassalage), read by `purview_reaches` (H-101) | homage is the same `oblige` with a term renewed by `transfer`; `swear` or `homage` would be a second opener |
| `give` | object kind Rung: cede a rung hold; the gate's handover already covers every non-seat hold (`verb_table.yaml:398`) | the same two-hold write; `cede` would duplicate it |
| `march` | the winner's writes on `Won` (a hold on the rung, stores) | conquest is a won march's outcome, not a choice. **needs_jordan: yes** — step 5: the ruling is silent on the winner (`effects_combat.py:277-279`) |
| `tell` | an authored `said` (H-183): a telling whose content the teller does not hold — a lie, a slander | same hearer, prize and channel; only the content's source differs |
| `survey` | subject kind Rung (declined at H-169 limit 6) | the same sheet mint; `census` or `audit` would duplicate it |
| `revoke` | pass 2: close an `oblige` under a basis mirroring `may_renew` (expel a member) | [DISAGREE: a seat closing a member's `oblige` is the obligee-side closer D-5 refused (`verb_table.yaml:757`). **Withdrawn here.** Expulsion is then the seat withholding renewal so the member's term matures at MATTER — no verb; under H-159's `None` control arm an unpaid edge never matures, so expulsion waits on that fixture. Reinstating pass 2's widening means revisiting D-5, which is Jordan's] |

### 7.6 Deferred, and classed as outcomes

- **Thread operations — deferred.** Leap, weave, pull, past-pull, lock, dissolve and mend
  (`research/cross_scale_action_catalogue_v1.md:711-729`) [R1-67]; weave, cut, reinforce, mend [P2-43];
  eleven cases with graded, costed operations [C-51]. They belong to plan positions 27/29f
  (`verb_table.yaml:1103`) and are not developed here.
- **Outcomes, not verbs.** A **sentence** (the disposal's kind); **conquest, raid, usurpation** (a won
  `march`); **murder** (a `fight` whose band is `Felled`, with `conceal`); and, by direction 3, **`kill`**
  and **`wound`**.

---

## 8. The enabler, the faction map, the non-act mechanics, the build order

### 8.1 The shared enabler: a second operand channel

Today a Candidate binds `subject`, `to` and `site` all to the question's **one** referent
(`decision/options.py:741-746`). Two narrower channels exist: a held writ answers `to`, `kind` and
`amount` through `_from_content_claim` (`options.py:540`, called at `:726-729`, names declared in
`rosters.yaml:1571-1584`), and `tell`/`give` fan one Candidate per person the actor knows
(`operand_bags`, `options.py:827-860`).

**Shape (pass 2).** Generalize the writ channel so a held Record of any rostered kind can answer operands
from its content keys, declared per kind in `rosters.yaml` as `writ_sourced_operands` is; and extend
`operand_bags` to fan over the actor's held Records as it fans over known persons. No faction actor, no new
form, no ninth operand.

[CORRECTION: pass 2 names the answered operands `accused`, `against`, `from`. The operand vocabulary is
closed at eight — `actor, subject, from, to, site, kind, amount, floor` (`rosters.yaml:1569`) — and the
writ roster must be a subset of it, refused at import otherwise (`:1576-1577`). The enabler must therefore
**map** each kind's content keys onto the eight (a warrant's `terms` answers `subject`; a challenge's
`from` answers `subject` for its acceptor), not coin names. `from` is deliberately off the writ roster —
r2 keeps "where the actor stands" off a document (`:1577-1581`) — so a kind that answers `from` needs its
own argued exception.]

**What it unblocks:** `detain` (the warrant), `seize`, `pardon` (the disposal), `interrogate`, the
acceptance of a challenge, `confer` and `revoke` (an office named in a held Record), `commit` (a
Proposition named in a held covenant) and H-163's docket coincidence — and, from pass 1, `oblige`,
`determine` (limit 2), `levy` (limit 3), `migrate`, `exchange`, `establish` (`15c`).

### 8.2 Faction actions mapped to person acts

Every entry of `references/action_vocabulary.yaml:32-60` (25, `status: provisional`), and the faction- and
office-scale acts it lacks, resolve to a seat-holder's acts. *Through a seat* means `Act.via`. New verbs
are in bold.

| faction action | person acts at a rung |
|---|---|
| Muster | `march`'s own `sides_of` muster; a retinue by `oblige` + `transfer` |
| March | `march` |
| Fortify | `build` (a garrison Site), `restore` |
| Blockade | **`besiege`** |
| Conquest | a won `march`; the winner's hold and stores are a widening that needs Jordan (§7.5) |
| Govern | `issue`, `levy`, `determine`, `open_case` through seats |
| Trade | `exchange` (THIN), `transfer` |
| Subsidy | `transfer` |
| Treaty | **`covenant`** + `commit` |
| Diplomacy | `tell`, `petition`, **`covenant`** through seats |
| Spy | `surveil` (+ the Person widening), **`conceal`**, and recruiting composed from `tell` and the recruit's own `oblige` (D-5 refuses a lever on a second person) |
| Investigate | the six findings + `open_case` |
| Counter-Intelligence | `surveil`, `examine`, **`seize`**, **`detain`**, `tell` (to expose) |
| Censure | `determine` under an arrangement disposing a Record (`parliamentary_debate` already does, `arrangements.yaml:114`) |
| Embargo | **`proclaim`**, kind `embargo` |
| Outlawry | a person: `determine` disposing `bar` on the realm's seat; an organisation: **`proclaim`** `condemnation` of its Proposition |
| Excommunication | `determine` under a Church arrangement disposing `bar`; lifted by **`pardon`** |
| Active Inquisition | `petition` kind `accusation` → `open_case` → **`detain`** → **`interrogate`** → `determine` (contested) → a sentence (`oblige`, `custody`, `bar`, or **`execute`** after Jordan) → **`pardon`** |
| Church Seizure | **`seize`** + `levy` |
| Recognition Challenge | **`proclaim`** or `petition`, + `commit` (recognition withheld or given) |
| Succession Endorsement | `commit` through a seat to the claim |
| War Authorisation | `commit` through a seat (the vote) + **`proclaim`** kind `war` |
| Piety Spread | **`argue`** + `oblige` to Church seats |
| Community Organising | `found`, `oblige`, **`covenant`** (a league) |
| Martial Governance | **`proclaim`** kind `emergency` + **`detain`** / `levy` |

**Acts the roster lacks, mapped the same way.** Declarations (`proclaim`); truces, treaties, alliances
(`covenant` + `commit`); councils (`convene` + `utter` + `commit` + `determine`); tribunals (`open_case` +
`interrogate` + `determine` + `pardon`); elections and conclaves (`commit` + `confer`, basis `elected`);
impeachment (`petition` accusation + `open_case` + `determine` on a seat-holder + `revoke`); deposition of
a seat with no rung above (`revoke`, needing a basis only Jordan can add); coronation (`convene` +
`confer`); sieges (`besiege`); embargoes (`proclaim`); purges (`revoke`, `seize`, `detain`, `execute`);
regency (`confer` + term); vassalage (`oblige` through a seat); raids (a won `march`, Jordan).

**Riskbreakers.** Their espionage and law work is `surveil` (place and, widened, person), `conceal`
(cover identity), `seize` and `detain` under warrant, `tell` to expose, and the composed recruit; their
exposure is the Query of state 17, never a stored meter.

**What is missing is the enabler, not an actor.** No row above needed a faction to act.

### 8.3 Non-act mechanics, and where each meets the season loop

These are properties of a stage, a seam or a Query — not verbs. Each is listed with where it would live.

| mechanic (source) | where it meets the loop | status |
|---|---|---|
| Inner voices, skills, the Thought Cabinet (*Disco Elysium*, *Esoteric Ebb*) | `Person.capability` and `pursuits` as score terms (`decision/choose.py:326-329`, per pass 2) | none yet for interjection |
| The case or evidence board (*Shadows of Doubt*, *Lacuna*) | the actor's own ledger + `reconstruct` | none yet for links |
| Interrogation pressure; Truth / Doubt / Lie (*L.A. Noire*) | `interrogate`'s obstacle; `teller_weight` (`options.py:1043`, per pass 2) | with `interrogate` |
| Exposure meters, deniability debt (corpus-rebuild; cases) | a Query over `seen` claims (state 17) | none yet as a number |
| Quorum (Commons 40, Venetian Senate 70) | `determine`'s `quorum` conjunct; `arrangements.yaml`'s `quorum` key | partly built |
| Election by lot (Venice) | a seeded draw with no actor | none yet as an arrangement key |
| Veto, reserved powers, royal assent | arrangement keys (`disposal`, `records_dissent`) | none yet for a single-member veto |
| Term limits, rotation, one per family (the Council of Ten) | `Tenure.term` on holds + a conferral basis | none yet for family limits |
| Opinion, hooks, dread, tyranny (CK3) | `Person.stance` rows; `regard` | partly |
| Secrets as stored facts (CK3) | ledger claims + `cover` Records | with `conceal` |
| Fervour, public order, world-health bands (CK3, RTK, cases) | `Site.condition` bands; Layer 1 forbids a social aggregate stored on a Rung (pass 2, `04_CODE_ARCHITECTURE.md:237`) | none yet at rung scale |
| Interposition and latitude (proceedings) | `interposition_kinds` (`rosters.yaml:1794`) | rostered |
| Hue and cry, frankpledge (English law) | collective liability | none yet |
| Clocks, counters, endings (cases) | MATTER's licensed clocks only; endings absent (H-176) | absent |
| Births, ageing, individuation | CENSUS; H-51 absent (`loop/census.py:30-41` generates nobody) | absent |
| Rumour spread, message loss | WITNESS channels + `Record.ttl` (no reader) | partly |
| Evidence decay (*Shadows of Doubt*) | `Claim.confidence` decaying at MATTER | built |
| A scene's time budget (*Pentiment*'s canonical hours) | `decision/budget.py` | built |
| Secrecy decay of schemes | none yet | absent |
| Thread co-movement (P-01) | the threadwork lane | deferred |

### 8.4 Build order

Pass 1's ten steps (§4.1) bring the 44 up; this order brings the states and new verbs in, each step
landing its reader with its carrier:

1. The enabler (§8.1), mapped onto the closed eight.
2. `commit` widened (a `remit:` alternative, cast `via` a seat) + `covenant`.
3. `proclaim` kind `war`, with `sides_of` as its reader.
4. `determine` contested; `disposes:` kinds `bar` and `custody` (the tenure kinds and their
   `RELEASABLE_KINDS` exclusion land here).
5. `detain`, `pardon` (scoped to `custody` and `bar`), `interrogate` (scoped as §7.1 argues).
6. `seize`; `issue` kinds `warrant`, `summons`, `charter`; `petition` kinds `accusation`, `demand`,
   `challenge`.
7. `oblige` through a seat (vassalage), with `purview_reaches` as its reader (H-101).
8. `besiege`, `raze`, `sabotage`.
9. `argue`, `tend`, `train`.
10. `conceal`, with an attribution reader.
11. `execute`, only after Jordan.

---

## 9. Decisions for Jordan

Sorted by CLAUDE.md §0's five-step filter (superseded · irrelevant · answered by a design document ·
answered by precedent · answered by what the architecture needs). Only what survives all five is
escalated. No ledger row was written for any of them.

### 9.1 Escalated — `needs_jordan: yes`

| # | decision | where the filter stops, and why |
|---|---|---|
| 1 | **`execute`**: judicial killing as a direct write, or death only through the combat seam | step 5 — two defensible options lead to materially different games; the 2026-09-02 ruling addressed choosing an outcome in a fight, not a sentence; direction 3 leans to the seam but was hedged (§7.1) |
| 2 | **A won `march` writing the winner's side** (a hold on the rung, stores) | step 5 — the ruling is silent on the winner because it was never asked (`effects_combat.py:277-279`) |
| 3 | **A `revocation_bases` member** so a seat with no rung above can be deposed | step 5 — the roster is `open: false` with one value "because one rule was ruled" (`rosters.yaml:1757-1762`) |
| 4 | **Succession as a conferral basis**, giving `succeed` an heir operand and a reader | step 5 — `conferral_bases` is `open: false`; "a fourth way to fill a seat is a design change, not a table edit" (`rosters.yaml:1745`) |
| 5 | **Cut `speak`** | step 4 — the precedent is that table membership is ruled (`verb_table.yaml:442-455,950-952`) |
| 6 | **Cut `repudiate`** into `release` | step 4, as 5 |
| 7 | **Cut or re-purpose `work`** | step 4, as 5 |
| 8 | **Cut `comply`; rename or split `evade / defy`** | step 3 — the triple *comply / evade\|defy / construe* is Jordan's (`verb_table.yaml:737`) |
| 9 | **`exchange`'s counterparty operands** | step 5 — the register reserves coining them for H-94's ruling (`rosters.yaml:1562-1564`) |
| — | Already registered, no new row: H-156's (a)/(b) decides `destroy_record`'s held shape and `commit`'s cost; J-4 decides the works channel behind `build` and `found` | — |

### 9.2 Answered here, not escalated

| question | answer | step |
|---|---|---|
| Does direction 3 close the `kill`/`wound` split pending at `verb_table.yaml:446-448` and `:467`? | Read as yes [ASSUMPTION — Jordan to correct] | 1 (a later direction) |
| What may `pardon` close? | `custody` and `bar` only, never an `oblige` | 4 — `revoke`'s precedent; D-5 governs obligations (`verb_table.yaml:757`) |
| May `revoke` close a member's `oblige` (expulsion)? | No; expulsion is non-renewal and lapse | 1 — D-5 stands |
| May `interrogate` emit findings by degree? | No; its contest disposes the charge (`confession.made`/`confession.withheld`) | 3 — `rosters.yaml:1031` |
| One carrier or two for outlawry? | One per target: a person's is `bar`; an organisation's is `condemnation` of its Proposition | 5 — two ladders for one state is an S defect (§0.06) |
| Are `custody` and `bar` releasable by their holder? | No; excluded from `RELEASABLE_KINDS` | 4 — the `contain`/`reside` precedent (`data/rosters.py:448-453`) |
| May the enabler coin operand names? | No; it maps content keys onto the closed eight | 3 — r2's "I do not coin a ninth operand" (`rosters.yaml:1582`) |

**Untouched and still pending in the table:** the `challenge` → `accept` half of the split recorded at
`verb_table.yaml:446-448`. Two readings exist and neither is decided here: the pursuit-basis worksheet's two
new verbs with `accept` carrying `contests: "the body"`
(`proposals/2026-09-20-pursuit-basis-worksheet.yaml:155-156`), and pass 2's `petition` kind `challenge`
whose acceptor `fight`s the challenger the held Record names (§8.1).

### 9.3 Table/code and source/source disagreements

| # | disagreement | sites |
|---|---|---|
| a | The `kill`/`wound` split is still planned, and `:467` says "THE SLASHED NAME SURVIVES THIS COMMIT", stale since the 2026-09-29 rename | `verb_table.yaml:442-448`, `:467` |
| b | H-108 reads "`Act` CARRIES NO `via`", grade `absent`; `Act.via` is live and the gate reads it — the row appears stale (its `unblocks:` — regency, governors, councils — is state 19) | `hole_register.yaml:1571-1581`; `state/carriers.py:543-550`; `loop/resolve.py:114-118` |
| c | `tell` declares `beneficiary: subject`; since T4 the person told is `to`, and `beneficiary_of` resolves `subject` to the topic | `verb_table.yaml:875`, `:886-887`; `decision/choose.py:87-88` (per pass 1) |
| d | `forge` emits `record.created`; its matrix row emits `record.forged` | `verb_table.yaml:312`; `write_matrix.yaml:265` |
| e | `_ch_chronicle`'s docstring says the eight `binding_decision` verbs are all unresolvable; there are nine such rows and eight are admitted (all but `succeed`) | `epistemic.py:536-540`; `resolvable_verbs()` |
| f | P-03 reads "GM is the rendering engine" against "there is no GM" — cross-lane observation | `canon/02_canon_constraints.md:45` |
| g | Layer 1 row 15 refuses a `budget` office bonus; `budget.py` adds `budget_office_bonus` per live `hold` of **any** object, held Records included — and `utter` minting a hold would extend it to every Proposition. Cross-lane observation | `architecture/meta/04_CODE_ARCHITECTURE.md:202`; `decision/budget.py:57-58` |
| h | The pursuit-basis worksheet records `kill / wound` as "RULED 2026-09-20 NOT A VERB"; the decision-layer execution plan's draft cells add `kill`, `wound`, `fight`, `challenge`, `accept` for 42 verbs. Direction 3 sides with the worksheet | `proposals/2026-09-20-pursuit-basis-worksheet.yaml:149-151`; `proposals/2026-09-26-decision-layer-execution-plan/candidate_pursuit_cells.md:98-99` |
| i | NPC-038 gives the Cardinal of Justice `dispatch` where `offices.yaml` gives `convene`; the overlay names the difference | `cases/exercises/NPC-038.yaml:25-27` |
| j | The seam-table comment lists social contest and mass battle as "refuses by name"; the prize manifest routes `a standing` and `a proposition` to `sigma_leverage` and `a field` to mass_battle [CONFIDENCE: medium — read, not run; the comment may describe the full providers rather than the interim ones] | `rosters.yaml:1003-1011`, `:1111-1153` |
| k | `remit_acts` is `open: true`, though its source line calls #353's five acts closed | `rosters.yaml:294-302` |
| l | The `release` row's note places the typed grammar's `all` form at `data/requires.py:542`; it is at `:858` | line drift |

---

## 10. Provenance and falsifiers

### 10.1 What would show each proposal hooked

Every observable below is read by an instrument that exists: `harness.corpus_run`, `harness.aperture`, or
`w.log` from `populated.run`. None has been run against a proposal; all are unbuilt.

| item | observable |
|---|---|
| `detain` | `aperture 1 0` ex > 0; `move` refused for a person holding a live `custody` edge |
| `interrogate` | the corpus `DEGREES RESOLVED` histogram gains this prize's bands |
| `seize` | `record.seized` in `w.log`; realm ex > 0 |
| `pardon` | a `custody` edge closes with `disposal.lifted`; the next season's `move` is admitted |
| `execute` | a `person.died` with no `fight` among its causes |
| `proclaim` | enters the corpus executed set; `told_by` claims above 0 of 418 |
| `covenant` | the addressee's `commit` to the covenant's Proposition in `w.log` |
| `besiege` | subsistence falls at the besieged rung with no act |
| `raze` | `w.rungs` shrinks |
| `conceal` | an Event's anchor resolves to a `cover` id |
| `sabotage` | `Site.condition` falls at RESOLVE with an act among its causes |
| `argue` | `Person.pursuits` moves (a RES row with no writer today) |
| `tend` | `Person.body` rises |
| `train` | `sigma._pool_of` varies by person |
| states | war: `march` counts split by war present/absent · truce: a `march` between truced seats refused or flagged · alliance: allied persons in a `march`'s sides · vassalage: `purview_reaches` true across two seats · hostage: `sides_of` excludes the hostage's side · embargo: `transfer.refused` between the two rungs · siege: as `besiege` · excommunication: a `confer` refused on a barred person · heresy declared: an accusation grounded on a condemned `commit` · custody: as `detain` · outlawry: a seatless `detain` on an outlaw · sentence: `_renewals` treating two disposal kinds differently · concealed identity: as `conceal` · claim: a `war` Record whose terms name a claim · debt: a `seize` grounded on a lapsed debt · charter: `purview_reaches` false across a charter |

### 10.2 What was not verified

- **Nothing here was executed.** The corpus run is the orchestrator's (2026-10-03); the realm `att/ex`
  figures are copied from `requirements.yaml:674-676` (tree `23bea9da`). The author re-ran only the two
  import counts and the matrix script (§1).
- **Etymologies** are from general knowledge; no dictionary was opened. Uncertain paths carry [UNVERIFIED].
- **Game and history facts** are as extracted, with the extractors' own verification tags; not re-checked.
- **Code citations.** The sites in 10.3 were opened by the author. Any other `path:line` is as cited by
  the adjudication passes, which list the sites they opened, and was not re-opened here — among them
  `effects_information.py:85`, `state/gate.py:538`, `decision/choose.py:87-88` and `:326-329`,
  `options.py:1043`, `seam/wrappers/sigma.py:94-97`, `effects_combat.py:126-129`, `loop/sides.py:65-68`,
  `04_CODE_ARCHITECTURE.md:237`, and the test pins in §4.
- **ED-IN-0210** (cited by pass 2 for the covenant's two-sidedness) was not opened.
- **Whether `world_q.reach` admits an office id** — the premise of the seat-referent hooks for `confer`,
  `revoke` and `oblige` — was opened by nobody.

### 10.3 Sites the author opened

`engine/season/rosters.yaml` 101–116, 160–215, 286–311, 488–491, 574–577, 998–1037, 1100–1154, 1503–1506,
1534–1545, 1556–1584, 1737–1762, 1818–1829, 2156–2159, 2192–2195, 2230–2233 · `verb_table.yaml` 312, 315,
438–468, 737, 748, 754, 757, 873–887, 949–960, 1022 · `write_matrix.yaml` 259–266, 376–395, and all 37 rows
by script · `hole_register.yaml` H-101 (1961–1975), H-108 (1571–1582), H-156 (3518–3521), H-163
(3609–3620), H-173 (3740–3751) · `arrangements.yaml` 8–30, 78–137 · `requirements.yaml` 672–677 ·
`loop/effects_combat.py` 270–290 · `decision/options.py` 712–750, 822–860 (and `_from_content_claim` at 540
by search) · `loop/predicates.py` 325–345 · `loop/resolve.py` 114–118 · `data/rosters.py` 441–456 ·
`data/verbs.py` 736–790 (by search) · `data/requires.py` (searched for `all`/`any`) · `state/carriers.py`
543–550 · `decision/budget.py` 55–59 · `epistemic.py` 536–541 · `cases/exercises/NPC-038.yaml` 22–30 ·
`systems/social_contest/sim/contest/modes.py` 35–66 · `references/action_vocabulary.yaml` 1–60 ·
`canon/02_canon_constraints.md` 45 · `architecture/meta/04_CODE_ARCHITECTURE.md` 202 ·
`proposals/2026-09-20-pursuit-basis-worksheet.yaml` 148–157 ·
`proposals/2026-09-26-decision-layer-execution-plan/candidate_pursuit_cells.md` 98–99.

### 10.4 Corrections made to the adjudication reports

1. **D-5 and C-1 were engaged by neither pass.** `verb_table.yaml:757` records that a disposal `oblige` is
   self-releasable by ruling and that no obligee-side closer of an obligation "exists or will". Hence:
   `pardon` scoped to `custody` and `bar`, with a new falsifier (§7.1); the `revoke` widening to expel
   withdrawn (§7.5); and the case for two non-releasable tenure kinds made explicit (§6.1).
2. **The enabler may not coin operand names** (`accused`, `against`): the vocabulary is closed at eight and
   the writ roster must be a subset of it (`rosters.yaml:1569`, `:1576-1577`) (§8.1).
3. **`interrogate`'s degree emissions** of `finding.made`/`finding.none` run against `rosters.yaml:1031`
   [DISAGREE, both kept] (§7.1).
4. **Outlawry had two carriers** (`bar` and a `proclaim` kind); reduced to one per target, and `proclaim`'s
   `outlawry` kind dropped (§6, §7.2).
5. **`remit_acts` is `open: true`** (pass 1 called it closed). A rename of the verb `dispatch` would not
   force a rename of the remit act, which already gates `march` as well (§9.3 k).
6. **Binding-decision count**: nine rows, eight admitted — not seven (§9.3 e).
7. **Coverage counts** recounted one class per family: 29 / 9 / 14 + 1 / 3 / 5, against pass 2's 31 / 10 /
   14 + 1 / 3 / 6, whose WIDENED figure counts verbs (§5).
8. **`raze`'s evidence**: RTK's Hidden Poison (development and public order fall) moved to `sabotage`
   (§7.2).
9. **The typed grammar's `all` form** is at `data/requires.py:858`, not `:542` as the `release` row's note
   says (§7.5, §9.3 l).

---

## Appendix A. The 44, in full

Pass 1's per-verb adjudication with pass 2's REACH and NOT merged in, corrections applied. Citations are
pass 1's unless §10.3 lists them as opened here. *nj* = needs_jordan.

### `build`
- **Etymology · fit:** OE *byldan* ← *bold* 'dwelling'; raise a dwelling → mint a Site at condition 0 from a held works. FITS.
- **Earns:** YES — the only `Site.exists` producer (`write_matrix.yaml:330-336`; `effects_founding.py:115-130`).
- **Group · module:** G9 · world fact.
- **Reach:** a held `works` planning a `site_kinds` member, at the rung it names; one fabric per works. **Not:** found a Rung (`found`); raise condition (`restore`); end a Site (unowned → `raze`).
- **Hook:** a Q2 question whose referent is a `works` Record the actor holds (`options.py:681-696`); direct; `Site.exists`.
- **Why:** housing is the capacity throttle (`effects_migration.py:140-149`) — a settlement grows by its own hands.
- **Falsifier:** realm ex > 0 (65/0, `requirements.yaml:676`); leaves the always-refused pin at `test_season_shape.py:7624`.
- **Blocker · nj:** H-165 limit 2, carried as J-4 (`hole_register.yaml:3638`) · no new row; J-4 stands.

### `carry`
- **Etymology · fit:** AN *carier* ← LL *carricare* ← *carrus*; convey → put a filed petition on a docket. STRAINED — reads as transport; the row dockets. Plain alternatives `present`, `lodge` (proposal).
- **Earns:** THIN — the `own`-eligible docketing route H-52 calls "a different game" (`hole_register.yaml:596`); effect declined (`verb_table.yaml:121`).
- **Group · module:** G4 · social contest (proceedings lineage).
- **Reach:** a held petition → the docket; one filed thing to one room. **Not:** file (`petition`); docket by remit (`open_case`); forward, amend, drop (unowned).
- **Hook:** the petitioner holds his petition (`effects_information.py:134-137`) → question → subject binds. Direct, on `open_case`'s body (`:215-225`): write the petition's `Record.stages` as the named subject; the docket item rides the receipt. Rows `Record.stages` (proposal), `DocketItem.matter`.
- **Why:** a complaint reaching a bench without a seat's leave.
- **Falsifier:** `test_record_kind_fold.py:119` (`..._and_carry_is_not`) flips.
- **Blocker · nj:** H-63, answered by precedent (`open_case` dockets its subject) · no.

### `commit`
- **Etymology · fit:** L *committere*; entrust → open a `commit` edge to a Proposition. FITS.
- **Earns:** YES — `ambitions` reads it for need questions (`world_q.py:1309-1322,1441-1442`).
- **Group · module:** G7 · world fact.
- **Reach:** any existing Proposition (an OUGHT, a faction, a treaty, a motion); own. **Not:** utter (`utter`); duty to a seat (`oblige`); seat-to-seat fealty (unowned, H-101); a vote cast through a seat (WIDEN, §7.5).
- **Hook:** no question's referent is a Proposition (`verb_table.yaml:773`; 802 of 802 attempts refused, `hole_register.yaml:3521`). Proposal: `_eff_utter` mints the utterer's `hold` on it (`rosters.yaml:152` admits a Proposition; the maker's-hold precedent, `effects_information.py:134-137`), making it the utterer's own in reach so Q2 names it. Direct; `Tenure.since`.
- **Why:** closes utter → commit → ambition → a quiet-season act.
- **Falsifier:** leaves the always-refused pin (`test_season_shape.py:7624`).
- **Blocker · nj:** H-156 · no for the hook; H-156's (a)/(b) stays Jordan's. A hold buys budget (`budget.py:57-58`, H-92; §9.3 g).

### `comply`
- **Etymology · fit:** L *complere* → It. *complire* [UNVERIFIED: intermediate]; fulfil → act per a dispensation's terms. FITS.
- **Earns:** REDUNDANT-WITH the writ-sourced `transfer` (`options.py:717-729`; `rosters.yaml:1571-1584`); nothing else executable (`verb_table.yaml:146`).
- **Group · module:** G5 · none yet.
- **Reach:** a held writ; emission only. **Not:** perform the terms (writ-sourced `transfer`); withhold (`evade / defy`); misread (`construe`).
- **Hook:** the executor holds the writ after `give`; the subject binds the writ (`carry`'s scoping precedent). Route: the writ-sourced `transfer` earns `compliance.given` beside `transfer.made` (per-subject kinds, `effects_governance.py:90-91`). Rows `Rung.stores` ×2.
- **Why:** obedience with a trace, so defiance is legible by absence.
- **Falsifier:** `compliance.given` in `w.log` from `populated.run`, with no hand-built act.
- **Blocker · nj:** H-44 (`hole_register.yaml:500`), H-94 · **yes**, for cutting a row of Jordan's triple (`verb_table.yaml:737`) — step 3.

### `confer`
- **Etymology · fit:** L *conferre*; bestow → seat an office by opening a `hold`. FITS.
- **Earns:** YES (`effects_governance.py:63-69`).
- **Group · module:** G7 · world fact.
- **Reach:** an Office; `to` a person; `remit:confer` via a seat with purview; opens the hold, closes the incumbent's (`effects_governance.py:60-91`). **Not:** found it (`establish`); strip (`revoke`); elect (an act; the basis exists, `rosters.yaml:1755`); heir (`succeed`); a term-limited seat (WIDEN, §7.5).
- **Hook:** reads payload `office` (`predicates.py:172-174`), which is not among the closed eight (`rosters.yaml:1569`). Proposal: the office rides `subject` (convene's C-11, `verb_table.yaml:172`; `oblige`, `predicates.py:394`); the conferee rides `to` via the known-person fan (`options.py:827-860`). Rows `Tenure.until/since`.
- **Why:** patronage.
- **Falsifier:** realm ex > 0 (70/0, `requirements.yaml:674`).
- **Blocker · nj:** no question's referent is a seat (`verb_table.yaml:676`) · no. [GAP: whether `world_q.reach` admits an office id — not opened.]

### `construe`
- **Etymology · fit:** L *construere* → ME *construen* 'interpret'; mint a distorted reading of terms. FITS (the ruled rename from `refract`, `verb_table.yaml:737`).
- **Earns:** THIN — grade `absent`, D18 (`verb_table.yaml:731-738`).
- **Group · module:** G5 · none yet.
- **Reach:** a held writ; a receiver-side reading. **Not:** lie (`tell`, H-183); forge (`forge`).
- **Hook:** WITNESS-side, not an act: H-36 rules distortion receiver-side, per receiver (`hole_register.yaml:400,404`), which the content deposit already does per holder (`witness.py:40,523-540`). Rows none.
- **Why:** misreadings that travel by document.
- **Falsifier:** two holders of one writ holding different `content:dispensation` values.
- **Blocker · nj:** H-36's magnitude half, H-44 · no.

### `convene`
- **Etymology · fit:** L *convenire* → OF *convenir*; assemble → schedule a sitting. FITS.
- **Earns:** THIN — sole `Date.due_at` writer, but the date fires vacant, `date.fired` never reaches WITNESS (`world_q.py:1362-1367`), and the slot forms with `matter: None` (`calendar.py:53`).
- **Group · module:** G4 · social contest (proceedings).
- **Reach:** any rung above `person`; `remit:convene`; adjourning is rescheduling (`effects_governance.py:240`). **Not:** docket (`open_case`/`carry`); decide (`determine`); summon a person (unowned).
- **Hook:** any rung above person rank (`predicates.py:489-494`); executes 2 of 12 in the realm. Route: pass CALENDAR's events into `witness()` (`driver.py:464`) and let `open_case` fill the fired slot's date. Rows `Date.due_at`, `DocketItem.matter`.
- **Why:** a sitting with a day people can act toward.
- **Falsifier:** a `date.fired` claim in any ledger (`test_season_shape.py:4307-4316` pins 0 of 0).
- **Blocker · nj:** H-163 limits 2 and 4 · no.

### `create_record`
- **Etymology · fit:** L *creare* + *recordari* → OF *record*; make a remembrance → mint a Record with stages. FITS.
- **Earns:** YES — the works' producer and the one mint (`effects_information.py:57-73,109-142`).
- **Group · module:** G6 · world fact.
- **Reach:** any rostered kind, declared content and stages, the maker's hold. **Not:** writs (`issue`); petitions (`petition`); sheets (`survey`); forgeries (`forge`); hand on (`give`).
- **Hook:** hooked (executes). A computed act mints contentless `text` (`:68-69`); the typed works cell is J-4.
- **Why:** documents can be found, carried, forged, burned (`rosters.yaml:637`).
- **Falsifier:** the corpus executed set; `test_works_founding.py:101`.
- **Blocker · nj:** H-80 · no.

### `destroy_record`
- **Etymology · fit:** L *destruere* → OF *destruire*; unbuild → delete a Record, ending its holds. FITS.
- **Earns:** YES — the only closer of `Record.exists` (`effects_information.py:313-318`).
- **Group · module:** G6 · world fact.
- **Reach:** a Record the actor holds or stands by; deletes it and every hold (`:441-451`). **Not:** take from another (unowned → `seize`); suppress a class of text (unowned); end a Rung or Site (unowned → `raze`, H-166).
- **Hook:** both eligibility alternatives decline (`resolve.py:119-150`; H-75); `give`'s shape was built and held (`verb_table.yaml:199`). Direct. Rows `Record.exists`.
- **Why:** the only way a document vanishes — the stake in holding one.
- **Falsifier:** `test_u7_own.py:153` flips.
- **Blocker · nj:** H-75; held on H-156's crowding · **yes**, no new row — H-156's registered (a)/(b) decides it (`hole_register.yaml:3527`).

### `determine`
- **Etymology · fit:** L *determinare* (*terminus*); fix the bounds → dispose of a docketed matter by opening the party's `oblige`. FITS.
- **Earns:** YES (`effects_information.py:284-297`).
- **Group · module:** G4 · social contest (proceedings).
- **Reach:** a docketed Person in the bench's ground; `remit:determine` via a seat; opens the disposal `oblige`, clears the docket. **Not:** grade a hearing (WIDEN, §7.5; H-162); a sentence other than service (H-173 → `custody`, `bar`); appeal (unowned; `open_case` nests); lift a disposal (the party's own `release` for an `oblige`; `pardon` for `custody`/`bar`).
- **Hook:** needs a question whose referent is a docketed person in the bench's ground (`hole_register.yaml:3612`, limit 2). Direct via a seat. Rows `Tenure.since`, `DocketItem.matter`.
- **Why:** a bench binding men with no player watching.
- **Falsifier:** realm ex (1/20, `requirements.yaml:674`); `test_u7_remit.py:278`.
- **Blocker · nj:** H-163 limit 2 (SC lane), H-162 · no.

### `dispatch`
- **Etymology · fit:** It. *dispacciare* / Sp. *despachar*, root disputed [UNVERIFIED]; send off → emit `order.given`, write nothing. STRAINED — ordinary use sends; the row orders (`verb_table.yaml:259`). Plain alternative `order` (proposal). [CORRECTION: pass 1 says `order` "collides with the closed `remit_acts`"; the roster is `open: true` (`rosters.yaml:294-302`), and a verb rename need not rename the remit act, which already gates `march`.]
- **Earns:** THIN — a documentless `issue`; no decision reads `order.given` (`epistemic.py:547`; tests).
- **Group · module:** G5 · none yet.
- **Reach:** an existing person; `remit:dispatch`; `order.given`. **Not:** a writ with terms (`issue`); muster (`march`); summons (unowned → `issue` kind `summons`).
- **Hook:** hooked (realm 16/86). The named person gets a claim about himself (Q2 clause 1). Terms as paper are `issue`.
- **Why:** a command the chronicle carries (`epistemic.py:547-549`).
- **Falsifier:** leaves the never-attempted pin (`test_season_shape.py:8372`).
- **Blocker · nj:** none · no.

### `establish`
- **Etymology · fit:** L *stabilire* → OF *establir*; make firm → found an Office or change its remit. FITS.
- **Earns:** YES (`effects_governance.py:138-154`).
- **Group · module:** G7 · world fact.
- **Reach:** a described Office at a rung; `remit:confer` (`predicates.py:226-312`). **Not:** seat (`confer`); found a place (`found`); an office under an office (unowned, H-101); dissolve (unowned).
- **Hook:** its operands are not among the closed eight (`predicates.py:212-223`; `rosters.yaml:1569`), so it refuses (`verb_table.yaml:268`). Direct via a seat. Rows `Office.exists`, `Office.remit_acts`, `Tenure.payload`.
- **Why:** institutions that grow.
- **Falsifier:** realm ex > 0 (19/0).
- **Blocker · nj:** plan position `15c` (`verb_table.yaml:268`) · no.

### `evade / defy`
- **Etymology · fit:** *evade* L *evadere*; *defy* VL \**disfidare* → OF *desfier*; slip away / renounce allegiance → withhold compliance (one Event). Each word FITS; the ROW is a MISFIT — covert and open refusal collapse into one `compliance.withheld` (`verb_table.yaml:283`). Plain word for the merged state: `withhold` (proposal).
- **Earns:** THIN (`verb_table.yaml:280-284`).
- **Group · module:** G5 · none yet.
- **Reach:** a held writ; withholding. **Not:** flee (`move`); contumacy (unowned; a summons' refusal); renounce fealty (unowned → `release` of a vassal's `oblige`).
- **Hook:** a held writ, as `comply`. `evade` = no transfer before the term matures (`Record.matured`, `write_matrix.yaml:266-272`); `defy` = a public refusal Event. Split only when a reader distinguishes them. Rows none.
- **Why:** disobedience others see or miss.
- **Falsifier:** `compliance.withheld` from computed play.
- **Blocker · nj:** H-44, H-94 · **yes** — renaming or splitting Jordan's triple (`verb_table.yaml:737`), step 3.

### `examine`
- **Etymology · fit:** L *examinare* (*examen*, the tongue of a balance); weigh → study a Site one stands at. FITS.
- **Earns:** THIN — its consequence is identical to the other five findings' (`verb_table.yaml:1033-1036`).
- **Group · module:** G11 · none yet.
- **Reach:** a Site stood at; physical trace (`:1024-1031`). **Not:** a person (`interview`); a document (`research`); a place over time (`surveil`).
- **Hook:** hooked (executes); producer is a co-located Site referent (`:789`). Route none.
- **Why:** a clue that is somewhere — but a finding carries no content.
- **Falsifier:** a `finding.made` claim with a non-trivial value.
- **Blocker · nj:** work item 4.5 (`:982-989`) · no.

### `exchange`
- **Etymology · fit:** OF *eschangier* ← VL \**excambiare*; swap → two-sided stores move. FITS.
- **Earns:** THIN — no cell, no effect (`verb_table.yaml:297-304`).
- **Group · module:** G8 · world fact.
- **Reach:** both sides' stores. **Not:** one-way (`transfer`); sale of an office (`exchange` + `confer`); ransom (unowned → `custody` + `transfer`).
- **Hook:** needs the counterparty's `kind` and `amount`, which have no operand names (`rosters.yaml:1562-1564`); `_shift` twice. Rows `Rung.stores` ×2.
- **Why:** trade, with scarcity paired on both sides.
- **Falsifier:** `exchange.made` in `w.log`.
- **Blocker · nj:** H-94 · **yes** — the register reserves coining these operands for H-94's ruling, step 5.

### `fight`
- **Etymology · fit:** OE *feohtan* → contest the body of a living person. FITS.
- **Earns:** YES — the one route to the duel engine (`seam/contest.py:154-169`).
- **Group · module:** G1 · personal combat.
- **Reach:** a living person; own; prize the body; the attempt only (`verb_table.yaml:456-553`). **Not:** kill or wound (outcomes — direction 3); war (`march`); restrain or arrest (→ `detain`); execute (→ `execute`, Jordan); challenge (pending, §9.2).
- **Hook:** hooked ("47/89" as pass 1 records it, without naming the denominator). Any person referent but self (`options.py:145-146`). Seam "the body"; rows by band (`verb_table.yaml:522-525`).
- **Why:** the irreversible personal stake. Priced by one alignment cell (sacred −0.3, `rosters.yaml:2189`); willingness is unbuilt (`:467`).
- **Falsifier:** `test_season_shape.py:12776`; the corpus `DEGREES RESOLVED` line (`corpus_run.py:993`) — on 2026-10-03: Failure 148, Felled 12, Partial 79, Success 21, Untouched 11, Wounded 20.
- **Blocker · nj:** H-98; the deontological gate · no.

### `forge`
- **Etymology · fit:** L *fabrica* → OF *forge*; 'counterfeit' from the 14th c. → mint a Record with `forgery_quality`. FITS.
- **Earns:** THIN (`verb_table.yaml:315`).
- **Group · module:** G6 · world fact.
- **Reach:** a Record carrying `forgery_quality` (`:306-316`). **Not:** a true record (`create_record`); plant it (`give`); a false telling (`tell`, WIDEN).
- **Hook:** a faction the forger holds a claim on (`survey`'s cell, `:859-861`); `survey`'s mint with perturbed content. Rows `Record.exists`, `Record.forgery_quality`.
- **Why:** a false sheet a rival acts on (`hole_register.yaml:3690`, limit 5).
- **Falsifier:** `test_information_cluster.py:297` stops asserting that no act forges.
- **Blocker · nj:** H-169 limits 2 and 5 (a consumer first) · no. Emits `record.created` where the matrix row emits `record.forged` (§9.3 d).

### `found`
- **Etymology · fit:** L *fundare* → OF *fonder*; lay a base → mint a Rung under its works' `at`. FITS.
- **Earns:** YES (`effects_founding.py:95-112`).
- **Group · module:** G9 · world fact.
- **Reach:** a held works planning a `rung_kinds` member; strict ascent. **Not:** a Site (`build`); an office (`establish`); a league (→ `covenant`); a charter (→ `issue` kind `charter`).
- **Hook:** as `build`. Rows `Rung.exists`, `Tenure.since` (`founding`).
- **Why:** new hearths (RR-2).
- **Falsifier:** realm ex > 0 (70/0).
- **Blocker · nj:** H-165 limit 2 (J-4); H-166 · no new row.

### `give`
- **Etymology · fit:** OE *giefan* → close the giver's `hold`, open the receiver's, in one write. FITS.
- **Earns:** YES — the only Record mover (`effects_information.py:389-428`; H-84).
- **Group · module:** G6 · world fact.
- **Reach:** a held Record `to` a known present person (`verb_table.yaml:386-398`); the gate's `handover` is general over every non-seat hold (`:398`). **Not:** stores (`transfer`); seize (→ `seize`); cede a rung hold (WIDEN, §7.5).
- **Hook:** hooked (executes in 1 corpus world; 63 refused on the `with` conjunct). Known-person fan (`options.py:827-860`). Rows `Tenure.until/since`.
- **Why:** a writ reaches the hand that can deny it.
- **Falsifier:** `test_give.py:94-399`.
- **Blocker · nj:** none · no.

### `interview`
- **Etymology · fit:** MF *entrevue*; a meeting → question an existing person. FITS.
- **Earns:** THIN — existence is the whole precondition, and self-interview is admitted (`verb_table.yaml:1045-1048`).
- **Group · module:** G11 · none yet.
- **Reach:** an existing person. **Not:** interrogation under custody (→ `interrogate`); covert watching (`surveil`, WIDEN).
- **Hook:** hooked (executes). Route none.
- **Why:** to be replaced by the Dialogue Lattice (`:1054`).
- **Falsifier:** the corpus executed set.
- **Blocker · nj:** work item 4.5; ED-FI-0004 · no.

### `issue`
- **Etymology · fit:** L *exire* → OF *issir/issue*; "issue a writ" → mint a dispensation to an executor in purview. FITS.
- **Earns:** YES (`effects_information.py:163-180`).
- **Group · module:** G6 · world fact.
- **Reach:** terms + `to` a person executor in purview; a dispensation (`verb_table.yaml:417-427`). **Not:** a documentless order (`dispatch`); an edict to a place (→ `proclaim`; the cell refuses a rung, `:427`); an instrument across to a foreign seat (→ `covenant`); rescind (unowned).
- **Hook:** hooked (realm 6/30, with `via`). Limit: the terms are the executor (`:176-179`). Rows `Record.exists`.
- **Why:** authority as paper.
- **Falsifier:** `test_u7_remit.py:460`.
- **Blocker · nj:** H-94; `15c` · no. New kinds proposed: `warrant`, `summons`, `charter` (§6).

### `levy`
- **Etymology · fit:** L *levare* → OF *levée*; a raising → move a rung's stores into the seat's treasury. FITS.
- **Earns:** YES (`effects_governance.py:336-347`).
- **Group · module:** G8 · world fact.
- **Reach:** a rung in purview with stores → the seat's rung. **Not:** tribute by term (`transfer`); a person's goods (unowned → `seize`); muster (`march`).
- **Hook:** the referent rung is empty, or not a rung (`hole_register.yaml:3612`, limit 3). Proposal: a question whose referent is a full larder in purview (a positive `stores.changed`). Rows `Rung.stores` ×2.
- **Why:** how a seat eats.
- **Falsifier:** realm ex > 0 (23/0); `test_u7_remit.py:201`.
- **Blocker · nj:** H-163 limit 3; the `remit:issue` substitution is H-52's neighbour (`verb_table.yaml:587`) · no for the hook.

### `march`
- **Etymology · fit:** OF *marchier*, probably Frankish [UNVERIFIED]; tread → send a mustered side against a settlement. FITS.
- **Earns:** YES (`sides.py:75-118`; `effects_combat.py:274-358`).
- **Group · module:** G2 · mass battle.
- **Reach:** a settlement; `remit:dispatch`; prize a field at ENCOUNTER; writes the losing side (`effects_combat.py:274-358`). **Not:** siege (→ `besiege`); conquest or raid writes (WIDEN, Jordan — the ruling is silent on the winner, `:277-279`); muster (its own `sides_of`).
- **Hook:** hooked in the realm (16/16); never in the corpus (H-175). Seam at ENCOUNTER. Rows `Person.body`, `Person.stance`.
- **Why:** war that leaves grudges.
- **Falsifier:** `test_march.py:323`; leaves the never-attempted pin (`test_season_shape.py:8372`).
- **Blocker · nj:** H-175, H-149 · no (the winner's writes: **yes**, §9.1).

### `migrate`
- **Etymology · fit:** L *migrare* → re-home `contain` and `reside`, throttled by capacity. FITS.
- **Earns:** YES (`effects_migration.py:124-149`).
- **Group · module:** G10 · world fact.
- **Reach:** a rung with room; `contain` + `reside`. **Not:** presence (`move`); exile another (unowned → `bar` + `migrate`); relocate a court (unowned).
- **Hook:** the destination is the migrant's own home (`hole_register.yaml:3677`). Proposal: a destination channel — a shortfall at home plus a positive `stores.changed` elsewhere in reach, or a founded hearth with room (`:3683`). Rows as `move`.
- **Why:** people who leave famine.
- **Falsifier:** leaves the always-refused pin (`test_season_shape.py:7624`).
- **Blocker · nj:** H-168 (H-94) · no.

### `move`
- **Etymology · fit:** L *movere* → re-home `contain` only. FITS.
- **Earns:** YES — presence (`effects_migration.py:103-108`).
- **Group · module:** G10 · world fact.
- **Reach:** a rung up the ladder (`verb_table.yaml:645-659`). **Not:** residence (`migrate`); flight from custody (unowned; refused by state 13).
- **Hook:** hooked ("650/73" as pass 1 records it). Rows `Person.travel_leg`, `Tenure.until/since`.
- **Why:** being in the room is the epistemic model.
- **Falsifier:** `test_migrate_capacity.py:153`.
- **Blocker · nj:** none · no.

### `oblige`
- **Etymology · fit:** L *obligare* → OF *obligier*; bind → open an `oblige` edge with a term. FITS.
- **Earns:** YES (`epistemic.py:445-454`; renewed by `transfer`).
- **Group · module:** G7 · world fact.
- **Reach:** a seat whose `binds` admits the joiner; own; with a term (`predicates.py:394-403`). **Not:** seat-to-seat fealty (WIDEN with `via`, §7.5); sentence (`determine`); hostage (→ `custody`).
- **Hook:** no question's referent is a seat, and the row is untyped (`verb_table.yaml:669,676`). Proposal: type clause 1 once a seat can be a referent — a `tenure.opened` is chronicle-broadcast (`epistemic.py:553-554`) and expands to the office id (`effects_governance.py:84-89`) [UNVERIFIED: whether `reach` admits it]. Rows `Tenure.since`, `Tenure.term`.
- **Why:** retinues.
- **Falsifier:** `test_obligees.py:282` flips; leaves the never-attempted pin.
- **Blocker · nj:** seat referents (H-94/H-54) · no.

### `open_case`
- **Etymology · fit:** L *casus* → OF *cas*; legal → mint a case file and docket the matter. FITS.
- **Earns:** YES (`effects_information.py:183-225`).
- **Group · module:** G4 · social contest (proceedings).
- **Reach:** any matter at a place in purview; `remit:determine`; a case file + the docket (`:215-225`). **Not:** own docketing (`carry`); a private accusation (a `petition` kind); appeal (the same verb, nested).
- **Hook:** hooked (realm 7/28). Rows `Record.exists`, `Record.stages`, `DocketItem.matter`.
- **Why:** grievances enter the institution.
- **Falsifier:** `test_u7_remit.py:246`.
- **Blocker · nj:** H-52 (`verb_table.yaml:700-701`) · already registered as H-52, no new row. New kind proposed: `case` (§6).

### `petition`
- **Etymology · fit:** L *petitio* → OF; a request → mint a petition Record to a person, from a rung. FITS.
- **Earns:** YES (`effects_information.py:300-319`).
- **Group · module:** G6 · world fact.
- **Reach:** terms; `to` a person; `from` a rung; own (`verb_table.yaml:710-717`). **Not:** docket (`carry`); a writ downward (`issue`); accusation, demand, challenge (kinds of itself, §6).
- **Hook:** hooked. Limit: addressed to its own subject (`verb_table.yaml:719`). Rows `Record.exists`.
- **Why:** the upward voice.
- **Falsifier:** `test_record_kind_fold.py:153`.
- **Blocker · nj:** H-94; its closers are unbuilt (`effects_information.py:313-318`) · no.

### `reconstruct`
- **Etymology · fit:** L *re-* + *construere* → make a finding from held claims. FITS.
- **Earns:** THIN — a self-feeding loop is visible (`test_season_shape.py:3974-3977`).
- **Group · module:** G11 · none yet.
- **Reach:** anything in one's own ledger; synthesis (`verb_table.yaml:1111-1113`). **Not:** new information (the other five); decipher (`research`).
- **Hook:** hooked ("404–426 acts" as pass 1 records). Route none.
- **Why:** synthesis that can be wrong (`verb_table.yaml:1115`) — unbuilt.
- **Falsifier:** the corpus executed set.
- **Blocker · nj:** the obstacle (`:1113`), work item 4.5 · no.

### `release`
- **Etymology · fit:** L *relaxare* → OF *relaissier*; let go → close one's own edge of any releasable kind. FITS.
- **Earns:** YES (`effects_governance.py:157-191`).
- **Group · module:** G7 · world fact.
- **Reach:** the object of one's own live edge, six kinds (`verb_table.yaml:748`), including a disposal `oblige` by ruling (`:757`). **Not:** another's edge (`revoke`); pardon (→ `pardon`, for `custody`/`bar`); waive what is owed you (refused by D-5, `:757`).
- **Hook:** 96% refused (`requirements.yaml:759-760`), untyped. Proposal: a person-side decline in `opening_set` when `p.tenures` holds no releasable edge to the referent (own tenures are person-side, `budget.py:57`) — no grammar change. Rows `Tenure.until`.
- **Why:** resignation, divorce, apostasy.
- **Falsifier:** `release` refusals fall; `test_g3_release_is_the_owners_discretion_and_the_owners_only`.
- **Blocker · nj:** none · no.

### `repudiate`
- **Etymology · fit:** L *repudiare* (*repudium* 'divorce'); cast off → close one's own `commit`. FITS.
- **Earns:** REDUNDANT-WITH `release` (`verb_table.yaml:748,773`). Dies with it: `commitment.ended` and the alignment cells at `rosters.yaml:2158,2194,2232`.
- **Group · module:** G7 · world fact.
- **Reach:** one's own `commit`. **Not:** renounce fealty (→ `release` of a vassal's `oblige`).
- **Hook:** cut; `_eff_release` earns one kind per closed edge kind (`effects_governance.py:90-91` precedent), so vow-breaking stays witnessable and `align_kind` (`data/verbs.py:1044-1061`) can price it.
- **Why:** nothing new.
- **Falsifier:** `test_u7_own.py:42`'s DECLINED tuple shrinks.
- **Blocker · nj:** none · **yes** — cutting a §E3 row; the precedent is that membership is ruled, step 4.

### `research`
- **Etymology · fit:** OF *recercher* (← L *circare*) → consult an existing Record. FITS.
- **Earns:** THIN (as `examine`).
- **Group · module:** G11 · none yet.
- **Reach:** an existing Record (`verb_table.yaml:1061-1063`). **Not:** a Site (`examine`); a person (`interview`); a letter in transit (unowned).
- **Hook:** hooked. Route none.
- **Why:** archives (`rosters.yaml:2229`).
- **Falsifier:** the corpus executed set.
- **Blocker · nj:** work item 4.5 · no.

### `restore`
- **Etymology · fit:** L *restaurare* → OF *restorer* → raise a Site's condition where present. FITS.
- **Earns:** YES (`effects_economy.py:133-164`; realm 18/82).
- **Group · module:** G9 · world fact.
- **Reach:** a Site stood at; raise toward the ceiling. **Not:** a body (→ `tend`); staking a works (`build`); damage (→ `sabotage`).
- **Hook:** hooked. Rows `Site.condition`.
- **Why:** towns that mend; walls before a march.
- **Falsifier:** `test_works_founding.py:237-282`.
- **Blocker · nj:** H-164, H-166 · no.

### `revoke`
- **Etymology · fit:** L *revocare*; recall → close another's `hold` through a seat with a basis. FITS.
- **Earns:** YES (`predicates.py:432-444`; `effects_governance.py:194-211`).
- **Group · module:** G7 · world fact.
- **Reach:** an office via a seat with a basis; closes the hold. **Not:** resign (`release`); excommunicate or outlaw (→ `determine` disposing `bar`); expel an obligee (refused by D-5; lapse instead, §7.5); dissolve (unowned); depose a seat with no rung above (closed roster — Jordan, §9.1).
- **Hook:** payload `office` (`predicates.py:433`). Proposal: the office rides `subject`, as `confer`. Rows `Tenure.until`.
- **Why:** a lord unmaking a subordinate.
- **Falsifier:** realm ex > 0 (15/0).
- **Blocker · nj:** seat referents; H-91 (`hole_register.yaml:1131`) · no for the hook.

### `speak`
- **Etymology · fit:** OE *sprecan/specan* → emit `speech.made` about a referent; no hearer, nothing said. STRAINED — speech has an audience; the row has none and carries no `said` (`options.py:193-202`).
- **Earns:** REDUNDANT-WITH `tell` — bystanders hear a `tell` by presence (`verb_table.yaml:887`).
- **Group · module:** G12 · none yet.
- **Reach:** a referent, nothing carried. **Not:** a motion (`utter`); a seat's proclamation (→ `proclaim`).
- **Hook:** hooked. Proposal: cut, or give it `tell`'s `holds` conjunct.
- **Why:** what dies — speech about what one knows nothing of.
- **Falsifier:** leaves the executed set; `test_seen_claim.py:55`.
- **Blocker · nj:** none · **yes** — cutting a §E3 row, step 4 [CONFIDENCE: medium]. Settle with a corpus run withholding `speak`: if claim counts and check R3 hold, cut.

### `succeed`
- **Etymology · fit:** L *succedere* → OF *succeder*; follow in place → the HOLDER designates an heir. STRAINED — the heir succeeds; the actor designates. Plain alternative `designate` (proposal); `succeed` is also the tenure kind (`rosters.yaml:115`).
- **Earns:** THIN — no reader (`carriers.py:939-942`), no heir operand (`verb_table.yaml:839`).
- **Group · module:** G7 · world fact.
- **Reach:** a held office or estate; heir unbound (`:829-839`). **Not:** seat (`confer`); regency (`confer` + term, WIDEN); inheritance at death (unowned).
- **Hook:** the heir via the known-person fan (`to` beside `subject`). Reader: `conferral_bases` is closed at appointed/elected/annex (`rosters.yaml:1737-1755`), so succession fills no seat. Rows `Tenure.since`.
- **Why:** dynasties (`verb_table.yaml:840`).
- **Falsifier:** `test_u7_own.py:42` shrinks; a `person.died` followed by the heir's `hold`.
- **Blocker · nj:** ED-IN-0256 ruling (2) · **yes** — step 5: adding a basis amends an `open: false` roster, "a design change" (`rosters.yaml:1745`).

### `surveil`
- **Etymology · fit:** back-formation from *surveillance* (F *surveiller* ← L *vigilare*) → observe a Rung one stands at. FITS.
- **Earns:** THIN; the person case and Exposure have no home (`verb_table.yaml:1084`).
- **Group · module:** G11 · none yet.
- **Reach:** a Rung stood at (`:1077-1083`). **Not:** a person over time (WIDEN, §7.5); intercepting letters (unowned); planting an agent (composed: `oblige` + `conceal`).
- **Hook:** hooked. Route none.
- **Why:** the covert act canon prices (`rosters.yaml:2205`).
- **Falsifier:** the corpus executed set.
- **Blocker · nj:** ED-FI-0009; work item 4.5 · no.

### `survey`
- **Etymology · fit:** AN *surveier* ← ML *supervidere* → commission a faction sheet. FITS (`verb_table.yaml:848-851`).
- **Earns:** YES (`effects_information.py:322-386`).
- **Group · module:** G6 · world fact.
- **Reach:** a faction, or a person under one, in one's own ledger (`:859-862`). **Not:** a rung (WIDEN; declined at H-169 limit 6); census (unowned); yield assessment (unowned).
- **Hook:** hooked (realm 10/165). Rows `Record.exists`.
- **Why:** a stake, once something reads the sheet.
- **Falsifier:** `test_information_cluster.py:146,204`.
- **Blocker · nj:** H-169 limit 5 · no.

### `tell`
- **Etymology · fit:** OE *tellan* 'recount' → tell a known present person what one holds, contesting their standing. FITS.
- **Earns:** YES (`verb_table.yaml:877-888`; `test_told_by_channel.py:796`).
- **Group · module:** G3 · social contest (interim `sigma_leverage`).
- **Reach:** a topic in one's own ledger; `to` a known present hearer; prize a standing; `said` (`:877-899`). **Not:** a public (presence covers bystanders, `:887`); lie (WIDEN, H-183); move convictions (→ `argue`, H-62).
- **Hook:** hooked. Rows none (WITNESS).
- **Why:** rumour, and the chain of tellers.
- **Falsifier:** `test_told_by_channel.py:1042`.
- **Blocker · nj:** `sigma`'s `REFUSED` raises an uncaught `Unspecified` (`resolve.py:585-590`) — an SC-lane observation · no. The declared beneficiary disagrees with the code (§9.3 c).

### `thread_read`
- **Etymology · fit:** OE *þrǣd* + *rǣdan* 'interpret' → a finding gated on Thread Sensitivity ≥ 30. FITS (canon term, `verb_table.yaml:959-960`).
- **Earns:** THIN — not admitted (`:1097`; H-85).
- **Group · module:** G11 · none yet.
- **Reach:** a TS-gated finding. **Not:** threadwork (deferred, plan 27/29f).
- **Hook:** needs a per-person TS value and a gate stem; `knowledge_kinds` is the taxonomy half (`rosters.yaml:1184-1196`). Rows none.
- **Why:** P-08's barrier made mechanical (`canon/02_canon_constraints.md:50`).
- **Falsifier:** enters `resolvable_verbs()`; `test_u7_own.py:42` shrinks.
- **Blocker · nj:** H-85; plan 27/29f (`verb_table.yaml:1103`) · no.

### `tie / knot`
- **Etymology · fit:** *tie* OE *tīgan*; *knot* OE *cnotta*; bind → open a bond edge of kind `tie` or `knot`. Each word FITS; the ROW is a MISFIT — one opener cannot name its kind, and openers derive from the `Tenure(...)` literal per effect (`rosters.yaml:116-131`).
- **Earns:** THIN — `tie` is unread; `knot` is read undirected (`epistemic.py:441-442`; `verb_table.yaml:1130`).
- **Group · module:** G7 · world fact.
- **Reach:** a bond edge, partner unbound (`:1120-1131`). **Not:** marriage with terms (the same + `transfer` + a term); an alliance of seats (→ `covenant`).
- **Hook:** the partner via the known-person fan; `tie`'s reader is `teller_weight`'s relation term (`hole_register.yaml:4071-4073`). Build as two rows. Rows `Tenure.since`.
- **Why:** telling knits people, and nothing records it (H-182).
- **Falsifier:** `aperture 1 0` `tie / knot` ex > 0 (`hole_register.yaml:4054-4055`).
- **Blocker · nj:** H-182; `29f` owns `knot` · no.

### `transfer`
- **Etymology · fit:** L *transferre* → stores from the actor's rung to the referent, renewing obligee terms via a seat. FITS.
- **Earns:** YES (`effects_economy.py:167-212`; `verb_table.yaml:1149`).
- **Group · module:** G8 · world fact.
- **Reach:** own rung → a rung; `kind`, `amount`; renews obligees via a seat (`:1137-1149`). **Not:** Records (`give`); seizure (→ `seize`); treaty tribute (needs the treaty state, §6).
- **Hook:** hooked. Rows `Rung.stores` ×2, `Tenure.term`.
- **Why:** relief, tribute, pay.
- **Falsifier:** `test_season_shape.py:9328`; `test_term_upkeep.py`.
- **Blocker · nj:** H-158 · no.

### `utter`
- **Etymology · fit:** ME *uttren* from *ūt* 'out', path via Middle Dutch [UNVERIFIED]; put forth → mint an immutable Proposition. FITS.
- **Earns:** YES (`effects_information.py:454-470`).
- **Group · module:** G12 · world fact.
- **Reach:** an immutable Proposition (`:463-470`). **Not:** speech (`tell`); binding (`commit`); a seat's edict (→ `proclaim`).
- **Hook:** hooked, but reaches nobody's questions (no place, not held). Proposal: mint the utterer's `hold` (see `commit`). Rows `Proposition.exists` (+ `Tenure.since`, proposal).
- **Why:** vows that bind the speaker (`rosters.yaml:2173`).
- **Falsifier:** a `commit` executing on a `prop:` id in `populated.run`.
- **Blocker · nj:** H-92, the cost of a hold · no.

### `work`
- **Etymology · fit:** OE *weorc* → alter `Site.condition` by a declared delta, else advance a works' fabric. MISFIT — labour produces, and yield is MATTER's (`Rung.yield`, `write_matrix.yaml:316-322`); the row does `restore`'s rise under a floor (`effects_economy.py:73-77`).
- **Earns:** REDUNDANT-WITH `restore` in computed play (183/0, `requirements.yaml:676`).
- **Group · module:** G9 · world fact.
- **Reach:** a floor-gated advance of a works (`effects_economy.py:73-96`). **Not:** wage labour (unowned); practice (→ `train`).
- **Hook:** fold into `restore`, or give labour a produce write (a Part D change). Rows `Site.condition`.
- **Why:** nothing `restore` lacks.
- **Falsifier:** leaves the always-refused pin (`test_season_shape.py:7624`).
- **Blocker · nj:** H-165 limit 2 · **yes** — cutting or re-purposing a §E3 row, step 4 [CONFIDENCE: medium]. Settle by grepping hand-built `work` acts with declared deltas.

---

## Appendix B. The 61 act families and their evidence

One class per family (§5). Evidence names the game and act, the repo document, or the historical
procedure; bracketed ids are extractor rows. *R* `research/`; *P1* governance proposals; *P2* narrative and
play proposals; *C* code-side demand; *G1* detective games; *G2* CK3 and RTK; *H1* history.

| # | family | class · verb | evidence |
|---|---|---|---|
| 1 | Question a person | COVERED · `interview` | *Pentiment*, questioning townspeople [G1-02]; *Disco Elysium* dialogue [G1-21]; *Lacuna*, interrogating suspects [G1-54]; *L.A. Noire*, notebook topics [G1-63]; *Shadows of Doubt*, sweet-talking witnesses [G1-92]; parliamentary questions to a minister [H1-31]; the Venetian Collegio receiving an embassy [H1-97] |
| 2 | Inspect a place, body or object | COVERED · `examine` | *Pentiment*, inspecting a body or inscription [G1-03]; *Disco Elysium* [G1-20]; *L.A. Noire*, the crime scene [G1-61]; *Shadows of Doubt*, prints [G1-84]; the coroner's view of the body [H1-161]; reading a person, witnessing a scene [R1-61] |
| 3 | Read, decipher records | COVERED · `research` | *Pentiment*, codes and invisible ink [G1-07]; *Shadows of Doubt*, call histories and emails [G1-85], receipts and phone books [G1-87]; Walsingham's cipher secretary [H1-179] |
| 4 | Watch a place; tail a person | WIDENED · `surveil` → Person | *Pentiment*, following a suspect unseen [G1-04]; *Shadows of Doubt*, CCTV [G1-86] and tailing a citizen [G1-91]; CK3's Spymaster finding secrets and disrupting schemes [G2-20, G2-21]; the State Inquisitors watching envoys [H1-187, UNVERIFIED]; the table's person case with no home (`verb_table.yaml:1084`) [C-16] |
| 5 | Evidence board | COVERED · `reconstruct` (+ SYSTEM) | *Lacuna*, assembling motives [G1-55]; *Shadows of Doubt*, the case board [G1-88] |
| 6 | Denounce, accuse | COVERED · `petition` kind `accusation` | *Pentiment*, accusing at the hearing with the proof gathered [G1-10]; *L.A. Noire*, accusing a lie [G1-65]; informing to the Inquisition [P2-66]; the *bocca di leone* [H1-105]; *denunciatio* [H1-116]; the jury of presentment [H1-157]; informers before the Ten [R1-41] |
| 7 | Open an inquiry, case, impeachment | COVERED · `open_case` kind `case` | the Archdeacon's inquiry in *Pentiment* [G1-11]; a bill's first reading [H1-13]; impeachment [H1-27]; a select committee [H1-32]; the Avogadori's prosecution [H1-102]; inquest *ex officio* [H1-118]; a heresy case filed with a 2–4-season term [P1-37]; heresy investigation [R1-38]; *quo warranto*, *residencia* [R1-39]; staged accusatory procedure in seven-plus cases [C-03] |
| 8 | Summons, writ, warrant, charter, safe-conduct | COVERED · `issue` kinds `summons`, `warrant`, `charter` | writs of summons [H1-01]; the royal writ [H1-53]; citation and contumacy [H1-119]; the safe-conduct [H1-153]; warrants of arrest or search [H1-168]; torture by warrant [H1-183]; charters and franchises [R1-18]; warrants overriding an assembly [R1-43] |
| 9 | Hear, try, judge | WIDENED · `determine` contested | *Pentiment*'s judgement and sentence [G1-12]; *L.A. Noire*, charging one of two suspects [G1-66]; *Shadows of Doubt*, resolving the case [G1-89]; second and third readings [H1-14]; the impeachment trial [H1-28]; the Forty [H1-103]; the public sentence [H1-125]; the consistory [H1-138]; condemning a doctrine [H1-150]; the inquiry verdict — tribunal recommended / inconclusive / exonerated [P1-40]; trying a heresy case [P2-67]; a graded hearing (H-162) and the four unseeded procedure games [C-02]; ordeal and judicial duel [H1-155, H1-156; P1-25] |
| 10 | Sentence | OUTCOME — `oblige`, `detain`, `transfer`/`levy`, `execute` | penance [H1-127]; imprisonment [H1-129]; relaxation to the secular arm [H1-130]; execution [H1-174]; *Pentiment*'s execution [G1-13]; execution and erasure [R1-36]; a sentence read as a job (H-173) [C-04] |
| 11 | Confess, swear, abjure | COVERED · `commit`, `tell`, `release` | swearing to answer truthfully [H1-120]; abjuration [H1-126]; compurgation [H1-154]; abjuring as releasing the commitment (`03_INQUIRY.md:280`) [P1-42]; `confession` as a rostered proof (`rosters.yaml:1828`) [C-10] |
| 12 | Excommunicate, interdict, absolve | WIDENED · `determine` disposing `bar`; `pardon` | CK3, excommunicate and lift [G2-54]; papal release from oaths [H1-77]; absolution [H1-128]; excommunication [H1-136]; interdict [H1-137]; the roster's Excommunication [P1-12]; a Cardinal's excommunication term [P2-68]; `church_standing` with no producer [C-06] |
| 13 | Edict, law, coinage, emergency | GAP · `proclaim` | edict and proclamation [H1-54]; coinage [H1-64]; the dispensing power [H1-66]; debasement and recoinage [R1-23]; edicts and emergency decrees [R1-43]; martial governance [P1-05]; the Policy Instrument [P1-60]; a state of emergency [C-32]; CK3, changing a realm law [G2-41] |
| 14 | Motion, debate, vote, veto | WIDENED · `commit` through a seat (motion `utter`, speech `tell`, veto SYSTEM) | moving a motion [H1-04]; the division [H1-10]; supply [H1-24]; the *liberum veto* [H1-35]; the Senate's ballot [H1-95]; casting a vote [P2-31]; argument moves as data [P2-37]; speech kinds [P1-17]; parliamentary manoeuvre [P1-59]; holdout in a consensus body [P1-67]; vote, veto, conditional assent [R1-02]; calling and casting a vote [C-34] |
| 15 | Elect, conclave, lot | COVERED · `commit` + `confer` basis `elected` (lot SYSTEM) | the Speaker's election [H1-03]; electing a king, tanistry [H1-72]; the doge by lot and ballot [H1-81]; procurators [H1-107]; conclave [P2-74]; acclamation and election [R1-08] |
| 16 | Appoint, invest, ennoble | COVERED · `confer`, `establish` | CK3, granting a title [G2-36] and court posts [G2-46]; investiture [H1-45]; charters [H1-52]; appointment [H1-59]; ennoblement [H1-80]; appointing and recalling officers [R1-30] |
| 17 | Depose, strip | COVERED · `revoke` (a seat with no rung above: Jordan) | CK3, revoking a title [G2-37]; expelling a member [H1-08]; deposing a king [H1-74]; trying or deposing a doge [H1-89]; conciliar deposition [H1-149]; deposing a sovereign [R1-07]; stripping and barring [R1-33]; seizing a higher seat [C-35] |
| 18 | Resign | COVERED · `release` | resigning an office (`proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:638-654`) [P1-20] |
| 19 | Heir, regency | WIDENED · `confer` + term (`succeed` THIN) | heir designation [H1-69]; regency [H1-70]; fixing the succession [R1-49]; CK3 inheritance under law [G2-64] |
| 20 | Homage, fealty | WIDENED · `oblige` through a seat | homage and fealty [H1-43]; *diffidatio* [H1-44]; CK3, transferring or releasing vassals [G2-38] and swearing fealty [G2-39]; oath and homage [R1-48] |
| 21 | Declare war | GAP · `proclaim` kind `war` | CK3, casus belli [G2-08] and holy war [G2-55]; war on a casus belli held as a record [P2-18]; declaring war with a compliance window [R1-04]; war authorisation [P1-15]; a graded war posture [C-38] |
| 22 | Truce, peace, treaty, alliance, tribute, cession | GAP · `covenant` (cession: widened `give`) | CK3, peace and purchased truce [G2-14]; RTK alliance [G2-96]; cession [R1-05]; treaty, tribute, surrender [R1-06]; leagues [R1-15]; Treaty and Diplomacy [P1-07]; settling a surplus [P1-65]; binding agreements in five cases [C-40] |
| 23 | Muster, hire, allies | COVERED · `march`'s muster, `oblige` + `transfer` | CK3, calling allies [G2-10] and raising levies and mercenaries [G2-11]; Muster and Fortify [P1-01]; muster and recruit [R1-26]; non-march military acts [C-39] |
| 24 | Siege, blockade, fortify | GAP · `besiege` (fortify COVERED) | naval blockade [P1-03]; CK3 sieges [G2-12]; besiege, storm, terms [R1-29] |
| 25 | Conquer, raid, usurp | OUTCOME of a won `march` (winner's writes: Jordan) | conquest [P1-04]; CK3 raids [G2-13], war goals [G2-15], usurpation [G2-34]; the *chevauchée* [R1-58] |
| 26 | Arrest, custody, bail, ransom, hostage | GAP · `detain`, `pardon` | arrest in *Disco Elysium* [G1-32, UNVERIFIED], *L.A. Noire* [G1-67] and *Shadows of Doubt* [G1-90]; CK3, abduct [G2-24], imprison [G2-47], ransom and release [G2-51]; inquisitorial imprisonment [H1-129]; the constable's arrest [H1-160]; bail [H1-163]; *habeas corpus* [H1-173]; confinement and hostage-kin [R1-35]; arrest and restraint [P2-45]; hostages and fostering [P2-53]; no custody kind [C-05]; rescue [C-24]; hostages [C-25] |
| 27 | Interrogate, torture | GAP · `interrogate` | pressing in *Disco Elysium* [G1-22]; Truth / Doubt / Lie [G1-64]; accusing a lie [G1-65]; CK3 torture [G2-48, UNVERIFIED]; interrogation with a notary [H1-121]; torture under limits [H1-122]; one scene per season [P1-38] |
| 28 | Execute | GAP · `execute` (Jordan) | *Pentiment* [G1-13]; CK3 [G2-49]; relaxation to the secular arm [H1-130]; execution of sentence [H1-174] |
| 29 | Outlaw, banish | WIDENED · `determine` disposing `bar` (organisation: `condemnation`; exile adds `migrate`) | the Althing's outlawry, the imperial ban, *utlagatio* [H1-39]; proscription and exile [R1-34]; declaring a person or organisation outlawed [P2-80]; CK3 banishment [G2-50, UNVERIFIED] |
| 30 | Seize, confiscate, suppress, search | GAP · `seize` (+ `examine`) | Church seizure [P1-14]; confiscation in thirds [H1-132]; the index [H1-134]; search and seizure [H1-175]; seizing church lands [R1-12]; seizing or burning property [P2-44]; suppressing a text or movement [P2-70]; taking a Record without consent [C-08] |
| 31 | Spy, infiltrate, informants | COVERED · composed: `tell` + the recruit's own `oblige` + `conceal` | Spy in the roster [P1-08]; a Riskbreaker operation [P1-47]; CK3 Spymaster [G2-20]; recruiting an intelligencer [H1-176]; planting an agent [H1-177]; a double agent [H1-181]; infiltration [P2-79]; recruiting and turning, thirteen cases [C-21]; an agent network [C-22] |
| 32 | Cover identity, deniability | GAP · `conceal` | Riskbreaker Identity [P1-48]; acting under cover [P2-77]; lapsing concealment, twelve cases [C-14]; deniable acts [C-15]; concealed-identity meters [R1-55] |
| 33 | Expose, publish | COVERED · `tell`, `give`, `survey` (exposure is state 17) | exposing a covert body [P1-49]; an operation exposed [P2-78]; counter-intelligence [C-18]; disclosing or selling a secret [C-28]; addressing a public [C-30] |
| 34 | Blackmail, hooks | COVERED · a held Record + `petition` kind `demand` + `tell` | CK3, fabricating [G2-17], blackmailing [G2-18] and spending a hook [G2-19]; pressing a fear [P1-28]; bribing an official [P1-29]; spending an obligation [P1-30]; evidence as standing leverage [C-29] |
| 35 | Bribe, gift, subsidy | COVERED · `give`, `transfer` | *Shadows of Doubt* bribes [G1-93]; CK3 gifts [G2-01]; RTK rewards [G2-71]; bribing an office-holder [P2-02]; endowing a public good [P2-58]; gifts for favour [R1-64]; funding a party [C-58] |
| 36 | Court, marry | COVERED · `tie / knot` (THIN) | CK3 personal and romantic schemes and marriage [G2-02, G2-03, G2-04]; courting [P2-14]; marriage with dowry [P2-52]; marrying into a house [R1-50]; forming a knot [R1-66]; marriage alliance [H1-76] |
| 37 | Slander, rumour | WIDENED · `tell` with authored `said` | slander [P2-15]; a competing account [P2-27]; RTK's estrangement [G2-90] and Dual Destruction [G2-93]; planting a rumour [R1-63] |
| 38 | Persuade, convert, preach | GAP · `argue` | *Disco Elysium* persuasion [G1-23]; CK3 conversion [G2-52, G2-53]; persuading one listener [R1-62]; preaching [R1-69]; spreading piety [P1-16]; changing convictions (H-62) [C-53] |
| 39 | Trade, wage, venality | COVERED · `exchange` (THIN) + `confer` | buying and selling in *Disco Elysium* [G1-29] and *Shadows of Doubt* [G1-100]; RTK trade [G2-78]; trading across a price gap [P2-55]; selling labour [P2-57]; selling office [R1-57]; venality and the *paulette* [H1-60]; a sold procuratorship [H1-109] |
| 40 | Borrow, distrain | GAP · `covenant` kind `debt` + `seize` | borrowing and default [R1-22]; settling or distraining [P2-56]; the Monte [H1-112] |
| 41 | Build, found, charter, patent | COVERED · `build`, `found`, `establish`, `issue` | CK3, creating a title [G2-33], holy orders [G2-56], buildings [G2-61]; chartered foundations [R1-16]; institutions [R1-17]; charters [R1-18]; durable works [R1-19]; patents [H1-114]; charters granted or denied [P2-60] |
| 42 | Survey, census, audit, visitation | COVERED · `survey` (rung subject WIDENED) | inquests and Domesday [H1-62]; visitation [H1-145]; the *curiosi* [H1-186]; *quo warranto* [R1-39]; resurvey [R1-45]; compiling a census [P2-24] |
| 43 | Envoy, legate | COVERED · `dispatch` + `give` (interposition SYSTEM) | ambassadors and *relazioni* [H1-98]; legates [H1-141]; an advocate or envoy interposed [P1-22] |
| 44 | Feast, coronation, progress | COVERED · `convene` + `utter`, `confer`, `move` | CK3 pilgrimage [G2-59] and activities [G2-60]; ceremonies [R1-47]; coronation [H1-41]; the itinerant court [H1-57]; crowning the doge [H1-87] |
| 45 | Heal, rest | GAP · `tend` | six cases [C-48]; *Esoteric Ebb*'s short rest [G1-46] |
| 46 | Train, educate | GAP · `train` | eight cases [C-49]; practising [P2-34]; CK3 education [G2-06] |
| 47 | Thread operations | GAP, deferred (plan 27/29f) | threadwork [R1-67]; thread operations [P2-43]; eleven cases [C-51] |
| 48 | Murder | OUTCOME of `fight` (+ `conceal`) | CK3 murder scheme [G2-23]; assassination [R1-56]; covert elimination [C-23]; *Disco Elysium*'s hanged man [G1-34] |
| 49 | Claim, coup, revolt | COVERED · composed (claim is state 18; revolt SYSTEM) | CK3, claiming the throne [G2-25], seizing the realm [G2-29], factions [G2-42]; pressing a claim [P1-54]; revolt at a band [P1-56]; seizing a higher seat [C-35]; a coup [P2-62] |
| 50 | Mediate, appeal, stay, adjourn | COVERED · `determine`, `open_case`, `convene` | *Disco Elysium*'s strike mediation [G1-30]; appeal [C-11]; mediation [C-41]; stays [P1-24]; appeal by nesting [P1-26]; the parliamentary stay [P1-39]; prorogation, dissolution, adjournment [H1-19, H1-20, H1-21] |
| 51 | Recognise, endorse | COVERED · `commit` (through a seat when cast by an office) | recognition given or refused [C-42]; recognition challenge and succession endorsement [P1-15] |
| 52 | Damage, raze | GAP · `sabotage`, `raze` | RTK's Hidden Poison [G2-89] and demolition [G2-84]; sabotaging a works [P1-62]; burning property [P2-44]; ending a Rung or Site (H-166) [C-60] |
| 53 | Admit, expel | WIDENED · `revoke` closing an `oblige` — withdrawn (§7.5); then COVERED by `oblige` + lapse | admission to a community [P2-41]; expulsion [P2-46]; the Serrata [H1-90] |
| 54 | Defect, poach | COVERED · composed | defecting with one's holdings [P1-55]; poaching [P2-16]; defection [P2-30]; RTK's Unattended Home [G2-92]; turning a person [R1-54] |
| 55 | Challenge, accept | COVERED · `petition` kind `challenge` + `fight` (pending, §9.2) | CK3 duel and trial by combat [G2-07]; challenge and accept [P2-32] |
| 56 | Privileged counsel | SYSTEM | four cases [C-13] |
| 57 | Regency through a seat | COVERED · `confer`; `Act.via` | delegation (H-108, stale) [C-37]; regency [H1-70] |
| 58 | Combat and battle moves | SYSTEM (inside the seams) | stratagems [P2-48]; fighting withdrawal [P2-49]; bout moves [P2-51]; grapple and feint [R1-59]; RTK attacks, fire, tactics, duels [G2-83 to G2-87] |
| 59 | Negotiation moves | SYSTEM (inside a bout) | propose, counter, probe [P2-38]; the four *upaya* [P1-66] |
| 60 | Events | SYSTEM | disaster, famine, epidemic, mutiny, riot, sack, succession crisis, defeat or default, a discovered plot [R1-72 to R1-80]; the bodies clock, interception, lost news, crises of conviction, starvation, coup, revolt, disaster, miracle [P2-13, P2-25, P2-26, P2-35, P2-36, P2-62 to P2-65]; heresy outbreak, inheritance, life events, locusts and plague [G2-63 to G2-65, G2-102]; quiet-season initiative, rumour, conviction drift, forgetting, a date firing, an inquisitor's arrival, revolt, a works stalling, hunger [P1-32 to P1-36, P1-45, P1-56, P1-63, P1-64]; individuation, institutional clocks, thresholds, world-health decay, hazards, awakenings, crises, fracture, endings, loyalty reassessment, expiry [C-50, C-57, C-66 to C-74] |
| 61 | Inner mechanics | SYSTEM (§8.3) | the non-act mechanics of both games tables |

---

## Appendix C. Evidence index by source

One line per source family: what was read, and what was not. The scratchpad tables themselves are not
retained; this index and the evidence written out above are what survives.

- **`research/`** — read in the cited ranges: the cross-scale and historical-concerns action catalogues,
  `governance/` (modes, conflicts, hierarchy), proactive governance, rise to power, the FA/SE precedents,
  rhetoric and oratory, and the precedents analysis and warfare files. Read in part: the systems
  integration master (lines 1–160 not read; part 4 read at 205–265 and 454–744; part 3 by heading); the
  game-precedent companion (v1 69–565, part 2 88–326, part 4 228–317, part 6 39–109, part 7 88–200;
  parts 3, 5 and 8 by heading); the personnel-muster master (40–765). The inquisition appears there only as
  heresy investigation, tribunal, interdict and informers; no Riskbreaker act beyond concealed identity
  and Exposure.
- **Governance proposals** — read in the cited passages: the proceedings subsystem's 04, 05, 10, 17 and 21;
  `social-contest-branches/03_INQUIRY.md` (1–350); `references/action_vocabulary.yaml` whole;
  `module_contracts.yaml`'s `domain_actions` block (566–607). Grepped only: proceedings 00–03, 06–08, 11–16,
  18–20 (with partial reads of 03, 14, 18); governance-and-holdings round one and r2 01–05; the
  settlements-factions-populations files beyond 00 and 03. Not read: governance-and-behaviour's
  `RULINGS.yaml`, `00_THE_SEAM.md`, `01_THE_BUILD_ORDER.md`; social-contest-branches 01, 05–08, 10–12. The
  2026-09-03 corpus-rebuild proposal (read at annex A 172–200, 369, 474–496, 560–580, 1185–1193, 1268;
  annex B 567; design v2 Parts III–IV) describes an uploaded corpus never verified against `main`.
- **Narrative and play proposals** — read: emergent-narrative primitives v2 00–01 and v1 00, 06, 05 §7, 04
  §2; the gather README and 02–04; character-and-play-surface 01, 03, 10 and recommendation rows of 02, 04,
  05, 08, 09; the 2026-08-30 play-space coverage tables (01, 08, 09) and keyword passages of 02, 03, 05–07;
  the pursuit-basis worksheet and execution-plan verb sections; root-level proposals at the named passages.
  Not read: the conviction-decision-layer files beyond headings; the gather 00, 01, 05; play surface 06–07.
  The coverage set and the term-ownership registry predate the 44-verb table, and the registry predates
  the Key substrate's retirement.
- **Season-loop demand** — read: the hole register's 176-row index and about 70 rows in full;
  `requirements.yaml`'s scales and R-01..R-09 (R-02, R-03 skimmed); `verb_table.yaml`'s writes, emits and
  decline notes; all 37 matrix rows; all 57 roster names and ten rosters' notes; `ENDINGS_CLASSIFIED.yaml`;
  `loop/census.py`; all 972 `need:` rows of the 143 cases. Not read: effect bodies and `witness.py` beyond
  event-kind greps; `harness/probes.py` beyond its no-signature decorators; the NPC registry beyond keyword
  lines; exercise overlays except by grep. Case counts carry about ±2; the `att/ex` figures are copied.
- **Detective games** — *Pentiment* (Obsidian, 2022), *Disco Elysium* (ZA/UM, 2019), *Esoteric Ebb*
  (Christoffer Bodegård / Sudden Snail, published by Raw Fury, 2026), *Lacuna* (DigiTales, 2021),
  *L.A. Noire* (Team Bondi / Rockstar, 2011), *Tails Noir* (EggNut / Raw Fury, 2021, launched as
  *Backbone*), *Shadows of Doubt* (ColePowered, 2024). Identities, developers and years were web-checked
  for all seven; many review sites returned HTTP 403, so several acts rest on search snippets and say so.
  Thinnest: *Lacuna* and *Tails Noir*; *Pentiment*'s Acts II–III trial detail was not fetched; some
  *Disco Elysium* and *L.A. Noire* rows are from memory and tagged.
- **Strategy games** — CK3 from the Paradox wiki's Interactions and Casus belli pages and secondary guides;
  the wiki's Schemes, Council, Laws, Hooks and Court-positions pages would not load, so several scheme
  effects are known by name only and council task names conflict between sources. RTK XIV from the
  official manual (pages 3100–6300); earlier entries (VIII, XI, XII, XIII) from secondary sources; RTK XI
  and XII espionage commands not retrieved.
- **Governance history** — parliaments (Westminster, with the Estates-General, Cortes, Reichstag, Althing
  and Sejm), royal governance (feudal, absolute, constitutional, elective), the Venetian councils, church
  justice and the inquisition (medieval and Spanish, mixed by act), secular law and intelligence (English
  template; the Byzantine *agentes in rebus*). Every "verified" source is a secondary summary read by a
  small model. Not covered: Ottoman, Chinese, Islamic, Mongol and Hanseatic governance. Several Venetian
  details (the Ten's voting thresholds, the *bocca di leone*'s witness rule, the cipher office) and
  tanistry stay [UNVERIFIED].

