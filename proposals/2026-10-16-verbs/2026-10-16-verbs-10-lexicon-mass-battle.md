# Verbs, v2 — part 10: Part VI.2, mass battle (the force and the field) (MB)

## Status: PROPOSED (2026-10-17). Reference, not canon (`CLAUDE.md` §0.05): nothing here binds the game or is read by it. Merging ratifies nothing unless Jordan so rules. Static reading and static lookup only; no run.
## Parts, in reading order: [head](2026-10-16-verbs-01-thesis-and-persons.md) (§0, Part I Persons) · [`verbs-02`](2026-10-16-verbs-02-attributes.md) (Part II Attributes) · [`verbs-03`](2026-10-16-verbs-03-standards-roster-and-reconciliation.md) and [`verbs-04`](2026-10-16-verbs-04-critics-etymology-gaps-and-decisions.md) (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`verbs-05`](2026-10-16-verbs-05-what-verbs-do-to-the-world-1.md) and [`verbs-06`](2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md) (Part IV What verbs do to the world) · [`verbs-07`](2026-10-16-verbs-07-roadmap-reliability-and-sources.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`verbs-08`](2026-10-16-verbs-08-engine-findings-from-the-first-trial.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: [`verbs-09`](2026-10-16-verbs-09-lexicon-personal-combat.md) PC · **this file** MB · [`verbs-11`](2026-10-16-verbs-11-lexicon-social-contest.md) SC · [`verbs-12`](2026-10-16-verbs-12-lexicon-fieldwork-and-inquiry.md) FI · [`verbs-13`](2026-10-16-verbs-13-lexicon-threadwork.md) TW · [`verbs-14`](2026-10-16-verbs-14-lexicon-settlements-and-governance.md) GV · [`verbs-15`](2026-10-16-verbs-15-lexicon-faction-actions.md) FA · [`verbs-16`](2026-10-16-verbs-16-lexicon-economy-trade-and-craft.md) EC · [`verbs-17`](2026-10-16-verbs-17-lexicon-world-travel-and-survival.md) WT · [`verbs-18`](2026-10-16-verbs-18-lexicon-npc-life-and-persons.md) NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`verbs-19`](2026-10-16-verbs-19-gap-register-pc-and-np.md) PC+NP · [`verbs-20`](2026-10-16-verbs-20-gap-register-mb-and-fa.md) MB+FA · [`verbs-21`](2026-10-16-verbs-21-gap-register-sc-and-gv.md) SC+GV · [`verbs-22`](2026-10-16-verbs-22-gap-register-fi-and-tw.md) FI+TW · [`verbs-23`](2026-10-16-verbs-23-gap-register-ec-and-wt.md) EC+WT.

**How to cite this Part.** The lane's own sections are numbered 3.1 to 3.9; cite them as `MB §3.n` (for example `MB §3.9` for its items for Jordan). Gap ids (`MB-G01` …) resolve in Part VII (`verbs-20`). Abbreviations such as `VT`, `VCD`, `v2-p3` are defined in the lane's opening paragraphs; `v2-p3`, `v2-p4`, `v2-p8` are the first-pass v2 parts as filed at `716c253`. Old file names such as `…synthesis_part8.md` or `_part8` in the body also mean those first-pass files; the suite was later renamed `2026-10-16-verbs-NN-…`. Mechanic ids (`M1`, `M-1`, `M-WT-1`) are this lane's own.

**Rulings that override this section** (`verbs-03` §III.5; where this section and the roster disagree, the roster governs):

- R-01: the separate `recruit` row folds into **`levy`** (a terms parameter); `recruit` the word is FA's act on a person.
- R-03: `raze` and `fortify` are GV's `raze` and `build`; MB keeps no row for either.
- R-08: `forage` and `sack` stay MB's; `camp` / `encamp` is WT's and parked.
- R-19: `surrender` is MB's row; `yield` is PC's scene move.
- R-25: `ambush` has two hosts (`fight`, `march`) for one meaning.

---

# MB — mass battle (the force and the field)

Lane: MB. Read at the working tree, HEAD `716c253` (after `requisition` and `seize`/arrival landed).
Reference only (CLAUDE.md §0.05): nothing here changes behaviour. Register rows are MB-G01…MB-G57 of
Part VII (`verbs-20`). Abbreviations are the register's (VT = `engine/season/verb_table.yaml`,
TS1/TS2 = the troop-stock design and its `_part2`, PW, PFF09, PFF10, PMM, COMP1, AFS, VCD, p3/p8 = v2
parts). Etymology sources: **Wikt** = en.wiktionary via the lane tool; **L&S** = Lewis & Short via the
tool's `ls` route. Anything not opened is tagged `[UNVERIFIED]`; a game named from memory is `[MEMORY]`.

**The one structural finding that shapes everything below.** Under TS1's default troop body (A), men
are counts in a settlement's `Rung.stores` that "fight for whoever holds the walls" (TS2:19-21), and
`march`'s arrival moves **persons** only (VT:698-701 write `Tenure.*` and `Person.travel_leg`), while
TS2 §4.6 writes casualties on stocks left at the origin. So a won march today, and under TS as drafted,
**arrives without its men**, and a stock carried into an enemy town would fight for the enemy. Every
act of a force away from its own walls (besiege, forage, sack, encamp, provision, ambush) waits on one
mechanic: **the field force**, a body of stocks that travels with its marchers and keeps the allegiance
of the faction that raised it (§3.7 M-1). This is named as a gap; it is not a reason to fold those verbs
into others (the lane brief rule 6).

---

## 3.1 Subsystem mechanic

**Shipped.** One MB row, `march` (VT:683-711): `remit:dispatch`, `contested_physical`, contests "a
field"; on the losing side writes `Person.body`/`Person.stance` only (ED-IN-0279, VT:702); since IN-13 a
`Won`/`Unopposed` march relocates its claimants (VT:698-701) and emits `army.arrived`. The field runs
through `seam/wrappers/mass_battle.py` into `modules/mass_battle/massbattle.py`, which builds **one
Line subunit per side** sized by summed `Person.weight`, power 4, command 4, discipline 5
(`massbattle.py:170-230`), graded Won/Lost/Unopposed by `field_degree` (`seam/ladder.py:185-206`). A side
is `mustered` persons present (`world_q.py:1257`); defence reads the garrison Site's `condition`
(`fortification_of`, `world_q.py:1277`). Occupation is a Query with no larder reader (H-212,
`hole_register.yaml:4549`). Adjacent rows MB reads: `seize` (VT:898, a Rung's hold under occupation,
`remit:issue`), `requisition` (VT:646, the store act), `transfer` (VT:1247).

**Built in the module, unreached by the season.** Stances `aggressive/balanced/hold/retreat`
(`config.py:290`), brace and shock rows, `pursuit_damage` and `recall_check`
(`orchestration.py:2549-2590`), feigned retreat (`:2593-2626`, `MB_FEIGNED_RETREAT` default on), a
reserve commit fixed at turn 2 (`config.py:258`), a Command-gated `reform_check` (`orchestration.py:297`),
an emergent yield-rally (`config.py:270-271`), `derive_command` (`core/exchange.py:57`), and two empty
hooks, `rally_check` (`orchestration.py:288-290`) and `threadwork_check` (`:333-335`).

**Absent.** A troop stock (`matter_kinds` = grain, salt, timber, ore, coin; `rosters.yaml:1308`); any
act that raises, assembles, equips, drills, pays or disbands men; an order-of-battle carrier; the field
force (above); an occupier's larder draw (H-212); a death carrier (H-152); a grade (experience) carrier.

---

## 3.2 Convention floor

What a player of a pre-modern strategy game with a field layer expects the force to do. Each is kept
(the lane brief rule 4); the open question is only how much is built.

