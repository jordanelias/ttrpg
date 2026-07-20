I have firsthand-verified every load-bearing formula, engine choice, Ob construction, and degree ladder across all seven subsystems, plus the Thread sim-engine drift (`sim/thread/operations.py:40,140` — imports only `roll_pool`, Overwhelming = `net ≥ ob+3`). Here is the deliverable.

---

# Valoria — Cross-Shape Coherence / Divergence Map

*How each resolving subsystem shapes its core mechanics, and where a player moving between them would find their intuition rewarded (coherent), deliberately surprised (divergent-by-design), or silently misled (divergent-by-drift).*

**Canonical anchor** (the reference every row is measured against): the current Combat Pool is **`max(5, Relevant History + 6)` — Agility-INDEPENDENT** (`designs/scene/combat_engine_v1/core.py:27-32`; `params/core.md:161`), ratified ED-901/900/904, explicitly superseding the struck **`(Agility × 2) + History + 3`** form. The shared core also defines the general Ob scale (1–20, `params/core.md:32-55`), the four-tier degree ladder (`params/core.md:46-55`), and the TN ladder 6/7/8 (`params/core.md:23-30`). Engine classifications follow the resolution-diagnostic Decision Rule (`skills/valoria-resolution-diagnostic/SKILL.md:144-155`): *pool ≥ ~5D + setup axis → A (sigma-leverage); bare-stat 1–7 pivotal → B (deterministic+stochastic); aggregable → aggregate then A; ambiguous → C.*

*All paths are repo-relative to `/home/user/ttrpg/`. Currency verified against `CURRENT.md` (2026-07-08). Note: Fieldwork has **no row in `CURRENT.md`'s head table** and **no NERS lane audit** — a gap flagged below.*

---

## 1. Pool-formula shape

| Subsystem | Exact pool formula | Attr-multiplied or flat-History? | Matches CURRENT combat `max(5,H+6)`? | Self-claimed match? | Citation |
|---|---|---|---|---|---|
| **Personal Combat** | `max(5, Relevant History + 6)` | **Flat History floor** (Agility-independent) | — *(this IS the canonical shape)* | n/a (the anchor) | `core.py:27-32`; `params/core.md:161` |
| **Social Contest / Argue** | `(Primary Attribute × 2) + History bonus` (attribute = Cog/Cha/Att by adjudicator; History bonus = points + 3) | **Attribute-multiplied** | **No** — this is the **OLDER `(Attr×2)+H+3`** shape | **Correctly self-disclaims**: "comparison column, not a shared formula" (`social_contest_v30.md:490`); "the analogy no longer holds… stands on its own" (`params/contest.md:277-279`) | `social_contest_v30.md:119`; `params/contest.md:16-22` |
| **Fieldwork** | `(Primary Attribute × 2) + History bonus` (identical to Contest) | **Attribute-multiplied** | **No** — OLDER `(Attr×2)+H+3` shape | ⚠️ **FALSELY claims to match combat**: "consistent across Combat (PP-615), Contest, and Fieldwork" (`designs/scene/fieldwork_v30.md:61`); "matching Combat Pool… construction" (`params/core.md:252`) — **both stale**, combat abandoned `Attr×2` at ED-901 | `fieldwork_v30.md:57-61` |
| **Mass Battle** (engagement) | live: `2 × Command` (smooth `Command × (1 + cohesion)`); legacy PP-233: `min(Size,Command) + Command`. Command `= clamp(round((2·Cha + Cog)/3),1,7)` | **Command-multiplied** (Command itself a Cha/Cog blend) | **No** — Command-driven, not History | n/a (its own model; engine-led per ED-899) | `params/mass_combat.md:60-79,139` |
| **Faction Domain Actions** | **No dice pool.** `M = acting_stat − difficulty`; `P_success = clamp(0.50 + 0.10·M, 0.05, 0.90)`; draw `r ~ U[0,1)` | **Neither** (bare-stat margin; pool abolished) | **No** — deterministic+stochastic, no pool at all | n/a (explicitly supersedes the bare-stat pool, ED-874) | `params/factions/stats_1_7_scale.md:56-97` |
| **Thread operations** | `(Spirit × 2) + History + TPS` (TPS = TS÷10; History cap 3, +3D floor) | **Attribute-multiplied + Thread term** | **No** — `(Attr×2)+H` family, plus TPS | n/a (own unified formula, PP-616) | `params/threadwork.md:18-24` |
| **Board Game** (generic) | legacy `d10 pool` = relevant stat as dice, TN 7 | **Raw-stat pool** | **No** — legacy raw-d10 | n/a (TTRPG-mode retention; faction actions route to the d+σ resolver) | `params/bg/core.md:51-62` |

