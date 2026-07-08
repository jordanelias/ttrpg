# Articulation + NPC Behaviour — Findings (adversarially verified)

**Canonical heads:** `designs/articulation/articulation_layer_v30.md` (self-contradicting status
lines: CANONICAL at L6, PROVISIONAL at L2/L9/L363 — confirmed verbatim, unresolved by CURRENT.md)
+ `designs/npcs/npc_behavior_v30.md` (clean CANONICAL, approved 2026-04-17).

## 1. Tracker inventory

Per-NPC Conviction (13 canonical values), Resonant Style (4 values), Thread Sensitivity, Scar
count, Disposition (pervasive, per-PC/per-faction) — the Companion App Active-tier panel
**confirmed to display Disposition and Scar count continuously**, not only after consequential
moments (a genuine legibility strength, not a gap). Articulation's own mechanism: `significance()`
(0–13, banded to render length) and `unarticulated_weight` (per-actor accumulator, unbounded,
never surfaced to the player).

## 2. Interaction chain map

Articulation is a universal Key subscriber (`consumes: {type: "*"}`) but its actual Tier-2
cut-scene trigger table (§3.1, 10 explicit conditions) is far narrower than that universal
subscription implies.

## 3. Cascade check — the Bonded-NPC starvation path

**Confirmed as a genuine, unflagged control-flow gap, control-flow trace independently verified.**
§3.3's `unarticulated_weight` accumulator is claimed to prevent an NPC whose Keys never match one
of the ten §3.1 trigger types from going permanently unrendered ("eventually a routine Key
triggers a higher-significance cut scene"). Tracing the actual §5 pseudocode: the accumulator only
feeds `accumulated_narrative_weight`, one term inside `significance()` — and `significance()` is
computed **only after** `matches_trigger_ruleset(key)` already succeeded. There is no code path by
which accumulated weight alone can cause a non-matching Key to fire. **Correction on framing:**
the critic pass found this is better read as a silent coverage gap than a broken promise — §3.3's
own prose ("a routine Key *triggers* a cut scene") already presupposes a triggering Key, so
calling it an asserted-but-unmet guarantee is mildly overstated, though the practical effect (no
catch-all/overflow trigger exists) is exactly as described.

## 4. Cognitive load — season close as the highest fan-in point

Season close is the one moment designed to synthesize ~9–10 subsystems' state at once. Confirmed
well-covered: faction/political and personal/NPC-relational beats. Confirmed gaps or contested:

- **Thread/Calamity silence** — real but narrower than "zero coverage": no dedicated Tier-2
  trigger exists for off-screen Thread/Calamity events, but Rendering Crisis itself is correctly
  *not* routed through articulation (it's protagonist-played), and Knot-adjacent content still
  surfaces via Tier-3 paragraphs. **Rated P3.**
- **Battle-conclusion self-contradiction** — §3.1's ten triggers do not include
  `scene.battle_concluded`/`scene.investigation_resolved`, yet §6.4 asserts these "already trigger
  Tier 2." Confirmed verbatim, a genuine internal contradiction. **Currency correction:** this is
  not a fresh, unadjudicated gap — **ED-IN-0004 (2026-07-05) already ratified-as-accepted by
  Jordan** the fix (add the trigger rows, correct §6.4), execution just hasn't landed yet. Reframe
  from "flag for Jordan" to "already accepted, track execution."
- **Victory-era transitions are wholly UNKEYED** — no Key type exists at all for MS=0/IP=100/
  all-dissolved world-state transitions (`module_contracts.yaml:689`, ED-1006). **Currency
  correction:** ED-1006 is technically still `status: open` in the flat ledger, but a
  lane-tagged successor, **ED-IN-0014 (2026-07-05), is RATIFIED-AS-ACCEPTED** with a defined
  action (register the Key types). Real gap, already accepted, awaiting execution — not an
  open decision.

## 5. Legibility gaps (severity per critic-corrected verdict)

- **P1 — Victory-era blindness.** Substance and severity both confirmed; correct the currency to
  "accepted, awaiting execution" rather than "open since 2026-06-10."
- **P2 (reframed) — Battle-conclusion self-contradiction.** Substance confirmed; disposition
  corrected to "already Jordan-accepted (ED-IN-0004), execution pending" rather than "needs
  adjudication."
- **P2 (reframed) — Bonded-NPC starvation path.** Control-flow trace confirmed exactly; note this
  exact critique is **already logged in the ledger** (ED-IN-0019/0012, ratified) — so at the
  ledger level it is not unflagged, only unflagged *within the articulation doc's own prose*.
- **P2 — NPC Conviction/Resonant Style never surfaced to the player pre-contest**, yet the Wrong-
  Style Penalty imposes a real institutional cost for guessing wrong. Confirmed in substance; the
  producer mis-homed the citation (the §6.4.1 RS-declaration lock lives in `npc_behavior_v30.md`,
  not `social_contest_v30.md` — corrected here).
- **P3 — Thread/Calamity silence** (downgraded per the narrower framing above).
- **Positive finding, not a gap:** Disposition and Scar count are shown continuously in the
  Companion App, contrary to a "shown only after" hypothesis — confirmed, worth preserving.

## Corrections applied from adversarial pass

The report's mechanical/control-flow claims are all independently confirmed accurate (the status-
line self-contradiction, the §3.1/§6.4 table mismatch, the §3.3/§5 starvation trace). Its main
weakness was a **systematic ~4-day currency blind spot**: three of its five headline findings
(battle-conclusion, victory-era, starvation) were already dispositioned by Jordan on 2026-07-05
(ED-IN-0004/0014/0019) but the report treated them as fresh, open, or needing adjudication. Track
these as "accepted, awaiting execution" going forward, not as open decisions for this audit to
re-surface.
