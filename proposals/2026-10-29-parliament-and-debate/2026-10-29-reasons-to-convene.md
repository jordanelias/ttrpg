# Reasons to convene — what the season engine would have to produce, and make salient, for a sitting to have a point

## Status: **REFERENCE (2026-10-29).** An analysis of what exists, measured on `main` at `120b3bf7` (after REM-28). It is a judgment about the engine as built, not a plan: it allocates no `ED`/`PP` and queues no work. §6 is a requirements analysis (what the engine would have to produce, make salient and constrain), not a to-do list. Measurements are read-only probes outside the tree (seeds 0-2, four seasons, the shipped chooser; the engine is deterministic across processes, checked).

> **Asked (Jordan, 2026-10-29):** *"carefully perform an analysis of what the season engine would need to produce and make salient in order for social contests to have reasons to convene."*

---

## 0. The result in six lines

1. **The engine convenes sittings and holds matters, and the two never meet.** Per four-season run it schedules 21-23 sittings (12-17 fire) and holds 4-9 person-matters awaiting one. **Zero to one waiting matter in a run is ever placed in a sitting's slot, none is determined, and 11-17 sittings are empty.** Part of that is placement, not salience: CALENDAR forms each slot as `{date, matter: None}` (`calendar.py:65`), and only `open_case` fills one, only when it creates the case (`effects_information.py:347-351`); `carry` appends a dateless item (`:414`) and both decline a matter already docketed (`:341`, `:405`). **A matter that is already waiting is never back-filled into a later slot**, however many sittings follow.
2. **Why: `convene` has no reason in its inputs.** It forms only on a rung that the *places-to-settle* stamp offers (the REM-28 note says so in its own words: "the rung stamp is places-to-settle, not venues"). A lord convenes where he has *heard of*, at the smallest tier, with no matter behind it.
3. **The tier of a sitting is its jurisdiction.** A sitting convened at a `hearth`-tier rung (the barracks, the inn) can hear only matters at that same hearth; `slot_for` walks *up* from the matter's rung. This is the concrete way the user's reading of a rung — a tier — governs the mechanics. Only 2 of 6, 2 of 4 and 3 of 8 undated matters can find any open slot.
4. **The matters exist and are within reach of a convener, but are not salient.** Every waiting matter lies under some `convene`-holder's scope (6 of 6, 8 of 8), yet the matter is in that holder's top five questions in only 3-4 of 20-22 covering pairs (≈14-20%). A convener faces 700-1,200 `claim_landed` questions a season against 32-39 `need` questions, and answers one per round.
5. **Most of the other classical reasons have no producer at all** (elected vacancies, disputes over holdings, offences reaching custody, consent-gated acts). The one cheap producer already running is the docket.
6. **Of the seven levers in §6, three carry most of the leverage, in order:** put the convener's referent on the *tier where a matter waits*, not on a place he has heard of; manufacture demand by making some acts need a sitting's count; and give the strained matters a producer. Each has a falsifier in §6.

---

## 1. Terms — what "rung", "tier" and "venue" mean here (a correction Jordan made)

Jordan's words: *"a rung has never been a place in my understanding"*, and "where" a decision occurs means a hierarchical position, not necessarily a physical place. The repo agrees with the type and the engine blurs it:

- **The type is a tier.** `Rung := (id, kind (ORDERED; the ordinal is rank), matter, dates[], envelope)` (`04_CODE_ARCHITECTURE.md` §B.3, `:255-258`); "`Rung` is the holon, one type at eight scales" (`holonic_ARCHITECTURE.md:58`); *"a rung is where a decision happens; a person is who makes it"* (§10.2). The eight kinds are `person < hearth < community < settlement < territory < province < duchy < realm`. ED-IN-0303 (Jordan, 2026-10-28) kept the word `rung` because Godot has no word for it, and defined it nowhere.
- **The engine also uses the ladder as its only location system.** A building is a rung: `b_s_014_barracks` and `b_s_001_court` are **`hearth`** rungs (`Site` is a separate carrier, for harbours and seams: 322 of them). A person "stands" at the smallest rung that contains him (`presence`, `co_located`, `place_of`). There is no separate geography in the engine's state.

So this analysis keeps two things apart that REM-28 and my earlier wording ran together:

| notion | what it is | engine surface |
|---|---|---|
| **the tier of a sitting** | which scale the sitting is held at, therefore its **jurisdiction** and which council counts | the Date's venue rung and its `kind` |
| **attendance** | where a person stands, so who can hear and argue | the hearth-tier rung a person occupies; `co_located`, `with` |

Whether the engine should keep location *as* the bottom tier, or model it separately, is a ruling that is Jordan's and the repo has not made. The analysis does not depend on it, but it changes the vocabulary: "convene at the realm rung" means "hold the sitting at the realm tier", not "gather at a place called the realm".

