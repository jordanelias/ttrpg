# Verb to attribute map, part 2: the designed-verb lexicon

## Status: PROPOSED (2026-11-05). Reference under CLAUDE.md §0.05: nothing here binds the game or is read by it; merging ratifies nothing and decides nothing. Every row is `[ASSUMPTION; medium; Jordan to correct; revert: delete the row]` unless its basis column says CODE.
## Lane: IN
## Parts, in reading order: [part 1](2026-11-05-verb-attribute-map.md) (the roster, the ten, the subsystem matrix, findings) · **this file** (the lexicon names)

**Scope.** The lexicon tables of `proposals/2026-10-16-verbs/2026-10-16-verbs-09` to `-18` (one per subsystem lane; the SC table is `verbs-11` §3.4). Every name those tables list that is not already a row of part 1, and is not CULLED, is mapped here: 159 rows, 147 distinct names (a name two lanes both list is two rows). The 31 CULLED names are listed in §3 and not mapped: their lane removed them.

**How a lexicon name is read.** A FOLDED name is a mode, a content label or a parameter of a host row (`testify` is `tell` to a bench member), so it **inherits the host's class, primary and secondary** from part 1. 47 rows override the host, because the lane's own mechanic column names a different pool; each says why. A class on a folded name is the host's: **the 12 R hosts of part 1 are unchanged**, and no folded name adds a verb that draws. PARKED names are mapped as designed (class P or D) and stay parked.

Jordan's in-session remarks on Grace, Attunement and Perception (2026-11-05) are quoted in part 1 §4 and applied here.

**What was read.** The mechanic column of each lexicon table (the first words of each row), not the suites' bodies. An override that the suite text would contradict is the likeliest error here. [GAP: suite bodies of `verbs-09` to `-18` not read.]

## 1. The map


### PC — personal combat

| name | status | host | class | primary | secondary | basis | note |
|---|---|---|---|---|---|---|---|
| `ambush` | FOLDED | `fight` | R | composite |  | CODE | inherits `fight` |
| `shoot` | FOLDED | `fight` | R | composite |  | CODE | inherits `fight` |
| `champion` | FOLDED | `challenge` | — |  |  |  | inherits `challenge` |
| `yield` | FOLDED | `fight` | R | composite |  | CODE | inherits `fight` |
| `flee` | FOLDED | `fight` | R | composite |  | CODE | inherits `fight` |
| `lunge` | FOLDED | `fight` | R | composite |  | CODE | inherits `fight` |
| `feint` | FOLDED | `fight` | R | composite |  | CODE | inherits `fight` |
| `parry` | FOLDED | `fight` | R | composite |  | CODE | inherits `fight` |
| `dodge` | FOLDED | `fight` | R | composite |  | CODE | inherits `fight` |
| `grapple` | FOLDED | `fight` | R | composite |  | CODE | inherits `fight` |
| `interpose` | FOLDED | `fight` | R | composite |  | CODE | inherits `fight` |

### MB — mass battle

| name | status | host | class | primary | secondary | basis | note |
|---|---|---|---|---|---|---|---|
| `garrison` | FOLDED | `muster` | — |  |  |  | inherits `muster` |
| `rally` | FOLDED | `march` | D | Presence | Reason | CODE | In-battle order on the Command pool, `derive_command` (Presence 2 : Reason 1); `rally_check` and `recall_check` are the module's own draws. (host `march`) |
| `pursue` | FOLDED | `march` | D | Presence | Reason | CODE | In-battle order on the Command pool, `derive_command` (Presence 2 : Reason 1); `rally_check` and `recall_check` are the module's own draws. (host `march`) |
| `retreat` | FOLDED | `march` | D | Presence | Reason | CODE | In-battle order on the Command pool, `derive_command` (Presence 2 : Reason 1); `rally_check` and `recall_check` are the module's own draws. (host `march`) |
| `withstand` | FOLDED | `march` | D | Presence | Reason | CODE | In-battle order on the Command pool, `derive_command` (Presence 2 : Reason 1); `rally_check` and `recall_check` are the module's own draws. (host `march`) |
| `storm` | FOLDED | `march` | R | Presence | Reason | CODE | inherits `march` |
| `besiege` | FOLDED | `march` | R | Presence | Reason | CODE | inherits `march` |
| `provision` | FOLDED | `supply` | — |  |  |  | inherits `supply` |
| `equip` | FOLDED | `supply` | — |  |  |  | inherits `supply` |
| `sack` | FOLDED | `forage` | — |  |  |  | inherits `forage` |
| `encamp` | NEW | `supply` | — |  |  |  | Halts the force on a `camp` Site; waits M-1, M-12. (host `supply`) |
| `reconnoitre` | PARKED | `examine` | P | Perception | Reason | REASONED | Military claims about a target from range. PARKED. [CONFIDENCE: low] (host `examine`) |
| `ambush` | PARKED | `fight` | P | Perception | Reason | REASONED | A hidden force sets the first mover. PARKED. [CONFIDENCE: low] (host `fight`) |

