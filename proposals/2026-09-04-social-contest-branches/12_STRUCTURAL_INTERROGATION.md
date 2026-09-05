# 12 · STRUCTURAL INTERROGATION — what shape the social contest engine assumes, and what that assumption costs

## Status: **READ-ONLY INTERROGATION, 2026-09-04. PROPOSED. Nothing ratifies on merge. This file is the only artifact; nothing else under the repository was created or edited.** Branch `claude/social-contest-system-review-dn2y5d`, HEAD `3ade3e33`.
## Author: Fable 5.1, `CLAUDE.md` §10 audit/planner node — this is a structural reading for **Opus 5 to build from** (§8), not a design. Sibling: `11_FOUR_GAMES_AUDIT_AND_PLAN.md` audits the four games for logic/coherency/NERS; **this file does not repeat it.** Where the two meet (the "issue fold"), §7 says why the fold is a second axis, not the master one.
## Grade under `CLAUDE.md` §0.2: every number below **executed** (§0.3); every design statement is **paper**.

---

## §0 · Scope, method, what was executed

### §0.1 The question, and the six lenses

Jordan's five observations (brief, verbatim) are all about **shape**: odds and bands; many lines of adjudication with a verdict each; bundles of subtopics with conditions; non-zero-sum and more-than-two-sided outcomes; the adjudicators being the contestants, or one contestant; persuasion tracks and audience. The coordinator added the **parliament** as the worked case that exercises all six at once (§7.2). The question under all of it: *what shape does the kernel assume, and what does that assumption cost?* — asked through six lenses, each with the same five questions: **(a) declared? (b) reachable on the production path? (c) load-bearing — does a resolver read it? (d) what does it presuppose? (e) what breaks when the presupposition fails?**

**Out of scope, by Jordan's instruction:** `engine/cross_scale/*` (the seams). The one seam-derived number I use — *81.9 % of 4,979 councils fought at faculty 1 v 6* — is **inherited from `08_NERS.md` §1.1** (`ners_ablate.py`, n = 64 campaigns) and **not re-verified here**; every measurement I ran at 1 v 6 stands on its own.

### §0.2 Method

Read every anchor cited; **checked the assertion, not the prose above it** (the failure this session has a measured rate on — §1.3 and §1.4 are two more instances). Where a claim is a number it has a script and an output line. No `pytest`. Nothing under the repository written except this file. Scripts in the session scratchpad: `interrogate.py` (S1–S8) and `mutual.py` (M1–M2).

### §0.3 Execution artifacts (all seeded; `random.seed(s)` per bout; the kernel's own global stream)

| id | drives | headline |
|---|---|---|
| **S1** | `build_contest(1, 6, venue="guild_arbitration")` × 400 seeds; `VoteAtClose` verdict vs `PersuasionTrack(start=5).resolve()` on the **same final `ContestState`**; benches 4/5/6/7; 5 v 5 for contrast | reproduces the brief's numbers exactly; draw 0 % at 5 and 7, 10 % at 4, 6.5 % at 6; at 5 v 5 the ballot says 52.5/47.5 where the track says 87.8 % committee |
| **S2** | `private_negotiation` 5 v 5 × 1,500 seeds under the canonical `no_adjudicator` and four swapped tastes/disciplines | the fabricated third party's taste moves P(A) from 0.3 % to 99.7 % |
| **S3** | leak table for the four canonical adjudicators × `public`; `Pressure` toward A/B on three proceedings × 1,500 | leak is saturated at `LEAK_CAP` for crowd and no_adjudicator at any `public` ≥ 0.4; only the bias half of `Pressure` is live there |
| **S4** | `grand_contest` with B = `fallback_ladder`, `record=True` × 400; three "topics" as three bouts under shared vs per-topic inputs × 400 | the live ground moved in 400/400 and `adv` did not partition; per-topic texture appears only with per-topic inputs |
| **S5** | `(adv[A], adv[B])` pairs × 2,000 on three proceedings | corr ≈ +0.02; the declared loser exceeded the median winner's persuasion in ~10 % of bouts |
| **S6** | `run_parliamentary_vote` × 3,000 with a duck-typed world; zero-zero under the clamp; resistance × pool size; a scratchpad ballot with an abstention dead-zone | **0 / 3,000 mismatches** against `PersuasionTrack(scale=1, start)` on `(movement_a, movement_b)`; the zero-zero branch is inert under ED-621; abstention makes draw reachable at n = 5 |
| **S7** | a scratchpad `Bout` subclass accumulating `adv` per `(side, member)` with each member's own leak/character × 400, homogeneous vs heterogeneous bench | homogeneous bench: 0.000 between-member spread, 0/400 splits; heterogeneous: 1.82 spread, 346/400 splits — vs the modelled i.i.d. noise of 1.33 |
| **S8** | `church_tribunal` × 300 seeds × 4 styles, `armature=None` vs `opponent_is_adjudicator=True` vs `False` | the gate zeroes δσ only; CR4's +1D and CR5's backfire still fire under the "gated-off" armature |
| **M1** | a scratchpad `Bout` subclass whose reception for side X reads the **counterparty's** taste, `private_negotiation` 5 v 5 × 1,500 × 3 tastes × 3 appeals | A's best appeal tracks B's taste (51.7 / 59.3 / 82.3 matched vs 3–5 % mismatched); under today's dummy, courtier wins 75 % regardless of who B is |
| **M2** | the same 2-D state read as an overlap (both moved ≥ a floor) vs `TallyAtClose` | 96.5 % "both moved" read as a 59/41 winner |

---

## §1 · L1 · TOPOLOGY — who decides

**(a) Declared.** Yes, twice, and the two declarations disagree. `modes.py:485-519 PROCEEDINGS` carries `roles` with six values — `alternating` ×2 (`:487`, `:490`), `crown_objects` (`:493`), `inquisitor_proposes` (`:496`), `symmetric` ×2 (`:508`, `:514`), `initiator_proposes` (`:511`), `appealer_proposes` (`:517`) — and `adjudicator` with four types (`:463 CANONICAL_ADJUDICATORS`). Canon `social_contest_v30.md:97-108` (§2 Step 5) is the source column *Role Structure*; `:391` defines it: *"Institution assigns Proposer/Respondent roles. Roles do NOT alternate."* So `roles` is a **turn-structure** label — who proposes, whether the proposer role rotates. But canon `:179` adds a second meaning to two of the six: *"In proceedings where the adjudicator IS the opponent (Royal Audience — the Crown objects; Church Tribunal — the Inquisitor proposes)"*. That is **decider identity**, and it lives inside a turn-structure enum.

**(b) Reachable.** `roles` reaches nothing. The only readers in the tree outside its definition are two `_kernel_tests.py` assertions — `:577` (`PROCEEDINGS["guild_arbitration"]["roles"]=="symmetric"`) and `:1400` (`PROCEEDINGS["church_tribunal"]["roles"] == "inquisitor_proposes"`) — verified by grep across `systems/`, `engine/`, `tests/`, `tools/`. (`_kernel_tests.py:149 prate(..., roles=)` is a different `roles` — a venue proof-weight dict, `:150-152`.) `dictionaries.py:503-620 Proceeding.role_structure` is a prose label from `_PROCEEDING_PROSE`, not a read of `PROCEEDINGS["roles"]`, and `_crosscheck_proceedings:607-624` compares `exchange_count`/`adjudicator_type`/`track_start`/`tracker_mode` — never `roles`. **My reading of the brief is confirmed: two test assertions, no resolver.**

