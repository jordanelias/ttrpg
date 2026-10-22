# Tutorial: Resolution and dice — how a contested act becomes one of four degrees, and what moves the odds

Repo `jordanelias/ttrpg` at HEAD `a4ca9a5`. Every number below was read from the code or computed by calling the repo's own
functions, except the precedent shapes (PbtA, Blades, d20, 2d6, 3d6), which are hand arithmetic; §9 lists what was opened and what was
run. The round-3 figures were computed by scripts that are not committed (`ctl/` is the only committed instrument); §9 names each
computation. Paths are relative to the repo root. Revised in round 3 against `51d7b05` (PR #495 on top of PR #494)
and the game-precedent suite (`research/game_precedent_suite/`); the changes are listed under §8, "Round-3 corrections".

## 0 Before you start

**The frame.** In the code there is no player character and no GM. Every person is a chooser that picks acts each season from a
closed table of verbs. It spends a scene-action budget of 5 or more (§4: about 7 acts at budget 5). The engine rolls whatever needs
rolling; nobody chooses dice. "You" in this tutorial means the
acting person: a player's character if one is ever seated, an NPC today.

**What you need from other subsystems.** The dice engine owns no inputs. It is handed a **pool** (how many d10s), an **obstacle**
(Ob) and an **advantage** in sigma units, and returns a degree. Who supplies each:

| input | supplied by | today |
|---|---|---|
| pool, social path | `engine/season/seam/wrappers/sigma.py::_pool_of` (:119-131) from `Person.capability` | `pool_default` = 2 for everyone |
| Ob, social path | `modules/social_contest/roll.py::obstacle` (:63-113) | `obstacle_default` 2, capped at 2 |
| advantage, social path | `sigma.py::contest_input` (:191) | hard-coded `leverage=0.0` |
| pool, Ob and advantage, combat | `modules/combat/core.py` (`resolution_pool` :54-56, `ob_from_defender` :100-115, `resolve` :118-127) | internal to a fight |
| pool, Ob, advantage, mass battle | `modules/mass_battle/resolution.py` (its own roller, :37-120, :221-235) | internal to a field |

**Status.** The grades follow the corrected rule, ERRATA G1. RUNS-IN-LOOP means the behaviour produced a non-refusal outcome inside
`SeasonDriver.season` over `build_realm`; "at control" means it runs but is inert at the shipped value. TESTS-ONLY means it executes
only under tests, fixtures or oracles, or with zero successful executions in the realm; a refusal gate firing does not count. DESIGN-ONLY
means no executing code. On that rule:
- The d10 roll and the margin ladder are **RUNS-IN-LOOP**: 133 graded rolls in seeds 0–1, through `tell`, `speak`, `determine`,
  `research` and `surveil`.
- The room terms and the ceiling are **RUNS-IN-LOOP at control**: they are computed every `speak`, and the ceiling clips the result
  back to the default.
- The advantage term (`leverage` is a literal 0.0), the S27.4 refusal (never fires) and fractional obstacles (none observed) are
  **TESTS-ONLY**.

## 0a How it plays

*Round-3 addition, in the form of the precedent suite's "how it plays" tutorials (`research/game_precedent_suite/tutorials/T05_social_rpgs.md`).
Every code line below was opened at `51d7b05`. The as-built text comes first; the [PROPOSED] block closes the section and none of it executes.*

**Setup choices.**
- Nothing about dice is chosen at world build except the seed. `build_realm(seed)` seats a cast whose `capability` the code states is
  empty on every corpus person (`seam/wrappers/sigma.py:123`), and `train` mints no key (`verb_table.yaml:1468`). The run bears it out:
  every person alive after two seasons has an empty `capability` (`ctl/realm_seed0_2seasons.txt:59`, counted at run end by
  `ctl/control.py:29`; seeds 1 and 2 `:60`). So the social pool is `pool_default` = 2 and any Ob without a scored
  opponent is `obstacle_default` = 2 under `obstacle_ceiling` = 2 (`fixtures.py:413-419`). TN is 7 and the owner refuses any other value
  (`dice_engine.py:182-193`). Those fixtures are injected, swept stand-ins (H-126, H-127, H-213), not choices.
- A person at the callback (`harness/play_surface.py:41-52`; TESTS-ONLY, because the season loop has no player interface of its own)
  chooses a verb and its operands, such as the subject and `to`. No `Act` field sets the pool or Ob the roll uses: the seam builds both from
  the world (`sigma.py:185-191`), and a hand-declared `Act.obstacle` reaches only the S27.4 refusal (`resolve.py:978-997`). The only
  `input()`-driven harness under `systems/`, `engine/` and `modules/` (grep) is a separate human-plays-a-contest harness for the
  multi-exchange kernel, outside the season loop (`systems/social_contest/sim/contest/agon_harness.py`).

**The loop** (one roll per contested act, inside RESOLVE; all automated):
1. The chooser forms the act from alignment and stance; it reads no odds (§5a).
2. `_admits` checks eligibility and the typed cell. A refusal emits the verb's refusal kind and the act ends there (`resolve.py:1025-1032`).
3. The seam reads the pool and Ob (`sigma.py:185-191`); `roll.py:103-113` composes the Ob from opposition, room, forgery and the ceiling;
   leverage is 0.0.
4. The act's own generator deals the dice: `draw_factory(world_seed, tick)(actor, "roll:<prize or verb>:<act id>")` (`resolve.py:792, :852`;
   `ids.py:48, :87-89`).
5. S27.4 may refuse (`sigma.py:273-275`); at pool ≥ 1 under ceiling 2 it cannot.
6. `degree_from_net` bands the margin (`dice_engine.py:286-301`); the fold picks `writes[degree]` and `emits[degree]` (`resolve.py:825`).
7. WITNESS turns the events into claims; a Partial `tell` may arrive distorted (`witness.py:136-175`).

**The choice menu** (the verbs that reach the dice; full rows in §4). Counts are §4's `attempted/ok` per seed 0 / 1 / 2 unless marked.

| verb | cost | effect by band, F / P / S / O | when a person picks it | grade |
|---|---|---|---|---|
| `tell` | one act in a scene, spent on any band | `news.untold` / `news.told` (the copy may be lossy) / told / told; writes nothing | holds a claim on the subject; the hearer is `with` him | RUNS-IN-LOOP (told 4/7/6) |
| `speak` | one act | `matter.turned` / `.held` / `.advanced` / `.carried`; writes nothing | a docketed matter exists | RUNS-IN-LOOP (seed 0: 3 rolled, all Failure); room terms at control |
| `argue` | one act | `argument.lost` / `argument.won` / `argument.won` + `pursuit.moved` (S, O) | a Proposition exists; the opponent is `with` him | TESTS-ONLY (0 rolled; formed and stopped 10/17/18, §4) |
| `determine` | one act; needs `remit:determine` | `matter.undetermined` / `matter.determined` (Tenure graded Partial) / + `pursuit.moved` (S, O) | a seat, a docket, a bench, a quorum | RUNS-IN-LOOP at seed 1 only (1 rolled of 6 formed) |
| `research`, `surveil` | one act | `finding.none` / `finding.made` (P = S = O) | a Record exists / present at a Rung | RUNS-IN-LOOP (`research` 7/1/2; `surveil` 5/9/5) |
| `examine` | one act | as `research` | present at a Site | TESTS-ONLY (0 admitted; formed 62/59/39; its `site` operand is filled from the subject, `decision/options.py:1047-1048`) |

No verb buys dice, lowers an Ob or adds advantage at a price; the `speak` room is earned through witnessed deeds (§5b). The precedent menus
put a spend before the roll (T05 precedent, BG3 §3: Add Bonus; Disco §3: clothing and drugs before a check); this one has none.

**First season, step by step** (seed 0, tick 0; the faces were re-derived at `51d7b05` from `ids.draw_factory`):
1. `build_realm(0)`: every `capability` is empty (`sigma.py:123`); the ctl count (`ctl/realm_seed0_2seasons.txt:59`) is over survivors
   at run end, so it bears this out but cannot show the nine dead were empty at build.
2. DELIBERATE: `p_npc_086` forms a `tell` to `p_npc_010` (§3).
3. RESOLVE admits it. Pool 2 (no `copying` key); Ob 2 (the hearer holds no key, and `tell` has no room); leverage 0.
4. `draw_factory(0, tick 0)("p_npc_086", "roll:a standing:762758bdca098db1")` deals 8 and 10: net 3, margin 1, Success.
5. The fold emits `news.told`, and WITNESS then turns the event into claims.
6. Same season: his `tell` to `p_npc_007` rolls 5 and 1 (net −1): Failure, `news.untold`. `p_npc_041` speaks at `b_s_036_cathedral`:
   reception −0.529 lifts the Ob to 2.529, the ceiling clips it to 2, he rolls 2 and 6: Failure, `matter.turned` (§3).
7. Over two seasons seed 0 rolls 70 times: 54 F / 9 P / 7 S / 0 O (§9). Four tellings land (`ctl/realm_seed0_2seasons.txt:50`) and all
   3 speeches fail (`:51`).

