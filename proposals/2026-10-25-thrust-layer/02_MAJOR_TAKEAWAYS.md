# Major takeaways from the thrust-layer session, expanded

## Status: PROPOSED — HELD BACK IN FULL

Currency (as `00_THRUST_LAYER_DESIGN.md`'s Status line carries it): the v10 plan has since folded the design in as
`CL-THRUST` (`workplans/valoria_master_workplan_v10_part12.md`) and ruled M20, M21 and ED-IN-0301
(`workplans/valoria_master_workplan_v10_part6.md`); read those rows before this file. The register's grades are as of
2026-10-25, and B10-02 (#509) has since landed instruments for G-02, G-08, G-11, G-12, G-20, G-27, G-28 and G-29.

Merging the PR that carries this file ratifies NOTHING in it (ED-1094's default is not applied; no ledger row,
`CURRENT.md` row or Status line elsewhere is flipped). Reference under CLAUDE.md §0.05: not a mechanism, binds no code,
creates no plan position and allocates no id. It is the third document of `proposals/2026-10-25-thrust-layer/`, beside
`00_THRUST_LAYER_DESIGN.md` (the design, "TL") and `01_MISSING_IN_CODE.md` (the gap register, "the register"). The
session's chat answers and the four subagent reports are in `reports/`.

## 1. What this is, and how to read it

The session asked one question in many forms: how can Valoria's emergent play be made legible, coherent and arc-shaped
without a director that writes outcomes. It produced three kinds of evidence, and every claim below carries one of them:

| Tag | Means | Strength |
|---|---|---|
| **[engine]** | measured on the shipped realm (`build_realm`, seeds 0–4) by a scratch probe in `probes/`, or read at a named call site | the only evidence about Valoria |
| **[toy]** | measured in an abstract world of the author's construction (`toy/`; 24 actors, 6 places, 24 seasons) | tests the *logic* of regimes, not Valoria; low confidence; several arms and intervals are post hoc |
| **[critic]** | found by an independent read-only agent that saw only a document and the tree (`reports/R13`, `R15`) | what survived re-opening is marked in the design and register |

The eight takeaways were first stated in chat (`reports/R10`). This document keeps their order, expands each, **corrects
the first delivery where later measurement disagreed** (§9 lists every change), and names who owns the fix. Section
numbers: §3–§8 are the takeaways (T1–T8); §9 corrections; §10 what is not answered; §11 what needs Jordan.

The register's section headings use the same T-numbers, so a register row cites the takeaway it serves. Gap ids ("G-nn")
are the register's.

## 2. The eight at a glance

| # | Takeaway | Strongest evidence | Register rows | Design |
|---|---|---|---|---|
| T1 | The substrate refuses most acts; fix that before anything else | [engine] 76.2% of 7,402 attempts refused; closers rarely execute | G-01–G-06, G-08, G-11, G-12 | §7 |
| T2 | A motive layer is needed, and part of it exists | [engine] goal rows, `need` question; [toy] motive depth 0.43 → 0.80 | G-09–G-12 | §1–§3 |
| T3 | Arc shape needs a goal ladder **and** a closure form together | [toy] +0.24 only with both | G-13, G-14, G-25, G-26 | §2–§4 |
| T4 | Killing has no consequences today, and fighting authority is easy | [engine] 20 deaths in 20 seed-seasons, 11 through unchallenged `accept` | G-15–G-20 | §5 |
| T5 | Do not build the tempting things | [toy] lookahead, blind scripts, forcing directors | none: nothing is missing | §9 |
| T6 | The deepest premise is the least buildable | [engine] 0 threadwork modules load; caste has no store | G-21–G-24 | §6 |
| T7 | Authoring is the largest content job | [engine] 46 case termini are prose; ten axes lack rows | G-25, G-26 | §6 |
| T8 | Metrics fail quietly | [critic] the first arc test was vacuous; [engine] instruments count refusals as story | G-27–G-29 | §1.2, §8 |

Dependency, as the register orders it (§5 there): T8's instruments and T1's alignment first, because every later count is
read through them; then the formation question (H-156); then death and consequence (T4); then ladders and closure (T3)
last, because they attach only to referents and verbs that exist and execute.

## 3. T1 — The substrate refuses; make the existing verbs execute first

**Claim.** Every narrative design from this session sits on a substrate that mostly fails. Top-down, bottom-up and hybrid
designs all end their arcs through acts that the shipped realm refuses almost every time.

**Evidence [engine].**
- *Refusal floor.* Seeds 0–4, driver's own definition (an act is refused when any Event it emitted is one of its row's
  `emits_on_refusal` kinds; `loop/driver.py:489-505`): 2 seasons, 7,402 attempts, 1,763 executed, **5,639 refused
  (76.2%)**; 4 seasons, 16,116 attempts, 3,744 executed, **12,372 refused (76.8%)**. With graded losses excluded (a
  Failure-degree event of a kind that is in both `emits` and `emits_on_refusal`; `corpus_run.attribute` does not count
  them), 73.8% and 73.9%. The orchestrator re-ran seed 0 to the same content hash (`5301d6b6…`).
- *Closers, executed over attempted at 4 seasons:* `determine` 3/43, `confer` 10/111, `covenant` 0/70, `commit` 8/564,
  `revoke` 0/32, `release` 63/460. The docket's front half runs (`open_case` 40/89, `issue` 73/112, `petition` 120/287,
  `oblige` 301/642); `determine` is the bottleneck. `succeed` is not in `resolvable_verbs()`; `arrest` formed 0 times.
