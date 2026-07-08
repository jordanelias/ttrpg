# Charter — Pessimist Subtractive NERS over player-available actions

## Status: RATIFIED 2026-07-08 (Jordan: 'Please ratify all'; ED-IN-0027) — §8.2-A landed in references/throughlines_meta.md; docket verdicts filed as lane EDs (ED-PC-0007/SC-0012/FA-0006/SE-0005/WR-0007/FI-0004), execution = lane follow-ups. Originally PROPOSED (read-only audit, 2026-07-08) · Lane: IN (cross-cutting) · Anchor: ED-IN-0027
## Method: 8 Sonnet lane dossiers → 1 Sonnet inverted critic → Fable-5 verdict+synthesis (opus effort:max fallback). Read-only: no canon, params, code, ledger, or handoff edits. This audit only proposes; nothing here is ratified until Jordan rules the docket.

---

## §0 · Purpose and the one non-negotiable rule

This audit does something the corpus's vetting framework cannot currently do: **issue subtractive
verdicts** — REFINE / DISTILL / PRUNE / CUT — on the game's player-available actions, so scope can
be *reduced* before the armature-first resolution program spends effort deploying, wiring, and
re-authoring every subsystem. It is a **scope gate upstream of realization**, deliberately
complementary to (not competing with) the additive Stratum A→E program (`designs/audit/
2026-07-07-unaddressed-areas-audit/resolution_plan_v1.md`).

> ## CARDINAL RULE — judge as-if-built, never by build state.
> For any action not yet built, judge **how it would contribute to the game if it were built as
> intended.** Being a stub, unwired, unbuilt, or Godot-unported is **NOT a flag for uselessness and
> NOT a flag for a problem with building the game** — it is orthogonal to the verdict. A never-built
> action whose realized contribution is load-bearing is a **KEEP**; a fully-built action that would
> be dominant or redundant *even when realized* is a **CUT**. Every verdict evaluates the *design
> intent's projected contribution*, on the counterfactual "if built as specified, then …", against
> N / Ω / Q. **Any verdict that cites stub-ness, unwired-ness, or Godot-unported status as a reason
> is invalid by construction and is kicked back.** Build state may appear only as routing metadata
> for the additive plan, never as verdict evidence.

---

## §1 · The unit of analysis

Each subsystem's **player-available-action set** — the verbs the player can take. Where the prose
menu and the code menu diverge (notably PC and FA), treat them as **two objects to reconcile**, not
one. Lanes in scope (corpus-wide sweep, Jordan 2026-07-08):

| Lane | Player-action homes (starting map — dossiers extend) |
|---|---|
| **PC** personal combat | `designs/scene/combat_v30.md` §4 ACTIONS (Strike/Feint/Establish Distance/Take a Breath/Full Guard/Disarm/Retrieve/Tie Up/Escape/Rescue/Dodge/Stunt); the continuous `combat_engine_v1/` resolver (no player concept yet) |
| **MB** mass battle | `designs/provincial/mass_battle_v30.md` §A.7 per-phase declarations + §D aftermath choices |
| **SC** social contest | `sim/personal/contest/dictionaries.py` Style×4 cards; the four games (Agôn built; Negotiation/Inquiry/Consensus prose); `player_interaction_walkthrough_v1.md` |
| **FA** faction / domain actions | three unreconciled vocabularies — `da.*` Keys · `faction_action.py` (Conquest/Muster/Govern/unique) · `faction_layer_v30 §7` priorities; `domain_actions` `doc:null` (C-FA-12) |
| **SE** settlements | `settlement_layer_v30.md` §3.2 governance action; Trade/develop verbs in `player_agency_v30 §9` |
| **WR** world | the Scene Slate mechanism (`player_agency_v30 §4`) as the umbrella surfacing surface |
| **FI** field investigation | `investigation_systems_v30.md` (Observe/Surveil/Reconstruct/Thread-Read; Dialogue Lattice utterances) |
| **TW** threadwork | `sim/thread/operations.py` `attempt_*` (Leap/Weaving/Pulling/Locking/Dissolution/Mending); `threadwork_v30.md §2` |

---

## §2 · The criteria (canonical, bound not invented)

Bind only to the canonical vetting framework `references/throughlines_meta.md` — **no new criteria.**

- **N — Necessity** (§0, meta:24): *"earns its existence if it models a real, load-bearing dynamic
  of Renaissance-era political leadership … Complexity is permitted only when grounded in the subject
  matter."* Failure modes (meta:34-37): Fantasy imposition · Duplicate coverage · Edge case mechanic
  · Abstractable.
- **Ω — Intent** (meta:47), four clauses: (a) cross-scale consequence traceable-not-fully-anticipable
  · (b) personal-scale transformation · (c) autonomous events regardless of player action · (d)
  **non-dominance — "every action pays what it buys."**
