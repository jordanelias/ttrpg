# Verbs and attributes — what the acts of the game ask of a character

## Status: PROPOSED (2026-09-30) · design-only · ratifies nothing on merge · reference under `CLAUDE.md` §0.05
## Lane: IN, with PC, SC, FI · IDs: none allocated
## Read at HEAD `c8cc408`: `engine/season/verb_table.yaml` (44 rows), `architecture/ARCHITECTURE_V2.md` §E3–E4, `references/descriptor_registry.yaml`, and the held-back `proposals/2026-09-05-proceedings-subsystem/04_VERBS.md`.
## Builds on: `proposals/2026-08-15-character-and-faction-stats-and-progression.md` §10, §13, §15 (held for Jordan).
## Suite: [README](README.md) · [09 the character sheet](09_the_character_sheet.md) · **10 verbs and attributes**

**The question, in Jordan's words from the session:** which attributes make sense once the verbs are
sorted thematically — with *"the context in which they exist in game world with narrative
implications"*, *"the other subsystems [that] may call for [them] that aren't built yet"*, and *"the
word definitions and etymologies themselves."*

**Answer.** Sort the verbs by what they *draw*, not by theme. Three of the 44 contest today, and the
held-back proceedings design would add six; only those have work for an attribute, and in every engine
that is built the attribute reaches them through a faculty, never as dice of its own. The thematic sort
given in the session assigned attributes to verbs that never roll; §2.2 withdraws that part.

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

Read from each row's `eligibility`, `writes` and `emits`:

| family | verbs | what they do | eligible through |
|---|---|---|---|
| **force** | fight, march, move, migrate | contest a body or a field; change where a person is, or where they live | `own`; `march` through `remit:dispatch` |
| **seats** | confer, revoke, convene, dispatch, issue, determine, establish, levy, open_case | an office's remit exercised | a `remit:` |
| **bonds** | commit, repudiate, oblige, tie / knot, release, succeed, give | open, close or hand over a tenure | `own`, with `hold:` for `give` |
| **answers to a decree** | comply, evade / defy, construe | fulfil a dispensation, withhold compliance, or read its terms | `own` |
| **word and suit** | utter, speak, tell, petition, carry | make a proposition, speak, pass on a claim, ask, carry a petition | `own` |
| **record and inquiry** | create_record, destroy_record, forge, survey; examine, interview, research, surveil, thread_read, reconstruct | make, destroy, falsify or mint a record; the six inquiries each deposit a `finding.made` claim in the actor's own ledger | `own`; four inquiries also need presence at a site or rung |
| **material and works** | work, restore, transfer, exchange, found, build | wear and repair sites, move stores, found a rung, raise a site | `own`, with presence or a hold for three |

One fact bears on everything below. §E4 states the table's first property — *"capability gates no
verb … Rank supplies dice at the seam and appears in no row"*; *"an office adds no verb and no
modifier."*

### 1.3 Draw — the reading that decides the attribute question

A verb either contests a prize or succeeds or is refused on eligibility and precondition. **Three
contest today:**

| verb | contests | resolved by | where aptitude enters |
|---|---|---|---|
| `fight` | the body | `combat_engine_v1` | attributes govern per-beat faculties; the pool is `max(5, History + 6)` with no attribute in it (ED-901) |
| `march` | a field | `resolve_field` | nowhere on the season path — `_weighted_unit` fixes power at 4 and morale at 5 ([08](08_mass_battle_units.md)) |
| `tell` | a standing | the σ-leverage provider | the capability key `copying` (`rosters.yaml: verb_capability`), empty for most persons |

**Six more would contest under the held-back proceedings design** (`04_VERBS.md` §B.1, §B.3.2), each
with a prize of its own:

| verb | proposed prize |
|---|---|
| `speak` | a matter — the whole proceeding, handed to the seam as one act |
| `examine` | what persists |
| `interview` | a disposition (against obstinacy) |
| `research` | what the record holds |
| `reconstruct` | what can be inferred |
| `surveil` | what is done unseen |

`thread_read` is deliberately left unwritten there, because its obstacle belongs to a rendering layer
nobody has derived (`P-19`, graded `absent`).

