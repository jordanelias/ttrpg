# Social Contest — Mode D: Gap Detection

**Audit date:** 2026-07-13
**Target:** `designs/scene/social_contest_v30.md` (+ `_index`/`_infill`), `params/contest.md`

Per the skill's Output Rules: P1 gaps below are dispositioned as `PROPOSED-ED, lane=SC`
(not appended to a YAML file — actual ED-<LANE>-NNNN allocation happens in a later sequential step
of this run, per the orchestrating instructions). Lower-severity items resolve to an explicit
no-action line, including citations to the extensive existing `ED-SC-0001..0015` ledger and the
2026-07-05 Fable-5 audit's `KT-`/`KU-`/`N-` finding IDs where this pass's finding overlaps or
confirms prior work.

| ID | Type | Description | Location | Severity | Status |
|---|---|---|---|---|---|
| G-1 | Referenced but underdefined | Practitioner Weaving (§9.3, R-65): "adds bonus dice: floor(TS÷30)" — the target roll is never named. "Must declare before rolling" (singular) implies a specific roll, most plausibly Argue (§4 Step 3), but Appraise is also plausible (a practitioner reading the room with Thread-sight) and the text does not exclude either. `params/contest.md`'s "Practitioner Weaving" entry repeats the same unqualified phrasing. | `social_contest_v30.md` §9.3 L551–552; `params/contest.md` "Practitioner Weaving (R-65)" L262–263 | P2 | **PROPOSED-ED, lane=SC** |
| G-2 | Formula/citation gap (cross-ref to formula_audit.md F-A13) | Succession Contest §7.2.1 split-ratio table cites "stress-test ED-762," which resolves in `canon/editorial_ledger.jsonl` to an unrelated *resolved* entry about doc-migration spec progression (a different topic entirely), which itself self-flags `_migration_flag: "ID-CONFLICT"` and carries a dangling `_migration_alt` fragment showing the succession-contest rationale was orphaned during the 2026-06-28 ledger migration and never re-filed under its own ID. The table's own internal ratios are additionally non-monotonic in a way inconsistent with its stated "track-distance weighted" framing (see formula_audit.md F-A13 for the full derivation). | `social_contest_v30.md` §7.2.1 L415–429 | P1 | **PROPOSED-ED, lane=SC** (filed jointly with F-A13; do not double-file — this is the same underlying defect viewed from the citation-integrity angle) |
| G-3 | Missing edge-case rule (cross-ref to formula_audit.md F-A6) | CROSS interaction: when floor(successes÷2) produces equal per-side movement from unequal raw successes, "direction toward the side with larger movement" and the Obscuring→Doubt-Marker branch have no defined behavior (not caught by the TIE rule, which triggers on equal *raw successes*, not equal *floored movement*). | `social_contest_v30.md` §4 Step 4 CROSS, L198–203 | P2 | **PROPOSED-ED, lane=SC** (filed jointly with F-A6) |
| G-4 | Orphaned/pending-design stub, self-flagged in-doc | Niflhel Social Toolkit (§9.7): "[EDITORIAL: ED-041 — full Niflhel social toolkit pending design.]" | `social_contest_v30.md` §9.7 L581–585 | P2 | No action — already tracked in-doc (`ED-041`, "Carried forward" table, §12) |
| G-5 | Open decision, self-flagged in-doc | Terminal Doubt resolution mechanism split (banded vs raw-tally) is "OPEN DECISION FOR JORDAN" | `social_contest_v30.md` §4 Step 4, L217 | P2 | No action — already tracked, `ED-1060` |
| G-6 | Open decision, self-flagged in-doc | Piety Track name collision (0–10 debate tracker vs per-territory BG stat) | Transitively referenced via `scale_transitions_v30.md` §5.4 domain-echo composition | P2 | No action — already tracked, `ED-SC-0003` |
| G-7 | Open decision, self-flagged in-doc | Argue-pool formula fork (legacy stub vs promoted kernel) | `sim/personal/contest/` vs `social_contest_v30.md` §3 | P1 | No action — already tracked, `ED-SC-0004` |
| G-8 | Open decision, self-flagged in-doc | Non-attribute bonus-die stacking cap value (Recall/Corroborate/Prep/Findings) — "whether to cap" resolved, exact numeric ceiling still open | `social_contest_v30.md` §4 Step 3, L89; `params/contest.md` L65–71 | P2 | No action — already tracked, `ED-SC-0005` |
| G-9 | Open decision, self-flagged | Total-Victory Mandate rider (−1) vs Censure target effect (−1) stacking to −2, implemented as literal-default stacking, not ratified | `CURRENT.md` Social-contest row; `sim/provincial/parliamentary_action.py`/`sim/personal/parliamentary_vote.py` | P1 | No action — already tracked, `ED-SC-0015` |
| G-10 | Unwired mechanic (spec exists, code doesn't consume it) | General strain≥Face→Rattled channel (the −1D-per-mark cascade, 2-mark incapacitation, Knot-buffer redirect) has no CLASH/REINFORCE-strain caller in the kernel; only the narrow CR5 self-backfire strip channel is wired | `social_contest_v30.md` §4 Step 6, §8 CR3-Face status block; `sim/personal/contest/primitives.py`/`resolver.py` | P2 | No action — already tracked and honestly self-flagged in-doc; corresponds to Fable-5 finding `KU-3` |
| G-11 | Unwired mechanic | Promoted kernel (`build_contest`/`resolve_contest`) reachability from the campaign loop — historically the deprecated raw-dice stub was the only reachable path | `sim/cross_scale/scene_dispatch.py` | P1 (historical) | No action — already tracked and **resolved**, `ED-SC-0006` (resolved 2026-07-05/2026-07-08; corresponds to Fable-5 finding `N-1`) |
| G-12 | Unwired mechanic | `sim/cross_scale/domain_echo.py` had no caller, `scene_dispatch` passed an empty payload | `sim/cross_scale/domain_echo.py`, `scene_dispatch.py` | P1 (historical) | No action — already tracked and **resolved**, `ED-SC-0007` (resolved; ECHO_TRANSPORT default-on per CURRENT.md 2026-07-08) |
| G-13 | Stale contract entry | `references/module_contracts.yaml` social_contest entry predates the Stage 1b–3 δσ-substrate rebuild (still reads `resolver: dice_pool`) | `references/module_contracts.yaml` L425–447 | P2 | No action — already tracked, `ED-SC-0008` |
| G-14 | Narrative-surface gap | Kernel's `Chronicle`/`classify()` narrative output carries no focalization/chronicler field; renders neutral omniscient summaries — P-03 concern if ever player-facing | `sim/personal/contest/narrative.py` | P3 | No action — already tracked, `ED-SC-0010`; see also core_principles_audit.md P-03 |
| G-15 | Stale downstream doc | `designs/ui/valoria_ui_ux_v4_1.md` Part 6 still specifies the pre-CR3 contest wholesale (Piety Track, Composure damage, Stance Triangle) | `designs/ui/valoria_ui_ux_v4_1.md` L592–649 | P3 | No action — already tracked (Fable-5 finding `N-6`); no dedicated ED-SC row found for it specifically, but it is UPHELD by the independent critic in the finding ledger and covered by the same rebuild-currency sweep as G-13 |
| G-16 | Content-completeness gap (accepted, deferred) | "Four deliberative games / mature-Agôn dominance" — the eight proceeding types currently play as "one game wearing eight venue skins" rather than mechanically distinct deliberative modes | Cross-cutting, §2/§4/§7 proceeding-type tables | P2 (content, not correctness) | No action — already tracked, Fable-5 finding `KT-1`, feeds the ratified Stage-4 sequencing |
| G-17 | Complexity/onboarding gap | ~13 recurring per-decision consultations per Agôn exchange vs the immersion audit's 3–4 personal-scene ceiling; no onboarding/complexity-gating doc exists | Cross-cutting, whole exchange loop §4 | P2 | No action — already tracked, Fable-5 finding `N-7` (UPHELD, caveat ±2 items) |

## New findings this pass (not previously filed)

- **G-1** (Practitioner Weaving target roll unnamed) — genuinely new; small, self-contained fix
  (name the roll the R-65 bonus dice apply to — most plausibly Argue).
- **G-2 / G-3** — new from this pass's independent Mode A derivation; cross-filed with
  `formula_audit.md` F-A13 and F-A6 respectively rather than duplicated as separate ED rows.

## Missing tables check

No missing tables were found for defined mechanics — every roll/formula referenced in the document
that is intended to resolve in play (Argue, Appraise, Corroborate, Pre-Contest Prep, Panel VoteAtClose,
BG Vote) has an accompanying table or explicit formula. The one exception (Practitioner Weaving's bonus
dice) is a missing *target*, not a missing table, and is filed as G-1 above.

## Missing resolution procedures ("what happens when X and Y conflict")

Reviewed for unstated conflict-resolution: multi-Inquisitor filings (§7.3.3 — explicitly resolved,
queue-and-wait or consolidate); simultaneous Stays (§10.1 — "multiple Stays possible, one per
Tribunal-equivalent filing per season" — explicit); Rattled+Spent stacking (§4 Step 6 — explicit,
"cumulative... Pool minimum 1D"); CROSS's own no-strain-overrides-TIE precedence (§4 Step 4 TIE clause —
explicit). The one unstated conflict found is G-3 above (CROSS floor-tie vs Doubt-Marker "larger
movement" language).
