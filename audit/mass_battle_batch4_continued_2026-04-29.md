# Continued Audit Findings — Batch 4
<!-- generated: 2026-04-29 | session continuation after synthesis+resolve pass -->

## NERS FILTER APPLIED — BLOAT CUT (23 items)
Prior findings reclassified as not-real-issues:
TN6=Controlled (fine), face-10 in mass battle (obvious), Ob floor (fine), Momentum (applies by default),
personal/mass pool difference (intentional), wound system (consistent), general TN (7 default is correct),
Fibonacci value (lives in personal combat §8), Domain Echo timing (confirmed clean), muster payment timing (obvious),
Military 1 BG bonus=0 (intended), Partial -15 Disc vs -1 Stab (granularity is the point of derived values),
Fort BG dice vs TTRPG DR (intentionally different by scale), NPC general Medicine (NPC AI handles),
Skirmish -1D pool (Off pool, obvious from context), Wedge negation removes drawback (negated = entire card null),
unit upkeep professional definition (resolved via §A.14c cross-ref), Mass Mismatch source (standalone mass-only rule fine),
Experience-on-draw exploit (draws are hard to engineer in practice), Military 1/2 Experience unreachable (design intent),
E-FAIL-01 (CLOSED: complementary layers), E-FAIL-02 (CLOSED: in derived_stats §10.2), Scene→Mass social win target (readable from context).

---

## APPLIED IN THIS SESSION (auto-resolved, committed)

### Batch 1 (778bdcd): 20 fixes to mass_battle, params, peninsular_strain, victory_v30, derived_stats
- H frozen at battle start clarification
- §A.5 personal combat pause: unilateral/bilateral distinguished
- §A.12 cascade timing: assigned to Phase 6 Step 3
- Rout vs Destroyed: definitional boundary added
- Idle army terrain carve-out (fortifications, Narrow Pass)
- Crown/Church params tactic cards: STRUCK per PP-283
- Command halving: floor, minimum 1
- Crossbow reload PP-301 binary: STRUCK (ED-094 every-turn abstraction confirmed)
- PP-530: moved to Phase 5, "opposing general's Command"
- Reserve first-engagement Off/Def: default split applies
- RS → MS: global replace in peninsular_strain_v30
- ED-743 propagation: struck IP/Strain direct trigger from peninsular_strain Step 4e + PP-NEW-06
- Campaign Supply: derived_stats §8.1 updated to flat −100 (not per-unit)
- Campaign-scale defeat: added Discipline −30 and Mandate −1 to derived_stats §8.1
- Command modifier cross-ref: derived_stats §10.2 ← mass_battle
- Player Morale Effect: unambiguous during pause
- 5-phase Cascade step ordering: clarified
- 5-phase: flagged as documentation-only
- Thread Ob: stated as total three-axis Ob
- S-FAIL-11 clarified

### Batch 2 (b7dcc20): 4 stale-doc fixes
- victory_v30 §0.3: Strain mechanism updated to Accord-based (not direct battle)
- peninsular_strain Step 4d: aligned with §4.2 territory-count condition
- faction_layer §2.3: "Accord frozen" struck; replaced with §7b-compliant wording
- canonical_sources.yaml: updated last_touched entries

---

## NEW FINDINGS (Batch 4)

### [ACCT-01] Step 4c "hostile action" undefined for Accord normalisation
peninsular_strain §7 Step 4c: "garrison present AND no hostile action for 2 consecutive seasons: Accord +1"
"Hostile action" is undefined. Does a Siege of the territory count? Thread operation? Adjacent Battle?
GAP: "hostile action" scope for passive Accord normalisation.

### [ACCT-02] STRUCK: Step 4d condition — FIXED this session.

