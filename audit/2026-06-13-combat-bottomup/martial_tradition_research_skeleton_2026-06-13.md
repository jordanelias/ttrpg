# Martial-tradition research skeleton — harvesting reusable elements for the ability system (PROVISIONAL)

**2026-06-13 · status: PROPOSED, Jordan-vetoable · a reusable research instrument, built on the consolidated master**

**Purpose.** A repeatable instrument for searching real martial traditions and extracting their *distinctive
mechanical elements*, mapped to the consolidated ability system's primitives (channels · behavior-accesses ·
weapon-physics · modes), so that **even a sparsely-documented tradition contributes whatever is unique** — and that
unique element becomes a recombinable component for tradition-making and for dual-mastery synthesis. Completeness is
not the goal; *distinctiveness* is. We harvest **mechanics**, decoupled from the source culture — the game's
cultures, names, and lore are Jordan's (mechanical-vs-creative). A harvested element is a mechanical package that any
of the game's own traditions can later wear.

`[Built on: combat_ability_system_consolidated_master_2026-06-13.md — channels, accesses, weapon-physics, modes]`

---

## §1 — The capture schema (the fillable record)

Per tradition, capture this — partial is fine; the starred field is load-bearing and is filled *even when the rest
is thin*.

```
TRADITION RECORD
  identity      : name · lineage/region/era · ROBUSTNESS {robust | partial | fragmentary}
  sources       : the strongest sources reached + tier (T0–T3, §2) + CONFIDENCE per claim
  weapon-physics: weapon(s) + property profile mapped to the WEAPONS keys
                  {reach · head{point|cut_thrust|blunt|…} · blade_guard · percussion/mass/pob ·
                   clinch · grip_len/head_len(leverage) · hand(handling)} ·
                  ⚑ NEW AXIS if the tradition forces a property the schema lacks (e.g. rigidity)
  channels      : emphasis per the 7 — Perception · Measure · Timing · Feel · Leverage · Composure · Structure
                  (grounded in what the tradition DOES, not asserted)
  mode/doctrine : the organizing concept → map to an existing mode OR propose a new one
  phase access  : the distinctive behavior-ACCESS per state-graph phase, where one exists —
                  Approach · Reading · Feint · Commit · Defence · Bind · Counter
                  (a learnable transition this tradition gives that others don't)
★ UNIQUE ELEMENTS: the 1–N distinctive mechanical components — what this tradition does that NO other does.
                  Each tagged by reusable type: {channel-emphasis | behavior-access | weapon-property |
                  mode | cost-dimension}. THIS is the harvest; capture it even when everything else is sparse.
  reuse notes   : where each unique element attaches (which phase/channel/weapon) + what it could synthesize with
```

---

## §2 — The search protocol

