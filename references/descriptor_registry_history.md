# descriptor_registry — history

Companion to `references/descriptor_registry.yaml`. **That file is the REGISTRY; this one is HISTORY.**

## Why the split (B-X extraction, 2026-10-06)

Jordan, 2026-10-06: *"you can extract all edit histories/discussion from .yaml files in references and
just make those a supplement."* `descriptor_registry.yaml` carries the descriptor space the engine's
exporter (`tools/export_descriptors.py` -> `engine/engine_params/descriptors.json`) and the quantity
vocabulary readers parse, and its comments had accreted dated rulings, renames, incident write-ups and
provenance chains around the rosters. The precedent is `references/id_reservations_history.md`.

**Nothing was deleted.** Every block below is the verbatim text that sat in the YAML at commit
`8b57336`, moved rather than rewritten, grouped under headings that follow the YAML's own sections.
Three unread `note`-style KEYS (`aggregates.note`, `not_descriptors.note`,
`not_descriptors.wave_q_step3_additions`) were moved too: no tool, test or skill reads them
(readers load by named section/bucket, or `yaml.safe_load` the whole file), so removing them changes
the parsed data in exactly those three keys and nothing else.

**What stayed behind, deliberately:** the schema, the `KIND:` enum (`tests/valoria/
test_descriptor_registry_category_b.py` reads the file's first 2,000 characters for `personal_track` and
exactly one `# KIND:`), the IN-FLUX / count-ruled attribute roster warning, the `category_b_scalars.note`
key (the same test asserts it is non-empty), the semantic-order and fifth-axis instructions on
`axis_roster`, the `deprecated:` rows (their `reason:` is data a reader needs, including its
correction), every entry's `source:` value, and a one-line summary where a reader needs the fact to
edit correctly today.

**Adding here, not there.** New dated narrative, rulings-in-passing and rationale for a descriptor
belong in this file (or the ED ledger), not in YAML comments. The YAML comment should stay one line
per section.

## Head: what the registry is a companion to

*(HEAD `8b57336`, lines 3-5 — verbatim.)*

```text
# Companion to core (the engine) AND key_substrate (the vectors): this registry DEFINES the
# descriptor space; Keys carry instances. Systems bind descriptors BY KEY (name-indexed), so a
# descriptor can be renamed / recategorized / extended HERE without rewriting any consumer.
```

## Decisions ratified 2026-06-06 (Jordan)

*(HEAD `8b57336`, lines 7-14 — verbatim.)*

```text
# Decisions ratified 2026-06-06 (Jordan):
#   W2.8  Body/Mind/Social aggregates -> PLACEHOLDERS (defined; not yet wired into derived values).
#   W2.9  ONE registry mechanism, partitioned by `domain` (actor/settlement/equipment/environment).
#   resonance_style -> DEPRECATED (was "most-persuasive mode of argument"; superseded by
#         contest_style + Conviction-driven interpretation; never canonically enumerated).
#   attribute roster -> 9 personal attributes (3 body / 3 mind / 3 social), IN FLUX:
#         `name` is the current primary; `aliases` carry alternatives + LEGACY names so existing
#         formula references back-resolve (this is what makes the roster cheap to churn).
```

## KIND enum: additions and the personal_track batch

*(HEAD `8b57336`, lines 20-27 — verbatim.)*

```text
#   practitioner_stat and territory_stat added 2026-07-08 (ED-IN-0029 docket, OPT-AV-3, D2/D3):
#   these two KINDs existed informally in audit census rows before this registry recognized them.
#   personal_track added 2026-07-29 (W3 item 4, OI-30a, 07-14 unification §3 / ED-IN-0059) to
#   cover the Category-B scalar batch below (Wounds/Turmoil/Accord/Poise/Initiative/season
#   counter) -- ONE kind for the whole batch, not one per scalar; these six span three different
#   `bucket:` values in module_contracts.yaml (track/clock/derived_value) and are not a single
#   mechanical family, so `personal_track` here names the REGISTRATION BATCH, not a shared runtime
#   shape -- see that section's own comment for the per-entry pointer + bucket citation.
```

## attributes: the `Influence` removal

*(HEAD `8b57336`, line 58 — verbatim.)*

```text
    # `Influence` removed 2026-09-16 -- it was `fac.influence`'s canonical name (that row retired at `29b`); see names_index.yaml.
```

## aggregates: the removed `note:` key (unread)

*(HEAD `8b57336`, lines 68-72 — verbatim.)*

```text
  note: >
    The legacy "Stat x 3" derived-value multipliers (e.g. Composure = Charisma x 3) are
    dimensionally equivalent to a category aggregate (3 members summed). These placeholders let a
    future migration (W3) define derived values off the aggregate and retire the ad-hoc multipliers.
    NOT active until that migration; R7 + derived_stats §14 remain authoritative meanwhile.
```

## PRACTITIONER stats: ratification and rationale

*(HEAD `8b57336`, lines 75-77 — verbatim.)*