---

## 2. How `convene` forms today

- **Eligibility:** `remit:convene` (13 seats held by 12 persons at build: territory `T9` ×3, `T1` ×2, the realm ×2, the duchies ×5, one seatless).
- **Referent:** after REM-28 (`verb_table.yaml:292`) a `convene` Candidate forms **only on a `Rung`-classed referent** that the question carries, and the only stamps that carry one are `places_named` (every rung his own ledger names that he does not live under) and `larders_in_purview` (a stocked rung in his purview; it offers nothing to anyone, 0 of 83).
- **Score:** the chooser scores the *verb* (`align(convene)`) plus a stance on the subject plus an inert urgency. Nothing in the score reads what a sitting would be *about*.
- **Effect:** `_eff_convene` makes a Date `{venue, holder = the seat exercised, due_at}`; CALENDAR fires it and forms **one empty docket slot**; `convene` "puts a date on the calendar and stops" (RL5).
- **Measured outcome (three seeds):** 23, 23 and 21 sittings scheduled, 17, 17 and 12 fired; conveners are lords' and clerics' seats **including the King's** (`off_npc_020`, seeds 1 and 2), always at a hearth-tier rung — a barracks, an inn, a court, a cottage, a market, a guildhall, a croft — and once at the territory `T13`. *(An earlier version of this design said the King never convenes. It was measured on the engine before REM-28 and was wrong for the current tree.)*

---

## 3. What a reason to convene is, in this architecture

A sitting has a reason when **all** of these hold. Each maps to one layer of the engine, which is why the layers, not the matters, are where it fails.

| | condition | layer | rule behind it |
|---|---|---|---|
| **N1** | a **matter** exists as world state, not as a meter | producer | persons own all edges; a disposal must write something that can be lost (`14` ABOUT-the-world test) |
| **N2** | a would-be convener **holds a `convene` grant whose scope covers the matter's tier** | power | `sits_over`; `judging_set`; purview |
| **N3** | the matter is **known to him**: a claim in his own ledger | knowledge | AX-2, AX-7: nothing arrives except by channel |
| **N4** | it is **salient**: it reaches the question he answers this round | `questions_for`, `attention_key` | one question per round (`first`); tier 0 aims, tier 1 `mine`, tier 2 judged deeds, tier 3 need, tier 4 the rest |
| **N5** | a `convene` Candidate **forms at the matter's tier** | `opening_set`, referent class | the class rule; `_derive_operand` |
| **N6** | the Candidate **outscores the alternatives for this matter** | `choose` | score is verb-only today (R1) |
| **N7** | the members and parties **learn and can attend** | witness, co-presence | `date.scheduled` is a `binding_decision`, chronicled |
| **N8** | the sitting **can dispose** the matter | `determine`, arrangement | the matter's tier lies under the sitting's tier (`slot_for` walks up) |

---

## 4. The reasons, with where each one stands

Evidence labels: **[M]** measured · **[R]** read in code · **[I]** inferred. "—" = not measured.

| reason | N1 produced? | N2 power | N3-N4 known / salient | N5 forms at the right tier | N8 can dispose | verdict |
|---|---|---|---|---|---|---|
| **A · docketed person-matters awaiting a sitting** (a trial, a hearing) | **YES** [M] 4-8 undated per run; `case.opened` 3-4 | **YES** [M] every one lies under some `convene`-holder's scope (6/6, 8/8) | known in part; **in the top five for 3-4 of 20-22 covering pairs** [M] | **NO** [R/M]: nothing stamps the matter's tier; the convener's referents are places-to-settle | YES in principle (`determine` disposes `oblige`/`detain`/`ban`); `matter.determined` **0** in all three runs, `determine.refused` 9-10 [M] | **the smallest gap and the cheapest real reason** |
| **B · petitions piling up** | YES [M] 26-33 filed and held per run | **NO** [M]: a computed petition's `terms` and `to` are the *same person*, the one it concerns (e.g. `terms: p_npc_003, to: [p_npc_003]`) — not the governor of the petitioner's tier | NO: `petition.filed` is `social` (heard by the present only) | NO | no decider named | a producer with no addressee that can convene |
| **C · an act that needs a count** (consent) | **NO** — no consent row exists | the owner | `<verb>.refused` **does** leave a claim in ledgers [M] (`give.refused` 13, `confer.refused` 4, `revoke.refused` 2, `determine.refused` 9, …) but carries no reason | NO | YES (the licence) | **the instrumental reason, and the one history shows**: rulers convened estates *because they needed consent* |
| **D · a vacant elected seat** | NO [M]: the seats offered vacant are all `appointed` (3-5); no elected seat in play (CR-35 unbuilt) | convener | n/a | n/a | yes | not yet producible |
| **E · a shortage** | partial: `hunger` returns a value for all 37 settlements [M] (decoding not verified); `stores.changed` ~150-260 | requisition-holders | `larders_in_purview` offers nothing, 0 of 83 [M, REM-28 note] | NO | only if a levy needs a count (it does not) | **no demand**: a lord who can requisition alone has no reason to sit |
| **F · an offence reaching custody → trial** | **starved upstream** [M]: `arrest`/`detain` **0**; `kill`/`sabotage`/`challenge`/`forge` are *refused* 50-89 times each per run | judges | — | — | yes | offences are attempted and refused, so few wrongs exist to try |
| **G · a dispute over holdings** | NO [M]: every computed `utter` is an empty Proposition | — | — | — | — | no producer |
| **H · war, peace, a treaty** | weak [M]: `march.declared` ~50, `covenant.offered` ~0, 7 `covenant.refused` | — | — | — | negotiation row unseeded | weak producer |
| **I · terms maturing** (oaths, writs, case files) | **YES, in bulk** [M] `term.matured` 613-667 per run (subjects not decoded) | — | — | — | — | a recurring periodic reason if a sitting were the renewal forum |
| **J · a legitimacy crisis** | computed on read, **no Event** [R]; the standing-crossing question "never fires in realm play" (H-222) | — | — | — | — | no occasion |
| **K · succession** | the King and Regent survive four seasons [M]; no death, no vacancy | — | — | — | — | no producer in play |
| **L · a standing session** | NONE; and no engine clock may produce one (T-c) | — | — | — | — | lawful only as a convener's Date or a term's maturity |

