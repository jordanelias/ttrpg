<!-- [PROVISIONAL: 2026-05-01 — PP-686 v2 Phase B Stage 5: per-faction state authoring] -->
<!-- STATUS: PROVISIONAL — Class A authoring document. Authors Mission + organizational_hierarchy reference + institutional_culture for the 6 canonical factions. Cross-references faction_politics_v30 §1.1d/§1.2c/§1.3c/§1.4c for full org_hierarchy graphs. -->
<!-- AUTHORITY: PP-686 v2 (faction_behavior_v30.md §3) -->

# Faction State Authoring (PP-686 v2 Phase B Stage 5)

## §1 Purpose

PP-686 v2 §3 specifies a 4-component faction state schema: Mission, Cascade, Public Expectation, and Legitimacy + Popular Support. Stage 5 authors the per-faction values that the engine reads at scenario init.

This document covers the 6 canonical factions: Crown, Church of Solmund, Hafenmark, Varfell, Restoration Movement, Löwenritter.

**Authority cross-reference:** `designs/provincial/faction_politics_v30.md` §1.1d through §1.4c contains the canonical Inner Circle Named NPC rosters. This Stage 5 doc references those sections for `organizational_hierarchy.nodes` rather than duplicating; the hierarchy graph itself remains in faction_politics_v30 as the single source of truth.

**What this doc adds beyond faction_politics_v30:**
- `mission` spec per faction (text, primary_objective, beneficiary, aligned/contradicted DA categories)
- `institutional_culture` scalar per faction
- `cascade_roots` declaration (multi-root vs single-root per faction structure)
- `role` mapping to PP-686 §3.3.1 role templates

---

## §2 Crown — Sovereign

```yaml
faction: crown
role: sovereign
mission:
  text: "Restore and maintain Peninsular Sovereignty under the Almqvist dynasty"
  primary_objective: victory.peninsular_sovereignty   # per victory_v30 §3.1
  beneficiary: populace_of_valoria                    # the Realm itself
  aligned_categories:
    - da.public_governance              # public administration is core role
    - da.diplomatic_alliance            # treaties advance sovereignty
  contradicted_categories:
    - da.covert_betrayal                # the Almqvist code is honor-bound
    - da.antinomian_action              # contradicts sovereign role
  authored_at: 2026-05-01
  prior_mission: null

leader: almud                            # per sim continuity (sim §1.2)
                                         # Almud is canonical Crown Captain;
                                         # Torben Almqvist is heir apparent (per faction_politics §1.1d)

organizational_hierarchy:
  nodes_ref: "faction_politics_v30 §1.1d Crown Inner Circle Named"
  cascade_roots:
    - almud                              # secular governance root
    # Multi-root candidates (deferred to designer):
    # - theodor_kreutz                   # military root (Royal Guard / Löwenritter Liaison)
    # - gerik_strand                     # household / Lord Steward root
    # Per faction_behavior_v30 §3.2.2, multi-root recommended for Crown given
    # secular/military/household separation. Single-root currently used until
    # Stage 10 sim observes whether multi-root produces meaningful divergence.
  
institutional_culture: 0.0               # neutral default
                                         # Crown is hierarchical but not rigid;
                                         # neither Hafenmark-procedural-rigid nor
                                         # Restoration-permissive

cascade_roots_rationale: |
  Single-root used initially (almud only). Per spec §3.2.2, multi-root is
  recommended when faction has institutional sub-hierarchies that may cascade
  divergently. Crown has secular governance + military command + household;
  designer review at Stage 10 observation point may upgrade to multi-root if
  cascade fidelity drift between branches becomes load-bearing.
```

---

## §3 Church of Solmund — Ecclesiastical

