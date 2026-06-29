# AUDIT REPORT: NPC Roster & Behavior System (v30) — Comprehensive

## Date: 2026-06-22
## Auditor: Claude (Opus 4.8) — multi-agent workflow (partial) + direct analysis
## Audited: designs/npcs/{npc_roster_v30(.md/_infill), npc_behavior_v30(.md/_infill), npc_character_analyses_v30(.md/_infill), npc_relational_graph_v30.md, npc_foils_v30.md, character_canon_v30.md, edeyja_npc.md, baralta_v30.md, companion_specification_v30.md}
## Against: canon/02_canon_constraints.md (P-01…P-15, GD-1…GD-3), canon/00_philosophical_foundations.md, canon/03_canonical_timeline.md, canon/supersession_register.yaml, canon/placeholder_names.yaml, canon/editorial_ledger.jsonl, CLAUDE.md naming rule

---

## Method & Coverage Note

This audit was launched as an `ultracode` multi-agent workflow (14 per-NPC auditors + 6 system-level
checks → adversarial verify → synthesis). The agent fleet was interrupted by a **transient
server-side rate-limit** (run 1) and then by a **hard account monthly spend limit** (runs 2–3,
`claude.ai/settings/usage`), which prevented the verify and synthesis stages and 12 of 14 per-NPC
agents from completing.

**What survived as agent output:** full audits of **Maret Uln** and **Sæmund Haelgrund** (run 1).
**Everything else here** was completed by direct main-loop analysis of the source files. Where a
finding is agent-produced it is tagged `[agent]`; direct findings are tagged `[direct]`. The
adversarial-verify pass did **not** run, so treat severities as first-pass (the two `[agent]` units
were self-consistent and well-evidenced, but not independently refuted).

**Remaining work (recommended once spend limit clears):** a per-NPC deep pass on the other 11 roster
NPCs (Edeyja, Vossen, Torsvald, Brandt, Feldhaus, Almstedt, Strand, Virke, Laskaris, Solberg,
Tormann) and the leader tier (Almud, Himlensendt, Baralta), plus the formal system checks. The
workflow is **resumable**: `Workflow({scriptPath: ".../npc-audit-wf_a6c7a620-0b7.js", resumeFromRunId: "wf_a6c7a620-0b7"})`.

---

## Summary

20 findings. **6 HIGH** (1 canon GD-1, 2 contradiction, 1 gap, 2 identity/contradiction),
**7 MEDIUM**, **3 LOW**, **4 NOTE/PASS**.

By category: contradiction ×7, gap ×5, canon ×3, naming ×1 (resolves to NOTE), note/pass ×4.

**Cross-cutting patterns:**
1. **Legacy bleed-through.** The v30 behavior infill inherited struck mechanics verbatim from the
   pre-v30 `npc_behavior_system_v1.md` — most seriously the **GD-1-violating co-victory** content
   (AUD-NPC2-01) and Vaynard-coded mechanics (VTM, AUD-NPC2-03).
2. **Two disjoint NPC tiers.** A *leader tier* (Almud, Himlensendt, Baralta, Vaynard, Edeyja,
   Lenneth, Torben) is statted in `npc_behavior_v30.md`, the relational graph, and foils; a
   *secondary roster* (the 13 named NPCs) is statted in `npc_roster_v30.md`. The two barely
   reference each other — the secondary roster is almost absent from the relational graph and foils
   (AUD-NPC2-12), and at least one roster NPC (Sæmund Haelgrund) has no behavior stat block at all
   (AUD-NPC2-05).
3. **Skeleton/infill drift.** Several NPCs disagree between their skeleton and infill files
   (Dalla Virke AUD-NPC2-13; Strand/Solberg mode coverage AUD-NPC2-16), and intra-file
   resolved-vs-open ED bookkeeping is stale (AUD-NPC2-07).
4. **Transformation arcs under-specified vs P-12.** Drift/Coherence arcs are described as a single
   "track degrades" without the tridimensional knot-strain propagation P-12 requires
   (AUD-NPC2-08, AUD-NPC2-10).

---

## RECOMMENDED FIX PRIORITY

