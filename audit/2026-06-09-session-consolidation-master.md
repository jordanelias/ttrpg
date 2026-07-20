# Valoria — Session Consolidation Master
**2026-06-09 · consolidates this session's four faction-stat audits + re-folds the three drifted active handoffs into one resumption picture**

This is the single working master. It (1) reconciles the four 2026-06-09 faction-stat audits into one comprehensive
account, and (2) folds the three active handoffs (`win-computation-victory`, `active-work-index`, `weapon-physics-stage2`)
back into one resumption index — those three are archived to `archives/handoffs/`; git preserves their full detail.
Consolidation per PI `<document_consolidation>`: collate → reconcile → one master, superseded instances archived.

---

## 0 — What this consolidates (provenance)

**Faction-stat audits (this session — same scope, consolidated in full below):**
- `…/2026-06-09-faction-settlement-attribute-flattening/attribute_flattening.md` — commit `a9cc3101`
- `…/2026-06-09-faction-stat-architecture-review/faction_stat_architecture_review.md` — commit `575a9b96`
- `…/2026-06-09-faction-stat-architecture-review/faction_stat_io_flattening.md` — commit `85e9a620`
- `…/2026-06-09-faction-stat-architecture-review/faction_attribute_ners_value_audit.md` — commit `4127d1e1`

**Active handoffs (archived by this master — folded into §2/§3 below):**
- `win-computation-victory-2026-06-09` (victory/integration; updated 21:00) → archived
- `active-work-index-2026-06-04` (combat/mass-battle/martial/formations master; updated 20:54) → archived
- `weapon-physics-stage2-2026-06-05` (personal-combat weapon physics) → archived

**Precedent base (unchanged, cited):** `faction_stats_renaissance_review.md`, `2026-05-16-faction-ners-all-directions.md`
(10 throughlines, N-PASS), `2026-05-28-resolution-diagnostic/ners_verdict_faction.md` (F1–F9).

---

# PART A — FACTION-STAT ARCHITECTURE (full consolidation)

## A.1 — The picture

Faction stats sit on a settlement/territory **substrate**. Today they are mostly **base** stats (1–7) read by the d+σ
resolver and written by many mechanics — **except Mandate**, which the LPS-2e ruling (Jordan 2026-05-30) already made a
**derived** settlement aggregate (`faction_canon L214`: `Mandate(faction)=clamp(round(7·T/(T+K)),0,7)`, `T=Σ` controlled-
settlement quotient `q=0.5·L+0.5·PS`). `derived_stats §14` still treats Mandate as base — the live contradiction.

**Jordan's hypothesis (architecture review):** generalize LPS-2e — invert primacy so every faction stat becomes
`aggregate(holdings) ⊕ Σ national-event-modifier-Keys`, and retire the `§14` "stats-derived-from-faction-stats" layer
(the capitals). **Verdict: largely correct and NERS-positive** (improves Smooth + Elegant). It is the right direction;
the qualification is Influence and Intel (below).

## A.2 — Contradictions, reconciled (severity-ranked)

| # | Sev | Contradiction | Reconciliation |
|---|---|---|---|
| **C-1** | P1 | Mandate derivation arrow **inverted** — `§14` (Mandate base → Legitimacy `×20`) vs LPS-2e (Mandate = settlement aggregate). | `§14` is the **stale** side (Jordan structural authority + recency). Mandate is derived; `§14`'s Mandate row retires. |
| **C-2** | P1 | Mandate declared derived (`L214`) yet **written at 78 sites** and read as a d+σ input — role-conflation, quantified. | The 78 writes are the **F1 backlog**: re-route each to settlement L/PS or a national-event modifier. Nothing writes Mandate directly. |
| **C-3** | P2 | Treasury **double-sourced** — `Wealth×100` vs aggregated settlement Local Economy. | Inversion resolves it: Wealth = Σ Local Economy; Treasury = that aggregate spent. Drop the `×100`. |
| **C-4** | P2 | Faction-stat **count 6-vs-7** across docs. | Roster is **six** (Mandate, Influence, Wealth, Military, Intel, Stability). Reconcile stray 7-counts on migration. |
| **C-5** | P3 | Prosperity labelled settlement-level in one doc, territory-level in another. | Minor; fix the label on migration (territory-level modifier per P-22). |

## A.3 — Per-attribute NERS + historical value (radically neutral)

| Attribute | N | R | S | E | Historical (load-bearing?) | Verdict |
|---|:--:|:--:|:--:|:--:|---|---|
| **Mandate** | ✅ | ◐→✅ | ✗→✅ | ◐→✅ | strong — legitimacy: papal bulls, investiture, dynastic claim (T-2) | **KEEP** (derived readout) |
| **Influence** | ✅ | ✅ | ◐ | ◐ | strong — Medici patronage / soft power (T-1) | **KEEP** — fix CI/Influence overload; national basis |
| **Wealth** | ✅ | ✅ | ✗→✅ | ✅ | strong — Medici banking, trade revenue | **KEEP** — inversion strengthens; kill double-source |
| **Military** | ✅ | ✅ | ✅ | ✅ | strong — standing armies, fortifications (T-2) | **KEEP** — Wealth-coupling is good |
| **Intel** | ◐ | ✗ | ✗ | ◐ | genuine — Venice Council of Ten, nuncios (T-8) — but mechanically thin (10in/5out) | **KEEP+EXPAND or FOLD** |
| **Stability** | ✅ | ◐ | ◐ | ◐ | strong — succession, coups, Pazzi (T-2) | **KEEP** — narrow the failure-sink |

