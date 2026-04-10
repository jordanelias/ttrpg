# Simulation Report: Territory Operations Suite
## Test ID: SIM-TERR-01
## Date: 2026-04-09
## Modes: A + D + J + L
## Systems: Casus Belli, Invading Territory, Seizing Territory, Claiming Territory,
##           Conceding Territory, Trading Territory, Developing Territory (Fortify + Govern)
## Sources: params_board_game.md (1541 lines), valoria_bg_v05 (734 lines),
##          geography_design.md (138 lines), mass_battle_v3.md (696 lines),
##          canon/02_canon_constraints.md (25 lines), params_factions.md (565 lines)
##          sim_graduated_seizure_SIM-GS-01.md (163 lines)

---

## FETCH LOG
canonical_sources.yaml:              ✓ (154 lines)
designs/setting/geography_design.md: ✓ (138 lines)
designs/board_game/valoria_bg_v05:   ✓ (734 lines)
designs/mass_combat/mass_battle_v3:  ✓ (696 lines)
references/params_board_game.md:     ✓ (1541 lines)
references/params_factions.md:       ✓ (565 lines)
canon/02_canon_constraints.md:       ✓ (25 lines)
tests/sim_graduated_seizure_SIM-GS-01.md: ✓ (163 lines)

---

## SCOPE OF MECHANICS TESTED

| Mechanic | Source | Status |
|----------|--------|--------|
| Casus Belli (CB) | bg_v05 §I-03, PP-014, SIM-GS-01 L2 | GAP — no definition |
| Invading Territory (March + Battle) | params_board_game §Battle Resolution | Defined |
| Seizing Territory (Church Graduated) | params_board_game §PP-494 | Partially defined |
| Claiming Territory (Uncontrolled entry) | params_board_game §PP-500 | Defined |
| Conceding Territory | MISSING | GAP — no definition |
| Trading Territory (Diplomatic transfer) | MISSING | GAP — no definition |
| Developing Territory (Govern/Fortify) | params_board_game §Standard Action Ob | Defined |

---

## ═══════════════════════════════════════════════════════
## MECHANIC 1: CASUS BELLI (CB)
## ═══════════════════════════════════════════════════════

### Spec Reconstruction (from scattered references)

CB is referenced in 4 locations without a unified definition:

1. **I-03 / PP-014:** "Treaty Betrayal → Free CB vs betrayer — permanent until used. Other
   CBs (Brutal disposition, fabricated Heresy Investigation) expire after 3 seasons unused.
   Varfell Patience Protocol CB expires on Riskbreaker exposure."
2. **PP-494 (Graduated Seizure):** "Seizure attempt grants controlling faction Casus Belli vs Church."
3. **SIM-GS-01 L2:** "CB undefined — mechanic referenced but no ruleset definition. Blocks
   accurate play." [P1]
4. **bg_v05 §Cognitive Load:** "CB: well-defined acquisition and effect. Load ≈ 3/10." — but
   the *effect* is never stated in any fetched doc.

### MODE A — Isolation

