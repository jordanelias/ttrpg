# HANDOFF — the meta-architecture stage

**Status: PROPOSED. Nothing here is ratified.** Written 2026-09-03, at the end of the session that
landed `W28`'s office schema (`f56b11e`) and the adversarial-audit remediation (`4c68adc`).

## Why this file exists, and what it replaces

Jordan redirected the work mid-session, in three messages:

> *"remember that we are most concerned with setting up the ideal code architecture, not
> necessarily canon compliancy, at this point"*
> *"so all the work we are doing with canon is intended to inform you of what is required from our
> system"*
> *"I am now asking you to deviate from the approved plan for building idealized code architecture
> so that we can design the ideal code meta-architecture, ie a level of abstraction so that we have
> more clearly defined idioms and axioms and rules and logics for how to design the game itself"*

⚠ **THIS IS A DELIBERATE DEVIATION FROM `PLAN.md`, NOT A DRIFT FROM IT.** `PLAN.md` Part 5's
critical path (`W18 → W20 → W21 → W22 → W23 → W26 → W27 → W30`) is not withdrawn and not
superseded; it is PAUSED at Jordan's direction, with `W28` partly done. A later session must not
"resume the plan" without reading this file, and must not delete the plan either. The two are
about different things: `PLAN.md` says what to BUILD; this stage asks what the things ARE.

⚠ **AND CANON IS NOW A REQUIREMENTS SOURCE, NOT A CONFORMANCE TARGET.** This reverses the posture
of the two commits above, which read `systems/world/` to decide what a roster should CONTAIN. The
question is no longer *"does the model match canon"* but *"can the model EXPRESS what canon needs"*.
The four-tier source precedence in `rosters.yaml`'s header still governs where names come from; it
no longer governs what the architecture must look like. Read canon for REQUIREMENTS.

## The question Jordan asked, which is the seed of the stage

> *"what comprises a person, faction, office, site, etc?"*

It has no good answer today, and the reason is worth stating precisely rather than apologetically:
**the tracer grew its entities one defect at a time.** `Person` has whatever fields a verb needed;
`Office` gained `body`/`faction` yesterday because Jordan asked a question; a "faction" is a STRING
in a roster with no type at all; a `Site` is a rung + kind + condition because MATTER needed one.
Nothing states what any of them IS, so every new requirement lands as another field.

## What the last two commits ESTABLISHED that this stage should build on

These are measured, not asserted, and each has a falsifier in `engine/season/tests/test_season_shape.py`.

1. **There is exactly one containment relation, and it is under-used.** `contain : Rung → Rung` is
   now direction-validated (`World.add_tenure`; 46/46 downward edges refuse). It is the ONLY
   hierarchy in the system that can be WALKED — which is why Jordan's *"is that unnecessary to nest
   these and instead just explicitly define scale?"* answers itself: `under_purview` walks the
   ladder, and a scale LABEL cannot be walked. A label says where a thing sits; a relation says
   what reaches it.
2. **Two more hierarchies are required and cannot be expressed at all** (`H-101`, tier 0). Faction
   under faction, office under office. Canon models BOTH as mutable, contested tracks and ships the
   detachment of each as a named event (Löwenritter Autonomy → Split; the Cardinal Independence
   Check and Jarnstal Drift). 14 corpus cases name a superior or subordinate.
3. **Titles and offices are CONFLATED, and Jordan's ruling names the missing relation.** Jordan:
   *"offices confer titles to characters."* Today there is no Title entity: `titles_held` derives a
   title from an Office whose `post` STRING happens to appear in the `titles` roster, and `confer`
   seats an office (`hold` Tenure) — it cannot grant a title. So the title ladder has a REVOKE path
   (`_req_revoke`'s three-term conjunction, built to Jordan's governance canon) and NO CONFERRAL
   path. That asymmetry is the clearest single piece of evidence that the entity model is wrong
   rather than merely incomplete.
   ⚠ A patch I made yesterday is implicated and should be RE-OPENED, not preserved:
   `Office.__post_init__` refuses a `post` that is both a title and a body. That refusal blocks a
   real error (a King seated in a Church chair) but it does so by treating title and office as
   MUTUALLY EXCLUSIVE CATEGORIES, which Jordan's ruling contradicts. It is a symptom marker, not a
   design. Decide the entity model first, then keep or drop it on purpose.
4. **The recurring defect class is now well characterised, and it is not carelessness.** Five of the
   seven audit findings were the same shape: *an artifact that reports success for something that
   did not happen*, or *a guard that cannot observe what it guards*. `move` published `travel.moved`
   while changing nothing; Q3's falsifier planted a tuple its writer never emits; `claim_decay`
   bypassed the counter that proves it was registered; `_check_office` validated three axes and
   discarded them. **A meta-architecture that does not make this class hard to write has not
   earned its cost.**

