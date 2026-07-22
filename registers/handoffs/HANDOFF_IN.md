# Handoff — IN (Infrastructure / Cross-Cutting)

Lane-scoped continuity for the `IN` (infrastructure/cross-cutting) lane, per the
`ED-<LANE>-NNNN` namespace (`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention.
Root `HANDOFF.md` is the index; see it for the global "Next actions" pointer and cross-lane
items. `IN` is also the catch-all for genuinely cross-cutting repo-governance work (ID systems,
CI gates, canon-currency reconciliation) that doesn't belong to any one subsystem lane.

## Pending

- **✅ IN lane-ledger archive pass DONE (2026-07-18).** `registers/editorial_ledger_in.jsonl` was at 99.7% of
  its 50k cap (after `ED-IN-0074`/`ED-IN-0075`). Established the **per-lane archive convention**:
  `registers/editorial_ledger_in_archive.jsonl` (the first lane archive; mirrors the flat
  `editorial_ledger_archive.jsonl` overflow pattern). Moved **25 `resolved`/`superseded` entries** there → live
  now **34,641 / 50,000 tokens (~30% headroom)**, archive 15,215 / 150,000. Wiring: `validate_ed_citations.py`'s
  `load_ed_universe` now **globs `editorial_ledger_*_archive.jsonl`** (so archived-ED citations still resolve —
  verified: archived `ED-IN-0031` is cited 7× and stays green); `ci_register_size_check.py` THRESHOLDS gained
  the archive (150k cap). `broken_dependency_checker` needs no change (validates live entries only).
  **Archiving is dedup-safe** — ids appearing more than once in the live file are NEVER archived, so no
  effective status ever changes via last-write-wins. Future lanes: same pattern, glob already covers them.
- **⚠ pre-existing bug surfaced (needs editorial reconciliation, NOT mine to rule): 4 duplicated ED-IN ids in
  the live ledger** — `ED-IN-0012`(×2), `ED-IN-0013`(×2), `ED-IN-0016`(×2), `ED-IN-0029`(×3), several with
  *conflicting* statuses (an `open` copy masked by a later `resolved` copy via last-write-wins). The known
  ED-IN-0012/0013 double-allocation is documented in `id_reservations.yaml`; the 0016/0029 duplicates are
  additional. These should be de-duplicated/reconciled (which status is authoritative?) in an editorial pass.

- **ED-IN-0075 FILED 2026-07-18 — "Truth" consolidation RULED + SoT authored; corpus sweep STAGED.**
  Jordan ruling (option A): the per-character metaphysical-stance axis is renamed **Truth**, consolidating
  the former **Certainty Track** (`params/core.md` PP-551, 0–5) + the retired character **"Piety Track"** /
  religious-standing meter (`derived_stats §14.2`). Keeps Certainty's engine-internal 0–5 spine + all PP-551
  mechanics; **players see qualitative bands only, never the number**. Poles: 5 = *Himmelenger* (Solmund
  orthodoxy) ↔ 0 = *Edeyja* (Thread-truth). OUT OF SCOPE (ruled A, not B/C): the 13-Conviction system
  (`conviction_taxonomy_v30`) and the territory-scale **Piety (PT)** — both DISTINCT and unchanged. SoT
  authored this pass: `engine/params/core.md` §Truth Track, `derived_stats_v30` §14.2 + §5.3.4,
  `clock_registry_v30`, `glossary.md`, `alias_registry.yaml`; ledger ED-IN-0075; `CURRENT.md`.
  **Corpus sweep EXECUTED (2026-07-18, second commit of this PR):** case-sensitive `\bCertainty\b → Truth`
  across the live corpus — **89 files / 515 refs** (NPC stat blocks, world/fieldwork/threadwork docs, arcs,
  machine-read `values_master`/`npc_registry`/`numeric_bounds`, `mechanical_terms_index`, glossary `CERT` entry).
  Case-sensitive so prose "certainty"/"uncertainty" is untouched. Excluded: the SoT files authored in commit 1
  (they intentionally keep "formerly Certainty" history), `deprecated/`, `designs/audit/`, `threadwork_superseded.md`.
  **Residuals (deliberately deferred):** (a) the `sim/personal/conviction.py` internal identifier
  `CERTAINTY_SCALING` / `certainty` param is RETAINED — renaming it would churn frozen `tests/sim` callers; the
  docstring notes it now denotes the Truth value; (b) the glossary "Piety Track (CT)" **debate-position tracker**
  is a distinct social-contest mechanic and keeps its name (out of scope for the Truth axis); (c) four
  **params-bearing / generated** files retain "Certainty" (alias-covered) to avoid the co-file params-co-change
  rule firing on a terminology-only change: `systems/factions/factions_personal_v30.md`,
  `systems/threadwork/threadwork_v30.md` (+ `_infill`), and the generated `registers/patch_register_index.md`.
  A params-coordinated rename (touching `engine/params/*` alongside) can fold these in later.

- **ED-IN-0073 FILED 2026-07-17 — adversarial audit of the character-decision machinery (read-only).**
  `designs/audit/2026-07-17-character-decision-adversarial-audit/` (00_findings + 01_remediation_L1_L2 +
  02_emergence_oracle_spec). Three-axis attack (logic / narrative emergence / qualitative rendering);
  3 Sonnet finders + Opus synthesis + independent arithmetic re-derivation. Genuine holes: **L1** contest
  armature `_row()` is algebraically a single-axis lookup (off-axis `0.15·S` cancels; balanced judge ties
  all styles at 0.725); **L2** two incompatible vector spaces both named `armature_position` — convictions
  never reach a social-contest verdict; **L3/L4** roster vs npc_behavior Conviction contradictions + legacy
  9-Conviction labels in CANONICAL npc_behavior with no matrix rows; **N1–N3** GD-2 mandatory pass / NPC arc
  state machine / GD-3 insurgencies all unbuilt-or-inert; **N6/N7** story-fraction hypothetical + Stage-10
  battery laundered into CANONICAL stamps; **Q1–Q4** qualitative-rendering layer largely unbuilt
  (articulation.py all `NotImplementedError`; flagship Key types never emitted; `Belief.statement` read by
  nothing). Remediation proposed & arithmetically verified: genre-overlap `STYLE_AXIS` (fixes L1, rank-3
  genre plane) + `CONV_TO_RESONANCE` 13×4 derivation (fixes L2); minimal n≥100 `mc_v18` emergence oracle
  (closes L6/N1–N4). N5 Hafenmark lockout already = ED-FA-0005 (not re-filed). **Next action: Jordan rules
  the C-1..C-9 docket** (`00_findings.md §5`); C-1 (L1 matrix) is self-contained and lowest-risk to land
  first, C-2 (L2) gated on C-4 (legacy-label migration). Read-only umbrella; no canon edited.

- **ED-IN-0064 FILED 2026-07-14 — multi-scale governance research + audit pass (analysis-only).**
  Durable comparative-governance research corpus at `research/governance/` (8 civilizations × 3 themes —
  modes / hierarchy-standing-advancement-demotion / conflicts; ~228 `=> Valoria design hook` lines;
  Byzantine deferred; **Mandate of Heaven history-only**, collapse/collision/relief-valve hooks grounded
  on non-MoH precedent — Roman/Byzantine dual-trigger usurpation, Ottoman vizier-scapegoat + Janissary
  revolt, Roman recusatio/penance, Polybian regime-cycle). Fresh post-#137 vector audit
  (`designs/audit/2026-07-14-governance-vector-audit/`). Chain/gap + decision-surface analysis docket
  (`designs/audit/2026-07-14-scale-chain-and-decision-surface-map/`): a 2-axis chain map
  (character→settlement→territory→province→duchy→country; faction-action→domain-action→social-contest→
  field-investigation, each edge state-classified with the **sim-WIRED ≠ canon-WIRED** principle), a
  per-scale decision-surface census (flags council-member / territory-bureaucrat / Parliament-as-body
  below the ~4-5 meaningful-action floor), a churn/event-opportunity map, a MoH-free gap register v2
  (~19 complete-the-chain / ~8 genuine-gap) + a ranked Tier-1–4 `decision_queue_delta_v1.md`.
  Adversarially unified end-to-end (docket-internal `adversarial_review_v1.md` + a **holistic**
  `unification_findings_v1.md` → `unification_synthesis_v1.md`, verdict UNIFIES_WITH_FIXES, fix-list
  applied). **Highest-leverage next action: code PR #136's L/PS §5 sequence** — it advances B1/A2/B4/A4
  from undesigned → SPEC-ONLY but all remain uncoded (`lps_inert_check` 100/100 red); until it lands the
  consent-cascade has no gameplay consequence. Two surfaces are unreachable by the live engine: the Key
  `scale_signature` enum is 3-of-6 (no province/duchy/country) and Field Investigation has zero live
  dispatch path. Analysis-only — hands a ranked MoH-free design surface to Jordan; no canon edited.
  Allocates ED-IN-0064 (`registers/editorial_ledger_in.jsonl`) + syncs the pre-existing **duplicate IN-key**
  `next_free` in `references/id_reservations.yaml` (flagged for a proper single-block repair). **Also
  indexed the previously-un-indexed ED-IN-0051** (2026-07-13 cross-scale-governance-grounding docket)
  into `CURRENT.md` + here.

- **ED-IN-0044 RATIFIED 2026-07-12 — simulation/test harness methodology.**
  `designs/audit/2026-07-12-simulation-test-harness-methodology/` (Status: RATIFIED): a generic
  harness core (canon-parameter resolution bound to `CURRENT.md`, never fabricates) + one thin
  per-module `Adapter` — the modular "test module" — bound to `references/module_contracts.yaml`'s
  existing IN→resolver→OUT shape, a depth-tiered (1 minor/2 medium/3 major) probabilistic
  branch-exploration policy per resolver-call event, and a mandatory triage-flag taxonomy that can
  never be silently swallowed into a PASS verdict. A runnable Gate-0 prototype ships at
  `tools/sim_harness/` (one demo adapter over `valoria_dice.py`) — its own `audit_registry.jsonl`
  append is the registry's first ever LIVE (non-backfilled) entry. Between filing and ratification
  the prototype went through **six rounds of adversarial review + deliberate stress-testing, 34
  real bugs found and fixed** (exception-safety gaps, a registry-id collision, trace-persistence
  completeness, tier-validation crashes, and more — full account in `tools/sim_harness/README.md`).
  Builds on PR #122's audit-ecosystem consolidation (ED-IN-0032–0037), which fixed the
  audit-tooling layer but explicitly left the simulation-execution/live-logging gap open
  (ED-IN-0035). **§11's four open questions were put to Jordan directly via AskUserQuestion, not
  assumed on his behalf** (an earlier attempt to self-answer them and attribute the answers to
  Jordan was correctly blocked and reverted): (1) rollout order — Jordan flagged a real gap
  ("Where is settlement management, faction actions, field investigations, threadwork?"); §8
  extended to add `faction_action.py`/`sim/territory/*`/`systems/threadwork/sim/*` as waves 5–7 (mass battle
  stays wave 4, campaign composition now wave 8); field investigation explicitly excluded, not
  omitted — its `sim/` implementation is still `[PROVISIONAL]` stub-only; (2) Wave 1 CI burn-in:
  full report-only, no deviation from the existing ratchet; (3) `mc_v18` full-campaign runs: never
  gate a PR, a firm constraint; (4) the four §9 quick-win findings: filed separately, not bundled
  — see **ED-IN-0045** below. Full resolution text: `registers/editorial_ledger_in.jsonl`.
- **ED-IN-0045 (open, execution pending) — the four ED-IN-0044 quick wins, filed separately.**
  (1) `tests/hooks/`/`tests/index/`/`tests/registry/` + 2 files under `tests/sim/` contain real
  pytest code no CI job or local hook executes — wire in or explicitly retire. (2)
  `sim/personal/combat.py` is confirmed dead (superseded, DEPRECATED-banner-marked 2026-06-23) but
  remains importable — no guard against accidental reimport. (3) `tools/propagator.py`,
  `find_references.py`, `verify_cuts.py` have the identical orphaned-tool profile as the batch
  already retired 2026-07-09, missed by that sweep's exact heuristics. (4) `contract_adjudicator.py`
  could be wired into CI report-only today, independent of the harness — already correct per its
  own fixture suite, just never pointed at the live `module_contracts.yaml` by an automated job.
  Whether to act on each item individually is not yet decided — this ED tracks the queue.
- **Resolution Plan v1 — Stratum-C armature deployment §6.3 wave 3 (consumer/contract hygiene)
  2026-07-08: ED-IN-0016 CLOSED, ED-IN-0030 filed.** Agonist/antagonist pair (producer + independent
  read-only critic, adversarially re-verified against source files) executed the already-ratified
  ED-IN-0016 ("RATIFIED-AS-ACCEPTED... Ratify all" on PR #81) plus C-INJ-4: (1) `module_contracts.yaml`
  `faction_politics` `doc: null` flipped to `designs/provincial/faction_politics_v30.md` (was stale —
  the CANONICAL PP-660 1,115-line home exists; C-INJ-4's scenario_authoring gap_notes needed no edit,
  already refreshed by ED-IN-0023); (2) `CURRENT.md` gained three rows/extensions (faction_politics_v30
  appended to the Faction/political row; new Scale-transitions row; new Player-agency row; new
  Fieldwork/Investigation row citing ED-FI-0004's Interview-MERGE resolution of the EP-8 contradiction);
  (3) repointed the dead `faction_politics_expanded_v1.md` filename (30 live-corpus citations, ep-14) to
  its promoted successor across 9 live canonical docs (baralta_crown_claim_v30, scale_transitions_v30,
  settlement_layer_v30, player_agency_v30, npc_behavior_v30, throughline_resolutions_v30 + its `_index`
  co-file, throughlines_complete.md) — verified section-by-section against the actual promoted doc's
  headers (not blind find-replace); one citation (player_agency §2, succession) could NOT be verified to
  a matching section and was rewritten as a prose pointer with an inline flag instead of guessed;
  deliberately left ALL `designs/audit/`, `tests/sim/`, `deprecated/archives/`, and `references/propagation_log.md`
  hits untouched (historical snapshots, rewriting would falsify the record); (4) `restructure_ledger.md`'s
  two stale PENDING rows closed (DONE / N/A — no skeleton split was ever authored); (5) **filed
  `ED-IN-0030`** (open, needs_jordan) for a genuinely new defect the sweep surfaced: `scale_transitions_v30`
  §4.3.2 row 8's "creating a debt scene per §1" clause cites a mechanic that does not exist anywhere in
  the promoted `faction_politics_v30.md` — flagged, not authored or struck. Critic caught two minor
  drift issues pre-commit (index co-file line-numbers off by 2 after an inserted note; one wrong
  key_type_registry_v30.md line citation) — both fixed. Gates green (`valoria_local --staged`,
  `validate_ed_citations` 0 violations, `freshness_gate` 133/133, naming clean); `pytest tests/valoria
  sim/tests` full-suite pass pending final confirmation in this same PR. NEXT §6.3 waves: down-seam
  (FA/WR targets[] population), A13-A16 checker implementation (needs a new `doc_emit_ref:` schema field
  + `references/rendering_dispositions.yaml`), rendering wave.
- **Attribute/value coherence audit 2026-07-08: ED-IN-0029 — PARTIALLY RATIFIED (2026-07-08 follow-on
  session, Jordan: "Resolve all conflicts ratify commit merge squash close session" + "adopt every
  stated recommended default" + explicit named exception "Skip OPT-AV-1").** Read-only cross-silo audit
  of every attribute/derived score/pool/track/clock/stat/constant, tied into the Key & Echo Armature.
  88-row quantity census; 82 findings post-critic (18 P1/39 P2/25 P3). Full per-item ratification
  outcome lives in `designs/audit/2026-07-08-attribute-value-coherence-audit/ed_options.md`'s
  "Ratification outcomes" section (single source, not restated here). Headline: **OPT-AV-1 (attribute
  roster) SKIPPED per Jordan's explicit instruction** — left fully open, no roster edits made, still
  feeds workplan v6 T1 queue-13 / ED-IN-0008. OPT-AV-2/3/7/14 + 5 of OPT-AV-18's 6 sub-items ratified
  AND executed this session (hygiene batch, secondary-index disposition, Class-B registry deltas,
  Political Pool/Discipline/Intel-floor naming). OPT-AV-4/5/6/16 ratified spec-only, build deferred to
  the extension's own Wave Q; OPT-AV-8 (wave sequencing) ratified as already stated. OPT-AV-9/10/11/12/
  15/17 + OPT-AV-18's Fort-Level/Garrison-LE-PO sub-items ratified as decisions, **execution deferred**
  to their owning lanes via **ED-FI-0005, ED-FA-0007, ED-SC-0014, ED-SE-0006, ED-PC-0013**. OPT-AV-13
  and OPT-AV-18's Renown-cap/Shadow-Renown sub-item **left explicitly open** — no default stated,
  none invented. `proposed_quantity_armature_extension.md` flipped PROPOSED → RATIFIED (spec-level;
  A17/A18/tier-promotion/exporter-widening are ratified-spec-pending-build). NEXT: Wave Q execution
  (hygiene already done; registry filing done; A17 report-only + keys.py hook + A18 detector + tier
  promotion remain, sequenced per the extension's §4); the five lane EDs above await their owning
  lanes' own execution passes.
- **Wave-Q-step-3 tooling build EXECUTED 2026-07-08 (same-day follow-on to the ratification above;
  Jordan: "enforce compliance with pointers").** Builds the concrete CI enforcement the prior entry
  ratified spec-only: `tools/quantity_registry.py` (single reader merging `descriptor_registry.yaml`
  + `names_index.yaml`) + `tools/ci_quantity_vocabulary_check.py` (A17, report-only, wired into CI
  via the `contract_adjudicator` `continue-on-error` precedent) + an optional warn-tier
  `stat_vocabulary` hook on `sim/substrate/keys.py`'s `KeyLog` (OPT-AV-16, candidate invariant 9;
  default `None` preserves prior behavior exactly — all 25 pre-existing substrate tests unchanged,
  3 new added). **Measured real A17 backlog: 36/71** (re-derived fresh against the now-much-larger
  post-ratification registry; `params/*.md` prose intentionally not scanned — that's A18's job).
  Also filed two small residual registry deltas the ratification pass above didn't cover:
  `set.facility_tier` (settlement_stats, D5) and "Settlement Weight" (not_descriptors.derived_values,
  D5's derived companion). **Two defects remain found-but-unfixed by both this pass and the prior
  ratification** — `ed_options.md` D11 (`pool.knot`/`track.persuasion` cross-link: no linkage exists
  at either cited source, rejected as fabrication-risk) and D15 (`contracts_bucket`↔KIND crosswalk
  field: `not_descriptors` carries no KIND field to cross against). One more small thing noticed in
  passing, flagged not fixed: `descriptor_registry.yaml`'s own Coherence disambiguation note (added
  by the ratification pass above) claims `module_contracts.yaml`'s `threadwork` module "still tags
  its Coherence state entry `bucket: pool`" — that's now stale; the same ratification pass's own
  `module_contracts.yaml` edit already corrected it to `bucket: track`, so the claimed "3-way
  disagreement" no longer holds.
- **Pessimist subtractive-action audit RATIFIED 2026-07-08 (ED-IN-0027; Jordan: "Please ratify all").**
  The corpus-wide read-only audit (`designs/audit/2026-07-08-pessimist-action-audit/`) is ratified.
  Two ratification acts landed: (1) **canon** — `references/throughlines_meta.md` §8.2-A + infill §7-A
  now carry the **subtractive disposition** (KEEP/REFINE/DISTILL/MERGE/PRUNE/CUT, judged *as-if-built*;
  the first removal verdict the vetting framework has ever had); (2) **docket** — the ratified verdicts
  are filed as per-lane work-item EDs **ED-PC-0007 / ED-SC-0012 / ED-FA-0006 / ED-SE-0005 / ED-WR-0007 /
  ED-FI-0004** with the DECISION ratified and EXECUTION scoped to each lane's own follow-up (not done
  in this IN-lane PR — lane-scoping, CLAUDE.md §4). NEXT (per-lane, when each lane next runs): execute
  its ED's verdicts against its surfaces, each naming the downstream resolution-plan Stratum/OPT it
  retires. Headline: 0 top-level CUTs, 2 PRUNEs (SE Trade, SE Grant/Revoke) — the corpus is
  over-articulated, not junk-laden; most execution is MERGE/DISTILL consolidation. The 2 critic-overturned
  candidates (MB Concentration, SC deliberative-game) take no action.
- **Resolution Plan v1 — Stratum-C (armature deployment) FIRST SLICE 2026-07-08: ED-IN-0028, echo-transport
  plumbing ("proceed large build").** Executed the IN-lane core of Key & Echo Armature §6.2. New
  `sim/cross_scale/echo_transport.py` un-orphans `domain_echo.py` (was a ZERO-caller C-REACH island) and
  routes a resolved scene → `domain_echo` (degree-keyed) → one `scene.*_resolved` Key via the substrate
  `TickScheduler` with an OF-7 **deferred** faction apply at the ACTION→ACCOUNTING boundary. Wired into
  `scene_dispatch._resolve_slot` (closes `zoom_out({})`) + `mc_v18` (world-scoped KeyLog; `key_log_hash`/
  `keys_emitted` telemetry), behind an `ECHO_TRANSPORT` flag (default OFF = byte-exact, MB FIELD_MOVEMENT
  precedent). Flag-OFF **and** flag-ON win-share both byte-identical to the F7 seed-42 golden; OF-7/degree/
  replay proven in `sim/tests/test_echo_transport.py` (9 cases); 396-pass sim regression green. **DEFERRED
  (owning lanes, nothing dropped):** SC context-derivation bridge (ED-SC-0006/0007) makes scenes resolve →
  live loop is INERT today (KeyLog born empty-deterministic; F7 named-zero-assertions stay 0 by design and
  flip when the bridge lands); FA comeback (parliamentary_vote-in-loop) is ED-FA-0005; §5.5 RNG fork not
  engaged (domain_echo deterministic). NEXT armature waves = §6.3 PR-3+ (keying / down-seam / rendering).
- **Resolution Plan v1 — Stratum-B THIRD SLICE 2026-07-08: ED-PC-0005 dead-code investigation →
  truth repair + Jordan flag.** Confirmed `WoundTracker.pool_penalty()` + `WOUND_POOL_PENALTY`
  (`combat_engine_v1/combatant.py`) have ZERO live callers and ED-1041's wound-Ob channel is the live
  mechanic. NOT deleted (it's the only −1D-per-wound impl; whether that rule survives is the crux ED
  tracks); instead the false "no Ob penalty, ever (canon)" docstrings were corrected + ED-PC-0005
  flipped needs_jordan. **The clean mechanical Stratum-B tail is now exhausted** — remaining items
  (ED-PC-0005 reconciliation, ED-SC-0011 contest dispatch, C-TW-3/4/6/8, armature echo-wiring) need a
  ruling or a large build; surfaced for Jordan, not forced.
- **Resolution Plan v1 — Stratum-B SECOND SLICE 2026-07-08: knots.py ED-912 rebuild (C-TW-12
  CLOSED).** `sim/personal/knots.py` rebuilt onto the bidirectional −5..+5 gauge (TIER_RANGE/
  TIER_START; rupture +5; −5 Tempered Close-only absorb-once; break/betrayal Disposition −3;
  positive-strain Close-break Scar) matching the doc side; pinned test
  `sim/tests/test_knots_ed912.py` (7 cases; knots had zero coverage). Closes ED-FI-0003's sim
  residual; ED-WR-0005 still carries C-TW-3 + C-TW-4/6/8/10/11. F7/seed-0 goldens unmoved (island).
- **Resolution Plan v1 — Stratum-B oracle-to-canon FIRST SLICE 2026-07-08.** The ruled, low-risk
  sim truth-alignment deferred from Stratum A (resolution_plan_v1.md §9). **ED-871 CLOSED
  end-to-end** — `systems/threadwork/sim/operations.py` `attempt_mending` cost −1 → 0 + Mending exempted from
  the blanket Partial/Failure penalty (all degrees net 0), with a pinned test
  `sim/tests/test_thread_mending_ed871.py` (threadwork had zero coverage). **CI-75 dead constant**
  `CI_PHASE_TRANSITION=75` removed from `sim/peninsular/ci_track.py` (CI75-9, under the
  already-resolved ED-IN-0025). F7 + seed-0 goldens unmoved (island/dead-code). ED-WR-0005 stays
  open (progress-noted): C-TW-3 (Leap), C-TW-4/6/8/10/11, knots.py C-TW-12 remain.
- **Resolution Plan v1 — PR-2 F7 smoke oracle LANDED 2026-07-08 (ED-IN-0021 → resolved).**
  `sim/tests/test_f7_smoke_oracle.py`: the "born guarded" campaign regression the U-4 lesson
  demanded (no balance claim without an oracle + n≥100). Pins the n=8/seed-42 golden (Varfell
  87.5% — the historical small-n artifact, labelled NOT balance), named zero-assertions
  (scenes_resolved / insurgencies_formed / npcs_generated = 0 — the islands; designed to TRIP when
  the transport waves land), the Hafenmark elimination-lockout (ED-FA-0005), the VICTORY_THRESHOLD
  dead-param regression (C-EMERGE-8), and a wall-time ceiling. Added minimal additive telemetry
  (`game_state.World.scenes_resolved` + 3 `CampaignResult` fields; no behaviour change, seed-0
  golden unmoved). Runs in CI via "Sim Reference Regression" (pytest sim/tests). Landed **ahead of**
  the armature echo wiring (baseline-first); the wiring is PR-2's remainder. See resolution_plan_v1.md §8.
- **Resolution Plan v1 — Stratum-A truth-reconciliation FIRST PASS EXECUTED 2026-07-07 (this branch,
  `claude/fable5-audit-resolution-plan-r6kzsa`).** Executes the doc/registry/ledger core of Stratum A;
  `designs/audit/2026-07-07-unaddressed-areas-audit/resolution_plan_v1.md` §7 has the full
  finding→fix execution log. EDs flipped `resolved`: ED-FI-0003 (OPT-6 knots ED-912 propagation),
  ED-IN-0022 (OPT-7 registry hygiene), ED-IN-0023 (OPT-8 consumer closure), ED-IN-0024 (OPT-14
  addenda), ED-IN-0025 (OPT-17 C-VERIFY notes), ED-SE-0004 (OPT-16 anti-orphaning), ED-PC-0004
  (OPT-15 ED-1042 flips + the **ED-PC-0005** residual re-file). Kept `open` with a progress note:
  ED-FA-0004 (OPT-1 — `[PRE-LPS-1/PORT-BLOCKING]` banners placed, LPS-1 sim impl = Stratum B),
  ED-WR-0005 (OPT-5 — ED-871 doc side done, sim + C-TW-3.. = Stratum B). Also executed the U-6
  CI-75→CI-100 supersession + fork-2 ARC-T04 strike (doc side), and DISAMBIGUATED the half-done
  ED-IN-0012/0013→0019/0020 renumber (U-11 — the ratification appended the new rows but never re-id'd
  the old edge-playability rows; now `status: superseded` + `renumbered_to`, physical row-dedup left
  to Jordan). **Deferred (loud):** all behavior-changing sim edits (`operations.py`, `ci_track.py`,
  `knots.py`, dead `pool_penalty`) = Stratum B; genuine needs-Jordan calls (anchoring cadence cap,
  CI75-1 seizure trigger, CI75-11 GD-1 checklist, knots §6.2 Coherence-loss) flagged in place, not
  decided. New id: **ED-PC-0005** (id_reservations PC next_free 5→6).
- **Unaddressed-areas comprehensive audit — DELIVERED 2026-07-07 (ED-IN-0017, this PR;
  deliverable 1 of 2).** 14 evidence clusters (incl. Jordan-directed pessimist NERS + pessimist
  resolver reviews) + 4 gap-closure agents + 5 independent refuters; every cluster's Honest-gaps
  section dispositioned per Jordan's directive. Deliverables at
  `designs/audit/2026-07-07-unaddressed-areas-audit/` — verdict-first report, finding_status,
  `ed_options.md` (17 candidates, **deliberately UNFILED — Jordan picks**; OPT-1/2/4/10/14 and
  the armature §5 docket are needs_jordan), and **`resolution_plan_v1.md`** — the comprehensive
  bottom-up + top-down resolution program (armature-FIRST sequencing override per Jordan;
  contract deployment + enforcement ladder; v40 re-authoring license operationalized; ecosystem
  tooling bindings; full finding→fix→lane→stratum→gate table). Headlines: the faction oracle implements the
  pre-LPS-1 superseded model; threadwork is a total island; live contests resolve through the
  deprecated raw-dice stub; the ~87% win-share is a small-n artifact riding an elimination
  lockout (n=100: 56/36/7/1); the Turmoil victory gate is permanently vacuous; ED-871/fork-2/
  ED-912/fork-11 rulings only partially executed; conviction_track_v30 still runs the superseded
  CI-75 model (unpropagated supersession, refuter-upgraded).
- **Key & Echo Armature v1 — DELIVERED 2026-07-07 (ED-IN-0018, this PR; deliverable 2 of 2,
  needs_jordan = its §5 fork docket).** `designs/architecture/key_echo_armature_v1.md` (seam
  contracts + Echo Matrix all-directions/all-scales + §3 registry deltas + A13-A16 conformance
  specs + the consolidated §5 docket — **merge does NOT ratify §5**) + the first executable Key
  substrate (`sim/substrate/keys.py`, 24 tests) + `tests/contracts` wired into CI. Staging:
  PR-2 = flag-gated echo wiring + the F7 smoke oracle; PR-3+ = per-lane shaping waves (armature
  §6.3). The §5 docket consolidates: OF-D6/OF-3/OF-7/OF-B1/RNG-COLLISION/ORD-3/ORD-4/OF-CAP,
  ED-SC-0002, ED-SE-0002, the ED-IN-0012/0013 double-allocation renumber (ledger lines 597-600),
  CI 75-vs-80, ER-2 band-discipline scope, contest live-dispatch.

- **Unaddressed-areas audit + Key & Echo Armature — RATIFIED 2026-07-07 (Jordan: "Perform
  consolidated ruling pass? I want to ratify all and get to work on this" — ED-IN-0026, same
  branch/PR, before merge).** Rules the armature's full §5 fork docket (16 rows — see
  `key_echo_armature_v1.md` §5 Ruling Log) and files all 17 `ed_options.md` candidates as EDs
  (`ED-FA-0004/0005`, `ED-IN-0019/0020/0021/0022/0023/0024/0025`, `ED-WR-0004/0005/0006`,
  `ED-FI-0003`, `ED-SE-0003/0004`, `ED-PC-0003/0004`, `ED-SC-0011`, `ED-MB-0004`; see
  `ed_options.md`'s Disposition table for the design-call ruling baked into each). Headlines:
  OF-7/OF-B1 ADOPTED — `sim/substrate/keys.py`'s `TickScheduler` now defaults both flags ON
  (propagation_spec_v1.md and key_substrate_v30.md amended to record the ratification; 25/25
  substrate tests + full 120-pass `tests/valoria` suite re-verified, no regressions); the
  ED-IN-0012/0013 double-allocation (§5.10) EXECUTED via the `ED-IN-0019`/`ED-IN-0020` renumber;
  the ER-2/Overwhelming band-discipline fork (§5.12, the one genuine no-default fork besides the
  renumber) ruled toward the symmetric-unification direction, execution deferred to `ED-PC-0003`;
  the A15 process extension (§5.16) landed in `key_type_registry_v30.md` §10, which also picked
  up a header CANONICAL/PROVISIONAL split correction found while editing the same file.
  `ED-SC-0002`/`ED-SE-0002` (§5.8/5.9) deliberately left unruled — pre-existing SC/SE-lane forks,
  out of this IN-lane pass's scope per CLAUDE.md §4's session-lane-scoping convention. Citation
  integrity + currency checks re-verified clean (`validate_ed_citations.py` 0 violations,
  `currency_consistency_check.py` clean, adjudicator baseline unchanged at 21/65).
- **Edge-playability audit — RATIFIED IN FULL 2026-07-05 (Jordan: "Ratify all", post-merge
  instruction on PR #81; merged as #81, ratification batch on the restarted branch).** Seam-level
  complement to PR #77: ~60 edges, 8 sonnet clusters, Fable-verified V1–V22. Deliverables at
  `designs/audit/2026-07-05-edge-playability-audit/` (all statuses now RATIFIED): report
  (verdict "the seams are the old GM's chair, still empty"; EP-1..EP-11 P1s, ep-12..ep-31 P2/P3
  register, SIG-1..4), grounding, dossiers + verification log. **All 10 §7 remediation items
  FILED 2026-07-05:** `ED-IN-0012` registry×rendering sweep · `ED-IN-0013` GM-token sweep of the
  handoffs (**renumbered 2026-07-07 to `ED-IN-0019`/`ED-IN-0020` respectively — armature §5.10,
  see the ratification entry below; `ED-IN-0012`/`ED-IN-0013` now mean the SC-audit batch content
  only**) · `ED-IN-0014` key the silent emitters (settlement/ci_political/era) · `ED-IN-0015`
  seam-feedback authoring convention · `ED-IN-0016` index the joints (CURRENT.md rows +
  faction_politics doc:null flip) · `ED-SE-0002` Accord/Order stacking ruling (**needs_jordan**:
  the ruling itself) · `ED-FA-0002` strategic-turn surface / domain_actions home doc ·
  `ED-FA-0003` BG victory-params re-export · `ED-FI-0002` counter-espionage loop · `ED-WR-0003`
  ambient-fabric window + Appraise Revelation (ED map also in the report §7 addendum;
  id_reservations bumped; SE/FA/FI/WR handoffs cross-referenced). P2/P3 register items without a
  §7 ED are ratified-as-findings, drawable for future allocations against the report. The five
  IN items execute in this lane; workplan-v6 sequencing applies.

- **Qualitative NERS audit (North-Star) — DELIVERED 2026-07-04, awaiting Jordan review (PR #77,
  branch `claude/ners-audit-fable5-9cpfdz`).** Corpus-wide qualitative audit (playability /
  cohesiveness / interdependencies / emergent narrative / threadwork-at-every-juncture), 55-agent
  adversarial workflow (12 dossiers + 5 degenerate-play hunters + 7 lenses; every carried finding
  refuted-or-confirmed with an intent gate). Deliverables at
  `designs/audit/2026-07-04-ners-qualitative-audit/`: `ners_qualitative_audit_v1.md`
  (verdict-first, throughlines-tree organized; 5 confirmed findings F-1..F-5 + 2 corpus signals
  S-1 register back-propagation blindness / S-2 steering-surface fragmentation),
  `strategic_judgments.md` (J-1..J-15: playable-season milestone, Gate-0-before-more-combat-depth,
  transport-seam closure, collision-engine detector, anti-drift + roadmap governance),
  `ed_options.md` (E-1..E-12 drafted candidates, **deliberately NOT filed** — Jordan picks and
  allocates per id_reservations protocol; merging PR #77 ratifies nothing). Follow-ups if adopted:
  E-2/E-3/E-7 are the recommended first three; GAP-1 = investigation lane never audited (E-12);
  32 deferred-unverified P2 candidates in `01_workings/deferred_unverified.json`.
- **Qualitative NERS audit (North-Star) — RATIFIED-AS-ACCEPTED 2026-07-05 (Jordan post-merge
  instruction on PR #77).** Corpus-wide qualitative audit (playability / cohesiveness /
  interdependencies / emergent narrative / threadwork-at-every-juncture), 55-agent adversarial
  workflow. Deliverables at `designs/audit/2026-07-04-ners-qualitative-audit/` (all statuses now
  RATIFIED): audit v1 (5 confirmed findings F-1..F-5 + corpus signals S-1/S-2),
  `strategic_judgments.md` (J-1..J-15), `ed_options.md`. **All 12 ED options FILED 2026-07-05**
  (forks resolved to audit defaults — E-1 adopt governance redesign; E-4 per-subsystem
  walkthrough policy; E-8 MS wins MS/RS): `ED-SE-0001`, `ED-IN-0003..0008`, `ED-WR-0001/0002`,
  `ED-PC-0001`, `ED-SC-0001`, `ED-FI-0001` (map in ed_options.md addendum; id_reservations
  bumped). ED-IN-0003 (convergence detector) + ED-IN-0004 (articulation triggers) are acceptance
  criteria of the **2026-07-05 emergent-narrative-engine design effort (IN FLIGHT, this branch)**
  — see `designs/audit/2026-07-05-emergent-narrative-engine/` once landed. Remaining filed items
  execute in their own lanes.

- **Emergent Narrative Engine design v1 — DELIVERED 2026-07-05, awaiting Jordan review (PR #78).**
  25-agent design workflow (4 dossiers → 3 architects → 3 judges + synthesis → 5 refuters → 5
  spec sections → 3 capstone verifiers → critic) + full remediation. Result: **the Arc-Vector
  Engine with a Subordinate Director** (B won all judge lenses; six layers,
  detect-then-schedule-then-render), closing ED-IN-0003 (L2 convergence detector) + ED-IN-0004
  (L5 render completion incl. the four ED-681 thread beats, worked) by construction. Deliverables
  at `designs/audit/2026-07-05-emergent-narrative-engine/`: `narrative_engine_design_v1.md`
  (head doc: architecture, staging, determinism, 9 open forks), `integration_with_ners_audit.md`
  (crosswalk), `00_grounding/` (charter with Jordan's four key considerations + C1–C7),
  `01_workings/spec_sections/s1..s5` (normative chapters incl. the ARC-S07 capstone trace,
  factionless mini-trace, effect-bearing COLLISION-B trace). **9 [OPEN — Jordan] forks — esp.
  fork 8 HELD BACK (director tension-curve subtract-only reverses charter language; not
  self-ratified by merge)**; forks 1–2 (Coup-Counter remap; ARC-T04 strike-or-author) block
  Stage 1. Corpus defects surfaced for follow-up: Coup Counter STRUCK but live in 6 register
  entries; ARC-T04 dangling; Torben Loyalty range register-vs-clock_registry conflict.

- **Narrative engine v2 "THE CHURN ENGINE" + Master Workplan v6 + steering reconciliation —
  RATIFIED IN FULL 2026-07-05 (Jordan: "Ratify commit merge all"; ED-IN-0009/ED-IN-0011;
  PR #78 merged). All stated fork defaults adopted incl. F-F/fork-8; fork 10's faction
  count = ED-FA-0001 (open, needs_jordan). Originally delivered as:** v2
  (`narrative_engine_design_v2_churn.md` + `spec/churn_amendments.md`, supersedes-in-part v1)
  reorganizes the engine around Jordan's churn critique: generator-not-corpus (templates ×
  binding, 138 register arcs = validation set), two-layer forecast (Layer A analytic — the M1
  ship, hard gate; Layer B seeded ensemble behind named preconditions incl. F7/F8), **the
  Light Function** (pruning-as-authorship; invariants i–iv; forecast severed from casting and
  actor-invisible per the adversarial pass), claim-grammar interface (a requirements input
  ADDING four SC sub-systems — shapes the SC lane's), load factorization (no runtime LLM;
  bake headline ~1,200–2,700 units under fork-6 default), kernel/data/wrapper modularity
  (nothing hard-baked; R-F1/R-F2/R-HB/R-CL/R-AI/R-RL). Five-refuter pass
  (`01_workings/refute_v2_*.md`) fully applied; survivors = forks 10–11 + fixture F8. **⚠️
  F-F/fork-8 (the Light-Function weight set + subtract-only discipline) is HELD BACK from
  merge-ratification — needs explicit Jordan sign-off.** Grounded by two dossiers
  (`01_workings/dossier_forecast_tractability.md`, `dossier_combinatorial_census.md`).
  **Workplan v6** (`workplans/valoria_master_workplan_v6.md`, ED-IN-0009): M1/M2/M3
  milestones, IN spine, per-lane sequencing, tiered T0/T1/T2 decision register (no status
  fields), governance incl. the ED-PC plan-text-label rule. **ED-IN-0006 EXECUTED**:
  roadmap_state → `deprecated/references/` (banner), v5 → `deprecated/archives/workplans/` (banner
  fixing its J-38 contradiction), decision-queue items 1–3 refreshed + queue demoted to
  dated snapshot, CURRENT.md rows updated (workplan v6 + new Narrative-engine row),
  `lane_assignments.yaml` repointed. Next IN actions live in v6 §2. **⚠️ F-F/fork-8 note
  below is superseded by the ratification above.**

- **Ecosystem-review Top-5 residuals not covered by their own lane.** Filed 2026-06-30 as
  ED-1050..1054 (full report: `designs/audit/2026-06-30-ecosystem-adversarial-review.md`).
  ED-1050 (combat parity oracle) lives in `registers/handoffs/HANDOFF_PC.md` (RESOLVED, one residual
  left). This lane owns the rest:
  - **ED-1051 — module-contract gaps, `needs_jordan`.** `references/module_contracts.yaml`
    has 11/27 modules `doc:null` (grew from the originally-filed 10/27) and 13/27 resolvers at
    `[ASSUMPTION]` grade (grew from 11/27) — re-measured 2026-07-02, docket adjudication
    ED-IN-0002. `engine_clock` (the temporal spine, highest-priority module) now has a
    CANDIDATE home doc — `designs/architecture/propagation_spec_v1.md` (ED-1093, CANONICAL) —
    its `gap_notes` explicitly keep `doc:null` unflipped until this entry is ruled. Authoring
    is effectively done for `engine_clock`; only ratification/ordering remains for it, plus the
    other ~10 modules and 13 resolvers untouched. Also tracked at `decision_queue.md` item 12.
  - **ED-1052 — typed engine-params layer for Godot ingestion, still open.** No scope/fence
    decision made. A narrower path was found and executed (2026-07-01): `tools/export_engine_params.py`
    serializes the LIVE `combat_engine_v1/config.py` Class-C oracle directly to
    `engine/engine_params/combat_engine_v1.json` (blocking CI round-trip check),
    sidestepping the settled-vs-in-flux dilemma without deciding the broader
    `params/*.md`-prose-parsing question (its own docstring is explicit it does NOT parse
    prose). A prior attempt (PR #37) asserting a Combat Pool formula as authoritative was
    REVERTED — that's the trap to avoid: type only what's genuinely settled, or mirror the
    live oracle mechanically. Also tracked at `decision_queue.md` items 17 and 24.
  - **ED-1054 — navigation surface, partially done, narrowed 2026-07-02 (ED-IN-0002).**
    Retired-session-file relocation to `deprecated/` is DONE (via ED-1084). Still open: (a)
    relocate the ~850KB of narrative markdown mislabeled as tests
    (`tests/emergent_arc_skeleton_test_2026-04-17_batch*.md`,
    `tests/sim_framework/session_audit_2026-04-19.md`) to `designs/audit/` or `deprecated/archives/`;
    (b) regenerate `sim/README.md` (self-flags stale rather than being rewritten accurate),
    `sim/CONVENTIONS.md` (still `[PROVISIONAL — Pass 2l armature scaffold 2026-05-17]`), and
    `tools/README.md` (missing `currency_consistency_check.py`, `ci_module_shape_check.py`,
    `export_engine_params.py`, `validate_ed_citations.py`). Also tracked at `decision_queue.md`
    item 25.
  - **ED-1053 RESOLVED 2026-06-30** (see Decisions below).

## Decisions

- 2026-07-12 — **Skills-ecosystem staleness remediation, "Phase 7" (ED-IN-0044..0042) — continues
  the 2026-07-11 audit-ecosystem batch (ED-IN-0032..0037) this file's Pending/Decisions log never
  got an entry for; note that gap here rather than backfilling the missing history.** Jordan asked
  for a cohesive update of all skills plus a gap scan. A 3-agent parallel audit of all 15 live
  skills against CLAUDE.md's current architecture found: three skills independently pointed P1/P2
  findings at the FROZEN flat `registers/editorial_ledger.jsonl` instead of the live lane-split files
  (`valoria-mechanic-audit`, `valoria-module-adjudicator`, `valoria-resolution-diagnostic` —
  ED-IN-0044); `valoria-compiler` had four independent breaks including a nonexistent gate field
  and an orphaned `compilation/` output path (ED-IN-0044); and `valoria-combat-simulator`'s
  bundled script was a fully superseded parallel implementation (a frozen 9-weapon 2026-03-31
  model vs. the live 51-weapon `combat_engine_v1/workbench/balance.py`), retired to
  `deprecated/skills/` after Jordan confirmed via AskUserQuestion (ED-IN-0045). Also, per Jordan's
  explicit confirmation: `valoria-dice-model` gained the canonical continuous (Godot-mode)
  resolver alongside the legacy discrete one, validated against the existing Monte Carlo
  implementation (ED-IN-0040). Closed one cheap ecosystem gap: PP-NNN allocation had no
  documented protocol despite `id_reservations.yaml` already reserving PP blocks the same way as
  ED — added to `valoria-editorial-register` (ED-IN-0041). Deferred gaps (Godot port-readiness
  tracking, session lane-scoping enforcement, `compliance_check.py` local-hook integration, missing
  sim↔port parity tooling) filed as `ED-IN-0042`, `needs_jordan: true` — see
  `designs/audit/2026-07-12-skills-ecosystem-audit/skills_ecosystem_audit_v1.md` for full detail
  and the per-gap suggested shape.
- 2026-07-09 — **Follow-on token-efficiency pass: dead GitHub-API tools retired, observability
  register re-capped, two stale size warnings resolved.** Jordan: "What other steps can we take to
  increase token efficiency... How often are we calling in from GitHub needlessly instead of just
  looking at local cloned repo?" then "All please, but carefully." A subagent traced every
  GitHub-API code path in the repo first: **zero live-invoked tools touch the GitHub API** — the
  ED-1053 migration to working-tree reads is complete for every gate CI/hooks actually run. What
  remained was dead code that only *looked* live, independently re-verified (grep for each
  filename across every workflow/hook/skill/Python import) before touching anything:
  - **Retired to `deprecated/tools/` / `deprecated/engine/`** (mirroring the existing
    `valoria-orchestrator` → `deprecated/skills/` precedent, not hard-deleted):
    `extract_values.py`, `extract_proper_nouns.py`, `valoria_collator.py`, `valoria_bulk_fix.py`,
    `file_lookup.py`, `compliance_dryrun.py`, `engine/engine_audit_harness.py`. Also
    `skills/prose-writer/scripts/consistency_check.py` (the GitHub-API-only naming-gate predecessor
    `tools/ci_naming_check.py` itself documents as superseded) → `deprecated/skills/prose-writer/scripts/`.
    Fixed the two `references/ci_checks_registry.yaml` rows that asserted a live pairing to two of
    these (`abbreviation_registry_gate` → `valoria_collator.py`, `forbidden_token_gate` →
    `consistency_check.py`) — both pairings were already stale/never wired, confirmed by grep.
    **`tools/canon_coverage_check.py` deliberately left in place** — GitHub-API-based and unwired
    too, but its own registry entry says `ci_job: ""  # not yet wired — Jordan to decide`, a
    pending-decision status, not confirmed-dead legacy.
  - **Dead single function removed in-place** (file itself is live): `fetch_full()` in
    `skills/valoria-vector-audit/scripts/vector_audit.py` — a GitHub Contents API helper with zero
    callers, vestigial from before the read-path rewrite (LB-22). Removed with its now-unused
    `urllib.request`/`base64`/`json` imports; file still compiles.
  - **`tools/observability/DECISIONS.md` re-capped**: was 59,085 tokens (4x its 15k
    `atomization_rules.yaml` cap) purely from `build_decisions.py`'s `PER_CAT_CAP=60` truncation
    setting being too generous — nothing reads the .md for completeness (console.html and any
    programmatic consumer read the uncapped `decisions.json`, unchanged). Dropped `PER_CAT_CAP` to
    12 and regenerated; file is now ~6.3k tokens. (Regeneration also re-swept the current corpus,
    surfacing the counts have drifted since the file's one prior commit — expected, not a bug.)
  - **Two other standing `compliance_check` size warnings resolved**, not by pruning content but by
    fixing the governance that was wrong: `references/module_contracts.yaml` (~14.4k tokens) was
    hitting the generic 10k `**/*.yaml` catch-all with no policy ever written for it despite being a
    genuinely comprehensive, actively machine-checked 27-module registry (CLAUDE.md §6 already notes
    it's expected to grow, not shrink) — raised its explicit cap to 18k, `warn_only`, same treatment
    as `canonical_sources.yaml`/`mechanical_terms_index.md`. The attribute/value coherence audit's
    `02_census/quantity_census.yaml` (~18.5k tokens) is a self-declared frozen evidence artifact
    ("QUARANTINE-NOTE: not a registry, not canonical truth") hitting the same catch-all with nothing
    to act on — given `on_exceed: skip`, scoped to that one file (not a blanket `designs/audit/`
    exemption). `compliance_check.py --check-only --repo-state .` now reports 0 warnings, 0 errors
    (previously 3 standing warnings).
  - Model-tiering gap noted but **not code-fixed**: of three persisted Workflow scripts in
    `.claude/` (git-tracked, each a provenance record of one already-executed audit —
    `wf_attribute_coherence.js`, `wf_combat_critique.js`, `wf_social_contest_critique.js`), only the
    first shows real haiku/sonnet/opus/fable tiering per CLAUDE.md §10; the other two have almost no
    `model:` overrides. These are historical run records, not reusable named workflows (no
    `.claude/workflows/` dir exists) — editing them now wouldn't change any past cost and would
    misrepresent what actually ran, so left as-is. The actionable form of this finding is: apply
    §10 tiering when *authoring* the next heavy audit/critique workflow, not a retrofit here.
  - Verified: `compliance_check.py --check-only --repo-state .` (0/0), `ci_register_size_check.py`,
    `ci_hooks_verifier.py` (dead-tool `/home/claude` warnings dropped from 6 files to the expected
    remainder), `ci_naming_check.py`, `currency_consistency_check.py`, `validate_ed_citations.py`
    (0 violations), `broken_dependency_checker.py` (clean), full `tests/valoria` suite — all green.
- 2026-07-08 — **Second HANDOFF atomization pass + editorial-ledger lane split.** Jordan: "Make it
  so that handoffs are by lane, not just a giant document. Break up handoffs and editorial register
  for that reason because they should be atomized for better management." Two changes:
  (1) root `HANDOFF.md`'s "## Next actions" section still carried ~9k tokens of lane-owned bullets
  (mass battle, PC, IN, SC) despite the 2026-07-02 lane split below — every one was cross-checked
  against its lane file first (most were already duplicated there verbatim) and dropped rather than
  re-copied; the two genuine gaps found (R2 capstone finding, J-36) were backfilled into
  `HANDOFF_PC.md`/`HANDOFF_IN.md` before trimming root. Root is now ~95 lines / ~1.6k tokens, only
  cross-lane content. (2) `registers/editorial_ledger.jsonl` (404 live entries, ~150k tokens, previously
  ungoverned by lane) split the same way: the 115 entries whose id already declares a lane
  (`ED-<LANE>-NNNN`) moved to their own `registers/editorial_ledger_<lane>.jsonl`; the 289 pre-cutover
  flat-ID entries stayed put (no retrofit, same precedent as the ID-namespace cutover itself). Main
  ledger dropped from ~150k tokens (at its own cap) to ~90k. Updated
  `tools/validate_ed_citations.py` (reads main + all lane files as "active") and
  `tools/broken_dependency_checker.py`'s `check_editorial_ledger` (same — the lane-tagged third of
  live entries would otherwise silently stop being checked for broken paths, the exact failure class
  ED-1081 already fixed once) and `tools/ci_register_size_check.py` (per-lane caps). Verified:
  `validate_ed_citations.py` 0 violations, `broken_dependency_checker.py` clean,
  `ci_register_size_check.py`/`compliance_check.py --check-only` clean, `currency_consistency_check.py`
  clean, full `tests/valoria` suite green.
- 2026-07-07 — **Consolidated ruling pass on the Key & Echo armature §5 docket + ed_options.md
  (ED-IN-0026).** Jordan: "Perform consolidated ruling pass? I want to ratify all and get to work
  on this" — exercising, before merge, the ratification authority PR #85's body had deliberately
  held back. Per-row disposition lives in `key_echo_armature_v1.md` §5's Ruling Log (16 rows) and
  `ed_options.md`'s Disposition table (17 filed EDs). Two rows were genuine no-default forks
  needing an actual pick: the ED-IN-0012/0013 renumber (executed) and the ER-2/Overwhelming
  band-discipline direction (ruled, execution deferred). Two rows (ED-SC-0002, ED-SE-0002) were
  explicitly left to their owning lanes rather than ruled from this IN-lane pass. See the Pending
  entry above for the full headline list.
- 2026-07-02 — **HANDOFF.md split into per-lane files, matching the `ED-<LANE>-NNNN`
  nomenclature.** Jordan: "Handoffs need to have the same tagging nomenclature. There are
  different handoffs for different lanes." Root `HANDOFF.md` is now a thin index + genuinely
  cross-cutting "Next actions" pointer; each lane (`MB, PC, FI, SC, FA, WR, IN, GO, SE`) gets
  its own `registers/handoffs/HANDOFF_<LANE>.md` carrying that lane's Pending/Decisions/Next-actions.
  Motivation is the same one behind the `ED-<LANE>-NNNN` split itself: reduce concurrent-session
  merge-collision surface on shared continuity files. Note this partially reverses an EARLIER,
  deliberate consolidation (`deprecated/session_machinery/` retired per-topic session-log files
  in favor of one `HANDOFF.md`, because fragmented files rotted/went stale) — the difference
  this time is the fragmentation is keyed to the SAME lane taxonomy the ID system already
  enforces, not an ad-hoc per-topic split, and `tools/session_status.py`'s SessionStart banner
  still reads one root file so there's still a single "start here" surface, just a thinner one.
  `tools/session_status.py` unchanged (still greps root `HANDOFF.md`'s one `## Next` heading).
- 2026-07-02 — **`ED-<LANE>-NNNN` lane-tagged editorial namespace created (`ED-IN-0001`, PR #67,
  merged); D1-D5 adjudication docket reconciled (`ED-IN-0002`, PR #69, merged).** PR #58 hit two
  same-session concurrent-allocation collisions on the flat `ED-NNNN` sequence within one PR
  (`ED-1088`→`1090`; then `1089`/`1090`→`1093`/`1094` — see `ED-1094`'s own entry). Jordan: new
  EDs use `ED-<LANE>-NNNN` (9 lanes: `MB` mass battle, `PC` personal combat, `FI` field
  investigation, `SC` social contest, `FA` faction actions, `WR` world, `IN` infrastructure,
  `GO` godot, `SE` settlements — `SC`/`PC` deliberately disambiguated after a first draft
  proposed `SC` for both; a proposed `PY` python lane was dropped as not a real subsystem). Flat
  `ED-NNNN` is FROZEN at `ED-1094`, permanently valid, never retrofitted.
  `references/id_reservations.yaml` gained per-lane `next_free` counters;
  `tools/validate_ed_citations.py` and `tools/currency_consistency_check.py` extended to
  recognize both formats; `CLAUDE.md` §3 documents the format plus a new, not-yet-CI-enforced
  session-lane-scoping convention. Separately, Jordan pasted an uncommitted local adjudication
  docket (D1-D5, drawn from the 2026-06-30 ecosystem review's `needs_jordan` subset) for
  relevance-checking against the current tree; verdicts folded into the ED-1050/1051/1052/1054
  entries above (this file) and `registers/handoffs/HANDOFF_PC.md`.
- 2026-07-02 — **Merge-ratifies-by-default convention adopted (ED-1094); ED-1083 doctrine
  ratified; J-38 propagation spec ratified (ED-1093).** Jordan: merging a PR ratifies its
  PROPOSED/provisional contents by default unless the PR body explicitly holds an item back
  for separate review — closes a real recurring gap where PR #55 was reviewed and merged but
  `holonic_container_doctrine_v1.md` (ED-1083) sat PROPOSED in `main` afterward because the
  prior convention required a distinct explicit ratification step nothing forced to happen.
  Applied same-day: ED-1083 flipped provisional → ratified; doctrine `## Status:` line
  PROPOSED → **CANONICAL**; `CURRENT.md` gained an Architecture/Holonic-doctrine row;
  `decision_queue.md` item 20 struck resolved; `CLAUDE.md` §2 documents the standing rule.
  **Applied a second time to J-38 itself, same PR (#58):** rather than land the propagation
  spec as PROPOSED and rely on "ratifies on merge" text (which would repeat the exact ED-1083
  failure mode this convention exists to close), the flip to CANONICAL was pre-staged in the
  PR — `designs/architecture/propagation_spec_v1.md` `## Status:` line PROPOSED → **CANONICAL**,
  ED-1093 ledger entry `status` → `ratified`, `decision_queue.md` item 18 struck resolved. A
  whole-session Fable review (triggered after the ED-1088 ID-collision reconciliation) caught
  this risk plus stale cross-references before merge. Scope: governs future PRs; does not
  retroactively reopen closed decisions or ratify anything a PR explicitly holds back and flags
  loudly as such.
- 2026-07-01 — **Month-overview + architecture-consolidation session executed** (12+ commits,
  ED-1081..1087; overview + execution/reconciliation logs + the frozen 23-item Jordan decision
  queue at `designs/audit/2026-07-01-month-overview-architecture-consolidation/`). Landed:
  LB-21 round-3 ID re-block · two silently-dead enforcement pieces revived
  (`broken_dependency_checker` ledger check; non-executable tracked pre-commit hook) · CLAUDE.md
  §6 falsified claims corrected (ED-1050/ED-1054 states) · holonic container doctrine v1
  **PROPOSED** (`designs/architecture/holonic_container_doctrine_v1.md`, ED-1083 — Jordan-vetoable)
  from the ingested 2026-07-01 workflow spec · Combat Pool collapsed to `max(5, History+6)` across
  every live stale site (ED-1084) · `values_master.yaml` QUARANTINED · names_index v2 (proper-noun
  fold; mirror 23→83) · session-log machinery → `deprecated/session_machinery/` · combat engine
  runtime **numpy-free** (σ-kernel via `sim.autoload.sigma_leverage`; state kernel engine-owned;
  ED-1085) with new container-hygiene guard · **first typed Godot params artifact**
  (`engine/engine_params/combat_engine_v1.json`, blocking round-trip CI; ED-1052 seed) ·
  contract-conformance CI (report-only; ED-1051 backlog surfaced per-PR) · CLAUDE.md §10 fable
  tier + relay patterns; workplan **J-38** (propagation-spec authorship) docketed ·
  `currency_consistency_check` self-updating recency gate (CI + SessionStart banner; ED-1087) ·
  freshness pins refreshed + gate flipped **blocking** (LB-23 residual closed). Three scope
  defaults adopted Jordan-vetoable (values_master quarantine-not-regenerate; Godot seed included;
  freshness flip). Rulings made: **none** — everything gated sits in the decision queue.
- 2026-06-30 — **ED-1053 resolved: working-tree integrity port + sim oracle.** Ported the three
  "integrity" gates off the GitHub API to the working tree (no PAT/network): `broken_dependency_checker`
  and `patch_propagation_checker` now `os.walk`/read locally (both green against the checkout);
  `freshness_gate` computes git blob SHAs locally (verified identical to `git hash-object`) and checks
  119/131 `canonical_sha__` pins (12 stale → report-only). Dropped `GITHUB_PAT` from the CI integrity job.
  Hardened `ci_sim_fabrication_check`: full float-literal capture + `(variable,value)` matching close the
  value-collision / float-split holes (corpus blast kept to +~200 latent, changeset-scoped; `tools/`
  excluded from sim-classification). Added the first `sim/` test — `sim/tests/test_mc_v18_regression.py`
  (deterministic seeded `run_batch(n=2,seed=0)`: determinism + golden + bounded smoke) — and a new
  'Sim Reference Regression' CI job wired into All-Gates-Green. Updated CLAUDE.md §8.
- 2026-06-30 — **Adversarial ecosystem review + safe fixes.** Ran a 72-agent verification workflow
  (6 audit dimensions × 2 skeptical lenses); 24 findings survived, headline items hand-spot-checked.
  Rewrote `CLAUDE.md` into a Claude-Code-optimized operating manual (numbered sections, currency
  priority, data→Godot pipeline, port state, known-defect callouts). Filed the report under
  `designs/audit/` and the Top-5 as ED-1050..1054. **Re-blocked IDs** (`references/id_reservations.yaml`
  v2: round-1 A/B/C exhausted+overrun to ED-1042; round-2 block D = ED 1050-1099 / PP 800-829, next_free
  ED-1081, after contest_rebuild reserved 1055-1079 + combat at 1080). **Safe code/doc fixes applied:** single-sourced the patch-register size cap
  (`ci_register_size_check.py` 20k→policy 15k; register is ~5k); RETIRED banners on
  `references/subsystems/{handoff,checkpoint,session_log}_subsystem.md`; flipped
  `canon/session_checkpoint.md` `status: active`→`retired`; STALE banners on the four `godot/*.md`
  specs; rewrote `README.md` to defer to CLAUDE/CURRENT/HANDOFF. **Not done (needs Jordan / re-sweep):**
  the parity-oracle balance values (ED-1050) and the Gate-0/contracts authoring (ED-1051).
- 2026-06-29 — **ED-citation integrity: full reconciliation (292 → 0; gate now BLOCKING).** Diagnosed the
  292 report-only violations: 286 `NONEXISTENT` from **dual ledger-of-record drift** (design docs minted ED
  numbers in inline `[EDITORIAL:]` tables never migrated to the JSONL), 6 `OPEN_AS_BASIS` (2 of them validator
  false positives). Fixed 3 validator defects (`tools/validate_ed_citations.py`): active-ledger precedence
  over stale archives, loud-parse + regex-salvage of 7 malformed archive YAMLs, and same-line basis scoping
  (table-row bleed). **Registered 91 grounded entries** (36 resolved / 12 provisional / 30 open / 13
  needs_jordan) — each verified against its citing doc by per-batch subagents (anti-fabrication). Repointed
  the ED-814→ED-907 phantom and reworded open/provisional over-claims to `pending`. Dropped `continue-on-error`
  on the `ed-citations` CI job + added to `ci-summary` needs. Report:
  `designs/audit/2026-06-28-ed-citation-triage/02_reconciliation.md`. **Residual for Jordan:** 13 needs_jordan
  items (NPC naming ED-634/595–602/610, ED-885 ratification ID); ID collisions ED-408–411/413/417/647.
- 2026-06-28 — **Editorial-ledger relevance triage.** Deep per-item verification of all **93 unresolved**
  entries (82 open + 10 provisional + 1 deferred) against the live working tree, in 6 read-only cluster
  passes. Result: **37 still relevant** (25 real open work + 12 NEEDS_JORDAN), **56 stale**. Applied via
  Workflow D: **31 struck** (21 superseded by later canon — esp. the mass-battle per-cell/Lanchester
  re-architecture + the 2026-06-22 `net-(Ob-0.5)` continuity fix; 10 `[PROPOSED:…]` migration residue),
  **25 resolved** (open-but-done — decision had landed, row never closed). Unresolved queue 93→37.
  ED-citation violations dropped 315→292 as a side effect. Report:
  `designs/audit/2026-06-28-editorial-relevance-triage/relevance_triage.md`. **Residual for Jordan:** 12
  NEEDS_JORDAN items (NPC naming ED-649/650/651, deferrals ED-644/788, design-intent gates
  ED-879/893/911/920/924/1033/1036); three of these (644/649/893) are the OPEN_AS_BASIS citations still
  holding the ED-citation validator report-only.
- 2026-06-28 — **Open-session unification + LB-22 closed.** Reviewed every `origin` session branch;
  six were already squash-merged into main (#14–#21), one (`claude/github-ci-environment-review` = PR #18)
  carried genuinely-unmerged work, and `claude/refresh-state-3m7nL` (abandoned 04-20 pre-migration line
  carrying the retired `session_checkpoint`/`session_log` harness) was excluded from the merge. Unified
  PR #18's **net-new** half (the LB-22 backlog) onto main — its already-landed half (12 skills +
  coverage_matrix, via #16) was kept at main's version, no re-litigation. **LB-22 done:** `valoria-orchestrator`
  retired to `deprecated/skills/`; `valoria-vector-audit` read-path rewritten; `ci_hooks_verifier.py`
  Check 4 flipped to **blocking for `skills/`** (`tools/` stays WARN pending the API→disk port). PR #18
  closed as superseded. `ci_register_size_check.py` taken from #18 (importable, no-PyYAML, ships the
  drift-guard test) with #22's `names_index.yaml` threshold line re-added; `lane_assignments.yaml`
  owns-globs repointed to `deprecated/`.
- 2026-06-28 — **Master Workplan v5** authored (`designs/audit/2026-06-28-recent-work-orchestration/`),
  reconciling the post-v4 work (06-12→06-28) into one register and superseding v4. Roadmap +
  lane_assignments repointed to v5. Ledger verified live: **713** entries / 0 duplicate IDs / ED 1042.
  (v5 de-staled this pass to live HEAD; PRs #16–#22 reconciled — see its §0/§10.)
- 2026-06-24 — Migrated the Claude↔GitHub automation to a Claude Code-native model:
  retired the `/home/claude` GraphQL/cache/session harness; gates now live once in `tools/`
  and run in CI (authoritative) + local hooks/`.githooks` (advisory). See the migration PR.
- 2026-07-01 — **Workplan sprawl cleanup.** `workplans/` was dead (both files pre-dated v3/v4)
  while the live master workplan kept spawning in a fresh one-off `designs/audit/<date>-*/` folder each
  revision, so `CURRENT.md` had to manually chase it. Relocated v5 into `workplans/` (now the
  one live home — see its `README.md`); archived the two dead files to `deprecated/archives/workplans/`. Repointed
  `CURRENT.md`, `references/lane_assignments.yaml`, `references/roadmap_state.yaml`, and v5's own §0
  commit-path note. Frozen historical versions (v4 in `designs/audit/2026-06-11-orchestration/`, v3 in
  `2026-06-10-master-workplan-v3/`) were left in place intentionally — they're bundled with sibling
  audit artifacts and CURRENT.md already documents them as frozen records, not lost ones. Separately,
  flagged (not moved) the `sim/` vs `tests/sim/` vs `tests/sim_framework/` naming collision — three
  distinct-purpose directories, not duplicates; disambiguated via README notes in each rather than a
  path rename, since `tests/sim/` is path-matched by `ci_sim_fabrication_check.py`/`atomization_rules.yaml`/
  `lane_assignments.yaml` and a rename would need to update all three.

## Next actions

- **WS0 Structural Observatory + WS1 registry reader (2026-07-13/14, ED-IN-0057..0063)** — the five
  Tier-0 audit scripts (`skills/valoria-vector-audit/scripts/{vector,structure,pointer,formula,gen}_audit.py`)
  and the read-only facade `tools/registry.py` (+ `references/registry/README.md` &
  `pointer_debt_worklist.md`, both **PROPOSED**) are built, merged (PRs #132/#135/#137), and
  hardened by two adversarial passes (a partial Fable-5 audit + a 5-critic holistic pass,
  `designs/audit/2026-07-14-holistic-unification/`). **Open, Jordan-gated decisions surfaced there:**
  (1) **`ED-IN-0059` pointer-debt worklist Category B** (register the genuinely-unregistered scalars —
  Wounds/Turmoil/Accord/etc., each needs a canonical key + home-doc verification) and **Category C2**
  (whether npc_behavior's `beliefs`/`concerns`/`projects`/`arc state` are registry quantities at all);
  (2) whether the observatory gets a **non-gating CI refresh job** that persists scorecards (it is
  runnable now but wired nowhere — `audit-refresh.yml` deliberately does not run it); (3) `settlement_layer`
  derivation `Legitimacy / Popular Support` (module_contracts.yaml) is a Mandate-feedback drift loop with
  **no `bucket:` tag** — is it a `derived_value` or a track-write? These are the concrete "needs_jordan"
  items a resuming session must not silently skip.

- **Governance Type Registry (2026-07-13)** — `designs/architecture/governance_type_registry_v1.md`
  inventories every governance/politics/hierarchy/faction/geography type across the corpus (4 parallel
  survey passes + this session's generation-methodology work), classified FLAG vs. VECTOR, cross-scale
  throughlines named (§3), 5 same-name/different-scale naming collisions surfaced unresolved (§2.8),
  and a grounded (not ratified) proposal for a `Field`/`Gauge` substrate primitive extending
  `key_echo_armature_v1.md` to cover continuous VECTOR state — closing the OF-3 `decay()` fork
  (deferred 2026-07-07, `key_echo_armature_v1.md §5.2`) generically instead of per-track. **Read this
  before authoring any new cross-scale accumulation/propagation/decay mechanic** — it names two
  working templates (MS's hysteresis+falloff, Π's homeostat clamp) to generalize from rather than
  re-deriving. OF-3's `decay()` fork itself is still Jordan's to rule.

_(Reserved-ID state healthy as of 2026-07-02: LB-21 executed, then the `ED-<LANE>-NNNN` cutover
(ED-IN-0001) froze the flat sequence at `ED-1094`. `references/id_reservations.yaml`'s `lane_ids`
section is now the live allocation source for all NEW EDs — read `next_free` for your lane,
allocate, bump, co-commit; never max+1.)_

- **START HERE — month-overview + consolidation (2026-07-01), doctrine + propagation spec now
  RATIFIED (2026-07-02).** The month's comprehensive review, the consolidation
  execution/reconciliation logs, and the **single consolidated 23+2-item Jordan decision queue**
  live at `designs/audit/2026-07-01-month-overview-architecture-consolidation/` (see
  `decision_queue.md` first — every gated item below is indexed there). **Doctrine ratification**
  (ED-1083, `designs/architecture/holonic_container_doctrine_v1.md`) and **J-38 propagation-spec
  authorship** (ED-1093, `designs/architecture/propagation_spec_v1.md` — supplies `engine_clock`'s
  candidate home doc; the `doc:null`/[ASSUMPTION] grade stays unflipped until ED-1051 is
  separately resolved) are both **CANONICAL** as of PR #58 (ED-1094 merge-ratifies-by-default).
  The propagation spec's own §5 carries its ranked open items (OF-7/OF-B1 amendments, D.6/OF-D6
  double-count, `decay()` spec, RNG-MODEL-COLLISION, cap constants, ORD-3/ORD-4) — ratification
  did not resolve these, only fixed the spec's home-doc status. Remaining highest-leverage queued
  decisions: the values_master regenerate-vs-retire call, the duplicate compilation homes, and
  item 19 (Agent-Teams/subagent-roster adoption).
- **Done this pass:** unified PR #18's net-new into main → **LB-22 complete** (orchestrator retired to
  `deprecated/skills/`; `valoria-vector-audit` read-path rewritten; `ci_hooks_verifier` Check 4 blocking
  for `skills/`). Earlier passes already landed the coverage_matrix single-source + 12-skill boilerplate
  strip (#16) — kept at main's version during the unify.
- **LB-22 residual (small):** `tools/` analysis utilities still carry `/home/claude` refs (WARN tier in
  `ci_hooks_verifier`); flip the `tools/` scope to blocking only after the GitHub-API→working-tree port
  (`freshness_gate`, `broken_dependency_checker`, `compliance_check`, `extract_*`, `valoria_collator`,
  `valoria_bulk_fix`). `valoria-orchestrator`'s old `tests/registry/test_descriptor_registry.py` import
  is dead (reads `/home/claude/…`, not CI-collected) — left as-is.
- **CI debt blocking-flips (LB-23) — reconciled 2026-07-01 (ED-1082):** `validate_ed_citations`
  is **already blocking** (since 2026-06-29, 0 genuine violations — the old "flip once triaged"
  action here was stale). `freshness_gate`'s remaining report-only step is being closed by the
  month-overview consolidation itself (pin refresh + blocking flip as its final commit); the
  optional K-2 SHA-split (115 `canonical_sha` fields → `references/canonical_freshness.yaml`)
  is a refactor that can follow independently, no longer a precondition.
- **`ci_political_v30` read-routing (LB-24):** raw file ~26k but tracked read returns 0
  (index-routes). Tooling/routing bug, not a faction-content decision — cross-referenced in
  `registers/handoffs/HANDOFF_FA.md` since the file itself is faction/political content.
- **Ledger-status reconciliation (LA-23, Lane A — mostly done):** flipped ED-841/842/912 `open`→`resolved`
  and filed the never-written ED-938/ED-939 (backfilled from #13; artifacts verified). Dropped the
  report-only `validate_ed_citations` count 748→731. **Residual:** ED-914 left `open` — its mechanical
  parts remain (PP-719 record-or-strike; dead `fieldwork_design_v1` parent-path refs in `params/bg/core.md`,
  `designs/scene/fieldwork_v30.md`, `designs/scene/fieldwork_godot.md` — cross-referenced in
  `registers/handoffs/HANDOFF_FI.md`).
- **The new `ED-<LANE>-NNNN` namespace's own residual (from ED-IN-0001's PR body):** the
  session-lane-scoping convention (`CLAUDE.md` §3) is documented but not yet CI-enforced —
  detecting which lane a PR's file changes belong to and flagging mismatches is real follow-up
  work, not built yet.
- **J-36 — Key-bus closure for the 6 off-bus writers**, gated on the distillation report's deferred
  adversarial pass. Design-tier docket item awaiting Jordan; see also `registers/handoffs/HANDOFF_SC.md`'s J-31
  (social-contest deliberative-game findings) — the two were tracked together in root `HANDOFF.md`
  before the 2026-07-08 per-lane content split.

- **Observatory Remediation Program filed (2026-07-14, ED-IN-0066 — renumbered off the #139 ED-IN-0065
  collision, PROPOSED)** — `designs/audit/2026-07-14-gameplay-subsystem-observatory/remediation_plan_v1.md`:
  the resolve-everything plan over ED-IN-0064's findings, **incorporating PR #139** (its landed observatory
  integrity fixes; its needs_jordan items as D15/D16; the G_pointer keyed-rate 21.8% baseline; the
  head_pointers.yaml + REPO_MAP.md action in P2). **Next action: Jordan rules the Phase-1 decision docket
  (D1–D16)**; P0 (instrument hardening, net of #139: the G_code __init__ HIGH, banner_classify tie-break,
  contract↔code join, direction_audit.py) can start in parallel, IN lane. Program structure ratifies on
  merge; every D-row stays needs_jordan.

- **Incompleteness Ledger + audit de-cull (2026-07-22, PR #205)** — the vectorization apparatus'
  core purpose is to **SURFACE WHAT IS MISSING**; it had been silently culling (a 16-system
  `SKIP_SYSTEMS` denylist + four length/threshold floors) to stay "signal-heavy" — the exact
  opposite. Fixed: (1) every cull is now a *surfaced, reasoned exclusion*
  (`vector_audit.audit_exclusions()`); (2) new `tools/observability/build_incompleteness.py` —
  the absorb-everything **Incompleteness Ledger** (`INCOMPLETENESS.md` / `incompleteness.json` /
  `_data.js`) scanning the whole tree for every stub/null/missing/excluded/unverified thing,
  surfaced as the dashboard's **Missing** face; (3) doctrine enshrined in
  `skills/valoria-vector-audit/SKILL.md` (⛔ SURFACE, NEVER CULL) so it survives context loss.
  **Next action (pending Jordan design call):** Stage F — wire the 7 island modules + 11 doc:null
  contracts. BLOCKED honestly: the design docs don't speak in the Key vocabulary, so any IN/OUT
  edge is *inference*, not extraction. Do NOT fabricate contract edges into the source of truth;
  author them grounded (e.g. re-point the 3 stale `designs/` doc paths first: `victory`,
  `clock_registry`/overview, `territorial_piety`→`conviction_track`) and mark any inferred edge
  `[ASSUMPTION]`, held back loudly per CLAUDE.md §2. `engine_clock` (ED-1051) + `domain_actions`
  (ED-FA-0002) need canon before their edges are real.

- **"Extend audit in all directions" — trace-completeness pass (2026-07-22, PR #205, in flight).**
  Working most→least impactful with an **adversarial pass at the end of each direction**:
  - **Dir #1 (DONE)** — `discover_unregistered_candidates`: name-level ontology match over the
    whole design corpus (folding + expanded stopwords; critic caught a substring-unsound first cut
    at ~50% noise → rebuilt to 39 high-signal). Feeds the ledger's `unregistered_term` face.
  - **Dir #2 (DONE + reconciled)** — the two observatories now TALK: `vector_audit --emit-findings`
    writes `tools/observability/audit_findings.json` (its UNIQUE cross-graph Mode-B implied-missing +
    Mode-H isolates), the Incompleteness Ledger surfaces them. TWO adversarial passes. Final state
    (commit 68a29955): **retain-and-flag, never cull** — the feed emits EVERY finding with a
    `filtered`+`filter_reason` flag (hub×hub Mode-B, Key-token Mode-H); the ledger consumes the
    unfiltered subset. Every implied-missing row carries a `primary_doc` back-link; every isolate
    links to the REGISTRY that defines it (source→registry map). Isolate text states the STRONG,
    accurate signal (max-deg ≤1 across all four graphs, no design-prose home) — the 2nd critic
    caught the 1st fix *softening* it. `audit_staleness` `vector-audit`+`npc-audit` families
    repointed to live artifacts; scope corrected to the real L0 inputs (systems/engine/canon/arcs/
    audit/references + registers/patch_register_active.yaml — the pp-graph source). Schema
    handshake (`schema_version==1`) self-surfaces a mismatch. Doctrine in SKILL.md.
  - **Dir #3 (DONE, commit 7cb3d432)** — broadened the **throughline graph** from a second registry
    source: `throughlines_complete.md`'s POST-ATOMIZATION `**Systems:**` lines (`parse_throughlines_
    complete` + `build_g_throughline(extra_rows=…)`, opt-in). MEASURED before adopting: +2
    implied-missing, +1 legit hub (Player Agency), 0 new isolates, no blob. The doc's INTERACTION
    MATRIX was measured + REJECTED (20/21 pairs interact → dense, 149/181 edges redundant, would
    inflate Clocks/MS hubs). The **μ graph is NOT extended** — no clean second Μ-mode source
    (`silo_overlap_matrix.yaml` is a frozen snapshot; the complete doc has no μ data). A critic is
    auditing #3 now.
  - **Dir #4 (pending)** — L1-layer validation calibration (P1/P2/P3 thresholds are L0-tuned).
