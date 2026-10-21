# Verb key rows: every folded name of the uploaded verb list, disposed, and the key rows it needs
## Status: PROPOSED (2026-10-21). Not ratified; merging ratifies nothing unless Jordan so rules. Static reading. No season, probe or test ran. One import of three loaders (running their import-time checks on the shipped tables) listed three rosters. No proposed row was loaded; every claim that a skeleton loads is unverified.
## Parts, in reading order: **this file** (§1 head, §2 disposition table) · [`_part2`](2026-10-21-verb-key-rows_part2.md) (§3.0-§3.1.9 key rows) · [`_part3`](2026-10-21-verb-key-rows_part3.md) (§3.1.10-§3.2 key rows, §4 why no per-row value fan, §5 host rows, §6 cost and ordering, §7 open items).

The import named in the status line loaded `engine.season.data.affiliations`, `data.rosters` and
`data.verbs` and printed the affiliations, the seven axes and the 46 verb names. No number in this
proposal comes from it.

Citations: `U:n` is line *n* of Jordan's upload (`verb_list.md`, the copy carrying `pillage`); `VT:n` is
`engine/season/verb_table.yaml`; `RO:n` is `engine/season/rosters.yaml`; `WM:n` is
`engine/season/write_matrix.yaml`; `DV:n` is `engine/season/data/verbs.py`; `OP:n` is
`engine/season/decision/options.py`; `WI:n` is `engine/season/loop/witness.py`; `PQ:n` is
`engine/season/queries/person_q.py`; `_partN:n` is part N of the v2 verb suite, now
`proposals/2026-10-16-verbs/2026-10-16-verbs-NN-*.md` with NN zero-padded (`_part10` is
`2026-10-16-verbs-10-lexicon-mass-battle.md`; renamed by #491, citations keep the old numbering)
(reference only). Every `file:line` here was opened by the producer. Design documents are cited for
intent and vocabulary only (CLAUDE.md §0.05); what the code does is cited to the code.

---

## 1. Head

### 1.1 Purpose

The upload folds about 120 names into host verbs with no row of their own (U:3, and every "Folded in"
line). The critique of the list found that a fold by CONTENT is invisible to every reader keyed by verb
name, so a told insult and a told praise are one act to the dice, the chooser, the creed table and the
Event record. Jordan's instruction is "Propose all key rows." This document answers it in the only way
that can be checked: it gives every folded name one disposition (KEY, DERIVED or PARKED), names the code
reader that consumes a KEY's distinction and the predicate that recovers a DERIVED one, and for each KEY
writes the row skeleton in `verb_table.yaml`'s own column order with every table cell the loader will
demand of it. It edits no file but its own three parts and builds nothing. One host rename
(`examine` → `search`) is recommended and priced in §5; no other rename is proposed.

**Which names folded into `tell` the game can tell apart, by name.** With confidence: `confide`,
`praise`, `insult` and `threaten` (each becomes its own row, so the verb name says it), and `confess`
and `confront` (each recovered from the act by a predicate shipped play can read: §2 #23, #26).
Not with confidence: `counsel` (a telling about an OUGHT Proposition cannot be told from news of a
motion, #30); `warn` (no intent claim exists to retell at the shipped `intent_disclosure: 0.0`, #25);
`testify` (no form says the hearer sits on a bench, #22); `flatter` (needs `lie`, #28).

### 1.2 What a key is, as the code defines it

A **key** is a verb's own row in `verb_table.yaml` that reaches the world through the host's code. The
one live example is `accept`: its row (VT:628-656) carries `fight`'s typed cell, `contests: "the body"`,
and `fight`'s degree-keyed `writes:` and `emits:` verbatim, and its own
`emits_on_refusal: ["accept.refused"]`; the effect `_eff_kill` is registered for both names by two
stacked decorators (`loop/effects_combat.py:34-35`), and `loop/effects_shared.py:43-47` shows the
registry is a flat `EFFECTS[verb] = fn` dict. The loader and the readers impose the following on any new
row. Each was read at the cited line.

| # | requirement | owner, and where it bites |
|---|---|---|
| K-1 | **A row.** Unique name (DV:577); no key outside `VerbRow`'s fields except `*_note` (DV:585-587); `beneficiary:` present and in the roster (DV:719, :737); `stratum:` in the roster (DV:860); eligibility kinds in the four-member roster, `capability` refused by name (DV:843, :848); `contests:` a rostered prize (DV:867); a `contests:` row has degree-keyed `writes:` and `emits:` with the same keys, and a degree-keyed row without `contests:` or a `graded_inquiries` route is refused (DV:771-824). | `data/verbs.py::_load_verb_table` (DV:567), at import |
| K-2 | **Writes are matrix rows.** Every `writes:` pair is a `(kind, field)` row of `write_matrix.yaml`, for every degree branch (DV:832-835). If the matrix row carries `unproduced:` the same commit deletes it (DV:1033-1045, invariant 2, both directions). | `_load_verb_table`; `write_matrix.yaml` |
| K-3 | **A refusal kind for every failable clause.** A row with a `requires` or a non-`own` eligibility needs a non-empty `emits_on_refusal` (DV:883-885); a row whose typed cell names its conjuncts keys refusals by exactly its failable clauses, and a contested keyed row uses one kind under every key (DV:905-943). | `_load_verb_table` |
| K-4 | **An effect, or a declared decline.** A row that writes needs an `@effect_for(<name>)` body or an `effect_decline_note:`, and a row with an effect may not carry the note (`manifest/registry.py:599-633`, `check_effects`, at `SeasonDriver` construction). A row with a precondition needs a typed cell, a `REQUIRES_PREDICATES` entry or a `requires_decline_note:` (`manifest/registry.py:637`). `resolvable_verbs()` drops a row failing either gate (`loop/driver.py:101-131`). | `loop/effects_*.py`; `manifest/registry.py` |
| K-5 | **Seven alignment cells or a named exemption.** Every verb carries a cell on each of the seven axes (a number or explicit `null`), or is named in `uncelled:` with a non-empty reason and then carries none (DV:1357-1398; the rule's statement at RO:2736-2742; `uncelled:` at RO:2743-2760). The axes are `hierarchical_equal` (RO:2809), `precedent_substantive` (:2857), `partisan_equitable` (:2904), `selfish_selfless` (:2952, all `null` by design because `beneficiary:` owns "for whom", RO:2779-2783), `rigid_flexible` (:3001), `grandiose_humble` (:3048), `deontological_instrumental` (:3101). | `data/verbs.py::_load_alignment` (DV:1401), at import |
| K-6 | **A capability key only if a pool is rolled and the key differs.** `rosters.yaml: verb_capability` (RO:1157-1182) maps a verb to the `Person.capability` key its pool draws on; `seam/wrappers/sigma.py:103` reads `VERB_CAPABILITY.get(verb)`. A verb with no entry rolls `pool_default`, which is not an error (RO:1167-1170). Today the table has two entries, both `"copying"` (`tell`, `speak`, RO:1180-1182), and one corpus person carries a capability at all (RO:1171-1176). | `seam/wrappers/sigma.py::_capability` (:94-106) |
| K-7 | **A creed cell, optional.** `affiliation_engagement` (RO:2420-2487) is SPARSE (`default_cell: null`, RO:2430); a verb has a cell in the shared `sacred` column or sign-only cells per affiliation, never both, and every key is a verb-table name (`data/affiliations.py:118-178`). No density rule applies. | `data/affiliations.py::_load_engagement`, `engagement` (:181-193) |
| K-8 | **Event kinds are declared on the row.** The kind roster is derived from every row's `emits:` and `emits_on_refusal:` (invariant 7, `architecture/meta/04_CODE_ARCHITECTURE.md` §B.13 item 7; DV:1271-1286). | `data/verbs.py::_derive_kind_verb` |
| K-9 | **The act id hashes the verb name.** `H(seed, tick, actor, f"act:{verb}:{act_key}")`, `act_key` the subject plus any known-person operand and the seat (DV:1089-1121, the key built at DV:1112-1121). A NEW key mints new ids for its own acts and moves no existing id; a RENAME moves every id of the renamed verb. Either moves a run's `content_hash` wherever the new row is chosen instead of something else (§6). | `data/verbs.py::act_key` |
| K-10 | **The chooser must be able to form it.** `opening_set` (OP:46) forms Candidates per row over the question's referents (`for subject in refs`, OP:164) through `operand_bags` (OP:1032-1101), which binds only names in the CLOSED operand roster `[actor, subject, from, to, site, kind, amount, floor]` (RO:1754-1769) plus the known-person fan (`known_person_operands: [to]`, RO:1880-1905). `Candidate` carries `verb, subject, operands` and nothing else (`state/carriers.py:546-548`). A row whose operands cannot all be bound, or whose subject no question raises, forms nothing and is a dead carrier (`ID-13`). | `decision/options.py` |

Six further facts change what a key can be, and each was found by reading, not assumed.

- **F-1. An Event has no payload, so a witness distinguishes acts by KIND.** `Event` carries `id, kind,
  changes, causes, emitted_at, degree, observed` (`state/carriers.py:254-262`); S19.3 bars actor and
  target from it (`:232-234`). A witness's claim of an Event is `(subject, <kind>, True)` (`WI:643`), so
  what a witness can tell apart is the kind. A WORLD-SIDE reader is not so limited: it recovers the act,
  its payload and its operands through `causes[]` (`state/attribution.py::actor_of`, described at
  `state/carriers.py:244-249`), as WITNESS itself reads `Act.payload["said"]` off the causing act
  (WI:104-105). This is what makes a DERIVED disposition checkable: its recovery predicate is a
  world-side read of the act or the state it wrote.
- **F-2. A key's own kind is judged, and under `claim_subject_rule: both` it is judged on every party it
  wrote.** `KIND_VERB` maps a kind to its verb only where exactly one row emits it (DV:1271-1283). A kind
  several rows emit joins `PAIRED_KINDS` (PQ:139) and is then judged only for the doer a `seen.who`
  pairing names, through authored `deed:<kind>` cells (PQ:91-104, :115-124). A kind ONE row emits is
  judged by its claim's subject as its doer (PQ:105, H-192). The shipped rule is `both`
  (`data/fixtures.py:485`): WITNESS lands a claim on the act's anchor and on every subject the act's
  changes name (`epistemic.py:207-216`). So an own kind on an act that writes ANOTHER party judges that
  party as the doer. Rule adopted: a key emits a success kind of its own (sharing the host's kind would
  move the host's judged deeds, as `accept` already does to `fight`'s, which is why
  `deed:person.died`/`deed:body.changed` exist, RO:3061-3062, :3123-3124); and a key that writes another
  party either carries all-`null` cells, or authors numeric `deed:<own kind>: 0.0` cells on each of its
  non-null axes, the `deed:matter.undetermined: 0.0` precedent (RO:2812: "lands the claim on the PARTY,
  and a null cell would fall back to `determine`'s own … Numeric, not null, for that reason"). The cost,
  said: a zero `deed:` cell zeroes the doer's judgement of that kind too; the verb's own cells still
  move the chooser. Refusal kinds are never deeds (DV:1288-1294).
- **F-3. The told deposit is keyed on one kind literal.** WITNESS deposits the told claim only when
  `e.kind == "news.told"` (WI:860), reading `Act.payload["said"]` (WI:86-105). A `tell`-family key that
  passes on what it holds (`confide`, `threaten`) therefore emits `["news.told", "<own kind>"]` on its
  telling bands, `tell`'s own precedent for a second kind on one band (`confidence.broken`,
  VT:1036-1041); `praise` and `insult` pass nothing on and emit their own kinds only. `said` rides on any
  row whose cell carries a NAMED `own_ledger` conjunct (`holds`) (OP:146-147, :244-260).
- **F-4. The opener walker keeps one decorator per function.** `_derive_openers_from_effects`
  (DV:438-546) records, for each decorated function, the verb of the LAST `@effect_for` in its list
  (DV:517-523). It follows a decorated function's helpers (DV:457-465), so a key with its OWN body that
  calls the host's helper is attributed correctly. True, and needed by no key here: the one stacked
  body, `_eff_kill`, opens no Tenure, and every key below on an opening host composes its own body.
- **F-5. A value fanned per row in `opening_set` is not a choice.** Two Candidates of one row that differ
  only in a fanned value share the act id (DV:1112-1121), the score (`align` by verb,
  `decision/choose.py:149`) and the choice noise (`choice:{verb}:{subject}`, `decision/choose.py:381`),
  and no person-side reader reads the value. §4 (`_part3`) gives the reasoning; the consequence is that
  this proposal has no "mode" category. A value that should vary the choice is a KEY; a value the host's
  own operands or world state already fix is DERIVED.
- **F-6. The told content is selected, not chosen.** `said` is `said_of(own ledger, subject)`, newest
  then most confident at the shipped `said_slant: newest` (RO:1948-1958). A key whose distinction is the
  VALENCE of what is told cannot be built on content; `praise` and `insult` therefore write a regard and
  tell no content.

### 1.3 The disposition test

Applied to each name, in this order; the first that holds decides.

1. **PARKED** — the distinction needs a mechanism that is not built and is not the host itself: a verb
   (`lie`, J-C-6), a carrier (a cover, a site kind, a siege state), a per-order input, or a ruling. The
   dependency is named. A name whose host row does not yet exist is NOT parked for that alone: its
   disposition is decided on the merits, and §6 orders it after its host.
2. **KEY** — any one of: (a) a reader keyed by verb name must tell it from the host (`align`, DV:1444;
   `refuses`, OP:356-370; `beneficiary_of`, `decision/choose.py:154-185`; `VERB_CAPABILITY`,
   `sigma.py:103`; `engagement`, `data/affiliations.py:185`; the choice noise, `choose.py:381`); (b) its
   precondition, counterparty or actor class differs from the host's typed cell; (c) its world write
   differs; (d) witnesses must separate its Event kind (F-1). A value that must vary the choice (F-5)
   is a KEY whose values live in a roster keyed by `verb_table`, the `graded_inquiries` shape
   (RO:1104-1130). The reader that consumes the distinction is named; a KEY with no named reader is not
   proposed (S-1, `ID-13`).
3. **DERIVED** — the host's act under a condition recoverable from its own operands or the world state
   it wrote, by a stated **recovery predicate** (F-1). No row and no operand. Where shipped play cannot
   read the predicate (the host is unbuilt, or the condition never arises), the row says "no predicate
   in shipped play: low confidence".

"Alias" is not used for this: `references/names_index.yaml:16` gives `aliases:` the meaning "allowed
equivalent phrasings" of one display string, and a derived act is not a synonym of its host.

A distinction recoverable from the SUBJECT's own rostered field is DERIVED: the engine already reads it
off the entity. This is how the ruled `conferral_bases` roster (RO:2064-2082, `open: false`,
ED-IN-0256) is respected: `appoint` is `confer` on a seat whose `conferral` is `appointed`, and no row may
add a basis.

### 1.4 Legend

| mark | meaning |
|---|---|
| **KEY** | own row; skeleton in §3 |
| **DERIVED** | no row; the host's act under the recovery predicate given |
| **PARKED** | waits on the named dependency; "eventual" says what it becomes |
| `host*` | the host has no row in `verb_table.yaml` today (a "Proposed" row of the upload) |
| `[ASSUMPTION: … — basis]` | a choice the code does not settle; the basis is stated |
| `[UNVERIFIED]` | a claim the producer did not check against the tree |

Reader shorthands used in §2, each opened at the line given:

| shorthand | the reader | where |
|---|---|---|
| **align** | `align(verb, axis)`, read by the score (`decision/choose.py:149`), the H-146 refusal gate (`refuses`, OP:356-370) and the scar (`elements_violated_by`, PQ:423) | DV:1444-1453 |
| **kind** | the event-kind claim every witness deposits (WI:643), judged by `deeds_judged` through `align_kind` (PQ:79-133; DV:1469-1481) | WI, PQ |
| **cell** | the fold's precondition and counterparty clause, `_admits` | `loop/resolve.py:183` |
| **elig** | the remit/own/hold/presence test, fold side and person side | `loop/resolve.py:90`; OP:373 |
| **stance_term** | `stance_toward` → `regard` → the score's `stance_term` | PQ:67-77, :336-350; `decision/choose.py:54` |
| **circle** | `_circle_of`, the confidence circle of a told deposit | WI:108-133 |
| **intent** | the declared-intent claim and its reader `world_q.named` (`queries/world_q.py:750`, via `person_q.intent_named`, PQ:894-900; `intent_claim`, RO:1907-1926) | PQ, RO |
| **via** | `_ch_post_remit`, which admits a seat's obligees to the acts done through `Act.via` | `epistemic.py:547`, :554-558 |

---

## 2. Disposition table

One row per folded name per "Folded in" line of the upload (a name folded twice gets two rows), plus
the PC keys and content folds the instruction names. 116 rows. Counts: **KEY 12 · DERIVED 67 · PARKED
37.** For a KEY the predicate column is "—": the verb name is the distinction. For a PARKED row it gives
the eventual predicate where the eventual form is DERIVED. §3.2 carries skeletons for the PARKED names
whose eventual form is a key.

### PC — personal combat (U:15, U:24; keys U:12-13, U:22)

| # | name | host | disp. | reader (KEY) | recovery predicate (DERIVED) | reason | dependency |
|---|---|---|---|---|---|---|---|
| 1 | `accept` | `fight` | **KEY** (shipped) | align: its own cells (RO:3009, :3056, :3121) differ from `fight`'s (:3053, :3119); the noise | — | consent changes the valuation; the one live key (VT:628-656) | none; §3.1.1 amends its kinds |
| 2 | `assassinate` | `fight` | PARKED | eventual KEY: cell (a held cover), align | — | what defines it is a killing whose author the world cannot name; nothing holds a cover | `conceal`'s cover Record; the seam's aim input |
| 3 | `capture` | `fight` | PARKED | eventual KEY: its own writes (a `detain` opened) | — | the scene must not kill when the aim is to take alive | the combat seam's aim *alive*; custody opener |
| 4 | `ambush` | `fight` | PARKED | eventual KEY or DERIVED, decided with the seam input | eventual: the scene's first mover was the actor from a held cover | today a coin flip in the scene; orthogonal to aim (`_part9:77`) | a first-mover input to the seam; a cover |
| 5 | `shoot` | `fight` | PARKED | — | eventual: the actor's kit in hand is a missile weapon | no ranged weapon in the one combat resolver (`_part9:78`) | M9 |
| 6 | `champion` | `challenge` | PARKED | eventual KEY: a third party, the principal | — | a three-party act; nothing reads stakes | the `challenge` Record (PC-10b); a stakes reader (M3) |

### MB — mass battle (U:44, U:52, U:62)

| # | name | host | disp. | reader (KEY) | recovery predicate (DERIVED) | reason | dependency |
|---|---|---|---|---|---|---|---|
| 7 | conscript | `levy`* | DERIVED | — | every `levy`; no predicate in shipped play: low confidence | conscription is raising men by obligation | host row |
| 8 | recruit-for-coin | `levy`* | **KEY** `hire_troops` | its own writes (treasury coin, no cohort stance row) read by the fold's gate; align | — | "different economies, not different tiers" (`_part10:108`) | host row; §3.1.2 |
| 9 | garrison | `muster`* | DERIVED | — | eventual: the destination Rung is held by the actor's faction; no predicate in shipped play: low confidence | a muster to a place the faction holds (`_part10:110`) | host row |
| 10 | rally | `marshal`* | PARKED | eventual KEY with its values in a roster keyed by `verb_table` | — | the field's orders are process-wide settings, not per-order inputs (`modules/mass_battle/config.py:246`, `:257-258`), and `engine/` may not import `modules/mass_battle` (CLAUDE.md §3) | a per-order input in the field module; `rally_check` (`orchestration.py:288`) reading it |
| 11 | pursue | `marshal`* | PARKED | as rally | — | as rally | as rally; `pursuit_damage`, `recall_check` (`orchestration.py:2549`, `:2585`) |
| 12 | retreat | `marshal`* | PARKED | as rally | — | as rally; `STANCE_COMMITMENT` member `retreat` (`config.py:290`) | as rally |
| 13 | withstand | `marshal`* | PARKED | as rally | — | as rally; member `hold` (`config.py:290`, `:374`) | as rally |
| 14 | the reserve and its release | `marshal`* | PARKED | as rally | — | `RESERVE_COMMIT_TURN` is an environment setting (`config.py:258`) | as rally |
| 15 | formation | `marshal`* | PARKED | as rally | — | as rally [UNVERIFIED: the `build_army` line was not opened] | as rally |
| 16 | who leads which subunits | `marshal`* | DERIVED | — | eventual: the `battle_order` Record names a person per subunit; no predicate in shipped play: low confidence | the field reads the assignment off the Record | host row |
| 17 | besiege | `march` | PARKED | eventual KEY: its writes differ | — | a siege is a state with a per-season reader; neither exists | M-6 |
| 18 | storm | `march` | DERIVED | — | the act is a `march` whose band is not `Declared` (its Event kind is `field.won`, `field.lost` or `field.unopposed`, VT:715-719) | today's `march` is the storm (`_part10:279`) | none |
| 19 | provision | `supply`* | DERIVED | — | `payload["kind"]` names food, as `_eff_transfer` reads its `kind` (`loop/effects_economy.py:168`); no predicate in shipped play: low confidence. `matter_kinds` is open (RO:1360-1371) and holds `grain` but no member called food | the kind moved | host row |
| 20 | equip | `supply`* | DERIVED | — | `payload["kind"]` names arms; no predicate in shipped play: low confidence, and none even with the host until an arms kind is registered (`matter_kinds`, RO:1371) | as provision | host row; an arms kind |
| 21 | sack | `pillage`* | **KEY** | cell (occupation), its own writes (every kind, all of it), kind (`place.sacked`) | — | witnesses must tell a sack from living off the land, and `surrender` must bar exactly it (U:69) | host row; §3.1.3 |

### SC — social contest (U:79, U:96, U:104, U:113, U:124)

| # | name | host | disp. | reader (KEY) | recovery predicate (DERIVED) | reason | dependency |
|---|---|---|---|---|---|---|---|
| 22 | testify | `tell` | PARKED | eventual KEY: cell (the hearer sits on the bench of a docketed matter about the subject) | — | no form says the HEARER sits on a bench (`basis` asks the actor's seat, VT:241-244); no reader weighs `testimony` (`proofs`, RO:2148-2158, read only by `data/arrangements.py:193`) | a hearer-side bench form; a proof reader |
| 23 | confess | `tell` | DERIVED | — | `said.subject == actor` and `said.predicate` is a deed kind (`DEED_KINDS`, DV:1294), read off `Act.payload["said"]` through `causes[]` (F-1) | the content, read today | none |
| 24 | confide | `tell` | **KEY** | circle: a chosen circle replaces the `telling_privacy` draw (WI:125-133) | — | today a confidence is a random draw | none; §3.1.4 |
| 25 | warn | `tell` | PARKED | — | eventual: `said.predicate` is a declared-intent claim (`intent:<verb>`) whose ids name `to` (PQ:894-900) | no intent claim exists to retell at `intent_disclosure: 0.0` (`data/fixtures.py:773`) | an intent claim in the teller's ledger (`intent_disclosure > 0`, or `threaten`, #33) |
| 26 | confront | `tell` | DERIVED | — | `to == subject` on the act (`binding_from_act`, WI:128), formable since IN-18 (OP:1042) | the content, read today | none |
| 27 | praise | `tell` | **KEY** | stance_term: writes the subject's `(Person, stance)` toward the actor (+) | — | a face-to-face praise changes nothing about the teller today (critique B3); praise of a third party stays `tell` | H-194's `declared` arm (§3.1.5) |
| 28 | flatter | `tell` | PARKED | eventual KEY on `praise`'s prize: insincerity | — | flattery is praise the teller does not believe | `lie` (J-C-6, U:80) |
| 29 | insult | `tell` | **KEY** | stance_term: the subject's `(Person, stance)` toward the actor (−) | — | as praise, opposite sign | as praise (§3.1.6) |
| 30 | counsel | `tell` | DERIVED | — | `said.subject` is a Proposition of mood OUGHT; **it cannot be told from news of a motion**: low confidence | counsel and news of a proposal are one telling | none |
| 31 | propose | `utter` | **KEY** | the mood it mints, `OUGHT`, read by `world_q.ambitions` (`queries/world_q.py:1700`, the OUGHT test at :1733); align; the noise | — | a value that must vary the choice (F-5): a person chooses to propose or to allege | none; §3.1.10 |
| 32 | allege | `utter` | **KEY** | the mood `HOLDS`, which the same test excludes from ambitions; align | — | as propose | none; §3.1.10 |
| 33 | threaten | `utter` (moved to `tell`) | **KEY** on `tell` | intent: always discloses the chosen act naming the hearer, which `world_q.named` raises as the hearer's question about the teller | — | a told own intent naming the hearer is a threat; the key replaces `declare_intents`'s draw (`decision/choose.py:486-516`) as `confide` replaces `telling_privacy` | none; §3.1.11 |
| 34 | vote | `commit` | DERIVED | — | the Proposition committed to is a docketed motion at a sitting the actor attends; no predicate in shipped play: low confidence | a vote is a member's commit to the motion | M-COUNT for the count; §5 adds the one-per-actor guard |
| 35 | swear | `commit` | DERIVED | — | `w.propositions[subject].mood == "HOLDS"`; no predicate in shipped play: low confidence (every computed `utter` is OUGHT, `effects_information.py:904`, until `allege`) | an oath is a commit to a claim | `allege` (#32) |
| 36 | accuse | `petition` | DERIVED | — | the petition's `to` is the person complained of; it cannot be told from a petition to a lord: low confidence | content (`_part11:229`) | none |
| 37 | adjourn | `convene` | DERIVED | — | a live Date already exists at the venue for the same docket when `convene` writes another | same pairs (VT:194) | none |
| 38 | plead | `speak` | DERIVED | — | every `speak` (identity) | pleading is speaking before the room | none |
| 39 | refute | `speak` | PARKED | eventual KEY with its speech kind (`deny`/`cite_incompatible`, `arrangements.yaml:44-82`) in a roster keyed by `verb_table` | — | no runtime reader of `SPEECH_KINDS` (loaded at `data/arrangements.py:252`, read by nothing in `loop/`, `decision/`, `queries/`, `seam/`) | the issue-rung write on `speak` |
| 40 | concede | `speak` | PARKED | as refute (`concede_fact`/`concede_harm`) | — | as refute | as refute |
| 41 | object | `speak` | PARKED | as refute, a speech kind not yet rostered | — | six of ten kinds rostered (`arrangements.yaml:45-51`) | as refute; the member (`H-153`/`H-154`) |
| 42 | define | `speak` | PARKED | as object | — | as object | as object |
| 43 | arbitrate | `determine` | DERIVED | — | `DocketItem.arrangement == "arbitration"` (`arrangements.yaml:94-108`); low confidence in shipped play (`open_case` dockets with no arrangement, VT:126) | the arrangement decides the procedure | none |

### FI — fieldwork and inquiry (U:141, U:177, U:186)

| # | name | host | disp. | reader (KEY) | recovery predicate (DERIVED) | reason | dependency |
|---|---|---|---|---|---|---|---|
| 44 | search | `examine` | DERIVED | — | every `examine` (identity) | the act `examine` performs is a search; §5 recommends the host rename | none |
| 45 | track | `examine` | PARKED | eventual KEY: cell (a Person quarry) and a destination finding | — | `inquiry_modules` keys on `finding.made` and answers a trail AT the subject (RO:2232-2281) | an inquiry entry for a quarry's leaving acts |
| 46 | audit | `survey` | **KEY** | elig (`remit:issue`) and cell (`purview`, `seize`'s cell, VT:916-920); via (the act carries `Act.via`, so the seat's obligees are admitted); align | — | a seat's audit is not a private survey | `survey`'s place sheet; §3.1.7 |
| 47 | census | `survey` | DERIVED | — | the surveyed subject is a Rung (`subject in w.rungs`) | survey of a place | `survey`'s place sheet |
| 48 | scout | `survey` | **KEY** | cell (presence at the Rung, `examine`'s shape VT:1172-1180, not `own_ledger`) | — | scouting is done where one stands | `survey`'s place sheet; §3.1.8 |
| 49 | disguise | `conceal`* | PARKED | — | eventual: the cover Record's scope is a room | no cover Record and no reader of a scope | `conceal` |

### TW — threadwork (U:212, U:235)

| # | name | host | disp. | reader (KEY) | recovery predicate (DERIVED) | reason | dependency |
|---|---|---|---|---|---|---|---|
| 50 | trace | `thread_read` | PARKED | — | eventual: the read went by the knot route | the host is untyped, uncelled and unformable (VT:1258-1259; RO:2749-2752) | `H-85` |
| 51 | diagnose | `thread_read` | PARKED | — | eventual: the finding is a displacement in a person | as trace | `H-85`; M9 (`_part13:491`) |
| 52 | heal | `mend`* | DERIVED | — | the mend's target is a Person body; no predicate in shipped play: low confidence | the ordinary `heal` is NP's `tend` (#110); a threadwork mend is narrated as a mend | host row |

### GV — settlements and governance (U:261, U:275, U:283, U:294, U:312)

| # | name | host | disp. | reader (KEY) | recovery predicate (DERIVED) | reason | dependency |
|---|---|---|---|---|---|---|---|
| 53 | appoint | `confer` | DERIVED | — | `Office.conferral == "appointed"` (`state/gate.py:582`) | the basis is the seat's, ruled closed (RO:2064-2082) | none |
| 54 | designate | `confer` | DERIVED | — | the office conferred is `off_heir` (`offices.yaml:247`) | designation is a `confer` of the heir seat, not a basis | none |
| 55 | elect | `confer` | PARKED | — | eventual: `Office.conferral == "elected"` and a count of commits passes | nothing counts the members' commits (`_part14:558`) | M-COUNT |
| 56 | steward | `confer` | DERIVED | — | `Tenure.term is not None` on the opened hold; no predicate in shipped play: low confidence (a computed `confer` declares no term, `loop/effects_governance.py:37-44`) | a termed hold (VT:182) | none |
| 57 | rotate | `confer` | DERIVED | — | the termed hold matured at MATTER and a new one opened; no predicate in shipped play: low confidence | a term rule, not an act | none |
| 58 | dismiss | `revoke` | DERIVED | — | every `revoke` (identity) | the same act named by its object | none |
| 59 | amend | `establish` | DERIVED | — | the office id existed before the act (`remit.changed`, VT:304) | re-remitting an existing office | none |
| 60 | resign | `release` | DERIVED | — | the closed Tenure is a `hold` on an Office (read off the act's change) | §5: the host earns `seat.resigned` | none |
| 61 | abdicate | `release` | DERIVED | — | as resign, and the Office sits on a rung with no rung above [ASSUMPTION: "the realm's top seat" read so] | as resign | none |
| 62 | abandon | `release` | DERIVED | — | the closed `hold` is on a Rung | as resign | none |
| 63 | deny | `release` | DERIVED | — | the closed `hold` on a Record was opened by a `give` (the opening act, found in the act store) | the receiver's release of what he was given (`_part11:231`) | none |
| 64 | withdraw | `release` | DERIVED | — | the closed `hold` is on a `petition` Record the actor minted | — | none |
| 65 | warrant | `issue` | DERIVED | — | the dispensation's `terms` names a Record or a person (`warrant_sourced`, RO:1820) | read by `seize` already | none |
| 66 | commission | `issue` | DERIVED | — | the dispensation names a seat and a person (OP:1055-1063) | read by `operand_bags` already | none |
| 67 | decree | `proclaim`* | DERIVED | — | no predicate in shipped play: low confidence | a notice-kind edict | host row |
| 68 | relieve (U:294) | `transfer` | DERIVED | — | the receiving rung is in shortfall [UNVERIFIED: which world read decides a shortfall; the tree records it as claims, RO:1853] | §5: the host earns `relief.given` | none |
| 69 | fortify | `build` | DERIVED | — | the works plans a `garrison` Site (`site_kinds`, RO:1358) | — | none |
| 70 | improve | `build` | PARKED | — | eventual: the works raises an existing Site's ceiling | no works shape for it | M-WORKS (b) (`_part14:595`) |

### FA — faction actions (U:323, U:332, U:341, U:350, U:358, U:366)

| # | name | host | disp. | reader (KEY) | recovery predicate (DERIVED) | reason | dependency |
|---|---|---|---|---|---|---|---|
| 71 | treaty | `covenant`* | DERIVED | — | every covenant; no predicate in shipped play: low confidence | the generic name of the act | host row |
| 72 | peace | `covenant`* | DERIVED | — | a `release` of a live `commit` to a WAR Proposition: "peace = writing `until` on that edge" (`queries/faction_q.py:229-232`); readable, and never true in shipped play, where no WAR Proposition exists (`:234-235`) | the tree already says what peace is, and it is not a covenant term | none (`declare`* to produce a war) |
| 73 | alliance | `covenant`* | PARKED | — | — | no reader: `mustered` reads faction members only (FA-G07, `_part20:111`) | a reader of allies at a march's destination |
| 74 | truce | `covenant`* | DERIVED | — | no predicate in shipped play: low confidence | its only reader was a march refusal, which is forbidden (`_part20:110`) | host row |
| 75 | tribute (U:323) | `covenant`* | PARKED | — | — | a recurring due needs the covenant that names it | `covenant` |
| 76 | vassalage | `covenant`* | DERIVED | — | no predicate in shipped play: low confidence | performed by the vassal's `pledge` | host row |
| 77 | league | `covenant`* | DERIVED | — | the covenant has more than two parties; no predicate in shipped play: low confidence | a count, not a choice | host row |
| 78 | ransom terms | `covenant`* | PARKED | — | — | a captive must exist to ransom | `capture` (#3) |
| 79 | cession terms | `covenant`* | DERIVED | — | performed by a `give` of a Rung; no predicate in shipped play: low confidence | — | host row |
| 80 | war | `declare`* | DERIVED | — | the declared Proposition's mood is WAR (`WAR_MOOD`, `queries/faction_q.py:216`); no predicate in shipped play | the host's first mood | host row |
| 81 | enlist | `recruit`* | DERIVED | — | every `recruit`; no predicate in shipped play | names | host row |
| 82 | retain | `recruit`* | DERIVED | — | the recruit already holds a duty edge to the seat; no predicate in shipped play | names | host row |
| 83 | plot | `conspire`* | DERIVED | — | every `conspire`; no predicate in shipped play | names | host row |
| 84 | scheme | `conspire`* | DERIVED | — | as plot | names | host row |
| 85 | coup | `conspire`* | PARKED | eventual KEY | — | the plot has no executor (critique F) | an executor of the plot Proposition |
| 86 | post | `assign`* | DERIVED | — | the posting moves no containment; no predicate in shipped play | — | host row |
| 87 | envoy | `assign`* | DERIVED | — | the posted man holds an instrument given by the seat; no predicate in shipped play | — | host row |
| 88 | garrison a man | `assign`* | DERIVED | — | the posting's place is a `garrison` Site; no predicate in shipped play | — | host row |
| 89 | annex | `seize` | PARKED | — | — | `annex` is a ruled conferral BASIS (RO:2082), not a taking; re-parenting `contain` is unbuilt | M-ANNEX |
| 90 | conquer | `seize` | DERIVED | — | the seized subject is a Rung (`rung.seized`, VT:939) | — | none |
| 91 | take | `seize` | DERIVED | — | as conquer | — | none |

### EC — economy, trade and craft (U:382, U:390, U:404, U:413)

| # | name | host | disp. | reader (KEY) | recovery predicate (DERIVED) | reason | dependency |
|---|---|---|---|---|---|---|---|
| 92 | cultivate | `work` | PARKED | — | eventual: work at a `field` Site | no `field` site kind (RO:1358) | a `field` site kind |
| 93 | mine | `work` | DERIVED | — | the worked Site's kind is `seam` | — | none |
| 94 | fish | `work` | DERIVED | — | the worked Site's kind is `harbour`; low confidence (a harbour's yield is grain, so fishing cannot be told from harbour labour) | — | none |
| 95 | hunt | `work` | PARKED | — | — | "no carrier": stores do not tell wild from farmed food (`_part17:210`) | a wild-food carrier |
| 96 | mint | `craft`* | DERIVED | — | the product is `coin`; no predicate in shipped play | — | host row |
| 97 | pay | `transfer` | DERIVED | — | the act emitted `term.renewed` (VT:1310) | — | none |
| 98 | repay | `transfer` | PARKED | eventual KEY: closes a `debt` Record | — | no debt Record exists | `borrow`* |
| 99 | haul | `transfer` | DERIVED | — | every `transfer`; no predicate distinguishes it until M3 prices distance: low confidence | — | none |
| 100 | relieve (U:404) | `transfer` | DERIVED | — | as #68 | — | none |
| 101 | tribute (U:404) | `transfer` | DERIVED | — | the transfer pays a covenant's recurring due; no predicate in shipped play | — | `covenant` |
| 102 | trade | `exchange` | DERIVED | — | every `exchange`; no predicate in shipped play (the host never executes, VT:330-339) | — | host's `H-94` |
| 103 | buy | `exchange` | DERIVED | — | the actor's side gives `coin`; no predicate in shipped play | — | host's `H-94` |
| 104 | sell | `exchange` | DERIVED | — | the actor's side takes `coin`; no predicate in shipped play | — | host's `H-94` |
| 105 | barter | `exchange` | DERIVED | — | neither side is `coin`; no predicate in shipped play | — | host's `H-94` |
| 106 | bargain | `exchange` | PARKED | eventual KEY: contested price | — | no prize for a price | `H-94`; a price prize |

### WT — world, travel and survival (U:436)

| # | name | host | disp. | reader (KEY) | recovery predicate (DERIVED) | reason | dependency |
|---|---|---|---|---|---|---|---|
| 107 | navigate | `move` (U's `travel`) | PARKED | eventual KEY: a route-finding capability | — | the journey has no roll and no route | M-WT-1, M-WT-3 |
| 108 | ride | `move` | PARKED | — | eventual: the traveller's kit holds a mount | as navigate | M-WT-1 |
| 109 | sail | `move` | PARKED | — | eventual: the edge travelled is water | as navigate | M-WT-2 |

### NP — NPC life and persons (U:459, U:467, U:487, U:497, U:506)

| # | name | host | disp. | reader (KEY) | recovery predicate (DERIVED) | reason | dependency |
|---|---|---|---|---|---|---|---|
| 110 | heal | `tend`* | DERIVED | — | every `tend`; no predicate in shipped play | the ordinary word for tending a wound | host row |
| 111 | recover | `tend`* | DERIVED | — | `subject == actor`; no predicate in shipped play | — | host row |
| 112 | study | `train`* | DERIVED | — | `subject == actor`; no predicate in shipped play | the beneficiary column (`subject`) resolves to the actor anyway | host row |
| 113 | teach | `train`* | **KEY** | cell and counterparty (a pupil present) | — | a second side; `study` has none | host row; §3.1.9 |
| 114 | wed | `marry`* | DERIVED | — | every `marry`; no predicate in shipped play | — | host row |
| 115 | swear (U:497) | `pledge` (row `oblige`) | DERIVED | — | every `oblige` (identity) | "swear fealty"; the oath to a claim is #35 | none |
| 116 | cede | `give` | DERIVED | — | the given `hold` is on a Rung; no predicate in shipped play (`give` moves Records until widened) | — | host rebuild |

Dispositions that differ from the upload's fold by more than a word, and the test that decided each:
`recruit-for-coin` (writes differ), `sack` (witnesses; `surrender`), `confide` (a choice the draw cannot
make), `praise` and `insult` (a regard write), `propose` and `allege` (a value that varies the choice,
F-5), `threaten` (a disclosure the draw cannot make), `audit` and `scout` (eligibility and
precondition), `teach` (a second side). `besiege`, `capture` and the `marshal` choices would be keys
too, and wait on a carrier or an input nobody has built.