- *The works and benevolence verbs:* `restore` 0/250, `tend` 0/302, `build` 0/230, `found` 1/208, `work` 3/726.
- *Wrong-kind formation.* **28.7% of 16,116 attempts (32.2% of 7,402 at 2 seasons) are refused at admission because the
  subject is the wrong kind** (a Person where a Site is wanted, and so on), counted per act. A further 174 (4 seasons) are
  a Record of the wrong sub-kind and 216 are `exists:DocketItem` = 0, which is a world read and stays a refusal. **No
  refusal is an eligibility refusal.** Wrong-kind refusals repeat: 4,620 acts fall on 3,286 distinct (seed, actor, verb,
  subject) pairs, so 29% repeat a pair already refused.
- *Chains.* Of the deepest cross-person chains rendered from the real engine (seeds 0, 1, 2, 4, 5), 55 of 66 acts were
  refused (53 of 66 by the older suffix rule). Of 4,951 acts at cross-person depth ≥ 2, 3,604 were refused. The cross-person
  share is 30.4% as `storybar` reads it and 17.9% counting only executed acts with an executed antecedent.
- *Under-counting.* A contested act refused at admission never enters `SeasonDriver.resolved`, so the committed `aperture`
  reports 1,182 acts for the run in which 1,511 acts emitted Events (G-02). R-05 records this as a limit; every reader of
  `resolved` inherits it.

**Evidence [toy].** At an 80% refusal rate (the engine's), the ladder-plus-tribunal arm's arc rate falls from 0.38 to 0.21
while a forcing director holds at 0.71. Both lawful routes collapse on a mostly-refusing substrate (`reports/R03`).

**What it means.** Any measurement of arcs, ambitions or closure on the shipped realm is read through a refusal floor of
about three-quarters. Two cautions keep "make the verbs execute" from becoming "delete the refusals": refusals are
witnessed and deposited as claims (`loop/witness.py:245-256`), and `claim_landed` supplies 13,074 of 14,357 delivered
questions at seed 0 (probe P9). A change that removes wrong-kind candidates may remove the world's motion along with its
waste; the register's G-01 control therefore reads questions delivered and claims deposited as well as executed counts,
and **the share of questions fed by a refusal-kind claim has not been measured.**

**Missing in code.**
- G-01: the formation question (below).
- G-02, G-03: one owner of "attempted" and one of "refused"; the instrument half moves no hash, the retry half does.
- G-04: Proposition referents reach almost no question (`commit` admissions on a Proposition: 3 of 180); act-minted
  Propositions are empty.
- G-05: `build`, `found` and `work` cannot execute in computed play by any typing, because no computed act declares a
  works (ED-IN-0297, H-165 limit 2).
- G-06: `migrate` is the largest refusal mass and refuses *after* admission (H-168).
- G-08, G-11, G-12: extend `aperture` and `arms` (do not write a new harness) to pool seeds, split `need` by what it is
  about, and sweep a build flag as well as a fixture.

**Owner and status.** The formation question is **H-156** (`engine/season/hole_register.yaml:3615`): an open ruling (**taken since as M19 (a)**, `workplans/valoria_master_workplan_v10_part11.md:13`) that
runs CLAUDE.md §0's five steps and leaves the row open, because two defensible options (decline wrong-kind candidates at
formation, or accept the refusal tax) lead to materially different corpora. **The first delivery wrongly said this
question "sits in no workplan"; the register's v1 design for it was withdrawn after the critic opened H-156.** It is the
register's one new escalation (§11).

