# Attribute derivation — part 2: §4 what each verb requires, §5 what each subsystem requires

## Status: PROPOSED (2026-10-16). Not ratified. Merging it ratifies nothing unless Jordan so rules.
## Parts, in reading order: [head](2026-10-16-attribute-derivation.md) (head, §1–§3) · **this file** (§4–§5) · [`_part3`](2026-10-16-attribute-derivation_part3.md) (§6–§11).

Words, tiers, the abbreviated sources and the draw format are the head's. **A draw is written
`` `slug` (role, [reason key] basis: locator or reason) ``.** Its role is one of: odds,
difficulty/cost, eligibility, effect size, resists another. Its basis is NAMED Tn; NAMED T4,
overridden for dice by the kernel, the 2026-09-05 gloss or the T3 row; or INFERRED. Draws of one
aptitude sharing a reason key rest on one reason.

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

A design that names a **different act sharing the verb's word**, or the same act at **scene scale**,
is an analogue, and an analogue is INFERRED, not NAMED: #12's price (FW:413 Negotiate), #24's travel
leg (FW:239), #56's interrogation (FW:94).

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
| 8 | `determine` | graded | cognitive: `reasoning` (odds, [judge-weighs] INFERRED: a judge weighs the matter; SCV:133 says an expert judge "evaluates logical structure", a reading of the bench, not of the determiner's dice)<br>perceptual: `discernment` (odds, [ax7] INFERRED: crediting testimony (AX-7 competence)) | P02 | sigma pool (T3: `contests: "a proposition"`) | — |
| 9 | `dispatch` | choice | **none in the act**: choice-only (S10) | P09 | none (OFF) | an order given; no degree |
| 10 | `establish` | choice | **none in the act**: choice-only (S10) | P09 | none (OFF) | founds an office |
| 11 | `evade / defy` | choice | **none in the act**: choice-only (S10) | — | none | compliance withheld; no draw (M-FA-5 asks for one) |
| 12 | `exchange` | graded | cognitive: `numeracy` (effect size, [price] INFERRED: valuing what is exchanged)<br>perceptual: `reading-people` (effect size, [negotiate] INFERRED: M-SE-2 asks for a price; FW:413 Negotiate (Attunement) is the scene-scale analogue) | P10 | none | effect size (a price) has no reader yet |
| 13 | `forge` | graded | physical: `precision` (effect size, [forgery-quality] INFERRED: `Record.forgery_quality` is written and no source says what sets it); `dexterity` (effect size, [forge-hand] INFERRED: a forged hand or seal) | P11, P14, P08 | none (`forgery_quality` open) | — |
| 14 | `found` | choice | **none in the act**: choice-only (S10) | P09 | none | founds a rung |
| 15 | `build` | choice | **none in the act**: choice-only (S10) | P11, P19 | none | commissions a site; the labour is not the actor's |
| 16 | `give` | book | **no actor requirement**: bookkeeping | — | none | hands over a Record |
| 17 | `issue` | choice | **none in the act**: choice-only (S10) | P09 | none (OFF) | a dispensation |
| 18 | `fight` | graded | physical: `strength` (effect size, [combat-str] NAMED T2: impact, balance, health); `quickness` (odds, [combat-tempo] NAMED T2: tempo, initiative); `reflexes` (odds, [combat-reflex] NAMED T2: reflex); `balance` (odds, [combat-balance] NAMED T2: balance); `stamina` (difficulty/cost, [combat-stamina] NAMED T2: stamina); `toughness` (difficulty/cost, [combat-health] NAMED T2: wound interval, health)<br>cognitive: `concentration` (difficulty/cost, [combat-conc] NAMED T2: the Concentration tracker (consistency, mental fatigue, disruption, poise))<br>perceptual: `anticipation` (odds, [combat-reading] NAMED T2: reading, initiative)<br>volitional: `boldness` (odds, [combat-disp] NAMED T2: `disp`) | P03 | Combatant fields (T2, combatant.py:93-94); `end` from BODY (T1) | — |
| 19 | `challenge` | choice | **none in the act**: choice-only (S10) | P03 | none | issuing a challenge; boldness would bear on the CHOICE (S10) |
| 20 | `accept` | graded | physical: `strength` (effect size, [combat-str] NAMED T2: as fight); `quickness` (odds, [combat-tempo] NAMED T2: as fight); `reflexes` (odds, [combat-reflex] NAMED T2: as fight); `balance` (odds, [combat-balance] NAMED T2: as fight); `stamina` (difficulty/cost, [combat-stamina] NAMED T2: as fight); `toughness` (difficulty/cost, [combat-health] NAMED T2: as fight)<br>cognitive: `concentration` (difficulty/cost, [combat-conc] NAMED T2: as fight)<br>perceptual: `anticipation` (odds, [combat-reading] NAMED T2: as fight)<br>volitional: `boldness` (odds, [combat-disp] NAMED T2: as fight) | P03 | as `fight` | — |
| 21 | `requisition` | choice | **none in the act**: choice-only (S10) | P09 | none (OFF) | taking stores under a remit |
| 22 | `march` | graded | cognitive: `tactical-read` (odds, [command-cog] NAMED T2: Command's "tactical read" term (exchange.py:59-60); tactic execution (MB:312)); `judgment` (odds, [command-decisions] INFERRED: when to pursue, recall or commit (orchestration.py:2585-2590))<br>perceptual: `anticipation` (odds, [feint-roll] NAMED T2: feint recognition roll (orchestration.py:2593-2599)); `situational-awareness` (eligibility, [span] NAMED T2: span of control (engine.py:93))<br>social: `leadership` (eligibility, [command-cha] NAMED T2: Command (CHA 2 : ACU 1, exchange.py:57-66) → reform gate, morale start, span) | P04 | derive_command (T2, exchange.py:57-66) | — |
| 23 | `migrate` | choice | **none in the act**: choice-only (S10) | P15 | none (the migrant's `weight`) | a household move; travel demands are S09 |
| 24 | `move` | graded | physical: `hardiness` (difficulty/cost, [calamity-travel] INFERRED: FW:239's Endurance check per Calamity territory is the scene-scale analogue; the season `move` is a contain-path check (verb_table.yaml:720-727)); `stamina` (difficulty/cost, [long-leg] INFERRED: a long leg) | P15 | none | the season travel leg has no draw; FW §3.3 is its scene-scale form |
| 25 | `oblige` | choice | **none in the act**: choice-only (S10) | — | none | takes a duty |
| 26 | `open_case` | choice | **none in the act**: choice-only (S10) | P02 | none (OFF) | opens a docket |
| 27 | `petition` | graded | cognitive: `verbal-fluency` (effect size, [written-words] INFERRED: a written petition)<br>social: `persuasiveness` (effect size, [petition-granted] INFERRED: M-SC-2 names a receiver who may deny; a better petition is likelier granted) | P02 | none | no reader grades a petition today |
| 28 | `construe` | graded | cognitive: `reasoning` (effect size, [construe-text] INFERRED: "terms.distorted": reading a text against its intent)<br>social: `deception` (effect size, [distortion] INFERRED: a distortion others accept) | P02 | none | not resolvable |
| 29 | `release` | book | **no actor requirement**: bookkeeping | — | none | closes a tenure |
| 30 | `restore` | graded | physical: `dexterity` (effect size, [craft-hand] INFERRED: repair work); `stamina` (effect size, [repair] INFERRED: repair work) | P11 | none (`× f(degree)` open, H-164) | — |
| 31 | `revoke` | choice | **none in the act**: choice-only (S10) | P09 | none (OFF) | closes another's tenure |
| 32 | `speak` | graded | cognitive: `verbal-fluency` (odds, [spoken-words] INFERRED: speech)<br>social: `presence` (odds, [scv-crowd] NAMED T4, overridden for dice by the kernel: SCV:134 a crowd "responds to delivery and authority") | P02, P01 | open (T3 vs T3: contested or not) | if contested, the pool is `capability` (06_RESOLUTION.md:403, T4) |
| 33 | `succeed` | choice | **none in the act**: choice-only (S10) | — | none | designates an heir |
| 34 | `survey` | book | **no actor requirement**: bookkeeping | P07, P09 | none | mints a faction sheet equal to `faction_q.resolve`'s view at the moment of writing (verb_table.yaml:917-928): no degree can move it. The settlement *Survey* (governance_play_redesign_v1:87) is a different act sharing the word |
| 35 | `tell` | graded | cognitive: `verbal-fluency` (odds, [spoken-words] INFERRED: telling)<br>perceptual: `discernment` (resists another, [ax7] INFERRED: the HEARER's side: AX-7's competence (01_AXIOMS.md:288-289) governs how far a reading diverges)<br>social: `persuasiveness` (odds, [carry-hearer] INFERRED: carrying a hearer); `sincerity` (odds, [believed] INFERRED: being believed) | P01, P02 | sigma pool (T1: `copying`; the hearer's key ÷ 2 = Ob) | — |
| 36 | `examine` | graded | perceptual: `observation` (odds, [fw-examine] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:93, :301); `thread-sensitivity` (eligibility, [fw-ts-gate] NAMED T4: Buried if TS ≥ 10 (FW:301)) | P07 | none (T3: `capability` dice) | — |
| 37 | `interview` | graded | cognitive: `reasoning` (eligibility, [lattice-cog-gate] NAMED T4: intellectual approaches need Cognition ≥ 3 (investigation_systems_v30:254))<br>perceptual: `reading-people` (odds, [fw-interview] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:94, :302)<br>social: `empathy` (eligibility, [lattice-att-gate] NAMED T4: emotional approaches need Attunement ≥ 4 (investigation_systems_v30:255)); `persuasiveness` (eligibility, [fw-converse] NAMED T4: Buried opens at Disposition +3 (FW:302), which Converse, Charisma, raises (FW:409); the Interview roll was itself a Charisma pool (investigation_systems_v30:243), overridden for dice); `relational-depth` (eligibility, [fw-connect] NAMED T4: Buried opens at Disposition +3 (FW:302), which Connect, Bonds, raises (FW:410)) | P07 | none (T3: `capability` dice) | — |
| 38 | `research` | graded | cognitive: `memory` (odds, [fw-research] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:95, :303)<br>volitional: `patience` (odds, [archive-work] INFERRED: archive work) | P07, P13, P14 | none (T3: `capability` dice) | — |
| 39 | `surveil` | graded | physical: `stamina` (difficulty/cost, [fw-exertion] NAMED T4: Surveil is a roll "that require[s] physical exertion" (FW:80))<br>cognitive: `concentration` (odds, [surveil-time] INFERRED: "over extended time" (FW:304))<br>perceptual: `observation` (odds, [fw-surveil] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:304, Cognition) | P07, P18 | none (T3: `capability` dice) | — |
| 40 | `thread_read` | graded | perceptual: `thread-sensitivity` (eligibility, [k3-gate] NAMED T3: TS ≥ 30 (K-3; FW:305))<br>volitional: `will` (odds, [thread-read-pool] NAMED T4: Spirit × 2 (FW:305)) | P05, P07 | none (untyped; K-3 TS gate) | — |
| 41 | `reconstruct` | graded | cognitive: `inference` (odds, [fw-reconstruct] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:306 Reconstruct rolls Recall to "assemble … into a coherent picture") | P07, P13 | none (T3: `capability` dice) | — |
| 42 | `tie / knot` | graded | perceptual: `thread-sensitivity` (eligibility, [knot-ts-gate] NAMED T2: either party `ts ≥ 30`)<br>social: `relational-depth` (eligibility, [knot-bonds-gate] NAMED T2: `bonds ≥ 5`, cap `bonds // 2 + 1`)<br>volitional: `will` (odds, [knot-roll] NAMED T2: `spirit × 2`) | P06 | knot gate (T2, knots.py:185-222) | the row declares no `contests:` (V-2) |
| 43 | `transfer` | book | **no actor requirement**: bookkeeping | P10 | none | moves stores |
| 44 | `utter` | choice | **none in the act**: choice-only (S10) | P02 | none | brings a Proposition into being |
| 45 | `work` | graded | physical: `stamina` (effect size, [labour] INFERRED: labour (M-SE-5)); `strength` (effect size, [labour] INFERRED: labour) | P17, P11 | none (`× f(degree)` open, H-164) | — |
| 46 | `seize` | choice | **none in the act**: choice-only (S10) | P09 | none | a warrant, then a hold |
| 47 | `covenant` | choice | **none in the act**: choice-only (S10) | P09, P02 | none | terms have no reader |
| 48 | `sabotage` | graded | physical: `dexterity` (effect size, [sabotage-hand] INFERRED: damage done well and quietly)<br>volitional: `concentration` (odds, [hidden-steadiness] INFERRED: not being caught) | P18, P11 | none | — |
| 49 | `tend` | graded | physical: `dexterity` (effect size, [medicine-hand] INFERRED: how much body is raised)<br>perceptual: `observation` (effect size, [diagnosis] INFERRED: diagnosis) | P12 | none (writes `Person.body` up) | — |
| 50 | `argue` | graded | cognitive: `reasoning` (odds, [scv-judge] NAMED T4, overridden for dice by the kernel: SCV:133); `concentration` (difficulty/cost, [scv-conc] NAMED T4, overridden for dice by the kernel: SCV:267; :199; J-13 also puts a person's latitude in the pool only (v9 _part5.md:433))<br>perceptual: `reading-people` (odds, [scv-appraise] NAMED T4, overridden for dice by the kernel: SCV:135, :147)<br>social: `presence` (odds, [scv-crowd] NAMED T4, overridden for dice by the kernel: SCV:134) | P02 | sigma pool (T3) | — |
| 51 | `train` | graded | cognitive: `learning` (odds, [recall-spark] NAMED T4: Recall sets learning speed, "floor(Recall/2) bonus dice on all spark checks" (HIST:35)); `breadth` (eligibility, [equip-slots] NAMED T4: Recall sets equip slots (HIST:34, :521)); `practice-ceiling` (eligibility, [depth-ceiling] NAMED T4: Recall sets the "skill depth ceiling" (HIST:517), "per Recall cap per History" (:522))<br>volitional: `will` (odds, [spark-check] NAMED T4: the spark check is Spirit + floor(Recall/2) (HIST:41); thread Approach Training resolves on a Spirit pool (threadwork_v30:119)); `discipline` (effect size, [deliberate-practice] INFERRED: deliberate practice) | — | a writer of `capability`, not a reader | writes PRA; every P-id is its domain |
| 52 | `conceal` | graded | cognitive: `reasoning` (effect size, [fw-cover] NAMED T4: how well cover holds is Cover = Cognition + History, which "determines Exposure thresholds" (FW:575-577))<br>social: `presence` (eligibility, [fw-cover-identity] NAMED T4, overridden for dice by the T3 row: FW:620 cover identity, Charisma; the T3 `conceal` row has no roll) | P08 | none (T3: no roll) | — |
| 53 | `forgive` | choice | **none in the act**: choice-only (S10) | — | none | a stance change; values |
| 54 | `arrest` | graded | social: `presence` (odds, [arrest-authority] INFERRED: authority to make an arrest stick); `intimidation` (odds, [compel] INFERRED: compelling submission) | P02 | sigma pool (T3: `a standing`) | — |
| 55 | `pardon` | choice | **none in the act**: choice-only (S10) | P09 | none | releases a detention |
| 56 | `interrogate` | graded | perceptual: `reading-people` (odds, [fw-interview] INFERRED: the interview analogue (FW:94))<br>social: `intimidation` (odds, [compel] INFERRED: pressure); `persuasiveness` (odds, [draw-testimony] INFERRED: drawing testimony) | P02, P07 | sigma pool (T3: `a proposition`) | — |
| 57 | `raze` | choice | **none in the act**: choice-only (S10) | P04 | none | an order |
| 58 | `Leap` | graded | cognitive: `concentration` (eligibility, [ops-per-contact] NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, [ts-pool] NAMED T2: `ts // 10`)<br>volitional: `will` (odds, [thread-pool] NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, [coherence-cost] NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, [thread-fatigue] NAMED T4: threadwork_v30:195, :203) | P05 | thread pool (T2, operations.py:235-274) | — |
| 59 | `Weaving` | graded | cognitive: `concentration` (eligibility, [ops-per-contact] NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, [ts-pool] NAMED T2: `ts // 10`)<br>volitional: `will` (odds, [thread-pool] NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, [coherence-cost] NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, [thread-fatigue] NAMED T4: threadwork_v30:195, :203) | P05 | thread pool (T2, operations.py:235-274) | — |
| 60 | `Pulling` | graded | cognitive: `concentration` (eligibility, [ops-per-contact] NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, [ts-pool] NAMED T2: `ts // 10`)<br>volitional: `will` (odds, [thread-pool] NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, [coherence-cost] NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, [thread-fatigue] NAMED T4: threadwork_v30:195, :203) | P05 | thread pool (T2, operations.py:235-274) | — |
| 61 | `Past-pulling` | graded | cognitive: `concentration` (eligibility, [ops-per-contact] NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, [ts-pool] NAMED T2: `ts // 10`)<br>volitional: `will` (odds, [thread-pool] NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, [coherence-cost] NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, [thread-fatigue] NAMED T4: threadwork_v30:195, :203) | P05 | thread pool (T2, operations.py:235-274) | — |
| 62 | `Locking` | graded | cognitive: `concentration` (eligibility, [ops-per-contact] NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, [ts-pool] NAMED T2: `ts // 10`)<br>volitional: `will` (odds, [thread-pool] NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, [coherence-cost] NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, [thread-fatigue] NAMED T4: threadwork_v30:195, :203) | P05 | thread pool (T2, operations.py:235-274) | — |
| 63 | `Dissolution` | graded | cognitive: `concentration` (eligibility, [ops-per-contact] NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, [ts-pool] NAMED T2: `ts // 10`)<br>volitional: `will` (odds, [thread-pool] NAMED T2: `spirit × 2`); `self-coherence` (difficulty/cost, [coherence-cost] NAMED T2: `resilience` vs the Coherence cost (gain 0)); `contact-endurance` (eligibility, [thread-fatigue] NAMED T4: threadwork_v30:195, :203) | P05 | thread pool (T2, operations.py:235-274) | — |
| 64 | `Mending` | graded | cognitive: `concentration` (eligibility, [ops-per-contact] NAMED T4: threadwork_v30:199)<br>perceptual: `thread-sensitivity` (odds, [ts-pool] NAMED T2: `ts // 10`)<br>volitional: `will` (odds, [thread-pool] NAMED T2: `spirit × 2`); `contact-endurance` (eligibility, [thread-fatigue] NAMED T4: threadwork_v30:195, :203) | P05 | thread pool (T2); no RES (cost 0) | — |
| 65 | `levy` | choice | **none in the act**: choice-only (S10) | P04, P09 | none (OFF: `remit:dispatch`) | raising troops under a remit |

**Counts, by shape** (from the table): **34 graded, 24 choice, 7 book** = 65.

- **Bookkeeping, no actor requirement (7):** #1 `carry`, #6 `create_record`, #7 `destroy_record`, #16
  `give`, #29 `release`, #34 `survey`, #43 `transfer`. `survey` was graded in the first pass on the
  strength of the settlement *Survey* roll (governance_play_redesign_v1:87). That is a cadastral
  assessment that shares the word. The engine's `survey` mints a faction sheet equal to
  `faction_q.resolve`'s view (`engine/season/verb_table.yaml:917-928`), and no degree can move it.
- **Choice-only (24):** #2, #3, #4, #5, #9, #10, #11, #14, #15, #17, #19, #21, #23, #25, #26, #31, #33,
  #44, #46, #47, #53, #55, #57, #65.

**Against the template's matrix.** The template's matrix has 22 verbs reading at least one personal
input (its buckets 11 + 2 + 9). All 22 are *graded* here.

- **12 more rows are graded here, all scored 0 there:** #12 `exchange`, #13 `forge`, #24 `move`, #27
  `petition`, #28 `construe`, #30 `restore`, #32 `speak`, #45 `work`, #48 `sabotage`, #49 `tend`, #51
  `train` and #52 `conceal`.
- Of those 12, **three rest on a source**:
  - #51 `train`, NAMED at T4 (HIST:34-35, :41, :517, :522; threadwork_v30:119);
  - #52 `conceal`, NAMED at T4 for how well cover holds (FW:575-577), with the cover-identity roll
    overridden for dice by the T3 row (FW:620);
  - #32 `speak`, overridden for dice by the kernel (SCV:134).

  **The other nine are inferred.** #24 `move` is among them: FW:239 is a scene-scale travel check,
  and the season `move` is a contain-path check (`verb_table.yaml:720-727`). Three of the nine are the
  template's own **open** effect cells (#13 `forgery_quality`; #30 and #45 `× f(degree)`). #12's price
  is the SE lane's M-SE-2.
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
| S01 | personal combat | `strength` (effect size, [combat-str] NAMED T2: combatant.py:40-42; AUG:88); `quickness` (odds, [combat-tempo] NAMED T2: combat_systems.py:113, :1416-1421); `reflexes` (odds, [combat-reflex] NAMED T2: combat_systems.py:172; FW:106 initiative by Attunement (T4)); `balance` (odds, [combat-balance] NAMED T2: combat_systems.py:184-188); `stamina` (difficulty/cost, [combat-stamina] NAMED T2: combatant.py:45-47; Take a Breath restores (Endurance + History) × 2 (derived_stats_v30:110)); `toughness` (difficulty/cost, [combat-health] NAMED T2: combatant.py:30-42) | `concentration` (difficulty/cost, [combat-conc] NAMED T2: combatant.py:147; combat_systems.py:1423-1436, :1449-1452; wrapper.py:186, :427, :523) | `anticipation` (odds, [combat-reading] NAMED T2: combat_systems.py:171); `situational-awareness` (odds, [many-party] INFERRED: scenes with more than two people (M-PC-3)) | `boldness` (odds, [combat-disp] NAMED T2: combat_systems.py:181-183) | 9 / 0 / 1 | ED-901: the resolution pool is attribute-independent, `max(5, history + 6)` (core.py:54-56); aptitudes act through the per-beat channels, not the pool |
| S02 | mass battle (commander and troops) | `stamina` (difficulty/cost, [march] INFERRED: march attrition) | `tactical-read` (odds, [command-cog] NAMED T2: Command's "tactical read" term (exchange.py:59-60); tactic execution (MB:312)); `judgment` (odds, [command-decisions] INFERRED: pursuit and commit under uncertainty) | `anticipation` (odds, [feint-roll] NAMED T2: feint recognition (orchestration.py:2593-2599)); `situational-awareness` (eligibility, [span] NAMED T2: span of control (engine.py:93; MB:309)); `observation` (odds, [survey-damage] NAMED T4: Survey the damage, a Cognition check that "reveals exact casualties, territory infrastructure damage" (MB:926)) | `leadership` (eligibility, [command-cha] NAMED T2: Command, CHA primary (exchange.py:57-66; MB:306); troop Discipline starts at min(general's Command, ceiling) (MB:209-210) and Morale at Command + unit quality (MB:230)); `persuasiveness` (odds, [address-population] NAMED T4: Address the population, a Charisma check, "speech as governance" (MB:927)) | 6 / 0 / 2 | officers' practice gates troop types: "named officer with Cavalry History" (military_layer_v30:132-133) — practice, eligibility |
| S03 | social contest / proceedings | — | `reasoning` (odds, [scv-judge] NAMED T4, overridden for dice by the kernel: SCV:133); `memory` (odds, [scv-appraise-recall] NAMED T4, overridden for dice by the kernel: SCV:155); `concentration` (difficulty/cost, [scv-conc] NAMED T4, overridden for dice by the kernel: SCV:267; :199 Focus defence; J-13 also puts a person's latitude in the pool only (v9 _part5.md:433)); `verbal-fluency` (odds, [argument-words] INFERRED: speech kinds); `quick-thinking` (odds, [rebut] INFERRED: rebut) | `reading-people` (odds, [scv-appraise] NAMED T4, overridden for dice by the kernel: SCV:135, :147); `discernment` (resists another, [bench-reads] INFERRED: the bench reads what is said (M-SC-8)) | `presence` (odds, [scv-crowd] NAMED T4, overridden for dice by the kernel: SCV:134; Face_max = Cha × 3 (SCV:247), a view that moves no outcome (resolver.py:226-229)) | 0 / 5 / 3 | the T2 kernel binds only `faculty` (practice); every aptitude here is the superseded v30 design or inferred; J-13 bars the cost-side reading too (head §3 note 3) |
| S04 | fieldwork / inquiry | `stamina` (difficulty/cost, [fw-endurance] NAMED T4: FW:80, :92); `hardiness` (difficulty/cost, [calamity-travel] NAMED T4: FW:239) | `reasoning` (eligibility, [fw-explore-gate] NAMED T4: the Exploration depth gates, Cognition ≥ 2 / ≥ 3 (FW:84, :446), a gate and not dice; the Lattice's Cognition ≥ 3 (investigation_systems_v30:254)); `memory` (odds, [fw-research] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:95); `inference` (odds, [fw-reconstruct] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:306); `spatial-sense` (odds, [fw-pathfinding] NAMED T4: FW:90); `concentration` (odds, [surveil-time] INFERRED: Surveil) | `observation` (odds, [fw-examine] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:93); `reading-people` (odds, [fw-interview] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:94, :97); `thread-sensitivity` (eligibility, [fw-ts-gate] NAMED T4: FW:84 "hard … the epistemological barrier", :446-447) | `presence` (odds, [fw-impress] NAMED T4: FW:98, :100, :620); `relational-depth` (odds, [fw-connect] NAMED T4: FW:99); `sincerity` (odds, [sincerity-check] NAMED T4: FW:430); `persuasiveness` (odds, [fw-converse] NAMED T4: FW:409); `empathy` (eligibility, [lattice-att-gate] NAMED T4: investigation_systems_v30:255); `deception` (odds, [cover-identity-lie] INFERRED: holding a cover identity (FW:620); the roll is Charisma, the lie is unnamed); `will` (odds, [thread-read-pool] NAMED T4: thread_read (FW:96, :305)); `devotion` (odds, [inspiration] NAMED T4: spending Inspiration lowers any fieldwork Ob (FW:82); Inspiration is capped by Spirit, "Resolve / Inspiration cap" (derived_stats_v30:178, :557), and gained by Spirit checks (:191, :196)); `patience` (odds, [desperate-trail] INFERRED: Desperate Trail (FW:337-345)) | 12 / 4 / 3 | the five inquiry acts' attribute column is overridden for dice by the 2026-09-05 gloss (04_VERBS.md:473-476), which is contestable (head §3 note 1); gates are not dice and stay NAMED |
| S05 | threadwork | `toughness` (resists another, [dissolution-ob] NAMED T4: Dissolution on a person: Ob = target's Endurance + Spirit + armour (threadwork_v30:82)) | `concentration` (eligibility, [ops-per-contact] NAMED T4: threadwork_v30:199) | `thread-sensitivity` (odds, [ts-pool] NAMED T2: operations.py:235-247) | `will` (odds, [thread-pool] NAMED T2: operations.py:235-247; threadwork_v30:163; the wound-disruption check during contact rolls Spirit (:229)); `self-coherence` (difficulty/cost, [coherence-cost] NAMED T2: operations.py:249-274); `contact-endurance` (eligibility, [thread-fatigue] NAMED T4: threadwork_v30:195, :203); `relational-depth` (odds, [anchoring] NAMED T4: an Anchoring Scene with a Close Knot is a Bonds check, +1 Coherence (threadwork_v30:678, :707; knots_v30:149)) | 7 / 0 / 0 | the co-movement Dissonance check for non-sensitives rolls Spirit (`fieldwork_v30_infill.md:48`); its failure is not stated, so it is not coded as `steadfastness` or `self-coherence` |
| S06 | settlements / administration | — | `reasoning` (odds, [settle-cog] NAMED T4: settlement_layer_v30:560; governance_play_redesign_v1:87); `judgment` (odds, [hold-court] NAMED T4: Hold Court (governance_play_redesign_v1:64)); `numeracy` (odds, [ledger] INFERRED: Ledger, AP (AUG:147)); `planning` (odds, [works-over-seasons] INFERRED: works over seasons) | `reading-people` (odds, [administer] NAMED T4: settlement_layer_v30:563) | `presence` (odds, [pacify] NAMED T4: settlement_layer_v30:562; governance_play_redesign_v1:63); `leadership` (odds, [keep-order] INFERRED: keeping order); `patience` (odds, [slow-admin] INFERRED: administration) | 4 / 0 / 4 | the season loop runs settlement matter inline, no seam (rosters.yaml:1052, :1062-1067) |
| S07 | faction actions / governance / politics | — | `judgment` (odds, [faction-options] INFERRED: choosing among factional options); `learning` (effect size, [mentor] INFERRED: a rank's mentor gives "+1D on one specified roll per season" (faction_politics_v30:56)) | `reading-people` (odds, [allies] INFERRED: factional judgement of allies) | `presence` (odds, [standing-ladder] INFERRED: the Standing ladder (AUG:146, :148)); `persuasiveness` (odds, [votes] INFERRED: Mandate and votes (AUG:146)); `leadership` (odds, [faction-emergence] INFERRED: Standing 7 / faction emergence (AUG:148)); `steadfastness` (difficulty/cost, [reformation] NAMED T4: a caste-transgressive Conviction raises the witness Spirit check to Ob 2 (faction_politics_v30:741) and the Conviction Reformation resolves on a Spirit pool, Ob 3 (:752)) | 1 / 0 / 6 | AUG:152-155: positions "are not distinguished by aptitude — they are distinguished by practice, instruments, and office"; faction ranks demote on "skill or attribute drift" (faction_politics_v30:77) without naming one |
| S08 | economy / trade / craft | `dexterity` (effect size, [craft-hand] INFERRED: craft); `precision` (effect size, [craft-quality] INFERRED: craft quality); `stamina` (effect size, [labour] INFERRED: labour (M-SE-5)); `strength` (effect size, [labour] INFERRED: labour) | `numeracy` (odds, [price] INFERRED: price (M-SE-2)) | `reading-people` (odds, [negotiate] INFERRED: bargaining (FW:413 analogue)) | `patience` (effect size, [long-craft] INFERRED: craft and husbandry) | 0 / 0 / 7 | sources name practices only (HIST:241 Craft Expertise; :312 Haggler's Nerve); no aptitude is named |
| S09 | world / travel / survival | `stamina` (odds, [fw-endurance] NAMED T4: FW:92); `hardiness` (difficulty/cost, [calamity-travel] NAMED T4: FW:239; HIST:92, :178); `toughness` (difficulty/cost, [body-hazard] INFERRED: the body hazard (world_q.py:778-790) reads age only; a per-person rate would be this or hardiness) | `spatial-sense` (odds, [fw-pathfinding] NAMED T4: FW:90) | `land-sense` (odds, [seasons-reader] NAMED T4: HIST:314); `thread-sensitivity` (eligibility, [rendering-strain] NAMED T4: rendering strain by TS (FW:253-255)) | `self-coherence` (difficulty/cost, [depth4-coherence] NAMED T4: Coherence check at Depth 4 (FW:253)); `steadfastness` (difficulty/cost, [core-zone] NAMED T4: a non-practitioner in a Core zone makes a Spirit check, Ob 2, per round or loses Truth (southernmost_v30:105)) | 7 / 0 / 1 | illness and age ship dark (fixtures.py:542-544) |
| S10 | NPC / the chooser | — | `judgment` (odds, [temperature] INFERRED: the chooser's `choice_temperature` is one global knob (fixtures.py:251); a per-person temperature would be this aptitude) | `discernment` (resists another, [ax7] NAMED T3: AX-7: divergence turns on "the reader's competence" (01_AXIOMS.md:288-289); `refracted_confidence` holds it at 1 (H-200)) | `boldness` (odds, [temperament] INFERRED: temperament as a weight on challenge/fight candidates (combat `disp` is its only home)); `steadfastness` (difficulty/cost, [belief-integrity] NAMED T4: a recruited NPC defects when a "Belief integrity check" fails, a Spirit pool (npc_behavior_v30:1054); a witness to a Thread event rolls Spirit or has a Conviction shaken (conviction_track_v1.md:95)) | 2 / 0 / 2 | values (pursuits, convictions), stance and scar thresholds are not aptitudes: per-person scar thresholds would overwrite ruled constants (person_q.py:468-469) |

**What only the subsystem level surfaced.** Seven requirements appear only at this level. Each is an
aptitude in a role, or a source, that no practice domain or verb row carries:

- **`steadfastness`** (S07, S09, S10, all NAMED T4). Holding one's beliefs against shock is rolled on
  Spirit in three designs: a recruited NPC's *"Belief integrity check"* (`npc_behavior_v30:1054`), the
  witness check and the Conviction Reformation (`faction_politics_v30:741`, `:752`;
  `conviction_track_v1.md:95`), and the Core-zone exposure check (`southernmost_v30:105`). No verb
  and no practice domain carries it, because it is a defence the world and the faction layer call
  for, not an act.
- **`devotion`** (S04, NAMED T4). *"Resolve / Inspiration cap"*, Spirit × 1
  (`derived_stats_v30:557`), sets how much Inspiration a person can hold; spending it lowers any
  fieldwork Ob (FW:82).
- **Two first-pass rows are withdrawn.** `courage` (S02) and `discipline` as a troop quality (S02) each
  inferred a per-person quantity under a troop stat. MB names that quantity: troop Morale starts at
  the general's Command plus unit quality (MB:230), and Discipline at min(general's Command, ceiling)
  (MB:209-210). That is `leadership`, already drawn at S02. Discipline is a UNIT field
  (`units.py:553-557`).
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
- **`relational-depth` inside threadwork** (S05). An Anchoring Scene with a Close Knot is a Bonds
  check that restores Coherence (threadwork_v30:678, :707; `knots_v30.md:149`), so BON is drawn by
  the thread's recovery, not only by forming the knot.

**Subsystems that require almost nothing of the person.**

- **S07 (faction actions)**: every draw but one is INFERRED. AUG:152-155 says the position roles are
  *"distinguished by practice, instruments, and office"*. The faction ranks demote on *"skill or
  attribute drift"* (`faction_politics_v30.md:77`) without naming an attribute. The one NAMED draw is
  `steadfastness`: the faction layer tests conviction, not competence.
- **S08 (economy, trade, craft)**: every draw is INFERRED. Its sources name practices only (HIST:241,
  :312).
- **Judgment call:** what these two subsystems require of a person is mostly practice and office, not
  aptitude, with conviction as S07's one exception. That fits the template's finding that most verbs turn on *"remits, holdings and presence"*
  (`10_verbs_and_attributes.md:148-150`).
