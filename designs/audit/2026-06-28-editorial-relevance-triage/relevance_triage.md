# Editorial Ledger — Relevance Triage (2026-06-28)

**Scope:** the 93 unresolved entries in `canon/editorial_ledger.jsonl` (82 `open` + 10 `provisional` + 1 `deferred`) as of commit `4a10191`.
**Method:** deep per-item verification — each item's cited contradiction/gap was checked against the live working tree (the current design/params doc, not the item's original snapshot), cross-referenced against later EDs/PPs and `canon/supersession_register.yaml`. Six read-only verification passes, one per topical cluster.

## Headline

**Of 93 outstanding items, 37 are still relevant today; 56 are stale.**

| Verdict | Count | Disposition |
|---|---|---|
| STILL_RELEVANT | 25 | KEEP OPEN |
| NEEDS_JORDAN | 12 | KEEP OPEN (Jordan) |
| ALREADY_DONE | 25 | → resolved |
| SUPERSEDED | 21 | → struck |
| MIGRATION_RESIDUE | 10 | → struck |
| **Total** | **93** | **31 struck · 25 resolved · 37 kept open** |

- **Still relevant (37):** 25 genuine open work items + 12 awaiting a Jordan design/creative decision.
- **Stale (56):** 25 already done but never closed (→ `resolved`), 21 superseded by later canon (→ `struck`), 10 migration `[PROPOSED:…]` residue (→ `struck`).
- **0 dangling references:** the deleted `designs/systems/faction_politics_expanded_v1.md` was re-homed to `designs/provincial/faction_politics_v30.md` (PP-660); every item there was verified against the live successor.

## What this says about the ledger

The largest single finding is that **the open queue was badly overstated**. Two failure modes dominated:

1. **Open-but-done (27% of the queue).** 25 items had their decision fully applied to canon — the ledger row was simply never flipped to `resolved`. The work is in `combat_v30.md`, `faction_politics_v30.md`, `social_contest_v30.md`, `victory_v30.md`, etc., often citing the very ED that stayed open.
2. **Superseded by re-architecture (23%).** Whole sub-systems were rebuilt after the item was filed — most visibly the **mass-battle engine**, where the old SIM-MB balance flags (ED-811/813/822/823/857/858) were overtaken by the per-cell / Lanchester re-architecture, and the **continuous-engine `net-(Ob-0.5)` continuity fix** (2026-06-22) closed a cluster of fieldwork/threadwork items (ED-873/915/1012).

Only the **June Fieldwork diagnostic batch (ED-913…929)** survived largely intact (12 of 17 still relevant) — it is the newest and least overtaken by later work.

## Actions applied to the ledger

Per `valoria-editorial-register` Workflow D. Struck/resolved rows remain in the ledger (never deleted) and are reversible.

- **SUPERSEDED → `status: struck`** with `stale_reason: "Superseded — …"` and `superseded_by` where a single resolved/struck ED is the successor.
- **MIGRATION_RESIDUE → `status: struck`** with `stale_reason: "Migration residue — …"`.
- **ALREADY_DONE → `status: resolved`** with `decision: "[VERIFIED-APPLIED] …"`, `propagation_status: complete`.
- **STILL_RELEVANT / NEEDS_JORDAN → untouched** (left open).
- Every touched row carries `triage_2026_06_28` for auditability.

Side effect: ED-citation-integrity violations dropped **315 → 292** (open-reference info 190 → 79) by moving 56 rows out of `open`. The residual OPEN_AS_BASIS hits on **ED-644 / ED-649 / ED-893** are exactly the NEEDS_JORDAN items left open — they are cited as basis in canon while still unresolved, which is a genuine item for Jordan.

## STILL_RELEVANT — 25 items  (KEEP OPEN)

