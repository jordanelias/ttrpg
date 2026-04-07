# Victory Architecture v1 — Critical Review
## Scope: BG mode + Hybrid mode mechanical consistency, design intent, balance
## Reviewer: Claude (Opus)
## Date: 2026-04-06
## Files reviewed: victory_architecture_v1.md, opus_design_proposal.md, params_board_game.md, params_factions.md, state_transfer_spec.md, bg_v05_simulation_and_patches.md, geography_design.md, canon_constraints.md, philosophical_foundations.md

---

## SEVERITY KEY
- **BLOCKER:** Cannot ship. Mechanical contradiction or missing specification that prevents play.
- **HIGH:** Serious design concern. Playable but produces unintended outcomes or degenerate strategies.
- **MEDIUM:** Design tension. Functional but should be addressed before calibration.
- **LOW:** Minor inconsistency or documentation gap.

---

## A. HYBRID MODE — STATE TRANSFER GAPS

### A-01 [BLOCKER] — CV has no state transfer specification

The state_transfer_spec.md defines every variable that crosses mode boundaries. CV is a new per-territory stat (0–5, 15 territories) that does not appear anywhere in the spec. The following hybrid transitions are undefined:

1. **TTRPG Zoom In → CV effect:** A PC preaches, debates faith, performs a Thread operation that alters local conviction, or conducts Community Weaving during a personal scene. How does this propagate to the CV track? Is it a Domain Echo (queued to Accounting)? Immediate? Does a single personal-scale sermon move a territory-wide population stat?

2. **BG CV change → TTRPG consequence:** If CV drops from 3 to 2 in a territory between sessions, does the TTRPG GM need to narrate changing popular mood? Is there a scene trigger?

3. **Calamity Drift during Zoom In:** If RS drops below 50 during a TTRPG scene, Calamity Drift fires at the next Accounting and changes CV in adjacent territories. But Accounting is suspended during Zoom In (per state_transfer_spec §1). Does Calamity Drift queue, or is it skipped for that season?

**Recommendation:** Add CV to state_transfer_spec §1 (BG → TTRPG), §Zoom Out (TTRPG → BG), and §4 (BG intra-turn transitions). Proposed rule: CV changes from TTRPG personal scenes queue as Domain Echoes (±1 CV cap per Zoom In, fires at Accounting). Calamity Drift fires at Accounting regardless of Zoom In suspension — it is a global environmental effect, not a player action.

### A-02 [BLOCKER] — TC Win-Delay Rule references obsolete threshold

state_transfer_spec §TC Win-Delay Rule: "TC ≥ 65 = Church win fires at Accounting regardless of active Zoom In suspension."

The victory architecture changes Church victory from TC ≥ 65 to TC 75 phase transition → TCV ≥ 18 held for 2 consecutive seasons. The Win-Delay Rule is now mechanically wrong:

- TC 75 no longer equals victory — it equals phase transition to seizure mode.
- Victory is TCV ≥ 18 with all held territories CV ≥ 3, checked at Accounting Step 12.
- The 2-season holding requirement means victory cannot fire instantaneously at a threshold crossing.

**Recommendation:** Rewrite the Win-Delay Rule: "Victory condition checks (all factions) fire at Accounting Step 12 regardless of active Zoom In. A Zoom In cannot delay or prevent a victory declaration. The 2-season holding requirement is assessed across consecutive Accounting steps."

### A-03 [HIGH] — Hybrid victory (P-32) not addressed

P-32 states: "Hybrid victory = BG victory PLUS personal arc resolution. A BG-only win with unresolved personal arc = Hollow Victory (valid but narratively incomplete)."

The victory architecture does not mention Hybrid victory at all. All victory conditions are BG-layer (TCV, CV, faction stats). Questions:

1. Does P-32 still apply? If so, what counts as "personal arc resolution"? The old Hollow Victory modifier table (params_board_game §Hollow Victory) references Deed counts, PC Belief arc contradictions, and Uphold/Compromise patterns. With Deeds dissolved, most of the Hollow Victory modifier table is invalid.