**What CB does (reconstructable from context):**
- Reduces Ob for a Military action targeting the CB-granting faction (implied by "Patience
  Protocol CB expires on Riskbreaker exposure" and "used for Military action" per PP-014).
- PP-014 text: "CB Expiration: 2 seasons after acquisition if unused for a Military action."
  This implies CB is specifically a gate/bonus on Military actions (Legionary/March/Battle).

**CB effect candidates (from cognitive load assessment "well-defined acquisition and effect"):**
No explicit effect text found in any canonical document.

**[FINDING CB-A-01 — P1]:** CB effect is undefined in all fetched canonical sources.
The cognitive load comment in bg_v05 is wrong or refers to a version of the document
that no longer exists. CB acquisition is partially defined (treaty betrayal, Brutal
disposition, Heresy Investigation, PP-494 seizure, Patience Protocol). CB effect is absent.

**[FINDING CB-A-02 — P1]:** CB expiration rules are internally contradictory.
PP-014: treaty CB = permanent; non-treaty CB = 3 seasons.
PP-494: seizure CB is granted per attempt with no expiration stated.
No unified CB expiration table exists.

**CB Acquisition Sources (reconstructed):**
| Source | CB Type | Expiration |
|--------|---------|------------|
| Treaty betrayal | Permanent | Never |
| Brutal faction disposition | Tactical | 3 seasons |
| Fabricated Heresy Investigation | Tactical | 3 seasons |
| Varfell Patience Protocol | Special | On Riskbreaker exposure |
| PP-494 Graduated Seizure attempt | Tactical | UNDEFINED |
| PP-428 Piety Spread | MISSING | UNDEFINED |

**CB stacking:** Whether multiple CBs vs the same faction stack (reduced Ob per CB, or
one CB = one-time binary toggle) is undefined.

**CB and non-Military actions:** Whether CB applies to non-Military Domain Actions
(e.g., Govern, Diplomacy) is undefined.

### MODE D — Edge Cases

**D1. Treaty CB + Military action sequencing:**
If Crown holds permanent treaty CB vs Hafenmark, and Crown plays Legionary card to March
into T8 (Hafenmark capital, Fort 1): does CB reduce Battle Ob? By how much?
UNDEFINED. The mechanic references "Military action" but provides no Ob modifier value.

**D2. [FINDING CB-D-02 — P1]:** CB and Battle initiation distinction: is CB required to
*initiate* Battle against a faction (i.e., attacking a non-adjacent territory requires CB),
or does CB provide a bonus *during* Battle? The distinction is critical:
- Model A (initiation gate): CB is required to declare war. Without CB, you cannot March
  into a friendly or neutral faction's territory.
- Model B (bonus): CB provides a mechanical bonus (+D or −Ob) to an already-permitted
  Military action. No gate function.
bg_v05 says "used for a Military action" (per PP-014), implying Model B. But if CB has no
gate function, what prevents arbitrary declaration of war at any time? March resolution
currently has no "must have CB" language. Factions can simply March into any adjacent
territory. This means CB is a bonus mechanic, not a gate mechanic — but its bonus is
undefined.

**D3. [FINDING CB-D-03 — P2]:** CB persistence through faction elimination:
If the CB-granting faction is eliminated (Stability 0, Political Vacuum per PP-500), the
CB target no longer exists. Whether the CB is lost, transferred to Löwenritter (as Crown's
successor), or persists as a general "faction hostility" token is undefined.

**D4. CB and the Mandate Uphold/Appease trigger (PP-189):**
PP-189 trigger: "Domain Action directly challenges a faction's core institutional authority."
Marching into a territory with CB backing — does the CB suppress the Appease option? Or
does Appease still work (faction cancels the action for Mandate −1)? Undefined.

**D5. [FINDING CB-D-05 — P2]:** CB and Diplomatic Tokens (PP-432):
If Hafenmark has a Diplomatic Token on Crown's mat, does Crown's CB vs Hafenmark get
consumed or suppressed? The Diplomatic Token says "target faction counts as Support in
Parliamentary Sessions" — no military interaction. But the diplomatic relationship they
represent ought to have some bearing on CB-based aggression. No rule stated.

### MODE J — Cognitive Load

**J1. [FINDING CB-J-01 — P2]:** CB is a floating mechanic. Players who acquire it have
no reference for what it does. The acquisition conditions are scattered across 4+ documents
with no centralized CB section. The cognitive load assessment of "3/10" in bg_v05 is
impossible to validate because the effect is not written down.

**J2.** No CB tracking token is described. Players may forget they hold CBs across seasons.
A faction mat section for CB tokens is needed.

### MODE L — Precedent / Cross-System

**L1.** March into uncontrolled territory (PP-500): no CB required, no Battle. March into
controlled territory: Battle required (implicit from resolution rules). CB's relationship
to this distinction is the key design question — is CB a narrative justification or a
mechanical gate/bonus?

**L2.** Löwenritter Riskbreakers: "Priority: Varfell Patience Protocol CB expires on
Riskbreaker exposure." This implies Riskbreakers have a detection action that burns
Patience Protocol CBs. No such action is specified in the Riskbreaker AI tree.

**L3. [FINDING CB-L-03 — P1]:** CB from PP-494 Graduated Seizure is granted to the
defending faction on every seizure attempt. If Church attempts seizure 10 times, the
defender accumulates 10 CBs. Whether these stack (exponential Ob reduction) or are
capped (1 CB per faction pair at a time) is undefined. Given that Seizure attempts can
be frequent (one/season post-TC 75), this creates potential mechanical runaway.

---

## ═══════════════════════════════════════════════════════
## MECHANIC 2: INVADING TERRITORY (MARCH + BATTLE)
## ═══════════════════════════════════════════════════════

### Spec (from params_board_game.md)

**March:** Legionary Outward. No roll for uncontested entry. Contested entry = Battle.
Battle Ob Formula (PP-499): Ob = defender Military ÷ 2 (round up, min 1).
Pool: attacker Military + Fort bonus for defender.
Fort bonus: Fort Level added as bonus dice to defensive Military roll (PP-191).

**Battle resolution (PP-476):**
Both sides apply their own degree result independently.
Margin = (own net − opponent net) if positive; 0 if own net ≤ opponent net.
Margin 0: no outcome for that side.
Margin 1 to Ob−1: Discipline −2 on opponent unit.
Margin = Ob: Discipline −4 on opponent unit.
Margin > Ob: opponent unit destroyed.
Draw (equal net): no degree for either side; both Discipline −1.

### MODE A — Isolation

**A1. Attack probability matrix (Attacker Military vs Defender Military)**
BG Battle: Attacker pool = Military dice, TN 7. Ob = defender Military ÷ 2 (round up).

| Att Mil | Def Mil | Ob | E(att net) | P(att win) | P(draw) | P(def win) |
|---------|---------|-----|------------|------------|---------|------------|
| 4 | 2 | 1 | 1.60 | ~85% | ~8% | ~7% |
| 4 | 4 | 2 | 1.60 | ~56% | ~20% | ~24% |
| 4 | 6 | 3 | 1.60 | ~27% | ~22% | ~51% |
| 6 | 4 | 2 | 2.40 | ~80% | ~10% | ~10% |
| 3 | 4 | 2 | 1.20 | ~40% | ~22% | ~38% |
| 6 | 6 | 3 | 2.40 | ~57% | ~17% | ~26% |

Approximated: P(≥Ob net) via trinomial (P(7-9)=0.30, P(10)=0.10, P(1)=0.10).

**A2. Fort Level impact (defender adds Fort dice to Military pool)**

| Fort Level | Effective Def Pool (Mil=4) | Shift in P(def win) |
|------------|--------------------------|---------------------|
| 0 | 4D | baseline |
| 1 | 5D | +~8% |
| 2 | 6D | +~16% |
| 3 | 7D | +~22% |
| 4 | 8D | +~27% |

Fort 3 (Ehrenfeld T14, Lowenskyst T3) makes a Military 4 defender functionally equivalent
to Military 7 vs a Military 4 attacker. This is the correct design: fortresses are
near-impenetrable to symmetrically matched forces.

**A3. Battle and terrain multiplier — no terrain modifiers exist in BG.**
BG battle abstracts terrain entirely. Fort Level is the only geographic modifier.
Open-field vs fortified is mechanically represented; hill/river/forest is not.
This is a design choice — BG operates at strategic not tactical scale.

**[FINDING INV-A-01 — P2]:** No terrain modifier in BG means T6 Stillhelm
(described as "difficult frontier terrain") has no mechanical expression in BG Battle
beyond its Fort 0 (no fort bonus). The "+1 Ob non-Thread" modifier on T6 applies to
non-Thread Domain Actions (Govern, Trade), not to Battle. A fort-0 territory with
difficult terrain is indistinguishable from any other fort-0 territory in BG Battle.
Acceptable at BG abstraction level — flag as deliberate design gap.

### MODE D — Edge Cases

**D1. March into Church-held territory (TC 75 seizure phase):**
Post-TC 75, Church is in territorial seizure mode. If Crown Marches into T9 Himmelenger:
Battle fires. Church also has Seizure action this season. Both resolve in Priority 2 (Military).
Per within-tier resolution: descending Stability order. Church Stability 5 > Crown Stability 4.
Church resolves first: Seizure fires. Seizure is a Domain Action (Priority 3). But wait —
TC 75 Seizure is listed under Special/Unique Powers (Priority 6). The Battle (Crown March)
fires at Priority 2. The Seizure fires at Priority 6. Crown's Battle fires first.
If Crown wins Battle: Crown controls T9. Church Seizure in Phase 6 targets a Crown territory.
Church must then declare fresh Seizure against Crown-held T9 (new Mandate check).
This is correct sequence but the interaction of same-season Battle + Seizure on the same
territory is not explicitly ruled.

**D2. [FINDING INV-D-02 — P1]:** Multi-faction Battle in single territory:
If Crown and Varfell both declare March into T9 (Himmelenger, Church-held) in the same
season, Phase 4 Priority 2 fires. Both have Legionary cards played. Per within-tier ordering:
descending Stability. Crown Stability 4 = Varfell Stability 4: simultaneous resolution.
But who fights whom? Are there two sequential Battles (Crown vs Church, then Varfell vs
winner), or one three-way Battle? Three-way Battle rules do not exist in any fetched doc.
The simultaneous resolution rule only addresses two-faction simultaneous cases.

**D3. [FINDING INV-D-03 — P2]:** Discipline loss tracking in BG:
PP-476 applies Discipline −2 or −4 from Battle margin results. But BG unit tokens have
Discipline as a stat. Does Discipline loss in BG persist across seasons (permanent attrition)
or reset at Accounting? The BG Discipline track from mass_battle_v3.md is designed for TTRPG
multi-turn battles. In BG single-resolution battles: Discipline is checked for Morale (Rout)
but whether it carries over is unspecified.

**D4. Battle and Löwenritter garrison sharing:**
T14 Ehrenfeld has "Löwenritter garrison" (per territory table). Pre-coup: Löwenritter is an
NPC sub-faction of Crown. If a faction Marches into T14, does the garrison add to Crown's
defensive Military pool? Or does it fight separately? No joint-defence rule exists.

**D5. [FINDING INV-D-05 — P2]:** Schoenland invasion route (T1 sea connection):
T16 Schoenland has only one connection: T1 Valorsplatz (sea). If Schoenland becomes hostile
(IP ≥ 75, Altonian Vanguard deploys via Schoenland), the Vanguard enters through T1. But
the Altonian Vanguard stats are not defined in any fetched doc (CLOCK-EDIT-01 editorial still
open). The invasion path exists but the invading force is undefined.

### MODE J — Cognitive Load

**J1.** Battle resolution (PP-476 both-sides degree table) is non-standard vs the rest of
the game. All other actions use "attacker's degree determines outcome." Battle uses a
comparative margin system. Reference card essential.

**J2. [FINDING INV-J-02 — P2]:** Multi-step BG Battle checklist missing:
Step 1 (CB/Ob check) → Step 2 (Roll both pools) → Step 3 (Compare margins) →
Step 4 (Apply Discipline loss) → Step 5 (Check Rout) → Step 6 (Territory transfer) →
Step 7 (Military −1 accounting). No unified checklist. Table will miss steps.

### MODE L — Precedent

**L1.** BG Battle uses both-sides roll (PP-476). This is unique in the game — all other
actions are single-pool rolls. Players will mistakenly apply the single-pool degree table.

**L2. [FINDING INV-L-02 — P2]:** Battle Ob formula (PP-499) = defender Military ÷ 2 (round up).
This means Military 1 defender → Ob 1. An eliminated/vestigial faction (Military 1) is
actually attackable — it has non-zero resistance. Correct and intended, but the edge case
of Military 0 (Restoration Movement) is explicitly handled by PP-039: "Military 0 makes
Muster invalid." Does Military 0 make defending against Battle invalid? PP-499 min 1 Ob
means even Military 0 defender rolls 1 Ob worth of resistance. But PP-039 says "no units,
cannot field new military units." With no units, what rolls? Undefined.

---

## ═══════════════════════════════════════════════════════
## MECHANIC 3: SEIZING TERRITORY (CHURCH GRADUATED + TC 75)
## ═══════════════════════════════════════════════════════

Substantively tested in SIM-GS-01. Key open findings carried forward:

**Open P1 from SIM-GS-01:**
- D5: Pre-TC 75 availability ambiguous
- D7: PP-421 vs PP-494 Overwhelming CV cap conflict
- J3 / ED-355: Fort Level absent from PP-494 Ob formula
- L2: CB undefined (now addressed in CB section above)
- L5: Battle trigger on success unspecified

**NEW FINDINGS from cross-system analysis:**

**[FINDING SEI-D-01 — P1]:** Church Seizure pool (Influence + floor(TC/15)) at TC=28
yields 7D. Ob = 7 − CV. Against a CV=3 territory (Ob=4): P(Success) ≈ 19%. Against CV=5
(Ob=2): P(Success) ≈ 88%. The pre-TC 75 question (D5 from SIM-GS-01) is critical: if
Graduated Seizure fires at TC=28, Church can seize CV=5 Himmelenger at 88% success rate
in Season 1. This would be a game-breaking early action. Confirms the pre-TC 75 gate is
REQUIRED and must be stated explicitly.

**[FINDING SEI-D-02 — P2]:** Seizure limits: "One seizure attempt per season. Cannot
target T15 or T16." Schoenland (T16) exclusion makes sense (not in territorial play).
T15 (Askeheim) exclusion is correct (cannot be controlled). But "one seizure attempt per
season" — does this mean one Graduated Seizure OR one total seizure (including PP-421
standard seizure)? Are these two different actions or one action with two variants? Undefined.