**Player-expectation collisions (explicit):** Combat, Contest, and Fieldwork are all "personal-scale skill checks" and a player will expect one pool rule. In fact **Contest and Fieldwork agree with each other** (`(Attr×2)+H+3`) — they are frozen in the *pre-ED-901 combat shape* — while **Combat alone** now uses the flat, Agility-independent `max(5,H+6)`. Worse, **Fieldwork's own doc still asserts it matches Combat** (`fieldwork_v30.md:61`, `params/core.md:252`), a claim that was true before 2026-05-29 and is now false. The sharpest irony: **Thread**, the system meant to feel *alien*, uses `(Spirit×2)+History+TPS` — the same `Attr×2 + History` base — so its pool is **closer to Contest/Fieldwork than Combat is to either of them.**

**So what for the player:** the three systems a player will most readily conflate ("I roll a skill pool") do not compute their pool the same way — a player who learns "pool = attribute×2 + history" in a debate or an investigation will silently compute the *wrong* pool the moment they draw a weapon, because combat is the one that moved. And a Godot importer trusting Fieldwork's or `params/core.md`'s "matches Combat Pool" self-description would transcribe an attribute-multiplied combat pool that no longer exists.

---

## 2. Engine choice (NERS instance)

| Subsystem | NERS instance | Basis | Right per Decision Rule? | Note |
|---|---|---|---|---|
| **Personal Combat** | **A** (sigma-leverage) | PC lane report "Rolling-engine verdict (Instance A)"; `core.py:47-53` `resolve()` = `roll_net + soft_cap(net_sigma)·sigma_n(pool)` | ✅ **Correct** (pool 5–18D + setup axis: tradition, initiative, poise, grip) | Lane "NON-COMPLIANT" is *legibility-contract debt*, not wrong-engine |
| **Social Contest** | **A** (sigma-leverage, δσ, TN 7) | SC lane report Instance A; CR2 substrate `params/contest.md:160` (single-sourced with combat via `sigma_leverage.py`) | ✅ **Correct** (healthy pool + stance/Appraise/armature axis) | Kernel at `sim/personal/contest/` |
| **Fieldwork** | **A by rule — but unmigrated & unaudited** | No NERS lane report exists; its own docs describe roll-pool-vs-Ob, count-successes (raw-d10 shape), `fieldwork_v30.md:57,217` | ⚠️ **Unverified** — *should* be A (pool ≥5D + History/Inspiration/concealment axis), but reads as **legacy raw-d10** and is not indexed in `CURRENT.md` | Latent Lesson-3 (wrong-engine) risk; genuinely unowned |
| **Mass Battle** | **A** (aggregated) | MB lane report "Instance A (aggregated sigma-leverage)"; SKILL "keep dice for aggregated mass battle" | ✅ **Correct** ("aggregable → aggregate, then A") | Volley sub-pool = bare Power stat at TN 6 (`params/mass_combat.md:236-237`) is a small dice exception |
| **Faction Domain Actions** | **B** (deterministic+stochastic) | FA lane report Instance B; `stats_1_7_scale.md:56-97` (ED-874) | ✅ **Correct** (bare-stat 1–7, pivotal, no aggregation → B) | The model migration off legacy bare-dice |
| **Thread operations** | **design intends A; sim runs LEGACY raw-d10** | TW lane report "NON-COMPLIANT — wrong engine class"; verified `sim/thread/operations.py:40` imports **only** `roll_pool` (not `sigma_leverage`); `_compute_degree` Overwhelming = `net ≥ ob+3` (`:140`) | ❌ **Mismatch** — should be A; is legacy raw-d10 with an uncited divergent degree formula | The clearest wrong-engine defect in the corpus |
| **Board Game** (generic) | **legacy raw-d10** | `params/bg/core.md:51-62`; SKILL flags videogame raw-d10-vs-Ob as a wrong-engine pattern | ⚠️ by-design TTRPG-mode retention; anything *pivotal* should route to B (as faction actions do) | Faction actions inside BG → Instance B |

