# Resolution Plan v1 — every identified issue, bottom-up and top-down, under an armature-first program

## Status: PROPOSED (sequencing + fix-shapes; files nothing, rules nothing — work routes through
## `ed_options.md` picks and the armature §5 docket; ED-1094 exception clause applies)
## Date: 2026-07-07 · Lane: IN · Anchors: ED-IN-0017 (audit) / ED-IN-0018 (armature)
## Jordan directives bound here: armature-built-FIRST · contract deployment + enforcement is the
## workplan's job · v40 re-authoring license · full ecosystem-tooling bindings · bottom-up AND
## top-down coverage of every identified issue

This plan resolves the audit's full confirmed-finding set two ways at once — **§2 top-down**
(strata that make the subsystems fit together as systems) and **§3 bottom-up** (every confirmed
finding → concrete fix · artifacts · lane · stratum · gate) — under one governing override:

## §0 · Sequencing override — the armature comes first (Jordan, 2026-07-07)

**No lane resumes subsystem work until the shaping harness is deployed.** The armature
(ED-IN-0018) is not one workstream among several; it is the instrument every other workstream is
shaped by. Concretely:

1. **Build (this PR + PR-2):** seam-contract spec + Echo Matrix (landed) · executable substrate
   (landed, critic-corrected: canon-authoritative defaults, OF-7/OF-B1 opt-in) · PR-2 =
   flag-gated echo wiring + the F7 smoke oracle + A14's runtime lint, so the harness can
   *observe* every subsystem it will shape.