### SC — social contest

| name | status | host | class | primary | secondary | basis | note |
|---|---|---|---|---|---|---|---|
| `testify` | FOLDED | `tell` | R | Presence | Grace | REASONED | inherits `tell` |
| `confess` | FOLDED | `tell` | R | Presence | Grace | REASONED | inherits `tell` |
| `confide` | FOLDED | `tell` | R | Presence | Grace | REASONED | inherits `tell` |
| `warn` | FOLDED | `tell` | R | Presence | Grace | REASONED | inherits `tell` |
| `confront` | FOLDED | `tell` | R | Presence | Grace | REASONED | `tell` with `to == subject`: Grace is nerve in the face of the subject. [CONFIDENCE: low] (host `tell`) |
| `praise` | FOLDED | `tell` | R | Attunement | Presence | REASONED | Knowing what will please; needs the regard reader (H-194, H-196). (host `tell`) |
| `flatter` | FOLDED | `tell` | R | Attunement | Presence | REASONED | Knowing what will please; needs the regard reader (H-194, H-196). (host `tell`) |
| `insult` | FOLDED | `tell` | R | Presence | Attunement | REASONED | Same reader as `praise`. (host `tell`) |
| `counsel` | FOLDED | `tell` | R | Reason | Presence | REASONED | A `tell` whose subject is an OUGHT Proposition the teller holds. (host `tell`) |
| `preach` | PARKED | `persuade` | D | Presence | Attunement | REASONED | inherits `persuade` |
| `propose` | FOLDED | `utter` | — |  |  |  | inherits `utter` |
| `allege` | FOLDED | `utter` | — |  |  |  | inherits `utter` |
| `threaten` | FOLDED | `utter` | P | Presence | Spirit | REASONED | Mood THREAT, "needs a reader"; no draw. [CONFIDENCE: low] (host `utter`) |
| `vote` | FOLDED | `utter` | — |  |  |  | inherits `utter` |
| `swear` | FOLDED | `utter` | — |  |  |  | inherits `utter` |
| `accuse` | FOLDED | `utter` | — |  |  |  | inherits `utter` |
| `deny` | FOLDED | `release` | — |  |  |  | inherits `release` |
| `withdraw` | FOLDED | `release` | — |  |  |  | inherits `release` |
| `adjourn` | FOLDED | `utter` | — |  |  |  | inherits `utter` |
| `plead` | FOLDED | `speak` | R | Presence | Grace | REASONED | inherits `speak` |
| `refute` | FOLDED | `speak` | R | Reason | Presence | REASONED | A speech kind (`cite_incompatible`, translative, definitional): argument over address. (host `speak`) |
| `concede` | FOLDED | `speak` | R | Grace | Reason | REASONED | Speech kinds `concede_fact`, `concede_harm`: admitting under pressure. [CONFIDENCE: low] (host `speak`) |
| `object` | FOLDED | `speak` | R | Reason | Presence | REASONED | A speech kind (`cite_incompatible`, translative, definitional): argument over address. (host `speak`) |
| `define` | FOLDED | `speak` | R | Reason | Presence | REASONED | A speech kind (`cite_incompatible`, translative, definitional): argument over address. (host `speak`) |
| `arbitrate` | FOLDED | `determine` | R | Reason | Attunement | RULED | inherits `determine` |
| `mediate` | PARKED | `persuade` | P | Attunement | Presence | REASONED | Non-binding go-between; no disposal. PARKED. (host `persuade`) |
| `negotiate` | PARKED | `covenant` | P | Attunement | Presence | REASONED | Reading the other side's intentions and goals; the offer of terms is FA's `covenant`. PARKED. (host `covenant`) |
| `filibuster` | PARKED | `speak` | P | Endurance | Presence | REASONED | A speech kind that spends the sitting's clock. PARKED. [CONFIDENCE: low] (host `speak`) |
| `lie` | PARKED | `tell` | P | Grace | Presence | REASONED | A `tell` of a claim not held; sits beside `forge` (ED-IN-0329). PARKED (J-C-6). [CONFIDENCE: low] (host `tell`) |

