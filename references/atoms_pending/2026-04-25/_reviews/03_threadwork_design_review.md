# Exhaustive Review — `03_threadwork_design`

**Topic:** Threadwork Design Synthesis (consolidated)
**Atoms:** 71
**Method:** strict ID-presence check in primary registers (definition-pattern aware: YAML `id: X-N` for ED/PP, `| T-N |` table-row or `## T-N` heading for T/M) + repo path-existence + substantive-claim extraction with best-match canon excerpt.

## Summary

### ID classification

- **DEFINED-IN-CANON:** present as a defined entry in primary register (YAML `id:` for ED/PP; table row or heading for T/M).
- **MENTIONED-IN-CANON:** appears in canon corpus but not as a primary-register definition (likely cross-reference or editorial marker).
- **PARTIAL:** defined in canon, but atom's discussion is materially richer.
- **NEW:** not present in any fetched canon file.

| status | count |
|---|---|
| DEFINED-IN-CANON | 9 |
| MENTIONED-IN-CANON | 19 |
| PARTIAL | 0 |
| NEW | 0 |

### Path verification

| status | count |
|---|---|
| EXISTS | 30 |
| MISSING-FROM-REPO | 1 |

### Substantive claims surfaced: 137

## ID-by-ID comparison

### ED-129 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/combat.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__109__ii-8-architecture-weaknesses-mechanical`):
  > e as-is 2. **Mass combat incomplete** — 14 PROVISIONAL = S ✗ 3. **Five+ unreviewed systems** — Companion, Player Agency, Derived Stats, Caste, Royal Assassination 4. **Ranged weapon dual taxonomy** — ED-129 open 5. **CI/Accounting density** — 7 nested in 10 steps (player-facing concern, see Part III) 6. **Thread-Read Fatigue cost unspecified** — potential degeneracy 7. **Stamina formula conflict**
- **canon context** (`params/combat.md`):
  > -         damage formula revised (armour-dependent modifier); Mass Mismatch exemptions corrected; --> <!--         Close/Far zone terminology flagged ED-129 (open). Stage 1/2 struck ED-130. Reach zone flagged ED-129 (open). -->  # params_combat.md — Personal Combat  ## Pool Formula Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5) Stamina = Endurance × 5 (ED-694 canonical; PP-611 supe

### ED-539 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/audit/valoria_systems_workplan.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_consolidation__13__4-5-rendering-strain-substrate-posture-cost`):
  > ## 4.5 Rendering Strain (Substrate-Posture Cost)  **The gap.** `tc_political_redesign_v30` addresses Church dominance (53% wins per simulation) through TC ceiling extension and milestone-gating. ED-539 (P1) flags the compound effect of TC reform + TCV revaluation + Seizure Accord ≥ 2 as unsimulated. Whether the redesign sufficiently addresses dominance is unknown.  **The proposal.** Alternative or
- **canon context** (`designs/audit/valoria_systems_workplan.md`):
  > erged into victory_v30. Hafenmark Parliamentary alternate struck but replacement not fully specified.  **Outstanding:** ED-538 (compound simulation). ED-539 (TC reform compound). J-6 (Seizure Ob). Starting PT values (provisional).  ---  # S08 — TC POLITICAL REDESIGN  ## B. File Index  | File | Repo | Role | |------|------|------| | designs/board_game/tc_political_redesign_v30.md | ttrpg | CI miles

### ED-663 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/scene/derived_stats_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__85__16-4-belief-revision-and-scars`):
  > *R** ✓ Progressive destabilization — each Scar makes the NPC more unpredictable and more vulnerable (more RS active). **E** ✓ Four states from one counter.  ### 16.4b Thread → Conviction Scar Matrix (ED-663)  7 Thread event types × 7 Convictions. Faith Scars from any Thread op except Mending. Mending never Scars anyone. Certainty scaling: C5 = +1 severity, C0 = −1 severity. Season cap: 1/NPC.  **N
- **canon context** (`designs/scene/derived_stats_v30.md`):
  > ld - Haushalt Competence bonus: +Competence × 25 gold/season (Competence 0–3). Cap: Haushalt Competence income cannot exceed Wealth × 50 per season. (ED-663 resolution) - Campaign Supply (units in hostile territory): −100 gold/season - Siege (attacker): −100 gold/season per active siege - Muster (Levy): −50 gold - Muster (Professional): −150 gold - Muster (Heavy Infantry/Cavalry): −300 gold - Must

### ED-664 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger_archive.yaml`.
- **atom context** (`valoria_master_document__116__iv-1-verify-against-source`):
  > oes PP-528 explicitly address lapse vs. refusal? | params/bg/core.md (or wherever PP-528 lives) | | Spirit non-practitioner uses (DECISION-02) | I claimed 4 uses (Resolve, Sincerity Gate, Dissonance, ED-664). Verify all four exist. | params/core.md, params/threadwork.md, ED-664 | | 14 PROVISIONAL items in mass combat | Re-list and verify count | params/mass_combat.md | | Domain Echo floor-function
