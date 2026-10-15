## Status: **REFERENCE.** Not canon, not a proposal, nothing ratifies on merge. Creates no plan position, allocates no ID, writes no ledger row.
## A terminal NERS pass whose verdict was the thing asked for (`CLAUDE.md` §0's one exception), recorded beside `what_valoria_is_and_what_runs.md` as its precedent. **The record dies when its subject dies**; where it disagrees with the tree, the tree is right and this file is stale.
## Written 2026-10-14 at HEAD `092fc45`, with every v9 position assumed built. Method: `skills/ners/SKILL.md`. Produced from ten read-only subagent digests, two independent read-only critics (Fable, Opus), and an Opus rewrite; the orchestrator re-opened the disputed lines and applied two corrections after the rewrite. Section 9's recommendations are text for the owning lane or for Jordan, not scheduled work.

# NERS PASS: Valoria, assumed built to the v9 plan — INSTRUMENTS: A (+ the B arithmetic by hand)

Repository `jordanelias/ttrpg`, HEAD `092fc45` (shallow clone, clean tree), 2026-10-14.

## 1. Verdict, scope, method and coverage

**Verdict: with every v9 position assumed built, Valoria is a sound simulation of persons at seats, but it is not yet a game of distinct persons. Its architecture holds against the attacks this pass ran. It fails on four counts that survive completion of the plan:** (1) nothing carries per-person difference into combat or mass battle, and only the social contest gains it, after `train`; (2) resolution reaches the one ladder by two dice substrates (with a logistic side-channel in combat) and several pool and Ob formulas, and leaves it for three result vocabularies, with odds that are non-monotone and nowhere shown; (3) the player is a callback over a candidate set the engine forms, with no built surface for creation or the grid; (4) the apparatus around the game is about ten times the game's size, and some of it is read only by itself. Grade: **paper**. Nothing was executed for this pass, and the planned-built object cannot be executed by construction.

**Target and head.** `CURRENT.md:17` names `engine/season/` as the game code and `CURRENT.md:19` names `workplans/valoria_master_workplan_v9.md` (+ `_part2`…`_part8`) as the one active plan. Layer 1 is `architecture/meta/00`–`04`. The repository's own last instrument reading, which I did not re-run: M1 not met; THE NINE met 3 (R-01..R-03), partial 5 (R-04, R-06, R-07, R-08, R-09), not met 1 (R-05) (`workplans/valoria_master_workplan_v9.md:183`).

