# VALORIA THREADWORK — SESSION THROUGHLINES
## Date: 2026-04-17 | Source: Stress test batches 1–7, 132 findings
## Context: Videogame implementation. All findings evaluated against that context.

---

## 1. THREAD WAS DESIGNED VERTICALLY BUT NEVER INTEGRATED HORIZONTALLY

The Thread system is internally complete: philosophical foundation → pool construction → co-movement → RS track → Coherence. But every horizontal system that connects to Thread does so at an undefined handoff. Thread-Read generates Evidence at 2–3× the rate of mundane investigation. Domain Echo has no Thread operation mapping — the zoom-out from personal Thread action to faction consequence requires case-by-case design. Conviction Scars register nothing from Thread operations — the most morally extreme actions in the game produce no arc-triggering signal in the NPC behavior system. The pattern across all seven batches is the same: individual systems acknowledge Thread exists but Thread doesn't know them back.

This is not 20 separate gaps. It is one integration pass that never happened. In a videogame engine, every undefined handoff becomes a hardcoded special case or a missing feature. The horizontal integration layer needs to be designed as a layer — a formal document that specifies exactly what fires at every system boundary when a Thread operation resolves.

**Blocking:** P0-11 (Thread-Read evidence), P0-12 (Conviction Scar mapping), P0-20 (Domain Echo mapping), P0-02 (RO as Conviction trigger). See audit register §A.

---

## 2. THE RS BUDGET HAS NEVER BEEN ASSEMBLED IN ONE DOCUMENT

Six independent RS drain sources (Gap persistence, Lock chronic drift, siege, battle, winter, TS 90+ Reality Strain) live across six documents. No document adds them up. This session found that the battle RS drain term from victory_v30 §0.4 (RS −1 per battle on Valorian soil, RS −2 at Campaign/War scale) was missing from every prior RS budget — adding approximately −4 RS/season at peak military activity.

The corrected peak drain in a 30-year campaign at Year 20–25 is approximately **23.25 RS/season at WC 0**, enough to Rupture from RS 45 in under two seasons. This is not a calibration problem. It is a missing aggregation layer. A single RS budget document that owns all inputs — analogous to a cost model — would make every calibration question answerable from one place. Without it, every simulation, every campaign mode, and every difficulty setting operates from an incomplete picture.

**Blocking:** P0-07 (WC as RS variable), P0-08 (R-63 domain rates), P0-09 (battle drain). See audit register §F for corrected budget.

---

## 3. THE ENDGAME SURVIVAL PATH IS NOT NARROW — IT IS SINGULAR

The RS Critical design note describes "a narrow, difficult path" to prevent Rupture. The stress tests show it is one specific path: WC 3 + concentrated mass battle Mending. WC 2 buys roughly one additional season before Rupture — not a viable alternative. Everything else (solo Mending campaigns, Lock removal, gap closure) is insufficient against the corrected peak drain without WC 3's +2 RS/season from active Edeyja Mending.

This has two implications. First, if WC 3 as the singular survival path is intentional design, it should be stated explicitly — the survival contest has one solution and it requires cross-faction cooperation toward the Wardens regardless of political outcome. Second, the WC track needs to be front-and-center in the game's design documentation as the mechanism of the "second contest," not a secondary Varfell-specific advancement track. In a videogame, this means WC state must be surfaced to the player as a primary strategic indicator alongside faction Stability and RS level.

**Blocking:** P0-07, P0-26 (Warden Harvest). See audit register §F.

---

## 4. THREAD'S MORAL WEIGHT IS MECHANICALLY INVISIBLE TO EVERY SYSTEM THAT SHOULD REGISTER IT

Dissolution tears the intelligible face of a living being. Lock prevents becoming. POP rewrites history. These are described in explicitly ontological terms in the design documents. Yet:

- Conviction Scar system: no Thread operation triggers a Scar event.
- NPC Stance Triangles: no defined response to witnessing Restricted Operations.
- Companion departure rules: Thread operations not listed as violation triggers.
- Social contest Adjudicator: no reaction to witnessing Thread use during proceedings.
- AP system: Thread detection → TC pipeline exists but is the only downstream signal.

The moral architecture of the world (Beliefs, Convictions, Knots, Resonant Style vulnerabilities) and the physical architecture of Thread operate in parallel without intersecting. In a videogame this is a critical design failure: every NPC reaction to Thread use must be coded, and the moral consequences of Thread practice are the system's richest source of character-differentiating NPC behavior. An NPC with Faith Conviction who witnesses Dissolution and registers no Scar event is a wasted dramatic moment.

This gap also means that the most strategically powerful actions (Structural Dissolution, Permanent Lock) carry no social cost beyond AP and TC — the systems that should make Thread practice politically and relationally expensive are silent.

**Blocking:** P0-02, P0-12. **Holistic fix needed:** Thread operation → moral consequence mapping across all four systems simultaneously (Conviction Scars, Stance Triangle reactions, companion departure triggers, adjudicator responses).

---

## 5. THE SHARED RS TRACK CREATES A POLITICAL WARFARE DOCTRINE THAT WAS NEVER NAMED

