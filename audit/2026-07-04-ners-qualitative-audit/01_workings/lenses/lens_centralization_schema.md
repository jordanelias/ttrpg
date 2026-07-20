# Lens: centralization_schema — working notes

Definitional infrastructure as a system. Question: where is the SAME concept defined more than
once and diverges; is it single-sourced; what home + enforcement; grade cohesiveness.

## Infrastructure inventory (the intended single-source homes)

- **names_index.yaml** — self-declared "the one place a definition's name lives." Read by
  tools/names.py → ci_naming_check (block), ci_names_check (warn drift), valoria_rename (executor),
  ci_names_consistency (mirror check). Mirrors: attr/agg/fac/set → descriptor_registry;
  world.* → proper_noun_registry. Mechanic/clock legacy → drift-lint only.
- **descriptor_registry.yaml** — single source for descriptors (attributes/aggregates/faction/
  settlement stats). 9-attribute roster (3 body/3 mind/3 social), self-marked IN FLUX.
- **glossary.md** — self-declared "canonical reference for all term expansions project-wide." NOT
  in the names_index mirror set → not consistency-checked. This is the systemic crack.
- **values_master.yaml** — QUARANTINED (ED-1084), auto-extract dead. Ignore.
- **references/engine_params/combat_engine_v1.json** — the ONE typed export (ED-1052). 26 other
  modules prose-only.

## Divergence candidates (verified)

### 1. Attribute roster — TWO naming authorities contradict [NEW, P2]
- glossary Part One "Core Attributes" = 7 rows, scale 1-7: Agility, Attunement, **Cognition**,
  Endurance, **Presence**, **Spirit**, Strength. No Focus, no Bonds.
- descriptor_registry attributes + names_index attr.* = 9: body{Strength,Endurance,Agility},
  mind{Focus,**Acuity**,**Will**}, social{Attunement,**Charisma**,**Bonds**}. Here Cognition is an
  *alias* of Acuity; Presence alias of Charisma; Spirit alias of Will.
- So the two files that each self-declare naming authority disagree on (a) the count (7 vs 9) and
  (b) which name is canonical (glossary: Cognition/Presence/Spirit canonical; names_index: those are
  aliases, Acuity/Charisma/Will canonical). descriptor_registry IS flagged IN FLUX (KNOWN, CLAUDE.md
  §5) — but the glossary-vs-registry *contradiction on canonical names* is the new scope.
- Propagation: mass_combat Command formula (glossary line 119, PP-232) = "⌈(Presence+Cognition)/2⌉"
  — prose formulas are written against the LEGACY attribute names. If the 9-roster is canonical, live
  formulas cite alias names.

### 2. resonance_style DEPRECATED vs Resonant Style LIVE-CENTRAL [NEW, P2]
- descriptor_registry §deprecated (line 100): resonance_style "Was the 'most-persuasive mode of
  argument'. Superseded by contest_style + Conviction-driven interpretation... Retired 2026-06-06."
- npc_behavior_v30.md §1.3 "Resonant Style Taxonomy" — LIVE, central: "Resonant Style | the NPC is
  vulnerable to" gates every named-NPC contest-targeting AI decision (Primary/Secondary per NPC).
  Same concept ("most-persuasive mode"). Registry says retired/superseded; the mechanic is live and
  load-bearing. A Godot importer trusting the registry treats a live gating mechanic as dead.

### 3. MS vs RS — single-source home exists but warn-tier; drift survives [KNOWN-TRACKED, P2]
- names_index HAS clock.mending_stability {legacy: ["Rendering Stability"], enforce: warn}. So the
  every-rule-lives-once home + drift-lint EXIST.
- Yet params/threadwork.md reads RS canonically throughout ("## RS Track (PP-603 — canonical)",
  "RS = 0: Rupture", 20+ hits), while glossary Part Two + threadwork_v30 §5 use MS. Same track.
