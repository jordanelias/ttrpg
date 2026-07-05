# Refutation — v2_churn on the FABRICATION-HONESTY axis

## Status: adversarial working record, 2026-07-05. Target:
## `narrative_engine_design_v2_churn.md`. Grounding checked: `dossier_forecast_tractability.md`,
## `dossier_combinatorial_census.md`, `params/core.md`, `domain_action_resolver_spec.md`,
## `spec_sections/s5_season_trace.md`.

**Verdict: v2 is honest at the census/load-factorization layer but commits a HIGH-severity
fabrication in §9.1 — its worked forecast numbers are presented as computed "from the live odds
surface" / "one computation," are untagged as illustrative, are internally inconsistent, and are
not reproducible from any resolver in the corpus. The doc's own intro promise ("every load-bearing
number below cites one of them [the dossiers]") is false for §9.1.**

---

## F1 · HIGH · §9.1 forecast numbers are fabricated-and-dressed-as-computed

**Claim.** "Covert Contact = Crown Intel pool vs Ob 3, P(success) ≈ Φ-band ~0.62 (Layer A, from
the live odds surface). *Layer A horizons*: P(Loyalty≤3 within 2 seasons)=P(≥2 failed
contacts)≈0.14→LOW; within 4 seasons≈0.35→GUARDED; under the lever 'assign the spymaster' (Intel
+2 → P(fail)≈0.19/season)... *Layer B (N=64,k=4)*: 9/64 futures co-spike..." Framed as "One stake,
**one computation**, three voices."

**Evidence (all reproduced, `python3` above):**
- **0.62 is not reproducible as a "Crown Intel pool vs Ob 3" bare check.** The tractability
  dossier's own census routes *faction bare-stat* draws through the **domain resolver**
  (`domain_action_resolver_spec.md §1`, Q1 row 4b / Q3), whose grid is `P=clamp(0.5+0.1·M)` →
  0.50/0.60/0.70 in 0.10 steps. **0.62 is off that grid.** Forced instead through the continuous
  dice engine `Φ((μN−(Ob−0.5))/(σ√N))` (μ=0.4,σ=0.8 per die at TN7), **0.62 requires a pool of
  N=8** — but faction Intel is 1–7 (`stats_1_7_scale.md`; census §2). Intel=7 gives only **0.556**.
  So the label "Crown Intel pool" + "Φ-band 0.62" is a resolver/category error producing an
  unreachable number.
- **The 2-season and 4-season horizons cannot share a P.** With P_succ=0.62 (P_fail=0.38):
  2-season P(≥2 fails)=0.38²=**0.144** (matches the doc's 0.14) but 4-season P(≥2 fails)=**0.490**,
  NOT 0.35. To get 0.35 you need P_succ≈0.70 (→0.348). The two "Layer A horizons" were eyeballed
  from *different* success probabilities; they are not a single computation.
- **The lever number silently switches resolver models.** "Intel +2 → P(fail)≈0.19" = base 0.38 −
  0.20 = 0.18, i.e. the **domain resolver's 0.10/point slope**, not Φ (Φ with +2 dice, pool 8→10,
  gives P_fail≈0.28). Base is dressed as "Φ-band," the lever delta is domain-resolver arithmetic —
  incoherent as "one computation."
