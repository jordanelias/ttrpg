# SPEC_GAPS — places the amended SC proceeding spec could not be implemented without a choice

Spec read at tree `/home/user/ttrpg`, branch `ccr-ef587cd0-nbwjff`, HEAD `e0c862296`.
Abbreviations: **RD** = `proposals/2026-11-12-subsystem-audit-suite/proposals/2026-11-14-social-contest-redesign.md`;
**RD2** = `..._part2.md`; **RD5** = `..._part5.md`; **PL** = `workplans/valoria_master_workplan_v12_part22_b24p.md`;
**PLc** = `..._b24p_cont.md`; **P8** = `workplans/valoria_master_workplan_v12_part8*.md`.
Each entry: id · spec location · quote · the choice the model makes (`scmodel` file/function) · severity
(H = changes outcomes materially / the spec contradicts itself; M = a guess a reasonable builder could make
differently; L = cosmetic / naming).

## Records and order (RD A.3, A.5)

- **G01 (L)** RD:194 `order: str  # alternating | rank | scripted | single` vs RD:313-319 (the A.5 order table:
  `free`, `written_only`, `alternating`, `rank`, `scripted`) and RD:387 (`abridged` sets `order: free`). `single` appears
  in no table. *Choice:* the model accepts the five table values; `single` is treated as `free` (`_mover`).
- **G02 (M)** RD:67 an exchange is "four draws taken in a fixed order (the reading, the hold, the speech, the other side's
  steadiness)" vs RD:290-292 "the reading's (one for its roll, one per ground, one for the other side's state) ... `G + 5`".
  Four draws vs G+5 normals: the reading consumes G+2 normals itself. *Choice:* G+5 (the explicit count); slot layout
  `[reading_roll, ground_1..ground_G, other_state, hold, speech, steadiness]`.
- **G03 (M)** RD:302 "`argue` moves the track by the margin" and RD:78 "track ... positive toward `for`". The margin is
  the speaker's own (positive = he landed). Nothing says an `against` speaker's margin is negated before it enters the
  track. *Choice:* `track += sign(side) * clip(margin)` (sign +1 for, -1 against); B.9 `sigma_x` uses the same sign.
- **G04 (H)** RD:346-350 (A.5) `sigma_d = levels_to_sigma(track*track_step + ... - resist(d))` and RD:1000-1001 (B.9)
  `... - end_levels(yield, break) - resist(d) +/- presumption`. Three defects: (a) `resist(d)` is defined at RD:863 as a
  PAIR `(max(-r,0), max(r,0))`; subtracting a pair from a signed scalar is undefined. Its net (for minus against) is `-r`,
  so `- resist(d)` read literally ADDS `+r` toward `for` for a high-Will decider, i.e. a stubborn voter is carried toward
  the proposition. *Choice:* `- r` (the scalar r = resist_step*(d.will - mid)): high Will pushes toward `against`, the side
  that need not overcome anything. A builder taking the pair's net gets the opposite sign. (b) `+/- presumption` gives no
  sign rule in the RD; PLAN B24p.12 settles it (`+level` when `presumes: for`, `-level` when `against`); inert at
  shipped anyway (G17). (c) A.5 writes `- end_levels(for) + end_levels(against)` and B.9 writes
  `- end_levels(yield, break)` (unsigned, sides dropped). *Choice:* A.5's signed form.
- **G05 (M)** RD:346 A.5 calls `levels_to_sigma(...)`; RD:425 names `levels_to_net_sigma`; B.9 RD:1000 writes the sum
  with no wrapper. The arguments are already sigma (track*track_step is "sigma per unit of track", level(modifier) is
  sigma). *Choice:* identity (the sum is sigma); `net_boost` applies the soft cap.
- **G06 (L)** RD:776 Grace "reads ... `SideState.marks`, `.standing`" — SideState (RD:226-234) has no `standing` field.
  *Choice:* read as `esteem`.
- **G07 (M)** RD:353-356 "`relevance(d)` counts `strike_level` once per strike from the k-th (B.1)" and RD:1007 "The strike
  levels leave `end_levels` and are carried by `relevance` alone" vs RD:472-476 B.1 "a side with k or more strikes takes
  `strike_level` against it at the close" (unweighted). B.9 supersedes by weighting with f_d. *Choice:* B.9 (`relevance`
  only, weighted by f_d); end_levels carries yield and break only.
