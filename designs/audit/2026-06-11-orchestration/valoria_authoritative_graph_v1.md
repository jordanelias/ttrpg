# Valoria — Authoritative Graph v1 (nodes · edges · loops · coverage, all directions)
**2026-06-11 · status: PROPOSED (Jordan-vetoable) · companion to the map (navigation) and workplan v4 (register/docket). Rendered views: `valoria_authoritative_graph.mermaid` (topology) + `valoria_decision_unblock_graph.mermaid` (docket DAG).**

**Source tier (load-bearing, atlas R1):** the edge set below is **primary-canon-grounded** — `key_substrate §4.1/§4.2/§8` · `key_type_registry` (37 types) · `scale_transitions §3–§10` · `derived_stats §14` + `settlement §1.8` (the last two live-verified exact this corpus). Contract-/`module_map`-derived rows are secondary leads. Type-granular emitter→consumer detail: **atlas §3** and generated `module_map_flat.md §4.5` — pointed to, not re-transcribed. Loop-safety status is **inherited** from the source audits (sims cited, not re-run — atlas R2).

---

## §1 — NODES

**27 contracted modules** (status table = map §5; honest split ≈ 14 specified + 11 registry-shadow + 2 stubs), under the **name-reconciliation rule** (atlas §0): registry/substrate speak canon names (`da_framework`, `faction_layer`, `conviction_track`), contracts speak impl names (`domain_actions`, `faction_state`, `piety_track`) — same nodes, two vocabularies; the divergence is itself register row 6 (J-2/J-30). **Plus:** the Key log (the single hub — no system has a private channel), the world clocks (RS/MS · CI · IP · PI · Strain + per-territory set), and actor classes (PC · named leaders · ~35/30/∞ NPC roster) whose armatures are the observer fan-out.

## §2 — EDGES BY CANONICAL DIRECTION (`canon/definitions.yaml` six)