**Wrong if.** Removing wrong-kind candidates lowers questions delivered, claims deposited or scenes beyond the seed-to-seed
spread; or pooled executed counts per verb fall. Then the refusals were doing work and the floor is a feature.

**Grade.** [engine], high for the counts (the probes agree with each other and with `aperture`'s own control to the hash);
medium for the interpretation.

## 4. T2 — The world needs a motive layer, and part of it is already there

**Claim.** Bottom-up play gave causal depth with no "why". A standing motive, held by the actor as its own state and
naming referents rather than outcomes, restores the "why"; the engine already has most of the carrier.

**Evidence [toy].** Four regimes, 300 seeds each (bottom-up BU, blind script TD, replanning director TDR, motive hybrid HY).
The share of events whose motive outlasts the moment: BU 0.43, TD 0.36, TDR 0.23, **HY 0.80**. HY minus BU is +0.35 to +0.39
(95% interval) and kept its sign in all five world conditions. The "fields present" measure of legibility does not
discriminate (1.00 in every regime) and should not be used (`reports/R02`).

**Evidence [engine].**
- `ambitions`, `goal_referents`, `attention_key` and the Q4 `need` question are on the run path. `need` supplies 149–174
  of 606–642 scenes per seed (24–28%); a `need` scene about a goal Proposition is 43–53 per seed (**7.1–8.5% of scenes**).
- `goals.yaml` has 38 rows: 24 orientation (they mint no Proposition), 6 seat-holder, 4 deed-doer, 4 rung. In the shipped
  realm 12 of 38 mint a Proposition, 55 `commit` edges exist, and 35 of 83 persons hold a goal ambition.
- **No seat-attached goal binds anyone in the shipped realm** (G-09): the two seat rows sit on foreign seats, seated only by
  `build_realm(foreign=True)`. Cohorts carry no wants.
- Ranking the ambition question first is a measured trade, not free: it starved news (`news.told` 14 → 7, events 21,735 →
  15,738; the `attention_key` docstring in `queries/world_q.py`, reported in `reports/R01`).

**Corrected since first delivery.** "The ambition question won 51 of 803 deliberations" (from
`proposals/2026-10-13-narration-mechanisms.md`) is **not reproduced as defined**; the register's probe counts scenes by the
occasion they carry, and the figures above replace it.

**What it means.** The motive is the existing ambition (a `commit` to an OUGHT) plus an *authored ladder of typed stages* in
`goals.yaml`; the current stage is derived from the person's own ledger every time, so there is no arc store (TL §1–§3).
The starved `need` question is fixed by promoting a stage's referents for one season per deadline period with a staggered
per-person phase (TL §3.3; **R3′ and the stage `deadline` are excluded by M20**, `v10_part6.md:172`), which avoids the measured news regression because the commits are not all minted at season 0.

**Missing in code.** G-09 (seat rows), G-10 (24 of 38 rows are orientation-only: authoring), G-11 (the `need` share is not
separable by what it is about), G-12 (`arms.py` can sweep one fixture and no build flag). The ladder runtime itself is
G-13 (§5).

**Wrong if.** Raising ambition weight raises the share of chain acts whose winning question was an ambition referent
while `news.told` collapses (the falsifier in `reports/R01`); or human readers find the thrust no more legible.

**Grade.** [toy] low-medium for the "why"; [engine] high for the carrier's state.

## 5. T3 — Arc shape needs a goal ladder and a closure form, together

**Claim.** Neither half alone produced an ordered arc. A ladder of short- and medium-term goals under each ambition, with a
decisive-form closure (a bound peace, a threshold-raised tribunal), did, without any engine writing an outcome.

**Evidence [toy]** (constrained world, 300 seeds per arm, `toy/exp_con_out.txt`; arc rate minus a shuffled null):

| Arm | Deaths/run | Arc − null [95% interval] | Complete beats |
|---|---|---|---|
| Bottom-up | 0.36 | −0.056 [−0.083, −0.027] | 0.077 |
| Ladder (HYg3) | 0.30 | −0.020 [−0.062, +0.022] | 0.160 |
| Ladder + threshold-raised tribunal (HYg3d) | 0.28 | +0.010 [−0.046, +0.067] | 0.357 |
| Forcing director, forced yield (TDR) | 0.41 | +0.099 [+0.041, +0.156] | 0.767 |
| Decisive-form set piece, no ladder (TDSc, non-lethal) | 0.33 | +0.016 [−0.019, +0.051] | 0.123 |
| **Ladder + decisive-form set piece, bound peace (HYg3c, non-lethal)** | **0.24** | **+0.244 [+0.188, +0.303]** | 0.517 |

Earlier, in the unconstrained world, ladder-plus-tribunal measured +0.09 [+0.04, +0.15] and matched the scripted director
(`reports/R03`, `R04`); **it does not transfer under the constraints** (+0.01). Of the constrained world's seven
pre-registered predictions, three held (K4, K6, K7); the misses are in `exp_con_out.txt`.

**What the toy cannot say.** The arc test is a three-act template; it credits a lone interior closing event at any season
and counts silence as an ending, so an arc rate is meaningful only beside its shuffled null and a bookkeeping null. The
constrained design was written after seeing results. Whether a plain exile closes an arc as well as a settlement did
(first delivery: +0.01 for exile) was run inline and **not saved**; `toy/regimes10.py` implements both (`exiled`,
`settled`) and the comparison can be re-run. [UNVERIFIED from committed outputs.]

**Evidence [engine]: the closure routes exist in the tree only as verbs that barely execute.** Docket → `determine`
3/43; bound peace → `covenant` 0/70; succession → `succeed` not resolvable (IN-61, stopped, H-230); an authored
arrangement set piece → only through `determine`'s effect (G-14). Two things exist and are underused: a MATTER crossing
that "emits and writes nothing" (`loop/matter.py`; so a threshold can raise a docket matter without acting), and
`world_q.endings_reached` over `rosters.yaml: endings`, an executable terminus over holds reported once per season
(`world_q.py:2084-2137`, `driver.py:520-523`), **which TL does not mention and goal-stage termini should compose on.**

**What it means.** Lawful top-down is arming engines the corpus already uses, not writing beats. Among 50 classified endings the
largest closing class is a decider (20), then a crossing-forced close (19), a never-closing state (10), a roll (9) and a
plain threshold (8); the closure engines TL arms are the decider and the threshold. The seven ways
the corpus achieves arcs (accrual, exposure, succession, decision point, contest, conjunction, held control state) are in
`reports/R02`; most character "arcs" are positions, not trajectories (§8.2).

**Missing in code.** G-13 (the whole ladder runtime: axes roster, `axis:`, stages, `current_stage`, stage referents,
pulse promotion (R3′ excluded by M20); no new design beyond TL, but name the key `goal_stages`, since `ladders` already means two other things in
the package), G-14 (closure verbs; ordering), G-25 (termini are unevaluated prose), G-26 (axes lack rows).

**Wrong if.** After the closers execute, stage-referent hit rate at the new refusal floor stays at the old one (TL B3.2); or
the arc rate under the shuffled and bookkeeping nulls does not exceed bottom-up's with the ladder on.

**Grade.** [toy] low; the ordering of mechanisms is suggestive, the magnitudes are not Valoria's.

## 6. T4 — Killing has no consequences today, and fighting authority is easy

**Claim.** The user's constraints are: arcs must not need an NPC's death; death should be extremely rare; fighting anyone
with authority or standing should be hard; and where killing happens its consequences should be significant. The engine
meets none of these today.

**Evidence [engine].**
- *Deaths.* Seeds 0–4, 4 seasons: **20 deaths in 20 seed-seasons; 16 of the 20 were seat-holders; 11 came from `accept`
  and 9 from `fight`.** In **0 of the 11 `accept` deaths was there a `challenge.issued` Event aimed at the acceptor by the
  accept's subject, in either direction** (15 `challenge.issued` Events in the five logs against 11 accept-kills): an
  `accept` forms and resolves as a duel with no challenge behind it (`verb_table.yaml:796` says so as a named residue).
- *The killing's reach.* `fight` requires only existence and co-location; its `Felled` band deletes the person and emits
  `person.died`; the "deontological gate" the row mentions does not exist. The cast is closed (ED-WR-0011), so every death
  is permanent.
- *Consequence.* No claim on any of the 16 dead holders' seats has predicate `person.died` or `tenure.closed` (H-206), yet
  the vacancy is acted on through the world read `vacancies` (9 of 16 seats draw `confer.refused`). The dead man is named
  in occasions (`occasions_naming_dead` = 36 across the 20 deaths), but **no later scene pairs the killer with a claim about
  the dead** (H-209).
- *The access gate.* It exists and is live on `move` and `migrate` (`world_q.py:1250-1344`), but ships with
  `guards=False`; only 3 guard rows exist for 31 seats (`cohorts.yaml:127-130`), so a "gate" protects 3 of 31 seats and the
  seats the user means by "authority" are unguarded.
- *A non-lethal duel exists, unwired.* PC-10a landed `fight(terms=)` with stop-at-first-wound and yield terms
  (`modules/combat/wrapper.py`), inert: the season passes no `terms`. RS-25 (Jordan, 2026-10-14) rules non-lethal duels in.

**Evidence [toy]** (constrained world). Death requires a skill-1 target and a 1% roll; harm against a standing-holder is
refused 90% of the time unless provoked, and the usual weapon becomes an accusation. The ladder with a decisive-form set piece
and a bound peace had the lowest death rate of any arm tested (0.24 per run) and the strongest signal. Making a killing heavy: a killing
at season 10 in the ladder-plus-tribunal world, paired against the same seed without it, drew about 9.5 acts against the
killer from about 4.9 distinct actors, about 1.3 tribunals naming the killer, no extra deaths (no runaway feud), and a world
about 7 events quieter; giving kin an "avenge" ambition added nothing measurable. Moderate, not significant (printed, not
saved). Among runs that passed the arc test before the constraints, the main thread closed on a death in 99% (forcing
director), 94% (lethal set piece) and 98% (ladder + lethal set piece) of runs; ladder + tribunal, 3% (`reports/R07`).

**Corrected since first delivery.**
- The register's v1 proposed a fixture putting non-lethal `terms` on every `fight`. That contradicts PC-10b's own text
  (*"`fight` — an unchallenged assault — keeps lethal terms"*) and is withdrawn (G-16); the seam is PC-10b's.
- TL's proposed `Slain` band is **not** a duplicate of PC-10a: a felling kills under any term, and TL's band would split
  down-alive from dead, a different cut. Only the *challenged-duel* case overlaps.

**Missing in code.** G-15 (the `accept` route to death; PC-10b's refusal of an `accept` with no held challenge would remove
it, conditional on H-240's route being chosen), G-16 (terms through the season seam: PC-10b), G-17 (killer and dead never
meet in a question: H-209), G-18 (a dead holder's seat is named by no claim: H-206, though the vacancy is acted on),
G-19 (guards: authored rows plus an A/B that needs G-12), G-20 (no committed reader of deaths by killing verb).

**Owner and status.** PC-10b is stopped at B-Y (BLK:H-240, a grammar-change route unchosen); H-206 and H-209 route to
IN-12 step 5 (BLK). TL §5.1–§5.3 compose on these; the one live design choice was where the `Slain` edge sits (D1, §11; **since ruled M21 (a): no `Slain` band**, `v10_part6.md:181`).

**Wrong if.** Pooled over seeds, `accept` deaths do not fall when an `accept` needs a held challenge (then `accept` was not
the route); or the consequence package produces a feud that raises deaths per run.

**Grade.** [engine] high for the counts and the missing links; [toy] low for the consequence magnitudes.

## 7. T5 — Do not build the tempting things

**Claim.** Three designs look natural and each failed its own test in the toy; nothing in the tree already does any of them
under another name.

**Evidence [toy].**
- *Lookahead-biased choice* (a narrative term on the chooser, computed by rolling candidate branches forward): at strength
  4, 126 leveraged decisions per run, about 3,200 rollouts, **about 270 times the run time**; 32% of leveraged decisions
  flipped; closure and cross-person depth rose (a proxy the method rewards, so partly circular), but the arc rate minus the
  shuffled null was **−0.08 [−0.14, −0.01]** against −0.01 with no leverage, and the share of events with an explained motive
  fell from 0.58 to 0.29 (`reports/R03`, `toy/lookahead.py`, `lb_more_out.txt`). The tilt moves choices the actor's own
  scores did not favour, which weakens the "why".
- *A blind script* (TD) violated world constraints in 96% of runs unperturbed and in every run after the thread leader was
  killed at season 10.
- *A forcing director* gets its arcs by dictating a death in 99% of the runs where it passed the arc test.

**Evidence [engine].** Register §4: the chooser's score has three terms (pursuit alignment, stance, urgency; `decision/choose.py`
`score_terms`, "the ONE owner of the formula") and no term reads an outcome probability; the only `deepcopy` in the
season's queries is the person projection, not a world rollout; there is no arc carrier (`class (Arc|Story|Plot|Thread)`:
0 hits); and a MATTER crossing "emits and writes nothing" (`loop/matter.py`), a refusal emits rather than raises
(`loop/resolve.py`). The Key substrate that would have carried an emit/consume interface is retired (ED-IN-0232).

