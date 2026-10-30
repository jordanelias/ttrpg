# Resolution design — how debate and parliament come to change the world

## Status: **PROPOSED (2026-10-29), revised after two blind passes. Design only. Nothing here runs. No head, roster, verb row, arrangement row or code moves; no `ED`/`PP` is allocated; no `CURRENT.md` row moves.**
## Held back from ED-1094's merge default: **§9's Layer-1 hunks and the one canon question in §7 (titles).** Merging this file applies none of them.

> **What it answers.** The fit adjudication (`2026-10-29-debate-fit-adjudication.md`) said why persuasion and parliament cannot yet change the game. Jordan asked for a design that resolves *all* of it, by an agonist–antagonist method with top-down and bottom-up handshakes, then for a blind pessimistic review and a blind antagonistic NERS pass. This is the design after all of them.

---

## 0. How it was made, and what each stage did to the answer

| stage | who | what it changed |
|---|---|---|
| **A · attack the findings** | three critics (facts at the code · the shape against Layer 1 · the premises) | five "deciding facts" became nine root problems (§1) |
| **B · design twice, apart** | a top-down designer (purposes, NERS, Layer 1) and a bottom-up designer (the code, with a measured baseline); neither saw the other's work. Their files are kept as reference | twelve-link chain I1–I12 (§3) |
| **handshake** | the orchestrator joined them, settling each conflict by a stated rule | the first joined design |
| **C · attack the join** | three critics | the join broke in three places; milestone 1 was *not* "a full chain in the seeded realm" |
| **D · two blind passes** | a pessimist and a NERS antagonist, each blind to the authors' reasoning and to every earlier critic, each forming its own expectation from the repo's prior design and the historical research *before* opening this file | **this revision** — see §2 |

Rules used to settle each conflict: a ratified law is never relaxed to suit code (`CLAUDE.md` §0.05); a contract the code cannot meet is split into a milestone and the gap named; the smaller edit wins unless it fails a falsifier; anything that changes who holds power or overwrites a ratified ruling is Jordan's; a reader never lands without its producer in the same commit.

**The honest conclusion, before any detail:**

1. **The architecture holds; the seeded realm cannot exercise it.** The bottom-up baseline (`build_realm(0)`, two seasons) found every computed `utter` an empty Proposition (44 of 44), `commit` refused 63 of 63, nothing determined, and `give`, `oblige` and `comply` forming zero times. What this design delivers is a **proven mechanism**, not a played feature; played debate from the world needs a *motion source* that does not exist (J-11).
2. **A counted vote needs no declaring act.** Both blind passes, independently, found that the earlier design's new verb (`enact`) re-proposed exactly what `21_RECONCILIATION.md` C-7 / ED-SC-0034 rejected ("a `declare` verb, or a stored tally") and that it was a false N-line: a **licence on the ruler's own act** does everything it did and also checks the ruler. Jordan ruled for the licence. §3 I7–I9 are rebuilt on it.
3. **Compulsion is gone, deliberately.** A parliament in this design is a **consent body**: it licenses and blocks; it does not order. That fits H-90, canon's no-confidence enforcement, and the history (Cortes, Joyeuse Entrée, the Crown "granting" what parliament petitioned), and it removes three unproven links (`give` of a held writ, `evade / defy`, the writ itself). The cost is stated in §6.

---

## 1. The corrected problem register (condensed)