- **G08 (M)** RD:994 `lost` = "the track increment of the diverted side's next exchange after that divert". The "track
  increment" of an exchange whose move is not `argue` (press, divert, rest) is 0; and "the diverted side" is the side the
  divert landed ON (T of the divert), whose next exchange is its own. If the sitting ends before that side speaks again,
  lost = 0. *Choice:* as stated; increment = signed clipped margin actually added (after the clamp: the change in track).
- **G09 (M)** RD:987-990 `q_x = net(x.levels["proofs"]) / (2*pw)` uses the room's pw, but at control/shipped
  `proofs` = level*usable*2*pw only for the MOVER's own speech; and `m_x` divides delivery by `2*(1-pw)`. Under
  `written_only` delivery is 0 (fine). `r_x = delivery_step * (k_x/10) * (S_x.reason - mid)` mixes delivery's step into a
  Reason term; at `delivery_step` 0 (control) r_x vanishes even when sense_step is shipped. Implemented as written.
- **G10 (H)** RD:997-998 the detection: `sincerity = level(ploy_level) * (ployed(against) - ployed(for))` — toward `for`
  when `against` ployed: consistent. But RD:1045-1046 "`deceive` is in no seeded rite" while C.4/RD:1031 make `deceive` a
  move with `resisted_by: attunement`. So in an automatic realm `sincerity` is structurally 0 (the RD says so). Implemented;
  only planted runs exercise it.

## Symbols the tree lacks (derived from the plan)

- **G11 (L)** P7:499-503 B04.24 `pool_of(...) -> int`; B05.25 item 5 retypes it `-> float`; RD:426 "A pool is fractional and
  is never rounded (R8)". *Choice:* float `max(pool_floor, score + addends + pool_add)` (`dice.pool_of`).
- **G12 (H)** RD:909-922 B.7 "The exchange builds one `SocialContestInput` and calls `roll.py::roll`" and RD:290-292 a
  FIXED normal count per exchange. The LIVE `modules/social_contest/roll.py::roll` (`:205`) is `roll_net(inp.pool, rng)`:
  the DISCRETE d10, one `rng.randint` per whole die (`round(pool)` of them), and its `obstacle_terms` (`:161-194`) is
  `difficulty + score/2 - room + forgery`, capped, with NO even line and no `obstacle_operands`. So until B05.02 (continuous
  roll) and B05.14 (composer with `even`, `opposed_ob`, operands) land, the speech cannot call the live roll AND keep
  the fixed draw count, and RD B.7's control equality cannot hold. *Choice:* `dice.roll`/`dice.obstacle` implement
  B05.02 row 1 and B05.14 item 4 as copied in the plan. Measured (`selfcheck.py`): 0/200 margins equal to the live roll on
  the same key and record; mean ob(model) - ob(live) = +2.20 (the even line 2.4 less the live cap/halving); the live roll
  consumed up to 15 rng calls per speech; band odds differ by up to 0.46.
- **G13 (H)** PLc:18 B24p.13 item 3 `pool.judging` = "the larger of his held rank ... and `untrained(fx)`, plus the
  `POOL_ADDENDS` sum" — NOT through `pool_of`, so no `pool_add` (6) and no `pool_floor` (5) — while RD:256 (C.7) gives a
  hearer `pool_of(untrained, 0, pool_add, pool_floor)` (= 8) and RD:345 / B24p.12 put `even` (= MU x pool_add = 2.4) in
  EVERY ballot's obstacle. A bench seat therefore ballots on 2-3 dice against an obstacle built for a 6-die base. Measured
  (`probe_findings.py`, shipped, default people): of 557 legal trials ending with the track at >= +2.9 for `for`, 54 were
  carried; of 552 such conversations (hearer ballot), 286. Bench types read 80-95 % Failure at both dial sets
  (`probe_readings.py`). *Choice:* as written.
- **G14 (L)** B05.14 item 3's `SocialContestInput` is not in the tree; the model's record carries only the fields the
  composer reads (`dice.SocialContestInput`); lane A's `reception/proof_step/forgery` fields are dropped (B05.17 moves the
  room into `obstacle_operands`).
