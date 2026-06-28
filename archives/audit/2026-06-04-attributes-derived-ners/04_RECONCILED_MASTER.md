# Valoria — Character Attributes & Derived Stats · NERS Audit · CONSOLIDATED MASTER

**Date:** 2026-06-04 · **Status:** consolidated master — **supersedes** stage artifacts `00`–`03` for going-forward use (they remain the work trail); **reconciles + extends** the `2026-05-08-character-mechanics-critical-audit`.
**Method:** 5-turn dual-instrument all-directions audit (structural NERS via `mechanic-audit` lens + rolling-engine Property Test via `resolution-diagnostic`) → comparative critique vs acclaimed games → adversarial pass → Stage-4 re-test. Bootstrap-grounded; every mechanical claim cited.
**Authority:** mechanical-tier — all recommendations **Jordan-vetoable**; **canon-structure items** (roster architecture, the contest-spec choice, Recall's fate, Spirit-centrality intent) are **Jordan's adjudication — flagged, not decided.**

---

## 1 · The original worry, answered (5-turn grounded)
**"Recall and Bonds are bad stats" — not symmetric, and "bad" mislocates the real defect.**
- **Bonds = KEEP (sound).** A relationship-capacity attribute (Disposition cap, Knot pool `(Bonds×2)+3`, Socializing, Corroborate) — the Persona/Fire-Emblem pattern; graded **N:critical** by the 2026-05-08 audit. Only blemish: the Disposition-cap formula contradiction (fixable — §F-DISP).
- **Recall = the genuinely weakest attribute — but a *decision*, not a verdict.** It is thin and is half of a real balance asymmetry, **but** it currently has ~5 *declared-canonical* roles (the contest-spec question is unresolved), and acclaimed design proves a recall stat can be excellent if fed (Disco Elysium *Encyclopedia*, Pillars *Lore*). Its fate is entangled with an unresolved canonical contradiction. **Three live paths, Jordan's call (§F-RECALL).**
- **What the worry actually surfaced:** the roster's **Spirit↔Recall balance asymmetry** (one over-central, one under-used) and a **two-canonical-contest-specs contradiction** that makes Recall undecidable. Recall is the *symptom*; these are the *findings*.

## 2 · Final NERS verdict (post-adversarial, Stage-4-qualified)
**SYSTEM:** character attributes (flat 1–7) + `derived_stats_v30` (PROPOSAL) · **rolling engines fed:** Instance A (combat/social), Instance B (faction, adjacent)
**VERDICT: NOT NERS-clean — but the durable failures are narrower than the Turn-2 read, and are mostly *contingent-on-Jordan-decisions* + *doc-hygiene*, not mechanical breaks. Individual mechanics are mostly sound.**

- **N — PARTIAL FAIL.** The **Spirit/Recall asymmetry**: Recall under-necessary (thinnest), Spirit over-necessary (5 downstream). *Qualifier (Stage-4): Spirit-centrality is likely **deliberate** (ratified S1 + ED-902 both added Spirit) — so the firm half is "Recall is under-necessary," and even that is contingent on the contest-spec decision.*
- **R — PARTIAL FAIL.** Durable basis = the **Disposition-cap cross-doc contradiction** (a reader of `complete_systems_reference` gets the wrong cap). The rest of Turn-2's "rot" was **transient edit-lag from today's changes** (P3) or the reframed §1 rule (P3) — not structural.
- **S — PARTIAL FAIL.** Durable basis = **two contest specs both declared canonical** (B1) + **no single canonical roster doc** + the **Spirit naming collision (F9)**. The lateral combat-vs-sibling split is acclaimed-normal → a documentation gap, not a failure.
- **E — PARTIAL FAIL.** **No single roster doc** + **vestigial Mind/Body/Spirit framing** over a flat live system + Spirit-overload obscuring the economy + Recall as the thin-payoff stat.

**Engine-fitness (rolling part): PASS for attributes-as-inputs.** Agility-as-σ-leverage is the correct C-04 fix. Live caveats (continuity correction not landed; ED-875 low-input leverage) are **engine-level, not attribute-level**.

## 3 · Reconciled finding ledger (single source of truth on findings)
| ID | Finding | Severity | Status after adversarial + Stage-4 | Basis |
|---|---|---|---|---|
| **F-ASYM** | Spirit over-central + Recall too thin (balance asymmetry) | **durable** | **survives** — Spirit-half likely **deliberate** (confirm intent); Recall-half firm but contingent | Mode-C downstream counts; D&D Con/Dex precedent; S1/ED-902 ratifications |
| **F-CONTEST** | `contest.md` (Recall/Bonds) **and** `social_contest_v30` (Composure/Conviction) **both declared canonical** — incompatible models | **P1 durable** | new in Turn 4; **blocks F-RECALL** | `canonical_sources.yaml` (both fresh) |
| **F-DISP** | Disposition-cap formula contradictory: `=Bonds` (PP-684) vs `floor(Bonds/2)+1` (csr, contest.md) | **P1 durable** | resolve → **`=Bonds`** (only value consistent with Knot candidacy +5) | derived_stats §10.1/§14.2 vs csr L219 / contest.md L78 |
| **F-ROSTER** | No single canonical attribute-roster doc; **macro Mind/Body/Spirit is vestigial** over a flat live system | **P2** | recalibrated (Turn 4): live system **flat** per NPC blocks + engine | Edeyja "Cognition 5, Focus 5, Endurance 4"; combatant.py; 2026-05-08 F2 |
| **F-RECALL** | Recall is the weakest attribute | **P2** | **contingent 3-path** (not a clean cut) — decide WITH F-CONTEST | contest.md (~5 roles, declared canonical); 2026-05-08 AUDIT/FOLD; DE-Encyclopedia/PoE-Lore precedent |
| **F-SPIRIT-NAME** | Spirit-the-pool vs Spirit-the-attribute naming collision | **P2** | survives (F9, 2026-05-08) | 2026-05-08 F9 |
| **F-§1** | §1 "one attribute × multiplier, no combinations" violated by ratified Stamina/Concentration | **P3** | **demoted** — multi-attribute derivation is acclaimed-normal; **retire the rule**, don't revert formulas | derived_stats §1 vs §14.1; D&D HP precedent |
| **F-LATERAL** | Combat stat-economics diverge from social/thread/fieldwork/knot | **P3 (doc)** | **softened** — acclaimed-normal; scope principle #5 | §14.4; v27 weapon-audit lateral flag; Battle Brothers/M&B precedent |
| **F-CLEANUP** | Today's edits (ED-902, combat-pool strike) not propagated to §13/§5.2; Stamina range 5–47 vs max 35 | **P3** | edit-lag; one commit clears | derived_stats §13/§5.2/§4.2 vs §14 |
| **F-PROV** | `contest.md` cites non-existent `designs/contest/` source | **P3** | provenance drift | 404 on `designs/contest/` |

## 4 · Remediation + Stage-4 re-test (each fix run back through the pipeline)
Worst-first. Re-test = "does the fix introduce a new defect?"
1. **[P1 · Jordan] Resolve F-CONTEST** — pick the live contest spec (contest.md Recall/Bonds · social_contest_v30 Composure/Conviction · the ratified 2026-06-03 groundup pisteis+Standing); strike the others from `canonical_sources.yaml`. **Re-test:** *resolves Recall's fate too (unblocks #4)*; **`[OPEN]` downstream references dangle** (e.g., derived_stats §5.2's "Recall +2D via History citation in social contest") and need propagation.
2. **[P1 · Jordan] One canonical roster doc + retire vestigial Mind/Body/Spirit.** **Re-test:** **`[OPEN — verify first]`** confirm **no live system consumes a Mind/Body/Spirit *aggregation*** before retiring (NPC blocks + combat are flat, but the 2026-05-08 audit called the macro "core resolution" — check nothing sums sub-pools).
3. **[P1] F-DISP → ratify `=Bonds`;** strike `floor(Bonds/2)+1` from `complete_systems_reference` (and contest.md if retained). **Re-test:** consistent with Knot candidacy; **clean** (the struck formula was the stale one). Minor interaction with #1 if contest.md is dropped.
4. **[P2 · Jordan, after #1] Recall — pick one:** **(a) fold into Cognition** (memory≈cognition; raises Cognition to ~4 downstream — *not* over-central; **NOT Spirit** — that worsens F-ASYM) and re-home equip-gating to Cognition/History; **(b) keep-and-feed** (give it lore/dialogue/codex/relic content to gate — DE-*Encyclopedia* path, best fit for Valoria's DE-citing design); **(c) leave** as the accepted weakest stat. **Re-test:** no path adds a mechanical defect; **fold→Cognition** is cleanest mechanically, **keep-and-feed** best by design-fit; **fold→Spirit is REJECTED** (Stage-4: worsens the asymmetry).
5. **[P2 · Jordan] Spirit:** **F9 rename = safe.** **Load-reduction = `[OPEN TRADE-OFF]`** — reducing Spirit's load **reverses ratified S1 + ED-902** (which deliberately added Spirit to Stamina/Concentration). **Re-test catch:** by the intent gate, those ratifications are **evidence Spirit-centrality is *deliberate*** → **F-ASYM's Spirit half is likely a feature, not a defect.** **Confirm with Jordan**: if Spirit-as-keystone is intended, the only Spirit fix is the **naming (F9)**, not the load.
6. **[P3] Doc cleanup** — propagate today's edits to §13/§5.2; fix Stamina range; retire §1's purist rule; scope principle #5 for combat; fix contest.md's source path. **Re-test:** pure doc-fixes, **clean**.

**Stage-4 net:** clean fixes — #3, #4(a/b), #5-rename, #6. **Pre-checks required** — #2 (confirm macro unused), #1 (propagate dangling refs). **`[OPEN TRADE-OFF]`** — #5-load (collides with ratified intent → likely *don't* fix; confirm Spirit is intended-central). No fix iterated into a new hard defect; two are gated on Jordan decisions.

## 5 · All directions (final, one line each)
- **Bottom-up:** chains hold *except* the Disposition-cap contradiction (F-DISP).
- **Top-down:** roster serves `intent_of_game` *except* Recall's thin contribution (F-RECALL).
- **Vertical:** derived-stat bridges work; **settlement layer PENDING** (acknowledged gap).
- **Lateral/horizontal:** combat-vs-sibling divergence = documented intentional exception (F-LATERAL), not a break.
- **Diagonal:** cross-scale loops (§10.4 personal→settlement→faction; wound; faction-collapse) are **bounded** where a roll sits in them.

## 6 · Prior-audit reconciliation (document_consolidation)
**Confirms + extends + updates `2026-05-08-character-mechanics-critical-audit`:** Recall AUDIT/FOLD → **recalibrated to contingent-3-path** (its "only sparking gatekeeper" premise was *incomplete* — it missed contest.md's Recall pools); **Bonds KEEP confirmed**; **F2 (structure) resolved** → flat live system + vestigial macro; **F9 (Spirit naming) confirmed + intent-qualified**. This master is the **attribute/derived-stat audit of record** going forward; the prior provisional doc is superseded for this scope.

## 7 · Consolidation status + commit offer
- This master **consolidates and supersedes** stage artifacts `00`–`03` (retained as work trail). Conflicts (Turn-2 vs Turn-4 on Recall/structure) **resolved toward the Turn-4 evidence**.
- **Proposed repo destination (NOT yet committed):** `designs/audit/2026-06-04-attributes-derived-ners/` (this master + the four stage docs), via `safe_commit`, scope `audit`/`cleanup`, `Citations:` block listing the sources read.
- **Editorial-ledger:** F-CONTEST, F-DISP (P1) and the P2s would append to `canon/editorial_ledger.jsonl` — but that is **gated and ID-collision-prone** (the open ED-NNN backlog) → **Jordan-adjudication**; I will not silently assign IDs.
- **I have not committed.** Offering, because (a) the four highest items (#1 contest-spec, #2 roster architecture, #4 Recall fate, #5 Spirit-intent) are **Jordan's canon-structure decisions**, which should precede any ledger write, and (b) ledger IDs need Jordan to avoid the collision class. Say the word and I commit the docs + stage the ledger entries for your ID assignment.

---
`[READ: derived_stats_v30 (full), params/contest.md, complete_systems_reference, combat_engine_v1/{combatant.py,ability_armature.md}, social_contest_v30(index)+groundup{README,RATIFICATION,framework,TERMINOLOGY}, mechanics_index, 00_foundations_rules, canonical_sources, supersession_register, edeyja_npc, prior audits {char-mechanics-critical, comparative-faction-vs-char, faction-stats-renaissance, all_directions_ners_v27}, resolution-diagnostic+mechanic-audit SKILLs]`
`[CONFIDENCE: high — F-DISP, F-CONTEST, F-ASYM(Recall-half), Bonds=KEEP all cited; Spirit-intent qualification cited to S1/ED-902. medium — completeness of the Recall 3-path menu; whether anything live consumes the macro layer (Stage-4 #2 open).]`
`[DRIFT: canon/definitions.yaml absent though both skills cite it — NERS criteria sourced from PI governance copy.]`
`[SELF-AUTHORED — bias risk: Turns 1–4 self-authored; adversarial pass (Turn 4) walked back the Recall and structure over-statements; this master states the corrected verdict.]`
