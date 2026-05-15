# Methodology Resolutions + Session Handoff

**Scope:** Resolves all 5 NERS findings and 7 self-bias limitations from file 14 (methodology audit), surfaces decisions where resolution requires a choice, and provides a session handoff document for continuation.

`[SELF-AUTHORED — bias risk]` Per PI layering rule. These resolutions are authored by the same party who proposed the methodology and conducted the audit. Independent reviewers would likely propose different counter-play designs, different calibration sequences, and different scope boundaries. Stated up front.

**Companion files:** Extends file 14 directly. Refers to file 9 (throughlines T-1..29, M-1..8), file 12 (moment-by-moment), file 13 (verification), file 14 (audit).

---

## Part I — NERS finding resolutions

### R-06 (P2) — Counter-play space not systematically designed

**Finding:** Just because counter-plays exist in principle (G-7/8/9) doesn't mean they're discoverable in practice.

**Resolution:** Counter-play design becomes a mandatory pre-implementation design pass. For each named historical play (G-1 through G-6), specify:

1. **The exact configuration that makes the play work** (which formations, terrain, reserve placement)
2. **The minimum-edit counter-play** — the smallest change to the defending army's deployment that would have defeated the play
3. **The condition for the counter-play's executability** (which primitives must exist)
4. **The discoverability vehicle** — how does a player find this counter-play without being told? Options: (a) AI demonstration during tutorial; (b) battle replay analysis showing "if you had done X"; (c) explicit doctrine-text descriptions; (d) emergent discovery via repeated play

**Specification for each G-tag:**

| Play | Min-edit counter | Discoverability vehicle |
|---|---|---|
| G-1 Cannae | Center-refuse + wing-engage (G-7) | Replay analysis; AI demo of Varro alternative |
| G-2 Pharsalus | Hold cavalry in reserve, screen with light troops | Doctrine text |
| G-3 Agincourt | Don't attack; force English to attack uphill (G-9) | Tutorial scenario |
| G-4 Panipat | Disperse elephants pre-charge; flank wagons (G-8) | Replay analysis |
| G-5 Marignano | Skirmisher screen to disrupt artillery | AI demo |
| G-6 Hastings | Maintain unit discipline; no pursuit | Replay analysis |

**Test:** A player who has never seen the historical pattern should be able to discover the counter-play within ~3–5 plays of being on the receiving end of the historical pattern.

**Status:** Counter-play design is now a tagged design-pass deliverable rather than an unspecified gap.

### S-03 (P3) — Reveal window for simultaneous resolution

**Finding:** Simultaneous resolution + blind commit + no specified reveal could produce player frustration over long battles.

**Resolution:** Reveal-window mechanic specified:

1. **Pre-commit phase (turn start):** Player sees current state of all visible units. Visibility determined by per-unit vision range × terrain. Units hidden by woods, beyond horizon, or behind larger friendlies are not visible.
2. **Commit phase:** Player commits orders. No information about opponent's commits.
3. **Resolution phase (between turns):** Engine resolves the 5-minute window.
4. **Post-resolution reveal:** Player sees what actually happened — what the opponent did within the resolution window, scoped by what was visible during/after the window. A unit that emerged from concealment is now visible from the moment it became visible.
5. **Replay scrub:** Player can scrub through the resolution window to see the dynamic-spacing changes (this is the visualization payoff for sub-tile vector precision per T-35 and the E-04 aggregation layer).

**Implementation note:** This makes scout / reconnaissance / light-cavalry units doctrinally significant. The Numidians at Cannae harassing the Roman allied cav — but never closing — is reproducible only if the engine models limited information.

**Status:** Resolved.

### S-04 (P2) — Scope limitation: battle-level only

**Finding:** Methodology is battle-level (tactical layer); operational, strategic, and campaign layers need their own design discipline.

**Resolution:** Explicitly bound the methodology to the **tactical layer (single battle, hours of game time)** and sketch the adjacent layers' methodology requirements without specifying them in detail:

