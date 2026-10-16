# Attribute derivation — part 2: §4 what each verb requires, §5 what each subsystem requires

## Status: PROPOSED (2026-10-16). Not ratified. Merging it ratifies nothing unless Jordan so rules.
## Parts, in reading order: [head](2026-10-16-attribute-derivation.md) (head, §1–§3) · **this file** (§4–§5) · [`_part3`](2026-10-16-attribute-derivation_part3.md) (§6–§10).

Words, tiers, the abbreviated sources and the draw format are the head's. **A draw is written
`` `slug` (role, basis: locator or reason) ``.** Its role is one of: odds, difficulty/cost,
eligibility, effect size, resists another. Its basis is NAMED Tn, NAMED T4 overridden for dice, or
INFERRED.

---

## 4. STAGE 2b: WHAT EACH VERB REQUIRES (all 65 rows of the template's master verb table)

**Fixed form, per verb.**

- **shape**: one of three.
  - ***graded***: the act has, or when complete would have, a draw, a degree, an obstacle, a gate or
    an effect size that a person's quality could move.
  - ***choice***: the act has no degree. Its quality is the choice itself, which the chooser makes
    from values, stance and held claims. Choosing well is one requirement, counted once, at S10.
  - ***book***: bookkeeping. A record or tenure move with no skill in it.
- **ACT**: what performing the act well requires of the actor, by family (physical, cognitive,
  perceptual, social, volitional). This is the only column counted as verb draws.
- **DOMAIN**: the practice domains the act draws. Their requirements are §3's, and are not
  re-counted here.
- **resolver already names**: what a T1/T2/T3 resolver or stub reads off a person today. These are the
  template's reads: the sigma pool, a `Combatant` field, `derive_command`, the knot gate, the thread
  pool.

**How a verb's requirement was decided.** A *graded* verb's ACT draws come from three places, in this
order:

1. what its resolver or stub names (T2/T3);
2. what a design names for the act (T4, or overridden);
3. failing both, what the act's outcome plainly turns on (INFERRED, with the reason in the cell).

No aptitude was added to a *choice* or *book* verb. Where an inference was tempting, such as
appointing well under `confer`, it is the chooser's question and sits at S10. **Rows 58–64 share one
resolver** (the thread pool), as do **rows 18 and 20** (one bout). §1's bracketed counts correct for
that.