**Net (neutral):** all six earn their place — each maps to a load-bearing Renaissance dynamic *and* holds a distinct role,
so **none is a clean cut.** The honest **subtraction** is not an attribute but the **`§14` capitals**
(Reputation/Treasury/Levies/Discipline) — vestigial relics of the bare-stat-pool era; their semantics re-home down
(Treasury→economy, Levies→garrison) and the scalings retire. **Intel** is the one keep/cut that turns on a *design
choice*: mechanize information-asymmetry (T-8) to make it a real axis, or fold it into Influence — no thin middle.
**Stability** is over-loaded as the universal failure-sink (45 of 97 writes are `Failure −1`); the inversion's
locus-routing differentiates it. The defensible changes are to **how stats are computed and coupled**, not **which exist**.

## A.4 — Input/output character (drives migration cost)

| Stat | in / out | profile | basis | migration |
|---|---|---|---|---|
| Mandate | 70 / 78 | balanced | settlement aggregate (**defined**) | the backlog (aggregation exists; 78 writes never re-routed) |
| Stability | 49 / **97** | write-heavy | Σ Order + Accord | **heaviest** — homogeneous (`−1` on Failure), clean basis |
| Wealth | 17 / 35 | write-heavy | Σ Local Economy | clean; economic events re-route to Prosperity |
| Influence | 52 / 23 | read-heavy | national/diplomatic (**not** settlement) | light; most "writes" are CI-clock, not the stat |
| Military | 38 / 17 | read-heavy | Σ Garrison + holdings | light; casualties → garrisons |
| Intel | 10 / 5 | read-heavy, tiny | national/institutional (no settlement) | cleanest national-derived |

**Reads need no change** — reading a derived value was never the problem, only writing one. All OUTPUT mechanics reduce to
**five archetypes**, each with a clean re-route target: *action_degree* → settlement-stat change at locus / national-event
modifier; *event* → national-event-modifier Key; *accounting* → re-derive at Accounting; *domain_echo* → settlement-stat
change at scene locus; *cap* (±2, ceiling 7) → derivation clamp. The migration is therefore a **bounded mechanical pass
over the write-sites**.

## A.5 — Migration worklist (if the inversion is adopted)

Re-route write-sites by archetype; leave reads. Order by volume / cleanliness:
1. **Wealth (35)** or **Mandate (78)** first — cleanest settlement basis; best single-stat pilot/sim.
2. **Stability (97)** — heaviest but homogeneous; locus-routing also fixes the over-sink.
3. **Military (17)**, **Influence (23, mostly CI-clock)**, **Intel (5)** — light.

**Touches:** `derived_stats §14`, `faction_canon`, `faction_layer`, `ci_political`, `victory`, `strategic_layer`,
`scale_transitions §5`/Domain Echo (direct-write → settlement-locus), `faction_state_authoring`.

## A.6 — OPEN faction-stat decisions (Jordan)

1. **Adopt / reject the inversion** (substrate primitive; faction stats = `aggregate(holdings) ⊕ Σ national-event-Keys`).
2. **[DECIDE-1] Influence + Intel derivation basis** — national/institutional, *not* a forced settlement sum.
3. **[DECIDE-2] national-event-modifier semantics** — decay / stacking / cap.
4. **Intel: expand (mechanize T-8 information-asymmetry, counter-intel, faction intel differentiation) vs fold into Influence.**
5. **CI vs Influence-stat naming overload** — rename the 0–100 clock or the 1–7 stat.
6. (Minor, resolve on migration: C-4 count, C-5 Prosperity label.)

**Lower-risk alternative to committing canon:** **sim the inversion on one stat** (Wealth or Mandate cleanest) to
pressure-test before touching the design docs.

---

# PART B — OTHER ACTIVE WORK-STREAMS (folded from the archived handoffs)

Concise resumption state; full detail in the archived source handoffs (named per stream).

## B.1 — Combat engine v1 + armature  *(src: `active-work-index-2026-06-04`)*
**Status:** `combat_engine_v1` BUILT + validated; ratification **STAGED, awaiting Jordan.**
**Entry:** on ratification → 3 `safe_commit`s (canonize + `canonical_sources` / `combat_v30` PARTIALLY SUPERSEDED /
deprecate `params/combat.md`).
**OPEN (Jordan):** ratify `combat_engine_v1`; `martial_traditions_synthesis` **D-alpha** (replace vs coexist), **D-beta**
(count = 6), **D-gamma** (grade `'V'` ratify), **D-delta** (in-world naming).

