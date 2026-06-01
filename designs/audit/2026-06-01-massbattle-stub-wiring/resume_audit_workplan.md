# Mass-Battle Engine — Stub/Wiring Audit + Resume Workplan
**Date:** 2026-06-01 · **Engine:** `tests/sim/sim_mb_sigma.py` @ `8b50144c` (commit `733cbc67`)
**Scope:** ratify current canon; audit stubs/wiring; sequence the speed/facing build.
`[SELF-AUTHORED — bias risk]` engine is largely my own work this session; findings stated as an independent reviewer would.

---

## PART 1 — RATIFIED CANON (current state)

- **σ-leverage engine** is the sole mass engine; advantages enter as δσ net-boosts, spine unchanged.
- **`PER_CELL=0` (default, shipped) is byte-exact to base `0dea67d1`** — re-verified 120/120 this session. All envelopment work lives in the opt-in `PER_CELL=1`/`PC_REFUSE` path.
- **Committed envelopment layer** (per-cell): wheel + FOV/perception + pinning + refusal + structural wrap (F1/F2/F3 nominal-span, mirror-unbiased *by construction*) + Polybius gap-trap pocket + **vectorized-depth resistance + oblique-offense roll-up** (commit `733cbc67`).
- **Roll-up / vectorized depth (`733cbc67`, RATIFIED):** depth measured PARALLEL to the attack vector (`_support_along_vector`, partial-cell weighted); flank-scoped roll-up gated by `MIN_DEPTH` (no attrition double-count). Validated 2-bank n=80: 11/13 CI-consistent (= baseline), H3 +4.4 & H11 +4.4 more central, H5 held, mirror inert, toggle-off 120/120.
- Current per-cell gauge: **11/13 CI-consistent**; persistent OUT = H7 (GappedLine open-gap base disadvantage) and R1 (ranged open-field — separate ranged-model issue).

---

## PART 2 — SPEED / FACING DESIGN (Jordan directive 2026-06-01)

Three mechanics, reframed against the actual code (most are *refinement*, not new build):