**What changes later.** Nothing on this layer. `train` mints no key (`ctl/` shows `train` 38/0, 30/0, 30/0 attempted/ok for seeds 0 / 1 / 2),
so season-2 odds equal season-1 odds. The one input that drifts is a bench's reception as ledgers fill, which can move `speak`'s Ob
between 1 and 2 (§5b).

**Failure and ending.** There is no ending on this layer. The loop does not halt on one: `SeasonDriver.season` reads `world_q.endings_reached`
once a season as a report, and the realm as built reaches none (`loop/driver.py:515-518`; `queries/world_q.py:1764`; ERRATA G17 for the
deleted victory layer). A Failure spends the act and writes nothing; it emits a kind that witnesses may hold, except the inquiries'
`finding.none`, which is undeposited (ERRATA C8). There is no reroll in the season, no streak protection and no debt: the same act can be
formed next season at identical odds. The social roll kills nobody; a fight's season degree is its wound band (`seam/ladder.py:136-182`).

**Consequential versus cosmetic choices.**
- *Consequential:* which verb (its row decides what each band writes); speaking before a favourable bench (Ob 2 → 1 takes
  Partial-or-better from 26 % to 58 %); for `determine` and `argue`, Success against Partial (pursuits move only at Success or better).
- *Cosmetic to the odds:* who rolls (every pool is 2); minor or moderate advantage on the social path (quantised to nothing, Table B, and
  nobody can supply it while `leverage` is a literal 0.0); any Ob in (1, 2] (plays as 2); a hostile bench (clipped by the ceiling).
- *Against precedent:* BG3 and Disco place the consequential choice in the build and the party (T05 precedent, BG3 §7, Disco §7). Valoria
  as built has no build.

**[PROPOSED] (none of it executes).**
- Stored attributes through a domain faculty (J-T1 Option B), or a character template seating `capability` (§7), would be the first setup
  choice that moves the odds.
- One ladder from practice to dice (J-T6), so that pool, Ob and capability read from one source (§7).
- Complication as the modal band (ENP v2 proposal 6): the ruled ladder cannot deliver it at Ob ≥ 1 (§7).

## 1 The pieces

| term | what it is | numbers / limits | where it lives |
|---|---|---|---|
| **d10 pool** | the number of ten-sided dice rolled for one act | integer on the social path; floor 1D (`max(1, ...)`) | `engine/dice_engine/dice_engine.py:196-206` |
| **face value** | what one die contributes to the net | face 1 = −1; 2–6 = 0; 7–9 = +1; 10 = +2; no reroll chain | `dice_engine.py:150-161` |
| **TN (target number)** | the face that counts as a success | always 7; any other value raises `ValueError` (ED-IN-0196) | `dice_engine.py:182-193`; `sigma_leverage.py:91` |
| **per-die mean / spread** | expected value and standard deviation of one die | μ = 0.40, σ = 0.800 | `dice_engine.py:174-175` (duplicated at `sigma_leverage.py:78, :112-113`) |
| **net** | the sum of face values (plus any advantage boost) | integer from the discrete roll; fractional once a boost or the Gaussian path is used | `dice_engine.py:204`; `roll.py:124` |
| **obstacle (Ob)** | the number the net is compared against; "a varying difficulty is an Ob, not a TN" | any float; no single owner derives it (ED-IN-0202, suspended) | `dice_engine.py:178-179, :241-254` |
| **margin** | net − Ob | the only thing the ladder reads | `dice_engine.py:286` |
| **degree** | one of four ordered bands read off the margin | Failure < 0 ≤ Partial < 1 ≤ Success < 3 ≤ Overwhelming | `dice_engine.py:286-301` |
| **degree ordinal / label** | numeric (0–3) and Title-Case spellings of the degree | Failure 0, Partial 1, Success 2, Overwhelming 3 | `dice_engine.py:36-53` |
| **band extension** | a subsystem's optional veto that can only demote Overwhelming to Success (ED-SC-0032) | not passed on the season path | `dice_engine.py:95-138, :291-300`; `seam/ladder.py:251` |
| **Gaussian stand-in** ("continuous engine") | a normal draw with the pool's mean and spread, used instead of dealing dice | `gauss(0.40·N, 0.800·√N)`; accepts fractional N; returns 0.0 for N ≤ 0 | `dice_engine.py:209-224` |
| **`roll_net` / `roll_net_continuous`** | the two wrappers callers use | discrete: `max(1, int(round(N)))` (banker's rounding); continuous: `max(1.0, N)` | `sigma_leverage.py:286-296, :299-332` |
| **advantage (net sigma)** | an edge expressed in standard deviations of the roll | summed from named levels or supplied raw by a caller | `sigma_leverage.py:224-234` |
| **modifier levels** | named advantage sizes | minor 0.25, moderate 0.50, strong 0.75, major 1.00 ("Class B draft sim-seeds … NOT canonical") | `sigma_leverage.py:95-102` |
| **soft cap** | squashes summed advantage | `1.5·tanh(x/1.5)`; ceiling M_MAX = 1.5σ, never reached | `sigma_leverage.py:104, :141-148` |
| **net boost** (μ-shift) | the advantage converted to net successes and added to the roll | `soft_cap(x)·0.800·√max(1,N)` | `sigma_leverage.py:190-203` |
| **`p_success`** | closed-form P(net ≥ Ob) on the Gaussian stand-in | helper only; no season caller. On whole dice it understates Partial-or-better: 14.4 % against 26.0 % at pool 2 / Ob 2, 43.0 against 58.0 at pool 2 / Ob 1, 50.0 against 60.0 at pool 5 / Ob 2, so a surface that printed it would show worse odds than the dice deal | `sigma_leverage.py:246-279` |
| **`eff_ob`** | "DISPLAY ONLY" effective difficulty | not a resolution value | `sigma_leverage.py:169-177` |
| **OB_MIN** | the obstacle floor a room's favour cannot go below | 1 | `sigma_leverage.py:108`; read by `roll.py:105, :110` |
| **obstacle ceiling** | a cap on how hard a social matter can get (H-213) | shipped 2; swept 1/2/3, `None` = uncapped | `engine/season/data/fixtures.py:418-419`; `roll.py:107-113` |
| **room terms** | the bench's reception of a speaker and his unmirrored proofs, subtracted from Ob (`speak` only) | `reception_gain` 1.0, `proof_step` 0.25 | `fixtures.py:424-427`; `roll.py:104-105`; `sigma.py:179-183` |
| **forgery quality** | added to the Ob of an inquiry that examines a Record | 0 on a genuine document | `roll.py:106`; `sigma.py:184, :191` |
| **refusal rule (S27.4)** | an attempt at Ob > 2 × pool is refused and the attempt is spent | `obstacle_refusal_multiple` = 2 | `fixtures.py:396, :417`; `sigma.py:273-275`; `loop/resolve.py:978-997` |
| **capability** | a person's practice dict; the only per-person pool source | maps `tell`, `speak` → `copying`; empty on every realm person | `engine/season/rosters.yaml` `verb_capability` (`tell: "copying"`, `speak: "copying"`); `sigma.py:113-131` |
| **pool_default** | the stand-in pool when capability is absent (H-126) | 2 | `fixtures.py:414` |
| **seed / draw** | per-act random generator | `random.Random(int(H(world_seed, tick, actor, purpose), 16))`; purpose `roll:<prize>:<act id>` or `roll:<verb>:<act id>` | `engine/season/state/ids.py:16-21` (`H`), `draw` inside `draw_factory`; `loop/resolve.py:792, :852` |
| **scene / scene action** | acts are packed into scenes of up to 3 acts; the budget counts scene actions, and an extended scene (more than 1 act) costs 2 | budget `max(1, 5 + 1 per live hold − body bands − 1 per travel leg)`; at most 1 scene released per round over 5 rounds, so 7 acts at budget 5 and 9 at budget 6 | `fixtures.py:228, :488-489, :493-502`; `decision/budget.py:19-20, :57-61`; `loop/driver.py:456`; `loop/deliberate.py:89-97, :250-259` |

## 2 How it works

The steps below come in the order an act goes through them. The live path is the **social path**
(`loop/resolve.py::_contest` :731 and `_grade` :836 → `seam/wrappers/sigma.py::resolve` → `modules/social_contest/roll.py::roll` →
`seam/ladder.py::degree_of`). Combat and mass battle reuse the same ladder from inside their own modules (§6).

**Step 1: an act reaches the roll.** Only a verb whose row declares `contests:` (`tell`, `speak`, `argue`, `determine` on the social
path; `fight`, `accept`, `march` elsewhere), or one of the three `graded_inquiries` (`research`, `examine`, `surveil`,
`rosters.yaml:1141-1143`), rolls at all. Every other verb is deterministic.

**Step 2: the pool.** `pool = capability[VERB_CAPABILITY[verb]]` if the actor holds that key, else `pool_default` = 2
(`sigma.py:130-131`). Only `tell` and `speak` have a capability key (`copying`); `argue`, `determine` and the inquiries always take
the default. The pool is an `int` here, so a fractional pool cannot enter the social path.

**Step 3: the obstacle**, composed in one function (`roll.py:103-113`):

```
ob   = opposition / 2            if the subject is a person holding the same capability key
     = obstacle_default (2)      otherwise
room = reception_gain · reception + proof_step · proofs      (speak only; else 0)
ob   = max(ob − room, min(ob, 1))   if room > 0              (a favourable room cannot push below 1)
     = ob − room                    if room ≤ 0              (a hostile room raises it)
ob  += forgery_quality                                       (inquiries examining a Record)
ob   = min(ob, obstacle_ceiling = 2)
```

The last line matters most: under the shipped ceiling, nothing can make a social roll harder than Ob 2. Run on the function
itself, a reception of −3.0 gives Ob 2.0, and a reception of +1.0 or +5.0 gives Ob 1.0. An opposition score of 3 gives Ob 1.5, and a
score of 1 gives Ob 0.5; that composed Ob is not floored (`roll.py:80-82`).

**Step 4: the roll.** `net = roll_net(pool) + net_boost(leverage, pool)` (`roll.py:124`). `roll_net` deals `pool` real d10s with the
act's own generator and sums the face values. With `leverage = 0.0` the boost is exactly 0.

**Step 5: refusal (S27.4).** If `ob > 2 × max(pool, 0)` the provider discards the roll and returns `REFUSED` (`sigma.py:273-275`);
the loop folds it as the verb's refusal event (`loop/resolve.py:809-821`). The uncontested branch applies the same rule to a
hand-declared `Act.obstacle` (`resolve.py:980-997`), which the computed chooser never sets (comment at `:989`). With pool ≥ 1 and the
ceiling at 2, the derived pair is never refused (`sigma.py:239-241`); only a pool of 0 would be.

**Step 6: the degree.** `degree_of` sees `net` and `ob` in the result and calls `degree_from_net(net, ob)` with no extension
(`ladder.py:240-251`):

| margin = net − Ob | degree | what the band means (`dice_engine.py:234-238`) |
|---|---|---|
| < 0 | Failure | fell short |
| 0 to < 1 | Partial | the obstacle is met but not exceeded |
| 1 to < 3 | Success | cleared by at least one whole success |
| ≥ 3 | Overwhelming | "3 or more is always overwhelming", whatever the Ob |

**Step 7: the fold.** The verb's row picks `writes[degree]` and `emits[degree]` (`resolve.py:825`). The roll itself writes nothing.

**The Gaussian stand-in.** `continuous_engine_sample(N)` draws `gauss(0.40·N, 0.800·√N)` instead of dealing dice. It is what combat
uses (`modules/combat/core.py:60, :126`), and it is what `p_success` integrates. It is *not* equivalent at small pools. At pool 2 against
Ob 2 the dice give 74.0 / 19.0 / 7.0 / 0.0 % (F/P/S/O); the normal curve gives 85.6 / 11.9 / 2.6 / 0.0. At pool 5: 40.0 / 22.0 / 29.7 /
8.3 against 50.0 / 21.2 / 24.1 / 4.7. The docstring's "statistically equivalent to discrete" (`dice_engine.py:213`;
`sigma_leverage.py:302`) holds for mean and
variance, not for band odds at these sizes, because the face distribution is lumpy (half the faces score 0) and its right tail is
long (a 10 scores 2).

