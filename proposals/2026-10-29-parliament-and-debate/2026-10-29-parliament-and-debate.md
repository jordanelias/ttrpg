# Parliament and debate — a motion drawn from the world, a sitting that argues it, a result the loop can feel

## Status: **PROPOSED (2026-10-29). Design only. Nothing here runs. No head, roster, verb row, arrangement row or code moves; no `ED`/`PP` is allocated; no `CURRENT.md` row moves.**
## This file is CR-38's design file (`workplans/valoria_master_workplan_v10_part4.md:404-415`), widened to the three things Jordan asked for on 2026-10-29. **HELD BACK from ED-1094's merge default: §12's calls.** Merging this file does not ratify them.
## **SUPERSEDED IN PART by `2026-10-29-resolution-design.md` (same folder).** That file withdraws this one's Speaker, `determine` on the council seat and the `resolution` it mints (§1; §2 steps 3 and 7; §4), the `evade / defy` reach clause (§4, §6 T3b), §6 T2 and T3b, §10 B-6 and B-7, §12 calls 1, 3 and 5, and §13's PD-2 and PD-3 as written. Sections 3, 5, 7, 8, 9 and 11 survive as reference. CR-38's gate still names this file as approved; re-pointing that build is Jordan's (see that file's relation paragraph). Stale facts corrected below: `Claim.round` exists; the shipped `bench_quorum` is 1 and cannot refuse; Varfell's duchy bench is not empty.

> **THE ASK (Jordan, 2026-10-29).** (1) two or more characters debate a topic that concerns worldly subjects
> retrieved from the season loop; (2) the result renders impact on the game world at the seam; (3) a basis
> for a parliament at the kingdom, duchy, province and territory rungs whose motions can move the world —
> *"even if it is just a change in opinions about a subject."*

---

## 0. The result, stated without softening

**The ratified architecture already has the right shape for a parliament. The running engine does not yet have the parts.** A sitting is a chain of existing acts; but seven of its links cannot run today, and the honest size of the work is the list in §10, not "a few readers".

**What the architecture gives us for free**

| | what | where |
|---|---|---|
| a | **A council is ONE seat; its members are the persons who `oblige` to it, and a join is the joiner's own act.** `hold` is one-per-object, so N parliament seats is *forbidden*; membership is a Query over live `oblige` edges, `establishment_of`. This decides the bench (§4) and removes the need for any new remit act, any new `arrangements.yaml` key, and any inverse containment in `sits_over` | `architecture/meta/01_AXIOMS.md` `AX §E.2.5` (`:1537`); `proposals/2026-09-17-governance-and-holdings-r2/03_SEATS_AND_CONTENT.md:671-698` (ruled); `world_q.hold_force` `:138-144`; `establishment_of` `world_q.py:2184` |
| b | A vote is a **count of live `commit`s, computed when read and stored nowhere** (CR-34) | `part4.md:352-362` |
| c | The assembly never acts on the world: it mints a document, and a seat that already has the power acts on it (CR-36 `resolution`, CR-37 `joint_concurrence`) | `part4.md:378-402` |
| d | The title ladder: realm king/queen, duchy duke/duchess, province count/countess, territory lord, settlement mayor | `engine/season/offices.yaml:153-166` (Jordan, 2026-09-02, verbatim) |
| e | Ownership is always a person's `hold`: territory is held by a person; a faction is a Proposition plus a view and never acts | `carriers.py:730`, `faction_q.py:84-96` *[agent-read]* |

**What does NOT exist** (each is a row in §10 with its owner): a way to bring a motion to the room · a way to summon an absent member · a way for a speech to carry the motion's content · a way for a voter to weigh a motion's content · a defined end to a motion · a Record-disposal site · a parliament seat · a land/asset consent conjunct · a completable negotiation.

---

## 1. The shape, in one paragraph

A **motion** is an OUGHT Proposition whose **subject is the person it concerns** (the *party*: the holder whose land, seat or act is in question) and whose predicate names what is proposed — exactly CR-34's counted-commit form, so nothing new carries it. The chair of the council seat convenes and calls it; **members** (persons who have obliged themselves to the council seat) hear speeches, each deciding for himself whether to `commit` to the motion; `determine`, on a `declared` row, is admitted only when ≥ `quorum` members hold such a live commit, and mints a `resolution`. The **owning seat** (the ruler of that rung) executes the resolution by his own ordinary act — `give`, `confer`, `revoke`, `issue` — which is admitted only where it holds a live `resolution` naming it. If he does not, the resolution stays held, citable and unexecuted — **but a non-act emits nothing**, so silence leaves nothing for the room to see. The record bites only if declining is itself an **act** (the writ machinery's `evade / defy`, which emits `compliance.withheld`, or a step of a remonstrance ladder), and only if the resolution reaches him by something that forms (B-12). The fit adjudication reaches the same conclusion independently (`2026-10-29-debate-fit-adjudication_part4.md` §0).

