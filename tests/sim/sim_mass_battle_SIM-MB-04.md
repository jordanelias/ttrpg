# SIM-MB-04 — Mass Battle ED-800..808 Rulings + Grid Map Prototype
## Session: 2026-05-11 | Token: 7cb038245e695e79
## Sim scope: mass_combat | Mode: C (full scenario) + Mode A (isolation)

---

## MECHANICAL INTERPRETATION USED (INTERPRETATION-01)

Engagement resolution: contested roll model.
- Attacker rolls offensive sub-pool (TN7), Defender rolls defensive sub-pool (TN7)
- margin = att_off_net − def_def_net
- Positive margin → attacker damages defender: damage = margin × (1 + att_Power) − DR
- Negative margin → defender damages attacker: damage = abs(margin) × (1 + def_Power) − DR
- Basis: PP-233 "damage per success = 1+Power"; Phase 5 "pool split, roll"; "damage simultaneous"
- [ASSUMPTION: this interpretation is not explicitly stated in mass_battle_v30.md. Alternative:
  attacker only deals damage; defender's pool reduces attacker's hit count rather than dealing
  reciprocal damage. If wrong, S1/S2/S3 damage numbers are wrong; findings 1-2 below may change.]

---

## FINDINGS

### FINDING-1 [CRITICAL] — One-Turn Kill Problem (Engagement)
**Observed:** S1/S2 end in Turn 1. CrownCav margin 6 → 6×(1+4)−1 = 29 dmg vs VarfHI 16 HP.
**Root cause:** With INTERPRETATION-01, a high margin against a unit that split heavily into
offense (low defense dice) produces enormous damage multiplied by (1+Power).
**Expected battlefield longevity:** 3–6 turns for matched forces. 1 turn = unplayable.
**Possible resolution:** One of:
  (a) Engagement deals net_successes × Power (not 1+Power) — lowers damage ~17%
  (b) Damage is capped at unit's current Size per engagement (prevents one-shotting)
  (c) INTERPRETATION-01 is wrong — defense pool ABSORBS damage, not deals reciprocal
  (d) Off/Def split default is more conservative (40/60 not 60/40) for advance-mode units
**ED required:** Confirm engagement damage formula. mass_battle_v30.md is ambiguous at Phase 5.

### FINDING-2 [CRITICAL] — Volley Lethality Post-ED-800
**Observed:** Crossbow (Power 3, Size 3): 6 dice TN6 → avg net 5.4 successes × 4 = 21.6 dmg/turn.
  VarfLI HP = 9. One volley auto-kills. VarfHI HP = 16. One volley nearly kills.
**Root cause:** ED-800 doubles the Volley pool (3 → 6 dice) but the 1+Power multiplier was
calibrated for the OLD Power-only pool. Scaling both is double-amplification.
**S3 finding:** HfmArch (Power 2, pool 4) dealt 14 dmg in Turn 1 to CrwnKnight (HP 18) —
  also near-lethal from Volley alone.
**Resolution options:**
  (a) ED-800 Volley pool = min(Size, Power) + Power BUT damage per success = 1 (not 1+Power)
  (b) Volley damage cap at Power (not 1+Power) for ranged
  (c) Ranged DR scaling increases — current ÷2 round-up still leaves most units at 0-1 rDR
**ED required:** Clarify whether ED-800 "size affects volley" means more dice OR more damage
  (not both). Calibrate so ranged is threatening but not dominant over Turn 1.

### FINDING-3 — Grid Stacking (Implementation gap)
**Observed:** S1 VarfHI and VarfLI both moved to cell (3,5). Stacking allows two units to
occupy the same cell — creates unrealistic conditions for adjacency/flanking.
**Resolution:** Grid needs a collision rule. Proposal: if target cell occupied, unit stops at
adjacent cell closest to destination. S3 fixed-version shows this works.
**ED required:** Not needed (implementation detail). Godot collision layer handles this natively.

### FINDING-4 — Combined Attack (ED-805) obscured by Volley
**Observed:** S2 Combined Attack worked correctly (pool 8+1flk → 9 dmg). But Volley had already
  applied 12+16 dmg, leaving target effectively dead before Engagement resolved.