```yaml
faction: church_of_solmund
role: ecclesiastical
mission:
  text: "Establish Solmundan Orthodoxy across the peninsula"
  primary_objective: victory.solmundan_orthodoxy       # per victory_v30 §3.2 (CI=100 Mass Seizure path)
  beneficiary: populace_of_valoria                     # the faithful
  aligned_categories:
    - da.public_governance              # CI Suppression, doctrinal acts
    - da.diplomatic_alliance            # ecclesiastical alliances (Altonia)
  contradicted_categories:
    - da.covert_betrayal                # public orthodoxy means visible action
    - da.antinomian_action              # heresy is the antithesis
  authored_at: 2026-05-01
  prior_mission: null

leader: cardinal_himlensendt             # per faction_politics canon — Himlensendt
                                         # is canonical Church leader (per
                                         # params/bg/core.md L233 "Church
                                         # (Himlensendt)")
                                         # Sæmund Haelgrund (Inquisitor) and
                                         # Aldric Tormann (Prudence) are
                                         # subordinate cardinals.

organizational_hierarchy:
  nodes_ref: "faction_politics_v30 §1.4c Church Consecration; worldbuilding_v30 §3.1 Four-Cardinal structure"
  cascade_roots:
    - cardinal_himlensendt               # institutional root
    # Multi-root candidates (canonical structure):
    # - cardinal_temperance               # Altonian diplomacy advancement track
    # - cardinal_justice                  # inquisitorial arm (Sæmund Haelgrund)
    # - cardinal_fortitude                # military arm
    # - cardinal_prudence                 # Aldric Tormann
    # Four-Cardinal multi-root supported by worldbuilding canon. Defer to
    # designer review whether to enable as initial state.
    
institutional_culture: -0.1              # mildly rigid (Faith + Precedent
                                         # cultural template)

cascade_roots_rationale: |
  Single-root initially (cardinal_himlensendt). Four-Cardinal structure is
  canonical and supports multi-root upgrade if Stage 10 sim shows that the
  Cardinals' independent action produces diverging cascades. Most Church DAs
  flow through institutional consensus, so single-root is conservative default.
```

---

## §4 Hafenmark — Mercantile-Procedural

```yaml
faction: hafenmark
role: mercantile-procedural
mission:
  text: "Establish Dynastic Assertion of the Hafenmark Constitutional Duchy"
  primary_objective: victory.dynastic_assertion        # per victory_v30 §3.3
  beneficiary: hafenmark_burgher_class
  aligned_categories:
    - da.public_governance              # parliamentary/procedural acts
    - da.economic_intervention          # core competence
    - da.diplomatic_alliance            # mercantile ties
  contradicted_categories:
    - da.antinomian_action              # rule-breaking contradicts core identity
    # da.covert_betrayal: ambiguous for Hafenmark — Spymaster operates covertly
    # by mandate. Not contradicted; neutral.
  authored_at: 2026-05-01
  prior_mission: null

leader: baralta                          # per params/bg/core.md L233 canonical
                                         # leader. Baralta in PP-685 migration
                                         # roster has Faith/Virtue/Warden primary,
                                         # ecclesiastical cultural background.
                                         # Note: Baralta-as-Hafenmark-leader
                                         # potentially flagged in
                                         # designs/provincial/baralta_crown_claim_v30
                                         # — verify at Stage 10.

organizational_hierarchy:
  nodes_ref: "faction_politics_v30 §1.2c Hafenmark Inner Circle Named"
  cascade_roots:
    - baralta                            # institutional/parliamentary root

institutional_culture: -0.2              # rigid — procedural-mercantile culture
                                         # is most rigid of the 6 factions
                                         # (per faction_behavior §3.2.3)
```

---

## §5 Varfell — Military-Order

