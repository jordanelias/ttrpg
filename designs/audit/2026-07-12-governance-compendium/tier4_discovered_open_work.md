# Tier 4 — Discovered Open-Work Register

**Scope note.** This tier is not new design content. It is a register of pre-existing, already-authored
work that intersects the governance-redesign proposals under consolidation here, surfaced by reading
`goldenfurt_slice/` and the two territory/settlement audits, but **not acted on** as part of this
compendium pass. Everything below was flagged, not fixed. Treat this tier as a work-intake queue for
whoever picks up governance/territory work next, and as a guardrail against the recurring failure mode
this repo has already hit once (`stress_test_synthesis_v1.md` re-deriving problems the corpus had already
solved) — see the register's closing cross-reference note.

Each entry states: what it is, its severity as assessed by its source document, and whether it blocks
any proposal considered elsewhere in this compendium.

---

## Register 1 — Goldenfurt v1.1 backlog and still-open items

Source: `designs/territory/goldenfurt_slice/README.md` + `verification_findings.md` (4-lens adversarial
pass, 2026-06-23; 32 findings — 15 high / 12 medium / 5 low). Status legend from the source: **✅ fixed**
(this commit) / **✅ v1.1** (fixed on the v1.1 branch) / **⏳** (still open, needs real design revision).
Only the still-open (⏳) items are carried forward here as open work; fixed items are listed in Register
2/3 cross-references only where they bear on this compendium's proposals.

| Item | What it is | Severity (source) | Blocks a Tier proposal in this compendium? |
|---|---|---|---|
| **sim-F4 — predicate-grammar history triggers** | The Π/deck trigger grammar is too weak to express event-history predicates like `Investigated(Tomas)` or `ruled against Orsk`. Fix specified but not built: require history-generating cards to drop a history/Leverage tag, and have triggers read `has_tag(...)`. | High | **Yes, conditionally.** Any proposal that leans on multi-season causal chaining (e.g. a card/Directive escalation keyed to a past ruling) inherits this gap until the tag-based fix lands. Not fatal to ratify design prose, but flag as unimplemented substrate — same caveat pattern as L/PS inertness (Register 3). |
| **npc-F4 — Wessel/Greta collision card is mechanically empty** | The Church (Wessel) vs. Reformed Motherhood (Greta) tradeoff has no verb that actually forces the collision — no card raises one NPC's disposition while lowering the other's. Needed: author a Sponsor/Hold-Court card that creates the tradeoff. | Medium | No direct block on this compendium's Tier proposals, but any proposal citing Goldenfurt as a "fully collision-wired" worked example should note this specific pairing is not yet wired. |
| **npc-F5 — decorative Knots never referenced by a card** | Three narrative Knots (Tomas→Old Brun, Wessel→Aldith, Hedda→Aldith) exist in the NPC dossiers but no deck card or tick reads them — purely flavor at present. Needed: wire each to a card, or formally cut it. | Medium | No. Cosmetic/content-completeness gap, not a mechanical dependency. |
| **npc-F6 — ethic mechanization** | α/β ethic tags on NPCs are flavor only; no card or ambition tick branches on `npc.ethic`. Needed: at least one resolution branch keyed to ethic. | Low | No direct block, but relevant to any proposal that claims NPC ethic as a lever — it currently isn't one in the built/spec'd system. |
| **Numeric tuning — AP curve** | AP economy (`AP = 2 + facility_tier (+1 Seat/Cathedral)` per the reconciliation addendum; README's worked example uses `AP=3, FacilityTier 1`) is unvalidated pending the §9 sim sweep — no seeded-play data confirms the curve produces the intended pace of player action per season. | Flagged in README "Still open"; not independently severity-tagged | **Yes, conditionally.** Any Tier proposal that assumes a specific AP throughput (verbs-per-season budget) is building on an unvalidated number. |
| **Numeric tuning — Π band** | The Π homeostat's target band (settles toward ~2–4 in the worked example) has the CG-1 bidirectional-restoring-term fix applied, but the band width/target itself is still pending the §9 sim sweep — i.e., the *direction* of the fix is verified, the *tuning* is not. | Flagged in README "Still open" | **Yes, conditionally.** Directly relevant to any proposal reasoning about pressure-driven pacing or "dramatic band" claims — the mechanism is sound (per Register-3-adjacent corroboration below) but the numbers are not validated. |
| **Numeric tuning — suspicion→recall threshold** | The Konrad suspicion track that feeds the G606 recall card has directional fixes (cap +1/season, Submit-to-audit escape) but the actual threshold at which recall triggers is still unvalidated pending the §9 sim sweep. | Flagged in README "Still open" | **Yes, conditionally.** Any proposal treating the recall/demotion cascade as a tuned, ready-to-ratify mechanism (see Register-3/reconciliation item C.2 below, §1.0d) should note the underlying threshold is still open even though the *architecture* is fixed. |

**Also still open per the verification findings' medium/low tables** (carried forward for completeness,
none currently gating a Tier proposal in this compendium):

