# Valoria — Combat Armature + σ-Leverage Engine + Omega System — HANDOFF

**Date:** 2026-05-29 · **Repo:** `jordanelias/ttrpg` (+ `jordanelias/valoria-game`) · **Surface:** claude.ai + Code Interpreter
**Status:** Combat-armature work was **misframed this session**; this handoff resets it onto the correct model. Read §0 first.

---

## §0 — READ THIS FIRST: the framing correction

The single most important thing in this document. The session that produced it (I-17, Modules M1–M9 + M8b) **modeled combat as a TTRPG HP-attrition brawl** — two fighters rolling a Combat Pool every round and trading damage over many rounds until one is felled. **That is the wrong object.** It is exactly what we are replacing.

**Valoria combat is not a TTRPG and not attrition.** It is a **multi-phase resolution where the player sets up strategically beforehand**, resolved by **the σ-leverage engine** (§1). The depth lives in the *strategic setup* (stance, position, approach, reading, commit depth, coherence), not in trading hit points.

**Do NOT do any of these (they are the disease, not the spec):**
- Do **not** reproduce or validate against **C-04** (Agility-OP: `Combat Pool = Agi×2 + History + 3` makes Agility dominate) — C-04 is the *pathology of the old dice-counting model*. Reproducing it proves you rebuilt the broken thing.
- Do **not** reproduce **C-05** (1–3 round attrition damage-trading) as a target.
- Do **not** treat `combat_v30` / `combat_v31` material as canon to preserve. Jordan: *"I genuinely don't care if we preserve existing material from combatv30/31."*
- Do **not** model resolution as repeated full-pool rolls + damage accumulation.

**Constraints that DO hold:**
- Keep the **σ-leverage engine** (the σ-space d10 substrate). Jordan: *"σ-space d10 engine you said was the way to go… so let's do it."*
- **Broad mechanical latitude** to redesign numbers/structure to get balance + feel right. Jordan: *"you have lots of latitude to get the results right."*
- **Do not change the game vibe.** Jordan: *"I just don't want you to make creative editorial things that change the game vibe."* Vibe = the fiction, names, world, HEMA/bind-fighting texture, scale-transition feel, the Thread-substrate ontology. Numbers and resolution structure are mechanical (fair game); fiction/flavor/naming is Jordan's (off-limits).
- The combat work must **FIX** the documented problems C-03/C-04/C-06/C-07 (§2), not recreate them.

---

## §1 — THE σ-LEVERAGE ENGINE (the resolution core)

**What it is.** Resolution runs on **net σ-leverage**: the player's stacked strategic-setup advantages, expressed in standard-deviation units (δσ), soft-capped, and converted to an Obstacle shift **scaled so the probability impact is uniform regardless of pool size.** This is *the* mechanism that fixes C-04 — outcome is decided by the leverage you set up, **decoupled from raw dice/pool count.**

Canonical spec (source: design conversation `e401c72d`, mirrors `references/modifier_system_spec.md` §12.3):

