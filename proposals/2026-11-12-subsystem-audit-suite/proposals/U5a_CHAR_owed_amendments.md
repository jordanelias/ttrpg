# U5a · CHAR — the owed amendments: what the CHAR audits decided as "an amendment to" another proposal and never wrote

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.3 rows CHAR owed (§3 (b) VIOLATES; §5 AMBIGUOUS), §2 rows A-47, §7, §7b-8, §7b-T; `unified/U1_GLOSSARY.md` *party* ("patient" → counterparty); `unified/U3_CONFLICT_LEDGER.md` C3-C16; `unified/U3_DEPENDENCY_ORDER.md` node B10, §6.2). Changed: §3 (b)'s keyed emission (a key that is a condition on the actor's ledger, neither a Degree nor a refusal clause, which the loader refuses, `04` §C.4) is replaced by one emission and a reading computed where read, `world_q.commitment_kept` (the D-48 precedent), and its `[UNVERIFIED]` on `release` is settled (`audits/25_GROUNDING_ENGINE.md` G-19 verified, `data/rosters.py:526`); §3's dependency cites A-47; §5's `Scene.decided` names its departure from `04` §B.9 at the site (B4 third disposition; C3-C16); §8 item 2 cites A-24 (D-28 answered: a drawn scruple); "patient" → counterparty (glossary), with `deed_patient` → `deed_counterparty`; the three scratch probes become named tests; lands-it and tier. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "patient" → "counterparty" (glossary *party*).

**Lands in batch:** B10 (§3 with `12_ARCS_arcs_as_staged_goals.md`, same batch). **Depends on:** B09 (`01_CORE_reason_trail_in_the_act_store.md`, `02_CHAR_reason_trail_and_small_edits.md` Part A for §5).

## Status: PROPOSED (a plan for future execution; nothing here is executed by the closing lane)

Authored by the U5a unification-closure lane, 2026-11-12. `audits/16_PESSIMIST_CHAR.md` decided six
resolutions as *amendments to existing proposals* (its §4 F-PES-CHAR-04, -07, -08, -09, -11 and §6 rows
9–12) and edited none of the amended files; `audits/02_CHAR_audit.md` decided three more with no file (§8
step 10; §6.1 H-60; §6.2 row 29). This file carries each as an exact edit, with its gate, falsifier and
order. Each section names the proposal it amends; that proposal's head carries a pointer here. It decides
nothing new except where marked **(U5a)**.

## What it changes in `engine/season/` at runtime

Every section ships at a control that reproduces today's hashes, except §9 and §10 (text and content) and
§5 (a stamp on a record that is not hashed). The flips in §8 are declared hash movers, each its own commit.

## Who lands it, and in what order

A CHAR-lane implementation session (the files are `decision/`, `queries/person_q.py`, `loop/resolve.py`,
fixtures and rosters), except §3, which lands with `12_ARCS_arcs_as_staged_goals.md` (the ARCS/WR lane).
Order: §9, §10 any time. §2 with `02_CHAR_scar_cap_and_regard_unit.md` item 3. §4 with or after
`02_CHAR_relations_have_a_ground.md`. §1 with `02_CHAR_resolve_and_temper.md`. §5 after
`01_CORE_reason_trail_in_the_act_store.md` and `02_CHAR_reason_trail_and_small_edits.md` Part A. §6 with
`02_CHAR_scar_is_a_wound.md`. §7 after `16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says.md` step 1.
§8 last, after the wound proposal's gate and §6.

---

## §1 · A person agrees with himself more than with a stranger (amends `02_CHAR_resolve_and_temper.md`, Gate)

