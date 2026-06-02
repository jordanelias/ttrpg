# Mass-Battle Engine — Comprehensive Workplan
**Date:** 2026-06-01 · **Engine:** `tests/sim/sim_mb_sigma.py` @ `7cfa44d5` · **Spec:** `designs/provincial/mass_battle_v30.md` (v4.8)
**Inputs:** the architecture+completeness audit (`1a525127`, `…/mb_engine_completeness_audit.md`) + Jordan directives 2026-06-01.
`[SELF-AUTHORED — bias risk]` engine is largely my own; phases stated as an independent reviewer; all mechanical magnitudes Jordan-vetoable, no canon edited without the editorial workflow.

**Standing directives this plan encodes:**
- **D-A (priority):** modularize the engine into a container/package, "intelligently and methodically." Confirmed go.
- **D-B (canon):** *eliminate general death as a consequence of mass battle — capture at worst, never automatic character elimination.* Jordan canon-structure decision (design authority). **Capture CONSEQUENCE is OUT of the mass-battle container** (rendered by a separate system) — the engine produces a terminal "captured/incapacitated" state and hands off; this plan does NOT design ransom/imprisonment.
- **D-C (formations, NEW):** Football-Manager-style **three-level compositional formation system** — army doctrine → unit formation (default template OR custom allocation) → subunit role/subformation + per-unit standing instructions. **Grounded in prior recorded design** (ED-814 "adjustable allocation grid; FM analogy exact"; the SI/FM architecture pivot; team-instruction layer Aggression/Cohesion-priority) — NOT invented here. Supersedes/expands old P-C.
- **D-D (Lanchester, NEW):** add an explicit **Linear-Law attrition substrate** (melee) + **Square-Law** for volley (ranged), feeding the morale/rout system — NOT replacing it. See P-Lanchester.

**Resolved open decisions (Jordan 2026-06-01 r2):**
1. Capture consequence → OUT OF SCOPE (rendered outside the mass-battle container). P-B/P-D simplify: emit "captured", hand off.
2. Terrain (P-E) → **STUB** (reserve the seam/interface; no terrain modifiers built now).
3. Phase-3 cavalry-shock magnitudes (`7cfa44d5`) → **RATIFIED**. Drop the "PROPOSAL/vetoable" caveat for those 9 constants; record ratification (ED entry).
4. Formation/tactic design → exists in prior conversation (FM parallel); see D-C, grounded not invented.

**Method gate (every phase):** bottom-up from canon + engine → top-down validation (historical precedent / the C1–C7 + H/R gauge) → `PER_CELL=0` byte-exact toggle-off → commit. Canon edits go through `safe_commit` with `canonical_sources.yaml` co-file + an `editorial_ledger.jsonl` ED entry. Stage work; never one mega-block (wall-clock).

---

## SEQUENCING (dependency-ordered)

```
P-A  Modularize (refactor; behaviour-frozen)        ← FIRST (D-A). Unblocks clean landing of all later work.
 ├─ P-B  General-death → CAPTURE (canon + relabel)   ← D-B. Small; capture-consequence OUT of container.
 ├─ P-L  LANCHESTER attrition substrate              ← D-D. Foundational; melee=linear, volley=square; feeds morale.
 │        (best landed right after P-A in resolution module; reframes the casualty term)
 └─ P-C  FM COMPOSITIONAL FORMATION/TACTIC SYSTEM     ← D-C. army doctrine → unit formation (template|custom)
     │     → subunit role/subformation + standing instructions. Closes the formation/tactic GAPs+PARTIALs.
     ├─ P-D  Two-stage general EVENT (capture-only)   ← depends P-B; consequence handed off out-of-container.
     ├─ P-E  Terrain  → STUB ONLY                     ← reserve seam; no modifiers built (Jordan r2).
     └─ P-F  Speed-into-combat (S1) + vectorized penetration (S4)
P-G  Cleanup/retire (S7/S8/S9) + deep formula-consistency audit   ← LAST.
```

P-A is the hard prerequisite. **P-L (Lanchester) and P-C (FM formations) are the two foundational additions** — P-L makes attrition physically principled; P-C is the player-facing strategic layer. Both should land in the new modular structure (P-L in `resolution`/a new `attrition.py`; P-C in a new `formations.py`/`tactics.py`). P-D/P-E/P-F independent.

---

## P-A — MODULARIZE INTO A CONTAINER (FIRST; behaviour-frozen)