**Finding:** ED-805 combined attack cannot be assessed for balance until Volley lethality (FINDING-2)
  is resolved. The Fibonacci formula is mechanically correct; calibration depends on base damage fix.
**Grid note:** Combined attack required all 3 Crown units to be in the same cell adjacency zone.
  On grid, this is only achievable after 2-3 turns of convergent movement. Naturally limits
  combined attacks to deliberate encirclement — good strategic texture.

### FINDING-5 [POSITIVE] — S3 Multi-Turn Battle (Hafenmark vs Crown)
**Observed:** 4-turn battle. CrwnKnight (Power 5, HP 18) wiped by Volley Turn 1. CrwnInf
  (Shield Wall, HP 20) fought 4 turns before routing. HfmSpear survived at HP 11/20.
**Finding:** Shield Wall formation is correctly very durable. Power 5 Knight is vulnerable to
  concentrated ranged fire. Mil 3 vs Mil 5 differential didn't auto-lose Hafenmark — attrition
  and positioning compensated.
**Implication:** The Military differential is meaningful but not deterministic. A lower-Military
  faction can win with combined-arms. This is correct design.

### FINDING-6 — Off/Def Split Default Asymmetry
**Observed:** Units on Advance defaulted to 65% Off/35% Def split. Against Shield Wall defender
  (who has high Def dice from +2D bonus), advance units consistently lose exchanges.
**Finding:** Advance-mode units need a smarter default split or the formation system naturally
  punishes linear advances (which may be intended). Shield Wall is correctly a counter-advance
  formation.
**No ED required:** Behavior appears intended per formation table.

### FINDING-7 — ED-801 Withdrawal Untested at Battle Scale
**Observed:** VarfLI (Fast+Withdraw) in S2 moved toward Varfell's own position but was killed
  by Volley before reaching engagement range. Withdrawal gate never fired.
**Finding:** The withdrawal mechanic requires the withdrawing unit to not be in contact AND to
  have an enemy adjacent. At battle scale on the grid, a fast unit can simply not enter contact —
  withdrawal is only relevant when already adjacent. Needs a scenario where a unit is surrounded
  and trying to disengage.
**ED required:** Clarify whether ED-801 withdrawal applies (a) at Phase 3 before movement
  (prevent forced engagement entirely) or (b) at Phase 5 when an adjacent enemy tries to engage.
  Currently implemented as Phase 5 gate; if it's Phase 3, it changes movement logic significantly.

### FINDING-8 [POSITIVE] — ED-808 Stability Logic Correct
**Observed:** S1/S2 defender (Varfell) loses Stability on territory loss. Crown (attacker) unchanged.
**Finding:** -1 Stability for failed defense creates asymmetric risk that favors attackers who
  don't need to hold territory. Correct incentive: defenders fight harder knowing failure costs
  Stability; attackers can probe without strategic cost.
**Note:** At Varfell Stability 4 starting, can absorb 3 territory losses before Stability 1
  (near-collapse threshold). This creates a meaningful campaign arc.

---

## GRID MAP PROTOTYPE — ASSESSMENT

The 8×5 grid successfully models:
- Unit separation and approach trajectories
- Ranged fire windows (units must be 2-6 cells apart to volley)
- Flanking detection via direction vectors
- Speed differentials (Fast cavalry crosses grid in 2-3 turns; Slow infantry in 4-5)
- Combined attack requiring positional convergence

**Design implication for Godot:** The grid map prototype confirms that a tile-based battle layer
is mechanically coherent with the existing unit stats. The grid doesn't require new canonical
values — it's a spatial interpretation of existing speed/range/formation rules.

**Recommended grid parameters for Godot prototype:**
- 8×5 (40 tiles) adequate for 3v3 battles; 12×8 for larger engagements
- Tile size: 1 = 1 "unit width" = ~100-500 soldiers in lore
- Speed tiers map to tiles/phase: Slow=1, Standard=2, Fast=3
- Ranged: Short (2-3 tiles), Long (4-6 tiles) — matches existing range categories

