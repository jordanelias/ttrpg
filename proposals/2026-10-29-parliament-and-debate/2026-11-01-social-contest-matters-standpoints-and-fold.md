# Social contest: where its matters come from, how standpoints arise, and how its decisions rejoin the season

## Status: PROPOSED (reference; resolves nothing, schedules nothing)

> **Asked (follow-up to PR #542):** *"elaborate upon how worldly matters are pulled into engine, and expand upon all
> matters that can be discussed in the subsystem. explain how different standpoints can occur, then explain how
> decisions from this engine will be folded into season loop."*

`[ASSUMPTION: "the subsystem" is the social-contest subsystem and "worldly matters" are R-26's "worldly topics"; basis:
PR #542's subject and R-26's wording]`

This is the companion to Proposal 4 (`2026-11-01-social-contest-proposal-4-authority-staged.md`, **P4**) and to the
comparison (`2026-10-30-social-contest-proposals-comparison.md`, §9). **Its three parts are armature, not proposal.**
Intake, standpoints and the fold are what any of the four proposals would sit on; §6 says where a proposal changes a
row. Rulings `R-1..R-41` and `S-1..S-8` are cited from `2026-10-30-social-contest-primitives-and-kinds.md` §1 and
outrank everything here. Canadian spelling.

**Evidence.** Code in `engine/season/` was read on this checkout (`eaf4c9b`), each cited line opened. Figures marked **probe**
come from three read-only scripts in this folder, `probe_matters_intake.py`, `probe_event_kinds.py` and `probe_controls.py`,
whose outputs sit beside them (`2026-11-01-probe-matters-intake-seed0.json`, `2026-11-01-probe-event-kinds-seed0.json`
and `-seed1.json`, `2026-11-01-probe-controls-seed0.json`). Each builds the realm for one seed, runs four seasons with the
shipped chooser, and writes nothing in the tree. The third was written after a critic pass to test four claims of the
first two (marked **control** below); the committed event-kinds script reproduces its committed seed-0 output exactly. **Nothing
was run with a proposal built, because none is built.** Statuses use P4 §8's words: **FIRES** (fires in computed
play), **NEVER** (exists; not observed in the probe's two seeds of four seasons, or never per the cited source), **ABSENT** (does not exist). A zero in a short run is not a proof of impossibility; no minimum latency is established for petition, carry, case, Date and determination.

---

## 1. The result

1. **No act fetches a matter.** The contest module is World-free and the chooser reads only its own person.
   `questions_for`, which does read the World, builds each person's Questions: mostly by one pipe (an Event is
   witnessed, a claim lands in a holder's own ledger, a Question follows) and, at three entry points, directly from
   World state (vacant offices, the docket, sittings). Only he may form an act on the Question. Two stores feed it,
   **what he has been told or seen** (the ledger) and **what he holds, owes or has committed to** (his edges). Seven
   entry points lead from those stores to a question (§2.2).
2. **The world pours in; matter-shaped content does not.** Over four seasons at seed 0 the shipped chooser's persons
   held 15,600 claims and faced 15,642 `claim_landed` questions against 495 `need` questions. Of the 261 Propositions
   in that world, 258 are OUGHT and 3 are HOLDS, so a past fact in dispute has almost no carrier in computed play. 28
   items sat on the docket, 18 of them empty sitting slots, and none of the 10 that held a matter named the arrangement
   row it is heard under (§2.3).
3. **Seventeen families of matter can be discussed** (§3.3), a sorting by what the disposal writes and not a proof of
   completeness. Each reduces to *a person-party and a thing someone can lose*. Families 1 to 3, 7, 11, 12 and 15 end
   in something that a `determine` or a witnessed claim writes today, though a computed case disposes only `oblige`
   because it names no arrangement row. Families 4, 5, 6, 9, 13 and the appeal half of 14 are blocked on a site or
   conjunct that does not exist (a `hold` transfer, a `resolution` licence, a consent conjunct, a computed `give`, an
   appeal closure). Families 8, 10, 16 and 17 have an owner verb that executes (or none) and no contest producer.
4. **A standpoint is computed, never stored** (R-20, S-7). It is a person's claims about the object, his edges to it,
   his dispositions, his role in the occasion, his authority and his capability, each read from his own interior.
   Eight sources make two persons differ on one matter (§4.2). At seed 0 the 78 persons alive at the end split in sign on
   their opinion of Hafenmark 39 to 39, and (positive to negative) of the Guilds 20 to 58 and the Crown 61 to 17; **the
   same spread stood at tick 0** (Hafenmark 43 to 40, Guilds 20 to 63), so it comes from the build, not from four seasons
   of play (**control**).
5. **A decision rejoins the season as a witnessed fact, never as a number pushed at anyone** (S-3, S-6, S-7). A
   contest outcome is a degree on the one ladder; the verb row's band says what is written; the gate writes it; the
   Event is witnessed; every standpoint receives it through its own channel and refraction. Six return routes carry it
   back into later questions (§5.5). **In the probe only the first of the six has a running pipe, and no contest-outcome claim travelled it, since no decision was made; the fourth has readers that run on a thin supply.** In both seeds `determine` never
   executed (`matter.determined` 0, `determine.refused` 8 and 13), no pursuit moved (`pursuit.moved` 0), and all 67 (seed 0) and
   43 (seed 1) `comply` and `evade / defy` acts were `compliance.impossible`; at seed 0 **none** of the 67 was formed on a
   writ (**control**: 13 dispensations existed and no act named one). None was observed; that fits the dead core the comparison names (§3, items 1
   to 6), seen from the fold's side, but two seeds of four seasons do not prove it.

---

## 2. How a worldly matter is pulled in

### 2.1 The rule: one pipe, two stores

The architecture forbids the other design. `decision/` imports no World (`engine/season/decision/questions.py`
docstring: *"AX-2 binds every file under `decision/`: no `World`"*), the chooser works from a person's own ledger, and
the social-contest module returns a `Margin` and writes nothing (`04_CODE_ARCHITECTURE.md` §A.2; P4 §6 *Keeps*). A
sitting cannot therefore *look up* a topic. The only lawful route is the one `loop/driver.py::season` runs every
season:

```
world change ─► Event (gate-emitted) ─► WITNESS fan-out ─► Claim in each holder's OWN ledger
        ▲                                   │ channels: co_located · witness_key · document_key
        │                                   │           · chronicle · post_remit   (rosters.yaml:389)
        │                                   ▼
   RESOLVE writes ◄── Act ◄── Candidate ◄── Question (questions_for, world_q.py:3217)
```

Each holder's copy carries its own `source` (`firsthand`, `told_by`, `inferred`, `firsthand_via_knot`; `rosters.yaml:438`), its own
confidence after refraction (`decision/options.py:1456`), and, for a told claim, the chain of tellers (`Claim.chain`,
`state/carriers.py:339`). Jordan, 2026-09-02: *"our understanding of all other words and actions is subjective and
singular"* (`rosters.yaml:438` note). Two persons in one room therefore hold one matter as two claims.

### 2.2 The seven entry points

Entry points 1 to 6 are readers inside `questions_for` (`queries/world_q.py:3217`); point 3 is a stamp on the first question
and point 7 is an upstream feeder, reaching a ledger through `reach` and through content clause 3. None adds a question
source; the sources stay `claim_landed` and `need` (`rosters.yaml:585`).

| # | entry point | what the person is handed | reads | state |
|---|---|---|---|---|
| 1 | **A claim landed** | a Question about the claim's subject, admitted if the subject, the subject's place or a name inside the claim's content lies in his `reach` | his ledger; `reach` (`world_q.py:907`) | **FIRES** (the bulk: §2.3) |
| 2 | **An ambition** (`need`) | a standing Question each season for every live `commit` to an OUGHT Proposition | his `commit` edges | **FIRES** (495 `need` Questions in four seasons; the count also includes `need` Questions made up for a person who has standing occasions and no ambition, `world_q.py:3426-3427`) |
| 3 | **A standing occasion** | classed referents stamped on the Question he answers: seats vacant (`vacancies`, `:2776`) or named to him, writs he holds, Records he holds that a row asks him to hold, places named to him, larders his seat may requisition, works sites | his tenures and seat | **FIRES**: the probe's stamped referents are mostly buildings and settlements, with some persons and Records; the probe does not log which term stamped which, so it cannot separate this point from the Question's own referents |
| 4 | **A sitting** | one Question per fired sitting whose docket holds a matter and whose bench he sits on | the docket; `sittings_before` (`:290`), `judging_set` (`:568`) | **NEVER** (**control**: at no season end of seed 0 did any docket item hold both a date and a matter); 18 and 15 Dates fired |
| 5 | **A docketed matter** | one Question on matters whose docketing Event his own ledger holds a claim of | the docket; his ledger (`docket_question`, `:374`) | formable (10 and 5 docketed matters); **firing not measured** |
| 6 | **A standing crossing** | one Question on his own standing crossing a band, about the people who told | his windowed estimate (`standing_crossed`, `:3192`) | **NEVER** in realm play (H-222, per reasons-to-convene §4 J) |
| 7 | **A thing he said** | `utter` mints a Proposition and the utterer's own `hold` on it, so later Questions can be *about* it; a document he holds deposits `content:<kind>` into his ledger | `Proposition`; `Record.subject_matter` (`rosters.yaml:179`; `ABOUT_KEYS`, `person_q.py:1213`) | **FIRES** (`proposition.uttered` 194 events, seed 0) |

A document is the one entry point that carries a *matter's content* and not only its occurrence. Every Record kind states
which key it is about (`petition.terms`, `dispensation.terms`, `works.plan`), and holding the Record deposits that
content into the holder's ledger, so a petition naming an accused makes the accused a referent for everyone who
holds or hears of it.

### 2.3 What the pipe carries (probe, seed 0, four seasons; 83 persons at the build, 78 at the end, since `person.died` is 5 in each seed)

| quantity | value |
|---|---|
| claims held at the end, all ledgers | 15,600 (firsthand 11,712 · told 3,866 · inferred 22) |
| the larger claim stems about social matters (`exists` 504 and `condition.worn` 376 are larger and not listed) | `seen` 6,421 · `term.matured` 1,086 · `dispensation.issued` 935 · `date.scheduled` 739 · `tenure.closed` 642 · `record.created` 596 · `proposition.uttered` 298 · `duty.refused` 260 · `finding.made` 233 |
| Questions at the four season starts, summed over persons | `claim_landed` 15,642 · `need` 495 |
| first question of a person-season was `claim_landed` / `need` | 226 / 56 |
| `claim.deposited` / `claim.decayed` Events | 35,700 / 37,049 (a ledger turns over; the end state is a remainder) |
| Propositions by mood | OUGHT 258 · HOLDS 3; live `commit` edges: OUGHT 128 · HOLDS 5 (seed 0) |
| Records by kind | `text` 342 · `faction_sheet` 76 · `cover` 52 · `petition` 27 · `dispensation` 13 · `works` 2 |
| live edges | `hold` 731 · `contain` 405 · `commit` 133 · `reside` 78 · `oblige` 52 |
| docket items / empty sitting slots / items holding a matter / of those naming an arrangement row | seed 0: 28 / 18 / 10 / 0 · seed 1: 20 / 15 / 5 / 0 |

One Event reaches many ledgers: 13 `dispensation.issued` Events at seed 0 stand behind 935 claim copies. That is
the fan-out, and it is why "how a matter is pulled in" is mostly a question of *who* each Event is deposited with.

The three HOLDS Propositions are `fac_guilds`, `fac_schoenland` and `fac_faction_x`, the factions with no creed
(`populated.py`'s fallthrough, noted in `creed_sweep`'s docstring; listed from a built realm at this checkout). **A forensic matter has no HOLDS carrier in computed play.** An accusation travels as a petition whose
`terms` is the accused, which names a party and a wrong but states no proposition that could be proved or denied. The
plea of P4 §3.5 (*deny / concede the fact / concede the definition*) has nothing to be a plea *to* until a case file
carries one.

### 2.4 Which matter a person meets first

He answers **one** Question per round (`question_aggregation_rule = first`, `data/fixtures.py:512`), so a matter must
sort first, not merely exist. `attention_key` (`world_q.py:3060`) orders by five tiers, each a reading of the person's
own state:

0. a referent of one of his own ambitions;
1. a referent among his tenure objects or inside his seat's purview;
2. a deed claim he judges strongly under his own pursuits, by `-|valence|`;
3. the standing `need`;
4. everything else, and the echo of his own deed.

**This is the first place a standpoint acts.** Two persons handed the same Event meet different matters first, and
the ranking is by *relation to the person*, not importance to the world. A territory's lord meets a larder first
because it lies inside his purview; a clerk meets a heresy first because it touches an ambition. No new meter is
needed for salience, and none may be added (S-7).

### 2.5 From a matter held to a matter before a room

A claim in a ledger is not yet a contest. Four lawful routes put a matter on the docket (`World.docket`), each an act
by a person:

| route | act | who may | writes |
|---|---|---|---|
| remit | `open_case` (`effects_information.py:301`) | a seat whose purview reaches the party | case file Record, docket item, `case.opened` |
| right | `carry` (`:383`) | whoever holds a petition | the petition's stages re-wound, docket item, `petition.carried` |
| sitting | `convene`, then `open_case` fills the slot | a seat holding `convene` | a Date; CALENDAR forms an empty slot; the next case fills it. **Never ran at seed 0**: no slot was ever filled (**control**) |
| consent refused | an act refused because it needs a count (reasons-to-convene RL3) | the owner of the act | **ABSENT** (no consent row) |

P4 changes the first row (a case file of kind `case`, a citation as a writ, the row named by the opener) and adds the
rite. A computed `open_case` today names no arrangement row (`effects_information.py:346, 355`), which the probe
confirms: of 28 and 20 docket items, 10 and 5 hold a matter and none names a row (the rest are empty sitting slots). `open_case` was attempted 16 and 11 times and opened 5 and 3
cases (`case.unauthorized` 3 and 1, `case.refused` 8 and 7).

### 2.6 What cannot enter

- **A matter with no person-party cannot be disposed.** `open_case` accepts any id (`world_q.py:270-272`), and a
  `cohort_set` was docketed in each probe seed (`cohort_set_s_026`, `cohort_set_s_017`). But `determine` refuses a
  non-person matter at its `party` conjunct (parliament design §10 B-1), and only a person's determination empties a
  slot, so such an item holds its slot for ever. Pure policy ("raise the levy") is carried only as a motion *about its
  holder*. This is the precedent, taken here; §7 gives the revert.
- **A fact nobody holds a claim of.** A shortage no ledger records raises no question. The chronicle channel
  (`binding_decision` emissions) is the one public record, and it reaches only decisions.
- **A possible future** (P-24, open in the parliament design §3).
- **A stored aggregate.** There is no standing, legitimacy or morale number to put on the agenda (S-7). A territory's
  regard for an authority is a Query over residents' ledgers, and P4 §11 Q2 asks whether the draw may read it.

---

## 3. The matters that can be discussed

### 3.1 What makes a matter a matter

Four tests, each from a ruling. A candidate that fails one is not a matter of this subsystem.

| test | ruling |
|---|---|
| it is **about the world and enacted by characters of the world**: what changes, why each person is in the room, who learns it | R-21 |
| it names **a person who is its party**, since persons own all edges | parliament design §1; `determine`'s `party` conjunct |
| the disposal **writes something that can be lost**, or moves a mind: a `Tenure`, a `Record`, a licence, a pursuit | R-21, R-26 (*"even if it is just a change in opinions"*), R-29 |
| a **carrier** names it: a Proposition, a Record kind with an `ABOUT` key, a docket item, or a claim | `rosters.yaml:179` |

### 3.2 Two axes every matter carries

**Mood** is the Proposition's own: `HOLDS` (a past fact: forensic), `OUGHT` (a future act: deliberative), or neither
(epideictic). It is derived, not a field of the matter (reconciliation E3). **Tier** is the rung where the decision
lies: a sitting at a hearth-tier rung can hear only matters at that hearth (`slot_for` walks up from the matter's
place; reasons-to-convene §0). **Authority** (the parties, the polity, the church; R-34) says whose force the venue
carries and so who may sit. The eight seeded arrangement rows give the disposals available (`arrangements.yaml`).
The rows carry no authority key today. The last column is what the comments give where they give one (`arrangements.yaml`
:99 for arbitration, :160-172 for the four SC-03a rows, :257 for excommunication); "the polity" for the two councils is
my reading. P4 §3.1 would make it a key:

| row | disposes | authority |
|---|---|---|
| `arbitration` | `oblige` | the parties |
| `parliamentary_debate`, `council_of_state` | `Record` | the polity (my reading; no comment says so) |
| `legal_trial`, `interrogation` | `detain` | a secular bench |
| `tribunal` | `ban` | a body over its own membership (*"binds the order"*) |
| `inquisition_hearing`, `excommunication_deliberation` | `ban` | the church |

### 3.3 The seventeen families

"State" is seed 0, four seasons, from the probe unless marked *(per source)*, meaning taken from the reasons-to-convene
measurements of 2026-10-29 at `120b3bf7` and not re-run.

| # | family: what is before the room | mood · party | a disposal can write today | state |
|---|---|---|---|---|
| 1 | **A wrong done**: a killing, wound, theft, sabotage, forgery, breach of duty, broken vow | HOLDS · the accused | `detain`, `ban`, `oblige` (penance) | offences are attempted and mostly refused: `kill.refused` 51, `sabotage.refused` 81, `challenge.refused` 125, `forge.refused` 86; `record.forged` 45 executes, but no forged sheet had a second holder. `case.opened` 5 (seed 1: 3); `arrest.made` 0 |
| 2 | **Heresy and creed**: deviation from orthodoxy, schism, excommunication | HOLDS or OUGHT · the accused, or the preacher | `ban` | five affiliations authored and 42 of 78 survivors hold a conviction; no producer for a charge; the church seat's reach stops at T9 (P4 §5 K3b, §11 Q1) |
| 3 | **Contempt and defiance**: a writ or summons refused | HOLDS · the defier | `ban` (no arm needed) | `comply` and `evade / defy` are emission-only (`verb_table.yaml`: `writes: []`); all 67 acts were `compliance.impossible` (seed 1: 43), and none of the 67 was formed on a writ (**control**); `compliance.withheld` 0 |
| 4 | **A dispute over a holding**: land, stores, a record, a title claimed by two | HOLDS · the holder | **a `hold` transfer: ABSENT** (`_disposal` has no `hold` site; no `succession` row) | 731 live `hold` edges; no producer of a dispute over holdings *(per source: reasons-to-convene §4 G)*; the 5 live `commit` edges on HOLDS Propositions are all on faction Propositions |
| 5 | **Office**: appointment, vacancy, deposition, revocation | OUGHT · the nominee or holder | `confer`, `revoke` (a `ban` on the stripped man); the licence is a `resolution` Record: **ABSENT** | `vacancies` stamped; every seat offered vacant is appointed *(per source)* |
| 6 | **A grant**: cession of land, fief, privilege, writ | OUGHT · the granting holder | `give` of a `hold`; `issue` a `dispensation`; the consent conjunct (CR-36 T3a) is **ABSENT** | 13 `dispensation.issued` Events, 935 claim copies; `give` 7 acts *(H-229: no computed `give` completes a transfer)* |
| 7 | **Obligation and service**: oath, tribute, levy, renewal | OUGHT · the obligor | `oblige` with a term | 52 live `oblige`; `term.matured` 762 events, subjects not decoded |
| 8 | **War, peace, treaty** | OUGHT · the opposing head | `covenant` (a Record); `march` | `march.declared` 78; `covenant.offered` ~0 *(per source)*; the negotiation row is unseeded |
| 9 | **Provision and shortfall**: hunger, stores, relief | OUGHT · the larder's holder | `requisition`, transfer of stores | `stores.changed` 253; `larders_in_purview` stamped; no consent row, so a lord who can requisition alone has no reason to sit |
| 10 | **Place and people**: settlement, migration, founding, an ungoverned place | OUGHT · the intended holder | `reside`, a `hold` on a Rung, a `works` Record | `migrate.refused` 129; `places_named` stamped for most persons |
| 11 | **Standing and reputation**: slander, censure, praise | HOLDS or neither · the person whose standing is in question | claims and stance moved in hearers; `ban` as censure | `tell` 55 acts, `news.told` 14, `news.untold` 90: the one social contest that runs (prize: a standing) |
| 12 | **Fact-finding itself**: what happened, whether a document is genuine, who acted under a cover | HOLDS · the subject of inquiry | claims, with a finding's quality | `finding.made` 210 · `cover.assumed` 52; feeds the other families |
| 13 | **A bargain**: offer, exchange, alliance, marriage, patronage | OUGHT · the counterparty | a `commit` pair, then `give` or `oblige`; `tie`, `knot` have no opener | `exchange` attempted 106, refused 106; `covenant` 17 acts; `tie / knot` have no opener |
| 14 | **Procedure itself**: forum, jurisdiction, the bench's composition, a challenge to a judge, an appeal, a pardon | HOLDS or OUGHT · the bench or the case | the docket item's row (P4 forum stage); `pardon` closes `detain` and `ban`; an appeal closure basis: **ABSENT** | `pardon` exists; one case per matter, a second refused (`effects_information.py:368`) |
| 15 | **Opinion on a subject**: the debate whose only result is a changed mind | neither · a person (a faction through its head) | `Person.pursuits` (`argue`); `speak` emits only | `argue` 0 folded acts at both seeds; one executed in three earlier two-season seeds *(per source: code audit §8)*; no Proposition reaches an arguer's question |
| 16 | **Membership**: admission to, expulsion from, or precedence in a body (the `tribunal` row "binds the order"; a guild, an order, a council) | OUGHT or HOLDS · the member or applicant | `ban` as exclusion; admission is a self-sworn `oblige` | `oblige` 255 acts at seed 0; no admission contest has a producer |
| 17 | **Trade and levy**: a market, a toll, a price, a tax | OUGHT · the holder of the market or the rung | none: no tax or levy verb exists beyond `requisition` (parliament design §8) | no producer *(per source)* |

Families are sorted by what the disposal writes, so an act is filed under the family whose disposal is sought: contempt is
a breach of duty and is family 3 when the `ban` is sought, family 1 when a sentence for the breach is. The table is a
sorting, not a proof that no other matter exists.

Three notes on the table.

- **Families 1 to 3 and 7 are the ones a bench disposes today**: `detain`, `ban` and `oblige` exist as disposals, and
  four seeded rows name them; but a computed case names no row and so disposes only `oblige`, and `detain` and `ban`
  need a hand-built act. Family 15 is R-26's *"change in opinions"*, and `argue` is its only writer.
- **Families 5, 6 and 9 are blocked at one place**: the owner's act must be licensed by a count or by a consent, and no
  verb row carries that conjunct (CR-36/37; reasons-to-convene RL3). Family 4 lacks a `hold` disposal site and family
  13 a computed `give`. None of these is a contest-design question.
- **No family is "a topic" in the sense of a subject for talk alone.** A family with no party has no disposal and no
  fold. The six speech kinds of `arrangements.yaml` (`deny`, `cite_incompatible`, `impugn_motive`, `concede_fact`,
  `concede_harm`, `hand_error_back`) are all `genres: [forensic]`, so the roster that answers *how* to speak is
  forensic only. Deliberative and epideictic matters (families 5 to 10, 15) have no speech-kind roster.

### 3.4 How the families map to the eight kinds

P4 §5's kinds are the *shapes* of contest; the families are the *content*. A family may occur under several kinds. P4
D-7 makes K8 a stage of a case and a warrant-holder's duty, not a matter type, so family 14 appears as a stage of K3
and K5.

| kind (P4 §5) | families it hears |
|---|---|
| K1 dyadic influence | 11, 12, 15 |
| K2 negotiation | 6, 7, 8, 13 |
| K3a royal tribunal | 1, 3, 4, 12 (as the proof stage), 14 |
| K3b heresy tribunal | 2, 3 |
| K4 petition | 5, 6, 9, 10, 16 |
| K5 panel (disposes as K3: `detain`, `ban`) | 1, 12, 14, 16 |
| K6 deliberation by count | 5, 6, 7, 8, 9, 10, 17 |
| K7 display | 11, 15 |

---

## 4. How different standpoints occur

### 4.1 What a standpoint is, and is not

A **standpoint** is the position from which one person meets one matter. It has no carrier. R-20 (primitives §1, gloss): a role is a
relation to an occasion, never a field. S-7: *"no magnitude carrier at any scale."* The 2026-09-06 rulings file, on legitimacy:
*"a ruler can be wrong about their own standing"* (`design_rulings_2026-09-06.md`, consequence 3 under S-7). Each part is a Query over the person's own interior, so two persons
holding different ledgers read different values from the same function (`person_q.legitimacy`, `person_q.py:452`).

A **side** is likewise derived: the persons holding a live `commit` to the same Proposition, counted when read and
stored nowhere (R-29; parliament design §0 b). No code asks a person which side he is on.

### 4.2 Eight sources of difference

| # | source | what makes two persons differ | owner | probe, seed 0 |
|---|---|---|---|---|
| 1 | **What they know** | different channel (presence, a held document, the public record, a remit); different source (firsthand, told, inferred); a told claim passes through tellers | `epistemic.observers_for`; `Claim.chain` | of 1,915 (subject, predicate-stem) pairs held by two or more persons, 317 differ in value, 1,197 in confidence, 67 in source *(a coarse count of differing copies, grouped by stem, not of disagreements; the confidence count is mostly age: see row 2)* |
| 2 | **How much they credit it** | refraction lowers confidence by the channel's distance and by dissent from what the holder already holds; the teller's weight depends on the hearer's regard | `refracted_confidence` (`decision/options.py:1456`); `teller_weight` (`:1559`) | **control**: among copies of one claim deposited in the same season, 1,122 groups have two or more holders and confidence differs in 59 of them (5%), with source differing in the same 59. The 1,197 above is therefore mostly age, since MATTER lowers every claim's confidence each season (`matter.py:432-462`) |
| 3 | **What they want** | fifteen pursuit weights, projected on seven bipolar axes; one deed is virtue to one and offence to another | `descriptor_registry.yaml`; `pursuit_projection`; `deed_valence` (`person_q.py:371`) | `stability` weights run .02 to .80 (sd .20); `community` sd .14; `stewardship` sd .12; all 78 survivors hold pursuits |
| 4 | **What they believe** | five affiliations on a 0 to 5 scale; a stored 0 is a held rejection; scars move a conviction at threshold 3 | `Person.conviction`; `affiliation_roster` | 42 of 78 hold a conviction |
| 5 | **Whom they regard** | stance rows plus the deeds they judge and were told of; opinion of a faction on `[-3, +3]`, from the faction's expectations, the poles it engages and the members the person regards | `person_q.regard` (`:393`); `world_q.opinion_of` (`:2684`) | eight factions: sd .43 to .48; signs split (see below) |
| 6 | **What they hold** | the edges a matter touches: holdings, obligations, commitments, seats | `Tenure`; `own_purview`, `reach` | 731 `hold` · 133 `commit` · 52 `oblige` · 32 offices |
| 7 | **Where they sit** | a seat adds purview and, under R-31, venue-keyed weight; a person's faction adds an authority | `Office.scope_rung`; `authority.by_faction` (P4) | 32 offices in the realm |
| 8 | **What they can bring** | attributes through faculties into the pool (P4 §3.2) | `Person.capability` | **0 of 78 hold any**; every roll is `pool_default` |

Opinion of a faction across the 78 persons alive at the end (tick 0, 83 persons: standard deviations .44 to .49 and the same sign splits within a few persons; **control**) (sign counts; a person at 0.0 counts in neither):

| faction | negative | positive | min | max |
|---|---|---|---|---|
| Hafenmark | 39 | 39 | -0.55 | 0.93 |
| Guilds | 58 | 20 | -0.82 | 0.85 |
| Restoration Movement | 54 | 24 | -0.68 | 1.15 |
| Church of Solmund | 30 | 48 | -0.88 | 1.02 |
| Altonia | 29 | 49 | -0.80 | 0.88 |
| Crown | 17 | 61 | -0.63 | 1.12 |
| Löwenritter | 17 | 61 | -0.56 | 1.18 |
| Varfell | 10 | 68 | -0.50 | 0.99 |
| Schoenland, "faction x" | 0 | 0 | 0.0 | 0.0 |

The last row is an **empty standpoint** at the end of four seasons: every person reads the same zero, so those two
factions divided no room in these runs. (`opinion_of` has a third term, the faction's head and the live members whose
deeds the person holds claims of, `world_q.py:2710-2717`; it had no input here, but a witnessed deed by a member would
move it.) The opinion function needs the faction's expectations (`data/goals.py::expected`) and its engaged poles; for these
two `expected` returns `{}` and `engaged_poles` returns `()` (checked at this checkout). This is a content gap, not a mechanism gap, and is the same shape as P4 §3.6's *"a Church goal
that engages `solmund_orthodoxy`, or church L is flat by construction."*

### 4.3 Role: the standpoint toward the occasion

Role is derived from edges and from the docket, per matter, and one person may hold several at once. The King holds
the realm seat and the Valorsmark duchy seat both, so he sits on benches at two rungs (parliament design §4); a duke is
a council member only by his own `oblige`.

| role | derived from | what it changes |
|---|---|---|
| **party** | subject of the docketed matter (`docketed`, `world_q.py:200`) | the obstacle's other side; the disposal binds him |
| **accuser** | holds or filed the petition whose `terms` is the party | burden under the accusatorial rite; named or secret under the inquisitorial (P4 §3.4) |
| **bench** | `judging_set`: seats holding `determine` whose scope contains the venue (`world_q.py:568`) | the one who decides; his own regard becomes σ on his own `determine` (P4 §3.3) |
| **member** | a live `oblige` to a council seat (`establishment_of`, `:2432`) | counted when a `commit` licence is read |
| **audience** | present at the venue, so the event is `co_located` | reception; first-hand claims |
| **advocate** | a proxy for a party; may only deny (P4 §4.6) | absorbs a disproved denial, not the principal's lie |
| **witness** | holds a relevant claim; identity, act and motive are separate claims, each possibly absent (S-8) | supplies or withholds proof |
| **warrant-holder** | holds `dispatch` whose purview reaches the party (P4 §3.7) | serves or declines; a decline is witnessed |
| **absentee** | a citation's addressee who does not come | tried against his own score ÷ 2 (P4 critic, finding 6) |

### 4.4 How standpoints become sides

Standpoints differ everywhere; a contest forms only where they **cannot both be satisfied** and someone with purview
holds a claim of it and chooses to act. Five collision shapes sort the families (a family may fall under more than one; family 15 needs none, since the hearer
alone decides):

| shape | what collides | families | the live carrier |
|---|---|---|---|
| **rival claims** | one says the fact is so, another denies it | 1, 2, 3, 11, 12 | a petition against a party; a plea (P4) |
| **rival commitments** | a motion and a counter-motion; offer and counter-offer; consent given and withheld | 5 to 10, 13, 16, 17 | two live `commit` edges on rival Propositions; a count when read |
| **rival stakes** | two holders or claimants of one object | 4, 5 | two `hold`-claims on one object; **no disposal site** |
| **rival authority** | who decides: parties, polity or church | 2, 14 | the row's authority; the forum stage (P4 §3.7) |
| **petitioner and grantor** | one wants, the other may give; no rival claim | 6, 9, 10, 16 | a petition addressed to a seat that can answer (RL4; H-94 limit today) |

The fourth shape is not a disagreement of fact or of wish. It is **a disagreement about whose standpoint counts**, and
R-34, R-36 and R-35 exist to arbitrate it: authority is vested by the nation, by religion or by the parties, and it is
scaled by local legitimacy.

### 4.5 One matter, five standpoints: a forged faction sheet

*An illustration of the design if a `give` delivered the sheet. As built it does not happen: a forged sheet is minted into the
forger's hand and nothing hands it on (**control**: of 45 forged Records at seed 0, 44 had one holder, the forger, and one
had none). The statuses below say so.*