### [CI-01] "Church Prominent" breaks when Church controls the territory
military_layer §3.2 Prominent definition: "Church Mandate > controlling faction Mandate."
When Church is the controlling faction: Church Mandate > Church Mandate = never true.
Church would generate 0 CI from territories it controls (Piety Yield, Conditional Passive require Prominent).
SIGNIFICANT GAP: Prominent definition must specify that Church controlling a territory = automatically Prominent.
Proposed fix: "Church is Prominent in a territory if: (a) Church controls it, OR (b) Church Mandate > the current controlling faction's Mandate."

### [CI-02] Fractional CI floor vs ±5 seasonal cap — sequence not stated
§3.3 fractional yields floor at Year-End. §3.11 Step 8: ±5 seasonal cap.
Does the cap apply before or after the floor?
GAP: sequence of floor(fractional CI) and ±5 cap application.

### [VIC-01] victory_v30 §0.3 Strain description — FIXED this session.

### [VIC-02] All-military victory path cannot win under current rules without Strain ≥ 6
Math: 6+ territories at Accord ≤ 1 → Strain +3/season. 4 seasons to govern 15 territories = 12 Strain. Cap is 6 for victory.
Pure conquest requires staged approach (≤5 low-Accord territories simultaneously) or hegemony.
This is the INTENDED design — military conquest alone cannot win. Record as confirmed design intent (N, R confirmed).

### [VIC-03] Church Theocratic Bid: no immunity from military during Bid phase
Other factions CAN conduct military operations against Church during Bid phase.
Multi-vector strategy: attack MS → collapse PT → raise Seizure Ob. Confirmed emergent N, R, E.

### [PT-01] PT seasonal cap (±1) — action-only or includes automatic drift?
§1.2: ±1 PT per season "from all sources."
§1.3: Calamity drift = automatic PT −1 at MS thresholds.
If Calamity drift counts toward the ±1 cap: a Preach action in a drifting territory = 0 net change.
GAP: Whether automatic drift and action effects are subject to the same ±1 cap.

### [MIL-01] Faction military balance — confirmed intended asymmetry
Crown: treasury-rich, medium military. Church: quality elite (KT) + volume (8 units).
Varfell: volume (10 units) + highest ceiling but treasury-poor. Hafenmark: economic not military.
Loewenritter: disruption faction, minimal military, coup-reliant.
Confirmed N, R, S, E — all intentional differentiation.

---

## REMAINING JORDAN DECISIONS (all from prior batches, unchanged)

S-FAIL-01: PP-297 Stalemate Break canonical version — Recommend: design doc (Withdrawal)
S-FAIL-02+13: Muster Size §1.2 vs §1.4 — Recommend: Option C (§1.2=target; §1.4=muster output)
S-FAIL-05: Discipline between-battle recovery — Recommend: persists (Option B)
S-FAIL-06: Morale reset between battles — Recommend: resets (Option A)
S-FAIL-15: Siege final Assault resolution — needs procedure
S-FAIL-16: Rout contagion at Morale 0 — Recommend: freeze until next turn
S-FAIL-19: Shadow Intel UX — Recommend: peek (Option A)
S-FAIL-21+22: Mercenary Surge / Martial Law specs needed
MATH-FAIL-01: Siege Ob formula — Recommend: pool = Military + 3
INTER-10d: Focus stat in mass battle — dead stat or secondary function?
INTER-12b: Discipline naming collision — Recommend: rename faction derived value to Cohesion
INTER-14a: military_advance vs BG Battle — do both fire?
INTER-14d+e: Siege × Occupation / War Auth — define Siege vs military_advance relationship
INTER-12e: Muster: Ob roll + Treasury cost — both or one?
INTER-17b: KT unit count vs Military×2 ceiling
INTER-09d: Critical hit vs Overwhelming — confirm same threshold
CI-01: Church Prominent definition when Church controls territory (NEW — HIGH PRIORITY)
CI-02: Fractional CI floor vs ±5 cap sequence (NEW)
PT-01: PT seasonal cap action-only vs total including drift (NEW)
ACCT-01: "Hostile action" for passive Accord normalisation (NEW)