**What it means.** Outcomes stay with people. If a sigma-leverage correlate is ever wanted it lives at the choice stage, in
τ units of `choice_temperature` and soft-capped like `sigma_leverage.soft_cap`, never on the resolution and never removing an
option; the narrative-engine rules R-AI and F8 would be overridden by it, and F8 would become a dosimeter that reports the
change in outcome probability per unit of leverage. That is a bounded option for a few thread-bearing actors, after T1.

**Missing in code.** Nothing, by design. The refusal of need-triggered outcome injection, even with permission to overrule
it, stands on three grounds: a threshold that acts is an actor, an injected beat has no author and cannot be contested,
and the storybar would end up measuring its own injections.

**Wrong if.** A drama manager shown, with human readers, to beat the ladder-plus-closure route; no such evidence is in the
precedent (`reports/R01`).

**Grade.** [toy] low for the magnitudes; the direction agrees across the arms.

## 8. T6, T7, T8

### 8.1 T6 — The deepest premise is the least buildable

**Claim.** The ten goal axes ask for things the engine cannot yet carry: healing the Calamity, hiding the threadwork truth,
overthrowing the caste system.

**Evidence [engine].**
- *Heal the Calamity (G-21).* **0 threadwork modules load in a season run** and no thread, lattice or Calamity event kinds
  exist; the coupling rule ships at `lattice_coupling=0` (`data/fixtures.py:616`) and, set to 250, moves only
  `Site.condition`; the one mend, `restore`, executes 0 of 250. Askeheim holds no Site in the built realm (`loop/matter.py`
  docstring). Owned by H-236 and H-85 (no source, no thread-sensitivity carrier); IN-06 was re-reviewed: "nothing plugs".
