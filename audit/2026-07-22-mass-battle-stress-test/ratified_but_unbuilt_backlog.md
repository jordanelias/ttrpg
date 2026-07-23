# Mass-battle ratified-but-unbuilt backlog (exhaustive sweep, 2026-07-23)

Built from a 3-way corpus sweep (all mass-battle `audit/` dirs incl. `findings_full.json`; all `proposals/`
+ the `mass_battle_v30.md` canon; all `editorial_ledger*.jsonl` + workplans), deduplicated and
**classified by decision status** — the distinction that matters most:

- **RATIFIED-but-unbuilt** = Jordan actually ruled *build this* (or it's canonical with a PP-NNN rule) and
  it has zero/partial code. These are the genuine deferred commitments.
- **PROPOSED-not-ruled** = the *goal* was ruled or the gap was only *diagnosed*; Jordan has not decided the
  mechanism. **Not broken promises** — the design queue awaiting his rulings.
- **Built-not-ratified** = shipped and live, but formal sign-off is still open (the inverse gap).

Nothing here is a shipped-and-broken *player-facing* feature: the whole spatial engine isn't live in the
game path yet (Stage G, A2 below), so every item is forward roadmap.

## A. RATIFIED-but-unbuilt (real deferred decisions)

| # | Item | Where ratified | Evidence unbuilt | Salience |
|---|---|---|---|---|
| A1 | **Waypoint primitive + `0.5×speed×max-ticks` path-length budget** (free-form ordered per-subunit goal/predicate list — Image 1 wide-arc-then-wrap, Image 2 asymmetric per-wing/interior-strike) | ED-1096 / ED-MB-0001: *"Jordan-ruled path-length budget formula… undeliverable paths rejected at design time"* | `units.py:763` *"NOT enforced here… not built in this pass, flagged as follow-up"*; only the narrow envelop/sweep `_resolve_maneuver_goal` was built; no `PATH_BUDGET` anywhere | **HIGH** |
| A2 | **Stage G / P-DEC-2** — route `resolve_mass_battle`+`faction_action` onto the field engine, retire the integer engine | `spatial_model_v2_plan.md` P-DEC-2: *"RESOLVED → RETIRE THE INTEGER ENGINE… now authorized"* | `HANDOFF_MB.md` — "architecturally-significant cross-lane (MB+FA) epic," not started; `systems/mass_battle/sim/` still integer | **HIGH** (the live bridge — nothing else is live until this) |
| A3 | **Multi-unit Path B** — cross-Unit concurrent fix-and-flank on one shared field (true N-on-1, full-ring, cavalry rear-transit) | `multiunit_envelopment_plan.md`: *"Decisions (Jordan, 2026-06-22). Path B confirmed — bottom-up emergent"* | Same doc: *"still-unbuilt… Phase-1 never started"*; `orchestration.py:2203` still `# future 2v1 support` | **HIGH** |
| A4 | **DG-2 emergent auto-yield + rally exit + pocket exit** (Cannae give-ground) | ED-MB-0005: Jordan *"build it now"* (2026-07-08) | ED-MB-0005: *"NOT built this pass: emergent auto-entry, rally exit, pocket exit"* — only commanded entry shipped | **HIGH** |
| A5 | **Faction Tactic Cards §B.4** (8 factions × 2 cards + shared cards) | `mass_battle_v30.md` §B.4: *"Tactic cards confirmed canonical (PP-283)"* | `sim/tactic_cards.py` = `FACTION_TACTIC_CARD_POOL_MODIFIERS = {}` — empty stub, *blocked since 2026-05-17* pending a contamination audit | **HIGH** (canonical, zero content) |
| A6 | **Reserve formation Phase-3-commit rule** (cannot engage; commits Phase-3 of next turn) | `mass_battle_v30.md` §A.6 + PP-MB-04 / PP-499 | Only hit in the sim is the inert data tag `config.py:290 "Reserve": {…"reserve"…}`; **zero** code consumes the `reserve` instruction | **HIGH** (canon rule, zero code) — distinct from the *geometric* depth-line item A9 |
| A7 | **Feigned Retreat** (deceive → punish the pursuit; Ob-1 pursuit-Discipline check) | §A.6 + PP-256 (*"pursuing Discipline check is Ob 1… Disc-4 ~87%, Disc-1 ~40%"*) + a §B.4 shared card | `grep feigned` in the sim → **zero hits**; the built DG-2 "yielding" is a *different* mechanism (morale give-ground, not a lure+Discipline-check tactic) | **HIGH** (easy to mistake as "covered" by DG-2 — it isn't) |
| A8 | **P-DEC-3 cavalry density cap** (< infantry) | `spatial_model_v2_plan.md` P-DEC-3: *"RESOLVED → per-troop-type density cap (cavalry < infantry)"* | `stage_F_verification.md` / `HANDOFF_MB.md` — *"deferred to keep the reach A/B clean"* | **MED-HIGH** (formations/spacings) |
| A9 | **Reserve / triplex-acies depth-lines + full-ring closure / cavalry rear-transit** | ED-909 (envelopment = wings+cavalry wrap flank AND rear); ED-MB-0017 motivated by Jordan's "units aren't getting behind the enemy" | ED-MB-0017: *"the wrap seals a horseshoe not a full ring… single line only (no reserve/triplex depth-lines)"* | **MED-HIGH** (borderline: the fix ED-MB-0017 only partially answered Jordan's complaint) |

## B. Built-but-NOT-ratified (the inverse gap)

| # | Item | Status |
|---|---|---|
| B1 | **Octagon damage model default-ON** (`PC_OCTAGON_DMG=1`) | Shipped live default-ON (ED-MB-0018/0019), but `needs_jordan: True` on keeping it default-on + the exchange-ratio characterization. A casual `status: resolved` reader would think it closed — it isn't. |

## C. PROPOSED-not-ruled (the design queue — NOT broken promises)

- **DG-6 completion trio** — (b) **conjunctive envelopment gate** (center-holds × cavalry-sufficiency ×
  terrain) + (c) **brace-repel preservation**; and the **CEV-friction default-on flip** (built, gated OFF).
  All "scoped as follow-on" by the audit, `needs_jordan` — Jordan ruled the *goal* (resolve DG-6), not the
  mechanism. (ED-MB-0016.)
- **DG-7 … DG-16 — nine open decision points** (DG-7,8,9,11,12,13,14,15,16: cell-count-generator canon,
  morale floor, cavalry/infantry envelopment differentiation, troop-type speed/dr/stamina, per-cell scope,
  volley-pool grounding, hold-stance semantics, reach ratification, tactics/role-layer grounding). Opened
  2026-07-08 (ED-MB-0007), **never revisited** — the largest single un-ruled batch. (DG-10 since built;
  DG-6 partially.)
- **ED-MB-0008 — two contradictory ranged/volley DR tables**, both live, neither marked superseded (~2×
  apart for the same armour). An importer/player can't tell which governs. `open, needs_jordan`. A live
  data-integrity blocker for any ranged number.
- **A.6 posture↔geometric-shape mapping** (ED-909 residual, "flagged for a follow-up decision," never
  ruled) — the dice-modifier formations (Shield Wall/Wedge/Skirmish/Column) vs the geometric shapes.
- **Inert instructions** (`lure`/`pin`/`screen`/`reserve`/`refuse`) — ED-1043 proposal, gate-by-gate,
  un-approved. (`reserve` overlaps A6.)
- **Per-cell troop-type heterogeneity** (veteran-front/levy-rear) — ED-MB-0006/0007 confirm byte-inert;
  "a legitimate future architecture, not a gauge fix." Diagnosed, not ruled.
- **Perimeter target-point / face-normal geometry** (`perimeter_targeting_geometry_v1.md`) — core concept
  from Jordan's 2026-07-23 drawing, but the spec's details (minor-point priority, ≤60° tip threshold,
  hard-gate vs soft-bonus alignment) are open questions *to* Jordan; entirely unbuilt. **This is the P1
  keystone** — it + A1 retire the scripted maneuver-goals.
- **Command-clamp(1–7) vs subunit-cap(11)** — cap-11 ruled; the >7-command mechanism (subordinate
  officers) explicitly carved out as "a future ED, not silently invented" — un-proposed.
- **Weapon-reach PP-290 ↔ lattice-reach (0.1/0.2/0.3) reconciliation** — flagged/deferred, never ruled.
- **Weapon-physics §7 concentration-error** (T_err/ERR_K) — held (personal-combat-adjacent).
- **Elephants/chariots; Square/cavalry-rhomboid shapes** — roadmap items only (readiness doc), never
  designed or ruled. (Needed for Zama/Gaugamela combined-arms.)

## D. Hygiene / defects (low)
- ED-MB-0009 (dangling `stage5_clocks.md` citation), ED-MB-0010 (fabricated Key-type in
  `module_contracts.yaml`) — both `open, needs_jordan`, registry hygiene.
- **Puncture `int()`-floor** (granularity leak — a continuous momentum edge truncated inside the σ-channel;
  MB sigma path + a related PC-lane ED-PC-0012 on the point mode). One-line fix.

## Reading of the whole

The genuine deferred-commitment list (A) is **~9 items**, and they cluster: the **maneuver/geometry
backbone** (A1 waypoint + the perimeter model → retires the scripted goals), the **capability layer**
(A3 Path B, A5 tactic cards, A6 reserve rule, A7 feigned retreat, A8 density cap, A9 depth/ring), and the
**live bridge** (A2 Stage G). The larger surface is (C) — Jordan's own open **decision queue** (DG-6
completion + DG-7…DG-16 + the reconciliations), which is design work awaiting rulings, not broken builds.
The one thing worth surfacing loudly: **A5/A6/A7 are canonical (PP-283/PP-MB-04/PP-256) with literally
zero mechanical code** — and **ED-MB-0008** (contradictory DR tables) is a live data-integrity blocker.
