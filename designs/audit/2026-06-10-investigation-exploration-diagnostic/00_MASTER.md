# Comprehensive Audit — Exploration / Investigation (Fieldwork) — All Workings, All Dimensions

**Date:** 2026-06-10
**Session:** audit | ef659454b0c8
**Skills:** valoria-mechanic-audit (Modes A–E) + valoria-resolution-diagnostic (Stages 0–4) — composite run
**Scope:** designs/scene/fieldwork_v30.md (master, DESIGN v1.1 PP-628/PP-630) + fieldwork_v30_infill.md + investigation_systems_v30.md (CANONICAL 2026-04-17) + split files fieldwork_exploration.md / fieldwork_investigation.md / fieldwork_godot.md / fieldwork_editorial.md + params/fieldwork.md + params/core.md + engine docs + sims/tests + ledger/register cross-checks
**Supersedes:** designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_investigation.md (index-depth verdict; that file self-declares "if a deeper read surfaced a fresh finding, it would supersede this verdict" — this is that deeper read). `[SELF-AUTHORED — bias risk]` applies to the 2026-05-28 verdict and to this session's predecessors; both treated as external.

---

## §0 Citations (every mechanical value below carries file + section)

Read in full this session (tracked path, task_gate('audit') per block): `fieldwork_v30_index.md`, `investigation_systems_v30_index.md`, `fieldwork_v30.md` (76,769 chars), `fieldwork_v30_infill.md` (27,760), `investigation_systems_v30.md` (36,114), `fieldwork_exploration.md`, `fieldwork_investigation.md`, `fieldwork_godot.md`, `fieldwork_editorial.md`, `params/fieldwork.md` (12,220), `params/core.md` (15,668), `canon/02_canon_constraints.md`, `skills/valoria-mechanic-audit/SKILL.md`, `skills/valoria-resolution-diagnostic/SKILL.md` (repo), `designs/audit/2026-05-28-engine-replacement/engine_replacement_reconciled.md`, `designs/audit/2026-05-28-resolution-diagnostic/domain_action_resolver_spec.md`, `designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_investigation.md`, `sim/personal/fieldwork.py`, `sim/personal/investigation.py`, `tests/sim/fieldwork_lifecycle_stress_01/fieldwork_lifecycle_stress_01.md`. Grepped: `canon/editorial_ledger.jsonl` (366,044 chars), `canon/patch_register_active.yaml`, `tests/coverage_matrix.md`, `canon/supersession_register.yaml`, `designs/audit/2026-06-04-attributes-derived-ners/04_RECONCILED_MASTER.md`, `references/canonical_sources.yaml`.

---

## §1 Verdict

**The fieldwork/investigation system is architecturally sound and canonically split.** The deterministic decision core (Five-Filter Chain, Scene-as-Graph, Dialogue Lattice, Evidence clock routing) survives a full-depth adversarial read — the 2026-05-28 architecture findings (INV1–INV9) stand. What the index-depth read could not see, and what reverses the prior NERS-COMPLIANT verdict, is that **the three documents that jointly specify the roll's inputs disagree on the live values**: master fieldwork_v30, params/fieldwork, and investigation_systems_v30 carry three incompatible Disposition/Knot specifications, two incompatible Disposition→Ob rules, and two different primary attributes for Thread-Read. A GM or implementer cannot determine which rule applies. That is a P1 cluster (blocks play/implementation), with a structural root cause: PP-632 was propagated to params and splits but never to the master, while PP-684/ED-773/ED-780/PP-628-era changes were applied to the master but never back-propagated. Severity-ranked findings follow.

---

## §2 P1 findings (block play / implementation)

### P1-1 · Fieldwork canonical-line split — Disposition / Knot / Ob-application (3-way contradiction cluster)

The same mechanics carry three incompatible specifications:

| Value | master fieldwork_v30 (current line: PP-684, ED-773, AUD-NPC-01) | params/fieldwork.md (PP-632 line) | investigation_systems_v30 |
|---|---|---|---|
| Disposition range | **−3 to +5** (§5.1: "Disposition range: −3 to +5") | **−4 to Bonds** (header) — but label table stops at **+4 Devoted** with no +5 Bonded row | **−4 to floor(Bonds/2)+1** (§Architecture, Ontological Ledger table) |
| Disposition ceiling | **= Bonds** (§5.1, PP-684, "revised from PP-632 floor formula") | header "= Bonds (PP-684)" **but** lifepath derivation clamps to **[−4, floor(Bonds/2)+1]** (internal self-contradiction) | floor(Bonds/2)+1 |
| Disposition → Ob | **Stepped table** (§5.1 column: −3→+3 Ob … +4/+5→−2 Ob; caps at ±3/−2) | **"effective Ob = max(1, base Ob − Disposition). Direct subtraction; no stepped table"** (PP-632) | n/a |
| Knot model | **Strain model** (§5.6a/§5.6b ED-773/AUD-NPC-01): formation Spirit×2 TN 7 Ob 2; tiers Distant/Close, strain capacity 4/7; prerequisites Disposition +5 + TS ≥ 30 + Bonds ≥ 5 + count < floor(Bonds/2)+1 | **Tier-cost model** (PP-632): Pool = (Bonds×2)+3; tiers Close 5 / Medium 2 / Loose 1 pts; formation = Connect roll, Ob = tier, Disposition subtracted | inherits via Ledger table |
| Rupture floor | §5.6b break: "floor at −3 per **§3.5** Disposition range" — **§3.5 does not exist** (range lives in §5.1); rupture row resets Disposition to **−4** (per npc_behavior §3.5.4 / ED-664), **below the master's own −3 floor** | Rupture: Disposition → −4 (consistent with its −4 range) | — |

**Known-ledger overlap (extended, not duplicated):** ED-841 TIER-DRIFT-001 (3-way Knot tier contradiction, open), ED-842 COMPOSURE-DRIFT-001 (Composure 5 vs 4 citation, open), 2026-06-04 attributes-master F-DISP ("Disposition-cap formula contradictory: =Bonds (PP-684) vs floor(Bonds/2)+1 — P1 durable — resolve → =Bonds"). **New in this audit:** the Ob-application conflict (stepped vs subtraction — these produce different effective Obs at |Disposition| ≥ 2 and different caps), params/fieldwork's internal self-contradiction (header vs lifepath clamp vs +4-capped table), the master's internal −4-reset-vs-−3-floor conflict with its dead "§3.5" citation, and the consequential off-by-ones (Gift fails at "≤ −3" in params vs "≤ −2" in master §5.2; recovery threshold "≤ −3" params vs "≤ −2" infill §5.2).

