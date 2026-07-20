<!--
PROVENANCE (added at ingest, 2026-07-01, ED-1083):
Uploaded by Jordan into the month-overview consolidation session; compiled 2026-07-01 in a
separate research session. Ingested VERBATIM below this comment block — do not edit; the
durable, Valoria-bound extraction lives at designs/architecture/holonic_container_doctrine_v1.md.
Platform facts inside carry the source's own tier tags (T0-T3 / UNVERIFIED) — re-verify
time-sensitive items (prices, availability, windows) before relying on them.
-->

# Multi-Agent Claude Code Workflow — Model Assignment & Orchestration Spec

**Project.** A bottom-up emergent game built over a nested *container / wrapper* architecture: holonic (each container is at once a whole and a part), one uniform canonical shape at every scale, with events propagating both **up** (aggregated as they cross a boundary) and **down** (distributed/refined), such that the code is *compliant* (conforms to the shape) and *convertible* (liftable and lowerable between scales without loss).

**Purpose.** Assign Claude models and Claude Code constructs across a five-stage build workflow — spending capability where fidelity is decided and cheap tiers where the work is mechanical.

**Compiled.** 2026-07-01. Consolidates and supersedes the running design from this session; every in-session correction is folded in.

**Reading the fact tags.** Platform facts are tier-tagged (`T0` strongest → `T2`). Anything not independently confirmed is `[UNVERIFIED]`. Verify time-sensitive items — prices, availability, versions — before relying on them.

> **Read §7 before building.** The short version: this apparatus is justified only if the systems web is too large for one session. If it is not, do not build it.

---

## 1 — Platform facts (2026-07-01)

**Model lineup.** Four tiers, strongest first: **Fable 5** (Mythos-class) > **Opus 4.8** > **Sonnet 5** > **Haiku 4.5**. Sonnet 5 is current and supersedes Sonnet 4.6; on the Claude API and Claude Code its `effort` parameter defaults to high. `[SOURCE: T1 — platform.claude.com models overview]`

**Fable 5 availability.** Suspended 2026-06-12 under a US export-control directive; controls lifted 2026-06-30; access restored **2026-07-01 (today)** across Claude.ai, the Claude Platform, Claude Code, and Claude Cowork. `[SOURCE: T1 — anthropic.com/news/fable-mythos-access; T2 — CNBC, The Hacker News]` Two constraints attach:

- **No zero-data-retention.** Fable requires 30-day retention of customer data. Where the game IP is retention-sensitive, Opus 4.8 is the fallback for any stage you would otherwise place on Fable. `[SOURCE: T1 — anthropic.com/news/fable-mythos-access]`
- **Subscription metering.** On Pro / Max / Team / select-enterprise plans, Fable is included for up to 50% of weekly usage limits through 2026-07-07. Via the API it is per-token at Fable pricing with no weekly cap. Match this to your billing path. `[SOURCE: T2 — CNBC]`

**Fable classifier.** Fable ships cybersecurity/biology/chemistry safeguards that fall back to Opus 4.8 for flagged requests — this much is confirmed at T1. The commonly cited "under 5% of sessions" figure and the exact domain list (including model distillation) are T2/T3 secondary and not confirmed at T1; treat them as approximate. The load-bearing point holds regardless of the number: a game sits outside those domains, so the classifier will not interfere with this workflow. `[SOURCE: T1 — anthropic.com/news/fable-mythos-access (safeguards exist); <5% figure + domain list T2/T3]`

**Context windows.** Opus 4.8 and Fable 5: ~1M input. Haiku 4.5: 200K. Sonnet 5: large window `[UNVERIFIED — Sonnet 4.6 was 1M; Sonnet 5 supersedes it, presumed 1M, confirm]`. The window that binds this workflow is the **orchestrator's**, not the subagents' — see §3. `[SOURCE: T1 + context reference]`