**Reading the table.** Only **A** and **I** are produced in volume today, and **A** has the shortest path to a reason: the matter, the power and (partly) the knowledge already exist. **C** is not produced at all, but it is the reason the history actually gives for assemblies, and it is *free in the sense that no world state needs inventing*: it needs a licence row (resolution design §3 I8) and a refusal that says why.

---

## 5. Why salience fails even where the matter exists

1. **Volume.** A convener's questions are 700-1,200 landed claims a season (a claim for nearly everything that happened to anyone he heard of) against 32-39 standing needs. The chooser takes **one question per round** (`question_aggregation_rule = first`, delivering only `out[0]`), so a matter has to be *first*, not merely present.
2. **The ranking is by the convener's relation, not the matter's importance.** `attention_key` places a question in tier 0 only if its referent is one of his ambitions' referents (`aims`), tier 1 if it is one of his own tenures' objects (`mine`), tier 2 if it carries a deed he judges, tier 3 for a `need`, tier 4 for the rest. A matter earns salience through the convener's own holdings — which is AX-2-lawful and means a matter about a tier he holds ranks high *without any new meter*. A docketed person-matter, however, names a person he may not hold anything over.
3. **A standing condition rides in by the stamped-occasion channel, not by ranking.** `_stamped` attaches classed referents to `out[0]` whatever its tier — the route `vacancies`, `seats_named`, `writs_held`, `places_named` and `larders_in_purview` already use. That is the established way to say "this condition is true for you now", and `convene` already reads its Rung class from it. **Nothing in the engine stamps the tier at which a matter waits.**
4. **Even a stamped candidate must win the score.** `convene` is scored by verb alignment alone, so it competes with every other candidate on the same question by how much the person's pursuits like the *word* "convene". A matter-sensitive reader (the resolution design's `motion` term, I6) is what lets *this* matter prefer convening.
5. **Attendance is the one link that is fine.** Since REM-28 so many Dates are scheduled that `date.scheduled` is held by 65, 67 and 67 of ~79 persons (≈85%); the summons reaches nearly everyone. First-hand hearing of a firing reaches 6-11 persons. *(Before REM-28, with 1-3 Dates a run, the figure was 2-69%; it measures how many sittings the engine schedules, not whether a channel is reliable.)*

---

## 6. What the engine would have to produce, make salient and constrain

**Levers, in order of leverage per unit of change.** Each names the measurement that would show it worked and the control that would show it did not just move numbers.

