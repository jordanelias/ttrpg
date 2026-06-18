# Combat — consolidated decision docket
### Two-week pile (06-03→06-17) reconciled to live HEAD · the thing that unsticks it

**2026-06-17 · status: PROPOSED working master · re-pinned to HEAD `15269f3c` (2026-06-17 19:32)**

`[SELF-AUTHORED — bias risk: synthesizes Claude-authored audit corpus + Claude's own reconciliation plan. Recommendations below are carried from the 06-16 reconciliation_plan, not new authority. Every "CLOSED" cite is a committed SHA or ledger ED read live this session.]`

`[READ: canon/editorial_ledger.jsonl (683 entries, tail) · canon/supersession_register.yaml · designs/audit/2026-06-16-combat-reconciliation/{combat_reconciliation_plan,stage1_validation} · designs/audit/2026-06-13-combat-bottomup/{README,representation_alternatives,classes_ability_library,research_skeleton} · designs/scene/combat_engine_v1/{tradition,core,systems,wrapper}.py · commits sha=main last 18]`

---

## §A — What CLOSED since your 06-11 corpus (the re-pin)

Your uploaded snapshot is from 06-11. The ledger has moved 653→**683** and HEAD is 60 hours ahead. A large share of what felt "stuck" actually landed in the last three days. This is the direct answer to "designs not getting wired in" — they have been, fast:

| Was "open" @06-11 | Now | Authority |
|---|---|---|
| Combat μ-shift / F4 `effective_ob` seam | **WIRED @ HEAD** | ED-934 · commit `15269f3c` (19:32 today) |
| `P_auth` (dead `pob_frac`/`mass` inputs) | **WIRED** (consumes them) | ED-934 · `15269f3c` |
| `atk_sig` → depleting Concentration | **WIRED** | `15269f3c` |
| F2 `eff_cw` channel wiring (channel-abilities inert) | **18/23 sites live** in `systems.py`; channel-abilities (misura/atajo/Stärke-Schwäche) now fire | ED-934 |
| J-2: 7 unregistered F2 Key types (the NERS **R-FAIL** driver) | **REGISTERED** + consumer-wired | ED-935/936/937 · `7b5edb11`/`acb61f07` |
| Orchestration v4 set (map/graph/workplan) — PROPOSED | **RATIFIED → CANON** | `d08b7a14` |
| 06-13 ability corpus + research skeleton (the 16 docs) | **LANDED in-repo** (committed PROVISIONAL) | `b05410c4`/`85e8d289` |
| Mass battle: cohesion pool, gauge, per-subunit stats | **WIRED** (active parallel session) | ED-1013/1014/1015/1016 |

**Supersession check result:** none of the two-week design docs are in `supersession_register.yaml`. The register's combat entries deprecate only the *pre-engine lineage* (`combat_v31/v32_proposal` → DEPRECATED by ED-900; `ners_verdict_combat_v32` record-retained; `combat_v30` PARTIAL, lore retained). The pile is **live-and-pending, not stale**. Within 06-13 the five ability-exploration variants converge into one `consolidated_master` (intra-session, by design — not register supersession).

**So the pile is not rotting. It is mid-consolidation, and Stage 1 already wired.** What remains is a *decision* backlog, not a wiring backlog — below.

---

## §B — The live open docket (your calls — ratify / modify / reject)

Ownership tags: `[BAL]` changes outcomes/feel, you ratify · `[CANON]` touches an authored/ratified value, yours alone · `[NEW]` unbuilt mechanism, you scope. Source = 06-16 reconciliation_plan §4 + stage1_validation DEFERRED + the 06-13 tradition thread + ledger ED-911. Mark each; I wire the accepted, retire the rest.

