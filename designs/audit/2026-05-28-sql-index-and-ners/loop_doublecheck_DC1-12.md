# Phase A Loop Map — Double-Check / Re-Test Findings

**Date:** 2026-05-28 · **Task:** audit (token c93a36df…; gate passed) · **Method:** adversarial self-audit of `loop_cascade_map.md`, testing every claim against source across all directions / scopes / scales. `[SELF-AUTHORED — bias risk]` — every map claim was treated as a hypothesis to falsify, not confirm. Each finding cites the section that proves it. **This is Pass 3 (re-review); it corrects and extends the map without silently rewriting it.**

---

## VERDICT (first)

**The map's cross-system *structure* is sound — the D-series accounting cascade is accurately mapped, and its dampers/caps are correctly cited and re-verified. But the map has one WRONG load-bearing claim (W1), it failed to surface a real canon contradiction sitting under that claim, it OMITS ~5 loop/structure classes, it uses a non-canonical scale ladder, and it asserts "heavily damped" without the per-cycle-gain computation that the one place I actually checked (MS) proved is necessary.**

The headline revision: **§0's "almost impossible to lose permanently" holds only if a Mending agent is active.** Without one, the world-scale MS spiral is a real, canon-faithful path to the single true terminal. R6's MS death-spiral was *substantially correct*, not an implementation artifact — I mis-grounded the keystone on historical backstory.

12 findings: 2 × P1, 5 × P2, 5 × P3.

---

## P1 — load-bearing errors (change the map's conclusions)

### DC-1 · W1 is wrong: MS does not self-heal at game-time
The map's "F1+F2 always push up and dominate F3; MS designed not to spiral" is **historical-trajectory backstory misapplied to game-time.**
- The Warden/baseline rates in `ms_trajectory §4` are historical and **decline to ~0.20 MS/year at game start** (≈ **0.05 MS/season**) — and `ms_trajectory §1` invokes P-07: the substrate "does **not** respond, heal, or repair." The upward 257-year climb was driven by Solmund (~25 pts) + Einhir-survivor Wardens, **both gone at game start.**
- Battle drain is **−1 to −3 MS/season** (`peninsular_strain §3.1`, `mass_battle §E.4`). The only game-time MS *recovery* is the **Mending operation** (Success +1, Overwhelming +2 — `threadwork §Mending`/L475), an **action requiring a practitioner agent to Mend a Gap.** Not automatic.
- So a peninsula at sustained war **with no active Mending agent** drives MS down — at ~60× the baseline rate. That is **canon-faithful behavior.**

**Revises:** map §0 pt 2; §4 W1 row; §6 row 1. The pair for "Battle→MS−1" is **not** "Warden+baseline Mending F1/F2" (backstory) — it is **an active Mending agent (Warden NPC AI or player Mending Gaps).** R6's MS spiral was the faithful consequence of a drain with no Mending agent, not a missing automatic damper. **The real open question is a DESIGN call: should game-time have passive Warden Mending, or is action-gated Mending the intent?** (→ Jordan.)

### DC-2 · Canon-internal contradiction on MS direction (map should have caught it)
Three sources disagree on which way MS moves:
- `ms_trajectory §2`: Force 1 baseline continuity **"always positive"** (toward 100).
- `clock_registry_v30 §MS`: MS "0–100, start 72, **direction ↓ (decay)**."
- `sim/peninsular/ms_track.py` L44: `MS_BASELINE_DECAY_PER_YEAR = -1` (baseline **decay**, applied year-end via `accounting.py` L57).

clock_registry + sim agree (↓); ms_trajectory's prose says ↑. **The map inherited the trajectory framing uncritically and reported MS as self-healing.** Either game-time net-decay is intended (post-Solmund, Wardens lowest — in which case `ms_trajectory §2` "always positive" is misleading for game-time and should be annotated) or the sim baseline is a sign error. **(→ Jordan; this is a canon defect on a load-bearing world variable, not just a map error.)**

---

## P2 — coverage gaps (loops / scales the map omitted)

### DC-3 · BG fuses omitted entirely → new **F-series**
`royal_assassination_fuse` (`params/bg/royal_assassination.md`) and `tensions_deck` (`params/bg/tensions_deck.md`) are **timed succeed-on-fire escalators** (S0 seed → S8+ fire). Royal fuse: leader death → **faction identity inversion / succession** (Almud dies → Lenneth throne, Crown flips pro-Einhir). Tensions deck: e.g. Feldmark Famine → Prosperity collapse → economic cascade (→ muster/Wealth, D5/D6). These are **guaranteed escalation unless the player intervenes** (investigation costs card slots) and feed D1 + succession. The map has **no fuse/timed-escalator class.** Add F1 (royal fuse), F2 (tensions deck), and treat "succeed-on-fire unless intervened" as the damper-by-agency.

