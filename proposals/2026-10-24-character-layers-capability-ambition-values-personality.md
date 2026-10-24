# Capability, ambition, values and personality: four layers of a person, and what the seven axes become

## Status: PROPOSED (2026-10-24). HELD BACK: nothing here ratifies on merge, unless Jordan so rules. Reference under CLAUDE.md §0.05 — prose is not a mechanism.
## Lane: IN, with PC, SC, SE as sources. IDs: none allocated.
## Read at HEAD `d59acc9`
## Builds on: `engine/season/queries/world_q.py` (`questions_for`) · `engine/season/decision/choose.py`, `options.py` · `engine/season/data/cast.py`, `pursuits.py`, `fixtures.py` · `engine/season/rosters.yaml` (`tables.alignment`, `tables.pursuit_projection`) · `references/descriptor_registry.yaml` · `engine/season/goals.yaml` · `engine/season/loop/effects_combat.py` · `modules/combat/combatant.py` · `proposals/2026-09-16-conviction-decision-layer/adjudication_register.yaml` · `proposals/2026-09-18-character-decision-layer/PROPOSAL.md` · `proposals/2026-10-24-character-progression-adjudication.md` (PR #505, an input, not authority)

**How this was produced.** One producer drafted it, one read-only critic attacked the draft against the tree, and the orchestrator reconciled the two. The findings that survived are folded in below as corrections; the producer's draft and the critic's report are not kept (CLAUDE.md §0, the adversarial pass is a stage, not a deliverable). Marks: **[CHECKED]** opened at that line at HEAD while reconciling; **[READER]** taken from a document or from the critic or producer, not reopened; **[REASONED]** inference; **[MEASURED]** produced by a command named beside it. `.designs/` is quarantined and is not cited as authority.

---

## 1. The claim

A person has four layers, and one question tells each apart.

| layer | question | what it decides |
|---|---|---|
| **Capability** | does more always help the outcome, whoever holds it and whatever they want? | how a verb's outcome lands (the resolver only) |
| **Ambition** | could some state of the world satisfy it and end the wanting? | which content is on the person's plate (question formation) |
| **Values** | is it a direction nothing finishes, held as a weight? | which option the person prefers among the candidates a question offers |
| **Personality** | does it vary independently of values, leave odds untouched, and have no pole that always wins? | manner: the part of how a person acts that their values do not predict |

**The owner's question: are the pursuits values and the axes personality poles, or something else?** The answer is a split, decided by data.

- The fifteen **pursuits are values**. Four of the seven axes (`selfish_selfless`, `partisan_equitable`, `hierarchical_equal`, `precedent_substantive`) are readouts of those values: a manner space derived from ends.
- Three axes (`rigid_flexible`, `grandiose_humble`, `deontological_instrumental`) are **personality poles**. Each is a value-derived prior plus a stored per-person offset, and the offset is bounded by a spread measured on the authored cast (§4).
- As built, the registry names the poles as dispositions ("unwilling to deviate", "puts oneself forward") and computes them as values. The design keeps the computation for four axes and adds the offset for three.

**What this does not do.** It adds no per-verb cell and no new reader. It does not give personality to cohorts or to persons minted without pursuits (§8). It does not design vindictiveness, boldness or patience (§5): the first has no reachable reader, the other two have no reader at all.

---

## 2. What it overrides, narrows or conflicts with

