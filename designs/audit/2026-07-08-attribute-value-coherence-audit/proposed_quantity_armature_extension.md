# Quantity Armature Extension v1 — the stat layer under the seams

## Status: PROPOSED — held back from merge-ratification (ED-1094 exception, stated loudly:
## merging the audit PR does NOT ratify this document; it waits for the ed_options.md docket ruling)
## Date: 2026-07-08 · Lane: IN · ED anchor: ED-IN-0029
## Companion to: designs/architecture/key_echo_armature_v1.md (RATIFIED, ED-IN-0018)

The armature bound the **seams** (Key contracts, Echo Matrix, conformance checks A1–A16, shaping
waves 1–5). This extension binds the **quantities** those seams read and write — the stat names in
`stat_deltas`/`impact_vector`/`required_payload_fields`, `module_contracts.yaml` state/derivations,
`params/*.md` prose tables, sim/engine constants, and Godot exports. Silo-grown stat vocabularies
are shape divergence at the quantity layer (armature §1 guardrail; holonic doctrine ED-1083 §2) —
the same disease as the C-INJ-12 provenance-naming split the armature §2.4 unified.

Anatomy mirrors the armature: §1 the per-quantity contract row (armature §1 analog) · §2 registry
deltas (§3 analog) · §3 conformance checks (§4 analog, report-only → flip-on-zero-backlog) · §4 the
shaping-wave slot (§6.3 analog).

---

## §1 · The quantity-contract row (armature §1 analog)

Every quantity that crosses a module boundary, appears in a Key payload, or is transcribed into the
Godot port must satisfy one row of this format — the per-quantity analog of the seam-contract row.
The audit's census (`02_census/quantity_census.{yaml,md}`, 88 rows) **is** the seeded instance of
this table; the format below binds the census row schema as normative:

| field | meaning | closure criterion |
|---|---|---|
| `canonical_name` | the one primary name | resolves to exactly one registry key |
| `kind` | KIND taxonomy: `attribute_scalar` \| `attribute_aggregate` \| `faction_stat` \| `settlement_stat` \| the not_descriptors classes `derived_value` \| `track` \| `clock` \| `pool` \| `code_constant` | one kind, agreeing across registry / contracts `bucket:` / design doc — the C7-F2 Coherence case (registry absent / contracts pool / doc track / ED-830 ruled Track) is the canonical failure |
| `defining_surface` | the ONE authoritative file:line for the formula/scale | never `AMBIGUOUS`; all other carriers cite it (A18) |
| `formulas[]` | every live formula assertion with surface + provenance | exactly one non-superseded entry |
| `aliases[]` | registry-declared alternates, with **scope tags** for cross-domain bare-word reuse (C1-F11 "Influence") | no undeclared synonym in live prose |
| `registered` | `block` \| `warn` \| `not_descriptors` \| `unregistered` | nothing load-bearing at `unregistered`; A17 zero-backlog before any `warn`→`block` flip |
| `consumers[]` / `key_bindings[]` | who reads it; which Key payload / contract state / gate names it | no orphan (defined-unconsumed) and no gate-only phantom (consumed-undeclared: cumulative_drift F-C-004, Fort Level F-C-007) |
| `scale_bounds` | scale + floors/ceilings, **per-entry** (C5-F3: blanket "1-7" loses per-stat floors) | port clamps match the defining surface |
| `status` | COHERENT / DRIFTED / AMBIGUOUS / ORPHANED / UNREGISTERED-LOAD-BEARING / DEAD | COHERENT |

Guardrails carried down from the armature (§1 / doctrine ED-1083 §2), quantity-layer phrasing:
- **No scale-local stat dialect**: a subsystem never mints a private name for an existing quantity
  (MS/"RS", Invasion/Institutional Pressure, Composure/Face — the last correctly scoped by ED-1056).
- **No formula re-transcription**: carriers cite the defining surface; they do not restate the
  formula (the C1-F5/F6 glossary rot and C3-F1 Knot four-way are re-transcription failures).