- **canon context** (`canon/editorial_ledger_archive.yaml`):
  > urce fluctuation, not direct -1 Stability stat damage)."     status: resolved     severity: P2    # Migrated 2026-04-24 from active ledger (ED-661/662/664/665/669/712 — resolved this session)   - id: ED-664     date: 2026-04-17     description: "Advisor-principal confidentiality boundary specified in npc_behavior §3.5. Three zones defined: private counsel (no consequence), public breach (Dispositi

### ED-665 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger_archive.yaml`.
- **atom context** (`valoria_master_document__85__16-4-belief-revision-and-scars`):
  > A Faith NPC Scars from Weaving. An Equity NPC Scars from Lock-on-a-being. **S** ✓ Parallel to Certainty movement triggers but targets a different track.  ### 16.4c Practitioner Coherence Thresholds (ED-665)  | Coherence | Rule | |---|---| | 10–6 | Operate freely. | | 5 | Defensive ops only. | | 4–3 | Cease Thread ops. Exception: MS ≤ 20 Wardens → Mending only. | | 2 | Seek withdrawal. | | 1 | Cris
- **canon context** (`canon/editorial_ledger_archive.yaml`):
  > s deduplication: settlement-events at same settlement same season collapse into single Mandatory entry. Source: 2026-04-24 audit §3.5."     status: resolved     severity: P3    # Migrated 2026-04-24: ED-665 resolved   - id: ED-665     date: 2026-04-17     description: "Grand Contest as succession trial not in canonical docs. Resolved 2026-04-24: social_contest §7.2 added — Succession Contest speci

### ED-668 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger_archive.yaml`.
- **atom context** (`valoria_master_consolidation__35__phase-x-vertical-slice-playtest-iteration`):
  > the abstract. Annual playtests catch design drift before it compounds.  ---  # 8. ACKNOWLEDGED GAPS  What these recommendations don't address. Honesty requires noting what's missing.  - **P0 blockers ED-668–672** (Thread horizontal integration from stress register). Workplan Phase 0.6 handles. Recommendations don't extend. - **Compilation staleness.** Player-facing-documentation work, downstream o
- **canon context** (`canon/editorial_ledger_archive.yaml`):
  > 6-04-24 from active ledger   - id: ED-660     date: 2026-04-17     description: "Certainty scale: Almstedt Certainty 6→4 (Jordan-confirmed 2026-04-23)."     status: resolved     severity: P2    - id: ED-668     date: 2026-04-17     description: "MS decline rate calibration — resolved by MS trajectory v1 (f2b5d143) and references/ms_budget.md. Baseline upward pressure ~0.2 MS/year from Warden contr

### ED-694 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/provincial/mass_battle_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__09__2-1-attributes-10-range-1-7`):
  > the floor formula. The divergence is presumably intentional (Disposition scales faster than Knot capacity). **STALE-07: Document the rationale for the formula split.**  ### 2.1b Focus — Role Change  ED-694 replaced "Contact Rounds = Focus" with "Thread Fatigue = Spirit × 5" and "ops/session = Focus − 1". Old Focus role (contact duration) is gone. **STALE-08: Verify all docs referencing old Contact
- **canon context** (`designs/provincial/mass_battle_v30.md`):
  > rritorial | | Campaign | ~1,000 soldiers | Territorial | | War | ~5,000 soldiers | Structural |  Scale sets **block_size** for TroopCount derivation (ED-694):  | Scale | block_size | |-------|-----------| | Skirmish | 10 | | Company | 100 | | Battle | 500 | | Campaign | 1,000 | | War | 5,000 |  **TroopCount = Size × block_size** (set at muster). Size becomes a computed integer: `Size = floor(Troop

### ED-738 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/audit/gameplay_assessment_2026_04_21.md` but not as a defined entry in primary register.
- **atom context** (`master_consolidation__02__2-ed-738-ein-sof-gradient-editorial`):
  > ## §2 ED-738 — Ein Sof gradient editorial  **Path:** `designs/audit/editorial_ein_sof_gradient_2026_04_21.md` **Commit:** `d80e1532` **Scope:** Establishes interpretive framing for canonical material; does not introduce new canonical mechanics.  ### §2.1 Three over-readings corrected  **Consciousness absent dur
- **canon context** (`designs/audit/gameplay_assessment_2026_04_21.md`):
  > **Verdict.** G-texture — but foundational texture. Without P4, post-Leap narrative defaults to ineffabilist or categorical registers that contradict ED-738. The texture is load-bearing for scene-writing and dialogue-generation, so its absence would be felt systemically even though it forces no decisions directly.  #### P11 — Ambient narrative self as faction differentiator **Decisions forced.** No

### ED-777 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger_archive.yaml`.
- **atom context** (`valoria_session_2026-04-25_master__05__section-5-cross-reference-audit`):
  > ` — historical preservation references, acceptable, not fixed.  Plus `social_contest L268` and `faction_politics L659`: `npc_behavior §3.2` → `§3.3` (Scar Accumulation, not Belief Revision). Fixed in ED-777.  All non-deprecated cross-references valid after these commits.  ---
- **canon context** (`canon/editorial_ledger_archive.yaml`):
  > set 1 season). Appeal mechanism added (2-season window, faction-internal Conviction Track, no appeal for Dismissal). Source: 2026-04-25 stress-test 33."     status: resolved     severity: P3    - id: ED-777     date: 2026-04-25     description: "Caste-transgressive Conviction PC mechanic specified (faction_politics §3.6.1 + §3.6.2). Closes spec gap surfaced by stress-test 46: §3.6 referenced 'elev

### M-7 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `references/throughlines_meta.md`.
- **atom context** (`master_consolidation__02__2-ed-738-ein-sof-gradient-editorial`):
  > ical-trauma phenomenology) into composite operational architecture. Composite is framework-original in assembly and substrate-ontological deployment; components have clean precedent. Meta-throughline М-7 captures this. Audit framing of "framework exceeds sources" corrected to "framework assembles specific components operationally."  ---
- **canon context** (`references/throughlines_meta.md`):
  > s pressure | Μ-α, Μ-δ | | М-3 | Substrate grounds all | Μ-γ | | М-4 | Institutions stake substrate-postures | Μ-γ | | М-5 | Scales connect through substrate | Μ-δ | | М-6 | Choice is forced | Μ-α | | М-7 | Borrowings are operational extensions (composite assembly) | Μ-γ, Μ-β | | М-8 | Access is vertical-position gated (within the renderable) | Μ-β, Μ-γ | | М-9 | Ontological inversion of clinical p

### M-8 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `references/throughlines_meta.md`.
- **atom context** (`master_consolidation__02__2-ed-738-ein-sof-gradient-editorial`):
  > differently. Canon/00 Inseparability does not support different-givens-per-observer. T-27 four-faction interpreter operates on what was received; T-30 information asymmetry is access-mode asymmetry; М-8 vertical-position-gated access governs what can be received.  ### §2.3 Iceberg gameplay conceptualisation authorised  Canon/01 Am 3 establishes waterline-language as canonical. ED-738 §4 authorises
- **canon context** (`references/throughlines_meta.md`):
  > ns stake substrate-postures | Μ-γ | | М-5 | Scales connect through substrate | Μ-δ | | М-6 | Choice is forced | Μ-α | | М-7 | Borrowings are operational extensions (composite assembly) | Μ-γ, Μ-β | | М-8 | Access is vertical-position gated (within the renderable) | Μ-β, Μ-γ | | М-9 | Ontological inversion of clinical phenomenology | Μ-γ, Μ-α | | М-10 | Environment as constitutive medium (bounded b

### PP-109 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/architecture/scale_transitions_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__58__10-2-domain-echo-the-upward-pipe`):
  > **Amount:** OW ±2, Success ±1, Partial narrative, Failure −1 own stat. **Cap:** One Echo/scene/faction (PP-329). **Timing:** Immediate (TTRPG) or queued to Accounting (Hybrid — intentional asymmetry PP-109).  **Three Echo types:** Standard (§5.2), Accord (±1 per territory per Zoom In), Thread (faction Stability/Mandate from Thread events with Thread Significance).  **N** ✓ **Without Domain Echo, p
