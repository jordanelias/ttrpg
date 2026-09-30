# Verbs and attributes — what the acts of the game ask of a character

## Status: PROPOSED (2026-09-30) · design-only · ratifies nothing on merge · reference under `CLAUDE.md` §0.05
## Lane: IN, with PC, SC, FI · IDs: none allocated
## Read at HEAD `c8cc408`: `engine/season/verb_table.yaml` (44 rows), `architecture/ARCHITECTURE_V2.md` §E3–E4, `references/descriptor_registry.yaml`, and the held-back `proposals/2026-09-05-proceedings-subsystem/04_VERBS.md`.
## Builds on: `proposals/2026-08-15-character-and-faction-stats-and-progression.md` §10, §13, §15, §20 (held for Jordan).
## Suite: [README](README.md) · [09 the character sheet](09_the_character_sheet.md) · **10 verbs and attributes**

**The question, in Jordan's words from the session:** which attributes make sense once the verbs are
sorted thematically — with *"the context in which they exist in game world with narrative
implications"*, *"the other subsystems [that] may call for [them] that aren't built yet"*, and *"the
word definitions and etymologies themselves."*

**Answer.** Sort the verbs by what they *draw*, not by theme. Three of the 44 contest today, and the
proceedings design (partly built, its proposal held back) would add seven; only those have work for an attribute, and in every
engine that is built the attribute reaches them through a faculty, never as dice of its own. The
thematic sort given in the session assigned attributes to verbs that never roll; §2.2 withdraws that
part.

---

## 1. Four readings of one table

### 1.1 Stratum — an ordering band, not a meaning

| stratum | rows |
|---|---|
| social | 15 — carry, commit, comply, construe, evade / defy, give, interview, oblige, open_case, petition, repudiate, speak, tell, tie / knot, utter |
| uncontested_material | 13 — build, create_record, destroy_record, exchange, forge, found, levy, reconstruct, research, restore, survey, transfer, work |
| binding_decision | 9 — confer, convene, determine, dispatch, establish, issue, release, revoke, succeed |
| contested_physical | 5 — examine, fight, march, surveil, thread_read |
| movement | 2 — migrate, move |

The table says what a stratum is: *"a RESOLUTION-ORDER band over what an act touches, and [it is] not
the `contests:` column"* (`examine`'s `stratum_note`). So `examine` and `surveil` sit beside `fight`
because they touch the physical world, not because they are risky or contested; the six inquiries were
split three ways on exactly that basis — the physical world, a conversation, the actor's own evidence.

### 1.2 Function — what the act does in the world, and how a person becomes eligible for it

Read from each row's `eligibility`, `writes` and `emits`. Eligibility is a **disjunction**, and `own`
admits on its own (`loop/resolve.py::_eligible`), so the column that separates the families is the
remit; presence enters through preconditions (`examine`, `surveil` and `restore` require the actor on
the spot).

| family | verbs | what they do | eligible through |
|---|---|---|---|
| **force** | fight, march, move, migrate | contest a body or a field; change where a person is, or where they live | `own`; `march` only through `remit:dispatch` |
| **seats** | confer, revoke, convene, dispatch, issue, determine, establish, levy, open_case | an office's remit exercised | a `remit:` |
| **bonds** | commit, repudiate, oblige, tie / knot, release, succeed, give | open, close or hand over a tenure | `own` |
| **answers to a decree** | comply, evade / defy, construe | fulfil a dispensation, withhold compliance, or read its terms — **none of the three executes today**: none is in `driver.resolvable_verbs()` | `own` |
| **word and suit** | utter, speak, tell, petition, carry | make a proposition, speak, pass on a claim, ask, carry a petition | `own` |
| **record and inquiry** | create_record, destroy_record, forge, survey; examine, interview, research, surveil, thread_read, reconstruct | make, destroy, falsify or mint a record; the six inquiries each deposit a `finding.made` claim in the actor's own ledger | `own`, except `destroy_record` (`hold:` or `presence`) |
| **material and works** | work, restore, transfer, exchange, found, build | wear and repair sites, move stores, found a rung, raise a site | `own` |

