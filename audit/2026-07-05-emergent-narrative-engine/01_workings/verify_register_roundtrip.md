# Verify: ARC-S07 register round-trip (capstone #10)

## Status: verification notes · Lane IN · 2026-07-05 · role: capstone verifier
Scope: is the typed-vector compilation faithful to `references/arcs/arc_register_factions.md`
ARC-S07 (L10-11)? Does the vector drive the trace beats? Is the two-seed sketch consistent with
the vector mechanics? Do the template-slot examples reference realizable bake assets per s3?
Targets: `spec_sections/s2_q3_arcs.md` §Q3.10 + `spec_sections/s5_season_trace.md` S5.1-S5.8,
cross-checked against `s3_q4_render.md`.

---

## 0. Register source of truth (arc_register_factions.md:10-11), parsed atom-by-atom

`ARC-S07 — Torben Loyalty Clock` `Crown | ALL | ALL`
1. IP 30 → Tutoring Demand fires.
2. Loyalty track (8→0) degrades −1/season when Covert Contact (Intel vs Ob 3/season) FAILS.
3. Loyalty ≤ 3 → Coup Counter +1.
4. Loyalty ≤ 2 → Crown Mandate −2 cumulative.
5. Contact maintained 3 consecutive seasons → floor at 6.
6. Laskaris (PROTECTIVE) delays demand 1 season but flips if Elske Loyalty ≤ 2 (IP +3 immediately).
7. Direction: "Altonian pressure converts the heir into a lever against the dynasty."

Corroborating grounding read:
- `clock_registry_v30.md:27` — Torben Loyalty range **0–7 start 3**, source `params_board_game.md
  §Torben (PP-498)`. (NB: conflicts with register "8→0"; see §5 caveat.)
- `clock_registry_v30.md:16` — Mending Stability (MS), source "params/threadwork.md **§RS Track**"
  → **MS is the compiled name for RS**. `:17` — Church Influence (CI). (s2 claims TC→CI alias via
  ED-731/782, `s2:452`.)
- `clock_registry_v30.md:29` — Löwenritter Autonomy is **categorical** (Loyal/Restless/Autonomous/
  Split), NOT numeric.
- `arc_register_events.md:39` — COLLISION-C combined = **"RS +8, IP +2, TC +2"** (verbatim).
- `arc_register_events.md:50` — COLLISION F "Succession Triangle" exists; `:34` COLLISION B names
  "Torben in Altonia (ARC-S07)". So ARC-S07 feeding B/C/F is grounded.
- `tests/sim/sim_arc_01_...md:64-70` — "Torben Loyalty Clock **8** → tracks down"; end-of-season
  ≥6 = straightforward retrieval/minor Crown cost; 4-5 = Crown Mandate −1 + covert extraction;
  ≤3 = coup trigger #2 + Elske only viable heir. IP-B path: negotiate Altonia direct → Fail =
  Altonian Intel +1 + departure accelerated. **Grounds the 8-start and the branch structure.**

---

## 1. Fidelity of the typed vector to the register — atom-by-atom, BOTH sections

| Register atom | s2 §Q3.10 vector | s5 S5.1 vector | Verdict |
|---|---|---|---|
| scope Crown\|ALL\|ALL | `{faction:[Crown], territories:ALL, mode:ALL}` | `{faction:Crown, territories:ALL, mode:ALL}` | both faithful |
| IP 30 trigger | `clock.IP >= 30` | `clock.IP >= 30` | both faithful |
| Loyalty −1/season on failed Intel vs Ob 3 | pe#1 `-1`/season, cond Intel vs Ob 3 dice_pool | pe#1 `-1`/per_season, cond Intel vs Ob 3 FAILS | both faithful |
| Loyalty ≤3 → Coup Counter +1 | pe#2 `clock.CoupCounter +1` + GAP note (struck) | pe#3 `track.Lowenritter_Autonomy +1` (fork-1 remap applied) | both faithful; two valid representations, both flag fork 1 |
| Loyalty ≤2 → Crown Mandate −2 cumulative | pe#3 `-2 cumulative` | pe#4 `-2` cumulative | both faithful |
| 3 consecutive → floor 6 | pe#4 `floor(6)` one_time | pe#2 `floor 6` once | both faithful |
| Laskaris flip: Elske Loy ≤2 → IP +3 | **pe#5 `clock.IP +3`** | **OMITTED from pe[]** (factored to NPC-ARC-LAK cross_ref) | see §2 finding F2 |
| Laskaris "delays demand 1 season" | not in pe[] (narrated in trace) | not in pe[] (narrated Beat 1.1) | both narrate, neither models; acceptable |
| Direction sentence | verbatim in payload.direction | verbatim in payload.direction | both faithful |