- **9/64 is a Layer-B ensemble output, but §3 itself concedes Layer B cannot run today**
  (~19 stubs incl. `npc_ai`, no event deck, no smoke oracle — "preconditions before any horizon is
  trusted"). A concrete "9/64 futures co-spike" is presented as "discovered, not authored" with no
  illustrative tag.
- **Violates v2's inherited s5 discipline.** `s5_season_trace.md` tags every illustrative Key
  `[TRACE-ILLUSTRATIVE]` and the illustrative PC `[UNGROUNDED — a trace vehicle]`. §9.1 carries
  NO such tag on any of 0.62 / 0.14 / 0.35 / 0.19 / 9-64, while asserting "from the live odds
  surface" and "one computation."

**REQUIRED_FIX:** Either (a) tag every §9.1 number `[TRACE-ILLUSTRATIVE]` and delete "from the live
odds surface" / "one computation," OR (b) recompute a self-consistent worked example: pick one
resolver, state the pool, and derive the horizons from a single P_fail (2-season and 4-season must
agree with the SAME p). Drop "Crown Intel pool" framing or move to a personal fieldwork pool where
a ~0.6 bare odds is reachable. Delete or explicitly tag 9/64 as illustrative-until-ensemble-runs.

## F2 · MODERATE · §3 "exact Normal first-passage" overstates Layer A scope

**Claim.** "Drift clocks (MS −1/yr, CI +1/season) get **exact Normal first-passage horizons** —
P(threshold within k seasons) with no sampling."

**Evidence.** Dossier Q1 row 1a classifies MS and CI-passive as **deterministic linear drift**
("hitting time = (threshold−x₀)/rate exactly") — zero variance, so "Normal first-passage" is a
mischaracterization (there is no distribution). Worse, **neither is pure drift**: `core.md:100` —
"Thread operations accelerate [MS decay]. Restoration sources can offset" → MS is player-coupled.
Dossier row 1b — CI *generation* (PP-412) is "Accounting-perturbed... some stochastic
(insurgency-driven)." So "exact / no sampling" for MS/CI elides the very coupling the dossier and
core.md flag. Only a *pure* drift residual is exact.

**REQUIRED_FIX:** Restate: pure-drift residual is exact-analytic; MS/CI horizons are analytic
*conditional on no thread-op / restoration / insurgency perturbation*, else Layer-B-coupled. Drop
"Normal first-passage" for the deterministic clocks (it's linear division).

## F3 · MODERATE · anti-slop property (5) RANGE is not a checkable property today

**Claim.** §6: "five **checkable** properties forbid [slop] **structurally**... (5) RANGE —
Expressive Range Analysis as a bake gate."

**Evidence.** ERA is the certifying instrument and per v2's own `s5_season_trace.md §S5.6` it is
**UNBUILT** and a "Stage-5 blocker" (`dossier_nlg_graduation §4 step5/§6`); it is nowhere specified
beyond its name (no metric, no axes, no threshold). Presenting RANGE as a currently-operative
structural forbiddance is an overclaim — the check does not exist. (Properties 1–4 are at least
proposed with mechanisms; 5 is vaporware.)

**REQUIRED_FIX:** Mark (5) RANGE as "proposed gate — ERA unbuilt, Stage-5 blocker," matching s5.
Do not assert "five checkable properties forbid it structurally" in present tense.

## F4 · MODERATE · §9.1 render line drops the "never a promise" honesty bound

**Claim.** §3 honesty bound: horizons are "field pressure under average play, **never a promise**"
(C7; echoed §6 "never promised... expectation-vs-outcome is itself a beat"). §9.1 Cert-2 render:
"**Miss two more contacts and the heir is theirs by spring** — the odds are not kind past that."

**Evidence.** "the heir is theirs by spring" is a flat outcome PROMISE, at the exact render surface
where the discipline must hold — and it promises *foreclosure*, which the trace itself gates on
Loyalty≤2 + Mandate−2 (s5 Beat 4.2), not the Loyalty≤3 the horizon addresses. The computed
P(Loyalty≤3 within 2 seasons)≈0.14 is the opposite of "theirs by spring." The trailing "odds are
not kind" hedge does not neutralize the main clause.

**REQUIRED_FIX:** Rewrite the Cert-2 line as pressure, not verdict (e.g. "miss two more and the
odds turn hard against the Crown"). Add a note that §9.1 render lines are audited against the
never-a-promise bound.

## F5 · LOW-MOD · §6 headlines the smaller bake figure against its own default

**Claim.** §6: "authored bake ≈ **230–450 units** (low-to-mid hundreds), swinging to ~1,200–2,700
if Certainty must gate."

**Evidence.** §10 fork-6 default is "**include**" (Certainty gates the pool) → low-thousands is the
honest headline. `s5 §S5.8 O-6` is explicit: "Do NOT label 350-450 'feasible' while defaulting to
the 5-6× choice: carry low-thousands as the headline under the default." §6 leads with 230–450
anyway. Census §4.3 itself calls the Certainty-in-bake resolution "the single biggest swing factor."

**REQUIRED_FIX:** Under the stated default, lead with ~1,200–2,700 and note 230–450 is the
fork-6-fallback (lexicon-swap) figure — per O-6.

## F6 · LOW · minor citation slips (faithful in the main, loose at the edges)

- "~850KB tests/ arc corpus" (§6): census §5 **corrects** this to ">1MB" (batches 2-8 = 769,581 B
  + ~280KB sim_arc). v2 repeats the figure its own census flagged as an undercount.
- "~12 venue-class scene shapes" (§6): census §4.2 grounded count is **10** ("~12 estimate but the
  grounded count is 10").
- "48 registered types" (§0/§1): the registry **declares 44**; 48 is the physical-`###`-grep count
  (census §1.1). Calling 48 "registered" is loose.
- "~13 structural shapes" (§0.1/§2/§7): census §3.2 gives **range 12–15** from a **24-of-138 arc
  sample**, not a full-corpus census; v2's tilde is honest but never surfaces the range or the
  sampled basis. LOW.

**FAITHFUL (checked, no issue):** §1/§6 "~10³ live Key instances/season" (census §1.4:
1,200–2,000); "~400–550 live strategic variables" (dossier Q4 ≈400–550→O(500)); "NPC (~25–35
named)" (census §1.3, uses the honest recount not the 35 cap); "37 settlements × ~6"; "230–450 …
1,200–2,700 … 10⁶–10⁷ … ~10–30 beats/season" (census §4.3/§4.4 — quoted faithfully); "event deck
7 families, 60–100 target, no deck code exists yet" (census §2, dossier); the determinism guards
(§3) map cleanly to dossier Q5.
