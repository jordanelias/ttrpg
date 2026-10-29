# Debate, persuasion and social-contest corpus — sorted by theme

## Status: **REFERENCE (2026-10-29).** An extraction, not a design. It allocates no `ED`/`PP`, moves no head, and asks nothing of a future session. **Every entry cites its source; read the source before relying on an entry** — the gatherers extracted and classified, they did not judge, and the adjudication (`2026-10-29-debate-fit-adjudication.md`) lists the entries it found stale or wrong.

**Scope note.** The proceedings design's own build is scope-banned from referring to earlier social-contest work (`proposals/2026-09-05-proceedings-subsystem/README.md`; HANDOFF_SC standing order). That ban binds *that build*. This file is a cross-corpus survey requested by Jordan on 2026-10-29 and does not lift it.

## What it holds

757 entries from seven lanes, each entry one mechanism, rule or finding with a `path:line` source: **CD** coded and ratified (110) · **PR** the proceedings-subsystem design (109) · **OP** other contest proposals and archived designs (110) · **GV** governance, parliament, faction and territory designs (107) · **CL** classical rhetoric, persuasion and negotiation theory (108) · **HP** historical politics and game precedents (108) · **NL** emergent narrative (105). Entry ids are `<LANE>-nnn`; gaps in numbering are entries a lane cut to stay under its cap.

**Sorting.** By *primary* theme (13 themes, listed below); an entry's other themes are shown as `(+X,Y)`. Within a theme, by authority class, most authoritative first: `CODED` (executes in the engine or a registry code reads) · `RATIFIED` · `INTENT` (ratified as intent) · `PROPOSED` · `ARCHIVED` (`.designs/`) · `NOTCODED` (a mechanism the design names that the code demonstrably lacks) · `RESEARCH` · `CLASSICAL` · `HISTORICAL` · `GAME` · `NARRLIT`. Entries about the not-adopted legacy kernel are `CODED` with a status saying so.

| code | theme | | code | theme |
|---|---|---|---|---|
| A | Agenda and salience | | H | Transfers of land, office and asset |
| B | Convening, venue, standing, procedure | | I | Disorder and failure modes |
| C | Argument and persuasion | | J | Record, memory and reputation |
| D | Judgment and voting | | K | Emergent narrative and churn |
| E | Negotiation and bargaining | | L | Architecture and coding constraints |
| F | Faction, patronage and corruption | | M | Persons as inputs |
| G | Outcome, binding and enforcement | | | |

Part 1 of this corpus holds themes A, B, D, J, L; `_part2` holds C, E, F, M; `_part3` holds G, H, I, K.

## Counts

| class | entries | | class | entries |
|---|---|---|---|---|
| CODED | 120 | | RESEARCH | 86 |
| PROPOSED | 120 | | HISTORICAL | 79 |
| INTENT | 95 | | ARCHIVED | 72 |
| NOTCODED | 45 | | NARRLIT | 43 |
| RATIFIED | 39 | | CLASSICAL | 30 |
| GAME | 28 | | | |

By primary theme: A 42 · B 97 · C 147 · D 76 · E 53 · F 28 · G 59 · H 33 · I 28 · J 23 · K 121 · L 32 · M 18.

## What each lane covered and did not (from the lanes' own reports)

| lane | covered | conspicuously absent or unread |
|---|---|---|
| CD | the eight arrangement rows and which keys code reads; the social-contest verb rows and effects; `judging_set`, `reception`, `proofs`; ED-SC rulings; Layer-1 constraints; v10 CR-34..39; the not-adopted kernel; the 2026-10-29 proposal | no vote/tally, Parliament seat, chair, order of speech, minutes, floor, negotiation, tax/levy/annex verb, bribery, veto, filibuster in code; some `src` lines in PROPOSED entries copied from the proposal's own citations (conf M) |
| PR | the proceedings design 00-21, the study, stress cases, the code that now builds part of it | source/03, 04, 07, 08; files 08, 09, 11-13; relay A-F (enter only via 17 and 18); atom rows beyond headers |
| OP | archived `social_contest_v30` and siblings; the verbs / system-description / subsystem-completion suites; the from-scratch argument design; the 2026-07/08 `.audit` contest reports | any ratified negotiation or ZOPA mechanism; the remainder of GATE_C, most greenfield/ideal suites |
| GV | archived faction/parliament docs (Parliamentary Transfer, Stay, Sacred Veto, Church Influence); the hierarchy ruling; r2 seats/writ/reach; SET-09; CR-32..39 | `faction_canon`, `faction_behavior`, `baralta_crown_claim`, r2 `04` and `05`; any rhetoric content in this lane |
| CL | Aristotle (pisteis, genres), Hermagoras/Cicero/Quintilian on stasis, Nyaya, Kautilya, Guiguzi/Han Feizi, Lawspeaker, petition/remontrance, negotiation psychology | Plato beyond one paragraph, Isocrates, Abelard, Boethius, Aquinas as debate, *disputatio* (etymology only), Aristotle *Rhetoric* II emotions; the "renaissance deliberation" file is not in the tree |
| HP | Rome, Carolingians, Reichstag/Golden Bull, Florence, Milan, Genoa, Venice, Ottoman, Han, Japan, Castile/Aragon, Althing, game precedents | Polish Sejm/liberum veto (named, never described), Magna Carta (one mention), Machiavelli/Guicciardini (cited without mechanisms), Dutch States, the Hanse assembly; about 35 lower-value entries cut |
| NL | the 42-source emergent-narrative corpus and 75-row apparatus; the churn principle; the narration package; thrust layer; endings machinery | Versu, Comme il Faut, Prom Week as read sources; the Sych 2023 thesis; J. Ryan thesis; Nemesis/Ingold/Sylvester primary talks; ED-IN-0225's own row |

## How to read an entry

`**ID** \`CLASS\` (+other themes) — mechanism \[the source's own status\] \`path:line\` · hook: the engine surface it touches · conf` — then one line of detail. `conf` is the gatherer's confidence that the entry is accurate to its source (H/M/L). About 35 entries run past the 30-word mechanism limit; they were not trimmed.

---

## A · Agenda and salience — 42 entries (CODED 13, RATIFIED 1, INTENT 3, PROPOSED 11, ARCHIVED 2, NOTCODED 1, RESEARCH 4, HISTORICAL 4, GAME 3)


### A / CODED

- **CD-019** `CODED` (+B) — open_case: a seat with remit 'determine' puts a person-matter before the room: mints a case file Record and fills the nearest open docket slot (or appends a dateless item). \[verb row open_case, verb_table.yaml:958; effect effects_information.py:274\] `engine/season/verb_table.yaml:958` · hook: verb open_case; World.docket; slot_for · conf H
  - slot_for walks up from the matter's place to the nearest sitting with an empty slot (venue is the match key, an assumption). A matter already docketed is declined. A computed case names no arrangement; only a hand-built act can name one.

- **CD-020** `CODED` (+B) — The docket is a list of items {date, matter, arrangement, petition}; CALENDAR forms an empty slot per fired sitting; a matter is before the room iff an item names it. \[code at world_q.py:193 docketed, :258 slot_for, :246 open_slots\] `engine/season/queries/world_q.py:193` · hook: docket; slot_for; docketed_under · conf H
  - A determination writes the item's matter back to None, keeping the slot, so the same sitting can hear the next matter ('one convene is a standing court'). Only a person-matter fills a slot.

- **CD-021** `CODED` (+G) — carry: whoever holds a petition puts it before the room: re-winds the petition's stages and appends a docket item whose matter is the petition's 'terms' (e.g. the accused). \[verb row carry, verb_table.yaml:108; effect effects_information.py:356 (IN-45)\] `engine/season/verb_table.yaml:108` · hook: verb carry; Record petition; docket · conf H
  - The one route by which someone WITHOUT a seat reaches the docket. Refuses (carry.refused) if the actor does not hold the petition, the matter is already docketed, or stages would not change. The matter choice (petition terms) is an assumption.

- **CD-022** `CODED` (+J) — petition: a person mints a Record of kind petition {terms, to, from}, addressed to a person and rising from a place, held by the petitioner. \[verb row petition, verb_table.yaml:1011; effect effects_information.py:614\] `engine/season/verb_table.yaml:1011` · hook: verb petition; Record kind petition · conf H
  - Grievance is a document with a counterparty. Its two closers (withdraw by petitioner, deny by receiver) are NOT built: both would close Record.exists, whose closer destroy_record declines on its eligibility (H-75). A petition cannot be answered by being refused.

- **CD-023** `CODED` (+B) — convene: a seat with remit 'convene' schedules a sitting, a Date at a venue above person rung, held by the convener's seat; an empty bench lets it lapse. \[verb row convene, verb_table.yaml:281; effect effects_governance.py:370\] `engine/season/verb_table.yaml:281` · hook: verb convene; Date; CALENDAR · conf H
  - Venue rides on the act's subject. A second identical convening by the same person at the same venue in a season is a no-op. CALENDAR then forms a docket slot only for a date with a holder. No invitation, summons or attendance list exists.

- **CD-024** `CODED` (+K) — A judge who heard a sitting fire and sits on its bench is asked a question about each docketed matter: the source that makes a bench consider cases. \[code at world_q.py:283 sittings_before; questions_for :2811\] `engine/season/queries/world_q.py:283` · hook: questions_for; sittings_before; claim_landed · conf H
  - Hearsay of a firing is not admitted; only a claim from the firing's tick. Without this, H-163 measured determine executing 0 times in shipped worlds. World-reading by construction (the room's docket is the room's business).

- **CD-025** `CODED` (+M) — A person answers questions in tiers: own ambitions, own offices' purview, deeds he feels strongly about, the need question, the rest. \[code at world_q.py:2654 attention_key (IN-57)\] `engine/season/queries/world_q.py:2654` · hook: attention_key; questions_for · conf H
  - This is the agenda-salience rule for individuals: who attends to what. Tiebreak inside a tier is the question_sources order then a content hash. Aggregation of many persons' salience into a shared agenda does not exist.

- **CD-026** `CODED` (+M) — Only two sources raise questions for a person: a claim landed in his ledger (including fired sittings, standing crossings), and the standing 'need' (ambition) question. \[roster question_sources [claim_landed, need], rosters.yaml:566\] `engine/season/rosters.yaml:566` · hook: question_sources · conf H
  - Folded from four to two (date_due, band_crossed measured zero). Petitions, crises and grievances reach a person only as claims he comes to hold. There is no 'issue' or 'agenda item' source independent of claims.

- **CD-068** `CODED` (+B,K) — Two seeded proceedings with zero authored acts run end to end byte-identical: convene, date fires, case opened, bench asked, determine, matter.determined whose causes walk back to the date. \[test file; THE BAR measurement (B-N, B-O); seeds picked from a sweep\] `engine/season/tests/test_sc01_the_bar.py:1` · hook: convene; open_case; determine; causes[] · conf H
  - Existence claim not a rate: 4 of 72 determinations walked to a date.fired; the rest were docketed before a sitting (a dateless item is determinable). At the shipped judge (pool 2 vs obstacle 2) most determinations are Failure. No test asserts execution in the realm.

- **CL-099** `CODED` (+G,B) — A petition exists in the engine: a Record of kind petition carried by the verb carry to a docket (writes Record.stages, DocketItem.matter, emits petition.carried), with a structurally required counterparty (ED-IN-0210: petition is the first verb where a counterparty is required), addressee read from a held faction sheet's head. \[code/registry: petition is a Record kind; carry verb docket-writes it (IN-45); engine/season/data/verbs.py:196 ED-IN-0210 ruling 2\] `engine/season/verb_table.yaml:112` · hook: petition Record kind; carry; DocketItem; hierarchy weights · conf M
  - Supersedes the 2026-06 research claim (RHET:359) that no petition subsystem exists in the repo; it still lacks the rank-indexed register, supplique/remontrance split, intercessor and Crown/Church addressee split the research proposed. Hierarchy weight petition -0.4 / 0.3 as 'the channel a subordinate has' (rosters.yaml:3202,3435).

- **HP-078** `CODED` (+B) — convene: calling a body, allowed when rank(subject.kind) exceeds the person tier or subject is none; writes a scheduled date and convening condition. \[code: verb_table.yaml convene row, grade ruled\] `engine/season/verb_table.yaml:281` · hook: verb convene · conf H
  - Jordan 2026-09-05: convene can happen at any scale except individual, people travel. Emits date.scheduled. This is the only agenda-setting/summoning act in the verb table that I opened.

- **HP-079** `CODED` (+G) — carry: the petition's holder carries it onto the docket, writing DocketItem matter, arrangement and petition; emits petition.carried. \[code: verb_table.yaml carry row, grade ruled; IN-45 built _eff_carry\] `engine/season/verb_table.yaml:108` · hook: verbs petition/carry; Record, DocketItem · conf M
  - Petition is a Record of kind petition held by the petitioner. Caveat: research/by_lane/SC_social_contest.md (dated 2026-10-16) says carry's effect is DECLINED, a no-op; the row text I opened says IN-45 built it, so the two disagree (the SC file predates the build).

- **HP-080** `CODED` (+E,G) — petition: a two-sided act needing an existing addressee Person and a Rung of origin; mints a petition Record; closed by withdraw (petitioner) or deny (receiver). \[code: verb_table.yaml petition row, grade ruled\] `engine/season/verb_table.yaml:1011` · hook: verb petition · conf H
  - ED-IN-0210 ruling 2 (Jordan 2026-09-10): petition is two-sided. Emits petition.filed. A person cannot petition themselves.


### A / RATIFIED

- **CD-067** `RATIFIED` (+B,J) — Three digest items await a proceedings carrier: P-4 procedure before the vote (agenda control, motion order, recorded defeat), V-4 acquisition layer, V-5 verb glosses. \[plan position SC-07, B10-Z, BLK a carrier per item; unbuilt\] `workplans/valoria_master_workplan_v10_part5.md:277` · hook: agenda; motion order (not built) · conf H
  - Exit for P-4: a carried-and-vetoed motion persists as a citable Record. Not in the set ED-IN-0290 ratifies as intent; stays reference until a carrier exists. There is no agenda control, no motion order and no recorded defeat in code.


### A / INTENT

- **GV-066** `INTENT` (+B,G) — A person is asked about a claim that landed in reach, or a need; reach(w,p) has four limbs: me, mine, the ladder above me, and purview (descendants of held seat rungs). Purview is a term of reach, not a fifth question source. \[RATIFIED AS INTENT ED-IN-0233; reading-only filter\] `proposals/2026-09-17-governance-and-holdings-r2/01_ATTENTION_AND_REACH.md:457` · hook: reach(w,p); question_sources [claim_landed, need] · conf H
  - Dates and crossings become claims; date_due and band_crossed question sources deleted (measured 0 questions each). Agenda salience for a person is thus structural: what is within their reach. A filter over what WITNESS deposited, never a broadcast fan.

- **PR-068** `INTENT` (+C,D) — What a matter is: a Proposition whose MOOD selects genre and ladder: HOLDS (assertion) -> forensic -> issue ladder, disposal a Tenure; OUGHT (uttered belief) -> deliberative -> no ladder, disposal an issue/levy/commit; no bench -> epideictic -> standing only. \[14 PROPOSED then ratified as intent; mood->genre derivation corroborated by an independent Fable synthesis\] `proposals/2026-09-05-proceedings-subsystem/14_THE_WORLD_IN_THE_ROOM.md:38` · hook: Proposition HOLDS/OUGHT mood; genre Query; DocketItem · conf H
  - 'Who owns this settlement' = HOLDS Proposition about a hold, issue ladder procedural->conjecture->definition->quality. 'Is it true' = conjecture rung, moves by tell. 'What to do about invasion' = OUGHT, proofs [], moves convictions x alignment. A matter is never the thing itself but a Proposition somebody uttered about it.

- **PR-070** `INTENT` (+K) — A matter about a POSSIBILITY (invasion) has no producer: WITNESS deposits from Events, and a future state has none. Lawful shape: someone utters a HOLDS Proposition asserting the threat and others commit or not (belief as commitment); nothing writes the commit that makes a person's fear legible to a bench. \[14 A.1 and P-24 (sharpest finding)\] `proposals/2026-09-05-proceedings-subsystem/14_THE_WORLD_IN_THE_ROOM.md:108` · hook: utter HOLDS threat; commit; Question sources; convene · conf H
  - Registered P-24. Also B.1: a proceeding cannot be raised by a fact - facts raise questions, questions candidates, and someone must decide to convene; a world where nobody convenes has no proceedings however bad things get.


### A / PROPOSED

