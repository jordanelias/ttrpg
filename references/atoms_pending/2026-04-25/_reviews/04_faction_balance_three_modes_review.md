# Exhaustive Review — `04_faction_balance_three_modes`

**Topic:** Faction Balance & Three-Mode Architecture (consolidated)
**Atoms:** 50
**Method:** strict ID-presence check in primary registers (definition-pattern aware: YAML `id: X-N` for ED/PP, `| T-N |` table-row or `## T-N` heading for T/M) + repo path-existence + substantive-claim extraction with best-match canon excerpt.

## Summary

### ID classification

- **DEFINED-IN-CANON:** present as a defined entry in primary register (YAML `id:` for ED/PP; table row or heading for T/M).
- **MENTIONED-IN-CANON:** appears in canon corpus but not as a primary-register definition (likely cross-reference or editorial marker).
- **PARTIAL:** defined in canon, but atom's discussion is materially richer.
- **NEW:** not present in any fetched canon file.

| status | count |
|---|---|
| DEFINED-IN-CANON | 2 |
| MENTIONED-IN-CANON | 3 |
| PARTIAL | 0 |
| NEW | 0 |

### Path verification

| status | count |
|---|---|
| EXISTS | 1 |

### Substantive claims surfaced: 69

## ID-by-ID comparison

### ED-706 — **MENTIONED-IN-CANON**