- **canon context** (`designs/architecture/scale_transitions_v30.md`):
  > Timing by Mode - **Full TTRPG (Register Shift):** Domain Echo fires immediately at scene end. No extra roll.  This timing difference is intentional (PP-109): Zoom In is a personal intervention in a strategic situation. Faction consequences propagate through seasonal accounting to prevent real-time manipulation of BG stats from personal scenes.  ### §5.4 Debate → Domain Echo (PP-108) | Conviction T

### PP-238 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/factions/stats_1_7_scale.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__102__ii-1-stale-references-10-items`):
  > ---------|-------|-----| | STALE-01 | CSR §3 | Composure = Cha + 6 | Update to Cha × 3 (ED-694) | | STALE-02 | PP-275 | Stamina = End+H+1−armour | Strike. ED-694 (End × 5) is canonical | | STALE-03 | PP-238 | Feint = full pool, Def = 0 | Strike. PP-294 (partial commitment) is canonical | | STALE-04 | params/bg/core.md | Faction Assignment table duplicated | Remove duplicate | | STALE-05 | params/c
- **canon context** (`params/factions/stats_1_7_scale.md`):
  > ent.  --- <!-- PP-236 applied 2026-04-04: Crown covert actions rule --> <!-- PP-237 applied 2026-04-04: Public Instability Hybrid definition --> <!-- PP-238 applied 2026-04-04: Lowenritter reactive Military NPC guidance --> <!-- PP-241 applied 2026-04-04: Crown-Lowenritter covert delegation rule (PROVISIONAL) --> <!-- PP-244 applied 2026-04-04: Scene→Mass transition modifier table (PROVISIONAL) --

### PP-243 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/factions/stats_1_7_scale.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__08__1-6-momentum-0-4`):
  > um (0–4)  Gain: Overwhelming OR Belief achieved. Spend: 1 = 1 auto-success (non-Thread only). Reset: session start. Carries within session. Auto-successes are additive with roll; 1-faces cancel them (PP-243).  **N** ✓ Converts exceptional performance to future reliability. **R** ✓ Cap 4. Session reset prevents hoarding. Non-Thread restriction prevents trivializing metaphysical ops. **E** ✓ Five va
- **canon context** (`params/factions/stats_1_7_scale.md`):
  > own interest |  ## PP-242 — Seasonal cap timing  ±2 cap applied at accounting. Multiple actions within a season tally; net clipped at accounting.  ## PP-243 — Royal Decree partial-sheet  Decree may only target stats present on target faction's sheet.  ## PP-244 — PC excommunication succession  Excommunicated PC faction leader: faction reverts to NPC institutional tendency until PC reinstated (Reve

### PP-255 — **MENTIONED-IN-CANON**

- **detail:** Appears in `references/propagation_log.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__25__4-6-key-sub-mechanics`):
  > e vs Church: Church Stability +1.  **Evidence Integration (PP-636):** 1 Finding = +1D E1. 2+ = +2D (cap). Stacks with prep (+1D). Max E1 bonus: +3D. Cross-system fieldwork→contest link.  **Stalemate (PP-255):** Max 10 exchanges. Forced Unmask after 10. Prevents infinite contests.  **Let It Ride:** Resolved questions cannot be re-contested without changed circumstances. One rule.  ---  # 5. THREADW
- **canon context** (`references/propagation_log.md`):
  > Domain Action Ob formula, ethical framework modifiers | REFERENCE | | `gm_ref/arcs_46_55_consolidated.md` | `references/params_threadwork.md` | Cites PP-255, Leap table, Contact Duration, Coherence | REFERENCE | | `gm_ref/arcs_46_55_consolidated.md` | `references/params_board_game.md` | Cites PI track, Coup Counter, Torben/Elske Loyalty, PP-563 VTM-TC | REFERENCE | | `gm_ref/arcs_46_55_consolidate

### PP-261 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/board_game.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__85__16-4-belief-revision-and-scars`):
  > 5 | Defensive ops only. | | 4–3 | Cease Thread ops. Exception: MS ≤ 20 Wardens → Mending only. | | 2 | Seek withdrawal. | | 1 | Crisis. Arc transition fires. +2 Ob all Thread. | | 0 | NPC Transition (PP-261). |  **N** ✓ NPC practitioners self-regulate based on Coherence. **R** ✓ The Warden MS override at Coherence 4–3 means Wardens will Mend themselves to destruction when the world is failing. Con
- **canon context** (`params/board_game.md`):
  > utions.md)  ~2,517 tokens    - Balance Findings — Status Update   - Concurrent Zoom In — Ordering (ED-072 resolved 2026-04-03)   - ED-019 Resolution (PP-261) [FLAGGED FOR DESIGNER REVIEW]   - ED-056 Resolution (PP-268)   - ED-072 Resolution (PP-269)   - ED-080 Resolution (PP-270)   - ED-081 Resolution (PP-271)   - ED-083 Resolution (PP-272)   - ED-085 Resolution (PP-273)   - ED-086 Resolution (PP-

### PP-275 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/combat.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__102__ii-1-stale-references-10-items`):
  > ## II.1 Stale References (10 items)  | # | Location | Issue | Fix | |---|----------|-------|-----| | STALE-01 | CSR §3 | Composure = Cha + 6 | Update to Cha × 3 (ED-694) | | STALE-02 | PP-275 | Stamina = End+H+1−armour | Strike. ED-694 (End × 5) is canonical | | STALE-03 | PP-238 | Feint = full pool, Def = 0 | Strike. PP-294 (partial commitment) is canonical | | STALE-04 | params/bg/core.md | Fact
- **canon context** (`params/combat.md`):
  > minimum.  ## PP-274 — Multi-engagement pool split Target declares one Offence/Defence split; both attackers roll against same Defence allocation.  ## PP-275 — Stamina maximum Stamina capped at base value (End + H + 1 − armour mod). Take a Breath restores Endurance score, capped at base.  ## PP-276 — Initiative mixed outcome Both succeed at different priorities → initiative stays with current holde

### PP-294 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/board_game.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__07__1-5-pool-minimum-1d`):
  > inimum (1D)  No penalty reduces pool below 1D. Universal. 1D at TN 7 = ~40% at Ob 1. Characters are never mechanically helpless.  **N** ✓ **E** ✓ One rule. No exceptions. **S** ✓ Confirmed in combat (PP-294), contest (Rattled+Spent), fieldwork, threadwork.
- **canon context** (`params/board_game.md`):
  > REVIEW]   - BG Overwhelming Threshold — Final (PP-281 / PP-299)   - ED-056 Resolution (PP-293) — Zoom In TC Win-Delay Exploit   - ED-072 Resolution (PP-294) — Concurrent Zoom In Ordering   ... +9 more headings  ## [params_bg_faction_actions.md](references/params_bg_faction_actions.md)  ~4,793 tokens    - Faction Unique Actions — Board Game (PP-428–442, 2026-04-07)     - Church — Piety Spread (PP-4