- **CD-098** `PROPOSED` (+K) — A motion arises from strain (an existing query such as vacancies, uncontrolled, hunger, at_war, legitimacy) plus an INDEPENDENT legitimating trigger of a different claim kind. \[PROPOSED (2026-10-29), design only, CR-38's design file; HELD BACK from the merge default: its section 12 calls; sec 3\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:65` · hook: questions_for; _stamped; vacancies; uncontrolled; legitimacy · conf M
  - Research reports strain alone fizzles. Rides as a stamped standing occasion because a sitting question ranks tier 4, below every need. Motion kinds are a data roster, refused at load if naming no strain query or executing verb. A strain-band threshold is an unruled assumption.

- **GV-094** `PROPOSED` (+D,K) — Elections, councils and votes are declined for the settlement/governance completion: Parliament is RULED AND NOT BUILT (H-90); the count reader (M-COUNT) is social-contest's vote, so the elected basis gains meaning when that lands. \[PROPOSED (completion proposal T08), item declined at step 3\] `proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-08-settlements-governance-economy.md:57` · hook: M-COUNT; elected basis; IN-61 successions · conf H
  - Also: King dies at tick 0 in every seed and the throne stays empty; seven null-conferral seats never refill; heirless/successor loader rule belongs to v9 IN-61 (stopped on H-230). Run evidence: confer refills a based seat in seed 1 only, a self-conferral.

- **OP-027** `PROPOSED` (+B) — The writ emitted at open: the question (raised by world pressure, a topic the world did not raise should not be arguable), stakes as draft Record text, dials. \[PROPOSED CIP-5, EVIDENCED (absorbs W1 and C3)\] `proposals/social_contest_consolidation_integration_v1.md:335` · hook: venue.start_ground; Record draft · conf H
  - Coarse Appraise read, declared compromise axes, and the end (topos) each side argues from. Basis: Blades in the Dark announces parameters before the roll; Burning Wheel Statement of Purpose; no no-GM game determines outcome meaning after resolution, so stakes must be machine data before dice. Generalise _derive_vote (lowest-Stability faction proposes). Fork: whether declared end is mechanical or flavour.

- **OP-043** `PROPOSED` (+K) — No proceeding can debate the future: a claim about a future state has no producer, so 'what should we do about invasion' cannot reach a bench. \[PROPOSED gap SC-G31, SC-G34\] `proposals/2026-10-16-verbs/2026-10-16-verbs-21-gap-register-sc-and-gv.md:64` · hook: utter; commit; Person.pursuits · conf H
  - And no verb writes convictions in a proceeding ('the most important thing this proposal did not build'). Deliberative argument types (the good and the advantageous) cited. Together with SC-G34 (argue must move Person.pursuits but 'which weight and toward what' unnamed).

- **OP-045** `PROPOSED` (+G) — A computed petition is addressed to the person it concerns, so it cannot rise to the seat above its subject; deny and withdraw closers do not exist. \[PROPOSED gap SC-G03/G04/G06\] `proposals/2026-10-16-verbs/2026-10-16-verbs-21-gap-register-sc-and-gv.md:36` · hook: petition; deny; withdraw · conf H
  - Rank-indexed supplique and institutional remonstrance as check are not modelled. Remonstrance ladder cited: jussion -> iterated remonstrances -> lit de justice. Silence beats refusal (R-CHOICE). Petition as accusation: a petition whose terms name the accused.

- **OP-067** `PROPOSED` (+B) — A motion must be Held (someone holds the proposition), Rooted (a ground ends in a firsthand occurrence) and Ripe (a chain of shared subjects reaches the prize allocated at the sitting's standing date). \[PROPOSED\] `proposals/2026-08-29-valoria-from-scratch/08_argument.md:284` · hook: standing dates; subject chains · conf H
  - Freshness is a property of the coupling, not a decay timer: old grievances never weaken but need a hook within the venue's coupling depth; revival compounds via a pattern counter.

- **OP-075** `PROPOSED` (+K,I) — Grievance as churn without clocks: petitions dropped accrue grievance and carried-and-won petitions mitigate; suppression adds fear-of-acting not changed stance, and the grievance claim is told to children. \[PROPOSED\] `proposals/2026-08-29-valoria-from-scratch/09_churning_world.md:560` · hook: petition drop/carry; stance deposits; hearth transmission · conf H
  - So the next petition assembles in one season instead of four (a lower trigger with no threshold object). Only clock-driven quantities are matter, bodies and memory confidence; every social quantity moves only when an act causes an event.

- **OP-076** `PROPOSED` (+B,F) — Convener power: the Parliament's convener orders its items, and three items ahead of yours kills yours by seat capacity at no cost. \[PROPOSED play-space audit (2026-08-30), from-scratch suite; nothing ratifies\] `proposals/2026-08-30-play-space-coverage/04_seasons_duchies.md:126` · hook: convene; veto_holders; carry/amend/bundle/drop · conf H
  - The veto-holder can strip a carried motion's force (CARRIED-WITHOUT-FORCE) without striking the record row. Duchess Baralta's season: convene and order items, veto, issue dispensations (reach-capped: one establishment member per node), confer sub-remit, revoke only own appointees, dispatch, carry/amend/bundle/drop at a standing date. Called 'the cheapest real power in the game'.

- **OP-078** `PROPOSED` (+F,B) — Agenda composition by a clerk: `compose_agenda` costs one act and its input is the petitions the clerk HOLDS A CLAIM OF. \[PROPOSED\] `proposals/2026-08-30-play-space-coverage/02_seasons_crown.md:655` · hook: compose_agenda; petition drop; channel dispositions · conf H
  - Omissions deposit as drops. A clerk at standing 1 who reads every petition outranks a minister (volume filtered, not rank). Design serves the clerk better than the King: Almstedt reaches more outcomes per act than Almud's six remit acts.

- **OP-080** `PROPOSED` (+B,J) — When the proceedings subsystem is taken up, build procedure before the vote: agenda control, the chair's order of motions, and recorded defeat ('nearly free to implement'). \[PROPOSED recommendation P-4 (owner SC, when un-held)\] `proposals/2026-09-30-character-and-play-surface/02_against_precedent.md:83` · hook: proceedings subsystem; stance rows · conf H
  - Falsifier: a carried-and-vetoed motion persists as a citable record. Companions: P-1 let more acts write relationship stance rows with a cause; P-3 seat faction heads then let a head act (Old World goals crossed with houses, expiring with the person).

- **PR-081** `PROPOSED` (+K,M) — Sixteen/seventeen ranked opportunities: O-1 room remembers who spoke; O-2 obstacle reads hearers' ledgers; O-3 unmet-want term (initiation); O-4 pressing a fear; O-5 Overwhelming forces descent; O-6 told_by from channel; O-7 conviction moves by consequence; O-8 pressure as band crossing; O-9 Partial names the matter; O-10 proof weighed by remove and mirror; O-11 silence priced; O-12 forged record a proof until examined; O-13 aptness; O-14 four degrees of presence and defy; O-15 petition route; O-16 standing route erosion; O-17 licence as BandExtension. \[18 PART E opportunity register O-1..O-17; 19_PLAN instructs on most; none built; 21 supersedes O-1 mechanism\] `proposals/2026-09-05-proceedings-subsystem/18_FINDINGS.md:192` · hook: deposit rules; reception; Tenure.term; Q4 score term · conf H
  - Three unlock the rest: O-1, O-6, fan-out off total (one roster member, one deposit line, one sweep arm). O-14's Tenure.term is the only new field and buys return day, inquisition indefiniteness, overdue pressure. Each lists the play it creates.


### A / ARCHIVED

- **GV-104** `ARCHIVED` (+K,F) — Petition and Friction cards make agenda: a Petition card asks the governor to adjudicate (seeded by Local-Actor convictions and needs); Friction cards force Directive-versus-Need conflict; ignored petitions escalate. \[ARCHIVED; PROPOSAL (consolidation D1: card-deck canonical for play)\] `.designs/systems/settlements/reference/governance_play_redesign_v1.md:197` · hook: card families; Needs emission · conf H
  - Agenda is thus generated from state: unmet Needs (low Order gives a petition for justice; famine a relief demand; a Guild a charter request). New 2026-07-09 triggers: Guild seeks Ordenanza sanction, Cell Revolt, Patron's Rivals Move. Governor's AP cannot serve both Directive and Needs.

- **OP-019** `ARCHIVED` (+B) — Format follows context; a contest starts only when two opposed parties are present and the outcome is both uncertain and consequential. \[ARCHIVED infill of v30\] `.designs/systems/social_contest/reference/social_contest_v30_infill.md:26` · conf H
  - Let It Ride bars re-contesting a settled question unless circumstances changed. Do not call a contest where one side has no plausible case or the result is fixed by prior Domain Actions. Re-contest needs new evidence, new faction alignment, an intervening Domain Action or changed politics. Players know the format before it begins.


### A / NOTCODED

- **CD-079** `NOTCODED` (+B,K) — The nested run is unbuilt: 'speak' is one act whose single roll stands for the whole speech; no rounds, turns, rebuttal, reserve or stasis shift. \[speak requires_typed_note; hole H-163 limit; the proceedings design\] `engine/season/verb_table.yaml:1177` · hook: verb speak; nested run (not built) · conf H
  - The proceedings design's nested run (21_RECONCILIATION step 15) would spend proofs one at a time and sequence order. Until then 'speech_kinds', 'order' and the hoard-or-spend choice have no mechanism, and a sitting is season-granular.


### A / RESEARCH

- **CL-044** `RESEARCH` (+G,L) — Claim: no petition / appeal-to-sovereign subsystem existed in the repo (zero hits for petition, grievance, supplication, remonstrance, redress, intercession, clemency); proposed as new, rank-indexed, slot-fillable, with intercessor and Crown/Church addressees. \[RESEARCH proposal, dated 2026-06-02; negative claim made against the then-repo\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:359` · conf M
  - Claim dated June 2026 over 1,605 files; later proceedings work (Oct 2026) may have changed it, check other lanes. Proposal not authorised. Intercessor maps to the old NPC Regard/Reconcile mediation mechanic.

- **HP-054** `RESEARCH` (+B) — P12 Agenda Control (relatio): right to convene a body and state its question, with a draft resolution; the wording sets which stasis the body sits at. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:361` · hook: convene verb / venue · conf M
  - Held by office; based on Roman ius agendi cum patribus (T2). Fails if the question is fixed by the scenario: framing must be a player-contestable first move.

- **HP-062** `RESEARCH` (+F) — P20 Drafting Right (piaoni): whoever drafts the response to a submission frames what the superior ratifies; sovereign choice reduced to accept, reject or return. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:409` · conf M
  - Ming Grand Secretariat pasted proposed rescripts onto memorials (T2, two sources). Models bureaucratic power without a power stat; clerk who drafts outranks minister who signs.

- **OP-083** `RESEARCH` (+K,J) — Event-to-motion chain: a world event deposits a graded Precedent tag with required provenance, and a motion's subject must name a real tag on a real owner (including an edge). \[RESEARCH/critique of a PROPOSED suite (2026-08-29), verdict PARTIAL\] `proposals/2026-08-29-fable5-throughline-critique/03_findings_T7_T9.md:8` · hook: Precedent/Grudge tags; motion subject · conf H
  - So no motion can exist without an antecedent occurrence; this chain survived attack (finding UPHELD). Example: route_severed -> Precedent tag; treaty breach -> Grudge on the treaty edge; 'censure the crown over the Baralta treaty's breach' names a real tag, not a free-text pretext. Blocs give arguments parties without authorship.


### A / HISTORICAL

- **CL-039** `HISTORICAL` (+G,B) — English Ancient Petitions (SC 8, 17,000+ docs c. 1270s-1450s): appeals for redress split into complaints and requests; common (communal) vs private petition; form shifted c. 1350-1405 to 'high style' (showed, prayed). \[RESEARCH; TNA SC 8 session-verified (line 302)\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:302` · conf H
  - Government by grace: petition as primary subject-sovereign channel; who carried it (proctors, intercessors, patrons) shaped success; royal and papal petitions ran in parallel systems (Crown vs Church). Common/private maps onto faction-level vs character-level appeals.

- **HP-025** `HISTORICAL` (+B) — Venetian layering: Collegio (26: Signoria plus 16 Savi) sets the Senate's agenda and receives ambassadors; Senate (Pregadi, 60 to ~300) votes; Great Council ratifies constitutional matters. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:340` · hook: Consensus resolver (proposed) · conf H
  - No single chamber both proposes and disposes. Signoria = Doge, six ducal councillors, three heads of the Quarantia. Repo hook: an agenda-setting inner body emitting proposals that a larger body resolves.

- **HP-050** `HISTORICAL` (+J,G) — English Ancient Petitions and French supplique versus remontrance: petition is rank-indexed and intercessor-shaped; subject-to-grace and institution-to-check are two different instruments. \[FILED 2026-10-16 critical evaluation; reference\] `research/by_lane/SC_social_contest.md:62` · hook: petition verb (proposed) · conf M
  - The repo's RHET source says to build petition as two mechanics. The evaluation grades the marks unverified and internally inconsistent (confidence medium, recovered from a transcript).

- **HP-096** `HISTORICAL` (+B) — Spanish councils differ in agenda control: in the Council of State the king sets the agenda; in Castile he ratifies the councillors' conclusion. \[FILED 2026-07-09 research, proposals KEEP/CUT judged; most items needs_jordan or unratified\] `.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:133` · hook: none (proposed) · conf M
  - Proposed as differentiated council types (agenda-set blind-framing versus ratify accept/veto) with a latency-to-paralysis cost where ministries overlap (HAB-4). Valido as informal favourite gating what reaches the ruler (HAB-2).


### A / GAME

- **HP-086** `GAME` (+D,F) — Templates TM02 and TM03: price the verb, delay delivery, track bloc approval, then vote through a chamber, with lockout after change or failure. \[FILED 2026-10-22 tier-3 reference, not canon; claims tagged V3 (fetched) / V2 / M (model memory)\] `research/game_precedent_suite/THROUGHLINES.md:129` · conf M
  - Examples: Democracy 4, Victoria 3, Tropico 6, Suzerain; Victoria 3 and Bannerlord for proposals; the choice left to the player is which bloc to disappoint and whose vote to buy. Valoria status per the file: no bloc ledger (LACKS) and chamber vote tests-only.

- **HP-091** `GAME` (+D,E) — Suzerain: twelve story turns in which an Assembly sends bills to sign or veto (veto only while the constitution grants it), constitutional reforms and decrees, stat-gated decisions. \[FILED 2026-10-22 tier-3 reference, not canon; claims tagged V3 (fetched) / V2 / M (model memory)\] `research/game_precedent_suite/tutorials/T11_policy_sims.md:82` · conf M
  - Vote outcomes by seat count; no dice, failure comes from thresholds; consequences arrive later through news and triggered decisions. Budget allocation with a penalty for skipping a promised focus.

- **HP-092** `GAME` (+D,F) — Democracy 4: spend political capital to introduce or change policies, which move toward target over implementation turns; 20 voter groups; dilemmas block the turn; election by voter mood and coalition. \[FILED 2026-10-22 tier-3 reference, not canon; claims tagged V3 (fetched) / V2 / M (model memory)\] `research/game_precedent_suite/tutorials/T11_policy_sims.md:198` · conf M
  - Cannot cancel a policy the turn it is introduced; a coalition lowers capital. Tropico 6 adds faction demands where two factions ask at once and the player must side with one, plus protests answered by negotiate, concede or military.



## B · Convening, venue, standing and procedure — 97 entries (CODED 23, RATIFIED 4, INTENT 16, PROPOSED 14, ARCHIVED 9, NOTCODED 6, RESEARCH 7, CLASSICAL 1, HISTORICAL 17)


### B / CODED

- **CD-001** `CODED` (+L) — An 'arrangement' is a data row of thirteen keys defining a proceeding (disposal, bench_basis, floor, records_dissent, venue_min_rank, term_required, appeal_basis, interposed, order, proofs, disposes, disposal_reach, quorum). \[code at data/arrangements.py:156; loader refuses unknown keys\] `engine/season/data/arrangements.py:156` · hook: arrangements.yaml; ARRANGEMENTS dict · conf H
  - Eight rows seeded in arrangements.yaml; loader checks every value against a roster and raises SystemExit on a stray key. Claim under test: 'a proceeding is just defined parameters'. A thirteenth row needs no code change.

- **CD-002** `CODED` (+D) — parliamentary_debate row: open floor, bench disposal, rank order, records dissent, venue at duchy or above, reach realm, interposed [procedure], proofs [], disposes Record. \[row in arrangements.yaml:123 (loaded); only 'disposes' is read by code\] `engine/season/arrangements.yaml:123` · hook: arrangement parliamentary_debate; verb determine · conf H
  - Closest seeded row to a parliament; council_of_state is the same but closed floor, records_dissent false. Both load and validate, but determine DECLINES a row disposing Record (effects_information.py:433), so nothing heard under either can be disposed.

- **CD-004** `CODED` (+D,G) — legal_trial (open, appeal via determine, detain), tribunal (admitted floor, no appeal, ban, reach body), interrogation (closed, scripted, detain), inquisition_hearing (closed, appeal, ban). \[rows at arrangements.yaml:177-246 (SC-03a); loaded\] `engine/season/arrangements.yaml:177` · hook: arrangements legal_trial/tribunal/interrogation/inquisition_hearing; detain, ban · conf H
  - Which row disposes which Tenure kind (detain vs ban) is an [ASSUMPTION; medium]: secular bench imprisons, membership body excludes. Only disposes is read by code, via determine.

- **CD-005** `CODED` (+G,H) — excommunication_deliberation row: closed floor, rank order, appeal via determine, disposes ban, reach realm: a body disposing of an absent person. \[row at arrangements.yaml:265 (SC-04); loaded\] `engine/season/arrangements.yaml:265` · hook: arrangement excommunication_deliberation; ban · conf H
  - Eighth row. records_dissent false chosen over the old 'verdict_reasons: given' by an [ASSUMPTION; medium]. 'negotiation' (disposal mutual) and 'public debate' (disposal none) remain unseeded.

- **CD-016** `CODED` (+D) — A judge may bind a party only via a judging seat he sits in, over another person present within the bench's ground (jurisdiction follows presence, J-17). \[code at state/gate.py:752 may_determine\] `engine/season/state/gate.py:752` · hook: gate.may_determine; sits_over; determination basis · conf H
  - Same predicate used by the fold (refuses, emits determine.refused) and the write gate (would raise), so they cannot disagree. Presence not residence; revert option residence_of recorded at H-174.

- **CD-043** `CODED` (+G) — A council is one seat whose members have taken oblige to it; establishment_of(seat) lists them. Joining is the joiner's own act (members_by_admission). \[code at world_q.py:2184 establishment_of; verb oblige verb_table.yaml:936\] `engine/season/queries/world_q.py:2184` · hook: oblige; establishment_of; binds_bases · conf H
  - AX E.2.5: 'a council is one seat whose members oblige'. The determination's disposal oblige also makes a convict an obligee of the bench's seat. Membership is a Query over edges, not a stored list.

- **CD-046** `CODED` (+H) — 'Court Parliament' is a body under the Crown whose function string reads 'Recommends policies, nominates Ministers/Rectorates/Magistrates'; it is a label for an office's type, not a seat or a mechanism. \[roster office_bodies, rosters.yaml:1725-1820 (H-99)\] `engine/season/rosters.yaml:1725` · hook: office_bodies; Office.body · conf H
  - Function strings are quoted from worldbuilding_v30 and read by nothing that executes a parliament. Jarl Council and Inner Council are leader councils with 2 named members each (npc_behavior superseding politics).

- **CD-084** `CODED` (+D) — Dyadic counsel, Negotiation (typed envoy latitude, escalating instruments, win = agreement in the overlap) and Ceremonial (build standing, win = acclamation) are scaffolds that raise a stub error. \[kernel, NOT adopted (SC-05, ED-SC-0033); runs only in its own tests; modes.py:333-358 (SCAFFOLD stubs)\] `systems/social_contest/sim/contest/modes.py:333` · hook: none (kernel); NegotiationMode (stub) · conf H
  - The kernel never built the three non-adversarial modes. Negotiation is gated on SC P0 docket ED-SC-0003..0005. So neither the live engine nor the kernel has a negotiation resolver.

- **GV-047** `CODED` (+H,L) — Title ladder is world-gen data: King/Queen realm > Duke/Duchess duchy > Count/Countess province > Lord territory > Mayor settlement > Community Leader > Family Head > Individual (person). Parliament as separate sovereign power is ruled, not built. \[code: data read by harness/populated.py build_realm; H-90 text records the ruling as 'RULED AND NOT BUILT' for Parliament\] `engine/season/offices.yaml:143` · hook: titles domains; office rung anchor · conf H
  - Jordan 2026-09-02 (H-90): governing authority, sovereign power (Parliament, deliberately not monopolised in the ruler) and holdings are three different things; ladder models only the first. Lord may govern several unassembled territories. Delegation ('assign others of lesser rank to govern any of their holdings') registered open, not built.

- **GV-052** `CODED` (+D,C) — parliamentary_debate arrangement: bench disposal by determine, open floor, dissent recorded, venue at least duchy rank, speech order by rank, procedure may interpose, disposes a Record, reach realm. \[code: data row read by data/arrangements.py, thirteen-key closed schema; ratified as intent ED-IN-0288 for SC-03a rows\] `engine/season/arrangements.yaml:123` · hook: arrangement row parliamentary_debate · conf H
  - Keys: disposal, bench_basis, floor, records_dissent, venue_min_rank, term_required, appeal_basis none, interposed [procedure], order rank, proofs [], disposes, disposal_reach. A parliament is thus 'just defined parameters'. Disposing a Record is unbuilt: _eff_determine declines for Record/none disposal.

- **GV-053** `CODED` (+I,J) — council_of_state arrangement: same shape as parliament but closed floor and no dissent recorded; deliberation sealed, decree proclaimed. \[code: data row, same loader\] `engine/season/arrangements.yaml:145` · hook: arrangement row council_of_state · conf H
  - Differs from parliamentary_debate in floor (closed), records_dissent (false), and disposal_reach unchanged (realm). Illustrates open-versus-sealed deliberation as a parameter; also affects what reputational record a defeat leaves.

- **GV-054** `CODED` (+D,G) — Eight seeded arrangements dispose a tenure kind: arbitration oblige; trial and interrogation detain; tribunal, inquisition hearing, excommunication ban; the two assemblies dispose a Record. \[code: arrangement rows arbitration, legal_trial, tribunal, interrogation, inquisition_hearing, excommunication_deliberation\] `engine/season/arrangements.yaml:106` · hook: arrangement.disposes; appeal_basis · conf H
  - appeal_basis none or determine; interposed subsets of person/office/procedure/document/ceremony; proofs from record/testimony/oath/confession. Tribunal and excommunication finding closable by pardon. Four of twelve source games unseeded. No succession row (disposes hold) because determine has no hold site.

- **GV-055** `CODED` (+D,M) — determine: a judging seat's holder disposes a docketed matter, opening on the party the tenure kind the docketed arrangement disposes, graded by the contest's degree band; matter leaves the docket. \[code: _eff_determine; contested act since SC-03b\] `engine/season/loop/effects_information.py:419` · hook: verb determine; may_determine; DocketItem · conf H
  - Bench conjunct: actor sits in a judging seat whose ground holds the party's home. Failure writes nothing. Edge degree = Overwhelming/Success/Partial. Determiner's own pursuits (convictions) move by consequence. A second determination of one matter in one fold refuses.

- **GV-056** `CODED` (+A) — convene schedules a sitting: a Date comes due at a venue with a convening condition attached, held by the convener's seat; CALENDAR forms a docket slot that open_case fills. \[code: _eff_convene; verb row eligibility remit:convene\] `engine/season/loop/effects_governance.py:370` · hook: verb convene; Date.holder; DocketItem · conf H
  - Jordan 2026-09-05: convene may happen at any scale except person; a proceeding convenes at a place. Venue rides the act subject. Convening itself decides nothing (a clock may not produce an outcome); the sitting decides via determine. Holder-of-date rule is flagged ASSUMPTION.

- **GV-057** `CODED` (+D) — may_fill: actor sits in the exercising seat, seat is not the target, target declares a conferral basis, and the exercising seat has purview over the target's rung; may_revoke adds the revocation rule. \[code: may_fill / may_revoke predicates\] `engine/season/state/gate.py:675` · hook: Act.via; purview_reaches · conf H
  - Reflexive on the rung, exclusive on the seat: a holder does not fill the seat he exercises. Which basis each act may exercise (confer only for appointed?) is unruled, so all three bases pass today. Authority is a property of the seat exercised, not the person (H-90 superseded default).

- **GV-067** `CODED` (+H,F) — Court Parliament is a named Crown body whose function is only to recommend policies and nominate Ministers, Rectorates and Magistrates; Hafenmark's Inner Council and Varfell's Jarl Council hold two named members each. \[code: office_bodies roster read by build_realm; source worldbuilding_v30 s6.1\] `engine/season/rosters.yaml:1726` · hook: office_bodies faction/function · conf H
  - Jordan 2026-09-13 ruled npc_behavior_v30 superior to faction_politics_v30: the 4-5 member councils are SUPERSEDED. The 22 committees/dicasteries/ministries of faction_politics Part 7 are deliberately NOT built (read by nothing; extra apparatus forbidden). No Hafenmark parliamentary body exists as a seat; only a Chief Parliamentary Clerk in Ministries.

- **GV-068** `CODED` (+J) — The only parliament-named seat in the built world is Chief Parliamentary Clerk (NPC-008) with remit issue, body Ministries, Crown; the draft's Senior Parliamentary Chair for Hafenmark was superseded by the 2026-09-13 ruling. \[code: seat row off_parliamentary_clerk, [LIVE]\] `engine/season/offices.yaml:312` · hook: seat off_parliamentary_clerk · conf H
  - The draft row's own note recorded an unresolved cross-document conflict about faction. Peder Almstedt is one of five names the NPC-behaviour ruling drops from Hafenmark's council. So the engine holds a clerk, not a chamber: no voting seats for a parliament exist.

- **GV-069** `CODED` (+L) — Venue data lists Parliament as a function served by court/hall/moot-hall venues and gives it a seat precedence slot, with Parliament seated at S-018 Gransol (T8). \[code: venue data read at world build\] `engine/season/venues.yaml:140` · hook: venues serves; seat_precedence · conf M
  - Venue slugs court, hall, moot_hall serve [Crown, court, Parliament]; seat_precedence ranks Lowenritter, Einhir, Altonian, Schoenland, Parliament... S-018 'Hafenmark constitutional capital. Baralta's court. Parliament'. Gives a physical site for sittings; convening is rung-and-place-based.

- **HP-044** `CODED` (+D,L) — Parliamentary_debate arrangement row: open floor, dissent recorded, venue rank duchy, speaking order by rank, procedure interposition, disposes a Record, reach realm. \[code at engine/season/arrangements.yaml (loader data/arrangements.py); rows ratified as intent ED-SC-0039\] `engine/season/arrangements.yaml:98` · hook: arrangement keys floor, order, records_dissent, disposes · conf H
  - Sibling council_of_state row is closed floor, no dissent record, same rank/order. Eight rows seeded in total. I verified only the row text and that only data/arrangements.py validates most keys and the gate/effects code reads `disposes`.

- **OP-033** `CODED` (+L) — The `speak` verb is a CONTESTED act on prize 'a matter' (requires a live occasion whose docket names the subject) but writes nothing at every band. \[code at engine/season/verb_table.yaml:1177 (speak row); v9 SC-01 step 12\] `engine/season/verb_table.yaml:1177` · hook: verb speak; prize 'a matter'; provider social_contest.roll · conf H
  - Each band only differs in what the witnessed event emits. Opponent is the subject; a person never forms a speak whose subject is himself. Design intent was stance writes and docket growth; no value/carrier exists (H-63), so all four bands write nothing. No reader of speech kinds or proofs exists. verbs-11 calls the N-line 'FALSE today'.

- **OP-034** `CODED` (+G) — `determine` is contested via the social_contest provider on prize 'a proposition': the judge rolls against the docketed party; success opens the arrangement's disposal Tenure (oblige, detain or ban) on a Person. \[code at engine/season/verb_table.yaml:352 (determine row; contests at :383, ED-IN-0288 as INTENT)\] `engine/season/verb_table.yaml:352` · hook: verb determine; arrangements.yaml disposal; DISPOSABLE_KINDS · conf H
  - Pool is the judge's pool_default, obstacle obstacle_default under the H-213 ceiling for every party; band read by the single ladder. verbs-11: no Record disposal, so parliament/council arrangements (disposes Record) decide nothing.

- **PR-093** `CODED` (+L) — The arrangement row is CODED at THIRTEEN keys (15 - registers, verdict_reasons, stakes_grade + quorum, with disposal: declared) and loaded by one loader rejecting unknown keys; EIGHT of twelve games are seeded: arbitration, parliamentary_debate, council_of_state, legal_trial, tribunal, interrogation, inquisition_hearing, excommunication_deliberation. \[code at engine/season/arrangements.yaml (header :7-:47) read by data/arrangements.py; supersedes README 'nothing exists in engine/season'\] `engine/season/arrangements.yaml:98` · hook: arrangements.yaml; data/arrangements.py · conf H
  - Not seeded: negotiation (+envoys), audience/embassy, appeal, public debate (disposes standing outside the enum). No succession (disposes hold) row yet. Excommunication seeded as disposes: ban (not 'severs a commit' as 03 says). 'Remaining seven' header text stale by SC-03a/SC-04 comments. Opened the file; did not run the loader.

- **PR-101** `CODED` (+A) — Docketing is CODED: _eff_convene gives the Date a holder (Act.via), _eff_open_case fills the nearest open slot of a sitting whose venue holds the matter (world_q.slot_for) else appends a dateless item, and world_q.questions_for asks each judge on a fired sitting's bench about its docketed matters citing his date.fired claim. \[code (v9 SC-01 fired-slot step; tests dated 2026-10-16) - W26 proof in one seeded run\] `engine/season/tests/test_sc01_fired_slot.py:1` · hook: convene; open_case; slot_for; questions_for · conf H
  - Answers 21 C-5 docketing in part (via open_case slot rather than DocketItem.matter write). Step exit: seeded run twice with equal World.content_hash(). A case on a matter that is a rung fills no slot.


### B / RATIFIED

- **CD-056** `RATIFIED` (+D,H) — Delegation has three shapes needing no new primitive: a governor (establish, confer), a council (one seat, members oblige), a mayoral election (a Date fires, the judging set decides, determine opens the hold). \[AX E.2.5 (Layer 1, ratified)\] `architecture/meta/01_AXIOMS.md:1537` · hook: oblige; establishment_of; confer vs determine · conf H
  - Authority belongs to the seat, so a body with no authority of its own can decide who occupies it. Conferral is bought and owed, election canvassed, succession bred for: one primitive, three genres of play. Election path via determine not yet built (CR-35).

- **CD-064** `RATIFIED` (+D,F) — Planned (design-first): Court Parliament has no bench of its own; today parliamentary_debate's realm bench is the King's and Widow Regent's seats; a design file derives a landed bench. \[plan position CR-38, B10-19, DESIGN-FIRST; the design file is the 2026-10-29 proposal\] `workplans/valoria_master_workplan_v10_part4.md:404` · hook: judging_set; parliamentary_debate; Court Parliament · conf H
  - Candidate routes: grant determine to duchy-head seats, or an arrangement-level bench key (a fourteenth key the loader refuses). Flips parliamentary_debate to declared. Waits on CR-36. Unapproved at B10-18 close: the interim bench is frozen and named.

- **GV-029** `RATIFIED` (+L) — Five-rung hierarchy Country > Duchy > Province (conditional) > Territory (new) > Settlement; province exists only while one faction holds all constituent territories. \[RATIFIED - direct Jordan ruling 2026-07-13 (doc archived; no ED allocated at the time); propagation tracked-not-executed\] `.designs/systems/settlements/reference/scale_hierarchy_v1.md:11` · hook: hierarchy tiers; province existence condition · conf H
  - Overrules PP-726 'Territory=Settlement' and fracturing rule. Province is an emergent aggregation, not a fixed container; no fracture state-machine. Duchies unchanged (Valorsmark/Hafenmark/Varfell). Ruling text kept in an ARCHIVED doc; code status of tiers not verified here.

- **GV-031** `RATIFIED` (+G,H) — Two authorities bypass the chain of control: the national ruler may act on any tier, and Parliament has no direct chain of control but can forcibly impact any province, territory or settlement. \[RATIFIED Jordan 2026-07-13 (archived doc); quoted in task brief\] `.designs/systems/settlements/reference/scale_hierarchy_v1.md:128` · hook: chain-bypass authority (Parliament, monarch) · conf H
  - Parliament holds no fixed hierarchy position (not duke, not governor). Its cross-cutting reach is a hierarchy property, composing with Censure mechanics. Monarch likewise exempt from nesting. Gives Parliament a lateral, non-owning form of power rather than ownership.


### B / INTENT

- **GV-061** `INTENT` (+H,L) — A council is ONE seat whose bench is a Query over oblige: members join by their own oblige to the seat and leave by release; establishment is not a field and hold is 1-per-object. \[RATIFIED AS INTENT (v9), ED-IN-0235; grade paper; cites ARCH B.7 call 2 and AX E.2.5\] `proposals/2026-09-17-governance-and-holdings-r2/03_SEATS_AND_CONTENT.md:671` · hook: oblige tenure; establishment_of query · conf H
  - Admission is the joiner's own-eligible act, so no sixth remit act is needed (closes ARCH F.17). Restoration Movement's second leader obliges to the first's seat as the live instance. world_q.hold_force already raises on a second hold. Contrast: faction_politics lists N-member councils.

- **GV-093** `INTENT` (+A,J) — P-4: procedure before the vote (agenda control, chair's order of motions, recorded defeat) awaits a proceedings carrier; a carried-and-vetoed motion should persist as a citable record. \[workplan v10 SC-07, STATE BLK (a carrier per item); P-4 not in the set ED-IN-0290 ratifies\] `workplans/valoria_master_workplan_v10_part5.md:277` · hook: agenda; motion order; Record of defeat · conf H
  - Falsifier: a motion vetoed in a seeded proceeding that leaves no Record fails P-4. Reference only until each item has a carrier. Names agenda control, motion order and recorded defeat explicitly as unbuilt.

- **GV-107** `INTENT` (+J,L) — Player Surface Law: the player controls a person, so anything shown before they declare is inside a decision; a surface may not look at the world from a seat, only through what the person holds (ARCH C.11 refuses the 'player is not an actor' reading). \[RATIFIED AS INTENT (v9), ED-IN-0237; STANDS (not superseded)\] `proposals/2026-09-17-governance-and-holdings/03_THE_SURFACE.md:3` · hook: Surface Law L-1..L-3; cell states · conf M
  - Jordan: 'Players need to have an interface with which to engage with the game world.' Read licences L-1..L-3, cell law (HELD/STALE/UNHELD/CONTRADICTED) and causation worksheet bind round two. Relevant to what a player in a sitting may be shown about the chamber.

- **PR-001** `INTENT` (+D) — A proceeding is an occasion at which persons address persons who may dispose of a matter; games differ by relation of parties, bench, floor plus one declared key (who may dispose). \[README Status: RATIFIED AS INTENT (v9), ED-SC-0039; nothing exists in engine/season until SC-01 built; 21 supersedes parts of 00-20\] `proposals/2026-09-05-proceedings-subsystem/README.md:12` · hook: speak/determine/convene/release verbs; Query.judging_set · conf H
  - Ownership ED-SC-0033; Phase 2-4 = SC-01/SC-02. Cost claim: zero new carriers, zero edge kinds, zero new verb names, zero fields; speak and determine gain a body, convene corrected, release landed, six investigation acts split into five rows; three Queries (judging_set, latitude, standing).

- **PR-002** `INTENT` (+D,E) — Three derived sets define any proceeding: parties (persons with commit edges to a disposition), bench (holders of seats whose remit covers the matter at the venue, a Query), floor (persons present). \[00 PROPOSED; ratified as intent via README/ED-SC-0039\] `proposals/2026-09-05-proceedings-subsystem/00_DERIVATION.md:45` · hook: Query.judging_set; commit edges; presence cache · conf H
  - All three already exist as data: commit edges, hold Tenures, presence cache. Bench is Query.judging_set, ownerless. Games differ by bench-parties intersection (empty, equals questioner, superset of parties), bench size (0, 1, >1, >>1) and whether the subject is on the floor.

- **PR-003** `INTENT` (+D,E) — The three sets alone cannot separate negotiation from public debate (both empty bench); a declared 'disposal' key (mutual / none / bench) does, since it asks whether the room can settle anything. \[00 PROPOSED, ratified as intent; 09_IMPOSSIBILITIES row 13 grades closure CONVENTION + scan not STRUCTURAL\] `proposals/2026-09-05-proceedings-subsystem/00_DERIVATION.md:53` · hook: arrangement key disposal · conf H
  - Draft claimed sets sufficient and was wrong; recorded not erased. Eleven of twelve games separated by relations over existing data, one declared key does the rest. No ProceedingKind enum; adding a thirteenth game adds a row. Subject-absent case (excommunication) is the 'subject did not travel' relation.

- **PR-008** `INTENT` (+L) — A proceeding never advances itself: no phase timer, no turn counter. Every step is somebody's act; the opening act (open_case) declares stages and terms (T-n), so a summons has a return day. \[00 PROPOSED; Tenure.term unbuilt (P-04); 21 C-10 says Tenure.term is architecture doc's own field, Record.ttl for document clocks\] `proposals/2026-09-05-proceedings-subsystem/00_DERIVATION.md:213` · hook: open_case; Tenure.term; Record.ttl; term.matured · conf H
  - A proceeding nobody advances lapses; 'a hearing nobody attended' is a legitimate outcome. Clocks can be bribed, delayed, burned. Tenure has no term field (shape.py:2066-2091). 21 C-10: two clocks - document life on Record.ttl/stages, edge life (term of service, oblige deadline) on Tenure.term.

- **PR-019** `INTENT` (+A) — No clerk verb or role field: the clerk is whoever holds the case Record, conferred by carry. open_case.writes gains DocketItem.matter; a docket reader branch lets exists:DocketItem evaluate; bench-less games route via petition -> carry. \[21 C-5 ruled; docketing is PHASE 2 step 10\] `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md:264` · hook: open_case; DocketItem.matter; petition; carry; WorldReader · conf M
  - Per 21 B.4 exists:DocketItem currently returns UNKNOWN (WorldReader looks for 'docketitems' collection, docket is a sequence) so the design's speak cannot form against the live reader; fix is a reader branch. Docketing was in none of 12_BUILD_ORDER's twelve steps.

- **PR-023** `INTENT` (+L) — convene's settlement-scale becomes an ordinal floor above the person tier via a new 'rank' stem in REQUIRES_STEMS replacing the scale: key; a convening at a person-rung is refused. \[21 C-11 and PHASE 2 step 9\] `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md:379` · hook: convene; rank stem; seam.contest place · conf M
  - scale: is live at verb_table.yaml:138; Jordan's 2026-09-05 correction supersedes it. Cost stated: one stem added to a closed set. Also C-8: venue is already seam.contest's place parameter; tracer derives rung wrongly (reads payload) and should read Scene.place.

- **PR-024** `INTENT` (+L) — The arrangement row a designer writes: disposal, bench_basis, floor, records_dissent, venue_min_rank, term_required, appeal_basis, interposed, order, registers, proofs, disposes, disposal_reach, verdict_reasons, stakes_grade (15 keys, 13 after 21). \[03 PROPOSED (held back); ratified as intent via README; 21 PHASE 2 step 6 takes key count 15 -> 13 (drops registers, stakes_grade, order's hardest value)\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:443` · hook: arrangement keys; data/arrangements.yaml (not yet built per README) · conf H
  - Closed set in data (arrangements.yaml, ID-12); nothing branches on a value; read as ordinal, set membership or relation. Derived Queries NOT keys: latitude (from interposed), genre (a set, from bench remit), ladder, bench, parties, floor membership, eloquence-vs-consequence. Three flagged weak keys: registers (P-07), order (P-08), stakes_grade (P-09, most likely deleted).

- **PR-025** `INTENT` (+M) — Latitude is derived, not a scalar: a Query over interposed[] (person, office, document, procedure, ceremony, pair). Designer says what stands between person and exchange; how much the person matters falls out. \[03 PROPOSED; ratified as intent; latitude = Query (one of three Queries in README)\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:59` · hook: Query.latitude; interposed key · conf H
  - A stored scalar would be two homes for one fact and a stored aggregate (T-a). Interposition buys protection but raises price obtained, impasse and lowers joint gain; magnitudes are assumption-grade (P-11). The 'obstacle' later takes a latitude floor (~0.7 per 21).

- **PR-032** `INTENT` (+M) — A role is a relation of one person to one occasion, not a field: party = live commit; adjudicator = seat holder acting via it; audience = present with no commit or seat; advocate = commit to another's disposition plus oblige; witness = one who tells; subject; clerk = holder of case Record. \[03 C.2; Jordan 'characters will be enacting the system as participants, audience, adjudicators'; ratified as intent\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:392` · hook: commit/oblige edges; Act.via; carry · conf H
  - Party/advocate/audience differ only by which commit edges held; no role enum. Advocate absorbing defeat costs zero lines since consequences attach to the actor. Nothing represents a court, verdict, vote, transcript or order of proceedings; the ordered fold is the order.

- **PR-046** `INTENT` (+L) — Thirteenth game 'examination' (sealed paper, fixed form, scripted, disposal bench, tenure conferred, verdicts withheld) authored with no code change; strains only at proofs, needing a 'performance' roster member (data edit, P-13). \[03 F.1 thirteenth game authored as proof; ratified as intent (P-13 open)\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:744` · hook: arrangement row examination; proofs roster · conf H
  - Candidate is subject and sole party; no adversary so no ladder descent; document interposition lowers latitude (anonymised exam). Reveals proofs is a forensic-shaped key. Closure claim test: test_no_branch_on_arrangement.py - a scan; status HYPOTHESIS until run.

- **PR-053** `INTENT` (+K) — Stratum order [movement, binding_decision, contested_physical, uncontested_material, social] resolves determine before speak in a season, so hearing and judgment cannot share a season: convene n, press n+1, determine n+2. The gap is a season in which people can flee, bribe, produce documents or die. \[04 B.2; precedent not chosen here; P-14 asks Jordan to check intent; rosters.yaml:129 stratum order\] `proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:409` · hook: stratum roster order; determine.unheard · conf H
  - Recorded as falling out of a stratum order set for other reasons; if one-tick trials are wanted the stratum roster is the row to argue about. A bench determining an unpressed matter is refused (determine.unheard).

- **PR-057** `INTENT` (+L) — Permutation test: speaking order, ladder rung order and evidence-before-argument are PROCEDURES (permuting changes outcome); witness deposit, attendance, bench determinations, interposition set are MAPS (permuting must not move the content hash). \[05 Status PROPOSED (held back) then README ratifies directory as intent; 21 C-2 corrects the rung fold\] `proposals/2026-09-05-proceedings-subsystem/05_PROCEDURE.md:14` · hook: arrangement.order; seam.proceed; content hash · conf H
  - Order is a parameter (arrangement.order). Register effects are taken as property of position in the sequence (faults of sequence: opening too elaborately, joke after concession, saying it twice); not permutation-tested, P-16. Nested run: seam.proceed(proj, venue, matter, arrangement, attendees, depth, max_depth) -> Margin, never a winner.

- **PR-058** `INTENT` (+I) — A proceeding ends by: nobody acting (all attendees form no candidate), the declared term maturing (T-n), the depth cap (typed Refusal), or the matter reaching the foot of the ladder. No turn limit or round cap - the bound is attendees' willingness to keep spending. \[05 B.1; ratified as intent; Tenure.term unbuilt (P-04)\] `proposals/2026-09-05-proceedings-subsystem/05_PROCEDURE.md:58` · hook: term.matured; depth cap; open_case terms · conf H
  - A round cap would be a clock nobody wound (AX-5) making hearing length a property of the engine not the people. Mutual commit ends a negotiation (21 C-12, F-07 omission). The engine never decides the debate is over.


### B / PROPOSED

- **CD-096** `PROPOSED` (+D) — A motion is an OUGHT Proposition about a person (the party); members commit to it; determine on a declared row mints a resolution; the owning seat acts only on a held resolution. \[PROPOSED (2026-10-29), design only, CR-38's design file; HELD BACK from the merge default: its section 12 calls; sec 1\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:33` · hook: utter; commit; determine; resolution Record · conf H
  - No party-less determine: cede territory is about its holder, fill seat about the nominee, deposition about the monarch. A pure policy question with no person is not carried. If the owner declines, the resolution stays held, citable and unexecuted.

- **CD-097** `PROPOSED` (+D,F) — One council seat per rung; members are persons with a live oblige to it; joining is the joiner's own act; the chair (Speaker) is a seat separate from the ruler. \[PROPOSED (2026-10-29), design only, CR-38's design file; HELD BACK from the merge default: its section 12 calls; sec 4\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:88` · hook: oblige; establishment_of; judging_set; Speaker seat · conf H
  - Rejected: grant determine to duchy seats (sits_over walks UP so a realm venue never lists a duke), a new bench_basis 'assembly' (contradicts Layer 1), a seat per member (hold is one per object). A duke is eligible by containment but is a member only if he joins.

- **CD-099** `PROPOSED` (+D) — A sitting in nine steps: summons, salience, tabling, attendance, speeches, division (commit), declaration (determine), execution by the owner, lapse. \[PROPOSED (2026-10-29), design only, CR-38's design file; HELD BACK from the merge default: its section 12 calls; sec 2\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:39` · hook: convene; open_case; commit; determine; MATTER lapse (new) · conf H
  - Season-granular, not round-granular: no round is stamped on any Event or Tenure. Only commits made in a season AFTER tabling count (Tenure.since > tabling season). Commits never close on their own; a changed mind needs repudiate/release.

- **CD-102** `PROPOSED` (+A) — Attendance is unmodelled: argue needs co-presence and nothing brings a duke to the venue; options are a costed move or a summons writ delivered by give. \[PROPOSED (2026-10-29), design only, CR-38's design file; HELD BACK from the merge default: its section 12 calls; sec 5 attendance\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:122` · hook: move; writs_held; comply; give; date.fired · conf M
  - Unverified whether anyone not at the realm rung hears a realm-venue date.fired first-hand; if none do, sittings_before asks nobody and the summons has no addressee. First measurement (PD-1). Computed give does not form (H-229).

- **CD-107** `PROPOSED` (+H) — Four rungs of parliament: realm (King/Queen convenes; Dukes may join), duchy (Duke; Counts), province (Count; Lords), territory (Lord; Mayors). Province rung does not exist in the authored realm. \[PROPOSED (2026-10-29), design only, CR-38's design file; HELD BACK from the merge default: its section 12 calls; sec 9\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:174` · hook: rung_kinds; provinces_of; venue_min_rank · conf H
  - Canon fixes the ladder; marquis appears nowhere (Jordan's call 1). venue_min_rank and disposal_reach have no readers, so lowering the floor changes nothing and a sub-realm resolution has no machinery to reach anywhere until the reach channel is built.

- **CD-108** `PROPOSED` (+D) — Thirteen blockers with owners: non-person matter refused, Record disposal declined, computed acts name no arrangement (H-80), dateless carry, rank of sitting question, no lapse, argue ignores motion, no addressee, no computed give. \[PROPOSED (2026-10-29), design only, CR-38's design file; HELD BACK from the merge default: its section 12 calls; sec 10 blockers B-1..B-13\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:189` · hook: determine; open_case; carry; give; H-80 · conf H
  - The honest size of the work is the list, not 'a few readers'. Hash: a new questions_for stamp and a new give conjunct are declared MOVERS. No tree-wide guard licensed; the loader's refusal per data family and the falsifiers are.

- **CL-097** `PROPOSED` (+D,C,L) — Borrowing ledger for the parliament design: TAKEN: convening and framing as office powers (ius agendi, relatio), senatus auctoritas as held unexecuted resolution, Lawspeaker-shaped Speaker seat separate from the Crown; DECLARED INERT: order by rank; REFUSED: sortition, log-rolling, scaled compromise, disputatio and the Nyaya named defeats. \[PROPOSED 2026-10-29, design only; §12 calls held back\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:155` · hook: argue; Speaker/council seat; off_king; parliamentary_debate arrangement · conf H
  - Stasis kept for forensic (HOLDS) motions only; BATNA/first-offer anchoring 'logged, not modelled'; first-defector snowball absent in code (every argue Candidate ties, Gumbel draw). Speaker declares, ruler convenes and executes (off_king), after Lawspeaker 'bounded away from outcomes'.

- **OP-041** `PROPOSED` (+L) — No act or operand names which arrangement governs a matter: computed open_case writes DOCKET_ARRANGEMENT None, so every computed case is heard as the default oblige and determine hard-codes oblige. \[PROPOSED evidence register (gap SC-G01/G02); reference not canon\] `proposals/2026-10-16-verbs/2026-10-16-verbs-21-gap-register-sc-and-gv.md:34` · hook: open_case; DOCKET_ARRANGEMENT; arrangements.yaml · conf H
  - Docket item is {date: None, matter}; names neither arrangement nor originating petition. Precedent cited: the venue is the engine (framing authority, speaking order, decision rule). Proposed fix: derive arrangement from the seat and matter (a killing -> legal trial; heresy -> tribunal).

- **OP-054** `PROPOSED` (+A,G) — As built: a matter reaches a docket two ways (petition then carry for the seatless; open_case from a seat granted determine) and leaves by one (determine). \[PROPOSED description tutorial, grades per seed by ctl/ runs; reference not canon\] `proposals/2026-10-22-system-description/2026-10-22-system-description-06-t05-social-contest.md:246` · hook: petition, carry, open_case, convene, speak, determine; judging_set · conf H
  - A sitting is a convene Date with a holder that forms a standing slot; speak writes nothing; the bench is judging_set.

- **OP-071** `PROPOSED` (+F,I) — One mechanic, a venue is a parameter row (container, prize, standing_date, judging_set_rule, decision_rule, admission_floor, privileged_custody, exchange_budget, article_count, coupling_depth, veto_holders, record_custody); Hafenmark Parliament, Doctrinal Dicastery, guild Masterpiece Examination, settlement court. \[PROPOSED\] `proposals/2026-08-29-valoria-from-scratch/08_argument.md:492` · hook: venues.yaml (cf. engine/season/venues.yaml) · conf H
  - Restoration consensus cell. Parliament: seat-holders, majority, floor G2, Duchess veto yields CARRIED-WITHOUT-FORCE. Dicastery: Cardinal determines, floor G3, Confessor veto. Guild exam: G4 on the work but G0 on fitness, which reproduces caste via institution. Restoration cell: no sustained objection, custody none, one member can block.

- **OP-074** `PROPOSED` — A venue adds a door to doc 08's tuple: (convener, enter, speak, admissible_source, attendance_cost) as boolean predicates over marks, office, standing and commitment degree. \[PROPOSED from-scratch design; nothing ratifies\] `proposals/2026-08-29-valoria-from-scratch/14_office_and_upper_rungs.md:396` · hook: venues.yaml (cf. engine/season/venues.yaml) · conf H
  - A door is a predicate and a verdict is a weighting. Venue table: Hafenmark Parliament (Duchess convenes; seat-holders enter and speak; majority; quarterly plus extraordinary on a Crown vacancy), Goldenfurt court (anyone enters; those carrying a petition may speak; praefect determines), three Church dicasteries with own registers.

- **OP-077** `PROPOSED` (+H) — The King cannot enter the Hafenmark Court Parliament (ENTER = seat-holders and attendants; Crown holds no seat). \[PROPOSED\] `proposals/2026-08-30-play-space-coverage/02_seasons_crown.md:140` · hook: venue ENTER predicate; dispatch; petition respondent · conf H
  - So to press a Crown claim he must dispatch an envoy to a dicastery; and 'you cannot address a petition to a Dicastery', only to a person holding an office, who can drop it.

- **OP-104** `PROPOSED` (+D,H) — Court Parliament's bench: design a derivation (not authored seats) for who sits in the realm Parliament. \[DESIGN-FIRST position CR-38 (held on its own approval); paper\] `proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-19.md:103` · hook: parliamentary_debate; judging_set at realm venue; offices.yaml titles.domains · conf H
  - Default test is the holders of governance-ladder title seats whose rung is inside the venue, with three costed routes (grant determine to duchy-head seats; an arrangement-level bench reading, a 14th arrangements key; the interim realm bench of King and Widow Regent).

- **OP-110** `PROPOSED` (+E,I) — Escalation ladders as verb chains: speech tell -> argue (planned) -> petition/open_case -> determine -> seize; violence challenge -> fight -> march. \[PROPOSED invariant audit (verbs v2 part 6), probe counts from v1's four-season realm run\] `proposals/2026-10-16-verbs/2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md:180` · hook: verbs tell, argue, petition, open_case, determine, seize, covenant · conf M
  - War utter WAR -> march -> seize/raze -> covenant; the top rungs (seize, raze, covenant, argue) had not shipped. Four-season probe executions: challenge 14, fight 16, march 18, open_case 8, determine 3; speak executes 70 times but writes nothing and petition 28.


### B / ARCHIVED

- **GV-020** `ARCHIVED` (+H,J) — Hafenmark rank ladder is parliament-based: advancement above Standing 2 is by public vote and recorded on a Roll of Burghers; Standing 3 needs a 2/3 council vote. \[ARCHIVED-NOT-CANON; was CANONICAL PP-660\] `.designs/systems/factions/reference/faction_politics_v30.md:212` · hook: rank ladder; vote-gated promotion · conf H
  - Petitioner, Advocate, Burgher (oral examination, may second motions), Alderman (2/3 council vote for seat), Parliamentarian (must propose and carry a motion; must vote every session), Parliamentary Chair, Chancellor (Parliamentary confirmation vote), Prime Parliamentarian/Speaker-Regent (resolution of endorsement). Eight ranks Standing 0-7.

- **GV-021** `ARCHIVED` (+G,I) — Hafenmark demotion by parliamentary means: council no-confidence (2/3), Motion of Censure, coalition collapse, losing majority for 2 sessions. \[ARCHIVED-NOT-CANON\] `.designs/systems/factions/reference/faction_politics_v30.md:230` · hook: demotion triggers; no-confidence · conf H
  - Alderman loses seat by 2/3 no-confidence; Parliamentary Chair falls on losing majority 2 consecutive sessions or successful Censure; Chancellor on Censure (2/3) or Baralta withdrawing confidence (Disposition -2); Chancellor falls to 5 if Parliament fails to convene twice. Abstention costs Standing -1.

- **GV-022** `ARCHIVED` (+D,F) — Hafenmark Parliamentary Committees: six standing sub-bodies with jurisdiction, chair rank (Std 4+), cost, and Competence/Corruption tracks; funding is itself a parliamentary vote. \[ARCHIVED-NOT-CANON; PROPOSED committees\] `.designs/systems/factions/reference/faction_politics_v30.md:942` · hook: committee competence/corruption tracks · conf H
  - Supreme Judiciary, Trade & Guild Relations, Defense, Foreign Affairs, Constitutional Review (Almstedt permanent chair), Internal Affairs. Competence 0-3 and Corruption 0-3; unfunded committees decay. Std 2 players can influence policy via committee positions (auditor/secretary/clerk).

- **GV-023** `ARCHIVED` (+I,G) — Varfell Jarl Assembly councils: five standing councils chaired by Senior Jarls; each has a Readiness Track 0-3 that decays without sessions and gates delegation. \[ARCHIVED-NOT-CANON; PROPOSED\] `.designs/systems/factions/reference/faction_politics_v30.md:980` · hook: readiness track; delegation threshold · conf H
  - Council of the March, Highlands, Skald, Warden, Voices. Readiness 0: matter defaults to Vaynard's personal decision; Readiness 3: chair may act without Vaynard. No seasonal cost; convene on need, often at annual Assembly. Models confederate, distributed institutional capacity.

- **GV-024** `ARCHIVED` (+H,D) — Varfell ladder: advancement by provable deed; Jarl seat needs Jarl-vacancy or unanimity of regional Senior Lendmanner; Senior Jarl needs unanimous Assembly; Regent needs 3 of 5 senior Jarls. \[ARCHIVED-NOT-CANON\] `.designs/systems/factions/reference/faction_politics_v30.md:256` · hook: land-grant; assembly confirmation thresholds · conf H
  - Lendmann gets a ceremonial Land-Grant of one named settlement (revocable only by public assembly consent, politically costly). Jarl removal needs unanimity minus one. Assembly attendance once per year-arc mandatory. Assembly 'creates the legitimacy it affirms' (Varangian Guard analogy).

- **GV-025** `ARCHIVED` (+H,G) — Crown ladder: personal favour of the monarch plus inner-circle consensus; Std 6 needs unanimous inner circle (5 NPCs at Disposition >=0); Std 7 is succession designation or a 3-of-5 supermajority. \[ARCHIVED-NOT-CANON\] `.designs/systems/factions/reference/faction_politics_v30.md:155` · hook: inner-circle disposition vote; decree delegation · conf H
  - Contrast with Hafenmark: Almud's personal favour suffices, no assembly. Std 3 Banneret via Banner grant (recognition event, can be withheld). Regent-Designate may issue decrees in Almud's name if she is Unavailable, with Legitimacy Token damage, subject to later endorsement within 2 seasons.

- **GV-041** `ARCHIVED` (+F,H) — Seggio Council: hereditary corporate subnational faction at Seat/City settlements, each seggio holding one bespoke non-transferable privilege, sitting as one joint Eletti bloc that the governor must treat with collectively. \[ARCHIVED; PROPOSED ED-SE-0024 (consolidation: REFINE-THEN-RATIFY, Mandate-Challenge undefined)\] `.designs/systems/settlements/reference/settlement_layer_v30.md:675` · hook: seggio privilege; bloc treat · conf H
  - Privileges cannot be granted or revoked by the standard Domain Action or Quo Warranto; only inherited, married into, or seized by force. One seggio's Disposition swing ripples across the bloc vote. Naples Seggi/San Lorenzo grounding. Soft political removal path (Mandate-Challenge) still undefined per consolidation.

- **OP-001** `ARCHIVED` (+C) — Four adjudicator types (Expert judge, Crowd, No adjudicator, Panel) fix the contest's primary Argue attribute and are fixed for the contest's duration. \[ARCHIVED-NOT-CANON banner; file self-labelled CANONICAL 2026-04-17 (superseded by proceedings direction)\] `.designs/systems/social_contest/reference/social_contest_v30.md:36` · conf H
  - Expert judge=Cognition, Crowd=Charisma, none=Attunement, Panel=Cognition (Guild Arbitration rebound to Panel, ED-1059; per-member ballot weighted by standing, ED-1057). If circumstances shift adjudicator type (private negotiation goes public) the contest ends and a new one begins.

- **OP-016** `ARCHIVED` (+D,I) — Parliamentary Stay: a Senator motion (2+ factions on the suspension side) halts a Church Tribunal filing one season, available only while Church Influence CI<55. \[ARCHIVED; ED-631\] `.designs/systems/social_contest/reference/social_contest_v30.md:655` · conf H
  - Failure means Tribunal proceeds and the motion cannot be re-filed that season. The CI<55 gate creates a timing incentive: suppress Church before parliament loses ability to check ecclesiastical judiciary. Uses the BG Parliamentary Vote resolution.


### B / NOTCODED

- **CD-006** `NOTCODED` (+D,I) — A 'declared' disposal (a tally is the finding) is a loader value but no arrangement row uses it and no code reads quorum or counts members' commitments. \[loader accepts quorum only for disposal: declared; no row seeded\] `engine/season/data/arrangements.py:210` · hook: arrangement quorum; determine quorum conjunct · conf H
  - Disposal values bench/mutual/none/declared load, but no seeded row uses declared, mutual or none. determine's quorum conjunct is a bench-size fixture (bench_quorum=1), not a vote threshold. Vote-quorum (C-7) measured, not built, waiting on J-4 (H-161).

- **CD-007** `NOTCODED` — Who may attend (floor open/closed/admitted) and the minimum rung of venue (venue_min_rank) are declared per arrangement but nothing enforces them. \[keys floor, venue_min_rank loaded; no production reader (grep of engine/season, excluding tests)\] `engine/season/data/arrangements.py:223` · hook: arrangement floor/venue_min_rank · conf H
  - Only the key 'disposes' of ARRANGEMENTS is read outside the loader (effects_information.py:521, gate.py:257). A closed council and an open parliament admit the same people today.

- **CD-008** `NOTCODED` (+C) — Order of speech (free, rank, alternating, scripted, written_only) is a declared arrangement key but no code sequences speeches by it. \[key order loaded; no production reader\] `engine/season/data/arrangements.py:227` · hook: arrangement order; verb speak · conf H
  - There is no speaking order, no chair, no floor-holding. 'speak' is a single contested act per actor per season, not a turn in a sequence. The nested run that would sequence speeches is unbuilt (21_RECONCILIATION step 15).

- **CD-047** `NOTCODED` (+D,F) — No Parliament exists in the running world: no seat, no members, no speaker. The only parliamentary office is the Chief Parliamentary Clerk (NPC-008), remit [issue]. \[offices.yaml has no Parliament seat; only off_parliamentary_clerk (offices.yaml:312)\] `engine/season/offices.yaml:312` · hook: Office; offices.yaml; Court Parliament · conf H
  - H-90 records Jordan's ruling that the realm has a Parliament so the ruler has no monopoly of power, 'RULED AND NOT BUILT'. The Jarl Assembly appears only as the justification for 12 seats marked elected.

- **CD-110** `NOTCODED` (+C) — Debate between two characters is mechanically thin: a computed argue draws among known persons, rolling pool_default 2 vs obstacle_default 2 with zero leverage, and never reads the topic. \[proposal sec 5 (agent-read claims about argue roll, not re-opened); hole H-126 at hole_register.yaml:923\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:112` · hook: argue; pool_default; capability · conf M
  - Persons differ in nothing the roll reads (Person.capability has one writer that zeroes it; H-126), so outcomes vary by seed and fixture, not by person. Topic content (the Proposition) does not enter the roll or the pursuit shift.

- **GV-089** `NOTCODED` (+D,K) — CR-38 (design-first): Court Parliament has no bench of its own; at a realm venue the bench is the King's and the Widow Regent's seats (an interim two-seat bench); a design must say how a landed bench is derived (duchy-head determine grants vs an arrangement-level bench key). \[workplan v10 position CR-38, STATE DESIGN-FIRST; interim bench noted\] `workplans/valoria_master_workplan_v10_part4.md:408` · hook: judging_set; parliamentary_debate bench · conf H
  - Default tested: holders of governance-ladder title seats inside the venue (Landed + distinguished service aristocrats). Cost of each route stated: remit edit lets duchy heads judge trials too; a fourteenth arrangements key is refused by the loader. Parliamentary Stay and H-90 'there is a Parliament' wait on this. Unapproved: post-freeze mover.


### B / RESEARCH

- **CL-038** `RESEARCH` (+L) — The venue is the engine: each institution supplies (a) a framing authority, (b) a standing-indexed speaking order, (c) a decision rule, (d) often a clock. Institution is the deterministic wrapper; speeches are the stochastic core. \[RESEARCH synthesis\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:294` · conf M
  - Doc ties this to the old CR1 'wrapper = praetor/magister' shape. Examples: relatio, Lawspeaker, discessio, klepsydra.

- **CL-089** `RESEARCH` (+C,I) — Eloquence requires many people who must be persuaded; consequence requires few who can constrain. Republic maximises the first, sultanate the second; literature migrated from rhetoric to mirrors-for-princes as the ratio moved (Tacitus; Jones & Olken 2005). \[proceedings study finding S2 (PROPOSED, HELD BACK)\] `proposals/2026-09-05-proceedings-subsystem/source/02-part-I-throughlines.md:55` · conf M
  - Every interposition device (advocate, envoy, paired missi, censor, Ottoman written summary, silent sovereign) is discretion-reducing. Same idea as research-doc 'regime decides load-bearing genre' (CL-014) from the person-side.

- **HP-055** `RESEARCH` (+J) — P13 Speaking Order: order derives from precedence; chair may call out of turn to honour or slight; members may speak or merely assent, at no cost. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:367` · hook: arrangement order: rank · conf M
  - Early speakers set terms, late ones assent or dissent. From album senatorum ordering. Fails if every member gets an equal turn, then order is noise.

- **HP-061** `RESEARCH` (+D) — P19 Competence and Quorum: each body's remit and presence threshold, with overlapping competences allowed; use Aristotle's division as description language then violate it. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:404` · hook: arrangement quorum · conf M
  - Cites Politics IV 1298a (T0) and Venice where the Ten sat as court, its members voted in the Senate and the doge was part of it, so the tripartite sort fails.

- **HP-070** `RESEARCH` (+F) — P37 Split Command: governorship divided between two officers with distinct competences who must both act and report separately. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:513` · conf M
  - Venetian rettori (podesta civil, capitano military) over whom provveditori and the Avogaria could review; also lay-plus-clerical missi pairs. Neither can defect alone.

- **HP-075** `RESEARCH` (+A) — Parliament component: only holders of agenda right convene; amendments create live motions; roll in precedence; chair selects motion order; veto window yields a Record; carried measures enter an enactment clock. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:608` · hook: convene/carry/speak (verbs exist, per SC evaluation mostly unbuilt) · conf M
  - Thesis: procedure is where power is exercised and the vote is a formality. Sessions must be scarce containers; shared-loss failure condition is not optional; model the drafting layer so a clerk with no vote matters.

- **PR-013** `RESEARCH` (+M) — Discretion gate: the person matters most where the arrangement constrains him least. Low latitude (scripted audience, written channel) leaves only capacities 1-2; high latitude (autocrat, envoy alone) leaves all nine and the entry step. \[01 PROPOSED; study Fig. 4 'the diagram this study turns on'\] `proposals/2026-09-05-proceedings-subsystem/01_THE_STUDY.md:129` · hook: latitude Query; arrangement row · conf H
  - Evidence: leader effects in autocracies not democracies (Jones & Olken ~1.5pp growth per SD); Crossland & Hambrick CEO effects; private firms 23.8% vs public 16.6% ROA variance. Transfer to tribunals/embassies is inference. So ten proceeding kinds are ten values of the arrangement.


### B / CLASSICAL

- **CL-024** `CLASSICAL` (+C,M) — Caraka debate triage: before debating assess type (friendly sandhaya vs hostile vigrhya), opponent's standing (superior/equal/inferior), and the assembly (parisad: learned vs ignorant, friendly/indifferent/hostile); strategy is conditioned on that triage. \[RESEARCH; Caraka-samhita Vimanasthana 8\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:212` · conf H
  - Against a weaker opponent before a hostile ignorant crowd jalpa devices are legitimate; against an equal before a learned assembly honest vada is owed. Oldest systematic debate manual in India; audience-conditioning model.


### B / HISTORICAL

- **CL-018** `HISTORICAL` (+C) — Chancery insha': a rank-indexed protocol table for petitioning power. Register, formula and deference level are a function of petitioner standing relative to addressee (al-Qalqashandi, Subh al-a'sha, 14 vols). \[RESEARCH; Qalqashandi 1412 web-verified (line 47)\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:158` · conf H
  - Also Abd al-Hamid al-Katib's Risala, al-Suli Adab al-Kuttab, Ibn Mammati. 'More than fifty insha' manuals' over five centuries. Doc calls it the best template for a petition-to-sovereign subsystem (a self-gating-by-standing mechanic).

- **CL-030** `HISTORICAL` (+C) — Concione / ars arengandi: public harangue before the 13th-c. commune assembly, grown out of the ars dictaminis (letter to speech, 'speak as you write'), tied to an ideology of the bene comune; occasion-typed model speeches (Matteo dei Libri). \[RESEARCH; ars arengandi flagged CONFIDENCE medium (line 257); Artifoni offprints\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:512` · conf M
  - One compositional engine could drive a written appeal and a spoken address. Bene comune gives civic deliberation a venue-specific ethos resource, distinct from the Crown-encomium register. Brunetto Latini's vernacular Cicero (La Rettorica) was the bridge (line 265).

- **CL-032** `HISTORICAL` (+D) — Roman Senate: presiding magistrate frames the question (relatio); opinions (sententiae) delivered in strict rank order, lower ranks often never reached; decision by discessio (physical division). \[RESEARCH\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:279` · conf H
  - Persuasion bounded by a rigid speaking order that is itself a function of standing. Doc's 'wrapper = deterministic accounting around a small stochastic surface' (line 294).

- **CL-033** `HISTORICAL` (+D) — Lawspeaker (lögsögumaðr): only paid official, elected by the Lögrétta for three years; recites a third of the law yearly and the standing orders (þingsköp) every year; authority procedural and session-bound, formally powerless between assemblies. \[RESEARCH; Grágás via wikisource, Icelandic theses; conf high\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:516` · conf M
  - A chair/reciter, not ruler or judge; may consult law-wise men before pronouncing. Law-as-recited-memory is a pre-literate mechanic. Earlier line 281 mentions vapnatak (weapon-clash assent). Doc suggests a Speaker role-actor.

- **CL-035** `HISTORICAL` (+D,G) — Modus Tenendi Parliamentum (England c. 1294-1327): 26 chapters idealising parliamentary procedure, orders summoned, precedence, ch. 17 on hard cases; read as Parliament being neutral ground for accord between warring factions. \[RESEARCH; date/purpose CONFIDENCE medium (line 62)\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:282` · conf M
  - The assembly as a contested arena that itself constrains the contest. Date (Edward I vs II) and genre (manifesto/treatise/reform programme) unsettled. Also Thomas Smith, De Republica Anglorum (1562-65), line 283; witenagemot consultative council, line 280.

- **CL-036** `HISTORICAL` (+C,D) — Athenian dikasteria: hundreds-strong lay juries, speeches timed by water-clock (klepsydra), no professional judges or lawyers, hence logographers. Persuasion under a hard clock before a large swayable lay audience. \[RESEARCH\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:287` · conf H
  - Roman quaestiones perpetuae are the standing jury courts, applied home of stasis (line 288).

- **CL-037** `HISTORICAL` (+C,J) — Romano-canonical ordo iudiciarius: libellus (written complaint), litis contestatio (joinder of issue), graded hierarchy of proof (two witnesses = full proof; confession queen of proofs), positiones/articuli to be proved. \[RESEARCH; Tancred ordo c. 1216\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:289` · conf H
  - Doc calls it the structural ancestor of an Evidence-clock system and suggests the proof hierarchy as a possible Evidence-weighting refinement (line 351). Bernard Gui's inquisitorial manual (1323-24) gives interrogation categories, line 290.

- **HP-008** `HISTORICAL` (+J) — Placitum generale: annual spring assembly of magnates; attendance and precedence were themselves a standing signal, exclusion a demotion. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:162` · hook: DELIBERATIVE_ASSEMBLY (proposed) · conf M
  - Marchfield moved to Mayfield for fodder. Compiegne/Soissons 833 staged Louis the Pious's deposition. Repo hook: exclusion triggers an L/PS cascade; holdout can escalate an assembly into a deposition proceeding.

- **HP-011** `HISTORICAL` (+D) — Reichstag as three colleges (Electors, Princes, Imperial Cities) voting separately; binding recess needs all three; cities only won a full vote at Frankfurt 1489. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:199` · hook: governance_mode NEGOTIATED_ESTATES (proposed) · conf H
  - Hoftag evolved into tri-curial body; princes' college voted in curiate blocs by 1653/54. Repo hook: NEGOTIATED_ESTATES with sequential veto and representation-lag (taxed long before seated) kept as texture.

- **HP-014** `HISTORICAL` (+D) — Florentine Signoria: eight Priori plus the Gonfaloniere, two-month terms, sequestered in the Palazzo; Dodici Buonuomini and Sedici Gonfalonieri as advisory colleges; Consulte e Pratiche canvassed elites. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:257` · hook: none (proposed) · conf H
  - Corrected: nine Signori not ten. Guild-delegate seats with forced rotation prevent permanent faction ownership; Pratiche are a non-binding sounding board before major decisions.

- **HP-030** `HISTORICAL` (+G) — 1172 reform after Vitale II's lynching: Great Council as indirect electoral body, doge always flanked by six Ducal Councillors (one per sestiere) whose co-signature was required. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:320` · hook: Monarch bypass leash (proposed) · conf M
  - Repo hook: a leashed monarch configuration needing a companion co-signature before a directive resolves, adopted by charter.

- **HP-031** `HISTORICAL` (+D) — Han tingyi: court conferences where Excellencies, Ministers and invited specialists debated a question and recorded opinions; emperor then ruled, never procedurally bound. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:377` · hook: DELIBERATIVE_ASSEMBLY inside AUTOCRATIC_FIAT (proposed) · conf M
  - Consultative autocracy. Repo hook: a genuine deliberative sub-procedure nested inside a pure-fiat crown tier, flagged separately from the tier that ratifies. Majority opinion usually adopted.

- **HP-051** `HISTORICAL` (+J) — Seating, precedence and audience are negotiated before speech (Liudprand 949/968, De ceremoniis, Callieres 1716): ceremony absorbs contests over standing, not substance. \[FILED 2026-10-16 critical evaluation; reference\] `research/by_lane/SC_social_contest.md:59` · hook: interposition_kinds ceremony · conf M
  - Maps to convene with venue rank above person rank and an interposition kind `ceremony`; attend or not attend as the lever. The absorb/cannot-absorb table is the vendored study's synthesis.

- **HP-052** `HISTORICAL` (+A) — Three settlements of the counsel problem: Hincmar's secret palace council (882), Japanese council 1225 with Shikimoku 1232 (consensus without recorded division), Ottoman telhis (written summary to a silent sovereign). \[FILED 2026-10-16 critical evaluation; reference\] `research/by_lane/SC_social_contest.md:60` · hook: records_dissent / order: written_only · conf M
  - Maps to records_dissent and order: written_only and the council_of_state row. The study marks Hincmar possibly advocacy and 'consensus suppresses dissent' only Medium confidence.

- **HP-053** `HISTORICAL` (+I,J) — Roman Senate procedure: relatio (magistrate frames), sententiae asked by rank, discessio, intercessio, filibuster by clock (diem dicendo consumere), senatus auctoritas. \[FILED 2026-10-16 critical evaluation; reference\] `research/by_lane/SC_social_contest.md:54` · hook: order: rank · conf M
  - Speaking order is a function of standing; veto nullifies but leaves a citable record. Maps to arrangement `order: rank`, SC-SRC P2 and P12-P17. Tiered T1/T2 in SC-SRC; the evaluation calls the pattern sound.

- **HP-105** `HISTORICAL` (+D,G) — Icelandic Althing (930): the Lawspeaker recited law from memory and chaired the Logretta; assent could be shown by weapon-clashing (vapnatak). Also the Modus Tenendi Parliamentum (c.1294-1327) as an idealised procedure. \[RESEARCH 2026-06-02 (rhetoric corpus); confidence tagged, no independent verifier\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:281` · hook: Speaker/chair role (proposed) · conf M
  - Lawspeaker was the only paid official, elected by the Logretta for three-year terms (line 516). Modus Tenendi frames parliament as neutral ground for accord between warring factions. De Republica Anglorum (1562-65) described procedure for foreigners.

- **PR-087** `HISTORICAL` (+J) — Institutions the study documents: Athenian juries 201-1501, no judge/appeal, secret ballot without deliberation, water clock, graphe paranomon on proposers; Roman patron-client and rank-ordered senatorial opinion; Byzantine ceremony as statement, precedent file, Liudprand 949/968; Carolingian two-tier assembly, Alcuin's admonition method, paired missi; Ottoman silent sovereign, vizier, telhis; Chinese Odes recitation, remonstrance offices. \[source Part V dossiers, as the study reports them (T2); not independently verified\] `proposals/2026-09-05-proceedings-subsystem/source/06-part-V-dossiers.md:7` · hook: none (historical reference for rosters/arrangements) · conf H
  - Nine dossiers each with fault catalogue and principal contribution. Worked example: Demosthenes on the crown 330 BC (defends policy as it appeared, not outcome; Aeschines fined and left Athens). Circle of justice (Fig 18) lets counsellor frame oppression as a revenue observation; fails when the hearer decodes. Strasbourg 842: oaths sworn in the other's vernacular.



## D · Judgment and voting — 76 entries (CODED 12, RATIFIED 6, INTENT 9, PROPOSED 6, ARCHIVED 11, NOTCODED 5, RESEARCH 8, HISTORICAL 14, GAME 5)


### D / CODED

- **CD-003** `CODED` (+G) — arbitration row: one decider chosen by the parties, no appeal, proofs [record, testimony, oath], disposes oblige, reach room. \[row in arrangements.yaml:106; the only seeded row whose disposal determine can open (oblige)\] `engine/season/arrangements.yaml:106` · hook: arrangement arbitration; determine; oblige · conf H
  - A bench of one: records_dissent false is the loader author's reading, not a transcription. oblige is also the UNDECLARED_DISPOSAL, so a computed case with no named arrangement behaves as arbitration.

- **CD-014** `CODED` (+G) — determine: a seated judge, acting through a judging seat, disposes of a docketed person-matter: party, docket, bench and quorum conjuncts, then a contest 'a proposition' decides whether and how hard. \[verb row determine, verb_table.yaml:352; effect _eff_determine effects_information.py:419\] `engine/season/verb_table.yaml:352` · hook: verb determine; prize a proposition; Tenure oblige/detain/ban · conf H
  - Success bands open a disposal Tenure (oblige, detain or ban) owned by the party on the seat exercised, set the edge's degree, clear the docket matter, and move the judge's own pursuits. Failure writes nothing and leaves the matter docketed (matter.undetermined).

- **CD-015** `CODED` (+M) — Bench at a venue = live holders of a hold on an Office granting 'determine' whose scope_rung contains the venue; an empty bench lets the sitting lapse. \[code at world_q.py:474 judging_set\] `engine/season/queries/world_q.py:474` · hook: query judging_set; gate.BENCH_BASIS; sits_over · conf H
  - Containment walk via ancestry; reads the Tenure's granted_acts snapshot, not the office field. No per-arrangement bench: 'matter' argument is accepted but unused, basis fixed at BENCH_BASIS 'determine'.

- **CD-017** `CODED` (+B) — determine requires bench size at or above a quorum fixture; shipped value 1, swept 1/2/3. Quorum is bench SIZE (members able to sit), not a vote threshold. \[Fixtures bench_quorum=1 (H-161), read by WorldReader quorum stem\] `engine/season/data/fixtures.py:943` · hook: determine quorum conjunct; bench.size · conf H
  - At 1 the conjunct cannot refuse (the judge is himself a member). At 2 or 3 a lone judge is refused. Numbers are an assumption with no source document. The vote-threshold reading (live commitments to a disposition) is not built.

- **CD-042** `CODED` (+H) — How a seat is filled: appointed, elected, annex (Jordan, ED-IN-0256). The roster is read by Office validation and by confer's basis test. \[roster conferral_bases [appointed, elected, annex], rosters.yaml:2304\] `engine/season/rosters.yaml:2304` · hook: conferral_bases; confer; Office.conferral · conf H
  - Nothing discriminates: confer admits a seat with any basis. No election verb and no annexation verb exist, so 'elected' and 'annex' seats can be filled only by confer. 8 seats in offices.yaml carry elected.

- **CD-080** `CODED` (+B) — Win conditions as pluggable venue rules: ThresholdRace (first to T), TallyAtClose (higher advantage at close), ProofBar (challenger must clear a burden), GraceThreshold (petitioner must reach a bar), PersuasionTrack, VoteAtClose. \[kernel, NOT adopted (SC-05, ED-SC-0033); runs only in its own tests; resolver.py:54-130\] `systems/social_contest/sim/contest/resolver.py:54` · hook: none (kernel); WinCondition · conf H
  - Institutions differ only by which win condition and defeat catalogue the venue imposes; primitives are identical. Each returns a side label (a/b/draw), not a margin, which is why the seam cannot adopt it.

- **CD-081** `CODED` (+F) — Persuasion Track: a 0-10 axis from 5, pushed up by A and down by B, read at close in bands (>=9 A_total, >=7 A_decisive, 4-6 committee, <=3 B_decisive, <=1 B_total). \[kernel, NOT adopted (SC-05, ED-SC-0033); runs only in its own tests; PersuasionTrack resolver.py:81\] `systems/social_contest/sim/contest/resolver.py:81` · hook: none (kernel); PersuasionTrack · conf H
  - Gives the 'committee/compromise' outcome binary wins lack. Track = start + scale x (advA - advB), clamped. Used for succession (unified/decisive/split) and the BG parliamentary vote. Compromise referral is not in the live engine.

- **CD-082** `CODED` (+I) — VoteAtClose (prototype): running advantage is only momentum; the verdict is a separate terminal secret ballot, each juror voting A iff sharpness x gap + noise > 0; majority decides. \[kernel, NOT adopted (SC-05, ED-SC-0033); runs only in its own tests; VoteAtClose resolver.py:98\] `systems/social_contest/sim/contest/resolver.py:98` · hook: none (kernel); Panel; VoteAtClose · conf H
  - Close room near a coin flip, lopsided near certain; a juror can cross against momentum (Athenian dikasteria model). Aggregation simple_majority or weighted_by_standing (juror discipline as bench weight, ED-1057). Panel count default 7.

- **CD-083** `CODED` (+B,I) — Institution venues: court (logos, ProofBar), disputation (ThresholdRace), assembly (pathos-weighted, TallyAtClose, no device bar), appeal (ethos, GraceThreshold). Plus eight canonical proceedings with exchange counts. \[kernel, NOT adopted (SC-05, ED-SC-0033); runs only in its own tests; modes.py:66-81, 485\] `systems/social_contest/sim/contest/modes.py:66` · hook: none (kernel); PROCEEDINGS · conf H
  - PROCEEDINGS: formal_contest, grand_contest, royal_audience, church_tribunal (FACT stasis, track start 6), guild_arbitration (Panel), casual_dispute, private_negotiation, personal_appeal; also public_oration, secret_council (Venetian), imperial_petition, memorial_remonstrance venues. All numbers [SEED].

- **OP-050** `CODED` (+J,M) — A bench's regard for a speaker (`reception`, summed over each seated judge's own ledger of deeds) and proofs the opponent cannot mirror lower the obstacle of a contested matter. \[code at engine/season/queries/world_q.py:581 reception(), :641 proofs(), :474 judging_set(); fixtures.py:425 reception_gain=1.0, proof_step=0.25, obstacle_ceiling=2\] `engine/season/queries/world_q.py:581` · hook: world_q.reception/proofs/judging_set; SocialContestInput.reception, proofs · conf H
  - Ceiling 2 means a hostile room cannot raise a defaulted obstacle. room = reception_gain*reception + proof_step*proofs subtracted in roll.obstacle. hole_register H-215 measured one roll heard by a room in 2 seasons of seed 0. Open ED-SC-0040: reception reads other holders' ledgers inside the fold, against a ratified Layer-1 row (needs_jordan).

- **PR-095** `CODED` (+L) — Query.judging_set(w, venue, matter=None) is CODED: live holders of a hold Tenure GRANTED the bench's basis (Tenure.granted_acts) whose Office scope_rung contains the venue (containment walk); empty set means the date fires and lapses. matter not yet mapping to an arrangement's bench_basis (default 'determine'). \[code at world_q.py:474 (H-32 BUILT, plan position 18/PROC-A); matter param accepted but not load-bearing\] `engine/season/queries/world_q.py:474` · hook: world_q.judging_set; Tenure.granted_acts · conf H
  - Reads the grant not the office's remit_acts (13e consolidation; AST guard test). Probe: removing determine from the grant empties the bench (probes.py:1371-1389). 04's third parameter is accepted but unused until docketing maps matters to arrangements.

- **PR-097** `CODED` (+G) — determine is CODED: remit:determine, four typed conjuncts - party (subject is a Person), docket, bench (the same basis predicate the write gate asks), quorum (scalar_threshold bench.size/quorum) - and is a CONTESTED act (prize 'a proposition') rolled by the social_contest provider with the party as counterparty. \[code at verb_table.yaml:352 (plan position 19; v9 SC-03b); departs from 21 C-1/C-7 as to cardinality form\] `engine/season/verb_table.yaml:352` · hook: determine verb row; quorum; scalar_threshold · conf M
  - Quorum is implemented as a scalar_threshold over bench.size, not the cardinality-over-commitments conjunct 21 C-7 rules. Only a person can be the subject (only a person owns an oblige). arrangement disposal: declared carries the quorum. I did not open the writes block to confirm Tenure.since/degree keying.


### D / RATIFIED

- **CD-048** `RATIFIED` (+F,H,I) — Governing authority, sovereign power and holdings are three different things: a King governs but does not monopolise power because there is a Parliament; lesser ranks may delegate governance. \[hole H-90 grade ruled (Jordan 2026-09-02); sovereignty half not built\] `engine/season/hole_register.yaml:1116` · hook: titles ladder; Act.via; purview · conf H
  - Authority is rank plus containment, now read off the seat exercised (via), not the person. Sovereign power and its Parliament counterweight remain modelled by nothing; delegation is 'registered as open, not built'.

- **CD-049** `RATIFIED` (+F) — Multilateral tally accepted: a count over the bench's live determinations, evaluated by a LATER ACT; somebody declares and the declaration is the write. Votes, conclaves, majority verdicts come into range. \[ED-SC-0034 ruled (Jordan, 2026-09-06); last row for the id; design not coded\] `registers/editorial_ledger_sc_archive.jsonl:37` · hook: arrangement disposal declared; quorum; commit · conf H
  - Aggregates may exist as a Query (cannot be a field, can be computed); per-proceeding aggregates that die with the run are free; a debate score is free in-run. records_dissent was reinstated because under a declared disposal it is the tally made visible. Pool-only latitude, floored (~0.7).

- **CD-057** `RATIFIED` (+H) — Office.conferral's vocabulary is content; the architecture is settled: the basis names WHICH ACT fills the seat, and an election is determine, not confer. \[Layer 1 AX E.3 row (ratified)\] `architecture/meta/01_AXIOMS.md:1681` · hook: Office.conferral; determine; FILLED_BY (not built) · conf H
  - In code today conferral_bases are appointed/elected/annex but confer admits any; no determine route opens a hold (H-217). Planned: CR-35 election and succession arrangement rows, FILLED_BY map.

- **CD-060** `RATIFIED` (+F) — Planned: determine on a 'declared' row needs at least quorum bench members holding a LIVE commit to an OUGHT Proposition about the party naming the disposes kind: a vote is a count of live commits. \[plan position CR-34, B10-13, STATE BUILD; unbuilt\] `workplans/valoria_master_workplan_v10_part4.md:352` · hook: determine; arrangement disposal declared; commit; quorum · conf H
  - excommunication_deliberation becomes the first declared row (quorum 2, swept 1/2/3). parliamentary_debate NOT flipped: it disposes a Record, which _eff_determine declines. A loyal-creed commit is not a vote against its leader. Reach in realm play recorded as 0 (computed open_case names no arrangement).

- **CD-061** `RATIFIED` (+H,F) — Planned: an elected seat is filled by its faction's bench through determine, not confer; a contested succession goes to the throne's bench; the electorate is the faction's determine-granting seats. \[plan position CR-35, B10-17; unbuilt; closes H-217\] `workplans/valoria_master_workplan_v10_part4.md:365` · hook: determine opens hold; election/succession rows; FILLED_BY · conf H
  - New gate arm 'election': candidate must hold a live commit to the seat's faction Proposition; an inheritance seat drops the faction clause so any claimant may be judged. New arrangement rows election and succession (declared, quorum 1 swept). Cardinal electorate default confirmed (ED-IN-0301).

- **CD-062** `RATIFIED` (+B,H) — Planned: 'nominated' conferral. A bench nominates by determine under parliamentary_debate, minting a 'resolution' Record; the confirming seat confers only while holding it. \[plan position CR-36, B10-17; unbuilt\] `workplans/valoria_master_workplan_v10_part4.md:378` · hook: resolution Record; confer; determine Record disposal · conf H
  - Adds a Record-disposal site to _eff_determine and a record_kinds member resolution [terms,to]. Two-seat clause: nominating and confirming through one seat is refused. First nominated seat: Chief Parliamentary Clerk. Delivery to the confirmer needs a computed give (H-229) so the route is hand-built.


### D / INTENT

- **HP-108** `INTENT` (+G,L) — Vote as holders' own commits counted by a Query; charge as a HOLDS Proposition; testimony as a witness commit; contested determine (SC-03b) blocked. \[VCD ratified as intent (v9, ED-IN-0288) per the SC evaluation; every grade assumption or absent\] `research/by_lane/SC_social_contest.md:166` · hook: verbs commit, determine, covenant · conf M
  - Verbs arrest, interrogate, pardon, seize, argue, covenant proposed; the evaluation says SC-03a landed detain/ban and docket-names-arrangement, but the new SC verbs were absent from the 45-row table at that time (covenant and pardon are now rows).

- **PR-007** `INTENT` (+L) — The bench is Query.judging_set: seats whose remit covers the matter at that venue. Deleted alternative Rung.judging_set_rule was decision-shaped state on a container. \[00 PROPOSED; Query.judging_set registered as H-32 'absent', on critical path W26; raises 'NOTHING IS DECIDED AT A SITTING' (shape.py:3161-3163)\] `proposals/2026-09-05-proceedings-subsystem/00_DERIVATION.md:200` · hook: Query.judging_set; Seat/Office remit · conf H
  - First deliverable of the subsystem is that function (21 step 7): removing a seat's remit empties the bench; a purview walk one rung up still finds it. Two matters with disjoint remit coverage must not return the same seats.

- **PR-021** `INTENT` (+L) — Quorum: no declare verb, no stored tally; members commit (their own edges) and the declaring act is determine, whose precondition gains a cardinality conjunct over live commitments to the disposition. \[21 C-7 ruled; PART A.1 strikes review's 'no widening' clause; 19_PLAN step 15 stands\] `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md:307` · hook: determine requires; cardinality form; threshold in arrangement row · conf H
  - Widens precondition grammar by two entries (cardinality does not admit amount); counted as design change under ED-SC-0034. Falsifier: grep for count/tally/quorum_reached field returns nothing. Refused alternative: filtered-cardinality eighth form; trigger named if non-bench commits counting toward quorum reads wrong in play.

- **PR-035** `INTENT` (+E) — GAME arbitration: disposal bench, one decider named in the opening act's terms (T-n), closed floor, appeal_basis none, term required, disposes oblige, reach room, proofs record/testimony/oath. \[03 E.2 game row 2; ratified as intent\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:579` · hook: arrangement row arbitration; open_case terms · conf H
  - appeal_basis none is what makes it arbitration not trial. Who arbitrates is itself negotiable before the game starts - a game before the game.

- **PR-036** `INTENT` (+G) — GAME legal trial: bench disposal, open floor, records_dissent true, venue >= settlement, appeal via determine, interposed person+procedure, order rank, registers restricted, stakes terminal, reach settlement. \[03 E.2 game row 3; ratified as intent\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:590` · hook: arrangement row legal_trial; issue ladder; seam depth cap · conf H
  - Open floor makes every ladder descent witnessed by all, so conceding the fact to argue quality is costly. Advocate absorbs defeat not a discovered lie. Appeal opens the nesting; depth cap declared by the opening act.

- **PR-037** `INTENT` (+G) — GAME tribunal: standing commission, admitted floor, interposed office+procedure, appeal none, reach body. Office interposition makes members criticise as a duty (absorbs affront but is discounted); admitted floor makes concessions cheaper. \[03 E.2 game row 4; P-12 flags finality as a ratchet unless disposal is closable\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:605` · hook: arrangement row tribunal; office interposition · conf H
  - Differs from trial in three keys. Under AX-6 an appeal-less finding must be closable by some other act or the row is a ratchet (P-12).

- **PR-041** `INTENT` (+B) — GAME parliamentary debate: bench includes parties, open floor, records_dissent true, venue >= duchy, interposed procedure, rank order, all seven registers, proofs [] (deliberative: future admits no witnesses), disposes Record, reach realm. \[03 E.2 game row 8; ratified as intent\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:663` · hook: arrangement row parliamentary_debate; Record disposal; records_dissent · conf H
  - No issue ladder; amplification and weighing advantage replace forensic play. Many on bench plus low latitude: eloquence matters, consequence does not (Fig 14). Recorded dissent does its informational work and a loser is on record as having lost.

- **PR-042** `INTENT` (+I) — GAME council of state: parliament shape with closed floor, records_dissent false (consensus requirement), verdict_reasons withheld, reach realm: deliberation sealed, decree proclaimed. \[03 E.2 game row 9; ratified as intent\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:678` · hook: arrangement row council_of_state; records_dissent false · conf H
  - Fig 14 inversion: closed floor hides disagreement from outsiders while permitting it inside; consensus suppresses dissent more thoroughly than secrecy. Hidden-profile cost: what only one member knows stays unsaid and the body picks the inferior option with nobody mistaken.

- **PR-052** `INTENT` (+G) — determine: eligibility remit:determine; requires a DocketItem, a basis conjunct, and a quorum cardinality conjunct; seat in judging_set(venue, matter); writes degree-keyed Tenure.since+degree; emits matter.determined / matter.undetermined; refusals determine.refused, determine.unseated. \[04 B.2 as corrected 2026-09-07 + 21 C-1/C-7; live verb_table determine grade 'absent'\] `proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:306` · hook: determine verb row; Query.judging_set; Tenure.since/degree · conf H
  - judging_set live signature is (w, rung_id); design adds matter as third param, an extension. Draft errors: Tenure.until write, basis 'of: actor, on: via' (via not in operand roster; Act has no via, P-03), 'heard' relation with no producer (P-23).


### D / PROPOSED

- **GV-070** `PROPOSED` (+F,M) — SET-09 Parliament as a deterministic tally: votes = Mandate (+floor(CI/20) Church; opponents of a Church motion lose floor(CI/30)); each polity's side = sign(regard toward proposer minus regard toward holder); Diplomatic Alignment forces Church and Hafenmark together. \[PROPOSAL 2026-09-03, nothing ratified; built from an uploaded zip, not the working tree; parameters unvalidated\] `proposals/2026-09-03-governance-corpus-rebuild/annex-b-state-graphs.md:603` · hook: regard ledger; motion tally; side by regard · conf H
  - Regard is a directed -3..+3 ledger per ordered polity pair (unifies Standing tokens, treaty-violation Standing, Warden Accord). Majority gives plus or minus one point to the proposer's kernel check. Proposer and holder vote their own side. Motion kinds: transfer, censure, embargo, outlawry, no_confidence, nomination, stay.

- **OP-030** `PROPOSED` (+C) — Deliberation as an extension of the ratified VoteAtClose ballot: keep each member's first ballot, add influence rounds where majorities apply informational and normative pressure, minorities informational only. \[PROPOSED CIP-11, EVIDENCED\] `proposals/social_contest_consolidation_integration_v1.md:498` · hook: VoteAtClose; ContestView audience · conf H
  - Acceleration and a momentum lock. Weighted-by-standing threshold (ED-1057) stays as the count rule inside deliberation; today's VoteAtClose is a degenerate zero-round version. Blocker: audience exposed as two booleans and Panel averages member discipline. Falsifier: persuading one named juror changes the verdict and the player can say which.

- **OP-052** `PROPOSED` (+C,M) — The verdict hears the bench: determine contests `a matter` and the room gains an `opposed` term, the bench's signed regard for the OPPONENT. \[PROPOSED CP-T05-01 (v10 home)\] `proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-05-social-contest.md:85` · hook: determine contests; SocialContestInput.opposed; ROLL::obstacle · conf H
  - So a judge who saw the party's deed binds more readily. obstacle room = reception_gain*reception + proof_step*proofs - opposed_gain*opposed. Hearsay of a paired kind (killing, wound) names no doer, so only a judge who saw it moves the verdict; a witness must plead instead. Risk: character as evidence (a man of ill repute is bound more easily for anything).

- **OP-101** `PROPOSED` (+G) — A declared-disposal vote counts live commits: determine on a matter whose arrangement is disposal: declared requires `quorum` distinct bench members holding a live commit to an OUGHT about the party naming the row's disposes kind. \[BUILD instruction CR-34 (C-7, ED-SC-0034 grammar widening); paper\] `proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-13.md:115` · hook: determine; arrangements disposal declared; quorum; commit · conf H
  - excommunication_deliberation becomes the first declared row (quorum 2, swept 1-3). Closes the loyal-creed hazard (a commit to a creed naming the leader is not a vote against him). parliamentary_debate is not flipped: it disposes a Record, which determine declines.

- **OP-105** `PROPOSED` (+H,F) — Election and nomination as determinations: an `election` gate arm admits opening a seat hold when the faction's determine-granted seats tally via a declared disposal; CR-36 adds a `nominated` conferral basis and a resolution Record. \[BUILD instruction CR-35/CR-36 (B10-17); paper\] `proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-17.md:200` · hook: tenure_write_basis; FILLED_BY; arrangements election/succession rows; resolution Record · conf M
  - Elected seat: candidate must hold a live commit to the faction's Proposition. For inheritance the faction clause is dropped (Baralta's claim). The resolution is minted by Record-disposing parliamentary_debate and the confirmer must hold it before confer; delivery is a give, hand-built until H-229.

- **OP-106** `PROPOSED` (+B,G) — Parliamentary mechanics mapped to engine primitives: a vote's count is a Query over bench members' live commits to the motion (no stored tally, C-7). \[PROPOSED #453 verb coverage map (2026-10-03); rows marked none-yet/partly built\] `proposals/2026-10-03-verb-coverage-and-gap-fill.md:2424` · hook: commit count Query; quorum; arrangements disposes Record · conf H
  - Quorum is determine's conjunct plus the arrangements quorum key (partly built); veto and royal assent are arrangement keys (none yet for a single-member veto); Venetian election by lot is a seeded draw with no actor (none yet); term limits via Tenure.term.


### D / ARCHIVED

- **GV-005** `ARCHIVED` (+B,H) — Transfer roll is wrapped in a Parliamentary Vote contest; voting blocs, computed from faction Standing toward proposer and holder, shift the pool by plus or minus 1D. \[ARCHIVED-NOT-CANON; vote-bloc modifier PROVISIONAL (PARL-VOTE-MODIFIER-001)\] `.designs/systems/factions/reference/parliamentary_transfer_v30.md:92` · hook: parliamentary_vote contest -> pool modifier · conf H
  - Steps: declare target+mode+CB; vote contest opens, all parliamentary factions vote; blocs by Standing relative to proposer/holder; majority for proposer +1D, for holder -1D, split 0; then Pool-vs-Ob roll. Pass 2h interpretive, dice deltas not in original v12c spec.

- **GV-007** `ARCHIVED` (+F) — Parliament phase placement: motions declared as a Senator action in the Social phase (max 3 active), voted at Accounting Step 1.5 before Stability checks. \[ARCHIVED-NOT-CANON; was CANONICAL\] `.designs/systems/factions/reference/faction_layer_v30.md:442` · hook: motion declaration; accounting step · conf H
  - Any faction with Mandate >=2 may declare a Parliamentary Motion, consuming its action slot. Votes resolve at Phase 5 Accounting Step 1.5; effects applied, then Stability checks. Distinct from Hafenmark's individual Parliamentary Manoeuvre action.

- **GV-008** `ARCHIVED` — Parliament tally: each faction casts votes equal to its Mandate; target of a motion abstains; majority is >50% of participating Mandate, supermajority >=60%. \[ARCHIVED-NOT-CANON; was CANONICAL\] `.designs/systems/factions/reference/faction_layer_v30.md:446` · hook: deterministic tally by Mandate · conf H
  - Deterministic Mandate tally, no dice. Targeted faction does not vote on motions naming it as subject. Faction collapse removes its seat and lapses its active motions (s1.5 step 5). A weighted-vote design with stat as vote weight.

- **GV-009** `ARCHIVED` (+I,G) — Church Sacred Veto: once per four seasons, free action, blocks a listed motion type at a Mandate cost; self-interested use costs extra Mandate. \[ARCHIVED-NOT-CANON; cadence ED-751\] `.designs/systems/factions/reference/faction_layer_v30.md:453` · hook: veto on motion; per-faction cooldown · conf H
  - Eligible: Censure, Embargo, Outlawry, Recognition Challenge, Succession Endorsement, Treaty Ratification. Not eligible: War Authorisation, Blockade, Subsidy. Costs Mandate -1 if used against a motion that would have passed; further -1 if it protects Church interests. Infill frames it as Julius II voiding the Pisa council.

- **GV-015** `ARCHIVED` (+I,F) — CI milestones alter parliamentary procedure: at CI 55 motions against Church get Ob+1; at CI 65 secular factions need two action slots to pass a motion against Church. \[ARCHIVED-NOT-CANON\] `.designs/systems/factions/reference/ci_political_v30.md:70` · hook: CI milestone thresholds · conf H
  - CI 100: Theocracy Unification Attempt, secular factions each get one free motion per season opposing Church while it is active. Mass Seizure one-shot; no longer a win trigger (superseded by GD-1 Peninsular Sovereignty). Seasonal CI cap +-5.

- **GV-045** `ARCHIVED` (+H) — Succession by procedure varies per faction: Hafenmark Option B (Parliamentary vote on vacancy), Varfell elective (Jarl Assembly elects Regent), Crown Succession Contest with inner-circle supermajority. \[ARCHIVED; was CANONICAL\] `.designs/systems/factions/reference/faction_politics_v30.md:875` · hook: succession mode by faction · conf M
  - Hafenmark Std 6 Chancellor is succession-eligible via Parliamentary vote; Std 7 needs Baralta endorsement plus a Parliamentary resolution of endorsement. Varfell Hochjarl needs 3 of 5 senior Jarls at Disposition +1 or Grand Contest victory. Rank-ladder cascades given for Baralta Crown Claim outcomes.

- **GV-080** `ARCHIVED` (+H) — Church offices by college: College of Prelates elects a Cardinal by 2/3 supermajority; Confessor-Presumptive needs a College majority or unanimous election, then Consecration within 2 seasons or default to next majority candidate. \[ARCHIVED; was CANONICAL\] `.designs/systems/factions/reference/faction_politics_v30.md:339` · hook: college election thresholds · conf H
  - Cardinal requires 4 year-arcs as Prelate, endorsement of outgoing Cardinal or Confessor, no outstanding Grand Debates. Guild Master is elected by Free Masters in a territory; Grand Guildmaster by unanimous Council. Shows elected-conferral variety per faction: dismissal by heresy for Church, Assembly vote for Varfell, Censure for Hafenmark.

- **GV-099** `ARCHIVED` (+G,H) — Motion of No Confidence: Parliamentary Vote (Influence vs Crown Mandate) then Holy See concurrence; concur gives deposal (Crown Mandate to 1, Stability -3, succession Torben, else IP +10, else interregnum); refuse gives CI +3, TT +2. \[ARCHIVED; reference (TTRPG worldbuilding, not mechanics), was canonical\] `.designs/systems/world/reference/worldbuilding_v30.md:186` · hook: no-confidence two-step · conf H
  - Church has structural veto over regime change. Constitutional Crisis card triggers when Crown Mandate is 1 or Crown loses 3+ territories in a season: no-confidence raised automatically. Ministry Collapse card (Stability <=2): no legal proceedings, taxation Crown Wealth -1; counter by spending Influence.

- **HP-081** `ARCHIVED` (+G) — Old faction parliament: each faction votes its Mandate; majority over 50, supermajority at least 60; Church adds floor(CI/20) and has a once-per-4-seasons Sacred Veto. \[retired tree: parliamentary_vote.py and parliamentary_stay.py deleted at plan position 29b (engine/season/requirements.yaml:105-107); catalogue FILED 2026-08-27\] `research/cross_scale_action_catalogue_v1.md:146` · hook: none (retired) · conf H
  - Targets do not vote. Retired with the faction-stat model (Mandate, Influence), so not engine truth; kept as the repo's account of its earlier design.

- **OP-004** `ARCHIVED` (+E) — Persuasion Track 0-10: Side A wins at 7 or more, Side B at 3 or less, 4-6 is a compromise zone; start GM-set (neutral 5); audience resistance from faction Stability. \[ARCHIVED; PP-234\] `.designs/systems/social_contest/reference/social_contest_v30.md:99` · conf H
  - Resistance = average Stability of represented factions rounded up, minus 1 (min 0), typical 0-2. With no adjudicator the track is optional; a tied exchange majority means a stall: strain persists, Read results become permanent knowledge, relationship stressed.

- **OP-017** `ARCHIVED` (+F) — Board Game Parliamentary Vote: factions declare Side A/B/Abstain, each side picks a genre, pool is the sum of Mandate on each side, resolved on the Persuasion Track. \[ARCHIVED; ED-621; PP-256\] `.designs/systems/social_contest/reference/social_contest_v30.md:597` · hook: Diplomacy action (lobbying); Mandate · conf H
  - Lobbying offset capped to the 4-6 zone. Resistance base 0, +1 per Stability>=6 abstainer (max +2). Prior-season Diplomacy actions shift start +1 each (max +/-2, capped 4..6). Result >=7 passes, <=3 fails, 4-6 referred to committee; zero-zero also committee. Total Victory costs loser's dominant faction Mandate -1 for a season.


### D / NOTCODED

- **CD-018** `NOTCODED` (+L) — No vote exists: no verb casts one, no member's disposition is counted, no majority rule runs. A bench 'decides' because ONE seated judge rolls one contest. \[hole H-161 cite: C-7 vote-quorum conjunct measured and not built (waits on J-4)\] `engine/season/hole_register.yaml:3680` · hook: determine; commit; cardinality · conf H
  - Design C-7 says: no verb, no stored tally, tally as live commitments of bench members to a disposition Proposition. 'commit' exists, the disposition Proposition and the count do not. cardinality stays in the requires grammar with no class.

- **CD-075** `NOTCODED` (+B) — A bench of several judges does not deliberate or divide: the acting judge is one seated member; other seats count only toward bench size; no second judge need agree. \[hole H-161 and verb_table determine requires_typed_note\] `engine/season/hole_register.yaml:3680` · hook: determine; judging_set; bench.size · conf H
  - determine is an individual act of a member exercising the seat; the contest uses that judge's pool vs a default obstacle. Collective decision exists in the design (vote of members) but in code a 'bench decision' is one person's roll.

- **GV-086** `NOTCODED` (+H,F) — CR-35: an elected seat is filled by its faction's bench through determine, never confer; a contested succession by the throne's bench; electors are live same-faction seats granting determine; candidate must hold a live commit to the faction's proposition. \[workplan v10 position CR-35, STATE BUILD; FILLED_BY not found in engine/season (grepped)\] `workplans/valoria_master_workplan_v10_part4.md:365` · hook: election arm; FILLED_BY; judging_set matter · conf H
  - Gate arm 'election' in tenure_write_basis: seat has no live hold, FILLED_BY admits it, via-seat faction equals seat faction; for an inheritance seat the faction clause drops so any claimant (Baralta) may be judged. Elector commit to an OUGHT naming the candidate. Candidate with a commit to a second faction refused. Cardinal electorate rule confirmed (ED-IN-0301).

- **GV-087** `NOTCODED` (+B,H) — CR-36: nominate-then-confirm, a fourth way to fill a seat: a bench nominates by determine under parliamentary_debate, minting a resolution Record; a different seat then confers only on a held resolution naming seat and nominee. \[workplan v10 position CR-36, STATE BUILD; no 'nominated' basis in rosters.yaml (grepped)\] `workplans/valoria_master_workplan_v10_part4.md:378` · hook: resolution Record; determine -> Record; nominated basis · conf H
  - Court Parliament 'recommends policies, nominates Ministers' in worldbuilding becomes mechanism. First nominated seat is off_parliamentary_clerk. Two-seat clause: one seat cannot both nominate and confirm. A nominated seat's revocation disposal is ban as appointed. Needs determine's Record disposal site (unbuilt).

- **GV-091** `NOTCODED` (+I,L) — FA-07: Parliament seats and the Sacred Veto reread as CR-34's live-commit tally once CR-38 seats a bench; the seats are unbuilt (H-90) and the Veto is a residue; Parliamentary Stay is a named residue triggered by H-90's Parliament being seated. \[workplan v10 FA-07, STATE LEAVE (named, unscheduled)\] `workplans/valoria_master_workplan_v10_part5.md:178` · hook: Sacred Veto residue; Stay residue · conf H
  - Also: Piety Track becomes the share of residents whose live commit is to the Church's Proposition; Church Attention is each Church seat-holder's own ledger; every stored clock refused. Gransol exception refused. Sacred Veto and Stay thus have no scheduled home.


### D / RESEARCH

- **CL-056** `RESEARCH` (+I,F) — Deliberation dynamics: faction size dominates; first-ballot distribution is the strongest predictor; majorities have informational plus normative influence, minorities informational only; slow-then-accelerating movement; once started rarely reverses, except at the first juror who crosses to the minority. \[SOURCE MATERIAL; T1 Devine et al. 2001 meta-analysis\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/04_negotiation_and_persuasion.md:140` · conf H
  - Doc N10: first ballot, influence asymmetry, acceleration, momentum, tunable asymmetry. 'Highest-value persuasion target is one specific person at one specific moment' (the first defector). Survived adversarial attack (line 502).

- **CL-057** `RESEARCH` (+M) — Leniency asymmetry is contested: mock-jury meta-analysis (13 studies) shows evenly split juries acquit ~4x as often as convict; Devine 2004 field data shows none; Kerr re-analysis finds a real but weaker asymmetry. Carried as a tunable parameter. \[SOURCE MATERIAL; CONFLICT logged: MacCoun & Kerr vs Devine\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/04_negotiation_and_persuasion.md:148` · conf M
  - Two entries disagree and are both recorded: resolved by recency and coding-bias argument. Doc 4 itself notes laboratory findings may not generalise (A5, line 481): T1 marks provenance, not transferability.

- **CL-103** `RESEARCH` (+B) — Review finds the repo's 'Renaissance deliberation and classical inheritance' research (Aristotle's tripartite constitution, Polybius mixed constitution, Cicero's res publica, universitas and quod omnes tangit, Bartolus, Marsilius's valentior pars, Cusa) is institutional-scale, imported down to personal contest, never reverse; Cicero's council-speech theory is its only individual-technique citation. \[FILED informational review 2026-07-08, advisory\] `.audit/2026-07-08-contest-settlement-faction-interface/interface_report_v1.md:336` · conf M
  - The cited document renaissance-deliberation-and-the-classical-inheritance.md is not present in the worktree (find returned nothing); only this report and fa_se_historical_precedent_research_v1.md:75-77 describe it. Treat as secondhand.

- **HP-056** `RESEARCH` (+A) — P14 Division (discessio): when several motions are live the chair chooses which to put and in what order, voting singly until one carries. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:373` · conf M
  - Roman presiding magistrate put motions 'such as he pleased' (T2). Count is standing-weighted or head-counted by the body's procedure. Order of putting must be a decision, not automated.

- **HP-057** `RESEARCH` (+I) — P15 Veto (intercessio): blocks a motion; scoped (before debate or stripping a carried motion); cost is political, paid in Standing and the Ledger. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:379` · conf M
  - Cites Polybius 6.16, Cicero de Legibus 3.3.10 (T1) and Ming fengbo/fenghuan, the returned edict. A free veto is used every time; the tribune's veto rested on an irreplaceable body.

- **HP-064** `RESEARCH` — P22-P24 Selection: sortition for unpredictability of target (ballottino, Florence's bimonthly lottery); threshold elections (25 of 41, 9 of 11/12, 7 of 9); alternating narrow/widen chain. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:424` · conf H
  - Chain 30-9-40-12-25-9-45-11-41. Makes bloc-building partially effective; must be playable with a spend decision at every stage, not a cutscene.

- **OP-096** `RESEARCH` (+I,F) — No consensus (Type-3) procedure: RM and Wardens are consensus institutions but 'by consensus' collapses into the Mandate-weighted sigma vote; there is no unanimity threshold, holdout or veto move. \[RESEARCH citing 2026-06-28 deliberation critique (filed medium/high, not promoted to ED)\] `.audit/2026-07-08-contest-settlement-faction-interface/interface_report_v1.md:277` · hook: consensus game stub; Sacred Veto · conf M
  - Nor sortition; proposed fix is a thin Consensus Proceeding with per-assenter rolls, a holdout minting an Obligation clock, and an anti-gaming cost mirroring Sacred Veto. Fable-5 audit sequencing ratified 2026-07-05: P0 spec reconciliation, P1 consequence spine, Stage 4 four-games build, calibration. Consensus mode was planned as a promotion of faction.py coalition_vote machinery, not a new engine.

- **OP-099** `RESEARCH` (+B,I) — Old board-game Parliament Integrity (PI) 0-20 meter (start 7): high PI gives a full Parliament where Crown Policy requires Mandate >=4. \[RESEARCH/PROPOSED decomposition of the old canon corpus (2026-09-03) with indexed contradictions; not code\] `proposals/2026-09-03-governance-corpus-rebuild/annex-a-decomposition.md:351` · hook: parliament.md PI scale (old canon) · conf M
  - PI <=2 makes Hafenmark lose Parliamentary Manoeuvre and the Crown govern by decree; PI degrades by Emergency Powers, Church seizure, Lowenritter coup and recovers by Manoeuvre success or Crown Parliamentary Session policy. Annex flags contradictions (CT-27: table monotone but another doc says it auto-resolves at PI>=20 on Crown elimination; 11-20 undefined).


### D / HISTORICAL

- **CL-034** `HISTORICAL` (+B) — Lögrétta law-council seats 48 godar each with two advisors he may consult in session; decides by cascade consensus, then lot (by quarter), then majority (afl rada); three-mark fines for procedural failure. Open Lögberg vs closed Lögrétta two-venue split. \[RESEARCH; Grágás Lögréttuþáttur\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:516` · conf M
  - Cascade consensus-to-lot-to-majority is a sourced decision procedure; goði plus two counsellors is a distributed-deliberation primitive with bounded consultation per voter. Anyone could speak from the open Lögberg.

- **CL-069** `HISTORICAL` (+B,F) — Composition contest: who sits on the deciding body is a larger, prior, longer-timescale contest than what is said. Roman jury panel fought over for ~50 years (Gracchus 122 BC, Sulla, lex Aurelia 70 BC splitting 900 jurors in thirds) while substantive law stayed unchanged. \[SOURCE MATERIAL; T1 Lex Aurelia iudiciaria; Roman quaestiones perpetuae\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/05_persuasion_in_the_era_sources.md:66` · conf H
  - Doc N19: persuasion difficulty set by a campaign-scale contest fought chapters earlier (voir dire at campaign scale). Audit B8: the interesting scene may be decided before it starts. Court always open; any citizen could bring a charge; album compiled annually by the urban praetor.

- **HP-001** `HISTORICAL` (+B) — Roman consular intercessio: each consul could veto the other; internal peer-blocking veto distinct from vote-tallying. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:106` · hook: governance_mode / Consensus holdout (proposed) · conf M
  - Two annual consuls each held imperium and could block a colleague. Repo hook: OLIGARCHIC_COUNCIL seat with unilateral block should gate the Consensus resolver's holdout state rather than be tallied. Collegiality (pairs) is the structure.

- **HP-003** `HISTORICAL` (+B) — Rome ran several assemblies at once with different electorates and binding scope: wealth-weighted comitia centuriata (193 centuries), tribal comitia tributa, plebeian concilium plebis. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:108` · hook: governance_mode (proposed) · conf M
  - lex Hortensia 287 BC made plebiscita bind everyone. Repo hook: a Settlement may carry two co-resident governance bodies whose jurisdictions overlap and collide, not one mode per tier.

- **HP-004** `HISTORICAL` (+I) — Tribune of the plebs: sacrosanct person plus intercessio over any magistrate, senatus consultum or fellow tribune; can only block, never compel. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:109` · hook: bypass authority type (proposed) · conf M
  - Gracchus deposed fellow tribune Octavius 133 BC by plebeian vote, a fight over the lever itself. Repo hook: a negative-only chain-bypass type (nullify, cannot command), removable only by the body that created it.

- **HP-010** `HISTORICAL` (+B) — Golden Bull 1356: seven electors fixed (3 ecclesiastical, 4 secular), majority 4 of 7 binding, Mainz convenes and presides, secular electorates indivisible by primogeniture. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:192` · hook: governance_mode LANDHOLDER_FRANCHISE (proposed) · conf H
  - Closed the double-election failure of 1198, 1257, 1314. Repo hook: OLIGARCHIC_COUNCIL with fixed seat cap and anti-splitting rule, plus recurring election even when one house keeps winning.

- **HP-013** `HISTORICAL` (+B) — Florence Ordinances of Justice 1293 (Giano della Bella): 152 magnate families barred from office, collectively liable, enforced by the new Gonfaloniere di Giustizia. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:254` · hook: OLIGARCHIC_COUNCIL carve-out (proposed) · conf M
  - Legitimacy from guild membership not blood. Repo hook: a named social bloc formally excluded from ranks 3+ with a dedicated enforcement office.

- **HP-015** `HISTORICAL` (+F) — Squittinio and imborsazione: vetted names in leather bags, blindfolded draw (tratta); Medici accoppiatori later packed the scrutiny and overrode by hand. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:261` · hook: eligible-officeholder pool (proposed) · conf M
  - Sortition legitimated by prior oligarchic vetting; power lay in who was scrutinised in. Repo hook: officeholder pool as a weighted bag a faction can quietly pack over cycles.

- **HP-022** `HISTORICAL` (+I) — Conclave: Gregory X's Ubi periculum (1274) locked cardinals in with shrinking rations until a two-thirds majority; cardinal-nephew substitutes for heredity. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:295` · hook: Consensus resolver holdout (proposed) · conf H
  - After a 1268-71 vacancy. Repo hook: holdout imposes an escalating but decaying cost on the whole body, a real but time-limited leverage instead of a free veto.

- **HP-028** `HISTORICAL` — Venetian doge election 1268: nine alternating stages of lot and vote ending in 41 electors, 25 votes needed; a boy draws the lots. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:353` · hook: Consensus resolver pipeline (proposed) · conf H
  - Designed so capturing the electorate means controlling every round; sortition breaks pre-arranged coalitions, election retains judgment. Repo hook: multi-round Consensus pipeline of random subsets.

- **HP-032** `HISTORICAL` (+B) — Kamakura Hyojoshu (1225): standing council of co-equal members under Hojo shikken issuing binding rulings by internal procedure under a codified rulebook (Shikimoku). \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:436` · hook: OLIGARCHIC_COUNCIL (proposed) · conf M
  - Shogun became figurehead. Repo hook: OLIGARCHIC_COUNCIL with named seat count and codified charter.

- **HP-049** `HISTORICAL` (+B) — A prior 2026-06-28 corpus catalogued 13 pre-1600 decision-procedure families (kleroterion, imborsazione, broglio, liberum veto, Cortes of Leon 1188, kurultai, Gadaa and others); files not in tree. \[FILED research; inventory of a 2026-06-28 corpus\] `research/fa_se_historical_precedent_research_v1.md:75` · conf L
  - This report only names them; the underlying files are not in the tree (keyword search of research/ and .audit/ finds the terms only here, in the interface report and one game table). Also lists civic humanism (Bruni, Contarini, Machiavelli Discorsi, Guicciardini), conciliarism, Marsilius, Cusa.

- **HP-095** `HISTORICAL` (+B) — Cortes of Castile and Aragon: Castile's 18 cities send two procuradores each to negotiate fixed multi-year taxes, cannot legislate or self-convene; Aragon's four brazos once needed unanimity. \[FILED 2026-07-09 research, proposals KEEP/CUT judged; most items needs_jordan or unratified\] `.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:127` · hook: none (proposed Compact tag) · conf M
  - The first draft wrongly said Aragonese unanimity survived to 1707; the verified version says it was a consent rule changed by scripted event (Tarazona 1592). Encabezamiento locks a tax figure below capacity in return for a petition right (HAB-5).

- **HP-097** `HISTORICAL` (+H,I) — HAB-6 Crush the Estates: an irreversible rewrite of a ratified faction's rank-ladder gate (Alderman two-thirds supermajority replaced by direct crown appointment) modelled on Cortes of Tarazona 1592. \[FILED 2026-07-09 research, proposals KEEP/CUT judged; most items needs_jordan or unratified\] `.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:222` · hook: none (proposed) · conf M
  - Marked needs_jordan, cross-lane and irreversible. Rise-to-power research adds that heritable robe-class ranks make clawback cost escalating Legitimacy.


### D / GAME

- **CL-059** `GAME` (+M,B) — Reacting to the Past: the audience is a set of agents, factions with shared aims plus 'indeterminates' with incomplete, imprecise or undisclosed aims who cannot win alone and must be courted individually; investigating them is a probe on a person. \[SOURCE MATERIAL; T1 Barnard RTTP programme\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/04_negotiation_and_persuasion.md:184` · conf M
  - Doc 4 N9 'Body' and N1 'Mind' (not a meter); calls it the only alternative to a persuasion meter found across four surveys, content-expensive (A3). Contrast with the Griftlands card finding.

- **HP-085** `GAME` (+G) — P09 weighted vote with a threshold: named blocs or seats cast weighted votes and a fixed share decides; P10 keeps one approval score per bloc. \[FILED 2026-10-22 tier-3 reference, not canon; claims tagged V3 (fetched) / V2 / M (model memory)\] `research/game_precedent_suite/THROUGHLINES.md:25` · conf M
  - Games cited include Frostpunk 2 council and Victoria 3's eight interest groups. Dispositions disagree whether Valoria has a vote at all (D_T05 says kernel ballot tests-only, D_T09 says none).

- **HP-089** `GAME` (+F,I) — EU4 estates: grant or revoke privileges against loyalty and influence; revoking needs loyalty above influence and costs loyalty; seizing land costs every estate loyalty; summoning the Diet takes one agenda. \[FILED 2026-10-22 tier-3 reference, not canon; claims tagged V3 (fetched) / V2 / M (model memory)\] `research/game_precedent_suite/tutorials/T17_repo_strategy_a.md:26` · conf M
  - Crownland share, absolutism and estate disasters; Diet roughly every five years. Estates as the polity grain (throughline 9). Players keep loyalty near 45-50 and crownland above 30 percent.

- **HP-093** `GAME` (+G,F) — Imperator: Rome republic government: actions needing senate approval cost tyranny when approval is low; senate factions elect the ruler; offices give stat bonuses but do not make policy. \[FILED 2026-10-22 tier-3 reference, not canon; claims tagged V3 (fetched) / V2 / M (model memory)\] `research/game_precedent_suite/tutorials/T12_paradox_classical.md:105` · conf M
  - Government type changes the political game entirely (republic senate approval and tyranny; monarchy legitimacy; tribe clan chiefs). CK2: crown authority at five levels costs vassal opinion; succession law choice including elective and tanistry; levy scales with opinion.

- **HP-103** `GAME` (+B,G) — Parliament survey: Victoria 3 enactment as a staged process with setbacks and lockout, plus agenda control, division, recorded defeat and drafting loans from Rome and Ming. \[PROPOSED 2026-08-28 reference under 0.05, not canon\] `research/valoria_game_precedent_companion_v1.md:107` · conf M
  - Verdict: Valoria had the vote and none of the procedure (no agenda, chair, recorded defeat, drafting layer or shared-loss condition). Ahead: the legible Persuasion Track, not to be flattened into a hidden clock.



## J · Record, memory and reputation — 23 entries (CODED 2, INTENT 5, PROPOSED 5, ARCHIVED 2, NOTCODED 2, RESEARCH 6, HISTORICAL 1)


### J / CODED

- **CD-073** `CODED` (+M) — Pressure as a standing-band crossing: MATTER records a crossing when the gap over claims about a person crosses a floor; next season a question names the tellers. \[hole H-222 + test_sc02_22b_standing_crossing.py; built, never fires in realm play\] `engine/season/hole_register.yaml:4711` · hook: standing_of; standing.band_crossed; questions_for · conf H
  - Proven on a hand-built world (told three things about himself). In the realm nothing mints a claim on a person_predicates member, so the gap is constant and nothing crosses. Floors (500,) are an injected assumption (H-223).

- **PR-100** `CODED` (+M,C) — Reception is CODED resolver-side: world_q.reception(w, speaker, venue) = sum over bench members of their own deed claims about the speaker weighted by remove_weight(source) x decayed confidence x member valence; proofs(w, speaker, opponent, venue) weighs speaker's claims by remove and zeroes any the opponent mirrors; route erosion zeroes a dominance weight after a called bluff. \[code at world_q.py:581 reception, :641 proofs (v9 SC-02 22a); test engine/season/tests/test_sc02_reception.py; arm 2 of the alignment table never authored (H-215 open)\] `engine/season/queries/world_q.py:581` · hook: world_q.reception/proofs; REMOVE_ORDINAL; standing_routes · conf H
  - Falsifiers in tests: bench obstacle invariant under a change to a member's ledger (so the Query is unreachable from a decision); mirrored proof moves nothing; called bluff zeroes dominance deeds no newer. reception_gain H-215, proof_step H-216 swept constants.


### J / INTENT

- **PR-006** `INTENT` (+C) — Descent down the issue ladder is a conceded act; cost needs no rule because every present witness deposits a claim that the descent happened. No concession_penalty field exists. \[00 PROPOSED; QUALIFIED by 21_RECONCILIATION C-2: visibility true at kind granularity only until R8.2 observation producer\] `proposals/2026-09-05-proceedings-subsystem/00_DERIVATION.md:177` · hook: WITNESS fan-out; claim deposits; observation_terms · conf H
  - 21 C-2: room learns that a descent happened, not how far, until a per-term observation producer (R8.2, IN lane, P-22) lands. Prediction D-6 expected to fire: a descent before an empty floor costs nothing. A hearing resumed next season restarts at ladder top.

- **PR-018** `INTENT` (+K) — One 'seen' claim per (witness, event), value {stratum, marks, who, why}, subject = changed thing else the rung (for a speech: the venue), so everyone contained there can raise a question; reception reads value.who. \[21 C-4 ruled: R8.1 shape wins; F-32 withdrawn (B.1)\] `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md:248` · hook: Claim.value struct; observation_terms; Q2 question; reception · conf H
  - Supersedes 19_PLAN step 2 'prepend the actor' mechanism. +1 claim per witness-event; eviction comparator untouched. Makes misattribution, hearsay and wrong-person-blamed reachable. Per-term split (R8.2) deferred. F-32's claim that actor survives was an artifact of a payload-less test.

- **PR-031** `INTENT` (+K) — Free descent in a closed room is correct: the argument's audience was never the world, and the player is IN the room (a small recurring cast of peers). The risk is forgetting (ledger_cap=200 evicts on confidence, recency), not concealment. \[03 B.8 Jordan ruling; P-41 closed as IRRELEVANT; risk relocated to P-42\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:295` · hook: ledger_cap (shape.py:1772); claim eviction; P-42 · conf H
  - Jordan: playing head of a major faction like Baralta means being in those closed rooms with game peers. Question becomes whether the bishop who watched you fold three seasons ago still holds it. 21 says the cap now evicts nothing after fan-out narrowing; P-42 measurement remains.

- **PR-079** `INTENT` (+K,C) — Three passes converge: corpus says a move's outcome is a reading ABOUT THE MOVER (15 of 27 figures); precedent says the load-bearing mechanism is typed persistent relationship records (A,B)->{type, magnitude, source_event, expiry} that gate eligibility; the code cannot write that record (no deposit names actor; all claims firsthand 100; told_by never minted; fan-out total). \[18 PROPOSED then ratified as intent; 21 C-4 replaces 'prepend the actor' (O-1) with R8.1 struct; 18 PART L item 1 superseded\] `proposals/2026-09-05-proceedings-subsystem/18_FINDINGS.md:49` · hook: WITNESS deposit rule; Claim.source/visibility; claim_subject_rule · conf H
  - Fix named: three deposit rules and one field. Second convergence: overshoot not deficiency (13 figures) - Failure sits just past Success, fail-forward sourced. Third: terminal = being seen at it (7 figures); costly = effect faults, terminal = exposure faults; Claim.visibility inert so severity = size of observer set at witness minus actor (19 step 21).

- **PR-104** `INTENT` (+K,L) — Six feedback loops signed: L-1 standing->reception->outcome->standing (amplifying, bounded by Turned band writing against you, elaboration, the erosion list, dominance route collapse on one bluff); L-2 descent (damping, finite ladder); L-3 witness->claims->questions->acts->witness (H-102, positive, not this design's); L-4 appeal (max_depth); L-5 interposition<->impasse UNSIGNED; L-6 determination->conviction UNSIGNED and severed. \[10 PROPOSED then ratified as intent; L-1 falsifier P-20 (forty seasons: does standing concentrate) is not run\] `proposals/2026-09-05-proceedings-subsystem/10_LOOPS_AND_GAPS.md:19` · hook: reception; stance; conviction write (O-7) · conf H
  - If L-6 positive a judge hardens into caricature over forty seasons; if negative every bench converges. The design writes no conviction-moving edge (P-21), safe but not a design. Real failure mode is L-1 unbounded because three of four bounds are properties of the corpus not the code.


### J / PROPOSED

- **OP-024** `PROPOSED` (+K,G) — Record spine: a close emits typed ledger Records (Precedent, Debt, Grudge, loser-record priced by margin) that factions hold and later contests read, instead of only stat deltas. \[PROPOSED CIP-1 (evidenced, highest value-to-cost per doc)\] `proposals/social_contest_consolidation_integration_v1.md:171` · hook: ledger.py LedgerTag; DomainEchoResult.records · conf H
  - Adds ledger list to Faction and contest Body, source/parties/uses/superseded_by fields, holder dimension, and reach. Falsifier: a seeded trace where a season-N contest changes which branch fires in season N+k. Distinct proceedings = distinct emittable record types. Cross-lane SE.

- **OP-032** `PROPOSED` (+K,F) — The audience as a party: the room has taste distinct from the bench (crowd profile config row), leaves a fama impression bounded by presence. \[PROPOSED CIP-14, CONDITIONAL on CIP-9b; headline item\] `proposals/social_contest_consolidation_integration_v1.md:601` · hook: Room; Pressure; Reputation ledger · conf H
  - And the bench presses back by reach; you can lose the case and win the room. Jordan: audiences press on characters and adjudicator and carry impressions into the world. Two of three channels already wired (Room->Readiness, Pressure->bias and leak); world channel absent. Conditional on CIP-9b, divergent bench/room taste, a reputation economy with stakes, and CIP-12 ruling.

- **OP-042** `PROPOSED` (+D) — A defeated or vetoed motion leaves nothing a later speaker can cite: records_dissent is a key on arrangement rows that nothing reads. \[PROPOSED gap SC-G09\] `proposals/2026-10-16-verbs/2026-10-16-verbs-21-gap-register-sc-and-gv.md:42` · hook: records_dissent; determine; carry · conf H
  - Senatus auctoritas / recorded defeat is called nearly free to implement. Cites Roman senatus auctoritas and tribunician intercessio as precedent for recording a blocked measure. Also SC-G08: the chair's order of motions and forwarding/amending/dropping a held petition are 'unowned', and carry is the only route by which a seatless person puts a matter before a room.

- **OP-053** `PROPOSED` (+K,D) — The bench remembers the hearing: a Query over seated judges' ledgers of speak outcomes enters the verdict's room, and the accused may answer his own matter. \[PROPOSED CP-T05-02\] `proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-05-social-contest.md:135` · hook: WQ::hearing; speak; subject_may_be_self; matter.advanced/turned · conf H
  - Outcomes count carried +2, advanced +1, held 0, turned -1; sign flips if the act was the party's own. New column subject_may_be_self lets a docketed party plead for himself. A lost hearing counts against its side in the next.

- **OP-066** `PROPOSED` (+D,I) — Recorded defeat: every sitting writes a record row (CARRIED, FAILED, CARRIED-WITHOUT-FORCE, WITHDRAWN, CLOSED-ON-FAULT). \[PROPOSED\] `proposals/2026-08-29-valoria-from-scratch/08_argument.md:248` · hook: record row; pattern counter; F2 · conf H
  - A motion that won a majority but was vetoed or unpublished is citable at proof grade G4 and banks a contradiction hazard on the vetoer. Senatus auctoritas: nearly free, few games have it.


### J / ARCHIVED

- **OP-009** `ARCHIVED` (+M) — Composure is retired as the contest buffer and split into three trackers: Concentration (stamina), Face (transient contest-local standing), Persuasion Track (merits clock). \[CR3 ratified 2026-06-01; ED-1056 Face scale-binding resolved Gate A\] `.designs/systems/social_contest/reference/social_contest_v30.md:240` · conf H
  - Face_max = Charisma x3 (3-21); Face_current = round(Standing/10 x Face_max); Face resets at contest end and is distinct from persistent Disposition/Reputation. Strain accumulates against Face; at threshold a Rattled mark gives -1D per level. Doc states strain-to-Face consumption is not wired in code.

- **OP-011** `ARCHIVED` (+K) — When an argument leaves a Conviction Scar on an NPC the player gets a momentary portrait cue (crack, flicker) with no count shown; Appraise later reveals Scar count. \[ARCHIVED; player-facing videogame note\] `.designs/systems/social_contest/reference/social_contest_v30.md:368` · conf H
  - Deliberate hidden-information signal so the player must remember that they wounded a conviction. Videogame implementation note embedded in a TTRPG-era doc.


### J / NOTCODED

- **CD-009** `NOTCODED` (+D) — records_dissent (whether a division is recorded) is declared per row but nothing records who dissented; no minutes, no division list exists in code. \[key records_dissent loaded; no production reader\] `engine/season/data/arrangements.py:225` · hook: arrangement records_dissent · conf H
  - The loader's own docstring says under a declared disposal the dissent key 'is the tally made visible'. No tally exists, so the key has no referent in running code.

- **CD-072** `NOTCODED` (+G) — Failure severity by who saw it ('terminal = being seen at it'): unseen failure costs only the actor's stance, a seen one also fires a terminal write. \[hole H-219 (STOPPED at v9 SC-02 22a)\] `engine/season/hole_register.yaml:4672` · hook: Claim.visibility; WITNESS observers · conf H
  - Not built: no row's Failure band writes anything to grade. The design calls it the corpus's cleanest severity rule. Claim.visibility is kept. No public-shame or recorded-defeat cost exists for a lost speech.


### J / RESEARCH

- **HP-058** `RESEARCH` (+D) — P16 Recorded Defeat (senatus auctoritas): a motion carried but vetoed persists as a Record with no force and full citability; may be re-put later. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:385` · hook: Record (disposes: Record) · conf M
  - Converts defeat into a durable asset and gives losers a reason to keep pressing. Roman category cited T1. Resolution creates a Record with Status vetoed.

- **HP-065** `RESEARCH` (+E) — P28 Standing Report (relazione): a persistent, cumulative document on another polity updated by successive ambassadors, decaying with time and stealable. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:459` · conf M
  - Venice required it of every recalled ambassador and was alone in doing so (Queller; Goffman, T1). Value grows over a campaign, a better reward than a number.

- **HP-098** `RESEARCH` (+B) — Parliament state graph S5: Dormant, Convened, Agenda (amendments), Drafting, Roll, Division, Carried/Lost, VetoWindow, Enactment or Record, with a nested enactment machine of setbacks, mobilised opposition and revolt. \[SOURCE MATERIAL, not canon; self-authored upload with evidence tiers\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/02_political_state_graphs.md:238` · conf M
  - Two clocks: session (minutes) and enactment (months). Session slots are the scarce container; P20 drafting and P21 return-unsigned give the clerk leverage; P45 shared loss needs AI factions to plan far enough to defect then relent, an unsolved opposition-model problem.

- **HP-099** `RESEARCH` (+G) — Throughlines: T1 record spine (every terminal state emits a citable Record guarding a later transition) and T5 bond chain (costly signal, lodged bond, forfeiture). \[SOURCE MATERIAL, not canon; self-authored upload with evidence tiers\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/02_political_state_graphs.md:632` · hook: Record / Tenure · conf M
  - Sealed denunciation (P30) is the one information primitive that reaches the adjudication cluster. The audit advises not breaking the S2 tribunal / S5 parliament cycle (officeholding must be risky) and not unifying negotiation with settlement management.

- **OP-089** `RESEARCH` (+G,K) — Every wired contest output dead-ends as a stat delta; Obligations had no code consumer and Committee referral produced nothing, while a Record primitive (LedgerTag) existed one subsystem over. \[RESEARCH audit finding (P1 NEW, ED-SC-0019)\] `.audit/2026-08-06-social-contest-three-lens-audit/00_synthesis.md:220` · hook: settlements/sim/ledger.py LedgerTag (old) · conf H
  - LedgerTag kinds: Precedent, Grudge, Debt, Reputation, Leverage; TTL; survives succession. tribunal.py deleted the canonical prerequisite 'Obligation violation or 2 prior convictions'. Fix: Decisive win emits Precedent, Obligation is a Debt, violation a Grudge.

- **PR-014** `RESEARCH` (+C) — Standing has four provenances (ascribed, accumulated, performed, staged); the predictive cut is prestige (freely conferred, erodes slowly) vs dominance (extracted by fear, collapses on one called bluff). \[01 PROPOSED; study Figs 3 and 25\] `proposals/2026-09-05-proceedings-subsystem/01_THE_STUDY.md:190` · hook: standing_routes roster; Query.standing · conf H
  - Byzantine reception (distance) vs Carolingian audience (closeness) are both A4 staged; route distinguishes them. Erosion: inconsistency, visible self-interest, visible effort once seen (terminal), over-claiming rank, the DISCOVERED lie (terminal). Liudprand 968: seating was the negotiation - titles are a pre-content procedural settlement.


### J / HISTORICAL

- **HP-039** `HISTORICAL` (+G) — Roman lex repetundae (149 BC): returning governors prosecuted; Cicero's Verrines itemise demanded versus delivered tribute, a ledger of extraction versus entitlement. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/political_hierarchy_standing.md:139` · hook: resolution-quality to standing bridge (proposed) · conf M
  - Conviction meant exile and confiscation. Repo treats this as a near-literal precedent for the resolution-quality to standing bridge.



## L · Architecture and coding constraints — 32 entries (CODED 4, RATIFIED 8, INTENT 5, PROPOSED 3, ARCHIVED 1, NOTCODED 4, RESEARCH 7)


### L / CODED

- **CD-069** `CODED` (+K) — No game code may branch on an arrangement id: a scan fails if any effect compares to a literal row id such as tribunal; arrangements differ only by data. \[test at test_sc01_the_bar.py:287 (scripting-drift falsifier)\] `engine/season/tests/test_sc01_the_bar.py:287` · hook: ARRANGEMENTS; scripting drift guard · conf H
  - A planted if arrangement.id == 'tribunal' in _eff_determine reddens the test. The scan sees literal compares only. The design claim 'a proceeding is just defined parameters' therefore holds, but only the disposes key actually differs in behaviour.

- **GV-058** `CODED` (+H) — Authority is rank plus containment: eligibility resolves through the seat carried by the act (Act.via) and purview asked of via.scope; delegates therefore work (regency was previously unbuildable). \[hole register row H-90, grade ruled; wiring partly built\] `engine/season/hole_register.yaml:1116` · hook: Act.via; in_holdings · conf M
  - Prior default read authority off the actor's own titles; superseded 2026-09-03 by #358 rev.2. Jordan 2026-09-02 four messages: King does not hold sovereign power of all territories; sovereign power is uncontested and absolute and the game has a Parliament so no monopoly in the ruler. Delegation to lesser ranks of governing their holdings.

- **GV-059** `CODED` (+B) — Generic 13-seat ladder hearth to realm with one binary split at the duchy, owned by test faction x, used to observe dissemination and aggregation. \[code: test fixture ladder (faction x), not canon\] `engine/season/governance_spine.yaml:1` · hook: governance spine fixture · conf H
  - Settlement shapes (publicly elected mayor/council, assigned governor/council) deliberately not modelled; ED-IN-0256 later ruled conferral appointed/elected/annex (not a 2x2). Two chains under one realm to show divergence. The spine adds regularity not depth.

- **OP-022** `CODED` (+C) — The live social-contest module entry is a single sigma-leverage roll returning a Margin (net, ob), not a winner; the older contest kernel is evaluated and explicitly NOT adopted. \[code at modules/social_contest/roll.py:16 (SC-05 measured 2026-10-16; ED-SC-0037 ruled by Jordan 2026-09-09)\] `modules/social_contest/roll.py:16` · hook: module social_contest entry roll; verb tell; provider contest/social_contest · conf H
  - Reasons: kernel uses global RNG, returns winners/bands not margins, reads a faculty not the host record. roll = roll_net(pool)+net_boost(leverage,pool); the proceedings nested run is stated 'unbuilt'.


### L / RATIFIED

- **CD-052** `RATIFIED` (+B) — The proceedings subsystem owns all social contests; seam dispatches by manifest row; prizes repoint to its provider; the obstacle has a single owner; the orphaned social-contest code retires. \[ED-SC-0033 ruled (Jordan, 2026-09-06); clause 2 retirement unexecuted\] `registers/editorial_ledger_sc_archive.jsonl:36` · hook: contest_subsystems; module social_contest · conf H
  - Jordan: 'this subsystem obviously owns all social contests'. Clauses 1-3 coded (SC-01). Retirement of systems/social_contest/sim/contest/ is ruled, unexecuted: timing is SC-05, asked and unanswered.

- **CD-054** `RATIFIED` (+C,J) — Option B taken: reception and proofs must be re-sourced from commits because the fold may read only the ACTOR'S OWN ledger (Layer 1 F8); the shipped code reads others' ledgers. \[ED-SC-0040 LAST ROW closed 2026-10-26 (v10 step 4b); HANDOFF_SC still reads it as needs_jordan\] `registers/editorial_ledger_sc.jsonl:5` · hook: reception; proofs; commit · conf H
  - Layer 1 is ratified and binds; 19_PLAN steps 17-18 are intent only. Revert if Jordan authorizes option A (amend B.2). Code at world_q.py:581/:641 still reads bench and opponent ledgers: the re-source is DESIGN-FIRST in SC-02 and unbuilt. HANDOFF_SC row 11 is stale against this row.

- **CD-058** `RATIFIED` (+C) — A contest provider returns a MARGIN, never a winner; one ladder reads it; a provider veto can only demote; claimants are persons, never factions; no state write from inside. \[Layer 1 C.5 contest seam (ratified)\] `architecture/meta/04_CODE_ARCHITECTURE.md:770` · hook: seam.contest; Margin; degree_of · conf H
  - Why a debate subsystem may not return 'A won'. The legacy kernel returns winners (band labels a/b/draw), which is why SC-05 measured and kept the interim roll.

- **CD-059** `RATIFIED` (+D) — Every act: eligibility, then requires against the world predecessors left, then a contest giving a degree, then degree-keyed gate writes, then emits; a failed precondition emits a refusal and writes nothing. \[Layer 1 C.4 one fold (ratified)\] `architecture/meta/04_CODE_ARCHITECTURE.md:658` · hook: RESOLVE fold; requires; writes_at(degree) · conf H
  - The scarcity channel. A debate that must end in a vote has to be built as acts in this fold: nothing can be decided by a clock or by the module. A below-quorum determine is a refusal that retries each round.

- **CD-066** `RATIFIED` — Retire the orphaned social-contest kernel and relocate its degree veto as an extension at the ladder; Jordan leans (indirect) to adopt, only the timing is asked. \[plan position SC-05, B10-Z; ASK-THEN (timing only), unanswered\] `workplans/valoria_master_workplan_v10_part5.md:265` · hook: systems/social_contest/sim/contest; degree_extension · conf H
  - Measured at SC-01 step 15: kernel takes no rng parameter (global random), returns winners not margins, reads a faculty not the host record. The interim sigma roll stays; the kernel (16 tracked files) is not adopted and not yet deleted.

- **CL-108** `RATIFIED` (+C) — Plato appears in canon only as Neoplatonic metaphysics (cascade from the One through intellect, soul, matter; shefa), a world-truth source; it is not connected to rhetoric, dialectic or the Gorgias/Phaedrus anywhere in canon/ or .designs/. \[canon review file under canon/philosophy/_review; Neoplatonism used for world metaphysics only\] `canon/philosophy/_review/C_lens_findings.md:138` · conf M
  - Cited so an adjudicator does not mistake 'Platonic' hits for rhetorical Plato. Rhetorical Plato is limited to: one paragraph in RHET:73, the Phaedrus contrast in the proceedings study (CL-083), and reading-list titles (CL-088). Plato's Republic is not discussed anywhere in research/, .audit/, proposals/ or .designs/.

- **GV-100** `RATIFIED` (+B) — GD-3: emerging factions start non-parliamentary (cast no Parliamentary votes), operate territorially, and promote to formal Faction (parliamentary or extra-parliamentary) when L>=3, 2+ territories, Accord>=4 averaged, sustained two seasons. \[canon constraint GD-3\] `canon/02_canon_constraints.md:72` · hook: parliamentary vs extra-parliamentary flag · conf H
  - Pipeline Revolt > Insurgency > Faction. Extra-parliamentary status blocks formal motions (used by Parliamentary Transfer). GD-1: sole victory is Peninsular Sovereignty (control all 15 territories, treaties counting), the political aim parliament moves feed.

- **PR-108** `RATIFIED` (+B) — The old social-contest kernel systems/social_contest/sim/contest/ is to be retired (deleted from main, kept at a named ref, FORK row, 20+ inbound references re-resolved) once the proceedings prizes repoint; ownership of the prize routing settled at ED-SC-0033. \[19 PART H D-1 RULED by Jordan 2026-09-06 ('orphaned social contest code: retire it'); executed elsewhere; roll.py docstring (SC-05, ED-SC-0037, ED-SC-0033) says the kernel is evaluated not deleted and its retirement timing is Jordan's SM-15\] `proposals/2026-09-05-proceedings-subsystem/19_PLAN.md:875` · hook: prize rows 'a standing', 'a proposition', 'a matter' in rosters.yaml contest_subsystems · conf M
  - Measured as 47 files, 1.2 MB with machine-read inbound references in blocking CI gates. Scope ban: the tree is not to be read. Code lane conflict: roll.py SC-05 says KEEP the roll, DO NOT ADOPT the kernel; retirement timing is Jordan's. Disagreement between 19 'ruled retire' and code's 'evaluated, not deleted'.


### L / INTENT

- **CD-053** `INTENT` (+D) — The design in proposals/2026-09-05-proceedings-subsystem (README, 21_RECONCILIATION, 04_VERBS) is ratified as intent; 00-20 stay reference; nothing exists in engine/season except what SC-01/SC-02 built with tests. \[ED-SC-0039 ratified (ED-IN-0286, 2026-10-06): the proceedings subsystem is ratified AS INTENT ONLY\] `registers/editorial_ledger_sc.jsonl:3` · hook: proceedings subsystem · conf H
  - Under CLAUDE.md 0.05 the design is reference, not mechanism. Built: SC-01 (speak, fired slot, provider), SC-03a/b (determine contested, detain/ban), SC-02 22a/23/22b, SC-04 (8 arrangement rows). Residue held.

- **GV-092** `INTENT` (+C) — The orphaned social-contest kernel systems/social_contest/sim/contest/ is not adopted; the interim roll stays; Jordan leans to retire the kernel and have the proceedings subsystem own all social contests; only the timing is asked. \[workplan v10 SC-05, STATE ASK-THEN (timing only); Jordan lean indirect, not a ruling\] `workplans/valoria_master_workplan_v10_part5.md:265` · hook: seam/ladder.py degree_of · conf H
  - parliamentary_vote.py and parliamentary_stay.py already deleted at 29b (PR #450). Quoted lean: 'this subsystem obviously owns all social contests'; 'orphaned social contest code: retire it'. Falsifier: a planted tell contest the old extension demoted.

- **PR-010** `INTENT` (+C) — The ladder rung is no field: a local of the single contest run, the lowest rung any resolved speak Act in this run named; dies with the run at the barrier. \[00 B.2 withdraws the new-field claim; 21 C-2 corrects the fold to be over run's own ACTS (act_of), not emitted matter.* Events\] `proposals/2026-09-05-proceedings-subsystem/00_DERIVATION.md:279` · hook: speak contests: operand; act_of in fold · conf H
  - Five objections killed Tenure.degree as rung home (faction-head strength, non-owner writes, five games with no open_case, two senses, falsifier cannot discriminate). Cost: ladder position does not persist across seasons; only witnessed concessions in ledgers do (P-22). 21 says earlier B.1 table cells were stale.

- **PR-017** `INTENT` (+J) — Witness fan-out moved off 'total' (the echo model Jordan refused, R7: legitimacy falls where the news has reached) to all_five; repair of document_key (R8.4) ordered before the flip. \[21 C-3 ruled; step 2 EXECUTED 2026-09-07 (ED-IN-0205) per 21 text; fixtures.py all_five arm shipped\] `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md:221` · hook: fan_out_mode; channels; document_key; ledger cap · conf M
  - Measured: deposits 649->60, ledgers [200,200,200]->[0,28,32]; ledger cap now evicts nothing. M-6 as specified cannot fail (walks Event.causes, never reads a ledger). total remains H-33 control arm. presence_only loses questions, all_five does not.

- **PR-022** `INTENT` (+C) — Deprivation floor fails: at 1D pool, p_success is 0.2266 at Ob1, 0.0228 at Ob2, 0.0006 at Ob3, 0 at Ob4+; sigma-leverage cannot lift a probability already zero. \[21 PHASE 0 result: M-7 RUN and FAILS; step 14 now 'obstacle needs a ceiling'\] `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md:442` · hook: composed obstacle; p_success; latitude floor · conf M
  - Base_Ob = opposition_score/2 reaches Ob3 before room terms. Remedy (b) obstacle ceiling or a pool floor above 1D; remedy (a) refuted. Pool sweep vs Ob11: pool 9 -> 0.0010, pool 16 -> 0.0753: survivable with a dossier (preparation game), not without. Uses sigma_leverage.p_success (engine/autoload/sigma_leverage.py:246).


### L / PROPOSED

- **CD-109** `PROPOSED` (+D) — Held for Jordan: titles (marquis absent from canon), how far a parliament binds (decline vs breach), who chairs, dice after a carried vote, debate depth. \[PROPOSED (2026-10-29), design only, CR-38's design file; HELD BACK from the merge default: its section 12 calls; sec 12 Jordan's five calls (held back)\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:235` · hook: H-90; CR-34; SC-05 · conf H
  - Canon calls the Crown 'first among equals'. Merging the file does not ratify these. H-90 records Jordan: there is a Parliament, so no monopoly of power in the ruler.

- **OP-055** `PROPOSED` (+D) — The Bout kernel: Standing(Face) 0-10, Reserve 12 with move costs, Room cap 3.0, an upward-only stasis ladder, reception roll pool max(5, 2*faculty+3), plus PersuasionTrack and VoteAtClose win conditions. \[PROPOSED/descriptive of retired-in-waiting Bout kernel (TESTS-ONLY, SM-15 timing Jordan's)\] `proposals/2026-10-22-system-description/2026-10-22-system-description-06-t05-social-contest.md:286` · hook: systems/social_contest/sim/contest (not adopted) · conf H
  - PersuasionTrack = clamp(start + 1.5*(advA-advB), 0, 10): >=9 A_total, >=7 A_decisive, >3 committee, >1 B_decisive. VoteAtClose: each juror votes A iff sharpness*(advA-advB)+noise > 0; Panel sums discipline weight. Faults (barred device, self-contradiction, evasion x2, silence x2) end the bout.

- **OP-100** `PROPOSED` (+D) — F8 re-source (SC-02): option B answered ED-SC-0040: reception and proofs must not read other persons' ledgers inside the fold. \[build instructions under adopted v10 plan (ED-IN-0299), grade paper; SC-02 DESIGN-FIRST\] `proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-13.md:46` · hook: world_q.reception, proofs; ED-SC-0040 · conf H
  - They are to be re-sourced from the commits a bench member made and an opponent can mirror, so the fold asks only the actor's own ledger. CP-T05-01 (opposed term) and CP-T05-02(i) (hearing) wait on this design's approval so they are built once. Layer-1 F8 row: the fold may ask the actor's own ledger and no other.


### L / ARCHIVED

- **GV-043** `ARCHIVED` (+G) — Registry classifying governance types as FLAG (discrete policy choice) or VECTOR (accumulating quantity) across scales, listing Parliament and monarch chain-bypass as flags. \[ARCHIVED; PROPOSED / REFERENCE 2026-07-13\] `.designs/systems/_architecture/reference/governance_type_registry_v1.md:71` · hook: flag vs vector classification · conf M
  - Gives hostage-kin as the canonical flag example. Lists governance-type cascade, independence eligibility, cross-scale claim, chain bypass as flags; consent gate (L/PS) and faction people-held weight as vectors. Flags a naming collision: settlement-derived Mandate meter vs a CI-driven settlement_mgmt parliamentary meter.


### L / NOTCODED

- **GV-060** `NOTCODED` (+D) — The sim modules that implemented Parliamentary Vote and Parliamentary Stay no longer exist; the season loop does not reach the old social-contest kernel. \[code deleted: parliamentary_vote.py and parliamentary_stay.py removed at plan position 29b (FORK:5c5d8ec6 rows)\] `engine/season/requirements.yaml:98` · hook: none (no Parliamentary Vote / Stay verb) · conf H
  - requirements.yaml says the kernel 'exists and already rolls through the substrate' but the loop does NOT reach it; retires at plan position 2-ii. So the Stay, bloc-modifier and Parliamentary Transfer pipeline of the archived docs has no running counterpart.

- **HP-045** `NOTCODED` — Of the arrangement keys (floor, order, records_dissent, interposed, venue_min_rank, bench_basis, disposal_reach), none is read by a runtime outcome-moving module; `disposes` is. \[code check at engine/season (grep of key names outside data/arrangements.py and probes)\] `research/by_lane/SC_social_contest.md:143` · conf M
  - The repo's own SC evaluation says the same. My grep for records_dissent/venue_min_rank/bench_basis/disposal_reach found only the loader and a probe. So historical procedure rows (rank order, dissent record) are data without a reader.

- **OP-021** `NOTCODED` (+D) — A faction-scale parliamentary vote resolver (declarations, ineligibility exclusion, abstention resistance, zero-zero committee, three-way passed/failed/committee band. \[Skeleton described parliamentary_vote.py; I found that file absent from the worktree (systems/social_contest/sim has only contest/)\] `.designs/systems/social_contest/reference/social_contest_flow_skeleton_v1.md:111` · hook: none (retired) · conf M
  - Total Victory Mandate -1) was traced as live in an older tree but is no longer in the tree. Skeleton S8: eligibility by Faction.parliamentary flag, proposer = lowest Stability, establishment = highest Mandate; dice-pool roll over Faction.L/Sta. engine/cross_scale/ (the bridge) and parliamentary_stay.py are also absent now. Design survives only in the archived doc and proposals.

- **PR-102** `NOTCODED` (+B) — The nested run (seam.proceed: ordered attendees, many speeches inside one contest, the rung fold, momentum, order key, <rung kind> reach channel) is NOT built; each docketed speak is a single contested draw. Likewise negotiation/audience/appeal/public-debate rows, aptness and latitude terms, Partial docket write, speaker stance write are absent. \[module docstring says the proceedings nested run is unbuilt; grep for seam.proceed found nothing in engine/season/seam (I opened roll.py and grepped)\] `modules/social_contest/roll.py:41` · hook: seam.proceed; order key; latitude; aptness · conf M
  - The roll docstring: 'The proceedings design's nested run (21 step 15) is not this entry either; it is unbuilt.' So arrangement.order and the ladder descent have no executing consumer; the issue ladder is data only. Treat 05_PROCEDURE and 06's room terms (rung, register, aptness, latitude) as design intent only.


### L / RESEARCH

- **CL-045** `RESEARCH` (+C) — Source-grounding is uneven: 'multilingual' means tradition coverage via mostly English-language scholarship plus a few primary-language academic passes; the doc is a structured secondary-source map, not a reading of primary texts in the original languages. \[RESEARCH; self-disclosed grounding limits (lines 41-63)\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:41` · conf H
  - Tiers [PR]/[REF]/[PRIM]/[TER] in section 11.5. Several attributions flagged: Cicero titles and ethopoeia UNVERIFIED, deliberative final headings LOW, ars arengandi MEDIUM, Guiguzi dating MEDIUM, du Rosier priority MEDIUM, ten-orator canon MEDIUM/LOW.

- **CL-073** `RESEARCH` (+C) — Source-tier rules: doc 4 retracts doc 3's warrant x attack matrix as fabricated ('invented rather than derived'); doc 5 puts TIER-FLOOR T2 on its Chinese material. Nothing in sources/ may be cited as a ratified rule. \[SOURCE MATERIAL README, ED-SC-0025; retraction recorded\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/README.md:27` · conf H
  - Fork B (ED-SC-0021) and CIP-2 had endorsed the matrix before doc 4 existed. Chinese techniques may be adopted as design on merits but not cited as historically grounded. Re-distillation: 20 N-primitives collapse to 5 mechanisms (README line 41).

- **HP-107** `RESEARCH` (+D) — Only the vendored study's gate half (concession ladder, genres, interposition kinds, proofs, dissent record) reached code as loaded data; RHET, SC-SRC primitives and governance patterns reach no owner code. \[FILED 2026-10-16 critical evaluation; reference\] `research/by_lane/SC_social_contest.md:80` · conf M
  - Evaluation also says governance research reached the season loop once, as hole row H-100, and that its verifier corrections are not reliably applied (notes cut mid-sentence). Treat the governance hooks as unadopted proposals.

- **OP-087** `RESEARCH` (+C) — Verdict: the social contest was three resolution models under one name: A the canonical prose (no engine), B the promoted Bout kernel (good, absent from the canonical head). \[RESEARCH audit report (PROPOSED, ED-SC-0017..22; 2026-08-06, pre-dates SC-05 adoption decision)\] `.audit/2026-08-06-social-contest-three-lens-audit/00_synthesis.md:12` · hook: build_contest; Bout; scene_dispatch (old) · conf H
  - C the deprecated legacy stub; the live campaign ran the one nobody designed. Gate-C items (armature, CR4 bonus, CR5 backfire) unreachable because build_contest had no armature parameter; live path ran logos_spammer vs logos_spammer. Every wired output was a stat delta, contradicting the doc's 'not just a stat change'.

- **OP-090** `RESEARCH` (+B) — A mechanism is code that branches; a configuration is a row in a table: all eight proceedings had already collapsed to PROCEEDINGS rows. \[RESEARCH audit finding\] `.audit/2026-08-06-social-contest-three-lens-audit/00_synthesis.md:201` · hook: modes.PROCEEDINGS · conf H
  - (Excommunication Tribunal differs from Church Tribunal in track start, budget and a corroboration flag), so roughly 300+ of the canonical head's 724 lines are special-casing and the cut list totals about 800 lines.

- **OP-095** `RESEARCH` (+H,G) — Interface finding: no settlement-scale contest mechanic existed; Settlement Revolt and Stability Crisis were named Mandatory Zoom-In triggers (negotiate with the populace as a social contest. \[RESEARCH informational review FILED 2026-07-08; advisory only\] `.audit/2026-07-08-contest-settlement-faction-interface/interface_report_v1.md:146` · hook: zoom-in triggers 4.3.2; Domain Echo; ED-SC-0002 · conf H
  - Emergency faction council) but the revolt trigger was never evaluated and settlement governance disputes (Hold Court, Treat, Bargain, Recall) were an unratified proposal blocked on the settlement registry. Declared consequences (Mandate shifts, faction splits, settlement-targeted Obligations, Accord echoes) almost none executed. The one live path (Stability Crisis) resolved a verdict then discarded it.

- **PR-103** `RESEARCH` (+I) — Stress suite of 38 attempts to run a proceeding against the tracer: 4 things executed (speak by a seatless person, appeal depth cap returns ContestError, seeded replay, attendee insertion order permuted); blockers shared across all twelve rows (arrangement loader, docket, bench, disposal writer) - 'no arrangement row is blocked on a parameter of its own'. \[20 PROPOSED then partly closed by 21; harness stress/stress_proceedings.py executes against proposals/2026-09-01-season-loop-tests/tracer/shape.py (an older tracer), re-hosted later in engine/season/tests/test_stress_proceedings_rehost.py\] `proposals/2026-09-05-proceedings-subsystem/20_STRESS_TESTS.md:81` · hook: stress/stress_proceedings.py; results.json · conf H
  - Worked trial of 16 steps: 5 supplied (all pre-existing), 10 stop, 1 ambiguous. 21 B.5 overturns three headline claims (ST-09 ran the live row; ST-35 replayed no draw; ST-36 permuted insertion order not attendance). Findings F-32, F-34 withdrawn; F-14 downgraded; F-05 re-cut to UNKNOWN reader.