- **detail:** Appears in `references/canonical_sources.yaml` but not as a defined entry in primary register.
- **atom context** (`master_document_2026-04-25__33__6-5-framework-propagation-gaps-deferred-from-prior`):
  > . This resolution needs canonical propagation.]`  `[GAP-28: PP-540/PP-541 inconsistencies between victory_v30 §3 and params/bg/victory.md. Sync needed.]`  `[GAP-29: VTM strike propagation incomplete (ED-706, pending PP-664). VTM → WR replacement in params/bg/victory.md not done.]`  `[GAP-30: Cultural Reformation strike (CR-STRIKE-2026-04-19) violates §0.5 design principle (each faction has non-mil
- **canon context** (`references/canonical_sources.yaml`):
  > no canonical advancement rule. Referenced in victory paths + Cultural Reformation pool but never defined. Struck per Jordan 2026-04-19."       eds: [ED-706]       replacement: "Pending editorial rewrite of Varfell victory paths."       commits: [f7aa0ed, 297f892, 13b8f30, 613ebf9, dc13a75, "pending-PP-664"]     - id: "PP-650"       name: "Cultural Reformation"       reason: "Varfell Colonist card 

### ED-727 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger_archive.yaml`.
- **atom context** (`master_document_2026-04-25__30__6-2-strategic-layer-mechanical-gaps`):
  > Path A "2 rival stats fully revealed" — mechanically vague. Which stats? Public reveal vs Tribune-internal? Counts current state or sustained reveal?]`  `[GAP-8: Lenneth TS pathway ceiling 10–20 (D-6 ED-727) — does Lenneth Crown ascension (Arc B) trigger Crown Conviction shift in BG mode? Current BG-layer mechanism for "Crown becomes pro-Einhir" unclear.]`  `[GAP-9: Co-victory pairing thresholds —
- **canon context** (`canon/editorial_ledger_archive.yaml`):
  > ite_network.md or expansion of designs/world/calamity_radiation_v30.md. Pending separate workplan."     status: resolved     severity: P1     source: "session_master_2026_04_20.md + handoff"    - id: ED-727     date: 2026-04-20     description: "D-6 resolved: Lenneth TS pathway = slow scholarly loosening, SA-gated, ceiling 10-20. Propagated designs/npcs/npc_character_analyses_v30{,_infill}.md 2026

### PP-540 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/provincial/victory_v30.md` but not as a defined entry in primary register.
- **atom context** (`master_document_2026-04-25__13__2-1-initial-faction-balance-audit-findings`):
  > | 1 | 13 | | RM (cond.) | 1 | 3 | n/a | 3 | 2 | 3 | 12 | | Löwenritter (cond.) | 1 | 2 | n/a | 1 | 3 | 2 | 9 |  **Key strategic-layer findings:**  - **Crown's PV ≥ 14 milestone is pre-met from S1** (PP-540 reduced 16→14 to match starting PV; Crown starts with exactly 14 PV). - **Most underbalanced = Varfell**, primarily because CR-STRIKE-2026-04-19 removed Cultural Reformation (Varfell's only non-
- **canon context** (`designs/provincial/victory_v30.md`):
  > 297f892 (engine), 13b8f30 (workplan). -->  ## ED-306 Resolution (v3 — geography_design.md territory numbering, CI 100 canonical, PT cap clarified) ## PP-540–546 (2026-04-10): Balance patches — solo + co-victory timeline normalisation ## Date: 2026-04-06 | Status: DESIGN — pending Varfell Path B user decision (ED-311) ## Supersedes: v2 (same path), params_board_game.md §Victory Conditions, all Deed

### PP-541 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/provincial/victory_v30.md` but not as a defined entry in primary register.
- **atom context** (`master_document_2026-04-25__14__2-2-monte-carlo-simulation-results`):
  > own Treaty cession on Success+OW** (P0) — operationalizes `peninsular_strain §5.1` 5. **Church PV ≥ 10 + Accord ≥ 2 in 3 non-cap + Mass Seizure must fire** (P1) 6. **Hafenmark PV ≥ 12** (P1) — revert PP-541 7. **Hafenmark Diplomatic Token -1 Ob** (P1) — auto-applied, models `peninsular_strain §5.3` 8. **Sovereign Authority costs Diplomat-card** (P1, audit §6.3) 9. **Calamity Refugee penalty at MS 
- **canon context** (`designs/provincial/victory_v30.md`):
  > constitutional reformer.]**  **All conditions simultaneous at Accounting:**  | Condition | Threshold | |-----------|-----------| | PV held | ≥ 13 | *(PP-541: was 12)* | | Hafenmark Mandate | ≥ 4 | | Hafenmark Stability | ≥ 3 | *(PP-571, ED-388: prevents Parliamentary Sovereignty while faction is destabilised)* | | PI | ≥ 5 | | Crown Mandate | ≤ 3 |  #### Alternate — Dynastic Assertion (ED-307)  | 

### PP-664 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/patch_register_active.yaml`.
- **atom context** (`master_document_2026-04-25__33__6-5-framework-propagation-gaps-deferred-from-prior`):
  > n needs canonical propagation.]`  `[GAP-28: PP-540/PP-541 inconsistencies between victory_v30 §3 and params/bg/victory.md. Sync needed.]`  `[GAP-29: VTM strike propagation incomplete (ED-706, pending PP-664). VTM → WR replacement in params/bg/victory.md not done.]`  `[GAP-30: Cultural Reformation strike (CR-STRIKE-2026-04-19) violates §0.5 design principle (each faction has non-military Accord ≥ 2
- **canon context** (`canon/patch_register_active.yaml`):
  > litics_v30.md     - designs/npcs/npc_behavior_v30.md     - designs/provincial/varfell_path_b_v30.md     - designs/provincial/peninsular_strain_v30.md   status: applied   applied_commit: pending - id: PP-664   date: 2026-04-19   severity: P2   description: "VTM-STRIKE residual cleanup — completes PP-663. Patches three files     where PP-663 added tombstone banners but left bodies unedited: faction_

## Path verification

| path | status | atom occurrences |
|---|---|---|
| `params/bg/victory.md` | EXISTS | 4 |

## Substantive claim findings

_69 substantive claims (max 3 per atom) with best-match canon excerpts._

### Matched claims (64)

- **atom** `master_document_2026-04-25__09__sim-balance-py-36k`
  - claim: > Faction-balance work remains valid as Mode 3 (Strategy) sub-tuning but is no longer the primary design question.
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 6/8)
  - canon excerpt: > sturing without resolution).  ---  ### A.13 REINFORCEMENT (between battles) *[editorial items]*  Natural: +1 Size per campaign season. Accelerated: 1 Faction Resource per additional Size point. Maximum: cannot exceed original Size at army creation. D

- **atom** `master_document_2026-04-25__09__sim-balance-py-36k`
  - claim: > Leadership felt-win** | Stature 7 attainment as victory | Does ascending to leadership feel like winning?
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 4/7)
  - canon excerpt: > through Standing 7). Standing 0 is explicit pre-initiation status, not "no relationship." Standing 7 is the senior-most position short of leadership; Leadership itself is a discrete state (not a ninth Standing), reached via the succession mechanisms 