| # | verb | shape | ACT: what doing it well requires of the actor | DOMAIN (P-ids, §3) | resolver already names | note |
|---|---|---|---|---|---|---|
| 1 | `carry` | book | **no actor requirement**: bookkeeping | — | none | moves a petition on the docket; procedural |
| 2 | `commit` | choice | **none in the act**: choice-only (S10) | — | none | an avowal; who commits is the chooser's question (values) |
| 3 | `comply` | choice | **none in the act**: choice-only (S10) | — | none | whether a person yields is `choose`'s question (10_verbs_and_attributes.md:166-167) |
| 4 | `confer` | choice | **none in the act**: choice-only (S10) | P09 | none (OFF: remit) | seating a holder; no degree |
| 5 | `convene` | choice | **none in the act**: choice-only (S10) | P02 | none (OFF: remit) | schedules a date |
| 6 | `create_record` | book | **no actor requirement**: bookkeeping | P14, P13 | none | writes a Record; literacy is the practice it presupposes [INFERRED] |
| 7 | `destroy_record` | book | **no actor requirement**: bookkeeping | — | none | presence and holding |
| 8 | `determine` | graded | cognitive: `reasoning` (odds, INFERRED: a judge weighs the matter; SCV:132 says an expert judge "evaluates logical structure", a reading of the bench, not of the determiner's dice)<br>perceptual: `discernment` (odds, INFERRED: crediting testimony (AX-7 competence)) | P02 | sigma pool (T3: `contests: "a proposition"`) | — |
| 9 | `dispatch` | choice | **none in the act**: choice-only (S10) | P09 | none (OFF) | an order given; no degree |
| 10 | `establish` | choice | **none in the act**: choice-only (S10) | P09 | none (OFF) | founds an office |
| 11 | `evade / defy` | choice | **none in the act**: choice-only (S10) | — | none | compliance withheld; no draw (M-FA-5 asks for one) |
| 12 | `exchange` | graded | cognitive: `numeracy` (effect size, INFERRED: valuing what is exchanged)<br>perceptual: `reading-people` (effect size, INFERRED: M-SE-2 asks for a price; FW:413 Negotiate (Attunement) is the scene-scale analogue) | P10 | none | effect size (a price) has no reader yet |
| 13 | `forge` | graded | physical: `precision` (effect size, INFERRED: `Record.forgery_quality` is written and no source says what sets it); `dexterity` (effect size, INFERRED: a forged hand or seal) | P11, P14, P08 | none (`forgery_quality` open) | — |
| 14 | `found` | choice | **none in the act**: choice-only (S10) | P09 | none | founds a rung |
| 15 | `build` | choice | **none in the act**: choice-only (S10) | P11, P19 | none | commissions a site; the labour is not the actor's |
| 16 | `give` | book | **no actor requirement**: bookkeeping | — | none | hands over a Record |
| 17 | `issue` | choice | **none in the act**: choice-only (S10) | P09 | none (OFF) | a dispensation |
| 18 | `fight` | graded | physical: `strength` (effect size, NAMED T2: impact, balance, health); `quickness` (odds, NAMED T2: tempo); `reflexes` (odds, NAMED T2: reflex, initiative); `balance` (odds, NAMED T2: balance); `stamina` (difficulty/cost, NAMED T2: stamina); `toughness` (difficulty/cost, NAMED T2: wound interval, health)<br>perceptual: `anticipation` (odds, NAMED T2: reading)<br>volitional: `composure` (difficulty/cost, NAMED T2: poise, disruption); `boldness` (odds, NAMED T2: `disp`) | P03 | Combatant fields (T2, combatant.py:93-94); `end` from BODY (T1) | — |
| 19 | `challenge` | choice | **none in the act**: choice-only (S10) | P03 | none | issuing a challenge; boldness would bear on the CHOICE (S10) |
| 20 | `accept` | graded | physical: `strength` (effect size, NAMED T2: as fight); `quickness` (odds, NAMED T2: as fight); `reflexes` (odds, NAMED T2: as fight); `balance` (odds, NAMED T2: as fight); `stamina` (difficulty/cost, NAMED T2: as fight); `toughness` (difficulty/cost, NAMED T2: as fight)<br>perceptual: `anticipation` (odds, NAMED T2: as fight)<br>volitional: `composure` (difficulty/cost, NAMED T2: as fight); `boldness` (odds, NAMED T2: as fight) | P03 | as `fight` | — |
| 21 | `requisition` | choice | **none in the act**: choice-only (S10) | P09 | none (OFF) | taking stores under a remit |
| 22 | `march` | graded | cognitive: `planning` (odds, INFERRED: tactic execution (MB:312)); `judgment` (odds, INFERRED: recall of a pursuit (orchestration.py:2589))<br>perceptual: `anticipation` (odds, NAMED T2: feint recognition roll (orchestration.py:2598)); `situational-awareness` (eligibility, NAMED T2: span of control (engine.py:93))<br>social: `leadership` (eligibility, NAMED T2: Command (CHA 2 : ACU 1) → reform gate, morale erosion, span) | P04 | derive_command (T2, exchange.py:57-66) | — |
| 23 | `migrate` | choice | **none in the act**: choice-only (S10) | P15 | none (the migrant's `weight`) | a household move; travel demands are S09 |
| 24 | `move` | graded | physical: `hardiness` (difficulty/cost, NAMED T4: Endurance check per Calamity territory crossed (FW:239)); `stamina` (difficulty/cost, INFERRED: a long leg) | P15 | none | the season travel leg has no draw; FW §3.3 is its scene-scale form |
| 25 | `oblige` | choice | **none in the act**: choice-only (S10) | — | none | takes a duty |
| 26 | `open_case` | choice | **none in the act**: choice-only (S10) | P02 | none (OFF) | opens a docket |
| 27 | `petition` | graded | cognitive: `verbal-fluency` (effect size, INFERRED: a written petition)<br>social: `persuasiveness` (effect size, INFERRED: M-SC-2 names a receiver who may deny; a better petition is likelier granted) | P02 | none | no reader grades a petition today |
| 28 | `construe` | graded | cognitive: `reasoning` (effect size, INFERRED: "terms.distorted": reading a text against its intent)<br>social: `deception` (effect size, INFERRED: a distortion others accept) | P02 | none | not resolvable |
| 29 | `release` | book | **no actor requirement**: bookkeeping | — | none | closes a tenure |
| 30 | `restore` | graded | physical: `dexterity` (effect size, INFERRED: repair work); `stamina` (effect size, INFERRED: repair work) | P11 | none (`× f(degree)` open, H-164) | — |
| 31 | `revoke` | choice | **none in the act**: choice-only (S10) | P09 | none (OFF) | closes another's tenure |
| 32 | `speak` | graded | cognitive: `verbal-fluency` (odds, INFERRED: speech)<br>social: `presence` (odds, NAMED T4, overridden for dice: SCV:134 a crowd "responds to delivery and authority"; superseded for dice by the kernel) | P02, P01 | open (T3 vs T3: contested or not) | if contested, the pool is `capability` (06_RESOLUTION.md:403, T4) |
| 33 | `succeed` | choice | **none in the act**: choice-only (S10) | — | none | designates an heir |
| 34 | `survey` | graded | cognitive: `reasoning` (effect size, NAMED T4: a settlement Survey rolls Cognition + Governance History (governance_play_redesign_v1:87); same word, a settlement assessment, so a near analogue)<br>perceptual: `observation` (effect size, INFERRED: what a survey records) | P07, P09 | none | — |
| 35 | `tell` | graded | cognitive: `verbal-fluency` (odds, INFERRED: telling)<br>perceptual: `discernment` (resists another, INFERRED: the HEARER's side: AX-7's competence (01_AXIOMS.md:288-289) governs how far a reading diverges)<br>social: `persuasiveness` (odds, INFERRED: carrying a hearer); `sincerity` (odds, INFERRED: being believed) | P01, P02 | sigma pool (T1: `copying`; the hearer's key ÷ 2 = Ob) | — |
| 36 | `examine` | graded | cognitive: `reasoning` (eligibility, NAMED T4, overridden for dice: FW:84 Cognition depth gate)<br>perceptual: `observation` (odds, NAMED T4, overridden for dice: FW:93, :301); `thread-sensitivity` (eligibility, NAMED T4: Buried if TS ≥ 10 (FW:301)) | P07 | none (T3: `capability` dice) | — |
| 37 | `interview` | graded | perceptual: `reading-people` (odds, NAMED T4, overridden for dice: FW:94, :302)<br>social: `empathy` (odds, INFERRED: getting a witness to Disposition +3); `persuasiveness` (odds, INFERRED: drawing an answer out (M-FI-6)) | P07 | none (T3: `capability` dice) | — |
| 38 | `research` | graded | cognitive: `memory` (odds, NAMED T4, overridden for dice: FW:95, :303)<br>volitional: `patience` (odds, INFERRED: archive work) | P07, P13, P14 | none (T3: `capability` dice) | — |
| 39 | `surveil` | graded | physical: `stamina` (difficulty/cost, NAMED T4: Surveil is a roll "that require[s] physical exertion" (FW:80))<br>cognitive: `concentration` (odds, INFERRED: "over extended time" (FW:304))<br>perceptual: `observation` (odds, NAMED T4, overridden for dice: FW:304) | P07, P18 | none (T3: `capability` dice) | — |
| 40 | `thread_read` | graded | perceptual: `thread-sensitivity` (eligibility, NAMED T3: TS ≥ 30 (K-3; FW:305))<br>volitional: `will` (odds, NAMED T4: Spirit × 2 (FW:305)) | P05, P07 | none (untyped; K-3 TS gate) | — |
| 41 | `reconstruct` | graded | cognitive: `inference` (odds, NAMED T4, overridden for dice: FW:306 "assemble … into a coherent picture"); `memory` (odds, NAMED T4, overridden for dice: FW:306 Recall) | P07, P13 | none (T3: `capability` dice) | — |
| 42 | `tie / knot` | graded | perceptual: `thread-sensitivity` (eligibility, NAMED T2: either party `ts ≥ 30`)<br>social: `relational-depth` (eligibility, NAMED T2: `bonds ≥ 5`, cap `bonds // 2 + 1`)<br>volitional: `will` (odds, NAMED T2: `spirit × 2`) | P06 | knot gate (T2, knots.py:185-222) | the row declares no `contests:` (V-2) |
| 43 | `transfer` | book | **no actor requirement**: bookkeeping | P10 | none | moves stores |
| 44 | `utter` | choice | **none in the act**: choice-only (S10) | P02 | none | brings a Proposition into being |
| 45 | `work` | graded | physical: `stamina` (effect size, INFERRED: labour (M-SE-5)); `strength` (effect size, INFERRED: labour) | P17, P11 | none (`× f(degree)` open, H-164) | — |
| 46 | `seize` | choice | **none in the act**: choice-only (S10) | P09 | none | a warrant, then a hold |
| 47 | `covenant` | choice | **none in the act**: choice-only (S10) | P09, P02 | none | terms have no reader |
| 48 | `sabotage` | graded | physical: `dexterity` (effect size, INFERRED: damage done well and quietly)<br>volitional: `composure` (odds, INFERRED: not being caught) | P18, P11 | none | — |
| 49 | `tend` | graded | physical: `dexterity` (effect size, INFERRED: how much body is raised)<br>perceptual: `observation` (effect size, INFERRED: diagnosis) | P12 | none (writes `Person.body` up) | — |
| 50 | `argue` | graded | cognitive: `reasoning` (odds, NAMED T4, overridden for dice: SCV:132); `concentration` (difficulty/cost, NAMED T4, overridden for dice: SCV:267)<br>perceptual: `reading-people` (odds, NAMED T4, overridden for dice: SCV:135)<br>social: `presence` (odds, NAMED T4, overridden for dice: SCV:134)<br>volitional: `composure` (difficulty/cost, NAMED T4, overridden for dice: SCV:199) | P02 | sigma pool (T3) | — |
| 51 | `train` | graded | cognitive: `learning` (effect size, NAMED T4: Recall sets learning speed (HIST:35); spark check Spirit + Recall/2 (HIST:41)); `breadth` (eligibility, NAMED T4: Recall sets equip slots (HIST:34, :521))<br>volitional: `discipline` (effect size, INFERRED: deliberate practice) | — | a writer of `capability`, not a reader | writes PRA; every P-id is its domain |
| 52 | `conceal` | graded | social: `presence` (eligibility, NAMED T4, overridden for dice: FW:620 cover identity, Charisma; T3 row has no roll); `deception` (effect size, INFERRED: how well the cover holds) | P08 | none (T3: no roll) | — |
| 53 | `forgive` | choice | **none in the act**: choice-only (S10) | — | none | a stance change; values |
| 54 | `arrest` | graded | social: `presence` (odds, INFERRED: authority to make an arrest stick); `intimidation` (odds, INFERRED: compelling submission) | P02 | sigma pool (T3: `a standing`) | — |
| 55 | `pardon` | choice | **none in the act**: choice-only (S10) | P09 | none | releases a detention |
| 56 | `interrogate` | graded | perceptual: `reading-people` (odds, INFERRED: the interview analogue (FW:94))<br>social: `intimidation` (odds, INFERRED: pressure); `persuasiveness` (odds, INFERRED: drawing testimony) | P02, P07 | sigma pool (T3: `a proposition`) | — |
| 57 | `raze` | choice | **none in the act**: choice-only (S10) | P04 | none | an order |
| 58 | `Leap` | graded | cognitive: `concentration` (eligibility, NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, NAMED T2: `ts // 10`)<br>volitional: `will` (odds, NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, NAMED T4: threadwork_v30:195) | P05 | thread pool (T2, operations.py:235-274) | — |
| 59 | `Weaving` | graded | cognitive: `concentration` (eligibility, NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, NAMED T2: `ts // 10`)<br>volitional: `will` (odds, NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, NAMED T4: threadwork_v30:195) | P05 | thread pool (T2, operations.py:235-274) | — |
| 60 | `Pulling` | graded | cognitive: `concentration` (eligibility, NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, NAMED T2: `ts // 10`)<br>volitional: `will` (odds, NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, NAMED T4: threadwork_v30:195) | P05 | thread pool (T2, operations.py:235-274) | — |
| 61 | `Past-pulling` | graded | cognitive: `concentration` (eligibility, NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, NAMED T2: `ts // 10`)<br>volitional: `will` (odds, NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, NAMED T4: threadwork_v30:195) | P05 | thread pool (T2, operations.py:235-274) | — |
| 62 | `Locking` | graded | cognitive: `concentration` (eligibility, NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, NAMED T2: `ts // 10`)<br>volitional: `will` (odds, NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, NAMED T4: threadwork_v30:195) | P05 | thread pool (T2, operations.py:235-274) | — |
| 63 | `Dissolution` | graded | cognitive: `concentration` (eligibility, NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, NAMED T2: `ts // 10`)<br>volitional: `will` (odds, NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, NAMED T4: threadwork_v30:195) | P05 | thread pool (T2, operations.py:235-274) | — |
| 64 | `Mending` | graded | cognitive: `concentration` (eligibility, NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, NAMED T2: `ts // 10`)<br>volitional: `will` (odds, NAMED T2: `spirit × 2`); `contact-endurance` (eligibility, NAMED T4: threadwork_v30:195) | P05 | thread pool (T2); no RES (cost 0) | — |
| 65 | `levy` | choice | **none in the act**: choice-only (S10) | P04, P09 | none (OFF: `remit:dispatch`) | raising troops under a remit |

**Counts, by shape** (from the table): **35 graded, 24 choice, 6 book** = 65.

- **Bookkeeping, no actor requirement (6):** #1 `carry`, #6 `create_record`, #7 `destroy_record`, #16
  `give`, #29 `release`, #43 `transfer`.
- **Choice-only (24):** #2, #3, #4, #5, #9, #10, #11, #14, #15, #17, #19, #21, #23, #25, #26, #31, #33,
  #44, #46, #47, #53, #55, #57, #65.

**Against the template's matrix.** The template's matrix has 22 verbs reading at least one personal
input (its buckets 11 + 2 + 9). All 22 are *graded* here.

- **13 more rows are graded here, all scored 0 there:** #12 `exchange`, #13 `forge`, #24 `move`, #27
  `petition`, #28 `construe`, #30 `restore`, #32 `speak`, #34 `survey`, #45 `work`, #48 `sabotage`, #49
  `tend`, #51 `train` and #52 `conceal`.
- Of those 13, **five rest on a source**: three NAMED at T4 (#24 FW:239, #34
  governance_play_redesign_v1:87, #51 HIST:34-35 and :41) and two overridden for dice (#32 SCV:134,
  #52 FW:620). **The other eight are inferred.** Three of the eight are the template's own **open**
  effect cells (#13 `forgery_quality`; #30 and #45 `× f(degree)`). #12's price is the SE lane's
  M-SE-2.
- **No disagreement in substance.** The template counts reads; this counts requirements. Every read the
  template counts is kept here in the *resolver* column.

---

## 5. STAGE 2c: WHAT EACH SUBSYSTEM REQUIRES

**The question per subsystem** (Jordan: *"WHAT does each verb/subsystem require"*): what does the
subsystem, as a design, require of the people who act in it? What makes one person better placed than
another to succeed, lead, survive, learn or be believed there? The sources are the subsystem's own
designs and stubs, tier-tagged. The pointers are each lane file's §0 and §8 under `research/by_lane/`
(T4); the missing-area rows cited are M-PC-3, M-MB-3, M-MB-16, M-SC-8, M-FI-3, M-FI-6, M-SE-2, M-SE-5,
M-WR-1 and M-NPC-12. **A subsystem row may name what no verb does**, and those are the reason for this
level.

| S | subsystem | (a) physical | (b) cognitive | (c) perceptual | (d) social / volitional | named / overridden / inferred | note |
|---|---|---|---|---|---|---|---|
| S01 | personal combat | `strength` (effect size, NAMED T2: combatant.py:39-40; AUG:88); `quickness` (odds, NAMED T2: combat_systems.py:113); `reflexes` (odds, NAMED T2: combat_systems.py:172; FW:106 initiative by Attunement (T4)); `balance` (odds, NAMED T2: combat_systems.py:188); `stamina` (difficulty/cost, NAMED T2: combatant.py:43-44); `toughness` (difficulty/cost, NAMED T2: combatant.py:30-40) | — | `anticipation` (odds, NAMED T2: combat_systems.py:171); `situational-awareness` (odds, INFERRED: scenes with more than two people (M-PC-3)) | `composure` (difficulty/cost, NAMED T2: combat_systems.py:1436, :1452); `boldness` (odds, NAMED T2: combat_systems.py:183) | 9 / 0 / 1 | ED-901: the resolution pool is attribute-independent, `max(5, history + 6)` (core.py:54-56); aptitudes act through the per-beat channels, not the pool |
| S02 | mass battle (commander and troops) | `stamina` (difficulty/cost, INFERRED: march attrition) | `planning` (odds, INFERRED: tactic execution (MB:312)); `judgment` (odds, INFERRED: pursuit and commit under uncertainty) | `anticipation` (odds, NAMED T2: feint recognition (orchestration.py:2598)); `situational-awareness` (eligibility, NAMED T2: span of control (engine.py:93; MB:309)) | `leadership` (eligibility, NAMED T2: Command, CHA primary (exchange.py:57-66; MB:306); morale start = Command (MB:230)); `discipline` (eligibility, NAMED T4: troop Discipline, "organisational integrity" (MB:209), a UNIT quality; per person, INFERRED); `courage` (difficulty/cost, INFERRED: troop Morale is the rout threshold (MB:230); per person, the aptitude under it) | 4 / 0 / 4 | officers' practice gates troop types: "named officer with Cavalry History" (military_layer_v30:132-133) — practice, eligibility |
| S03 | social contest / proceedings | — | `reasoning` (odds, NAMED T4, overridden for dice: SCV:132); `memory` (odds, NAMED T4, overridden for dice: SCV:155); `concentration` (difficulty/cost, NAMED T4, overridden for dice: SCV:267); `verbal-fluency` (odds, INFERRED: speech kinds); `quick-thinking` (odds, INFERRED: rebut) | `reading-people` (odds, NAMED T4, overridden for dice: SCV:135, :147); `discernment` (resists another, INFERRED: the bench reads what is said (M-SC-8)) | `presence` (odds, NAMED T4, overridden for dice: SCV:134; Face_max = Cha × 3 (SCV:247), a view that moves no outcome (resolver.py:226-229)); `empathy` (odds, NAMED T4, overridden for dice: SCV:147); `composure` (difficulty/cost, NAMED T4, overridden for dice: SCV:199) | 0 / 7 / 3 | the T2 kernel binds only `faculty` (practice); every aptitude here is the superseded v30 design (X) or inferred |
| S04 | fieldwork / inquiry | `stamina` (difficulty/cost, NAMED T4: FW:80, :92); `hardiness` (difficulty/cost, NAMED T4: FW:239) | `reasoning` (eligibility, NAMED T4, overridden for dice: FW:84, :446); `memory` (odds, NAMED T4, overridden for dice: FW:95); `inference` (odds, NAMED T4, overridden for dice: FW:306); `spatial-sense` (odds, NAMED T4: FW:90); `concentration` (odds, INFERRED: Surveil) | `observation` (odds, NAMED T4, overridden for dice: FW:93); `reading-people` (odds, NAMED T4, overridden for dice: FW:94, :97); `thread-sensitivity` (eligibility, NAMED T4: FW:84 "hard … the epistemological barrier", :446-447) | `presence` (odds, NAMED T4: FW:98, :100, :620); `relational-depth` (odds, NAMED T4: FW:99); `sincerity` (odds, NAMED T4: FW:430); `persuasiveness` (odds, NAMED T4: FW:409); `deception` (odds, INFERRED: cover and concealment (FW:573-620)); `will` (odds, NAMED T4: thread_read (FW:96, :305)); `composure` (difficulty/cost, INFERRED: exposure); `patience` (odds, INFERRED: Desperate Trail (FW:337-345)) | 9 / 5 / 4 | X = the five inquiry acts' attribute column, overridden for dice by the 2026-09-05 ruling as glossed (04_VERBS.md:473-476) |
| S05 | threadwork | `recovery` (difficulty/cost, NAMED T4: threadwork_v30:203); `toughness` (resists another, NAMED T4: Dissolution on a person: Ob = target's Endurance + Spirit + armour (threadwork_v30:82)) | `concentration` (eligibility, NAMED T4: threadwork_v30:199) | `thread-sensitivity` (odds, NAMED T2: operations.py:235-247) | `will` (odds, NAMED T2: operations.py:235-247; threadwork_v30:163); `self-coherence` (difficulty/cost, NAMED T2: operations.py:249-274); `contact-endurance` (eligibility, NAMED T4: threadwork_v30:195); `discipline` (eligibility, NAMED T4: HIST:293) | 8 / 0 / 0 | the wound-disruption check during contact rolls Spirit (threadwork_v30:229): will, already listed |
| S06 | settlements / administration | — | `reasoning` (odds, NAMED T4: settlement_layer_v30:560; governance_play_redesign_v1:87); `judgment` (odds, NAMED T4: Hold Court (governance_play_redesign_v1:64)); `numeracy` (odds, INFERRED: Ledger, AP (AUG:147)); `planning` (odds, INFERRED: works over seasons) | `reading-people` (odds, NAMED T4: settlement_layer_v30:563) | `presence` (odds, NAMED T4: settlement_layer_v30:562; governance_play_redesign_v1:63); `leadership` (odds, INFERRED: keeping order); `patience` (odds, INFERRED: administration) | 4 / 0 / 4 | the season loop runs settlement matter inline, no seam (rosters.yaml:1052, :1062-1067) |
| S07 | faction actions / governance / politics | — | `judgment` (odds, INFERRED: choosing among factional options); `learning` (effect size, INFERRED: a rank's mentor gives "+1D on one specified roll per season" (faction_politics_v30:56)) | `reading-people` (odds, INFERRED: factional judgement of allies) | `presence` (odds, INFERRED: the Standing ladder (AUG:146, :148)); `persuasiveness` (odds, INFERRED: Mandate and votes (AUG:146)); `leadership` (odds, INFERRED: Standing 7 / faction emergence (AUG:148)) | 0 / 0 / 6 | AUG:152-155: positions "are not distinguished by aptitude — they are distinguished by practice, instruments, and office"; faction ranks demote on "skill or attribute drift" (faction_politics_v30:77) without naming one |
| S08 | economy / trade / craft | `dexterity` (effect size, INFERRED: craft); `precision` (effect size, INFERRED: craft quality); `stamina` (effect size, INFERRED: labour (M-SE-5)); `strength` (effect size, INFERRED: labour) | `numeracy` (odds, INFERRED: price (M-SE-2)) | `reading-people` (odds, INFERRED: bargaining (FW:413 analogue)) | `patience` (effect size, INFERRED: craft and husbandry) | 0 / 0 / 7 | sources name practices only (HIST:241 Craft Expertise; :312 Haggler's Nerve); no aptitude is named |
| S09 | world / travel / survival | `stamina` (odds, NAMED T4: FW:92); `hardiness` (difficulty/cost, NAMED T4: FW:239; HIST:92, :178); `toughness` (difficulty/cost, INFERRED: the body hazard (world_q.py:771-790) reads age only; a per-person rate would be this or hardiness) | `spatial-sense` (odds, NAMED T4: FW:90) | `land-sense` (odds, NAMED T4: HIST:314); `thread-sensitivity` (eligibility, NAMED T4: rendering strain by TS (FW:253-255)) | `self-coherence` (difficulty/cost, NAMED T4: Coherence check at Depth 4 (FW:253)) | 6 / 0 / 1 | illness and age ship dark (fixtures.py:542-544) |
| S10 | NPC / the chooser | — | `judgment` (odds, INFERRED: the chooser's `choice_temperature` is one global knob (fixtures.py:251); a per-person temperature would be this aptitude) | `discernment` (resists another, NAMED T3: AX-7: divergence turns on "the reader's competence" (01_AXIOMS.md:288-289); `refracted_confidence` holds it at 1 (H-200)) | `boldness` (odds, INFERRED: temperament as a weight on challenge/fight candidates (combat `disp` is its only home)) | 1 / 0 / 2 | values (pursuits, convictions), stance and scar thresholds are not aptitudes: per-person scar thresholds would overwrite ruled constants (person_q.py:468-469) |

**What only the subsystem level surfaced.** Six requirements appear only at this level. Each is an
aptitude in a role, or a source, that no practice domain or verb row carries:

- **`courage`** (S02). Troop Morale is the rout threshold (MB:230). No verb names a per-person courage,
  because no verb fields a person as a soldier: a troop is a stock (the troop design's J-1 default) or
  a `weight`.
- **`discipline` as a troop quality** (S02, MB:209 *"organisational integrity"*). It is a UNIT field
  (`units.py:553-557`); per person it is inferred.
- **`judgment` at the chooser** (S10). `choice_temperature` is one global knob (`fixtures.py:251`). A
  per-person temperature is the only place in the tree where "judgment" could become a mechanism, and
  no source proposes it. **INFERRED.**
- **`discernment`** (S10, T3). AX-7 rules that a reading's divergence turns on *"the reader's
  competence"* (`architecture/meta/01_AXIOMS.md:288-289`). That is a T3 statement that a person-level
  aptitude exists, with its input **open** (the template's PD1b and J-T9). It is the one T3-named
  aptitude with no home among the nine.
- **`toughness` as a defence against the thread** (S05). Dissolution on a person sets *"Ob = target's
  Endurance + target's Spirit + armour"* (threadwork_v30:82): a *resists another* draw no verb row
  carries.
- **`self-coherence` outside threadwork** (S09). Rendering strain at Depth 4 is a *"Coherence check Ob
  1"* (FW:253), so RES is drawn by the world, not only by the operations.

**Subsystems that require almost nothing of the person.**

- **S07 (faction actions)**: every draw is INFERRED. AUG:152-155 says the position roles are
  *"distinguished by practice, instruments, and office"*. The faction ranks demote on *"skill or
  attribute drift"* (`faction_politics_v30.md:77`) without naming an attribute.
- **S08 (economy, trade, craft)**: every draw is INFERRED. Its sources name practices only (HIST:241,
  :312).
- **Judgment call:** what these two subsystems require of a person is mostly practice and office, not
  aptitude. That fits the template's finding that most verbs turn on *"remits, holdings and presence"*
  (`10_verbs_and_attributes.md:148-150`).