One fact bears on everything below. §E4 states the table's first property — *"capability gates no
verb … Rank supplies dice at the seam and appears in no row"*; *"an office adds no verb and no
modifier."*

### 1.3 Draw — the reading that decides the attribute question

A verb either contests a prize or succeeds or is refused on eligibility and precondition. **Three
contest today:**

| verb | contests | resolved by | where aptitude enters |
|---|---|---|---|
| `fight` | the body | `combat_engine_v1` | in the engine, attributes govern per-beat faculties and the pool is `max(5, History + 6)` with no attribute in it (ED-901); on the season path every attribute but `end` is a class default ([09](09_the_character_sheet.md) §1.3) |
| `march` | a field | `resolve_field` | nowhere on the season path — `_weighted_unit` fixes power at 4 and morale at 5 ([08](08_mass_battle_units.md)) |
| `tell` | a standing | the σ-leverage provider | the capability key `copying` (`rosters.yaml: verb_capability`), empty for most persons |

**Seven more would contest under the proceedings design** (`04_VERBS.md` §B.1, §B.2, §B.3.2). Its
proposal is held back, and the build is partial: plan position `22` has steps 6, 7, 9 and 10 done and
the contest-resolution core, steps 11–16, open. None of these verbs contests yet:

| verb | proposed prize |
|---|---|
| `speak` | a matter — the whole proceeding, handed to the seam as one act |
| `determine` | declared contested, with degree-keyed writes and emits; no prize string is written |
| `examine` | what persists |
| `interview` | a disposition (against obstinacy) |
| `research` | what the record holds |
| `reconstruct` | what can be inferred |
| `surveil` | what is done unseen |

`thread_read` is deliberately left unwritten there, because its obstacle belongs to a rendering layer
*"this proposal has not derived"* (`P-19`, graded `absent`).

This is the whole of the attribute question's scope. The August census reached the same place from the
resolvers: *"attributes are absent from resolution in every finished engine"* and *"every engine
consumes blends, never a bare attribute"* (its T1 and T5). An attribute has work only where a verb
contests, and there only through a faculty; a verb that never contests needs none.

### 1.4 Etymology — where the words confirm the design, and where they break it

Settled lexicography, read against the rows:

