# canonical_sources.yaml — provenance notes archive

Extracted 2026-05-30 to clear the `references/canonical_sources.yaml` 9,000-token `pre_commit_gate` ceiling (CSRC-SIZE-1, flagged across the 2026-05-30 resolution-diagnostic ratifications). These `note__*` / `note:` annotations are **decorative** — no hook parses them (the parser reads `design_doc`/`canonical*`/`canonical_sha__*`/`index`/`params` keys only). Preserved here verbatim; full detail also lives in commit messages and `designs/audit/2026-05-28-resolution-diagnostic/ledger_candidates_consolidated.json`. Git history preserves the originals in `canonical_sources.yaml` prior to this commit.

Extracted: 30 note line(s).

## designs/factions/faction_systems_overview_v30.md
- note: "Pass 2 follow-up. Single-pane reference cataloging ~50 faction-touched mechanics across 6 layers (primitives -> peninsular). Points at canon; does not duplicate. ~80% of Pass 2 forward-flags concentrate on faction surface."

## designs/audit/2026-05-17-v18-integration/integration_plan_v18.md
- note: "Pass 2m. Build roadmap mapping 72 sim/ modules to 12-phase implementation sequence with test plan + validation gates + dependency graph. 23 forward-flags accumulated for Pass 2k. v17→v18 migration discipline."

## designs/world/insurgency_pipeline_v30.md
- note: "ED-881 (2026-05-29): §6.2/§6.3 insurgency dissolution down-path ratified (4-path: military/sponsor-withdrawal/amnesty/persist), RAND-validated; closes GD-3 R-FAIL. Jordan-directed."
- note: "Pass 2i. GD-3 4-stage layered model: world PT decay → Latent RM → Insurgency → Promoted Faction. GD-1/2/3 cross-bindings. 7 forward-flags."

## designs/provincial/parliamentary_transfer_v30.md
- note: "Pass 2h. v12c §4.4 universal mechanic, validated_n1000_v12c. 4 modes; 8 CB sources. Wraps Parliamentary Vote contest. 3 forward-flags."

## designs/provincial/treaty_expiration_v30.md
- note: "Pass 2h. v12c §4.5 universal mechanic, validated_n1000_v12c, primary Crown-nerf. 90-95%/arc lapse. Re-bind via Senator Outward. 3 forward-flags."

## designs/personal/knots_v30.md
- note: "Pass 2g synthesis of Knot mechanic from 9 canon fragments. Forward-flags 3 contradictions to Pass 2k."

## designs/provincial/mass_battle_integration_v30.md
- note: "Pass 2n. Integration spec for porting sim_mb_06_v22 features. Does not supersede mass_battle_v30."

## designs/scene/combat_v30.md
- note: "ED-799 fix — design_doc updated from params/combat.md to designs/scene/combat_v30.md (section-structured doc). params/combat.md retained as params reference."

## designs/provincial/factions_personal_v30.md
- note: "ED-865/874 ext (2026-05-30): Treaty positioning+ratification (faction_layer §3.3) added to the resolver governed-checks list. Resolution-diagnostic ratification (CIP-1)."
- note: "ED-865/874 (2026-05-29): deterministic+stochastic resolver ratified as canonical Domain Action resolution; bare-stat-vs-Ob superseded for faction Domain Actions; bare-stat checks migrated (hooks preserved); dice systems unchanged. Jordan-directed."

## designs/world/geography_v30.md
- note: "geography_v30.md (atomized: index + infill) holds physical-geography canon — terrain regions, RS-band/node-distance matrix, 17-territory roster with starting control, fort levels, sub levels, adjacency. valoria_geography_v30.yaml + valoria_map_v30.svg are the structured/visual companions. Cited as source by sim_verification_ledger.json for territory IDs and counts."

## designs/provincial/faction_layer_v30.md
- note__fssloop: "FSS-LOOP-1/2+F2 2026-05-30 res-diag ratif: §1.4 determ Stab<=2 floor (supersedes Ob-4; GD-3 preserved); §5.7 Wealth>=1 Mil re-muster; F2 contested=tgt-stat/non=floor2+1. Detail: master _faction_layer_loop_ratifications_2026-05-30."
- note: "ED-865/874 ext (2026-05-30): §3.3 Treaty positioning (contested) + ratification migrated to the deterministic+stochastic resolver; Guarantor +1D->+1 M, Grand Debate degree->margin; Grand Debate social contest stays dice. §5.3 CI vote-contribution cross-ref added. Resolution-diagnostic ratification (CIP-1)."
- note: "ED-880 (2026-05-29): Varfell 'purely military' prose corrected to acknowledge Cultural Reclamation (Piety-alignment, non-military, VTM-free). VTM/Reformation stay struck; not a control transfer or victory path; sole victory remains Peninsular Sovereignty (GD-1). Authority unchanged."
- note: "ED-876 (2026-05-28): Trigger-5 Condition-C pool>=6 cliff removed from gate, retained as cost-table escalator. Authority unchanged; mechanical patch only."

