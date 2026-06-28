# Valoria — Loop-Safety Ledger (Consolidated)

**Audit · 2026-06-04 · `[SELF-AUTHORED — bias risk]` (corrects this session's own prior-turn L2 finding)**
A reconciled master of every cross-system / cross-scale feedback loop in Valoria, with current canonical loop-safety status (damper · cap · gain · verdict). Lens: `valoria-resolution-diagnostic` Phase 4 (Lesson 5 — a loop is a defect only when **both undamped and unbounded**).

---

## §0 What this is — a consolidation, not a fresh audit

The audit gate's first instruction is *check prior outputs*. The loop set has already been audited across four artifacts; this ledger collates them, reconciles to **current** canon, adds the layer they pre-date, and isolates what remains open. Sources folded:

- `designs/audit/2026-05-28-sql-index-and-ners/passC_loop_map_and_NERS.md` — the loop map + per-system NERS verdicts (already self-corrected once).
- `designs/audit/2026-05-28-sql-index-and-ners/loop_doublecheck_DC1-12.md` — adversarial re-test (DC-1..12; 2×P1, 5×P2, 5×P3).
- `designs/audit/2026-05-25-r6-death-spiral-reconciliation/findings.md` — the MS death-spiral reconciliation.
- `faction_layer_v30.md` §1.4 **FSS-LOOP-1** + §5.7 **FSS-LOOP-2** — the 2026-05-30 resolution-diagnostic ratifications now **in canon**.
- per-system diagnostics + NERS verdicts (`resolution_diagnostic_*.md`, `ners_verdict_*.md`, 2026-05-28).
- this session's `valoria_key_cascade_scope.md` (Key-substrate propagation map).

Per `<document_consolidation>`: the originals stay in git history; formally superseding/archiving them is a commit step for Jordan's call, not done here. Substantive open conflicts are carried as `[OPEN — Jordan]`, never silently resolved.

**Companion artifacts (this session):** `loop_gain_sim.py` + `loop_gain_results.txt` (the DC-8 gain pass, §7) and `key_cascade_scope.md` (the propagation map, §1).

---

## §1 The unifying finding (validates the per-loop approach)

From the cascade scope (`key_substrate_v30 §2.3 invariant 4`, §4.6, §5): the Key substrate guarantees the **provenance graph is acyclic** — but every turn of a *behavioral* loop emits a new, legitimately-caused Key, so the graph grows strictly forward and never trips cycle detection **even as the underlying systems spiral**. The engine therefore provides **no loop-safety whatsoever**; it lives entirely in the consuming systems. This is exactly why each loop below must be hand-verified for a damper and a cap — the prior audits' per-system method is not optional thoroughness, it is the only place loop-safety can be checked. The substrate's acyclicity is necessary, not sufficient.

---

## §2 Consolidated loop register (current canon)

`agent` = damper is an agent-gated *action* (requires a player/NPC to act), not automatic. `gain?` = is a per-cycle gain computed (DC-8 standard) vs only damper/cap *structure* cited.

| Loop | Scale | Drain / amplify | Damper | Cap / bound | gain? | Verdict |
|---|---|---|---|---|---|---|
| **MS / threadwork** (world-tearing) | peninsula/world | battle → MS −1..−3/s → Fractured: spontaneous Gaps → more drain (`peninsular_strain §3.1`, `mass_battle §E.4`) | Mending op +1/+2 — **agent-gated** (`threadwork §Mending`) | **−10/s net cap (CONTESTED, DC-2)**; 4-season floor | **YES (Monte-Carlo)** | Bounded **iff** cap holds **and** a Mending agent is active — else a faithful path to the single terminal (DC-1) |
| **faction-collapse** | territory | Stability triggers → 0 → collapse | Stability +1/clean season (§1.3, agent) · **FSS-LOOP-1** deterministic Stab≤2 floor (passive decay cannot reduce) · **FSS-LOOP-2** Military re-muster while solvent | Survival Exception 1×/campaign; **reconstitution ≠ extinction** (§1.5 → settlement §6.2) | analytic + sim | **BOUNDED** — collapse only via *active* Trigger 1–5 (intended, GD-3) |
| **D-series accounting** (CI / Treasury / L-PS) | territory | DA outcomes → L/PS → strictness → DA Ob | DA-Ob clamp **±2** (`faction_behavior §3.7`) **+ Mandate↔L/PS mean-reversion** (negative feedback, `settlement §1.8`) | L/PS **0–7**; Mandate saturating `T/(T+6)`, clamp 0–7 | **YES — gain 0.966** | **DAMPED + BOUNDED (verified)** — mean-reverting + saturating; returns to equilibrium |
| **Strain / Turmoil** | peninsula | Accord≤1 territories → Strain +1/ea → Crisis erodes Accord → more Strain | decay −1..−3/s (clean territories, treaty pairs, diplomacy; `peninsular_strain §4.2`) | **Strain 0–10; advance capped +3/s** (§4.1, explicit anti-runaway) | **cap-proof (sim)** | **CAP-BOUNDED (verified)** — ratchets to ceiling 10 under sustained drive + weak governance (37/40s); damps to 0 under active de-escalation; recovery is active |
| **L-CONV** (Scar → crisis → arc) | personal | Scar → conviction shift → behavior → Scar | 1 Scar/season; concentration weights | per-Conviction thresholds; salience decay (`key_substrate §4.5`) | no | Bounded single-path; **multi-Conviction cascade `[INTENT UNDETERMINED]`** (needs `conviction_axis_matrix`) |
| **L-CONV → faction** (cross-scale) | personal→peninsula | NPC convictions → faction effective convictions → Mission → action → world → Domain-Echo Scar → NPC | cascade damping toward equilibrium (`faction_behavior §3.2.3`) — **SUSPENDED when leader.scars ≥ 3** | — | **UNREAD/partial (DC-6)** | damper present but suspends at high leader scars; gain owed |
| **L-SPLIT** (succession → split) | territory | leader killed → contested succession → faction splits → 2 weak factions amplify collapse | re-merge at Mandate ≥ 3 | RM emergence **4-season cooldown (UNTUNED)** | no | Bounded; cooldown PROVISIONAL |
| **R-series / L-DEFECT** (relational defection) | relational | edge break → chain defection → officer loss → weaker faction → more defection (`npc_relational_graph_v30`, KOEI model) | strain −1/s; ½ spillover; tier-3 rare | strain tiers | n/a | **FAIL NERS-R — defection cascade UNBUILT (B1.2, §7 hooks only)** |
| **L-INSURG** (revolt → insurgency → faction; GD-3) | territory | revolt → insurgency → new faction | suppression 2→1; sustained-2 gate | Legitimacy gates | n/a | **RESOLVED-APPLIED** — dissolution down-path authored to canon 2026-05-29 (ED-881, Jordan-ratified; supersedes passC's "missing") |
| **mass-battle morale** (rout → contagion) | territory | rout → morale contagion | rout contagion **braked**; rally/reform | per-turn | sim in-band | Bounded (design); separate P0 *sim-stub* impl gaps |
| **L-MIRACLE** (RWCE → Accord/SA) | peninsula | miraculous event → Accord/Mandate | one-time Accord; TD counter | SA-gated | no | Bounded |
| **F-series (BG fuses)** | territory/peninsula | royal-assassination fuse (leader death → faction inversion) · tensions deck (Famine → Prosperity collapse → economic cascade) | succeed-on-fire **unless player intervenes** (agency) | timed S0→S8 | **UNREAD (DC-3)** | structure mapped; gain owed; feeds collapse + succession |
| **Varfell Intel ratchet** | territory | intel accumulation | reset at 4 | 0–3 | **UNREAD (DC-11)** | minor accumulator |

---

## §3 Status classes

**A — Positively verified bounded (gain computed or canon-ratified):**
MS/threadwork (Monte-Carlo, *conditional* — see §6); faction-collapse (sim + FSS-LOOP-1/2 in canon); **D-series accounting** (gain 0.966 < 1, mean-reverting + saturating — DC-8 pass this session); **Strain/Turmoil** (cap-proof sim: bounds at 10, +3/s advance — DC-8 pass this session).

**B — Bounded by cited dampers/caps, per-cycle gain still owed:**
L-CONV (deferred — needs `conviction_axis_matrix`), mass-battle (cited prior: braked, sim-validated in-band; full recompute needs `mass_battle §E`), L-SPLIT and L-MIRACLE (gated-event loops — a continuous gain is the wrong frame; bounded by gating, see §2). **DC-8: capped ≠ damped** still applies to the un-recomputed members.

**C — Incompleteness (unbuilt — *not* instability):**
- **L-DEFECT** — the relational defection cascade (the system's load-bearing consequence) is unbuilt (hooks only, B1.2). Remediation is a *build* (a PP), not a lesson, and is tracked as a build item rather than an ED candidate.
- **L-INSURG — RESOLVED** (was a Class-C fail in passC): the GD-3 dissolution down-path was authored to canon 2026-05-29 (**ED-881**, Jordan-ratified, grounded in RAND *How Insurgencies End*). No longer a fail; corrected here.

**D — Unread / un-gain-computed (the rigor + coverage debt):**
F-series fuses, L-CONV→faction cascade, R-series relational, Varfell ratchet.

---

## §4 Emergent-narrative loops (NEW — articulation/PP-688, absent from the prior map)

The prior loop map pre-dates heavy articulation-layer focus. The Key substrate's universal articulation sink (`articulation_layer_v30 §5`) adds two loops:

- **L0 — the `intent_of_game` master loop:** player decision → Key emission → world/state change → articulation (cut scene / annual Chronicle) → player decision. This is the game's *designed* positive feedback loop — the thing the engine exists to produce. Damper: player pacing (human-in-loop). Cap: none mechanical, by design. The diagnostic flags `intent_of_game` itself as a positive loop requiring Lesson-5 discipline; here that discipline is satisfied by the player being the loop's clock, not by a mechanical bound.
- **L3 — cascade-cluster surfacing:** cascade-fidelity clustering (`articulation §3.1` trigger 9, cosine-sim ±0.40 / 4 seasons) → cut scene → player attention → action. **Self-bounds**: fires once per regime, refire only on regime transition.

Neither is a defect; both are recorded so the loop set is complete. They compound *onto* the §2 loops via the articulation sink rather than forming new drains.

---

## §5 The standalone defect (non-loop; confirmed across every pass)

Not a loop, but the single strongest standalone resolution finding, unchanged through passC and the DC re-test:

> **Faction bare-stat 1–7D roll delivering binary verdicts on pivotal, irreversible outcomes** (seizure, parliamentary vote) at the small-pool floor → **Lesson 3** (route through deterministic accounting / aggregate the pool). NERS-R fail (fragile small-pool binary), S fail (dice on a deterministic layer), E fail (a roll the player cannot meaningfully influence).

**Candidate remediation already drafted:** `designs/audit/2026-05-28-resolution-diagnostic/domain_action_resolver_spec.md` — the deterministic domain-action resolver. This is the same artifact relevant to the opening question of this thread ("do we need a domain-action resolver?"): one exists in spec, addressing exactly this defect. Its ratification status should be checked.

---

## §6 Open DESIGN decisions — `[OPEN — Jordan]`, not mine to resolve

These gate verdicts and are owner calls; two touch the metaphysical layer and are explicitly out of editorial scope.

1. **MS Mending model (DC-1) — the load-bearing one.** Should game-time have *passive* Warden Mending, or is *action-gated* Mending the intent? MS does **not** self-heal at game-time (the historical climb was Solmund + Wardens, both gone at start; P-07: the substrate does not self-repair). With no active Mending agent, sustained war drives MS to its single terminal at ~60× baseline — **canon-faithful**, not a bug (R6 was substantially correct). MS is the *Meaning Substrate* (metaphysical, Jordan's layer); the loop-safety question is mechanical but the resolution is a design+metaphysical call. **→ Jordan.**
2. **MS direction contradiction (DC-2).** `ms_trajectory §2` says baseline "always positive" (↑); `clock_registry §MS` and `sim/peninsular/ms_track.py` say decay (↓, −1/yr). Three canonical sources disagree on a load-bearing world variable. **→ Jordan** (canon defect, not a map error).
3. **−10/s MS net-loss cap (DC-2).** Contested; the MS NERS-R verdict is conditional on it holding (without it, instakill is possible).
4. **L-SPLIT RM 4-season cooldown** — untuned; smoke-test.
5. **L-CONV multi-Conviction cascade severity** — `[INTENT UNDETERMINED]`; needs the axis matrix + an intent ruling.

---

## §7 The remaining rigor (DC-8) — narrowed this session

**This session's DC-8 pass** (`loop_gain_sim.py` / `loop_gain_results.txt`) computed two of the previously-uncomputed loops:
- **D-series (Mandate↔L/PS):** per-cycle gain **0.966 < 1** — strictly contracting (slow but damped), via the §1.8 mean-reverting feedback + saturating `T/(T+6)` aggregate; Mandate clamp 0–7 confirmed. **Promoted to verified-damped.**
- **Strain/Turmoil:** **cap-proof** — bounds hard at 10 with +3/s advance; ratchets to the ceiling under sustained drive + weak governance (37/40 seasons pinned), damps to 0 under active de-escalation. Lesson-5-safe by the cap (not unconditionally self-damping). **Promoted to verified-bounded.**

**Still owed:** L-CONV (needs `conviction_axis_matrix` cascade coefficients, per DC-6); mass-battle morale (a real recompute needs the `mass_battle §E` morale formula — only cited-prior here); the Class-D loops (F-series fuses, conviction→faction cascade, R-series relational). L-SPLIT and L-MIRACLE are gated-event loops where a continuous gain is the wrong frame — bounded by gating, no sim owed. The MS gain stands (Monte-Carlo) but is **conditional on the §6 decisions**, which no computation can settle.

---

## §8 What changed since the prior passes (reconciliation)

- **faction-collapse:** the original diagnostic called it "undamped terminal" → passC **retracted** that (damped + bounded) → 2026-05-30 **FSS-LOOP-1/2 ratified the fix in canon**. This session's prior-turn L2 ("damped but terminally unbounded — true finding") read the SKILL's stale worked example and is **corrected here** to BOUNDED.
- **L/PS:** Legitimacy and Popular Support are now **per-settlement values (0–7)**, not faction state (LPS-1, Jordan ruling 2026-05-30; faction-level is a derived saturating aggregate). The D-series loop therefore operates on bounded per-settlement meters. (This is a Jordan canon-structure decision — recorded, not contested.)

---

## §9 Next steps (ranked)

1. **Jordan decisions on §6** — above all DC-1 (MS Mending). It gates the MS verdict and the entire question of whether the world can reach its single terminal with no agent intervention.
2. **Finish the DC-8 gain pass** — D-series + Strain done this session; remaining: L-CONV (extract `conviction_axis_matrix`), mass-battle morale (recompute against `mass_battle §E`), and the Class-D loops once read.
3. **Build the remaining incompleteness fail** — L-DEFECT defection cascade (B1.2/B1.3): author the missing mechanic (a PP). (L-INSURG's dissolution down-path is already done — ED-881.)
4. **Read + map the unread loops** — F-series fuses (`params/bg/royal_assassination.md`, `tensions_deck.md`), R-series relational (`npc_relational_graph_v30`), conviction→faction cascade (`faction_behavior §3.2` full extraction).
5. **Resolve the bare-stat defect (§5)** — check the `domain_action_resolver_spec` ratification status and route the pivotal DA rolls through it.

*Read-only consolidation; changes no canon. Candidate P1 ledger entries (the two incompleteness fails; the MS contradiction) are flagged, not written — appending to `editorial_ledger.jsonl` is a commit step for Jordan's call. Belongs in `designs/audit/2026-06-04-loop-safety-ledger/` if committed.*