- **A port never corrects its oracle in-place** (ED-1050 rule, re-affirmed by C6-M1's RESIST drift).
- **Note (C1 critic):** `practitioner_stat` and `unit_stat` appear in the census but are NOT in
  descriptor_registry's declared KIND enum — §2 must either add them or fold those rows into
  existing kinds; do not propagate the unrecognized labels silently.

---

## §2 · Registry deltas (armature §3 analog)

Consolidated from the seven dossiers. Filed via the armature §10 extension process; each is
**Class-B (PP-674 vetting: mechanical fact extraction from cited surfaces, no invented values)**
unless marked Class-C/design. Names in *italics* embed a docket decision and must not be filed
until the matching OPT-AV row is ruled.

| # | key (proposed) | KIND | aliases | defining surface | vetting note |
|---|---|---|---|---|---|
| D1 | *`attr.mind.recall`* | attribute_scalar | — | params/core.md:140-145,151 | Class-B extraction; the *roster slot* is OPT-AV-1 (queue-13) |
| D2 | `prac.thread_sensitivity` (+ derived `prac.tps`) | practitioner_stat (new kind — see §1 note) or attribute_scalar | TS, TPS | glossary.md:60; params/threadwork.md:13 | Class-B; load-bearing in 3 pool formulas (F-REG-006/007) |
| D3 | *`terr.fort_level`* | new territory/province kind, distinct from settlement_stat | Fort | module_contracts.yaml:591-592; params/bg/geography.md:8-25 | Class-B key; the settlement-inheritance rule is OPT-AV-18/SE |
| D4 | `derived.wound_interval`, `derived.max_wounds` | derived_value | WI, MW | combatant.py:35-37,30-32; module_contracts.yaml:819-821 | Class-B; formula-intermediate pattern (F-C-009) |
| D5 | `set.facility_tier`, `derived.settlement_weight` | settlement_stat / derived_value | FacilityTier, W_s, base(Type) | settlement_layer_v30.md:159-165 | Class-B (C5-F11: prose-defined, contract-undeclared) |
| D6 | `derived.face` (max + current) | derived_value | Face | social_contest_v30.md:481-512; params/contest.md:137,144 | Class-B; distinct from retained Composure (ED-1056); SC co-sign |
| D7 | `track.coherence` | **track per ED-830** | — | derived_stats_v30.md:261,563 | Class-B **propagation of a resolved ruling** (C7-F2); also fix module_contracts.yaml:288 `bucket: pool` |
| D8 | *`pool.political`* | pool | Mandate Pool (deprecated), Faction Political Pool | ci_political_v30.md:161-169; mechanical_terms_index.md:192 | name per prior art; final name = OPT-AV-18 |
| D9 | `track.warden_recognition` | track | WR | params/bg/geography.md:412-431 | Class-B; distinct from retired WA (FIX-07); victory.md sweep = OPT-AV-7 |
| D10 | 8 missing `not_descriptors.derived_values` (Legitimacy-derived, Treasury, Levies Available, Reputation, Discipline, Intelligence Holdings, Public Order, TroopCount) | derived_value | — | derived_stats_v30.md:533-547 §14.1 | Class-B; regenerate mechanically from §14.1 so it can't drift (C5-F5/U5) |
| D11 | `pool.knot` registry linkage + `track.persuasion` cross-link | pool / track | — | mechanics_index.yaml:350; social_contest_v30.md:89-93 | Class-B (F-REG-013, F-REG-009) |
| D12 | alias **scope tags** on cross-domain bare words | schema field | "Influence" (attr alias vs fac.influence), "Legitimacy" (set 0-7 vs faction derived 0-140), "Discipline", "Standing" | descriptor_registry.yaml:43,65,78; derived_stats_v30.md:297,554 | Class-B schema addition; the *renames* are OPT-AV-12/-18 |
| D13 | `formula_pointer` field on not_descriptors entries | schema field | — | (new) | Class-B; makes A18 checkable — carriers point, never restate (C1 U-set) |
| D14 | per-entry `scale`/`floor` on faction_stats | schema fix | — | params/bg/core.md:200-207 | Class-B; Intel floor value itself = OPT-AV-18 |
| D15 | `contracts_bucket` ↔ registry KIND crosswalk (incl. `bucket: pool` → `reservoir` rename or merge) | schema | — | module_contracts.yaml:288,645,822 vs descriptor_registry.yaml:106-112 | Class-B/C boundary; C3-F3, C4-F7 |
| D16 | Piety/Conviction family key(s) | track | PT/CT/CV | (per OPT-AV-13 ruling) | **held**: ED-644/1006/1009 keep the name open; key filing follows the ruling |

---

## §3 · Conformance checks (armature §4 analog)

Same lifecycle as A1–A16: **land report-only → burn the backlog via the §4 wave → flip to blocking
at zero backlog.** Numbered continuing the armature's sequence.

### §3.1 A17 — stat-vocabulary closure

- **Mechanical predicate:** every stat identifier appearing in (a) Key payload `stat_deltas` /
  `impact_vector` keys and `required_payload_fields`, (b) `module_contracts.yaml` `state:` /
  `derivations:` entries and gate conditions, (c) `params/*.md` table row names, (d) exported
  engine-param keys — resolves (directly or via declared alias) to exactly one
  `descriptor_registry.yaml` key of a declared KIND.
- **Input surfaces:** `sim/substrate/keys.py` traffic (requires the OPT-AV-16 validation hook —
  today stat_deltas is unsampleable, `keys.py:239-251` checks field presence only, never names);
  `references/module_contracts.yaml`; `params/`; `references/engine_params/*.json`.
- **Missing artifact:** the registry union loader + alias resolver (small; `tools/names.py` already
  loads names_index but matches only the empty `legacy:` fields — C7-F3); the keys.py warn-tier
  hook (candidate **invariant 9** in `key_substrate_v30.md` §2.3, mirroring the existing
  impact_vector AXES check at `keys.py:321-327`).
- **Measured backlog (C7, seeded):** ~34/88 census quantities (39%); ~23/34 (68%) of
  module_contracts state/derivation declarations; stat_deltas layer unmeasured. *Caveat: seeds are
  cluster-prose estimates without per-item citations (C7 critic, cardinal rule a) — the check's
  first report-only run re-derives the true backlog; do not flip on the seed numbers.*
- **Gating:** blocked on OPT-AV-1 (roster) for the attr family; other families can report
  immediately.

### §3.2 A18 — formula single-source

- **Mechanical predicate:** for each registered quantity, exactly one surface carries a formula
  *definition* (the `defining_surface` / D13 `formula_pointer`); every other surface that states
  the formula either cites the pointer or textually matches it; a non-matching restatement without
  a supersession marker is a violation.
- **Input surfaces:** the same four as A17, **plus prose formula extraction from `params/*.md` and
  design docs** — the hard half.
- **Missing artifact — the prose-formula drift detector (specified here, NOT built):** a `tools/`
  extractor that (1) walks markdown tables + inline `X = expr` patterns in params/ and the
  designated design heads, normalizing unicode ×/− and parenthetical clamps ("minimum 5") into a
  canonical expression string; (2) groups extractions by resolved registry key (via A17's
  resolver); (3) diffs each group against the defining surface's expression; (4) emits
  report-only violations with both file:lines. This is the missing detector CLAUDE.md §5 names
  ("no tool parses params/*.md prose — prose formula drift has NO automated detector") and the
  concrete next slice of **ED-1052**. It does *not* need to evaluate formulas — string-normalized
  inequality plus a supersession-marker whitelist is enough to have caught C1-F5/F6, C2-F2, C3-F1,
  C3-F7, and C5-F1.
- **Measured backlog (C7, seeded):** ~25–27/88 (28–31%); same seed caveat as A17. Registration
  does not imply single-sourcing (Mandate, 8/8 surfaces, dual-formed — C7-F8).
- **Sequencing:** after A17 (A18 consumes A17's resolver; A17 is deterministic, A18 needs the
  citation whitelist judgment).

### §3.3 Companion micro-checks (cheap, land with the wave)

- **A17a — export fence:** every constant in `combat_config.gd`/`engine_params/*.json` either
  round-trips through `tools/export_engine_params.py --check` or carries an explicit
  hand-transcribed annotation (closes the C6-F2/C6-M1 class).
- **A17b — dead-export lint:** exported keys with zero engine consumers are flagged (C6-F3's 7/181).
- **A17c — registry liveness:** every `references/*_registry.yaml`/index either has ≥1 live tool
  consumer or a `historical_snapshot: true` header (C7-F5/M1's thirteen unconsumed surfaces).

---

## §4 · The shaping-wave slot (armature §6.3 analog)

**Wave Q — "Quantity/descriptor unification wave (IN)"** — one PR-sized lane, verified by the
extended adjudicator like waves 1–5.

Worklist (in order):
1. **Hygiene batch** (OPT-AV-7): the ~20 pure-propagation stale-carrier fixes — no design calls,
   every edit cites the ruling it propagates.
2. **Registry filing** (§2 deltas D2, D4–D7, D9–D15 — the Class-B set with no pending docket
   dependency; D1/D3/D8/D16 follow their OPT-AV rulings).
3. **A17 report-only** + the keys.py warn-tier hook (OPT-AV-16); first true backlog measurement.
4. **A18 detector build** (§3.2) + A18 report-only.
5. **Tier promotion** (OPT-AV-6): warn→block + registry test resurrection, only at zero A17 backlog
   on the ratified roster.

**Sequencing against armature waves 1–5:** insert **after wave 1 (echo transport wiring)** — the
transport must exist before its vocabulary hook has traffic to check — and **before any wave that
transcribes params/ numbers toward Godot** (the §5 pipeline), so every number that crosses does so
under A17/A18 report coverage. Steps 1–2 have no wave dependency and can ride any open IN window.

Roster discipline (doctrine spec §7): no new `.claude/agents/` role for this; the standing
conformance-scanner candidate absorbs A17/A18 once they exist.

---

## Provenance

Authored at the Fable synthesis tier (CLAUDE.md §10 propagation-spec authorship node) from the
2026-07-08 attribute/value coherence audit: 88-row census (`02_census/`), 7 dossiers + 7 critic
passes (`01_workings/`), 82 post-funnel findings (`finding_status.md`), docket (`ed_options.md`).
Every criterion above binds existing doctrine (armature §1/§4/§6.3, holonic ED-1083 §2, ED-1050
port rule, PP-674 vetting classes) — no new criteria invented.