| verb | root | what it shows |
|---|---|---|
| **evade / defy** | Latin *evadere*, "to go out, slip away" · Old French *desfier*, "to renounce pledged faith" | **opposite postures in one row.** The row emits one kind, `compliance.withheld`, so were it to execute a witness would learn that compliance was withheld and never whether it was dodged or refused — the difference between a subject who slipped the order and one who declared against it |
| construe | *construere*, "to pile together, to build" | a reading assembled from an instrument's terms. The row's `naming_note` keeps `terms.distorted` on purpose: the premise is refracted *by* the act of construing, "two names for two things". `reconstruct` shares the root |
| oblige · tie / knot | *ob-* + *ligare*, "to bind to" (the root of *ligament*) · Old English *tīgan* and *cnotta*, Germanic | different roots, one sense — to bind — and the engine agrees that these are one act in two registers: `oblige` opens a tenure to a seat, with a term; `tie / knot` opens a bond, stored once between its two parties |
| confer · levy | *conferre*, "to bring together", whence both "to consult" and "to bestow" · *levare*, "to raise" | `confer` uses the second sense — it seats a person in an office. The two are a seat's bestowal and a seat's extraction |
| give | Old Norse *gefa*, which displaced Old English *giefan* | a handover of what the actor holds — the giver's `hold` closes and the receiver's opens in one effect — where `confer` bestows what an office controls |
| found · build | *fundare*, "to lay the bottom", from *fundus* · Old English *byldan*, "to make a dwelling" | `found` lays a rung and `build` raises a site; both require the actor to hold a works |
| survey · surveil | Anglo-French *surveier*, from *super* + *videre*, "to see over" · French *surveiller*, from *vigilare*, "to keep watch" | near-synonyms in English, different acts here: `survey` mints a faction sheet into the surveyor's hand; `surveil` watches a place. The roots separate them correctly; a cold reader will not |
| migrate · move | *migrare*, "to change one's abode" | the rows agree: both relocate, and only `migrate` also closes one `reside` edge and opens another |
| utter | Middle English *uttren*, "to put out, make outward" | the act that makes a proposition exist at all: the only row that writes `Proposition.exists`, and what it makes is immutable (`commit`'s cell, §14) |
| tell | Old English *tellan*, "to count, to relate" | the claim field `teller` keeps the second sense: who related it |
| examine | *examinare*, from *examen*, the tongue of a balance | to weigh; the act weighs a site's evidence, and `interview` is the one that questions a person |
| forge | via Old French *forgier*, from *fabricare* (*faber*, smith) | to shape and to counterfeit; the row writes `Record.forgery_quality` |

**One latent collision.** The proceedings design's ten speech kinds include `construe` — the move apt
at the *quality* rung, where `refute` is apt at *conjecture* (`04_VERBS.md` §B.1.1) — and the §E3 verb
formerly `refract` took the same name on 2026-09-18. The live roster does not collide: `arrangements.yaml`
carries six kinds, the forensic ladder (`deny`, `cite_incompatible`, `impugn_motive`, `concede_fact`,
`concede_harm`, `hand_error_back`), and `construe` is not among them. Rostering the design's remaining
kinds under their written names would put two objects under one name, which is what `CLAUDE.md` §4
exists to stop.

### 1.5 The verbs still to come

The proceedings design adds **no** verb — *"NO NEW ACT IS INVENTED"*: every verb it uses is already
in the tree, `speak` becomes the contest, and what a speaker does is a **speech kind** in a closed data
set, weighed by aptness rather than by coefficient. The design names ten kinds (propose, concede,
refute, define, construe, amplify, object, impugn, pre-empt, recapitulate); the live roster is a
different six, the forensic ladder, which its own comment calls *"SIX OF TEN, NAMED SCOPE-DOWN"*
(§1.4). The design meets the precedent survey's constraint on a social contest by construction: manoeuvres *"must differ in what they change about the state of the
argument, not in how much they subtract"* (`research/…_part3.md` §7.10), and the roster is keyed on
*what the move does to the matter*.

The other unbuilt calls are **threadwork operations**, typed by scale, which will draw on the
substrate; and `thread_read` itself, which waits on a derivation (§1.3).

---

## 2. What attributes follow

### 2.1 One domain per family of prize

| domain | verbs that draw | how aptitude enters today | attributes the designs name |
|---|---|---|---|
| **arms** | fight | in the engine, per-beat faculties: impact, handling, tempo, balance, reading, reflex, durability, action economy, steadiness. On the season path, class defaults but `end` | Strength, Agility, Endurance, Acuity (as Cognition), Attunement, Will (as Spirit), Focus — August §10.1 |
| **command** | march | season path: none. Mass-battle engine: `command = round((2·Charisma + Cognition) / 3)`, clamped to 1–7, on an `Officer` or the general's `Unit` when both are set (`derive_command`) | Charisma, Acuity |
| **standing and the matter** | tell; speak and determine, proposed | the capability key `copying`; the retiring kernel's abstract `faculty` | **none bound.** The kernel refuses attributes; in it, Charisma appears only as a derived ceiling, `Face_max = Cha × 3` |
| **inquiry** | examine, interview, research, surveil, reconstruct, proposed | nothing resolves them | the fieldwork design (§4.2): Cognition for examine and surveil, Attunement for interview, **Recall** for research and reconstruct |
| **substrate** | thread_read; threadwork operations | Thread Sensitivity ≥ 30, an untyped gate | Spirit × 2 + History + TPS (fieldwork §4.2; threadwork) |

Every verb not in this table needs **no** attribute: all of the seats, bonds, answers to a decree and
material, and the rest of word and suit and of record. Those acts turn on remits, holdings and
presence; §E4 bars capability from gating any verb and an office from adding a modifier.

**Recall has no name in the registry.** The descriptor registry lists nine attributes and leaves the
tenth unnamed, and it neither lists nor aliases Recall; the fieldwork design still makes it primary for
two inquiries, and the August census classes it as *"CAPACITY, not attribute — equip slots + learning
rate; never rolled."* The August proposal's own §20.1 records the same gap. It is evidence for D2,
not a candidate for it.

### 2.2 What this corrects in the session's own sort

The session sorted the verbs into four themes — body; mind and perception; presence and authority;
voice and relation — with a fifth stratum, craft, left to the generic `capability`. Three assignments
in it do not survive the rows:

- **Presence and authority for `confer` and `levy`.** Seat acts are eligible through a remit and take
  no modifier (§E4). No attribute can reach them.
- **Disposition for `comply`, `oblige`, `repudiate`, `evade / defy`.** None of them contests. Whether a
  person yields is `choose`'s question, answered from pursuits and stance, not a roll.
- **Coherence for `tie / knot`.** The row has no precondition and no draw.

What survives is the mapping of themes onto prizes: body to arms, mind and perception to inquiry,
presence and authority to command — reachable only through `march` — and voice and relation to standing
and the matter. The craft point stands unchanged.

### 2.3 How this meets the August proposal

The August proposal's `faculty(domain) = f(governing aptitudes, practice in that domain)` is the right
owner for the aptitude slot, and the prizes enumerate its domains. Three cautions from its own later
sections bind whoever builds it:

1. Its thesis — *"an attribute dependency is what a subsystem has instead of an acquisition layer"* —
   is, by its own account, *"an inference, not a measurement, and … falsifiable exactly once"*
   (§15.8). And its prediction that the roster would shrink is **withdrawn** (§20.1): Jordan ruled
   the count at ten on 2026-08-14 (ED-IN-0193), so the open work is naming the tenth (D2), not sizing
   the roster.
2. Its first test design **failed structurally** because the policy layer could not see the
   acquisition layer, so *"all 11 policies play identically with or without a school"* (§13.1). The
   season loop has the same shape today: nothing under `engine/season/decision/` reads `capability`
   except to state that it gates nothing. An acquisition layer the chooser cannot see is purchasable,
   not playable.

---

## 3. Recommendations

| # | recommendation | where | observable (falsifier) | cost | gate |
|---|---|---|---|---|---|
| **V-1** | Carry the `evade / defy` split into ED-IN-0210, which already asks Jordan whether `comply` is one verb or two: the row joins opposite postures under one emit, and ED-FI-0009's split of *"the six investigation acts"* is the precedent for splitting a combined row. | `verb_table.yaml`; `ARCHITECTURE_V2.md` §E3 | once the family executes (none of the three does today), a witness's claim distinguishes the two acts | small | **Jordan, inside ED-IN-0210** (open; blocks `19b`) |
| **V-2** | An attribute reaches a verb only through a faculty, and only if the verb's row has `contests:`. Record `contests:` for every new verb as the deciding column. | resolvers; `verb_table.yaml` | no resolver reached from a row without `contests:` reads an attribute | — | standing rule, from §E4 and T5 |
| **V-3** | Adopt `faculty(domain)` as the single owner of the aptitude slot, with the domains named by the prizes: arms, command, standing and the matter, inquiry, substrate. | the resolvers' pool formulas | every pool reads `faculty(domain)`; none reads a bare attribute | medium | PC, SC, FI |
| **V-4** | Build one non-combat acquisition layer — in the proceedings design, since the contest kernel the August proposal named retires at `2-ii` — and let the aptitude it still cannot serve inform D2. Satisfy §13.1 first: the chooser must see the person's own kit. | `proposals/2026-09-05-proceedings-subsystem/`; `decision/` | two persons differing only in an acquired technique choose differently in the same situation | medium | SC, when un-held |
| **V-5** | Keep verb names idempotent in meaning (`CLAUDE.md` §4): gloss `survey` and `surveil` at their rows by their roots — to see over, to keep watch — now; and if the design's remaining speech kinds are rostered, name that one something other than `construe`, or make it the same object as the verb. | `verb_table.yaml` notes; `arrangements.yaml: speech_kinds` | — | trivial | gloss buildable now; speech kind when rostered |

**For Jordan:** nothing new. V-1 is evidence for ED-IN-0210, already his. The count of attributes is
ruled at ten (ED-IN-0193, which settled OPT-AV-1); naming the tenth — the plan's D2, which it records
as *"inert for `engine/season`"* — remains his, and §2.1 and the Recall finding are evidence for it.