Almost every motion has a person party, because persons own all edges: *cede territory T* is a motion about **its holder**; *fill seat S* is about **the nominee** (CR-36 already mints `to: [party]`); *deposition* is about **the monarch** (CR-37). So no party-less `determine` is designed here. A matter with no person in it (a pure policy question) is **not carried**; see §12.

---

## 2. The sitting, in order

Season order is fixed: CALENDAR, MATTER, then R rounds of [DELIBERATE, RESOLVE, ENCOUNTER, WITNESS], then CENSUS (`loop/driver.py:452-519`). **The sitting is season-granular, not round-granular.** `Tenure.since` is the season tick and no round is stamped on an Event or a Tenure (`effects_information.py:1166-1167`; `driver.py:531-535`; `Claim.round` exists, for Claims only), so the engine cannot tell round *r* from *r+1* in a stored record. Anything below that claims an order *within* a season is marked.

| # | step | act / reader | season | precondition it actually reads | leaves |
|---|---|---|---|---|---|
| 1 | **Summons** | `convene` → a `Date` | *s* | `convene` in the convener's grant (**unverified for the King**) | the `Date` fires at *s+1*: CALENDAR (`effects_governance.py:406`; `calendar.py:40`) |
| 2 | **Salience** | `questions_for`, new variant (§3) | *s+1* DELIBERATE | a strain query holds **and** an independent trigger landed in the member's ledger | a `Question` |
| 3 | **Tabling** | `utter` the OUGHT, then `open_case` with the **Date as operand** | *s+1* RESOLVE | the tabler holds `remit:determine` and purview over the **party**; the slot exists | a docket item |
| 4 | **Attendance** | the member `oblige`s and **stands at the venue** (§5) | *s+1…* | co-presence for `argue` (`verb_table.yaml:142-144`) | a member in the room |
| 5 | **Speeches** | `speak` to the body; `argue` to one member | *s+1…* | a Proposition; for `argue`, `with` (same place) | pursuits moved; claims witnessed |
| 6 | **Division** | `commit` (each member's own act) | counted only if made in a season **after tabling** | the motion exists | live `commit` edges |
| 7 | **Declaration** | `determine`, `disposal: declared` | ≥ one season after step 3 | ≥ `quorum` members hold a live `commit` to **this** motion | Success: a `resolution`. Below quorum: **refused, and retried every round** (at the shipped `bench_quorum` of 1, `fixtures.py:945`, the quorum cannot refuse; this describes a raised value) |
| 8 | **Execution or refusal** | the owner's own act | any later season | the act's precondition, plus *holds a live `resolution` naming it* | the world change, or nothing |
| 9 | **Lapse** | MATTER (new) | *the season after the division season* | the item is still docketed | the item is cleared; `matter.lapsed` is emitted and witnessed |

**What is enforced and what is not.**
- **Enforced:** a Date cannot fire before *s+1*; a `commit` to *this* Proposition cannot exist before its `utter`; a Proposition is immutable, so a re-tabling is a **new** Proposition and starts with no commits (the refusal is only while the first is docketed, `effects_information.py:341`).
- **NOT enforced: speech before commit inside a season.** Both are RESOLVE acts. The only enforceable order is season-granular: **count only commits made in a season after tabling** (`Tenure.since > tabling season`). That needs the tabling season recorded — the docket item is a plain dict `{date, matter, arrangement, petition}`; whether it takes a fifth key, or the tick is read off the `utter` Event, is a build question (§10 B-6). **A cheaper order — "committed after being argued" — is not available**: no `commit` records what moved it.
- **NOT withdrawable by being persuaded away.** Commits never close on their own (`:1128-1131`). A member who changes his mind must `release` his own `commit` (`repudiate` was cut at IN-11 and `release` absorbed it, `verb_table.yaml:1062`); until he does he still counts. Releasing a commit emits `commitment.ended`, a witnessed **vow-break** that is itself judged by the room (`deed_valence`), so changing one's vote openly has a reputational price. Persuasion therefore changes **who commits next**, not who has already, and the cost of reversing is part of the design rather than a loophole.
- **Nothing ends a motion today.** At Failure `determine` writes `[]` and the matter stays docketed (`verb_table.yaml:389,391`); a below-quorum attempt is a *precondition refusal*, which writes nothing at all (T-b, `01_AXIOMS.md:356-358`) and is retried every round (`deliberate.py:332-340`); `term_required` is not read. Step 9 is therefore **new**, not a reading.

---

## 3. Where a motion comes from — salient subjects

A world fact cannot raise a proceeding (`14_THE_WORLD_IN_THE_ROOM.md` Part B). Facts raise questions, questions raise Candidates, a person acts. The lawful route is the one `sittings_before` took: a `claim_landed` variant of `questions_for`, not a third source (`world_q.py:2811-2822`, `:2937-2954`).

| motion kind (a roster row; data) | strain: a query that already exists | party | proposes |
|---|---|---|---|
| fill a seat | `vacancies` (`world_q.py:2480`) | the nominee | name him (feeds CR-36) |
| dispose of an ungoverned place | `uncontrolled` (`:2030`) | the intended holder | `give` on a Rung |
| relieve a shortfall | `hunger` (`:1536`), `larders_in_purview` (`:2585`) | the holder of the larder | requisition / transfer |
| end or enter a war | `at_war` (`faction_q.py:219`) | the opposing head | covenant on terms |
| censure / restrain | `restrained` (`:1404`), `legitimacy` (`person_q.py:452`) | the accused | `oblige` / `revoke` (CR-37 for the throne) |
| dispute a hold | two live `commit`s to rival HOLDS on one object | the holder | `determine` the hold |

**Two attacks on the first draft survive and are built in.**
- **The rule is not "two-signal".** The research needs an **independent legitimating trigger** beside material strain — a fatwa, an acclamation, an authority's utterance (`conflicts_power_struggles.md:14,32`); a claim *about the same strain* is only awareness of it, one signal. So the trigger must be a claim of a **different kind**: an utterance by a seat-holder, or a witnessed Event of another class. [ASSUMPTION; medium; revert: strain alone, which is one signal and fizzles by the research's own account.]
- **The question will not be answered unless it ranks.** Each member answers one question per round (`question_aggregation_rule="first"`, `data/fixtures.py:487`, which delivers only `out[0]`). A sitting question about a Proposition lands in attention tier 4, below every `need` (tier 3) (`world_q.py:2761-2764`), so a member with any ambition never sees it. The motion therefore must ride as a **stamped standing occasion** (`_stamped`, `world_q.py:2983-2991`), as `vacancies` does, or its rank must be set in `attention_key`. The existing docstring lists **five** stamped occasions, not six (`:2812-2817`).

