# CHAR — what an act risks: a cost term for danger to the actor, read off the row's own prize and his own body

## Status: PROPOSED

Written by the CHAR audit lane, addendum B (`audits/02_CHAR_audit_addendum_B.md`, F-CHAR-20, B3.2
property P4, B6.2 rows 11 and 12). Ratifies nothing. Reference under `CLAUDE.md` §0.05. It is an
**input to CL-PERSON's open ask M40** (risk appetite, ED-IN-0304) and to CR-93's design, as the first
lane's `02_CHAR_resolve_and_temper.md` is for the noise of choosing; it does not pre-empt either. It
is distinct from that proposal: temper is how far a person strays from his best act; this is one of
the terms that make an act best or not.

## What this changes in `engine/season/` at runtime

`decision/choose.py::score_terms` returns one more term, `risk`, which is 0.0 for every candidate at
the shipped `risk_gain` 0 (the control; hash EQUAL). At a non-zero gain, a candidate whose row
contests a bodily prize is scored lower by what the person believes he stands to lose, more so the
worse his body already is. A declared mover when the gain is flipped. Uncontested candidates and
contests for a standing, a proposition or a matter are untouched at any gain.

## The problem, with evidence

**No term counts what an act may cost its actor.** `score_terms` (`decision/choose.py:193-221`)
returns `(pursuit, stance)`. `odds_weight` multiplies a contested candidate's value by his believed
chance of the bands that write, so a probable loss makes winning worth less and never makes losing
cost anything. `Person.body` reaches a decision only through the number of scenes (`budget.py`; the
first audit's F-CHAR-14). Two persons identical but for a body at the top band and at the lowest
therefore rank `fight` on one subject identically, by reading.

**The realm hides the absence.** At seed 0 over two seasons `fight` resolved 0 times while
`challenge` was refused 84 times (first audit, probe 2), so nobody yet reaches the choice this term
would inform. It becomes visible the moment the first lane's `02_CHAR_offer_what_can_be_done.md`
lands and fights can form.

**Ruled, and unbuilt.** ED-IN-0304: persons differ in risk appetite. AR-51 and AR-52 (ED-IN-0347):
*"proposing a duel is far easier than seeing it accepted"*; *"a king would see no reason to duel
unless…"*. The adjudication amends CR-87 so that `accept` takes `fight`'s cost. AR-38: an opponent's
emotional state colours what he does. None has a carrier in the score.

**What the design meant** (ARCHIVED-NOT-CANON; intent only). Every decider in the design looks after
himself: a faction at Stability 1 abandons conviction for survival (`npc_behavior_v30` §4.1, §8.1); a
Companion one wound from the limit goes to full guard (`companion_specification_v30` §4.1); a
practitioner at Coherence 5 self-limits and at 2 withdraws (§4.3). The 2026-09-16 synthesis writes
the score as pull minus cost and says *"exactly one term carries a minus sign"*: what the act *"will
take out of me"*, scaled by courage.

## The resolution, decided

Ladder: step 3 (ED-IN-0304; the synthesis, whose rulings were absorbed), step 5 for the form. The
term is built from three things that exist and one new roster:

```
risk(p, c) = − risk_gain · exposed(c) · (1 − chance(p, c)) · (1 + bands_below(p)) · nerve(p)
```

- `exposed(c)` is 1 when the candidate's row contests a prize in `rosters.yaml: bodily_prizes`, else
  0. Read off the row's own `contests:` column, never a verb name. Today the prizes are `the body`
  (the rows `fight`, `capture`, `accept` declare it) and `a field` (`march`).
- `chance(p, c)` is his believed chance of coming through it, asked of the one odds query
  (`View.odds`, `seam/wrappers/sigma.py::believed_chance`). **Stated limit, read in code:** that query
  answers `None` for a band the social ladder does not carry, and the bodily rows' bands are the
  combat module's and the field's (`Declared`, `Felled`, `Wounded`, `Untouched`; `Won`, `Lost`), which
  also do not say which party fell. So today every bodily candidate reads `None` and the term uses
  `risk_unknown_chance`, a fixture at 0.5: it separates persons by body and nerve at once, and by
  believed odds only when a module's own estimate is served through the same query (the first
  audit's interface line `View.odds(act, bands)`; `10_DICE_believed_odds_have_a_prior.md` by title).
  The band set that means "I came through" is then the module's to declare on its row, not this
  term's to guess.
- `bands_below(p)` is `decision/budget.py::body_band_penalty`: 0 at full health.
- `nerve(p)` is `capability_factor(p, "choice_exposure", fx)` (the first lane's interface, the DICE
  map's `judgement` role): 1.0 with no uses row, and with the row
  `{use: choice_exposure, role: judgement, key: attr.mind.will, gain: nerve_gain}` it falls below 1
  for a person of high Spirit and rises above for one of low. Spirit is the attribute by Jordan's
  AR-44 (*"the capacity to tolerate harm and strain"*) and the adjudication's §2.2 (iv) (*"nerve is
  Spirit's"*).

**Appetite is not in this term and is not a capability.** A stored per-person appetite for risk
(ED-IN-0304) passes the personality test (no pole always wins) and is CL-PERSON's; when M40 answers
where it is carried, it multiplies `risk` at this site and nowhere else, so there is one ladder for
the quantity. This proposal supplies the term it would scale and the half that is capability.

## Exact edits, by file and owner

1. **`engine/season/rosters.yaml`**: `bodily_prizes: {values: ["the body", "a field"]}`, closed
   against the set of `contests:` values the verb table declares (refused at import otherwise).
2. **`engine/season/decision/choose.py::score_terms`** (the one owner of the formula): the third
   element of the returned tuple; `score` sums three. The chance is asked through the same `odds`
   callable `odds_weight` receives, and is not asked at all at gain 0. With the first lane's `aim` term the
   tuple is four; the order is `(pursuit, stance, aim, risk)`.
3. **`engine/season/data/fixtures.py`**: `risk_gain` (0.0; sweep 0, 0.5, 1.0), `risk_unknown_chance`
   (0.5), `nerve_gain` (0.0), each with a hole-register row.
4. **The uses table**: the `choice_exposure` site joins `capability_use_sites`; no row ships.
5. **Instruments**: `harness/decision_spread.py::attribute_top` already calls `score_terms`; its
   deciding-term tally gains the `risk` column by reading the tuple's length, not a name.

## What it is for in the other lanes (stated, not built)

- **PC, MB.** The opening approach and a standing order's `retreat_at` are options on an exposed
  act. Once `View.odds` answers by option (the first lane named that gap), the same term ranks a
  cautious approach above a rash one for a wounded or fearful person, with no approach-specific rule.
  Inside a bout the module's default policy needs the same quantity as typed input; `Combatant.disp`
  has no registry key, and `1 − nerve·(1 + bands)` normalised is the candidate source. That input
  field is PC's.
- **SC.** `arrest`, `interrogate` and a trial contest a standing or a proposition, not the body, and
  are untouched. If a verdict can cost a body, the prize roster is where that is said.

## The gate (an execution artifact)

(a) `risk_gain` 0: `build_realm(0)` one-season hash `5ab73af2`, EQUAL. (b) Two hand-built persons
identical but for `body` (top band against the lowest), one question, the real ranker at temperature
0 and `risk_gain` 1: the wounded one ranks `fight` and `accept` on the same subject strictly lower
than the whole one does, and `challenge` (which contests nothing) at the same rank. (c) The same
pair, equal bodies, one holding Spirit 7 and one Spirit 1 with the `choice_exposure` row at a
non-zero `nerve_gain`: the low-Spirit person ranks the exposed acts lower. (d) Seeds 0 to 2, after
the offer proposal lands: attempts at exposed acts by persons below the top body band fall against
the gain-0 control.

## The falsifier

At a non-zero gain the rank of any candidate whose row contests no bodily prize changes (the term
leaked); or (b) shows no difference (the body does not reach the term); or, in (d), wounded persons
attempt exposed acts as often as before at three seeds, in which case the term is too small to
matter against the stance term's scale (the first audit's F-CHAR-08) and the clamp lands first.

## NERS reading (`CLAUDE.md` §0.06; E last)

- **N.** Top-down: the brief asks that an NPC choose an approach and a retreat as a person would.
  Bottom-up: the believed chance and the body band are both computed already and neither prices a
  loss. Lateral: duels (AR-51), marches and captures all lack the same term. Diagonal: it is what a
  module's NPC policy would be handed. Removing it leaves the fearless realm.
- **R.** A player can learn that a man is cautious or brave from what he declines; a wounded lord
  sues for terms without anyone scripting it; and the extreme is bounded (gain 0 is today, and the
  term is zero for everything that is not dangerous).
- **S.** It reuses the one odds query and the one band function, so danger in a choice and odds in a
  roll cannot disagree; it pauses nothing.
- **E.** One term, one roster, three fixtures. Stated in a line: the less likely he thinks he is to
  come through it, and the worse off he already is, the less he wants to.

## Cost class

Small build, shipped at its control; a flip after (b), (c) and the offer proposal.