**Every register number is present and correct in at least one section; the delta magnitudes,
floors, thresholds, and Ob values all match.** The compilation is faithful. Divergences are
between-section (§2), not register-infidelity — except the Laskaris-flip omission in s5's own
`pressure_effects` (F2) and the COLLISION-C alias mis-transcription in s2 (F1, now fixed).

---

## 2. Findings

### F1 [FIXED] — s2 mis-transcribes COLLISION-C deltas as aliased "MS/CI"
`s2:116` and `s2:600` rendered COLLISION-C as `MS +8, IP +2, CI +2` while citing
`arc_register_events.md:39`, which reads **`RS +8, IP +2, TC +2`**. s5 (`:293`) and s3 (`:393`)
both use the register-verbatim RS/TC. MS=RS is a real alias (`clock_registry:16`); TC→CI is
*claimed* (ED-731/782) but not verified here and adds reader-confusion against the cited line.
**Fix applied:** both s2 occurrences → `RS +8, IP +2, TC +2` (register-verbatim, unifies with
s5/s3). Register-fidelity strictly improved regardless of whether the CI alias holds.

### F2 [needs — cross-section reconciliation] — Laskaris IP+3 flip is dual-homed inconsistently
Register puts the flip inside ARC-S07's own text AND has NPC-ARC-LAK (`:312-313`) as a separate
arc with the same `Elske Loyalty ≤2 → IP +3` trigger. s2 keeps it as ARC-S07 `pressure_effects[5]`
(but omits NPC-ARC-LAK from `cross_refs`). s5 factors it to `cross_refs:[…NPC-ARC-LAK…]` (but omits
it from `pressure_effects`). Both defensible; neither wrong against the register, but they
disagree. Recommend a single convention: model the flip in NPC-ARC-LAK, cross_ref it from ARC-S07
(s5's factoring), OR keep it inline and add NPC-ARC-LAK to cross_refs (s2). Not applied — it is a
compile-convention call.

### F3 [needs] — `stakes_tags` differ materially between sections
s2 `[gating, pricing, pattern_response]` vs s5 `[pricing, foreclosure]`. `foreclosure` is
strongly grounded (the Altonian-oath ending forecloses `retrieve_as_loyal_heir` — capstone-6
exemplar, s5 Beat 4.2) and is **missing from s2**. `pattern_response` (s2) is weakly grounded in
the register text. `gating` (s2): s5's own S5.4 note (`:481`) argues the one GATED option (Formal
Crown Treaty) is ARC-T17's diplomacy gate, not an ARC-S07 wall — which would exclude `gating` from
ARC-S07. Recommend canonical set ≈ `[pricing, foreclosure]` (s5), with `gating` only if the treaty
option is attributed to ARC-S07. Not applied (design call on the canonical tag set).

### F4 [FIXED] — s5 misspells canon name "Himmensendt" → "Himlensendt"
`s5:80` participating_actors listed `Himlensendt` (no such canon name; Church Confessor is
Himmensendt, register `:47,85,103,118`). **Fix applied:** spelling corrected. Separate open
question (F5): Himmensendt is Church and has **no direct edge to ARC-S07's Loyalty clock**, so the
inclusion itself is questionable.