---

## ═══════════════════════════════════════════════════════
## MECHANIC 4: CLAIMING TERRITORY (UNCONTROLLED ENTRY)
## ═══════════════════════════════════════════════════════

### Spec (from params_board_game.md PP-500)

Political Vacuum (post-elimination): 1 season duration. No March in during Vacuum.
After Vacuum: territory becomes Uncontrolled. Any faction may March in freely (no Battle,
no defender). Fort level retained.

T15 Askeheim: "Not a normal territory — cannot be controlled by any faction through
standard mechanics."

### MODE A — Isolation

**A1. Claiming Uncontrolled territory:**
No roll required. March (Legionary Outward card) → control transferred immediately.
No defender = no Battle. No Ob. The action is free (costs the Legionary card for the season).

**A2. Claiming from Political Vacuum:**
Timing: Vacuum lifts at Accounting. Control transfers at next Phase 4 Legionary action.
So if Faction A is eliminated at Accounting step 1, their territories enter Vacuum.
Vacuum lasts 1 Accounting cycle. At the *following* Accounting: Vacuum lifts and territories
become Uncontrolled. Factions may March in at Phase 4 of *that* season.

**A3. Claiming T15 Askeheim:**
Not claimable. Warden domain. Any Legionary card played toward T15 fails without
stated resolution. What happens if a player tries? Rule is silent on the consequence —
does the Legionary card get wasted, or is the attempt illegal (card returned)?

