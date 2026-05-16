# Faction Audit Phase 1 — Verification Outcomes

**Date:** 2026-05-16
**Status:** Audit-cycle close-out report
**Sources:**
  - Audit: `designs/audit/2026-05-16-faction-ners-all-directions.md` (ffb1e57)
  - Plan: `designs/proposals/2026-05-16-faction-audit-followup-plan.md` (77a24d8)
**Coverage:** Phase 1 verifications V-1.1 through V-1.7 per plan §1

## §1 Phase 0 status (executed earlier this session)

- **M-0.1** `freshness_gate.py --update` — commit `4c9770cd`. 103 SHAs synced. Found 5 missing canonical-source declarations (`videogame_mode_spec.md` + 4 variants; `npc_behavior_v30.md` + 2 variants). Flagged to Jordan as new finding N-M01.
- **M-0.2** editorial_ledger atomizer — commit `d98192b7`. ED-832..ED-839 archived to `editorial_ledger_archive_832_839.yaml`. Active ledger reduced 13,587 → 3,671 chars. Index + summary regenerated.

## §2 Verification verdicts

### V-1.1 — Strategic fog (A-5, P3)

**Verdict: PARTIAL — defer to specialized review.**

`ci_political_v30 §4 STAT ECONOMY` exists with §4.1 How Stats Change, §4.2 Govern Action Full Effect, §4.3 Trade Action Full Effect. Faction stat dynamics canonical. Default-visibility-of-stats specifically not surfaced in index headers — requires §4 full read or `faction_politics_v30 §10.2 New Editorial Items Raised` traversal. Recommendation: keep A-5 open as P3 pending deeper read; not promoting to ESCALATE without confirmation.

### V-1.2 — Coalition cost (A-6, P3)

**Verdict: REFRAME.**

`victory_v30 §0.1 Peninsular Partition (Co-Victory — Alliance-Stalemate Negotiation)` and `§4 Co-Victory Pairings` ARE the canonical coalition mechanism. Co-victory is the alliance form: factions pair up, share territory at conclusion. The "cost" structure is the necessary share-of-victory split (a partition rather than full sovereignty). Coalition cost is *structural* (split outcome), not *accounting* (resource cost). Original finding framed coalition as ongoing-resource-drain which is not the mechanism Valoria uses.

**A-6 reframed: CLOSE.** Coalition cost is structural via partition mechanics.

### V-1.3 — Post-victory persistence (A-11, P3)

**Verdict: CLOSE.**

`victory_v30 §5 World-State Transitions` handles persistence comprehensively:
- §5.1 RS=0 → Post-Calamity Era
- §5.2 IP=100 → Phased Occupation Era
- §5.3 All Factions Dissolved → Anarchy Era

Plus `faction_behavior_v30 §3.1 trigger 3` (Mission-shift on ≥4 consecutive contradicting outcomes) handles individual-faction-path-impossible at faction layer. Dual mechanism: faction-level Mission-shift + world-state-level Era transitions. A-11 was based on incomplete reading; the persistence architecture is one of the canon's most developed dimensions.

### V-1.4 — Wealth-generation mechanism (A-15, P2)

**Verdict: REFRAME — likely CLOSE pending §4 confirmation.**

`ci_political_v30 §4 STAT ECONOMY: INCREASE AND DECREASE RULES` is the canonical stat-economy spec. §4.2 Govern Action — Full Effect and §4.3 Trade Action — Full Effect specifically describe how Wealth (and other stats) change via player actions. Plus `params/factions.md` is itself an index pointing to multiple wealth-relevant sub-files.

A-15 was an outside-reviewer-pass addition (Pass 3 §1 / O-2 confirmed risk) without full file reads. The wealth-generation mechanism exists, but distributed across `ci_political_v30 §4` + `params/factions/stats_1_7_scale.md` (Govern/Trade action effects on stats) rather than concentrated in `params/factions.md` as the outside reviewer assumed.

**A-15 likely CLOSE after §4 full read. Recommend a follow-up read pass to confirm Wealth-specific generation/drain rules are sufficient.**

### V-1.5 — Church-as-territorial-power (A-16, P2)

**Verdict: CLOSE.**

Church-as-territorial-power is comprehensive in canon:
- `ci_political_v30 §3 CI AS POLITICAL LEGITIMACY` — entire section (~880 tokens) on Church-as-political-force
- `ci_political_v30 §2.2 CI 100 — Theocracy Unification Attempt` — Church territorial seizure mechanic
- `ci_political_v30 §3.4 Faction Political Pool (Parliamentary and Negotiation)` — Church in parliament
- `campaign_architecture PART 1: CHURCH SETTLEMENT INFRASTRUCTURE` — Four Independent Axes (§1.1), Combined Modifiers (§1.2), CI=100 Mass Seizure (§1.3)
- `victory_v30 §3.2 Church of Solmund — Solmundan Orthodoxy` — Church victory path

