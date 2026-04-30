# Continued Audit — Batch 5
<!-- generated: 2026-04-29 | scope: social_contest, fieldwork, fractional_province -->

## CONFIRMED CONSISTENT (no action)

- Social contest: Composure→CT feedback is indirect (pool quality). Correct and elegant.
- Social contest CROSS + dual Obscuring: only the larger-movement side triggers Doubt Marker. Readable.
- Fieldwork pool formula: (Attr×2) + History — consistent with combat and contest. Confirmed.
- Fieldwork TS gates: hard gates, no Beginner's Luck. Intentional design pillar.
- Rattled → social fieldwork: clean cross-system coupling. S confirmed.
- Fieldwork Hybrid Offset vs Contest Track Offset: different mechanisms for different action types. Correct.
- BG Parliament pool (Mandate sum): Church weakest in Parliament. Intentional asymmetry.
- Fractional PV math: formula correct in worked example.
- Fractional Accord: controller penalized by adversary's low-Order settlement. Intended.
- Fragmentation→Secession→RM: confirmed as the designed emergence pathway. R confirmed.

---

## GAPS FOUND

### [SOC-01] Hybrid §11 — BG vote winner initiative carry-over not specified
§11 Hybrid: BG Parliamentary Vote runs first, sets Conviction Track offset.
Whether the BG vote winner gains initiative advantage in the following TTRPG contest is not stated.
§5 rolls initiative fresh at exchange 1. But should a faction that "won" the BG layer get any
positional advantage beyond the track offset?
GAP: Hybrid §11 — BG vote winner initiative in TTRPG contest undefined.

### [SOC-02] Chain Contest — lobbying offset vs carry-forward starting track
§6.3: chain contest starts at the final Track position from the prior contest.
§10 BG lobbying: can offset starting track by ±2 (capped 4–6).
In a chain contest, do lobbying offsets apply to the carried-forward starting position,
or is the carry-forward immutable?
GAP: chain contest start position and lobbying offset interaction undefined.

### [FW-01] Domain Echo cap — per-scene (scale_transitions) vs per-season (fieldwork §2.5)
scale_transitions: Domain Echo cap ±2 per SCENE.
fieldwork §2.5: Domain Echo cap ±2 per SEASON.
A player running two investigations producing Domain Echoes in the same season:
scale_transitions allows ±4 total; fieldwork §2.5 caps at ±2 total.
GAP: one of these is wrong. Fieldwork §2.5 is more restrictive and appears intentional
(investigations are slower-burn than personal scenes). Recommend: §2.5 (seasonal cap)
is the correct rule for investigation Domain Echoes; per-scene cap applies only to
immediate personal-scene Domain Echoes (social contest, combat win, etc.).
Needs confirmation and clarification in both docs.

### [FW-02] Knot-mediated remote investigation — Cognition direction
§2.6: Knotted party detection Ob = practitioner's Cognition ÷ 2 (floor, min 1).
Higher Cognition → higher detection Ob → harder for Knotted party to detect.
Is this intended? High Cognition = better at concealing intrusions (precision)?
Or should high Cognition make detection easier (clumsy with too much analytical force)?
No footnote explains the direction. Needs design confirmation.
GAP: Cognition direction for remote detection Ob — intentional or inverted?

### [FRAC-01] PV share formula — division by zero at all-Prosperity-0 province
If all settlements in a province reach Prosperity 0: PV share formula divides by zero.
Extremely rare but reachable via sustained warfare and devastation.
GAP: PV share formula has no zero-denominator guard. Add: "if sum-Prosperity = 0,
PV distributes equally across settlements (1/N each), or province is treated as Uncontrolled."

### [FRAC-02] Consolidation Ob — round-up conflicts with floor convention
§2.4: Consolidation Ob = remaining non-faction PV share × 2, rounded UP.
Valoria convention: all fractions floor. This is the only spec using ceiling.
Either: (a) floor is correct (easier to consolidate — small enclave = low Ob),
or (b) ceiling is intentional (even tiny enclave = full Ob resistance).
GAP: Consolidation Ob rounding — confirm ceiling or change to floor per convention.

### [FRAC-03] Fragmentation Ob formula — internal conflict §2.6 vs §5
§2.6: Ob = 2 + (number of non-Seat-held settlements).
§5 Open Items: "if three factions hold one settlement each, Fragmentation Check multiplies Ob."
These produce Ob 5 vs Ob 6 (or more) for the same scenario.
The §5 note is an unresolved design question, not a patch.
GAP: resolve before implementation. Recommend: §2.6 additive formula (2 + count) is cleaner (E).

### [FRAC-04] Universal victory condition — Seat vs fractional PV
§0 "all 15 territories": does this mean all 15 Seats, or all PV across all settlements?
§2.5 says victory PV count includes fractional shares, but the victory condition itself
uses territory count (not PV sum) as the threshold.
GAP: clarify that universal victory requires all 15 Seats (nominal territory control),
and fractional PV contributes to the PV victory PATH tracking but does not satisfy
the "control all 15" condition unless all Seats are held.

---

## AUTO-APPROVABLE (no design decision)

### [FW-01 fix] Domain Echo cap — update fieldwork §2.5 to clarify scope
Add to fieldwork §2.5: "This seasonal cap applies to Domain Echoes originating from investigation
specifically. Personal-scene Domain Echoes (social contest wins, combat wins per scale_transitions §8)
are subject to the per-scene cap from scale_transitions. Investigation and personal-scene Echoes
accumulate independently toward their respective caps."
This resolves the apparent conflict without changing either rule — the caps apply to different
Echo sources. No Jordan decision needed IF the intended design is that investigations are slower-burn.

### [FRAC-01 fix] PV zero-denominator guard
Add to §2.2: "If sum of all settlement Prosperities in province = 0, distribute PV equally across
settlements (floor(base PV / settlement count), remainder assigned to Seat). Province is treated
as Economically Collapsed — Accord forced to 0 at next Accounting regardless of Order values."
This is a purely defensive guard. No design decision needed.

### [FRAC-03 fix] Strike §5 "multiplies" note, confirm §2.6 additive
§5 note says "multiplies Ob — needs balance verification." The additive formula is cleaner.
Recommend: add a note confirming §2.6 additive is canonical, mark §5 note as resolved.

---

## JORDAN DECISIONS (new, from this session)

- SOC-01: Hybrid §11 BG vote winner initiative — carry-over or fresh roll?
- SOC-02: Chain contest lobbying offset — applies to carry-forward or immutable?
- FW-02: Knot detection Cognition direction — higher Cognition = harder to detect (precision) or easier?
- FRAC-02: Consolidation Ob — ceiling (intentional) or floor (convention)?
- FRAC-04: Universal victory "all 15 territories" — Seats or PV? (Likely Seats; confirm.)