1. **AUD-NPC2-01 (HIGH, GD-1):** Strike all co-victory content from `npc_behavior_v30_infill.md`
   (lines 67, 98, 180) — Peninsular Sovereignty is the sole victory condition.
2. **AUD-NPC2-03 (HIGH):** Re-express Maret's succession effect off the struck VTM mechanic (use WR per PP-663).
3. **AUD-NPC2-04 (HIGH):** Reconcile Maret (and Varfell framing) with ratified ED-787 ("not intelligence-themed").
4. **AUD-NPC2-02 (HIGH):** Pick one canonical Maret TS (35 vs ~50) and propagate.
5. **AUD-NPC2-05 / -06 (HIGH):** Author Sæmund Haelgrund's behavior stat block; disambiguate from Lennart Haelgrund.
6. **AUD-NPC2-12 (MED):** Decide whether the secondary roster belongs in the relational graph / foils; close the coverage gap or document the tier split.
7. **AUD-NPC2-13, -07, -08, -09, -10, -11 (MED):** Skeleton/infill + ED + P-12 reconciliations.
8. LOW/NOTE: address opportunistically.

---

## FINDINGS TABLE

| ID | Unit | Category | Severity | Constraint/Ref | Title |
|----|------|----------|----------|----------------|-------|
| AUD-NPC2-01 | Almud / behavior infill | canon | HIGH | GD-1 | Live "co-victory" content violates sole-victory-condition rule |
| AUD-NPC2-02 | Maret Uln | contradiction | HIGH | TS value | Thread Sensitivity stated as both ~50 and 35 |
| AUD-NPC2-03 | Maret Uln | canon | HIGH | VTM-STRIKE / PP-663 | Succession arc depends on struck VTM mechanic |
| AUD-NPC2-04 | Maret Uln | contradiction | HIGH | ED-787 | Built as intelligence specialist; Varfell ratified "not intelligence-themed" |
| AUD-NPC2-05 | Sæmund Haelgrund | gap | HIGH | behavior §2 | No behavior stat block despite contest-mechanic dependency |
| AUD-NPC2-06 | Sæmund / Lennart Haelgrund | contradiction | HIGH | identity | Two NPCs share surname + TS 12 (hidden); ambiguous refs |
| AUD-NPC2-07 | Maret Uln | contradiction | MEDIUM | ED-397/398 | Marked resolved in stat block but still open in same file |
| AUD-NPC2-08 | Maret Uln | gap | MEDIUM | D3 floor / P-12 | No base (pre-succession) stat block; arc not tridimensional |
| AUD-NPC2-09 | Sæmund Haelgrund | contradiction | MEDIUM | Certainty | Certainty 4 (§7.10) vs 3 (§2.14) |
| AUD-NPC2-10 | Sæmund Haelgrund | canon | MEDIUM | P-12 | Arc C Coherence drift lacks tridimensional knot-strain |
| AUD-NPC2-11 | Sæmund Haelgrund | gap | MEDIUM | roster §4 | Roster entry omits Beliefs/Conviction/Ethics carried by peers |
| AUD-NPC2-12 | Relational graph / Foils | gap | MEDIUM | graph/foils purpose | Secondary roster (13 NPCs) largely absent from both |
| AUD-NPC2-13 | Dalla Virke | contradiction | MEDIUM | skeleton vs infill | "Independent, Niflhel DISSOLVED" vs "operates for active Virke family" |
| AUD-NPC2-14 | Maret Uln | contradiction | LOW | character_canon D2 | Ethics in two vocabularies (Rawlsian vs Equity/Conviction) |
| AUD-NPC2-15 | Sæmund Haelgrund | gap | LOW | relational graph | No Haelgrund→Olafsson patron-client edge |
| AUD-NPC2-16 | Strand & Solberg | gap | LOW | Mode Interface Matrix | Missing mode-bridge text all peers carry |
| AUD-NPC2-17 | Baralta | note | NOTE | ED-400 | Conviction Order→Precedent pending user approval; doc PROVISIONAL |
| AUD-NPC2-18 | Naming (all v30) | note | NOTE | naming rule | v30 clean of "Galbados"; Vaynard/Almud/Himlensendt are LIVE names |
| AUD-NPC2-19 | Edeyja / Sæmund | note | PASS | P-08 | Moral-anchor + Diagnosis-reveal arcs are P-08 compliant |
| AUD-NPC2-20 | Stat-scale | note | PASS | 1–7 scale | No >7 stat violations found; roster numeric blocks deferred |

