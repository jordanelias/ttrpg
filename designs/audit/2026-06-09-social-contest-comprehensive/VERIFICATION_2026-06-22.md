# Social-Contest Audit — Round-2 Adversarial Re-Verification (2026-06-22)

Completes the rate-limit-errored verification pass over the 10 social-contest findings raised in
[`ANALYSIS.md`](ANALYSIS.md). Each finding was re-checked by an independent **3-lens panel**
(literal-evidence / context / canonical-direction); a finding is **confirmed** at ≥2 of 3 real votes.
Source harness: `tools/observability/social_contest_reverify.workflow.js`. Run: 30 agents, no
rate-limit failures (the earlier throttling has cleared).

## Bottom line — 9 / 10 confirmed

| # | ID | Sev | Votes | Verdict |
|---|---|---|---|---|
| 1 | **C1-CONCENTRATION** | critical | 3/3 | CONFIRMED — two live Concentration formulas + two depletion rates; ED-902-struck `Focus×3` survives in 4 places |
| 2 | **C2-CHA-FOC-X3** | critical | 3/3 | CONFIRMED — ×3 Cha-mod/Foc-defence scaling in the summary but not in the strain-computing §4 rules/params (factor-of-3 swing) |
| 3 | **C3-SIM-FIDELITY** | critical | 3/3 | CONFIRMED — `sim/personal/contest.py` is CLASH-only; no strain/Concentration/interaction-types; over-applies Contest Fatigue; tie→A bug. Sim conclusions invalid for current ruleset |
| 4 | **M1-RATTLED-CHANNEL** | major | 3/3 | CONFIRMED — Rattled still `+Ob` in spec §4/§6 and canonical derived_stats §5.1, violating the Decision-B/PP-716 −1D channel reservation |
| 5 | **M2-RECALL-LINGER** | major | 2/3 | CONFIRMED — Recall (removed from Concentration by ED-694) still inflates the Appraise pool and the §9.2 coalition Concentration pool |
| 6 | **M5-FIRST-TO-SPEAK** | major | 3/3 | CONFIRMED — spec resolved to ROLLED (ED-581) but params still deterministic + treats ED-138 as open |
| 7 | **M6-RESIST-EROSION** | major | 3/3 | CONFIRMED — ED-864 per-exchange vs ED-582 chain-Deadlock erosion unreconciled; stale "ED-295 awaiting resolution" block persists in params |
| 8 | **m1-TERMINOLOGY** | minor | 3/3 | CONFIRMED — pervasive spec↔params naming drift; "Coalition Push" cited but never defined |
| 9 | **CM5R-PIETY-PERSUASION** | major | 2/3 | CONFIRMED — resolution track is "Persuasion Track" in spec/params/sim but canonical (derived_stats §14.2/§11, npc_behavior) is "Piety Track" |
| — | **M3-APPRAISE-POOL** | major→**re-framed** | 1/3 | NOT confirmed *as written* — see below |

**Severity of confirmed set:** 3 critical · 5 major · 1 minor.

## M3-APPRAISE-POOL — re-frame, do not drop

The panel refuted the **"three different ways"** framing, not the existence of a defect:

- The 3rd cited variant — `params/contest.md:70` Exchange-Structure `"Read (Attunement, TN 7, Ob 1)"` —
  is **explicitly struck in its own file's patch log**: `## PP-614/PP-278 — Appraise (canonical)` …
  *"Old 'Read pool = Attunement only Ob1' struck"* and *"Step 1 renamed from 'Read' to 'Judge'"* (PP-254).
  So it is stale-but-undeleted text, not a live third spec.
- A **genuine two-way contradiction survives**: spec §4 (`social_contest_v30.md:121`, Attunement-only / Ob 1)
  vs params Pools (`params/contest.md:23`, **Attunement + Recall / Ob = opponent Cha÷2**).
- **There is a canonical winner already:** PP-614/PP-278 = **Attunement + Recall, Ob = opponent Cha÷2 (round up, min 1)**.
  derived_stats §14 is silent here; the sim implements no Appraise step at all.

**Corrected classification:** not "needs a ruling," but a **propagation/cleanup task with a known target** —
propagate the PP-614 form into spec §4 Step 1, and delete the struck "Read" line from the params
Exchange-Structure section. Downgrade live-ambiguity severity to **minor**; the underlying drift is real.

## Disposition (proposals — Lane A to file; nothing self-filed)

These are **canon/params content fixes → Lane A** (`designs/scene/**`, `params/**`). The fixes are
write-disjoint from the in-flight territory/observability lanes. Suggested order:

1. **C1 + C2** (critical, same files): propagate `(3×Focus)+(2×Spirit)` (range 5–35) and one depletion rate;
   make §4 resolution rules + params §Derived carry the ×3-scaled Cha-mod/Foc-defence. Targets: derived_stats §5.2,
   social_contest §4/§8, contest_extensions PP-NEW-D, sim.
2. **M1** (engine invariant): Rattled → −1D in social_contest §4/§6 and derived_stats §5.1.
3. **CM5R**: rename "Persuasion Track" → "Piety Track" in social_contest_v30, params/contest.md, sim.
4. **M2 / M3(re-framed) / M5 / M6 / m1**: Appraise/Recall reconciliation; first-to-speak→rolled + close ED-138;
   one resistance-erosion model + delete stale ED-295 block; one glossary + define/rename "Coalition Push".
5. **C3** (Lane C): bring `sim/personal/contest.py` to §4/§6/§14.4, or banner it a reduced model and stop citing it as validation.

> These map to **workplan v4 docket J-31 (contest D-1…D-10)**. Filing them is a Lane-A structural op
> (ID allocation from reserved ED 890–939) and is **Jordan-gated** — staged here, not committed.