```text
# PRACTITIONER stats (actor/thread-practitioner). RATIFIED 2026-07-08 (ED-IN-0029, OPT-AV-3, D2):
# Thread Sensitivity/Thread Pool Score were load-bearing in 3+ pool formulas (threadwork, knot
# formation, fieldwork investigation) with zero prior registry presence.
```

## TERRITORY/PROVINCE stats: ratification and rationale

*(HEAD `8b57336`, lines 86-89 — verbatim.)*

```text
# TERRITORY/PROVINCE stats. RATIFIED 2026-07-08 (ED-IN-0029, OPT-AV-3, D3): Fort Level was
# load-bearing in the Garrison Strength formula with zero registry presence; distinct scale from
# settlement_stats below (17 province/territory nodes vs 35-37 settlements -- the
# province-to-settlement inheritance rule itself is a separate open item, OPT-AV-18, fed to SE).
```

## FACTION stats: the retirement at `29b`

*(HEAD `8b57336`, lines 97-103 — verbatim.)*

```text
# FACTION stats: RETIRED at plan position `29b` (2026-10-01). The six rows (`fac.influence`, `fac.legitimacy`,
# `fac.wealth`, `fac.military`, `fac.intel`, `fac.stability`, scale 0-7) were declared for exactly one reader,
# `engine/autoload/game_state.py::Faction`, which is deleted; the season's faction is a set of person acts
# `via` seats and carries no stat vector of its own. `architecture/meta/01_AXIOMS.md` `ID-13`: a declared field
# that reaches no reader is not declared. The block, with the two 2026-08-23 rulings that shaped it ("Legitimacy
# is a base"; "Influence can be 0", all six floored at 0) and the Mandate-is-derived note, is in git at
# `5c5d8ec6:references/descriptor_registry.yaml`. `set.legitimacy` (settlement_stats below) is unaffected.
```

## inline comment on line 117

*(HEAD `8b57336`, line 117 — verbatim.)*

```text
   # ED-IN-0029 D5 residual, filed 2026-07-08 (Wave-Q-step-3 pass) -- distinct from `terr.fort_level` above; the companion derived `settlement_weight`/W_s is registered below under not_descriptors (no derived.* KIND exists in this file)
```

## CATEGORY-B SCALARS: header, provenance

*(HEAD `8b57336`, lines 120-121 — verbatim.)*

```text
# CATEGORY-B SCALARS (07-14 unification §3 / ED-IN-0059 list). Registered 2026-07-29 (W3 item 4,
# OI-30a). These are POINTER REGISTRATIONS ONLY -- they name each scalar and cite its canonical
```

## CATEGORY-B SCALARS: scope of the registration pass

*(HEAD `8b57336`, lines 126-127 — verbatim.)*

```text
# never by re-deriving it from this entry. C2 (npc beliefs/concerns/projects, §5 fork 11) is
# OUT OF SCOPE for this section -- stays J, untouched by this registration pass.
```

## CONVICTION ROSTER: title

*(HEAD `8b57336`, line 155 — verbatim.)*

```text
# CONVICTION ROSTER -- ENUMERATED HERE, 2026-08-24, AND THE REASON IS A LIVE DEFECT.
```

## CONVICTION ROSTER: the live defect and the resolution

*(HEAD `8b57336`, lines 157-179 — verbatim.)*

```text
# This roster used to live ONLY in `by_reference` below ("authoritative content stays in the
# source doc"). Under CLAUDE.md 0.05 that is the anti-pattern: a `.md` is reference, so a roster
# stated only in prose is a roster no code can read -- and two subsystems therefore invented their
# own. Measured 2026-08-24:
#
#   systems/characters/sim/conviction.py   9 names (Faith Order Reason Equity Precedent Autonomy
#                                            Continuity Community Warden) -- 3 of them (Reason,
#                                            Autonomy, Continuity) appear in no canonical set
#   systems/world/sim/npe.py               8 names (Faith Order Reason Justice Survival Loyalty
#                                            Truth Power) -- 6 appear in no canonical set
#                                            (only Faith and Order are canonical)
#   this registry                         13 by reference, enumerated nowhere
#
# The two code rosters overlapped in THREE names, and the cost was a silent no-op: the only game
# caller of `apply_conviction_scar` passes `conviction='Loyalty'`, which is in npe's set and not in
# conviction.py's, so ED-912 6.1's Close-Knot-break Conviction Scar never landed while the caller
# reported that it had.
#
# RESOLVED ON ARCHITECTURE, not by picking a favourite: this registry is the centralized surface
# every descriptor already resolves through, and it already declared the count as 13. So the 13
# are transcribed here from `systems/characters/reference/conviction_taxonomy_v30.md` 2, exported into
# `engine/engine_params/descriptors.json` behind the existing blocking `--check`, and read by
# `engine/substrate/descriptors.py`. Both subsystems now read the leaf. One roster, one home.
```

## THE FOUR ETHICAL AXES: the defect that put the roster here

*(HEAD `8b57336`, lines 199-214 — verbatim.)*

