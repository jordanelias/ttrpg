# Pessimist Subtractive NERS + Corpus Contamination Follow-up — Workplan

**Date:** 2026-07-08. **Status:** PROPOSED (read-only audit; no canon file edited by this pass).
**Follows on from:** `designs/audit/2026-07-08-crunch-cascade-cogload-legibility-audit/` (PR #101,
merged) — this audit takes every mechanism/tracker/mechanic/gap that pass flagged and subjects it
to a second, adversarial lens, then separately sweeps the corpus for every glossary term,
attribute, and derived-score usage to build a centralized single-source-of-truth map.

## ⚠️ CURRENCY DISCLOSURE — read before acting on any finding below

This audit's source material (the crunch-cascade findings + direct working-tree reads) was
gathered starting from commit `4af9684` (2026-07-08 morning). **Between then and this PR's push,
`main` advanced through ~15 more commits that overlap substantially with this audit's own
territory** — a genuinely unusual amount of same-day concurrent activity on exactly the systems
this pass covers. Confirmed, specific overlaps found on a post-hoc `git fetch`:

- **`designs/audit/2026-07-08-attribute-value-coherence-audit/` (ED-IN-0029, PRs #106/#110/#112)
  is an independently-run, more rigorous sibling audit of almost the entire `02_term_usage_sweep/`
  + `03_cross_contamination.md` + `05_single_source_hardcode_registry.md` territory** — an 88-
  quantity census, 7-cluster all-directions trace, and a critic funnel yielding 82 confirmed
  findings (18 P1/39 P2/25 P3), already through a Jordan ratification pass. **Treat ED-IN-0029 as
  the authoritative source for attribute/quantity naming-coherence, not this folder's term-sweep
  documents.** Specifically:
  - **Already fixed by ED-IN-0029's ratified hygiene batch (OPT-AV-7, commit `9ffddb7`)** — do NOT
    action these from this audit's documents, they are stale: `params/core.md:4`'s stale PP-247
    header; `params/board_game.md`/`params/factions.md`'s broken auto-indexes; the glossary's
    Health/Stamina rows (converted to formula-lives-at pointers); `campaign_modes.md`'s MS
    72→60 mislabel + bad citations; the clock-registry Torben Loyalty stale start value; the
    TC/CI citation errors; the `settlement_layer_v30.md` derived-stats citation; the
    `combat_v30.md §7`/`mass_battle_v30.md` wound-penalty sweep; the ED-869 footnote.
  - **Still genuinely open, independently corroborated by both audits** (safe to still cite from
    either): the attribute-roster conflict (ED-IN-0029's OPT-AV-1 was **explicitly SKIPPED** by
    Jordan — "left fully OPEN/UNRULED," matching this audit's finding that it remains unresolved,
    though ED-IN-0029 found a **fourth** roster witness, `canonical_registry.md`'s independent
    10-table, that this audit's sweep did not catch); the Piety/Persuasion/CT naming family
    (ED-IN-0029's OPT-AV-13 was **left open**, no default stated).
  - **Ratified in direction but execution deferred to a lane ED** (mid-state — check the lane ED
    before treating as either "open" or "fixed"): Standing's range collision (OPT-AV-12 → filed
    ED-SC-0014); the Combat Pool struck-form propagation (still `KNOWN-TRACKED ED-1084`, unexecuted).
  - **Genuinely additive, not covered by ED-IN-0029 at all** (its scope is quantities/attributes/
    derived-scores specifically, not categorical/enum types or resolver-engine selection): the
    Interaction Type label mismatch (§03 row 7); the much larger live-"RS"-usage finding in
    `params/threadwork.md` (25+ occurrences vs. ED-IN-0029's narrower 2-line citation at
    `params/threadwork.md:139-142`); the entire `01_pessimist_subtractive_ners/` mechanism-critique
    (a design-merit + rolling-engine-compliance lens, not a naming-coherence one); the entire
    `04_cross_shape_coherence_divergence.md` pool-shape/engine-choice comparison, including the
    Thread-engine wrong-engine-class finding (§04 Engine choice) — ED-IN-0029's C6 cluster covers
    code-*constant* drift, not resolver-*engine-selection* coherence, so this is a distinct defect
    class it did not surface.

- **Personal combat, mass battle, and social contest each saw additional same-day commits directly
  invalidating specific claims in `01_pessimist_subtractive_ners/`:**
  - **`464fa89` (#103) deferred ED-PC-0007**, the ratified PC action-consolidation item this
    folder's PC lane report (`01_lane_PC.md`) cites as a "new finding from adversarial pass — the PC
    action set is being actively consolidated as of today." Jordan's ruling: the verdicts judged the
    stale discrete `combat_v30 §4` action menu, not the canonical `combat_engine_v1/`, so the
    consolidations were "already realized / moot," not live work. **Correct that PC lane citation
    to "deferred, retroactively-validated, not live" before acting on it.**
  - **`e6d8bd1` (#102) shipped ED-MB-0004** — the exact "`subunit_combat_pool` applies full Command
    to every sub-unit independently, letting simultaneous fronts each fight at near-full strength"
    defect that this folder's corpus synthesis (`00_corpus_synthesis.md` §3, item #3) and the MB
    lane report both flag as an open P1, **is now FIXED** (a partition-invariance renormalization,
    `core/exchange.py:_pair_engaged_troops` + `orchestration.py:_convergence_scale`). **This P1
    finding is resolved on current `main`; do not re-file it.**
  - **`c651282`/`a767e3e`/`fe20170`** (#96/#95/#104) wired `scene_dispatch` to the promoted contest
    kernel and landed the consequence spine (`ECHO_TRANSPORT` default ON) — this folder's SC lane
    report already correctly flagged the `contest_legacy_stub` PRUNE as "already Jordan-accepted,"
    but **execution may now be complete rather than merely accepted** — re-verify before citing.
  - Three further PC-lane commits (`c55bdde` #99, `83bc08e` #109, plus `e6d8bd1`'s sibling
    ED-MB-0005 DG-2 yield mechanic) landed wound-Ob calibration and JD-4/JD-9 wiring not reflected
    anywhere in this folder's PC/MB material.

**Net implication:** this folder's `01_pessimist_subtractive_ners/` and `02_term_usage_sweep/` +
`03_cross_contamination.md` + `05_single_source_hardcode_registry.md` documents are a snapshot,
not a live index — treat every P1/P2 finding as a **hypothesis to re-verify against current
`main`**, not a confirmed-current defect, before filing any new ED or acting on any recommendation.
The genuinely durable contributions are the **methodology artifacts** (the pessimist-subtractive
mechanism critique + rolling-engine NERS lens, the hardcode-vs-pulled classification scheme) and
the **specific items flagged above as "genuinely additive"** — everything else should be
re-derived fresh against current `main` rather than trusted as still-accurate.

## Scope (four deliverables, five sections below)

1. **Pessimist Subtractive NERS critique** (`01_pessimist_subtractive_ners/`) — applies the
   established Valoria "Pessimist Subtractive NERS" methodology
   (`designs/audit/2026-07-08-pessimist-action-audit/00_grounding/00_charter.md`: N/Ω/Q criteria
   bound to `references/throughlines_meta.md`, the cardinal rule — judge as-if-built, never by
   build state — and the KEEP/REFINE/DISTILL/MERGE/PRUNE/CUT disposition table) to every element
   the crunch-cascade audit named, generalized from "player actions" (the original audit's scope)
   to *any* tracker, mechanic, interaction-chain flag, cascade-check item, or legibility finding.
   Where an element is a rolling engine (a mechanism resolving via a draw), it additionally gets
   the *other* thing this corpus calls NERS — the rolling-engine compliance test from
   `skills/valoria-resolution-diagnostic/SKILL.md` (Necessary/Robust/Smooth/Elegant, N/R/S/E).
   Nine lanes (PC/MB/SC/FA/SE/TW/DC/AN/XS, matching the crunch-cascade audit's nine subsystems),
   each run as an independent dossier → inverted-adversarial-critic pair, then rolled up into one
   corpus synthesis (`00_corpus_synthesis.md`).
2. **Term/attribute/derived-score usage sweep** (`02_term_usage_sweep/`) — ten batches, each doing
   an exhaustive corpus-wide grep of every glossary term (`references/glossary.md`'s thirteen
   parts), attribute (`references/descriptor_registry.yaml`, `params/core.md`), and derived score,
   citing every occurrence file:line and flagging any divergence from the term's canonical home
   definition.
3. **Cross-contamination map** (`03_cross_contamination.md`) — synthesizes the ten batches into
   the definitive collision/divergence register: every term whose meaning, range, or formula
   disagrees across the corpus, severity-rated, with a status flag for whether
   `references/glossary.md` already knows about the collision (and is right or stale) or has no
   awareness of it at all.
4. **Cross-shape coherence/divergence map** (`04_cross_shape_coherence_divergence.md`) — compares
   pool formulas, rolling-engine choice (NERS Instance A/B/C), Obstacle-scale construction, and
   degree-of-success ladders across every resolving subsystem, flagging which pairs of subsystems
   a player would expect to feel similar but that silently diverge (DIVERGENT-BY-DRIFT) versus
   which diverge on purpose (DIVERGENT-BY-DESIGN) versus which are genuinely COHERENT.
5. **Single-source-of-truth / hardcode registry** (`05_single_source_hardcode_registry.md`) —
   added mid-run at Jordan's explicit instruction: *"ensure you are approaching this from a
   centralized manner where you have tracked where terms/definitions/attributes/scores/values/etc
   are being hard-coded instead of being pulled, so that we don't have stale errors."* Every term
   the usage sweep touched is classified per occurrence as CANONICAL DEFINITION / PULLED-REFERENCED
   (with the actual pointer mechanism named — an import, an export script, a citation) / HARDCODED
   DUPLICATE (an independent literal copy with no sync mechanism — flagged as a staleness risk
   *even when it currently agrees with canon*) / UNCLEAR-NO SOURCE. This is the document meant to
   answer "if I change X, what will I forget to also change because it's a silent hardcoded copy"
   directly, without re-deriving it.

## Method notes

- All five lenses used opus at `effort: 'max'` for the synthesis/rollup stages (per this session's
  explicit instruction, matching the established fallback pattern in this corpus's own tiering
  table — `CLAUDE.md` §10: "verdict-rendering + cross-corpus synthesis... = fable, with opus
  effort:'max' as the drop-in fallback" — used here directly since Fable has a documented
  hanging/metering-cap failure mode in this environment).
- Every dossier/batch stage was sonnet-tier per the same tiering table (bounded pattern-recognition
  work); every synthesis stage (corpus rollup, cross-contamination, cross-shape, hardcode registry)
  ran independently in parallel once their shared inputs were ready, since none of the four depends
  on another's output.
- The Pessimist Subtractive lane reports are themselves already adversarially verified (each went
  through an independent inverted-critic pass, per the established methodology's own discipline);
  the three corpus-level synthesis agents were instructed to re-verify striking claims against the
  working tree directly rather than transcribing lane/batch material uncritically, and each
  reports doing so with specific file:line spot-checks.

## Headline results (see each deliverable for full detail)

- **Corpus pessimist-subtractive tally: 101 KEEP / 67 REFINE / 6 DISTILL / 7 MERGE / 7 PRUNE / 0
  CUT** across 188 scored elements. As with the original action audit, the corpus is
  over-articulated in its *documentation and legibility contracts*, not junk-laden in its
  *mechanisms* — 77% of subtractive verdicts are REFINE (the mechanism stays, its naming/currency/
  display contract gets fixed), and zero elements were CUT outright.
- **New, corpus-level rolling-engine finding:** the Thread Operations resolver is confirmed
  NON-COMPLIANT — it imports only the legacy discrete `roll_pool`, never the shared
  `sigma_leverage` substrate that Personal Combat and Social Contest both migrated to, and
  reimplements its own divergent Overwhelming threshold (`net ≥ Ob+3`) found nowhere else in the
  corpus. This is the single highest-value migration target found by this pass.
- **The attribute-roster conflict is worse than the crunch-cascade audit scoped it:** not a 2-way
  (glossary vs descriptor_registry) or 3-way question — it is a confirmed **7-vs-9-vs-10-way**
  conflict, with a fourth independent witness (`alias_registry.yaml`) hand-copying the glossary's
  stale 7, and `params/core.md`'s 10th attribute ("Recall") appearing in neither of the other two
  rosters at all.
- **Piety Track vs. Persuasion Track is resolved definitively:** these are not the same mechanic
  under two names. The live 0–10 debate tracker is Persuasion Track; the glossary's "Piety Track
  (CT)" entry misnames it *and* cites the wrong canonical home file (which actually describes an
  unrelated Conviction-Scar mechanic). Already tracked open as ED-SC-0003, needs-Jordan.
- **The Interaction Type label mismatch is confirmed and is not cosmetic:** the glossary's
  CLASH/AMPLIFY/CROSS/DIVERGE does not match the live kernel's CLASH/REINFORCE/CROSS/TIE — and two
  of the four labels (DIVERGE vs. TIE) do not even correspond to the same underlying condition.
- **The hardcode registry's #1 worst offender is a system-level finding, not a term-level one:**
  the Godot typed export (`combat_engine_v1.json`) is generated by a script that imports only
  `config.py` and never the sibling `core.py` where the live Combat Pool formula
  (`max(5,History+6)`) actually lives — so the one pipeline built specifically to prevent
  hand-transcription drift cannot itself emit the corpus's most-audited value. One batch's
  step-4 classification called this "a correct scoping boundary, not a gap"; the registry's
  synthesis explicitly overrules that at the system level.
- **RS (Rendering Stability) survives far beyond the one historical-annotation exception the
  glossary claims:** confirmed 25+ live bare-"RS" occurrences in `params/threadwork.md` alone plus
  17 in the co-filed integration spec — an order-of-magnitude undercount in the glossary's own
  Part Twelve collision table.

## Next actions

This audit proposes; it does not rule. Every P1 item across the five deliverables should be
triaged against `canon/editorial_ledger.jsonl` before being filed as new — several items this pass
flagged as "NEW" in a term batch were found, on cross-check, to already have an open or
ratified-but-unexecuted ED (see each deliverable's currency corrections). Recommended entry points:
the Thread-engine migration (§04, Engine choice, row "Thread operations"), the attribute-roster
ratification (§03 row 1 / §05 §1A), and the Godot export gap (§05 Worst Offender #1).
