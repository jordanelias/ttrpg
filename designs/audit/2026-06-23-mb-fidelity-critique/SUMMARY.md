# Mass-Battle Fidelity Critique — Consolidated (2026-06-23)

Adversarial critique of the live engine (`tests/sim/mass_battle/`) across 8 regions × three lenses
(history / academic theory / acclaimed games), NERS-adjudicated, reconciled with a fidelity +
bottom-up-emergent + clean-hierarchy mandate. Seed: `tests/sim/massbattle_battery/FINDINGS_2026-06-23.md`
+ historical-eval `wf_0cde2440-931`. Authorities: `references/historical/mass_battle_gauge_grounding.md`,
`research/pre_firearms_formations/`, `skills/valoria-resolution-diagnostic/SKILL.md`.

## Headline

Executing the plan bottom-up against the **calibrated gauge** (not the 2×-pace controlled-sweep harness)
materially reframed the "four defects." **One was a genuine code bug (fixed + verified); two are
non-defects / harness artifacts (reconciled, no change); the real formation-fidelity gap is a
multi-subunit phenomenon that belongs to the hierarchy layer.** The calibrated engine is in better
shape than the seed framing implied.

> **Methodological key (load-bearing):** the **gauge** (`run_multi_turn_battle`, 1× pace, history bands)
> is the fidelity authority. The **2×-pace continuous controlled-sweep harness** was built to make the
> hierarchy *visible* (engagements join, variables differentiate) — but it **amplifies cavalry**
> (doubled absolute speed → faster wrap) and used a weaker `heavy_infantry` control. So a controlled-sweep
> number is a hypothesis; a gauge band is the verdict. This distinction resolved D2.

## Verdicts (NERS-adjudicated)

### D1 — charge-recoil over-fires vs infantry — **REAL · FIXED · VERIFIED**
`orchestration.py` L1922-1931: the reciprocal charge-recoil (a braced wall shattering a charger) fired on
**any** higher-momentum actor into a `_subunit_braced` defender — **no actor gate, no zone gate**. An
*advancing infantry line* therefore shattered a held shield-wall (controlled sweep: shieldwall +38.5 / decА 96).
History: a wall **holds** and is attrited (Hastings ~9h then lost), it does not annihilate an equal attacker;
the recoil constant `PC_CHARGE_RECOIL` was calibrated vs *cavalry* charges (Courtrai/Swiss/Waterloo) — grounding §4.3.

**Fix (NERS-N clean — narrows an existing term, adds no apparatus):** added `_is_charge_actor()` (resolution.py)
and gated both recoil branches on **(a) a genuine charge actor** (cavalry/`mounted_archers` or a `charge`
instruction) **and (b) the wall facing the charger** (GREEN/frontal octagon). 
- **Effect:** shieldwall vs advancing line **+38.5/decА 96 → −6.1/decА 36.8** (holds-and-slightly-loses, historically right).
- **Gauge-safe (verified, n=60 post-fix):** C2 cav-vs-braced rawA **3.3** (band 0-30, repelled — recoil still fires for the cavalry charger); C4 **92.9** (75-95), C7 **100** (65-100); mirror unchanged. Non-braced rows are byte-identical by construction (recoil is guarded by `_subunit_braced`).
- **NERS:** N pass (narrowing), E pass (legible: only a charge into a faced wall recoils), R pass (gauge bands held), S pass. **Re-pin required** (braced-scenario digest changes; non-braced byte-exact).

### D2 — cavalry frontal lethality — **NOT A DEFECT · RECONCILED**
Controlled sweep showed cavalry +50.7 / decА 100 vs the `heavy_infantry` control → flagged HIGH by the
historical-eval. **But the calibrated gauge C1 (frontal cavalry vs a steady line) = decА 37.7, in band 35-55.**
The sweep's 100% is the 2×-pace harness amplifying cavalry + a weaker control (heavy_infantry D4/M5 vs the C1
line D5/M6). The engine already encodes Burkholder 2007 (a horse will not charge solid foot; frontal-vs-steady
is contested). **No engine change** — a "fix" would push C1 below band and break C4/C5/C7, failing **NERS-Necessity**.