**Legacy / wrong-engine callout:** two live surfaces run the exact raw-d10-vs-flat-Ob pattern the diagnostic skill flags as a videogame defect: **Thread** (by *drift* — the design claims the shared sigma-leverage substrate, the sim never migrated) and **generic Board Game** (by *retention*). Faction (→B) and Mass Battle (→aggregate-then-A) are the two systems that *did* apply the Decision Rule; Fieldwork is the one that was never audited at all.

**So what for the player:** engine choice is where the corpus is actually *most* disciplined — the two hard cases (bare-stat faction, aggregable mass battle) are correctly and deliberately split. The failure is Thread: a player (or the balance oracle) who assumes Thread resolves like combat/contest (continuous, in-band leverage, continuity-corrected) is wrong — the executable Thread engine counts raw d10 successes and calls Overwhelming at a threshold (`net ≥ Ob+3`) that no other system uses.

---

## 3. Obstacle-scale construction

| Site | Ob construction | Exception / boundary | How it diverges | Citation |
|---|---|---|---|---|
| **General core** | Discrete 1/2/3/5/8/20 (continuous in videogame mode); Ob min 1 | **Ob 20**: Overwhelming unavailable; Partial requires **net ≥ 10** | *(the reference)* | `params/core.md:32-55` |
| **Board Game** | Same base concept, TN 7 | **Ob 10**: Overwhelming unavailable; Partial requires **net ≥ 5** — **half** the general values; **`[FLAGGED FOR REVIEW: ED-142-R]`** ("confirm Ob 10 exception carries") | Exception band at **10/5** vs core's **20/10**, and *unresolved* | `params/bg/core.md:65-75` |
| **Personal Combat** (`combat_engine_v1`) | **Fixed `DECISIVE_OB = 3`** for *every* action; all difficulty variation routed through σ-leverage μ-shift, never the Ob number. Wounds add **fractional Ob** (+0.15 atk / +0.25 def) | no cap-exception concept (single anchor) | **Does not use the 1–20 scale at all** — one fixed Ob + continuous leverage | `core.py:25`; `params/core.md:158` |
| **Social Contest** | No fixed Ob ladder. Appraise Ob = `opponent Cha ÷ 2` (min 1); CLASH/REINFORCE resolve **margin vs audience-resistance** | Persuasion-Track bands are the effective "obstacle" | Opposed-margin, not a difficulty number | `params/contest.md:23,109-110` |
| **Fieldwork** | Own 5-tier **Depth Ob** 1/2/4/6/8 + cumulative modifiers; floor 1 | — | Distinct Depth ladder (not the 1/2/3/5/8/20 reference points) | `fieldwork_v30.md:29-51` |
| **Mass Battle** | Tactic/Command checks: small Ob (1–2). **Engagement has no Ob** — output is damage `net × (1+Power)`. BG battle = **margin** `\|atk−def\|` | BG battle: Margin ≥2 Win / ≤1 Partial / ≥2 defender Lose | Engagement is obstacle-free; strategic BG battle uses margin bands | `params/mass_combat.md:71-73,322-327` |
| **Faction Domain Actions** | Ob **remapped to a stat margin**: `D = max(1, (Ob−1)·2)`, then `M = stat − D` | clamp bounds (FLOOR 0.05 / CAP 0.90), not an Ob exception | Ob inverted into the deterministic margin; no Ob roll | `stats_1_7_scale.md:71` |
| **Thread operations** | **Three-Axis additive Fibonacci**: `Total Ob = Depth(1,2,3,5,8,13) + Breadth(0–4) + Distance(0–3)`; TN modifiers on top | no Ob-cap exception — composite routinely reaches ~20 *before* TN (Foundational 13 + Regional 4 + Far 3) | Additive composite on a Fibonacci depth axis; unbounded past 20 | `params/threadwork.md:65-101` |

**Divergences:** the "general 1–20 scale with an Ob≥20/net≥10 exception" is honored as-written **only** by core and (nominally) Fieldwork's modifier layer. The **Board Game runs a parallel Ob-10/net≥5 exception that is exactly half and self-flagged unresolved** (ED-142-R). **Combat discards the scale entirely** for a fixed `DECISIVE_OB=3`. **Contest and Faction replace Ob with opposed/derived margins.** **Thread replaces it with a Fibonacci additive composite** that has no cap-exception at all. Six subsystems, five genuinely different obstacle geometries.