Because RS is a shared track — Rupture ends the campaign for every faction — several coherent strategic behaviors emerge from the mechanics that no document currently acknowledges as intentional design:

- **Lock-and-cede:** Place Locks on critical configurations before military defeat. The conquering faction inherits RS drain and ungovernable provinces (Accord blocked below 2 while Lock holds), gaining territorial control but not TCV.
- **Thread brinksmanship:** Present high-value targets to bait enemy practitioners into attempting high-Ob Dissolution operations near-critical RS, where their failure collapses the world without the player faction bearing the political cost.
- **Niflhel as controlled catastrophe faction:** If Harvest = Dissolution Residue collection, Niflhel is structurally incentivized to maximize Dissolution activity just short of Rupture — the only faction whose strategic interest diverges from RS preservation.
- **Mutual deterrence:** Enemy Dissolution failures hurt all factions equally. Aggressive Thread warfare by any faction is a credible threat against every faction including itself.

These behaviors are not exploits to patch — they are a coherent doctrine of Thread political warfare that the shared RS track generates. In a videogame context they need to be designed as explicit NPC faction AI behaviors (Niflhel actively harvesting, enemy factions weighing Thread risk against shared RS cost) rather than emerging accidentally from player play.

**See audit register P1-06, P1-19, P3-08, P3-09, and Batch 5 §18.**

---

## 6. THE PRACTITIONER ARC IS A DEPLETION-AND-RECOVERY LOOP, NOT A ONE-TIME CRISIS

Coherence depletes at 2–4× the rate of recovery. Thread Sensitivity grows rapidly (Overwhelming Leap ≈ +1 TS at TS 50+, nearly every Leap). The career path of an intensively-used practitioner is: fast TS growth → Coherence burnout → Rendering Crisis → partial recovery (−1 TS permanent) → resume. This is a repeatable loop. The Rendering Crisis is described throughout the documents as a catastrophic endpoint — but it is actually the designed career arc for any practitioner operating aggressively.

In a videogame this matters for three reasons: (1) NPC practitioner AI needs a Coherence decision threshold that governs when to step back, not just a binary "NPC conversion at 0" endpoint. (2) The player practitioner's arc needs UI that makes the loop legible — the degradation and recovery stages should feel like a rhythm, not a series of penalties. (3) The Rendering Crisis arc (one season withdrawal + three Anchoring Scenes + resolution roll) needs to be a designed narrative beat with its own scene structure, not a mechanical checklist that fires offscreen.

**Blocking:** P0-22 (NPC practitioner AI). **See audit register §E, item E-10.**

---

## 7. WC IS THE SPINE OF THE "TWO CONTESTS" BUT IS BURIED IN THE DOCUMENTATION

The victory architecture establishes two simultaneous contests: who governs the peninsula AND whether the world survives. Warden Cooperation is the only faction-choice mechanism that directly addresses the survival contest. WC 3 is the only viable endgame RS path under corrected budget assumptions. Yet WC:

- Does not appear in the RS Critical design note.
- Is not cross-referenced from IP recalibration or the 30-year clock specification.
- Reads in the clock registry as a secondary Varfell-specific advancement track (WR gates WC, suggesting WC belongs to Varfell).
- Is not named anywhere as the answer to the survival problem.

WC is actually a shared track with peninsula-wide RS consequences that any faction can contribute to through Southernmost expedition support. The political contest is the board game. The survival contest is WC. In a videogame, this means WC state needs the same UI real estate as Rendering Stability — it is not a faction-stat sidebar, it is the primary instrument of the second contest.

The IP/expedition tension (high IP forces military attention exactly when Southernmost expedition maintenance is most needed) is also undocumented as a strategic choice architecture. This is the mechanic that makes the two-contest structure actually feel like two simultaneous contests with competing demands on player time. It needs to be surfaced explicitly as a design principle, not left as an emergent coincidence.

**Blocking:** P0-07, P0-26. **See audit register §G (critical path for open items).**

---

## VIDEOGAME-SPECIFIC NOTES

The stress tests were conducted with TTRPG framing throughout (table speed, lookup cost, GM improvisation). Several findings require reframing for videogame implementation:

- **Three-axis Ob, Dissolution Residue tracking, pre-calculation overhead** — all handled by the engine. Not design debt.
- **GM improvisation gaps** (Domain Echo mapping, NPC practitioner AI, Thread moral consequences) — in TTRPG these are GM judgment calls; in a videogame they are missing code. These are more critical for videogame, not less.
- **Ambiguous rulings** (POP on Memory-genre contest, Lock after practitioner death, Knot with threadcut being) — in TTRPG these are resolved at the table per session; in a videogame they must be resolved before implementation or the engine will either hardcode an arbitrary choice or crash at the edge case.
- **Emergent faction behaviors** (Lock-and-cede, Thread brinksmanship, Niflhel harvesting) — in TTRPG these emerge from player creativity; in a videogame they must be designed as NPC AI behaviors or they never appear.

**The videogame context makes ambiguous rulings more urgent, not less, and makes emergent behaviors require intentional design rather than organic discovery.**

---

*Document source: stress test batches 1–7 (session d8b924fb834a398c / thread_stress_2026-04-17). Full finding register: tests/thread_stress/threadwork_audit_register.md.*