### FI — fieldwork and inquiry

| name | status | host | class | primary | secondary | basis | note |
|---|---|---|---|---|---|---|---|
| `search` | FOLDED | `examine` | R | Perception | Focus | REASONED | inherits `examine` |
| `track` | FOLDED | `examine` | R | Perception | Focus | REASONED | inherits `examine` |
| `decipher` | FOLDED | `research` | R | Reason | Focus | REASONED | inherits `research` |
| `shadow` | NEW | `watch` | P | Coordination | Perception | REASONED | Person-bound; co-moves with the quarry. PARKED. [CONFIDENCE: low] (host `watch`) |
| `eavesdrop` | FOLDED | `watch` | R | Perception | Coordination | REASONED | inherits `watch` |
| `intercept` | PARKED | `examine` | P | Perception | Coordination | REASONED | A Record in transit. PARKED, no host. [CONFIDENCE: low] (host `examine`) |
| `trace` | PARKED | `thread_read` | D | Spirit |  | CODE | inherits `thread_read` |
| `audit` | FOLDED | `survey` | P | Perception | Reason | REASONED | inherits `survey` |
| `census` | FOLDED | `survey` | P | Perception | Reason | REASONED | inherits `survey` |
| `scout` | FOLDED | `survey` | P | Perception | Reason | REASONED | A survey of the Rung the actor stands at. (host `survey`) |
| `disguise` | FOLDED | `conceal` | P | Grace |  | REASONED | inherits `conceal` |
| `suborn` | FOLDED | `bribe` | P | Attunement | Grace | REASONED | inherits `bribe` |

### TW — threadwork

| name | status | host | class | primary | secondary | basis | note |
|---|---|---|---|---|---|---|---|
| `trace` | FOLDED | `thread_read` | D | Spirit |  | CODE | inherits `thread_read` |
| `diagnose` | FOLDED | `thread_read` | D | Spirit | Attunement | REASONED | Finding kind: a displacement in a person's configuration (needs M9). [CONFIDENCE: low] (host `thread_read`) |
| `leap` | FOLDED | `thread_read` | D | Spirit |  | CODE | A stage of every operation; the Thread Sensitivity gate (`attempt_leap`) is its own carrier, not an attribute. (host `thread_read`) |
| `pull` | PARKED | `thread_read` | D | Spirit |  | CODE | `attempt_pulling` (`operations.py`); PARKED. (host `thread_read`) |
| `past-pulling` | FOLDED | `thread_read` | D | Spirit |  | CODE | `attempt_pulling` (`operations.py`); PARKED. (host `thread_read`) |
| `loosen` | FOLDED | `mend` | D | Spirit | Focus | REASONED | inherits `mend` |
| `heal` | FOLDED | `mend` | D | Spirit | Focus | REASONED | inherits `mend` |

### GV — settlements and governance

