# Verb to attribute map: Jordan's ten attributes against the verb roster

## Status: PROPOSED (2026-11-05). Reference under CLAUDE.md §0.05: nothing here binds the game or is read by it; merging ratifies nothing and decides nothing. Every row is `[ASSUMPTION; medium; Jordan to correct; revert: delete the row]` unless its basis column says CODE or RULED.
## Lane: IN
## Parts, in reading order: **this file** (the roster, the ten, the subsystem matrix, findings) · [part 2](2026-11-05-verb-attribute-map_part2.md) (the designed-verb lexicon)

**Question answered.** Which of the ten attributes (ED-IN-0328, Grace named by ED-IN-0333 item 3) does each verb's pool stand on? The verbs are the 92 of `proposals/verb_list.md` (coded and proposed) plus `argue`, which the coded table has and the roster omits. Every roster name is mapped; the check ran against both rosters (script output: roster missing none; one name outside the roster, `argue`).

**What is not changed.** `references/descriptor_registry.yaml` still names nine keys and Bonds, and stays IN FLUX until CR-84 rewrites it (ED-IN-0333). No `Person.attributes` carrier exists yet (CR-20). This map is the input to CR-20's closed `vocation_attribute` rows (keys: `verb_capability`'s values), which the plan sends to a judgment-tier verify pass; it writes none of them.

## 1. How to read it

