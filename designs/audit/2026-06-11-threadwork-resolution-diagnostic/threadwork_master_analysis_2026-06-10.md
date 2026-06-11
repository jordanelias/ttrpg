# Threadwork Master Analysis & Workplan — 2026-06-10

**Scope:** All threadwork / thread-operations material in jordanelias/ttrpg as of this date.
**Method:** Full retrieval → all-directions mapping → flattening → adversarial review → reconciliation against every prior audit → consolidated docket and phased workplan.
**Companion artifacts:** `threadwork_flowchart.mermaid` (operation lifecycle), `threadwork_state_graph.mermaid` (five state machines + couplings).

---

## §0 Evidence trail

[READ: designs/threadwork/threadwork_v30.md — full, 81k chars]
[READ: designs/threadwork/threadwork_v30_infill.md — full, 40k chars]
[READ: params/threadwork.md — full; canonical state 2026-04-14]
[READ: designs/threadwork/thread_horizontal_integration_spec.md — full (ED-673..681)]
[READ: designs/threadwork/threadwork_philosophical_reference_v30.md + infill — full]
[READ: designs/articulation/articulation_layer_v30.md — full (PP-688)]
[READ: designs/personal/conviction_taxonomy_v30.md, conviction_track_v1.md, knots_v30.md — full]
[READ: tests/audit/aud_tw_001_threadwork_audit.md; tests/audit/audit_threadwork_v25.md — full]
[READ: designs/audit/threadwork_p0_triage_2026-04-27.md — full]
[READ: tests/stress/thread/threadwork_audit_register.md — full (132 findings)]
[READ: designs/audit/2026-05-28-resolution-diagnostic/{resolution_diagnostic,ners_verdict}_threadwork.md — full]
[READ: canon/editorial_ledger.jsonl — grepped for all thread-relevant entries; canon/patch_register_active.yaml — full]
[READ: designs/audit/2026-06-10-master-workplan-v3/valoria_master_workplan_v3.md — thread items]
[READ: sims — mending_coherence_2026-04-17, sim_x_20, sim_x_21, opposing_threadwork_final — conclusions sections]

Not deep-read (inventoried; conclusions absorbed into register/patch layer): conviction_axis_matrix_v30, conviction_migration_roster_v30, params/threadwork_superseded.md, threadwork_v25_historical.md, thread stress batches 1–7, ~25 legacy thread sims. [ASSUMPTION: their live content is represented by the 132-finding register and the patch register — basis: register §H traces each batch to patches.]

---

## §1 Verdict

**The threadwork chassis is mechanically sound and NERS-compliant at the resolution-fitness lens, but the document layer is in supersession debt: at least five canonical rulings have not been propagated into the live v30 body, the body itself is keyed to a dead scale taxonomy, and three independent forks (dissolution ladder, Mending Ob, Knot formation/tiers) mean a reader of any single document gets wrong numbers.** Nothing found here breaks the design intent — the failures are coherence-of-record, not coherence-of-design. But the record is currently unsafe to implement from without the reconciliation layer in §4–§6 of this document.

Severity shape: 5 findings are P1 (one purely propagation, executable now; four require Jordan rulings or mappings), 6 are P2, 4 are P3. One previously open diagnostic claim (T11, inbound drift on non-practitioners) is now **confirmed as a structural gap, not a documentation gap** — the mechanic does not exist anywhere in canon (§4 N14).

---

## §2 All-directions system map

### 2.1 Top-down (intent → mechanics)
Philosophical root (P-01, Foundations): rendered reality is consciousness's compression of the Ein Sof's fullness; Thread operations suspend rendering and act on the substrate. The Einhir principle — *the system rewards restraint and punishes ambition* — is the design's governing asymmetry. Every mechanical layer below it implements that asymmetry: Fibonacci Depth costs (1/2/3/5/8/13) make deep operations disproportionately expensive; Coherence is the personal price, Mending Stability the shared price; PP-603's struck cap means the world absorbs the *full* consequence of ambition; Mending is the only operation priced at a *discount* (Depth−1) — repairing is structurally cheaper than breaking, by exactly one step.