**Resolution direction (Jordan's call; F-DISP argues ceiling = Bonds is the only value consistent with Knot candidacy at +5):** pick the master line, regenerate params/fieldwork from it, decide stepped-vs-subtraction and −3-vs-−4 floor explicitly. `[OPEN — Jordan]` on both value choices.

### P1-2 · Thread-Read primary attribute stale in params + split

Current canon: master §2.1 / §4.2 / §4.5 — Thread-Read pool = **(Spirit × 2) + History + TPS** (PP-619, PP-626; "Attunement struck from Thread contact pools"), confirmed by params/core §Attribute-Roles-Fieldwork (PP-628). Stale: **params/fieldwork** §Primary-Attribute table ("Thread-Read | Attunement (+ Thread Pool Score)") and §Thread-Read block ("Pool: (Att × 2) + History bonus + Thread Pool Score"); **fieldwork_investigation.md** §4.2/§4.5 step 3 ("Attunement × 2"). Wrong attribute on a core investigation action — the extracted-values file an implementer would consume rolls the wrong stat.

### P1-3 · Propagation / authority breakdown (root cause of P1-1/P1-2)

- PP-632 (Disposition redesign + Knot system) was applied to params/fieldwork + split files, **never to master fieldwork_v30**; PP-684/ED-773/ED-780/PP-628-era changes were applied to master, **never back-propagated** to params or splits. The two lines diverged in both directions and both are presented as live.
- Split files (`fieldwork_exploration.md`, `fieldwork_investigation.md`) self-describe as "canonical subsystem file" with Parent header → `designs/fieldwork/fieldwork_design_v1.md` — **path does not exist** (renamed to designs/scene/fieldwork_v30.md 2026-04-13 per master header). params/fieldwork header source path carries the same dead path.
- `references/canonical_sources.yaml` has **no fieldwork system key** (61 keys; only `investigation` → investigation_systems_v30.md), **despite** fieldwork_v30 §12 Propagation status claiming "canonical_sources.yaml | Fieldwork system entry | DONE (PP-575)". The claim is false against the live file.
- Master §5.6b cites **PP-719** ("PP-719 clarification per EC-F2.A-01") — PP-719 is absent from `canon/patch_register_active.yaml` (NOT FOUND) and has 0 ledger hits. Archived-or-unrecorded; either way the citation is unverifiable. `[GAP: PP-719 — no register or ledger record located]`
- Split divergences in both directions: splits lack master's Reconstruct-as-completion degree table (§4.1 — Failure→false conclusion) and retain pre-PP-628 content (exploration split uses pre-rename "RS" for MS; lacks Mode 1/2 distinction and §3.3a ED-676 map detectability); master lacks PP-632 content the splits carry.

---

## §3 P2 findings (cause ambiguity)

1. **ER-2 continuity correction unlanded × wound-floored fieldwork pools.** params/core §Pool Floor explicitly lists "wound-penalised fieldwork pools" at the 1D floor; Endurance-based exploration and Surveil take −1D/wound (master §2.2). The continuous engine without `net − (Ob − 0.5)` runs 4–32% low below ~5D (engine_replacement_reconciled §2); the term is recommended, not landed in params/core §Continuous Engine. TTRPG and videogame odds diverge exactly where wounded explorers operate. (Lesson 6 / P-iii; cross-filed RD-1.)
2. **Zero continuous-engine validation at fieldwork parameters.** Decision E covers fieldwork only "by construction" (ED-836/WS-D-1: validated at combat 5–17D TN 7; per-system sims not run). SIM-DEBT-FW-01..10 validated the **discrete d10** pre-Decision-E. `sim/personal/fieldwork.py` and `sim/personal/investigation.py` are Pass-2l armature stubs (NotImplementedError); investigation_systems' four subsystems have zero registered sim coverage (coverage_matrix: 0 hits for SOC-*/FW-*/fieldwork); SIM-DEBT-SOC-01..03 (fieldwork_editorial.md) unresolved with 0 ledger hits — and SOC-03's premise is stale (written against Composure = Cha+6; ED-694 changed it to Cha×3, min 3 < Knot-break damage 4, so the question it poses is live, not moot). (Lesson 2 verification obligation; cross-filed RD-2.)
3. **§10.5 d10 dice-face visualisation contradicts Decision E.** Master §10.5 specifies per-face d10 UI (skull/pip/checkmark/chain) for the Godot mode; canon resolution is the continuous magnitude gauge (params/core §Continuous Engine, Decision E). A raw-d10 presentation leak at the UI layer. (Lesson 3; cross-filed RD-5.)
4. **Niflhel text live after strike.** ED-600 (operatives dead, struck in arc_expansion) + params/fieldwork comment 2026-04-30 ("Niflhel struck... Replacement: settlement-broker social actions per settlement_layer §4.7-4.9") — but master §5.8 Niflhel Social Toolkit Extension and §6.3 "Niflhel social action +2" exposure row remain live, and the splits carry the same. supersession_register has no fieldwork/Niflhel entry.
5. **Naming drift: "Piety Track offset" vs "Conviction offset."** Master §2.3/§5.7 map Disposition to "Piety Track offset"; params/fieldwork §Contest Escalation says "Conviction offset." ED-302: the personal track is **Conviction (CV)**; "Piety/PT" is the separate 0–5 territory stat. Master's wording points social escalation at the wrong track.
6. **Pool-construction deviations on sub-5D pivotal rolls.** Sincerity Gate = bare Spirit (master §5.3, params; 1–7D — Lattice doc's "37% failure" implies bare Spirit 3); Knot formation = Spirit×2, no History (§5.6a; 2–14D). Both deviate from the canonical (Attr×2)+History construction; Knot formation at Spirit 1–2 puts a 4-season-cooldown outcome on 2–4D. Spirit as the attribute is intent-explicit (ED-503); the bare/no-History pool construction is not. `[INTENT UNDETERMINED]` (cross-filed RD-3.)
7. **Evidence-yield conflict, Lattice ↔ fieldwork degree table.** investigation_systems Outcome Types: "Evidence yield | Advances Evidence Track by 1" (flat) and Cross-System table reroutes Interview "through Dialogue Lattice + Response Matrix **instead of single Charisma roll**" — Interview is Attunement (master §2.1/§4.2), and the fieldwork schedule is +0/+1/+2/+3 by degree (§4.2). The rerouted Interview's progress schedule is unspecified and the doc mischaracterizes what it replaces.
8. **Pending decisions untracked.** NPE-01/NPE-02, DL-01/DL-02, RR-01 sit in a CANONICAL doc (investigation_systems, approved 2026-04-17) under "PENDING DECISIONS (not editorial — mechanical gaps requiring resolution)" with **0 ledger hits** — mechanical gaps in canon with no register entry. (ED-545 "substantially resolved, provisional" and ED-547 "scene cap IS the fieldwork resource, provisional" are the adjacent tracked items.)
9. **F3 Heresy Investigation lifecycle audit deferred-open** (fieldwork_lifecycle_stress_01 §1: F3 DEFERRED, "open follow-up") — the contested-investigation institutional form (§4.6) has no lifecycle verification.
10. **Depth-3 social gate divergence.** Master §1 scope note + §5.4 Socializing→Buried map the Depth-3 social tier to **Disposition +3**; params/fieldwork's Depth table gates it at **Disposition ≥ Bonds − 1 (PP-684)**. At Bonds 5 the two rules differ by one step; at low Bonds they diverge further. Same root as P1-1 (unpropagated lines) but a distinct live gate an implementer must pick.
11. **Evidence-threshold legibility unsuperseded.** Master §4.1: "the threshold is not known to the player"; investigation_systems' Case Board exposes legible tiers (3 = theory / 5 = leverage / 8 = proof) and the Godot Journal spec renders a current/threshold bar. TTRPG-era concealment vs videogame legibility — neither doc carries a supersession note, so both rules are live.
12. **Internal Exposure schedule conflict.** Master §6.3: failed investigation action → +1 Exposure (+2 only at Depth ≥ 3); master §4.2 degree table: Failure → +2, Partial → +1, at any depth. params/fieldwork reproduces both verbatim. Two answers to what a failure costs, inside one document.

---

## §4 P3 findings (polish)

1. Master §7 Derived Values stale parallels: "Composure (Cha + 6); Stamina (End + Hist + 1)" — ED-694: Composure = **Cha×3**, Stamina = **End×5**.
2. Cover range stated "2–14" (§7); achievable minimum is 1 (Cognition 1 + no relevant History).
3. params/fieldwork Gift threshold "≤ −3" vs master §5.2 "≤ −2"; recovery "≤ −3" vs infill "≤ −2" (instances of P1-1's range shift).
4. investigation_systems title "Proposal" vs Status: CANONICAL — title never updated on approval.
5. Mode-1 Anomaly Evidence-halving (after 3rd scene, §3.1) × non-sensitive Thread-verified halving (§4.3): stacking order unspecified (floor of floors vs sequential rounding differs at odd values).
6. `canon/definitions.yaml` does not exist — cited by both skills and the architecture spec; PI <definitions> is the operative NERS source. Infrastructure drift.
7. valoria-resolution-diagnostic SKILL Instance-A scope list omits fieldwork (lists combat/social/thread/mass) though Decision E assigns it; `/mnt/project` copy of the skill is a stale pre-engine-replacement version `[DRIFT: reading_documents — repo canonical used instead]`.
8. fieldwork_godot.md G10-F01..07: no fieldwork implementation exists in valoria-game as of 2026-04-13 (blockers A-02/A-05/B-03/DA-03) — status documentation, no drift found, but the doc predates Decision E and should be re-dated when touched.
9. Index headers carry `canonical_sha: unknown` (both fieldwork and investigation indexes).
10. Disposition decay threshold off-by-one: params "decays above +2" vs infill (ED-500 line) "Disposition ≥ +3 decays −1/season; ≤ +2 stable" — the maintenance rule shifted with the P1-1 range and only one side propagated.

---

## §5 Examined and sound — null results (trail per finding)

`[NULL: Five-Filter Chain — examined, nothing found]` All five filters' inputs (Certainty, TS, Conviction wounds, Disposition, Compromise Profile, Standing, ethical framework) are defined in the Ontological Ledger table or NPC Genome; chain is deterministic, ordered, with explicit pass/modify/block/escalate outcomes; full-chain example consistent. Mode C dependency map closed.
`[NULL: Scene-as-Graph + Traversal Economy — examined, nothing found]` Node taxonomy complete; costs expressed in the existing scene-time budget (no new resource); graph size scales with threshold.
`[NULL: Evidence Track — examined, nothing found]` Multi-threshold accumulator (3/5/8), persistent, no decay, progress-above-threshold inert — a deep clock, not a disguised binary; INV2/INV3 re-confirmed at full depth. Reconstruct-as-completion Failure→false-conclusion is design-explicit ("GM does not reveal the error") — intent-gated pass.
`[NULL: Exposure loop — examined, loop is damped and bounded]` Fail→+Exposure→Noticed +1 Ob is positive feedback, but: Success clears Desperate Trail and normalises; concealment −2, cover identity −1/scene, faction support −2/season; leave-territory and season resets; Compromised is a recoverable terminal; Church-AP feed capped +1/char +2/territory per season (PP-581: ~11% of max CI acceleration). Lesson-5 pass — deliberate with adequate safeguards.
`[NULL: Knot lifecycle state machine — examined, mature]` stress_01 verified 22/24 NERS cells (2 ⚠ Horizontal: low-Bonds lockout, pre-known); five-state machine closed post-ED-773. (Values themselves are P1-1's subject; the *machine* is sound on the master line.)
`[NULL: attribute basis — examined against 2026-06-04 reconciled master]` All fieldwork attributes survive; open items there (F-CONTEST two-canonical-contest-specs P1, Recall's fate, Spirit centrality) are Jordan's and cross-referenced, not re-opened here.
`[NULL: NPE — examined, bounded]` Season-end stance convergence is bounded by Volatility checks and ecology re-weighting; long-run homogenization is plausible but unsimmed — noted under P2-2, not asserted as a defect.
`[NULL: NPC name drift — examined, nothing found]` All 8 Lattice zoom-trigger NPCs (Lenneth, Elske, Haelgrund, Himlensendt, Almud, Baralta, Vaynard, Maret) verified verbatim against `references/npc_registry.yaml`. The `entities` SQL table returns empty for the set — registry, not the table, is the probative source.

---

## §6 Jordan decision points (consolidated)

1. `[OPEN — Jordan]` **Disposition→Ob rule:** stepped table (master §5.1, caps ±3/−2) vs direct subtraction with floor 1 (params PP-632). Different balance at |Disposition| ≥ 2; PP-684's note covers the ceiling only. `[INTENT UNDETERMINED]`
2. `[OPEN — Jordan]` **Disposition floor:** −3 (master §5.1) vs −4 (params + master's own §5.6b rupture reset). One value; propagate.
3. `[OPEN — Jordan]` **Canonical-line consolidation:** adopt master line (recommended; aligns with F-DISP "resolve → =Bonds"), regenerate params/fieldwork, demote or refresh splits, add fieldwork key to canonical_sources.yaml.
4. `[OPEN — Jordan]` **Knot model:** strain model (ED-773) vs PP-632 tier-cost model — ED-841's open TIER-DRIFT-001, now with the formation-roll conflict added.
5. `[OPEN — Jordan]` **Niflhel §5.8/§6.3 strike propagation** to master + splits (replacement: settlement-broker per settlement_layer §4.7–4.9).
6. `[OPEN — landing]` **ER-2 continuity term** into params/core §Continuous Engine (one line; no shift ≥5D by construction).
7. `[OPEN — Jordan]` **Sincerity/Knot pool construction** (bare Spirit / Spirit×2-no-History) — ratify as deliberate or normalize to (Attr×2)+Hist.
8. `[OPEN — Jordan]` **Lattice-rerouted Interview progress schedule** (flat +1 vs degree table) + NPE-01/02, DL-01/02, RR-01.
9. `[OPEN — Jordan]` **Evidence-threshold legibility:** declare videogame-mode supersession of §4.1's hidden-threshold rule (Case Board/Journal already expose 3/5/8) or restore concealment in the UI spec.

---

## §7 Confidence, gaps, trail

`[CONFIDENCE: high]` — P1-1/P1-2/P1-3: every cell in the §2 table is a verbatim value from a full-document read this session; the contradictions are textual, not interpretive.
`[CONFIDENCE: high]` — null results in §5: each rests on a full read of the governing sections plus the stress-01/PP-581 evidence cited inline.
`[CONFIDENCE: medium]` — RD-2's practical impact (unvalidated ≠ wrong; CLT argument is plausible, just unverified at fieldwork's TN ladder and modifier stack).
`[GAP: PP-719 — cited in master §5.6b; absent from active register and ledger]`
`[GAP: SIM-DEBT-SOC-01..03 — opened in fieldwork_editorial.md; no resolution or coverage-matrix record]`
`[GAP: omega framework — not read; NERS retained as verdict per skill note]`

Audit trail: `[READ:]` entries for every file in §0 were emitted at fetch time in-session; Phase tags and Stage outputs live in `resolution_diagnostic_fieldwork.md` and `ners_verdict_fieldwork.md` (this folder). Read additionally: `designs/audit/2026-06-03-contest-groundup/EVIDENCE_PRESSURE_VALIDATION.md` (4,207 chars), `references/npc_registry.yaml` (name verification), `references/lane_assignments.yaml`. All findings are staged append-ready in `ledger_candidates_jsonl_ready.jsonl` (this folder), P1 rows first. `[DRIFT: task_gate('audit') P1-append — this session declared no lane; per references/lane_assignments.yaml ID discipline (allocate EDs only from a reserved block) the append is staged for Lane A to file, matching the 2026-05-28 ledger_candidates_jsonl_ready precedent.]`
