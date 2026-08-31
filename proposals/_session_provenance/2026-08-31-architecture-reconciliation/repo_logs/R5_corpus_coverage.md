# R5 — the proposals corpus: coverage measured, uncited work mined

## 1. METHOD — exactly what you ran, so it is reproducible

**Corpus enumeration.**
```
find proposals -name '*.md' | xargs wc -l | sort -rn
```
191 `.md` files under `proposals/`, 81,360 lines total. Filtered to `$1 > 200` (excluding the `total`
row): **133 files**, saved to `over200.txt`.

**The citing suite, as named by the task.** Six files:
`proposals/2026-08-31-ideal-v2/{01_ARCHITECTURE,02_THE_SEASON_LOOP,03_COMPENDIUM,04_GODOT_IMPLEMENTABILITY}.md`
+ `proposals/2026-08-31-ideal/{10_SUPERSEDING,00_THE_SHAPE}.md` (8,293 lines combined).

**Citation extraction — three passes, because one pass undercounts by an order of magnitude.**
1. `grep -ohE '[A-Za-z0-9_./-]*proposals/[A-Za-z0-9_./-]+\.md'` — full relative paths. **Only 7 hits.**
   Most in-suite citations do **not** carry the `proposals/` prefix (the doc is already inside
   `proposals/`), so this pass alone is the wrong instrument and would have reproduced PR #344's
   undercount-of-what's-cited if trusted alone.
2. `grep -ohE '[A-Za-z0-9_-]+\.md'` — bare filenames. **29 distinct basenames.** Cross-checked each
   against `find proposals -name '<basename>'` for uniqueness; nine basenames appear in more than one
   directory (`00_INDEX.md` x5; eight `NN_*.md` names shared between `2026-08-28-greenfield-systems-suite/`
   and its v2 successor), resolved by reading the citing sentence's surrounding context.
3. **The citation-key table at the top of `01_ARCHITECTURE.md` §0.1**, which is itself the strongest
   evidence: it declares `NN:LLL` as *"line LLL of `proposals/2026-08-29-valoria-from-scratch/NN_*.md`
   — the seventeen-document suite, read directly."* Grepping for the doc-number:line pattern finds
   **doc numbers 01-14 all cited** this way (counts: 01x104, 02x89, 03x123, 04x15, 05x32, 06x6, 07x2,
   08x12, 09x30, 10x10, 11x12, 12x7, 13x15, 14x19). This channel alone accounts for **14 of the ~24
   real external citations** and is invisible to a plain `.md`-filename grep — it is why the true
   cited count is larger than a naive re-run of the PR's own method would find.

Disambiguation of the nine shared basenames: every citing sentence that names a bare `NN_*.md` shared
with the v1 (`2026-08-28-`) suite resolves to the **v2** directory by content match (e.g.
`09_ambitions_and_arcs.md` is quoted at *"1,065 lines"*, which matches only
`2026-08-29-greenfield-systems-suite-v2/09_ambitions_and_arcs.md` + `_part2`, 695+370). `00_INDEX.md`'s
five copies resolve per-citation by the quoted line content (verified individually — the
`valoria-from-scratch/00_INDEX.md:105-109` "Not an audit's call" quote is **not** one of the >200-line
files and does not affect the count).

**Set difference.** `over200.txt` minus the verified cited set = the uncited list, sorted, saved to
`uncited_sorted.txt` (103 rows) and titled (`uncited_titles.txt`).

---

## 2. THE MEASUREMENT

| metric | PR #344's figure | my figure | agree? |
|---|---|---|---|
| Proposal documents >200 lines | 123 | **133** | **no — off by 10** |
| Documents cited by the six-document suite | 15 (123-108) | **30** (24 external + 6 self) | **no — roughly double** |
| Uncited documents | 108 | **103** | close, both ways of counting land near 80-90% |
| % of >200-line corpus uncited (by doc count) | 87.8% | **77.4%** (103/133) or **81.1%** excluding self (103/127) | no, but same order |
| % of >200-line corpus uncited (by line count) | not stated | **67.7%** (51,111 / 75,453 lines) | — |
| Total corpus lines (all `.md`, not just >200) | not stated | **81,360** | — |

**Why the discrepancy, and it is not noise.** `01_ARCHITECTURE.md` in the **current working tree**
already carries a self-correction section (roughly lines 1440-2180) that was **added after** PR #344's
warning text was written — it directly quotes and answers the PR body's own five bullet points
(`11_world_events.md`, `09_ambitions_and_arcs.md`, `10_the_slate_and_salience.md`,
`02_the_act_economy.md`, `03_knowledge_telling_investigation.md`), and it independently found **nine
more** valoria-from-scratch documents (01, 02, 04, 05, 06, 07, 08, 12, 13, 14) via the `NN:LLL`
citation channel that the PR's own headline text does not mention. **The PR body describes an earlier
state of the suite; the working tree has since partially — not remotely fully — closed the gap it
describes.** Both numbers are true of their own moment. Reading PR #344's 108/123 as the current state
would be exactly the stale-number failure this repo's own CLAUDE.md keeps finding elsewhere.

Also material: `133` includes 23 files under `2026-08-31-ideal/`, `2026-08-31-ideal-v2/`,
`2026-08-31-integration/` and `_session_provenance/` — the review/synthesis apparatus surrounding the
citing suite itself, some of which postdates PR #344's own count (`2026-08-31-integration/` in
particular reads as a *second*, later synthesis pass — see §5's finding on it). If PR #344's 123 was
counted before that directory existed, the arithmetic reconciles almost exactly: 133 minus 12 (the
`integration/` files) = 121, close to 123 within rounding on which borderline files were >200 lines at
count time.

**Bottom line, stated the way the task asked for it:** the true coverage is worse in absolute document
count than PR #344 said (133 not 123 candidates) but meaningfully *better* in what has actually been
read (30 not 15 touched) — and still catastrophically incomplete: **just under 70% of the corpus's own
line-weight, and four in five of its documents, remain outside the citing suite's field of view.**

---

## 3. THE FULL UNCITED LIST

Priority: **H** = large, likely-fresh mechanism, not yet superseded, not process/audit apparatus.
**M** = smaller mechanism, worked example, or fix filed against a document ideal-v2 partially reads.
**L** = process, audit-of-audit, superseded-suite duplicate, or pure narrative probe.

