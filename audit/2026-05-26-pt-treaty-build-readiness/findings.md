# PT + Treaty Build Readiness Review

**Date:** 2026-05-26
**Status:** PROVISIONAL — pending Jordan ratification on the two open decisions in §4.
**Trigger:** Following the 2026-05-25 R6 death-spiral reconciliation audit (commit `82887dc`), session was directed to proceed with Treaty Expiration + Parliamentary Transfer build. Ground-up review (this document) re-scoped the work and surfaced blocking gaps before code beyond annotation cleanup (Pass A, commit `281debe`).
**Companion:** Pass A annotation cleanup landed in `281debe` (treaty.py, parliamentary_transfer.py, parliamentary_vote.py, coverage_matrix.md, module_manifest.md). Behavior-neutral.

## §1. Verdict

The original handoff framing — "two stubs need filling" — is incorrect. Both canon docs (`parliamentary_transfer_v30.md`, `treaty_expiration_v30.md`, CANONICAL Pass 2h 2026-05-17) exist and are clear. The sim does not. Roughly half the required substrate is missing or stubbed, and several canon provisions are not implementable against the current `Faction`/`World` schema without additions. This is a 4–6 commit coupled build, not 2. Implementing PT+Treaty alone will not reach the v12c-validated balance (24.7 / 28.6 / 24.2 / 22.5) because those numbers are a five-mechanic equilibrium; the other three mechanics (Einhir Revival, Altonian Reinforcements, RM PT-decay) are unbuilt. The build can still proceed honestly with a documented interim target, but Jordan must ratify the target before code beyond Pass A.

## §2. Findings

### §2.1 Severity 1 — blocking

**F1. `parliamentary_vote` and `parliamentary_stay` are stubs.** PT canon §4 routes resolution through a formal Parliamentary Vote contest with Stay (ED-631) handling. `sim/personal/parliamentary_vote.py` is a 2-function file where both functions raise `NotImplementedError`. `sim/personal/parliamentary_stay.py` is the same shape. Both depend on `sim/personal/contest.py` (exists, 10KB) and a `Motion` type that is imported by the stub headers but whose source was not confirmed in this review. PT cannot be implemented against canon without first building the vote contest engine, the Motion type, and Stay handling. This is a subsystem, not a function. Canon basis: `parliamentary_transfer_v30.md` §4; `social_contest_v30.md` §10 + §10.1.

**F2. CB (Casus Belli) economy has zero substrate.** PT §1 prerequisite is CB; §3 enumerates 8 CB sources; CB is pair-scoped with stacking and decrement semantics ("Multiple CB sources can stack on the same pair; consumption decrements one source per Parliamentary Transfer attempt"). `Faction` has no `cb` field. `World` has no CB registry. Repo-wide grep for `casus_belli|CB[^_a-zA-Z]|\.cb\b` returns only stub docstrings and one insurgency-pipeline match unrelated to faction CB. Every CB source is itself a hook into another system — adjacent-instability needs an arc-boundary Accord scan; Einhir Revival is "Pass 2d pending"; Treaty-violation needs the §3 violation handler; Conviction Scar needs `conviction_track`; Excommunication-CB needs Church-ally tracking that does not exist. Faithful CB economy touches 5+ other systems, several unbuilt. Canon basis: `parliamentary_transfer_v30.md` §3, §1.

### §2.2 Severity 2 — canon-vs-schema

**F3. Cross-faction Standing is unmodeled.** PT §4.3 computes voting blocs by "faction Standing relative to proposer + holder"; Treaty §3 violation specifies "Standing −2/+1" deltas. `Faction.standing` is a single scalar int (`game_state.py:98`), not pairwise. `crown_initiative.py` already flags this exact gap in its Coronation Renewal `OW` branch: "[PROVISIONAL] §3.4 OW 'Crown-Church Standing +1' not modeled (cross-faction Standing not in v18 schema)". Vote-bloc computation as canon-specifies cannot run without schema extension to `faction.standing_vs[other_faction]` (or equivalent).