2. The victory architecture redefines "Hollow Victory" as specifically the Church+Hafenmark partition (ED-304). This conflicts with P-32's definition of Hollow Victory as any BG win without personal arc resolution. Two meanings for the same term.

**Recommendation:** Rename the Church+Hafenmark partition to "Partition Victory" or "Negotiated Peace" to avoid collision with P-32's Hollow Victory concept. Separately, redesign the Hybrid Hollow Victory modifier table to reference the new victory system (TCV-based conditions, CV alignment, RS at declaration) rather than Deed counts.

### A-04 [MEDIUM] — Domain Echo redesign (ED-300) not integrated

ED-300 resolves Domain Echo as scene-availability declaration (scenes available for player engagement, with escalation clock; uninvestigated echoes resolve autonomously). This was marked resolved but propagation is pending.

The victory architecture implicitly assumes the old Domain Echo model (events that fire and queue to Accounting). If ED-300's autonomous resolution mechanic is canonical, then:

- An uninvestigated echo could autonomously change territory control, which changes TCV, which could trigger or break a victory condition.
- The 2-season holding requirement could be disrupted by an autonomous echo in the intervening season.
- This creates a scenario where a faction's victory is nullified by an event no player chose to engage with. This may be intended (the world moves whether or not players attend to it) but it needs explicit design acknowledgment.

**Recommendation:** Add a note in victory_architecture: "Autonomous domain echo resolution that changes territory control is assessed at Accounting. TCV changes from autonomous resolution count toward or against victory conditions. The 2-season holding requirement does not exempt autonomous changes."

---

## B. BOARD GAME MODE — MECHANICAL CONFLICTS

### B-01 [BLOCKER] — params_board_game still contains full Deed system

params_board_game.md §Victory Conditions lists the complete Deed-based victory system (Crown 5 Deeds, Church 4 Deeds, Hafenmark 3 Paths with Deeds, Varfell 3 Paths with Deeds). canonical_sources.yaml now lists victory_architecture_v1.md as canonical for "victory," but params_board_game.md is still canonical for board game mode broadly.

A player or GM reading params_board_game will encounter two incompatible victory systems. The Deed system references mechanics (Deed Tokens, Deed counts, Deed-based Hollow Victory modifiers) that have been dissolved.

**Recommendation:** Propagation pass required. Replace params_board_game §Victory Conditions with a pointer to victory_architecture_v1.md. Remove the Hollow Victory modifier table. Remove all Deed Token references. This is a large edit — flag for dedicated propagation session.

### B-02 [HIGH] — Reformed Settlement references Deed Tokens

The Reformed Settlement mechanic (bg_v05 Cascade Test 2, params_board_game §TC Increases/Decreases) awards "Hafenmark gains Deed" on Church Resist. With Deeds dissolved, what does Reformed Settlement award?

Additionally, the old Hafenmark Path A required "Reformed Settlement completed" as a Deed. The new Hafenmark Reformed Sovereignty has no Reformed Settlement condition. Is Reformed Settlement still a mechanic? If so, what does it do now?

**Recommendation:** Reformed Settlement should award a tangible benefit under the new system. Proposal: Reformed Settlement success (Church Resists) = Hafenmark gains +1 TCV effective bonus in the Reformed Settlement territory for victory calculation purposes (symbolic authority gain). Or: Reformed Settlement is dissolved as a mechanic — the CV track now handles ideological shifts that Reformed Settlement was trying to represent. Requires [EDITORIAL] decision.

### B-03 [HIGH] — Hollow Victory modifier table is orphaned

The Hollow Victory modifier table (params_board_game §Hollow Victory v04 B12) references:
- "Compromised Institutional Mandate: −0.5 Deeds per Compromise"
- "RS < 30 at victory: −1 Deed"
- "IP > 60 at victory: −1 Deed"
- "Torben Loyalty ≤ 1: −1 Deed"
- "PC Belief arc contradicted: −1 Deed per season"

All of these subtract from Deed counts. Deeds no longer exist for Crown/Church/Hafenmark/Varfell. The table is mechanically dead but still present in params_board_game.

Löwenritter retains Deeds. Does the Hollow Victory modifier still apply to Löwenritter? If so, Löwenritter is the only faction subject to this modifier — creating asymmetry.

