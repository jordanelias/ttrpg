# Gap-closure G3 — threadwork/FI/sigma probes

_Archived verbatim from the agent's final message (2026-07-07)._

# G3 Gap-Closure Report — C-TW / C-FI / C-SIG

## Gap 1 — C-TW runtime-confirmation (Mending, Weaving, Leap)

**Probe:** Executed `sim/thread/operations.py`'s `attempt_mending`, `attempt_weaving`, `attempt_leap` directly (script: `/tmp/.../scratchpad/gapclosure/g3_ctw_runtime_probe.py`), using a scripted-face RNG stand-in to force Success/Partial/Failure degrees against real actor pools (no mocking of the resolution logic itself — `_resolve_operation`, `roll_pool`, `apply_coherence_delta` all ran for real).

**(a) C-TW-2 — Mending, Relational scale:**
| Degree | `coherence_delta` returned |
|---|---|
| Overwhelming (net=10) | **−1** |
| Partial (net=1, ob=2) | **−2** |
| Failure (net=−5) | **−2** |

Confirmed exactly as claimed: base `-1` (hardcoded in `attempt_mending`, "substrate engagement is inherently deep regardless of scale"), plus the generic `_resolve_operation` Partial/Failure `-1` penalty stacks on top → `-2`.

**(b) C-TW-5 — Weaving, Relational+ scale exceeding the −1 cap:**
| Case | `coherence_delta` |
|---|---|
| Weaving/Relational Success | −1 |
| Weaving/Relational Partial (net=2, ob=3) | **−2** |
| Weaving/Relational Failure | **−2** |
| Weaving/Structural Failure (base −2) | **−3** |

Canon citation for the "−1 cap": `threadwork_v30.md:659` — "At Relational+ scale (base operation cost = −1, already capped): the cap absorbs the residue cost — **total remains −1**." Line 636: "The §3.2 per-operation cap still governs non-FR operations." Weaving is non-FR. The live code produces `-2` (Relational) / `-3` (Structural) on Partial/Failure, both exceeding the canonical −1 ceiling. Confirmed numerically.

**(c) C-TW-3 — Leap docstring vs. behavior:**
| Case | `coherence_delta` |
|---|---|
| Leap Success (any TS band) | **0** |
| Leap Partial (TS=40, net=1, ob=2) | **−1** |
| Leap Failure (TS=40 or 60) | **−1** |
| Leap ineligibility early-return (TS<30) | 0 (the *only* truly-free path) |

Docstring claims "Failure does NOT cost Coherence per §3.2." Confirmed false for the resolved-failure path: `_resolve_operation` unconditionally applies the generic Partial/Failure `-1` penalty regardless of which operation calls it, so a rolled Leap Failure/Partial costs −1 despite the docstring. Only the pre-roll TS<30 eligibility-failure branch (which never reaches `_resolve_operation`) is actually free.

## Gap 2 — C-TW cadence-cap on Anchoring Scene