This is the whole of the attribute question's scope. The August census reached the same place from the
resolvers: *"attributes are absent from resolution in every finished engine"* and *"every engine
consumes blends, never a bare attribute"* (its T1 and T5). An attribute has work only where a verb
contests, and there only through a faculty; a verb that never contests needs none.

### 1.4 Etymology — where the words confirm the design, and where they break it

Settled lexicography, read against the rows:

| verb | root | what it shows |
|---|---|---|
| **evade / defy** | Latin *evadere*, "to go out, slip away" · Old French *desfier*, "to renounce pledged faith" | **opposite postures in one row.** Both emit `compliance.withheld`, so a witness learns that compliance was withheld and cannot learn whether it was dodged or refused — the difference between a subject who slipped the order and one who declared against it |
| construe | *construere*, "to pile together, to build" | a reading assembled from an instrument's terms. The row's `naming_note` keeps `terms.distorted` on purpose: the premise is refracted *by* the act of construing, "two names for two things". `reconstruct` shares the root |
| oblige · tie / knot | *ob-* + *ligare*, "to bind to" | the root of *ligament*. The engine agrees that these are one act in two registers: `oblige` opens a tenure to a seat, with a term; `tie / knot` opens a bond, stored once between its two parties |
| confer · levy | *conferre*, "to bring together", whence both "to consult" and "to bestow" · *levare*, "to raise" | `confer` uses the second sense — it seats a person in an office. The two are a seat's bestowal and a seat's extraction |
| give | Old English *giefan* | a handover of what the actor holds — the giver's `hold` closes and the receiver's opens in one effect — where `confer` bestows what an office controls |
| found · build | *fundare*, "to lay the bottom", from *fundus* · Old English *byldan*, "to make a dwelling" | `found` lays a rung and `build` raises a site; both require the actor to hold a works |
| survey · surveil | Anglo-French *surveier*, from *super* + *videre*, "to see over" · French *surveiller*, from *vigilare*, "to keep watch" | near-synonyms in English, different acts here: `survey` mints a faction sheet into the surveyor's hand; `surveil` watches a place. The roots separate them correctly; a cold reader will not |
| migrate · move | *migrare*, "to change one's abode" | the rows agree: both relocate, and only `migrate` also closes one `reside` edge and opens another |
| utter | Middle English *uttren*, "to put out, make outward" | the act that makes a proposition exist at all: the only row that writes `Proposition.exists`, and what it makes is immutable (`commit`'s cell, §14) |
| tell | Old English *tellan*, "to count, to relate" | the claim field `teller` keeps the second sense: who related it |
| examine | *examinare*, from *examen*, the tongue of a balance | to weigh; the act weighs a site's evidence, and `interview` is the one that questions a person |
| forge | via Old French *forgier*, from *fabricare* (*faber*, smith) | to shape and to counterfeit; the row writes `Record.forgery_quality` |

**One collision.** `construe` names two things: the §E3 verb (renamed from `refract`, Jordan
2026-09-18) and, in the proceedings design, a member of the proposed `speech_kinds` roster — the move
apt at the *quality* rung, where `refute` is apt at *conjecture* (`04_VERBS.md` §B.1.1). The senses are
cognate, but these are two objects under one name, which is what `CLAUDE.md` §4 exists to stop.

### 1.5 The verbs still to come

The proceedings design adds **no** verb — *"NO NEW ACT IS INVENTED"*: nineteen verbs reach a
proceeding, every name already in the tree, `speak` becomes the contest, and what a speaker does is a **speech kind** in a closed data
set (propose, concede, refute, define, construe, amplify, object, impugn, pre-empt, recapitulate),
weighed by aptness rather than by coefficient. That meets the precedent survey's constraint on a
social contest by construction: manoeuvres *"must differ in what they change about the state of the
argument, not in how much they subtract"* (`research/…_part3.md` §7.10), and the roster is keyed on
*what the move does to the matter*.

The other unbuilt calls are **threadwork operations**, typed by scale, which will draw on the
substrate; and `thread_read` itself, which waits on a derivation (§1.3).

---

## 2. What attributes follow

### 2.1 One domain per family of prize

| domain | verbs that draw | how aptitude enters today | attributes the designs name |
|---|---|---|---|
| **arms** | fight | per-beat faculties: impact, handling, tempo, balance, reading, reflex, durability, action economy, steadiness | Strength, Agility, Endurance, Acuity (as Cognition), Attunement, Will (as Spirit), Focus — August §10.1 |
| **command** | march | season path: none. Mass-battle engine: `command = ⌈(2·Charisma + Cognition) / 3⌉` on an `Officer` | Charisma, Acuity |
| **standing and the matter** | tell; speak, proposed | the capability key `copying`; the retiring kernel's abstract `faculty` | **none bound.** The kernel refuses attributes; in it, Charisma appears only as a derived ceiling, `Face_max = Cha × 3` |
| **inquiry** | examine, interview, research, surveil, reconstruct, proposed | nothing resolves them | the fieldwork design (§4.2): Cognition for examine and surveil, Attunement for interview, **Recall** for research and reconstruct |
| **substrate** | thread_read; threadwork operations | Thread Sensitivity ≥ 30, an untyped gate | Spirit × 2 + History + TPS (fieldwork §4.2; threadwork) |

Every other family — seats, bonds, answers to a decree, word and suit, record, material — needs **no**
attribute. Its acts turn on remits, holdings and presence, and §E4 forbids either an office or
capability to modify one.

**Recall has no name in the registry.** The descriptor registry lists nine attributes and leaves the
tenth unnamed, and it neither lists nor aliases Recall; the fieldwork design still makes it primary for
two inquiries, and the August census classes it as *"CAPACITY, not attribute — equip slots + learning
rate; never rolled."* That is evidence for D2, not a candidate for it.

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
owner for the aptitude slot, and the prizes enumerate its domains. Two cautions from its own later
sections bind whoever builds it:

1. Its thesis — *"an attribute dependency is what a subsystem has instead of an acquisition layer"* —
   is, by its own account, *"an inference, not a measurement, and … falsifiable exactly once"*
   (§15.8).
2. Its first test design **failed structurally** because the policy layer could not see the
   acquisition layer, so *"all 11 policies play identically with or without a school"* (§13.1). The
   season loop has the same shape today: nothing under `engine/season/decision/` reads `capability`
   except to state that it gates nothing. An acquisition layer the chooser cannot see is purchasable,
   not playable.

---

## 3. Recommendations

| # | recommendation | where | observable (falsifier) | cost | gate |
|---|---|---|---|---|---|
| **V-1** | Split `evade / defy` into two rows with distinct emits, so a witness can tell avoidance from declared refusal. ED-FI-0009's split of *"the six investigation acts"* is the precedent. | `verb_table.yaml`; `ARCHITECTURE_V2.md` §E3 | a witness's claim distinguishes the two acts; no other behaviour changes while neither contests | small | **Jordan** — it amends a ratified §E3 row |
| **V-2** | An attribute reaches a verb only through a faculty, and only if the verb's row has `contests:`. Record `contests:` for every new verb as the deciding column. | resolvers; `verb_table.yaml` | no resolver reached from a row without `contests:` reads an attribute | — | standing rule, from §E4 and T5 |
| **V-3** | Adopt `faculty(domain)` as the single owner of the aptitude slot, with the domains named by the prizes: arms, command, standing and the matter, inquiry, substrate. | the resolvers' pool formulas | every pool reads `faculty(domain)`; none reads a bare attribute | medium | PC, SC, FI |
| **V-4** | Before D2 is ruled, build one non-combat acquisition layer and see which attributes it still needs — the August sequence, relocated to the proceedings design, since the contest kernel it named retires at `2-ii`. Satisfy §13.1 first: the chooser must see the person's own kit. | `proposals/2026-09-05-proceedings-subsystem/`; `decision/` | two persons differing only in an acquired technique choose differently in the same situation | medium | SC, when un-held |
| **V-5** | Keep verb names idempotent in meaning (`CLAUDE.md` §4): gloss `survey` and `surveil` at their rows by their roots — to see over, to keep watch — now; and when the proceedings design is taken up, give the speech kind a name other than `construe`, or make it the same object as the verb. | `verb_table.yaml` notes; `04_VERBS.md` §B.1.1 | — | trivial | gloss buildable now; speech kind with the proceedings design |

**For Jordan:** V-1, because it amends ratified canon. The roster (OPT-AV-1; the plan's D2, which the
plan records as *"inert for `engine/season`"*) remains his; §2.1 and the Recall finding are evidence for
it.