**Fractional pools and Ob.** The ladder accepts fractional operands with no epsilon (`dice_engine.py:241`). In practice:
- **Discrete path, fractional Ob:** the net is an integer, so Ob 1.5 behaves exactly as Ob 2 (Table A: identical rows at every pool).
  A fractional Ob rounds *up* in effect.
- **Discrete path, fractional pool:** rounded by `int(round(N))`: 1.5 → 2, 2.5 → 2, 3.5 → 4, 0.5 → 1 (banker's rounding, then the 1D
  floor).
- **Gaussian path, fractional pool:** kept fractional (`sigma_leverage.py:331`), floored at 1.0; pool 0.5 gives the same odds as pool 1.
- **Mass battle**, its own roller: the integer part rolls dice and the remainder is one extra die rolled with probability equal to the
  fraction (`modules/mass_battle/resolution.py:57-79`); no 1D floor, so a 0.5 pool rolls nothing half the time.

**Advantage as a mean shift.** Advantage never lowers Ob and never changes TN (`sigma_leverage.py:173-174, :255`). It adds
`soft_cap(x)·0.8·√N` to the net, so a given x moves the roll's z-score by the same amount at any pool size. The soft cap bends large
sums: 0.25 → 0.248, 0.5 → 0.482, 1.0 → 0.874, 1.5 → 1.142, 3.0 → 1.446, 10 → 1.500. Stacking past about 1.5σ buys almost nothing.

## 3 A worked example

**A real roll from the seeded realm** (`build_realm(0)`, season tick 0, captured by `t01_example.py`, §9).

`p_npc_086` tells `p_npc_010`. `tell` contests *a standing* against its `to` operand.
1. Pool: `p_npc_086.capability` is `{}`, so the pool is `pool_default` = 2.
2. Ob: `p_npc_010` holds no `copying` score, so the opposition is `None` and Ob = `obstacle_default` = 2. `tell` has no room
   (`heard_by` is absent from its prize row), so there are no room terms. The ceiling (2) does not bind. Ob = 2.0.
3. Generator: `random.Random(int(H(0, 0, "p_npc_086", "roll:a standing:762758bdca098db1"), 16))`. Re-deriving it from those four values
   alone reproduces the same two faces: **8 and 10**.
4. Net: 8 → +1, 10 → +2, so net = 3. Boost: `net_boost(0.0, 2)` = 0.
5. Refusal check: 2.0 > 2 × 2? No.
6. Margin 3 − 2 = 1, so the degree is **Success**.
7. Fold: `tell`'s row declares `news.told` and `confidence.broken` on Overwhelming, Success and Partial, and `writes: []` on every
   band. This act's log holds one degree-carrying event, `news.told` at Success. The told claim then travels through WITNESS.

In the same season, `p_npc_086`'s second `tell` (to `p_npc_007`) rolled 5 and 1: net 0 + (−1) = −1, margin −3, **Failure**,
`news.untold`. And `p_npc_041` spoke at `b_s_036_cathedral` before a bench whose reception of him was −0.529. The room term was
therefore −0.529 and raised Ob to 2.529, but the ceiling clipped it back to 2.0. He rolled 2 and 6 (net 0, margin −2): **Failure**,
`matter.turned`.

**The odds behind it.** At pool 2, net ≥ 2 needs {+1,+1} 9 %, {+2,0} 10 %, {+2,+1} 6 % or {+2,+2} 1 %, which totals 26 %. Net ≥ 3 is
{+2,+1} or {+2,+2}, 7 %, and net ≥ 5 is impossible. So F/P/S/O = **74 / 19 / 7 / 0 %**. Control: 200,000 calls of
`modules.social_contest.roll.roll` at the shipped fixture gave 74.10 / 18.94 / 6.96 / 0.00. Observed in the realm, seeds 0 and 1, two
seasons each: 133 social-path rolls, **every one at pool 2 and Ob 2**, with 99 Failure (74.4 %), 25 Partial, 9 Success and 0
Overwhelming.

**Table A: exact band odds, discrete d10 (the social path).** F / P / S / O in %. Ob 1.5 is omitted because it equals Ob 2 at every
pool (above). † = refused by S27.4 (Ob > 2 × pool).

| pool | Ob 1 | Ob 2 (and 1.5) | Ob 3 | Ob 4 |
|---|---|---|---|---|
| 1 | 60.0 / 30.0 / 10.0 / 0.0 | 90.0 / 10.0 / 0.0 / 0.0 | † | † |
| 2 | 42.0 / 32.0 / 25.0 / 1.0 | 74.0 / 19.0 / 7.0 / 0.0 | 93.0 / 6.0 / 1.0 / 0.0 | 99.0 / 1.0 / 0.0 / 0.0 |
| 3 | 31.8 / 28.2 / 34.8 / 5.2 | 60.0 / 22.8 / 16.2 / 1.0 | 82.8 / 12.0 / 5.1 / 0.1 | 94.8 / 4.2 / 1.0 / 0.0 |
| 4 | 25.1 / 23.8 / 39.3 / 11.9 | 48.8 / 23.2 / 24.2 / 3.8 | 72.1 / 16.1 / 11.0 / 0.9 | 88.1 / 8.1 / 3.7 / 0.1 |
| 5 | 20.2 / 19.8 / 40.2 / 19.8 | 40.0 / 22.0 / 29.7 / 8.3 | 62.0 / 18.2 / 17.0 / 2.8 | 80.2 / 11.5 / 7.6 / 0.7 |
| 6 | 16.5 / 16.5 / 38.9 / 28.1 | 33.0 / 20.0 / 32.8 / 14.2 | 53.0 / 18.8 / 22.2 / 5.9 | 71.9 / 14.0 / 12.2 / 2.0 |
| 7 | 13.6 / 13.8 / 36.3 / 36.3 | 27.4 / 17.9 / 33.9 / 20.8 | 45.3 / 18.5 / 26.0 / 10.2 | 63.7 / 15.5 / 16.6 / 4.3 |
| 8 | 11.3 / 11.5 / 33.3 / 43.9 | 22.8 / 15.7 / 33.6 / 27.8 | 38.6 / 17.5 / 28.5 / 15.4 | 56.1 / 16.1 / 20.4 / 7.4 |