| # | Decision | Tag | Bottom-up basis | Prior recommendation | YOUR CALL |
|---|---|---|---|---|---|
| **D1** | Continuous weapon-vs-armour **transmission model** (`armour_axes`/`damage_model`) replaces `RESIST`/`DELIVERY`/`HEFT`/`ADEF` so mass/balance drive damage as a live gradient | `[BAL]` re-baseline | top-down inventory §2 #1/#2; `damage_model` calibrated to RATIFIED_TABLE | **yes, deliberate re-baseline w/ full re-validation** | ☐ ratify ☐ modify ☐ reject |
| **D2** | **Puncture mode** — poleaxe beak ≠ mace face through plate (`puncture_pressure = authority × strike_concentration`) | `[CANON]` | `combat_puncture` doc; `geometry.percussion_concentration` derived | yes, but refines an authored RATIFIED_TABLE row + needs an anchor that doesn't exist `[GAP: pick-vs-plate magnitude]` | ☐ ratify ☐ modify ☐ reject |
| **D3** | **Continuum degree + saturating quality** replaces the 4-band degree + `QUAL{.35/1.0/1.5}` (one change atop the μ-shift) | `[NEW]`/`[BAL]` | armature A5; top-down inventory #10 | **yes, paired with μ-shift** — matches "videogame, not d10 table" | ☐ ratify ☐ modify ☐ reject |
| **D4** | **Pool recompute** as composite (combat-experience / tradition / stamina / focus) instead of History-only | `[NEW]` | sigma_leverage_handoff §0; armature A6 | yes for richness, but it **re-scales σ-leverage** — must hold A6 parity; bring measured recal first | ☐ ratify ☐ modify ☐ reject |
| **D5** | **Disposition-as-selection** layer — disposition biases which maneuver/ability/skill is chosen & when (current 3 hooks measure NULL) | `[NEW]` | emergent reframe; gating-chain §1–2; your canon-intent | scope-then-build (genuinely unbuilt) | ☐ scope ☐ defer ☐ reject |
| **D6** | **Tradition representation**: keep the scalar channel-weight vector **vs** dissolve into abilities-primary (S3⊕S4: abilities = qualitative layer; channels → player-allocated *affinity budget* that gates abilities) | `[CANON]`/`[NEW]` | representation_alternatives (proves scalar can't both specialize & balance); eff_cw now live | recommends **S3⊕S4** — but note eff_cw is now wired, so re-decide with that in hand | ☐ keep ☐ S3⊕S4 ☐ modify |
| **D7** | **Ability schema extension** (`trigger`/`cost`/`prereq`) + adopt the ~55-ability library as the composable layer | `[NEW]`/`[BAL]` | classes_ability_library §1–3 | adopt schema (invariant-safe defaults); library is content you curate/reskin | ☐ ratify ☐ modify ☐ reject |
| **D8** | **Tradition coverage / new traditions** — priority-gap schools (Polish/Hungarian/etc.) stay ability-less until an S1/S2 anchor; the urumi candidate would add a **rigidity axis** (flexible blade, guard-bypass, area-denial, self-risk) | `[CANON]` (your world) | research_skeleton §4 (urumi, T2/T3, `[CONFIDENCE: medium]`) | author or not — yours; nothing canon until you say | ☐ author ☐ park ☐ reject |
| **D9** | **ED-911 (open in ledger)**: ranged / group / thread-in-combat have **no engine resolution** today | `[CANON]`/`[NEW]` | ledger ED-911 (P1 supersession-scope gap) | scope a resolution path or declare out-of-scope | ☐ scope ☐ defer ☐ out-of-scope |

---

## §C — `[MECH]` residuals I can wire now (no decision needed — just a go)

These reproduce/correct toward canon or finish in-flight wiring. Logged, vetoable, each re-validated against the parity anchors (longsword mirror .481; wound-handicap .490/.329/.215).

| # | Task | Basis | State |
|---|---|---|---|
| **M1** | Finish `eff_cw` routing — **5 residual `channel_weight` sites in `wrapper.py`** still bypass abilities (systems.py is done, 18/18) | grep @ HEAD: `wrapper.py channel_weight×5` | ready |
| **M2** | Drop the dead `POOL_FLOOR` branch (`History≥1 ⇒ pool≥7>5`; floor never binds — cosmetic) | derived_stats_audit §1; stage1_validation DEFERRED | ready |
| **M3** | Dead `seize` lever — `vorschlag`/`sen_no_sen` point at the cut lever, empirically baseline-dead → repoint to a live lever **or** retire (the retire-vs-repoint is a micro-`[CANON]` ability call) | `systems.py:242` seize cut 2026-06-05; ability sweep | needs micro-call |
| **M4** | Wound-sweep re-confirm — the Class-A `−1D` wasn't re-measured under the μ-shift `[GAP]` | stage1_validation honesty block | ready |

---

## §D — Untouched (canon / sound — not on the table)

The `−1D`-per-wound penalty (Class-A, derived_stats §4.1 / PP-717) · `RATIFIED_TABLE` (the weapon-vs-armour anchor) · the authored `TRADITIONS`/`ABILITIES`/`FAMILIARITY` cognitive-mode content · `UPSET_FLOOR` 0.05 (the 95% videogame cap) · the ~100 Class-C `config` coefficients · the world / characters / metaphysics / HEMA texture / naming (project-owner contract).

## §E — Parked observations (no action unless you want it)

- **Read-dominance:** Cog/History out-driving physical stats is an A6 *balance tune*, not a defect. Stage-1 re-validation showed the μ-shift **compressed** spans (att +80→+66, focus +30→+15), the opposite of the feared widening.
- **F5-A wound enrichment:** adding wound→stamina/concentration channels — recommend **not**; the `−1D` is already sufficient and uniform.

## §F — Honesty

- `[CONFIDENCE: high]` on §A closures (committed SHAs + ledger EDs read live) and the engine-state grep (eff_cw 18/0 systems, 5 channel_weight wrapper, 7 resolve markers core).
- `[CONFIDENCE: medium]` on D6/D7/D8 framing — PROPOSED self-authored layer; D8's urumi rests on T2/T3 sources pending a T0/T1 pass.
- `[GAP: pick-vs-plate magnitude (D2)]` — validated ranking, not a calibrated number; no ratified anchor.
- `[ASSUMPTION: 06-06 weapon-physics-ners + 06-09 comprehensive banners not opened this session — basis: their decision content is subsumed by the 06-16 reconciliation_plan's directive map, which read and operationalized them; flagged rather than claimed.]`
- Re-pin caveats: roadmap_state 8 days stale; 20 canonical sources flagged stale by freshness_gate; the parallel mass-battle session is committing live (HEAD moved 4× in 30 min) — D-items here are personal-combat, write-disjoint from `tests/sim/mass_battle/**`.
- Nothing here is committed. The canon engine is unchanged beyond what HEAD already holds.