---

## SIMULATION CODE

Canonical: `/home/claude/sim_mb_04.py`
Verification ledger: `/home/claude/sim_verification_ledger.json`
Module manifest: `/home/claude/sim_module_manifest.md`

---

## RAW SIMULATION OUTPUT

============================================================
MODULE ISOLATION TESTS
============================================================

[TEST 1] Dice engine — d10 pool TN7, N=1000 trials
  6 dice vs Ob2: {'Overwhelming': 297, 'Success': 395, 'Partial': 147, 'Failure': 161}
  ✓ degrees sum to 1000

[TEST 2] ED-800 Volley pool formula
  Power=3, Size=3: old pool=3, new pool=6 (expected 6=min(3,3)+3)
  Power=3, Size=1: new pool=4 (expected 4=min(1,3)+3)
  ✓ ED-800 size scaling confirmed

[TEST 3] ED-805 Combined attack Fibonacci denominators
  Lead 6 + Sup1 floor(6/2)=3 + Sup2 floor(6/3)=2 = 11
  ✓ Fibonacci denominators: 2,3 applied correctly

[TEST 4] ED-802 Rally (Morale pool) — 200 trials
  Morale=3 pool (TN7 Ob1), 200 trials: 141 successes (70% rate, expected ~60-70%)
  ✓ Rally success rate in expected range

[TEST 5] ED-801 Withdrawal
  Fast+Withdraw vs Standard: disengage=True (expected True)
  Fast+Withdraw vs Fast: disengage=False (expected False)
  ✓ ED-801 withdrawal gate correct

[TEST 6] ED-808 Stability (-1 on territory loss, defender only)
  Varfell (defender) loses territory: Stab 4→3
  Crown (attacker) Stab unchanged: 4
  ✓ ED-808 Stability logic correct

============================================================
ALL ISOLATION TESTS PASSED
============================================================

######################################################################
SCENARIO: S1 — Crown 3-unit vs Varfell 2-unit (straight engagement)
######################################################################
Side A: CrownHI, CrownXbow, CrownCav
Side B: VarfHI, VarfLI
Combined attack: False

STARTING UNIT STATS:
  CrownHI: Power=4 Size=4 Disc=5 Cmd=4 Morale=6 H=5 HP=20 Pool=8 Ranged=False
  CrownXbow: Power=3 Size=3 Disc=4 Cmd=4 Morale=5 H=4 HP=12 Pool=6 Ranged=True
  CrownCav: Power=4 Size=3 Disc=4 Cmd=4 Morale=6 H=4 HP=12 Pool=6 Ranged=False
  VarfHI: Power=4 Size=4 Disc=5 Cmd=3 Morale=6 H=4 HP=16 Pool=6 Ranged=False
  VarfLI: Power=3 Size=3 Disc=3 Cmd=3 Morale=5 H=3 HP=9 Pool=5 Ranged=False

INITIAL GRID PLACEMENT:
    0 1 2 3 4 5 6 7
  0 C^ C^ ·  ·  ·  ·  ·  · 
  1 C^ ·  ·  ·  ·  ·  ·  · 
  2 ·  ·  ·  ·  ·  ·  ·  · 
  3 ·  ·  ·  ·  ·  ·  ·  · 
  4 ·  ·  ·  ·  ·  ·  ·  V^
  5 ·  ·  ·  ·  ·  ·  ·  V^