**F4. Senator Outward is absent in `crown_initiative`.** Treaty canon §2 names Senator Outward as the canonical Crown re-binding action against the 90% lapse rate. `crown_initiative.py` has three modes only: `royal_progress`, `great_work`, `coronation_renewal`. There is no `senator_outward` function, no dispatch entry, no canon citation of `part10_crown_initiative_design §3.4 Mode III`. Without Senator Outward, implementing 90%/arc lapse means Crown treaties decay with no renewal path — Crown receives only the nerf, not the canon's compensating Wealth-and-action-slot investment loop. That breaks the v12c balance the doc itself documents (Treaty §5: "Sensitivity: `TREATY_LAPSE_RATE` +0.05 → Crown −1pp, distributed to others" assumes re-binding exists).

**F5. Treaty-violation auto-detection is absent.** Treaty §3 specifies that a treaty-bound faction attacking the other party voids the Treaty immediately and generates Standing/CB consequences. `_try_conquest` in `faction_action.py` (line 132) has no treaty awareness — it does not look up `world.treaties` for the attacker-defender pair, does not void on violation, does not penalize Standing. Implementing Treaty §3 requires modifying `_try_conquest` (and any future PT-against-treaty-party path) to check membership and trigger the violation cascade.

**F6. v12c baseline is structurally unreachable from main with PT+Treaty alone.** PT §5 and Treaty §5 both validate at N=1000 with **five** mechanics co-active: Parliamentary Transfer, Einhir Revival, Altonian Reinforcements, Restoration Movement PT-decay, Treaty Expiration, plus "EA throttle every-arc." Main has none of these. Varfell and Hafenmark faction-unique action slots are explicitly `BLOCKED on Pass 2d/2e + contamination audit` in `faction_action.py:128` (they return `'invalid'` and fall through to generic conquest). v12c's 24.7 / 28.6 / 24.2 / 22.5 is a five-mechanic equilibrium; implementing two and expecting that equilibrium is unsound. The other three are load-bearing.

### §2.3 Severity 3 — annotation + provisional canon

**F7. Stale annotations.** Multiple stub headers, the treaty.py module docstring, `coverage_matrix.md`, and `module_manifest.md` carried "canon authoring pending Pass 2h" markers that became false on 2026-05-17 when canon landed. `treaty.py` also incorrectly stated `World` had no `treaties` field (it does — `game_state.py:164`, with serialize/deserialize). **Resolved in Pass A, commit `281debe`**, behavior-neutral.

**F8. Forward-flagged provisional canon items requiring ratification.** The canon docs themselves flag derivation choices for "Pass 2k Jordan ratification." Implementing them silently = ratifying on Jordan's behalf, which violates the project-owner contract. Items, all `[PROVISIONAL]` in their canon docs:

- **PARL-MODE-DRIFT-001** (`parliamentary_transfer_v30.md` §2): Punishment mode "no L+1 on Failure"; Appeasement mode "+2 Accord on Success" — derivation from v12c §4.4 framing, not in source.
- **PARL-VOTE-MODIFIER-001** (`parliamentary_transfer_v30.md` §4): Vote-bloc Pool modifiers (+1D / −1D / 0) — derivation, not in v12c §4.4 or `social_contest §10`.
- **PARL-PROTECTION-001** (`parliamentary_transfer_v30.md` §1.3): Self-transfer block — obvious-case derivation.
- **TREATY-VIOLATION-001** (`treaty_expiration_v30.md` §3): Violation magnitudes (Standing −2 violator / +1 wronged) — Pass 2h derived from v12c §4.4.1's CB-source reference, magnitudes not in v12c.
- **TREATY-NARRATIVE-001** (`treaty_expiration_v30.md` §4): 90% lapse vs deferred active-maintenance alternative (v12c §8.3) — canonized 90% but flagged narratively extreme.

