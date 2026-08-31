# THE COMPENDIUM — keys, inputs, outputs, terms

## Status: PROPOSED (2026-08-31). **Nothing here has executed.** `CLAUDE.md` §0.2 applies: **done means
## it runs, and none of this runs.**

---

## §0 · HOW TO READ THIS, AND WHAT IT IS NOT

**What it is.** The cross-referenced register for the architecture at `01_ARCHITECTURE.md` and the loop
at `02_THE_SEASON_LOOP.md`. One row per object, per field, per function, per term. It indexes those two
documents; it does not restate them and it does not decide anything they do not.

> **⚠ THIS DOCUMENT IS REFERENCE, NOT MECHANISM** (`CLAUDE.md` §0.05). **No table here may be cited as
> the reason a behaviour is correct.** It may be cited for intent, history and vocabulary. If a table
> here and the code disagree, that is a defect in one of them and it is resolved by deciding and then
> changing **the code** — never by declaring this document authoritative. A later session that treats a
> row here as a gate has misread this paragraph.

**Its own vocabulary must pass the two tests it applies to everyone else's** (`CLAUDE.md` §4):
**idempotent in meaning** — a later session reading a term cold derives the same meaning — and
**idiomatic in choosing** — ordinary usage already supplies the word. **A compendium that coins while
cataloguing coinage is self-refuting**, so this document introduces no term of its own.

### §0.1 Citation key

| form | resolves to |
|---|---|
| `ARCH §N` | section N of `01_ARCHITECTURE.md` (this directory) |
| `LOOP §N` | section N of `02_THE_SEASON_LOOP.md` (this directory) |
| `SUP:NNN` | line NNN of `proposals/2026-08-31-ideal/10_SUPERSEDING.md` — the prior design |
| `REV:NNN` | line NNN of the adversarial review of that design: document **20** in `proposals/2026-08-31-ideal/` |
| `ABS:NNN` | line NNN of `CODE_SHAPE_ABSTRACT.md`, in the 2026-08-31 review directory under `proposals/_session_provenance/` |
| `NN:LLL` | line LLL of `proposals/2026-08-29-valoria-from-scratch/NN_*.md` |
| a bare repo path | read at the working tree |

### §0.2 Namespace key — **five id families, three of which share token shapes**

| family | shape | example | means |
|---|---|---|---|
| **review findings** | `A#`, `B#`, `C#`, `M#`, `O#`, `F#` | `B1`, `M1`, `C13` | a finding in the adversarial review |
| **runner findings** | `F-#`, `M-#`, `m-#`, letter-suffixed | `F-2`, `M-a` | a finding by one of the five audit runners behind these documents |
| **reserved forks** | `D-#`, `S##` | `D-2`, `S19` | a fork the prior design reserved; `ARCH §7` resolves six of seven |
| **module rules** | `R-#` | `R-1` (`SUP:374`), `R-2` (`SUP:379`) | an architecture rule |
| **loop steps** | **words only** | `CALENDAR`, `RESOLVE` | a step of the season |

> **THE LOOP STEPS HAVE NO LETTER-NUMBER NAMES, PERMANENTLY.** The brief these documents replace spelled
> them `B1 … M2` and cited review findings `B1` and `M1` seventy-six lines away in the same file. **Two
> namespaces, one token shape, one document.** The legacy phase names `P0 … P7` (`SUP:641-654`) are
> retired and appear only inside quotations.

### §0.3 Conventions used in the tables

- **`⛔`** — the type, range, producer or owner is **not stated in any document this suite read.** ⚠
  **That is a scope, not a corpus fact: 108 of 123 proposal documents over 200 lines are uncited by
  this suite** (`00_INDEX.md`), so a `⛔` means *we did not find it in what we read*, never *it does not
  exist*. Every `⛔` has a row in §8.
- **`RESERVED`** — a fork carried rather than answered. Six of the seven the prior design reserved are
  answered at `ARCH §7`. **All seven are now answered; two were ruled by Jordan.**
- **NEW** — introduced by `ARCH`/`LOOP`; **SHIPPED** — inherited from `SUP` or #342 unchanged;
  **AMENDED** — inherited and changed, with the departure listed at `ARCH §10`.

---

## §1 · THE IDENTITY REGISTER

**One row per object. This is the spine.** *Nameable in `Claim.subject`* is against the **open** referent
space (`SUP:229-234`); *nameable as a stance referent* is against the **closed** set, which
`ARCH §2.7` amends from four kinds to three: `Person | Proposition | Place`, where
`Place = Rung | Site`.

| object | id | identity tuple | stable / season | owner | minted by | effaced by | claim subject | stance referent |
|---|---|---|---|---|---|---|---|---|
| **Person** | `id` NEW | `id` | **yes** — `id` is a substream hash, not a path | itself | individuation, at CENSUS | death at MATTER; `efface` at RESOLVE | **yes** (`SUP:238`) | **yes** |
| **Cohort** | *not a separate object* | — | — | — | — | — | — | — ⚠ **ONE TUPLE. A cohort is a `Person` record at `weight > 1`; at `weight = 1` the record IS a person and no conversion operation exists** (`02:553-555`). An earlier version of this register gave it its own row and its own tuple while claiming no conversion existed |
| **Rung** | `id` NEW | `id` | yes | itself | `mint` | `efface` | **yes**, NEW | **yes**, as `Place` NEW |
| **Office** | `id` NEW | `id` | yes | itself | `mint` (establishment) | `efface` | **yes**, NEW | **no** — an office is not a Person, Proposition or Place; you hold an attitude to its holder or its proposition |
| **Site** | `id` NEW | `id` | yes | its Rung | `mint` (building) | `efface` (razing) | **yes**, NEW | **yes**, as `Place` NEW |
| **Tenure** | `id` NEW | `id`; secondarily `(subject, object, kind, since)` | yes | **its SUBJECT** (`SUP:337`) | `confer`, `commit`, `admit`, a naming act, co-presence, `form_knot`, kinship | `revoke`, degree→0, re-naming, decay, rupture, discharge — **each sets `until`, none deletes** | **yes**, and this is the thesis-critical one | no |
| **Act** | `id` NEW | `id` | one tick | its actor | `choose` | — | ⛔ unstated | no |
| **StateChange** | — | `(subject, mode, driver)` — position in its driver's `changes[]` | one tick | its driver | — | — | no | no |
| **Event** *(as driver)* | `id` | `id` | permanent | the event log | the world, at MATTER | never | as a `source` payload; **and as a `Claim.subject`, because an event is as disputable as an act** | no |
| **Event** | `id` | `id` — required by `firsthand(event_id)` (`SUP:243`) | permanent | the event log | `resolve` | never | as a `source` payload | no |
| **Claim** | `id` NEW | `(ledger owner, id)` — **a two-part address** | evictable at WITNESS | **one Person's ledger** | `witness`, and nothing else | eviction; decay to zero | **yes** — `SAID(Aldwin, C, s12)` | no |
| **Proposition** | `id` NEW | `id`; structural equality over `(mood, subject, predicate, value, when, scope)` is the **fallback** | yes | the Person who uttered it | **uttered inside an ordinary act** — no constructor | never; it persists as long as anything names it | yes | **yes** |
| **Case** | `id` NEW | `id` | one sitting | its holder | pleading at a venue | the sitting closing | yes | no |
| **Ground** | `id` NEW | `id` | one sitting, **unless struck** | its Case | pleading | **`strike` — dead at every venue for everyone** | yes | no |
| **Venue** | — | `(rung, prize, standing_date)` | yes | its Rung or Office | authored | — | ⛔ | no |
| **Date** | `id` NEW | `id` | yes | Rung or Office | charter arithmetic; a convening condition; `convene` | passing; the holder effaced | yes | no |
| **DocketItem** | `id` NEW | `id` | one date | its Date | **`carry`**, NEW | the date passing; the matter decided | yes | no |
| **Petition** | `id` NEW | `id` | across seasons | its petitioner | produced by need exceeding own reach | lapse; supersession; **⚠ at a rootless vacant office, never — S19** | yes | no |
| **Dispensation** | `id` NEW | `id` | permanent until countermanded | its issuer | `issue` | a countermanding dispensation | yes | no |
| **Record** | `id` NEW | `id` | yes | its Rung, as matter | authored; written by an act | **`efface`** | yes | no |
| **ConveningCondition** | `id` NEW | `id` | yes | Rung or Office | `convene`'s first operation | struck by another act | yes | no |
| **Sensation** | **none, deliberately** | — | one `choose` call | **nobody** | `sense`, at DELIBERATE | discarded | **NO, BY DESIGN** | no |
| **View** | none | value, per person per question | one `choose` call | nobody | `assemble` | discarded | no | no |
| **World** | — | the whole state | — | — | — | — | no | no |
| **Envelope** | — | `(rung)` — one per Rung | yes | its Rung, as matter | authored at world-gen | its Rung effaced | ⛔ | no |
| **Stores** | — | `(rung, MatterKind)` | yes | its Rung, as matter | `yield`, `transfer` | consumption | yes | no |
| **MatterKind** | `name` | `name` | permanent | world authoring | authored | never | yes | no |
| **Practice** | `name` | `(person, name)` | yes | its Person | `02:153` | — | yes | no |
| **Candidate** | none | value | one `choose` call | nobody | `opening_set` | discarded | no | no |
| **Contest** | none | `(rung, prize, tick)` | one tick | — | the conflict rule; `SUP:327`, `SUP:1141` | — | yes | no |

### §1.1 Five identity facts worth stating on their own

1. **The prior brief declared ZERO identifier fields across eleven record definitions**, while the
   design it inherits **consumes eight id-shaped things it never mints** (§3.4). Every row above now
   carries one, and they all come from one place: `id = H(world_seed, tick, subject_id, purpose)`.
2. **`Tenure` is the row that matters most.** Every disputable political fact — *Aldwin holds the
   praefecture*, *Mereth is sworn to the Restoration*, *the Row was annexed* — **is a Tenure.** Without
   an id it cannot be a `Claim.subject`, and *the design's central thesis does not reach the object the
   politics is made of.*
3. **`until?` is what makes destruction leave a trace.** With `since` alone, re-conferral after
   revocation is indistinguishable from an unbroken tenure and `entrenchment` (`ABS:555`) has nothing
   to read.
4. **`Sensation` is the one object deliberately given no identity**, and the consequence is written down
   rather than discovered: **it is un-nameable, therefore undisputable.** No person can hold a claim
   about another person's hunger. Claims reach the larder and the body and stop.
5. **A Claim's address is two-part** — `(ledger owner, claim id)` — because a claim exists only inside
   one ledger. Nothing in the corpus states this and `inferred(claim_id…)` requires it.

---

## §2 · THE TYPE CATALOGUE

Every record, every field. **Closed sets are enumerated in full.** `⛔` = **not stated in any document
this suite read** — see §0.3's scope warning.

### §2.1 The four carriers

```
Person    := (id, weight, marks, capability, stance, ledger, ties)   -- ONE tuple. weight >= 1.
                                                                     -- weight > 1 IS a cohort.
Rung      := (id, kind, stake[], judging_set_rule, dates[], matter, envelope)
Office    := (id, post, rung?, remit, conferral, revocation, establishment,
              dates[], upkeep)
Site      := (id, rung, kind, condition, drawers[])
```

