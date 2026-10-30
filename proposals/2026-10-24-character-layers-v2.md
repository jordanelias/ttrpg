# Capability, ambition, values and personality, v2: ten axes, fifteen traits and the attribute readers

## Status: PROPOSED — HELD BACK IN FULL; reconstructed from a digest, not from the original file; where this file and a re-derivation from the tree disagree the tree wins
## Lane: IN. IDs: none allocated.
## Reconstructed 2026-10-30 from a digest. Original `layers_v2.md` (session of 2026-10-24/25): LOST
## Builds on: `proposals/2026-10-24-character-layers-capability-ambition-values-personality.md` (v1, committed through PR #505; superseded in part by this file) · `engine/season/queries/world_q.py` (`questions_for`) · `modules/combat/combatant.py`, `modules/combat/config.py` · `engine/season/loop/effects_combat.py` · `engine/season/data/fixtures.py` · `proposals/2026-09-16-conviction-decision-layer/adjudication_register.yaml` · `proposals/2026-10-24-character-progression-adjudication.md`

**How this file was produced, and what it is not.** The design below was worked in a session of 2026-10-24/25 whose file `layers_v2.md` was never committed and cannot be recovered. A read-only extraction agent later wrote a digest of that session's own closing summary (timestamp 2026-10-25T02:43Z); this file restates the digest and nothing else. It adds no number, no mechanism and no file reference that the digest does not carry. Every figure, count and `path:line` below is the session's, was not re-opened for this reconstruction, and may be stale: the digest itself records that several figures the session trusted turned out to be stale. This is reference under CLAUDE.md §0.05: prose is not a mechanism, and merging it ratifies nothing. The session's closing line was *"Tell me if you want the v2 design landed as a replacement"*, and the transcript holds no answer from Jordan; so this file is a record of a design exercise, not a landing of v2.

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

Constraint carried from the tree: ED-IN-0261 R7 says projected axes are linear in pursuit weights, so identical weights give identical axes (*"two people with identical pursuits ARE identically disposed and the variation comes from the candidates"*). v2 overrides it for the stored-offset axes (§2, §3).

---

## 2. What v2 changes against v1

v1 is `proposals/2026-10-24-character-layers-capability-ambition-values-personality.md`. The digest does not say which v1 sentences v2 rewrites; the mapping below is this reconstruction's reading of the digest against v1's §2 and §5, and each row says how v2 differs.

| v1 §2 / §5 row (quoted) | v1 says | what v2 does |
|---|---|---|
| §2, ED-IN-0261 R7: *"two people with identical pursuits ARE identically disposed and the variation comes from the candidates"* | "**Overridden for three axes.** Persons with identical pursuits may differ on `rigid_flexible`, `grandiose_humble` and `deontological_instrumental`." | Overridden for the stored-offset axes, now six of the ten: those three plus the three new personality-only axes (`cautious_bold`, `hasty_patient`, `conciliatory_coercive`). The four value readouts stay at spread 0. |
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