**Source.** F-PES-CHAR-04 (a). Reading today (`c1_two_men.py` (b), a scratch script not in the repository, seed 0, 46 cast × 6 referents × 5
ticks' draws): the same man in the same situation takes the same first act in 39.3 % of redraw pairs; two
different men agree in 17.0 %.

**Edit.** One more reading in `engine/season/harness/decision_spread.py` (beside the pairwise table that
proposal's edit 4 adds): `--retest` prints self-agreement and between-person agreement of the sampled top,
over a stated number of draw ticks, on the built realm. One more line in that proposal's Gate:

- at `temper_gain` 0 the two figures reproduce today's (the control);
- with two hand-built persons equal in pursuits and at Focus's two ends, at `temper_gain` > 0, the
  high-Focus person's self-agreement is strictly higher than the low-Focus person's;
- on the realm, self-agreement stays above between-person agreement at every swept `temper_gain`.

No threshold is invented: each line is a direction against a control. Named tests (new, in
`engine/season/tests/test_temper.py`, beside `02_CHAR_resolve_and_temper.md`'s):
`test_retest_reproduces_todays_figures_at_gain_zero`, `test_high_focus_agrees_with_himself_more`,
`test_self_agreement_exceeds_between_person_agreement`. **Falsifier.** Self-agreement does
not move with Focus at any gain (the hook is not on the draw). **Hash movers.** None at gain 0.

## §2 · A strong loyalty makes acting against its object rare, not impossible (amends `02_CHAR_scar_cap_and_regard_unit.md` item 3)

**Source.** F-PES-CHAR-04 (b); the standing rule. The clamp at `STANCE_MAX` is necessary and not
sufficient: a clamped stance of 10 leaves a gap of 40 score units between acting for and against its
object, which is 800 choice temperatures, so the draw never crosses it (`x1_extremes.py`, scratch). That is a fixed
function of state wherever a relationship exists.

**Edit, owner `engine/season/decision/choose.py::stance_term`.** The term reads regard as a share of
`STANCE_MAX` (on ±1, the pursuit term's own range) times a new fixture `stance_scale`:

```
stance = (1 + stance_gain) · sign · clamp(regard, ±STANCE_MAX) / STANCE_MAX · stance_scale
```

`engine/season/data/fixtures.py`: `stance_scale`, control `STANCE_MAX` (25: today's value exactly, so the
hash is EQUAL), swept so that a full loyalty sits 4, 8 and 16 temperatures from zero (0.2, 0.4, 0.8 at
`choice_temperature` 0.05), with its hole-register row `[ASSUMPTION; medium; Jordan to correct; revert:
the control]`. The live value is flipped only after a reading; none is proposed here.

**Gate.** Control: `build_realm(0)` one-season hash EQUAL. At each swept value, one cast person with an
authored stance of 10 on a subject, 200 draws on one question: he takes an act the row treats as against
that subject in some draws and in fewer than half (named test, new:
`engine/season/tests/test_regard_unit.py::test_a_strong_loyalty_makes_acting_against_rare_not_impossible`). **Falsifier.** 0 of 200 at every swept value (the gap
is still out of the draw's reach), or more than half (the relationship no longer restrains: the `nostance`
arm's harm returns). **Hash movers.** The flip, when taken.

## §3 · A want can be kept or laid down (amends `12_ARCS_arcs_as_staged_goals.md`; U5d's file)

**Source.** F-PES-CHAR-07: 243 and 226 commitments live after three seasons at seeds 0 and 1, 0 ever ended;
other tenure kinds end in the same runs (`reside` 16 and 5, `hold` 3 and 9), so the reading sees an ending
when one occurs.

**Edit (design-first for (b); (a) is an edit).**

- (a) Owner `engine/season/queries/world_q.py::questions_for` (Q4): the standing `need` question for a
  commitment is not raised while the holder's **own ledger** reads the committed Proposition's content as
  true. Scope: Propositions whose content is a typed predicate the ledger reader can evaluate (the rung
  goals AM-B-09 narrowed aim states to; a stage predicate of `goal_stages` once authored). A want with no
  evaluable content is unchanged. A want he believes met and that is not met is then a false belief at
  work, which is intended.
- (b) Owner `engine/season/verb_table.yaml` (`release`), `decision/options.py`, `queries/world_q.py`:
  `release` on his own `commit` forms as an ordinary Candidate (it admits one's own commit today:
  `audits/25_GROUNDING_ENGINE.md` G-19, verified at `data/rosters.py:526`) and keeps its **one** emission,
  `commitment.ended`. Whether the released want was **kept** is a reading computed where read (the D-48
  precedent, ladder step 4): `world_q.commitment_kept(w, tenure) -> bool`, true when the closed `commit`
  Tenure's Proposition content was held true in the releaser's own ledger at the closing Event's tick. A
  row-keyed emission whose key is a condition on the actor's ledger is neither a Degree nor a refusal
  clause, and the loader refuses it (`04` §C.4, §B.13 invariant 12), so it is not built. The person closes
  his own edge (T-m); nothing closes it for him. **(U5a)** The pessimist's wording "the fold closes the
  tenure" is not taken: an edge closed by nobody's act is the unauthored write the gate refuses.

**Gate.** Realm, seeds 0–2, three seasons: `commitment.ended` Events above zero, `commitment_kept` true for
at least one and false for at least one; the count of live commitments is no longer monotone. With (a)
alone: `need` questions for met rung goals fall to 0 and the hash of a world with no met goal is EQUAL.
Named tests (new, `engine/season/tests/test_wants_end.py`): `test_a_met_rung_goal_raises_no_need_question`,
`test_commitment_kept_reads_the_releasers_own_ledger`, `test_release_has_one_emission`. **Falsifier.** 0 commitments end at three seeds (the
candidate never ranks: the lean is F-CHAR-01's and the goal-lean proposal lands first). **Hash movers.**
(a) where a goal is met; (b) wherever the candidate forms. **Dependency.** A-47 (D-61 answered B: a threshold may open a
mandatory scene, never decide it) is consistent with this. **Falsifier, added:** a `commit` whose releaser's
ledger did not hold the content true is read kept.

## §4 · What is done to a man decides what he thinks of who did it (amends `02_CHAR_relations_have_a_ground.md`)

**Source.** F-PES-CHAR-08: `person_q.py:128` reads a deed's claim subject as its doer for every kind but
the paired ones; the counterparty's regard for the actor rises after `sabotage` (+0.16) and `lie` (+0.18)
and is flat after `give` (−0.02) and `tend` (+0.02).

**Edit, owner `engine/season/queries/person_q.py::deed_term`.** For every deed kind whose verb row names a
person subject, the judge's reading of the deed is multiplied by `_bond(judge, counterparty, lean)`, the
factor `PAIRED_KINDS` already use; a judge who *is* the counterparty is his own full ally. Behind a fixture
`deed_counterparty` (control `paired_only`, today; live arm `person_subject`), with its register row. The set
of kinds is read off the verb table (`subject` of kind Person), never a list of verbs.

**Gate.** Control: hash EQUAL. Live, seed 0, two seasons (`b2_done_to_him.py`'s reading, scratch; restated
as `engine/season/tests/test_relations.py::test_what_is_done_to_a_man_orders_his_regard`): the mean change
in a counterparty's regard for the actor is higher for `give` and `tend` than for `sabotage` and `lie`.
**Falsifier.** The order is unchanged at the live arm (the term does not reach those deeds). **Hash
movers.** The flip.

## §5 · The stored reason names what decided, the draw included (amends both reason-trail proposals)

**Source.** F-PES-CHAR-09: 45 % of readings are decided by the draw (223 of 498); a trail that stores only
the occasion narrates a motive for acts that had none.

**Edit.** `02_CHAR_reason_trail_and_small_edits.md` Part A moves `attribute_top`'s rule beside
`score_order` under `decision/`. `decision/choose.py::pack_scenes` stamps each Scene it returns with
`decided: str`, one of the score's term names or `draw`, by that one rule, for the Scene's first act.
`state/carriers.py::Scene` gains the field (default `""`). **Layer 1, named at the site:** `04` §B.9's
`Scene` record is `(id, person, occasion, place, interactions)` and has no `decided`; the field is a
departure named in `Scene`'s docstring with its one reader (`harness/chronicle.py`, ID-13), under B4's third
disposition, and `04` is not edited (C3-C16). The Scene is `decision/`'s own return value, so
this is no write and no carrier beyond the record `01_CORE_reason_trail_in_the_act_store.md` already keeps;
that proposal's sentence *"one optional attribute on the stored Scene … is not built here"* is the
attribute built here. `harness/chronicle.py`'s per-act line prints it.

**Gate.** Content hash EQUAL (a Scene is not hashed, that proposal's Edit 4); the stamp's counts over the
built realm equal `decision_spread --decisions` (223 draw, 265 pursuit, 10 stance at seed 0, `601e715`).
Named test (new): `engine/season/tests/test_scene_store.py::test_scene_decided_counts_equal_decision_spread`.
**Falsifier.** The counts differ (two owners of the rule).

## §6 · The most scarred man is not the least changed (amends `02_CHAR_scar_is_a_wound.md`)

**Source.** F-PES-CHAR-11: `queries/person_q.py:883` (`if not crisis or not heirs: return base`): with the
weight shift armed, a person scarred past the threshold on every held pursuit ranks exactly as an
unscarred one, because the shift needs an unscarred pursuit to receive the weight.

**Edit, owner `engine/season/queries/person_q.py::crisis_weights`.** When every held (primary) pursuit is
at the threshold, the shift is taken from the most-scarred toward the least-scarred of them, by count,
ties by name; it is not skipped. No fixture: it is the dormant arm's own missing case, reachable only at
`scar_weight_shift` > 0.

**Gate.** At `scar_weight_shift` 0: hash EQUAL. At 0.5, a hand-built person scarred to 5 on every pursuit
but one at 3 ranks differently from his unscarred twin (named test, new:
`engine/season/tests/test_scar_stock.py::test_the_most_scarred_man_is_not_the_least_changed`).
**Falsifier.** The twins rank alike at 0.5.

## §7 · A creed's triggers are about the creed (extends `16_PESSIMIST_CHAR_B…`'s mechanism) **(U5a)**

**Source.** F-PES-CHAR-03 item 3 and §5: the affiliation track is violated by the same three verbs for
every creed (`destroy_record`, `evade / defy`, `forge`; `thread_read` for one more), so a believer's
crisis is triggered by forgeries; emptying every `Person.conviction` moves conduct by 0.053.

**Edit.** `engine/season/rosters.yaml`, beside `pursuit_signatures`: `affiliation_signatures`, one row per
member of `affiliation_roster`, `{favours: [...], opposes: [...]}`, checked by the same reader shape
(`signature_breaks`) against `tables.affiliation_engagement`. Content is Jordan's
(`[ASSUMPTION; low]` rows may be proposed by the CHAR content pass); the cells are repaired in that
table and nowhere else. The loader's refusal follows when the breaks read zero, as in B's step 3.

**Gate.** `conviction_spread --words` prints the creed breaks; after the cells, each creed's violating set
differs from at least one other creed's. **Falsifier.** With breaks at zero, the conviction swap still
moves the top act in under 5 % of readings (then the engagement gain, not the cells, is what is small: say
so and sweep it).

## §8 · Arming the two dormant readers, in order (carries `02_CHAR_audit.md` §8 step 10; H-187, H-146)

Two flips, each its own declared-mover commit, each after the reading that licenses it:

1. `scar_weight_shift` from 0 to a swept live value, **after** `02_CHAR_scar_is_a_wound.md`'s gate (b)
   reads a share strictly between 0 and 1 and §6 has landed. Gate: the realm's per-person conduct (the
   pessimist's total-variation reading against the `drawseed` floor) moves for persons at threshold 2 and
   not for persons below it, seeds 0–2.
2. `refusal_axis` armed, **after** `16_PESSIMIST_CHAR_C_the_stop_is_the_mans.md` items 1–3 land (its gate
   2: refusing persons strictly between 0 and 46). The draw form (item 4) follows A-24 (D-28 answered B: a
   scruple is a drawn tendency).

**Falsifier (both).** Everyone moves together, or nobody does. Then the flip is reverted in the same
commit and the reading recorded on the fixture's register row.

## §9 · H-60 closed on its row (carries `02_CHAR_audit.md` §6.1)

`engine/season/hole_register.yaml` H-60: closed, `cite:` naming `decision/sheet.py` (the player's space
calls `ask_budget()` and `release`). Text only; `register --check` shape passes.

## §10 · Two cast rows gain goals (carries `02_CHAR_audit.md` §6.2 row 29)

`references/npc_registry.yaml`, rows NPC-034 and NPC-071: author `goals:` (content; the CHAR content pass
or Jordan). The cases' "UNCLEAR: no goal authored" need is an authoring gap, not an engine need. Gate:
`data/cast.py` loads; the two persons hold a live `commit` at build. A declared build-hash mover.

## NERS reading (E last)

**N.** Each section closes a hole a measurement found in a proposal already written; without §2 the clamp
leaves the certainty it was meant to soften, without §3 no ambition in the realm ever ends, without §5 the
trail lies for half of what persons do. **R.** §3 and §4 are the no-player half: wants that end and
grievances that are about what was done. **S.** One rule for the deciding term (§5), one `_bond` for every
deed with a counterparty (§4), one signature reader for pursuits and creeds (§7). **E (last).** Ten small
edits on seven existing owners; no new carrier, no new instrument.

## Cost class

Edit (§1, §5, §6, §9, §10); small build behind a control (§2, §4, §7); §3 (b) is now an edit (one reader);
§8 is two flips.

**Lands it and tier.** The B10 batch, a CHAR/IN `valoria-author` session on `sonnet` (`high`), one commit per
section in the order above, closed by B10's `methodology-close` once; §3 with `12_ARCS_arcs_as_staged_goals.md`.
**INCOMPLETE, content:** §7's signature rows and §10's goals are Jordan's or the CHAR content pass's.