Rules of thumb that fall out of the table:
- One point of Ob costs about two and a half to three dice. Pool 2 at Ob 1 has Partial-or-better 58 %, against 60 % for pool 5 at Ob 2;
  pool 4 at Ob 2 has 51.2 %, against 54.7 % for pool 7 at Ob 3. Each die adds only 0.4 to the mean.
- On integers, "Partial or better at Ob k" equals "Success or better at Ob k − 1".
- Under the shipped ceiling, the Ob 3 and Ob 4 columns cannot occur on the social path.
- Against the common shapes: one whole Ob step moves Partial-or-better by up to 32.0 points at pool 2 (28.2 at pool 3, 22.0 at pool 5),
  against 5.0 on a d20 and at most 16.7 on 2d6. The pool-2 net has mean 0.8 and SD 1.131 over a range of 6 (SD ÷ range 0.189, near 3d6's
  0.197): a bell, so what a modifier is worth depends on where the Ob sits. [precedent: BG3 gives a flat 5 points per +1 on a d20, and
  Disco's 2d6 is the 16.7 case (`research/game_precedent_suite/tables/R4_combat_social_rpgs.md`, BG3 and Disco bullets). The Valoria
  figures are exact enumeration of `_die_result` (`dice_engine.py:153-161`) banded by `degree_from_net` (`:286-301`).]

**Table B: what advantage does on the social path** (discrete roll + `net_boost`), P(Success or better) in %. The boost is shown in
brackets for pool 2 / 4 / 8.

| x (σ) | boost at pools 2 / 4 / 8 | Ob 1: pools 1 / 2 / 4 / 8 | Ob 2: pools 1 / 2 / 4 / 8 | Ob 3: pools 2 / 4 / 8 |
|---|---|---|---|---|
| 0 | 0 / 0 / 0 | 10.0 / 26.0 / 51.2 / 77.2 | 0.0 / 7.0 / 27.9 / 61.4 | 1.0 / 11.9 / 43.9 |
| 0.25 minor | 0.28 / 0.40 / 0.56 | 10.0 / 26.0 / 51.2 / 77.2 | 0.0 / 7.0 / 27.9 / 61.4 | 1.0 / 11.9 / 43.9 |
| 0.50 moderate | 0.55 / 0.77 / 1.09 | 10.0 / 26.0 / 51.2 / **88.7** | 0.0 / 7.0 / 27.9 / **77.2** | 1.0 / 11.9 / **61.4** |
| 0.75 strong | 0.78 / 1.11 / 1.57 | 10.0 / 26.0 / **74.9** / 88.7 | 0.0 / 7.0 / **51.2** / 77.2 | 1.0 / **27.9** / 61.4 |
| 1.00 major | 0.99 / 1.40 / 1.98 | 10.0 / 26.0 / 74.9 / 88.7 | 0.0 / 7.0 / 51.2 / 77.2 | 1.0 / 27.9 / 61.4 |
| 1.5 (two levels stacked) | 1.29 / 1.83 / 2.59 | 10.0 / **58.0** / 74.9 / 95.4 | 0.0 / **26.0** / 51.2 / 88.7 | **7.0** / 27.9 / 77.2 |

Because the dice net is an integer and the Ob is an integer, a boost changes nothing until it carries the net across a whole step:
`net + b ≥ k` only when `b ≥ k − net`. So on the social path, **advantage is quantised into whole successes**. Minor (0.25σ) does
nothing at any pool up to 8. Major (1.0σ) gives a pool-2 actor a boost of 0.989, just short of 1, and so also does nothing. At pool 1
the boost never exceeds 1.2, and it reaches 1 only at x ≈ 1.8σ. Below that, no advantage moves a pool-1 band at all; at x = 3.0
(boost 1.157), Ob 2 Success rises from 0 to 10 %. Against a
fractional Ob the steps fall in different places (a boost of 0.5 against Ob 1.5 is a full step). On the Gaussian path, where combat
rolls, the same levels act smoothly. At Ob 2, P(Success+) for x = 0 / 0.25 / 0.5 / 0.75 / 1.0 is 2.6 / 4.5 / 7.2 / 10.5 / 14.2 % at
pool 2, and 19.1 / 26.5 / 34.7 / 42.8 / 50.0 % at pool 4.

## 4 What you can do

The dice engine has no verbs of its own. These are the verbs that reach it, read from `engine/season/verb_table.yaml`.

**What an act costs.** `budget()` returns **scene actions** (`decision/budget.py:19-20`):
`max(1, 5 + 1 per live hold − body bands − 1 per travel leg)` (`:57-61`). A `hold` is a holding Tenure: a seat, a landholding, or a
held Record or Proposition.
- Acts are packed into scenes. A scene holds up to `interactions_per_scene` = 3 acts (`fixtures.py:488`); one holding more than one
  act is *extended* and costs `extended_scene_cost` = 2 (`:489`).
- The driver runs 5 rounds (`loop/driver.py:456`). In each round it releases at most one scene per person, charging that scene's cost
  against the budget (`loop/deliberate.py:250-259`).
- So a budget of 5 releases 2 + 2 + 1 = 7 acts, and a budget of 6 releases 9.
- The tree disagrees with itself on spendability. `deliberate.py:89-97` says a sixth scene is unspendable; `fixtures.py:493-502`
  makes the budget a cost budget, so an extended scene stays affordable. Read both before relying on either.
- On the basis of `d.resolved`, seed 0 resolved 1,132 acts in 2 seasons, about 7.6 per person-season.
- A contested act uses up its place whether it succeeds, fails or is refused. S27.4 calls this "the season is spent"
  (`resolve.py:978`).

**Who may, and what is required.** "Who may" is the row's `eligibility`, a disjunction:
- `own` admits every person (`loop/resolve.py`, `_eligible`, `kind == "own"` returns True).
- `presence:<…>` never admits today (H-75), so an inquiry's eligibility is in effect `own`.
- The admission test is the row's **typed cell** (`requires_typed`), not its prose `requires:` string. The column below gives the
  typed cell, and names any half of the prose that is not typed.

| verb | contests / route | who may | requires (typed cell) | pool | Ob | F / P / S / O | writes |
|---|---|---|---|---|---|---|---|
| `tell` | *a standing*, against `to` | `own` (anyone) | `own_ledger` on the subject (`holds`) AND `to` is `with` the teller (`hearer`) | `copying` or 2 | hearer's `copying`/2, else 2; ≤ 2 | `news.untold` / `news.told` (P, S, O alike); `confidence.broken` is declared on P/S/O but emitted only when the telling breaks a confidence circle, and at the shipped `telling_privacy` 0 "no claim holds a circle" (`resolve.py:586-587`; `fixtures.py:853`) | nothing |
| `speak` | *a matter*, heard by the bench | `own` | `existence` of the subject as a `DocketItem`, and nothing else. The prose's "live occasion at the actor's venue" half is not in the typed cell (`verb_table.yaml:1072-1077`) | `copying` or 2 | 2 − room, floor 1; ≤ 2 | `matter.turned` / `.held` / `.advanced` / `.carried` | nothing |
| `argue` | *a proposition*, against `to` | `own` | `existence` of the subject as a `Proposition` AND `to` is `with` the arguer | 2 | 2 | `argument.lost` / `argument.won` / `.won`+`pursuit.moved` (S, O) | S, O: `Person.pursuits` |
| `determine` | *a proposition*, against `subject` | `remit:determine` (an office) | four conjuncts: `party` (subject is a Person), `docket` (a DocketItem), `bench` (the `bench` basis), `quorum` (`bench.size` threshold). The prose's "fired Date" is not typed (`verb_table.yaml:322-341`) | 2 | 2 | `matter.undetermined` / `matter.determined` / `+pursuit.moved` (S, O) | P: `Tenure.since`, `DocketItem.matter`, `Tenure.degree`; S, O add `Person.pursuits` |
| `research` | graded inquiry, no prize | `own` (the `presence:<site>` alternative never admits) | `existence` of the subject as a `Record`; no presence clause | 2 | 2 (+ forgery quality); ≤ 2 | `finding.none` / `finding.made` (P, S, O alike) | nothing |
| `examine` | graded inquiry | `own` (as above) | `existence` of the site as a `Site` AND the actor is `present_at` it | 2 | 2; ≤ 2 | as `research` | nothing |
| `surveil` | graded inquiry | `own` (as above) | `existence` of the subject as a `Rung` AND the actor is `present_at` it | 2 | 2; ≤ 2 | as `research` | nothing |
| `fight`, `accept` | *the body* | see the combat tutorial | — | combat's own (`max(5, history+6)`) | defender history / 2 | season reads wound bands (Felled / Wounded / Untouched), not this ladder | combat's |
| `march` | *a field* | see the mass-battle tutorial | — | mass battle's own | its own | Won / Lost / Unopposed | mass battle's |