| name | status | host | class | primary | secondary | basis | note |
|---|---|---|---|---|---|---|---|
| `appoint` | FOLDED | `confer` | — |  |  |  | inherits `confer` |
| `designate` | FOLDED | `confer` | — |  |  |  | inherits `confer` |
| `elect` | FOLDED | `confer` | — |  |  |  | inherits `confer` |
| `rotate` | FOLDED | `confer` | — |  |  |  | inherits `confer` |
| `dismiss` | FOLDED | `revoke` | — |  |  |  | inherits `revoke` |
| `amend` | FOLDED | `establish` | — |  |  |  | inherits `establish` |
| `resign` | FOLDED | `release` | — |  |  |  | inherits `release` |
| `abdicate` | FOLDED | `release` | — |  |  |  | inherits `release` |
| `abandon` | FOLDED | `release` | — |  |  |  | inherits `release` |
| `warrant` | FOLDED | `issue` | — |  |  |  | inherits `issue` |
| `commission` | FOLDED | `issue` | — |  |  |  | inherits `issue` |
| `decree` | FOLDED | `proclaim` | — |  |  |  | inherits `proclaim` |
| `repeal` | FOLDED | `destroy_record` | — |  |  |  | inherits `destroy_record` |
| `charter` | PARKED | `proclaim` | — |  |  |  | PARKED; no quantity or reader exists. (host `proclaim`) |
| `relieve` | FOLDED | `transfer` | — |  |  |  | inherits `transfer` |
| `assess` | PARKED | `proclaim` | — |  |  |  | PARKED; no quantity or reader exists. (host `proclaim`) |
| `annex` | FOLDED | `seize` | — |  |  |  | inherits `seize` |
| `fortify` | FOLDED | `build` | — |  |  |  | inherits `build` |
| `improve` | FOLDED | `build` | — |  |  |  | inherits `build` |
| `patrol` | PARKED | `proclaim` | — |  |  |  | PARKED; no quantity or reader exists. (host `proclaim`) |
| `depose` | PARKED | `proclaim` | — |  |  |  | PARKED; no quantity or reader exists. (host `proclaim`) |
| `abolish` | PARKED | `proclaim` | — |  |  |  | PARKED; no quantity or reader exists. (host `proclaim`) |

### FA — faction actions

| name | status | host | class | primary | secondary | basis | note |
|---|---|---|---|---|---|---|---|
| `treaty` | FOLDED | `covenant` | P | Grace | Presence | REASONED | inherits `covenant` |
| `peace` | FOLDED | `covenant` | P | Grace | Presence | REASONED | inherits `covenant` |
| `alliance` | FOLDED | `covenant` | P | Grace | Presence | REASONED | inherits `covenant` |
| `truce` | FOLDED | `covenant` | P | Grace | Presence | REASONED | inherits `covenant` |
| `tribute` | FOLDED | `covenant` | P | Grace | Presence | REASONED | inherits `covenant` |
| `cession` | FOLDED | `covenant` | P | Grace | Presence | REASONED | inherits `covenant` |
| `vassalage` | FOLDED | `covenant` | P | Grace | Presence | REASONED | inherits `covenant` |
| `league` | FOLDED | `covenant` | P | Grace | Presence | REASONED | inherits `covenant` |
| `ransom` | FOLDED | `covenant` | P | Grace | Presence | REASONED | inherits `covenant` |
| `hostage` | PARKED | `covenant` | P | Grace | Presence | REASONED | inherits `covenant` |
| `marriage alliance` | PARKED | `covenant` | P | Grace | Presence | REASONED | inherits `covenant` |
| `war` | FOLDED | `declare` | — |  |  |  | inherits `declare` |
| `embargo` | PARKED | `declare` | — |  |  |  | inherits `declare` |
| `sanction` | PARKED | `declare` | — |  |  |  | inherits `declare` |
| `condemnation` | PARKED | `declare` | — |  |  |  | inherits `declare` |
| `hire` | FOLDED | `recruit` | D | Presence | Attunement | REASONED | inherits `recruit` |
| `enlist / retain` | FOLDED | `recruit` | D | Presence | Attunement | REASONED | inherits `recruit` |
| `turn` | PARKED | `recruit` | D | Presence | Grace | REASONED | A concealed `recruit` of a rival's obligee. PARKED. [CONFIDENCE: low] (host `recruit`) |
| `conscript / draft` | FOLDED | `recruit` | D | Presence | Attunement | REASONED | inherits `recruit` |
| `assign / post` | FOLDED | `assign` | — |  |  |  | inherits `assign` |
| `envoy` | FOLDED | `assign` | — |  |  |  | inherits `assign` |
| `garrison (post a man)` | FOLDED | `assign` | — |  |  |  | inherits `assign` |
| `conquer / take` | FOLDED | `seize` | — |  |  |  | inherits `seize` |
| `annex` | PARKED | `seize` | — |  |  |  | PARKED; fill an `annex` seat (unruled). (host `seize`) |
| `plot / scheme` | FOLDED | `conspire` | D | Presence | Attunement | REASONED | inherits `conspire` |
| `coup` | FOLDED | `conspire` | D | Presence | Attunement | REASONED | inherits `conspire` |
| `mediate` | PARKED | `persuade` | P | Attunement | Presence | REASONED | As SC `mediate`. PARKED (not FA). (host `persuade`) |

### EC — economy, trade and craft