## What the stage should produce

Suggested, not prescribed — Jordan named the axes and this is one reading of them.

- **An entity axiom set.** For each of `Person`, `Rung`, `Site`, `Office`, `Title`, `Faction`,
  `Tenure`, `Claim`, `Event`, `Act`: what it IS, what it OWNS, what may reference it, and what may
  never be a field on it. `Rung._DECLARED` and `Office.__post_init__` are the closest existing
  precedents for enforcing such a statement.
- **A relation set, small and closed.** The strong hypothesis from `H-101`: there is ONE
  subordination relation asked at several scales, and `tenure_kinds` (`contain`, `oblige`, `tie`,
  `hold`, `commit`, `succeed`, `knot`) already contains the carriers. Building a second ladder for
  factions and a third for offices would be the §8 violation the register row names.
- **The idioms, stated so they can be checked.** Candidates earned in this session:
  *an emission asserts a state change* (D22, which `move` broke);
  *a guard must be able to observe the failure it excludes* (§0.1 pt 2, which Q3's test broke);
  *validate at the constructor, not at the caller* (which `_check_office` broke, then fixed);
  *no evidence is a refusal, never a default* (§42.2, which optional-faction broke);
  *one owner per rule* (§8).
- **The slices of play and the loops.** Jordan asked for these explicitly. The barrier sequence
  (CALENDAR → MATTER → DELIBERATE → RESOLVE → WITNESS → CENSUS) is the season loop and is real;
  what is NOT stated anywhere is which loops nest inside it, where a contest re-enters, and what a
  "slice of play" is as a first-class thing.

## State at handoff — verified, not remembered

- Branch `claude/agonist-antagonist-workplan-rbc3oc`, PR #357. Head `4c68adc`.
- `python -m pytest engine/season/tests -q` — **181 passed as of 2026-09-05**; run it rather than citing the number. All 8 register gates clean on every touched row.
- Corpus: **89 of 143 runnable**, UNREPRESENTABLE 54 (faction 44 · world 10).
  **NPC RUNS = 0 · ARC ENDS = 0** — unchanged, and both remain honest zeros.
  ⚠ **UPDATED 2026-09-03 — THE ZEROS ARE STILL ZERO AND THE CHECK UNDER THEM IS NOT.** `R3`
  (an act by one person caused by an act of another) went **0 of 30 → 30 of 30** on the NPC lane
  and **0 of 59 → 54 of 59** on ARC when `N3`'s two edges were closed; `RUNS-ALONE-UNDECLARED`
  went 64 → 5. `RUNS` and `ENDS` themselves need `R2`/`A2`, which are NOT-COMPUTABLE, so they do
  not move and nothing here claims they did. **Read the two numbers separately** — that is what
  `PLAN.md` Part 6 means by never averaging the lanes, applied one level down.
- Executed verbs **5 of 32** (`create_record, speak, tell, utter, work`); refused: `move`, `transfer`.
  ⚠ This went DOWN from 6 in this session and that is a correction, not a regression — see `4c68adc`.
- Register: **91 rows** · absent 28 · assumption 42 · measured 3 · ruled 18 · tier 0: 37.

## W28's remainder, if the stage does not absorb it

44 faction cases (15 NPC · 29 ARC) + 10 world cases + 47 ARC endings + 40 prose spans.
Two findings worth keeping whatever happens to the item:
- **The 44 are not one job.** ~19 name a person-shaped actor; ~25 name only an institution or a bare
  MECHANIC ("a private counter accumulates"). A case whose subject is a mechanic may have no person
  to seat, which would make it unrepresentable for a DIFFERENT reason than `H-95`'s vocabulary
  mismatch. ⚠ That split came from a keyword regex — an INDICATOR, not a classification. Do not
  build the classifier; `W10` deleted that router once already.
- **The 15 NPC cases split 5 / 5 / 5 across the source tiers.** Five are in canon (Tormann IS §3.1's
  Cardinal of Prudence; Himlensendt is the Confessor with canon's exact four arms; Ehrenwall
  commands the Lions' Table; Vaynard and Baralta are §2's named Duke and Duchess — and those two are
  DUCHY-scale TITLE-holders, a path the three pilots never exercised). Five are near-canon only.
  Five — Falkenrath, Torberg, Kessler, Grindvold, Doukas — appear NOWHERE in the tree outside
  `proposals/`. ⚠ Not necessarily invented: four culling waves retired trees to the fork, so the
  extraction's source may be at a ref. Establish it; do not assume it either way.

## Open, and Jordan's to rule

`H-98` (winner vs degree) · `H-94`'s structural half (where operands live — it now blocks TWO verbs,
`move` and `transfer`) · `H-95`'s `world` half · `H-101` (the subordination relation) ·
`H-100` (what a revocation costs).
