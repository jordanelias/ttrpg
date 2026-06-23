# Territory & Settlement Audit — Findings

**Date:** 2026-06-22
**Scope:** `designs/territory/*` (design source-of-truth) ↔ `sim/territory/*.py` (implementation) ↔ `canon/mechanics_index.yaml` + 2026-06 settlement audit maps.
**Method:** 5-dimension multi-agent sweep (spec↔code, geo-data, doc-consistency, cross-ref/index, stale/gap) with adversarial per-finding verification.

> **Run note (honest):** the multi-agent workflow degraded under a monthly-spend-limit hit (run 1) and persistent server-side rate-limiting (run 2). Dimensions **D4 (cross-ref)** and **D5 (stale/gap)** completed their finder passes via agents; **D1/D2/D3** finders and nearly all adversarial verifiers never completed. The findings below were **recovered from the run journals and then verified directly against ground truth by hand** (file reads + programmatic diffs). Each finding is tagged with its verification status:
> - **[V]** verified directly against the cited file(s) in this audit.
> - **[V-agent]** adversarially verified by a workflow agent (high-confidence verdict).
> - **[R]** recovered from a finder but not independently re-verified — treat as a lead.

---

## Root cause: the PP-726 settlement migration is half-applied

Most doc/data findings trace to one event. On **2026-05-10 (PP-726)** the settlement model was re-cut from a **36-entry** scheme (S-001…S-036, mixing settlements with districts/outposts) to a **37-entry** scheme (S-001…S-037, settlements proper + a "Village" type). `settlement_layer_v30.md` **§2.1/§2.3** and the geography YAML `settlement_adjacency:` block were migrated; **almost nothing else was.** The stale surfaces (§1.1, §4.5, the YAML `settlements:`/`provinces:` blocks, the index file, the UI supplement) are all the same root cause.

---

## HIGH

### H1 — `sim/territory/adjacency.py` is missing the `T16` node  **[V]**
`ADJACENCY['T1']` lists `'T16'` as a neighbor ([adjacency.py:10](sim/territory/adjacency.py:10)) but there is **no `'T16':` key** (dict jumps `T15`→`T17`). Programmatic diff vs the canonical YAML `adjacency:` block: sim has **16 nodes, YAML has 17**; the sole difference is `T16: sim=[] yaml=['T1']`; sole symmetry violation is `T1→T16` with no reverse.
- **Impact:** `ADJACENCY['T16']` raises `KeyError`; `faction_action.py:147` (`adj |= ADJACENCY.get(tid, set())`) silently returns an empty neighbor set for **T16 / Schoenland**, dropping the canonical T1↔T16 coastal edge from all reachability.
- `temperaments.py` *does* define `T16`, so the two sim modules disagree on whether T16 exists.
- **Fix:** add `'T16': {'T1'},` to `ADJACENCY`. (The bug is copied verbatim from the cited source `tests/sim/v17-integration/m1_church_infrastructure.py`.)

### H2 — Geography YAML `settlements:`/`provinces:` blocks are the stale pre-PP-726 36-scheme  **[V]**
`valoria_geography_v30.yaml` header reads `# ─── SETTLEMENTS (36) ───`; the block defines **36** settlements with the **old type vocabulary** (no "Village": distribution is Seat 3, City 4, Town 10, Fortress 5, Port 4, Cathedral 3, Mine 2, Outpost 5). Yet the **same file's** `settlement_adjacency:` block is the 37-node rebuild (55 edges, S-001…**S-037**). **S-037 (Schoenland) is referenced as an adjacency edge target ([line 636](designs/territory/valoria_geography_v30.yaml:636)) but is never defined as a settlement node** — a dangling reference.
- **Fix:** regenerate the `settlements:`/`provinces:` blocks to the PP-726 37-settlement registry (`settlement_layer §2.1` + §2.3 map) so they match the already-migrated adjacency block.