- *Ageing (G-22).* `age_at_build` is not sweepable on a built world (`Person.born` is fixed from `DEFAULT_FIXTURES` at
  construction, `state/carriers.py:687`; sweeping it left the hash unchanged), and 29 of the 46 registry rows have `age: null` (H-208). `body_step` and `illness_rate` do move the world and ship off, so the world is quiet by construction.
- *Caste (G-23)* has no readable store or query: `grep -rnwi caste engine --include=*.py` returns 0 hits. TL takes it as a
  Query over affiliation convictions (D3).
- *Hide the threadwork truth (G-24)* has no goal row; the nearest, `goal_varfell_thread_knowledge`, is the opposite pole.

**What it means.** Axis J (heal) stays out of the design until H-236 has a source. Axes H and I need authored content and a
Record question the design leaves open.

**Grade.** [engine], high: these are absences found by executing the thing that would show presence.

### 8.2 T7 — Authoring is the largest content job

**Claim.** Most of the arc content does not exist as data.

**Evidence [engine].**
- All 46 NPC cases carry `ends_when` as **prose that no code evaluates**. How many say nothing executable depends on the
  rule: the extractor's own `never` marker gives 40 of 46; a strict regex gives 28 but was fit to the strings after reading
  them. The first delivery's hand classification (by one reader) was: forks 11, exit events only 7, terminus presumed 12,
  nothing authored 16. The claim the register uses is the first (prose, unevaluated), not any one count (G-25).