| field | type | range | notes |
|---|---|---|---|
| `Person.address` | derived from the `contain` Tenure | a path to the root | ⚠ **the edge wins and the field is a VIEW.** The prior brief kept both, giving two homes for one fact and two update paths, only one of which the conflict rule sees. `SUP:368`'s own precedent: *"Who holds the praefecture is a **query**, not a field."* |
| `Person.marks` | 6 kinds, §2.7 | per kind | ascribed, publicly read |
| `Person.capability` | attributes 1–7 · practices 0–5 | pool 1–12 | `SUP:498-505` |
| `Person.stance` | `map[referent → (valence, weight, provenance)]` | valence −5..+5, weight 0..5 | `ABS:73`; `provenance` is claim ids |
| `Person.ledger` | `[Claim]` | budget `L`, `ABS:641` gives 200 as ASSUMPTION | evicted at WITNESS |
| `Person.ties` | derived from `tie`/`knot` Tenures | — | same view/edge ruling as `address` |
| `Person.weight` | integer | **≥ 1, default 1** | **at weight 1 the record IS a person; above 1 it is a cohort** — no conversion operation (`02:553-555`). **This is the one-type guarantee, and it is what prevents elite-only politics by construction.** ⚠ *An earlier version of this catalogue printed two tuples while claiming no conversion existed* |
| `Rung.kind` | the ladder, §2.7 | 7 rungs, extensible | `SUP:96` |
| `Rung.stake[]` | contested material stakes | — | `SUP:322-325` |
| `Rung.judging_set_rule` | a rule, not a set | — | the set is `judging_set(c)`, §5 |
| `Rung.matter` | ⚠ **must be STRUCTURED, not one untyped field** | — | it is asked to hold five distinct kinds — Sites, `stores`, the envelope, Records, the transmission pointer — and four of the five are addressed **by name** from elsewhere. A field with no declared structure cannot be indexed |
| `Rung.envelope` | `Envelope` | — | matter; **does not act**. ⚠ **It is named as its own field rather than folded into `matter`, deliberately: `matter` is the untyped-and-must-be-structured field of the row above, and the envelope is addressed by name from person-minting.** Listing it twice would be the two-homes defect |
| `Office.rung?` | `Rung \| null` | — | **null is the office-cluster case** and S19's home |
| `Office.remit` | `(acts[], scope_rung, binds)` | `acts[]` from the closed five | `SUP:417-424` |
| `Office.conferral` | names a **Rung**, a **parent Office**, **or the office's own judging set** | — | AMENDED, `ARCH §7` F3; the third limb is what closes S19 |
| `Office.revocation` | a rule | — | ⚠ the prior brief dropped it; restored |
| `Office.establishment` | `[Person]` | — | **the office's throughput** under one-act |
| `Office.upkeep` | `Stores` | — | ⛔ magnitude unstated |
| `Site.condition` | float | `[0,1]` | **primary state, written at RESOLVE only** |
| `Site.drawers[]` | `[Person]` — including records at `weight > 1` | — | the denominator of `share(actor, site)` |

