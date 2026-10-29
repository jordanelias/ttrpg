# Resolution design — the bottom-up designer's supply sheet and minimal edits (reference input to the handshake)

## Status: **REFERENCE (2026-10-29).** Written independently of the top-down design, from the code upward; includes a measured baseline of `build_realm(0)` over two seasons (the only thing run). **Superseded wherever `2026-10-29-resolution-design.md` differs.** Kept because the resolution design cites its supply sheet, baseline counts and probe plan.



---

# BU — Bottom-up design: parliament and debate from what the code supplies

Designer: BOTTOM-UP (agonist, stage 1). Tree: `C:\Github\ttrpg-parliament` @ `89f31735`. Input:
`CORRECTED_REGISTER.md`. Every `file:line` was opened in that tree; paths are under
`engine/season/` unless prefixed. **[M]** = measured by me this session (`probe_bu.py` in this folder,
`build_realm(0)`); **[A]** = [ASSUMPTION]; **[U]** = unmeasured.

## 1. SUPPLY SHEET

**The one score.** `decision/choose.py:130-151` `score_terms(p, c, fx, memo) -> (pursuit, stance,
urgency)` is the single owner of the chooser's score (IN-62): `pursuit = damp·Σ axis_w[ax]·align(c.verb, ax)`
(verb only), `stance = stance_term(p,c,fx,memo)` (subject only, `:54-106`), `urgency` constant per
deliberation (`:217-238`, inert by construction). `Candidate.operands` reaches the scorer
(`_payload_of`, `:544-561`) and **no term reads it**. Every I6 change enters here or nowhere.