**Goal:** split the ~2,640-line monolith into an importable package along its four existing seams, with a thin wrapper and a mechanics registry. **Zero behaviour change** — the entire phase is verified by byte-exact `PER_CELL=0` (and PER_CELL=1 numeric-identity on the gauge).

**Target structure** (`tests/sim/mass_battle/`):
| Module | Owns (functions already in the monolith) |
|---|---|
| `geometry.py` | `*_cells`, `oriented_pattern`, `cell_facing`, `octagon_angle`, `_support_along_vector`, `atom_max_width`, `cells_to_orig_coords`, `support_engage_frac`, `cell_speed`, facing helpers |
| `resolution.py` | `roll_pool`, `compute_degree`, `_sigma_softcap`, `_sigma_net_boost`, `_morale_sigma`, `_charge_shock_sigma`, the σ-head constants (`SIGMA_*`, `MORALE_*`) |
| `percell.py` | `_ColBlock`, `build_column_grid`, `_engaged_cols`, `distribute_casualties`, `_fatigue_sigma`, `_envelopment_sigma`, `_defender_depth`, `update_stamina`, all `PC_*` constants |
| `orchestration.py` | `Subunit`, `Unit`, `find_contacts`, `assign_targets`, `resolve_cross_side_contention`, `resolve_engagements(_cascading)`, `volley_phase`, `run_battle`, `run_multi_turn_battle`, `run_multi_unit_battle`, pursuit/recall/rally/reform, phase hooks |
| `config.py` | all module-level tunables, single source; env-var reads centralized |
| `engine.py` | thin wrapper: imports the above, exposes the public API the gauge uses, defines `MECHANICS` registry |

**`MECHANICS` registry** (the troubleshooting win): `name → {fn, toggle_env, canonical_source, status}` for every mechanic in the audit table. Enables: one place to see what exists, per-mechanic enable/disable, and a self-test that asserts every canonical mechanic has a registry row (turns the audit into an executable check).

**Steps (staged commits):**
1. Create `tests/sim/mass_battle/` package; move geometry + resolution + percell + config (pure-ish, fewest cross-refs first). Each module commits with a passing import smoke-test.
2. Move orchestration; resolve circular refs via the config module + dependency-injection where a percell fn needs a resolution fn.
3. Write `engine.py` wrapper + `MECHANICS` registry; point a shim `sim_mb_sigma.py` at `from mass_battle.engine import *` (back-compat: `gauge_mb.py` keeps working unchanged).
4. **Verify:** `PER_CELL=0` gauge byte-exact to `7cfa44d5`; `PER_CELL=1` gauge numerically identical (H1–R3 + C1–C7). Registry self-test green.
5. Update `gauge_mb.py` ENGINE path (or keep the shim); update `coverage_matrix.md`; commit.

**Risks/guards:** `gauge_mb.py` uses `exec(open(ENGINE).read())` — the shim must preserve the exact public names it relies on (`make_unit` deps: `Subunit`, `Unit`, `SIDE_A_START_ROW`, `run_battle`, `run_multi_turn_battle`, `ANCHOR_MAP` is gauge-side). Inventory the gauge's used symbols first. **Acceptance = byte-exact**; any diff is a refactor bug, not a tuning question.
**Effort:** L (large surface, low conceptual risk). **Autonomous.**

---

## P-B — GENERAL DEATH → CAPTURE (D-B; canon edit + minor engine)

**Directive:** mass battle never automatically eliminates a character. A general/officer is, at worst, **incapacitated and/or captured**. Removes the "killed" outcome from battle entirely.

**Bottom-up — the three canon sites that currently kill a character in battle:**
1. **A.5 General two-stage death** (L260-263): Stage 2 = "killed", −2 Morale, Command=0, uncommanded.
2. **A.4 morale triggers** (L193-201): "General killed (Stage 2): −2 … −2 general kill" wording + the −5 max-loss clarification.
3. **§D.2 Officer death** (L867) + **companion-officer combat death** (L878): `1d20 ≤ Size lost → officer killed`; companion "killed in battle → departure scene as combat death".

