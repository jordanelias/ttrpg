# Mass Battle Patch Proposals — 2026-04-29
<!-- From: mass_battle_stress_test_2026-04-29.md + historical NERS review -->
<!-- Status: PROPOSAL — each requires Jordan approval before application to canonical docs -->

---

## AUTO-APPROVABLE (no design decision required)

These are clarifications / corrections to existing canonical intent, not design changes.

### PP-PROP-MB-01 — H frozen at battle start [MATH-FAIL-02]
File: mass_battle_v30.md §A.4, params/mass_combat.md §Core Formula
Add to §A.4 Discipline block and PP-233 commentary:
> "H per Size is computed once at the start of the battle from the unit's opening Discipline and
> Command values, then frozen for the battle's duration. Discipline degradation (Phase 6 Step 2)
> modifies the Effective Power penalty table only — it does not recalculate H or Total Health."

Rationale: PP-233 states "H is fixed" but H formula uses Discipline which degrades. This resolves
the contradiction by specifying when H is evaluated.

---

### PP-PROP-MB-02 — §A.5 personal combat pause disambiguation [S-FAIL-04]
File: mass_battle_v30.md §A.5
Current: "Mass battle pauses during personal combat."
Replace with:
> "Mass battle pauses if one general enters personal combat (the army is without command until
> resolved). Exception: if both generals enter personal combat simultaneously (PP-506), mass battle
> does not freeze — both armies continue uncommanded at 1D minimum, Line formation, no tactics,
> until each general re-establishes Command (Ob 2, Phase 1 of following turn)."

Rationale: PP-506 already states bilateral = no freeze. §A.5 must reflect this distinction.

---

### PP-PROP-MB-03 — §A.12 Morale Cascade timing assigned to Phase 6 Step 3 [S-FAIL-17]
File: mass_battle_v30.md §A.12, params/mass_combat.md
Current: "When a unit routs... all friendly units in same engagement make an immediate Discipline
check Ob 1."
Replace "immediate" with:
> "When a unit routs (Morale reaches 0), at Phase 6 Step 3 (Morale checks), all friendly units
> in the same engagement make a Discipline check Ob 1. Failure: Morale −1. This fires as part of
> Step 3, not as a separate interrupt — multiple simultaneous routs all trigger their cascade checks
> at Step 3 together."

Rationale: "Immediate" is ambiguous vs Phase 6 step ordering. Step 3 is the only coherent placement
(after Step 1 damage, after Step 2 Discipline checks, during Morale processing).

---

### PP-PROP-MB-04 — "Rout" vs "Destroyed" defined; Artillery trigger enumerated [S-FAIL-18]
File: mass_battle_v30.md §A.4 (add to Morale block)
Add definitional note:
> "**Rout:** Morale reaches 0 — unit flees, cannot fight back (§A.12). Triggered by Morale checks.
> **Destroyed:** Size reaches 0 — unit eliminated, removed from battle immediately at Phase 6 Step 1.
> These are distinct states with distinct trigger chains.
> §A.12 Morale Cascade fires only on Morale rout, not on destruction by Size loss.
> Artillery destruction (Size→0 at Step 1) triggers Morale −1 to adjacent allies (per §A.4
> 'Allied unit routed in same zone' and PP-198) as a separate enumerated trigger — this is NOT
> §A.12 cascade and does not fire the Discipline check."

Rationale: PP-198 and §A.12 currently overlap ambiguously. This separates the two chains cleanly.

---

### PP-PROP-MB-05 — Idle army carve-out for terrain-blocked engagements [S-FAIL-08]
File: mass_battle_v30.md §A.7 Phase 7, params/mass_combat.md
Current Phase 7 idle rule: "if no engagements in Phase 5 this turn AND previous turn: both sides
lose 1 Morale."
Add exception:
> "Terrain exception: the idle army rule does not fire for a side that was unable to initiate
> any engagement due to terrain constraint (defender behind Walls/fortifications who cannot advance;
> either side in Narrow Pass with no available approach route this turn). The rule applies only to
> voluntary inaction, not terrain-forced inaction."

Rationale: A defender correctly holding walls loses Morale for doing their job correctly. This is
both historically incorrect and a perverse incentive against fortification play.

---

### PP-PROP-MB-06 — Params §ED-019 Crown/Church tactic cards STRUCK [S-FAIL-20]
File: params/mass_combat.md
Add to §ED-019 entry:
> "STRUCK — PP-283 confirmed mass_battle_v30.md §B.4 as canonical for all faction tactic cards.
> §ED-019 Crown and Church cards (Royal Authority, Diplomatic Shield, Templar Vanguard,
> Excommunication Threat) are superseded by §B.4 (Royal Guard, Ducal Call, and Church equivalents).
> Struck 2026-04-29."

---

### PP-PROP-MB-07 — Command halving rounding: floor [Minor-3c]
File: mass_battle_v30.md §A.5, params/mass_combat.md
Add to Stage 1 death block:
> "Command halved: floor(Command / 2). Minimum 1 — a Stage 1 general retains at least 1 Command."

Rationale: Floor is standard in Valoria (all other halving uses floor). Command=1 → floor(0.5) = 0
would create a second Command=0 state identical to Stage 2; floor with minimum 1 preserves the
Stage 1 / Stage 2 distinction.

---

### PP-PROP-MB-08 — Crossbow reload: every turn at mass scale [S-FAIL-12]
File: params/mass_combat.md §PP-301
Add STRUCK to §PP-301 ED-094 sub-entry:
> "§PP-301 ED-094 (binary reload marker) STRUCK — superseded by standalone §ED-094 resolution
> (2026-04-03): HP crossbow units fire every Volley Phase at mass combat scale; individual reload
> is abstracted. Struck 2026-04-29."

