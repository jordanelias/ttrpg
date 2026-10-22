# Tutorial: Fieldwork, investigation and the information model — how a person comes to know, hide, plant and spread what happened

Repo HEAD `a4ca9a5`. Paths are relative to `/home/user/ttrpg`. "Ctl" means the control run files
`scratchpad/ctl/realm_seed{0,1,2}_2seasons.txt` (seeds 0-2, two seasons). Every run column reads
**attempted/ok**:

- *attempted* counts acts that passed admission and reached the fold (`d.resolved`). Acts refused at
  admission are not counted.
- *ok* means at least one Event that is not a refusal. For a graded inquiry that means Partial or better.

"Probe" means a read-only script I ran for this tutorial (§9). Times are given as **ticks** (one tick per
season; the first MATTER runs at tick 0), not as "season N".

## 0 Before you start

**The frame.** The code has no player character and no GM. Every person is a chooser that spends a
**scene-action budget** each season on verbs from a closed table. The budget is
`max(1, 5 + 1 per live hold − body bands − 1 per travel leg)` (`decision/budget.py:19-20,57-61`), where a
*hold* is a Tenure (a stored relation edge) saying you have a seat, a landholding, a Record or a
Proposition.

- A scene of one act costs 1. A scene of up to `interactions_per_scene = 3` acts is "extended" and costs
  `extended_scene_cost = 2` (`fixtures.py:488-489`; `decision/choose.py:643-657`).
- The driver releases at most one scene per round, over 5 rounds (`loop/driver.py:456`).
- So budget 5 buys 2+2+1 = 7 acts, and budget 6 buys 9. Seed 0 shows about 7.6 acts per person per
  season (basis: 1,132 resolved acts / ~74 persons / 2 seasons).

"You" in this tutorial is the person acting: a player's character if one is ever seated, an NPC today.
So the tutorial teaches three things: what a person can do, what the rules do with it, and what a person
has to arrange to reach a goal.

**What this subsystem is.** Two layers that cannot be pulled apart:

1. **The information model (WITNESS).** Truth is one Event log. Belief is a per-person list of Claims
   (the *ledger*). Only the WITNESS barrier writes a ledger. Every subsystem's outcomes reach people
   this way and no other.
2. **Fieldwork (FI).** These are the verbs a person uses on that model on purpose: six *inquiries*
   (`examine`, `interview`, `research`, `surveil`, `thread_read`, `reconstruct`), the document makers
   (`survey`, `forge`, `conceal`, `create_record`), and the carriers `give` and `tell`.

**What you need from other subsystems.** The social-contest roller (`modules/social_contest/roll.py`)
grades three of the inquiries, and it also grades `tell`. Factions (`faction_q.resolve`) supply what a
survey or a forgery says. MATTER supplies decay and stage maturation, which is how covers lapse. The
decision layer (`questions_for`, `opening_set`) turns your claims into your next choices.