## §3. Revised build plan (recommended; provisional)

This sequence corrects the original 4-pass sketch from earlier in session. Dependencies are real and ordered.

| Pass | Scope | Blocking on | Estimated lines |
|------|-------|-------------|------------------|
| **A** | Annotation cleanup (stale "canon-pending" markers across 5 files). | — | ~30 (LANDED `281debe`) |
| **B** | Treaty Expiration end-to-end. Wire `process_treaty_expirations` into the arc-boundary cascade (currently un-invoked). Add Senator Outward to `crown_initiative` per Treaty §2. Seed initial Crown treaties at world init (canon implies treaty stack already exists; baseline shape needs decision). N=100 telemetry. | F4 (Senator Outward spec is clear enough; magnitudes need ratification). Cross-faction Standing (F3) deferrable — Senator Outward Ob is `target_faction.Sta` per canon, no cross-faction Standing needed; the "Standing +1" Overwhelming effect can be deferred or mapped to `crown.standing` scalar with `[PROVISIONAL]` flag. | ~300 |
| **C** | CB economy substrate. `faction.cb_against` dict (pair-scoped), `World.cb_registry` if needed. Implement the 3-4 CB sources whose dependencies exist: Crown-restoration (territories<6 auto), adjacent-instability (arc-boundary Accord-≤1 scan), PT-Partial (self-retry), Treaty-violation. Defer Einhir-Partial / Conviction-Scar / Excommunication-CB (deps unbuilt). | F2; F5 (Treaty-violation source needs §3 handler integrated with `_try_conquest`). | ~400 |
| **D** | Parliamentary Vote contest engine. Build `parliamentary_vote.run_parliamentary_vote` against `social_contest_v30 §10` using existing `sim/personal/contest.py`. Build `parliamentary_stay.invoke_stay` / `resolve_stay_lift` per §10.1 ED-631. Define `Motion` dataclass. | F1; verify `sim/personal/contest.py` API contract before code. | ~500 |
| **E** | Parliamentary Transfer modes + outcome table. Wire to `faction_action.py` dispatch (PT joins the 30% faction-unique slot for parliamentary factions, or competes with Conquest under a separate roll-band — design choice). Consume CB on attempt; invoke Vote contest; apply Pool/Ob roll + degree table; deliver territory transfer / Accord = 1 / Legitimacy delta per §1.2. | C, D. PARL-MODE-DRIFT-001 + PARL-VOTE-MODIFIER-001 + PARL-PROTECTION-001 ratifications. | ~600 |
| **F** | Joint N=100 balance validation. Compare against interim target (§4.2). Document v12c gap. Tune `TREATY_LAPSE_RATE`, `PARL_MAJORITY_OB_BONUS`, Senator Outward cost only within ratified ranges. | B, E. Balance target ratification (§4.2). | ~150 + report doc |

Total: ~2000 lines of new code + the report. 4-6 commits depending on whether C splits into substrate-vs-sources.

## §4. Open decisions (PROVISIONAL — awaiting Jordan ratification)

### §4.1 Provisional canon items

The five items in F8 cannot be silently implemented. Three options:

- **(a) Ratify all as-written.** Take the canon docs' provisional values (Punishment no-L+1, Appeasement +2 Accord, vote-bloc ±1D, self-transfer block, violation −2/+1, 90% lapse). Implementation proceeds against canon-literal.
- **(b) Validated-core-only.** Implement only the v12c-validated mechanic core (Pool/Ob/outcome table, CB sources from §3 except Excomm/Conviction, expiration roll, Senator Outward base). Leave mode-specific effects, vote-bloc modifiers, self-transfer block, violation magnitudes as `[PROVISIONAL]` constants set to no-op or canon defaults, callable but flagged. Defer ratification.
- **(c) Mixed.** Ratify some now (e.g., self-transfer block — obvious), defer others (vote-bloc modifiers — load-bearing on balance).

