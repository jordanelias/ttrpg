# canonical_sources — history

Companion to `references/canonical_sources.yaml`. **That file is the INDEX; this one is HISTORY.**

## Why the split (B-X, 2026-10-06)

Jordan, 2026-10-06: *"you can extract all edit histories/discussion from .yaml files in references and
just make those a supplement."* The precedent is `references/id_reservations_history.md`. Dated
narrative (what a session did to the file, which LPS step touched which doc, provenance chains) sits
here; the index keeps what a reader or a tool needs today.

**Nothing was deleted.** Every block below is the text that used to sit in the YAML, moved verbatim
(the `Was at line N` numbers are lines of the file as it stood before the move).

**What stayed in the YAML, deliberately:** every `canonical_sha__*` pin and the path line above it
(`tools/freshness_gate.py` parses them), every `design_doc`/`index`/`infill` key (read by
`tools/ci_generation_consistency.py`, `tools/canon_coverage_check.py` and the vector audit), the
`struck`, `status`, `added`, `reason` and `canonized_pass` data, the `module_contracts` `note`, and the
section dividers. One line of operative text replaced three of the blocks: the combat resolver
pointer, the pin-format sentence, and the `settlement_layer` `note`.

**Three readers scan this file's RAW text, comments included**, so a path or `design_doc:` pattern that
lived only in a moved comment would drop out of them: `tools/broken_dependency_checker.py`
(`extract_file_refs`, reports references to missing files),
`skills/valoria-vector-audit/scripts/vector_audit.py` (`_MD_PATH_RE`) and
`skills/valoria-vector-audit/scripts/gen_audit.py` (`_mentioned_in_canonical_sources_raw`, an
informational bucket). `tests/valoria/test_flow_skeletons.py` also reads the raw text, to find a symbol
that a frozen skeleton cites for this file (`LINE_UNSTABLE_TARGETS`); the symbols are keys (`ui_ux`,
`victory`) and stay.

**Adding here, not there.** New narrative about this file belongs in this file or in the ED chain. The
YAML's head comment stays one pointer line.

---

## File header

*Header line 3, the strip-and-cap-raise note. Was at line 3.*

```text
# 2026-05-02: All 'Last touched: ...' breadcrumb comments removed (now 7 stripped); editorial history lives in ED entries + propagation_log. ED-770 SHA-follow-up status preserved. Cap raised 5000 → 8000 per ED-786.
```

## `systems:` -> `combat`

*Comment block above `resolution_engine`. Was at lines 79-83.*

```text
    # engine/params/combat.md DEPRECATED 2026-06-04 (Jordan) -> deprecated/params/combat.md; resolution superseded by combat_engine_v1 (ED-900/901/902)
    # ── RESOLUTION ENGINE (ratified 2026-06-04, Jordan 'ratify commit all'; ED-900) ─────────────────
    # systems/combat/combat_engine_v1/ is the CANONICAL personal-combat resolver, superseding the RESOLUTION
    # layer of combat_reference_v1.md (lore/flavor retained; ED-PC-0056 consolidated five docs into it). Modules: wrapper/systems/core/config/combatant/geometry/
    # tradition. config.py = live Class-C parameter source. SHA-track via freshness_gate.py --update.
```

## `systems:` -> social_debate pin comment (above `scale_transitions`)

*Comment block after `mass_combat`. Was at lines 99-108.*

```text
  # social_debate SHA-pins current as of 2026-07-01 (Contest Stage 2 / Gate B closeout).
  # Detailed per-round rationale lives in the ED chain, not here (ED-1055/1056 Gate A CR1/CR2/CR3
  # fold-in; ED-1057 Panel aggregation=weighted-by-standing; ED-1058 Stage-2 dictionaries;
  # ED-1059 Panel reachability via Guild Arbitration rebind; ED-1060 Terminal Doubt
  # banded/tally split; ED-1061 Guilds boost=context-derived-from-venue) — all ratified except
  # where an ED text says otherwise. Pins are git blob OIDs (LF-normalized, as committed),
  # computed via `git hash-object <file>` — identical to what freshness_gate.py --update
  # produces on an LF/CI checkout. NOT raw-CRLF-disk-byte SHAs. social_contest_v30_index.md is
  # REGENERATED (doc_index_gen.py) from the design doc, not hand-edited — re-run the generator
  # after any structural edit to the design doc, then re-pin both.
```

