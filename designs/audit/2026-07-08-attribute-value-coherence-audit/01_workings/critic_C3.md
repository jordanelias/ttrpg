# Critic pass — C3 (Pools)

Antagonist relay over `dossier_C3.md` (independent read-only verification).

## Verdicts

| target | verdict | reason (condensed, evidence-cited) |
|---|---|---|
| C3-F1 | **uphold** | Fully re-verified: knots_v30.md:37 table (Bonds×2)+3 min5; :76 §3.2 Spirit×2+History(Rel) no +3; fieldwork_v30.md:473 bare "Spirit pool (Spirit × 2) vs TN 7, Ob 2"; sim/personal/knots.py:213-215 pool=(spirit*2)+history_rel. Four distinct formulas at the cited lines; ED-912 (knots_v30.md:45-58) resolved only TIER-DRIFT/COMPOSURE-DRIFT. P1/collision/NEW correct. |
| C3-F2 | **uphold** | test_knots_ed912.py has exactly 7 test_* functions (:50-119), zero 'pool' hits — the oracle's formation formula is untested. |
| C3-F3 | **uphold** | registry:110 pools (dice-size, 7 items) vs module_contracts `bucket: pool` (resource meter — Coherence :288, Stamina :822, political :645), no reconciling note; Stamina kind mismatch verified (registry:107 derived_value vs contracts:822 pool). Coherence's total registry absence (see C3-MISSED-2) strengthens the point. |
| C3-F4 | **soften** (calibration NEW→KNOWN-UNTRACKED; naming default flagged) | Collision real (ci_political_v30.md:161 §3.4 vs derived_stats_v30.md:590; no cross-reference). But mechanical_terms_index.md:192 already canonicalizes "Political Pool" (Faction/Mandate Pool deprecated) and collision_registry.yaml's active_violations flags the same pair; the sibling census (quantity_census.md:239) cites this chain. U3's fresh name "Parliamentary Vote Tally" would mint a third label against prior art — surfaced, not picked. |
| C3-F5 | **uphold** | params/mass_combat.md:62 and mass_battle_v30.md:28-30,443 carry inline ED-899/ED-1013 caveats; derived_stats_v30.md:589 alone lacks any. Narrowing of census F-DESIGN-3 accurate (the :443 caveat is a parenthetical vs the :28-30 blockquote — degree, not error). |
| C3-F6 | **uphold** | module_contracts mass_battle block (:458+) has `state: []` — no representation of the live pool formula, unlike personal_combat's resolver-comment pin (:810). |
| C3-F7 | **uphold** (citation-precision slip noted) | threadwork_v30.md:968 and :1008 state the struck Att+Focus Mending pool as current; the actual in-doc correction is at :455/:458, not the cited :452-453 (an unrelated R-56 note). Claim holds exactly as described. |
| C3-F8 | **uphold** | social_contest_v30.md defines Argue Pool = (Primary×2)+History with genre/orientation dice "added to the Argue pool at Step 3" (~:88, restated ~:490), while derived_stats_v30.md:585 folds "+ style" into the formula; contracts pin no formula. ED-SC-0004 correctly cited as feed (HANDOFF_SC.md:101,127), SC lane respected. |
| C3-F9 | **uphold** | quantity_census.md's Knot Pool row (:275-277) cites only F-REG-013 and never surfaces the formula divergence — genuine census gap. |
| C3-F10 | **uphold** | derived_stats_v30.md:515 (§13 "What Does NOT Change") states the struck (Agi×2)+History+3 as current while :584 (§14.4) says STRUCK 2026-06-04 (ED-901) — intra-document contradiction beyond the shared baseline; correctly KT via ED-1084. |
| U1 | **soften** | Correctly routed to Jordan via ED-920, but ED-920's ledger text (editorial_ledger.jsonl:189) scopes it to the fieldwork bare-Spirit deviation only — folding the Bonds-vs-Spirit table/procedure contradiction in silently widens an open docket item's scope. Flag the widening explicitly (done in OPT-AV-9). |
| U2 | **uphold** | Neutral vocabulary bookkeeping, IN lane; both bucket:pool sites carry [ASSUMPTION]; "reservoir" doesn't collide (checked). |
| U3 | **soften** | Should reconcile with the prior-art "Political Pool" recommendation rather than mint a third name (see F4). |
| U4 | **uphold** | IN-lane contract hygiene citing live ED-1013; no design call. |
| U5 | **uphold** | Housekeeping aligning the doc with rulings already made (ED-901/899/1013). |
| U6 | **uphold** | Gated on U1; FI/sim test-coverage debt. |

## Missed findings

**C3-MISSED-1 · P2 · synonym · KNOWN-UNTRACKED** — An entire pre-existing naming-collision lane
directly on point was never consulted: mechanical_terms_index.md:192,1475,1483 (canonicalizes
"Political Pool"; deprecates Faction/Mandate Pool), collision_registry.yaml:6-9 (same collision,
same §3.4 source), plus silo_overlap_matrix.yaml + name_collision_database.yaml cataloguing
Combat/Argue/Fieldwork/Thread Pool naming from the 2026-05-10 sweep. The sibling census
(quantity_census.md:239) already cites this chain. Recalibrates C3-F4 and is itself a dossier
coverage gap. No ED owns it.

**C3-MISSED-2 · P2 · unregistered · NEW** — **Coherence is completely absent from
descriptor_registry.yaml** (full-file grep: zero matches in derived_values/tracks/clocks/pools)
despite being load-bearing (stat_deltas type:coherence), `bucket: pool` [ASSUMPTION] at
module_contracts.yaml:288, and a §14.2 Track at derived_stats_v30.md:563 — a three-way state
(absent / pool / track) that F3 gestured at via Stamina but never named for Coherence.
*Synthesis note: deduped into C7-F2 (same quantity, sharpened there with the ED-830 lineage);
counted once.*

## Conformance note

Mostly clean. No invented criteria; no fork ruled outright (U1/U3 defaults routed to Jordan via
ED-920/FA/IN feeds, rule e); lane scoping respected (ED-SC-0004 deferred as a feed). Deductions:
(1) C3-F7 cites :452-453 for a correction actually at :455/:458 — precision slip, not a false
claim; (2) U1 quietly widens ED-920's ledger scope without flagging it; (3) the dossier never
checked the existing naming-collision registries its own sibling census uses — softening F4 and
constituting a coverage gap (MISSED-1). No build-state-as-verdict instances.