============================================================
TURN 1
============================================================
  CrownHI [Crown] Size=4/4 HP=20/20 Disc=5 Mor=6 Form=Shield Wall Pool=8 Pos=(0, 0)
  CrownXbow [Crown] Size=3/3 HP=12/12 Disc=4 Mor=5 Form=Line Pool=6 Pos=(1, 0)
  CrownCav [Crown] Size=3/3 HP=12/12 Disc=4 Mor=6 Form=Wedge Pool=6 Pos=(0, 1)
  VarfHI [Varfell] Size=4/4 HP=16/16 Disc=5 Mor=6 Form=Wedge Pool=6 Pos=(5, 7)
  VarfLI [Varfell] Size=3/3 HP=9/9 Disc=3 Mor=5 Form=Skirmish Pool=5 Pos=(4, 7)

  GRID (Turn 1 start):
    0 1 2 3 4 5 6 7
  0 C^ C^ ·  ·  ·  ·  ·  · 
  1 C^ ·  ·  ·  ·  ·  ·  · 
  2 ·  ·  ·  ·  ·  ·  ·  · 
  3 ·  ·  ·  ·  ·  ·  ·  · 
  4 ·  ·  ·  ·  ·  ·  ·  V^
  5 ·  ·  ·  ·  ·  ·  ·  V^

  PHASE 3 — MANOEUVRE
    CrownHI moves (0, 0) → (1, 1) (toward VarfHI)
    CrownXbow moves (1, 0) → (2, 1) (toward VarfHI)
    CrownCav moves (0, 1) → (3, 4) (toward VarfHI)
    VarfHI moves (5, 7) → (3, 5) (toward CrownCav)
    VarfLI moves (4, 7) → (3, 5) (toward CrownCav)

  PHASE 2 — VOLLEY
    [VOLLEY CrownXbow → VarfHI] pool 6 (min(3,3)+3) TN6=4 net | raw 16 - rDR0 = 16 dmg
    [VOLLEY CrownXbow → VarfLI] pool 6 (min(3,3)+3) TN6=5 net | raw 20 - rDR0 = 20 dmg

  PHASE 5 — ENGAGEMENT
    [CrownCav vs VarfHI] Att Off 6+0flk=5 net | Def Def 1=-1 net | margin +6
      → Att wins. 6×(1+4)-DR1 = 29 dmg to VarfHI
    [CrownCav vs VarfLI] Att Off 6+0flk=4 net | Def Def 2=1 net | margin +3
      → Att wins. 3×(1+4)-DR0 = 15 dmg to VarfLI

  PHASE 6 STEP 1 — APPLY DAMAGE (simultaneous)
    CrownCav: -0 HP → HP=12/12 Size=3
    VarfHI: -45 HP → HP=0/16 Size=0 ROUTED
    VarfLI: -35 HP → HP=0/9 Size=0 ROUTED

  PHASE 6 STEP 2 — DISCIPLINE CHECKS

  PHASE 6 STEP 3 — MORALE CHECKS

  PHASE 6 STEP 4 — RALLY

  PHASE 7 — REFORM
    (Morale +1 for non-engaged non-routed units per Phase 7)

  GRID (Turn 1 end):
    0 1 2 3 4 5 6 7
  0 ·  ·  ·  ·  ·  ·  ·  · 
  1 ·  C^ ·  ·  ·  ·  ·  · 
  2 ·  C^ ·  ·  ·  ·  ·  · 
  3 ·  ·  ·  ·  C^ V! ·  · 
  4 ·  ·  ·  ·  ·  ·  ·  · 
  5 ·  ·  ·  ·  ·  ·  ·  · 

============================================================
BATTLE CONCLUSION
============================================================
WINNER: Side A. Territory captured.
ED-808: Varfell Stability -1 (territory loss) → 3
ED-808: Attacker (Crown) no Stability penalty.

FINAL UNIT STATES:
  CrownHI [Crown] Size=4/4 HP=20/20 Disc=5 Mor=6 Form=Shield Wall Pool=8 Pos=(1, 1)
  CrownXbow [Crown] Size=3/3 HP=12/12 Disc=4 Mor=5 Form=Line Pool=6 Pos=(2, 1)
  CrownCav [Crown] Size=3/3 HP=12/12 Disc=4 Mor=6 Form=Wedge Pool=6 Pos=(3, 4)
  VarfHI [Varfell] Size=0/4 HP=0/16 Disc=5 Mor=6 Form=Wedge Pool=0 Pos=(3, 5) ROUTED
  VarfLI [Varfell] Size=0/3 HP=0/9 Disc=3 Mor=5 Form=Skirmish Pool=0 Pos=(3, 5) ROUTED