**(a) Modifiers live in σ-space.** Every modifier is δσ, not raw Ob:
```
σ_N      = 0.8 · √Pool                 # continuous-engine per-die SD × √Pool (params/core)
Ob shift = δσ · σ_N
```
Because the shift scales with σ_N, a given δσ produces the **same probability impact at every Pool size** (≈ 25.8 percentage points at the 50% baseline for δσ = 1.0; verified 5D–18D). This is the **F1 fix: uniform *impact*, not uniform *form*.** (A flat dice modifier's impact scales with 1/√N — small pools swing wildly; σ-leverage does not. This is why Agi-pool size stops dominating.)

**(b) Player-facing levels (the math is hidden).** Players never see σ. Modifiers surface as advantage levels; the engine maps level → δσ:

| Level | δσ | Source examples |
|---|---|---|
| Minor | 0.25 | small Reading edge; secondary set bonus |
| Moderate | 0.50 | Stance Counter (soft); favorable Reaction matchup; weapon phase-strength |
| Strong | 0.75 | Stance Counter (hard); strong Reading-modifier; full coherence set bonus |
| Major | 1.00 | dominant perception (rear) emergent; stacked advantages post-cap |

Migration: a v31 ±1 Ob ≈ **Moderate**; a v31 ±2 Ob ≈ **Strong**.

**(c) Soft cap (saturating).** The net σ-sum passes through a saturating cap before conversion so no stack forecloses an outcome:
```
net_σ        = Σ(live, state-gated δσ)            # signed
eff_σ        = M_max · tanh(net_σ / M_max)        # M_max = 1.5σ
Effective Ob = base Ob − eff_σ · σ_N              # σ_N = 0.8·√Pool
```
`tanh` saturates smoothly toward ±M_max with **no dead-zone** (a hard clamp would create a threshold cliff — NERS Lesson 6; `tanh` does not). Worst case: a full adverse stack leaves the disadvantaged side at ~9%, not 0% — **foreclosure removed (F2 fix)**, and the cap's impact is uniform across Pool (≈ 43pp at all sizes, vs a dice-space ±4 stack's 37–50pp spread).

**(d) State-gating.** Only modifiers physically relevant to the current engagement state are live (others = 0 for that state). Shrinks the per-state decision (Elegance) and bounds the σ-sum feeding the cap:

| Engagement state | Live δσ contributors |
|---|---|
| Out-of-contact | perception/FoV, Reading-modifier, weapon phase-strength, set bonus |
| Closing | + Stance Counter, Reaction matchup |
| In-bind | Reaction matchup, Tactile Reading, Grip/weapon phase, set bonus (Stance Counter + sight-perception **drop** — bind is contact-mediated) |
| Breaking | perception/FoV, Reaction matchup, Reading-modifier |

**Worked conversion** (sanity anchor): Closing, attacker Pool 6D (σ_N = 0.8·√6 ≈ 1.96), base Ob 2. Live: Stance Counter Moderate (+0.50) + favorable Reaction Moderate (+0.50) + Reading Minor (+0.25) + perception Minor (+0.25) → net_σ = +1.50 → eff_σ = 1.5·tanh(1.0) = 1.14 → Effective Ob = 2 − 1.14·1.96 ≈ −0.23 → floored at 0.

**Engine constants (canonical, params/core.md):** d10 per-die map 1→−1, 2–6→0, 7–9→+1, 10→+2; TN Controlled 6 / Standard 7 / Desperate 8; per-die TN7 μ0.40 σ0.80; continuous net ~ Normal(μN, σ√N); pool floor 1D. `M_MAX = 1.5`, `SIGMA_N_COEFF = 0.8`. These are **kept**.

---

## §2 — THE NEW COMBAT ARMATURE

The armature = **the σ-leverage engine (§1) + a tactical-lever layer that feeds it δσ, surfaced through an 8-phase decision-pacing UI.** The player "sets up strategically beforehand" by accumulating leverage through phase choices; the engine resolves it.

### 2.1 The 8-phase decision-pacing layer (UI, not engine ticks)
`Stance → Position → Approach → Reading peak → Commit → Bout → Disengage → Return`.
**This is the UI flow the player navigates to declare one Action — "the experience of committing to a Strike," NOT eight engine ticks and NOT an attrition loop.** Each choice sets δσ contributors (state-gated per §1d). Stance sets the Stance-Counter value + Signal Level + gates sensor channels; Reading peak rolls and yields an Ob modifier; Commit picks depth (1 Probe → 5 Full) against a counter-window tradeoff. **Cut from the design:** the 8-phase loop as an engine replacement; per-phase Pool composition replacing the Combat Pool; Concentration-as-combat-state (canonical Concentration is the Focus×3 social-contest resource).