A person forges a faction sheet (`forge`; `record.forged` executes, 45 Events at seed 0). It is `survey`'s document
with one key false: it says the forger heads the faction (`_eff_forge`, `loop/effects_information.py:777`). The forger
holds it first. A holder cannot tell it from a true sheet, *"by construction, not by a flag"* (r2 §A.15, quoted in that
docstring); only an inquiry's roll carries its `forgery_quality`. A petition filed on the strength of the false `head`
is addressed to the forger, who then holds it and may sit on it or `give` it.

| person | how the matter reaches him | what he holds afterward | his standpoint |
|---|---|---|---|
| **the forger** | `co_located` with his own act; `firsthand` | the Record (his `hold`) and a claim of his deed | wants it believed; a petition addressed to himself is declined person-side, so the lie works on others |
| **a holder the sheet reached** | `document_key`: holding it deposits `content:faction_sheet` | the claim that the forger heads faction F, at document confidence | has no way to doubt it; addresses his business to the forger |
| **the faction's actual head** | learns later through a told chain (lower confidence) or `post_remit` (`inferred`) | a claim that another is named head of his faction | has standing to act; his regard for the forger falls by `deed_valence` once he holds the deed |
| **an inquirer** | `research` on the Record; the roll's obstacle carries the forgery quality; the finding deposits (`finding.made` 210) | a finding | the only one whose claim rests on a draw rather than a teller |
| **a member of the faction who hears of it** | two hops, refracted | a weak claim; a stance toward the forger | credits it by his regard for the forger and the faction |

