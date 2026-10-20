# Verbs, v2 — part 03: Part III, Verbs (standards, roster, reconciliation)

## Status: PROPOSED (2026-10-17). Not ratified; merging ratifies nothing unless Jordan so rules. Static reading and static lookup only: no probe, run or trace was made. This Part **replaces** the first-pass Part III and Part V verdicts (the text as filed at `716c253`, which the lane sections cite as `v2-p3`, `v2-p4`, `v2-p8`; recover it with `git show 716c253:proposals/2026-10-16-v2-person-troop-attribute-synthesis_part3.md`).
## Parts, in reading order: [head](2026-10-16-verbs-01-thesis-and-persons.md) (§0, Part I Persons) · [`verbs-02`](2026-10-16-verbs-02-attributes.md) (Part II Attributes) · **this file** and [`verbs-04`](2026-10-16-verbs-04-critics-etymology-gaps-and-decisions.md) (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`verbs-05`](2026-10-16-verbs-05-what-verbs-do-to-the-world-1.md) and [`verbs-06`](2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md) (Part IV What verbs do to the world) · [`verbs-07`](2026-10-16-verbs-07-roadmap-reliability-and-sources.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`verbs-08`](2026-10-16-verbs-08-engine-findings-from-the-first-trial.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: [`verbs-09`](2026-10-16-verbs-09-lexicon-personal-combat.md) PC · [`verbs-10`](2026-10-16-verbs-10-lexicon-mass-battle.md) MB · [`verbs-11`](2026-10-16-verbs-11-lexicon-social-contest.md) SC · [`verbs-12`](2026-10-16-verbs-12-lexicon-fieldwork-and-inquiry.md) FI · [`verbs-13`](2026-10-16-verbs-13-lexicon-threadwork.md) TW · [`verbs-14`](2026-10-16-verbs-14-lexicon-settlements-and-governance.md) GV · [`verbs-15`](2026-10-16-verbs-15-lexicon-faction-actions.md) FA · [`verbs-16`](2026-10-16-verbs-16-lexicon-economy-trade-and-craft.md) EC · [`verbs-17`](2026-10-16-verbs-17-lexicon-world-travel-and-survival.md) WT · [`verbs-18`](2026-10-16-verbs-18-lexicon-npc-life-and-persons.md) NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`verbs-19`](2026-10-16-verbs-19-gap-register-pc-and-np.md) PC+NP · [`verbs-20`](2026-10-16-verbs-20-gap-register-mb-and-fa.md) MB+FA · [`verbs-21`](2026-10-16-verbs-21-gap-register-sc-and-gv.md) SC+GV · [`verbs-22`](2026-10-16-verbs-22-gap-register-fi-and-tw.md) FI+TW · [`verbs-23`](2026-10-16-verbs-23-gap-register-ec-and-wt.md) EC+WT.

---

## PART III. VERBS

### III.0 What this Part replaces, and why

The first-pass Part III triaged 179 proposed verbs, distilled the 66 live ones to 37 by a "pessimistic" NERS pass in which each verb *"has to argue its case for inclusion"*, and Part V's trial restored 13 for a post-trial set of 50. Jordan's directions for this rewrite (this session) change the method, so the counts, the dispositions and the thesis that followed from them are withdrawn:

1. **The work is a linguistics exercise beneath a design exercise.** The design exercise transforms precedent, research and identified gaps into the verbs each subsystem needs. The linguistic exercise gives every verb an English name with an **academic etymology traced into Latin** (and to Proto-Indo-European where attested).
2. **Each subsystem requires certain verbs, by NERS, and must address every gap or shortcoming about verbs identified in the repository's precedent, research and gap documents at the start of this PR.** The evidence base is Part VII (488 gap rows over the ten subsystems, each traced to its source and precedent documents). Part VI answers every row.
3. **Order of work:** group the verbs by subsystem, then by **suite of related concepts** (a host verb with its related-but-distinct acts folded in, as `covenant` hosts treaty, alliance, truce and cession terms); assess each suite by NERS and against precedent games and systems; **then** deduplicate and cull.
4. **This is a game, and its conventions bind.** What a player of this kind of game expects is necessary by NERS's own definition: removing it worsens the experience. Settlement management lets you build and affect the economy; factions recruit, set assignments and hold territory. These are the **convention floor**. A floor verb is kept; only the depth to which it is built is open. v2's habit of cutting a verb because it failed to "argue its case" is withdrawn for the floor. Beyond the floor a verb earns its place by NERS and by precedent.
5. **No workarounds.** A convention verb is its own verb, named in the actor's voice, owned by the subsystem that resolves it, writing its own world effect. Jordan called "recruit = `tell` plus the recruit's `oblige`" *an insane workaround*. A fold into a host is legitimate only for a **true equivalent**: the same actor, the same subsystem mechanic, differing in a parameter or content: never by composing other verbs, other actors' replies or several steps.
6. **All verbs occur within a subsystem, and so have mechanics that affect the game world.** A verb with no subsystem mechanic and no named world effect (the Record, edge, store, condition, Tenure or Event it writes) is not a verb. It is an outcome, a parameter, or a choice inside another verb. Where the effect does not yet exist in the engine, that is a **named gap against the subsystem** (§III.10), not a reason to hide the verb inside another.