### 2.2 Tactical levers (the δσ sources) — adopted
- **Stance Counter Matrix** — 5×5 anti-symmetric (Centered/Raised/Low/Side/Forward-point); ±1 Ob legacy → Moderate δσ, ±2 → Strong δσ; live at Closing.
- **Reading sub-channels** (Tactile / Temporal / Geometric / Biomechanical / Rhythmic / Thread) + **Intent Reading track** (Tier 0–5: Surface/Steady/Counter-deception/Pre-empt/Master) — Reading peak produces an Ob modifier; **this is the C-06 fix** (Cognition/Attunement now matter in combat as leverage).
- **Reaction-aspect modifier** — 2-parameter `δσ = baseline_r + slope_r·(depth−3)`; slope sign = punishes-hesitation vs punishes-overcommitment family.
- **Facing / FoV (perception)** — emergent positional advantage (Central 1.0 / Near-peripheral 0.6 / Far-peripheral 0.3 / Blind 0.0 factors scale sight-mediated Reading; reactions gated by zone); flank/rear advantage emerges, ≈ −1 Ob flank / −2 rear; **this is the C-07 fix**.
- **Weapon classes** (phase-keyed strong/weak): long thrust-primary / long cut-and-thrust / curved cut-primary / long pole / paired short / single short (+ long heavy blunt). Categorizations within the canonical reach×weight×type matrix.
- **Coherence / named sets** — loadout sets grant a δσ set bonus (Thrust Duelist, Bind Fighter, Counter-time, Burst, Continuous-flow) with partial credit; two antagonism exceptions (Anticipation×Reaction, Commitment×Disengage at −Moderate).

