# Mass Battle — Findings (adversarially verified)

**Canonical head:** `designs/provincial/mass_battle_v30.md` (+ `mass_battle_integration_v30.md`,
⚠ PARTIALLY SUPERSEDED for pool formula/geometry/formation taxonomy — `tests/sim/mass_battle/
config.py` + `orchestration.py`/`hierarchy/units.py`/`core/exchange.py` are leading canon for
those). Per-cell/Lanchester re-architecture confirmed live (`PER_CELL`/`FIELD_MOVEMENT`/
`PC_NODE_COHESION` default ON, ED-1089/ED-MB-0001). Currency confirmed fresh by the critic pass
(git log: ED-MB-0003/PR #84 is the last mass-battle commit; nothing later changed calibration).

## 1. Tracker inventory

Size 1–7 (`Size=floor(TroopCount/block_size)`, explicit UI text given: "Heavy Infantry —
4,428/5,000 (Size 4)"); Power 1–7 (tier-set, not Size-derived); Discipline 1–7 per-subunit, smooth
penalty; Morale 1–7 per-subunit, continuous (not rounded); Army Morale 0–7 derived composite,
explicitly designed to be the player's single legible indicator; Command 1–7
`clamp(round((2·Cha+Cog)/3),1,7)`; **Cohesion** (`hp/hp_max`, `hierarchy/units.py:1572`) — the
critic pass found this **is** design-doc-named after all (`mass_battle_v30.md:30`, ED-1013 note
explicitly defines it), correcting the producer's "engine-internal only" claim — but it is still
not a first-class *player-facing* tracker. Stamina 0–100 per-subunit; sub-unit count 1–11
(videogame; TTRPG hard cap 3, `SUBUNIT_CAP=11`).

Roughly a third of load-bearing state (per-cell facing zones, stamina, node-relational position,
sibling-morale pull) exists with much finer grain in engine code than in the design-doc tracker
set the prose describes.

## 2. Interaction chain map

- **Command** feeds pool base AND Discipline ceiling AND Morale start/floor AND tactic execution
  AND span-of-control — 4+ multiplicative downstream effects from one stat. Explicit design intent
  ("Generalship dominates," `mass_battle_v30.md:36`), not a bug, but a legibility risk.
- **`subunit_combat_pool` applies the general's FULL Command to every sub-unit independently**
  (`core/exchange.py:71`, PP-504) — Jordan's own team flags this as possibly letting
  spatially-separated fronts each fight at near-full strength simultaneously; **explicitly
  undecided** (`HANDOFF_MB.md:118-121`), gated on Jordan, not blocked on engine work.
- **Three pool-formula generations textually coexist** in the same file (`mass_battle_v30.md:
  28-30`): legacy `min(Size,Command)+Command` (PP-233), ED-899 `2×Command+Lanchester`, ED-1013
  `Command×(1+cohesion)`. Critic caveat: the doc explicitly demotes the first two as
  superseded/off-path and code comments reinforce precedence, so a reader can resolve this by
  tracing the notes — but must still trace three layered notes to do so.
- **Formation dice-modifier table (Shield Wall/Wedge/Skirmish/Column) has no live engine
  consumer.** ED-909 explicitly parked the mapping to the geometric shape system; `config.py:
  60-62` confirms `SHAPE_OFF_MOD`/`SHAPE_DEF_MOD` were **retired outright** ("formations grant NO
  flat per-shape bonuses"). A Godot dev implementing from the prose table alone would build dead
  mechanics.
- **`threadwork_check` phase-boundary hook** — computed nowhere, still an unimplemented stub
  ("TBD pending Thread canon implementation," `mass_battle_integration_v30.md:265`).

## 3. Cascade check

Threadwork↔mass-battle cross-system load is **still present, unreduced, and still bounded only by
narrative-disclosure text, not a mechanical cap.** PP-201/PP-204 read verbatim as literal GM
address text ("the GM should confirm the table understands...", "the GM must inform the declaring
practitioner before the roll... mandatory table information") with **no engine-executable analog
specified anywhere** — in a repo whose explicit premise is "there is no GM." Meanwhile mass
battle's own internal state has grown strictly *more* granular since the 2026-04-04 audit's
19.4/EXTREME cognitive-load finding for Thread-during-Mass-Battle (per-subunit Discipline/Morale/
rout, per-cell facing/stamina/cohesion, sibling-morale pull all added since). The combined load is
very likely still ≥19.4/EXTREME; nothing in the current corpus reduces it.

**Per-unit-count scaling:** decisions scale with sub-unit count, capped at `SUBUNIT_CAP=11` —
linear-and-capped. Tracked-variable count scales with *troop count* via cells
(`CELL_FLOOR=40`..`CELL_CAP=200`, up to `MAX_TROOPS_PER_UNIT=10000`) — up to ~50–250
individually-positioned/faced/fatigued cells per large sub-unit, with **no player-facing cap or
display rule**, decoupled from the capped decision axis. Command clamps 1–7 but sub-units can
number up to 11 — commanding sub-units 8–11 has no defined mechanism (flagged "future ED" in
`HANDOFF_MB.md:38-41`, still open).

## 4. Cognitive load

Assuming a 4-sub-unit army (the engine's own gauge-battery composition): ≈19–20 discrete decisions
for one Phase-1 declaration pass alone; ≈28 trackers on one's own side, roughly doubling to ~50+
including the enemy-side mirror data needed to choose formations/targets. This is **7–10× the
corpus's own stated strategic ceiling of 7** consultations, before Thread is even added. Adding an
embedded Thread practitioner layers +5–6 more trackers/decisions on top — very plausibly still the
single highest cross-system cognitive-load combination in the corpus.

## 5. Legibility gaps (severity per critic-corrected verdict)

- **P1 — No player-interaction/UI model exists for mass battle at all.** Confirmed: `designs/ui/`
  has no mass-battle spec among its 9 files; the only artifact is a dev/test workbench under
  `tests/`, absent from `CURRENT.md` and `designs/ui/`, with no governing design doc.
- **P1 — PP-201/PP-204's enforcement mechanism is literal GM-address text, in a no-GM engine** —
  exactly where cognitive load peaks.
- **P1 — Formation dice-modifier table has no live engine consumer** — computed nowhere; a Godot
  dev following §A.6 alone would build dead mechanics.
- **P1 (nuanced) — Balance is known-broken, not merely uncalibrated,** but the critic pass found
  the producer's "15/20 gauge rows overshoot decisively" framing overstates a more granular
  picture: per `HANDOFF_MB.md:99-125` (ED-MB-0003), of the 15 currently-failing rows, **9 fail for
  a separate, unrelated, not-yet-triaged reason (RC-5)** — only ~6 are the attacker-favor
  overshoot the producer described as the whole picture. The next step is explicitly gated on a
  Jordan ruling (the full-Command-per-subunit question above), not further engine work.
- **P2 — Three pool-formula generations coexist in the same file** (with the precedence caveat
  above).
- **P2 — Sub-unit-count-vs-Command mismatch** (8–11 sub-units, Command caps span-of-control at 7)
  unresolved.
- **P2 — Jargon collision:** engine-internal "cohesion" (`hp/hp_max`) is one character from
  "Coherence" (the core player-facing Thread stat); the doc flags one Command/Coherence trap
  explicitly but never this newer one.
- **P2 — MS/RS naming split** (see the Threadwork findings) reaches into mass battle's own Thread
  section (`params/mass_combat.md`).
- **P3 — orphaned unbannered superseded doc** (`references/mass_battle_redesign_workplan_v1.md`).
- **P3 (corrected) — the integration doc's `LETHALITY_SCALE` restoration item is a disclosed,
  never-built deferred feature, not a silent rename to `CASUALTY_SCALE`** as the producer
  characterized it. The critic pass found the integration doc's own scope line explicitly lists
  "LETHALITY restoration" as deferred-and-never-built; `CASUALTY_SCALE` is a semantically
  different knob (per-tick lethality vs. a damage multiplier), not a renamed successor. The real,
  narrower defect: a canonical doc still orders restoration of a knob the live engine never
  adopted, with no cross-reference disclaiming it.
- **P3 — CURRENT.md's own canonical-head pairing contains friction:** `mass_battle_integration_
  v30.md` is listed as half the canonical pairing, yet its first substantive banner says "don't
  trust these numbers, see config.py instead."