**Recommendation:** If the Hollow Victory modifier concept survives (P-32 still implies it should for Hybrid mode), redesign it as a universal "Victory Integrity Check" that applies to the new conditions-based system. For example: RS < 30 at declaration = victory cannot be declared (the world is too damaged for any government to claim legitimacy). IP > 60 at declaration = Crown and Hafenmark victories blocked (Altonia is at the gates). These become hard gates, not Deed subtractions.

### B-04 [HIGH] — PP-404 coalition pairs misaligned with co-victory pairings

PP-404 (Missed Coalition Ob Penalty) references 4 canonical coalition pairs (PP-405):
1. Church + Hafenmark (Trade-Mandate Pact, both Influence ≥ 6)
2. Varfell + Löwenritter (Military Alliance, both Military ≥ 5)
3. Guilds + Hafenmark (Economic Bloc, both Wealth ≥ 6)
4. Restoration + Niflhel (Restoration Compact, both Influence ≥ 4)

The victory architecture co-victory pairings are:
1. Crown + Hafenmark
2. Crown + Varfell
3. Varfell + RM (latent)
4. Hafenmark + RM
5. Löwenritter + Hafenmark
6. Church + Hafenmark (Hollow/Partition)

Only one pair overlaps: Church + Hafenmark. But the PP-405 coalition is a mechanical alliance (combined actions, +1D), while the victory architecture's Church + Hafenmark is a game-ending partition. These are different things.

PP-404's penalty fires when a coalition trigger is met and not activated — but the coalition pairs are operational alliances, not victory co-wins. The two systems serve different purposes and should not be confused. However, a reader may assume co-victory pairings and coalition pairs are the same thing.

**Recommendation:** Add a clarifying note in victory_architecture: "Co-victory pairings (§4) are distinct from operational coalition pairs (PP-404/PP-405). Coalitions are in-game alliances with mechanical benefits. Co-victories are game-ending conditions. A faction may pursue a coalition without pursuing a co-victory, and vice versa."

### B-05 [MEDIUM] — Accounting Step 12 still references Deed Tokens

Accounting procedure (params_board_game §Seasonal Accounting): Step 12 reads "Victory condition check. All Deed Tokens simultaneously = declare victory."

This language is Deed-based. The new system checks simultaneous conditions held for 2 consecutive seasons.

**Recommendation:** Update Step 12: "Victory condition check. If a faction meets all conditions for any of its victory paths and has met them continuously since the previous Accounting, declare victory."

### B-06 [MEDIUM] — 2-season holding is new; pacing implications unstated