A verb belongs to one of four classes, because capability supplies dice and gates nothing (`verb_table.yaml` header, quoting #353 §9.2): only a verb that draws a pool has an attribute to read.

| class | meaning | verbs |
|---|---|---|
| **R** | the season engine draws a pool for it now (a `contests:` prize, or `rosters.yaml: graded_inquiries`) | 12 |
| **D** | a draw is planned, proposed, or lives in a module off the season path | 13 |
| **P** | a performance with no draw built or ruled; the home is recorded for if one is given | 16 |
| **—** | no performance: an authority, a record write, a transfer, a choice | 52 |

**Primary** is the attribute the pool is built on; **Secondary** is a second contributor. Basis: **CODE** (a module or seam reads that attribute today), **RULED** (Jordan's words, cited), **REASONED** (this document's reading of the roster's effect text). Of the 12 R rows, four are CODE or RULED (`fight`, `accept`, `march`, `determine`); the rest are reasoned.

`faculty(w, p, verb)` (`engine/season/seam/wrappers/sigma.py:146`) takes one base per vocation under CR-20. A Secondary column therefore cannot be carried by CR-20 as written: it needs weights (the `faculties:` table of `proposals/2026-10-29-parliament-and-debate/2026-11-01-social-contest-proposal-4-authority-staged.md`, PROPOSED) or it is dropped.

## 2. The ten, against the registry as it stands

| Jordan's ten (ED-IN-0328) | registry now | change owed (CR-84) |
|---|---|---|
| Strength | `attr.body.strength` | none |
| Coordination | `attr.body.agility` (alias Dexterity) | rename |
| Endurance | `attr.body.endurance` | none |
| Reason | `attr.mind.acuity` (aliases Reasoning, Cognition) | rename |
| Focus | `attr.mind.focus` | none |
| Perception | alias of `attr.social.attunement` | own key |
| Attunement | `attr.social.attunement` | loses the alias |
| Presence | `attr.social.charisma` (alias Presence) | rename |
| Grace (alias Composure) | none | new key |
| Spirit | `attr.mind.will` (alias Spirit) | rename |
| (dropped) | `attr.social.bonds` | dropped by the ruled count of ten |

New key names are CR-84's to choose; none is invented here.

## 3. The map


### PC — personal combat

| verb | class | primary | secondary | basis | note |
|---|---|---|---|---|---|
| `fight` | R | composite |  | CODE | Combat reads seven fields: Strength, Coordination (`agi`), Endurance, Reason (`cog`), `att` (Perception; §5 finding 8), Spirit, Focus (`combatant.py:93`). Reads no Presence, Grace or Attunement in code; Attunement reads the opponent's emotional state by Jordan's description, unbuilt (finding 8). |
| `assassinate` | D | composite | Coordination | REASONED | `fight` with a held cover and the first move. |
| `capture` | D | composite |  | REASONED | `fight` with aim alive. |
| `challenge` | — |  |  |  |  |
| `accept` | R | composite |  | CODE | `fight`'s row, carried. |
| `guard` | — |  |  |  | Writes an edge; the fight it joins is `fight`'s. |
| `rescue` | D | composite |  | REASONED | A fight against the custodian's guards. |

### MB — mass battle

| verb | class | primary | secondary | basis | note |
|---|---|---|---|---|---|
| `levy` | — |  |  |  |  |
| `muster` | — |  |  |  |  |
| `drill` | — |  |  |  |  |
| `disband` | — |  |  |  |  |
| `marshal` | — |  |  |  | Writes the order-of-battle Record; the field reads it. |
| `march` | R | Presence | Reason | CODE | `derive_command(charisma, cognition)` weights 2:1 (`modules/mass_battle/core/exchange.py`, `config.py:532`); Officer units only. |
| `supply` | — |  |  |  |  |
| `forage` | — |  |  |  |  |
| `surrender` | — |  |  |  |  |

### SC — social contest

| verb | class | primary | secondary | basis | note |
|---|---|---|---|---|---|
| `tell` | R | Presence | Grace | REASONED | Contested against the hearer's standing; Grace is the dignity the telling is received with (Jordan, 2026-11-05). `verb_capability` maps it to the vocation `copying`. |
| `persuade` | D | Presence | Attunement | REASONED | Moves the hearer's pursuits, so it works through understanding what the hearer wants (Jordan, 2026-11-05). "By reason" leans on Reason instead; one key cannot hold both modes. |
| `utter` | — |  |  |  |  |
| `commit` | — |  |  |  |  |
| `petition` | P | Grace | Presence | REASONED | The seatless person's upward channel: the form of address is the performance. No draw built. [CONFIDENCE: low] |
| `lodge` | — |  |  |  | Coded as `carry`. |
| `convene` | — |  |  |  |  |
| `open_case` | — |  |  |  |  |
| `speak` | R | Presence | Grace | REASONED | Contested on "a matter" at a sitting; address is judged on decorum as well as force (Jordan, 2026-11-05). |
| `determine` | R | Reason | Attunement | RULED | ED-IN-0326: reasoning sharpens judgment of offices, regimes and obligations; attunement, of persons. |
| `argue` | R | Reason | Presence | REASONED | Coded, not in the roster: the charge's disposition at a sitting (`contests: "a proposition"`). Distinct from `persuade`. |
| `interrogate` | R | Attunement | Presence | REASONED | Contested against the prisoner's resistance; the resisting side is §5 finding 2. |

### FI — fieldwork and inquiry

| verb | class | primary | secondary | basis | note |
|---|---|---|---|---|---|
| `examine` | R | Perception | Focus | REASONED | Graded through `social_contest.roll` (`rosters.yaml: graded_inquiries`). |
| `research` | R | Reason | Focus | REASONED | As `examine`; tells a forgery from a true Record. |
| `watch` | R | Perception | Coordination | REASONED | Coded as `surveil`. Coordination is not being seen watching. |
| `interview` | P | Attunement |  | REASONED | No degree on the asker by ruling (#453 K-36): the questioned person answers by his own `tell`. |
| `reconstruct` | P | Reason | Perception | REASONED | Waits on a value space nothing supplies (K-37). Perception for what the ledger is missing. |
| `survey` | P | Perception | Reason | REASONED | Fieldwork: what is there, what is out of place, what is absent (Jordan, 2026-11-05). [CONFIDENCE: low] |
| `conceal` | P | Grace |  | REASONED | Holding a cover under scrutiny: the "remain calm, etiquette and manners" half of Jordan's Grace. [CONFIDENCE: low] |
| `infiltrate` | P | Grace | Attunement | REASONED | As `conceal`; Attunement for what the seat will look for. [CONFIDENCE: low] |
| `forge` | P | Focus | Coordination | REASONED | Forgery quality is error-avoidance, Jordan's Focus gloss. |
| `create_record` | — |  |  |  |  |
| `destroy_record` | — |  |  |  |  |
| `bribe` | P | Attunement | Grace | REASONED | Knowing what the payee wants; Grace in not being caught. [CONFIDENCE: low] |

### TW — threadwork

| verb | class | primary | secondary | basis | note |
|---|---|---|---|---|---|
| `thread_read` | D | Spirit |  | CODE | Pool is `2·spirit + min(3, history+3) + ts//10` (`systems/threadwork/sim/operations.py`); off the season path. |
| `weave` | D | Spirit | Focus | REASONED |  |
| `lock` | D | Spirit | Focus | REASONED |  |
| `dissolve` | D | Spirit | Focus | REASONED |  |
| `mend` | D | Spirit | Focus | REASONED |  |
| `ward` | D | Spirit |  | REASONED | Hostile workings resolve in an opposed roll against the warder. |
| `knot` | D | Spirit |  | CODE | Rolls on `spirit` (`systems/fieldwork/sim/knots.py`); its gate and cap read `bonds`, which the ten drop (§5 finding 4). |

### GV — settlements and governance

| verb | class | primary | secondary | basis | note |
|---|---|---|---|---|---|
| `confer` | — |  |  |  |  |
| `revoke` | — |  |  |  |  |
| `establish` | — |  |  |  |  |
| `succeed` | — |  |  |  |  |
| `release` | — |  |  |  |  |
| `issue` | — |  |  |  |  |
| `order` | — |  |  |  | Coded as `dispatch`. |
| `comply` | — |  |  |  |  |
| `evade` | — |  |  |  | Coded in `evade / defy`. A choice; its detection is the issuer's, not a pool of the actor. |
| `defy` | — |  |  |  | Coded in `evade / defy`. |
| `construe` | — |  |  |  |  |
| `proclaim` | — |  |  |  |  |
| `tax` | — |  |  |  |  |
| `requisition` | — |  |  |  |  |
| `ration` | — |  |  |  |  |
| `arrest` | R | Presence | Strength | REASONED | `contests: "a standing"`; the row records "a standing or the body" as open [ASSUMPTION; medium]. |
| `pardon` | — |  |  |  |  |
| `found` | — |  |  |  |  |
| `build` | — |  |  |  |  |
| `raze` | — |  |  |  |  |

### FA — faction actions

| verb | class | primary | secondary | basis | note |
|---|---|---|---|---|---|
| `covenant` | P | Grace | Presence | REASONED | A seat's offer or seal of terms between seats; ceremony and conduct, no draw built. [CONFIDENCE: low] |
| `declare` | — |  |  |  |  |
| `recruit` | D | Presence | Attunement | REASONED | The roster's contested offer of service: knowing what the recruit wants. The coded `recruit` is a troop-Record write (no draw). |
| `conspire` | D | Presence | Attunement | REASONED |  |
| `assign` | — |  |  |  |  |
| `seize` | — |  |  |  |  |
| `sabotage` | P | Coordination | Focus | REASONED | [CONFIDENCE: low] |

### EC — economy, trade and craft

| verb | class | primary | secondary | basis | note |
|---|---|---|---|---|---|
| `work` | P | Endurance | Strength | REASONED | Labour is staged on a Site and tallied; no draw. [CONFIDENCE: low] |
| `craft` | P | Coordination | Focus | REASONED | [CONFIDENCE: low] |
| `restore` | P | Coordination | Focus | REASONED | [CONFIDENCE: low] |
| `transfer` | — |  |  |  |  |
| `exchange` | — |  |  |  | The price is read from stock, not rolled. |
| `hire` | — |  |  |  |  |
| `borrow` | — |  |  |  |  |
| `lend` | — |  |  |  |  |

### WT — world, travel and survival

| verb | class | primary | secondary | basis | note |
|---|---|---|---|---|---|
| `travel` | P | Endurance | Perception | REASONED | Coded as `move`. [CONFIDENCE: low] |
| `migrate` | — |  |  |  | Throttled by settlement capacity. |
| `explore` | P | Perception | Endurance | REASONED |  |

### NP — NPC life and persons

| verb | class | primary | secondary | basis | note |
|---|---|---|---|---|---|
| `tend` | P | Reason | Attunement | REASONED | [CONFIDENCE: low] |
| `train` | — |  |  |  | Writes `Person.capability`; the trained key's own base decides the pupil's pool, so `train` inherits and adds no attribute. |
| `forgive` | — |  |  |  |  |
| `tie` | — |  |  |  |  |
| `marry` | — |  |  |  |  |
| `pledge` | — |  |  |  | Coded as `oblige`. |
| `defect` | — |  |  |  |  |
| `give` | — |  |  |  |  |

## 4. By subsystem

Jordan, 2026-11-05 (in session, not a ledger row): *it is okay for some of these attributes to be niche.* A niche attribute is therefore not a defect below; it is reported so the choice is visible.

Jordan, 2026-11-05 (in session, not a ledger row), on Grace: *social contest can also use Grace. Having a strong presence/commanding aura without having the required dignity or etiquette (ie grace) for the occasion is a thing. Grace will involve a lot of interactions with being seen as respectable/dignified and often ties into views of royal conduct.* The SC rows below carry Grace as Presence's partner, not its rival.

Jordan, 2026-11-05 (in session, not a ledger row), on Perception: *perception is relevant to things like surveillance and fieldwork and noticing things out of place or discerning something is missing intuitively etc.* Perception is therefore the primary of the inquiry verbs that observe (`examine`, `watch`, `survey`, `explore`) and the secondary of `reconstruct`, which has to notice what the ledger lacks.

Jordan, 2026-11-05 (in session, not a ledger row), adding to that: *this means that perception will impact how much any given character will know about something and therefore impact their choices*, and, on being asked nothing further, *but it concerns FACTUAL matters.* With ED-IN-0326 that gives the knowledge model three readers, each on its own kind of matter: **Perception** on facts (what is the case, what is out of place, what is missing), **Attunement** on persons' minds (intentions, pursuits, convictions, goals), **Reason** on offices, regimes and obligations.

Jordan, 2026-11-05 (in session, not a ledger row), on Attunement: *attunement helps with understanding other characters in terms of their intentions in a given moment as well as their pursuits, convictions, ambitions, goals, desires etc.* This extends ED-IN-0326 (pursuits and convictions) to intentions in the moment, so Attunement is the secondary of every verb that works through the other party's wants (`persuade`, `recruit`, `determine`) and the primary of the verbs that read them (`interrogate`, `interview`, `bribe`).

Cells read **primary / secondary** verb counts; **c** is a composite read inside personal combat (`fight` and kin; `modules/combat/combatant.py:93`); **·** is none. Subsystems are the roster's lanes. Module reads that are not verbs: mass battle's `derive_command` (Presence 2 : Reason 1) is the `march` row; threadwork's pool and the knot roll (Spirit) are the D rows; the knot gate and cap read `bonds` (§5, finding 4).

| attribute | PC | MB | SC | FI | TW | GV | FA | EC | WT | NP | subsystems with a primary |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Strength | c | · | · | · | · | /1 | · | /1 | · | · | 0 |
| Coordination | /1+c | · | · | /2 | · | · | 1 | 2 | · | · | 2 |
| Endurance | c | · | · | · | · | · | · | 1 | 1/1 | · | 2 |
| Reason | c | /1 | 2 | 2/1 | · | · | · | · | · | 1 | 3 |
| Focus | c | · | · | 1/2 | /4 | · | /1 | /2 | · | · | 1 |
| Perception | c | · | · | 3/1 | · | · | · | · | 1/1 | · | 2 |
| Attunement | · | · | 1/2 | 2/1 | · | · | /2 | · | · | /1 | 2 |
| Presence | · | 1 | 3/3 | · | · | 1 | 2/1 | · | · | · | 4 |
| Grace | · | · | 1/2 | 2/1 | · | · | 1 | · | · | · | 3 |
| Spirit | c | · | · | · | 7 | · | · | · | · | · | 1 |

Reading it by subsystem:

- **Demand sits in four lanes.** SC (Presence, Reason, Attunement, Grace), FI (Reason, Perception, Attunement, Grace, Focus), TW (Spirit, Focus) and PC (seven attributes, composite). MB reads two (Presence, Reason) through one verb.
- **GV, NP and most of EC read almost nothing through a verb's pool.** Offices, writs, stores and bonds resolve by remit, hold or price, not by a person's pool. Perception reaches them another way, as the knowledge a holder acts on (a governor noticing low grain before `ration`, `requisition` or `transfer`; §5 finding 9), which no verb row shows. Of their 36 rows, 4 have a performance (`work`, `craft`, `restore`, `tend`, all P) and one draws (`arrest`, R). That follows the roster's own rule that capability gates nothing; it is not a gap in the map.
- **Presence does not meet personal combat, and Attunement meets it only by Jordan's description, for which combat has no carrier (§5 finding 8);** Strength, Endurance and Coordination do not meet the social lanes. The body attributes and the social attributes are served by disjoint subsystems, bridged only by `arrest` (Presence, Strength) and by Reason and Perception, the two attributes that appear in both a body lane (PC) and a social or inquiry lane.
- **Niche attributes, accepted:** Strength (combat plus two secondaries), Spirit (threadwork primaries; combat's `conc_max`), Coordination (FI and EC craft). Presence is the least niche (four lanes with a primary), then Reason (three).

## 5. Coverage, and what it shows

Primary counts over single-attribute rows ("of which R / D" counts those that draw); `fight`, `accept`, `capture`, `rescue` and `assassinate` are composite and excluded from primaries.

| attribute | primary | of which R / D | secondary |
|---|---|---|---|
| Strength | 0 | 0 | 2 |
| Coordination | 3 | 0 | 3 |
| Endurance | 2 | 0 | 1 |
| Reason | 5 | 3 | 2 |
| Focus | 1 | 0 | 9 |
| Perception | 4 | 2 | 2 |
| Attunement | 3 | 1 | 6 |
| Presence | 7 | 7 | 4 |
| Grace | 4 | 0 | 3 |
| Spirit | 7 | 7 | 0 |

Findings, worst first:

1. **Strength has no single-key home (niche; accepted, §4).** It is a combat read and the Secondary of `arrest` and `work`; no verb that rolls on one attribute puts Strength first. If Strength is to matter outside a fight, a verb must be given a draw on it (`work`, `build`, `raze` are the candidates); otherwise it is a combat attribute only.
2. **Grace has no defender-side key under CR-20, and its royal-conduct half is a reader, not a pool.** Its primaries are performances with no draw (`conceal`, `infiltrate`, `petition`, `covenant`, all P); in the R verbs it is Presence's secondary (`tell`, `speak`). Resisting `interrogate` or `arrest` is where "remain calm under pressure" lives, and `_opposition_of` reads the party's key for the *same verb* (`sigma.py`), which for those verbs is Attunement and Presence, not the party's Grace or Spirit. A separate resistance key would be a new mechanism and is not proposed. The other half of Jordan's description, being *seen as* respectable and its tie to royal conduct, is how others read a person: a reader of standing or stance (`tell` is already contested "against the hearer's standing"), which no verb row can show (§5 finding 11). [ASSUMPTION; medium; Jordan to correct]
3. **Presence is the primary of seven rows, four of them R** (`tell`, `speak`, `march`, `arrest`); Reason of three R rows (`determine`, `argue`, `research`). Presence has the most R rows of any single attribute.
4. **The knot gate has no reader.** `systems/fieldwork/sim/knots.py` gates on `bonds` (`KNOT_BONDS_MIN`) and caps on `bonds//2+1`; Bonds is dropped. A6's proposal was to read Charisma; nothing is decided. The cap and gate are off the season path today.
5. **Spirit is a single-subsystem attribute (niche; accepted, §4).** All seven of its primaries are threadwork (D). Spirit's other reader is combat (`conc_max = 3F+2S`).
6. **Focus is almost wholly a Secondary (niche; accepted, §4)** (9 rows, 1 primary), the orphan A6 reported for the nine; Jordan's gloss ("avoiding errors") has made it the natural Secondary of every precision verb rather than the main input of any. Combat reads it five ways as a composite (§5 finding 13), so the count understates it there.
7. **Twelve verbs draw today**, and two have a CODE or RULED attribute outside combat (`march`, `determine`). The rest of the map is inert until CR-20 lands `Person.attributes` and `faculty` reads a `vocation_attribute` row; today only `tell` and `speak` map to a vocation, `copying`, and one authored person holds it (docket `07_social_fieldwork.md`).
8. **Combat's `att` is Perception, on both of its reads.** Jordan (2026-11-05, in session, not a ledger row): *perception will tie into combat because it involves seeing what your opponent is actually doing as per cognitive processing.* `reading(c) = (2·cog + att)/3` and `reflex(c)` both take `att` (`modules/combat/combat_systems.py:171-172`): reading what the opponent is doing, and responding to it. Both are Perception, with Reason (`cog`) as the processing half of `reading`. The line between the two readers is therefore *actual action* (Perception) against *intention* (Attunement), and combat as built reads only the first. [CORRECTION: an earlier draft of this finding put `reading` on Attunement; Jordan's description puts it on Perception.] CR-84 gives Perception its own key, `attr.mind.perception`, and the knowledge-model plan named it the candidate for PC-14's `att` registry key (null today); as built, combat has no reader of Attunement.

   Attunement does have a combat role, on Jordan's later description (2026-11-05, in session, not a ledger row): *attunement has involvement in combat because it involves reading the current emotional state of your opponent, and emotional states (anxious, angry, etc) should be colouring what actions a combatant may take.* So Attunement reads the opponent's emotional state, and the emotional state is a condition that shapes a combatant's action set. Neither half exists in the tree: `modules/combat` has no emotional-state quantity (no match for `anxi`, `anger`, `emotion` or `panic`), its only temperament is the static `disp` aggression axis (`combatant.py:99`, `lean = (disp-4)/3`), and `Person` carries none (`Proposition.mood` is a grammatical mood, not a feeling). The nearest existing quantity is mass battle's morale, which is a unit's, not a person's. The map therefore records the link as designed and unbuilt: a carrier for a combatant's emotional state and a rule by which it colours the available actions, with Attunement as the opponent's reader, are PC-14's or a character-state design's to supply. Not decided. [ASSUMPTION; medium; Jordan to correct]
9. **Perception's largest effect is not a verb's pool; it is what a person comes to know.** On Jordan's description it sets how much of the factual record a character holds, and so which options they weigh. The verb rows above show only the active half (`examine`, `watch`, `survey`, `explore`). The passive half is WITNESS: `observers_for` and the `seen` deposit (`engine/season/epistemic.py:794`, `loop/witness.py`) admit a person by channel (co-location, a knot, a document, a purview) and read no attribute (no match for `attributes` or `perception` in either file, 2026-11-05); the `total` arm credits everyone uniformly. Nothing in the tree lets one person see more of the same Event than another because of who they are. Jordan's example (2026-11-05, in session): *someone governing a settlement with high perception [is] more likely to notice that grain stores are low.* The code path for exactly that case exists and is uniform: MATTER's larder pass records a drained larder's `shortfall:<kind>` read, and `witness` deposits it, as an `inferred` claim through the seat channel, to every governor whose purview contains the rung (`loop/witness.py:491-524`, `world_q.governors_of`). Every governor in reach learns it at the same confidence; Perception would be the factor that makes the lord of a fed town and the lord of a starving one differ in what they notice, and when. CR-83 (familiarity sets inference and adjudication, B10-13, design-first) names Attunement and Reason through ED-IN-0326 and not Perception; this clause belongs beside it as the factual third. Not decided: whether Perception thins the deposit (fewer claims, lower confidence) or gates it (a claim is or is not held), and whether it acts on `seen` only or on every channel. [ASSUMPTION; medium; Jordan to correct]

10. **An attribute reaches a choice by one path today, and only for the 12 R verbs.** Jordan (2026-11-05, in session, not a ledger row): *these attribute capabilities are to be combined with pursuits, convictions, ambitions, goals, obligations, demands etc. to provide weighting for the best course of action available to that character.* The chooser's score is `pursuit + stance` (`decision/choose.py:171`, `score_terms`); the pursuit term is `Σ axis_w · align(verb, axis)` times `odds_weight`, the person's believed chance on a contested candidate (CR-17). That believed chance is built from the believer's own `faculty` (`seam/wrappers/sigma.py`, `odds_of`, the stated exception to the own-ledger rule), so an attribute weights a choice only through the pool of a verb that rolls. For the 54 verbs of class — and the P rows, which have no draw, an attribute weights nothing: a governor's Perception cannot make `ration` more attractive, and a ruler's Grace cannot make `covenant` more attractive, except through what they know (finding 9). The option set is untouched by design (`capability` gates nothing; probe P11), so what Jordan describes is a *weighting* term, which is what is missing for uncontested candidates. This map supplies the data such a term would read (a primary and secondary per verb); the term, and whether obligations and demands enter the same score, are not decided here, and `score_terms` carries no obligation or ambition term today. [ASSUMPTION; medium; Jordan to correct]

11. **Grace is a reader of regard, and regard is already independent of office rank.** Jordan (2026-11-05, in session, not a ledger row): *someone can occupy an office of low standing but have high grace, which will make people think well of them despite their standing.* In the code, how a person is thought of is `regard(p, referent)` = the holder's stored stance plus judged deeds plus told valence (`queries/person_q.py:397`), and a bench's disposition toward a speaker is `reception` (`queries/world_q.py:678`), a sum over the bench's held deeds of the speaker. Neither reads an attribute, and neither reads the rank of the office the person holds; so the "despite their station" half already holds, and what is missing is the Grace term. Where it would enter (an added term in `regard` and `reception`, a prior before deeds accumulate, or both) is not decided. **Three things share the word standing and must stay apart:** an office's rank (an ordinal in `rung_kinds`, `REMOVE_ORDINAL`), the code's `standing` (`options.py:1380`, `standing_of`: the gap between what others tell of a person and what that person holds of themself, zero meaning agreement, the opposite polarity to reputation), and regard. Jordan's sentence uses the first and the third. [ASSUMPTION; medium; Jordan to correct]

12. **Presence's command half shows in one verb.** Jordan (2026-11-05, in session, not a ledger row): *presence moreso concerns the ability to notice and to influence and command.* Jordan then confirmed the reading (2026-11-05, in session): *presence is about being noticed, not noticing things.* Noticing things is Perception, so the two do not overlap. The influence rows are mapped (`tell`, `speak`, `persuade`, `recruit`, `conspire`, `arrest`). The command rows are not: only `march` and mass battle's in-battle orders draw (Presence 2 : Reason 1, `derive_command`). The verbs by which a person commands (`order`, `assign`, `levy`, `muster`, `marshal`) are class — and weight nothing, so a commanding Presence changes whether an order is given or obeyed in no row. Obeying is the receiver's choice (`comply`, `defy`, `evade`), also class —. That is finding 10's gap seen from Presence: the weighting term would have to act on the receiver's choice, not on a roll. Being noticed has no reader at all (the fan-out is by channel, finding 9). Not decided. [ASSUMPTION; medium; Jordan to correct]

13. **Combat already builds Focus as an error rate; the pain half is partly there and the inattention half is not.** Jordan (2026-11-05, in session, not a ledger row): *focus also affects combat because it impacts your rate of making errors due to lapses in concentration whether that be due to inattention or pain.* Combat reads Focus five ways (`modules/combat/combat_systems.py`, `combatant.py`): the concentration reserve `conc_max = 3F + 2S` (`combatant.py:147`); `consistency(c)`, a sigma term that falls as the reserve is spent (`:1423`, the spread of the fighter's outcomes, which is the error rate in this model); `mental_fatigue` (`:1427`); `disrupt_resist_p`, the chance of completing a strike despite being hit, logistic in Focus (`:1449`); and `poise_regen` (`:1436`). **Pain** reaches it by one route: every hit drains the reserve by `CONC_DRAIN_HIT` (`wrapper.py:194, 226, 395, 420`), so a wounded fighter makes more errors; the drain is per hit, not a function of the wound's severity or the accumulated wound state. **Inattention** has no source: nothing lowers the reserve for a fighter who is distracted, outnumbered or watching two opponents. Spirit is the reserve's other term (`2S`), so Focus alone sets the error rate only at a fixed reserve. Focus is thus richer in combat than finding 6's secondary count shows (combat reads it as composite, not as a verb's secondary). Not decided: whether wound severity should drain the reserve, and what the inattention source would be. [ASSUMPTION; medium; Jordan to correct]

14. **Focus's other half, resisting distraction and irrelevant information, has one natural home in the chooser: the noise level.** Jordan (2026-11-05, in session, not a ledger row): *high focus characters are less likely to be distracted as well as less likely to have irrelevant information impact their choices.* The chooser ranks candidates by `pursuit + stance` and then samples an order from `softmax(score / tau)` (`decision/choose.py:352-390`), where `tau` is the fixture `choice_temperature`, one value for every person. A person's attention to irrelevant things therefore has no channel except that noise and the stance term. A per-person `tau` falling with Focus would give "less swayed by what does not matter" without a new term; `_sample_order` already receives the person `p`, so the change is local. Distraction in combat (finding 13's missing inattention source) and in choice would then be one quantity read twice, not two mechanisms. Not decided, and it moves every seeded choice, so it is a golden re-record whenever it lands. [ASSUMPTION; medium; Jordan to correct]

15. **Reason's choice-side role has no reader, and Focus is its reliability, not a verb's secondary.** Jordan (2026-11-05, in session, not a ledger row): *reason concerns mental acuity, logic, understanding of concepts/facts, forecasting, understanding what a choice entails; but if you have low focus then you may make avoidable errors or fail to filter and prioritize correctly so your forecast includes irrelevant info.* On the verb side Reason is mapped where it argues, judges or infers (`determine`, `argue`, `research`, `reconstruct`, `counsel`, `refute`, `object`, `define`, `navigate`). On the choice side it has nothing to act on: `score_terms` uses `align(verb, axis)`, a table keyed by verb and axis alone (`data/verbs.py:1874`), so what a choice entails is the same for every chooser, and the believed chance (`odds_of`) is computed exactly from the chooser's own ledger and pool, with no error that Reason shrinks or Focus enlarges. Both are the places a forecast lives, and neither varies by person. Two consequences for this map. (a) Focus relates to Reason as a **modifier on the reliability of every Reason-based result** (errors, irrelevant material in the forecast), not as a Secondary of any one verb; the Secondary column, one slot per verb, cannot say it, and Focus is already the Secondary of `research` and `reconstruct` only incidentally. (b) Combat already treats Focus this way: `consistency(c)` is a sigma term, a spread of outcomes, that falls with the concentration reserve (finding 13). The same shape (Focus as a spread on a Reason-based forecast or roll) would be the unified reading, with the roll's own `leverage` (`sigma.py:261`) as the existing sigma input; that is a suggestion about shape, not a design. Findings 13, 14 and this one describe one quantity read at three sites: a fighter's strike, a chooser's order, a forecaster's estimate. Not decided. [ASSUMPTION; medium; Jordan to correct]

## 6. Not covered

- **Combat's composite.** `fight` and kin are owned by PC-14 (`modules/combat/attributes.py`, unbuilt); `att` is Perception (finding 8); PC-14 owns the key. Histories are being eliminated as a roll input (ED-IN-0330, ED-IN-0333 item 4); combat's `history` read is outside this map.
- **Verbs the roster parks or does not name.** The designed-verb lexicon is mapped in [part 2](2026-11-05-verb-attribute-map_part2.md).
- **Skills.** A skill is a capability key on a base attribute (ED-IN-0330); this map names the base only.