| ID | Sev | Evidence |
|---|---|---|
| ED-539 | P2 | canonical_registry.md 'CI reform + TCV revaluation + Seizure Accord compound on Church \| P1 (ED-539)' — real open unsimulated-compound flag. |
| ED-615 | P2 | victory_v30.md 'Schoenland Treaty' reward never defines what Schoenland receives from Crown; only Crown-side benefits spec'd. |
| ED-616 | P2 | faction_layer_v30.md §Parliament motions lack any Intelligence-Embargo motion blocking Tribune Domain Actions; mechanic absent. |
| ED-640 | P2 | faction_politics_v30.md Hafenmark Militia ladder still '(provisional — see ED-640)'; not built. |
| ED-648 | P2 | faction_politics_v30.md Hochschule Ministry 'proposed... Minister TBD. [ED-648]'; inclusion unconfirmed. |
| ED-658 | P2 | faction_politics_v30.md Warden-Chief×Path-B Deed-sequence still open; varfell_path_b_v30.md has no Warden-Chief integration. |
| ED-913 | P1 | fieldwork_investigation.md §4.2/§4.5 still 'Thread-Read\|Attunement' & 'Att×2'; params/fieldwork.md still '(Att×2)' — decided pool (Spirit×2)+History+TPS not propagated. |
| ED-914 | P1 | PP-719 still unrecorded in canon/; dead path designs/fieldwork/fieldwork_design_v1.md still referenced in fieldwork_v30.md + fieldwork_godot.md (resolved part: canonical_sources key added). |
| ED-916 | P2 | sim/personal/fieldwork.py + investigation.py continuous-engine validation still owed (Lane C); coverage gap persists. |
| ED-917 | P2 | fieldwork_v30.md §10.5 still per-face d10 skull/pip UI vs params/core continuous magnitude gauge. |
| ED-918 | P2 | fieldwork_v30.md §5.8/§6.3 Niflhel social toolkit still live; no Niflhel/ED-600/ED-894 supersession entry. |
| ED-919 | P2 | fieldwork_v30.md §2.3/§5.7 map Disposition->'Piety Track offset' vs params/fieldwork.md 'Conviction offset' (ED-302). |
| ED-921 | P2 | investigation_systems_v30.md L425 'instead of single Charisma roll' (Interview is Attunement); outcome types lack failure/Exposure schedule. |
| ED-922 | P2 | investigation_systems_v30.md L437-443 PENDING DECISIONS NPE-01/02, DL-01/02, RR-01 still present, 0 ledger records (J-18). |
| ED-925 | P2 | fieldwork_v30.md §6.3 '+1/+2 if Depth>=3' vs §4.2 degree table 'Failure +2' at any depth; params reproduces both. |
| ED-927 | P3 | params/fieldwork.md recovery '<=-3' vs infill §5.2 '<=-2'; decay '>+2' vs infill '>=+3 decays/<=+2 stable' — off-by-ones persist. |
| ED-928 | P3 | fieldwork_v30.md §7 'Composure (Cha+6); Stamina (End+Hist+1)' vs ED-694/params core Composure Cha×3, Stamina (3×End)+(2×Spi). |
| ED-929 | P3 | investigation_systems_v30.md title 'Proposal' vs Status CANONICAL; canon/definitions.yaml still absent. |
| ED-930 | P2 | stats_1_7_scale.md PP-236 still 'Crown has NO Intel stat... use Influence +1 Ob', unmarked-superseded, contradicting same file's ED-787 Crown Int 3. |
| ED-931 | P3 | arc_expansion_v30.md 4.3 still cites dangling params/clocks/clock_registry_v30.md (404s); arcs/ owns-gapped; autonomy-spec home open. |
| ED-932 | P3 | params/bg/clocks.md dup removed @2aee0bba, BUT residuals remain: Battle-Consequences tri-naming + ED-743 staleness; C14a integrity items owns-gapped. |
| ED-1006 | mechanical | A6 gap closed (ED-1038) & F2 types registered (ED-935), but 3-way piety/conviction name collision still open (ED-644); consolidation veto unlogged. |
| ED-1009 | mechanical | A6 resolved (ED-1038) & contest-leverage closed (ED-1037), but 'registry_derived' status & settlement/faction over-coupling never adopted. |
| ED-1010 | P1 | threadwork_v30 §3.2 table still lacks '-1 total' cap text (only in infill l.121); mass_battle A.10 War '-2/op' vs cap unreconciled. |
| ED-1011 | P1 | params/core.md PP-261 'see params_threadwork for full rule' is dead; threadwork §3.7 still [PROVISIONAL], no Coherence-0 fallback. |