What survives from the first pass: the engine findings of Part V §V.2 (carried in `verbs-08`), the instruments of Part IV (the chooser, the world-state model, the assessment framework), and the evidence that the *readers* are the shortage. What does not: the 37, the 50, the "distil the vocabulary" corollary, the trial's tables and the IV §3.4 lever as written (a verb's context nodes read from its root sense).

### III.1 The standards

| id | standard | where it comes from |
|---|---|---|
| **S-1** | **Subsystem and world effect.** Every roster verb belongs to exactly one subsystem and names what it writes (Record, edge, store, condition, Tenure, Event). Acts a subsystem's resolver already chooses inside one verb's resolution (a parry, a rally) are *scene moves* or *choices*, not verbs. | Jordan, this session (direction 6); first-pass triage III.1 |
| **S-2** | **Convention floor.** The acts a player of the genre expects are kept, each tied to at least one precedent: an in-tree precedent document (path and section) or a named game or system for a stated mechanic. A game named from memory is tagged `[MEMORY]`. | direction 4 |
| **S-3** | **NERS, then cull.** Each suite is assessed by the four criteria (`CLAUDE.md` §0.06; method `skills/ners/SKILL.md`): N from all six directions with a false-N-line check, E last as a ratio against what N and R found. Only then are duplicates culled. | direction 3 |
| **S-4** | **The fold test.** A fold passes only if all three hold: same actor, same mechanic, differing in a parameter or content. | direction 5 |
| **S-5** | **Etymology is the linguistic record; fit is a usage finding.** A chain runs English ← Middle English ← French or other intermediate ← Latin lemma with principal parts and the attested sense (Lewis & Short) ← PIE root where attested. A Germanic, Frankish or unknown-origin word says so; a Latin cognate through PIE is labelled *cognate, not ancestor*. Fit (FITS / STRAINED / MISFIT) is judged by ordinary current usage (`CLAUDE.md` §4, ED-IN-0179: a reader with no memory of this repository must land on the row's meaning). **No merge, gap or context node rests on a root sense alone.** | direction 1; critic L-01 |
| **S-6** | **Names.** The actor's voice (*the recruiter recruits*); a plain word where one covers (*coin nothing a plain word already covers*); no repurposed software term; no name that is also a stat or a store in this repository (*Command*, *Discipline*, *yield*). | `CLAUDE.md` §4; critics L-02, L-13, L-17, V-10, V-20 |
| **S-7** | **Evidence.** Every `file:line` was opened; absence claims name the check that would show presence; every KEEP and CULL names its falsifier. A claim from memory is tagged `[UNVERIFIED]`, an assumption `[ASSUMPTION: … — basis]`. | `CLAUDE.md` §0.1 |
| **S-8** | **`needs_jordan` is not a parking space.** An item reaches Jordan only after the five answer-it-first tests (superseded · irrelevant · design document · precedent · architecture) fail and two defensible options lead to materially different games or an answer would overwrite ratified canon. | `CLAUDE.md` §0 |

### III.2 How the evidence was built

1. **Gap register (Part VII).** Five reader lanes extracted, for the ten subsystems, every verb-related gap, shortfall, name defect, collision and deferral from the lane files (`research/by_lane/`), the precedent corpus they index, the verb-coverage pass (`proposals/2026-10-03-verb-coverage-and-gap-fill.md`), the hole register (`engine/season/hole_register.yaml`), the plan, v2's own first pass and the troop-stock design: **488 rows** (PC 40, NP 41, MB 57, FA 50, SC 59, GV 45, FI 58, TW 42, EC 53, WT 43), each with its source, kind, the verbs the source names, its precedent documents and v2's first-pass disposition.
2. **Two adversarial critics (Opus)** attacked the incumbent lexicon (19 findings, L-01 to L-19) and v2's own verb claims (21 findings, V-01 to V-21). Their findings and every lane's answer are in `verbs-04` §III.7.
3. **Ten subsystem lanes (Opus)** each built a section (Part VI): the subsystem's mechanic, the convention floor, the suites with NERS and precedent, the lexicon with etymology chains and fit, the deduplication and culls, a coverage table that disposes of **every** gap row of the subsystem, the mechanics it waits on, cross-subsystem flags, and the few items for Jordan.
4. **Reconciliation (this file, §III.5).** Where lanes collide, one ruling per collision, with the lane text it overrides.
5. **Etymology audit.** The lexicon chains were audited by two independent Opus auditors against Wiktionary and Lewis & Short (Perseus), with corrections applied (`verbs-04` §III.8).

Verification of the coverage tables was mechanical: every one of the 488 gap ids appears in its lane's coverage table exactly once (a script check, not a probe).

### III.3 The roster: 92 verbs in ten subsystems

**The count.** 92 verbs: **48** descend from the 46 shipped rows (44 keep their row; `tie / knot` and `evade / defy` each split into two), **11** are planned positions, **33** are new. The first pass ended at 37 and, after its trial, 50. The difference is the convention floor (§III.0 pt 4): the first pass cut the acts a game of this kind needs because they had to "argue their case", and composed others out of unrelated verbs. This is a proposal. Merging it builds nothing: most rows wait on named mechanics (§III.10), and several names wait on a ruling (§III.11).

**How to read the tables.** *Status*: SHIPPED (a row in `engine/season/verb_table.yaml` today; "rebuilt" means the row stands but its name, actor or effect changes), PLANNED (a workplan position, not yet a row), NEW (this Part proposes it). The third column is the lane's own statement of the world effect, shortened; mechanic ids such as `PC-M5` are numbered per lane and listed in each Part VI section. Etymology chains, fit verdicts, folds, culls and the coverage tables are in the Part VI section for the subsystem. **Where a lane table and this roster disagree, the roster governs** (§III.5 lists every override).

#### PC — personal combat — 7 verbs

| verb | status | the world effect it writes (the lane's words, shortened) |
|---|---|---|
| `fight` | SHIPPED, rebuilt | body contest via `personal_combat`; Felled → `Person.body`, `Person.exists`, `Tenure.until`, `person.died`; Wounded → `Person.body`, `body.changed`; Untouched → `contest.undecided` (`VT:556-581`); rebuilt to write both parties (PC-M1) |
| `challenge` | SHIPPED, rebuilt | today writes nothing, emits `challenge.issued` (`VT:609-611`); rebuilt: mints a `challenge` Record (terms, stakes, `for`), lapses witnessed |
| `accept` | SHIPPED, rebuilt | named fold of `fight` (own key on `_eff_kill`); rebuilt: requires a held challenge naming the actor, fights under its terms, emits a duel kind |
| `assassinate` | NEW (key of fight) | `fight`'s scene with aim *death* (yields refused), a held cover, first move, actor withheld from witnesses by the cover's degree (PC-M6) |
| `capture` | NEW (key of fight) | `fight`'s scene with aim *alive*: a Felled or yielded subject is taken into custody (PC-M5), `person.captured` `[ASSUMPTION: kind name]` |
| `guard` | NEW | protective edge guard → ward (`Tenure` kind `guard`, PC §3.9), `guard.taken`; read by the N-party scene (PC-M7) |
| `rescue` | NEW | closes a live `detain` by force and relocates the prisoner; `prisoner.freed` |

#### MB — mass battle (the force and the field) — 9 verbs

| verb | status | the world effect it writes (the lane's words, shortened) |
|---|---|---|
| `march` | SHIPPED, rebuilt | VT:683-711; adds posture, carries the force (MB-M1), reads the order, writes stocks and garrison |
| `levy` | NEW | settlement act, `remit:dispatch`; `Rung.stores` `recruits`→`troops_raw`, plus the cohort's `stance` toward the seat's faction; `levy.raised` |
| `muster` | NEW | settlement act; troop kinds `from` → `subject` via `_shift`; `army.mustered`, witnessed |
| `drill` | NEW | settlement act; `troops_<g>`→`troops_<g+1>`; `troops.drilled` |
| `disband` | NEW | settlement act; `troops_<g>`→`recruits`, capped; `army.disbanded` |
| `marshal` | NEW | settlement act; writes the `order_of_battle` Record read by `order_of_battle()` at every field; `army.marshalled` |
| `supply` | NEW | stores from a settlement in purview into the force's stores (MB-M1); `force.supplied` |
| `forage` | NEW | stores from the occupied rung into the force's stores; `stores.foraged` |
| `surrender` | NEW | the hold passes (`seize`'s Tenure pair); stocks stand down; `sack` barred; `place.surrendered` |

#### SC — social contest — 11 verbs

| verb | status | the world effect it writes (the lane's words, shortened) |
|---|---|---|
| `tell` | SHIPPED | contested on "a standing" vs `to`; told claim deposited at WITNESS with the teller chained; `news.told`, `confidence.broken` |
| `persuade` | PLANNED, renamed from argue | contested; writes the hearer's `Person.pursuits` (`pursuit.moved`); `manner` reason/appeal |
| `utter` | SHIPPED | as `declare` |
| `commit` | SHIPPED | opens a `commit` Tenure on a Proposition |
| `petition` | SHIPPED | mints a `petition` Record held by the petitioner, `to` a Person, `from` a Rung |
| `lodge` | SHIPPED, renamed from carry | re-winds a held petition's stages; appends a docket item naming it (EI:300-) |
| `convene` | SHIPPED | writes `Date.due_at` and the convening condition (VT:194) |
| `open_case` | SHIPPED | by `remit:determine`: a case file and a docket item (EI:228-296) |
| `speak` | SHIPPED, rebuilt | today writes nothing; planned: contested on "a matter" at a docketed sitting, moving its `issue` rung |
| `determine` | SHIPPED, rebuilt | opens the docketed row's disposal Tenure on a Person by bench and quorum (VT:222-267) |
| `interrogate` | PLANNED | questioning under custody; `confession.made` |

#### FI — fieldwork and inquiry — 12 verbs

| verb | status | the world effect it writes (the lane's words, shortened) |
|---|---|---|
| `examine` | SHIPPED, rebuilt | presence at the Rung; reads the log there; `seen` claims in the actor's ledger (FI-M1) |
| `research` | SHIPPED, rebuilt | consult deposit (`content:<kind>`); forgery read against `forgery_quality` |
| `watch` | SHIPPED, renamed from surveil | presence at the Rung over the season; pierces covers (true `who` against the FI-M4 grade) |
| `interview` | SHIPPED, rebuilt | `told` claims from the questioned person (FI-M5); the question deposited with him; `counterparty` clause |
| `reconstruct` | SHIPPED, rebuilt | a deed claim (`who`) from the own-ledger candidate set; FI-M3 on Failure |
| `survey` | SHIPPED, rebuilt | `_mint_document` → `faction_sheet` (or `rung_sheet`, FI-M7) in the surveyor's hold; content deposit |
| `conceal` | PLANNED | `cover` Record (`terms` = actor, FI-M4 grade, scope); `anchor_of` |
| `infiltrate` | NEW | `oblige`'s duty edge, taken under a live cover |
| `forge` | SHIPPED, rebuilt | `_mint_document` false sheet; writes `forgery_quality` (FI-M4); emits `faction.surveyed` |
| `bribe` | NEW | `transfer`'s write + an inducement deposit to the circle of two; FI-M8 reader |
| `create_record` | SHIPPED | `Record.exists` true (CRUD-named; no retrofit, FI-L-15) |
| `destroy_record` | SHIPPED | `Record.exists` false |

#### TW — threadwork — 7 verbs

| verb | status | the world effect it writes (the lane's words, shortened) |
|---|---|---|
| `thread_read` | SHIPPED, rebuilt | Thread-Read pool via the Leap stage; Claim to own ledger (WITNESS); knot; `(Person, coherence)` at Relational+ |
| `weave` | NEW | `attempt_weaving`; `(Person, coherence)`; held-load Tenure `weave` (TW-M6); knot; strain for IN-35 |
| `lock` | NEW | `attempt_locking` (scale + FR); `(Person, coherence)`; Tenure `lock` read by the write gate (TW-M6); knot; MS −1 |
| `dissolve` | NEW (the name sever was proposed) | `attempt_dissolution` (scale + FR); `(Person, coherence)`; target ended (`Site.condition` to floor; a held shape's Tenure closed); residue (TW-M10); knot |
| `mend` | NEW | `attempt_mending`; target by kind (lock, weave, lattice Site via `_rise`, a person's resting point, body); mender's elastic return or resting point; knot; 0 Coherence |
| `ward` | NEW (build-gated) | Tenure `ward` with a season `Term`; routes hostile operations to `opposing.py` (TW-M8); knot |
| `knot` | SHIPPED, split from tie / knot | `knots.py::form_knot`; directed Tenure `knot`; strain (TW-M3) |

#### GV — settlements and governance — 20 verbs

| verb | status | the world effect it writes (the lane's words, shortened) |
|---|---|---|
| `confer` | SHIPPED | opens a seat `hold` under the office's `conferral` basis (`Tenure.since`/`term`); `tenure.opened` |
| `revoke` | SHIPPED | closes another's seat `hold` under `revocation_bases` (`Tenure.until`); `tenure.closed` |
| `establish` | SHIPPED | founds an Office (`Office.exists`, `remit_acts`); `office.established` |
| `succeed` | SHIPPED, rebuilt | the heir opens the vacant throne's `hold` through `inheritance` |
| `release` | SHIPPED | the holder closes his own edge (`Tenure.until`); `tenure.closed` |
| `issue` | SHIPPED | mints a dispensation Record to one executor (`Record.exists`); `dispensation.issued` |
| `order` | SHIPPED as dispatch (documentless order) | a documentless order to a named person; `order.given`; needs M-ORDER |
| `comply` | SHIPPED | emits `compliance.given`; writes nothing; the performance is the executor's own act |
| `evade` | NEW, split from evade / defy | covert non-performance; `compliance.evaded`, deposited on detection; cuts a tax take at MATTER |
| `defy` | NEW, split from evade / defy | open refusal; `compliance.refused` to the issuing seat; withholds a tax take for the season |
| `construe` | SHIPPED, moved from SC | the receiver's reading of a writ; writes nothing |
| `proclaim` | NEW | mints an `edict` Record (`kind: notice`) published to the residents of `at`; `edict.proclaimed` |
| `tax` | NEW | mints an `edict` (`kind: tax`, `amount`); MATTER diverts yield to the seat's treasury each season (`Rung.stores` ×2); `tax.levied`, `tax.collected`, `tax.withheld` |
| `requisition` | SHIPPED | moves a rung's stock into the seat's treasury now (`Rung.stores` ×2); `requisition.taken` |
| `ration` | NEW | mints an `edict` (`kind: ration`); MATTER's draw per mouth at `at` is cut; `ration.set` |
| `arrest` | PLANNED | opens `detain` (prisoner → warrant seat), contested; `arrest.made` / `arrest.resisted` |
| `pardon` | PLANNED | closes another's `detain`/`ban` under the determination basis (`GT:1112-1119`); `detention.ended` / `ban.ended` |
| `found` | SHIPPED | mints a Rung under its works' `at` plus the founder's `hold`; `rung.founded` |
| `build` | SHIPPED, rebuilt | mints a Site at condition 0, paying `works_cost`; `site.built` |
| `raze` | PLANNED | ends a Rung or Site; licensed by occupation; must re-house persons |

#### FA — faction actions — 7 verbs

| verb | status | the world effect it writes (the lane's words, shortened) |
|---|---|---|
| `covenant` | PLANNED | a seat's offer or seal of terms. Writes `Proposition.exists`, `Record.exists` (dispensation) and the party's own edge; in force while both parties' edges are live |
| `declare` | NEW | a seat's public stance toward another faction. Writes `Proposition.exists` (mood WAR first) and the declarer's own edge; `binding_decision`, so public |
| `recruit` | NEW | the recruiter's contested offer of service. On Won writes the recruit's `oblige` (+ term) to the exercised seat |
| `conspire` | NEW | draw a person into a plot against a seat; mints the plot Proposition and opens edges to it on Won |
| `assign` | NEW (the posting act; was the rebuilt dispatch) | post a named obligee to a place with a task. Writes `Tenure.payload` on his `oblige` and, for a posting elsewhere, his `contain` (via `_relocate`) |
| `seize` | SHIPPED | take a Record under warrant or a Rung under occupation; one hold closed, one opened |
| `sabotage` | PLANNED | lower a Site's condition |

#### EC — economy, trade and craft — 8 verbs

| verb | status | the world effect it writes (the lane's words, shortened) |
|---|---|---|
| `work` | SHIPPED, rebuilt | labour staged on a Site, read by MATTER's yield (`Site` labour tally → `Rung.yield` → `Rung.stores`); EC-M1 |
| `craft` | NEW | conversion at a workshop: `Rung.stores` inputs down, product up; `goods.made`; EC-M2 |
| `restore` | SHIPPED, rebuilt | raises a worn Site no works names (`Site.condition`, `_rise` to full scale) |
| `transfer` | SHIPPED | `Rung.stores` ×2; through a seat, `Tenure.term` |
| `exchange` | SHIPPED, rebuilt | swap of two rungs' stores at the price (`Rung.stores` ×4); EC-M10 |
| `hire` | NEW | the hireling's service edge (`Tenure.since`, `Tenure.term`) + the first wage (`Rung.stores` ×2); EC-M11 |
| `borrow` | NEW | advance (`Rung.stores` ×2) + a `debt` Record (`Record.exists`); EC-M9 |
| `lend` | NEW | as `borrow`, the creditor acting |

#### WT — world, travel and survival — 3 verbs

| verb | status | the world effect it writes (the lane's words, shortened) |
|---|---|---|
| `travel` | SHIPPED, renamed from move | `_relocate`: closes and opens a `contain` Tenure, appends to `Person.travel_leg`, emits `travel.moved`/`.blocked`/`.ended` (VT:753-755; `matter.py:577`). Leg priced in `budget.py:60`; by route once M-WT-1 exists |
| `migrate` | SHIPPED | `_relocate` plus `reside` re-homed, throttled by `WQ.capacity`. Emits `residence.changed`; refusals `travel.blocked`/`migrate.refused` (VT:733-739) |
| `explore` | NEW | presence in a territory → XSC §6.4 Discovery → reveals an authored POI (Site/Record) to the explorer; emits `site.discovered` (needs M-WT-5) |

#### NP — NPC life and persons — 8 verbs

| verb | status | the world effect it writes (the lane's words, shortened) |
|---|---|---|
| `tend` | PLANNED | raises `Person.body`; `body.tended` |
| `train` | PLANNED | writes `Person.capability`; `capability.raised` |
| `forgive` | PLANNED | removes the actor's negative `Person.stance` rows toward `subject`; `stance.moved` |
| `tie` | SHIPPED, split from tie / knot | opens a directed `tie` Tenure; `bond.formed` (declined until NP-M7 and NP-M8) |
| `marry` | NEW | opens two directed `kin` Tenures (content `spouse`); `marriage.made` (needs NP-M9) |
| `pledge` | SHIPPED, renamed from oblige | opens the joiner's `oblige`-kind Tenure to a seat (`Tenure.since`, `Tenure.term`); `duty.taken` (`VT:772-774`) |
| `defect` | NEW | closes the actor's `commit`/`oblige` to A and opens one to B in one write; `allegiance.changed` |
| `give` | SHIPPED, rebuilt | closes the giver's `hold` and opens the receiver's; `record.given` (`VT:433-437`) |

### III.4 Suites and the names folded into each host

A **suite** is a host verb with the related-but-distinct acts folded into it. Each fold passed the three-part test of S-4 in its lane; the lane section gives the test per name. *Content* means a parameter or content kind of the host's one effect; *posture* and *choice* mean a state or decision inside the host's own resolver; *key* means a named key of a host's single effect (as `accept` is of `fight`). Names after "parked" are held on a trigger the lane names; names after "culled" died because nothing a floor act needs dies with them.

| sub | host | folded into it | parked | culled or not a verb |
|---|---|---|---|---|
| PC | `fight` | keys `accept`, `assassinate`, `capture`; contents `ambush`, `shoot` | — | scene moves under IN-46, not verbs: `feint`, `lunge`, `parry`, `dodge`, `grapple`, `flee`, `yield`, `interpose`; culled names `strike`, `rush`, `disengage`, `withdraw`; outcomes `kill`, `wound`, `disarm` |
| PC | `challenge` | content `champion` (a `for` naming the principal) | — | — |
| MB | `march` | postures `besiege`, `storm` (default); in-battle choices `rally`, `pursue`, `retreat`, `withstand` | `reconnoitre`, the MB half of `ambush` | names `invest` (reads as money), `assault` (PC's ground); `command` (a stat, not a verb); `fortify` moves to GV `build` |
| MB | `levy` | conscript and recruit-for-coin as a terms parameter (R-01) | — | — |
| MB | `muster` · `supply` · `forage` | `garrison` · `provision`, `equip` · `sack` | — | — |
| SC | `tell` | `testify`, `confess`, `confide`, `warn`, `confront`, `praise`, `flatter`, `insult`, `counsel` | `lie` (J-C-6) | — |
| SC | `utter` | `propose`, `allege`, `threaten` (moods of one Proposition mint) | — | rename open (R-06) |
| SC | `speak` | `plead`, `refute`, `concede`, `object`, `define` | `negotiate`, `mediate` | — |
| SC | `commit` · `petition` · `convene` · `determine` | `vote`, `swear` · `accuse` · `adjourn` · `arbitrate` | `filibuster` | `supplicate` |
| SC | `persuade` | the planned `argue`, renamed | `preach` (audience operand) | — |
| FI | `examine` · `research` · `watch` · `survey` · `conceal` · `bribe` | `search`, `track` · — · — · `audit`, `census`, `scout` · `disguise` · — | `decipher`, `eavesdrop`, `shadow`, `intercept`, `suborn` | — |
| TW | `thread_read` | `trace`, `diagnose` | — | `leap` is a stage of every operation |
| TW | `weave` · `lock` · `dissolve` · `mend` | — · — · — · `heal` | `pull` (with past-pulling) | `sever` as a name, `anchor`; `loosen` goes to `release` (own shape) or `mend` (another's) |
| GV | `confer` | `appoint`, `designate`, `elect`, `steward`, `rotate` | — | — |
| GV | `revoke` · `establish` · `release` · `issue` | `dismiss` · `amend` · `resign`, `abdicate`, `abandon` (and SC's `deny`, `withdraw`) · `warrant`, `commission` | `depose`, `abolish` | — |
| GV | `proclaim` · `build` · `seize` (owner FA) · `transfer` (owner EC) | `decree` · `fortify`, `improve` · `annex` · `relieve` | `charter`, `assess`, `patrol` | `repeal` is `destroy_record` |
| FA | `covenant` | treaty, peace, alliance, truce, tribute, vassalage, league, ransom terms, cession terms | `hostage`, marriage alliance | — |
| FA | `declare` | war (built first) | `embargo`, `condemnation`, `sanction` (use `embargo`) | `proclaim` leaves FA for GV |
| FA | `recruit` · `assign` · `conspire` | `enlist`, `retain` · post, envoy, garrison a man · plot, scheme, coup | `turn` (with `conceal`) | `suborn`, `claim`, `designate` |
| EC | `work` · `craft` · `transfer` · `exchange` | `cultivate`, `mine`, `fish`, `hunt` · `mint` · `pay`, `repay`, `haul`, `relieve`, `tribute` · `trade`, `buy`, `sell`, `barter`, `bargain` | `smuggle`, `toll`, `hoard` | `appraise` |
| WT | `travel` · `migrate` | `navigate`, `ride`, `sail` · — | `camp` (with `encamp`), `evacuate` | `endure`, `climb`, `swim` (scene scale) |
| NP | `tend` · `train` | `heal`, `recover` · `study`, `teach` | — | — |
| NP | `marry` · `pledge` · `give` | `wed` · `swear` · `cede` | `court`, `betroth`, `rear`, `consecrate` (with `crown`) | `reconcile`, `avenge`, `betray` (a judgement across acts, not a verb), `bless`, `pray`, `mourn` |

### III.5 The reconciliation ledger

Ten lanes worked in parallel and collided in places. Each ruling below is one collision, the lane text it overrides and the reason. The rulings follow the standards of §III.1; none is Jordan's unless §III.11 lists it. A ruling is *contestable* where a lane argued the other way; the lane's argument is in its Part VI section.

| id | collision | ruling | overrides | reason |
|---|---|---|---|---|
| **R-01** | `recruit`, `levy`, `hire` claimed across MB, FA, EC and NP | **`levy`** (MB, actor a seat): raise men from a settlement's recruit pool into a troop stock; compulsory or paid is a *terms* parameter. **`recruit`** (FA): a seat enlists a named person into its faction or office; writes the membership edge. **`hire`** (EC): the employer opens a paid-service edge, for a person or a company; NP and FA use it. | MB's separate troops-for-coin `recruit` (folds into `levy`); FA's fold of `hire` into `recruit`; NP's own `hire` row | MB's own analysis (MB §3.9, item 2: default no term, no upkeep) makes `levy` and a paid recruit differ only in cost: same actor, same mechanic, parameter (S-4). The troop-stock design rejected a separate troops `recruit` verb. A hired man is not a member of a faction: different edge, different write. Contestable: MB wanted two armies (temporary and permanent) |
| **R-02** | `tie / knot` split: NP said `knot` goes to FI, TW kept it | `knot` is TW's; `tie` is NP's | NP §3.3 suite D, FI | TW takes the verb (the deliberate thread bond; `knots.py` is only the module's home); FI-G55 points at TW |
| **R-03** | `build`, `found`, `raze`, `fortify` claimed by EC and GV (`raze` also MB) | **GV** owns `found`, `build`, `raze`: the seat decides to found, build or raze. `fortify` is a content of `build` (new works) or `restore` (EC; upkeep of a garrison Site's condition). EC keeps `work`, `craft`, `restore`, `transfer`, `exchange`, `hire`, `borrow`, `lend` | EC S3; MB's `raze` | One row per act. The settlement-management suite is a governing act that spends EC's stores. V-21 resolves by content: new fortification is `build`, repair is `restore` |
| **R-04** | `tax`: GV an own row, EC a content of `requisition` | **`tax`** is its own GV row (a standing levy a MATTER reads each season); **`requisition`** stays the shipped one-off act | EC's recommendation | Different mechanic (a standing edict read each season versus an act), so not a fold (S-4). The detail is in the GV section |
| **R-05** | `dispatch`: GV renames the shipped documentless order `order`; FA rebuilds `dispatch` as the posting act | The shipped act (an order to a named person, no document) is `order`; the posting act (a person sent to a place with a task) is **`assign`**. **Until Jordan rules, the shipped name `dispatch` stands** (ED-IN-0210 kept it; the rename was withdrawn under K-24), and `remit:dispatch` is untouched | FA's rebuild under the old name; GV's immediate rename | Two acts, two writes. A ratified ruling is not overwritten by a lane (S-8). Decision D-V7 |
| **R-06** | `declare`: SC renames `utter` to `declare` and folds war into it; FA adds `declare` as a seat's public stance | **`declare`** is FA's new row: a seat's public stance toward another faction, war first. SC's rename is withdrawn. SC's host keeps `utter` for now; the candidate rename is `propound` ← L *prōpōnere* 'set forth' (Wiktionary: to put forward; to offer for discussion) [rename open] | SC's rename; SC's fold of `declare (war)` | FA's argument stands on the fold test: actor class (a seat, `remit:dispatch`) and stratum (`binding_decision`, public) differ from a person's `utter` (`social`). A private `utter` of mood WAR must not make a war |
| **R-07** | `interrogate`: SC sent it to FI, FI sent it to SC | **SC** owns `interrogate` (questioning under custody, planned with `arrest` and `pardon` in B-R; the `interrogation` arrangement is SC's); **FI** owns `interview` (no custody). FI's open item is how the questioned person answers (§III.11) | both | The plan pairs it with the custody verbs; its write is a proof, not a finding |
| **R-08** | `forage`, `camp`, `encamp`, `sack` across MB, WT, EC | **`forage`** is MB's (a force draws wild food at its location for its stock); `sack` is a content of it. WT supplies the land's yield (M-WT-8). **`camp`** is WT's, parked, hosting `encamp` (company size as a parameter). The Contribution System is `requisition` under an occupation basis | WT's own `forage` row; v2's `encamp` as a `march` posture | The actor and eater are MB's. A halt moves nobody, so it is not a march (WT) |
| **R-09** | `explore` (WT new) vs FI's `scout`→`survey` | **`explore`** is WT's: it reveals terrain and points of interest to the actor's ledger. `survey` is a faction or Rung sheet | — | Different write (map knowledge versus a sheet) |
| **R-10** | Renames: `oblige`→`pledge` (NP), `carry`→`lodge` (SC), `surveil`→`watch` (FI), `move`→`travel` (WT), `sever`→`dissolve` (TW), `utter` (open) | All adopted as proposals except `utter`. Each touches act ids that hash the verb name, so they land as **one rename batch** with declared hash moves and an openly stated golden re-record (`CLAUDE.md` §7) | — | `oblige` runs against ordinary English (critic L-02); `petition.carried` reads as adopted (L-04); `survey`/`surveil` are one letter apart (L-09); `dissolve` is the plain word for Dissolution (V-08) |
| **R-11** | `succeed` claimed by NP, FA and GV | **GV** owns the row (the heir's own claim, IN-61; `inheritance` basis); FA and NP consume it | — | The first pass's cut misread RS-27. The gate is GV's |
| **R-12** | `construe`: SC sent it to GV; GV listed none | **GV**: the receiver's third answer to a writ beside `comply` and `evade`/`defy` | — | SC's argument stands; GV's roster is amended here |
| **R-13** | `thread_read` listed by FI and TW | **TW** owns it; FI supplies the finding shape | FI S6 | The mechanic is threadwork's gate and cost |
| **R-14** | `forge`, `create_record`, `destroy_record` listed by SC and FI | **FI** owns them; SC's proofs reader reads `forgery_quality` through the same rule (one owner) | — | One reader rule, not two |
| **R-15** | `capture` (PC) and `arrest` (GV) | Two keys on one custody-opening mechanic: `arrest` the warrant-bearing key (GV), `capture` the warrant-less key (PC). GV owns the `detain` opener | — | PC's recommendation; the precedent is `fight`/`accept` |
| **R-16** | `release` (critic L-08: a release of an obligation is granted by the party owed; `renounce` for one's own vow) | `release` stays; `renounce` is **not** adopted now. L-08 is recorded open at medium confidence; it reopens if the vow half of `release` splits when `defect` and the betrayal reader land | NP, FA, GV proposals | TW's objection stands: `release` also lets go a held shape or a knot, and `renounce` reads worse there |
| **R-17** | `ransom` and the custodian's discharge | Ransom is a `covenant` content; the payment is a `transfer`; the discharge is `pardon`'s mechanic. **The name `pardon` is a defect** (a pardon is remission by authority, not release for payment; V-16): candidate plain word `free` [name open] | FA, GV, EC | One mechanism, one open name |
| **R-18** | `drill` (MB, a stock) and `train` (NP, a person) | Two rows kept apart by object: `train` writes `Person.capability`; `drill` raises a stock's grade. Recorded as a near-synonym pair of the `give`/`transfer` kind (L-10) | — | Writes differ, so not a fold |
| **R-19** | `surrender` (MB), `yield` (PC), `cede` (NP), treaty terms (FA) | `surrender` is MB's row (a force gives up a place); `yield` is a PC scene move and duel term (event kinds prefixed `fight.`); `cede` is `give` with a Rung object; treaty terms are `covenant` content | — | Different actors and objects |
| **R-20** | Doublets and near-doublets: `guard`, `ward`, `watch`, `patrol` | Kept apart by object: `guard` a person's body (PC), `ward` a thread (TW), `watch` a place (FI), `patrol` parked (GV) | — | V-19 noted; no merge is lawful across different objects |
| **R-21** | `bribe`, `suborn`, `turn` | `bribe` is FI's own row (the inducement to an unlawful act is its content, parked on J-C-6); `turn` (a rival's man served to you) is a content of FA `recruit` | — | V-05: a bribe is a means, suborning an aim |
| **R-22** | `infiltrate` built over another verb's write | FI's own row; the cover-bound membership it writes is **its own effect**, to be specified by FI before it is built | — | S-4: it may not be a composition |
| **R-23** | `lie`, `suborn` by threat | Parked on J-C-6. SC recommends yes, built in a stated order (§III.11) | — | — |
| **R-24** | The word `challenge`; the word `accept` | `challenge` is the duel (PC); "challenge a claim" in SC is `dispute`. `accept` stays PC's, STRAINED; another lane needing "accept terms" uses `commit` or its own word | — | L-17, L-12 |
| **R-25** | `ambush` named by PC and MB | One meaning (the first mover is set from a held cover), two hosts: a content of `fight` (persons) and of `march` (armies; parked) | — | Same parameter on two different mechanics |
| **R-26** | `restore`, `mend` (critic V-01) | `mend` is Mending (TW). `restore` is fabric repair only (EC), and refuses the lattice Site kind. The first pass's "`restore` keeps IN-35's fabric arm" is withdrawn; IN-35's Mending arm re-points to `mend` | v2 Part V §V.2.6 and §V.2.7 | TW's fold test: actor (a Thread Sensitivity gate) and mechanic (a roll) differ |
| **R-27** | `hunt`, `forage`, `provision` | `hunt` is `work` at a wild site (EC; the verb survives as a content); persons do not mint stores (W8) | WT, v2 | EC's reading holds W8 |
| **R-28** | `tend`, `heal`, `recover`, `mend` | `tend` is NP's care; `mend` TW's; `heal`/`recover` fold into `tend` (self-tending) | — | — |
| **R-29** | `proclaim`, `declare`, `utter`, `issue`, `order` | Five acts kept apart by actor class and write: `proclaim` (a seat, an edict to a place in its purview, GV); `declare` (a seat, a stance toward another faction, FA); `utter` (any person, a Proposition, SC); `issue` (a Record to a named executor, GV); `order` (documentless, GV) | — | FA's four-way table, extended |

### III.6 What this overturns in v2's first pass

Principal reversals, each argued in the Part VI section named. The first pass is cited by its filed text.

| first pass said | this Part says | where |
|---|---|---|
| the 66 live verbs distil to 37 (50 after the trial) | 92 verbs; the convention floor is kept | §III.0, §III.3 |
| "the game is short of readers, not of verbs; distil the vocabulary" | the readers are short (§III.10: the verbs wait on named mechanics), and the vocabulary was cut below what the genre needs | §III.0 |
| 15 combat moves fold into `fight` | ten were never verbs (scene moves of IN-46); six are acts, of which `accept`, `assassinate`, `capture` are keys of `fight` and `guard`, `rescue` own rows | PC |
| `recruit` and `hire` are `tell` or `oblige` with a reply | each is its own verb in the actor's voice | R-01 |
| `oblige` is "the binder's" act | the actor binds themself: the name runs against English, so `pledge` | NP, R-10 |
| `levy` FITS, then cut by the trial's treatment | `levy` raises troops; `requisition` moves stores | MB, GV |
| `declare (war)` is a preset of `utter` | its own row: a seat's public act | R-06 |
| `lock` folds into `weave`; `sever` kept as code-identical to Locking | `lock` has its own cost regime; `sever` is `dissolve` | TW |
| `mend` and `restore` double-cover Mending (V-01) | `mend` is Mending; `restore` is fabric | R-26 |
| `evade / defy` retires into `comply` | the row is two acts and splits | GV |
| `succeed` is cut | `succeed` is the heir's own claim (IN-61) | R-11 |
| `tax` is `issue` → `comply` → `transfer` | `tax` is a standing levy a MATTER reads | R-04 |
| `track`, `eavesdrop`, `decipher`, `infiltrate` cut or folded away | `track` → `examine`; `eavesdrop`, `decipher` parked as modes; `infiltrate` its own row | FI |
| `navigate`, `ride`, `sail`, `hunt` cut for lack of a route graph | `travel` hosts route, mount and water as parameters; the missing route graph is a named mechanic | WT |
| IV §3.4: a verb's context nodes are read from its root sense | withdrawn (S-5); the table is rebuilt from the row's reads and writes and the word's attested sense | `verbs-05` IV §3.4 |

