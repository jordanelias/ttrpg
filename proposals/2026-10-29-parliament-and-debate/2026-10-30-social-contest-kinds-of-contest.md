# The kinds of contest in the social-contest subsystem, and how each operates

Reference, not a plan (CLAUDE.md §0.05). It describes what the code does; it dies with the code it describes.
Companion to `2026-10-30-stress-test-report.md` and `2026-10-30-lopsided-outcomes-inquiry.md`.

**Two systems share the name, and they are not the same thing.**

| | the **kernel** | the **live module** |
|---|---|---|
| where | `systems/social_contest/sim/contest/` | `modules/social_contest/roll.py`, called by `engine/season/seam/wrappers/sigma.py` |
| status | evaluated, **not adopted** (SC-05); reached by `build_contest` / `resolve_contest` | registered, called by the season loop |
| shape | two sides alternate arguments over several exchanges before an adjudicator; a win-condition reads the result | **one draw** by one actor against an obstacle; returns a `Margin` (net, ob) |
| kinds of contest | 8 named proceedings (+ a library of venues, + faction votes) | 5 verbs that contest + 3 graded inquiries |

Numbers below marked *(measured)* come from `2026-10-30-stress-log-*.jsonl`, every cell with its `n`. They are
for **bare-integer sides, both playing the logos-only policy**; "1 v 4" is side A at faculty 1 against side B at
faculty 4. Everything else is read from code at `73fa88d0` (= `origin/main` + the stress-test commit) and was not run.

---

## 1. The kernel's shared bout (what all eight proceedings do)

- **Turn order.** Each exchange, A moves then B moves. Every proceeding alternates strictly, A first.
- **Moves.** advance, hard, shift, support, pass, evidence, rebut. Reserve starts at 12; costs advance 3,
  hard 5, shift 4, support 2, evidence 3, rebut 3, pass 0; `support` and `pass` refill 4.
- **An advance** must be on the *live ground* (else an evasion strike), rolls the reception (pool dice + σ-leverage
  against **Ob 2.0**, §3 of the inquiry), and a landed degree 1–3 adds `2.6 × degree × resonance × readiness × jitter`
  to that side's advantage. **Ethos** builds Standing; **pathos** builds the Room.
- **Resonance** = how much a proof moves *this* judge: `(1−leak)·venue weight + leak·judge character`, where
  `leak = (1 − judge discipline) + 0.5·standing`, capped 0.9. **Readiness** = `0.4 + 0.6·(0.4·standing + 0.4·room)`.
- **Evidence** adds its hidden weight (cap 3.0, corroboration 1 / 0.7 / 0.5 / 0.35) with no roll and no readiness.
- **Faults** end the bout at once for the faulting side: a barred device, self-contradiction, two off-issue
  moves, two silences. A *shift* may only move the live ground up the ladder fact → definition → quality →
  jurisdiction → consequence → feasibility.
- **Nothing resolves before the close** in the track and tally proceedings. The win-condition is read once,
  after the last exchange, unless a fault ended the bout.

## 2. The eight canonical proceedings

What each is, in the order the registry lists them. "Declared" means the registry or the authored prose says it;
"operates" means resolution reads it.

| proceeding | exchanges (declared → run) | adjudicator → judge profile | verdict rule | start ground |
|---|---|---|---|---|
| formal_contest | 3 → 3 | crowd of 15: discipline 0.30, pathos 0.55 / ethos 0.30 / logos 0.15, not learned | Persuasion Track, start 5 | quality |
| grand_contest | 5 → 5 | crowd (same) | Persuasion Track, start 5 | quality |
| royal_audience | 3 → 3 | expert judge: discipline 0.75, logos 0.55 / ethos 0.25 / pathos 0.20, learned | Persuasion Track, start 5 | quality |
| church_tribunal | 1–5 → **5** | expert judge (same) | Persuasion Track, **start 6** | **fact** |
| guild_arbitration | 3 → 3 | panel of 5 expert judges | each juror votes; weighted by discipline | quality |
| casual_dispute | 1 → 1 | "no adjudicator": one neutral stand-in, discipline 0.30 | higher advantage wins, no track | quality |
| private_negotiation | 1–3 → **3** | no adjudicator | exchange majority; Track opt-in | quality |
| personal_appeal | 1 → 1 | no adjudicator | exchange majority; Track opt-in | quality |