- **atom** `master_document_2026-04-25__09__sim-balance-py-36k`
  - claim: > Stage 5 (Three Modes) is the canonical recommendation.
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 3/5)
  - canon excerpt: > % of max: −1 - Size dropped below 25%: −1 additional - Discipline broken this turn: −1 - Allied unit routed in same zone: −1 - General incapacitated (Stage 1): −1 - General killed (Stage 2): −2 - Flanked and lost exchange: −1 - No engagement for 2+ c

- **atom** `master_document_2026-04-25__10__1-1-three-modes-of`
  - claim: > - **Fulfilment terminus:** Portrait Sequence (a record of who the character became)
- **Reference design space:** Mount & Blade sandbox, Pathologic 2, Disco Elysium, Manor Lords immersion
- **Mechanical posture:** Predominantly personal-scale, no dec
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 3/8)
  - canon excerpt: >  engagement pool formula (PP-233) — ranged output is governed by unit quality, not generalship. Net successes − DR (Projectile column) = Size loss to record. (PP-503) [PROVISIONAL] Prepared Defence: declare in Phase 1; half Effective Power as passive

- **atom** `master_document_2026-04-25__13__2-1-initial-factio`
  - claim: > - **Most structurally favoured = Hafenmark**: calamity insulation (all territories at radiation distance 4–5), 4 co-victory paths, Sovereign Authority passive CI drain (no action cost), lowest Leadership Deviation Ob 1, BALANCE-005 unenforced.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 4/8)
  - canon excerpt: >  Almstedt). The Almqvist dynasty traces its legitimacy to the first Almqvist's documented deeds at kingdom-founding. Rank advancement in the Crown is structurally a re-enactment of that logic: each rank demands a deed that renews the founding princip

- **atom** `master_document_2026-04-25__14__2-2-monte-carlo-si`
  - claim: > **Tribune Compact** for Varfell (P0, audit §6.1) — Ob = M/2 + 2, gates Intel ≥ 5 + S ≥ 4
2.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 5/6)
  - canon excerpt: > ence) | Riskbreaker ladder (Part 2, §2.2); Niflhel transactional relationships (Part 2, §2.6) | Spymaster (TBD name) → Riskbreaker Commander | Senior Tribune of the Schattendienst |  Branch switching is possible but expensive: requires one completed 

- **atom** `master_document_2026-04-25__14__2-2-monte-carlo-si`
  - claim: > **Mass Seizure quadratic** declaration probability (P0) — replace `^3.3` with `^2.0`
3.
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 4/5)
  - canon excerpt: > nsular_strain §3.2. Battle-season immediate costs (MS, Accord erosion) retained.]  ### §E.3 Exceptions  - Covert operations (Niflhel sabotage, Church Seizure of ungarrisoned territories): no MS/IP/Strain cost. - Altonian Vanguard battles: MS −1 (sieg

- **atom** `master_document_2026-04-25__14__2-2-monte-carlo-si`
  - claim: > **Crown all-3-rivals milestone** (P0) — revert PP-540's 2-of-3 softening
4.
  - best match: `designs/provincial/victory_v30.md` (overlap 5/6)
  - canon excerpt: > cturally blind to the Mending Stability (MS) crisis. Church compensates with Mass Seizure — a one-shot bid available at CI ≥ 60, strongest at CI 100. Crown and Varfell can address MS via Thread path but at cost of political resources.  **Equal win pr

