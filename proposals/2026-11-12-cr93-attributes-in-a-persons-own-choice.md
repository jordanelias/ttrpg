# CR-93: attributes in a person's own choice

## Status: PROPOSED (2026-11-23). Workplan v12 position B10.51 (Batch B10-character, lane IN), the design half of CR-93; its build is `B10.80` (HELD). A design: reference under `CLAUDE.md` §0.05, binding nothing and resolving nothing. No file under `engine/` changes with it. Every take is marked `[ASSUMPTION; Jordan to correct]` and reverts alone.
## Lane: IN
## Reads: `engine/season/decision/choose.py` (`score_terms`, `odds_weight`, `_writing_bands`, `_sample_order`) · `engine/season/decision/options.py` (`opening_set`, `_judgement_factor`, `competence`) · `engine/season/seam/wrappers/sigma.py` (`believed_chance`, `odds_of`, `believed_input`, `_rolled_as`) · `engine/season/seam/wrappers/pool.py` (`governing_score`, `rank`, `faculty`) · `engine/season/verb_table.yaml` (`capability:`, `governing:`, `opposed_attribute:`) · `references/descriptor_registry.yaml` (`attributes`, `capabilities`) · `engine/season/rosters.yaml` (`graded_tasks`, `task_fraction`, `capability_uses`) · `proposals/2026-10-24-character-layers-v2.md` §11 (B10.53, M40) · workplan v12 `B10.28`, `B10.31` (`valoria_master_workplan_v12_part12_cont.md`)
## Base read: the working tree at `43da21c37`. Every number below is the output of a command quoted beside it, or is marked `[ASSUMPTION; Jordan to correct]`.

**The four questions** (v11's REMAINING UNBUILT, copied by v12 `B10.51`, the words A-98 corrected marked there): (1) a **skill** term on an uncontested candidate, its scale against the pursuit term, and why it is not a second ladder for `odds_weight` on contested ones; (2) a per-person τ falling with Focus (AR-23); (3) an error on the believed chance that Reason shrinks and low Focus widens (AR-21), and how it composes with M40's risk term so the two are not two ladders for one quantity (NERS S); (4) obligations and demands named as CR-88's. Each answer carries a falsifier and a control. Focus and Reason are **attributes** (`attr.mind.focus`, `attr.mind.acuity`, display name Reason, `references/descriptor_registry.yaml:50-51`), never skills.

**The rulings this composes on** (ED-IN-0347, RULED; verbatim from `proposals/2026-11-05-attribute-rulings-by-subject.md`):

- **AR-04** (`:29`): *"these attributes capabilities are to be combined with pursuits convictions ambitions goals obligations demands etc to provide weighting for best course of actions available to that character"*.
- **AR-21** (`:58`): *"reason concerns mental acuity, logic, understanding of concepts/facts, forecasting, understanding what a choice entails...but if you have low focus then you may make avoidable errors or fail to filter and prioritize correctly so your forecast includes irrelevant info"*.
- **AR-23** (`:63`): *"high focus characters are less likely to be distracted as well as less likely to have irrelevant information impact their choices"*.
- ED-IN-0261 (narrowed by A-108, not reversed): a person's choice weights are his pursuits; nothing here adds a weight vector. A-98 (4): one capability kind, `skill`.

**Sources the entry cites by short path.** `proposals/2026-11-12-subsystem-audit-suite/` exists in the tree. This design worked from the entry's own copied INSTRUCTION, the rulings file above and the tree; the intake, `master/eval/E1.md` and `E4.md` were not opened (the entry copies v11's text, and the tree, not the intake, says what is built).

**Three corrections to the entry's premise, read off the tree.**

1. **A skill names no attribute.** The entry reads "that skill's `base` attribute in `descriptor_registry.yaml: capabilities`" and `rosters.yaml: vocation_attribute`. Both are gone: B05.25 moved which attributes a verb reads onto the verb row (`references/descriptor_registry.yaml:69-71`: *"A skill names NO attribute (B05.25): which attributes a verb reads is the verb row's own `governing:` and `opposed_attribute:`"*). The sibling design `proposals/2026-11-12-cr95-spirit-against-circumstance-and-influence.md` §0 makes the same correction for `opposed_by`. Here the verb row's `capability:` names the skill and its `governing:` names one to three attributes; `pool.py::faculty` (`:122`) composes both into the one pool.
2. **`capability_factor` does not exist.** `B10.28` and `B10.31` call `capability_factor(p, "<use>", fx)`. The tree's reader of a `judgement` row is `decision/options.py::_judgement_factor(p, rows, fx)` (`:1622-1636`: `about_mid` of `p.attributes[row.key]`, several rows at one site multiplied, `None` where no row or nothing held), whose one caller is `competence` (`:1639`). This design names `_judgement_factor` wherever the entry names `capability_factor`; whether the build renames it or wraps it is the build's (§5).
3. **Uncontested acts are drawn.** v11 wrote (1) when an uncontested act always succeeded. Since B07.05, `task_draw_arm="on"` ships (`engine/season/data/fixtures.py:1162`): every row of `rosters.yaml: graded_tasks` (`:1314-1324` and on) is dealt by the social roll on the person's own pool against the row's `difficulty:`, and a band whose `task_fraction` share is 0 writes nothing (`loop/resolve.py:446`; `rosters.yaml:1419-1423`: `Failure 0, Partial 0.5, Success 1, Overwhelming 1`). This changes what (1) is (§1).