**No new threshold.** A strain band (how low legitimacy is "low") is a swept `[ASSUMPTION]` row like `standing_band_floors`; until it is ruled the kind is not seeded. The roster of motion kinds is data the code reads, and a kind naming no strain query or no executing verb is **refused at load** — the loader's refusal per data family, the only guard licensed.

**P-24 stays open** (`14:113-119`): a motion about a *possible* future (invasion) has no producer.

---

## 4. The body — the council is one seat (CR-38's question, answered)

**Route taken: one council seat per rung, members by `oblige`.** This is `AX §E.2.5` and `r2 03` §A.9, both ratified; it is not a new route. It replaces all five routes the first draft weighed.

| | |
|---|---|
| **The seat** | one `Office` per rung that sits: `body` = the roster's existing name (`office_bodies` already carries "Court Parliament" and "Jarl Council", `rosters.yaml:1725-1820`), `rung` = that rung, `remit_acts` including `determine`. Its single `hold` is the **chair** (a Speaker). |
| **The members** | `establishment_of(w, seat)` — persons with a live `oblige` to the seat (`world_q.py:399-413` per `r2 03`). **A join is the joiner's own act** (`oblige` is `own`-eligible, `verb_table.yaml:952-954`), admitted when the seat's `rung` reaches his containing rung. So a duke is *eligible* for the realm council because his duchy lies inside the realm; he is *a member* only if he joins. That is the Bohemian-estates move, and it is a decision, not a fact. |
| **The tally** | CR-34's "distinct members of the bench" reads `judging_set` (the holders of the `determine` grant). For a council seat the bench to count is `establishment_of(seat)` and the declarant is the chair. **That is one reading to add at CR-34, not a rule.** |
| **Estates** | the Church, a commune, an emerged creed enter the same way — by admission. CR-39's "promotion earns standing" becomes *a creed's members are admitted*, not a seat authored (the reader CR-39 waits on). |