### F5 [needs] — participating_actors sets diverge and s5's is weaker-grounded
s2 `[Torben, Almud, Ehrenwall/Löwenritter, Laskaris, Elske, Baralta]` vs s5 `[Torben, Almud,
Elske, Laskaris, Himmensendt, Ehrenwall]`. **Baralta** (s2) is grounded via ARC-S45 (Deed Claim
activates on Torben Loyalty ≤3, `:37-38`); **Himmensendt** (s5) is not connected to ARC-S07.
Recommend: include Baralta, drop Himmensendt (or justify). Not applied — casting set is interpretive.

### F6 [FIXED] — s5 `ledger_cause` carried no PP/ED id (schema violation)
Schema (`s2 §Q3.8 :441`) requires `ledger_cause: [PP-NNN | ED-NNN]` (CI-checkable). s5 had a
`{gate_of, cause}` object with no provenance id. The Torben track's cause is **PP-498**
(`clock_registry:27`; s2 uses it at `:560`). **Fix applied:** added
`citation: "PP-498 (…§Torben; clock_registry_v30.md:27)"` while preserving s5's gate semantics.
Residual: the object shape still deviates from the schema's list form (shape-divergence, holonic
guardrail) — flag for compile-lane normalization.

### F7 [needs — minor] — s5 `resolves_via: dice_pool` mis-scopes the trigger
`resolves_via` is a **trigger** field (`s2 §Q3.8 :431`). ARC-S07's trigger is `IP >= 30`, a pure
clock/state read → s2 correctly sets `null`. s5 sets `dice_pool`, conflating the trigger with the
Covert-Contact pressure-effect condition (which is correctly a dice pool, but belongs to the
`pressure_effects[].condition`, where s5 also places it). Recommend s5 → `null`/`state_reader`.
Not applied (single-token judgment; flagging for author).