Refusals: `tell` → `news.untold` (the same kind as its Failure); `speak` → `speech.unheard`; `argue` → `argument.refused`; `determine` →
`determine.refused`; the inquiries → `finding.none` (the same kind as their Failure). An S27.4 refusal takes the verb's refusal kind
(`resolve.py:809-821`).

What a degree means in play beyond the table: at Partial, WITNESS may copy a told claim lossily (`loop/witness.py:136-139`), so a
Partial `tell` delivers the news but perhaps not intact. A Partial `determine` opens its disposal graded `Partial`
(`verb_table.yaml:353`). For `research`, `examine` and `surveil`, Partial and better are indistinguishable in what they emit.

**What executes** (control run, `build_realm`, 2 seasons, from the `ctl/` files). Each entry is `attempted/ok` per seed 0 / 1 / 2.
- "attempted" means the act reached `_fold`. `d.resolved` is appended there (`loop/resolve.py:377-379`), and an act refused at
  admission `continue`s before it (`:1025-1032`). For these verbs, then, "attempted" = admitted and rolled.
- "ok" means at least one non-refusal event.
- Acts refused at admission still emit their refusal kind and stay in the act store: seed 0 holds 275 acts beyond `d.resolved` (1,407
  against 1,132; seed 1 1,394 against 1,122; seed 2 1,447 against 1,175), among them `research` 111, `examine` 62, `surveil` 21, `speak`
  19 and `argue` 10. Nineteen of the 275 are `act.ineligible`, an actor a predecessor act removed (`resolve.py:61-91`). Counted as
  `w.acts` against `d.resolved`, re-run on seeds 0/1/2 at `51d7b05`.

| verb | seed 0 | seed 1 | seed 2 | notes |
|---|---|---|---|---|
| `tell` | 23/4 | 25/7 | 19/6 | |
| `surveil` | 30/5 | 29/9 | 22/5 | |
| `research` | 14/7 | 8/1 | 4/2 | |
| `speak` | 3/3 | 0/0 | 2/2 | all three seed-0 speeches were Failures: `matter.turned` is not a refusal kind |
| `determine` | 0/0 | 1/1 | 0/0 | runs at seed 1 only |
| `argue` | 0/0 | 0/0 | 0/0 | formed and stopped before the roll 10 / 17 / 18 times: `argument.refused` 10 / 17 / 15, and 3 `act.ineligible` in seed 2 |
| `examine` | 0/0 | 0/0 | 0/0 | formed by the chooser but never passing admission (CROSS C2; measured in round 3: 62 / 59 / 39 formed, none reaching the roll) |

Cohort persons (`cohort_set_s_*`) roll inquiries as well as named persons.

## 5 Pursuing goals here

**(a) Goals and how the code represents them.** The goal in this subsystem is always the same: land a degree high enough for the verb's
row to write or emit what you want. Success or better moves pursuits on `argue` and `determine`; Partial or better delivers a `tell` or
makes a finding; each `speak` band moves the matter differently. The code represents the goal only as the degree token the fold keys on.
Nothing records a target degree, and the chooser does not read odds: no `p_success`, obstacle or odds term appears anywhere in
`engine/season/decision/` (grep, §9). The chooser picks by the verb's alignment with the person's values and stance
(`decision/choose.py:149`, per D06 §4.6), and the dice then decide. Nor would a seated player see them: no surface shows a chance
(overview §7), and the per-act draws carry no streak memory of any kind (`state/ids.py:16-21, :87-89`: the generator is seeded from
`(world_seed, tick, actor, purpose)` alone; contrast BG3's Karmic Dice [V3] and XCOM's aim assist [V3, with [CONTESTED] refinements]:
`research/game_precedent_suite/tutorials/T05_social_rpgs.md`, BG3 §7-§8, and `T18_repo_strategy_b.md`, XCOM §7), so realised odds
equal Table A.

**(b) The levers, as the code lets anyone pull them today.** These are the three ways to raise the odds, and their current state.

| lever | mechanism | what it does at pool 2 | can anyone pull it today? |
|---|---|---|---|
| **More dice** | hold the verb's capability key (`copying` for `tell`/`speak`) at a value above 2 | pool 3: Partial+ 26 → 40 %, Success+ 7 → 17 %; pool 5: 60 / 38 % | **No** in the realm: `capability` is empty on 74 of 74 (seed 0) and 77 of 77 (seed 1) persons. `train` raises a key only if the pupil already holds it (`verb_table.yaml:1468`) and was refused 38 of 38 times in seed 0. The one corpus person with a key is `NPC-088`, `{copying: 3}`, through a case overlay; in the realm, `p_npc_088` has none. |
| **Lower the Ob with the room** (`speak` only) | the bench's `reception` of you, plus 0.25 per unmirrored proof against your opponent, subtracted from 2, floor 1 | Ob 1: Partial+ 26 → 58 %, Success+ 7 → 26 %, Overwhelming 0 → 1 % | **In principle.** Reception comes from deeds of yours the bench holds and values (`queries/world_q.py:546-600`, docstring). It saturates at +1 (Ob cannot go below 1). Four unmirrored proofs (4 × 0.25) do the same. In seed 0's three speeches, reception was −0.529, −0.048 and 0.0, so the room only worked against the speaker, and the ceiling cancelled that. |
| **Lower the Ob through the opponent** | Ob = opponent's score / 2 when he holds the key | a hearer with `copying` 2 gives Ob 1, the same gain as a good room | **No**: nobody holds a key. |
| **Advantage** | `leverage` → `net_boost` | at pool 2, nothing below 1.015σ net (the first x whose boost reaches 1); 1.5σ gives Ob 2 Success+ 7 → 26 % | **No**: `leverage=0.0` is a literal in `sigma.py:191`, with "zero until something supplies leverage" (:160-162). |

**A play that works today: speak before a friendly bench.** (1) Earn deeds the bench values, and let them be witnessed, so their ledgers
hold claims about you. (2) Gather claims against your opponent that he does not hold in return (proofs). (3) Speak on a docketed
matter at that venue. If reception plus 0.25 × proofs reaches 1, your Ob is 1 instead of 2 and your Partial-or-better odds go from 26 %
to 58 %. Nothing else in the code moves a social roll's odds for a person today.

**(c) Costs, risks, counter-play, blocks.**
- Every attempt uses up its act in a scene. A refusal or a Failure uses it up exactly as a Success does, and there is no reroll in
  the same season.
- What Failure costs: `determine` leaves the matter on the docket; `tell` deposits nothing; an inquiry deposits no claim
  (`test_fi01_graded_inquiries.py::test_a_failed_inquiry_deposits_no_claim_and_news_untold_still_does`, name only).
- Counter-play is nearly absent on the dice. A defender cannot raise your Ob above 2 (the ceiling). A hostile bench raises it only above
  2, where the ceiling cuts it back. A hearer with a high `copying` score would compute Ob = score/2 > 2 and be capped too.
- The only way an opponent hurts your odds is by mirroring your proofs: each proof he holds back about you cancels one of yours
  (`world_q.py:606-633`, docstring).
- Blocks: the S27.4 refusal cannot bind while pool ≥ 1 and the ceiling is 2. What blocks an act in practice is its typed cell (`requires_typed`)
  and its eligibility, not the dice.

**(d) What the mechanics structurally reward or punish.**
- With every pool at 2 and every Ob at 2, Overwhelming is unreachable: it needs net 5, and two dice give at most 4. So `speak`'s
  `matter.carried` and any Overwhelming-only write cannot occur except before a favourable room (1 % at Ob 1).
- For `tell` and the inquiries only "Partial or better" matters (26 %). For `argue` and `determine` only Success or better moves
  pursuits (7 %).
- Advantage below one whole step is wasted on the social path (Table B). A "minor" or "moderate" edge on a small pool is a dominated
  option if anyone ever spends a cost to get it.
- Ob 1.5 is no easier than Ob 2 on whole dice. A half-point of room favour buys nothing; a whole point buys the full gain.
- Opposition by score/2 means a hearer who holds `copying` at 1 or 2 is *easier* to tell (Ob 0.5 or 1) than one who holds no key
  (Ob 2). A score of 3 gives Ob 1.5, which plays as Ob 2 on whole dice; at 4 or more the ceiling holds Ob at 2. Ob 0.5 plays as Ob 1:
  Partial or better needs net ≥ 1, 58 % at pool 2. Today nobody holds the key, so this does not arise.
- The middle band is narrow by ruling. Partial is "met but not exceeded" (ED-IN-0187; `dice_engine.py:238, :286-301`): 19 % at the
  shipped pair, and never the most likely band at any pool 1–8 against Ob 1–4 (largest: 32 % at pool 2, Ob 1). PbtA's 7–9 band and
  Blades' 4–5 band sit at 41–45 % across the competent range (recomputed here: PbtA 41.7 / 44.4 / 41.7 % at +0 / +1 / +2 on 2d6;
  Blades 44.4 / 45.4 / 42.0 % at 2 / 3 / 4 dice; the repo records the figure at `research/by_lane/IN_infrastructure.md:145` as
  "arithmetic, corpus unverified"). On the social path the typical outcome is Failure, which writes nothing, not a complication.