| floor act | precedent (in-tree opened · game) | state today |
|---|---|---|
| **raise** men from one's land, by obligation | PW:45-51 §1.3b (feudal levy, fixed term); PMM:465-470 M-6 (CK levies "a standing entitlement drawn down … never economically"); CK3 levies from holdings `[MEMORY]` | **designed** (TS1 §3.1 `levy`); absent in VT |
| **recruit** men for coin | PMM:465-480 M-6 (CK men-at-arms: gold plus maintenance; JA2 bought regulars); PW:48-49 (professionals "serve as long as they're paid"); Total War: recruit a unit for gold, pay upkeep each turn `[MEMORY]` | **absent**; TS1:806 refused it as minting men from matter |
| **assemble** the raised men at one place (and garrison a place) | PW:110 §3.1 (vassals summoned bring retinues); COMP1:322-325 (garrison is an assignment of the one pool, 4/4); CK3 raised levies gather at a rally point `[MEMORY]` | **absent** as an act; TS1:803 makes it a Query |
| **equip** men | PW:118 §3.2 (Wealth gates professional equipment); PMM:486-498 M-7; Mount & Blade: troop upgrade changes a troop's kit and type `[MEMORY]` | **designed** as `transfer` (TS1:792); not reachable (no arms producer) |
| **drill** men (quality by training and service) | PW:112 §3.1 (Swiss militia "trained regularly"); COMP1:340-342 (Shogun 2 ashigaru earn honour: gap is a floor); PFF10:485-489 Obs 7 (training institutions) | **designed** as `train` (p8:418); no reader on a stock |
| **arrange** the army (order of battle, commanders) | PFF10:441-457 Obs 1-2 (deployment; the decisive commit); PFF10:473-477 Obs 5 (anvil and hammer roles); Total War pre-battle deployment `[MEMORY]` | **built in harness** (`build_army`); no season act |
| **march** on a place | shipped | **shipped** VT:683 |
| **camp** | PFF10:47 Phase 0 (fortified camps); Total War: Rome II/Attila camp stances `[MEMORY]` | **designed**, cut by v2 (p8:409) |
| **forage** / live off the land | PW:34-36 §1.3a (3 days carried, ~10-mile forage radius); Total War: Attila raiding stance takes supplies from the land `[MEMORY]` | **designed** (v2 → `requisition`, p8:411) |
| **supply** a force | PW:37-41 §1.3a (supply lines lift sieges); CK3 army supply/provisions `[MEMORY]` | **designed** (v2 → `transfer`, p8:412) |
| **besiege** | PW:78-82 §2.1 (HYW: most territory changed by siege); PW:86-92 §2.2; CK3 siege progress to capture `[MEMORY]` | **designed** (v2 posture `invest`, p8:413) |
| **assault** (storm) | PFF10:392-396 Archetype 5 (final storm); Total War: assault a besieged settlement `[MEMORY]` | **designed** (v2 posture `assault`, p8:421) |
| **pursue** | PFF10:268-294 Phase 7, 509-514 Obs 10; module `pursuit_damage` | **built in module**; not on the season path |
| **retreat** | PFF10:294, 513 ("an army that withdraws in good order should be reusable"); module `retreat` stance | **built in module**; season collapses it (R-7) |
| **surrender** (a place or a force, on terms) | PW:100-102 §2.3 ("most sieges ended in negotiated surrender"); PW:82 (Osaka); FASE:134-140 T6 | **designed** (v2 preset of `give`, p8:420) |
| **disband** | PW:64 ("raise, fight, disband"); PMM:397-403 (Medieval II requires manual disbanding; Shogun 2 culls); CK3 disband returns levies home `[MEMORY]` | **absent** (TS1:805, "Jordan's to ask for") |

Beyond the floor, argued by NERS and precedent in §3.3: rally, withstand, reconnoitre, sack, raze,
ambush.

---

## 3.3 Suites

Four suites. The fold test is the lane brief rule 5: **A** same actor? **B** same subsystem mechanic? **C**
differing only in a parameter or content? A fold needs three yeses; otherwise the act is a sibling row
in the suite, its own verb. "Season" marks an act chosen in the season loop (a verb row); "in-battle"
marks a choice the battle module resolves inside the field (a content of another row, never a row).

### Suite 1 — Raising and keeping the force (host `levy`)

**Members.** `levy` (host), `recruit`, `muster` (with `garrison` folded), `drill`, `disband`. All
season acts; eligibility `remit:dispatch`, the remit `march` uses (VT:687) and TS1:702 gives `levy`.

| act | A | B | C | result |
|---|---|---|---|---|
| `recruit` into `levy` | Y | **N** — it debits coin from the seat's treasury and writes no consent cost; PMM:465-470 M-6, "different economies, not different tiers" | N | sibling row |
| `muster` into `levy` | Y | **N** — it moves existing men between settlements; `levy` mints men from the pool on one rung | N | sibling row |
| `garrison` into `muster` | Y | Y — stocks moved to a settlement the faction holds | Y — the destination is the place they will defend (COMP1:322-325: garrison is an assignment of the one pool, 4/4) | **FOLD** |
| `drill` into `levy` | Y | **N** — moves men up a grade on the same rung; writes no pool | N | sibling row |
| `drill` into `train` (v2 p8:418) | **N** — `train`'s learner is a person (J-13 (iii)); `drill`'s object is a stock | **N** — a person's capability vs a stock's grade | N | sibling row; v2's merge rejected |
| `disband` into `levy` | Y | Y (pool ↔ stock) | **N** — sign-opposed; ordinary English treats raising and disbanding as opposite acts, so one name fails the ED-IN-0179 test | sibling row |
| gathering by `transfer` (TS2:247) | **N** — `transfer` is `remit:issue`/`own`/`hold:<store>` (VT:1249) | **N** — EC's store move | — | rejected: men move by `muster` and `march` only |

**World effect.**
- `levy`: `Rung.stores` `recruits` → `troops_raw` on one settlement (TS1:775-776), **plus one `stance`
  row on the resident cohort toward the seat's faction** (TS1:683-686 names it "the one lawful carrier";
  PW:118 "you can't muster effectively from a hostile population"; PMM:433-441 M-3, JA2 and RoTK VIII
  charge loyalty per head). Emits `levy.raised`. Waits on M-2, M-8.
- `recruit`: `recruits` → `troops_raw` on the settlement, **and** coin from the seat's treasury
  (`Act.via`'s rung, `requisition`'s destination precedent, VT:652) by a price per weight unit; no
  stance row. Draws the same pool, so R-POOL holds and TS1:806's objection ("it mints men from matter")
  is answered: coin buys men already in the pool. Emits `recruit.made`. Waits on M-2, M-8.
- `muster`: troop kinds move from `from` (a settlement in the seat's purview) to `subject` (a settlement
  the faction holds), through `_shift`, the one body of a two-rung move (VT:671). Emits
  `army.mustered`, a witnessed act: the threat signal FASE FA-5 weights and GD-2's "draws a muster"
  (MBL:445 M-MB-12). [ASSUMPTION: one source per act, `transfer`'s operand shape — basis: the closed
  operand set; gathering three towns is three musters of one verb, not a composition.]
- `drill`: `troops_<g>` → `troops_<g+1>` on one rung, capped below the top grade (veterans only by a
  field, J-5 (c)); cost [OPEN — coin, or the stock may not march that season]. Emits `troops.drilled`.
  Waits on the grade roster (TS1:581-588; M-2) and on J-1, since a grade carrying a discipline offset is
  the NEVER-list strain TS1:588-589 names.
- `disband`: `troops_<g>` → `recruits` on the same settlement, capped at the pool's ceiling; grade is
  lost. Emits `army.disbanded`. Waits on M-2.

**Why `transfer` and `requisition` should stop moving men.** TS1:791-793 lets `requisition` move a troop
stock into a settlement treasury and `transfer` gather troops. With `muster` owning the move of men, both
lose their troop special cases (`placeable` keeps only "no `recruits`"): one owner per operation
(CLAUDE.md §8), and E improves (§3.5).