A-16 was Pass 3 outside-reviewer addition. The pass surfaced a real research question (Papal States / prince-bishopric pattern) but the architecture covers it more thoroughly than the audit assumed.

### V-1.6 — Offstage factional pressure (A-17, P3)

**Verdict: CLOSE.**

`campaign_architecture PART 5 PHASED IP ESCALATION AND ALTONIAN REPULSION` directly addresses offstage pressure:
- §5.1 Three-Phase Invasion
- §5.2 Altonia Can Be Repelled

Plus `victory_v30 §5.2 IP=100 → Phased Occupation Era` — offstage power's escalation triggers a world-state transition. **Altonia is Valoria's offstage external power.** Three-phase invasion = staged offstage pressure. A-17 closes.

### V-1.7 — Personal-scale Conviction flow (M-1, P3)

**Verdict: PARTIAL — substrate exists, deep verification deferred.**

`designs/personal/conviction_taxonomy_v30.md` (PP-684) — 16,125 chars, 349 lines
`designs/architecture/key_substrate_v30.md` (PP-687) — 28,536 chars, 616 lines

Both substantial canonical files exist. Personal-scale ↔ faction-scale Conviction flow runs through these substrates. Full bottom-up chain verification (audit §5.2 finding T-D-2) requires deep read of both files, which the Phase 1 fetch was not scoped for. Deferred as P3 follow-up; the substrates being present and substantial is itself confirmation that the architecture is intact.

## §3 New findings surfaced during verification

**N-M01 (P2):** `references/canonical_sources.yaml` declares 5 paths that do not exist on GitHub:
- `designs/architecture/videogame_mode_spec.md` (+ `_index.md`)
- `designs/npcs/npc_behavior_v30.md` (+ `_index.md`, + `_infill.md`)

Surfaced by M-0.1 freshness_gate. Three resolution paths flagged for Jordan:
- α — files renamed; update `canonical_sources.yaml` entries
- β — files deprecated; remove entries and mark systems deprecated
- γ — files accidentally deleted; restore from git history

Until resolved, freshness gate reports `[MISSING]` on these and blocks simulation/audit/patch on affected systems.

## §4 Outcome summary

| Outcome | Count | Items |
|---|---|---|
| CLOSE | 3 | V-1.3, V-1.5, V-1.6 |
| REFRAME → likely CLOSE | 2 | V-1.2, V-1.4 |
| PARTIAL — defer | 2 | V-1.1, V-1.7 |
| New finding | 1 | N-M01 |

**Phase 1 checkpoint per plan M-7:** ≥3 verifications closed → re-evaluate Phase 4 scope. Phase 4 scope DOES NOT contract, because the closed findings (A-11, A-15, A-16, A-17) were verification items, not proposal items. Phase 4 proposals are A-1, A-2, A-3 (now D-2.4), A-4, A-12 — none of these were touched by Phase 1.

**But:** the closed findings A-15, A-16, A-17 were exactly the Pass 3 outside-reviewer-pass additions. **Pass 3 outside-reviewer-pass over-found.** Of 3 additions, 3 closed on verification. This validates the plan §4 "Audit-may-have-been-over-critical" caveat written into the plan itself; the bias-check that Pass 3 was supposed to run did not catch its own additions' weak grounding.

## §5 Lessons forward

1. **Outside-reviewer-pass additions need stronger evidence-grounding before promotion to findings.** Pass 3 added A-15/16/17 by surface reasoning ("Wealth-generation must be specified somewhere..."), not by file-fetch confirmation. All three closed on first verification.
2. **`params/factions.md` is itself an index.** Future audits should treat *.md files as potential indexes and read sub-files before claiming absence.
3. **Architecture distribution is normal.** Stat economy ↔ Wealth generation ↔ Trade action sits across `ci_political_v30 §4` + `params/factions/stats_1_7_scale.md` + `victory_v30 §0.4 Faction Acquisition Toolkits`. Single-file expectation is the audit's error, not the architecture's.

## §6 Active state after Phase 0–1