- **deck-F6** — G401 riot's only no-cost Π-release is gated on a disposition threshold that can be
  locked out by a Grudge trigger; needs a widened gate or a Force-branch release. Medium.
- **CG-5b** — compact Ambition rows G602/G603/G604 need expansion to the full response schema (Π-delta +
  Ledger write) to satisfy the churn invariant uniformly. Medium.
- **sim-F7b** — Treasury draw location for Sponsor/relief actions needs explicit spec (delegation
  mechanism itself, `treasury_source`, is fixed). Medium.
- **sim-F8** — `social_contest(§7)` is a dangling reference in the build sequence and absent from the
  build; needs `social_contest_v30 §7` wired into `governance.py` as an added build step. Medium.
- **sim-F10** — build-order dependency: the deck engine (S4) needs the ambition runtime (S5/§6) for its
  forced-queue interface; needs the `deck_state['forced']` interface landed in S4 plus an anti-stall
  test. Medium.
- **F11 / F11b** — NPC boolean/relationship flags (`Wessel.informer-active`, `Hedda allied`) have no
  accessor; needs modeling as Leverage tags with derived booleans. Medium/Low.
- **F12 / F12b** — `succeed_governor` (succession survival) isn't in the build/file list and TTL
  durability across succession is untested. Medium/Low.
- **deck-F7** — G201 (War-Levy) has no cooldown; a permanent-war Crown could spam it and starve the
  Opportunity family (G301). Needs a cooldown or one-Extract-per-N cap. Low.
- **Thread family is thin** — only 2 cards exist across all 7 families' 28-card deck; flagged as still
  open in the README, not severity-tagged in the findings table.

---

## Register 2 — 2026-06-22 baseline territory/settlement audit: open gaps

Source: `designs/audit/2026-06-22-territory-settlement-audit/findings.md`. This audit's own confidence
tags are preserved: **[V]** verified directly against cited files, **[V-agent]** verified by a workflow
agent, **[R]** recovered from a finder run but not independently re-verified.

| Item | What it is | Severity (source) | Status | Blocks a Tier proposal here? |
|---|---|---|---|---|
| **G1 — no settlement registry** | `settlement.py` originally mapped territory→settlement 1:1, so the §1.3 multi-settlement province floor-average aggregation could never fire (always averaged one synthetic settlement). | Gap (unscored severity tier, listed under "GAPS") | **✅ CLOSED.** `sim/territory/registry.py` (`Settlement` dataclass) + `ledger.py` landed on the Goldenfurt branch, S0–S1, with `tests/sim/territory_registry/test_registry_ledger.py` (6 passing tests including 3-settlement aggregation). Confirmed closed by the 2026-07-12 reconciliation addendum. | No — this was the compendium's biggest inherited unknown and it is now resolved; safe to build on `registry.py`. |
| **G2 — church infrastructure keyed per-territory, not per-settlement** | `infrastructure.py`'s ASSUMPTION block stores church-infrastructure state by `territory_id`, but §1.5 specifies "per settlement" (including the −4 seizure cap, which is also specified per-settlement). Silently coarsened to province granularity. | Gap | **Open.** Not addressed by the Goldenfurt S0–S1 build or the reconciliation addendum. | **Potentially.** Any proposal reasoning about per-settlement church infrastructure/seizure state (distinct from province-level aggregates) is currently working against code that only tracks it at province granularity. Flag before ratifying settlement-level church-infra mechanics as implementation-ready. |
| **G3 — unused generation constants** | `infrastructure.py` defines `PT_GAIN_*`, `CI_GAIN_TEMPLAR`, `ORDER_GAIN_*` per §1.5/§1.6, but no entry point applies them — only `build`/`count`/`seizure_ob_modifier` are wired. The per-season PT/CI/Order generation these constants describe is not implemented. | Gap | **Open.** | **Yes, conditionally.** Any proposal assuming per-season passive generation of PT/CI/Order from church infrastructure is describing unimplemented behavior — the constants exist but nothing calls them. |
| **H3 — "Village" settlement type used but undefined** | `settlement_layer §2.1` assigns type `Village` to ~18 spoke settlements, but the §1.2 Settlement Types table defines only 8 types (Seat/City/Town/Fortress/Port/Cathedral/Mine/Outpost) — no Village row, and it's also absent from §1.4.1 (facility slots) and §4.5 (local-actor counts). These 18 settlements have no defined facility slots, stats column, or local-actor counts. | High | **Open.** Not touched by the Goldenfurt work (Goldenfurt/S-006 is a Town, not a Village). Independently re-confirmed and sharpened by the 500-seed stress test (Register 3, item F1) as part of a broader type-taxonomy — Village/Fortress-City/Cathedral-City are 3 of 11 real registry types against only 8 canonical ones. | **Yes.** Any proposal that touches settlement typing, facility slots, or local-actor counts for a Village-typed settlement is building on an undefined type. This is the single most cross-confirmed open item across all four source documents (baseline audit H3 + 500-seed F1). |

**Other baseline-audit items not re-litigated here** (H1 adjacency T16 gap, H2 stale 36-scheme geography
YAML, M1–M7, L1–L3, Q1–Q2): these are territory/geography-layer defects orthogonal to the governance
proposals under consolidation and are not repeated in this register; see the source findings doc directly
if territory geography becomes in-scope for a future pass.