| | root problem | resolution |
|---|---|---|
| **R1** | The chooser scores the *verb*, never the Proposition's operands: argument and the voter's view of a motion are content-blind, and risk and horizon are the same missing reader | §3 I5, I6 |
| **R2** | Information does not reach members: no one but the utterer can `commit` on a Proposition; nobody can `oblige` to a seat nobody told them of; a sitting question sorts low and is answered only if it sorts first | §3 I3 |
| **R3** | Delivery and execution; as constrained, a parliament can restrain but not *cause* | §3 I7–I9 and §6: causes only through persons' own acts and opinion |
| **R4** | Motion identity and lifecycle: the docket names a *person*, so tallies are shared, re-tablings inherit commits, nothing ends | §3 I2 |
| **R5** | Body and bench: a council chair with `determine` judges every realm matter; the count includes the sentenced; joining reads as vassalage; the joiner's term is the chair's purse | §3 I4 |
| **R6** | Only `disposes` of 13 arrangement keys has a reader; a computed `open_case` names no arrangement (H-80) | §3 I2, §5 |
| **R7** | Constraint tension (only persons act + thresholds only raise questions + nothing stored) | resolved by naming the lawful causal path: licence, opinion, members' own acts |
| **R8** | Stability and the player: unclamped loops, no dominance table, nobody asked how a human takes part | §3 I12, §4 |
| **R9** | Verdict corrections (sortition, Nyaya's non-semantic faults, weighted votes computed when read dismissed too fast) | later steps; named |

Withdrawn: "no round on any record" (`Claim.round` exists; a season has five rounds); "a below-quorum vote is retried for ever" (today the quorum counts bench size and at the shipped value cannot refuse); `Act.via` is landed; "a duke is admitted because the seat's rung reaches his" (that clause was never built: anyone may join from anywhere, `predicates.py:396-399`).

---

## 2. What the blind passes did to the design

Neither reviewer knew what any earlier critic had found. They converged on the verb and diverged elsewhere; what each found is below with the change made.

| finding | by | change |
|---|---|---|
| **`enact` re-proposes the "declare verb" C-7/ED-SC-0034 rejected, and the design never cited either.** The licence idiom already exists (`confer` counts live commits inside a precondition; CR-36 and CR-37 schedule it) | both | `enact`, the writ, `writs_to_deliver`, `held_sourced: give`, the `evade / defy` re-type and the dispensation mint are **removed**. The count is a conjunct on the owner's own act (§3 I7–I9). The design now cites C-7 and ED-SC-0034 and is compatible with them: there is no declaring act |
| **The motion keyed on a *person* blocks that person's criminal trials and shields him from them** (a live motion makes its holder `docketed`; `open_case` declines anyone docketed) | both | a motion item is **person-less**: `{date, matter: None, motion, file}`; `docketed(person)` ignores motion items; one live motion per **subject** (the Proposition's), not per holder |
| **Only judges can table** (`open_case` is `remit:determine`; the chair holds none) | pessimist | tabling is **`carry`** of a petition Record naming the Proposition — seatless, built, and the existing route for a person without a seat |
| **The `council` rule sits at three sites, not one**: sworn `oblige` edges feed `purview_reaches`, `guard_weight` and `admits_audience` limb 3, and `imposed` is skipped at all three | NERS | the skip is placed at all three |
| **"`upkeep: 0` removes the purse lever" is false**: a joiner's `oblige` gets `Term(tick+4)`, renewed only by the seat-holder's transfer; seeded obligees get no term — two classes of member | NERS | stated as a **decision** (J-membership), default: a council join carries no term, as a data value |
| **The fourth `score_terms` summand hidden inside `stance_term` is concealment** | NERS | the placement is stated openly as a Layer-1 question (§7, J-layer1): amend `04 §F2` or read through `stance_term` and say so |
| **The lapse by CALENDAR is the route Layer 1 rejected** (`04_CODE_ARCHITECTURE.md:388`); a chair who never convenes produces no fired Date, so nothing is emitted | both | route (b): `term.matured` with a venue-reaching witness channel. A motion whose tabler dies is not live; its absence of an event is a **named gap**, not a hidden one |
| **Re-committing is free for loyalists, so "count only commits made after tabling" filters nothing; it also discards in-season debate although `Claim.round` exists** | NERS | stated as a limit. Count by **round** within the tabling season is the intended refinement (J-6), measured before adopted |
| **A "nay" is not an act, so two allied members carry any motion over a silent majority (rump rule).** The tree's own fixture is `quorum: 0.5` | pessimist | the threshold is a **share of the sworn membership**, not an absolute count; an absent or abstaining member is not an aye |
| **Recorded defeat (P16) is destroyed**: the loader says "a declared disposal's tally IS the finding" | pessimist | the lapse event **carries the state of the count** as a witnessed claim; no stored tally |
| **Drops prior safeguards**: the Parliamentary Stay, last-territory protection, abstention as a costed choice | pessimist | recorded in §5 as dropped from the prior design, not silently; last-territory protection fits as a **row of consent data** |
| **Membership frozen in computed play** (`oblige` forms only on a seat the person's ledger names) | pessimist | stated; seeded at build; later churn waits on probe P3 |
| **AX E.2.5's council governs a lord's holdings *in his stead*** — delegation, not an independent parliament | pessimist | the design uses E.2.5 for the **shape** (one seat, members by `oblige`) and no longer claims it settles a parliament's semantics |
| **The summons rides `_ch_chronicle`, a channel built on the refused echo model and scheduled for deletion** | pessimist | the contract is **channel-agnostic** ("some channel that forms reaches every member"); chronicle is the interim, with its declared successor named |
| **"Each fails a ratified rule" was circular** — B-10 was the same authors' earlier open question | pessimist | claim removed |
| **"Three critics independently found it" was one relay attacking one join** | pessimist | independence is claimed only for the two *blind* passes |
| **`goal_aim` "does not exist"** | pessimist | a misread: J-1 *lifts* `attention_key`'s `salience` closure into `person_q` under that name |

---

## 2A. WHAT WAS MEASURED (2026-10-29; seeds 0-2, four seasons, `build_realm`, the shipped chooser)

The first run of the whole design. It corrects four claims made earlier in this file and its sources. Harness: `probe_ext.py`, `probe_ext2.py` (outside the tree); nothing in the tree was changed.

| item | measured | what it settles |
|---|---|---|
| **Realm sittings** | 1, 1 and 3 Dates scheduled and fired in 4 seasons (seeds 0, 1, 2), **all at `terr_T13` or a settlement, convened by local lords' seats** (`off_npc_082`, `off_npc_052`, `off_npc_070`). **No realm-level sitting in 12 season-seeds**, though the King's seat holds `convene` | the King does not convene; nothing gives his chooser a reason. A realm parliament that never sits is a *producer gap*: the occasion must be stamped on the ruler's question (M2) |
| **Who learns a sitting is scheduled** | `date.scheduled` is held by **2 of 80**, **56 of 81** and **13 of 77** persons (seeds 0, 1, 2); `date.fired` first-hand by **0, 7 and 3**. The claim's subject is a Person, a Record or nothing, never the venue | answers B-9 / P2: the chronicle is **not** "everyone alive"; its reach varies from 2% to 69% by seed. **No channel in the tree reaches every member reliably.** §3 I3 is rewritten |
| **The King and the Regent** | after four seasons at seeds 0 and 2, `p_npc_020` still holds `off_npc_020` and `off_duke_valorsmark`, and `p_npc_032` still holds `off_npc_032` | answers P5: the earlier worry (H-230: the King dies in season 1 at seed 0) **does not reproduce in this tree**. A deposed king is possible |
| **`oblige` forms** | `duty.taken` 33, 43, 40 per four seasons; **33 and 38 persons sworn to one seat** (`off_npc_034` at seed 0, `off_npc_013` at seed 2) | answers P3's first half: joining a seat is live in computed play, not "frozen". It is also a **bandwagon**: one seat takes nearly every oath. Added as loop L7 |
| **`commit`** | `commitment.refused` 112-119 per run; `commitment.made` 0, 2, 3 | commits are chosen constantly and nearly all refused, so the vote's raw material barely exists |
| **`argue`** | 22-39 refused; **0 won or lost** | no debate occurs in the seeded realm; consistent with the earlier baseline |
| **Delivery** | `give.refused` 1-8, `record.given` 0-1, **`rung.ceded` 1 in seed 2**, `dispensation.issued` 12-20, `compliance.given`/`withheld` 0 | `give` of a rung forms *rarely, not never*; writs are issued often but never answered. With the writ removed (§3 I9) this no longer matters |
| **`petition` / `carry`** | 56-61 petitions and 62-66 `carry` acts resolved; 20-22 `petition.filed` | the petition route is **live** in computed play: the tabling route is not hypothetical |
| **Goal Propositions** | minted `OUGHT` (`populated.py:684`); `commit` has no per-pair refusal in its effect; only the once-per-season filter | re-committing is allowed, as the design assumed |

**Read from the code (no run needed):** `confer`'s precondition at `predicates.py:175` checks that the *holder* has any live `commit`, an existence test, **not a threshold count of other persons' commits**. The licence conjunct is therefore **not** an existing idiom; it needs the **cardinality widening ED-SC-0034 already accepted** for CR-34 (`21_RECONCILIATION.md` Part A.1: "the grammar widening is real", counted as a design change and taken). `_req_oblige` requires the seat to exist but **no holder** (clause 3 forbids only the actor holding it), so an unheld council seat is lawful. The three sites that skip an `imposed` oblige are `purview_reaches`, `guard_weight` and `admits_audience` limb 3 (confirmed). `petition`'s typed cell is `to` (Person) and `from` (Rung); `utter` is untyped, with a closed operand roster of eight (`actor, subject, from, to, site, kind, amount, floor`).

---

## 3. THE RESOLVED DESIGN, LINK BY LINK

Chain: **I1** world→topic · **I2** topic→room · **I3** summons · **I4** room→members · **I5** speech→hearer · **I6** hearer→vote · **I7** the count · **I8** count→licence · **I9** licence→owner's act · **I10** act→world · **I11** world→memory · **I12** stability. Labels: **[MATCH]** · **[EXTEND]** code grows · **[RELAX]** contract weakened · **[JORDAN]** · **[OPEN]**.

**I1 World → topic · [RELAX → M2].** *Contract:* a motion's operands come from the utterer's own claims, whose provenance ends at a world Event. *Supply:* every computed `utter` is empty; the only operand-bearing Propositions are the 21 seeded goal/creed rows. *Resolution:* milestone 1 takes a **goal row's typed fields** as the operands (subject a rung or office, value an organisation, plus a pursuit map). That is a worldly subject retrieved from the loop but *authored at world-build*, so **AP-1 is unmet in M1** and stated so. Tabling refuses a motion **already satisfied** (the seeded realm's one rung-goal, T13, is Varfell's own). M2 (J-11) is a **motion source**: a data roster of motion kinds, each naming a strain query, a predicate verb and an executing verb, refused at load without both, with `utter` binding `subject` and `value` from the question's two classed referents (a vacant seat and a candidate; an ungoverned place and a proposed holder). Whether an existing operand form can bind a second referent is **H-94**, settled by a spike, not argument. Magnitudes (40 vs 25 grain) stay out; named-object motions come first. A strain band raises a Question; it never produces the motion (T-b).

**I2 Topic → room · [EXTEND] + [RELAX].** A **motion is a petition Record naming a Proposition**, tabled by **`carry`** into the nearest open slot of a Date convened at a council's rung (any `convene`-holder there may call it; the council seat itself is unheld). The docket item is **person-less**: `{date, matter: None, motion: <Proposition id>, file: <the petition Record>}`, with `DOCKET_MOTION` and `DOCKET_FILE` each given a write-matrix row (the `TERM_KEY` precedent). Consequences, all removals of earlier problems: no `determine` party conjunct; no `hold_force` substitution; no coupling to where a holder stands; no shielding of a holder from trial; `docketed(person)` ignores motion items; **the decline of a second motion is keyed on the Proposition's subject**. Motion items fill only the slots of Dates convened at a council's rung; ordinary items skip those slots, so a judge's case never fills a council's slot (and never the reverse). `carry` today always appends a dateless item (B-4); routing it through `slot_for` for Dates at a council's rung is the one change to an existing act. **[RELAX]** several live motions about one subject (needs a typed Proposition-subject cell) are out.

**I3 Summons and attendance · [MATCH-with-EXTEND] + [RELAX].** *Contract:* some channel that forms in computed play reaches every member. *Measured (§2A):* `convene` is a `binding_decision`, so `_ch_chronicle` carries `date.scheduled`, but only **2%-69% of persons** hold the claim by seed and first-hand hearing of a firing reaches 0-7 persons. **No existing channel reaches every member reliably, and chronicle is built on the echo model R7 refused and is scheduled for deletion.** The design therefore does **not** rely on it: a member *who did not hear* is simply not asked, and that is the play: a council meets among those who heard, and the absent are a story (a faction that was not told). The contract stays channel-agnostic so the `<rung kind>` reach channel slots in when it exists. `sittings_before` widens to *the bench or the sworn, non-imposed members of the council seat at the Date's rung*, admitted by a `date.fired` claim on the firing tick **or a `date.scheduled` claim matched by Date id** landed before `due_at` (the claim's subject is the Date or the convener, never the venue); hearsay of a firing is still refused. The sitting question carries the motion as a referent and rides as a **stamped standing occasion** (a person answers one question per round and only if it sorts first; tier 4 below `need` means a person with any ambition never sees it). **[RELAX]** no per-member summons writ. **[OPEN]** distance costs no vote (`argue` needs co-presence; `commit` does not). **Not fixed, and a real failure mode of real assemblies:** a ruler (or any `convene`-holder at that rung) who never convenes produces no sitting and no event. The history calls this the Personal Rule; it is a story, and the pressure against it must come from outside the room (grievance, petition, supply), not from a rule.