- Where a trajectory exists it is accrue-then-fork: 10 of the 11 forks name a cumulative or graded variable; no middle beat is
  authored. Of 50 classified endings, 16 are not multi-season arcs (10 never close, 3 name no closing condition, 3 resolve
  in one roll).
- The ten axes lack referent-bearing goal rows: per TL §6, benevolence, hide-truth, caste and heal have none; four others
  have one or two; suppress-revival has several (G-26). Existing opposing poles are already authored for four axes
  (suppress vs revive; resist Altonia vs the Kommerkiarios treaty row; hide vs "Thread truth accessible"; the Church vs
  Hafenmark), and the missing poles (nobody defends caste; nobody opposes healing) block arcs on two.

**What it means.** Every axis has a non-lethal closing act in existing verbs (a determination, exposure, schism, an
establishment, a revocation, a conferral, a completed work, a restoration), so no axis needs a death. The toy's "accuse" step
stands in for what the axes need: a case opened, a record destroyed, a determination won. Stage predicates must be typed
per referent kind (person, record, seat, rung, site, or institution-wide orientation).

**Grade.** [engine], high that the data is prose; medium on counts.

### 8.3 T8 — Metrics fail quietly

**Claim.** Every instrument built or read in this session passed something it should have failed.

**Evidence.**
- *The first arc test was vacuous* [critic F1]: every witnessed act deposits a claim and the gate mints a Receipt for it
  (`loop/witness.py:654-657`, `state/world.py:1306-1322`), so "moved and was seen" counted as an arc. The design now uses
  named field rosters, planted cases that must read FALSE, and a bookkeeping null.