⚠ **`seat_items` is DELETED** from `Office` (`SUP:416`'s nine-field form). It and `capacity(date)` are
one quantity seen from two sides (`ARCH §7`, D-2).

### §2.2 The one edge

```
Tenure := (id, subject, object, kind, since, until?, conferrer?, degree?, payload?)
   subject   ∈ Person | Rung | Proposition
   object    ∈ Person | Rung | Office | Site | Proposition
   conferrer ∈ Person | Office | null
   kind      ∈ hold | commit | contain | succeed | tie | knot | oblige     -- SEVEN
```

**Per-kind optionality and cardinality — the table the flat tuple cannot express:**

| kind | subject → object | `degree?` | `conferrer?` | `payload?` | **cardinality** |
|---|---|---|---|---|---|
| `hold` (office) | Person → Office | — | required | — | **1 per Office object** |
| `hold` (ground) | Person \| Proposition → Site \| Rung | — | required | — | **1 per object** |
| `commit` | Person → Proposition | **required, 0–5** | — | `avowal` | 1 per (subject, object) |
| `contain` | Person → Rung; Rung → Rung | — | the admitting person, or null at world-gen | — | **1 per subject** |
| `succeed` | Rung → Person | — | the naming person | — | **1 per Rung subject** |
| `tie` | Person → Person | — | null | `(familiarity, last_contact, channel_class)` | 1 per unordered pair, **stored at the lower id** |
| `knot` | Person → Person | — | null | `(depth ∈ {1,2}, strain)` — **one SHARED gauge** | 1 per unordered pair, **stored at the lower id** |
| `oblige` | Person → Person | — | kinship, admission or oath | — | 1 per (subject, object) |

⚠ **`avowed?` is DELETED as a field.** It appeared once with no producer, reader or meaning, written as
an optional flag over a domain that ships **three** states. It is `commit`'s payload:
`avowal ∈ {avowed, private, covert}` (`ABS:239-240`).

⚠ **`payload?` is an ADDITION beyond the eight named fields, and it is flagged rather than smuggled.**
`knot`'s `depth` and shared `strain` and `tie`'s three fields have no home in the named eight, and
`bandwidth(k) = max(0, 2 − floor(strain/3))` reads `strain` every season (`ABS:502`). Storing a
**shared** gauge on a **directed** record twice lets it disagree with itself, which is why the record is
stored once at the lower id.

### §2.3 The one act

```
StateChange := (subject, mode, driver, field?, delta?, spec?)
   mode    ∈ mint | alter | efface                          -- CLOSED, 3
   driver  ∈ Act | Event                                    -- the SUBJECT decides which is legal

Act    := (id, actor, verb, changes[], reads[], contests[], payload)   -- a character's choice
Event  := (id, kind, subject, changes[], emitted_at)                   -- the world acting on itself
spec   := (type, kind?, parent, initial[], slot)            -- mint only
```

> **THE PARTITION (Jordan).** A state change whose **subject is peninsular human society** — polities,
> institutions, offices, organizations, occupations, religion, settlements, marriage — is **driven by a
> character's choice, always.** A state change whose subject is anything else — weather, the
> non-peninsular, tears in the metaphysical substrate — is **an event acting on the world.** **The mode
> is orthogonal: events create and destroy too, within their half.**

⚠ **`read` and `exclude` are NO LONGER MODES.** They were not state changes. `reads[]` is a declaration
on the Act so the conflict rule can see a dependency; `contests[]` is a claim on contention — what
`exclude` meant — which routes the act to `contest`. **An Event carries `changes[]` only**: it does not
read, because it is not deciding, and it does not contest, because it is not an agent.

| field | notes |
|---|---|
| `verb` | **domain OPEN by construction, and the resolver never branches on it** — nor on an Event's `kind`. A verb is a bundle of `changes` with an eligibility predicate and an obstacle composer; an event kind is a bundle of changes plus a locus. `remit.acts`' closed five is **not** the act vocabulary — it is the set an office's remit makes eligible where it otherwise is not |
| `field?` | null for `read`, `exclude`, `efface`. **Required for `alter`**, because the conflict rule quantifies over a field |
| `delta?` | the signed amount, for an `additive` field |
| `spec.slot` | the index that makes the minted id computable: `H(world_seed, tick, actor_id, "mint:" + slot)` |
| `payload` | ⛔ untyped in every surface |

**Commutativity** is declared **on the field, where the field is declared**: `additive` (all writers
apply — `condition`, `stores`, envelope weights) vs `exclusive` (contested — a succession pointer, an
office's remit, an address). **The default for an undeclared field is `exclusive`.** ⚠ `additive` is
order-independent **only under batching**: the resolver sums a season's deltas per field and applies the
clamp **once**.

### §2.4 Knowledge

```
Claim       := (id, subject, predicate, value, when, source, confidence, visibility)
source      ∈ firsthand(event_id) | told_by(person | record, handle)
            | inferred(claim_id…) | firsthand_via_knot(event_id)        -- CLOSED, 4
Proposition := (id, mood, subject, predicate, value, when, scope)   mood ∈ HOLDS | OUGHT
Case        := (id, holder, motion, rung, grounds[])
Ground      := (id, proposition, warrant, support[])                -- claim ids
Record      := (id, rung, kind, forgery_quality, subject_matter)
               kind ∈ register | charter | deed | roll | letter
Sensation   := (subsistence, standing)                              -- TWO scalars
```

- **`when` is a mandatory closed interval and is universal, never existential** (`SUP:223-226`).
- **Claims collide iff same subject, same predicate form, same arguments, intersecting `when`,
  incompatible values** — computed at deposit time, **in one ledger at a time** (`SUP:228-229`).
- **The predicate vocabulary is CLOSED; the referent space is OPEN** (`SUP:231-234`). **Its membership
  is enumerated in full at `03:66-79` — FOURTEEN forms**, listed in §2.7, with **one entailment table
  and no grammar**, and a stated test for a fifteenth: *is the new form already being deposited
  somewhere in this design?* ⚠ *An earlier version of this row said the membership was enumerated
  nowhere, with `SAID` as its one worked example.*
- **Negation is a VALUE, not a form** (`03:100-101`), which is why assert and deny land on the same row
  and collide by computation rather than by a coincidence of naming.
- ⚠ **THERE IS NO FIFTH SOURCE.** An earlier version of this suite added `documented(record_id)`.
  **`03:528` already ships it**: `research(archive, question)` produces **`told_by(record, …)` with
  VERIFIED rootprints**, and archives are *"the only non-person root-bearers"*. **A record is a speaker
  that cannot lie and cannot be interviewed** — its rootprint is *verified* where a person's is
  *asserted*, and that is the entire difference.
- **Closure is PROVED, not asserted** (`03:432-464`): `firsthand` mints and needs an event and a
  witness with vantage; `told_by` **copies**; `inferred` **unions** and **refuses an empty union**;
  `firsthand_via_knot` **reuses** the originating event's id. **There is no path to an empty ancestry,
  so repetition cannot become corroboration** — a rumour told three times hashes to one synthetic root
  and the multiplier stays 1.0.
- ⚠ **`Sensation` carries TWO scalars, not four.** Only `subsistence` and `standing` read the world
  (`SUP:187-188`); `commitment` and `exposure` read the **view** (`SUP:189-190`) and are computed inside
  `choose` from claims already held.

### §2.5 Calendar, up-stroke, down-stroke

```
Date               := (id, holder, form, when, capacity, convener_office?, docket[])
                      holder ∈ Rung | Office
DocketItem         := (id, date, matter, placed_by, placed_at)
                      matter ∈ Petition | Motion | Report | Conferral | Determination
Petition           := (id, petitioner, proposition, respondent, backing[])
                      respondent ∈ Rung | Office
ConveningCondition := (id, holder, predicate, date_form, set_by, set_at)
   -- SIX fields. `SUP:710` ships FIVE: (holder, predicate, date_form, set_by, set_at).
   -- `id` is this suite's addition, per §2.2's rule that every record carries one.
                      date_form = (venue, horizon, convener office)
Dispensation       := (id, issuer, proposition, scope, terms)
Venue              := (rung, prize, standing_date, judging_set_rule, decision_rule,
                       admission_floor, privileged_custody, exchange_budget, article_count,
                       coupling_depth, veto_holders, record_custody)
door               := (convener, enter, speak, admissible_source, attendance_cost)
```

⚠ **`Venue` is a TWELVE-field tuple plus a FIVE-field door** — seventeen only if the two are folded, and
they are separate objects. **Eight of the seventeen appear exactly once in the corpus and carry no
value.** §8 and §11.

### §2.6 Matter

```
Stores     := map[MatterKind -> quantity]                        -- AMENDED, ARCH §7 F2
MatterKind := (name, perishability, bulk, edible)
Envelope   := (rung, counts_by_age_band[], marks_bundle, capability_distribution)
```

**`edible` is what stops silver satisfying hunger, and it is a field, not a resolver case.** ⛔
`counts_by_age_band`'s band boundaries are not stated in any document this suite read.

### §2.7 Every closed set, enumerated

| set | members | count | source |
|---|---|---|---|
| **`StateChange` modes** | **mint · alter · efface** | **3** | AMENDED. `SUP:689` ships `read \| alter \| exclude`; an earlier version of this suite made it five by adding `mint`/`efface` as act modes. **Jordan's partition makes them modes of a change with two drivers**, and `read`/`contest` are re-sited off the mode set entirely |
| **change drivers** | **`Act` (a character's choice) · `Event` (the world acting on itself)** | **2** | NEW — Jordan's partition. **The subject decides which is legal** |
| **`Tenure` kinds** | hold · commit · contain · succeed · tie · knot · **oblige** | **7** | AMENDED |
| **write classes** | CALENDAR · MATTER · ACTS · **INTERIOR** | **4** | AMENDED from `SUP:661-678`'s 3 |
| **loop steps** | CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS | **6 steps, 4 barriers** | AMENDED from `SUP:641-654`'s 8 labels |

| **stance referent kinds** | Person · Proposition · **Place (= Rung \| Site)** | **3** | AMENDED from `ABS:188`'s 4; `Faction` and `Proposition` denoted the same thing after `ARCH §2.7`, and `Place` was not defined in any document this suite read |
| **the owner table** | Person · Rung · Office · **Nobody** | **4** | AMENDED from `SUP:334-340`'s 5; the Faction row is deleted and re-homed |
| **`remit.acts`** | issue · determine · confer/revoke · dispatch · convene | 5 | SHIPPED, `SUP:421-424` |
| **`convene`'s two operations** | setting a date · ordering its items (`compose_agenda`) | 2 | SHIPPED, `SUP:426-431` |
| **`binds`** | members-by-admission · persons-by-presence | 2 | SHIPPED, `SUP:418` |
| **containment ladder** | Person → Hearth → Community → Settlement → Territory → Province → Realm | 7, extensible | SHIPPED, `SUP:96` |
| **degree bands** | Disaster (≤−2) · Failure (−1) · Costed Success (0) · Clean (+1,+2) · Overwhelming (≥+3) | 5 | SHIPPED, `SUP:540-546` |
| **dispensation terms** | Price · Prohibition · Levy · Exemption · EntryStandard · Excommunication · Blockade · TreatyClause · Ordenanza | 9 | SHIPPED, `SUP:1123-1125` |
| **stasis ladder** | Denial · Definition · Quality · Jurisdiction | 4, strongest first | SHIPPED, `SUP:1525-1527` |
| **the twelve faults** | F1 self-contradiction `close` · F2 contradicting the record `descend` · F3 silence when pressed `close` · F4 shifting the ground `descend` · F5 repetition `strike` · F6 the quibble `close` · F7 rootless ground `strike` · F8 conceding and pressing anyway `close` · F9 deficient pleading `close` · F10 speaking without standing `strike` · F11 incoherent assertion `strike` · F12 inadmissible challenge `descend` | 12 | SHIPPED, `SUP:1536-1540` |
| **fault severities** | `strike` kills the ground at every venue for everyone · `descend` concedes a rung and **closes nothing** · `close` force-closes the sitting against the faulting party | 3 | SHIPPED, `SUP:1540-1542` |
| **proposition mood** | HOLDS · OUGHT | 2 | SHIPPED, `SUP:1514` |
| **need kinds and what each reads** | subsistence → **world** · standing → **world** · commitment → **view** · exposure → **view** | 4 | SHIPPED, `SUP:185-190` |
| **larder bands** | Provisioned → Sufficient → Thin → Hungry → Failing | 5 | SHIPPED, `SUP:1407` |
| **commitment ladder** | 0 none (w 0) · 1 sympathy (0.15) · 2 sympathiser (0.40) · 3 member (1.00) · 4 sworn (1.60) · 5 constitutive (2.20) | 6 | SHIPPED, `ABS:230-237`; ⚠ its licence column is *"live in two contradictory states"* |
| **avowal** | avowed · private · covert | 3 | SHIPPED, `ABS:239-240` |
| **mark kinds** | heritage · house · grade · church · office · sensitivity | 6 | SHIPPED, `ABS:195-203` |
| **mark legibility** | open · attested · latent | 3 | SHIPPED, `ABS:206` |
| **resolution strata** | movement · binding decisions at docket dates · contested physical acts · uncontested material acts · **social acts last** | 5, ordered | SHIPPED, `SUP:695-698` |
| **fidelities** | played · witnessed · auto — *differ only in who is asked to choose* | 3 | SHIPPED, `SUP:617-620` |
| **carrier choices at the rung above** | forward · amend · bundle · drop | 4 | SHIPPED, `SUP:894-895` |
| **channels open to a person with no office** | requisition kin · petition · take an opening · migrate · commit to a rival proposition | 5 | SHIPPED, `ABS:264` |
| **decider-free exceptions** | metabolism and nature · matter events · the confidence of a memory decaying · **the calendar, LAPSE ONLY** | 4 | SHIPPED, `ABS:269-277` |
| **clock-driven quantities** | matter · bodies · the confidence of a memory | 3 | SHIPPED, `ABS:280` |
| **individuation triggers** | Named · Spread · Divergent view · Capability demand | 4, exhaustive | SHIPPED, `02:543-552` — **RULED over `09:535-537`** |
| **person-generation triggers** | individuation · a succession pointer resolving to an heir who does not yet exist · an admission act needing a candidate · a petition needing a carrier at a rung with no live person · a view assembly requiring a subject the observer is looking at | 5, exhaustive | SHIPPED, `02:573-576` — **RULED** |
| **de-individuation predicate** | no Knot **and** no office **and** no live petition **and** no other person's ledger names them | 4 clauses, conjunctive | SHIPPED, `SUP:209-210` |
| **knot rupture triggers** | strain +5 · public betrayal of counsel · the partner's death · a Fell/Dissolution op targeting the partner · both partners' primary Conviction rows crossing to opposite sign on a shared referent · deliberate severance | 6 | SHIPPED, `ABS:302` |
| **what a Knot adds over a maxed tie** | unbidden deposit · Composure buffering · counsel extraction · Coherence contagion | 4 | SHIPPED, `ABS:305` |
| **manoeuvres at declaration** | reframe the pool source · contest the venue not the fight · escalate the stake · draw aid from a Knot | 4 | SHIPPED, `ABS:308` |
| **force forms** | seize · restrain · strike · burn · expel · disperse · kill | 7 | SHIPPED, `ABS:261` |
| **predicate forms** | `LOCATED`(subject, place) · `DID`(actor, act_kind, object) · `HOLDS`(person, office \| holding \| mark) · `MARKED`(person, mark) · `CONDITION`(subject, condition) · `ALIGNED`(person, faction, degree_band) · `TIED`(person, person, tie_kind) · `QUANTITY`(rung, stake, band) · `IN_FORCE`(rung, proposition) · `INTENDS`(person, proposition) · `SAID`(speaker, claim, when, place) · `CAUSED`(event\|act, event\|act\|condition) · `CONTRADICTED`(source, source) · `HOLDS_STANCE`(person, referent, valence_band) | **14** | SHIPPED and **enumerated in full at `03:66-79`.** `03:81`: *"Fourteen forms, and the count was twelve until this document was audited against its own use."* ⚠ **An earlier version of this compendium called this set unenumerated with `SAID` as its one worked example. See `ARCH §12.8`** |
| **claim source constructors** | `firsthand(event_id)` · `told_by(person \| record, handle)` · `inferred(claim_id…)` · `firsthand_via_knot(event_id)` | **4** | SHIPPED, `SUP:243-245`, `03:411-413`. ⚠ **An earlier version of this suite added a fifth, `documented(record_id)`. It was a reinvention: `03:528`'s `research` already produces `told_by(record, …)` with VERIFIED rootprints, and archives are *"the only non-person root-bearers"*. Withdrawn** |
| **investigative acts** | `examine` · `interview` · `research` · `surveil` · `reconstruct` · `Thread-Read` | **6** | SHIPPED at `03:526-531`, each with a pool, a product and a cost. ⚠ **An earlier version invented a single `investigate` verb "built here entirely from existing parts"** |
| **deception deltas** | sincere (δ=0) · **lie** (value flipped) · **overclaim** (confidence inflated) · **false witness** (provenance inflated) · **invention** (content absent from ledger) | **5** | SHIPPED, `03:243-249`. *"One act, one delta, four behaviours. No liar flag, no deception stat"* |
| **visibility** | `open` · `discreet` · `concealed` | **3** | SHIPPED, `03:628`. One field, two application sites — on an act it hides the deed; on a channel it is `withhold` |
| **channel dispositions** | **approve** · **suppress** · **surface** | **3** | SHIPPED, `03:635-644`. *"Surfacing is more powerful than suppressing and leaves less trace"* |
| **the empty-view ladder** | marks-based expectation (0.35) · rumour draw (0.2) · what he believes his neighbours hold (0.25) · **the option leaves the act list** | **4, ordered** | SHIPPED, `03:377-407` |
| **the fourteen refusals** | §2.8 | 14 | SHIPPED, `SUP:1732-1747` |
| **refusals outside the fourteen** | no apparatus · no threshold firing an outcome / stored gauge / second resolver / pushed aggregate · variable not threshold | 3 | SHIPPED, `SUP:1749-1765` |
| **structural tests** | no decision function can see the world · two witnesses of one event can disagree · a person with no office can act, petition and receive an opportunity · order independence | 4, **none run** | SHIPPED, `SUP:1767-1770` |
| **the thirteen Convictions** | Faith · Authority · Order · Scholastic · Utility · Equity · Liberty · Precedent · Community · Identity · Warden · Virtue · Honor | 13 | SHIPPED, `ABS:192` |

### §2.8 The fourteen refusals, and where each new object was walked

Full walk at `ARCH §9`. **Eleven new objects × fourteen rows each, plus a twelfth walk for the EVENT
driver of `mint`/`efface`** — because the ten original objects were walked against those modes **as act
modes only**, and Jordan's partition gives them a second driver.

> **THE UNCLEARED VERDICTS ARE FOUR, ACROSS TWO ROWS**: row 4 once (`Site`), row 11 three times
> (`Site`'s `exclude` limb, act-driven `efface`, `Record`'s `efface` limb). **Every other cell of
> 11 × 14 + 14 clears.** ⚠ *An earlier version of this index disagreed with the walk it indexes.*

| # | forbidden | objects walked against it | not cleared |
|---|---|---|---|
| 1 | a `World` parameter on any decision function | all ten | — |
| 2 | a `view_of(world, person)` that masks rather than assembles | all ten | — |
| 3 | any function taking `[Person]` and one `Event` | all ten | — (Record's near-crossing is closed by the gate) |
| 4 | a deposit into a cohort carrying a VALUE rather than a DISTRIBUTION | all eleven, **plus the event driver** | ⚠ **Site (1)** — the construal-spread rule is under-specified upstream at `SUP:1737`. ⚠ **And `03:196-209` supplies most of what it needs and was unread: a cohort claim stores *"the share distribution over the construal set, not the argmax"*, and an individuating member DRAWS from it** |
| 5 | a pushed aggregate, or a field one is stored in | all ten | — |
| 6 | a stored aggregate, norm, density, unrest or reputation field | all ten | — |
| 7 | a knowledge value stored on the thing known | all ten | — |
| 8 | a second resolver, an auto-resolve formula, a fast path | all eleven, **plus the event driver** | **none.** ⚠ *The `R ≤ 1` obstacle branch is carried open at §11; it is a question about the SHIPPED obstacle formula, not a verdict in this walk, and an earlier version of this index listed it here* |
| 9 | a `tier`, `level` or `scale` field on a faction | all ten | — |
| 10 | a flat additive modifier from a person onto a roll | all ten | — |
| 11 | a personal effect on a group that is not a fraction of that group | all ten | ⚠ **`efface`** — the discrete limb, inherited and **widened by four object classes** |
| 12 | a scheduled recovery tick on standing | all ten | — |
| 13 | a per-entity branch anywhere in the resolver | all ten | — |
| 14 | an authored per-person opportunity or quest object | all ten | — |

---

## §3 · THE REFERENCE MAP

### §3.1 Who points at whom

| # | referrer.field | → target | declared | on target's destruction |
|---|---|---|---|---|
| 1 | `Tenure.subject` | Person \| Rung \| Proposition | `ARCH §2.3` | `until = tick`; **the Tenure survives as a historical fact** |
| 2 | `Tenure.object` | Person \| Rung \| Office \| Site \| Proposition | `ARCH §2.3` | as above |
| 3 | `Tenure.conferrer` | Person \| Office \| **null** | `ARCH §2.3`, `ARCH §7` F1 | as above; **null is legal for `tie`/`knot`** |
| 4 | `Act.actor` | Person | `ARCH §2.4` | ⛔ an act declared by a person who dies at MATTER of the same season — resolution unstated |
| 5 | `touch.target` | any object id, or a `spec` | `ARCH §2.4` | **this is the destructor itself** |
| 6 | `Office.rung?` | Rung \| **null** | `ARCH §2.1` | null is the cluster case; F3 supplies the clock |
| 7 | `Office.establishment` | `[Person]` | `ARCH §2.1` | per member; a dead member no longer sources a pool |
| 8 | `Office.conferral` | a Rung, a parent Office, **or the office's own judging set** | `ARCH §7` F3 | **may cycle** — §3.4 |
| 9 | `Rung.matter` | Sites, `stores`, Records, the transmission pointer | `ARCH §2.1` | ⚠ **must be structured to be indexable** |
| 10 | `Rung.envelope` | one Envelope | `ARCH §2.6` | — |
| 11 | `Rung.dates[]` / `Office.dates[]` | Dates, each naming a convener office | `SUP:337-339` | dangles when the office is effaced |
| 12 | `Person.address` | **a VIEW of the `contain` Tenure** | `ARCH §2.1` | derived; no second update path |
| 13 | `Person.ties` | **a VIEW of the `tie`/`knot` Tenures** | `ARCH §2.1` | derived |
| 14 | `Person.ledger` | Claims | `ARCH §2.1` | owner-scoped; **cross-person `efface` forbidden** |
| 15 | `Person.stance[referent]` | Person \| Proposition \| Place; `provenance` = claim ids | `ABS:73` | dangles on both axes |
| 16 | `Claim.subject` | the open object namespace, **including other Claims** | `SUP:229-234` | dangles |
| 17 | `Claim.source` | `event_id` \| `(person, handle)` \| `claim_id…` \| **`record_id`** | `ARCH §5.4` | **the record limb degrades confidence rather than dangling** |
| 18 | `Ground.support[]` | claim ids in the holder's ledger | `SUP:1516` | dangles |
| 19 | `Date.docket[]` | DocketItems | `ARCH §5.5` | the item dies with the date |
| 20 | `DocketItem.matter` | Petition \| Motion \| Report \| Conferral \| Determination | `ARCH §5.5` | — |
| 21 | `Petition.respondent` | Rung \| Office | `SUP:840-841` | **a vacant office is a legal respondent** |
| 22 | `Petition.backing[]` | `[Person]` — including records at `weight > 1` | `SUP:843-845` | per backer |
| 23 | `Site.rung` | Rung | `ARCH §2.1` | effacing a Rung effaces its Sites |
| 24 | `Site.drawers[]` | `[Person]` — including records at `weight > 1` | `ARCH §2.1` | recomputes `share` |
| 25 | `ConveningCondition.holder` | Rung \| Office | `ARCH §5.12` | dies with the holder |
| 26 | `Dispensation.scope` | `[Rung]` | `SUP:1121` | per Rung |
| 27 | substream tuple | `(world_seed, tick, subject_id, purpose)` | `ARCH §2.2` | **`subject_id` now resolves — every record carries one** |

### §3.2 The inverse index — for each object, everything that points at it

**Nothing else in the corpus has one.** Every entry below is derived on demand, stored nowhere.

| object | pointed at by |
|---|---|
| **Person** | 1, 2, 3, 4, 7, 15, 17 (`told_by`), 21, 22, 24; `succeed` objects; every `tie`/`knot`/`oblige` endpoint |
| **Rung** | 1, 2, 6, 11, 21, 23, 25, 26; every `contain` object; `hold`-of-ground objects |
| **Office** | 2, 8, 11 (as convener), 21; every office `hold` |
| **Site** | 2, 23, 24; `yield`'s `site(H)`; `share(actor, site)` |
| **Proposition** | 1, 2 (`commit`), 15, 20, 26; `Ground.proposition`; `norm(c, prop)` |
| **Claim** | 15 (`provenance`), 16, 17 (`inferred`), 18 |
| **Event** | 17 (`firsthand`, `firsthand_via_knot`) |
| **Record** | 17 (`told_by(record, …)`) — **and this edge is the purge limb's whole mechanism** |
| **Date** | 11, 19; `ConveningCondition.date_form`; `capacity(date)` |
| **Tenure** | ⚠ **nothing pointed at a Tenure in the prior design, which is why it could not be disputed.** Now: `Claim.subject`, `Ground.support[]`'s subject matter, and `entrenchment` |

### §3.3 Dangling, orphans, and the one rule that covers both

> **THE GENERAL RULE, generalised from the one place the prior design got it right: AN EFFACED
> REFERENT DEGRADES WHAT POINTS AT IT; IT NEVER ORPHANS IT.**
>
> `SUP` applies this to exactly one object out of seven — effacing a record *"removes the corroborating
> source"* rather than deleting the citing claims. **Suppression is a confidence attack, not a
> deletion.** That is the right answer for every row of §3.1, and it is stated once here.

**Applied:**

| effaced | what happens |
|---|---|
| **Person** | `until = tick` on every Tenure they held; a conferral Date opens; the `succeed` pointer resolves. **Claims about them survive at existing confidence until their holders learn** (`SUP:1188-1198`) |
| **Rung** | **its `contain` children MUST be re-parented in the same act.** There is no orphaning operation — a person's address is their path to the root, and a bare `revoke` on `contain` leaves them with none |
| **Office** | `until` on every `hold`; its Dates lapse; petitions filed at it wait |
| **Site** | `until` on every `hold`; it leaves `drawers`' `share` denominators; `condition(c)` no longer sums over it |
| **Proposition** | it is **never effaced** — it persists as long as anything names it |
| **Claim** | evicted from its own ledger only. **Cross-person `efface` is forbidden** (R-2) |
| **Record** | claims citing it keep their content and lose corroboration — **gated on a claim of the loss reaching each holder** |

**Two guards already exist in the design and are named so nobody re-invents them:**

1. **De-individuation is refcounted** — *"no other person's ledger names them"* (`SUP:209-210`). It is
   the only refcount in the design, and it guards the **merge** path, not the `efface` path.
2. **A dangling `succeed` pointer is repaired by generation, not by integrity** — person-generation
   trigger 2 is *"a succession pointer resolving to an heir who does not yet exist"* (`02:574`). **The
   design's answer to one dangling reference is to mint the missing referent.** A real, citable pattern
   that does not scale to the other rows.

**Orphan classes, and what detects each:**

| orphan | arises when | detected by |
|---|---|---|
| Person with no `contain` edge | **cannot arise** — migration and secession are `confer` to a different parent, atomically | the cardinality declaration |
| Rung with no parent | the root | ⚠ **`sovereign_fraction(root)` presumes one root and the design declares no root-uniqueness invariant.** `SUP:475-478` rules that a contested succession undefines *the choice of root, not the function*, so **root-plurality is a political condition callers must handle** |
| Office with `rung = null` | by design — the cluster | F3's conferral-completeness requirement gives it a clock |
| Tenure whose endpoint is effaced | any `efface` | `until` is set; the Tenure becomes history |
| Site whose Rung is effaced | Rung `efface` | the cascade above |

### §3.4 Cycles

| cycle | reachable | what holds |
|---|---|---|
| `contain`: Rung → Rung → … | **NO, and this is a change.** The cardinality declaration is stated over **`contain` subjects generally**, not over Persons only | `SUP:97-98`: *every person exactly one parent hearth; every hearth exactly one community.* The prior brief scoped single-parent to Persons and thereby licensed a multi-parent Rung graph while citing `SUP:94-108` as its authority |
| `succeed ∘ contain`: Rung → Person → Rung | **yes, and it is the NORMAL case** — the heir lives in the hearth | **the reference graph is not a DAG; every traversal needs a visited-set.** Unremarked in the prior design |
| `tie`/`knot`: Person ↔ Person | yes by construction | the record is **stored once, at the lower id**, so the symmetric relation has one home |
| `Claim.subject` → Claim → … | yes — *subjects include other claims* | ⚠ **solved in this repo's substrate and not in the design**: `engine/substrate/keys.py:389-392` gets cycle-freedom **by construction** from an append-only log whose citations may name only already-logged ids, enforced at `keys.py:384-388`. **That mechanism is adoptable verbatim for `Claim.source` and for Tenure history** |
| `inferred(claim_id…)` → Claim → … | yes | as above |
| `Office.conferral` → Office → … | yes | ⚠ **`conferral_path(o) reaches root` (`ABS:55`) — a cyclic path never reaches root, so a cycle SILENTLY EXCLUDES the office from its cluster instead of being detected.** Under F1's per-office basis and F3's completeness requirement this is more reachable, not less. §8 |

---

## §4 · THE FUNCTION CATALOGUE

Columns: printed signature · reads · writes · **write class** · invariant maintained · gaps.

### §4.1 The three signatures

| | `choose` | `resolve` | `witness` |
|---|---|---|---|
| **signature** | `(Person, View, Sensation) -> Act` | `(Act[], World) -> Event[]` | `(Person, Event) -> Claim[]` |
| **reads** | own ledger, stance, capability, remits; the View; two scalars | every object a `touch` names | the Event; presence and channel; the person's ledger for collision |
| **writes** | **nothing but the returned Act** | everything else | **that one person's ledger only** |
| **class** | — | ACTS | INTERIOR |
| **invariant** | **no `World` in scope, ever** — by omission, not by inspection (`SUP:143-147`) | **no `Person` parameter**, so no per-actor special case (`SUP:148-149`); order-independent | **a collection of persons and one Event is a TYPE ERROR** (`SUP:150-151`); the only root-token minter |
| **gaps** | ⛔ the question `q` the View is assembled against has no producer, type or lifetime; ⛔ `Act.payload` untyped | ⛔ `World` is not defined in any document this suite read, including any surface | ⛔ `Event`'s record is defined nowhere; it is known only to carry `id` and the degree band |

**Supporting functions, and why each is legal:**

| function | signature | why it does not break a signature rule |
|---|---|---|
| `sense` | `(Person, World) -> Sensation` | **§14 row 1 bans a `World` parameter on a DECISION function.** `sense` decides nothing — it returns two floats carrying no references and answering no query |
| `assemble` | `(Person, Question) -> View` | reads claims only; **assembled, not filtered** |
| `opening_set` | `(Person, View) -> [Candidate]` | person-side; belief |
| `verbs` | `(Site, Rung) -> Set[Verb]` | **resolver-side**; world truth; never in `choose`'s scope |
| `contest` | `(Rung, Prize, Claimant[]) -> Event[]` | it *is* `resolve`'s conflict route, not a second resolver |

### §4.2 The loop steps

| step | signature | reads | writes | class | gaps |
|---|---|---|---|---|---|
| **CALENDAR** | `(World, date) -> World'` | dates, convening-condition predicates, band memberships | dates, dockets | CALENDAR | a predicate may read own state, an R-1 aggregate, or the calendar — and **nothing else** |
| **MATTER** | `(World) -> World'` | larders, bodies, travel, Sites, envelopes | larders, bodies, travel, `yield`, envelope weights | MATTER | ⛔ `season_factor`'s distribution; **`condition` is NOT written here** |
| **DELIBERATE** | `(Person, FrozenWorld) -> Act`, per person, pure | own interior; the frozen world, through `sense` only | nothing but the returned Act | — | ⛔ the question `q` |
| **RESOLVE** | `(Act[], World) -> Event[]` | everything named by a `touch` | everything else | ACTS | the `R ≤ 1` fast-path branch, carried |
| **WITNESS** | `(Event[], World) -> World'` then `(Person, Event) -> Claim[]` | presence, channels, Knots; own ledger | own ledger only | INTERIOR | ⛔ channel latency values |
| **CENSUS** | `(World) -> World'` | the post-eviction ledger set, **once** | the population | MATTER | ⛔ where the channel store lives |

### §4.3 Act constructors and verbs

**`remit.acts`, the closed five an office's remit makes eligible where they otherwise are not:**
`issue` · `determine` · `confer`/`revoke` · `dispatch` · `convene`. ⚠ **`convene` names TWO distinct
operations and they are separate acts**: *setting* a standing date, and *ordering its items*
(`compose_agenda`). Each costs an act when performed, and performing one is not performing the other.

**Ordinary acts — available to any person subject to their preconditions, and NOT in `remit.acts`:**

| verb | signature | cost | notes |
|---|---|---|---|
| `commit` | `(person, proposition, Δdegree)` | the act | degree → 0 **is** departure; no operation needed |
| `transfer` | `(giver, receiver, amount, kind)` | the act | ⚠ **needs the precondition the design lacks: `stores(hearth(giver), kind) ≥ amount`**, or a negative larder mints matter |
| `carry` | `(person, petition, date)` | the act | precondition: **standing at the respondent** and a claim that the petition exists. **Mints a DocketItem** |
| `compose_agenda` | `(convener, rung, date)` | the act | input is the petitions he **holds a claim of**; admits the top `capacity(date)`; **an omitted petition is a DROP** |
| `requisition` | `(obligor, obligee, act)` | the act | reads an `oblige` edge; **surfaces another person's act as theirs to refuse** |
| `investigate` | `(actor, question, subject)` | the act | resolves to **an Event the actor witnesses** — never a direct deposit |
| `admit` / `migrate` | `(person, rung)` | the act | **`confer` on `contain` to a different parent, atomically** |
| `form_knot` | `(a, b)` | the act | Disposition +5, TS ≥ 30 both, Bonds ≥ 5, free slot (`02:399`) |
| `tell` | `(teller, claim, audience-by-presence)` | the act | distortion in transit is free |
| a `mint`/`efface` act | any verb whose touches carry those modes | the act, plus whatever material the thing requires | founding, building, establishment, razing |

⚠ **`annex` and `secede` are NOT verbs and are deleted.** Zero occurrences in the prior corpus.
Annexation is `confer` of a `hold` Tenure over a Rung. `secede` additionally collides with
`05:594`'s shipped use of *secession* for a duke's **defection**, which is a `commit` moving away.

⚠ **`spend` is deleted** as an argument of `investigate`. It named an unnamed third capacity quantity.

### §4.4 Predicates and formulas

| thing | as stated | gaps |
|---|---|---|
| **conflict** | two acts conflict iff they share a target and either mode is `exclude`/`efface`, **or** both `alter` an `exclusive` field, **or** both `mint` edges that jointly break a declared cardinality | closed by `touch.field`, by the `mint` parent-touch, and by the cardinality table |
| **tiebreak** | `H(act_id, world_seed)` — **never rank, office or list position** | `act_id` now exists |
| **field commutativity** | `additive` vs `exclusive`, declared on the field; **default `exclusive`**; the resolver sums a season's deltas and clamps **once** | — |
| **eviction ranking** | `confidence_live × recency`, and **nothing else** | must be a **different function** from retrieval's `salience`, because **`relevance(c, q)` is defined against a question and eviction has no `q` in scope** |
| **retrieval ranking** | `salience(c) = recency × confidence_live × relevance(c,q) × stanceweight`; `recency = 2^(−age/halflife)`, **halflife 4, or 12 if the subject is a Knot partner, a hearth member or a Conviction-primary referent** (`03:337-339`); `relevance = 1.0` in `q`'s read-set, `0.3` within two graph edges, `0` otherwise (`03:342-344`); `stanceweight = clamp(1 + (obstinacy/5)·agreement, 0.05, 2.0)`. **Ties break firsthand > told_by > inferred, then more recent, then lower claim id — never randomly** (`03:369-372`) | ⛔ `relevance`, ⛔ `q` |
| **view budget** | `K = 7 + Focus + 2 per Knot consulted − Coherence penalty (Dissonant 1 … Severed 5)`; **K = 3 per cohort** | ruled over `09:63`'s flat 12 |
| **substream** | `H(world_seed, tick, subject_id, purpose)` | ⛔ `purpose`'s vocabulary is open; **its stability across runs IS the determinism requirement** |
| **pool** | `Pool = Attribute[relevant] + Practice[practice]`; attributes 1–7, practice 0–5, pool 1–12 | ruled over `10:33`'s 0–7 |
| **die reading (pool)** | N d10; 1–6 nothing, 7–9 one, 10 two; mean `Pool/2`, σ ≈ 0.671/die | for anything with a performer |
| **die reading (magnitude)** | `(3 + d10)/8.5` — `0.47×` to `1.53×`, **mean exactly 1.0**; a bad season is `d10 ≤ 3`, a 30% event | for nature, which has no skill |
| **obstacle** | `if opponent is a person: OPPOSED; R = resistance_pool; if R ≤ 1: 0; else round_half_up(R/2)`; refuse if `Obstacle > 2 × Pool` | ⚠ the `R ≤ 1` branch is a fast path by the review's reading, **carried unruled** |
| **degrees** | `Margin = successes − Obstacle`, five bands | ⚠ **Overwhelming is unreachable at Pool 1–2** — one die yields at most two successes. A property of the arithmetic, not repaired |
| **`Δcondition`** | `−condition × f(degree) × share(actor, site)`; `f` = 0 · 0 · 1/16 · 1/8 · 1/4 | restoration is the mirrored `+(1 − condition) × f × share` |
| **`condition` accumulator** | `clamp(condition + Σ this season's deltas, 0, 1)` — **RESOLVE only, ACTS only** | `base(H)` is constant; weather lives in `yield` |
| **`yield`** | `base(H) × condition(site(H)) × season_factor(territory) × (3 + d10)/8.5` | ⛔ `season_factor`'s distribution |
| **larder** | `mouths = Σ appetite`; `stores += draw − mouths` (**may go negative — a shortfall is a debt**); `margin = stores/mouths`; `draw = Σ yield − Σ levy + Σ transfers_in − Σ transfers_out` | `need(subsistence) > 1.0` **outweighs stance entirely** |
| **advancement** | a rank rises when an attempt at a standard **above** it resolves AND (witnessed by someone holding it higher OR it failed at a cost actually paid). **No experience clock** | ⛔ `standard` is undefined; an **`alter`**, not a `mint` |
| **demotion** | NEW: a rank falls when an attempt at a standard at or below it resolves at **Disaster** AND (witnessed by someone holding it at least as high OR the failure cost something unrecoverable within a season). **No decay clock** | **falsifier: if a rank can fall with no attempt behind it, the clock is back** |
| **entrenchment** | `min(1, seasons_held/60)` | **read off `since`/`until`**, stored nowhere |
| **`carry` regard** | `regard_cost = Σ_{judging set} max(0, −stance(j, prop)) × weight(j)`; `regard_gain = Σ_{backers WHO LEARN} stance(b, prop) × weight(b)` | **both limbs are required** — `regard_gain` is what breaks omission's dominance |
| **grievance deposit** | `m = shortfall_at_raising × weight × amplification(chain)` | **the telling's grammar decides where the grudge lands** — a claim naming an actor deposits on him; one naming only the rung deposits on the rung |
| **bandwidth** | `max(0, 2 − floor(strain/3))` | reads the knot payload's shared gauge |
| **person minting** | address from the cohort · marks from the cohort **plus its variation** · capability from its distribution **conditioned on the naming event** · stance from its aggregate **plus dispersion** | ⚠ two different conditionings; the prior brief flattened them |

---

## §5 · THE DERIVED CATALOGUE

> ### ⚠ EVERY RESOLVER-SIDE QUERY TAKES `World` AS ITS FIRST PARAMETER, AND THAT IS THE ENFORCEMENT
>
> GDScript has no module system and no way to scope an identifier out of a function body, so omitting
> `World` from `choose` makes world access **unwritten, not unwritable** (`ARCH §3.1a`). **The repair
> is to make the world a value that must be passed**: with `World` as parameter one, calling a
> resolver-side query from inside `choose` **fails at the call site for want of an argument.** Twelve
> signatures plus one rule — *no live world state behind any global name* — take enforcement-by-omission
> from **3 signatures to 23**, and turn the **side** column below from a table a reader must honour into
> a call-site impossibility. **Person-side queries take no `World` and must never acquire one.**

**Kept separate from §4 deliberately: a Query never writes and is never stored, and merging them is how
a query becomes a field.** The **side** column is the design's central rule — a **resolver-side** query
may read true state; a **person-side** query may read only the asking person's ledger.

| # | name | signature | side | range / units | reads | replaces | gaps |
|---|---|---|---|---|---|---|---|
| 1 | `faction` | `Proposition → Set[Tenure]` | resolver | a set | all `commit` Tenures | a stored faction object | needs the object-side inverse index (§3.2) |
| 2 | `leaders` | `(Proposition, Rung, Person)` — **three arguments: the faction, the place, and the OBSERVER** | **person** | ranked | the observer's own ledger only | a faction **leader field** | ⛔ **the comparator.** `REV:772-778` proposes `commitment degree × backing raisable`; **an entire political mechanism rests on it and it is not ruled** |
| 3 | `presence` | `(World, Proposition, Rung) → scalar` | resolver | **a WEIGHTED SUM, not a count**: `Σ over members inside n of w(degree)` (`07_alignment.md:222`) | member addresses and commitment degrees | faction scale | ⚠ *an earlier version typed this `→ count`* |
| 4 | `density` | `(World, Proposition, Rung) → [0,1]` | resolver | `presence / weighted_population(n)` (`07_alignment.md:223`) | member addresses | faction scale | breaches `[0,1]` if `contain` cardinality is violated |
| 5 | `footprint` | `(World, Proposition) → Set[Rung]` | resolver | `{ n : presence(f, n) > 0 }`, **upward-closed in the tree** (`07_alignment.md:224`) | member addresses | faction scale | ⚠ **one subject argument** — the pre-v2 brief gave all three the same two-argument signature |
| 6 | `sovereign_fraction` | `Rung → [0,1]` | resolver | **PARTIAL — total only over the office-rooted subgraph** | the conferral graph | stored control | ⛔ root-uniqueness is a political condition, not an invariant; callers must handle plurality **and** partiality |
| 7 | `condition` | `Rung → [0,1] ∪ ⊥` | resolver | draw-weighted mean of its Sites and children; **⊥ at a Site-less leaf** | Sites, `draw_share` | a stored coarse condition | the base case is NEW — the prior form had none and was not total |
| 8 | `verbs` | `(Site, Rung) → Set[Verb]` | **resolver** | — | `condition`, band floors | — | **world truth; never in `choose`'s scope** |
| 9 | `opening_set` | `(Person, View) → [Candidate]` | **person** | — | ledger, stance, capability, Sensation, remits | an authored opportunity | returns **Candidates**, not Acts |
| 10 | `norm` | `(Rung, Proposition) → [−5,+5]` | resolver | member-stance mean **over the judging set** | stances | a stored norm/unrest/reputation | ⚠ *whose* stances was ⛔ in the prior brief; ruled here as the judging set |
| 11 | `occupation` | `(Person, Person) → Proposition?` | **person** | — | the observer's ledger | a profession field | **null is legal** — a person may have no declared occupation |
| 12 | `estimated_profile` | `(Person, Proposition) → Profile` | **person** | — | that person's ledger only | reading true state | ⛔ **`Profile` is a type name that exists in no surface** |
| 13 | `eligible` | `(Person, Verb, Rung) → bool` | resolver | — | remit, marks, standing, matter | `SUP:435` | — |
| 14 | `judging_set` | `Rung → Set[Person]` | resolver | — | `judging_set_rule`, addresses | a stored membership list | — |
| 15 | `draw_share` | `(Site \| Rung, Rung) → (0,1]` | resolver | **shares sum to 1** | draws | `SUP:1245` | stops summing to 1 under a `contain` violation |
| 16 | `share` | `(Person, Site) → (0,1]` | resolver | actor's draw ÷ site total | draws | `SUP:1264` | — |
| 17 | `capacity` | `Date → ℕ` | resolver | items the sitting processes | the date's own term | **the second allowance** | ⚠ **never spent — it caps selection**; spending it as well as `seat_items` was the double-count |
| 18 | `entrenchment` | `(Person, Object) → [0,1]` | resolver | `min(1, seasons_held/60)` | `since`, `until` | a stored tenure counter | needs `until?`, which is why it was added |
| 19 | `address` | `Person → Path` | resolver | a path to the root | the `contain` chain | a stored field | **becomes a SET, not a value, if cardinality is violated** |
| 20 | `regard` | `(World, Person, Rung) → scalar` | resolver | member-stance sum | stances | a stored reputation | ⛔ sign convention |
| 21 | `retention` | `(World, Facet) → [0,1]` | **resolver** | `base(facet_kind) × 2^(−age/halflife(facet_kind)) × (1 − concealment_spend)` (`03:499`) | the facet's kind, age and any concealment spend | **the GM setting an investigation threshold** | ⛔ `base` and `halflife` per facet kind |
| 22 | `trace` | `(Person, Claim) → ProvenanceTree` | **person** | — | **that person's own SAID rows, rootprints and collision records, and nothing else** (`03:538-540`) | a clue counter, a case file, an investigation score | *"only as good as what they went and got"* — **a free provenance query is omniscience with an extra step** (`03:840`) |
| 23 | `filter_share` | `(World, Person) → [0,1]` | resolver | items dispositioned ÷ items reaching the office this season (`03:653`) | the channel's traffic | **a power stat.** A person with `filter_share 0.6` in a ducal household **structurally outranks ministers while holding no standing whatever** | — |

**Nothing stores an aggregate. Every one of these is a query, and that is why power is not static.**

---

## §6 · THE VOCABULARY REGISTER

Row shape mirrors `references/names_index.yaml:19-32` so a later migration is transcription rather than
redesign. **Idem.** = idempotent in meaning; **Idio.** = idiomatic in choosing (`CLAUDE.md` §4).

### §6.1 The coinages, judged

| term | defined at | one-sentence definition | Idem. | Idio. | verdict |
|---|---|---|---|---|---|
| **`Rung`** | `ARCH §2.1` | a rung of the containment tree | **pass** | **pass** | **ADOPTED, at the SECOND attempt.** It is the parenthetical inside `SUP:337`'s own gloss *"Container (a rung)"*. ⚠ **Both earlier candidates collide with Godot built-ins, the port target: `Node` is the scene-tree base class (`godot/scene_tree_architecture.md:16`), and `Container` is the `Control`-derived base of `VBoxContainer` — a WORSE collision, because `Node` fails loudly and `Container` shadows a UI type silently.** `Rung` collides with nothing anywhere |
| **`Tenure`** | `ARCH §2.3` | the one edge record; seven kinds | **fail** — a reader lands right for `hold` and wrong for the other six | **fail** — ordinary usage gives *the holding of an office or of land*; calling a friendship or an address a "Tenure" is not a meaning ordinary usage supplies | **KEPT, with a mandatory qualifier.** The dispositions these documents build on are written in this word; a third name for one object is the failure being avoided. **`Edge` and `Relation` are what the design reaches for when it explains itself** and are the available alternatives. **Qualifier: `Tenure` is the record; `tenure` in prose means the duration of a `hold`** |
| **`mint`** | `ARCH §2.4` | a `touches` mode that brings an object into existence | **fail** — `SUP:245` already uses it for *minting a root token*, a claim-provenance operation | pass | **KEPT, with a mandatory qualifier and one deletion.** `mint` on a **practice rank** is **WITHDRAWN** (advancement is an `alter`), which removes one of the two live meanings inside the design. **Qualifier: `mint` an OBJECT; `witness` mints a TOKEN.** `create` is the available alternative |
| **`efface`** | `ARCH §2.4` | the inverse of `mint` | pass, barely | **fail** — plain English `efface` means *rub out*, near-reflexive; it is not the word English supplies for *destroy this object* | **KEPT, with a target restriction stated once.** `destroy` is the available alternative. **Restriction: `efface` may never target a Claim in another person's ledger** |
| **`Query`** | `ARCH §2.5` | a named pure function over state, never stored | **pass** | **pass** | **ADOPTED, replacing `Derived`.** ⚠ **`Derived` collided directly and in the opposite sense**: `engine/engine_params/params_tables.yaml` ships *"Derived Values"* / *"Derived Scores"* and `references/glossary.md:75-82` lists their members — Health, Stamina, Coherence, Composure, Momentum — which are **stored per-character values**, in a **flat global namespace**. `Query` is the word this tree already uses for compute-on-demand, and **R-1 (`SUP:374-377`) is its definition**: *"compute-on-demand, never push, never store"* |
| **`Sensation`** | `ARCH §3.1` | the two-scalar record a body reports to `choose` | pass | pass | **KEPT, and BOUND.** Risk: the scalars already have a name — **`needs`** (`SUP:183-190`). **Binding, stated once so the next session cannot derive two objects: `Sensation` is the RECORD; `needs` are what it reports, and only TWO of the four reach it** |
| **`leaders`** | `ARCH §2.5` | the ranked query that replaces a faction leader field | pass | pass | **ADOPTED** over `principals`, which carries three ordinary readings plus a homophone this design uses heavily (*principle*), and which `systems/factions/_identifier_census.yaml:3371` uses for a **fourth** thing — the parties present in a scene. The row's own gloss said what it meant: *"replaces a faction **leader** field"* |
| **`oblige`** | `ARCH §5.10` | the seventh Tenure kind: kin obligation | pass | pass | **ADOPTED.** Ordinary English; and the edge it names is `SUP:302-304`'s shipped *obligation edge* |
| **`documented`** | — | — | — | — | ⚠ **WITHDRAWN. A reinvention of `told_by(record, …)`, which ships at `03:528`.** The source set is four and stays four |
| **`avowed`** | — | — | — | — | **DELETED as a field.** The word is fine and is inherited; the **type** was silently narrowed from a three-state enum to an optional flag. It returns as `commit`'s payload: `avowal ∈ {avowed, private, covert}` |
| **`annex` / `secede`** | — | — | — | — | **DELETED as verbs.** Zero occurrences in the prior corpus, and `secede` collides with `05:594`'s shipped use of *secession* for a duke's **defection** |

### §6.2 Field and object terms defined by these documents

| term | defined at | definition |
|---|---|---|
| `Cohort` | `ARCH §2.6` | **persons at coarse fidelity — one record, a weight, evaluated once, applied to all. IT ACTS**, once per season, and is **exactly one type** with an individuated person |
| `Envelope` | `ARCH §2.6` | the **inflow reservoir only** — counts by age band, marks bundle, capability distribution. **It is matter and does not act** |
| `Site` | `ARCH §2.1` | a carrier with an identity, holding `condition` as **primary state at the finest Rung an act names** ⚠ *an earlier version of this row used the refused word "node"* |
| `DocketItem` | `ARCH §5.5` | the object `carry` mints on a Date, which is what gives a matter a clock |
| `Record` | `ARCH §5.4` | a register, charter, deed, roll or letter — matter at a Rung, `efface`-able, and cited through the shipped `told_by(record, …)` |
| `Candidate` | `ARCH §3.2` | what `opening_set` returns: `(verb, target_spec[], believed_obstacle_band)` — **not an Act** |
| `spec` | `ARCH §2.4` | what a `mint` touch carries in place of a reference: `(type, kind?, parent, initial[], slot)` |
| `payload` (Tenure) | `ARCH §2.3` | the kind's own record, for the state the eight named fields cannot hold |
| `INTERIOR` | `LOOP §1.2` | the fourth write class: **one person's own ledger and nothing else** |
| `CENSUS` | `LOOP §7` | the global pass that settles the population from **one** post-eviction snapshot |
| `Place` | `ARCH §2.7` | **`Rung | Site`** — the stance referent kind that was used everywhere and was not defined in any document this suite read |

---

## §7 · THE COLLISION REGISTER

**One row per word carrying two or more meanings.** Kept separate from §6 because a collision is a
*pair* of entries. **After this section, no term in §1–§5 is used in more than one sense.**

| word | meaning A | meaning B | further | severity | **disambiguation RULED** |
|---|---|---|---|---|---|
| **`B1` / `M1` / `B3` …** | loop barriers, in the brief these documents replace | **review finding ids**, cited 76 lines away in the same file | `M1` is also `CLAUDE.md` §0.2's milestone | **was highest** | **CLOSED. The loop steps are named by words, permanently** (§0.2). The letter-number families are review and runner findings only |
| **`hold`** | a `Tenure` kind | Proposition mood `HOLDS` | *the claim ids the **holder** holds*; **and the refusal *"`force` and `hold` never appear in a precondition"***, which becomes unstatable if `hold` is only an edge kind | **very high** | **The edge kind is always written `Tenure(kind=hold)` or "a `hold`-edge". The mood is always written `HOLDS`, capitalised. The coercion quantity is not used in these documents at all**, and `ARCH §9.11` states that the refusal is about the quantity, not the kind |
| **`condition`** | `condition(site) ∈ [0,1]` | **convening condition** | *defeat by named condition* on the stasis ladder | high | **The scalar is always written `condition(site)` or `condition(c)` with an argument. The calendar object is always written in full: `ConveningCondition` / "a convening condition." The stasis usage is "a named condition"** |
| **`subject`** | `Tenure.subject` | `Claim.subject` | `Proposition.subject`; `subject_id` in the substream; a Key `Target` role at `engine/substrate/keys.py:65` | high — five | **Always qualified by its record: `Tenure.subject`, `Claim.subject`, `Proposition.subject`. Bare `subject` is never used** |
| **`object`** | `Tenure.object` | `touch.target` | "every object in this architecture" | high | **`touch` names its field `target`, NOT `object`** — that rename is made here precisely to break this collision. `Tenure.object` keeps the word; the generic sense is written "an object" |
| **`kind`** | `Rung.kind` | `Tenure.kind` | mark kind, need kind, stance referent kind, `Record.kind`, `MatterKind` | high — seven | **Always qualified by its record.** Bare `kind` is never used |
| **`act`** | the record `Act` | `remit.acts`, the closed five | **a unit of currency** — *costs one of his own acts* | high | **The record is `Act`, capitalised. The allowance is "the act" or "his season's act". `remit.acts` is always written with its field path** |
| **`matter`** | `Rung.matter`, a field | **the MATTER step and write class** | *matter events*; the English verb | medium-high | **The step and class are UPPERCASE. The field is always written `Rung.matter`** |
| **`root`** | `sovereign_fraction(root)` | *root token* (`SUP:245`) | `conferral_path(o) reaches root` | medium | **The graph sense is always "the root Rung". The provenance sense is always "root token", never bare `root`** |
| **`degree`** | commitment degree 0–5 | **degree-of-success band** | knot `depth` is a third depth-like scalar | medium | **The commitment sense is `Tenure.degree` or "commitment degree". The band sense is always "degree band" or the band's own name** |
| **`presence`** | the Query `presence(prop, c)` | *deposits by presence and channel* | `binds = persons-by-presence`; `enforcer_presence` | medium | **The Query always carries its arguments. The witnessing sense is always "by presence"** |
| **`View` / `view`** | the **type** passed to `choose` | the **function** `view(person, question)` | — | medium — distinguished only by case | **The function is renamed `assemble(person, question)` in these documents**, which is what `SUP:154` calls the operation anyway (*"`View` is assembled, not filtered"*). The type keeps the word |
| **`Act` / opening** | a declared Act | a **candidate** returned by `opening_set` | — | medium | **CLOSED. `opening_set` returns `Candidate`, not `Act`** |
| **`stake`** | `Rung.stake[]` | `stake_band` manoeuvre; *escalate the stake* | — | low-medium | **The field always carries its record. The manoeuvre is always "escalate the stake"** |
| **`address`** | `Person.address` | *a petitioner may **address** many offices* | *addressable*, an identity property | low | **The field always carries its record. The verb is always "file at" or "put to" in these documents** |
| **`magnitude`** | a die reading, `(3 + d10)/8.5` | `impact_vector: axis → signed magnitude` at `engine/substrate/keys.py:96` | — | low-medium | **The die reading is always "the magnitude reading"** |
| **`standard`** | *an attempt at a standard above its rank* | `EntryStandardTerm` | — | low, **and A is ⛔** | **The advancement sense is ⛔ and is in §8. The dispensation term always carries its full type name** |
| **`commit`** | a `Tenure` kind | the operation `commit(+Δ)` | git commit (`CLAUDE.md` §2) | low | **Acceptable — a kind and its constructor sharing a name is fine once declared, and it is declared here** |
| **`Derived`** | this design's query category, in an earlier version of THIS suite | **stored** per-character values in `params_tables.yaml` and `glossary.md:75-82`, in a **flat global namespace** | — | **was high, and it was a REPO collision in the OPPOSITE sense** | **CLOSED by rename. The category is `Query`, whose definition is R-1; `Derived` is not used in this suite** |
| **`Node`** | a rung, in the brief these documents replace | **Godot's scene-tree base class**, the port target | — | high | **CLOSED. The object is `Rung`** |
| **`Container`** | a rung, in an earlier version of THIS suite | **Godot's `Control`-derived base of `VBoxContainer` and family** — also a built-in | *"a rung"* in `SUP:337`'s own gloss | **high, and worse than `Node`'s** — `Node` fails loudly at once; `Container` silently shadows a UI type | **CLOSED. The object is `Rung`** |
| **`HOLDS`** | the Proposition mood (`SUP:1514`) | **a PREDICATE FORM, `HOLDS(person, office \| holding \| mark)`** (`03:68`) | the `hold` Tenure kind; *the claim ids the holder holds*; the refusal *"`force` and `hold` never appear in a precondition"* | **very high — FOUR, and an earlier version of this register recorded only three** | **The mood is `mood = HOLDS`. The predicate form is always written with its arguments, `HOLDS(p, x)`. The edge kind is `Tenure(kind=hold)`. The coercion quantity is unused in this suite.** ⚠ *This row is the collision register failing on its own subject: it missed a meaning that lives in the document it had not read.* |

---

## §8 · THE GAP REGISTER

Every `⛔`, with what would close it. **`RESERVED` rows must not be closed by accident.**

| id | what is unstated | where it bites | what closing it requires | status |
|---|---|---|---|---|
| G-01 | **the question `q`** the View is assembled against — type, producer, lifetime | `assemble`; `salience`'s `relevance(c, q)`; every retrieval | a producer for `q`. `LOOP §4.1` names a defensible default — the highest-ranked unmet need — **and does not assert it** | open |
| G-02 | ⚠ **CLOSED — struck.** `relevance(c, q)` is defined in full at `03:342-344`. This row previously said it was never defined anywhere in the corpus | — | nothing; the definition exists. **What is open is `q`'s producer, which is G-01** | **CLOSED** |
| G-03 | **`Profile`'s FIELD LIST.** ⚠ **Narrowed — it is not undefined.** `07_alignment.md:217-231` defines the two profiles and gives the arithmetic: `presence(f, n) = Σ over members inside n of w(degree)`, `density = presence / weighted_population(n)`, `footprint(f) = { n : presence(f, n) > 0 }`, upward-closed | every faction reading | a record grouping the three, nothing more | open, narrowed |
| G-04 | **`leaders`' comparator** | deposition, every negotiation above the office ladder | a ruling. `REV:772-778` proposes `commitment degree × backing raisable` | open |
| G-05 | **where the channel store lives** | a minted person's *plausible past* | a home that is a ledger. **Ruled against three ways** (`ARCH §5.3`): `SUP:74-75`, `SUP:355-360`, `SUP:746-748`; §14 row 7 independently forbids the near alternative | open |
| G-06 | **§14 row 4's construal-spread rule** — where a cohort's spread lives, what produces it, what a member draws from | every cohort witnessing; `LOOP §7.3` | a placement inside the four owners. **The review could not close it inside the design's refusals** | open |
| G-07 | **`season_factor(territory)`'s distribution** — range, mean, shape, tail | `yield`, every season; §10.6's band edge | a statement in the form the term beside it already has (`0.47×`–`1.53×`, mean 1.0, `d10 ≤ 3` is bad) | open |
| G-08 | ⚠ **CLOSED — struck.** The predicate vocabulary is enumerated in full at `03:66-79`, **fourteen forms**, with a stated test for a fifteenth. This row previously said one worked example existed | — | nothing; §2.7 carries the roster | **CLOSED** |
| G-09 | **`Venue`'s eight once-occurring parameters** | the sitting | values, or deletion. It is a **12-field tuple plus a 5-field door** | open |
| G-10 | **`standard`** in the advancement and demotion gates | both gates | a definition of *a standard above its rank* | open |
| G-11 | **`Act.payload`** | anything a verb needs beyond its touches | a type, or its deletion in favour of the `touch` fields | open |
| G-12 | **`Event`'s record** | `witness`; `firsthand(event_id)` | fields. Known only to carry an `id` and the degree band | open |
| G-13 | **`World`'s record** | `resolve`'s second argument; the fourteen refusals are written against it | fields | open |
| G-14 | **`Rung.matter`'s structure** | four things are addressed **by name** inside it — Sites, `stores`, Records, the pointer — and an unstructured field cannot be indexed | a typed sub-record per kind | open |
| G-15 | **age-band boundaries** in `Envelope` | births, deaths, capability draws | an enumeration | open |
| G-16 | **channel latency values** | every telling; the news map that vacancy and arson both ride | per-channel-class latencies | open |
| G-17 | ⚠ **CLOSED — it cannot arise.** MATTER runs **before** DELIBERATE, so a person who dies at MATTER never reaches `choose` and declares no act. This row was written against a mis-ordering of the very loop it cites | — | nothing | **CLOSED** |
| G-18 | **`upkeep`'s magnitude; establishment size; who authors the first one** | D-2's residue; the office economy | authoring | open |
| G-19 | **the empty judging set** | F3's own falsifier — an office with an empty judging set has no self-convening route | a floor | open |
| G-20 | **the Coherence-0 officeholder** | F4's own cost — a frozen seat | vacancy-by-absence reaching them | open |
| G-21 | **the `exclude` limb of §14 row 11**, now widened by `efface` across four object classes | razing anything undefended | a bound. **Inherited from `SUP:1839-1844`; no bound is invented here** | open, inherited |
| G-22 | **the `R ≤ 1 → 0` branch** — a fast path by the review's reading, and §14 row 8 is marked Clear | every trivial attempt | a ruling. Deleting it moves the odds of every low-resistance act | open |
| G-23 | **`Office.conferral` cycles** — a cyclic path never reaches root, so a cycle **silently excludes** the office | office clusters, more reachable under F1 and F3 | detection, or the substrate's append-only pattern | open |
| G-24 | **root-uniqueness** | `sovereign_fraction` | nothing — **`SUP:475-478` rules that root-plurality is a political condition callers must handle**, and F1 makes the answer additionally partial | ruled, not closed |
| G-25 | **the two incompatible shipped Coherence band tables** | Coherence-0; the K penalty ladder | a ruling between `ABS:222` and `ABS:223` | open |
| G-26 | **the commitment ladder's licence column**, *"live in two contradictory states"* | what a degree entitles you to | a ruling | open |
| G-27 | **the exchange form** — two transfers plus a binding | rescue-by-market; every purchase | an object. **Gift constructs; market is asserted** (`SUP:1797-1798`) | open |
| G-28 | **re-denominating the coercion layer's coin arithmetic** into typed `stores` | every retinue cost, arrears schedule and wage | unwritten work (`SUP:1795-1796`) | open |
| G-29 | **L-4, the playable-seat list** | **every R-line in the prior design is conditional on it** | authoring | open |
| G-30 | **is the world dying or misunderstood?** | what a twenty-season campaign feels like | **Jordan.** The code is identical either way — which is the signature of a real fork | **RESERVED** |

---

## §9 · CROSS-REFERENCE INDICES

### §9a · By object

| object | §1 | §2 | §3 | §4 | §5 | §6 | §7 | §8 | ARCH | LOOP |
|---|---|---|---|---|---|---|---|---|---|---|
| Person | ✓ | 2.1 | 1,3,4,7,12–15 | 4.1 | 11,19 | 6.2 | subject | G-17 | §2.1, §2.6 | §4, §7 |
| Cohort | ✓ | 2.1 | 22, 24 | — | — | 6.2 | — | G-06 | §2.6 | §4.3, §7 |
| Rung | ✓ | 2.1 | 1,2,6,9–11,21,23,25,26 | — | 7,10,14 | 6.1 | — | G-14, G-24 | §2.1, §5.8 | §2, §7 |
| Office | ✓ | 2.1 | 2,6,7,8,11 | 4.3 | 6,17 | — | — | G-18, G-19, G-23 | §2.1, §5.10 | §2.2 |
| Site | ✓ | 2.1 | 2,23,24 | — | 7,8,16 | 6.2 | — | G-21 | §2.1, §9.2 | §5.7 |
| Tenure | ✓ | 2.2 | 1,2,3 | — | 1,18 | 6.1 | subject, object, kind, degree, hold | — | §2.3, §9.1 | §5.6 |
| Act | ✓ | 2.3 | 4,5 | 4.1, 4.3 | — | — | act, Act/opening | G-11, G-17 | §2.4 | §4.3, §5 |
| Claim | ✓ | 2.4 | 14,16,17,18 | 4.1 | — | — | — | G-08 | §5.14 | §6.2 |
| Event | ✓ | — | 17 | 4.1 | — | — | — | G-12 | §5.15 | §6.1 |
| Proposition | ✓ | 2.4 | 1,2,15,20,26 | — | 1,2,10,11 | — | hold | — | §2.7 | §5.8 |
| Record | ✓ | 2.4 | 17 | — | — | 6.2 | — | — | §5.4 | §5.9 |
| Date / DocketItem | ✓ | 2.5 | 11,19,20 | — | 17 | 6.2 | — | — | §5.5 | §2, §5.8 |
| Sensation | ✓ | 2.4 | — | 4.1 | — | 6.1 | — | — | §3.1, §9.3 | §3.5 |
| Envelope | ✓ | 2.6 | 10 | — | — | 6.2 | — | G-15 | §2.6, §9.7 | §3.4, §7 |
| Stores / MatterKind | ✓ | 2.6 | 9 | 4.3 | — | — | matter | G-27, G-28 | §7 F2, §9.10 | §3 |
| Venue | ✓ | 2.5 | — | — | — | — | — | G-09 | §5.7 | §5.8 |

### §9b · By function

| function | §4 | §5 | its step | its class |
|---|---|---|---|---|
| `choose` | 4.1 | — | DELIBERATE | — |
| `resolve` | 4.1 | — | RESOLVE | ACTS |
| `witness` | 4.1 | — | WITNESS | INTERIOR |
| `sense` | 4.1 | — | DELIBERATE | — |
| `assemble` | 4.1 | — | DELIBERATE | — |
| `opening_set` | 4.1 | 9 | DELIBERATE | — |
| `verbs` | 4.1 | 8 | RESOLVE | — |
| `contest` | 4.1 | — | RESOLVE | ACTS |
| `carry`, `compose_agenda` | 4.3 | 17 | RESOLVE | ACTS |
| `transfer`, `commit`, `requisition`, `investigate` | 4.3 | — | RESOLVE | ACTS |
| `confer`, `revoke`, `issue`, `determine`, `dispatch`, `convene` | 4.3 | — | RESOLVE | ACTS |
| every Query | — | 1–20 | any | **none — a Query never writes** |

### §9c · By term

`address` §6.2, §7 · `additive`/`exclusive` §2.3, §4.4 · `avowal` §2.2, §6.1 · `Candidate` §6.2 ·
`capacity` §5, §7 · `CENSUS` §6.2 · `Cohort` §6.2 · `condition` §5, §7 · `Rung` §6.1 ·
`Query` §6.1, §7 · `documented` §6.1 · `efface` §6.1 · `Envelope` §6.2 · `INTERIOR` §6.2 ·
`kind` §7 · `leaders` §6.1 · `matter` §7 · `magnitude` §7 · `mint` §6.1 · `Node` §7 · `object` §7 ·
`oblige` §6.1 · `payload` §6.2 · `Place` §6.2 · `presence` §7 · `Record` §6.2 · `root` §7 ·
`Sensation` §6.1 · `Site` §6.2 · `spec` §6.2 · `stake` §7 · `standard` §7, §8 · `subject` §7 ·
`Tenure` §6.1 · `View`/`view` §7

### §9d · By source section — the three deliverables stay mutually navigable

| `ARCH §` | compendium sections |
|---|---|
| §0 namespace key | §0.2 |
| §2.1 carriers | §1, §2.1 |
| §2.2 identity | §1, §1.1, §3.1 row 27 |
| §2.3 Tenure | §1, §2.2, §3.1, §6.1 |
| §2.4 the act | §2.3, §4.3, §4.4 |
| §2.5 Query | §5, §6.1 |
| §2.6 cohort / envelope | §2.6, §6.2 |
| §2.7 the owner table | §2.7 |
| §3.1 signatures, Sensation | §2.4, §4.1 |
| §3.2 the belief/truth split | §5 rows 8–9 |
| §3.3 contest | §4.1 |
| §5.x the demanded coverage | §4.3, §5 |
| §7 the forks | §8 (G-19, G-20, G-24, G-27, G-30) |
| §9 the fourteen rows | §2.8 |
| §10 departures | §2.7, §6.1 |
| §11 open | §8 |

| `LOOP §` | compendium sections |
|---|---|
| §1 shape, barriers, classes | §2.7, §4.2 |
| §2 CALENDAR | §4.2, §2.5 |
| §3 MATTER | §4.2, §4.4 |
| §4 DELIBERATE | §4.1, §5 |
| §5 RESOLVE | §4.1, §4.4 |
| §6 WITNESS | §2.4, §4.2 |
| §7 CENSUS | §2.7, §4.2 |
| §9 the write matrix | §4.2 |
| §12 open | §8 |

### §9e · By inherited source

| source | what it owns here |
|---|---|
| `SUP:88-133` | one actor · single-parent containment · alignment with no tier field · the two profiles |
| `SUP:138-162` | the three signatures and the plurality ruling |
| `SUP:166-213` | the person's six fields · needs and what each reads · the cohort · de-individuation |
| `SUP:221-263` | the claim · collision · the closed source set · view assembly and salience |
| `SUP:271-296` | **the conflict rule between #342's documents**, which §2.7's roster ruling applies |
| `SUP:300-487` | the rungs · the owner table · the two capacity quantities · Office · conferral |
| `SUP:492-620` | the roll · the obstacle · degrees · the exposure partition · determinism |
| `SUP:624-698` | phases · write classes · the act conflict rule · resolution strata |
| `SUP:702-830` | the calendar · convening conditions · the five provenance rules |
| `SUP:835-1115` | the up-stroke: petition · carriage · multi-petition · agenda · expiry · vacancy · grievance |
| `SUP:1117-1206` | the down-stroke: dispensation · compliance · one order many executors · vacancy at telling speed |
| `SUP:1208-1384` | matter · the commons · the sizing rule · band gating · the matter-channel licence |
| `SUP:1386-1507` | the larder · `yield` · the transfer act · the denominator fork · gift and market |
| `SUP:1509-1594` | argument: the proposition, case and ground · stasis · the twelve faults · the venue |
| `SUP:1595-1724` | no fallback · vacant-allocator semantics · coincidence · the epistemic payoff |
| `SUP:1726-1772` | **the fourteen rows and the three refusals outside them** |
| `SUP:1774-1874` | the stated limits and the live choices |
| `02:*` | the person: practice rank 0–5 · advancement · individuation and generation triggers · `form_knot` |
| `09:*` | churn: the envelope · the draw · the channel store |
| `11_code_shape.md:243-245` | **the apparatus refusal**, which binds all three of these documents |

---

## §10 · WHAT IS INHERITED AND NOT RESTATED

**The tree's standing rule is *"registered BY REFERENCE … re-transcription = drift"*
(`references/descriptor_registry.yaml:29-30`). This section stops this document re-transcribing the
design.** Nothing listed here is defined in full in §2 or §6.

| term | its definition lives at |
|---|---|
| `K`, `Focus`, `Coherence` | `SUP:251-253`; ⚠ two incompatible band tables, `ABS:221-225` |
| `obstinacy`, `credulity` | `SUP:174-176`; ranges and coefficients at `ABS:653-657` |
| `Practice`, practice rank 0–5 | `02:153`; ruled at `SUP:284` |
| `marks` and their six kinds | `ABS:195-203` (`02:26-33`) |
| `legibility` | `ABS:206` |
| the thirteen Convictions | `ABS:192` |
| `Knot` `depth`, `strain`, `bandwidth`, rupture | `ABS:296-305` |
| `channel_class`, `handle` | `ABS:76`, `SUP:243` |
| `judging set` | `SUP:311-313` |
| `remit`, `binds`, `conferral`, `establishment`, `upkeep`, `post` | `SUP:416-424` |
| `stores`, `yield`, `levy`, `draw`, `mouths`, `margin` | `SUP:1392-1401` |
| `capacity(date)` | `SUP:394-396` |
| `salience`, `confidence_live`, `recency`, `stanceweight` | `SUP:251-263` |
| `SAID`, `firsthand`, `told_by`, `inferred`, `firsthand_via_knot` | `SUP:238`, `SUP:243-245` |
| `Venue`'s twelve fields and five-field door | `SUP:1571-1574` |
| the twelve faults and three severities | `SUP:1536-1542` |
| the stasis ladder | `SUP:1525-1527` |
| the nine dispensation terms | `SUP:1123-1125` |
| `entrenchment` | `ABS:555` (`04 §3.1`) |
| `contest` | `SUP:327`, `SUP:691`, `SUP:1141` |
| `forestall` | `13:141-144`; ⚠ **its precedent does not transfer to arson — it is a purchase and the goods survive** |
| the probability tables | `ABS:610-626`, all DERIVED |
| the parameter and constant table | `ABS:572-760`, with a provenance column per value |

---

## §11 · OPEN AND RESERVED — CARRIED, NOT ANSWERED

**Reserved. Do not close by accident.**

| # | the choice | why it is not answerable here |
|---|---|---|
| **F6** | **Is the world dying, or misunderstood?** | **The code is identical either way, and only the game differs — which is the signature of a real fork.** `ARCH §7` answers the other six precisely because each of them changed the code |

**Six forks the prior design reserved are ANSWERED at `ARCH §7`**, each with its cost and its
falsifier: **D-2** the act economy (one act per person or cohort, universally) · **F1** conferral basis
(per office) · **F2** the `stores` denominator (`MatterKind`) · **F3** S19 (a conferral rule may name
the office's own judging set) · **F4** Coherence-0 (de-individuation by another cause) · **F5**
off-board polities (a Rung with an establishment; the one-actor rule keeps no exception).

**Open, not reserved** — thirty rows at §8. The ones that block a compendium row are G-03 (`Profile`
has no record, so §5 row 12 has no range), G-04 (`leaders`' comparator, so §5 row 2 is a signature with
no semantics), G-08 (the predicate vocabulary, so §2.4's *closed* claim has no enumeration), G-12 and
G-13 (`Event` and `World` have no records, so §4.1's argument types are names).

---

## §12 · PRECEDENT APPENDIX — WHAT THE EXECUTABLE SUBSTRATE ALREADY DOES

**Short, and it earns its place because §1's and §3's gaps have working answers two hundred lines away
in this repository.** ⚠ **These are precedents to copy, not claims that the design uses them.** Nothing
in `01`, `02` or this document runs, and the code below is unrelated to it except as a template.

| gap | the working answer | where |
|---|---|---|
| no id on any record | `Key.id: str` | `engine/substrate/keys.py:145` |
| no uniqueness check | invariant 1 — a duplicate id **raises** | `keys.py:379-381` |
| **no referential integrity** | invariant 3 — a `causes` entry naming an unknown id **raises** | `keys.py:384-388` |
| cycles in a citation graph | **cycle-freedom by construction**: an append-only log whose citations may name only already-logged ids | `keys.py:389-392` |
| no lookup by id | `lookup(key_id)` as a first-class operation | `keys.py:363-365` |
| no shape constraint on type ids | a regex, `[a-z_]+\.[a-z_]+` | `keys.py:399` |
| **nowhere for a per-field `additive`/`exclusive` annotation to live** | dotted quantity keys with per-key metadata and aliases | `references/descriptor_registry.yaml:49-58` |
| a word colliding with common English | the `context:` field, which exists **precisely** for that | `references/names_index.yaml:30-32` |
| resolving a dependency by name rather than by import | role resolution through a registry | `engine/substrate/composition.py` |

⚠ **`params_tables.yaml` is a byte-frozen 2026-08 capture of prose and is REFERENCE, not mechanism**
(`CLAUDE.md` §5). Do not lift a number from it without checking the code first — its *Degrees of
Success* section holds a **pre-ruling** ladder. This matters here because `ARCH §9`'s degree bands and
`SUP:540-546`'s are the design's, not that file's, and the two must not be conflated.

---

## §13 · STATED LIMITS

1. **Nothing here has executed**, and this document indexes two other documents that also do not run.
2. **Every count in §2.7 is a count of what a cited line enumerates**, not a count of anything measured.
3. **`⛔` means "not stated in any document THIS SUITE READ".** The surfaces read are named at §0.1.
   ⚠ **And that scope is a minority of the corpus: 108 of 123 proposal documents over 200 lines are
   uncited here** (`00_INDEX.md`). **Four mechanisms this suite called new or missing are already
   designed in uncited documents.** A `⛔` is a statement about this suite's reading, never about the
   corpus.
4. **The repo-collision claims in §6 and §7 rest on greps of `engine/`, `systems/`, `references/` and
   `godot/`**, not of the whole tree.
5. **This document is REFERENCE, not mechanism.** The test to apply to every row: *if this document were
   deleted, would the game behave differently?* **No — because there is no game yet.** That is the
   honest state, and it is why §12 exists: the answers are in the code or they are nowhere.
