# CR-12: melee attrition back to the locked linear law (design, measure-first)
## Status: PROPOSED. Builds nothing until Jordan approves. Lane MB; ED-MB-0045 (melee item); batch B10-12.

Reference, not mechanism (`CLAUDE.md` §0.05): the code named below is the mechanism; the instrument
`systems/mass_battle/sim/lanchester_signature.py` is the observer. Read at commit `aa6871b8` (MB-07r:
`MB_SUPPORT_RANK_CAP` default `'1'`, `POOL_QUALITY_SCALE` 0.8). Every reading below was taken under
Python 3.11.18 with `PYTHONHASHSEED=0` (CI's interpreter; the container default 3.13 differs).

## 1. The readings (step 1)

`python3 -m systems.mass_battle.sim.lanchester_signature` at `aa6871b8`, unmodified. The instrument
`setdefault`s `PER_CELL='0'`; the shipped default is `'1'` (`modules/mass_battle/config.py::PER_CELL`).
Both logs end with an `EXIT` line; exit 1 is the instrument's own verdict (`sys.exit(0 if run() else 1)`),
not a crash. The two arms ran in parallel, single-threaded each, on a 4-core container.

| check | arm 0 (`PER_CELL=0`, the instrument's default) | arm 1 (`PER_CELL=1`, shipped) |
|---|---|---|
| LINEAR (melee 4:1) | **FAIL** big_win=52.0% (band [74, 83]), cas_diff=+24.0 (≥20) | **FAIL** big_win=52.0%, cas_diff=+22.8 |
| SQUARE (volley 4:1) | PASS cas_exchange small/big=19.7 (≥4) [big 1.35%, small 26.55%] | PASS 6.6 [big 2.25%, small 14.90%] |
| NO-ANNIHILATION (mirror) | PASS max_cas=10.4% (≤60), loser_hp=89.6% | PASS max_cas=8.1%, loser_hp=91.9% |
| LAW EXPONENTS | **FAIL** melee p=1.50 (≤1.4) cv=0.00292 identifiable; volley p=2.10 (≥1.6) cv=0.00446 identifiable | **FAIL** melee p=1.70 cv=0.00191 identifiable; volley p=1.70 cv=0.00877 identifiable |
| no-rout pin (melee / volley) | OK 0/40 routed, fit window 28 / 31 ticks | OK 0/40 routed, fit window 28 / 31 ticks |
| verdict, wall | 2/4, `EXIT 1`, 68 s | 2/4, `EXIT 1`, 84 s |

**Control (env only, no code): the pre-MB-07r magnitudes** (`MB_SUPPORT_RANK_CAP=0 POOL_QUALITY_SCALE=0.5`,
same commit, same interpreter; MB-07r changed no other engine line):

| check | arm 0 | arm 1 |
|---|---|---|
| LINEAR | FAIL big_win=63.0%, cas_diff=+25.1 | FAIL big_win=52.0%, cas_diff=+23.1 |
| LAW EXPONENTS | FAIL melee p=1.90; volley p=2.05 | FAIL melee p=2.05; volley p=1.80 |
| SQUARE / NO-ANNIH. | PASS 19.7 / PASS 10.2% | PASS 6.6 / PASS 8.5% |

What the readings say:

- **The recorded 1.65 to 3.20 are stale, as the entry said.** Today melee p is 1.50 (arm 0) and 1.70
  (arm 1), both identifiable, neither routed. MB-07r's support cap moved it DOWN (1.90 → 1.50,
  2.05 → 1.70): cutting the support ranks a body counts into its pool cut the exponent. That is the
  first piece of evidence for §2's diagnosis.
- **The LINEAR 4:1 band fails on both arms, and MB-07r did not cause it**: the control fails too
  (63%, 52%). ED-MB-0045's 2026-10-08 row recorded 77.0% PASS; something between that row and
  `aa6871b8` moved it, and this design does not bisect it (out of scope; named in §6). The CI flip
  (§5) needs it back in band regardless, so the fix's exit reads it.
- **Volley passes on both arms**, but arm 1's 1.70 sits 0.10 above its 1.6 bar with cv 0.00877
  (the noisiest fit of the four). A melee fix must not be bought with the volley term; §5 reads it.

## 2. The term, located by symbol (step 2)

One melee pair, one tick, casualties to A (the B side is the mirror):

```
_pair_a = K_LINEAR * lin_b * max(0, DAMAGE_BY_DEGREE[b_deg](atom_b.eff_power) - atom_a.eff_dr) * _a_dmg_mult
```

- **The casualty term**: `modules/mass_battle/orchestration.py::resolve_engagements`, the
  `if LANCHESTER_ENABLED:` block (`_pair_a` / `_pair_b`). `K_LINEAR` is `config.py::K_LINEAR` (12).
- **`lin_*`**: `modules/mass_battle/core/attrition.py::_lanchester_strength(contact_cells, unit, front_width)`
  = engaged columns × `min(unit.hp / unit.ncells, CELL_CAP) / LANCHESTER_DENSITY_REF / LANCHESTER_STRENGTH_REF`.
  The density is the WHOLE BODY's average (`unit.hp / unit.ncells`), not the contact cells' own troops.
- **The degree**: same function, `a_deg = compute_degree(a_net, max(1, b_net))`, `b_deg = compute_degree(b_net, max(1, a_net))`
  (`modules/mass_battle/resolution.py::compute_degree`, the ruled margin ladder). The contest is
  OPPOSED: each side's net is graded against the OTHER side's net, and a negative margin is `Failure`,
  which `config.py::DAMAGE_BY_DEGREE` maps to 0 damage.
- **The pool behind each net**: `modules/mass_battle/core/exchange.py::subunit_combat_pool`, the
  `if POOL_QUALITY_MODEL:` branch: `raw = atom.eff_power * atom.eff_size * POOL_QUALITY_SCALE + pen + stam_pen`
  (then the yield malus and `_friction`). It is split onto the pair by
  `core/exchange.py::pair_pool_contribution` (`base_pool / atom.cur_troops * _pair_engaged_troops(...)`),
  called from `resolve_engagements` under `POOL_VARIANT == "C-ii"` (`config.py::POOL_VARIANT`). With
  `eff_size = cur_troops / BLOCK_SIZE`, the pair pool is `eff_power * POOL_QUALITY_SCALE * engaged / BLOCK_SIZE`:
  quality times the troops in contact plus the support ranks `config.support_weight` admits
  (`core/exchange.py::_pair_engaged_troops`; MB-07's cap).
- **The second pool site**: `modules/mass_battle/hierarchy/units.py::Unit.base_combat_pool`, the
  `if POOL_QUALITY_MODEL:` branch, `raw = self.power * self.effective_size * POOL_QUALITY_SCALE + pen + stam_pen`
  (at `aa6871b8` it sits at `:3012`, not the `:2961` the plan recorded). It is the unit-grain copy of
  the same base term; its callers are `orchestration.py`'s pursuit, rearguard and freed-attacker pools
  (`pursuit_damage`, `freed_attacker_damage`, and the `a_pool`/`b_pool` trace at the multi-unit
  battle), NOT the melee exchange, so it does not enter the instrument's reading. Its wrapper differs
  (no yield malus, no friction, the overextend penalty), so only the base term is one rule.

### Where troop numbers enter the melee term

Three channels, not two:

1. **`lin_*` (own numbers).** In the instrument's bodies the density is far below `CELL_CAP` (200):
   tier 3 Line is 400 troops over 25 cells (16.0 per cell, 5 columns, 5 ranks), tier 4 Line 800 over
   35 cells (22.9 per cell, 7 columns, 5 ranks). So `min(tpc, CELL_CAP)` never caps, and because the
   density is the body's average, every casualty anywhere in the body thins the contacting rank:
   `lin_X` is proportional to X's own total troops (at fixed columns). A kill rate proportional to
   own numbers is the SQUARE law's premise, not the linear law's.
2. **The pool (own numbers).** `engaged` counts contact plus capped support troops, so the pool,
   hence the expected net, rises with own numbers.
3. **The opposed degree (the enemy's numbers).** Because the degree is margin-against-the-enemy's-net
   and `Failure` deals nothing, B's damage to A depends on A's pool: the bigger body wins more rolls
   and the smaller body's hits go to 0. This is a cross-coupling the linear law does not have at all.

The instrument fits the exponent `p` that conserves `A^p − B^p` over a no-rout trajectory. With
`dA/dt = −f_B` and `dB/dt = −f_A`, the quantity is conserved exactly when `A^(p−1) f_B = B^(p−1) f_A`:
`p = 1` means each side inflicts the same casualties per tick whatever the two sizes (frontage-limited,
equal quality); `p = 2` means a kill rate proportional to own numbers. The bar `p ≤ 1.4` therefore
allows the bigger body's kill rate to exceed the smaller's by at most `(A/B)^0.4`. Channels 1 and 2
each push toward 2; channel 3 is not a power law and the fit absorbs it as a higher `p`.

`config.py`'s own 2026-07-08 note (`POOL_QUALITY_MODEL` block) anticipated this: it records that
numbers "now ALSO enters `_lanchester_strength` separately" and calls whether the two compound "an
empirical question for `lanchester_signature.py`". The readings in §1 answer it: they compound. The
comment at `resolve_engagements` ("Numbers-in-contact lives ONLY here under Lanchester") predates
the pool-quality model and is no longer true.

## 3. Which fix moves the exponent: probes, not code

To decide the stop condition this design had to know whether a fix that KEEPS troop numbers in the
pool can bring melee to the bar. Each probe below is a runtime monkeypatch in a throwaway script
outside the repo, applied to the instrument's own `check_law_exponents` (both arms, `TRAJ_SEEDS` 40,
same base and interpreter); nothing in the tree was edited. The `base` row reproduced §1 exactly on
both arms (1.50 / 1.70), which is the probe harness's control. Every fit was identifiable and no
trajectory routed.

| probe | what it changes | numbers in the pool? | melee p arm 0 / arm 1 | "volley" p arm 0 / arm 1 |
|---|---|---|---|---|
| base | nothing | yes | 1.50 / 1.70 | 2.10 / 1.70 |
| C | `lin_*` density frozen at its battle-start value (channel 1 out) | yes | 1.45 / 1.60 | 2.05 / 1.70 |
| D | `lin_*` reads the CONTACT cells' own troops, not the body average (the `MB_CLOSE_RANKS` reading of contact strength) | yes | 1.45 / 1.60 | 2.05 / 1.70 |
| B | degree graded against a fixed Ob 1, not the enemy's net (channel 3 out) | yes | 1.60 / 1.55 | 2.05 / 1.70 |
| BC | B and C together | yes | 1.55 / 1.45 | 1.85 / 1.65 |
| F | support ranks stop adding to the pair pool (numbers = troops in contact only) | yes (contact only) | 2.00 / 2.25 | 1.90 / 1.55 |
| DF | D and F together | yes (contact only) | 2.00 / 2.20 | 1.85 / 1.50 |
| scale 1.6 | `POOL_QUALITY_SCALE` 0.8 → 1.6 (env only; full instrument) | yes | 1.50 / 1.65 | 1.95 / 1.65 |
| scale 3.2 | `POOL_QUALITY_SCALE` → 3.2 (env only; full instrument) | yes | 1.50 / 1.45 | 1.95 / 1.70 |
| **E** | **the pair pool at a fixed reference size (`eff_size` 4): troop numbers OUT of the melee pool** | **no** | **1.05 / 1.00** | 1.45 / 1.20 |
| CE | E and C together | no | 1.00 / 1.00 | 1.35 / 1.10 |

The scale rows also read LINEAR 4:1 at 65% / 61% (1.6) and 69% / 70% (3.2), still under the band's 74%.

**Result: every probe that keeps numbers in the melee pool stays above 1.4 on at least one arm;
the one that takes them out (E) lands at the linear law on both arms.** The "volley" column is
explained in §5.1: that arm is mostly melee, which is why it falls when melee is fixed.

## 4. The fix, and the stop condition

**The fix the evidence supports:** melee pool = quality only. Troop numbers leave the base term of
`core/exchange.py::subunit_combat_pool` as the melee exchange uses it (`eff_power * eff_size`
becomes `eff_power` times a fixed reference size, the role probe E played; `pair_pool_contribution`
keeps splitting it by engaged share). Numbers then act on melee in two places only: the frontage
term (`lin_*`, how many men are in contact) and staying power (how long the body lasts). That is the
linear law's premise, and it is what the 2026-06-02 Command-only block in `config.py` already
argued: "numbers (Size) enter outcomes ONLY through the Lanchester frontage term".

**The stop condition fires.** On the evidence of §3 the only fix that reaches the bar removes troop
numbers from the pool, so it contradicts the 2026-07-08 directive. Per the entry: build nothing; put
the two directives to Jordan. `[ASSUMPTION; medium; the orchestrator or Jordan to correct]`: the probe
set (C, D, B, BC, F, DF, two scales) covers the plausible keep-numbers fixes. A fix outside it that
keeps numbers and passes would un-fire the stop. None is known.

### The question for Jordan

Two of your directives cannot both hold for melee as the engine is built:

1. **Pool strength from troop type, quality and numbers** (2026-07-08): *"abandon combat pools being
   related to the commander, and instead [derive them] solely from the subunit troop type, quality
   and numbers"*. Source: `modules/mass_battle/config.py`, the `POOL_QUALITY_MODEL` block; the
   ED-MB-0041 superseding row of 2026-10-01 (`registers/editorial_ledger_mb_archive.jsonl`) cites it
   as a prior ruling.
2. **Melee follows the linear law** (locked): *"linear melee / square volley per Jordan's confirm
   (not blended 1.5). Locked."* Source: `mb_lanchester_design.md` §6, quoted in
   `systems/mass_battle/sim/lanchester_signature.py`'s block above `LIN_EXP_MAX`, and by ED-MB-0050 and
   ED-MB-0045's 2026-10-01 row, which owes "melee attrition back to the locked linear law".

**Why they conflict.** With numbers in the pool, a bigger body rolls more dice, wins the opposed
roll more often and hits harder per man in contact, so its kill rate rises with its own numbers.
That is the square law's mechanism, so melee lands at p 1.5 to 1.7. The linear law needs a melee
kill rate set by frontage and quality, not by numbers behind the line.

**Options:**

- **(a) Numbers out of the melee dice.** Read directive 1 as "numbers act through frontage and
  staying power", not through the dice. Melee goes linear (probe E: p 1.05 / 1.00). Troop type and
  quality still set the pool; a bigger army still wins by overlap, by envelopment and by outlasting.
  Cost: directive 1's word "numbers" no longer reaches the pool, and every mass-battle magnitude
  calibrated since 2026-07-08 (`POOL_QUALITY_SCALE` 0.8, MB-07r's pike > heavy > levy ordering, the
  LINEAR 4:1 band) has to be re-read.
- **(b) Keep numbers in the pool and unlock the linear law for melee.** The engine stays as built
  (p 1.5 / 1.7, the "blended" regime the lock refused). The instrument's melee bar is re-set by your
  ruling, not tuned to the engine, and the CI job stays report-only until then.

Recommendation, as the ladder asks (`CLAUDE.md` §0): (a). The lock is the more specific ruling on
this exact quantity, and the 2026-06-02 block shows the same trade was made once before on the same
evidence. It stays a question because (a) overrides the plain words of a standing directive, and (a)
and (b) give two materially different battle games.

## 5. What the fix would move, and the exit (when built, if (a))

- **Code.** One base term: `core/exchange.py::subunit_combat_pool`'s `POOL_QUALITY_MODEL` branch,
  plus whatever `config.py` constant names the reference size. Do this AFTER the base-term
  consolidation the v11 entry orders: `hierarchy/units.py::Unit.base_combat_pool`'s copy moves into
  one function in `core/exchange.py` that both call, in its own commit, hash EQUAL, same operation
  order. Whether the unit-grain callers (pursuit, rearguard, freed attacker) also lose numbers is a
  build-time decision for the same ruling. They are not the melee exchange and the instrument does
  not read them. **If the stop holds (no ruling), that consolidation commit is CR-12's only code**,
  as the v11 entry provides. It is not built here.
  The fix need not touch `orchestration.py`, so ED-1043's extraction trigger (pre-flight item 4) is
  not tripped unless the stale comment at `resolve_engagements` is edited with it. Under (a) that
  comment becomes true again.
- **Hash: MOVER.** The three field golden digests in `systems/mass_battle/sim/bat.py::EXPECTED` and
  the `engine/tests` goldens. Also every season hash where a field is fought: MB-07r's commit records
  seed 2 fighting one at one season, while `build_realm(0)` and one season at seed 0 stay EQUAL
  because no field is fought there. Re-pinned in the batch's pin commit (P15), old → new.
- **Exit, as the entry states it:** melee p ≤ 1.4 with an identifiable fit (`TRAJ_SEEDS` 40) and
  volley p ≥ 1.6, on both arms; the planted collapse (`MB_FRICTION_SIGMA=4`, ED-MB-0045's 2026-10-08
  row: 57.0% FAIL) still FAILS LINEAR; all four checks passing flips the CI job. The flip is proposed
  in the PR body, because `.github/workflows/` is Jordan's (CODEOWNERS). The workflow comment on the
  `lanchester-signature` job ("It flips to blocking when fork #2 is ruled", with "melee fits
  p≈3.20") has been stale since ED-MB-0045's 2026-10-01 row ruled fork #2. That goes in the PR body
  too and is not edited.

### 5.1 Two instrument findings that block that exit as written

1. **The volley arm of LAW EXPONENTS is mostly melee.** Counted inside the instrument's own volley
   trajectory (`resolve_engagements_cascading` calls carrying pairs): 3,455 of 4,015 ticks resolved
   a melee pair on arm 0, and 4,026 of 4,586 on arm 1. The `balanced + kite` scenario stays out of
   contact in the shipped, rout-on sweep the instrument's comment measured, but not over a 160-tick
   no-rout trajectory. So the volley PASS rests partly on super-linear melee. Under probe E, volley
   reads 1.45 / 1.20 and FAILS. **A correct melee fix fails the volley bar until the volley scenario
   keeps melee at zero for the whole trajectory.** That is an instrument repair. It is owed before
   CR-12's exit can be read, and it is not this item's lane.
2. **The fit cannot separate a linear law with a frontage edge from a super-linear one.**
   `_best_exponent` fits `A^p − B^p` with equal coefficients. As a synthetic control through the
   instrument's own `_best_exponent`, an EXACT linear law in which the 800-troop body kills 7/5 as
   fast (its 7 columns against 5) reads p 1.45, 1.35 and 1.30 as the small body falls 400 → 300,
   → 200 and → 100. Equal rates read 1.00 and the square law reads 2.00, so the control behaves.
   The melee window here ends near B ≈ 290–310, where that edge alone reads about 1.45. Probe E landed at 1.0,
   so the engine does not show the edge in this pair today. But the 1.4 bar can fail a correctly
   linear engine whenever the bigger body's overlap tells. This is recorded, not fixed.

Also failing, not caused by MB-07r and not bisected here: **LINEAR 4:1 reads 52% on both arms** (63%
/ 52% with MB-07r's magnitudes reverted), against ED-MB-0045's 2026-10-08 reading of 77.0%. The
flip needs it in band, so whatever moved it has to be found before the exit can pass. Probe E did
not run the LINEAR check.

## 6. Not decided here

- The volley scenario repair (§5.1 item 1), and whether the fit should carry a frontage coefficient
  (item 2). Both belong to the instrument's owner, not to this item.
- What moved LINEAR 4:1 from 77% to 52% between ED-MB-0045's 2026-10-08 row and `aa6871b8`.
- Whether option (a) reaches the unit-grain pool (pursuit, rearguard, freed attacker).