**Cost ordering (the load-bearing fact).** Fable > Opus > Sonnet > Haiku. The approximate ratio in circulation is ~10 : 5 : 3 : 1 (input) and ~50 : 25 : 15 : 5 (output), but those derive from T2/T3 price figures — verify exact current prices at the Anthropic pricing page (T0) before budgeting. `[SOURCE: ordering T1-consistent; ratios T2/T3 indicative]`

**Claude Code subagent architecture.** `[SOURCE: T1 — code.claude.com/docs subagents; claude.com/blog subagents]`

- Per-subagent model via `model:` frontmatter; aliases `sonnet`, `opus`, `haiku`, `fable`.
- Subagents are **stateless and isolated**: each starts with only its own system prompt plus the working directory, runs to completion, returns a result to the orchestrator, and ends. Each has its own context window. **They do not communicate with each other.**
- Per-subagent tool restriction (e.g. `Read, Grep, Glob` only) and `isolation: worktree` for an isolated repo copy.
- Definitions live in `.claude/agents/` (project) or `~/.claude/agents/` (user), as YAML frontmatter + a markdown system prompt; `name` and `description` required.
- Delegation is **description-driven**: the orchestrator matches a task to a subagent by its `description`. You own the roster and the descriptions; the routing is the orchestrator's.
- **Agent Teams** (experimental, disabled by default): teammates run in their own windows and communicate directly via a shared task list — the construct for genuine multi-agent dialogue.
- **Background agents:** many independent sessions in parallel.
- Documented best practice: start with conversational prompts and CLAUDE.md; promote recurring patterns into subagents/hooks as they clarify. Do not architect the full ensemble first.

---

## 2 — Governing principles

**Tiering discipline.** Default every node to the cheapest tier that clears its quality bar. Promote to Opus/Fable only on evidence a cheaper tier failed — an adversarial pass caught a real fault the tier produced — never pre-emptively. Opus at the judgment nodes (contract, hard antagonist, synthesis, logic/emergence audit); Sonnet 5 as the workhorse; Haiku at the leaves (extractive reads, boilerplate, conformance scans, routing).

**Strong producer when producing; strong critic when auditing.** At a generative stage the binding constraint is the artifact being produced — put the stronger tier on the *producer*, because a weak proposer gives a strong critic only weak material to attack. At an audit stage the binding constraint is catching what slipped — put the stronger tier on the *critic*. So: Stage 2 skeleton = strong agonist; Stage 5 audit = strong antagonist.

**Two failure modes dominate this project — and the model causes them, it does not merely miss them.**

- *Scripting drift* (from bottom-up emergent play): the cheapest path to a working game is a top-down special-case that hard-codes an outcome meant to arise from local rules. Guardrail for every infill agent: implement the local rule only; touch only declared inputs and outputs; never special-case an entity or an outcome to make it work.
- *Shape divergence* (from the uniform-shape multi-scale architecture): asked to build containers at different scales in separate lanes, a model treats each as a fresh problem and emits subtly different dialects that stay invisible until a wrapper composes or converts across a boundary.

**The lever.** Because every container is the same shape, conformance is a deterministic schema/contract check, not a judgment call. Freeze one canonical contract at the top, once, and most downstream work becomes instantiate-and-conform, which a cheap tier or ordinary tooling can verify. Uniformity is what lets volume move down-tier safely.

**Two properties define fidelity, and they are not in tension:** structure is uniform and top-imposed (one shape at every scale); behaviour is bottom-up and emergent (local rules produce play). The contract constrains shape, never behaviour.

---

## 3 — Claude Code construct mapping (what to build with)

The tiering is sound and the model assignment is real (§1). What the orchestration needs is the right construct per stage; the common error is to assume a richer primitive than exists.

**"Agonist–antagonist pair" is not a native subagent primitive.** Subagents do not converse. What the primitive gives is an orchestrator-mediated *relay*: dispatch agonist → capture its output → dispatch antagonist with that output as input → orchestrator reconciles. For skeleton review and the final audit this relay suffices — and for the audit it is *preferable*, because a stateless critic that never saw the producer's reasoning is more independent, not less. Reserve **Agent Teams** for the case where a proposer and a critic must actually iterate against each other; accept its experimental status and enable it explicitly.