---

## 0. What attributes do in a person's choice today, read off the code

| where | what an attribute or skill does in the choice | opened at |
|---|---|---|
| `score_terms` | nothing directly: `(pursuit, stance, fit)`, no attribute or skill read | `decision/choose.py:252-284` |
| `odds_weight` on a **contested** candidate | the pursuit term is multiplied by his believed chance of the bands that write (`odds_weighting="believed"`, shipped, `fixtures.py:888`). That chance is `believed_chance` → `odds_of` mode (b) → `believed_input(pool=faculty(w, believer, verb))`, and `faculty` is `pool_of(governing_score + rank, …)`: **his `governing:` attributes and his rank in the row's `capability:` skill already reach a contested choice, through the chance** | `choose.py:166-191`; `sigma.py:985-991`, `:998-1025`; `pool.py:76-90`, `:115-122` |
| `odds_weight` on an **uncontested** candidate | 1.0: `_writing_bands` answers `None` for a row that contests nothing (`choose.py:159-160`), so a drawn task (`research`, `build`, `work`, …) is weighed as if certain, whatever he holds | `choose.py:155-163` |
| `_sample_order` | τ is `choice_temperature` (0.05, `fixtures.py:292`) for every person; nothing personal | `choose.py:472` |
| `fit_term` | the conferrer's belief about the candidate's skill (another person's), at `confer_fit_weight` 0.0 | `choose.py:220-241` |
| `opening_set` | reads no attribute: which candidates form is the person's tenures, the question and the row, never his scores (falsifier, §1) | `decision/options.py:64` |
| the uses table | one `judgement` row, `told_claim_credit` (Attunement, `competence_gain`); no row at any choice site | `rosters.yaml:3610-3619`; `capability_use_sites` `:1552-1557` |

**The defect in one line.** A contested act is priced by how well he expects to do it, skill and attributes included; an uncontested act he can fail is priced as certain. A man with Reason 1 and no `inquiry` weighs `research` exactly as a scholar does. AR-04 asks for the opposite, and AR-21 asks that how well he forecasts depend on Reason and Focus, which nothing reads (`proposals/2026-11-05-attribute-rulings-adjudication.md:31`: *"`odds_of`, exact from the believer's own pool and ledger, no error term"*).

**The principle all four answers keep.** Attributes and skills enter a person's choice as **how well he expects to do an act** ((1), (3)) and **how steadily he chooses** ((2)); never as **what he wants**. What he wants stays his pursuits (ED-IN-0261), so no answer below adds a weight vector or an additive "likes what he is good at" term, and every new factor is exactly 1 (or exactly the old chance) at its neutral value.

**The instrument.** Every reading below is one of two commands. The repo's own `python -m engine.season.harness.decision_spread --decisions|--season --seed N` (at `PYTHONHASHSEED=0`), and a scratch probe that wraps the module globals the chooser calls (`choose.odds_weight`, `choose._sample_order`) with the proposed terms and plays one season per arm: `PYTHONHASHSEED=0 PYTHONPATH=<worktree> python3 <scratchpad>/cr93_probe.py {reach|pair|season} <seed> …`. The probe was run once and is not kept (the batch's accretion rule); it changes no file. **Its own control:** with every proposed term at neutral, the wrapped season's content hash equals the unwrapped base at seed 0 (`6e3a066a9d4b921bf5258a23b55d0e37`), seed 1 (`01f7f9aa0f3d9a52242ea78c8c92cc23`) and seed 2 (`0a00352e0e9349f8c12d26f8f9e7e467`), the same three hashes `character-layers-v2.md` §11.6 records. So the wrap itself moves nothing, and every difference below is the term.

Realm facts the readings depend on (seed 0, 83 persons; `build_realm(0)`, counted over `Person.attributes`): Focus held `1:12, 2:10, 3:10, 4:17, 5:20, 6:14` (mean 3.78); Reason held `1:9, 2:16, 3:9, 4:20, 5:14, 6:15` (mean 3.71). No realm person holds 7 in either.

---

## 1. The skill term on an uncontested candidate

**The answer: the skill term is `odds_weight` itself, reaching the uncontested rows that are drawn.** For a candidate whose verb contests nothing and has a graded route (`rosters.yaml: graded_tasks`, read through `data/rosters.py::graded_route`, the one reader the fold and the believed odds share), the pursuit term is multiplied by his **believed expected share of the act's effect**:

```
task_weight(p, c) = Σ_k (share_k − share_(k−1)) · odds(act, bands ≥ k)       k over Failure < Partial < Success < Overwhelming
                  = 0.5 · P(≥ Partial) + 0.5 · P(≥ Success)                    with today's `task_fraction` (0, 0.5, 1, 1)
```