### DC-4 · Relational scale + defection-cascade loop collapsed into one V5 line
Canon `scale_transitions §2` names **Relational** a full scale (TS 50+, Coherence −1). `npc_relational_graph_v30.md` (680L) specifies **6 edge types** (sworn-bond, liege-vassal, kinship, patronage, rivalry…), strain mechanics, **liege-vassal defection cascades** (KOEI officer-network model — mid-chain defection propagates), and Conviction-coupling Resonant Styles. A **defection cascade** (NPC defects → chain defects → faction officer loss → D1 weaker → more defections) is a distinct Relational-scale loop. The map folded an entire scale + its cascade into V5. Add R-series (relational defection / knot-strain cascades).

### DC-5 · faction_succession_split omitted as a loop
`faction_succession_split_v30 §2`: leader elimination (= D1 Trigger 5 named-officer-killed) → contested succession → **faction SPLITS** (Stability −1, Mandate −1 turnover; splinter starts Stability 2 fragile). Two weaker factions **amplify D1** and couple to D4 (RM emergence trajectory §4). A fragmentation amplifier the map listed in the registry but never mapped.

### DC-6 · conviction→faction-behavior cascade omitted
`faction_behavior §3.2`: NPC `effective_convictions = α·personal + (1−α)·supervisor.effective`, aggregated up a supervisor graph to **faction effective convictions → Mission → action selection (GD-2) → world-state → (Domain Echo Scar fires → NPC conviction)**. A genuine **cross-scale loop: personal conviction → faction behavior → world → personal.** Zero-vector leader → Provisional state → forced succession (→ DC-5). Omitted.

### DC-7 · Scale ladder is non-canonical and internally inconsistent
Map ladder = Personal/Scene/Provincial/Territory/Peninsula/World. Canon `scale_transitions §2` = **Object/Personal/Relational/Territorial/Structural** (5). Engine audit §2 = 6 (adds Foundational). The map **omits Object** (one item/wound — healing, Thread-signature reading, Coherence 0 cost), **collapses Relational** (DC-4), and uses **non-canonical names** for the upper rungs. For Phase-B consumption and durability, **re-anchor the ladder to canon's named scales.**

---

## P3 — precision / asymmetry / methodology

### DC-8 · "Heavily damped" asserted without computing per-cycle gain < 1 (the core methodological hole)
The diagnostic skill (Phase 4b) requires showing **gain < 1 per loop cycle** before calling a loop damped. The map asserts "heavily damped" across §2–§5 **without one gain computation.** DC-1 is the proof this matters — I asserted MS self-heals without checking the rate, and was wrong by ~60×. **Phase B must compute, per loop, the per-cycle drain magnitude vs the per-cycle damper magnitude (e.g., Stability: is recovery +1/clean-season + peace ≥ the Trigger-1/5 drain rate under sustained pressure? Strain: does −1/peaceful + treaty −2 exceed +1/territory × N at the +3 cap?), not assert "capped ⇒ safe."** A cap bounds the *rate*, not the *direction* — a capped one-way drain still spirals.

### DC-9 · V2 asymmetry: positive Thread Domain Echo missed
V2 listed only negative edges (Dissolution→Stability−, Gap→Stability−). It omitted **Mending (Territorial+) → Mandate +1** (`scale_transitions §5.6`) — which is *also* the W1 recovery action (DC-1). Mending is simultaneously the MS damper and a faction-Mandate-positive cross-scale edge. Add it; the omission biased V2 toward drain-only.

### DC-10 · miraculous_event omitted — the rare positive Accord/PT injector + a TD transfer loop
`miraculous_event_v30`: Mending event → **Accord +1** (radius, one-time), PT +1, SA +1, Mandate +1 (§20.5, §25); and a Reformed-Doctrine **TD escalation** where at TD 3 any season the Church loses PI gives **Hafenmark PI +1** (zero-sum Church↔Hafenmark transfer loop). One of the **few world-scale Accord RECOVERY edges** — omitting it (like DC-9) biased the whole map toward drain-only and made the cascade look more spiral-prone than canon is.

### DC-11 · Varfell Intel resetting ratchet omitted
`clock_registry`: Intel Advancement Counter 0–3, **resets to 0 at 4 → Intel +1** — a resetting accumulator ratcheting a stat upward. Minor, but a missed accumulator class (cf. CI ratchet D3).

### DC-12 · clock_registry not used as the authoritative bounds source
The map grounded caps/floors piecemeal from individual design docs. `clock_registry_v30` is the **canonical registry of every track's range/direction/floor** and would have (a) grounded all caps in one place and (b) surfaced DC-2 (MS ↓) immediately. **Phase B: cross-check every bound against clock_registry** (it confirmed Composure 7–13, Wounds 0–max=floor(End/2)+1, Stability floor 0=eliminated, Knot Count 0–floor(Bonds/2)+1, TS 0–100 cap — all consistent with the map's piecemeal values, but the registry is the source of record).