**Independence is structural, not asserted.** An "independent auditor" here means a separate subagent, tools restricted to `Read, Grep, Glob` (no `Write`/`Edit`) so it cannot rewrite what it judges, its own context, optionally `isolation: worktree`. Tool restriction is the mechanism.

**Routing is by description.** You do not assign Fable to Stage 5 per run; you define an audit subagent with `model: fable`, restricted tools, and a precise `description`, and the orchestrator delegates by matching. The artifact you deliver is the roster (§6), not a per-invocation instruction.

**Parallel write lanes need isolation.** Multiple write-capable subagents on one repo collide over the working tree. Put `isolation: worktree` on every infill lane that writes; reconcile by merge at fan-in.

**Synthesis binds on the orchestrator's window, not the subagents'.** Each lane has its own window, but the orchestrator must hold every lane's output to synthesize. Have lanes return fixed-format summaries, not raw context; run the synthesizer on a 1M-window model; if even summaries overflow a deep ladder, synthesize hierarchically (adjacent scales first, then aggregates).

**Check built-ins before hand-rolling.** Claude Code reportedly ships a Haiku-powered Explore subagent and a dedicated Plan subagent, which would cover part of Stage 1. `[UNVERIFIED — single T3 source; confirm against your `claude` version's release notes]` Use them if present; define only the gaps.

---

## 4 — Stage assignment (final)

| Stage | Construct | Model(s) | Tools / isolation | Charter & guardrail |
|---|---|---|---|---|
| **1. Read + define canonical shape** | subagents (+ built-in Explore/Plan if present) | Haiku (extractive, fits 200K) · Sonnet 5 (interpretive or >200K) · **Opus/Fable** (the contract) | readers read-only; contract-author scoped `Write` | Readers map systems and existing coverage. Top tier authors the one artifact replicated at every scale: container contract + wrapper contract + propagation spec. Highest-leverage judgment — an error here is N-amplified. |
| **2. Skeleton — freeze ONE interface** (strong agonist) | subagent relay | **Opus** (agonist) · Opus/Sonnet (antagonist) | agonist scoped `Write`; antagonist read-only | Agonist proposes the single container interface, wrapper interface, propagation mechanism. Antagonist hunts scripting, hidden coupling, shape divergence, up/down asymmetry, order-dependence, cross-scale feedback loops. Haiku excluded. |
| **3. Infill — instantiate + local rules** (workhorse) | subagents, worktree per lane | **Sonnet 5** · Haiku (boilerplate) · Opus (hard lanes) | scoped `Write`, `isolation: worktree` | Implement each scale's local rule against the frozen contract. Guardrail: conform exactly; add no scale-specific interface members; never alter propagation semantics; local rule only. Cheap tiers safe here *because* conformance is mechanically checkable. |
| **4. Synthesis — assemble the scale ladder** | orchestrator over compressed summaries | **Opus** default · Fable (deep/rich) | `Read` + `Write` | Wire containers through wrappers; verify an up-event reaches the top correctly transformed, a down-event reaches the bottom, round-trips are consistent, cascades converge. Lanes return summaries, not raw context. |
| **5. Invariance + emergence audit** (strong antagonist) | independent subagents, read-only | **Fable/Opus** (emergence, propagation/termination, logic) · Sonnet/Haiku (conformance, content, shape) | `Read, Grep, Glob` only | Independent of producers, tier above. Static: trace for system-originated global-state writes; flag entity special-cases; deterministic conformance scan. Dynamic: seeded headless sims diffed against the emergence contract; **ablation** — disable one system and the dependent emergent behaviour must degrade gracefully, not vanish (a clean vanish means it leaned on a scripted crutch — a fidelity break). |

> Haiku's 200K window bounds any single unit it reads, audits, or scans; route a container or scan target that exceeds it to Sonnet 5. Uniform, small containers should stay well under this.

---

## 5 — Fidelity artifacts (the spine)