The matter is **HOLDS, party the forger**: family 12 (the document), feeding family 1 (a wrong done) and family 11
(standing). The collision is *rival claims*: the actual head's charge against the forger's silence or denial, with the
holder caught between reliance and doubt. No role is assigned; each falls out of the edges.

| link | status | evidence |
|---|---|---|
| a forgery executes | **FIRES** | `record.forged` 45, `forge` acts 131, `forge.refused` 86 (seed 0) |
| a second person holds the sheet | **NEVER**: 44 of 45 forged Records had one holder (**control**); delivery needs a `give` that does not complete in computed play (H-229) | `epistemic.py:379-383`; `probe_controls.py` |
| a holder reads the sheet as true | would hold by construction (the content deposit gives a holder the same claim either way); **no holder exists in play** | `_eff_forge` docstring |
| an inquirer finds the forgery | **NEVER** for the same reason; the 210 `finding.made` are not findings of forgeries, and a test pins that the seed-0 realm reaches no trail by `research` | `epistemic.py:379-383` |
| the actual head or a member files a petition naming the forger | **NEVER**: a computed petition's `terms` and `to` are the same person (H-94) | reasons-to-convene §4 B *(per source)* |
| a seat with purview opens a case on the forger | opening a case **FIRES** (5 and 3 `case.opened`); on this forger **not examined** | `effects_information.py:301`; probe |
| a `determine` disposes `detain` under `legal_trial` | **NEVER**: `matter.determined` 0 at both seeds; and a computed case names no row, so it would dispose the undeclared `oblige` | `effects_information.py:346, 355`; probe |