**Why the first draft's routes are withdrawn.**
- *Grant `determine` to the duchy-head seats* (CR-38 route (i)): `judging_set` lists a holder only if `sits_over` — the seat's `scope_rung` is the venue or one of its **ancestors** (`gate.py:747-749`). A duke is scoped to his duchy, which is below a realm venue; the walk runs **up**, from the superior, and a vassal assembly runs the other way. `ancestry(realm)` is `[realm]` (`containment.py:121-127`), so no duchy seat is ever listed at a realm venue. *Refinement the plug-in critic made:* the bench the **determination** counts is taken at the **party's** place (`world_q.py:3341-3342`; `gate.py:807`), so under route (i) the party's *own* duke would count and no one else — never the assembly. It fails.
- *`bench_basis: assembly`*: `bench_basis` is typed a remit act (`data/arrangements.py:170-172`; `gate.py:238-243`) and Layer 1 defines the judging set as *the seats whose remit covers the matter* (`04_CODE_ARCHITECTURE.md:345-347`, F.8 `:1163`). An `assembly` value would contradict both and need an amendment. `bench_basis_of` also does not exist, and the gate cannot ask which arrangement is docketed (`gate.py:251-254`). Withdrawn.
- *A seat per member*: `hold` is one-per-object; `AX §E.2.5` says "not N seats". Withdrawn.

**The interim.** Today the realm bench for `parliamentary_debate` is the King's and the Widow Regent's seats (`world_q.py:475-481`); the King also holds `off_duke_valorsmark` (NPC-020) so a duchy-scoped read puts him on Hafenmark's side too (`offices.yaml:195-203`). **The duchy bench is thin, not empty** (Varfell has `determine` seats NPC-073 and NPC-074, `offices.yaml:494-518`) — the only titled posts are the five at `offices.yaml:183,196,209,222,235`, and the realm build raises on a titled holder with no row (`harness/populated.py:1392-1399`). The control in §11 keeps this interim.

**The chair and the ruler are separate seats.** The ruler convenes and executes (`off_king`); the Speaker declares (the council seat). That is the Lawspeaker's shape — a session-bound chair "bounded away from outcomes" (`rhetoric:516`) — and it lets CR-36's two-seat clause hold with no special case: a nomination minted through the council seat and confirmed through `off_king` are two seats (`part4.md:383` (iv)). Whether the ruler may also be a member is §12.

---

## 5. How a vote is moved — and what the engine cannot do yet

This is the weakest part of the design, and the first draft overclaimed it. What `argue`/`speak` do today:

- **`argue`** is one hearer per Candidate and needs co-presence (`relation of to, with`, `verb_table.yaml:142-144`; `world_q.py:3285-3296`). The roll is **a seed**: no `argue` row exists in `rosters.yaml:1230-1233`, so the arguer rolls `pool_default` 2; the hearer has no capability, so the obstacle is `obstacle_default` 2 under ceiling 2 (`roll.py:103-113`); `leverage` is always 0 (`sigma.py:191`). On a win the hearer moves toward the arguer's **whole pursuit profile** and **the Proposition is never read** (`person_q.py:652-658`; `effects_information.py:575`). Arguing for and against the motion is the same act; ethos, pathos, logos, stasis and audience (`rhetoric:107,212-217`) are absent.
- **`speak`** is the verb the proceedings design made for addressing a convened body, with `heard_by: bench` so `reception` enters the roll — but it writes **nothing at any band** (H-63) and `reception`/`proofs` never enter the `a proposition` prize (`rosters.yaml:1317-1322` vs `:1327`).
- **A voter cannot see what the motion says.** The pursuit term is `align(c.verb)` (`choose.py:149`), identical for every `commit`; the shipped `legacy` stance reads stance rows naming the referent, and none exist for a newly uttered Proposition (`person_q.py:70-79`). A cession, a censure and the rival motion score the same.

**So, as built, "debate" cannot change a vote *about this subject*.** What would make it so — three builds, in order, each with its own owner (§10):