- *The toy arc test* credited a lone closing event at any season and counted silence as closure; v1 had four instrument
  defects (a prize/duel thread split, a climax outside its own peak window, tied climaxes, an early transient inflating the
  null) and was re-run as v2, disclosed. Pre-registered predictions scored 11 of 21 (v1), 13 of 21 (v2), 4 of 7 (ladder),
  3 of 7 (constrained).
- *`aperture`, `storybar` and `chronicle` count refusals as story* (G-02, G-27): 55 of 66 acts in the deepest chains were
  refused, and the cross-person share is 30.4% as read against 17.9% executed-on-executed. The default reading is IN-19's
  pinned meaning, so the fix reports an executed-only reading beside it, never instead.
- *Two definitions, four readers* (G-03): the driver, `witness._happened`, `is_deed` and `corpus_run.attribute` classify a
  graded loss differently.
- *My own corrections in this session* (§9) are the same failure at a smaller scale.

**Practice.** Read an arc rate beside a shuffled null and a bookkeeping null; give every result claim the test that would
have shown it wrong and that test's outcome (CLAUDE.md §0.1 pt 3); put a structurally independent, read-only critic on every
judgment node; and say plainly when a re-recorded golden moved.

**Grade.** [critic] and [engine], high.

## 9. Corrections: every first-delivery figure that changed