| lever | what changes | why it is lawful | measured now → target | control |
|---|---|---|---|---|
| **RL1 · stamp the tier where a matter waits** | a standing occasion `matters_awaiting(w, p)`: for each undated person-matter on the docket whose place lies under a seat `p` holds `convene` for, stamp the **lowest rung of that seat's tier that contains the matter**, as a Rung-classed referent, on `out[0]` — beside `vacancies`, `places_named`. `convene` then forms *at a jurisdiction that can hear the matter* | an existing mechanism (`_stamped`); a Query over the docket and containment, stored nowhere; no new verb | matters with a dated slot: **0/6, 0/4, 1/9** → above 0 for matters opened after the stamp exists. **Matters already waiting need a re-slot step as well**, because no act back-fills them (§0, `effects_information.py:341`, `:405`); without it the target cannot be met for them | a matter whose place lies outside every convener's scope stays undated; a world with no docketed matter forms no such candidate |
| **RL2 · stop offering places-to-settle as venues** | `convene` reads its Rung only from matter-bearing stamps (RL1, RL3), not from `places_named` | REM-28 itself names the limit; removes the empty hearth-tier sittings that cannot hear anything | fired sittings holding a matter: **0/17, 0/17, 1/12** → the share of fired Dates with a matter approaches the share of convenes that had one | convene count falls; matters heard rises. **Flag:** REM-28 landed (#526) while plan batch B10-06 is still in flight, so this is a plan change, not an edit |
| **RL3 · demand by constraint** | some acts are admitted only on a council's count (the resolution design's consent rows); a refusal on that conjunct has its **own kind** (e.g. `give.unlicensed`, not `give.refused`), so the refused owner holds a claim that says *why*, and the claim stamps the council's tier as his convene referent | `<verb>.refused` already deposits a claim in ledgers [M]; a distinct kind is data; the licence is the resolution design's | consent-blocked acts that lead to a convening: 0 → above 0 | an owner whose act needs no count never convenes for it |
| **RL4 · address petitions to the tier that can answer** | a computed `petition` takes `to` = the holder of the seat governing the `from` rung's tier, not the person it concerns (`from` is already an operand) | `to` and `from` exist; the change is in what the chooser binds | petitions reaching a `convene`-holder's questions: ~0 → above 0 | petitions with no governing seat stay unaddressed |
| **RL5 · let the matter reach the score** | the content reader (`motion` term) gives a convene Candidate a matter-specific sign, so convening can beat the alternatives for *this* matter | resolution design I6 | of persons offered an RL1/RL3 candidate, the share who choose it | gain 0 reproduces today |
| **RL6 · give strains a producer** | RM2: a motion kind per strain query (vacancy, ungoverned rung, shortage, war) bound through the typed `utter` | resolution design RJ-11 | motions per run: 0 → above 0 | a strain with no trigger forms nothing |
| **RL7 · terms as a periodic reason** | a council join carries a term, so oath renewal is a recurring occasion (613-667 `term.matured` a run is the raw supply) | T-n; reverses the resolution design's default of no term | renewals heard at a sitting | joins without a term never recur — the trade-off is that a term needs a renewer, and an unheld seat has none, so renewal would have to be by attending (RJ-membership) |

**What this does not fix, and the engine must be given before any of it matters:** offence supply (F) — `kill`, `sabotage`, `challenge` and `forge` are refused 50-89 times each; until some execute and reach custody, trials have few accused. The analysis names the starvation; the cause is upstream of social contests.

### Instruments (read-only, runnable now)

1. **Motivation rate** — fired Dates whose slot holds a matter ÷ fired Dates. *Now:* 0/17, 0/17, 1/12.
2. **Latency** — undated person-matters ÷ person-matters. *Now:* 6/6, 4/4, 8/9.
3. **Jurisdiction fit** — undated matters for which an open slot exists right now ÷ undated matters. *Now:* 2/6, 2/4, 3/8.
4. **Salience** — (matter, covering convener) pairs where the matter is in the convener's top five ÷ pairs. *Now:* 4/20, 3/22.

Each is computed from `w.docket`, `w.dates`, `slot_for` and `questions_for`; none changes the tree.

---

## 7. By proceeding — what would make each kind of social contest convene

| arrangement | the reason it needs | status now |
|---|---|---|
| `legal_trial` | an offence with an accused in custody | starved upstream (F); the docket path exists (A) |
| `tribunal` | an officeholder's abuse brought by someone with standing | no producer |
| `interrogation`, `inquisition_hearing` | a suspect in custody; a creed deviation | no producer |
| `excommunication_deliberation` | an ecclesiastical charge (SC-04 row seeded) | no producer |
| `arbitration` | two parties and a dispute | no producer (G) |
| `negotiation` | an offer outstanding between two persons | row unseeded; weak (H) |
| `parliamentary_debate` | a consent-gated act (C), a petition backlog addressed to a council (B/RL4), an elected vacancy (D) | no demand yet |
| `council_of_state` | an executive's need for counsel | no demand |

---

## 8. Limits

- **Measured on four seasons and three seeds**; none of the instruments was measured over a long run or the 143-world corpus.
- **`hunger` decoding is unverified** (a nonempty value for all 37 settlements is reported, not interpreted).
- **`term.matured` subjects were not identified** (the class lookup returned none).
- The matter-in-top-five count is an *end-of-run* reading of `questions_for`, not the ranking the chooser saw at each deliberation.
- Everything in §6 is a candidate: no lever was built or run, and RL2 would change an in-flight plan batch.