**[FINDING CLM-A-01 — P2]:** Askeheim March attempt resolution undefined. A player
might accidentally play a Legionary card toward T15. The card should be returned (illegal
play, not wasted) but no rule states this.

### MODE D — Edge Cases

**D1. Race condition — multiple factions claim same Uncontrolled territory:**
Two factions play Legionary Outward targeting same Uncontrolled territory in same season.
Within-tier resolution: descending Stability. First faction to resolve claims it. Second
faction's March now targets a controlled territory — Battle fires. But the second faction
declared March into an *uncontrolled* territory. Does the declaration of intent lock target
as "uncontrolled at declaration time" (March proceeds as claim, no Battle) or "controlled
at resolution time" (Battle fires)?

**[FINDING CLM-D-01 — P1]:** Race condition on Uncontrolled territory claim is unresolved.
This will occur every time multiple factions compete for a vacated territory (after elimination
or during early expansion). Critical ruling needed.

**D2. Claiming Askeheim via Expedition vs standard March:**
Expedition procedure (PP-219) provides access to T15 for Warden-related actions. Expedition
success does NOT grant control. Standard March is explicitly blocked. There is no mechanism
for any faction to place a control token in T15. Varfell Path B requires "control T4 AND T13"
not T15. Correct as designed.

**D3. [FINDING CLM-D-03 — P2]:** Claiming creates a timing gap:
If territory X enters Vacuum at Accounting step 1, and all factions immediately plan March
into X, the Vacuum prevents entry for 1 full season. This means the territory is "locked"
for one season of planning without access. Some factions (those adjacent to X) will race
on the next Phase 4. Others (non-adjacent) cannot reach in one season. Non-adjacent
factions are structurally excluded from claiming vacated territories unless adjacency is
established within the Vacuum season. This seems intentional (adjacency matters) but no
rule explicitly confirms it.