---

## HIGH

### AUD-NPC2-01 — GD-1 VIOLATION: live "co-victory" content in the NPC behavior infill `[direct]`
**Constraint:** GD-1 — Peninsular Sovereignty is the **sole** victory condition; "Does any 'co-victory' or 'shared victory' mechanic exist? If yes → FAIL."
**Issue:** Three live passages in the v30 behavior infill define co-victory mechanics: Almud's reform arc is a "Crown-Restoration **co-victory** enabler"; Vaynard's awakening "Varfell-Restoration **co-victory** path opens"; and there is a dedicated "**Co-victory cooperation**" AI sub-tree ("When co-victory conditions are ≥ 75% met, cooperating factions shift to a simplified tree…"). All three are struck by GD-1. They are inherited verbatim from the pre-v30 `npc_behavior_system_v1.md`.
**Evidence:** `designs/npcs/npc_behavior_v30_infill.md:67`, `:98`, `:180`; legacy origin `designs/npcs/npc_behavior_system_v1.md:422`, `:497`.
**Fix:** Strike or rewrite all three to express tactical leverage *toward* universal Peninsular Sovereignty, not a shared/alternate win path. Add `[SUPERSEDED-BY: GD-1]` markers per the §B cross-reference convention.

### AUD-NPC2-02 — CONTRADICTION: Maret Uln TS stated as both ~50 and 35 `[agent]`
**Issue:** Maret's TS is ~50 in the roster/analyses but 35 in the behavior tree, companion spec, and conviction-vector table — and the 35 value is stamped "ED-397 resolved," so ~50 is not a loose approximation the lower value refines.
**Evidence:** TS ~50: `npc_roster_v30.md:30`, `:238`; `npc_roster_v30_infill.md:17`; `npc_character_analyses_v30_infill.md:15`. TS 35: `npc_behavior_v30.md:240`, `:1194`; `companion_specification_v30.md:88`. (Note: `npc_roster_v30_infill.md:32` gives **Sigrid Torsvald** TS 35 consistently — do not conflate.)
**Fix:** Pick one canonical TS. If 35 is the ED-397 resolution, correct the roster/analyses "~50" refs (and the prose that leans on ~50 perception). If ~50 is base-state and 35 a post-succession reset, state the gating explicitly in both docs.

### AUD-NPC2-03 — CANON: Maret's succession arc depends on VTM, a struck mechanic `[agent]`
**Constraint:** `supersession_register.yaml` VTM-STRIKE-2026-04-19 ("VTM STRUCK entirely") / PP-663.
**Issue:** Maret's signature succession outcome is "VTM resets to 0 / VTM → 0." VTM (Vaynard Thread Mastery) was struck in full and the behavior tree rebuilt (PP-663) to change Varfell's clock from VTM to WR. The roster/analyses hinge her mechanical payoff on a mechanic that no longer exists.
**Evidence:** VTM as live canon: `npc_roster_v30.md:33`, `:239`, `:240`; `npc_character_analyses_v30_infill.md:18`. Strike: `canon/supersession_register.yaml:37-49`. Behavior doc already de-VTM'd: `npc_behavior_v30.md:832, 836, 1144, 1146, 1177`.
**Fix:** Rewrite Maret's succession effect in `npc_roster_v30.md` and `npc_character_analyses_v30_infill.md` to use the surviving Varfell clock (WR) or another canonical quantity.