**The change (canon, Jordan-directed):**
- A.5 Stage 2 → **"incapacitated → captured/incapacitated"**: keep the *command* effect (−2 Morale outside cap, Command=0, uncommanded — a downed/captured general still stops commanding) but rename the outcome from *killed* to *incapacitated; captured if the field is lost*. The character survives.
- A.4: reword "General killed" → "General incapacitated (Stage 2)"; the −2/uncapped morale effect and the −5 max stay (mechanically identical; only the lethal semantics drop).
- §D.2: the `1d20` officer roll → an **incapacitation/capture** roll, not death. Companion-officer "combat death" departure scene → a **capture/wounded** scene (the companion is removed from the field, not killed).
- **Add** a short canonical paragraph: *"No mass-battle mechanic kills a player or named character. The worst battlefield outcome for a general/officer is incapacitation and (if their side loses the field) capture. Death of a named character, if it ever occurs, is a narrative/world-layer event, never an automatic battle result."*

**Engine implication (minor):** the engine only ever applied the **−2 morale effect** (L2163) — no elimination code exists. So P-B in the engine = relabel the comment/semantics and (when P-D wires the event) implement *capture state*, not death. Nothing to delete.

**FLAGGED — Jordan/world-layer decision (do NOT invent):** *what a captured general/officer actually triggers* — ransom, imprisonment, escape/rescue arc, Disposition/relationship effects, return-to-play conditions. No prisoner/ransom mechanic exists in canon today (verified: none in `canonical_sources.yaml`). P-B defines the *battle outcome* (capture, not death); the **capture consequence is a separate design decision** to be specified before P-D can fully wire it. The workplan records this as `[OPEN — Jordan: capture consequence / ransom system]`.

**Editorial mechanics:** edit `mass_battle_v30.md` (co-file `references/canonical_sources.yaml` REQUIRED by the design-doc co-file hook) + an `editorial_ledger.jsonl` ED entry recording the Stage-2/officer-death reframing and its Jordan-directive provenance. Commit scope `editorial`.
**Effort:** S (canon-text + 1 engine comment). **Jordan-directed** (canon authority). Capture consequence handed off OUT of container — not designed here.

---

## P-L — LANCHESTER ATTRITION SUBSTRATE (NEW; D-D; foundational)

**Why (honest assessment).** The engine today has **no Lanchester attrition law**: per tick `casualties = CASUALTY_SCALE × DAMAGE_BY_DEGREE(degree, Power) − enemy_DR` — casualty output is set by roll-degree + Power, **not** by the number of enemy troops in contact. Numbers enter combat only via the pool (continuous `effective_size` → fewer dice when depleted), never as a force-on-force attrition term. So Jordan's instinct is right: a foundational piece is absent.

**Which law (grounded, not pattern-matched).** Lanchester has two:
- **Linear Law** = *ancient/melee*: one fighter engages one fighter; casualty rate capped by **troops-in-contact / frontage**; numerical superiority is only a *linear* edge. (Wikipedia/OR lit: linear law is explicitly "for ancient combat"; mechanism = "casualties... proportional to combatants in direct physical contact... limited by terrain or formation frontage".)
- **Square Law** = *modern/ranged/aimed fire*: any unit engages any enemy; power ∝ N². Requires the frontage cap to be lifted (firearms/artillery).
- Empirically, real battles sit **between** (exponent ≈1.5; Willard 1618–1905).

**The design (composes with the σ head + per-cell, does NOT replace morale):**
- **Melee (engagement phase): Linear Law.** Casualty rate ∝ (engaged enemy strength), **frontage-capped by the per-cell contact set** — which the Incr-4 depth-aware contact fraction *already computes*. So the engine already has the linear law's *frontage-limitation mechanism*; P-L adds the *attrition term* on top of it. The σ-leverage exchange ratio sets *who wins the exchange / the kill-ratio asymmetry*; Lanchester sets the *casualty magnitude from numbers-in-contact*. Clean separation of roles (Lesson 1).
- **Volley (ranged phase): Square Law.** Aimed fire lifts the frontage cap → concentration matters → N². The engine **already separates the volley phase** (`volley_phase`), so this is the exact, historically-correct seam: **melee=linear, volley=square.**
- **Feeds, not replaces, morale.** Battles still end by rout at ~30% casualties (du Picq); Lanchester governs the *casualty-accrual rate* feeding the morale/rout triggers, not a new victory condition. This is the critical guard — without it, an attrition law would re-introduce annihilation battles the morale model deliberately avoids.