1. **Speech carries the motion's content.** An `argue` win pulls along the motion's **predicate verb** (`pursuit_lean`, `person_q.py:600-612`) instead of the arguer's whole profile.
2. **The voter weighs content.** `commit`'s stance term gains one reader: the motion's predicate verb weighed against the member's **own pursuits and convictions** and the **party's standing with him** (his `opinion_of` the party's faction), one owner, no new field. This is what "an opinion about a subject" *is* in the engine; without it T1 below is empty.
3. **The room hears the body-speech.** `speak` gets writes (H-63's value problem, solved by `argue`'s precedent of computing the shift in a query) and the `a proposition` prize gains `heard_by: bench`.

**Attendance.** `argue` needs the speaker and the hearer at one place, and nothing brings a duke to the venue. Two options, neither verified to form in computed play: the member `move`s to the venue on the summons (an act with a cost — the duchy unguarded is the churn); or the summons is a **writ** he holds (the `writs_held` stamped occasion, `comply` as the answering verb), delivered by `give`, which the chooser cannot yet reach (H-229). **Also unverified: whether anyone not standing at the realm rung itself ever hears a realm-venue `date.fired` first-hand** (`calendar.py:54-58`; `epistemic.py:449-453`) — if no one does, `sittings_before` asks nobody, and the summons has **no addressee**. That is the first thing PD-1 measures.

---

## 6. What a result does

**Constraint.** A module returns a typed outcome and writes nothing; the host writes through the gate; every write needs a `write_matrix.yaml` row and, for a tenure change, a gate basis (`gate.py:196-309`); WITNESS never writes a belief (`world.py:61-104`). The assembly never acts on the world.

| tier | what it is | the write | gate cost |
|---|---|---|---|
| **T1 — opinion** | requires §5's builds 1-3. With them: a speech moves the hearers' `pursuits` along the motion's verb; the sitting's acts are witnessed by those present; a later `commit` weighs the motion. **Without them T1 is empty.** `records_dissent` is **not** a source: it has no reader but the loader, there is no "nay" act (not committing is not an act and emits nothing), and `floor` is inert (`arrangements.py:173-176`; `harness/probes.py:2725-2743` raises `Unspecified` for "nothing writes a per-seat division yet"). A per-seat division record is a separate build | `pursuits`, ledger claims | none for the writes; the three builds are the cost |
| **T2 — the record** | Success mints a `resolution` (CR-36's site, `_eff_determine`). **No defeat Record is designed.** The research's *senatus auctoritas* is a motion that **carried but was vetoed** (`S/01:88`), which the held, unexecuted `resolution` already *is*, citable and without force. A vote-down is a lapse (step 9), and the lapse Event is witnessed | a Record held by the declarant; `matter.lapsed` | CR-36 for the site; step 9 is new |
| **T3a — concurrence** | the owner's act gains the conjunct *the actor holds a live `resolution` naming this act's object*, as `confer` (CR-36) and `revoke` (CR-37) do. **Land and asset transfer enter here.** *Limit:* `warrant_sourced` maps one *kind* per verb and a listed verb then forms **only** on a subject a held Record names (`rosters.yaml:1931-1961`), so `give: resolution` would gate **every** `give`, not just cessions. The discriminator "this cession needs consent" must live at a **data owner** (a rung-kind or hold-kind row), not in the effect — otherwise it is scripting drift. And CR-36's two-seat clause needs `via`; `give` of one's own hold has none. Until both are answered T3a is limited to verbs exercised through a seat (`confer`, `revoke`, `issue`) | whatever the act writes | one conjunct per row, plus the data owner |
| **T3b — obligation** | carrying opens an `oblige` on the owner's seat | an `oblige` tenure | no gate basis lets a bench open a tenure on a **seat** (`DISPOSABLE_KINDS` bounds a bench to a person party, `gate.py:256-258`). **Held** |

**Inherited defect, not mine to close.** `determine` on a `declared` row is still a contested act: it rolls against `obstacle_default` (`verb_table.yaml:384`) after the vote has passed, so **a carried motion can fail on the declarant's dice.** CR-34 says nothing about skipping the roll. Either the declared arm resolves without it, or an unlucky declaration is accepted as content. This is CR-34's to decide at B10-13; recorded here so it is not discovered by a played session.

---

## 7. Negotiation and transfer between two characters

- **Offers are authored, dated `utter`s**; the treaty is the Proposition both hold a live `commit` to (`14:76-91`). The first offer therefore leaves a record a later party can produce.
- **That is all that is modelled.** Because the voter cannot yet weigh content (§5), a 40-grain offer and a 25-grain offer score identically; no reservation value exists, so *the first offer anchors* and *BATNA* (`S/04:118-126`, `S/01:527-530`) are **logged, not modelled** — not "taken" or "emerges".
- **A transfer cannot complete in computed play.** `covenant` needs `remit:issue` (seat-holders only); the instrument is held by its maker, the counterparty learns the terms only through `give`, which the chooser cannot reach (`effects_information.py:249-254`; `loop/witness.py:476`); its readers are deferred; and nothing ties a `give` to the agreed terms. If one side commits and the other never does, nothing lapses. **Negotiation is hand-built until a computed `give` forms** (H-229).
- **To close it** (PD-5): `give` gains the conjunct *the actor holds a live `commit` to terms naming this object* — the same data-owner discriminator as T3a.
- **Not modelled and noted:** side payments (a `give` never reaches a `commit`, so votes cannot be bought: `S/01:532-535`), reactance (a failed argument costs nothing: `S/04:108-110`), the fief as a **renewing** bond rather than a one-shot `give` (`political_hierarchy_standing:230`).

---

## 8. What the research says, and what this takes

Tier-3 sources (`research/00_INDEX.md`) — input, not authority. *[R] = in the corpus.*

| mechanism | source | this design |
|---|---|---|
| convening and framing are office powers | *ius agendi*, *relatio* (`S/01:82-84`) | **taken** — the ruler convenes (step 1) |
| strain plus an *independent* legitimating trigger | `conflicts_power_struggles.md:14,32` | **taken, narrowed** — §3: the trigger must be a claim of another kind |
| order of speech by rank | Roman Senate (`S/01:84`) | **declared, inert** — `order: rank` is read by nothing; building it is the nested run (`21_RECONCILIATION.md:579`) |
| a motion carried but vetoed persists, citable | *senatus auctoritas* (`S/01:88`; workplan P-4 exit `part5:282`) | **taken** — the held, unexecuted `resolution` (T2). *(The first draft cited `part4:246`, which is an unrelated position's source line.)* |
| peer veto / *intercessio* | `governance_modes:22`; blocks the *relatio* or strips a carried motion (`S/01:87`) | **absent** — the ruler declining to execute is an executive act, not a peer veto |
| session-bound chair separate from the Crown | Lawspeaker (`rhetoric:281,516`) | **taken** — §4: the Speaker is a separate seat |
| separate colleges, all three needed | Reichstag (`governance_modes:199`) | **deferred** — a flat establishment only |
| sortition against bribery | Venice (`S/01:69`) | **refused** — a bench by lot has no basis in `oblige` |
| first defector is the high-value target; first ballot dominates | `S/04:140-146` | **absent as built; fits if adapted** — every `argue` Candidate ties and a Gumbel draw breaks it across everyone the arguer knows (`choose.py:263-269`; `verb_table.yaml:145`); nothing in `score_terms` reads other members' commits, so there is no snowball. The fit form (adjudication D6/C11) is a voter's `commit` reading the *witnessed* commits of fellow members he regards: one term, his own ledger, no influence rounds |
| log-rolling; scaled compromise | `S/04:128`; `S/01:538-540` | **refused** — no producer (`by_lane/SC:14-16`) |
| first offer anchors; BATNA | `S/04:118-126`; `S/01:530` | **logged, not modelled** — §7 |
| consent for taxation | Cortes (comparative-governance file, row D-24 is *not* this); Joyeuse Entrée is a privileges-at-accession charter (`fa_se:138`) | **fits T3a** in principle; no tax/levy verb exists (only `requisition`) |
| stasis (fact/definition/quality/jurisdiction) | `rhetoric:90-99`; kernel `rhetoric.py` | **forensic motions only** — a HOLDS matter has the issue ladder; an OUGHT matter has none and `proofs: []` (`14:108-111`). The kernel is NOT adopted (SC-05); a reference, not an import |
| *disputatio*; the Nyaya named defeats | [own]; `rhetoric:205-221` | **refused** — a named-fault roster with no producer |

---

## 9. Four rungs

| sitting at | council seat's rung | owner (convenes, executes) | members who may join |
|---|---|---|---|
| **realm** | realm | King / Queen | Dukes / Duchesses |
| **duchy** | duchy | Duke / Duchess | Counts / Countesses (Lords where no province is assembled) |
| **province** | province | Count / Countess | Lords |
| **territory** | territory | Lord | Mayors |

`provinces_of` is computed and a province exists only while one faction holds its territories (`scale_hierarchy_v1.md` §2; `world_q.py:1886`), so a duchy whose territories are unassembled seats its Lords directly. The authored realm has **no province rung** (`offices.yaml:505`); a province sitting has nothing to run on there.

**Two earlier "prices" are dropped:** `venue_min_rank` and `disposal_reach` have no reader but the loader and tests, so lowering the floor changes nothing and nothing over-reaches today. Reach becomes real only when the `<rung kind>` reach channel is built (`21_RECONCILIATION.md:579`); until then a sub-realm resolution has **no machinery to reach anywhere**, and the claim that it "over-reaches" was wrong in the other direction — it reaches nothing.

---

## 10. The blockers, with owners — nothing here is hidden behind "readers"

*Inherited* = already in the plan; *new* = this design adds it.

| id | blocker | evidence | owner |
|---|---|---|---|
| B-1 | `determine` refuses a non-person matter at the `party` conjunct, `may_determine`, and `bench.size` (`place_of` of a Proposition is `None`). **Avoided** by §1's person-party rule; stated so the party-less arm is not smuggled back | `verb_table.yaml:363-366`; `gate.py:805-807`; `world_q.py:3341-3342` | avoided |
| B-2 | `open_case` declines an arrangement whose `disposes:` is not a Tenure kind; a docket item cannot name `parliamentary_debate` | `effects_information.py:334-337`; `gate.py:256-258` | CR-36 (the Record site) |
| B-3 | a computed `open_case`/`carry` names **no** arrangement (**H-80**), so any rule keyed on the row never holds outside a hand-built act. CR-34 records the same reach as 0 | `effects_information.py:319-325,410`; `part4.md:357` | inherited; **a dependency of PD-2 and PD-4** |
| B-4 | `carry` always appends a **dateless** item, which `sittings_before` skips; tabling must go through `slot_for` | `effects_information.py:414`; `world_q.py:307` | new |
| B-5 | the sitting question ranks below every `need` | `world_q.py:2761-2764`; `fixtures.py:487` | new (§3) |
| B-6 | no tabling season on the docket item; no round on a Tenure or an Event (`Claim.round` exists) | `driver.py:531-535` | new (§2) |
| B-7 | a below-quorum `determine` is a refusal that retries forever (at the shipped `bench_quorum` of 1 it cannot refuse); nothing lapses; `term_required` unread | `deliberate.py:332-340` | new (step 9) |
| B-8 | `argue` ignores the motion; the voter ignores the motion | §5 | new, three builds |
| B-9 | the summons has no addressee; attendance is unmodelled | §5 | new |
| B-10 | a `declared` determination still rolls | `verb_table.yaml:384` | **inherited — CR-34** |
| B-11 | `give`/T3a consent discriminator has no data owner; `give` has no `via` | `rosters.yaml:1931-1961` | new |
| B-12 | a computed `give` does not form; negotiation and delivery are hand-built | H-229 | inherited |
| B-13 | `Act.via` is plan position 6 and the council's tally reads the exercised seat | `r2 03` §A.10 | inherited; **unverified how far it has landed** |

**Hash.** The first draft said every pin stays EQUAL until `parliamentary_debate` is flipped. That is **false**: a new `questions_for` stamp reorders `out[0]` under `first`, and a new conjunct on `give` changes admission — each changes the hash whether or not the row is flipped. **Both are declared MOVERS**, to be measured when built (`build_realm(0)`, the 1- and 2-season pins).

---

## 11. Exit and falsifiers — each able to fail

None is run; the build runs them.

1. **The bench is the assembly (CR-38's exit).** A motion against the King is carried by a council of ≥ 2 admitted members and refused with one. **Control:** the interim two-seat bench kept → the outcome differs. *Falsifier for §4:* grant `determine` to a duke and list a realm-venue `judging_set`; if he appears, the inverse-containment claim is wrong. (Tried against `populated.py:1407,1467` by the plug-in critic: every built seat gets `scope_rung = rung`, and it could not be falsified.)
2. **Membership is a decision.** A duke who has not `oblige`d is not counted; one who has is. **Control:** `release` him → not counted.
3. **Order, season-granular.** A `commit` made in the tabling season is not counted; one made later is. *The first draft's mutation ("drop the `since` filter") could not redden* — every commit to a Proposition uttered at tabling is already after the slot — so the plant is instead: a commit made in the tabling season, with the filter on, must be **refused by the tally**; with it dropped, **admitted**.
4. **Opinion changes a later vote on this subject — both directions.** Same seed, three runs: no speech; a speech **for**; a speech **against** by the opponent to the *same* k members. The commit counts must move up, stay, and move down. The first draft's falsifier (pursuits differ; commit counts differ) passed on *any* shift and so could not fail. Control: `argue` at Partial/Failure → no change. **This test is meaningful only after §5 builds 1-2.**
5. **Strain without trigger forms nothing; trigger without strain forms nothing; both form one.** Control: a member whose `reach` omits the referent gets none, even with both. *Falsifier for B-5:* a member with an ambition still receives the stamped motion.
6. **A motion ends.** A tabled motion below quorum for one full season is cleared and `matter.lapsed` is witnessed; a re-tabling is a fresh Proposition with no commits.
7. **A carried, unexecuted motion leaves a held `resolution` and no world change**, and the ledgers of those present hold the claim *carried, not executed*. If no claim lands, reception is dead.
8. **`judging_set` and the gate agree.** For a council seat the members the Query lists are exactly the members the gate admits to the tally, over the same world.
9. **Hash.** Seeded rows unchanged → `build_realm(0)` and the 1- and 2-season pins EQUAL *until the first mover is built*; each mover (§10, Hash) is recorded when built, never assumed.

---

## 12. Unverified, out of scope, and Jordan's

**Unverified (stated, not guessed).** Whether a member's `commit` forms as a Candidate on a sitting question in computed play (the first measurement, PD-1); whether anyone hears a realm-venue `date.fired` first-hand; whether `convene` is in the King's grant; whether `give` on a Rung forms computed (`test_in12_give_rung.py` is hand-built); whether `speak` requires co-presence; how far `Act.via` has landed.

**Out of scope.** The nested run (`order`, `proofs`, `speech_kinds`); weighted and bicameral votes; the per-issue vector (ED-SC-0038); multilateral treaties; ransom; a tax/levy verb; many-part motions; sortition; a per-seat division record; a policy motion with no person in it (it has no party and so no disposal, and the `14` design already refuses it).

**Jordan's calls — held back from the merge default.**

1. **Titles.** Canon fixes province = count/countess and territory = lord; **marquis appears nowhere in canon**. If the intended ladder is king / duke / marquis / count, province and territory both change, which overwrites the 2026-09-02 verbatim ruling (`H-90`). This file uses canon.
2. **How far a parliament binds** (H-90: *"there is a Parliament, so there is no monopoly of power in the ruler"*). T3a lets the ruler decline *by an act*; T3b makes declining a breach. This file ships T3a and holds T3b. The adjudication judges T3a (negative concurrence plus a witnessed held record) the fit and T3b a misfit: it makes the ruler's non-act the breach, and gives the assembly the monopoly H-90 denies the ruler.
3. **Who chairs, and may the ruler sit?** This file makes the Speaker a separate seat and the ruler convener and executor. Canon calls the Crown "first among equals" (`canon/03_canonical_timeline.md:88`); the interim bench seats the King.
4. **Is a motion allowed to lose on dice after it carried?** (B-10.) It is CR-34's to settle; a played session will feel it first.
5. **Debate depth.** v1 reuses `speak`/`argue` with §5's three builds; the alternating-exchange nested run comes later if at all, and SC-05's adoption timing is decided with it.

---

## 13. Build order — proposed positions, not plan edits

This file edits no workplan (one active plan per lane). Each position names the artifact that shows it ran.

| | position | rests on | artifact |
|---|---|---|---|
| PD-1 | **probe** (no code change): does a sitting question reach a member, does `commit` form, does a realm `date.fired` reach a duke? | — | a run and its log; decides whether PD-2…4 are computed or hand-built |
| PD-2 | a council seat for the realm, members by `oblige`, the tally reading `establishment_of` (§4) | CR-34, CR-36, B-3 | §11.1, 11.2, 11.8 |
| PD-3 | tabling through `slot_for`; the tabling season; step 9's lapse (§2) | PD-2 | §11.3, 11.6 |
| PD-4 | motion kinds as stamped occasions (§3) | PD-1, B-3 | §11.5 |
| PD-5 | §5 builds 1-3 (content in speech and in the vote) | PD-2 | §11.4 |
| PD-6 | T3a conjuncts and their data owner; `give` consent (§6, §7) | CR-36, CR-37, B-11 | §11.7 |
| PD-7 | the sub-realm councils and the reach channel (§9) | `21` step 15 | a province resolution that does not reach the realm |

**Not licensed:** a tree-wide guard (`CLAUDE.md` §0.1 pt 5). The licensed checks are the loader's refusal per data family (§3) and the falsifiers above.
