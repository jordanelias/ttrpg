# Valoria — Master Workplan v4 (orchestrated, three-lane, single register)
**2026-06-11 · status: CANON — ratified 2026-06-12 (Jordan); the active master, supersedes v3 (§3 remains the live decision docket — open J-keys await rulings; the document itself is no longer provisional)**
**as_of: the 2026-06-11 upload corpus (latest cited commits `c8e982b5` contracts / `6199d83a`·`c005da27` game-flow / `ac49cea6` workplan-v3). Verified at commit against live HEAD `d010fe27`: editorial ledger 653 entries / 0 duplicate IDs confirmed; the v2 source layer confirmed committed. The two §0 value flags (CI 22v28; MS-start) remain OPEN — not resolved this session.**

**Supersedes (on commit):** `designs/audit/2026-06-10-master-workplan-v3/valoria_master_workplan_v3.md` — its frame, lanes, and approved carries are retained; its docket is extended and de-staled below. Banner discipline per the v3→v2 precedent; v3 stays the frozen 06-10 record, J-1…J-18 IDs stay citable and are NOT renumbered.
**Binds (does not fork):** `valoria_authoritative_map_v1.md` + `valoria_authoritative_graph_v1.md` (this orchestration's companion views) · the conversion strategy (`b42aa03`, Lane C spec) · interdependency master v1 (v2-corrected) + atlas v1 · canon flatten v2 · the per-system analysis set · `references/module_contracts.yaml` (the generated spine).

`[SELF-AUTHORED — bias risk: every consolidated input is Claude-authored across 06-06→06-11 sessions. Counterweights carried: verdict §7 (registry-shadow over-claim), atlas §7/§7-bis (R1–R8, P1–P5), flatten v2 §0.5 (one P1 reversed). This consolidation applies their corrections rather than re-asserting the originals.]`

---

## §0 — RECONCILIATION RECORD (per-source scan; corrections applied with citations)

| Source | Verdict | Correction applied in v4 |
|---|---|---|
| **Workplan v3** (06-10) | Sound frame; four staleness points | (a) A6 counts restated **8 cross-band seams / 15 type-edges** (19 = raw assessor count incl. one near-lateral) per atlas R4/P1; (b) ED attribution corrected — the top-down gap and naming items cite **ED-1009** (adjudication verdict), not ED-1006 (extraction) per atlas P2; (c) the **combat engine-v1 residual restored to the docket** (J-33) — v3 §0 correctly struck "combat-v32 ratify" (proposal lineage dead) but dropped the live engine-v1 residual (3 post-ED-904 commits + coverage ruling) that remained a handoff blocker and roadmap Gate 3; (d) the **stale ★P1 ID-conflict blocker struck** per the roadmap's CORRECTED banner (below). |
| **Roadmap 06-09** | Authoritative for the ★P1 strike + lane state; stale in spots | **Ledger: 639 entries / 0 duplicate IDs verified 06-09; 653 entries read 06-11 (flatten v2); **re-confirmed live at HEAD d010fe27: 653 entries, 0 duplicate IDs, ED ceiling 1012.** The ID-conflict adjudication gate is RESOLVED.** 06-10/06-11 artifacts still carrying "ID-conflict backlog" language (v3 §0 item-2 ledger column; master §8 OPEN note; atlas P2 motivation clause) are corrected here. Retained on its own merits: ED citations are **ledger-verified, never memory-sourced** — atlas P2 proved the failure mode on a clean ledger. Roadmap staleness: B.1's "on ratify → 3 commits" already executed (deprecation map: combat_v30 PARTIAL banner 06-04; `params/combat.md` → `deprecated/` 06-04; register entries 06-10); roadmap regen rides LB-3/K-1. |
| **Interdependency master v1 (v2) + atlas v1** (06-11) | The graph layer of record | Carried with their own fixes: loop-safety + NERS verdicts are **INHERITED from source audits, not re-derived** (R2); contract-/module_map-derived rows are **secondary** to the primary-canon spine; 4 of 6 stale canonical sources are load-bearing — live reads outrank stale pins (R7). J-19/20/21 (introduced by the master) formalized below. |
| **Canon flatten v2** (06-11) | The canon-side register of record | **C2 REVERSED honored:** PP-675 is a terminology workplan; no ratification store strikes the 218 AG backstory; **canon/03 stands — do NOT edit it.** J-23 frames the genuine open question (default: backstory IN). C14e withdrawn (M-series = vetting framework). C1/C3–C13 + C14r docketed below. |
| **Game-flow v2 (analysis + flat-spec)** (06-11) | The temporal spec of record | Adopted: Accord/Strain/battle accounting at **Step 6** (ED-678; F12), not Step 4; CI uncontested Seizure window **≈ S16** (AR-1 — Piety Yield ≈0 at seed), not S11; F10 resolution direction (Stability −1 dominant; victory §7 outlier); F1 narrowed per F13; F11/F14 registered. |
| **Per-system set** (threadwork ×7 · social contest ×2 · faction ×4 · settlement ×3 · combat ×2 · mass battle ×3 · fieldwork) | Live system-depth | Their consolidated Jordan sections restored to the docket as one-sitting items (J-31/J-32/J-33) or confirmed already covered (J-9/J-10/J-18/LA-1). Staged ledger candidates (ED-911, ED-970/971, faction §8 set) file via lane-block discipline at next lane entry — the staging-only counsel is struck with the ★P1. |
| **Deprecation map + supersession register** (06-10) | Live enforcement companions | Residual wired in: LB-19 (bootstrap fetch-set), LB-13 carry (proposal `git mv`). |

**Two unresolved value flags surfaced by cross-reading (verify at bootstrap; do not silently pick):**
- **Seed CI: 22 vs 28.** canon/03 carries an explicit Conflicts-Resolved row ("Earlier: CI 0 or CI 15 → CI 22") — flatten C5(i) rates it the stronger authority — while `canonical_registry` §1.1 and the entire 06-11 mechanics corpus (init seed, metronome, S16 derivation) use **28**. J-24 sub-decision; on "22" the uncontested Seizure window shifts ≈3 seasons later (~S19). `[UNVERIFIED at live HEAD]`
- **MS start referent: 72 vs "80→60".** canon/03 / ms_trajectory / game-flow seed all say **MS 72** at 245 AG; roadmap B.4 + v3 §7 record a victory-stream commit (`2edf6432`) as "Mending Stability start 80→60" — whether that 60 is the campaign seed or a victory-condition threshold is not determinable from the corpus. `[GAP: referent of the 60 — check 2edf6432 at bootstrap; assign to LB-3]`

---

## §1 — OPERATING MODEL (carried unchanged from v3)
Three write-disjoint lanes per `references/lane_assignments.yaml` (owns-globs, reserved ED/PP blocks — A: 890–939 · B: 940–969 · C: 970–999 — launch protocol, boundary rule). One operator; sessions are the currency; **Lane B WIP = 1**; rituals ride with feature work; **budget rule** — no new structural proposal advances while K-1/K-2/K-3 are unbuilt; hooks detect · the model interprets · Jordan decides. The Decision Docket (§3) is not a lane; every lane parks against it (launch-protocol step 7). Consolidation sessions (like the one producing this) operate under the sole master handoff, outside lane declaration.

---

## §2 — UNIFIED OPEN REGISTER (single de-duplicated surface; verdict-first, worst-first)

**Verdict: unchanged from the master and strengthened by the intensification pass — the architecture is sound and the loop layer is safe (inherited verdicts, sims cited not re-run); closure is blocked by structural decisions that are Jordan's plus a propagation-debt layer, not by runaway dynamics.** Safety set that PASSES: A7 (no undamped+unbounded cycle), A5 (0 derived-write violations), A1 (stubs empty), J1 bucket fitness (examined-null).

| # | Defect / decision | Sev | Sources (corpus) | Owner |
|---|---|---|---|---|
| 1 | **Top-down Key delivery** — engine already delivers **and applies** down (`key_substrate §4.1` step 4 + scale-agnostic `§4.2`); the gap is **target-population** (strategic `da.*`/`env.*` Keys carry faction/territory targets, no personal ones) + no `scale_transitions §3` rule. **8 cross-band seams / 15 type-edges** (19 raw). Blocks Wave-S/4 specs. | P2/P3 contingent | atlas §2.4/§5.4/P3; master item 1; verdict §4; ED-1009 | **J-1** |
| 2 | **Faction-stat inversion / write-path** — Mandate derived (LPS-2e); Domain/Debate/Thread Echo text still writes ±Mandate directly (R4 violation in canon text, atlas §5.5); inversion decides every Wave-2 write-path. | **P1** | master item 2; atlas §5.5; consolidation master Part A | **J-7** (+J-8) |
| 3 | **7 unregistered emitted Key types** + no combat `scene_outcome` subtype + `battle_concluded` naming drift — an internal contradiction in the canonical substrate pair (`key_substrate §8.4/§8.6` declare types its own registry omits; `validate()` rejects). | P2 | atlas §3/§5.2-3; master items 3–4; ED-1006/1007/1009 | **J-2** → LA-2 |
| 4 | **11/27 shadow modules** (registry-derived, no home doc) — honest split ≈14 specified + 11 shadow + 2 stubs. | P2 | verdict §3/§7.1; ED-1006/1009 | **J-4** → LA-3 |
| 5 | **Duplicate-module pair** — `settlement_economy` vs `settlement_layer §1.3`; `faction_politics` vs `faction_state`. | P2 | verdict §5-N; ED-1009 | **J-5** |
| 6 | **3-way piety/conviction collision + CI-clock/Influence-stat overload** — confirmed at the primitive (registry/substrate canon names vs contract impl names). | P2 | atlas §0/§5.1; master item 7; ED-1009 | **J-2/J-4** → LA-4; cluster J-30 |
| 7 | **GD-1 victory threshold: 11+ vs all-15** — canon/02 + mechanics_index vs victory_v30 §0+§11 (byte-confirmed twice); a 12-territory hold wins under canon/02 and not under victory_v30. Gates victory finalization. | **P1** | flatten C1 (SURVIVES-STRENGTHENED) | **J-22** → gates J-11/LC-7 |
| 8 | **218 AG backstory: in or out** — the C2 REVERSAL. Strike ratified by neither store; the chains banner mis-cites PP-675; canon/03 stands and is likely correct. Default: IN. After ruling: fix the banner's citation; if OUT, then (and only then) propagate to canon/03 + E-01. | **P1-class decision** | flatten C2 (REVERSED) | **J-23** |
| 9 | **canonical_registry drift** (≥7 values; renames adopted by zero docs; struck PI/RDT still live downstream) incl. the **seed-CI 22-vs-28** sub-decision (§0 flag). Re-ratify or demote the "Definitive" header. | **P1** | flatten C5; §0 flag | **J-24** |
| 10 | **arcs 28–30 fail canon/01 Amendment 5** (no TS-at-failure, no reality-strain; single Resonant-band outcome) — the one CP14 file canon binds. Regeneration is creative-tier. | **P1** | flatten C6 (byte-confirmed both sides) | **J-25** → LA-21 (Jordan-led) |
| 11 | **Vaynard identity bifurcation** — conqueror canon (ratified, CR-STRIKE) vs un-struck scholar-collector arc layer; the Jordan-ordered rewrite (2026-04-19) has not landed. | **P1** | flatten C7 (strike ratified) | LA-22 (Jordan-led) + interim banners |
| 12 | **Niflhel strike residue** — incl. the NEW intra-doc contradiction inside live `settlement_layer_v30` (§4.7 replacement + still-live Niflhel governance row). Mostly mechanical re-skins; two rows are Jordan's (canon/03 faction table; Viability Matrix). | **P1** | flatten C8 (STRENGTHENED) | LA-13 + **J-26** |
| 13 | **World-track fracture** — one track, four names (TT/RS/MS/Metaphysical; F11 adds `faction_layer §7` "RS" vs four docs "MS"); one doc with **inverted TT arithmetic**; `rs_track`/`ms_track` duplicate index pair. | **P1** | flatten C3; flat-spec F11; master item 11 | **J-21** → LA-11 sweep |
| 14 | **Rename-note self-clobbering** ("X (X)" pattern, ≥5 sites; TC/CT/RWCE old names erased) — byte-confirmed. | **P1** | flatten C4 | LA-12 + LB-20 hook |
| 15 | **Social contest record** — 3 P1 contradictions (Appraise struck-rule in doc; strain ×3 ambiguity; PP-351 in three incompatible forms); **repair already ratified** (CR1–CR7 + groundup engine 151/151) but unpropagated. **(ED-884 mu-shift / F1 since landed — ED-1037, `060f0838`; CR1–CR7 propagation still LA-19; 06-18 sim/audit residual → reg #33.)** | **P1** | ANALYSIS §0/§4 | **J-31** → LA-19 |
| 16 | **Threadwork record-S FAIL** — 5 unpropagated rulings, dead scale taxonomy in the live body, 3 forks; N14 inbound-drift is a structural gap (mechanic exists nowhere). Design itself NERS-compliant. | **P1** | threadwork master §1/§8; all-directions §3 | **J-32** → LA-20 |
| 17 | **Personal combat residual** — engine CANONICAL (ED-900–904) but: 3 post-ED-904 unratified commits (incl. `deb405b944` wound −1D, −18pp first wound); **F1 coverage gap** (ranged/group/thread live only in superseded combat_v30 layer; ED-911 staged); F2 tradition imbalance + dead abilities; F3/F4 doc↔engine seams. | **P1** (F1) | combat analysis VERDICT/F1–F7 | **J-33** (D-α…δ parallel-owned — coordinate) |
| 18 | **Mass battle** — COMPLIANT-WITH-BACKLOG; debt = tri-strata doc drift (ED-899 FOLLOW-UP) + F1 (ED-800 implemented nowhere) + F2 (ED-910 control surface absent) + band/CAP/discipline set; ED-970/971 staged. | P2 | massbattle analysis §0/§7; ners verdict | **J-9** → LA-8 + LC-8 |
| 19 | **Settlement port-gating** — GD-2 always-fires + Order→Accord clamp unstated (**J-19**) and the §V quartet: intra-Accounting order, base Order-decay rate, stat-damage substrate PENDING, Fortress-City Weight 2v3 (**J-34**). Both gate the recommended first port. | P2 | flat-spec C2.1/A2.2; settlement §V | **J-19 + J-34** → gate LC-3 |
| 20 | **Fieldwork** — P1 canonical-line split (Disposition triple-divergence; Thread-Read stat) gates Lane-C module 20; §11 five pending decisions. | **P1** | `a11e2fa` diagnostic; v3 LA-1/J-18 | LA-1 + **J-18** |
| 21 | **Faction propagation debt** — 7 P2s (ratified ED-787/869/874/876/LPS-2 not propagated across sibling docs) + 8 P3s. | P2 | faction analysis §6 | LA-17 |
| 22 | **Value-taxonomy drift** — Composure ×3 vs +6 (the open name/formula call) + Stamina/Concentration/Combat-pool/Intel consumer+manifest staleness (R8: needs a real docket home, LA-5 is index-regen only). | P2/P3 | master item 10; atlas R8 | **J-12** + LA-18 |
| 23 | **Pre-pivot residue** — shared-loss text, "all 15" echoes, ×3 MS multiplier, stale CI start mentions, scene-count drift, "GM" references (F14; `params/scale_transitions` v0.14 wholesale). Propagation of decided canon, not new decisions. | P3 | master item 11; flat-spec F14; atlas §5.6 | LA-11 |
| 24 | **Assert/Suppress failure penalty** — Stability −1 (×3 in faction_layer) vs Discipline −15 (victory §7 lone outlier, not derivable). Direction resolved; correction Jordan-vetoable. | P3 | flat-spec §H/F10 | **J-20** |
| 25 | **Klapp dual-state** (she/TS8/Temperance vs he/TS31/CE) + Voss/Vorn/Kald alias residue; **Lenneth archive date** three ways (load-bearing lore). Character canon = creative tier. | P2 | flatten C10/C11c | **J-27 / J-28** + LA-16 |
| 26 | **CI threshold tri-scheme** (clocks.md 30/50/70–74 · registry 40/55/65/80/100 · CI-75/ED-110) + >74 bands unauthored. | P2 | flatten C12 | **J-29** |
| 27 | **Naming batch** — IP expansion (3 ways) · Strain/Turmoil/Political-Stability tri-name · PT name (ED-302) · calendar (E-03) · **Halvardshelm/Halvarshelm T11-vs-T17** (C14r). One sitting. | P2/P3 | flatten C13/C14g/C14r; §7.2 | **J-30** |
| 28 | **Hygiene set** — C14a status-integrity, C14b README misplacement, C14c clocks.md duplication, C9 dangling autonomy path + Coup-Counter table migration, C11 a/b/d date arithmetic, C14m/n/p/q sites; orphan types + MS-no-owning-module + 37-vs-38 + `scene.gossip` yaml + stale indices. | P3 | flatten C9/C11/C14; atlas §5.7 | LA-14/15/16 + LA-5 + LB-5 |
| 29 | **ED-935 inferred Key payloads** — `scene.thread_operation` / `scene.draft_da` / `scene.displacement` / `scene.combat_resolved` payloads inferred (not canon-specified), registered provisionally per J-2 register-all; pending Jordan payload ratification. Stubs at key_type_registry entries. | P3 | ED-935; key_type_registry §2/§7 | Lane A / Jordan |
| 30 | **ED-936 consumer effect magnitudes** — scene_outcome→Procedure D opinion-drift magnitude/curve, combat_resolved Tier-2 default, scene_outcome→faction Echo routing authored under delegated grant; effect sizes unspecified, pending Jordan tuning. Stub at doc-12 §5.4. | P3 | ED-936; political_dynamics_keys_migration §5.4 | Lane A / Jordan |
| 31 | **ED-937/PR-1 Lane-B propagation** — battle_concluded naming fixed at substrate §8.5; residual: `module_contracts.yaml` L446 drift-form + stale `[unreg]`/`NOT in registry` comments (L130-133/268/467/816, now registered ED-935) + `module_map_flat.md` regen. | P3 | ED-937; module_contracts.yaml | Lane B (LB-5) |
| 32 | **ED-937/PR-3 belief_revised under-attribution** — registry `emitting_systems=[fieldwork]`; npc_behavior §3 belief revision may also emit `state.belief_revised` — verify; if so add npc_behavior. | P3 | ED-937; key_type_registry §8; npc_behavior §3 | Lane A / Jordan |
| 33 | **Social-contest sim/audit residual (2026-06-18)** — ED-884 mu-shift now propagated to the contest engine (commit `060f0838`, **ED-1037**); F1 leverage-non-uniformity = the ED-1009 module-13 R-defect **CLOSED** (z-shift uniform; 151/151; venue dists stable). **Open:** Indirect orientation has **no track-movement path** (**ED-1033**, intent UNDETERMINED — denial/tempo role vs a track lever); L3 venue **policy-dominance / legibility** (**ED-1036**, worst-policy 0.00 every venue → Godot venue→rhetorical-fit affordance); **excommunication venue** — keep bar 3.0 + ship §7.3 lifecycle **vs** soften to 2.5 (**D-5(b)**; the mu-shift already lifted +4-faculty overturn 0.54→0.72, so the directive's aim is met without a bar change). Doc/code drift (ED-1034) + recoverability-rule-as-principle (ED-1035) resolved this session. | P2/P3 | sim_audit 2026-06-18 §9–§11; ED-1033–1037 | **J-31** (+ Lane C when the affordance is specced) |

`[NULL: new P1 classes beyond rows 1–17 — the unified read of all five graph views + canon flatten v2 + per-system set surfaced no additional P1; the additions over the master's register are the canon-side items (7–14, 25–27) and the restored combat residual (17), all already present in their source documents.]`

---

## §2b — STUB RESUMPTION SPECS (expanded detail for register rows #29-#32; the inline `[STUB]` markers in canon point here)

**#29 — ED-935 inferred Key payloads.** *Pending:* required/optional payload field sets for `scene.thread_operation`, `scene.draft_da`, `scene.displacement`, `scene.combat_resolved` are inferred (substrate §8.4/§8.6 + sibling mirror), not Jordan-authored. *Needs, per type:* **thread_operation** — confirm `[operation, operator_id]` + optional `[target_thread, operation_scale]` against the threadwork op vocabulary; **draft_da** — confirm `[action_type, actor_id]`+`[target_id]`, or rule it telemetry-only (no payload beyond a ref); **displacement** — confirm `[observer_id, displaced_relation]`+`[displaced_by, neglect_context]` against doc-12 `displacement_neglect_observed`; **combat_resolved** — confirm `[scene_id, outcome, participants]`+`[casualties, wounds_inflicted]`, the `outcome` enum (attacker_win/defender_win/draw/rout/withdrawal), and emitter name (`personal_combat` vs `combat_engine`). *Closes when:* Jordan ratifies/edits each; the 4 registry `[STUB]`s flipped. *Owner:* Jordan ratify / Lane A apply.

**#30 — ED-936 consumer effect magnitudes.** *Pending:* the authored consumer wiring (ED-936) has unspecified effect sizes. *Needs:* (a) scene_outcome -> Procedure D opinion-drift **magnitude + curve** (how far opinion of each participant shifts, by outcome severity x observer relationship) — currently "drifts" with no number; (b) confirm `combat_resolved` -> articulation **Tier-2** is the right significance (vs Tier-1/3); (c) confirm scene_outcome -> faction reuses the existing **Domain Echo cap (+/-2 per stat)** rather than a new bound. *Closes when:* Jordan sets drift magnitude/curve (or delegates a grounded value) and confirms (b)/(c); doc-12 §5.4 `[STUB]` flipped. *Owner:* Jordan tune / Lane A apply.

**#31 — ED-937/PR-1 Lane-B propagation.** *Pending:* battle_concluded naming fixed at the substrate source only. *Needs:* in `references/module_contracts.yaml` — resolve L446 `scene_outcome.battle_concluded` (align to / strike in favour of L447 `scene.battle_concluded`); update the now-false `[unreg]`/`NOT in registry` comments at L130-133/268/467/816 to "registered ED-935"; then regenerate `module_map_flat.md` (+ the 2 mermaids) so the type matrix shows 44 types and the correct battle name. *Closes when:* no `scene_outcome.battle_concluded` remains; module_map regenerated @44 types; comments accurate. *Owner:* Lane B (LB-5 regen; references/ is Lane-B).

**#32 — ED-937/PR-3 belief_revised under-attribution.** *Pending:* registry `state.belief_revised` `emitting_systems=[fieldwork]`. *Needs:* read `npc_behavior §3` (belief formation/revision) to determine whether it emits `state.belief_revised`. If yes -> add `npc_behavior` to `emitting_systems`; if belief changes route via `state.opinion_revised`/another type -> confirm `[fieldwork]` sole and close. *Closes when:* npc_behavior §3 checked; registry corrected if needed; registry `[STUB]` flipped. *Owner:* Lane A verify / Jordan confirm if structural.

## §3 — DECISION DOCKET (Jordan-gated; J-keys stable — J-1…J-18 carried, J-19…J-21 formalized, J-22+ new; ordered by unblock leverage within tiers)

**Tier 1 — highest unblock count (rule these first):**
| ID | Decision | Unblocks |
|---|---|---|
| **J-2** | Registry §10 type set: 7 F2 register-or-strike (incl. doc-12 §8 / substrate §8.4–8.6 side), F3 `scene.combat_resolved`, `battle_concluded` naming, `draft_da` strike, `belief_revised`/`scene.dialogue` attribution | LA-2 → every dice-engine port (LC-4) |
| **J-1** | Top-down delivery: **(a)** declare engine-mediated delivery canonical + A6-exempt (assessor carve-out + tests; **strengthened** — §4.1/§4.2 already deliver+apply; option adds authoring discipline: strategic emitters populate personal targets where intended, + §3 documentation) **or (b)** author an explicit §3 down-rule | 8 seams' status; assessor fix (LB); `scale_transitions` edit (LA); strategy flag (LC); Wave-S/4 specs |
| **J-22** | **GD-1 number: 11+ or all-15** | victory finalization (J-11 → LC-7); canon/02 ↔ victory_v30 ↔ mechanics_index one-commit propagation |
| **J-6** | Lane-C starters: (a) autoload ruling (b) first module (settlement_layer recommended — now explicitly gated J-19+J-34) (c) Python-corpus end-state (d) Key runtime form (on K8) | LC-0a · LC-3 · LC-6 · LC-0d |
| **J-23** | **218 AG backstory in/out** (default IN; canon/03 stands) | timeline certainty (most-fetched canon file); chains-banner citation fix; E-01 disposition |

**Tier 2 — system gates:**
| ID | Decision | Unblocks |
|---|---|---|
| **J-7** (+**J-8**) | Faction-stat inversion + DECIDE-1/2 + Intel + CI/Influence naming; Mandate-echo routing/calibration | LA-6 migration; faction_state write-side port; Echo R4 fix |
| **J-31** | Social-contest sitting: ANALYSIS §5 D-1…D-10 (strain math D-2, PP-351 D-3, CR1–CR7 propagation order, L3 commit) **+ 06-18 residual (reg #33): Indirect intent (ED-1033 — denial role vs track lever), venue policy-legibility (ED-1036), excommunication keep-3.0+§7.3-lifecycle vs soften-2.5 (D-5(b)); ED-884 mu-shift already landed (ED-1037)** | LA-19; module 13 port confidence |
| **J-32** | Threadwork sitting: master-analysis §6 docket (one sitting; incl. N14 inbound-drift ruling, fork picks, taxonomy re-key) | LA-20 → record-S to PARTIAL; module 21 port |
| **J-33** | Combat residual: ratify/reject the 3 post-ED-904 commits (wound-wiring intent rides `deb405b944`); F1 coverage ruling (ED-911 staged — engine-extend vs retain-combat_v30-layer vs descope); F2 tradition direction. D-α…δ parallel-owned — coordinate, don't claim | module 16 completion; handoff blocker clears |
| **J-9 / J-10** | Mass-battle set (bands H3/H4, per-cell CAP, ED-910, ED-909, discipline 4-role) / weapon-physics S2 constants (+ error params, defender-wound, draw-rate, P3 calibrate-or-cut) | LA-8 + LC-8 |
| **J-19 + J-34** | Settlement sitting: GD-2 intent + Order→Accord clamp; intra-Accounting order, base Order-decay, stat-damage substrate, Fortress-City Weight | LC-3 first port |
| **J-24** | canonical_registry: re-ratify or demote (**incl. seed-CI 22-vs-28**; Accord 0–3 vs 0–4; PT 0–5 vs 0–4; TV range; rename table; PI/RDT strikes) | the "Definitive" instrument stops poisoning reads; metronome re-derivation if 22 |
| **J-4 / J-5** | Shadow-module status (docs vs `registry_derived`) / duplicate-pair fold-vs-distinct | LA-3; Wave-2 modules 14/15 |
| **J-11** | Victory: treaty wiring go + territory fallback (after J-22) | LC-7 |

**Tier 3 — naming, canon hygiene, carried:**
| ID | Decision |
|---|---|
| **J-21** | World-track canonical name + authorize the TT-arithmetic inversion sweep + merge `rs_track`/`ms_track` |
| **J-30** | Naming batch (one sitting): IP expansion · Strain tri-name · PT (ED-302) · calendar (E-03) · Halvardshelm/Halvarshelm |
| **J-25** | Commission arcs 28–30 regeneration (creative-tier; TS-banded taxonomy + TS-at-failure + strain per branch) |
| **J-26** | Niflhel Jordan pair: canon/03 faction-stat row · Viability-Matrix row |
| **J-27 / J-28** | Klapp canonical state (arc_expansion version recommended) / Lenneth archive date |
| **J-29** | CI threshold scheme pick + author >74 bands |
| **J-20** | Assert/Suppress penalty — confirm Stability −1 (recorded dominant); victory §7 correction |
| **J-3 / J-12…J-18** | Carried verbatim from v3: D-3 boundary rulings · Composure name · ED-868 collapse bound · D6 scope-set · Resonant Styles · filename versioning · classification trio · fieldwork §11 five |

**Docket cadence is Jordan's.** Highest-leverage first ruling by unblock count: **J-2 → J-1 → J-22 → J-6(a,b) → J-23**; the three one-sitting batches (J-31, J-32, J-30) clear nine register rows in three sittings.

---

## §4 — LANE A QUEUE (Canon / Editorial / Design-content)

| ID | Item | Gate |
|---|---|---|
| LA-1 | Fieldwork P1 canonical-line split (carried; gates Lane-C module 20) | — |
| LA-2…LA-10 | Carried from v3 unchanged (registry executions J-2; shadow docs J-4; naming exec; stale-index regens + `scene.gossip` yaml; faction write-migration J-7; martial-traditions coordinate; mass-battle canon J-9; voice-canon closeout J-3; fieldwork §11 J-18) | per v3 |
| LA-11 | **Pre-pivot residue sweep** (register row 23 list + F14 GM-refs + `params/scale_transitions` reframe) — four-name half gated | J-21 (that half) |
| LA-12 | **Rename-note archaeology** — restore TC/CT/RWCE inside the rename notes from git history / atom slugs (mechanical-tier, logged, vetoable) | — |
| LA-13 | **Niflhel propagation sweep** keyed off the supersession register — incl. the settlement_layer intra-doc row; broker/black-market re-skins per the already-specified successors | J-26 (two rows only) |
| LA-14 | Coup-Counter → graduated-autonomy migration (throughline §4 tables onto Loyal/Restless/Autonomous/Split); fix the dangling `params/clocks/clock_registry_v30.md` path; `[ASSUMPTION: autonomy spec home = params/bg/clocks.md — natural clock-spec home; Jordan-vetoable]` | — |
| LA-15 | Timeline arithmetic fixes C11 a/b/d (mechanical, logged); C11c rides J-28 | — |
| LA-16 | Canon-hygiene batch: C14a status headers · C14b README relocation · C14c clocks.md de-dup · Voss/Vorn/Kald alias sweep · C14m/n/p/q sites | — |
| LA-17 | **Faction propagation-debt sweep** (the 7 P2s: ED-787/869/874/876/LPS-2 residuals across sibling docs) | — |
| LA-18 | **Derived-value formula propagation** (R8's gap): Stamina/Concentration/Combat-pool/Intel — consumers + manifest in the same commit (R7 rule) | — |
| LA-19 | Social-contest CR1–CR7 propagation + groundup-engine L3 commit, in the order J-31 fixes | J-31 |
| LA-20 | Threadwork reconciliation: the purely-propagation P1 executes now; the docket-gated remainder after the sitting | (half) J-32 |
| LA-21 | arcs 28–30 regeneration — **Jordan-led** (creative tier); Claude drafts only on commission | J-25 |
| LA-22 | Vaynard rewrite execution — **Jordan-led** (creative tier; already ordered 2026-04-19); interim banners on chains Arc 9 + arc_expansion Vaynard arcs are mechanical and ungated | — (banners) |

## §5 — LANE B QUEUE (Infrastructure · WIP = 1)

LB-1…LB-18 **carried from v3 with status notes:** LB-5 (adjudicator v3-basis re-run) now also closes the 8/15-vs-19 presentation, the §9 37-vs-38 count, and the 56-vs-58 derived-view drift in one regen · LB-8 (M4 soft-warn) verified still unbuilt · LB-11 (ED-867 markers) is the ★P1's only true residual · LB-16/17/18 stay behind the K-budget.

| ID | New item | Gate |
|---|---|---|
| LB-19 | Wire `canon/supersession_register.yaml` into the bootstrap fetch set (deprecation-map residual; one-line; **propose, don't self-commit** — hook/arch text is Jordan-applied) | K-budget |
| LB-20 | Hook candidate: pre-commit regex for rename self-clobbering — `X (X)` and `renamed from X … X` patterns (C4 class) | K-budget |

## §6 — LANE C QUEUE (Simulation / Godot)

LC-0a…LC-8 **carried from v3** with these annotations: **LC-0b** gate = J-2 (set restated per ED-1009/1007) · **LC-3** (first ritual, settlement_layer recommended) now explicitly gated **J-19 + J-34** alongside J-6b; its golden scenario keeps the Mandate↔L/PS §1.8 damper property-check (ED-1008) · **LC-7** gated **J-22 then J-11** · **LC-8** unchanged (J-9/J-10) · **LC-5** (OWN-5 cascade sim-verify) ungated, anytime. Interim rule for downward edges (strategy IV.2) stays in force until J-1; every down-edge a port touches gets flagged.

---

## §7 — DONE-REGISTER DELTA (06-10 → 06-11; excluded from queues)

The intensification pass: canon flatten **v2** (adversarial reconciliation; C2 reversed, C14e withdrawn, C1/C8 strengthened, C14r found) · game-flow **v2** (flat-spec §H adversarial review; F11–F14; Step-6 + CI-window + GD-1-hegemony-treaty corrections; full trigger/Parliament/collapse tables resolved from raw `faction_layer`) · interdependency **master v1 (v2-corrected)** + **atlas v1** (primitive-grounded edge atlas; R1–R8 + P1–P5; §4 faction multipliers + Mandate/Accord block live-verified exact; ED-1006→ED-1009 re-attribution) · this orchestration (map + graph + workplan v4). Everything in v3 §7 stands.

## §8 — CARRIED SETS & PRINCIPLES

Deferred / Triggered / Dropped / Principles carry from R2 via v3 unchanged. **Three principles added (from the pass's process lessons):**
1. **Propagate, don't caveat** — a correction stated once while headline assertions keep the old value manufactures internal contradiction (atlas P1).
2. **ED citations are ledger-verified, never memory-sourced** (atlas P2) — and the docket J-key is the durable handle where the ED is uncertain.
3. **Source-tier discipline** — primary canon (registry/substrate/scale_transitions/derived_stats live reads) outranks contract-/map-derived rows; live reads outrank stale registry pins (atlas R1/R7); inherited verdicts are labelled inherited (R2).

## §9 — SEQUENCE & SIZING

- **Jordan (docket):** J-2 → J-1 → J-22 → J-6(a,b) → J-23, then the three sittings (J-31 · J-32 · J-30), then J-7 and the system gates as they come up in lane order.
- **Lane A:** LA-1 + LA-12…LA-18 are ungated now (≈2–3 sessions of mechanical-tier propagation that shrinks the register by ~8 rows without a single ruling); gated items fire per docket.
- **Lane B (WIP=1):** unchanged spine LB-1→2→3 → **K-1** → LB-5 → **K-2 (solo)** → LB-8 → **K-3** → LB-13/14 → gated; LB-19/20 post-budget.
- **Lane C:** LC-0a (1) → LC-1 spine (1) → LC-3 first ritual (1, after J-6b+J-19+J-34) → LC-4 ≈1 session/module; LC-5 anytime.
- **Commit path for this orchestration:** bootstrapped session → re-pin as_of → verify ledger + the two §0 value flags → land map/graph/workplan under `designs/audit/2026-06-11-orchestration/` → banner v3 → repoint `lane_assignments.yaml` source + entry queues to v4 IDs in the same commit.

---
*v4 is the single working master per PI `<document_consolidation>` — committed and ratified 2026-06-12 (Jordan), the active canonical master. Every recommendation is Jordan-vetoable; §3 is the veto surface. No ED IDs assigned by this document; staged candidates file via lane blocks.*