### 4.6 How a standpoint changes

A standpoint is recomputed each season from stores that moved. Four things move them: a **decision** (the loser's regard
for the bench drops; the winner's rises), a **deed told** (`regard` and `legitimacy` read the deeds a person holds
claims of), a **new edge** (a seat, a hold, a commit, a `ban`), and **forgetting** (`claim.decayed`: 37,049 events at
seed 0, the ledger's own weathering; `recent_claims` anchors the window on the holder's *newest* claim, so a person who
has heard nothing reads old news as current). A person's change is always the person's own act or his own reading of a
witnessed fact. Nothing pushes a stance onto him (R-19, R-23).

---

## 5. How the engine's decisions fold into the season loop

### 5.1 Where a contest sits in the season

`loop/driver.py::season` (`:375`) runs the steps in a fixed order; `w.tick` advances once, at the end.

| step | token | what a contest does here |
|---|---|---|
| CALENDAR | `CALENDAR` | fires Dates; forms an empty docket slot for each sitting (`date.fired`) |
| MATTER | `MATTER` | matures terms and stages (`loop/matter.py:340`, `due != w.tick`); an oblige term lapses; **once per season, never per round** |
| per round, R times (`scene_budget`): | | |
| DELIBERATE | none (a map) | each person answers one question from `questions_for`; the chooser forms Candidates and acts |
| RESOLVE | `ACTS` | admits each act (`_admits`), dispatches a contested one to the seam, folds the result |
| ENCOUNTER | `ACTS` | fights the field battles RESOLVE declared; no social contest here |
| WITNESS | `INTERIOR` | fans every Event out to ledgers by channel; this is the only writer of claims |
| after the rounds: | | |
| CENSUS | `MATTER` | once per season, after the last round (`driver.py:519`): individuates cohorts; the endings are then read (`:523`) |