- **G15 (L)** P8:131 B05.02 row 3: the H-213 cap "solved on the closed form", and "with a signed channel the floor is
  solved at the largest lawful disadvantage (the soft cap's -M_MAX)" — the second clause gives no formula. *Choice:*
  `cap(p) = MU p + sqrt(p) (ceiling - MU)` (the pool at which Partial-or-better equals one die's chance at the ceiling, no
  boost). Binds only on bench pools (G13).
- **G16 (L)** B06's `Draw` and `fmath.tanh` are not in the tree. *Choice:* `rng.Draw` = `random.Random(sha256((seed,
  actor, label)))` normals with a counter; `math.tanh`.

## Shipped values and controls

- **G17 (H)** RD B.1 (RD:483) ships `strike_level: minor`, RD C.1 (part2:38-40) ships `presumption_level: minor`, RD B.3
  (RD:697) ships `reading_kept: on`; PLAN B24p.23 item 1 (PLc:187) and the batch DIALS line (PL:41) leave all three at
  control "for B98", and RD5:129 F.4 says B98 writes each "BLOCKED (design: no target reading) unless Jordan gives one".
  The plan governs, so at shipped: (a) the `presumes` key of C.1/C.3 (and C.8's "presumed for the charge") has NO effect
  anywhere; (b) a side's off-topic strikes cost it nothing at the close (only the per-speech `off_topic` term), so the
  `strikes` column (k = 1, 2) is inert except through `struck_ends`, which is False on every seeded row; (c) B.9's
  `relevance` strike term is 0. *Choice:* plan (`dials.shipped`); `dials.rd_shipped()` gives the RD's literal column.
- **G18 (M)** B24p.04's controls are "the value at which the role does nothing" but the B05 values beneath them (pool_add 6,
  pool_floor 5, opposition_rate 0.4, difficulty_ob half arm, regard_step 1, reception_gain 1, favour_level major) are not
  B24p's to control. *Choice:* both dial sets carry B05.23's shipped arm.
- **G19 (M)** RD:198 `stakes` "(B05.21 stakes_ob), 0 with none"; B05.21 ships `stakes_ob` 0 for every kind and only B98
  sizes it (P8 B05 DIALS line). So `ProceedingType.stakes` is 0 on every row through B24p: "what is at stake" (R4's first
  parameter, C.1 row 1) does not reach the ballot. *Choice:* 0 (`data.STAKES_OB_B98` available for a planted run).

## The exchange (RD A.4; B24p.07-.10)

- **G20 (M)** RD:285-287 T is "the weight-mean of `deciders`" — which fields are meaned is unsaid (score, will, grace,
  attunement, moved_by all matter). *Choice:* every numeric field and the moved_by vector, by `Decider.weight`.
- **G22 (M)** RD:666 `fit_body` over "the deciders an argument addresses"; under `hearers` (conversation, questioning) the
  `against` speaker IS a decider (B24p.13: "the one addressed ... followed by the hearers"), so his own argument would be
  fitted to his own dispositions; under `mutual` there are no deciders. *Choice:* exclude the mover; fall back to hearers,
  then to the other speaker.
- **G23 (L)** C.4 `concede` "the track moves `concede_step` toward the other side" — no clamp stated, but A.3 says the track
  is clamped "after every exchange". *Choice:* clamp.
- **G24 (M)** PL:227 B24p.09 the hold is drawn on every exchange "whatever the pull" and PL:246 B24p.10 "`s.strikes += 1`
  when off the topic" with no draw condition: a `rest` or `concede` whose hold fails is an off-topic STRIKE. At shipped
  every room has `distraction` >= 0.25, so every exchange (rest included) can strike; at Focus 4 in a private room the
  off-topic share is about one in three. *Choice:* as written.
- **G26 (M)** PL:264 B24p.11 `_auto`'s `p_land` is "read from `exchange_odds` for that press on his believed values (the
  reading's entries)". The reading holds only `moved_by` and strain; a press has `fit: false`, so no believed value enters
  its speech record, and `exchange_odds` reads the TRUE target score and the TRUE Will (`resist`) — against RD:245
  `ExchangeView` "never the other side's true values". *Choice:* the true record (only course the text allows).
- **G29 (L)** RD:265 `Exchange.margin` "the speech draw's real margin" — undefined for `rest`/`concede` (no draw).
  *Choice:* 0.0 with empty `terms`/`levels`.
- **G47 (M)** RD:466 the hold's obstacle is `even + pull`; with `distraction` on every kind at shipped, Focus is never inert
  (B.8's "when it does nothing: nothing pulls" never occurs in a shipped room). Implemented.
- **G48 (M)** One stance read twice: B05.21's `regard` obstacle term (the hostile hearer's stance, one counterparty, no
  audience) enters the speech, and C.7's `Decider.lean` (the same hearer's stance x regard_step) enters his ballot, in the
  same full `conversation`. *Choice:* both, as written.
- **G51 (L)** `proofs` is a `bound: host` advantage source (B05.17 `_proof_levels`) but B24p.07 item 4 computes it in the
  module and B24p.13 excludes it from `Speaker.levels`: two owners of one source's formula. *Choice:* the module's.
- **G52 (L)** RD:915 "fit (B.3; argue and answer only)" vs PLAN B24p.01 `fit: true` on `argue` AND `deceive`. Plan.
- **G59 (L)** PL:212 the reading's guard is "the other speaker's `grace`" even when the argument addresses a bench: reading
  the room is opposed by the opponent's composure, not the room's. As written.
- **G70 (M)** RD:548 `pool = pool_of(case, ...) * heard`: `heard` multiplies AFTER the floor, so a speaker short of the
  room's attention falls below `pool_floor` (5 x 0.5 = 2.5): the floor is not a floor. As written.
- **G73 (L)** B.9's `lost` needs each exchange's track increment; A.3's `Exchange` has neither the side nor the increment
  (recomputable by replaying clip/clamp, as A.2's host does). The module keeps the deltas locally.
- **G74 (L)** RD:250 `ExchangeView.read` lists "believed sore ground"; B24p.08's `_read` returns no such entry. Omitted.

## The sitting (RD A.5, A.6; B24p.11)

- **G21 (M)** RD:323 `rested` = "every side rests in turn, or has no legal move but `rest`"; PL:265 B24p.11 ends `rested`
  only when `_mover` returns None. *Choice:* both (a run of `len(speakers)` consecutive rests also ends `rested`).
- **G25 (M)** "the sides in turn" with "a speaker with no legal move but rest is passed over" (PL:262): who speaks after a
  pass-over is unsaid. *Choice:* the next in the order's cycle after the last mover who can move.
- **G28 (M)** PL:262 "`effort - spoken`": `spoken` undefined (every exchange, or drawing ones only). *Choice:* every
  exchange he makes, rest included.
- **G42 (M)** PLc:12 "`effort = effort + 1` for the actor, and the same for the one addressed"; with an act effort of 0
  (D.1 `argue`: "two exchanges") every full sitting is two exchanges and ends `rested`, whatever the row's minimum:
  `parliamentary_debate` ([3, 5]) runs 2 (measured). `exchanges[0]` is read nowhere: PL:265's "A sitting shorter than
  `type.exchanges[0]` continues past `rested` only if a side can still move" is vacuous (`rested` means nobody can).
- **G44 (M)** PL:265 `yielded` = "a side with `resolve <= 0` whose opposite still has resolve and effort", and resolve falls
  by one per drawing speech AND by `mark_resolve` per mark. With A.6's policy (the side behind presses), the side AHEAD is
  rattled and yields: measured, legal_trial at effort 2: 404/1000 sittings `yielded`, the yielding side leading the track
  in 344 (and unmarked in 73: pure attrition). `yield_level` then counts against the leader. As written.
- **G45 (M)** RD:1045-1046 / PLc:194: `_auto` never forms a `divert` and no seeded rite holds `deceive` (an abridged `lie`
  has `deceive` but no ballot), so B.9's `relevance` (thread lost) and `sincerity` are 0 in every automatic sitting; the
  RD concedes it. Confirmed by `selfcheck.py` (300 arbitration sittings: 0 non-zero ballots, 0 diverts).

## The close (RD A.5, B.9; B24p.12, .14)

- **G31 (M)** RD:215 `deciders` "in id order" vs PLc:13 under `hearers` "the one addressed ... followed by the hearers".
  *Choice:* `_close` sorts by id (the RD's and B24p.12's "in id order").
- **G32 (M)** PL:281 `closing_odds(inp, state)`: `ProceedingState` holds no exchanges, but `sense` and `lost` read them.
  *Choice:* an optional `exchanges` argument.
- **G33 (M)** PLc:36 `act_margin(outcome, type)`: `hearers` needs each verdict's weight and `none`/`mutual` need the `for`
  speaker's id; neither is in `(outcome, type)`. *Choice:* `inp` passed.
- **G34 (M)** RD:157 a bench seat's `score` "is the respondent's"; the `audience` row is a bench with ONE speaker and no
  respondent. *Choice:* the seat's own score there.
- **G39 (H)** PLc:36 under `none`/`mutual` the act's margin is "the margin of the last exchange drawn by the ACT's actor",
  whatever that exchange's effect: a landed `press` or `divert` (which moves no track) reads as the act succeeding.
  Measured: negotiation, 99/1000 sittings band Success+ while the track stands AGAINST the actor; negotiation reads 40 %
  Overwhelming at both dial sets. As written.
- **G41 (M)** RD:335 / part2:265 C.8: `bench` ballots "the presiding seat ALONE"; PL:280 B24p.12 `_close` ballots "every
  other value -> per `inp.deciders` member", and `act_margin` reads the first. Plan governs: every seat drawn (3 normals
  each), only the presiding verdict used.
- **G43 (M)** no check that a `declared` row's filtered bench can reach its `quorum` (C.2 lists none): with fewer seats than
  `quorum` (`excommunication_deliberation`, quorum 2, behind a one-seat church bench) the veto fires on every sitting.
  `selfcheck.py` FAIL with the toy bench; whether the realm seats two church seats per venue was not read (C.8 claims three).
- **G49 (L)** A one-speaker bench type's T (the bench mean) takes the seats' `score`, which under G34 is each seat's own.

## Host (C.5-C.7; B24p.06, .13, .15)

- **G27 (L)** `RUNG_KINDS` order and `DISPOSABLE_KINDS` were not opened. *Assumed:* `hearth < settlement < duchy < realm`;
  `oblige, detain, ban`.
- **G35 (M)** C.5's example ("an abridged `tell` ... reads `none`") requires the one addressed NOT to count as a hearer;
  then a `rally` to one cohort with nobody else present reads `none` (attention 0, proof_weight 0.5), not `crowd`; the
  crowd must be onlookers. *Choice:* the addressed is never a hearer.
- **G36 (H)** part2:218 case_rows row 2 names `parliamentary_debate`, whose `disposes` is `Record`; part2:229
  `row_for_case` "skips a row whose `disposes` is not disposable" (`DISPOSABLE_KINDS`), so row 2 can never be named.
  `selfcheck.py` FAIL: never named `['parliamentary_debate']`.
- **G37 (L)** `pool.score(w, p, verb)` not read: *Choice:* held `argue` rank, else `pool_default` (2).
- **G38 (M)** RD:257 a hearer's `lean` is "his regard for the speaker": with two speakers, whose? *Choice:* the `for`
  speaker's (lean is signed toward `for`); his regard for `against` is ignored.
- **G40 (L)** B24p.11's test "no decider is asked" holds only because the host passes `decide=None`; the module asks any
  callable it is handed, abridged or not.
- **G62 (L)** PL:176 `strain_carried` "`0.0` when `blow_gain` is 0" is an extra clause, not a consequence of its formula
  (which reads `press_base`, 1.0 at control). Implemented as an explicit branch.
- Host levels: of the `bound: host` sources only `favour` (B05.17) and an `office` level (A-12) are modelled; `effort` and
  `capability` (B05.10) were not opened, so they are absent (toy limitation, not a spec gap).

## Float exactness

- **G53 (L)** RD:609-612, PL:198, PLc:112 assert pool differences "exactly" (4, 1.6, 2.4 dice times the share heard). The
  blend is exact in tenths (`weighted_tenth`), but the pool is a binary float: Reason 2->6 at k=4 gives 1.6000000000000014,
  Presence at k=4 gives 2.3999999999999986, 4 x 0.9 gives 3.6000000000000005. A `==` test as written fails; it passes
  within 1e-9. (`selfcheck.py`: 5 FAILs, all this one cause.)

## Self-check findings (spec assertions NOT reproduced)

1. B.7's control equality against the LIVE `roll.py::roll`: fails, by construction (G12).
2. "Exactly" pool differences: float, not exact (G53).
3. case_rows row 2 unreachable (G36).
4. A declared bench smaller than its quorum is admitted and always vetoed (G43; toy bench).
Every other numeric assertion reproduced: k 10/0/4; resolve_0 3.0/5.0 (and 2.5/5.0); shield -0.9/-0.5 and 0.6 at Will 7;
delivery +-0.5; heard 0.7; venue_standard 1.5/0; esteem +-0.16; account 0.9 at Reason 7; pw_d 0.75->0.90; f_d 0.25/1.75;
relevance = f_d x 0.25 x 2; usable proofs 1.0/3.0; G+5 = 9 and 3 per decider; ballots in id order; track clamp; the
B.9 zero; `1 - steady_odds` = 0.406 at zero strain (B24p.11); the four statistical directions (B.1, B.3 ii/iii, B.6 i)
and B.6 (ii)'s "Will 2 spends first in every sitting". Readings: `read_ob`/`ploy_ob` "even odds" read 0.532.