| Layer | Scope | Methodology status | Suggested verification suite (if implemented) |
|---|---|---|---|
| **Tactical** | Single battle (hours) | **Specified** (this methodology) | 6+ historical battles (file 14) |
| **Operational** | Single campaign (days–weeks) | Not yet specified | Hannibal in Italy 218–216 BC; Belisarius in N. Africa 533–534; Mongol Western Campaign 1236–1242 |
| **Strategic** | Single war (months–years) | Not yet specified | 2nd Punic War; Hundred Years' War; 30 Years' War |
| **Campaign** | Bridge layer between strategic and operational | Not yet specified | Same as operational, with strategic context |
| **Geopolitical** | Multi-war / civilization (years–decades) | Not yet specified | Roman expansion 264–146 BC; Islamic conquests 632–732; Mongol unification |

Each layer's methodology should follow the **same bottom-up design / top-down verification pattern** but with its own primitives. Operational primitives include logistics, supply, march speed under load, attrition; strategic primitives include alliance dynamics, treasury, levy capacity, technology spread.

**Cross-layer integration** is itself a design discipline: how does a tactical outcome feed back to operational state? How does strategic state constrain tactical options (e.g., a strategically-exhausted army has lower cohesion ceilings)? This integration is a separate methodology task.

**Status:** Scope acknowledged. Adjacent-layer requirements sketched. Cross-layer integration tagged as separate work.

### E-04 (P2) — Sub-tile precision creates visualization complexity

**Finding:** Simulation precision (sub-tile vectors) vs. display legibility (whole-tile or unit-summary) creates a UX engineering problem.

**Resolution:** Specify the **aggregation layer** between simulation and display:

1. **Engine state:** Sub-tile vector positions, per-unit cohesion, per-unit facing — full precision retained.
2. **Display state:** Unit position shown as centroid + footprint outline; vector arrows show direction; cohesion shown as banner color/animation; lethal-density condition shown as overlay (red tint on affected tile).
3. **Detail-on-demand:** Player can zoom in to see sub-tile positions; zoomed-out view shows aggregated unit-as-block.
4. **Movement preview:** Before commit, hovering over a movement order shows the projected end-state position with confidence interval (if opponent action could deflect).
5. **Replay scrub (per S-03):** Allows player to step through resolution window at sub-second granularity to see the dynamic-spacing changes.

**Design principle:** **Sub-tile precision is engine-internal; player UI works at unit-level.** Trade: precision retained, legibility preserved.

**Status:** Aggregation layer specified at the level of UX policy. Detailed UX design is downstream.

### E-05 (P2) — Multi-objective calibration may not converge

**Finding:** Tuning all primitive parameters to make all 6 verification tests pass simultaneously is a non-trivial optimization that may not converge on first attempt.

**Resolution:** Specify **incremental calibration with stop-rules**:

**Phase 1 — Single-battle calibration.**
- Pick **Cannae** as the first verification (most canonical, best-documented, exhibits the most distinctive primitives — convex deploy, refused wing, lethal-density compression).
- Tune primitives until Cannae passes both achievability (T-39 phase 1) and counter-play (T-39 phase 2 — Varro options).
- **Stop-rule:** If Cannae alone cannot be calibrated within ~3 iterations of primitive tuning, the primitive set is fundamentally flawed and requires redesign before adding battles.

**Phase 2 — Sequential additions.**
- Add **Agincourt** to the suite. Re-test Cannae; re-test Agincourt. Tune to pass both.
- Add **Pharsalus**. Re-test all three.
- Continue with **Panipat → Marignano → Hastings**.
- **Stop-rule per addition:** If adding battle N requires breaking battle N-1's test pass, the new battle requires a *new primitive* (not a recalibration). Identify the primitive; add it to L0/L1/L2 as appropriate; re-test all.

**Phase 3 — Tier and cross-cultural expansion (V2 suite).**
- Add non-Western battles (per limitation 5 resolution).
- Add tier-tests (longbow-tier including Crécy + Poitiers + Agincourt; pike-and-shot tier).

**Total calibration effort estimate:** Phase 1 ~1 person-month; Phase 2 ~3–6 person-months; Phase 3 ~3–6 person-months. Cumulative 7–13 person-months for full V2 calibration.

**Status:** Calibration sequence specified. Tractability remains an engineering bet but the bet is now structured.