| First stated (chat reports `R01`–`R10`; register v1 where marked) | Source of the first figure | Now | Source of the new figure |
|---|---|---|---|
| 929 of 1,318 acts refused (70.5%), one seed, two seasons | `narration-mechanisms.md` scratch instrument | **76.2%** of 7,402 (seeds 0–4, 2 seasons); 76.8% at 4; 73.8% / 73.9% without graded losses | P1, P10 |
| 33% (439 acts) aimed at a subject of the wrong kind | same | **32.2%** (2 seasons) / **28.7%** (4), per act, classes corrected | P10; P3b's 33.1% was calls, not acts, and is withdrawn |
| `determine` refused 7 of 7, `confer` 4 of 4, `commit` 74 of 74 | one seed | executed/attempted at 4 seasons: 3/43, 10/111, 8/564 | P1 |
| 66 of 81 chain acts refused (81%), six seeds, suffix definition | chat run | 55 of 66 (83%), seeds 0, 1, 2, 4, 5, driver's definition; 53 of 66 by suffix; seed sets and definitions differ, all near 80% | P7 |
| The ambition question won 51 of 803 deliberations | `narration-mechanisms.md` | not reproduced as defined; goal-about `need` scenes 43–53 of 606–642 (7.1–8.5%) | P2 |
| 28 of 46 cases have no authored or only a presumed terminus; 16 have nothing | hand classification | all 46 are unevaluated prose; 28 (regex fit) to 40 (extractor marker) say nothing executable; the claim stands, the count is not robust | P6 |
| The candidate-typing decision "is unruled and sits in no workplan" | orchestrator's reading | **wrong**: it is H-156, an open ruling that survives all five steps; the register's v1 design for it was withdrawn | critic A1 (`reports/R15`) |
| "Closure through settlement works; a plain exile does not (+0.01)" | inline toy run | settlement arm saved (+0.244); the exile comparison was not saved | `exp_con_out.txt`; [UNVERIFIED] for exile |
| *Register v1:* TL's `Slain` band duplicates PC-10a | register v1 | not a duplicate; the seam is PC-10b's; the default for an un-negotiated `fight` is lethal by PC-10b's own text | critic A7 |

## 10. What none of this establishes

- **Whether players find any of it legible or compelling.** No step used human readers, and the repo's own research says no
  method certifies generated content as good (N-5). Only narrower claims can be falsified; human reading closes the rest.
- **Anything about Valoria's balance or content from the toy.** The toy's world, metrics and arc template are the author's.
  Only the refusal rate, the goal rows and the death counts come from the engine.
- **The primary literature.** Compton, Smith and Whitehead, Ryan and colleagues, and drama-manager work outside the repo
  (Façade, Riedl) were read through the repo's research files and not re-fetched. [GAP at filing; read since in `research/emergent_narrative_literature/`]
- **Two-level lookahead, other value proxies, any human judgement of "construable".** Not tested.
- **A player character.** A player's acts come through `harness/play_surface.py`'s callback and bypass `opening_set`, so any
  formation filter binds NPCs only; this set of documents says nothing else about a player character.
- **The share of delivered questions fed by a refusal-kind claim.** Unmeasured; G-01's motion control depends on it.

## 11. What needs Jordan, and where each item lives

*As of 2026-10-25. Decided since in the v10 plan: H-156 = M19 (a) (`v10_part11.md:13`); D1 = M21 (a) (`v10_part6.md:181`); D4 = M20, narrowed (`v10_part6.md:172`); PC-10b / H-240 = route (1) (`v10_part3.md:192`); ED-IN-0297 closed by a superseding row (`registers/editorial_ledger_in.jsonl:81`).*

| Item | Question | Lives in |
|---|---|---|
| **H-156** | decline wrong-kind candidates at formation, or accept the tax (supplied with the measurement above) | `engine/season/hole_register.yaml:3615`; register G-01, §5 |
| D1 | whether a beaten fighter is ever killed outright, and where the `Slain` edge sits (the un-negotiated `fight` default is already answered: lethal) | TL §10 |
| D4 | where "a sequence of ladder stages" (licensed 2026-08-18) ends and "an entire arc" (not licensed) begins | TL §10 |
| PC-10b / H-240 | the grammar route for a held challenge (already Jordan-gated) | `v10_part3.md:192` (was workplan v9 part 7 §PC-10) |
| ED-IN-0297 | where a works comes from in computed play (already open) | `registers/editorial_ledger_in.jsonl` |
| Contraventions | ED-IN-0225 (narrowed), `narration-mechanisms.md` §3.4, the `oblige` declared-term precedent, the 2026-09-03/04 combat rulings, G4 | TL §9 |
| Assumptions | who holds axis 2 (the Church, from canon); caste as a Query over affiliation convictions (D2, D3) | TL §10 |

Everything in this document is reference. Nothing here asks a future session to build anything; what is missing in code is
the register's, and what to build and in what order is TL §8's and the register's §5, both held back in full.
