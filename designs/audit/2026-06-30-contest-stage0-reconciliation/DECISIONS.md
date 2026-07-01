# Social-Contest Rebuild — Stage 0 (Foundation) DECISIONS & Reconciliation Contract

**Status:** Gate 0 **RATIFIED by Jordan, 2026-06-30.** This is the design contract every later stage cites.
**Provenance:** produced by the agonist/antagonist Stage-0 workflow (`wf_1e602524-a77`, 20 agents, 6 rounds).
Full artifacts co-filed here: `reconciliation_map_raw.md` (95KB agonist map) · `gate0_packet.md` (40KB scribe memo).

## Convergence record (honest)
Capped at the 6-round hard cap — did **not** hit 2 consecutive dry rounds. Trajectory: **7 upheld findings
(5 major) at round 1 → 2 major + 1 minor at round 6**, with **5 of 7 lenses fully cleared** (reconciliation
soundness, GM-removal, ID-discipline, scope-creep, anti-fabrication). The two residual majors were not
map-wording defects — they are genuine design-authority forks that no rewording dissolves, so they were
escalated to Jordan and **ratified below.** The harness correctly refused to stamp the map "clean" while it
papered over two real forks.

## Ratified decisions

### D0-1 — Appeal axis (ethos/pathos/logos): build BOTH forms, decide by seeded A/B
The groundup houses appeal as a **per-move multiplicative** gain-term (`gain = MERIT_SCALE·magnitude·res·…`,
`resolver.py:214`, carrying the Aristotelian appeal×tense cross-term via `joint_weight`). The reconciliation
map proposed folding it into the **additive δσ** armature — the antagonist correctly flagged that as an
unsound multiplicative→additive semantic change (would drop the cross-term without a conversion + parity check).
**Ruling:** the two forms trade *player-forgiveness* against *venue/adjudicator identity* on this one lever
(multiplicative = punishing off-axis + sharp identity; additive = forgiving + flat identity). Do **not** pick
by taste. **Build both behind a config flag**; keep **multiplicative-with-a-raised `RES_FLOOR`** as the
validated baseline (survivable-but-meaningful off-axis); run a **seeded A/B** measuring (a) player win-rate vs
a fixed NPC policy (the "not stacked against you" axis) and (b) venue-identity spread (the variety axis). The
A/B result decides. Emergent-from-primitives + tested — no fiat.

### D0-2 — σ-leverage housing: numpy-free autoload sibling (`sim/autoload/sigma_leverage.py`)
The working σ-core (`soft_cap`/`sigma_n`/`net_boost`) currently lives in a **test dir**
(`tests/sim/v32-combat-balance/m1_dice_sigma_core.py`) and **imports numpy**; canonical `sim/autoload/dice_engine.py`
is stdlib-only ("root primitive, no deps"). **Ruling (by prescriptive architecture, not preference):** port the
σ layer into a **new numpy-free first-class autoload module** `sim/autoload/sigma_leverage.py` that imports
`dice_engine` and is **single-sourced** for both combat and contest. This simultaneously retires the test-dir
dependency, the numpy dependency, the combat `sys.path.insert` hack, **and** the distillation report's "two σ
kernels" debt. Separation of concerns: `dice_engine` = pool/degree primitive; `sigma_leverage` = the
advantage→μ-shift layer atop it. **Requires** a parity test: the stdlib port (`math.tanh`/`math.sqrt`) must
match the numpy original within float tolerance on every function combat/contest use.

### D0-3 — TN6/7/8 boost divergence + fractional-Ob: probe, do NOT block; contest stays δσ TN7
`net_boost` is TN-dependent (`sigma_per_die` 0.806/0.800/0.781 for TN6/7/8); combat's `soft_cap·sigma_n` is
TN-independent (coeff 0.8). They agree **only at TN7**. Contest is **TN7-only**, so it is unaffected — the
divergence is latent for contest, live only for the combat re-point. Jordan raised **fractional Ob** as an
alternative representation of advantage (a threshold subtraction is TN-agnostic and more legible — serves the
opacity goal). **Ruling:** fractional Ob is a legitimate candidate, BUT it partially reopens **CR6**, which
chose the δσ μ-shift *specifically* because flat/Ob-style bonuses don't scale uniformly across pool sizes
(5D vs 26D — the ratified "F1 fix"). Do not fiat it mid-Stage-0. **Contest proceeds on the existing δσ
substrate at TN7** (preserving the 151-test behavior). **Open a dedicated substrate probe** (new ED): δσ-μ-shift
vs fractional-Ob compared on BOTH cross-pool uniformity and legibility, touching combat — resolve deliberately,
non-blocking. Keep the kernel's Ob/resistance path clean enough that a fractional-Ob variant is swappable.