---

## Part II — Self-bias limitation resolutions

### Limitation 1: Multi-objective calibration tractability is an engineering bet

**Resolution:** Addressed by E-05 incremental calibration sequence above. If Phase 1 fails the stop-rule, methodology requires redesign before proceeding.

### Limitation 2: Verification suite necessarily incomplete (M-13)

**Resolution:** Specify the **suite expansion policy**:

- **Trigger for adding a battle:** When the engine produces an "unexpected" outcome from a historical-pattern scenario — i.e., a primary-source-documented pattern that the current primitives fail to reproduce.
- **Inclusion process:** (a) identify the surprising pattern; (b) identify the primitive responsible; (c) decide: tune the existing primitive (Phase 2 stop-rule), or add a new primitive (Phase 3); (d) re-test.
- **Suite size cap:** 12 battles in V1 suite; expand to 24 maximum in V2. Beyond this, regression-test cost outweighs marginal information.
- **Acknowledgment:** Methodology is open-ended, not closed-form. There will always be a battle that could surprise the system. The policy makes the open-endedness operational, not unbounded.

### Limitation 3: Historical realism as calibration target is a design choice

**Resolution:** Introduce **calibrated divergence** mechanism:

- **Realism dial parameter** (per-primitive, not global): 0.0 = exact historical pattern reproduction; 1.0 = fully divergent / pure gameplay tuning.
- **Divergence tracking:** Each non-zero divergence is documented with: which primitive, what historical value, what game value, why diverged.
- **Test invariance:** A divergent system should still pass non-divergent-primitive tests. If diverging primitive X breaks test Y unrelated to X, the divergence is invalid (the primitive's effect propagated beyond its design scope).
- **Example use:** Longbow effective range historically ~200–250 m. If game tile = 50 m, this is 4–5 tiles, which may be too far for tactical decision-making. Diverge to 150 m (3 tiles) with documented reason: "tactical decision-density." Test that Crécy/Agincourt still reproduce; if they do, divergence is valid.

**Status:** Mechanism specified. Mechanical implementation = each L0 primitive has an optional `divergence` field with `historical_value`, `game_value`, `reason`.

### Limitation 4: Self-review limitations real

**Resolution:** Specify **periodic independent audit policy**:

- **Trigger:** Every 6 months of development, OR when methodology-affecting changes are proposed, OR when a verification battle test changes (added, removed, or revised criteria).
- **Auditor:** Designated non-author reviewer (could be Jordan himself for the Valoria project — he is not the methodology author in this case).
- **Audit scope:** Re-run all verification tests; re-check primitives against current research findings; identify drift from methodology principles.
- **Output:** Audit report following the file-14 structure (all-directions + throughlines + NERS + limitations + recommendations).
- **Action threshold:** P1 findings require immediate methodology revision; P2 findings require revision within the next development cycle; P3 findings can be deferred.

### Limitation 5: Western-European bias in 6-battle V1 suite

**Resolution:** Specify **V2 suite expansion with global coverage**:

Add ~4 non-Western battles to the verification suite:

| Battle | Era | Distinctive primitive tested |
|---|---|---|
| Mohi 1241 (Mongol-Hungarian) | High medieval | Mongol feigned-retreat + horse-archery cycle |
| Red Cliffs 208 AD (Chinese, Han / Three Kingdoms) | Classical China | River-based naval-land integration; fire-attack primitive |
| Ain Jalut 1260 (Mamluk-Mongol) | High medieval | Mamluk furusiyya cavalry doctrine vs. Mongol; first major Mongol defeat |
| Tarain 1192 (Ghurid-Rajput) | High medieval | Cavalry-archery vs. heavy cavalry; pre-Mughal South Asian doctrine |

V2 suite total: 10 battles (6 European + 4 non-Western). Geographic spread: Europe (5), Mediterranean (1, Adrianople if added), North Africa / Levant (1, Ain Jalut), South Asia (2, Panipat + Tarain), China (1, Red Cliffs), Steppe / Eastern Europe (1, Mohi).

**Status:** Expansion path specified. Implementation requires per-battle primary-source review (same effort as files 1–8 of this research module).

### Limitation 6: AI play silent

**Resolution:** Specify **AI design pass as separate methodology work** with these requirements:

1. **AI plays within same primitive set.** No special AI bonuses, no information AI doesn't earn. The AI has the same orders, same constraints, same vision as a human player.
2. **AI difficulty tiers:**
   - **Novice:** Plays single-formation defaults; forgets reserve commits; doesn't use terrain optimally.
   - **Competent:** Uses textbook plays (G-1, G-3, G-5); recognizes obvious traps; basic counter-play.
   - **Expert:** Varies play to opponent observation; uses hidden reserves (G-2); recognizes setup for counter-play.
   - **Master:** Adapts to opponent's tendency; uses asymmetric scenarios (G-12); writes battle accounts (G-13).
3. **AI verification:** Each AI tier should pass a specific subset of the verification suite as the *active player*. E.g., a competent AI playing Hannibal should reproduce Cannae against a novice Roman; an expert AI playing Varro should defeat a novice Hannibal via G-7 counter-play.
4. **AI methodology audit:** Apply the same bottom-up design / top-down verification to AI behavior. AI tactics should emerge from compositional decision-making, not from scripted recognition of board states.

**Status:** Scope specified. AI design is a separate ~3–6 person-month effort, not addressable within the formations methodology.

### Limitation 7: Implementation cost not addressed

**Resolution:** **Preliminary effort estimate** for V1 Valoria tactical layer:

| Component | Effort (person-months) |
|---|---|
| L0 primitives (soldier-level) | 1–2 |
| L1 primitives (unit-level) | 2–3 |
| L2 primitives (formation cluster) | 2–3 |
| L3 primitives (army) | 1–2 |
| L4 integration (battle) | 2–3 |
| Sub-tile vector engine + tile grid | 2–3 |
| Aggregation/visualization layer (per E-04) | 2–3 |
| Reveal-window mechanic (per S-03) | 0.5–1 |
| 6-battle verification suite (per E-05) | 3–6 (calibration) |
| Counter-play design pass (per R-06) | 1–2 |
| **V1 total** | **17–28 person-months** |
| AI design pass (per limitation 6) | 3–6 |
| V2 suite expansion (per limitation 5) | 4–8 |
| Adjacent-layer methodology design (per S-04) | 6–12 each layer |
| **V2 total addition** | **13–26 + adjacent layers** |

`[CONFIDENCE: low]` on these estimates — they're order-of-magnitude only. Actual implementation will reveal cost factors not anticipated. Recommend revisiting after Phase 1 calibration completes.

**Status:** Preliminary estimate provided. Validation deferred to actual implementation.

---

## Part III — Resolution status summary

| Item | Resolution status |
|---|---|
| R-06 (counter-play space) | ✓ Specified as design pass; G-tags annotated with counter + vehicle |
| S-03 (reveal window) | ✓ 5-step mechanic specified |
| S-04 (scope limit) | ✓ Bounded to tactical; adjacent layers sketched |
| E-04 (viz complexity) | ✓ Aggregation layer policy specified |
| E-05 (calibration) | ✓ 3-phase incremental calibration with stop-rules |
| L1 (tractability) | ✓ Addressed by E-05 |
| L2 (suite incomplete) | ✓ Expansion policy specified |
| L3 (realism as target) | ✓ Calibrated divergence mechanism specified |
| L4 (self-review limits) | ✓ Periodic independent audit policy specified |
| L5 (Western bias) | ✓ V2 suite expansion with 4 non-Western battles |
| L6 (AI silent) | ✓ AI design pass scope specified |
| L7 (implementation cost) | ✓ Preliminary estimate provided |

**All 12 items resolved or scoped to deferred work with explicit specifications.**

---

## Part IV — Session handoff document

### Where stopped and why

**Stopped at:** Completion of methodology resolutions. Research + design-methodology phase is complete. Ready for either: (a) implementation start, beginning with L0 primitive contracts in code; or (b) further methodology work on adjacent layers (operational, strategic, campaign).

**Why stopped:** Context budget approaching upper bands; resolutions are a natural stopping point. The methodology has been proposed, audited, and resolved within the bounds of single-author self-review. Independent audit (per L4 resolution) is the appropriate next step before implementation commit.

### Completed and verified this session

| Deliverable | File | Commit | Status |
|---|---|---|---|
| Research catalogue | 00–08 | `8d716382` | ✓ committed, on repo |
| Throughlines + matchup matrix (T-1..29, M-1..8) | 09 | `8d716382` | ✓ committed |
| Battle-phase choreography | 10 | `8d716382` | ✓ committed |
| NERS audit of throughlines | 11 | `8d716382` | ✓ committed |
| Moment-by-moment dynamic spacing (40+ primary sources, 9 battles) | 12 | `bfc8a301` | ✓ committed |
| Verification + corrections (P1×2, P2×4) | 13 | `c632720d` | ✓ committed |
| Methodology audit (T-30..43, M-9..13, G-1..13, NERS) | 14 | `73ba75b7` | ✓ committed |
| Methodology resolutions + handoff (this file) | 15 | (pending commit) | this file |
| React/SVG visualization artifact (Cannae, Agincourt, Panipat × 6 phases each) | — | n/a | ✓ in /mnt/user-data/outputs/ |

**Total: 16 deliverables (15 markdown + 1 React artifact); 5 commits to `jordanelias/ttrpg` repo expected after this file commits.**

### Reading order for continuation

Recommended sequence for a new session picking up this work:

1. **File 9** — establishes throughline / meta-throughline taxonomy (T-1..29, M-1..8).
2. **File 12** — moment-by-moment dynamic spacing; the primary-source reconstruction foundation.
3. **File 13** — corrections to file 12 (P1 + P2 errors identified).
4. **File 14** — methodology audit, extending file 9's taxonomy with T-30..43, M-9..13, and introducing G-1..13.
5. **File 15** — this file; resolutions to file-14 findings and session handoff.

If only reading two files: 12 + 14.
If only reading one file: 14.

### Remaining items (ordered)

**Immediate (pre-implementation):**

1. **Independent audit of methodology by Jordan or designated reviewer.** Per L4 resolution. Output: audit report following file-14 structure. Methodology revisions per P1/P2 findings before implementation.
2. **Counter-play design pass.** Per R-06 resolution. Specify each G-tag's counter, conditions, and discoverability vehicle. Output: extension to file 14 or new file 16.
3. **Phase 1 calibration: Cannae alone.** Per E-05 resolution. Build minimal L0–L4 implementation; tune primitives until Cannae passes both achievability and counter-play tests. Stop-rule: ~3 iterations max before methodology redesign.

**Near-term (V1 development):**

4. **Phase 2 calibration: sequential additions (Agincourt → Pharsalus → Panipat → Marignano → Hastings).** Per E-05.
5. **Reveal-window mechanic implementation.** Per S-03 resolution.
6. **Aggregation/visualization layer.** Per E-04 resolution.
7. **AI design pass.** Per L6 resolution; scope 3–6 person-months.

**V2 / longer-term:**

8. **V2 suite expansion with 4 non-Western battles.** Per L5 resolution: Mohi 1241, Red Cliffs 208, Ain Jalut 1260, Tarain 1192.
9. **Adjacent-layer methodology design** (operational, strategic, campaign, geopolitical). Per S-04 resolution. Each is its own ~6–12 person-month effort.
10. **Cross-layer integration design.** Per S-04. How tactical outcomes feed operational state; how strategic state constrains tactical options.

### Gaps

`[GAP: Hastings and Adrianople reconstructions in file 12 were not web-verified in the file-13 audit — only 5 of 9 reconstructed battles received explicit cross-check. Full audit coverage is a follow-up.]`

`[GAP: Non-Western battles under-represented across the research module. 1 of 9 in file 12 (Panipat); 1 of 6 in file-14 verification suite (Panipat). L5 resolution proposes 4 additions; not yet executed.]`

`[GAP: AI play design absent from methodology. L6 resolution scopes the work; the work itself is separate.]`

`[GAP: Implementation effort estimates in L7 resolution are order-of-magnitude only with low confidence. Validation requires actual implementation experience.]`

`[GAP: Adjacent-layer (operational/strategic/campaign/geopolitical) methodologies not designed. S-04 resolution acknowledges this; the design work is deferred.]`

`[GAP: Counter-play discoverability test (R-06) specifies "discover within ~3–5 plays" as a criterion but doesn't specify how to measure this empirically. Playtesting protocol is undesigned.]`

### Decision context for continuation

Decisions made this session that downstream work should preserve unless explicitly revisited:

- **Tile = 50 m, turn = 5 min.** Per T-43 and file-12 derivation. Other points in this two-parameter space exist; this is a defensible choice but not the only one.
- **Soldier abstraction = free parameter.** Per T-42. Recommended: 10–50 historical men per L0 entity for performance × fidelity balance.
- **Reserves as first-class system.** Per T-38. "Held / committed" is a unit state, not emergent.
- **V1 verification suite = 6 battles.** Cannae, Pharsalus, Agincourt, Panipat, Marignano, Hastings. Expansion to 10 (V2) and 12 (V1.5 cap) per L2 resolution.
- **Calibration sequence:** Cannae first, sequential additions per E-05 Phase 2.
- **Calibrated divergence allowed.** Per L3 resolution. Each diverging primitive documented with historical_value, game_value, reason.
- **AI plays within same primitive set.** Per L6 resolution. No special AI advantages.
- **Methodology scope = tactical layer only.** Per S-04 resolution. Adjacent layers need separate methodologies.

### Files referenced (no fetch needed for continuation)

This handoff is self-contained alongside the file-9 / file-12 / file-13 / file-14 sequence. Continuation does not require re-reading the full primary-source corpus from files 1–8 unless modifying specific battle reconstructions.

For the visualization artifact (`battle_visualizer.jsx`): standalone React component, no external dependencies beyond standard React + Tailwind. Three battles (Cannae, Agincourt, Panipat) with 6 phases each, all corrections from file 13 surfaced in per-battle panels.

---

## Closing log

`[CONFIDENCE: high on resolution coverage — all 12 audit items have specified resolutions or deferred-work scopes. Medium on resolution adequacy — independent audit (L4 resolution) is the appropriate check before commitment. Low on implementation effort estimates (L7) — order-of-magnitude only.]`

`[ASSUMPTION: tag conventions established in file 14 (T-, M-, G-, NERS severity P1/P2/P3) continue in this file — basis: consistency with file-9 / file-14 sequence. If Jordan wants different conventions for resolution-tier tags, prefixes can be revised.]`

`[ASSUMPTION: handoff document format follows PI handoff_under_pressure specification — docs to read, where stopped and why, completed/verified, remaining items with decisions and context, gaps per logging_tags. Markdown artifact since handoff content exceeds 30 lines.]`

`[GAP: this file is itself self-authored and not yet independently audited. Per L4 resolution, periodic independent audit is the methodology's required check. The resolutions specified here are subject to that audit.]`

`[SELF-AUTHORED — bias risk]` Final flag. This entire resolution document is the methodology's author resolving the methodology's audit findings. An independent reviewer would likely propose different counter-play designs, different calibration sequences, different scope boundaries, and different effort estimates. The resolutions are rigorous within the bounds of single-author work — which is the bound being flagged. **The L4 resolution (periodic independent audit) is the methodology's own mechanism for transcending this bound. It should be exercised before implementation commitment.**

---

## Tag tally (this file)

| Tag class | New tags | Cumulative |
|---|---|---|
| Throughlines (T-) | 0 new | T-1..43 (file 9 + file 14) |
| Meta-throughlines (M-) | 0 new | M-1..13 (file 9 + file 14) |
| Gameplay opportunities (G-) | Annotated G-1..6 with counter + vehicle | G-1..13 (file 14) |
| NERS findings | 5 resolved | 0 P1 / 4 P2 / 1 P3 (all resolved) |
| Self-bias limitations | 7 resolved | 7 (all resolved) |
| Resolutions | 12 specified | 12 |
| Handoff structure items | 6 (docs / stop / done / remaining / gaps / context) | 6 |

**This file: 0 new tags introduced; 12 resolutions specified; 1 handoff document delivered.**