```text
# THE FOUR ETHICAL AXES — enumerated here for the same reason the 13 Convictions are, and after
# the same class of defect. `engine/substrate/keys.py::AXES` and `engine/season/rosters.yaml:
# conviction_axes` each carried their own literal copy; the roster's note asserted that
# "a fifth axis or a rename is one edit there and a loader refusal here rather than two rosters
# drifting apart", and MEASURED 2026-09-14 that refusal did not exist. Exactly one module in the
# tree imports `AXES` (`engine/substrate/__init__.py`, re-exporting it) and nothing under
# `engine/season/` reads it — so a fifth axis added to `keys.py` alone left the season engine
# scoring on four in silence, and one added to the roster alone left the season engine scoring on
# five while `keys.py` invariant 6 rejected every Key that named it. Two failures, opposite
# directions, neither side able to see the other.
#
# This is the `conviction_roster` shape applied to the object one level up, and it is a PRECEDENT
# rather than a new decision: nine names in one subsystem, eight in another and thirteen registered
# is what put the roster here in 2026-08-24, and the disagreement had already disabled a ratified
# mechanic. `by_reference` below still carries the `axis.*` row for the axis SEMANTICS (poles,
# scale, source doc); what moves here is the NAME SET, which is what code compares against.
```

## NOT DESCRIPTORS: the 2026-07-08 list extension

*(HEAD `8b57336`, lines 254-261 — verbatim.)*

```text
#
# Lists extended 2026-07-08 (ED-IN-0029 docket, OPT-AV-3/D6/D7/D9/D10, OPT-AV-18/D8) to close a
# registry-completeness gap the coherence audit found: derived_stats_v30.md §14.1 actually tables
# 16+ derived values and the pools list was missing an 8th live pool, vs. the 9 originally listed
# here -- none of the additions below change any formula, they only register names already live
# and computed elsewhere. Bare-string entries only (no individual keys/formulas) -- matches this
# block's existing minimal-registration pattern; per-entry structure (formula_pointer, D13) is
# specified as a future W2.8-style migration, not implemented by this ruling.
```

## not_descriptors: the removed `note:` and `wave_q_step3_additions:` keys (unread)

*(HEAD `8b57336`, lines 268-302 — verbatim.)*

```text
  note: >
    Computed/bounded FROM registered descriptors (derived_stats §14). The §14.1 derivation specs
    (which attribute x what multiplier) are registry-ADJACENT data; a future step (W2.8 migration)
    may hold them here so multipliers are data, not code.

    Disambiguation notes (RATIFIED 2026-07-08, ED-IN-0029 docket):
    - "Legitimacy (faction, derived)" is Mandate x 20, a 0-140 faction buffer -- distinct from
      `set.legitimacy` (settlement_stats above, 0-7). "Discipline (faction)" is Stability x 10, a
      0-70 faction buffer -- distinct from the unrelated unit-scale mass-battle Discipline stat
      (1-7, organisational integrity; lives in mass_battle_v30.md, not this registry). Display-scope
      label ratified OPT-AV-18: prefer "Faction Discipline" in new UI/prose to reduce the collision,
      formula unchanged.
    - Coherence: registered here as a `track` per the already-resolved-but-never-propagated ED-830
      ruling ("Coherence reclassified from Derived Value to Track"). `module_contracts.yaml`'s
      `threadwork` module still tags its Coherence state entry `bucket: pool` -- that is now a
      confirmed 3-way disagreement (ledger: track / here: track / contracts: pool) pending the
      `contracts_bucket` <-> registry-KIND crosswalk (D15, not yet built) or a direct contracts fix.
    - "Political Pool" (D8): the parliamentary vote-tally construct (Church `Mandate+floor(CI/20)`;
      opponents `max(0,Mandate-floor(CI/30))`, ci_political_v30 §3.4). Name ratified per existing
      prior art in mechanical_terms_index.md (which already deprecates "Mandate/Faction Pool" in
      favor of this name) -- not a new coinage.

  wave_q_step3_additions: >
    Residual filed 2026-07-08 alongside the Wave-Q-step-3 tooling build (A17 checker +
    `sim/substrate/keys.py` stat_vocabulary hook, see registers/handoffs/HANDOFF_IN.md): `set.facility_tier`
    (settlement_stats, D5 residual -- distinct from `terr.fort_level` above) and "Settlement Weight"
    (D5's derived companion, no `derived.*` KIND exists in this file so it's a plain name here, same
    treatment as the other derived_values). Two proposed deltas remain REJECTED, not filed, by both
    this pass and the prior ratification pass: D11 (`pool.knot`/`track.persuasion` cross-link -- no
    linkage exists at either cited source) and D15 (`contracts_bucket`<->KIND crosswalk field --
    `not_descriptors` carries no KIND field to cross against). Also flagged, not fixed: the Coherence
    disambiguation note two paragraphs up is itself now STALE -- `module_contracts.yaml`'s
    `threadwork` module's Coherence entry was corrected to `bucket: track` in this same PR #112
    ratification pass, so the "3-way disagreement... contracts: pool" claim no longer holds; left
    as-is rather than hand-edited, since fixing PR #112's own prose is out of this pass's scope.
```