**The assumption (the user's, binding).** Every stub, unbuilt or planned item is treated as BUILT. A defect counts only if it survives completion of the eight v9 plan files. Where the plan says "no position builds this", or an item is LEAVE, unscheduled, held, or "[medium; Jordan to correct]", it counts as a design gap, not a stub. A Jordan ruling that makes an effect absolute is not a finding. Code claims cite the working tree. `.designs/` and `proposals/` are cited for intent only.

**Method.** `.claude/skills/ners/SKILL.md` (§§2–10) owns the method and `CLAUDE.md` §0.06 owns the definitions. A PASS is licensed only by a named failed attack. E is scored last, as a ratio. R-PLAYER binds only at seats a player can occupy, and R-WORLD binds everywhere. Parameter values are Jordan's (`[OPEN — Jordan tuning]`), never structural defects.

**Coverage, stated honestly.**

| class | what |
|---|---|
| **Opened first-hand this pass** | Every `file:line` in this report that carries no tag. That covers the whole MUST-REOPEN list I was given, except `loop/matter.py:152–236`. It also includes three files I added: `loop/witness.py:227–250, 486–535`, `tools/evacuation_plan.py:1–25` and `workplans/…_part2.md:158–182`. Counts come from read-only parses of `verb_table.yaml`, `offices.yaml`, `cohorts.yaml`, `arrangements.yaml`, `references/ci_checks_registry.yaml` and the 20 ED ledger files, and from `git ls-files … \| xargs cat \| wc -l`. |
| **Relayed** (`[RELAYED]`) | Readings from the ten subagent digests and two critics that I did not re-open. Each is tagged where used. |
| **Not read** | UI Parts 4–10; squad-engagement Parts A–D; most of the `canon/philosophy` bodies; `.audit/` (by rule); `proposals/2026-08-25-throughlines-and-precedent/` (headings only, by file name); the bodies of `governance_play_redesign_v1.md` beyond a grep. |
| **Executed** | Nothing in the repository. The only computation was read-only counting (`git ls-files`, `wc`, `grep`, a `yaml.safe_load` of three registries) and the dice arithmetic by hand. |

**Attacks actually run:** cutting AX-1; looking for a verb that raises instead of emitting; reading for mid-round writes against the frozen world; cutting the budget; the chooser score, term by term; the dice arithmetic; a plan-closure search for each defect (grep of workplans, proposals and ledgers); a read-only walk of AX-7's falsifier over the five `Claim` construction sites. **Not run:** any play-length behaviour, any equilibrium analysis of the act economy, or the executable form of AX-7's falsifier.

## 2. The two lists

**MUST BE STATED AS A LIMIT**

- *"Personal-scale resolution" varies by person.* No carrier in combat or mass battle survives the plan. The contest varies by person only where a case names a vocation (A1) [C1].
- *"One degree ladder for every scale"* (`03_VERBS_AND_LOOPS.md:272–275`). The margin ladder has one owner, but three result vocabularies and a non-margin mass-battle result sit beside it (A3) [§7.3 methodology].
- *The player can act in the world as a person.* The player overrides a chooser over a set the engine forms. Creation, development and the grid mode have designs and no build batch (A2) [C5].
- *"No character touches the world directly"* holds at runtime. The falsifier was walked, not run. By its letter, the deposited VALUE is still the engine's resolution at every site, and the actor's own deposit is not refracted at all (A9) [C2].
- *A demand travels up a rung to a person who filters it.* For the petition path it does not: a computed petition is addressed to its own subject (A5) [§7.1 S-UP].
- *The world throws hooks unwatched.* This is unmeasured under planned=built. The one datum is a one-seed scratch run in which a third of acts targeted the wrong kind of subject (A4, T5) [§6 R-WORLD].
- *History improves a thread roll.* It does not (A8).

**MAY BE CLAIMED, HAVING SURVIVED**

- *Only a person acts* (AX-1). **Residual:** a player has no designed way to read a faction.
- *Refusal emits* [NULL: `verb_table.yaml` — all 45 rows carry `emits_on_refusal`; that every effect body honours it is RELAYED].
- *The world is frozen during deliberation.* **Residual:** a stale comment at `matter.py:113–116` says otherwise.
- *The scene budget is the mechanism of triage.*
- *Draws replay exactly.* The draw key is `(world_seed, tick, pid, purpose)` (`state/ids.py:45–46`), and the chooser's noise is keyed per candidate (`choose.py:316–336`). Attack: find a positional stream. None found.

The attacks behind the first four, and why each failed, are in §5's N-line table.

## 3. The NERS axis table

| axis / test | verdict | what would overturn it |
|---|---|---|
| **N (six directions)** | FINDINGS, narrowed (§5). Holds: AX-1, refusal-emits, frozen world, scene budget, ENCOUNTER (MEDIUM). False N-lines: `urgency`, and mass battle's survivor-ratio "degree". | A named object whose loss survives the cut in the lateral direction. For example, if `ENCOUNTER`'s two consumers (grid suspension, deferred contests) folded into RESOLVE with no second barrier, the ENCOUNTER N-line falls. |
| **E-OVERHEAD** | FINDINGS. Game objects: 45 verb rows (34 carry a `requires_typed` key, 6 of them set to `none`, so 28 are typed and 17 are not; parsed from `verb_table.yaml`), 4 with `contests:`, 15 pursuits × 7 axes, 29 seats (14 with `revocation: null`), 37 cohorts, 7 arrangements (14 declared keys, only `disposes` read), 66 fixture knobs (13 annotated "(control, SHIPPED)"), 10 rows carrying a retiring `scale:` key. Process artifacts: §7. The watchlist is in §5. | A cut object whose loss turns out NOT to survive. For example, if the 13 dark controls each guard a play behaviour Jordan has ruled in, they are N, not overhead. |
| **E-LEGIBILITY** | FINDINGS. Contest and season odds are non-monotone in score and appear on no surface (A3). The pursuit→act mapping is indirect (15 pursuits projected through 7 axes onto 45 verbs, `rosters.yaml:2295–2425`, `choose.py:403–406`). | A shown odds surface, or a monotone pool/Ob rule. |
| **R-COMPLETE** | FINDINGS. Dead zones: S27.4 refusal at Ob > 2×pool (`sigma.py:190`); pool 2 can never be Overwhelming at Ob 2 (`degree_extension.py:31–34`, ruled "accept"); the σ-boost floors to zero below one die (`orchestration.py:1284–1289`). Mass battle is uncalibrated at season scale (A7). Coherence has no rule after the crossing (A8). The design does not say what an investigation finds (A8). | A branch shown to be written, e.g. a ruled weight→troop conversion. |
| **R-VARIETY** | FINDINGS. One build fights like every other (A1). The player's act set is the engine's candidate set (A2). | Two persons with different authored interiors producing different combat distributions at fixed seeds. |
| **R-WORLD** | FINDINGS, [CONFIDENCE: medium]. `at_war` is False in every buildable world, "a fact about what nothing yet chooses to utter" (`faction_q.py:232–240`). Hunger, ageing and illness ship at control (`fixtures.py:530,542,543`). The one-seed act-content datum (T5). Forcing is now scheduled: IN-35, IN-36 and FORCE-WEATHER (`_part5:144,158`; the v9 plan `.md:343`). The Calamity's class is answered [medium] (forcing proposal, `## Status` line). | A seeded multi-season run of the planned-built loop in which an unwatched seat emits a war, a succession or a dearth that changes a later decision. |
| **R-CHOICE** | FINDINGS, upper bound (A5). At the lord's seat, intent "fill the treasury": `levy` costs one scene and writes only `Rung.stores` (`verb_table.yaml:629–651`), and its other cost depends on who witnesses (*decaying cost*); the slower yield route through `restore`/`work` is the second act (A5). The dependency is the act economy, which IN-14 rules [medium; Jordan to correct]. | An equilibrium run over `levy` against the slower `restore`/`work` yield route (A5). |
| **S-UP** | FAIL for the petition path; PARTIAL for the docket path (A5). | A computed petition addressed to a seated person at the rung above its subject. |
| **S-DOWN** | PASS in shape (telling is published, distorts through `refraction_gain`, and is picked up by the hearer's own channel). The tree delivers thinly: 4 of 1,270 `told_by` claims arrived by a telling (narration datum, one seed). The old addressed Scene Slate fails, and it is intent only. | A telling routed to a named recipient by the engine. |
| **S — coverage · pause · methodology** | FINDINGS. Coverage: the contest at RESOLVE/ENCOUNTER is the one carried vertical seam. Mass→personal duel, thread→mass and Domain Echo have no carrier (A2). Pause: a human callback runs inside the per-person map that `deliberate.py:116` marks parallel, and nothing specifies how it blocks. Methodology: A3. | A carrier named for each uncarried direction; a specified suspension. |
| **the design's own falsifier (§8)** | HITS. They cluster in one family: fixtures standing where an opener's or arrangement's declaration should be (§6). | A hit traced to a person's act. |
| **self-audit (§9)** | Both sweeps run (§6). | An independent reviewer would add a play-length run, an act-economy equilibrium, and squad-engagement Parts A–D. |

## 4. Findings, worst first

### A1 · Nothing carries per-person difference across the contest scales

**Evidence.**
- **Combat.** The only input derived from a Person is `end = max(1, 4 − body_band_penalty)` (`seam/wrappers/combat.py:130–138`). `modules/combat/fight.py:45` builds `Combatant(a_id, end=a_end)`; every other field is a class default (`modules/combat/combatant.py:93–94`: strength 4, agility 4, history 3, weapon `arming`, armour `light`, tradition `none`). Pool and Ob both read `history` (`core.py:54–56`, `:115`), so every season duel rolls pool max(5, 3 + 6) = 9 against Ob 1.5 (`wrapper.py:181, :210`). The 16-state engagement graph and the derived weapons are reached through `end` alone.
- **Contest.** The pool is the capability for the verb's key, else `pool_default` 2 (`seam/wrappers/sigma.py:97–109`, `fixtures.py:381`). Ob is half the subject's capability, else `obstacle_default` 2 (`sigma.py:112–129`, `fixtures.py:383`). `leverage=0.0` is hard-coded (`sigma.py:147`). Capability is empty on 429 of 430 built persons (`requirements.yaml:77–79`; `rosters.yaml:1096–1101`).
- **Mass battle.** One infantry Line per side at `power` 4 and `command` 4, with troops equal to the raw sum of `Person.weight` (`massbattle.py:170–186, 196, 226–230`).

**Why it survives the plan.** `train` (IN-12 step 9, B-Q) writes `Person.capability` only where a case names a vocation. The only vocation key is `copying` (`rosters.yaml:1104–1106`), and J-13 (iii) is the adopted interim [medium; Jordan to correct] (`_part5:73`). R-09's by-person conjunct stays partial (the v9 plan `.md:189`), and J-13's remainder is §J.2 rank 1 (`_part5:449`). For combat, K-1/K-5 (a Combatant built from the person; loadout as `hold` tenures) "are NOT scheduled": they need `Person.attributes` (K-2), which "builds only with its first reader", and "K-2 is not ratified". M-2..M-6, U-4 and K-6 stay LEAVE (`_part7:44, :51`). After the plan, the contest pool varies by person where a case names a vocation. Combat and mass battle do not vary at all.

**Consequence.** A duke and a copyist fight identically. Their difference shows only through body band (fewer `end` points, fewer scenes; `budget.py:57–61`), seat (remit and office bonus) and stance. No Person reaches the physics below the seam.

**Overturned by:** a ruled source for per-person magnitudes with a scheduled first reader (K-2 with K-1), or a ruling that identical fighters are intended. **Confidence:** high.

### A3 · Resolution reaches one ladder by several roads, and its odds are not legible

**The die and the ladder.** Faces 1 → −1, 2–6 → 0, 7–9 → +1, 10 → +2 (`dice_engine.py:151–161`). Re-derived: mean = −0.1 + 0.3 + 0.2 = **0.4**; E[x²] = 0.1 + 0.3 + 0.4 = 0.8; variance 0.64; **σ = 0.8**. The ladder (`dice_engine.py:286–301`): margin < 0 is Failure, 0 ≤ m < 1 Partial, 1 ≤ m < 3 Success, m ≥ 3 Overwhelming (an extension may veto the last). The per-die literals have four owners: `dice_engine.py:174–175`, and in `sigma_leverage.py` the `PER_DIE` table at `:77–79`, `SIGMA_N_COEFF` at `:105`, and `MU_PER_DIE`/`SD_PER_DIE` at `:112–113`. That is against `CLAUDE.md` §8's one-owner rule.

**The season roll is discrete.** `modules/social_contest/roll.py` computes `net = roll_net(pool) + net_boost(0.0, pool)`. With leverage 0 the boost is 0, so `net` is an integer held in a float. A fractional Ob of k + 0.5 then behaves exactly as an integer Ob of k + 1 (the ceiling): Failure at net ≤ k, Partial at net = k + 1, Success at net from k + 2 to k + 3, Overwhelming at net ≥ k + 4. The fractional branch (`sigma.py:125–128`) is reachable only once `capability` is written.

**Equal scores (pool c against Ob c/2), re-derived by hand.** 2d pmf over −2..4: .01 / .10 / .31 / .32 / .19 / .06 / .01. 3d P(net = 2..6): .228 / .120 / .042 / .009 / .001. 4d P(net ≥ 2) = .5118 and P(net ≥ 3) = .2794, from the 4d pmf −4..8 = .0001 / .002 / .0162 / .0684 / .1639 / .2376 / .2324 / .1608 / .0807 / .0292 / .0074 / .0012 / .0001.

| c | Ob | P(Partial or better) | P(Success or better) |
|---|---|---|---|
| 1 | 0.5 | 0.40 | 0.10 |
| 2 | 1.0 | 0.58 | 0.26 |
| 3 | 1.5 | 0.40 | 0.172 |
| 4 | 2.0 | 0.512 | 0.279 |

Both series fall at c = 3. A more capable equal pair does worse than a less capable one, because a half-integer Ob costs a full success on a lattice. **At the shipped default pair** (pool 2, Ob 2, which covers 429 of 430 persons), Failure is 0.74, Partial 0.19, Success 0.07 and Overwhelming 0. Against Ob 2 at pool 2, the continuous Normal gives P(net ≥ 2) = 1 − Φ((2 − 0.8)/(0.8√2)) = 1 − Φ(1.061) = 0.144, while the discrete roll gives 0.26. Almost all of that gap is the missing half-unit continuity correction: with it, the Normal gives 0.268. So the two substrates disagree mainly on what a fractional Ob means.

**Substrates and filters.** Combat's main roll draws from the continuous Normal (`core.py:60`, `SL.roll_net_continuous`) and is graded on the owner ladder (`core.py:65–74`). Reads, binds and disengages resolve through a logistic (`core.py:26–41`). After the degree, combat applies fixed neutralise filters: parry 0.55, dodge 0.62, wind 0.50 (`config.py:131`, applied at `wrapper.py:321–333`). Season, contest and mass-battle dice are discrete (`orchestration.py:1288–1292`).

**Vocabularies.** `seam/ladder.py:209–251` maps a result to one of three vocabularies: the four-band margin; combat's Felled/Wounded/Untouched, read off wound state (`:136–182`); and march's Won/Lost/Unopposed, read off `attacker_wins` (`:185–206`). Mass battle returns a winner, not a margin. `03_VERBS_AND_LOOPS.md:286–289` says such a subsystem "has not met the contract". Its own four-label survivor-ratio degree (`massbattle.py:289–296`) drives nothing (`ladder.py:198–203`). Pool-from-score has at least four formulas: season `c` or 2; combat `max(5, history + 6)` with Ob history/2 (`core.py:54–56, :115`); threadwork `spirit×2 + min(3, history + 3) + TS//10` (`operations.py:246–247`); and the contest kernel `max(5, faculty×2 + Pool.BASE)` [RELAYED; BASE unverified].

**Legibility.** Nothing on a game path calls `p_success` or `eff_ob`: grep finds only `sigma_leverage.py`'s own wrapper (`:185–187`), kernel tests, a tool and a proposal. No surface shows the odds.

**Why it survives the plan.** No position unifies the substrates or the pool formulas. The mass-battle margin is "open MB-lane work" (`ladder.py:201–203`), with no plan position I found [CONFIDENCE: medium — searched `ladder.py`'s own note and the MB rows I read, not every MB plan row]. **Overturned by:** a ruling that combat is deliberately continuous and the season deliberately discrete, together with an odds display. **Confidence:** high on the arithmetic; parameters stay `[OPEN — Jordan tuning]`.

### A2 · The player surface is thin by construction, and one Layer-1 collision is unreconciled

The question of which player design wins is answered. A row naming a quarantined document is "reference, not a head" (`CURRENT.md:13`). `architecture/PLAN.md:438` and `fixtures.py:423` file `player_agency_v30` §6.3 as "CANONICAL but pre-#337 and REFERENCE under §0.05". Duty, Slate, Standing, Renown, mandatory scenes and Domain Echo are therefore intent only.

**What survives:**

(a) **The player is a callback over the engine's own candidates.** `play_surface.py:46–51` routes a person's turn to `overrides[p.id]`, which receives `auto` and the same `View`. The plan gives creation as "no act; a cast entry the world-gen builder seats" (`_part4:41`). IN-46 and IN-47 have "no build batch" (`_part4:22, :33, :40`). The playable duel decision set {engage, withdraw} is marked `[ASSUMPTION]` in the grid proposal [RELAYED]. `Person.conviction` is `{}` for every shipped person [RELAYED].

(b) **§C.11 against AX-7.** `04_CODE_ARCHITECTURE.md:849–855`: "The engine owes the ARITHMETIC of what the character already holds, and nothing else", and "a split on who is looking breaches the axiom" (`:847`). `01_AXIOMS.md:299–304` quotes Jordan verbatim ("the player gets to retain their own beyond-game understanding…"), then adds, outside the quotation, "**No state is hidden from the player.**" The collision is between §C.11 and that gloss, not Jordan's words, which §C.11 can satisfy. `04` never mentions AX-7 (grep count 0), and no ledger row cites §C.11 beside AX-7.

(c) **A dead canonical citation.** `requirements.yaml:34–35` calls `systems/_architecture/reference/scale_transitions_v30.md` "Status: CANONICAL" and treats its tables as a requirement. That path no longer exists: the file is at `.designs/systems/_architecture/reference/` (ED-IN-0231).

**Scale-transition coverage.** The contest at RESOLVE/ENCOUNTER is the one carried seam. `scale_transitions_v30.md` heads §3 "Eight Handoff Rules" but lists nine sub-sections (§3.1–§3.9); other documents give twelve [RELAYED]. Thread→Mass has an empty hook (`orchestration.py:333–335`, "threadwork lands in a future cycle"). Mass→Personal (the general duel) has no yield point: the battle is one 18-tick call (`massbattle.py:281–283`), and M-6 is LEAVE. Domain Echo has no lawful carrier: as designed it is a threshold producing an outcome [RELAYED]. 03 §C.4 says one slice renders at any depth, yet nothing selects fidelity; the switch is a party test at the seam (A-25) [RELAYED].

**Overturned by:** a build batch for IN-46/IN-47, plus one edit reconciling AX-7's gloss with §C.11. **Confidence:** high for (a) and (c); medium for (b), because whether the gloss is the ruling is itself the question.

### A7 · Mass battle, as designed, cannot resolve a season force

**Evidence.** Season forces are named persons at weight 1. The code says of single- and double-digit forces that they "rout on contact regardless of who wins" (`massbattle.py:198–207`), against `SUBUNIT_ROUT_FLOOR = 80` (`config.py:117`). No ratified weight→troop conversion exists (`massbattle.py:198–199`). `test_march.py:224–235` hand-builds a `Resolution` because `Won` "may be UNREACHABLE": the reversed 6-against-2 scenario "still resolved `Lost`". Cohorts are the only persons with weight above 1, and they carry no `commit` (`populated.py:391–395`). Mustering reads a live `commit` to the faction (`world_q.py:1124–1135`, `sides.py:85`), so cohorts cannot be mustered. Whether a cohort could ever `commit` in play: not checked. The battle is one atomic call inside ENCOUNTER, so a general's duel has nowhere to yield.

**Not findings:** the winning side takes no writes (`verb_table.yaml:682`, ED-IN-0279, Jordan's ruling). Levy→field (IN-52) ships off by design (`_part4:122–140`) [RELAYED].

**Why it survives the plan.** No position supplies the conversion. M-6 is LEAVE, and IN-52 ships off. **Overturned by:** one ruled conversion owned in one place. **Confidence:** high, on the code's own disclosure.

### A4 · NPC choice: what survives

**The score** is `damp · Σ_axis axis_w[ax]·align(c.verb, ax) + stance_term(p, c, fx, memo) + u` (`choose.py:403–406`). The first term reads only `c.verb`. `stance_term` reads the subject. At the shipped `stance_polarity = "legacy"` and `stance_gain = 1.0` (`fixtures.py:759, 773`) it is constant over candidates on the plain referent, but not over classed referents (`world_q.py:1662–1668`). The order is a Plackett–Luce sample through Gumbel noise at `choice_temperature = 0.1` (`choose.py:305–345`, `fixtures.py:251`).

**Question choice.** `question_aggregation_rule = "first"` (`fixtures.py:417`) takes one question. Sources are ordered `claim_landed`, then `need`, with ties broken by `q.id`, which for `claim_landed` "carries a CONTENT HASH" (`rosters.yaml:575–583`, `world_q.py:1790–1791`). IN-57 (B-W) tiers this order by the person's own state (`_part5:238–240`), so after the plan the hash is only the tie-break within a tier.

**R-08 is defined, and the repository splits it in its own words** (`requirements.yaml:1129–1152`). "Declines the optimum": BUILT, by sampling. "Inclination breaks a tie": NOT BUILT, blocked on a sparse alignment table.

**Surviving, evidenced:**
- (i) `urgency` is added identically to every candidate. Its own docstring calls it "INERT BY CONSTRUCTION" (`choose.py:172–193`).
- (ii) `benefits_me` has no production caller; grep finds only tests (`tests/test_governance_build.py:913–1002`). Its docstring says ED-IN-0261 names the `selfish_selfless` axis score as its weight and "no position builds that term" (`choose.py:162–165`). In the chooser that axis contributes nothing, because every verb's cell is null "by design", deferring to `verb_table.yaml`'s `beneficiary:` column (`rosters.yaml:2644–2690`). Yet 12 of 15 pursuits project onto it: virtue −.2, honour +.2, liberty −.1, justice +.2, wealth −.6, reputation −.6, individuality −.4, community +.4, happiness −.4, family +.5, love +.7, stewardship +.5; scholastics, stability and doctrine are 0 (`rosters.yaml:2305–2417`). Its one live consumer is world generation: loyalty is the cosine of the full axis vector against the role template (`cast.py:318–331`), which becomes a stance row (`cast.py:347–366`). It is a ruled mechanism that the plan does not carry, so it is not a free cut.
- (iii) An authored OUGHT's predicate is read by nothing, and "nothing planned needs it" (H-185, `hole_register.yaml:4162–4172`).
- (iv) Every character-change mechanism ships unarmed: `scar_weight_shift = 0`, `confliction_weight = 0`, `refusal_axis = None`, `intent_disclosure = 0.0`, `age_step = 0.0`, `illness_rate = 0.0`, `body_step = 0` (`fixtures.py:643, 651, 661, 736, 542, 543, 530`).
- (v) No live or planned term in the candidate score reads odds, cost or capability, and no ruling says NPCs deliberately ignore outcomes (Fable's grep of the decision-layer directories [RELAYED]). Whether this harms the coherence of NPC motives is UNMEASURED. The §0 ladder's step-5 answer is not to add an outcome evaluator, because that would be a fix that adds a system. **I state it as an unmeasured risk to R-WORLD, not a Jordan item.**

**Candidate-formation datum** (one seed; a scratch run whose instrument is not committed; `proposals/2026-10-13-narration-mechanisms.md:38–52`):
- 439 of 1,318 acts (33.3%) chose a subject of the wrong kind;
- about 48 acts had an effect beyond an existence flag;
- 52 of 52 act-minted Propositions have an empty predicate;
- 70.5% of acts were refused, blocked or null.

**Confidence:** high for (i)–(iv); low for anything resting on the datum.

### A9 · AX-7's falsifier, walked by its letter, fires

`01_AXIOMS.md:314–317` defines the falsifier as "any deposit into a person's ledger whose value is the engine's own resolution, unmediated by channel, competence or prior belief". It names three sites: `witness.py:191`, `:271` and `:361`. Those line numbers are stale. Today the sites are `loop/witness.py:521` (`Claim(cid, pid, subj, e.kind, True, …)`), `:637`, `:660`, `:689` and `:839`.

All five pass through `_refract`, which changes **only the confidence**: "id, value, source and chain are `c`'s" (`witness.py:227–235`). The rule is `refraction_gain = 0.5` (`fixtures.py:800`, ruled 2026-10-09). Refraction is skipped entirely when the witness is the act's own actor (`witness.py:486`: `refracting = bool(gain) and actor_of(w, e) != pid`).

**By the letter, then:**
- every deposit's VALUE is still the engine's resolution;
- the actor's own deposit is unmediated in value and in confidence. AX-7's row (2) requires that the performer's own understanding be fallible "by its OWN mechanism" (`01:280`), and none is built.

Whether confidence mediation is what the axiom means by "mediated" is not settled by its text. The partial-observation requirement (identity, act and motive as separate claims) is the unbuilt half [RELAYED]. **Why it survives the plan:** no position I read builds the self-reading mechanism [CONFIDENCE: medium — not every plan row was searched for it]. **Overturned by:** running the falsifier and finding a self-reading mechanism, or a ruling that a confidence-only refraction satisfies AX-7. **Confidence:** medium.

### A5 · The act economy: two items survive

**Withdrawn under planned=built.** The claim that a hold minted by `utter`/`create_record` buys budget is closed by IN-14 (ruled 2026-10-12 [ASSUMPTION; medium; Jordan to correct]): `budget()` counts only holds with non-empty `granted_acts`, and rounds = `max(budget)` (`_part4:26`). The claim "the sixth scene is unspendable" fails too. The ceiling counts released scenes (5 rounds × 1, `deliberate.py:89–92`) while the budget is a cost budget, so at the shipped `greedy` packing (`fixtures.py:424–426`) a budget of 6 is spent as three extended scenes at cost 2 each, three releases. The tree's own comment (`deliberate.py:89–97`) is accurate only under the `one_per_scene` arm. Narrowing the budget breaks the NPC telling transport (H-92; `_part4:27`), which is the plan's declared cost.

**Survives (a): a contradiction with Layer 1 (C4).** `_drop_what_was_already_done` (`deliberate.py:305–380`) removes acts already REALISED this season, keyed `(verb, subject[, counterparty])` (`data/verbs.py:1054–1057`). `03_VERBS_AND_LOOPS.md:138–140` says verbatim: "No cap, no dedup, no per-venue limit, no *already-before-this-body* rule — each of those would be the engine deciding a person's options". The filter's docstring calls itself "NOT A NEW RULE" and rests its case on `player_agency_v30` §6.3 (`deliberate.py:322–323`), a reference document under §0.05.

**Survives (b): the form only.** An extended scene costs `extended_scene_cost = 2` (`fixtures.py:425`), so a budget of 5 buys 3 + 3 + 1 = 7 acts. That is the form; the value is a swept fixture and Jordan's.

**R-CHOICE, upper bound.**

| SEAT: lord with `remit:issue` · INTENT: fill the treasury | gain | cost |
|---|---|---|
| `levy` | the seat's treasury rises at once by the levied amount (`verb_table.yaml:651–652`) | one scene; refusal emits `levy.refused` or `levy.unauthorized`; any grievance depends on who witnesses (*decaying cost*) |
| `restore` / `work` on a producing Site | `Site.condition` rises, and MATTER credits yield to the rung's stores in later seasons (`matter.py:515–536` [RELAYED]) | one scene; no one is taxed; the gain arrives slowly |

A second route to the intent exists, so this is a dominance question and not a corridor. The shapes differ: `levy` is immediate and unpriced (the Order and popular-support price in the old design has no carrier, and IN-23's stability Query is read by persons' estimates, not charged to the act); `restore` is slow and costs no one. Which dominates depends on the horizon and on how often `levy` is refused. **That is a shape mismatch, upper bound only; no run was made.** [CORRECTION: the producer wrote "a corridor… no second act reaches this intent". It had not looked at the yield route; the settlements digest names it.]

**S-UP.** A computed petition has `to == subject` (`deliberate.py:355–356`). A petition about a person is therefore addressed to that person, not to whoever holds the rung above them, and the receiver holds no Record until `give` places it (`effects_information.py:411–416`). **S-UP fails for the petition path.** The docket path is better: a date's lapse emits `date.fired` even when its holder is vacant (`calendar.py:41–57`), so burial on the docket is not silent. **Confidence:** high on the code facts; upper bound on dominance; no equilibrium run.

### A8 · Threadwork and Coherence against canon and Layer 1

- **Code defect.** `operations.py:246`: `history_contrib = min(3, history + 3)` is 3 for every history ≥ 0, and 2 or 1 only at history −1 or −2. History never improves a thread roll. The docstring (`:238–239`, "+3 constant per PP-624") shows the cap was meant to apply to the history term, not the sum.
- **Coherence head.** `coherence.py:9–14` marks `threadwork_v30` Part 3 SUPERSEDED. `CURRENT.md:27` still names `threadwork_v30.md` as head, but cites the WR-lane ruling that supersedes it (the row's last ledger id), in the same row. The row carries its own supersession.
- **After the crossing.** The module reports a crossing, and routing the load "has NO carrier" (`coherence.py:66–69`). K-3 (B-S) schedules a season carrier for Coherence (`_part7:42–48`).
- **Mending.** It costs 0 at every degree (`operations.py:449–451`, ED-871). No mending-fatigue brake exists in `systems/threadwork/sim/*.py` (grep "fatigue" returns nothing).
- **Canon.** The philosophical content is RULED (`canon/philosophy/README.md:3`). P-12 forbids propagation "as a single generic strain value" (`10_constraints.md:36`). The knot gauge's carrier is undecided (H-182), so P-12 is a CONSTRAINT on IN-32's choice, not a present defect. P-09 (detectable memory operations) and P-11 have no lawful carrier under the append-only log [RELAYED/UNVERIFIED].
- **Investigation yield.** Five of the six investigation verbs declare `writes: []`, and `survey` writes `Record.exists` (parsed). `reconstruct`'s row says what is missing is "the degree that would decide which to mint" (`verb_table.yaml:1178–1179`). The design is silent on what an investigation finds.

**Confidence:** high on `:246`; medium elsewhere.

### A6 · Governance and settlement management (narrowed)

**Closed by the plan.** `found`/`build` get a cost, a holder and a closer (IN-28, `_part5:109–114`). Legitimacy and stability become Queries over stance and claims (IN-23, `_part5:88–92`). **Domain actions are answered by the architecture**: "a seated person's verb `via` the seat — built by IN-10, IN-12's steps, IN-28, IN-45 and IN-49" [medium; Jordan to correct] (`_part2:160–167`). The `domain_actions` home document is CUT (`_part7:160`).

**Survives:**
- (i) `references/module_contracts.yaml` still declares `domain_actions` and `settlement_economy` with `doc: null`. The plan itself notes the stale row (`_part2:164–165`).
- (ii) The designed governance verbs (Keep Order with its consent, force and clergy methods; Hold Court; Develop; Fortify) appear in `references/action_vocabulary.yaml:63–72` and in no verb row. Hold Court has a near carrier in the proceedings verbs (`open_case`, `determine`). Keep Order's method choice has none [CONFIDENCE: medium].
- (iii) There is no birth or growth producer: "no position builds one" (`_part8:134`). The cast is closed by ruling (`cohorts.yaml:25–32`, which cites the WR-lane ruling). A cohort is one Person, so its death is final (`matter.py:461–463`). Hunger ships off (`fixtures.py:530`), so this is dormant.

**Confidence:** medium.

## 5. The N-line ledger, false N-lines and the E watchlist

**N-lines that hold** (each with the attack run and why it failed):

| object | N-line (narrowed where needed) | attack | direction |
|---|---|---|---|
| AX-1, only a person acts | Cut it and obstruction, deception and the bribable clerk vanish, because institutions resolve without a person who can be leaned on. | The cut walked: factions acting directly restore the four-weighted-faction campaign [RELAYED: `what_valoria_is_and_what_runs.md:159–161`]. `deliberate.py:280–284` enforces it. | top-down, lateral. **Narrowed**: bottom-up fails for the player, who has no designed reading of a faction (Query views exist for code, not for a client). |
| Refusal emits | Cut it and scarcity stops being witnessable, because a second claimant on an empty larder would raise instead of leaving an Event (`verb_table.yaml:654–659`, `levy`'s per-clause refusals). | Look for a row with no refusal emission: none in 45. | lateral, bottom-up |
| Frozen world during DELIBERATE | Cut it and deliberation order becomes an outcome, because a person deliberating second would read the first's writes. | `deliberate.py:72–74` raises; `driver.py:449–450` re-freezes each round. | horizontal |
| The scene budget | Cut it and a king's scarcity equals a copyist's, because nobody chooses what to leave undone (`03:131–134`). | Walked: no other object makes office cost attention. | vertical (office → triage) |
| ENCOUNTER step | Cut it and the grid's suspension and deferred contests lose their barrier (IN-46, `_part4:32–34`). | "Fold it into RESOLVE": RESOLVE thaws the world each round (`matter.py:113–116`), so a suspended scene would straddle a thaw. Kept, MEDIUM. | vertical |

**False N-lines** (cuts that are free):

- **`urgency`** (`choose.py:172–193`). The possibility it claims, that hunger reorders choice, survives the cut because nothing carries it now. The term is constant across candidates. Disqualifier 5 applies: the residue is a flat term, "+u" to all. Cutting it takes `test_season_shape.py:2754` with it.
- **Mass battle's survivor-ratio four-label degree** (`massbattle.py:289–296`). `field_degree` reads `attacker_wins` instead (`ladder.py:198–206`). Disqualifier 2 applies: no consumer.
- **NOT false: `benefits_me` / `selfish_selfless`.** ED-IN-0261 rules the weighting, and world generation consumes the axis (`cast.py:324–331`). The cut is not free; it is unscheduled (A4 ii).
- **NOT false: `challenge`.** PC-10, assumed built, gives it a carrier [RELAYED].

**E watchlist (over-distillation):**

| watched | the N it protects | verdict |
|---|---|---|
| A cohort as one Person at weight (`populated.py:391–398`) | one code path for crowds (S9.1, "a crowd must be able to act") | kept, MEDIUM. Costs: a cohort cannot dissent internally, cannot be mustered (no `commit`), and dies whole (`matter.py:461–463`). |
| A faction as a view, never an actor (`04` A-4; `_part2:158–161`) | AX-1 | kept, MEDIUM. Costs: player readability, and the stale `domain_actions` contract row. |
| The scar/conviction core shipped at control (`fixtures.py:643, 651, 736`) | the only character-change mechanism | kept, MEDIUM. Half-armed: built and shipped dark. |
| Three bands at the combat seam (`ladder.py:136–182`) | one write table keyed on a token | kept, LOW. The trace is returned and folded nowhere (`seam/wrappers/combat.py:245–252`); one magnitude crosses (`effects_combat.py:137–146`). |

## 6. The design's own falsifier, and the self-audit

**§8. Discipline under test:** "the person triages; the engine never truncates" (`choose.py:364`; `deliberate.py:199–200`), and every effect traces to a self-interested act. **Hits:**

| hit | class |
|---|---|
| `_drop_what_was_already_done` (`deliberate.py:305–380`) removes options, against `03:138–140` | **clean hit**: the engine deciding a person's options, in Layer 1's words |
| scene packing groups the next k by score, not by place (`choose.py:613–621`), against `03:116`'s "One place … a slice that spans places has no witness set" | **clean hit** |
| `bench_quorum = 1` stands in for an arrangement's own `quorum:` (`world_q.py:2144–2148`, `fixtures.py:849`) | clean hit, fixture family |
| `oblige_term = 4`, `record_stages_default = 3` (`fixtures.py:818, 460`) are terms an opener should declare | clean hit, fixture family [the readers in `matter.py` were not re-opened] |
| `remit_default` hands every seat every remit act (`rosters.yaml:313–365`) | **borderline**: a declared test placeholder by Jordan's ruling (`:314`). "22 of 29 seats hold `dispatch`" is a dated comment (`offices.yaml:106–113`), not a measurement made here. |
| `budget_office_bonus = 1` (`fixtures.py:462`) | **passes by tracing**: S26.3 rules that the budget varies by office; only the magnitude is a fixture |

The clean hits cluster into one family plus two singletons. The family is **fixture constants standing where an opener's or an arrangement's declaration should be.** The singletons are the dedup filter and place-blind packing. The discipline is real, and its exception list is missing this family. **Repair:** licence the fixtures narrowly as `[OPEN — Jordan tuning]` stand-ins, and make the term and the quorum a declaration on the opening act or arrangement. That is a schema field each, not a free one-liner.

**§9. Self-audit** `[SELF-AUTHORED — bias risk: this report rewrites an audit whose author's corrections it inherits]`.

**9a, backward propagation.** Each correction listed in §12 was carried back into the verdict, §2, the axis table and §9. In particular:
- domain actions dropped out of the recommendations;
- R-WORLD's forcing clause now reads "scheduled";
- X1 keeps `results.json`;
- G6 edits AX-7's gloss, not §C.11.

Three residues were found and fixed:
- the S-DOWN figure (4 of 1,270) lacked its one-seed caveat;
- the verdict said "three substrates" where the tree has two and a logistic side-channel;
- the A5 citation of the sixth-scene comment was restated as accurate only under `one_per_scene`.

**9b, §3 turned on my additions.** The new A9 sub-claim (the actor's own deposit is unrefracted) rests on `witness.py:486`, which I opened; it is not a store or a system. The pool-2/Ob-2 default odds are arithmetic on opened fixtures. The recommendation formerly "R10, a committed instrument" fired disqualifier 1 (the carrier exists): `harness/aperture` and `corpus_run` already measure acts. It is rewritten to use them. No other addition adds an object.

**An independent reviewer would add:** a play-length seeded run of the shipped loop; an equilibrium analysis of the act economy; squad-engagement Parts A–D; the bodies of `canon/philosophy` 02–08.

## 7. What is overbuilt

**Question:** what in the tree simulates itself rather than contributing to the game? **Test:** the repository's ID-13 reader clause at repository scale — name the consumer. A thing whose only consumer is another process artifact simulates itself. Continuity for a one-person-plus-agents workflow is legitimate where it constrains or informs a decision that changes the game. Rulings do; measurement history does not.

**Sizes** (tracked files, `git ls-files <dir> | xargs cat | wc -l`; mixed prose, YAML and JSON):

| class | lines | parts |
|---|---|---|
| **Runtime the loop executes** | **≈ 49,300** | `engine/season` loop 7,072 · state 4,462 · decision 2,281 · queries 3,344 · seam 1,313 · manifest 725 · data 5,779 · top-level `.py` 1,176 (= 26,152); `modules/` 15,841; `engine/dice_engine` 673; `engine/substrate` 499; data tables 6,123 (rosters 2,830, verb_table 1,247, offices 557, write_matrix 445, npcs 445, arrangements 234, venues 154, governance_spine 110, cohorts 101) |
| **Tests** | **≈ 116,100** | `tests/` 58,820 (231 files); `engine/season/tests` 37,649 (74); `engine/tests` 19,638 (5) |
| **Prose and records that execute nothing in the game** | **≈ 499,800** | `proposals/` 227,877 (507 files; of which `.md` 171,802, `.py` 11,254, `.json` 30,155); `.audit/` 79,085; `research/` 65,314; `.designs/` 60,804; `registers/` 42,765; `architecture/` 10,715; `canon/` 10,391; `workplans/` 2,861 |
| **Generated run output, tracked** | **87,678** | `engine/season/runs/`: `TRACE.txt` 72,433; `results.json` 11,215; eight `.md` logs 4,030 |
| **Instruments and tooling** | 40,087 | `engine/season/harness` 10,873; `tools/` 15,800 (54 files); `skills/` 13,414 (43 files; `.claude/skills/*` are symlinks into it) |
| **Season case corpus** | 8,908 | `engine/season/cases` (84 files) |
| **Game registers** | 5,773 | `hole_register.yaml` 4,493 (198 rows); `requirements.yaml` 1,280 |

**Ratios.** About 10.1 lines of non-executing prose and records per line of runtime, and 2.4 lines of test per line of runtime.

**Findings, ranked:**

1. **Tracked run output (87,678 lines).** `harness/report.py:143, 304–305` writes it. `harness/delta.py` reads `results.json` to produce the deltas "a commit message is allowed to claim" (`delta.py:24–27`), and warns that without regeneration the comparison "cannot fail" (`:8–12`). Two tests read the committed `results.json` (`tests/test_season_shape.py:2664–2666, :7366`). Nothing reads `TRACE.txt` or the `.md` logs except as citations in comments. The repository's own rule covers this: "GENERATED ARTIFACTS EVACUATE; THEIR GENERATORS STAY" (ED-IN-0125, quoted at `tools/evacuation_plan.py:21–22`). **What dies if cut:** a baseline the game never reads; two tests that check a committed file rather than a run. Confidence: high.
2. **R-01/R-02's narrative.** The instrument is `proposals/2026-09-04-degree-sweep/` (55 files, 28,679 lines), a sweep of about 75 minutes on four cores (`requirements.yaml:317`). R-02 passes because 43.03% is *below* a 96% bar: "at or above 96% would have meant the flips were absorbed" (`:451–461`). That bar passes anything not on rails. The `none` arm itself diverges 22.87% "through channels this run does not isolate" (`:489`). The positive plants read "detected OVER THE BASELINE on ALL 4 plants: False" (`:406`). The measured blocks run from `:192` to `:412` and `:419` to `:548`, as dated narrative inside a file the loop treats as mechanism. **What dies:** narrative a commit message could hold. The statements are Jordan's verbatim and stay. Confidence: medium.
3. **The world's start state lives in the test harness.** `harness/populated.py` (1,423 lines) builds the only realm. The acceptance instruments read two worlds (the authored 143-case corpus and the populated realm), and the plan records that they disagree on `march`: 16 of 16 executed in one realm reading, 11 declared and 11 refused in another (`_part2:170`, which tags both [UNVERIFIED]). This is a structure and elegance defect, not apparatus. Confidence: high on location.
4. **Overlapping ledgers of what is undone or decided.** `hole_register.yaml` (198 rows), "read by the corpus grader, not the loop" (`CLAUDE.md` §3); the v9 state index; 1,435 ED rows across 20 JSONL files in `registers/` (80 files, 42,765 lines). The ED statuses are resolved 876, open 178, superseded 95, ratified 74, closed 63, struck 46, ruled 25, proposed 17, with 1,281 distinct ids. Add nine lane handoffs with history and closed files, plus `CURRENT.md` and `HANDOFF.md`. The split: rulings are load-bearing, because code docstrings cite them and decisions rest on them; measurement history is not. Confidence: medium.
5. **CI by consumer.** `references/ci_checks_registry.yaml` lists 34 rows (33 tools, since `ci_naming_check.py` appears twice). Its `subject:` field reads `compliance` on 32 of 34, so it does not discriminate. **My rule:** a check guards THE GAME if its input or output is code the game executes, data the loop or port reads at runtime, or the tests that execute it; it guards PROCESS if its subject is documents, ledgers, names in prose, size caps, provenance or currency. **My count: game 13, process 19, borderline 2.**
   - **Game (13):** golden modes; Lanchester signature; module shape; sim fabrication; the six export round-trips (engine params, game constants, descriptors, NPC roster, composition, names); vacuous-assertion; `arms.py`; `m1_acceptance`.
   - **Borderline (2):** names consistency (a registry feeding `names.json`); quantity vocabulary.
   - **Process (19):** register size; co-file; editorial markers; broken dependency; freshness gate; canon coverage; PP frozen; naming ×2; prose quarantine; generation consistency; claim provenance; vetting; compliance; currency consistency; identifier census; mechanics index; ED-citation validation; ledger fold.

   `CLAUDE.md` §0.1 pt 5 already forbids adding more. Confidence: medium (the classification is a judgement on `role:` lines).
6. **Depth beneath a collapsing seam.** `modules/mass_battle` is 10,154 lines, 59% of them in `hierarchy/units.py` (3,017) and `orchestration.py` (2,989). The season builds one infantry Line per side (`massbattle.py:170–178`). `Officer` is "bookkeeping only — nothing at resolution time reads it" (`units.py:2793–2795`). `equipment/` is "NOT YET WIRED into resolution" (`equipment/weapons.py:18`). `modules/combat` is 5,643 lines, reached through `end`. No scheduled consumer exists: M-6, U-4 and K-6 are LEAVE, and K-1/K-5 are unscheduled. In PLAYABLE mode the duel engine runs its own turn loop [RELAYED], so the depth is spent for a played fight once a Person→Combatant mapping exists, and wasted for every automated fight. Park; do not delete. Confidence: medium.
7. **`engine/engine_params/params_tables.yaml`** (10,821 lines, 68% of `engine/engine_params/`). It is "a frozen, no-longer-regenerable, ungated capture" (`CLAUDE.md` §5). Runtime files mention it only in comments (`dice_engine.py:169, :262`; `ladder.py:58`; `modules/mass_battle/resolution.py:226`). Tools list it (`ci_naming_check.py:124`, `currency_consistency_check.py:92–105`, `evacuation_plan.py:395–405`), and one `.audit/` script loads it. No game reader exists. Confidence: high.
8. **Fixture knobs.** `data/fixtures.py` has 66 knob assignments, 13 annotated "(control, SHIPPED)" and 27 lines pairing control with SHIPPED in some form. Each carries a hole row and test arms: a configuration space nobody ships. The values are Jordan's; this is E-OVERHEAD, not a defect.
9. **Declared fields with no scheduled reader** (ID-13 at game scale, excluding those the plan gives readers):
   - `urgency`;
   - the null `selfish_selfless` row (see A4);
   - the OUGHT predicate (H-185);
   - `scale:` on 10 verb rows, which retires when `Act.via` carries scope (`verb_table.yaml:66–75`);
   - of the 14 declared arrangement keys (`data/arrangements.py:78–82`), only `disposes` is read by production code (`effects_information.py:260, :355`; `state/gate.py:254`). SC-01 may give the rest readers.

   Five rows declaring writes with no effect, and 13 emission-only rows, are [RELAYED].
10. **Quarantined prose still pointed at as heads.** In `CURRENT.md:20–36`, 14 head rows name `.designs/` documents, and one (Narrative engine) names an `.audit/` document, while `CURRENT.md:13` calls such a row "reference, not a head". `requirements.yaml:34–35` cites a dead path as CANONICAL. Every audit pays the cost: this one had to reconcile `player_agency_v30` against Layer 1.
11. **`tools/evacuation_plan.py`** (1,035 lines). It is not in the CI registry; its only automated consumer is `tests/valoria/test_evacuation_plan.py`. [UNVERIFIED whether an evacuation under ED-IN-0125 is still pending.]

**Not overbuilt, with the attack:**
- Layer 1's front door, `00_THE_METHOD.md` (175 lines [RELAYED]).
- The golden gates and the morale write-sweep. `CLAUDE.md` §0.1 pt 5 keeps them because their output crosses into the engine.
- Refusal-emits and the frozen world (§5).
- The export round-trips: the port's oracle.
- The dice engine (673 lines), whose only defect is the duplicated literals.
- ENCOUNTER.
- The ED rulings as such.

[GAP: `skills/valoria-compiler`, `-chunker`, `-vector-audit`, `-editorial-register` — whether they still serve a workflow; not examined, and `CLAUDE.md` §9 still routes to them.]

## 8. Throughlines

**Definition.** A throughline here is a pattern that recurs in findings from at least three independent subsystems or layers, has a shared cause, and says something about what the game is or how it is being built. The repository uses the word differently: there a throughline is "a causal spine connecting 3+ systems … mechanical chains that the engine must implement" (`.designs/systems/_architecture/reference/throughlines_complete.md:12`). Theirs are designed chains; mine are recurring defects with one cause. The repository's own `proposals/2026-08-25-throughlines-and-precedent/` has chapter files named "the world has no people" and "one resolver, four scales, one scalar". I read only the file names, but T1 and T3 below may restate patterns named there seven weeks ago and still standing [UNVERIFIED].

### T1 · Persons differ in what they want, not in what they can do

- **Instances:**
  - combat: `end` is the only derived input (`seam/wrappers/combat.py:130–138`; `combatant.py:93–94`);
  - contest: `pool_default` 2 and `obstacle_default` 2 for 429 of 430 persons (`sigma.py:97–129`; `requirements.yaml:77–79`);
  - mass battle: `power` 4 and `command` 4 for every side (`massbattle.py:183, 196`);
  - player: creation picks a person the cast already holds (`_part4:41`);
  - decision layer: cohorts carry no pursuits (`populated.py:391–398`), and every character-change mechanism ships at control (`fixtures.py:530–543, 643–661, 736`).
- **The counterexample I looked for:** a character quantity that moves a resolved outcome. **Found, and it narrows the claim.** `pursuits`, authored per person at genesis (`choose.py:157–159`), moves choice through the score's first term (`choose.py:404`). Stance moves it through `stance_term`. So persons do differ, but in their wants and ties. Their capacities are identical.
- **Shared cause:** there is no ruled source for per-person magnitudes (K-2 "not ratified", `_part7:44`; J-13's remainder, `_part5:449`; the closed cast, `cohorts.yaml:25–32`). That meets a discipline that refuses to invent: "not the place to invent one" (`massbattle.py:198–207`); "inventing convictions for a population would be authoring a creed nobody wrote" (`populated.py:394–395`). Under both, the default is the only lawful value.
- **Prediction:** a player meets people distinguished by office, body and relationships. Two people in the same seat fight, argue and march alike, and outcomes vary by seed.
- **Confidence:** high.

### T2 · The seam keeps the band and drops the fight

- **Instances:**
  - combat returns its trace, and "nothing here or downstream folds it into `World`" (`seam/wrappers/combat.py:245–252`);
  - mass battle computes survivor fractions and a four-label degree, and the season reads only `attacker_wins` (`ladder.py:198–206`); `Officer` and `equipment/` are unread (`units.py:2793–2795`; `equipment/weapons.py:18`);
  - threadwork's hook into mass battle is empty (`orchestration.py:333–335`);
  - the contest's σ-leverage enters at 0 (`sigma.py:147`).
- **Counterexample sought:** a magnitude that crosses. **Found one:** the wound fraction sets `Person.body` (`effects_combat.py:137–146`). A second exists and ships at 0 (`field_morale_loyalty_gain`, `fixtures.py:608`).
- **Shared cause:** effects are keyed on a degree token (`degree_of` → `writes_at`, `ladder.py:209–225`), and the subsystems were built for inputs the season Person does not supply. This is T1 seen from the output side.
- **Prediction:** tuning combat physics or mass-battle formations changes almost nothing in the world beyond who falls.
- **Confidence:** medium.

### T3 · One ladder, many roads to it and around it

- **Instances:**
  - four owners of the per-die literals (`dice_engine.py:174–175`; `sigma_leverage.py:77–79, :105, :112–113`);
  - two substrates and a logistic (`core.py:26–41, :60`; `roll.py`);
  - four pool formulas (A3);
  - three result vocabularies plus mass battle's fourth (`ladder.py:136–206`; `massbattle.py:289–296`);
  - two Coherence heads (`CURRENT.md:27`; `coherence.py:9–14`);
  - `scene_budget` with "two readers [that] read it as two different quantities" (`deliberate.py:85–88`).
- **Does the one-ladder rule fail only where subsystems were ported in?** No. `seam/ladder.py` and `deliberate.py` are Layer-2 code written under Layer 1.
- **Counterexample sought:** a quantity with one owner held by a guard. **Found:** `degree_from_net` is single-owned, and combat routes its grading through it (`core.py:65–74`, citing `test_degree_ladder_single_owner.py`). So the margin ladder is one; the multiplicity is in the roads to it and the vocabularies beside it.
- **Shared cause:** each lane closed its own seam locally. "One owner" holds only where a test enforces it.
- **Prediction:** the same score buys different odds shapes at different scales, and a tuning in one scale does not transfer.
- **Confidence:** high.

### T4 · Built ahead of its readers, and kept as the record of a measurement

- **Instances:**
  - `urgency`, "kept and computed anyway, faithfully, because deleting it would hide the finding" (`choose.py:188–190`);
  - `benefits_me` (no caller);
  - the OUGHT predicate (H-185);
  - 13 of 14 arrangement keys unread;
  - `scale:` on 10 rows;
  - 13 controls shipped dark;
  - `equipment/` and `Officer`;
  - `params_tables.yaml`;
  - `runs/`.
- **One cause or several?** Two proximate causes: declaring a field before its reader, and shipping a swept arm dark as the control. They share one root: in a tree without memory, a retained carrier is the record that a measurement happened.
- **Counterexample sought:** deletion of a dead carrier. **Found:** `DECISIVE_OB` (`core.py:47–49`), `effective_ob` (`core.py:57–59`), the TN 6/8 rows (`dice_engine.py:166–167`) and the `_attempted` set (`deliberate.py:341–344`) were all deleted. Narrowed: the tree deletes what a ruling or a zero-caller sweep kills, and keeps what a measurement has touched.
- **Prediction:** the vocabulary a future session must read grows faster than the behaviour.
- **Confidence:** medium.

### T5 · Acts record that something happened, not what

- **Instances** (one seed, a scratch run, `narration-mechanisms.md:38–52`):
  - Propositions: 52 of 52 have an empty predicate;
  - Records: 112 of 120 have no `subject_matter`;
  - about 48 of 1,318 acts do anything beyond an existence flag;
  - investigation: five of six verbs write nothing (parsed), and the value space of a finding is unruled (`verb_table.yaml:1178–1179`);
  - war: no world-gen code authors a war utterance (`faction_q.py:232–240`).
- **Counterexample sought:** content-bearing acts. **Found:** tellings carry a `Said` with a predicate, and 8 Records carry content (`narration-mechanisms.md:50, :53`).
- **Shared cause:** T1 and T4, again. `Proposition.predicate` is read by nothing (H-185), so nothing has reason to fill it.
- **Prediction:** a chronicle of an unwatched season would read as a list of existence events.
- **Confidence:** low. The plan's forcing handles (IN-35, IN-36), the paper sink (IN-26) and SC-01 may change this, and the evidence is one uncommitted seed.

### T6 · Apparatus grows where the game cannot read it, and moves when banned

- **Instances:**
  - about 10 lines of prose and records per runtime line;
  - 87,678 tracked lines of run output;
  - R-01/R-02's narrative;
  - 19 process checks in CI;
  - four overlapping ledgers of what is undone;
  - game-code comments carrying dated correction narrative ("⚠⚠ IT IS LIVE, AND THIS COMMENT SAID LATENT UNTIL 2026-09-20", `deliberate.py:97`; `:85–112`; `:305–366`).
- **Counterexample sought:** apparatus being removed. **Found:** the `.designs/` quarantine (ED-IN-0231), the retired `balance_oracle`, the deprecated `mc_v18`, and `CLAUDE.md` §0's ban on audit directories. Growth is displaced, not unchecked.
- **Shared cause:** sessions have no memory, so each correction must be written where the next reader will meet it. That is a property of the workflow, not of carelessness.
- **Prediction:** with `.md` banned under `systems/` and audit directories banned, the next apparatus will appear inside docstrings and comments of game code, and in `requirements.yaml`'s `measured:` blocks. Both are already visible.
- **Confidence:** medium.

**Considered, dropped:**
- *The plan closes engine truth before the player-facing bottom.* The dependencies are mostly genuine (IN-46 needs IN-04; rendering needs content). The two items not downstream of anything are T1's cause and A2, not a separate pattern.
- *The architecture's refusals are all damping terms.* No measurement exists beyond four seasons, so there was nothing to attack it with.
- *Silence is free where acts are priced.* The docket lapse emits (`calendar.py:41–57`) and refusals emit. The one verified silent omission, the dedup filter, is one instance, not three.

### How the throughlines connect

Two causes sit upstream. The first is the workflow's lack of memory (T6), which produces T4: carriers kept as records. The second is that no source has been ruled for per-person magnitudes, combined with the refusal to invent one (T1's cause). That starves the seams. With nothing distinctive going in, a seam has only a band to carry out (T2), and an act has little content to record (T5). T3 has a separate origin, lanes closing seams locally, but T2 shelters it: each subsystem's private vocabulary survives because the band discards everything else. So the order of repair is: first rule the per-person source, the one decision that changes the game; then unify the roads to the ladder, cheaply, before more depth is wired through T2's seams; then make the deletions T4 and T6 license, which shorten what every later step must read.

## 9. Recommendations, sequenced by the throughlines' causal order

Each is a deletion or at most one object. "Ladder" is `CLAUDE.md` §0's five steps: superseded / irrelevant / design document / precedent / architecture.

| # | finding → change | owner / gate (ladder result) | falsifier | cost |
|---|---|---|---|---|
| **G1** | **A1/T1.** Rule a source for per-person capacities: `Person.attributes` (K-2) with its first reader `party_end`, or rule that identical fighters are intended and drop the claim of person-varying personal-scale resolution. | **Jordan.** Survives all five steps. (1) Nothing supersedes it. (2) Combat is a retained scale (`requirements.yaml:143`). (3) K-2 is "not ratified" (`_part7:44`). (4) J-13 (iii) covers the contest only. (5) Both options are lawful under AX-1..7 and give materially different games. | Two persons with different authored attributes yield different Felled rates over the same seeds; identical attributes reproduce today's `content_hash`. | One field and one reader; golden re-pins. |
| **G2a** | **A3/T3.** One owner for the per-die literals: `sigma_leverage.py` imports `dice_engine`'s. | Agent, IN lane. Step 4, precedent: `CLAUDE.md` §8 and `degree_from_net`'s single owner. | A grep finds the 0.4/0.8 pair defined once; the export `--check` round-trips stay green. | About four lines. |
| **G2b** | **A3.** Delete mass battle's survivor-ratio four-label degree (a false N-line). | Agent, MB lane. Step 2: nothing reads it (`ladder.py:198–203`). | The `result['degree']` key is gone and march's bands are unchanged. | About ten lines. |
| **G2c** | **A3.** Mass battle returns a margin to the owner ladder (`03:286–289`). | **Jordan.** Step 3 would answer it, but the change rewrites march's ruled Won/Lost writes (ED-IN-0279, `verb_table.yaml:682`), and that overwrites ratified canon. The agent may draft. | — | Re-pins; one formula, Jordan's. |
| **G2d** | **A3.** One substrate: combat's main roll moves to the discrete die, or the season states its ceiling-Ob rule as the deliberate lattice reading. | Agent, PC lane [medium]. Step 4: the die rule and "TN7 always" are ruled and discrete (`dice_engine.py:151–161, :164–165`). | The combat-balance workbench is re-measured before and after; the goldens are re-pinned and declared. | Combat balance moves. |
| **G3** | **A7/T2.** One ruled weight→troop conversion, owned at `massbattle._weighted_unit`. | Form: agent, MB lane. Value: `[OPEN — Jordan tuning]`. | `test_march.py:224–235`'s hand-built `Resolution` is replaced by a real fold reaching `Won`. | One constant; re-pins. |
| **G4** | **A5a/§8.** Delete `_drop_what_was_already_done`. | Agent, IN lane. Step 3: Layer 1 forbids it verbatim (`03:138–140`), and its only stated basis is reference prose (§0.05). If R-03 goes red, the filter is load-bearing on a Jordan requirement, and amending 03 §C.3 becomes the Jordan item. | R-03's `measure:` and `test_u2_`. | One function and one call. |
| **G5** | **A4/T4.** Delete `urgency` and its test; delete `benefits_me`. | Agent, IN lane. Step 3: `urgency`'s own docstring calls it a §F2 defect; `benefits_me` has no caller. **Whether ED-IN-0261's self/other weighting is ever built is Jordan's**: it survives step 5, because NPCs that weigh self-interest and NPCs that do not are different games. | `content_hash` equal at seed 0 before and after (inert by construction). | About 50 lines out. |
| **G6** | **A9/A2b.** (i) Walk AX-7's falsifier over the five current sites, and re-point `01_AXIOMS.md:307, :315–316` to them. (ii) Narrow the gloss "No state is hidden from the player" (`01:301–302`) to Jordan's verbatim, which §C.11 satisfies. | Agent drafts; Layer-1 text lands by PR review (merge ratifies, ED-1094). Step 3: the verbatim is narrower than the gloss. Step 5: §C.11 is the mechanized contract (`explain` has no `World` parameter, `04:860`). Not escalated: AX-7 (2) says self-understanding *may* be wrong, so a self-reading mechanism is permitted, not owed. | The reconciled texts admit `explain(p, v)` with no exception clause. | Two sentences. |
| **G7** | **A8.** `operations.py:246` → `min(3, history) + 3`, per its own docstring; re-point `CURRENT.md:27`'s head to `systems/threadwork/sim/coherence.py`. | Agent, WR lane. Step 3: PP-624 as quoted in the docstring. [ASSUMPTION: "capped +3D from level" (`operations.py:245`) caps the history term, not the sum. PP provenance is unvalidated, so verify PP-624 by hand first.] | The pool at history 0 differs from the pool at history 3, in one test. | One line and one test. |
| **G8** | **A2c/§7.10.** Re-point the 15 quarantined head rows in `CURRENT.md` to their code owner where one exists, or "no live head"; then delete `CURRENT.md:13`'s caveat. Fix `requirements.yaml:34–35`'s dead path. | Agent. Layer 0 pointer index, not RULED. | `freshness_gate.py` and `currency_consistency_check.py` pass. | About 17 lines. |
| **G9** | **A4 datum/T5.** Re-read candidate formation with the existing `harness/aperture` over several seeds before building on the 33% figure. | Agent. No new instrument (§9b). | The figure reproduces or does not. | Run time. |
| **X1** | **§7.1/T6.** Untrack `runs/TRACE.txt` and the eight `.md` logs (76,463 lines). Keep `results.json` until its two tests regenerate it. | Agent, IN lane. Step 4, precedent: ED-IN-0125, "generated artifacts evacuate". IN-55's plan entry re-records a TRACE-derived artifact, so it must name a regenerated file instead. | `report && delta` on a clean checkout gives the same deltas; the two tests stay green. | `.gitignore` plus one plan line. |
| **X2** | **§7.2.** Move R-01/R-02's dated narrative to commit history. Keep each row's statement (Jordan's verbatim), `status:`, a one-paragraph `measured:` and `measure:`. | Agent. Statements untouched. | `register --requirements` still accepts both rows. | About 300 lines out. |
| **X3** | **§7.7.** Delete `params_tables.yaml` with a `FORK:` row. Re-point the four runtime comments to the fork ref and edit `CLAUDE.md` §5's mention (not RULED). | Agent. Step 2: no game reader. | A grep finds no runtime load; the tools that list it are updated. | 10,821 lines out. |
| **X4** | **§7.6/T2.** Park: no new depth below the season seam in `modules/mass_battle` or `modules/combat` until K-1 or M-6 is scheduled. No deletion. | MB/PC lanes; A-25's module rule. | — | Zero. |
| **X5** | **§7.3.** Move `populated.build_realm` from `harness/` into the game code. | Agent, IN lane (Layer-2 organisation). | `content_hash` equal at seed 0; importers updated. | One move. |
| **X6** | **§7.4.** Move the 1,017 resolved, superseded and struck ED rows into the lane `_archive.jsonl` files the validator already reads. | Agent. Step 4: the archive files exist. | `validate_ed_citations.py` passes. | Churn only. |
| **X7** | **§7.5.** Add no process checks. Apply `CLAUDE.md` §0.1 pt 5's predicate to the 19 process checks, and retire those it condemns. | Agent proposes; a PR Jordan reviews, since blocking gates on the protected branch change. | The CI workflow's blocking set shrinks with no game-path check removed. | Per check. |
| **X8** | **§7.11.** Delete `tools/evacuation_plan.py` and its test with a `FORK:` row, if no ED-IN-0125 evacuation is pending. | Agent [UNVERIFIED precondition]. | — | 1,035 lines out. |

**Order:** G1 → G2 → G3 (T1, T3, T2), then G4–G7 (instances), then X1–X8 (T4, T6). G8 and G9 can run at any point.

## 10. Limits, UNVERIFIED and SKIPPED

- [UNVERIFIED] Whether AX-7's falsifier, as executed, passes. It was walked by reading, not run.
- [UNVERIFIED] Whether a cohort could ever `commit` in play.
- [UNVERIFIED] The contest kernel's `Pool.BASE = 3`.
- [UNVERIFIED] The two disagreeing `march` readings (`_part2:170`).
- [UNVERIFIED] Whether an ED-IN-0125 evacuation is pending (X8).
- [UNVERIFIED] Whether `proposals/2026-08-25-throughlines-and-precedent/` already names T1 and T3.
- [RELAYED] `Person.conviction` is `{}` for every shipped person.
- [RELAYED] The duel decision set {engage, withdraw} is marked `[ASSUMPTION]`.
- [RELAYED] The handoff count of twelve in a third document.
- [RELAYED] Domain Echo is a threshold.
- [RELAYED] The fidelity switch is a party test (A-25).
- [RELAYED] Five rows declare writes with no effect; 13 rows are emission-only.
- [RELAYED] PC-10 gives `challenge` a carrier.
- [RELAYED] IN-52 ships off (`_part4:122–140`).
- [RELAYED] The PLAYABLE duel runs its own turn loop.
- [RELAYED] `00_THE_METHOD.md` is 175 lines.
- [RELAYED] AX-1's cut cost (`what_valoria_is_and_what_runs.md:159–161`).
- [RELAYED] No decision-layer ruling says NPCs ignore outcomes (Fable's grep).
- [RELAYED/UNVERIFIED] P-09/P-11 have no carrier under the append-only log.
- [CONFIDENCE: low] Every figure from `narration-mechanisms.md` §1.1: one seed, a scratch instrument, uncommitted.
- [SKIPPED: UI Parts 4–10 — player-facing rendering — out of reach in this pass]
- [SKIPPED: squad-engagement Parts A–D — combat depth — header only]
- [SKIPPED: `canon/philosophy` 01–09 bodies — canon detail — rows of `10_constraints.md` only]
- [SKIPPED: `.audit/` — by rule]
- [SKIPPED: `loop/matter.py:152–236` — readers of `oblige_term`/`record_stages_default` — not re-opened]
- [GAP: equilibrium of the act economy — no instrument run; every R-CHOICE verdict is an upper bound]
- [GAP: play-length behaviour — nothing runs beyond four seasons in any reading cited]

## 11. GRADE

**paper.** No execution artifact was produced by this pass. The object graded is the design with every v9 position assumed built, which cannot be run by construction. The shipped loop has a recorded run (`register --requirements`, 2026-10-10, exit 0, `workplans/valoria_master_workplan_v9.md:183`). That run was not repeated here, and it is evidence about the shipped tree, not the planned one.

## 12. Appendix: changes from the first draft

**Withdrawn:**
- "No designed ending" and "the sole-victory rule is a forbidden threshold": IN-27 schedules a Query-based ending (`_part5:102–107`).
- The cost of witness and log scans: IN-54..56 target them, and the cited timing was confounded.
- "Stored MS/Stability/Accord" as a false N-line: already cut.
- `found`/`build` as free with no closer: closed by IN-28.
- Governance with no Query replacement: closed by IN-23.
- "Pyrrhic victory impossible": Jordan's ruling.
- "A hold minted by records buys budget": closed by IN-14.
- "The sixth scene is unspendable": refuted by greedy packing.
- "Nothing records which player design wins": recorded at `CURRENT.md:13`.
- "Domain actions have no plan position": answered at `_part2:160–167`, cut at `_part7:160`.

**Corrected:**
- "Layer 1 survives every attack" became the attacks actually run (§1), with A9 added.
- The `selfish_selfless` projection count is 12 of 15, not 7, and the axis is consumed at world generation, not "multiplied by zero" everywhere.
- "The main roll uses Φ" became: combat draws from the Normal; the season and contest are discrete.
- `requires_typed`: 34 of 45 rows carry the key, but 6 of those are `none` (evade/defy, exchange, oblige, construe, release, thread_read), so the first draft's 28 typed and 17 untyped was right. The intermediate "34 vs 11" misread key presence as typing. [CORRECTION applied by the orchestrator after the producer's receipt.]
- `scale:` is on 10 rows, not 9.
- Five investigation verbs write nothing, not six.
- `CURRENT.md` has 15 quarantined heads, not ten.
- `runs/results.json` has two test readers.
- The ED ledger is 20 JSONL files, not 80.
- `verb_capability` is at `rosters.yaml:1104–1106`; the plan's own cite of `:1062–1064` is stale.
- `units.py` is at `modules/mass_battle/hierarchy/units.py`.
- AX-7's falsifier line references are stale.
- The forcing handles are scheduled, and the Calamity's class is answered [medium].
- R2's target moved from §C.11 to AX-7's gloss.