**So what for the player:** "Ob 5 = Entrenched" is a stable mental model only at the tabletop-core and BG layers — and even those two disagree on where the ceiling exception bites (20 vs 10). Inside a combat scene the number "3" is *every* fight's Ob and difficulty lives in an invisible σ-shift; inside a Thread operation the "Ob" is a sum of three separate axes that can hit 20 on a routine deep operation. A player cannot carry a single sense of "how hard is Ob N" across these systems, and a designer tuning the BG Ob-10 exception has an open, unratified decision (ED-142-R) sitting under it.

---

## 4. Degree-of-Success ladder

| Subsystem | Outcome tiers | Same 4-tier Overwhelming / Success / Partial / Failure? | Bespoke vocabulary a player must learn separately | Citation |
|---|---|---|---|---|
| **Core / Combat / Fieldwork** | Overwhelming / Success / Partial / Failure (Overwhelming = `2×Ob AND ≥3`) | ✅ **Yes** (combat engine returns `overwhelming/success/partial/fail`) | none | `params/core.md:46-55`; `core.py:42-45`; `fieldwork_v30.md:69` |
| **Faction Domain Actions** | Overwhelming / Success / Partial / Failure — **"output unchanged"**, emitted via probability bands not net-vs-Ob | ✅ **Yes** (vocabulary identical; production differs) | none | `stats_1_7_scale.md:86` |
| **Board Game** | Overwhelming / Success / Partial / Failure | ✅ **Yes** (with the halved Ob-10 exception) | none (but see §3) | `params/bg/core.md:65-75` |
| **Thread operations** | design: Overwhelming / Success / Partial / Failure | ⚠️ **Vocabulary yes; threshold no** — the **sim's Overwhelming = `net ≥ Ob+3`** (`operations.py:140`), a fifth formula disagreeing with the design's own `2×Ob AND ≥3` | none in vocab; a silent threshold divergence in code | `params/threadwork.md:27,132-137` vs `sim/thread/operations.py:140` |
| **Social Contest** | 4-tier appears in **sub-rolls** (Appraise: Failure/Partial/Success/Overwhelming). **Headline outcome is bespoke**: Persuasion-Track banding **Total Victory (≥9/≤1) / Decisive (≥7/≤3) / Compromise (4–6)** + interaction types **CLASH / REINFORCE / CROSS / TIE** | ⚠️ **Partial** — reuses the 4-tier for sub-rolls, overlays two bespoke vocabularies for the outcome | **Yes** — Persuasion-Track bands *and* interaction-type classes | `params/contest.md:106-125`; `social_contest_v30.md:276,292` |
| **Mass Battle** | Engagement emits **damage** (`net × (1+Power)`), not a degree. **BG battle uses bespoke Win / Partial / Lose** (margin). Discipline/Morale are threshold tables | ❌ **No** at the resolution layer | **Yes** — Win/Partial/Lose; plus damage-as-output | `params/mass_combat.md:71-73,322-327` |

**Verdict on identity:** the four-tier ladder is a genuine shared spine for the **personal (combat/fieldwork), faction, board-game-generic, and Thread-design** surfaces — an impressive amount of coherence. It is **not** identical everywhere: **Social Contest** overlays a bespoke Persuasion-Track banding *and* an interaction-type vocabulary the player must learn from scratch; **Mass Battle's core engagement** doesn't emit degrees at all (it emits casualties) and its BG resolution uses a separate Win/Partial/Lose; and **Thread's sim** keeps the words but silently moves the Overwhelming line.

**So what for the player:** "Overwhelming / Success / Partial / Failure" is a real lingua franca and mostly works — a player reads a fieldwork result the way they read a faction result. But two of the highest-stakes moments break it: winning a *debate* is spoken in Persuasion-Track bands ("Decisive," "Compromise") and interaction types ("you CLASHED"), and winning a *battle* is spoken in casualties and Win/Partial/Lose — neither maps onto the four tiers the player learned everywhere else, and a Thread "Overwhelming" is quietly earned at a different bar than a combat "Overwhelming."

---

## 5. Shape-coherence verdicts (per pair a player will mentally connect)