| I | Supplied today (symbol, file:line) | Behaviour | Gaps / hand-built only / [U] |
|---|---|---|---|
| **I1** World→topic | `questions_for` `queries/world_q.py:2811`; Q2 via `reach` `:813`; Q4 `need` via `ambitions` `:2262` + `goal_referents` `:2301`; sitting question `:2953`; `_stamped` occasions `:2983-2991` (`vacancies` `:2480`, `seats_named` `:2505`, `writs_held` `:2523`, `places_named`, `larders_in_purview`). `utter` (`verb_table.yaml:1608`, `_eff_utter` `loop/effects_information.py:1073`) | Questions come from landed claims, standing ambitions, sittings, and classed standing occasions on `out[0]`. `utter` mints `Proposition(id, mood or OUGHT, subject or actor, predicate or "", value)` (`:1100`) and opens the utterer's `hold`; `commit` then reaches it through `reach`. | **A computed `utter` carries only `subject`** (`utter` has no typed cell → `operands` `{}`; `_payload_of` adds `subject`), so every computed Proposition has `predicate ""`, `value None` [M: see §3 P0]. The content an R1 reader would read **does not exist in computed play**. Only the build's seeded creeds/goals carry predicates. |
| **I2** Topic→room | `open_case` (`verb_table.yaml:958`; `_eff_open_case` `:274-352`); `carry` (`:108-130`; `_eff_carry` `:356`); `petition` (`:1011`); `_docket_item` `:162`; `docketed` `world_q.py:193`; `docketed_under` `:319`; `slot_for` `:258` | A docket item is `{date, matter, arrangement, petition}`. `open_case` (remit:`determine`, purview over the matter's place) mints a `text` case file **with stages** (`_declared_stages` `:143`) and fills the nearest open slot — **only for a Person matter** (`slot_for` `:271`), else appends a dateless item. Declines a matter already docketed (`:341`). | Identity = the matter id; a Proposition id can be docketed (dateless) but `sittings_before` skips it (`:307`) and `determine`'s `party` conjunct refuses it. Arrangement/petition keys are `None` on every computed item (H-80). |
| **I3** Summons | `convene` (`:281`; `_eff_convene` `loop/effects_governance.py:370-416`); CALENDAR `loop/calendar.py`; `sittings_before` `world_q.py:283-316`; `_ch_chronicle` `epistemic.py:649-686`; `_ch_co_located` `:428` | `convene` writes a Date `{venue, holder=via, due_at=tick+1}` and emits `date.scheduled`. **`convene` is `binding_decision`, so `_ch_chronicle` broadcasts `date.scheduled` to everyone alive (`told_by`)** — a realm-wide summons already exists. CALENDAR's `date.fired` is on no verb's `emits:`, so it is heard firsthand only by those present at the venue. | `sittings_before` admits only a `date.fired` claim with `when == due` and only bench members (`judging_set`). A member is never asked about a sitting; nothing makes him travel. Claim subject of `date.scheduled` (Date id vs venue) [U]. |
| **I4** Bench | `judging_set` `world_q.py:474` (unused `matter` param `:493-513`); `BENCH_BASIS="determine"` `state/gate.py:243`; `may_determine` `:752-807`; `sits_over` `:729`; `establishment_of` `world_q.py:2184` over `sworn_to` `gate.py:440`; `oblige` (`:936`; `_req_oblige` `loop/predicates.py:358-417`); `may_renew` `gate.py:698-726`; `purview_reaches` oblige clause `:389-428` | Bench = holders granted `determine` whose `scope_rung` contains the venue. 8 seats hold `determine` at build, 13 hold `convene` [M]. Membership = live `oblige` to a seat (imposed included); a computed `oblige` forms only on a seat the joiner's ledger names (`referent_named`). | No council type. `bench` and `establishment` are two populations. `BINDS_BASES` has one value. A non-imposed `oblige` = vassalage (purview). Term renews only by the seat-holder's paid `transfer`. |
| **I5** Speech→hearer | `argue` (`:131-166`; `_eff_argue` `:555-581`; `argued_pursuits` `queries/person_q.py:638-658`); `speak` (`:1177-1204`); `tell`; `modules/social_contest/roll.py` | `argue` needs a Proposition subject and the hearer `with` the arguer; contested; a win moves each held pursuit of the hearer toward the arguer's weight. `speak` on a docketed subject writes nothing, emits `matter.carried/advanced/held/turned`. | Neither reads the Proposition's operands. `argue` cannot move one side of one motion. |
| **I6** Hearer→vote | `commit` (`:205-220`; `_eff_commit` `:1111`); `release` (`:1051`); `terms_sourced` `rosters.yaml:1963-1995`; readers available: `pursuit_lean` `person_q.py:599`, `regard` `:393`, `legitimacy` `:452`, `opinion_of` `world_q.py:2388` | `commit` forms on Proposition referents the person reaches (his own utterance) or on a held dispensation's `terms`. | Content-blind score (above). |
| **I7** Count | `determine` (`:352-409`, four conjuncts party/docket/bench/`bench.size>=quorum`); `data/arrangements.py:64,205-221` (`declared` + `quorum` accepted at load) | Judge vs party contested roll; opens the arrangement's `disposes:` kind (`oblige`/`detain`/`ban`) on `via`; Record disposal **declines** (`_disposal` `:584-610`). | **CR-34's tally is NOT in this tree** (no `declared` row, no tally code: grep). |
| **I8** Document | `_mint_document` `:171-197`; MATTER Record stages `loop/matter.py:310-354` (`Record.matured`, `term.matured`); Tenure `term` → `T-n` `:387-394`; `Term` `state/carriers.py:43-68` | Two lawful maturation clocks exist: a Record's act-declared stages, and a Tenure's declared term. | No `resolution` record kind (CR-36 unbuilt). `determine` Failure leaves the matter docketed. |
| **I9** Executor | `writs_held` `world_q.py:2523-2545`; `comply` (`:221-244`); `evade / defy` (`:439-453`); `give` (`:571-595`; `_eff_give` `:795`); `issue` (`:596-632`); `warrant_sourced` `rosters.yaml:1924-1961` | A held writ naming the holder is a stamped occasion; `comply` forms on it. `comply` **writes nothing** — "what compliance PERFORMS is the separate act the writ names" (`:242`). | **`evade / defy` is untyped and NOT in `resolvable_verbs()`** [M: False] — declining is not formable today. Only the maker holds a minted writ (ED-IN-0292 (1)); reaching the addressee needs `give` (H-229: rare). |
| **I10** Act→world | `seize` (`:1151`, warrant_sourced), `arrest`, `give`+Rung (`rung.ceded`), `confer`, `revoke`, `transfer`, `requisition` | The world-changing acts all exist and all license on a held Record or on a seat. | Only `seize`/`arrest` read a held document as licence. |
| **I11** Witness | channels `epistemic.py`: `co_located` (firsthand), `document_key`, `witness_key`, `post_remit` `:563-646` (obligees at the seat, `inferred`), `chronicle` (binding_decision kinds, everyone, `told_by`) | `determine`, `issue`, `convene` are `binding_decision`: their outcomes are public. `utter`/`commit`/`argue`/`open_case` are `social`: heard only by those present (or obligees). | — |
| **I12** Stability | `consequence_pursuits` (no clamp, `person_q.py:627`); `argued_pursuits` (pull toward arguer only); `opportunity_key` bar (`loop/deliberate.py:329-357`); 5 rounds | — | No bound on herding; no player menu. |

**Baseline measured [M] (P0, `build_realm(0)`, 2 seasons, hash `52a106bcb0ce`):** `utter` 44 acts →
44 Propositions, **every one `predicate ""`, `value None`**; `commit` 63 acts, **63
`commitment.refused`, 0 made** (formed on Person/Rung/Record referents); `argue` 9, all
`argument.refused`; `open_case` 11 (6 `case.opened`); `determine.refused` 6, **`matter.determined` 0**;
`convene` 5, `date.scheduled` 1, `date.fired` 1; docket 7 items, 1 dated; `give`, `oblige`, `comply`
**0 formed**. At build: 67 Propositions — 21 goal/creed OUGHTs **with real operands**
(`goal_varfell_oastad_gate`: subject `terr_T13`, value `Varfell`, 5 commits;
`goal_crown_peninsular_sovereignty`: subject `off_npc_020`, 15 commits), 46 personal principles (value
`True`), 2 live `oblige` edges. **The realm's debate chain is dead end to end at seed 0; the only
content-bearing Propositions are the seeded goals, and they are SHARED (many persons already commit
to one id).** The design builds on that.

## 2. PER ROOT PROBLEM

### The spine (every root below is one piece of it)
A **motion is a goal-backed OUGHT Proposition** (`goals.yaml` mints it under the goal's id,
`world_q.py:2307`). A man tables **his own live ambition about the thing his question is about**; the
docket item names that Proposition; the sitting question puts it before the convening seat's sworn
members; each member's `commit` (for) / `release` (withdraw) is scored by a **content reader** over the
goal's operands and his own edges; the tally counts live commits **to that id**; a carried motion mints
a **dispensation** (no new kind) addressed to whoever holds the motion's subject; he answers by an ACT
(`comply` + the performing act, or `evade / defy`), and a defiance is the occasion for others' acts.

### R1 — Consequence-blindness (I5, I6)
**(a) Primitives.** `score_terms`; the goal row read person-side through `data/goals.py` (`goal`,
`expected`, `.pursuits`, `.object`, `.org`) — `decision/` may import `data/` (`choose.py:35-49`); the
**salience closure inside `attention_key`** (`world_q.py:2732-2747`), which reads only `data/` and `p`;
`projected_axes`, `to_axes`, `pursuit_cosine_axes` (`data/pursuits.py:98`); `faction_prop_id`;
`p.tenures` (own edges, AX-2-lawful); `argued_pursuits`.

**(b) Minimal change set.**
1. *One owner for the aim.* Lift `salience` into `queries/person_q.py` as `goal_aim(p, prop_id,
   scar_shift) -> float` (cosine of `p`'s projected axes with `to_axes(expected(org) +
   goal.pursuits)`; a creed → `expected(faction)`; else `0.0`); `attention_key` calls it. Hash EQUAL.
2. *The content reader*, new, person-side: `person_q.motion_terms(p, prop_id, fx) -> (aim, stake,
   delay)`, GENERAL over the goal row's operands:
   - `aim = goal_aim(...)` — the **predicate** operand, read through the goal's typed `pursuits:`
     (the prose predicate is not machine-readable [M]).
   - `stake` — **subject × value against holdings**: `objs` = the ids the goal's `object` names (`rung`,
     `seats`; `seat_holders`/`deed_doers` → `()`); `mine` = `p` holds a live `commit` to
     `faction_prop_id(goal.org)`; `held` = `p` holds a live `hold` on some `o in objs`.
     `stake = (+1 if mine) + (-1 if held and not mine)`. A Varfell man gains from "Varfell holds
     Oastad"; Oastad's non-Varfell holder loses; everyone else 0. **No per-motion table.** A quantity
     operand (40 grain vs 25) has **no computed instance** — no goal row carries a magnitude — so
     magnitude enters only as the count of `objs` held [A]; a quantity waits on a producer (§4).
   - `delay` — seasons until the consequence lands: `0` for an act that writes this season, `1` for a
     motion (its consequence needs another person's act) [A; revert: no delay].
   Non-goal Propositions (creeds, principles, every computed utterance) read `(0, 0, 0)`.
3. *Enter the score:* `score_terms` gains a fourth term
   `motion = g_m · side(c.verb) · (aim + w_r(odds, appetite) · h(delay, horizon) · stake)` for a
   Candidate whose `subject` is goal-backed; `side` is a **per-VERB** polarity (`commit` +1, `release`
   −1, `argue`/`speak` +1, else 0) in a new `rosters.yaml: motion_polarity` table; `g_m` = new fixture
   `motion_gain`, **`0` the control** (byte-identical). `memo` caches `motion_terms` per subject as it
   caches `regard`. `score_terms`' other readers (`harness/decision_spread.py`,
   `engine/season/tests/test_in62_decision_spread.py`, a reference in `person_q.py`) unpack a 3-tuple
   [M: grep] — all updated in the same commit.
4. **Risk and horizon enter THIS reader and nowhere else.** `w_r(odds, appetite)` multiplies the stake
   by the believed chance the motion carries (CR-17's believed-odds input, CP-T01-03's reader) bent by
   appetite (`odds ** (1 − appetite)`, appetite ∈ (−1, 1), 0 neutral) [A]; `h(delay, horizon) = 1` if
   `delay ≤ H` else `0.5 ** (delay − H)`, H ∈ {1, 3, 5} (`part4.md:138`) [A]. **The consequence
   representation is `(aim, stake, delay)`, computed when read from the Proposition's operands and the
   voter's own edges — no stored aggregate.** Where appetite and horizon COME FROM is not supplied: none
   of the seven axes carries either [M `PURSUIT_AXES`]; until a field is authored both read neutral
   (`w_r = odds`, `h = 1`), so the term ships live and the dispositions are a later data edit.
5. *Content-sensitive `argue`.* `argued_pursuits` gains `toward: dict | None`; `_eff_argue` passes the
   argued goal's pursuit map **signed by `sign(goal_aim(arguer, prop))`**, so a won argument moves only
   the hearer's held pursuits the motion engages, toward it if the arguer favours it, away if he
   opposes. A non-goal Proposition passes `None` → today's behaviour. This moves **one side of one
   motion** (and of motions pointing the same way).

**(c) Alternatives.** *Smaller:* `pursuit_lean` over the predicate verb (the register's candidate) —
rejected: the predicate is prose, there is no verb, and it keeps value-blindness (A3-X2). *Larger:* a
WITNESS `content:proposition` deposit so a person reads any Proposition's operands from his own claim
(`content:dispensation`'s precedent) — general, but needs a deposit rule and a typed-predicate producer
that does not exist; deferred until `utter` can carry operands (H-80).
**(d) Hazards.** `motion_gain > 0` moves any world where a goal Proposition is a scored Candidate;
today no `commit` succeeds [M], so the 1-/2-season realm hash may stay EQUAL until R2 lands [U].
Argue change: realm wins 0 [M]. Interaction: without R2 nothing puts a goal Proposition on a member's
question, so this term has no Candidate.
**(e) Falsifier / control.** Hand-built: two persons with equal pursuits, one holding `terr_T13`
outside Varfell, one Varfell-committed; at `motion_gain=1` they rank `commit
goal_varfell_oastad_gate` on opposite sides; at `0` identically (CONTROL). Planted failure: `stake`
forced 0 reddens it. Argue: a won Varfell argument moves the hearer's `honour/stability/stewardship`
only; `toward=None` moves every held key.
**(f) Layer 1.** None if the fourth term is H-03's open weighting (*"only the weighting is open"*) [A];
if `04 §F2`'s three-term sum is read as closed, it is an amendment to `04 §F2` — name it.

### R2 — Information to members (I2, I3)
**(a)** `sittings_before`; `_ch_chronicle` broadcasting `date.scheduled`; `sworn_to`; the sitting loop
(`world_q.py:2953`); `commit`'s plain-referent formation.
**(b) Minimal change set.**
1. `sittings_before(w, p)` widens on two clauses: **who** — on the bench **or** a sworn (non-`imposed`)
   member of the Date's holder seat (`sworn_to(w, date["holder"])`); **how he knows** — the `date.fired`
   claim on the firing tick **or a `date.scheduled` claim about that Date landed before `due_at`** (the
   summons; hearsay of SCHEDULING — the ban on hearsay of a FIRING stands).
2. The sitting question's referents become `matters + motions` (R4's `DOCKET_MOTION`). `commit`,
   `release`, `argue` form on the Proposition by the unchanged referent rule; `determine` on the party.
   No class, no source added.
3. **M-2 by seeding, not a channel:** the council seat is minted at build with its members' sworn
   `oblige` edges via `offices.yaml`'s `obligees:` (`offices.yaml:128`; precedent: NPC-070 on
   `off_npc_020` [M]). Later members join by `oblige` once a deposit names the seat (IN-10 (a)).
**(c)** *Larger:* a `place_of` limb for a Proposition (its subject's place) — general, answers H-227
too, but falsifies "a Proposition has no place" everywhere and moves every world. *Smaller:* bench-only
voting — fails goal (3).
**(d)** Mover wherever a sitting fires with members. Scene tax: the Proposition referent forms
`argue`/`release` that refuse [U]. Turnout is bounded by attention: tier 0 only for members whose
ambitions name the party; `first` delivers one question — selection, not a defect, but measure it.
`argue` still needs co-presence (B-9).
**(e)** Hand-built: a member told `date.scheduled`, absent from the venue, is asked and forms `commit`;
one told nothing is not. CONTROL: a bench-only world reproduces today's questions. A `date.fired`
claim a tick late still admits nothing.
**(f)** None (a Query's admission rule).

### R3 / R7 — Delivery, execution, how an assembly causes change (I8–I10)
**R7, stated plainly:** an assembly causes change **only through persons' acts on the occasions its
resolution creates**. The resolution is a writ addressed to whoever holds the motion's subject;
holding it puts an answer on his list; both answers are acts and both are witnessed; a defiance is the
occasion for other members' acts (`issue` a warrant → `seize`).
**(a)** `_mint_document`; `writs_held`; `comply`; IN-09's typed `evade / defy` (`60073e75`, reverted at
0 executions); `terms_sourced`; `warrant_sourced`; `give`/`rung.ceded`; `hold_force`.
**(b) Minimal change set.**
1. `_eff_determine`, row `disposes: Record`, Overwhelming/Success: mint via `_mint_document` a
   **`dispensation`** (CR-36's new `resolution` kind is unnecessary: K-11/K-54, *a writ is distinguished
   by its terms*) with `terms = motion.subject`, `to = [holder of motion.subject]`, held by the
   determining actor (ED-IN-0292 (1)). `determine`'s band `writes:` gain `Record.exists` (check-only
   beside the Tenure pairs; the `(Record, exists)` cell exists — no new cell). No Tenure opens, so
   the gate's `determination` basis is not asked.
2. **Delivery without reversing ED-IN-0292 (1):** `world_q.writs_to_deliver(w, p)` — dispensations on
   `p`'s live `hold` whose addressees do NOT name him — stamped `Record`-classed after `writs_held`; a
   roster beside `terms_sourced`, `held_sourced: {give: [dispensation]}`, lets `give` form, beside its
   plain referents, on a held writ (`to` fans over known persons; `with` decides at the fold).
3. **The answer is an act:** re-type `evade / defy` as IN-09 did (`referent_class: Record`,
   `referent_named`, cell `existence subject dispensation ∧ own_ledger subject`) so it is resolvable
   [M: today it is not]. The performing act: `terms_sourced` gains `give: [dispensation]` — the
   addressee forms `give terr_T13` to a known person; `rung.ceded` is the change. His score:
   `motion_terms` (stake −1) against `regard`/`legitimacy` toward the issuing seat's holder.
4. **Enforcement occasion:** `compliance.withheld` is heard by those present and the issuing seat's
   obligees (`_ch_post_remit`; the writ was minted through `via`) — i.e. the council members. One whose
   seat grants `issue` may `issue` a warrant naming the rung; `seize` forms by `warrant_sourced` —
   **unchanged code** (`_seize_rung` licenses on occupation, so enforcement is a muster: persons).
**(c)** *Smaller:* a warrant to the chair (he seizes) — makes the chair an executive; rejected.
*Larger:* mint into the addressee's hand (reverse ED-IN-0292 (1)) — removes the `give` hop and
H-229's risk; **the one ruling I would ask for** (§4).
**(d)** Re-typing `evade / defy` moves any world with a held addressed writ [U]. `give` is the weak link
(0 formed [M]; H-229). `commit`'s `terms_sourced: [dispensation]` would form on the rung and refuse —
drop it only if measured as tax.
**(e)** Hand-built: carried motion → `{terms: terr_T13, to: [holder]}` held by the chair; after `give`
the holder forms `comply`, `evade / defy`, `give terr_T13`; `give` emits `rung.ceded`; `evade / defy`
emits `compliance.withheld` heard by the obligees. CONTROL: Failure mints nothing; a `bench` row
disposes as today.
**(f)** None: record kinds are content; H-44 answered as data.

### R4 — Motion identity and lifecycle (I2, I7, I8)
**(a)** `_docket_item` and K-55's keys; `ambitions` + `goal_referents`; `hold_force`; the case file's
`_declared_stages`; MATTER's `Record.matured` write (`matter.py:310-354`).
**(b) Minimal change set.**
1. Two docket keys, `TERM_KEY`'s shape: `DOCKET_MOTION` (Proposition id), `DOCKET_FILE` (the Record the
   item is heard on: `open_case`'s case file, `carry`'s petition).
2. `_eff_open_case` derives both **world-side from the actor's own state**: `motion` = the first of
   `ambitions(w, actor)` whose `goal_referents` contain the act's subject [A: "a man tables his own live
   ambition about the thing"]; if the subject is a Rung/Office, the docketed **matter** is its holder
   (`hold_force`), so the party is a person, `slot_for` fills a sitting and `may_determine`'s party
   conjunct holds. A hand-built act may name `motion` (K-55). No operand coined; H-80 not filled.
3. **Identity:** an item is the same motion iff `(matter, motion)` match; `open_case` declines only that
   pair. Two live motions about one party stay blocked (`_eff_determine` clears every item naming the
   party) — the register's limit, kept.
4. **Lapse = the tabling act's declared term, matured by MATTER, read when asked:** an item whose
   `DOCKET_FILE` is `matured` is not live; one helper `live_item(w, d)` read by `docketed`,
   `open_slots`, `sittings_before`. MATTER writes nothing new — `(Record, matured)` is the existing cell
   — **no new write-matrix cell, no fourth clock**; the term is the act's `stages` (`H-80`'s declared
   default, swept by `record_stage_term`). A lapsed slot reopens.
5. **The tally (CR-34, in this form):** for a `disposal: declared` row, `determine`'s quorum conjunct
   counts **distinct sworn members of the Date's holder seat plus the bench holding a live `commit`
   whose object == `DOCKET_MOTION`**, computed when read, against the row's `quorum`. Commits predating
   the tabling count — the motion IS a standing ought [A; revert: `since ≥ tabled_at`, readable from the
   file's stages]. Withdrawal is `release` (`commitment.ended`, witnessed).
**(c)** *Smaller:* CR-34 as written (subject = party, predicate names the `disposes:` kind) — no
identity, no lapse, and the predicate test matches nothing [M: goal predicates are sentences].
*Larger:* matter = motion id, `determine` on a Proposition subject — clean, multi-motion, but a new
typed cell.
**(d)** Mover wherever `open_case` executes (realm 6 [M]): items gain two keys (K-55 declared the same);
the `hold_force` substitution changes which person a rung matter dockets (today dateless and never
heard). Lapse length [U].
**(e)** Hand-built: file stage due t+2 → at MATTER t+2 the item stops being docketed, the slot reopens,
the question stops; a second `open_case` on the pair declines before t+2 and executes after. Tally,
quorum 2: two members committed to the motion → admitted; one to the motion and one to the faction
creed → refused. CONTROL: a `bench` row ignores the tally.
**(f)** None: keys on a sequence the `DocketItem` cells cover; the lapse is MATTER's ruled stage
maturation.

### R5 — The body and the bench (I4)
**(a)** `BINDS_BASES` + `_req_oblige` clause 2's foreseen second basis (`predicates.py:380-382`);
`purview_reaches`' `imposed` skip (`gate.py:411-428`); `judging_set`'s unwired `matter` and every
row's `bench_basis`; `may_determine`.
**(b) Minimal change set.**
1. `binds_bases` gains **`council`** — *the joiner's act admits him; his oath brings the seat no
   ground*. Its rule at the one site: `purview_reaches` skips sworn edges to a `council` seat (beside
   `imposed`). A King who joins a duchy council hands it nothing (A2-P-6).
2. `offices.yaml`: one council seat per parliament rung, realm first (`off_court_parliament` at
   `r_valoria`, untitled post, `binds: council`, `remit_acts: [convene]`, `upkeep: 0`, `obligees:` = the
   ladder title-holders inside the venue — CR-38's default as DATA [A]). **Its chair holds `convene`
   only, so he judges nothing else** (every `bench` row reads `determine`).
3. **Per-arrangement bench** — the one line `judging_set` foresaw (`world_q.py:500-502`): `basis =
   ARRANGEMENTS[row]["bench_basis"]`; `parliamentary_debate` gets `bench_basis: convene`, `disposal:
   declared`, `quorum: 2` (swept {1,2,3}). For a `convene`-basis row the bench narrows further to
   **the holder of the seat that convened the sitting** (`date["holder"]`, read through the docket
   item's `date`) — *the convener presides* [A] — so two `convene`-holders over one venue (the King's
   `off_npc_020` and `off_npc_032` both qualify at `r_valoria` [M]) do not both preside. The
   precondition's `bench` stem passes the basis to `may_determine(..., basis=)` (site: the `bench`
   stem's reader in `data/requires.py`, [U] exact line); for a Record row no Tenure opens, so gate
   and fold cannot desync.
4. **The ruler:** he presides only if HE convened (his seat grants `convene` [M]) and votes only if
   sworn (he is not); a motion about his seat is carried by members, and he answers the writ (R3). A
   motion the King convenes and chairs against himself is the party-is-judge case — `may_determine`
   conjunct 2 refuses it (`party == actor`), so a hostile parliament needs a convener other than the
   King: the council seat's own holder. That is the political content of who holds that seat.
5. A1-M3 (party already obliged) is moot for Record rows (nothing opens on the seat).
6. Upkeep 0: `_renewals` renews every obligee on any seat transfer (`effects_economy.py:313`, "0: all
   of them"); otherwise membership lapses at `oblige_term` and the member re-swears. The purse lever
   is weak by data.
**(c)** *Smaller:* the interim two-seat bench. *Larger:* a council TYPE field on `Office`; CR-38 route
(i) (rejected: `sits_over` walks up).
**(d)** Build hash mover (new office, obliges). Council members now hear acts done through the council
seat (`_ch_post_remit`) — wanted. Second owner (A2-P-7): voters = `sworn_to`, judges = `judging_set`,
two roles, two existing owners.
**(e)** A motion about the King's seat carried by two sworn landed members, refused by one; the chair
cannot `determine` a `legal_trial`; a King sworn to a duchy council leaves `purview_reaches(council,
his ground)` False. CONTROL: `binds: members_by_admission` restores the vassalage reading.
**(f)** `council` is the foreseen basis — data plus its rule at one site. Whether a council oath may
carry no purview against `AX §E.2.5` is a reading [A]; if Jordan reads E.2.5 as vassalage, it is a
Layer 1 question.

### R6 — Reach and unread keys
`bench_basis` (R5.3), `disposal: declared` + `quorum` (R4.5) gain readers. Computed items get an
arrangement: `_eff_open_case` writes `DOCKET_ARRANGEMENT = parliamentary_debate` when the slot's Date
holder seat has `binds: council` [A] — the first computed route to a named arrangement, ending H-80's
reach 0 for council sittings. The other keys stay unread; none is needed. **B-10:** for a `declared`
row the contest opponent is `obstacle_default`, no opposition (CR-35 (6)'s polarity keyed on
`disposal`) — dice measure procedure; a Failure leaves the matter docketed until its file matures [A].

### R8 — Stability, legibility, the player (I12)
(1) The argue rewrite pulls toward OR away from a motion by the arguer's side, so opposed arguers
contest one vector instead of everyone converging on the winner's profile. (2) Clamp
`consequence_pursuits` and the argue move to the authored range [A; the docstring's own revert].
(3) No social-proof term, so no herding loop is built. (4) **Scarcity:** a Date forms one slot; one
live motion per slot; `opportunity_key` bars a second `commit` on the motion per season. (5) **The
player's menu** is the same Candidate list on the sitting question — `commit`/`release` the motion,
`argue` a present member, `speak` to the docket, `open_case`/`carry`, `give`/`comply`/`evade / defy` a
held writ; a human chooser replaces `choose` on no new path. (6) Unanimity and capture are not
prevented; they are measured (P6).

### R9 items that touch code
- **D4/F2 weighted votes:** the tally can weight each counted commit by a computed-when-read factor
  (`legitimacy`'s precedent, `person_q.py:452`) — e.g. the number of the voter's live `hold`s inside
  the venue (an estate weight) — with no stored aggregate. Not in the minimal set; one line in the
  tally if wanted [A].
- **D8 sortition:** fits as the convener's own act over `sworn_to` (a draw keyed by the act,
  `draw_factory`), choosing which members' commits count. Not in the minimal set; it needs a
  subset carrier (a docket key naming the drawn members) — larger than its N.
- **C7 non-reply / self-contradiction:** evaluable from claims a named person holds (`speech` and
  `argument.*` deposits), but nothing reads them into the contest yet; out of scope.
- **"A deposed king" cannot emerge at seed 0 (H-230)** [U whether the King dies in season 1 at this
  tree, P5]; the spine needs only a seat holder alive at the sitting.

## 3. DEPENDENCY ORDER AND MEASUREMENT PROBES

| Step | Lands | Needs | Hash |
|---|---|---|---|
| 1 | `goal_aim` lifted to `person_q` (one owner); `attention_key` calls it | — | EQUAL (P1 control) |
| 2 | `binds: council` + its purview clause; `off_court_parliament` seeded with `obligees:` | — | build MOVER (`build_realm(0)`, 1-/2-season, goldens if the realm is goldened) |
| 3 | `DOCKET_MOTION`/`DOCKET_FILE`; `_eff_open_case`'s motion and holder derivation; `live_item` lapse; council arrangement on computed items | 2 (arrangement read off `binds`) | MOVER where `open_case` executes |
| 4 | `sittings_before` widened (members + summons); motions on the sitting question | 2, 3 | MOVER |
| 5 | `motion_terms` + the fourth score term at `motion_gain` 0; `motion_polarity` table | 1 | EQUAL at 0; MOVER at the shipped gain |
| 6 | per-arrangement bench (`convene`, convener presides); `parliamentary_debate` → `declared`, the tally | 3, 4 | MOVER |
| 7 | Record disposal → `dispensation` mint; `determine` writes `Record.exists` | 6 | MOVER |
| 8 | `writs_to_deliver` + `held_sourced: give`; `terms_sourced: give`; `evade / defy` re-typed | 7 | MOVER |
| 9 | content-sensitive `argue`; clamps | 1, 5 | MOVER where an argument is won |
| 10 | appetite/horizon fields (data) | 5, CR-17 commit 1 | MOVER |

Each step is a hand-built falsifier first (the (e) lines) and a realm reading second. Every probe
below is a script beside `probe_bu.py` (same build/run shape: `populated.build_realm(seed)`, a
`SeasonDriver`, `make_chooser(..., verbs=resolvable_verbs(), draw=draw_factory(...))`, N seasons),
run with `PYTHONUTF8=1` on Windows [M: cp1252 breaks the roster load otherwise].

- **P0 (done)** baseline: the counts in §1, seeds 0, to extend to seeds 0-2.
- **P1** `goal_aim` refactor: content hash at 1 and 2 seasons equal to P0's (`52a106bcb0ce` at 2).
- **P2 = B-9** (does anyone off the venue hear a firing): for each `date.fired` Event, list persons
  holding a claim with that subject and `predicate == "date.fired"` and `when == due`, split by
  `source` and by whether they were in `cache.presence_index` at the venue; ALSO the `date.scheduled`
  holders (count, `source`, claim `subject` — Date id or venue, which step 4 must match). Seeds 0-2,
  4 seasons, with step 2 applied so a council convening exists.
- **P3 = M-2** (does a duke learn the council seat): per season, `seats_named(w, p)` ∋
  `off_court_parliament` for each title-holder NOT seeded as obligee; and `duty.taken` on it.
- **P4** `convene` on the renamed King's seat: settled [M] — `p_npc_020` holds `off_npc_020` with
  `convene` (and `off_duke_valorsmark`). Re-check after step 2 only if the build renames seats.
- **P5** the Widow Regent / the King: log `person.died` with tick for the holders of `off_npc_020`
  and `off_npc_032` over 4 seasons, seeds 0-2; and whether either `convene`s.
- **P6** the chain after steps 2-8: per season count `date.scheduled`, sitting questions asked to
  members (instrument `questions_for` output by `q.id` prefix `q:sitting:`), `commitment.made` on
  goal ids, the tally value at each `determine`, `matter.determined`, dispensations minted with a
  goal subject in `terms`, `record.given` of those, `compliance.given`/`withheld`, `rung.ceded`; and
  **the distribution of commits per motion** (unanimity/capture: share of members on the majority
  side, and whether the same seat-holder's motions always carry).
- **P7 = resolution handover by `give`** (UNMEASURED today): after step 8, over the corpus
  (`harness/corpus_run.py`) and seeds 0-2, count `give` Candidates formed on a held dispensation,
  their `give.refused` reasons (the `with` conjunct vs no known receiver), and executions. H-229's
  method: log the chair's questions at the barrier after the mint.
- **P8 = H-229/H-230 corpus counts:** `corpus_run` 143 worlds, count `record.given` by Record kind
  and `rung.ceded`; for H-230, whether any claim names the throne after the King's death.
- **P9 scene tax:** `argument.refused`, `commitment.refused`, `release.refused` per season before/after
  step 4; a rise beyond the new successes is the cost of the extra referent.

## 4. WHAT THE CODE CANNOT SUPPLY CHEAPLY (and what I ask the top-down side to relax)

1. **Content in computed Propositions.** Every computed `utter` is empty [M]. Content exists only in
   the 21 seeded goal/creed rows. A motion about *this harvest's 40 grain* has no producer; it needs
   an operand channel (H-80). **Ask:** accept goal-backed motions as the first deliverable; motions
   are drawn from what persons are already committed to.
2. **Magnitude.** No quantity operand on any motion; `stake` is a sign. **Ask:** relax "40 vs 25" to a
   later step.
3. **Appetite and horizon as person data.** None of the seven axes carries them [M]. The reader hosts
   them; the values need authoring (or a ruled derivation). **Ask:** decide their source.
4. **Delivery.** `give` forms 0 times [M]; ED-IN-0292 (1) bars minting into the addressee's hand.
   **Ask:** reconsider ED-IN-0292 (1) for resolutions only (the addressee's hold opens with the mint),
   or accept that delivery is a co-presence event and rare.
5. **Several live motions about one party.** Needs `determine` on a Proposition subject. **Ask:**
   relax to one live motion per party.
6. **Co-presence for debate.** `argue` needs `with`; nothing makes members travel for a sitting. A
   debate happens only among those present. **Ask:** accept that debate is the members at the venue;
   absent members vote by commit (§2 R2), not by argument.
7. **A sitting decides one matter at a time per slot**, and a Failure keeps it until the file lapses.

## 5. MY OWN WEAKEST POINTS

1. **`_eff_open_case` reading the actor's ambitions to name the motion** is an effect inferring
   intent from state. Defensible (his own live commit about the thing), but it is the closest thing
   here to a decision the person did not make on his Candidate; if two ambitions match, "first in
   edge order" is arbitrary [A].
2. **Reading `goals.yaml` person-side as a Proposition's content** assumes a member who has the
   Proposition as a referent knows what it says. For goal ids this is the content; for anything
   else the reader is silent, so the design covers ~21 Propositions in the realm. Narrow.
3. **The summons is admitted from a `chronicle` broadcast**, so EVERY sworn member is summoned
   realm-wide; distance never costs a vote. Possibly too frictionless (S), and `chronicle`'s own
   docstring says it is slated to be replaced by a `<rung kind>` reach channel — my summons rides a
   channel with a declared successor.
4. **Counting pre-tabling commits** means a motion whose goal already has 15 committed persons
   (`goal_crown_peninsular_sovereignty` [M]) can carry with no debate at all if they are sworn
   members. Debate then matters only at the margin.
5. **`evade / defy` was reverted at 0 executions**; I re-type it on the claim that resolutions give it
   an occasion — unproven until P6.
6. **Step 7 adds `Record.exists` to `determine`'s bands** beside Tenure pairs; whether the fold's
   "first pair is the receipt" convention tolerates a band whose receipt differs by arrangement is
   [U] — it may force a split row (`determine` vs a council verb), which is larger than I claim.
7. **I did not run any proposed change**; only P0 and the build census. Every hash claim in §3 is a
   prediction.
