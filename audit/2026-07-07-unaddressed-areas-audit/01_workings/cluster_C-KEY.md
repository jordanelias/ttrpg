# cluster_C-KEY

_Evidence cluster dossier, read-only; archived verbatim from the agent's final message by the Fable orchestrator (2026-07-07). Verdicts pending refuter pass + Fable adjudication - see `unaddressed_areas_audit_v1.md`._

# Cluster C-KEY dossier

**Read-only evidence cluster. No files created/edited/deleted — Bash used only for grep/probes per mandate. Barred from rendering verdicts; findings below are evidence-graded (P1/P2/P3, status tag) for Fable 5 adjudication, not final rulings.**

Primary sources read in full: `references/module_contracts.yaml` (891L), `designs/architecture/key_type_registry_v30.md` (1046L, 48 physical type entries), `designs/articulation/articulation_layer_v30.md` (363L), `designs/architecture/scale_transitions_v30.md` (335L, incl. §12), `designs/architecture/propagation_spec_v1.md` (394L). Plus targeted greps/reads of ~20 emitter-side design docs and `sim/`.

---

## Part 1 — emit-clause coverage table (extended to all modules)

Method: for each module in `module_contracts.yaml` with a non-trivial state machine, grep its home `doc:` (and infill/index siblings where co-filed) for `emit`/`Key`, distinguish genuine Key-substrate citations from coincidental English usage (e.g. "Key rules:", "Key principle:"), and compare against the contract's `emits:` list.