**The Persuasion Track** is `start + 1.5 × (advA − advB)`, clamped 0–10, read at the close: ≥9 A_total, ≥7
A_decisive, above 3 up to 7 `committee`, then B_decisive, B_total. Start 5 means A needs a gap of +1.33 and B
−1.33; start 6 means +0.67 and −2.0.

**What differs between the eight.** Only four things: the exchange count, the verdict rule, the judge profile,
and (for the tribunal only) the start ground. `proceeding_venue` passes nothing else, so all eight share the
default proof weights (ethos 0.30 / pathos 0.30 / logos 0.40), equal temporal weights, the default fault catalogue,
no pressure, no rebuttal, fused standing. The `roles`, the exchange *minimum*, and the derived `resistance` are
copied into the typed table for display and never read by resolution.

### Per proceeding

**formal_contest.** *Operates:* three exchanges before a pathos-leaning crowd, read on the Track. *Declared, not
operating:* "Standard" resistance. *Measured:* equal sides reach a side **0.5%** of the time (n = 6,680; 34
decided; gap sd 0.47 against a +1.33 threshold). 1 v 4: `committee` 85.3%, stronger side 14.7%, weaker side
0.02% (n = 29,540). A logos argument earns about 0.50 per advance from this crowd; a pathos argument 1.25.

**grand_contest.** As formal at five exchanges. Equal sides decided **1.6%** (n = 10,140); 1 v 4 decided 31.8%,
weaker side 0.03% of all contests (n = 11,580).

**royal_audience.** *Operates:* three exchanges before one expert judge, on the Track. *Declared, not operating:*
"the Crown objects throughout" (roles do not alternate) and the petitioner's halved resistance
(`dictionaries.py:539-540`). *Measured:* equal sides decided 15.1% (A share 48.8%, n = 24,980); 1 v 4: `committee`
42.1%, stronger side 57.4%, weaker side 0.6% (n = 42,440).

**church_tribunal.** *Operates:* five exchanges (the maximum, always), on the Track **starting at 6**, opening on
the fact ground (past-tense weights). *Declared, not operating:* "the Inquisitor sets the terms", the length
choice, the accused's halved resistance "to compensate" for the bias (`dictionaries.py:546-550`), and the
Church boosting Obscuring (that needs an armature, which the wrapper never passes). *Measured:* equal sides
decided 33.2%, **side A takes 84.5%** of those (n = 15,520); with the start set to 5.0 and nothing else changed,
50.0%. 1 v 4: `committee` 38.3%, stronger 59.8%, weaker 1.9% (n = 22,380).

