# Faction Play — Comprehensive Analysis (All Workings, All Dimensions)
**Audit deliverable · 2026-06-09 · session token b23ffbb924119c66 · scope: every faction system, mechanic, and dimension**

---

## 0 — Verdict (first)

**Faction play is architecturally sound and substantially remediated, but carries a propagation-debt layer of canon-internal contradictions, and its next structural step sits behind five open Jordan decisions.**

Three sentences of state:

1. **The resolution core is fixed.** The 2026-05-28 NERS verdict (NON-COMPLIANT: fragile bare-stat pools on pivotal outcomes, theatre safeguards, two undamped loops) has been answered by a ratified remediation wave — the d+σ resolver (ED-874), the deterministic low-Stability floor (FSS-LOOP-1), the Wealth→Military re-muster damper (FSS-LOOP-2), the Trigger-5 cliff removal (ED-876), the F2 contested/non-contested Ob scoping, and the FSS-1 two-stage succession. Every P1 from that verdict is closed in its primary doc.
2. **The structural redesign is half-landed.** LPS-1→2e (Jordan ruling 2026-05-30) made L/PS per-settlement and Mandate a derived size-weighted aggregate — but the migration left residual faction-level L/PS and Mandate-as-base writing in at least seven docs (the 2026-06-09 flatten's C-1/C-2 plus residuals newly found below), and the 2026-06-09 stat-architecture review proposes finishing the inversion for the whole six-stat lineup. That proposal is NERS-positive and **open on Jordan's DECIDE items**.
3. **The texture layer is rich and mostly canonical** — behavior model (PP-686 v2), political progression (PP-660 rank ladders, sub-offices, castes, parity), succession/split, emergence (GD-3), parliament/treaty/excommunication/seizure — with the known blocked set (~7 Jordan-contamination-audit items, 2 Varfell placeholders, Church Pass-2f content) unchanged since the overview.

**New findings this session: 0 × P1, 7 × P2, 8 × P3** — all are drift/propagation/documentation defects, none structural. Severity-ranked register in §6. The system's worst current liability is not a mechanic; it is that **ratified rulings (ED-787, ED-869, ED-874, ED-876, LPS-2) have not finished propagating across sibling docs**, so contradictory canon coexists.

---

## 1 — Scope, method, and read trail

Bootstrap clean (1 active handoff: `active-work-index-2026-06-09`, faction-stat-architecture stream OPEN). `task_gate('audit')` passed. Prior audit outputs checked per gate instruction (extensive — see §4 timeline).

**Read in full this session** (`[READ:]` trail; all fetched via tracked GraphQL path):

| # | File | Depth |
|---|---|---|
| 1 | `designs/factions/faction_systems_overview_v30.md` | full |
| 2 | `designs/provincial/factions_personal_v30.md` | full |
| 3 | `params/factions.md` + `params/factions/stats_1_7_scale.md` | full |
| 4 | `designs/provincial/faction_layer_v30.md` | full |
| 5 | `designs/provincial/faction_succession_split_v30.md` | full |
| 6 | `designs/provincial/faction_behavior_v30.md` | full |
| 7 | `designs/provincial/faction_state_authoring_v30.md` | full |
| 8 | `designs/provincial/faction_canon_v30.md` | full (Stage 1 = framework + Crown/Church sheets) |
| 9 | `canon/02_canon_constraints.md` | full (P-01–P-15 + GD-1/2/3) |
| 10 | `designs/territory/settlement_layer_v30.md` | full fetch; deep-read §1.3, §1.8 |
| 11 | `designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_faction.md` | full |
| 12 | `designs/audit/2026-06-09-faction-stat-architecture-review/faction_stat_architecture_review.md` | full |
| 13 | `designs/audit/2026-06-09-faction-stat-architecture-review/faction_attribute_ners_value_audit.md` | full |
| 14 | `designs/audit/2026-06-09-faction-settlement-attribute-flattening/attribute_flattening.md` | full |
| 15 | `designs/provincial/faction_politics_v30.md` | full fetch; deep-read index, PART 0, PART 8–§9.3 |
| 16 | `skills/valoria-mechanic-audit/SKILL.md` + faction entries of `canonical_sources.yaml` | full |

**Not deep-read** (transparency): `faction_politics` Parts 1–7/10–11 prose (ladder tables — index + parity + findings read), `resolution_diagnostic_faction.md` (Stage-1 companion; its verdict doc read), `lps_mandate_comprehensive_ners_audit.md` (its conclusions are canonized in settlement_layer §1.8, which I read directly), `faction_stat_io_flattening.md` (its 78-write-site worklist is summarized in flatten C-2), the 2026-06-09 session-consolidation master (its faction blockers are quoted verbatim in the active handoff), `ci_political` / `military_layer` / `victory` / `peninsular_strain` / `insurgency_pipeline` (consumed via the flatten's per-line excerpts and direct cross-quotes in the docs above). Claims below about those files cite the excerpting source.

---

## 2 — The architecture: what faction play is

### 2.1 Six layers (`faction_systems_overview_v30 §1`)

L1 primitives/services → **L2 Faction Identity** (stats, status flags, Standing matrix, Conviction Scars, AI priority stack) → **L3 Faction Action** (per-season universal + faction-unique actions) → **L4 Inter-Faction Resolution** (vote, transfer, treaty, tribunal, seizure, conquest, CB matrix) → **L5 Faction-Emergent** (GD-3 revolt→insurgency→faction pipeline) → **L6 Peninsular Accounting** (end-of-season cascade). GD enforcement crosses layers: GD-1 at L6 (sole victory), GD-2 at L3 (mandatory threat response), GD-3 at L4/L5 (status semantics + emergence). ~50 faction-touched mechanics; ~80% of all Pass-2 forward flags sit on this surface.

### 2.2 Identity: the stat substrate (post-LPS canonical state)

- **Six faction stats** (`stats_1_7_scale` header; `faction_canon §5.1`): **Mandate (headline, derived) / Influence / Wealth / Military / Intel / Stability**, 1–7 (Stability/Mandate 0–7).
- **L and PS are per-settlement (0–7), not faction stats** — Jordan structural ruling 2026-05-30, canonical home `settlement_layer §1.8`. Faction **Mandate = clamp(round(7·T/(T+K)), 0, 7)** with `T = Σ_s W_s·(0.5·L_s + 0.5·PS_s)/7`, `K = 6`, `W_s = base(Type) + Prosperity + FacilityTier` — size-weighted, saturating, with a mean-reverting Mandate→settlement feedback (±1/settlement/season). Examined this session: the size-scaling is **deliberate and intent-stated in-doc** ("one province of large, developed settlements outranks many tiny ones"), Lesson-5-bounded by the saturation, Stage-4 sim-validated (bounded, convergent over 30 seasons). `[NULL: §1.8 Mandate formula — examined, intent-gated pass]`
- **Intel restored** as the sixth stat per ED-787 (Position A, Jordan 2026-05-03): Crown 3 / Church 4 / Hafenmark 3 / Varfell 4 (revised from 5 per Jordan) / Guilds 4 / Löwenritter 3, with defensive Spy Ob `floor(target Intel/2)+1`, counter-espionage at Intel ≥ 4, strategic fog.
- **Crown Military 5/6** per ED-869 (Jordan 2026-05-31; prior 4 struck) — expressed through Löwenritter Power 5 / Discipline 6 units pre-coup (`faction_layer §1.5` doctrine).
- **Partial sheets** (`faction_canon §11`): Restoration (no Mandate/Military/Wealth; Presence markers + Community Weaving per PP-460/PP-616), Löwenritter (no Mandate/Wealth pre-coup; embedded under Crown until Graduated Autonomy 4), Ministry (Influence + Stability only; institutional actor, Throughline T4).
- **Behavior model** (PP-686 v2, `faction_behavior`): four components — **Mission** (authored telos with aligned/contradicted PP-687 DA categories; four shift triggers), **Cascade** (α-weighted Conviction blending down supervisor graphs; multi-root allowed; crisis-bypass at leader Scars ≥ 3), **Public Expectation** (role templates over the 13-Conviction taxonomy; cascade-fidelity cosine), **L+PS** (now per-settlement dynamics with 5-temperament populace weighting; strictness `clamp(0.4 + 0.5·L/7 − 0.3·PS/7)` as deviation-cost modulator only). Triadic Ob modifier clamped ±2 (C1). Legacy Ethical Framework Modifiers struck (SUPERSESSION-PP686-001/002).
- **Per-faction authoring** (`faction_state_authoring`): Missions, cascade roots (single-root default), institutional_culture for the 6 player factions; seeds L/PS per settlement (Crown/Church 5/5, Hafenmark/Varfell 4/4, Guilds 3/3, Restoration & Löwenritter 0/0 — but see finding P3-12). Role map: sovereign=Crown, ecclesiastical=Church, mercantile-procedural=Hafenmark, military-order=Varfell **and** Löwenritter, reformist=RM; intelligence-diplomatic template currently unassigned (available for emergents).
- **Status flags** (parliamentary / extra-parliamentary / non-parliamentary), **Standing matrix** (pairwise, gates treaties/votes/CBs), **Conviction Scars** (grievance ledger), **NPC AI priority stacks** — last two AUDIT-PENDING per the Jordan contamination audit (overview §2.4–2.6).

### 2.3 Resolution: the d+σ resolver (ED-874, ratified 2026-05-31)

**Canonical for all bare-stat faction checks** (`stats_1_7_scale §Domain Action Resolution`): `M = acting_stat − difficulty`; contested difficulty = target's relevant stat directly, non-contested = fixed rating (legacy Ob maps `D = max(1,(O−1)·2)`); `P_success = clamp(0.50 + 0.10·M, 0.05, 0.90)`, with Overwhelming/Partial band offsets. Constant +10%/point leverage closes the σ-leverage non-uniformity no dice pool can (1/√N); FLOOR 0.05 kills the ~1% punching-up wall; CAP 0.90 keeps overmatch uncertain. Output unchanged (four-degree ladder), so Domain Echo and cost tables are untouched. Governed: all Domain Actions, Suppress (Failure→Stab −1 retained), Rebuttal (OW bonus retained), treaty positioning/ratification (+ Grand Debate degree → margin), §1.4 Accounting Stability Check, the four migrated unique actions (Royal Decree, Excommunication, Private Collection, Economic Leverage). **Scope boundary:** healthy dice systems (personal combat, social contest 5–18D, mass battle) stay dice. Historical anchor: COIN/political-contest literature — structure-decisive with a stochastic tail. The F2 "conflicting Ob formulas" defect is closed by scoping (contested = stat-direct; non-contested = ⌊/2⌋+1-mapped rating), reconciliation notes in both `factions_personal §8.1` and the resolver block.

### 2.4 Action layer (L3)

Universal: `govern`, `muster`, `military_conquest`, `parliamentary_transfer` (4 modes × 8 CB sources). Faction-unique (status per overview §3 + current params): Crown ×4 (Royal Decree migrated; Great Work; Coronation Renewal; Crown Treaty), Church ×6 (Excommunication migrated; Absolution; Council; **CI-60 Seizure — authoritative form `Influence + floor(CI/15) vs Ob = 7 − PT`, Failure → Mandate −1, per `faction_layer §2.7`, FCN-SEIZURE-DRIFT closed by LPS-2c**; 2 audit-blocked placeholders), Hafenmark ×3 (Charter; Altonian Reinforcements; equipment placeholder — **Sovereign Authority Doctrine not yet resolver-migrated, pending decision**), Varfell ×2 (mandate-action BLOCKED on redesign per Jordan's double-cost-asymmetry diagnosis; territorial acquisition mechanism ready, identity pending — plus the non-unique Cultural Reclamation, Piety-shift only, VTM-free, no victory path per ED-880/GD-1), Guilds (Economic Leverage migrated), RM (Community Weaving = PP-616 Thread operation, not a DA), Löwenritter (Martial Law trigger at Graduated Autonomy 4, no roll). CI economy: passive +1/season, Assert +2, Suppress negate (Failure → Stab −1), Baralta structural suppression −1/season while her Mandate ≥ 4, caps ±3 DA / ±5 total (`faction_layer §9`).

### 2.5 Inter-faction layer (L4)

**Parliament** (`faction_layer §5`): votes = current Mandate; Church weight `Mandate + ⌊CI/20⌋`, anti-Church contribution `max(0, Mandate − ⌊CI/30⌋)` floored at 0 (ED-865/874 consistency, per `ci_political §3.3–3.4` cross-quote); ten motion types with proposer minima, thresholds, rescission; Sacred Veto on a once-per-4-seasons cadence (ED-751); Rebuttal migrated to resolver; Turmoil coupling (target Stab ≤ 2 → Accord −1 across holdings). **Treaties** (§3): six types; three-phase negotiation — positioning (resolver, contested Influence vs Influence), concession declaration (no roll), ratification (resolver, M = Mandate − 2; Grand Debate Zoom-In stays dice, degree → ±M); Trigger-2 Stability deltas; breach → Mandate −2/Stab −1/CB; Survival-exception waiver at Stab 1. **Excommunication chain** (action → tribunal → absolution). **Seizure** (§2.7 authoritative, above). **Conquest** via mass battle (orthogonal, dice — ED-876 boundary). **CB matrix**: 8 sources; consumes on use, auto-expires after 3 seasons unused (ED-NEW-001 resolution).

### 2.6 Stability lifecycle

Five canonical triggers (occupation/loss with capital escalators; treaty terms; antagonistic votes; subterfuge; **Trigger 5** three-condition gate — ED-876 moved "pool ≥ 6" from gate to cost-escalator, restoring monotonic battle→Stability exposure). Recovery: six paths, ±2 seasonal cap; Institutional Consolidation (+1 clean season) is the universal damper. **§1.4 Accounting Check** runs on the resolver with the **FSS-LOOP-1 deterministic floor**: at Stab ≤ 2 the check cannot reduce Stability — collapse is reachable only via active Trigger pressure, never passive dice decay (historically anchored: Byzantine 1204 / Habsburg bankruptcies; Stage-4 sim P(collapse) 0.41→0.97 under rising active pressure, recovery via §1.3 when pressure relents). **Collapse** (ED-675, §1.5): six-step exit — Mandate→0, territories Uncontrolled (Accord 0), officers Independent, PC de-affiliated, seat lost, victory closed; Reconstitution (Influence vs Ob 4 ×3 seasons, ≥1 territory) at Stab 1 / Mandate 1 / 50% frozen values; one-time Survival Exception at Stab 1. **Wealth-zero** (§5.7): no muster, Military −1/Accounting — now bounded by **FSS-LOOP-2** re-muster (+1/Accounting at Wealth ≥ 1 up to pre-collapse value; Spanish-Habsburg fiscal-military anchor; sim: 5→2→5). **Succession/split** (`faction_succession_split`, FSS-1 2026-05-30): two-stage — Stage 1 *who leads* via resolver on strength gap, Stage 2 *whether it splits* deterministic on gap G (G≥3 unified / G=2 fractious Disposition-gated / G≤1 split 60/40 with dice tails) — fragmentation tracks claimant power balance (Carolingian/Diadochi anchor), not roll variance; asset-division table; splinters persist per §2.5; Regency fallback; 3 failed contests → collapse.

### 2.7 Emergence (L5) and accounting (L6)

GD-3 pipeline (canon/02 §B): 2+ contiguous Uncontrolled territories sustained 2 seasons → Insurgency (territorial, non-parliamentary) → promotion at thresholds to parliamentary or extra-parliamentary faction (PT-gated RM-variant); insurgencies invade like factions, including the parent; **promoted factions win via GD-1 like anyone**. RM additionally has the staged Cell→Hegemon ladder (`settlement_layer §6.2`) plus per-settlement Emergence (Order = 0 ∧ PT ≤ 1 ∧ Vossen Disposition ≥ +3; once per province per 4 seasons). Accounting: 10-step cascade (`faction_layer §7`, ED-678/PP-472 — collapsed from 13), with parliamentary/treaty resolution at Step 1, stability/collapse at Step 2, clocks at Step 4, Turmoil at Step 6, occupation duration + Institutional Consolidation at Step 9, victory at Step 10.

### 2.8 Political progression dimension

`faction_politics_v30` (CANONICAL, PP-660, Jordan-approved 2026-04-17): 8-rank Standing ladders (0–7) for Crown/Hafenmark/Varfell/Church with Skyrim-pattern institutional gates; seven sub-office ladders (Löwenritter, Riskbreakers with Shadow Renown 0–10 + Deniability Debt 0–7, Inquisitors, Templars, Guilds, Niflhel-arms, Warden); caste integration layer; CI × rank integration; Baralta-claim × ladder cascades; Ministry expansion to all factions (committees/dicasteries/councils with Readiness tracks); generational-shift fix (A-10 — four trigger paths replacing the unreachable 10-year clock); **cross-faction parity table enforced at every Standing** (§9.2–9.3: equivalent scene-action bonus / delegation / political access / hall tier; deviations must be justified). Its eleven structural findings (A-01–A-11) are all addressed in-doc; ED-634–658 tracked in the ledger.

### 2.9 Cross-scale and constraints

Upward ripple: Domain Echo (`scale_transitions §5`, ±2 cap) currently writes faction stats directly — the 2026-06-09 review reconceives it as substrate ripple (settlement-locus write or national-event Key → re-derive). Downward: Mandate→settlement feedback (§1.8); ΔL/ΔPS mission outcomes apply per controlled settlement. Constraint surface: P-14 binds faction-card co-movement; GD-1 single victory verified consistent across every doc read (victory namespaces reframed as approach-tracks per FSA-1); GD-2 mandatory-actions pass precedes stochastic selection. `[NULL: GD-1 wiring across read set — examined, no alternate-victory residue found in the faction docs read]`

---

## 3 — Design arc: how the system got here

| Date | Event | Authority |
|---|---|---|
| 2026-04-17 | `faction_politics_v30` canonical — rank ladders, sub-offices, castes, parity | PP-660, Jordan-approved |
| 2026-05-01 | PP-686 v2 behavior architecture (Mission/Cascade/Expectation/L+PS) promoted after Stage-10 sim 12/14 | PP-686 |
| 2026-05-03 | Intel restored as sixth stat, Position A | ED-787, Jordan |
| 2026-05-17 | `faction_systems_overview_v30` written as single source of truth (now stale — P3-11) | — |
| 2026-05-28 | Resolution diagnostic → **NERS verdict: NON-COMPLIANT** (F1–F12; R: FAIL — F1, F3, F6, F7 bite at extremes) | audit |
| 2026-05-30 | **LPS-1→2e**: L/PS become per-settlement; Mandate derived, size-weighted saturating aggregate. **FSS-1** two-stage succession ratified. | Jordan ruling |
| 2026-05-31 | Remediation wave ratified: **ED-874** d+σ resolver; **ED-869** Crown Military 5/6; **ED-876** Trigger-5 gate→cost; **FSS-LOOP-1** Stability floor; **FSS-LOOP-2** re-muster | Jordan |
| 2026-06-09 | Stat-architecture review + per-attribute NERS value audit + attribute flattening → **full-inversion proposal** (faction stat = aggregate(holdings) ⊕ decaying national-event Key ledger; retire `derived_stats §14` capitals; Domain Echo → substrate ripple). NERS-positive. **OPEN on Jordan DECIDE items.** | review stream |
| 2026-06-09 | This comprehensive analysis (session `b23ffbb924119c66`) | — |

## 4 — Where the 2026-06-09 inversion stream stands

The flatten established the two structural contradictions the inversion resolves: **C-1 — Mandate derivation is inverted between docs** (`derived_stats §14` derives Legitimacy *from* Mandate; `settlement_layer §1.8` derives Mandate *from* settlement L/PS — arrows point opposite ways), and **C-2 — Mandate is declared derived but is written and rolled as a base stat** (78 write sites). The review's answer: one direction only (substrate → faction); nothing writes a faction stat — the 78 sites become settlement-locus writes or national-event Keys that the aggregate re-derives through. The per-attribute NERS value audit is positive on every stat under the inversion. **Nothing is committed**: adoption, the Influence/Intel national-derivation basis (DECIDE-1), national-event modifier semantics — decay/stack/cap (DECIDE-2), Intel expand-vs-fold, CI/Influence naming, and per-stat aggregation functions are all Jordan's (§7). An explicitly offered alternative sequencing — *simulate Wealth/Mandate aggregation first, decide after* — is also open.

**Ordering dependency for remediation (matters for §8–§9):** if the inversion is adopted, the `derived_stats §14` and Domain-Echo rewrites land inside that work; the propagation fixes below that touch §14 should then be folded in, not done twice. The drift fixes in sibling faction docs (P2-1…P2-5, P3-*) are needed either way.

## 5 — Prior verdict disposition map (F1–F12, 2026-05-28 → today)

| F | Verdict finding (severity → routing) | Current disposition |
|---|---|---|
| F1 | Bare-stat pool on pivotal DA (P1 → L3 master) | **CLOSED** — ED-874 resolver replaces every bare-stat pool; constant +10 %/point leverage |
| F2 | Canon defect: conflicting Ob formulas (P1 → ledger) | **CLOSED by scoping** — contested = target stat direct; non-contested = ⌊/2⌋+1-mapped rating; reconciliation notes in `factions_personal §8.1` + resolver block |
| F3 | Anti-death-spiral floor non-functional (P1 → L3+L4) | **CLOSED** — FSS-LOOP-1 deterministic floor + resolver FLOOR 0.05 |
| F4 | Absolute stat damage non-uniform (P2 → L2; Lesson-2 at P=0) | **RESOLVED-BY-RESOLVER** — linear P-space makes a −1 cost uniform at every stat level |
| F5 | Decrease > Increase stat asymmetry (P1 → L5) | **DISPOSITIONED, no new mechanic** — asymmetry ruled intentional and bounded; recovery paths + Institutional Consolidation carry the load |
| F6 | L1 collapse loop unbounded (P1 → L5; trigger ≥1/season net-negative) | **CLOSED** — FSS-LOOP-1: at Stab ≤ 2 only active Triggers can cut Stability |
| F7 | Wealth-Zero Military cascade undamped (P1 → L5) | **CLOSED** — FSS-LOOP-2 re-muster (+1/Accounting at Wealth ≥ 1, capped at pre-collapse value) |
| F8 | Canon defect: PP-686 v2 / ED-787 drift (P1 → ledger) | **PARTIALLY OPEN** — authoritative values landed in `stats_1_7_scale`, but `factions_personal §8.1` and retained PP-236/PP-241 prose still contradict them → **carried forward as P2-2** |
| F9 | Best-of-3 Parliamentary clock shallow (P2 → L4 deepen) | **CONDITIONAL** — never appears in the ED-874 migration list; the bare-pool form persists in `factions_personal §8.11` → **carried forward as P2-6** |
| F10 | Stability triple-role | **NOTED** — downgraded in-verdict: "not a true conflation," no Lesson-1 violation |
| F11 | CI political amplification (Lesson 5) | **PASS** — damped + bounded by intent (Baralta structural suppression, ±caps) |
| F12 | GD-3 RM emergence (Lesson 5) | **PASS** — deliberate, adequate safeguard (PT gate, cadence limit) |

Net: every P1 from 2026-05-28 is closed **in its primary document**; the two canon-defect P1s (F2, F8) closed at the authoritative source but F8's drift and F9's migration gap survive as this session's P2-2 and P2-6.

---

## 6 — New findings register (this session: 0 × P1, 7 × P2, 8 × P3)

All are drift / propagation / documentation defects. None is structural; none changes the §0 verdict. **Fix class** column: *EG* = evidence-grounded correction (canon already rules; the contradiction licenses the edit), *JR* = requires a Jordan ruling first.

### P2 — contradictory canon coexists

| # | Where | Finding | Fix class |
|---|---|---|---|
| **P2-1** | `faction_layer §6.2` vs `§1.2` | Same-document contradiction: §6.2 still carries the **"OR pool ≥ 6"** Trigger-5 gate clause that ED-876 struck from §1.2 (gate → cost-escalator). A reader entering at §6.2 reconstructs the pre-ED-876 cliff. | EG — delete the residual clause, cite ED-876 |
| **P2-2** | `stats_1_7_scale` (internal) + `factions_personal §8.1` | ED-787/F8 drift persists: the Starting-Stats table sets **Crown Intel 3**, yet the retained PP-236 prose in the same file states **"Crown has NO Intel stat"** (PP-241 supplies the delegation rationale). `factions_personal §8.1` still prints Intel "—" for the five majors and Crown Military 4. | EG — strike PP-236/241 retained prose as superseded (ED-787); refresh §8.1 table (ED-787 + ED-869) |
| **P2-3** | `factions_personal §8.2` / `faction_canon` Crown sheet / `stats_1_7_scale` Royal Decree row | **Royal Decree failure cost — three-way split:** "Mandate −1" vs "Legitimacy −1" (faction-level L no longer exists) vs "Failure \| —" (no penalty). The most recently migrated source is the silent one, so the drop may be deliberate or accidental. | **JR** — rule the cost (Mandate −1 / settlement-L write / none), then propagate |
| **P2-4** | `stats_1_7_scale` vs `faction_layer §1.5` vs `faction_canon` Crown sheet + prose | **Crown Military drift:** 5/6 (ED-869 authoritative) vs "Military stat 5" vs "Military 4 (TTRPG/BG)" in two places. Slash-notation semantics (5/6 = stat/discipline?) are nowhere defined. | EG for the two stale 4s and the §1.5 partial; JR-lite: one sentence defining the slash notation |
| **P2-5** | `faction_canon` (Royal Decree "Legitimacy −1"); `stats_1_7_scale` ("Baralta's L −1", "L ≥ 4" vs `faction_layer §9` "NPC Mandate ≥ 4"); `params/bg/faction_actions.md` L17/L243 ("Roll: L vs Ob = ⌊controlling faction L / 2⌋ + 1 + Fort Level"); `derived_stats §14` (Mandate-as-base + "Legitimacy −25" writes; also `peninsular_strain` §/L319) | **LPS residuals that contradict the lps2d "verified end-to-end" claim.** Faction-level L is still rolled, gated, and written in at least four files outside the 11-doc set that claim covered. `faction_actions` L-rolls were missed by LPS-2d entirely. | EG — map each site to its LPS-2e equivalent (aggregate-L read, settlement write, or Mandate); §14 sites should fold into the inversion work if adopted (§4 ordering note) |
| **P2-6** | `factions_personal §8.11`; `ci_political` ~L250 + `peninsular_strain` ~L321 (flatten excerpts) | **Parliamentary Vote (best-of-3, bare faction pools) is absent from the ED-874 migration list** — the only pivotal bare-stat contest not migrated or declared exempt. The strain-band "Mandate check pool vs Ob 1/2" carries the same gap. This is F9 still breathing. | JR-lite — either migrate to the resolver (mechanical translation is unambiguous) or declare dice-scope exemption; decision is Jordan's, execution is EG |
| **P2-7** | `canon/02_canon_constraints.md §B` (GD-3) | GD-3 still speaks pre-LPS faction-level **L** ("starts at L = 1.0", "promotes L ≥ 3"). Insurgencies hold territory, so a settlement-L reading exists, but GDs are constitution-tier: **edits require Jordan ratification**, and the mapping (aggregate-L? seed value?) is a design choice. | **JR** — rule the post-LPS mapping, then a one-line GD edit |

### P3 — hygiene, staleness, presentation

| # | Where | Finding | Fix class |
|---|---|---|---|
| P3-8 | `faction_behavior`, `faction_canon`, `faction_state_authoring`, `faction_succession_split` | Status-declaration incoherence: CANONICAL banner comments over PROVISIONAL body labels (and `canonical_sources.yaml` entries disagreeing with both) — an automated header pass half-applied. | EG — one status line per doc, synced to the registry |
| P3-9 | `faction_layer` | **Duplicate §1.5**: Doctrine Notes interleaved mid-Trigger-sequence and again at Collapse Exit; numbering collides. | EG — renumber, single location |
| P3-10 | `settlement_layer_v30_index` (no §1.8), `faction_politics` index (anchors at 1033 lines vs 1115 actual), `faction_layer` index (stale SHA) | Stale indices — the `read_sections` path silently misroutes on these. | EG — regenerate via `doc_index_gen.py` |
| P3-11 | `faction_systems_overview_v30` (2026-05-17) | The declared single source of truth is stale: pre-LPS stat block in §2.1, 13-step cascade (10 since ED-678), seizure drift listed "pending" (closed by LPS-2c). Its authority claim now actively misleads. | EG — refresh against post-05-31 state |
| P3-12 | `faction_state_authoring §8` vs `stats_1_7_scale` BG columns | Löwenritter seed conflict: L/PS {0, 0} vs L (BG) 3 / PS (BG) 3. | EG after a 10-second Jordan confirm of which seed is meant |
| P3-13 | `faction_succession_split` worked example | Uses Varfell "Intelligence 5" (ED-787 set 4) and retains pre-resolver dice text. | EG |
| P3-14 | Hafenmark Sovereign Authority Doctrine | Resolver migration explicitly pending — known-open, restated for completeness. | JR (already queued) |
| P3-15 | UI supplement | "Legitimacy: 87/100" — a ×20-scaled meter not bound to any 0–100 quantity post-LPS (aggregate-L is 0–7). | EG — re-spec the meter against aggregate-L or Mandate |

`[NULL: §1.8 Mandate formula; FSS-LOOP-1/2; resolver scope boundary; FSS-1 succession determinism; faction_politics parity table; GD-1 single-victory wiring — each examined this session, nothing found]`

---

## 7 — Open decisions (all Jordan's; nothing here is mine to take)

1. **Adopt or reject the faction-stat inversion** as substrate primitive (the 2026-06-09 review recommends adopt; NERS-positive on every stat).
2. **DECIDE-1** — Influence/Intel national derivation basis (what national substrate, if any, feeds the two non-holdings stats).
3. **DECIDE-2** — national-event modifier semantics: decay curve, stacking rule, cap.
4. **Intel: expand vs fold** — mechanize the T-8 information-asymmetry layer, or fold Intel into Influence.
5. **CI vs Influence-stat naming overload** (two "influence" quantities in adjacent systems).
6. **Per-stat aggregation functions** — Wealth/Military/Stability weights + saturation constants.
7. **Hafenmark Sovereign Authority Doctrine → resolver** (P3-14).
8. **Substrate postures** for Crown/Church/Varfell/Guilds (ED-717 Phase B creative layer).
9. **Alternative sequencing** — simulate Wealth/Mandate aggregation first, decide inversion after.
10. **Royal Decree failure cost** (P2-3) — Mandate −1, settlement-L write, or no cost.
11. **GD-3 L mapping post-LPS** (P2-7) — constitution-tier edit, ratification required.

(The handoff additionally carries combat `martial_traditions` D-alpha–delta and mass-battle items — out of faction scope, noted so the decision queue reads complete.)

---

## 8 — Staged editorial-ledger candidates (staged here, **not committed**)

Per the 2026-05-28 staging precedent and the ID-collision backlog, these are formatted for `canon/editorial_ledger.jsonl` (JSONL — the skill text's `.yaml` reference is stale) with **placeholder IDs**; allocate `next_id` at commit time after Jordan review. EG items are commit-ready on a nod; JR items need the §7 ruling first.

```jsonl
{"id":"ED-NEXT-1","date":"2026-06-09","scope":"faction_layer §6.2","change":"Strike residual 'OR pool ≥ 6' Trigger-5 gate clause; §1.2 post-ED-876 text governs","source":"ED-876","status":"staged-EG","finding":"P2-1"}
{"id":"ED-NEXT-2","date":"2026-06-09","scope":"stats_1_7_scale PP-236/PP-241 retained prose; factions_personal §8.1","change":"Mark 'Crown has NO Intel stat' prose SUPERSEDED-BY ED-787; refresh §8.1 table to ED-787 Intel row + ED-869 Crown Military","source":"ED-787; ED-869","status":"staged-EG","finding":"P2-2"}
{"id":"ED-NEXT-3","date":"2026-06-09","scope":"factions_personal §8.2; faction_canon Crown sheet; stats_1_7_scale Royal Decree row","change":"Unify Royal Decree failure cost to <Jordan ruling>","source":"§7 item 10","status":"staged-JR","finding":"P2-3"}
{"id":"ED-NEXT-4","date":"2026-06-09","scope":"faction_layer §1.5; faction_canon Crown sheet + prose","change":"Crown Military → 5/6 per ED-869; add one-line slash-notation definition","source":"ED-869","status":"staged-EG","finding":"P2-4"}
{"id":"ED-NEXT-5","date":"2026-06-09","scope":"faction_canon; stats_1_7_scale; params/bg/faction_actions.md L17/L243; derived_stats §14; peninsular_strain ~L319","change":"Map each residual faction-level L read/write/roll to its LPS-2e equivalent (aggregate-L read, settlement-L write, or Mandate); §14 sites contingent on inversion decision","source":"LPS-2e (settlement_layer §1.8)","status":"staged-EG (part contingent)","finding":"P2-5"}
{"id":"ED-NEXT-6","date":"2026-06-09","scope":"factions_personal §8.11; ci_political ~L250; peninsular_strain ~L321","change":"Parliamentary Vote + strain-band Mandate check → resolver, or declare dice-scope exemption per <Jordan>","source":"ED-874 scope rule","status":"staged-JR-lite","finding":"P2-6"}
{"id":"ED-NEXT-7","date":"2026-06-09","scope":"canon/02_canon_constraints.md §B (GD-3)","change":"Replace faction-level L thresholds with <ruled post-LPS mapping>","source":"§7 item 11; GD edits require ratification","status":"staged-JR","finding":"P2-7"}
{"id":"ED-NEXT-8","date":"2026-06-09","scope":"P3-8/9/10/11/12/13/15 sites","change":"Hygiene sweep: status lines synced; faction_layer §1.5 renumbered; three indices regenerated; overview refreshed; Löwenritter seed unified per confirm; succession example values ED-787-corrected + dice text struck; UI Legitimacy meter re-specced","source":"per-finding citations §6","status":"staged-EG","finding":"P3-8…P3-15 (excl. P3-14)"}
```

---

## 9 — Recommendations (ordered)

1. **One propagation-sweep commit** for the EG set (ED-NEXT-1, -2, -4, -5 non-§14 sites, -8) — small, mechanical, every edit licensed by an existing ruling. This clears most of the P2 layer in one review.
2. **Two rulings from §7** (items 10, 11) unblock ED-NEXT-3 and -7; one confirm unblocks the Löwenritter seed.
3. **Decide P2-6** (migrate vs exempt) — ten minutes; closes the last live thread of the 2026-05-28 verdict.
4. **Then the inversion decision** (§7 items 1–6, 9). Taking it before touching `derived_stats §14` avoids doing that file twice (§4 ordering note). If deferred, the sim-first alternative (item 9) still de-risks it.
5. **Index regeneration + overview refresh** ride the sweep commit (P3-10/11) so the single-source-of-truth claim becomes true again.
6. Hafenmark Sovereign Authority (P3-14) and the audit-blocked set (Conviction Scars, AI stacks, 2 Church placeholders, Varfell mandate-action) stay queued behind their existing blockers — nothing new found that changes their order.

---

## 10 — Read depth and confidence

`[CONFIDENCE: high]` on every finding whose contradiction sits inside documents read in full this session (P2-1, P2-2, P2-3, P2-4, the faction_canon/stats sites of P2-5, P2-7, P3-8…P3-13, P3-15) — both sides of each contradiction were read directly.
`[CONFIDENCE: medium — excerpt-sourced]` on the P2-5/P2-6 sites located in `faction_actions.md`, `ci_political`, `peninsular_strain`, `derived_stats §14`: cited via the 2026-06-09 flatten's per-line excerpt tables, not full reads of those files. Line anchors (~L17/L243/L250/L319/L321) are the flatten's; verify at edit time.
`[GAP: faction_politics Parts 1–7/10–11 prose; lps_mandate_comprehensive_ners_audit.md; faction_stat_io_flattening.md 78-site worklist — not deep-read; conclusions consumed via their canonized or excerpted forms]` — none of these gaps touches a register entry's evidence.
No commits were made this session; the repository is untouched. Session `audit | ef659454b0c8` remains open.