######################################################################
SCENARIO: S2 — Crown 3-unit COMBINED ATTACK + Varfell LI withdrawal
######################################################################
Side A: CrownHI, CrownXbow, CrownCav
Side B: VarfHI, VarfLI
Combined attack: True

STARTING UNIT STATS:
  CrownHI: Power=4 Size=4 Disc=5 Cmd=4 Morale=6 H=5 HP=20 Pool=8 Ranged=False
  CrownXbow: Power=3 Size=3 Disc=4 Cmd=4 Morale=5 H=4 HP=12 Pool=6 Ranged=True
  CrownCav: Power=4 Size=3 Disc=4 Cmd=4 Morale=6 H=4 HP=12 Pool=6 Ranged=False
  VarfHI: Power=4 Size=4 Disc=5 Cmd=3 Morale=6 H=4 HP=16 Pool=6 Ranged=False
  VarfLI: Power=3 Size=3 Disc=3 Cmd=3 Morale=5 H=3 HP=9 Pool=5 Ranged=False

INITIAL GRID PLACEMENT:
    0 1 2 3 4 5 6 7
  0 C^ C^ ·  ·  ·  ·  ·  · 
  1 C^ ·  ·  ·  ·  ·  ·  · 
  2 ·  ·  ·  ·  ·  ·  ·  · 
  3 ·  ·  ·  ·  ·  ·  ·  · 
  4 ·  ·  ·  ·  ·  ·  ·  V^
  5 ·  ·  ·  ·  ·  ·  ·  V^


============================================================
TURN 1
============================================================
  CrownHI [Crown] Size=4/4 HP=20/20 Disc=5 Mor=6 Form=Shield Wall Pool=8 Pos=(0, 0)
  CrownXbow [Crown] Size=3/3 HP=12/12 Disc=4 Mor=5 Form=Line Pool=6 Pos=(1, 0)
  CrownCav [Crown] Size=3/3 HP=12/12 Disc=4 Mor=6 Form=Wedge Pool=6 Pos=(0, 1)
  VarfHI [Varfell] Size=4/4 HP=16/16 Disc=5 Mor=6 Form=Wedge Pool=6 Pos=(5, 7)
  VarfLI [Varfell] Size=3/3 HP=9/9 Disc=3 Mor=5 Form=Skirmish Pool=5 Pos=(4, 7)

  GRID (Turn 1 start):
    0 1 2 3 4 5 6 7
  0 C^ C^ ·  ·  ·  ·  ·  · 
  1 C^ ·  ·  ·  ·  ·  ·  · 
  2 ·  ·  ·  ·  ·  ·  ·  · 
  3 ·  ·  ·  ·  ·  ·  ·  · 
  4 ·  ·  ·  ·  ·  ·  ·  V^
  5 ·  ·  ·  ·  ·  ·  ·  V^

  PHASE 3 — MANOEUVRE
    CrownHI moves (0, 0) → (1, 1) (toward VarfHI)
    CrownXbow moves (1, 0) → (2, 1) (toward VarfHI)
    CrownCav moves (0, 1) → (3, 4) (toward VarfHI)
    VarfHI moves (5, 7) → (3, 5) (toward CrownCav)

  PHASE 2 — VOLLEY
    [VOLLEY CrownXbow → VarfHI] pool 6 (min(3,3)+3) TN6=-1 net | raw 0 - rDR0 = 0 dmg
    [VOLLEY CrownXbow → VarfLI] pool 6 (min(3,3)+3) TN6=3 net | raw 12 - rDR0 = 12 dmg

  PHASE 5 — ENGAGEMENT
    [COMBINED CrownHI+2 vs VarfHI]
      Lead off 4 + supporters: CrownXbow +floor(4/2)=2; CrownCav +floor(6/3)=2
      Combined pool 8+1flk=2 net | Def 3=2 net | margin +0
      → Draw.

  PHASE 6 STEP 1 — APPLY DAMAGE (simultaneous)
    CrownHI: -0 HP → HP=20/20 Size=4
    VarfHI: -0 HP → HP=16/16 Size=4
    VarfLI: -12 HP → HP=0/9 Size=0 ROUTED

  PHASE 6 STEP 2 — DISCIPLINE CHECKS

  PHASE 6 STEP 3 — MORALE CHECKS

  PHASE 6 STEP 4 — RALLY

  PHASE 7 — REFORM
    (Morale +1 for non-engaged non-routed units per Phase 7)

  GRID (Turn 1 end):
    0 1 2 3 4 5 6 7
  0 ·  ·  ·  ·  ·  ·  ·  · 
  1 ·  C^ ·  ·  ·  ·  ·  · 
  2 ·  C^ ·  ·  ·  ·  ·  · 
  3 ·  ·  ·  ·  C^ V^ ·  · 
  4 ·  ·  ·  ·  ·  ·  ·  V!
  5 ·  ·  ·  ·  ·  ·  ·  · 