### H3 — "Village" settlement type is used 18× in canon but is undefined  **[V]**
`settlement_layer §2.1` assigns type **`Village`** to ~18 spoke settlements, but the **§1.2 Settlement Types table defines only 8 types** (Seat/City/Town/Fortress/Port/Cathedral/Mine/Outpost) — `Village` is absent there, from the **§1.4.1** facility-slot table, and from the **§4.5** local-actor table. (§1.x line 160 even claims Village is "from §1.2", but it isn't.) These 18 settlements therefore have no defined facility slots, stats column, or local-actor counts.
- **Fix:** add a `Village` row to §1.2 / §1.4.1 / §4.5 (+ §1.3 stats), or retype the spokes as `Town`.

---

## MEDIUM

### M1 — Settlement count contradicts itself: 36 vs 37  **[V]**
`settlement_layer §1.1` table ([line 20](designs/territory/settlement_layer_v30.md:20)) says `S-001 to S-036 / 36`; §2.1 (line 312) and §2.3 (line 354) canonize **37** (S-001…S-037). Same staleness in **§4.5 line 524** ("across 36 settlements") and the **UI supplement line 65** (`settlement_data.tres (36 entries)`).
- **Fix:** update §1.1 / §4.5 / UI supplement to 37.

### M2 — Adjacency edge count is stated three different ways; actual = 55  **[V]**
Programmatic count of `settlement_adjacency:` = **55 edges**. Canon variously claims:
- **55** — YAML L572/L581 ✓ (correct)
- **56** — YAML **L594 (self-contradicts L581 in the same comment block)**, and `valoria_political_hierarchy_v30.md` L4 + L162
- **49** — `settlement_adjacency_v30.md` L4/L36 (stale PP-723 figure)
- **Fix:** reconcile every reference to **55** (or add the intended missing edge and fix the L594 arithmetic).

### M3 — Stale old-scheme S-IDs in `settlement_layer` prose  **[V] / [R]**
§5.1 ([line 578](designs/territory/settlement_layer_v30.md:578)) calls Löwenskyst Fortress **S-006**, but §2.1 assigns **S-006 = Goldenfurt (Town)** and **Löwenskyst Fortress = S-007** (§2.3 confirms old S-006→new S-007). **[V]** Finder also reports §3.2/§4.1/§6.3 reusing deprecated IDs (S-015/S-010/S-003) **[R]**.
- **Fix:** renumber prose S-IDs to the §2.1 registry (or reference by name).

### M4 — `settlement_layer_v30_index.md` is stale  **[V]**
The generated section index predates the doc: it omits **§1.8** entirely, carries wrong line numbers (says §2.1 at line 149; actual 187), and still labels **"PART 2: THE 36 SETTLEMENTS"** (doc now reads "PART 2: THE SETTLEMENTS (PP-726 corrected granularity)").
- **Fix:** regenerate the index.

### M5 — `temperaments.py` drift write/read mismatch  **[V]**
`apply_strain_shock(…, world=W)` writes drift to `world.npc_drift_state` ([temperaments.py:153](sim/territory/temperaments.py:153)), but `temperament_modifiers` reads `_drift_store()` **with no `world` argument** ([temperaments.py:117](sim/territory/temperaments.py:117)) — so it only ever reads the module-level fallback dict. **Drift applied through `world` is invisible to the one consumer that uses it.** Currently latent (the [ASSUMPTION] block says no consumer mutates drift yet), but a correctness landmine the moment one does.
- **Fix:** thread `world` through `temperament_modifiers()`.

### M6 — `mechanics_index` infrastructure note mislabels Axis 4  **[V]**
The note ([mechanics_index.yaml:730](canon/mechanics_index.yaml:730)) lists "Religious Buildings + Templar Stations + Inquisitor Bases + **Forts**". The implemented §1.5 fourth axis is **Church Governor** (`infrastructure.py:84`); Forts are not part of this module (Fort Level is a separate `settlement.py` garrison input).
- **Fix:** replace "Forts" with "Church Governors".

### M7 — Near-identical province names: `Halvardshelm` (T11) vs `Halvarshelm` (T17)  **[V]**
Two **distinct** provinces — T11 Halvar**d**shelm (Varfell duchy, fjord communities) and T17 Halvarshelm (Hafenmark duchy, mining+Guild) — differ by a single letter, and both spellings are scattered across every doc, the sim, and the SVG (`valoria_political_hierarchy_v30.md:117` has both on one line). High typo / mis-assignment hazard.
- **Fix:** editorial ruling — confirm both are intentional and consider renaming one for legibility.

---

## LOW

### L1 — `mechanics_index` marks implemented territory mechanics as `not_implemented`  **[V-agent] / [V]**
`settlement_state`, `infrastructure`, `territory_adjacency`, `territory_temperaments` are all `test_status: not_implemented`, but their sim modules carry real logic and **zero `NotImplementedError`**. Per the index's own legend (line 40) the honest value is **`provisional`**. (Systemic: ~78/88 index entries are stale this way — the four territory entries are the in-scope instances.)

### L2 — "Population" listed as a settlement stat that doesn't exist  **[V-agent] / [V]**
`mechanics_index.yaml:720` note and `settlement.py:2` docstring both say the stats are "Order, Prosperity, **Population**". Canon §1.3 stats are **Prosperity / Defense / Order**; §1.8 marks Population unscaled/PENDING; the code implements **Defense**, not Population.
- **Fix:** replace "Population" with "Defense" in both.

### L3 — `Bishop-Governor (PP-TBD)` placeholder proposal ID  **[R]**
§3.2 defines a Bishop-Governor governor type but tags its authorizing proposal `PP-TBD` while writing it as live canon. Replace with the real ED/PP id or move to Part 9 Open Items.

---

## GAPS (canon declares behavior the code defers)

- **G1 — No settlement registry [V].** `settlement.py` maps 1:1 territory→settlement ([ASSUMPTION block, lines 13-17]); the §1.3 multi-settlement province floor-average aggregation **can never fire** (always averages one synthetic settlement).
- **G2 — Church infra keyed per-territory, not per-settlement [V].** `infrastructure.py` ASSUMPTION (lines 15-19) stores state by `territory_id`; §1.5 specifies "per settlement" and the −4 seizure cap is "per settlement" — silently coarsened to province granularity.
- **G3 — Unused generation constants [V].** `infrastructure.py` defines `PT_GAIN_*`, `CI_GAIN_TEMPLAR`, `ORDER_GAIN_*` per §1.5/§1.6 but **no entry point applies them** — only `build`/`count`/`seizure_ob_modifier` are wired. The per-season PT/CI/Order generation the constants describe is not implemented.

---

## NEEDS A DESIGN RULING (not scored as defects)

- **Q1 — Seat coverage [V data].** Only 3 of 36 YAML settlements are typed `Seat`; 14 provinces have none. Per `settlement_adjacency_v30.md §39` a province hub may be a non-Seat type, so this is **likely fine** — but confirm each province's §2.1 hub assignment.
- **Q2 — Single-settlement provinces [V data].** YAML T7 and T11 have 1 settlement each. §1.1 allows "1–3"; §2.1 (PP-726) mandates "≥2". Resolved once the YAML is migrated (H2).

---

## Spec↔code that is CLEAN (verified, no defect)

- `settlement.py` derived values match §1.3 exactly: Prosperity×50, Defense×20 + Fort×30, Order×20; province Accord = `floor(avg order)`; effective Prosperity = `sum`.  **[V]**
- `infrastructure.py` §1.5/§1.6 constants match canon exactly (PT 0.5/1/2 +0.5 adj; CI +1; seizure Ob −0/−1/−2/−1/−1/−2, cap −4).  **[V]**
- `temperaments.py` §1 weights and §3 faction aggregates match canon (Crown 0.50/0.50, Church 0.20/0.80, Hafenmark 0.55/0.45, Varfell 0.50/0.50).  **[V-agent]**
- Territory adjacency `sim ↔ YAML` parity is exact **except** the H1 T16 omission.  **[V]**
- No `Galbados` placeholder leakage in the territory surface — the Solmund naming law is clean.  **[V]**

---

## Coverage gaps in THIS audit

D1 (spec↔code), D2 (geo-data), D3 (doc-consistency) were completed by **direct hand-verification** rather than the intended agent fan-out + adversarial cross-check, because the API was rate-limited. The deterministic checks (counts, adjacency diffs, formula fidelity) are as reliable hand-done as agent-done; the **judgment-heavy doc-consistency sweep (D3) is the least exhaustively covered** and may have additional contradictions not surfaced here. Re-running the workflow once limits clear would add adversarial verification to the **[R]** leads and broaden D3.