- **atom** `master_document_2026-04-25__15__2-3-critical-findi`
  - claim: > Iteration 2 disabled milestone paths and tested universal sovereignty alone.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 6/8)
  - canon excerpt: > ggers** (per worldbuilding_v30 §4.3 Card: Riskbreaker Exposure). Crown Domain Actions against non-Crown factions +1 Ob. | | 4 | Cooling-off reduction disabled (Debt sticks above 4). | | 5 | **Parliamentary inquiry opens** — Grand Debate (Crown Influe

- **atom** `master_document_2026-04-25__15__2-3-critical-findi`
  - claim: > The peninsula collapses before any faction reaches "all 15 territories + Accord ≥ 2 + Strain ≤ 6."

**Implication for canon:** Either retain milestone paths as canonical alternate endpoints (revert peninsular_strain §6.2 framing), or universal path r
  - best match: `designs/provincial/faction_layer_v30.md` (overlap 8/8)
  - canon excerpt: > , ED-334/335 (Officer Capture), PP-500 (Political Vacuum) --> <!-- Integrates with: Phase 4 Priority-4 Social actions; Phase 5 Accounting steps 1–13; peninsular_strain_v1.md (Accord, Strain, battle consequences) --> <!-- Status: CANONICAL — approved 

- **atom** `master_document_2026-04-25__16__2-4-strategic-laye`
  - claim: > - **Church Theocratic Triumph**: PV ≥ 10 + 3 non-cap territories Accord ≥ 2 + Mass Seizure declared AND Cardinal succession confirmed (specific Cardinal arc resolved).
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 7/8)
  - canon excerpt: > eferences: player_agency_v30 (Standing §5, Renown §5.4, Duties §3), factions_ttrpg_v30 (8-faction roster §8.2–§8.9), worldbuilding_v30 (Four-Cardinal Church §3, Löwenritter arms §4, Guild structure §5, Parliament §6), npc_roster_v30 §14 (caste annota

- **atom** `master_document_2026-04-25__16__2-4-strategic-laye`
  - claim: > - **Hafenmark Sovereign Recognition**: PV ≥ 12 + Sovereign Authority Doctrine validated by Crown formal recognition (a *scene*, not just stat values).
  - best match: `designs/provincial/baralta_crown_claim_v30.md` (overlap 8/8)
  - canon excerpt: > laim — BG Mechanic Design ## Status: DESIGN (editorial decision, flagged for review) ## Date: 2026-04-11 ## Resolves: Mechanical gap — no BG path for Hafenmark to claim the Crown despite deed-logic supporting Baralta as strongest candidate ## Affects

- **atom** `master_document_2026-04-25__16__2-4-strategic-laye`
  - claim: > - **Varfell Tribune Triumph**: PV ≥ 8 + T4 + T13 held + WR ≥ 3 + an Einhir restoration ceremony performed at T13.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 6/7)
  - canon excerpt: > ) | | A-09 | Ministry system (MIN-01–06) is Crown-exclusive. The Church's four-cardinal apparatus, Hafenmark's parliamentary committee structure, and Varfell's Jarl councils have equivalent institutional functions with no mechanical scaffolding. | P2

- **atom** `master_document_2026-04-25__17__3-1-player-experie`
  - claim: > Hafenmark's strategic strengths (calamity insulation, 4 co-victory paths, geographic insularity) translate to **player-experience deficits** — fewer crisis scenes at home, narrower Conviction surface, leaner Faction-Internal Duty texture.
  - best match: `designs/provincial/victory_v30.md` (overlap 6/8)
  - canon excerpt: > ndition, faction acquisition toolkits)  ---  ## Core Frame   Two simultaneous contests: who governs the peninsula AND whether it survives. Church and Hafenmark are structurally blind to the Mending Stability (MS) crisis. Church compensates with Mass 

- **atom** `master_document_2026-04-25__17__3-1-player-experie`
  - claim: > **Varfell has the highest Conviction surface area** (9 distinct Conviction generators vs Crown 7, Church 6, Hafenmark 5) — counter to its lowest strategic-layer ranking.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 7/8)
  - canon excerpt: > ) | | A-09 | Ministry system (MIN-01–06) is Crown-exclusive. The Church's four-cardinal apparatus, Hafenmark's parliamentary committee structure, and Varfell's Jarl councils have equivalent institutional functions with no mechanical scaffolding. | P2

- **atom** `master_document_2026-04-25__19__3-3-the-strong-cho`
  - claim: > **Fix for faction balance must not collapse into the strategic layer at the expense of the personal layer.**

---

# PART IV — LEADERSHIP WIN ARCHITECTURE (Stage 4 outcomes)

This section preserves Leadership Win mechanics as input to Mode 3 Stature 
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 7/8)
  - canon excerpt: >  (EXPANDED) ## Date: 2026-04-16 (original audit); expanded 2026-04-17 ## Status: CANONICAL (approved Jordan 2026-04-17, commit PP-660) ## Supersedes: faction_politics_patch_register_2026-04-16.md (original, 5-rank draft) ## [EDITORIAL: ED-634–ED-658 

- **atom** `master_document_2026-04-25__20__4-1-the-3-scene-as`
  - claim: > - **Stature 5–6 contested**: Council Contest Scene — inner-circle deliberation with player swing-vote performance.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 7/8)
  - canon excerpt: > ence Checks (resists Confessor countermanding) | +1D; arm-specific modifier (see §5.2) | Cardinal retains full arm authority even if the Confessor is contested | | 7 Confessor-Presumptive | Standard | Named Character Event Cards for the Presumptive's