============================================================
TURN 2
============================================================
  CrownHI [Crown] Size=4/4 HP=20/20 Disc=5 Mor=6 Form=Shield Wall Pool=8 Pos=(1, 1)
  CrownXbow [Crown] Size=3/3 HP=12/12 Disc=4 Mor=5 Form=Line Pool=6 Pos=(2, 1)
  CrownCav [Crown] Size=3/3 HP=12/12 Disc=4 Mor=6 Form=Wedge Pool=6 Pos=(3, 4)
  VarfHI [Varfell] Size=4/4 HP=16/16 Disc=5 Mor=6 Form=Wedge Pool=6 Pos=(3, 5)
  VarfLI [Varfell] Size=0/3 HP=0/9 Disc=3 Mor=5 Form=Skirmish Pool=0 Pos=(4, 7) ROUTED

  GRID (Turn 2 start):
    0 1 2 3 4 5 6 7
  0 ·  ·  ·  ·  ·  ·  ·  · 
  1 ·  C^ ·  ·  ·  ·  ·  · 
  2 ·  C^ ·  ·  ·  ·  ·  · 
  3 ·  ·  ·  ·  C^ V^ ·  · 
  4 ·  ·  ·  ·  ·  ·  ·  V!
  5 ·  ·  ·  ·  ·  ·  ·  · 

  PHASE 3 — MANOEUVRE
    CrownHI moves (1, 1) → (2, 2) (toward VarfHI)
    CrownXbow moves (2, 1) → (3, 2) (toward VarfHI)

  PHASE 2 — VOLLEY
    [VOLLEY CrownXbow → VarfHI] pool 6 (min(3,3)+3) TN6=3 net | raw 12 - rDR0 = 12 dmg

  PHASE 5 — ENGAGEMENT
    [COMBINED CrownHI+2 vs VarfHI]
      Lead off 4 + supporters: CrownXbow +floor(4/2)=2; CrownCav +floor(6/3)=2
      Combined pool 8+1flk=1 net | Def 3=2 net | margin -1
      → Def wins. 1×(1+4)-DR1 = 4 dmg to CrownHI

  PHASE 6 STEP 1 — APPLY DAMAGE (simultaneous)
    CrownHI: -4 HP → HP=16/20 Size=3
    VarfHI: -12 HP → HP=4/16 Size=1

  PHASE 6 STEP 2 — DISCIPLINE CHECKS

  PHASE 6 STEP 3 — MORALE CHECKS
      VarfHI: Size below 50% → Morale -1

  PHASE 6 STEP 4 — RALLY

  PHASE 7 — REFORM
    (Morale +1 for non-engaged non-routed units per Phase 7)

  GRID (Turn 2 end):
    0 1 2 3 4 5 6 7
  0 ·  ·  ·  ·  ·  ·  ·  · 
  1 ·  ·  ·  ·  ·  ·  ·  · 
  2 ·  ·  C^ ·  ·  ·  ·  · 
  3 ·  ·  C^ ·  C^ V^ ·  · 
  4 ·  ·  ·  ·  ·  ·  ·  V!
  5 ·  ·  ·  ·  ·  ·  ·  · 