### 2.2 Bottom-up (primitives → assemblies)
Primitives: dice pool (Spirit×2)+History+TPS, floor 5 (params, Pool Notice PP-616/618/619/624/625); TN 7/8/9 by approach; three-axis Ob = Depth + Breadth (0–4) + Distance (0–3). These compose into: the Leap gate (TS≥30, Coherence≥1, Health>0 — v30 §2.3), five operations (Weave/Pull/Lock/Dissolve/Mend — v30 §2.4), collective ops (§2.5), opposing ops (§2.6, PP-653), co-movement randomness (Part 4). Outputs land on four ledgers: practitioner Coherence (Part 3), world MS/RS (Part 5), Gap inventory (PP-604), Knot strain (knots_v30 §4–6).

### 2.3 Lateral (sibling systems at the same layer)
- **Combat:** Leap eligibility consumes the wound system's incapacitation threshold (v30 §2.3 l.219 — ceiling(Health÷2) retained *here* even though PP-232 removed it from the eligibility gate at l.150). Thread-in-combat resolution has **no engine ruling** — ED-911 (open P1, Jordan) ratified the combat engine without it.
- **Social:** Coherence bands impose −1D/−2D on social and Recall rolls (PP-234); Knot partners absorb Composure damage (knots_v30 §5, tier-capped — the cap values are inside the ED-841 fork).
- **Fieldwork:** Thread-Read stat fieldwork integration is master-workplan LA-1 (P1); fieldwork §5.6b is one prong of the Knot tier fork.
- **Mass battle / settlement:** Settlement-level consequences via Throughline T1 (v30 header block) and integration spec ED-675 (settlement environment); Mending Sanctuary (params, Edeyja) couples the WC track to settlement state.

### 2.4 Vertical (scale stack)
Personal (Coherence, Knots, Convictions/Scars) ↔ settlement (RS-affecting environment, Sanctuary) ↔ territory (Lock chronic drift per territory; Gap drains; Fragile-band +1 Ob "in affected territories") ↔ peninsula (MS worldwide thresholds; Critical-band faction Stability checks; Revelation Curve Part 5.6 makes substrate damage *politically legible* to every faction).

### 2.5 Diagonal (cross-scale, cross-domain couplings)
- Revelation curve → faction politics: MS bands map to escalating faction reactions (v30 §5.6) — substrate state drives Church/Crown/RM doctrine via integration spec ED-679 (NPC AI doctrine).
- Domain Echo (ED-673): operation Depth/Breadth echoes into faction stats — a Structural op is a *political event*.
- Knot rupture → Coherence (PP-632): a relational catastrophe is structurally identical to substrate self-damage.
- Crisis arc → Knots: recovery from Coherence 0 is *gated on Close Knots* (Anchoring Scenes) — the system's deepest personal failure can only be repaired relationally. This is the Einhir principle inverted: restraint's reward is that the people you kept are the ladder out.
- Conviction/Scar layer (PP-684/PP-718): belief revision triggers articulation (PP-688 trigger list) and Scar accrual — the perceptual cost of thread practice is routed through the same machinery as moral injury.

---

## §3 Flattened system (inputs → calculations → gates → outputs)

### 3.1 Inputs
| Input | Source | Used by |
|---|---|---|
| Spirit, History, Thread Sensitivity (TPS) | character sheet | pool = (Spirit×2)+History+TPS, floor 5 (params, Pool Notice) |
| Approach (trained?) | v30 §2.1 | TN 7/8/9 selection |
| Target configuration (Depth/Breadth/Distance) | declaration | three-axis Ob (params) |
| Coherence current band | v30 Part 3 | +1 Ob (Fragmented) / +2 Ob (Severed) on all ops incl. Leap |
| MS current band | v30 Part 5 | +1 Ob in affected territories (Fragile) / worldwide (Critical) |
| Thread Fatigue count | ED-694 | contact duration limit; Mending seasonal fatigue +1 Ob/consecutive season (params) |
| Wounds / Health | wound system | Leap gate (Health>0, PP-232); mid-contact incapacitation (ceiling(Health÷2), v30 l.219) |
| Knot roster (tier, strain, Bonds) | knots_v30 | opposing-op strain (v30 §2.6), Composure absorption, Crisis arc pool |
| Substrate Saturation counter | PP-606 | repeat-operation pressure in one area |
| Disposition / Bonds | derived stats PP-684 | Knot formation gate (+5 / Bonds≥5, ED-780) |