Two timing rules bind a contest. **A staged hearing is season-granular**: `Tenure.since` is the season tick and no
round is stamped on an Event or a Tenure, so order *within* a season is not enforceable (parliament design §2). **MATTER
matures a stage only on `due == tick`**, not `<=` (`matter.py:340`), so a stage that did not mature at its due tick never
matures later; and a stage whose holder is gone or not in `w.persons` at that tick is skipped (`matter.py:340-346`). P4
repair b is the `<=` fix.

### 5.2 One act, from question to ledger

```
Question ─► Candidate (chooser, person-side) ─► Act
   RESOLVE:  _admits (eligibility · requires · budget)
             └► contested verb? ── yes ─► sides_of ─► contest() seam ─► provider roll ─► Margin
                                                   (R-24 routes a non-player contest through the automated route; the same-draw-at-both-fidelities rule is the armature's, comparison §6 item 7)
             degree_of(Margin) ─► the one ladder (degree_from_net; R-5, R-6) ─► Overwhelming/Success/Partial/Failure
             _fold: the verb row's band says what is WRITTEN and what is EMITTED
             effect(w, a, res) ─► Change   (the effect writes nothing; it returns the change)
             World.write(token, …, change) ─► the gate: class · step · partition · tenure basis ─► receipts
             Event (emits, or emits_on_refusal) ─► w.log
   WITNESS:  observers_for(Event) ─► Claim in each observer's own ledger (source · confidence · chain)
   next DELIBERATE: those claims are Questions again
```

