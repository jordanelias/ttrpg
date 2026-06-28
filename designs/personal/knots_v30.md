# VALORIA — Knot System (Unified Canon)

## Status: CANONICAL — Pass 2g synthesis 2026-05-17

## Scope: consolidates the Knot mechanic specification scattered across 9 canon fragments (complete_systems_reference Part 8 PP-632, threadwork_v30 §2.6 §3.5 §3.6 §3.7 + Rendering Crisis Beat 2, fieldwork_v30 §2.6 §2.8 §5.1 §5.6 §5.6a §5.6b, social_contest_v30 §4 Corroborate, articulation_layer_v30 §2.4 §3.1 §3.5 §6.1 §6.2, derived_stats_v30 §10.1 §14.4). No new mechanics introduced — existing canon synthesis. Section §11 catalogs canon-vs-canon contradictions surfaced during synthesis (TIER-DRIFT-001 + COMPOSURE-DRIFT-001) for Jordan resolution.

## GD constraints: none directly. Knots are personal-scale relational mechanics. Cross-references GD-3 indirectly (extra-parliamentary status of emergent factions may exclude Knot-based political mechanics).

## Source authority:
- `designs/architecture/complete_systems_reference.md` Part 8 — PP-632 spec
- `designs/threadwork/threadwork_v30.md` §2.3 §2.6 §3.3 §3.5 §3.6 §3.7 + Rendering Crisis Narrative Structure
- `designs/scene/fieldwork_v30.md` §2.6 §2.8 §5.1 §5.6 §5.6a §5.6b
- `designs/scene/social_contest_v30.md` §4 Corroborate
- `designs/articulation/articulation_layer_v30.md` §2.4 §3.1 §3.5 §6.1 §6.2 §4.4
- `designs/scene/derived_stats_v30.md` §10.1 §14.4
- `canon/02_canon_constraints.md` §A P-12 (relational contagion), A12 (Thread-binding inseparability)
- `params/core.md` Bonds attribute spec

## Sim module: `sim/personal/knots.py`

---

## §1. What is a Knot

A **Knot** is a thread-substrate binding between two characters whose relational depth has reached the structural maximum (Disposition +5). It is *constitutive*, not contractual — the Knot IS the Thread-level relationship, not a label applied to one. Once formed, the binding can be strained, broken, or ruptured but not unilaterally dissolved by either party except through deliberate Player Choice (per §6 below).

**Knot vs Bond.**
- **Bonds** (attribute, 1-7) is structural capability — how deep relationships CAN go. Gates Knot eligibility (Bonds ≥ 5); it does **not** cap Disposition (ED-912 — Disposition is a flat −5..+5).
- **Knot** is the realized state of one specific relationship at Disposition +5.

The PC's Knot count is capped at `floor(Bonds/2) + 1` (per PP-632, derived_stats §14.4 Knot Pool entry).

**Mechanical definition table:**

| Property | Value | Canon source |
|---|---|---|
| **Knot Pool** (formation roll) | `(Bonds × 2) + 3`, min 5 | PP-632; derived_stats §14.4 |
| **Knot Max** (simultaneous Knots) | `floor(Bonds/2) + 1` | PP-632; fieldwork §5.6a prereq 3 |
| **Knot tier system** | **Distant / Close** (2-tier), bidirectional −5..+5 strain | RESOLVED ED-912 (TIER-DRIFT-001); fieldwork §5.6b |
| **Disposition range** | flat **−5..+5** (NOT Bonds-capped; Bonds ≥ 5 is a separate Knot prereq) | ED-912; fieldwork §5.1 |
| **Knot detection** | Bonded characters perceive each other across distance via the binding | fieldwork §2.6 |

---

## §2. Tier System — RESOLVED (ED-912, 2026-06-28)

**TIER-DRIFT-001 and COMPOSURE-DRIFT-001 — RESOLVED.** Jordan ruling 2026-06-28: **Option A**, reframed onto a bidirectional **−5..+5 bond-strain gauge**. The prior 0→capacity accumulator (Distant 4 / Close 7) is replaced by a single −5..+5 axis: positive strain is *wear* toward rupture; negative strain is *resilience* earned through mutual investment. Canonical spec: `fieldwork_v30.md` §5.6b.