**Emergence contract** — Stage 1's key output. For each intended emergent behaviour, name the local systems and interactions that should produce it, and explicitly prohibit the scripted shortcuts. This is the spec Stages 2 and 5 test against; without it, "fidelity to emergence" is not a checkable property, only an aspiration.

**Canonical contract, frozen before any fan-out.** Stage 2 fully freezes the container and wrapper shape *before* Stage 3 parallelizes across scales. Fanning out over an unfrozen contract is exactly how each lane invents its own dialect. This is the one place the strict bottom-up rule yields to a top-imposed constraint: the grounding stays bottom-up; the shape does not.

**Propagation spec** — the hardest reasoning artifact and the scariest runtime risk. Bidirectional cross-scale events invite non-termination (an up-event triggers a down-event triggers an up-event). Pin down, per direction: the boundary transform (aggregate up, distribute down); ordering and determinism (seeded RNG, fixed timestep, stable iteration order, so cascades replay); and a termination/convergence guarantee (bounded propagation depth or a fixpoint condition). Without this, "consistent shape across scales" holds statically and shatters at runtime. Top-tier judgment; do not down-tier it.

**Determinism is a hard requirement, not a nicety.** Seeded RNG threaded through every system, fixed timestep, stable iteration order — established in Stage 3. Emergence is debugged and audited by replaying seeds; non-determinism makes the Stage 5 audit impossible.

**Convertibility = round-trip morphisms.** Test lift∘lower and lower∘lift across every adjacent scale pair; assert the invariants each must preserve. If shape is truly uniform, conversion is near-identity, and a diverged scale surfaces exactly at the round-trip.

**Conformance scan is deterministic — so make it cheap and non-negotiable.** A schema/contract check over every container and wrapper at every scale (Haiku, or ordinary tooling) catches divergence deterministically. Reserve model judgment for propagation and emergence.

---

## 6 — Subagent roster (`.claude/agents/`)

Frontmatter sketches. The `description` is the trigger — keep it precise and keyword-rich. Session default (orchestrator) model: `opus`. Adopt selectively — see §7 before creating the whole set.

```yaml
# explore.md        (skip if a built-in Explore covers this)
name: explore
model: haiku
tools: Read, Grep, Glob
description: >
  Extractive codebase reads that fit context. Enumerate systems, components,
  signatures, and existing test/sim coverage. No interpretation, no writes.

# interp-reader.md
name: interp-reader
model: sonnet
tools: Read, Grep, Glob
description: >
  Interpretive and large-corpus reads: a system's role, hidden global-state
  coupling, whole-codebase coherence beyond a 200K window.

# contract-author.md
name: contract-author
model: opus            # fable if the scale ladder is deep
tools: Read, Grep, Glob, Write
description: >
  Author the canonical container contract, wrapper contract, and propagation
  spec — the frozen shape replicated at every scale. Highest-leverage artifact.

# skeleton-agonist.md
name: skeleton-agonist
model: opus
tools: Read, Grep, Glob, Write
description: >
  Propose one system's interface, tick contract, and component schema against
  the frozen contract.

# skeleton-antagonist.md
name: skeleton-antagonist
model: opus            # sonnet on routine lanes
tools: Read, Grep, Glob
description: >
  Attack a skeleton for scripting, hidden coupling, shape divergence, up/down
  asymmetry, order-dependence, and cross-scale feedback loops. Read-only.

# system-infill.md
name: system-infill
model: sonnet
tools: Read, Grep, Glob, Write
isolation: worktree
description: >
  Implement one system's local rule against the frozen interface. Local rule
  only; declared I/O only; no special-casing of entities or outcomes.

# boilerplate.md
name: boilerplate
model: haiku
tools: Read, Write
description: >
  Mechanical, near-identical template code (component structs, serialization,
  data tables) from an unambiguous spec.

# synth.md
name: synth
model: opus            # fable if deep/rich
tools: Read, Grep, Glob, Write
description: >
  Assemble the scale ladder over compressed lane summaries; verify up/down
  propagation and cascade convergence.

# emergence-auditor.md
name: emergence-auditor
model: fable           # opus if zero-data-retention is required
tools: Read, Grep, Glob
description: >
  Independent adversarial audit: emergence fidelity, propagation determinism,
  convertibility, runaway-cascade detection. Runs seeded headless sims and
  ablation. Read-only, independent of producers.

# conformance-scanner.md
name: conformance-scanner
model: haiku
tools: Read, Grep, Glob
description: >
  Deterministic schema/contract check over every container and wrapper.
  Report divergences only.
```