| item | what the design does |
|---|---|
| ED-IN-0261, R7's dissolution clause: *"two people with identical pursuits ARE identically disposed and the variation comes from the candidates"* (`registers/editorial_ledger_in.jsonl:36` [READER: critic confirmed verbatim]) | **Overridden for three axes.** Persons with identical pursuits may differ on `rigid_flexible`, `grandiose_humble` and `deontological_instrumental`. The clause's own reason, that self/other lives in pursuit space, is kept; it is why `selfish_selfless` stays at spread 0. |
| ED-IN-0261, the deontology gate: *"the weighting is a threshold for certain actions"* (`engine/season/decision/options.py:426` [CHECKED]) | **Narrowed.** The gate stays and stays dormant (`refusal_axis` ships unset, `fixtures.py:749`). Its tolerance, when armed, becomes prior plus offset. The gate's own convention is a separate matter (§8). |
| Jordan 2026-09-17: *"these four are value-frames (what is right), the seven are bearing"* (`adjudication_register.yaml:200-201` [READER]) | **Narrowed.** Of the live seven, three are bearing in the sense that they can vary at fixed ends. |
| `bend_price` / `drift_rate` (`PROPOSAL.md:91-92` [READER]) | **Declined.** Neither has a reader. |
| **SE-06 / ED-IN-0296** (`workplans/valoria_master_workplan_v9_part6.md:90-94` [CHECKED]): cohorts hold no pursuits (246 of 638 season-1 acts score pursuit term 0, measured 2026-10-14/15) and a `needs_jordan` ruling would give them temperament rows | **Not pre-empted.** Cohorts read personality as 0 until that ruling is answered. The layer is named *personality*, not *temper* or *temperament*, because `temp.*` (`descriptor_registry.yaml:229` [CHECKED]) and SE-06's `temperaments:` already use the word. |
| R3, *"best design wins"* (`PROPOSAL.md:52` [READER]) | Invoked. Cost is stated in §4, not argued from. |
| R1/R2 (`Person.conviction` is the religious side; confliction derived), the scar model, `goals.yaml`, PR #505's attribute ceilings | Untouched. |

---

## 3. The four layers

### 3.0 Membership tests, asked in order (the first "yes" decides)

1. **Does more always help the verb's outcome, whoever holds it and whatever they want?** Capability.
2. **Could some state of the world satisfy it, so the wanting ends?** Ambition.
3. **Is it a direction nothing finishes, held as a weight?** A value. Then, for a manner quantity derived from values: *for a generic pursuit vector, can you name two coherent people with that vector at opposite poles?* If no, the axis spread is **0**: a value readout. If yes, but the disagreement is about a specific institution or state of affairs, the residue is an ambition (a commit) and the spread stays 0. If yes, and the disagreement is about the holder's own conduct, the spread is above 0: **personality**.
4. **Personality must also pass this: at every value it leaves outcome odds untouched, and no pole is better for its holder in every situation.** A trait where one pole always wins is a hidden capability (the "who bought balance" failure).

### 3.1 Capability: how a verb lands