```yaml
faction: varfell
role: military-order
mission:
  text: "Establish Southernmost Dominion through military conquest"
  primary_objective: victory.varfell_path_b            # per victory_v30 §3.4
                                                       # (Path A intelligence
                                                       # hegemony alternative;
                                                       # Path C struck per PP-663)
  beneficiary: varfell_huscarls + alpine_population
  aligned_categories:
    - da.public_governance              # martial governance is public role
    - da.economic_intervention          # tribute and conscription
  contradicted_categories:
    - da.antinomian_action              # contradicts military Honor code
    # da.covert_betrayal: Varfell does have intelligence operations (Path A),
    # so not strictly contradicted. Neutral.
    # da.diplomatic_alliance: Varfell allies pragmatically; neutral.
  authored_at: 2026-05-01
  prior_mission: null
  notes: |
    Per PP-663, Varfell Path C struck (Cultural Reformation removed). Path A
    (Intelligence Hegemony) and Path B (Southernmost Dominion) remain.
    Default Mission is Path B (military conquest), most aligned with Varfell's
    canonical character per Reinhardt von Lohengramm parallel.

leader: vaynard                          # canonical apex
                                         # Maret Uln (Huscarl Captain, PP-685)
                                         # is succession fallback.

organizational_hierarchy:
  nodes_ref: "faction_politics_v30 §1.3c Varfell Inner Circle Named (Hochjarl + Senior Jarls)"
  cascade_roots:
    - vaynard                            # apex
    # Multi-root candidates (oral-law confederacy structure):
    # - thorvald_hann                    # Eastern March Senior Jarl
    # - bjorn_holdar                     # Western Highlands Senior Jarl
    # - ingrid_stenskald                 # Skald-Chief (cultural memory)
    # The Jarl Confederacy is structurally multi-root in canon
    # (per faction_politics §1.3a Hochjarl Incapacity); designer should
    # consider enabling multi-root at Stage 10.

institutional_culture: -0.1              # mildly rigid (military-order
                                         # discipline) but Confederacy
                                         # structure has slack vs Hafenmark
```

---

## §6 Restoration Movement — Reformist

```yaml
faction: restoration_movement
role: reformist
mission:
  text: "Establish Cultural Revolution through Communal Sovereignty"
  primary_objective: victory.cultural_revolution      # per victory_v30 §3.5
                                                       # (5-player only, hardest mode)
  beneficiary: alpine_communal_polities
  aligned_categories:
    - da.economic_intervention          # community-level economic acts
    # public_governance: ambiguous for RM — they reject formal sovereignty
    # in favor of communal sovereignty. Not aligned.
  contradicted_categories:
    - da.public_governance              # formal sovereignty contradicts
                                        # communal-sovereignty principle
    - da.diplomatic_alliance            # formal alliances contradict communal
                                        # autonomy (RM operates via
                                        # Presence markers and Community Weaving
                                        # only — ED-589 / PP-460)
    # antinomian_action: ambiguous — RM may use antinomian acts as protest;
    # not strictly contradicted. Neutral.
  authored_at: 2026-05-01
  prior_mission: null
  notes: |
    RM is unusual: per PP-460, RM operates via Presence markers and Community
    Weaving only; no faction stats. PP-686 schema partially applies — Mission
    and Cascade are meaningful; Public Expectation reads against communal
    norms; Legitimacy + Popular Support track community-level acceptance
    rather than peninsula-wide.

leader: yrsa_vossen                      # per npc_roster #3 + PP-685 canonical

organizational_hierarchy:
  nodes_ref: "faction_politics_v30 (RM placement TBD per ED-589)"
  cascade_roots:
    - yrsa_vossen                        # singular apex; communal structure
                                         # below intentionally horizontal
    # Multi-root not used — RM ideology rejects hierarchy beyond loose
    # collective leadership.

institutional_culture: +0.1              # permissive — reformist movement
                                         # has slack (low alpha_institution
                                         # per faction_behavior §3.2.3)
```

---

## §7 Löwenritter — Military-Order