`loop/resolve.py::_contest` (`:734`) and `_fold` (`:342`) are the only places a social-contest result becomes a write.
The module returns a typed outcome and holds no token (`04_CODE_ARCHITECTURE.md` §A.2); the driver is the sole
constructor of write tokens (`driver.py::mint_token`). A refusal is an Event of the row's `emits_on_refusal`, never an
exception, and it is witnessed like any other.

### 5.3 What each outcome writes today

Bands are the one ladder's. A cell shows the write at Success unless the band changes it. *Emits* is what WITNESS
fans out.

| act (verb) | prize | writes | emits | who learns |
|---|---|---|---|---|
| `tell` | a standing | nothing by itself; the hearer's claim lands at WITNESS | `news.told` and `confidence.broken` (any band but Failure), `news.untold` on Failure | the hearer; those present |
| `argue` | a proposition | the hearer's `Person.pursuits`, moved toward the arguer's (`argued_pursuits`, `person_q.py:638`); Partial and Failure write nothing | `argument.won` · `pursuit.moved`; `argument.lost` | those present |
| `speak` | a matter | **nothing at any band** (`writes` empty) | `matter.carried` · `advanced` · `held` · `turned`; `speech.unheard` on refusal | the room |
| `determine` | a proposition | the disposal edge (`oblige` / `detain` / `ban`, with the band as its `degree`), the docket item cleared (`matter: None`), **and the judge's own pursuits** by `consequence_pursuits` (`person_q.py:615`, called at `effects_information.py:561`); Failure writes nothing | `matter.determined` · `pursuit.moved`; `matter.undetermined` | the reach of the row |
| `arrest` | a standing | a `detain` on the seat that issued the warrant | `arrest.made`; `arrest.resisted` | those present |
| `open_case` | none | case file (kind `text`), docket item | `case.opened` | those present |
| `carry` | none | the petition's stages; docket item | `petition.carried` | those present |
| `petition` | none | a `petition` Record | `petition.filed` | those present |
| `utter` | none | a Proposition and the utterer's `hold` | `proposition.uttered` | those present |
| `commit` | none | a `commit` edge | `commitment.made` | those present |
| `comply`, `evade / defy` | none | nothing | `compliance.given` · `compliance.withheld` | emission only; **no price** until P4 |
| `pardon`, `release` | none | closes `detain` / `ban`, or an `oblige` | `detention.ended`, `ban.ended`; `tenure.closed`, `commitment.ended` | the reach |
| `convene` | none | a Date | `date.scheduled` | all who hold it (~85% of persons, per source) |

Two features of this table matter for the fold.

- **`speak` is a contest with no write.** A body-speech is rolled and graded but the world changes only through
  its emitted kinds, which become claims. Whether the room's opinion moves is therefore decided entirely by what each
  hearer's own reading of `matter.advanced` does. P4 does not change this; the parliament design §5 names it as
  build 3.
- **`determine` changes the decider.** The judge's pursuits move by the consequence of what he decided, scaled by
  the band (`Partial` moves nothing; `Failure` writes nothing). A judge who convicts becomes, by a sliver, a different
  judge. That is a standpoint change produced by the engine's own decision (§4.6), and it has not yet happened in
  either probe seed.

**Probe: what the seasons produced.** *(Seeds 0 and 1, four seasons each; counts are Events in `w.log` and acts
folded.)*

