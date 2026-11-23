# Capability, ambition, values and personality, v2: ten axes, fifteen traits and the attribute readers

## Status: PROPOSED — HELD BACK IN FULL; reconstructed from a digest, not from the original file; where this file and a re-derivation from the tree disagree the tree wins
## Lane: IN. IDs: none allocated.
## Reconstructed 2026-10-30 from a digest. Original `layers_v2.md` (session of 2026-10-24/25): LOST
## Builds on: `proposals/2026-10-24-character-layers-capability-ambition-values-personality.md` (v1, committed through PR #505; superseded in part by this file) · `engine/season/queries/world_q.py` (`questions_for`) · `modules/combat/combatant.py`, `modules/combat/config.py` · `engine/season/loop/effects_combat.py` · `engine/season/data/fixtures.py` · `proposals/2026-09-16-conviction-decision-layer/adjudication_register.yaml` · `proposals/2026-10-24-character-progression-adjudication.md`

**How this file was produced, and what it is not.** The design below was worked in a session of 2026-10-24/25 whose file `layers_v2.md` was never committed and cannot be recovered. A read-only extraction agent later wrote a digest of that session's own closing summary (timestamp 2026-10-25T02:43Z); this file restates the digest and nothing else. It adds no number, no mechanism and no file reference that the digest does not carry. Every figure, count and `path:line` below is the session's, was not re-opened for this reconstruction, and may be stale: the digest itself records that several figures the session trusted turned out to be stale. This is reference under CLAUDE.md §0.05: prose is not a mechanism, and merging it ratifies nothing. The session's closing line was *"Tell me if you want the v2 design landed as a replacement"*, and the transcript holds no answer from Jordan; so this file is a record of a design exercise, not a landing of v2.

**Amended 2026-11-23 in place (workplan v12 `B10.53`; E5 Block D4: "the lane amends it, it does not fork it").** §11 is new and is NOT from the digest: it was worked against the tree at the amendment's base, and every figure in it is either a command's quoted output or marked `[ASSUMPTION; Jordan to correct]`. Where §11 and §1–§10 disagree, §11 is the later reading; §1–§10 stand as the digest's record. The `## Status:` line above is unchanged (held until merge).

**Why v1 is stale.** v1 was committed through PR #505 (merged, held back) and still carries cuts that Jordan withdrew on 2026-10-25 (02:17Z): *"don't cut anything because there isn't a code reader yet. that's what we can build."* and *"treat as design exercise"*. v1 remains in the tree unedited except for a pointer on its Status line.

---

## 1. The layer cut

One question tells each layer apart.

| layer | question | what it decides |
|---|---|---|
| **Capability** | does more always help the outcome? | how a verb lands; the resolver only |
| **Ambition** | could some state of the world satisfy it and end the wanting? | which content is on the plate; it commits to OUGHT propositions (`goals.yaml`, landed claims) and feeds five standing occasions, through `questions_for` (`world_q.py:2717`) |
| **Values** | is it a direction nothing finishes, held as a weight? | the fifteen pursuits and the readout axes |
| **Personality** | does it vary independently of values, leave odds untouched, and have no pole that always wins? | manner |

Constraint carried from the tree: ED-IN-0261's ruled sentence (R7's dissolution clause; R7 itself is a result in `proposals/2026-09-16-conviction-decision-layer/formal_analysis.md:195`) says projected axes are linear in pursuit weights, so identical weights give identical axes (*"two people with identical pursuits ARE identically disposed and the variation comes from the candidates"*). v2's stored-offset axes would contradict that sentence (§2, §3); they are held for Jordan (workplan v10 `-10` E-4).

---

## 2. What v2 changes against v1

v1 is `proposals/2026-10-24-character-layers-capability-ambition-values-personality.md`. The digest does not say which v1 sentences v2 rewrites; the mapping below is this reconstruction's reading of the digest against v1's §2 and §5, and each row says how v2 differs.