**NERS.**
- **N.** Cut `levy` → no army exists at a realistic scale (MB-G01: every opposed march grades Lost;
  `massbattle.py:226` feeds summed weight). Holds bottom-up (settlement → field), top-down (a faction
  cannot build a host), vertical (R-POOL's pool has no reader). Cut `recruit` → coin cannot become force,
  and the only cost of war is consent: holds laterally (EC ↔ MB) and horizontally (levy has no rival
  option). Cut `muster` → an army is the levy of the one town its general stands in (TS2:251-253), and a
  threatened town cannot be garrisoned (GD-2): holds top-down and laterally (FA's threat → MB). Cut
  `drill` → experience has no producer short of J-5 (c), which is Jordan's; holds bottom-up only:
  **narrowed** — "a seat can buy quality with time instead of blood". Cut `disband` → a levy is a food
  sink whose only end is hunger or death (TS1:796); holds bottom-up (larder) and horizontally (no
  raise-fight-disband cycle, PW:64).
- **False N-line check.** `muster`: is "assemble" already carried? `mustered` (`world_q.py:1257`) reads
  persons present and moves nothing; `march` moves persons and, under TS, no stocks. Disqualifier 1
  fails to fire: no shipped object moves men between settlements. `recruit`: does `levy` already
  provide "men for coin"? No: `levy` writes no coin. Disqualifier 5 (flat bonus): `drill`'s residue is
  a grade step, a discrete state the module reads as preset offsets, not "+X" on a pool. No false N-line
  found; trail as above.
- **R.** R-CHOICE: levy (consent cost, free) against recruit (coin, no consent cost) is a real trade
  only because the cost carriers differ; without the stance row, levy dominates recruit and the seat is
  a corridor. Keep veterans (food) or disband (lose the grade): a real choice. R-WORLD: an NPC seat that
  over-levies hardens its own towns against it, a hook nobody scripts.
- **S.** Methodology: `levy` and `recruit` share `requisition`'s typed cell (purview + stores
  threshold, TS1:745-746); `muster` shares `transfer`'s `_shift`. Pauses: none needed — all season acts.
  Scale: settlement (pool) → faction (purview) → field (`fielded`, TS2:18-21).
- **E (last).** Five rows against five floor acts (raise, recruit, assemble, train, disband) and two
  special cases removed from `transfer`/`requisition`. Ratio favourable; folding any two would put two
  world effects behind one name.

**Precedent.** §3.2 rows raise, recruit, assemble, drill, disband.

**Gaps.** Closes MB-G01, G02, G07, G08, G12, G13, G14, G25 (with Suite 2), G51, G53. Leaves open
MB-G54 (the pool by settlement kind: SE data) and the service term and upkeep (§3.9 item 2).

**Disposition.** `levy` NEW ROW (TS1 §3.1 plus the stance write) · `recruit` NEW ROW · `muster` NEW ROW
(`garrison` FOLD) · `drill` NEW ROW · `disband` NEW ROW. **Falsifiers.** `levy`: a seeded levy that
raises no stock or moves the cohort's `weight` (R-POOL). `recruit`: a run where recruiting and levying
leave identical world states. `muster`: a computed army that reaches a field with stocks from two
settlements without a `muster` in the log. `drill`: a drilled stock whose band distribution over N
seeds equals an undrilled one. `disband`: a disbanded stock that is not re-levyable next season.

### Suite 2 — Ordering the force (host `marshal`)

**Members.** `marshal` (host, season act). Folded, all in-battle: `rally`, `pursue`, `retreat` (with
the feigned retreat as a parameter), `withstand`, the reserve and its release, formation/stance/role
per subunit, and who leads which subunits. `command` is culled as a verb name.

**World effect.** `marshal` writes the **standing order of battle** of the force at a settlement: a
Record of kind `order_of_battle`, held by the marshalling seat, about that rung (M-3). `order_of_battle`
(TS2 §4.2) reads it whenever that force fights, **attacking or defending**. It replaces TS2 §4.3's
`order` payload on `march`, so one spec list has one owner (the shape condition at p8:205). Emits
`army.marshalled`. Absent a Record, the module's defaults stand (TS2:171-174).

**Why a row and not `march`'s operand.** The defender does not march, so an order carried only by
`march` leaves the defender's choices with no chooser — v2's MB call 4 (p8:661: `withstand` "a
choice vs a portrait … flips if no act the defending seat already makes can carry the garrison's
order"). No shipped act can: `dispatch` writes nothing (VT:276). So the flip condition holds, and
`marshal` is that act. NPC5's need (`cases/NPC5.yaml:172`, quoted at MBL:436: a commander "must be able
to command levies or forces distinct from the council's collective decision-making") is met by the
order naming the general and officers.

| folded choice | in-battle mechanic it sets (module) | A | B | C | season-scale effect |
|---|---|---|---|---|---|
| formation, stance, role per subunit (v2's "tactic", V116's choice half) | `build_army` spec, `role_allowed`, `STANCE_COMMITMENT` (`config.py:290`) | Y | Y | Y | via the field result only |
| who leads which subunits | officers and span (`trim_to_command`, TS2:186-189) | Y | Y | Y | NPC5: a commander who breaks with his council takes his order |
| `rally` | `rally_check` filled (M-4): officers ordered to rally roll a Command pool against Ob 2 (`recall_check`'s method, `orchestration.py:2585-2590`) and restore **a fraction of the subunit's lost morale**, within their own span | Y | Y | Y | the rallying officer's exposure is the mass → personal yield (K-MB-10, Jordan's) — PARKED half |
| `pursue` | pursue / hold on the enemy's rout: `pursuit_damage`, `recall_check`, the feint check (`orchestration.py:2549-2626`) | Y | Y | Y | more of the loser's men die; deaths by name wait on K-MB-9 |
| `retreat` (+ feigned) | a threshold at which the side takes the `retreat` stance and leaves the field; the feigned flag (`MB_FEIGNED_RETREAT`) | Y | Y | Y | a withdrawn army keeps its survivors in order; waits on M-5 (R-7) |
| `withstand` | `hold`/brace on chosen subunits (`MB_SHOCK_HOLD_BRACE`, `MB_BRACE_ENABLED`) | Y | Y | Y | via the field result |
| the reserve and its release | `MB_RESERVE_COMMIT`, today the constant `RESERVE_COMMIT_TURN = 2` (`config.py:258`) | Y | Y | Y | PFF10:447-457 Obs 2's decisive commit becomes a choice |

All seven pass the fold test: same actor (the marshalling seat), same mechanic (the one spec list the
module reads), differing in content. Under a played fidelity (MB-G49, J-C-31) the same contents are
issued live; the lexicon does not change.

**MB-G28, `rally_check`: fill, not delete.** K-MB-11's order is conditional: "Delete … until a design
gives each a reader" (MBL:735). This suite gives `rally_check` a body and a chooser, so the condition is
met; K-MB-11 stands for `threadwork_check` (TW's). The fill is not redundant with what exists:
`reform_check` restores Discipline to **unengaged** units only (`orchestration.py:297-331`), and the
yield-rally reverts a yielding subunit **with no commander** at 75% morale (`config.py:268-271`). A
commanded rally of an engaged, breaking subunit is carried by neither. Precedent: PFF10:242 ("Officers
attempt to rally; sometimes successful at small scale; rarely successful at army scale"), which the
span limit models. The archived canon form, "+1 Morale" on Command Ob 2
(`.designs/…/mass_battle_integration_v30.md:271`), is reference only and is the flat shape MB-G55
forbids; the fraction replaces it.

**MB-G55, "a personal→unit effect is a fraction, never flat": it bears on the form, not the
existence.** The rule's own text (MBL:158, Dominions row) constrains the size of a person's effect on a
unit, and its evidence is `[UNVERIFIED — player-community consensus]`. `rally` as a fraction of lost
morale on a Command-sized pool satisfies it; `command` is no longer a verb (below), and the Command
stat already enters the module as a pool size (`recall_check`, `pursuit_damage`'s PP-233 pool), which
is the sanctioned methodology. The shipped violation is elsewhere: `Command=0 → instant rout`
(`orchestration.py:2221`), K-MB-10's subject. So p3:215 ("against a `command` verb or a `rally` verb")
is answered: against their flat forms only.

**`command` culled as a verb (V-10 applied).** V116 bundled two things: the Command stat drawn from a
seated person (`derive_command`, an input: K-MB-2, R-C-1) and the commander's choices (now `marshal`'s
contents). "Command" is the canonical mass-combat stat (`references/synonym_registry.yaml:29-31`), so a
verb of that name would put the stat's word on an act. V-10's replacement, `tactic`, is a noun and names
no act in the actor's voice, so it is not adopted either. **What dies:** nothing; the stat is an input,
the choices are contents. **Falsifier:** an act that seats a commander and writes something no
`marshal` content and no FA/GV `confer` of a military office carries.

**NERS.**
- **N.** Cut `marshal` → the defender has no chooser (MB call 4), the decisive commit stays a constant,
  and the built menus (roles, formations, brace, pursuit, feint) never become decisions (MBL:438
  M-MB-5, "the only decision in mass battle is whether and where to march"). Holds top-down (the seat's
  intent reaches the field), bottom-up (module rows reach a chooser), laterally (attacker and defender
  both choose), vertically (a person's appointment reaches subunits). False N-line check: does `march`'s
  operand already carry it? Only for the attacker, and that operand is not built — disqualifier 1 does
  not fire.
- **R.** R-CHOICE and customization: the same stocks fight differently by order (K-MB-4's falsifier).
  R-WORLD: a defender's standing order and a reserve held too long are hooks with no player in them.
  R-completeness: `rally` capped by span keeps the army-scale extreme from becoming a flat save.
- **S.** Pauses correctly: the season act sets orders; the field resolves them without returning to
  the loop (one atomic field call, `massbattle.py:283` per MBL:437). Methodology: every in-battle roll
  is a Command or Discipline pool against an Ob, as `recall_check` and the feint check already are.
- **E (last).** One row hosting seven contents, against seven named choices v2 kept and a defender with
  no chooser. Ratio strongly favourable.

**Precedent.** §3.2 "arrange", "pursue", "retreat"; PFF10:473-477 Obs 5 (anvils hold position =
`withstand`); PFF10:242 (`rally`); PFF10:509-514 Obs 10 (`pursue` as its own decision).

**Gaps.** Closes MB-G04, G05, G06, G10, G11, G26, G27, G28, G29, G30, G31, G45, G46, G47, G48, G55.
Leaves open MB-G09 (K-MB-10), G36 (K-MB-9), G49 (fidelity).

**Disposition.** `marshal` NEW ROW. `rally`, `pursue`, `retreat`, `withstand` FOLD (in-battle). `command`
CULL as a verb. **Falsifier for the host:** two fields with identical stocks and different marshalled
orders that give the same band distribution over N seeds.

### Suite 3 — The campaign (host `march`)

**Members.** `march` (host, shipped) with two postures folded, `storm` (the default) and `besiege`;
sibling rows `supply` (with `provision` and `equip` folded), `forage` (with `sack` folded) and
`encamp`; `reconnoitre` and the field half of `ambush` PARKED. All season acts.

| act | A | B | C | result |
|---|---|---|---|---|
| `storm` into `march` | Y | Y — the field fought at arrival, today's behaviour | Y — a posture value | **FOLD** (default) |
| `besiege` into `march` | Y | Y, narrowly — `march`'s move onto a Rung; the posture selects whether the field is fought at arrival, and the per-season effect is a reader of the state the march leaves (M-6) | Y — a posture value | **FOLD**; the convention shape (a siege begins when a force sits before a place, and an assault is a later choice: CK3, Total War `[MEMORY]`) |
| `besiege` as its own row (v2 MB call 2) | — | — | — | rejected: the act a seat chooses is the march; what follows is a state and its reader |
| `supply` into `transfer` (v2 V111) | **N** — `transfer`'s eligibility (VT:1249) is not the commanding seat's | **N** — the destination is the force's own stores (M-1), which EC's verb does not know | — | sibling row |
| `provision` into `supply` | Y | Y — stores into the force's stores | Y — the kind is food | **FOLD** |
| `equip` into `supply` | Y | Y — stores into the force's stores; `kind_for_kit` (TS1:591-602) reads kit where the men stand | Y — the kind is arms | **FOLD** |
| `forage` into `requisition` (v2 V110) | **N** — `requisition` is a seat's `remit:issue` act into its treasury (VT:650-652); forage is the force's commander taking where the force stands | **N** — GV/EC's store act | — | sibling row |
| `sack` into `forage` | Y | Y — stores of the place the force holds, taken by force | Y — content: every kind, all of it, from a place taken by `storm`; own event kind | **FOLD** |
| `encamp` into `build` | **N** | **N** — `build` mints a settlement's Site; a camp is the force's | — | sibling row |
| `reconnoitre` into `surveil` (v2 V107) | **N** — the force's scouts at range vs a person present (VT:1186-1190) | **N** — FI's inquiry | — | not a fold; PARKED as MB's |

**World effect.**
- `march` (REBUILD; the row stands, its effect widens): reads `marshal`'s order (Suite 2); carries the
  posture; **moves the fielded stocks with the marchers on `Won`/`Unopposed`** and keeps their
  allegiance (M-1); writes TS2 §4.6's casualties on stocks and the garrison's `condition`. `storm`
  fights now, walls graded by the garrison's `condition` (H-150; TS2:74-77). `besiege` arrives
  **before** the place without a field and leaves a siege state (M-6): each season the place draws no
  supply from outside, the besieger eats from its own stores, the garrison wears, and an event is
  witnessed (p8:413's condition). A later `march` with `storm` from the siege is the assault. The
  besieger's terms offered are a `besiege` content read by `surrender` (Suite 4).
- `supply`: food (`provision`) or arms (`equip`) move from a settlement in the seat's purview into the
  force's stores (M-1); the stock eats from them (TS1 §2.5's draw, re-pointed) and is armed from them
  (`kind_for_kit`). Emits `force.supplied`. **Until M-1 the home case is EC's `transfer` into the
  settlement where the men stand, and `supply` writes nothing of its own** — named, not hidden.
- `forage`: stores from the rung where the force stands (one not held by its faction) into the force's
  stores; the residents' larder falls. Emits `stores.foraged`. `sack` (content): every kind, licensed
  only on a place the force took by `storm` this season (FASE:134-140 T6: a town taken by storm forfeits
  protection; surrender on terms keeps it); emits `town.sacked` so a witness can judge it (FASE:219-222
  FA-6 (c), "reputational contagion"). Harm to the townspeople's bodies waits on a cohort-weight writer (H-49), as v2 says (p8:422).
- `encamp`: the force halts where it stands outside walls and makes camp: a `camp` Site whose
  `condition` (field works) `fortification_of` reads if the force is attacked there (M-12); while
  encamped it does not travel and eats from its stores. Winter quarters are this act (v2 MB call 1).

**The false N-line check on `forage`.** H-212's reader, once built, makes an occupier eat the occupied
larder automatically, so "an army feeds off the land" survives a cut of `forage` (disqualifier 1). What
dies with the cut is narrower: **carrying the land's food away** so the force can stay elsewhere, and
**stripping a district to deny it** (PW:80, chevauchée). N holds, narrowed to that.

**NERS.**
- **N.** `march`: the only act that contests ground (p3:253). Postures: cut `besiege` → "a march that
  stays" is a non-act (p8:556) and siege — "Most territory changed hands through siege, not field battle" (PW:80) — is absent; holds
  top-down and laterally (the besieged seat's surrender has nothing to answer). `supply`: cut → a force
  away from home lives only by forage and has no supply line (PW:37-38); holds bottom-up and vertically.
  `forage`: narrowed, above. `encamp`: cut → a force outside walls has no defended place and no winter
  quarters; holds bottom-up only once M-1 exists — **narrowed**: "a force away from walls may make a
  defended stand".
- **R.** R-CHOICE: storm (blood now) against besiege (time, food) is the besieger's defining choice
  (p8:563); forage (harm, ill will) against supply (cost, a line) is the occupier's. R-WORLD: a long
  siege starves a town and turns its people, unwatched.
- **S.** Methodology: every store move is `_shift`; every reader of walls is `fortification_of`.
  Pauses: none in the season; the field remains one call. Down-scale: the field's result writes stocks
  and Sites (TS2 §4.6), so a siege and a storm propagate into the settlement's larder and walls.
- **E (last).** One shipped row plus three new rows host eight named acts (storm, besiege, supply,
  provision, equip, forage, sack, encamp) on four floor acts (march, camp, forage, supply) and two
  floor postures (siege, assault). Every new row waits on one mechanic (M-1) rather than adding three.

**Precedent.** §3.2 rows march, camp, forage, supply, besiege, assault; PW:34-43 §1.3a; PFF10:392-396.

**Gaps.** Closes MB-G16, G17, G18, G19, G20, G21, G22, G56. Leaves PARKED MB-G34, G35, G44.

**PARKED here.** `reconnoitre` — trigger: K-MB-12's reader of the seat's own military claims on the
`march` chooser (MBL:748) **and** M-1 (a force with scouts away from walls). Until then FI's `surveil`
by a person present supplies the claims (that act is FI's, not a fold). `ambush` (the field half) —
trigger: M-1 and PC's `conceal` (the person half is PC's, p8:398, p8:555).

**Disposition.** `march` REBUILD · `storm`, `besiege` FOLD (postures) · `supply` NEW ROW (`provision`,
`equip` FOLD) · `forage` NEW ROW (`sack` FOLD) · `encamp` NEW ROW (waits M-1, M-12) · `reconnoitre`
PARK · `ambush` (MB half) PARK. **Falsifiers.** `besiege`: a besieged town whose larder and garrison
are unchanged after a season. `supply`: a supplied and an unsupplied force away from home that starve
alike. `forage`: a run in which no force ever carries food it took. `encamp`: an encamped and an
unencamped force attacked at the same place with the same band distribution.

### Suite 4 — The place given up or destroyed (host `surrender`)

**Members.** `surrender` (host, season act); `raze` (sibling, PLANNED). Adjacent and owned elsewhere:
`seize` (VT:898, FA/GV), the bargaining of terms (SC), and raising walls (`fortify`, GV/EC).

| act | A | B | C | result |
|---|---|---|---|---|
| `surrender` into `give` + `covenant` (v2 V086) | Y (the holder) | **N** — beyond the hold, it writes the defending stocks, ends the siege state and bars `sack`; and it is two verbs composed | N | rejected (the lane brief rule 5); own row composed on the **primitive**, `give`'s and `seize`'s Tenure pair, not on the verbs |
| parley (MB-G33) into `surrender` | **N** — two parties bargain | **N** — SC's `negotiation` arrangement (p8:496) | — | not MB's; its result is `surrender`'s terms |
| `raze` into `surrender` | **N** (the occupier or holder) | **N** — it ends a place | — | sibling row |
| `fortify` into MB | **N** — the settlement's builder | **N** — a Site's `condition` rises: `restore`'s arm (IN-35); new walls are `build` | — | out of MB; GV/EC content (§3.8). L-06: not `work` |

**World effect.**
- `surrender`: the holder of a settlement under siege or occupation (or his seat's officer present)
  yields it. The Rung's `hold` passes to the besieging faction's seat in one effect (`seize`'s
  `Tenure.until`/`since` pair, VT:912-913); the defending stocks at the place stand down into its pool;
  the terms content (offered under `besiege`) may spare the garrison's persons from `detain` and bars
  `sack`. Emits `place.surrendered`, a **cession under arms**, neither `rung.seized` nor `record.given`
  (VT:915's reason for a distinct kind: a reader asking whether title moved by consent must not misread
  it). PW:102: a town that surrenders is easier to govern than one taken — the residents' stance row
  toward the new holder is milder than after `storm` [OPEN — tuning].
- `raze`: ends a Site, or a Rung, the actor holds or occupies (VCD §9.2, IN-12 step 11). No carrier
  ends a place today (H-166; M-9); the fate of persons inside is unruled (VCD:1812, "[GAP: persons contained in a razed Rung are left placeless").

**NERS.**
- **N.** Cut `surrender` → a siege ends only by storm or starvation, though "most sieges ended in
  negotiated surrender" (PW:102); the loser's War → Peace edge has no act (p8:562). Holds laterally
  (besieger ↔ besieged), top-down (a ruler cedes a town to save the rest) and diagonally (MB → FA:
  cession). False N-line check: `give` moves a hold by consent but writes no stocks and bars no sack;
  `seize` takes, it is not given. Disqualifier 1 does not fire. Cut `raze` → `found` and `build` have
  no inverse (p3:254); holds bottom-up.
- **R.** R-CHOICE for the defender: hold (hunger, the risk of sack) or yield on terms. R-WORLD: a town
  that yields on terms and one taken by storm diverge for decades in their stance.
- **S.** Methodology: the title move is one primitive used by `give`, `seize` and `surrender`. Pause:
  none.
- **E (last).** One new row (`surrender`) on one floor act; `raze` was already planned.

**Precedent.** PW:100-102 §2.3; PW:82 (Osaka, won by negotiation); FASE:134-140 T6; Total War: a
starving garrison, and the post-capture occupy / sack / raze choice `[MEMORY]`.

**Gaps.** Closes MB-G32, G33 (with SC), G41 (once M-9). MB-G50 (show of force) is closed emergently
by `muster`'s witnessed `army.mustered` or a `besiege`, and the defender's `surrender`.

**Disposition.** `surrender` NEW ROW · `raze` PLANNED (stands as v2 has it, p3:254) · `fortify` CULLED
from MB. **Falsifiers.** `surrender`: a surrendered and a stormed town that leave identical holds,
stocks, stances and sack licence. `raze`: a razed Site still read by `fortification_of`. `fortify`'s cull:
a garrison whose `condition` can rise only through an MB act.

---

## 3.4 Lexicon table

Chains: English ← intermediate(s) ← Latin lemma with principal parts and attested sense ← PIE. Wikt =
en/la.wiktionary through the lane tool; L&S = Lewis & Short through the tool. A link the tool did not
show is `[UNVERIFIED]`. Fit is by ordinary current usage (ED-IN-0179), not by the root.

| verb | suite | status | mechanic and world effect (carrier) | etymology chain (sources) | fit | rename |
|---|---|---|---|---|---|---|
| `levy` | 1 | NEW (designed TS1 §3.1) | settlement act, `remit:dispatch`; `Rung.stores` `recruits`→`troops_raw`, plus the cohort's `stance` toward the seat's faction; `levy.raised` | levy ← AN *leve* ← OF *levee* ← OF *lever* ← L **levō, levāre, levāvī, levātum** (1) "to lift up, raise, elevate" (L&S *lĕvo*; Wikt adds "make light, lighten") ← *levis* "light, not heavy" ← PIE \*h₁lengʷʰ- (Wikt). Wikt gives no ME stage (AN *leve* directly). Raising men is a long English sense: Wikt en verb senses 3–4, "To draft someone into military service"; "said of troops, to form into an army by enrollment, conscription" | FITS — "levy troops" is ordinary; Jordan's word (TS1:22); old `levy.*` citations name the store act (L-03) | — |
| `recruit` | 1 | NEW | settlement act; `recruits`→`troops_raw` and the seat treasury's `coin` debited; no stance row; `recruit.made` | recruit ← F *recruter* (Wikt) ← F *recrue* "new growth; levy" ← OF *recreü*, pp. of OF *recreistre* (= OF *re-* + *creistre*) (Wikt fr) ← L **crēscō, crēscere, crēvī, crētum** "to grow, increase" (L&S; Wikt la) ← PIE \*ḱreh₁-sḱéti, from the root \*ḱer- "grow" (Wikt la) | FITS — "recruit soldiers"; collides with FA's person act (§3.8) | — (or FA renames) |
| `muster` | 1 | NEW | settlement act; troop kinds `from` → `subject` via `_shift`; `army.mustered`, witnessed | muster ← ME *musteren* ← AN *mostrer*, MF *monstrer/moustrer* ← L **mōnstrō, mōnstrāre, mōnstrāvī, mōnstrātum** (1) "to show, point out, indicate" (L&S) ← *mōnstrum* ← *moneō* "warn, remind" ← PIE \*men- "think" (Wikt, causative). Latin "show" → English "assemble (for review)"; date `[UNVERIFIED]` | FITS — "muster troops" = assemble them | — |
| `garrison` | 1 | FOLDED (`muster`) | `muster` whose destination is the place the men will defend | garrison ← ME *garisoun* ← OF *garison/guarison* ← *guarir* "defend" (OF "protect, save"), of Germanic origin ← Frankish \*warjan ← PWGmc \*warjan "to ward off" (Wikt fro *guarir*) ← PIE \*wer- "cover" (Wikt root). Not through Latin | FITS | — |
| `drill` | 1 | NEW | settlement act; `troops_<g>`→`troops_<g+1>`; `troops.drilled` | drill ← MDu *drillen* (Wikt). Germanic; no Latin path; the source gives no PIE root | FITS — "drill the levies" | — |
| `disband` | 1 | NEW | settlement act; `troops_<g>`→`recruits`, capped; `army.disbanded` | disband (1590s) ← MF *desbander* ← *des-* (L *dis-* "apart") + MF *bande* (which *bande* Wikt does not state) ← Germanic ← PIE \*bʰendʰ- "bind" (Wikt *disband*, *band*). Latin prefix, Germanic stem | FITS | — |
| `marshal` | 2 | NEW | settlement act; writes the `order_of_battle` Record read by `order_of_battle()` at every field; `army.marshalled` | marshal ← ME *marschal* ← AN *mareschal* ← ML *mariscalcus* ← Frankish \*marhaskalk (or OHG *marah-scalc*) ← PWGmc \*marh "horse" + \*skalk "servant" (Wikt). Germanic; Latin only as a medieval carrier. The verb "arrange (troops) in order" comes from the officer's duty; date `[UNVERIFIED]` | FITS — "marshal one's forces"; the Royal Marshal (`offices.yaml:274`) is the same sense | — |
| `rally` | 2 | FOLDED (in-battle) | `rally_check` filled: a fraction of lost morale on a Command pool, within the officer's span | rally ← MF *rallier* ← OF *ralier* ← *re-* + L *ad* + L **ligō, ligāre** (1) "to tie, bind" (Wikt; L&S *alligo* "to bind to something") ← PIE \*leyǵ- "to bind" (Wikt la *ligō*, Etymology 2; the "uncertain" note belongs to the noun *ligō* "hoe") | FITS — "rally the line" | — |
| `pursue` | 2 | FOLDED (in-battle) | pursue/hold order: `pursuit_damage`, `recall_check` | pursue ← ME *pursuen* ← AN *pursuer*, OF *poursuire* ← L **prōsequor, prōsequī, prōsecūtus sum** (3, dep.) "to follow … to follow after, pursue" (L&S), influenced by *persequor* (Wikt) ← *sequor* ← PIE \*sekʷ- "follow" (Wikt) | FITS | — |
| `retreat` | 2 | FOLDED (in-battle) | a withdrawal threshold and the `retreat` stance; feigned flag | retreat ← ME *retret* ← OF *retrait/retret* ← L *retractus*, pp. of **retrahō, retrahere, retrāxī, retractum** (3) "to draw back, withdraw; to call back" (L&S) ← *trahō* "drag, pull"; PIE disputed (Wikt: "Unclear", \*dʰregʰ- uncertain) | FITS — armies retreat; persons withdraw (PC) | — |
| `withstand` | 2 | FOLDED (in-battle) | `hold`/brace on chosen subunits | withstand ← ME *withstanden* ← OE *wiþstandan* ← PWGmc \*wiþistandan, *with-* "against" + *stand* (Wikt). Germanic; no Latin; *stand* ← PGmc \*standaną ← PIE \*steh₂- (Wikt) | FITS, slightly literary | — |
| `command` | 2 | CULLED (as a verb) | none of its own: the stat is an input (`derive_command`); the choices are `marshal`'s | command ← ME *commanden* ← OF *comander* ← LL *commandō* ← L **commendō, commendāre, commendāvī, commendātum** (1) "to commit to one for preservation … to intrust" (L&S) ← *com-* + *mandō* "order, command; hand over" ← *manus* "hand" (PIE disputed, Wikt) | STRAINED — the canonical mass-combat stat is **Command** (`synonym_registry.yaml:29-31`) | none; V-10's `tactic` is a noun |
| `march` | 3 | SHIPPED (REBUILD) | VT:683-711; adds posture, carries the force (M-1), reads the order, writes stocks and garrison | march ← ME *marchen* ← MF *marcher* ← OF *marchier* ← Frankish \*markōn ← PGmc \*markōną, akin to *mark* (Wikt). Not Latin. Wikt shows no PIE form for the verb | FITS | — |
| `storm` | 3 | FOLDED (posture, default) | the field at arrival; walls graded | storm (verb, "take by assault", from the noun) ← ME *storm* ← OE *storm* ← PWGmc \*sturm ← PGmc \*sturmaz ← PIE \*(s)twerH- (Wikt). Germanic | FITS — "take a town by storm" | replaces v2's `assault` |
| `besiege` | 3 | FOLDED (posture) | arrive before the place without a field; the siege state and its per-season reader (M-6) | besiege ← ME *besegen*, *be-* "around" + *sege* ← OF *sege* ← VL \*sēdicum ← L *sēdēs* "seat" (Wikt *siege*: the military sense is "an army 'sitting down' in front of its target"); cf. **sedeō, sedēre, sēdī, sessum** (2) "to sit … to keep the field, remain encamped" (Wikt) ← PIE \*sed- (Wikt) | FITS | replaces v2's `invest` |
| `invest` | — | CULLED (name) | — | invest ← MF *investir* / ML *investīre* ← L **investiō, investīre** (4) "to clothe in, to cover" ← *vestiō* ← *vestis* ← PIE \*wes- (Wikt). The money sense came via It. *investire* (Wikt) | MISFIT — the siege sense is technical; a reader lands on money (V-11) | `besiege` |
| `assault` | — | CULLED (name) | — | assault ← ME *assaut* ← OF *assaut* ← *assalir* ← LL **assaliō** (4) "to jump on, attack" (*ad* + *saliō*; classical *assiliō*) (Wikt), through *saliō* ← PIE \*sel- (Wikt root template) | STRAINED — general and personal (legal) sense; PC's ground | `storm` |
| `supply` | 3 | NEW | stores from a settlement in purview into the force's stores (M-1); `force.supplied` | supply ← ME *supplien* ← OF *soupleer/souploier* ← L **suppleō, supplēre, supplēvī, supplētum** (2) "to fill up, make full or whole, to make good, to complete, supply"; "in milit. lang. … to fill up … furnish with a complement, recruit" (L&S, Liv. 29.24.14) ← *sub-* + *pleō* "fill" ← PIE \*pleh₁- (Wikt) | FITS — "supply the army" | — |
| `provision` | 3 | FOLDED (`supply`, food) | `supply` with a food kind | provision ← ME *provisioun* ← OF *provision* ← L *prōvīsiō* ← **prōvideō, prōvidēre, prōvīdī, prōvīsum** (2) "to see forwards … to act with foresight … to provide, see to" (L&S; Wikt) ← *videō* ← PIE \*weyd- "see" (Wikt). The English verb is formed from the noun `[UNVERIFIED]` | FITS — "provision a garrison" | — |
| `equip` | 3 | FOLDED (`supply`, arms) | `supply` with an arms kind; read by `kind_for_kit` | equip ← F *équiper* ← OF *esquiper* "fit out (a ship)", of Germanic origin, most probably ← ON *skipa* ← PGmc \*skipōną (Wikt, akin to *ship*). Not through Latin | FITS | — |
| `forage` | 3 | NEW | stores from the occupied rung into the force's stores; `stores.foraged` | forage ← ME *forage* ← OF *fourage/forage* ← *fuerre* "fodder" ← Frankish \*fōdar ← PGmc \*fōdrą ← PIE \*peh₂- (Wikt). Not Latin | FITS | — |
| `sack` | 3 | FOLDED (`forage`) | every kind from a place taken by `storm`; `town.sacked` | sack "plunder" ← MF *sac*, from *mettre à sac* "put in the bag", a command to pillage; parallel It. *sacco* ← ML *saccō* ← VL *saccāre* ← L **saccus** "a sack, bag" ← Gk *sákkos* ← Semitic (Wikt). No PIE root (a loan) | FITS | — |
| `encamp` | 3 | NEW (waits M-1, M-12) | a `camp` Site read by `fortification_of`; the force halts | encamp ← *en-* + *camp* ← ME *kampe* ← OE *camp* ← PWGmc \*kamp (an early loan from L *campus*), reinforced c. 1520 by MF/ONF *camp* ← L **campus** "open flat level ground: a plain, a natural field" ← PIE \*kh₂em- (Wikt: traditional, uncertain) | FITS | — |
| `reconnoitre` | 3 | PARKED | military claims about a target from range | reconnoitre ← F *reconnoître* (obs. spelling of *reconnaître*) ← L **recognōscō, recognōscere, recognōvī, recognitum** (3) "to know again, recognize; to look over, review, investigate, examine, inspect" (Wikt) ← *re-* + *cognōscō* ← *gnōscō* (= *nōscō*) ← PIE \*ǵneh₃- (the adjective \*ǵn̥h₃tós) (Wikt la *nōscō*) | FITS (Canadian spelling) | — |
| `ambush` | 3 | PARKED (MB half) | a hidden force sets the first mover | ambush ← ME *enbuschen* ← OF *enbuscier* ← *en-* + VL *boscus* "wood" ← Frankish \*busk ← PGmc \*buskaz (Wikt). Germanic stem via Vulgar Latin | FITS | — |
| `surrender` | 4 | NEW | the hold passes (`seize`'s Tenure pair); stocks stand down; `sack` barred; `place.surrendered` | surrender ← ME *surrendren* ← OF *surrendre* ← *sur-* (L *super*) + *rendre* ← LL *rendō* (Wikt en *render*; the VL \*rendere is not attested there) ← L **reddō, reddere, reddidī, redditum** (3) "to give back, return, restore … to give up, hand over, deliver" (L&S; Wikt) ← *re-* + *dō* ← PIE \*deh₃- "give" (Wikt). Wikt lists "to yield (a town, a fortification) to an enemy" | FITS | — |
| `raze` | 4 | PLANNED (IN-12 step 11) | ends a Site or Rung (M-9) | raze ← ME *rasen* ← AN/OF *raser* ← VL \*rasāre ← L *rāsus*, pp. of **rādō, rādere, rāsī, rāsum** (3) "to scrape, scratch, shave" (L&S) ← Proto-Italic \*razdō; no secure PIE root (Wikt) | FITS — "raze the walls" | — |
| `fortify` | — | CULLED (from MB) | GV/EC: `restore` of a garrison Site; `build` for new walls | fortify ← LME *fortifien* ← OF *fortifier* ← LL **fortificō** "to strengthen, fortify" ← *fortis* "strong" (PIE \*bʰerǵʰ- or \*dʰerǵʰ-, disputed) + *-ficō* (Wikt) | FITS | lives in GV/EC |

---

## 3.5 Deduplication and culls

**Near-synonym groups and what was done.**

| group | ordinary-English overlap | what was done, and the discriminator |
|---|---|---|
| levy · recruit · raise · muster | all "get soldiers" | `levy` = raise by obligation (cost: consent); `recruit` = raise for coin (cost: coin); `muster` = bring raised men together. "Raise" is not a row: it is the genus |
| muster · marshal | "marshal one's forces" can mean assemble | kept apart by object and write: `muster` moves stocks between places; `marshal` writes an order and moves nothing. The discriminator is stated in each row's `scale_note` when built |
| storm · assault · attack | one act on a place | `storm` kept (specific to a place); `assault` culled as a name (PC's personal sense); "attack" is the genus |
| besiege · invest · siege | one act | `besiege` kept; `invest` culled (V-11); "siege" names the state M-6 carries |
| retreat · withdraw · disengage | leaving a fight | `retreat` = the mass choice; `withdraw` stays PC's IN-46 (MB-G31's collision removed by naming); `disengage` was folded into PC's `withdraw` by v2 (p8:396) |
| supply · provision · equip | "supply X with Y" | one act, content by kind: host `supply`, `provision` (food) and `equip` (arms) folded |
| forage · sack · plunder · raid · requisition | taking stores | `forage` hosts `sack`; `requisition` stays the seat's lawful store act (GV/EC); "plunder"/"raid" not adopted (no second act behind them) |
| command · marshal · order | directing the army | `command` culled as a verb (the stat); `marshal` carries the orders; FA's `dispatch` (the remit) stays FA's |
| drill · train | practice | `drill` = a stock's grade (MB); `train` = a person's capability (another lane); v2's merge (p8:418) rejected by the fold test |
| withstand · endure · hold · guard · brace | resisting | `withstand` is the in-battle choice; `hold` and `brace` are the module's names for its two mechanisms; WT's `endure` folds in for the battle sense (v2 V168, p8:522); `guard` is PC/GV's |
| surrender · yield · give · cede | handing over | `surrender` = a place under arms (MB); `yield` = a duel's end (PC, V104); `give` = consent (FA/GV); "cede" is the treaty sense (FA's `covenant`) |
| fortify · restore · build · work | raising walls | out of MB: `restore` (condition) or `build` (new Site); not `work` (L-06: two senses in one row) |
| encamp · camp | one act | `encamp` (the verb; "camp" is also the noun the Site kind takes) |
| reconnoitre · surveil · scout | looking at a target | `reconnoitre` parked as MB's; not folded into FI's `surveil` |

**Culls, each with its fold test and floor check.**
- **`command` (as a verb).** Fold test into `marshal`: A Y, B Y, C Y for the choice half; the stat half
  is an input, not an act. Floor: "arrange the army" lives in `marshal`. Nothing a floor act needs dies.
- **`invest`, `assault` (as names).** Names only; the acts survive as `besiege` and `storm`.
- **`fortify` (from MB).** Not culled from the game: moved to GV/EC (`restore`/`build` content on a
  garrison Site). MB keeps the wear, which `march` writes (TS2:214-216). Floor: "siege" is MB's; raising
  walls is settlement building, GV's floor.
- **`tactic`** (V-10's proposal): not adopted, a noun naming no act.
- **`provision` as its own row (v2 V111):** folded into `supply`.
- **`besiege` as its own row (v2 MB call 2):** folded as a posture.

**Critics' findings that concern MB.**

| finding | verdict | how |
|---|---|---|
| **V-10** (`command` is a stat; name the choice `tactic`) | **applied, differently** | `command` culled as a verb; the choice is `marshal`'s content, not a `tactic` row (a noun) |
| **V-11** (`invest` reads as money) | **applied** | posture names `besiege` and `storm` |
| **V-15** (`tax` needs the retired `evade / defy`) | **answered for MB** | `levy` carries its own cost carrier (a stance row) and needs no `comply`/`evade` reply; draft evasion is PARKED until FA rebuilds `evade / defy` (FA-G23) |
| **V-02** (`withstand` and `endure` classed inconsistently) | **answered** | `endure` (battle sense) is a named content of `withstand`, folded |
| **V-06** (`hire`/`recruit` asymmetry; the recruiter has no act) | **applied** | MB's `recruit` is in the recruiter's voice and writes its own effect |
| **V-19** (`guard`/`ward` doublets) | **noted** | neither is an MB row |
| **L-03** (`levy` reused; old citations change meaning) | **applied** | `levy` names the troop act; TS-L's re-key of `requirements.yaml` and `hole_register.yaml` (TS1:728-738) must land before the row |
| **L-05** (`dispatch` misfits) | **answered for MB** | MB rows use `remit:dispatch` as the military remit; "dispatch troops" fits that use. The verb row is FA's (FA-G12) |
| **L-06** (`work` holds two senses) | **applied** | fortify goes to `restore`, not `work` (MB-G24) |
| **L-01** (root sense used as design intent) | **applied** | every design claim here stands on reads/writes/emits and ordinary usage; e.g. `besiege` is kept for its effect, not for *sedeō* |
| **L-12** (`seize`, `requisition` unjudged) | **partly** | MB judges only where it leans on them: `requisition` and `transfer` should stop moving men (Suite 1) |

---

## 3.6 Gap coverage table

One disposition per row. "Closed by X once M-n" means the verb is assessed and the mechanic is §3.7's.

| gap id | closed by | PARKED (trigger) | OUT OF SCOPE (why) | STALE (cite tree) | DISPUTED (why) |
|---|---|---|---|---|---|
| MB-G01 | `levy` once M-2 (the stock at `men_per_weight`) | | | | |
| MB-G02 | `levy` once M-2 | | | | |
| MB-G03 | | | | renamed: VT:646 `requisition`; `levy` now names raising troops | |
| MB-G04 | `marshal` once M-3 (and TS-1/TS-5 move `build_army`) | | | | |
| MB-G05 | `marshal` once M-3 | | | | |
| MB-G06 | `marshal` (who leads) once M-10 (Command from a seated person) | | | | |
| MB-G07 | `drill` once M-2's grade roster (battle experience: J-5 (c), Jordan's) | | | | |
| MB-G08 | `drill` (not `train`) once M-2 | | | | |
| MB-G09 | | K-MB-10 ruled (the mass → personal yield; Jordan's) | | | |
| MB-G10 | `marshal` (in-battle choices) and `march` postures | | | | |
| MB-G11 | `marshal` (the reserve and its release) once M-4 | | | | |
| MB-G12 | `levy` (R-POOL's pool, not cohort weight) once M-2 | | | | |
| MB-G13 | `muster` (new row; TS1:803's Query reading superseded) | | | | |
| MB-G14 | `muster` (`garrison` content) once a threat question source exists | | | | |
| MB-G15 | `march` (target ranking reads `at_war`) once FA's `declare` produces it; gating is §3.9 item 1 | | | | |
| MB-G16 | `forage` and `besiege` once M-6 (H-212's reader) | | | | |
| MB-G17 | `march` posture `besiege` once M-6 | | | | |
| MB-G18 | `march` posture `storm` once graded walls and wear (H-150; TS2 §4.6) | | | | |
| MB-G19 | `forage` (`sack` content) once M-1 | | | | |
| MB-G20 | `forage` once M-1 | | | | |
| MB-G21 | `supply` (`provision`) once M-1 | | | | |
| MB-G22 | `encamp` once M-1, M-12 | | | | |
| MB-G23 | `march` (garrison wear, TS2:214-216) with GV/EC `restore` raising it | | | | |
| MB-G24 | | | `work` is an EC/GV row; MB routes fortify to `restore` (L-06) | | |
| MB-G25 | `levy`/`muster` (stocks and garrison men defend, TS2 §4.1) and `marshal` (`withstand`) | | | | |
| MB-G26 | `marshal` (`withstand` content; the defender's chooser) | | | | |
| MB-G27 | `marshal` (`rally`) once M-4 | | | | |
| MB-G28 | `marshal` (`rally`): **fill**, per K-MB-11's own condition (§3.3 Suite 2) | | | | |
| MB-G29 | `marshal` (`pursue`) once M-4 (season path reaches `pursuit_damage`) | | | | |
| MB-G30 | `marshal` (`retreat`) once M-5 | | | | |
| MB-G31 | naming: `retreat` (MB) vs `withdraw` (PC) | | | | |
| MB-G32 | `surrender` (new row) | | | | |
| MB-G33 | `surrender` (terms) with SC's `negotiation` | | | | |
| MB-G34 | | K-MB-12's reader on the `march` chooser and M-1 | | | |
| MB-G35 | | M-1 (a field away from walls) and season terrain rows readable | | | |
| MB-G36 | | K-MB-9 / J-C-19 (death policy, Jordan's) | | | |
| MB-G37 | | | grading the field on one margin is K-MB-8, a Jordan item on the module, not a verb | | |
| MB-G38 | | | the mutual-rout tie-break is a grading rule of the module | | |
| MB-G39 | | | corpus question sources (H-175), not a verb; the computed `levy` (TS-7) is what gives authored generals an army | | |
| MB-G40 | | | | arrival and `seize` built: VT:698-707, VT:898; `raze` continues as MB-G41 | |
| MB-G41 | `raze` once M-9 (H-166) | | | | |
| MB-G42 | | | `forgive` is a person's act (NP/SC); MB only appends the grudge | | |
| MB-G43 | | J-5 ruled (TS2:717) | | | |
| MB-G44 | | M-1 and PC's `conceal` | | | |
| MB-G45 | `marshal` (role/stance content: the module's charge and shock rows) | | | | |
| MB-G46 | `supply` (`equip`) and `marshal` once arms and mount kinds exist (M-11) | | | | |
| MB-G47 | `marshal` (`retreat`, feigned) | | | | |
| MB-G48 | `marshal` (the order Record carries orders to the field) | | | | |
| MB-G49 | | J-C-31 (played fidelity); the lexicon is unchanged by it | | | |
| MB-G50 | `muster` (witnessed) or `besiege`, answered by `surrender` — an emergent path, no row | | | | |
| MB-G51 | `disband` | | | | |
| MB-G52 | `supply` (`equip`) once M-11 | | | | |
| MB-G53 | `levy` (the cohort `stance` row) once M-8 | | | | |
| MB-G54 | | | the pool keyed by settlement kind is SE data (TS1 lane split) | | |
| MB-G55 | `marshal` (`rally` as a fraction; `command` a stat) | | | | |
| MB-G56 | `supply` and the one larder draw (TS2:299-301 resolves X-19) | | | | |
| MB-G57 | | | `threadwork_check` is TW's hook (K-MB-11 deletes it until TW gives it a reader) | | |

Count: 57 rows; closed 41, PARKED 7, OUT OF SCOPE 7, STALE 2, DISPUTED 0.

---

## 3.7 Mechanics this subsystem needs (named gaps)

| id | mechanic | what it must write | verbs that wait on it |
|---|---|---|---|
| **M-1** | **the field force**: the stocks a march fields travel with its marchers on `Won`/`Unopposed`, keep the allegiance of the faction that raised them (not the rung's holder, TS2:19-21), and hold their own stores | stocks (and kit, food) moved with the arrival; a force-owned store the larder draw reads | `march` (an arrival with men), `besiege`, `forage`/`sack`, `supply`/`provision`/`equip`, `encamp`, `ambush`, `reconnoitre`, a force's `surrender` |
| **M-2** | the recruit pool and the troop stock with grades (TS1 §2.1-2.8; TS-3, TS-4, TS-7) | `recruits` and `troops_<grade>` matter kinds; regrowth at MATTER; `fielded` | `levy`, `recruit`, `muster`, `drill`, `disband`, `march` |
| **M-3** | the `order_of_battle` Record kind, read by `order_of_battle()` (TS2 §4.2) in place of `march`'s `order` payload (TS2 §4.3) | one Record per force; the spec list `build_army` takes | `marshal` and its seven contents |
| **M-4** | the module's choices wired: `rally_check` filled (fraction of lost morale, Command pool, Ob 2, within span); the reserve's release read from the order (replacing `RESERVE_COMMIT_TURN`); the season path reaching `pursuit_damage`/`recall_check` (multi-subunit run, TS-5) | morale restored per subunit; the commit turn; pursuit casualties | `rally`, `pursue`, the reserve |
| **M-5** | `field_degree` telling a withdrawn army from a routed one (R-7 is `[ASSUMPTION; Jordan to correct]`, VT:701) | a band or margin `march` writes on | `retreat` (season half) |
| **M-6** | the siege state and its readers: H-212's occupant draw; no outside supply into a besieged place; garrison wear per season; a witnessed per-season event | larder draws, `Site.condition`, an Event per season | `besiege`, `storm` (from a siege), `forage`, `surrender` |
| **M-7** | a death carrier for a lost field (K-MB-9; H-152) | `person.died` on the losing side | `pursue` (deaths by name), `sack` (harm, with H-49) |
| **M-8** | the costs of raising: the cohort `stance` row on `levy`; the coin debit on `recruit`. PARKED extensions: a levy's service term and a paid stock's upkeep (§3.9 item 2) | `Person.stance` (cohort); the treasury's `coin` | `levy`, `recruit`, `disband` |
| **M-9** | an end for a Site or a Rung (H-166) | a closing write the readers honour | `raze` |
| **M-10** | Command from a seated person (`derive_command` on charisma/cognition; R-C-1, K-MB-2) | the commander's Command into the order | `marshal` (who leads), `rally`, `pursue` (recall) |
| **M-11** | arms (and mount) matter kinds and a producer (TS1:610-613; `site_yield` has no arms row, TS2:722-723) | arms stores | `supply` (`equip`); cavalry for J-19 |
| **M-12** | a `camp` Site kind that `fortification_of` reads | a Site minted where the force halts | `encamp` |

---

## 3.8 Cross-subsystem flags

- **FA — `recruit` collides.** FA's register row FA-G47 wants `recruit` for enlisting a person
  (a retinue, an intelligencer). MB's `recruit` takes men from a pool for coin. One name, two acts with
  different objects and writes; the typed grammar has no disjunction (VT:911's note on `seize`). One
  of the two must take another word: MB proposes FA's person act be `retain` or `enlist`; if FA keeps
  `recruit`, MB's act needs a plain alternative ("hire" is NP/EC's, V-06). For the reconciliation (Part III §III.5).
- **FA — war and the march.** MB-G15: `march` reads `at_war` (FA's `declare`, FA-G01) at least in its
  ranking; whether war *gates* a march is §3.9 item 1. FA-G07: an ally's force joining a side
  (`sides_of`) reads FA's `covenant`.
- **FA — `seize`** (VT:898) is FA/GV's row; MB's occupation licenses it. **`dispatch`** (FA-G12–G14)
  is FA's verb row; MB rows use `remit:dispatch` as the military remit (VT:687; TS1:702).
- **FA — `muster` is read by** FA-G35 (sabotage to deny a muster) and FA-G50 (GD-2's mandatory pass);
  FA-G42 / MB-G50 (show of force) is the emergent `muster`/`besiege` → `surrender` path.
- **FA/SC — `surrender`'s terms** are bargained in SC's `negotiation` arrangement (V153, p8:496); FA's
  `covenant` carries any treaty that outlives the place.
- **GV/EC — `fortify`** moves to `restore` (a garrison Site's `condition`) and `build` (new walls), not
  `work` (L-06). **`requisition` and `transfer`** should stop moving troop kinds (TS1:791-793); men move
  by `muster` and `march`. The **arms producer** (M-11) is EC's. **`raze`** overlaps any GV demolition
  act; one row should own the end of a Site.
- **GV — the levy's cost** writes a cohort `stance` row: GV's unrest and the revolt floor (PMM:446-452
  M-4, PARKED) read it.
- **PC.** `withdraw` (IN-46) stays PC's; the mass choice is `retreat`. `ambush`'s person half and
  `conceal` are PC's (p8:398). `yield` (V104) is the duel's end, not `surrender`. The rallying officer's
  exposure is the mass → personal yield (K-MB-10). `rush` at the field is a `marshal` content (the
  module's charge), not PC's `fight`.
- **NP / attributes lane.** `train` (a person) is not `drill` (a stock). Command from a seated person
  (M-10) waits on `Person.attributes` (K-2). `forgive` closes the grudge `march` appends (MB-G42).
- **WT.** `endure`'s battle sense folds into `withstand`; `encamp` was tagged WT in AFS:301 — the camp
  is the force's (MB), shelter on a journey is WT's.
- **TW.** `threadwork_check` (MB-G57) is TW's to fill or delete.
- **FI.** `reconnoitre` is parked as MB's, not folded into `surveil` (VT:1186); FI's `surveil` is the
  interim path.
- **SE.** The pool's data (ceiling, regrowth, settlement kind: MB-G54) is SE's.

---

## 3.9 For Jordan

Ladder tried on each: superseded · irrelevant · design document · precedent · architecture.

1. **Does a march between factions require war?** (MB-G15; K-MB-5, MBL:724.) Not superseded; not
   irrelevant; no document rules it (`faction_q.py:219`'s docstring leaves it open, MBL:440 M-MB-7);
   precedent splits — CK3 requires a declared war to attack, Total War lets an attack itself start one
   `[MEMORY]`; architecture is neutral (MBL:724 dropped "a field makes war" as a second producer). Two
   games: war as a gate on violence, or war as a state that values and witnesses read. FA will raise
   the same item from its side.
2. **Service and pay.** Does a levied stock go home after a term, and does a recruited stock need
   upkeep (PW:53-64 §1.3b)? TS1:650-651 answers "no term" under A by step 5. Precedent splits: PW's
   term table vs CK3 levies, which `[MEMORY]` cost upkeep while raised and have no term. With term and
   upkeep, `levy` and `recruit` are different armies (temporary vs permanent); without, they differ only
   in the first cost. Default here: no term, no upkeep (M-8's base), the extensions PARKED.
3. **The field force (M-1) amends ratified Layer 1, so it rides J-1.** Floor acts (camp, forage,
   supply, siege) are answered by precedent at step 4: every named game keeps armies in the field. But
   a force that holds its own stores off a settlement deepens A's strains TS1:62-70 lists (the Rung as
   "the address, never the occupant"; units as persons at weight). That overwrites ratified canon, so
   it is Jordan's with J-1, not a lane decision. Default: M-1 as stated.
4. **`sack`'s tone.** FASE:219-222 FA-6 marks branch (c) Sack `needs_jordan` ("atrocity content … is a
   tone/taste ruling"). Precedent keeps it (Total War `[MEMORY]`); no design document rules it. It is
   kept here as a `forage` content and can be dropped without touching any other row.

Not escalated (answered): the Accord cost on `levy` (steps 4-5: JA2/RoTK VIII via PMM M-3, and without
it `levy` strictly dominates `recruit`; TS1 §2.10's step-5 objection does not reach a cohort stance
row, which TS1:683-685 itself calls lawful); `rally_check` fill vs delete (K-MB-11's own condition);
`command` as a verb (V-10, the canonical stat); posture names (V-11, ordinary usage); whether
`equip` binds kit to men (architecture: kit sits in the force's stores under M-1, `kind_for_kit`
unchanged).

---

## Limits

- **Opened:** the lane brief; the register (MB rows in full, FA rows skimmed); both critic reports; TS1 §0,
  §2.5-§3.5; TS2 §4.1-§5, §9; v2 p3:200-268, p8:170-206, p8:380-422, p8:541-567, p8:650-665, p7:242,
  p7:246; VT rows `dispatch`, `requisition`, `march`, `seize`, `transfer` (head); `massbattle.py:160-235`;
  `orchestration.py:280-345, 2546-2626` and line 2221; `config.py` grep lines; `seam/ladder.py:180-215`;
  `rosters.yaml:110-130, 1297-1308`; `hole_register.yaml` H-212; MBL 150-165, 430-452, 712-750; PW
  28-172; PMM 365-510; PFF10 38-60, 236-246, 441-516 and a grep; PFF09 37-41, 91-94; FASE 134-140,
  218-222; COMP1 320-346; AFS 262-312; NERS skill 1-165; the archived MB integration doc by grep only.
- **Not opened:** VCD (cited only through the register: VCD:1812); HCC; XSC; MBG; `cases/NPC5.yaml`
  (quoted through MBL:436); `faction_q.py` (through MBL:440); `world_q.py` beyond what TS quotes.
- **Not run:** no test, no `aperture`, no validator. No repo file was edited.
- **Sub-agents spawned: 0.** The MB rows, both critics and the troop-stock design fit one reader;
  a second producer would have read the same files to the same verdicts (CLAUDE.md §10). Independent
  attack belongs to the reconciliation (Part III §III.5)'s critic stage.