---

## VERIFIED OK (scope-confirmation, not balance)

- **D1 chain, dampers, caps** — re-verified against `faction_layer §1.2/§1.3/§1.5`, `peninsular_strain §3/§4`, `mass_battle §E`. Accurate as cited. Collapse-with-Survival-Exception + reconstitution correctly corrects the diagnostic skill's "termination, not a bound."
- **R6 drain-absence** (battle→Mil, battle→MS, Turmoil→Mandate) — **re-verified at current HEAD `05f523a3`** (not R6's `9763d23`, not session-log's `307e86ca`): still absent. `massbattle.py` (1905L) has 0 MS adjustments. **Caveat:** sim DOES apply MS baseline decay −1/yr (DC-2) — so "sim omits MS dynamics" was too strong; sim drifts MS down already.
- **Domain Echo caps** (1/scene/faction PP-329; ±2; queued — `§5.2/§5.3`) and **V4 hysteresis** (ED-749) — accurate; the cross-scale plumbing is genuinely the best-damped layer.
- **D2 no-cross-feed** (`§4.4`), **D3 CI floor + cubic Mass-Seizure gate** (`victory §7`), **D5 Wealth-0 = Discipline-not-Military** (`military_layer §1.7`) — accurate; D5 correctly corrects R6's "Mil −1" assumption.

---

## Corrected §0 verdict (supersedes map §0)

1. The cross-system cascade is real and, in canon, **rate-capped** — but "capped" ≠ "damped" (DC-8). Per-cycle gain is uncomputed; Phase B must compute it per loop.
2. **The world-scale MS spiral is a real path to the one true terminal (Second Calamity, 10 seasons MS≤5) whenever no Mending agent is active** (DC-1). This is the opposite of the map's original claim. Whether to add passive Warden Mending is a Jordan design call.
3. The danger remains **partial implementation**, but the pairing is subtler than "drain + automatic damper": several dampers are **agent-gated actions** (Mending, Govern, Suppress, fuse-intervention). Implementing a drain without implementing the **agent that takes the paired action** reproduces R6's spirals faithfully.
4. **Coverage was incomplete:** add F-series (fuses, DC-3), R-series (relational defection cascades, DC-4), succession-split (DC-5), conviction cascade (DC-6); re-anchor the scale ladder (DC-7); add the positive edges (DC-9, DC-10) that the drain-biased map omitted.
5. The strongest standalone defect (faction bare-stat 1–7D feeding D1, ER-1) is unchanged and confirmed.

---

## Phase B impact

- **Promote to P1 for Phase B:** W1/MS (DC-1) and the MS-direction contradiction (DC-2) — was previously a "keystone," now a defect requiring a design decision.
- **Add to the loop register:** F1/F2 (fuses), R1 (relational defection cascade), the succession-split and conviction-cascade couplings, miraculous-event injector. Phase B reading set gains: `npc_relational_graph_v30`, `npc_behavior_v30` (Resonant Styles + Scar firing), `params/bg/royal_assassination.md`, `params/bg/tensions_deck.md`, `clock_registry_v30` (bounds cross-check), `miraculous_event_v30`.
- **Methodology fix (binding for Phase B):** every loop gets an explicit per-cycle gain-vs-damper computation (DC-8); no "damped" verdict without it.
- **Coherence recovery (V5 open GAP)** still unresolved — `threadwork §3.5 Recovery` exists (L663: "Full rest resets to 0. Meditation reduces by Spirit score" — but that line is the **Out-of-Breath/Composure** recovery at L194/L570, not Coherence; and L705–706 show Coherence-recovery arcs require a full-season arc and can fail to NPC-conversion). **Phase B must full-read `threadwork` Part 3 to settle whether Coherence has a routine recovery path or only a season-arc gated one** — if the latter, V5 is a slow one-way drift (Lesson-5 confirmed).

---

## Drift found during double-check (adds to map §8)

- `[DRIFT: ms_trajectory §2 "Force 1 always positive" vs clock_registry §MS "↓ decay" vs sim ms_track −1/yr — canon-internal sign contradiction on MS. = DC-2.]`
- `[DRIFT: current ttrpg HEAD 05f523a3 — session_log_current HEAD 307e86ca and R6-audit HEAD 9763d23 both stale; R6 (2026-05-25) is itself ahead of the session-log's last-recorded session (2026-05-20).]`
- `[DRIFT: sim/peninsular/ms_track.py L19 docstring flags accounting._ms_decay (accounting.py L36-39) as a duplicate of apply_ms_baseline_decay — two MS-decay paths; in-code DRIFT note unresolved.]`
- `[ASSUMPTION: R6's "drains absent" re-verified by grep at 05f523a3, not by full sim trace — basis: targeted regex on the 6 files R6 named; a hidden adjust via indirection would be missed. Phase B sim work should trace, not grep.]`