The 2-season holding requirement standardizes what was previously inconsistent (some paths had holds, some didn't). This changes game dynamics:

- A faction that meets all conditions at Accounting can be knocked out of victory position by any opponent in the intervening season. This is good (creates counterplay) but means victory requires sustained dominance, not a single peak turn.
- The earliest possible solo victory is now effectively Season 3 minimum (conditions met S1, maintained S2, declared S3). In practice, no faction can meet conditions before ~S10.
- The Partition Victory (Church + Hafenmark) doesn't specify a holding requirement. Is it instant on meeting conditions, or does it also require 2 seasons?

**Recommendation:** Confirm: Partition Victory has no holding requirement (it is a mutual agreement, not a sustained state) or it does require 2 seasons (it must be stable). State explicitly.

---

## C. BALANCE AND WIN PROBABILITY

### C-01 [HIGH] — Crown victory is easier than stated

ED-109 confirms Crown victory should be the hardest because it requires "suppressing all other factions including Altonia — eradication, surrender, or Crown-favourable treaties." But the mechanical conditions tell a different story:

**Crown starts meeting most of its victory conditions at game start:**

| Condition | Starting value | Met? |
|-----------|---------------|------|
| TCV ≥ 18 | 12 (needs +6) | No |
| Mandate ≥ 5 | 5 | **Yes** |
| TC < 50 | 28 | **Yes** |
| IP < 60 | 20 | **Yes** |
| PI ≥ 4 | 7 | **Yes** |
| CV 3–4 in ≥ 3 held territories | T5(3), T6(3), + 4 at CV 4 | **Yes** |

Crown's only unmet condition is TCV ≥ 18 (needs +6). Hafenmark also needs +6 TCV (from 8 to 14). But Crown starts with higher Mandate (5 vs 4), higher Military (4 vs 3), more territories (6 vs 4), and more TCV (12 vs 8). Crown's non-TCV conditions are maintenance tasks (keep TC/IP from rising, keep PI/Mandate from falling), while Hafenmark's include an active sabotage requirement (Crown Mandate ≤ 3).

**The asymmetry of difficulty is inverted.** Crown's conditions amount to "hold what you have and conquer +6 TCV." Hafenmark's conditions amount to "hold what you have, conquer +6 TCV, AND bring Crown Mandate from 5 down to 3."

**Recommendation:** Crown's TCV threshold should be higher (20–22) or it should require an additional active condition — e.g., "every other playable faction has Mandate ≤ 3" or "Torben Loyalty ≥ 6" (requiring active succession management) or "Warden Cooperation ≥ 1" (requiring Southernmost engagement, creating tension with TC/IP maintenance). Needs simulation to calibrate.

### C-02 [HIGH] — Crown has no CV tool; CV 3–4 band is fragile

Crown has no mechanical action that moves CV in any direction. The document says Crown "governs the centre by blocking extremes" but doesn't specify how Crown blocks:

- Crown cannot prevent Church Preach in Crown territory (Church only needs to be "prominent" — Church Mandate > Crown's local Mandate equivalent, which is not defined at per-territory granularity).
- Crown cannot prevent Varfell Cultural Reclamation (requires Varfell control or "Einhir cultural presence" — undefined for Crown territories).
- Crown cannot prevent Calamity Drift (requires RS maintenance, which Crown has no direct tool for).

If Church Preaches in T2 (Crown, CV 4 → CV 5), Crown loses its CV alignment condition there. Crown has no response action — it can only try to reduce Church Mandate via Royal Decree or Domain Action, which is an indirect and expensive counter.

**Recommendation:** Either (a) give Crown a CV action: "Royal Patronage — Crown spends Wealth in controlled territory to maintain CV at current value, blocking one CV change this season" (defensive, not directional, fits Crown's statist character), or (b) remove the CV 3–4 alignment condition from Crown's victory, replacing it with a simpler "no territory held at CV 0 or CV 5" (Crown doesn't need a specific band — it just can't allow extremes).

### C-03 [MEDIUM] — CV ±1/season cap makes starting values nearly deterministic

With 1 CV action per faction per season, and ±1 CV cap per territory per season, moving a territory's CV from 4 to 1 takes a minimum of 3 seasons of unopposed action. With opposition (Church Preaching back), it takes 6+ seasons of dedicated investment.

In a 12–20 season game, this means:
- Crown territories (CV 3–4) will stay CV 2–5 for the entire game.
- Varfell territories (CV 2) will stay CV 1–3.
- Himmelenger (CV 5) will stay CV 4–5 unless multiple factions invest against it.

**The CV starting values are the primary determinant of who can win where.** The map is ideologically partitioned at game start and barely shifts. This may be intended (reflecting the inertia of popular belief) but it compresses strategic choice: each faction can only realistically win in territories whose starting CV matches their victory band.

This creates a problem for Church: Church needs all held territories at CV ≥ 3, but seizing Varfell territories (CV 2) requires raising CV to 3 first. That takes at least 1 season per territory — and Church can only perform 1 CV action per season. Seizing 4 Varfell territories (all at CV 2) requires 4 seasons of Preaching before the seizures can proceed. This creates a minimum ~4 season lead time before Church can seize Varfell territory, during which Varfell can counter-Reclaim.

**Recommendation:** Either (a) increase the CV action frequency (2 per season, or 1 per territory per season), or (b) allow Church seizure to raise CV as part of the seizure outcome (Overwhelming seizure: CV +1 in target territory, consuming the CV cap for that territory this season). Option (b) is already partially present — the opus doc's seizure results table includes "CV +1 (if below 5)" on Overwhelming — but this should be formalized and counted against the seasonal cap.

### C-04 [MEDIUM] — Varfell stat reveal condition scales with player count

Varfell Path A requires "all other factions' stats revealed at least once." In a 2-player game, this means revealing one faction's stats. In a 5-player game, four factions'. The difficulty is variable by table size — a structural problem for equal win probability.

**Recommendation:** Fix to a constant: "at least 3 factions' stats revealed" or "at least 2 rival playable factions' stats revealed." Player-count-invariant.

### C-05 [LOW] — TCV values untested

The document flags TCV balance as SIM-DEBT P1-BLOCKER. The critique agrees: TCV thresholds (18/18/14/14/—) are unvalidated. The Gransol raise from TCV 3→4 and Spartfell raise from 1→2 both benefit Hafenmark's starting position. Whether this is correct depends on simulation.

---

## D. PHILOSOPHY COMPLIANCE

### D-01 [MEDIUM] — T15 CV hard-fix cites wrong constraint

The document justifies T15 CV permanently 0 by citing P-07. But P-07 concerns rendering frame incompatibility at Coherence 0 — it is about individual practitioners, not territorial populations.

The correct justification is P-02 (Ein Sof = infinite positive being, the unintelligible ground is fullness not void) combined with the Foundations §5.3 (threadcut beings) and §8 (Solmund as catalyst). At the Calamity epicentre, the rendering itself is compromised (Locked/Snapped/Oscillating Zones per geography_design.md). Orthodox Solmundan faith cannot be sustained where the population has direct experiential contact with the rendering failure that Solmund's emergence produced. This is not a P-07 issue (practitioner Coherence) but a P-03 issue (rendering = consciousness-performed — in a zone where rendering is structurally compromised, the consciousness-performed rendering of orthodox faith is impossible).

**Recommendation:** Change citation from "P-07" to "P-03 + Foundations §8 — rendering capacity in the Southernmost is structurally compromised; orthodox conviction cannot be sustained where the rendering of ordinary experience fails."

### D-02 [MEDIUM] — Community Weaving P-01 compliance unclear

Community Weaving is a Thread operation. Per P-01, all Thread operations must produce automatic co-movement effects across all three dimensions. The opus_design_proposal.md Community Weaving table shows RS effects but does not show all three dimensional auto-effects:

- Temporal auto-effect: Not specified. Does Community Weaving produce temporal co-movement? It should.
- Epistemic auto-effect: Not specified.
- Actual auto-effect: Not specified (the CV −1 is a designed outcome, not an auto-effect).

If Community Weaving is a Thread operation, it must draw a Co-Movement card and fire all three auto-effects per P-01 and the existing Thread operation procedure. The opus doc's table elides this.

**Recommendation:** Community Weaving fires the standard Thread operation procedure including Co-Movement card draw. The CV −1 is the intended primary effect; the co-movement auto-effects fire additionally. Add a note: "Community Weaving follows the standard Thread operation procedure (params_board_game §Thread Operation) including Co-Movement card draw. The CV −1 effect is the operation's intended outcome; temporal/epistemic/actual auto-effects fire as standard consequences."

### D-03 [LOW] — "Structurally blind to RS" is philosophically elegant

The observation that Church and Hafenmark are "structurally blind to RS crisis" — they can win the political game while the ontological substrate collapses — maps directly to the Foundations' distinction between rendered institutional knowledge and the constitutive ground that makes rendering possible. This is not a critique; it is a commendation. The design correctly implements P-03 (rendering = consciousness-performed) by making factions whose power is rendered-institutional (Church doctrine, Hafenmark law) unable to perceive or address the sub-rendering crisis.

However, the victory architecture should make this explicit: Church victory while RS < 30 should have a narrative consequence marker ("The Church governs a dying world"). Currently, the only RS-linked victory gate is in Varfell and RM paths. Crown's victory requires IP < 60 but not RS > X. Church's victory has no RS condition at all. A Church victory at RS = 5 is mechanically valid — the Church rules the peninsula while reality unravels. Is this intended?

**Recommendation:** [EDITORIAL] — Confirm: Is Church victory at RS < 20 valid? If so, add a narrative marker: "Church victory at RS < 30: Pyrrhic Theocracy — the Church governs a world that is structurally failing. This is a valid victory but the game's epilogue should reflect the impending Rupture."

---

## E. GAME COMPONENT AND COGNITIVE LOAD

### E-01 [MEDIUM] — CV tracking across 15 territories is heavy

Each territory needs a CV marker (0–5). 15 territories × 6 values = 90 possible board states for CV alone. This is a significant cognitive load increase over the current system, which tracks only peninsula-wide clocks (TC, RS, IP, PI).

Per bg_v05 Part Four cognitive load analysis, the game already has "moderate load" systems that require reference cards. Adding 15 independent territory-level stats pushes toward the high-load boundary.

**Recommendation:** Physical component design: use stackable cubes (0–5 cubes on each territory tile) or a separate CV track board with 15 rows. Include a CV reference card per player showing starting values and which CV ranges each faction needs for victory. The ±1/season cap actually helps here — CV changes slowly and players only need to update 1–2 territories per season.

### E-02 [LOW] — 2-season holding needs a tracking mechanism

Players need to track "have I met all conditions for 2 consecutive seasons?" A simple marker (placed when conditions first met, checked at next Accounting) suffices.

---

## F. SUMMARY OF FINDINGS

| ID | Severity | Category | Issue |
|----|----------|----------|-------|
| A-01 | BLOCKER | Hybrid | CV has no state transfer specification |
| A-02 | BLOCKER | Hybrid | TC Win-Delay Rule references obsolete threshold |
| B-01 | BLOCKER | BG | params_board_game still contains full Deed system |
| A-03 | HIGH | Hybrid | P-32 Hybrid victory not addressed; Hollow Victory term collision |
| B-02 | HIGH | BG | Reformed Settlement references dissolved Deed Tokens |
| B-03 | HIGH | BG | Hollow Victory modifier table orphaned |
| B-04 | HIGH | BG | PP-404 coalition pairs ≠ co-victory pairings (needs clarification) |
| C-01 | HIGH | Balance | Crown victory easier than intended (4/6 conditions met at start) |
| C-02 | HIGH | Balance | Crown has no CV tool; CV 3–4 band is undefendable |
| A-04 | MEDIUM | Hybrid | ED-300 Domain Echo redesign not integrated |
| B-05 | MEDIUM | BG | Accounting Step 12 language is Deed-based |
| B-06 | MEDIUM | BG | Partition Victory holding requirement unspecified |
| C-03 | MEDIUM | Balance | CV ±1/season cap makes starting values nearly deterministic |
| C-04 | MEDIUM | Varfell | Stat reveal condition scales with player count |
| C-05 | LOW | Balance | TCV values untested (acknowledged as SIM-DEBT) |
| D-01 | MEDIUM | Canon | T15 hard-fix cites wrong constraint (P-07 → P-03) |
| D-02 | MEDIUM | Canon | Community Weaving P-01 compliance unclear |
| D-03 | LOW | Canon | Church victory at very low RS — confirm intended |
| E-01 | MEDIUM | Cogload | CV tracking across 15 territories is heavy |
| E-02 | LOW | Cogload | 2-season holding needs tracking mechanism |

**BLOCKERs: 3** (A-01, A-02, B-01)
**HIGH: 7**
**MEDIUM: 8**
**LOW: 3**

---

## G. RECOMMENDED RESOLUTION ORDER

1. **A-01 + A-02** (Hybrid state transfer) — mechanical specification, can be done immediately.
2. **B-01 + B-05** (params_board_game propagation) — large but mechanical edit.
3. **C-01 + C-02** (Crown balance) — requires [EDITORIAL] decision on Crown conditions + CV tool.
4. **A-03 + B-03** (Hollow Victory redesign) — requires [EDITORIAL] decision on term usage.
5. **B-02** (Reformed Settlement) — requires [EDITORIAL] decision.
6. **D-01 + D-02** (Canon citations) — mechanical fixes.
7. **C-03 + C-04** — design refinements, can wait for simulation.
8. **All other MEDIUM/LOW** — addressable during propagation or compilation.