Default if no answer: (b).

### §4.2 Balance target

v12c (24.7 / 28.6 / 24.2 / 22.5) is unreachable with 2-of-5 mechanics. Three honest targets:

- **(x) Accept-and-document.** Report whatever PT+Treaty produces. Treat full v12c as a later milestone when Einhir Revival, Altonian Reinforcements, and RM PT-decay land. No tuning to hit v12c numbers; only tune to preserve no-faction-at-0%.
- **(y) Chase full v12c.** Additionally implement minimum-viable versions of the other three mechanics. Much larger scope (probably doubles the build).
- **(z) Interim target.** Define a 2-of-5 expected band — e.g., "Crown drops below 40%; no faction at 0%; Hafenmark and Varfell both gain territorial-acquisition vector via PT." Tune within ratified ranges to hit it.

Default if no answer: (x).

## §5. Operational note — parallel session activity

During Pass A commit, a `CollisionError` surfaced: remote HEAD advanced from `82887dc` to `0a948ec` mid-session via 4 commits from another active session (roadmap-state infra, orchestrator SKILL/skill_registry updates, `github_ops.py` modification, "Phase 1 complete; advance to Phase 2"). No overlap with Pass A's 5 files; rebase was clean. Pass A landed on the new HEAD.

`[ASSUMPTION: parallel session is Jordan's own (or expected teammate) — basis: PT-token controls indicate sole authorized writer; no indication of compromise. Flagging for visibility only.]`

Each subsequent build pass carries collision risk. Mitigation: refresh fetch-HEAD via `quick_bootstrap` before each commit; treat hook `CollisionError` as a normal reconcile signal (not a halt), check diff overlap, rebase clean.

## §6. Sources

**Canon read this session (full):**
- `designs/provincial/parliamentary_transfer_v30.md` (179L, CANONICAL Pass 2h 2026-05-17)
- `designs/provincial/treaty_expiration_v30.md` (197L, CANONICAL Pass 2h 2026-05-17)
- `designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md` §4.4, §4.4.1, §4.5, §5 (v12c balance basis)
- Prior turn citations carried forward: `mass_battle_v30.md` §B.3 / §E.1 / §E.2 / §E.4; `ci_political_v30.md` §4.4

**Sim read this session (full or relevant ranges):**
- `sim/provincial/treaty.py`, `sim/provincial/parliamentary_transfer.py` (both annotation-cleaned in Pass A)
- `sim/personal/parliamentary_vote.py`, `sim/personal/parliamentary_stay.py` (both stubs raising)
- `sim/provincial/faction_action.py` (full 228L), `sim/provincial/crown_initiative.py` (mode dispatch + coronation)
- `sim/mc_v18.py`, `sim/peninsular/season.py`, `sim/peninsular/accounting.py`, `sim/autoload/season_manager.py`
- `sim/autoload/game_state.py` (Faction, Territory, World schema, MULTS, STARTING_OWNER, STARTING_STATS)
- `sim/autoload/victory.py` (Peninsular Sovereignty: 11/15 threshold)

**Existence-verified (not read in full):**
- `sim/personal/contest.py` (10257 bytes — basis for F1 vote engine build in Pass D)
- `designs/scene/social_contest_v30.md` (618L — §10 vote contest, §10.1 ED-631 Stay)

## §7. Status declaration

`[STATUS: PROVISIONAL — 2026-05-26. Findings F1–F6 are sim-state facts (grep-verified, schema-verified). F7 is resolved in Pass A commit 281debe. F8 enumerates canon-side provisional items requiring ratification. §3 build plan is a recommended sequence, not committed work. §4 decisions are reserved to Jordan; defaults declared but not auto-applied. No code changes from this document — pure analysis + plan.]`

## §8. Changelog

- **v1 (2026-05-26):** Initial provisional review. Companion to Pass A cleanup commit `281debe`. Awaiting §4 ratification before Pass B onward.