### 3.2 Calculations & mechanics (canonical values)
| Mechanic | Formula / values | Cite |
|---|---|---|
| Operation Ob | Depth(1/2/3/5/8/13: Obj/Pers/Rel/Field/Struct/Found) + Breadth(0–4) + Distance(0–3) | params three-axis block |
| Mending Ob | (Depth Ob − 1) + age (0/+1/+2 fresh/established/entrenched); "Ceiling 8" stated | params PP-604 table + Mending block l.246 — **internally conflicted, N5** |
| Dissolution → Gap | breach cost n RS; Ovw: closes in-scene / Succ: n / Partial: n+1 / Fail: n+2 | params PP-604 |
| Gap self-closure | n=0:1 / n=1:2 / n=2:4 / n=3:8 / n=5:32 seasons; drain n RS/season | params PP-604 |
| Lock chronic drift | Obj 0; Pers −1/s; Rel −1→−2 (s4+); Field −2→−3; Struct −3→−5, per territory | params PP-604 block |
| RS track | 100→0; seasonal cap STRUCK (PP-603); 0 = Rupture, terminal | params PP-603 |
| Coherence bands | 10–8 / 7–5 / 4–3 / 2 / 1 / 0 with stacking penalties | v30 §3.3 ll.643–647 |
| Crisis arc | withdraw 1 season → 3× Anchoring (Bonds TN7 Ob2) → roll (best Close-Knot Bonds + scenes, TN7 Ob3) → Coh 4/3/1/NPC | v30 §3.7 |
| Knot formation | knots §3.2: Spirit×2+History TN7 Ob2 → Distant; vs params PP-632: (Bonds×2)+3, Ob=tier−Disposition — **fork, N9** | both |
| Knot strain caps | Distant 4 / Close 7 [Option A, ED-841 pending] | knots_v30 §3 |
| Knot rupture | 5 triggers; −1 Coherence mandatory (PP-632); FR-rupture victim +1 Wound | knots_v30 §6.2 |
| Opposing ops | engagement modifier + resolution table + Knot strain + FR-vs-FR both-fail scaling | v30 §2.6 (PP-653) |
| Dissonance (bystanders) | Spirit TN7 vs Dissonance Factor | params PP-607/610 |
| Foundational Mending price-point | 22D TN7 Ob12 ≈ 22% (params key) — exceeds stated ceiling 8 | params l.110 — **N5** |

### 3.3 Sequences & gates
1. **Declaration** (intent + configuration; "Diagnosis" struck per ED-134/124 but residual in prose — N7)
2. **Leap gate:** TS≥30 ∧ Coherence≥1 ∧ Health>0 (v30 §2.3) → Leap roll (band Ob penalties apply)
3. **Contact:** operations fire; fatigue accrues (ED-694); exits = voluntary / fatigue / Attunement-disruption / incapacitation (op→Failure)
4. **Resolution:** degree ladder per operation; co-movement auto-effect (Part 4, random by design)
5. **Accounting (seasonal):** Gap timers tick; RS drains; Lock drift; MS spontaneous events by band; Knot strain pacing; Crisis-arc resolution rolls; player Knot dissolution window

### 3.4 Outputs (ledgers written)
Practitioner: Coherence Δ, Fallout rolls on band entry, TS Δ (Crisis arc), Fatigue, Scars (conviction_track PP-718), Belief rewrites (Fractured).
World: RS/MS Δ (breach + drain + Mending + WC track), Gap inventory Δ, Substrate Saturation, territory Ob modifiers.
Social/political: Knot strain/rupture, Disposition Δ, Domain Echo → faction stats (ED-673), visibility events (ED-677) → Revelation curve position, faction Stability checks at Critical.
Narrative: articulation triggers (PP-688), Scene Slate entries (ED-674), Case Board (ED-680), Crisis beats (ED-681).
---

## §4 Findings register (new, this audit; worst-first)

**P1**