## NEEDS_JORDAN — 12 items  (KEEP OPEN (Jordan))

| ID | Sev | Evidence |
|---|---|---|
| ED-644 | P2 | conviction_track_v30.md retains deferred CV-equals-PT equivalence note ('Full rename deferred'); deliberate-deferral design call. |
| ED-649 | P2 | Two College-of-Prelates names (Standing 5) unfilled; creative NPC-naming — Jordan's call. |
| ED-650 | P2 | Succession rivals (Crown Cadet, Varfell protege, Hafenmark candidate) unnamed; creative NPC-naming. |
| ED-651 | P2 | Markamt Minister 'still needs explicit name and Triangle'; creative-naming decision. |
| ED-788 | P2 | '[DEFERRED—SKIP] LICENSE/GOV-08 — skipped per Jordan 2026-05-09, not blocking'; deliberate human deferral. |
| ED-879 | P2 | Out-of-bounds × Pool-Floor-5 interaction; ED-883 confirms GATE-G8 owner-intent; combat_v30 has no rule; design-intent gate. |
| ED-893 | P2 | Citation<->ledger scope mismatch: row='Arc E wager scar-threshold' but ED-893 citations are PP-614 Appraise; 2026-06-28 triage flags reconcile; wager tolerance still silent. |
| ED-911 | — | combat_engine_v1 resolves 1v1 melee only; ranged/group/thread-in-combat still on superseded combat_v30 chassis; ED-1029 D9 'unbuilt', adjudication pending. |
| ED-920 | P2 | Sincerity Gate bare Spirit & Knot Spirit×2 no-History deviate from (Attr×2)+History; ledger asks ratify-or-normalize — design intent. |
| ED-924 | P2 | fieldwork_v30.md §4.1 'threshold not known to player' vs investigation_systems Case Board exposing 3/5/8; mode-intent call. |
| ED-1033 | P2 | contest.md 'Obscuring win: no track movement'; INTENT UNDETERMINED, Jordan to confirm Indirect as denial/tempo vs track lever. |
| ED-1036 | P2 | L3 venue policy-fit legibility; explicit 'Jordan to confirm UI surfaces this' design-intent; no canon contradiction. |

## ALREADY_DONE — 25 items  (→ resolved)