**Read:** Full `designs/personal/knots_v30.md` (372 lines) plus the source canon `threadwork_v30.md` §3.5/§3.7/Beat 2 (the doc's own citation targets).

**Verdict: cap absent.** §4.4/§8.2 of `knots_v30.md` and §3.5 of `threadwork_v30.md` specify the Anchoring Scene mechanic (Bonds/Spirit check TN7 Ob2, success = +1 Coherence, costs the Knot +1 strain) with **no per-season or per-scene frequency limit** anywhere in either doc. The only caps found nearby are unrelated: "Cap: once per contest" (§4.2 Composure-buffer, a different use-site), Knot count cap `floor(Bonds/2)+1` (unrelated formation gate), and §3.5's own explicit ceiling is only on the *magnitude* ("Cannot exceed 10. Cannot be purchased with CP"), not frequency. §8.3's "Three Anchoring Scenes" is a precondition count for the separate Rendering Crisis Resolution procedure, not a general-use cap. Exploit surface confirmed: nothing stops a player from running multiple Anchoring Scenes per season for repeated +1 Coherence (each costing only Knot strain, which itself decays).

## Gap 3 — C-TW historical-patch callouts beyond R-55/R-57

**Read:** `designs/threadwork/threadwork_v25_historical.md` in full, then cross-checked against the live head `designs/threadwork/threadwork_v30.md` (confirmed canonical via `CURRENT.md:31`).

**Found and still cross-referenced by the current canonical head:** R-54 (Pull duration-ladder correction, `threadwork_v30.md:332`), R-56 (Healing/Overweave Ob escalation, `:448`), R-58 (Mending Stability drain cap on Locks, `:369`), R-63 (variable Mending Stability drift, `:406`), R-67 (Fortification Ob addition, `:311`) — in addition to the already-known R-55/R-57. All five are embedded verbatim as inline "> **Correction (R-NN)**" blockquotes inside the current combat-adjacent threadwork spec, i.e., these are not archived-only artifacts — the live canon still runs on them.

## Gap 4 — C-FI knot-stress staleness against ED-912

**Read:** `tests/sim/fieldwork_lifecycle_stress_01/fieldwork_lifecycle_stress_01.md` (F2 Knot Lifecycle, the 22/24 NERS artifact) in full.

**Verdict: stale, confirmed.** Dated **2026-05-10**, five weeks before ED-912 (resolved 2026-06-28). Its state machine, F-L05 verification-ledger entry, and edge-case analysis (EC-F2.B-01, EC-F2.C-01) all use the pre-ED-912 **monotonic 0→capacity accumulator** ("Distant cap 4 strain," "Close cap 7 strain," "Strain at exactly capacity (4 or 7)") — the exact model ED-912 struck in favor of the bidirectional −5..+5 wear/resilience gauge (rupture only at +5, Close starts at −2, "Tempered" absorb-state at −5, seasonal reinforcement). This directly answers the open question `cluster_C-FI.md:116` already flagged but declined to resolve ("whether the Knot lifecycle NERS-PASS still holds under the current mechanic is an open question this dossier surfaces but does not answer") — it does not hold as-is; the 22/24 pass was never re-run against the current mechanic. Corroborating: `cluster_C-TW.md`'s independent C-TW-12 finding that `sim/personal/knots.py` itself still implements the same superseded PP-632 fixed-capacity model.

## Gap 5 — C-FI SHA-pin freshness

**Probe:** `python3 tools/freshness_gate.py` (report-only, no `--update`).

**Result:** `[GATE PASSED] All canonical sources are current.` 133/133 entries `[FRESH]`, 0 STALE, 0 NO-SHA — including every fieldwork/investigation key (`fieldwork_v30.md` + index/infill, `fieldwork_bg/hybrid/editorial/exploration/exposure/godot/investigation/rationale/socializing/summary`, `investigation_systems_v30.md` + index). **Verdict: the C-FI-11 caveat is closed — the fieldwork/investigation pins currently match live blobs.** (`references/canonical_sources.yaml` was last touched 2026-07-02, commit `f0ed31c`, consistent with this clean run.)

## Gap 6 — C-SIG Ob≥20 reachability

**Probe:** Grepped `designs/` + `sim/` for `base_ob`/Ob configuration ≥8 across contest, fieldwork, faction, mass-battle, and threadwork; then live-executed the candidate.

**Findings:**
- Contest `Venue.base_ob` default 2.0, no venue configs found ≥8 (consistent with prior C-SIG dossier's "max ~4").
- Combat: Ob fixed at 3 (prior dossier, not re-disputed).
- Fieldwork Depth Axis (`fieldwork_v30.md` §1): base Ob reaches **8** at Depth 5 "Unintelligible," stackable via Calamity-radiation/hostile-territory modifiers (explicitly "stacks with all other modifiers") into roughly the low-to-mid teens in the worst case, but no path to 20.
- Faction actions (`faction_action.py`): d6-threshold model with its own degree bands (Overwhelming≥3, Success≥1) — doesn't use an "Ob" field at all, so contributes nothing toward Ob≥8 reachability.
- Mass battle: no configured Ob≥8; `compute_degree`'s `ob` argument is always `max(1, opposing_net)` — dynamic, not a fixed configuration.
- **Threadwork is the real hit:** `sim/thread/operations.py`'s live `DEPTH_OB` = Structural **8**, Foundational **13**; `MENDING_OB` = Structural **7**, Foundational **12** — both actually executed (confirmed via my Gap-1 probe run against `attempt_mending`/`attempt_weaving`).
- **The canonical Three-Axis Ob formula** (`params/threadwork.md:62-63`, PP-622/623): `Total Ob = Depth Ob + Breadth Ob + Distance Ob`. At max axis values (Foundational 13 + Regional 4 + Far 3) this sums to **exactly 20** — landing precisely on the Ob=20 Foundational-band threshold.
- **But it's dead in code.** Live-executed check: calling `attempt_weaving(actor, {'scale':'Foundational','breadth':'Regional','distance':'Far'})` returns `result.ob == 13`, not 20 — `BREADTH_OB`/`DISTANCE_OB` are defined constants never referenced anywhere else in the module (grep-confirmed) and are silently dropped by `attempt_weaving`/`attempt_pulling`/etc., which only ever compute `DEPTH_OB.get(scale)`.

**Verdict for C-SIG-8's latency question:** Ob=20 is **not reachable by any currently live/executable system**. The design intends the Three-Axis formula to reach exactly 20 at Foundational+Regional+Far, but the live sim only implements one of its three axes, capping the real ceiling at Ob **13** (Foundational Depth). This both confirms and sharpens the prior "unreachable, flagged not asserted" verdict: it's unreachable specifically *because* Breadth/Distance are unimplemented, not because no subsystem gets close.

## Gap 7 — C-SIG fifth-kernel hunt

**Probe:** grepped `sim/`, `tests/`, `designs/` for `random.gauss`, `normalvariate`, `d10`, `randint(`, `TN7`, degree/success patterns — targeting exactly the gap the C-SIG dossier admitted (`cluster_C-SIG.md:70`): "I did not audit fieldwork/faction/threadwork's own dice usage for a fifth independent σ-kernel."

**Candidates found, with dispositions:**

| Candidate | Location | Disposition |
|---|---|---|
| **d6 threshold kernel for faction actions** | `sim/provincial/faction_action.py::_successes()` — d6≥4 per die, own `_degree()` bands (Overwhelming≥3/Success≥1/Partial==0) | **Live fifth kernel — strongest finding.** Different die (d6 not d10), different success rule (no negative/critical faces), different degree semantics. Actively exercised by `sim/mc_v18.py` (main campaign runner), `sim/peninsular/season.py`, and full-campaign tests — not dead code. |
| **Gaussian-noise juror-vote model** | `sim/personal/contest/resolver.py::VoteAtClose` — `random.gauss(0, noise)` probit-style per-juror threshold vs `sharpness*gap` | **Live, distinct stochastic mechanism** (not a dice pool at all) coexisting in the same file that explicitly celebrates eliminating "the third σ-kernel hazard" for the main exchange resolution — that consolidation didn't touch this second, separate randomness channel. Opt-in/PROTOTYPE but actively tested (`sim/tests/test_contest_kernel.py`, `_kernel_tests.py`). |
| **Single-die discipline check** | `sim/provincial/units.py:276` — `random.randint(1,10)` single die vs `unit_discipline` threshold (formation-collision resolution) | Minor: single-die pass/fail, no pool/degree bands, bypasses both `dice_engine.roll_pool` and massbattle's own pool functions. Low materiality but architecturally independent. |
| **Duplicated (not divergent) d10 pool** | `sim/provincial/massbattle.py::roll_pool()` (:627) and `::_roll_volley_pool()` (:1053) | Two separate reimplementations of the identical canonical face rule within one file, neither calling `dice_engine.roll_pool`. Redundant, not "broader terms" — same math, just copy-pasted twice (code-hygiene finding, not a new kernel). |
| **d6 flavor roll** | `sim/thread/opposing.py:190` (`shift_roll`, weak-oscillation flavor table) | Not a resolution kernel — cosmetic sub-roll only. |
| **Percentile/d6 world-event rolls** | `sim/world/npe.py` (multiple `randint(1,100)`/`randint(1,6)`) | Narrative/NPC-emergence event rolls, unrelated to TN/Ob degree resolution — out of scope. |

**Net:** the faction-action d6 kernel and the contest jury Gaussian-vote model are the two genuine additions beyond the four already-known kernels (sigma_leverage, combat core, contest resolver, mass battle), both confirmed live via call-site grep, not merely theoretical.