**(e) What success leaves in the world.** The roll writes nothing. What the degree leaves comes from the verb row: events (`news.told`,
`finding.made`, `matter.determined`...), which WITNESS turns into claims in observers' ledgers; and for `argue`/`determine` at Success
or better, `Person.pursuits`; for `determine` at Partial or better, an opened Tenure graded with the degree (`Tenure.degree`). The
degree also rides on the Event (`Event.degree`, `state/carriers.py:260`).

## 6 How it connects

- **Social contest.** The live social path *is* this subsystem with a host builder in front: the one roll per act, with no rounds. The
  multi-exchange kernel in `systems/social_contest/sim/contest/` uses the same `roll_net`, `net_boost` and ladder, plus a
  pool-desaturation band extension. It is not called by the season (`roll.py:16-37`, "KEEP THIS ROLL, DO NOT ADOPT THE KERNEL").
- **Personal combat.** `fight`/`accept` route to `modules/combat`. Inside a fight every exchange rolls the Gaussian path with
  `net = roll_net_continuous(pool) + soft_cap(net_sigma)·sigma_n(pool)` against `ob_from_defender = history / 2`
  (`core.py:100-127`, called from `wrapper.py:182, :213, :307`). The pool is `max(5, history + 6)` (`core.py:51-56`), so combat pools are
  never below 5. Combat composes `net_sigma` from its own terms (wounds, armour and so on), so advantage *is* live inside a fight. The
  season reads the fight's outcome off wound bands, not off this ladder (`ladder.py`, `combat_degree`). Combat also carries a deliberate
  override of its own odds: `UPSET_FLOOR` = 0.05 (`modules/combat/config.py:295`, "DESIGNER RULE — Jordan", ED-PC-0036) makes the
  decided loser the `winner` with probability 0.05 (`modules/combat/wrapper.py:526-529`). The season reads the wound bands, never
  `result` (`seam/ladder.py:141, :155`), so the flip does not reach the fold (H-119, `engine/season/hole_register.yaml:2393`: the
  reported winner is the felled fighter in 6.06 % of 300 seeded fights). The social path has no fixed floor, but its pass/fail line is
  never certain at a pair S27.4 admits: the refusal (Ob > 2 × pool, `sigma.py:273`) removes exactly the pairs above the dice's maximum
  net (2 × pool, all tens), so Partial-or-better is at least 0.1^pool (1 % at pool 2 / Ob 4, Table A) and Failure is never 0 at Ob > 0.
  Its certain zeros are in the upper bands: pool 2 / Ob 2 can never be Overwhelming, and pool 1 / Ob 2 can never reach Success. The
  floor is 5 % in combat (on `winner` only, above) and 0.1^pool here, so the "no matchup is certain" guarantee differs by resolver. [precedent:
  BG3's natural 1 and natural 20 on attacks and ability checks, and Disco's snake-eyes rule (no active check above 97.2 % or below
  2.8 %), keep a check short of certain; `research/game_precedent_suite/tables/R4_combat_social_rpgs.md`.]
- **Mass battle.** `march` resolves at ENCOUNTER through `modules/mass_battle/resolution.py`, which copies the face rule, the 0.800
  spread and the ladder (with a 1e-9 epsilon) rather than importing them. Two guard tests hold the copies equal:
  `tests/valoria/test_degree_ladder_single_owner.py` the ladder (per `resolution.py:104-112`), and
  `tests/valoria/test_tn7_always.py::test_the_mass_battle_roller_uses_the_same_face_window` (`:95`) the face rule. The per-die μ/σ
  literals are typed in five files (`dice_engine.py:174-175`, `sigma_leverage.py:78, :112-113`, `modules/mass_battle/resolution.py:227`
  for σ, `modules/mass_battle/config.py:306` for μ, `engine/reference/contest-groundup/engine.py:35`), plus the oracle copy
  `tests/sim/v32-combat-balance/m1_dice_sigma_core.py:28`. Only the engine pair is pinned (`test_tn7_always.py:172-179` asserts
  0.40 / 0.800 in `dice_engine` and `sigma_leverage.PER_DIE`); neither mass-battle copy is guarded. No test pins the mass-battle σ
  magnitude (`test_degree_boundary_epsilon.py:158-165` checks sign and zero only), and its μ is checked by `pytest.approx(0.4)`
  (`tests/valoria/test_fractional_pool.py:31`). The season grades the field Won / Lost / Unopposed.
- **Fieldwork.** The three graded inquiries roll here (§4); `forgery_quality` from an examined Record is their one Ob modifier, and it
  is inert under the ceiling.
- **Witness.** It reads the degree: a Partial `tell` can be copied lossily (`witness.py:136-139`).
- **Seeding.** Every roll has its own generator keyed `(world_seed, tick, actor, purpose)`, so adding a verb or reordering acts
  never moves another act's dice. The same seed gives the same faces; §3's faces were re-derived from the four keys alone.
- **Combinations.** The one composition that works today is the room (§5b): witnessing feeds reception, and reception lowers `speak`'s
  Ob. Proofs connect fieldwork (claims gathered) to the social roll.

## 7 Playing it as proposed

Everything in this section is **[PROPOSED]**: none of it executes.

- **[PROPOSED] Stored attributes feed the pool through a domain faculty.** Option B of J-T1 (verbs-01 §I.5, D03 §4.5–4.6) stores ten
  attributes (1–7: STR AGI END FOC ACU WIL ATT CHA BON, plus Thread Sensitivity on its own 0–100 scale) on `Person.attributes` (K-2).
  A `faculty(domain)` in each resolver's module would blend the domain's attributes with practice. Under V-2, attributes reach only
  rows declaring `contests:`. You would then raise your social odds by being innately able, as well as by practice. *Waits on:* J-T1,
  J-T2 (the tenth), J-T4 (do attributes change; recommended none), V-2a (gates and caps), all Jordan's. The proposal's own falsifier B6
  is combat (`fight`), not the social roll (D06 §4.2).
- **[PROPOSED] A character template seats practice at world-gen.** `characters.yaml` + `cast.template_of` + `seat_template` write
  `capability` (B1–B3, gated by nothing; D03 §4.3, D06 §4.2). That would be the first lawful way for a realm person to start with more
  than 2 dice. Template probe 4: `tell`'s pool is 2 with `{}` and 5 with `{copying: 5}` (D03 §5). A minted key below 2 would *lower* a
  pool, which is why `train` refuses to mint (`verb_table.yaml:1468`).
- **[PROPOSED] One ladder from practice to dice (J-T6).** Today the sigma pool is the capability value; combat uses `max(5, history+6)`;
  threadwork uses `min(3, history+3)` (D03 §6; G20 TW-G26/27). This is named as an S defect, not decided, and rides with J-13's scale
  remainder.
- **[PROPOSED] Per-person capacity in combat and mass battle (JQ-2, J-13 remainder).** Whether "pool only" reaches those scales;
  "ASK; not answered" (D01 §5).
- **[PROPOSED] Social obstacle terms.** The SC lexicon proposes several (L11 lines 135-145, 247): `tell`'s Ob reading the *teller's*
  standing (SC-G21, open); manners whose Ob reads the hearer's held claims (`reason`) or regard (`appeal`); `refute` raising the
  opponent's Ob. In FI, a concealer's score would set an inquiry's Ob (FI-G16, lands with `conceal`), and investigators would come to
  differ (FI-G14, folded into J-T1/J-T2).
- **[PROPOSED] One Ob owner (ED-IN-0202).** The ruling "score/2 plus whatever specific modifiers" is not implemented by a single
  derivation; the reconciliation is "SUSPENDED by Jordan (2026-08-21)" (`dice_engine.py:241-254`).
- **[PROPOSED] Per-die literals owned once (REM-42).** `sigma_leverage.py` would alias `dice_engine.py`'s μ/σ instead of retyping them
  (D02, remediation RB-4a). This is behaviour-neutral.
- **No proposal I read names a producer for `leverage`.** Advantage on the social path stays at 0 until one exists.
- **[PROPOSED] Complication as the modal band** (ENP v2 proposal 6, `proposals/2026-09-12-emergent-narrative-primitives-v2/01_THE_TEN.md:293-336`,
  held back). It pairs a capability producer with an open design call. Under the ruled ladder no pool and no fixture makes Partial modal
  at Ob ≥ `OB_MIN` (1): none of pools 1–40 against every whole Ob from 1 to 2 × pool does (largest Partial share 32 %, pool 2 / Ob 1,
  exact enumeration). The only modal-Partial cell is pool 1 at Ob 0 (50 %), below the floor; `roll.py:80-82` leaves a composed Ob
  unfloored. A modal Partial would need a wider band, which is the ladder's ruling (ED-IN-0187), not a fixture.

**Stubbed, inert at shipped defaults, or never firing in the realm run:**