## designs/provincial/ci_political_v30.md
- note: "CIP-1/2/3 (2026-05-30, resolution-diagnostic ratification): §3.2/§3.3/§3.4 CI political-forum weight made paradigm-consistent (Parliament tally vote-mod, floored at 0; resolver checks margin; no bonus dice). §2.2 Theocracy-Unification VICTORY struck per GD-1 (Mass Seizure = recoverable event). §4.2/§4.3 Govern/Trade annotated resolver-governed."
- note: "Renamed from tc_political_redesign_v30 — same doc, CI is Theocracy Counter's politically-active form."

## designs/provincial/peninsular_strain_v30.md
- note__pst1: "PST-1 (2026-05-30, resolution-diagnostic): §6.4 Post-Calamity (MS=0) forward-pointer to the ms_trajectory §5.1 leading warning. Verdict NERS-compliant after PST-1 (only S-consistency fix). All Strain/IP loops capped+damped; accumulators category-exempt."

## designs/scene/derived_stats_v30.md
- note: "PP-716, PP-717 — derived_stats_v30.md §4.1 is the authoritative source for Health formula (MW cap at 3) and wound-penalty universality. §14 (4-bucket taxonomy: Derived Values / Tracks / Clocks / Pools) is the authoritative engine-value map across canon docs (ED-830, 2026-05-15). §10.5 holds propagation timescales. §1 documents engine duality (Decision E ED-833, 2026-05-15): discrete and continuous engines are statistically equivalent specifications; params/core.md §Continuous Engine is the canonical spec. params/factions/stats_1_7_scale.md remains supplemental for faction-scale derived stats (Legitimacy/Popular_Support/Influence/Wealth/Military/Intel/Stability per PP-686 v2)."

## designs/provincial/faction_succession_split_v30.md
- note__fss1: "FSS-1 (2026-05-30, resolution-diagnostic ratification): §2.2 succession resolution split into two stages (Stage-1 contested resolver for WHO leads; Stage-2 deterministic strength-gap G for WHETHER it splits) — fixes the prior variance-driven structural fork (roll-margin<2 fragmented ~50% of near-peer successions regardless of power balance) + role-conflation. Split now tracks claimant power balance (Carolingian/Diadochi/Ottoman precedent), dice a bounded tail. Doc was PROVISIONAL/not-v12c-pinned (ratifiable). §3 example recomputed."

## designs/architecture/conflict_architecture_proposal.md
- note: "CANON 2026-04-18. Niflhel dissolution + Löwenritter graduated autonomy + Tensions Deck + Royal assassination fuse."

## references/throughlines_meta.md
- note: "Canonical vetting authority for all proposals (PP-672, PP-674)."

## designs/world/ms_trajectory_v1.md
- note__pst1: "PST-1 (2026-05-30): §5.1 ED-882 leading-warning window extended to the MS<=12 approach toward MS=0 (deepest tip; falling direction only). No new threshold. Resolution-diagnostic of peninsular_strain."
- note: "ED-882 (2026-05-29): §5.1 band hysteresis (recovery edges +8 above collapse) + leading warning signal (within 12 MS); Scheffer/Holling-validated; falling-direction unchanged. Jordan-directed."
- note: "Canonical for peninsula-wide Mending Stability values at specific historical dates. D-1 (12y emergence) + PR-3 (MS terminology) resolved 2026-04-20. Two provisional elements: colonial revolts §8 gap 1; Himmelenger R-7 §8 gap 2. ED-722/ED-731."

## canon/02_foundations_amendment_leap_mechanism.md
- note: "Canonical for Leap suspension dynamics, knot formation, and operation-type taxonomy (restorative/manipulative/destructive). Supplements canon/01 Amendments 1-4. ED-730."

## canon/01_foundations_amendment_self_rendering.md
- note: "Canonical for three-layer being-persistence, Leap definition, Coherence definition, Coherence 0 TS-gated outcomes."

## designs/provincial/faction_behavior_v30.md
- note__fsa1: "FSA-1 2026-05-30: §3.1 stale victory example fixed per GD-1."

## designs/provincial/faction_state_authoring_v30.md
- note__fsa1: "FSA-1 2026-05-30: §1 GD-1 note (primary_objective=approach not victory). NERS-compliant data doc."