| v1 §2 / §5 row (quoted) | v1 says | what v2 does |
|---|---|---|
| §2, ED-IN-0261, R7's dissolution clause: *"two people with identical pursuits ARE identically disposed and the variation comes from the candidates"* | "**Overridden for three axes.** Persons with identical pursuits may differ on `rigid_flexible`, `grandiose_humble` and `deontological_instrumental`." | Would be contradicted on the stored-offset axes (held, `-10` E-4), now six of the ten: those three plus the three new personality-only axes (`cautious_bold`, `hasty_patient`, `conciliatory_coercive`). The four value readouts stay at spread 0. |
| §2, the deontology gate: *"the weighting is a threshold for certain actions"* | "**Narrowed.** The gate stays and stays dormant (`refusal_axis` ships unset). Its tolerance, when armed, becomes prior plus offset. The gate's own convention is a separate matter." | The convention becomes an open owner call (§9, call 4): the dormant refusal gate refuses by `a > tolerance`, and `refusal_axis` ships unset (`fixtures.py:749`, H-146's), and that convention cannot carry the new one-signed axes. |
| §2, Jordan 2026-09-17: *"these four are value-frames (what is right), the seven are bearing"* | "**Narrowed.** Of the live seven, three are bearing in the sense that they can vary at fixed ends." | Not restated by the digest as a change, except through open call 1, which concerns whether `selfish_selfless` becomes a stored seventh manner axis, siding with the 2026-09-17 Borgia example (`adjudication_register.yaml:242-249`). |
| §2, SE-06 / ED-IN-0296 (cohorts hold no pursuits, `needs_jordan`) | "**Not pre-empted.** Cohorts read personality as 0 until that ruling is answered." | Unchanged in substance: cohorts and minted persons read 0 because they hold no pursuits (SE-06 / ED-IN-0296 open); the layer applies only where values exist. |
| §1 and §5, "It adds no per-verb cell and no new reader" and "does not design vindictiveness, boldness or patience" | boldness and patience out at v1's HEAD; `forgiving_vindictive` "**out, dead reader**" | v2 designs all three, and adds per-verb cells to do it: `cautious_bold` is derived from verb-table exposure and `hasty_patient` is declared per verb (§3), against v1's "no per-verb cell". Vindictiveness is cut in v1 as dead-as-specified (the grudge row is keyed on a faction name, `effects_combat.py:311-313`, that no candidate subject reaches); v2 restores it as `forgiving_vindictive`, with the referent question (moving the grudge referent to a person) left open. This follows Jordan's 2026-10-25 rule against cutting for want of a reader. |
| §5, `Combatant.disp` "not mapped" | a combat-local lean, left unmapped | Still unmapped. v2 names it as the in-tree template (per person, three hooks, a cost at each pole; `modules/combat/combatant.py:94-99`, `config.py:273-279`) and as two ladders for one trait family. |
| §5, "`stance_gain` … out" and "candour, discretion, credulity, dogmatism … not tested [GAP]" | out / not tested | v2's census (§4) lists candour, discretion, credulity and dogmatism among the pairs where both halves exist, and rules `rank_gain`, `regard_gain` and `stance_gain` out by test (§7), the digest's reason being that they are entailed by priors. Which of the nine gain traits of §4 corresponds to which v1 candidate is not stated in the digest. |
| §4, spreads: "one corpus standard deviation of the authored prior, rounded up to the next 0.05" | ±0.15 on three axes | Carried: ±0.15, described by the digest as one measured corpus standard deviation (sd 0.12, 0.11 and 0.15 over 46 authored rows). |

Rows of v1 §2 that the digest says nothing about (R3 "best design wins"; R1/R2 conviction and the scar model; `bend_price` / `drift_rate`) are left as v1 has them.

---

## 3. The ten axes

| group | axes | spread |
|---|---|---|
| Four value readouts | `hierarchical_equal`, `precedent_substantive`, `partisan_equitable`, `selfish_selfless` | 0 |
| Three prior-plus-offset | `rigid_flexible`, `grandiose_humble`, `deontological_instrumental` | ±0.15 (sd 0.12, 0.11, 0.15 over 46 authored rows) |
| Three new, personality-only | `cautious_bold`, `hasty_patient`, `conciliatory_coercive` | not stated in the digest |

- `cautious_bold` is derived from verb-table exposure (12 of 56 verbs).
- `hasty_patient` is declared per verb (13 delay cases).
- `conciliatory_coercive` is declared per verb.
- `selfish_selfless` is to be derived from the declared `beneficiary` column (25 actor, 11 subject, 20 none), building the unbuilt `benefits_me` term. Whether it stays at spread 0 (the draft's choice) is open call 1. In the tree as the session read it, `selfish_selfless` has no nonzero cell on any verb (§8).

---

## 4. The fifteen personality traits

Fifteen traits in two kinds.

- **Six manner offsets**, which are the axes of §3 that carry a stored offset: `rigid_flexible`, `grandiose_humble`, `deontological_instrumental`, `cautious_bold`, `hasty_patient`, `conciliatory_coercive`.
- **Nine "gain" traits**, each a per-person copy of an existing global setting: `forgiving_vindictive`, `trusting_sceptical`, `open_dogmatic`, `guarded_open`, `steadfast_malleable`, `callous_scrupulous`, `serene_torn`, `frugal_lavish`, `steady_capricious`.

The session's census of "both halves exist" trait pairs, all global except combat's (the gain traits above come from here):

- vindictiveness (`field_grudge_weight` = 1; `stance_gain` = 1.0, `stance_polarity` = "legacy"),
- plasticity of values (`pursuit_shift`),
- conscience (scar thresholds),
- candour, discretion, credulity, dogmatism,
- aggression and caution.

One half only: decisiveness (`choice_temperature` = 0.1), energy (`scene_budget` = 5), tolerance for inner conflict (`confliction_weight` = 0), temper, generosity.

Capacities, not personality: memory (`claim_decay_per_season` = 5, `ledger_cap` = 200, `view_k` = 12), the untrained floor (`pool_default` = 2), forgery.

---

## 5. The attribute readers

v2 gives the attributes non-dice readers. The six are Fable-adjudicated (Body, Hand, Wit, Nerve, Presence, Sense) and immutable in play.

| attribute | reads |
|---|---|
| Body | budget base and combat strength |
| Hand | forgery quality and combat agility |
| Wit | Recall: `claim_decay_per_season`, `ledger_cap`, `view_k` |
| Nerve | wound-band penalty and combat spirit |
| Sense | Watchfulness and `record_gain` |
| Presence | none |

The progression adjudication (merged PR #505) recorded nine corrections (C-1 to C-9), including C-8, name collisions: "Body" against `Person.body`, and "Presence" being a registry alias of Charisma. Its open gaps, as the digest lists them: where Thread Sensitivity sits among the six; floors and ceilings for persons with no authored row; the mapping of the registry's `stats:` onto the six; the decay period N; and an unresolved tension, that the adjudication keeps Nerve while Jordan's decision-matrix comparison argues Nerve belongs to the chooser.

---

## 6. The sorting rule

**A trait whose effect varies by VERB is an axis; a trait whose effect varies by claim, stance row, deposit or scar is a per-person copy of an existing global setting.**

That is the rule that puts `cautious_bold`, `hasty_patient` and `conciliatory_coercive` among the axes (§3) and the nine traits of §4 among the gains.

---

## 7. What stays out, by test

- Anger display: it changes contest odds.
- Warmth's caring half: entailed by love, family and stewardship.
- `rank_gain`, `regard_gain`, `stance_gain`: entailed by priors.

Cohorts and minted persons read 0: they hold no pursuits (SE-06 / ED-IN-0296 open), and the layer applies only where values exist.

---

## 8. Limits, and what the session did not check

**Worked example [MEASURED by the session].** Two persons with identical pursuits, A at `cautious_bold` −1 and B at +1. Chance of landing a duel (`accept`) in the top five: control 0.208, A 0.130, B 0.324. Expected exposed acts among five: 1.07 (control), 0.82 (A), 1.39 (B). Today's code gives both persons the control row.

**Not checked by the session:** the gain reader sites, the Recall sites, the 112 one-word cells, and the correlation. "17 changed read sites" is the producer's count and was not verified.

**Findings the session recorded as bearing on the plan (its own ranking):**

1. People barely differ in outcomes: capability is empty for 429 of 430 corpus persons, only `tell` and `speak` read it, and the combat seam takes only `end`. "Any attribute or progression design is moot until the seam reads more of the person."
2. Characters barely differ in choice: candidate gaps are 0.01 to 0.06 at tau 0.1, the top candidate reaches the top five 41% of the time, and the stance term is −8.0 on every candidate. A bold person took a duel 32% of the time against 13% for a cautious one with identical pursuits.
3. Much built machinery is inert: `selfish_selfless` has no nonzero cell on any verb; the refusal gate is dormant; `confliction_weight`, `intent_disclosure`, `telling_privacy`, `age_step` and `illness_rate` ship at 0; `succeed` is declined; `march` is the only writer of stance and its grudge row names a faction no candidate reaches; cohorts hold no pursuits (246 of 638 season-1 acts scored 0 on values); arrest, raze and sabotage have no alignment cell. The session's conclusion: "Wiring what exists comes before adding new layers."
4. The growth loop has no start and no exit: `train` raises a key only if already held, 429 of 430 hold none, nothing lowers capability, age hazards ship at 0, and `succeed` is declined.
5. Several trusted figures were stale; re-measure with `decision_spread` and `m1_acceptance`.

Every figure above is the session's, as the digest reports it, and was not reproduced for this file.

---

## 9. Open owner calls (the four the session named)

1. **`selfish_selfless`.** Whether it stays at spread 0 (the draft's choice) or becomes a stored seventh manner axis, siding with the 2026-09-17 Borgia example in `adjudication_register.yaml:242-249`.
2. **`choice_temperature`.** The shipped tau of 0.1 swallows personality: candidate gaps are 0.01 to 0.06, so a ±0.06 trait term shifts odds by 1.5 to 2.5 times but does not change decisions. A recognisable bold character needs tau, or the spreads, to move; spreads several times the prior's sd would decide alone. This relates to CR-17's last commit, the tau re-derivation, and to ED-IN-0304.
3. **The declared per-verb columns.** `payoff` and `force` are judgment cells nobody has argued.
4. **The refusal gate's convention.** The dormant gate refuses by `a > tolerance`; `refusal_axis` ships unset (`fixtures.py:749`; H-146's). That convention cannot carry the new one-signed axes.

---

## 10. Falsifiers

The digest carries none for v2. These are v1's §9 falsifiers, taken from the committed v1 as written. Each names a quantity that v2 changes (ten axes in place of seven, six stored offsets in place of three), so each is to be restated at v2's numbers; none is evidence about v2 as it stands.

- **Capability.** [CARRIED FROM v1 §9, to be restated at v2's numbers] A capability key appears in `score_terms`, or a personality value changes a contest's odds.
- **Ambition.** [CARRIED FROM v1 §9, to be restated at v2's numbers] A person with no live commit and no landed claim forms a question from values alone. Then values are forming content and the layer line is wrong.
- **Values and the spread-0 axes.** [CARRIED FROM v1 §9, to be restated at v2's numbers] A cast pair with near-identical pursuits whom the authors insist differ on `hierarchical_equal` or `precedent_substantive`, where no commit expresses the difference. The fix is one cell.
- **Personality (a).** [CARRIED FROM v1 §9, to be restated at v2's numbers] At spread 0, `World.content_hash()` differs from today's for the same seed. Then the control is not a control. (v1 held this true by having the likeness readers read the prior over all seven columns; that clause is v1's.)
- **Personality (b).** [CARRIED FROM v1 §9, to be restated at v2's numbers] At live spread, an n-seed `engine/season/harness/decision_spread.py --arms` comparison shows no decision moved. Then personality is inert. (`harness/arms.py` is `field_casualty_model`-only, CLAUDE.md §7, and is not the instrument.)
- **Personality (c).** [CARRIED FROM v1 §9, to be restated at v2's numbers] One pole of a trait wins across the corpus on any outcome measure. Then it is a hidden capability. (v1 named `deontological_instrumental` as the likeliest to show this; v2 adds axes v1 never tested for it.)

---

## 11. The personality layer's design: risk appetite, decision horizon, the beneficiary cells, `selfish_selfless` (B10.53)

**What this section answers.** CL-PERSON's design half (ratified as a DESIGN-FIRST row, ED-IN-0305), M34's open question, M36 and M40, in the order of E5 Block D4's "Must contain" (copied into workplan v12 `B10.53`; `master/eval/E5.md` itself is not in the tree, so the copy in the workplan entry is the text worked from). Rulings read: ED-IN-0304 (risk appetite and decision horizon; the bands), ED-IN-0261 as narrowed by A-108 (stored manner offsets allowed on `rigid_flexible`, `grandiose_humble`, `deontological_instrumental`), ED-IN-0305. Each choice is argued on the `needs_jordan` ladder of CLAUDE.md §0 (1 superseded, 2 irrelevant, 3 a design document, 4 precedent, 5 what suits the architecture) and names its step, or is marked a remaining question. Code is the mechanism; nothing here binds the game until `B10.82` (HELD) builds it.

**Block D4's N-line rule, copied:** "Any trait beyond those two that the design cannot tie to a reader is cut." *Those two* are read as risk appetite and decision horizon, ED-IN-0304's two terms `[ASSUMPTION; Jordan to correct: E5 Block D4's surrounding text is not in the tree]`. §11.4 applies it.

**The tree this section was worked against** (each line a command run at the amendment's base, `43da21c37`):

- `choose.score_terms` returns `(pursuit, stance, fit)` (`engine/season/decision/choose.py:252`). `aim` (`B10.30`) and `risk` (`B10.31`) are not yet in the tuple; both are cited here as PROPOSED, first-half items.
- `choice_temperature=0.05` (`engine/season/data/fixtures.py:292`). §8 and §9 call 2 above quote 0.1: stale.
- `odds_weighting="believed"` ships (`fixtures.py:888`, CR-17).
- The verb table: 67 rows. `beneficiary`: actor 28, none 28, subject 8, to 3. Rows contesting a bodily prize (`contests:` `the body` or `a field`): `fight`, `capture`, `accept`, `march` (4). §3 above quotes "12 of 56" and "25 actor, 11 subject, 20 none": stale. Command: `python3 -c` over `engine.season.data.verbs.VERB_TABLE` (counts of `.beneficiary`, `.contests`).
- `selfish_selfless` alignment cells: `{'fight': -0.3, 'accept': -0.3}` (CR-87's cost of violence; `rosters.yaml:4241` declares every other cell null because "the per-candidate fact 'for whom' is single-owned by `verb_table.yaml`'s `beneficiary:` column"). §8's "no nonzero cell on any verb" is stale by these two.
- `goals.yaml` carries no stage `term:` line (`grep -n "term:" engine/season/goals.yaml` returns nothing); the roster `goal_stage_terms: [short, medium, long]` exists (`rosters.yaml:2364`, CL-THRUST B2.2) and "carries no length of time".
- `refusal_axis=None` ships (`fixtures.py:780`); `decision/options.py::refusal_tolerance` reads `project(p)[axis]`, and `project` is `projected_axes(p, 0)`.

### 11.1 M40: the risk term and the horizon term

**The one owner of risk.** `02_CHAR_what_an_act_risks` (first half, `B10.31`, PROPOSED) builds the cost of danger as the fourth element of `score_terms`:

```
risk(p, c) = − risk_gain · exposed(c) · (1 − chance(p, c)) · (1 + bands_below(p)) · nerve(p)
```

and says: "Appetite is not in this term and is not a skill … when M40 answers where it is carried, it multiplies `risk` at this site and nowhere else". This design takes that site. **The one owner of risk is `decision/choose.py::score_terms`' `risk` element; nothing else in the chooser prices danger to the actor.** `B10.51`'s (3), the error on the believed chance that Reason shrinks and low Focus widens, acts on `chance(p, c)`, the term's *input*; appetite acts on the term's *weight*. One term, five factors, each from one place: the prize (`exposed`, the row), the belief (`chance`, `View.odds`, with `B10.51`'s error on it), the body (`bands_below`), the skill (`nerve`, Spirit through `capability_factor`) and the temperament (`appetite`, below). Not two ladders.

**(1a) What the risk term multiplies.** The workplan's candidate input is "the believed-odds-weighted alignment of CR-17 commit 1", i.e. appetite reshaping `odds_weight` on the pursuit term (a bold man discounts his doubt about a gain). **Rejected, step 4 (precedent) and step 5:** `odds_weight` is the one place a believed chance prices a *gain*, and `B10.51`'s (3) already puts the believed-chance error there; an appetite exponent on the same chance would be a second ladder for one quantity (NERS S, "calculations consistent in methodology"), and it would reach every contested row (`argue`, `determine`, …) where nothing bodily is staked. **Chosen:** appetite multiplies `risk`:

```
risk'(p, c) = risk(p, c) · (1 − appetite(p))          appetite(p) ∈ [−1, 1]
```

At `appetite` 0 the factor is 1 and `risk'` is `B10.31`'s term exactly (the neutral control). At +1 a person ignores the danger in his ranking (the danger itself still lands in the fold: wounds, a lost field, so the pole has a cost and does not always win); at −1 he weighs it double. A value outside `[−1, 1]` is refused at load: below −1 is harmless arithmetic but unbounded, above +1 inverts the term into a pull toward danger.

**(1b) Where appetite comes from. Step 5.** The four options the instruction names:

| source | verdict |
|---|---|
| a creation-time per-person value | **chosen**: a stored value per person, `appetite` = his own value on `cautious_bold`, absent = 0 |
| a derivation from pursuits | not chosen now: it needs a 15-cell `cautious_bold` column in `tables.pursuit_projection` that nobody has argued, and would make appetite linear in pursuits, so two persons with the same pursuits could not differ in it, which is what ED-IN-0304 (1) reverses ("persons differ in risk appetite as well as …") |
| a derivation from convictions | the same as pursuits (`Person.convictions` → `pursuits`, ED-IN-0261) |
| a derivation from scars | rejected: `Person.scar[axis]` is kept per pursuit axis (Layer 1 §B.2), a mark on his convictions, not on his body; the body is already in the term (`bands_below`), so a scar-derived appetite would either invent a mapping or count the body twice |

The stored value follows A-108's shape (manner = what pursuits project + his own offset) with the projected part absent: no projection column ships, so `appetite(p) = manner_offset["cautious_bold"]`. **Remaining question (the carrier):** Layer 1 §B.2 defines `manner_offset?` as "a stored offset per manner axis, added to what `pursuits` project" (`architecture/meta/04_CODE_ARCHITECTURE.md:241`); `cautious_bold` is not on `pursuit_axes`, so either that clause is read to include an axis with no projection (projected part 0) or the build needs a Layer 1 node. The design picks the first reading; it is the orchestrator's (or Jordan's) to confirm before `B10.82`.

**(1c) Per person or per verb.** Appetite is **per person**. The per-verb half is `exposed(c)`, already read off the row's own `contests:` column by `B10.31` (no new column, §11.2). Nothing about appetite is declared per verb.

**(1d) The horizon term. Steps 3 and 4.** ED-IN-0304 (2): "short time horizon means that the person is choosing to get the best results within the current season or the season after. medium term is within three to four seasons. long term is anything five or more seasons." Read with the current season as the first, so that the ruled bands cover every count with no gap or overlap (the ledger row says they do):

| band | seasons ahead `d` (0 = the current season) |
|---|---|
| SHORT | 0, 1 |
| MEDIUM | 2, 3 |
| LONG | 4 or more |

The other reading (MEDIUM = 3 or 4 seasons *ahead*) leaves `d = 2` in no band, and is rejected by the row's own "without gap or overlap".

*What lands later.* Every act the fold resolves writes in the season it resolves; no verb-row field says an act's good arrives later (`VerbRow` has no such field; see §11.2's `payoff`). The one carrier in the tree of "how far ahead" is a goal stage's `term:` (`rosters.yaml: goal_stage_terms`, `[short, medium, long]`, the same three words, CL-THRUST B2.2, step 4 precedent). So the horizon weights **what an act does for a goal stage**, which is `aim` (`B10.30`, PROPOSED: "how much an act serves the goal that raised the question being answered"), by the term of the stage that goal is on (`world_q`'s first unpassed stage of the goal's `goal_stages` row):

```
aim'(p, c) = aim(p, c) · horizon_discount ^ max(0, rank(term) − rank(horizon(p)))
rank: short 0, medium 1, long 2
```

`horizon(p)` is a member of `goal_stage_terms`, **per person** (ED-IN-0304: persons differ in it), stored at creation, absent = `long`. `horizon_discount` is a fixture in `[0, 1]`, shipped `1.0`. A stage at or inside his horizon weighs in full; each band beyond it multiplies by the discount once. At the shipped `1.0` every weight is 1, and an unauthored person (`long`) weighs 1 at any discount: two separate neutral controls. The ruled season counts above are the meaning of each `term:` word for an author choosing a stage's term; no reader holds a season count `d` today, so no `band_of(d)` function is proposed (one would be built with its first reader).

*The pursuit and stance terms are not discounted*: they price what the act itself does, which lands this season (SHORT). `[ASSUMPTION; Jordan to correct: a multi-season act, if one exists, would land later than its season; none is named in the verb table]`.

**Remaining question (the carrier, again):** a horizon is a band, and `manner_offset?` is numeric. Either `hasty_patient` is stored as a number with fixed cut points into the three bands, or the build needs a Layer 1 node for a band-valued field. Not decided here.

**Measured reach of the horizon term:** none at ship, by construction: no `goal_stages` row ships and `aim` is not in the tree, so the term multiplies nothing until stages are authored. Its decision shift is a remaining question, to be read where stages land.

**Falsifiers (1).** (i) At `risk_gain` > 0, appetite changes the rank of any candidate whose row contests no bodily prize (the factor leaked off its term). (ii) At `risk_gain` > 0, persons at `appetite` −1 and +1 rank an exposed candidate alike (appetite does not reach the term). (iii) At `horizon_discount` < 1, an unauthored (`long`) person ranks differently from the shipped chooser (the neutral is broken). (iv) A `short` and a `long` person, identical otherwise, rank a candidate serving a `long`-term stage alike at `horizon_discount` < 1 (the horizon does not reach `aim`). (v) Some `d` ≥ 0 falls in no band or in two.

### 11.2 M36: the per-verb columns

The digest's columns (§3, §9 call 3) were four: exposure for `cautious_bold`, a delay or `payoff` for `hasty_patient`, `force` for `conciliatory_coercive`, and `beneficiary` for `selfish_selfless`. The rule (Block D4): derived from an existing verb-row field where one says it; declared under a stated rule where none does, each declared cell `[ASSUMPTION]`.

| column | an existing field that says it? | disposition |
|---|---|---|
| exposure | **yes**: `contests:` ∈ `rosters.yaml: bodily_prizes` (`B10.31`) | **derived, no new column**: `exposed(c)` reads it (4 rows today) |
| `payoff` (when the act's good lands) | no | **no column**: the horizon reads the goal stage's `term:` (§11.1 (1d)); a per-verb payoff band would be 67 judgment cells to say what the fold already says (every act writes in its own season) |
| `force` | no | **no column**: its only reader would be `conciliatory_coercive`, cut by the N-line rule (§11.4) |
| `beneficiary` | **yes**: `verb_table.yaml: beneficiary:` (67 rows; `actor`, `subject`, `to`, `none`; the loader requires it on every row, `rosters.yaml` "`none` is a declaration, not a blank") | **derived, no new column**: read through `decision/choose.py::beneficiary_of(p, c)`, which exists and "no game code reads (tests only)" |

**So no column is added and no cell is declared.** M36's default in force ("no per-verb declared cells") stands, and no `[ASSUMPTION]` cell is owed.

**The beneficiary column's new owner.** REM-44 deleted `benefits_me` (`hole_register.yaml:832`). The column's reader is now a part of `score_terms`' `pursuit` sum on the one axis whose alignment row is null by design: for `selfish_selfless`, the cell the sum multiplies by `axis_w["selfish_selfless"]` is

```
self_other(p, c) = beneficiary_gain · ( −1  if beneficiary_of(p, c) == p.id
                                       +1  if it is another person
                                        0  if the row declares `none`, or a declared carrier did not bind )
```

added to the row's own alignment cell (the cost of violence on `fight`, `accept`). The sign follows the axis' own convention (`rosters.yaml`: "negative = for oneself · positive = for others"), so a person whose pursuits project selfish (`wealth` −0.6) is drawn to `beneficiary: actor` rows and a selfless one (`love` +0.7) to `subject`/`to` rows. `beneficiary_gain` is a fixture, shipped `0.0` (the control). Owner: `decision/choose.py::score_terms`, step 5: it is the axis term the alignment table's note says the column replaces, read where the axis is already read, and `beneficiary_of` stays the one resolver.

*Not the first half's `beneficiary` stance arm* (`B10.11`/`B10.69`, PROPOSED; not in the tree: `stance_polarities` has no `beneficiary` member at this base). That arm prices **whom** the act serves by the actor's regard for that person; `self_other` prices **self against others** by his disposition. Both read the same column through `beneficiary_of`; neither is a copy of the other (falsifier (2)(iii)).

**Falsifiers (2).** (i) `exposed(c)` and `contests:` ∈ `bodily_prizes` disagree on any row (a second copy grew). (ii) Any reader of the `beneficiary:` column other than through `beneficiary_of` (`grep -rn "\.beneficiary\b" engine/season --include=*.py` names a second site). (iii) With every regard 0, a selfish and a selfless person (opposite `selfish_selfless` projection) rank a `beneficiary: actor` row against a `beneficiary: to` row alike at `beneficiary_gain` > 0 (the term does not reach); or, with `beneficiary_gain` 0, the stance arm alone stops separating two persons of unequal regard (the two terms are not independent). (iv) `self_other` changes the score of a `beneficiary: none` row.

### 11.3 Spreads against CR-17's τ (M35)

The landed τ is `choice_temperature` 0.05. **The margins τ divides, measured** (built realm, no season; `outvoted margins' median` is the median gap the draw overrode):

```
$ python -m engine.season.harness.decision_spread --decisions --seed 0
  the draw's 201 tops, split: tie 4, outvoted 197; outvoted margins' median 0.0590 against choice_temperature 0.05
$ … --seed 1
  the draw's 212 tops, split: tie 2, outvoted 210; outvoted margins' median 0.0590 against choice_temperature 0.05
$ … --seed 2
  the draw's 204 tops, split: tie 3, outvoted 201; outvoted margins' median 0.0567 against choice_temperature 0.05
$ python -m engine.season.harness.decision_spread --season --seed 0
  acts 627 by 82 actors; … the draw's 161 tops, split: tie 13, outvoted 148; outvoted margins' median 0.0439 against choice_temperature 0.05
  content_hash 6e3a066a9d4b921bf5258a23b55d0e37
```

`--persons` (built realm) reads cosines, not decisions, and cannot observe a term: quoted only to say it was run (`persons 83 (cast 46, cohorts 37) … median cosine 0.3516`).

**The decision shift at a proposed spread (the V0-5 re-run).** No risk term is in the tree, so it was measured by a scratch probe, not kept: one season per arm at the same seed, `B10.31`'s term (with `chance` fixed at its `risk_unknown_chance` 0.5, the value every bodily candidate reads today, and `nerve` 1) times `(1 − appetite)`, added to `score_terms`' first element by wrapping the module global the chooser calls, with **every person at the same appetite** (a whole-realm arm, not the hand-built pair of (6)). Counted: resolved acts on the four exposed rows. `[ASSUMPTION: V0-5's own form is v11's and is not in the tree; this is a re-run of its question, a decision shift at the proposed spread]`.

| seed | arm | exposed acts resolved | acts | content hash |
|---|---|---|---|---|
| 0 | base, no wrap | 5 (`capture` 2, `march` 3) | 627 | `6e3a066a…` |
| 0 | `risk_gain` 0 (control) | 5 | 627 | `6e3a066a…` (equal) |
| 0 | `risk_gain` 1, appetite −1 / −0.15 / 0 / +0.15 | 0 / 0 / 0 / 0 | 655 / 655 / 655 / 654 | four values, `ea4a…`, `59de…`, `59de…`, `b8a2…` |
| 0 | `risk_gain` 1, appetite +1 | 5 | 627 | `6e3a066a…` (equal to base: the factor is 0) |
| 0 | `risk_gain` 0.05, appetite −0.15 / +0.15 | 3 / 4 | 628 / 628 | differ |
| 0 | `risk_gain` 0.05, appetite −0.5 / +0.5 | 3 / 4 | 628 / 628 | differ |
| 0 | `risk_gain` 0.1, appetite −0.15 / +0.15 | 3 / 3 | 628 / 628 | equal |
| 0 | `risk_gain` 0.1, appetite −0.5 / +0.5 | 3 / 4 | 628 / 628 | differ |
| 1 | base; `risk_gain` 0 (control) | 4 (`capture` 2, `march` 1, `accept` 1); 4 | 666; 666 | `01f7f9aa…`; equal |
| 1 | `risk_gain` 0.05, appetite ±0.15; ±0.5 | 4 / 4; 4 / 4 | 666 | equal; equal |
| 1 | `risk_gain` 0.1, appetite ±0.15; ±0.5 | 4 / 4; 3 / 4 | 666 | equal; differ |
| 2 | base; `risk_gain` 0 (control) | 3 (`capture` 1, `march` 1, `accept` 1); 3 | 653; 653 | `0a00352e…`; equal |
| 2 | `risk_gain` 0.05, appetite ±0.15; ±0.5 | 2 / 2; 2 / 3 | 661 / 661; 669 / 653 | equal; differ |
| 2 | `risk_gain` 0.1, appetite ±0.15; ±0.5 | 2 / 2; 1 / 2 | 669 / 669; 668 / 661 | equal; differ |

Command (scratch, outside the tree): `PYTHONPATH=<worktree> python3 <scratchpad>/appetite_season_probe.py <seed> <gains> <spreads>`.

**What the reading says.**

1. **`B10.31`'s sweep points (0.5, 1.0) swamp τ.** At `risk_gain` 1 the term is 0.5 per exposed candidate at full health, about ten times the outvoted-margin median: every exposed act vanishes whatever the appetite (seed 0: 0 of 5 survive from −1 to +0.15). Appetite then decides nothing but the last sliver. The gain at which appetite separates persons is near τ's scale (0.05 to 0.1).
2. **±0.15, the spread §3 carries for the A-108 axes, moves almost nothing here** (the hash differs between −0.15 and +0.15 in 1 of the 6 seed × gain cells at `risk_gain` 0.05 and 0.1). **±0.5 moves a decision in 5 of the 6.** **Proposed spread: appetite in `[−0.5, +0.5]` for authored persons `[ASSUMPTION; Jordan to correct]`**, the bound a fixture (`appetite_bound`, shipped 0.5) beside the load-time refusal of `[−1, 1]`.
3. **The exposure base is thin**: 3 to 5 exposed acts in 627 to 666 per season. Appetite can only ever reach these four rows; a recognisable bold character needs exposed candidates to form (`challenge` → `accept` and `march` are the paths) as much as it needs the term.
4. **The horizon spread is unmeasurable at ship** (§11.1: it multiplies nothing until goal stages are authored): a remaining question.

**τ.** The new terms do **not** leave the margins τ divides alone: at any non-zero `risk_gain` the hash moves and margins change. So **CR-17's τ rule is re-applied after the first non-neutral value** (M35's answered default), in the commit that flips the first of `risk_gain`, `beneficiary_gain`, `horizon_discount` or an authored appetite; `fixtures.py:292`'s own comment already names "CL-PERSON's first non-neutral value" as a mover that stales τ.

**Falsifier (3).** At the first non-neutral value, the `--decisions` outvoted-margin median and the one-season hash at seeds 0–2 equal the neutral run's: then the terms left τ's margins alone, the re-application clause is moot, and the second branch of Block D4's (3) holds instead.

### 11.4 Stored manner offsets (and the N-line rule)

| axis | stored offset? | ground |
|---|---|---|
| `rigid_flexible`, `grandiose_humble`, `deontological_instrumental` | **yes** | A-108 (ED-IN-0261's superseding row, 2026-11-12): "a person may carry a stored offset on each manner axis"; `B10.58` builds them at ±0.15 (its bound, §2 and §3 above). ED-IN-0304 is not needed for these: A-108 answers §4 E-4 for them. |
| `cautious_bold` | **yes, as risk appetite** | implements ED-IN-0304's first term (risk appetite), §11.1 (1a)–(1b); its reader is `risk'` |
| `hasty_patient` | **yes, as decision horizon** | implements ED-IN-0304's second term (decision horizon), §11.1 (1d); its reader is `aim'`; band-valued (carrier open) |
| `conciliatory_coercive` | **no; cut** | ties to no ED-IN-0304 term, A-108 does not name it, so a stored offset on it would contradict ED-IN-0261's ruled sentence (R7's dissolution clause, `formal_analysis.md:195`) and wait on §4 E-4; and the design names no reader (its `force` column is not declared, §11.2). **Cut by the N-line rule.** Restoring it needs a reader and a ruling. |
| `selfish_selfless` | **no (spread 0)** | §11.4a |

**The N-line rule, applied.** Beyond appetite and horizon, the three A-108 axes are tied to a reader (`score_terms`' pursuit sum through `projected_axes`) and stay; `conciliatory_coercive` is cut. The nine gain traits of §4 are not stored manner offsets and are not designed in this section; the rule is the test each meets at its own design (a trait kept only where its design names the reader it scales). None of them is in `B10.82`.

**Falsifier (4).** An offset loads on an axis outside the closed roster (`rosters.yaml: manner_offset_axes`, `B10.58`'s, plus the two keys this section ties to ED-IN-0304 when `B10.82` builds them): `conciliatory_coercive: 0.1` on a cast row loads instead of being refused.

### 11.4a M34: where self and other live, and whether `selfish_selfless` needs a spread

**Where the difference lives once `benefits_me` is gone:** in `verb_table.yaml`'s `beneficiary:` column, the per-candidate fact, read by `self_other` (§11.2) and weighted by the person's projected `selfish_selfless`, the disposition. ED-IN-0261's own split: "the selfish axis score supplies the disposition, the column supplies the per-candidate fact" (`rosters.yaml:4241`).

**Spread: none (0), steps 4 and 5.** M34's default in force is "no stored offset", A-108's row keeps "the other axes … projected", and `B10.58` is written to it ("`selfish_selfless` stays at spread 0"). Persons already differ on the axis through their pursuits (the projection loads it heavily: `wealth` −0.6 at `rosters.yaml:4033`, `love` +0.7 at `:4105`). What they lack today is a reader: the axis moved 0.000 of round-0 top picks when ablated (`hole_register.yaml:782`, its 2026-11-08 supplement, a reading not re-run here), and its alignment cell is zero on 65 of 67 verbs (measured above). `self_other` gives it a reader on the 39 rows that name a person beneficiary (28 actor + 8 subject + 3 to). Build the reader first and measure; add a spread only on evidence.

*The evidence that would license one*, and therefore **the falsifier (4a):** the Borgia case (`proposals/2026-09-16-conviction-decision-layer/adjudication_register.yaml:242-249`; `conviction_taxonomy_v30.md` §2.3, *"different gameplay even with identical Conviction vectors"*): two cast persons with identical pursuits whom the authors insist differ in for whom they act. With spread 0 they rank every `beneficiary:` row alike (R7, by linearity), so the design cannot express them. If the cast holds such a pair, `selfish_selfless` joins `manner_offset_axes` (one roster member on A-108's carrier, no new mechanism) under its own ruling. A second falsifier: once `beneficiary_gain` > 0, the axis' ablation still moves no top pick at seeds 0–2 (the reader does not reach).

### 11.5 M37

**No manner axis feeds the refusal gate.** The gate's threshold is the person's projected weight on the armed axis from his pursuits alone (`refusal_tolerance` → `project(p)[axis]`, Jordan: "the weighting is a threshold for certain actions"). No stored offset (A-108's three, appetite, horizon) enters it, and no personality-only axis can be `refusal_axis` (`require_member(axis, PURSUIT_AXES, …)`, `options.py`).

**Conflict named, not resolved here:** `B10.58` step (3) adds the offset inside `person_q.projected_axes` and says "every reader of manner (the chooser's alignment term, the refusal gate when armed) gets the offset through it"; `project` is `projected_axes(p, 0)`, and `B10.32` arms `refusal_axis = "deontological_instrumental"`, one of A-108's three. As written, the two items would feed a stored manner offset into the gate. M37 is the sentence above; reconciling `B10.58` (the offset added at the chooser's read, not inside the projection the gate reads, or the gate reading an offset-free projection) is outside this file.

**Falsifier (5).** With `refusal_axis` armed on `deontological_instrumental`, two hand-built persons with identical pursuits and opposite stored offsets on that axis refuse different verbs (or the same verb at different tolerances).

### 11.6 Falsifier and control for the build (`B10.82`)

**Falsifier (6).** Two hand-built persons with identical pursuits and opposite risk appetite (`appetite` −0.5 and +0.5), one question, the real ranker at temperature 0 and `risk_gain` > 0: they rank one exposed verb (`fight` on the same subject) differently, and rank it identically when the term is zeroed (`risk_gain` 0). **Planted failure:** the appetite factor dropped from `risk'` (the term computed as `B10.31`'s alone) makes them rank alike, and the test must go red.

**Control.** Every new term at neutral (`appetite` absent = 0, `horizon` absent = `long`, `horizon_discount` 1.0, `beneficiary_gain` 0.0, `risk_gain` at `B10.31`'s shipped 0.0) reproduces the base hash at seeds 0–2. The scratch probe's control row above is the same check on a stand-in: at `risk_gain` 0 the one-season hash equals the unwrapped run at seed 0 (`6e3a066a9d4b921bf5258a23b55d0e37`), seed 1 (`01f7f9aa0f3d9a52242ea78c8c92cc23`) and seed 2 (`0a00352e0e9349f8c12d26f8f9e7e467`). A new `Person` field moves the hash by encoding (`B10.58` step (4)'s precedent); if `B10.82` adds one, the control is the behaviour (executed-act and Event tallies equal) and the move is declared, as there.

### 11.7 Remaining questions

1. The carrier for `cautious_bold` and `hasty_patient` (§11.1 (1b), (1d)): `manner_offset?` read as covering an axis with no projection, or a Layer 1 node; and how a band-valued horizon is stored.
2. The horizon's decision shift: unmeasurable until a `goal_stages` row and `aim` exist.
3. `B10.31`'s sweep points (0.5, 1.0) against τ 0.05 (§11.3 reading 1): an observation for `B98`'s flip, not a change to `B10.31`.
4. `B10.58` step (3) against M37 (§11.5).