**I4 Room → members · [EXTEND].** *One council seat per rung, members by their own `oblige`* (AX E.2.5, for its **shape** — one seat, many holders, membership a Query; that axiom's semantics are delegation, "govern in his stead", and this design does not claim it settles what a parliament is). A new `binds` basis **`council`** (*the joiner's act admits him; his oath brings the seat no ground*), with its rule at **all three sites** that read sworn edges — `purview_reaches`, `guard_weight`, `admits_audience` limb 3 — beside the `imposed` skip. The rule lands with the basis in `_req_oblige`; the `test_obligees.py` pin on `BINDS_BASES` moves in the same commit. The seat is **data** in `offices.yaml` with `obligees:` = the ladder title-holders inside the venue (CR-38's default; precedent NPC-070 on `off_npc_020`), which is how a member learns the seat exists (M-2). The seat grants **neither `determine` nor `convene`** and is **unheld**, so it judges nothing and convenes nothing: there is **no chair and no declarant**; a sitting is called by any `convene`-holder at the council's rung. The count (I7) is the only thing the room produces. **The joiner's term is a decision (J-membership):** a joiner's `oblige` otherwise gets `Term(tick+4)` renewed only by the seat-holder's `transfer` (an unheld seat has no purse, which is why the default below is no term), while seeded obligees get none; the default here is that a council join carries no term, as a data value. *Membership churns in computed play* (§2A: 33-43 `duty.taken` per four seasons) but **bandwagons onto one seat** (33-38 persons sworn to a single seat per seed), so a council in this engine would fill from whichever seat persons already know of. That is loop **L7** (below), measured not prevented; whether a duke ever learns a *new* council seat is the second half of probe P3 and is still unmeasured. An unheld council seat is lawful (`_req_oblige` requires no holder).

**I5 Speech → hearer · [EXTEND].** `argued_pursuits` gains `toward`: the argued goal's pursuit map **signed by the sign of the arguer's own motion term**, so a won argument moves only the pursuits the motion engages — toward it if he favours it, **away if he opposes**. A non-goal Proposition keeps today's behaviour. Clamp `consequence_pursuits` and the argue step to the authored range (loops L1, L2). *Not fixed:* everyone argues at pool 2 against 2 (no `argue` capability row; 1 of 430 persons holds any capability), so persuasive skill varies by seed, not by person; `speak` writes nothing (H-63). *Caution from the pessimist:* re-weighting values from one motion homogenises the council; the clamp and the signed step bound it, and probe P6 measures pursuit variance.

**I6 Hearer → vote · [RELAX] + [EXTEND].** The content reader is **one general function** of the motion's typed operands, the voter's own tenures and pursuits, and an odds fixture, computed inside `choose` and discarded: a **sign** — `aim` (pursuit alignment through the goal's typed `pursuits:`) and `stake` (+1 committed to the goal's organisation, −1 a holder of the object not so committed). It reads only static goal rows and the voter's own tenures (AX-2: decision code imports only `person_q`), so `seat_holders` referents give zero. **Placement is a Layer-1 question, stated openly (J-layer1):** a fourth `score_terms` summand amends `04 §F2`; carrying it inside `stance_term`'s arms (gain `1+g`) avoids the amendment but makes "stance" mean two quantities, which the NERS pass called concealment. Per-verb polarity: `commit +1`, `release −1`, `argue`/`speak` = the sign of the arguer's own term. A vote *against* is the absence of `commit` or a `release`; there is no separate "nay" act in the first slice (a contrary motion needs M2 operands). Social proof and the first defector are *forgone* (no term reads others' commits). Risk and horizon enter **only here**, but the first slice has no instance (`delay` is 0 or 1, so `h ≡ 1`), so **appetite and horizon (J-10) and AP-8 are deferred to M2**; where they come from is **[JORDAN]** (none of the seven axes carries either). *Disqualifier to watch:* where `stake = 0` the term reduces to the `aim` that `attention_key` already weighs; probe P6 checks and, if so, `aim` is dropped from the vote.