## `systems:` -> `settlement_layer` (the four `note__lps*` KEYS)

*These four DATA keys were the whole body of `settlement_layer`; no code read them by key (checked). The entry now carries one `note:` pointing here. Was at lines 120-123.*

```text
    note__lps2d: "LPS-2d (2026-05-30) final residual close: remaining faction-level Church/target-L degree effects -> per-territory Legitimacy (Excommunication/Heresy/Baralta-suppression, magnitude-preserving) OR Mandate −1 (Seizure FAILURE, authoritative faction_layer §2.7) in stats_1_7_scale + faction_canon. Broadened same-line sweep = 0 faction-level L/PS across 11 docs; faction system verified end-to-end."
    note__lps2c: "LPS-2c functional reconciliation (2026-05-30): CI-60 Seizure aligned to AUTHORITATIVE faction_layer §2.7 (Influence+floor(CI/15) vs Ob 7−PT; Fail->Mandate−1) in faction_canon §9+Church sheet+stats_1_7_scale (FCN-SEIZURE-DRIFT closed); Excommunication degree effects (faction L +-1) -> per-territory Legitimacy (magnitude-preserving); Restoration PS clarified community-level per FSA §6/PP-460. §1.8 zero-territory refined (Lowenritter embedded vs Restoration community). Detail: master."
    note__lps1b: "LPS-1b (2026-05-30 self-review remediation): §1.8 += zero-territory Mandate=0 handling (Restoration/Lowenritter) + aggregation note (plain mean; temperament is the sibling rollup, both await numeric per-territory population for population-weighting — LPS-3). F4 dispositioned RESOLVED-BY-RESOLVER (no new mechanic). Detail: master."
    note__lps1: "LPS-1 (2026-05-30 Jordan structural ruling): §1.8 added — L/PS PER-TERRITORY (0-7); faction Mandate = round(mean controlled-territory 0.5L+0.5PS); mean-reverting Mandate->territory feedback (sim-stable). Supersedes faction-level L/PS in PP-686 v2. Rewiring staged LPS-2+. Detail: master _lps_structural_redesign_2026-05-30."
```

## `systems:` -> Foundations comment

*Comment block under the "Foundations" divider. Was at lines 147-149.*

```text
# Repointed 2026-09-07. The two amendments these entries named are SUPERSEDED and
# carry banners saying so; pinning them here would have made this index name
# superseded documents as canonical. Their content lives in the philosophy suite.
```

## `systems:` -> after `self_rendering`

*Divider note about the full_stack mapping, then the D-3 / D-6 / D-7 propagation comments. Was at lines 157-168.*

```text
# ────────────────────────────────────────────────────────────────────────
# All 17 full_stack systems mapped. sim_gate('full_stack') will pass after a
# verification ledger is built at /home/claude/sim_verification_ledger.json
# citing these paths. See valoria_hooks.sim_gate() for requirements.

# ── D-3 + D-6 + D-7 propagation (2026-04-22) ─────────────────────────────
# D-3 (ED-724): Solmund dissolution site — specific, contested, off-map.
#   Propagated canon/03_canonical_timeline.md §Solmund.
# D-6 (ED-727): Lenneth TS pathway — slow scholarly loosening, SA-gated,
#   ceiling 10-20. Propagated systems/npcs/npc_character_analyses_v30{,_infill}.md.
# D-7 (ED-728): Valn origin — pre-Altonian, ambiguous, possibly pre-Einhir.
#   Propagated arcs/simulated/arcs_10_18.md §Terminology (L17) + ED-NEW-7 row.
```