```yaml
faction: lowenritter
role: military-order
mission:
  text: "Preserve Valorian Sovereignty through Martial Discipline"
  primary_objective: victory.crown_peninsular_sovereignty   # serves Crown
                                                            # per Loyalty stage;
                                                            # shifts on Autonomy/Split
                                                            # via Graduated Autonomy track
  beneficiary: valorian_realm_continuity
  aligned_categories:
    - da.public_governance              # martial governance per Crown auth.
  contradicted_categories:
    - da.antinomian_action              # contradicts Honor code
    - da.covert_betrayal                # at Loyal/Restless stage — ironically
                                        # at Autonomous/Split, covert action
                                        # against Crown becomes mission-aligned;
                                        # see Mission shift triggers below.
  authored_at: 2026-05-01
  prior_mission: null
  notes: |
    Löwenritter Mission shifts on Graduated Autonomy track stage transitions.
    Per faction_behavior §3.1 D4 trigger 1 (victory milestone passes/fails)
    and trigger 2 (leader replacement under exceptional circumstances), each
    track stage transition (Loyal → Restless → Autonomous → Split) triggers
    Mission shift. Specifically:
    - Loyal: serve Crown peninsular sovereignty.
    - Restless: serve Crown but mission text shifts to "Preserve Valorian
      Sovereignty even at cost to Crown".
    - Autonomous: split mission — preserve Sovereignty independently.
    - Split: T14 becomes Löwenritter territory; Mission becomes
      Sovereign-territory-defense.
    These transitions emit mechanical.mission_shift Keys (PP-687 §4)
    automatically when Graduated Autonomy track advances.

leader: ehrenwall                        # canonical Grand Master
                                         # (per faction_politics §1.3c
                                         # disambiguation against Ingrid
                                         # Ehrenwall rename)

organizational_hierarchy:
  nodes_ref: "faction_politics_v30 §2.1 Löwenritter Knight Ladder + §2.2 Riskbreaker Ladder (covert sub-ladder)"
  cascade_roots:
    - ehrenwall                          # institutional root
    # Multi-root candidate:
    # - sigrid_torsvald                  # Riskbreaker covert sub-ladder root
    # Per §2.2 the Riskbreaker covert sub-ladder is structurally distinct;
    # multi-root is structurally justified for Stage 10 observation.

institutional_culture: -0.1              # mildly rigid (military-order
                                         # discipline; less rigid than
                                         # Hafenmark)
```

---

## §8 Initial Legitimacy + Popular Support Values

Per PP-686 v2 §4 (transitional retention) + Phase B Stage 3 (params/factions_personal.md):

```yaml
init_state:
  crown:           {Legitimacy: 5, Popular_Support: 5}
  church:          {Legitimacy: 5, Popular_Support: 5}
  hafenmark:       {Legitimacy: 4, Popular_Support: 4}
  varfell:         {Legitimacy: 4, Popular_Support: 4}
  guilds_npc:      {Legitimacy: 3, Popular_Support: 3}
  restoration:     {Legitimacy: 0, Popular_Support: 0}    # no Mandate; PS climbs from 0 via Mission outcomes
  lowenritter:     {Legitimacy: 0, Popular_Support: 0}    # no Mandate; embedded under Crown initially
```

Sourced from `params/bg/core.md §Faction Starting Stats` / `params/factions_personal.md §Starting Values` Mandate column. After first Accounting, faction_behavior_v30 §3.4–3.5 dynamics replace these seed values.

---

## §9 Open Items

| Item | Resolution |
|---|---|
| Multi-root cascade enablement per faction | Single-root default; designer review at Stage 10 sim observation |
| Crown vs Hafenmark leader disambiguation (Baralta) | Default per params/bg/core.md L233 (Baralta = Hafenmark); flag to designer for verification against `designs/provincial/baralta_crown_claim_v30.md` |
| RM faction stat applicability | Partial — Mission and Cascade meaningful; PE+L+PS scoped to community level |
| Vaynard succession-fallback Mission | Default Path B (Southernmost Dominion); Path A available at designer's authoring time |
| Löwenritter Mission shift on track transitions | Wired via `mechanical.mission_shift` Key emission (PP-687 §4); track-stage handler needs implementation in Phase B Stage 1 (doc 12 procedures) |
| Guilds NPC faction state | Stage 5 covers 6 player factions; Guilds NPC state covered via existing canon — no Mission spec at this layer |
| Niflhel | Removed per ED-764; not authored at this layer |

---

## §10 Sign-off

| Item | Status |
|---|---|
| Mission specs authored for 6 factions | YES — PROVISIONAL |
| organizational_hierarchy referenced (not duplicated) | YES — points to faction_politics_v30 §1.1d-1.4c, §2.1-2.2 |
| cascade_roots authored | YES — single-root default; multi-root candidates flagged |
| institutional_culture authored | YES — defaults per faction character |
| Init L+PS values | YES — sourced from Phase B Stage 3 params updates |

**Stage 5 closed:** PROVISIONAL pending Stage 10 sim verification + designer review of multi-root and Mission edge cases.

---

**End Stage 5 authoring. PROVISIONAL pending Stage 10 calibration.**