### D0-minor — ED citation chain for the Concentration formula
The CR3 `Focus×3` supersession must cite the full chain: **ED-901** (STRUCK `Focus×3`) + **ED-902**
(corrected coefficients to `(3×Focus)+(2×Spirit)` + the Cognition→Focus engine fix) + **ED-933** (params
propagation). Not ED-902 alone. Mechanical result unchanged; use this chain in all fold-in ED entries.

## Good news — the audit shrinks later stages
- **The groundup kernel is 9 modules, not 5** (adds `policy.py`, `faction.py`, `narrative.py`). Bigger
  promotion set, but more is already built.
- **The test suite prints `151 passed, 0 failed`, is seeded (`random.seed(20260603)`) and gates
  (`sys.exit(1 if fail)`)** — RATIFICATION finding #6 is already fixed; the "36/36" and "62/62" self-reports
  are stale. The kernel is far more validated than the docs claimed.
- **`faction.py` already implements §10 BG-Vote (`coalition_vote`), §7.2 Succession (`succession`), and the
  committee band (`band_of`/`rate_banded`)** → **Consensus (Stage 4) is largely promote-existing, not
  author-new.** Real scope reduction.

## Reconciliation map — summary (full table in `reconciliation_map_raw.md`)
| groundup | v30 surface | CR | verdict → handling |
|---|---|---|---|
| `Appeal{ethos,pathos,logos}` (per-move, multiplicative) | adjudicator primary-attr (per-contest) | CR6 | **CONTRADICTORY → D0-1** (build both, A/B) |
| `Stasis.tense{past,present,future}` | genre{Memory,Projection} | CR4 | LOSSY (present/definitional has no genre-tense) → routed to stasis terrain; **resolved in final map, re-verify in Stage 3** |
| orientation{Revealing,Obscuring} | — | CR5 | Direct→Persuasion / Indirect→Face-attack + self-backfire |
| `Standing/Reserve/Room/Readiness` | Composure/Concentration | CR3 | three trackers: Concentration+Face+Persuasion; **Composure retired** |
| per-side advancement clock | Persuasion Track 0-10 banded | — | CLEAN (groundup ships `PersuasionTrack`) |
| win-conditions (6) | the four games | — | Agôn=`PersuasionTrack`; **Consensus mostly in `faction.py`**; Negotiation/Inquiry author-new |
| `DefeatCatalogue`/`SelfGating` | fallacy-as-foul | CR5 | Quintilian/Nyāya nigrahāsthāna |
| resolution substrate | success-count (superseded) | CR2/CR6 | δσ μ-shift via `net_boost`; **housed per D0-2**, TN7-only, fractional-Ob probe per D0-3 |

## Stage 1 entry criteria (what Stage 1 builds, under the agonist/antagonist loop)
1. `sim/autoload/sigma_leverage.py` — numpy-free port + parity test vs the numpy original (D0-2).
2. Promote the **9-module** groundup kernel into `sim/personal/contest/` (config/core/primitives/venues/
   adjudicators/modes/armature/keys/wrapper), re-skinned to the v30 surface, wired to `dice_engine` +
   `sigma_leverage`. Appeal **multiplicative baseline + additive behind a flag** (D0-1).
3. `build_contest` adapter + `resolve_contest` router mirroring `tests/sim/mass_battle/engine.py`
   ("RESOLVES NOTHING") + a `MECHANICS` registry/self-test.
4. Propagate **CR1/CR2/CR3** into the prose head + params (cite ED chain per D0-minor).
5. Golden-trace parity test + preserve the 151-test green. Deprecate (don't delete) the two live stubs.
**Gate A:** `resolve_contest(game='agon')` reproduces canonical agôn at parity; CR1–CR3 ratified.

## ID reservation
Reserved sub-block `contest_rebuild` in `references/id_reservations.yaml`: **ED 1055-1079, PP 800-809.**