## `faction_behavior` (the `note__lps2` KEY)

*A DATA key; no code read it by key (checked). `status`/`added` stay. Was at line 211.*

```text
    note__lps2: "LPS-2 (2026-05-30): faction-level L/PS DEMOTED per LPS-1 — faction_behavior §2/§3.4/§3.5/§3.6/§4 (Mandate now = round(mean controlled-territory 0.5L+0.5PS); strictness reads aggregate), faction_canon §3.4/§5.1/§5.2(RESOLVED)/§5.3, faction_state_authoring §8 (per-territory seed), stats_1_7_scale (6-stat header), derived_stats footnote. Detail: master _lps_structural_redesign_2026-05-30."
```

## `faction_canon_consolidation` (the `note__lps2b` KEY)

*A DATA key; no code read it by key (checked). `status`/`added` stay. Was at line 234.*

```text
    note__lps2b: "LPS-2b (2026-05-30): faction tactics rolling faction-level L demoted to Mandate (Royal Decree/Excommunication/Sovereign Authority) in faction_canon §9 + Crown/Church sheets + stats_1_7_scale (matches factions_personal §8.2/8.4); PART B L/PS Dynamics marked per-territory; Seizure flagged FCN-SEIZURE-DRIFT. Detail: master _lps_structural_redesign_2026-05-30."
```

## Trailing comments (after `module_contracts`)

*LPS-2e / LPS-2+ / F-RESID / NERS-audit / term-propagation comments, to end of file. Was at lines 282-292.*

```text
# LPS-2e (2026-05-30): settlement_layer_v30 §1.8 re-grained — L/PS per-settlement (was faction-level); Mandate = size-weighted saturating aggregate, W=base(Type)+Prosperity+FacilityTier, K=6; geography "territory" (T1-T17)=province-tier, retained.
# LPS-2+ consumer wiring (2026-05-30): faction_behavior/faction_canon/faction_state_authoring/stats_1_7_scale/derived_stats wired to settlement-grain + size-weighted Mandate; settlement_layer §1.8 (LPS-2e) is authoritative for Weight + formula.
# LPS-2+ wiring follow-up (2026-05-30): faction_behavior §3.4/§3.5/§3.6 terminology territory->settlement (root PP-686 doc fully consistent with §1.8).
# LPS-2e audit-patch (2026-05-30): completed settlement re-grain across all consumers (faction_behavior §4 Mandate block, faction_canon 6-stat resolution + Excommunication, stats_1_7_scale Church L-strip + seizure->§2.7); Church L-strip effects now PER-SETTLEMENT (Jordan ruling); flagged Mandate x20 / 0-7 meter calibration.
# Mandate x20 meter resolved (2026-05-30, mechanical-tier): NOT a defect -- per derived_stats §3 multipliers are per-system (Treasury x100, Reputation x15, Discipline x10, Legitimacy x20), no 0-100 master scale; sigma engine governs Mandate RESOLUTION (d+sigma resolver) not the meter buffer. Removed the speculative 0-100 flag.
# F-RESID migration (2026-05-30, ED-885 — pending ledger entry; ratification ID to confirm, likely ED-874): 4 bare-stat Unique Actions (Royal Decree, Excommunication, Private Collection, Economic Leverage) migrated to the d+sigma resolver (D=max(1,(O-1)*2); contested=target stat). Hafenmark Doctrine flagged, not migrated.
# Comprehensive all-directions NERS audit of LPS-2e + size-weighted Mandate + F-RESID migration (2026-05-30): designs/audit/2026-05-30-lps-mandate-ners-audit/. Verdict NERS-compliant as built; 2 Jordan intent/data confirmations (hugeness-premium, Weight redundancy) + 1 elegance reservation; no hard mechanical defect.

# ─── 2026-06-04 term-propagation co-file note ───
# settlement_layer_v30.md: "Public Support" → "Popular Support" (Jordan 2026-05-30 ruling).
# Term-level change only; canonical source authority for the settlement layer is unchanged.
```