**I7 The count · [EXTEND] — one owner, two consumers.** The count is a **Query computed when read, stored nowhere**: the number of distinct **sworn, non-imposed members of the council seat** holding a live `commit` to `DOCKET_MOTION`, made after tabling, **as a share of the sworn membership** (fixture `quorum`, the tree's own is 0.5; swept {0.5, 0.6, 2/3}). An absent or abstaining member is not an aye, so a silent majority is not outvoted by an allied minority. It is the **single owner** of "how many support this" and has **two consumers**: CR-34's quorum conjunct on `determine` (for a bench of judges, unchanged and unrolled-back) and the licence conjunct below. Nothing declares, nothing rolls, nothing is minted, **no verb is added** — C-7's "the declaring act is `determine`" is untouched because for a licence **no declaring act exists**. *Counting by round within the tabling season* (using `Claim.round`) is the refinement J-6 measures; counting only commits made in a **later season** than tabling is the first-slice rule, and its weakness (re-committing is free for loyalists, so it filters nothing for them) is stated, not hidden. **The cardinality conjunct is not an existing idiom** (§2A: `confer` tests only that the holder has *a* commit): it is the grammar widening ED-SC-0034 accepted for CR-34, taken once and reused by both consumers.

**I8 Count → licence · [EXTEND].** The **data owner of consent** is a roster row: *(executing verb, object kind, council seat, threshold)*, refused at load if the verb or the seat is unknown — the answer to "where does the consent discriminator live" (B-11) that an effect body would be scripting drift. A row says *this verb on this kind of object is admitted only while the count for a motion naming this object clears the threshold*. Candidate rows: the Holy See's `revoke` of the throne (canon: the Parliamentary vote plus the Holy See), a ruler's `give` of a rung that is a holder's last territory (the prior design's last-territory protection, `parliamentary_transfer_v30.md`), `confer` of a nominated seat (CR-36), a levy. The conjunct reads **tenures** (commits), the same world read CR-34's quorum conjunct already makes — not another person's ledger (F8).