| name | status | host | class | primary | secondary | basis | note |
|---|---|---|---|---|---|---|---|
| `cultivate` | FOLDED | `work` | P | Endurance | Strength | REASONED | inherits `work` |
| `mine` | FOLDED | `work` | P | Strength | Endurance | REASONED | Work at a seam under `deep_mining`. [CONFIDENCE: low] (host `work`) |
| `fish` | FOLDED | `work` | P | Endurance | Strength | REASONED | inherits `work` |
| `mint` | FOLDED | `craft` | P | Coordination | Focus | REASONED | inherits `craft` |
| `fortify` | FOLDED | `build` | — |  |  |  | inherits `build` |
| `improve` | FOLDED | `build` | — |  |  |  | inherits `build` |
| `pay` | FOLDED | `transfer` | — |  |  |  | inherits `transfer` |
| `repay` | FOLDED | `transfer` | — |  |  |  | inherits `transfer` |
| `haul` | FOLDED | `transfer` | — |  |  |  | inherits `transfer` |
| `relieve` | FOLDED | `transfer` | — |  |  |  | inherits `transfer` |
| `smuggle` | PARKED | `transfer` | — |  |  |  | inherits `transfer` |
| `trade` | FOLDED | `exchange` | — |  |  |  | inherits `exchange` |
| `buy` | FOLDED | `exchange` | — |  |  |  | inherits `exchange` |
| `sell` | FOLDED | `exchange` | — |  |  |  | inherits `exchange` |
| `barter` | FOLDED | `exchange` | — |  |  |  | inherits `exchange` |
| `bargain` | FOLDED | `exchange` | D | Presence | Attunement | REASONED | Price set by a contest's degree (SC); the host `exchange` reads a price, not a roll. (host `exchange`) |
| `tax` | FOLDED | `proclaim` | — |  |  |  | Tax content; GV owns it. (host `proclaim`) |
| `toll` | PARKED | `proclaim` | — |  |  |  | Tax content; GV owns it. (host `proclaim`) |
| `hoard` | PARKED | `transfer` | — |  |  |  | inherits `transfer` |

### WT — world, travel and survival

| name | status | host | class | primary | secondary | basis | note |
|---|---|---|---|---|---|---|---|
| `navigate` | FOLDED | `travel` | P | Reason | Perception | REASONED | Route choice and leader on the journey roll (M-WT-1, M-WT-3). [CONFIDENCE: low] (host `travel`) |
| `ride` | FOLDED | `travel` | P | Endurance | Perception | REASONED | inherits `travel` |
| `sail` | FOLDED | `travel` | P | Endurance | Perception | REASONED | inherits `travel` |
| `camp` | PARKED | `migrate` | — |  |  |  | inherits `migrate` |
| `encamp` | FOLDED | `migrate` | — |  |  |  | inherits `migrate` |
| `evacuate` | PARKED | `migrate` | — |  |  |  | inherits `migrate` |

### NP — NPC life and persons

| name | status | host | class | primary | secondary | basis | note |
|---|---|---|---|---|---|---|---|
| `heal` | FOLDED | `tend` | P | Reason | Attunement | REASONED | inherits `tend` |
| `recover` | FOLDED | `tend` | P | Endurance |  | REASONED | `tend` with `subject` = actor. [CONFIDENCE: low] (host `tend`) |
| `study` | FOLDED | `train` | — |  |  |  | inherits `train` |
| `teach` | FOLDED | `train` | — |  |  |  | inherits `train` |
| `court` | PARKED | `persuade` | P | Grace | Attunement | REASONED | Owner SC; waits on a consent contest. Etiquette and manners are the performance. PARKED. [CONFIDENCE: low] (host `persuade`) |
| `betroth` | PARKED | `give` | — |  |  |  | PARKED; content of a kin write. (host `give`) |
| `rear` | PARKED | `give` | — |  |  |  | PARKED; content of a kin write. (host `give`) |
| `swear` | FOLDED | `pledge` | — |  |  |  | inherits `pledge` |
| `designate` | FOLDED | `confer` | — |  |  |  | inherits `confer` |
| `cede` | FOLDED | `give` | — |  |  |  | inherits `give` |
| `confess` | FOLDED | `tell` | R | Presence | Grace | REASONED | inherits `tell` |
| `consecrate` | PARKED | `give` | P | Grace | Presence | REASONED | Investiture of a throne or seat: royal conduct (Jordan, 2026-11-05). PARKED (owner GV). [CONFIDENCE: low] (host `give`) |
| `crown` | FOLDED | `give` | P | Grace | Presence | REASONED | Investiture of a throne or seat: royal conduct (Jordan, 2026-11-05). PARKED (owner GV). [CONFIDENCE: low] (host `give`) |

