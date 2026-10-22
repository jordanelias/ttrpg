# Tutorial: Personal Combat (PC) — settle a matter body against body: kill, wound, or walk away from a duel the engine fights for you

Repo `jordanelias/ttrpg` at HEAD `a4ca9a5`; **revised in round 3 against `51d7b05` and the precedent suite** (`research/game_precedent_suite/`;
this file's disposition record is `dispositions/D_T03.md` there; the corrections are listed under `### Round-3 corrections`, end of §8).
Path abbreviations: `MC/` = `modules/combat/`; `SW` = `engine/season/seam/wrappers/combat.py`;
`EC` = `engine/season/loop/effects_combat.py`; `VT` = `engine/season/verb_table.yaml`; `ROS` = `engine/season/rosters.yaml`;
`FX` = `engine/season/data/fixtures.py`; `GMS` = `proposals/2026-10-07-grid-mode-suspension.md` (IN-46's design);
`L09` = `proposals/2026-10-16-verbs/2026-10-16-verbs-09-lexicon-personal-combat.md`;
`REM2` = `proposals/2026-10-21-v9-remediation/2026-10-21-v9-remediation-02-items-rb0-to-rb3.md`;
`WB` = `systems/combat/combat_engine_v1/workbench/`; `PS/` = `research/game_precedent_suite/` (reference, tier 3; precedent games are cited as
`T02`, `T05`, `T10`, `T14`, `T18` = `PS/tutorials/T02_warband.md`, `T05_social_rpgs.md`, `T10_npc_economy.md`, `T14_squad_settlement.md`,
`T18_repo_strategy_b.md`, and `R4` = `PS/tables/R4_combat_social_rpgs.md`, each with its game heading and section). Every number below was read from code or produced by a read-only run (§9).

## 0 Before you start

**The frame.** The code has no player character and no GM. Every person is a chooser that picks acts each season from a closed table of
verbs, against a budget of 5 scene actions: a scene holds up to 3 acts, one with more than one act costs 2, so budget 5 buys at most
2+2+1 = 7 acts (§1, "scene"); "you" below means the acting person (a player's character if one is seated later, an NPC today). This tutorial
teaches what an actor can do with personal combat, what the rules do with it, and what an actor must arrange to reach a goal — and it
keeps the large engine (which executes) apart from the thin seam the season uses (which fixes almost every input).

**What you need from other subsystems.**
- A **target in your question's referents.** The chooser only forms acts about the referents of the one question it is answering this
  season (decision layer; draft A2 §B.2). Information (claims in your ledger) decides whom you can think of attacking.
- Your own **`Person.body`** and the target's. It is the only personal quantity the season passes into the fight.
- Nothing else: no skills, kit, office, faction or place is read by the fight today (`MC/fight.py:45`).

**Status (grade per the draft's preamble and ERRATA G1).**
The duel engine `MC/` (5,643 lines) is **RUNS-IN-LOOP in its default build only**: at seed 0 (2 seasons, `ctl/realm_seed0_2seasons.txt`, attempted/ok)
`fight` 7 / 4, `accept` 18 / 11, `challenge` 23 / 6; it executes at seeds 1 and 2 as well (§4). For `fight`/`accept`, "attempted" means
admitted and fought; acts refused at admission are not counted. Weapons, armour, traditions, abilities and every attribute
except endurance are **TESTS-ONLY** (they execute only when an oracle script or test builds a non-default `Combatant`). Yield is TESTS-ONLY.
Duel terms, capture, guards, ranged arms and played fights are **DESIGN-ONLY**.

## 0a How it plays

*Added in round 3, in the format of the precedent suite's tutorials (`PS/tutorials/`). Grades per ERRATA G1. Numbers come from the control runs
(`ctl/`, seeds 0-2, two seasons) and from a read-only trace of the same recipe that logs every personal-combat seam call (the probe is not
committed; its totals are in the header of `PS/dispositions/D_T03.md`, and a re-run on `51d7b05` reproduced its three traces byte for byte).
The as-built text comes first; the last block is [PROPOSED].*

**Setup choices.** *At world build*: `build_realm(seed)` makes every realm person at body 1000 (`FX:217`, `condition_scale`); nothing else about a
person reaches a fight. Each fighter is the class-default Combatant (`arming`, `light`, tradition `none`) except `end`, derived from body bands
(`SW:34-49`, `:130-138`; `MC/fight.py:45`). The seed fixes every fight: the RNG is `H(world_seed, tick, actor, "contest:the body:<cause>")`
(`SW:222`). *At the callback*: a harness-only hook (`engine/season/harness/play_surface.py::dispatching_chooser`) can hand the loop any resolvable
act; for combat that is a verb and a subject, nothing more. One test does it for a `fight` (Carin against the bailiff in the `headless` world,
`engine/season/tests/test_combat_trace_returned.py`); none of the nine hand-built chains in the I1 verification of the capability inventory (not
filed; see `PS/README.md`) was a `fight`. Compare the setup surface of the precedents: Battle Brothers picks origin, recruits and kit (T02
precedent, Battle Brothers §1, §3); Jagged Alliance 2 builds an I.M.P. merc from a 500-point pool (T14 precedent, Jagged Alliance 2 §1). In
Valoria the build is the body.

**The loop.** One season is CALENDAR → MATTER → five rounds of DELIBERATE → RESOLVE → ENCOUNTER → WITNESS → CENSUS (overview §2.1). Combat's
part, all automated after step 1:
1. DELIBERATE: the chooser forms `fight` / `accept` / `challenge` about its question's referents and orders them by score plus Gumbel noise
   (§2.1). No odds, opponent body or place enters the score.
2. RESOLVE: the fold re-checks "the subject is a living person" (`VT:617-621`), then calls the seam (`SW:207-226`).
3. The engine plays up to 12 turns and stops at the first felling (`MC/wrapper.py:504-520`); every move for both sides is drawn.
4. The band is read off the **subject's** tracker (`ROS:784-848`; `seam/ladder.py:155-156`); `_eff_kill` writes the subject only (`EC:107-178`).
5. WITNESS deposits `person.died` / `body.changed` / `contest.undecided` as claims; the observers' scar count moves nothing at shipped values (§5c).

**The choice menu.**

| verb | cost | effect | when a person picks it | grade |
|---|---|---|---|---|
| `fight` | one act in a scene (a multi-act scene costs 2, §1) | subject Felled: body 0, removed, tenures closed; Wounded: body × health left ÷ health full; Untouched: nothing | a living person is among his question's referents; the instrumental pole favours it (§5d) | RUNS-IN-LOOP (ok 4/5/5, seeds 0-2, §4) |
| `accept` | as `fight` | as `fight`, on the challenger; reads no challenge (`VT:742-749`) | the deontological pole favours it; no challenge is needed | RUNS-IN-LOOP (ok 11/6/10) |
| `challenge` | one act | writes nothing; emits `challenge.issued` | rarely acted on: 0 of 39 resolved `accept`s answered one (§8 #6) | RUNS-IN-LOOP, emission only (ok 6/6/12) |
| `tend` | one act | body raised to 1000 | in practice names the dead, the absent or the whole (§5d) | TESTS-ONLY by the grade rule (0 of 75); a hand-built `tend` on a body of 250 raised it to 1000 |

**First season, step by step** (seed 0; each call logged at the seam; the 25 calls and 9 deaths are `ctl/realm_seed0_2seasons.txt`'s).
1. Tick 0, `p_npc_006` `fight`s the King, `p_npc_020`. Both at body 1000, `end 4`. Four turns. 006 is felled in the scene; the King takes two wounds
   (health 18 of 40). Band Wounded: the King's body becomes 1000 × 18 ÷ 40 = 450, two bands down, so `end 2` (and, had he lived, two scene actions
   fewer next season, `decision/budget.py:57-61`). 006 is not written.
2. `p_npc_011` `accept`s against `p_npc_082`. Nobody has issued a challenge yet (the first `challenge.issued` is at fold position 91 of 1,132;
   this `accept` is at position 10). Three turns; 082 is Felled, removed, his tenures closed.
3. `p_npc_040` `fight`s `p_npc_003` and is felled: band Untouched, `contest.undecided`, nothing written. Next, `p_npc_038` `accept`s against 003 and fells him.
4. `p_npc_032`, the Queen, `accept`s against the King, now at `end 2` (health full 23). Four turns; the King is Felled. His seat has no
   conferral basis (`engine/season/offices.yaml:188`). The Queen took two wounds in the scene (health 19 of 40) and is not written.
5. Tick 0 closes with 15 combat calls: 5 Felled, 4 Wounded, 6 Untouched, and the actor felled in all 10 non-Felled calls.
6. Tick 1 (10 calls) shows the carry-over: `p_npc_004`, cut to 650 and then 48 by two fights he won as subject, attacks at `end 1`, is felled in
   one turn, and keeps body 48 to the end of the run.

**What changes later.** A lowered body carries from fight to fight; wounds do not (trackers reset per call, `MC/wrapper.py:498`). Over seeds 0-2,
11 calls met a subject below `end 4` and 7 of them Felled him. No fighter improves (`train` writes `capability`, which the fight never reads) and
no `tend` lands. Deaths run 9 / 6 / 11 in two seasons.

**Failure and ending.** The run has no ending to fail into: the season now reports `endings` (`loop/driver.py:518`; `queries/world_q.py:1764`;
rows `peninsular_sovereignty` and `theocracy`, `ROS:2524`, `:2542`), halts on none of them, and the realm as built reaches none
(`world_q.py:1789-1790`); no death, the King's included, ends it. A subject's failure is final (`EC:178`). An attacker's failure does not exist
in the world: 33 of 59 calls felled the actor and none was written. Nobody can surrender (the season passes no `yield_decl`, `MC/fight.py:52`),
be captured, be spared or reload. In the precedents a fight's harm falls on the side that lost it, whoever started it (T02 precedent, Battle
Brothers §6; T14 precedent, Jagged Alliance 2 §6; T18 precedent, XCOM §2 step 5, §6). Valoria charges only the subject, and charges him when he wins.

**Consequential vs cosmetic.** Consequential: whom you can name (your referents); the target's body; being the actor rather than the subject.
Cosmetic in the season: `challenge` (writes nothing, answered by nobody in seeds 0-2); the upset floor (flips a field nothing reads,
`MC/wrapper.py:526-530`); `winner`; weapon, armour, tradition and abilities (unreachable; §3 shows they would decide fights).

**As proposed [PROPOSED].** All DESIGN-ONLY; reference only.
- [PROPOSED] IN-46 (REM-31, ruled to build by D-2): a played person's fight suspends at the seam and a decider picks, each turn, from
  [ASSUMPTION] {engage, withdraw}, reading the turn index and a read-only view of both fighters (`GMS:116-122`); the engine's own comment already
  marks the per-turn unit ("the GAME calls one engagement per turn", `MC/wrapper.py:504`). AUTOMATED and PLAYABLE with equal choices must end at
  one `content_hash` (the falsifier, `REM2:570-589`). Against the precedents' played fights: XCOM and Baldur's Gate 3 put a hit chance on the
  decision (T18 precedent, XCOM §7; R4 precedent, Baldur's Gate 3 M4) and IN-46's decider receives none, although the workbench already turns
  trace inputs into branch odds (`WB probabilities.py:109-123`); Jagged Alliance 2 lets the player choose auto-resolve per battle (T14 precedent,
  Jagged Alliance 2 §2) where IN-46 decides by a party test at the seam; Battle Brothers and Kingdom Come: Deliverance let the build decide (T02
  precedent, Battle Brothers §7; T05 precedent, Kingdom Come: Deliverance §5) where IN-46 leaves the Combatant at its default (M13 is separate).
- [PROPOSED] L09 M11: the decider set widened to the scene's moves (`feint`, `lunge`, `parry`, `dodge`, `grapple`, `flee`, `yield`,
  `interpose`), one engagement per act; L09 M1: both parties take their band (`SW:230` already returns both). M1 is not a remediation item
  (`REM2:575-576` lists the files REM-31 changes; `loop/effects_combat.py` is not among them), so under IN-46 as scheduled a played attacker who
  is felled still stands.
- [PROPOSED] L09 M3/M4 duel terms (first blood, yield, death); M5 capture and rescue; M15 a grudge on the survivor; M13 per-person inputs
  (Jordan's). These map onto the precedents' non-lethal exits and aftermaths: Griftlands' surrender and spare-or-kill (T05 precedent, Griftlands §2),
  the capture of Jagged Alliance 2 and Kenshi (T14 precedent, Jagged Alliance 2 §6; T02 precedent, Kenshi §2), Wildermyth's Mortal Choice (T10
  precedent, Wildermyth §6), JA2's morale cost of a death (T14 precedent, Jagged Alliance 2 §7).
- [PROPOSED] IN-46's design names no outcome for a played person's death: `GMS` mentions a felling only as the loop's own exit (`:111`), and its
  "Not decided here" list (`:172-180`) does not carry one. [precedent: T02 precedent, Battle Brothers §1, §6 (the Lone Wolf origin ends the run when
  he dies)]

## 1 The pieces

| term | what it is | numbers / limits | where it lives |
|---|---|---|---|
| **scene action / scene** (season sense) | the budget unit; a scene holds 1–3 acts (`fight` is one act inside a scene) and costs 1, or `extended_scene_cost` 2 if it holds more than one act; a chunk is cut to one act when only 1 is left; the driver releases ≤ 1 scene per round over 5 rounds | budget `max(1, 5 + 1 per live hold − body bands − 1 per travel leg)` → budget 5 = 7 acts, budget 6 = 9 | `decision/budget.py:19-20`, `:57-61`; `FX:488-489`; `decision/choose.py:643-657`; `loop/deliberate.py:252-259` |
| **`fight`** | season verb: attack the named subject; contests the prize `"the body"` | stratum `contested_physical`; eligibility `own`; requires "the subject is a living person" | `VT:612-707` |
| **`challenge`** | season verb: call someone out before witnesses | writes nothing; emits `challenge.issued` / `challenge.refused` | `VT:716-736` |
| **`accept`** | season verb: answer a challenge; the same fight as `fight` | same writes/emits as `fight`; refusal `accept.refused` | `VT:737-765` |
| **prize `"the body"`** | routes a contested verb to the `personal_combat` provider at RESOLVE | no `step:`, so it fights at RESOLVE | `ROS:1273-1277`, `:1296-1298` |
| **`Person.body`** | a person's physical state | scale 1000 (`condition_scale`, `FX:217`); every realm person starts at 1000 (run) | `FX:217` |
| **body bands** | floors on body: `full_operations 800`, `limited 500`, `withdrawal_only 100` | penalty = number of floors body is below (0–3) | `ROS:2627-2630`; `budget.py:71-83` |
| **`end`** (endurance) | the one Combatant field the season sets | `end = max(1, 4 − body band penalty)` → 4/3/2/1 | `SW:130-138` |
| **Combatant** | one fighter in the engine | defaults `strength 4, agi 4, end 4, cog 3, att 3, spirit 3, focus 3, history 3, disp 4, weapon 'arming', armor 'light', tradition 'none'` | `MC/combatant.py:93-94` |
| **disposition** (`disp`) | aggression axis 1–7, 4 neutral; lean `(disp−4)/3` | skews commit depth, initiative drift, counter choice | `MC/combat_systems.py:181-183` |
| **WoundTracker** | cumulative damage → wounds and felling | `wounds = min(dmg // wi, max_wounds+1)`; `felled = dmg ≥ health_full` | `MC/combatant.py:50-89` |
| **wound interval (`wi`)** | damage per wound | `round(end + 4 + 0.4·spirit)` → 9 at defaults | `MC/combatant.py:35-37` |
| **max wounds** | wound cap before felling | `min(end//2 + 1, 3)` → 3 | `MC/combatant.py:30-32` |
| **health_full** | damage that fells | `round(wi·(max_wounds+1) + 0.25·strength·end)` → 40 | `MC/combatant.py:40-42` |
| **stamina** | physical reserve; spent per attack, recovered between turns | max `3·end + 2·spirit` → 18; collapse at ≤ −4 | `MC/combatant.py:45-47`; `MC/wrapper.py:462` |
| **concentration** (`conc`) | mental reserve; drained by hits and lost exchanges | max `3·focus + 2·spirit` → 15 | `MC/combatant.py:147`; `MC/wrapper.py:22-24` |
| **initiative** | the "who is pressing" edge, ±1.5 | gains on hits (+0.18), losses when wounded (−0.28), steals in binds | `MC/combat_systems.py:1164`; cfg |
| **poise** | balance, 0.4–1.0 | broken by hits, binds, grapples; regenerates per beat | `MC/combat_systems.py:1195-1200`, `:1433-1436` |
| **fight (engine)** | up to 12 **turns** (engagements, ~10 s each) | ends on a felling, an accepted Yield, or 12 turns → 0 "undecided" | `MC/wrapper.py:487-532` |
| **engagement / turn** | approach → a burst of exchanges → separation | ≤ 24 beats; ≤ 4 exchanges (`BURST_MAX`) | `MC/wrapper.py:47-465` |
| **beat** | one tick of footwork/tempo inside an engagement | a fighter acts when his `ready` reaches `ACT_THRESHOLD 2.5` | `MC/wrapper.py:117-149` |
| **reach / measure gap** | distance advantage of the longer weapon | `reach_base = 4.0 + 2.1167·forward_extent + reach_adj`; gap ≤ 0 closed, ≥ 0.6 open | `MC/combat_systems.py:48-75`; `MC/wrapper.py:77-80` |
| **stop-hit** | the longer weapon's free strike while the shorter one closes | `0.75·min(1, gap/3)·(1−displace)·reach_threat` | `MC/wrapper.py:208` |
| **commit depth** | how deeply the attacker commits, 2–5 | `2 + 3·Beta(a,b)`, skewed by disposition and wariness | `MC/combat_systems.py:1106-1121` |
| **lunge** | a commit ≥ 4.0 that extends | depth `min(1, (commit−4)/4)` if a lunge-quality roll passes | `MC/wrapper.py:259-260` |
| **read contest** | defender tries to read the attack | `P = logistic(read_d − read_a)`; a win picks the best defence mode, a loss picks at random | `MC/combat_systems.py:1123-1137` |
| **defence modes** | parry, dodge, wind (bind-seeking) | `DEFENCE_MODES = (parry, dodge, wind)` | `MC/vocabulary.py:72` |
| **net sigma (σ)** | the sum of situational edges fed to the roll | `attack − defence − reach + armour-defeat + initiative + wound impairment` | `MC/combat_systems.py:1090-1104` |
| **wound impairment** | wounds as a σ term (not an Ob term) | `+0.25·defender wounds − 0.15·aggressor wounds` | `MC/combat_systems.py:1038-1044` |
| **pool** | dice count of the exchange roll | `max(5, round(history) + 6)` → 9 | `MC/core.py:54-56` |
| **Ob** (obstacle) | what the roll must clear | `defender.history / 2` → 1.5; nothing else is added | `MC/core.py:100-115` |
| **the roll** | one per exchange | `net = N(0.40·pool, 0.80·√pool) + soft_cap(σ)·0.8·√pool`; `soft_cap(x)=1.5·tanh(x/1.5)` | `MC/core.py:118-127`; `engine/dice_engine/sigma_leverage.py:104-148` |
| **exchange degree** | the margin ladder | `net−Ob` < 0 fail; [0,1) partial; [1,3) success; ≥ 3 overwhelming | `engine/dice_engine/dice_engine.py:227-239`, via `MC/core.py:65-74` |
| **bind** | blades in contact; up to 3 inner beats | dominance `logistic(bind_sigma)`; winner strikes w.p. 0.4 | `MC/wrapper.py:395-417` |
| **riposte** | counter-strike after a defence; roles flip | on fail w.p. 0.32 (+exposure); on a neutralised success w.p. 0.2 | `MC/wrapper.py:317-333`, `:418-428` |
| **grapple / contact** | grab branch on an opening | six outcomes: disarm, throw, pin, control, foot_pin, escape; poise/initiative only, no wound | `MC/contact.py:29-62`; `MC/wrapper.py:435-450` |
| **damage** | `impact × coupling × quality × 1.55`, then an armour penetration knee | quality graze 0.25 / success 1.0 / overwhelming 1.5–2.5 | `MC/core.py:149`, `:573-641` |
| **armour tier** | none / light (cloth) / medium (mail) / heavy (plate) | resist (percussion, shear, puncture): cloth .12/.45/.12, mail .20/.85/.45, plate .30/.95/.70 | `MC/core.py:149-190` |
| **weapon** | a physical record: mass, head and grip length, hands, head type, geometry | 54 keys (50 base + 4 half-sword forms; header says 53) | `MC/weapons.py` |
| **tradition** | a "cognitive mode", not a rule-set | 7 + `none`; familiarity 1.0 same/none, 0.93 adjacent, 0.85 otherwise | `MC/traditions.py:1-8`, `:32-55` |
| **ability** | a tradition-gated multiplier/bonus on a named channel | 9 abilities (e.g. `indes` +0.15 counter success; `misura` ×1.15 measure); inert outside own tradition | `MC/ability_primitives.py:29-70`, `:100-126` |
| **Yield** | a Phase-1 surrender declaration | needs `yield_decl`; the season never passes one | `MC/wrapper.py:467-513`; `MC/fight.py:52` |
| **upset floor** | 5 % chance a decided result's sign is flipped | flips `result`, not the trackers; the season band reads the subject's tracker (`ROS:820-848`; `seam/ladder.py:155-156`), so the floor never reaches the world and its stated purpose ("no matchup is ever certain", `:526-527`) is not delivered in the season | `MC/wrapper.py:526-530` |
| **band (season degree)** | Felled / Wounded / Untouched, read off the SUBJECT's tracker | Felled if `felled`, Wounded if `wounds > 0`, else Untouched | `ROS:784-848`; `seam/ladder.py::combat_degree` |
| **wound harm model** | how much body a Wounded band costs | shipped `scene_fraction`: `body = max(1, body·health_remaining // health_full)` | `FX:624`; `EC:134-151` |
| **`tend`** | season verb: raise a person's body to 1000 | requires subject exists and is `with` the actor | `VT:1146-1168`; `EC:370-393` |

## 2 How it works

Read this in the order the rules meet you: the season decides that a fight happens and against whom; the seam builds two fighters; the
engine plays turns, engagements, beats and exchanges; the season reads one band off the subject and writes it.

### 2.1 Getting into a fight (season side)
1. **DELIBERATE.** Your chooser answers one question and forms candidates about its referents. `fight` is eligible for anyone (`own`) and
   requires only that the subject is a living person (`VT:614-621`): no co-location, no hostility, no war test. It scores
   `Σ pursuit weight × alignment` plus a stance term plus a constant (`decision/choose.py:149-151`). `fight` has two alignment cells:
   `grandiose_humble −0.3` and `deontological_instrumental +0.3` (`ROS:3346`, `:3412`). The stance term ships as `legacy`
   (`FX:833`): your stored stance toward the subject is ADDED to every verb about him, at weight `1 + stance_gain`, and
`stance_gain` ships at 1.0 (`FX:847`; `choose.py:84-86`), so the stance counts double. So a grudge (negative stance) makes `fight`
   on him score **lower**, not higher (`choose.py:54-79` docstring). Candidates are then ordered by a Gumbel draw at temperature 0.1.
2. **RESOLVE.** The fold re-checks the precondition against the world; a subject who does not exist refuses with `kill.refused`
   (`VT:705`). Otherwise `loop/resolve.py::_contest` calls the seam with `claimants = [actor, subject]`.
3. **The seam builds two fighters** (`SW:207-226`). Each gets `end = max(1, 4 − body band penalty)` (`SW:130-138`); everything else is
   the class default (`MC/fight.py:45`). With body ≥ 800 you fight at `end 4`; 500–799 → 3; 100–499 → 2; below 100 → 1. The RNG
   seed is `H(world_seed, tick, actor, "contest:the body:<cause>")` (`SW:222`): the fight is fully determined by the world clock and
   the causing act.

| `end` | body band | wound interval | max wounds | health_full | stamina max |
|---|---|---|---|---|---|
| 4 | ≥ 800 | 9 | 3 | 40 | 18 |
| 3 | 500–799 | 8 | 2 | 27 | 15 |
| 2 | 100–499 | 7 | 2 | 23 | 12 |
| 1 | < 100 | 6 | 1 | 13 | 9 |

(Computed by building `Combatant(end=e)`, `t03/derive.py`.)

### 2.2 The fight: turns (`MC/wrapper.py:487-532`)
- Both trackers and live state reset: stamina and concentration full, initiative 0, poise 1.0 (`:498-499`, `:21-26`).
- Each of up to 12 turns: a coin flip names `first` (`:514`), one engagement runs, then each fighter recovers half his missing stamina
  (scaled by `stamina_max/18`) and concentration drifts by `−3 + 0.4 × missing` (`:521-523`).
- The fight ends at the first felling. After 12 turns with nobody felled the result is `0`, **undecided** — a ruled outcome, never
  retried (`:524-525`). A decided result is then flipped with probability 0.05, the **upset floor** (`:529-530`).

### 2.3 An engagement: measure, approach, exchanges (`MC/wrapper.py:47-465`)
1. **Measure.** The longer weapon's reach minus the shorter's is the gap. Gap ≤ 0 starts **closed**; ≥ 0.6 starts **open**; between,
   a draw decides (`:77-80`). Two equal weapons (every season fight: both `arming`, reach 5.42) start closed at gap 0 — so the whole
   open-measure game below is skipped.
2. **Open measure (unequal reach only).** Each beat the shorter fighter closes at `close_rate`; the longer may take a **stop-hit**
   (chance up to 0.75 × reach threat) resolved by a full roll (`:190-226`). Closed again, the longer weapon may **reopen** measure, and a
   fighter may try to **disengage** — the pursuer gets a roll at `σ −0.3` (`:155-188`). All three need a base gap > 0.3.
3. **Cadence.** Each fighter's `ready` starts at a random phase in [0, 2.5) and grows each beat by his tempo (base 2.0, cut by weapon
   heft, fatigue and poise; compressed when closed, `combat_systems.py:89-160`). Whoever crosses 2.5 attacks; ties break at random.
   The coin-flip `first` labels the engagement; the cadence draw decides who swings first.

### 2.4 An exchange (`MC/wrapper.py:233-453`)
1. **Commit.** `commit = 2 + 3·Beta(a,b)`; neutral disposition gives `a = b = 1.2` (mean 3.5). Wariness against an unfamiliar tradition
   pulls commitment down; aggression pushes it up (`combat_systems.py:1106-1121`). Commit ≥ 4 may become a **lunge**. The attacker pays
   stamina `(2 + heft + 0.4·commit)·0.5` and loses tempo in proportion to `commit − 2` (`:261-262`).
2. **Read contest.** The defender's read `read_d = reading × familiarity × legibility × (1 − 0.4·mental fatigue)` against the attacker's
   `reading + consistency`; `P(read) = logistic(read_d − read_a)` (`combat_systems.py:1123-1137`). Default reading is
   `(2·cog + att)/3 = 3`. A won read picks the defence mode with the best σ; a lost read picks parry, dodge or wind at random.
3. **Net σ.** `attack_sigma − defence_sigma − reach_penalty + armour_defeat + initiative_edge + wound_impairment`
   (`combat_systems.py:1090-1104`). Attack σ is `0.18·(commit − 3) + tempo-emphasis − out-of-stamina penalty − handling + consistency`.
   **Wounds enter here, as σ**: each defender wound adds +0.25 σ, each attacker wound −0.15 σ (`:1038-1044`).
4. **The roll.** Pool 9, Ob = defender `history/2` = 1.5. Net is a Normal draw, mean 3.6 and s.d. 2.4 at pool 9, plus
   `soft_cap(σ) × 2.4`. The margin `net − Ob` gives the degree.

| net σ | fail | partial | success | overwhelming |
|---|---|---|---|---|
| −1.0 | 0.500 | 0.162 | 0.233 | 0.106 |
| −0.5 | 0.347 | 0.162 | 0.295 | 0.196 |
| 0.0 | 0.191 | 0.133 | 0.323 | 0.354 |
| +0.5 | 0.087 | 0.086 | 0.284 | 0.543 |
| +1.0 | 0.040 | 0.051 | 0.217 | 0.691 |

   (Normal-CDF arithmetic at pool 9, Ob 1.5, `t03/derive.py`; the sampler's own mean/s.d. measured 3.591/2.396 over 20,000 draws.)
   One defender wound shifts net by +0.60 (success-or-better 0.677 → 0.760); three wounds by +1.66 (→ 0.875).
5. **Outcome map** (`MC/wrapper.py:317-345`). Fail → the defender may riposte (0.32 + exposure). Partial → a dodge or parry may still
   take a graze (0.4 / 0.3); a wind binds. Success → a wind binds w.p. 0.55; otherwise the defence neutralises w.p. 0.55 parry / 0.62
   dodge / 0.5 wind (then a riposte chance 0.2), else a clean hit. Overwhelming → a hit unless a reduced neutralise roll (`neutralise −
   0.45`) succeeds. A defender who won the read on a deep commit may attempt a **counter** (stealing initiative, `:300-345`).
6. **Bind** (`:395-417`): `bind_sigma` from technique, leverage, guard, tactile read, strength; the dominant side strikes w.p. 0.4 per
   inner beat, a lost dominance gives the other a riposte.
7. **Grapple** (`:435-450`): on an opening (or always for a head ≤ 0.375 m), a grab resolves to disarm, throw, pin, control, foot_pin or
   escape. These move poise and initiative only; a grapple never wounds.
8. **Separation**: the burst ends after 4 exchanges, a clean defence (no hit, riposte or bind), either fighter's stamina ≤ −4, or 24 beats.

### 2.5 Damage and armour (`MC/core.py:573-677`)
`raw = (strength + heft) × coupling × quality × 1.55`, where `coupling = delivery[head] × transmission(material, mode)`: percussion,
shear and puncture are resisted differently by cloth, mail and plate (table in §1), and a point's puncture uses the better of material
transmission and `gap exposure × gap precision × thrust authority`. Quality is 0.25 graze, 1.0 success, and 1.5 rising to 2.5 with how far
an overwhelming roll cleared its floor (`tanh`, `:635-641`). Against medium and heavy armour a penetration knee `raw·raw²/(raw²+t²)`
cuts weak blows hardest (`PEN_THR` 2.5 / 6.5). At defaults (arming sword on cloth) landed main-exchange blows ran 4–34, median 21
(400 fights); a success typically does ~14 (one wound), an overwhelming 26 (two wounds: 26 // 9 = 2) to 28 (three).

### 2.6 Back to the season: band and write
The band is read off the **subject's** tracker only (`ROS:820-848`): `felled` → **Felled**; `wounds > 0` → **Wounded**; else
**Untouched**. The effect `_eff_kill` writes the subject only (`EC:107-179`):
- **Felled**: `body = 0`, then `World.remove_person` closes every tenure naming him; emits `person.died`.
- **Wounded**: `body = max(1, body × health_remaining // health_full)`; emits `body.changed`. A wound cannot kill.
- **Untouched**: writes nothing; emits `contest.undecided` — even when the actor was the one felled.
The fold then scars the act's observers (`loop/resolve.py::_scar_witnesses`). The trace is returned to the caller but never folded
into `World` (`SW:245-252`). The actor's wound state reaches the effect (`SW:230`, `:237` return both parties) and is not read: `_eff_kill` reads
`wound_state[subject]` only (`EC:125`). **The attacker is never written.**

## 3 A worked example

**Setup.** `build_realm(0)`, tick 0; `p_npc_001` attacks `p_npc_002`. Both bodies 1000 → penalty 0 → `end 4`: wi 9, max wounds 3,
health 40, pool 9, Ob 1.5. Called through the real seam (`SW.resolve(w, ["p_npc_001","p_npc_002"], ["act-example"], "the body",
verb="fight", subject="p_npc_002")`, `t03/seam.py`); the cause string is synthetic, so a real season's seed for this pair differs.
Seed `15439169748778464981`. Reach 5.42 each, gap 0: every turn starts closed.

| turn | first | exchange | commit | read (P) | mode | net σ | net | margin | degree | result |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 002 | 002 → 001 | 3.06 | lost (0.389) | dodge, random | +0.016 | 1.42 | −0.08 | fail | no riposte; clean defence → separate |
| 2 | 001 | 001 → 002 | 2.74 | lost (0.391) | parry, random | −0.086 | 0.32 | −1.18 | fail | grapple: `control`; clean defence |
| 3 | 001 | 002 → 001 | 3.04 | lost (0.402) | dodge, random | −0.064 | 0.25 | −1.25 | fail | grapple: `disarm` (poise only) |
| 4 | 002 | 002 → 001 | 2.29 | **won** (0.408) | parry, by read | −0.238 | 5.74 | 4.24 | overwhelming | hit **26** → 001 has 2 wounds |
| 4 | — | 002 → 001 | 3.25 | lost (0.409) | wind, random | +0.564 | 6.46 | 4.96 | overwhelming | 001 **felled** (≥ 40) |

Notes on the arithmetic. The defender's read probability sits near 0.39–0.41 in a mirror because `read_d ≈ 2.5` (reading 3 × legibility)
against `read_a ≈ 2.9–3.0`. In turn 3 the engagement's `first` was 001 but 002 struck first: the cadence draw, not the coin, decides.
In turn 4 the first hit (26 damage = 2 wounds at wi 9) let the burst continue; the second exchange's σ includes +0.50 of wound
impairment (2 × 0.25) and its overwhelming blow took 001 past 40. The felling blow has no `outcome` event in the trace (the engine
returns before emitting it, `MC/wrapper.py:386-394`, `:451`).

**What the season does with it.** `result = −1`, `winner = p_npc_002`. Subject `p_npc_002`: `felled False, wounds 0,
health_remaining 40/40` → band **Untouched** → nothing written, `contest.undecided` emitted. Actor `p_npc_001`: felled, wounds 4,
health 0 — and **not written**: he stays alive at body 1000. Had the subject been felled, `p_npc_002` would be removed with his tenures;
had he taken, say, 14 damage, body would become `1000 × 26 // 40 = 650` (band `limited`, `end 3` and a budget one scene action smaller next season).

**Over 400 seeds** (same season entry, `ends = (4,4)`, `t03/fights.py`): subject Felled 194, Wounded 112, Untouched 94; actor felled
205 (51 %), all unwritten; undecided 1. Turns per fight 1–12, mode 2. Exchange-degree shares 0.204 / 0.131 / 0.312 / 0.353 (fail →
overwhelming), matching the σ = 0 row above. Bodies written for Wounded subjects: 25–650, median 450. In 94 of 400 fights (23.5 %)
the act reports `contest.undecided` for a scene in which the attacker died.

**One non-default pairing, and the season's one lever** (`MC/wrapper.fight` directly, n = 400, seeds 0–399, `t03/pairs.py`; A vs B;
the control reproduces the season entry exactly):

| A (B at defaults unless stated) | A won | B won | undecided | A felled | B felled | turns | what woke up |
|---|---|---|---|---|---|---|---|
| control: default vs default | 47.2 % | 52.5 % | 0.2 % | 51.2 % | 48.5 % | 3.4 | rolls 6.4, grapples 1.2 per fight |
| heavy armour (plate) | 90.0 % | 7.5 % | 2.5 % | 0.0 % | 97.5 % | 4.8 | — |
| medium armour (mail) | 70.2 % | 29.0 % | 0.8 % | 26.2 % | 73.0 % | 4.0 | — |
| no armour | 47.5 % | 52.2 % | 0.2 % | 52.0 % | 47.8 % | 3.4 | — |
| spear | 95.5 % | 4.5 % | 0.0 % | 0.2 % | 99.8 % | 1.1 | approach 3.6, stop-hits 2.2 per fight |
| poleaxe | 91.5 % | 8.5 % | 0.0 % | 3.0 % | 97.0 % | 1.5 | approach, stop-hits |
| dagger | 10.5 % | 89.5 % | 0.0 % | 95.0 % | 5.0 % | 2.3 | approach 5.2, disengage 0.2 |
| history 5 (pool 11; Ob against A 2.5) | 87.8 % | 12.0 % | 0.2 % | 9.2 % | 90.5 % | 3.4 | — |
| german + `indes`, `staerke_schwaeche`, `zwerchhau` | 48.2 % | 51.5 % | 0.2 % | 49.8 % | 50.0 % | 3.4 | — |
| german kit vs italian kit (familiarity 0.93) | 44.2 % | 55.8 % | 0.0 % | 53.5 % | 46.5 % | 3.5 | — |
| disposition 7 | 54.2 % | 45.8 % | 0.0 % | 45.8 % | 54.2 % | 3.5 | — |
| "knight": longsword, plate, german kit, str 5, history 5 | 93.2 % | 6.8 % | 0.0 % | 0.0 % | 100.0 % | 2.3 | approach, half-sword |
| end 4 vs B end 1 (body < 100) | 77.8 % | 22.2 % | 0.0 % | 19.8 % | 80.2 % | 2.3 | — |

Read the table this way: armour, reach, training (history) and endurance decide fights in the full engine; tradition and abilities, on
equal arming swords, move nothing beyond noise (±2.5 points at n = 400). Where one side is felled almost always, the other side's "won"
share above 95 % is capped by the upset floor: the spear is felled in 0.2 % of fights yet "loses" 4.5 %. In the season, **only the last
row is reachable**, and only through body.

## 4 What you can do

Each combat verb is one act, which sits inside a scene: alone it costs 1 scene action, and in a scene with other acts it shares that
scene's cost of 2 (§1). All are eligible to anyone (`own`). None tests place, war, office
or relationship.

| verb | prerequisite (checked in the world at RESOLVE) | who | outcome by degree (subject's band) | writes | emits |
|---|---|---|---|---|---|
| `fight` | subject is a living person (`VT:617-621`) | anyone, against anyone in the question's referents | Felled: body 0, removed, tenures closed · Wounded: body scaled by health left · Untouched: nothing | `Person.body`, `Person.exists`, `Tenure.until` (subject only) | `person.died` / `body.changed` / `contest.undecided`; refusal `kill.refused` |
| `challenge` | challenged is a living person other than the challenger (`VT:721-733`) | anyone | none: there is no contest | nothing (`VT:729-730`) | `challenge.issued`; refusal `challenge.refused` |
| `accept` | the challenger is a living person (`VT:742-749`) — **not** that a challenge was issued | anyone | exactly as `fight`, the subject being the challenger | as `fight` | as `fight`; refusal `accept.refused` |
| `tend` (preparation) | subject exists and is `with` the actor (`VT:1151-1160`) | anyone, self or another | body raised to `max(body, 1000)` in one act (`EC:389-392`) | `Person.body` | `body.tended`; refusal `tend.refused` (also when body is already whole) |

What you **cannot** do inside the fight: choose a move. Commit depth, lunge, defence mode, bind, riposte, grapple, disengage and yield
are all drawn by the engine for both sides (`MC/wrapper.py`), and the season passes no `yield_decl` (`MC/fight.py:52`). `train` raises
`Person.capability` (`EC:397`), which the fight never reads.

Execution in the realm (`ctl/realm_seed{0,1,2}_2seasons.txt`; columns attempted/ok). "Attempted" is acts that reached the fold
(`loop/resolve.py:377-379`): for the contested `fight` and `accept` that means **admitted and fought**. An act refused at admission
(`loop/resolve.py:1025-1032`; e.g. a subject who does not exist) is not counted, which is why seed 0 has 11 `kill.refused` events against
7 attempted `fight`s. "Ok" is a Felled or Wounded band: `contest.undecided` (Untouched) is counted as not ok. For the uncontested
`challenge` and `tend`, "ok" is the success kind.

| verb | seed 0 attempted / ok | seed 1 | seed 2 |
|---|---|---|---|
| `fight` | 7 / 4 | 5 / 5 | 8 / 5 |
| `accept` | 18 / 11 | 9 / 6 | 12 / 10 |
| `challenge` | 23 / 6 | 22 / 6 | 33 / 12 |
| `tend` | 34 / 0 | 22 / 0 | 19 / 0 |

Seed 0 by band (`t03/realm.py`): `fight` 2 Felled, 2 Wounded, 3 Untouched; `accept` 7 Felled, 4 Wounded, 7 Untouched. Every one of the
9 deaths in that run is from these two verbs (ERRATA G9; 9 `person.died`, 9 persons gone). All 34 `tend`s were refused: 18 named a
subject not in the world (10 never in the realm, 8 already dead), 2 one who was not with the tender, and 14 met both preconditions and were refused because the body was
already whole. The refusal kind is flat (`tend.refused` for every cause, `VT:1164-1165`), so this split is inferred by elimination
from each event's `observed` tuple (an `exists` check on every event, and a `with` check only on the 16 whose subject existed). A split
that counts absent subjects as failed `with` is reading the same events differently.

## 5 Pursuing goals here

### 5a What a fight is for, and how the code represents it
No combat goal object exists. A person reaches a fight through (i) the **question** the chooser answers (its referents bound who can be
named), (ii) the **score** (pursuit weights on the verb's alignment cells, plus stance toward the subject) and (iii) Gumbel noise. The
goals a fight can serve are therefore read off what the band writes:

| goal | represented by | reachable today? |
|---|---|---|
| **kill** a person | the subject's Felled band: body 0, `remove_person`, every tenure naming him closed | yes, by chance: 48.5 % of mirror fights |
| **wound** a person | the Wounded band: body scaled down, which lowers his `end` and his scene budget next season | not by winning: the fight runs to the first felling (`MC/wrapper.py:516-520`), so a subject left Wounded or Untouched means the attacker was felled. Of the 112 Wounded mirror fights (§3) at least 111 felled the actor (206 non-Felled = 205 felled actors + 1 undecided); in the realm, 15 of 15 (seeds 0-2). The body cut lands on the winner |
| **force a duel** | `challenge` → the other's `accept` | no carrier: `challenge` writes nothing and `accept` does not read it (`VT:749`) |
| **provoke / be seen** | `challenge.issued` and the fight's band kind, fanned to witnesses as claims | yes; it changes what others hold, not what they do |
| **defend yourself** | nothing: there is no guard, no interpose, no refusal to be attacked | no; your only defence is your body band |
| **take someone alive** | — | no (DESIGN-ONLY, §7) |

### 5b Plays, step by step
**Play 1 — the kill.**
1. Have the target among your question's referents (in practice: claims about him in your ledger).
2. Keep your own body ≥ 800 (`end 4`). Below 800 you lose health, wound tolerance and stamina (table §2.1).
3. Prefer a target whose body has already fallen: against `end 1` (body < 100) the subject is felled in 80.2 % of fights; against
   `end 4`, 48.5 %.
4. Spend one act on `fight` (1 scene action alone, or a share of a 2-cost scene). Repeat next season on a survivor: wounds do not carry over in the engine (trackers reset each call,
   `MC/wrapper.py:498`), but his lowered body does, through `end`.

**Play 2 — the duel as the challenged.** If someone challenged you, `accept` is a `fight` with the challenger as subject: the band and the
writes fall on the **challenger**. If you are the challenger, your `challenge` writes nothing and puts you at risk only if someone else
independently forms `accept` against you.

**Play 3 — preparation.** `tend` (yourself, or someone `with` you) restores body to 1000 in one act, so a wounded fighter returns to
`end 4` and to a full scene budget. It refuses on a body already whole.

### 5c Costs, risks, counter-play, blockers
- **Cost:** one act from the season's budget (budget 5 → at most 7 acts, §1). No stamina, wealth, office or standing is spent.
- **Risk to the attacker:** none in world state today. The actor's wound state is returned and not read (§2.6); in 51 % of mirror fights the
  attacker is felled in the scene and stands up unharmed in the world. In the realm the share is higher: 33 of 59 combat calls over seeds 0-2.
  At tick 1 of seed 0, `p_npc_004`, cut to body 48 (`end 1`) by two fights he won as subject, attacked, was felled in one turn, and kept body 48.
- **Risk to bystanders:** observers take a scar count per violated pursuit (`loop/resolve.py:597-610`), which shifts no pursuit at
  shipped values (`scar_weight_shift 0`, ERRATA G1).
- **Counter-play for the subject:** none inside the act. He cannot guard, flee, yield or refuse; nobody can interpose. His only levers are
  his body (tend) and, later, his own `fight`.
- **Blockers:** the subject must exist when the act resolves. Many formed acts name persons not in the world (seed 0: all 11
  `kill.refused` and 16 `accept.refused` events name a subject never in the realm); a known-false claim can veto the candidate earlier.
  The stance term ships as `legacy`, so ill will toward someone lowers the score of fighting him.

### 5d What the mechanics structurally reward or punish
- **Attacking is dominant over being attacked.** Only the subject can lose body or life; the act's two parties are asymmetric by
  construction (`EC:107-109`).
- **`accept` is a `fight` with different alignment cells** (`rigid_flexible −0.3`, `grandiose_humble −0.2`,
  `deontological_instrumental −0.4` against `fight`'s `−0.3` and `+0.3`; `ROS:3302`, `:3346-3349`, `:3412-3414`), so a person weighted
  toward the deontological pole prefers `accept` and the instrumental pole prefers `fight`; neither requires a challenge.
- **Issuing a challenge is mechanically empty.** It could expose you as the subject of a later `accept`; in seeds 0-2 no challenged person
  accepted, and four challengers used `accept` on their own challenged (§8 #6), at no risk to themselves (§5c).
- **Body is the whole build.** Kit, tradition, training and attributes are inert in the season; a trained fighter fights as an untrained
  one (`train` writes `capability`, unread by combat).
- **Dead end:** `tend` never executed in three seeds (0 of 75), so recovery is built but not reached; a Wounded body otherwise stays down. The verb works when it names a wounded person: a hand-built `tend`
  on oneself at body 250, run through the real season loop, raised it to 1000 with `body.tended` (the I1 verification's paired control, re-run on
  `51d7b05`). The computed `tend`s name a subject who is not a person in the world (dead, a rung, a record), one not `with` the tender, or a body
  already whole (§4); the self-targeted ones, 4 / 4 / 3 across seeds 0-2, were all refused.
- **Cohorts:** a cohort `Person` (one record standing for many) fights as one default fighter and is deleted whole by one Felled band.

### 5e What success leaves in the world
A Felled subject is gone with every tenure that named him (seats, holdings, edges), and witnesses hold `person.died` claims. A Wounded
subject keeps a lower body (fewer scenes, lower `end`). The winner gains nothing: no stance (only `march` and `forgive` write stance,
`EC:426`, ERRATA C1), no reputation, no custody, no record of how the fight went (the trace is discarded).

## 6 How it connects

| from / to | what flows | evidence |
|---|---|---|
| decision layer → PC | the chooser picks `fight`/`accept`/`challenge` and the subject; nothing tactical | `decision/choose.py:149-151` |
| NP body ↔ PC | `body` → `end` in; Wounded/Felled → `body` out; `tend` raises it | `SW:130-138`; `EC:134-151`, `:370-393` |
| PC → decision budget | each body band below a floor takes one scene action off next season's budget (budget 5 → 4 = 2+2 acts) | `budget.py:59` |
| PC → governance / tenures | a felling closes the dead person's tenures through `World.remove_person` (vacancy claims are not modelled, PC-G28) | `EC:178` |
| PC → information | band kinds are witnessed and deposited as claims; `challenge.issued` likewise | `VT:698-701`, `:731` |
| PC → scar | observers scarred per violated pursuit; inert at shipped shift | `loop/resolve.py:597` |
| MB → PC | a lost field lowers `body` (via `field_casualty_model`), which would lower a later duel's `end`; no realm seed reached a field | `EC` `_eff_march`; ctl `field.*` 0 |
| MATTER → PC | none at shipped values: hunger and ageing kill nobody, so every death in the run is combat | ERRATA G9 |
| dice engine → PC | the per-exchange roll uses the shared continuous sampler and the shared margin ladder; the season band does not | `MC/core.py:60-74`; ERRATA G5 |

**Combinations that work today:** information that puts a rival in your referents → `fight` → his tenures close. A rival already lowered
(by an earlier fight) is easier to fell. Nothing else stacks.

## 7 Playing it as proposed [PROPOSED]

All of this is intent in `proposals/2026-10-16-verbs/…-09-lexicon-personal-combat.md` (status PROPOSED, reference only; extract L09) and
the v9 remediation; none of it executes. Mechanic ids M1–M15 are the lexicon's; build order M1, M2, M14, M15, M3, M4, M12, M10, M5, M6,
M7, M8, M9, M11, M13.

- [PROPOSED] **Both parties take their band** (M1, K-PC-2): a felled attacker would die and the false `contest.undecided` would go.
  Attacking would then carry a ~51 % lethal risk in a mirror.
- [PROPOSED] **Cohorts may not fight** (M2, K-PC-12): a refusal conjunct `is_cohort`.
- [PROPOSED] **Distinct kinds** (M14): `fight.refused` instead of `kill.refused`; a duel kind on `accept`; `fight.yielded`, `fight.fled`.
- [PROPOSED] **A grudge on the survivor** (M15): a negative stance row from subject to actor, on `march`'s shape.
- [PROPOSED] **A real challenge** (M3, PC-10b): `challenge` mints a Record with terms, stakes and an optional `for`; `accept` must close
  one naming you. **Terms in the scene** (M4, PC-10a): `first blood` stops at the first wound, `yield` passes a Yield declaration,
  `death` refuses them — needs the seam to pass `yield_decl` (`MC/wrapper.py:487`).
- [PROPOSED] **How it ended** (M12, K-PC-9): the band's Event carries felled / yielded / fled / undecided and the decisive blow.
- [PROPOSED] **Co-location** (M10, IN-59 (a); blocked on IN-60): you could only fight someone at your place.
- [PROPOSED] **`capture`** (M5): a Felled or yielded subject taken into custody (`detain`); a seatless captor needs Jordan's ruling
  (L09 §3.9 item 2, overwrites ED-IN-0288). **`rescue`** closes a live `detain` by force.
- [PROPOSED] **`assassinate` / `ambush`** (M6): held cover (FI's `conceal`, which exists at `VT:207`) sets the first mover and withholds
  the actor from witnesses.
- [PROPOSED] **N-party scenes, `guard`, `interpose`** (M7 K-PC-5, M8; guard edge is L09 §3.9 item 1, Jordan's).
- [PROPOSED] **`shoot`** (M9): a missile kind inside the one resolver, never a second one.
- [PROPOSED] **Played fights** (IN-46, REM-31; L09 M11 / K-PC-4). IN-46's design (`GMS` §3, `:116-131`) suspends the one provider call and hands a
  seated player a per-turn decider over `wrapper.fight`'s turn loop: it reads the turn index and a read-only view of both fighters and returns
  one member of a closed set, **[ASSUMPTION] {engage, withdraw}**; it draws nothing. The mode is set by a party test at the seam (is a claimant a
  played person), not chosen per fight. L09 M11's menu (the Suite D moves `feint`, `lunge`, `parry`, `dodge`, `grapple`, `flee`, `yield`,
  `interpose`, one engagement per act; `L09:145-160`, `:329`) is what that set may widen to (`GMS` M-4, PC's Plan layer; `L09:52`); the
  per-engagement variant is open (`GMS:11-13`). D-2 (RULED yes, 2026-10-21) puts IN-46 in RB-3 (ERRATA G16; REM-31, `REM2:570-589`). IN-46
  changes who decides a turn, not who is written: a played attacker who is felled still stands (M1 is not a remediation item; `REM2:575-576`
  lists the files REM-31 changes, and `loop/effects_combat.py` is not among them).
- [PROPOSED] **Per-person inputs** (M13, K-PC-1, Jordan's): attributes, experience and kit reach the Combatant — the step that would make
  every row of the §3 pairing table reachable.
- [PROPOSED] **Contents-aware value term** (D-V6): would turn `accept`, `assassinate`, `capture` into contents of `fight`.

**Built but inert or stubbed today:** Yield (`MC/wrapper.py:467-513`, tested by `test_combat_yield`, never passed); `tempo_pressure`
"currently OUTCOME-INVISIBLE" by its own comment (`MC/combat_systems.py:1331-1340`); ability levers `edge_read`, `choke_control`,
`facing_regime` bare and `seize` dead (`MC/ability_primitives.py:17-26`); the swept fixtures `wound_harm_model` (`total`, `none` are
controls) and `combat_wounded_above` (`FX:624`, `:635`); `systems/combat/sim/combat.py` (v30) deprecated. `tend` executes 0 times in
the realm (§4).

## 8 Common mistakes and traps

1. **"My fighter's kit and training matter."** Not in the season: only `end` varies (`MC/fight.py:45`). Even in the full engine, tradition
   and abilities on equal arming swords moved the win rate by about one point (§3).
2. **"If I attack and lose, I die."** The actor is never written (`EC:107-109`); a felled attacker survives in the world at full body.
3. **"`contest.undecided` means nobody was hurt."** It means the *subject* was untouched; in 23.5 % of mirror fights it hides a felled
   attacker. So does `body.changed`: a Wounded band is a fight the attacker lost, bar one that ran 12 turns undecided (§5a). Over seeds 0-2,
   33 of 59 realm combat calls felled the actor in the scene (16 / 8 / 9) and none was written; the only harm combat writes besides a death
   lands on the person who won.
4. **"`winner` tells me who fell."** In about 4 % of decided fights the upset floor flips `result` and so `winner` names the felled
   fighter (17 of 400 control fights; `MC/wrapper.py:529-530`). Nothing writes from `winner`.
5. **"A grudge makes me likelier to attack."** Under the shipped `legacy` stance arm it makes it less likely (`FX:833`;
   `choose.py:54-79`).
6. **"`accept` answers a challenge."** It answers nobody's challenge: its cell refuses only a dead or absent
   challenger (`VT:742-749`). The "0 of 12" figure in that note was measured at IN-08 (seed 0, four seasons, 142 `accept` attempted, 12
   executed), not in this run. Re-measured on this run's recipe (per-act rows in fold order, seeds 0-2, two seasons, re-run on `51d7b05`): 0 of 39
   resolved `accept`s (18 / 9 / 12) follow a `challenge.issued` from their subject; a planted challenge is counted, so the test can see a link.
   The only challenge-linked `accept`s run the other way: the challenger accepts against the man he challenged (seed 0: fold positions 576 and
   939, both Felled; seed 2: positions 559 Wounded, 1080 Felled), and as the actor he is never written.
7. **"Season fights use footwork and reach."** Both fighters carry `arming` (reach 5.42), the gap is 0, so stop-hits, reopening and
   disengage never occur (control: 0 approach, 0 stop-hit, 0 disengage events in 400 fights).
8. **"Ob rises with wounds."** Ob is `defender.history/2` and nothing else (`MC/core.py:108-115`); wounds are a σ term.
9. **"The engagement's `first` swings first."** The cadence draw decides the first swing (worked example, turn 3).
10. **"Every hit is in the trace's `outcome` events."** The felling blow returns before its `outcome` is emitted (`MC/wrapper.py:386-394`).
11. **"A wound can kill."** Only Felled sets body 0; Wounded floors at 1 (`EC:151`).

**Where the draft appendix (A3, PC block) was wrong, and the correction:**
- A3 §2: "each [wound] adds fractional Ob via `WOUND_DEF_OB=0.25`, `WOUND_ATK_OB=0.15`" — wrong. Wound impairment is a **σ term** summed
  into net σ (`MC/combat_systems.py:1038-1044`, `:1103-1104`); Ob is history/2 only (`MC/core.py:115`; ERRATA C1).
- A3 §3: "`person.died` also has a matter source, hunger, so it is not combat-only" — at shipped values MATTER kills nobody; every realm
  death is combat (ERRATA G9). Confirmed: seed 0, 9 `person.died`, 9 from `fight` (2) + `accept` (7) (`t03/realm.py`).
- A3 §3 aperture counts (`fight` 4/4, `accept` 11/11, `challenge` 13/4, one season) — replaced by the control-run counts: `fight` 7/4,
  `accept` 18/11, `challenge` 23/6 (seed 0, two seasons; ERRATA C1, G2).
- A3 header "PC ~5,000 LOC" — `modules/combat` is 5,643 lines (`wc -l`; ERRATA G14).
- A3 §5 "recovery via `tend`" — `tend` is built but TESTS-ONLY by the grade rule: 0 of 75 attempts executed across seeds 0–2 (ERRATA C7).
- A3 §4 omits that `systems/combat/combat_engine_v1/state_graph.py` (duel state graph as data) and `capabilities.py` (weapon-affordance
  gates) exist (ERRATA C1).
- A3 §2's "band by the one ladder `degree_from_net`" is true of the per-exchange roll only; the season band never reads that ladder
  (ERRATA G5). A3 §3 already says so; keep the two apart.
- A3 §2 "most of the fight's variance is in those draws, not the roll" is labelled the writer's reading; it was not measured here.
- L09 (the lexicon) says `conceal` has no row; it does (`VT:207`).
- L09's 205/400 felled-actor figure was reproduced exactly (seeds 0–399, `t03/fights.py`).

**§8 Round-2 corrections** (audit2; each cited line opened before accepting):
- **Scene cost (CROSS C1, G-F4, L-X1).** The first version said "up to 5 scene actions" and "each verb costs one scene action". Wrong:
  the budget is 5 scene actions, a scene holds up to 3 acts, and a multi-act scene costs `extended_scene_cost` 2. Checked at
  `decision/budget.py:19-20` (returns SCENE ACTIONS), `FX:488-489` (3 per scene, extended cost 2), `decision/choose.py:643-657`
  (cost charged; a chunk cut to one act when only 1 is left), `loop/deliberate.py:252-259` (the driver charges `cost(ext)` and
  releases ≤ 1 scene per round). Budget 5 → 7 acts. Fixed in §0, §1, §4, §5b, §5c, §6 and the §3 note.
- **"Attempted" (CROSS C2, G-F1).** Accepted: `d.resolved` is appended in the fold (`loop/resolve.py:377-379`), and an admission refusal
  emits and `continue`s before it (`:1025-1032`). For `fight`/`accept`, attempted therefore means admitted and fought. Relabelled in §0 and §4.
- **0-of-12 `accept` link (G-F5).** It is an IN-08 four-season measurement, as `VT:749` says, not this run's. Fixed in §8 item 6.
- **Overwhelming wounds (G-F11).** 26 // 9 = 2 wounds, not 3; the worked example already said 2. Fixed in §2.5.
- **Stance weight (G-F12).** The term is `(1 + stance_gain) × stance` (`choose.py:84-86`), and `stance_gain` ships at 1.0 (`FX:847`), so
  the stance counts double. Fixed in §2.1. The sign conclusion (a grudge lowers `fight`'s score under `legacy`) is unchanged.
- **`tend` refusal split (L-X9).** I keep my split (18 absent / 2 not `with` / 14 whole) because it comes from the events' own `observed`
  tuples; the `with` check appears only on the 16 events whose subject existed. I now state that the kind is flat (`VT:1164-1165`) and the
  split is inferred. A split that reads 20 failed `with` is counting absent subjects as failing `with`.
- **Column order (L-X19).** Run columns are attempted / ok throughout, matching the ctl files.

### Round-3 corrections

Against `51d7b05` and the precedent suite (`PS/dispositions/D_T03.md`); each cited line was re-opened at the current tree before it was accepted.
- **§7 Played fights** (D_T03 row 50). Old: IN-46 "pauses per engagement so a seated player chooses `feint` … `interpose`". New: IN-46's design is a
  per-turn decider with an [ASSUMPTION] set {engage, withdraw}, chosen by a party test at the seam; the eight-move menu is L09 M11's. Evidence:
  `GMS:116-131`, `:11-13`; `L09:52`, `:145-160`, `:329`; `REM2:575-576` (REM-31 changes four files, none an effect file; a grep of the four
  remediation parts for `_eff_kill|K-PC|two-sided|PC-G09` finds nothing).
- **§8 #6** (row 26). Old: "the link was not re-measured". New: 0 of 39 resolved `accept`s (18 / 9 / 12) follow a `challenge.issued` from their
  subject; 4 challengers accepted against their own challenged. Evidence: the control recipe re-run on `51d7b05` (per-act rows in fold order;
  39 `accept`s, 0 forward links, 4 reverse links; a planted challenge counts 1).
- **§5d, challenge bullet** (row 26). Old: issuing a challenge "exposes you as the subject of any later `accept`". New: it could; in seeds 0-2 it
  did not, and the challengers were the ones who accepted. Same evidence.
- **§5a, wound row** (row 49). Old: "yes, by chance: 28 % of mirror fights; you cannot choose wound over kill". New: not by winning; a Wounded
  subject is one the attacker failed to fell. Evidence: `MC/wrapper.py:516-520`; §3's counts (206 non-Felled = 205 felled actors + 1 undecided);
  realm trace 15 of 15 Wounded calls had the actor felled.
- **§8 #3** (rows 25, 39). Added: `body.changed` hides a felled attacker as `contest.undecided` does; 33 of 59 realm calls (16 / 8 / 9) felled the
  actor and none was written. Evidence: seam-call trace, seeds 0-2 (59 calls: Felled 26, Wounded 15, Untouched 18), re-run on `51d7b05`, byte-identical.
- **§1 upset floor** (rows 22, 40). Added: the season band reads the subject's tracker, so the floor never reaches the world. Evidence:
  `MC/wrapper.py:526-530`; `seam/ladder.py:155-156`; `ROS:820-848`; nothing in `engine/season/` reads a combat `winner`.
- **§2.6 and §5c** (row 25). Old: "The actor's tracker is discarded". New: both wound states reach the effect (`SW:230`, `:237`) and `_eff_kill`
  reads the subject's only (`EC:125`). The §5c wording follows §2.6; the fact that the attacker is never written is unchanged.
- **§5d, dead end** (row 4). Added: `tend` works on a wounded person (hand-built, body 250 → 1000, `body.tended`); the computed ones are all
  refused (self-targeted 4 / 4 / 3). Evidence: control re-run through the real season loop on `51d7b05`; `EC:385-393`.
- **§5c, risk to the attacker** (row 24). Added: 33 of 59 realm calls, and `p_npc_004`'s tick-1 chain (body 650, then 48, then felled attacking,
  body 48 at the end of the run). Evidence: seam-call trace calls 22-24, seed 0; `p_npc_004` body 48 after season 2.
- **Line numbers moved by PR #494** (no claim changed). `FX:823` → `833`; `FX:837` → `847` (+10 lines after `FX:716`). `ROS:2561-2564` →
  `2627-2630`; `ROS:3280`, `:3346` → `3346`, `:3412`; `ROS:3236`, `:3280-3283`, `:3346-3348` → `3302`, `:3346-3349`, `:3412-3414`; the §9 ranges
  likewise (+66 lines after `ROS:2488`). Each new line was opened. `MC/`, `SW`, `EC`, `VT`, `budget.py` and `resolve.py` did not change.
- **§0a is new.** Its draft was re-verified against the tree; changed on the way: the King's "budget of 3" is dropped (the budget also counts held
  offices); "no ending" is restated for PR #494 (the season now reports `endings`; the realm as built reaches none); the loser-takes-the-harm line
  cites Battle Brothers, Jagged Alliance 2 and XCOM only (Kingdom Come: Deliverance §6 says death reloads the last save, which does not show it);
  the callback paragraph names the one test that hand-builds a `fight`.
- Not changed, noted: §8 #2 says a felled attacker survives "at full body"; true of the mirror example, not of `p_npc_004` above.

## 9 Checks

Opened (path:line): `MC/fight.py:32-69`; `SW:85-253`; `engine/season/decision/budget.py:55-83`; `FX:217, 228, 623-640, 833`;
`ROS:784-870, 1268-1300, 1465-1470, 2586-2630, 3302, 3339-3349, 3402-3414`; `VT:612-765, 1146-1168`; `EC:30-179, 360-396`;
`MC/wrapper.py:18-27, 440-465, 467-532`; `MC/core.py:50-75, 100-127`; `MC/combat_systems.py:1036-1046, 1086-1104`;
`engine/dice_engine/sigma_leverage.py:95-160, 299-330`; `engine/dice_engine/dice_engine.py:227-257`;
`engine/substrate/pc_engine.py:30-52`; `engine/season/decision/choose.py:54-84, 140-151`; `engine/season/loop/resolve.py:597-610`.
Other figures (weapons, traditions, outcome-map probabilities, sigma-term formulas) are from extract C08, spot-checked where cited above.

Ran (read-only, `python -I`, scripts under `$SP/t03/`):
- `derive.py` — derived stats for `end` 1–4; pools for history 1/3/5/7; `TRADITION_KIT`; 54 weapon keys; exchange-band odds; sampler
  mean 3.591 / s.d. 2.396 at pool 9.
- `fights.py 400` — season entry `modules.combat.fight.fight` at ends (4,4), (4,1), (1,4): results, bands, turns, rolls, damage.
- `seam.py` — `SW.resolve` on `build_realm(0)` persons `p_npc_001` vs `p_npc_002`; the trace in §3.
- `pairs.py 400` — 15 pairings through `MC/wrapper.fight`; the control equals the season entry's numbers.
- `realm.py 0 2` — per-act bands for `fight`/`accept`/`challenge`, refusal observations, `tend` refusals, deaths.
- Arithmetic for wound impairment (+0.595 net per defender wound) by inline `python -I -c`.
- Read `ctl/realm_seed{0,1,2}_2seasons.txt` for the execution counts.

Not confirmed: why the chooser forms acts against persons never in the realm (observed, not traced); the wear row `body: 10`
(`ROS:1468`) was not traced to a person-side reader. The budget question (ERRATA G11) is settled by CROSS C1, whose cited lines I opened
(`deliberate.py:252-259`, `choose.py:643-657`, `FX:488-489`, `budget.py:19-20`).

Round 3 (against `51d7b05`) opened: `GMS:1-249`; `L09:23, 52, 145-160, 164, 316, 329`; `REM2:570-589`; `seam/ladder.py:136-185`; `offices.yaml:182-188`;
`loop/driver.py:514-532`; `queries/world_q.py:1764-1795`; `ROS:2490-2545`; `engine/season/tests/test_combat_trace_returned.py`; the precedent
sections cited in §0a. Ran (read-only, `python -I -B`): the seam-call trace of seeds 0-2, two seasons (59 calls; byte-identical to the earlier
trace); the per-act link count (39 `accept`s, 0 forward, 4 reverse; positive control 1); a hand-built self `tend` at body 250 (→ 1000); the final
body of `p_npc_004` (48). The probe scripts are not committed.