### AUD-NPC2-04 — CONTRADICTION: Maret is an intelligence specialist; Varfell is canonically "not intelligence-themed" `[agent]`
**Constraint:** ED-787 (P1, closed 2026-05-03 with signoff) / `canon/03_canonical_timeline.md:144`.
**Issue:** Maret's whole identity ("intelligence operative," serving "an intelligence faction that weaponises information asymmetry," priority tree built on Tribune Investigate / "maximise information advantage") codes Varfell as the intelligence faction. ED-787 revised Varfell to "opportunist/revolutionary … not intelligence-themed."
**Evidence:** `npc_roster_v30.md:30`, `:238`; `npc_roster_v30_infill.md:18`; `npc_behavior_v30.md:832-834, 923, 1144-1146`. Canon: `canon/editorial_ledger.jsonl:522` (ED-787); `canon/03_canonical_timeline.md:144`.
**Fix:** Re-theme Maret toward an opportunist/revolutionary frame, or file an ED noting her as a deliberate personal exception with rationale in-doc.

### AUD-NPC2-05 — GAP: Sæmund Haelgrund has no behavior stat block, yet his core mechanic needs one `[agent]`
**Issue:** The Inquisitor's signature interaction is the contest/Resonant-Style social scene ("Social scenes with Haelgrund use the contest system — he argues from evidence"), which requires Conviction, Ethical Framework, Resonant Styles, Certainty, Beliefs, and Leadership Deviation Ob. Peers have full §2.x blocks; Sæmund has none. The only "Haelgrund" block in the behavior doc is the unrelated Ministry Registrar **Lennart** Haelgrund (§2.14).
**Evidence:** `npc_roster_v30.md:260`; full blocks at `npc_behavior_v30.md` §2.2 (Himlensendt) and §2.14 (Lennart); no §2.x block for the Inquisitor; `npc_behavior_v30_index.md` lists only §2.14.
**Fix:** Author a §2.x block for Sæmund Haelgrund (Conviction Order/Faith; Ethics Deontological per infill; Resonant Style Evidence; Certainty; 3 Beliefs; Leadership Deviation Ob; the three arc branches) and disambiguate from §2.14.

### AUD-NPC2-06 — CONTRADICTION: two NPCs share surname "Haelgrund" and TS 12 (hidden) `[agent]`
**Issue:** Sæmund Haelgrund (Church Inquisitor, TS 12 hidden) and Lennart Haelgrund (Ministry Registrar, TS 12 hidden, buried Thread knowledge) are different characters with the same surname, TS, hidden status, and "proceduralist with buried knowledge" profile. Many references say only "Haelgrund." The §7.10 stat table has a single unqualified "Haelgrund | 12 (hidden) | 4" row.
**Evidence:** `npc_roster_v30.md:56, 63`; `npc_behavior_v30.md:299, 308` (Lennart), `:1195` (unqualified); bare "Haelgrund" at `npc_roster_v30.md:172, 194, 262, 375`.
**Fix:** Rename one (the Registrar is the easier rename) or qualify every reference with the first name; split the §7.10 row into two.

---

## MEDIUM

### AUD-NPC2-07 — CONTRADICTION: ED-397/398 "resolved" in stat block but still "open" in same file `[agent]`
**Evidence:** Resolved: `npc_behavior_v30.md:240-241`. Still open (P3): `npc_behavior_v30.md:1069-1070`.
**Fix:** Strike/mark-resolved the open-decisions rows if truly resolved; else remove the "resolved" tags.

### AUD-NPC2-08 — GAP: Maret has no base (pre-succession) stat block; arc not tridimensional `[agent]`
**Constraint:** character_canon D3 texture floor / P-12.
**Issue:** The only full Maret block (`npc_behavior_v30.md` §2.10) is gated "Activates only if Vaynard is eliminated." Her primary on-board state has no Conviction/Certainty/Resonant Style/Belief block, and her dual-loyalty "CONFLICTED" shift is narrated morally without tridimensional knot-strain.
**Evidence:** `npc_behavior_v30.md:229-246`; `npc_character_analyses_v30_infill.md:16-18`.
**Fix:** Author a base-state block; if the shift is a Coherence/drift arc, express it tridimensionally (P-12).

### AUD-NPC2-09 — CONTRADICTION: Haelgrund Certainty 4 vs 3 `[agent]`
**Evidence:** `npc_behavior_v30.md:1195` (Certainty 4) vs `:309` (Lennart, Certainty 3 Questioning).
**Fix:** Reconcile once the two Haelgrunds are disambiguated; give Sæmund an explicit Certainty.