## 2. What the lexicon changes in part 1

The 47 overrides are the only rows that add an attribute home; the rest repeat their host.

| attribute | primary of (overrides) | secondary of (overrides) |
|---|---|---|
| Strength | `mine` | · |
| Coordination | `shadow` | `intercept` |
| Endurance | `filibuster`, `recover` | `mine` |
| Reason | `counsel`, `define`, `navigate`, `object`, `refute` | `ambush`, `concede`, `pursue`, `rally`, `reconnoitre`, `retreat`, `scout`, `withstand` |
| Focus | · | · |
| Perception | `ambush`, `intercept`, `reconnoitre`, `scout` | `navigate`, `shadow` |
| Attunement | `flatter`, `mediate`, `negotiate`, `praise` | `bargain`, `court`, `diagnose`, `insult` |
| Presence | `bargain`, `confront`, `insult`, `pursue`, `rally`, `retreat`, `threaten`, `turn`, `withstand` | `consecrate`, `counsel`, `crown`, `define`, `filibuster`, `flatter`, `lie`, `mediate`, `negotiate`, `object`, `praise`, `refute` |
| Grace | `concede`, `consecrate`, `court`, `crown`, `lie` | `confront`, `turn` |
| Spirit | `diagnose`, `leap`, `past-pulling`, `pull` | `threaten` |

Against part 1's findings:

- **Finding 1 (Strength).** The lexicon gives Strength one primary, `mine` (class P, low confidence). The earlier reading stands: Strength is a combat attribute with an occasional labour home. Niche, accepted.
- **Finding 2 (Grace).** Grace gains `concede`, `lie`, `court`, `crown` and `consecrate` as primaries and `confront` and `turn` as secondaries, with `tell` and `speak` (and so `testify`, `plead` and the other tell and speech modes) already carrying it as a secondary from part 1. `crown` and `consecrate` are the royal-conduct rows (PARKED, owner GV). All are actor-side performances: no lexicon row puts Grace on the resisting side, so the one-key opposition limit (`_opposition_of`) stays, and the reader half of Jordan's description (being *seen as* respectable) is still not a verb.
- **Finding 3 (Presence).** Presence gains the most overrides (the SC tell and speech modes, mass battle's in-battle orders, `bargain`). Mass battle's `rally`, `pursue`, `retreat` and `withstand` all stand on the same `derive_command` pool as `march`, so MB remains a two-attribute lane.
- **Finding 5 (Spirit).** Not niche (part 1 findings 5 and 21). The lexicon adds only threadwork rows (`diagnose`, `leap`, `pull`, `past-pulling`) and `threaten` as a secondary; none of the defender-side or circumstance-modifier readings appears in a lexicon row.
- **Subsystem reading (part 1 §4).** GV, FA's treaty family, EC's trade family and NP's kin family add rows but no performance: nearly all are class —. The verb-pool demand stays in SC, FI, TW and PC; Perception's knowledge effect on the governing lanes is part 1 §5 finding 9.
- **New finding: SC's folded modes are where the Attunement and Grace homes differ from the host's.** `praise`, `flatter` (Attunement first) and `concede`, `lie` (Grace first) are modes of `tell` or `speak`, whose host key is Presence. Under CR-20's one attribute per vocation a mode cannot change the key, so these rows differ from their host only if `tell` and `speak` take a mode operand into `vocation_attribute` (a design question for CR-20, not decided here), or if the modes become verbs of their own.

## 3. Culled names, not mapped

- **PC:** `strike`, `rush`, `disengage`, `withdraw`, `disarm`, `kill`, `wound`
- **MB:** `command`, `invest`, `assault`, `fortify`
- **SC:** `argue`, `supplicate`
- **TW:** `sever`, `anchor`
- **FA:** `proclaim`, `suborn`, `claim`, `designate`
- **EC:** `appraise`
- **WT:** `endure`, `climb`, `swim`, `hunt`
- **NP:** `reconcile`, `avenge`, `wed`, `betray`, `bless`, `pray`, `mourn`