### PP-329 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/architecture/scale_transitions_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__58__10-2-domain-echo-the-upward-pipe`):
  > combat vs faction officer, Disp +4/+5 with officer, settlement governance changing Order ±1).  **Amount:** OW ±2, Success ±1, Partial narrative, Failure −1 own stat. **Cap:** One Echo/scene/faction (PP-329). **Timing:** Immediate (TTRPG) or queued to Accounting (Hybrid — intentional asymmetry PP-109).  **Three Echo types:** Standard (§5.2), Accord (±1 per territory per Zoom In), Thread (faction St
- **canon context** (`designs/architecture/scale_transitions_v30.md`):
  > ory → Settlement governance → Disposition reach → Investigation completion → Faction-leader-direct → Other. Cap: 1 Domain Echo per faction per scene (PP-329). See §5.5 (Accord Domain Echo) and §5.6 (Thread Domain Echo) for the full Echo specifications.  [EDITORIAL: ED-748 — §3.4 stub filled with forward-reference. Source: 2026-04-24 audit §3.12.]  ### §3.5 Thread → Faction Thread operation targeti

### PP-528 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/provincial/victory_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__116__iv-1-verify-against-source`):
  > ION-14) | How are Evidence (+2D) and positional (+5D) caps related? | designs/scene/fieldwork_v30.md §2.5; designs/npcs/npc_behavior_v30.md §6.5 | | Crown Treaty re-sign cooldown (DECISION-15) | Does PP-528 explicitly address lapse vs. refusal? | params/bg/core.md (or wherever PP-528 lives) | | Spirit non-practitioner uses (DECISION-02) | I claimed 4 uses (Resolve, Sincerity Gate, Dissonance, ED-6
- **canon context** (`designs/provincial/victory_v30.md`):
  > re: Crown Stability −1.  **Treaty period:** 4 seasons. Either party may extend (action, no roll) or let lapse. Lapse is not betrayal. **Lapse timing (PP-528):** Treaty lapse occurs at Phase 1 of the season after the period ends. Treaty formed Season N lapses at Phase 1 of Season N+5. Accounting of Season N+4 sees the Treaty as active. Extension must be declared at Phase 1 of Season N+5. **Hybrid D

### PP-614 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/contest.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__25__4-6-key-sub-mechanics`):
  > ## 4.6 Key Sub-Mechanics  **Appraise (PP-614):** Att + Rec, TN 7, Ob = opponent Cha ÷ 2. Graduated results (misleading → boost + detail). Clean after consolidation.  **Resonant Style Targeting:** Appraise OW reveals RS. +1D + style-specific bonus. Wrong-Style vs Church: Church Stability +1.  **Evidence Integration (PP-636):** 1 Finding = +1D
- **canon context** (`params/contest.md`):
  > -242, PP-245, PP-253–259, PP-272, PP-278–279, PP-378, PP-390–395, PP-349, PP-351, PP-401, PP-449–450, PP-452–458, PP-460–463, PP-465, PP-529, PP-612, PP-614 --> <!-- PP-234: Full system redesign. Genre restructure (3→2), attribute renames (Presence→Charisma, Memory→Recall), --> <!--         Composure = Charisma + 6, faction boost revision (4 single-axis options), integer bonus dice, --> <!--      

### PP-616 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/factions/stats_1_7_scale.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__26__5-1-thread-pool`):
  > ## 5.1 Thread Pool  Pool = (Spirit × 2) + History + TPS. TPS = floor(TS / 10). Single formula ALL Thread ops (PP-616).  **N** ✓ **E** ✓ Same (Attr × 2) + H + bonus pattern. **S** ✓ No exceptions.
- **canon context** (`params/factions/stats_1_7_scale.md`):
  > /sabotage/assassination functions distributed to settlement-level intelligence brokers.   ### Restoration Movement — Community Weaving [SUPERSEDED by PP-616]  > **SUPERSEDED:** This spec is superseded by `params/threadwork.md` PP-616 (Community Organizing — Canonical Pool). PP-616 unifies all Thread operations under a single pool formula: `(Spirit × 2) + History + TPS`, supersedes the Influence-po

### PP-636 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/contest.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__25__4-6-key-sub-mechanics`):
  > g → boost + detail). Clean after consolidation.  **Resonant Style Targeting:** Appraise OW reveals RS. +1D + style-specific bonus. Wrong-Style vs Church: Church Stability +1.  **Evidence Integration (PP-636):** 1 Finding = +1D E1. 2+ = +2D (cap). Stacks with prep (+1D). Max E1 bonus: +3D. Cross-system fieldwork→contest link.  **Stalemate (PP-255):** Max 10 exchanges. Forced Unmask after 10. Preven
- **canon context** (`params/contest.md`):
  > r effects) cannot raise Concentration above this maximum. Source: SIM-DB-STRESS-01 D-08b finding. 2026-04-09.  ## Evidence Track Findings in Contest (PP-636)  Findings from completed fieldwork investigations may be cited in Contest opening (§9.1).  | Findings cited | Exchange 1 bonus | |---|---| | 1 Finding | +1D | | 2+ Findings | +2D (cap) |  Findings are **not consumed** by citation — remain on 

### PP-642 — **MENTIONED-IN-CANON**

- **detail:** Appears in `references/propagation_log.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__119__v-1-companion-system-gap-05`):
  > **Sources to fetch:** `designs/npcs/companion_specification_v30.md` (referenced in NPC behavior doc).  **Review questions:** - How are companions acquired? Disposition gates, recruitment procedure (PP-642), Standing thresholds? - How do companions advance? Independent character sheets or attached to player? - How does companion death/loss interact with Knots (Loss = Coherence −1)? - What is the co
- **canon context** (`references/propagation_log.md`):
  > ) |  ## PP-641–642 Propagation (2026-04-13)  ### PP-641 — Opposing Operations → threadwork design doc | Source | Target | Status | |---|---|---|  ### PP-642 — NPC Recruitment | Source | Target | Notes | |---|---|---| | `designs/systems/npc_behavior_v30.md` §9.5 | `references/params_contest.md` | Findings citation extracted ✓ | | `designs/systems/npc_behavior_v30.md` §9.5 | `references/params_comba