| element | state | evidence |
|---|---|---|
| social `leverage` / `net_boost` | literal 0.0 | `sigma.py:191` |
| S27.4 refusal on the derived pair | wired; cannot fire with pool ≥ 1 under ceiling 2 | `sigma.py:239-241`; probe `A38` (`harness/probes.py:2783`) exercises it with a hand-built act |
| S27.4 on a hand-declared `Act.obstacle` | wired; the computed chooser never sets one | `resolve.py:980-997` |
| fractional Ob | reachable via room or opposition; 0 of 133 realm rolls had Ob ≠ 2 | §9 probe |
| `forgery_quality` | added, then cut by the ceiling; 0.0 on all 133 rolls | `roll.py:96-102`; §9 probe |
| band extension (`PoolDesaturation`) | not passed by the season | `ladder.py:251` |
| `p_success`, `eff_ob`, `LEVEL_SIGMA`, `levels_to_net_sigma` | no season caller | C01 §8; grep of `engine/season/decision/` |
| capability-based pools | 0 persons with a key in the realm | §9 probe; `ctl/` files |

## 8 Common mistakes and traps

1. **"A fractional Ob is a finer difficulty."** Not on the social path: whole dice give an integer net, so any Ob in (k−1, k] plays
   as Ob k. Ob 1.5 = Ob 2 in every row of Table A. Fractional Ob is only fine-grained on the Gaussian path (combat).
2. **"Minor advantage helps a little."** On the social path a boost moves odds only when it crosses a whole success. A minor 0.25σ
   never does at pools 1–8, and major 1.0σ does not at pool 2 (boost 0.989).
3. **"The Gaussian stand-in is the same game."** Mean and variance match; band odds do not at small pools. P(Partial+) at pool 2 / Ob 2
   is 26 % on dice and 14.4 % on the curve. The H-213 justification "p_success 0.0006 at Ob 3" at 1D (`fixtures.py:418`, `roll.py:74-75`)
   is a Gaussian figure; on real dice that pair is exactly 0 and is refused by S27.4 (Ob 3 > 2 × 1).
4. **"Advantage lowers the obstacle."** It never does (`sigma_leverage.py:173-174, :255`). `eff_ob` is display only.
5. **The draft says "a pool-2 contest cannot reach Overwhelming"** (A1 §1.2, after C01 §4.4). That is true at Ob ≥ 2 only. At Ob 1,
   which `speak`'s room can reach, two 10s give net 4, margin 3: Overwhelming, 1 %.
6. **The draft's "every social roll is a 2-die pool against Ob 2, failing 74 %"** (overview §1 point 4) is **confirmed**: 133 of 133
   rolls in seeds 0–1 were pool 2 / Ob 2, with 74.4 % Failure against 74.0 % exact.
7. **A hostile bench is not a harder roll.** Its negative reception raises Ob above 2, and the ceiling cuts it back (seed 0, `p_npc_041`:
   reception −0.529, Ob 2.0).
8. **Counting `finding.none` or `news.untold` as Failures overcounts them.** These kinds are also the refusal kinds of the inquiries and
   of `tell`. An admission refusal never reaches `_fold`, so it is absent from the `ctl/` counts altogether (§4). Inside those
   counts, "ok" equals Partial-or-better only where the Failure kind is a refusal-looking kind (`news.untold`, `finding.none`,
   `matter.undetermined`). For `speak` (`matter.turned`) and `argue` (`argument.lost`) a Failure counts as "ok".
9. **Stale paths.** `CLAUDE.md` §5 cites `engine/autoload/dice_engine.py`; the directory does not exist (the owner is
   `engine/dice_engine/dice_engine.py`). D05 cites `sigma._obstacle_of` (:112); that site was deleted at SC-01 step 14
   (`sigma.py:137-141`), and the obstacle is `roll.py::obstacle`'s.
10. **Stale docstring in mass battle.** `roll_pool_fractional` says `compute_degree` "thresholds at `net<=0`"
    (`resolution.py:63-64`); the function now reads the margin with an epsilon (`:116-119`). Likewise `roll_pool`'s own comment says the volley path
    "hand-rolls its own d10 loop" (`resolution.py:43-45`); `_roll_volley_pool` now delegates to `roll_pool` (`orchestration.py:1565-1574`).
11. **Status labels disagree.** `LEVEL_SIGMA` is headed "NOT canonical" while each line is tagged `[canonical: …]`
    (`sigma_leverage.py:95-101`). The package `__init__` says PROVISIONAL while both modules say CANONICAL (C01 §2).
12. **Two pool floors.** The roll floors the pool at 1D, but S27.4 reads the unfloored pool (`max(pool, 0)`), so a pool-0 act would be
    rolled with one die and then refused (`sigma.py:264-275`). The discrete wrapper rounds half to even (2.5 → 2), and the Gaussian
    wrapper keeps fractions.
13. **TN is not a dial.** Any `tn` other than 7 raises; every difficulty is an Ob.
14. **Combat's labels are lower-case** (`'fail'`, `'partial'`...), a relabel of the same ladder (`core.py:63-74`). The season grades
    fights by wound band in any case.

**Where the draft appendix (A1 §1, overview §2.2) was wrong or loose, and what this tutorial uses instead:**

15. **"THE degree ladder … for every scale"** is the docstring's promise (`dice_engine.py:229`), not what the season reads. The season
    reads `degree_from_net` only for the social path and the graded inquiries. Combat's season degree is the wound band, the field's
    is Won / Lost / Unopposed, and mass battle keeps its own copy of the ladder (ERRATA G5; `ladder.py:218-259`). Combat does call the
    owner ladder per exchange internally (`core.py:65-74`), but that degree never reaches the fold.
16. **Scene budget.** The draft's "scene budget 5 per season" (overview §2.1) omits the +1 per live `hold`, the `max(1, …)` floor,
    extended-scene pricing and the in-tree dispute over a sixth scene. The budget counts scene actions; budget 5 releases about 7 acts
    (CROSS C1; §4 above).
17. **Grades.** The draft graded by reachability ("the season loop reaches it"). Under G1, the room terms are RUNS-IN-LOOP at control,
    and `p_success`, `eff_ob`, `LEVEL_SIGMA` and the S27.4 gate are TESTS-ONLY. A refusal that never fires, or an advantage that is
    always zero, is not a running mechanic (§0).
18. **Counts.** Every execution count here is from `ctl/realm_seed{0,1,2}_2seasons.txt` or this tutorial's own probe (§9), never from
    the draft's A2 §C.3 table, which counted differently (ERRATA G2: e.g. its research 125 and examine 62 attempted, against ctl's
    research 14 and examine 0 in seed 0). `argue` never reaches the roll in any seed, though it is formed and stopped 10 / 17 / 18 times (`argument.refused` 10 / 17 / 15, plus 3 `act.ineligible` in seed 2); `determine` reaches the roll once (seed 1) and is refused 2 / 5 / 2 times.

**§8 Round-2 corrections** (each cited line re-opened before accepting it):

- **R2-1 (F1, C2, X19).** The ctl columns are relabelled `attempted/ok` in one order, with "attempted" defined as "reached `_fold`"
  (`resolve.py:377-379`, `:1025-1032`, opened). Every count is given per seed.
  *Partly disputed:* C2 and F1 say "ok" = Partial-or-better for contested verbs. That holds for `tell`, the inquiries and `determine`,
  but not for `speak` or `argue`, whose Failure kinds are not in the ctl refusal list. Seed 0's `speak` 3/3 were three Failures
  (§3, my probe). See item 8.
- **R2-2 (F2).** "`copying` 1–3 is easier" was wrong. Only scores 1–2 are easier (Ob 0.5–1); 3 gives Ob 1.5, which plays as Ob 2.
  Corrected in §5d.
- **R2-3 (F3, X3, CROSS C10).** §4's "requires" column now teaches the typed cell. `speak` types only the DocketItem existence; its
  venue half is untyped (`verb_table.yaml:1072-1077`). `determine` types party/docket/bench/quorum, and its "fired Date" is untyped
  (`:322-341`). `tell`, `argue` and the inquiries were checked by loading `requires_typed`. `research` has no presence clause.
- **R2-4 (F8, CROSS C1).** "The driver releases at most 5" is replaced by the cost-budget account, citing both readings
  (`deliberate.py:89-97` and `fixtures.py:493-502`). `budget.py:19-20`, `fixtures.py:488-489`, `driver.py:456` and
  `deliberate.py:250-259` were opened. The frame sentence and the §1 "scene" row were changed to match.
- **R2-5 (F13).** `confidence.broken` is declared on `tell`'s P/S/O but never emitted at the shipped `telling_privacy` 0
  (`resolve.py:586-587`: "no claim holds a circle, so this is False for every act"; `fixtures.py:853`).
- **R2-6 (X13).** Eligibility is a disjunction. `own` admits everyone, and `presence:<…>` never admits (H-75; `resolve.py`,
  `_eligible`, opened). The inquiries' "who may" therefore reads `own`. For `examine` and `surveil`, presence is enforced by the
  typed cell's `present_at`, not by eligibility.

### Round-3 corrections

Each cited line was re-opened at `51d7b05`. Where the precedent-suite disposition (`research/game_precedent_suite/dispositions/D_T01.md`)
carried a shifted or loose citation, the corrected one is used here.