`share` is `task_fraction` (`data/rosters.py::task_share`, the fold's own reading of what a band lets land, `loop/resolve.py:446`); the band order is `dice_engine.DEGREE_ORDINAL`; `odds` is the one query, `View.odds` (`sigma.py::believed_chance`), probed with the act the candidate would become, exactly as `odds_weight` probes it (`choose.py:190`). It is asked only for **upper sets** of the band order, which is what lets (3)'s error carry one sign (§3). An answer of `None` reads 1.0, as `odds_weight`'s does.

**Where the skill is read.** Nowhere new. The believed chance of a graded task is `odds_of` mode (b) over `believed_input(pool=faculty(w, believer, verb))` (`sigma.py:985-991`), and `faculty` is `pool_of(governing_score + rank, …)` (`pool.py:122`): the verb row's `capability:` skill (his `rank`, `pool.py:115`) and its `governing:` attributes (`governing_score`, `pool.py:76`). So the term reads the skill and its attributes through the **one pool reader**, against the row's own `difficulty:`, and names neither.

**As a row of the uses table.** The term is the existing row `{use: social_roll, role: dice, key: verb, side: actor, add: pool_add, floor: pool_floor}` (`rosters.yaml:3612`): the place the verb's skill already changes an outcome. (1) adds **no row and no constant**, the strongest form of B04.05's *"that build adds rows and no constants"*: one member of `rosters.yaml: odds_weightings`, `believed_all` (contested candidates as `believed`, plus the drawn uncontested ones) `[ASSUMPTION; Jordan to correct: the member's name]`, and one predicate in `decision/choose.py`, the sibling of `_writing_bands`, answering the share steps of a drawn uncontested candidate or `None`.

**Its scale against the pursuit term.** A factor in `[0, 1]` on the pursuit term, the unit `odds_weight` already uses on a contested candidate. **No gain, so no coefficient to choose:** a believed expected share has no free scale. Measured, the factor over every drawn uncontested candidate formed for `--decisions`' questions at seed 0 (`cr93_probe.py reach 0`):

```
conceal      n=498 E[share] min 0.340 median 0.516 max 0.628
forge        n=498 E[share] min 0.340 median 0.546 max 0.652
move         n=498 E[share] min 0.340 median 0.484 max 0.652
raze         n=156 E[share] min 0.340 median 0.602 max 0.652
reconstruct  n=498 E[share] min 0.217 median 0.391 max 0.619
sabotage     n=498 E[share] min 0.340 median 0.546 max 0.652
surveil      n=498 E[share] min 0.217 median 0.391 max 0.595
survey       n=498 E[share] min 0.340 median 0.516 max 0.716
thread_read  n=24  E[share] min 0.340 median 0.515 max 0.652
train        n=1992 E[share] min 0.340 median 0.546 max 0.652
```

Every query was answered (no `None`). Today every one of these candidates is weighed at 1.0: as if certain.

**Its decision shift** (`cr93_probe.py season <seed> 1 0 0 0.5` against `… 0 0 0 0.5`; one season, `odds_weighting` `believed_all` in the stand-in):

| seed | resolved acts, base → `believed_all` | acts on drawn uncontested rows, base → `believed_all` | hash at `believed_all` |
|---|---|---|---|
| 0 | 627 → 615 | 196 → 158 | `d3ec56f4…` |
| 1 | 666 → 659 | 231 → 194 | `afcccbea…` |
| 2 | 653 → 620 | 213 → 177 | `d07d0f9e…` |

Drawn tasks fall by 16 to 19 per cent, most of it on the hardest (`reconstruct` 46 → 18 at seed 0, 67 → 45 at seed 1; `forge` 23 → 15, 25 → 17). The largest movers are the rows a person fails most often, which is the behaviour AR-04 asks for.

**Why it is not a second ladder for `odds_weight` on contested ones.** It is `odds_weight`: one function, one chance query, one unit, and two branches **disjoint by the row's own `contests:`**. On a contested candidate nothing is added, because the skill already reaches the chance through `faculty`; a skill factor on top would count the skill twice. Step 4 (precedent): CR-17 put the believed chance on the pursuit term; this extends its reach to the rows B07.05 made drawable after CR-17 was written.

**The alternative, rejected (step 5).** v11's "aptitude term" read as a judgement factor, `about_mid(skill or governing score, gain)` on uncontested candidates. Rejected on three counts: (a) it is the second ladder the instruction warns of, a factor centred on 1 beside a chance in `[0, 1]` for the same question, "how well does he expect to do this" (NERS S, *"calculations consistent in methodology"*); (b) it ignores the row's `difficulty:`, so a routine and a hard task would be priced alike; (c) it needs a gain fixture where the chance needs none. **An uncontested row that is not drawn** (a flat or brute row: `give`, `confer`, `commit`, …) has no outcome a skill can change, so no term reaches it: its factor stays 1.

`settle_efforts` is not widened: effort is still offered only where `_writing_bands` holds (a contested candidate) `[ASSUMPTION; Jordan to correct; revert: offer effort on a drawn task too, which the share steps would price]`. An inquiry (`research`, `examine`, `surveil`, `reconstruct`: `form: inquiry`) is weighted by the same `task_fraction` steps as a task `[ASSUMPTION; Jordan to correct; revert: an inquiry weighted by P(not Failure), the band its route's source names as depositing nothing, `rosters.yaml:1281-1283`]`.

**Falsifier (1).** (i) Two hand-built persons with equal pursuits and different attributes rank one drawn uncontested candidate differently at `believed_all` and identically at `believed` (the term at 0). Measured on the stand-in (`cr93_probe.py pair 0`): a realm person copied with every attribute at 1 and at 7 reads `conceal` on the same subject at E[share] **0.340** against **0.696**. (ii) *Gates nothing:* `opening_set` returns equal sets for the two. Measured: equal for each of three persons tried (`cohort_set_s_001`, `_002`, `_003` on `fac_church_of_solmund`, 19 candidates each). (iii) *Not a second ladder:* at `believed_all`, the factor on every contested candidate equals the `believed` arm's exactly; a difference means the branch leaked across `contests:`.
**Control (1).** `odds_weighting` `believed` (shipped) after the build: the one-season hash equals the base at seeds 0 to 2 (the stand-in's neutral reproduced all three, above).

---

## 2. A per-person τ falling with Focus

**The site and the control are `B10.28`'s** (`temper(p)` multiplies `choice_temperature` in `_sample_order`, through the use row `{use: choice_temper, role: judgement, key: attr.mind.focus, side: actor, gain: temper_gain}`, 1.0 where unauthored or at gain 0). This section states only the coefficient and the reading rule that chooses it.

**The sign: a conflict in `B10.28`, named for the orchestrator.** `about_mid(v, floor, ceiling, g) = 1 + g · (v − mid) / (mid − floor)` (`engine/substrate/descriptors.py:79-83`) **rises** with `v` at `g > 0`. So with `temper = about_mid(focus, …, temper_gain)` and `temper_gain > 0`, τ **rises** with Focus, the opposite of AR-23; yet `B10.28`'s named test reads *"at `temper_gain` > 0 … the low-Focus person's top differs from the score's top strictly more often"*. Both cannot hold. **Taken (step 5): the gain is negative and the reader is unchanged.** `temper_gain` lives in `(−1, 0]`: the judgement row reads through `_judgement_factor` as `competence` does, with one convention for every judgement row (a negative gain is a factor that falls as the attribute rises; the loader refuses a negative gain only on a `circumstance` row, `data/rosters.py:1651-1652`). The other fix, negating the gain inside `temper`, was rejected: it would make one judgement row's `gain` mean the opposite of another's (NERS S, two conventions for one form). **`B10.28`'s tests then read `temper_gain < 0`** where they say `> 0`; that edit is the orchestrator's (§7).
The bounds: at `temper_gain = −1` a Focus-7 person's factor is 0, so his τ is 0 and his order falls back to the score order with the `(verb, subject)` tie-break that H-96's sampler exists to remove (`choose.py:385-412`). So `−1` is refused, as is anything above 0 (that inverts AR-23).

**The reading rule** (step 4, `B10.29`'s precedent: *"No threshold is invented: each line is a direction against a control"*): **`temper_gain` is the swept value of least magnitude at which, at every one of seeds 0 to 2, the low-Focus group (Focus 1 to 2) takes a sampled top that is not the score top MORE often than at gain 0, AND the high-Focus group (Focus 5 to 6) takes one LESS often than at gain 0.** Each pole moves the way AR-23 says, each against its own control. That needs both because the groups differ at the control already: they face different questions.

**The sweep** (`cr93_probe.py season <seed> 0 <g> 0 0.5`, `g` the magnitude, so the gain is `−g`; one season; "off top" is the share of deliberations with two or more candidates whose sampled top is not the score top, read by the chooser's own `watch` hook):

| seed | gain | off top, low Focus (1–2) | off top, high Focus (5–6) | low moves up? | high moves down? |
|---|---|---|---|---|---|
| 0 | 0 | 43/91 = 0.473 | 62/142 = 0.437 | | |
| 0 | −0.25 | 55/93 = 0.591 | 65/142 = 0.458 | yes | **no** |
| 0 | −0.5 | 59/97 = 0.608 | 53/146 = 0.363 | yes | yes |
| 0 | −0.75 | 60/94 = 0.638 | 46/146 = 0.315 | yes | yes |
| 1 | 0 | 73/119 = 0.613 | 38/110 = 0.345 | | |
| 1 | −0.25 | 81/116 = 0.698 | 35/110 = 0.318 | yes | yes |
| 1 | −0.5 | 89/118 = 0.754 | 33/113 = 0.292 | yes | yes |
| 1 | −0.75 | 88/116 = 0.759 | 29/113 = 0.257 | yes | yes |
| 2 | 0 | 50/115 = 0.435 | 82/166 = 0.494 | | |
| 2 | −0.25 | 58/114 = 0.509 | 75/167 = 0.449 | yes | yes |
| 2 | −0.5 | 69/115 = 0.600 | 64/167 = 0.383 | yes | yes |
| 2 | −0.75 | 78/111 = 0.703 | 59/167 = 0.353 | yes | yes |

**Read: `temper_gain = −0.5`.** At −0.25 the high-Focus group departs *more* often at seed 0 (0.437 → 0.458), so −0.25 fails the rule; −0.5 is the least magnitude passing at all three seeds. At −0.5 the realm's τ runs from `0.05 × 1.5 = 0.075` (Focus 1) to `0.05 × (1 − 0.5 × 2/3) = 0.033` (Focus 6), and `0.025` for an authored Focus 7. `B10.28` ships `temper_gain` 0 (its control); −0.5 is the value the flip (B98) sets `[ASSUMPTION; Jordan to correct; revert: 0]`.

**Falsifier (2).** `B10.28`'s, with the sign read as above: two hand-built persons with equal pursuits at Focus 1 and 7, at `temper_gain` −0.5, over twenty draw seeds: the low-Focus person's top differs from the score's top strictly more often (`assert checked >= 20`); at 0 the two are byte-identical. Realm form: the table above, re-read at the flip: if at −0.5 either pole moves against AR-23 at any of seeds 0 to 2, the hook is not on the draw or the value is wrong.
**Control (2).** `temper_gain` 0: `temper` is exactly 1.0 and `x * 1.0 == x`, so the one-season hash equals the base at seeds 0 to 2 (`B10.28`'s control; the stand-in at 0 reproduced all three).

---

## 3. The error on the believed chance, and its one owner

**The one owner: `decision/choose.py::misjudged(odds, p, fx, draw)`**, a new function that wraps the View's query **once per deliberation**, in `make_ranker`, before `score` is defined (beside `odds = getattr(v, "odds", None)`, `choose.py:655`). It returns the query unchanged at neutral. Every reader of a believed chance in the chooser takes the wrapped query and none other:

| reader | how it receives the erred chance |
|---|---|
| `odds_weight`, contested | the `odds` argument `score_terms` passes (`choose.py:279`) |
| `odds_weight`, a drawn task ((1) above) | the same argument, the same function |
| `aim` (`B10.30`, PROPOSED) | it multiplies by `odds_weight` (*"the same believed-odds factor"*), so it reads the same chance |
| `risk`'s `chance(p, c)` (`B10.31`, PROPOSED) | *"The chance is asked through the same `odds` callable `odds_weight` receives"* (`B10.31` edit 3) |
| `settle_efforts` | through `score`, which closes over the wrapped query |

So `risk` does not perturb a chance, `odds_weight` does not, and no reader carries its own copy: **one owner, every reader composed on it.** The query itself (`sigma.py::believed_chance`) stays exact: it is what the person's own ledger implies; `misjudged` is how well he reasons from it. That split keeps the error person-side (AX-2: `decision/` holds the draw, `sigma` holds the World) and keeps `odds_of`'s mode (a), the figure shown for the true roll, untouched.

**The form.**

```
misjudged chance = logistic( logit(chance) + s(p) · logit(u) )        u from draw(p.id, "belief:<verb>:<subject>")
s(p)             = forecast_spread · _judgement_factor(p, rows of site `choice_forecast`, fx)
```

- `logit(u)` for `u` uniform on (0, 1) is a standard logistic variate: one uniform, no second distribution, zero-centred, so the error makes him **wrong, not bold or timid**. Boldness is appetite's (M40), below.
- The draw is **keyed by the candidate** (`verb`, `subject`), exactly as `_sample_order` keys its noise (`choose.py:484-503`, with its retry on `u == 0` advancing one stream), and read off the act the query is handed (`act.verb`, the payload's `subject`). So one person misjudges one act once per season (the factory seeds by `(world_seed, tick, pid, purpose)`, `state/ids.py:58-61`), the same way in every band set he asks of it and at every effort he weighs it at. The purpose differs from the choice draw's (`choice:…`), so neither stream moves the other.
- **One sign for every reader.** Every chance the chooser asks is of an **upper set** of bands favourable to the asker: the bands that write what he prices (`argue` `{Overwhelming, Success}`, `determine` and `arrest` `{…, Partial}`, read off `writes_by_degree`), the share steps `bands ≥ k` of (1), and the bands he comes through (`risk`). So a positive draw is optimism for every reader at once: a man who overrates his chances in a fight both prizes it more and fears it less, which is the coherent misjudgement AR-21 describes.
- **What it never touches.** An answer of `None` stays `None` (he cannot say; `risk`'s `risk_unknown_chance` fallback is a fixture, not his belief, and is not erred). A chance of exactly 0 or 1 stays where it is (`logit` is infinite there) `[ASSUMPTION; Jordan to correct; revert: clamp into (ε, 1 − ε) first, so a sampled certainty can be misjudged too]`. An uncontested row that is not drawn asks no chance and is never reached.
- A missing `draw` at `forecast_spread > 0` **raises** (`Unspecified`), never falls back to the exact chance: `_sample_order`'s rule (`choose.py:409-412`).

**As rows of the uses table.** A new site `choice_forecast: decision/choose.py::misjudged` in `capability_use_sites`, and two rows:

```
{use: choice_forecast, role: judgement, key: attr.mind.acuity, side: actor, gain: forecast_gain}    # Reason shrinks it
{use: choice_forecast, role: judgement, key: attr.mind.focus,  side: actor, gain: forecast_gain}    # low Focus widens it
```

`_judgement_factor` multiplies the two (`options.py:1622-1627`: *"A site with several rows multiplies them"*). With a **negative** gain (§2's convention) each factor falls as its attribute rises: at `forecast_gain = −0.5`, `s(p)` runs from `2.25 × forecast_spread` (Reason 1, Focus 1) to `0.25 ×` (7, 7), and is `1 ×` at the mid-points. `decision/` names no attribute (U1 §8); the keys are the rows'. One gain for both rows `[ASSUMPTION; Jordan to correct; revert: one gain per row, `forecast_reason_gain` and `forecast_focus_gain`]`.

**Is Focus read twice, (2) and (3)?** Yes, by two rulings for two quantities. AR-23's Focus is distraction among options already scored: τ divides every candidate's score, priced or not. AR-21's Focus is *"fail to filter … so your forecast includes irrelevant info"*: noise on the forecast, which reaches only the candidates priced by a chance, and moves an act's gain and danger together. Neither can stand in for the other (§6, the cut test).

**How it composes with M40's risk term, so the two are not two ladders.** `character-layers-v2.md` §11.1 (B10.53) already took the composition this design needs: *"`B10.51`'s (3) … acts on `chance(p, c)`, the term's input; appetite acts on the term's weight. One term, five factors, each from one place"*, and in (1a) rejected an appetite exponent on the chance because *"`B10.51`'s (3) already puts the believed-chance error there"*. This design keeps that cut and names the owner:

```
risk'(p, c) = − risk_gain · exposed(c) · (1 − misjudged chance(p, c)) · (1 + bands_below(p)) · nerve(p) · (1 − appetite(p))
```

| factor | quantity | attribute or trait read | owner |
|---|---|---|---|
| `exposed` | what the act stakes | none (the row's `contests:`) | `B10.31` |
| `misjudged chance` | how likely he thinks he is to come through, and how wrong | Reason, Focus | `misjudged` (this design) |
| `bands_below` | how hurt he already is | none (his body) | `decision/budget.py::body_band_penalty` |
| `nerve` | how far he bears a danger | Spirit | `B10.31`'s `choice_exposure` row |
| `appetite` | how much he will stake on a chance | `cautious_bold` (stored) | `B10.53` §11.1 (1b) |

Each attribute or trait sits in exactly one factor; the chance has one perturbation, and appetite never touches a chance. Appetite is a stable trait that tilts the weight; the error is a zero-centred misreading drawn each season. A cautious man who misreads a fight as safe will still go into it, and a bold one who reads it right will still weigh it lightly. Those are two different people, which is why both factors are kept.

**The reading rule for `forecast_spread`.** **The largest swept spread at which, at every one of seeds 0 to 2, the error moves the score top of low-Reason persons (Reason 1 to 2) strictly more often than that of high-Reason persons (Reason 5 to 6).** The error is worth having only while it separates persons by Reason. A spread past that point is noise that blurs persons into one another, and τ already supplies that noise (step 4, `B10.29`'s direction-against-control form).

**The sweep** (`cr93_probe.py season <seed> 1 0 <spread> 0.5`, i.e. with (1)'s `believed_all` on so that drawn tasks are priced too, `forecast_gain` −0.5; "moved" counts the deliberations with a chance-priced candidate whose score top under the misjudged chance differs from the top under the exact one, both read in the same `watch` call):

| seed | spread | moved, low Reason | moved, high Reason | low > high? | resolved acts | hash |
|---|---|---|---|---|---|---|
| 0 | 0.5 | 4/109 = 0.037 | 2/122 = 0.016 | yes | 619 | `1a28ecce…` |
| 0 | 1.0 | 4/108 = 0.037 | 5/121 = 0.041 | **no** | 620 | `c7166db4…` |
| 0 | 2.0 | 4/106 = 0.038 | 11/119 = 0.092 | **no** | 618 | `1ee2c070…` |
| 1 | 0.5 | 15/103 = 0.146 | 3/118 = 0.025 | yes | 658 | `88b9c7f2…` |
| 1 | 1.0 | 14/102 = 0.137 | 5/117 = 0.043 | yes | 653 | `40823b85…` |
| 1 | 2.0 | 15/103 = 0.146 | 7/118 = 0.059 | yes | 666 | `16743f97…` |
| 2 | 0.5 | 8/143 = 0.056 | 6/112 = 0.054 | yes (by 0.002) | 627 | `388233a2…` |
| 2 | 1.0 | 7/142 = 0.049 | 10/116 = 0.086 | **no** | 627 | `7cde450e…` |
| 2 | 2.0 | 7/141 = 0.050 | 11/116 = 0.095 | **no** | 634 | `58750d94…` |

**Read: `forecast_spread = 0.5`**, the only swept value that passes at all three seeds; at 1.0 and 2.0 the high-Reason group's tops move more often at seeds 0 and 2. **The pass is thin:** seed 2 holds by 0.002 on counts of 8 and 6, and the reach is small (2 to 15 per cent of priced deliberations). The build ships `forecast_spread` 0 (the control) and the flip re-reads this table; if 0.5 fails it at any seed then, the error ships at 0 and the value becomes a remaining question `[ASSUMPTION; Jordan to correct; revert: 0]`. `forecast_gain` −0.5 was **not swept**; it is taken equal to §2's read value of the same form `[ASSUMPTION; Jordan to correct]`.

**Falsifier (3).** (i) Two hand-built persons with equal pursuits, one at Reason 1 and Focus 1 and one at 7 and 7, one question with one contested candidate (`argue` on the same hearer), at `forecast_spread` > 0, over twenty draw seeds: the low person's factor departs from the exact chance by more on average, and his top departs from the exact-chance top more often (`assert checked >= 20`); at spread 0 both read the exact chance and rank identically. (ii) *One owner:* with `forecast_spread` > 0 and `risk_gain` > 0, for one exposed candidate, the chance `odds_weight` reads and the chance `risk` reads are the same misjudged value. **Planted failure:** `risk` reading the raw `View.odds` makes them differ, and the test goes red. (iii) A `None` chance and a candidate whose row is neither contested nor drawn score identically at every spread. (iv) `grep -n '"belief:' engine/season` names one site, `misjudged`.
**Control (3).** `forecast_spread` 0: `misjudged` returns the query object itself (identity, not a wrapper that recomputes), so the one-season hash equals the base at seeds 0 to 2 (the stand-in at 0 reproduced all three).

---

## 4. Obligations and demands: CR-88's, no term here

AR-04 lists *"obligations demands"* among what a choice weighs. **This design adds no term for them.** Their owner is CR-88's design, `B21d.01` (`proposals/v12_B21d_duty_of_office.md`, not in the tree at `43da21c37`; workplan `valoria_master_workplan_v12_part29.md:71-85`): the duty decline, the betrayal reading (`person_q.grievance_against`), the pricing of `accept` for an office-holder (AR-52), and its item (3) restated as `B10.30`'s `aim` on the goal that raised the question. (1) to (3) above compose with whatever CR-88 builds without an edit, because they act on the chance and on τ, never on what is wanted: a duty-raised candidate that is contested or drawn is priced by (1) and misjudged by (3) like any other.

**Falsifier (4).** `B10.80`'s diff (this design's build) adds a reader of an obligation or a demand: a read of `commit` tenures, `oblige`, `person.demanded`, a seat's duty or `grievance_against` under `decision/` (grep of the build's diff). **Control (4).** The build's diff touches no reader CR-88's design names; `B21d.01`'s gate is its own.

---

## 5. What the build (`B10.80`, HELD) changes, its controls and its hash

Stated for the build's author, not done here. Each term ships at its neutral value, so the build is **HASH EQUAL**; each flip is a declared mover of every seeded choice (v11's HASH MOVERS line), scheduled at B98.

| term | code | data | ships at | flips to |
|---|---|---|---|---|
| (1) drawn-task weight | `choose.py`: the share-step predicate beside `_writing_bands`; one branch in `odds_weight` | `rosters.yaml: odds_weightings` gains `believed_all` | `odds_weighting` `believed` | `believed_all` |
| (2) temper | `B10.28` (lands first) | `B10.28`'s row and `temper_gain` | 0 | −0.5 |
| (3) forecast error | `choose.py::misjudged`; `make_ranker` wraps `odds` once; the harness readers that score outside `choose` (`harness/decision_spread.py::attribute_top`'s caller, `harness/interactions.py`) call the same function or read a different figure | `capability_use_sites: choice_forecast`; two `capability_uses` rows; fixtures `forecast_spread`, `forecast_gain`, each with a hole-register row | `forecast_spread` 0 | 0.5 (re-read first) |

**Order.** (2) is `B10.28`'s. (3)'s falsifier (ii) needs `B10.31`'s `risk`; if `B10.80` lands first, (ii) is written against `odds_weight` and `aim` and is extended when `risk` lands. `capability_factor`, which `B10.28` and `B10.31` name, is `_judgement_factor` in the tree (premise correction 2); the build either names `_judgement_factor` or adds the public name as a call, not a copy.

**The control, all terms together (v11's EXIT, copied).** *"Every term at neutral reproduces the base hash at seeds 0-2"*: `6e3a066a9d4b921bf5258a23b55d0e37`, `01f7f9aa0f3d9a52242ea78c8c92cc23`, `0a00352e0e9349f8c12d26f8f9e7e467`, read on the build's own base, which later EQUAL items may have re-read.

---

## 6. The NERS cut test (`skills/ners`, instrument A only, compact)

Run on each object against `CLAUDE.md` §0.06. No draw is *resolved* by these terms (they shape a choice, not an outcome), so `resolution-diagnostic` (instrument B) was not run. This is the cut question per object, not the full §2–§9 ledger.

- **N, cut (1).** What dies: a person's competence stops reaching any act he does alone; a scholar and a dullard weigh `reconstruct` alike, and drawn tasks stay weighed as certain beside contested acts weighed by their chance (measured: the base resolves 16 to 19 per cent more drawn-task acts than the arm that prices them, §1). *Attacked as a false N-line* ("the pool already carries skill"): the pool reaches the roll, not the choice, so it fails as an attack. The cut is not free. **Residual:** reach is only the drawn rows (`graded_tasks`); a skill on a flat row stays unread, by design.
- **N, cut (2).** What dies: AR-23's distraction, and every person draws at one temperature. *Attacked as covered by (3):* (3) reaches only chance-priced candidates (2 to 15 per cent of priced deliberations moved), so it fails as an attack. **Residual:** the realm holds no Focus 7, so the pole is read on hand-built persons only.
- **N, cut (3).** What dies: Reason's only season reader (`attribute-rulings-adjudication.md:31`: *"Nothing in the season reads Reason"*), and a misjudged fight. *Attacked as covered by appetite:* appetite is a stable tilt on danger, not a zero-centred misreading of a chance, and reads no attribute, so it fails as an attack. **Residual:** the measured separation is thin (§3); N holds on the ruling and the pair falsifier more than on the realm reading.
- **R.** (1) gives authored skill and attributes a consequence in what a person *does*, not only in how it lands (customisation; R-world: unwatched persons shy from the tasks they are likeliest to fail, `reconstruct` and `forge` most, §1). (3) makes one person's error co-move his gain and his danger, so a misjudged duel follows from his Reason without being scripted. **Residual:** at the read values (2) and (3) move the season's hash but not its shape (acts within ±5 per cent, §2, §3).
- **S.** Methodology: (1) is the existing believed-chance factor and (3) is one perturbation of that one chance, so there is no second ladder anywhere. *Pauses correctly:* each term acts inside `score_terms` or `_sample_order` and nowhere in the fold. *Across scales:* `march` (a field) is contested and priced by the same `odds_weight`, so (3) reaches it with no new seam. **Residual:** the field's estimate is mode (a) only (`sigma.py:963-967`), so a believer's `march` chance is `None` today, and (3) leaves it alone.
- **E, last, as a ratio.** Against what N and R found, the design adds: one roster member and one predicate for (1); for (2), nothing beyond `B10.28`; for (3), one function, one site, two rows and two fixtures. There are no new carriers, no new weight vector, and no new attribute read outside the uses table. *Remove more:* dropping `forecast_gain` (fixing `s` to Reason alone) loses AR-21's Focus clause, so it is not free. **Verdict: passes, on the trail above.** The weakest point is (3)'s realm-level coefficient, not its structure.

---

## 7. Takes, each reverting alone, and what only the orchestrator or Jordan can decide

**For the orchestrator (a conflict between plan items).**
1. **The sign of `temper_gain`** (§2): `B10.28`'s tests say `temper_gain > 0` and AR-23 then needs `< 0` under `about_mid`. This design takes a negative gain, keeping `_judgement_factor` unchanged. `B10.28`'s test text needs the sign flipped before it is built. The other fix is to negate the gain inside `temper`, which gives two conventions for one row form.
2. **`capability_factor`** in `B10.28` and `B10.31` names a function the tree spells `_judgement_factor` (premise correction 2).

**Remaining questions (Jordan to correct; each reverts alone).**
3. `forecast_spread` 0.5 is a thin pass (§3); `forecast_gain` −0.5 was not swept.
4. The name `believed_all` (§1); an inquiry priced by `task_fraction` (§1); effort not offered on a drawn task (§1).
5. A chance of exactly 0 or 1 is not misjudged (§3).
6. **The player's sheet.** `decision/sheet.py` shows the player `View.odds` per candidate (`:146-147`), the exact belief, while the order it offers comes from `make_ranker` and so reads the misjudged chance. Taken: the sheet shows what the ranker reads, through the same `misjudged`, so a player character's Reason matters to the player as it does to the person `[ASSUMPTION; Jordan to correct; revert: the player sees the exact belief, and Reason binds only unplayed persons]`.
7. **Read for `B10.31`, not changed here.** Its "stated limit" (every bodily candidate's chance is `None`) predates B14.24's route: `believed_chance` now answers a row whose prize provider registered a `believed_estimate` (`personal_combat`'s) from that provider (`sigma.py:1006-1018`). Whether the bands `risk` asks are on that provider's ladder is for `B10.31`'s build to read. If they are, (3) reaches `fight` through `risk` from the first flip.