### AUD-NPC2-10 — CANON: Haelgrund Arc C Coherence drift lacks tridimensional knot-strain `[agent]`
**Constraint:** P-12 ("knot-strain … not a single generic strain value"); P-10 framing test passes (drift correctly non-moral).
**Evidence:** `npc_character_analyses_v30_infill.md:28`; `canon/02_canon_constraints.md:19, 21`.
**Fix:** Specify Arc C drift across actuality/intelligibility/temporality and define knot propagation (handlers, Olafsson, case history).

### AUD-NPC2-11 — GAP: Haelgrund roster entry omits Beliefs/Conviction/Ethics carried by peers `[agent]`
**Evidence:** `npc_roster_v30.md:56-66` (only TS + Arc trigger) vs peers `:96-98` (Feldhaus), `:119-121` (Strand); content only in `npc_roster_v30_infill.md:23-28`.
**Fix:** Ensure the merged roster surfaces Ethics (Deontological), Behavioral AI (PROCEDURALIST), and ≥1 explicit Belief at peer depth.

### AUD-NPC2-12 — GAP: the 13-NPC secondary roster is largely absent from the relational graph and foils `[direct]`
**Constraint:** purpose of `npc_relational_graph_v30.md` (canonize NPC-NPC ties) and `npc_foils_v30.md`.
**Issue:** Across all 13 roster surnames there are only **4** total occurrences in the relational graph and **0** in the foils skeleton. Both docs model the *leader tier* (Almud, Himlensendt, Baralta, Vaynard, Edeyja, Lenneth, Torben). The secondary roster therefore has essentially no canonized relational ties or foil pairings — including patron-client ties the docs explicitly enumerate (e.g. Haelgrund→Olafsson, Maret↔Vaynard, Brandt↔Ehrenwall, Strand↔Almud).
**Evidence:** Grep of `npc_relational_graph_v30.md` for the 13 names → 4 hits; grep of `npc_foils_v30.md` → 0 hits; foil/edge taxonomies at `npc_relational_graph_v30.md:50`.
**Fix:** Decide the design intent. If the secondary roster is meant to be in-graph, add their edges (at minimum the canonical patron-client/loyalty ties named in the roster). If foils/graph are intentionally leader-only, state that scope in both docs' headers so the omission isn't read as a gap.

### AUD-NPC2-13 — CONTRADICTION: Dalla Virke skeleton vs infill `[direct]`
**Issue:** The roster skeleton titles her "Independent Intelligence Broker (formerly Niflhel — **DISSOLVED**)," but the infill describes her as operating "for the **Virke family** … one of several competing syndicate houses" that are clearly active ("They compete with at least three other major syndicates"), and titles her "**Syndicate** Broker (Niflhel)." Independent-vs-family and Intelligence-vs-Syndicate and DISSOLVED-vs-active all disagree.
**Evidence:** `npc_roster_v30.md:125` (skeleton) vs `npc_roster_v30_infill.md:52-56` and index/summary "Virke syndicate."
**Fix:** Pick one status. Either Niflhel/Virke family is dissolved and she's independent (update the infill), or the family is active and she's its broker (update the skeleton title).

---

## LOW

### AUD-NPC2-14 — CONTRADICTION: Maret Ethics in two vocabularies `[agent]`
**Evidence:** `npc_roster_v30_infill.md:18` ("Rawlsian") vs `npc_behavior_v30.md:235-237` (Conviction Equity/Reason + Ethical-Framework hybrid); `character_canon_v30.md:427` (D2: Ethical-Framework labels superseded as mechanical drivers).
**Fix:** State the canonical Conviction vector once; demote "Rawlsian" to a descriptive tag per D2.

### AUD-NPC2-15 — GAP: Haelgrund absent from the relational graph despite canonical ties `[agent]`
(Specific instance of AUD-NPC2-12.) **Evidence:** `npc_roster_v30_infill.md:24` (reports to Cardinal Olafsson); no match in `npc_relational_graph_v30.md`.
**Fix:** Add a Haelgrund→Olafsson patron-client edge with the defection-rupture trigger, or note field inquisitors are below the graph's threshold.