**Validation:** the C1–C7 + H/R gauge must stay in band (Lanchester replaces the casualty term, so re-tune `CASUALTY_SCALE`/coefficients to hold the historical win-rate + casualty bands); add a 2-force-size sweep asserting the linear-law signature (larger force's survivors ≈ difference of sizes for equal quality) in pure melee, and the square-law signature (concentration advantage) in pure volley. `PER_CELL=0` byte-exact preserved (gate the new term behind the per-cell/contact machinery or a flag until validated).
**Effort:** M–L (replaces a load-bearing term; heavy validation). **Autonomous** mechanics; the linear-vs-square-vs-1.5 exponent choice is a Jordan design confirm. Land in `resolution.py`/new `attrition.py`.

---

## P-C — FM COMPOSITIONAL FORMATION / TACTIC SYSTEM (D-C; grounded in prior design)

**Goal:** the player-facing strategic layer, modeled on Football Manager (the recorded design intent). **Grounded in prior conversation** — ED-814 ("the grid is not a hand-authored 9-cell grid; it is an adjustable allocation surface where you allocate X% with parameters/conditions; the FM analogy is exact; auto-distribute with manual override"), the SI/FM architecture pivot (deploy → doctrine → assign roles → intervention windows, not per-tick control), and the team-instruction layer. **Three composition levels:**

| Level | FM analogue | Valoria object | Notes |
|---|---|---|---|
| **Army doctrine** | team mentality/tempo | standing posture across all units (Aggression: Cautious/Balanced/Pressing; Cohesion-priority: Hold-shape/Adapt) | conditions Phase-3 movement bias + degradation behaviour |
| **Unit formation** | team formation (4-4-2 / custom) | **default template (Line/Wedge/Shield Wall/Skirmish/Column/Reserve/Horseshoe/Arrowhead/etc.) OR a custom allocation** (set %composition + shape intent; engine auto-distributes to cells; manual cell override) | this is ED-814's adjustable allocation surface; the canonical A.6 formations are the *templates*, custom is the override |
| **Subunit role / subformation** | player role + instructions | each subunit gets a role/subformation + its own standing instructions (e.g. a flanking subunit set aggressive while the line holds) | "assign subunits their own subformation" — nested formations |

**This subsumes the old declared-formation/tactic gap.** The canonical A.6 formations become **default templates** in the unit-formation level (each carrying its dice rule: Shield Wall +2D Def/cannot-advance/negate-flank, Wedge +2D Off/negated-by-SW, Skirmish no-flank/−1D-vs-Heavy, Column movement-only/+1 speed, Reserve turn-delay). The A.8 tactics (Envelopment, Feigned Retreat, Ambush, Concentration, Hammer & Anvil) become **declarable doctrines/maneuvers** at the army/unit level. So building D-C closes the same 6 GAPs + 8 PARTIALs the audit found — but as the *intended FM strategic surface*, not a flat tactic list.

**Bottom-up engine mapping:** a `Formation` object on `Unit` (template-id | custom allocation grid) that drives cell layout (replacing the current hardcoded `*_cells` selection with a template-or-custom resolver) + injects σ-modifiers (uniform-impact, NOT pool mods) at `resolve_engagements`; a `role`/`instructions` field on `Subunit`; a `doctrine` field on the army/side. Auto-distribution = the allocation→cells solver (the ED-814 core). Manual override = per-cell edit.

**Design discipline:** this is a large player-facing layer — build it **after P-A** so it lands in `formations.py`/`tactics.py`, and **incrementally** (template-selection first → custom allocation → subunit roles → standing instructions → A.8 maneuvers), each increment gauge-validated against the A.6/A.8 counter-logic (Wedge>Line, Shield Wall>Wedge, Skirmish flank-immune, Feigned Retreat reproduces Hastings) + historical precedent. `PER_CELL=0` byte-exact preserved (new layer opt-in/default-template until validated). Re-read the full ED-814 thread + the FM-pivot conversation before building (bottom-up: the design exists).
**Effort:** XL (the biggest single piece; multi-increment). **Autonomous** mechanics; magnitudes + the template/instruction catalog Jordan-confirmable. Pull the prior-conversation design into a canon doc first (it is conversation-only today — not yet in canon/ledger; **a design-capture step is prerequisite**).

---

## P-D — TWO-STAGE GENERAL EVENT (capture-only; depends on P-B + P-C)

Wire the **general-as-event** the audit flagged (A.5) — but per D-B, as **incapacitation→capture**, never death. Stage 1 (incap: −1 morale, Command halved, Medicine Ob2 stabilize window) → Stage 2 (not stabilized: Command=0, −2 morale, **general captured if field lost**). Triggerable on the existing command/morale machinery. The post-capture state is **handed off out of the mass-battle container** (D-B r2) — the engine emits "captured/incapacitated" + which side holds the field; the consequence system renders the rest. No `[OPEN]` blocker remains.
**Effort:** M. **Autonomous** (consequence is out-of-scope, not a blocker).

---

## P-E — TERRAIN / ENVIRONMENT (A.9) — **STUB ONLY** (Jordan r2)

Do **not** build terrain modifiers now. **Reserve the seam:** a no-op `terrain` parameter/interface on the battle setup + a registry slot, so a future terrain layer (forest → Cavalry Standard + no-flank; broken ground; high ground) can be added without re-plumbing. The stub asserts open-ground behaviour is unchanged (byte-exact). Full terrain is explicitly deferred.
**Effort:** S (interface only). **Autonomous.**

---

## P-F — SPEED-INTO-COMBAT (S1) + VECTORIZED PENETRATION (S4)

The still-open original Phase-1/Phase-2 from the speed/facing workplan:
- **S1:** wire canonical `Unit.speed` (Slow/Standard/Fast) into **combat closing-speed** (today it feeds pursuit only; per-cell cavalry mult exists but the canonical tier isn't in combat). Canon gives speed no *direct* combat effect → route closing through the tier, don't invent. C1–C7 are the regression guard.
- **S4:** replace `_defender_depth` (mean col depth) with `_support_along_vector` along the charge vector, speed-scaled. C2/C6 braced-repulse + C7 rear-bypass guard against ahistorical dominance.
**Effort:** M each. **Autonomous.**

---

## P-G — CLEANUP / RETIRE + DEEP FORMULA-CONSISTENCY AUDIT

- Retire `_envelopment_sigma` (dormant `PC_ENVELOP_SIGMA=0`) if still redundant after P-C; reconcile superseded v14 items; fix the stale docstring (audit S7/S8/S9).
- Run `valoria-mechanic-audit` (formula consistency) over the now-modular engine to line-check every PARTIAL row's dice values against canon — the deeper pass this completeness audit deferred (`[CONFIDENCE: medium]` items).
**Effort:** M. **Autonomous.**

---

## OPEN DECISIONS (status after Jordan r2)
1. ✅ **RESOLVED** — Capture consequence: OUT of the mass-battle container (rendered elsewhere). P-B/P-D no longer blocked.
2. ✅ **RESOLVED** — Terrain: STUB only (P-E reserves the seam, builds nothing).
3. ✅ **RATIFIED** — the 9 `PC_SHOCK_*`/`PC_CHARGE_SIGMA` magnitudes (`7cfa44d5`) are accepted. Action: record ratification in the editorial ledger + drop the "PROPOSAL/vetoable" caveat on those constants (small `editorial` commit).
4. ✅ **GROUNDED** — Formation/tactic design exists in prior conversation (ED-814 + FM pivot); P-C is built from it, not invented. Remaining confirm: the template/instruction *catalog* + σ-magnitudes at build time (Class-B, sim-tunable).
5. 🔶 **NEW CONFIRM (P-L)** — Lanchester exponent choice: linear (melee) + square (volley) as proposed, vs a blended ~1.5 exponent. Recommend the linear/square split (historically exact + matches the existing phase separation); Jordan to confirm.

## EXECUTION NOTE (sequenced for Jordan's go)
**Methodical order** ("modularize intelligently and methodically"):
1. **P-A modularize** — staged sub-commits, each **byte-exact**-verified against `7cfa44d5`. This is the foundation; everything lands cleanly afterward.
2. In parallel / immediately after, three small independent commits: **P-B** canon reframe (`editorial`); **ratification record** for Phase-3 magnitudes (`editorial`); **design-capture** of the ED-814/FM formation system from conversation into a canon design doc (`editorial`) — prerequisite for P-C.
3. **P-L Lanchester** — foundational attrition substrate (re-tune to hold the gauge bands).
4. **P-C FM formation system** — the big multi-increment player-facing layer.
5. **P-D / P-E-stub / P-F**, then **P-G** cleanup + deep audit.

Nothing now blocks starting P-A. The two foundational additions (P-L, P-C) are the heart of the remaining work; both are grounded (Lanchester literature; the recorded ED-814/FM design) and both land in the new modular structure.