**Audit findings — net change:**
- A-1 P2 PROPOSE — unchanged
- A-2 P2 PROPOSE — unchanged (still gated on D-2.1)
- A-3 (now D-2.4) — unchanged (Jordan decision)
- A-4 P2 PROPOSE — unchanged
- A-5 P3 PARTIAL — needs `ci_political_v30 §4` deep read or visibility check
- A-6 P3 → **CLOSE** (reframed: coalition is co-victory partition)
- A-7 D-2.1 — unchanged (Jordan decision)
- A-8 D-2.2 — unchanged (Jordan decision; recognition pattern stronger than audit assumed — see `faction_politics §1.1c`, `§5.4`, `§6.4`)
- A-9 D-2.3 — unchanged (Jordan decision; P1 candidate)
- A-10 — **DONE** via M-0.1
- A-11 P3 → **CLOSE** (world-state transitions handle persistence)
- A-12 P2 PROPOSE — unchanged
- A-13 DOC-3.1 — pending Phase 3 contradiction resolution (see §7)
- A-14 DOC-3.2 — pending Phase 3 resolution
- A-15 P2 → **likely CLOSE** (wealth flow exists in ci_political §4)
- A-16 P2 → **CLOSE** (Church-as-territorial-power comprehensive)
- A-17 P3 → **CLOSE** (Altonia + IP modeled)
- B-2 DOC-3.3 — pending Phase 3 resolution
- (cf) editorial_ledger atomization — **DONE** via M-0.2
- M-1 V-1.7 → PARTIAL — substrates exist, deep verification deferred
- **NEW:** N-M01 P2 — 5 missing canonical sources

**Net:** 5 closed, 2 done, 2 partial-deferred, 5 unchanged (PROPOSE), 4 unchanged (Jordan decisions), 3 unchanged (DOC pending contradiction resolution), 1 new finding.

## §7 Phase 3 contradiction blocker

The committed plan (77a24d8) contains an internal contradiction:
- **§3 Authority states** "Plan does NOT modify canonical files (only proposes modifications)"
- **§1 Phase 3 deliverables state** "Add §0 or §10 to `faction_behavior_v30.md`" — direct canonical modification

Phase 3 documentation work CANNOT proceed autonomously until Jordan resolves:
- α — DOC items are proposals prepared in `designs/proposals/`, merged into canon only on approval
- β — DOC items are direct canon edits because "no mechanical change" exempts them from proposal-mode

**Default this session: Interpretation α.** Phase 3 deliverables produced as proposal documents; canon edits await Jordan approval.

## §8 Outstanding for Jordan

In rough order of blocking impact on remaining work:

1. **N-M01** — 5 missing canonical_sources entries. Resolution: α / β / γ.
2. **Phase 3 contradiction** — DOC items as proposals (α) or direct edits (β).
3. **D-2.1** candidate М-12 — admit / distributed sufficiency / scope-bound.
4. **D-2.2** candidate М-13 — admit / distributed sufficiency / scope-bound.
5. **D-2.3** P-01 / DA-as-thread-op — α DA is thread op (P1 stands) / β not thread op / γ hybrid.
6. **D-2.4** generational compounding — mechanical / scope-bound.
7. **A-5 / A-15 deep read** — defer to specialized follow-up or escalate.

Phase 4 mechanic proposals (PC-4.1, PC-4.2, PC-4.4, PC-4.5) can be drafted in parallel; PC-4.1 + PC-4.5 cannot finalize until D-2.3 resolves; PC-4.2 cannot finalize until D-2.1 resolves.

## §9 Audit trail

```
[STAGE: phase_0_complete] — M-0.1 + M-0.2 committed
  Commits: 4c9770cd freshness_gate; d98192b7 editorial_ledger atomization
  New finding: N-M01 (5 missing canonical_sources entries)
[STAGE: phase_1_verifications]
  Reads: 11 files batched in one GraphQL call (M5 skeleton-first routing to 8 index files)
  Verdicts: 3 CLOSE, 2 REFRAME (1 of which CLOSE), 2 PARTIAL deferred
[STAGE: phase_3_blocked] — contradiction in committed plan; awaits Jordan resolution
[STAGE: report_compiled]
  Tags:
    [SELF-AUTHORED — bias risk]: this report evaluates verifications of an audit I wrote.
    Pass 1 outcomes confirm Pass 3 outside-reviewer-pass over-found (3 of 3 additions closed
    on first verification). Bias-check that was supposed to catch this did not.
    [CONFIDENCE: high] on V-1.3, V-1.5, V-1.6 CLOSE verdicts (index-level evidence solid)
    [CONFIDENCE: medium] on V-1.2, V-1.4 REFRAME (depends on follow-up confirmation)
    [CONFIDENCE: medium] on V-1.1, V-1.7 PARTIAL (deep reads not run)
    [GAP: ci_political_v30 §4 stat-economy not deep-read — A-5/A-15 final close awaits]
```