**(c) Load-bearing.** Nothing. `Bout` consults exactly one object for "who decides": `self.adj` (`resolver.py:243`), read at `:280` (`ContestView.audience_learned/hostile`), `:323` (leak), `:326` (character), `:376` (`SelfGating`), `:405` (`armature.dsigma`), `:462`/`:465` (`win.resolve(adj=)`). It is always a **third party**, and it is the same object for both sides' moves.

**`no_adjudicator` fabricates a third party where canon says there is none — executed.** `modes.py:449-454` returns `Adjudicator(learned=True, discipline=0.30, char 0.34/0.33/0.33)` and its docstring says so: *"Re-skins a single low-discipline neutral Adjudicator (character leaks — the counterpart is read)"*. The parenthesis is false: nothing about the counterpart is read; the dummy's own neutral taste is. **S2:** at `private_negotiation` 5 v 5, A = demagogue vs B = logos, the canonical dummy gives A 64.5 %. Swap the dummy's taste to logos-heavy: **0.3 %**. Pathos-heavy: **99.7 %**. Raise its discipline to 0.90 with neutral taste: 32.3 %. The invented party's taste is the single largest determinant of a contest canon says the parties decide themselves. Two consequences follow from the numbers, not the prose: **(i)** `Resonance.leak(0.30, f)` is already 0.70 at `standing_frac = 0` and hits `LEAK_CAP` 0.90 at `standing_frac ≥ 0.4` (`primitives.py:242-245`), so `res ≈ 0.1·venue_w + 0.9·0.33` — nearly appeal-blind; **(ii)** the residual lever is `Readiness` (`:253-260`), fed by ethos-built Standing, which is why **courtier beats logos 75/25 under the dummy** while losing 30.6/69.4 before an `expert_judge`. Canon's *"Attunement-primary — you must read the other party"* (`modes.py:429`, `v30` §3) is unexpressible: there is no other party to read. (`06_SYSTEM_AUDIT.md` FA5.2 records the venue-dependent dominance; the *cause* — a fabricated decider saturating leak — is the finding here.)