| ID | Sev | Evidence |
|---|---|---|
| ED-617 | P2 | social_contest_v30.md implements '(ED-617)' Grand Contest Recall once-per-source-per-contest verbatim; row never closed. |
| ED-618 | P2 | Torben Emergence Window live: npc_character_analyses_v30.md + npc_behavior_v30.md reference ED-618 Conviction-window arc. |
| ED-619 | P3 | clock_registry_v30.md + social_contest_v30.md implement 'cap ~3 active (ED-619)' GM advisory; row never closed. |
| ED-620 | P1 | victory_v30.md §8 'RM Founding Mechanic (ED-620 — approved 2026-04-17)' fully built; row never closed. |
| ED-642 | P2 | faction_politics_v30.md confirms Grand Guildmaster Std 6 exists-but-normally-omitted per collective-leadership; answered in body. |
| ED-643 | P1 | Grep designs/ for the deprecated faction name: zero live-canon hits; all matches are audit/violation-records; Solmund-naming propagation complete. |
| ED-645 | P2 | faction_politics_v30.md §4.3 reconciliation + geography_v30.md applies it (Askeheim=territory, Southernmost=region). |
| ED-652 | P2 | faction_politics_v30.md §1.0/§1.4 fully spec dismissal/re-entry/Dishonored-flag; closed by ED-776. |
| ED-655 | P2 | faction_politics_v30.md PART 7 builds uniform Ministry/Committee expansion with faction-specific titles (the recommendation). |
| ED-657 | P2 | faction_politics_v30.md §1.4 specifies restoration paths/costs; closed by ED-776. |
| ED-670 | P3 | Heresy Jurisdiction applied: thread_horizontal_integration_spec.md 'ED-670 \| Applied (§3.4 npc_behavior_v30)'. |
| ED-707 | — | CR/VTM strike applied: params/bg/faction_actions.md 'Cultural Reformation STRUCK (PP-664)' + VTM Discretion struck; CR-STRIKE-2026-04-19. |
| ED-708 | — | Varfell Path C dissolution landed: strategic_layer_v30.md 'G-03 STRUCK (PP-663)'; VTM-STRIKE-2026-04-19. |
| ED-709 | — | PP-664 residual cleanup applied in all 3 files (faction_actions.md, npc_priority_trees.md, strategic_layer_v30.md). |
| ED-738 | P1 | Ein Sof gradient committed d80e1532 '[editorial] ED-738'; live in params/threadwork.md; 'not committed' claim stale. |
| ED-843 | P3 | threadwork_v30.md §3.3 Severed/Coherence-1 row is full ('All Knots +2 strain/session'+narrative); Pass-2g truncation gone live. |
| ED-867 | P3 | ners_verdict_faction.md already carries '[SUPERSEDED-BY ED-867 ... corrected to 0.010]' markers at source; requested markers in place. |
| ED-873 | P3 | params/core.md §Continuous Engine carries 'net-(Ob-0.5)' continuity correction (landed 2026-06-22); flagged omission applied. |
| ED-890 | P2 | combat_v30 §Reach Rules (PP-268): 'Close->Melee, Far->Ranged renamed throughout'; ED-129 resolved; row never closed. |
| ED-891 | P2 | contest.md 'Exchange Step 1 renamed Read->Judge', Appraise (PP-614); rename applied; row never closed. |
| ED-894 | P3 | Niflhel rows deleted from params/factions_personal.md & params/contest.md per ED-764; propagation done; row never closed. |
| ED-915 | P2 | params/core.md §Continuous Engine landed the ER-2 continuity term 'net-(Ob-0.5)' (2026-06-22); wound-floor concern resolved. |
| ED-926 | P2 | F3 lifecycle audit now exists: tests/sim/fieldwork_lifecycle_stress_01/f3_heresy_investigation_lifecycle.md + ledger F3-L01..L10. |
| ED-933 | P3 | params/core.md now 'Stamina = (3×Endurance)+(2×Spirit)' (range 5-35); the @7ad92356 fix present; row never closed. |
| ED-1012 | P1 | params/core.md continuous engine now 'net-(Ob-0.5)' (landed 2026-06-22) — the ED-873/RD-1 fix; row never closed. |

## SUPERSEDED — 21 items  (→ struck)