### PP-674 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/patch_register_active.yaml`.
- **atom context** (`valoria_master_consolidation__04__2-4-recent-canonical-strikes`):
  > aynard mechanic (incompatible with military-conqueror identity). - **Niflhel dissolved.** - **Mass Seizure probabilistic (2026-04-19):** P = ((CI-60)/40)^3.3, 1% at CI 70, 100% at CI 100. - **Tier N (PP-674):** Necessity test added 2026-04-19. Existing canon grandfathered.
- **canon context** (`canon/patch_register_active.yaml`):
  > ts/valoria_hooks.py     - skills/valoria-atomizer/SKILL.md     - skills/valoria-simulator/SKILL.md     - 75 auto-generated *_skeleton.md → *_index.md   status: applied   applied_commit: pending - id: PP-674   date: 2026-04-19   severity: P1   description: "Framework enforcement + tier N (Necessity Test). Adds vetting_gate     to valoria_hooks.py, new task type design_proposal, new tier N (subject-

### PP-684 — **MENTIONED-IN-CANON**

- **detail:** Appears in `references/propagation_log.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__09__2-1-attributes-10-range-1-7`):
  > barely use it (Sincerity Gate only). This creates a binary: practitioner tax. **DECISION-02: Confirm this is the intended balancing cost for Thread power.**  ### 2.1a Bonds — Dual Formula Divergence  PP-684 revised Disposition ceiling to flat `Bonds`. Knot max count remains `floor(Bonds/2)+1`. Previously both used the floor formula. The divergence is presumably intentional (Disposition scales fast