**Universal mechanism:** every edge is a Key through `§4.1` — validate (registry #2 = the F2 wall; `causes[]` DAG #4) → append → `compute_observers` (`§4.2`, **scale-agnostic**: any observer whose state intersects `scale_signature`) → interpret → memory → **apply_state_changes** → typed consume → causal edge. Edge legality = type-registered ∧ scale-intersecting observer.

### Lateral / horizontal — ✅ complete
Scene-internal: `scene_slate`/`social_contest`/`fieldwork`/`npc_behavior` interchange `scene.*` (dialogue/insult/threat/gift/witness/interaction/gossip) consumed by npc_behavior · conviction_track · faction_layer · articulation. Provincial-internal: `da_framework → faction_layer` (`da.*` ×5) · `faction_politics → faction_layer` (`state.coup_attempted`/`succession`/`standing_change`) · `faction_layer` self (`mechanical.cascade_resolution`/`mission_shift`). Fieldwork lateral matrix `§3.9` (post-combat site +1/+2/+3 Exposure; contest Appraise → +1 Testimonial Evidence).

### Bottom-up — ✅ covered & safeguarded
Gate first: **Sufficient Scope (`§7`)** — a scene Echoes only on ≥1 of: faction leader present · institutional challenge · Complex/Structural investigation · Relational+ Thread op · officer-combat victory · Disposition +4/5 with officer · governance moving Order ±1; multi-condition tie-break `§3.4`.

| Channel | Effect | Cap / timing |
|---|---|---|
| Domain Echo `§5.1–5.3` | OW ±2 / Succ ±1 / Fail −1-own → most-relevant faction stat | **±2/stat · 1/scene/faction (PP-329) · queued to Accounting (PP-109)** |
| Debate Echo `§5.4` | PT ≥7 → winner +1 Mandate (≤3 reversed) | queued; **canon text writes ±Mandate directly — R4 violation, route ΔL/ΔPS (register #2, J-7/J-8)** |
| Accord Echo `§5.5` | governance OW/Succ → settlement Accord ±1; transfer set-2; violence −1 + MS −1 | ±1/territory/Zoom-In · queued 4c-block (Step 6) · no-stack with Govern |
| Thread Echo `§5.6` (ED-673) | Dissolution/Gap → Stability −1 · Mending(Terr+) → Mandate +1 · unauth Lock → Mandate −1 | 1/scene/faction · queued |
| Accounting recompute | L/PS/W → **Mandate `clamp(round(7T/(T+6)),0,7)`** · Order → **Accord `⌊mean⌋`** | saturating + clamped + mean-reverting drift ±1 (L3 closed); **A5 bars the inverse write** |

### Vertical — ◐ half-covered
The Eight Handoffs (`§3`): 3.1 Personal→Thread ↑ · 3.2 Personal→Faction (same-roll dual-Ob) ↑ · 3.3 Personal→Scene ↔ · 3.4 Scene→Faction ↑ · 3.5 Thread→Faction (Thread-op-as-DA) ↑ · 3.6 Thread→Mass (substrate cost by scale) ↔ · **3.7 Mass→Personal ↓ — the lone down-handoff, a narrow general-duel (PP-111/232)** · 3.8 Scene→Mass ↔; plus §3.9 fieldwork bidirectional (carries the BG-Survey→TTRPG-Discovery **down-modifier**) · §9 PC-embedding +1D ↑ (ED-075) · §10 Thread→CI ↑ (PP-125/260). **None is top-down Key-delivery.**

### Top-down — ⛔ OPEN (J-1; register #1)
**Channels that exist:** C1 §3.7 duel · C2 mandatory zooms (Revolt/Heresy/Leader-Removal/Mass-Battle/Companion/Knot-Crisis/Stability-Crisis/Rank) · C3 world-state zooms (band transitions, treaties, control changes, Warden RS≤40) · C4 retrospective (cannot change outcomes) · C5 board-degree → scene Ob (±1/±2) · C6 Slate read-down (presentation) · **C7 substrate observer delivery — `§4.2` scale-agnostic, and `§4.1` step 4 applies `stat_deltas`: the engine already delivers AND mutates down.**
**The gap = target-population + documentation, not capability:** strategic `da.*`/`env.*` Keys carry faction/territory targets (registry schemas), no personal ones — step 4 has nothing personal to apply — and no `§3` rule prescribes populating them. **8 genuine cross-band seams / 15 type-edges** (19 = raw assessor count incl. near-lateral seam 9 `scene_slate→piety_track`):

| # | Seam | Crossing | Types |
|---|---|---|---|
| 1 | domain_actions → npc_behavior | provincial→personal | `da.*` ×3 |
| 2 | domain_actions → piety_track | provincial→personal | `da.*` ×2 |
| 3 | domain_actions → settlement_economy | provincial→settlement | ×1 |
| 4 | faction_politics → npc_behavior | provincial→personal | ×4 |
| 5 | peninsular_strain → npc_behavior | peninsula→personal | ×1 |
| 6 | peninsular_strain → settlement_economy | peninsula→settlement | ×1 |
| 7 | peninsular_strain → settlement_layer | peninsula→settlement | ×2 |
| 8 | scenario_authoring → settlement_layer | peninsula→settlement | ×1 |

Ruling J-1: (a) declare engine-mediated delivery canonical + A6-exempt (**strengthened** — adds authoring discipline + docs, not mechanism) or (b) author a §3 down-rule. Consume intent is already canonical (registry lists these consumers); only the rule is missing.

### Diagonal — ◐ split
Bottom-up diagonals covered (Thread Echo: personal-meta → provincial-faction; Accord Echo: scene → settlement-derived). Top-down diagonals (`da.*`/`env.*` → personal npc) absent — the same J-1 gap across a family boundary.

## §3 — QUANTITY-COUPLING LATTICE (beneath the Keys; verified blocks marked)

**Faction multipliers (✅ live-verified):** Treasury W×100 · Discipline Stab×10 · Reputation Inf×15 · Levies Mil×2 · Legitimacy Mand×20. **Settlement block (✅):** Mandate/Accord formulas as §2 above; Local Economy P×50 · Garrison D×20+Fort×30 · Public Order O×20. **Personal (unverified this corpus):** Health `(End+6)(MW+1)` · Stamina `3End+2Spi` · Concentration `3Foc+2Spi` · Composure ×3 ⚑J-12 · Thread-Fatigue Spi×5 · **wounds −1D to every personal pool.** Movement edges (income/drain `derived_stats §8.1`, derived-at-0 ratchet `§8.2`) pointed to, not transcribed.

**Clock couplings:** **CI≥60 → IP +2/season — the Church→Altonia valve, the campaign's central pacing coupling** · Accord≤1 → Strain +1/territory (cap +3) and IP banded +0..+3 · battles → MS −1/−2 flat (×3 struck; ±10/season net) · MS bands fall 60/40/20, recover +8 hysteresis + leading warnings · Strain bands 3–4/5–6/7–8/9–10 threshold effects · CI → Parliament `+⌊CI/20⌋ / −⌊CI/30⌋` · CI 100 → forced Mass Seizure (`((CI−60)/40)^3.3` from 60) · collapse → Strain +2 / IP +2 · treaty pair → Strain −1 (cap −2) · PI ≥20 → Crown elimination.

## §4 — LOOP INVENTORY (status INHERITED from source audits — game_flow §8 / verdict A7; not re-derived)

| # | Loop | Damper / cap | Status |
|---|---|---|---|
| L1 | Faction death spiral | FSS-LOOP-1 deterministic floor (Stab ≤2 ⇒ passive check can't reduce) + Consolidation + Survival Exception | **Ratified 05-30** |
| L2 | Wealth-0 Military ratchet | FSS-LOOP-2 re-muster +1 while W ≥1 | **Ratified 05-30** |
| L3 | Mandate runaway | LPS-2e saturating `7T/(T+6)` + clamp + mean-revert | **Ratified** |
| L4 | Instability contagion | Strain +3 / treaty −2 caps · IP bands · Accord normalization | **Bounded (ED-743)** |
| L5 | Substrate spiral (war→MS) | flat −1 (×3 struck) · Mending recovery · hysteresis + warnings (ED-882) | **Damped + warned** |
| L6 | Collapse → insurgency | deliberate amplifier, promotion-gated (L ≥3, Accord ≥4 avg, 2 seasons) | **Intended, gated** |
| L7 | `intent_of_game` itself | Slate surplus + Witness budget | **By design — damp excess only** |

A7 PASS: no cycle undamped+unbounded. The one machine-annotated cycle (Mandate↔L/PS) carries its §1.8 damper (ED-1008) — LC-3's first property check.

## §5 — COVERAGE VERDICT

| Direction | Coverage |
|---|---|
| lateral / horizontal | ✅ complete |
| bottom-up | ✅ covered & safeguarded (capped, gated, queued; A5 bars inverse) |
| vertical | ◐ eight handoffs up/lateral; §3.7 lone down-handoff; §3.9 down-modifier |
| **top-down** | ⛔ **OPEN J-1 — 8 seams / 15 edges (19 raw); engine delivers+applies, targets+rule missing** |
| diagonal | ◐ up covered, down absent (same J-1) |
| substrate | ✅ single-update rule routes everything |

**The single structural sentence:** the graph is fully wired laterally and bottom-up, safeguarded at every loop, and already delivers down at the engine level — the only thing between it and Robust is the J-1 ruling plus the J-2 registrations and the J-4 shadow-doc decision (NERS R-FAIL closes when register rows 1/3/4 close).

## §6 — RENDERED-VIEW INDEX & REGENERATION RULE

| Artifact | Shows | Authority class |
|---|---|---|
| `valoria_authoritative_graph.mermaid` (this orchestration) | scales × modules (status-coded) × direction-typed edges × clock valve × the 8 J-1 seams | hand-authored **synthesis** — update with this doc |
| `valoria_decision_unblock_graph.mermaid` | J-docket → lane items → outcomes DAG | hand-authored synthesis — update with workplan |
| `module_flowchart.mermaid` · `state_graph.mermaid` · `module_map_flat.md` | contract-level Key topology / state machine / 44-type matrix | **GENERATED from `module_contracts.yaml` — regenerate, never hand-edit** (LB-5 re-run pending) |
| per-system mermaids (threadwork/faction/settlement ×2 each) | system-internal flow + lifecycle | live system-depth |

## §7 — OVERLAY → REGISTER

Every defect drawn or named here lives once in workplan v4 §2: seams → #1 · ±Mandate echo text → #2 · F2 wall → #3 · shadow nodes → #4 · dup pair → #5 · name map → #6 · GD-1 read by victory → #7 · settlement gates → #19 · clock-naming → #13. No graph-local finding IDs exist.

`[SELF-AUTHORED — bias risk · verified at live HEAD d010fe27 this session · loop/NERS rows inherited (sims cited, not re-run).]`