**Status, with grades** (the grade rule is the errata's G1):

| part | grade |
|---|---|
| WITNESS fan-out, refraction, decay, cap and eviction | RUNS-IN-LOOP |
| `co_located`, `chronicle` and `document_key` channels | RUNS-IN-LOOP |
| `witness_key` channel | TESTS-ONLY: it admitted nobody in seeds 0 or 2 (0 `firsthand_via_knot`) |
| `post_remit` slot (the obligee channel and IN-22 seat reports) | TESTS-ONLY at seed 0 (0 `inferred`). At seed 2 one `inferred` claim exists. With 0 found deposits, it must come from the channel (`witness.py:598`) or a seat report (`witness.py:513-524`), so this slot executes at seed 2. Which of the two I did not trace |
| the inquiry rolls, `survey`, `forge`, `conceal`, `create_record`, `tell` | RUNS-IN-LOOP |
| what an inquiry uncovers (the found deposit) | TESTS-ONLY: 0 found deposits in seeds 0 and 2 (probe) |
| `give` | 0 of 16 in seed 0; 1 of 19 in seed 2 (a cover changed hands) |
| told drift and private circles | Partial drift TESTS-ONLY in effect; circles are RUNS-IN-LOOP at control (`telling_privacy=0`) |
| `systems/fieldwork/sim/knots.py` | TESTS-ONLY (unplugged) |
| `destroy_record` | TESTS-ONLY. The row is typed and has an effect (`verb_table.yaml:292-313`; `effects_information.py:969`), so a hand-built act executes, but formation is withheld by fixture (`fixtures.py:923`) |
| `thread_read`, every proposed verb | DESIGN-ONLY |

`engine/season/requirements.yaml:169-172` lists the scale "investigations / detective / interactive
fiction" as `in_loop: false`. The verbs run, but there is no playable investigation mode.

## 1 The pieces

| term | what it is | numbers / limits | where it lives |
|---|---|---|---|
| Event, log | what happened (truth): kind, causes, changes, degree | append-only | `state/carriers.py:232` |
| Rung | a node of the containment tree: a place, a holding, or a person's own rung | — | `state/carriers.py` |
| Tenure | a stored relation edge (`hold`, `commit`, `oblige`, `knot`, …) with `since`/`until` | live while open | `state/carriers.py:77` |
| Proposition | an immutable uttered statement with a mood (default `OUGHT`); `utter` makes one | never edited | `carriers.py:849`; `effects_information.py:1001` |
| Office, purview, establishment | a seat; the places it reaches; the people attached to it (who the `post_remit` channel admits) | — | `epistemic.py:563-646` |
| stratum | a verb's resolution-order band (`social`, `uncontested_material`, `binding_decision`…); the `seen` term `stratum` reports it | — | `verb_table.yaml` per row |
| prize | what a contested verb is contested over (`tell`: "a standing"); inquiries have none | — | `verb_table.yaml:1186` |
| `with` | the typed relation "the other person stands where you stand" | — | `data/requires.py` (REQUIRES_STEMS) |
| Claim | one belief held by one person: `holder, subject, predicate, value, when, source, confidence, visibility, round, chain, doer` | `confidence` is an integer, default 100 | `state/carriers.py:291`; `data/fixtures.py:247` |
| ledger | `Person.ledger`, the person's list of Claims. Only WITNESS writes it | cap 200 | `data/fixtures.py:231` |
| event-kind claim | `(subject, e.kind, True)`: "this happened to/by subject" | subjects by `claim_subject_rule="both"` (the anchor plus each changed thing, minus a hidden actor) | `epistemic.py:185`; `fixtures.py:512` |
| `seen` claim | a Claim whose value is a `Seen(stratum, marks, who, why)`. `None` means the channel withheld that term | `who` = the act's actor; `marks` is always `()`; `why` is always `None` | `epistemic.py:874,901-932` |
| content claim | `content:<kind>`: what a Record you newly hold says, frozen | one per newly held Record | `loop/witness.py:68-83` |
| source | how the claim came to be held: `firsthand`, `told_by`, `inferred`, `firsthand_via_knot` | fixed by the channel | `rosters.yaml:419-434` |
| chain, hops, teller | who passed it on (origin first); `hops = len(chain)`, `teller = chain[-1]` | empty for anything that was not told | `state/carriers.py:337-379` |
| visibility, circle | `"own"`, or `(teller, addressee)` for a confided telling | circles form with probability `telling_privacy = 0.0` | `fixtures.py:853`; `witness.py:108-133` |
| witness channel | a rule deciding whether a person learns of an Event; precedence order `co_located, witness_key, document_key, chronicle, post_remit` | one channel per person per Event (the strongest one) | `rosters.yaml:419`; `epistemic.py:794-840` |
| remove | how far a channel is from seeing the thing | 0, 1/3, 2/3, 2/3, 1 | `decision/options.py:1338-1353` |
| refraction | received confidence = `int(conf·(1−g·remove)·(1−g·dissent)+0.5)` | `refraction_gain g = 0.5`; competence factor fixed at 1 | `options.py:1410-1448`; `fixtures.py:864` |
| dissent | 1 if the incoming claim contradicts your own firsthand claim about yourself or about a cell, or your ledger makes the reported act impossible for its actor | 0 or 1 | `options.py:1365-1407` |
| decay | MATTER takes 5 confidence off every claim each season, floored at 0 | `claim_decay_per_season = 5` | `loop/matter.py:317-347`; `fixtures.py:293` |
| eviction | while a ledger is over the cap, drop the claim with the lowest `confidence × (when+1)` | cap 200 | `state/ledgers.py:17-32` |
| Said | what a `tell` carries, copied from the teller's ledger when he chooses | best non-`seen` claim on the subject | `carriers.py:369`; `queries/person_q.py:909` |
| teller weight | weight given to hearsay when it is read: `told_weight^hops × relation × record`, clamped to [0,1] | `told_weight = 0.5`; `rank()` always 0 | `options.py:1513`; `fixtures.py:778` |
| Record | a world-side document: `kind`, `subject_matter`, `stages`, `forgery_quality` | kinds seen in the realm: `text`, `faction_sheet`, `cover`, `petition`, `dispensation` | `carriers.py:751` |
| hold | a `hold` Tenure: who has a Record. Each live hold also adds 1 to your scene budget | one live holder per Record | `effects_information.py:170-196`; `budget.py:57` |
| `_mint_document` | the one function that makes a Record and opens the maker's hold | 3 stages, one season apart (`record_stages_default=3`, `record_stage_term=1`) | `effects_information.py:170`; `fixtures.py:524-525` |
| faction sheet | a frozen snapshot of `faction_q.resolve`: `proposition, members, holdings, seats, head` | written by `survey` and `forge` | `effects_information.py:635,704` |
| `forgery_quality` | a forgery's grade; it is added to an inquiry's obstacle | `default_forgery_quality = 1`; the obstacle ceiling is 2 | `fixtures.py:419,439`; `roll.py:103-113` |
| cover | a `cover` Record whose `terms` names its maker. While it is live, your acts are *anchored* on the cover's id | live while a stage is unmatured, about 3 seasons | `effects_information.py:258`; `state/attribution.py:183-235` |
| anchor | what an Event is *about* (`anchor_of`): the actor, or his live cover | `seen.who` still reads the real actor | `attribution.py:105-150` |
| inquiry | the six verbs that write nothing to the world and emit `finding.made` or `finding.none` | 3 are graded (`research`, `examine`, `surveil`) | `verb_table.yaml:1321-1438`; `rosters.yaml:1115-1143` |
| degree, band | Overwhelming / Success / Partial / Failure, from `margin = net − Ob` | ≥3 / ≥1 / 0 to <1 / <0 | `engine/dice_engine/dice_engine.py:227-239` |
| `finding_terms` | which `Seen` terms a band uncovers | O and S: `[stratum, marks, who]`; P: `[stratum, marks]`; F: none | `rosters.yaml:2446-2472` |
| covert kind | a deed kind that leaves a findable *trail* | one member: `record.forged` | `rosters.yaml:2474-2489` |
| trail | `trail_of`: the most recent covert Event on the subject, if a person did it, it was not you, and you do not already hold it | at most one per kind per side | `epistemic.py:368-404` |
| `holds_trail` | "already known": you hold `(s, e.kind, True)` on a subject specific to the Event, made no earlier than the Event | any source counts | `epistemic.py:336-365` |
| found claim | what a finding deposits: source `inferred` (the `post_remit` slot), refracted at remove 1 | 100 → 50 | `witness.py:259-315` |
| `undeposited_kinds` | Event kinds that WITNESS gives to nobody | `finding.none` only | `rosters.yaml:1145` |
| Question | an item on your agenda for your next deliberation, raised by claims that landed since your last one | one question per deliberation | `queries/world_q.py:2249` |
| known-false veto | drops an option whose precondition your own ledger says is false | absence of a claim is UNKNOWN, never False | `options.py:308`; `epistemic.py:72-134` |
| knot (engine) | a `knot` Tenure that feeds the `witness_key` channel | its opener `tie / knot` cannot be resolved (H-182) | `epistemic.py:543-560` |
| knot (sim) | a separate bond model: tiers, strain, rupture | no season caller | `systems/fieldwork/sim/knots.py` |

## 2 How it works

This is the order in which an actor meets the rules.

**2.1 You act, and the act becomes an Event.** RESOLVE folds your act. It writes the world, or writes
nothing in the case of inquiries and `tell`, and emits Events. Nobody "observes" by choosing to.
Observation is computed afterwards.

**2.2 WITNESS decides who learns it** (barrier 4, once per round; `loop/driver.py:510`). Events of an
undeposited kind (`finding.none`) are dropped first (`witness.py:365`). For each remaining Event and
each person, the engine asks the channels in precedence order and takes the **first** one that admits
the person (`epistemic.py:794-840`):

| channel | admits | source | remove | `Seen` terms shown |
|---|---|---|---|---|
| `co_located` | anyone at the Event's place | firsthand | 0 | stratum, marks, who |
| `witness_key` | the anchor himself, or a live `knot` partner of the anchor | firsthand_via_knot | 1/3 | stratum, who |
| `document_key` | anyone holding an object the Event wrote | told_by | 2/3 | (none) |
| `chronicle` | **everyone**, if the Event's **kind** appears in the `emits:` of any `binding_decision`-stratum row | told_by | 2/3 | stratum |
| `post_remit` | the establishment of the seat the act was done through, within its purview | inferred | 1 | stratum |

(`rosters.yaml:419-425,1020-1025`; `epistemic.py:428-686`.)

`chronicle` is a **kind filter, not an act filter** (`epistemic.py:652-654,685-686`). Any Event whose
kind some `binding_decision` row emits goes to every person alive, whatever caused it:

- `determine` emits `pursuit.moved` (`verb_table.yaml:355`), so `argue`'s `pursuit.moved`
  (`verb_table.yaml:157`) is also realm-wide;
- MATTER's `tenure.closed` is broadcast too (round-2 audit, CROSS C5).

The consequence for play: matters of record, including some that are not governance acts, are public
across the whole realm. A private act whose kind no binding row shares is seen only by the people in
the room.

**2.3 What each admitted person receives** (`witness.py:590-972`):

- an **event-kind claim** for each subject;
- a **`seen` claim**, masked to the channel's terms;
- **observation claims** of cells (for example `stores:grain`), which go **only to the actor** at
  `observation_deposit_mode="actor"` (`fixtures.py:518`);
- **content**: if the Event made you the new holder of a Record, you get `content:<kind>` with what it
  says. "A held document is a held belief". The deposit carries no attribution, so a forged sheet and
  a genuine one land identically;
- **told content**, for `news.told` (2.5).

**2.4 Refraction.** Every copy except the actor's own is refracted once, at deposit (`witness.py:606`):

```
conf' = int( conf × (1 − 0.5·remove) × (1 − 0.5·dissent) + 0.5 )
```

| channel | from 100, no dissent | from 100, with dissent |
|---|---|---|
| co_located | 100 | 50 |
| witness_key | 83 | 42 |
| document_key / chronicle | 67 | 33 |
| post_remit, and found claims | 50 | 25 |

Refraction can only lower a confidence. The seed-0 realm shows confidences of 100, 95, 67 and 62. 67 is
the chronicle copy, and 62 is that copy after one decay (67 − 5).

**2.5 Telling.** `tell` needs a claim on the subject in your own ledger, and the hearer must be `with`
you, at the same place (`verb_table.yaml:1169-1192`). It is contested over "a standing". On O, S or P
the result is `news.told`; on Failure it is `news.untold`. Each hearer gets a copy of your `Said`:

- source `told_by`, with **your** confidence, `chain = your chain + (you,)`, refracted by the channel
  that admitted the hearer (`co_located` for the hearer you addressed, so ×1);
- **dedup**: the copy is skipped if the hearer already holds the same subject, predicate and value
  with an empty chain or the same origin (`witness.py:932-935`);
- **drift at Partial only** (`witness.py:136-231`): a hash, not a die, selects either one dropped
  addressee from a document's `to` list, or a plain number moved by `1 + sel % ceil(0.5·|v|)`, keeping
  its sign. Event-kind `True` values and `Seen` values pass through verbatim;
- **circles**: with probability `telling_privacy` (0.0) the copy is held "in confidence". Retelling it
  outside the circle emits `confidence.broken`. At shipped values this never happens.

When a told claim is *read*, it weighs `0.5^hops × relation × record` (`options.py:1513-1545`): 0.5
for one hop, 0.25 for two. `ledger_weigh` returns `None` (plain reading) for a ledger with no chained
claim (`options.py:1356-1362`).

**2.6 Fading and forgetting.** MATTER, once per season, takes 5 off every claim's confidence and emits
`claim.decayed` (`matter.py:317-347`). Over the cap of 200, WITNESS evicts the lowest
`confidence × (when + 1)` (`ledgers.py:17-32`). A 100-confidence claim from tick 0 scores 100, and a
50 from tick 2 scores 150, so **old firsthand knowledge is forgotten before fresh hearsay**. Nobody
can witness a forgetting, and nothing "unsays" a claim.

**2.7 How beliefs drive choice.** The chooser sees your ledger, never the World. Claims that landed
since your last deliberation raise **Questions** about subjects within your reach
(`world_q.py:2249`), and `opening_set` forms candidates on the question's referents. Your ledger also
vetoes options it makes known-false (`options.py:308`) and supplies names and operands. News sets the
agenda; beliefs do not create preferences.

**2.8 Inquiries.** An inquiry writes nothing to the world. The three graded rows roll through
`social_contest.roll` (`rosters.yaml:1115-1143`):

- pool = `pool_default = 2`, for everyone. **The reason is structural, not data.** `VERB_CAPABILITY`
  maps only `tell` and `speak` (to `copying`; `rosters.yaml:1228-1231`), and `_capability` returns
  `None` for an unmapped verb (`seam/wrappers/sigma.py:113-116,130-131`). Writing a person's capability
  would therefore not change any inquiry pool. (Capability is also empty on every realm person; ctl
  "capability nonempty 0".)
- Ob = `obstacle_default = 2`, plus the Record's `forgery_quality`, then capped at
  `obstacle_ceiling = 2` (`roll.py:103-113`; `fixtures.py:414-419`). So **a forgery adds nothing**;
- dice: TN 7, a face of 1 counts −1, 2-6 count 0, 7-9 count +1, 10 counts +2
  (`dice_engine.py:153-161`).

With two dice the net is at most 4, so the margin is at most 2. The odds are **Overwhelming 0,
Success 0.07, Partial 0.19, Failure 0.74** (exact enumeration, §9).

Results: O, S or P emit `finding.made` with that degree; Failure emits `finding.none`; a refusal (a
failed precondition) also emits `finding.none`. `interview` and `reconstruct` are ungraded: they emit
`finding.made` with `degree None`.

**2.9 What a finding uncovers** (the "planted trail"). At RESOLVE, `find_trail` dispatches only
`finding.made` (`rosters.yaml:2423-2445`). The host builds a `FieldworkInput` with the band, the trail
and `finding_terms` (`seam/wrappers/fieldwork.py:49-63`), and `modules/fieldwork/find.py` returns
`(trail event, terms[band])` for each trail item. No band (Failure, or ungraded) means nothing is
uncovered.

The trail is `trail_of(subject, you)`: the latest `record.forged` that wrote the subject (deeds done to
it) or that is anchored on it (deeds done by it). An item is dropped if no person did it, if you did it,
or if you already hold it. At the next WITNESS, `_found_claims` gives you what a witness would have
held, masked to the band's terms. At Partial, `who` is masked, and so is the event-kind claim on the
actor. The source is `inferred`, refracted at remove 1 (`witness.py:276-315`).

The docstring states the consequence: the trail is "REACHABLE ONLY THROUGH A PLANT" (`epistemic.py:379`).
You learn a forged Record's id either by witnessing the forging, which already tells you and closes the
trail, or by being given the Record.

**2.10 Covers.** `conceal` mints a `cover` naming you (`effects_information.py:258-269`). While one of
its 3 stages is unmatured, `anchor_of` answers the cover's id for your acts. Deposits are then *about*
the alias, `witness_key` partners stop seeing you, and the "deeds by" side of `trail_of` moves. **`seen.who`
still names you to everyone present** (`attribution.py:118-121`).

## 3 A worked example

The world is `test_fi03_trail.py::trail_world`: `tiny_world` with the Crown faction planted. I ran it
read-only (§9). Its ticks are seasons, advanced by hand between stages. The cast: **p_other** (the
forger) and p_mid and p_low are in Hh; **p_high** (the investigator) is in S; p_king is in R.

**Tick 0 — forge.** p_other already holds a claim about p_mid (the `own_ledger` precondition), and p_mid
commits to the Crown. `forge` mints Record `rec:fi03_forge`, kind `faction_sheet`:
`{proposition: fac_crown, members: [p_high, p_mid], holdings: [], seats: [off_duke], head: p_other}`.
`head` is the one false key. The Record has `forgery_quality 1` and stages at ticks 1, 2 and 3. Its hold
opens to p_other. The Event is `record.forged`.

WITNESS: p_mid is co-located and gets `(p_other, record.forged)`, `(rec, record.forged)` and
`seen{stratum: uncontested_material, who: p_other}`, all firsthand at 100. p_high gets nothing.
`trail_of(rec, p_high)` returns `[record.forged]`.

**Tick 1 — the plant.** p_other `move`s to S (`travel.moved`), then `give`s the Record to p_high
(`record.given`). `give` requires that the subject is a Record, that you hold it, and that the receiver
is `with` you. p_high, co-located, now holds at 100 firsthand: `travel.moved` and `record.given` on
p_other, `seen{who: p_other}` and `content:faction_sheet` with `head: p_other`. He now believes the
forger heads the Crown, at full confidence.

**Tick 2 — research.** The real chooser path forms `research` on the Record.

- Ob = min(2 + 1, ceiling 2) = 2. Pool 2.
- Across 40 act ids the degrees came out Success 5, Partial 7, Failure 28 (theory: 7%, 19%, 74%).

*Success (act id 0):* `finding.made`, terms `[stratum, marks, who]`. p_high gains three `inferred`
claims at `int(100 × (1 − 0.5×1) × (1 − 0) + 0.5) = 50`:
`(p_other, record.forged, True)`, `(rec, record.forged, True)` and `seen(rec){who: p_other}`. Each
`claim.deposited` names both the finding and the forging as causes. His own act also deposits
`(rec, finding.made)` and `seen(S){who: p_high}` at 100, unrefracted because he is the actor.

*Partial (act id 1):* only `(rec, record.forged)` and `seen(rec){who: None}`, at 50. He learns the
sheet was forged, not by whom. **The trail is now closed to him for good**: a later Success on the
same Record deposits nothing (`holds_trail`, `epistemic.py:356-360`).

*Counter-information:* p_other is in S and receives `(rec, finding.made)` and `seen(S){who: p_high}` at
100. **The forger learns he was investigated, and by whom, with more confidence than the investigator
has in his finding.**

*Next deliberation:* `questions_for` raises a question about the claim `(p_other, record.forged)`, and
`opening_set` forms candidates on p_other from it (`test_fi03_trail.py:565-588`). In the control arm,
with `finding_terms` emptied, he forms none.

**Tick 3 — spreading it.** p_high `move`s to R and `tell`s p_king about p_other. His Said is
`(p_other, record.forged, True, conf 50, chain ())`. Across 12 act ids the result was 2 `news.told`
(Success) and 10 `news.untold`. On a told: p_king holds `(p_other, record.forged, True)`, `told_by`,
confidence 50 (co_located, ×1), chain `(p_high,)`, read weight 0.5^1 × 1 × 1 = **0.5**.

**After that.** Each MATTER takes 5 off: 50 → 45 → 40, reaching 0 after ten seasons. The eviction score
at tick 2 is 50 × 3 = 150.

**The same chain under a cover** (probe). If p_other takes `conceal` first, the bystander's deed
claims are about `rec:cv` instead of p_other, but his `seen.who` is still p_other. A Success finder
gets `(rec:cv, record.forged)` plus `seen{who: p_other}`. **The cover moves what the claim is about. It
does not hide the hand.**

## 4 What you can do

**Who may act.** Eligibility is a list of alternatives. Every row below except `issue` (`remit:issue`) and
`open_case` (`remit:determine` only, `verb_table.yaml:902`) includes `own`, so anyone may attempt those
rows. A `presence:` alternative never admits by itself: it is unevaluable person-side
(`options.py:623-625`).

**Cost.** Each act spends from your scene-action budget (§0): 1 as a lone scene, or a share of an
extended scene that costs 2 for up to 3 acts. Holding the Record a maker verb mints raises next
season's budget by 1.

The "seed 0" column is ctl attempted/ok. Formation counts come from my `w.acts` probe: these are acts
the chooser formed, including those refused at admission.

| verb | prerequisites (typed) | outcome | writes | seed 0 |
|---|---|---|---|---|
| `research` | subject is a Record (you need only know its id) | graded, 2.8. O/S/P: `finding.made`, uncovers a trail if one exists | nothing | 14 / 7 (probe: 6 P, 1 S, 7 F); 115 `finding.none`, so about 108 formed acts were refused at admission |
| `surveil` | subject is a Rung and you are `present_at` it | graded. The Person case is absent, so the trail's "deeds by" side is unreachable | nothing | 30 / 5 (2 P, 3 S, 25 F) |
| `examine` | a Site exists and you are present at it | graded | nothing | **0 / 0 in seeds 0-2: it never passes admission.** It is formed 62 times in seed 0, and all 62 emit `finding.none` at admission (probe; reason not traced) |
| `interview` | subject is a Person | ungraded `finding.made`. Uncovers nothing and reads nothing from the interviewee | nothing | 32 / 11 |
| `reconstruct` | you hold a claim on the subject | ungraded. Uncovers nothing | nothing | 39 / 33 |
| `thread_read` | `requires_typed: none` (TS ≥ 30, no carrier, H-85) | not resolvable | — | never formed |
| `survey` | a claim on the subject, and the subject coheres under one faction | `faction.surveyed`; a true sheet in your hold, and its content in your ledger | Record | 57 / 13 |
| `forge` | as `survey` | `record.forged`; a sheet with `head` = you, `forgery_quality 1`, in your hold | Record | 52 / 12 |
| `conceal` | none | `cover.assumed`; a cover naming you, live about 3 seasons | Record | 19 / 19 |
| `create_record` | none | `record.created`; a `text` Record in your hold | Record | 87 / 87 |
| `give` | a Record you hold, to a person `with` you | `record.given`; your hold closes and the receiver's opens; he gets the content | Tenures | 16 / 0 (seed 1: 21 / 0; seed 2: 19 / 1, a cover) |
| `tell` | a claim on the subject, and the hearer `with` you | contested; 2.5 | nothing | 23 / 4 (seed 1: 25 / 7; seed 2: 19 / 6) |
| `destroy_record` | a Record you hold | `record.destroyed` | Record | withheld from formation (`fixtures.py:923`); TESTS-ONLY |
| `utter`, `petition`, `issue` (`remit:issue`), `open_case` (`remit:determine`) | (their own rows) | make Propositions, petitions, dispensations and case files. Their kinds are chronicle-public only if a `binding_decision` row emits them (2.2) | Record / Proposition | 39/39, 42/14, 6/5, 12/6 |

Every Record you hold adds 1 to your scene budget (`budget.py:57-58`). A failed or refused inquiry is
invisible to everyone, you included, because `finding.none` is never deposited.

## 5 Pursuing goals here

**(a) Goals and how the code represents them.** No "investigation" goal object exists. An actor's
pursuits do not name a culprit to find. (In ctl, 37 of 74 persons have empty pursuits after two
seasons in seed 0.) What drives fieldwork is the **agenda**: a claim landing in your ledger raises a
Question (2.7). The goals below are what a person can *arrange*. The code marks success only as claims
in someone's ledger.

| goal | what success is, in code |
|---|---|
| find out who did X | you hold `(doer, kind, True)`, or a `seen` claim on the thing with `who` set |
| hide what you did | nobody else holds your deed claim, or holds it only about your cover's id |
| plant evidence | someone else holds the `content:` of a Record you made, which says what you chose |
| spread news | hearers hold your claim as `told_by`, with you in the chain |
| suppress news | others hold no claim, or a weak one (low confidence, evicted, decayed) |

**(b) The plays, step by step.**

*Play 1: find the hand behind a document.*

1. Get the Record's id into your ledger without witnessing its creation. Being given it is the only
   built route, since witnessing the creation closes the trail.
2. `research` it.
3. Per attempt: 7% the hand is found (Success), 19% the deed without the hand (Partial, and the trail
   then closes to you), 74% nothing.

Only forged Records have a trail. A survey, a cover or a text Record yields nothing, because they are
not in `covert_kinds`. `surveil` and `examine` cannot reach a forging, since a forging writes a Record,
not a Rung or a Site.

*Play 2: just be there.* Standing where the deed happens gives `firsthand` 100 with `who`, which beats
any finding (50, `inferred`). Being in the room is the strongest information act in the game, and it
costs no slot.

*Play 3: hide a deed.*

- Act where nobody else stands.
- Avoid acts whose Event kind a `binding_decision` row also emits. `chronicle` broadcasts those to
  every person.
- Avoid acting through a seat (`post_remit`).
- Avoid writing a thing others hold (`document_key`).
- `conceal` first, so that later learners file the deed under an alias. This costs one act, and the
  cover lapses after about 3 seasons.

A cover does not hide you from anyone present (3, cover probe).

*Play 4: plant false paper.*

1. `forge`. You need a claim on a subject that coheres under one faction; 40 of 52 forges were refused
   in seed 0.
2. `move` to the target.
3. `give` the Record. He must be `with` you. You keep no copy, but your own ledger keeps the content.

He now holds the false `head` at 100, indistinguishable from a true sheet. What reads it: a petition
he files on it is addressed to the forger (`effects_information.py:756-758`). Nothing else in the
decision layer reads the sheet's `members`, `holdings` or `seats` (G20 FI-G03).

*Play 5: spread news.*

1. Have a claim on the subject.
2. Stand with the hearer.
3. `tell`.

The hearer gets **your** confidence, discounted at read time by 0.5 per hop. If he already holds the
same triple from anywhere, the telling deposits nothing. A Partial telling may garble a number or drop
a name.

*Play 6: suppress.* No verb removes a claim. `destroy_record` is withheld from formation. Your levers
are prevention (Play 3) and time: −5 per season, plus eviction at 200 claims, where old claims go
first.

**(c) Costs, risks, counter-play, blockers.**

- Every act spends scene-action budget (1 alone, or a share of a 2-cost extended scene; §0). There is
  no Exposure meter, no money cost and no wound.
- Inquiries are themselves witnessed. **Anyone co-located** gets the `finding.made` claim and
  `seen{who: you}` at 100 (`epistemic.py:428-453`). That includes the forger, if he is there.
- Failure and refusal both leave nothing in any ledger. You cannot tell a missed roll from an
  impossible inquiry, and nobody else can either.
- A Partial on a trail permanently denies you the hand.
- The forger can see you coming (3, tick 2). There is no counter-espionage verb (ED-FI-0002 unbuilt).
- Blockers: no `give` of a forged Record in seed 0 (the chooser's `give` subjects are people and
  buildings, §8), so in practice the plant never happens.

**(d) What the mechanics structurally reward and punish.**

- **No investigator is better than another.** Pool 2 and Ob 2 apply to everyone. Even a written
  capability would not change this, because no `VERB_CAPABILITY` row names an inquiry.
- **Forgery quality is inert**: the ceiling 2 swallows the +1.
- **`interview` and `reconstruct` are dominated**: they spend budget, uncover nothing by construction
  (no degree, so no `finding_terms` row), and emit a `finding.made` that tells bystanders you asked.
- **`examine` never passes admission** in seeds 0-2. It is formed 62 times in seed 0 and refused every
  time.
- **Presence dominates inquiry**: 100 firsthand against 50 inferred.
- **Telling something your hearer saw with you deposits nothing.** This is a mechanism: dedup skips a
  copy the hearer already holds unchained (`witness.py:932-935`). The evidence is small: all 4 seed-0
  tellings hit it (probe). That is one seed, n = 4. Seeds 1 and 2 have 7 and 6 `news.told`, which I did
  not trace. I make no claim that telling is generally wasted. A telling to someone who was absent does
  land (the §3 example).
- **Kind-sharing broadcast.** Any Event whose kind a `binding_decision` row emits reaches every person
  at 67 (2.2). That includes kinds produced by non-binding acts (`argue`'s `pursuit.moved`) and by
  MATTER.

**(e) What success leaves in the world.**

- *A finding:* claims in the finder's ledger only, at 50 and decaying; `claim.deposited` Events whose
  causes chain claim → finding → forging; and a question on his next agenda. No world state changes.
- *A plant:* a hold moved and a false content claim at 100.
- *A cover:* a Record and an anchor map entry (`World._covers_logged`) that fixes forever what each
  logged Event is about.
- *A telling:* a chained claim, the only place a path of hearsay is recorded.

## 6 How it connects

- **Social contest (SC):** owns the roll for the graded inquiries and for `tell`. Reads deed claims for
  `reception` and `proofs`, and reads `Record.forgery_quality` through the input builder
  (`seam/wrappers/sigma.py:174-191`). No inquiry product is a proof kind yet (FI-G47).
- **Governance (GV):** `issue`, `dispatch`, `confer` and `release` are `binding_decision` rows, so every
  Event of a kind they emit is chronicle-public, whoever or whatever caused it. Seat reports of MATTER changes go to governors via `post_remit`
  (`witness.py:513-524`). `petition` and `open_case` make Records.
- **Factions (FA):** `survey` and `forge` freeze `faction_q.resolve`. The forged `head` addresses the
  holder's later petitions.
- **Decision layer:** claims become Questions, vetoes, names and operands. The chooser never reads the
  World.
- **MATTER:** decay, plus stage maturation, which ends covers and document terms.
- **Threadwork (TW):** `thread_read` waits on a Thread Sensitivity carrier. The sim knots and `trace`
  are TW-side.
- **Combinations:** `conceal` → `forge` → `give` puts the deed claims under an alias for bystanders but
  not for a hand-band finder. `research` → `tell` moves a 50-confidence inference outward at a read
  weight of 0.5 per hop.

## 7 Playing it as proposed

**[PROPOSED] throughout this section.** The rows come from the lexicon `proposals/2026-10-16-verbs/2026-10-16-verbs-12-lexicon-fieldwork-and-inquiry.md`
(Status PROPOSED, 2026-10-17; named mechanics in §3.7 `:860-875`). None of it executes.

| you would… | how it would work | waits on |
|---|---|---|
| learn something from every inquiry | a per-verb selector over the world: `examine` reads the Rung's log, `research` reads a Record's content and whether it is forged, `reconstruct` names the best-supported candidate; confidence by degree, at remove 0 | **M1** finding producer (FI-G01) |
| tell a missed roll from an impossible ask | refusal → `inquiry.refused`; Failure stays `finding.none` | **M2** |
| be honestly wrong | on Failure, a wrong `who` drawn from the inquiry's candidate set | **M3** (K-37) |
| face a skilled hider | Ob = the concealer's score/2; `forgery_quality` = the forger's score/2; a graded cover | **M4**, J-T1 (stored score), H-210 |
| hear the interviewee's answer | the question lands in his ledger; he answers, evades or lies by his own act next season | **M5**, J1 (lexicon prefers option (b)), ED-FI-0004 Lattice |
| destroy or access paper by holding | `hold:<object>` eligibility typed | **M6** (H-75) |
| survey a place | `rung_sheet` (holder, persons, stores, forces); `audit`, `census` and `scout` as modes | **M7** |
| bribe | `transfer`'s write plus an inducement deposit to a circle of two; payee-side weight | **M8**; `suborn` parked on J-C-6 (lying) |
| bring a finding to court | `determine` and contests read held findings by proof kind | **M9** (SC) |
| shadow a person | co-movement | **M10** |
| unmask a cover | `watch` (the proposed rename of `surveil`): the true `who` of a covered act at the watched Rung, rolled against the cover's grade | M1, M4; ED-FI-0002 |
| disguise yourself | a cover with scope `room` hides `seen.who` from those present | `conceal` scope decision |
| infiltrate | a cover plus `oblige`'s duty edge | live cover; R-21/22 |

Also proposed: `search` and `track` as modes of `examine`, `decipher` (parked), `eavesdrop` and
`intercept` (parked), `trace` (TW, needs plugged knots). The lexicon also proposes that `forge` emit
`faction.surveyed` in place of `record.forged`. My reading: that would leave `covert_kinds` naming a
kind no row emits, which `data/verbs.py::_check_covert_kinds` refuses at import (`rosters.yaml:2480-2484`),
so the two would have to move together. The canon price "+2 Exposure" was declined (FI-G29).

**Stubbed or inert at shipped values today:**

- `telling_privacy 0`, `intent_disclosure 0`, `stance_polarity "legacy"` (regard does not enter
  choice);
- `rank()` ≡ 0, competence ≡ 1 (H-200), `Seen.why` ≡ None, `marks` ≡ ();
- `witness_key` admits nobody new, because no `knot` Tenure can be opened (`tie / knot` effect declined,
  H-182);
- `forgery_quality` is capped away;
- `thread_read` is unresolvable; `destroy_record` is withheld;
- `surveil`'s Person case is absent.

**The knots sim** (`systems/fieldwork/sim/knots.py`, called only by `engine/tests/test_knots_ed912.py`).

| element | rule |
|---|---|
| formation | bonds ≥ 5, disposition ≥ 5, one party with TS ≥ 30; roll `spirit×2 + history_relationships` d10s at TN 7 against Ob 2 (`:52-59,214-227`). Overwhelming gives a Close knot, Success a Distant one. At the default spirit 3 (pool 6): Close 14%, Distant 33%, none 53% (my enumeration) |
| strain | clamped to Distant (−2, 5) and Close (−5, 5); start 0 and −2; breaks at ≥ 5 (`:68-80`) |
| tempered | a Close knot at ≤ −5 absorbs one rupture |
| loss | composure 4 and disposition −3 are *returned, not applied*. A Close knot with positive strain lands a conviction Scar 1; a rupture costs Coherence −1 (`[UNVERIFIED post-ED-912]`) |

## 8 Common mistakes and traps

**Wrong assumptions about the rules:**

1. **"A cover hides me."** Not from those present, and not from a finder whose band shows `who`. It
   changes what claims are *about* (verified, §9).
2. **"A forgery is hard to detect."** Its quality is capped away. Every research on it rolls 2 dice
   against Ob 2.
3. **"A Partial is a step toward the answer."** It closes that trail to you permanently (`epistemic.py:356-360`).
4. **"`research` needs the document in hand."** It needs only an existing Record id
   (`verb_table.yaml:1364-1372`). The *trail*, however, is reachable only through a plant.
5. **"`interview`/`reconstruct` succeeded, so something was learned."** Ctl counts their
   `finding.made` as ok, but they carry no degree and uncover nothing.
6. **"Findings are certain."** They land at 50 (`inferred`, remove 1), half of what a bystander gets.
7. **"Claims are frozen at deposit."** C10 said so. `refracted_confidence`'s "FROZEN AT DEPOSIT"
   (`options.py:1433`) refers to the refraction factors only. MATTER decays every claim by 5 each
   season (errata G8).
8. **"Old firsthand knowledge is safest."** Eviction ranks `confidence × (when+1)`, so old claims go
   first.
9. **Two "knots".** The engine's `knot` Tenure (the `witness_key` channel) and the unplugged sim are
   unrelated.
10. **"Inquiry runs, so investigation is in the loop."** The register grades the scale `in_loop: false`.

**Stale statements in the tree and the extracts:**

11. `rosters.yaml:2484-2485` says `conceal` is unbuilt. It is built (`verb_table.yaml:207`; 19 of 19 in
    seed 0).
12. G20 FI-G23/G24 ("`forgery_quality` written by nothing") and FI-G26 ("no `conceal` verb") are stale
    at HEAD. L12's `watch` is a *proposed* rename; HEAD has only `surveil` (errata C8).

**Where the draft appendix A8 was wrong, and the correction:**

- *"G20 does not exist."* It does: `extract/G20_gaps_SC_GV_FI_TW.md` holds FI-G01..G58.
- *"`examine` formed and refused only", "62 `finding.none`"* (A8 A3, A4). **A8 was right.** My
  round-1 text, which said examine is never formed, was wrong. `w.acts` holds 62 `examine` acts in seed
  0, and all 62 emit `finding.none` at admission; ctl's 0 counts only resolved acts. Corrected wording:
  "never passes admission".
- *"250 `finding.none` (218 refusals, 32 Failures)."* **Now reproduced** by attributing on `w.acts`.
  The 250 are research 115, examine 62, surveil 46, interview 21, reconstruct 6. Of these, 32 are
  rolled Failures (research 7, surveil 25), leaving 218 refusals. Errata C8 had marked the breakdown
  unverified; the probe verifies it.
- *"Uncertain why every `give` is refused."* Answered by the probe: of the 16, 15 name a person or a
  building as subject (the question's referent), which fails `existence(subject, Record)`. One names a
  cover held by someone else. Seed 2 has 1 success, a cover.
- *"Why no chained `told_by` survives."* Answered: each of the 4 seed-0 tellings carried a triple its
  hearer already held unchained, so the dedup skipped it.
- *"`witness_key`/`post_remit` RUNS-IN-LOOP"* (A8 B4). `witness_key` is TESTS-ONLY: it admitted
  nobody. `post_remit` is TESTS-ONLY at seed 0 and executes at seed 2 (one `inferred` claim).
- *Scene allowance.* A8 says "one season = up to `scene_budget=5` rounds". The correct reading is in §0
  (CROSS C1): `budget()` returns scene actions; an extended scene costs 2 for up to 3 acts; one scene is
  released per round. Budget 5 therefore buys 7 acts, and seed 0 shows ~7.6 resolved acts per person per
  season. Errata G11's "~8-10" is not supported.
- *`dissents`* (A8 B2 "disagrees with the holder's own firsthand claims about a person"). It is only
  about the holder **himself** (a person predicate with `subject == holder`) or a cell, plus the act
  prior (`options.py:1393-1407`; errata C8).

**§8 Round-2 corrections** (each cited line re-opened before accepting it):

1. *H-F2, inquiry pools.* Accepted. I had given the wrong reason ("no capability is written").
   `VERB_CAPABILITY` maps only `tell`/`speak` (`rosters.yaml:1228-1231`), and an unmapped verb gets
   `None` (`sigma.py:113-116`), so a written capability would not move any inquiry pool. Fixed in 2.8
   and 5(d).
2. *H-F4, seed-2 `inferred`.* Accepted. The `post_remit` slot is regraded per seed: TESTS-ONLY at seed
   0, executing at seed 2 (§0). The producers are `witness.py:289` (found, 0 in seed 2), `:513-524`
   (seat report) and `:598` (channel).
3. *H-F6, `destroy_record`.* Accepted. It is TESTS-ONLY, not DESIGN-ONLY: the row is typed with an
   effect, and formation is withheld by `fixtures.py:923` (`verb_table.yaml:306-312`).
4. *H-F7, `open_case`.* Accepted. Its eligibility is `remit:determine` only (`verb_table.yaml:902`), and
   `issue`'s is `remit:issue`. The §4 claim "every row includes `own`" is fixed.
5. *H-F10 and CROSS C1, scene budget.* Accepted. `interactions_per_scene = 3` (`fixtures.py:488`) and
   `extended_scene_cost = 2` (`:489`); the spend loop is `choose.py:643-657`; one scene per round is
   released (`driver.py:456`). Every "one slot per act" phrasing is replaced (§0, §4, §5c).
6. *H-F16 and L-X6, `examine` and who sees an inquiry.* Accepted. "Never formed" becomes "never passes
   admission" (62 formed in seed 0, by probe). "The subject's holder learns who inquired" becomes
   "anyone co-located".
7. *H-OBS, CROSS C5 and L-X17, chronicle.* Accepted. It is a kind filter (`epistemic.py:652-654,685-686`);
   `pursuit.moved` comes from `determine` (`verb_table.yaml:355`) and also from `argue` (`:157`).
   Rewritten in 2.2, Play 3, 5(d) and §6. MATTER's `tenure.closed` I took from CROSS C5 without
   re-tracing which binding row emits it.
8. *L-X19, column order.* My columns already read attempted/ok. The header now defines attempted as
   "passed admission" and ok as Partial-or-better for graded rows (CROSS C2).
9. *L framing note.* Accepted. "Telling to companions is wasted" generalised from 4 tellings in one seed.
   It is restated as the dedup mechanism plus its n = 4 evidence, with no general claim (5d).
10. *CROSS C3 and C11.* Ticks replace "season N" in 2.6. Rung, Tenure, Proposition, Office, purview,
    establishment, stratum, prize and `with` are added to §1.

## 9 Checks

- Opened: `modules/fieldwork/find.py:28-34`; `seam/wrappers/fieldwork.py:46-64`;
  `epistemic.py:329-404,428-686,794-840`; `loop/witness.py:86-315,365,386-391,606,932-966`;
  `decision/options.py:615-625,1338-1448,1513-1545`; `state/ledgers.py:17-32`; `loop/matter.py:312-347`;
  `state/attribution.py:105-265`; `loop/effects_information.py:170-200,258-270,744-830`;
  `verb_table.yaml:207-222,281-313,434-452,533-580,925-948,1127-1200,1321-1438,1495-1505`;
  `rosters.yaml:415-434,1018-1025,1115-1160,2423-2489`;
  `data/fixtures.py:228-247,293,386,414-439,489-527,761-864,923`;
  `modules/social_contest/roll.py:96-125`; `engine/dice_engine/dice_engine.py:153-161,196-239`;
  `seam/wrappers/sigma.py:119-191`; `decision/budget.py:40-61`; `requirements.yaml:169-180`;
  `systems/fieldwork/sim/knots.py:46-97,201-227`; `engine/season/tests/test_fi03_trail.py:1-300,534-625`;
  the lexicon §3.7.
- Ran (`python -I`, scripts in `scratchpad/t06/`):
  - `chain.py` (trail_world): record content, stages, `forgery_quality 1`; removes 0/.333/.667/.667/1;
    bystander claims at 100; Success deposits 3 claims at 50; Partial deposits 2 with `who=None`;
    40 act ids gave S 5, P 7, F 28.
  - `tell.py`: 2 of 12 tellings succeed; told claim at 50 with chain `(p_high,)`, weight 0.5.
  - `cover.py`: deed claims go to `rec:cv`; `seen.who = p_other` for bystander and finder.
  - `seen_by_forger.py`: the forger gets `finding.made` and `seen{who: p_high}` at 100.
  - `resp.py`: 1 trail question and candidates on the forger.
  - `realm.py`, `realm2.py`, `realm3.py` (`build_realm(0)` and `(2)`, two seasons, the ctl recipe):
    inquiry degrees; give subjects; 0 found deposits and 0 chained claims in seed 0; 1 `record.given`
    and 1 `inferred` in seed 2; 250 `finding.none` in seed 0; 0 resolved `examine`; tellings deduped.
  - `examine.py` (round 2, seed 0): `w.acts` 1,407 against `d.resolved` 1,132. 62 `examine` formed, all
    `finding.none`. `finding.none` by verb: research 115, examine 62, surveil 46, interview 21,
    reconstruct 6.
- Round 2, re-opened: `rosters.yaml:1226-1232`; `sigma.py:110-117`; `verb_table.yaml:155-158,300-313,355,900-903`;
  `fixtures.py:486-490`; `epistemic.py:650-656,683-687`; `decision/choose.py:643-657`; `loop/driver.py:454-458`;
  `decision/budget.py:18-22`.
- Enumerated: 2d10 at TN 7 against Ob 2 gives O 0, S 0.07, P 0.19, F 0.74. 6d10 against Ob 2 gives
  O 0.142, S 0.328. The refraction table in 2.4 is computed from the formula.
- Not confirmed:
  - why 40 of 52 forges are refused in seed 0;
  - why every `examine` is refused at admission;
  - whether seed 2's one `inferred` claim came from the `post_remit` channel or a seat report;
  - the seed-1 and seed-2 tellings;
  - which binding row emits `tenure.closed` (taken from CROSS C5);
  - `deliberate.py:252-259` (CROSS C1), which I did not find at that path.