### F8 [observation — pre-existing corpus tension, not a section defect] — Loyalty 8 vs 0–7/start-3
Register (and sim_arc_01) use **start 8, range 8→0**; `clock_registry:27` canonicalizes **0–7
start 3**. s2 flags and rules this "a looser gloss … not a contradiction" (`:605-606`); s5 uses 8
unflagged. Under the canonical 0–7/**start-3**, the trace's multi-season escalation (8→…→3 by
Autumn) would NOT hold — start-3 is already at the ≤3 escalation threshold. The sections are
faithful to the *register* (which says 8); the register↔clock_registry conflict is a real
pre-existing defect that should route to a Jordan reconciliation (register gloss vs clock_registry
canonical). Note for the compile lane; not a round-trip fidelity failure against the register.

---

## 3. Does the compiled vector drive the trace beats? — YES

Traced each s5 beat back to a vector field:
- Beat 1.1 seed→active ← `trigger clock.IP>=30`; Laskaris 1-season delay narrated (register atom 6a). ✓
- Beat 2.1 Covert Contact Intel vs Ob 3, Loyalty 8 ← pe#1 + sim_arc_01:64 (start 8). ✓
- Beat 3.1 Loyalty≤3 → Autonomy+1 ← pe#3 (fork-1 remap). ✓
- Beat 3.2 COLLISION-C blocked (ARC-T04 dangling) + cosine ARC-S07↔ARC-S20; deltas `RS+8/IP+2/TC+2`
  cited correctly. ✓ (register-authored-only effect; cosine = RENDER-ONLY zero pe — consistent
  with s2 CR-2 / s3 `convergence-effect-provenance`.)
- Beat 4.2 Loyalty=2 + Mandate−2 → foreclosure (Altonian oath); Laskaris may flip IP+3 (Elske≤2)
  ← pe#4 + register atom 6b. ✓
- Beat 4.3 resolved; floor-6 success branch ← pe#2. ✓
All mechanics used by the trace originate in the vector or in cited register/sim atoms. The one
mechanic the s5 vector under-models (Laskaris IP+3, F2) is still narrated correctly and cross-ref'd
to NPC-ARC-LAK.

## 4. Two-seed sketch (S5.6) vs vector mechanics — CONSISTENT

- Seed 42: contact succeeds → floors at 6 → no convergence, Torben retrieved, minor cost, Laskaris
  steady. Mechanically coherent: floor-6 (pe#2) means Loyalty never crosses ≤3 → no escalation, no
  Autonomy increment → ARC-S07↔ARC-S20 pressure never correlates → cosine below threshold; Elske
  Loyalty not ≤2 → no Laskaris flip. Matches sim ≥6 branch. ✓
  - Minor: S5.6 compresses "succeeds" → "floors at 6"; floor-6 actually needs **3 consecutive**
    successes (pe#2). S5.3 states this precisely (`:427`), so the sketch is a defensible shorthand.
- Seed 77 (spine): fail → 3 → 2 → convergence fires (RENDER-ONLY) → Elske sole heir, Laskaris flips
  (NPC-ARC-LAK), Mandate−2, Succession Vacuum (ARC-S35 grounded `:31-32`, "Feeds into COLLISION F"),
  Torben Altonian (foreclosure). Every step maps to a vector pe or grounded cross_ref. ✓
Divergence on {named actors, stakes, outcomes} is real at the data layer (capstone #11 data-level).
s5's own anti-oatmeal sidebar correctly withdraws the "prose distinctiveness by construction" claim
and defers to the ERA gate (consistent with s3 Defense 2). ✓

## 5. Template slots (S5.1 :99-108) vs s3 realizable bake assets — REALIZABLE (one nit)

s3 fragment slot-type enum (`s3 Q4.6.1 :218-221`): entity_name | pronoun | place | axis_label |
causal_connective | time_phrase | chronicler_voice_tag | stat_delta_phrase; all resolve
qualitative/named, never raw id/number (C4).

| s5 slot | s5 type | maps to s3 enum? | realizable source in s3 |
|---|---|---|---|
| {heir} | entity_name | ✓ | targets[].role subject (s3 :230) |
| {sovereign} | entity_name | ✓ | scope.faction leader |
| {foreign_power} | **place/faction** | `place` ✓ ("faction" not in enum — nit) | payload actor |
| {lever_phrase} | axis_label | ✓ | payload.direction (s3 worked ex. :236-244) |
| {loyalty_state} | stat_delta_phrase | ✓ (qualitative, "letters gone cold", never "Loyalty −1") | s3 Q4.6.2 coherence-band exact-match; C4 (s3 :221) |
| {cause_connective} | causal_connective | ✓ | causes[] walk (s3 Q4.4) |
| {chronicler_voice} | chronicler_voice_tag | ✓ | Church Cert-5/Restoration Cert-2 fixed pairs (s3 :53, prose-writer/SKILL.md:151) |

s3's own ARC-S07 worked example (`:236-244`) uses the SAME slots (payload.direction template
source; {entity_name Torben, axis_label Loyalty, causal_connective because, place Crown court};
flash band vs chronicle_paragraph via Church chronicler Cert-5). The significance_band values
(flash/scene/chronicle_paragraph) and the certainty registers s5 references all exist in s3's
fragment schema and the cited canon (`solmund_voice_v30 §18`, `coherence-tiers.md`). **The template
slots reference realizable bake assets.** Only nit: {foreign_power} type "place/faction" should be
`place` (or entity_name) to match the s3 enum exactly.

---

## Verdict
Round-trip is **faithful with fixes**. Every register number (thresholds 30/≤3/≤2, deltas −1/−2/
floor-6/+1/+3, Ob 3, 3-consecutive) is correctly compiled; the vector drives the trace; the
two-seed sketch is mechanically consistent; template slots are realizable per s3. 3 fixes applied
(F1 COLLISION-C RS/TC, F4 Himmensendt spelling, F6 ledger_cause PP-498). 4 items flagged for author/
compile-lane reconciliation (F2 Laskaris home, F3 stakes_tags, F5 participating_actors, F7
resolves_via) + 1 pre-existing corpus tension (F8 Loyalty 8 vs 0–7) + 1 nit (place/faction slot).
None of the flagged items is a register-infidelity; they are between-section divergences and
schema-shape/scoping nits.