**Source tiers** (per the project's source-hierarchy; flag confidence, reach the strongest available):
- **T0 — primary.** Historical treatises/manuals (Liechtenauer/Ringeck, Fiore, Capoferro, Silver, the koryū densho,
  I.33/Walpurgis, Sangam-era references) and primary scholarship. The thing itself.
- **T1 — authoritative synthesis.** Academic / serious HEMA scholarship that cites its primaries.
- **T2 — reputable secondary.** Museums, established practitioner organizations, named-expert analysis.
- **T3 — enthusiast/retail/wiki/aggregator. NAVIGATION ONLY** — harvest a lead, an image, a term, a name; never the
  evidentiary basis. Verify upward before trusting an element.

**Query patterns** (chase the *distinctive*, not the overview):
- `"[tradition]" treatise | manual | primary source` · `"[tradition]" "[weapon]" technique how it works`
- `"[tradition]" footwork | guard | timing | defence concept` · `"[tradition]" what makes it distinctive | unique`
- when an element surfaces, drill it: `"[the specific concept]" mechanics`.

**The sparse-tradition rule.** A thin tradition is *not* discarded. Extract the **one distinctive thing** — a
footwork, a timing concept, a weapon, a way of defending — and record it as a reusable element with its confidence
and its best available source. One unique element from a fragmentary art is a full success.

**Decouple culture from mechanic.** Capture the *mechanic* (the trajectory, the timing, the access, the property);
record the source for provenance; leave the cultural/lore framing to Jordan. The harvested element enters the pool
as mechanics, not as a people.

---

## §3 — How the harvest feeds the system

Each captured element becomes a candidate in a **pool of reusable components**:

- **behavior-accesses** (filed by phase) · **channel-emphasis templates** · **weapon-property axes** · **modes** ·
  **cost-dimensions**.
- **Tradition-making (Jordan's):** compose a game-tradition from pool elements — a channel profile + a weapon
  affinity + a set of accesses + a mode. Historical traditions are *templates*; the game's traditions recombine pool
  elements freely (the emergent model permits any coherent combination, and coherence is judged by the channel-physics
  fit, not by provenance).
- **Synthesis feed:** pool accesses populate the bounded dual-mastery synthesis space (a new access composed from two
  pool accesses).
- **Primitive growth:** a genuinely new property axis (e.g. *rigidity*) **extends the WEAPONS schema itself** — the
  harvest can grow the primitive space, not only recombine within it.

---

## §4 — Worked example (scraped this session): Kalaripayattu / the urumi

A deliberately *thin-in-engine-terms* tradition that nonetheless yields four reusable elements none of the existing
8 traditions / 12 weapons cover — the principle, demonstrated.

```
identity      : Kalaripayattu (Kerala/Tamil Nadu; Sangam-era roots) · ROBUSTNESS: partial
                (living art, mechanically thin in our terms; the urumi itself is well-described)
sources       : T2/T3 — Kerala Tourism (urumi page), practitioner/retail descriptions, Grokipedia.
                CONFIDENCE: medium. ⚑ deepen to T0/T1 (Sangam references, academic Kalaripayattu studies) on a
                second pass before any of these become canon.
weapon-physics: urumi — flexible double-edged whip-blade, ~1.5–2 m, hilt with cross/knuckle guard, worn coiled.
                ⚑ NEW AXIS — rigidity: the roster is entirely rigid; the urumi forces a rigid↔flexible axis.
channels      : Structure (body-coordination) HIGH · Timing HIGH · Measure HIGH (perimeter control) ·
                Composure mid · Feel/Leverage low (no bind game) · Perception: it ATTACKS perception (see below)
mode/doctrine : continuous-flow / centrifugal — a new doctrine variant (kin to filipino kinetic-rhythmic but
                perimeter-defensive rather than limb-destructive)
phase access  : Approach/Defence — rotational barrier (below) · Commit — guard-bypass (below)
★ UNIQUE ELEMENTS (4):
   1. weapon-property — FLEXIBLE BLADE (rigidity axis). The blade "coils and turns rapidly"; trajectory is
      whip-driven and unpredictable, so it DEFEATS normal Reading (the line can't be predicted) and normal parry.
      Trades predictability + parryability for control-difficulty + self-risk.
   2. behavior-access (Commit/Defence) — GUARD-BYPASS. The flexible line "curls around the edge of the shield" —
      an attack the rigid-weapon Defence (parry/guard) does not stop.
   3. behavior-access (Approach/Defence) — ROTATIONAL AREA-DENIAL. Continuous figure-eight/circular swings build a
      "shield of whirling steel" — a space-covering perimeter that deters entry without rigid positioning;
      multi-opponent by nature.
   4. cost-dimension — SELF-RISK. On failure the weapon punishes its own wielder (recoil/self-injury); a high
      skill-floor, high-variance cost. A genuinely new *downside* primitive.
reuse notes   : 1 → a flexible-weapon class (new property axis). 2 → a guard-bypass Commit access (attaches to any
                flexible or whip weapon; synthesises with a feint to defeat both read and parry). 3 → an area-denial
                Approach/Defence access (attaches to long/rotational weapons; synthesises with measure-hold).
                4 → a self-risk tag attachable to any high-variance technique to gate its power.
                All four are mechanical — wrap them in whatever culture you wish.
```

This is the instrument's point: a tradition with almost no engine-grade documentation still contributed a new
weapon-property axis, two new accesses, and a new cost-dimension — four recombinable components for the pool.

---

## §5 — Status / honesty

- This is the **instrument**, not the filled research. Running it across a target list produces one record per
  tradition and grows the pool.
- The urumi example is a **single demonstration** on T2/T3 sources (medium confidence); flagged for primary-source
  deepening before canon. `[CONFIDENCE: medium — secondary sources; T0/T1 pass pending]`.
- **Mechanical, not creative.** The pool is a mechanical-component library; tradition names, cultural framing, and
  lore are Jordan's. Historical sources are templates and provenance, never gates.
- **Next:** agree a target tradition list (European HEMA core + a wide net for distinctive non-European elements),
  run the schema per tradition, and assemble the pool; deeper passes chase T0/T1 for the high-value elements. The
  instrument is promotable to `references/` or a triggerable skill once the schema proves stable.

Provisional; engine unchanged. The skeleton: **search → extract the distinctive → record in ability-system terms →
pool the reusable element → recombine into the game's own traditions and syntheses.**
