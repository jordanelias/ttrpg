# External Practice Corpus — Investigation & Proposals

## Status: PROPOSED — investigation complete; **every** adoption in §7, including the declines, is HELD FOR JORDAN except P1, which is marked `RATIFY-ON-MERGE` as a bug fix. See §0.3.

**Date:** 2026-07-28
**Lane:** IN (infrastructure / cross-cutting)
**Anchor:** ED-IN-0085
**Instrument:** `tools/ci_claude_workflow_paths.py` (ships with this doc; every §5.1 number is its output)
**Method:** full-text read of nine sources, scored under three filters Jordan supplied mid-investigation — **saliency** (§0.4), **the repo's already-evidenced method** (§0.5), and **critique-or-confirmation** (§1, §6.4) — then adversarially reviewed by two independent read-only agents whose corrections are folded in and credited in §0.7.

---

## §0 Preamble

### 0.1 Sources

| # | Source | Type | Retrieval |
|---|---|---|---|
| S1 | r/ClaudeAI — "Sonnet v Opus effort levels" | Reddit self-post (LLM-generated body) | `old.reddit.com` HTML → BeautifulSoup; body + 11 comments |
| S2 | r/ClaudeAI — comment `owcqe5k` (`fable-chief-agent`) | Reddit comment | same; comment + 15 siblings |
| S3 | r/ClaudeWorkflows — "Create a `You.md` Skill" (Ditto) | Bot-generated digest | same; body, 0 comments |
| S4 | r/ClaudeWorkflows — "Multi-Agent Adversarial Code Review" | Bot-generated digest | same; body, 0 comments |
| S5 | atlasworkspace.ai — "Claude for Research" | Vendor content marketing | curl → html2text |
| S6 | code.claude.com — Best practices | Official documentation | **WebFetch, full page (39.6 KB)** |
| S7 | code.claude.com — Common workflows | Official documentation | **WebFetch, full page (18.5 KB)** |
| S8 | github.com/ChristopherKahler/aegis | Spec corpus, 112 files (108 `.md`), 1.28 MB | cloned @ `73a6461` |
| S9 | github.com/itsmesherry/claude-audit | TypeScript CLI, 39 files | cloned @ `2038ef5` |

Model facts (§4) come from the authoritative `claude-api` skill, **not** the corpus — S1 is a generation stale (§3.2).

### 0.2 Read-completeness disclosure

AEGIS is ~320k tokens, larger than one context. **Read in full:** `README.md`, `src/rules/epistemic-hygiene.md`, `src/rules/agent-boundaries.md`, `src/schemas/confidence.md`, `src/core/workflows/phase-4-adversarial-review.md`, `src/core/workflows/session-handoff.md`, `src/core/agents/architect.md`. **Measured rather than assumed:** personas' mean pairwise heading-skeleton similarity 1.000 / body 0.914; agents 1.000 / 0.907; domains genuinely distinct at 0.355. **Not read:** 11 personas, 11 agent manifests, 13 domains, 8 tool adapters, 10 commands, the `src/transform/` tier, `install.sh`.

⚠️ **Correction to an earlier draft of this line.** It claimed *"every behavioural claim in §2.1 comes from a file I read in full."* That was false: §2.1's defect 2 rests on the tool adapters and the Transform tier, both listed above as **not read**. What I actually read is `README.md`'s tooling table (one line per adapter) — enough to establish that all eight are static/historical, not enough to have read `src/transform/schemas/intervention-level.md`, the file that makes the confidence gate hard. §2.1 is re-sourced accordingly. This is the exact failure §0.1 point 3 exists to catch, and the honesty apparatus was pointed at the wrong tier.

### 0.3 Ratification boundary (CLAUDE.md §2, made loud)

Merging normally ratifies PROPOSED contents. **P1 only** is `RATIFY-ON-MERGE` (a bug fix). **P2–P9 and every row of the Declined table are HELD** — declining AEGIS's corpus, its confidence vector, `you.md`, `fable-chief-agent`, Atlas, and `claude-audit` are six design calls, and they must not ratify silently.

### 0.4 Saliency filter — what this repo actually is

Jordan: *"we don't really need 'security' for a one-man private project."* This disqualifies more of the corpus than any quality judgment does. Solo, private, pre-production, prose-and-simulation — no users, PII, deployment, uptime, on-call, or team.

| Salient (7/14 AEGIS domains) | Not salient |
|---|---|
| 0 Context · 1 Architecture · 3 Correctness · 6 Testing · 9 Maintainability · 11 **Change risk** · 13 Risk synthesis | 4 Security · 5 Compliance/PII · 7 Reliability/SLA · 10 Operability/on-call · 12 Bus factor |