- **N1 — ED-871 resolved but unpropagated.** Ledger (2026-05-31) rules Mending Coherence cost = 0 (Foundations Amendment 3). Live v30 §3.2 cost row still charges −1; infill temporal-auto-effect line repeats it. *Owner: Claude-executable (pure propagation).* Strike both, cite ED-871 inline.
- **N2 — Scale-taxonomy schism.** v30 body is keyed to Object/Personal/Relational/**Territorial**/Structural; canonical axis (params) is .../Field/Structural/**Foundational**. Affected: §3.2 Coherence costs, FR totals, settlement triggers, integration-spec ED-673 trigger (c), OA table. Field and Foundational ops have **no Coherence cost defined anywhere**. *Owner: Jordan (mapping ruling).* Proposal: restate §3.2 in Depth terms — Obj/Pers 0, Rel −1, Field −1, Struct −2, Foundational = new value Jordan sets.
- **N3 — PP-603 strike unpropagated.** RS seasonal cap (±10) struck in params; still live in v30 §5.5, the PP-198 quotation, and the §5.3 endgame note. Named as P0-13 seven weeks ago; still present. *Owner: Claude-executable.*
- **N4 — Dissolution ladder fork.** v30 §2.4 degree table (Partial → Shifting Object; differing MS magnitudes) vs params PP-604 (Partial → Gap n+1). Params governs by supersession rule. *Owner: Claude-executable for the table swap; Jordan ruling needed only for the v30-only riders (Incursion-on-Failure, incapacitation interaction) — carry or strike.*
- **N5 — Mending Ob fork, now three-legged.** (a) v30 §2.4 age-based Gap ladder (2/3/5/6/7/8+); (b) params (Depth−1)+age; (c) **params-internal conflict:** PP-604 table prices Foundational Mending at Ob 12 — and the probability key prices 22D@Ob12 — while the params Mending block (l.246) and infill (l.89) state "ceiling 8 / total cannot exceed 8." Either the ceiling caps modifiers only (then infill wording "total" is wrong) or it caps the total (then the Ob 12 row and key are dead). *Owner: Jordan one-line ruling; then Claude propagates.*

**P2**

- **N6 — Two live Rendering-Crisis ladders.** Integration spec ED-681 Beat-4 (Spirit+Focus, Ob 2; +2/+1/0/floor) vs v30 §3.7 PP-194 (Knot-Bonds+scenes, Ob 3; →Coh 4/3/1/NPC). Different pools, Obs, and outcome shapes. *Owner: Jordan — pick one or scope them to different contexts explicitly.*
- **N7 — "Diagnosis" residue.** Struck (ED-134/124) yet load-bearing in: declaration prose ("during Diagnosis"), Collective Diagnosis, Priority-4 round reference, threadcut row. *Claude-executable sweep → "Declaration."*
- **N8 — Stranded values in infill.** Skeleton/infill contract says values live in skeleton; these live only in infill: POP gate (TS70+/MS≤60), Mending ceiling 8, Lock variable drift, Foundational POP (+2 Ob/×3 MS), First-Leap effects, Leap melee-eligibility, PP-200/202/205/207, Revolution Mandate≥1, collective Stunt rule. *Claude-executable hoist; values byte-identical.*
- **N9 — Knot formation fork** (new; outside ED-841's tier catalog). params PP-632 pool (Bonds×2)+3, Ob = tier−Disposition vs knots_v30 §3.2 Spirit×2+History TN7 Ob2. *Owner: Jordan — recommend appending to the ED-841 decision packet rather than a new ledger line.*
- **N10 — Scar trigger matrix unmigrated.** conviction_track §3 matrix has the 7 legacy columns; the 13-Conviction taxonomy (PP-684) leaves Authority/Utility/Identity/Virtue/Honor/Community/Warden with **no defined Scar triggers**. canonical_sources claims the matrix "applies to migrated" — only partially executable. *Owner: design work; coordinate with the ED-1006/1009 naming stream before adding columns.*
- **N13 — Mode-era saturation.** v30 Parts 5.4/5.5/7 + GM/table phrasing predate PP-675 (Strategic/Scene + Zoom-In). *Fold into PP-675's existing phases; do not run a separate sweep.*
- **N14 — T11 closed: inbound drift does not exist.** Diagnostic T11 asked where the P-12 "Coherence drift for connected non-practitioners" formula lives. Answer after full retrieval: nowhere. Knot strain pacing (knots §3.3) and threadcut +0.5/strain exist; an NPC-side Coherence-drift mechanic does not. **Structural gap, not a lost reference.** *Owner: Jordan — decide whether P-12 implies the mechanic (then design it) or the philosophical claim is satisfied by strain pacing (then annotate P-12).* I present options; I have not invented a formula.

**P3**

- **N11 — Record hygiene cluster.** canonical_sources `threadwork:` status note actually describes conviction_track §1–3 (mis-attached); v30 index sha stale (18cf588b vs 08e4dcf2); version-header chaos (file says v2.6, v3.2, "v30" simultaneously); integration-spec propagation map uses dead `designs/ttrpg` paths; RS-vs-MS naming split (params says RS, v30 body says Mending Stability); v30 l.150 (PP-232: "incapacitation is binary") vs l.219 (mid-contact threshold restated as ceiling(Health÷2)) — likely stale parenthetical, verify against current wound system before sweep. *Claude-executable.*
- **N12 — Starting-RS dual default.** TTRPG 60 / BG 72 (params PP-603) unresolved for the single-mode videogame target. *Jordan, one number.*
- **N15 — Inherited open items** (not re-found; carried): ED-911 (thread-in-combat, P1), ED-841/842 (tier/composure drift), LC-0b/J-2 (scene.thread_operation Key registration), J-3 (philosophical-ref boundary), LA-4 (piety/conviction naming), LA-1 (Thread-Read fieldwork). Residual 04-27 P0s with unconfirmed closure: P0-01 (settlement-Order-as-target), P0-05 (risk-die scope), P0-17, P0-18, P0-24/25/28 (Foundational family), P0-15 — each [UNVERIFIED-residual]: no closing ledger line found, no superseding patch found.

[NULL: opposing-operations chain (v30 §2.6 + PP-653 + sim_opposing_threadwork_final) — examined for internal contradiction, found consistent; sim's edge cases were folded into PP-653 correctly.]
[NULL: collective-operations math (§2.5 + sim_x_21) — examined; brittleness is documented design intent (OA brittleness validated), not a defect.]
[CONFIDENCE: high — every finding above carries a file+line or ledger cite; N14 is the one negative-existence claim and rests on exhaustive grep of the retrieval set.]
---

## §5 Reconciliation with prior work

| Prior artifact | Standing | This audit's relation |
|---|---|---|
| AUD-TW-001 (18 findings) | Mostly closed via patch layer | 3 of its items resurface as propagation debt (N1/N3 family); none contradicted |
| audit_threadwork_v25 (14/14 canon PASS) | Historical (v25) | Superseded by v30 body; kept as provenance only |
| 132-finding register (2026-04-16) | The structural backbone | §F's "WC3-or-Rupture endgame" still holds (re-confirmed via sim_mending_coherence); §H patch sequence executed except the propagation residue now in N1/N3/N4/N5 |
| P0 triage 2026-04-27 | 7 resolved / 15 OPEN-DESIGN / 4 OPEN-MECH | OPEN set carried into N15 with [UNVERIFIED-residual] markers; P0-13 escalated into N3 (still unfixed after 7 weeks) |
| 05-28 NERS diagnostic + verdict | VERDICT: NERS-COMPLIANT, S: PARTIAL | **Stands for the chassis; understated for the record.** That pass did not read the integration spec, Part 6/7 deep, or the params supersession layer — the gaps it could not see are exactly N2/N5/N6/N8. T1–T10, T12 dispositions unchanged; T11 now closed as N14 (gap confirmed, harder verdict than "PARTIAL" implied) |
| Editorial ledger | Source of truth | ED-871/878 honored (878 **not relitigated** per its FALSE-contradiction ruling); ED-841/842/911 referenced, not duplicated; ED-1006/1009 stream (today, parallel) — N10/LA-4 explicitly deferred to it for naming |

**Consolidation statement:** no prior finding is overturned. This audit adds 15, closes 1 (T11→N14), escalates 1 (P0-13→N3), and re-keys the NERS "S: PARTIAL" to "S: FAIL at the record layer" (§8).

---

## §6 Jordan decision docket (consolidated; one sitting)

1. **N2** — Coherence-cost mapping to Depth taxonomy (proposal on table: 0/0/−1/−1/−2/Jordan-new). Sets Field+Foundational costs for the first time.
2. **N5** — Mending ceiling: modifiers-only or total? One line; unblocks Foundational Mending pricing.
3. **N4 riders** — carry or strike v30-only Dissolution riders (Incursion-on-Failure; incapacitation interaction).
4. **N6** — Crisis ladder: ED-681 vs PP-194 (or scope split).
5. **N9 + ED-841 + ED-842** — Knot packet: tier system (A/B/C), formation roll, composure cite. One packet, three sub-rulings.
6. **N12** — starting RS single default.
7. **N14** — P-12 inbound drift: design it, or annotate P-12 as satisfied by strain pacing.
8. **ED-911** — thread-in-combat engine ruling (pre-existing P1; listed for the same sitting).
9. **N15 residuals** — confirm or re-open the six [UNVERIFIED-residual] P0s.

---

## §7 Phased workplan

**Phase A — Claude-executable now (no rulings needed; one batch PR):**
N1 (ED-871 propagation), N3 (PP-603 sweep), N4 table-swap (params version in, riders flagged pending item 3), N5 leg-(a) removal (v30 ladder out, params formula in, ceiling flagged pending item 2), N7 (Diagnosis→Declaration sweep), N8 (infill→skeleton hoist, byte-identical), N11 (hygiene cluster). Each edit cites its ledger/patch authority inline. Sim re-validation after batch: re-run mending_coherence + opposing scenarios to confirm no numeric drift.

**Phase B — post-docket propagation (each unblocks on its §6 item):**
N2 restatement; N5 final form; N4 riders; N6 single ladder; Knot packet edits across params + knots_v30 + articulation §2.4 + fieldwork §5.6b; N12 value; ED-911 combat insertion.

**Phase C — design work (scoped, not started unilaterally):**
N10 Scar-matrix completion (blocked on ED-1006/1009 naming stream); N14 if "design it" is chosen; PP-675 mode-language phases absorb N13.

**Coordination boundaries:** active-work-index session owns combat/sim/massbattle/faction streams — Phase A touches none of their files; ED-911 lands in their lane and is handed as a docket item, not edited here. ED-1006/1009 module-adjudication stream owns naming; N10/LA-4 wait. Master-workplan lanes LC-0b/J-2/J-3/LA-1/LA-4 referenced, not duplicated.

**Ledger staging:** proposed entries for N1–N15 are drafted but **not committed** — staged for veto per project protocol (P1 findings → editorial_ledger only with Jordan's sign-off in this workflow).

---

## §8 NERS re-verdict

- **N (Necessity):** PASS — every mechanic traces to a P-01-rooted need; no orphan subsystems found.
- **E (Elegance):** PASS — Fibonacci Depth + struck cap + Mending discount is one asymmetry expressed three ways; the chassis is *more* elegant than its documents.
- **R (Robustness):** PASS with the §F caveat re-confirmed — WC3-or-Rupture is the only endgame pair; sims hold.
- **S (Supersession/record):** **FAIL** (was PARTIAL on 05-28). Five unpropagated rulings, one dead taxonomy in the live body, three forks, and a params-internal contradiction. The 05-28 PARTIAL was an artifact of that pass's narrower retrieval; with the full layer in view, the record does not currently support implementation without this document's reconciliation table.

Chassis verdict unchanged: **NERS-compliant design, non-compliant record.** Phase A alone moves S to PARTIAL; the docket clears it.

---

## §9 Artifact inventory (this session)

| Artifact | Path | State |
|---|---|---|
| Operation lifecycle flowchart | /mnt/user-data/outputs/threadwork_flowchart.mermaid | done |
| Five-machine state graph + couplings | /mnt/user-data/outputs/threadwork_state_graph.mermaid | done |
| This master analysis & workplan | /mnt/user-data/outputs/threadwork_master_analysis_2026-06-10.md | done |
| Staged ledger entries (N1–N15) | §4 above; not committed | awaiting veto |

[PASS-3 verdict recorded in session log.]