| ID | Sev | Evidence |
|---|---|---|
| ED-295 | P2 | params/contest.md 'ED-295... RESOLVED Option D per-exchange erosion'; ED-896 marks the [PROPOSED] scrape stale. |
| ED-542 | P2 | mass_battle_v30.md §A.4/§E carries fully-built battle-consequences propagation (ED-743/1027/898); original gap closed. |
| ED-587 | P2 | scale_transitions_v30.md §4.3.2 implements 'Stability <=2 OR drops >=2 in single Accounting (ED-587)' + ED-749 hysteresis. |
| ED-631 | P2 | social_contest_v30.md §7.3 (ED-772) specifies Heresy Investigation '4-6 seasons'; resolution-time gap closed. |
| ED-706 | P2 | GAP-29 VTM strike propagation pending PP-664 — now complete across all targets (see ED-709); gap closed. |
| ED-811 | P1 | massbattle.py adopts PP-233 continuous net_successes×(1+power) at all sites; mass_combat.md Core Formula confirms; margin ambiguity resolved. |
| ED-813 | P2 | Live engine continuous tick-based with disengage/reform at phase boundaries, not Phase-3-vs-5 gate; SIM-MB-04 question moot. |
| ED-822 | P2 | Recommended TN7 NOT adopted — live VOLLEY_TN=6 + density-scaled volley + Lanchester; SIM-MB-05 concern superseded by re-architecture. |
| ED-823 | P2 | Live engine per-cell support-stacking + puncture, not Fibonacci denominators; 'needs SIM-MB-06' overtaken by tests/sim/mass_battle. |
| ED-857 | P2 | Speed now per-cell continuous (PC_CAVALRY_SPEED_MULT=2.0 etc); 3-tier table assumption superseded; canonize-table ask moot. |
| ED-858 | P3 | POOL_VARIANT C-ii's 0.5 mult superseded — live pool = COMMAND_POOL_MULT×Command (Jordan 2026-06-02, ED-899/1013). |
| ED-864 | P2 | jordan_decision 'ratified 2026-05-17'; sub-decisions ED-295/296/297 resolved, Contest renames applied (Read->Judge); content done. |
| ED-869 | P1 | Crown-Mil decision applied (stats_1_7_scale.md '5/6 struck per ED-869'); 6->7 schema drift explicitly deferred to Lane-A by Jordan 2026-05-31. |
| ED-870 | P1 | combat_v30.md now 'Combat Pool = max(5, History+6)' [RATIFIED 2026-05-29 R1], Agility-independent — supersedes both old & PP-717; params/combat.md deprecated (ED-1029). |
| ED-892 | P2 | Derived-stat split from ED-694, which ledger marks 'superseded' by ED-789 (jordan 'revert ED-694', 2026-05-09); parent reverted. |
| ED-923 | P2 | ED-912: params/fieldwork.md now 'Disposition >=+3 (ED-912 — was Bonds-1)', matching master §1/§5.4; divergence gone. |
| ED-1002 | P1 | contest.md & social_contest_v30.md now 'Attunement+Recall, Ob=opp Cha/2'; old 'Attunement alone Ob1' struck (PP-614/ED-893). |
| ED-1003 | P1 | social_contest_v30.md ×3 strain (ED-891) + depletion -3->-5 (ED-890) reconciled; params Derived Values match. |
| ED-1004 | P1 | PP-351 single canonical form (ED-900/D-3); social_contest §9.4 + contest.md PP-258 both marked SUPERSEDED. |
| ED-1007 | canonical-gap | ED-935 (2026-06-14 J-2) registered scene.displacement/project_advanced/completed/failed in key_type_registry; attributions explicitly deferred there. |
| ED-1042 | P2 | Wound model reconciled 2026-06-18 via ED-1021 (D-A): sim r2_consequence_wounds.py & derived_stats_v30 §4.1 share WI=round(End+4+0.4·Spi); drift gone. |

## MIGRATION_RESIDUE — 10 items  (→ struck)

| ID | Sev | Evidence |
|---|---|---|
| ED-129 | P2 | 'Ranged weapon dual taxonomy (PROPOSED)' scrape; actionable content split to ED-890 (close/far->reach). |
| ED-131 | P2 | 'Contest values unplaytested' scrape; content carried to ED-891; stub. |
| ED-545 | P2 | Self-resolving scrape 'Substantially resolved by §4.3.2/§4.3.3/§4.4'; scale_transitions_v30.md exists; no open action. |
| ED-547 | P2 | Self-resolving scrape 'Scene cap IS the fieldwork resource'; fieldwork_v30.md confirms; nothing to do. |
| ED-763 | P2 | '[PROVISIONAL] doc 12 v1.2 promotion-readiness' tracking note; actionable remnant split to ED-893. |
| ED-764 | P3 | '[PROVISIONAL] throughlines load-bearing column' tracking note; Niflhel-propagation remnant split to ED-894. |
| ED-860 | P3 | 'Pass 2n explicitly NOT canonizing' interim multi-turn bands; declined-proposal process artifact. |
| ED-861 | P3 | 9-week cadence 'Process target' in integration_plan_v18 §6; scheduling note, never canon. |
| ED-862 | P3 | ±2pp v17/v18 parity tolerance — process_threshold; v17/v18 build superseded by mass_battle engine. |
| ED-863 | P3 | Phase-9 per-faction split sequencing note; build-sequencing artifact. |

## Recommended follow-ups (not done here)

- **12 NEEDS_JORDAN** items need a creative/design ruling: NPC naming (ED-649/650/651), deliberate deferrals (ED-788 license, ED-644 CV→PT rename), and design-intent gates (ED-879, ED-893, ED-911, ED-920, ED-924, ED-1033, ED-1036).
- **25 STILL_RELEVANT** items are real engineering/propagation work — the bulk is the Fieldwork master-vs-params reconciliation (ED-913…929) already tracked as Lane A / workplan-v5 row #15/#20.
- Consider flipping the ED-citation validator to **blocking** once the three NEEDS_JORDAN basis-citations (644/649/893) are resolved — that was the last batch holding it report-only.