- **atom** `master_document_2026-04-25__20__4-1-the-3-scene-as`
  - claim: > - **Standing 4+ challenge**: Confrontation Scene — public denunciation, Council adjudication.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 5/8)
  - canon excerpt: > orial items and 5 SIM-DEBT items raised by this register, tracked in canon/editorial_ledger.yaml.] ## Scope: Item 1 rank-ladder expansion to 8 ranks (Standing 0–7) with Skyrim-guild progression patterns; sub-office ladders (Löwenritter, Riskbreakers,

- **atom** `master_document_2026-04-25__29__6-1-three-mode-arc`
  - claim: > Player writes a sentence; engine must extract target NPCs, target territories, target Conviction-types, target factions, completion criteria.
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 6/8)
  - canon excerpt: > las reference Size unchanged. Output scaling: `effective_damage = floor(successes × (1 + Power) × TroopCount / max_TroopCount)`, capped at ratio 1.0. Player sees: "Heavy Infantry — 4,428 / 5,000 (Size 4)".  Thread Sensitivity minimums per scale still

- **atom** `master_document_2026-04-25__29__6-1-three-mode-arc`
  - claim: > Recommend: start with template-only Trajectory (P0); authored Trajectory deferred to P1.]`

`[GAP-2: Mode-shift recognition scenes need authored content per shift type.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 3/8)
  - canon excerpt: > ved in this register.** This is flagged as:  **New editorial item:** ED-645 (P2) — T15 name reconciliation. Check geography_v30 for canonical choice. Recommend: use "Southernmost" for directional references and "Askeheim" for proper-name references; 

- **atom** `master_document_2026-04-25__29__6-1-three-mode-arc`
  - claim: > Six shift directions × variant scenes per direction = ~18 scene templates needed.
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 6/8)
  - canon excerpt: > he damage | Cognition check, Ob 1 | Success: reveals exact casualties, territory infrastructure damage, and one hidden consequence (NPC death, Accord shift, or evidence planted during the chaos). Overwhelming: +1 Momentum (tactical understanding). | 

- **atom** `master_document_2026-04-25__30__6-2-strategic-laye`
  - claim: > Counts current state or sustained reveal?]`

`[GAP-8: Lenneth TS pathway ceiling 10–20 (D-6 ED-727) — does Lenneth Crown ascension (Arc B) trigger Crown Conviction shift in BG mode?
  - best match: `designs/provincial/peninsular_strain_v30.md` (overlap 5/8)
  - canon excerpt: >  Crown 12, Hafenmark 6, Church 5, Varfell 6.  ---  ## §2 Accord (Per-Territory Attribute) — NEW  Accord represents the population's acceptance of the current controller's governance. It modifies the territory's effective Prosperity.  **Range:** 0–3 (

- **atom** `master_document_2026-04-25__30__6-2-strategic-laye`
  - claim: > Current BG-layer mechanism for "Crown becomes pro-Einhir" unclear.]`

`[GAP-9: Co-victory pairing thresholds — calibrated against pre-PP-540/PP-541 PV values?
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 5/8)
  - canon excerpt: > interaction; Ministry expansion to non-Crown factions; cross-faction parity; unified resolution of ED-POL-01 through ED-POL-14. ## Cross-references: player_agency_v30 (Standing §5, Renown §5.4, Duties §3), factions_ttrpg_v30 (8-faction roster §8.2–§8

- **atom** `master_document_2026-04-25__30__6-2-strategic-laye`
  - claim: > Crown+Varfell requires Crown PV ≥ 12, but Crown starts at 14.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 6/6)
  - canon excerpt: > s (Löwenritter, Riskbreakers, Inquisitors, Templars, Guilds, Niflhel, RM-when-active); caste integration; CV≡PT terminology equivalence note; Baralta Crown Claim rank-ladder interaction; Ministry expansion to non-Crown factions; cross-faction parity;

- **atom** `master_document_2026-04-25__31__6-3-player-experie`
  - claim: > Each friction needs ~4–6 Slate templates.]`

`[GAP-16: Victory Scene templates per audit §6.9 not yet drafted.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 4/8)
  - canon excerpt: > inition.** Deniability Debt is the Riskbreaker-specific tracked risk that the Order's covert operations leave traces. It accumulates from operational friction (evidence trails, partial successes, witness exposure) and discharges through cooling-off p