---

## Register 3 — `settlement_mgmt_stress_01` (500-seed executable stress test): open items

Source: `designs/audit/2026-07-12-settlement-season-stress-sim/reconciliation_with_existing_territory_work.md`,
which reconciles the stress test's own kernel-derived findings against the three other bodies of work.
The stress test itself is `tests/sim/settlement_mgmt_stress_01/` — 500 seeds × 120 seasons, 13 modules,
403 tests, a 24-probe NERS grid.

| Item | What it is | Severity (source) | Blocks a Tier proposal here? |
|---|---|---|---|
| **F1 — type-taxonomy drift (structural root)** | The canonical §1.2 table defines 8 settlement types (Seat/City/Town/Fortress/Port/Cathedral/Mine/Outpost); the §2.1 registry's real type set is 11, adding **Village**, **Fortress-City**, and **Cathedral-City**. Flagged by the reconciliation addendum as "the structural root of 7 [stress-test] findings" — downstream modules hit fallback logic whenever they encounter the three undeclared types. Cross-confirmed against baseline-audit H3 (Village specifically). | Root cause / structural (drives 7 dependent findings) | **Yes.** This is the highest-leverage open item in the entire register: it is independently found by two different methodologies (hand-audit and 500-seed batch) and is a precondition for any proposal that types settlements, assigns facility slots, or branches logic on settlement type. Fix once (extend §1.2/§1.4.1/§4.5 to cover all 11 real types, or retype the extras), and 7+ downstream findings collapse. |
| **F6 — S-ID blocker** | An S-ID-related blocker in the 500-seed harness (the reconciliation addendum does not fully unpack F6's mechanics beyond naming it as a blocking item; it sits alongside F1 in the "structural root" cluster of findings the type-taxonomy drift produces). | Not independently re-scored in the addendum; grouped with F1's dependent findings | **Possibly.** Flagged here as open and unresolved; anyone relying on settlement-ID stability across the 500-seed harness or porting its seeds should check F6 directly in `tests/sim/settlement_mgmt_stress_01/` before assuming clean S-ID handling. Not confirmed to block any specific Tier proposal in this compendium, but not clearable without direct inspection either. |
| **24 NERS probes — specified but never executed** | The stress test's harness defines a 24-probe NERS (presumably Needs/Ethic/Resolution/State or equivalent — grid name as given in source) stress grid, but per the reconciliation addendum's framing of the stress test as a specified-and-run harness, these 24 probes are called out as specified in the harness design but **never executed** as part of the reported 500-seed/403-test run. | Not severity-tagged in source; listed as an execution gap | **Yes, conditionally.** The reconciliation addendum's confirmed NERS **MERGE** verdict on §1.0d (Performance Audit → recall unification, see below) is treated as validated in the addendum's narrative, but if that verdict rests on the specified-not-executed probe set rather than an actually-run probe, its confidence should be downgraded from "confirmed" to "designed but unvalidated" pending a real execution pass. Flag before treating any NERS-sourced verdict in this compendium as empirically settled. |

**Reconciliation-addendum items that sharpen but don't newly open work** (context, not separate open
items): the addendum also confirms the death-spiral / negative-bias finding as independently corroborated
by both methodologies (Register 1's Π-restore fix + this stress test's 500-seed batch — see addendum §B.1);
confirms the territory-governor AP-economy gap as consistent with baseline-audit G1 (closed, see Register
2); and surfaces two genuinely new cross-cutting reconciliation items not on any prior register — **(1)
Ledger-family divergence**: the built `ledger.py` `TAG_KINDS` set is `{Precedent, Grudge, Debt,
Reputation, Leverage}`, but a separate proposal (addendum's "PR#119 §1.3a") introduces `Compact` as a
purported "5th family" when Leverage already occupies that slot — unreconciled, and per the addendum "must
be reconciled before §1.3a ratifies"; and **(2) §1.0d Performance Audit likely duplicates Goldenfurt's
already-designed G606 recall** — a second accountability cascade competing with the existing
suspicion→recall mechanism rather than merging onto it. Both are flagged by the addendum as the
highest-value **new** findings from this cross-reading and should be treated as live blockers on any
Tier proposal in this compendium that touches ledger-tag families or the recall/accountability cascade,
independent of the registers above.

---

## Cross-cutting caution for this compendium

The 2026-07-12 reconciliation addendum exists *because* a prior stress-test pass re-derived roughly a
third of its findings from scratch without reading the Goldenfurt slice or the baseline audit first. This
tier is written specifically to prevent that recurrence within this compendium: before ratifying any
Tier 1–3 proposal that touches settlement typing, ledger-tag families, the Π/pressure homeostat, the
suspicion/recall cascade, or church infrastructure, cross-check it against the open items above — several
of them (type-taxonomy drift, Compact-vs-Leverage, §1.0d-vs-G606) are not yet resolved anywhere in the
corpus and would silently re-open if a Tier proposal here assumes them settled.