**guild_arbitration.** *Operates:* three exchanges build a running advantage (the room's momentum); then five
jurors each vote A if `0.6·gap + N(0, 0.8) > 0`, ballots weighted by discipline (all 0.75, so a plain majority;
five is odd, so a draw cannot occur). The Track is not used and there is **no committee outcome**. *Measured:*
equal sides always decided, A share 50.3% (n = 16,740); 1 v 4 weaker side 12.3% (n = 18,500).

**casual_dispute.** *Operates:* one exchange, no judge; whoever's advantage is higher wins, a tie (both fail) is
a draw. *Measured:* equal sides decided 99.6%; 1 v 4 weaker side **21.6%** (n = 63,180).

**private_negotiation.** *Operates:* three exchanges, same rule as casual. The Track can be opted into
(`use_tracker=True`, start 5). *Declared:* "failing to agree is its own answer" (prose); the kernel has no
agreement state, so a stand-in judge's tally names a winner (100% decided). *Measured:* 1 v 4 weaker side 8.6%.

**personal_appeal.** As casual at one exchange, Track optional. 1 v 4 weaker side 21.5% (n = 67,240).

## 3. Mechanical-library venues (reachable through `ContestedMode`, not by name through `build_contest`)

Described from code; **not run** in these probes.

| venue | verdict rule | judge | notes |
|---|---|---|---|
| court | ProofBar 2.0 (challenger A must lead by 2) | default | logos 0.55, past-weighted, fact |
| disputation | ThresholdRace 5.0 | default | logos 0.75, fact |
| assembly | exchange majority | default | pathos 0.50, future-weighted, consequence, no device bar |
| appeal | GraceThreshold 5.5 | default | equal weights, no evasion clinch |
| fused_arbiter | exchange majority | single | epideictic, present-tense |
| deliberative_body | **jury vote** of 7, noise 1.0, rebuttal licit | panel of 7 | the vote can cross the room |
| scholastic_disputation | ThresholdRace 5.0 | single | rebuttal licit, definition ground |
| public_oration | exchange majority | crowd of 15 | pathos 0.50, no rebuttal |
| inquisition_hearing | ProofBar 2.5 | hostile learned inquisitor, discipline 0.25 | one evasion strike is fatal |
| excommunication_court | ProofBar 3.0 | panel of 7, discipline 0.75 | ethos 0.50 |
| imperial_petition | GraceThreshold 5.5 | sovereign, discipline 0.05 | character leaks almost fully |
| secret_council | **jury vote** of 5, noise 0.8 | panel of 5, discipline 0.95 | logos 0.75, neutral |
| memorial_remonstrance | GraceThreshold 5.5 | lord, discipline 0.40 | ethos 0.45 |

Four docstrings disagree with their own code: `imperial_petition` says bar 8.0 (code 5.5), `memorial_remonstrance`
says 6.0 (code 5.5), `inquisition_hearing` says 3.0 and "lower than civil court 4.0" (code 2.5 and 2.0),
`secret_council` says ThresholdRace 3.0 (code is a five-juror vote). Three scaffolds (`DyadicMode`,
`NegotiationMode`, `CeremonialMode`) return a self-flagging stub.

## 4. The other game types

`resolve_contest` routes four games. Only `agon` (Sections 1–3) resolves.

- **consensus** (stub in the router; the work is in `faction.py`, an adapter, not canon):
  - *Parliamentary motion.* The proposer and target argue a separate exchange bout *before each voting faction*
    (the voter is the adjudicator, its disposition and discipline set resonance); each vote is cast for whoever
    wins that bout; votes weighted by Mandate (+ Church CI÷20); the target does not vote; the proposer votes
    yes. Pass thresholds 50% (censure, embargo, blockade, subsidy) and 60% (outlawry); within ±0.06 of the
    threshold the result is `committee`.
  - *Succession.* Two claimants on a Track (scale 1.5, five exchanges, ethos-weighted): unified, decisive, or
    split, with winner's share 0.60 / 0.55 / 0.50 for Track 4 / 5 / 6.
  - *Coalition vote.* Each side's pool is the sum of its members' Mandate; one pooled roll each; Track start
    5 ± lobby clamped to 4–6, compressed toward committee by abstainers of Mandate ≥ 5.
- **negotiation** (stub): the scaffold text reads "typed envoy latitude, escalating instruments; win = agreement
  in the overlap". **inquiry** (stub): Church Tribunal / Inquisition as a later game.

## 5. The live module's contests

The roll is one draw by the actor: `pool` dice plus `leverage` (μ-shift) against an obstacle composed in
`roll.py::obstacle`, returning a `Margin`; the season loop turns the margin into a band.

- **Pool** = `Person.capability[VERB_CAPABILITY[verb]]` else `pool_default`. By its docstring the capability dict
  is empty on every corpus person (1 of 430 carries one), so every actor rolls `pool_default`.
- **Leverage** = 0.0, always ("nothing supplies it", `sigma.py:160`).
- **Obstacle** = the opponent's score ÷ 2 (when the opponent is a person with a score), else `obstacle_default`
  (2.0); a bench's regard for the actor and the actor's unmirrored proofs move it (`room`) only for a prize with
  `heard_by: bench`; an examined record's forgery quality is added; a ceiling (shipped: 2) caps it. By its
  docstring a hostile room cannot raise a defaulted obstacle under that ceiling.

| contest (verb) | prize | who rolls, against whom | room terms | capability row |
|---|---|---|---|---|
| tell | a standing | teller against the hearer (`to`) | no | `copying` |
| speak | a matter | speaker, before a docketed matter | **yes (bench)** | `copying` |
| argue | a proposition | arguer against the hearer (`to`) | no | none |
| determine | a proposition | **the judge (the actor)** against the party | no | none; default obstacle "for every party" |
| arrest | a standing | the arresting seat against the prisoner | no | none |
| research / examine / surveil | graded inquiry | the inquirer against the finding; examine adds the record's forgery quality | no | none |

`fight` / `accept` (the body) and `march` (a field) belong to combat and mass battle, not here. The `argue` row's
own note records that, once restricted to a Proposition referent, it formed for 0, 0 and 0 of 83 persons at
seeds 0–2, which agrees with the stress test's zero `argument.*` events over 13 seasons.

## 6. Side by side

| | kernel proceedings | live verbs |
|---|---|---|
| opponent rolls | yes, every exchange | no; the opponent contributes a score |
| adjudicator | crowd / expert / panel / stand-in, per proceeding | none; only a bench, for `speak` |
| contestant as adjudicator | no mode; "no adjudicator" is a neutral phantom | `determine`: the actor *is* the judge |
| obstacle | fixed 2.0 | derived from the opponent, the room, a forgery, capped |
| outcome shape | band (decisive/total/committee) or a side | a margin, then a band |
| asymmetry between sides | the tribunal's start of 6 only | none by kind |

## 7. Measured: what a die and a σ of leverage are worth in the live roll

`roll.py` at `obstacle_default` 2.0, no ceiling, no opposition. P(net ≥ Ob), n ≥ 36,000 per cell (≥ 92,000 for
pools 2–4):

| pool \ leverage | 0 | 0.25σ | 0.5σ | 0.75σ | 1.0σ |
|---|---|---|---|---|---|
| 2 | 0.258 | 0.260 | 0.260 | 0.260 | 0.260 |
| 3 | 0.400 | 0.400 | 0.400 | 0.401 | **0.682** |
| 4 | 0.512 | 0.512 | 0.512 | **0.748** | 0.749 |
| 5 | 0.599 | 0.600 | 0.600 | **0.795** | 0.795 |
| 6 | 0.668 | 0.669 | 0.669 | **0.833** | 0.833 |
| 8 | 0.770 | 0.770 | **0.888** | 0.889 | 0.889 |

- **Leverage acts in whole-number steps.** The roll's net is an integer and the boost is continuous, so a
  rising leverage does nothing until it crosses the next integer threshold, then moves the rate all at once
  (+0.28 at pool 3, +0.24 at pool 4, +0.12 at pool 8). At pool 2, leverage up to 1.0σ changes nothing. The step
  positions move with the obstacle (an opposition score ÷ 2 can be a half-integer).
- **A die is worth less per unit but arrives smoothly:** pool 3 → 4 adds 0.11, 4 → 5 adds 0.09, 5 → 6 adds 0.07.
- **Leverage cannot lift a small pool off a high obstacle.** `roll.py` records p_success 0.0006 at Ob 3 for a
  one-die pool and says buying σ-advantage cannot lift it; this is why the ceiling exists.
- **The soft cap is `1.5·tanh(x/1.5)`** (`sigma_leverage.py:104,141`), not a clamp at 1σ. The stress-test
  report's earlier "saturates at one σ" reading was the pool-3 rounding above, and is corrected there.

## 8. Not shown

The library venues and the faction votes were not run here. The live verbs' firing rates in a season were not
measured. Sides built from the host `World` were not tried against the kernel. Every kernel rate is for a fixed
logos-only policy and integer sides; the lever cells in the lopsided inquiry show how much that matters.