### AUD-NPC2-16 — GAP: Strand and Solberg missing Mode Interface bridge text `[direct]`
**Constraint:** Mode Interface Matrix — "Every NPC must have meaningful presence in at least 2 of 3 modes."
**Issue:** Every roster NPC has a "**Mode bridge:**" paragraph except Gerik Strand (#9) and Rikard Solberg (#12), whose Mode Interface subsections are header-only.
**Evidence:** `npc_roster_v30_infill.md:94` (Strand, header only), `:99` (Solberg, header only); contrast `:81, 85, 87, 89, 91, 93, 96, 98, 101`.
**Fix:** Author mode-bridge text for Strand and Solberg, or confirm the omission is intentional.

---

## NOTES / PASS

### AUD-NPC2-17 — NOTE: Baralta Conviction change (ED-400) pending approval; doc PROVISIONAL `[direct]`
Baralta's Primary Conviction was changed from Order (stage6) to **Precedent** with an in-doc flag `[EDITORIAL: ED-400 … User approval required]` (`npc_behavior_v30.md:91`). Separately, `baralta_v30.md` is wholly marked PROVISIONAL pending Jordan editorial review, with an open `[EDITORIAL ITEM]` to refine "she does not question the Church's theology" → "…theological content" (`baralta_v30.md:1, 6, 25`). Both await user ratification. (This is the resolution of the prior audit's AUD-NPC-04; the flag now exists.) **No fix — needs user decision.**

### AUD-NPC2-18 — NOTE: naming is clean in v30; superseded *names* vs superseded *mechanics* `[agent+direct]`
The CLAUDE.md rule "always Solmund, never Galbados" is satisfied in v30: **no occurrence of "Galbados" in any `*v30*` NPC doc** (the 310 earlier hits and the 52 repo-wide "Galbados" hits are legacy `npc_behavior_system_v1.md`, archives, and hook/test fixtures). "Vaynard," "Almud," and "Himlensendt" are **live canon character names** (e.g. Duke Magnus Vaynard, `canon/03_canonical_timeline.md:144`; King Almud Almqvist, `npc_behavior_v30.md:46`; Confessor Arne Himlensendt, `:66`) and appear in **neither** `supersession_register.yaml` nor `placeholder_names.yaml`. What is struck is Vaynard-**coded mechanics/flavor** (VTM — see AUD-NPC2-03 — and `varfell_mandate_action`), not the names. **Do not scrub these names.** If the project intends to retire any of them, file a separate supersession entry.

### AUD-NPC2-19 — PASS: P-08 compliance at the most likely failure points `[agent+direct]`
Edeyja is correctly framed as the moral anchor whose inability to transmit Thread knowledge to non-sensitives *is* P-08 (`npc_roster_v30_infill.md:15`). Haelgrund's Diagnosis-reveal arc gates on a PC with TS ≥ 30 diagnosing the NPC's latent capacity (not using Thread-level evidence to act against a TS<30 NPC), so P-08 is not triggered (`npc_roster_v30.md:65`; `npc_character_analyses_v30.md:49`). The Himlensendt/Vaynard Arc-C "Thread-level evidence becomes valid only if TS crosses Stirring (30+)" gate (`npc_behavior_v30_infill.md:114`) is the correct P-08 mechanic. **No fix.**

### AUD-NPC2-20 — PASS: stat-scale `[direct]`
No stat values outside the 1–7 scale were found in `npc_behavior_v30.md`. The roster carries **no numeric stat blocks** by design ("Stat blocks will be generated after identities are confirmed," `npc_roster_v30.md:104`). The one fractional mechanic (Aldric Tormann −0.5 Mandate) has a defined rounding/application rule ("tracked fractionally, applied at Year-End: −1 per 2 territories squeezed," `npc_roster_v30.md:161`). **No fix** — but full per-stat verification of §7.10 was not exhaustively machine-checked (see Coverage Note).

---

*End of audit. Per-NPC deep passes for the 11 un-agented roster NPCs + leader tier remain
outstanding pending spend-limit clearance; resume the `npc-audit` workflow to complete them.*