- **Owns:** resolver operands. **Never owns:** a chooser term, question formation or a preference.
- **Carrier:** `Person.capability` (`engine/season/state/carriers.py:663` [READER]), plus `Person.body` for harm.
- **Writer:** only `train`, which declines unless the key is already held (`engine/season/loop/effects_combat.py:422-446` [CHECKED]).
- **Readers:** the contest pool. Only `tell` and `speak` map to a capability key; the combat seam derives only `end` from a person [READER: PR #505 §2].
- **Bound and scale:** PR #505's ceilings if adopted; this design adds nothing. Cohort: the same `Person` at `weight > 1`. Mass battle: the seam's derived `end`. Faction: none.

### 3.2 Ambition: which content

- **Owns:** which questions exist and which come first. **Never owns:** verb ranking or outcomes. The `goals.yaml` header says a goal *"never acts"* (`engine/season/goals.yaml` header [CHECKED]).
- **Carrier:** `commit` claims to OUGHT propositions in `Person.ledger`.
- **Writers:** world-gen goal minting (`goals.yaml`) and the `commit` verb.
- **Readers:** `questions_for`'s `need` source (`engine/season/queries/world_q.py:2717-2757` [CHECKED]: a live `commit` to an OUGHT generates a standing question every season), `claim_landed`, and five standing occasions (vacancies, seats named, writs, places named, larders).
- **Exit:** the proposition becomes true, or the commit is withdrawn.
- **Scale:** cohort: shared commits. Faction: organization goals minted as propositions. Mass battle: none; a war aim reaches the field only through a person choosing `march`.
- **Limit, stated.** The cut between ambition and values holds at the chooser, not at the authored row. A `goals.yaml` row carries an object (what) and a REQUIRED `pursuits:` lean (why), and its `stance:` seeds `Person.stance` (`goals.yaml` header lines 25-29; `harness/populated.py:711-718` [READER: critic]). The salience target is the organization's expected values plus the goal's lean (`world_q.py:2646-2647` [READER: critic]).

### 3.3 Values: what is worth wanting

- **Owns:** the fifteen weights and, through `to_axes`, the **prior** on all seven axes. **Never owns:** question formation or outcomes.
- **Carrier:** `Person.pursuits`. **Writers:** world build; consequence of a `determine` (`pursuit_shift=0.1`, shipped, `fixtures.py:433` [CHECKED]); the scar weight shift at threshold 2 (`scar_weight_shift`, `fixtures.py:721`, ships 0).
- **Readers:** the chooser's score through the axis vector; salience ordering; faction opinion; scar exposure through `pursuit_lean` (`person_q.py` lines named by the critic [READER]).
- **Every authored NPC holds all fifteen.** `data/cast.py:209-211` refuses a registry row that names fewer (*"every NPC must have a fully populated and coherent 15x7 pursuit-axis matrix"* [CHECKED]). All 46 registry rows therefore carry a full vector [MEASURED below]. Persons minted by `loop/census.py:106` carry none.

### 3.4 Personality: the stored deviation from what a person's values predict

- **Owns:** a per-person offset on three axes. **Never owns:** outcome odds, question formation, likeness to an organization (organizations have values, not personality), or any quantity that improves with use.
- **Carrier (proposed):** `Person.personality: dict`, keys drawn from three axis names. An absent key reads as offset 0, which is the control.
- **Writer:** world build only, following `thread_sensitivity` (`carriers.py:708-717` [READER]): no `write_matrix` row, so the gate refuses any write in play. Authored cast rows set it; the clamp in §4 binds authored values too.
- **Scale:** person: as here. Cohort and minted persons: read 0 (§8). Faction: none; a faction's conduct is its officers' personalities, choosing. Mass battle: `march` aligns −0.4 on `grandiose_humble` and +0.4 on `deontological_instrumental` (`tables.alignment` [CHECKED by loading]), so personality reaches the field through the commander's choice.

---

## 4. The seven axes and the fifteen values

- **Values: kept, all fifteen, unrenamed.**
- **Axes: kept, all seven, unrenamed.** The projected value stays the prior. For three axes it is joined by a stored offset.

| axis | spread (±) | test-3 verdict [REASONED] |
|---|---|---|
| `selfish_selfless` | 0 | entailed: self/other lives in pursuit space. Its alignment column has no nonzero cell over all verbs [READER: critic loaded `rosters.yaml:3321-3368`], so it is inert in the score today either way |
| `partisan_equitable` | 0 | entailed: justice +0.8 against family −0.6 and love −0.7 [CHECKED by loading `tables.pursuit_projection`] |
| `hierarchical_equal` | 0 | the residue at fixed ends (monarchist against republican) is a belief about a specific order, so a commit |
| `precedent_substantive` | 0 | as `hierarchical_equal`; the weakest call (§10, failure 1) |
| `rigid_flexible` | **0.15** | free: two honour-and-gain nobles, one unbending and one pliant, are both coherent |
| `grandiose_humble` | **0.15** | free: a vain priest and a meek one |
| `deontological_instrumental` | **0.15** | free: an honest merchant and a robber baron at identical wealth weight |

**The spreads are derived, not chosen.** The producer's draft set them at the half-range of each projection column (0.55, 0.45, 0.65). That swamps the prior: every authored NPC holds all fifteen pursuits, so its projected value on these columns is a near-zero blend. [MEASURED: `python3` over `engine.season.data.cast._rows()` through `cast.pursuits_of` and `pursuits.to_axes`, all 46 registry rows, 2026-10-24]

| axis | mean | sd | range | mean \|x\| |
|---|---|---|---|---|
| `rigid_flexible` | −0.19 | 0.12 | −0.44..0.17 | 0.20 |
| `grandiose_humble` | 0.14 | 0.11 | −0.16..0.40 | 0.15 |
| `deontological_instrumental` | −0.02 | 0.15 | −0.39..0.32 | 0.13 |

A uniform offset at ±0.55 has a typical magnitude near 0.3, two to three times the existing between-person spread of the prior. The offset would decide and the 45 projection cells (15 rows × 3 columns) would centre nothing. The rule adopted: **spread = one corpus standard deviation of the authored prior, rounded up to the next 0.05.** Offset is clamped to prior ± spread and to the projection column's range. With it, the prior and the offset have comparable weight, and the projection cells keep moving behaviour. The fraction (one standard deviation) is an [ASSUMPTION]; the three numbers are re-measured by the command above.

- **R7's consequence.** At fixed weights the four spread-0 axes are identical, as R7 requires. The three free axes vary by exactly the offset. R7 binds *projected* quantities, and the offset is not projected (`adjudication_register.yaml:242-249` [READER]).
- **Likeness readers read the prior over all seven columns, offset excluded.** `pursuits.py:98-106` takes the cosine over all seven axes, and `world_q.py:2652` and `person_q.py:532` call it (salience and faction opinion) [READER: critic]. Masking three columns would change attention order for every person at spread 0 and move the hash. Reading the prior over all seven keeps the control exact. An organization has values and no personality, so the offset has no business in the comparison.
- **Act readers read prior plus offset.** The chooser's pursuit term (`choose.py:125`, `:149`), regard from deeds judged, legitimacy, teller slant, reception and paired deeds all call `projected_axes`. Each dots the vector with a verb or deed alignment row [READER: critic confirmed all seven]. A deontologist condemns a killing more, because the `deed:person.died` row is +0.6 on `deontological_instrumental` [READER: critic].
- **Cost.** 0 projection cells deleted; 0 alignment cells added; 3 new data cells; 3 numbers per authored person (138 across 46 rows). One function changes: `projected_axes` becomes prior plus clamped offset, with a prior-only view for the likeness readers. The projection matrix stays 15×7; its three personality columns become priors, the centre a person's offset is clamped around. Those columns also stay the scar's exposure data, because `pursuit_lean` reads the unit projection.

---

## 5. The roster, and what is out

The minimum roster is the three axis offsets. Everything else was tested and is out, for the stated reason.

| candidate | verdict | reason |
|---|---|---|
| `forgiving_vindictive` | **out, dead reader** | The grudge row's referent is a *faction name*: `_eff_march` appends `(winner_faction, -1.0, grudge_w)` (`effects_combat.py:311-313` [CHECKED]). Both chooser arms read stance by `c.subject` (`choose.py:91-101` [CHECKED]), and question referents are persons, rungs, seats and records (`world_q.py:2217-2222` [READER: critic]). Under `declared` polarity `fight`'s subject is a person, so the negated regard never meets the faction row. A trait with no reachable reader is dead (ID-13). [UNVERIFIED by execution: no run shows a candidate whose subject is a faction id.] The writer (`field_grudge_weight`) and the gain (`stance_gain`) exist; the reach does not. Moving the grudge referent to a person is a separate ruling this design does not make. |
| boldness, patience | out | The chooser has no risk term and no timing term (`choose.py:130-151` [CHECKED]: pursuit + stance + urgency). Each would need a new per-verb column. |
| `stance_gain` | out | Signed, so it scales gratitude and loyalty too; it is not vindictiveness. |
| `choice_temperature` | out | Lower noise is always better for its holder, which fails test 4. |
| budget `k` | out | More always helps: capability-shaped. It already varies by office, body and travel. |
| `confliction_weight` | out | Ships 0, so the reader is dormant, and it scales a quantity already per-person (R1 intensities). |
| `scar_weight_shift`, `pursuit_shift` | out of the minimum | Both pass tests 3 and 4 as plasticity of values, but both share a meaning with `rigid_flexible`'s gloss, *"unwilling to deviate in the face of difficulties"* (`descriptor_registry.yaml:177` [CHECKED]). Two homes for one word is the defect to avoid. |
| candour, discretion, credulity, dogmatism (`intent_disclosure`, `telling_privacy`, `told_weight`, `refraction_gain`, `rank_gain`, `regard_gain`, `record_gain`) | not tested | The fixtures exist as global gains with readers (`options.py::teller_weight`). Whether each passes the tests was not examined. [GAP] |
| `Combatant.disp` | not mapped | A combat-local aggression lean (1-7, three hooks, both poles cost: `modules/combat/config.py:273-279` [CHECKED]), orthogonal to tradition. The season seam leaves it at its default. Mapping it to `grandiose_humble` is a guess; leaving it unmapped is two ladders for one trait family (§10, failure 3). |

---

## 6. Composition, and the worked example

**Order of evaluation, and where each layer enters.**

1. **Question formation.** `questions_for` builds questions from ambitions (`need`) and from claims landed.
2. **Attention order.** Ambitions enter at tier 0. Values enter as a salience cosine over the prior, all seven columns. The axis vector enters as deed valence.
3. **Opening set.** `opening_set` (`options.py:56`) forms the candidates. Eligibility is `own | remit | hold | presence`, never capability (`options.py:463-464` [CHECKED]). If the gate is armed, personality enters here as the tolerance.
4. **Score.** `pursuit` (prior plus offset against alignment) + `stance` + `urgency` (`choose.py:130-151` [CHECKED]). Urgency is constant across candidates.
5. **Budget.** The top `budget` candidates are kept. Budget reads office, body and travel only.
6. **Resolution.** Capability alone, through the contest pool.
7. **Feedback.** Witnesses judge the act through their own axis vectors. Scar accrues on values through `pursuit_lean` (projection only). `commit` mints new ambitions.

**Worked example.** Persons A, B and C hold identical pursuits `{honour: 0.5, wealth: 0.5}`. Today's projection is identical for all three (`project(A) == project(B)`; rigid −0.05, grandiose −0.20, deontological −0.05, partisan −0.35, hierarchical −0.35, precedent −0.20, selfish −0.20) [MEASURED]. Honour and wealth cancel on the means axes: R7 made visible. Offsets are ±0.15, the derived spread: A at 0, B at `+rigid +grandiose −deontological`, C at the reverse. Score is `Σ_axis w[axis] · align(verb, axis)`, over the live alignment cells [MEASURED: `python3` calling `engine.season.decision.options.project` and `engine.season.data.verbs.align`, 2026-10-24].

| verb | A (today's score) | B | C |
|---|---|---|---|
| comply | 0.205 | 0.070 | 0.340 |
| evade / defy | −0.450 | −0.555 | −0.345 |
| petition | 0.080 | 0.125 | 0.035 |
| forge | 0.135 | 0.015 | 0.255 |
| utter | 0.035 | 0.140 | −0.070 |
| challenge | 0.195 | 0.150 | 0.240 |

- **Rank, A:** comply > challenge > forge > petition > commit > construe > utter > evade.
- **Rank, B:** challenge > utter > petition > commit > comply > construe > forge > evade.
- **Rank, C:** comply > forge > challenge > construe > petition > commit > utter > evade.
- Today cannot separate A, B and C. The design does, at the derived spread, using only existing alignment cells. The candidate set is illustrative: `opening_set` was not run to show these verbs share one question. [GAP]

**Gate check, same script.** With `refusal_axis` set to `deontological_instrumental`, B's tolerance (prior −0.15) is −0.20 and C's (prior +0.15) is +0.10. The armed gate refuses `comply`, `evade / defy`, `forge` and `construe` at both. The same set at both poles shows the gate's convention (`options.py:446-460`, refuse any engaged verb whose alignment exceeds the tolerance) hardly discriminates at these magnitudes. The gate is dormant (§8).

---

## 7. Mapping the fourteen and the six

From-scratch fourteen: `proposals/2026-10-16-attributes-from-scratch_part4.md:34-35`. The six: PR #505.

| item | test result | layer |
|---|---|---|
| Bodily force, Quickness, Fine hand, Toughness | test 1 yes | capability |
| Watchfulness, Reading people, Reasoning, Presence, Thread perception | test 1 yes | capability. Watchfulness has no reader today: WITNESS rolls no capability |
| Composure | test 1 yes (steadiness under scrutiny) | capability |
| Forethought | split: execution (provision, audit) passes test 1; timing passes no test and has no reader | capability, plus [GAP] for timing |
| Constancy | fails test 1; test 3 says free | personality, as `rigid_flexible`'s offset; not a new trait |
| Warmth | split: caring is entailed by love, family and stewardship; being liked is others' stance | values and world state; nothing stored |
| Nerve | split: steadiness passes test 1; willingness to enter danger fails test 1 and has no reader (no risk term) | capability (steadiness); boldness excluded (§5) |
| #505's Body, Hand, Wit, Presence, Sense | test 1 yes | capability, as ceilings if adopted |
| #505's Nerve | as Nerve above | capability |

---

## 8. Limits the design states

1. **Ambition and values separate in the chooser, not in the authored row** (§3.2).
2. **Two ladders for one quantity.** `pursuit_shift` (shipped 0.1) drifts the prior half of an axis from the person's own `determine` acts (`person_q.py:615-629` [READER: critic]) while the offset half is frozen. Over many seasons, manner is a drifting term plus a frozen term with no shared rule. Nothing ratchets or converges; personality adds variety at time zero and no dynamics. Routing the offset through the scar shift's single owner would give it drift; this design does not.
3. **Cohorts and minted persons read 0.** Cohorts hold no pursuits (§2, SE-06). Persons minted by `census.py:106` hold none either. For a person with prior 0, an offset would be the whole manner vector with no values behind it: the layer order inverted. Personality applies only where values exist.
4. **The gate's convention is not this design's to settle.** The dormant gate refuses by `a > tolerance`. At a pole of ±0.7 (the producer's earlier spread) it would refuse `oblige`, `tie / knot`, `challenge` and `accept`: the honour pole refusing honour's own binding acts [READER: critic, `rosters.yaml:3486-3490`]. The derived spread of 0.15 shrinks that, and the convention is H-146's.
5. **Cohort and population scale.** A personality drawn for a corpus person is a representative member's, not an average [REASONED].

---

## 9. Falsifiers

- **Capability:** a capability key appears in `score_terms`, or a personality value changes a contest's odds.
- **Ambition:** a person with no live commit and no landed claim forms a question from values alone. Then values are forming content and the layer line is wrong.
- **Values and the four spread-0 axes:** a cast pair with near-identical pursuits whom the authors insist differ on `hierarchical_equal` or `precedent_substantive`, where no commit expresses the difference. The fix is one cell.
- **Personality:**
  - (a) at spread 0, `World.content_hash()` differs from today's for the same seed. Then the control is not a control. The likeness readers reading the prior over all seven columns is what keeps this true.
  - (b) at live spread, an n-seed `engine/season/harness/decision_spread.py --arms` comparison shows no decision moved. Then personality is inert. (`harness/arms.py` is `field_casualty_model`-only, CLAUDE.md §7, and is not the instrument.)
  - (c) one pole of a trait wins across the corpus on any outcome measure. The `deontological_instrumental` column carries 14 positive verbs (store- and body-moving) against 7 negative [READER: critic, `rosters.yaml:3474-3497`] and shares the largest spread, so it is the likeliest to show this. Then it is a hidden capability.

---

## 10. Failure modes and gaps

1. **`precedent_substantive` and `hierarchical_equal` are filed as spread 0 on a judgment.** `precedent_substantive` is glossed as a style of resolving (*"returns to previous ideas … forges new ones"*, `descriptor_registry.yaml:174` [CHECKED]), which reads like personality. If authors keep needing it to vary at fixed values, it is personality; the change is one cell.
2. **Stored poles expose alignment cells the blends hid.** Projected values sit near zero because blends cancel. Stored offsets, even at ±0.15, move scores by the amounts in §6. The instrumental pole carries `work`, `move`, `transfer` and `exchange` (+0.4 to +0.6 [READER: producer, loaded from `tables.alignment`]), so a strong deontologist under-chooses plain labour and trade. These are properties of the cells that personality makes visible, not defects it creates; they need reading before any spread above 0 is believed.
3. **Combat keeps a second personality.** `Combatant.disp` is a combat-local aggression lean. Leaving it unmapped means two ladders for the same trait family.
4. **The narrowed N-line.** Persons with identical pursuits already differ through `Person.conviction` (`religious_intensity` scales `doctrine` live, `person_q.py:744-767` [READER: critic]), stance rows, ledgers, scars and the Gumbel draw (`choose.py:350-390`). Personality is necessary only for the residual: manner independent of values at identical relations and knowledge, in the horizontal direction; no vertical producer exists. Elegance is argued by the cost in §4, whose denominator is 46 authored rows, a derived clamp and one function change. [CONFIDENCE: medium]

**[GAP]s.**
- Whether the example verbs share one real `opening_set`.
- Whether any question referent is ever a faction id (found none by construction; not executed).
- The draw distribution for corpus persons, and the spread fraction (one standard deviation).
- The 50-season behaviour is reasoned from shipped fixtures, not measured: no two-arm artifact exists in either direction.
- Candour, discretion, credulity and dogmatism were not tested (§5).