- **(A) Cavalry deals full / takes less / morale shock.** Deal-more-take-less ALREADY emerges from **puncture** (`a_pen = a_mom − b_mom` + cavalry `charge_pen` → `ns` boost; via opposed-degree math one boost both raises own degree and lowers enemy's). **Gap: morale shock** — puncture is combat δσ, not a morale hit. du Picq's *moral effect* (charge breaks morale at/just before impact) needs a distinct morale term.
- **(B) Speed → penetration depth.** Currently `a_pen` is absorbed by `_defender_depth` (old `col_grid` column depth, full subtraction). Rewire to `_support_along_vector` (depth along the charge vector) and **scale absorbing depth inversely with speed** (faster → fewer ranks stop it). Deeper unabsorbed penetration feeds δσ + the new morale shock.
- **(C) Facing → deals less (not only takes more).** LARGELY EMERGENT: octagon `angle_mod` lowers a mis-facing unit's `ns`, which via opposed degrees makes it both deal less and take more. Verify empirically; add the deferred explicit bad-facing trigger only if the coupling is insufficient (avoid redundant apparatus — NERS-N).
- **TOP-DOWN ANCHOR Jordan did not name but history demands — the prepared-defense exception.** Cavalry shock devastates unprepared/flanked/thin/disordered infantry but is REPELLED by braced+deep+disciplined formations (Waterloo squares; the pike's raison d'être). `charge_pen=3` is flat, so speed→deeper-penetration WITHOUT this exception makes cavalry ahistorically dominant. Defender depth × discipline × stance must be able to negate the charge (deep+steady repels → charger eats the morale shock; thin+flanked+disordered gets punched through + shocked).

---

## PART 3 — STUB / WIRING AUDIT (severity-ranked, worst first)

| # | Finding | Type | Site |
|---|---------|------|------|
| **S1** | **Canonical `Unit.speed` (Slow/Standard/Fast) wired ONLY to pursuit, never to combat.** Two disconnected speed models: `Unit.speed` (canonical, mass_battle_v30 L120) read only in `pursuit_damage`/victor-pursuit; the per-cell momentum chain (`cell_speed`→`cell_last_speed`→`_momentum_speed`→puncture) is the de-facto *combat* speed mechanism and never references the canonical tier. | WIRING GAP (load-bearing) | 1039; 2230-2248, 2517 vs 704/755/1284/1722 |
| **S2** | **Cavalry/charge/momentum/puncture subsystem has ZERO gauge coverage** — no cavalry or Fast unit in the battery ("noted but NOT WIRED — no cavalry in current battery"). `charge_pen`, `_momentum_speed`, puncture absorption, `PC_CAVALRY_SPEED_MULT` all UNVALIDATED. | TEST GAP (critical) | line 70; gauge battery |
| **S3** | **`charge_pen` flagged "stubbed mechanic being wired"; full wiring "requires power × facing inputs."** Wired into puncture as a flat +3 (cavalry), but should scale with charger power and defender facing. | PARTIAL WIRING | 70-72, 780-782, 1729 |
| **S4** | **Penetration absorbed by old column depth, not the vectorized primitive, and not speed-scaled.** `_defender_depth` (mean `col_grid` block depth) ≠ `_support_along_vector`. (Jordan B) | WIRING GAP | 1731-1732, `_defender_depth` |
| **S5** | **Bad-facing→output combat trigger DEFERRED to v14** ("available for v14+ when paired with a proper bad-facing trigger"). Facing→deals-less currently only emergent. (Jordan C) | DEFERRED STUB | 19-20, 35-36 |
| **S6** | **Morale shock from speed differential — absent.** No morale-hit term for cavalry shock. (Jordan A) | GAP | puncture block 1721-1734 |
| **S7** | **`_envelopment_sigma` retained but dormant (`PC_ENVELOP_SIGMA=0.0`)** — called (1745-46) but inert; flagged "do not add unneeded apparatus." Geometry path now carries envelopment → retirement candidate. | INTENTIONAL DORMANT (retire?) | 1353-1355, 1745-1746 |
| **S8** | Stale `_depth_by_col` mention in `_support_along_vector` docstring (code fully removed). | COSMETIC | 553 |
| **S9** | v14-deferred items (anti-wrap defensive, refused-stub repositioning, depth-ratio pool bonus) — several **SUPERSEDED** by the committed refusal/pocket/depth-resistance/roll-up. Reconcile: superseded vs still-open. | RECONCILE | 35-36, 71-72 |
| **S10** | over-run correction disabled (documented intentional, pre-pairs halting handles it). | INTENTIONAL (note only) | 910 |

Plus Class-B `[ASSUMPTION]` tuning flags (stamina, recovery, troop-speed-class mapping at 1037) — logged, Jordan-vetoable, not defects.

---

## PART 4 — RESUME WORKPLAN (sequenced from the audit)

Ordering insight: **S2 is a prerequisite — nothing speed-related is testable without cavalry matchups.** Each phase: bottom-up build → top-down validate (du Picq / Waterloo squares / Leuthen) → full-gauge incl. new cavalry matchups → toggle-off 120/120 → commit. All in `PER_CELL=1`; `PER_CELL=0` stays byte-exact.

- **Phase 0 (PREREQUISITE) — cavalry test coverage [S2].** Add Fast/cavalry matchups to the gauge: cav-vs-infantry-line (charge devastates), cav-vs-deep/braced (repelled), cav-vs-flank (shock). Historical bands. Until this lands, S1/S3/S4/S6 are unvalidatable.
- **Phase 1 — unify + wire canonical `Unit.speed` into combat [S1].** Make the combat speed-differential reference the canonical Slow/Standard/Fast tier (+ `troop_type`); collapse the two speed models into one.
- **Phase 2 — (B) vectorized + speed-scaled penetration [S4].** Replace `_defender_depth` in puncture with `_support_along_vector` along the charge vector; effective absorbing depth scales inversely with speed differential.
- **Phase 3 — (A) speed-differential morale shock, prepared-defense-gated [S6 + anchor].** New morale term: high speed-diff vs slow/stationary → defender morale hit; NEGATED by deep+disciplined+braced stance, AMPLIFIED by thin/flanked/disordered. Reconcile with existing `PC_CHARGE_SIGMA`/`PC_CHARGE_TICKS`.
- **Phase 4 — (C) verify facing→deals-less; wire explicit only if needed [S5, S3].** Empirically test the σ-head coupling strength; add the deferred bad-facing trigger + power×facing charge scaling only if insufficient.
- **Phase 5 — reconcile/retire [S7, S8, S9].** Mark v14-deferred items superseded by roll-up/pocket/refusal; decide `_envelopment_sigma` retirement; fix the docstring.

**Open design calls for Jordan (before Phase 3):** (1) morale-shock magnitude + exactly which defender states (stance? discipline floor? `MIN_DEPTH`?) negate vs amplify; (2) whether (C) stays emergent or gets an explicit attacker-output gate.