| step | event kind or act | seed 0 | seed 1 |
|---|---|---|---|
| put a matter before a room | `petition.filed` · `petition.carried` · `carry.refused` | 27 · 5 · 19 | 27 · 2 · 16 |
| | `case.opened` · `case.unauthorized` · `case.refused` | 5 · 3 · 8 | 3 · 1 · 7 |
| sittings | `date.scheduled` · `date.fired` | 20 · 18 | 19 · 15 |
| speech | `speak` acts · `speech.unheard` | 4 · 59 | 4 · 55 |
| | `matter.advanced` · `matter.turned` · `matter.carried` · `matter.held` | 1 · 3 · 0 · 0 | 0 · 4 · 0 · 0 |
| argument | `argue` acts · `argument.won` · `argument.lost` | 0 · 0 · 0 | 0 · 0 · 0 |
| telling | `tell` acts · `news.told` · `news.untold` | 55 · 14 · 90 | 54 · 20 · 87 |
| commitment | `commitment.made` · live `commit` edges (of which HOLDS) | 6 · 133 (5) | 6 · 131 (5) |
| judgment | `matter.determined` · `matter.undetermined` · `determine.refused` | 0 · 0 · 8 | 0 · 0 · 13 |
| a moved mind | `pursuit.moved` | 0 | 0 |
| enforcement | `arrest.made` · `compliance.given` · `compliance.withheld` | 0 · 0 · 0 | 0 · 0 · 0 |
| | `comply` + `evade / defy` acts · `compliance.impossible` | 67 · 67 | 43 · 43 |
| release | `pardon` acts · `pardon.refused` · `detention.ended` + `ban.ended` | 8 · 8 · 0 | 9 · 9 · 0 |
| the supply of wrongs | `forge` acts · `record.forged` · `kill.refused` | 131 · 45 · 51 | 113 · 45 · 49 |
| inquiry | `finding.made` · `finding.none` | 210 · 260 | 208 · 218 |

The pattern fits the comparison's dead core (§3 there), read from the other end; its audit count (`determine` executed 0
times) is the longer-run evidence. The front of the fold runs: petitions are filed, cases open, Dates fire, claims land.
**Nothing downstream of `determine` was observed in either seed**: no
judgment, no moved pursuit, no arrest, no pardon that frees anyone, no writ answered (none was ever the subject of an answer). Every `pardon` (8 of 8, 9 of 9)
is `pardon.refused`, and no `detain` or `ban` is live at the end; the cause of each refusal was not isolated. Every `comply` and `evade / defy` is
`compliance.impossible`, and at seed 0 none of the 67 was formed on a writ. The same gap holds for `speak` (4 folded acts, 59 `speech.unheard`). `determine.refused` was emitted 8 and 13 times, yet `determine` is not among the folded acts
(`d.resolved`) of either seed, so those refusals came before the fold or are not counted there; which, I did not
examine.

### 5.4 What P4 would add to the fold

P4 adds no resolver and no stage code. It adds carriers the fold already knows how to write.

| addition | fold route | gate cost |
|---|---|---|
| **case file** (Record kind `case`) | `open_case` mints it; `determine` asks to *hold* it; only the holder writes `stages` | a `record_kinds` member and its readers; a fifth `determine` conjunct |
| **citation** | a `dispensation` addressed to the party, served by `give` | none: an existing kind |
| **stage close** | one draw by whoever the rite names; Failure is held to the next sitting; MATTER matures `<=` | the one transition; the `<=` repair |
| **disposal with an arm** | a `detain` opens directly only if the seat's purview reaches the party; otherwise a **warrant** to a `dispatch` holder, who serves or declines | the warrant branch in `_disposal` |
| **a decline is an Event** | a warrant that matures unserved, and a citation unanswered, emit and are witnessed | MATTER on the warrant's stage |
| **forum** | the docket item's row changes in place; no second case | none beyond the stage |
| **appeal** | a `petition` to the row's `appeal_to` seat; a new closure basis lets it void | an appellate closure basis (`pardon` closes only the exercised seat's edges) |
| **count** | `licence` is a Query over live `commit`s; the owner's act gains a conjunct *holds a live `resolution`* | one conjunct per row, plus a data owner for "this cession needs consent" |

### 5.5 The return path: six feedback routes

*Propagation without reaction is a chronicle, not a game* (`design_rulings_2026-09-06.md`, quoted in primitives §1.0).
The fold closes only if some reader of the next season consumes what this one wrote.