**I9 Licence → the owner's act · [MATCH] + [RELAX].** The owner's ordinary act (`confer`, `revoke`, `give`, `requisition`, `transfer`) carries the motion as a **typed operand chosen person-side** (the `terms_sourced` precedent); the conjunct refuses it without the count, emitting the verb's own refusal. **The licence checks the owner and the history agrees:** parliament petitions and the Crown grants; a ruler who ignores it is unmoved, but cannot do the licensed thing without it. **What this does not do, and the design does not pretend otherwise:** it cannot compel. A carried motion creates **no occasion** for the owner — he acts only if he wants to — and *announces nothing* until a lapse event or his act. Two consequences are accepted: (a) the strongest answer to "the outcome changes the world" is, in this design, *consent withheld or granted plus opinion*; (b) a motion that carried and was never acted on is visible only through the lapse event (I8's state-of-count claim) and through members' witnessed commits.

**I10 Act → world · [MATCH].** The world-changing acts all exist (`give`+Rung = `rung.ceded`; `confer`; `revoke`; `seize` licensed by `warrant_sourced`; `transfer`; `requisition`); no new gate basis, no assembly write. **Where a change happens that the owner did not choose**, it is **persons' own acts**: members committed to an OUGHT hold an ambition and may act on it with their own means — the commits *are* a faction (T-h) — so a parliament breeds coalitions, rivalries and, by the existing `issue` → `seize` machinery, enforcement by persons who hold the power to muster.

**I11 World → memory · [MATCH].** No stored tally or division record. `utter`/`commit`/`argue`/`carry` are heard by those present or by obligees; `convene` and the lapse are public. A vow-break (`release` ⇒ `commitment.ended`) is already priced.