### MODE J — Cognitive Load

**J1.** Claiming Uncontrolled is the simplest territory action — Legionary card, no roll.
Vacuum timing is the only complex element. Acceptable at 2/10 load.

**J2.** Vacuum end timing vs March timing: Vacuum lifts AT Accounting. Phase 4 is before
Accounting in the season sequence. So Vacuum ends at Accounting of Season N; Phase 4 of
Season N+1 is when claim occurs. Players will forget that the Accounting in which Vacuum
ends is NOT the Phase in which they can claim. Clear on a checklist; confusing in play.

---

## ═══════════════════════════════════════════════════════
## MECHANIC 5: CONCEDING TERRITORY
## ═══════════════════════════════════════════════════════

### Spec

**GAP: No definition in any fetched canonical document.**

Conceding territory does not appear in params_board_game.md, bg_v05, or geography_design.md
as a defined action. The concept appears implicitly in:
- Total Domination path: factions at Stability 0 may "formally Submit" (territorial surrender).
- Submission mechanic (PP-475): Submitted faction's territories come under Total Domination
  faction control, but as a faction-level surrender, not territory-by-territory concession.
- Diplomatic pledge language (bg_v05 §Treaty Betrayal): implies territorial pledges exist
  but doesn't define how control actually transfers from pledge fulfillment.

**[FINDING CON-A-01 — P1]:** Voluntary unilateral territory concession has no mechanic.
A faction that wants to hand over a territory to an ally (without battle) has no procedure.
This is a significant gap: diplomatic settlements, strategic retreats, and negotiated transfers
all require a mechanic that does not exist.

**[FINDING CON-A-02 — P1]:** Forced concession (post-Battle defeat) is also ambiguous.
PP-476 Battle outcome: "Attacker wins → Territory captured." Does the defending faction's
military unit get destroyed? Does it retreat to an adjacent friendly territory? Or is it
simply removed from the board? No retreat mechanic exists in BG (it exists in TTRPG mass
battle as Rout/Pursuit). This means the tactical aftermath of losing a territory in BG is
unspecified beyond "Territory captured; Defender Military −1."

**[FINDING CON-A-03 — P2]:** PP-476 says "Attacker wins → Territory captured; Defender
Military −1." Does the defender's unit remain in the territory (now under attacker control)
as a captive/masterless unit? Or does it disappear? Per PP-224 (implicit from bg_v05):
"P-24: On faction elimination, units remain on board until Muster order removes them
(holding ground, now Masterless)." This ruling is for *elimination*, not for territory
loss. For non-elimination territory loss, unit disposition is undefined.

### MODE D — Edge Cases

**D1. Strategic withdrawal vs forced concession:**
A player who wants to pull units from a territory before a superior force arrives has no
explicit mechanic. The column formation ("movement only" — TTRPG) has no BG equivalent.
Voluntary withdrawal before Battle fires is undefined.

**D2. [FINDING CON-D-02 — P2]:** If Crown voluntarily offers T5 Feldmark to Hafenmark
as a diplomatic gesture (Pledge), what is the procedure? There's no "Transfer Territory"
action. A Formal Crown Treaty (Senator Outward, Ob = target Mandate) is the closest
analogue, but its resolution conditions are "both factions must agree" — it doesn't specify
that territory transfers as part of a Treaty. It's a relationship-building action, not a
conveyance action.

---

## ═══════════════════════════════════════════════════════
## MECHANIC 6: TRADING TERRITORY (DIPLOMATIC TRANSFER)
## ═══════════════════════════════════════════════════════

### Spec

**GAP: No definition in any fetched canonical document.**

Territory trading (faction A gives territory X to faction B in exchange for territory Y or
resources) is implied by the Diplomatic pledge system but never defined procedurally.

**[FINDING TRA-A-01 — P1]:** No Territory Trade action exists. Diplomatic actions
(Senator card) can build relationship and create Pledges, but no Pledge fulfillment mechanic
transfers territorial control. If two players agree to swap T4 (Grauwald, Varfell) for T7
(Rendstad, Hafenmark), they have no mechanic to execute this.