| Module | doc: | mutates state? | doc has native emit/Key-type clauses? | contract `emits:` non-empty? | Verdict |
|---|---|---|---|---|---|
| faction_state | `faction_behavior_v30.md` | yes | **YES** — 7 "emit" hits incl. explicit §5.1 table "Faction state changes emit Keys" (L414-431) | yes (3) | **OK-NATIVE** |
| npc_behavior | `npc_behavior_v30.md` | yes | doc-of-record: 0/0. Real spec lives in uncited co-doc `political_dynamics_keys_migration_v30.md` ("doc-12"): 61 "emit" / 66 "Key" hits, explicit §8 sequencing tree | yes (11) | **OK-COREF** (doc field points to a silent doc; native content lives in a file named only in `sources:`) |
| npc_memory | null | reader only | N/A — no doc | emits: [] (by design, pure consumer) | DOC-NULL, non-emitting |
| piety_track | `conviction_track_v1.md` | yes (scars) | 0/0 | yes (1) | **SILENT/NONEMPTY** |
| territorial_piety | `conviction_track_v30.md` | yes (CV/CI/TC) | 0/0 (index+infill also 0/0) | **empty** | **ZERO-INTEGRATION** (own gap_note, L262) |
| threadwork | `threadwork_v30.md` | yes (Coherence, Fatigue) | 0 emit; 1 "Key" hit, non-substantive ("Key effects:") | yes (2) | **SILENT/NONEMPTY** |
| fieldwork_knots | `knots_v30.md` | yes | Partial — §10.3/10.4 (L302-303) explicitly name `meta.knot_formed`/`meta.knot_ruptured`; `scene.gift`/`state.belief_revised` named nowhere in this doc or `fieldwork_socializing.md` | yes (4) | **PARTIAL** (2/4 native) |
| scene_slate | null | no owned state; emits richly | N/A — no doc | yes (7) | **DOC-NULL-GAP** |
| game_director | null | no owned state | N/A | yes (3) | **DOC-NULL-GAP** |
| scene_timer | null | — | N/A | empty | **DELIBERATE-N/A** (tooling sidecar, `[verification RU-5]`) |
| audit | null | — | N/A | empty | **DELIBERATE-N/A** (QA/telemetry, `[verification RU-5]`) |
| social_contest | `social_contest_v30.md` | yes (persuasion_track) | 0/0 (index+infill also 0/0) | yes (4) | **SILENT/NONEMPTY** |
| mass_battle | `mass_battle_v30.md` | resolves battle outcomes | 2 generic "emit" hits (describe engine behaviour abstractly, e.g. "engine emits an incapacitated/captured state"), 0 hits for "battle_concluded" or any Key type_id; index+infill also 0/0 | yes (2, dual-form naming drift already flagged in-file) | **SILENT/NONEMPTY** |
| domain_actions | null | — | N/A (resolver-spec audit-output file also 0/0) | yes (5) | **DOC-NULL-GAP** |
| peninsular_strain | `peninsular_strain_v30.md` | yes (Turmoil, IP) | 0 emit; 1 "Key" hit, non-substantive ("Key principle:") | yes (4) | **SILENT/NONEMPTY** |
| settlement_layer | `settlement_layer_v30.md` | yes (heavy) | **0/0 — CALIBRATION EP-4.** `g_ord0`/`g_def0` gates carry no emit clause; whole doc zero "Key"/"emit" hits | yes but only 1 (`env.population_change`) — the revolt/auto-capture gates have **no** emit at all, doc or contract | **ZERO-INTEGRATION for the gates** |
| settlement_economy | null | phantom (recommend retire) | N/A | empty | DOC-NULL, phantom |
| ci_political | `ci_political_v30.md` | yes (political pool, cards) | **0/0 — CALIBRATION EP-5** | **empty** | **ZERO-INTEGRATION** (own gap_note, L641) |
| victory | `victory_v30.md` | reader, but **triggers era transitions** | 0 emit; 3 "Key" hits, all non-substantive ("Key rules:"/"Key Difficulty"/"Key findings:"); infill also 0/0 | **empty** | **ZERO-INTEGRATION** (own gap_note, L679) |
| engine_clock | null (candidate: `propagation_spec_v1.md`, ED-1051 pending) | yes (season counter) | candidate doc **does** have native emit clauses (O.2 block, explicit) | yes (2) | **DOC-NULL-but-candidate-exists-unflipped** |
| faction_politics | null (a same-named but unrelated CANONICAL doc, `faction_politics_v30.md`, exists — 0/0 Key language, it's a rank-ladder patch register) | Standing lives cross-module in faction_state | N/A | yes (4) | **DOC-NULL-GAP** |
| miraculous_event | `miraculous_event_v30.md` | gated emitter | 0/0 | yes (1) | **SILENT/NONEMPTY** |
| scenario_authoring | null (`emergent_scenarios.md`/`narrative_scenario_chains.md` exist, uncited, 0/0 Key language) | — | N/A | yes (2) | **DOC-NULL-GAP** |
| articulation_layer | `articulation_layer_v30.md` | reader/renderer by design | N/A — not expected to emit | empty (deliberate) | **DELIBERATE-N/A** |
| clock_registry | `clock_registry_v30.md` | manifest | N/A | empty (deliberate) | **DELIBERATE-N/A** |
| personal_combat | `combat_engine_v1/` (Python source dir, not prose) | yes (heavy) | Has its own internal `_emit()` trace-event vocabulary (25+ kinds: `engagement_start`, `commit`, `read`, `roll`, `contact`…) that is **never mapped** anywhere in the corpus to the 4 canonical `scene.combat_*` types; those are declared only in the Godot skeleton's `.tres` resources, external to this doc | yes (3) | **CODE-SEPARATE-VOCAB** |
| campaign_architecture | `campaign_architecture_v30.md` | stub; reclassified non-runtime | — | — | excluded (recommend-retire) |

**Roll-up:** of 19 non-null-doc, state-mutating modules, only **1** (faction_state) has genuine doc-native emit-clause coverage backing its contract; **1** more (npc_behavior) has it only via a co-doc not named in `doc:`; **1** is partial (fieldwork_knots); **9** have zero native "emit"/Key-type language in their canonical doc (6 of these — piety_track, threadwork, social_contest, mass_battle, peninsular_strain, miraculous_event — nonetheless carry non-empty contract `emits:` lists extracted purely from the substrate/registry cross-reference, never validated against doc prose; 3 — territorial_piety, ci_political, victory — are zero-integration on both sides). settlement_layer is the calibration hybrid (1 declared emit, 2 gates with none at all).

---

## Part 2 — §12.3 population reality / causes[] population

**§12.4's four down-seam emitter families and their actual specs:**

| Emitter | Home doc | targets[]/scale_signature/stat_deltas guidance? | causes[] guidance? |
|---|---|---|---|
| domain_actions | **null** (only quasi-doc: `designs/audit/2026-05-28-resolution-diagnostic/domain_action_resolver_spec.md`, itself an audit-output artifact) | 0 hits for any of the three terms | 0 hits |
| faction_politics | **null** (the similarly-named CANONICAL `faction_politics_v30.md` is a rank-ladder patch register, unrelated content) | 0 hits | 0 hits |
| peninsular_strain | `peninsular_strain_v30.md` (the one family that *does* have a home doc) | **0 hits** — the doc never uses "targets[]", "scale_signature", or "stat_deltas" anywhere | 0 hits |
| scenario_authoring | **null** (`designs/arcs/emergent_scenarios.md`, `narrative_scenario_chains.md` exist but are uncited by the module contract and score 0/0 for these terms too) | 0 hits | 0 hits |

**Sim-side reality is stronger than "unpopulated" — it's absent.** `grep -rl "targets\[\]\|scale_signature\|stat_deltas" sim/ --include=*.py` returns **zero files**; there is no `class Key` anywhere in `sim/`. The Key-substrate schema (targets[]/scale_signature/stat_deltas/causes[]) has **no runtime implementation at all** in the Python reference — only the Godot skeleton's combat slice (`designs/godot/skeleton/engines/combat/`) instantiates anything resembling `stat_deltas`. This corroborates `propagation_spec_v1.md`'s own framing (AU-5: "OUTCOME→ECHO MAPPING GAP," `domain_echo.py` unwired to `scene_dispatch.py`) but sharpens it: there is no substrate to populate `targets[]` *into* for any of these four families outside the one ported combat module.

**causes[] population — corpus-wide check.** Grepping all of `designs/` + `references/` for literal `causes[]` and filtering to non-audit canonical heads: exactly **one** canonical design doc gives emitter-side authoring guidance for populating it — `political_dynamics_keys_migration_v30.md` (npc_behavior's Procedure D, L304/324/583/613: "the `causes[]` field wires the opinion revision to the source Keys"). **None** of the four §12.4 emitter docs (where they exist) mention `causes[]` at all. `key_substrate_v30.md` itself self-reports (L357) that only **~15% of Keys have causes[] populated** in production sim observation — the sparse-diagonal problem is self-acknowledged in the substrate spec, not merely inferred here.

---

## Part 3 — consumer-declaration closure mismatches

Method: parsed all 48 registry entries' `consuming_systems:` and cross-checked each against the named module's `consumes:` list in `module_contracts.yaml` (script-verified, not spot-checked). One methodology note first: `articulation_layer`'s contract declares `consumes: [{type: "*", from: engine}]` — a documented wildcard (its own gap_note, L768: "registry also lists 31 explicit per-type subscriptions — kept as the wildcard"). Every one of the 41 registry entries naming `articulation` as a consumer is therefore **not** a real mismatch; excluded below.

**Real mismatches found (8 type-module edges, all resolve to two modules):**

| Key type | Registry-declared consumer | Consumer's `consumes:` list | Status |
|---|---|---|---|
| `scene.combat_resolved` | npc_behavior | absent | **KNOWN-TRACKED** — personal_combat's own gap_note A4 (module_contracts.yaml L844) already names exactly this |
| `scene.combat_resolved` | faction_state (faction_layer) | absent | KNOWN-TRACKED (same A4 note) |
| `scene.combat_felled` | npc_behavior | absent | KNOWN-TRACKED (A4) |
| `scene.combat_felled` | faction_state | absent | KNOWN-TRACKED (A4) |
| `scene.thread_operation` | npc_behavior | absent | **NEW** |
| `scene.draft_da` | npc_behavior | absent | **NEW** |
| `scene.displacement` | npc_behavior (self — npc_behavior also *emits* this) | absent | **NEW** |
| `mechanical.project_advanced` | npc_behavior (self) | absent | **NEW** |
| `state.project_completed` | npc_behavior (self) | absent | **NEW** |
| `state.project_failed` | npc_behavior (self) | absent | **NEW** |

The six NEW rows are notable because npc_behavior's own gap_note (module_contracts.yaml L168) actively asserts the **opposite, now-stale** claim: "doc-12 §8 sequencing tree names FOUR Key types its own §7 never declares **and the registry lacks**." That was true before ED-935 (J-2 register-all); the registry's own §9 Type Count Summary (L1022) confirms ED-935 subsequently registered exactly `scene.thread_operation`, `scene.draft_da`, `scene.displacement`, `mechanical.project_advanced`, `state.project_completed`, `state.project_failed` (plus `scene.combat_resolved`) — so the "unregistered" half of the complaint is resolved, but nobody circled back to add the corresponding `consumes:` entries once the types existed. Four of the six are **self-loop** gaps (npc_behavior both emits and is registry-declared as its own consumer for `scene.displacement`/`mechanical.project_advanced`/`state.project_completed`/`state.project_failed`).

No other mismatches exist anywhere in the 48-type × module cross-product (verified exhaustively, not sampled).

---

## Part 4 — the 44-row registry × rendering sweep table (core deliverable)

**Scope note (itself a finding, see C-KEY-8 below):** the registry declares "44" types (§9) but **48 entries are physically present** in §2-§8 — 3 combat sub-types (`scene.combat_strike/hit/felled`) and `meta.legacy_event` are outside the declared count. This drift is already flagged in-file ("the pre-existing declared-vs-parsed header drift, master item 11 / A9" — L1022), so KNOWN; I sweep all 48 physical entries below, all of them "in §2-§8" per the charter's instruction.

**Methodology note on the Zoom-trigger column:** `scale_transitions_v30.md` §4.3.2/§4.3.3 use **natural-language state conditions**, never literal Key `type_id` citations. No row in either table cites a registered type by name. "Correlate" below is my own semantic mapping (payload fields ↔ condition text), not a canon citation — treat it as lower-confidence than the Tier-2/Tier-3 columns, which are literal string matches. This gap is itself C-KEY-10.

Legend: **RR**=RENDERED-RICH (dedicated Tier-2 and/or explicit Tier-3-named pathway) · **RG**=RENDERED-GENERIC (reaches the player only via universal significance/salience scoring — all 48 types are theoretically Tier-3-eligible via the wildcard consumer + top-N significance; RG means *no dedicated guarantee*) · **UR**=UNRENDERED (no meaningful narrative pathway, or explicit low-priority/plumbing-only design) · Prior-audit column cites the ratified edge-playability-audit (PR #81) finding where one already exists.

| Type | Family | §3.1 Tier-2? | §4.4 Tier-3? | Zoom-table correlate | Verdict | Deliberate-silent? | Status / prior audit |
|---|---|---|---|---|---|---|---|
| scene.dialogue | scene_event | No | No | No | RG | UNDETERMINED | NEW |
| scene.witness | scene_event | No | No | No | RG (feeds scar/memory) | UNDETERMINED | NEW |
| scene.gift | scene_event | No | No | No | RG | UNDETERMINED | NEW |
| scene.insult | scene_event | No | No | No | RG | UNDETERMINED | NEW |
| scene.threat | scene_event | No | No | No | RG | UNDETERMINED | NEW |
| scene.thread_operation | scene_event | No | No | No | RG, thin [STUB] | DELIBERATE (ED-936) | KNOWN-TRACKED |
| scene.draft_da | scene_event | No | No | No | RG, thin [STUB] | UNDETERMINED | NEW |
| scene.displacement | scene_event | No | No | No | RG, thin [STUB] | UNDETERMINED | NEW |
| scene.interaction (Class B) | scene_event | No | No | No | UR — near-zero (stakes 0-1, hard-coded `private_observers`) | Partially deliberate; overall NOT-INTENDED | **KNOWN-TRACKED (EP-7)** |
| scene.gossip (Class B) | scene_event | No | No | No | RG (stakes 1, escalates on propagation) | Partially deliberate | **KNOWN-TRACKED (EP-7)** |
| da.public_governance | da_outcome | No | No | No | RG | UNDETERMINED | NEW |
| da.covert_betrayal | da_outcome | **Yes (#5, exposed=true only)** | No | No | RR conditional / near-invisible when exposed=false | DELIBERATE for the visibility split; NOT-INTENDED overall (no counter-play) | **KNOWN-TRACKED (EP-6)** |
| da.diplomatic_alliance | da_outcome | No | **Yes** ("treaties", §4.4 item 1) | Correlate: "Treaty Proposed or Broken" §4.3.3 | RR at Tier-3 only | UNDETERMINED | NEW |
| da.antinomian_action | da_outcome | No | No (despite own notes: "major...contribution to significance") | No | RG | UNDETERMINED | KNOWN-TRACKED (EP-6) |
| da.economic_intervention | da_outcome | No | No | No | RG / near-invisible (nominal consumer settlement_economy is a phantom) | UNDETERMINED | KNOWN-TRACKED (EP-6) |
| mechanical.season_change | mechanical_event | No | No (temporal spine, not content) | No | UR, plumbing | DELIBERATE | NEW |
| mechanical.accounting | mechanical_event | No | **MECHANISM** — fires Tier 3 itself (annual==true), not rendered as content | No | UR-as-content / mechanism-critical | DELIBERATE | NEW |
| mechanical.cascade_resolution | mechanical_event | No | **Yes** ("Cascade fidelity trajectory") | No | RR at Tier-3 only | UNDETERMINED | KNOWN-TRACKED (cluster_G) |
| mechanical.mission_shift | mechanical_event | **Yes (#4)** | **Yes** ("Mission progress") | No | RR | — | KNOWN-TRACKED (cluster_G) |
| mechanical.scene_entered | mechanical_event | No | Pacing-only ("may consume for Tier 3 pacing analysis" — not content) | N/A, self-referential | UR-as-content | DELIBERATE (explicit no-wall-clock-in-payload) | NEW |
| mechanical.scene_exited | mechanical_event | No | Pacing-only | N/A | UR-as-content | DELIBERATE | NEW |
| mechanical.scene_skipped | mechanical_event | No | No — consuming_systems=[scene_timer, audit] only, **not even articulation** at the per-type level | No | UR | DELIBERATE (explicit telemetry-only) | NEW |
| mechanical.project_advanced | mechanical_event | No | No | No | RG | UNDETERMINED | NEW |
| state.scar_acquired | state_transition | **Yes (#1)** | Implied ("Notable individuals") | Correlate: NPC Conviction Crisis §4.3.3, Knot Partner in Crisis §4.3.2 | RR | — | KNOWN-TRACKED (cluster_G) |
| state.standing_change | state_transition | **No** (despite `trigger` enum including `death`) | No | Correlate: "Rank Advancement Recognition Event" §4.3.2 (rising rank only, not death/demotion) | UR — no trigger at all | UNDETERMINED | **KNOWN-TRACKED (F-B/EP-3)** |
| state.coup_attempted | state_transition | **Yes (#2)** | Implied | Correlate: Faction Leader Removal §4.3.2 | RR | — | KNOWN-TRACKED (cluster_G) |
| state.succession | state_transition | **Yes (#3, non-routine modes only)** | **Yes** ("succession events") | Correlate: Faction Leader Removal §4.3.2 | RR (routine excluded) | DELIBERATE (stated rationale) | KNOWN-TRACKED (cluster_G / F-F) |
| state.project_completed | state_transition | No | No | No | RG | UNDETERMINED | NEW |
| state.project_failed | state_transition | No | No | No | RG | UNDETERMINED | NEW |
| state.opinion_revised (Class B) | state_transition | **No** — despite its own registry description claiming "Drives Articulation Tier 2 trigger evaluation" (L923-940) | No | No | RG, **internally contradicted** | UNDETERMINED (looks like doc drift) | **NEW** |
| state.concern_resolved (Class B) | state_transition | No | No | No | UR-ish, near-zero (stakes 1-2, private_observers) | UNDETERMINED | NEW |
| env.peninsular_strain_shock | environmental | **Yes (#8, severe/crisis only)** | **Yes** | Correlate (weak): Warden Emergency §4.3.3 | RR conditional; mild/moderate excluded | DELIBERATE (severity gate) | KNOWN-TRACKED (cluster_G) |
| env.crisis | environmental | **No** | **Yes** | No clean correlate | RR at Tier-3 only (annual latency) | UNDETERMINED | **KNOWN-TRACKED (F-D/EP-3)** |
| env.disaster | environmental | No | No (not named; only crisis + strain_shock named) | No | RG, no chronicle slot | UNDETERMINED | KNOWN-TRACKED (cluster_G) |
| env.population_change | environmental | No | No | No | RG, likely pure noise | UNDETERMINED | NEW |
| scene.contest_resolved | scene_outcome | No | No | No | UR at Tier-2 | UNDETERMINED | KNOWN-TRACKED (cluster_G) |
| scene.battle_concluded | scene_outcome | **No** (§6.4 falsely claims yes) | No (not named; "per-faction movements" could sweep it) | Correlate: Mass Battle at Settlement §4.3.2 (precursor), Territory Control Change §4.3.3 (via `territorial_outcome`) | UR at Tier-2, self-contradicted | NOT-INTENDED | **KNOWN-TRACKED (F-A/F-4, RATIFIED)** |
| scene.investigation_resolved | scene_outcome | No | No | Correlate (weak): Heresy Investigation Target §4.3.2 (precursor only) | UR at Tier-2 | UNDETERMINED | KNOWN-TRACKED (F-4/EP-3) |
| scene.combat_resolved | scene_outcome | **No** in the table itself (§6.4 grants "by default", `[ASSUMPTION]`-tagged) | No | No | UR at Tier-2, aspirational only | NOT-INTENDED (self-contradiction) | KNOWN-TRACKED (F-A/EP-3) |
| scene.combat_strike | scene_outcome | No | No | No | UR, intra-engine input | DELIBERATE | NEW |
| scene.combat_hit | scene_outcome | No | No | No | UR, intra-engine plumbing (consuming_systems=[personal_combat] only) | DELIBERATE | NEW |
| scene.combat_felled | scene_outcome | No — no §6.4 grant either, despite "ripples...into NPC memory" framing | No | No | UR, not even aspirational | UNDETERMINED | KNOWN-TRACKED (cluster_G, explicit row) |
| meta.knot_formed | system_meta | **Yes (#6)** | **Yes** | Correlate: Knot Partner in Crisis | RR | — | KNOWN-TRACKED (cluster_G) |
| meta.knot_ruptured | system_meta | **Yes (#7)** | **Yes** | Correlate | RR | — | KNOWN-TRACKED (cluster_G) |
| meta.thread_woven | system_meta | No | No (only Knot/Belief named) | No | RG, weakest per F-F (no stakes/causes field) | DELIBERATE per ED-936, but flagged UNDETERMINED-quality by F-F | KNOWN-TRACKED (F-F/cluster_G) |
| meta.miraculous_event | system_meta | **No** — despite own notes: "Always indelible... Always public-visible... High significance contribution" | No (not named; thematically closest to §4.4 item 1 but absent) | No | RG despite self-described maximal significance | UNDETERMINED | **NEW** |
| state.belief_revised | system_meta (filed) | **Yes (#10)** | **Yes** ("Belief revisions") | No | RR | — | KNOWN (primary-source, articulation doc itself) |
| meta.legacy_event | system_meta | No | No | No | UR | DELIBERATE (explicit "pruned once migration completes" wrapper) | NEW (uncontroversial) |
| *(reverse case)* meta.cascade_cluster_event | cited by §3.1 trigger #9 | **cited, but type_id absent from registry §2-§8 entirely** | — | — | N/A — unregistered | NOT-INTENDED (§10 Extension Process not followed) | **NEW — see C-KEY-8** |

**Cross-check against the ratified "10-of-44" figure (EP-3):** counting only literal §3.1 table rows, exactly **9 registered types** get a dedicated Tier-2 hook (scar_acquired, coup_attempted, succession, mission_shift, covert_betrayal, knot_formed, knot_ruptured, peninsular_strain_shock, belief_revised) plus **1 phantom row** citing an unregistered type (cascade_cluster_event) = "10 rows." This independently reproduces EP-3's ratified figure exactly, which cross-validates this sweep's method.

---

## Findings (C-KEY-1..9)

**C-KEY-1 · Silent-doc/populated-contract is a corpus-wide pattern, not two isolated cases** · P2 · NEW (generalization; the 2 named instances are individually KNOWN-TRACKED as EP-4/EP-5)
Of 19 checked modules, 9 have zero native "emit"/Key-type language in their canonical doc (index+infill checked where co-filed) — 6 of these (piety_track, threadwork, social_contest, mass_battle, peninsular_strain, miraculous_event) nonetheless carry non-empty `emits:` in `module_contracts.yaml`, extracted purely from substrate/registry cross-reference and never validated against the doc's own prose. EP-4 (settlement_layer) and EP-5 (ci_political) are the two examples already ratified; the other 7 share the identical structural pattern and are not individually tracked anywhere. Evidence: `references/module_contracts.yaml` L198-341, L425-535, L727-742; zero-hit greps against `designs/personal/conviction_track_v1.md`, `designs/threadwork/threadwork_v30.md`(+infill), `designs/scene/social_contest_v30.md`(+infill), `designs/provincial/mass_battle_v30.md`(+infill), `designs/provincial/peninsular_strain_v30.md`, `designs/scene/miraculous_event_v30.md`.

**C-KEY-2 · npc_behavior's `doc:` field cites a Key-silent doc; the real spec is an uncited co-file** · P3 · KNOWN-UNTRACKED (underlying consolidation is gap-noted; this specific emit-clause-coverage risk framing is not)
`module_contracts.yaml` L107 cites `designs/npcs/npc_behavior_v30.md` (0/0 for emit/Key), while the module's actual native Key-sequencing spec lives in `designs/provincial/political_dynamics_keys_migration_v30.md` (61/66 hits), named only under `sources:` (L173), not `doc:`. A future edit to "the npc_behavior doc" would very plausibly target the wrong file. Evidence: `references/module_contracts.yaml` L105-176.

**C-KEY-3 · personal_combat's internal trace-event vocabulary is never reconciled with its Key-type vocabulary** · P2 · NEW
`combat_engine_v1/wrapper.py`/`state_graph.py` define ~15-25 internal `_emit()` trace-event kinds (`engagement_start`, `commit`, `read`, `roll`, `contact`…) used for telemetry/probability tooling. Nowhere in the corpus is this vocabulary mapped to the 4 canonical `scene.combat_*` Key types, whose `.tres` declarations live only in `designs/godot/skeleton/data/key_types/`, external to the doc the contract cites. Evidence: `designs/scene/combat_engine_v1/wrapper.py` L9-136 (`_emit` definitions), `state_graph.py` L9-39 (`emits:` node metadata); `designs/godot/skeleton/data/key_types/scene_combat_hit.tres`.

**C-KEY-4 · §12.4's four down-seam families have no runtime substrate to populate targets[]/stat_deltas into** · P2 · KNOWN-TRACKED (evidence reinforcement of the already-open D.4/D.6 worklist), with a new empirical datum
`grep -rl "stat_deltas" sim/ --include=*.py` returns zero files; no `class Key` exists in `sim/`; 3 of the 4 emitter families (domain_actions, faction_politics, scenario_authoring) have `doc: null`; the 4th's home doc (`peninsular_strain_v30.md`) scores zero hits for targets[]/scale_signature/stat_deltas too. Evidence: `designs/architecture/propagation_spec_v1.md` §3 D.4 (L228-239); `designs/architecture/scale_transitions_v30.md` §12.3-§12.4 (L323-332); grep results above.

**C-KEY-5 · causes[] authoring guidance exists in exactly one canonical doc corpus-wide** · P2 · KNOWN-TRACKED (charter's own Gap class 2; key_substrate_v30's self-reported 15% figure)
Only `political_dynamics_keys_migration_v30.md` gives emitter-side causes[] guidance; none of the four §12.4 families' docs do. `key_substrate_v30.md` L357 self-reports ~15% causes[] population in production. Evidence as cited in Part 2.

**C-KEY-6 · Six type-edges registry-declares npc_behavior as consumer, absent from its contract `consumes:` list; npc_behavior's own gap_note is now stale** · P2 · NEW
`scene.thread_operation`, `scene.draft_da`, `scene.displacement`, `mechanical.project_advanced`, `state.project_completed`, `state.project_failed` are all registry-declared consumed by npc_behavior (4 of these being self-loops on its own emissions) but absent from its `consumes:` list. npc_behavior's gap_note (L168) claims "the registry lacks" these types — falsified by ED-935 having since registered them (registry §9, L1022). Evidence: full cross-check in Part 3; `references/module_contracts.yaml` L110-133 (consumes list) vs L134-145 (emits list) vs L168 (stale gap_note); `designs/architecture/key_type_registry_v30.md` L1022.

**C-KEY-7 · scene.thread_operation, scene.draft_da, scene.displacement payloads and (from C-KEY-6) their consumer wiring are simultaneously [STUB]-flagged and consumer-orphaned** · P3 · KNOWN-TRACKED (payload-stub half; consumer half is C-KEY-6/NEW)
Noted as a compounding observation, not a separate root cause — see registry `[STUB]` markers at L145, L162, L180 plus C-KEY-6.

**C-KEY-8 · articulation §3.1 trigger #9 cites an unregistered Key type** · P2 · NEW
`meta.cascade_cluster_event` (articulation_layer_v30.md L91, trigger #9) does not appear anywhere in `key_type_registry_v30.md` §2-§8 — a CANONICAL trigger spec depends on a type that was never entered per §10's own Extension Process (step 2: "Append entry to this registry"). Grepped the corpus for prior flags of this specific absence; none found. Evidence: `designs/articulation/articulation_layer_v30.md` L77-112; `designs/architecture/key_type_registry_v30.md` (zero hits for "cascade_cluster_event" across all of §2-§8); §10 process at L1026-1035.

**C-KEY-9 · The exhaustive 48-row sweep confirms the pattern cluster_G anticipated but did not execute, at comparable severity, across ~30 unexamined rows** · P1/P2 (recommend Fable set tier; flagging two sub-items as comparable to existing P2s) · NEW (rows), pattern itself KNOWN
cluster_G_rendering.md's own closing line predicts exactly this: "the trigger table was built sim-first around the 8–10 cases Stage 10 measured, not swept exhaustively against the full 44-type registry." This sweep executes that. Two sharpest new sub-findings: (a) **the entire scene_event "core five"** (`scene.dialogue/witness/gift/insult/threat` — the highest-frequency interaction types in the whole registry) have zero dedicated Tier-2 or Tier-3 pathway, generic-significance-only; (b) **`state.opinion_revised`'s own registry description** ("Drives Articulation Tier 2 trigger evaluation," L923) is **contradicted** by its literal absence from the §3.1 table — structurally the same shape as the already-P2-rated §6.4/battle_concluded contradiction (F-A), but on a different, previously-unflagged type; (c) **`meta.miraculous_event`** is self-described as maximal-significance/"always public-visible" yet has no dedicated pathway at either tier. Evidence: full Part 4 table above.

**C-KEY-10 · Zoom-trigger tables and the Key-type registry are textually disconnected** · P3 · NEW
No row in `scale_transitions_v30.md` §4.3.2/§4.3.3 cites a registered Key `type_id`; all correlations in Part 4's "Zoom-table correlate" column are inferred from condition-text/payload-field similarity, not canon citation. This means nothing in the corpus lets a reader or validator mechanically confirm that a Zoom trigger and its semantically-adjacent Key type actually fire in the intended relationship. Evidence: `designs/architecture/scale_transitions_v30.md` §4.3.2 (L125-140), §4.3.3 (L142-152) — zero `type_id`-shaped strings in either table.

---

## Honest gaps

- **Infill coverage is not exhaustive.** I checked index+infill siblings for the docs I found silent (conviction_track_v30, threadwork_v30, social_contest_v30, mass_battle_v30, victory_v30 all confirmed 0/0 in infill too), but did not re-verify every co-filed pair in the corpus for a possible emit-clause hiding only in an infill I didn't think to check.
- **Grep-based methodology has a false-negative risk.** A doc could describe Key emission without using the literal words "emit" or "Key" (e.g., "fires a state-transition event"). I spot-checked near-misses (mass_battle's "engine emits an incapacitated/captured state") and found they name no type_id even when phrased close to a Key clause, but did not re-read every doc word-by-word beyond grep+targeted context.
- **combat's 9 PENDING action modules** (feint, bind, approach, displace, grapple, halfsword, initiative, poise, armour_defeat — module_contracts.yaml L830-838) have no Key-type declarations to check at all yet; C-KEY-3's finding covers only the 2 PORTED sub-modules.
- **Part 4's Zoom-correlate column is inherently interpretive** (see C-KEY-10) — treat my Yes/Partial/No calls there as lower-confidence than the literal-string Tier-2/Tier-3 columns.
- **Single-pass, no independent re-verification.** Per the charter's relay pattern, citations here should get a refuter pass before being treated as settled; I did not re-verify every line-number citation a second time.
- **Part 3's cross-check trusts the registry's `consuming_systems` field as ground truth** and checks contract `consumes:` against it one-directionally; I did not separately audit the reverse (contract `consumes:` entries with no registry backing at all), which was outside the charter's ask but could surface over-declaration.
- I did not attempt to adjudicate whether any of the KNOWN-TRACKED findings I re-cite (EP-3/4/5/6/7, F-A..F-G, F-4) remain accurately characterized post-ratification — I'm relying on the 2026-07-05 `edge_playability_audit_v1.md` text as-merged.
