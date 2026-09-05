# 13 · THE PARLIAMENT FOLD, AND THE RECALIBRATION IT MAKES NECESSARY

## Status: **PROPOSED, 2026-09-05. HELD BACK IN FULL — nothing ratifies on merge. Read-only over the tree; this file is the only artifact.** Branch `claude/social-contest-system-review-dn2y5d`, HEAD `8eff87f4`.
## Author: Fable 5.1, `CLAUDE.md` §10 planner/audit node — a specification for **Opus 5 to execute** (§4), not a design essay. Sibling of `11_FOUR_GAMES_AUDIT_AND_PLAN.md` (the 23-item plan this slots into — §3) and `12_STRUCTURAL_INTERROGATION.md` (the six lenses and the `decider(side) → positions` shape this builds on).
## Grade under `CLAUDE.md` §0.2: every number below **executed** (§0.3, scratchpad scripts, no `pytest`, no repo writes); every design statement is **paper** until its §4 artifact runs.

---

## §0 · Scope, method, what was executed and its controls

### §0.1 The two deliverables and why they interlock

Jordan: *"fold the parliament stuff in"* and *"have fable plan the recalibration"*. They are one job. The fold puts N declared **positions** into the kernel (§1); the recalibration is what makes a position's *taste* a **modifier** rather than the verdict (§2). Today an adjudicator's appeal preference multiplies every exchange's gain (`resolver.py:326`, `:334`), so a **mild** lean decides a contest before anyone argues — measured §2.1 — and a bench drawn with mild individual variation is decided in **one draw in three** (§2.7). Jordan's stated goal — *"modifiers for it based upon adjudicators as individuals and audience"* — cannot ship on that channel. So §2 is a **precondition** of the feature §1 folds in, not a polish pass.

### §0.2 Method

Every anchor cited was opened this session (`path:line symbol`); the assertion was checked, not the prose above it. Where a claim is a number it has a script and a line in an output file. **Each sweep states its control** (§0.3), because this session had already produced three measurement errors of one class — arms that could not observe the effect under test — and I made a fourth before catching it (§0.4). Seams (`engine/cross_scale/*`) are cited only as *callers* whose read surface the fold must not break; nothing here prescribes on them.

### §0.3 Execution artifacts (scratchpad; `random.seed(s)` per bout on the kernel's global stream unless stated)