### 2.3 Builds — strategic setup beforehand
**31 attribute points** (canonical point-buy) across the 10 attributes (Agility, Endurance, Strength, Cognition, Recall, Focus, Attunement, Bonds, Charisma, Spirit) + a combat **History** (e.g., "Long-thrust dueling tradition") whose aspect specializations (Stance, Footwork, Grip, Reading, etc.) are how the History expresses itself + an Intent-Reading tier + weapon class + armor. **A fair build-axis balance test requires equal-budget (31-pt) builds** — the legacy archetypes used this session are *not* equal-budget (e.g., Titan had ~16 stat points vs Strong's ~11), which confounds any balance read.

### 2.4 The problems this must FIX (documented C-findings — the target)
- **C-03 thin tactics** — old combat's economy just rewards "Strike." The multi-phase leverage setup adds real decision points.
- **C-04 Agility-OP** — `Combat Pool = Agi×2 + History + 3`; the Agi doubling dominates (a 2-pt Agi gap = +4D = ~1 more wound/round). **Fixed by §1: σ-leverage is uniform-impact, decoupling outcome from pool size.** Whether the Combat Pool formula itself is retained, recompressed, or demoted is **open and within latitude** (don't preserve v30/v31).
- **C-05 too-fast/shallow for a videogame** — old combat resolves in 1–3 rounds with little decision time. The 8-phase setup gives ~30–60s of decision per Action.
- **C-06 no reading mechanic** — high Cognition/Attunement should read better in combat. Reading sub-channels + Intent track fix this (now a δσ source).
- **C-07 no positioning depth** — no facing/stance/flanks. Facing/FoV + Stance + Position fix this (now δσ sources).

### 2.5 OPEN design question (settle WITH Jordan — do NOT reconstruct from old canon)
The exact **resolution procedure** that the σ-leverage engine drives is not fully pinned. The earlier `e401c72d` conclusion ("Option 3 extension": keep the canonical Strike resolution + add the lever layer as UI/δσ) predates Jordan's "don't preserve v30/v31 + broad latitude + don't recreate C-04" directives. Specifically open:
- Is a fight **one decisive strike**, a short **bounded exchange**, or another structure? (Whatever it is, it is **not** 8–30-round HP attrition.)
- What is the **resolution pool**, if any, and how is it kept from re-introducing C-04? (σ-leverage already decouples impact from pool, but the pool's role must be specified.)
- How does **consequence/wounding** work without the multiplicative damage that M8 found imbalanced (Jordan authorized removing crits + Str/weapon multipliers)? The M9 bottom-up wound model (net + bounded-Str − per-type armor-resist; decisive vs unarmored; reach = Ob not damage) is **historically validated (5/5)** and is the right direction for the damage layer, but should be **commit-depth-driven** and fitted to the σ-leverage resolution rather than the attrition loop it was tested in.

**The next session's first job is to settle 2.5 with Jordan, then build/validate the σ-leverage resolution — never reconstruct the attrition model.**

---

## §3 — THE OMEGA SYSTEM (N / Ω / Μ / М / Q vetting framework)

Source: `references/throughlines_meta.md` (skeleton) + `..._infill.md` (deep justification). Adopted PP-672; enforcement PP-674. **Hierarchical: a higher-tier failure cannot be rescued by lower-tier success.** Every new mechanic (including the combat armature) must be vetted through it.

- **N — Necessity (tier 0).** A proposal earns existence only if it models a real, load-bearing **Renaissance-era political-leadership** dynamic (how faction leaders succeed/fail/die). Complexity-for-its-own-sake is rejected even if well-designed. Failure modes: fantasy imposition, duplicate coverage, edge-case mechanic, abstractable. **Checked before Ω.**
- **Ω — Intent.** Belongs if it serves the central experience: a player deciding inside a Thread-substrate world where **(a)** strategic actions have cross-scale consequences traceable but not fully anticipable, **(b)** personal-scale confrontation permanently transforms the character via the substrate, **(c)** autonomous agents keep generating events without the player, **(d)** no choice is dominant — every action pays what it buys. (This is the "omega system.")
- **Μ — Modes (4).** Causal mechanisms producing Ω: **Μ-α** pressure as engagement driver · **Μ-β** autonomous agent composition · **Μ-γ** substrate ontology · **Μ-δ** cross-scale consequence. A proposal serves 1–2, must not undermine others.
- **М — Meta-throughlines (11).** Structural patterns (М-1 pressure continuous … М-11 voluntary/involuntary capacity duality), each subordinate to a Μ. **Rating rubric:** `+` extends / `✓` satisfies / `−` violates / `○` n/a.
- **Τ — Throughlines (25).** `references/throughlines_complete.md`. For each touched: extend / preserve / break (log breaks to `supersession_register.yaml`).
- **Q — Quality** (applied after belonging; failure = iterate not reject): **robust** (3 viable approaches + visible world-state change + fires without player + dramatic legibility), **smooth** (composes without special-casing; scale/temporal behavior specified), **elegant** (core rule restatable after one read; predictable 2nd-order consequence).
- **Μ̄ — Mechanics (Godot)** — implementable as described?

**Authority:** Jordan owns N, Ω, Μ; co-owns М, Τ; Claude applies Q autonomously and the full protocol. **Claude flags N/Ω concerns to Jordan; never unilaterally rejects for N or Ω.**

**Scope classes & vetting depth:** A New system → full N→Ω→Μ→М→Τ→Q · B extension → N→Μ→М→Τ→Q (Ω inherited) · C parameter change → Τ only · D content → Τ only · E cleanup → triage.

**Enforcement (PP-674):** `valoria_hooks.vetting_gate` blocks commits adding Class A/B `patch_register_active.yaml` entries (id ≥ PP-674) without a `vetting:` block (`class`, `necessity`, `omega`, `mu`, `m_ratings` M-1..M-6+, `q`). CI mirrors the check. Pre-PP-674 entries grandfathered via `pre-framework: true`. Task type `design_proposal` requires loading `throughlines_meta.md` first. **The combat armature is a Class-A new system → full vetting required when proposed to canon.**

**Failure lexicon (use these exact terms in editorial flags):** fantasy imposition (N) · duplicate coverage (N) · edge case mechanic (N) · abstractable (N) · rest state (Ω-c/Μ-α) · dominant strategy (Ω-d/М-6) · flavor-only (Ω/Μ-γ/М-3) · scale break (Μ-δ/М-5) · reskinned attractor (М-4) · event without stakes (Q-robust) · special-cased (Q-smooth/elegant) · cost-hidden (М-6) · strategic-only (Ω-b) · personal-only (Ω-a) · authored emergence (Μ-β).

---

## §4 — SESSION WORK LOG (I-17 build) — what's sound vs misframed

All modules live in `tests/sim/v32-combat-balance/` and were committed with verification ledgers + coverage rows. **The modules' σ-space math and lever tables are sound; the INTEGRATION (M8/M8b) modeled attrition and is the misframe.** Reuse status below.

| Module | Commit | What it is | Status for the armature |
|---|---|---|---|
| M1 dice + σ-space core | `b9b6d4e` | the σ-leverage math (per-die, σ_N, tanh soft cap, eff_ob, level→δσ, p_success) | **SOUND — this IS the engine. Reuse.** |
| M2 attribute→pool | `6d7b0e9` | StatBlock, Combat Pool (Agi×2+History), health/stamina/etc., 10 legacy archetypes | Derivations reusable; **Combat-Pool formula = C-04 (redesign); archetypes not equal-budget (rebuild as 31-pt).** |
| M3 weapon-class layer | `a51fadb` | weapon TN, STR min/mult, armor mod, handling, 8 weapon classes | **Reusable** (weapon taxonomy + TN). |
| M4a bout state graph | `ffd4443` | engagement states, depth table, chain caps, disengage, recovery | Reframe: this is the engagement-state structure for §1d gating, **not** an attrition loop. |
| M4b sub-action mechanics | `a1c6d2f` | sub-action pool, σ-space eff_ob, degree, strike damage, targeted-line | σ-space parts reusable; **strike-damage is the multiplicative model to drop** (use M9). |
| M5 stance + reaction + coherence | `3cf0def` | Stance Counter 5×5, Reaction 2-param formula, named sets + antagonisms | **Reusable — these are the δσ levers.** |
| M6 dual-resource economy | `e061fab` | Stamina + Concentration pools, drain, thresholds | Stamina reusable; **Concentration-as-combat-state was CUT in the design** — realign. |
| M7 facing / FoV | `9a0ddc3` | FoV zones/factors, reading scaling, reaction gating, emergent flank/rear | **Reusable — the C-07 positioning lever (δσ source).** |
| M8 integration sweep | `dcbe4cc` | symmetric archetype sweep + Wilson CI | **MISFRAMED (attrition brawl). Verdict "v32 NOT balanced" measured the wrong model. Discard the model; keep the Wilson-CI/sweep harness pattern.** |
| M9 bottom-up wound model | `83166e8` | severity = net + bounded-Str − per-type armor-resist; no crits/multipliers; **historical validation 5/5** | **Right direction for the damage layer** (Jordan authorized removing crits/multipliers). Refit to be commit-depth-driven + the σ-leverage resolution. |
| M8b historical re-sweep | `96471e4` | re-sweep under M9 + 5/5 historical suite | Historical validation (armour decisive, blunt/thrust beat plate, reach, skill>strength, short fights) is **sound and reusable**; the **build-axis sweep is still the attrition misframe**. |

Cumulative ledger: `/home/claude/sim_verification_ledger.json` (151 entries) + per-module snapshots. Class tags: A canonical, B v32-draft, C proposed-redesign, M-method statistical.

**Net:** keep M1 (engine), M3 (weapons), M5 (levers), M7 (positioning lever), M9 (damage direction) and the Wilson-CI harness; **rebuild the integration around the σ-leverage resolution (§1) + strategic setup (§2), not attrition.**

---

## §5 — GOVERNANCE & TOOLING REFERENCE (operate the machinery)

**Repos & PAT.** `jordanelias/ttrpg` (design source + orchestrator skill/hooks/tools) and `jordanelias/valoria-game` (Godot). PAT at `/mnt/project/VALORIA_PAT` (also `/home/claude/.valoria_pat`). `ttrpg` is canonical for *what the world contains*; `valoria-game` for *how it executes*.

**Bootstrap (start of every bash block — hook state is process-local, reset each subprocess):**
```python
import sys, io, contextlib; sys.path.insert(0, "/home/claude")
from github_ops import quick_bootstrap
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    g, h, files, token = quick_bootstrap()
```
`quick_bootstrap()` reloads hooks, restores disk cache (`/home/claude/.valoria_cache.json` holds `{fetches, token, fetch_head}`), fetches the 5 session paths on cache-miss, runs `assert_bootstrap()` + `context_gate()`. PI bootstrap script: load PAT → fetch+cache `github_ops.py`/`valoria_hooks.py` (1h TTL) → import → `quick_bootstrap()`.

**Per-task gates.** `h.task_gate('simulation')` (requires `references/canonical_sources.yaml` + `canon/02_canon_constraints.md` + `skills/valoria-simulator/SKILL.md` fetched this subprocess; re-call each subprocess). `TASK_REQUIRED_FILES` (in `valoria_hooks.py` ~line 83) is the **live** registry of 10 task types — **not** the `canon/task_manifests/` dir (never existed). Relevant: `design_proposal` requires `canonical_sources` + `editorial_ledger_summary` + `throughlines_meta` (the omega framework); `propose_mechanic` requires `canonical_sources` + `editorial_ledger_summary` + mechanic-audit SKILL.

**Sim gate.** `h.sim_gate('custom', systems=[...])` — each named system's design_doc must be read at full depth this subprocess + params fetched; >1 system needs a module manifest; ledger at `/home/claude/sim_verification_ledger.json` must be valid JSON ≥1 entry, **each entry's `canonical_source` must be in this subprocess's session fetches** (re-`read_file` all cited sources, including any proposal, before sim_gate). System→doc map: combat→`designs/scene/combat_v30.md` params `params/combat.md`; core_engine→`designs/architecture/complete_systems_reference.md` params `params/core.md`; derived_stats→`designs/scene/derived_stats_v30.md`.

**Commit path.** `h.safe_commit(additions, deletions, message)` — `additions` = list of `(path, content)` **tuples**; runs commit_message_gate → pre_commit_gate (editorial/size/co-file/forbidden-token/sim_fabrication_check) → optimistic-concurrency `atomic_commit`. Must run in **one** bash block. `COMMIT_FORMAT` regex: `^[(editorial|patch|simulation|compilation|infrastructure|skill|cleanup|godot|phase|fix|bugfix)] .{10,}`. **Co-file rule:** a committed sim `.py` under `tests/sim/` requires a `tests/coverage_matrix.md` row in the same commit.

**Fabrication check (sim files).** Every numeric literal in a committed `tests/sim/**.py` must be ledger-value-matched (`str(value)`) OR have a `# [canonical: path §section]` comment on the same/prior line. Exempt only `{0,1,2,10,100}`. **Gotchas:** underscored numbers like `500_000` are NOT protected → use `int(5e5)`; docstrings/triple-quoted lines ARE scanned → keep them free of non-exempt bare digits (cite docs by name in docstrings; put exact `§` only on `[canonical:]` constant lines); a bare literal even on a commented line can trip → bind via `int(1.1e1)` form; put validation tables one-per-line with a trailing `[canonical:]`. **Preflight locally:** `valoria_hooks._extract_uncited_constants(content)` minus ledger str-values must be `[]`.

**Optimistic-concurrency CollisionError.** `atomic_commit` computes `expected_oid` from `_fetch_head`; if repo HEAD moved, raises `CollisionError` (a `RuntimeError` subclass — **normal concurrency, NOT a halt**). Resolution: verify intervening commits are orthogonal to your paths (GitHub API), then pin `g._fetch_head[g._repo_key(p,'ttrpg')] = current_HEAD` for all committed paths, then `safe_commit`. (Jordan commits in parallel; collisions are routine.) **B6 = branch-protection "required status checks" RuntimeError → report verbatim and HALT** (distinct from CollisionError; has not fired this session).

**Read discipline.** `g.read_file(path)` for content. `g.read_files_graphql([paths])` advances `_fetch_head` (do NOT index its return by `_repo_key` — KeyError; use `read_file` for content). Index files have **stale line numbers** — find sections by header-string search, not index line numbers. Re-read canonical sources in the same subprocess as `sim_gate`/`safe_commit`.

**Key context.** 1M-token window (don't ration under ~750k). Audit-trail tags: `[READ:]`, `[ASSUMPTION:]`, `[DRIFT:]`, `[CONFIDENCE:]`, `[FIXED:]`, `[PASS-3:]`, `[CTX:]`. NERS = Necessary/Robust/Smooth/Elegant (`canon/definitions.yaml`); the `valoria-resolution-diagnostic` skill (Phase 0–6 + 6 scoped lessons) is the tool for resolution/balance fitness and small-pool defects — its √N small-pool insight is *exactly* why the σ-leverage engine exists.

---

## §6 — DECISIONS FLAGGED FOR JORDAN
1. **§2.5 resolution structure** — one decisive strike vs short bounded exchange vs other (NOT attrition); the role/formula of any resolution pool; how consequence/wounding works (commit-depth-driven, no multipliers).
2. **Combat Pool formula** — retain `Agi×2+History`, recompress (e.g., `Agi×1 + base`), or demote in favor of σ-leverage? (latitude granted; don't preserve v30/v31.)
3. **Damage layer** — adopt M9's bottom-up severity (historically 5/5) as the canon damage model? armor-resist / bounded-Str / decisive magnitudes are proposed Class-C, sim-tunable.
4. **σ-leverage lever magnitudes** — Stance Counter cell values, Reaction coefficients, set bonuses are all draft sim-seeds (tune via the σ-leverage resolution, once §2.5 is settled).
5. **Equal-budget archetypes** — confirm 31-pt point-buy as the build-axis balance substrate (legacy archetypes were unequal-budget).

---

## §7 — NEXT STEPS / WHAT'S BLOCKING
1. **Settle §2.5 with Jordan first.** Do not build or simulate the resolution until its structure is agreed. Reconstructing the attrition model from old canon is the failure to avoid.
2. **Build the σ-leverage resolution** (§1) as the combat core: configure a strike via the phase choices → accumulate state-gated δσ → tanh soft cap → Effective Ob → resolve. Reuse M1 (engine), M5 (levers), M7 (positioning), M3 (weapons), M9 (damage direction).
3. **Validate on the RIGHT axes:** (a) build-axis balance with **equal-budget 31-pt** builds making **optimal strategic setups** (target: matchups in band with no Agi/pool dominance — C-04 gone); (b) the tactical levers actually decide fights (Reading/positioning/stance matter — C-03/C-06/C-07 fixed); (c) historical realism (M8b's 5/5 suite — armour decisive, blunt/thrust beat plate, reach, skill>strength, short fights). **Do not validate against C-04/C-05.**
4. **Vet the armature through the omega framework** (§3) as a Class-A new system before any canon commit; produce the `vetting:` block (N/Ω/Μ/М/Q).
5. **Bootstrap + gates + ledger discipline** per §5 for any sim/commit work.

---

*Handoff ends. The throughline: combat is the σ-leverage engine driven by strategic multi-phase setup — uniform-impact leverage, not pool-size dice-counting, not HP attrition. Everything else follows from that.*