- **Μ Modes / М Meta-throughlines / Τ Throughlines** — checked where an action's contribution turns
  on them (e.g. Μ-δ cross-scale, М-6 cost-hidden, Τ breaks).
- **Q — Quality** (meta:114): Q-robust (3 viable approaches · visible traceable change · fires
  player-independently · **dramatic legibility**: whose position is at risk / what each named actor
  wants / what happens if no one acts — one sentence each from game-state); Q-smooth (composes
  without special-casing); **Q-elegant (core rule restatable after one reading).**

The **Failure Lexicon** (meta:157-173) is the bridge to subtraction — it already names *why* a
mechanic doesn't deserve to exist, it simply lacks a subtractive disposition today.

---

## §3 · The subtractive disposition table (the novel extension — PROPOSED)

`throughlines_meta.md` §8.2 routes every failure to build/wire/redesign/flag/iterate — there is **no
cut/prune/distill verdict**. This audit proposes the missing mapping (to be filed as a PROPOSED §8.2
addendum, not written into canon here). All triggers are **design-intrinsic and judged as-if-built**:

| Trigger (canonical signal, judged as-if-built) | Subtractive verdict |
|---|---|
| **N-fail** — even realized, not a real load-bearing leadership dynamic (Fantasy imposition) | **CUT** |
| **Duplicate coverage** (N) — two actions that would do the same job even if both built | **PRUNE / MERGE** |
| **Abstractable / Edge-case** (N) — folds into a more general rule with no lost decision | **DISTILL** |
| **Q-elegant fail** — even well-built, the rule isn't restatable after one read | **REFINE** (simplify the design) |
| **Dominant strategy** (Ω-d, М-6) — if built, a strictly-best no-brainer; doesn't pay its cost | strong **CUT / PRUNE** |
| **Flavor-only** (Ω, Μ-γ, М-3) — adds no decision the player weighs | **CUT / DISTILL** |
| **Personal-only / Strategic-only** (Ω-a / Ω-b) — no cross-scale consequence | **PRUNE** signal |
| Passes N + Ω + Q **as-if-built**, under adversarial attack | **KEEP** (whether or not any code exists yet) |

**Default stance (inverted, pessimist):** an action, judged as-if-built, must *prove* it is
load-bearing (N), pays-what-it-buys (Ω-d), produces cross-scale consequence (Ω-a), and is
one-read-legible (Q-elegant) — or the verdict is subtractive, not "iterate."

---

## §4 · The boundary with the additive resolution plan (intent gate on the *design*)

Every verdict carries an intent gate — **DELIBERATE / NOT-INTENDED / UNDETERMINED** — applied to the
**design**, never the code:

- *"It isn't wired / built / ported yet"* → **never a verdict input.** Routes to the resolution plan
  (wiring debt it already owns). This audit does not cut, flag, or penalize anything for being
  unbuilt.
- *"Would this concept, if realized, earn its place?"* → **this audit's call** (subtractive verdict
  on design merit). Catching a not-worth-building concept **before** the deployment waves spend
  effort on it is the entire value.

**Complementarity is checkable:** every docket row must name the resolution-plan Stratum/OPT or lane
task it *retires or shrinks*. A row that can't name downstream work it removes is not a scope cut —
it drops to an ordinary finding.

---

## §5 · Method, discipline, output

- **Six directions** (per the ratified NERS-audit charter): top-down, bottom-up, lateral, diagonal,
  forwards, backwards. **Severity:** P1 (blocks/undermines North Star) · P2 (materially narrows
  meaningful choice) · P3 (friction/debt). **Calibration tags:** KNOWN-TRACKED / KNOWN-UNTRACKED /
  NEW.
- **Inverted adversarial critic:** an independent Sonnet pass **steelmans each condemned action** —
  tries to *save* it (why it should be KEPT, judged as-if-built). A CUT/PRUNE survives only if it
  withstands an honest attempt to justify the action's existence. Pessimist, not reckless.
- **Model tiering (CLAUDE.md §10):** dossiers + critic = `sonnet`; verdict-rendering + cross-corpus
  synthesis + §8.2-extension authorship = `fable`, with `opus effort:'max'` as the drop-in fallback
  (Fable metering has hung twice here; verify terms, fall back on any stall). Dossiers never wait on
  Fable.
- **Deliverables (new files only):** per-lane dossiers + inverted critic (`01_workings/`), the
  verdict-first report, `finding_status.md`, `ed_options.md` (the subtractive docket, Jordan-ruled),
  the PROPOSED §8.2 extension, and workplan-v6 §5 register deltas (scope-reduction rows). No lane
  surface is edited; the §8.2 flip and any acted-on CUT are separate Jordan-ratified follow-ups
  (ED-1094 merge-ratifies discipline).