| Pair | Dimension | Verdict | Why |
|---|---|---|---|
| **Combat vs Contest** ("the two personal-scale dice systems") | **Engine** | **COHERENT** | Both Instance A (sigma-leverage), single-sourced through `sigma_leverage.py` — intuition about how advantage moves the roll transfers cleanly |
| | **Degree (sub-roll)** | **COHERENT** | Both use the 4-tier ladder for the underlying roll |
| | **Pool** | **DIVERGENT-BY-DRIFT** | Combat = `max(5,H+6)` (flat), Contest = `(Attr×2)+H+3` (attribute-multiplied). Combat's Agility-independence was a *deliberate* fix (ED-901, Agi-OP defect); nothing ever re-decided that Contest *should* keep `Attr×2` — Contest's "stands on its own" note (`params/contest.md:277-279`) is a post-hoc rationalization of an un-propagated split, and Fieldwork still *falsely* claims the old parity (`fieldwork_v30.md:61`). **A player who internalizes the contest pool computes the wrong combat pool.** |
| | **Ob** | DIVERGENT-BY-DESIGN (mostly) | Combat fixed-3 + σ vs Contest opposed-margin — defensible (solo-vs-environment vs two-party contest) |
| **Mass Battle vs Faction** ("the two strategic-scale systems") | **Engine** | **DIVERGENT-BY-DESIGN** | A (aggregated dice) vs B (deterministic+stochastic, no dice). The Decision Rule *prescribes* exactly this: aggregable pool → A, bare-stat 1–7 pivotal → B (`SKILL.md:148-149`); the SKILL explicitly says keep dice for mass battle and route bare-stat faction to B. Principled and documented. |
| | **Output** | **COHERENT** | Both emit the same 4-tier ladder — faction explicitly preserves it ("output unchanged", `stats_1_7_scale.md:86`) |
| | **Feel** | DIVERGENT-BY-DESIGN, *with a real legibility cost* | Same strategic scale, two utterly different resolution acts: roll a fistful of dice for a battle vs. read a % and draw once for a domain action. Correct, but warrants a player-facing "these resolve differently, here's why" note. |
| **Thread vs everything else** ("the system meant to feel different on purpose") | **TN ladder & Ob** | **DIVERGENT-BY-DESIGN** | TN 7/8/9 escalation + Three-Axis Fibonacci Ob is the ontological-depth model — Thread is *supposed* to feel alien; this is the system earning its difference |
| | **Pool** | COHERENT-ish (ironically) | `(Spirit×2)+H+TPS` shares the `Attr×2+H` base that Contest/Fieldwork use and that Combat abandoned — the "different" system is closer to the norm than the "same" ones are to each other |
| | **Engine implementation** | **DIVERGENT-BY-DRIFT** | Design claims the shared sigma-leverage substrate (Instance A); the **sim runs legacy raw-d10** (`operations.py:40`) with a **fifth, uncited Overwhelming threshold `net ≥ Ob+3`** (`operations.py:140`). The drift lives *inside* the by-design-different system: nothing decided Thread should resolve on a different engine than combat/contest — it simply never migrated. **Fixable**: migrate Thread to the shared substrate, or explicitly ratify `ob+3`. |

**So what for the player:** the pairs split cleanly by cause. **Combat↔Contest** is *coherent where it counts for engine feel but divergent-by-drift in the one number a player will most confidently reuse* (the pool) — this is the legibility problem worth fixing, and Fieldwork's stale "matches Combat" claim actively propagates the error. **Mass Battle↔Faction** is *divergent-by-design* — the right call, but a place to invest in explaining *why* two strategic actions resolve so differently. **Thread** is *correctly alien where it intends to be* (Ob/TN) and *accidentally alien where it doesn't intend to be* (a legacy engine and a bespoke Overwhelming line that disagree with Thread's own design doc). The single highest-value fix is the Combat/Contest/Fieldwork pool-shape drift, because it is the one divergence with **no stated design reason**, it sits under the three systems a player is *most* likely to treat as one, and one of the three docs still asserts a parity that ED-901 broke.

---

**Files inspected firsthand (absolute):** `/home/user/ttrpg/params/core.md`, `/home/user/ttrpg/designs/scene/combat_engine_v1/core.py`, `/home/user/ttrpg/params/contest.md`, `/home/user/ttrpg/designs/scene/social_contest_v30.md`, `/home/user/ttrpg/designs/scene/fieldwork_v30.md`, `/home/user/ttrpg/params/mass_combat.md`, `/home/user/ttrpg/params/factions/stats_1_7_scale.md`, `/home/user/ttrpg/params/threadwork.md`, `/home/user/ttrpg/sim/thread/operations.py`, `/home/user/ttrpg/params/bg/core.md`, `/home/user/ttrpg/skills/valoria-resolution-diagnostic/SKILL.md`, `/home/user/ttrpg/CURRENT.md`.
