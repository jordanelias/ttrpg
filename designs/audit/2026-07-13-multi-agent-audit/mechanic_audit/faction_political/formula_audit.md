# Mode A — Formula Validation: Faction / Political

**Subsystem:** faction_political (lane: FA)
**Target docs (working-tree, superseding any stale `canonical_sources.yaml` pin):**
`designs/provincial/faction_canon_v30.md`, `faction_layer_v30.md`, `faction_behavior_v30.md`,
`faction_state_authoring_v30.md`, `faction_politics_v30.md` + `params/factions.md` +
`params/factions/stats_1_7_scale.md`.

Currency check: `CURRENT.md` line 75 ("Faction / political" row) confirms these five design docs
as the live head, cross-checked against `references/canonical_sources.yaml` `faction_canon_consolidation`
/ `faction_layer` / `faction_behavior` / `faction_state_authoring` / `faction_politics` entries
(2026-05-07/05-01/04-17 vintages) and `canon/02_canon_constraints.md` P-01–P-15 / GD-1–GD-3.

| ID | Formula | Min Output | Max Output | Issues | Status |
|---|---|---|---|---|---|
| FA-F-01 | Mandate: `clamp(round(7·T/(T+K)),0,7)`, `T=Σ_s W_s·(0.5L_s+0.5PS_s)/7`, `K=6` (`faction_canon_v30.md` §5.1; `faction_behavior_v30.md` §4) | T=0 → Mandate=0 | T→∞ → Mandate→7 (asymptotic, correctly clamped) | K is a fixed constant (6), never 0 → no div-by-zero. T is a **sum**, not a mean, over controlled settlements, so it grows with settlement count as intended (saturating curve). No negative-pool or boundary defect found. | PASS |
| FA-F-02 | Domain Action resolver: `P_success=clamp(0.50+0.10M,0.05,0.90)`, `P_overwhelming=clamp(0.50+0.10M−0.35,0,0.55)`, `P_atleast_partial=clamp(0.50+0.10M+0.20,P_success,0.97)` (`params/factions/stats_1_7_scale.md` §Domain Action Resolution) | M=−10: Overwhelming 0%, Success 5%, Partial 0%, Failure 95% | M=+10: Overwhelming 55%, Success 35%, Partial 7%, Failure 3% | Verified band ordering (`P_overwhelming ≤ P_success ≤ P_atleast_partial`) holds across the tested M range; the dynamic lower-clamp on `P_atleast_partial` (`P_success`) correctly zeroes the Partial band at extreme mismatches rather than going negative. This formula is explicitly Stage-1/4/5 sim-tested and ratified (ED-874, 2026-05-31) — re-derivation here confirms no residual defect. | PASS |
| **FA-F-03** | **Ob_modifier (Domain Action Ob calc):** `Ob_modifier = mission_alignment_modifier + cascade_alignment_modifier + expectation_alignment_modifier`, clamped ±2 (`faction_behavior_v30.md` §3.7) | — | — | **Two of the three summands are not computable as written.** (1) `cascade_alignment_modifier(da, faction.aggregate_effective_convictions)` is invoked with a signature and an inline comment (`# -1, 0, +1`) but **no formula is given anywhere in the document** — unlike `mission_alignment_modifier`, which has full pseudocode. (2) `expectation_alignment_modifier(da, faction) = sign(da.cascade_alignment_with_role) × strictness(faction) × {1, 2}` — the `× {1, 2}` term is not a formula, it is a set literal with no rule for selecting 1 vs 2. The trailing comment ("+1 if action is ±1 from role expectation, +2 if ±2 deviation") implies a **deviation-magnitude variable that the formula never defines or reads** — `sign()` collapses `da.cascade_alignment_with_role` to {−1,0,+1}, discarding exactly the magnitude information the comment says should select the multiplier. Since §3.7 governs the Ob (difficulty) of **every Domain Action for every faction**, this is a canonical, universally-invoked formula that cannot be mechanically executed by an implementer as literally written for two of its three terms. | **FAIL — see finding FA-A-01 below** |
| FA-F-04 | Cascade blending: `effective_convictions(npc) = α·personal_convictions(npc) + (1−α)·effective_convictions(supervisor(npc))`, `α = clamp(α_base + α_seniority(standing) + α_institution, 0, 1)` (`faction_behavior_v30.md` §3.2.3) | α at Standing 1, Hafenmark (−0.2 inst): `0.4−0.2−0.2=0.0` | α at Standing 7, Restoration (+0.1 inst, capped table shows +0.2 max used): `0.4+0.4+0.2=1.0` | Boundary values land exactly on the stated `[0,1]` clamp range at the documented Standing 1/7 extremes — no violation. **Edge case:** `α_seniority` is only specified "Standing 1: −0.2; Standing 7: +0.4 (linear)" — the rank ladders (`faction_politics_v30.md` §1.0) explicitly include **Standing 0** (Petitioner/Stranger/Catechumen/Squire, pre-initiation). Linear extrapolation to Standing 0 gives `α_seniority(0) = −0.3`, which **falls outside the documented "−0.2 to +0.4" range** for `α_seniority` and could push `α` below the intended floor if a Standing-0 NPC is ever plugged into a cascade graph. Likely non-triggering in practice (Standing-0 NPCs are pre-initiation and presumably outside `organizational_hierarchy.nodes`), but this exclusion is never stated. | PASS (with edge-case note, folded into gap register as P3 — no NPC data structure explicitly excludes Standing 0 from cascade participation) |
| FA-F-05 | Public Expectation Strictness: `strictness = clamp(0.4 + 0.5·(agg_L/7) − 0.3·(agg_PS/7), 0, 1)` (`faction_behavior_v30.md` §3.6) vs. the illustrative table immediately below it | high-L/high-PS (7,7) computes 0.6 | high-L/low-PS (7,0) computes 0.9; low-L/high-PS (0,7) computes 0.1; low-L/low-PS (0,0) computes 0.4 | **Formula and table disagree on 3 of 4 rows.** Table states: high/high=0.4, high/low=0.7, low/high=0.2, low/low=0.4. Recomputing the formula at the natural 0–7 extremes gives 0.6, 0.9, 0.1, 0.4 respectively — only the low/low cell matches. No choice of "high"/"low" as intermediate values (tested 5/2) reconciles the mismatch either. The table reads as a stale hand-worked illustration from an earlier coefficient set that was not regenerated when `base_strictness=0.4`/`0.5`/`0.3` were finalized. | **FAIL — see finding FA-A-02 below** |
| FA-F-06 | ΔLegitimacy: `+λ_continuity·seasons_in_role_uninterrupted + λ_procedural·procedural_event_score − λ_violation·violation_event_score`, `λ_continuity=0.05` (`faction_behavior_v30.md` §3.5) | seasons=0 → term=0 | seasons=20 (realistic late-campaign tenure per `victory_v30`-cited S14–S20 pacing) → continuity term alone = **+1.0/season**, unbounded and growing linearly thereafter | `seasons_in_role_uninterrupted` has **no stated cap**, unlike every other per-season delta term in this corpus (Stability's explicit `FACTION_STAT_SEASONAL_CAP=±2`, faction stats' `±2/season` cap in `stats_1_7_scale.md`). At realistic late-campaign tenure the continuity term becomes comparable to or larger than the maximum plausible `λ_violation·violation_event_score` term (≈0.6×1–3 ≈ 0.6–1.8), meaning a long-uninterrupted leader trends toward legitimacy near-immunity from violations — undercutting the explicit design promise in `faction_layer_v30.md` §5.6b ("Parliament is a legitimacy weapon: sustained institutional pressure degrades governance"). No hard range violation (L is clamped 0–7 elsewhere), so this is a balance/degenerate-tendency finding, not a crash-class defect. | PARTIAL (balance risk, not a hard formula break) — see finding FA-A-03 |
| FA-F-07 | Royal Decree escalation: faction_canon_v30.md §9/Crown sheet ("+1 Ob/season consecutive") vs. `params/factions/stats_1_7_scale.md` ("difficulty +2/season (legacy +1 Ob)") | — | — | Both describe the **same mechanic** (Crown's Royal Decree consecutive-use fatigue) but in **different, non-interchangeable units** post-ED-874 resolver migration (2026-05-31). `stats_1_7_scale.md` correctly translates the legacy "+1 Ob" into the resolver's native "+2 difficulty" (per the resolver's own stated `D=max(1,(O−1)·2)` legacy mapping). `faction_canon_v30.md` (dated 2026-05-07, predates the 2026-05-31 resolver ratification) was never swept and still reads literally as "+1 Ob/season" — an implementer following faction_canon alone would apply half the intended escalation. Mitigated: faction_canon's own header explicitly subordinates itself ("Source files remain canonical until ratification commits"), and `stats_1_7_scale.md` is the correct/authoritative source, so this is a propagation-lag ambiguity rather than a dual-canon conflict. | PARTIAL (documentation propagation lag) — see finding FA-A-04 |
| FA-F-08 | Casus Belli expiry timer: `faction_layer_v30.md` §3.5 body ("CB is consumed upon first use or **after 1 season of non-use** (expires)") vs. `faction_layer_v30.md` §10 open-items table, `ED-NEW-001` ("Casus Belli: consumes on use vs expires after 1 season. **RESOLVED** — consumes on use. **Auto-expires after 3 seasons if unused.**") | — | — | **Direct in-file contradiction on a concrete state-machine timer.** §3.5 states the CB unused-expiry window is 1 season; §10's own resolution table — whose stated purpose is to settle exactly this question ("expires after 1 season" is the literal alternative posed and rejected in the same cell) — answers with 3 seasons. Both passages are written as settled canon, not as open questions, so there is no textual signal for which value an implementer should encode. This governs the Casus Belli mechanic used across §3.5 (treaty breach), §5.4 (Outlawry "CB granted to all"), and cross-referenced by `faction_layer_v30.md §4.1` Varfell's diplomatic bonus row — a widely-consumed identifier. | **FAIL — see finding FA-A-06 below** |
| FA-F-09 | Institutional Mandate gates: `Faction L ≥ 4` (`params/factions/stats_1_7_scale.md` §"Institutional Mandate Trigger" and §"Institutional Mandate — Uphold / Appease", PP-189/ED-003) | — | — | References a bare faction-level **L** (Legitimacy) stat. Per the LPS-1→LPS-2e ruling (Jordan, 2026-05-30) propagated through `faction_canon_v30.md` §5.1/§5.3, `faction_behavior_v30.md` §2/§3.4/§3.5/§4, and `stats_1_7_scale.md`'s own §"Mandate Recovery" section (which *was* swept — "REVISED by LPS-2e... per controlled SETTLEMENT"), **Legitimacy no longer exists as a faction-level scalar** — only per-settlement L (settlement_layer §1.8) and the aggregate Mandate stat exist at faction scale. These two PP-189/ED-003 blocks were not swept in the same pass (both still carry their pre-LPS `[PROVISIONAL]` tag, unlike the neighboring Mandate-Recovery section a few dozen lines below in the same file, which explicitly documents its own LPS-2e revision). No definition remains of what "Faction L ≥ 4" should now resolve against (aggregate_Legitimacy? Mandate? a specific settlement?). | **FAIL — see finding FA-A-07 below** |

---

## Findings (Mode A)

### FA-A-01 — `Ob_modifier` (§3.7) has two non-computable summands [P1]
**File/section:** `designs/provincial/faction_behavior_v30.md` §3.7 (Domain Action Ob Calculation).
`cascade_alignment_modifier` is invoked but never defined anywhere in the corpus (no formula, no
pseudocode — only an inline `# -1, 0, +1` range comment). `expectation_alignment_modifier`'s formula
multiplies by a bare set literal `{1, 2}` with no rule for which value applies; the accompanying
comment implies a deviation-magnitude input that the pseudocode discards via `sign()`. Since
`Ob_modifier` governs the difficulty of **every faction Domain Action for every faction** (the
canonical resolver path per `stats_1_7_scale.md` §Domain Action Resolution), this is a load-bearing,
universally-invoked calculation that cannot be executed deterministically as written.
**Disposition: PROPOSED-ED, lane=FA.** (Not GO/IN — this is a design-completeness gap in a live
canonical mechanics doc, not an implementation-pipeline issue.)

### FA-A-02 — Public Expectation Strictness table contradicts its own formula [P2]
**File/section:** `designs/provincial/faction_behavior_v30.md` §3.6. The formula and the illustrative
4-row table beneath it diverge by 0.1–0.2 on 3 of 4 rows (see FA-F-05 above). The formula is fully
computable and bounded (no crash-class defect); this is a stale-table/documentation-only mismatch.
**Disposition: no action — flag for a routine documentation-fix pass** (regenerate the table from the
formula, or vice versa, at the next editorial sweep of this doc). Not filed as a new ED; below the
P1 bar since the formula itself is complete and executable.

### FA-A-03 — ΔLegitimacy continuity term has no seasonal cap [P2]
**File/section:** `designs/provincial/faction_behavior_v30.md` §3.5. `seasons_in_role_uninterrupted`
accumulates without bound, unlike every sibling per-season delta mechanism in this subsystem (all of
which carry an explicit `±2/season` or similar cap). At realistic late-campaign tenure this term can
rival or dominate the violation-erosion term, softening the "sustained pressure erodes legitimacy"
guarantee asserted in `faction_layer_v30.md` §5.6b. No hard range violation; a tuning/balance risk,
not a crash.
**Disposition: no action — flag for the next Stage-10-style calibration pass** (recommend capping the
term, e.g. `λ_continuity · min(seasons_in_role_uninterrupted, N)`). Not filed as a new ED.

### FA-A-04 — Royal Decree fatigue units stale in faction_canon vs. the ratified resolver [P2]
**File/section:** `designs/provincial/faction_canon_v30.md` §9 + Crown sheet body (~line 464) vs.
`params/factions/stats_1_7_scale.md` §Unique Actions — All Factions. Same mechanic, incompatible
units (raw "Ob" vs. resolver "difficulty") because faction_canon predates the 2026-05-31 ED-874
resolver ratification and was not swept. `stats_1_7_scale.md` is the correct, authoritative version;
faction_canon self-declares subordinate/provisional status ("Source files remain canonical until
ratification commits"), which limits practical risk.
**Disposition: no action — flag for the next propagation sweep of faction_canon_v30.md** against the
ED-874 resolver migration (the sweep already covered `faction_layer_v30.md` §0's audit-patch table
and `stats_1_7_scale.md` itself, per that table's `FACTION_RESOLVER_PROPAGATION` entry — faction_canon
was evidently missed). Not filed as a new ED; not P1 because the authoritative source is unambiguous
and locatable.

### FA-A-06 — Casus Belli unused-expiry timer contradicts itself (1 season vs 3 seasons) [P1]
**File/section:** `designs/provincial/faction_layer_v30.md` §3.5 body text vs. §10 `ED-NEW-001`
resolution-table entry, in the **same file**. §3.5 states CB "expires" after "1 season of non-use."
§10's own settled-answer table — posed as a direct 1-season-vs-alternative question — answers "Auto-expires
after 3 seasons if unused." Both read as finished canon (no "TBD"/"pending" marker on either), so there
is no in-doc tiebreak. This governs a concrete, engine-relevant timer consumed by treaty-breach CB
grants (§3.5), Outlawry's CB-to-all rider (§5.4), and Varfell's diplomatic-stratagem bonus (§4.1) — a
widely-referenced mechanical identifier, not a cosmetic value.
**Disposition: PROPOSED-ED, lane=FA.** Recommend Jordan pick one value and strike the other; §10's
table (being the explicit "RESOLVED" answer to the named open item) is the more likely intended source
of truth, but the body text at §3.5 is what a first-time reader encounters and currently states the
opposite value with no forward pointer to §10.

### FA-A-07 — "Institutional Mandate" (PP-189/ED-003) still gates on faction-level "L", which LPS-2e removed [P2]
**File/section:** `params/factions/stats_1_7_scale.md` §"Institutional Mandate Trigger" and
§"Institutional Mandate — Uphold / Appease" (both `[PROVISIONAL]`, ED-003/PP-189). Both still read
"Faction L ≥ 4" as their trigger condition. Per LPS-1→LPS-2e (2026-05-30 Jordan ruling), Legitimacy is
no longer a faction-level stat anywhere in this subsystem — it exists only per-settlement
(`settlement_layer_v30.md` §1.8) and as the derived faction **Mandate** aggregate. Every other
Mandate/L-touching passage in this same file was swept with an explicit `[REVISED by LPS-2e]` banner
(see e.g. the "Mandate Recovery" section immediately below §"Unique Actions") — these two were missed.
No definition remains of what value an implementer should read for "Faction L ≥ 4" post-migration.
**Disposition: PROPOSED-ED, lane=FA.** Downgraded from P1 to P2 because both blocks already carry a
pre-existing `[PROVISIONAL]` tag predating the LPS sweep, signalling lower confidence/priority even
before this drift, and neither is cross-referenced as a dependency by any of the other four target
docs (unlike Mandate, which is load-bearing everywhere) — so the blast radius is narrower than
FA-A-06's Casus Belli defect.

### FA-A-05 — α_seniority undefined at Standing 0 [P3]
**File/section:** `designs/provincial/faction_behavior_v30.md` §3.2.3 table. Linear extrapolation of
the stated "Standing 1: −0.2; Standing 7: +0.4" rule to Standing 0 (a real rank on the 0–7 ladder per
`faction_politics_v30.md` §1.0) yields −0.3, outside the documented `[−0.2, +0.2]`-ish window implied
by the table's own bounds. No evidence a Standing-0 NPC is ever plugged into a cascade graph
(pre-initiation ranks are unlikely `organizational_hierarchy.nodes` members), so this is a dormant
edge case.
**Disposition: no action — working as intended in practice; recommend an explicit "cascade applies to
Standing ≥ 1 only" note if this is ever formalized.** Not filed as a new ED.