| script | drives | control(s) | headline |
|---|---|---|---|
| `s6_parl.py` | `run_parliamentary_vote` × 3,000 on a duck-typed world (6 factions, random L/Sta/declarations/genres/lobby) vs `PersuasionTrack(scale=1, start)` on `(movement_a, movement_b)`; **a depth-0 prototype `body_vote` built from kernel atoms only**; resistance × pool; the campaign's declaration shape | same `random.Random(s)` handed to both arms | **0/3,000** (S6 re-verified) and **0/3,000** for the prototype on `(status, final_track, total_victory, resistance)` — the fold has a byte-identical path |
| `dose2.py` | preference dose-response, A `logos` v B `demagogue`, `private_negotiation` 4v4, five levels × four transforms × two draws; budget sweep 1/2/3/5/8 | **(i)** every transform's *neutral* arm equals the baseline (0.423, all four); **(ii)** mirrored contestants give the complement (1−mirror within 0.02 at every level); **(iii)** discipline sweep 0.30/0.75/0.90 | the multiplier is unbounded; √ compresses but does not bound; δσ is bounded and a **staircase under the discrete draw** (needs W-G1) |
| `extra.py` | the MUTUAL proxy (discipline 0.10 → leak at `LEAK_CAP` 0.90); logos v the two builders; the disciplined judge; the shipped benches' actual tastes | same three controls | under MUTUAL the counterparty's taste **is** the verdict (mild → 0.80); **every shipped bench already carries a "moderate" preference** (`expert_judge` logos 0.55, `crowd` pathos 0.55) |
| `ethos.py` | the ethos "second channel" decomposed: R-matrix flat; ethos build off; Room build off; `ETHOS_UNLOCK = 0` | `logos` v `logos` = 0.529 on every arm (the side-symmetry control); "no build either" returns to it | the ethos-specific extra is **+0.03** (leak) **+0.08** (R-matrix); the real asymmetry is *logos builds nothing* |
| `readiness.py` | the Readiness dials at a neutral judge on a flat R-matrix, three pure-appeal pairs | `logos` v `logos` = 0.529 on every arm | `FLOOR 0.55, W 0.25/0.25` puts the three pairs at 0.549 / 0.507 / 0.490 on the shipped role weights |
| `faculty.py` | faculty dose-response on the production terminal and the band ladder on the **same** state; `Pool.size`/`net_boost` staircase; the `TRACK_SCALE × MERIT_SCALE` table | same seeds, same state, two readers | 1v6 reproduces `11_` row 3 (0.071 / 0.299); **the two dials are one dial** for the band terminal (product) |
| `bench2.py` | 100 random 5-benches × 200 bouts, per-member reception (12_ S7's shape), three transforms, two aggregations, spread s ∈ {0, .04, .08, .12}; one leaning member on a neutral bench | **s = 0 gives SD 0.000** (homogeneous = one mind); `MemberBout` byte-identical to the kernel `Bout` on the crowd proceeding, **0/500** mismatches; mirror arm | under the multiplier, **33 %** of mildly-varied benches are decided (>70/30) before anyone argues; under δσ, **0 %** |
| `draw.py` | `VoteAtClose` with a per-juror abstention dead zone at n = 5; institutional pressure as today's multiplier vs a start offset under the ED-621 clamp; `private_negotiation` under the multiplier | eps = 0 reproduces 0 % draw; inst = 0 identical across arms | draw reachable at an odd bench from eps > 0; the institutional multiplier moves `grand_contest` 0.11 → 0.81 A-decisive, the clamped offset caps at 0.26 |
| `extra2.py` | the fold's one decision: the parliament's **raw** margin vs the **banded** margin, same 3,000 votes; the raw rule's pool-size dependence | same rng | banding changes 39 % of outcomes and makes total victory unreachable (0.351 → 0.038) — **J-P1, closed raw 2026-09-05 (§1.8.1)** |

### §0.4 The measurement error I made, and the control that caught it

My first `dsigma` arm dropped the office/person blend entirely (`res = venue_w`) instead of moving only the *deviation from neutral* into δσ — so its **neutral** arm read 0.757 against a baseline of 0.423, and its dose-response was measuring the undiluted venue register, not the preference. The control "every transform's neutral arm must equal the baseline" is what exposed it; `dose2.py`/`bench2.py` are the corrected runs and the earlier outputs are not cited. Stated because §0.1 of the brief asked for the controls and because a reader should know this class of error is easy here: the blend `(1−leak)·venue + leak·char` couples the office and the person, and any transform that touches one silently moves the other.

---

## §1 · THE PARLIAMENT FOLD

### §1.1 What the parliament is, re-verified, and what it carries that the kernel lacks

**One mechanism, three implementations.** `run_parliamentary_vote` (`systems/social_contest/sim/parliamentary_vote.py:125-220`) is `PersuasionTrack(scale=1, start)` (`resolver.py:81-95`) over a **one-roll reception per side**: pool = Σ Mandate + two `+1D`s (`:169-175`), `movement = max(0, net − resistance)` (`:185-186`), `track = clamp(start + movement_a − movement_b)` (`:196`), banded at the five `PERSUASION_*` constants it imports from the contest package (`:45-51`, re-exported from `contest_legacy_stub.py:67-71` via `contest/__init__.py:35-50`). **S6 re-run: 0 / 3,000 mismatches** on `status` and `total_victory`. The third implementation, `faction.coalition_vote` (`faction.py:128-148`), is the same terminal over `max(0, roll_net(max(1, pool)))` with resistance as a *scale damp* (`RESIST_DAMP`, `:28`, `:141`) instead of a subtraction, no eligibility, no genre dice, and its own `[4, 6]` clamp (`:142`) — `11_` W-A3 already deletes it and the count below does not re-count it.

**The only structural difference is the reading of the margin.** The kernel's reception bands `net − base_ob` through the one ladder (`resolver.py:307-308` → `dice_engine.degree_from_net`, `dice_engine.py:227-281`, `margin = net - ob` at `:279`) and accumulates a *degree* (0–3, `:407-408`); the parliament accumulates the *margin itself*, unbanded (`:185`), against `base_ob = resistance`. Everything else the kernel does per exchange — readiness, resonance, jitter, σ-leverage, policies, the exchange loop — the parliament has none of, which is what **depth 0** means (`12_` §2 break 1, §7.2 Q2): the positions are *inputs*, not movers.

**The two things the kernel lacks and the fold must not lose:**

- **Abstention.** `parliamentary_vote.py:149-151` (eligible, undeclared → abstainer), `:153-158` (*+1 resistance per Stability ≥ 6 abstainer, cap +2*), `:57-66` (the *non sinceri* precedent: a high-Stability abstainer forces redrafting rather than decision). **It is live on the campaign path**: `engine/cross_scale/parliamentary_bridge.py:105-106` declares exactly two factions and leaves the rest to abstain, and `s6_parl.py` shows abstainers at Sta ≥ 6 supply resistance 2. Its effect is **attenuated, not inert** — P(committee) at equal pools, resistance 0/1/2: pool 2 → 0.625 / 0.768 / 0.917; pool 8 → 0.344 / 0.370 / 0.436; pool 16 → 0.273 / 0.274 / 0.283 (`faction.py:139`'s "went inert" overstates; `12_` §3 concurs). And it is **not `draw`** (`12_` §7.2 Q3, upheld here): it is a *member position* whose aggregate effect is the middle band. The kernel has no member position at all — `Panel` averages its members into one mind (`contract.py:47-51`) and `VoteAtClose` forces every juror to a side (`resolver.py:139`, `:144`), which is why `draw` is unreachable on every odd bench (`11_` §1.2 row 2).

- **Institutional pressure.** `Pressure.institutional` (`contract.py:70-77`, *"a thumb on the scale (Crown/Church/party leaning on the verdict)"*) enters the kernel as a per-exchange multiplier on the favoured side's every gain (`resolver.py:310-312 _bias`, `INST_BIAS = 0.6` at `:42`). **The parliament already carries the same concept under its canonical name**: `Motion.lobbying_offset` (`parliamentary_vote.py:85`), *"+1 toward lobbying side per successful Diplomacy action (max ±2)"*, entering as a **start-position offset** clamped to `[4, 6]` by ED-621 (`:160-163`; canon `social_contest_v30.md:599`, *"Lobbying cannot predetermine a vote — it provides advantage, not a guaranteed outcome"*). Two homes for one thing, and only the parliament's is bounded by canon. On the campaign path the bridge passes `lobbying_offset=0` (`parliamentary_bridge.py:104`), so the field has a referent and no producer yet.

### §1.2 Target shape — a ninth proceeding row and a depth-0 entry point beside `Bout`

**The parliament becomes a row of `PROCEEDINGS` (`modes.py:485-519`) resolved by a depth-0 function, not a terminal and not a topology class.** Under `12_` §8.2 it is `BODY(factions' members)` at depth 0: positions are declarations, the two arguing coalitions receive once each, the terminal is the band. The kernel object that *runs a proceeding* is `Bout.resolve` (`resolver.py:440-466`: budget × sides × policy); at depth 0 there is no budget and no policy, so the row cannot be run by `Bout` — it is run by a sibling entry point that shares every atom `Bout` shares: `ContestState`, `PersuasionTrack`, the band constants (`11_` W-A2), `dice_engine.roll_pool`, and `ContestOutcome` (`11_` W-C1).

```python
# modes.py — the NINTH row. exchanges=(0,0) IS the depth: no exchanges, one reception per side.
"parliamentary_vote": dict(      # social_contest_v30 §10 (:589-613); 12_ §8.2 BODY at depth 0
    exchanges=(0, 0),            # depth 0 — resolve_body, not Bout
    roles="symmetric",           # kept only for _crosscheck_proceedings; 12_ §8.4 step 5 deletes the field
    resistance="abstention",     # §10 step 3: +1 per Stability>=6 abstainer, cap +2 — the ADAPTER derives it
    adjudicator=None,            # BODY: the declared positions are the deciders; no third party is minted
    track_start=TRACK_START, tracker=True, tracker_mode="required",
    scale=1.0,                   # §10: "net track movement = difference" — the RAW margin (J-P1 closed raw, §1.8.1)
),

# resolver.py — the depth-0 entry point, beside Bout. Shares ContestState / PersuasionTrack / ContestOutcome.
def resolve_body(pools: dict, base_ob: float, venue, rng=None) -> "ContestOutcome":
    """BODY topology at depth 0 (12_ §8.2 row 4; social_contest_v30 §10). Each side receives ONCE:
       pool = the side's declared weight (the adapter sums Mandate and adds the §10 genre dice);
       base_ob = the abstention resistance (the adapter counts it);
       adv[side] = max(0, net - base_ob)  — the RAW margin (canon §10 verbatim; J-P1 closed raw
       2026-09-05, §1.8.1 — and THIS docstring is where the depth reasoning must be written). Draws exactly as run_parliamentary_vote did: dice_engine.roll_pool(pool, 7, rng) for
       side A then side B, so the campaign goldens do not move. The venue's terminal reads the state."""
    s = ContestState()
    for side in (A, B):
        pool = int(pools.get(side, 0))
        s.adv[side] = 0.0 if pool <= 0 else max(0.0, roll_pool(pool_size=pool, tn=7, rng=rng).net - base_ob)
    return venue.win.outcome(s, adj=None, reason="win")
```

`run_parliamentary_vote(motion, parties, world, rng)` **survives as the adapter** (the parliament's `build_contest`): GD-3 eligibility (`:141`; `canon/02_canon_constraints.md:40`), abstainer derivation (`:149-151`), the resistance count (`:153-158`), the ED-621 start (`:160-163` → `track_start_of`, §1.7), the pools with the §10 genre/audience dice (`:166-175`) — then `resolve_body(...)` — then the **Total-Victory Mandate write** (`:208-219`) and a `VoteResult` view of the `ContestOutcome` (§1.6). Its 55-line resolution body (`:176-206`) is deleted. `parliamentary_stay.py` (zero callers, `11_` §1.3) keeps calling the adapter unchanged.

**A correction `11_` W-C1 needs before this row can use it.** W-C1's `WinCondition.outcome()` bands `degree_of_margin(self.margin(s))` = `band_of_track(track_of(margin))` with the **default** start and scale (`11_:566-575`). The parliament's terminal is `PersuasionTrack(scale=1.0, start=track_start_of(lobby))` — a lobbied start of 4 or 6 and scale 1 — so `PersuasionTrack.outcome()` must band **`self.track(s)`** (its own start and scale), never `track_of(margin)` with the module defaults. Otherwise the lobbying offset is lost in the degree and the fold is not byte-identical. One line in W-C1; §4 item F-1 carries it.

### §1.3 What dies, what survives

| object | today | after the fold | why |
|---|---|---|---|
| `PersuasionTrack` (`resolver.py:81-95`) | the kernel's band terminal | **survives** as the single owner of the band (via W-A2) | it is the mechanism (S6: 0/3,000) |
| `run_parliamentary_vote` resolution body (`:166-206`) | the second implementation | **deleted**; the function stays as the adapter | the body is `PersuasionTrack` over one roll |
| the zero-zero branch (`:188-193`) | "both fail to exceed resistance → committee" | **deleted** | inert under ED-621 — `start ∈ [4,6]` is already `committee` (`12_` §7.2; measured: 223/3,000 zero-zero votes, every one already banded `committee` by the track) |
| `_TRACK_FLOOR`, `_TRACK_CEIL` (`:74`) | a self-flagged `[ASSUMPTION]` copy of the 0–10 clamp | **deleted** (D4 closed; `resolver.track_of` clamps) | one clamp, one home |
| `BG_VOTE_TN = 7` (`:54`) | a per-module TN | **deleted** | `dice_engine._require_tn7` (`dice_engine.py:199`) — TN 7 is the only TN (ED-IN-0196) |
| `VoteResult.movement_a/_b`, `side_a/b_net`, `side_a/b_pool`, `rolls_a/b` (`:102-113`) | eight diagnostic fields | **deleted**; the two receptions become two `ContestOutcome.beats` | one legibility carrier (W-C1's `beats`) |
| `faction.coalition_vote`/`coalition_rate`/`band_of`/`rate_banded`/`RESIST_DAMP` | the third implementation | deleted by **`11_` W-A3** (not re-counted here) | — |
| `Motion`, `VoteDeclaration` (`:79-93`) | the parliament's inputs | **survive unchanged** (`references/module_contracts.yaml:93-101` names them) | inputs, not mechanism |
| `BG_VOTE_ABSTAIN_*`, `BG_VOTE_RESISTANCE_MAX`, `BG_VOTE_GENRE_BONUS`, `BG_VOTE_AUDIENCE_BONUS`, `BG_VOTE_TOTAL_VICTORY_MANDATE_DELTA`, `GENRES` (`:55-76`) | canon §10's cited constants | **survive in the adapter** | they shape inputs and the one write; every one cites §10 |
| `BG_VOTE_LOBBY_OFFSET_MAX/START_MIN/START_MAX` (`:70-72`) | the ED-621 clamp, one of two homes (D3) | **relocate to `resolver.py`** under `track_start_of` (§1.7); same names | the clamp becomes one owner used by depth 0 and, after §2.6, by depth k |
| `Contest.resistance` (`wrapper.py:75-79`) | metadata, "NOT plumbed into resolution" (F10) | **becomes `Venue.base_ob`'s increment at build** — the one owner of resistance; at depth 0 it *is* `base_ob` | 12_ §7.2 Q3(iii): pick one owner; the parliament's subtraction is canon §10 verbatim and the only one measured |
| `parliamentary_stay.py` | built, uncalled | untouched | calls the adapter |

### §1.4 Abstention enters as a member position — one object at two depths

- **Depth 0 (the parliament).** A position is `(member, stance ∈ {A, B, abstain}, weight)`. Today abstention is *implicit* (eligible-and-undeclared, `:149-151`); the adapter keeps deriving it that way (the three callers declare only the sides — `parliamentary_action.py:123-124` says so in its own comment) **and** accepts `VoteDeclaration(side="abstain")` as the explicit form, because a *chosen* abstention is exactly what ED-SC-0013's played arm produces (`12_` §8.3 row 4: chosen at played fidelity, sampled at auto). Its mechanical effect is unchanged and byte-identical: a high-Stability abstainer raises **`base_ob`** for both active sides (`:153-158` → `resolve_body(base_ob=…)`). **Resistance is the Ob of the depth-0 reception** — which is what unifies the three resistance homes `12_` §3 found: the parliament's floored subtraction (kept), `RESIST_DAMP`'s scale damp (deleted by W-A3), and `_derive_resistance`'s Stability formula (`wrapper.py:43-56`, kept as the *personal* proceedings' derivation of the same `base_ob` increment, §2.6).

- **Depth k (a bench that hears).** A member position that is *neither* side is a per-juror dead zone on the ballot: `VoteAtClose(abstain_dead_zone=ε)` — a juror whose `k·gap + noise` falls inside `±ε` casts no ballot, and `n_effective = n − abstainers`. **Measured (`draw.py`, `guild_arbitration` 4v4, n = 5, 2,000 seeds):** ε = 0 → draw 0.000 (today); 0.3 → **0.127**; 0.6 → 0.159; 1.0 → 0.270; 1.5 → 0.587. (`12_` S6(d) measured 3.5 % at ε = 0.3 on 1v6 gaps; both hold — draw reachability via abstention falls with the room's gap, as it should.) Default `ε = 0.0` is byte-identical on the production bench; the value is Jordan's (§2.5) and flips in phase G.

- **Why it is one object.** At both depths an abstainer makes the *middle* outcome likelier and never a side: at depth 0 by raising the bar the sides must clear (P(committee) rises, table above); at depth k by withholding a ballot (P(draw) rises). `12_` §7.2 Q3's line — *a per-member abstention is a per-member committee band* — is what the code now says in one word, `abstain`, and one ε. **Nothing is added at depth 0** (the rule exists, cited to §10); **one `[SEED]` is added at depth k**, and its N-line is stated so it can be cut: *cut ε and `draw` is a declared outcome no shipped bench can reach* (`11_` §1.2 row 2, R-COMPLETE).

### §1.5 Institutional pressure attaches where the parliament already has it — the start

At depth 0, `Pressure(toward=X, institutional=p)` **is** the lobbying offset: it enters as `start = track_start_of(offset)` under the ED-621 clamp and nowhere else — there are no exchanges to multiply. The adapter keeps taking `Motion.lobbying_offset` (an integer count of Diplomacy actions, canon's unit) so the three callers are untouched. At depth k the kernel today applies `_bias` per exchange; §2.6 measures the two forms side by side and proposes the start offset as the one home for both depths — the recalibration half of this item, phase G because it moves goldens. **What the fold itself does is only declare the mapping:** `institutional` at depth 0 = the start offset, with ED-621's bound. `Pressure.public` (the crowd) has no depth-0 referent in canon §10 beyond the "audience boost" `+1D` (`:174-175`), which the adapter keeps as a pool die; §2.6 says what it becomes at depth k.

### §1.6 The callers, and the deletion date of the `VoteResult` view

Three production callers resolve the role by string (`references/module_contracts.yaml:93-101`): `engine/cross_scale/parliamentary_bridge.py:170` (seam — reads `vr.status`, `vr.total_victory`, `vr.final_track`, `vr.mandate_penalty`, `:127-131`, `:190-192`), `systems/factions/sim/parliamentary_transfer.py:317` (reads `vote.status`, `:319-320`), `systems/factions/sim/parliamentary_action.py:137` (reads `result.status`, `:170`, `:175`). One sibling imports it by name (`parliamentary_stay.py:34`, `:85`, reads `vote.status`). Tests: `engine/tests/test_parliamentary_action.py:145-224` pins seeds 5/1/0/9 → passed/TV-passed/committee/failed and the **−2 Mandate stack on a TV pass** (`:167-200`; the open ED-SC-0015 is this stack); `test_parliamentary_bridge.py:286-370` constructs `VoteResult(status, final_track, total_victory)` directly and sweeps `_winner_and_degree` over 22 reachable triples.

**So the adapter returns a `VoteResult` built from the `ContestOutcome`** — `status` from `band` (`A_total`/`A_decisive` → `passed`, `committee`, `B_*` → `failed`; S6 proved this map is the identity), `final_track = int(track)`, `total_victory = degree is OVERWHELMING`, `starting_track`, `resistance`, `abstainers`, `ineligible`, `mandate_penalty`, `notes` — **value-identical**, and every caller and test above keeps working. The view carries a deletion date, the same one `11_` W-C1 gives `winner`/`band`: **the commit in which the rebuilt seam reads `ContestOutcome`.** The TV Mandate write (`:208-219`) stays in the adapter until then for the same reason (PR #362 §A.2 forbids a kernel write; `11_` §6 last row leaves it to the seam rebuild; `test_parliamentary_action.py:167-200` pins it today).

### §1.7 Vocabulary delta — incremental to `11_` §5.7's −14

`11_` already deletes `coalition_vote`, `coalition_rate`, `band_of`, `rate_banded`, `CONCENTRATION_MULTIPLIER`, `PERSUASION_TRACK_START_DEFAULT`, `CANONICAL_TRACK_START` and the legacy stub, and adds `track_of`, `band_of_track`, `ContestOutcome`, `WinCondition.outcome`. Counting only what **this** document adds on top:

**Deleted (16):** `parliamentary_vote._resolve` (inner), the zero-zero branch, `_TRACK_FLOOR`, `_TRACK_CEIL`, `BG_VOTE_TN`, `VoteResult.movement_a`, `.movement_b`, `.side_a_net`, `.side_b_net`, `.side_a_pool`, `.side_b_pool`, `.rolls_a`, `.rolls_b` (13, the fold); `INST_BIAS`, `PUB_BIAS`, `Bout._bias` (§2.6, phase G — 3; `Pressure.institutional` stays as the *name* of the start offset, so it is not counted).

**Added (6):** `resolve_body`; the stance value `"abstain"`; `VoteAtClose.abstain_dead_zone` `[SEED]`; `track_start_of(offset)` (the single owner of the ED-621 clamp, replacing `parliamentary_vote.py:161-162`; `faction.py:142` dies with W-A3); `PREF_DSIGMA_MAX` `[SEED]` (§2.1, phase G); `PUBLIC_DSIGMA_MAX` `[SEED]` (§2.6, phase G). The ninth `PROCEEDINGS` key is a row, not a name.

**Net −10 on top of `11_`'s −14.** The NERS meta-rule (`skills/valoria-resolution-diagnostic/SKILL.md:751`, *a fix that adds a system has failed*) is satisfied by deletion, and the largest single move is the removal of a resolver.

### §1.8 The decisions, through the five-test ladder (`CLAUDE.md` §0, amended 2026-08-24)

| question | rung | disposition |
|---|---|---|
| row or terminal or topology class? | 4 — the eight rows are the precedent (`modes.py:485-519`); `12_` §8.2 maps the parliament to BODY/depth 0 | **a row, resolved by a depth-0 entry point. Not Jordan.** |
| which implementation survives? | 5 — S6 (0/3,000) shows the terminal is the mechanism; `coalition_vote` has zero callers (`11_` §1.3) | **`PersuasionTrack`; the module becomes the adapter. Not Jordan.** |
| abstention: chosen or sampled? | 1 — ED-SC-0013 (resolved) | **both, by fidelity. Not Jordan** (`12_` §8.3) |
| resistance owner? | 4 — the parliament's subtraction is canon §10 verbatim and the only measured one | **`Venue.base_ob`; subtraction. Not Jordan** (`12_` §8.3) |
| institutional pressure at depth 0? | 3 — canon §10 step 4 + ED-621 already define it as the start offset | **the start offset. Not Jordan** |
| keep the `VoteResult` view? | 4 — W-C1's `winner`/`band` precedent: legibility fields with a deletion date | **keep until the seam reads `ContestOutcome`. Not Jordan** |
| where does the TV Mandate write live? | 4 — PR #362 §A.2, `11_` §6 last row | **the adapter now, the calling verb after the seam rebuild. Not Jordan** (ED-SC-0015's stack is the seam's to resolve then) |

**Survives all five — needs Jordan (one):**

**J-P1 · Does the parliament's track move by the RAW margin or the BANDED degree?** Canon §10 says raw (*"movement = successes − resistance … net track movement = difference"*, `social_contest_v30.md:606-607`); the 2026-08-14 ruling says every scale reads **one** ladder (`dice_engine.py:227-229`), and `parliamentary_vote.py:185` is a second reading of `net − ob` beside `degree_from_net` — an S defect (*two ladders for one quantity*, §0.06). The ruling is newer than §10; §0.05 says the code is the mechanism and canon is reference; neither rung 1–4 settles it because **the two options are materially different games — executed (`extra2.py`, the same 3,000 votes):**

| reading | passed / committee / failed | total victory | equal pools 2 / 8 / 20: P(TV) |
|---|---|---|---|
| **raw** (today) | 0.412 / 0.342 / 0.246 | **0.351** | 0.038 / 0.287 / **0.497** |
| **banded** (one ladder) | 0.193 / 0.692 / 0.115 | **0.038** | — |

Banding changes **39 %** of outcomes, makes the chamber referral-dominant, and makes total victory unreachable without a lobbied start (each side's movement is ≤ 3, so |A − B| ≤ 3 < 4). The raw rule has its own property to weigh: **decisiveness scales with pool size** — big coalitions produce a total victory half the time (0.497 at pool 20), a flat-shift trap of the kind `SKILL.md` §11 names. Architecture prefers **raw** — byte-identical, canon verbatim, and the kernel already has one unbanded magnitude entering `adv` (evidence, `resolver.py:364-365`, readiness-free and capped) — so the **default is raw, declared on the row as `scale=1.0` with this citation**, and banded is a one-line switch (`resolve_body` calls `DEGREE_ORDINAL[degree_from_net(net, base_ob)]`) that lands only in phase G with the re-pin. If Jordan picks banded, the raw rule's pool-size trap goes with it and TV needs lobbying, which may be the intended reading of *"lobbying provides advantage"*.

#### §1.8.1 · **DISPOSITION 2026-09-05 — the consequences, laid out, and RAW recorded as the default**

**Jordan was asked to rule and said, correctly, that the consequences were not in front of him.** They
are below. The row is **closed at rung 3 — answered by a design requirement Jordan stated this session**
— not escalated. It stays reopenable on the one condition named at the end.

**The two readings are not "more texture vs less". They are two different shapes of chamber.**

| | passed | committee | failed | total victory | P(TV) at equal pools 2 / 8 / 20 |
|---|---|---|---|---|---|
| **raw** (today, canon §10) | 0.412 | 0.342 | 0.246 | **0.351** | 0.038 / 0.287 / 0.497 |
| **banded** (one ladder) | 0.193 | **0.692** | 0.115 | **0.038** | — (bounded, see below) |

**Consequence 1 — banded collapses the distribution into the middle.** 69 % committee is a chamber that
refers seven motions in ten and decides three. The argument for banded was Jordan's requirement (1)
(*"somewhat okay odds to win or at least not completely lose, which is where degrees and bands come
in"*) read as *lower the loss rate* — and it does lower it, 0.246 → 0.115. But that requirement asks
bands to **spread** outcomes so a loss is partial rather than total; a legislature that almost never
resolves anything is not a spread, it is a constant. **Raw is the three-outcome distribution, 41 / 34 /
25, with a real 34 % middle already there.** On Jordan's own criterion raw wins, and the earlier reading
measured the wrong property.

**Consequence 2 — banded silently removes the top and bottom of the ladder.** Each side's banded
movement is 0–3, so |A − B| ≤ 3; from the neutral start 5 the track is confined to [2, 8], and
`A_total` (≥ 9) and `B_total` (≤ 1) become **unreachable on the dice**. They return only through an
ED-621 lobbied start, and asymmetrically — at start 6 a diff of +3 reaches `A_total` while `B_total`
stays unreachable *in that same vote*. Aggregate P(TV) 0.351 → 0.038, the residual entirely lobbied. So
banded is not a re-weighting; it is a rule that **no motion can be totally won or totally lost unless
someone lobbied the start in that direction.** Defensible as a reading of *"lobbying provides
advantage"*, and a large commitment to make by implication.

**Consequence 3 — raw's pool-size scaling is a parliament feature, not a defect.** P(TV) 0.038 / 0.287 /
0.497 at equal pools 2 / 8 / 20 was filed as a flat-shift trap. In a chamber that is correct behaviour:
**a bigger coalition should be more decisive.** The trap framing came from the resolution-diagnostic
vocabulary Jordan has ruled out of use here, and it does not survive on its own terms.

**Consequence 4 — raw is free and banded is not.** Raw is today's code and canon §10 verbatim
(`social_contest_v30.md:606-607`), so it is **byte-identical**: phase G loses its only mandatory golden
re-pin and `tools/balance_oracle.py` is not needed as a control for this row. Banded moves ~39 % of
outcomes and forces the re-pin.

**⚠ What raw owes, stated rather than dissolved — this is the real cost of the answer.** The S finding
survives the disposition: the kernel moves the track by a **degree** (`resolver.py:307-308` →
`degree_from_net`), the parliament by the **raw margin** (`parliamentary_vote.py:185`) — one quantity,
the movement into a shared track, computed two ways, which §0.06 S names as *calculations inconsistent
in methodology*. Recording raw makes that a **declared depth difference rather than an accident**: a
bout is an exchange sequence whose per-exchange contribution is quantized so repeated exchanges cannot
compound a fractional edge; a chamber vote is a single reception, where the margin **is** the quantity
and there is nothing to compound. Per §0.05 and §4 that reasoning must live **at the call site**, not
in this document — `resolve_body`'s docstring is the site, and writing it there is the one line this
disposition adds to the plan.

**Reopening condition — the only one.** If a later reading cannot defend the depth distinction on its
own terms (i.e. the parliament acquires more than one reception per motion, so its margin *does*
compound), raw becomes a second ladder with no reason and the row reopens on that fact alone.

**Falsifier owed:** the claim is that raw is byte-identical; its falsifier is a same-seed campaign whose
parliamentary outcomes differ at all from today's. Nothing here has run under `CLAUDE.md` §0.2 — this
is a recorded disposition, not an executed one.

---

## §2 · THE RECALIBRATION

### §2.0 The mechanism, and why three channels are one channel

`resolver.py:323-334`:

```
leak    = min(LEAK_CAP, Resonance.leak(adj.discipline, standing_frac) + public·PUBLIC_LEAK)      # :323-324
venue_w = venue.joint_weight(appeal, tense)                                                       # :325
res     = max(RES_FLOOR, (1 − leak)·venue_w + leak·adj.character()[appeal])                        # :326  ← the preference
rdy     = Readiness.of(standing_frac, room_frac)                                                   # :333
gain    = MERIT_SCALE · magnitude · res · rdy · U(1±JITTER) · _bias(side)                          # :334  ← the pressure
```

Three things multiply every exchange's gain and none is bounded: the adjudicator's **character** (through `res`), **institutional** and **public pressure** (through `_bias`, `:310-312`: `1 + inst·0.6 + public·0.3` on the favoured side only). The kernel already ruled once that a judge-side multiplier on `res` is the wrong channel: the armature's `res *= (1 + resonance_uplift)` was *"a SECOND, uncited channel"* and was removed for a **δσ μ-shift** on the reception (`resolver.py:289-296`, `:327-332`; `armature.py:61-71` citing CR6: *"setup advantages (genre-stasis affinity, AUDIENCE BOOST, Recall …) accumulate as δσ, tanh soft-capped, uniform probability impact"*; the cap `M_MAX = 1.5σ` at `sigma_leverage.py:104`). A judge's taste for an appeal is the same class of object as the judge's Conviction alignment with a Style. **The precedent answers the form** (rung 4): bounded δσ, not a multiplier. What it does not answer is the magnitude, which is Jordan's `[SEED]`.

**Why a multiplier cannot be "mild".** Compare-type terminals read `adv[A] − adv[B]` (`resolver.py:65`, `:87`, `:126`). A ratio *r* on all of A's gains fixes the *expected* difference at `(r − 1)·E[ΣX]`, and the sums' relative noise falls with the budget — so any *r* > 1 is decisive once the bout is long enough, and the bout is already long enough at budget 3 (measured next). The **budget sweep** (`dose2.py`) is the falsifier of the "compounding" framing: under the multiplier, A at *mild* holds **0.84 / 0.84 / 0.80 / 0.79 / 0.77** at budgets 1 / 2 / 3 / 5 / 8 while the *neutral* arm falls 0.70 → 0.24 (pathos's Room build compounds over exchanges, `:338-339`). The multiplier is **budget-invariant** — it does not compound, it *sets the ratio of totals* and lets the noise shrink under it. A once-per-bout additive term is the opposite failure: it dilutes as 1/n (**0.94 → 0.84 → 0.69 → 0.52 → 0.39**). A per-exchange δσ tracks the neutral curve at a fixed offset (**+0.03 / +0.03 / +0.03 / +0.03 / +0.03**): it scales with the signal, which is what "a modifier" means. So the answer to the brief's question — *ratio or compounding?* — is **neither: the fix is the channel, not the transform.**

### §2.1 The preference channel (`adj.character()` in `res`)

**Current measurement** (`dose2.py`, A `logos` v B `demagogue`, `private_negotiation` 4v4, `no_adjudicator` discipline 0.30 → leak 0.70; preference on logos with the remainder split evenly; discrete draw; N = 1,500; mirror control 1−P in the last column):

| preference | w | L:P ratio | **mult** (today) | **√** (Jordan) | δσ 0.5σ | δσ 1.0σ | 1 − mirror |
|---|---|---|---|---|---|---|---|
| neutral | .333 | 1.00× | 0.423 | 0.423 | 0.423 | 0.423 | 0.376 |
| mild | .450 | 1.64× | **0.796** | 0.635 | 0.423 | 0.423 | 0.775 |
| moderate | .550 | 2.44× | 0.938 | 0.789 | 0.423 | 0.508 | 0.946 |
| strong | .650 | 3.71× | 0.981 | 0.889 | 0.508 | 0.553 | 0.988 |
| extreme | .800 | 8.00× | 0.994 | 0.963 | 0.508 | 0.553 | 0.998 |

The brief's numbers reproduce (42.3 / 79.3 / 95.7 / 99.0 / 99.7 → 42.3 / 79.6 / 93.8 / 98.1 / 99.4). √ compresses the *mild* band (0.80 → 0.64) and leaves *strong*+ decided, as the brief said. **δσ under the discrete draw is a staircase** — flat at 0.423, then 0.508, then 0.553 — because `net = roll_net(pool) + net_boost(lev, pool)` adds a fraction to an integer and the ladder reads integer edges (`11_` §1.2 row 1; a 0.1σ shift is invisible until it crosses one). That makes W-G1 (the continuous draw) a **precondition** of the δσ route:

| preference | mult | √ | δσ 0.5σ | δσ 1.0σ | δσ 1.5σ | (continuous draw) |
|---|---|---|---|---|---|---|
| neutral | 0.427 | 0.427 | 0.427 | 0.427 | 0.427 | |
| mild | 0.767 | 0.615 | 0.447 | 0.461 | 0.484 | |
| moderate | 0.923 | 0.759 | 0.459 | 0.497 | 0.531 | |
| strong | 0.975 | 0.870 | 0.477 | 0.530 | 0.564 | |
| extreme | 0.991 | 0.943 | 0.502 | 0.563 | 0.608 | |

Under δσ at 1.0σ (leak-gated, so the *effective* shift is `1.0σ × leak × centred(w)`, at most 0.63σ at w = 0.80 before a 0.30-discipline judge), an **extreme** preference is worth **+0.14** — about two faculty steps near even (`faculty.py`: 4v6 → 6v6 is 0.394 → 0.503) — and a **mild** one **+0.03**, half a step. That is the scale of *"a modifier based upon adjudicators as individuals"*. The **discipline gate survives** as designed: at discipline 0.75 the multiplier still runs 0.640 → 0.949 (a 0.31 swing) where δσ runs 0.619 → 0.677 (`extra.py` (3)); at 0.90, 0.706 → 0.871. And the **MUTUAL** case `12_` gives negotiation (the counterparty hears; leak → identity, proxied at discipline 0.10 → `LEAK_CAP` 0.90): multiplier **0.345 → 0.804 (mild) → 0.996**; √ → 0.616 → 0.978; δσ-continuous → 0.385 → 0.486. Under the multiplier, *reading the other party* is not Attunement, it is the whole game — the recalibration is a precondition of `12_` §8.4 step 1 too.

On the band terminal (`grand_contest`, budget 5, one judge, P(A-decisive+) / P(committee), continuous draw): multiplier **0.057 / 0.300 / 0.697 / 0.901 / 0.985**; √ 0.057 / 0.143 / 0.269 / 0.473 / 0.796; δσ 1.0σ 0.057 / 0.066 / 0.076 / 0.081 / 0.098 (committee stays 0.73–0.80). Ethos behaves the same as logos on every arm (`dose2.py` last table: multiplier 0.620 → 0.994; √ → 0.975; δσ-continuous → 0.757) — the brief's second correction, confirmed.

**Target.** A preference is a *modifier*: **an extreme lean moves P(A) by no more than a faculty step or two at even faculty, and a mild lean by less than the binomial noise of a 200-bout sample (±0.035)**; the neutral arm is byte-identical; discipline still gates the person; and the shift *scales with the bout* rather than deciding it. **Transform: δσ.** `res = max(RES_FLOOR, (1 − leak)·venue_w + leak·(1/3))` — the office/person blend survives with the person's *mean* taste, so the neutral judge is unchanged by construction — and `_reception` gains `dsigma_bonus += PREF_DSIGMA_MAX · leak · clamp((char[appeal] − 1/3) / (2/3), −1, 1)`. `PREF_DSIGMA_MAX = level("major") = 1.0σ  # [SEED]` — the measured row above; the soft cap (`M_MAX` 1.5σ) still binds the sum with the armature. **Jordan's √ is recorded as the value-cheap interim** (three lines, keeps the multiplier, halves the mild-band damage, does not bound the extremes) and is *not* the default, because it compresses the wrong form (rung 4). **The magnitude is Jordan's** (`[OPEN — Jordan tuning]`, `SKILL.md:757`); the table gives him 0.5 / 1.0 / 1.5.

**Falsifier** (lands with W-G5, §4): the five-level table above re-executed through `build_contest(...)` with the row's judge replaced by `pref(axis, w)`, asserting (i) neutral == the pre-change neutral to 3 dp on the same seeds, (ii) mirror complement within 0.03 at every level, (iii) `P(A | extreme) − P(A | neutral) ≤ 0.20` and `≥ 0.05` at discipline 0.30, (iv) `P(A | mild) − P(A | neutral) ≤ 0.05`. Fails before on (iii) and (iv) by 0.37 and 0.33; passes after. Plus the budget-invariance probe: `P(A | mild) − P(A | neutral)` within ±0.02 across budgets 1/3/8 — fails before (+0.15 / +0.37 / +0.52), passes after (+0.03 / +0.03 / +0.03).

**Goldens that move:** all of them that resolve a bout before a non-neutral bench — which is every shipped bench (`extra.py` (4): `expert_judge` and `panel` carry logos **0.55**, `crowd` carries pathos **0.55**; the "moderate" dose): `GOLDEN_TRACE` (`_kernel_tests.py:738-749`, `grand_contest`/crowd, logos v logos — symmetric policies, but the crowd's res on logos changes so every `advA`/`advB` moves), the `_kernel_tests` rate checks that pin adjudicator effects (`:86-93`, `:153-154`, `:167-168`, `:246-252`, `:518`), and **both campaign goldens** (`test_mc_v18_regression.py:127-136`, `test_f7_smoke_oracle.py`) because the campaign resolves `guild_arbitration` before a bench of five logos-0.55 judges. **Must not move:** the parliament goldens (`test_parliamentary_action.py`, `test_parliamentary_bridge.py`) — depth 0 has no `res`.

### §2.2 The ethos "second channel" — decomposed, and it is not what the brief says

`ethos.py`, `courtier` (ethos) v `demagogue` (pathos), neutral judge (discipline 0.30), `private_negotiation` 4v4, N = 1,500; control `logos` v `logos` = 0.529 on every arm:

| arm | P(A) | what it isolates |
|---|---|---|
| as-is | **0.620** | the brief's 66/34 (mine 62/38 at this N) |
| `RhetoricalWeights` flat (all nine = 1.0) | 0.543 | the R-matrix is **+0.08** of it: `ethos_present 1.20` v `pathos_present 0.90` (`primitives.py:197`, `:201`) — at QUALITY the present tense applies |
| flat + ethos build off (`c.build_ethos`, `resolver.py:336-337`) | 0.296 | remove ethos's build and the courtier **loses** — because pathos still builds |
| flat + Room build off (`self.room.build`, `:338-339`) | 0.752 | remove pathos's build and the courtier wins big |
| flat + both builds off | 0.529 | = the control: **the builds are symmetric** — `Readiness.of` weights Standing and Room equally (`W_STANDING, W_ROOM = 0.40, 0.40`, `primitives.py:256`) |
| flat + `ETHOS_UNLOCK = 0` (`:241`, the leak uplift from built Standing) | 0.516 | the ethos-**only** extra — leak — is worth **+0.03** |

**So the brief's claim is wrong in two places and right in the conclusion.** Pathos *also* has a second channel (Room → Readiness, `:338-339` → `:333`); the ethos-only extra is the leak uplift and it is small (+0.03); the R-matrix `[SEED]`s contribute more (+0.08). **The genuine asymmetry is that `logos` builds nothing** (`_advance:336-339` has no logos branch) and is compensated only by the venue's role weight (`proof_logos 0.40` v `0.30`, `resolver.py:152-154`): `logos` v `courtier` **0.360** and `logos` v `demagogue` **0.423** before the neutral judge; with the R-matrix flat, courtier v logos **0.659** and demagogue v logos **0.650**, and both fall to **0.412** when the builder's build is removed — i.e. the +0.10 role weight is worth ~0.09 and each build is worth ~0.24.

**Target.** *No dominant appeal at a neutral hearing*: at a neutral judge on a flat R-matrix, each pure appeal against each other within **±0.10 of even** `[SEED target]` — an R-VARIETY property (§0.06 R: *variety in approach*) and the "is one option dominant" question the NERS pass asks. **Transform: the existing Readiness dials, no new mechanism.** `readiness.py` (shipped role weights `.30/.30/.40`, flat R): `FLOOR 0.40, W 0.40/0.40` (today) → 0.543 / 0.659 / 0.650; **`FLOOR 0.55, W 0.25/0.25` → 0.549 / 0.507 / 0.490**; `FLOOR 0.60, W 0.40/0.40` → 0.547 / 0.547 / 0.532. On *equal* role weights (⅓ each) no Readiness setting reaches the target (best 0.525 / 0.614 / 0.618 at `FLOOR 0.70`), which says the logos role weight *is* the compensation and the dials are what to trim, not the register. **Default: `Readiness.FLOOR = 0.55`, `W_STANDING = W_ROOM = 0.25`** — both already `[SEED]`s that have been retuned once each (`:255-256`: *"raised from 0.35"*, *"lowered from 0.50"*). The R-matrix's nine `[SEED]`s (`:192-202`) and `ETHOS_UNLOCK` are Jordan's and untouched: the leak channel is the designed way *built ethos draws the judge toward character* (`:240`), and +0.03 is a portrait, not a defect.

**Falsifier:** the three pairwise rates at a neutral judge, flat R, shipped role weights, N ≥ 1,500 each: all within ±0.10 of 0.5, with `logos` v `logos` within ±0.05 (the control). Fails before at two of three (0.659, 0.650), passes after. **Goldens:** `GOLDEN_TRACE` (logos v logos — Readiness at zero Standing/Room is `FLOOR`, so *every* gain scales by 0.55/0.40 — moves), the `_kernel_tests` build-payoff checks (`:92`, `:246-252`), both campaign goldens. Phase G.

### §2.3 The faculty channel

**Current measurement** (`faculty.py`, `guild_arbitration`, the production terminal and the band ladder on the **same** final state, N = 1,500):

| A v B | ballot a / draw / b | band A_tot / A_dec / **comm** / B_dec / B_tot | mean gap |
|---|---|---|---|
| 1v6 | 0.071 / 0.000 / 0.929 | 0.000 / 0.000 / **0.299** / 0.499 / 0.203 | −1.79 |
| 2v6 | 0.150 / 0 / 0.850 | 0 / 0.003 / 0.515 / 0.406 / 0.075 | −1.25 |
| 3v6 | 0.279 / 0 / 0.721 | 0 / 0.015 / 0.715 / 0.241 / 0.028 | −0.73 |
| 4v6 | 0.394 / 0 / 0.606 | 0 / 0.017 / 0.881 / 0.100 / 0.003 | −0.31 |
| 6v6 | 0.503 / 0 / 0.497 | 0.001 / 0.029 / 0.945 / 0.025 / 0 | +0.04 |
| 4v4 | 0.526 / 0 / 0.474 | 0.002 / 0.067 / **0.858** / 0.069 / 0.003 | +0.03 |

`11_` §1.2 row 3 reproduces (1v6: 0.066 / 0.295 there). Three facts bind the plan: **(a)** faculty enters the reception twice — `Pool.size = max(5, 2f + 3)` (`primitives.py:211`) and `Leverage.net = (f − 4)/6 + level("moderate")` (`:225-230`) through `net_boost` (`sigma_leverage.py:190-203`) — and under the discrete draw the leverage half is **a staircase** (faculty 0–3: `net_boost` −0.30 / 0.00 / +0.35 / +0.79, all below the first integer edge; faculty 4: +1.28 crosses it), so faculty is a no-op below 4 except through pool size (`11_` row 1, reproduced); **(b)** Jordan's 1D-floor ruling does not reach here (`11_` §0.2 item 2: zero callers of `p_success`/`roll_net_continuous` in the package; the kernel's floor is the `5` at `:211`, which binds only at faculty 0 — `2·1 + 3 = 5` already — so the S defect is one cell wide); **(c)** requirement (1) — *somewhat okay odds, or at least not completely lose* — is met at the terminal, not in the channel: the band gives the 1v6 side **30 % committee** on the rolls the ballot resolves 93 % loss, which is `11_` W-C1's whole point.

**Target: a design choice, and the default is to leave the channel alone.** How much a five-step skill gap should decide is Jordan's (E4 in `11_` §8), and the instrument is the table above. The two *architectural* items are already `11_`'s: W-C1 reports the band on every terminal (fixes "completely lose"), W-G1 un-quantizes the leverage staircase (makes faculties 0–3 distinguishable at the lower edges). After G1, re-run this table — the 1v6 gap will widen slightly (the fraction at faculty 1 is 0.000, at 6 it is +2.35, and the continuous draw pays the fraction) and that is the number to hand Jordan, not this one.

**Falsifier for "leave it":** the faculty table above is a `ck` at ±0.03 per cell before G1 and re-pinned after G1 with the before/after in the commit. **Goldens:** none before G1; all in G1.

### §2.4 Band edges and the track scale — two dials that are one

The edges 9/7/3/1 are canon (`social_contest_v30.md:279`, `:608`); their **width in `adv` units** is `TRACK_SCALE` (`resolver.py:86`, `[SEED]` 1.5), and `MERIT_SCALE` (`:39`, `[SEED]` 2.6) scales every gain. For the band terminal the two are **collinear** — `track = start + TRACK_SCALE · MERIT_SCALE · Σ(…)` — and the table shows it (`faculty.py`, `grand_contest`, expert judge, logos v logos, N = 800; P(committee) / P(A-dec+) at 4v4):

| product | (MERIT, TRACK) | 4v4 comm / A+ | 3v4 | 1v6 comm | 6v1 A+ |
|---|---|---|---|---|---|
| 2.6 | (2.6, 1.0) | 0.95 / 0.03 | 0.84 / 0.03 | **0.33** | 0.66 |
| 3.9 | (2.6, 1.5) **today** | **0.80 / 0.10** | 0.65 / 0.08 | 0.16 | 0.84 |
| 5.2 ≈ 5.25 | (2.6, 2.0) ≈ (3.5, 1.5) | 0.70 / 0.15 ≈ 0.70 / 0.15 | 0.52 / 0.13 ≈ 0.52 / 0.13 | 0.10 ≈ 0.10 | 0.89 ≈ 0.89 |
| 7.0 ≈ 6.75 | (3.5, 2.0) ≈ (4.5, 1.5) | 0.54 / 0.24 ≈ 0.55 / 0.23 | 0.39 ≈ 0.40 | 0.06 ≈ 0.06 | 0.93 ≈ 0.92 |
| 11.25 | (4.5, 2.5) | 0.36 / 0.34 | 0.24 / 0.23 | 0.03 | 0.96 |

(`MERIT_SCALE` is *not* redundant elsewhere — `ThresholdRace(5.0)`, `REBUT_CAP`, `EVIDENCE_CAP` read `adv` directly — so the dial to turn is `TRACK_SCALE`.) **The tension a target must face:** widening the equal-faculty spread (less committee at 4v4) *removes the weak side's middle* at 1v6 (0.33 → 0.03 across the table). `11_` §5.4 asks for a per-issue mix near 0.11 / 0.33 / 0.56; nothing on the table gives it at one faculty pair, and a product that gives 4v4 texture (≈ 7) gives 1v6 nothing. **So the band scale cannot be set until the faculty channel is** (§2.3) — the gap at 1v6 (−1.79) must shrink relative to the committee half-width (1.33 at scale 1.5) for both requirements to hold at once, and that is the order §4 imposes: G1 (draw) → the faculty table → `TRACK_SCALE`. **Target: Jordan's mix (E4); default: today's 1.5**, with this table as the instrument and one addition to it — the `PARTIAL` fraction of a nine-issue bundle at 3v4 (`11_` W-D2's texture test), which is the number the mix is actually stated in.

**Falsifier:** the table is a `ck` grid at ±0.05 per cell pinned at (2.6, 1.5); a `TRACK_SCALE` change re-pins it with the grid in the commit. **Goldens:** everything on a `PersuasionTrack` proceeding moves with `TRACK_SCALE` (`GOLDEN_TRACE`'s track column; both campaign goldens do **not** — `guild_arbitration` is `VoteAtClose`, which reads the gap, not the track, `resolver.py:126`).

### §2.5 `draw` and abstention reachability

Measured in §1.4: ε = 0.3 → 12.7 % draw at n = 5, 4v4; 3.5 % at 1v6 (`12_` S6(d)). **Target: `draw` reachable on every odd bench, at a rate that falls with the room's gap** (a hung bench is a close-room outcome). **Transform:** `VoteAtClose.abstain_dead_zone` `[SEED]`, in the ballot's own units (`k·gap + N(0, noise)`; `noise` 0.8, `resolver.py:121`). **Default 0.0 in phase F** (byte-identical), **0.3 in phase G** `[SEED]` — the measured row where a 4v4 bench hangs one time in eight and a 1v6 bench one in thirty. Jordan's value.

**Falsifier:** at ε = 0.3, `guild_arbitration` 4v4 over 2,000 seeds: `0.08 ≤ P(draw) ≤ 0.18`; at 1v6: `0.01 ≤ P(draw) ≤ 0.08`; at ε = 0: `P(draw) == 0` (the control). Fails before (no parameter), passes after. **Goldens:** none at ε = 0; at 0.3, both campaign goldens (the production bench) and `_kernel_tests.py:117` (`draw < 0.10` on a matched f7 — re-read at the new ε).

### §2.6 Pressure — institutional to the start, public to δσ

**Current measurement** (`draw.py`, `grand_contest`, expert judge, 4v4 logos v logos, N = 1,500; P(A-dec+) / committee / P(B-dec+)):

| `institutional` | **multiplier** (today, `_bias`) | **start offset** `+2·inst`, ED-621-clamped `[4, 6]` | start offset unclamped |
|---|---|---|---|
| 0.00 | 0.111 / 0.783 / 0.105 | 0.111 / 0.783 / 0.105 | same |
| 0.25 | 0.268 / 0.677 / 0.055 | 0.162 / 0.778 / 0.060 | same |
| 0.50 | 0.486 / 0.492 / 0.022 | **0.264** / 0.709 / 0.027 | same |
| 0.75 | 0.684 / 0.303 / 0.013 | 0.264 (clamped) | 0.390 / 0.595 / 0.015 |
| 1.00 | **0.807** / 0.183 / 0.010 | 0.264 (clamped) | 0.517 / 0.473 / 0.010 |

On `private_negotiation` (TallyAtClose, 3 exchanges) the multiplier alone moves P(A) **0.529 → 0.705 (inst 0.25) → 0.923 (inst 1.0)** — a 1.15× thumb is already a 70/30 verdict. It is the §2.0 class exactly: an unbounded ratio on the total.

**Target and transform.** `institutional` → **the start offset, at both depths**, under the ED-621 clamp — canon's own bound (*"cannot predetermine a vote"*), the parliament's own carrier, one home (S: *calculations consistent in methodology*). `build_contest(..., lobbying_offset: int = 0)` → `win = PersuasionTrack(start=track_start_of(offset))` on tracked rows (the untracked `TallyAtClose` rows have no start; there, institutional pressure has no carrier and **should have none** — a tally of what was said cannot be lobbied, which is the design reading of canon marking those rows "N/A"). `public` → the **δσ channel** on the favoured side's reception (CR6 names *audience boost* as a δσ advantage verbatim, `armature.py:61-64`), at the same `[SEED]` cap as the preference; its leak half (`PUBLIC_LEAK`, `:323-324`) stays — `12_` §3 measured it inert below discipline 0.5 because `LEAK_CAP` binds, which is a `LEAK_CAP` question for Jordan, not this item's. `_bias`, `INST_BIAS`, `PUB_BIAS` are deleted. **Not measured here:** the public arm under δσ (same class as §2.1; its falsifier is the same table with `public` in place of `w`).

**Falsifier:** the institutional table above through `build_contest(venue="grand_contest", lobbying_offset=k)` for k ∈ {0, 1, 2, 3}: P(A-dec+) ≤ 0.30 at every k (fails before at 0.81 for the equivalent multiplier; passes after), and identical for k = 2 and k = 3 (the clamp). **Goldens:** `_kernel_tests.py:153-154` (`institutional=0.5` → `a > 0.65` — rewritten to the start-offset form and its measured value 0.26 at grand_contest, or asserted on a tracked venue where a start of 6 gives ≥ 0.6 of non-B outcomes); both campaign goldens **do not move** (the seam passes `Pressure()` on every proceeding — `10_` §1.7 — and `lobbying_offset = 0`).

### §2.7 The bench — the feature's precondition, measured

`bench2.py`: 100 random 5-benches, each member's taste `neutral + N(0, s)` renormalised; 200 bouts per bench; A logos v B pathos on `private_negotiation`; per-member reception (`12_` S7's shape — one shared roll, one shared jitter draw, each member hears with its own leak and character; **byte-identical to the shipped `Panel`-mean when members are identical, 0/500**). "Decided" = |P(A) − 0.5| > 0.2 before anyone has argued differently.

| spread s | transform | SD of P(A) across benches | benches decided | min – max |
|---|---|---|---|---|
| 0 (control) | any | **0.000** | 0 % | one mind |
| 0.04 | mult / √ / δσ-cont | 0.064 / 0.027 / 0.006 | 3 % / 0 % / 0 % | .29–.64 / .34–.52 / .41–.44 |
| 0.08 | mult / √ / δσ-cont | 0.129 / 0.069 / 0.013 | 15 % / 3 % / 0 % | .18–.75 / .28–.65 / .38–.45 |
| **0.12** | **mult** / √ / δσ-cont | **0.177** / 0.113 / **0.018** | **33 %** / 12 % / **0 %** | **.09–.84** / .24–.76 / .38–.45 |

(Binomial noise at n = 200 is 0.035; the per-member *ballot* aggregation gives the same picture, SD 0.198 / 0.117 / 0.018 at s = 0.12.) `s = 0.12` is *mild* individual variation — one weight moved by about what "mild" (0.45) means. **Under the multiplier one bench in three is decided by who was drawn; under δσ the bench-to-bench spread is half the sampling noise.** One extreme member on a neutral bench: mult 0.745, √ 0.650, δσ 0.450 (from 0.435); all five at mild: 0.775 — a homogeneous bench is one mind, so the single-judge dose table *is* the bench table.

This is the number the brief's sentence — *"a member drawn with a mild lean decides the case before anyone argues"* — actually measures, and it is the falsifier for the whole recalibration: **after W-G5, SD across mildly-varied benches ≤ 0.05 and 0 % decided; before, 0.177 and 33 %.**

### §2.8 Goldens — which move, which must not, by item

| item | phase | `GOLDEN_TRACE` | `_kernel_tests` rate checks | campaign goldens (seed-0 n=2, seed-42 n=8) | parliament goldens (action/bridge/transfer) |
|---|---|---|---|---|---|
| **W-D4** the fold (§1.2, raw margin) | D | no | no (count moves by the deleted `coalition_*` checks — W-A3's arithmetic) | **no** — falsifier: 3,000-seed byte-identity | **no** — falsifier: the four pinned seeds + the 22-triple sweep |
| F-1 `PersuasionTrack.outcome` bands `self.track` | C | no | no | no | no |
| **W-F3b** `abstain_dead_zone` = 0.0 | F | no | no | no | no |
| W-G1 continuous draw (`11_`) | G | **yes** | yes | **yes** | no (depth 0 keeps `roll_pool`) |
| **W-G4** pressure → start / δσ | G | no (no pressure on the path) | `:153-154` | no | no |
| **W-G5** preference → δσ | G | **yes** | `:86-93`, `:167-168`, `:518` | **yes** | no |
| **W-G6** Readiness dials | G | **yes** | `:92`, `:246-252` | **yes** | no |
| **W-G7** ε = 0.3 | G | no | `:117` | **yes** | no |
| ~~**J-P1** banded~~ — **closed raw 2026-09-05** | — | no | no | **no** (byte-identical) | **no** — row closed, no re-pin |

Phase G is one re-pin (`11_` §7: *the goldens MOVE, deliberately*) with `tools/balance_oracle.py` as the campaign-level control — and note `CLAUDE.md` §7's caveat applies: the oracle is a **campaign** instrument, so for W-G4 (no pressure on the path) and W-F3b (ε = 0) both arms are identical by construction and running it would be a fake control; run it for G1, G5, G6, G7 and J-P1 only.

---

## §3 · Where this slots into `11_`'s seven phases and twenty-three items

`11_` §7's table (`11_:337-345`) stands; nothing here re-orders it. The fold and recalibration add **six items and two corrections**, and every addition before G is value-identical for agôn and byte-identical for the parliament:

| phase | `11_` items it depends on | this document adds | done when |
|---|---|---|---|
| A | **W-A2** (band single owner — the parliament imports the five names from `resolver`), **W-A3** (deletes the third implementation), **W-A4** (the stub) | *correction A-2′*: `track_start_of(offset)` and the three `BG_VOTE_LOBBY_*` names relocate to `resolver.py` in W-A2's block, one owner for the ED-621 clamp | `grep -n "max(4" faction.py parliamentary_vote.py` → zero |
| C | **W-C1** (`ContestOutcome`, `outcome()`) | *correction F-1*: `PersuasionTrack.outcome()` bands `self.track(s)`; `Bout.outcome` unchanged | a lobbied-start `PersuasionTrack(start=6).outcome()` on a zero state reports `committee`, and `start=4`'s degree equals `start=6`'s |
| D | **W-D1..D3** (the fold over issues; `resolve_issues`) | **W-D4 · the parliament row + `resolve_body` + the adapter** (§1.2–1.6). A multi-clause motion is the **adapter** calling `resolve_body` once per clause on the same pools and `base_ob` (per-clause lobbying/genre allowed) — it does *not* route through `resolve_issues`, which would need `Issue` to carry a depth-0 spec (pools, `base_ob`) and is not shipped here; inter-clause *conditions* therefore wait on that residual, named in §6 | 3,000-seed byte-identity vs the pre-fold `run_parliamentary_vote`; the four action seeds; the 22-triple bridge sweep; a two-clause motion returning two `ContestOutcome`s |
| F | **W-F3** (`disposition` + `unanimity_required`; *do not alter `weighted_by_standing`*) | **W-F3b · `abstain_dead_zone=0.0`** on `VoteAtClose`, in the same `_ballots` pass (one draw per member, unchanged count) | ε = 0 → the goldens' draw count unchanged (patch `gauss` with a counter); ε = 0.3 → the §2.5 band |
| G | **W-G1** (continuous draw — precondition of every δσ item) | **W-G4** pressure (§2.6) · **W-G5** preference δσ (§2.1) · **W-G6** Readiness (§2.2) · **W-G7** ε = 0.3 (§2.5) · **J-P1** only if Jordan picks banded | one re-pin commit per item, in the order G1 → G5 → G6 → G4 → G7; the §2.1/§2.2/§2.7 tables before/after in each message; `balance_oracle` for G1/G5/G6/G7 |

Two of `11_`'s escalations are touched: **E4** (the win/partial/lose mix) gains the §2.4 instrument and the ordering constraint (faculty before scale); **E1** (the interaction model) is *not* reopened — `resolve_body` is the accumulation model at depth 0 (two independent receptions, a difference at close), which is what `11_`'s default already is. `12_` §8.4 step 5 ("retire `run_parliamentary_vote`'s body into the depth-0 path … keeping its constants as the single owner") is W-D4.

---

## §4 · FOR OPUS 5 — the executable instruction set

**Ground rules are `11_` §9's, unchanged**, plus one: **the parliament goldens are a control, not a target.** `python -m pytest engine/tests/test_parliamentary_action.py engine/tests/test_parliamentary_bridge.py engine/tests/test_parliamentary_transfer_bridge.py -q` must be green and *unchanged* after every item below except J-P1. If one moves before G, the depth-0 path is not consuming `rng` in the same order — stop and diff `roll_pool` calls.

### A-2′ · The ED-621 clamp gets one owner (with W-A2)
- **Files:** `resolver.py` (W-A2's module-level block); `parliamentary_vote.py:70-72`, `:160-163`; `faction.py:142` (dies with W-A3).
- **Target:** in `resolver.py`: `LOBBY_OFFSET_MAX = 2  # social_contest_v30 §10 step 4 "max ±2"`, `TRACK_START_MIN, TRACK_START_MAX = 4.0, 6.0  # ED-621 "compromise zone"`, and `def track_start_of(offset: int) -> float: return max(TRACK_START_MIN, min(TRACK_START_MAX, TRACK_START + max(-LOBBY_OFFSET_MAX, min(LOBBY_OFFSET_MAX, offset))))`. `parliamentary_vote.py` imports it; `BG_VOTE_LOBBY_*` become aliases for one release, deleted with W-D4.
- **Falsifier:** `track_start_of(k)` for k ∈ −3..3 equals the pre-change `start` at `:161-162` for every k (a 7-point `ck`); `grep -rn "min(6\|max(4" systems/social_contest --include=*.py` → zero after.
- **Control:** parliament goldens unchanged (same arithmetic). Blast: three files.

### F-1 · `PersuasionTrack.outcome()` bands its own track (with W-C1)
- **File:** `resolver.py` W-C1's `outcome()`.
- **Target:** `class PersuasionTrack: def outcome(self, s, adj=None, reason="win"): t = self.track(s); w = self.resolve(s, True, adj); return ContestOutcome(winner=…, degree=BAND_TO_OUTCOME[band_of_track(t)][1], margin=s.adv[A]-s.adv[B], reason=reason, band=w)` — `degree_of_margin(margin)` with module defaults is for the terminals that have no start of their own.
- **Falsifier:** over a 500-state seeded sweep of `PersuasionTrack(scale=1.0, start=4.0)`, assert `outcome().degree == BAND_TO_OUTCOME[resolve(s, closing=True)][1]` and `assert checked == 500`. The two forms disagree wherever the terminal's own scale or start moves the banding — the named discriminating case is `adv = (2.7, 0)` at `scale 1.0, start 5.0`: `self.track` = 7.7 → `A_decisive`/SUCCESS, while `track_of(2.7)` under the module default (scale 1.5) = 9.05 → `A_total`/OVERWHELMING. Fails under the defaults-based form, passes after.
- **Control:** every existing `PersuasionTrack()` (default start/scale) is unchanged — `track_of(m)` ≡ `self.track(s)` there.

### W-D4 · The parliament row, `resolve_body`, the adapter
- **Files:** `modes.py:485-519` (+ the ninth row), `resolver.py` (+ `resolve_body`, after `Bout`), `parliamentary_vote.py` (the body `:166-206` deleted; `:74`, `:54` deleted; `VoteResult` loses the eight diagnostic fields; `run_parliamentary_vote` becomes derive → `resolve_body` → write → view), `wrapper.py` W-D2's `resolve_issues` (+ the `budget == 0` branch), `contest/__init__.py` (+ `resolve_body`).
- **Current:** `parliamentary_vote.py:166-206` rolls `dice_engine.roll_pool(pool_size=pool, tn=BG_VOTE_TN, rng=rng)` for A then B (`:178`, `:181-182`), floors the margin per side (`:185-186`), clamps and bands (`:196-205`).
- **Target:** §1.2's code, verbatim, with this order of draws: **side A's `roll_pool` then side B's, and no other draw** — `resolve_body` consumes `rng` exactly as `:181-182` did. `_side_genre` and the two `+1D`s stay in the adapter (`:117-122`, `:172-175`). `VoteResult` view per §1.6. `PROCEEDINGS_TABLE`'s `_crosscheck_proceedings` (`dictionaries.py:607-624`) compares `exchange_count`/`adjudicator_type`/`track_start`/`tracker_mode` — add the ninth row to `_PROCEEDING_PROSE` with `adjudicator_type=None` handled, or exclude `exchanges == (0, 0)` rows from the adjudicator check; state which in the commit.
- **Falsifiers:** **(1)** the 3,000-seed byte-identity of `s6_parl.py` re-run against the *parent commit's* `run_parliamentary_vote` (write its outputs to a fixture first): `(status, final_track, total_victory, resistance, abstainers, mandate_penalty)` equal, `assert checked == 3000`; **(2)** `engine/tests/test_parliamentary_action.py` and `test_parliamentary_bridge.py` green and unedited; **(3)** `run_parliamentary_vote(motion_with_two_clauses, parties, world, rng)` (the adapter iterating `resolve_body` per clause) returns two `ContestOutcome`s whose `band`s equal two independent `run_parliamentary_vote` calls consuming the same rng sequence in clause order; **(4)** `VoteDeclaration("Guild", "abstain", "Memory")` on a Sta-6 faction yields `resistance 1` and the same outcome as leaving it undeclared (the explicit and implicit forms are one position).
- **Control:** both campaign goldens byte-unchanged (the bridge's path is `run_parliamentary_vote(motion, decls, world, rng)` with `world.rng` — same draws). **Blast:** five files; `_KERNEL_EXPECTED` moves by the added `ck`s (state the arithmetic).

### W-F3b · Abstention at depth k (with W-F3)
- **File:** `resolver.py:98-147` `VoteAtClose`, inside W-F3's single `_ballots` pass.
- **Target:** `VoteAtClose(..., abstain_dead_zone: float = 0.0)  # [SEED] a juror whose k·gap+disposition+noise lies within ±ε casts no ballot`; `_ballots` returns `(i, weight, assent | None)`; both aggregation rules count only cast ballots (`total = Σ weight of cast`), so `n_effective = n − abstainers` is implicit. `weighted_by_standing`'s rule is unaltered for ε = 0 (`11_` §9 rule 7 honoured: the ratified rule is not changed, a member can decline to vote under it).
- **Falsifiers:** §2.5's three bands; draw-count control (`gauss` counter: exactly `len(members)` per resolve at every ε); ε = 0 byte-identical over 500 `guild_arbitration` seeds.
- **Control:** goldens (ε = 0). Blast: one class.

### W-G4 · Pressure: institutional → the start, public → δσ (phase G, after G1)
- **Files:** `resolver.py:41-43` (`PUBLIC_LEAK` stays; `INST_BIAS`, `PUB_BIAS` deleted), `:310-312` (`_bias` deleted), `:334` (the `* self._bias(side)` factor deleted), `_reception` (+ `public` δσ on the favoured side), `contract.py:69-77` (`Pressure` docstring: `institutional` is the start offset), `wrapper.py` (`build_contest(..., lobbying_offset=0)`), `modes.py` (`proceeding_venue` applies `track_start_of` on tracked rows).
- **Target:** `institutional` is carried as an integer offset (canon's unit) — `Pressure.institutional` becomes `int` and the venue's `win.start = track_start_of(offset)` for tracked rows; untracked rows ignore it (documented). `public`: `dsigma_bonus += PUBLIC_DSIGMA_MAX * public  # [SEED] level("moderate")` on the side `toward` names, in `_apply` beside the armature's δσ.
- **Falsifiers:** §2.6's table as a `ck` grid; `grep -n "_bias\|INST_BIAS\|PUB_BIAS" resolver.py` → zero; the untracked-row no-op (`private_negotiation` P(A) at offset 2 == offset 0 within 0.03 — fails before at 0.53 → 0.81 under the equivalent multiplier).
- **Control:** campaign goldens unchanged (no pressure on the path). Blast: four files; `_kernel_tests.py:153-154` rewritten to the start-offset assertion.

### W-G5 · The preference channel → δσ (phase G, after G1)
- **Files:** `resolver.py:326` (`res`), `:283-308` (`_reception`), `:399-406` (`_apply`, beside the armature's δσ), `contract.py:24-35` (docstring only).
- **Target:** `res = max(RES_FLOOR, (1 - leak) * venue_w + leak * NEUTRAL_TASTE)` with `NEUTRAL_TASTE = 1/3`; in `_apply`, `pref_dsigma = PREF_DSIGMA_MAX * leak * max(-1.0, min(1.0, (self.adj.character()[mv.appeal] - 1/3) / (2/3)))` where `leak` is the same value `_advance` computes (hoist the leak computation into one helper `_leak(side)` called from both — one owner); `PREF_DSIGMA_MAX = level("major")  # [SEED] 1.0σ; §2.1's measured row; Jordan tunes`. A `Panel`'s `character()` is its mean (`contract.py:48-51`) — so a homogeneous bench is one mind, as today, and `12_` §8.4 step 2 (per-member `adv`) is where members diverge.
- **Falsifiers:** §2.1's four assertions; the budget-invariance probe; **§2.7's bench spread** (100 benches at s = 0.12, `MemberBout`-equivalent per-member reception once step 2 exists — until then, the single-judge table stands in).
- **Control:** the neutral-judge sweep (`pref(axis, 1/3)` at every discipline) byte-identical before/after on 500 seeds — this is the control that catches the §0.4 error class. **Blast:** `resolver.py`; every golden in §2.8's row.

### W-G6 · Readiness dials (phase G)
- **File:** `primitives.py:255-256`.
- **Target:** `FLOOR = 0.55  # [SEED] was 0.40; §2.2: no dominant appeal at a neutral hearing`, `W_STANDING, W_ROOM = 0.25, 0.25  # [SEED] were 0.40`.
- **Falsifier:** §2.2's three pairwise rates within ±0.10 at flat R, shipped roles, neutral judge; `logos` v `logos` within ±0.05.
- **Control:** the same three pairs at the *shipped* R-matrix, reported (not asserted) in the commit — the R-matrix is Jordan's and this item must not silently retune it. Blast: two lines; `GOLDEN_TRACE` and both campaign goldens re-pin.

### W-G7 · ε = 0.3 (phase G)
- **File:** `dictionaries.py:699-725` `panel_win_condition` (the default the production bench receives).
- **Target:** `abstain_dead_zone=0.3  # [SEED] §2.5`. **Falsifier:** §2.5's bands. **Control:** `balance_oracle` two-arm (ε 0 vs 0.3), 120 campaigns each. Blast: one default; both campaign goldens.

### J-P1 · only if Jordan rules "banded"
- **File:** `resolver.resolve_body`: `s.adv[side] = float(DEGREE_ORDINAL[degree_from_net(roll_pool(...).net, base_ob, extension=…)])`. **Falsifier:** `extra2.py`'s table re-executed: committee ≈ 0.69, TV ≈ 0.04. **Control:** `balance_oracle`; every parliament golden re-pins with the before/after status mix in the message. Do not land without the word.

**Commit plan:** `A-2′` inside W-A2's commit · `F-1` inside W-C1's · `W-D4` alone (it re-pins the count) · `W-F3b` inside W-F3's · phase G one commit per item in the order G1 → G5 → G6 → G4 → G7 (→ J-P1). After D4: `python -m pytest engine/tests/test_contest_kernel.py engine/tests/test_mc_v18_regression.py engine/tests/test_f7_smoke_oracle.py engine/tests/test_parliamentary_action.py engine/tests/test_parliamentary_bridge.py engine/tests/test_parliamentary_transfer_bridge.py tests/valoria/test_import_cycle_game_state_npe.py -q`. `HANDOFF_SC.md` gains one line per phase boundary; close nothing in the ledger from here — ED-SC-0015 (the TV stack) is the seam's, and it moves with the write.

---

## §5 · ATTACKS THAT FAILED, REPORTED AS FAILED

| attack | how | result |
|---|---|---|
| The parliament is a different procedure from the kernel (a fourth resolver, not a terminal over one roll) | `s6_parl.py`, 3,000 votes, random world/declarations/genres/lobby | **FAILED** — 0 mismatches; and a kernel-atom prototype reproduces it byte-for-byte, 0/3,000 |
| The fold cannot be byte-identical because the kernel rolls on the global stream | `resolve_body` takes `rng` and calls `dice_engine.roll_pool` in the parliament's order | **FAILED** — same draws, same order; the prototype proves it |
| The zero-zero branch is a distinct rule the fold would lose | counted zero-zero votes (223/3,000) and their band | **FAILED** — every one already `committee` by the track (`start ∈ [4,6]`); inert, as `12_` found |
| Abstention resistance is inert at large pools (`faction.py:139`) | resistance × pool, N = 4,000 per cell | **FAILED** — attenuated (0.273 → 0.283 at pool 16; 0.625 → 0.917 at pool 2), not inert |
| Abstention is not live on the campaign path | the bridge's two-declaration shape with Sta-6 abstainers | **FAILED** — resistance 2 fires at Sta ≥ 6 |
| The dose-response is a side bias, not a preference effect | mirrored contestants at every level | **FAILED** — 1−mirror tracks the direct arm within 0.02 |
| My δσ arm measured the preference | its neutral arm vs the baseline | **SUCCEEDED against my first run** (0.757 vs 0.423 — §0.4); corrected, the neutral arms agree to 3 dp |
| The multiplier "compounds" with budget (the brief's framing) | budget sweep 1/2/3/5/8 at mild | **FAILED** — budget-invariant (0.84 → 0.77); it is a ratio of totals, and the *once-per-bout* term is the one that dilutes (0.94 → 0.39) |
| √ bounds the channel | five levels, discrete and continuous | **FAILED** — 0.963 / 0.943 at extreme; it compresses the mild band only |
| δσ works under the discrete draw | five levels, `dsigma` 0.5σ and 1.0σ | **FAILED** — a staircase (flat, then 0.508, then 0.553); W-G1 is a precondition |
| Ethos is inert (the session's earlier claim) | `courtier` v `demagogue` at five ethos preferences | **FAILED** — 0.620 → 0.994, the same shape as logos |
| Ethos has a second channel the other two lack | the six-arm decomposition | **HALF-FAILED** — pathos has one too (Room); ethos's *only* extra is leak (+0.03); the asymmetry is logos-builds-nothing |
| The heterogeneous-bench claim rests on the per-member subclass differing from the kernel | `MemberBout` vs `Bout` on the crowd proceeding, 500 seeds | **FAILED** — 0 mismatches; and s = 0 gives SD 0.000 |
| One mild member on a bench decides the case (the brief, literally) | one member at 0.45 on four neutrals | **FAILED as stated** — +0.085 (0.435 → 0.520); what decides is a *bench* drawn with mild variation (33 % decided at s = 0.12). The per-member *ballot* on that bench is degenerate (four identical members are one mind) — the random-bench rows are the honest ballot measurement |
| `MERIT_SCALE` and `TRACK_SCALE` are independent dials | the 12-cell product table | **FAILED** for the band terminal — equal products give equal cells to 0.01 |
| The institutional multiplier is gentle at small values | `private_negotiation`, inst 0.25 (1.15×) | **FAILED** — 0.529 → 0.705 |
| A start offset can predetermine a vote | unclamped +2 at inst 1.0 | **PARTLY** — 0.517 A-decisive unclamped; the ED-621 clamp holds it at 0.264 — canon's bound does the work |
| Banding the parliament's margin is value-neutral | `extra2.py` | **FAILED** — 39 % of outcomes change; TV 0.351 → 0.038 (hence J-P1) |
| The 1D-floor ruling reaches the faculty channel | `Pool.size` at faculty 0–2; `11_` §0.2's grep | **FAILED** — the `5` binds only at faculty 0; zero callers of the continuous helpers |

---

## §6 · WHAT WOULD MAKE THIS DOCUMENT WRONG

1. **The δσ magnitude is a `[SEED]` measured on one venue at one faculty pair.** `PREF_DSIGMA_MAX = 1.0σ` gives +0.14 at extreme on `private_negotiation` 4v4 before a 0.30-discipline judge; on `grand_contest`'s band terminal it gives +0.04. If Jordan wants a judge's taste to be worth more on the band venues, the value rises and the soft cap (`M_MAX` 1.5σ, shared with the armature) starts to bind — at which point the armature and the taste compete inside one cap and the *sum* is the design question, not either number.
2. **`resolve_body` is measured byte-identical on a duck-typed world**, not on `game_state.Faction`. The prototype reads `.L`, `.Sta`, `.parliamentary`, `.adjust` — the same four attributes the module reads — but W-D4's falsifier (1) must run on `game_state.create_world` before the parliament goldens are trusted as the control.
3. **The bench measurement uses a per-member reception the kernel does not yet have** (`12_` §8.4 step 2). Until it lands, W-G5's bench falsifier is the single-judge table; the 33 % → 0 % claim is about the *rebuilt* kernel and is stated as such.
4. **The Readiness default assumes the shipped role weights stay.** `W-G2` (a venue preset per row, Jordan's) changes the register per proceeding; if it lands first, the §2.2 falsifier is re-run per row and 0.55/0.25 may not hold on `imperial_petition_venue`'s weights.
5. **"Institutional pressure has no carrier on untracked rows" is a design reading**, not a measurement — canon marks those rows N/A for the tracker, which I read as "cannot be lobbied". If Jordan wants a thumb on a tally, the start offset has nowhere to go there and a bounded δσ (the `public` route) is the fallback — the same form, a second `[SEED]`.
6. **The raw-margin default (J-P1) preserves a pool-size trap** (TV 0.50 at pool 20). If the seam rebuild routinely produces large coalitions, the parliament becomes total-victory-dominant and the "default: raw" recommendation inverts — the measurement that would show it is P(TV) over a seeded campaign after the seam lands, which nothing here can run.
7. **`[SELF-AUTHORED — bias risk]`.** §2.0 argues the δσ form from a precedent (the armature's resonance channel removed for δσ) that the kernel's own comments record; a reader should check that I have not read a *ratification* into a *judge finding*: `resolver.py:327-332` and `armature.py:61-71` cite CR6 and ED-1062 as ratified, and `sigma_leverage.py:104` cites `modifier_system_spec.md §3.1` for the cap — but the `RATIFIED_2026-06-01.md` file those comments name is not in the tree (it is at the fork), so the precedent stands on the code, which under §0.05 is the mechanism. If Jordan says the multiplier *is* what he wants and a judge's taste should be able to decide a case, §2.1's transform is wrong and only its measurements survive.
8. **Inter-clause conditions on a motion are not shipped.** A multi-clause motion is the adapter iterating `resolve_body` (§3, W-D4); *"clause 2 is withdrawn if clause 1 fails"* is `11_` W-D3's condition tuple, which lives on `Issue`, and a depth-0 `Issue` (carrying pools and `base_ob` instead of two `Contestant`s) is not specified here. If Jordan's parliament needs amendments-as-conditions before the seam rebuild, that is the one place where this fold and `11_`'s fold have to meet, and the meeting point is two fields on `Issue` — stated so it is not re-derived as a new class.
9. **Nothing here changes the grade.** Every recommendation is paper until §4's artifacts exist; the fold's byte-identity is the only claim with an execution artifact already in hand, and it is a prototype in a scratchpad, not the kernel.

*End. One file. Nothing else under the repository was created or edited; scratchpad scripts `s6_parl.py`, `dose2.py`, `extra.py`, `extra2.py`, `ethos.py`, `readiness.py`, `faculty.py`, `bench2.py`, `draw.py` and their `.out` files hold the numbers.*