### D3 — wedge/oblique/manipular underdeliver — **REAL gauge gap · HIERARCHY-LAYER**
Gauge multi (n=120): H2 wedge 45.6 (48-62), H4 Cannae 43.8 (45-62), H5/H6/H7 oblique/manipular below band.
This is real divergence — **but a single subunit cannot express these tactics' mechanism**: the oblique's
*weighted wing* (Leuctra), the manipular's *line-relief* (Pydna/Sabin), the wedge's *depth-concentration*.
The historical-eval reconciliation reached the same conclusion (the single-subunit mirror "cannot express the
oblique order's actual mechanism"). The proper fix is **Phase 2 (the hierarchy)** — a unit with weighted-wing
*subunits* — possibly with the single-subunit gauge rows re-scoped to multi-subunit. Not a single-shape Phase-1 tweak.

### D4 — morale→rout channel — **WORKS · ENHANCEMENT IS HIERARCHY-LAYER**
`morale_check_phase` L308-314 erodes morale on casualty-fraction (cohesion <50%→−1, <25%→−1 more) → routs on
attrition; the macro cavalry-winged envelopment already routs 40/40. `MORALE_PHASE_CAP`/`MORALE_EROSION_DAMP`
are genuinely dead (DRIFT-5) but cosmetic (cap value already = 3.0). The legitimate enhancement — an
**envelopment/encirclement → morale-erosion** channel (du Picq: the moral effect of being outflanked, beyond
the casualties) — makes *width-based* envelopment rout faster; it helps the **macro** layer (and is the
narrower side's penalty, so it does *not* help the single-subunit oblique). Implement as Phase-2 behaviour wiring.

### Region checks (b/c covered above; a/f/g/h)
- (a) combat-pool/σ — low-Command σ-leverage (ED-875/Gate-G8): **OPEN**, re-verify leverage in-band across the Command range.
- (f) Lanchester — melee exponent ≈1 vs the measured p≈1.7 leak: **OPEN check** (`lanchester_signature.py`).
- (g) movement/pace — base pace ~2× too slow to *join* an engagement in budget: **structural** (the proposed simultaneous-12-round + ~2× pace structure addresses it).
- (h) troop-type ladder — **sound** (levy→cavalry orders correctly; gauge §7 / Sabin).

## Bottom-up / fidelity / hierarchy mandate — how it held
- **No flat per-shape bonuses introduced.** D1 *removed* an over-firing term's reach; nothing bolted on.
- **History > theory > games** enforced: D2's "make cavalry decisive" (game intuition) lost to Burkholder's contested-frontal (history) — which the engine already encodes.
- **Hierarchy:** the real formation gap (D3) is the cleanest possible argument *for* enforcing the unit→subunit→cell / formation→subformation→behaviour / strategy→tactic→instruction triples — the tactics that underdeliver are exactly the ones that need subunit-internal structure.

## Phase 2 — the substantive remaining work (hierarchy enforcement)
Make the 3×3 first-class and byte-exact-defaulted (per the approved plan): `Unit.formation`/`strategy`/
`cohesion_priority`, `Subunit.tactic` (first-class; `ROLE_SPEC`→`TACTIC_SPEC`), `resolve_directives` tether,
wire the dead instructions to per-cell behaviour channels (advance/loose/harass → movement/density; then
charge/pin/screen → sigma head), the envelopment→morale channel (D4), and the Hold-shape vs Adapt axis. Validate
via `directive_view()` independence + the one-variable sweeps moving only their level + byte-exact regression at
defaults. **This is where D3's formation fidelity is actually fixed** (weighted-wing oblique, line-relief manipular).

## Artifacts
- Engine: `tests/sim/mass_battle/{resolution.py (`_is_charge_actor`), orchestration.py (recoil gate L1922-1931)}` — D1.
- Verification: `tests/sim/massbattle_battery/{verify_d1.py, gauge_cav_spot.py, baseline_gauge_n120.log}`.
- Plan: `~/.claude/plans/based-upon-findings-so-optimized-kurzweil.md`.
- Read-only otherwise; engine commits via `h.safe_commit()` only.