**I12 Stability and the player · [EXTEND] + [OPEN].** Loops: L1 and L2 bounded by the clamps and the signed argue; L3 (herding) not built; L4 (always agrees) and L5 (capture by the seat-holder, by silence and by the joiner's term) **measured (P6), not prevented**; L6 (runaway) bounded because a re-tabling is a new Proposition with no inherited commits; **L7 (bandwagon: persons swear to the seat everyone already swore to) measured, not prevented**, since §2A saw 33-38 oaths on one seat. Scarcity: one slot per fired Date, one live motion per subject, `opportunity_key` bars a repeat. The human player's menu is the same Candidate list on the sitting question (`commit`/`release`, `argue` a present member, `speak`, `carry`, the owner's licensed act). **R-CHOICE dominance remains** (§4).

---

## 4. R-CHOICE AND WHAT A PLAYER SEES

**The dominant act at each seat is silence, and the design reduces it without removing it.** Proposer: not tabling (no seeded motion gains him anything). Opposer: abstain — free; the share-of-house threshold turns abstention into a quiet "no". Swing member: abstain or commit nearly free. Chair/convener: never convene — no Date, no lapse event, nothing to answer for (the Personal Rule). Owner: ignore the council. Whether abstention should cost (renewal by attending) is **J-membership**.

**What a player sees at a sitting:** the motion (the petition naming the Proposition), the commits he witnessed, the arguments he heard, and the arithmetic of his own holdings through `explain()`. **What he can say to a friend:** "it carried because enough of the council committed after it was tabled, so the King was allowed to do it." **What he cannot predict:** why an ally's earlier vow did not count (the post-tabling rule); whether a defeat will be announced (it depends on someone convening and on the lapse's reach). *Verdict (NERS antagonist): a partial pass on legibility.*

---

## 5. THE BUILD SEQUENCE (a mechanism slice)

Every step is a **hand-built falsifier first, a realm reading second**; every reader lands **with its producer in the same commit**. Hash: `build_realm(0)`, the 1- and 2-season pins and any golden reached; "EQUAL" is a claim to measure.

| step | lands | needs | hash | falsifier · control |
|---|---|---|---|---|
| **J-0a** | baseline to seeds 0-2; P5 (the King's/Regent's lifetime); P8 (`record.given` by kind, `rung.ceded`) — **no code** | — | — | numbers only |
| **J-1** | `goal_aim` — a **lift** of `attention_key`'s `salience` closure into `person_q`; one owner | — | EQUAL | content hash at 1 and 2 seasons equals the baseline |
| **J-2** | `binds: council`; the skip at **three** sites; the `_req_oblige` rule; the `test_obligees` pin; the council seat seeded with `obligees:`; the join-term data value | — | build MOVER | a King sworn to a duchy council leaves `purview_reaches`, `guard_weight` and `admits_audience` unchanged for him; the council seat grants no `determine`, so `may_determine` is False for every holder of it; control `binds: members_by_admission` restores today |
| **J-0b** | probes P2 (a member hears the scheduling/firing), P3 (a duke learns the seat) — **after J-2** | J-2 | — | decides computed vs hand-built for J-3..J-5 |
| **J-3** | person-less motion items; `DOCKET_MOTION`/`DOCKET_FILE` + matrix rows; `carry` routed through `slot_for` for Dates at a council's rung; `docketed(person)` ignores motion items; one live motion per subject; liveness (declared term, tabler alive); tabling refuses an already-satisfied motion | J-2 | MOVER where `carry`/`open_case` run | a motion about a duke does not block a criminal case against him, nor the reverse; two motions on one subject: the second declines; a judge's case never fills a council slot; a dead tabler's motion is not live |
| **J-4** | the lapse emission, route (b), carrying the state of the count | J-3 | MOVER | a lapsed motion leaves one event heard by a person present, naming the count; a motion acted on leaves none |
| **J-5** | `sittings_before` widened (members; `date.scheduled` by Date id); the motion as a referent and a stamped occasion | J-2, J-3 | MOVER | a member told `date.scheduled`, absent, is asked; one told nothing is not; **a member with an ambition still receives it** |
| **J-6** | the count Query (single owner); CR-34's quorum conjunct reads it; the by-round refinement measured | J-3, J-5 | EQUAL (no consumer yet fires) | quorum share: a minority of aye commits with a silent majority fails; **a commit made in the tabling season does not count**; same count, two seeds, same result |
| **J-7** | the consent data row and the licence conjunct on the owner's act; the typed motion operand | J-6 | MOVER | the licensed act is refused without the count and admitted with it; a count for a different object does not license it; control: a verb with no consent row is untouched |
| **J-8** | the content reader (placement per J-layer1); per-verb polarity; odds fixture; gain **0** | J-1 | EQUAL at 0 | two persons, equal pursuits, one holding the object outside the organisation, one committed to it: opposite `commit` ranking at gain 1, identical at 0; planted `stake = 0` reddens |
| **J-9** | content-sensitive `argue` (`toward`); the clamps; `motion_gain` set (declared mover) | J-6, J-8 | MOVER where a speech is won | three arms (no speech / won for / won against to the same members): commits move up / stay / down; an unrelated motion planted in the same sitting is unchanged; Partial/Failure move nothing |
| **J-10** | appetite and horizon fields (data) | J-8, CR-17 | MOVER | **deferred to M2** |
| **J-11** | the **motion source**: the motion-kind roster; `utter` binding `subject`/`value` from two classed referents (spike on H-94 first) | J-3, J-8, the spike | MOVER | a strain with no trigger forms nothing; a trigger with no strain forms nothing; both form one; a member whose reach omits the referent gets none |

**Removed from the earlier design:** the `enact` verb; the writ and its delivery; the `evade / defy` re-type; the dispensation mint; the chair holding `determine`; probe P7. **Not built, named:** contrary motions (a "nay" as a count); several live motions per subject; weighted votes (computed when read — a lawful later add); sortition as the convener's own act; speech-quality faults; `speak` writes; the Parliamentary Stay; a province rung in the authored realm.

---

## 6. WHAT EACH GOAL CAN DO, AND WHAT IT CANNOT

| | after the mechanism slice | after M2 |
|---|---|---|
| **(1) two characters debate a topic from the world** | on a hand-built world: a goal motion is tabled, two persons at the venue argue for and against, hearers move along the motion, members commit after tabling. **In the seeded realm this almost never fires** (9 of 9 `argue` refused; one `date.fired` in two seasons); the one executable goal motion is vacuous (already satisfied) | motions arise from strains (a vacant seat and a candidate; an ungoverned place and a proposed holder) |
| **(2) the result changes the world at the seam** | **consent, not command**: a count licenses or blocks the owner's own act; members' own acts and opinion change the world. A parliament that *checks the ruler* needs a consent row on his act (the throne's `revoke`, a last territory) — buildable here — but **a carried motion creates no occasion and the ruler may ignore it** | the same, with real motions to license |
| **(3) a parliament at four rungs** | one shape, a seat per rung seeded as data with title-holders as `obligees`; the realm first; rungs differ by containment and purview, not by branch. A province council needs a world that assembles a province | the same, with motions at each rung |
| **opinion change alone** | real: a speech moves the pursuits a motion engages, for or against; a motion that does not carry leaves a lapse event naming the count. Persons absent show no change | adds risk and horizon |

**What this design gave up for the licence, plainly:** it cannot make an unwilling ruler act. The strongest history supports that — assemblies petitioned and the Crown granted; where an assembly did compel, an executor with force (princes executing a Reichsacht, a king overriding at a *lit de justice*) did the compelling, and that is the members' own-acts path (I10), not a mechanism.

---

## 7. THE DECISIONS, RESOLVED BY THE REPO'S OWN RULE

`CLAUDE.md` §0: a decision is answered, in order, as *superseded*, *irrelevant*, *answered by a design document*, *answered by precedent*, or *what makes sense for the architecture*; only what survives all five is Jordan's. Each row below names the rung used. Every row is `[ASSUMPTION; medium; Jordan to correct]` with its revert.

**Decided by Jordan (2026-10-29):** the counted vote becomes an outcome by **licence by count**: no new verb, no declaring act, C-7/ED-SC-0034 untouched. This dissolves J-beta (an assembly writ), J-gamma (licensing a third person's `seize`) and J-delivery (reversing ED-IN-0292 (1)).

| decision | rung of the rule | taken | revert |
|---|---|---|---|
| **J-titles** | design document: Jordan's 2026-09-02 verbatim ruling (`offices.yaml:153-166`) | **canon stands**: realm king/queen, duchy duke/duchess, province count/countess, territory lord. "Marquis" is nowhere in canon and is **not adopted** | marquis/marquise at province and count at territory is one data edit to `titles.domains` that **overwrites the verbatim ruling**, a canon change only Jordan makes |
| **J-layer1 (a)** where the content reader sits | architecture ("amend openly or not at all", the NERS pass) | a **named fourth term `motion`** in `score_terms`, with the §F2 amendment drafted in §9 (H-1). Not hidden in `stance_term` | read through `stance_term`'s arms and document that "stance" then means two quantities |
| **J-layer1 (b)** risk and horizon as `Person` fields | superseded: Jordan ruled persons differ in risk appetite and in short/medium/long horizon (2026-10-29) | two fields on `Person`, `appetite` and `horizon`, authored per case in the cast with a **neutral default**, as `scar` and `conviction` are; the `§B.2` field list updated (§9, H-2) | omit; the term reads neutral |
| **J-layer1 (c)** a council oath bringing no purview | design document: the `binds` roster itself says "a second basis arrives with its rule in `_req_oblige`" (`predicates.py:376-382`, r2 `05` RULED (b)); AX E.2.5 does not define `binds` | the **`council`** basis, rule at the three sites (§9, H-3) | `members_by_admission` restores the vassalage reading |
| **J-appetite/horizon source** | precedent: `scar`, `conviction` and `thread_sensitivity` are authored in the cast | authored data, neutral default; the values are world content | none needed |
| **J-chair / convener** | precedent + measurement: local lords convene (§2A); the King's seat holds `convene` but no realm sitting occurs | **no chair**: the council seat is an unheld container (lawful); a sitting is convened by **any `convene`-holder whose seat's rung equals the council's rung**; the ruler may be sworn (a `council` oath brings him no purview) | author a Speaker and give the seat `convene` |
| **J-membership** | architecture: the design's stance is "measure loops, don't prevent them" (ID-16) | a council join carries **no term** (data value); abstention costs nothing now; bandwagon (L7) and always-agree (L4) are measured in P6 | `oblige_term` for council seats, or renewal by attending |
| **J-consent** (which acts need a count) | design document + precedent: canon names the throne's removal (the Parliamentary vote plus the Holy See, `worldbuilding_v30_infill.md:58`); CR-36 plans nomination; `parliamentary_transfer_v30.md:52` protects a last territory | **two rows to start**: the Holy See's `revoke` of the throne, and a ruler's `give` of a rung that is a holder's last territory. `confer` of a nominated seat stays CR-36's held-resolution licence | drop either row (data) |
| **J-quorum** | precedent: the loader test's own fixture is `quorum: 0.5` (`test_arrangements.py:186`) | share of the sworn membership, **0.5**, swept {0.5, 0.6, 2/3}; a defeat is **not** a recorded act (T-a); the lapse event carries the count | an absolute count |
| **D-lapse** | architecture: `04_CODE_ARCHITECTURE.md:388` rejects ending a term through CALENDAR | route (b): `term.matured` with a venue-reaching witness channel; a dead tabler's motion is not live and leaves no event (named gap) | route (a) |
| **H-94 spike** | answered by reading: the operand roster is closed at eight, and `to` and `amount` already exist | **no new operand name**: a motion binds `subject` (the vacant seat or rung), `to` (the proposed person, the known-person fan) and, later, `amount` (a quantity); needs `utter` typed and `_eff_utter` reading them | a new operand name (the ruling H-94 is waiting for) |
| **`aim` versus `attention_key`** | architecture: they rank different things (which *question* to attend vs whether to *back* a motion) | keep `aim` in the vote term; P6 checks and, if `stake = 0` makes it a duplicate, drops it | drop `aim` from the vote |

**What remains Jordan's, and only this:** (1) the **Layer-1 hunks in §9** apply on his merge, as earlier hunks did; (2) the **marquis** question, if he wants it to overturn his own verbatim ruling.

---

## 8. THE WEAKEST POINTS OF THIS DESIGN

1. **The licence cannot compel.** If Jordan's goal (2) is read as "the parliament orders", this is the wrong design; the earlier writ route did that and was cut for failing N, for needing three never-observed links, and for overturning C-7.
2. **The slice does not make the realm debate.** It makes a lawful mechanism that hand-built worlds exercise and the corpus can measure. Played debate waits on J-11 and the H-94 spike.
3. **The first-slice vote is crude.** It sees a sign over a goal row's object, not a quantity, and where `stake = 0` it may only duplicate salience. Free re-commits mean the post-tabling rule filters nothing for loyalists.
4. **Dominance by silence is reduced, not removed.** The lapse event makes some of it visible; the chair or ruler who never convenes leaves nothing.
5. **Membership bandwagons.** Joining is live but concentrates on one seat; a council may be one seat's court rather than a rung's parliament.
6. **No channel reliably reaches the members** (2%-69% hear a scheduling), and **the King never convenes** (no realm sitting in 12 season-seeds). Both are producer gaps for M2.
7. **Nothing here was run** beyond the bottom-up designer's baseline. Every hash, reach and formation claim is a prediction until its probe, and the two blind reviewers also ran nothing.

---

## 9. CLOSURE LEDGER, AND THE LAYER-1 HUNKS

**Every issue raised, by how it closes.** *Resolved* = settled in this design by decision, correction or measurement. *Build* = closes only when its step lands, with the falsifier named. Nothing is left as an unnamed open.

| issue | closes by | where |
|---|---|---|
| R1 content-blind argument and vote | **Build** J-8, J-9 (the reader, signed `argue`); `value` magnitude to M2 | §3 I5, I6 |
| R1 risk and horizon | **Resolved** (fields ruled, authored, neutral default) + **Build** J-10 | §7 |
| R2 no one but the utterer commits; seat unknown; sitting question ranks low | **Build** J-5 (members, stamped occasion); **Resolved** seat knowledge by seeding | §3 I3, I4 |
| R2 summons reach | **Resolved by measurement** (2%-69%; no channel reliable) and by design (the unaware are not asked) | §2A, §3 I3 |
| R3 a parliament can only restrain | **Resolved by decision**: consent, not command; licence by count; the rest is members' own acts | §3 I9, I10; §6 |
| R4 shared tally, inherited commits, shield from trial, no end | **Build** J-3, J-4, J-6 | §3 I2 |
| R5 chair leak, dice, vassalage, purse, count of the sentenced | **Resolved**: no chair holds `determine`, no declarant, `council` basis at three sites, no join term, imposed excluded | §3 I4, §7 |
| R6 unread keys, H-80 | **Resolved**: the council row reads `disposal: declared` and the quorum through the one count Query; other keys stay unread and are named | §3 I7 |
| R7 constraint tension | **Resolved**: named causal path | §0, §6 |
| R8 loops, dominance, the player | **Build** J-9 clamps; **measured** in P6 (L4, L5, L7); silence-dominance **named, not removed** | §3 I12, §4 |
| R9 verdict corrections | **Deferred, named** (sortition, weighted votes, non-semantic faults) | §5 |
| `enact` / C-7 regression | **Resolved**: removed | §2 |
| ED-IN-0292 (1), the writ, `evade / defy` | **Resolved**: removed from this design | §2 |
| recorded defeat (P16) | **Resolved**: the lapse event carries the count | §3 I8 |
| Parliamentary Stay, last-territory protection | **Stay deferred, named**; last-territory protection **taken as a consent row** | §5, §7 |
| a parliament that cannot check the King | **Resolved in shape** (consent row on the throne's `revoke`); **Build** J-7 | §3 I8 |
| the King / Regent dying early (H-230) | **Resolved by measurement**: alive after 4 seasons, seeds 0 and 2 | §2A |
| the King never convenes | **Named producer gap**; **Build** M2 (a stamped occasion on the ruler's question) | §2A, §8 |
| motion source (M2) and `utter` typing | **Build** J-11, narrowed to typing `utter` and reading `to`/`amount` | §3 I1, §7 |
| the licence's cardinality conjunct | **Build** J-6/J-7, on the grammar widening ED-SC-0034 already accepted | §2A, §3 I7 |
| AP-1 (operands from world events), AP-8 (risk/horizon) | **Stated unmet in M1**; M2 | §3 I1, I6 |
| `aim` vs `attention_key` duplication | **Resolved by rule**; P6 checks | §7 |
| everyone argues at pool 2 (no `argue` capability row) | **Named, not fixed**: data (capability values) | §3 I5 |
| hash movers and probes | **Build**: each step lists its hash and probe | §5 |

**Layer-1 hunks: drafted, not applied.** Layer 1 is ratified (ED-IN-0204); these change it and apply only when Jordan merges them, by the hunk mechanism earlier amendments used.

- **H-1 · `04_CODE_ARCHITECTURE.md` §F2.** *Today:* the chooser's score is the three-term sum, "the shape is ruled; only the weighting is open". *Proposed:* "...and, for a Candidate whose subject is a Proposition with typed operands, a fourth term `motion`: a sign read from the Proposition's operands against the chooser's own tenures and pursuits, weighted by a fixture gain. It reads only the actor's `PersonInterior` and the verb table's declarations (T-f). Gain 0 reproduces the three-term score."
- **H-2 · `§B.2` Person field list.** Add `appetite` (a small closed set, neutral default) and `horizon` (short / medium / long, Jordan's ruled bands, neutral default), person-owned (AX-4), written at world build; any later writer needs a write-matrix row.
- **H-3 · `§B.7` / `binds` roster.** Add `council` ("the joiner's act admits him; his oath brings the seat no ground") with its rule at `purview_reaches`, `guard_weight` and `admits_audience` limb 3, landing with the basis in `_req_oblige`.