| # | result | the reader that picks it up | what changes next season | state |
|---|---|---|---|---|
| 1 | a witnessed decision | `questions_for` entry point 1: the claim lands in ledgers within `reach` | the decision becomes a Question for parties, bench and neighbours | the pipe runs (35,700 deposits); **no contest-outcome claim was followed through it**, since no decision was made |
| 2 | a disposal edge (`oblige`, `detain`, `ban`) | `oblige` refuses a `ban` holder service; `move` and `migrate` decline a `detain`; a mustered army excludes him; `confer` declines to seat him | the party's available acts and his seat change | **NEVER** at both seeds (no disposal opened: `matter.determined` 0, `arrest.made` 0); the readers exist |
| 3 | a moved pursuit | `choose`'s pursuit alignment; `attention_key` tiers 0 and 2 | the hearer or judge answers different matters first | **NEVER**: `pursuit.moved` 0 at both seeds (`argue` 0 acts, `determine` 0) |
| 4 | a deed told | `regard`, `legitimacy`, `opinion_of` | the person's regard for the doer, and the authority's standing, move | readers **FIRE** (the spread of §4.2 is computed from them); supply is thin: `news.told` 14 and 20; `judged_gain` and `told_valence_gain` ship at 0.5 |
| 5 | a held writ or warrant | `writs_held` stamp; `comply` and `evade / defy` | the addressee must answer; a decline is a deed others judge | writs are issued (13 and 19 Events) but reach no one (a writ is minted into its maker's hand and needs a `give`; `writs_held` returns `()` for nearly everyone, `world_q.py:2823-2827`); the 67 and 43 `comply` and `evade / defy` acts were formed on other Records, **every one `compliance.impossible`**; a price for defiance: **ABSENT** (P4 repair i) |
| 6 | an unanswered stage | MATTER on the stage; a witnessed lapse (`matter.lapsed`, an Event no code emits; proposed in the parliament design, step 9) | the matter is held, then lapses visibly | **ABSENT** (MATTER matures only `due == tick`) |

Only route 1 has a running pipe in the probe, and nothing contest-made has crossed it. **The route that would make a contest matter to a third party is route 4**, because
a decision changes what the neighbours think of the authority that made it, and that is R-36's legitimacy arrived at
by persons rather than by a stored number. It has readers and a thin supply, since a decision must first be made and
told.

### 5.6 What stays outside the fold

- **No declaring verb and no stored tally** (R-29). A count licenses or blocks the owner's own act; the assembly never
  acts on the world.
- **No immediate re-contest of a rendered outcome** (R-35). Appeal goes to another authority.
- **No magnitude carrier** (S-7). Legitimacy, standing and morale are read, never written.
- **Not every contest is played** (R-24). A non-player contest takes the module's automated route; the armature's rule is the same Act and the same
  draw at both fidelities (comparison §6 item 7), so the fold is identical and a player's trial and an NPC's trial are
  one path.
- **No special case for an entity or an outcome** (scripting drift, `04_CODE_ARCHITECTURE.md` G.1.6). A new family of
  matter is a row, a Record kind or a Proposition predicate, never a branch.

---

## 6. What depends on which proposal

| part | P1 one draw | P2 staged | P3 authority | P4 |
|---|---|---|---|---|
| intake (§2) | same | same | same | same, plus a `case` Record |
| the families (§3) | disposals: the three kinds | same | same, plus forum | same, plus the rite's four switches |
| standpoints (§4) | capability unauthored | same | same | the faculty table gives source 8 content |
| the fold (§5) | smallest | adds stages | adds warrant, appeal closure | adds both and the case file |

Sections 2 to 4 describe the live code and hold for every proposal; the table lists what each adds. The families in
§3.3 whose disposal is **ABSENT** are absent in all four.

---

## 7. Assumptions and their reverts

No question reaches Jordan from this file. Each assumption was taken in the order CLAUDE.md §0 sets for a pending
decision (superseded, irrelevant, answered by a design document, by precedent, by what suits the architecture). The
person-party rule is the weakest: its precedent is itself PROPOSED (the parliament design, `:3`), and R-29 is its firmer
ground.

| assumption | basis | revert |
|---|---|---|
| "worldly matters" means R-26's worldly topics, and "the engine" is the social-contest subsystem as the season loop reaches it | PR #542's subject | read "the engine" as the whole season loop and widen §5 |
| a matter must name a person-party; policy enters only as a motion about a holder | parliament design §1 and B-1, followed as precedent | allow a party-less `determine`, which needs a Record-disposal site and a gate basis |
| the seventeen families are the catalogue | derived from the disposals, carriers and the corpus themes A to M; a sorting, not a proof of completeness | add or merge a family; the fold is unchanged |
| a standpoint is the eight-part tuple of §4.2 | each part is a Query the tree already owns | none is stored; removing a part removes a Query |
| role is derived per matter | R-20 | none |

---

## 8. Limits and fidelity

**Real:** every citation to `engine/season/` was opened at its line; the verb-table writes and emits in §5.3 were read
from `verb_table.yaml` by loading it, except three cells that come from the effect and not the row (`utter`'s `hold`, `arrest`'s `detain`, `open_case`'s kind `text`: `effects_information.py:1110`, `:1029`, `:370`); the probe counts are the scripts' own output. **Taken from other documents, not
re-opened:** citations to `04_CODE_ARCHITECTURE.md` (via `CLAUDE.md` and P4), the rulings (via primitives §1) and the
cells marked *(per source)*. **Model:** none. This file proposes no number.

**What the probe is.** Two scripts build the realm for one seed and tick four seasons with the shipped chooser. They
describe what flowed in that world, not what flows in play. Seed 0 is the sole seed for §2.3 and §4.2; the event-kind
table uses seeds 0 and 1. The probe cannot see a hearer's inner reading, so §4.2's differences are differences in
*stored inputs*, not in decisions.

**A mislabel in the output.** The intake probe's key `stamped_class_on_first_question` lists referent *ids* stamped on
first questions, not classes; the script was left as run.

**Coarse counts.** The 1,915-pair figure groups claims by subject and predicate *stem*, so two claims under one stem
with different sub-predicates count as differing. It measures spread, not disagreement.

**When the Questions were counted.** The intake probe projects `questions_for` once at each season's start, before CALENDAR
and MATTER and without `since`, while DELIBERATE receives one projection per round after them (`driver.py:452-472`). "Faced"
is therefore a projection. The number of person-seasons with no first question was not recorded.

**Controls ran on seed 0 only.** The controls (writ subjects, forged-sheet holders, filled slots, tick-0 opinion, equal-season
copies) are seed 0; seed 1 was not examined.

**Not done.** No season was run with any proposal built. Statuses marked *(per source)* come from earlier
measurements and were not re-run. The five persons absent from the end-state counts are the five that `person.died` records in each seed; the probe also catches and drops an `opinion_of` exception, which was not observed to fire. The event-kind table is two seeds of four seasons; a count of 0 is an absence in
those runs, not a proof that no seed can fire it. No full suite was run; nothing in the tree outside this folder changed.

`[CONFIDENCE: medium]` on the families and the collision shapes, which are my sorting of the corpus; `[CONFIDENCE: high]`
on the code facts, each opened at its line.

---

## 9. The critics' pass and its reconciliation

One round, two independent read-only critics who saw the document and the tree and not my reasoning: **accuracy**
(Sonnet; 19 findings, none BREAKS) and **logic** (Opus; 20 findings, 4 BREAKS). Rule applied: a critic's finding is a
claim, so each was re-opened at its source before acceptance, and the same effort went to the ones I could have
rejected. Where a finding turned on something no one had measured, I ran a **control** (`probe_controls.py`) and the
tree decided. The fixes are not themselves audited.

| finding | verified how | disposition |
|---|---|---|
| the 67 and 43 "attempts to answer a writ" were not shown to be about writs (logic F1, BREAKS) | control C1: none of 67 was formed on a dispensation | **accepted**; §1, §3.3 family 3, §5.5 route 5 rewritten |
| the forged-sheet statuses rested on a docstring (logic F4, BREAKS) | control C2: 44 of 45 forged Records had one holder; `epistemic.py:379-383` | **accepted**; §4.5 relabelled an illustration, statuses NEVER |
| a party-less matter "cannot enter" (logic F3, BREAKS; accuracy F6) | the probe's own docket holds two `cohort_set` items; `open_case` accepts any id | **accepted**; §2.6 now says "cannot be disposed" |
| "only route 1 closes" used a different test per route (logic F2, BREAKS) | route 1 carried no contest outcome, since none was made | **accepted**; §1, §5.5 reworded |
| 83 persons / five "unanswered" (accuracy F1) | `person.died` 5 in each seed; control C4 shows no exception | **accepted**; end-state counts are of 78 |
| 28 docket items (accuracy F2; logic F10) | 18 and 15 are empty slots; control C3: no item ever held a date and a matter | **accepted** |
| confidence differences credited to refraction (logic F11) | control C5: 59 of 1,122 same-season groups differ | **accepted**; the 1,197 is mostly age |
| opinion spread offered as standpoints arising (logic F12) | control C4: the same spread at tick 0 | **accepted**; it comes from the build |
| "dead standpoint", "can never divide a room" (logic F6) | `opinion_of` has a third term | **accepted** in part; "empty standpoint" in these runs |
| family partition, kind map, collision shapes, catalogue completeness (logic F5, F7, F8, F9) | re-read against §3.3, P4 §5 and D-7 | **accepted**; two families added, maps rewritten, "sorting" not "partition" |
| CENSUS shown per round; `argue`, ruling glosses, authority labels, citations, source list, `matter.lapsed` (accuracy F3 to F19; logic F13 to F20) | each opened | **accepted**, fixed in place |

**Not changed.** Logic F15 asked that every FIRES and NEVER read "not observed in 2×4" unless shown otherwise; the
Evidence paragraph now says so once and gives the latency caveat, and the labels stay. Logic F20 (the committed script
is not byte-identical to the one that ran) is stated in the script's docstring, and the committed event-kinds script
reproduces its committed output exactly.

**What survived.** All 140-odd probe numbers match the JSON; 33 of 38 `engine/season` citations were exact; the 15
verb-table rows match; the `_eff_forge` description, the `determine` writes and the "no HOLDS carrier" claim withstood
the attack tried against them.
