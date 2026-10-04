# Verb coverage and gap fill — the 44 verbs of `engine/season/verb_table.yaml`, what they reach, what is missing, and the resolved suite

## Status: PROPOSED

> **SCOPE, STATED LOUDLY.** This document is **reference and a proposal** (CLAUDE.md §0.05): it resolves
> nothing at runtime, and if it were deleted the game would behave identically. **Revision 2
> (2026-10-04)** rewrites revision 1 (2026-10-03) so that it states one coherent suite, after an
> independent audit pass registered 27 conflicts in revision 1 and resolved them (§12). **Revision 3
> (2026-10-04)** applies Jordan's statement of what a march is (§2, direction 8): the stake is derived at
> the destination, `besiege` folds into `march`, war is the uttered Proposition the tree already reads,
> and `proclaim` and `truce` are deferred with their readers (§12, K-28…K-34). **Revision 4
> (2026-10-04)** interrogates the 44 and the suite against a survey Jordan supplied (§2, direction 9;
> §6): it states Valoria's verification policy, adds `steal` (§9.3, R-8), carries the charge as an
> uttered Proposition and the hostage as a composition, and registers six conflicts (K-35…K-40).
> **Merging the PR that carries it does NOT ratify the verification policy or any verdict in §6, any
> verb, state, widening, cut, gate basis or roster edit in §7–§11, nor any recommendation in §13**, notwithstanding the merge-ratifies default (ED-1094): each of those
> items carries its own decision and is **held back** until it is built in code, at its owner, with a
> test that executes it. Every grade proposed here is `assumption` or `absent`; none is `ruled`. Five
> residual decisions (§13: R-1, R-3, R-4, R-5, R-8) each carry a recommendation that the suite adopts and
> that Jordan may overrule; R-2 is resolved (§13.2) and leaves two one-line residuals (R-6, R-7). A design
> document is never the reason a behaviour is correct — the code is.

- **Date:** revision 1, 2026-10-03; revision 2, 2026-10-04; revision 3, 2026-10-04; revision 4,
  2026-10-04.
- **Authorship:** Claude — orchestrating two read-only adjudication passes, seven extraction passes, an
  independent read-only audit pass, an independent read-only march analysis, an independent read-only
  survey interrogation, and the write-up.
- **Lane:** IN (cross-cutting). No ID was allocated; no ledger row was written.

---

## 1. Purpose, method and limits

**Purpose.** Jordan asked for five things: an etymology and word-fit adjudication of each of the 44 verbs
in `engine/season/verb_table.yaml`; a comparative analysis isolating what each does in this game;
grouping into related sets with their relations to personal combat, social contest and the plain
instantiation of world facts; a hook proposal per verb; and the missing verbs and states, found by
comparing the table's reach against precedents and research and filled without conflicting with the
existing verbs, from faction- and office-scale acts down to granular person acts and events. After
revision 1 he asked that its conflicts be resolved and the result orchestrated into a coherent suite
(§2, direction 7); after revision 2 he stated what a march is (direction 8), and revision 3 carries the
consequences; after revision 3 he supplied a survey of other games' mechanics and asked that it be used
to interrogate the verbs (direction 9), and revision 4 carries that (§6). This document is that answer.
It changes no code.

**Pipeline.** A fact sheet was extracted from the live table (loading `engine/season/data/verbs.py`'s
`VERB_TABLE`, `loop/effects.py`'s `EFFECTS`, `loop/driver.py`'s `resolvable_verbs()` and the raw YAML).
A read-only adjudication pass, holding no write tool, adjudicated the 44 against the code (pass 1:
etymology, fit, whether each row earns its place, group, hook, falsifier, blocker). Seven extraction
passes then harvested **707** candidate acts: the repo's `research/` (80), its governance proposals (67),
its narrative and play proposals (80), the season loop's own measured demand — hole register,
requirements, case needs (77) — seven detective games (107), *Crusader Kings III* and *Romance of the
Three Kingdoms* (107), and governance history: parliaments, royal governance, the Venetian councils,
church justice and the inquisition, secular law and state intelligence (189). The adjudication pass's
second round (pass 2) classified those against the 44's reach and proposed states and new verbs. The
authoring pass wrote revision 1 and corrected the reports where a citation did not say what they claimed.

**The audit pass (revision 2).** An independent audit pass was given revision 1 and the tree, not the
producers' reasoning. It was **structurally read-only** — it held no write, edit or shell tool, so it
could not alter what it judged — and it had no part in producing revision 1. It checked revision 1
against the verb loader's invariants, the rosters, the write gate, the carriers, the ledgers and itself;
registered 27 conflicts (K-01…K-27), each with a resolution filtered through CLAUDE.md §0's five steps;
composed one roster, one state table and one build order; and left five decisions that survived the
filter, each with a recommendation (R-1…R-5). The author of revision 2 opened every load-bearing
citation the audit relied on (§14.3) and corrected the audit where a cite did not say what it claimed or
where its resolution collided with a ruling (§14.5).

**The march analysis (revision 3).** An independent read-only analysis pass was given direction 8,
revision 2 and the tree. It traced what `march` does today, derived each stake from state at the
destination, decided `besiege`, the winner's write (R-2), war and truce, and returned an edit list and
six conflicts (K-28…K-33). The orchestrator added one decision of its own (K-34, `proclaim` deferred).
The author of revision 3 opened every citation the analysis relied on (§14.3) and corrected it where a
cite did not say what it claimed or where its design would have broken a live check (§14.8).

**The survey interrogation (revision 4).** Jordan supplied *Mechanics of Inquiry, Speech and Rule*
(prepared 3 October 2026) in session. **It is not committed to this repository**, so this document cites
it by title, by its own labels (Findings 1–4, Recommendations 1–4, primitives P1–P58, families A–K) and
by the game it names, and writes out every point it relies on. The survey decomposes investigative,
narrative and grand-strategy games into 58 primitives, groups them into eleven verb families, and draws
four findings and four recommendations. An independent read-only pass, given the survey, revision 3 and
the tree, interrogated every verb against it, mapped the 58 primitives, and returned an edit list, six
conflicts (K-35…K-40) and one decision that survived the filter (R-8). The author of revision 4 opened
every load-bearing citation it relied on (§14.3) and corrected it where a cite did not say what it
claimed (§14.9).

**Limits, stated plainly.**

- The extraction tables were built partly from headings and greps, not full reads. Each extraction
  pass's own coverage notes name what it skipped; Appendix C carries one line per source. The material
  gaps: `research/` integration and game-companion volumes read in part (meta-analysis, not act
  catalogues); the proceedings subsystem's files 00–03, 06–08, 11–16 and 18–20 grepped only, and the
  governance-and-behaviour `RULINGS.yaml` not read; the 2026-09-03 corpus-rebuild proposal describes an
  *uploaded* corpus never verified against `main`; the 2026-08-30 coverage set and the term-ownership
  registry predate the 44-verb table (and the latter, the Key substrate's retirement); effect bodies and
  `witness.py` were grepped for event kinds only; case-need counts carry about ±2 from regex aid.
- Web facts about the games rest partly on **search snippets**: many review sites returned HTTP 403, and
  the Paradox wiki's Schemes, Council, Laws, Hooks and Court-positions pages would not load. *Lacuna* and
  *Tails Noir* are thinly sourced; *Pentiment*'s Acts II–III trial detail was not fetched. History rows
  rest on secondary summaries (mostly Wikipedia) read by an extraction pass. Items the sources tag
  [UNVERIFIED] stay tagged here.
- The per-verb attempt/execution figures for the realm (written `att/ex` below) are **copied from
  `engine/season/requirements.yaml:674-676`**, which labels them as tree `23bea9da`, older than HEAD.
  They were not re-run, by the authoring passes or by the audit pass.
- **The audit pass reads; it does not execute.** It ran no instrument, re-ran none of the counts revision
  1 copied, and its resolutions are judgments over code it opened. Where it was wrong, §14.5 says so.
  The march analysis is the same: its realm figures are H-149's and H-175's own recorded measurements,
  not a run, and §14.8 lists where it was wrong.
- The adjudication and audit passes are judgments over the extraction tables and the code sites they
  opened. They are not execution evidence, and nothing in this document is.
- **The survey's facts are the survey's.** Its own evidence paragraph says its titles were checked
  against store pages, wikis, developer posts and reviews in October 2026; that *Espiocracy* is
  unreleased and described from developer material only; that *Disco Elysium*, *Papers, Please*,
  *Sherlock Holmes: Consulting Detective*, *Ace Attorney* and *Twilight Struggle* are described from
  established knowledge and were not re-checked; and that *Crusader Kings III* and *Hearts of Iron IV*
  are patched continually. Nothing in it was re-checked here except against the games extraction pass
  where the two overlap (§6.4). Like every pass before it, the survey interrogation reads and does not
  execute.

**Instruments and measurements.**

| measure | value | instrument | when, by whom |
|---|---|---|---|
| verbs defined | **44** | `len(VERB_TABLE)`, import only | re-run by the author 2026-10-03 and 2026-10-04 |
| verbs admitted to the fold | **34** | `resolvable_verbs()` in `engine/season/loop/driver.py`; the ten not admitted are `carry`, `comply`, `construe`, `evade / defy`, `exchange`, `forge`, `repudiate`, `succeed`, `thread_read`, `tie / knot` | re-run by the author 2026-10-03 and 2026-10-04 |
| verbs that executed | **17 of 44** — `create_record`, `examine`, `fight`, `give`, `interview`, `issue`, `move`, `petition`, `reconstruct`, `release`, `research`, `restore`, `speak`, `surveil`, `tell`, `transfer`, `utter` | `python -m engine.season.harness.corpus_run` (143 cases, seed 0, 2 min 58 s) | 2026-10-03, run by the orchestrator; not re-run |
| attempted and always refused | **7** — `build`, `commit`, `found`, `levy`, `migrate`, `survey`, `work` | same run; agrees with the pin at `engine/season/tests/test_season_shape.py:7624-7625` | same |
| foldable but never attempted | **10** — `confer`, `convene`, `destroy_record`, `determine`, `dispatch`, `establish`, `march`, `oblige`, `open_case`, `revoke` | same run | same |
| `write_matrix.yaml` rows written by no verb | **15 of 37** | read-only script: the union of every row's `writes:` as `kind.field` strings gives 22, every one a matrix row; the 37 `rows:` entries not in that set are counted | re-run by the author 2026-10-03 and 2026-10-04 |

Of the 15, ten are written by a non-act step or are immutable: `Act[].returned` (DEL), `Claim.confidence`,
`Record.matured`, `Record.ttl`, `Rung.yield` (MAT), `Date.fired` (CAL), `Person.claim_ledger` (WIT),
`Person.weight` (CEN), `Rung.envelope` (MAT, CEN) and `Proposition.*` (immutable). **Five are act-class
(RES) rows with no writer at all:** `Person.axis_count`, `Person.coherence`, `Person.pursuits`,
`Rung.dates` and `Tenure.degree`. The suite supplies first producers for two: `argue` writes
`Person.pursuits` (§9.4), and the contested `determine` writes `Tenure.degree` by band (§9.6) — the table's
own note names the contested determination as that row's missing writer (`verb_table.yaml`, `determine`'s
`writes_note`; the matrix row declares `unproduced: H-162`). A sixth row, `Person.capability`, is
**retired** (`write_matrix.yaml:386`) and returns with `train` (§9.4).

---

## 2. Direction given in session

Stated by Jordan **in conversation and NOT ledgered** — no ED id was allocated, so none of these is a
ruling of record. Directions 1–6 were given on 2026-10-03, before revision 1; direction 7 after it was
pushed; direction 8 on 2026-10-04, after revision 2; direction 9 on 2026-10-04, after revision 3. They
are carried verbatim because the rest of this document is built on them.

1. **Method.** *"we do etymology and comparative analysis and sets and everything else so that we can
   logically identify where we have coverage and the flexibility of what a verb should be able to do,
   and then based on our precedents and research and stuff we find where our gaps lie and what verbs
   fill the gaps without conflicting with others"*. §3 is the etymology, comparison and sets; §5 is the
   coverage; §7 and §9 are the gap fill, each new verb carrying a CONFLICTS axis against its nearest
   neighbours.
2. **Expectation.** *"I am expecting there to be gaps and missing coverage"* / *"so fill them"* / *"I
   think you just need to develop more verbs"*. The suite adds twelve verbs and widens six (§7).
3. **`kill` and `wound`.** *"kill and wound are verbs that handle outputs, which I think means they
   shouldn't exist as they just relay state changes? characters can not actively choose to kill or
   wound. they can choose to fight tho"*. The statement is hedged (*"I think"*). It agrees with the
   earlier ruling recorded at `engine/season/verb_table.yaml:442-448` (Jordan, 2026-09-27: *"a character
   can only attempt to kill or wound, never choose the outcome directly"*), on which the row was renamed
   `fight`. [ASSUMPTION: this direction **closes** the still-pending split of `fight` into `kill` and
   `wound` that the table records at `verb_table.yaml:446-448` and again at `:467` — basis: the
   direction names both as outputs that "shouldn't exist"; Jordan to correct if he meant otherwise.] The
   same logic is why the suite has no `execute` (§9.8, R-1) and, with direction 8, no `besiege` (K-28).
   The **other half** of the pending note —
   `challenge` → `accept` — is a different question (whether a fight may be offered and taken); the
   suite answers it without a new verb (K-23).
4. **States.** *"we're also going to need states that can flag war and peace and alliances and treaties
   and stuff"*. §8 carries them. War needs no new carrier: it is a `WAR`-mood Proposition plus live
   `commit`s, which the tree already reads (K-29); truce waits for a reader (K-32).
5. **Church and Riskbreakers.** *"remember we have to hook into inquisitions with church as well as stuff
   for riskbreakers for espionage and law and stuff"* and *"as well as heresy and trials and stuff"*.
   The law-and-custody verbs (§9.1), the polity instruments (§9.2), the covert verbs (§9.3) and the
   Active Inquisition chain in §10.2 answer this.
6. **Altitude.** *"have to ensure we can cover from faction actions down to granular events that hook
   into season loop"*. §10.2 maps every faction action in `references/action_vocabulary.yaml` down to a
   person's act at a rung, and §10.3 maps the non-act mechanics to the season loop's own stages.
7. **Revision 2.** *"carefully resolve all conflicts, orchestrate into a coherent suite"*. Read as: adopt
   the audit's resolution for every conflict; where a decision survived the filter with a recommended
   option, carry that option in the suite and say plainly that Jordan may overrule it (§13); where a
   revision-1 proposal was refuted, delete it from the body and record it once (§12); leave no sentence
   that contradicts the suite.
8. **March (2026-10-04).** *"march simply indicates that an army has been sent to a location. the stakes
   for a march are variable--is it to capture another's settlement (capturing attempt) march to
   intercept someone's army that is targetting your settlement (defending), or move an army to one of
   your own settlements (relocate)?"* Read as: the verb is the simple choice — send the army to a place —
   and the stake is **derived from world state at the destination**, never declared by a separate verb.
   It is direction 3's principle applied to a field: as `kill` and `wound` are outcomes of a `fight`, a
   capture, an interception and a relocation are stakes of a `march`. Revision 3 carries it (§7.2, §9.6,
   §13.2; K-28…K-33).
9. **The survey (2026-10-04, stated in conversation, not ledgered).** Supplying *Mechanics of Inquiry,
   Speech and Rule*: *"Use this document to interrogate existing verbs and determine applicability to
   game."* Read as: the survey is evidence about how other games are designed — their primitives,
   their verbs, their failures — and the code decides what Valoria does. Each verdict in §6 therefore
   names the code site that decides it, and a survey pattern the code or a ruling refuses is recorded
   as not applying, never adopted against the code. Revision 4 carries it (§6; `steal`, §9.3; K-35…K-40;
   R-8).

**Resolved names.** "Shadows of darkness" is *Shadows of Doubt* (Jordan confirmed in session). "Romance of
three kingdoms" is read as Koei's *Romance of the Three Kingdoms* game series [ASSUMPTION: basis — the
list is of games]. *Tails Noir* is the renamed *Backbone* (EggNut, published by Raw Fury), per the games
extraction pass's web check [UNVERIFIED: search snippet, not a primary page]. *Shadows of Doubt*
(ColePowered Games) entered early access on 24 April 2023 — the survey and the games extraction pass
agree — and reached full release on 26 September 2024 per the extraction pass's web check; the survey
gives no full-release date, and Appendix C's "2024" is the full release. Both dates are carried; neither
was re-checked here.

**One ruling binds every faction-scale row below.** There is no faction actor in this model: every
faction act is a person's act, taken by an office-holder through a seat (`Act.via`) at a rung. Where a
source says "the Church excommunicates" or "Parliament votes", this document reads it as a named holder
acting through a named seat — or, for a vote, as each member's own act (K-07). The tree already says so
where code reads it: `engine/season/rosters.yaml:1026-1029` — Layer 1 PART D rows 1, 8 and 14 forbid a
faction that acts; a Faction is a type with no verbs, and its holdings are a Query over members' `hold`
Tenures.

---

## 3. The 44

### 3.1 Origin and fit

*Origin chain* abbreviations: OE Old English, ME Middle English, OF Old French, AN Anglo-Norman, MF Middle
French, L Latin, LL Late Latin, VL Vulgar Latin (\* = reconstructed), ML Medieval Latin, ON Old Norse.
*Earns*: YES = removing it loses a write or reader no other row supplies; THIN = present but the
consequence is unbuilt or duplicated; REDUNDANT-WITH = another row already does it. Groups are §3.2.
Renames are deferred until a row gains its operand, so a hash move is paid once (K-24).

| verb | origin chain | root sense | what the row does | word fit | earns | grp |
|---|---|---|---|---|---|---|
| `build` | OE *byldan* ← *bold* 'dwelling' | raise a dwelling | mint a Site at condition 0 from a held works | FITS | YES — sole `Site.exists` producer | G9 |
| `carry` | AN *carier* ← LL *carricare* ← *carrus* 'wagon' | convey | put a held petition on a docket | STRAINED — reads as transport; plain: `lodge`, `present`, deferred (K-24) | THIN — effect declined | G4 |
| `commit` | L *committere* (*com-* + *mittere* 'send, put') | entrust | open a `commit` edge to a Proposition | FITS | YES — `ambitions` reads it | G7 |
| `comply` | It. *complire* ← L *complere* 'fill up' [UNVERIFIED: the Spanish/Catalan intermediate] | fulfil | answer a held dispensation; emission only | FITS | THIN — retained by ruling (ED-IN-0210, K-01); the performance is the writ-sourced `transfer` | G5 |
| `confer` | L *conferre* 'bring together, bestow' | bestow | open a `hold` on a seat, close the incumbent's | FITS | YES | G7 |
| `construe` | L *construere* 'build up' → ME *construen* | interpret a text | a distorted reading of an instrument's terms | FITS (ruled rename, `verb_table.yaml:737`) | THIN — grade `absent` | G5 |
| `convene` | L *convenire* via OF *convenir* | come together | schedule a sitting: `Date.due_at` | FITS | THIN — the date fires vacant | G4 |
| `create_record` | L *creare* + *recordari* 'call to mind' via OF *record* | make a remembrance | mint a Record with declared stages and the maker's hold | FITS | YES — the one mint | G6 |
| `destroy_record` | L *destruere* via OF *destruire* | unbuild | delete a Record and every hold on it | FITS | YES — sole closer of `Record.exists` | G6 |
| `determine` | L *determinare* ← *terminus* 'boundary' | fix the bounds | dispose of a docketed matter by opening the party's `oblige` | FITS | YES | G4 |
| `dispatch` | It. *dispacciare* / Sp. *despachar*, root disputed [UNVERIFIED] | send off | emit `order.given`; write nothing | STRAINED — ordinary use sends, the row orders; kept by ruling, rename withdrawn (K-24) | THIN — no decision reads `order.given` | G5 |
| `establish` | L *stabilire* via OF *establir* | make firm | found an Office or change its remit | FITS | YES | G7 |
| `evade / defy` | *evade* L *evadere* 'go out'; *defy* OF *desfier* ← VL \**disfidare* 'renounce faith' | slip away / renounce allegiance | withhold compliance with a held writ | each word FITS; the ROW merges covert and open refusal into one `compliance.withheld`; split when built (K-24) | THIN | G5 |
| `examine` | L *examinare* ← *examen* 'tongue of a balance' | weigh | study a Site one stands at | FITS | THIN | G11 |
| `exchange` | OF *eschangier* ← VL \**excambiare* | swap | two-sided stores move | FITS | THIN — no cell, no effect | G8 |
| `fight` | OE *feohtan* | strive, do battle | contest the body of a living person; the attempt only | FITS | YES — the one door to the duel engine | G1 |
| `forge` | L *fabrica* 'workshop' via OF *forge*; 'counterfeit' from the 14th c. | work metal; make falsely | mint a Record carrying `forgery_quality` | FITS | THIN — effect declined | G6 |
| `found` | L *fundare* ← *fundus* 'bottom' via OF *fonder* | lay a base | mint a Rung under its works' `at` | FITS | YES — sole `Rung.exists` producer | G9 |
| `give` | OE *giefan* (the *g-* from ON *gefa*) | hand over | close the giver's `hold` on a Record, open the receiver's | FITS | YES — the only consensual Record mover | G6 |
| `interview` | MF *entrevue* ← *s'entrevoir* 'see each other' | a meeting | question an existing person | FITS | THIN | G11 |
| `issue` | OF *issir* ← L *exire* 'go out' | send out | mint a dispensation to an executor in purview | FITS | YES | G6 |
| `levy` | OF *levée* ← L *levare* 'raise' | a raising | move a rung's stores into the seat's rung | FITS | YES | G8 |
| `march` | F *marcher*, prob. Frankish [UNVERIFIED] | tread | send a mustered side against a settlement; writes the losing side and moves nobody (K-28) | FITS | YES | G2 |
| `migrate` | L *migrare* | change abode | re-home `contain` and `reside`, throttled by room | FITS | YES | G10 |
| `move` | L *movere* via AN | set in motion | re-home `contain` only | FITS | YES — presence | G10 |
| `oblige` | L *obligare* 'bind to' via OF *obligier* | bind | open an `oblige` edge with a term to a seat | FITS | YES | G7 |
| `open_case` | *case* ← L *casus* 'a falling' via OF *cas* | what befalls | mint a case file, docket the matter | FITS | YES | G4 |
| `petition` | L *petitio* ← *petere* 'seek; aim at' | a request | mint a petition Record from a rung to a person | FITS | YES | G6 |
| `reconstruct` | *re-* + L *construere* | build again | a finding from claims already held | FITS | THIN | G11 |
| `release` | OF *relaissier* ← L *relaxare* 'loosen' | let go | close one's own live edge of a releasable kind | FITS | YES | G7 |
| `repudiate` | L *repudiare* ← *repudium* 'divorce' | cast off | close one's own `commit` | FITS | REDUNDANT-WITH `release` — cut recommended (R-3) | G7 |
| `research` | MF *recercher* ← L *circare* 'go about' | search closely | consult an existing Record | FITS | THIN | G11 |
| `restore` | L *restaurare* via OF *restorer* | renew | raise a Site's condition toward its ceiling | FITS | YES | G9 |
| `revoke` | L *revocare* 'call back' | recall | close another's `hold` through a seat with a basis | FITS | YES | G7 |
| `speak` | OE *sprecan*/*specan* | say words | emit `speech.made` on a referent; no hearer, nothing said | STRAINED — speech has an audience; the row has none | THIN — retained (§3.5): it binds and carries nothing, which `tell` cannot do, and it executes | G12 |
| `succeed` | L *succedere* 'come after' via OF | follow in place | the holder designates an heir | STRAINED — the heir succeeds; the actor designates; plain: `designate`, deferred (K-24) | THIN — no reader, no heir operand (R-5) | G7 |
| `surveil` | 20th-c. back-formation from *surveillance* ← F *surveiller* ← L *vigilare* | keep watch | observe a Rung one stands at | FITS | THIN | G11 |
| `survey` | AN *surveier* ← ML *supervidere* 'oversee' | look over | commission a faction sheet | FITS | YES | G6 |
| `tell` | OE *tellan* 'count, recount' | recount | tell a known present person what one holds, contesting their standing | FITS | YES | G3 |
| `thread_read` | OE *þrǣd* + *rǣdan* 'advise, interpret' | — | a finding gated on Thread Sensitivity ≥ 30 | FITS (canon term) | THIN — not admitted | G11 |
| `tie / knot` | *tie* OE *tīgan*; *knot* OE *cnotta* | bind | open a bond edge of kind `tie` or `knot` | each FITS; the ROW merges two openers that cannot name their kind; split when built (K-24) | THIN | G7 |
| `transfer` | L *transferre* 'carry across' | carry across | stores from the actor's rung to the referent; renews obligee terms via a seat | FITS | YES | G8 |
| `utter` | ME *uttren* ← *ūt* 'out', path via Middle Dutch [UNVERIFIED] | put forth | mint an immutable Proposition | FITS | YES | G12 |
| `work` | OE *weorc*/*wyrcan* | labour | alter `Site.condition` by a declared delta, else advance a works | MISFIT — labour produces; the row is `restore`'s rise under a floor | THIN — retained; its declared delta restricted to ≥ 0 so it owns one sign (K-09) | G9 |

**Tallies.** Fit: 37 FITS, 4 STRAINED (`carry`, `dispatch`, `speak`, `succeed`), 1 MISFIT (`work`), 2 rows
whose words fit but whose row merges two acts (`evade / defy`, `tie / knot`). Earns: 25 YES, 18 THIN, 1
REDUNDANT-WITH (`repudiate`). **No row is now named for an outcome** (`fight` replaced `kill / wound`);
`succeed` is the one row named for what happens to someone else rather than what the actor chooses — the
ground of the `designate` rename, deferred with the row's heir operand (K-24, R-5).

### 3.2 Groups

Each group is defined by a column, named in the last cell; a row that meets two columns is placed by the
one that discriminates it, and the overlap is named. Of the 44, three reach a contest seam today
(`fight`, `march`, `tell`); in the suite seven do (`fight`, `march`, `tell`, `argue`, `determine`,
`detain`, `interrogate`). The six findings are investigation, ruled not a contest;
twenty-six of the 44 instantiate world facts directly. G13–G15 hold only new verbs. The audit pass
grouped the suite under eight coarser codes; this document keeps one grouping, this one.

| group | the 44 | suite additions (§7) | relation to combat, contest, proceedings, world fact | the column that makes it true |
|---|---|---|---|---|
| **G1 Personal combat** | `fight` | — | personal_combat owns the prize (`rosters.yaml:1107-1110`); world facts only as the band's consequence | `contests: "the body"`; degree-keyed `writes:` |
| **G2 Mass battle** | `march` | — (`march` widened: the army arrives, K-28) | mass_battle through the `mass_battle.resolve_field` role, fought at ENCOUNTER (`rosters.yaml:1111-1130`); sides are armies; in the suite a won or unopposed march re-homes the army, so `march` also meets G10's column | `contests: "a field"`; `step: ENCOUNTER` on the prize row |
| **G3 Social contest** | `tell` | `argue` | social_contest through the interim `sigma_leverage` (`rosters.yaml:1131-1153`); the opponent is `to` | a `sigma_leverage` prize with the opponent bound as `to` |
| **G4 Proceedings** | `carry`, `convene`, `determine`, `open_case` | — (`determine` widened: contested) | social contest by lineage: `a proposition` repoints to the proceedings provider when it lands (`rosters.yaml:1149-1153`); in the suite `determine` contests it | `DocketItem.matter` on three; `Date.due_at` on `convene` |
| **G5 Writ answers and orders** | `comply`, `construe`, `dispatch`, `evade / defy` | — | none yet; H-36 rules construal receiver-side; all four retained by ruling (ED-IN-0210, K-01) | `writes: []` on all four |
| **G6 Documents** | `create_record`, `destroy_record`, `forge`, `give`, `issue`, `petition`, `survey` | `conceal`, `steal` | world fact; `issue` and `petition` feed G4, G5 and G13; `steal` is `seize`'s write with no licence, so it also meets G13's column | `Record.exists`, or `give` or `steal` moving the two `hold` edges |
| **G7 Seats and bonds** | `commit`, `confer`, `establish`, `oblige`, `release`, `repudiate` (cut recommended), `revoke`, `succeed`, `tie / knot` | — | world fact | `Tenure.since/until/term/payload`, `Office.exists/remit_acts`; the tenure kind is the discriminant (`rosters.yaml:115`) |
| **G8 Matter** | `exchange`, `levy`, `transfer` | — | world fact | `Rung.stores` written by one `_shift` body |
| **G9 Ground and fabric** | `build`, `found`, `restore`, `work` | `raze`, `sabotage` | world fact | `Rung.exists`, `Site.exists`, `Site.condition`; `_rise` is the one formula and `sabotage` its mirror |
| **G10 Movement** | `migrate`, `move` | — | world fact | stratum `movement`; `Person.travel_leg` and the `contain`/`reside` pairs |
| **G11 Findings** | `examine`, `interview`, `reconstruct`, `research`, `surveil`, `thread_read` | — | investigation, "its own kind — not a contest" (`rosters.yaml:1008`); it must not be made a contest to become gradeable (`:1031`) | `writes: []`, `emits: finding.made` on all six |
| **G12 Free speech acts** | `speak`, `utter` | — | `utter` is world fact (`Proposition.exists`); `speak` emits only | `requires: —`; empty `emits_on_refusal` |
| **G13 Law and custody** | — | `detain`, `interrogate`, `pardon`, `seize` | proceedings' enforcement; `detain` and `interrogate` reach the `sigma_leverage` seam | a held warrant or a `custody`/`ban` edge is the precondition or the write; `detain` and `pardon` also meet G7's column, `seize` G6's |
| **G14 Polity instruments** | — | `covenant` (`proclaim` deferred, K-34) | world fact between seats | Record kinds `treaty`, `alliance` minted under `remit:issue`, addressed across purview (also G6's column) |
| **G15 The person** | — | `tend`, `train` | world fact on a body or a skill | `Person.body` raised; `Person.capability` |

### 3.3 Comparative clusters

| cluster | discriminating axis | verdict |
|---|---|---|
| `give` / `transfer` / `exchange` / `levy` (+ `seize`, `steal`) | what moves, to whom: a Record's `hold` to a known present person; stores from the actor's rung to the referent; stores from a rung in purview to the seat's rung under `remit:issue`; both sides' stores (no cell); a Record's `hold` taken without consent under a warrant; the same taken with no licence at all | `give`, `transfer`, `levy` EARN; `exchange` THIN — two `transfer`s survive its cut, losing only atomicity and the paired scarcity; its counterparty operands are registered under H-94 (`rosters.yaml:1562-1564`) |
| `speak` / `tell` / `utter` | `utter` writes `Proposition.exists`; `tell` binds a hearer, contests a standing, carries `said`; `speak` binds, carries and contests nothing, and bystanders already hear a `tell` by presence (`verb_table.yaml:887`) | `utter`, `tell` EARN; `speak` THIN — retained (§3.5). It executes 104–139 corpus acts across the re-pins recorded at `hole_register.yaml:3521` and is the only row for speech by someone who knows nobody present or holds no claim on the topic |
| `issue` / `petition` / `carry` / `open_case` | eligibility and direction: down a remit; up from a rung; `carry` and `open_case` both write `DocketItem.matter`, differing by eligibility (`own` vs `remit:determine`) and subject kind. A warrant, summons or charter is a `dispensation` distinguished by what its `terms` names; an accusation, demand or challenge is a `petition` the same way — no new kinds (K-11, K-23) | `issue`, `petition`, `open_case` EARN; `carry` THIN — H-52's `own` alternative, scoped to petitions |
| the six findings | in code, only the `requires_typed` object class (Site, Person, Record, Rung, own claim, TS gate); under the survey interrogation, also the content source — the log at a present Site; another person's ledger, which the fold may not read; a Record's `subject_matter`; the log at a Rung across the season; the actor's own ledger; a TS gate (§6.3) | all six THIN, each with its own producer shape rather than one producer for six (work item 4.5, `verb_table.yaml:982-989`): `examine` and `surveil` read the log at a place; `research` reuses the content deposit; `interview` is a prompt (K-36); `reconstruct` and `thread_read` wait (K-37, H-85). THIN is about consequence, not a cut: Jordan ruled the six built as six rows (`verb_table.yaml:950-952`), which is also why `surveil`'s Person case waits for a grammar disjunction rather than a seventh row (K-16) |
| `confer` / `establish` / `oblige` / `commit` / `succeed` / `tie / knot` | what is opened, and who reads it: `oblige` → `establishment_of`, `_ch_post_remit`, and in the suite `purview_reaches` (vassalage); `commit` → `ambitions` → need questions; `knot` → `_ch_witness_key`; `tie` and `succeed` → nobody | `confer`, `establish`, `oblige`, `commit` EARN; `succeed`, `tie / knot` THIN; `succeed`'s reader is R-5 |
| `release` / `revoke` / `repudiate` / `pardon` | whose edge: one's own of any releasable kind; another's `hold` on a seat through a seat with a basis; one's own `commit` — already inside `release`'s domain (`verb_table.yaml:748`); another's `custody` or `ban` through the seat that owns it | `release`, `revoke` EARN; `repudiate` REDUNDANT-WITH `release` — cut recommended (R-3), with `_eff_release` earning `commitment.ended` on a closed `commit` (precedent: per-subject kinds, `effects_governance.py:90-91`) so the three alignment cells (`rosters.yaml:2158, :2194, :2232`) survive; `pardon` new (§9.1) |
| `restore` / `work` / `sabotage` | preconditions (floor vs presence), and sign; one formula | `restore` EARNS; `work` THIN — the floor-gated, works-only advance, restricted to a declared delta ≥ 0 (K-09); `sabotage` owns the negative sign (§9.3) — the thinnest pair in the suite (K-27) |
| `move` / `migrate` (+ `march`'s arrival) | the `reside` edge and the capacity refusal; whose `contain` is re-homed — one's own, or (`march`) every mustered claimant's, through a seat | both EARN; `migrate` executes nowhere yet; `march` composes on their one body, `_relocate` (§9.6) |
| `comply` / `evade / defy` / `construe` | none in code; what compliance performs is a `transfer` whose addressee comes off the held writ (`decision/options.py:717-729`; `rosters.yaml:1571-1584`) — the writ's `kind` and `amount` decline every time today, because neither live schema carries them (`options.py:548-555`) | all three retained by ruling (ED-IN-0210's last row, `registers/editorial_ledger_in_archive.jsonl:178`; K-01) and THIN. Whether `dispatch` and `comply` are two sides of one thing stays open under ED-IN-0211 and is not re-derived here |
| `fight` / `march` / `detain` | prize, sides, step, write target | all EARN their place; `besiege` was folded into `march` (K-28) |
| `create_record` / `forge` / `survey` / `conceal` | content source: verbatim; falsified with an unread quality; resolved at writing; about the maker himself, read by attribution | `create_record`, `survey` EARN; `forge` THIN; `conceal` new (§9.3) |
| singletons | `convene` — sole `Date.due_at` writer, but `date.fired` never reaches WITNESS; `dispatch` — writes nothing, read by channels and tests only; `destroy_record` — sole closer of `Record.exists`; `found`/`build` — sole producers of `Rung.exists`/`Site.exists` | `convene`, `dispatch` THIN; `determine`, `destroy_record`, `found`, `build` EARN |

### 3.4 REACH and NOT — the coverage baseline

*REACH* is what the row can do as built or as its cell reads; *NOT* is the nearest act it does not do and
which verb owns it in the suite. "unowned" marks an act the suite leaves without a verb; "none-yet" marks
one whose verb is deferred with its reader. The REACH of the six widened verbs in the suite is §7.2.

| verb | REACH | NOT → owner |
|---|---|---|
| `build` | a held `works` planning a `site_kinds` member, at the rung it names | found a Rung (`found`); raise condition (`restore`); end a Site (`raze`) |
| `carry` | a held petition → the docket | file (`petition`); docket by remit (`open_case`); forward, amend, drop (unowned) |
| `commit` | any existing Proposition — an OUGHT, a faction, a treaty, a motion, a war; opens `commit`; formable once `utter` mints a hold or a held Record names the Proposition | utter (`utter`); duty to a seat (`oblige`); a vote through a seat (none: a vote is each holder's own `commit`, the count a Query, K-07) |
| `comply` | a held writ; emission only | perform the terms (the writ-sourced `transfer`); withhold (`evade / defy`); misread (`construe`) |
| `confer` | an Office, `to` a person, `remit:confer` via a seat with purview | found it (`establish`); strip (`revoke`); elect (the basis exists, `rosters.yaml:1755`; the votes are members' own `commit`s); heir (`succeed`, R-5) |
| `construe` | a held writ; a receiver-side reading | lie (deferred: the telling workplan's G7, §9.7); forge (`forge`) |
| `convene` | any rung above `person`; `remit:convene`; `Date.due_at`; adjourning is rescheduling (same verb) | docket (`open_case`/`carry`); decide (`determine`); summon a person (`issue`, a dispensation whose `terms` is the person) |
| `create_record` | any rostered kind, declared content and stages, the maker's hold | writs (`issue`); petitions (`petition`); sheets (`survey`); forgeries (`forge`); a cover (`conceal`); hand on (`give`) |
| `destroy_record` | a Record the actor holds or stands by | take from another (`seize` under a warrant; `steal` with none); suppress a class of text (unowned); end a Rung or Site (`raze`) |
| `determine` | a docketed Person in the bench's ground; opens the disposal `oblige`, clears the docket | (the suite's contested reach: §7.2) appeal (`open_case`, nested); lift a disposal (the party's own `release` for an `oblige`; `pardon` for `custody`/`ban`) |
| `dispatch` | an existing person; `remit:dispatch`; `order.given` | a writ with terms (`issue`); muster (`march`); summons (`issue`) |
| `establish` | a described Office at a rung; `remit:confer` | seat (`confer`); found a place (`found`); an office under an office (unowned, H-101); dissolve (unowned) |
| `evade / defy` | a held writ; withholding | flee (`move`); contumacy (unowned); renounce fealty (`release` of a vassal's `oblige`) |
| `examine` | a Site stood at; physical trace | a person (`interview`); a document (`research`); a place over time (`surveil`) |
| `exchange` | two sides' stores | one-way (`transfer`); office sale (`exchange` + `confer`); ransom (`transfer` + `pardon`) |
| `fight` | a living person; the attempt; prize the body | kill, wound (outcomes, direction 3); war (`march`); restrain or arrest (`detain`); a death sentence (not a verb: `custody` + the enforcement seat-holder's `fight`, §9.8); accept a challenge (the same `fight`, on a held `petition`, K-23) |
| `forge` | a Record with `forgery_quality` | a true record (`create_record`); plant it (`give`); a false telling (deferred, §9.7) |
| `found` | a held works planning a `rung_kinds` member; strict ascent | Site (`build`); office (`establish`); league (`covenant`, kind `alliance`); charter (`issue`; its exemption reader deferred, §9.7) |
| `give` | a held Record `to` a known present person; the gate's handover covers every non-seat hold | stores (`transfer`); take without consent (`seize` under a warrant; `steal` with none); (cede a rung hold: §7.2) |
| `interview` | an existing person | interrogation under custody (`interrogate`); covert watching of a person (deferred, §9.7); the reply (the questioned person's own `tell`, K-36) |
| `issue` | terms + `to` a person executor in purview | a documentless order (`dispatch`); a proclamation to a place (none-yet: `proclaim` deferred with its readers, K-34); an instrument to a foreign seat (`covenant`); rescind (unowned) |
| `levy` | a rung in purview with stores → the seat's rung | tribute by term (`transfer`); a person's held Records (`seize`); muster (`march`) |
| `march` | a settlement; `remit:dispatch`; prize a field at ENCOUNTER; writes the losing side; in the suite also the arriving army's presence, the stake read at the destination (§7.2) | title (`seize` under occupation, `give`, `release`, death — never `revoke`, K-30); a war declaration (`utter`, K-29); muster (its own `sides_of`) |
| `migrate` | a rung with room; `contain` + `reside` | presence (`move`); exile another (a `ban` + the exile's own `migrate`); relocate a court (unowned) |
| `move` | a rung up the ladder | residence (`migrate`); an army (`march`, through a seat); flight from custody (refused by `custody`'s reader, §8) |
| `oblige` | a seat whose `binds` admits; own; with a term — including a seat-holder obliging himself to another seat, which the suite reads as vassalage (§7.2) | sentence (`determine`); hostage (`custody`) |
| `open_case` | any matter at a place in purview; `remit:determine`; case file (kind `text`) + docket | own docketing (`carry`); private accusation (a `petition`); appeal (the same verb, nested); the charge (`utter`, mood `HOLDS`, subject the accused; K-35) |
| `petition` | terms, `to` a person, `from` a rung; own | docket (`carry`); writ downward (`issue`); accusation, demand, challenge (a `petition` by what its `terms` names); the charge itself (`utter`, mood `HOLDS`, subject the accused — the accusation's `terms` names it; K-35) |
| `reconstruct` | anything in one's own ledger | new information (the other five); decipher (`research`) |
| `release` | the object of one's own live edge, six kinds (`verb_table.yaml:748`) | another's edge (`revoke`, `pardon`); waive what is owed you (refused by D-5, `verb_table.yaml:757`) |
| `repudiate` | one's own `commit` | renounce fealty (`release`); everything else is `release`'s — cut recommended (R-3) |
| `research` | an existing Record | Site (`examine`); person (`interview`); a letter in transit (unowned) |
| `restore` | a Site stood at; raise to ceiling | a body (`tend`); stake a works (`build`); damage (`sabotage`) |
| `revoke` | an office via a seat with a basis | resign (`release`); excommunicate, outlaw (`determine`, `disposes: ban`); expel an obligee (refused by D-5; lapse instead, §7.2); dissolve (unowned); depose a seat with no rung above (none: R-4) |
| `speak` | a referent, nothing carried | a motion (`utter`); a seat's proclamation (none-yet: `proclaim` deferred, K-34) |
| `succeed` | a held office or estate; heir unbound | seat (`confer`); regency (`confer` + term); inheritance at death (R-5: an `inheritance` basis, later) |
| `surveil` | a Rung stood at | a person over time (deferred, §9.7; `verb_table.yaml:1084`); intercept letters (unowned); plant an agent (composed) |
| `survey` | a faction, or a person under one, in one's own ledger | (a rung: §7.2); census (unowned); yield assessment (unowned) |
| `tell` | a topic in one's own ledger `to` a known present hearer; `said` | a public (presence covers bystanders); lie (deferred, §9.7); move convictions (`argue`) |
| `thread_read` | a TS-gated finding | threadwork (deferred, plan positions 27/29f) |
| `tie / knot` | a bond edge, partner unbound | marriage with terms (same + `transfer` + term); an alliance of seats (`covenant`) |
| `transfer` | own rung → a rung; `kind`, `amount`; renews obligees via a seat | Records (`give`, `seize`, `steal`); treaty tribute (a `treaty` read by `_renewals`, §8) |
| `utter` | an immutable Proposition, including a declaration of war (mood `WAR`, read by `faction_q.at_war` once committed, K-29) and a charge (mood `HOLDS`, subject the accused, K-35) | speech (`tell`); binding (`commit`); a seat's proclamation (none-yet: `proclaim` deferred, K-34); a charge's filing (`petition`, whose `terms` names it) and testimony to it (a witness's own `commit`, K-35) |
| `work` | floor-gated advance of a works; a declared delta ≥ 0 | damage (`sabotage`); wage labour (unowned); practice (`train`) |

### 3.5 The one cut, and the cut proposals withdrawn

Every verdict below changes, or declines to change, a row of the ratified table. None is decided here.

| verb | suite | why | needs_jordan |
|---|---|---|---|
| `repudiate` | **cut, recommended** — fold into `release`, which earns `commitment.ended` on a closed `commit` | the same edge has two closers (`verb_table.yaml:748, :773`); the alignment cells re-key on the event kind | yes — R-3 (§13) |
| `comply`, `evade / defy` | retained, unchanged | ED-IN-0210's last row (2026-09-18, ruled) keeps the three response verbs and `dispatch`: *"i did not realize that meant deleting those verbs. i think that's wrong"* (`registers/editorial_ledger_in_archive.jsonl:178`). Revision 1's escalation is superseded | no — K-01, filter step 1 |
| `speak` | retained, THIN | it binds no hearer and carries nothing, which no other row does, and it executes (104–139 corpus acts, `hole_register.yaml:3521`). A row that does something different, thinly, is not a duplicate; revision 1's settling run (a corpus run withholding `speak`) is not needed to keep it | no — withdrawn (§12, after K-27) |
| `work` | retained; declared delta ≥ 0 | `_eff_work` stages a declared delta with no sign check (`loop/effects_economy.py:86-98`), so today a hand-built `work` is also sabotage; restricting it gives each verb one sign | no — K-09 |
| `exchange` | retained, THIN | its counterparty operands are reserved for H-94's ruling (`rosters.yaml:1562-1564`) | no new row — already registered (§13.8) |
| `carry` | retained; build on `open_case`'s body, writing the petition's `Record.stages` | H-63 is answered by precedent (`open_case` dockets its subject). The survey's agenda control (P43, from *The Republic of Rome*: a procedural office decides what is voted on and when — the primitive it calls least imitated in videogames) is evidence for building it: `carry` is the one route by which someone without a seat puts a matter before a room (§6.3) | no |
| `dispatch` → `order` | rename withdrawn | `order:` is an `arrangements.yaml` key (`:95`, `:112`) and the fold's order key — a cold reader lands on the wrong meaning (§4) | no — K-24 |
| `carry`, `succeed` renames | deferred | until each row gains its operand, so the hash moves once | no — K-24 |
| `evade / defy`, `tie / knot` splits | when built | openers derive per `Tenure(...)` literal (`rosters.yaml:116-131`) | no — K-24 |

---

## 4. Hooks for the existing 44

*Hook* is how a question forms the act and what it writes; *falsifier* is the observable that would show
it hooked. "Realm ex" means executions in `python -m engine.season.harness.aperture 4 0` (the populated
realm, four seasons, seed 0); the `att/ex` pairs quoted are from `requirements.yaml:674-676`, not re-run.
"Q2" is the question source that names a referent the person holds a claim about. "The enabler" is the
held-Record operand channel of §10.1. Full blocks are in Appendix A.

| verb | hook (route · rows) | why | falsifier | blocker · needs_jordan |
|---|---|---|---|---|
| `build` | a question whose referent is a `works` the actor holds · `Site.exists` | housing throttles migration (`effects_migration.py:140-149`) | leaves the always-refused pin (`test_season_shape.py:7624`); realm ex > 0 (65/0) | H-165 limit 2, carried as J-4 · no new row |
| `carry` | the petitioner holds his petition; on `open_case`'s body, writing the petition's `Record.stages` · `DocketItem.matter` | a complaint reaching a bench without a seat's leave | `test_record_kind_fold.py:119` (`..._and_carry_is_not`) flips | H-63, answered by precedent · no |
| `commit` | `_eff_utter` mints the utterer's `hold` on the Proposition, so Q2 can name it; a Proposition named in a held `treaty` or `alliance` reaches it through the enabler · `Tenure.since` | utter → commit → ambition → a quiet-season act; a covenant's acceptance; a war's backing | leaves the always-refused pin | H-156; a hold buys budget (`budget.py:57-58`) · no for the hook; H-156 (a)/(b) stays Jordan's |
| `comply` | the executor holds the writ after `give`; `comply` forms on the held writ and emits `compliance.given`; what it performs is the separate `transfer` the writ names · none | obedience with a trace, so defiance is legible by absence | `compliance.given` in `w.log` from `populated.run` with no hand-built act | H-44, H-94; ED-IN-0211's fork stays open · no (retained by ruling, K-01) |
| `confer` | the office rides `subject` from a held dispensation's `terms` (the enabler), the conferee rides `to` via the known-person fan (`options.py:827-860`) · `Tenure.since/until` (+ `Tenure.term`, §7.2) | patronage | realm ex > 0 (70/0) | a holder's own seat is in `reach` (`world_q.py:461`); what is absent is any claim about a seat (`verb_table.yaml:676`) — K-25 · no |
| `construe` | WITNESS-side, not an act: the content deposit already reads per holder (`witness.py:40,523-540`) · none | misreadings that travel by document | two holders of one writ holding different `content:dispensation` values | H-36 magnitude half, H-44 · no (retained by ruling) |
| `convene` | pass CALENDAR's events into `witness()` (`driver.py:464`); `open_case` fills the fired slot's date · `Date.due_at`, `DocketItem.matter` | a sitting with a day people act toward | a `date.fired` claim in any ledger (`test_season_shape.py:4307-4316` pins 0) | H-163 limits 2, 4 · no |
| `create_record` | hooked; a computed act mints contentless `text` · `Record.exists`, `Record.stages` | documents to find, carry, forge, burn | corpus executed set; `test_works_founding.py:101` | H-80 · no |
| `destroy_record` | `give`'s shape, built and held (`verb_table.yaml:199`) · `Record.exists` | the only way a document vanishes; in the suite, also how a `cover` Record is ended | `test_u7_own.py:153` flips | H-75; held on H-156 · yes, no new row (H-156) |
| `determine` | a question whose referent is a docketed person in the bench's ground; direct via seat; contested in the suite (§7.2) · `Tenure.since`, `DocketItem.matter` (+ `Tenure.degree`) | a bench binding men with no player watching | realm ex (1/20); `test_u7_remit.py:278` | H-163 limit 2 (SC lane), H-162; the party-gap fold edit (K-02) · no |
| `dispatch` | hooked; the named person gets a claim about himself · none | a command the chronicle carries | leaves the never-attempted pin (`test_season_shape.py:8372`) | none · no (retained by ruling) |
| `establish` | operands outside the closed eight refuse; the enabler's `terms` replaces the `office` payload key; direct via seat · `Office.exists`, `Office.remit_acts`, `Tenure.payload` | institutions that grow | realm ex > 0 (19/0) | plan position `15c` · no |
| `evade / defy` | held writ; `evade` = no transfer before the term matures; `defy` = a public refusal; split when built (K-24) · none | disobedience others see or miss | `compliance.withheld` from computed play | H-44, H-94 · no (retained by ruling, K-01) |
| `examine` | hooked on a co-located Site · none | a clue that is somewhere | a `finding.made` claim with non-trivial value | work item 4.5 · no |
| `exchange` | needs the counterparty's `kind`/`amount`; `_shift` twice · `Rung.stores` | trade, scarcity paired both ways | `exchange.made` in `w.log` | H-94 · no new row — registered (`rosters.yaml:1562-1564`) |
| `fight` | hooked; any person referent but self; also the acceptor of a challenge `petition` (K-23) and the enforcement seat-holder against a prisoner (§9.8) · by band | the irreversible personal stake | `test_season_shape.py:12776`; corpus `DEGREES RESOLVED` | H-98; the deontological gate · no |
| `forge` | a faction the forger holds a claim on (`survey`'s cell); `survey`'s mint with perturbed content · `Record.exists`, `Record.forgery_quality` | a false sheet a rival acts on | `test_information_cluster.py:297` stops asserting that no act forges | H-169 limits 2, 5 (a consumer first) · no |
| `found` | as `build` · `Rung.exists`, `Tenure.since` | new hearths | realm ex > 0 (70/0) | H-165 limit 2 (J-4); H-166 · no new row |
| `give` | hooked; the known-person fan · `Tenure.until/since` | a writ reaches the hand that can deny it | `test_give.py:94-399` | none · no |
| `interview` | hooked · none | to be replaced by the Dialogue Lattice (`verb_table.yaml:1054`) | corpus executed set | work item 4.5; ED-FI-0004 · no |
| `issue` | hooked (realm 6/30, with `via`); in the suite `to` fans over known persons so `terms` and the executor separate (§10.1) · `Record.exists` | authority as paper; the warrant | `test_u7_remit.py:460` | H-94; `15c` · no |
| `levy` | a question whose referent is a full larder in purview (a positive `stores.changed`) · `Rung.stores` | how a seat eats | realm ex > 0 (23/0); `test_u7_remit.py:201` | H-163 limit 3 · no |
| `march` | declared in the realm (16), fought 0 — H-149's check refuses every natural target (K-31); never attempted in the corpus (H-175); seam at ENCOUNTER · `Person.body`, `Person.stance`; in the suite also `Tenure.until/since`, `Person.travel_leg` (the arrival, §9.6) | war that leaves grudges, and armies that stand somewhere | `test_march.py:323`; leaves the never-attempted pin | H-175, H-149; the `muster` basis and three `ENC` cells (K-33) · no |
| `migrate` | a destination channel: shortfall at home plus a positive `stores.changed` elsewhere in reach, or a founded hearth with room · as `move` | people who leave famine | leaves the always-refused pin | H-168 (H-94) · no |
| `move` | hooked · `Person.travel_leg`, `Tenure.until/since` | presence is the epistemic model | `test_migrate_capacity.py:153` | none · no |
| `oblige` | type clause 1 once a seat can be a referent — from a held Record's `terms` (the enabler) or a `tenure.opened` deposit (K-25) · `Tenure.since`, `Tenure.term` | retinues; vassalage, read by `purview_reaches` (H-101) | `test_obligees.py:282` flips; leaves the never-attempted pin | seat referents (H-94/H-54) · no |
| `open_case` | hooked (realm 7/28) · `Record.exists`, `Record.stages`, `DocketItem.matter` | grievances enter the institution | `test_u7_remit.py:246` | H-52 · already registered |
| `petition` | hooked; addressed to its own subject until the enabler separates them · `Record.exists` | the upward voice; accusation and challenge | `test_record_kind_fold.py:153` | H-94; closers unbuilt · no |
| `reconstruct` | hooked; a self-feeding loop is visible (`test_season_shape.py:3974-3977`) · none | synthesis that can be wrong | corpus executed set | the obstacle; work item 4.5 · no |
| `release` | a person-side decline in `opening_set` when the actor holds no releasable edge to the referent · `Tenure.until` | resignation, divorce, apostasy, *diffidatio* | refusals fall from 96% (`requirements.yaml:759-760`) | none · no |
| `repudiate` | cut; `_eff_release` earns `commitment.ended` on a closed `commit` | nothing new | `test_u7_own.py:42` DECLINED tuple shrinks | none · yes (R-3) |
| `research` | hooked · none | archives | corpus executed set | work item 4.5 · no |
| `restore` | hooked (realm 18/82) · `Site.condition` | towns that mend; walls before a march | `test_works_founding.py:237-282` | H-164, H-166 · no |
| `revoke` | the office rides `subject` from a held dispensation's `terms`, as `confer` · `Tenure.until` | a lord unmaking a subordinate | realm ex > 0 (15/0) | seat referents; H-91 · no for the hook |
| `speak` | hooked (executes); no change proposed · none | speech nobody is told | stays in the executed set | none · no |
| `succeed` | heir via the known-person fan; a reader at the vacancy — `conferral_bases` is closed at appointed/elected/annex (`rosters.yaml:1737-1755`) · `Tenure.since` | dynasties | a `person.died` followed by the heir's `hold` | ED-IN-0256 ruling (2) · yes (R-5) |
| `surveil` | hooked; the Person case waits (§9.7) · none | the covert act canon prices (`rosters.yaml:2205`) | corpus executed set | ED-FI-0009; work item 4.5 · no |
| `survey` | hooked (realm 10/165); subject Rung in the suite (§7.2) · `Record.exists` | a stake once something reads the sheet | `test_information_cluster.py:146,204` | H-169 limit 5 · no |
| `tell` | hooked · none (WITNESS) | rumour and the chain of tellers | `test_told_by_channel.py:1042` | `sigma`'s `REFUSED` raises an uncaught `Unspecified` (`resolve.py:585-590`) · no |
| `thread_read` | a per-person TS value and a gate stem; `knowledge_kinds` is the taxonomy half · none | P-08's barrier made mechanical | enters `resolvable_verbs()` | H-85; plan 27/29f · no |
| `tie / knot` | partner via the known-person fan; `tie`'s reader is `teller_weight`'s relation term; build as two rows · `Tenure.since` | telling knits people | `tie / knot` executes > 0 in `aperture 1 0` | H-182; `29f` owns `knot` · no |
| `transfer` | hooked · `Rung.stores`, `Tenure.term` | relief, tribute, pay | `test_season_shape.py:9328`; `test_term_upkeep.py` | H-158 · no |
| `utter` | hooked but reaches nobody's questions; mint the utterer's `hold` · `Proposition.exists` (+ `Tenure.since`) | vows that bind the speaker; a covenant's terms; a declaration of war (mood `WAR`, K-29) | a `commit` executing on a `prop:` id in `populated.run` | H-92, the cost of a hold · no |
| `work` | as `build` (the J-4 works channel); declared delta ≥ 0 · `Site.condition` | a works advanced by hands | leaves the always-refused pin | H-165 limit 2 · no |

### 4.1 Dependency order (pass 1)

1. **A second operand channel** beyond the question's one referent (`options.py:741-746`; H-94/H-54) —
   gates `confer`, `revoke`, `oblige`, `determine` (limit 2), `levy` (limit 3), `migrate`, `exchange`,
   `establish` (`15c`). It is step 1 of the suite's build order (§10.4).
2. `utter` mints a hold → `commit` binds → `ambitions`/need questions; with R-3, `repudiate` folds into
   `release`. Step 2 of §10.4.
3. `give` puts a writ in the executor's hand → `comply`, `evade / defy`, `construe` become formable →
   H-44 decides what compliance performs.
4. CALENDAR events reach WITNESS and `open_case` fills a fired slot → `convene` → `determine` (H-163
   limits 2, 4; SC lane).
5. The J-4 works channel → `found`, `build`, `work`.
6. H-156's ruling → `destroy_record`'s held shape, `found`/`build` formation policy, `commit`'s cost.
7. A sheet consumer (H-169 limit 5) → `forge` → `destroy_record` as the burn.
8. `teller_weight`'s relation reader → `_eff_tie`; `knot` after `29f`.
9. A ruling on succession as a conferral basis → `succeed`'s heir operand and a reader at the vacancy
   (R-5).
10. The investigation degree producer (work item 4.5) → the six findings stop being one act with six
    preconditions; one producer shape per verb (§6.3): `research` first, the cheapest, since both its
    readers exist (the content deposit); `examine` and `surveil` (the log at a place); `interview` as a
    prompt (K-36); `reconstruct` waits on a value space (K-37) and `thread_read` additionally on H-85.

---

## 5. Coverage

Pass 2 grouped the 707 candidates into 61 act families; revision 4 adds a 62nd, theft, from three
extraction rows pass 2 left in no family (K-39). Each is classified against the resolved suite:

- **COVERED** — an existing verb carries the family's central act, sometimes as data (an accusation is a
  `petition` whose `terms` names the accused);
- **WIDENED** — an existing verb carries it once one named reach widens (§7.2);
- **GAP** — no existing verb can; filled by a new verb (§9.1–§9.4);
- **DEFERRED** — the family's central act waits on a named ruling, grammar change, reader or plan
  position (§9.7);
- **OUTCOME** — the family names a result, not a choice; by direction 3's logic it is not a verb;
- **SYSTEM** — a property of a mechanism, a seam or a loop stage, not an act (§10.3).

**Counts, one primary class per family:** COVERED 32 · WIDENED 6 · GAP 10 · DEFERRED 5 · OUTCOME 4 ·
SYSTEM 5 — 62 in all. Verbs: 6 widened, 12 new, and every new verb fills at least one GAP family.
[Revision 4 adds family 62 (steal, pilfer) as GAP, filled by `steal` on R-8's recommendation (K-39);
the family exists whichever way R-8 is ruled, and under R-8 (b) it would stay GAP with no verb. No other
family changes class; families 6, 11, 26, 27 and 30 gain the charge, testimony, hostage and theft
readings (Appendix B; K-35, K-38).]
[Revision 3 moves two families: 21 (declare war) from GAP to COVERED — `utter` of a `WAR`-mood
Proposition plus `commit`, read by `faction_q.at_war` (K-29); and 24 (siege, blockade) from GAP to
WIDENED — a `march` that arrives at an enemy-held settlement, the siege a Query (K-28). Family 25 stays
OUTCOME with its text changed (R-2 resolved); 13 stays DEFERRED with `proclaim` deferred (K-34).]
[CORRECTION: revision 1 reported COVERED 29 · WIDENED 9 · GAP 14 + 1 · OUTCOME 3 · SYSTEM 5, then withdrew
one WIDENED family in the same table without moving it (K-26). The suite moves seven families: 4 and 37
(their widenings deferred, K-16, K-15), 13 (its kinds deferred, K-11) and 40 (`debt` deferred, K-14) to
DEFERRED, beside 47; 14 (the vote is the holder's own `commit`, K-07) and 53 (expulsion is lapse, §7.2) to
COVERED; and 28 to OUTCOME (R-1).]

| class | families (Appendix B numbers) |
|---|---|
| COVERED (32) | 1 question a person · 2 inspect a place, body or object · 3 read and decipher records · 5 evidence board · 6 denounce, accuse · 7 open an inquiry or impeachment · 8 summons, writ, warrant, charter · 11 confess, swear, abjure · 14 motion, debate, vote · 15 elect · 16 appoint, invest, ennoble · 17 depose · 18 resign · 21 declare war (`utter`, mood `WAR`, + `commit`) · 23 muster · 31 spy, infiltrate, run informants · 33 expose, publish · 34 blackmail · 35 bribe, gift, subsidy · 36 court, marry · 39 trade, venality · 41 build, found, charter · 42 survey, census, visitation · 43 envoy, legate · 44 feast, coronation, progress · 49 claim, coup, revolt · 50 mediate, appeal, stay, adjourn · 51 recognize, endorse · 53 admit, expel · 54 defect, poach · 55 challenge and accept · 57 regency through a seat |
| WIDENED (6) | 9 hear, try, judge (`determine` contested) · 12 excommunicate, absolve (`determine` disposing `ban`; `pardon`) · 19 heir, regency (`confer` + term) · 20 homage, fealty (`oblige`, read by `purview_reaches`) · 24 siege, blockade (`march` arriving at an enemy-held settlement; the siege a Query; its larder effect deferred) · 29 outlaw, banish (`determine` disposing `ban`) |
| GAP (10) | 22 truce, peace, treaty, alliance, cession (`covenant`, kinds `treaty` and `alliance`; cession by widened `give`; truce deferred, K-32) · 26 arrest, custody, ransom, hostage (`detain`, `pardon`; a hostage composed on `move` + `issue` + `detain` + `pardon`, K-38) · 27 interrogate (`interrogate`) · 30 seize, confiscate, search (`seize`) · 32 cover identity, deniability (`conceal`) · 38 persuade, convert, preach (`argue`) · 45 heal, rest (`tend`) · 46 train, educate (`train`) · 52 damage, raze (`sabotage`, `raze`) · 62 steal, pilfer (`steal`, R-8) |
| DEFERRED (5) | 4 watch a place, tail a person (the place is `surveil`'s; the person waits on a grammar disjunction, K-16) · 13 edict, law, emergency (`proclaim` deferred with its readers, K-34; its `edict`/`emergency` kinds wait on a reader each, K-11) · 37 slander, rumour (the telling workplan's G7, K-15) · 40 borrow, distrain (`debt` waits with its `seize` reader, K-14) · 47 thread operations (plan positions 27/29f, `verb_table.yaml:1103`) |
| OUTCOME (4) | 10 sentence (the disposal's kind: `oblige`, `custody`, `ban`) · 25 conquer, raid, usurp (a won or unopposed `march` writes occupation; title by `seize`, `give`, `release` or death, R-2 resolved) · 28 execute (a `fight` against a prisoner in `custody`, R-1) · 48 murder (a `fight` whose band is `Felled`, with `conceal`) — and, by direction 3, `kill` and `wound` |
| SYSTEM (5) | 56 privileged counsel · 58 combat and battle moves (inside the seams) · 59 negotiation moves (inside a bout) · 60 events (disaster, plague, dearth, mutiny, death, succession, heresy outbreak, clocks, endings) · 61 inner mechanics (§10.3) |

[NULL: all 62 families — examined for a family needing a fifth eligibility kind or a non-person actor;
none found. Every faction-scale row resolved to an office-holder's act through a seat, or to members'
own acts counted by a Query.]

### 5.1 What each source contributed

What each source supplied that the others did not, and which suite members it stands behind. The
per-family evidence is Appendix B.

| source (rows) | distinctive contribution | suite members and states it backs |
|---|---|---|
| `research/` (80) | faction- and office-scale acts the setting's own research catalogued — sanctions put to a vote of factions, war declared with a compliance window, cession and tributary status, leagues, confinement and hostage-kin, the Riskbreakers' Shadow Renown and Deniability Debt meters — and nine event cards | `covenant`, `detain`, `pardon`, `conceal`; war (an uttered Proposition), treaty, alliance, hostage (embargo deferred with `proclaim`, K-34) |
| governance proposals (67) | the 25 provisional faction actions; the proceedings design (speech kinds as data, hearing, quorum, stay, appeal by nesting, interposition, dissent); the inquisition procedure of `proposals/2026-09-04-social-contest-branches/03_INQUIRY.md` (a 2–4-season case, one interrogation per season, a three-way verdict, an excommunication tribunal, abjuration, a parliamentary stay); Riskbreaker operations | the contested `determine`, `interrogate`, `seize`, `conceal`; excommunication, sentence; the faction map (§10.2) |
| narrative and play proposals (80) | the closers named and never built (waive, depose, fray, rescind, withdraw, abolish); the pursuit-basis worksheet's kill/wound and challenge/accept rulings; cover, planted evidence, infiltration, outlawry | `conceal`, `seize`, `train`; the single outlawry carrier (`ban`); challenge as a `petition` (K-23) |
| season-loop demand (77) | what the running code and its registers say cannot be expressed, by hole id and case count: no custody kind; `church_standing` with no producer; a sentence read as a job (H-173); a graded hearing (H-162) and the four unseeded procedure games (`arrangements.yaml:16-21`); seizure (H-84); concealment (12 cases); recruiting (13); nothing raises `Person.body`; `Person.capability` retired; nothing ends a place (H-166) | `detain`, `seize`, `conceal`, `tend`, `train`, `raze`, `sabotage`, `argue`; custody, excommunication, sentence |
| detective games (107) | the investigation family confirmed in all seven; *Pentiment*'s church hearing, judgement and execution; *L.A. Noire*'s read of a lie and the charge; arrest in three games; evidence decay; the time budget. **Negative:** no warrant, covert identity or distinct confession act verified in any of the seven | `detain`, `interrogate`; execution as custody + `fight` (§9.8); §10.3 |
| CK3 and RTK (107) | CK3: crime as a standing legal basis for imprisonment and revocation; imprison, torture, execute, ransom; hooks and blackmail; casus belli, war goals, truces; fealty and vassal contracts; excommunication and holy war — every act a character's, as Valoria rules. RTK XIV: the schemes line (sabotage, estrangement, incited defection), alliances, submission demands — there the force itself acts | `detain`, `pardon`, `covenant`, `sabotage`, `raze`; war as an uttered `WAR` Proposition; `march`'s stakes; vassalage through `oblige` |
| governance history (189) | procedure, step by step: the parliamentary motion, division, supply, impeachment and prorogation; the royal writ, edict, homage and *diffidatio*, pardon, regency; Venice's lot-and-ballot election, quorum, the Ten, the *bocca di leone*, the Avogadori's suspension; church justice from denunciation and the edict of grace through citation, interrogation, torture under limits, sentence, abjuration, relaxation, confiscation, excommunication and interdict; secular warrant, arrest, bail, *habeas corpus*, ordeal, execution, informants, interception, double agents | the procedural spine of the Active Inquisition chain (§10.2); `detain`, `interrogate`, `seize`, `pardon` (edicts and interdicts deferred with `proclaim`, K-34); the vote as members' own `commit`s and homage as `oblige`; custody, excommunication, outlawry (interdict and heresy declared deferred) |
| the survey, supplied by Jordan, not committed (58 primitives) | a primitive-level decomposition across investigative, narrative and grand-strategy games: the verification scale (per-item grading, batch confirmation, consequence-tested submission, no verification), approach over classification in questioning, stores of obligation spent at visible thresholds, agenda control, and succession as an investigable case. **Negative:** no primitive the suite lacked except theft and approach; most of its grand-strategy primitives (hooks, forced votes, intel levels, timers) are refused here by ruling or axiom (§6.4) | `steal`; the charge as an uttered Proposition (K-35); the verification policy and the six findings' producer shapes (§6.1, §6.3); approach as data; `carry` (P43) |

---

## 6. The survey interrogated

The source is *Mechanics of Inquiry, Speech and Rule* (prepared 3 October 2026), supplied by Jordan and
not committed (§1). It breaks investigative, narrative and grand-strategy games into 58 primitives —
each the smallest unit of a mechanic that keeps a distinct function, labelled input, state, rule or
feedback — and groups them into eleven verb families: A attending, B asking, C reading, D recording,
E judging, F committing, G being, H entering, I binding, J ruling, K concealing. Direction 9 asks that it
be used to interrogate the verbs. The survey is evidence of how other games are designed; **what
Valoria does is decided by the code**, so each verdict names its deciding site, and where a survey
pattern meets a ruling or an axiom the ruling stands (§6.4). Each primitive is written out where it is
used. The survey's evidence caveats are carried in §1, its unverified items in §14.2, and the conflicts
this interrogation raises against the suite itself are K-35…K-40 (§12).

### 6.1 Findings and recommendations, and the verification policy

The survey has four findings and four recommendations.

| the survey's item | verdict | deciding sites |
|---|---|---|
| **Finding 1** — verification organizes investigative design, on a four-point scale: per-item grading (*L.A. Noire* grades every interrogation answer against a hidden reading); batch confirmation (*Return of the Obra Dinn* confirms deductions only in sets of three, the last six fates in twos); consequence-tested submission (*Lacuna*, *Shadows of Doubt*: a judgment is accepted whether or not it is right and the world answers later); no verification (*Pentiment*, whose director said there "cannot be a right answer"). What questioning, a clue and a failure are follows from where a game sits | **APPLIES** as the organizing question; the scale has no point for Valoria's answer (below) | `loop/witness.py:380` — every event-kind deposit is `Claim(cid, pid, subj, e.kind, True, …)`, so a finding today is `(subject, "finding.made", True)`, content-free; AX-7's falsifier names that deposit "a contradiction to fix" (`01_AXIOMS.md:314-317`); work item 4.5 (`verb_table.yaml:982-989`); `reconstruct`'s obstacle and Failure (`:1113-1115`); investigation its own kind, never a contest (`rosters.yaml:1031-1034`); `determine` reads no truth (`loop/effects_information.py:284-297`); `proofs` rostered and weighed by nothing (`rosters.yaml:1818-1828`); `record()` (`decision/options.py:1001-1040`); fading (`loop/matter.py:235-265`) |
| **Finding 2** — politics, at character and at strategic scale, is an economy of obligation: votes (*The Republic of Rome*), hooks and secrets (*Crusader Kings III*), budget and authority (*Suzerain*) are stores of owed compliance, built by conversation, payment or discovery and spent at a procedural chokepoint | **PARTLY** | stores are owned edges with terms, never counters (`Tenure`; `commit`, `oblige`, and `transfer` renewing terms, `verb_table.yaml:1149`); the chokepoint is `determine`'s quorum conjunct (`:224-229`), which at the shipped `bench_quorum` of 1 cannot refuse (`data/fixtures.py:724`, as cited); an aggregate is never a field (T-a, `01_AXIOMS.md:327-354`); compelled compliance, the survey's hook, is refused by ruling (D-5, `verb_table.yaml:757`) |
| **Finding 3** — espionage at strategic scale is investigation seen from the other side: what *Shadows of Doubt* asks the player to find (traces, prints, a name), *Crusader Kings III*, *Hearts of Iron IV* and *Espiocracy* ask the player to hide, delay or counter | **APPLIES** structurally; one half unbuilt | every act is a trace to whoever is present (`epistemic.py:322`); hiding is `conceal` (§9.3); countering is presence; taking is `steal` (§9.3, R-8). Unbuilt: a trace readable later, at a place, by someone who was not there — 4.5's content for `examine` and `surveil` (§6.3) |
| **Finding 4** — player verbs fall into eleven families; grand strategy delegates many of them to agents and timers | **APPLIES** for the families (§6.2, §6.3); **DOES NOT APPLY** for agents and timers | an agent is a Person with his own ledger and choice (AX-1); a "timer" is a `Tenure.term` or `Record.stages` some act wound; nothing executes on a schedule (AX-5's three motions; T-i, `01_AXIOMS.md:482-484`) |
| **Recommendation 1** — fix the verification policy first, choosing consciously among the four points; mixing them produced *L.A. Noire*'s strain | **APPLIES** — decided below | as Finding 1 |
| **Recommendation 2** — prefer approach verbs (press, flatter, threaten: *Lacuna*, the *L.A. Noire* remaster) to classification verbs (Truth / Doubt / Lie) | **PARTLY** — no classification verbs, already true; approach verbs **DO NOT APPLY**; approach is data | below |
| **Recommendation 3** — model political action as stores of obligation spent at visible procedural thresholds: show the threshold, hide part of the count, make each store traceable to a conversation or discovery; agenda control is the primitive most missing from videogames | **PARTLY** | below |
| **Recommendation 4** — treat succession as an investigable case: no examined game asks the player to establish legitimacy by evidence and testimony | **APPLIES** as intent; **PARTLY** carried | below |

**The verification-policy decision.** Valoria's policy — the one its code already implies, and the one
an engine with no GM can hold — is **consequence-tested submission over held truth, with hidden
reliability grading of evidence at production, and judgment of a Proposition as probability, not
verification.** The survey's scale has no point for it. Four clauses:

1. **Truth is held, never handed over.** World state and the append-only log are the truth. A claim is a
   reading — `Claim.source`, `chain`, `confidence` — that may be false (AX-2, `01_AXIOMS.md:104-120`) and
   that fades in confidence, never in value (`loop/matter.py:235-265`; AX-3's carve-out, `:130-141`).
   WITNESS lands evidence: it moves what is held true and never what is held right (T-j, `:486-488`).
2. **No judgment is marked.** No row's `emits:` names a correctness kind; `determine` opens its disposal
   on whoever is docketed and reads no truth (`loop/effects_information.py:284-297`); an accusation is a
   `petition` minted regardless (`:300-319`). The world answers later: `record()` lowers a teller whose
   word contradicts what the hearer holds firsthand (`decision/options.py:1001-1040`), and `pardon`, a
   nested `open_case` and `release` reverse what was done (AX-6: every irreversibility is authored and
   contestable).
3. **Evidence is graded at production, by band, hidden.** 4.5's text is the shape
   (`verb_table.yaml:982-989`): a finding deposits a claim whose value and confidence the band decides,
   and Failure deposits nothing. The actor holds a claim, never a score. 4.5 is a plan work item, which
   the table itself calls work and not a ruling (§14.9).
4. **Judgment of a Proposition is probability.** `interrogate`, `argue` and the contested `determine`
   roll pool against obstacle (`seam/wrappers/sigma.py:159-170`) — the survey's own reading of grand
   strategy, where "judgment becomes probability": not whether the player is right, but how likely a
   plot is to succeed.

**Why the other three points fail here.** *Per-item grading* needs one correct reading per line and an
unmediated mark: a reading someone authors — and there is no one to author it (`reconstruct`'s canon
obstacle needs a scope "chosen at opening BY A GM", `verb_table.yaml:1113`) — and a deposit AX-7
forbids. *Batch confirmation* needs a confirmation surface the engine owns and the character reads; a
confirmed deduction is the engine's own resolution handed into a ledger unmediated, which AX-7 forbids
(the survey interrogation grounded this on T-j; T-j's belief is what is held right, so the ground is
AX-7 — §14.9), and nothing in the loop confirms anything to anybody. *No truth value* is false of the
world — AX-2's "may be false" presupposes a truth — but true of the bench today: `proofs` is read only
by the arrangement loader's membership check (`data/arrangements.py:200-201`), nothing in the fold
weighs it, and `Tenure.degree` has no producer (H-162). That is the defect the contested `determine`
closes, not the policy to adopt. **The survey's mixing warning does not bite:** *L.A. Noire*'s strain
comes from grading a reading of a person; Valoria grades no reading (`tell` contests the hearer's
standing), and its two layers sit on different objects — evidence's reliability at production, a
judgment's consequence afterwards.

**Where the policy bites, in order.** (i) 4.5's producer must deposit content read from the world,
mediated by band and channel — never a bare `True` (AX-7's falsifier). (ii) `interrogate`'s
`confession.made` must carry the charge (K-35). (iii) The contested bench's obstacle should be read from
testimony — live `commit`s to the charge — not from the accused's `capability/2`, which is what
`_obstacle_of` reads for a person subject (`seam/wrappers/sigma.py:105-122`): an observation for the SC
lane, whose ED-SC-0033 clause 3 names the proceedings subsystem the obstacle's owner
(`rosters.yaml:1138-1148`).

**Approach is data, not verbs (Recommendation 2).** *No classification verb* is already true: no row
grades a reading; `interview` is existence-only (`verb_table.yaml:1043-1048`); `interrogate` disposes the
charge, not a reading (§9.1); `tell`'s credit to a teller is computed, never chosen
(`decision/options.py:1043-1093`). *Approach as separate verbs* does not apply: Jordan's six-as-six and
canon's "No new action vocabulary" (`verb_table.yaml:950-960`), ED-FI-0004's fold of `interview` into
the Dialogue Lattice (`:1054`), and this suite's own rule — no discriminating axis, no verb. Approach is a
non-operand payload key on the one row, read by the effect or the obstacle, on `mood`'s precedent on
`utter` (`loop/effects_information.py:467`); its reader is the subject's regard
(`queries/person_q.py:63-69`, today the stored half only). A computed act carries no non-operand key —
its payload is its operands and `subject` (`decision/choose.py:358-369`) — so approach is hand-built
until the decision layer supplies a source.

**Recommendations 3 and 4, where they land.** *Recommendation 3:* the threshold is data (the `quorum`
key; `bench_quorum`); the count is a Query the fold reads (K-07) that no character holds (AX-2) and the
player always can — "No state is hidden from the player" (`01_AXIOMS.md:299-304`). Every store is
traceable by construction: a `commit` is an act in the log with its causes. Agenda control is present in
pieces — the docket (`queries/world_q.py:152-166`), `open_case` by remit, `carry` by right (declined
today), `convene`, the speaking order `order:` (`arrangements.yaml:95, :112`) — and the missing piece is
the join: CALENDAR's `date.fired` never reaches WITNESS (`queries/world_q.py:1362-1367`) and `open_case`
dockets with `date: None` (`loop/effects_information.py:220`), H-163 limit 4, registered (§10.3). The
survey is evidence for building `carry` (§3.5). *Recommendation 4:* `succeed` opens an edge nothing
reads (`verb_table.yaml:839`); the six findings deposit claims; the contested `determine` grades with
evidence entering nowhere. The tree already has the channel under another name — the faction map's
Succession Endorsement, each endorser's own `commit` to the claimant's Proposition (§10.2) — and an oath
is an utterance (`01_AXIOMS.md:1399-1403`). Legitimacy is the claimant's uttered Proposition, the
endorsers' commits, the findings held about it, and a bench whose obstacle reads those commits: SYSTEM
(the proceedings provider) plus R-5, with no new verb; the law that chooses among heirs is K-40.

### 6.2 The primitive map, P1–P58

Each line: the survey's primitive and its game, then the verdict, the carrier and the site. CARRIED —
the code does it; PARTLY; GAP; STATE or SYSTEM (§5's senses); DEFERRED; DOES NOT APPLY.

| P | the survey's primitive | verdict · carrier or reason |
|---|---|---|
| 1 | limited time slots — *Pentiment*, *Consulting Detective*: curiosity has an opportunity cost | CARRIED · the scene budget (`decision/budget.py`), which the person triages |
| 2 | clock advanced by reading — *Esoteric Ebb* | CARRIED as "every act costs a scene"; no reading clock (AX-5) |
| 3 | social occasion as information gate — *Pentiment*'s meals | PARTLY · presence witnessing (`epistemic.py:322`), `convene`; no companion choice |
| 4 | highlight mode — *Lacuna* | DOES NOT APPLY (presentation) · the analogue is Q2 surfacing what one may act on |
| 5 | result cap on queries — *Her Story*, five clips per word | CARRIED · the `View` cap |
| 6 | decaying evidence — *Shadows of Doubt*: prints and footage expire | CARRIED · confidence fades at MATTER (`loop/matter.py:235-265`); `Record.ttl` has no reader |
| 7 | three-way response — *L.A. Noire*: Truth / Doubt / Lie, one correct per question | DOES NOT APPLY · no row classifies a statement; a teller's credit is computed (`decision/options.py:1043-1093`) |
| 8 | evidence-gated accusation — *L.A. Noire*, *Ace Attorney*: name the item that contradicts | PARTLY · `tell`'s `holds` gates telling; `petition` gates nothing on evidence; testimony enters through the charge (K-35), not a petition precondition |
| 9 | approach choice — *Lacuna*, the *L.A. Noire* remaster | GAP → data · a payload key on `interview` and `interrogate` (§6.1) |
| 10 | generic prompts, payment, confrontation — *Shadows of Doubt* | CARRIED · `interview` existence-only; `give`, `transfer`; a challenge `petition`; `detain` |
| 11 | keyword query — *Her Story* | DOES NOT APPLY · the analogue is Q2's third clause, whom a claim's content names (`queries/world_q.py:1433`) |
| 12 | physical trace and name lookup — *Shadows of Doubt* | PARTLY · `seen` claims name `who` unless a channel withholds it (`epistemic.py:863-891`); no trace at a place for a later reader (§6.3) |
| 13 | frozen-moment record — *Obra Dinn* | CARRIED · a `faction_sheet` resolved at writing and frozen; the append-only log |
| 14 | inference from indirect markers — *Obra Dinn*: clothing, speech, position | PARTLY · `Seen` terms per channel; `why` always `None` |
| 15 | facial performance as evidence — *L.A. Noire* | DOES NOT APPLY · replaced by `record()` (`decision/options.py:1001-1040`) |
| 16 | structured hypothesis slots — *Obra Dinn*, *Lacuna*, *Shadows of Doubt* | PARTLY · the claim's `(subject, predicate, value)`; exact Record keys |
| 17 | free-form evidence board — *Shadows of Doubt* | DOES NOT APPLY · `reconstruct` writes nothing (§10.3, "none yet for links") |
| 18 | automatic logs — *L.A. Noire*, *Lacuna*, *Tails Noir* | CARRIED · WITNESS deposits unasked into `Person.ledger` |
| 19 | quest log as growth — *Esoteric Ebb* | PARTLY · ambitions raise need questions; `Person.pursuits` has no writer until `argue` |
| 20 | per-item grading — *L.A. Noire* | DOES NOT APPLY · AX-7; no mark is emitted (§6.1) |
| 21 | batch confirmation — *Obra Dinn* | DOES NOT APPLY · AX-7; no confirmation surface (§6.1) |
| 22 | submission regardless of correctness — *Lacuna*, *Shadows of Doubt* | CARRIED · `petition`, `determine`; consequence through `record()`, `pardon`, a nested `open_case` |
| 23 | no truth value — *Pentiment* | PARTLY · true of the bench today, false of the world (§6.1) |
| 24 | irreversibility — *Lacuna*, *Pentiment* | CARRIED, inverted · AX-6: every permanence authored; a Proposition immutable; `Felled` |
| 25 | remembered-choice notice — *Pentiment* | DOES NOT APPLY · no state is hidden from the player (`01_AXIOMS.md:299-304`); provenance is `causes` and `chain` |
| 26 | convergent branching — *Tails Noir* | DOES NOT APPLY · no script; R's half with no player in it (CLAUDE.md §0.06) |
| 27 | line closed on error — *L.A. Noire* (and *Disco Elysium*, §6.4) | DOES NOT APPLY by design · a refusal emits; no lockout without an author (AX-6) |
| 28 | soft failure — *Shadows of Doubt*: beaten, you wake in hospital | CARRIED · `Failure` and `Untouched` emit and cost a scene; a body-band penalty on the budget |
| 29 | background flag — *Pentiment* | PARTLY · conviction refusal (H-146); the Thread Sensitivity gate unbuilt (H-85) — `thread_read` is P29 made metaphysical (P-08) |
| 30 | attribute voice — *Esoteric Ebb*, *Disco Elysium* | DOES NOT APPLY (presentation) · §10.3, "none yet for interjection" |
| 31 | dice check, one-time or retriable — same | CARRIED · the `sigma_leverage` roll; S27.4's refusal; retry bounded by the budget only |
| 32 | identity assertion — *Esoteric Ebb* | PARTLY · `conceal` and `anchor_of` (§9.3); a `commit` to a creed |
| 33 | play-as-heir — *Crusader Kings III* | DOES NOT APPLY (no player model in the loop) / STATE through R-5 |
| 34 | trespass as categorical crime — *Shadows of Doubt*: any illegal act seen provokes attack; its size is the fine's | GAP → SYSTEM (reception) · no access state on a place; `presence:` eligibility still declines unconditionally (`decision/options.py:88-91`); being seen is the price (`epistemic.py:322`); no fine |
| 35 | consent as temporary state — *Shadows of Doubt*: lawful search with the occupant's permission | PARTLY · `give` is consensual; a safe-conduct is a `dispensation`; no reader on `examine` or presence until H-75's `hold:` eligibility is live |
| 36 | social-credit gate — *Shadows of Doubt*: 1 to start, 8 to retire | DOES NOT APPLY as a meter · T-a; `exposure` forbidden as an axis (`rosters.yaml:490`); standing computed (`standing_of`) |
| 37 | weighted vote — *The Republic of Rome*, *Suzerain* | PARTLY · a vote is the holder's own `commit`, the count a Query (K-07), unweighted; `Person.weight` exists and is unread there |
| 38 | bribe converted to votes — same | CARRIED composed, never converted · `give` or `transfer`, then the receiver's own `commit`; D-5 |
| 39 | budget and authority — *Suzerain*, *Crusader Kings III* | CARRIED · scenes, plus `budget_office_bonus` per live `hold`; stores by `levy` and `transfer` |
| 40 | hook — *Crusader Kings III*: a favour owed or compliance compelled | DOES NOT APPLY by ruling · D-5: no creditor verb, no `call_in`; an `oblige` is self-dischargeable |
| 41 | secret — *Crusader Kings III*: a hidden fact, discoverable, convertible by blackmail | CARRIED composed · a claim others lack (AX-2), a `cover`, a `seen` with `who` withheld; blackmail is a held Record, a `petition` and a `tell` (family 34) |
| 42 | hostage and ward — *Crusader Kings III*, Wards & Wardens | hostage STATE (`custody`), composed (K-38); ward DOES NOT APPLY · CENSUS generates nobody (H-51) |
| 43 | agenda control — *The Republic of Rome* | PARTLY · the docket, `convene`, `open_case`, `carry`, `order:`; the date↔docket join missing (H-163 limit 4) |
| 44 | shared loss condition — *The Republic of Rome* | DOES NOT APPLY — an observation for the FA and WR lanes · endings absent (H-176); GD-1's single victory (`canon/02_canon_constraints.md:71`) |
| 45 | two-body threshold — *Suzerain*: two audiences persuaded separately | SYSTEM · the arrangement key `appeal_basis` (`arrangements.yaml:93`; the two seeded rows opened here, `arbitration` and `parliamentary_debate`, set it `none`); two benches are two `determine`s; a nested `open_case` |
| 46 | advisory legislature — *Suzerain*'s Rizia | CARRIED · `parliamentary_debate` disposes a `Record` (`arrangements.yaml:103-115`), binding nobody until a seat acts |
| 47 | succession law — *Crusader Kings III* | STATE and SYSTEM · R-5 plus a rule per basis on `REVOCATION_RULES`' dispatch (`rosters.yaml:1767-1771`) — K-40 |
| 48 | forced vote — *Crusader Kings III*: spend a hook to dictate an elector | DOES NOT APPLY · D-5; `commit` is `own` |
| 49 | decree — *Suzerain*'s Rizia | PARTLY · to a person, `issue` or `dispatch`; to a place, `proclaim` deferred (K-34) |
| 50 | scheme with potential, phases and secrecy — *Crusader Kings III* | PARTLY composed · a Proposition, commits and a `cover`; phases as `Record.stages`; secrecy decay absent |
| 51 | agent roles — *Crusader Kings III*, *Hearts of Iron IV*, *Espiocracy* | CARRIED by AX-1 · every agent a Person; delegation rides `Act.via` |
| 52 | countermeasure focus — *Crusader Kings III* | CARRIED as an act · `surveil` each season; a standing focus would be a clock on a container (T-i) |
| 53 | intel level — *Hearts of Iron IV*: a percentage per target and branch | DOES NOT APPLY · T-a; the analogue is a dated `faction_sheet` and a claim's confidence |
| 54 | cryptology — *Hearts of Iron IV* | DEFERRED · no demand, no reader; `research` reads content verbatim |
| 55 | false intelligence — *Hearts of Iron IV*, La Résistance | PARTLY · `forge` THIN (H-169); the lie is G7; lossy retelling (`loop/witness.py:137-160`); detection is `record()` |
| 56 | graded operation outcome — *Espiocracy* (planned): an assassination might merely injure | CARRIED · `fight`'s Felled / Wounded / Untouched; `march`'s field bands |
| 57 | trace and counterintelligence — *Espiocracy* (planned) | PARTLY · every act witnessed by presence; `anchor_of`; turning is the agent's own `release` and a new `commit`; no trace at a place for a later reader |
| 58 | information as a held object — *Espiocracy* (planned): it has a source and can be extracted in interrogation | CARRIED; extraction GAP → closed by K-35 · a `hold` on a Record — "a held document is a held belief" (`loop/witness.py:283-305`); `chain` records the source |

### 6.3 The verbs, one by one

The 44, then the twelve additions, alphabetical within each; none is skipped. **Family** is the survey's
A–K. **Producer** names, for the six findings, the distinct shape each takes — the survey interrogation's
answer to 4.5's "claims graded by degree", one shape per verb rather than one producer for six.

| verb | family | primitives | what the survey implies | applicability | change | conflict |
|---|---|---|---|---|---|---|
| `build` | — | none | nothing | DOES NOT APPLY | none (H-166, J-4 stand) | none |
| `carry` | J | P43 | agenda control turns on who may put a matter before the room | APPLIES — the one route by which someone without a seat dockets (H-52 calls `own` docketing "a different game") | none to the row; evidence for building it on `open_case`'s body (§3.5) | none |
| `commit` | I, G | P37 (the count a Query over live commits, unweighted), P39 (a standing commit is spent attention), P50 | votes are the paradigm store; show the threshold | APPLIES | none (step 2); a weighted count would read `Person.weight` in the Query, never in a row | none |
| `comply` | F | P22 (an emission regardless of performance) | nothing | PARTLY | none (K-01) | none |
| `confer` | J | P47 (the bases are closed and nothing discriminates them, `rosters.yaml:1751-1754`), P33 | law decides inheritance; elections | PARTLY — `elected` has no count reader | the suite's term widening; R-5 later, with a rule table (K-40) | `conferral_bases` `open: false` — Jordan's |
| `construe` | C, K | P14, P55 (distortion on the receiver's side) | misreading belongs to the receiver | PARTLY — it already runs without the verb: the per-holder content deposit and lossy retelling (`loop/witness.py:137-160`) | none (ruled) | none |
| `convene` | J | P43 (when a body sits), P3 (a feast, family 44) | agenda is what and when | APPLIES | none to the row; CALENDAR's `date.fired` routed into WITNESS (H-163 limit 4) | none |
| `create_record` | D | P18 (an authored note), P16 (exact kinds), P58 (the maker's hold) | logs spare memory; slots clarify | APPLIES | none | none |
| `destroy_record` | K | P41 (a secret kept by ending its carrier), P6 | hiding is investigation reversed | APPLIES; held (H-75, H-156) | none | none |
| `determine` | E, J | P20–P23 (the scale lands here), P37 (quorum), P45, P46 (`disposes: Record`) | strict verification fixes one truth; loose verification makes judgment social | APPLIES; today's row is P23 — it reads no truth | the contested widening (§9.6): the Proposition contested is the charge (K-35), its obstacle from testimony rather than `capability/2` — the SC lane's | none — the contest is the charge, never the finding, so investigation stays uncontested |
| `dispatch` | J | P49 (a decree to a person), P51 (the named person's own choice) | a decree bypasses a body; agents decide | APPLIES | none (ruled; ED-IN-0211 open) | none |
| `establish` | J | P46 (a body that disposes a Record), P43 | institutions as thresholds | PARTLY | none (`15c`) | none |
| `evade / defy` | F, K | P27, P50 (evasion is covert refusal) | covert and open refusal cost differently | PARTLY — supports the split when built (K-24) | none now | none |
| `examine` | C | P12, P13, P14 | evidence is placed; a frozen scene rewards looking; looking is costly in *Pentiment*, free in *Obra Dinn* | APPLIES; THIN — a content-free claim (`loop/witness.py:380`), and Site-bound, so always refused in the corpus (`verb_table.yaml:1006-1015`) | **producer:** the only finding whose content is the log at a place — past Events anchored at the present Site's rung (`place_of`, `anchor_of`); the band selects which `Seen` terms deposit, on `seen_of`'s shape where the channel selects them today [ASSUMPTION], Partial withholding `who`; Failure nothing | AX-7: band- and channel-mediated, never a bare `True` |
| `exchange` | I | P38, P39 | nothing new | PARTLY (THIN, H-94) | none | none |
| `fight` | F, K | P56 ("might merely injure" is `Wounded`), P28 (`Untouched`), P24 (`Felled`) | graded outcomes beat binary ones | APPLIES exactly | none | none; *The Republic of Rome*'s "assassinate" is an outcome here (direction 3) |
| `forge` | K | P55, P16 | false intelligence needs a detector | APPLIES; THIN (H-169: a consumer first) | none | none |
| `found` | — | none | nothing | DOES NOT APPLY | none | none |
| `give` | I, B, K | P58 (a receipt deposits content, `loop/witness.py:283-305`), P38, P35 (consent: `counterparty` and `with`), P55 (a plant) | payment buys answers; information travels as objects | APPLIES | the suite's Rung widening | none |
| `interview` | B | P9, P10; P7 and P8 do not apply | approach beats classification; generic prompts scale; *L.A. Noire*'s model is fragile | APPLIES | **producer: a prompt (K-36)** — the content lives in another's ledger, which the fold may not read (`verb_table.yaml:1048`): it emits, the questioned person witnesses it by presence, Q2 raises their question, and they answer by their own `tell` from what they hold; no degree on the asker. Bind a counterparty so the subject is present and self-interview closes [the author's alternative, kept beside it: `counterparty: subject`, as `detain` and `interrogate` declare, closes self-interview through the fold's existing counterparty clause without moving the questioned person to `to`]; approach as payload data | self-interview admitted today (`:1048`); a counterparty closes it |
| `issue` | J, I | P49, P35 (a safe-conduct), P42 (a warrant naming one's own hostage) | a decree is the ruler's direct instrument | APPLIES | none beyond §10.1 | none |
| `levy` | J, I | P39 | a budget makes promises cost | APPLIES | none | none |
| `march` | — | P56 (the field bands), P24 | graded outcomes | PARTLY | none beyond the arrival | none |
| `migrate` | H | P36 read as T-b (capacity changes what can be chosen) | gates price access | PARTLY | none | none |
| `move` | A, H | P1 (a visit costs a scene and a leg), P34 | visiting costs; trespass is priced | APPLIES for P1; GAP for P34 — no lock, no fine | none — trespass is priced by reception (§6.4); a hostage's handing-over (K-38) | none |
| `oblige` | I | P40 (the owed thing, self-dischargeable), P39, P42 (a hostage's own surety) | hooks are the hinge of intrigue | PARTLY — the obligation exists; the lever may not (D-5) | none (reader `purview_reaches`, H-101) | P40 and P48 against D-5 — ruled; the survey's pattern does not apply |
| `open_case` | J, E | P43, P8, P47 (a succession dispute as a case) | agenda; succession as a case | APPLIES | none to the row; the charge needs a carrier (K-35) | none |
| `petition` | B, E, I | P8 (not evidence-gated, `verb_table.yaml:710-717`), P22, P23 at filing, P41 (a demand) | evidence-gated accusation is the most legible confrontation | APPLIES | no precondition on the row — kinds as data would gate every petition (K-11); the charge (K-35) makes the accuser's own `commit` the oath | none |
| `reconstruct` | D, E | P16, P17, P14, P5 (the `View` cap bounds what is synthesized) | boards externalize reasoning; they fail when the rules ignore links | APPLIES; THIN; a self-feeding loop | **producer: waits (K-37)** — the one finding with no world read; canon's obstacle needs a scope a GM chooses (`verb_table.yaml:1113`); an obstacle without one (own claims about the subject against a per-`knowledge_kind` fixture) would be an invented number and is not adopted; Failure's wrong value needs a value space nothing supplies | AX-3: its output stays held-true and may never move `pursuits` |
| `release` | F, I | P24 inverted (AX-6: every bond closable), P40 abandoned | irreversibility gives weight | APPLIES — here weight is authored reversibility | none (+ R-3's fold) | none |
| `repudiate` | F | P24 | nothing distinct | DOES NOT APPLY distinctly | the cut stands (R-3) | none |
| `research` | C, A | P11, P18, P58; P54 in its NOT list | archives are free; the cost is interpretation | APPLIES | **producer:** a Record's `subject_matter`, read without holding it — Success deposits the content verbatim, as a holder's deposit does; Partial reuses `_told_value`'s drift (`loop/witness.py:137-160`); Failure nothing. The cheapest of the six: both readers exist | none |
| `restore` | — | none | nothing | DOES NOT APPLY | none | none |
| `revoke` | J | P47 (deposition); P48 does not apply | nothing new | PARTLY | none (R-4) | none |
| `speak` | B, G | P26 (speech that changes nothing), P57 (witnessed by presence) | expression without outcome reads as empty | PARTLY — not empty: it seeds `tell` | none | none |
| `succeed` | G, J | P33, P47 | the dynasty as continuing identity; law decides; succession as a case | APPLIES; a carrier nobody reads (`verb_table.yaml:839`) | R-5's basis with a rule table (K-40); the heir by the known-person fan; a contested designation composed on `utter`, `commit` and `open_case` | `conferral_bases` closed — Jordan's (R-5) |
| `surveil` | C, K | P52, P57, P6, P12 | counter-espionage is investigation of the one hiding | APPLIES | **producer:** the only finding over time at a place — the log's Events at the watched Rung across the season, which the actor need not have witnessed (against `examine`'s present Site); degree as `examine`; canon's Exposure +2 has no carrier and is §8.1's Query | the Person case held (K-16); canon's Exposure meter against T-a, resolved as a Query |
| `survey` | C, D | P13 (resolved at writing, frozen), P53 (as a dated sheet, not a percentage), P58 | frozen records; intel levels | APPLIES for P13; P53 does not apply (T-a) | the suite's Rung widening | none |
| `tell` | B, K, I | P9 (the teller's manner is nowhere), P55 (the lie: G7), P10 (showing is telling what one holds), P25 (the chain is the remembered source); P15 does not apply | conversation feeds the store; approach over classification | APPLIES | none (the telling workplan's G3, G6, G7) | none |
| `thread_read` | C, G | P29, P14 | a background unlocks readings | APPLIES exactly — P-08 (`canon/02_canon_constraints.md:50`) is P29 made metaphysical | **producer: waits** on H-85 (plan 27/29f) | P-08 forbids study — `train` excluded (K-20) |
| `tie / knot` | I | P41 (a knot partner witnesses), P42 weakly | bonds store obligation | PARTLY | none (H-182) | none |
| `transfer` | I | P38 (open, priced, witnessed), P39 | a bribe turned into votes, as an open act | PARTLY — priced, never converted | none | P38's conversion against D-5 |
| `utter` | J, I | P43 (a motion is what is proposed), P50, P37, P47 and Recommendation 4 (a claim or a charge as a Proposition) | propose; declare | APPLIES | step 2 (mint the hold); the charge (K-35) | none |
| `work` | — | none | nothing | DOES NOT APPLY | none (K-09) | none |
| `argue` | B, G | P31 (chance in speech), P30 | voices and checks make speech consequential | APPLIES; its `Person.pursuits` write is AX-3's "argument … move[s] what is held right" made mechanical (`01_AXIOMS.md:126-127`) | none | none |
| `conceal` | K | P41, P50 (secrecy), P57 (cover) | hide what the investigator seeks | APPLIES exactly | none | none |
| `covenant` | I, J | P39, P42 (a hostage clause) | treaties as stores | APPLIES | a hostage composes on `move`, `issue`, `detain` and `pardon` (K-38), closing §8.1's `[GAP]` | none |
| `detain` | H, I | P34 (announcing an arrest, *Shadows of Doubt*), P42 (custody as hostage) | an arrest ends or escalates a case | APPLIES | none; the hostage by composition | its prize [CONFIDENCE: medium] stands as §9.1 says |
| `interrogate` | B, E, K | P9, P58 (extraction), P27 | approach, not classification; extraction yields a held object | APPLIES | `confession.made`'s claim value is the charge's id (K-35); approach as payload data; a failure closes no line | none |
| `pardon` | J | P24 (authored reversibility) | — | APPLIES | none | none |
| `raze` | — | none | — | DOES NOT APPLY | none | none |
| `sabotage` | K | P57 (a witnessed act) | — | PARTLY | none | none |
| `seize` | H, K | P58, P12 | the hider's document is the finder's prize | APPLIES under a warrant or occupation | none | theft without licence is the gap → `steal` |
| `steal` | H, K | P34 (the Entering family's verbs include *steal*), P58, Finding 3's covert half | access at the risk of a fine; information as a held object the finder can take | APPLIES | new (§9.3, R-8) | the survey's fine has no carrier; the price is reception and what other people do next |
| `tend` | — | P28 (recovery from a soft failure) | soft failure needs recovery | APPLIES | none | none |
| `train` | G | P29, P32 | the self as instrument | APPLIES | none | P-08's exclusion stands (K-20) |
| `determine` (widened) | E | the verification policy's bench | — | APPLIES | obstacle from testimony — an SC-lane observation (§9.6) | none |
| `confer` (+ term), `give` (+ Rung), `survey` (+ Rung), `march` (arrival), `oblige` (reader) | — | — | — | unchanged by the survey | — | — |

### 6.4 What the suite does not already carry, and where the survey disagrees

**The survey's primitives not marked CARRIED in §6.2, classed.**

| class | primitives — carrier, or why |
|---|---|
| COVERED, composed or computed; no change | P3 (`convene`, `move` and presence); P16 (the claim's shape); P19 (ambitions; `argue` writes `pursuits`); P29 (`refuses()`; `knowledge_kinds`, H-85); P32 (`conceal`; a creed `commit`); P36 (standing with an institution, computed by `standing_of`; `church_standing` has no producer); P37 (the Query; a weight would be read there); P41; P50 (§8.1's Scheme; secrecy decay absent); P55 (`forge`, G7, `_told_value`) |
| WIDENED | P9 — approach as payload data on `interview` and `interrogate`; P35 — `hold:<dispensation naming the place>` on `examine` and `research` once H-75's `hold:` eligibility is live, the instrument being `issue`; P43 — `carry` built (§3.5) |
| STATE | P8 and Recommendation 4 — the charge, a `HOLDS` Proposition (K-35); P42 — the hostage, `custody` by composition (K-38); P47 and P33 — R-5's basis and its rule table (K-40) |
| SYSTEM | P12, P57 — a trace read later at a place (4.5's producer for `examine` and `surveil`); P14 — `why` has no reader; P23 — the contested bench closes it; P34 — trespass priced by reception: being seen, then a `petition` or a warrant, never a fine; P43's date↔docket join (H-163 limit 4); P45 — `appeal_basis`, two benches as two `determine`s, a nested `open_case` |
| GAP → a new verb | theft — the Entering family's *steal*, three extraction rows and family 30's [C-08] → `steal` (R-8). P58's extraction closes by K-35, with no verb |
| DEFERRED | P54 (cryptology); P49's decree to a place (`proclaim`, K-34) |
| DOES NOT APPLY | P4, P7, P11, P15, P17, P20, P21, P25, P26, P27, P30, P40, P42's ward, P44 (an observation for the FA and WR lanes), P48, P53 — reasons in §6.2 |

**The survey against the games extraction pass, or against itself.**

| # | the survey says | the other source | disposition |
|---|---|---|---|
| 1 | *Shadows of Doubt* accepts a judgment "whether or not it is right" (Finding 1; P22) | its own Part 1: optional form entries "earn extra credit when correct"; handing in the form "raises social credit if correct"; extraction G1-89: "right or wrong answer [consequence UNVERIFIED]" | internally inconsistent: the form is graded at submission [CONFIDENCE: medium — neither source verified a wrong name's consequence]; Appendix D (s) |
| 2 | *Shadows of Doubt*: early access 24 April 2023 | the extraction pass gives that date and a full release on 26 September 2024 | an omission, not an error; both carried (§2) |
| 3 | *Esoteric Ebb*'s conflict is "resolved by dialogue and skill checks rather than combat" | G1-41, a store-page fetch: turn-based encounters, "violence as a last resort" | a conflict; nothing here rests on either reading |
| 4 | P27, a line closed on error, is *L.A. Noire*'s | G1-22: *Disco Elysium*'s failed press locks options (snippet) | the survey under-attributes |
| 5 | *Pentiment* attaches no truth value to its accusation (P23) | G1-10: proof gathered widens what can be argued; good conduct gives another chance to sway the Archdeacon | a refinement: evidence-gated input with unverified output — P8 and P23 at once |
| 6 | *Crusader Kings III* 1.19 "Scribe" (April 2026) | the extraction pass confirms only 1.13 "Basileus" (September 2024) | [UNVERIFIED] here |
| 7 | *Espiocracy*'s mechanics; *L.A. Noire*'s 236 / 56 / 106 / 74 question counts; *Suzerain*'s two-thirds Assembly and Supreme Court; *The Republic of Rome*'s designers | no extraction coverage | carried as the survey states them, under its own evidence paragraph |
| 8 | no *Romance of the Three Kingdoms* at all | the extraction pass's 40 RTK rows, used by families 24, 37, 39, 52 and 54 | an omission; nothing in §6.3 rests on RTK |

**The survey's patterns against standing rulings and axioms.**

| the survey's pattern | ruling or axiom | resolution (§0 filter step) |
|---|---|---|
| Recommendation 2's approach verbs | six-as-six and "No new action vocabulary" (`verb_table.yaml:950-960`); ED-FI-0004 (`:1054`) | approach as data (§6.1) — step 4, `mood`'s precedent |
| P40 hook, P48 forced vote, P38's bribe turned into votes | D-5 (`verb_table.yaml:757`); T-g | do not apply — step 1 |
| P36 social credit, P53 intel level, canon's Exposure meter | T-a (`01_AXIOMS.md:327-354`); `exposure` forbidden as an axis (`rosters.yaml:490`) | computed Queries — step 3 |
| P20 per-item grading, P21 batch confirmation, P25 notices | AX-7 (`01_AXIOMS.md:263-317`), including "No state is hidden from the player" (`:299-304`) | do not apply — step 3 |
| Finding 4's timers | AX-5; T-c; T-i | a term an act wound, never a clock — step 3 |
| P44 shared loss | GD-1's single victory (`canon/02_canon_constraints.md:71`); endings absent (H-176) | an observation for the FA and WR lanes |

---

## 7. The resolved suite

### 7.1 The roster

One row per verb: the 44 (alphabetical), then the twelve new (alphabetical). Scale is the table's
`scale`; "—" is a declared absence. The structural fields of the 44 were read off the live
`VERB_TABLE` by import (2026-10-04) and agree with the audit pass's roster except in `fight`'s
counterparty (§14.5, item 16); the group column uses §3.2's codes. Degree bands: `sigma_leverage` prizes use Overwhelming / Success / Partial / Failure; `a field`
uses Declared / Won / Lost / Unopposed (`field_degree_bands`, `rosters.yaml:801-817`).

| verb | status | stratum | scale | eligibility | benef. | counterparty | prize | writes | states | grp | axis vs nearest |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `build` | retained | uncontested_material | person | own | none | — | none | `Site.exists` | — | G9 | vs `found`: a Site |
| `carry` | retained (THIN) | social | person | own | none | — | none | `DocketItem.matter` | accusation pending | G4 | vs `open_case`: own, a held petition |
| `commit` | retained | social | person | own | actor | — | none | `Tenure.since` (commit) | membership, recognition, a vote, a covenant's acceptance, war (backing a `WAR` Proposition) | G7 | vs `oblige`: the object is a Proposition |
| `comply` | retained (ruled) | social | person | own | none | — | none | `[]` | — | G5 | vs `transfer`: an emission on a held writ |
| `confer` | **widened** | binding_decision | settlement | remit:confer | subject | — | none | `Tenure.until`, `Tenure.since` (hold; + `Tenure.term`) | regency | G7 | vs `establish`: fills a seat |
| `construe` | retained (ruled) | social | person | own | actor | — | none | `[]` | — | G5 | vs `comply`: one's own reading |
| `convene` | retained | binding_decision | person | remit:convene | none | — | none | `Date.due_at`, `ConveningCondition.attached` | a sitting | G4 | vs `open_case`: a date, not a matter |
| `create_record` | retained | uncontested_material | person | own | none | — | none | `Record.exists`, `Record.stages` | — | G6 | vs `issue`: own, any kind |
| `destroy_record` | retained | uncontested_material | person | hold:\<record\> \| presence | actor | — | none | `Record.exists` | ends a `cover` Record | G6 | vs `seize`: ends, does not move |
| `determine` | **widened** | binding_decision | settlement | remit:determine | none | subject | **a proposition** | by band: `Tenure.since` (+ `Tenure.degree`), `DocketItem.matter` | sentence (`oblige` \| `custody` \| `ban`), excommunication, outlawry | G4 | vs `pardon`: opens |
| `dispatch` | retained (ruled) | binding_decision | territory | remit:dispatch | none | — | none | `[]` | — | G5 | vs `issue`: no document |
| `establish` | retained | binding_decision | settlement | remit:confer | none | — | none | `Office.exists`, `Office.remit_acts`, `Tenure.payload` | — | G7 | vs `confer`: the seat itself |
| `evade / defy` | retained (ruled) | social | person | own | actor | — | none | `[]` | — | G5 | vs `comply`: withholds |
| `examine` | retained | contested_physical | person | own \| presence:\<site\> | actor | — | none | `[]` | — | G11 | a Site |
| `exchange` | retained (THIN) | uncontested_material | settlement | own | none | — | none | `Rung.stores` (both sides) | — | G8 | vs `transfer`: two-sided (H-94) |
| `fight` | retained | contested_physical | person | own | actor | — (the subject is the second claimant) | the body | by band: `Person.body`, `Person.exists`, `Person.scar`, `Tenure.until` | — | G1 | vs `detain`: the body |
| `forge` | retained (THIN) | uncontested_material | person | own | actor | — | none | `Record.exists`, `Record.forgery_quality` | — | G6 | vs `create_record`: falsified |
| `found` | retained | uncontested_material | person | own | none | — | none | `Rung.exists`, `Tenure.since` (contain) | — | G9 | vs `build`: a Rung |
| `give` | **widened** | social | person | own \| hold:\<record\> | to | to | none | `Tenure.until`, `Tenure.since` (hold; + on a Rung) | cession | G6 | vs `seize`: consensual |
| `interview` | retained | social | person | own | actor | — | none | `[]` | — | G11 | vs `interrogate`: own, no custody |
| `issue` | retained | binding_decision | province | remit:issue | none | to | none | `Record.exists` (dispensation: a warrant, summons or charter by its `terms`) | warrant | G6 | vs `dispatch`: a document |
| `levy` | retained | uncontested_material | settlement | remit:issue \| presence:\<rung\> | actor | — | none | `Rung.stores` | — | G8 | vs `transfer`: taken by remit |
| `march` | **widened** (the army arrives; R-2 resolved) | contested_physical | settlement | remit:dispatch | actor | — | a field @ENCOUNTER | by band: Won/Lost `Person.body`, `Person.stance` (the losing side); Won/Unopposed `Tenure.until`, `Tenure.since` (contain), `Person.travel_leg` (the arriving side) | occupation and siege (a Query) | G2 | vs `move`: an army, through a seat |
| `migrate` | retained | movement | person | own | actor | — | none | `Person.travel_leg`, `Tenure.until/since` (contain, reside) | — | G10 | vs `move`: reside |
| `move` | retained | movement | person | own | actor | — | none | `Person.travel_leg`, `Tenure.until/since` (contain) | — | G10 | vs `migrate`: presence only |
| `oblige` | **widened (reader)** | social | person | own | actor | subject | none | `Tenure.since`, `Tenure.term` (oblige) | vassalage | G7 | vs `commit`: a seat, with a term |
| `open_case` | retained | social | person | remit:determine | none | — | none | `Record.exists`, `Record.stages`, `DocketItem.matter` | accusation pending | G4 | vs `carry`: by remit |
| `petition` | retained | social | person | own | actor | to | none | `Record.exists` (petition: an accusation, demand or challenge by its `terms`) | accusation pending | G6 | vs `issue`: upward |
| `reconstruct` | retained | uncontested_material | person | own | actor | — | none | `[]` | — | G11 | vs `research`: own ledger |
| `release` | retained | binding_decision | person | own | subject | — | none | `Tenure.until` (hold, commit, oblige, succeed, tie, knot) | ends fealty, a service sentence, membership, a war (its commits) | G7 | vs `pardon`: one's own edge |
| `repudiate` | **cut (recommended, R-3)** | social | person | own | actor | — | none | `Tenure.until` (commit) | — | G7 | vs `release`: none |
| `research` | retained | uncontested_material | person | own \| presence:\<site\> | actor | — | none | `[]` | — | G11 | vs `examine`: a Record |
| `restore` | retained | uncontested_material | person | own \| presence:\<site\> | none | — | none | `Site.condition` (+) | — | G9 | vs `work`: no floor |
| `revoke` | retained | binding_decision | settlement | remit:revoke | none | — | none | `Tenure.until` (hold on a seat) | — | G7 | vs `pardon`: a seat's hold |
| `speak` | retained (THIN) | social | person | own | none | — | none | `[]` | — | G12 | vs `tell`: no hearer, no prize |
| `succeed` | retained (THIN, R-5) | binding_decision | person | own | subject | — | none | `Tenure.since` (succeed) | — | G7 | vs `confer`: an heir |
| `surveil` | retained (Person case deferred) | contested_physical | person | own \| presence:\<rung\> | actor | — | none | `[]` | — | G11 | vs `examine`: a Rung over time |
| `survey` | **widened** | uncontested_material | person | own | actor | — | none | `Record.exists` (faction_sheet; + a Rung's holding faction) | — | G6 | vs `create_record`: resolved content |
| `tell` | retained (lie deferred) | social | person | own | subject | to | a standing | `[]` at every band | — | G3 | vs `argue`: any topic |
| `thread_read` | retained (deferred) | contested_physical | person | own \| presence:\<site\> | actor | — | none | `[]` | — | G11 | TS-gated |
| `tie / knot` | retained (split when built) | social | person | own | actor | — | none | `Tenure.since` (tie \| knot) | a bond | G7 | vs `oblige`: person to person |
| `transfer` | retained | uncontested_material | person | own \| hold:\<store\> | to | — | none | `Rung.stores`, `Tenure.term` | renews fealty; tribute | G8 | vs `levy`: own stores |
| `utter` | retained | social | person | own | none | — | none | `Proposition.exists` | war (a `WAR`-mood Proposition) | G12 | vs `speak`: writes a Proposition |
| `work` | retained (delta ≥ 0) | uncontested_material | person | own \| presence:\<site\> | none | — | none | `Site.condition` (+; a floor; a works) | — | G9 | vs `restore`: floor + works |
| `argue` | **new** | social | person | own | actor | to | a proposition | Overwhelming/Success: `Person.pursuits`; else `[]` | — | G3 | vs `tell`: a Proposition, and a write |
| `conceal` | **new** | social | person | own | actor | — | none | `Record.exists` (cover) | concealed identity | G6 | vs `forge`: about oneself |
| `covenant` | **new** | social | settlement | remit:issue | to | to | none | `Record.exists` (treaty \| alliance), `Record.stages` | treaty, alliance | G14 | vs `petition`: a seat, across |
| `detain` | **new** | contested_physical | person | remit:dispatch | none | subject | a standing [CONFIDENCE: medium] | Overwhelming/Success: `Tenure.since` (custody); else `[]` | custody, hostage | G13 | vs `fight`: prize, write |
| `interrogate` | **new** | social | person | remit:determine | actor | subject | a proposition | `[]` at every band | — (a `confession` proof) | G13 | vs `interview`: remit, custody |
| `pardon` | **new** | binding_decision | settlement | remit:determine | subject | — | none | `Tenure.until` (custody \| ban) | ends custody, a ban | G13 | vs `release`: another's edge, via the seat |
| `raze` | **new** | contested_physical | settlement | remit:dispatch | none | — | none | `Site.exists` / `Rung.exists` → absent | ends a place where the seat's faction is mustered | G9 | vs `sabotage`: existence |
| `sabotage` | **new** | uncontested_material | person | own \| presence:\<site\> | actor | — | none | `Site.condition` (−) | — | G9 | vs `restore`, `work`: sign, beneficiary |
| `seize` | **new** | uncontested_material | settlement | remit:issue | none | — | none | `Tenure.until`, `Tenure.since` (hold on a Record under a warrant; on a Rung under occupation) | ends another's hold; conquest of an occupied place | G13 | vs `give`: no consent |
| `steal` | **new** (R-8) | uncontested_material | person | own | actor | — | none | `Tenure.until`, `Tenure.since` (hold on a Record another holds) | ends another's hold | G6 | vs `seize`: no licence |
| `tend` | **new** | uncontested_material | person | own | subject | — | none | `Person.body` (+) | — | G15 | vs `restore`: a Person |
| `train` | **new** | uncontested_material | person | own | subject | — | none | `Person.capability` (un-retired) | — | G15 | vs `tend`: capability |

**Counts (recounted from the table by script, revision 4).** 56 rows: the 44 and 12 new. **The suite is
55 verbs** — the 44, less the recommended cut of `repudiate`, plus 12 (`steal` carried on R-8's
recommendation; under R-8 (b) the suite is 54). Of the 43 retained: 36 unchanged (four of them —
`comply`, `construe`, `dispatch`, `evade / defy` — kept by ruling), 1 narrowed (`work`, delta ≥ 0) and 6
widened (`confer`, `determine`, `give`, `march`, `oblige` by a new reader only, `survey`). Contested rows:
7 of 55 (`argue`, `detain`, `determine`, `fight`, `interrogate`, `march`, `tell`); `steal` is uncontested.
Across the suite, 38 of 55 rows admit `own` (29 of them `own` alone). New verbs by eligibility: `own` 6
(`argue`, `conceal`, `sabotage` — `own` | `presence:<site>` — `steal`, `tend`, `train`);
`remit:dispatch` 2 (`detain`, `raze`); `remit:determine` 2 (`interrogate`, `pardon`); `remit:issue` 2
(`covenant`, `seize`) — every
remit act already on the roster (`rosters.yaml:302`), so no `remit_acts` value is added and H-52's
warning (`:298-301`) is not engaged. Not in the suite: `execute` (§9.8, R-1); `besiege`, folded into
`march` (K-28); `proclaim`, deferred with its readers (K-34). `seize`'s Rung object is part of the new
verb's own reach, not a widening of an existing row.

### 7.2 REACH and NOT of the changed verbs

- **`determine`** (widened) — disposes any kind the exercised seat's arrangement `disposes:` (`oblige`,
  `custody`, `ban`), by band, on a docketed person in the bench's ground; the Proposition it contests is
  the charge (K-35). NOT: lift a disposal (`pardon` for `custody`/`ban`; the party's own `release` for an
  `oblige`); grade a finding (investigation stays uncontested — the contest is the charge).
- **`confer`** (widened) — a seat-hold carrying a `term` (regency, a term-limited seat). NOT: an heir
  (`succeed`); a seat under a seat (H-101's reader).
- **`give`** (widened) — a held Record or a held Rung `to` a known present person. NOT: a seat
  (`confer`); stores (`transfer`).
- **`survey`** (widened) — a faction, a person under one, or a Rung's holding faction. NOT: a census of
  persons.
- **`oblige`** (widened by a reader only) — the row is unchanged; a seat-holder's `oblige` to another seat
  is read as subordination by `purview_reaches` (H-101). Expulsion is the seat withholding renewal so the
  term matures at MATTER. NOT: a remit; a vote.
- **`commit`** (unchanged row) — a motion's or a covenant's Proposition reaches it through `utter`'s hold
  or the enabler. NOT: a vote through a remit — a vote is the holder's own `commit`, the count a Query
  over bench members' live commits (K-07).
- **`march`** (widened) — send the mustered army to a settlement; the stake is read at the destination
  (capture attempt, interception or defence, relocation, arrival at unheld land, §9.6); writes the losing
  side's casualties and grudge and, on a won or unopposed field, the arriving army's presence. NOT: title
  (`seize`, `give`, `release`, death); muster (`sides_of`); a larder effect (deferred reader, §10.4); a war
  declaration (`utter`).
- **`detain`** — a Person named in a held warrant; opens `custody` to the seat that issued the warrant.
  NOT: harm (`fight`); release (`pardon`).
- **`interrogate`** — a Person in custody; the charge's disposition as `confession.made`, whose
  deposited claim's value is the charge Proposition's id (K-35), or `confession.withheld`. NOT: a finding
  (the six); a reading of the prisoner (no row classifies one, §6.1); a lost line (a refusal emits and
  the act may be chosen again).
- **`seize`** — a Record named in a held warrant, or (from build step 8) a settlement where the exercised
  seat's faction is mustered and the holder's is not; whatever `hold` it carries closes and the actor's
  opens under the `seizure` basis. NOT: stores (`levy`); a seat; a place the seat has no army at;
  a Record taken with no licence (`steal`).
- **`steal`** (R-8) — a Record another person holds, where its holder stands where the actor stands; the
  holder's `hold` closes and the actor's opens under the `theft` basis. NOT: consent (`give`); a warrant or
  occupation (`seize`); ending it (`destroy_record`); stores (`levy`, `transfer`); a seat (a `hold` on an
  Office is `conferral`'s and `T-o`'s alone); a person (`detain`).
- **`pardon`** — a live `custody` or `ban` whose object is the exercised seat. NOT: an `oblige` (D-5,
  `verb_table.yaml:757`).
- **`covenant`** — a `treaty` or `alliance` Record `to` another seat's holder about an uttered
  Proposition; in force by both holders' `commit`s. NOT: a private debt (deferred); a truce (deferred,
  K-32).
- **`raze`** — end a Site or Rung at a settlement where the exercised seat's faction is `mustered`. NOT:
  lower condition (`sabotage`); any place the seat has no army at.
- **`conceal`** — a `cover` Record on oneself; `anchor_of` answers its id. NOT: a false document
  (`forge`).
- **`sabotage`** — lower a present Site's condition by `_rise`'s mirror. NOT: end it (`raze`).
- **`argue`** — contest a Proposition with a present hearer; a win moves the hearer's pursuits. NOT:
  inform (`tell`).
- **`tend`** — raise a present Person's body. NOT: a Site (`restore`).
- **`train`** — raise one capability on self or a present pupil. NOT: Thread Sensitivity (H-85, P-08).

---

## 8. States

Every state below is an **output**: the choices that set them are `utter`, `commit`, `covenant`,
`march`, `move`, `determine`, `detain`, `conceal`, `issue`, `petition`, `confer` and `oblige`, and nothing
names a state as a verb.

**Carrier rules the code already enforces.** An instrument is a `Record` of a rostered kind with
**exact** keys — `Record.__post_init__` refuses an unlisted kind and a key set that differs in either
direction (`engine/season/state/carriers.py:699-721`). A Record kind may never also be a tenure kind; the
loader refuses the overlap where the two rosters meet (`engine/season/data/rosters.py:469-476`). A
standing between a person and a seat is a `Tenure`. `tenure_kinds` is `open: true` (`rosters.yaml:101-115`).
**A new tenure kind needs a closer, not an opener:** it must sit in `release`'s declared domain or be
excluded by `RELEASABLE_KINDS` (`data/rosters.py:453`), and the loader fails the load when the two
disagree (`data/verbs.py:779-786`); a kind no act opens is only REPORTED (`:766`, `:831-840`). The parties
to a state are whoever its carrier names — seat-holders for an instrument between seats; a single person
for `custody`, a `ban` or a `cover`. "Reader" names code; **a kind ships only with its reader** — a state
no code reads is §0.05's dead carrier.

### 8.1 The state table

| state | carrier | parties | writers | readers | duration · drama | status |
|---|---|---|---|---|---|---|
| **War** | a `WAR`-mood Proposition whose `subject` and `value` are the two factions, plus live `commit`s to it — already built (`queries/faction_q.py:208-250`; `01_AXIOMS.md:1374-1384`: *"NEVER a stored flag"*) | the utterer and every committed person | `utter`, `commit`; ended by `release` of the commits (peace is `until`, T-m) | `faction_q.at_war` (and whatever `score` makes of it); it gates no verb — a march into an enemy-held settlement needs no war (K-29) | until the last commit is released · a war that outlives its supporters | COVERED — carrier and reader built; a computed declaration waits on build step 2 (`commit` formable on a Proposition) and on a source for `mood`, a payload key a computed act never carries, so a computed `utter` mints `OUGHT` (`loop/effects_information.py:467`; `decision/choose.py:358-369`) [GAP, the charge's too — §14.10] |
| **Truce** | — | two seats | — | none: its only proposed reader was a `march` refusal or flag, which direction 8 forbids and the fold cannot express (emits are keyed per band, `hole_register.yaml:3309-3313`) | — | DEFERRED with its reader (K-32) |
| **Treaty / peace** | Record `treaty` [terms, to, at] + both holders' `commit` to its Proposition | two or more seats | `covenant`, `commit`; it ends a war only through the parties' own `release` of the war's commits | `_renewals` (tribute as upkeep) | term or breach · lapsed tribute breaks a peace | GAP |
| **Alliance** | Record `alliance` [terms, to, at] + both holders' `commit` | seats | `covenant`, `commit` | `world_q.mustered` (allies' persons present at a march's destination join the holder's side — interception by an ally) | term or breach · an ally's war pulls you in | GAP |
| **Vassalage / fealty** | seat A's holder's own `oblige` to seat B; term renewed by `transfer` upkeep (`verb_table.yaml:1149`) | the two seats' holders | `oblige`; ended by `release` (*diffidatio*) or lapse | `state/gate.py::purview_reaches` (H-101: "nothing can be under anything", `hole_register.yaml:1961`) | the term · unpaid fealty lapses and the ladder breaks | GAP (the reader) |
| **Hostage** | a `custody` edge, composed (K-38): the hostage `move`s to the receiving seat — the handing-over is his own act; that seat's holder `issue`s a warrant whose `terms` names him (the cell's `authority` conjunct asks only that the seat's purview reach where the executor `to` lives, `verb_table.yaml:423-427`, so the warrant does not depend on the move — §14.9); `detain` opens `custody` to that seat; `pardon` ends it on performance of the covenant | the hostage; the giving and receiving seats | `move`, `issue`, `detain`; ended by `pardon` | `move`/`migrate` refuse, as for any custody; `sides_of` excludes him | the covenant's term · breach costs a life or a release | COVERED (composed) — no new carrier and no covenant-as-warrant basis; the `warrant` basis is unchanged |
| **Siege / blockade** | none — a Query: some faction other than the holder's `mustered` at a settlement it does not hold (`world_q.py:980-996` against `:1165-1189`), over `contain` edges each person owns | the occupying seat; the holder | `march` (Won, Unopposed); ended by the army marching on or dying | `raze` and `seize`'s occupation licence (both built with it, steps 8 and 11); a larder effect has no reader — only cohorts eat (`world_q.py:559-572`), and a cohort holds no `commit`, so never musters (`harness/populated.py:386-398`) | while the army stands · a town sat before | WIDENED (`march`, step 8); the subsistence reader DEFERRED as a new hole (§10.4) |
| **Excommunication** | Tenure `ban` (person → a Church seat), opened by `determine` under a Church arrangement with `disposes: ban` | the banned person; the Church seat | `determine`; ended by `pardon` | `_req_oblige` / `may_fill` (a banned person cannot serve or be seated); `_ch_chronicle` broadcasts the `tenure.opened` (`engine/season/epistemic.py:553-554`); deposits the `church_standing` claim nothing produces today (`rosters.yaml:576`) | until pardon · clients' commits waver | GAP |
| **Outlawry** | a person: Tenure `ban` to the realm's seat. An organization: a `condemnation` of its Proposition — deferred, no reader | the outlaw; the realm's seat | `determine`; ended by `pardon` | proposed: `detain` gains an `own` alternative against a `ban` holder, its custody's object the banning seat — a second gate clause, unbuilt | until pardon · anyone may seize him | GAP |
| **Custody** | Tenure `custody` (prisoner → the seat that issued the warrant) | the prisoner; that seat | `detain` (and a second `detain` under a second bench's warrant — "relax to the secular arm"); ended by `pardon` | `move`/`migrate` refuse; `sides_of` excludes; a `budget` floor | until released · a prisoner's faction petitions, ransoms or marches | GAP |
| **Sentence in force** | the disposal's **kind** — `oblige` (service), `custody`, `ban` — chosen by the arrangement's `disposes:` | convict; bench | `determine` | every reader of `oblige` sees a job today (H-173, `hole_register.yaml:3740`); `custody` and `ban` have their own readers | by kind · a sentence that reads as a sentence | GAP (H-173 stays open for the service kind) |
| **Concealed identity** | Record `cover` [terms] — `terms` = the agent; the Record's own id is the alias | the agent | `conceal`; ended by `destroy_record` | `state/attribution.py::anchor_of` (tier 1 answers the cover's id for an actor holding a live `cover`) | until destroyed · a Riskbreaker's act lands on a false name | GAP — ships with the `anchor_of` read (step 10) |
| **Charge** | a `HOLDS`-mood Proposition whose `subject` is the accused (`Proposition(pid, mood, subject, predicate, value)`, `loop/effects_information.py:467-468`), uttered by the accuser — no new carrier (K-35) | the accuser; the accused; every witness or endorser who commits to it | `utter`; named by the accusation `petition`'s `terms` through the enabler (§10.1); `commit` (testimony, endorsement — an oath is an utterance, `01_AXIOMS.md:1399-1403`) | `interrogate` (`confession.made`'s claim value is its id); the contested bench's obstacle, proposed — live commits to the charge, an SC-lane observation (ED-SC-0033 cl. 3, `rosters.yaml:1138-1148`); a Query over those commits | immutable; testimony until released · a charge that outlives its witnesses | COVERED (composed). The docket stays person-keyed: `open_case` dockets the accused, and `interrogate` and the contested `determine` read the charge at the effect as the `HOLDS` Proposition the docketed petition names, whose `subject` is the party [ASSUMPTION: an effect-side read, since the grammar cannot join two hops]. [GAP: a computed `utter` can name the accused — the referent rides `subject` — but cannot set `HOLDS`; it mints `OUGHT`, which `ambitions` would read as a standing need (`queries/world_q.py:1311, :1342`). Hand-built acts declare it.] |
| **Accusation pending** | `petition` whose `terms` names the charge (or, with none uttered, the accused) + `DocketItem.matter` (the accused) | accuser; accused; bench | `petition`; docketed by `open_case` or `carry` | the docket (exists) | until determined · a denunciation enters the docket | COVERED |
| **Warrant** | `dispensation` whose `terms` is a Person or a Record | issuer; executor; the named person | `issue` | `detain` and `seize` through the enabler | until used or destroyed · the hand that holds it can act | COVERED (needs §10.1's separation of `terms` from addressee) |
| **Exposure** | no field — `exposure` is forbidden as an axis name (`rosters.yaml:490`); a Query over others' `seen` claims naming the agent | agent; observers | no act writes it | the Query | rising with conspicuous acts · detection debt | COVERED (as a Query) |
| **Regency / delegation** | a `hold` carrying `Tenure.term` (widened `confer`); delegation already rides `Act.via` (`state/carriers.py:543-550`) | regent; the seat | `confer` | the gate's seat check (`loop/resolve.py:114-118`) | the term · a puppet ruler | COVERED |
| **Faction membership / recognition** | `commit` to a Proposition | member | `commit`, `release` | `sides_of`, `faction_q` | standing | COVERED |
| **Scheme** | a Proposition the conspirators `commit` to, plus `cover` Records; progress as `Record.stages` | conspirators | `utter`, `commit`, `conceal` | secrecy decay is SYSTEM (§10.3) | until discovered or done | COVERED (composed) |
| **Debt** | a `covenant` kind with an `amount` key | creditor; debtor | — | `seize` on a lapse (unbuilt) | — | DEFERRED with its reader (K-14) |
| **Embargo**, **interdict**, **emergency**, **edict** | none-yet: kinds of the deferred `proclaim` | — | — | none yet | — | DEFERRED with `proclaim` and its readers (K-11, K-34) |
| **Heresy declared** / an organization outlawed | a `condemnation` of a Proposition | — | — | proposed: an accusation grounded on a live `commit` to a condemned Proposition (unbuilt) | — | DEFERRED (K-11) |
| **Claim to a title** | none | — | — | none | — | DEFERRED — the word collides with the `Claim` carrier and the `claim.*` event kinds, and nothing reads it (K-11) |
| **Charter / privilege / exemption** | a `dispensation` whose `terms` is the grantee | — | `issue` | proposed: a `purview_reaches` exemption (unbuilt) | — | DEFERRED — the instrument exists; the state ships with its reader |

### 8.2 Exact roster additions

**`record_kinds` additions** — three, each with its exact keys (`Record.__post_init__` refuses any other
set; no name is a `tenure_kinds` member). `terms` reads from the act's `subject` (`rosters.yaml:225-226`).
`at` follows `dispensation`'s precedent: it is no operand, so the mint reads it from the act's payload as
declared and a computed act carries `at: None` (`loop/effects_information.py:84-85`); the seat's rung,
where a reader needs it, is where the Record is drawn up (`_seat_rung`, `:145`).

| kind | keys | producer | reader |
|---|---|---|---|
| `treaty` | [terms, to, at] | `covenant` | `_renewals` |
| `alliance` | [terms, to, at] | `covenant` | `mustered` |
| `cover` | [terms] | `conceal` | `attribution.anchor_of` |

**Not added, and why (K-11):** `case` — `_eff_open_case` mints kind `text` by its own ruling until a
reader needs a case kind (`effects_information.py:196-198`); `warrant`, `summons`, `charter` — each would
carry `dispensation`'s exact keys `[terms, to, at]` (`rosters.yaml:212`), a second vocabulary for one
shape; `accusation`, `demand`, `challenge` — likewise `petition`'s; `peace` — one instrument with
`treaty`; `war` — it exists as a `WAR`-mood Proposition read by `at_war` (`faction_q.py:214-250`), and a
Record would be a second owner of one fact (K-29); `siege` — a Query over arrived armies (K-28);
`truce` — no reader (K-32), and revision 1's `until` key was in any case a second owner beside
`Record.stages`; `claim`, `embargo`, `interdict`, `emergency`, `edict`, `condemnation`, `debt` — no reader
yet. Observation for the FA lane, not adopted here: `treaty` and `alliance` could take `at_war`'s shape
(an uttered Proposition plus commits) rather than Records, for the reason `01_AXIOMS.md:1386-1389` gives.

**`tenure_kinds` additions** — two: **`custody`** (prisoner → the issuing seat) and **`ban`** (person →
the excluding seat). Both join `contain` and `reside` in the exclusion at `data/rosters.py:453`, so
`RELEASABLE_KINDS` stays the six kinds of `release`'s declared domain, which is unchanged. Arrangement
rows may then declare `disposes: custody` or `disposes: ban` (`data/arrangements.py:202-205`), and C-1's
report `arrangements_without_a_disposal_opener` is satisfied once `_eff_determine` opens them. The word
is `ban`, not revision 1's `bar`: read cold, `bar` is a tavern, the legal bar or a verb; `ban` is the
ordinary word for both exclusions, and the sources name the imperial ban (K-12).

### 8.3 Why `custody` and `ban` must be their own kinds

A disposal today is an `oblige`, and **by ruling a convict may release it himself**: `verb_table.yaml:757`
records that `determine`'s finding opens an `oblige` owned by the party it binds (proceedings C-1, RULED
A), so *"a convict can discharge his own penance"*, and that D-5 (Jordan, 2026-09-06, *"second-person
lever stays refused"*) leaves that the only route — *"no creditor verb, no `call_in`, no obligee-side
closer on an obligation exists or will"*. The code agrees: `_req_release` admits any live edge of a
releasable kind whose subject is the actor (`loop/predicates.py:338-340`). Custody built as an `oblige`
would therefore let a prisoner walk out by releasing it. Hence two new kinds, excluded from
`RELEASABLE_KINDS` on the precedent of `contain` and `reside`, which are excluded because something other
than their holder ends them (`data/rosters.py:448-453`).

This narrows C-1 rather than contradicting it: a sentence of service stays a self-dischargeable `oblige`,
priced by reception as ruled; only physical custody and the exclusion become kinds their holder cannot
close. It follows that `pardon` may close `custody` and `ban` and **never an `oblige`**, and that the
widened `determination` gate basis (§10.4 step 3) closes those two kinds only — an `arbitration` disposal
is an `oblige` (`arrangements.yaml`'s seeded row), and a basis that let a bench close it would be the
obligee-side closer D-5 refused. [ASSUMPTION: D-5 governs obligations, not every edge a seat holds on a
person — basis: its own words, and `revoke`, which closes another's `hold` through a basis, coexists with
it.] The four procedure games the source left unseeded — interrogation, legal trial, tribunal,
inquisition hearing — were left out because their `disposes:` tenure was an unresolved placeholder
(`arrangements.yaml:16-21`); `custody` and `ban` answer it.

---

## 9. New verbs

Twelve rows, written table-ready in the table's own columns and in their resolved form. Grade is
`assumption` for all twelve. Evidence is written out; the bracketed id is the extraction row, kept as a
courtesy. Every remit eligibility is `issue`, `determine` or `dispatch`, already on the roster
(`rosters.yaml:302`). Every contested row keys its `writes:` and `emits:` by degree, as the loader
requires (`data/verbs.py:589-620`; `tell`'s shape, `verb_table.yaml:890-899`). No precondition uses a new
stem: `REQUIRES_STEMS` is closed and refuses an unknown one at load (`data/requires.py:708-711`,
`:836-842`), so a read the grammar cannot spell — a negation, a custody check, a held warrant — is the
effect's decline, on `_req_oblige`'s and `_eff_open_case`'s precedent (K-18).

### 9.1 Law and custody

#### `detain` — G13
*L* detinere *'hold back', via OF* detenir. **Fit:** FITS — it names a holding that lasts, which is what
the `custody` edge is; *arrest* (OF *arester* 'stop') names only the moment.

- **row:** stratum `contested_physical` · scale person · eligibility `remit:dispatch`, through a seat
  whose portfolio is enforcement (Knights of the Peace, "law enforcement"; Royal Investigators, "court
  prosecution", `rosters.yaml:1542-1543`) · beneficiary `none` · counterparty `subject`
- **requires:** `existence` of `subject` kind Person (conjunct `party`). The warrant is not a stem: the
  enabler forms a `detain` only from a held dispensation whose `terms` names the subject (§10.1); the
  effect declines an act whose actor holds none (`detain.refused`, the write clause); the gate's new
  `warrant` basis re-checks it at the write (K-03).
- **writes (by band):** Overwhelming, Success → `Tenure.since`, kind `custody`, prisoner → **the seat
  that issued the warrant**, read off the held dispensation; the enforcement seat acts `via` but does not
  own the edge (K-17). Partial, Failure → `[]`.
- **emits (by band):** Overwhelming, Success → `custody.taken`; Partial, Failure → `custody.resisted`.
  **Refusals:** eligibility → `detain.unauthorized`; party, write, counterparty → `detain.refused`. Two
  kinds on a contested keyed row are lawful once build step 4's party-gap fold edit lands (K-02), which
  precedes this verb.
- **contests:** `a standing` (`sigma_leverage`, interim) [CONFIDENCE: medium — whether resisting arrest is
  a contest of standing or of the body; if of the body, a Failure should hand off to `fight` rather than
  carry its own prize]
- **producer · composes:** the enabler's fan over held dispensations (§10.1) · `issue` (the warrant),
  `interrogate`, `determine`, `pardon`; states custody, hostage. Handing a prisoner to another bench —
  "relaxation to the secular arm" — is a second `detain` under that bench's warrant.
- **CONFLICTS:** `fight` — axis: prize and write row (`detain` writes no body); `oblige` — axis:
  eligibility and counterparty (`oblige` is one's own and consensual)
- **falsifier:** `aperture 1 0` `detain` ex > 0; `move` refused for a person holding a live `custody`
  edge
- **evidence:** *L.A. Noire* — Cole Phelps arrests a suspect [G1-67, memory-sure]; *Shadows of Doubt* —
  the player arrests a suspect the Enforcers will not chase, for the bounty [G1-90]; *Disco Elysium* —
  arrest as an RCM officer [G1-32, UNVERIFIED]; CK3 — imprison a criminal, at no tyranny cost when the
  crime is known [G2-47]; the English constable's arrest and watch and ward [H1-160]; the season loop has
  no custody kind (`rosters.yaml:115`) while NPC-088 needs "protected / exposed / arrested / dead" as a
  persistent fact and ARC-23 a capture instead of a death [C-05].
- **blocker · needs_jordan:** build steps 1, 3 and 4 (§10.4) · no

#### `interrogate` — G13
*L* interrogare *'ask'* (inter + rogare). **Fit:** FITS; set apart from `interview` by custody and by what
is at stake.

- **row:** `social` · person · `remit:determine` via a seat · beneficiary `actor` · counterparty `subject`
- **requires:** `existence` of `subject` kind Person. Custody is read at the effect, which declines a
  subject holding no live `custody` edge (`interrogation.refused`) — not a new stem (K-18). The charge is
  read at the effect too: the `HOLDS` Proposition the docketed petition names, whose `subject` is the
  prisoner (K-35; §8.1, Charge); an act with no charge to dispose declines on the same kind
  [ASSUMPTION: the alternative, a confession carrying no value, is the content-free deposit AX-7's
  falsifier names]. **Approach**
  — calm or aggressive questioning, the survey's P9 (*Lacuna*; the *L.A. Noire* remaster) — is a
  non-operand payload key read by the obstacle, on `mood`'s precedent on `utter`
  (`loop/effects_information.py:467`), never a sibling verb (§6.1, Rec 2); a computed act carries none
  until the decision layer supplies one.
- **writes:** `[]` at every band.
- **emits (by band):** Overwhelming, Success → `confession.made`, whose deposited claim's value is the
  charge Proposition's id, so the confession carries what was confessed (K-35; the survey's P58,
  information extracted in interrogation as a held object); Partial, Failure → `confession.withheld`.
  **Refusal:** `interrogation.refused` (one kind).
- **contests:** `a proposition` (social_contest, interim `sigma_leverage`). The ground: the Church
  Tribunal is accusatorial — "an Inquisitor investigating whether the accused committed an act"
  (`systems/social_contest/sim/contest/modes.py:37-52`). Its outputs are **the charge's disposition, not
  findings**: `rosters.yaml:1031` forbids making investigation a contest so that it becomes gradeable —
  "forcing one mechanism's shape onto another because it is the one that exists" — and degree-graded
  `finding.made`/`finding.none` emissions would be that route by another door. `confession` is already a
  rostered proof (`rosters.yaml:1828`), which `determine` can read.
- **producer · composes:** Q2 on a docketed person in custody, where a petition naming a charge whose
  `subject` is that person is docketed with him (the charge rides the effect-side read above, not a
  second operand) · `utter` (the charge), `detain`, `open_case`, `determine`
- **CONFLICTS:** `interview` — axis: eligibility (remit vs own), the counterparty's state (held), the
  prize
- **falsifier:** the corpus `DEGREES RESOLVED` histogram (`harness/corpus_run.py:993`) gains this prize's
  bands; `confession.made` in `w.log`
- **evidence:** *Disco Elysium* — pressing a subject (Half Light); a failed attempt locks dialogue
  [G1-22, snippet] — the lockout itself (the survey's P27, line closed on error) is **not adopted**: a
  refusal emits and the act may be chosen again, and no permanence is unauthored (AX-6); *L.A. Noire* — reading Truth / Doubt / Lie and accusing a lie with contradicting
  evidence [G1-64, G1-65]; the inquisitor's interrogation with a notary, witnesses' names withheld
  [H1-121]; torture under limits — once, bounded, no bloodshed, only where proof is "virtually certain"
  (*Ad extirpanda*) [H1-122]; the inquiry proposal's one interrogation scene per season, burden on the
  accuser, silence convicts (`proposals/2026-09-04-social-contest-branches/03_INQUIRY.md:176-193`)
  [P1-38]; the social-contest `inquiry` game is a stub whose source is "Church Tribunal / Inquisition"
  [C-01].
- **blocker · needs_jordan:** custody (build step 3); the charge (build step 5a); torture is a fixture of
  the obstacle, not a verb · no

#### `seize` — G13
*OF* saisir *'put in possession, take'* (cf. *seisin*), *from a Frankish or Medieval Latin legal root*
[UNVERIFIED]. **Fit:** FITS.

- **row:** `uncontested_material` · settlement · `remit:issue` via a seat · beneficiary `none` ·
  counterparty — (K-04: a non-consensual act on another's edge names no counterparty, on `revoke`'s and
  `destroy_record`'s precedent; the dispossessed is read at the effect)
- **requires:** at build step 6, `existence` of `subject` kind Record. The warrant is the Candidate's
  source (a held dispensation whose `terms` names the Record); the effect declines a Record the actor
  already holds (the grammar has no negation). At build step 8 the object widens to a Rung (a
  settlement), and "Record or Rung" is a disjunction the typed grammar lacks (`rosters.yaml:1699-1703`),
  so the row then takes `pardon`'s route: `requires_typed: none` with the reason, a registered predicate,
  and the licence read at the effect — a held warrant for a Record, occupation for a Rung (§14.8).
- **writes:** `Tenure.until`, `Tenure.since` — whatever `hold` the object carries closes and the actor's
  opens, under a new gate basis `seizure` (judged in `tenure_write_basis`, `state/gate.py:538`), licensed
  for a Record by purview over its place and a held warrant naming it, and for a Rung by **occupation**:
  the exercised seat's faction `mustered` at the settlement and the holder's not. A hold on the settlement
  itself is lawful (`hold_object_kinds` admits a Rung) and shadows a territory hold in
  `holder_faction_of`'s walk (`world_q.py:1165-1189`), so one town can change hands without its
  territory · `record.seized`, `rung.seized`; refusals `seize.unauthorized` (eligibility), `seize.refused`
- **contests:** none
- **producer · composes:** the enabler's fan over held dispensations whose `terms` names a Record; for a
  Rung, Q2 on an `army.arrived` claim the seat-holder holds about a place his faction occupies ·
  `issue`, `destroy_record` (burn it after), `levy` (the stores half), `march` (the occupation that
  licenses a Rung seizure)
- **CONFLICTS:** `give` — axis: consent and eligibility; `levy` — axis: object (Record vs stores);
  `destroy_record` — axis: moves, does not end; `march` — axis: write row (a `hold`, not the army's
  `contain`; occupation licenses the seizure and does not perform it); `steal` — axis: eligibility
  (`remit:issue` vs `own`) and licence (a warrant or occupation vs none), the `carry`/`open_case` shape
  (§9.3)
- **falsifier:** `record.seized` in `w.log`; realm ex > 0; a seat cannot be seized (a `hold` on an Office
  is `conferral`'s and `T-o`'s alone; in `test_give.py:285`'s style); a `seize` on an occupied settlement
  flips `holder_faction_of` there, and one on a settlement the seat's faction does not occupy is refused
- **evidence:** the Cardinal of Justice's portfolio includes "text suppression" (`rosters.yaml:1536`),
  and NPC-088's copied text can be found and taken [C-08]; `give` is the only Record mover and it is
  consensual (H-84); confiscating a heretic's goods in thirds (*Ad extirpanda*; Spanish practice)
  [H1-132]; the index and seizure of copies [H1-134]; pursuivants searching premises and seizing papers on
  warrant [H1-175]; the Church's mass seizure of territory declared by an Archbishop (corpus-rebuild annex
  A, `:477-483`) [P1-14]; nationalizing church lands and foreign charters [R1-12]; for the Rung half,
  family 25's conquest, raid and usurpation rows (Appendix B).
- **blocker · needs_jordan:** build steps 1 and 6 (Records), 8 (Rungs) · no; R-6 asks whether a won field
  should instead transfer title directly

#### `pardon` — G13
*OF* pardoner *← ML* perdonare *'grant wholly'*. **Fit:** FITS.

- **row:** `binding_decision` · settlement · `remit:determine` via the seat that owns the disposal ·
  beneficiary `subject` · counterparty —
- **requires:** a live edge **of kind `custody` or `ban`** whose object is the exercised seat. That is a
  disjunction over kinds, which the typed grammar does not have (`rosters.yaml:1699-1703`), so the row
  takes `release`'s route: `requires_typed: none` with the reason, a declared `domain: [custody, ban]`,
  and a registered predicate. An `oblige` disposal is self-releasable by ruling and D-5 bars an
  obligee-side closer of an obligation (§8.3), so `pardon` never closes an `oblige`; it follows
  `revoke`'s precedent — a seat closing another's edge under a basis — and does not touch D-5's object.
- **writes:** `Tenure.until`, under the widened `determination` basis (closing `custody` and `ban` only,
  §8.3) · `disposal.lifted`; refusal `pardon.refused`
- **contests:** none
- **producer · composes:** Q2 on the prisoner or the banned (the post-remit channel already deposits to
  those a seat binds) · `determine`, `detain`; states custody, excommunication, outlawry, sentence
- **CONFLICTS:** `release` — axis: whose edge (another's, closed by the object; not one's own, closed by
  the subject); `revoke` — axis: edge kind (a disposal, not a seat-`hold`) and basis
  (`determination`, not revocation)
- **falsifier:** a `custody` edge closes with `disposal.lifted` in `w.log` and the former prisoner's
  `move` is admitted the next season
- **evidence:** the king's pardon, grace and remission, which by the Act of Settlement 1701 cannot bar an
  impeachment [H1-63]; the Great Council of Venice granting grace [H1-115]; absolution and reconciliation
  of a penitent [H1-128]; bail and *habeas corpus* as secular releases [H1-163, H1-173]; CK3 — grant a
  pardon, release or ransom a prisoner [G2-51]; reversing a verdict, restoring standing posthumously
  [R1-42]; reversing an excommunication by penance or a Grand Debate [P1-43].
- **blocker · needs_jordan:** build steps 3 and 5 · no

### 9.2 Polity and war

**War needs no new verb and no new carrier (K-29).** The tree already carries it: a `WAR`-mood
Proposition whose `subject` and `value` are the two factions, uttered by a person, plus live `commit`s
to it, read by `faction_q.at_war` (`queries/faction_q.py:208-250`), on `01_AXIOMS.md:1374-1384`'s
de jure/de facto shape. A declaration of war is `utter` of that Proposition and then the seats' own
`commit`s; peace is each committed person's `release`. A march needs no war — `at_war` gates no verb,
and a march into an enemy-held settlement is the casus belli the other side may answer by uttering.

**`proclaim` is deferred, with its readers (K-34).** With `war` a Proposition and `truce` deferred
(K-32), `proclaim` has no Record kind that any code reads — edict, embargo, interdict, emergency and
condemnation were already deferred as orphans (K-11) — and a verb whose every kind is unread breaks the
suite's own rule (§8, §10.4). It returns when its first kind has a reader. Its evidence — edicts and
proclamations [H1-54], the edict of grace [H1-117], emergency decrees [R1-43], proscription lists
[R1-34], the Policy Instrument [P1-60], censure and embargo [P1-11], a state of emergency [C-32] — stays
indexed under families 13 and 29 (Appendix B); the war rows [G2-08, G2-55, P2-18, C-38] under family 21.

#### `covenant` — G14
*OF* covenant, *present participle of* convenir *'agree' ← L* convenire. **Fit:** FITS [CONFIDENCE:
medium — the root it shares with `convene` and its religious sense in a setting with a Church are the
risks; `pact` (L *pactum*) is the alternative].

- **row:** `social` · settlement and up · `remit:issue` via a seat **only** — an `own` alternative would
  let anyone mint a treaty (K-14) · beneficiary `to` · counterparty `to` (the other seat's holder)
- **requires:** `existence` of `to` kind Person ∧ `existence` of `subject` kind Proposition (the terms are
  uttered first). No question's referent is a Proposition today (`verb_table.yaml:773`; 802 of 802
  refused, `hole_register.yaml:3521`), so the row is built after `utter` mints the utterer's hold (build
  step 2), or it joins the always-refused set.
- **writes:** `Record.exists`, kinds `treaty`, `alliance` [terms, to, at], `terms` = the Proposition;
  `Record.stages` as the term (matures at MAT) · `covenant.offered`; refusal `covenant.refused`. `truce`
  is deferred with its reader (K-32). [GAP: which of the two kinds a computed covenant mints — the `kind`
  operand has no source for it today; a hand-built act declares it.]
- **contests:** none. The instrument is in force when both holders `commit` to its Proposition; the
  acceptance is the counterparty's own act. This two-sidedness stands on its own argument — revision 1
  tagged it to ED-IN-0210 ruling 2, which is `petition`'s withdraw/deny pair (`verb_table.yaml:719`), not
  this (K-14).
- **producer · composes:** the known-person fan (`options.py:827-860`) over seat-holders the actor knows ·
  `utter`, `commit`, `transfer` (tribute renews through `_renewals`), `march` (breach)
- **CONFLICTS:** `issue` — axis: purview (a writ reaches down; a covenant reaches across, so the authority
  conjunct is dropped); `petition` — axis: eligibility (a seat) and the two-sided commit
- **falsifier:** a `commit` by the addressee to the covenant's Proposition in `w.log`; an ally's persons
  present at a march's destination appear in its `subject_members` (a named test in
  `test_mass_battle_provider.py`)
- **evidence:** negotiating, ratifying or letting lapse a treaty, tribute or terms of surrender [R1-06];
  a league of towns [R1-15]; Treaty and Diplomacy in the faction roster, the Formal Crown Treaty being
  Crown-only [P1-07]; settlement as the split of a jointly created surplus, composing `utter` and `commit`
  (`proposals/2026-09-04-social-contest-branches/02_NEGOTIATION.md:36-50`) [P1-65]; CK3 — white peace,
  enforced demands, a purchased truce [G2-14]; RTK XIV — apply for or dissolve an alliance [G2-96]; five
  cases ask to conclude, renew or repair a binding agreement [C-40]; the Venetian Senate deciding war and
  peace [H1-99]; hostages exchanged as surety for a treaty [H1-75].
- **blocker · needs_jordan:** build steps 2 and 7; the `debt` kind is deferred with its `seize` reader
  (§9.7) · no

**There is no `besiege` (K-28).** Revision 2's `besiege` shared `march`'s prize, step, eligibility,
cell and sides, and differed only in what it wrote on `Won` — a verb declaring its intended outcome,
which direction 3 retires and direction 8 names as a stake. A siege is a `march` that has arrived at a
settlement its side does not hold, read as a Query (§8.1); its larder effect waits for a reader (§10.4).
Its evidence [R1-29, P1-03, G2-12] stays under family 24 (Appendix B).

#### `raze` — G9
*F* raser *'shave, scrape' ← L* radere. **Fit:** FITS.

- **row:** `contested_physical` · settlement · `remit:dispatch` via a seat · beneficiary `none` (the
  loader requires the column, `data/verbs.py:528-534`; K-06) · counterparty —
- **requires:** the Site or Rung exists; occupation — the exercised seat's faction `mustered` at the
  settlement (`world_q.py:980-996`) — is read at the effect. No log read, no Record.
- **writes:** `Site.exists` / `Rung.exists` to absent (the rows admit RES, `write_matrix.yaml:302-336`;
  `destroy_record` is the precedent on `Record.exists`) · `site.razed`, `rung.razed`; refusal
  `raze.refused`
- **contests:** none
- **CONFLICTS:** `sabotage` — axis: write row (existence vs condition)
- **falsifier:** `w.rungs` shrinks — H-166 limit 3, "nothing shrinks it" (`hole_register.yaml:3651`)
- **evidence:** H-166, "no verb ends a Rung or a Site" [C-60]; RTK XIV — demolish a building [G2-84];
  the *chevauchée* and scorched earth [R1-58]; razing a heretic's house [H1-132]; the townspeople burning
  Kiersau Abbey and its library in *Pentiment* [G1-17].
- **blocker · needs_jordan:** build step 11, after H-166's own design order — cost, holder, closer
  (`hole_register.yaml:3651-3652`) · no (H-166 carries its own record)

### 9.3 Covert

#### `conceal` — G6
*OF* conceler *← L* concelare (*celare* 'hide'). **Fit:** FITS.

- **row:** `social` · person · eligibility `own` · beneficiary `actor` · counterparty —
- **requires:** — (no precondition, so an empty `emits_on_refusal` is lawful)
- **writes:** `Record.exists`, kind `cover` [terms], `terms` = the agent; the Record's own id is the
  alias · `cover.assumed`
- **witnessing:** ordinary. Taking a cover is seen by whoever is present, as any act is; there is **no
  channel exception** in `witness_channels`' precedence (`rosters.yaml:398-405`), which would be a
  per-verb special case (K-19). What the cover changes is attribution afterwards:
  `state/attribution.py::anchor_of` answers the cover Record's id, at tier 1, for an act whose actor holds
  a live `cover`, and every reader downstream of the anchor is unchanged.
- **contests:** none
- **producer · composes:** a need question of a covert seat-holder — the Riskbreakers, "Extralegal
  infiltration. Loyal to Valoria the concept, not institutions" (`rosters.yaml:1544`), a Löwenritter body
  (`:1505`) · `surveil`, `seize`, `fight`, `tell`; state concealed identity
- **CONFLICTS:** `forge` — axis: what is falsified (a Record about oneself, read by attribution, not a
  document's content)
- **falsifier:** `anchor_of` resolves an Event's anchor to a `cover` id; `seen` claims name the alias
- **evidence:** Riskbreaker Identity and Deniability Debt 0–7 (corpus-rebuild annex A, `:1185`;
  `references/names_index.yaml:360`) [P1-48]; acting under cover so that an act emits nothing below a
  vantage threshold [P2-77]; twelve cases ask for concealment by an ongoing, lapsing effort [C-14] and five
  for deniable acts — NPC-005: "a clean act leaves no trace to her, her order or the Crown" [C-15]; the
  concealed-identity meters [R1-55]; concealing a source, hiding a death, delaying succession news
  [R1-52]; *Tails Noir* — sneaking past or hiding from guards [G1-77]; *Pentiment*'s town priest hiding
  the saints' origin as Mars and Diana [G1-18].
- **blocker · needs_jordan:** build step 10, with the `anchor_of` cover read · no

#### `sabotage` — G9
*F* saboter (19th–20th c.) [UNVERIFIED: the clog etymology]. **Fit:** FITS as the plain word; it is a
modern coinage, a voice question for in-world labels, not for the row.

- **row:** `uncontested_material` · person · `own` | `presence:<site>` · beneficiary `actor` ·
  counterparty — (K-04: a Site cannot be held at all, `rosters.yaml:152`, so "the fabric's holder" is
  nobody)
- **requires:** `restore`'s cell
- **writes:** `Site.condition`, negative, by `_rise`'s mirror through the same accumulator ·
  `site.damaged`; refusal `sabotage.refused`
- **contests:** none
- **CONFLICTS:** `restore`, `work` — axis: sign and beneficiary. `_eff_work` stages a declared delta with
  no sign check (`loop/effects_economy.py:86-98`), so today a hand-built `work` can already lower a
  condition; the same build step restricts `work`'s declared delta to ≥ 0, so each verb owns one sign
  (K-09). The thinnest pair in the suite (K-27).
- **falsifier:** `Site.condition` falls at RESOLVE with a computed `sabotage` among its causes
- **evidence:** RTK XIV's Hidden Poison — a target area's development and public order fall [G2-89];
  *Shadows of Doubt* — sabotaging or hacking security systems [G1-96]; seizing or burning property
  [P2-44]; sabotaging a works [P1-62]. [DISAGREE, kept: P1-62's source,
  `proposals/2026-09-17-governance-and-holdings/00_THE_DESIGN.md:373-382`, argues sabotage needs no verb
  because emptying a works' store or taking its plot already stalls it. That covers stalling a works; it
  does not lower a built Site's condition, which no computed act does.]
- **blocker · needs_jordan:** build step 9 · no

#### `steal` — G6 (R-8)
*OE* stelan. **Fit:** FITS (§4) — a cold reader lands on taking what another holds without consent or
authority; *take* is too wide (prose says "take the seat"), and *rob* implies force, which here is a
`fight` and then a `steal`.

- **row:** `uncontested_material` · person · eligibility `own` · beneficiary `actor` · counterparty —
  (K-04: a non-consensual act on another's edge names none, on `revoke`'s, `destroy_record`'s and
  `seize`'s precedent; the dispossessed is read at the effect)
- **requires:** `existence` of `subject` kind Record. "Held by another" is a negation the grammar lacks
  (`rosters.yaml:1699-1703`), so the effect declines a Record the actor already holds (`seize`'s route,
  §9.1) and one whose holder does not stand where the actor stands — `place_of` answers a Record by its
  holder's place (`queries/world_q.py:423-425`). No new stem (K-18).
- **writes:** `Tenure.until`, `Tenure.since` — the holder's `hold` closes and the actor's opens, under a
  new gate basis `theft` (both matrix rows exist) · `record.stolen`; refusal `theft.refused`. No new kind,
  no ninth operand, no remit act.
- **gate:** the opening already passes `T-m` — an actor opening a `hold` on a non-seat object naming
  himself (`state/gate.py:707-710`; Appendix D, p). What no basis admits is the **closure** of the
  holder's `hold`: its owner is not the actor (`T-m`), nothing it names is gone (`cascade`), it is no
  seat's (`T-o`), and the actor ended no hold of his own on it (`handover`); the suite's `seizure` (§9.1)
  is licensed by a warrant or occupation. **`theft`** — the closure of another's live `hold` on a
  non-seat object, judged across the batch with the actor's own opening on the same object as `handover`
  is, the co-location read at the effect — is a Layer-1 §C.2 addition on K-33's precedent (bases are
  added per plan position, `04_CODE_ARCHITECTURE.md:564-586`). Every basis so far is bound to the
  owner's own act, to a seat's authority, or to causation (`state/gate.py:557-628`); this one is bound to
  none of the three, and that is R-8's question.
- **contests:** none. Whether the taking was seen is WITNESS's (`epistemic.py:322`), and what follows —
  a `petition`, a warrant `issue`d, a `detain` — is other people's acts. No rostered prize fits
  (`rosters.yaml:1106-1153`), and inventing one so the attempt can be graded is the drift `:1031-1034`
  names.
- **producer · composes:** Q2 on a `content:` or `record.created` claim about a Record the actor does not
  hold (Records are 633 of 4,451 realm question referents, `verb_table.yaml:676`); direct; the thief
  learns what it says through the newly-held deposit, "a held document is a held belief"
  (`loop/witness.py:283-305`) · `conceal` (before), `destroy_record` or `give` (after), `fight` (a
  robbery)
- **CONFLICTS:** `give` — axis: consent and counterparty; `seize` — axis: eligibility (`own` vs
  `remit:issue`), licence (none vs a warrant or occupation) and beneficiary (`actor` vs `none`) — on the
  `carry`/`open_case` precedent, the same write with eligibility differing, it is `seize`'s sibling and
  not a widened reach: adding `own` to `seize` would make its warrant optional, the "different game" H-52
  names; `destroy_record` — ends, does not move; `levy` — stores, by remit; `transfer`, `exchange` —
  stores, one side or both; `forge` — makes a Record; `conceal` — a Record about oneself; `detain` — a
  person, under a warrant; `fight`, `march` — a prize
- **falsifier:** `record.stolen` in `w.log` from `populated.run` with no hand-built act; the former
  holder's Q2 question about the Record the next season; a `steal` refused on a Record the actor already
  holds, or whose holder stands elsewhere
- **evidence:** *Esoteric Ebb* — "steal anything in sight" [G1-38]; *Shadows of Doubt* — stealing a
  document on a side job [G1-98], and the survey's Entering family (H), whose verbs are *sneak*, *pick*,
  *steal*, *climb* — access taken at the risk of a fine (P34); CK3 — the steal-an-artifact scheme, its
  effect inferred from its name [G2-26, UNVERIFIED]; family 30's "taking a Record without consent"
  [C-08]; the Riskbreakers' "Extralegal infiltration" (`rosters.yaml:1544`) and the Cardinal of Justice's
  "text suppression" (`:1536`), neither of which has a route to a document today except a warrant.
- **blocker · needs_jordan:** the `theft` basis (build step 6a); H-156's (a)/(b), which decides its
  formation policy as it does `destroy_record`'s · **yes — R-8** (§13.7), carried on its recommendation;
  Jordan may overrule.

### 9.4 Persuasion and the person

#### `argue` — G3
*OF* arguer *← L* arguere *'make clear, prove; accuse'*. **Fit:** FITS.

- **row:** `social` · person · eligibility `own` · beneficiary `actor` · counterparty `to` (the hearer,
  by the known-person fan)
- **requires:** `existence` of `subject` kind Proposition ∧ `relation` of `to`, `with`
- **contests:** `a proposition` (social_contest, interim `sigma_leverage`)
- **writes (by band):** Overwhelming, Success → `Person.pursuits` (the row's own "moved by argument",
  `write_matrix.yaml:186-193`); Partial, Failure → `[]`. The row's `unproduced: H-62` declaration
  (`write_matrix.yaml:193`) is deleted in the same commit, or the loader refuses a stale declaration
  (`data/verbs.py:818-821`; K-21).
- **emits (by band):** Overwhelming, Success → `argument.won`; Partial, Failure → `argument.lost`.
  **Refusal:** `argument.refused` (one kind).
- **producer · composes:** a need question (the actor's own OUGHT), fanned over hearers · `utter`,
  `commit`, `tell`
- **CONFLICTS:** `tell` — axis: subject kind (a Proposition vs any topic), prize, write row
  [CONFIDENCE: medium — pass 2's own open question: whether a conviction write should instead ride every
  successful telling]
- **falsifier:** `Person.pursuits` moves in a run — today a RES row with no writer (§1); H-62 gains a
  producer
- **evidence:** H-62 — three interior rows with no verb, "Part E carries no argument verb" [C-53]; CK3 —
  convert, or demand conversion, eased by low fervour [G2-52]; persuading one powerful listener [R1-62];
  preaching as an office-less authority [R1-69]; spreading piety [P1-16]; *Disco Elysium* — persuade,
  charm or bluff [G1-23]; RTK's debate between officers [G2-103]; moving and debating a motion in
  Parliament [H1-04, H1-05].
- **blocker · needs_jordan:** the pursuits delta's magnitude (an `assumption` fixture); a Proposition
  referent (build step 2) · no

#### `tend` — G15
*Aphetic form of* attend *← L* attendere *'stretch toward, heed'*. **Fit:** FITS. *Heal* (OE *hǣlan*)
names the outcome — the body rising — and is refused on direction 3's logic, as `kill` is.

- **row:** `uncontested_material` · person · eligibility `own` · beneficiary `subject` · counterparty —
- **requires:** `existence` of `subject` kind Person ∧ `relation` of `subject`, `with`
- **writes:** `Person.body` upward (the row admits RES, `write_matrix.yaml:161-167`) · `body.tended`;
  refusal `tend.refused`
- **contests:** none
- **producer · composes:** Q2 on a `body.changed` claim about a known person · `fight`, `march`
- **CONFLICTS:** `restore` — axis: kind (Person vs Site); `train` — axis: field (body vs capability)
- **falsifier:** `Person.body` rises with a `tend` among its causes — no code path raises it today; its
  writers only lower it (`fight`, `march`, MATTER subsistence)
- **evidence:** six cases ask to heal or recover, in a fast partial and a slow full form (ARC-53, SCN-03,
  SCN-04, SCN-07, EMG-X7, SCN-LOOP-C) [C-48]; *Esoteric Ebb*'s short rest restoring hit dice and spell
  slots while the clock advances [G1-46].
- **blocker · needs_jordan:** none named · no

#### `train` — G15
*OF* trainer *'drag, draw'; 'instruct' from the 16th c.* **Fit:** FITS — it covers self and pupil, where
*practise* covers only self.

- **row:** `uncontested_material` · person · eligibility `own` · beneficiary `subject` (self or pupil) ·
  counterparty —
- **requires:** `existence` of `subject` kind Person
- **writes:** `Person.capability` — a **retired** row (`write_matrix.yaml:386`), returned with its
  producer in the same commit under the file's own discipline, "a row exists because a producer produces
  it" (`:383-384`; K-21) · `capability.raised`; refusal `train.refused`. The capability raised ranges over
  the capability names `verb_capability` maps verbs to (`rosters.yaml:1061-1064`, today `copying`).
  Thread Sensitivity has no carrier (H-85, `hole_register.yaml:1052-1054`), so it is structurally outside
  the range, and the row records that exclusion: P-08 forbids non-sensitives gaining Thread-level
  capability by study (`canon/02_canon_constraints.md:50`; K-20).
- **contests:** none
- **producer:** a need question
- **CONFLICTS:** none among verbs — no verb writes capability; a `cast:` overlay is its only writer today
  (`rosters.yaml:1054-1059`)
- **falsifier:** `sigma._pool_of` varies by person (R-09's `partial`, `seam/wrappers/sigma.py:94-97`)
- **evidence:** "NOTHING creates or develops a person" (`requirements.yaml:71`) and the seam table's "no
  creation, no progression, no chronicle" (`rosters.yaml:1011`), with eight cases asking [C-49];
  practising to raise a capability [P2-34]; CK3 — educating a child [G2-06]; teaching a group in secret
  [P2-72, C-47].
- **blocker · needs_jordan:** a capability-key operand — the `kind` operand, from the fixture or referent
  fallback [ASSUMPTION] · no

### 9.5 Cross-check

No two new verbs share write row, eligibility and counterparty. Eligibility is shared, and each sharing
pair differs by write row or counterparty: `remit:dispatch` — `detain` (a `custody` edge; counterparty
`subject`), `raze` (existence), beside the existing `dispatch` and `march`; `remit:determine` —
`interrogate` (no write; a prize), `pardon` (`Tenure.until`), beside `determine` and `open_case`;
`remit:issue` — `seize` (a `hold` moved), `covenant` (a Record `to` a person), beside `issue` and `levy`;
`own` — `argue` (`Person.pursuits`), `conceal` (a `cover` Record), `sabotage` (`Site.condition`, −),
`steal` (a `hold` moved), `tend` (`Person.body`), `train` (`Person.capability`). `steal` shares `seize`'s
write row and differs by eligibility and licence — the `carry`/`open_case` shape, a sibling pair rather
than a thin one.
[CORRECTION: revision 1 said the law verbs "share eligibility"; `detain`, `seize` and `pardon` have three
different eligibilities (K-26).] The one thin pair, named rather than hidden (K-27): `sabotage`/`work`
(sign only); revision 2's second, `besiege`/`march`, is gone with `besiege` (K-28). No new verb depends
on the `repudiate` cut.

### 9.6 Widened reaches — and why no new verb

| verb | what widens | why a new verb was refused |
|---|---|---|
| `determine` | `contests: "a proposition"` (social_contest through the interim `sigma_leverage`, repointing to the proceedings provider, `rosters.yaml:1149-1153`). Writes by band: Overwhelming, Success, Partial → `Tenure.since`, `Tenure.degree`, `DocketItem.matter` (the disposal opened and graded); Failure → `DocketItem.matter` (acquittal: the matter leaves the docket, nothing opens) [ASSUMPTION: which bands convict]. Emits by band: `matter.determined` / `matter.dismissed`. Disposes whatever kind the arrangement `disposes:` — `oblige`, and with the suite `custody` and `ban`. **One fold edit is needed:** the row keys two refusal kinds (`verb_table.yaml:235-242`) and the loader refuses a contested keyed row with more than one (`data/verbs.py:717-720`), because the seam's party-gap refusal emits the union (`loop/resolve.py:546-553`). The party gap IS the counterparty clause failing, so `_party_gap_refusal` emits `row.refusal_for(COUNTERPARTY_CLAUSE)` where the row keys it, and the loader rule narrows to rows that do not (K-02). **The Proposition contested is the charge (K-35)**, and its obstacle should be read from testimony — live `commit`s to the charge — rather than from the accused's `capability/2`, which is what `_obstacle_of` reads for a person subject today (`seam/wrappers/sigma.py:105-122`): an observation for the SC lane, whose ED-SC-0033 clause 3 names the proceedings subsystem the obstacle's owner (`rosters.yaml:1138-1148`), not built here. Investigation stays uncontested: the contest is the charge, never the finding | the matter, bench, docket and eligibility are `determine`'s; a `try` or `judge` beside it would be a second act disposing the same docket item — shape divergence. A judicial duel composes as a challenge (`petition` + `fight`, K-23) whose outcome the bench reads [ASSUMPTION]; the row's one prize does not change by arrangement |
| `confer` | a seat-`hold` carrying `Tenure.term` (regency, a term-limited seat). The `conferral` basis admits a seat-hold's opening and its `payload`; it must also admit a `term` at opening — one gate clause | same edge and basis; regency is a term, and `Act.via` already carries delegation |
| `give` | object kind Rung: cede a rung hold; the gate's `handover` already covers every non-seat hold, while the live cell narrows the verb to `kind: Record` (`verb_table.yaml:398`) — so this widening is load-bearing for cession, the one consensual route by which title moves | the same two-hold write; `cede` would duplicate it |
| `march` | **The army arrives.** Today `_eff_march` writes `body` and `stance` on the losing side only (`loop/effects_combat.py:316-317, :345-370`) and moves nobody: after a `Won` the attackers are still `mustered` at their origin, so capture, interception and relocation are inexpressible, and a march on one's own occupied settlement fights one faction against itself (H-151). **One write is added:** on `Won` and `Unopposed`, every claimant is relocated to the destination by `_relocate`'s pair (`loop/effects_migration.py:68-89`, which gains a person parameter so the leg id keys on the mover) — close the live `contain`, open one to the destination, append it to `travel_leg` — emitting `army.arrived` beside the band's kind. `Lost` is unchanged (the attackers' casualties and grudge) [ASSUMPTION: a routed army does not arrive — R-7]. **The stake is derived at the destination `d`, never declared**, from three reads that exist: `mine` (the faction of the seat in `a.via`, `loop/sides.py:77-78`), `holder = holder_faction_of(w, d)`, `defenders = mustered(w, d, holder)`. `holder == mine` → relocation (or a defence, if an enemy march on `d` follows): no contest, `Unopposed`, the army arrives. `holder is None` → arrival at unheld land, no title write (who holds an unheld place is unruled, H-166). Another holder, `defenders` empty → capture attempt, unopposed: occupation. Another holder, `defenders` present → capture attempt, opposed: `Won` arrives, `Lost` does not. Interception needs no new state: an army that has arrived is in every later `mustered(d, holder)` read (`seam/wrappers/mass_battle.py:154`); within one round, two marches on one settlement are ordered by `_canonical_order`'s hash (`loop/resolve.py:47-54`), so same-round interception is order-dependent and cross-round interception deterministic. **Code edits, no new resolver or operand:** (i) `sides_of` returns `subject = None` when `holder == mine` (H-151's reverted fix, `hole_register.yaml:3258-3264`); (ii) the wrapper returns its existing `Unopposed` shape (`mass_battle.py:164-169`) instead of `PARTY-GAP` when `subject is None` and claimants and rung are given; (iii) H-149's non-settlement refusal moves from `subject = None` to empty `claimants`, so it still refuses at `loop/resolve.py:558-559` and `subject None` comes to mean only "no opposing holder" (§14.8); `ENC` on `(Tenure, since)`, `(Tenure, until)`, `(Person, travel_leg)` (`write_matrix.yaml:352-354, :366-368, :225-226`), on M4's own precedent for `body`/`stance` (`loop/encounter.py:25-28`); and a tenth gate basis, `muster` (K-33) | a stake is not a choice (direction 8). `besiege`, `intercept` or `relocate` beside `march` would each be a verb declaring its intended outcome — the `kill`/`wound` shape direction 3 retires — over one prize, one step and one muster |
| `survey` | subject kind Rung, answered by the rung's holding faction (effect-side, `holder_faction_of`); declined at H-169 limit 6 today | the same sheet mint; `census` or `audit` would duplicate it |
| `oblige` (a reader) | no row change: a seat-holder's own `oblige` to another seat — `oblige : Person → Person \| Office`, owned by the person who swore it (`architecture/meta/01_AXIOMS.md:1205-1218`: *the Grandmaster forswore the King*) — is read by `purview_reaches` as subordination (H-101). Expulsion of a member is the seat withholding renewal, so the term matures at MATTER: the shipped `oblige_term` is 4 (`data/fixtures.py:694`), and only H-159's `None` control arm never matures [CORRECTION: revision 1 said expulsion waits on that fixture (K-26)] | homage is the same `oblige` with a term renewed by `transfer`; `swear` or `homage` would be a second opener. A seat closing a member's `oblige` would be the obligee-side closer D-5 refused (`verb_table.yaml:757`) |

Revision 1 also widened `commit` and `oblige` by a `remit:` alternative, `march` to a title or stores for
the winner, `tell` to an authored `said`, `surveil` to a Person and `revoke` to an `oblige`. None is in the
suite: K-07, R-2 (resolved as occupation, not title — the `march` row above), K-15, K-16, and revision
1's own D-5 withdrawal (§12).

### 9.7 Deferred, and classed as outcomes

- **`tell`'s lie — deferred (K-15).** `opening_set` declines a `tell` whose `said_of` is `None`, because
  the `holds` conjunct is named (`verb_table.yaml:930-932`), and `holds` refuses content the teller does
  not hold. A lie needs a second `said` source — a decision-layer change at `said_of`, not a row edit. It
  belongs to the telling workplan's position G7, deception (`workplans/2026-10-01-telling-workplan.md:311`,
  site `said_of`), whose falsifier is a caught liar's record falling below an honest teller's. H-183
  (`hole_register.yaml:4083`) is how much that record weighs, and names deception in its `unblocks:`.
- **`surveil`'s Person case — held (K-16).** The typed grammar has no disjunction
  (`rosters.yaml:1699-1703`), so one row cannot take "Rung or Person", and a seventh investigation row
  would break canon's *"No new action vocabulary"* and Jordan's six-as-six (`verb_table.yaml:950-960`).
  It waits until an `any` combinator is ruled — `release` is the other cell waiting for one
  (`verb_table.yaml:753`), and two cells then justify it — and is registered on ED-FI-0009.
- **`thread_read` and the thread operations — deferred.** Leap, weave, pull, past-pull, lock, dissolve
  and mend (`research/cross_scale_action_catalogue_v1.md:711-729`) [R1-67]; weave, cut, reinforce, mend
  [P2-43]; eleven cases with graded, costed operations [C-51]. They belong to plan positions 27/29f
  (`verb_table.yaml:1103`); `thread_read` additionally waits on H-85.
- **`debt` — deferred (K-14),** with the `seize` reader that would distrain on a lapse.
- **`proclaim` — deferred (K-34),** with every kind it would mint; a declaration of war is `utter` and
  `commit` (§9.2).
- **`truce` — deferred (K-32).** Its only proposed reader was a `march` refusal or flag; refusal
  contradicts direction 8 and a flag has no mechanism, because emits are keyed per band
  (`hole_register.yaml:3309-3313`).
- **A siege's effect on a larder — deferred,** with its reader, as a new hole (§10.4).
- **Approach verbs — not verbs (§6.1, Rec 2).** Pressing, flattering and threatening are data on the one
  row — a non-operand payload key on `interview` or `interrogate`, read by the effect or the obstacle, on
  `mood`'s precedent on `utter` — not siblings of either; a computed act carries none until the decision
  layer supplies a source.
- **Theft without licence — `steal`, carried (R-8).** If Jordan rules R-8 (b), `steal` leaves the suite
  and family 62 stays GAP with no verb.
- **Cryptology (the survey's P54) — deferred,** with no demand and no reader; `research` reads content
  verbatim, and misreading is the receiver's (`construe`, WITNESS-side).
- **The orphan Record kinds — deferred (K-11, K-34).** `edict`, `embargo`, `interdict`, `emergency`,
  `condemnation` (heresy declared; an organization outlawed), `claim` and a charter's exemption each ship
  only with the code that reads them; the first five return with `proclaim`. `claim` also collides with the `Claim` carrier and the `claim.*`
  event kinds, so it needs another word when it comes.
- **Outcomes and stakes, not verbs.** A **sentence** (the disposal's kind); **occupation** (a won or
  unopposed `march`) and **conquest** (`seize` on the occupied place, R-2 resolved); **raid** and
  **usurpation** (the same occupation, then `raze` or `seize`); a **siege** (a Query over an arrived army,
  K-28); **capture, interception, relocation** (the stakes of a `march`, direction 8); **murder** (a
  `fight` whose band is `Felled`, with `conceal`); **execution** (§9.8); and, by direction 3, **`kill`**
  and **`wound`**.

### 9.8 Why `execute` is not a verb (R-1, K-10)

Revision 1 proposed `execute` (*L* exsequi *'follow out'*) with grade `absent`, writing `Person.exists` by
fiat. The suite refuses it as a verb, on two grounds:

1. **The word.** "Executed" is this repo's process vocabulary — the corpus's executed set, `ex` in
   `att/ex`, `resolvable` (`requirements.yaml:674-676`). A verb of that name fails §4's test: a reader
   with no memory of the repo would not land on one meaning.
2. **The write.** Its write is the outcome direction 3 says a character cannot choose: *"characters can
   not actively choose to kill or wound. they can choose to fight tho"*.

**What a death sentence is in the suite:** a `determine` that disposes `custody`, then the enforcement
seat-holder's `fight` against the prisoner through the combat seam, the prisoner's pool held at a custody
floor [ASSUMPTION: no custody floor exists in the combat pool today — it would be a fixture]; `person.died`
arrives by degree (`Felled`). A botched execution is then a story the seam can tell. If Jordan prefers
judicial killing by direct write, the verb may not be spelled `execute` (§13, R-1). The evidence for the
family — *Pentiment*'s condemned put to death after the Archdeacon's judgement [G1-13]; CK3's execution,
raising dread [G2-49]; relaxation to the secular arm, because clerics may not shed blood (Lateran IV,
canon 18) [H1-130]; the sheriff or hangman [H1-174]; fratricide, forced suicide, scapegoat execution
[R1-36] — is the same either way.

---

## 10. The enabler, the faction map, the non-act mechanics, the build order

### 10.1 The shared enabler: a held-Record operand channel

Today a Candidate binds `subject`, `to` and `site` all to the question's **one** referent
(`decision/options.py:741-746`). Two narrower channels exist. A held writ answers operands through
`_from_content_claim` (`options.py:540`, called at `:726-729`) for the names declared in
`writ_sourced_operands` (`rosters.yaml:1571-1584`) — `to`, `kind`, `amount` — but only `to` ever resolves:
`kind` and `amount` decline every time, because neither live schema carries those keys
(`options.py:548-555`). And `tell`/`give` fan one Candidate per person the actor knows (`operand_bags`,
`options.py:827-860`).

**Shape.** `writ_sourced_operands`, a flat list, becomes a per-kind map, `record_sourced_operands`: for
each Record kind, which of the closed eight operands (`actor, subject, from, to, site, kind, amount,
floor`, `rosters.yaml:1569`) a held Record of that kind answers, and from which of its content keys.

```yaml
record_sourced_operands:        # per Record kind -- operand (one of the closed eight): content key
  dispensation: {to: to, subject: terms}
  petition:     {to: to, subject: terms}
  treaty:       {to: to, subject: terms}
  alliance:     {to: to, subject: terms}
```

Every key is one of the eight; every value is a content key of its kind, which tightens today's check
(a member of the writ list must be one of the eight, refused at import, `rosters.yaml:1576-1577`) to the
kind's own keys. `from` is on no kind — r2 keeps "where the actor stands" off a document (`:1577-1581`).
A later kind that carries `kind` or `amount` (the deferred `debt`) adds them; no live kind does, so
dropping them from `dispensation` changes no behaviour. `_derive_operand` (`options.py:717-729`) reads the
map; `operand_bags` fans one Candidate per held Record whose kind has an entry, as it fans known persons.
No faction actor, no new form, no ninth operand, no coined name. [CORRECTION: the audit pass's map gave
`dispensation` `kind` and `amount` entries; those are not `dispensation` keys (`[terms, to, at]`,
`rosters.yaml:212`).]

**One precondition revision 1 named and the audit's order omitted:** a computed `issue` is addressed to
what it is about — `terms` and `to` both bind the one referent (`loop/effects_information.py:176`) — so
every held dispensation's `terms` names its own executor, and a warrant read through the map would make
the holder detain himself. `issue` therefore joins the known-person fan for `to`, as `tell` and `give`
do, so that `terms` (the referent: the person or Record wanted) and the executor separate. It lands in
the same step.

**What it unblocks:** `detain` and `seize` (a warrant's `terms` answers `subject`); `confer`, `revoke`
and `establish` (a dispensation's `terms` naming an office answers `subject`, replacing the `office`
payload key, `predicates.py:433`); `commit` (a treaty's `terms` answers `subject`, and so does an
accusation's `terms` naming a charge, which is how a witness testifies to it, K-35); the acceptance of a
challenge (a petition's `terms` answers the acceptor's `fight` subject); H-163's docket coincidence; and,
from pass 1, `oblige`, `determine` (limit 2), `levy` (limit 3), `migrate`, `exchange`, `establish`
(`15c`). It also answers revision 1's open question about seat referents: limb 2 of `world_q.reach`
admits every live Tenure's object (`queries/world_q.py:461`), so a holder's own seat is already in reach;
what is absent is any **claim** about a seat (`verb_table.yaml:676`). The seat referent comes from a held
Record's `terms` or a `tenure.opened` deposit (K-25).

### 10.2 Faction actions mapped to person acts

Every entry of `references/action_vocabulary.yaml:32-60` (25, `status: provisional`), and the faction-
and office-scale acts it lacks, resolve to seat-holders' acts or to members' own acts counted by a Query.
*Through a seat* means `Act.via`. New verbs are in bold.

| faction action | person acts at a rung |
|---|---|
| Muster | `march`'s own `sides_of` muster; a retinue by `oblige` + `transfer`. Cohorts carry no `commit`, so no cohort ever musters — the realm's armies are named persons (`harness/populated.py:393`) |
| March | `march`; capture, interception and relocation are its stakes, read at the destination (direction 8) |
| Fortify | `build` (a garrison Site), `restore` (`fortification_of`, `world_q.py:999-1020`) |
| Blockade | a `march` that arrives at an enemy-held settlement (occupation, a Query); its larder effect is deferred (§10.4) |
| Conquest | `march` (occupation), then **`seize`** of the Rung hold under the `seizure` basis; or the holder's `release` or `give`; or death — never `revoke`, which closes seat-holds only (K-30) |
| Govern | `issue`, `levy`, `determine`, `open_case` through seats |
| Trade | `exchange` (THIN), `transfer` |
| Subsidy | `transfer` |
| Treaty | **`covenant`** + both holders' `commit` |
| Diplomacy | `tell`, `petition`, **`covenant`** through seats |
| Spy | `surveil` (a place; the Person case is deferred), **`conceal`**, and recruiting composed from `tell` and the recruit's own `oblige` (D-5 refuses a lever on a second person) |
| Investigate | the six findings + `open_case` |
| Counter-Intelligence | `surveil`, `examine`, **`seize`**, **`detain`**, `tell` (to expose) |
| Censure | `determine` under an arrangement disposing a Record (`parliamentary_debate` already does, `arrangements.yaml:114`) |
| Embargo | none-yet: deferred with its reader — it waits for code that refuses trade across two rungs, and for `proclaim` (K-34) |
| Outlawry | a person: `determine` with `disposes: ban` on the realm's seat; an organization: a `condemnation` of its Proposition — deferred |
| Excommunication | `determine` under a Church arrangement with `disposes: ban`; lifted by **`pardon`** |
| Active Inquisition | `utter` (the charge: mood `HOLDS`, subject the accused, K-35) → a `petition` whose `terms` names it, and witnesses' own `commit`s to it → `open_case` (docketing the accused) → `issue` (a warrant) → **`detain`** → **`interrogate`** → `determine` (contested) → a sentence (`oblige`, `custody` or `ban`; death is `custody` + the enforcement seat-holder's `fight`, §9.8) → **`pardon`** |
| Church Seizure | **`seize`** + `levy` |
| Recognition Challenge | `petition` + `commit` (recognition withheld or given) |
| Succession Endorsement | each endorser's own `commit` to the claimant's Proposition — the testimony channel the survey's "succession as an investigable case" asks for (§6.1, Rec 4): the claim uttered, endorsements committed, findings about it held, and a bench whose obstacle reads those commits (R-5, K-40) |
| War Authorisation | each member's own `commit` to the motion, counted by a Query (K-07), then `utter` of a `WAR`-mood Proposition and each seat's own `commit` to it, read by `faction_q.at_war` (`faction_q.py:233-236` names the fold; K-29) |
| Piety Spread | **`argue`** + `oblige` to Church seats |
| Community Organising | `found`, `oblige`, **`covenant`** (kind `alliance`, a league) |
| Martial Governance | **`detain`** and `levy` through seats; a declared emergency is none-yet: deferred with its reader and `proclaim` (K-34) |

**Acts the roster lacks, mapped the same way.** Declarations of war (`utter` of a `WAR`-mood Proposition,
then the seats' own `commit`s); edicts, interdicts and other proclamations (none-yet: deferred with their
readers, K-34); treaties and alliances (`covenant` + `commit`; truces deferred, K-32); councils (`convene` + `utter` + members' `commit`s + `determine`); tribunals
(`open_case` + `interrogate` + `determine` + `pardon`); elections and conclaves (members' `commit`s +
`confer`, basis `elected`); impeachment (a `petition` + `open_case` + `determine` on a seat-holder +
`revoke`); deposition of a seat with no rung above (none: R-4 — it ends by `release` or death); coronation
(`convene` + `confer`); sieges (a `march` that arrives at an enemy-held settlement; the siege a Query);
purges (`revoke`, `seize`, `detain`, and a death sentence as `custody` + `fight`); regency (`confer` +
term); vassalage (a seat-holder's own `oblige`, read by `purview_reaches`); raids (a won or unopposed
`march`, then `raze` or `seize` at the occupied place); a challenge to single combat (a `petition` whose `terms` is the
challenger, then the acceptor's `fight`, K-23 [CONFIDENCE: medium — nothing in a petition's content marks
it as a challenge rather than an accusation; the addressee's choice of act does]).

**Riskbreakers.** Their espionage and law work is `surveil` (a place), `conceal` (cover identity),
`seize` and `detain` under warrant, `steal` without one (R-8), `tell` to expose, and the composed
recruit; their exposure is the Query of the Exposure state (§8.1), never a stored meter.

**What was missing is the enabler, not an actor.** No row above needs a faction to act.

### 10.3 Non-act mechanics, and where each meets the season loop

These are properties of a stage, a seam or a Query — not verbs. Each is listed with where it would live.

| mechanic (source) | where it meets the loop | status |
|---|---|---|
| Inner voices, skills, the Thought Cabinet (*Disco Elysium*, *Esoteric Ebb*) | `pursuits` is a score term, projected onto the axes by `project` (`decision/choose.py:325-329`); capability supplies dice in contested acts and is not a score term | none yet for interjection |
| The case or evidence board (*Shadows of Doubt*, *Lacuna*) | the actor's own ledger + `reconstruct` | none yet for links |
| Interrogation pressure; Truth / Doubt / Lie (*L.A. Noire*) | `interrogate`'s obstacle; `teller_weight` (`options.py:1043`) | with `interrogate` |
| Exposure meters, deniability debt (corpus-rebuild; cases) | a Query over `seen` claims (§8.1) | none yet as a number |
| Quorum (Commons 40, Venetian Senate 70) | `determine`'s `quorum` conjunct; `arrangements.yaml`'s `quorum` key | partly built |
| A vote's count (parliaments, councils) | a Query over bench members' live `commit`s to the motion — no stored tally (C-7) | none yet |
| Election by lot (Venice) | a seeded draw with no actor | none yet as an arrangement key |
| Veto, reserved powers, royal assent | arrangement keys (`disposal`, `records_dissent`) | none yet for a single-member veto |
| Term limits, rotation, one per family (the Council of Ten) | `Tenure.term` on holds + a conferral basis | none yet for family limits |
| Opinion, hooks, dread, tyranny (CK3) | `Person.stance` rows; `regard` | partly |
| Secrets as stored facts (CK3) | ledger claims + `cover` Records | with `conceal` |
| Fervour, public order, world-health bands (CK3, RTK, cases) | `Site.condition` bands; Layer 1 forbids a social aggregate stored on a Rung (`architecture/meta/04_CODE_ARCHITECTURE.md:257`) | none yet at rung scale |
| Interposition and latitude (proceedings) | `interposition_kinds` (`rosters.yaml:1794`) | rostered |
| Hue and cry, frankpledge (English law) | collective liability | none yet |
| Clocks, counters, endings (cases) | MATTER's licensed clocks only; endings absent (H-176) | absent |
| Births, ageing, individuation | CENSUS; H-51 absent (`loop/census.py:30-41` generates nobody) | absent |
| Rumour spread, message loss | WITNESS channels + `Record.ttl` (no reader) | partly |
| Evidence decay (*Shadows of Doubt*) | `Claim.confidence` decaying at MATTER | built |
| A scene's time budget (*Pentiment*'s canonical hours) | `decision/budget.py` | built |
| Secrecy decay of schemes | none yet | absent |
| Thread co-movement (P-01) | the threadwork lane | deferred |
| The verification policy (the survey's Finding 1 and Recommendation 1; §6.1) | WITNESS deposits readings, never the engine's resolution (AX-7); `record()` lowers a teller contradicted by firsthand claims (`decision/options.py:1001-1040`); confidence fades at MATTER (`loop/matter.py:235-265`); `pardon`, a nested `open_case` and `release` reverse | built: reception and decay; absent: 4.5's content deposit, which must be band- and channel-mediated, never a bare `True` (`loop/witness.py:380`) |
| Agenda control: the date↔docket join (the survey's P43, *The Republic of Rome*) | CALENDAR's `date.fired` reaching WITNESS — it does not (`queries/world_q.py:1362-1367`) — and `open_case` filling the fired slot, where today it dockets with `date: None` (`loop/effects_information.py:220`) | absent — H-163 limit 4, registered |
| Approach in questioning (the survey's P9: *Lacuna*'s calm or aggressive questioning; the *L.A. Noire* remaster's Good Cop / Bad Cop) | a non-operand payload key on `interview` and `interrogate`, read by the effect or the obstacle; the subject's `regard` (`queries/person_q.py:63-69`, the stored half only) is its reader | none yet |

### 10.4 Build order

Each step lands its reader with its carrier, and each names its gate, the existing instrument that
observes it, and the conflicts it retires. Pass 1's steps (§4.1) bring the 44 up; its steps 1 and 2 are
steps 1 and 2 here.

| # | step | gate · instrument | retires |
|---|---|---|---|
| 1 | The enabler (§10.1): `record_sourced_operands`; `operand_bags` over held Records; `issue` joins the known-person fan for `to` | a held dispensation's `terms` answers `subject` in `_derive_operand`; `aperture 4 0` `confer` leaves 70/0 | K-25; H-94 in part |
| 2 | `utter` mints the utterer's hold → `commit` on Propositions. With R-3: `repudiate` cut, `_eff_release` earning `commitment.ended` on a closed `commit` and its three alignment cells re-keyed | `commit` leaves the always-refused pin (`test_season_shape.py:7624`); with R-3, `test_u7_own.py:42`'s DECLINED tuple shrinks | K-14's precondition; R-3. H-156 (a)/(b) stays registered |
| 3 | Tenure kinds `custody`, `ban`; their exclusion at `data/rosters.py:453`; the `determination` basis widened (opening any kind the exercised seat's arrangement `disposes:`; closing `custody` and `ban` only); the new `warrant` basis (opening `custody` whose object is the issuing seat, licensed by a held dispensation naming the owner); the four unseeded arrangement rows with `disposes: custody` or `ban` | the loader stays green; in `test_u7_remit.py`'s style, a determination under `disposes: ban` opens a `ban` and `release` is refused on it | K-03, K-12, K-17 |
| 4 | `determine` contested, with the party-gap fold edit | the corpus `DEGREES RESOLVED` line gains `a proposition` bands for `determine`; `Tenure.degree` is written and its `unproduced: H-162` declaration deleted | K-02; H-162 |
| 5 | `detain`, `pardon`, `interrogate` | `aperture 1 0` `detain` ex > 0; `move` refused in custody; `disposal.lifted` in `w.log`; `confession.made` in `w.log` | K-05, K-18, K-26 |
| 5a | The charge, with step 5 (§8.1): `utter` of a `HOLDS`-mood Proposition whose `subject` is the accused, named by the accusation `petition`'s `terms` through the enabler (`record_sourced_operands`); `interrogate`'s effect-side read of it; `confession.made`'s claim value its id. A computed charge waits on a `mood` source, as a computed war does (§8.1) | a hand-built charge, a witness's `commit` to it formed from the held petition, and a `confession.made` whose deposited claim's value is the charge's `prop:` id | K-35 |
| 6 | `seize`, with the `seizure` basis — object kind Record (a warrant); the Rung half lands at step 8, where its licence, occupation, lands | `record.seized` in `w.log`; a seat cannot be seized | K-04 |
| 6a | `steal` (R-8), with the `theft` basis, after `seize`, whose write and effect-side declines it mirrors | `record.stolen` in `w.log` from `populated.run` with no hand-built act; the former holder's Q2 question about the Record the next season; refused on a Record the actor holds or whose holder stands elsewhere | K-39; R-8 |
| 7 | `covenant` (kinds `treaty`, `alliance`) + `_renewals` and the `mustered` widening (allies present at a destination join the holder's side). No `war` kind (war is a Proposition, K-29); no `truce` (K-32); no `proclaim` (K-34) | allied persons appear in a march's `subject_members` (a named test in `test_mass_battle_provider.py`); tribute renewed by `_renewals` | K-11, K-14, K-29, K-32 |
| 8 | **The arrival** (§9.6's `march` row): `ENC` on `(Tenure, since)`, `(Tenure, until)`, `(Person, travel_leg)`; `sides_of` same-faction → `subject None`; the wrapper's `subject None` → `Unopposed`; H-149's refusal moved to empty `claimants`; the `muster` basis; `_relocate` taking a person; `army.arrived`; `seize` widened to Rung holds under occupation (untyped, `pardon`'s route) | in `test_march.py`: (i) `Won` (a constructed `Resolution`, since `Won` is unreachable at fixture scale, `:224-235`) and `Unopposed` at `set_s_036`/`set_s_003` leave `mustered(w, d, "fac_crown")` equal to the claimants, and `Lost` leaves them at `set_s_014` (fixture facts at `:78, :134-140, :238-239`); (ii) H-151's own falsifier (`hole_register.yaml:3293-3298`) with the expected outcome `field.unopposed`; (iii) interception: Crown relocates to a Crown-held settlement in one `_fold_one`, and a Church march on it in a second resolves `Won`/`Lost`, not `Unopposed`; (iv) `test_a_march_on_a_non_settlement_rung_refuses_h149_is_enforced` stays green; (v) the unheld-settlement test (`:196-221`) re-pinned to `field.unopposed` + `army.arrived`, and `test_declared_and_unopposed_are_no_change_directly` (`:267-274`) re-written with claimants in the `Resolution`, or it keeps passing and observes nothing (§14.8); (vi) `seize` on an occupied settlement flips `holder_faction_of` | K-27's second pair, K-28, K-30, K-33; H-151 closes; K-05 and K-08 amended |
| 9 | `sabotage` (with `work`'s declared delta restricted to ≥ 0), `tend`, `argue`, `train` (with `Person.capability` un-retired and `Person.pursuits`' declaration deleted) | condition falls with a `sabotage` among its causes; `Person.body` rises; `Person.pursuits` moves; `sigma._pool_of` varies by person | K-09, K-20, K-21 |
| 10 | `conceal` + the `anchor_of` cover read | an Event anchors on a `cover` id | K-19 |
| 11 | `raze`, licensed by occupation (the exercised seat's faction `mustered` at the settlement), after H-166's own order | `w.rungs` shrinks; a `raze` where the seat has no army is refused | K-06 |
| later | R-5, if it stands: `conferral_bases` + `inheritance`, read by CENSUS at `person.died`, the basis dispatching to a rule table on `REVOCATION_RULES`' precedent whose first rule is the designated heir (K-40) | a `person.died` followed by the designated heir's `hold` | R-5; K-40 |
| deferred | **Siege subsistence** — recommended as a new hole in `engine/season/hole_register.yaml` (not written here): what an occupying army does to a besieged settlement's larder, and its MATTER-side reader over the occupation Query (the natural site is `nearest_store`'s walk, `world_q.py:498`). No ruling states a magnitude — H-148's shape — and the arrived army are weight-1 persons who do not eat (`world_q.py:559-572`), so nothing existing carries it | — | — |

No cycle: every reader lands with or before its carrier, and `covenant` ← `commit` ← the `utter` hold is a
chain, not a loop; `seize`'s Rung half lands with the arrival that licenses it; `steal` lands after
`seize`, whose declines it reuses, and the charge with the verb that reads it. [CORRECTION: the audit
pass listed K-13 as retired at step 1; revision 2 moved it to step 7, where `war` would have landed.
Revision 3 supersedes it: no `war` Record lands at all (K-29).]

---

## 11. Suite-level invariant check

The loader invariants and rosters each new or changed row touches, and whether it passes as specified
above. "After K-nn" means the resolution of that conflict is what makes it pass.

| row | invariant or roster touched | passes? |
|---|---|---|
| `determine` (contested) | invariant 12, degree maps; invariant 9, prize `a proposition` ∈ `contest_subsystems` (`rosters.yaml:1149`); invariant 4, a contested keyed row with one refusal kind | 12 ✓, 9 ✓; 4 ✗ until K-02's fold edit (`data/verbs.py:717-720`) |
| `detain` | eligibility `remit` (`rosters.yaml:438`) ✓; prize `a standing` ✓; counterparty `subject` bound by the cell ✓; beneficiary `none` ✓; writes and emits degree-keyed; `Tenure.since` a matrix row ✓; two refusal kinds | passes after K-05 and K-02 (step 4 precedes step 5) |
| `interrogate` | prize ✓; writes and emits degree maps; beneficiary `actor` ✓; counterparty `subject` ✓; one refusal kind; no new stem | passes after K-05, K-18 |
| `seize` | counterparty empty (K-04); `Tenure.until/since` matrix rows ✓; the new `seizure` basis; from step 8 a Record-or-Rung object, untyped on `pardon`'s route (`rosters.yaml:1699-1703`) | passes after K-04 + the basis; the Rung half after step 8 |
| `pardon` | `Tenure.until` ✓; beneficiary `subject` ✓; untyped with a declared domain, as `release`; the widened `determination` basis | passes after K-03 |
| `steal` | eligibility `own` ✓; beneficiary `actor` ✓; counterparty empty (K-04); `Tenure.until/since` matrix rows ✓; `existence` of `subject` kind Record, typed; the held-by-another and co-location reads are the effect's declines, not stems (K-18); the new `theft` basis for the holder's closure (the actor's opening already passes `T-m`) | passes after K-39's basis |
| `covenant` | beneficiary `to` carriable, since the cell binds `to` (`data/verbs.py:563-575`) ✓; `Record.stages` ✓; kinds `treaty`, `alliance` rostered | ✓, built after step 2 (K-14) |
| `march` (widened) | degree maps over `field_degree_bands` ✓; one refusal kind ✓; Won/Unopposed write `Tenure.until`, `Tenure.since`, `Person.travel_leg`, whose matrix rows admit no `ENC` today (`write_matrix.yaml:225-226, :352-354, :366-368`); the gate admits no seat-authored re-home of another person's `contain` (`state/gate.py:707-757`) | ⚠ after K-33: three `ENC` cells and the `muster` basis |
| `raze` | beneficiary `none` (`data/verbs.py:528-534`); `Site.exists`/`Rung.exists` admit RES (`write_matrix.yaml:302-336`) ✓ | passes after K-06 |
| `conceal` | `own`, no precondition → an empty `emits_on_refusal` is lawful; kind `cover` rostered | ✓ |
| `sabotage` | counterparty empty (K-04); `Site.condition` ✓ | ✓ |
| `argue` | prize ✓; degree maps; `Person.pursuits`' `unproduced:` deleted (`data/verbs.py:818-821`); counterparty `to` bound by `relation of to, with` ✓ | ✓ after K-21 |
| `tend` | `Person.body` admits RES (`write_matrix.yaml:161-167`) ✓; beneficiary `subject` ✓ | ✓ |
| `train` | `Person.capability` un-retired with its producer (`write_matrix.yaml:383-386`) | ✓ after K-21 |
| `confer` (+ term) | `Tenure.term` a matrix row ✓; the `conferral` basis admits opening and `payload` only | ⚠ one gate clause: `conferral` admits `term` at opening |
| `give` (+ Rung) | `handover` is general over non-seat holds (`verb_table.yaml:398`) ✓ | ✓ |
| `survey` (+ Rung) | effect-side (`holder_faction_of`) | ✓ |
| `work` (delta ≥ 0) | an effect-side refusal of a negative declared delta in `_eff_work` (`loop/effects_economy.py:86-98`) | ✓ |

**Roster and code edits, with owner file and openness.**

| owner | edit | openness |
|---|---|---|
| `rosters.yaml` `tenure_kinds` (`:101-115`) | + `custody`, + `ban` | `open: true` |
| `data/rosters.py:453` `RELEASABLE_KINDS` | exclusion becomes {`contain`, `reside`, `custody`, `ban`}; `release`'s `domain:` unchanged | code |
| `rosters.yaml` `record_kinds` (`:164-215`) | + `treaty`, `alliance`, `cover` | `open: true` |
| `rosters.yaml` `writ_sourced_operands` (`:1571-1584`) | → the per-kind `record_sourced_operands` map (§10.1); the subset check in `data/requires.py` kept and tightened to each kind's keys | — |
| `arrangements.yaml` | the four unseeded procedure rows (`:16-21` names them) with `disposes: custody` or `ban` | — |
| `write_matrix.yaml` | delete `Person.pursuits`' `unproduced:` (with `argue`); un-retire `Person.capability` (with `train`); delete `Tenure.degree`'s `unproduced:` (with step 4); `ENC` on `(Tenure, since)`, `(Tenure, until)`, `(Person, travel_leg)` (with step 8) | — |
| `state/gate.py` | `determination` widened (§10.4 step 3); + `warrant`; + `seizure`, licensed by a warrant (Record) or occupation (Rung); + `muster` (K-33); + `theft` (K-39, R-8) — nine bases become thirteen (twelve under R-8 (b)); `conferral` admits `term` at opening | code |
| `loop/resolve.py::_party_gap_refusal` and `data/verbs.py:717-720` | the fold edit (K-02) | code |
| `loop/sides.py::sides_of`, `seam/wrappers/mass_battle.py::resolve` | same-faction → `subject None`; H-149's refusal → empty `claimants`; `subject None` with claimants and rung → `Unopposed` (step 8) | code |
| `loop/effects_combat.py::_eff_march`, `loop/effects_migration.py::_relocate` | Won/Unopposed relocate every claimant through `_relocate`, which takes the person it moves (step 8) | code |
| `verb_table.yaml` | + 12 rows; − `repudiate` (R-3); `determine`, `confer`, `give`, `march`, `survey` rows edited | — |
| `loop/effects_economy.py::_eff_work` | refuse a negative declared delta | code |
| `rosters.yaml` `remit_acts` (`:294-302`) | none | `open: true` |
| `rosters.yaml` `contest_subsystems` | none | — |
| `rosters.yaml` `conferral_bases` (`:1737-1755`) | none in the numbered steps; R-5's `inheritance` later, its rule table in `state/gate.py` beside `REVOCATION_RULES` (K-40) | `open: false` — Jordan |
| `rosters.yaml` `revocation_bases` (`:1757-1772`) | none (R-4) | `open: false` |
| `beneficiary_kinds`, `requires_operands`, `requires_forms`, `REQUIRES_STEMS` | none | closed |
| `verb_capability` (`rosters.yaml:1045-1064`) | none required | open |
| `alignment` | none: new rows take `default_cell` | — |
| `hole_register.yaml` | recommended, not written here: one new row for the siege subsistence reader (§10.4); H-151 closes with step 8 | — |

---

## 12. Conflict register

The independent audit pass's 27 conflicts in revision 1, each with its sides, severity, resolution and
CLAUDE.md §0 filter step (1 superseded · 2 irrelevant · 3 answered by a design document · 4 answered by
precedent · 5 answered by what the architecture needs), what changed in this revision, and what remains.
*Severity:* **blocks** — the proposal as written could not load or run; **weakens** — it would run and be
wrong or incoherent; **cosmetic** — a defect of wording or citation. Where the audit named no filter step,
the author assigned one. "Rev 1 §n" is revision 1's own numbering. Corrections the author made to the
audit's resolutions are §14.5. Revision 3 registers seven more (K-28…K-34, after the closing paragraph
of the audit's set): six from the march analysis and one decision of the orchestrator's; it retires
K-22, K-13 and K-27's second pair and amends K-05, K-08 and K-11, each marked in place. Revision 4
registers six more (K-35…K-40, after K-34) from the survey interrogation; it retires none.

**K-01 · ruling · blocks.** *Sides:* revision 1 (rev 1 §3.5, §9.1 item 8) escalated cutting `comply` and
splitting `evade / defy`, on the ground that the triple is Jordan's (`verb_table.yaml:737`) — against
ED-IN-0210's last row (`registers/editorial_ledger_in_archive.jsonl:178`, 2026-09-18, `status: ruled`):
*"i did not realize that meant deleting those verbs. i think that's wrong"* — the three response verbs and
`dispatch` stay. *Resolution:* retain `comply`, `evade / defy`, `construe` and `dispatch` unchanged; the
escalation closes. *Filter:* step 1, superseded by a later ruling. *Changed:* §3.1, §3.3, §3.5, §4,
Appendix A. *Residual:* whether `dispatch` and `comply` are two sides of one thing stays open under
ED-IN-0211 and is not re-derived.

**K-02 · code · blocks the `determine` widening.** *Sides:* revision 1 (rev 1 §7.5) added `contests: "a
proposition"` to `determine` — against the row, which keys its seven clauses to two refusal kinds
(`verb_table.yaml:235-242`), and the loader, which refuses a contested keyed row with more than one
(`data/verbs.py:717-720`) because `_party_gap_refusal` emits the union (`loop/resolve.py:546-553`).
*Resolution:* the seam's party gap is the counterparty clause failing; `_party_gap_refusal` emits
`row.refusal_for(COUNTERPARTY_CLAUSE)` where the row keys it, and the loader rule narrows to rows that do
not — one fold edit; `determine` keeps both kinds. *Filter:* step 5. *Changed:* §9.6, §10.4 step 4, §11.
*Residual:* none; the same edit makes `detain`'s two kinds lawful.

**K-03 · state and code · blocks the law verbs.** *Sides:* revision 1 had `pardon` close, `detain` open
and `determine` dispose `custody` and exclusion edges, and named a gate basis only for `seize` — against
the gate's nine bases (`state/gate.py:557-628`), where `determination` opens an `oblige` only (the kind is
hard-coded, `:490-492`) and may not close, `T-o` closes seat-holds only, and `T-m` admits the owner only.
*Resolution:* `determination` widened to open any kind the exercised seat's arrangement `disposes:`
(lawful once rostered, `data/arrangements.py:202-205`), on C-1 item 3's precedent
(`proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md:181-185`); its closing half admits
`custody` and `ban` only (§14.5); one new basis `warrant`, opening `custody` whose object is the issuing
seat, licensed by a held dispensation naming the owner; and `seizure` for `seize`. *Filter:* step 4.
*Changed:* §8.3, §9.1, §10.4 step 3, §11. *Residual:* none.

**K-04 · code · blocks `seize` and `sabotage` as written.** *Sides:* both named `counterparty: to` while
their cells bind only `subject` or `site`; the loader refuses an unbound counterparty
(`data/verbs.py:503-510`); and a Site cannot be held at all (`rosters.yaml:152`), so "the fabric's holder"
is nobody. *Resolution:* no counterparty on either; `seize`'s effect closes whatever `hold` the Record
carries. *Filter:* step 4 — `revoke` and `destroy_record` act non-consensually on another's edge and name
no counterparty. *Changed:* §7.1, §9.1, §9.3. *Residual:* none.

**K-05 · code · blocks `interrogate`, `detain`, `besiege` as written.** *Sides:* `interrogate` declared a
prize with a flat `writes: []`; `detain` a prize with a flat `Tenure.since` and `custody.taken`; `besiege`
a prize with a flat `Record.exists`. A contested row with a flat `writes:` or `emits:` fails the load
(`data/verbs.py:589-620`). *Resolution:* degree maps in `tell`'s shape (`verb_table.yaml:890-899`) —
`interrogate` `[]` at every band; `detain` writes on Overwhelming and Success only; `besiege` on Won and
Unopposed only. *Filter:* step 4. *Changed:* §9.1, §9.2. *Residual:* none. *Revision 3:* the `besiege`
clause is struck — `besiege` is folded into `march` (K-28), whose own degree maps already load.

**K-06 · code · cosmetic.** *Sides:* `raze` declared no `beneficiary:`; the loader requires the column on
every row (`data/verbs.py:528-534`). *Resolution:* `none`, the declaration for an act whose good accrues
to a Site or a Rung (`rosters.yaml:1652-1654`). *Filter:* step 4. *Changed:* §9.2. *Residual:* none.

**K-07 · code and proposal · weakens.** *Sides:* revision 1 said no new `remit_acts` value was needed
(rev 1 §7), then gave `commit` and `oblige` "a `remit:` alternative" (rev 1 §7.5). A `remit:<act>` is
granted only if `<act>` is on the seat's remit, checked against `remit_acts` (`rosters.yaml:302`;
`loop/resolve.py:116-117`); no `commit` or `oblige` remit act exists, and adding one is what `:298-301`
warns would close the roster by hardcoding. *Resolution:* no remit. A vote is the holder's own `commit`
and the count a Query over bench members' live commits (C-7, no stored tally); vassalage is seat A's
holder's own `oblige` to seat B (`architecture/meta/01_AXIOMS.md:1205-1218`), read by `purview_reaches`.
*Filter:* steps 3 and 4. *Changed:* §3.4, §5 (family 14), §7.2, §9.6, §10.2. *Residual:* none.

**K-08 · ruling and source · weakens; R-2 resolved in revision 3 (§13.2).** *Sides:* revision 1 said the ruling is silent on a
won `march`'s winner (`loop/effects_combat.py:277-279`); the table's note says Jordan ruled "nothing on the
WINNING side" (`verb_table.yaml:607`); ED-IN-0279's third row (`registers/editorial_ledger_in.jsonl:34`)
reads *"nothing specified for the winner"*. *Resolution:* revision 1 upheld — the ruling is silent, and
the table note overstates it (Appendix D). The decision survives the filter: R-2, recommended no winner
writes. *Filter:* survives step 5. *Changed:* §3.4, §9.7, §10.2, §13. *Residual:* R-2. *Revision 3:* the
finding stands — silence, not a ruling, for the winner — and R-2 is resolved at steps 1, 3 and 5: a won
or unopposed `march` writes occupation (the army arrives) and no hold; title moves by `seize`, `give`,
`release` or death (§13.2). What remains is R-6 (α or β) and R-7 (a routed army).

**K-09 · overlap · weakens.** *Sides:* revision 1 justified `sabotage` by "no act lowers a built Site's
condition"; `_eff_work` stages a declared delta with no sign check (`loop/effects_economy.py:86-98`), so a
hand-built `work` already does. `sabotage` and `work`/`restore` share stratum, eligibility, write row and
prize; they differ by sign and beneficiary. *Resolution:* keep `sabotage` as the signed opposite
(beneficiary `actor`, no counterparty, magnitude `_rise`'s mirror, one accumulator); restrict `work`'s
declared delta to ≥ 0 so each verb owns one sign. *Filter:* step 5. *Changed:* §3.1, §3.3, §3.5, §9.3,
§10.4 step 9. *Residual:* the thinnest pair in the suite (K-27).

**K-10 · naming and ruling · weakens; residual R-1.** *Sides:* revision 1's `execute` — (a) the word is
this repo's process vocabulary ("executed set", `ex`, `resolvable`; `requirements.yaml:674-676`), failing
§4's idempotence; (b) its write is the outcome direction 3 says a character cannot choose. *Resolution:*
survives the filter; recommended no verb — a death sentence is a `custody` disposal plus the enforcement
seat-holder's `fight` through the seam, and `person.died` arrives by degree. *Filter:* survives step 5.
*Changed:* §5 (family 28), §9.8, §10.2, §13. *Residual:* R-1; if the direct write is chosen it may not be
spelled `execute`.

**K-11 · state · weakens.** *Sides:* revision 1 proposed nineteen Record kinds. `case` is refused by
`_eff_open_case`'s own ruling (`loop/effects_information.py:196-198`); `warrant`, `summons`, `charter`
would carry `dispensation`'s exact keys `[terms, to, at]` (`rosters.yaml:212`) — a second vocabulary for
one shape (`:174-177`); `claim` collides with the `Claim` carrier and `claim.*` kinds and nothing reads
it; `interdict`, `emergency`, `embargo` are orphans by revision 1's own rule; `truce` carried `until` and
"the term as `Record.stages`" — two owners; `peace` and `treaty` are one instrument. *Resolution:* six
kinds (§8.2); a warrant, summons or charter is a `dispensation` and an accusation, demand or challenge a
`petition`, distinguished by what `terms` names. *Filter:* step 4 — revision 1's own `petition`-kinds
precedent. *Changed:* §3.3, §8, §9.2, §9.7. *Residual:* the deferred kinds wait for readers.
*Revision 3:* three kinds, not six — `war` is a Proposition (K-29), `truce` is deferred (K-32), `siege`
is a Query (K-28) — and `proclaim`, left with no kind that has a reader, is deferred (K-34).

**K-12 · state and naming · weakens.** *Sides:* revision 1 said every kind needs an opener (loader
invariant 6, `rosters.yaml:116`); openers are only REPORTED (`data/verbs.py:766`, `:831-840`) and only the
closer half fails the load (`:779-786`). And `bar`, read cold, is a tavern, the legal bar or a verb.
*Resolution:* kinds `custody` and `ban`, both added to the exclusion at `data/rosters.py:453`; `release`'s
domain unchanged; the carrier rule restated. *Filter:* step 3 for the loader fact (the code says so); §4
for the word. *Changed:* §8, and every occurrence of `bar`. *Residual:* none.

**K-13 · proposal and enabler · weakens.** *Sides:* `war {terms: a casus-belli Proposition, at, against:
a rung}` needs two operands, and non-operand keys a computed act fills with nothing
(`loop/effects_information.py:84-85`). *Resolution:* `war [terms, at]`, `terms` = `subject` = the rung
proclaimed against (`rosters.yaml:225-226`); the casus belli is a separate `commit`. One referent; no
dependence on the enabler. *Filter:* step 5, on `issue`'s shape. *Changed:* §8.2, §9.2, §10.4 step 7.
*Residual:* none. **[SUPERSEDED in revision 3 by K-29]** — there is no `war` Record to key; war is the
`WAR`-mood Proposition `at_war` already reads.

**K-14 · proposal · weakens.** *Sides:* `covenant` required an existing Proposition, and no question's
referent is one (`verb_table.yaml:773`; 802 of 802 refused, `hole_register.yaml:3521`), so it would join
the always-refused set until `utter` mints a hold; its `own` alternative let anyone mint a treaty; and its
two-sidedness was tagged to ED-IN-0210 ruling 2, which is `petition`'s withdraw/deny pair
(`verb_table.yaml:719`). *Resolution:* `remit:issue` only; built after the `utter`-hold hook; `debt`
deferred with its `seize` reader; the two-sidedness stands on its own argument, untagged. *Filter:* step
5. *Changed:* §8, §9.2, §9.7, §10.4 steps 2 and 7. *Residual:* none.

**K-15 · proposal and code · weakens.** *Sides:* revision 1 widened `tell` to an authored `said`;
`opening_set` declines a `tell` whose `said_of` is `None` because `holds` is named
(`verb_table.yaml:930-932`), and `holds` refuses content the teller does not hold. A lie needs a second
`said` source, a decision-layer change revision 1 did not name. *Resolution:* deferred; not a row edit.
The audit deferred it to H-183; the position that owns it is the telling workplan's G7 (§14.5). *Filter:*
step 3 — a live plan already owns it. *Changed:* §3.4, §5 (family 37), §9.7. *Residual:* G7.

**K-16 · proposal and canon · weakens.** *Sides:* revision 1's `surveil` → Person: the grammar has no
disjunction (`rosters.yaml:1699-1703`), so its own row said "a sibling row" while headed "no new verb";
and a seventh investigation row breaks canon's *"No new action vocabulary"* and Jordan's six-as-six
(`verb_table.yaml:950-960`). *Resolution:* hold until an `any` combinator is ruled — `release` is the other
cell waiting for one (`verb_table.yaml:753`), and two cells then justify it; register on ED-FI-0009.
*Filter:* step 3. *Changed:* §3.4, §5 (family 4), §9.7, §10.2. *Residual:* the combinator ruling.

**K-17 · internal · weakens.** *Sides:* `detain` opened `custody` "prisoner → holding seat" via
`remit:dispatch`; `pardon` needed the edge's object to be the exercised seat under `remit:determine`. An
enforcement seat's custody could never be pardoned by the bench. *Resolution:* `custody`'s object is the
seat that issued the warrant, read off the held dispensation; the enforcement seat acts `via` but does not
own the edge; "relaxation to the secular arm" is a second `detain` under a second bench's warrant.
*Filter:* step 5. *Changed:* §8.1, §9.1. *Residual:* none.

**K-18 · proposal · cosmetic.** *Sides:* `interrogate`'s "new stem `held_in_custody`"; `REQUIRES_STEMS`
is closed and refuses an unknown stem at load (`data/requires.py:708-711`, `:836-842`). *Resolution:* the
custody read is the effect's decline, `interrogation.refused`. *Filter:* step 4, `_req_oblige`'s negation
precedent. *Changed:* §9.1. *Residual:* none.

**K-19 · proposal · weakens.** *Sides:* `conceal`'s success emission "withheld from `co_located`" is a
per-verb exception in `witness_channels`' precedence (`rosters.yaml:398-405`) — scripting drift.
*Resolution:* no channel exception; `state/attribution.py::anchor_of`, at tier 1, answers the cover
Record's id for an actor holding a live `cover`, and every reader downstream is unchanged. *Filter:* step
5. *Changed:* §9.3. *Residual:* none.

**K-20 · proposal and canon · weakens.** *Sides:* `train` writes `Person.capability`; P-08
(`canon/02_canon_constraints.md:50`) forbids non-sensitives gaining Thread-level capability by study.
*Resolution:* the capability raised ranges over the names `verb_capability` maps (`rosters.yaml:1061-1064`);
Thread Sensitivity has no carrier (H-85, `hole_register.yaml:1052-1054`) and so is structurally outside;
the row records the exclusion. *Filter:* step 3. *Changed:* §9.4. *Residual:* cross-lane observation, not
ruled here — GD-2 (`canon/02_canon_constraints.md:72`) presupposes a faction selecting actions, against
AX-1 (Appendix D).

**K-21 · proposal and code · cosmetic.** *Sides:* `argue` writes `Person.pursuits`, whose matrix row
declares `unproduced: H-62` (`write_matrix.yaml:193`), and the loader refuses a stale declaration
(`data/verbs.py:818-821`); `train`'s row is in `retired:` (`write_matrix.yaml:386`). *Resolution:* delete
the declaration and un-retire the row in the same commit as each producer. *Filter:* step 4 — the
matrix's own discipline, "a row exists because a producer produces it". *Changed:* §9.4, §10.4 step 9,
§11. *Residual:* none.

**K-22 · order · weakens. [RETIRED in revision 3 — moot: `besiege` is folded into `march` (K-28), and
the subsistence reader, never buildable as written (§14.8), is deferred as a new hole (§10.4).]**
*Sides:* revision 1's build step 8 landed `besiege` with no reader, against
its own rule that each step lands its reader with its carrier; `siege`'s readers appeared only as
blockers. *Resolution:* step 8 is `besiege` with the MATTER subsistence reader; `raze` waits on H-166's
own order (`hole_register.yaml:3651-3652`). *Filter:* step 4. *Changed:* §10.4. *Residual:* none.

**K-23 · ruling and proposal · weakens.** *Sides:* revision 1 left `challenge` → `accept` pending; an
`accept` carrying `contests: "the body"` (`proposals/2026-09-20-pursuit-basis-worksheet.yaml:155-156`)
would be a second door to the duel engine beside `fight` (`seam/contest.py:154-169`, as cited by pass 1).
*Resolution:* a `petition` whose `terms` is the challenger; the acceptor `fight`s the person the held
Record names. No new verb. [CONFIDENCE: medium] *Filter:* step 4, `petition`'s kinds-as-data. *Changed:*
§2, §3.4, §4, §5 (family 55), §10.2. *Residual:* what marks a petition as a challenge rather than an
accusation (§10.2).

**K-24 · naming · cosmetic.** *Sides:* revision 1 proposed `dispatch` → `order`; `order:` is an
`arrangements.yaml` key (`:95`, `:112`) and the fold's order key — a §4 failure — and ED-IN-0210 keeps
`dispatch`. *Resolution:* keep `dispatch`; defer the `carry` and `succeed` renames until each row gains
its operand (one hash move, paid once); split `evade / defy` and `tie / knot` only when built (openers
derive per `Tenure(...)` literal, `rosters.yaml:116-131`). *Filter:* step 4 and §4. *Changed:* §3.1,
§3.5, Appendix A. *Residual:* none.

**K-25 · document vs code · cosmetic.** *Sides:* revision 1's [GAP] "whether `world_q.reach` admits an
office id". Limb 2 admits every live Tenure's object (`queries/world_q.py:461`), so a holder's seat is in
reach; what is absent is any claim about a seat (`verb_table.yaml:676`). *Resolution:* the seat referent
comes from a held Record's `terms` (the enabler) or a `tenure.opened` deposit. *Filter:* answered by the
code — a fact, not a decision. *Changed:* §4, §10.1. *Residual:* none.

**K-26 · internal · cosmetic.** *Sides:* four contradictions inside revision 1 — "parties are always
seat-holders" against its own custody, cover and debt states; the cross-check "`detain`, `seize`,
`execute` and `pardon` share eligibility", false (`dispatch`, `issue`, `determine`); WIDENED 9 → 8
against "10 widened"; and "expulsion waits on H-159's fixture", whereas `oblige_term = 4` is shipped
(`data/fixtures.py:694`) and only the control arm never matures. *Resolution:* each corrected. *Filter:*
facts. *Changed:* §5, §8, §9.5, §9.6. *Residual:* none.

**K-27 · overlap · [NULL].** Pairwise over the resolved suite, every pair differs on counterparty, prize,
write row or object kind. The two thin pairs are `sabotage`/`work` (sign) and `besiege`/`march` (write row
only, same step and prize). Named rather than hidden. *Changed:* §3.3, §9.5. *Revision 3:* the second
pair is retired with `besiege` (K-28); `sabotage`/`work` is the one thin pair.

**Revision-1 proposals withdrawn that the audit did not register as conflicts.** The audit's roster
retains `speak` and `work`, and revision 1 had proposed cutting both (rev 1 §3.5 and §9.1 items 5 and 7). The
author reads the roster as withdrawing them: `speak` does something no other row does — speech that binds
no hearer — and executes; `work` keeps the positive sign once K-09 restricts it. Neither redundancy
argument survives once each row owns a distinct act, and cutting a ruled §E3 row on a thin redundancy is
what ED-IN-0210's reversal warns against. Revision 1's [DISAGREE] on `interrogate`'s finding emissions is
resolved on the confession side (§9.1, `rosters.yaml:1031`). Revision 1's own earlier withdrawals stand:
the `revoke` widening to expel a member (D-5) and the second outlawry carrier.

**Registered in revision 3.** K-28…K-33 are the march analysis's, checked against the code by the author
(§14.8 lists where they were corrected); K-34 is the orchestrator's.

**K-28 · direction vs proposal · blocks `besiege`.** *Sides:* revision 2's `besiege` — same prize, step,
eligibility, cell and sides as `march`, differing only in writing a `siege` Record on `Won` — against
direction 8 (the stake is derived at the destination) and direction 3's principle (a verb that declares
its intended outcome is an outcome, not a choice). And `march` today moves nobody: `_eff_march` writes
`body` and `stance` only (`loop/effects_combat.py:345-370`), so capture, interception and relocation are
inexpressible or conflated. *Resolution:* `besiege` folds into `march`; a won or unopposed march
relocates the army (`_relocate`'s pair), and the stake is read from `holder_faction_of` against the seat's
faction and `mustered` at the destination (§9.6). A siege is a Query over an arrived opposing army, not a
Record: a `siege` Record minted at ENCOUNTER would need `(Record, exists)`, which admits `RES` only
(`write_matrix.yaml:252-254`), widened to carry a fact the `contain` edges already state — two homes for
one relation (§0.05 clause 3; `04_CODE_ARCHITECTURE.md:910`, D-10). *Filter:* step 1 (a later direction)
and step 5. *Changed:* §2, §3.2, §3.3, §5 (families 24, 25), §7, §8.1, §8.2, §9.2, §9.5, §9.6, §9.7,
§10.2, §10.4 steps 8 and 11, §11, Appendices A and B. *Residual:* the siege's larder effect, deferred as a
new hole (§10.4).

**K-29 · code vs proposal · weakens `proclaim` and `covenant`.** *Sides:* revision 2's Record kind `war`
(§8.1, §8.2; K-13) against the war the tree already carries — a `WAR`-mood Proposition plus live
`commit`s, read by `faction_q.at_war` (`queries/faction_q.py:208-250`; `01_AXIOMS.md:1374-1384`;
*"NEVER a stored flag"*). *Resolution:* no `war` Record; war is uttered and committed; peace is each
committed person's `release`. No march gate: refusing a march on `at_war` would refuse every capture
attempt, since `at_war` is measurably `False` for every pair in every built world (`faction_q.py:232-242`),
and a march may not mint a war, since `Proposition.exists` has one writer, `utter`
(`write_matrix.yaml:245-250`). *Filter:* step 3 (the axioms) and step 4 (built precedent). *Changed:* §2,
§3.4, §5 (family 21), §7.1, §8.1, §8.2, §9.2, §10.2, §10.4 step 7. *Residual:* observation for the FA lane —
`treaty` and `alliance` could take the same shape (§8.2).

**K-30 · code vs proposal · cosmetic but load-bearing.** *Sides:* revision 2's "title moves by … a seat's
`revoke`" (§3.4, §10.2, §13.2, Appendix A) against the code: `_req_revoke` requires `obj in w.offices`
(`loop/predicates.py:432-444`) and `T-o` admits a closure of a `hold` on a seat only (`state/gate.py:589-590,
:751-754`). A rung `hold` ends by its owner's `release` (`hold` is releasable, `data/rosters.py:453`), by
death's cascade, by `give` (once widened to a Rung, §9.6), or by the suite's `seize`. *Resolution:* each
site corrected. *Filter:* a fact. *Residual:* none.

**K-31 · measurement vs proposal · weakens §4.** *Sides:* revision 2's "hooked in the realm (16/16)"
against H-149's own measurement: the realm declares 11 marches in one `populated.run(4, 0)` and ENCOUNTER
refuses all 11 at H-149's check — 9 target a `hearth`, 2 a `person`-kind rung
(`hole_register.yaml:3148-3156`; `requirements.yaml:1020-1023`); the 16/16 pair's own note calls its
`both` column "a two-Event convention" (`requirements.yaml:674-676`). *Resolution:* declared 16, fought 0;
a realm count is a fake control for any stake split until H-149's and H-175's referents move (CLAUDE.md
§7). *Filter:* a fact (§0.1 pt 3, row 2). *Changed:* §4, §14.1, Appendix A. *Residual:* none.

**K-32 · the suite's own rule vs the truce row.** *Sides:* "a kind ships only with its reader" (§8)
against `truce`, whose only proposed reader was a `march` refused or flagged between truced seats.
Refusal contradicts direction 8 — breaking a truce is a choice with consequences — and a flag has no
mechanism, because emits are keyed per band (`hole_register.yaml:3309-3313`). *Resolution:* `truce`
deferred with its reader. *Filter:* step 5. *Changed:* §5 (family 22), §7, §8, §9.2, §9.7, §10.1, §10.4
step 7. *Residual:* `truce` returns with a reader.

**K-33 · gate vs the relocation write.** *Sides:* direction 8 ("sent to a location") against the gate's
nine bases, none of which admits a seat's act re-homing another person's `contain`
(`state/gate.py:707-757`: `T-m` needs the actor to own the edge; `handover` is `hold` only; `cascade` and
`founding` are causation-bound; `T-o`, `conferral`, `renewal` and `determination` read seats or
`oblige`). *Resolution:* a tenth basis, **`muster`** [CONFIDENCE: medium on the name — `dispatch` is both
the remit act and a verb, so the ordinary word that already names the query, `mustered`, is the safer
choice under CLAUDE.md §4]: a `contain` re-home — one closure and one opening on the same Person subject
in one write, judged across the batch as `handover` is (`gate.py:660-669`) — by a seat in `Act.via` the
actor sits in, whose grant carries `dispatch`, for a subject whose `faction_holding` is the seat's
faction. Nothing else: no `hold`, no other kind. Authority-bound like `T-o`. Whether a mustered person may
refuse is pre-existing in `sides_of` and not opened here. *Filter:* step 4 (a basis per plan position:
five were added after the first enumeration, `04_CODE_ARCHITECTURE.md:564-586`) and step 5. *Changed:*
§4, §9.6, §10.4 step 8, §11. *Residual:* none.

**K-34 · the suite's own rule vs `proclaim` · blocks `proclaim`. [THE ORCHESTRATOR'S DECISION — a human
may overrule it.]** *Sides:* with `war` a Proposition (K-29) and `truce` deferred (K-32), `proclaim` is
left with no Record kind that any code reads — edict, embargo, interdict, emergency and condemnation were
already deferred as orphans (K-11) — against the suite's rule that a kind ships only with its reader (§8)
and that each build step lands its reader (§10.4). *Resolution:* `proclaim` deferred from the suite with
its readers, as `thread_read` and `debt` are; a declaration of war is `utter` of a `WAR`-mood Proposition,
then the seats' own `commit`s. **Every site that leaned on it, checked:** the faction map's Embargo,
Martial Governance and War Authorisation rows and its declarations line (§10.2) — re-pointed or marked
none-yet; Censure (`determine`) and Recognition Challenge (`petition` + `commit`) never named it; G14 and
the roster (§3.2, §7.1); the NOT entries of `issue`, `speak` and `utter` (§3.4); `covenant`'s composition
(§9.2); the states table (§8.1); build step 7 (§10.4); the invariant and roster-edit tables (§11);
Appendices A and B. One possible dependency was examined and does not hold: `_ch_chronicle` would
broadcast a `proclamation.made` as a `binding_decision` emission (`epistemic.py:553-554`), but that reads
the Event, not a Record's state, and revision 2 already deferred edict, embargo, interdict and emergency
though that broadcast would have carried them (K-11). No dependency found makes the deferral wrong.
*Filter:* step 5 (CLAUDE.md §0). *Changed:* the sites listed. *Residual:* `proclaim` returns with its
first kind that has a reader.

**Registered in revision 4.** K-35…K-40 are the survey interrogation's, checked against the code by the
author (§14.9 lists where they were corrected).

**K-35 · the charge has no carrier · weakens `interrogate`, the contested `determine` and Rec 4.**
*Sides:* K-11 makes an accusation a `petition` whose `terms` is the accused; `determine`'s `party`
conjunct dockets a Person (`verb_table.yaml:210-229`); `interrogate` contests `a proposition` and the
contested `determine` grades one (§7.1) — yet no Proposition says *what* is charged, and `confession.made`
carries nothing. *Resolution:* the charge is an uttered Proposition of mood `HOLDS` whose `subject` is the
accused (`Proposition(pid, mood, subject, predicate, value)`, `loop/effects_information.py:467-468`); the
accusation `petition`'s `terms` names it through the enabler (§10.1); testimony and endorsement are
`commit`s to it; `confession.made`'s claim value is its id; the docket stays person-keyed, and
`interrogate` and the contested `determine` reach the charge at the effect through the Proposition whose
`subject` is the party. *Filter:* step 4 — war (K-29) and subordination take this shape, and an oath is an
utterance (`01_AXIOMS.md:1399-1403`). *Changed:* §3.4, §7.2, §8.1 (Charge, Accusation pending), §9.1,
§9.6, §10.1, §10.2, §10.4 step 5a, Appendices A and B. *Residual:* a computed charge needs a `mood`
source (§8.1, §14.9); observation for the SC lane that the bench's obstacle should read the commits.

**K-36 · `interview` vs the F8 carve-out.** *Sides:* 4.5's "claims graded by degree", read as a roll on
the asker, would deposit content from the questioned person's ledger, which the fold may not read — the
carve-out admits a resolver-side read of the actor's own ledger and no other (`verb_table.yaml:1048`;
`04 §B.2`). *Resolution:* `interview` is a prompt: it emits, the questioned person witnesses it by
presence (`epistemic.py:322`), Q2 raises their question, and they answer by their own `tell` from what
they hold — testimony reaching self-knowledge is AX-7's own clause (`01_AXIOMS.md:285-287`). No degree on
the asker. *Filter:* step 3. *Changed:* §3.3, §3.4, §4.1, §6.3, Appendix A. *Residual:* none; ED-FI-0009
carries the investigation rows (§13.8).

**K-37 · 4.5's `Failure` vs canon's false lead.** *Sides:* 4.5 says Failure deposits nothing
(`verb_table.yaml:985-987`); canon grades Failure as a false lead and a failed `reconstruct` as a wrong
conclusion the player acts on (`:972-973`, `:1115`). *Resolution:* a false lead is a claim with a wrong
value, which needs a value space nothing supplies; until one is ruled, deposit nothing — no invented
number. *Filter:* step 5. *Changed:* §3.3, §4.1, §6.3, Appendix D (r). *Residual:* the value space,
already ED-FI-0009's.

**K-38 · the hostage `[GAP]` in §8.1.** *Sides:* revision 3's hostage row asked how a covenant stands in
for the warrant the `warrant` basis reads. *Resolution:* it need not: the hostage `move`s to the
receiving seat, that seat's holder `issue`s a warrant naming him, `detain` opens `custody`, and `pardon`
ends it on performance — a composition on four existing or suite verbs, no new carrier and no
covenant-as-warrant basis. *Filter:* step 4 (the `warrant` basis unchanged). *Changed:* §5 (family 26),
§8.1, §14.1, Appendix B. *Residual:* none.

**K-39 · theft unhoused.** *Sides:* three extraction rows — *Esoteric Ebb*'s "steal anything in sight"
[G1-38], *Shadows of Doubt*'s stolen document [G1-98], CK3's steal-an-artifact scheme [G2-26] — reach no
family, and family 30's "taking a Record without consent" [C-08] is answered only by a warrant-bound
`seize`. *Resolution:* family 62 and `steal` (§9.3) with a `theft` gate basis. *Filter:* survives step 5
— R-8. *Changed:* §2, §3.2–§3.4, §5, §7.1, §7.2, §9.1, §9.3, §9.5, §9.7, §10.2, §10.4 step 6a, §11,
Appendix B. *Residual:* R-8.

**K-40 · P47, succession law.** *Sides:* R-5 proposes one basis, `inheritance`; the survey's primitive
(from CK3) is a **law** that selects among rules for who inherits. *Resolution:* the basis dispatches to a
rule table on `REVOCATION_RULES`' precedent — a roster naming the basis, the rule living once in code, and
an import-time refusal if either side lacks the other (`rosters.yaml:1767-1771`); the first rule, the
designated heir, ships with R-5, and a law selecting among rules is a second value in the same table.
*Filter:* step 4; the roster is Jordan's (`open: false`). *Changed:* §10.4 ("later"), §11, §13.5.
*Residual:* R-5, extended.

---

## 13. Residual decisions

Five decisions survive all five filter steps (R-1, R-3, R-4, R-5, R-8): in each, two defensible options
lead to materially different games, or the answer amends a closed roster or a ratified row. **The suite
carries the recommended option in each. Every recommendation is Jordan's to overrule**, and each entry
says what the other option would change. R-2 is resolved in revision 3 inside the filter and is kept
here with what its alternative would change; it leaves two one-line residuals (§13.6). No ledger row
was written for any of them.

### 13.1 R-1 — `execute`: judicial death by direct write, or only through the combat seam?

- **(a)** A `remit:dispatch` verb writing `Person.exists` (the kill cascade, `loop/effects_combat.py:126-129`
  as cited by pass 1) on a prisoner under a death disposal.
- **(b) — recommended, carried in the suite.** No verb. A death sentence is a `custody` disposal plus the
  enforcement seat-holder's `fight` against the prisoner through the seam; `person.died` arrives by degree.
- **Why (b):** it keeps direction 3 whole — no character chooses an outcome — avoids the name collision
  with the repo's "executed" vocabulary (§4), and makes a botched execution a story.
- **What (a) would change:** benches gain certain death, and the suite a thirteenth new verb (56 in all),
  spelled something other than `execute`, with a disposal kind carrying "death" that no carrier has today
  [GAP]; §5 family 28 moves from OUTCOME to GAP; §9.8 and §10.2's Active Inquisition row change.

### 13.2 R-2 — does a won `march` write the winner's side? (resolved in revision 3)

**Resolved, at filter steps 1, 3 and 5.** A won or unopposed `march` writes the arriving army's presence
— `_relocate`'s pair for every claimant, under the `muster` basis (K-33) — and nothing on any hold.
ED-IN-0279's third row (`registers/editorial_ledger_in.jsonl:34`) fixes the loser's writes, *"casualties
only, decrease in morale, and a grudge token"*, and its "nothing else" stands; direction 8 names stakes,
not writes, and its own words — "sent to a location" — require the arrival (step 1, not contradicted;
step 5). `04_CODE_ARCHITECTURE.md` §C.5.1 types holdings as what a defeat can cost (`04:794`), and
`01_AXIOMS.md` §E.1.6 separates title from ground (step 3). Title moves by `seize` of the Rung hold under
the `seizure` basis licensed by occupation, by `give`, by `release`, or by death — not by `revoke`, which
closes seat-holds only (`loop/predicates.py:432-444`; `state/gate.py:751-754`; K-30). Every change of
title stays an authored act (AX-6, `01_AXIOMS.md:199`: *"nothing becomes permanent without an author"*),
and `seize` under occupation is the first route by which a hold whose banner nobody carries becomes
contestable (T-h (b)'s standing debt, `01_AXIOMS.md:474-480`).

- **(α) — Jordan may rule it instead.** A won field transfers title directly. What α changes: war becomes
  decisive in one season; ED-IN-0279 row 3's "nothing else" on the loser is amended; `_eff_march` carries
  the `seizure` licence itself — without it, `T-m` would admit a first capture as the actor opening a
  non-seat `hold` for himself (`gate.py:707-710`) and refuse every recapture on the non-owner's close; the
  faction map's Conquest row and §9.7's family 25 become "a won march".
- **(β) — carried in the suite.** Occupation, then `seize`. It changes nothing ruled.
- **What revision 2 said, corrected.** Its option (a) "needs a fifth lawful non-owner Tenure write,
  amending ratified §C.2" is overtaken: five bases were added after that enumeration, each by a plan
  position (`04_CODE_ARCHITECTURE.md:564-586`), so adding one is precedent, not re-ratification (§14.7).

### 13.3 R-3 — cut `repudiate`?

- **(a)** Keep it: a ratified §E3 row that closes one's own `commit`.
- **(b) — recommended, carried in the suite.** Cut it. `release` already closes a `commit` — its domain
  lists it (`verb_table.yaml:748`) and the row's own note says so (`:773`). `_eff_release` earns
  `commitment.ended` on a closed `commit` (precedent: per-subject event kinds,
  `effects_governance.py:90-91`), so vow-breaking stays witnessable and the three alignment cells that
  price it (`rosters.yaml:2158, :2194, :2232`) re-key on the event kind.
- **Why (b):** one edge, one closer.
- **What (a) would change:** two closers of one edge stay; the suite is 56 verbs; build step 2 loses its
  second half.

### 13.4 R-4 — may a seat with no rung above be deposed by rule?

- **(a)** Add a `revocation_bases` member — the roster is `open: false` with one value "because one rule
  was ruled" (`rosters.yaml:1757-1772`).
- **(b) — recommended, carried in the suite.** No basis. A top seat ends by `release` or death. A `ban`
  from a bench with purview refuses its holder new service and seating (its readers, §8.1) but does not
  itself close a live seat-hold — so a banned King keeps his seat until he releases it or dies, and the
  pressure runs through reception.
- **Why (b):** a basis would make the King revocable by rule.
- **What (a) would change:** the top of every ladder becomes revocable; `revoke`'s NOT list and the
  deposition row of §10.2 change.

### 13.5 R-5 — succession as a conferral basis?

- **(a)** Leave `conferral_bases` closed at appointed, elected, annex (`rosters.yaml:1737-1755`, `open:
  false` — "a fourth way to fill a seat is a design change, not a table edit", `:1745`).
- **(b) — recommended, carried in the suite as a later step.** A fourth member, `inheritance`, read by
  CENSUS at `person.died`, so the edge `succeed` opens fills the vacancy. The fill is authored by the
  designation, so it adds no fourth way the world moves by itself (AX-5, `01_AXIOMS.md:164`).
- **Why (b):** without it `succeed` stays a carrier nobody reads.
- **What (a) would change:** `succeed` stays THIN indefinitely and dynasties stay unbuilt; the "later"
  row of §10.4 drops.
- **Extended in revision 4 (K-40), not a new decision.** The survey's succession law (P47, from CK3) is a
  law that selects among rules. `inheritance` therefore needs a rule, and the basis dispatches to a rule
  table on `REVOCATION_RULES`' precedent (`rosters.yaml:1767-1771`: the roster names the basis, the rule
  lives once in `state/gate.py`, and the import refuses a basis without a rule or the reverse). The first
  rule is the designated heir; a law selecting among rules is a second value in the same table, and
  equally Jordan's roster.

### 13.6 R-6 and R-7 — one line each, not blockers

- **R-6.** Does ED-IN-0279 row 3's "nothing else" on the loser survive capture named as a stake — β,
  occupation then `seize` (carried) — or should a won field transfer title directly, α (§13.2)?
- **R-7.** [ASSUMPTION] A routed army (`Lost`) stays at its origin rather than arriving; the alternative
  puts a beaten force in occupation of the field (§9.6).

### 13.7 R-8 — `steal`: may a person take what another holds, with no licence?

- **(a) — recommended, carried in the suite (revision 4; the orchestrator adopted the survey
  interrogation's recommendation).** Build `steal` (§9.3) with a `theft` gate basis: uncontested, fully
  witnessed, priced by reception and by what follows — a `petition`, a warrant, a `detain`.
- **(b)** Possession is sacrosanct: a held thing moves only by consent (`give`), by a warrant or
  occupation (`seize`), or by its holder's end.
- **Why it survives the filter.** Steps 1–4 are silent: no ruling; family 30's demand is live; no design
  document chooses; and the gate's precedent cuts both ways — bases are added per plan position
  (`04_CODE_ARCHITECTURE.md:564-586`), yet every basis so far is bound to the owner's own act, a seat's
  authority or causation (`state/gate.py:557-628`), and `theft` would be the first bound to none. Step 5
  splits: both architectures are sound and give materially different games — one where a Riskbreaker can
  lift a text and the holder's recourse is law, one where documents move only by law.
- **Why (a):** it gives the covert half of the survey's Finding 3 — the finder can take, not only see —
  a carrier, and three demand rows a family.
- **What (b) would change:** `steal` leaves the suite (55 → 54 verbs, 12 → 11 new, 56 → 55 roster rows,
  13 → 12 gate bases, new `own` verbs 6 → 5); family 62 stays GAP with no verb; the three extraction rows
  [G1-38, G1-98, G2-26] and the Church's "text suppression" portfolio (`rosters.yaml:1536`) keep no covert
  route to a document; and the espionage layer is one in which the finder can never take.

### 13.8 Already registered — no new row

- **H-156's (a)/(b)** decides `destroy_record`'s held shape, the `found`/`build` formation policy and
  `commit`'s cost.
- **J-4** decides the works channel behind `build`, `found` and `work`.
- **H-94** reserves the coining of `exchange`'s counterparty operands (`rosters.yaml:1562-1564`).
- **ED-IN-0211** holds whether `dispatch` and `comply` are two sides of one thing.
- **H-166** carries its own design order for ending a place (cost, holder, closer), before `raze`.
- **H-101** carries vassalage's reader, `purview_reaches`.
- **The telling workplan's G7** carries the lie; **ED-FI-0009** the investigation rows, including
  `surveil`'s Person case and the value space a false lead needs (K-37).
- **H-163 limit 4** carries the date↔docket join the survey's agenda control needs (§10.3).

### 13.9 Answered here, not escalated

| question | answer | step |
|---|---|---|
| Does direction 3 close the `kill`/`wound` split pending at `verb_table.yaml:446-448` and `:467`? | Read as yes [ASSUMPTION — Jordan to correct] | 1 (a later direction) |
| Cut `comply`; split `evade / defy`? | No; retained unchanged | 1 — ED-IN-0210's 2026-09-18 row (K-01) |
| What may `pardon` close? | `custody` and `ban` only, never an `oblige` | 4 — `revoke`'s precedent; D-5 governs obligations (`verb_table.yaml:757`) |
| May the widened `determination` basis close an `oblige`? | No — `custody` and `ban` only | 1 — D-5 stands |
| May `revoke` close a member's `oblige` (expulsion)? | No; expulsion is withheld renewal and lapse | 1 — D-5 stands |
| May `interrogate` emit findings by degree? | No; its contest disposes the charge (`confession.made` / `confession.withheld`) | 3 — `rosters.yaml:1031` |
| One carrier or two for outlawry? | One per target: a person's is a `ban`; an organization's is a `condemnation` of its Proposition, deferred | 5 — two ladders for one state is an S defect (§0.06) |
| Are `custody` and `ban` releasable by their holder? | No; excluded from `RELEASABLE_KINDS` | 4 — the `contain`/`reside` precedent (`data/rosters.py:448-453`) |
| May the enabler coin operand names? | No; it maps content keys onto the closed eight | 3 — r2's "I do not coin a ninth operand" (`rosters.yaml:1582`) |
| Does a vote need a remit? | No; a vote is the holder's own `commit`, the count a Query | 4 — K-07 |
| New Record kinds for warrants, accusations, cases? | No; a `dispensation` or `petition` by its `terms`; `case` is refused by the effect's own ruling | 4 — K-11 |
| May anyone mint a treaty? | No; `covenant` is `remit:issue` only | 5 — K-14 |
| `speak` and `work`: cut? | No; retained, THIN | 4 — each owns a distinct act (§12) |
| A siege: a verb, a Record, or a Query? | A Query over an arrived army; `besiege` folds into `march` | 1 and 5 — direction 8 (K-28) |
| Does a march need a war? | No; `at_war` gates no verb, and war is an uttered Proposition the tree already reads | 3 and 4 (K-29) |
| Is `proclaim` in the suite? | No; deferred with its readers — no kind it would mint has one | 5 — the orchestrator's decision, overrulable (K-34) |
| What is Valoria's verification policy? | Consequence-tested submission over held truth, with hidden reliability grading of evidence at production, and judgment of a Proposition as probability (§6.1) | 3 and 4 — AX-2, AX-3, AX-7, T-j; `record()`; 4.5's own text |
| Approach in questioning: verbs or data? | Data — a non-operand payload key on the one row | 4 — `mood` on `utter`; six-as-six (`verb_table.yaml:950-960`) |
| Is `interview` a graded finding? | No; a prompt the questioned person answers by their own `tell` | 3 — the F8 carve-out (K-36) |
| What carries the charge? | An uttered `HOLDS` Proposition whose subject is the accused | 4 — war's shape; an oath is an utterance (K-35) |
| How is a hostage held? | `move` + `issue` + `detain` + `pardon`; no new carrier | 4 — the `warrant` basis unchanged (K-38) |
| What does 4.5's Failure deposit? | Nothing, until a value space is ruled | 5 — no invented number (K-37) |
| Should the contested bench's obstacle read testimony? | Yes, as an observation for the SC lane; not built here | — ED-SC-0033 cl. 3 names the owner |
| The survey's shared loss (P44), P-03's "GM is the rendering engine", GD-2's faction that selects | observations for the FA, WR and canon lanes; not acted on | — (Appendix D, f, n) |

---

## 14. Provenance and falsifiers

### 14.1 What would show each proposal hooked

Every observable below is read by an instrument that exists: `harness.corpus_run`, `harness.aperture`,
`w.log` from `populated.run`, or a test file named. None has been run against a proposal; all are unbuilt.

| item | observable |
|---|---|
| `detain` | `aperture 1 0` ex > 0; `move` refused for a person holding a live `custody` edge |
| `interrogate` | the corpus `DEGREES RESOLVED` histogram gains this prize's bands; `confession.made` in `w.log` |
| `seize` | `record.seized` in `w.log`; realm ex > 0; a seat cannot be seized |
| `steal` (R-8) | `record.stolen` in `w.log` from `populated.run` with no hand-built act; the former holder's Q2 question about the Record the next season; refused on a Record the actor holds or whose holder stands elsewhere |
| the charge (K-35) | a `confession.made` whose deposited claim's value is the charge's `prop:` id; a witness's `commit` to that id, formed from a held petition |
| the six findings' producers (§6.3) | a `finding.made` claim with a non-trivial value — for `research`, the Record's content; for `examine` and `surveil`, `Seen` terms of a past Event at the place; a bare `True` (`loop/witness.py:380`) is the failure |
| `pardon` | a `custody` edge closes with `disposal.lifted`; the next season's `move` is admitted |
| `covenant` | the addressee's `commit` to the covenant's Proposition in `w.log`; an ally's persons in a march's `subject_members` |
| `march` (arrival) | the step-8 tests in `test_march.py` (§10.4): `mustered(w, d, f)` equals the claimants after `Won`/`Unopposed`, and the origin keeps them after `Lost`; an interception resolves `Won`/`Lost`, not `Unopposed`; H-149's refusal stays green. At realm scale, a named test over `populated.run`/`build_realm(0)` reading `w.log` (`test_build_realm_determinism.py:104-116`'s precedent) counts `army.arrived` and splits it by stake through `w.acts` (`causes` → act → `subject` → `holder_faction_of`) — expected 0 today, since the realm fights no field (K-31), so it proves nothing either way until H-149's and H-175's referents move |
| `raze` | `w.rungs` shrinks |
| `conceal` | an Event's anchor resolves to a `cover` id |
| `sabotage` | `Site.condition` falls at RESOLVE with a computed `sabotage` among its causes |
| `argue` | `Person.pursuits` moves (a RES row with no writer today) |
| `tend` | `Person.body` rises |
| `train` | `sigma._pool_of` varies by person |
| `determine` (contested) | `DEGREES RESOLVED` gains `a proposition` bands for `determine`; `Tenure.degree` written |
| `confer` (+ term) | a seat-hold opens with a `term` and an act executes `via` it under a regent |
| `give`, `survey` (+ Rung) | a rung `hold` changes hands by `give`; a `faction_sheet` minted on a Rung subject |
| `oblige` (reader) | `purview_reaches` true across two seats joined by a holder's `oblige` |
| `work` (delta ≥ 0) | a hand-built `work` with a negative declared delta is refused |
| R-3 | `test_u7_own.py:42`'s DECLINED tuple shrinks; `commitment.ended` emitted by `release` |
| states | war: `at_war` true after an `utter` of a `WAR`-mood Proposition and a `commit` to it, false after the `release` (already a real fold, `faction_q.py:232-242`) · truce: deferred · treaty: tribute renewed by `_renewals` · alliance: allied persons in a `march`'s sides · vassalage: as `oblige` · hostage: a `custody` edge opened by `detain` under the receiving seat's warrant after the hostage's `move`, and his `move` refused while it is live (K-38) · siege: some faction other than the holder's `mustered` at a settlement after an arrival · excommunication: a `confer` refused on a banned person · outlawry: a seatless `detain` on a `ban` holder · custody: as `detain` · sentence: `_renewals` treating two disposal kinds differently · concealed identity: as `conceal` |

### 14.2 What was not verified

- **Nothing here was executed.** The corpus run is the orchestrator's (2026-10-03); the realm `att/ex`
  figures are copied from `requirements.yaml:674-676` (tree `23bea9da`). The author re-ran the two import
  counts and the matrix script on 2026-10-04 and read the 44 rows' structural fields off `VERB_TABLE` by
  import; nothing else.
- **Etymologies** are from general knowledge; no dictionary was opened. Uncertain paths carry [UNVERIFIED].
- **Game and history facts** are as extracted, with the extraction passes' own verification tags; not
  re-checked.
- **Code citations.** The sites in §14.3 were opened by the author of revision 1 or 2. Any other
  `path:line` is as cited by the adjudication or audit passes and was not re-opened — among them
  `loop/effects_combat.py:126-129`, `seam/contest.py:154-169`, `seam/wrappers/sigma.py:94-97`,
  `loop/sides.py:65-68`, `witness.py:40,523-540`, `effects_governance.py:90-91`, `rosters.yaml:398-405`
  (`witness_channels`) and `:1794`, and the test pins in §4 other than `test_season_shape.py:7624`.
- **The four unseeded arrangement rows'** other keys (`03_PARAMETERS.md` §E.2) were not opened; whether
  they are otherwise complete is unknown.
- **The `anchor_of` cover read** is a proposal: tier 1 today answers the act's own id
  (`state/attribution.py`, read at its docstring and the `anchor_of` definition only).
- **The custody floor** on a prisoner's combat pool (§9.8) and **which bands of a contested `determine`
  convict** (§9.6) are assumptions with no fixture behind them.
- **The march analysis** ran nothing. Its realm figures are H-149's and H-175's recorded measurements;
  the author of revision 3 opened those rows and the code sites in §14.3 and re-ran nothing. Not opened
  by the author: `Tenure.granted_acts` (`state/carriers.py:107-131`, the grant the `muster` basis reads),
  `world_q.py:999-1020` (`fortification_of`) and `hole_register.yaml:3651, :3657` (H-166's clauses) —
  each as the analysis cites it.
- **The survey interrogation** ran nothing. The author of revision 4 opened the sites in §14.3 and the
  survey's and the games extraction pass's text; every other `path:line` in §6 is as the survey
  interrogation cites it and was not re-opened — among them `decision/budget.py:18-61`,
  `state/carriers.py:379-392`, `epistemic.py:781-798`, `queries/world_q.py:1309-1344`,
  `effects_information.py:323-386`, `seam/wrappers/sigma.py:159-170`'s ladder and
  `data/fixtures.py:724`.
- **The survey's own unverified items**, carried as it states them: *Crusader Kings III* 1.19 "Scribe"
  (April 2026), which the games extraction pass does not confirm (it confirms 1.13 "Basileus",
  September 2024); *Espiocracy*'s planned 2027 release, its 34 operation types and its graded outcomes,
  from developer material; the *L.A. Noire* fan wiki's count of 236 interrogation questions (56 Truth,
  106 Doubt, 74 Lie); *Suzerain*'s two-thirds Assembly majority plus Supreme Court for an amendment, from
  one guide; *The Republic of Rome*'s designers. None was re-checked here (§6.4).

### 14.3 Sites opened

**By the author of revision 4 (2026-10-04).** `loop/witness.py` 135–162, 278–329, 370–394 ·
`architecture/meta/01_AXIOMS.md` 100–153, 260–359, 480–491, 1395–1414 · `verb_table.yaml` 205–232,
408–429, 743–757, 836–842, 948–961, 965–1119, and line 676 · `rosters.yaml` 1000–1038, 1138–1149,
1536, 1544, 1697–1704, 1730–1831 · `loop/effects_information.py` 76–115, 205–325, 440–480 ·
`decision/options.py` 88–114, 995–1094 · `decision/choose.py` 355–370 · `loop/matter.py` 230–266 ·
`epistemic.py` 305–340, 863–891 (and `TERMS_SUPPLIED_BY`, `marks` by search) · `state/gate.py` 190–215,
700–758 (and `released`, `HANDOVER` by search) · `arrangements.yaml` 85–120 · `queries/world_q.py`
148–167, 389–392, 420–427, 1355–1371, 1426–1436 · `state/carriers.py` 930–945 · `queries/person_q.py`
55–70 · `seam/wrappers/sigma.py` 100–171 · `data/arrangements.py` and `data/rosters.py` (`proofs` by
search: read only by the loader's membership check) · every non-test Python file under `engine/season/`
for a `succeed` kind read (none) and for `mood` (`faction_q.py:208-246`, `world_q.py:1311, :1329,
:1342`). Outside the tree: the survey, whole; the games extraction table at its title rows and at
G1-10, G1-17, G1-22, G1-34, G1-38, G1-41, G1-84 to G1-90, G1-98, and the CK3 table at G2-26 and G2-36.

**By the author of revision 3 (2026-10-04).** `engine/season/verb_table.yaml` 384–407, 585–615 ·
`loop/sides.py` 1–122 · `loop/effects_combat.py` 270–370 · `loop/encounter.py` 20–64 ·
`seam/wrappers/mass_battle.py` 140–194 · `loop/resolve.py` 44–56, 505–604 · `loop/effects_migration.py`
30–109 · `state/gate.py` 575–757 · `state/world.py` 150–163, 262–325, 560–585 · `loop/predicates.py`
425–445 · `queries/world_q.py` 555–608, 951–996, 1125–1189 · `queries/faction_q.py` 200–250 ·
`hole_register.yaml` H-148 (3076–3120), H-149 (3122–3158), H-150 (3160–3245), H-151 (3247–3300), H-152
(3302–3375), H-175 (3767–3806) · `tests/test_march.py` 55–279 · `tests/test_build_realm_determinism.py`
100–118 · `harness/aperture.py` 150–178, 214–226 · `harness/populated.py` 384–400 · `write_matrix.yaml`
220–259, 345–372 · `data/rosters.py` 444–457 · `rosters.yaml` 130–150, 845–860, 1695–1706 ·
`requirements.yaml` 672–677, 1018–1024 · `architecture/meta/01_AXIOMS.md` 197–201, 472–482, 1370–1391 ·
`architecture/meta/04_CODE_ARCHITECTURE.md` 560–590, 790–796, 908–912.

**By the author of revision 2 (2026-10-04).** `registers/editorial_ledger_in_archive.jsonl` 178 ·
`registers/editorial_ledger_in.jsonl` 32, 34 · `engine/season/data/verbs.py` 92–93, 503–510, 528–534,
563–575, 589–620, 674–681, 690–730, 766, 779–786, 818–821, 831–840 (and `refusal_for`, `COUNTERPARTY_CLAUSE`
by search) · `state/gate.py` 485–495, 530–545, 555–630 · `rosters.yaml` 101–116, 150–153, 164–177,
210–227, 294–310, 436–440, 801–817, 1024–1032, 1040–1066, 1108–1116, 1147–1154, 1569–1584, 1648–1656,
1695–1705, 1737–1772 · `state/carriers.py` 699–721 · `data/rosters.py` 445–476 · `queries/world_q.py`
455–465 · `loop/effects_information.py` 78–110, 145, 176, 190–200 · `loop/effects_economy.py` 70–100 ·
`data/fixtures.py` 690–697 · `data/arrangements.py` 198–208, 260–268 · `arrangements.yaml` 10–24, 90–100,
108–116 · `verb_table.yaml` 228–245, 427, 440–449, 465–469, 600–622, 672–678, 686–692, 716–722, 730–775,
888–900, 928–933, 948–961, 1084, 1103, 1149 · `hole_register.yaml` H-85 (1050–1055), H-156 (3519–3522),
H-166 (3648–3653), H-183 (4083–4110) · `write_matrix.yaml` 186–194, 380–388, and all 37 rows by script ·
`decision/options.py` 540–580, 700–750, and the `operand_bags` and `teller_weight` definitions ·
`decision/choose.py` 320–332 · `loop/resolve.py` 540–560 · `data/requires.py` 706–712, 834–843 ·
`state/attribution.py` (docstring; `anchor_of`) · `epistemic.py` 537, 553 ·
`proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md` 178–188 ·
`architecture/meta/01_AXIOMS.md` 164–172, 199–212, 1203–1219 ·
`architecture/meta/04_CODE_ARCHITECTURE.md` 235–238, 255–259 · `canon/02_canon_constraints.md` 48–52, 72 ·
`references/action_vocabulary.yaml` 28–62 · `workplans/2026-10-01-telling-workplan.md` 311 ·
`engine/season/cases/exercises/NPC-038.yaml` 22–30 · `engine/season/tests/test_season_shape.py`
7618–7628.

**By the author of revision 1 (2026-10-03).** `rosters.yaml` 101–116, 160–215, 286–311, 488–491, 574–577,
998–1037, 1100–1154, 1503–1506, 1534–1545, 1556–1584, 1737–1762, 1818–1829, 2156–2159, 2192–2195,
2230–2233 · `verb_table.yaml` 312, 315, 438–468, 737, 748, 754, 757, 873–887, 949–960, 1022 ·
`write_matrix.yaml` 259–266, 376–395 · `hole_register.yaml` H-101 (1961–1975), H-108 (1571–1582), H-156
(3518–3521), H-163 (3609–3620), H-173 (3740–3751) · `arrangements.yaml` 8–30, 78–137 · `requirements.yaml`
672–677 · `loop/effects_combat.py` 270–290 · `decision/options.py` 712–750, 822–860 (and
`_from_content_claim` at 540 by search) · `loop/predicates.py` 325–345 · `loop/resolve.py` 114–118 ·
`data/rosters.py` 441–456 · `data/verbs.py` 736–790 (by search) · `data/requires.py` (searched for
`all`/`any`) · `state/carriers.py` 543–550 · `decision/budget.py` 55–59 · `epistemic.py` 536–541 ·
`systems/social_contest/sim/contest/modes.py` 35–66 · `references/action_vocabulary.yaml` 1–60 ·
`canon/02_canon_constraints.md` 45 · `architecture/meta/04_CODE_ARCHITECTURE.md` 202 ·
`proposals/2026-09-20-pursuit-basis-worksheet.yaml` 148–157 ·
`proposals/2026-09-26-decision-layer-execution-plan/candidate_pursuit_cells.md` 98–99.

### 14.4 Corrections to revision 1, applied in this revision

From the audit pass (its §8 defects and K-items), and two of the author's own (marked †). Items 4, 5, 9,
24 and 26 record what revision 2 corrected in `war`, `truce` and `besiege`; revision 3 has since removed
all three (K-28, K-29, K-32).

1. Cutting `comply` and splitting `evade / defy` was escalated against a later ruling that keeps them
   (K-01).
2. "Every kind needs an opener": openers are reported; only the closer half refuses (K-12).
3. "Parties are always seat-holders" contradicted the custody, cover and debt states (K-26).
4. `war`'s keys needed two operands (K-13).
5. `truce` carried `until` beside `Record.stages` (K-11).
6. Nineteen Record kinds → six: `case` refused by its effect, `claim` colliding with `Claim`, warrant,
   summons and charter duplicating `dispensation`'s keys (K-11).
7. "No new `remit_acts` value" was false for the `commit`/`oblige` remit alternatives; those are dropped
   (K-07).
8. `custody`'s object differed between `detain` and `pardon` (K-17).
9. Flat writes on contested rows (`detain`, `interrogate`, `besiege`) (K-05).
10. A new precondition stem would be refused at load (K-18).
11. Unbound counterparties on `seize` and `sabotage` (K-04).
12. ED-IN-0210 ruling 2 does not back `covenant`'s two-sidedness (K-14).
13. `raze` declared no beneficiary (K-06).
14. A per-verb witness exception for `conceal` is scripting drift (K-19).
15. "No act lowers a Site's condition": a hand-built `work` does (K-09).
16. "The law verbs share eligibility" was false (K-26).
17. `surveil`'s Person widening was a sibling row headed "no new verb" (K-16).
18. "Expulsion waits on H-159's fixture": `oblige_term = 4` is shipped (K-26).
19. `choose.py:326-329` scores `pursuits` through `project`; capability is not a term there (§10.3).
20. `04_CODE_ARCHITECTURE.md:237` → `:257` for the ban on stored social aggregates (§10.3).
21. `cases/exercises/NPC-038.yaml` → `engine/season/cases/exercises/NPC-038.yaml` (Appendix D).
22. `world_q.reach` admits a held seat; the gap is a claim about one (K-25).
23. The coverage counts were internally inconsistent (K-26); recounted (§5).
24. `war`'s "must not be in purview" is a negation the grammar cannot spell; it is effect-side (§9.2).
25. `bar` → `ban` (K-12).
26. `execute` refused as a verb (K-10, R-1); `challenge`/`accept` resolved without one (K-23); the
    `dispatch` → `order` rename withdrawn (K-24); `besiege` lands with its reader (K-22).
27. † The lie belongs to the telling workplan's G7, not H-183 (§9.7).
28. † A held writ answers only `to` today; `kind` and `amount` decline every time (`options.py:548-555`),
    so revision 1's "a held writ answers `to`, `kind` and `amount`" overstated the channel (§10.1).
29. † Appendix A, `issue`: the "terms are the executor" limit is `loop/effects_information.py:176`, not an
    unanchored `:176-179`.

### 14.5 Corrections to the audit pass, made by the author

Items 5, 6 and 10 concern `war` and `proclaim`, which revision 3 has removed (K-29, K-34); they stand as
the record of revision 2.

1. **K-05:** `detain`'s two refusal kinds are not "lawful only on a flat row". The loader refuses a
   contested keyed row with more than one kind (`data/verbs.py:717-720`); K-02's own fold edit narrows that
   rule to rows that do not key the counterparty clause, and `detain` keys it, so its two kinds are lawful
   once step 4 lands — which precedes `detain` at step 5.
2. **K-03:** the widened `determination` basis may not close every `disposes:` kind. `arbitration`
   disposes an `oblige` (`arrangements.yaml`; `state/gate.py:488-489`), and a bench closing it would be the
   obligee-side closer D-5 refused (`verb_table.yaml:757`). The closing half admits `custody` and `ban`
   only. C-1 item 3 (`21_RECONCILIATION.md:181-185`) licenses an opening clause; the closing half is this
   suite's extension [ASSUMPTION].
3. **The enabler's map** gave `dispensation` `kind` and `amount` entries, but its keys are `[terms, to,
   at]` (`rosters.yaml:212`) and those two decline every time today (`options.py:548-555`). Dropped; a kind
   that carries them adds them.
4. **The enabler's step** omitted a precondition: a computed `issue` binds `terms` and `to` to one referent
   (`loop/effects_information.py:176`), so a warrant's `terms` would name its own holder. `issue` joins the
   known-person fan in the same step (§10.1). Revision 1 named this; the audit's order did not.
5. **`war`'s `at` = `_seat_rung`:** `_seat_rung` (`effects_information.py:145`) is the rung a Record is
   drawn up at; the `at` key is read from the act's payload as declared and is `None` on a computed act
   (`:84-85`). The key list stands; its filling is restated (§8.2).
6. **§4's `proclaim` row** keyed refusals on an `authority` conjunct. A purview conjunct would refuse every
   war, whose target lies outside purview; the cell is `existence` of a Rung (`target`) and the in-purview
   decline is effect-side (§9.2).
7. **K-15** deferred the lie to H-183 (`hole_register.yaml:4083`). H-183 is how much a teller's record
   weighs; the lie is the telling workplan's position G7, deception, at `said_of`
   (`workplans/2026-10-01-telling-workplan.md:311`), which H-183's `unblocks:` names.
8. **K-23** cites `verb_table.yaml:1299` for `fight` as the one door to the duel engine. The table has
   1,179 lines; the line is revision 1's own, whose source is `seam/contest.py:154-169` (as cited by pass
   1). Likewise K-11's `:380`, K-12's `:1625` and K-23's `:1421` are revision-1 lines, not code.
9. **R-5 against §4's roster edits:** R-5 recommends an `inheritance` member of `conferral_bases`, while
   the audit's roster-edit list says `conferral_bases`: none. The suite carries R-5 as a later step outside
   the eleven (§10.4, §11).
10. **Build step 1** listed K-13 as retired; K-13's resolution frees `war` from the enabler, so it retires
    at step 7.
11. **`pardon`'s precondition** — a live `custody` *or* `ban` — is a disjunction over kinds, which the
    grammar lacks (`rosters.yaml:1699-1703`). The row takes `release`'s route: untyped, with a declared
    domain and a registered predicate (§9.1). Beneficiary `subject` is structural, so an untyped row may
    carry it (`data/verbs.py:92-93`).
12. **R-4's** "a top seat ends by … a `ban` from a bench with purview": `ban`'s readers refuse service and
    seating; neither closes a live seat-hold. Restated (§13).
13. **R-3** had no build step; placed at step 2, where `commit` becomes formable.
14. **`oblige`'s "hostage-kin" state** dropped: a hostage is `custody` under a covenant (§8.1).
15. **K-20:** the capability `train` raises ranges over `verb_capability`'s values (capability names),
    not its keys (verb names) (`rosters.yaml:1061-1064`).
16. **The roster's `fight` counterparty** read "subject (contest)"; the live row's counterparty is empty,
    and the subject is bound as the second claimant by the typed cell (§7.1).

### 14.6 Corrections revision 1 made to the adjudication reports (carried)

1. **D-5 and C-1 were engaged by neither adjudication pass.** `verb_table.yaml:757` records that a
   disposal `oblige` is self-releasable by ruling and that no obligee-side closer of an obligation
   "exists or will". Hence `pardon` scoped to `custody` and `ban` (§9.1), the `revoke` widening to expel
   withdrawn (§9.6), and the case for two non-releasable tenure kinds (§8.3).
2. **The enabler may not coin operand names** (`accused`, `against`): the vocabulary is closed at eight and
   the writ roster must be a subset of it (`rosters.yaml:1569`, `:1576-1577`) (§10.1).
3. **`interrogate`'s degree emissions** of `finding.made`/`finding.none` run against `rosters.yaml:1031`;
   the suite takes the confession reading (§9.1).
4. **Outlawry had two carriers**; reduced to one per target (§8.1).
5. **`remit_acts` is `open: true`** (pass 1 called it closed); a rename of `dispatch` would not have
   forced a rename of the remit act, which already gates `march` (`rosters.yaml:294-302`). The rename is in
   any case withdrawn (K-24).
6. **Binding-decision count**: nine rows, eight admitted — not seven (Appendix D, e).
7. **`raze`'s evidence**: RTK's Hidden Poison (development and public order fall) belongs to `sabotage`
   (§9.3).
8. **The typed grammar's `all` form** is at `data/requires.py:858`, not `:542` as the `release` row's note
   says (Appendix D, l).

### 14.7 Corrections to revision 2, applied in revision 3

From the march analysis, each checked against the code:

1. "Hooked in the realm (16/16)": declared 16, fought 0 — every natural target is refused at H-149's check
   (K-31).
2. "Title moves by … a seat's `revoke`": `revoke` closes seat-holds only; a rung hold ends by `release`,
   `give`, `seize` or death (K-30).
3. R-2's option (a) "needs a fifth lawful non-owner Tenure write, amending ratified §C.2": five bases were
   added after that enumeration, each by a plan position (`04_CODE_ARCHITECTURE.md:564-586`) (§13.2).
4. A `war` Record was a second owner of the war `faction_q.at_war` already reads (K-29).
5. "`aperture` `march` counts split by war present or absent" named no existing instrument: `aperture`
   counts attempts, executions and refusal kinds per (holder, verb) and splits nothing by target
   (`harness/aperture.py:154-176`). Replaced by a named `w.log` + `w.acts` test (§14.1).
6. `besiege`'s subsistence reader was never buildable as written: only cohorts eat (`world_q.py:559-572`),
   a cohort holds no `commit` and so never musters (`harness/populated.py:393`), and an arrived army of
   weight-1 persons draws nothing (`world_q.py:604`) (K-22 retired; §10.4).

### 14.8 Corrections to the march analysis, made by the author of revision 3

1. **Its two code edits would have broken H-149.** `sides_of` signals H-149's refusal of a non-settlement
   target by `subject = None` (`loop/sides.py:89-92, :105-107`) — the same value an unheld settlement
   produces. Edit (ii), the wrapper's `subject None` → `Unopposed`, would therefore turn every march on a
   hearth or a person-kind rung into an arrival — all eleven of the realm's natural marches
   (`hole_register.yaml:3148-3156`), each re-homing an army into the actor's own building — and fail
   `test_a_march_on_a_non_settlement_rung_refuses_h149_is_enforced` (`tests/test_march.py:158-171`). A
   third edit is needed: H-149's branch returns empty `claimants`, which refuses at `loop/resolve.py:558-559`
   with the same `march.refused`. That splits `sides.py:89-92`'s "one mechanism for both causes" on
   purpose: the two causes now mean different outcomes (§9.6).
2. **`test_declared_and_unopposed_are_no_change_directly` does not flip as the analysis says.** It passes
   `Resolution("Unopposed", {})` with no `parties` (`tests/test_march.py:267-274`), so an effect that
   relocates the claimants named in `res.result["parties"]` still returns `NO_CHANGE`; the assertion keeps
   passing and stops observing the band it names (CLAUDE.md §0.1 pt 2). It must be re-written with
   claimants (§10.4 step 8).
3. **`seize` widened to a Rung needs a disjunction the grammar lacks.** "Record or Rung" cannot be one
   typed cell (`rosters.yaml:1699-1703`) — K-16's ground — which the analysis did not address. Resolved on
   `pardon`'s route: untyped, a registered predicate, the licence read at the effect (§9.1).
4. **`_relocate` moves `a.actor` and keys its leg id on him** (`loop/effects_migration.py:77-81`), so
   reusing it "for every claimant" needs the mover as a parameter, or every claimant's leg shares one id
   (§9.6).
5. **H-152 is cited for more than it says.** It states that emits are fixed per degree, not per swept
   fixture (`hole_register.yaml:3309-3313`); "never per stake" is the analysis's extension. It holds, since
   the schema keys emits on degree alone, but the row does not say it.
6. **§E.1.6 is cited for more than it says.** `01_AXIOMS.md:1386-1389` recommends an uttered Proposition
   plus an owned edge for a relation between things that cannot act. It supports refusing an ownerless
   stored `siege` Record; it does not name a Query. The siege's carrier is the persons' own `contain`
   edges (§8.1).

Verified and not corrected: the §11 ladder admits the relocation — a person's `contain` to a settlement
ascends (`state/world.py:282-285`: a non-rung subject passes, and a `person`-kind rung sits below a
settlement) — and `_subtree` includes the settlement itself (`world_q.py:956`), so an army re-homed onto
the settlement is in every later `mustered` read.

### 14.9 Corrections to the survey interrogation, made by the author of revision 4

1. **Batch confirmation is refused by AX-7, not T-j.** The interrogation grounded it, and P21, on T-j
   (`01_AXIOMS.md:486-488`). T-j's *belief* is AX-3's "what is held right" (`:124-127`); a confirmed
   deduction is about what is held true. The ground is AX-7: a confirmation is the engine's own
   resolution handed into a ledger unmediated (`:314-317`). The conclusion stands (§6.1).
2. **4.5 is not a ruling.** The interrogation called work item 4.5 "the only ruled producer shape". The
   table says *"THE DEGREE IS WORK, NOT A RULING"* (`verb_table.yaml:982`): 4.5 is a plan work item that
   closed the blank at §0's test 3. Restated as the only producer shape the tree has written down.
3. **AX-7's own citations have drifted.** The interrogation cites `01_AXIOMS.md:306-317` as naming "that
   deposit"; AX-7 names `witness.py:191`, `:271`, `:361`, and the event-kind deposit is at
   `loop/witness.py:380` today. The substance holds; Appendix D (t).
4. **The path is `engine/season/epistemic.py`**, not `loop/epistemic.py`; `_ch_co_located` is at `:322`.
5. **`state/carriers.py:939-942` does not say the `succeed` edge has no reader.** It records that the
   Rung's `transmission` field was deleted and that transmission is the holder's `succeed` edge. The
   ground for "nobody reads it" is `verb_table.yaml:839`'s decline note (*"A CARRIER NOBODY READS"*) and a
   search: no non-test Python under `engine/season/` reads a `succeed` kind. Revision 1's Appendix A
   `succeed` block carries the same cite and is marked.
6. **K-35's charge has a computed-source gap the interrogation did not name.** `mood` and `subject` are
   payload keys of `_eff_utter` (`loop/effects_information.py:467`), and a computed act's payload is its
   operands plus `subject` (`decision/choose.py:358-369`). A computed `utter` can therefore name the
   accused, the question's referent, but cannot set `HOLDS`: it mints `OUGHT`, which `ambitions` reads
   as a standing need of whoever commits (`queries/world_q.py:1311, :1342`). And because `interrogate`
   and the contested `determine` take a Person as `subject`, the charge is reached at the effect through
   the Proposition whose `subject` is the party — two hops the grammar cannot join (§8.1).
7. **The hostage's warrant does not depend on his move.** The interrogation said the `issue` cell's
   `authority` conjunct passes "since he now stands there" (`verb_table.yaml:423-427`). That conjunct is
   asked of `to`, the executor, and of where the executor lives; the person a warrant names is its
   `terms`, which no conjunct of the cell reads. The composition stands; the `move` is the handing-over,
   not the licence (§8.1).
8. **`steal`'s opening already passes the gate.** "No basis admits it" holds for half the write: the
   thief's opening of a `hold` naming himself passes `T-m` (`state/gate.py:707-710`; Appendix D, p), and
   what no basis admits is the closure of the holder's `hold`. `theft` is a closing licence paired with
   the actor's opening (§9.3). "`seizure` is licensed" refers to the suite's proposed basis, not a live
   one. "Every basis is authority- or causation-bound" omits the owner-bound bases (`T-m`, `handover`).
9. **The band does not select `Seen` terms today; the channel does.** `seen_of` unions the terms each
   admitting channel supplies (`epistemic.py:863-891`). A band selecting them for `examine` and `surveil`
   is the proposal, built on that shape [ASSUMPTION] (§6.3).
10. **`proofs` is read — by the loader only.** "Read by nothing in the fold" holds; the arrangement
    loader checks membership against it (`data/arrangements.py:200-201`), and nothing weighs a proof.

**Kept beside the interrogation's reading, not a correction:** to close self-interview it binds a
counterparty `to` through the known-person fan with a `with` relation; the author records the cheaper
alternative beside it — `counterparty: subject`, as `detain` and `interrogate` declare, which the fold's
existing counterparty clause already enforces, with no move of the questioned person to `to` (§6.3).
Both stand until `interview` is built.

**Not a correction to the interrogation:** the task brief said the survey had five findings; it has four
(Findings 1–4), and the interrogation said so. Four is used throughout.

Verified and not corrected: AX-2 (`01_AXIOMS.md:104-120`), T-a (`:327-354`) and the player clause
(`:299-304`); `verb_table.yaml:757`, `:1043-1048`, `:1113-1115`, `:985-987`; `rosters.yaml:1031-1034`,
`:1737-1755`, `:1767-1771`, `:1818-1828`; `effects_information.py:220`, `:284-297`, `:300-319`;
`decision/options.py:1001-1040`, `:1043-1093`; `loop/matter.py:235-265`; `state/gate.py:707-757` (nine
bases); `arrangements.yaml:93`, `:95`, `:103-115`; `queries/world_q.py:152-166`, `:1362-1367`,
`:423-425`; `queries/person_q.py:63-69`; `seam/wrappers/sigma.py:105-122`; `01_AXIOMS.md:1399-1403`; the
three theft rows and the two *Shadows of Doubt* dates in the games extraction table.

### 14.10 Corrections to revision 3, applied in revision 4

1. §8.1's hostage `[GAP]` — how a covenant stands in for a warrant — is closed by composition (K-38).
2. §8.1's War row said a computed declaration waits on build step 2; it waits also on a `mood` source a
   computed act lacks (§14.9 item 6). The row now says so.
3. Appendix C's "*Shadows of Doubt* (ColePowered, 2024)" is the full release; early access opened on
   24 April 2023 (§2).

---

## Appendix A. The 44, in full

Pass 1's per-verb adjudication with pass 2's REACH and NOT merged in, as revision 1 carried it. Section
references are renumbered to this revision, the exclusion kind is written `ban` (K-12), and a NOT entry
that pointed at an unowned act now names the suite's owner; otherwise each block is revision 1's. **A block the suite changed carries one line `[SUPERSEDED by …]` naming what no
longer holds; the section it names states the suite.** Citations are pass 1's unless §14.3 lists them as
opened. *nj* = needs_jordan.

### `build`
- **Etymology · fit:** OE *byldan* ← *bold* 'dwelling'; raise a dwelling → mint a Site at condition 0 from a held works. FITS.
- **Earns:** YES — the only `Site.exists` producer (`write_matrix.yaml:330-336`; `effects_founding.py:115-130`).
- **Group · module:** G9 · world fact.
- **Reach:** a held `works` planning a `site_kinds` member, at the rung it names; one fabric per works. **Not:** found a Rung (`found`); raise condition (`restore`); end a Site (→ `raze`).
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
- [SUPERSEDED by §3.5 / K-24]: the rename to `present` or `lodge` is deferred until the row gains its operand.

### `commit`
- **Etymology · fit:** L *committere*; entrust → open a `commit` edge to a Proposition. FITS.
- **Earns:** YES — `ambitions` reads it for need questions (`world_q.py:1309-1322,1441-1442`).
- **Group · module:** G7 · world fact.
- **Reach:** any existing Proposition (an OUGHT, a faction, a treaty, a motion); own. **Not:** utter (`utter`); duty to a seat (`oblige`); seat-to-seat fealty (unowned, H-101); a vote cast through a seat (WIDEN, §9.6).
- **Hook:** no question's referent is a Proposition (`verb_table.yaml:773`; 802 of 802 attempts refused, `hole_register.yaml:3521`). Proposal: `_eff_utter` mints the utterer's `hold` on it (`rosters.yaml:152` admits a Proposition; the maker's-hold precedent, `effects_information.py:134-137`), making it the utterer's own in reach so Q2 names it. Direct; `Tenure.since`.
- **Why:** closes utter → commit → ambition → a quiet-season act.
- **Falsifier:** leaves the always-refused pin (`test_season_shape.py:7624`).
- **Blocker · nj:** H-156 · no for the hook; H-156's (a)/(b) stays Jordan's. A hold buys budget (`budget.py:57-58`, H-92; Appendix D, g).
- [SUPERSEDED by §7.2 / K-07]: there is no vote through a seat — a vote is the holder's own `commit` and the count a Query; seat-to-seat fealty is a holder's own `oblige`, read by `purview_reaches`.

### `comply`
- **Etymology · fit:** L *complere* → It. *complire* [UNVERIFIED: intermediate]; fulfil → act per a dispensation's terms. FITS.
- **Earns:** REDUNDANT-WITH the writ-sourced `transfer` (`options.py:717-729`; `rosters.yaml:1571-1584`); nothing else executable (`verb_table.yaml:146`).
- **Group · module:** G5 · none yet.
- **Reach:** a held writ; emission only. **Not:** perform the terms (writ-sourced `transfer`); withhold (`evade / defy`); misread (`construe`).
- **Hook:** the executor holds the writ after `give`; the subject binds the writ (`carry`'s scoping precedent). Route: the writ-sourced `transfer` earns `compliance.given` beside `transfer.made` (per-subject kinds, `effects_governance.py:90-91`). Rows `Rung.stores` ×2.
- **Why:** obedience with a trace, so defiance is legible by absence.
- **Falsifier:** `compliance.given` in `w.log` from `populated.run`, with no hand-built act.
- **Blocker · nj:** H-44 (`hole_register.yaml:500`), H-94 · **yes**, for cutting a row of Jordan's triple (`verb_table.yaml:737`) — step 3.
- [SUPERSEDED by §3.5, §4 / K-01]: retained unchanged by ruling (ED-IN-0210, 2026-09-18) — THIN, not REDUNDANT-WITH; no cut, nj no. `comply` itself emits `compliance.given`; the `transfer` it answers performs the terms, with no new emission.

### `confer`
- **Etymology · fit:** L *conferre*; bestow → seat an office by opening a `hold`. FITS.
- **Earns:** YES (`effects_governance.py:63-69`).
- **Group · module:** G7 · world fact.
- **Reach:** an Office; `to` a person; `remit:confer` via a seat with purview; opens the hold, closes the incumbent's (`effects_governance.py:60-91`). **Not:** found it (`establish`); strip (`revoke`); elect (an act; the basis exists, `rosters.yaml:1755`); heir (`succeed`); a term-limited seat (WIDEN, §9.6).
- **Hook:** reads payload `office` (`predicates.py:172-174`), which is not among the closed eight (`rosters.yaml:1569`). Proposal: the office rides `subject` (convene's C-11, `verb_table.yaml:172`; `oblige`, `predicates.py:394`); the conferee rides `to` via the known-person fan (`options.py:827-860`). Rows `Tenure.until/since`.
- **Why:** patronage.
- **Falsifier:** realm ex > 0 (70/0, `requirements.yaml:674`).
- **Blocker · nj:** no question's referent is a seat (`verb_table.yaml:676`) · no. [GAP: whether `world_q.reach` admits an office id — not opened.]
- [SUPERSEDED by §10.1 / K-25]: `reach` admits a holder's own seat (`world_q.py:461`); the gap is any claim about a seat, and the office comes from a held dispensation's `terms` through the enabler. An election's votes are members' own `commit`s (K-07).

### `construe`
- **Etymology · fit:** L *construere* → ME *construen* 'interpret'; mint a distorted reading of terms. FITS (the ruled rename from `refract`, `verb_table.yaml:737`).
- **Earns:** THIN — grade `absent`, D18 (`verb_table.yaml:731-738`).
- **Group · module:** G5 · none yet.
- **Reach:** a held writ; a receiver-side reading. **Not:** lie (`tell`, H-183); forge (`forge`).
- **Hook:** WITNESS-side, not an act: H-36 rules distortion receiver-side, per receiver (`hole_register.yaml:400,404`), which the content deposit already does per holder (`witness.py:40,523-540`). Rows none.
- **Why:** misreadings that travel by document.
- **Falsifier:** two holders of one writ holding different `content:dispensation` values.
- **Blocker · nj:** H-36's magnitude half, H-44 · no.
- [SUPERSEDED by §9.7 / K-15]: the lie is deferred to the telling workplan's G7; H-183 is the weight of a teller's record.

### `convene`
- **Etymology · fit:** L *convenire* → OF *convenir*; assemble → schedule a sitting. FITS.
- **Earns:** THIN — sole `Date.due_at` writer, but the date fires vacant, `date.fired` never reaches WITNESS (`world_q.py:1362-1367`), and the slot forms with `matter: None` (`calendar.py:53`).
- **Group · module:** G4 · social contest (proceedings).
- **Reach:** any rung above `person`; `remit:convene`; adjourning is rescheduling (`effects_governance.py:240`). **Not:** docket (`open_case`/`carry`); decide (`determine`); summon a person (→ `issue`).
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
- **Reach:** a Record the actor holds or stands by; deletes it and every hold (`:441-451`). **Not:** take from another (→ `seize`); suppress a class of text (unowned); end a Rung or Site (→ `raze`, H-166).
- **Hook:** both eligibility alternatives decline (`resolve.py:119-150`; H-75); `give`'s shape was built and held (`verb_table.yaml:199`). Direct. Rows `Record.exists`.
- **Why:** the only way a document vanishes — the stake in holding one.
- **Falsifier:** `test_u7_own.py:153` flips.
- **Blocker · nj:** H-75; held on H-156's crowding · **yes**, no new row — H-156's registered (a)/(b) decides it (`hole_register.yaml:3527`).
- [SUPERSEDED by §9.3 / K-39]: taking from another is `seize` under a warrant or `steal` with none (R-8).

### `determine`
- **Etymology · fit:** L *determinare* (*terminus*); fix the bounds → dispose of a docketed matter by opening the party's `oblige`. FITS.
- **Earns:** YES (`effects_information.py:284-297`).
- **Group · module:** G4 · social contest (proceedings).
- **Reach:** a docketed Person in the bench's ground; `remit:determine` via a seat; opens the disposal `oblige`, clears the docket. **Not:** grade a hearing (WIDEN, §9.6; H-162); a sentence other than service (H-173 → `custody`, `ban`); appeal (unowned; `open_case` nests); lift a disposal (the party's own `release` for an `oblige`; `pardon` for `custody`/`ban`).
- **Hook:** needs a question whose referent is a docketed person in the bench's ground (`hole_register.yaml:3612`, limit 2). Direct via a seat. Rows `Tenure.since`, `DocketItem.matter`.
- **Why:** a bench binding men with no player watching.
- **Falsifier:** realm ex (1/20, `requirements.yaml:674`); `test_u7_remit.py:278`.
- **Blocker · nj:** H-163 limit 2 (SC lane), H-162 · no.

### `dispatch`
- **Etymology · fit:** It. *dispacciare* / Sp. *despachar*, root disputed [UNVERIFIED]; send off → emit `order.given`, write nothing. STRAINED — ordinary use sends; the row orders (`verb_table.yaml:259`). Plain alternative `order` (proposal). [CORRECTION: pass 1 says `order` "collides with the closed `remit_acts`"; the roster is `open: true` (`rosters.yaml:294-302`), and a verb rename need not rename the remit act, which already gates `march`.]
- **Earns:** THIN — a documentless `issue`; no decision reads `order.given` (`epistemic.py:547`; tests).
- **Group · module:** G5 · none yet.
- **Reach:** an existing person; `remit:dispatch`; `order.given`. **Not:** a writ with terms (`issue`); muster (`march`); summons (→ `issue`).
- **Hook:** hooked (realm 16/86). The named person gets a claim about himself (Q2 clause 1). Terms as paper are `issue`.
- **Why:** a command the chronicle carries (`epistemic.py:547-549`).
- **Falsifier:** leaves the never-attempted pin (`test_season_shape.py:8372`).
- **Blocker · nj:** none · no.
- [SUPERSEDED by §3.5 / K-24]: the rename to `order` is withdrawn — `order:` is an `arrangements.yaml` key and the fold's order key — and `dispatch` is kept by ruling (ED-IN-0210).

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
- **Reach:** a held writ; withholding. **Not:** flee (`move`); contumacy (unowned; a summons' refusal); renounce fealty (→ `release` of a vassal's `oblige`).
- **Hook:** a held writ, as `comply`. `evade` = no transfer before the term matures (`Record.matured`, `write_matrix.yaml:266-272`); `defy` = a public refusal Event. Split only when a reader distinguishes them. Rows none.
- **Why:** disobedience others see or miss.
- **Falsifier:** `compliance.withheld` from computed play.
- **Blocker · nj:** H-44, H-94 · **yes** — renaming or splitting Jordan's triple (`verb_table.yaml:737`), step 3.
- [SUPERSEDED by §3.5 / K-01, K-24]: retained unchanged by ruling; no rename; split only when built; nj no.

### `examine`
- **Etymology · fit:** L *examinare* (*examen*, the tongue of a balance); weigh → study a Site one stands at. FITS.
- **Earns:** THIN — its consequence is identical to the other five findings' (`verb_table.yaml:1033-1036`).
- **Group · module:** G11 · none yet.
- **Reach:** a Site stood at; physical trace (`:1024-1031`). **Not:** a person (`interview`); a document (`research`); a place over time (`surveil`).
- **Hook:** hooked (executes); producer is a co-located Site referent (`:789`). Route none.
- **Why:** a clue that is somewhere — but a finding carries no content.
- **Falsifier:** a `finding.made` claim with a non-trivial value.
- **Blocker · nj:** work item 4.5 (`:982-989`) · no.
- **Survey interrogation (§6.3):** APPLIES (P12 physical trace, P13 frozen-moment record, P14 inference from indirect markers). Its producer reads the log at a present Site — past Events anchored at its rung — and deposits `Seen` terms by band, Failure nothing; never a bare `True` (AX-7).

### `exchange`
- **Etymology · fit:** OF *eschangier* ← VL \**excambiare*; swap → two-sided stores move. FITS.
- **Earns:** THIN — no cell, no effect (`verb_table.yaml:297-304`).
- **Group · module:** G8 · world fact.
- **Reach:** both sides' stores. **Not:** one-way (`transfer`); sale of an office (`exchange` + `confer`); ransom (→ `transfer` + `pardon`).
- **Hook:** needs the counterparty's `kind` and `amount`, which have no operand names (`rosters.yaml:1562-1564`); `_shift` twice. Rows `Rung.stores` ×2.
- **Why:** trade, with scarcity paired on both sides.
- **Falsifier:** `exchange.made` in `w.log`.
- **Blocker · nj:** H-94 · **yes** — the register reserves coining these operands for H-94's ruling, step 5.
- [SUPERSEDED by §13.8]: already registered under H-94; no new row.

### `fight`
- **Etymology · fit:** OE *feohtan* → contest the body of a living person. FITS.
- **Earns:** YES — the one route to the duel engine (`seam/contest.py:154-169`).
- **Group · module:** G1 · personal combat.
- **Reach:** a living person; own; prize the body; the attempt only (`verb_table.yaml:456-553`). **Not:** kill or wound (outcomes — direction 3); war (`march`); restrain or arrest (→ `detain`); execute (→ `execute`, Jordan); challenge (pending).
- **Hook:** hooked ("47/89" as pass 1 records it, without naming the denominator). Any person referent but self (`options.py:145-146`). Seam "the body"; rows by band (`verb_table.yaml:522-525`).
- **Why:** the irreversible personal stake. Priced by one alignment cell (sacred −0.3, `rosters.yaml:2189`); willingness is unbuilt (`:467`).
- **Falsifier:** `test_season_shape.py:12776`; the corpus `DEGREES RESOLVED` line (`corpus_run.py:993`) — on 2026-10-03: Failure 148, Felled 12, Partial 79, Success 21, Untouched 11, Wounded 20.
- **Blocker · nj:** H-98; the deontological gate · no.
- [SUPERSEDED by §9.8, §10.2 / R-1, K-23]: there is no `execute` — a death sentence is `custody` plus this `fight`; a challenge is a `petition` whose acceptor answers it with this `fight`.

### `forge`
- **Etymology · fit:** L *fabrica* → OF *forge*; 'counterfeit' from the 14th c. → mint a Record with `forgery_quality`. FITS.
- **Earns:** THIN (`verb_table.yaml:315`).
- **Group · module:** G6 · world fact.
- **Reach:** a Record carrying `forgery_quality` (`:306-316`). **Not:** a true record (`create_record`); plant it (`give`); a false telling (`tell`, WIDEN).
- **Hook:** a faction the forger holds a claim on (`survey`'s cell, `:859-861`); `survey`'s mint with perturbed content. Rows `Record.exists`, `Record.forgery_quality`.
- **Why:** a false sheet a rival acts on (`hole_register.yaml:3690`, limit 5).
- **Falsifier:** `test_information_cluster.py:297` stops asserting that no act forges.
- **Blocker · nj:** H-169 limits 2 and 5 (a consumer first) · no. Emits `record.created` where the matrix row emits `record.forged` (Appendix D, d).
- [SUPERSEDED by §9.7 / K-15]: a false telling is deferred to the telling workplan's G7, not a `tell` widening.

### `found`
- **Etymology · fit:** L *fundare* → OF *fonder*; lay a base → mint a Rung under its works' `at`. FITS.
- **Earns:** YES (`effects_founding.py:95-112`).
- **Group · module:** G9 · world fact.
- **Reach:** a held works planning a `rung_kinds` member; strict ascent. **Not:** a Site (`build`); an office (`establish`); a league (→ `covenant`); a charter (→ `issue` kind `charter`).
- **Hook:** as `build`. Rows `Rung.exists`, `Tenure.since` (`founding`).
- **Why:** new hearths (RR-2).
- **Falsifier:** realm ex > 0 (70/0).
- **Blocker · nj:** H-165 limit 2 (J-4); H-166 · no new row.
- [SUPERSEDED by §8.2 / K-11]: a charter is a `dispensation` distinguished by its `terms`, not a kind; a league is `covenant` kind `alliance`.

### `give`
- **Etymology · fit:** OE *giefan* → close the giver's `hold`, open the receiver's, in one write. FITS.
- **Earns:** YES — the only Record mover (`effects_information.py:389-428`; H-84).
- **Group · module:** G6 · world fact.
- **Reach:** a held Record `to` a known present person (`verb_table.yaml:386-398`); the gate's `handover` is general over every non-seat hold (`:398`). **Not:** stores (`transfer`); seize (→ `seize`); cede a rung hold (WIDEN, §9.6).
- **Hook:** hooked (executes in 1 corpus world; 63 refused on the `with` conjunct). Known-person fan (`options.py:827-860`). Rows `Tenure.until/since`.
- **Why:** a writ reaches the hand that can deny it.
- **Falsifier:** `test_give.py:94-399`.
- **Blocker · nj:** none · no.
- [SUPERSEDED by §9.3 / K-39]: taking a Record without consent and without a warrant is `steal` (R-8); `seize` needs a warrant or occupation.

### `interview`
- **Etymology · fit:** MF *entrevue*; a meeting → question an existing person. FITS.
- **Earns:** THIN — existence is the whole precondition, and self-interview is admitted (`verb_table.yaml:1045-1048`).
- **Group · module:** G11 · none yet.
- **Reach:** an existing person. **Not:** interrogation under custody (→ `interrogate`); covert watching (`surveil`, WIDEN).
- **Hook:** hooked (executes). Route none.
- **Why:** to be replaced by the Dialogue Lattice (`:1054`).
- **Falsifier:** the corpus executed set.
- **Blocker · nj:** work item 4.5; ED-FI-0004 · no.
- [SUPERSEDED by §9.7 / K-16]: covert watching of a person is held until a grammar disjunction is ruled; there is no `surveil` widening in the suite.
- **Survey interrogation (§6.3 / K-36):** APPLIES (P9 approach, P10 generic prompts). Not a graded finding but a prompt: the content lives in the questioned person's ledger, which the fold may not read (F8), so they answer by their own `tell`; no degree on the asker; approach is payload data; a counterparty closes self-interview.

### `issue`
- **Etymology · fit:** L *exire* → OF *issir/issue*; "issue a writ" → mint a dispensation to an executor in purview. FITS.
- **Earns:** YES (`effects_information.py:163-180`).
- **Group · module:** G6 · world fact.
- **Reach:** terms + `to` a person executor in purview; a dispensation (`verb_table.yaml:417-427`). **Not:** a documentless order (`dispatch`); an edict to a place (→ `proclaim`; the cell refuses a rung, `:427`); an instrument across to a foreign seat (→ `covenant`); rescind (unowned).
- **Hook:** hooked (realm 6/30, with `via`). Limit: the terms are the executor (`effects_information.py:176`). Rows `Record.exists`.
- **Why:** authority as paper.
- **Falsifier:** `test_u7_remit.py:460`.
- **Blocker · nj:** H-94; `15c` · no. New kinds proposed: `warrant`, `summons`, `charter` (§8).
- [SUPERSEDED by §8.2, §10.1 / K-11]: no new kinds — a warrant, summons or charter is a `dispensation` distinguished by its `terms`; in the suite `to` fans over known persons so `terms` and the executor separate.
- [SUPERSEDED by §9.2 / K-34]: an edict to a place is none-yet — `proclaim` is deferred with its readers.

### `levy`
- **Etymology · fit:** L *levare* → OF *levée*; a raising → move a rung's stores into the seat's treasury. FITS.
- **Earns:** YES (`effects_governance.py:336-347`).
- **Group · module:** G8 · world fact.
- **Reach:** a rung in purview with stores → the seat's rung. **Not:** tribute by term (`transfer`); a person's goods (→ `seize`); muster (`march`).
- **Hook:** the referent rung is empty, or not a rung (`hole_register.yaml:3612`, limit 3). Proposal: a question whose referent is a full larder in purview (a positive `stores.changed`). Rows `Rung.stores` ×2.
- **Why:** how a seat eats.
- **Falsifier:** realm ex > 0 (23/0); `test_u7_remit.py:201`.
- **Blocker · nj:** H-163 limit 3; the `remit:issue` substitution is H-52's neighbour (`verb_table.yaml:587`) · no for the hook.

### `march`
- **Etymology · fit:** OF *marchier*, probably Frankish [UNVERIFIED]; tread → send a mustered side against a settlement. FITS.
- **Earns:** YES (`sides.py:75-118`; `effects_combat.py:274-358`).
- **Group · module:** G2 · mass battle.
- **Reach:** a settlement; `remit:dispatch`; prize a field at ENCOUNTER; writes the losing side (`effects_combat.py:274-358`). **Not:** siege (→ `besiege`); conquest or raid writes (WIDEN, Jordan — the ruling is silent on the winner, `:277-279`); muster (its own `sides_of`).
- **Hook:** declared in the realm (16; fought 0, every natural target refused at H-149's check — K-31); never in the corpus (H-175). Seam at ENCOUNTER. Rows `Person.body`, `Person.stance`.
- **Why:** war that leaves grudges.
- **Falsifier:** `test_march.py:323`; leaves the never-attempted pin (`test_season_shape.py:8372`).
- **Blocker · nj:** H-175, H-149 · no (the winner's writes: **yes**).
- [SUPERSEDED by §7.2, §9.6, §13.2 / K-28, K-30, K-33]: there is no `besiege` — a siege is a Query over an arrived army; a won or unopposed march writes the arriving army's presence (basis `muster`) and no hold; title moves by `seize` under occupation, `give`, `release` or death, never `revoke`; R-2 is resolved, nj no (R-6 and R-7 remain as one-line residuals).

### `migrate`
- **Etymology · fit:** L *migrare* → re-home `contain` and `reside`, throttled by capacity. FITS.
- **Earns:** YES (`effects_migration.py:124-149`).
- **Group · module:** G10 · world fact.
- **Reach:** a rung with room; `contain` + `reside`. **Not:** presence (`move`); exile another (unowned → `ban` + `migrate`); relocate a court (unowned).
- **Hook:** the destination is the migrant's own home (`hole_register.yaml:3677`). Proposal: a destination channel — a shortfall at home plus a positive `stores.changed` elsewhere in reach, or a founded hearth with room (`:3683`). Rows as `move`.
- **Why:** people who leave famine.
- **Falsifier:** leaves the always-refused pin (`test_season_shape.py:7624`).
- **Blocker · nj:** H-168 (H-94) · no.

### `move`
- **Etymology · fit:** L *movere* → re-home `contain` only. FITS.
- **Earns:** YES — presence (`effects_migration.py:103-108`).
- **Group · module:** G10 · world fact.
- **Reach:** a rung up the ladder (`verb_table.yaml:645-659`). **Not:** residence (`migrate`); flight from custody (refused by `custody`'s reader, §8.1).
- **Hook:** hooked ("650/73" as pass 1 records it). Rows `Person.travel_leg`, `Tenure.until/since`.
- **Why:** being in the room is the epistemic model.
- **Falsifier:** `test_migrate_capacity.py:153`.
- **Blocker · nj:** none · no.

### `oblige`
- **Etymology · fit:** L *obligare* → OF *obligier*; bind → open an `oblige` edge with a term. FITS.
- **Earns:** YES (`epistemic.py:445-454`; renewed by `transfer`).
- **Group · module:** G7 · world fact.
- **Reach:** a seat whose `binds` admits the joiner; own; with a term (`predicates.py:394-403`). **Not:** seat-to-seat fealty (WIDEN with `via`, §9.6); sentence (`determine`); hostage (→ `custody`).
- **Hook:** no question's referent is a seat, and the row is untyped (`verb_table.yaml:669,676`). Proposal: type clause 1 once a seat can be a referent — a `tenure.opened` is chronicle-broadcast (`epistemic.py:553-554`) and expands to the office id (`effects_governance.py:84-89`) [UNVERIFIED: whether `reach` admits it]. Rows `Tenure.since`, `Tenure.term`.
- **Why:** retinues.
- **Falsifier:** `test_obligees.py:282` flips; leaves the never-attempted pin.
- **Blocker · nj:** seat referents (H-94/H-54) · no.
- [SUPERSEDED by §7.2, §10.1 / K-07, K-25]: no `via` or remit alternative — vassalage is the row as it stands, a seat-holder's own `oblige` to another seat, read by `purview_reaches`; `reach` admits a held seat, and the seat referent comes from a held Record's `terms` or a `tenure.opened` deposit.

### `open_case`
- **Etymology · fit:** L *casus* → OF *cas*; legal → mint a case file and docket the matter. FITS.
- **Earns:** YES (`effects_information.py:183-225`).
- **Group · module:** G4 · social contest (proceedings).
- **Reach:** any matter at a place in purview; `remit:determine`; a case file + the docket (`:215-225`). **Not:** own docketing (`carry`); a private accusation (a `petition` kind); appeal (the same verb, nested).
- **Hook:** hooked (realm 7/28). Rows `Record.exists`, `Record.stages`, `DocketItem.matter`.
- **Why:** grievances enter the institution.
- **Falsifier:** `test_u7_remit.py:246`.
- **Blocker · nj:** H-52 (`verb_table.yaml:700-701`) · already registered as H-52, no new row. New kind proposed: `case` (§8).
- [SUPERSEDED by §8.2 / K-11]: no `case` kind — the effect mints `text` by its own ruling until a reader needs one (`effects_information.py:196-198`); an accusation is a `petition` by its `terms`, not a kind.
- [SUPERSEDED by §8.1 / K-35]: the docket stays person-keyed — `open_case` dockets the accused — and what is charged is an uttered `HOLDS` Proposition the petition names.

### `petition`
- **Etymology · fit:** L *petitio* → OF; a request → mint a petition Record to a person, from a rung. FITS.
- **Earns:** YES (`effects_information.py:300-319`).
- **Group · module:** G6 · world fact.
- **Reach:** terms; `to` a person; `from` a rung; own (`verb_table.yaml:710-717`). **Not:** docket (`carry`); a writ downward (`issue`); accusation, demand, challenge (kinds of itself, §8).
- **Hook:** hooked. Limit: addressed to its own subject (`verb_table.yaml:719`). Rows `Record.exists`.
- **Why:** the upward voice.
- **Falsifier:** `test_record_kind_fold.py:153`.
- **Blocker · nj:** H-94; its closers are unbuilt (`effects_information.py:313-318`) · no.
- [SUPERSEDED by §8.2 / K-11, K-23]: not kinds — an accusation, demand or challenge is a `petition` distinguished by what its `terms` names.
- [SUPERSEDED by §8.1 / K-35]: an accusation's `terms` names the charge — an uttered `HOLDS` Proposition whose subject is the accused — and testimony is a witness's `commit` to it.

### `reconstruct`
- **Etymology · fit:** L *re-* + *construere* → make a finding from held claims. FITS.
- **Earns:** THIN — a self-feeding loop is visible (`test_season_shape.py:3974-3977`).
- **Group · module:** G11 · none yet.
- **Reach:** anything in one's own ledger; synthesis (`verb_table.yaml:1111-1113`). **Not:** new information (the other five); decipher (`research`).
- **Hook:** hooked ("404–426 acts" as pass 1 records). Route none.
- **Why:** synthesis that can be wrong (`verb_table.yaml:1115`) — unbuilt.
- **Falsifier:** the corpus executed set.
- **Blocker · nj:** the obstacle (`:1113`), work item 4.5 · no.
- **Survey interrogation (§6.3 / K-37):** APPLIES (P16, P17 boards, P5's cap bounding what is synthesized); the one finding with no world read. It waits: canon's obstacle needs a scope a GM chooses, and canon's wrong conclusion on Failure needs a value space nothing supplies, so Failure deposits nothing; its output stays held-true and never moves `pursuits` (AX-3).

### `release`
- **Etymology · fit:** L *relaxare* → OF *relaissier*; let go → close one's own edge of any releasable kind. FITS.
- **Earns:** YES (`effects_governance.py:157-191`).
- **Group · module:** G7 · world fact.
- **Reach:** the object of one's own live edge, six kinds (`verb_table.yaml:748`), including a disposal `oblige` by ruling (`:757`). **Not:** another's edge (`revoke`); pardon (→ `pardon`, for `custody`/`ban`); waive what is owed you (refused by D-5, `:757`).
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
- [SUPERSEDED by §13 / R-3]: the cut is the suite's recommendation, carried at build step 2; Jordan may overrule it.

### `research`
- **Etymology · fit:** OF *recercher* (← L *circare*) → consult an existing Record. FITS.
- **Earns:** THIN (as `examine`).
- **Group · module:** G11 · none yet.
- **Reach:** an existing Record (`verb_table.yaml:1061-1063`). **Not:** a Site (`examine`); a person (`interview`); a letter in transit (unowned).
- **Hook:** hooked. Route none.
- **Why:** archives (`rosters.yaml:2229`).
- **Falsifier:** the corpus executed set.
- **Blocker · nj:** work item 4.5 · no.
- **Survey interrogation (§6.3):** APPLIES (P11, P18, P58). The cheapest producer of the six, since both readers exist: Success deposits the Record's content verbatim, as a holder's deposit does (`witness.py:283-305`); Partial reuses `_told_value`'s drift (`:137-160`); Failure nothing. Reading without holding.

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
- **Reach:** an office via a seat with a basis; closes the hold. **Not:** resign (`release`); excommunicate or outlaw (→ `determine` disposing `ban`); expel an obligee (refused by D-5; lapse instead, §9.6); dissolve (unowned); depose a seat with no rung above (closed roster — Jordan).
- **Hook:** payload `office` (`predicates.py:433`). Proposal: the office rides `subject`, as `confer`. Rows `Tenure.until`.
- **Why:** a lord unmaking a subordinate.
- **Falsifier:** realm ex > 0 (15/0).
- **Blocker · nj:** seat referents; H-91 (`hole_register.yaml:1131`) · no for the hook.
- [SUPERSEDED by §10.1, §13 / K-25, R-4]: the office comes from a held dispensation's `terms` through the enabler; the suite recommends no basis for deposing a top seat.

### `speak`
- **Etymology · fit:** OE *sprecan/specan* → emit `speech.made` about a referent; no hearer, nothing said. STRAINED — speech has an audience; the row has none and carries no `said` (`options.py:193-202`).
- **Earns:** REDUNDANT-WITH `tell` — bystanders hear a `tell` by presence (`verb_table.yaml:887`).
- **Group · module:** G12 · none yet.
- **Reach:** a referent, nothing carried. **Not:** a motion (`utter`); a seat's proclamation (→ `proclaim`).
- **Hook:** hooked. Proposal: cut, or give it `tell`'s `holds` conjunct.
- **Why:** what dies — speech about what one knows nothing of.
- **Falsifier:** leaves the executed set; `test_seen_claim.py:55`.
- **Blocker · nj:** none · **yes** — cutting a §E3 row, step 4 [CONFIDENCE: medium]. Settle with a corpus run withholding `speak`: if claim counts and check R3 hold, cut.
- [SUPERSEDED by §3.5]: retained, THIN — no cut and no new conjunct; nj no.
- [SUPERSEDED by §3.4 / K-34]: a seat's proclamation is none-yet — `proclaim` is deferred with its readers.

### `succeed`
- **Etymology · fit:** L *succedere* → OF *succeder*; follow in place → the HOLDER designates an heir. STRAINED — the heir succeeds; the actor designates. Plain alternative `designate` (proposal); `succeed` is also the tenure kind (`rosters.yaml:115`).
- **Earns:** THIN — no reader (`carriers.py:939-942`), no heir operand (`verb_table.yaml:839`).
- **Group · module:** G7 · world fact.
- **Reach:** a held office or estate; heir unbound (`:829-839`). **Not:** seat (`confer`); regency (`confer` + term, WIDEN); inheritance at death (unowned).
- **Hook:** the heir via the known-person fan (`to` beside `subject`). Reader: `conferral_bases` is closed at appointed/elected/annex (`rosters.yaml:1737-1755`), so succession fills no seat. Rows `Tenure.since`.
- **Why:** dynasties (`verb_table.yaml:840`).
- **Falsifier:** `test_u7_own.py:42` shrinks; a `person.died` followed by the heir's `hold`.
- **Blocker · nj:** ED-IN-0256 ruling (2) · **yes** — step 5: adding a basis amends an `open: false` roster, "a design change" (`rosters.yaml:1745`).
- [SUPERSEDED by §3.5, §13 / K-24, R-5]: the rename is deferred until the row gains its operand; the suite recommends an `inheritance` basis as a later step.
- [SUPERSEDED by §13.5, §14.9 / K-40]: "no reader" rests on `verb_table.yaml:839`'s decline note and a search, not on `carriers.py:939-942`; the `inheritance` basis dispatches to a rule table, the first rule the designated heir.

### `surveil`
- **Etymology · fit:** back-formation from *surveillance* (F *surveiller* ← L *vigilare*) → observe a Rung one stands at. FITS.
- **Earns:** THIN; the person case and Exposure have no home (`verb_table.yaml:1084`).
- **Group · module:** G11 · none yet.
- **Reach:** a Rung stood at (`:1077-1083`). **Not:** a person over time (WIDEN, §9.6); intercepting letters (unowned); planting an agent (composed: `oblige` + `conceal`).
- **Hook:** hooked. Route none.
- **Why:** the covert act canon prices (`rosters.yaml:2205`).
- **Falsifier:** the corpus executed set.
- **Blocker · nj:** ED-FI-0009; work item 4.5 · no.
- [SUPERSEDED by §9.7 / K-16]: the person case is held until an `any` combinator is ruled, not widened; Exposure is a Query (§8.1).
- **Survey interrogation (§6.3):** APPLIES (P52 countermeasure, P57 trace and counterintelligence, P6, P12) — counter-espionage is investigation of the one hiding. Its producer reads the log's Events at the watched Rung across the season, which the actor need not have witnessed; degree as `examine`.

### `survey`
- **Etymology · fit:** AN *surveier* ← ML *supervidere* → commission a faction sheet. FITS (`verb_table.yaml:848-851`).
- **Earns:** YES (`effects_information.py:322-386`).
- **Group · module:** G6 · world fact.
- **Reach:** a faction, or a person under one, in one's own ledger (`:859-862`). **Not:** a rung (WIDEN, §9.6; declined at H-169 limit 6); census (unowned); yield assessment (unowned).
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
- **Blocker · nj:** `sigma`'s `REFUSED` raises an uncaught `Unspecified` (`resolve.py:585-590`) — an SC-lane observation · no. The declared beneficiary disagrees with the code (Appendix D, c).
- [SUPERSEDED by §9.7 / K-15]: the lie is deferred to the telling workplan's G7, a decision-layer change at `said_of`, not a row widening.

### `thread_read`
- **Etymology · fit:** OE *þrǣd* + *rǣdan* 'interpret' → a finding gated on Thread Sensitivity ≥ 30. FITS (canon term, `verb_table.yaml:959-960`).
- **Earns:** THIN — not admitted (`:1097`; H-85).
- **Group · module:** G11 · none yet.
- **Reach:** a TS-gated finding. **Not:** threadwork (deferred, plan 27/29f).
- **Hook:** needs a per-person TS value and a gate stem; `knowledge_kinds` is the taxonomy half (`rosters.yaml:1184-1196`). Rows none.
- **Why:** P-08's barrier made mechanical (`canon/02_canon_constraints.md:50`).
- **Falsifier:** enters `resolvable_verbs()`; `test_u7_own.py:42` shrinks.
- **Blocker · nj:** H-85; plan 27/29f (`verb_table.yaml:1103`) · no.
- **Survey interrogation (§6.3):** APPLIES exactly — P29's background flag made metaphysical by P-08 (`canon/02_canon_constraints.md:50`). It waits on H-85; `train` stays excluded from Thread Sensitivity (K-20).

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
- **Reach:** own rung → a rung; `kind`, `amount`; renews obligees via a seat (`:1137-1149`). **Not:** Records (`give`); seizure (→ `seize`); treaty tribute (needs the treaty state, §8.1).
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
- [SUPERSEDED by §9.2 / K-29, K-34]: a declaration of war is this verb — a `WAR`-mood Proposition, read by `faction_q.at_war` once committed; `proclaim` is deferred with its readers, so a seat's edict is none-yet.
- [SUPERSEDED by §8.1 / K-35]: a charge is this verb too — mood `HOLDS`, subject the accused; a computed `utter` sets no mood, so a computed charge, like a computed war, waits on a source (§14.9).

### `work`
- **Etymology · fit:** OE *weorc* → alter `Site.condition` by a declared delta, else advance a works' fabric. MISFIT — labour produces, and yield is MATTER's (`Rung.yield`, `write_matrix.yaml:316-322`); the row does `restore`'s rise under a floor (`effects_economy.py:73-77`).
- **Earns:** REDUNDANT-WITH `restore` in computed play (183/0, `requirements.yaml:676`).
- **Group · module:** G9 · world fact.
- **Reach:** a floor-gated advance of a works (`effects_economy.py:73-96`). **Not:** wage labour (unowned); practice (→ `train`).
- **Hook:** fold into `restore`, or give labour a produce write (a Part D change). Rows `Site.condition`.
- **Why:** nothing `restore` lacks.
- **Falsifier:** leaves the always-refused pin (`test_season_shape.py:7624`).
- **Blocker · nj:** H-165 limit 2 · **yes** — cutting or re-purposing a §E3 row, step 4 [CONFIDENCE: medium]. Settle by grepping hand-built `work` acts with declared deltas.
- [SUPERSEDED by §3.5 / K-09]: retained, THIN, with its declared delta restricted to ≥ 0 so `sabotage` owns the negative sign; no fold, no produce write; nj no.

---

## Appendix B. The 62 act families and their evidence

One class per family, against the resolved suite (§5). Evidence names the game and act, the repo
document, or the historical procedure; bracketed ids are extraction rows. *R* `research/`; *P1*
governance proposals; *P2* narrative and play proposals; *C* code-side demand; *G1* detective games; *G2*
CK3 and RTK; *H1* history.

| # | family | class · verb | evidence |
|---|---|---|---|
| 1 | Question a person | COVERED · `interview` | *Pentiment*, questioning townspeople [G1-02]; *Disco Elysium* dialogue [G1-21]; *Lacuna*, interrogating suspects [G1-54]; *L.A. Noire*, notebook topics [G1-63]; *Shadows of Doubt*, sweet-talking witnesses [G1-92]; parliamentary questions to a minister [H1-31]; the Venetian Collegio receiving an embassy [H1-97] |
| 2 | Inspect a place, body or object | COVERED · `examine` | *Pentiment*, inspecting a body or inscription [G1-03]; *Disco Elysium* [G1-20]; *L.A. Noire*, the crime scene [G1-61]; *Shadows of Doubt*, prints [G1-84]; the coroner's view of the body [H1-161]; reading a person, witnessing a scene [R1-61] |
| 3 | Read, decipher records | COVERED · `research` | *Pentiment*, codes and invisible ink [G1-07]; *Shadows of Doubt*, call histories and emails [G1-85], receipts and phone books [G1-87]; Walsingham's cipher secretary [H1-179] |
| 4 | Watch a place; tail a person | DEFERRED · the place is `surveil`'s; the person waits on a grammar disjunction (K-16) | *Pentiment*, following a suspect unseen [G1-04]; *Shadows of Doubt*, CCTV [G1-86] and tailing a citizen [G1-91]; CK3's Spymaster finding secrets and disrupting schemes [G2-20, G2-21]; the State Inquisitors watching envoys [H1-187, UNVERIFIED]; the table's person case with no home (`verb_table.yaml:1084`) [C-16] |
| 5 | Evidence board | COVERED · `reconstruct` (+ SYSTEM) | *Lacuna*, assembling motives [G1-55]; *Shadows of Doubt*, the case board [G1-88] |
| 6 | Denounce, accuse | COVERED · `utter` of the charge (mood `HOLDS`, subject the accused) + a `petition` whose `terms` names it; testimony is each witness's own `commit` to it (K-35) | *Pentiment*, accusing at the hearing with the proof gathered [G1-10]; *L.A. Noire*, accusing a lie [G1-65]; informing to the Inquisition [P2-66]; the *bocca di leone* [H1-105]; *denunciatio* [H1-116]; the jury of presentment [H1-157]; informers before the Ten [R1-41] |
| 7 | Open an inquiry, case, impeachment | COVERED · `open_case` (a case file of kind `text`) | the Archdeacon's inquiry in *Pentiment* [G1-11]; a bill's first reading [H1-13]; impeachment [H1-27]; a select committee [H1-32]; the Avogadori's prosecution [H1-102]; inquest *ex officio* [H1-118]; a heresy case filed with a 2–4-season term [P1-37]; heresy investigation [R1-38]; *quo warranto*, *residencia* [R1-39]; staged accusatory procedure in seven-plus cases [C-03] |
| 8 | Summons, writ, warrant, charter, safe-conduct | COVERED · `issue`, a `dispensation` distinguished by its `terms` | writs of summons [H1-01]; the royal writ [H1-53]; citation and contumacy [H1-119]; the safe-conduct [H1-153]; warrants of arrest or search [H1-168]; torture by warrant [H1-183]; charters and franchises [R1-18]; warrants overriding an assembly [R1-43] |
| 9 | Hear, try, judge | WIDENED · `determine` contested | *Pentiment*'s judgement and sentence [G1-12]; *L.A. Noire*, charging one of two suspects [G1-66]; *Shadows of Doubt*, resolving the case [G1-89]; second and third readings [H1-14]; the impeachment trial [H1-28]; the Forty [H1-103]; the public sentence [H1-125]; the consistory [H1-138]; condemning a doctrine [H1-150]; the inquiry verdict — tribunal recommended / inconclusive / exonerated [P1-40]; trying a heresy case [P2-67]; a graded hearing (H-162) and the four unseeded procedure games [C-02]; ordeal and judicial duel [H1-155, H1-156; P1-25] |
| 10 | Sentence | OUTCOME — the disposal's kind: `oblige`, `custody`, `ban`; death is `custody` + `fight` (R-1) | penance [H1-127]; imprisonment [H1-129]; relaxation to the secular arm [H1-130]; execution [H1-174]; *Pentiment*'s execution [G1-13]; execution and erasure [R1-36]; a sentence read as a job (H-173) [C-04] |
| 11 | Confess, swear, abjure | COVERED · `commit`, `tell`, `release` — swearing and testimony are `commit`s to the charge (an oath is an utterance, `01_AXIOMS.md:1399-1403`); a confession is `interrogate`'s `confession.made`, whose claim value is the charge's id (K-35) | swearing to answer truthfully [H1-120]; abjuration [H1-126]; compurgation [H1-154]; abjuring as releasing the commitment (`03_INQUIRY.md:280`) [P1-42]; `confession` as a rostered proof (`rosters.yaml:1828`) [C-10] |
| 12 | Excommunicate, interdict, absolve | WIDENED · `determine` disposing `ban`; `pardon` (interdict deferred with `proclaim`, K-34) | CK3, excommunicate and lift [G2-54]; papal release from oaths [H1-77]; absolution [H1-128]; excommunication [H1-136]; interdict [H1-137]; the roster's Excommunication [P1-12]; a Cardinal's excommunication term [P2-68]; `church_standing` with no producer [C-06] |
| 13 | Edict, law, coinage, emergency | DEFERRED · `proclaim` deferred with its readers (K-34); its `edict` and `emergency` kinds wait on a reader each (K-11) | edict and proclamation [H1-54]; the inquisitor's edict of grace, a 30–40-day window for self-denunciation [H1-117]; censure, embargo and outlawry in the faction roster [P1-11]; coinage [H1-64]; the dispensing power [H1-66]; debasement and recoinage [R1-23]; edicts and emergency decrees [R1-43]; martial governance [P1-05]; the Policy Instrument [P1-60]; a state of emergency [C-32]; CK3, changing a realm law [G2-41] |
| 14 | Motion, debate, vote, veto | COVERED · members' own `commit`s, counted by a Query (motion `utter`, speech `tell`, veto SYSTEM) (K-07) | moving a motion [H1-04]; the division [H1-10]; supply [H1-24]; the *liberum veto* [H1-35]; the Senate's ballot [H1-95]; casting a vote [P2-31]; argument moves as data [P2-37]; speech kinds [P1-17]; parliamentary manoeuvre [P1-59]; holdout in a consensus body [P1-67]; vote, veto, conditional assent [R1-02]; calling and casting a vote [C-34] |
| 15 | Elect, conclave, lot | COVERED · members' `commit`s + `confer` basis `elected` (lot SYSTEM) | the Speaker's election [H1-03]; electing a king, tanistry [H1-72]; the doge by lot and ballot [H1-81]; procurators [H1-107]; conclave [P2-74]; acclamation and election [R1-08] |
| 16 | Appoint, invest, ennoble | COVERED · `confer`, `establish` | CK3, granting a title [G2-36] and court posts [G2-46]; investiture [H1-45]; charters [H1-52]; appointment [H1-59]; ennoblement [H1-80]; appointing and recalling officers [R1-30] |
| 17 | Depose, strip | COVERED · `revoke` (a seat with no rung above: none, R-4) | CK3, revoking a title [G2-37]; expelling a member [H1-08]; deposing a king [H1-74]; trying or deposing a doge [H1-89]; conciliar deposition [H1-149]; deposing a sovereign [R1-07]; stripping and barring [R1-33]; seizing a higher seat [C-35] |
| 18 | Resign | COVERED · `release` | resigning an office (`proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:638-654`) [P1-20] |
| 19 | Heir, regency | WIDENED · `confer` + term (`succeed` THIN; R-5) | heir designation [H1-69]; regency [H1-70]; fixing the succession [R1-49]; CK3 inheritance under law [G2-64] |
| 20 | Homage, fealty | WIDENED · `oblige`, read by `purview_reaches` | homage and fealty [H1-43]; *diffidatio* [H1-44]; CK3, transferring or releasing vassals [G2-38] and swearing fealty [G2-39]; oath and homage [R1-48] |
| 21 | Declare war | COVERED · `utter` of a `WAR`-mood Proposition + the seats' own `commit`s, read by `faction_q.at_war` (K-29; `proclaim` deferred, K-34) | CK3, casus belli [G2-08] and holy war [G2-55]; war on a casus belli held as a record [P2-18]; declaring war with a compliance window [R1-04]; war authorization [P1-15]; a graded war posture [C-38] |
| 22 | Truce, peace, treaty, alliance, tribute, cession | GAP · `covenant`, kinds `treaty` and `alliance` (cession: widened `give`; peace also the `release` of a war's commits; truce deferred, K-32) | CK3, peace and purchased truce [G2-14]; RTK alliance [G2-96]; cession [R1-05]; treaty, tribute, surrender [R1-06]; leagues [R1-15]; Treaty and Diplomacy [P1-07]; settling a surplus [P1-65]; binding agreements in five cases [C-40] |
| 23 | Muster, hire, allies | COVERED · `march`'s muster, `oblige` + `transfer` | CK3, calling allies [G2-10] and raising levies and mercenaries [G2-11]; Muster and Fortify [P1-01]; muster and recruit [R1-26]; non-march military acts [C-39] |
| 24 | Siege, blockade, fortify | WIDENED · `march` arriving at an enemy-held settlement — the siege a Query over the arrived army; its larder effect deferred (K-28) (fortify COVERED) | naval blockade [P1-03]; CK3 sieges [G2-12]; besiege, storm, terms [R1-29] |
| 25 | Conquer, raid, usurp | OUTCOME — a won or unopposed `march` writes occupation; title by `seize`, `give`, `release` or death (R-2 resolved) | conquest [P1-04]; CK3 raids [G2-13], war goals [G2-15], usurpation [G2-34]; the *chevauchée* [R1-58] |
| 26 | Arrest, custody, bail, ransom, hostage | GAP · `detain`, `pardon`; a hostage is composed — his own `move` to the receiving seat, that seat's warrant (`issue`), `detain`, and `pardon` on performance (K-38) | arrest in *Disco Elysium* [G1-32, UNVERIFIED], *L.A. Noire* [G1-67] and *Shadows of Doubt* [G1-90]; CK3, abduct [G2-24], imprison [G2-47], ransom and release [G2-51]; inquisitorial imprisonment [H1-129]; the constable's arrest [H1-160]; bail [H1-163]; *habeas corpus* [H1-173]; confinement and hostage-kin [R1-35]; arrest and restraint [P2-45]; hostages and fostering [P2-53]; no custody kind [C-05]; rescue [C-24]; hostages [C-25] |
| 27 | Interrogate, torture | GAP · `interrogate` — `confession.made` carries the charge (K-35); approach (calm, aggressive) is payload data, not a verb; a failure closes no line (§6.1) | pressing in *Disco Elysium* [G1-22]; Truth / Doubt / Lie [G1-64]; accusing a lie [G1-65]; CK3 torture [G2-48, UNVERIFIED]; interrogation with a notary [H1-121]; torture under limits [H1-122]; one scene per season [P1-38] |
| 28 | Execute | OUTCOME — `custody` + the enforcement seat-holder's `fight` (R-1) | *Pentiment* [G1-13]; CK3 [G2-49]; relaxation to the secular arm [H1-130]; execution of sentence [H1-174] |
| 29 | Outlaw, banish | WIDENED · `determine` disposing `ban` (an organization: `condemnation`, deferred; exile adds the exile's own `migrate`) | the Althing's outlawry, the imperial ban, *utlagatio* [H1-39]; proscription and exile [R1-34]; declaring a person or organization outlawed [P2-80]; CK3 banishment [G2-50, UNVERIFIED] |
| 30 | Seize, confiscate, suppress, search | GAP · `seize` (+ `examine`) under a warrant or occupation; [C-08]'s taking without consent and without a warrant is family 62's `steal` (R-8) | Church seizure [P1-14]; confiscation in thirds [H1-132]; the index [H1-134]; search and seizure [H1-175]; seizing church lands [R1-12]; seizing or burning property [P2-44]; suppressing a text or movement [P2-70]; taking a Record without consent [C-08] |
| 31 | Spy, infiltrate, informants | COVERED · composed: `tell` + the recruit's own `oblige` + `conceal` | Spy in the roster [P1-08]; a Riskbreaker operation [P1-47]; CK3 Spymaster [G2-20]; recruiting an intelligencer [H1-176]; planting an agent [H1-177]; a double agent [H1-181]; infiltration [P2-79]; recruiting and turning, thirteen cases [C-21]; an agent network [C-22] |
| 32 | Cover identity, deniability | GAP · `conceal` | Riskbreaker Identity [P1-48]; acting under cover [P2-77]; lapsing concealment, twelve cases [C-14]; deniable acts [C-15]; concealed-identity meters [R1-55] |
| 33 | Expose, publish | COVERED · `tell`, `give`, `survey` (exposure is a Query, §8.1) | exposing a covert body [P1-49]; an operation exposed [P2-78]; counter-intelligence [C-18]; disclosing or selling a secret [C-28]; addressing a public [C-30] |
| 34 | Blackmail, hooks | COVERED · a held Record + a `petition` whose `terms` is a demand + `tell` | CK3, fabricating [G2-17], blackmailing [G2-18] and spending a hook [G2-19]; pressing a fear [P1-28]; bribing an official [P1-29]; spending an obligation [P1-30]; evidence as standing leverage [C-29] |
| 35 | Bribe, gift, subsidy | COVERED · `give`, `transfer` | *Shadows of Doubt* bribes [G1-93]; CK3 gifts [G2-01]; RTK rewards [G2-71]; bribing an office-holder [P2-02]; endowing a public good [P2-58]; gifts for favour [R1-64]; funding a party [C-58] |
| 36 | Court, marry | COVERED · `tie / knot` (THIN) | CK3 personal and romantic schemes and marriage [G2-02, G2-03, G2-04]; courting [P2-14]; marriage with dowry [P2-52]; marrying into a house [R1-50]; forming a knot [R1-66]; marriage alliance [H1-76] |
| 37 | Slander, rumour | DEFERRED · the telling workplan's G7 (K-15) | slander [P2-15]; a competing account [P2-27]; RTK's estrangement [G2-90] and Dual Destruction [G2-93]; planting a rumour [R1-63] |
| 38 | Persuade, convert, preach | GAP · `argue` | *Disco Elysium* persuasion [G1-23]; CK3 conversion [G2-52, G2-53]; persuading one listener [R1-62]; preaching [R1-69]; spreading piety [P1-16]; changing convictions (H-62) [C-53] |
| 39 | Trade, wage, venality | COVERED · `exchange` (THIN) + `confer` | buying and selling in *Disco Elysium* [G1-29] and *Shadows of Doubt* [G1-100]; RTK trade [G2-78]; trading across a price gap [P2-55]; selling labour [P2-57]; selling office [R1-57]; venality and the *paulette* [H1-60]; a sold procuratorship [H1-109] |
| 40 | Borrow, distrain | DEFERRED · a `covenant` kind `debt` + `seize`, deferred together (K-14) | borrowing and default [R1-22]; settling or distraining [P2-56]; the Monte [H1-112] |
| 41 | Build, found, charter, patent | COVERED · `build`, `found`, `establish`, `issue` | CK3, creating a title [G2-33], holy orders [G2-56], buildings [G2-61]; chartered foundations [R1-16]; institutions [R1-17]; charters [R1-18]; durable works [R1-19]; patents [H1-114]; charters granted or denied [P2-60] |
| 42 | Survey, census, audit, visitation | COVERED · `survey` (rung subject WIDENED) | inquests and Domesday [H1-62]; visitation [H1-145]; the *curiosi* [H1-186]; *quo warranto* [R1-39]; resurvey [R1-45]; compiling a census [P2-24] |
| 43 | Envoy, legate | COVERED · `dispatch` + `give` (interposition SYSTEM) | ambassadors and *relazioni* [H1-98]; legates [H1-141]; an advocate or envoy interposed [P1-22] |
| 44 | Feast, coronation, progress | COVERED · `convene` + `utter`, `confer`, `move` | CK3 pilgrimage [G2-59] and activities [G2-60]; ceremonies [R1-47]; coronation [H1-41]; the itinerant court [H1-57]; crowning the doge [H1-87] |
| 45 | Heal, rest | GAP · `tend` | six cases [C-48]; *Esoteric Ebb*'s short rest [G1-46] |
| 46 | Train, educate | GAP · `train` | eight cases [C-49]; practising [P2-34]; CK3 education [G2-06] |
| 47 | Thread operations | DEFERRED · plan positions 27/29f | threadwork [R1-67]; thread operations [P2-43]; eleven cases [C-51] |
| 48 | Murder | OUTCOME of `fight` (+ `conceal`) | CK3 murder scheme [G2-23]; assassination [R1-56]; covert elimination [C-23]; *Disco Elysium*'s hanged man [G1-34] |
| 49 | Claim, coup, revolt | COVERED · composed (a claim as a Record kind is deferred; revolt SYSTEM) | CK3, claiming the throne [G2-25], seizing the realm [G2-29], factions [G2-42]; pressing a claim [P1-54]; revolt at a band [P1-56]; seizing a higher seat [C-35]; a coup [P2-62] |
| 50 | Mediate, appeal, stay, adjourn | COVERED · `determine`, `open_case`, `convene` | *Disco Elysium*'s strike mediation [G1-30]; appeal [C-11]; mediation [C-41]; stays [P1-24]; appeal by nesting [P1-26]; the parliamentary stay [P1-39]; prorogation, dissolution, adjournment [H1-19, H1-20, H1-21] |
| 51 | Recognize, endorse | COVERED · each holder's own `commit` | recognition given or refused [C-42]; recognition challenge and succession endorsement [P1-15] |
| 52 | Damage, raze | GAP · `sabotage`, `raze` | RTK's Hidden Poison [G2-89] and demolition [G2-84]; sabotaging a works [P1-62]; burning property [P2-44]; ending a Rung or Site (H-166) [C-60] |
| 53 | Admit, expel | COVERED · `oblige` + lapse (expulsion is withheld renewal) | admission to a community [P2-41]; expulsion [P2-46]; the Serrata [H1-90] |
| 54 | Defect, poach | COVERED · composed | defecting with one's holdings [P1-55]; poaching [P2-16]; defection [P2-30]; RTK's Unattended Home [G2-92]; turning a person [R1-54] |
| 55 | Challenge, accept | COVERED · a `petition` whose `terms` is the challenger + the acceptor's `fight` (K-23) | CK3 duel and trial by combat [G2-07]; challenge and accept [P2-32] |
| 56 | Privileged counsel | SYSTEM | four cases [C-13] |
| 57 | Regency through a seat | COVERED · `confer`; `Act.via` | delegation (H-108, stale) [C-37]; regency [H1-70] |
| 58 | Combat and battle moves | SYSTEM (inside the seams) | stratagems [P2-48]; fighting withdrawal [P2-49]; bout moves [P2-51]; grapple and feint [R1-59]; RTK attacks, fire, tactics, duels [G2-83 to G2-87] |
| 59 | Negotiation moves | SYSTEM (inside a bout) | propose, counter, probe [P2-38]; the four *upaya* [P1-66] |
| 60 | Events | SYSTEM | disaster, famine, epidemic, mutiny, riot, sack, succession crisis, defeat or default, a discovered plot [R1-72 to R1-80]; the bodies clock, interception, lost news, crises of conviction, starvation, coup, revolt, disaster, miracle [P2-13, P2-25, P2-26, P2-35, P2-36, P2-62 to P2-65]; heresy outbreak, inheritance, life events, locusts and plague [G2-63 to G2-65, G2-102]; quiet-season initiative, rumour, conviction drift, forgetting, a date firing, an inquisitor's arrival, revolt, a works stalling, hunger [P1-32 to P1-36, P1-45, P1-56, P1-63, P1-64]; individuation, institutional clocks, thresholds, world-health decay, hazards, awakenings, crises, fracture, endings, loyalty reassessment, expiry [C-50, C-57, C-66 to C-74] |
| 61 | Inner mechanics | SYSTEM (§10.3) | the non-act mechanics of both games tables |
| 62 | Steal, pilfer | GAP · `steal` (R-8; K-39) — added in revision 4 | *Esoteric Ebb*, "steal anything in sight" [G1-38]; *Shadows of Doubt*, stealing a document on a side job [G1-98], and the survey's Entering family, whose verbs include *steal* beside *sneak*, *pick* and *climb*, access at the risk of a fine (P34); CK3, the steal-an-artifact scheme, effect inferred from its name [G2-26, UNVERIFIED]; taking a Record without consent [C-08]; the Riskbreakers' extralegal infiltration and the Cardinal of Justice's text suppression (`rosters.yaml:1544`, `:1536`) |

---

## Appendix C. Evidence index by source

One line per source family: what was read, and what was not. The working tables themselves are not
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
- **Narrative and play proposals** — read: emergent-narrative primitives v2 00–01 and v1 00, 06, 05 §8, 04
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
  *Backbone*), *Shadows of Doubt* (ColePowered, published by Fireshine Games; early access 24 April 2023,
  full release 26 September 2024). Identities, developers and years were web-checked
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
  template; the Byzantine *agentes in rebus*). Every "verified" source is a secondary summary read by an
  extraction pass. Not covered: Ottoman, Chinese, Islamic, Mongol and Hanseatic governance. Several
  Venetian details (the Ten's voting thresholds, the *bocca di leone*'s witness rule, the cipher office)
  and tanistry stay [UNVERIFIED].
- **The independent audit pass (revision 2)** — opened, by its own account: the 44 rows' structural fields
  and 19 cited notes in `verb_table.yaml`; every loader invariant in `data/verbs.py:431-822`;
  `rosters.yaml` 101–215, 280–320, 388–410, 416–444, 484–491, 570–577, 995–1160, 1500–1590, 1613–1835,
  2150–2240; `state/carriers.py` (Term, Tenure, `Act.via`, Record, Rung); `state/gate.py`'s bases and
  `purview_reaches`; `data/requires.py`'s forms, stems and `all`; all 37 `write_matrix.yaml` rows and
  `retired:`; `data/arrangements.py` and `arrangements.yaml`; the cited `options.py`, `predicates.py`,
  `resolve.py` and `effects_*` sites; hole rows H-44, 52, 62, 84, 85, 91, 94, 101, 108, 156, 162, 163, 165,
  166, 169, 173; every live ED-IN-0210 row and ED-IN-0279's three rows; `01_AXIOMS.md` AX-1, AX-5, T-h,
  §E.1; `04_CODE_ARCHITECTURE.md` §A.3, §B.2 and PART D rows 1, 8, 14; canon P-01..P-15 and GD-1..3; the
  proceedings `04_VERBS.md` §B.2 and `21_RECONCILIATION.md` C-1 and PART E; `03_INQUIRY.md:176-193`. It
  re-ran no count.
- **The march analysis (revision 3)** — opened the `march` path end to end (the verb row, `sides_of`,
  `_contest`, the mass-battle wrapper, `_eff_march`, ENCOUNTER), the holder and muster Queries, `at_war`,
  the gate's bases, the write matrix's Tenure and `travel_leg` rows, H-148 to H-152, H-166 and H-175, and
  `test_march.py`; the author re-opened each load-bearing site (§14.3). It re-ran no count.
- **The survey (revision 4)** — *Mechanics of Inquiry, Speech and Rule*, prepared 3 October 2026,
  supplied by Jordan and not committed. Read whole by the survey interrogation and by the author. It
  covers *Pentiment*, *Esoteric Ebb*, *Lacuna*, *L.A. Noire*, *Shadows of Doubt*, *Return of the Obra
  Dinn* and *Tails Noir* in depth; *The Republic of Rome*, *Her Story*, *Disco Elysium*, *Papers,
  Please*, *Sherlock Holmes: Consulting Detective*, *Ace Attorney* and *Twilight Struggle* briefly; and
  *Crusader Kings III*, *Hearts of Iron IV* with La Résistance, *Espiocracy* and *Suzerain* from the
  grand-strategy side. It has no *Romance of the Three Kingdoms*. Its evidence caveats are carried in §1.
- **The survey interrogation (revision 4)** — opened, by its own account: the survey; this document's
  revision 3 and both games extraction tables in full; all of `verb_table.yaml`; `witness.py`,
  `epistemic.py`, `resolve.py`, `contest.py`, `sigma.py`, `world_q.py`, `person_q.py`, `options.py`,
  `choose.py`, `budget.py`, `matter.py`, `gate.py`, `attribution.py`, `carriers.py`, the cited effect
  bodies, `calendar.py`, `census.py`; `rosters.yaml`, `write_matrix.yaml`, `arrangements.yaml` 1–130 and
  the hole rows it names; `01_AXIOMS.md` AX-1 to AX-7, T-a to T-l and §E.1.6–7; canon constraints 34–90.
  Not read: `.designs/`, `.audit/`, the inquiry proposal, `offices.yaml` beyond a search (no Riskbreaker
  seat row found by name). The author re-opened each load-bearing site (§14.3). It re-ran no count.

---

## Appendix D. Table/code and source/source disagreements

Observations met while checking, recorded where they were found. None is acted on here; the owner of each
file decides.

| # | disagreement | sites |
|---|---|---|
| a | The `kill`/`wound` split is still planned, and `:467` says "THE SLASHED NAME SURVIVES THIS COMMIT", stale since the 2026-09-29 rename | `verb_table.yaml:442-448`, `:467` |
| b | H-108 reads "`Act` CARRIES NO `via`", grade `absent`; `Act.via` is live and the gate reads it — the row appears stale (its `unblocks:` — regency, governors, councils — is the regency state) | `hole_register.yaml:1571-1581`; `state/carriers.py:543-550`; `loop/resolve.py:114-118` |
| c | `tell` declares `beneficiary: subject`; since T4 the person told is `to`, and `beneficiary_of` resolves `subject` to the topic | `verb_table.yaml:875`, `:886-887`; `decision/choose.py:87-88` (per pass 1) |
| d | `forge` emits `record.created`; its matrix row emits `record.forged` | `verb_table.yaml:312`; `write_matrix.yaml:265` |
| e | `_ch_chronicle`'s docstring says the eight `binding_decision` verbs are all unresolvable; there are nine such rows and eight are admitted (all but `succeed`) | `engine/season/epistemic.py:536-540`; `resolvable_verbs()` |
| f | P-03 reads "GM is the rendering engine" against "there is no GM" — cross-lane observation | `canon/02_canon_constraints.md:45` |
| g | Layer 1 row 15 refuses a `budget` office bonus; `budget.py` adds `budget_office_bonus` per live `hold` of **any** object, held Records included — and `utter` minting a hold would extend it to every Proposition. Cross-lane observation | `architecture/meta/04_CODE_ARCHITECTURE.md:202`; `decision/budget.py:57-58` |
| h | The pursuit-basis worksheet records `kill / wound` as "RULED 2026-09-20 NOT A VERB"; the decision-layer execution plan's draft cells add `kill`, `wound`, `fight`, `challenge`, `accept` for 42 verbs. Direction 3 sides with the worksheet | `proposals/2026-09-20-pursuit-basis-worksheet.yaml:149-151`; `proposals/2026-09-26-decision-layer-execution-plan/candidate_pursuit_cells.md:98-99` |
| i | NPC-038 gives the Cardinal of Justice `dispatch` where `offices.yaml` gives `convene`; the overlay names the difference | `engine/season/cases/exercises/NPC-038.yaml:25-27` |
| j | The seam-table comment lists social contest and mass battle as "refuses by name"; the prize manifest routes `a standing` and `a proposition` to `sigma_leverage` and `a field` to mass_battle [CONFIDENCE: medium — read, not run; the comment may describe the full providers rather than the interim ones] | `rosters.yaml:1003-1011`, `:1111-1153` |
| k | `remit_acts` is `open: true`, though its source line calls #353's five acts closed | `rosters.yaml:294-302` |
| l | The `release` row's notes place the typed grammar's `all` form at `data/requires.py:542`; it is at `:858` | line drift |
| m | The `march` row's note says Jordan ruled "nothing on the WINNING side"; ED-IN-0279's third row says "nothing specified for the winner" — silence, not a ruling (K-08) | `verb_table.yaml:607`; `registers/editorial_ledger_in.jsonl:34` |
| n | GD-2 presupposes a faction selecting actions (`select_actions(faction, world)`), against AX-1 and Layer 1's ban on a faction that acts — cross-lane observation, not ruled here (K-20) | `canon/02_canon_constraints.md:72`; `rosters.yaml:1026-1029` |
| o | `release`'s `domain_note` says the loader compares its domain with `tenure_kinds` minus `contain`; `RELEASABLE_KINDS` excludes `contain` and `reside` | `verb_table.yaml:754`; `data/rosters.py:453` |
| p | `T-m` admits an actor opening a `hold` on any non-seat object naming himself, with no other basis — the seat carve-out covers seats only — so a direct title write would pass on a first capture and fail on every recapture (`NotYours` on the non-owner close) | `state/gate.py:677-688, :707-710` |
| q | `sides_of`'s same-faction comment points to an "`H-150`-adjacent note"; the row is H-151 | `loop/sides.py:116-117`; `hole_register.yaml:3247` |
| r | Work item 4.5 says an investigation Failure deposits nothing; canon grades Failure as a false lead and a failed `reconstruct` as a wrong conclusion the player acts on — a claim with a wrong value, for which no value space exists (K-37) | `verb_table.yaml:972-973`, `:985-987`, `:1115` |
| s | The survey against itself and against the games extraction pass: (1) Finding 1 and P22 class *Shadows of Doubt* with *Lacuna* as accepting a judgment "whether or not it is right", while its own account of the resolution form says optional entries "earn extra credit when correct" and handing it in "raises social credit if correct" — graded at submission [CONFIDENCE: medium — neither source verified a wrong name's consequence; the extraction pass's G1-89 reads "right or wrong answer [consequence UNVERIFIED]"]; (2) the survey says *Esoteric Ebb*'s conflict is "resolved by dialogue and skill checks rather than combat", while the extraction pass's store-page row G1-41 has turn-based encounters with "violence as a last resort"; (3) the survey attributes P27, a line closed on error, to *L.A. Noire* only, while G1-22 has *Disco Elysium*'s failed press locking options (snippet); (4) *Pentiment*'s "no truth value" (P23) sits beside the extraction pass's finding that proof gathered widens what can be argued at the hearing — evidence-gated input with unverified output (G1-10) | the survey (Finding 1; Parts 1 and 3); the games extraction pass |
| t | AX-7's falsifier names the three `Claim`-constructing sites as `witness.py:191`, `:271`, `:361`; the event-kind deposit is at `:380` today, and `verb_table.yaml`'s investigation block cites `rosters.yaml:482`, `:487-491`, `:505-508` for text now at `:1008`, `:1013-1017`, `:1031-1034` — line drift | `architecture/meta/01_AXIOMS.md:307, :315-316`; `loop/witness.py:380`; `verb_table.yaml:974-980` |