Also disqualified before any quality question: **the entire tooling stack** (CVE/secrets/IaC/SBOM scanners on a repo whose deps are `pyyaml`+`pytest`); **the Reality Gap framework** (no production); **the Safety/Liability framework and intervention levels 1–4** (they gate an AI auto-applying changes on someone else's behalf); **domain 12** (bus factor 1 is the premise, not a finding); **claude-audit's Security + Dependencies** categories.

**This downgrades one of my own findings.** §2.1's defect 2 disables a tier we would never enter. It is evidence about spec-only rot, **not a blocker** — ranking it as a headline would be the "sounds rigorous, changes nothing" failure §0.1 exists to prevent.

### 0.5 The evidenced method — the real baseline

Measured from `.claude/wf_*.js`, this repo already runs:

| # | Practice | Evidence |
|---|---|---|
| 1 | Agonist→antagonist relay, read-only critic | `critic` ×20, `antagonist` ×2 |
| 2 | Refutation-based verify | `refute` ×10, `adversarial` ×21 |
| 3 | **Corpus-wide gap-refutation** — *"is the claimed gap actually unfilled across the whole corpus?"* | `wf_social_contest` Verify |
| 4 | **All-directions pipeline tracing** | `wf_attribute_coherence` Trace |
| 5 | Dead-data / orphan-emission detection | `dead-data` ×6, `orphan` ×5 |
| 6 | Sampled provenance validation vs cited `file:line` | Validate phase (10 random rows) |
| 7 | Per-lens fan-out (7 families; 8 lenses) | both scripts |
| 8 | Per-phase model + effort + schema-forced output | `meta.phases[].model` haiku→sonnet→fable |
| 9 | Cite `file:line`; severity P1/P2/P3 | SHARED preamble |
| 10 | Three-mode stance — curious / adversarial / judicious | `wf_combat_critique` SHARED |
| 11 | Barrier-merge census → dedup before expensive work | Census phase |

**Practices 3 and 4 are ahead of the entire corpus** — nothing in nine sources proposes an equivalent.

⚠️ **But practice 1 is currently a label, not a mechanism.** "read-only adversarial critic" lives in a `detail:` display string; **no `.claude/wf_*.js` restricts critic tooling**. S6 supplies the fix (`--allowedTools`) — see P4.

### 0.6 RULED 2026-07-28 (Jordan) — Fable placement

> *"Fable is too expensive to use for synthesis. I would prefer fable to work on a read-only audit basis or as a planner/orchestrator/guardrail."*

**Supersedes `CLAUDE.md` §10's fable row**, which assigns it *"propagation-spec authorship… deepest cross-corpus synthesis"* — the artifact-producing role now ruled out.

| Fable 5 — yes | Fable 5 — no |
|---|---|
| Read-only audit · planner · orchestrator · guardrail | Synthesis · artifact authorship · long-output stages |

Corpus **confirms it independently** (§6.4). Rationale beyond price: a synthesis artifact is reviewable and cheap to revise; **an audit verdict or guardrail decision is where being wrong is silent.** Spend the top tier where the error doesn't announce itself. Immediate consequence: `wf_attribute_coherence.js` declares `Synthesis | model: 'fable (opus max fallback)'` — the exact anti-pattern; re-tiers to Opus 5 (P1c).

### 0.7 Adversarial review of this document

Two independent read-only agents attacked this doc. **They found real errors, and the pattern in what they found is the finding:** everything re-derivable from a register held; **everything I counted by hand and shipped without an instrument was wrong** — the §5.1 headline (inflated ~10×), the §5.4 CI ratio (inverted), the §6.2 growth figure (units mismatch), and five accounting details. That is this repo's own P1-falsifier discipline, applied to me, and I had not taken it from the corpus I was reading. Every correction is folded in below and the instrument now ships. Two further corrections they surfaced — that `tools/ci_claim_provenance_check.py` and `tools/sim_harness/trace_logger.py` already own most of what my P6 proposed — collapsed a proposal to a one-line change (§7/P6).

---

## §1 Executive summary

**These proposals are as much a confirmation of current operations as a critique of them, and the split is the finding.** On *method*, the ecosystem is validated: five sources independently arrived at practices the repo already runs, at 4-independent-source strength on the adversarial core, and two practices are ahead of everything in the corpus (§6.4). On *plumbing*, it is not — but far less dramatically than my first draft claimed.

1. **Corrected headline.** `tools/ci_claude_workflow_paths.py` (shipped here) resolves **51 dependencies across `.claude/`: 12 live, 35 aliased, 4 DEAD.** My hand-count said "44 of 64 broken"; that was wrong ~10× because it ignored the sanctioned alias map and counted paths the scripts *deliberately name as nonexistent as their own findings*. The real defect is narrower and different: **35 references resolve only through an indirection the scripts never declare**, 4 are genuinely dead, and two scripts carry `C:/Github/ttrpg` and `/home/claude` prefixes that **never resolved in this checkout** — predating the retirements I blamed.
2. **The registry-blindness half survives intact and is the more important half.** `build_apparatus_registry._workflows()` resolves to `.github/workflows` only; the incumbent owner of the retired-pointer rule declares this exact blind spot in its own `COVERAGE_GAPS`; and the same rot has reached **three more apparatus surfaces** nobody swept (§5.1).
3. **A live hole in §11's guard** — the highest-value item the corpus produced, and I nearly missed it. `update_trigger`, `fire_trigger`, and the `loop` skill are undenied route-arounds of the denied `create_trigger` (§5.2, P2).
4. **Two sources fail under execution** (§2), both the spec-never-executed failure mode this repo is itself exposed to (§6.3).
5. **§10 is stale in six ways, not two**, and no file in the tree binds tier aliases to model IDs — the only place IDs exist is `tools/model_router.html`, which routes to **Sonnet 4 and Opus 4.6** (§5.3, P5).

---

## §2 The two repos

### 2.1 AEGIS — a specification that cannot execute its own top tier

90 (v0.1) / 112 (v0.2) files defining 12 personas × 14 domains, a 7-layer epistemic schema, a confidence vector, a disagreement protocol, and a Transform pipeline gated by four intervention levels. Its README's own "What v0.1 Is Not": *"v0.1 does not include runtime execution."*

**Defect 1 — the flagship confidence example violates its own rule.** `src/schemas/confidence.md` rule 3: *"`overall` must be derived from the formula. Manual override is not permitted."* Example 1 declares 4/2/5/5 and asserts **`Overall: high`**; `floor(min(4,2)·0.6 + 5·0.3 + 5·0.1) = floor(3.2) = 3` → **medium**. Its own prose concedes *"the raw formula yields medium."* Reproduces exactly.

**Defect 2 — the authorization tier is unreachable under honest anchoring.** Sweeping all 5⁴: only 35/625 combinations reach `high` (29 after the dimension-1 override), and `high` requires **both** `evidence_diversity ≥ 4` **and** `signal_freshness ≥ 4` — the latter defined as *"recent runtime data (logs, metrics, profiling)."* All eight adapters are static or historical (`iac_scan`, `history_mining`, `secrets_detection`, `vulnerability_scan` ×2, `static_analysis`, `code_quality`, `sbom`); every `runtime` mention in `src/tools/` is a stated *limitation*. So no honestly-anchored finding reaches `high`, and intervention levels 3–4 stay shut. **Three of six** Phase-1 signal dimensions are declared with no adapter behind them (Behavior/profilers, OpenSSF Scorecard, OpenAPI/gRPC validation) — the *orphan-emission* class §0.5 practice 5 hunts.

⚠️ **Two corrections to my own framing.** (a) I first wrote *"can never be entered by the system as shipped."* Too strong: AEGIS **has no runtime**, so nothing executes the formula at all — and an agent that inflates `signal_freshness` to 4 (precisely the confidence inflation the schema exists to prevent) enters the tier trivially. Correct claim: **unreachable under honest anchoring, and unenforceable either way.** (b) Sourced from `README.md`'s tooling table, not from the adapter files or `intervention-level.md` — both unread (§0.2).

**Additive to §0.5 — three things:**

1. **Disagreement as a first-class record with a mandatory adjudication.** `{finding_id, layer_disputed, positions[], root_cause (closed set), resolution_model, principal_response REQUIRED, status}`, plus five named resolution models and *"no silent disappearance."* **This is the real gap:** the repo generates disagreements better than AEGIS (practice 3 beats its Devil's Advocate) and **records them worse** — a critic finding that synthesis quietly drops leaves no trace.
2. **"Cross-domain observation, not cross-domain judgment."** Maps onto lane discipline and extends it from commits down to findings.
3. **The null-result alarm** — converges independently on §0.1 point 2.

**Not additive:** the Devil's Advocate concept (practice 1), adversarial review generally (2), the confidence vector (superseded, P6).

### 2.2 claude-audit — the inverse: thin theory, real machinery

Working, tested, published; two of its seven categories non-salient (§0.4). I read `agent-loop.ts` in full rather than trusting the README: **the guardrails are real** — SHA1-hashed repetition detection (3-in-6 window), turn cap, token budget, prompt-cache blocks, per-turn streaming, errors-as-results, full `agent-trace.jsonl`.

**Defect 1 — a failed audit still renders a score, at two sites.** When the agent never calls `finalize_audit`, `agent-loop.ts:490` stamps `score: 50, grade: 'C'` — but `types.ts:140` returns `'D'` for 50, so the literal contradicts the project's own grading function; `auditor.ts:219` then renders a real overall number and grade. **The same `score: 50, grade: 'C'` literal appears a second time** in `claude-analyzer.ts:172`, in the one-shot path, reached whenever the model omits a category — arguably more reachable. A two-site pattern defect, which is §0.1 point 5's own standard for sweeping rather than patching. *Mitigations I initially omitted:* the null branch also sets an explicit `summary: 'Agentic audit ended without a finalized submission.'`, and `auditor.ts:36` recomputes `grade = scoreToGrade(score)` after static penalties — so the bogus `'C'` survives only for categories with zero static findings.

**Defect 2 — the budget ceiling is soft by one turn.** The `totalTokens > maxBudgetTokens` check runs *after* the response returns, so a run overshoots by up to a full turn (`max_tokens: 16000` + input). *Correction:* "hard cost ceiling" is a **source comment** (`agent-loop.ts:7`); the README's phrasing is "500k-token hard ceiling." My earlier "the README overstates it" quoted a phrase the README doesn't contain.

**Additive — the termination discipline the repo entirely lacks:** repetition breaker · `stopReason` as a first-class closed-set output · `agent-trace.jsonl` · budget-aware nudge at 70%.

---

## §3 The seven web sources

### 3.1 S6 / S7 — official docs (highest credibility, and the source I mined worst)

An adversarial reviewer's sharpest finding: **I extracted four bullets from ~15 adoptable mechanisms** from the two highest-credibility sources — the "skimming" the brief forbade. The ones I missed matter more than the ones I took:

- **`--allowedTools`** — makes §10's *"critic gets read-only tools"* structural instead of a label (§0.5 ⚠️). **The single highest-leverage fix in the corpus.**
- **`/code-review`** — a bundled fresh-subagent adversarial diff review, already installed, absent from §9's routing table. I proposed building critic infrastructure while the shipped one goes unused.
- **Stop hook as a blocking gate.** I observed the repo's Stop hook *"reminds but does not block"* (`session_handoff_reminder.py` — "NEVER blocks stopping (always exits 0)") and proposed **nothing**. A Stop hook running `review_core.py --check` is the cheapest high-value adoption available.
- **Auto mode's abort-on-repeated-block for `-p` runs** — a shipped circuit breaker with a documented threshold, i.e. P3's requirement, from the top-credibility source rather than a third-party TypeScript port.
- **"After two failed corrections, `/clear`"** — a quantified, zero-cost thrash breaker.
- **`/rewind` + restore-code-only** — the native "design review reset" S4 asks for and cannot specify.
- **"Convert it to a hook"** — S6's actual prescription for CLAUDE.md bloat, and the model §11 used to make its own rule stick. My P8 destinations omitted it.
- **CLAUDE.md hygiene** and the per-line test *"Would removing this cause Claude to make mistakes?"*

### 3.2 S1 — model/effort tiering (directionally useful, factually superseded)

Claude output relayed by the poster, conceding *"my estimates… not measured figures."* One generation stale — reasons about Opus 4.8; top comment is *"Need this tested with opus 5."* **No number in it is safe to port.**

| Rule | Status |
|---|---|
| "Escalate the model, not the effort" | Absent from §10 — but §4.3 shows a cost S1 omits |
| "Never let a thread validate its own work" | **Already held** (practice 1). *Correction: I credited this to S1; **S6 states it independently at the top credibility tier** — "a fresh context improves code review since Claude won't be biased toward code it just wrote." Cite the reliable one.* |
| "Set effort explicitly" | Partially held — `agent()` already carries `effort` |

⚠️ **Not adopted:** S1's claim that changing `effort` invalidates the cache. The authoritative invalidation hierarchy does not list `effort`. Unverified.

### 3.3 S2 — `fable-chief-agent` (right taxonomy, unevaluable rule)

Its tiering **is** §10 + practice 8, arrived at independently — convergent, not additive. Its `<boundary>` test is sharper: *"delegate work where the result can be checked from evidence."* **The hole, raised in-thread and never answered:** work Fable directly *"only when delegation would cost more than the task itself"* — with no price deltas. §10 has the identical gap; §4.2 closes it. Adoption evidence is poor: *"blew through all my fable tokens within 10 minutes without getting anything done"*; *"Fable fired me."*

### 3.4 S4 — multi-agent adversarial review

A digest whose **Limitations** are its most useful part: *"the method for the judge subagent to detect 'spiraling' is not detailed."* Its review-panel / judge / cross-model elements are **already held** (practices 1, 2, 7). Two things are additive and both are loop control: **spiral detection with a design-review reset**, and a **3-round cap**. Every `wf_*.js` phase list is fixed-length and terminates by exhaustion; nothing detects fix-thrash.

⚠️ **Correction:** I cited `wf_attribute_coherence.js` as evidence the repo "already has a more sophisticated harness." Given §5.1, a script with 4 dead paths and 35 undeclared indirections is *degraded* coverage. The claim stands on the *design*, not on current runnability.

### 3.5 S3 — `you.md` / Ditto (decline; salvage one idea)

**Decline:** grows the always-loaded surface against a measured upward trend (§6.2); cuts across the deliberate lane split. *(Saliency-adjusted: the secret-stripping concern is weak here — solo, private.)*

**Salvage: rank by independent rediscovery.** Composes directly with practice 7 — `wf_social_contest` already runs 8 lenses and discards the rediscovery count. Also the quantitative answer to §6.1.

### 3.6 S5 — Atlas (vendor marketing; one step, now largely redundant)

Step 7's **support-strength classification** (*directly supported / weakly supported / contradicted / missing / needs context*) looked like the missing vocabulary for §5.3. **It mostly isn't** — see P6: the repo already ships `canon_status: verified|provisional` and a blocking `MEASURED-BY:` provenance gate.

---

## §4 Model currency (authoritative — replaces every S1 number)

### 4.1 Roster

| Model | ID | Context | Max out | $/MTok in | $/MTok out | Cache min |
|---|---|---|---|---|---|---|
| Fable 5 | `claude-fable-5` | 1M | 128K | $10 | $50 | 512 |
| Opus 5 | `claude-opus-5` | 1M | 128K | $5 | $25 | 512 |
| Sonnet 5 | `claude-sonnet-5` | 1M | 128K | $3 (**intro $2 → 2026-08-31**) | $15 (**intro $10**) | 1024 |
| Haiku 4.5 | `claude-haiku-4-5` | 200K | 64K | $1 | $5 | 4096 |

Effort `low/medium/high/xhigh/max`, GA, **default `high`**. Opus 5: thinking **on by default**; `disabled` accepted **only at effort ≤ high** (400 at `xhigh`/`max`).

### 4.2 The price ladder — closing the S2/§10 hole

**Today (intro pricing, through 2026-08-31): Haiku 1× · Sonnet 2× · Opus 5× · Fable 10×.**
**At list (from 2026-09-01): 1× · 3× · 5× · 10×.**

⚠️ I first wrote only the list ladder because it is more memorable — while my own §4.1 table recorded the intro price *currently in effect*. P5 must transcribe **both**, with the reversion date, or §10 will carry a number that is wrong today and right in five weeks.

### 4.3 Three caching facts bearing on the fan-out pattern

1. **Parallel agents sharing a prefix cannot read each other's cache.** An entry becomes readable only once the first response *begins streaming*; N concurrent identical-prefix requests all pay full price. Fix: fire 1, await first token, then fire N−1. Every `parallel()` fan-out currently pays N× on its preamble (measured 1,616 / 996 / 400 tok — small today, scales with width).
2. **Haiku 4.5's cache minimum is 4,096 tokens — 8× Opus 5's 512, and non-monotonic.** All three preambles are *below* Haiku's floor, so on a Haiku finder stage they **silently never cache**. "Cheap tier ⇒ cheap fan-out" has a caveat running opposite to the price ladder.
3. **Model switching invalidates the entire cache — no escape hatch.** The real cost behind "escalate the model, not the effort." Escalate at *phase* boundaries, where the cache turns over anyway.

---

## §5 What the investigation found in this repo

### 5.1 The `.claude/` apparatus — corrected, instrumented, and wider than I thought

`tools/ci_claude_workflow_paths.py` output:

| File | Referenced | Live | Aliased | **DEAD** |
|---|---|---|---|---|
| `wf_attribute_coherence.js` | 36 | 10 | 24 | **2** (`sim/personal/`, `sim/provincial/`) |
| `wf_social_contest_critique.js` | 11 | 1 | 9 | **1** (`sim/personal/contest.py`) |
| `wf_combat_critique.js` | 3 | 1 | 1 | **1** (`designs/scene/combat_engine_v1`) |
| `launch.json` | 1 | 0 | 1 | 0 |
| **Total** | **51** | **12** | **35** | **4** |

**Three corrections to my first draft, all from adversarial review:**
- **"44 of 64 missing"** ignored `references/restructure_ledger.md`, the *sanctioned* resolution route. 35 of those resolve.
- It counted paths the scripts **deliberately name as nonexistent** (`"filed under NONEXISTENT params/combat.md"`, `"generator tools/extract_values.py is dead"`) as evidence of rot. Those are the audit's **findings**; counting them inverts the script's meaning. The instrument now excludes them.
- **"Every miss is collateral from `designs/` and `sim/`"** is false, twice over: many are `params/ → engine/params/` (ED-IN-0071 P3), a third move CLAUDE.md §3 states leaves prose refs in place **by design**; and `wf_combat_critique.js` / `wf_social_contest_critique.js` carry `C:/Github/ttrpg` (3 occurrences) and `/home/claude` (6 occurrences, 2 distinct) absolute prefixes that **never resolved in this checkout** — so §6.3's "rotted unobserved for nine days" is wrong for two of three scripts.

**The real defect is narrower and different:** 4 dead, and **35 references that resolve only through an indirection the scripts never declare** — a dispatched agent is told to read `designs/npcs/npc_behavior_v30.md` and must independently know to consult the alias map.

**The registry-blindness half survives intact, and the rot is wider than `.claude/`:**
- `build_apparatus_registry._workflows()` → `.github/workflows` only. Zero `wf_` in `references/apparatus_registry.yaml`.
- **The incumbent owner already declares this gap.** `tools/observability/build_incompleteness.py::scan_retired_tree_pointers` owns the retired-pointer rule and states in its own `COVERAGE_GAPS`: *"pointers in docs/comments and non-`designs/` dead paths are not yet validated."* Its `RETIRED_TREES = ("designs/",)` — **missing `sim/`**. My first draft proposed bolting this onto `broken_dependency_checker` without naming the incumbent: the §8 hazard I claimed to be honouring.
- `build_apparatus_registry._py_import_index()` walks `("tools","skills","sim","tests")` — `sim/` is retired, so **144 `.py` files under `engine/` and `systems/` are invisible to the orphan detector's import graph**, in the very file I opened to critique. I read three lines and stopped.
- `tools/canon_coverage_check.py` walks `designs/` (gone) and is wired as a **blocking** CI job.
- `.claude/launch.json` points at `designs/scene/combat_engine_v1/workbench/server.py`.

*Nuance:* "orphaned" holds in the **invoker** sense only — the scripts are documented in `registers/handoffs/HANDOFF_IN.md`, the IN ledger (ED-IN-0029), and an audit doc.

### 5.2 A live hole in §11's guard

`.claude/settings.json` denies four primitives. Undenied and **live in this session**: `mcp__Claude_Code_Remote__update_trigger` (re-enable/re-cron an existing Routine — a direct route-around of the denied `create_trigger`), `mcp__Claude_Code_Remote__fire_trigger`, and the **`loop` skill**. §11's own falsifier anticipates exactly this: *"if a session ever schedules a wake-up while these pass… find the new primitive and add it to `REQUIRED_DENY`."* S7 enumerates four scheduling surfaces against §11's four-item roster; I read the enumeration and never diffed the lists.

### 5.3 Vocabularies and model IDs

**Three confidence vocabularies, not two.** (A) editorial ledgers: 1,075 entries, **700 (65%) absent**, and of the 375 present **89% say `high`, 2 say `low`**, with `med` (27) / `medium` (11) as unvalidated spellings of one value — empirical confirmation of exactly what AEGIS's schema was written to prevent. (B) `audit_registry.py`: `measured|inferred`, validated but its CI check always exits 0. (C) **`tools/sim_harness/trace_logger.py`: `canon_status: verified|provisional`** — which I missed because I grepped for *AEGIS's terms* (`confidence_vector|evidence_diversity`) rather than the concept. Pattern-matching on the source, which the brief forbade, producing a false negative my P6 was built on.

**§10 is stale in six ways, not two:** (1) "updated for Opus 4.8"; (2) the `fable` cap expired 2026-07-07; (3) "availability restored 2026-07-01", never re-verified; (4) "no zero-data-retention → use `opus`" — an unsourced commercial-terms claim that **routes work away from a tier**; (5) "the safety classifier is irrelevant to game-design content" — unsourced; (6) it sources its whole discipline from `deprecated/skills/…/model_routing_table.md`, which §1/§3 declare *"history only, never canonical."*

**And no file binds tier aliases to model IDs.** The only IDs in the tree are `tools/model_router.html:78-80` — `claude-haiku-4-5-20251001` (current), **`claude-sonnet-4-20250514`** and **`claude-opus-4-6`** (both stale). A live tool routing to Sonnet **4**.

### 5.4 CI gate mix — my claim was inverted

⚠️ I wrote *"27 of 31 CI jobs are report-only… the repo already practises an intervention ratchet without having named it."* **Both halves are wrong.**

`valoria-ci.yml` has **29 jobs**; **5** carry job-level `continue-on-error`, ~5 more have a report-only *step*, and 2 tools always exit 0 — **~10–12 of 29 (≈40%)**, with the majority **blocking**, consistent with §8's *"CI is the unbypassable boundary."* The "27" was a `grep -c` on the string `report-only`, counting job **names** and comments.

**And the repo has named the ratchet.** `tools/review_core.py`: *"**The ratchet**: report-only signals are graded against `registers/review_baseline.yaml` — a signal is a REGRESSION (and fails `--check`) only when it exceeds its accepted baseline. **Debt can only shrink.**"* It ships closed verdict/tier sets, RED/AMBER/GREEN roll-ups, and machine-readable state (ED-IN-0077). My draft mentioned `review_core` zero times while proposing to import the concept from AEGIS.

---

## §6 Conflicts, tensions, confirmations

### 6.1 "Empty critic panel means broken" vs "reviewers over-report"

Different stages, not opposites. AEGIS's is a **harness health check** on the producing side (a null result is evidence about the *harness*); S6's is a **triage rule** on the consuming side. The repo holds the synthesis in §0.1 point 2. The mechanism letting both coexist: **alarm on zero, rank by independent rediscovery** (P7).

### 6.2 "Max effort by default" vs "prune ruthlessly"

Not in conflict — max effort is *how hard to work a task*; pruning is *what must be resident to work any task*. The reconciling test is S6's and is compatible with §0.

⚠️ **Corrected measurement.** I compared characters-now to bytes-then and reported +7%. Like-for-like: **48,612 → 52,519 bytes = +8.0%** (chars 48,160 → 52,036 = +8.05%), and the growth landed in ~1 day, not two. **Corollary I missed: `CLAUDE.md` §11's own arithmetic is now stale** — it self-asserts "48,612 chars ≈ 12,153 tokens" against a file that is no longer that size. One line to fix, and it is a live instance of the §0.1-point-5 signature §11 itself defines.

### 6.3 Spec-first vs ship-first — the cautionary tale that lands closest

AEGIS wrote 1.28 MB of specification, shipped no runtime, and its top tier turned out arithmetically unreachable **with nobody noticing, because nothing ever ran it.** claude-audit shipped a working loop; its defects are small and local. This repo sits closer to AEGIS than is comfortable — §6 records a Godot conversion *"PROPOSED and largely un-executed"* with a spine *"defined nowhere in the corpus"*, and §5.1 shows apparatus rot across five surfaces. **The precise warning is not "write tests": it is that a specification's internal arithmetic can make its headline capability impossible, undetected, because the specification was never executed against its own tooling.** My own uninstrumented headline (§0.7) was the same failure in miniature.

### 6.4 The confirmation ledger — what the corpus validates

| Practice (§0.5) | Independently confirmed by | Strength |
|---|---|---|
| **1. Agonist→antagonist, independent critic** | S8, **S6** (*"a fresh context improves code review since Claude won't be biased toward code it just wrote"*), S1, S4 | **Very strong — 4 sources** |
| **2. Refutation-based verify** | S8 (attack confidence, not conclusions), S6 | Strong |
| **6. Sampled provenance vs cited `file:line`** | S5 (open the citation, read the passage, classify support) | Moderate |
| **7. Per-lens fan-out** | S2 thread (*"embarrassingly-parallel breadth… isolated from your main context"*), S6, S8 | Strong |
| **8. Per-phase tiering + explicit effort** | S1, S2, §10 — three independent derivations of one ladder | **Very strong** |
| **8b. Top tier on review, not authorship** *(§0.6 ruling)* | S1 (*"the one supervisor task worth Opus… precisely the capability adversarial review needs"*), S2 (Fable keeps risk-identification, disagreement resolution, gating) | **Strong — arrived before the ruling did** |
| **9. Cite `file:line`** | S9's system prompt (*"never report a finding you have not verified in the actual source"*) | Strong |
| **§0.1 pt 2 — assert that you asserted** | S8's null-result alarm | **Exact convergence** |
| **§11 no self-scheduling** | S6/S7 route recurring work to Routines / GitHub Actions / `/loop`, never to self-re-arming — and S7 documents **GitHub Actions cron as the §11-compliant path the repo already uses** (`audit-refresh.yml`) | Confirms, and supplies the sanctioned alternative |

**Two practices are ahead of the entire corpus:** practice 3 (corpus-wide gap-refutation) and practice 4 (all-directions tracing with dead-data detection).

**Net verdict:** the method is externally corroborated at 4-source strength, ahead on two axes, with one structural gap (**loop termination**), one recording gap (**disagreements**), one *mechanism* gap (**read-only critics are a label, not a tool restriction**), and a plumbing layer that has rotted across five surfaces.

---

## §7 Proposals

Scored `ADDITIVE` / `ALREADY HELD` / `DECLINE` against §0.5, filtered for §0.4 saliency, each with a falsifier and its current outcome.

### P1 — Route dead-path detection through its incumbent owner `ADDITIVE` `RATIFY-ON-MERGE`

**Why:** §5.1. Five apparatus surfaces rotted; the rule already has an owner that declares this gap.

**Do:** (a) widen `build_incompleteness.py` — `RETIRED_TREES += ("sim/",)` and fold in `ci_claude_workflow_paths.py`'s resolver, so **one owner** covers dead paths (§8: never re-implement a rule; my first draft violated this by proposing `broken_dependency_checker` while never naming the incumbent); (b) fix `_py_import_index`'s roots to `("tools","skills","engine","systems","tests")` — 144 files currently invisible — and teach `_workflows()` about `.claude/*`; (c) repair or retire the three scripts, **declaring the alias indirection or rewriting to live paths**, and re-tier `Synthesis` off Fable per §0.6; (d) fix `.claude/launch.json` and `canon_coverage_check.py`.

**Falsifier:** `python3 tools/ci_claude_workflow_paths.py` exits 0. **Currently FAILS (4 dead)** — red now, green after repair. Instrument ships with this doc.

### P2 — Close the §11 deny-list hole `ADDITIVE` `HELD` — **highest value**

**Why:** §5.2. `update_trigger` / `fire_trigger` / `loop` are live route-arounds of a denied primitive, and §11's own falsifier says to add them.

**Do:** add all three to `REQUIRED_DENY` in `.claude/settings.json`, `tools/ci_hooks_verifier.py`, and `tests/valoria/test_no_polling_triggers.py`.

**Falsifier:** the existing mutation-verified test, extended — delete any of the three and both it and the CI job fail. **Currently the three pass while undenied.**

### P3 — Termination discipline `ADDITIVE` `HELD`

**Why:** §3.4 + §2.2. The clearest structural gap: excellent at fanning out and refuting, **no loop-termination discipline at all**.

**Do:** prefer the **native** mechanisms S6 supplies over a third-party port — auto mode's documented abort-on-repeated-block for `-p` runs, `/rewind` restore-code-only as S4's undefined "design review reset", and the "after two failed corrections, `/clear`" rule. Add `claude-audit`'s repetition breaker only where native cover is absent, plus `stopReason` from a closed set **surfaced in the report headline** (the §2.2 defect), a 3-round cap, and a JSONL run trace.

**Falsifier:** a seeded fix-thrash run trips the breaker within N rounds and returns `stopReason: 'repetition'`; a run halted early cannot render a report without a non-`completed` stop reason in its summary. **Neither written.**

### P4 — Make read-only critics structural `ADDITIVE` `HELD` — cheapest real fix

**Why:** §0.5 ⚠️ + §3.1. Practice 1's independence rule is a display string; **no script restricts critic tooling.** §10's own doctrine says *"make independence structural: critic gets read-only tools."*

**Do:** set `--allowedTools` / read-only `agentType` on every critic stage; add a `/code-review` row to §9's routing table; make the Stop hook run `review_core.py --check` (S6's blocking-gate pattern — currently it always exits 0).

**Falsifier:** a critic stage attempting a write fails. **Currently it would succeed.**

### P5 — §10 refresh + a single owner for tier→ID `ADDITIVE` `HELD`

**Do:** (a) fix all **six** stale items (§5.3), not two; (b) rewrite the fable row per §0.6 — *ruling to transcribe, not a proposal*; (c) name the effort ladder and Opus 5's thinking rules; (d) record **both** price ladders with the 2026-08-31 reversion date (§4.2); (e) add §4.3's three caching facts; (f) **create a single owner for the tier→model-ID map with a currency check**, and fix `tools/model_router.html`'s Sonnet 4 / Opus 4.6 routing.

**Falsifier:** no unverified dated claim past its expiry; every model ID in the tree matches the live roster. **Currently FAILS.**

### P6 — Extend the provenance gate that already exists `ADDITIVE` `HELD` — collapsed

⚠️ **This proposal shrank by an order of magnitude under review.** I proposed importing Atlas's 5-state vocabulary as "the axis nothing covers." **Two existing tools already cover it**, and I found neither because I grepped for AEGIS's terms instead of the concept:
- `tools/ci_claim_provenance_check.py` (ED-PC-0040, **blocking** CI job) already requires a quantitative ledger claim to name a re-runnable instrument via `MEASURED-BY:`, scoped by `LEDGERS = {"registers/editorial_ledger_pc.jsonl": ...}` with the widening plan written into the source: *"widen deliberately, lane by lane."*
- `tools/sim_harness/trace_logger.py` already ships `canon_status: verified|provisional` **with the exact ambiguity rationale** my draft claimed was missing.

**Do, in full:** (a) add `registers/editorial_ledger_in.jsonl` to that `LEDGERS` dict — **one line**, the widening its author planned for; (b) collapse `med` → `medium` and add a closed-set validator. **Introduce no new vocabulary** — my draft would have made a *fourth* scale on an axis (C) already covers, after §5.3 explicitly warned against a third.

**Falsifier:** the blocking `claim-provenance-check` job covers the IN lane and zero `med` spellings remain. **Currently neither.**

### P7 — Null-result alarm + rank-by-independent-rediscovery `ADDITIVE` `HELD`

Two halves of one fix that **must ship together**, or the alarm becomes pressure to manufacture findings (§6.1). (a) a critic returning zero findings records `stopReason: 'null_result'` and flags; (b) weight each finding by how many of the N lenses independently surfaced it — practice 7 already produces this data and discards it.

**Falsifier:** a deliberately no-op critic fires the alarm, and a multi-lens run's output carries a per-finding rediscovery count that a reader can check against the lens roster. **Neither today.**

### P8 — Structured disagreement records `ADDITIVE` `HELD`

Critic stages emit `{finding_id, layer_disputed, positions[], root_cause (closed set), resolution_model, adjudication REQUIRED, status}` with *no-silent-disappearance*, plus the cross-domain-observation-not-judgment rule. Epistemic parts only; drop the intervention machinery (non-salient).

**Falsifier:** a validator asserting every critic-stage disagreement carries a non-empty adjudication before synthesis is written. **Not written.**

### P9 — Measure the always-loaded surface `HELD`

A measurement, not a cut (§0.1 point 4). Apply S6's per-line test and report the split; **include "convert it to a hook" as a destination** (S6's actual prescription, and §11's own model) — my draft omitted the strongest option while claiming not to pre-judge. Fix `CLAUDE.md` §11's stale self-measurement (§6.2) as a one-line prerequisite.

**Falsifier:** a committed script reproduces the classification, and §11's quoted figure matches `wc -c`. **Neither today.**

### Declined — `HELD`, not silently ratified

| Item | Why |
|---|---|
| **AEGIS persona/domain corpus** | 1.28 MB; personas 91% similar; spec-only; 7/14 domains non-salient; top tier unreachable. Take the three epistemic parts (P8). |
| **AEGIS tooling stack, Reality Gap, Safety/Liability, intervention levels** | Saliency, not quality. |
| **AEGIS confidence vector** | Superseded by P6 at ~1 line; two verified defects; needs runtime evidence never collected here. |
| **`you.md` / Ditto** | Grows the always-loaded surface against a measured +8% trend; cuts across the lane split. Salvaged into P7. |
| **`fable-chief-agent` as written** | Taxonomy already held; boundary rule unevaluable without the cost data §4.2 now supplies. |
| **Atlas the product** · **`claude-audit` the tool** | Off-domain; 2/7 categories non-salient. Take the loop engineering (P3). |
| **S4's review-panel / judge / cross-model review** | **Already held** (practices 1, 2, 7). Only its loop-control elements are additive. |

---

## §8 Open questions for Jordan

1. **P1 as `RATIFY-ON-MERGE`** — bug fix, proceed? Everything else, including the declines, is held.
2. **P2 is the highest-value item and touches §11's enforcement architecture.** Confirm the three additions.
3. **Repair or retire the three `wf_*.js`?** Recommendation: repair `wf_attribute_coherence.js`; the other two carry `C:/Github` and `/home/claude` prefixes that never worked here — retire to `deprecated/`.
4. **P3's terminal behaviour** — halt for you, or degrade to report-only and continue? Must not be "schedule a check-in" (§11).
5. **P9 — take the measurement at all?** I have deliberately not pre-judged the outcome, though my draft did once and was caught.

---

## §9 Provenance

- **Retrieval:** reddit.com and atlasworkspace.ai were egress-blocked (403 CONNECT); Jordan opened the environment mid-session. Reddit's anti-bot then 403'd the JSON API, so S1–S4 came via `old.reddit.com` HTML + BeautifulSoup. **S6/S7 via WebFetch, full pages** — disclosed here because an earlier draft documented every other source's method and was silent on the two it rated highest.
- **Instrumented:** §5.1 is `tools/ci_claude_workflow_paths.py` output. §2.1's sweep, ledger counts, registry coverage, CI job parsing, file sizes, and preamble sizes were re-derived by script.
- **Corrected under adversarial review (§0.7):** the §5.1 headline (~10× inflated), the §5.4 CI ratio (inverted), §6.2's growth figure (units mismatch), §2.1's over-strong "can never be entered" and its sourcing, §2.2's single-site claim and misattributed quote, §4.2's ladder (intro pricing), and five accounting details (SHA `73a6461`; 10 commands; 108 `.md` of 112 files; **207** open EDs).
- **Not verified, not used:** every quantitative claim in S1, and its effort-invalidates-cache claim.