| Knot tier | Strain range | Starts at | Notes |
|---|---|---|---|
| **Distant** | −2 … +5 | 0 | Shallower bond; reinforces only to −2. Upgradeable to Close (§3.3). |
| **Close** | −5 … +5 | −2 | Deeper bond; begins buffered, tempers to −5. |

- **Rupture at +5** (both tiers). **−5 = Tempered** (Close only) absorbs the next rupture trigger once, then resets to 0.
- **Reinforcement:** −1 strain/season at Accounting when Disposition ≥ +3 and no strain added.
- **Break Composure damage = 4** (COMPOSURE-DRIFT-001 resolved — the canonical value is **4** per `fieldwork_v30.md` §5.6b; the prior articulation §2.4 citation of "5" is corrected).

**Superseded:** the PP-632 Loose/Medium/Close 3-tier point-cost model (1/2/5) is struck in favour of the Distant/Close strain model. Supersession logged in `canon/supersession_register.yaml`; `complete_systems_reference.md` Part 8 and `articulation_layer_v30.md` §2.4 updated to match.

---

## §3. Formation

### §3.1 Prerequisites (all required)

Per fieldwork §5.6a (AUD-NPC-01 + ED-780):

1. **Disposition +5** with the target NPC
2. **Either PC or NPC has TS ≥ 30** (Thread contact — per A12, Knots bind threads; substrate must be accessible)
3. **PC's current Knot count < floor(Bonds/2) + 1** (per PP-632)
4. **No existing Knot with this NPC**
5. **PC Bonds ≥ 5** (explicit prerequisite per ED-912 — Disposition is a flat −5..+5 with no Bonds ceiling, so this gate is stated directly; a Bonds 1-4 character can reach Disposition +5 yet still cannot form a Knot. ED-780's intent preserved.)

### §3.2 Procedure

Roll: **Spirit × 2 + History (Relationships)**, **TN 7**, **Ob 2**.

| Degree | Outcome |
|---|---|
| Overwhelming | Knot forms at **Close** tier directly. Strain starts at −2 (Close buffer). |
| Success | Knot forms at **Distant** tier. Strain starts at 0. Can be upgraded to Close per §3.3. |
| Partial | Knot does not form. Disposition holds at +5. May retry next season. |
| Failure | Knot does not form. Disposition drops to +4. May retry only after returning to +5. |

(Canonical per ED-912 — Option A Distant/Close tiers.)

### §3.3 Tier Upgrade

Per fieldwork §5.6b: a Distant Knot can be upgraded to Close via a subsequent §3.2 procedure rolled at Overwhelming success. Upgrade resets strain to 0.

(Option B's Loose/Medium/Close tiers are not adopted — ED-912 canonizes Distant/Close only.)

### §3.4 Bonds Capacity Rationale (ED-780)

A character with Bonds 1-4 cannot form a Knot. Bonds 5+ is the floor. This means the Knot-mediated systems below are closed off to low-Bonds characters:

- Knot-mediated Wager system (social_contest §6.1)
- Knot-as-Composure-buffer (social_contest §4 Step 6)
- Knot-mediated remote Thread-Read (§4.1 below)
- Knot Anchoring for Coherence recovery (§8 below)
- Knot-mediated counsel extraction (npc_behavior §3.5.3)
- Knot-sharing corroboration bonus (social_contest §4 Corroborate)

High Bonds at character creation is the canonical investment for opting into these systems.

---

## §4. Use

Five mechanical use-sites; each costs the Knot strain.

### §4.1 Knot-mediated remote Thread-Read

Per fieldwork §2.6:
- Pool: standard Thread-Read pool
- TN: 7
- Ob: 2 (Personal scale)
- Cost: **+1 Knot strain per use**
- **Detection roll:** Knotted party rolls Spirit TN 7 Ob = practitioner's Cognition ÷ 2 (min 1). Failure: no detection. Success: detection.
- **If detected:** Disposition −3 (betrayal of relational trust). The Knot persists (constitutive, not contractual) but the relationship may degrade.

Evidence: Thread-verified. Inert Knowledge for non-sensitives. Advances Evidence Track normally.

### §4.2 Knot-as-Composure-buffer

Per social_contest §4 Step 6 (referenced in articulation §2.4):
- A Knot partner present in a social contest may absorb up to N Composure damage on the PC's behalf (N capped by Knot tier — Close = up to 5, Distant = up to 4).
- Cost: **+1 Knot strain per use** (per fieldwork §5.6b)
- Cap: once per contest

### §4.3 Knot-mediated counsel extraction

Per npc_behavior §3.5.3 (referenced in fieldwork §5.6b ED-664):
- A Knotted NPC may be queried for private knowledge they would not otherwise share
- **Single-extraction-per-campaign rule** — first extraction costs +0 Knot strain; subsequent retrievals (re-querying same Knot for additional counsel) cost +1 strain each
- Public citation of extracted counsel (per ED-664 §3.5.4): **immediate Knot rupture** (see §6.2)

### §4.4 Knot Anchoring for Coherence recovery

Per threadwork §3.5 (Recovery):
- A Close Knot voluntarily anchoring through a dedicated Anchoring Scene: Bonds check TN 7 Ob 2.
- Success: +1 Coherence for the practitioner.
- Cost: **+1 Knot strain** on the anchoring Knot.

Used in Rendering Crisis Resolution (per threadwork §3.7): pool for the resolution roll uses **highest Close Knot's Bonds score + number of successful Anchoring Scenes**, TN 7, Ob 3.

### §4.5 Knot-sharing corroboration

Per social_contest §4 Corroborate (PP-257):
- A Knot-sharing corroborator declaring support before the Argue roll rolls at **Ob 1** (vs Ob 2 for non-Knot coalition members).
- Asymmetric proceedings: all corroborators for the disadvantaged party use Ob 2 regardless of Knot.
- **No strain accrued by the supporting Knot from corroboration use** (per absence in §5.6b strain accumulation list).

---

## §5. Strain Accumulation

Per fieldwork §5.6b. Strain accrues as Knot history of use:

| Source | Strain |
|---|---|
| Knot-mediated remote Thread-Read (§4.1) | +1 per use |
| Knot-as-Composure-buffer (§4.2) | +1 per use |
| Knot-mediated counsel — subsequent retrievals (§4.3) | +1 per re-query (first query is free) |
| FR Lock or Dissolution near a Knot partner (threadwork §6 Knot-substrate inseparability) | +1 |
| Witnessing Conviction Scar fire in Knot partner (Piety Track ≥ 3 Scar count) | +1 at next Accounting |
| Sustained Disposition reduction (Disposition < +3 for 2 consecutive seasons, season N+1 confirmed at Accounting) | +1 at Accounting of season N+1 (PP-719 clarification, EC-F2.A-01) |
| Knot strain from contested Thread operations (threadwork §2.6) | +1 Ob next Thread op this scene + 2 Composure (per loser/tied in opposed contest); +2 Ob + 4 Composure for FR Lock/Dissolution; +1 strain to the Knot per opposing-operations event |

**Strain decay:** at Accounting, if **no strain was added that season AND Disposition is +3 or higher**: strain decreases by 1. Sustained mutual investment dissipates accumulated stress.

---

## §6. Break and Rupture

Two end states: **break** (strain accumulation exceeds capacity) and **rupture** (immediate trigger event bypasses capacity).

### §6.1 Break (strain-capacity exceeded)

Per fieldwork §5.6b. At Accounting, if strain exceeds tier capacity, Knot breaks.

**Tier capacities [PROVISIONAL: TIER-DRIFT-001 — see §2]:**

| Tier (Option A) | Capacity |
|---|---|
| Distant Knot | 4 strain |
| Close Knot | 7 strain |

**Break consequences:**
- **Disposition** drops to +2 (or current − 2, whichever is lower; floor at −3 per §3.5 Disposition range)
- **Both partners take 4 Composure** (per A12-derived disorientation; the Thread previously connecting renderings releases force)
- **All Knot-mediated benefits cease immediately**: shared Composure buffer, +1D social, P-12 contagion, Wager prerequisite, counsel extraction eligibility
- **Knot count slot frees** — player may form new Knot per §3 in a subsequent season
- **Close Knots broken at high strain (Option A: strain ≥ 6 of 7)**: Conviction Scar +1 to both partners (broken Knot leaves perceptual residue per A1/C1 Thread-binding inseparability)

### §6.2 Rupture (immediate, bypassing strain)

Per fieldwork §5.6b. Five triggers cause immediate rupture:

| Trigger | Source | Mechanical effect |
|---|---|---|
| Public citation of private counsel | ED-664 §3.5.4 | Knot ruptures, Disposition → **−4** (per PP-632 rupture spec + §3.5.4) |
| Knot partner's death | Universal | Disposition becomes irrelevant; Knot partner enters Memory state. Knot-as-buffer can absorb final Composure damage per Last Stand rule (player_agency §X — TBD) |
| FR Dissolution targeting Knot partner | threadwork §3.4 | Tears the Knot directly. Rupture-victim takes **+1 Wound** (no armour). |
| Permanent Conviction shift to opposing Conviction | npc_behavior §5 | Knot tied to specific Conviction-state; opposing Conviction makes Thread-binding incompatible. |
| Player explicit dissolution | Player choice | Player may dissolve a Knot at Accounting. Cost: **2 Composure** (one-sided release strain). Disposition unchanged (relationship persists at non-Knotted level). |

**Coherence loss:** Per PP-632, rupture imposes mandatory **−1 Coherence** on the practitioner (cannot be voluntarily forgone). Rupture is structural damage at the Thread layer.

---

## §7. Knots in Opposing Thread Operations

Per threadwork §2.6 (Knot Strain table). When a Knot partner participates in opposing Thread operations:

| Scenario | Losing/Tied Practitioner | Winning Practitioner |
|---|---|---|
| Standard (Weave / Pull) | +1 Ob next Thread op this scene; 2 Composure | 1 Composure |
| FR (Lock / Dissolution) | +2 Ob next Thread op this scene; 4 Composure. If winner Dissolved: +1 Wound (tear through Knot, no armour) | 2 Composure |
| Both meet Ob (tie) | Both: +1 Ob, 2 Composure (FR: +2 Ob, 4 Composure) | N/A |
| Both fail | Both: 1 Composure | N/A |

**Composure restores at scene change. Ob penalty expires after next Thread operation or at scene end.**

**N-Way Opposing Operations (3+ practitioners):** Per threadwork §2.6. Three or more practitioners with at least two genuinely opposing intentionalities on the same configuration → automatic lattice collapse. All operations fail. Gap forms at target's scale. Mending Stability −(2 × number of opposing practitioners). All: Coherence per §3.2; Knot strain +2 Ob, 4 Composure.

---

## §8. Knots in Coherence Recovery

Per threadwork §3.3 + §3.5 + §3.7 + Rendering Crisis Narrative Structure.

### §8.1 Coherence threshold effects on Knots

| Coherence band | State | Knot strain effect |
|---|---|---|
| 10-8 | Stable | None |
| 7-5 | Dissonant | Close Knots sense wrongness: +1 strain per 3 sessions |
| 4-3 | Fragmented | All Knots at wrongness pace: +1 strain per 2 sessions |
| 2 | Fractured | All Knots at accelerated wrongness: +1 strain per session |
| 1 | Severed | All Knots +2 strain (per threadwork §3.3 — truncated in extract; full canon to be verified Pass 2k) |
| 0 | NPC | Per PP-261, practitioner transitions to NPC; Knots persist as NPC-NPC bindings |

### §8.2 Anchoring Scene (§3.5 recovery path)

Eligibility: Close Knot voluntarily participates.
Mechanic: Bonds check TN 7 Ob 2.
Cost: +1 Knot strain (on the anchoring Knot).
Benefit: +1 Coherence (to the practitioner). Cannot exceed 10.

### §8.3 Rendering Crisis Resolution (PP-194 [PROVISIONAL])

Per threadwork §3.7. Minimum conditions:
1. Full season withdrawal from Thread practice
2. Three Anchoring Scenes with Close Knots (each: §8.2 procedure; failed scene costs the scene without progress)

**Resolution attempt** (Accounting after conditions met):
- Pool: **highest Close Knot's Bonds + number of successful Anchoring Scenes**
- TN: 7, Ob: 3

| Degree | Outcome |
|---|---|
| Overwhelming | Coherence → 4. Functional. Permanent −1 Thread Sensitivity. |
| Success | Coherence → 3 (Fragmented). Minimally functional. −1 TS. |
| Partial | Coherence → 1 (Severed). Another full-season arc required for further recovery. |
| Failure | No recovery. Practitioner becomes NPC at season end. |

### §8.4 Rendering Crisis Narrative Structure (ED-681)

Per threadwork Rendering Crisis Narrative Structure. Beat 2 — **Knot Anchoring**: a Close Knot NPC arrives. Practitioner perceives them simultaneously as rendered person and thread-configuration. Mechanical: Spirit check TN 7 Ob 1. Success: Coherence +1. Failure: NPC receives Knot Strain +1.

---

## §9. Threadcut Beings and Knots

Per fieldwork §2.8.

**Knot formation prerequisite:** threadcut being at Disposition +5 becomes a Knot candidate only if the practitioner has **TS ≥ 30**. The threadcut being is already performing continuous Thread work to maintain its existence — Knotting adds relational load to that self-maintenance.

**Self-maintenance strain:** Each Knot use (§4.1 remote, §4.2 buffer, §4.4 anchoring) costs the threadcut being **+1 self-maintenance strain** (separate from the PC-side +1 Knot strain). GM tracks cumulative strain:
- At strain 5: rendering shows visible instability — facial consistency fails, temporal micro-slippages increase, originary state bleeds through
- Strain reduces by 1 per season of Knot non-use

**Threadcut Knot collapse alternate trigger:** Per fieldwork §5.6b ("Threadcut being Knots"). Strain on the Knot also drains the threadcut being's Coherence at **+0.5 per strain (round up)**. When threadcut Coherence reaches 0, Knot collapses regardless of strain count.

---

## §10. UI / Articulation Surface

Per articulation_layer_v30.

### §10.1 Tier 1 — Bonds register (per §2.3 §2.4)

Continuous UI: list of named NPCs with Bond level + **Knot status** + active Belief markers.

Knot status indicator per Bonded NPC shows tier (Distant / Close [Option A] or Loose / Medium / Close [Option B] per §2 PROVISIONAL).

### §10.2 Tier 2 — Cut-scene triggers (per §3.1)

Two Knot-related triggers in the 10-trigger ruleset fire cut scenes:

- **Trigger #6**: `meta.knot_formed` (Class B per §6.1)
- **Trigger #7**: `meta.knot_ruptured` (Class B per §6.2 — added 2026 per articulation §6)

### §10.3 Tier 2 — Significance scoring (per §3.5)

Scene-event Keys with `knot_partners_present` field including protagonist's Bonded NPC pair gain **+1 significance** when scoring for cut-scene articulation.

### §10.4 Tier 3 — Chronicle integration (per §4.4)

Per-year chronicle structure includes a "Knot/Belief inflections" paragraph: Knot formations and ruptures, Belief revisions emitted as named events with NPC pair attribution.

---

## §11. Canon Contradiction Catalog (forward-flag to Pass 2k)

Three contradictions surfaced during Pass 2g synthesis. Each requires Jordan resolution at editorial-ledger batch:

| ID | Description | Sources | Recommended resolution |
|---|---|---|---|
| **TIER-DRIFT-001** | Knot tier system disagrees across PP-632 (Loose/Medium/Close, 3 tiers, strain 1/2/5) vs ED-773 fieldwork §5.6b (Distant/Close, 2 tiers, strain 4/7) vs articulation §2.4 (uses PP-632 tier names but cites ED-773 for Composure cost) | complete_systems_reference Part 8; fieldwork §5.6b; articulation §2.4 | Option A — ED-773 supersedes PP-632 (chronological, with explicit gap-closing framing). Strike Loose/Medium tiers; canonize Distant/Close with strain 4/7. Update articulation §2.4 reference + register supersession in `canon/supersession_register.yaml` + amend PP-632 entry in complete_systems_reference. |
| **COMPOSURE-DRIFT-001** | articulation §2.4 cites Composure damage "5 default per ED-773" but ED-773 in fieldwork §5.6b spec text says "4 Composure" | articulation §2.4; fieldwork §5.6b | Canonical value is **4** per spec text. Correct articulation §2.4 reference from "5 default" to "4 default" |
| **TRUNC-DRIFT-001** | threadwork §3.3 Coherence-1 Severed row in source extract shows "All Knots +2 strain" but extract is truncated. Full canon text needs verification | threadwork §3.3 | Re-fetch full §3.3 and confirm the strain value for Coherence-1 |

[FLAG: these are pre-existing canon contradictions, not introduced by Pass 2g. Pass 2g surfaces them; Pass 2k editorial-ledger batch resolves them under Jordan ratification.]

---

## §12. Cross-references

### Canon docs consolidated (this doc does NOT supersede; it synthesizes)

- `designs/architecture/complete_systems_reference.md` Part 8 (PP-632)
- `designs/threadwork/threadwork_v30.md` §2.3, §2.6, §3.3, §3.5, §3.6, §3.7, Rendering Crisis Narrative Structure ED-681
- `designs/scene/fieldwork_v30.md` §2.6, §2.8, §5.1, §5.6, §5.6a, §5.6b (ED-773)
- `designs/scene/social_contest_v30.md` §4 Corroborate (PP-257)
- `designs/articulation/articulation_layer_v30.md` §2.4, §3.1, §3.5, §4.4, §6.1, §6.2
- `designs/scene/derived_stats_v30.md` §10.1 (PP-684), §14.4

### Foundational canon

- `canon/02_canon_constraints.md` §A P-12 (relational contagion), A12 (Thread-binding inseparability), A1 (perceptual residue)
- `params/core.md` Bonds attribute, Disposition track

### Sim integration

- `sim/personal/knots.py` — formation / use / strain / break / rupture
- `sim/thread/coherence.py` — Coherence delta on rupture, Anchoring Scene recovery
- `sim/thread/opposing.py` — Knot Strain in opposing operations
- `sim/personal/contest.py` — Knot-as-Composure-buffer (§4.2), Knot-sharing corroborator (§4.5)
- `sim/personal/fieldwork.py` — Knot-mediated remote Thread-Read (§4.1)
- `sim/cross_scale/articulation.py` — UI surface (§10)

### Mechanics index entry

`canon/mechanics_index.yaml` → `mechanics.knots` — `unified_canon_target` field updated from "designs/personal/knots_v30.md (Pass 2g, pending)" to "designs/personal/knots_v30.md (Pass 2g canonized 2026-05-17)" in companion commit.

---

## §13. Status Declaration

This unified spec is **CANONICAL synthesis** of existing canon. No new mechanical content introduced. The Knot system was mechanically complete across its 9 source fragments; Pass 2g consolidates the dispersed specification into a single readable doc, surfaces three canon contradictions (TIER-DRIFT-001, COMPOSURE-DRIFT-001, TRUNC-DRIFT-001) for Pass 2k resolution, and binds the unified spec to `sim/personal/knots.py` for implementation.

Where Pass 2g made interpretive choices in the presence of canon ambiguity (degree-table outcomes in §3.2 assuming Option A tier resolution; tier-named strain values in §6.1), those choices are marked **[PROVISIONAL: TIER-DRIFT-001]** and revert to whatever Jordan ratifies in Pass 2k.

[STATUS: CANONICAL synthesis — Pass 2g 2026-05-17. Three canon contradictions forward-flagged to Pass 2k. Interpretive choices marked PROVISIONAL pending Jordan ratification.]

---

## §14. Changelog

- **v30 init (2026-05-17, Pass 2g):** Initial synthesis from 9 canon fragments. Unified Knot mechanic spec for sim/personal/knots.py target. Surfaces TIER-DRIFT-001 (PP-632 vs ED-773 tier-system contradiction), COMPOSURE-DRIFT-001 (articulation §2.4 cites wrong Composure value), TRUNC-DRIFT-001 (threadwork §3.3 Severed row needs verification). No new mechanics. Forward-flagged for Pass 2k editorial-ledger batch resolution.
