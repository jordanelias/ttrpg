# Mass-Battle Engine — Primitive Provenance Ledger

**Date:** 2026-06-30 · **Directive (5):** primitives grounded in evidentiary/academic/historical
sources. **Companion artifact:** the machine-readable seed `tests/sim/mass_battle/provenance.py`.

---

## 1. Why a typed provenance registry

The repo already enforces *that* every sim numeric literal is cited (`tools/ci_sim_fabrication_check.py`
requires a `sim_verification_ledger.json` entry or a `# [canonical: …]` comment). That gate answers
"is it cited?" — a binary. The audit's bar is stricter and needs a **tier**: a value cited only because
"it matches Waterloo" *is* cited, yet it is still an **assertion**. So we promote the binary gate to a
typed registry that records *how* each constant is grounded and enforces that **values** terminate at
`derived` while **laws** may terminate at `academic-law` and **history** is only ever a behavior gate.

This is the data backbone for directive (5) and the enforcement hook for the "never an assertion" bar.

## 2. The tiers (terminal dispositions)

| Tier | For | Terminal-OK? |
|---|---|---|
| `derived` | a value computed from a named primitive | ✅ (the only OK terminal for a value) |
| `academic-law` | a cited relationship/shape that parameterizes a derivation (supplies no magnitude) | ✅ (for the law row) |
| `historical` | a documented battle/band used to gate emergent *behavior* | ✅ (as a gate; never a value's provenance) |
| `calibrated` | a free magnitude tuned to hold a band | ❌ **debt** — needs a `retire_to` gate |
| `ungrounded` | no source | ❌ **CI failure** |

## 3. Seed contents (`provenance.py`) and starting counts

The seed catalogs the 9 census findings (F1–F9) plus the three load-bearing laws that must be
*preserved*. Starting histogram (`provenance.counts()`):

```
academic-law: 3   (Lanchester; du-Picq morale σ; cavalry regimes — KEEP, these are correct)
calibrated:  13   (debt — F3..F9 magnitudes/coefficients; each carries a retire_to + gauge_rows)
ungrounded:   2   (F1 cell speeds, F2 cell dimensions — the shape-name assertions; CI-failure targets)
derived:      0   (none yet — every value migration moves a row here; the metric is this going UP)
```

**The success metric:** `calibrated + ungrounded → 0`. Tracked like the repo's ED-citation count
(748→0). The seed is illustrative-but-real; Stage 0 expands it to 100% literal coverage via
`tools/extract_values.py`, which will surface every uncatalogued literal as a fresh `ungrounded` row —
the first honest inventory of the engine's magic numbers.

> The seed stores every `value` as a **string** on purpose: it is a *record* of a constant, not a live
> constant, so it neither trips the fabrication scanner nor changes engine behavior (adding it is
> byte-exact — the gauge digest is unchanged).

## 4. Row schema

`Prov(name, value, loc, tier, source, law, derives_from, gauge_rows, toggle, retire_to, note)`:
- `derives_from` — the primitive a `derived` value is computed from (required for `derived`).
- `law` — the grounded relationship a `calibrated` coefficient parameterizes (separates the *shape* we
  keep from the *magnitude* we must derive).
- `gauge_rows` — the bands that **validate the behavior** (and, for a `calibrated` debt row, temporarily
  *license* it until retired). A calibrated row with no gauge row is unlicensed — a hard error.
- `retire_to` — the derivation a debt row must become.

## 5. CI integration (roadmap Stage 0 → Stage 5)

Extend `tools/ci_sim_fabrication_check.py` with a provenance pass asserting:
1. **Every** sim literal has a `Prov` row (no silent magic numbers).
2. **No `ungrounded`** rows (blocking once promoted in Stage 5).
3. Every `calibrated` row names a `retire_to` **and** ≥1 `gauge_rows` entry that exists in
   `gauge_mb`’s band table and currently passes — the band is what *licenses* a calibration; remove or
   loosen the band and the constant is instantly unlicensed.
4. Every `derived` row names a `derives_from` primitive that exists in the codebase.

Tier/value changes ride the existing editorial co-file gate (`tools/ci_co_file_checker.py` +
an `editorial_ledger.jsonl` ED entry). The `MECHANICS` registry (`engine.py` L29) already carries a
`source`+`toggle` per mechanic; the self-test (`mechanics_selftest`) extends to assert each mechanic's
constants resolve to `Prov` rows with matching toggles — turning the registry into a provenance
self-test.

Day-1 posture: **warnings** (the seed is partial). Stage 5 flips it to **blocking errors** once
coverage is complete and the debt count is zero — that flip *is* the "never an assertion" acceptance.

## 6. Relationship to historical validation (directive 6)

Note the deliberate firewall: a band (e.g. C2 "cavalry vs braced wall repelled") appears in a
`calibrated` row's `gauge_rows` as the thing that **validates the behavior** the constant produces — it
is **never** copied into the value. When `PC_CHARGE_RECOIL` is retired from `calibrated` to `derived`,
the C2 band does not change; it simply continues to validate that the now-derived value still yields the
historical repulse. History stays a top-down gate, exactly as directive (6) requires. The gauge
mechanics live in `04_validation_and_scale.md`.