## B.2 — Mass battle + martial traditions  *(src: `active-work-index-2026-06-04`)*
**Status:** mass-battle RATIFIED + CANONIZED (ED-905 discipline); ED-907..910 filed (`aafdc05d`).
**OPEN (Jordan):** gauge **canonical band realignment** (H3/H4 Horseshoe targets non-canonical); **per-cell CAP value**
(blocks density-into-exchange); density magnitude + troop-type→role table (pending research); **ED-910 phase-dependence**
adopt?; **ED-909 residual** (§A.6 dice-modifier ↔ geometric-shape mapping); **NEXT ENGINE REVAMP** (amend ED-816, move
Horseshoe/RefusedFlank to Unit-level Envelopment/Refused-Flank); discipline **4-role wiring** direction.

## B.3 — Weapon physics Stage-2  *(src: `weapon-physics-stage2-2026-06-05`)*
**Status:** build in progress — three-regime derived-physics from committed mass/pob_frac.
**OPEN (Jordan):** three-regime authority/MoI constants (sim-calibrated, vetoable); concentration error params
(`T_err`/`ERR_K`/effect); defender-side wound; draw-rate (~7% vs auto-tiebreak); **P3 over-atomization** per-subsystem
calibrate-or-cut (CFG grouping + impact annotation — **do NOT bulk-delete**; low-impact-in-harness may be untested).

## B.4 — Victory / win-computation / integration  *(src: `win-computation-victory-2026-06-09`)*
**Status:** per-faction victory **NOT canon**; **ED-306 + ED-107 DEPRECATED** (`victory_architecture_v1.md` does not
exist); Mending Stability start 80→60 (`2edf6432`).
**Entry:** territory fallback; **wire `treaty.py`** (~157L implemented, UNWIRED); substrate ED-109/304/312.

---

# PART C — CROSS-STREAM RECONCILIATION (project-level)

- **★ SHARED P1 — the ~94-ID editorial conflict backlog (ED-865/866/867 class).** This is **not** stream-specific: it is
  the combat resolver dispute (B.1/B.2: ED-883/865/866, gates 7 Lane-C stubs + Varfell), the victory backlog (B.4), the
  weapon-physics canonization (B.3), **and** the faction-stat migration (ED-865/874). It **blocks editorial canonization
  project-wide.** Elevate to a single top-level **Jordan-adjudication** item; until resolved, pull clean IDs only.
- **ID coordination (do not collide):** ED lane-B max **884** (`<890`), lane-C next **970** (`970–999`); PP lane-B **726**
  (`<727`), lane-C next **780** (`780–799`). `Command = round((2·Cha + Cog)/3)` (ED-899).
- **Index drift (from bootstrap):** `params/combat.md` manifest path points at a missing file (combat ratification fixes
  it); two active design docs registered to no concept (`ners_verdict_combat_v32.md`, `weapon_axes_v2.md`).
- **Freshness:** 4 stale canonical SHAs — `freshness_gate.py --update` (non-blocking).

---

# PART D — CONSOLIDATED OPEN-JORDAN REGISTER (single list, severity-ranked)

1. **★ P1 — resolve the ~94-ID editorial conflict backlog** (ED-865/866/867 class) — blocks canonization across all four
   streams. Adjudicate / renumber later claimants.
2. **Faction-stat: adopt/reject the inversion** + [DECIDE-1] Influence/Intel basis + [DECIDE-2] national-event semantics
   + Intel expand-vs-fold + CI/Influence naming. *(or sim one stat first)*
3. **Combat: ratify `combat_engine_v1`** (→ 3 commits) + martial-traditions D-alpha/beta/gamma/delta.
4. **Mass battle: gauge band realignment + per-cell CAP** (unblocks density-into-exchange) + ED-910 phase-dependence +
   ED-909 residual mapping + discipline 4-role wiring.
5. **Weapon-physics: three-regime constants + error params + defender-wound + draw-rate + P3 calibrate-or-cut.**
6. **Victory: wire `treaty.py` + territory fallback** (per-faction victory stays non-canon).

---

# PART E — NEXT-SESSION ENTRY POINTS

- **Faction-stat:** make the inversion call (or sim Wealth/Mandate); then the staged write-side migration (A.5). Start
  fresh — canon reloads clean and the migration gets room.
- **Combat:** await Jordan ratify → 3 commits.
- **Mass battle:** Jordan band realign + per-cell CAP → unblock density-into-exchange.
- **Weapon-physics:** Jordan constants → re-baseline.
- **Victory:** wire `treaty.py`; territory fallback.
- **Editorial:** resolve the ID-conflict backlog (Jordan) — clears canonization for everything.

---
*Handoff hygiene: the three active handoffs are archived to `archives/handoffs/`; this master + its companion master
handoff supersede them and add the faction-stat stream. Originals preserved in git. Faction-stat detail in the four audit
docs (§0). NERS per `definitions.yaml`. Structural-ontology calls (the inversion, Influence/Intel basis, Intel scope) are
reserved for Jordan.*