---

## 7 — Economy, and the two warnings

**Scale the apparatus to the systems web, not the game's ambition.** The tiering and the five-stage structure pay off in proportion to *ladder depth × propagation richness*. A shallow ladder with one-directional-dominant propagation — or a systems web that fits one Sonnet 5 window over a run of hours — does not need this: freeze the contract with one Opus pass, run Stages 1–3 in a single Sonnet 5 session, and spend the saved budget on a heavy Stage 5. For emergent play the audit is the part you cannot compress, because it is the only stage that proves the game emerges rather than pretends to.

**The method warning — carried forward, unresolved.** Anthropic's documented best practice is itself bottom-up: start with conversational prompts and CLAUDE.md, and let the roster emerge from recurring friction — promote a role into `.claude/agents/` only once you have repeatedly needed it. This spec does the opposite: it lays out the full ensemble before a line of the game exists. The contradiction is exact — the tool's own guidance is emergent, and so is your design axiom, yet the build plan is top-down. The disciplined path: write the canonical contract, build two or three systems in one session with a single Opus audit pass, and let the roles that genuinely recur (a standing conformance scan, a persistent emergence audit) reveal themselves — then adopt only those from §6. **Treat §4 and §6 as the shape the workflow may grow into, not the shape to impose on day one.** `[ASSUMPTION: the systems web's size was never established across the session — the over-build risk is real until it is]`

---

## 8 — Open items to verify

- Built-in Explore (Haiku) / Plan subagents — `[UNVERIFIED, T3]`; check your `claude` release notes.
- Exact current prices for all four models — verify at the Anthropic pricing page (T0); circulating figures are T2/T3.
- Sonnet 5 context window — `[UNVERIFIED]`; presumed 1M (Sonnet 4.6 was), confirm.
- Opus 4.8 zero-data-retention support for your account/tier — `[UNVERIFIED]`; the solid fact is that Fable does *not* support ZDR.
- Whether the systems web actually exceeds one session — undetermined; this decides whether the spec applies at all (§7).

---

## 9 — Provenance (load-bearing facts)

| Fact | Tier | Source |
|---|---|---|
| Lineup Fable 5 > Opus 4.8 > Sonnet 5 > Haiku 4.5; Sonnet 5 supersedes 4.6; effort defaults high | T1 | platform.claude.com models overview |
| Fable 5 suspended 06-12, restored 07-01 across Claude.ai/Platform/Code/Cowork | T1 + T2 | anthropic.com/news/fable-mythos-access; CNBC; The Hacker News |
| Fable 5 no ZDR / 30-day retention | T1 | anthropic.com/news/fable-mythos-access |
| Fable 5 subscription = 50% weekly usage through 07-07; API uncapped | T2 | CNBC |
| Fable 5 has cyber/bio/chem safeguards that fall back to Opus | T1 | anthropic.com/news/fable-mythos-access |
| The "<5% of sessions" figure and exact domain list (incl. distillation) | T2/T3 | secondary coverage — approximate, not confirmed at T1 |
| Subagents stateless/isolated, no inter-agent comms; `model:` aliases sonnet/opus/haiku/fable; description-driven routing; tool restriction; `isolation: worktree`; Agent Teams for dialogue; start-simple best practice | T1 | code.claude.com/docs subagents; claude.com/blog subagents |
| Exact prices; Sonnet 5 window; Opus ZDR-by-tier; built-in Explore/Plan | — | **unverified — see §8** |

*Tiers: T0 primary · T1 authoritative synthesis · T2 reputable secondary. T3 aggregator/SEO sources were used only for navigation and are not cited as evidence.*