- **atom** `master_document_2026-04-25__31__6-3-player-experie`
  - claim: > Each faction needs one canonical Victory Scene + 3 alternate paths.]`

`[GAP-17: Calamity-track-to-faction-victory connection per audit §6.10 needs canonical specification.
  - best match: `designs/provincial/victory_v30.md` (overlap 7/8)
  - canon excerpt: >  All VTM references and Cultural Reformation references below this line are SUPERSEDED. Pending: editorial rewrite --> <!-- of Varfell victory paths, faction actions list, and NPC priority trees. See commits: 297f892 (engine), 13b8f30 (workplan). -->

- **atom** `master_document_2026-04-25__31__6-3-player-experie`
  - claim: > Currently exists as proposal only.]`

`[GAP-18: Stature 5 leadership challenge multi-scene arc per audit §6.12 needs full scene specifications.]`

`[GAP-19: Hafenmark Faction-Internal Duty content beyond cadet-branch family + parliamentary work.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 5/8)
  - canon excerpt: > ader dies during assessment | Immediate succession per SUC-01. |  **Vaynard-specific:** If Vaynard is assessed as incapacitated, the Hochjarl (if one exists) automatically becomes Regent. If no Hochjarl exists, the Senior Jarl with highest Military c

- **atom** `master_document_2026-04-25__32__6-4-leadership-win`
  - claim: > Each faction needs at least 3 Vacancy Scene variants (peaceful succession, contested, post-coup) with specific NPC speaking parts.]`

`[GAP-23: First Decree action options per faction.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 7/8)
  - canon excerpt: >  (EXPANDED) ## Date: 2026-04-16 (original audit); expanded 2026-04-17 ## Status: CANONICAL (approved Jordan 2026-04-17, commit PP-660) ## Supersedes: faction_politics_patch_register_2026-04-16.md (original, 5-rank draft) ## [EDITORIAL: ED-634–ED-658 

- **atom** `master_document_2026-04-25__32__6-4-leadership-win`
  - claim: > Each faction needs ~4–6 canonical First Decree archetypes, drawing from common Conviction patterns.]`

`[GAP-24: Maret Uln's promotion to canonical Varfell successor needs alignment with existing npc_character_analyses.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 7/8)
  - canon excerpt: >  (EXPANDED) ## Date: 2026-04-16 (original audit); expanded 2026-04-17 ## Status: CANONICAL (approved Jordan 2026-04-17, commit PP-660) ## Supersedes: faction_politics_patch_register_2026-04-16.md (original, 5-rank draft) ## [EDITORIAL: ED-634–ED-658 

- **atom** `master_document_2026-04-25__32__6-4-leadership-win`
  - claim: > Confirm Maret's stat profile and Conviction set support this role.]`

`[GAP-25: Hall of Lineage data structure not specified.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 6/8)
  - canon excerpt: > ing burden | **Proposed resolution**: Shadow Renown tracked on companion app as separate subfield of Renown track; does not create additional burden. Confirm with companion_specification_v30. | | ED-POL-05 | Ministry NPCs Stance Triangles | **Partial

_(34 more matched.)_

### Unmatched claims — possibly NEW or rephrased (5)

- atom `master_document_2026-04-25__15__2-3-critical-findi`: > Result: 0% wins, 75% anarchy.
- atom `master_document_2026-04-25__35__phase-b-three-mode`: > Implement Trajectory templates (proposal #13)
8.
- atom `master_document_2026-04-25__42__8-2-universal-sove`: > Resolves peninsular_strain §6.2 vs victory_v30 §3 propagation gap.
- atom `master_document_2026-04-25__47__8-7-defeat-is-also`: > Strategy players who lose should feel their loss, not see a generic end-card.
- atom `master_document_2026-04-25__49__8-9-faction-balanc`: > Add Wanderer mode mechanics to §5.3.

## Recommendation

**Recommendation: CANONICAL-PROMOTION-NEEDED — 3 IDs mentioned in canon but not in primary register; promote to formal entries before ingestion.**

- ID classification: {'DEFINED-IN-CANON': 2, 'MENTIONED-IN-CANON': 3, 'PARTIAL': 0, 'NEW': 0}
- Path verification: {'EXISTS': 1}
- Substantive: 64 matched / 5 unmatched