---

## REQUIRES JORDAN DECISION

### DECISION-MB-01 — PP-297 Stalemate Break: which version is canonical? [S-FAIL-01]
Option A (design doc §A.12): 3-turn zero-damage → Tactical Withdrawal, ends inconclusive.
  - No Rout possible. IP +1 at Accounting (military posturing). Both sides leave.
Option B (params §PP-297): 3-turn zero-damage → Discipline Ob 1 → Morale −1 → possible Rout.
  - Battle may continue if neither side routs. Rout possible.
Option A is cleaner (E) and historically accurate (prolonged indecision = mutual withdrawal, not
collapse — armies needed to eat). Recommend Option A.

### DECISION-MB-02 — Muster initial Size: §1.2 defaults vs §1.4 formula [S-FAIL-13]
Option A: Strike §1.2 defaults as "default" language; §1.4 formula governs all muster output.
  Levy at Prosperity 1-3 = Size 2. HI at Prosperity 6-7 = Size 4.
Option B: Strike §1.4 formula; §1.2 defaults are the muster output by unit type regardless of
  Prosperity. Prosperity modifier applies only as a one-time additional bonus.
Option C: §1.4 governs base; §1.2 defaults are the TARGET SIZE (what full reinforcement looks like),
  not the muster output. Units build toward the defaults through reinforcement seasons.
Recommend Option C — it makes the defaults meaningful without conflicting with the formula.

### DECISION-MB-03 — Morale reset between battles [S-FAIL-06]
Option A: Morale resets to starting formula (Command + quality modifier) at each battle start.
Option B: Morale persists across battles in a campaign.
Recommend Option A: resets. Otherwise long-campaign units start battles at dangerously low Morale
from prior degradation, which snowballs toward deterministic rout regardless of player decisions.
Persistent Morale is a separate mechanic (campaign fatigue) that could be layered later.

### DECISION-MB-04 — Discipline recovery between battles [S-FAIL-05]
Option A: Discipline recovers fully at battle end (resets to min(Command, Military ceiling)).
Option B: Discipline persists; recovery only via Muster action on existing unit.
Option C: Discipline recovers +1 per season of garrison (non-hostile, non-active territory).
Recommend Option B — consistent with §1.7 Wealth Zero logic and creates meaningful strategic
consequence for burning through Discipline in battle.

### DECISION-MB-05 — Rout contagion brake at Morale 0 [S-FAIL-16]
Option A: Secondary contagion loss CAN bring a unit to Morale 0, but that unit does NOT rout
  until next turn (brake prevents immediate cascade rout).
Option B: Secondary contagion loss is capped at Morale 1 (floor) — cannot drive to 0 at all.
Recommend Option A: cleaner, preserves the floor-1 mechanic while still allowing eventual collapse.

### DECISION-MB-06 — Shadow Intel UX resolution [S-FAIL-19]
Option A (Peek): Both sides commit tactic card simultaneously. Varfell then sees opponent's
  committed card and may swap their own before reveal. One-card hand-reveal delay.
Option B (Sequential): Opponent commits first publicly. Varfell then chooses and commits. Both reveal.
Historical note: Option A (peek) is more grounded — intelligence about enemy deployment was gained
while both sides were already committed to their approach. Option B creates an asymmetric turn
structure that complicates the BG UI significantly.
Recommend Option A.

### DECISION-MB-07 — Siege formula fix [MATH-FAIL-01]
The stated Ob = 2 + Fort Level is impossible under Military stat pool (Ob 5 from 4 dice = 0%).
Reverse-engineering the claimed 2%: TN7, pool=7, Ob=6.
Options:
  A: Pool = Military stat + 3 (representing siege engineers, equipment). Fort3 Mil4: pool=7, Ob=6 → 2%. Matches.
  B: Ob = Fort Level only (not 2+Fort). Fort3 Mil4: Ob=3, pool=4 → 18%. Too easy.
  C: Pool = Military stat, Ob = Fort Level (not 2+Fort). Fort3 Mil4: Ob=3 → 18%. Too easy.
  D: Pool = 2×Military. Fort3 Mil4: pool=8, Ob=5 → 5%. Close.
Recommend Option A: Pool = Military + 3 siege bonus. Produces calibration match and makes sense
thematically (siege trains add capability beyond raw Military stat).

### DECISION-MB-08 — Cascade speed: should cap be loosened for encirclement? [Historical]
Morale cap of −3/phase (plus −2 for general kill) means a unit at Morale 6 takes 2+ phases to
rout even under worst conditions. Historically, encircled armies (Cannae) and armies with no
retreat route collapsed catastrophically fast.
Proposal: Add encirclement condition — if a unit has no valid retreat path (flanked from 3+
directions, or all retreat zones occupied by enemy), the Morale cap is removed (or raised to −5).
This is a design addition, not a fix. Jordan's call on whether the game needs this.

---

## HISTORICAL DESIGN NOTES (no action, record only)

- Pursuit lethality is structurally correct (no Defence, net Offence = Size loss). Calibration
  should be verified in simulation. Historical pursuit killed 70-80% of routing armies.
- Depth rotation (Roman manipular, shield wall relief) is not modeled. This is acceptable for E.
  A "Formation Relief" tactic card could be a future addition.
- Officer death rate (1d20 ≤ Size lost) is conservative vs historical officer mortality. Appropriate
  for named-NPC retention. No change recommended.
- Pre-battle intel: Shadow Intel as "peek" (DECISION-MB-06 Option A) is historically grounded.
  Generals read enemy deployment before committing. Simultaneous-secret-declaration is an abstraction.