- **R3-1 (§3 rules of thumb).** Old: no comparison of a whole Ob step with the common roll shapes. New: a step moves Partial-or-better by up
  to 32.0 points at pool 2 (28.2 at pool 3, 22.0 at pool 5), against 5.0 on a d20 and at most 16.7 on 2d6; the pool-2 net is a bell (SD ÷
  range 0.189). Evidence: exact enumeration of `_die_result` (`dice_engine.py:153-161`) banded by `degree_from_net` (`:286-301`).
- **R3-2 (§1 `p_success` row).** Old: "helper only; no season caller". New: also understates Partial-or-better on whole dice (14.4 against
  26.0 % at pool 2 / Ob 2; 43.0 against 58.0 at Ob 1; 50.0 against 60.0 at pool 5 / Ob 2). Evidence: `sigma_leverage.p_success(ob, pool)`
  called at those pairs, against Table A.
- **R3-3 (§5d).** Old: silent on the shape of the middle band. New: Partial is narrow by ruling (ED-IN-0187), 19 % at the shipped pair and
  never modal at pools 1–8 against Ob 1–4; Failure (74 %) is the typical outcome and writes nothing. Evidence: enumeration over
  `degree_from_net`; `dice_engine.py:238`.
- **R3-4 (§7).** Old: no entry for complication as the modal band. New: [PROPOSED] ENP v2 proposal 6 cannot be met by a pool or fixture at
  Ob ≥ `OB_MIN`; the only modal-Partial cell is pool 1 at Ob 0. Evidence: enumeration over pools 1–40, whole Ob 0 to 2 × pool
  (`roll.py:80-82` for the unfloored Ob; `proposals/2026-09-12-emergent-narrative-primitives-v2/01_THE_TEN.md:293-336`).
- **R3-5 (§6 personal combat).** Old: silent on combat's odds override. New: `UPSET_FLOOR` 0.05 flips `winner` but not the wound bands
  the season reads; the social path has no equivalent floor. Evidence: `modules/combat/config.py:295`, `modules/combat/wrapper.py:526-529`,
  `seam/ladder.py:141, :155`, `hole_register.yaml:2393` (H-119).
- **R3-6 (§4 "What executes", §8 item 18).** Old: "`argue` is unreached in all three seeds, and `determine` attempted once (seed 1)". New:
  `argue` never reaches the roll but is formed and stopped 10 / 17 / 18 times (`argument.refused` 10 / 17 / 15, plus 3 `act.ineligible` in
  seed 2); `determine` reaches the roll once and is refused 2 / 5 / 2 times; seed 0 holds 275 acts beyond `d.resolved`; the `examine` row's
  "not re-measured here" becomes the measured 62 / 59 / 39 formed. Evidence: `w.acts`
  against `d.resolved`, re-run on seeds 0/1/2 at `51d7b05`; `resolve.py:61-91, :1025-1032`.
- **R3-7 (§6 mass battle, §8 item 10).** Old: "A guard test holds the copies equal". New: two guard tests (ladder, and face rule at
  `test_tn7_always.py:95`); the per-die μ/σ literals are typed in four files; `roll_pool`'s comment that the volley path hand-rolls its
  dice is stale. Evidence: `resolution.py:37-55, :43-45, :104-120, :227`; `orchestration.py:1565-1574`; `engine/reference/contest-groundup/engine.py:35`.
- **R3-8 (§5a).** Old: no statement on streak memory or on what a seated player would see. New: the per-act generator is seeded from
  `(world_seed, tick, actor, purpose)` alone, no surface shows a chance, so realised odds equal Table A. Evidence: `state/ids.py:16-21, :87-89`;
  overview §7.
- **R3-9 (new §0a).** Old: no account of what a person chooses, or what changes later. New: the section above, re-checked against PR #494:
  the season now reports `world_q.endings_reached` and the realm as built reaches none (`loop/driver.py:515-518`). The ctl counts still hold.

## 9 Checks

Opened (HEAD `a4ca9a5`, tree clean before and after):
- `engine/dice_engine/dice_engine.py:140-306` (faces, TN guard, `roll_pool`, `continuous_engine_sample`, `degree_from_net`).
- `engine/dice_engine/sigma_leverage.py:70-350` (constants, `soft_cap`, `net_boost`, `p_success`, wrappers).
- `modules/social_contest/roll.py:55-125`; `engine/season/seam/wrappers/sigma.py:105-278`; `engine/season/seam/ladder.py:240-259`.
- `engine/season/data/fixtures.py:228, :396-427`; `engine/season/state/ids.py:16-21` and `draw_factory`;
  `engine/season/loop/resolve.py:785-830, :852, :970-997`.
- `modules/combat/core.py:40-127`; `modules/combat/wrapper.py:182, :213, :307` (grep); `modules/mass_battle/resolution.py:57-79, :101-120, :221-235`.
- `engine/season/rosters.yaml:1115-1143, :1206-1231`; `verb_table.yaml` rows for the seven social-path verbs (yaml load), `:353`,
  `:1451-1471` (`train`); `engine/season/decision/budget.py:18-60`; `engine/season/loop/witness.py:136-139`.
- `ls engine/autoload` → "No such file or directory". A grep of `engine/season/decision/*.py` for `p_success|obstacle|odds` → no match.

Ran (`PYTHONDONTWRITEBYTECODE=1 python -I`, scripts in the scratchpad, repo read-only):
- `t01_odds.py`: exact convolution of `_die_result` over faces 1–10 (μ 0.4, σ 0.8 confirmed), banded by `degree_from_net` → Tables A
  and B; Gaussian bands and `p_success`; `obstacle()` on hand-built inputs (reception −3 → 2.0; +1, +5 → 1.0; proofs 2 with reception
  0.5 → 1.0; opposition 3 → 1.5; opposition 1 → 0.5; uncapped forgery 1.5 → 3.5). Control: 200,000 calls of `roll()` at pool 2 / Ob 2
  → 74.10 / 18.94 / 6.96 / 0.00 %.
- `t01_realm.py 0 2` and `t01_realm.py 1 2`: spy on `contest_input` over `build_realm` → 70 and 63 rolls, all pool 2, opposition None,
  leverage 0.0, forgery 0.0. Degrees: seed 0 F 54 / P 9 / S 7 / O 0; seed 1 F 45 / P 16 / S 2 / O 0. Capability non-empty on 0 of 74
  and 0 of 77.
- `t01_example.py`: captured faces per act in seed 0, tick 0, and re-derived each from `H(seed, tick, actor, purpose)`; all matched.
  Examples used in §3: `p_npc_086` → `p_npc_010` [8, 10] Success; → `p_npc_007` [5, 1] Failure; `p_npc_041` `speak` [2, 6] Failure.
- Control-run files `ctl/realm_seed{0,1,2}_2seasons.txt` for attempted counts.

Ran at `51d7b05` (round 3; scripts not committed). `git diff --stat 51d7b05 HEAD -- engine modules systems` is empty, so the code is the
same at the current HEAD; the act-store, `p_success` and pools 1–40 computations below were re-run in the audit-fix pass with the same
figures. Each round-3 figure comes from one of these:
- **Act store against `d.resolved`.** Build the realm and run two seasons as `ctl/control.py:6-11` does, then take the ids in `w.acts`
  that are not in `d.resolved`, by `act.verb` and by the first-cause event kind. It gives the 275 beyond `d.resolved` at seed 0 (1,407
  against 1,132; seed 1 1,394 against 1,122; seed 2 1,447 against 1,175), and at seed 0 `research` 111, `examine` 62, `surveil` 21,
  `speak` 19, `argue` 10 and `act.ineligible` 19. By seed it also gives `argument.refused` 10 / 17 / 15 plus 3 `act.ineligible` at
  seed 2, `determine.refused` 2 / 5 / 2, and `examine` formed 62 / 59 / 39.
- **`sigma_leverage.p_success(ob, pool)`.** Called at (2, 2), (1, 2), (2, 5) and over pools 1–5 × whole Ob up to 2 × pool, set against the
  exact dice odds: it understates at every admitted pair (10–15 points at pool 2–5 / Ob 1–2; 17.3 at pool 1 / Ob 1; 0.8 at pool 2 /
  Ob 4) and gives 0.0006 at the refused pool 1 / Ob 3, where the dice give 0.
- **Exact odds.** `_die_result` convolved over faces 1–10 for pools 1–40, banded by `degree_from_net` at every whole Ob from 0 to
  2 × pool: Tables A and B, the largest Partial share at Ob ≥ 1 (32.0 %, pool 2 / Ob 1), and the single modal-Partial cell (pool 1 /
  Ob 0, 50 %).
- **Hand arithmetic, not the repo's functions.** PbtA P(2d6 + m in [7, 9]) for m = 0 / 1 / 2 (15/36, 16/36, 15/36); Blades
  (5/6)^n − (1/2)^n for n = 2 / 3 / 4 dice; the d20, 2d6 and 3d6 comparison figures in §3.

Not confirmed: `world_q.reception`/`proofs` bodies (docstrings only); that the seam's `fight` call reaches `wrapper.py`'s `core.resolve`
lines (composition row and grep only); `decision/choose.py:149` (cited from D06, not opened); the proposal extracts' document claims
(D01, D02, D03, D06, L11, G20) are the documents' statements, not re-read at source.