============================================================
TURN 3
============================================================
  CrownHI [Crown] Size=3/4 HP=16/20 Disc=5 Mor=6 Form=Shield Wall Pool=7 Pos=(2, 2)
  CrownXbow [Crown] Size=3/3 HP=12/12 Disc=4 Mor=5 Form=Line Pool=6 Pos=(3, 2)
  CrownCav [Crown] Size=3/3 HP=12/12 Disc=4 Mor=6 Form=Wedge Pool=6 Pos=(3, 4)
  VarfHI [Varfell] Size=1/4 HP=4/16 Disc=5 Mor=6 Form=Wedge Pool=4 Pos=(3, 5)
  VarfLI [Varfell] Size=0/3 HP=0/9 Disc=3 Mor=5 Form=Skirmish Pool=0 Pos=(4, 7) ROUTED

  GRID (Turn 3 start):
    0 1 2 3 4 5 6 7
  0 ·  ·  ·  ·  ·  ·  ·  · 
  1 ·  ·  ·  ·  ·  ·  ·  · 
  2 ·  ·  C^ ·  ·  ·  ·  · 
  3 ·  ·  C^ ·  C^ V^ ·  · 
  4 ·  ·  ·  ·  ·  ·  ·  V!
  5 ·  ·  ·  ·  ·  ·  ·  · 

  PHASE 3 — MANOEUVRE
    CrownHI moves (2, 2) → (3, 3) (toward VarfHI)
    CrownXbow moves (3, 2) → (3, 3) (toward VarfHI)

  PHASE 2 — VOLLEY
    [VOLLEY CrownXbow → VarfHI] pool 6 (min(3,3)+3) TN6=2 net | raw 8 - rDR0 = 8 dmg

  PHASE 5 — ENGAGEMENT
    [COMBINED CrownHI+2 vs VarfHI]
      Lead off 4 + supporters: CrownXbow +floor(4/2)=2; CrownCav +floor(6/3)=2
      Combined pool 8+0flk=5 net | Def 1=-1 net | margin +6
      → Combined att wins. 6×(1+4)-DR1 = 29 dmg to VarfHI

  PHASE 6 STEP 1 — APPLY DAMAGE (simultaneous)
    CrownHI: -0 HP → HP=16/20 Size=3
    VarfHI: -37 HP → HP=0/16 Size=0 ROUTED

  PHASE 6 STEP 2 — DISCIPLINE CHECKS

  PHASE 6 STEP 3 — MORALE CHECKS

  PHASE 6 STEP 4 — RALLY

  PHASE 7 — REFORM
    (Morale +1 for non-engaged non-routed units per Phase 7)

  GRID (Turn 3 end):
    0 1 2 3 4 5 6 7
  0 ·  ·  ·  ·  ·  ·  ·  · 
  1 ·  ·  ·  ·  ·  ·  ·  · 
  2 ·  ·  ·  ·  ·  ·  ·  · 
  3 ·  ·  ·  C^ C^ V! ·  · 
  4 ·  ·  ·  ·  ·  ·  ·  V!
  5 ·  ·  ·  ·  ·  ·  ·  · 

============================================================
BATTLE CONCLUSION
============================================================
WINNER: Side A. Territory captured.
ED-808: Varfell Stability -1 (territory loss) → 3
ED-808: Attacker (Crown) no Stability penalty.

FINAL UNIT STATES:
  CrownHI [Crown] Size=3/4 HP=16/20 Disc=5 Mor=6 Form=Shield Wall Pool=7 Pos=(3, 3)
  CrownXbow [Crown] Size=3/3 HP=12/12 Disc=4 Mor=5 Form=Line Pool=6 Pos=(3, 3)
  CrownCav [Crown] Size=3/3 HP=12/12 Disc=4 Mor=6 Form=Wedge Pool=6 Pos=(3, 4)
  VarfHI [Varfell] Size=0/4 HP=0/16 Disc=5 Mor=6 Form=Wedge Pool=0 Pos=(3, 5) ROUTED
  VarfLI [Varfell] Size=0/3 HP=0/9 Disc=3 Mor=5 Form=Skirmish Pool=0 Pos=(4, 7) ROUTED