- New scope for this lens: the machinery that should catch it is registered but NON-BLOCKING
  (warn), so the ED-731/772 sweep never reached params/threadwork.md and the lint doesn't force it.
  Tracked: ED-428/731/772, threadwork dossier ms-rs-split-live.

### 4. glossary is an un-mirrored third naming authority [KNOWN-UNTRACKED, P2 — systemic root]
- ci_names_consistency checks descriptor_registry + proper_noun_registry against names_index. It does
  NOT check glossary.md. glossary self-claims "canonical reference for all term expansions" (line 4)
  yet is outside the mirror gate → free to drift (this is WHY #1 persists).
- Root of the centralization failure: three authorities (names_index, descriptor_registry, glossary),
  only two wired together.

### 5. Prose-params → one-typed-export gap [KNOWN (CLAUDE.md §5), P2 forwards/Godot]
- references/engine_params/ contains ONLY combat_engine_v1.json. 26 other modules have no typed
  export. Cost to the Godot goal: every non-combat value crossing into Godot is hand-transcribed,
  no round-trip CI check outside combat (CLAUDE.md §5 "recommended, not yet built").

### 6. Enforcement almost entirely warn-tier [NEW, P3]
- names_index: only world.solmund (Galbados) is enforce:block. Every attribute/faction/settlement
  stat, every clock (incl. MS/RS), every mechanic rename = enforce:warn. The Godot-load-bearing
  names have no hard gate; drift persists by construction (see #1, #3).

### 7. conviction_track stem collision [KNOWN-TRACKED, P3]
- designs/personal/conviction_track_v1.md (personal per-Conviction Scars) vs
  designs/scene/conviction_track_v30.md (per-territory Piety BG stat) — unrelated mechanics sharing a
  stem; the version suffix reads as supersession, not "different mechanic." mechanics_index already
  miscited the wrong one (npc dossier mechanics-index-wrong-file). Schema hazard: stem+version-suffix
  can't distinguish newer-version from different-concept. glossary Part Three maps Piety Track→v1.

### 8. glossary CI entry internally garbled [NEW, P3]
- Line 23: "**CI is no longer used** — ... Church Influence (renamed to Church Influence / CI per
  ED-782) ... Use `CI` for the Church clock; write `Piety Track` in full elsewhere." Self-contradictory
  ("no longer used" then "use CI for the Church clock") and "renamed to itself." The naming authority
  is incoherent on its most collision-prone abbreviation.

## Non-divergence verified (charter instruction)
- **Combat Pool RECONCILED**: params/core.md line 161 = max(5, Relevant History + 6); module_contracts
  line 801 = pool=max(5,History+6). The two LIVE sites AGREE (ED-901/900/904, ED-1084 propagation).
  The struck (Agility×2)+History+3 form survives only in QUARANTINED values_master + KNOWN-stale
  carriers (mechanics_index, sim/personal/combat.py, data_serialization_spec — all enumerated in
  module_contracts line 841). So NOT a live divergence — the single-sourcing worked. Residual stale
  carriers are a Godot drift surface but KNOWN-TRACKED.

## Single-source verdict (every-rule-lives-once for definitions)
- HOME: names_index.yaml is the correct home and is well-designed (mirror + rename executor + 4
  readers). Fixes: (a) fold glossary attribute/stat/clock names into the ci_names_consistency mirror
  set — or generate the glossary tables FROM names_index; (b) flip Godot-load-bearing entries
  (attributes, MS/RS) warn→block once triaged; (c) reconcile descriptor_registry's resonance_style
  deprecation against npc_behavior's live Resonant Style (they are the same concept).
- COHESIVENESS GRADE: **MODERATE-WEAK.** Not an absence-of-infrastructure problem — the machinery is
  unusually good — but undermined by (i) near-total warn-tier enforcement, (ii) an un-mirrored third
  authority (glossary) that has drifted on the attribute roster, (iii) a registry deprecating a live
  concept, (iv) a registered lint (MS/RS) its own drift survives. The single-source design is sound;
  the binding is loose.