**`opponent_is_adjudicator` does not change who rules, and does not gate the armature "entirely" — executed.** `armature.py:374-395 position_of` returns the zero vector when the flag is set (`:389-390`), so `ArmatureConfig.dsigma` (`:436-451`) returns 0.0. Nothing else reads the flag; `Bout` never does. **S8**, `church_tribunal` × 300 seeds: with `styles={A:"precedent",B:"precedent"}` the "gated-off" armature still differs from `armature=None` in **126/300** bouts (CR4's +1D at `resolver.py:402-404` keys on the chosen genre, Memory at FACT, and is not gated); `suppression` still fires CR5 (`cr5_self_backfire("suppression", False, 5.0) = 2.0`, `resolver.py:423-438`). Canon `:179`'s *"the armature is gated off entirely"* is false in code; one of three channels is gated. And the topology the gate was written for does not exist: `PROCEEDINGS["royal_audience"]["adjudicator"] == "expert_judge"` and likewise `church_tribunal` (`modes.py:494`, `:497`) — a third party rules in both. `03_INQUIRY.md:176-178` carries the contradiction forward verbatim (`adjudicator = expert_judge, armature = ArmatureConfig(..., opponent_is_adjudicator=True)`), and `01_SPINE.md:553-561` A7 proposes deriving the flag from `roles` — making `roles` load-bearing on exactly one bit, for a bout in which the opponent does *not* adjudicate.

**(d) Presupposes.** Two things. (1) That there is always a third party with a taste and a discipline against which every reception is scored (`resolver.py:323-326`). (2) That `roles` will be read by the canon §4 Step 4 interaction model — the only place canon uses the proposer role mechanically is the TIE rule, *"Persuasion Track moves +1 toward first-to-speak holder's position"* (`v30:209`, `:213`) — and that model has no engine (`10_SC_STRUCTURAL_READING.md` §1.8, re-verified: `_apply` never compares the two sides).

**(e) What breaks when it fails.** Negotiation (no third party): the dummy decides (S2). Royal Audience / Church Tribunal (the opponent rules): the Crown accumulates `adv` against its own judge — a decider with an accumulator, which is meaningless; and the *resistance* that canon gives the deciding side (`resistance="halved_petitioner"`, `:493`; `_derive_resistance`, `wrapper.py:43-56`) is computed and carried on `Contest.resistance` (`:75-79`) and read by nothing that resolves. The body case (parliament, §7.2): N deciders who are also parties have no representation at all — `Panel` averages them into one mind for the bout (`contract.py:47-51`) and `VoteAtClose` re-splits that one mind with i.i.d. noise at close (`resolver.py:139`, `:144`).

---

## §2 · L2 · TRACK — how many positions move, and whose

**(a) Declared.** One track, two-pole: `PersuasionTrack` (`resolver.py:81-95`), 0–10, start 5, `track = start + 1.5·(adv[A] − adv[B])` (`:87`). `TRACKERS` (`primitives.py:154-166`) binds it as *"merits clock (0-10 banded, two-pole; PRESERVED)"*, `per_side: False`. Underneath it, **two accumulators**: `ContestState.adv = {A: 0.0, B: 0.0}` (`resolver.py:50`). Beside it, two more per-side movers that are not tracks in canon's vocabulary but are positions that move: `Standing` (Face, `primitives.py:31`) and `Room.r = {A, B}` (`:232-236`).

**(b) Reachable.** `PersuasionTrack` on five of eight proceedings (`modes.py:556-557`); `TallyAtClose` on three (`:558-559`, the difference without the banding); `VoteAtClose` on `guild_arbitration` (`:553-555`). The accumulators on all eight.

**(c) Load-bearing.** Every terminal reads `adv` (`10_` §1.2, re-read); none reads Standing or Room, which feed only `Readiness` and leak (`resolver.py:323`, `:333`).

**The hypothesis — track count is a function of topology — tested case by case.**

| topology | hypothesis predicts | what the kernel has | verdict |
|---|---|---|---|
| one neutral decider (judge) | one track = the judge's position | `PersuasionTrack` = start + scale·(advA − advB): the judge's position moved by both | **holds**, and is what the code is |
| two self-deciding parties (negotiation) | two tracks; overlap = deal (ZOPA) | the two accumulators **already are** two tracks — `adv[A]` is "how far the hearer of A's moves has moved", `adv[B]` likewise; but the hearer is the dummy (§1), and the terminal projects the pair onto a difference and discards the overlap. **S5:** corr(advA, advB) = +0.02; in **~10 %** of bouts the declared loser had persuaded more than the median winner. **M2:** with concession floors of 2.0/2.0, **96.5 %** of bouts are "both moved" — `TallyAtClose` on the same bouts returns a winner in every one (59.3/40.7) | **holds — the state exists, the terminal throws it away** |
| one party decides (Royal Audience) | one track = the deciding party's position; the other party's moves push it; the decider's "objections" are resistance, not a track | two accumulators, one third-party judge; the Crown's `adv` is an accumulator with no reader that should exist; canon's resistance modifier is dead (`wrapper.py:75-79`) | **holds as a design; fails as code** — the kernel gives the decider a track it cannot mean |
| an N-member body | N tracks | one mean mind (`contract.py:47-51`) during the bout; N i.i.d. ballots at close. **S7:** on the shipped homogeneous `panel()`, per-member reception would give **0.000** between-member spread and **0/400** split benches — the members are one track by construction; on a heterogeneous five, spread **1.82** and **346/400** splits, versus the modelled `noise/sharpness = 0.8/0.6 = 1.33` | **holds, but only at the played fidelity** — see the first break below |

**Where the hypothesis is too neat — three places it breaks.**

1. **Depth.** The parliament (§7.2) has N positions and they are **fixed inputs** — `VoteDeclaration.side` (`parliamentary_vote.py:89-93`) — moved *between* scenes by prior Diplomacy (`Motion.lobbying_offset` → `start`, `:160-163`; canon §10 `v30:597`) and never during the vote. So N tracks exist at depth 0 as **start positions**, not as movers. Track count is a function of topology **and depth**: at depth 0 every position is a `start`; at depth k they move. The kernel already carries the cross-scene position as `PersuasionTrack.start` (`resolver.py:86`; chain contests resume from the previous final position, `v30:373`). The hypothesis holds only if "track" is allowed to persist across scenes, which the code half-does.
2. **Fidelity.** The Formal Contest's crowd is canon's *adjudicator* (`v30` §2 Step 1; `modes.py:440-447`) — fifteen minds averaged into one (`contract.py:47-51`). Whether that is one track or fifteen is a **fidelity** choice (`auto_manual_resolution_duality_v1` — ED-SC-0013, resolved), not a topology fact; S7 shows the count collapses to one whenever the members are authored identical, whatever the topology says.
3. **Audience tracks.** `Room.r` (`primitives.py:232-236`) is a per-side position that moves every pathos move (`resolver.py:338-339`) and decides nothing (it feeds `Readiness`, `:333`). So track count ≠ decider count: **there are tracks that are not any decider's position.** The clean statement is *decider tracks are a function of topology; audience tracks are a function of who is in the room.*

**(d) Presupposes.** That the two accumulators are commensurable and opposed — which is true only before a single neutral hearer. `PersuasionTrack.scale=1.5` (`:86`) and `faction.coalition_vote(scale=1.0)` (`faction.py:128`) are the two shipped values of the one number that says how far a difference in persuasion moves a decider — a `[SEED]` with two homes (`10_` D5).

**(e) What breaks.** In the mutual case the difference is the wrong function (M2). In the body case the average is the wrong function (S7: the modelled noise is a stand-in for member heterogeneity that the averaging destroys — and it destroys *structured* disagreement and replaces it with random). In the one-party-decides case one of the two accumulators has no meaning.

---

## §3 · L3 · AUDIENCE — who influences without deciding

**(a) Declared.** Six mechanisms in the kernel and two more in the parliament module. In the kernel: **(1)** `Pressure.public → leak` (`contract.py:70-77`; `resolver.py:323-324`, `+ public·PUBLIC_LEAK`); **(2)** `Pressure.public → bias` (`:310-312`, `+ public·PUB_BIAS` on the favoured side only); **(3)** `Pressure.institutional → bias` (`:312`, `+ institutional·INST_BIAS`); **(4)** `Room → Readiness` (`primitives.py:232-236` → `:253-260`; `resolver.py:333`, `:338-339`); **(5)** `ContestView.audience_learned / audience_hostile` (`contract.py:64-65`) — which are **not the audience**: `resolver.py:280` fills them from `self.adj.learned/hostile`, the decider; **(6)** `_derive_resistance` (`wrapper.py:43-56`), canon's *"average Stability of represented factions … −1"* (`v30:94`), computed, carried on `Contest.resistance`, read by nothing. In the parliament: **(7)** the audience bonus `+1D` when the side's genre matches `parliament_dominant_genre` (`parliamentary_vote.py:174-175`); **(8)** abstention resistance (`:153-158`). Dead beside them: `FACTION_BOOSTS`/`guilds_boost_for` (`dictionaries.py:387-487`, zero resolution consumers — `ED-SC-0028` verified the +1D is prose-level).

**(b) Reachable.** (1)–(3): only through a prebuilt `Venue` — `build_contest:133` passes no `**o`, so `Venue.pressure` is `Pressure()` on all eight proceedings (`10_` §1.7, re-verified). (4): every bout, every pathos move. (5): every bout, misnamed. (6): computed every named-proceeding build, inert. (7)–(8): every parliamentary vote.

**(c) Load-bearing.** (2)–(4) on any bout that carries them; (1) **only where discipline is high**. **S3** leak table: for `expert_judge`/`panel` (discipline 0.75) leak runs 0.25 → 0.75 across `public` 0 → 1 at `standing_frac` 0; for `crowd`/`no_adjudicator` (0.30) it starts at 0.70 and is **pinned at `LEAK_CAP` 0.90 from `public ≥ 0.4`** — and at 0.90 for any `standing_frac ≥ 0.4` regardless of `public`. So *"public pressure makes the adjudicator more swayable"* (`contract.py:73`) is inert on exactly the two adjudicator types canon associates with a public. **S3** outcomes: `formal_contest` (crowd) — `public=0.7 → A` moves the band distribution from 99.5 % committee to 99.6 % committee (nothing); `institutional=1.0 → A` moves it to 29.3 % A_decisive (the bias half works). `private_negotiation` (dummy) — `public=0.7 → A` moves P(A) 51.7 → 79.5 % — **entirely the bias half**, since leak was already saturated. `royal_audience` (expert judge) — public 0.7 → A_decisive 6.8 → 25.8 %.

**So audience = "make the judge rule as a person rather than as an office" is one of two live meanings, and the weaker one.** The other — *a thumb on the scale for the favoured side* — is a multiplier on that side's every gain (`_bias`, `:310-312`) and works in every topology because it never asks who the office is.

**(d) Presupposes.** The leak half presupposes an **office/person distinction on the decider**: a venue proof register (`Venue.role()`, `:167`) versus the adjudicator's own `character()` (`contract.py:34-35`), blended by leak (`resolver.py:326`). The bias half presupposes only a favoured **side**.

**What it means when there is no office.** In a mutual topology the decider of A's move is B, and B has no office — B's "role weights" *are* B's character. Leak is then the identity blend and the leak half of `Pressure` has nothing to act on; the bias half survives unchanged: the public favouring B is a multiplier on B's gains against A, i.e. on how much A concedes. **When the office-holder is the opponent** (Royal Audience), the leak half means *the Crown rules as a person rather than as the Crown* — which is a real thing (a king swayed by the mob) and is exactly the case the code cannot reach, because the Crown is not the adjudicator in code (§1). `crowd` is a third, separate object: a **decider** (a Panel, `modes.py:445`), not an audience — the same word for a bench of fifteen and for the gallery pressing on a bench.

**Do they compose?** (2) and (3) compose additively inside one multiplier (`1 + inst·0.6 + public·0.3`, `:312`), applied to one side only — an asymmetric multiplier that never touches the unfavoured side. (1) composes with the standing-fed leak by addition under a cap, and the cap is what kills it (S3). (4) composes with nothing on the adjudicator side — it is a per-side self-reinforcement (pathos → Room → Readiness → bigger pathos gains; `06` FA5.2). (6)–(8) are three homes for "audience resistance": canon's Stability-derived subtraction (dead), the parliament's abstention-derived subtraction (live, per side, floored at 0 — `:185-186`), and `faction.RESIST_DAMP` (`faction.py:28`, `:141`), which **damps the track scale instead of subtracting**, with an inline comment rejecting the subtraction (*"went inert at large pools"*). **S6** measures the parliament's version: at pool 16 per side, resistance 2 raises P(committee) from 4.9 % to 16.3 %; at pool 2, from 58.3 % to 94.6 %. Attenuated, not inert — the rejection in `faction.py` overstates. Three implementations, one canon rule, no shared owner.

**(e) What breaks.** With no office, `public` collapses to `bias` and `PUBLIC_LEAK` is a dead constant. With the opponent as office-holder, the one interesting case (the king swayed) is unreachable. With a body, `Pressure.toward` must name a **position**, not a side — the Crown leaning on a chamber presses on members, and `Pressure` has no member dimension (`contract.py:75`, `toward: A | B | None`).

---

## §4 · L4 · SUBJECT — what is being decided

**(a) Declared.** One axis, six values: `Stasis.LADDER = [fact, definition, quality, jurisdiction, consequence, feasibility]` (`primitives.py:14`), with `stronger_than` = higher index (`:23`) and a tense map (`:16-17`). **No topic object exists anywhere in the package** — `Move.ground` is a stasis (`contract.py:14`), `Bout.live` is a stasis (`resolver.py:245`), `EvidenceItem.ground` is a stasis (`primitives.py:283-289`). `11_` §3 row 3 says the same and I re-verified the three anchors.

**(b) Reachable.** `shift` is a live move kind (`resolver.py:352-358`) and `fallback_ladder` issues it (`policy.py:25-31`). **S4:** `grand_contest` with B = `fallback_ladder`: the live ground moved in **400/400** bouts — the loser reframes whenever not leading, and B starts not leading. `church_tribunal` starts at FACT (`modes.py:499`); the other seven at QUALITY (`resolver.py:155`).

**(c) Load-bearing.** The ladder gates **which moves count** — `Stasis.relevant` at `resolver.py:380-381` (off-ground → evasion fault), `stronger_than` at `:356-357` (downward shift → contradiction fault). It does **not** partition what was decided: `_advance` adds to `state.adv[side]` with no ground key (`:335`). **S4** sample log: A advances on QUALITY (+0.66), B shifts to JURISDICTION, A advances there (+0.66), B shifts to CONSEQUENCE, A advances (+0.65) — `advA = 1.97`, one number, three grounds. A shift is a *fault-exposure* move (it changes which arguments are evasions), not a *verdict* move.

**Are the two axes orthogonal?** Yes, and the test that shows it is the one Jordan's example supplies. *"Did he do it / was it theft / was it justified"* is one topic at three stases, and the ladder already sequences it. *"Harbour rights AND toll exemption"* is two topics, and **each is at its own stasis**: harbour rights could be at FACT (did the charter ever grant them), toll exemption at CONSEQUENCE (what it would cost). A move on harbour-rights-at-FACT is not relevant to toll-exemption-at-CONSEQUENCE and should not be an evasion of it either — the relevance gate (`:380`) has no way to say so, because it has one `live`. **The axes collapse only in the degenerate case where every topic sits at the same stasis and is decided by one verdict — which is the case the kernel hard-codes.** Any bout in which two topics can end at different bands (Jordan's observation 2) refutes the collapse.