- **canon context** (`references/propagation_log.md`):
  > 30.md` (ED-629 dependency) | `designs/systems/faction_politics_expanded_v1.md` §2.7 | ED-629 Thread stress resolution may require Warden audit |  ### PP-684 — Disposition ceiling = Bonds (was floor(Bonds/2)+1) | Source | Target | Status | |--------|--------|--------| | references/params_core.md (Bonds definition) | designs/fieldwork/fieldwork_v30.md §5.1 | DONE | | references/params_core.md (Bonds

### T-27 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `references/throughlines_meta_infill.md`.
- **atom context** (`master_consolidation__02__2-ed-738-ein-sof-gradient-editorial`):
  > TS expansion is expansion of what can be received from a given substrate, not what is given to different observers differently. Canon/00 Inseparability does not support different-givens-per-observer. T-27 four-faction interpreter operates on what was received; T-30 information asymmetry is access-mode asymmetry; М-8 vertical-position-gated access governs what can be received.  ### §2.3 Iceberg gam
- **canon context** (`references/throughlines_meta_infill.md`):
  > onal standings into institutional reality. |  | T-26 | Recursion as Setting Structure (TL-3) | М-5 | М-3 | Primary scale-recursive (same dynamic at multiple scales). Secondary substrate-grounded. | | T-27 | Effects Real, Explanation Wrong (TL-4) | М-4 | М-6 | Primary institutional (faction interpretive-frame coherent-but-wrong). Secondary forced-choice (argument fails; frame-crack requires confron

### T-30 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `references/throughlines_meta_infill.md`.
- **atom context** (`master_consolidation__02__2-ed-738-ein-sof-gradient-editorial`):
  > n substrate, not what is given to different observers differently. Canon/00 Inseparability does not support different-givens-per-observer. T-27 four-faction interpreter operates on what was received; T-30 information asymmetry is access-mode asymmetry; М-8 vertical-position-gated access governs what can be received.  ### §2.3 Iceberg gameplay conceptualisation authorised  Canon/01 Am 3 establishes
- **canon context** (`references/throughlines_meta_infill.md`):
  > Cracker (TL-8) | М-4 | М-8 | Primary institutional (Baralta's partial prophylaxis-crack is formation-structural). Secondary access-gated (crack admits substrate content into receptive capacity). | | T-30 | Information Asymmetry as Core Mechanic (TL-7) | М-8 | М-5 | Primary access-gated (different receptive capacities at different observer-nodes). Secondary scale-recursive (asymmetry operates at al

## Path verification

| path | status | atom occurrences |
|---|---|---|
| `params/core.md` | EXISTS | 4 |
| `params/bg/core.md` | EXISTS | 4 |
| `params/threadwork.md` | EXISTS | 3 |
| `designs/npcs/npc_behavior_v30.md` | EXISTS | 3 |
| `designs/threadwork/threadwork_v30.md` | EXISTS | 2 |
| `params/mass_combat.md` | EXISTS | 2 |
| `designs/scene/fieldwork_v30.md` | EXISTS | 2 |
| `designs/provincial/peninsular_strain_v30.md` | EXISTS | 2 |
| `designs/audit/editorial_ein_sof_gradient_2026_04_21.md` | EXISTS | 1 |
| `designs/architecture/core_experiential_moments.md` | MISSING-FROM-REPO | 1 |
| `params/combat.md` | EXISTS | 1 |
| `params/contest.md` | EXISTS | 1 |
| `params/scale_transitions.md` | EXISTS | 1 |
| `designs/territory/settlement_layer_v30.md` | EXISTS | 1 |
| `designs/npcs/companion_specification_v30.md` | EXISTS | 1 |
| `designs/architecture/player_agency_v30_index.md` | EXISTS | 1 |
| `designs/scene/social_contest_v30.md` | EXISTS | 1 |
| `designs/scene/derived_stats_v30.md` | EXISTS | 1 |
| `designs/provincial/faction_politics_v30.md` | EXISTS | 1 |
| `designs/provincial/mass_battle_v30.md` | EXISTS | 1 |
| `designs/provincial/faction_layer_v30.md` | EXISTS | 1 |
| `designs/provincial/victory_v30.md` | EXISTS | 1 |
| `designs/architecture/scale_transitions_v30.md` | EXISTS | 1 |
| `designs/architecture/campaign_architecture_v30.md` | EXISTS | 1 |
| `designs/architecture/player_agency_v30.md` | EXISTS | 1 |
| `params/factions_personal.md` | EXISTS | 1 |
| `params/bg/npc_priority_trees.md` | EXISTS | 1 |
| `references/glossary.md` | EXISTS | 1 |
| `references/canonical_sources.yaml` | EXISTS | 1 |
| `canon/editorial_ledger.yaml` | EXISTS | 1 |
| `canon/editorial_ledger_archive.yaml` | EXISTS | 1 |

## Substantive claim findings

_137 substantive claims (max 3 per atom) with best-match canon excerpts._

### Matched claims (103)

- **atom** `master_consolidation__02__2-ed-738-ein-sof-gradien`
  - claim: > Canon/01 Am 3 explicit: TS measures how much of the below-waterline Thread-substrate the practitioner can perceive and deliberately operate upon.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 6/8)
  - canon excerpt: > form: (Spirit × 2) + relevant History bonus + Thread Pool Score.** > Ob tables in this document predate the three-axis Ob system (PP-622/PP-623). > **Canonical Ob values: params_threadwork.md §Three-Axis Ob System.**  ## SETTLEMENT-LEVEL THREAD CONSE

- **atom** `master_consolidation__02__2-ed-738-ein-sof-gradien`
  - claim: > Only the knots themselves (canon/02 Am 2) lodge below reflexive-access threshold.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 6/8)
  - canon excerpt: > recedes Leap):** - **Round 2+:** Operations proceed as declared. - **Round (Focus + 1):** Contact drops. Rendering reasserts. Practitioner returns to themselves.  **Operations per Focus:**  | Focus | Contact Rounds (legacy) | Operation Rounds (legacy

- **atom** `master_consolidation__02__2-ed-738-ein-sof-gradien`
  - claim: > Cartographic-contemplative register applies in Regimes 1–3; apophatic register applies only at Regime 4 (Ein Sof structural terminus).
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/8)
  - canon excerpt: > cene at season end: Spirit pool, TN 7, Ob 2.   - Success: Approach Training tag granted. Trainee gains 1 Thread Sensitivity (the formal Leap exposure registers as substrate engagement per §3.2).   - Partial: tag granted at next Accounting (one additi

- **atom** `master_consolidation__11__11-methodological-notes-`
  - claim: > **Pattern guard.** Mystical-tradition training priors drift toward ineffabilist, pure-apophatic, and consciousness-absent readings when phenomenological framework cues trigger.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/8)
  - canon excerpt: > ack | Haiku | | 9 | Update hybrid mode branching catalogue | Haiku | | 10 | Solmund rename + AG→AS + Church rename (all files) | Haiku | | 11 | Canon guard pass on complete redesign | Sonnet |  

- **atom** `master_consolidation__11__11-methodological-notes-`
  - claim: > **Iceberg conceptualisation.** Authorised by ED-738 §4 for design-team gameplay-conceptualisation use only.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 2/7)
  - canon excerpt: > <!-- SKELETON — mechanical spec only — atomized 2026-04-13 from designs/ttrpg/threadwork_v30.md --> <!-- Infill: designs/ttrpg/threadwork_v30_infill.md --> <!-- DO NOT add prose. Rationale/examples live in the infill file. -->  <!-- v30 baseline — re

- **atom** `threadwork_master__00__preamble`
  - claim: > Awaits Jordan approval at flagged decision points.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 3/6)
  - canon excerpt: > 2.6 ## Date: 2026-03-27 (revised 2026-04-02) ## Authority: Philosophical Foundations (immutable) → this document (design proposal, requires editorial approval) ## Version: v3.2 — Part Nine (S-01–S-06 / P-11–P-26) applied in-place. All appendix sectio

- **atom** `threadwork_master__01__i-foundational-stance`
  - claim: > Foundational stance

### I.1 What this document does not claim

This document does not claim to know what threads are at the substrate-origin level.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 6/8)
  - canon excerpt: > 2026-04-25 stress-test 30 propagation defect.]   ## 2.2 Diagnosis — STRUCK (ED-134/ED-124, 2026-04-03)    ## 2.3 The Leap — Suspending Rendering  > **Foundational reference (canon/02).** The Leap's suspension target (layer 2 reflexive facing), the me

- **atom** `threadwork_master__01__i-foundational-stance`
  - claim: > The substrate emerges from Ein Sof, which canon (§1.2) names as *infinitely constituted yet epistemically inaccessible*: not a void, not a chaos, not a structureless ground, but a fullness that exceeds all description because all description is downs
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/8)
  - canon excerpt: > f scale or outcome. - **Cataclysmic Mass Battle** (player-tagged at scene setup, extraordinary circumstances): −2 MS. - **Mass Battle in destabilized substrate** (MS ≤ 10): −1 MS base, plus Stability Check (Ob 3) — failure adds −1 MS (maximum −2/batt

- **atom** `threadwork_master__01__i-foundational-stance`
  - claim: > The middle admits cartographic description under depth-and-condition-dependent constraints (per ED-738 — graduated specificity decay terminating at structural limit).
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/8)
  - canon excerpt: > ng, Locking, Dissolution, Mending). The substrate is legible to them but their rendering does not have the trained capacity to suspend. - Eligible to undergo training as described above.  **Loss of tag:**  - Approach Training is generally permanent o

- **atom** `threadwork_master__03__iii-what-the-player-should-`
  - claim: > What the player should feel

The player should feel that they are encountering a world that is thicker than they had thought, that has an order beneath its surface they can partially perceive but never fully understand, that responds to action in way
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/8)
  - canon excerpt: > r is replaced by a flat additive model:  - **Standard Mass Battle:** −1 MS per battle, regardless of scale or outcome. - **Cataclysmic Mass Battle** (player-tagged at scene setup, extraordinary circumstances): −2 MS. - **Mass Battle in destabilized s

- **atom** `threadwork_master__03__iii-what-the-player-should-`
  - claim: > They should feel that operations on this world have weight before they have cost — that the act of *touching* something at substrate depth changes both the toucher and the touched in ways neither can fully account for.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 7/8)
  - canon excerpt: > 622/PP-623). > **Canonical Ob values: params_threadwork.md §Three-Axis Ob System.**  ## SETTLEMENT-LEVEL THREAD CONSEQUENCES (Throughline T1)  Thread operations at Relational scale or above produce settlement-level stat consequences alongside provinc

- **atom** `threadwork_master__03__iii-what-the-player-should-`
  - claim: > They should feel, by the end of the campaign if they have travelled far enough, that what they have learned to do is itself a kind of intimacy with what cannot be described.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 6/8)
  - canon excerpt: >  | Object |    > **Mass battle Mending Stability cost note (ST-TW-03):** **Finding from sim_x_03_massbattle_thread.md** **[DESIGN NOTE]** **[STRUCK — campaign_architecture_v1 §3.1]** The ×3 MS multiplier is replaced by a flat additive model:  - **Sta

- **atom** `threadwork_master__04__iv-three-stories-the-system`
  - claim: > Three stories the system produces

### IV.1 The Mender's Burden

A practitioner mends faithfully for years.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 5/8)
  - canon excerpt: >  + Thread Pool Score.** > Ob tables in this document predate the three-axis Ob system (PP-622/PP-623). > **Canonical Ob values: params_threadwork.md §Three-Axis Ob System.**  ## SETTLEMENT-LEVEL THREAD CONSEQUENCES (Throughline T1)  Thread operations

- **atom** `threadwork_master__05__v-operations-what-threadwor`
  - claim: > Each operation tagged restorative, manipulative, or destructive per canon/02 Amendment 3.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 7/7)
  - canon excerpt: > Incorporates Leap-as-rendering-suspension. Supersedes v1.  ---  ---  ## CANONICAL POOL NOTICE (PP-616, PP-618, PP-619, PP-624, PP-625) > **All Thread operation pool formulas in this document have been updated to the canonical > post-PP-619 form: (Spi

- **atom** `threadwork_master__05__v-operations-what-threadwor`
  - claim: > Zero Coherence cost (canon Amendment 3).
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 3/3)
  - canon excerpt: >  especially dangerous — chance-based, not multiplicative.  A practitioner performing Thread operations in mass battle pays the standard per-operation Coherence cost (−1/op at Relational+, 0 for Mending per asymmetry) but MS drain from battle is the f

- **atom** `threadwork_master__05__v-operations-what-threadwor`
  - claim: > *Tag depends on attunement.* |

### V.2 Manipulative

| Operation | Phenomenological character | Substrate-tendency relation |
|---|---|---|
| **Weaving (unattuned)** | Forcing pattern against substrate's tolerance without sufficient perception | Imp
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/8)
  - canon excerpt: > es editorial approval) ## Version: v3.2 — Part Nine (S-01–S-06 / P-11–P-26) applied in-place. All appendix sections eliminated. PP-632: §2.6 Opposing Operations added. ## Revision: Incorporates Leap-as-rendering-suspension. Supersedes v1.  ---  ---  

- **atom** `threadwork_master__08__viii-substrate-ontology-con`
  - claim: > The two-roll architecture's Roll 2 opacity is metaphysical fidelity, not information-design.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/6)
  - canon excerpt: >  |    > **Mass battle Mending Stability cost note (ST-TW-03):** **Finding from sim_x_03_massbattle_thread.md** **[DESIGN NOTE]** **[STRUCK — campaign_architecture_v1 §3.1]** The ×3 MS multiplier is replaced by a flat additive model:  - **Standard Mas

- **atom** `threadwork_master__08__viii-substrate-ontology-con`
  - claim: > This must be preserved against rationalising tendencies in design.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 2/5)
  - canon excerpt: > sserts violently — the body's damage overrides the suspension. Contact drops. (PP-624: corrected from Attunement. Maintaining Thread-state suspension against physical disruption is Spirit's function — metaphysical grounding while engaged — not Attune

- **atom** `threadwork_master__08__viii-substrate-ontology-con`
  - claim: > The system must never promise legibility it cannot deliver.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/6)
  - canon excerpt: > the canonical > post-PP-619 form: (Spirit × 2) + relevant History bonus + Thread Pool Score.** > Ob tables in this document predate the three-axis Ob system (PP-622/PP-623). > **Canonical Ob values: params_threadwork.md §Three-Axis Ob System.**  ## S

- **atom** `threadwork_master__09__ix-decisions-awaiting-jorda`
  - claim: > Decisions awaiting Jordan

Eleven decisions require Jordan-level authority per throughlines §10.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 2/8)
  - canon excerpt: > DWORK MECHANICS — v2.6 ## Date: 2026-03-27 (revised 2026-04-02) ## Authority: Philosophical Foundations (immutable) → this document (design proposal, requires editorial approval) ## Version: v3.2 — Part Nine (S-01–S-06 / P-11–P-26) applied in-place. 

- **atom** `threadwork_master__09__ix-decisions-awaiting-jorda`
  - claim: > No separate track."
- §5.9 ThS / CD eliminated: "→ Coherence (10→0).
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/4)
  - canon excerpt: > practitioner possesses at least one Einhir Text technique applicable to Mending   Pre-calculate the Leap pool on the character sheet as a named entry separate from History pools.  | Degree | Outcome | |---|---| | Overwhelming | Clean suspension. Next

- **atom** `threadwork_master__09__ix-decisions-awaiting-jorda`
  - claim: > Campaign tracking eliminated as separate system."
- "Epistemic seduction": "Cut — Coherence degradation."

These consolidations contradict canon/00 A3, A11, C2, C4 and canon/01 Amendment 3 (which explicitly states *Coherence is orthogonal to Thread S
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 8/8)
  - canon excerpt: > omething evil is happening to them. Because they have been outside rendering so many times that rendering no longer holds. | | 0 | Rendering Crisis | Campaign event. Reality as commonly rendered is no longer accessible. The practitioner's spooling is

- **atom** `valoria_master_consolidation__03__2-3-simulation-f`
  - claim: > 103-entry verification ledger covering 43 distinct canonical values.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/7)
  - canon excerpt: > r_histories §Formation, characters whose 2F slot is "Practitioner Mentorship" begin with Approach Training as a starting skill. This is the canonical entry route for player characters wanting Thread agency from session 1. - **In-campaign training (fu

- **atom** `valoria_master_consolidation__03__2-3-simulation-f`
  - claim: > Session 2 pending (territory model, Domain Action framework, Piety Yield, Strain propagation, mass combat, contests, faction AI).
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 6/8)
  - canon excerpt: > e unguided Leap leaves perceptual residue per A1/C1 inseparability).  **Effects of holding the tag:**  - Eligible to attempt §2.3 Leap operations (suspending rendering). - +1D on Leap rolls (per character_histories §270 Approach Training trait listin

- **atom** `valoria_master_consolidation__03__2-3-simulation-f`
  - claim: > Session 3 pending (threadwork, victory, scale transitions, NPC priority trees, arc transitions).
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/8)
  - canon excerpt: > e unguided Leap leaves perceptual residue per A1/C1 inseparability).  **Effects of holding the tag:**  - Eligible to attempt §2.3 Leap operations (suspending rendering). - +1D on Leap rolls (per character_histories §270 Approach Training trait listin

- **atom** `valoria_master_consolidation__04__2-4-recent-canon`
  - claim: > - **CR-STRIKE (2026-04-19):** Cultural Reformation removed as Vaynard mechanic (incompatible with military-conqueror identity).
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 3/8)
  - canon excerpt: > fy before rolling)  - Approach Training tag ✓ - Thread Sensitivity 30+ ✓ - Not incapacitated (Health > 0) (PP-232 — prior ceiling(Health÷2) threshold removed; incapacitation is binary under current wound system)   ### The Leap Roll  **Pool:** (Spirit

- **atom** `valoria_master_consolidation__08__2-8-per-system-q`
  - claim: > Combat, Thread Operations, Victory, Fieldwork, Social Contest, Player Agency, NPC Behavior all 8–9/10.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 7/8)
  - canon excerpt: >  rendered-level events — not practitioner operations but the thread events that combat, death, and substrate instability constitute:  | Observer TS | Combat Wound | Death | Mass Casualty | Gap Manifestation | Rendering Crisis | |---|---|---|---|---|-

- **atom** `valoria_master_consolidation__08__2-8-per-system-q`
  - claim: > Five Moments framework still genuine contribution (no prior work names touchstone moments) but framing must acknowledge what bridge accomplished |
| "Metaphysics is designer-facing not player-facing" | **Substantially true with caveat** | Bridge adde
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 5/8)
  - canon excerpt: > ement struck; all Leaps are Spirit-primary) **TN:** 7 **Ob:** Thread Sensitivity 30–49 = 2 · Thread Sensitivity 50+ = 1 · +1 Ob per Wound  > **Einhir framework (P-26):** "Einhir framework" appears as a prerequisite for Locked Zone border Mending (Ob 

- **atom** `valoria_master_consolidation__08__2-8-per-system-q`
  - claim: > Foundations §22.1 literal rendering still unimplemented — that gap remains |
| Specific numeric proposals (Rendering Strain at 5/10/15/20, Pamphlet Ob values, gunpowder Wealth costs) | **Placeholder-quality** | params/ directory unread; values labele
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 4/8)
  - canon excerpt: > ttrpg/threadwork_redesign_v25.md on 2026-04-13 --> # THREADWORK MECHANICS — v2.6 ## Date: 2026-03-27 (revised 2026-04-02) ## Authority: Philosophical Foundations (immutable) → this document (design proposal, requires editorial approval) ## Version: v

- **atom** `valoria_master_consolidation__09__4-1-the-five-mom`
  - claim: > Throughlines do not specify which *experiential* moments every campaign should produce — what the player carries with them when they stop playing.
  - best match: `designs/threadwork/threadwork_v30.md` (overlap 6/8)
  - canon excerpt: > ing books and documents, but it is NOT possible to truly EXPERIENCE or understand threadwork through rational/linguistic means. Thread Sensitivity is experiential, not intellectual. This means RM's cultural revival can reconstruct governance structur

_(73 more matched.)_

### Unmatched claims — possibly NEW or rephrased (34)

- atom `master_consolidation__11__11-methodological-notes-`: > ED-738 §10 codifies this discipline.
- atom `threadwork_master__06__vi-apparatus-what-the-pract`: > *Restored from threadwork_v30 Taint cut.* 0 → 10.
- atom `valoria_master_consolidation__04__2-4-recent-canon`: > - **Niflhel dissolved.**
- **Mass Seizure probabilistic (2026-04-19):** P = ((CI-60)/40)^3.3, 1% at CI 70, 100% at CI 100.
- atom `valoria_master_consolidation__04__2-4-recent-canon`: > - **Tier N (PP-674):** Necessity test added 2026-04-19.
- atom `valoria_master_consolidation__12__4-4-multi-perspe`: > Per P-03, no omniscient narrator is canonically possible.
- atom `valoria_master_consolidation__14__4-6-per-faction-`: > Klapp's awakening (canonical per `npc_faction_arc_interdependency §1.2`) is the seed.
- atom `valoria_master_consolidation__35__phase-x-vertical`: > 20–40 hours of play.
- atom `valoria_master_document__07__1-5-pool-minimum-1d`: > 1D at TN 7 = ~40% at Ob 1.
- atom `valoria_master_document__09__2-1-attributes-10-ran`: > Max 5 (one attr only, rest ≤ 4).
- atom `valoria_master_document__09__2-1-attributes-10-ran`: > **R** ✓ 31 points forces trade-offs.
- atom `valoria_master_document__09__2-1-attributes-10-ran`: > **E** ✓ Uniform 1–7 range.
- atom `valoria_master_document__109__ii-8-architecture-we`: > **Contest CLASH stalls at median** — P1 blocker, not implementable as-is
2.
- atom `valoria_master_document__109__ii-8-architecture-we`: > **Mass combat incomplete** — 14 PROVISIONAL = S ✗
3.
- atom `valoria_master_document__10__2-2-derived-scores`: > At 0: NPC transition.
- atom `valoria_master_document__119__v-1-companion-system`: > (Identified gap in gameplay audit GX-04.)
- atom `valoria_master_document__120__v-2-player-agency-co`: > (Fulfilled/Failed/Transformed/Unresolved per Portrait Retirement.)
- What is the Standing 0–5 ladder?
- atom `valoria_master_document__25__4-6-key-sub-mechanics`: > **Stalemate (PP-255):** Max 10 exchanges.
- atom `valoria_master_document__26__5-1-thread-pool`: > TPS = floor(TS / 10).
- atom `valoria_master_document__33__5-8-wr-wc`: > Mending Sanctuary at WC ≥ 2.
- atom `valoria_master_document__35__5-10-mending-communit`: > Competent (3–4): standard.
- atom `valoria_master_document__35__5-10-mending-communit`: > Adept (5–6): −1 Ob, +2 RS on success.
- atom `valoria_master_document__36__6-1-depth-axis-0-5`: > **E** ✓ Clean Ob progression: Auto → 1 → 2 → 3 → 5 → 8.
- atom `valoria_master_document__44__7-2-phase-structure`: > 5-phase consolidation available.
- atom `valoria_master_document__44__7-2-phase-structure`: > Damage simultaneity at Phase 6 Step 1.
- atom `valoria_master_document__44__7-2-phase-structure`: > **E** ⚠ 7 phases is complex.
_(9 more.)_

## Recommendation

**Recommendation: CANONICAL-PROMOTION-NEEDED — 19 IDs mentioned in canon but not in primary register; promote to formal entries before ingestion.**

- ID classification: {'DEFINED-IN-CANON': 9, 'MENTIONED-IN-CANON': 19, 'PARTIAL': 0, 'NEW': 0}
- Path verification: {'EXISTS': 30, 'MISSING-FROM-REPO': 1}
- Substantive: 103 matched / 34 unmatched