**[FINDING TRA-A-02 — P2]:** "Between players: Negotiated — Not a roll" (from Standard
Action Ob Reference). This suggests player-to-player diplomacy is freeform. But if it's
freeform with no mechanic, how does the negotiated outcome (territory transfer) actually
execute on the board? Is it simply: both players move tokens by mutual agreement? If so:
- What prevents either party reneging?
- Does this consume a card play?
- Does it affect any clocks (TC, RS, PI)?

**[FINDING TRA-A-03 — P2]:** Territory trade would interact with:
- TCV totals (both factions' TCV changes; victory conditions may be instantly met or broken)
- Fort levels (physical fortifications transfer with the territory)
- Ministry AP-tokens (do they follow the territory to new control, or stay as residual presence?)
- Church Prominence (if traded territory has Church CV, prominence calculation changes)
None of these interactions are specified for a trade scenario.

### MODE L — Precedent

**L1.** The Hafenmark+RM co-victory and Crown+Hafenmark co-victory both require territorial
thresholds. Territory trading between co-victory partners could instantly manufacture a
co-victory. Without a CB or cooldown on traded territory TCV counting toward victory,
a single negotiated trade (e.g., Crown gives Varfell two TCV-1 territories, Varfell gives
Crown one TCV-5 territory) could be exploited to reach victory threshold in one action.
A "traded territory cannot count toward victory for 1 season" rule would prevent this.

---

## ═══════════════════════════════════════════════════════
## MECHANIC 7: DEVELOPING TERRITORY (GOVERN + FORTIFY)
## ═══════════════════════════════════════════════════════

### Spec (from params_board_game.md)

**Govern (Consul Inward):** Ob = Prosperity ÷ 2 (round up, min 1). −1 Ob in own capital.
Success: Prosperity +1 in territory (up to 5). Fail: Prosperity −1.

**Fortify:** Pool = Military (PROV: ED-338). Ob = Fort Level + 1.
No degree table specified beyond "success/failure."

**Parish/Cathedral (Church, ED-319):** 2 sequential Consul Inward successes + 1 Wealth =
Parish (CV floor 1). 5 total + 2 Wealth = Cathedral (CV floor 2 + Prominence boost).

### MODE A — Isolation

**A1. Govern probability matrix (Consul Inward, Influence as pool)**

| Prosperity | Ob | Pool=4 P(Suc) | Pool=4 P(Fail) | Pool=6 P(Suc) |
|------------|-----|---------------|----------------|---------------|
| 1 | 1 | ~85% | ~15% | ~95% |
| 2 | 1 | ~85% | ~15% | ~95% |
| 3 | 2 | ~56% | ~44% | ~80% |
| 4 | 2 | ~56% | ~44% | ~80% |
| 5 | 3 | ~27% | ~73% | ~57% |

Note: Govern uses Consul card (not Influence directly). The pool is the faction's relevant
stat for Consul Inward. Faction mechanic uses "roll faction stat pool." For Govern: the
acting stat is not explicitly stated for BG Domain Actions. Ob formula is clear; pool stat
is not.

**[FINDING DEV-A-01 — P2]:** Govern pool stat undefined for BG.
The Standard Action Ob Reference states Ob only. It does not state which faction stat is
rolled as the dice pool for each action type. Most Domain Actions imply the relevant stat:
Military for Legionary, Influence for Senator/Tribune, Wealth for Trade. Govern (Consul
Inward) logically uses Influence (administrative capacity) or Mandate (political authority).
No explicit rule states which.

**A2. Fortify probability matrix**

Fortify pool = Military (PROV: ED-338). Ob = Fort Level + 1.

| Current Fort | Next Level | Ob | Pool=4 P(Suc) | Pool=6 P(Suc) |
|-------------|------------|-----|---------------|---------------|
| 0 | 1 | 1 | ~85% | ~95% |
| 1 | 2 | 2 | ~56% | ~80% |
| 2 | 3 | 3 | ~27% | ~57% |
| 3 | 4 (if max 4) | 4 | ~8% | ~27% |
| Max (no 4) | — | — | Cannot fortify | — |

Fort max 4 applies to T3 Lowenskyst and T14 Ehrenfeld only. All other territories: Fort
max is not stated. Implied max = 4 (by analogy), but not explicit.

**[FINDING DEV-A-02 — P2]:** Fort maximum for non-capped territories is undefined.
T3 and T14 have explicit "max 4" notation. Other territories (e.g., T9 Himmelenger, Fort 2)
have no maximum stated. Can Church fortify Himmelenger to Fort 5, 6, 7? Unclear.

**A3. Prosperity effect on Trade Ob:**
Trade (Consul Outward) Ob = Prosperity ÷ 3 (round up, min 1). At Prosperity 5: Ob = 2.
At Prosperity 1: Ob = 1. Developing Prosperity primarily benefits Trade reliability,
not Govern reliability. Govern Ob grows with Prosperity (harder to govern prosperous
territories). This is a natural tension: develop territory and it becomes harder to
maintain governance. Correct design.

**A4. Church Parish/Cathedral — probability sequence:**

Sequence: 5 successful Consul Inward + 3 Wealth total, over multiple seasons.

At Influence 6, Ob = Prosperity ÷ 2 (round up):
- T9 Himmelenger, Prosperity 5: Ob = 3. P(Suc) ≈ 57%/season.
- Expected seasons to 5 consecutive successes: 5 ÷ 0.57 ≈ 8.8 seasons average (non-consecutive requirement)
- Actually: 5 sequential successes (not consecutive); Church can retry each season.
- P(all 5 succeed) = 0.57^5 ≈ 6% if taken serially in any 5-season stretch without failure.
  But each is independent: expected number of successes in 10 seasons: 5.7. Reaching 5
  cumulative over 10 seasons: binomial(10, 0.57), P(≥5) ≈ 68%.
- Cathedral is achievable in a 10–15 season game. Calibrated correctly.

**[FINDING DEV-A-03 — P2]:** Parish/Cathedral Ob uses Prosperity ÷ 2 (same as Govern).
But the Parish rule (ED-319) says "Church Consul Inward action." It doesn't specify the Ob
explicitly — only that it's a Consul Inward. Is Parish using Govern Ob (Prosperity ÷ 2)
or a separate Ob? Implicit from "Consul Inward" = Govern Ob. Needs explicit confirmation.

### MODE D — Edge Cases

**D1. [FINDING DEV-D-01 — P1]:** Govern on territory changing control this same Phase 4:
If Crown plays Consul Inward (Govern) in T5 in Priority 3, and Varfell wins Battle against
Crown for T5 in Priority 2 (which fires first), Crown's Govern card plays in a territory
it no longer controls. Does the Govern action:
(a) Resolve normally (Prosperity still benefits the new controller),
(b) Fail (Crown no longer has standing),
(c) Carry over to Crown's next season in any territory?
Priority 2 (Military/Battle) fires before Priority 3 (Domain). So at the time Govern
resolves, the territory has already changed hands. Option (b) seems correct but is not stated.

**D2. Fortify on territory lost in Battle same season:**
Same problem as D1. Fortify (Priority 3 or 6 PROV) fires after Battle (Priority 2).
If territory is lost, Fortify action is moot. If Fortify was Overwhelming (fort upgraded),
does the upgraded fort now serve the capturing faction? Physical fortifications don't
vanish — PP-500 confirms "Fort level retained" on Political Vacuum. By analogy, a fort
built by the losing faction this season should remain. But the Fortify action resolution
firing after a Battle loss is undefined.

**D3. [FINDING DEV-D-03 — P2]:** Govern and Church Piety Spread both use Consul Inward.
Church can use Piety Spread (PP-428, Consul Inward Church-only) OR standard Govern in the
same territory. They're both Consul Inward — can Church play both in one season? One card
play = one Consul Inward. Church starts with one Consul card. Church cannot play both
Piety Spread and Govern in the same territory in the same season without a second Consul card.
This is correct but the constraint needs to be explicit: Piety Spread and Govern are
mutually exclusive in a given season (one Consul card).

**D4. [FINDING DEV-D-04 — P2]:** Govern success: "Prosperity +1 in territory." What stat
is Prosperity for the purpose of Govern Ob? The Ob formula uses the territory's Prosperity
track (0–5). But "Prosperity ÷ 2 round up, min 1" means:
- Prosperity 0: Ob 1. (Governing abandoned land is easy.)
- Prosperity 5: Ob 3. (Governing thriving land is harder — bureaucracy, expectations.)
This inversion (higher Prosperity = harder Govern) is counterintuitive. Most players will
expect governing a developed territory to be easier. The design rationale (managing high
expectations) is sound but should be stated explicitly on the reference card.

### MODE L — Cross-System

**L1.** Prosperity feeds Trade Ob, Govern Ob, Govern outcome, and Year-End Accounting
Wealth generation. It is the most connected territory stat. Loss of Prosperity from failed
Govern has cascading effects: lower Trade income, easier (but pointless) future Govern.
A faction that repeatedly fails Govern enters a self-perpetuating low-Prosperity state.
This is correct design — administrative neglect degrades a territory's productivity.

**L2. [FINDING DEV-L-02 — P2]:** Prosperity on contested vs controlled territory:
"Govern success: Prosperity +1 in territory" — is this valid for contested territories?
If Crown controls T5 but Varfell has a military unit present (contested, not lost), Crown
can still play Consul Inward. The territory hasn't changed hands. But governing while under
military pressure seems unrealistic. No penalty for contested-territory Govern exists. The
only relevant modifier is "−1 Ob in own capital" (bonus for own capital, not penalty for
contested territory). Suggest: +1 Ob to Govern in contested territory (military unit of
non-controlling faction present).

---

## ═══════════════════════════════════════════════════════
## CONSOLIDATED FINDINGS REGISTER
## ═══════════════════════════════════════════════════════

| ID | Sev | Mechanic | Description | Action |
|----|-----|----------|-------------|--------|
| CB-A-01 | P1 | Casus Belli | CB effect undefined — no mechanic for what CB does | Patch required |
| CB-A-02 | P1 | Casus Belli | CB expiration inconsistent — no unified table | Patch required |
| CB-D-02 | P1 | Casus Belli | CB gate vs bonus model undefined — is CB a war declaration requirement? | ED required |
| CB-L-03 | P1 | Casus Belli | CB stacking from repeated Seizure attempts — no cap stated | Patch required |
| CON-A-01 | P1 | Conceding | No voluntary territory concession mechanic exists | Patch required |
| CON-A-02 | P1 | Conceding | Defending unit disposition after Battle loss undefined | Patch required |
| TRA-A-01 | P1 | Trading | No Territory Trade action exists | Patch required |
| CLM-D-01 | P1 | Claiming | Race condition on Uncontrolled territory claim unresolved | Patch required |
| INV-D-02 | P1 | Invading | Three-way Battle (2 attackers vs 1 defender) undefined | ED required |
| DEV-D-01 | P1 | Developing | Govern on territory lost in Battle same season undefined | Patch required |
| SEI-D-01 | P1 | Seizing | Pre-TC 75 Graduated Seizure gate must be explicit (carries from SIM-GS-01) | Patch required |
| D7-SIM-GS | P1 | Seizing | PP-421 vs PP-494 OW CV cap conflict (carries from SIM-GS-01) | Patch required |
| J3-SIM-GS | P1 | Seizing | Fort Level absent from PP-494 (carries from SIM-GS-01 ED-355) | Patch required |
| L5-SIM-GS | P1 | Seizing | Battle trigger on Graduated Seizure success unspecified | Patch required |
| CB-D-03 | P2 | Casus Belli | CB persistence through faction elimination undefined | ED required |
| CB-D-05 | P2 | Casus Belli | CB vs Diplomatic Token interaction undefined | ED required |
| CB-J-01 | P2 | Casus Belli | No centralized CB section — scattered across 4+ docs | Infrastructure |
| INV-A-01 | P2 | Invading | T6 Stillhelm terrain modifier has no BG expression | Design note |
| INV-D-03 | P2 | Invading | BG Discipline loss persistence across seasons undefined | Patch required |
| INV-D-05 | P2 | Invading | Altonian Vanguard stats undefined (CLOCK-EDIT-01 open) | ED required |
| INV-J-02 | P2 | Invading | BG Battle resolution checklist missing | Infrastructure |
| INV-L-02 | P2 | Invading | Military 0 defender (Restoration) vs Battle Ob resolution | Patch required |
| CLM-A-01 | P2 | Claiming | Askeheim March attempt resolution undefined | Patch required |
| CLM-D-03 | P2 | Claiming | Non-adjacent faction exclusion from Vacuum territory is unconfirmed | Design note |
| CON-A-03 | P2 | Conceding | Post-Battle unit disposition: P-24 only covers elimination, not territory loss | Patch required |
| CON-D-02 | P2 | Conceding | Diplomatic territory pledge fulfillment has no execution mechanic | ED required |
| TRA-A-02 | P2 | Trading | Freeform diplomacy has no enforcement/execution mechanic | ED required |
| TRA-A-03 | P2 | Trading | Territory trade interaction with TCV, Fort, Ministry, Church undefined | ED required |
| DEV-A-01 | P2 | Developing | Govern pool stat undefined for BG | Patch required |
| DEV-A-02 | P2 | Developing | Fort maximum for non-capped territories undefined | Patch required |
| DEV-A-03 | P2 | Developing | Parish Ob formula confirmation needed | Patch required |
| DEV-D-03 | P2 | Developing | Piety Spread vs Govern mutual exclusion not explicit | Note |
| DEV-D-04 | P2 | Developing | Govern Ob inversion (high Prosperity = harder) should be explicit on ref card | Infrastructure |
| DEV-L-02 | P2 | Developing | No penalty for Govern in contested (non-lost) territory | Patch required |
| SEI-D-02 | P2 | Seizing | Standard vs Graduated Seizure — one-per-season cap scope | Patch required |
| L6-SIM-GS | P2 | Seizing | Mandatory Assert post-TC 75 action economy waste | ED required |

**P1 total: 14 | P2 total: 22**

---

## WHAT IS WORKING

- BG Battle probability matrix is well-calibrated. Fort levels create meaningful asymmetry.
- Govern/Prosperity loop creates natural territory development tension (Ob rises with Prosperity).
- Parish/Cathedral system is achievable over a 10–15 season campaign — correctly paced.
- Uncontrolled territory claim is clean and fast (no roll, one card).
- CB acquisition sources are consistently distributed (treaty, aggression, fabrication, seizure).
- Political Vacuum (PP-500) is a sound one-season buffer that creates brief diplomatic windows.
- Fortify probability curve (Ob = Fort+1 against Military pool) produces diminishing returns
  at high fort levels — correct design: upgrading Fort 3 to 4 is a rare, committed action.

---

## SIMULATION COMPLETE — READY FOR AUDIT + PATCH