**Where conditions live — two homes by nature, one declared.**

- **Intra-topic** — *"was it justified"* is conditional on *"did he do it"*: the ladder is already a conditional chain. But note what kind: classically the defender **concedes** the lower rung to contest the higher (`stronger_than` licenses only upward shifts, `:356`), so the condition is *"if the lower rung is conceded, the higher is live"* — a concession structure, not a prerequisite. The kernel records the concession nowhere (§4(c)): after a shift, nothing says FACT was conceded. **Declared (the ladder), not recorded.**
- **Inter-topic** — *"harbour rights IF toll exemption"* is an **edge between two topics' outcomes**, a constraint on the joint verdict vector. Nothing in the kernel; in the corpus it is `settle()`'s `terms` (`00_BRANCH_SHAPES.md` §3(e), `Settlement(share, terms: dict)`) and `TreatyRecord.terms` (`systems/factions/sim/treaty.py:62`), i.e. a **property of the deal**, declared at open (CIP-5's "declared compromise axes", `proposals/social_contest_consolidation_integration_v1.md:335-373`) and evaluated at close. Not a property of a topic (a topic does not know what it is conditioned on) and not an act during the bout (`00` §2.3 cut `offer` moves as false N-lines; an offer is an `utter`).

**(d) Presupposes.** One matter, one stasis at a time, one verdict. And that the party who *reframes* is the one losing (`fallback_ladder` is the loser's policy) — the ladder is modelled as retreat.

**(e) What breaks.** Two topics: unexpressible (one `live`). Two verdicts: unexpressible (one `adv` per side). A condition: unexpressible (no edge). And **texture by per-topic banding is noise unless the topics have distinct inputs — executed.** **S4:** three "topics" as three seeded bouts with identical specs → 5 distinct verdict 3-vectors, every marginal ~99 % committee (the base rate `06` P4.5 measured), differing only by RNG; give topic 0 A-held evidence and topic 2 B-held evidence → topic 0 A_decisive 14.0 %, topic 2 B_decisive 13.2 %, topic 1 unchanged. Per-topic banding multiplies **texture** exactly when topics carry distinct leverage (evidence, stasis, the hearer's taste on *that* question), and multiplies **noise** otherwise. The mechanism that makes it texture rather than noise in a *played* contest is the one shared budget — `Reserve` (`primitives.py:49-56`), canon's Concentration — spent across topics, so the vector is a function of allocation. That is not executed here (the kernel has no multi-topic bout to allocate over) and is stated as design, §8.

---

## §5 · L5 · VERDICT — what comes out

**(a) Declared.** Six terminals, two vocabularies: side labels `a | b | draw` from five classes, band strings `A_total | A_decisive | committee | B_decisive | B_total` from `PersuasionTrack` (`resolver.py:52-147`; `10_` §1.2 table, re-executed). `draw` is declared by `ThresholdRace:60`, `TallyAtClose:66`, `VoteAtClose:138,142,147`.

**(b) Reachable.** On the shipped proceedings: the band vocabulary on five, `TallyAtClose` on three, `VoteAtClose` on one. `ProofBar`/`GraceThreshold`/`ThresholdRace` on none (`10_` §1.7).

**(c) Load-bearing — the brief's measurement, re-verified.** **S1**, 400 paired seeds, faculty 1 v 6, `guild_arbitration`, both terminals on the **same** final `ContestState` (the two-venue route confirms: 0/100 bouts differed in `adv`, since `VoteAtClose` draws only at close):

| terminal | outcome distribution |
|---|---|
| `VoteAtClose` (production, weighted, 5 jurors) | **a 6.2 % · draw 0.0 % · b 93.8 %** |
| `PersuasionTrack(start=5)` on the same state | **committee 29.8 % · B_decisive 50.2 % · B_total 20.0 %** |

Cross-tab: `(b, B_total) 80 · (b, B_decisive) 199 · (b, committee) 96 · (a, committee) 23 · (a, B_decisive) 2` — the ballot awarded A the win in two bouts the track reads as B_decisive. Track position min 0.00 / mean 2.33 / max 6.48: the weak side never reaches the A half of the axis. **The brief's numbers reproduce to the decimal.** The 81.9 % / 4,979 provenance is inherited (§0.1).

**`draw` is unreachable at every odd bench — verified by execution and by arithmetic.** `panel()` defaults to `size=5` (`modes.py:456`); `PANEL_DEFAULT_JURORS` reads that default by `inspect.signature` (`dictionaries.py:697`); members are homogeneous (`discipline` 0.75 ×5, S1). `weighted_by_standing` (`resolver.py:128-142`) draws iff `wA·2 == total`; with five equal weights `wA ∈ {0, .75, 1.5, 2.25, 3.0, 3.75}` and `total = 3.75`, so equality needs `wA = 1.875` — not in the set. **S1** benches: 5 → 0 %, 7 → 0 %, 4 → **10.0 %**, 6 → **6.5 %**. `11_` §1.2 row 2 measured the same across every factory and graded it R-COMPLETE-small; the structural reading is sharper than "even benches would reach it": **draw is unreachable because every juror must pick a side** (`self.k*gap + gauss > 0` is binary, `:139`, `:144`). The object that makes a bench tie at odd size is **abstention**, which the parliament has (§7.2) and the kernel does not.

**The two terminals disagree about what a close room *is* — executed at 5 v 5 (S1):** `VoteAtClose` 52.5 / 47.5; `PersuasionTrack` on the same states **87.8 % committee**. ED-1057 ratified the ballot's reading for the Panel (*"a close room is near a coin-flip"*, `resolver.py:100-105`; `09_PRESCRIPTION.md` §0.1). The band's reading is that a close room is a compromise. Both are declared; the shipped venue picks the coin-flip; Jordan's observation 1 asks for the band. These are compatible only if the ballot **feeds** a band (share − 0.5 as a margin, `00` §2.1) rather than replacing it — which is what `08`/`11` propose and what nothing yet does.

**(d) Presupposes.** One matter. One position (or one difference) to band. A hearer whose ballot is binary.

**(e) Where texture should come from.** Per **track** bands give five outcomes on one matter; per **topic** bands give 5^k on k matters; per **member** (a bench of N with per-member tracks, S7) give a *distribution* over the bench that the aggregate then bands. §4(e) settles the texture-vs-noise question empirically: bands multiply texture in proportion to **independent inputs per banded thing**. So: bands on every decider track (§2), per topic (§4), with the aggregate over members banded once. **Both, and the noise objection is answered by allocation, not by fewer bands.**

---

## §6 · L6 · PARTIES — how many sides

**(a) Declared.** Two, by construction: `A, B = "a", "b"` and `other()` (`contract.py:7-8`). Grep of the four resolving modules finds **16 sites** that assume exactly two: `resolver.py:50` (`adv = {A, B}`), `:70`, `:78` (`other()` inside terminals), `:241` (`self.c = {A: _Side, B: _Side}`), `:273`, `:279` (`_view`), `:344`, `:372` (`_apply`), `:441`, `:443` (`resolve` loops `(A, B)`), `:457`, `:461` (fault check and clinch award); `primitives.py:234` (`Room.r`), `:273` (`DefeatCatalogue.check`); `contract.py:8`; plus `Pressure.toward: A | B | None` (`:75`) and `PersuasionTrack.track` (`resolver.py:87`), which is a difference of two. The corpus states the collapse rule as doctrine in two places: `faction.py:88-89` *"a multi-claimant field reduces to its two leaders"*; `:131-132` *"COALITIONS pool onto the two-party engine — the multi-faction case needs no N-party spine."*

**(b) Reachable / (c) load-bearing.** Every bout. Nothing N-ary is reachable because nothing N-ary exists; `11_` §3 row 4 says "architecturally blocked at the `Bout`" and I concur, with the site count above as the cost.

**(d) Presupposes.** That every deliberative situation is either two-sided or reducible to two coalitions with no loss. The parliament reduces (pro/anti/abstain, `parliamentary_vote.py:146`); a three-way treaty does not (a side deal between two excludes the third; `treaty.py:62 TreatyRecord(parties, terms, …)` already takes a list, so the *record* is N-ary while the *contest* is not).

**(e) Is non-zero-sum expressible at all?** **Yes in the state, no in the terminal — executed.** The accumulators are independent and both can rise (**S5**: corr +0.023 / +0.023 / +0.003 on three proceedings; both sides above the median winner's persuasion in 9–10 % of bouts). `11_` §3 row 4 found the same one level up (two `GraceThreshold`s on one state can both pass). Every shipped terminal then projects the pair onto a winner or a difference: `TallyAtClose` compares (`:65-66`), `PersuasionTrack` subtracts (`:87`), `VoteAtClose` reads the gap (`:126`). **M2** is the clean version: under the mutual reading 96.5 % of negotiations are *both moved past a floor* — a deal — and `TallyAtClose` calls 59.3 % of them a win for A. The kernel has a non-zero-sum state and only zero-sum readers. Side effects are already non-zero-sum with no reader at all: both Standings can rise (`:336-337`), both Rooms (`:338-339`).

**What breaks at N > 2, precisely.** `other()` has no meaning; `Pressure.toward` cannot name a third; `PersuasionTrack.track` has no third pole; the clinch awards `other(loser)` (`:461`) — with three parties, a clinch against one has no single winner; `DefeatCatalogue.check` returns the first faulting side in `(A, B)` order; `_view.leading` is a two-way comparison; `resolve(polA, polB)` takes two policies. **None of it is hard; all of it is everywhere.**

---

## §7 · THE SYNTHESIS QUESTION — is `roles` the master axis?

### §7.1 The attack, and what survives it

**The hypothesis:** *who decides* determines track count, determines what "audience" means, determines whether a verdict is a winner or an overlap — and `roles` is the one declared field that carries it, load-bearing on nothing.

**Attack 1 — `roles` does not carry "who decides."** Its six values are a turn-structure vocabulary (`v30:391`) with decider identity leaking into two of them via canon `:179` (§1(a)). `symmetric` and `alternating` are the same topology (a third party rules, both argue) with a rotation bit; `initiator_proposes` / `appealer_proposes` are burden/turn labels under the dummy; `crown_objects` / `inquisitor_proposes` name a decider the code does not instantiate. The enum partitions neither axis. Making it load-bearing as it stands (`01_SPINE.md` A7) binds one bit for a bout that contradicts the bit (S8; `03_INQUIRY.md:176-178`). **The field is not the axis. Attack succeeds against the field.**

**Attack 2 — "who decides" is not a scalar on the proceeding; it is a function of the side.** In Royal Audience the petitioner's moves land on the Crown and the Crown's moves land on nobody (they are resistance). In a negotiation A's land on B and B's on A. Before a judge both land on the judge. In a body both land on every member. So the axis is `decider(side) → positions`, and a proceeding-level enum cannot express the one-party-decides case without a second field saying which side. **Attack succeeds against "one field."**

**Attack 3 — burden, audience and depth are orthogonal to the decider.** `ProofBar` (`resolver.py:67-73`) puts the burden on one side *before a third-party judge* — burden ≠ decider. `Pressure` presses on whichever position exists (§3) — audience ≠ decider; `Room` is a track that is no decider's (§2). And the parliament shows that the same decider set (N members) yields N *start positions* at depth 0 and N *tracks* at depth k (§2 break 1). **Attack succeeds against "master": at least three other axes do not derive from it.**

**What survives:** the **concept**. Replace the field with the function and re-run the six lenses:

| `decider(side)` | tracks (§2) | audience means (§3) | verdict is (§5) | arity (§6) |
|---|---|---|---|---|
| both → one third party J | J's position | pressure on J: bias, and leak (office → person) | a band on J's position; burden picks the stall winner | 2 sides, 1 decider |
| A → B, B → A (mutual) | each party's position | bias on a party; leak is identity (no office) | the **overlap** of the two positions against each side's floor (ZOPA) — M2 | N positions, deals as overlaps |
| A → B, B → ∅ (opponent rules) | B's position only; A's moves push it, B's `discipline`/`hostile` resist it (`contract.py:28-33` already carry both) | pressure on B, including leak (the king swayed as a person) | a band on B's position; "halved for petitioner" is B's resistance halved | 2 sides, 1 decider who is a side |
| both → every member M₁…Mₙ (body) | N positions (S7) | pressure on members; `toward` names a position | an aggregation over N positions, then a band; abstention is a member with no side | N members who may also be sides |

Every column is either what the code already does (row 1), or a one-line change to *which object `_advance` reads* (rows 2–3: `self.adj` → `decider(side)`, `resolver.py:323-326`, `:376`, `:280`), or S7's per-member accumulation (row 4). **The decider function is a master axis for L1, L2, L3, L5's shape and L6's positions.** It is not the master axis for L4 (subject) or for burden or depth. **There are two axes underneath this engine, not one: who decides (topology × depth) and what is decided (topics × stases). `roles` gestures at the first and carries neither.**

**Against the sibling's line — "the issue is the unit."** `11_` §3 concludes the rebuild's central move is the issue fold. The fold is L4/L5: it gives per-topic verdicts and conditions. It does not touch who rules, so it leaves the dummy deciding negotiations (S2), the Crown accumulating before its own judge (§1(e)), the bench averaged into one mind (S7), and the terminals zero-sum (M2). Conversely the decider function without the fold leaves one matter per bout. Neither is the unit; the unit is a **position on a topic** — `adv[topic][position]` — and both axes are needed to index it. Jordan's distrust of the "issue is the unit" line is warranted in exactly this sense: it is half.

### §7.2 The parliament as the test case (the coordinator's four questions)

**Re-checked, all five cites hold:** `parliamentary_vote.py:196` (`track = max(0, min(10, start + (movement_a − movement_b)))`), `:200-205` (`passed`/`committee`/`failed`), `:208` (`total_victory` at 9/1), `:45-51` (imports the five `PERSUASION_*` constants from the contest package — which re-exports them from `contest_legacy_stub.py:67-71`, `contest/__init__.py:35-50`), `:110`/`:149-151`/`:153-158` (abstainers and their resistance), `:57-66` (the Venetian *non sinceri* precedent).

**Q2 first — one mechanism or two? One, executed.** **S6:** 3,000 seeded votes over a duck-typed world; for each, `PersuasionTrack(scale=1.0, start=starting_track).resolve` on a `ContestState` whose `adv` is `(movement_a, movement_b)` reproduces `status` and `total_victory` in **3,000/3,000**. `run_parliamentary_vote` is `PersuasionTrack` over a **one-exchange bout** whose reception is `roll_pool(Mandate + bonuses) − resistance` floored at 0 (`:166-179`, `:185-186`) — the kernel's `_reception → _advance` with readiness, resonance, jitter and the σ-leverage stripped out, and two `+1D`s that are CR4's shape (`:172-175` vs `resolver.py:402-404`). So: **a `WinCondition` that escaped the family, plus a degenerate reception rule.** Not a different procedure. What it has that the kernel lacks is not procedure but **inputs**: N declared positions, eligibility (GD-3, `:141`), a cross-scene start (`:160-163`), and abstention.

**The `committee` count, verified against `10_` §4 D14.** Four sites, and the honest count is **two rules, one inert special case, two implementations**: the track band `3 < t < 7` (`resolver.py:93` on a float; `parliamentary_vote.py:204-205` on an int — same rule, two homes); the zero-zero branch (`:189-193`) — **inert under ED-621**, since it sets `final_track = start` and `start ∈ [4, 6]` (`:162`) is inside the committee band already (S6: committee at 4, 5, 6); and `faction.band_of` (`faction.py:68-74`), a genuinely different rule on a vote share ± 0.06. D14's "three unrelated rules" counted the inert branch as a rule; it is a special case of the band that cannot disagree with it.

**Q1 — does the parliament fall out of `roles`? No. Does it fall out of the decider function? Yes, with the two riders §2 found.** Under `roles` the parliament is `alternating` (Formal Contest, `modes.py:487`) — a turn-structure word that says nothing about N members voting. Under `decider(side)` it is row 4 of §7.1's table: every member is a position; the two arguing coalitions push every position; the verdict aggregates positions then bands. It needs **depth** (at depth 0 the positions are declarations and the "debate" is prior seasons — `lobbying_offset`; at depth k they move, S7) and it needs the **fold** (per clause, §4). Amendments are inter-topic conditions (§4). Factions as members are N > 2 by declaration and 2 by coalition (`:146`) — the collapse `faction.py:131` asserts, which is right for a *division* and wrong for a *debate*. **The parliament is evidence for the decider function and against the field, and it is the strongest evidence that depth is a rider on topology: the same N positions are inputs at one fidelity and tracks at another.**

**Q3 — abstention: what it costs, and whether it is `draw`.** It is **not** `draw`. `draw` is an aggregate outcome (a tied bench); abstention is a **member position** — neither side. They are related in one direction only: abstention is what makes `draw` reachable at an odd bench (§5; **S6(d)**: a scratchpad `VoteAtClose` with a per-juror dead zone `|k·gap + noise| < ε` at n = 5 gives draw 3.5 % / 4.5 % / 8.0 % at ε = 0.3 / 0.6 / 1.0, from 0 %). Cost to bring it in: **(i)** a third ballot value per member — one dead-zone `[SEED]` on `VoteAtClose`, or at played fidelity a member's chosen act (ED-SC-0013's duality already says the auto arm samples what the played arm chooses; the parliament's declaration *is* the chosen form, `:136-146`); **(ii)** `n_effective = n − abstainers` in the aggregation (`:143`); **(iii)** its resistance effect — the parliament subtracts per side with a floor (`:185-186`), `faction.py:141` damps the scale, canon subtracts from the margin (`v30:187`): pick **one** owner (§8 gives the default). And a unification falls out that costs nothing: **a per-member abstention is a per-member committee band** — the same dead zone, at the member instead of the aggregate. The middle band and the abstaining member are one object at two scales, which is why `committee` is the token both implementations share.

**Q4** honoured: `parliamentary_bridge.py` and every other seam untouched and uncited except as the inherited provenance of one number.

---

## §8 · FOR OPUS 5 — the engine's assumed shape, stated so the design can be written from it

### §8.1 What is now known (each line has an executed or read anchor above)

1. **The kernel assumes: two sides, one third-party decider with a taste, one matter at one stasis, one difference banded or balloted.** Everything Jordan asked for is a violation of one of those four.
2. **The resolution atom is right and should not be rebuilt** (`10_` §2.14, concurred): pure, seed-reproducible, single-owner ladder with a structural veto-only extension, venue-configured faults. What is wrong is **which object each step reads** and **what the terminal keeps**.
3. **Two axes, not one.** `decider(side) → positions` (topology, with depth as a rider) and `topic × stasis` (subject). The unit of state is a **position on a topic**: `adv[topic][position]`, where a *position* is a hearer (judge, member, or counterparty). `roles` carries neither and should be deleted or redefined, not made load-bearing (§7.1 attack 1; `01_SPINE.md` A7 should not land as written).
4. **The two accumulators already are the mutual case's two tracks**; the terminal discards them (M2, S5). **Per-member tracks are computable from the existing atoms with no new primitive** (S7: `res` per member, one roll shared). **The cross-scene position already has a carrier** (`PersuasionTrack.start`; `lobbying_offset`).
5. **Audience has two meanings and only one generalises.** Bias (a multiplier on a position's movement toward a favoured side) works in every topology. Leak (office → person) exists only where a position-holder has an office distinct from their taste — a judge, a Crown, a member with a party line — and is inert wherever discipline is low (S3). `Room` is an audience track, not a decider track, and feeds only readiness.
6. **The ladder is a concession chain, not a verdict partition** (S4). Conditions live in two homes: intra-topic (the ladder, declared, unrecorded) and inter-topic (terms on the deal, undeclared).
7. **`draw` is dead vocabulary until members can abstain**; **abstention is the member-scale committee band** (§7.2 Q3).
8. **Texture is a function of independent inputs per banded thing** (S4); the mechanism that makes per-topic bands texture in a played contest is a shared budget spent across topics.
9. **The parliament is the kernel at depth 0 with N declared positions** (S6); one mechanism, three implementations (`PersuasionTrack`, `coalition_vote`, `run_parliamentary_vote`) that disagree only on resistance.

### §8.2 The shape to write from (paper; every name is a proposal)

```
Position      := a hearer whose stance on a topic moves — a Judge, a Member, or a Party-as-hearer
                 carries: taste (ethos/pathos/logos), discipline, learned/hostile, office? (role weights) — contract.Adjudicator already has all but `office?`
Topology      := decider(side) -> set[Position]       # not a proceeding enum; a per-side function, from the venue row
                 THIRD:  {A: {J}, B: {J}}   MUTUAL: {A: {B}, B: {A}}   OPPONENT: {A: {B}, B: {}}   BODY: {A: M, B: M}
Depth         := 0 (positions are starts; one reception per side — the parliament)  |  k exchanges (positions move — the Bout)
Subject       := list[Topic]; each Topic has its own live stasis and its own adv[position]; one Reserve shared across topics
State         := adv[topic][position], Standing[side], Room[side], Reserve[side], live[topic], faults[side]
Reception     := as today (resolver.py:283-308), once per move; res computed per position in decider(side) (S7)
Terminal      := per topic: THIRD -> band(J's position, burden picks the stall winner)
                            MUTUAL -> overlap(A's position vs B's floor, B's position vs A's floor) -> deal | no-deal, with terms as constraints across topics
                            OPPONENT -> band(B's position); B's moves are resistance (Ob / discipline), never an accumulator
                            BODY -> aggregate(positions, abstain dead-zone) -> band; draw is the tied aggregate
Audience      := Pressure.toward names a Position, not a side; bias applies to that position's movement; leak applies iff the position has an office
Record        := the verdict vector (per topic) + terms; a seam concern, not the kernel's
```

What each row of today's `PROCEEDINGS` becomes: `formal/grand_contest` → BODY(crowd members), depth 3/5; `guild_arbitration` → BODY(masters), depth 3, ballot with abstention; `royal_audience` → OPPONENT(Crown), depth 3; `church_tribunal` → OPPONENT(Inquisitor) at FACT with burden on the inquisitor **— see J1**; `private_negotiation` → MUTUAL, depth 1–3, overlap terminal (this is `settle()`, and it needs no new function beyond the overlap read — M2); `casual_dispute`/`personal_appeal` → MUTUAL at depth 1; the §10 parliament → BODY(factions' members) at depth 0, positions from declarations, resistance from abstainers.

### §8.3 The decisions, through the five-test ladder (`CLAUDE.md` §0 amendment 2026-08-24)

Closed by the ladder — cite, do not re-surface:

| question | closed by | disposition |
|---|---|---|
| Is negotiation's decider the counterparty (delete the dummy)? | test 3 — canon §2 Step 1 *"the parties themselves decide"*, §3 *"you must read the other party"* (`modes.py:429`); test 4 — `faction.py:37-39 _adj(f)` already builds an Adjudicator view **from a party's disposition**; test 5 — S2/M1 | **MUTUAL. Not Jordan.** Cost: a `Contestant` must carry a hearer view (taste, discipline) — `_adj` is the precedent |
| Per-topic verdicts, shared budget vs independent bouts? | test 5 — S4: independent bouts under shared inputs are noise; Jordan's observations 2–3 already ask for the vector | **one bout, k topics, one Reserve. Not Jordan** |
| Where do conditions live? | test 4 — CIP-5's declared compromise axes; `TreatyRecord.terms`; `00` §2.3's cut of `offer` moves | **terms on the deal, declared at open, evaluated at close. Not Jordan** |
| Abstention chosen or sampled? | test 1/3 — ED-SC-0013 duality (resolved): played arm chooses, auto arm samples; the parliament's declaration is the chosen form | **both, by fidelity. Not Jordan** |
| Keep `draw` in the vocabulary? | test 4 — the parliament's abstention + *non sinceri* precedent make it reachable | **keep, reachable via abstention. Not Jordan** |
| Which resistance owner? | test 4 — the parliament's per-side floored subtraction is canon §10 verbatim (`:184-186`) and the only one measured (S6: attenuates, not inert); `faction.py:141`'s damp was a fix for a subtraction that cancels, which the floor prevents | **per-side floored subtraction, one owner. Not Jordan** |
| Ballot vs band for a body (ED-1057 vs observation 1)? | test 5 — the ballot's share feeds a band (`00` §2.1); ED-1057's per-juror rule is retained as the count inside | **ballot → margin → band. Not Jordan** |
| N-ary native or coalition-collapsed? | test 3 — Jordan's observation 4 ("more than two sides"); test 4 — `TreatyRecord.parties` is already a list; `faction.py:131`'s collapse is right for a division, wrong for a treaty | **native positions with a two-sided fast path. Not Jordan; the cost is the 16 sites in §6** |
| Crowd: one mind or N? | test 3 — canon §2 Step 1 "collective audience"; test 5 — S7 | **BODY, per-member; homogeneous authoring collapses it to one. Not Jordan** |

**Survives all five — needs Jordan (one):**

**J1 · In Royal Audience and Church Tribunal, who rules?** Canon says both things: the §2 Step 5 table gives both an *Expert Judge* (`v30:103-104`), and `:179` says *"the adjudicator IS the opponent"*; `:391` assigns Proposer/Respondent to the institution. Code gives a third party (`modes.py:494`, `:497`); the armature was designed for the opponent (`armature.py:376-384`); the branch proposal carries both at once (`03_INQUIRY.md:176-178`). The two options are materially different games: **OPPONENT** — the Crown cannot lose an audience, only be moved or not; its objections are resistance; the petitioner's whole game is reading the Crown (Attunement); the Inquisitor decides his own case at FACT with the burden on himself, historically exact — versus **THIRD** — a judge before whom the Crown or Inquisitor can lose, and `roles` is merely who speaks first. Neither is superseded, irrelevant, settled by a document (the document contradicts itself), or settled by precedent (the tree holds both). Architecture prefers OPPONENT (one position instead of two accumulators plus a dead resistance field; it is the row the armature, the halved-resistance mercy and `:179` were all written for) — **default: OPPONENT for both**, with THIRD available as a venue row for a bench tribunal if Jordan wants one. Consequence to accept with the default: the deciding side has **no accumulating moves** — playing the Crown is choosing how to resist (raise the Ob on a stasis, shift the question), not arguing.

### §8.4 Build order that follows from the shape (each with the artifact that makes it DONE, §0.2)

1. **`decider(side)` replaces `self.adj` at the four read sites** (`resolver.py:280`, `:323-326`, `:376`, `:405`), with THIRD as the default so the two campaign goldens do not move. Done when: the goldens are byte-identical and a MUTUAL bout reproduces M1's taste-tracking.
2. **`adv` keyed by position** (S7's `madv`), aggregate = mean for THIRD/crowd so the goldens still hold. Done when: a heterogeneous bench splits (S7's 346/400) through the public API.
3. **Terminals read positions, not a difference**: overlap for MUTUAL (M2), aggregate-with-abstention for BODY (S6(d)), band on the single position for OPPONENT. Done when: a private negotiation can return a deal and `guild_arbitration` can return a draw.
4. **Topics**: `adv[topic][position]`, `live[topic]`, one `Reserve`. Done when: one seeded bout returns a two-topic verdict vector that differs from two independent bouts under an allocating policy.
5. **Delete `roles`** (or redefine it as the turn-order bit it is) and the `no_adjudicator` factory; retire `run_parliamentary_vote`'s body into the depth-0 path of the same kernel, keeping its constants as the single owner.

---

## §9 · ATTACKS THAT FAILED, REPORTED AS FAILED

| attack | how | result |
|---|---|---|
| The brief's 1 v 6 numbers are a tuple-key artefact (the coordinator's first attempt was) | S1, keyed on the bare verdict, both terminals on one state; cross-checked by the two-venue route | **FAILED** — reproduced to the decimal; 0/100 state divergence between routes |
| `VoteAtClose` draws random numbers mid-bout and desynchronises the two-venue comparison | read `:124-125`; S1 two-venue route | **FAILED** — `if not closing: return None` precedes every draw; states identical |
| `draw` is reachable at 5 with the weighted rule because weights are floats | arithmetic on `{0, .75, …, 3.75}` vs `total/2 = 1.875`; S1 bench 5 and 7 | **FAILED** — unreachable; the even benches reach it |
| `opponent_is_adjudicator` gates the whole armature (canon `:179` says "entirely") | S8, four styles, three arms | **FAILED against canon, SUCCEEDED against my reading of the code** — δσ is gated; CR4 and CR5 are not |
| The parliament is a different procedure from the kernel (a genuinely fourth resolver) | S6, 3,000 votes vs `PersuasionTrack` on movement | **FAILED** — 0 mismatches; it is the terminal over a one-roll reception |
| The parliament's resistance is inert at large pools (`faction.py:139`'s claim) | S6 resistance × pool | **FAILED** — attenuated (4.9 → 16.3 % at pool 16), not inert |
| The zero-zero → committee branch is a distinct rule (D14's third rule) | S6(a) at start 4/5/6 | **FAILED** — inert under the ED-621 clamp; it cannot disagree with the band |
| Per-topic bands add texture by themselves | S4 shared-input topics | **FAILED** — noise; texture appeared only with per-topic inputs |
| `Pressure.public` is live on the crowd proceeding | S3 leak table and `formal_contest` outcomes | **FAILED** — saturated at `LEAK_CAP`; 99.5 → 99.6 % committee |
| The stasis ladder partitions the verdict (per-stasis outcomes exist) | S4 log; `resolver.py:335` | **FAILED** — one accumulator; a shift changes relevance, not the tally |
| `roles` has a resolver reader I missed under another name (`role_structure`, `Proceeding`) | grep; `dictionaries.py:503-624` (`_crosscheck_proceedings` at `:607`) | **FAILED** — the typed table reads its own prose dict and the crosscheck never compares `roles` |
| The homogeneous bench is only *nearly* one mind (floating-point spread) | S7 | **FAILED** — spread 0.000, 0/400 splits; exactly one mind |

---

## §10 · WHAT WOULD MAKE THIS INTERROGATION WRONG

1. **The 81.9 % / 4,979 provenance is inherited.** If the seam rebuild changes what reaches the kernel, "the live case" changes with it and every 1 v 6 figure here becomes a hypothetical. The structural claims do not depend on it; the *urgency* does.
2. **S7 and M1/M2 are scratchpad subclasses, not the kernel.** They show N-track and mutual receptions are *computable* from the atoms with the stated changes; they do not show a rebuilt `_advance` would be numerically identical to them. A rebuild should re-run both as its falsifiers.
3. **`decider(side)` is my abstraction.** The evidence is that four topologies need four different read targets at four sites; the evidence is *not* that a single function is the elegant home. If Opus finds the per-side function makes the venue row unreadable, a per-proceeding pair (`decider_a`, `decider_b`) is the same content.
4. **The "two axes" claim could be three.** Burden (`ProofBar`/`GraceThreshold`; ED-SC-0020) is treated here as a terminal parameter under the decider axis. If burden turns out to change *reception* (who must clear an Ob) rather than only the stall rule, it is a third axis and §7.1's table gains a column.
5. **Depth is asserted from two data points** (the parliament at 0, the Bout at k). A middle fidelity — positions that move once per season across a multi-season case (`03_INQUIRY.md`'s S2 loop) — is the case that would test whether "depth" is a scalar or a schedule.
6. **The ladder-is-concession reading rests on `stronger_than` being upward-only.** If Jordan intends the *accuser* to climb (framing up, not retreating), the intra-topic condition inverts and §4's "concession chain" is the wrong word for the same mechanism.
7. **Self-review bias, marked.** §7.1 argues against the sibling's "issue fold" as the master move. A reader should check that I have not under-weighted the fold because the decider function is *my* finding: §7.1's own table shows the fold is necessary for L4/L5, and §8.2 builds it in at step 4 — but a reader who thinks the fold should be step 1 has a defensible order, and nothing measured here decides between the two orders.
8. **Nothing here changes the grade.** Every recommendation is paper until §8.4's artifacts exist.

*End. One file. Nothing else was created or edited.*