2. **Deploy (the §6.3 waves, re-scoped as contract deployment):** each wave takes the armature
   onto one subsystem surface — its seam rows become that subsystem's acceptance criteria; its
   §3 key types become that subsystem's emit clauses; `references/rendering_dispositions.yaml`
   (A15's datafile) ships in the rendering wave. **Every subsequent lane task description MUST
   cite the armature rows it conforms to** — that citation is what "using the harness on each
   subsystem" means in practice, and its absence is a review-blocking defect.
3. **Enforce (the ladder):** A13–A16 + the existing A1–A12 run report-only from deployment,
   flip to CI-blocking per-check on backlog-to-zero (the repo's established warn→block
   discipline, §8 of CLAUDE.md). Session-level enforcement: the SessionStart banner + navigator
   surface the conformance state; the Stop-hook/handoff convention records which armature rows a
   session touched. Holonic guardrails (ED-1083 §2 — local rule only · declared I/O only · no
   scripting drift · no shape divergence) bind every implementation lane, with the armature rows
   as their checkable form.

Only Stratum A (truth reconciliation — pure doc/registry repairs that make the armature's own
reads trustworthy) runs concurrently with armature deployment; Strata B–E queue behind it and
consume it. This inverts nothing in workplan v6's milestones — it re-orders the *entry* into
them: M1's junctures are reached THROUGH armature-conformant wiring, never around it.

---

## §1 · Ecosystem bindings — the tools/skills/scripts each program layer calls

The plan is executed with the repo's own instruments (CLAUDE.md §8/§9), never ad-hoc re-implementations:

| Program layer | Instruments (invoke these, extend never re-implement) |
|---|---|
| Steering / "where are we" | `valoria-workplan-navigator` skill + `tools/workplan_status.py` (the ED-IN-0010 progress board; refresh `workplan_v6_progress.yaml` `as_of` on every wave merge) · `tools/session_status.py` SessionStart banner · root `HANDOFF.md` + lane handoffs (the ONLY status surfaces, v6 §0) |
| Currency / truth (Stratum A) | `tools/currency_consistency_check.py` (self-updating recency gate) · `tools/freshness_gate.py` (133/133 green as of this audit — keep it green; `--update` after every head re-export) · `tools/validate_ed_citations.py` (OPEN_AS_BASIS discipline) · `canon/supersession_register.yaml` + `tools/ci_supersession_check.py` for every v40 re-authoring strike |
| Contract deployment/enforcement | `skills/valoria-module-adjudicator` + its `contract_adjudicator.py` (A1–A12 today; A13/A14-static land there with the `doc_emit_ref:` schema field) · the co-file-checker pattern (`tools/ci_co_file_checker.py`) hosts A16 · `sim/substrate` hosts A14-runtime · `references/rendering_dispositions.yaml` feeds A15 · CI job flips per the report-only→blocking ladder |
| Sim / oracle work (Strata B–E) | `sim/tests/` seeded regressions + the F7 oracle (OPT-3) · `tests/valoria` unit suite · the byte-exact gates (MB precedent) for every flag-gated behavior change · `tools/ci_sim_fabrication_check.py` (with its known leaks — provenance still verified by hand) · `valoria-simulator` / `valoria-combat-simulator` skills for module builds |
| Design / canon authoring (v40 re-writes) | `valoria-compiler` (assembly w/ canon-guard) · `valoria-canon-guard` (P-01..14 compliance) · `valoria-atomizer` + `valoria-chunker` (index/infill hygiene for re-authored heads) · `prose-writer` for infill · `valoria-dice-model` for any number that moves |
| Audit / verification cadence | `valoria-mechanic-audit` (consistency) · `valoria-resolution-diagnostic` (rolling-engine re-verdicts post-§5.12) · the relay/refuter pattern institutionalized by this audit (charter §method) for every wave's P1/P2 claims · `valoria-vector-audit` for structural-debt re-scans |
| ID / ledger discipline | `references/id_reservations.yaml` protocol (repaired this PR; §5.10 renumber pending Jordan) · lane-scoped PRs (CLAUDE.md §4) · merge-ratifies with loud exceptions (ED-1094) |

Retired/dead instruments are NOT called (CLAUDE.md §8's dead-tools list; `roadmap_state.yaml` is
retired — the navigator + progress board replaced it; anything under `deprecated/`).

---

## §2 · Top-down (holistic): five strata + the governance thread

**Ordering logic.** The failure pattern is layered: rulings that never executed (truth) under an
oracle that drifted from canon (reference) under transport that exists only as prose (spine) —
which is why play surfaces are unreachable (reach) and why every balance number is untrustworthy
(measurement). Fixing a layer above a broken lower layer is band-fitting; so **A ∥ armature →
B → C(deploy) → D → E**, with §0's override making the armature the spine of the whole sequence.

**Stratum A — Truth reconciliation** *(runs now, alongside armature deployment).* Execute every
ruled-but-unexecuted item (ED-871 · ED-912 propagation · CI-75→100 supersession incl. the
Church-victory text · fork-2 strike · fork-11 + miraculous_event contract refreshes · ED-935
consumer edges · ED-SE-0001's own anti-orphaning updates · ED-1042 steering flip + residual
re-file · register back-propagation · intent-hygiene corrections [needs_jordan]). Exit: zero
ruled-but-unexecuted items older than a week; currency/freshness/citation gates green.
Carriers: OPT-5/6/8/14/15/16/17.

**Stratum B — Oracle to canon.** LPS-1 faction model in sim or loud pre-LPS-1 banner (OPT-1) ·
§5.12 band-discipline ruling then ER-2/Overwhelming unification + six-kernel parity coverage
(OPT-10) · contest dispatch to the promoted kernel as ED-SC-0006/0007 acceptance criteria
(OPT-11) + pool-formula ruling (ED-SC-0004) · Turmoil gate repair (OPT-4, needs_jordan) ·
fault-channel + dead-param hygiene. Exit: every live resolver implements ratified canon or
carries a loud [PROVISIONAL] docket pointer; parity suite covers all six kernels.

**Stratum C — Contract deployment** *(the armature waves, §0.2).* PR-2 echo wiring + F7 →
keying wave (OPT-9: §3 types onto settlement/ci_political/era gates) → down-seam wave (§12.4
targets[] per family) → consumer/contract hygiene wave → rendering wave (dispositions datafile +
articulation rows + zoom type_id citations). Exit: one seeded campaign yields a canonical key
log where every §2.1 echo rule fires end-to-end; A13–A16 backlogs zero; enforcement ladder
flipping.

**Stratum D — Reach and agency.** The context-derivation bridge (SC) · scene types beyond
contest + §4.3.3 procedures/code · player surfaces in dependency order (domain-action menu →
MB battle surface + §D aftermath implementation → combat input post-R3 → un-islanded
settlement/thread/NPC content) · injector paths to play. Exit: M1's seven junctures each have a
reachable, feedback-bearing, armature-conformant surface.

**Stratum E — Measurement and balance.** Lockout ruling (OPT-2) + Muster accrual cap → n≥100
oracle-guarded re-measurement (the ~87% lesson: R1 traced it to an n=8 batch that propagated
into ≥5 docs unchallenged — institutionalize "no balance claim without the F7 oracle + n≥100") ·
MB gauge triage (OPT-13) → RC-5/DG-1 rulings → DG-2 · full emergence audit re-run on real key
logs · post-R3 hunts · P3-lite human-plays. Exit: balance claims cite seeded, oracle-guarded
runs of a canon-conformant sim.

**Governance thread** *(gates items, not strata).* The armature §5 docket (16 rows incl.
OF-D6 [HIGH], OF-CAP, RNG-COLLISION, §5.12, §5.10, §5.16) + needs_jordan OPTs (1/2/4/14, §6.3
Partition). **Recommended: one consolidated ruling pass before PR-2 merges** — it unblocks PR-2
semantics, Stratum B's choices, and Stratum E's trap ruling in one sitting.

---

## §3 · Bottom-up (granular): every confirmed finding → fix · artifacts · lane · stratum · gate

*(Unchanged in substance from the §2 tables of the prior draft, now with R1/R5/critic
corrections folded in. KNOWN-TRACKED calibration items stay with their existing owners; killed
findings live in `finding_status.md` only. Coverage check at the end.)*

### Faction / oracle
| Finding | Fix | Artifacts | Lane | Str. | Gate |
|---|---|---|---|---|---|
| C-FA-1 (R2-qualified) | Implement LPS-1 in sim (wire the inert registry.py L/PS fields into Mandate aggregation + an Accounting step) OR banner the oracle pre-LPS-1/port-blocking | accounting.py, territory/registry.py, game_state.py | FA | B | OPT-1 ruling |
| C-FA-2 (G2-resolved) | settlement_layer:47 → Local Economy ×50 (display); Treasury stays ×10 (:169, canon); fix dead `derived_stats_v1` cites | settlement_layer_v30 | SE | A | — |
| C-FA-3 | Retire the "PS" collision (victory.py comments + port maps) | victory.py | FA | B | — |
| C-FA-4 / C-EMERGE-3 (G1-adjudicated: real, not sufficient) | Wire Varfell/Hafenmark uniques (post contamination audit) AND decouple the unique-slot→Conquest fallthrough confound | faction_action.py + 8 provincial stubs | FA | D | contamination audit |
| C-FA-5 (G1/G2-narrowed) | Cap/curve Muster accrual — the snowball motor (battle function verified concave; no defender advantage exists to soften it) | faction_action.py; faction_layer §7 | FA | E | OPT-2 adjacent |
| C-FA-8 | Author GD-2 mandatory-precedence; replace the flat mix | faction_action.py; domain_actions doc | FA | D | ED-FA-0002 |
| C-FA-9 / C-EMERGE-8 | One victory threshold, one home; delete/wire the dead param | mc_v18.py, victory.py | FA | B | — |
| C-FA-10 | Implement propose_treaty or banner treaty exploit analyses doc-only | treaty.py | FA | D | — |
| C-FA-11 | De-overload α before typed export | faction_canon/behavior | FA | A | — |
| C-FA-12 | One verb menu via the domain_actions home doc | new doc | FA | D | ED-FA-0002 |
| C-FA-6 / C-STUB-6 | faction_politics doc:null flip + dead-path sweep + CURRENT.md row + authored emit clauses (G2: doc has zero) + sim stub | module_contracts, CURRENT.md | FA | A/C | ED-IN-0016 |

### Emergence / campaign loop
| Finding | Fix | Artifacts | Lane | Str. | Gate |
|---|---|---|---|---|---|
| C-EMERGE-1/2 (R1-qualified: trap one-way but avoidable; Mil-floor not load-bearing; ~87% = n=8 provenance) | OPT-2 lockout ruling (weigh the Tainter collapse-recovery ruling vs its unimplemented Reconstitute mechanic); pin n=100 in F7; correct CLAUDE.md §7's figure | mc_v18, F7 oracle, CLAUDE.md | FA/IN | E | OPT-2 |
| C-EMERGE-4 | The derivation bridge — the unlock for the whole scene phase | scene_dispatch + canon rule | SC | D | ED-SC-0006/0007 |
| C-EMERGE-5 (R1: Revolt never built) | Rule Uncontrolled-reachability; wire revolt→owner-None via the keying wave or retire the trigger's precondition | insurgency_pipeline, keying wave | WR/SE | C/D | design call |
| C-EMERGE-6 (R1-confirmed) | Seed world.npcs (canon-backed population rule) so NPE stops no-op'ing | npe.py, worldgen | WR | D | — |
| C-EMERGE-7 | Resolved per-wave as subsystems gain writers | (per-wave) | all | C/D | — |
| C-EMERGE-9 | Ablation-flag layer with F7 — required for causal claims | mc_v18 params | IN | E | — |
| C-EMERGE-10/11 (G1: 60/60 silent) | Retire/wire `parliamentary`; replace `except: pass` with a counted, serialized fault channel | mc_v18, serialize | IN | B | — |
| C-REACH-5 (R1: NOT-INTENDED, canon fully specifies) | Turmoil track module (peninsular_strain is the writer) or re-spec the GD-1 gate | new turmoil track, victory.py | WR/FA | B | **OPT-4 needs_jordan** |
| C-REACH-6 | Implement ip_track/Strain/PI stubs (Stage-2.5 preconditions) with MS naming | sim/peninsular | WR | C | ED-WR-0002 |
| C-REACH-2 | Retire deprecated combat branch; route via substrate when PC input lands | scene_dispatch | PC | D | ED-PC-0001, post-R3 |
| C-REACH-10 (R1: KNOWN-TRACKED ED-SC-0007) | Already accepted consequence-spine work — PR-2 routes it | PR-2 | SC | C | — |

### Threadwork / knots / fieldwork
| Finding | Fix | Artifacts | Lane | Str. | Gate |
|---|---|---|---|---|---|
| C-TW-2 (G3 runtime-measured −1/−2) | Execute ED-871: cost 0 in §3.2 + operations.py; Mending exits the blanket penalty | threadwork_v30, operations.py | WR | A | — |
| C-TW-3/4/10/11 | Per-op cost tables replace the blanket penalty; un-invert the POP cap; Leap's 3 gates; R-57/R-55 | operations.py | WR | B | — |
| C-TW-6/7 | Implement or loudly banner Thread Fatigue + Overweave state | operations.py | WR | C | — |
| C-TW-8/9 | Invoke co_movement per op; implement/banner Community Organizing + Thread-Read | co_movement.py | WR | C | — |
| C-TW-12 (R3: capacities are ED-773's, not PP-632's) | Rebuild knots.py on the ED-912 gauge | knots.py | FI | A/B | — |
| C-TW-1 | Thread reachability = Stratum D; sim/tests coverage NOW | scene_dispatch, sim/tests | WR | C/D | ED-1010/1011 |
| Anchoring exploit (G3: cap absent) | Add the cadence cap (1/season/Knot natural) to §3.5 | threadwork_v30 | WR | A | canon ruling |
| C-FI-1/2 | Reconcile double-economy + Disposition contradiction inside the EP-8 head adjudication (Options A/B/C prepped) | fieldwork vs investigation docs | FI | A | ED-IN-0016 row |
| C-FI-4/5/6/7 | fieldwork_bg re-export + the knots propagation batch (OPT-6) | co-files, mechanics_index | FI | A | — |
| C-FI-8 (R3: doubly stale) | params/fieldwork:106 → Spirit | params/fieldwork | FI | A | — |
| C-FI-10 | Banner the orphaned second resolver | tests/sim_framework | FI | A | — |
| C-FI-12 | Claim-grammar back half = SC/FI evidence-object + precedent-store build | v2 §5 chain | FI/SC | D | v2 acceptance |
| Knot-stress staleness (G3) | Re-run F2 lifecycle stress on the ED-912 gauge before citing 22/24 again | stress harness | FI | E | after C-TW-12 |

### Keys / rendering / injectors / contracts
| Finding | Fix | Artifacts | Lane | Str. | Gate |
|---|---|---|---|---|---|
| C-KEY-1/2 | A13 + per-module emit clauses in the deployment waves; `doc_emit_ref:` schema field | armature §4, module docs | IN | C | — |
| C-KEY-3 | Combat trace-vocab → Key-type mapping table | combat_engine_v1 doc | PC | C | — |
| C-KEY-6 | Six consumes: edges + gap_note refresh (OPT-8) | module_contracts | IN | A | — |
| C-KEY-8 | Register meta.cascade_cluster_event (OPT-7) | registry | IN | A | — |
| C-KEY-9 (R4: core-five DELIBERATE) | §2.5 dispositions: core-five as DELIBERATE-SILENT rows; opinion_revised + miraculous_event get pathways or corrected descriptions | registry, articulation | IN/WR | C | — |
| C-KEY-10 | Zoom rows cite type_ids | scale_transitions §4.3 | IN | C | — |
| C-INJ-1/2/3/5 | miraculous_event full contract footprint; scenario_authoring mechanics_index entry + Stage-1 compile build | module_contracts, Stage-1 | WR/IN | C | fork-11 (ruled) |
| C-INJ-7/8/9 | check_world_state_triggers + §4.3.3 procedures; zoom rows name queueing call sites; the §25 witness row | zoom_in_out, scene_slate wiring | IN/WR | C/D | — |
| C-INJ-11/12 | causes[] rules (armature §2.4) + provenance-name unification | registry + emitters | IN | C | — |
| C-STUB-1..7 | Stub×milestone map into the workplan reconcile; T0 domain_actions row; NPC lane assignment; MS-rename at implementation | workplan §5, handoffs | IN | A | monthly reconcile |
| scene.gossip yaml (G4: the only strict-parse failure of 48) | Quote the scalar | registry | IN | A | — |

### σ-substrate / resolvers
| Finding | Fix | Artifacts | Lane | Str. | Gate |
|---|---|---|---|---|---|
| C-SIG-3 / C-RESPESS-1 (R5-corrected: 6%→45.9% at the real History-7 ceiling) | §5.12 ruling → ER-2 + pool-aware bar unification; then re-run diagnostics | sigma_leverage, core.py | PC/IN | B | **§5.12** |
| C-SIG-2 (+G3: 2 more kernels) | Parity coverage: massbattle σ-copy + d10 duplication + faction d6 kernel + Gaussian jury model | parity suite | IN | B | — |
| C-SIG-4 (R5: 3.445pp reproduced) | Revise armature-doc proofs to shipped banding | engine/ armature doc | IN | B | — |
| C-SIG-5 (R5: 14.19–23.40% reproduced) | Document the sawtooth or re-spec the bar pre-calibration | sigma_leverage + params | SC | B | ED-SC-0004 adj. |
| C-SIG-6 | Correct params/core.md ER-2 tail ranges | params/core.md | IN | A | — |
| C-SIG-8 (G3: Breadth/Distance silently dropped) | Implement the missing ⅔ of the Three-Axis Ob formula or strike from params | operations.py, params | WR | B | — |
| C-RESPESS-2/3/4/5 | OPT-11 dispatch criterion + ED-SC-0004 formula ruling + the filed KU-3/stack items | contest package | SC | B/D | ED-SC-0004/0006/0009 |
| C-RESPESS-6/7 (R5-qualified: pre-clamp; ~6/28 cells clamp) | One difficulty derivation; spec the high-Ob flat-5% behavior | domain resolver spec | FA | B | ED-874 lineage |

### Mass battle / settlement
| Finding | Fix | Artifacts | Lane | Str. | Gate |
|---|---|---|---|---|---|
| C-MBSE-1/2/3 (+full gauge run) | Per-row triage from the archived run → RC-5/DG-1 rulings → attacker-side pool discipline fix | gauge, orchestration | MB | E | RC-5/DG-1 |
| C-MBSE-4 | DG-2 after RC-1 stability + partition-invariance (its own doc's rule) | proposal doc | MB | E | DG-2 |
| C-MBSE-5/6/7 | Player-facing battle surface (Phase-1 declarations, per-phase decisions) + implement the §D aftermath apparatus | new MB UI spec, sim | MB | D | — |
| C-MBSE-9..13 | The keying wave (OPT-9) with gate-differentiated emits; CI thresholds as data pending §5.11 | contracts + heads | SE/WR | C | §5.11 |
| C-MBSE-14/15 | Deck engine S3–S6 (M2 critical path); port the 28-card pack | sim/territory | SE | D | — |

### NPC / pessimist / process
| Finding | Fix | Artifacts | Lane | Str. | Gate |
|---|---|---|---|---|---|
| C-NPC-1..6 (G4: Reichard still live) | OPT-12 triage ED + implement-or-banner the six unimplemented mechanisms; assign the NPC lane | npc docs, sim, workplan | WR | A/D | OPT-12 |
| C-NPC-7/8 | Complete the half-applied damper note; ONE direction for npc_memory (retire-vs-build fork) | module_contracts | WR | A | needs ruling |
| C-NERSPESS-1/2/3 (R5-confirmed) | Re-grade #77's Ω table with the design/operational split; operational column inherits Strata B–D exits | #77 addendum | IN | E | OPT-14 adj. |
| C-NERSPESS-4/5/6 | OPT-14 (intent hygiene) + OPT-16 (settlement re-anchor) | ledger notes, CURRENT.md | IN/SE | A | **needs_jordan** |
| C-VERIFY confirmed set | OPT-15/17 batches (registers, armor upside, echo season-cap, roster/glossary, resonance_style, Partition §6.3 [needs_jordan]) | per-item | IN/WR | A | OPT-17 |
| U-11 process | §5.10 renumber; ratify-all batches serialize on id_reservations (workplan §6 addition at reconcile) | ledger, workplan | IN | A | **§5.10** |

**Coverage check:** every NEW/KNOWN-UNTRACKED finding in `finding_status.md` appears above or in
its named OPT carrier; KNOWN-TRACKED items stay with their owners; killed/retired findings are
recorded in finding_status only.

---

## §4 · Master-workplan v6 integration (binds, does not fork — v6 §0 hierarchy rule)

v6 stays the single working master; this plan is dated-audit evidence its monthly reconcile
(§6/J-14) folds in by pointer. Bindings: **M1 junctures ← strata** (1–2 ← D-menus on C-transport;
3 ← OPT-11 + the bridge; 4 ← C-REACH-2 post-R3; 5 ← A/B thread fixes + C-TW-1; 6 ← substrate
accounting_boundary + ED-1051; 7 ← rendering wave feeding narrative Stage 0). **v6 §2 IN-spine ←
this PR** (item 2 gains the substrate; item 3 = Stratum D's first doc; item 4 = the armature
wholesale; items 5–6 gain Stratum A batches). **v6 §5 register deltas for the next reconcile:**
the armature §5 rows (T0: OF-D6 + the PR-2-gating trio; T1: §5.12, §5.11; T2: §5.10, §5.16) +
the missing domain_actions T0 row (C-STUB-3) + **the §0 armature-first override recorded as the
program's entry condition**. **v6 §4 lanes** gain their §3 rows above; the NPC-lane question
(C-STUB-7) resolves at reconcile; Appendix-B's orphan = OPT-12. No status duplicated here.

## §5 · v40 unification / Godot-readiness lens — with the re-authoring license

**Jordan's license (2026-07-07):** documents MAY be duplicated, renamed, or rewritten entirely
for v40 — uniformity, coherency, consistency, and an EXPLICIT new-version marker outrank
in-place patch-history. Operationalized:

- **The v40 re-authoring mechanism:** a subsystem head reaches v40 by REWRITE-AND-SUPERSEDE —
  author `<subsystem>_v40.md` (+ index/infill co-files) fresh from the reconciled truth (Stratum
  A output + armature rows as its transport section), banner the old head `[SUPERSEDED-BY:
  <head>_v40.md]`, register the supersession, flip CURRENT.md, `freshness_gate --update`, all in
  one PR per head. This retires the CLAUDE.md §4 hazard ("no file carries _v40") by making the
  generation marker explicit in filenames, and every v40 head is born armature-conformant
  (emit clauses, FEEDBACK lines, §2.5 dispositions as authored sections, not retrofits).
- **Re-authoring order = deployment order:** heads are rewritten in their wave (keying wave
  rewrites settlement_layer/ci_political/victory heads; down-seam wave rewrites the four emitter
  families' homes incl. the new domain_actions_v40; rendering wave rewrites articulation;
  Stratum B rewrites faction_canon/behavior to LPS-1-as-implemented). The EP-8 adjudication picks
  which fieldwork text seeds `fieldwork_v40.md`.
- **The unification bar, per surface** (each with its carrier): currency completeness incl. the
  joints (ED-IN-0016/OPT-16 · Stratum A) · supersession hygiene (CI-75, Partition §6.3, RS
  carriers, ED-912 residue, ARC-T04 · Stratum A) · contracts-bound: 0 doc:null, 0 [ASSUMPTION],
  consumer closure, A13–A16 green (Strata A/C; ED-1051 flips engine_clock) · one resolution
  substrate, six kernels under parity (Stratum B/§5.12) · oracle = canon (Stratum B) · typed
  data crossing (OPT-7 + ED-1052 + armature §3 payload alignment) · the Key spine in code
  (**closed this PR**; hardened PR-2/3) · all directions audited AND specified (the armature §2
  standing contract; A15/A16 keep it complete) · measurement trust (Stratum E).
- **The v40 statement:** when Strata A–C exits hold, "v40" stops being a generation label and
  becomes a checkable predicate — adjudicator + A13–A16 + F7 green over explicitly-versioned
  `_v40` heads on a canon-conformant oracle. That is the state M3's Gate-0 starts the Godot port
  from, with `sim/substrate` as Key.gd's oracle and the typed exports as its data pack.

## §6 · Sequencing summary (one screen)

**Now (this PR):** armature spec + substrate landed (critic-corrected) · registry repaired ·
audit + this plan delivered · docket + 17 OPTs to Jordan. **Next:** Jordan's consolidated ruling
pass ∥ Stratum A batch ∥ PR-2 (echo wiring + F7 + A14-runtime — the harness becomes observable).
**Then:** deployment waves (Stratum C) per lane — each wave = deploy contract rows + re-author
that head to `_v40` + enforce (checker report-only) — with Stratum B's oracle work landing as
its rulings arrive. **Then:** Stratum D reach/agency in juncture order. **Last:** Stratum E
measurement against a machine that finally matches its canon. Enforcement ladder flips each
check to blocking as its backlog zeroes. M1 = A+B+C complete, D through juncture 7; M2 adds the
deck + narrative stages; M3 (GO) opens at Gate-0 with the v40 predicate green.