| path | lines | subject | architecture? | priority |
|---|---:|---|---|---|
| `2026-08-15-character-and-faction-stats-and-progression.md` | 1676 | attribute/faction stat census measured from running code; rounding-fix census; progression scaffold | y | H |
| `2026-08-21-execution-order-v1.md` | 1154 | repo process — session ordering for the culling/centralization program | n | L |
| `2026-08-31-integration/04_integration_a_npc_matrix.md` | 1050 | a **second**, parallel synthesis of #342 + play-space-coverage + fixes into an NPC/season matrix — sibling to ideal-v2, uncited by it | y | H |
| `2026-08-18-fieldwork-architecture-and-nonadversarial-play.md` | 1032 | the FI architecture that `03_knowledge_telling_investigation.md` itself reads and composes on | y | H |
| `2026-08-30-arc-reachability/02_arcs_19_40.md` | 1005 | read-only: can #342 reproduce canon arcs 19-40 | n (evidence, not mechanism) | M |
| `_session_provenance/.../v2/KEYS_AUDIT.md` | 982 | one of five audit runners' raw output against an earlier `ARCH_CORE.md` draft | n | L |
| `2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md` | 971 | PC-lane (deferred by ideal-v2's own scope) | y (deferred lane) | M |
| `2026-08-25-throughlines-and-precedent/06_ch3_one_resolver_four_scales_one_scalar.md` | 854 | cross-scale resolver analysis, prior throughlines corpus | y | M |
| `2026-08-18-breaking-the-recursion.md` | 852 | diagnosis of the repo's apparatus-growth loop; **§4.5 finds the tenth attribute is `Recall`, already shipped in Godot** | y (one load-bearing finding) | H |
| `2026-08-30-play-space-coverage/03_seasons_church.md` | 833 | worked Church-lane season probe | n (evidence) | M |
| `2026-08-30-play-space-coverage/06_seasons_without_office.md` | 819 | worked postless-character season probe | n (evidence) | M |
| `2026-08-30-play-space-coverage/04_seasons_duchies.md` | 805 | worked Duchies-lane season probe | n (evidence) | M |
| `2026-08-30-play-space-coverage/02_seasons_crown.md` | 796 | worked Crown-lane season probe (source of the King-is-THIN finding) | n (evidence) | M |
| `2026-08-18-recursion-interrogation-log.md` | 794 | working log behind `breaking-the-recursion.md` | n | L |
| `2026-08-29-greenfield-systems-suite-v2/01_substrate_primitives.md` | 786 | **the four primitives (Entity/Tag/Post/Gauge), the write-rule, `derive_ob`** — the base every cited 09/10/11 document composes on | y | H |
| `social_contest_consolidation_integration_v1.md` | 781 | SC-lane (deferred) | y (deferred lane) | M |
| `2026-08-30-arc-reachability/01_arcs_01_18.md` | 774 | read-only arc reachability, lane 1 | n | L |
| `2026-08-25-throughlines-and-precedent/05_ch2_the_ladder_runs_both_ways.md` | 758 | prior throughlines corpus, resolver ladder | y | M |
| `2026-08-29-greenfield-systems-suite-v2/04_personnel_management.md` | 747 | office/personnel management module | y | H |
| `2026-08-29-greenfield-systems-suite-v2/05_faction_actions_part2.md` | 733 | faction action resolution, contracts, audit | y | H |
| `2026-08-30-play-space-coverage/05_seasons_sword_and_shadow.md` | 709 | worked covert-lane season probe | n (evidence) | M |
| `2026-08-30-play-space-coverage/07_seasons_edges_and_ground.md` | 702 | worked frontier-lane season probe (control case, Alvid Bekk) | n (evidence) | M |
| `2026-08-29-greenfield-systems-suite-v2/07_places_and_settlements.md` | 681 | Place object, growth/decay, presences, terrain | y | H |
| `2026-08-29-greenfield-systems-suite-v2/05_faction_actions.md` | 680 | faction actions, every tier | y | H |
| `2026-08-31-integration/05_integration_b_arcs.md` | 679 | integration lane (b), the arcs — sibling to ideal-v2 | y | H |
| `2026-08-25-throughlines-and-precedent/03_method_and_corrections.md` | 678 | method notes, prior corpus | n | L |
| `2026-08-29-greenfield-systems-suite-v2/12_adjacent_systems.md` | 669 | adjacent systems (mass battle/PC/SC seams) | y | M |
| `2026-08-30-arc-reachability/03_arcs_41_55_and_emergent.md` | 638 | read-only arc reachability, lane 3 | n | L |
| `2026-08-29-greenfield-systems-suite-v2/03_world_population.md` | 638 | world population — who exists, how many | y | H |
| `2026-08-31-integration/11_INTEGRATED.md` | 633 | the integration effort's own synthesis of NPC matrix + arcs | y | H |
| `2026-08-25-throughlines-and-precedent/04_ch1_the_world_has_no_people.md` | 630 | prior corpus, population-absence diagnosis (root cause E's ancestor) | y | M |
| `2026-08-29-greenfield-systems-suite-v2/06_faction_management.md` | 625 | faction management, ethos, divergence, blocs | y | H |
| `2026-08-29-greenfield-systems-suite-v2/02_character_generation.md` | 621 | character generation — life paths, caste, heritage | y | H |
| `2026-08-29-greenfield-systems-suite-v2/01_substrate_primitives_part2.md` | 605 | edges, disclosure, the herald, module contracts | y | H |
| `_session_provenance/.../FABLE_FINDINGS.md` | 601 | raw adversarial findings behind `10_SUPERSEDING.md`/REV | n | L |
| `2026-08-29-greenfield-systems-suite-v2/00_INDEX.md` | 582 | the v2 suite's own index, playing-surface budget, hierarchy | y | H |
| `2026-08-28-greenfield-systems-suite/01_substrate_primitives.md` | 575 | **v1** substrate — superseded in place by v2's own | n (superseded) | L |
| `2026-08-30-fixes/05_the_blocked_cores.md` | 573 | disposition on 19 BLOCKED-CORE characters found by play-space-coverage | y | H |
| `2026-08-22-session-master-log-fieldwork-to-delta.md` | 565 | process log | n | L |
| `2026-08-29-greenfield-systems-suite-v2/08_settlement_management.md` | 526 | settlement management, the governor's one decision | y | M |
| `2026-08-24-error-regions-v1.md` | 526 | executable process plan | n | L |
| `valoria_fork_plan_of_record_v1.md` | 522 | repo-fork/architecture-boundary plan (2026-08-03, Class A) | n (process, not game mechanism) | M |
| `2026-08-25-throughlines-and-precedent/08_ch5_what_we_should_not_do.md` | 506 | prior corpus, negative-space design guidance | y | M |
| `2026-08-20-return-to-game-plan-v1.md` | 489 | process plan | n | L |
| `2026-08-22-wiring-map.md` | 474 | process — coded vs designed connection map | n | L |
| `2026-08-30-fixes/03_the_missing_needs.md` | 463 | fixes D-3: `need(commitment)`/`need(exposure)` formulas, uncomputed for magnates | y | H |
| `2026-08-29-greenfield-systems-suite-v2/06_faction_management_part2.md` | 455 | faction management contracts/audit | y | M |
| `2026-08-23-suite-02-narrative-texture-census.md` | 446 | census, earlier vocabulary suite | n | L |
| `2026-08-30-fixes/01_the_floor.md` | 445 | fix D-1, the design's floor (ordinary-capability character) | y | H |
| `2026-08-18-culling-plan-v1.md` | 431 | apparatus-culling process plan | n | L |
| `2026-08-23-competing-vocabularies-index.md` | 418 | earlier vocabulary-collision index | n (superseded content) | M |
| `2026-08-23-MASTER-vocabulary-and-rulings.md` | 416 | earlier vocabulary rulings | n (superseded content) | M |
| `2026-08-28-greenfield-systems-suite/04_personnel_management.md` | 412 | **v1**, superseded by v2's own 04 | n (superseded) | L |
| `2026-08-28-greenfield-systems-suite/05_faction_actions.md` | 409 | **v1**, superseded | n (superseded) | L |
| `2026-08-30-play-space-coverage/01_the_machine.md` | 387 | the tick/rung/degree/remit instrument used by the season probes | y | M |
| `2026-08-29-valoria-from-scratch/15_adjudications.md` | 379 | **genuinely uncited doc of #342 itself** — the adjudication register (A/B-numbered rulings) | y | H |
| `2026-08-23-suite-03-competing-vocabularies.md` | 378 | earlier vocabulary suite | n | L |
| `2026-08-28-greenfield-systems-suite/09_adjacent_systems.md` | 364 | v1, superseded | n | L |
| `2026-08-30-play-space-coverage/08_coverage_matrix.md` | 360 | the populated 6x coverage matrix behind the gap report | y | M |
| `2026-08-30-fixes/04_relational_at_settlement.md` | 360 | fix D-4/D-5: relational is empty at Settlement/Territory; no councillor venue | y | H |
| `_session_provenance/.../v2/REVISIONS.md` | 348 | audit-runner dispositions against an earlier `ARCH_CORE.md` draft | n | L |
| `canonical_nomenclature_v1.md` | 342 | namespaced-identifier plan (see §6) | y | H |
| `2026-08-28-greenfield-systems-suite/08_settlement_management.md` | 341 | v1, superseded | n | L |
| `grounded_event_card_deck_v1.md` | 335 | 58 event cards bound to `governance_ripple_substrate_v1.md` (itself uncited by `systems/`) | y | M |
| `2026-08-29-valoria-from-scratch/16_ners_audit.md` | 334 | **genuinely uncited doc of #342 itself** — pessimistic steelman NERS audit | y | M |
| `2026-08-25-throughlines-and-precedent/07_ch4_weights_bias_noise_chooses.md` | 328 | prior corpus | y | M |
| `2026-08-28-greenfield-systems-suite/02_character_generation.md` | 315 | v1, superseded | n | L |
| `2026-08-29-greenfield-systems-suite-v2/13_handoff_build_order.md` | 311 | v2's own build-order/impact-class handoff | y | M |
| `2026-08-23-suite-01-rulings-and-execution.md` | 309 | earlier ruling record | n | L |
| `2026-08-28-greenfield-systems-suite/00_INDEX.md` | 308 | v1, superseded | n | L |
| `2026-08-24-completion-plan-v1.md` | 308 | process plan | n | L |
| `2026-08-28-greenfield-systems-suite/07_places_and_settlements.md` | 305 | v1, superseded | n | L |
| `2026-08-18-next-session-handoff.md` | 303 | process handoff | n | L |
| `2026-08-16-system-scores-census.md` | 301 | every attribute/score by system, census | y | M |
| `2026-08-25-throughlines-and-precedent/01_verified_defects.md` | 300 | prior corpus, defects at an old HEAD | n | L |
| `2026-08-29-greenfield-systems-suite-v2/02_character_generation_part2.md` | 299 | determinism, surface, contracts, audit | y | M |
| `2026-08-28-greenfield-systems-suite/06_faction_management.md` | 294 | v1, superseded | n | L |
| `pc_formation_system.md` | 287 | PC-lane formation system (deferred) | y (deferred lane) | M |
| `mass_battle_fighting_withdrawal_v1.md` | 286 | MB-lane fighting-withdrawal mechanic (deferred) | y (deferred lane) | M |
| `2026-08-28-greenfield-systems-suite/03_world_population.md` | 280 | v1, superseded | n | L |
| `2026-08-24-suite-07-reconciliation-against-main.md` | 277 | reconciliation record | n | L |
| `2026-08-19-obstacle-stat-and-identity-census.md` | 272 | census behind earlier B1/B2/B3 rulings | y | M |
| `2026-08-23-rulings-and-adversarial-review.md` | 267 | earlier ruling record | n | L |
| `2026-08-18-epistemic-propositions-and-provenance.md` | 265 | the belief-layer origin doc — five Jordan rulings P1-P5, cited AS a source by `09_ambitions_and_arcs.md` O-A5 but not read directly by ideal-v2 | y | H |
| `2026-08-29-fable5-throughline-critique/02_findings_T4_T6.md` | 262 | throughline critique against greenfield v2 PR #340 | n (audit) | M |
| `2026-08-23-suite-04-wiring-gaps-and-orphans.md` | 261 | earlier wiring-gap census | n | L |
| `2026-08-19-subsystem-delta-and-narrative-robustness.md` | 257 | delta between designed and built | n | L |
| `2026-08-29-fable5-throughline-critique/01_findings_T1_T3.md` | 256 | throughline critique | n (audit) | M |
| `2026-08-28-greenfield-systems-suite/10_handoff_build_order.md` | 256 | v1, superseded | n | L |
| `2026-08-29-fable5-throughline-critique/03_findings_T7_T9.md` | 250 | throughline critique (T9 field investigation) | n (audit) | M |
| `2026-08-23-suite-06-method-corrections-and-queue.md` | 237 | earlier method notes | n | L |
| `2026-08-19-roll-and-resolution-inventory.md` | 230 | every dice call/obstacle census | y | M |
| `2026-08-31-integration/12_PART3_RECONCILIATION.md` | 219 | integration effort's own relay close | y | M |
| `2026-08-30-play-space-coverage/09_GAP_REPORT.md` | 219 | **the D-1..D-10 gap register** — see §5, §7 | y | H |
| `2026-08-31-integration/06_antagonist_a_npc_matrix.md` | 216 | integration lane (a), antagonist findings | y | M |
| `_session_provenance/.../new6.md` | 213 | "ten changes that would do the most, ranked" — process notes | n | L |
| `2026-08-29-fable5-throughline-critique/00_INDEX.md` | 213 | throughline critique index | n (audit) | M |
| `2026-08-18-ruling-execution-plan.md` | 212 | process plan | n | L |
| `_session_provenance/.../PRECEDENT.md` | 211 | cross-game/historical precedent ammunition for #342 | y (reference material) | M |
| `2026-08-31-integration/07_antagonist_b_arcs.md` | 211 | integration lane (b), antagonist findings | y | M |
| `2026-08-25-throughlines-and-precedent/00_index.md` | 210 | prior corpus index | n | L |
| `2026-08-31-ideal/04_ners_audit.md` | 208 | ideal suite's own NERS audit | n (audit, in-suite) | L |
| `2026-08-31-integration/10_comparative_judgment.md` | 203 | integration effort's analytical spine | y | M |

**103 rows.** L (~48) and M (~35) dominate by count; the H rows (~20) carry the real re-invention risk
and are the subject of §4/§5/§8 below.

---

## 4. THE FIVE NAMED DOCUMENTS

### 4.1 `11_world_events.md` (715 lines) — the actorless event channel

**The complete mechanism.** `world_events:` is a registry block in `references/content_registry.yaml`,
schema-identical to `05`'s (faction-action) row shape with two deltas: `remit_kinds: []` (always empty
— no post-holder invokes it) and `hazard_pool: <int>` (a fixed die-pool size standing in for the
missing actor's attribute pair). Full row shape (`11:114-152`):
```
event, family (Opportunity|Crisis), origin: exogenous, scope (place|faction), remit_kinds: [],
triggers: [...], hazard_pool, resilience {target_score, modifiers, M_max}, cooldown (>=1),
excludes: [...], durability_bp, identity_touch_bp, mandatory, deposits {overwhelming/success/partial/failure},
follow_on {on_fire: {tag: Precedent, key, ttl}}, emits: world.event_fired
```
**Who writes:** nobody — the row is applied by `05`'s own dispatcher (`fa.gate`/`fa.resolve`), extended
to iterate by target instead of by post, and to source its roll pool from `hazard_pool`. **Zero new
module contracts** (`11 §6`). **Who reads:** whatever module already gates on the deposited
gauge/tag — `08`'s `sm.act` for the three place-scoped rows; nothing yet for the fourth
(`we.altonian_pressure`, deliberately shipped as a **known-failing** worked example, `11 §4.2`).
**When it ticks:** at the accounting boundary, gated (never rolled) on terrain/season/gauge-band/tag
predicates (`11 §2.1`); rolled via `roll_pool(hazard_pool)` against `derive_ob(target_score, modifiers)`,
the ratified margin ladder (`11 §2.2`) — reused, not reinvented. **Rate-bounded three ways**: G-1 (one
fire per target per season, structural), `cooldown >= 1` per row, and a load-time check against
`DEFAULT_EMISSIONS_PER_TICK_MAX = 64` (`11 §3`). **Persistence is a Tag, never a scheduled Key** — the
substrate has no cross-season latency (verified against `engine/substrate/keys.py`), so a "drought
lasting three seasons" is three independent seasons of the same row re-gating on a `follow_on` Tag with
a `ttl` (`11 §2.4`, filed as **J-N**). **What it refuses:** designing salience/ranking (`10` owns it),
firing a form transition directly (only `gauge_deposit`/`tag_append`), writing an aggregate (AU-1), a
bespoke roller (reuses `d_sigma`/`derive_ob`), a new `world` Entity kind (the top-tier `place` node at
`tier: country` already is one), a second surfacing path (routes through the Slate). Every literal key
name introduced: `origin: exogenous` (schema field), `institutional_pressure` (a proposed new Gauge on
the top-tier place node, unconfirmed by `07`/`12`), `route_cut:<place>` (a proposed shared Tag key),
`we.crop_failure`/`we.plague`/`we.route_severed`/`we.altonian_pressure` (the four worked rows).

**What ideal-v2 said, quoted on both sides.** ideal-v2's `01_ARCHITECTURE.md §7 F5` originally answered
*"is an off-board polity simulated?"* with *"generate persons, and take no exception"* — an off-map
Rung with minted persons. The suite's own correction (line 1632-1637), now in the tree, reverses this:

> *"AND THE CHANNEL IS ALREADY BUILT, IN A DOCUMENT THIS SUITE DID NOT READ. `.../11_world_events.md`
> (715 lines) ships the actorless event row with rate bounds, two-way reachability and a registry
> block, and it ships **`we.altonian_pressure`** by name ... It also records `external_shock` as
> 'never defined by anything on disk' and states that it is that definition ... So this section is a
> re-derivation, not an invention, and it should be read as a pointer to `11_world_events.md` rather
> than as a design."*

Verdict: **full re-invention, self-corrected in the current working tree.** The correction is honest
and complete for the specific claim (off-board-polity-as-event-source); it does not, however, absorb
`11`'s rate-bound proofs, the `informational`/candidate-contract integration with `10`, or the
`institutional_pressure` open item — those remain unread by ideal-v2 even after the correction.

### 4.2 `09_ambitions_and_arcs.md` + `_part2` (1,065 lines) — ambition's carrier

**The complete mechanism.** A Project is **not a fifth stored primitive** — it is a composition of the
existing four: the intent/target/terms/horizon live as an **`Ambition` Tag** (the seventh tag kind,
argued from `01`'s own two-part test, `09 §2.1`) with `ttl: horizon`; progress is **derived, never
stored** (`09 §3`, cutting a drafted `progress` Gauge, O-A2):
```
progress(P, season) = Sum_i  w_i * [ term_i holds at season ]     # integer basis points
```
Seven closed term kinds: gauge band, form value, tag existence, **tag age** (an addition, closing the
COLLISION shape), post holder, edge state, season index. Four verbs: `am.declare` (the **one** surface
verb, costs one budget point, gated by `remit`), `am.advance`/`am.fire`/`am.lapse` (all **headless**,
herald-run at the boundary, `consumes: []`). Fire is **always a `gate`, never a roll** — the
uncertainty is in getting the world there, not in a second roll at the threshold (`09 §4`). Obstruction
needs **no verb**: any act that moves a term the project reads obstructs it (`09 §5`) — the design's
sharpest cut. §6.4 ships the suite's only **mass actor**: a `place`-bound project kind (e.g. `rising`,
a revolt) **auto-declares** at the boundary when its owner-binding gate holds and auto-lapses when it
stops — the two-signal-resonance shape (objective strain **and** an independent legitimating tag,
matching the researched *"a bare grievance fizzles"* precedent). Arcs are **not an object** — they are
tag chains walked via `Tag.provenance -> Key.causes[]`, a query over the one beat stream, never a store.

**What ideal-v2 said, quoted on both sides.** ideal-v2's F6 resolution (Jordan's *"the world is in
flux"* ruling) originally struck its own claim that ambition has no carrier:

> *"THIS DOCUMENT'S FINDING THAT AMBITION HAS NO CARRIER IS FALSE AND IS STRUCK. IT HAS AT LEAST TWO,
> IN DOCUMENTS THIS SUITE DID NOT READ. 1. `.../09_ambitions_and_arcs.md` + `_part2` (1,065 lines) ships
> ambition as a first-class object with derived-at-read `progress` ... That is the carrier. ... The claim
> struck, in the terms it was made: `'ambition' and goal occur zero times` was true of this suite and
> false of the corpus, and it was made without running the grep it quantified over."*

Verdict: **full re-invention, self-corrected.** The correction absorbs the carrier claim but not §6.4's
mass-actor mechanism, the hook-grammar generalization argument (§4, four named drift guards), or the
`tag age` grammar extension — none of those appear anywhere in ideal-v2's text.

### 4.3 `10_the_slate_and_salience.md` + `_part2` (1,152 lines) — how anything reaches a decider

**The complete mechanism.** The **candidate** is the missing definition the ratified Light Function
(`narrative_engine_design_v2_churn.md §4`, ED-IN-0011) presupposes but never states: a derived,
never-stored value returned by an emitter at the accounting boundary (`10 §2.1`), with six normative
rules (C-1..C-6: required non-empty `provenance`, required non-empty `witness`, realized-state terms
only, an existing `resolver_ref`, 3-5 `responses` from that resolver's own set, and the emitter never
ranks or checks budget). `cast_score` (Slate entry, realized terms only) and `depth_score` (render
depth among the cast, forecast-admitting) are two scores **because the ratified severance says two**
— casting must never key on forecast, or the North-Star loop (surface -> attend -> change state ->
strengthen the forecast) rubber-bands invisibly. Truncation is a five-step algorithm
(`M u E u F u P`: mandatory, exempt-capped, free-pool, reserved-slice) **proved bounded (`|Slate| <= B`)
and monotone** (raising one candidate's score never evicts it or promotes a lower one) — the proof is
load-bearing on the exempt set being a *count cap*, never a *score threshold*. Inertia is derived from
the append-only Key log rather than carried (J-N compliance), with a v3 fix for a real bootstrap
deadlock (`INERTIA_NEUTRAL` at 0 made every cold-start candidate score zero and un-liftable — fixed to
a multiplicative-neutral baseline). Headless resolution is proved invariant under three properties
(P-A fidelity neutrality, P-B baseline parity, P-C order neutrality), secured by a **per-candidate RNG
substream** keyed on `campaign_seed || accounting_index || candidate_id` rather than a shared stream.

**What ideal-v2 said, quoted on both sides.**

> *"14 | Clear, and improved. ... And the general question — how does anything get put in front of a
> decider — is designed at length in `.../10_the_slate_and_salience.md` + `_part2` (1,152 lines),
> which this suite did not read"* (`01_ARCHITECTURE.md:1805`, and restated at :2146).

Verdict: **acknowledged as unread and left unread** — unlike the other four, ideal-v2 does **not**
attempt to re-derive or absorb any of `10`'s content; it simply flags the gap. This is the most honest
of the five disclosures and also the least closed: ideal-v2's own `02_THE_SEASON_LOOP.md` still has to
answer "what surfaces this season" for its worked seasons, and it does so without `10`'s candidate
contract, cast gate or truncation proof anywhere in evidence.

### 4.4 `02_the_act_economy.md` (426 lines) — D-2 already worked out

**The complete mechanism.** Reconciles the flat contradiction between `09_churning_world §1.1` ("one
act per person per season, universal") and `14_office_and_upper_rungs §8`'s worked ducal season (ten
acts, no faction verbs). **Reading C**, chosen on the strength of a discriminating measurement (56
coverage-exercise probes, not argument): an office-holder's own act count is always exactly one; an
office's **throughput** is its **establishment**'s acts — every establishment member is an ordinary
person under the same one-act rule, with their own `choose`, own needs, and standing right to refuse.
`dispatch` costs **both** parties an act and names exactly one person. The derived count:
```
acts_in_a_holder's_season = 1 + |{m in establishment(o) : m's own choose selected an act serving the office}|
```
Discriminating evidence, verbatim from the coverage matrix: *"Among office-holders: an empty or
unreachable establishment, never a small remit ... The design prices remit and forgets establishment"* —
which falsified both competing readings (flat-one-act, and budget-scales-with-office) and confirmed C
at 100% within its class.

**What ideal-v2 said, quoted on both sides.**

> *"THIS RESOLUTION MAY BE A RE-DERIVATION AND IS NOT PRESENTED AS NOVEL. `.../02_the_act_economy.md`
> (426 lines) is D-2 already worked out, and this suite did not read it. Read it before treating
> anything below as the design's answer ... ONE ACT PER PERSON OR COHORT PER SEASON. UNIVERSALLY. ...
> An office's throughput is its ESTABLISHMENT's acts — and every member of an establishment is a named
> person who has exactly one act, their own stance, their own ledger, and the standing option to
> refuse, comply badly, or defect."* (`01_ARCHITECTURE.md §7 D-2`)

Verdict: **exact re-derivation, independently reached, self-disclosed.** This is the cleanest
convergence in the corpus — same conclusion, same discriminating shape (establishment as the missing
unit), reached from a different route and correctly flagged by ideal-v2 as unread-but-matching rather
than claimed as original.

### 4.5 `03_knowledge_telling_investigation.md` (980 lines) — the never-read document

**The complete mechanism** (abbreviated; the full field list is in §8 below). `Claim = (subject,
predicate, value, when, source, confidence, visibility)`. **Fourteen closed predicate forms**
(`LOCATED, DID, HOLDS, MARKED, CONDITION, ALIGNED, TIED, QUANTITY, IN_FORCE, INTENDS, SAID, CAUSED,
CONTRADICTED, HOLDS_STANCE`) over an **open referent space** — closure binds the three operations
(collision, entailment, relevance), not the argument space. `witness` runs two stages — **registration**
(vantage x capability, a hard floor for rendering-side facets) then **construal** (a small closed set
of readings per `act_kind`, indexed by kind never by entity, selected by a Conviction-weighted score) —
so two honest witnesses can register identical facets and construe opposite meanings; construals
deposit `source: inferred`, so agreement among them never corroborates. `tell` computes a **deception
delta** (delta = distance(as_asserted, held)) (sincere/lie/overclaim/false-witness/invention) from one
Speaker-pool/Hearer-pool contest, and **unconditionally deposits `SAID(speaker, content, when, place)`
regardless of outcome** — the single most load-bearing sentence in the document, and the entire raw
material of investigation. Corroboration has **exactly one minting operation** (`firsthand`), everything
else copies or unions tokens, with a `x2.0` cap so no crowd size makes a claim unfalsifiable. Six
field-investigation acts (`examine, interview, research, surveil, reconstruct, Thread-Read`), each a
real pool against a real obstacle (`retention(f)`, world-set, never a person's whim), available to
**any** person regardless of office. Concealment/exposure is a paired counter
(`P(discover) = 1 - exp(-pressure*exposure/theta)`) that is provably safe-at-rest and provably
discoverable-under-spend. P-08 (the Thread-sensitivity barrier) is implemented **in the hearer's ledger
referent space**, not on any channel — a non-sensitive's ledger literally has no address for a
rendering-side subject, so study cannot cross it by any route, closing a hole the document's own
earlier draft left open (tell-side-only degradation, routable via `research`).

**What ideal-v2 said, quoted on both sides.**

> *"THE MECHANISM BEHIND LIMIT 8 IS HOW THE SUITE WAS AUDITED. `.../03_knowledge_telling_investigation.md`
> — 980 lines, the largest document in #342 and the declared owner of the claim, the predicate
> vocabulary, view assembly, salience, corroboration, concealment and field investigation — WAS NEVER
> READ by the prior review, by the five parallel audit runners, by the 982-line keys audit, or by the
> first draft of these three documents. It is cited twice in the 1,823-line review and once in the
> 2,017-line superseding document, which made it LOOK covered. Citation count is not coverage. The
> cost, measured: two FATAL errors ... a reinvented fifth claim source ... and an entire invented
> `investigate` verb standing where six shipped acts, an obstacle owner, a derived query and a
> counter-investigation layer already were."*

Verdict: **the single largest re-invention in the corpus, fully diagnosed by ideal-v2 itself** (§5 has
the complete register). ideal-v2 replaced the invented `investigate` verb with the six shipped acts
(reproduced verbatim at `01_ARCHITECTURE.md §5.11`) after the correction — this is the one case where
the fix in the current tree is essentially complete for the specific defect named, though §7-§9 of the
source document (correspondence filtering / channel-holder disposition, the setting's-own-epistemics
machinery for P-08/P-09/P-13, and the full worked trace in §12) are still not discussed anywhere in
ideal-v2 beyond the `filter_share` term picked up once in `03_COMPENDIUM.md:630`.

---

## 5. THE RE-INVENTION REGISTER

| ideal-v2 claim + cite | already designed at | how completely | verdict | closes/changes |
|---|---|---|---|---|
| Off-board polities are event sources, not simulated persons (`01_ARCHITECTURE.md §7 F5`) | `11_world_events.md` §1, §7 (`we.altonian_pressure`) | full mechanism, rate-bounded, registry-ready | re-invention, self-corrected | F5 |
| Ambition needs a carrier object (`§7 F6`) | `09_ambitions_and_arcs.md` §2-3 (Ambition Tag, derived progress) | full mechanism | re-invention, self-corrected | F6 |
| How anything reaches a decider / the Slate contract | `10_the_slate_and_salience.md` (+part2) | full mechanism, unread and *left* unread | acknowledged gap, not re-invented nor absorbed | G-14 (the `01_ARCHITECTURE.md` gap register row) |
| D-2, the act-economy contradiction | `2026-08-30-fixes/02_the_act_economy.md` | exact match, independently reached | re-derivation, self-disclosed | D-2 |
| Field investigation as a single invented `investigate` verb | `03_knowledge_telling_investigation.md` §6 (six acts, obstacle owner, derived query) | full mechanism, corrected in current tree at §5.11 | re-invention, corrected | §5.11 |
| `relevance(c, q)` "never defined anywhere in the corpus" (an original FATAL finding) | `03:342-344` | defined in full | fabricated-absence, corrected | §12.8 (correction log) |
| "The predicate vocabulary's membership is enumerated nowhere" (original FATAL finding) | `03:66-79` (fourteen forms, closed) | defined in full | fabricated-absence, corrected | §12.8 |
| A "fifth claim source" the suite believed it needed to invent | `03 §5`'s corroboration/root system already supplies it | full mechanism | reinvented, then struck | §12.8 |
| `Profile`'s field list "undefined" | `07_alignment.md:217-231` (`presence`, `density`, `footprint` formulas) | full arithmetic, only the record's field list genuinely open | narrowed from FATAL to a real-but-smaller gap | `03_COMPENDIUM.md` G-03 |
| `season_factor(territory)`'s distribution — "not present in the documents this suite read" | possibly answered in `11_world_events.md`'s rate bounds (flagged, unverified) | unclear — ideal-v2 itself only suspects, does not confirm | **genuinely open**, correctly flagged as open rather than invented | `01_ARCHITECTURE.md` gap-register row 6 |
| D-1 "the floor" (ordinary-capability character is inaudible) | `2026-08-30-fixes/01_the_floor.md` | full fix (three edits to existing formulas/gates) | uncited, unabsorbed | not referenced anywhere in ideal-v2 |
| D-3, two missing need formulas (`need(commitment)`, `need(exposure)`) | `2026-08-30-fixes/03_the_missing_needs.md` | full fix | uncited, unabsorbed — ideal-v2 never states these formulas at all | not referenced anywhere in ideal-v2 |
| D-4/D-5, Relational empty at Settlement/Territory; no councillor venue | `2026-08-30-fixes/04_relational_at_settlement.md` | full fix | uncited, unabsorbed — zero hits for "relational" + "settlement" together in ideal-v2 | not referenced |
| D-6, the Church conferral cycle (person-rooted vs office-rooted, `sovereign_fraction` undefined) | `2026-08-30-play-space-coverage/09_GAP_REPORT.md` D-6 (names the off-map Holy See as canon's own resolution) | partial — names the resolution direction, does not build it | **genuinely converging, independently arrived at** (ideal-v2's own F4.5/§16 D-7 wrestles with the identical question under a different local D-number) | ideal-v2's §4.5 fork, `10_SUPERSEDING.md` D-7 |
| D-7, the B-11 petition-cost mispricing (Dicastery unpetitionable) | `09_GAP_REPORT.md` D-7 | full diagnosis | uncited | not referenced |
| D-9, vacancy-by-absence empty at every rung | `09_GAP_REPORT.md` D-9 | full diagnosis | uncited | not referenced |
| D-10, material economy empty for the holdingless | `09_GAP_REPORT.md` D-10 | full diagnosis | uncited | not referenced |
| The whole "19 of 55 characters have a BLOCKED CORE" finding | `2026-08-30-fixes/05_the_blocked_cores.md` (disposition on all 19) | full disposition | uncited | not referenced anywhere in ideal-v2 |
| A parallel, same-day synthesis of #342 + play-space-coverage + fixes into an executable design | `2026-08-31-integration/04, 05, 11` (NPC matrix + arcs integration, `11_INTEGRATED.md`) | a **second complete synthesis effort**, produced the same day as ideal/ideal-v2, reading much of the same evidence base | **not a claim-level re-invention but a whole-effort duplication** — two independent same-day synthesis passes over overlapping sources that do not cite each other | genuinely open — needs reconciliation, not a claim fix |
| The tenth attribute is unnamed / IN FLUX (per `CLAUDE.md §5` and the registry's own banner, still current as of this session) | `2026-08-18-breaking-the-recursion.md §4.5` (`Recall`, 19 shipped references in the Godot codebase) | fully answered, months before ideal-v2 was written | **not addressed at all** — zero mentions of "Recall" anywhere in ideal-v2 | closes an open item CLAUDE.md itself still flags |
| `governance_ripple_substrate_v1.md` / `governance_play_redesign_v1.md` uncited (a `systems/` finding, flagged by ideal-v2's own §12.8 point 8, not by this lane's proposals-only scope) | `systems/_architecture/governance_ripple_substrate_v1.md` (559 lines), `systems/settlements/governance_play_redesign_v1.md` (337 lines) | not verified by this lane (out of `proposals/` scope) | **ideal-v2's own finding, corroborated**: the next gap is likelier to come from `systems/` than `proposals/` | flagged, not closed |

**Reading the register as a whole.** Every genuine re-invention ideal-v2 committed was against
`valoria-from-scratch` (#342) — the suite it explicitly names as its primary, if incompletely read,
source. Every re-invention ideal-v2 has **not yet found** is against the *second tier* of the corpus:
the `2026-08-30-fixes/` and `2026-08-30-play-space-coverage/` directories that are themselves built
*on top of* #342, one level further out, and the sibling `2026-08-31-integration/` effort running in
parallel. The correction pattern in ideal-v2's own text (§12.8) is a self-aware, working immune
response — but it stopped one layer too early.

---

## 6. `canonical_nomenclature_v1.md` — the naming scheme, and the design's collision register

**The scheme, reproduced completely.**

- **Grammar:** `<namespace>.<leaf>` or `<namespace>.<group>.<leaf>` (e.g. `settlement.piety_track`,
  `character.mind.will`).
- **Five rules:** (1) namespaces spelled out, never abbreviated (`set.`->`settlement.` — `set.` is a
  Python builtin and unusable in a grep); (2) leaves spelled out, never abbreviated
  (`clock.ip`->`world.invasion_pressure`); (3) no leaf may be a bare ambiguous English word — tested
  against `build_glossary.py`'s existing ambiguity floor, but the rule binds on **the dotted string
  being the citation form**, not on banning the word itself; (4) the dotted ID **is** the code access
  path, not a decorated comment — a dataclass field equals the leaf, the local/parameter name equals
  the namespace; where state is dict-keyed the *string key* becomes the full dotted ID; (5) one
  concept, one ID (closes a three-way alias: *Conviction Track*/*Piety Track*/`conviction_track`, one
  stat, three names).
- **Two-axis recommendation:** **Axis C** (owner/scale — `npc.`, `faction.`, `settlement.`,
  `character.`, `world.`, `unit.`, `thread.`) governs entities and owned state; **Axis B** (event
  domain — the 56 Key types, already dotted and already working, median 24 hits/type with zero
  complaints) is kept unchanged for Keys; **Axis A** (the current bare-abbreviation scheme —
  `set./fac./agg./conv./ppt./mech.`) is retired.
- **What it explicitly refuses to decide** (Jordan's calls): `piety_track`'s owner
  (`settlement.`/`territory.`/`character.` — three docs already disagree); whether Key types get a
  `key.` prefix (recommends: leave them); full contract rename vs citation-form only (recommends:
  citation-form only — 27 module names, ~10k references, enormous join surface); `world.`'s reuse
  (freeing it for owned state orphans 62 proper-noun entries that need re-prefixing in the same pass).
- **Phasing:** Phase 0 (Jordan rulings) -> Phase 1 (registry + guarded rename executor + report-only
  checker, zero renames) -> Phase 2 (migrate the two source registries, alias-backed) -> Phase 3
  (adopt in code, one subsystem per PR, worst-noise first, guarded against read/write asymmetry per
  `CLAUDE.md §0.1` point 1) -> Phase 4 (flip to blocking at zero backlog).
- **A named, verified blocker:** `tools/valoria_rename.py`, the repo's only "rewrite the old name
  everywhere" executor, scopes to `('designs', 'params', 'references', 'canon')` — two of those four
  roots no longer exist and it silently no-ops on missing directories, so **270 files of live design
  corpus, 261 `.py` files and 41 `.json` files are invisible to it today.** Phase 1 makes fixing and
  guarding this a blocking prerequisite.

**Judgment: does it solve ideal-v2's `hold`/`subject`/`kind`/`Derived`/`Container` collisions?**
**Partially, and the two halves are genuinely different problems.**

The nomenclature plan solves — completely, and it is already validated with real numbers — the
*English-word-in-prose* collision: a canonical concept like *Order* or *Authority* being unfindable by
grep because it also appears as an ordinary word 1,000+ times across hundreds of files (the median
contract name has 131 bare hits and zero qualified ones). That is Axis C's whole job, and it is proven
against the *quantity* and *entity* layer (attributes, faction stats, settlement fields, world clocks,
named characters).

It does **not** address ideal-v2's `Container`/`Rung`/`Node` problem, which is a **different kind of
collision**: a `class_name` in Godot colliding with an **engine built-in** (`Node`, `Container` is
itself `VBoxContainer`'s base) — a code-identifier collision at the class-declaration layer, not a
grep-noise collision in prose. The nomenclature plan's grammar governs *quantities and entities* keyed
by owner/scale (`settlement.legitimacy`, `npc.almud_almqvist`); it says nothing about *carrier/record
type names* (`Rung`, `Office`, `Site`, `Person`) at all, and those are exactly the names ideal-v2 is
fighting over. Nor does it address structural field-name reuse across record schemas — `kind` appears
on a Tag, a Rung, and a candidate row; `subject` appears on a Claim and (differently) on a proposition.
Under ordinary typed-object access (`tag.kind` vs `rung.kind`) this is not actually ambiguous — each
record type is its own namespace by construction — so the nomenclature plan's Rule 3 (test every
*leaf* against the ambiguity floor) would, if applied literally to structural field names rather than
top-level quantity/entity keys, be solving a problem that dotted field access already solves for free.

**Net:** the plan is a real, load-bearing answer to one entire class of the design's naming trouble
(the 1,630-hit "Order" problem) and is silent on the other (Godot class-name collision, and structural
field reuse across record schemas) — because it was scoped, correctly, to quantities and entities, not
to the carrier-type vocabulary ideal-v2 is actually contesting. **Neither collision register subsumes
the other; a session should apply both, not pick one.**

---

## 7. THE OLDER PROPOSAL LINE — architecture still live and uncontradicted

- **`2026-08-18-fieldwork-architecture-and-nonadversarial-play.md`** — the FI architecture
  `03_knowledge_telling_investigation.md` itself composes on and reads. It carries **ratified Jordan
  rulings** (§13, 2026-08-18) including the load-bearing *"scripting hooks and sequences is ALLOWED;
  scripting arcs is not"* ruling that `09_ambitions_and_arcs.md §4` builds its whole hook-grammar
  defense on, and the P-08/GAP-A/GAP-B analysis (`Key.visibility` written-never-read;
  `Key.causes` essentially unpopulated) that the knowledge/telling document's own provenance rules were
  built to close. Nothing in the current suite contradicts it; nothing in the current suite cites it
  either.
- **`2026-08-18-epistemic-propositions-and-provenance.md`** — five **RULED** Jordan calls (P1-P5) that
  `09_ambitions_and_arcs.md`'s O-A5 override explicitly builds on (*"a Condition (a proposition or
  conjunction) the engine evaluates"*). ideal-v2 inherits this only at second hand, through `09`, and
  never reads the ruling document directly — a live but currently-secondhand dependency.
- **`grounded_event_card_deck_v1.md`** (2026-07-11) — 58 grounded event cards bound to
  `systems/_architecture/governance_ripple_substrate_v1.md`. This is the direct ancestor of
  `11_world_events.md`'s exogenous-event concept (event cards vs. actorless registry rows), and it is
  the reason `governance_ripple_substrate_v1.md` — flagged by ideal-v2's own §12.8 point 8 as an
  uncited `systems/` load-bearing spec — matters: it is not an orphan reference, it already has a
  content deck built against it.
- **`valoria_fork_plan_of_record_v1.md`** (2026-08-03) — Class-A repo-fork/architecture-boundary plan.
  Largely process/infrastructure rather than game mechanism (the centralized-value layer, the
  dependency-direction inversion, the two mass-battle trees); its concrete game-relevant content
  (mass-battle tree status) is superseded by later `systems/`/`engine/` state described in the current
  `CLAUDE.md`, so it is uncontradicted rather than live.
- **`canonical_nomenclature_v1.md`** — see §6; live, unratified, unexecuted (Phase 0 rulings never
  landed), and still the correct next step for the "Order"/"Authority"/"Standing" grep-noise problem
  whenever a session picks it up.

---

## 8. ARCHITECTURE LOG

| ID | kind | name/term | path:line | what it asserts | ideal-v2 aware? |
|---|---|---|---|---|---|
| A-R5-001 | registry row schema | `world_events:` row (14 fields) | `11_world_events.md:114-152` | actorless event schema, one-schema with `05` | yes (post-correction) |
| A-R5-002 | mechanism | `we.eligible`/`we.fire` collapsed onto `05`'s dispatcher | `11_world_events.md §6` | zero new modules for exogenous events | no |
| A-R5-003 | Gauge (proposed) | `institutional_pressure` | `11_world_events.md:45,570` | a top-tier-place gauge, unconfirmed by `07`/`12`, a **known-failing** reachability check today | no |
| A-R5-004 | Tag kind | `Ambition` (the seventh, closes at seven) | `09_ambitions_and_arcs.md §2.1` | intent/target/terms as a Tag; the two-part-test argument for a new tag kind | yes (post-correction) |
| A-R5-005 | formula | `progress(P, season) = Sum w_i * [term_i holds]` | `09_ambitions_and_arcs.md:196` | derived-at-read progress, never stored | yes (post-correction, quoted) |
| A-R5-006 | term-kind grammar | seven advance-term kinds, incl. `tag age` | `09_ambitions_and_arcs.md §3.1` | closed predicate grammar for project advance | no |
| A-R5-007 | mechanism | place-bound auto-declaring project kind (the `rising`) | `09_ambitions_and_arcs.md §6.4` | the suite's only mass actor — no post, no budget, gate-only | no |
| A-R5-008 | candidate contract | `candidate:` row (14 fields, six normative rules C-1..C-6) | `10_the_slate_and_salience.md §2.1` | the missing definition the ratified Light Function presupposes | no (acknowledged unread) |
| A-R5-009 | algorithm+proof | truncation `M u E u F u P`, bounded & monotone | `10_the_slate_and_salience.md §5.1-5.3` | Slate truncation is provably `<= B` and score-monotone | no |
| A-R5-010 | boolean field | `informational: true` | `10_the_slate_and_salience.md §2.1a` | crossing-fact candidates exempt from resolver/response requirements | no |
| A-R5-011 | derivation | inertia from Key-log, not carried | `10_the_slate_and_salience_part2.md §7` | J-N-compliant light-inertia with a fixed cold-start bug | no |
| A-R5-012 | property set | P-A/P-B/P-C headless-resolution invariance | `10_the_slate_and_salience_part2.md §6.3` | fidelity neutrality, baseline parity, order neutrality, each with a falsifier | no |
| A-R5-013 | ruling | Reading C: act = person, throughput = establishment | `02_the_act_economy.md §3` | resolves D-2 via a measured discriminator (56 probes) | yes (quoted, D-2) |
| A-R5-014 | formula | `acts = 1 + \|establishment members whose choose served the office\|` | `02_the_act_economy.md:171-174` | the derived act count | yes (matches ideal-v2's own D-2 wording) |
| A-R5-015 | claim schema | `Claim = (subject, predicate, value, when, source, confidence, visibility)` | `03_knowledge_telling_investigation.md:21` | the one claim object for the whole knowledge layer | yes |
| A-R5-016 | closed vocabulary | fourteen predicate forms | `03_knowledge_telling_investigation.md:64-80` | closed forms, open referents | yes (post-correction) |
| A-R5-017 | mechanism | `witness` two-stage (registration, construal) | `03_knowledge_telling_investigation.md §2` | perspective divergence without noise on a single truth | yes, partially (via §5.11's six acts) |
| A-R5-018 | mechanism | unconditional `SAID` deposit | `03_knowledge_telling_investigation.md:262-265` | the traceable source row that makes lying catchable | not discussed directly |
| A-R5-019 | mechanism | corroboration root system, x2.0 cap | `03_knowledge_telling_investigation.md §5` | provably un-launderable corroboration | not discussed directly |
| A-R5-020 | mechanism | correspondence filtering, `filter_share` | `03_knowledge_telling_investigation.md §8` | a channel-holder with no rank structurally outranking ministers | yes — `filter_share` picked up once at `03_COMPENDIUM.md:630` |
| A-R5-021 | mechanism | P-08 barrier lives in the hearer's ledger referent space | `03_knowledge_telling_investigation.md §9` | study cannot cross the sensitivity barrier by any channel | not discussed |
| A-R5-022 | fix (D-1) | three edits to existing formulas/gates | `2026-08-30-fixes/01_the_floor.md` | closes the "ordinary-capability character is inaudible" defect | no |
| A-R5-023 | fix (D-3) | `need(commitment)`, `need(exposure)` formulas | `2026-08-30-fixes/03_the_missing_needs.md` | the two uncomputed need terms, filled | no |
| A-R5-024 | fix (D-4/D-5) | Relational at Settlement/Territory; councillor venue | `2026-08-30-fixes/04_relational_at_settlement.md` | fills two empty rungs' membership machinery | no |
| A-R5-025 | disposition | 19 BLOCKED-CORE characters, ruled individually | `2026-08-30-fixes/05_the_blocked_cores.md` | resolves the report's headline 35% finding | no |
| A-R5-026 | primitive set | Entity/Tag/Post/Gauge, four write leaves | `2026-08-29-greenfield-systems-suite-v2/01_substrate_primitives.md` | the base every cited 09/10/11 document composes on | no (foundation of cited docs, itself uncited) |
| A-R5-027 | attribute finding | the tenth attribute is `Recall` | `2026-08-18-breaking-the-recursion.md:335-357` | closes a CLAUDE.md-flagged-open item, 19 shipped Godot references | no |
| A-R5-028 | parallel synthesis | NPC matrix + arcs integration | `2026-08-31-integration/04, 05, 11` | a second complete same-day synthesis of #342 + play-space-coverage + fixes | no — not cross-cited by ideal-v2 |
| A-R5-029 | gap register | D-1..D-10 | `2026-08-30-play-space-coverage/09_GAP_REPORT.md` | the empirically-measured defect ranking behind every `2026-08-30-fixes/*` document | partial (D-2 only) |

---

## 9. VOCABULARY DELTA

Named terms in the uncited corpus with no equivalent in ideal-v2's own vocabulary register
(`03_COMPENDIUM.md`'s key/term table), based on the terms actually deployed above:

- `hazard_pool`, `resilience.{target_score,modifiers,M_max}`, `origin: exogenous`,
  `institutional_pressure`, `route_cut:<place>` — the whole `11_world_events.md` schema vocabulary.
- `tag age` (a term kind), `PROJECT_CAP`, `formation_cause`, `rising` (the worked place-bound project
  kind name) — from `09_ambitions_and_arcs.md`.
- `cast_score`, `depth_score`, `informational`, `INFO_CAP`, `witness.channel` (five named channels:
  `post_remit, co_located, witness_key, document_key, chronicle`), `never_lit(c)`, `engaged(c)`,
  `fidelity: played|witnessed|auto` — from `10_the_slate_and_salience.md` (+part2).
- `filter_share` — partially adopted (one hit, `03_COMPENDIUM.md:630`), but the surrounding channel
  vocabulary (`disposition: approve|suppress|surface`) is not.
- `CONTRADICTED`, `HOLDS_STANCE`, `roots(...)`, `rootprint`, sigma (synthetic root hash),
  `corroboration_multiplier`, `retention(f)`, `plant(actor, ...)`, `exposure`/`pressure` (the
  counter-investigation pair) — from `03_knowledge_telling_investigation.md`.
- `establishment(o)` as a **derived-count object** rather than a prose phrase — from
  `02_the_act_economy.md`; ideal-v2's own quoted text uses "establishment" but the derivation formula
  itself (§3.5) is not reproduced.
- `Recall` — the tenth character attribute, entirely absent from ideal-v2's vocabulary.

---

## 10. Claims to escalate

1. **D-6 / the conferral cycle.** `09_GAP_REPORT.md` D-6 names canon's own resolution direction (an
   off-map Holy See) for the person-rooted/office-rooted conferral cycle that ideal-v2's own §4.5/§16
   independently wrestles with under a locally-numbered D-7. Both are plausible, neither is built, and
   they were reached independently — a genuine convergence worth a ruling that reads both.
2. **Two same-day parallel syntheses.** `2026-08-31-integration/{04,05,11}` and
   `2026-08-31-ideal-v2/*` are two independent, complete attempts at the same task (reconcile #342
   against play-space-coverage's findings and the fixes directory) produced the same day, and neither
   cites the other. This is not a single-claim contradiction to adjudicate; it is a process fact that
   needs a human decision about which synthesis is authoritative, or whether they should be merged.
3. **`piety_track`'s owner** (`settlement.`/`territory.`/`character.`) — `canonical_nomenclature_v1.md
   §3.3` names this as a design ruling three docs already disagree on, unrelated to and unresolved by
   the naming plan itself.
4. **Whether `canonical_nomenclature_v1.md`'s Phase 0 rulings should land now** — the plan is complete,
   unratified, and directly answers the "Order"/"Authority" grep-noise problem the design keeps
   re-encountering (`Container`/`Rung` is a different, unaddressed problem — see §6).

---

*Method note for the next reader: every citation above that names a line number was read directly off
the file at that line during this pass; every "0 hits" / "uncited" claim was verified by grep against
the six-document citing set, not inferred from a title. Files marked L in §3 were surveyed by header
and opening `## Status:`/`## Reads:` line only, per the task's instruction to work down the list by
heads + headings + tables rather than full reads once the five mandatory documents and the highest
architecture-priority items were covered in full.*
