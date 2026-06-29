# Territory & Settlement Audit — Round-2 Verification (2026-06-22)

Completes the rate-limit-degraded round-1 audit ([`findings.md`](findings.md)). Two jobs, both run
as adversarial multi-agent passes after the API limits cleared (27 agents, no failures):

1. **Adjudicate the 2 unverified `[R]` leads** (M3 deprecated S-IDs in §3.2/§4.1/§6.3; L3 Bishop-Governor PP-TBD).
2. **Deepen the under-covered D3 doc-consistency sweep** — 4 finders over the territory corpus hunting
   contradictions *beyond* the round-1 findings, each fresh candidate re-verified against ground truth.

**Yield:** both `[R]` leads adjudicated; **18 NEW confirmed contradictions** (D3-1…D3-20, 3 refuted).
Counts: r_leads 2/2 · d3_raw 21 → 18 confirmed / 3 refuted.

---

## `[R]` lead adjudications

### M3-R — **PARTIAL** (medium): stale S-IDs confirmed, but the section attribution was wrong
The deprecated-ID reuse is real, but **§3.2 (Governor Assignment) contains no S-IDs** and is not an
affected section. The live mismatches vs the §2.1 37-entry registry are:
- **§4.1** — `S-015 Gransol Parliament` (now Nordhain; Gransol = S-018), `S-017 Gransol Market Quarter` (now Holzbrück)
- **§6.3** — `S-015 Gransol Parliament`; `S-010 Stillhelm` (now Erntehof; Stillhelm = S-012); `S-003 Valorsplatz Cathedral` (now Königsbrück; Cathedral is an S-001 district); the `S-023–S-025` "Himmelenger" block (now the secular Halvarshelm-province settlements)
- **Residue (uncited):** §5 L578 `Löwenskyst Fortress (S-006)` → should be S-007; intro L99 `Valorsplatz Cathedral S-003`
- **Fix:** renumber prose S-IDs to the §2.1 registry (or reference by name). Same root cause: half-applied PP-726.

### L3-R — **CONFIRMED** (low): Bishop-Governor is live canon with a placeholder id
`settlement_layer_v30.md:434` defines the Bishop-Governor as live canonical rules (doc Status: CANONICAL;
declarative mechanics; in Part 3 governance canon; **absent** from Part 9 Open Items) but authorizes it only
with `(PP-TBD)`. Greps of `canon/patch_register_active.yaml` and `canon/editorial_ledger.jsonl` for
bishop / Ecclesiastical = **zero hits** — no real id exists. **Fix:** allocate a real ED/PP id, or move to Part 9 until authorized.

---

## NEW confirmed contradictions (D3 deepening)

| ID | Sev | File(s) | Contradiction | Fix |
|---|---|---|---|---|
| **D3-1** | high | settlement_layer §1.8 L169 vs §1.3 L47 / derived_stats §8.1 | Treasury income = `Σ Prosperity × 10` in §1.8 but `× 50` in §1.3 and the cited derived_stats | §1.8 → ×50 |
| **D3-18** | high | mechanics_index.yaml drift_report | Stale/inconsistent: claims 70 mechanics (actual 87), not_implemented 60 (actual 78); breakdown sums to 69 ≠ stated 70 | regenerate drift_report (87 / 78) |
| **D3-2** | med* | settlement_layer §1.3 L43, §1.4.3 L92 | Cite non-existent `derived_stats_v1`; canonical file is `derived_stats_v30` (as §1.8 correctly cites) | retarget to v30 + fix anchor |
| **D3-3** | med | settlement_layer §1.2 vs §1.3 L53 | §1.2 "Stats" column lists phantom stats (Trade/Naval/Garrison Capacity/Piety Influence/Special) not in the canonical 3-stat model (Prosperity/Defense/Order) | reconcile §1.2 to 3-stat model |
| **D3-8** | med | settlement_layer §4.5 vs §2.1 | Local-actor "Count by type" keyed to Port/Mine/Outpost (absent from registry) and omits Village (most common type) | rebuild §4.5 against the real type set |
| **D3-10** | med | settlement_layer §6.1 | Standing track declared 0–5, but §1.4.1 "Wing Slots (Std 6+)" and inner-circle mechanics need 6+ | pick one ceiling document-wide |
| **D3-11** | med | geography YAML L538/556/636 vs settlement_adjacency §1.1 | Edge types `gate`/`sea` used in data but undefined in §1.1's 5-type table; YAML comment mis-cites §1.1 | add Gate/Sea rows, or fix data |
| **D3-12** | med | settlement_adjacency §1.2 vs geography YAML | §1.2 promises 4 specific Thread-Witnessed edges; the canonical YAML block contains **zero** | author the 4 edges, or strike the claim |
| **D3-13** | med | geography YAML L646 | Ehrenfeld↔Himmelenger edge originates from spoke S-015 while all other Ehrenfeld edges use hub S-014 | route from S-014 |
| **D3-15** | med | settlement_adjacency §3 example L125 | Worked example names `S-012 Kronburg Seat` / `S-014 Kronmark Cathedral` — exist in **no** S-ID scheme; asserts a non-existent Gransol↔Kronmark edge | rewrite example against real PP-726 IDs |
| **D3-19** | med | mechanics_index.yaml | 5 mechanics use `test_status: validated_n1000_v12c`, not in the 8-value enum | add the value or normalize the 5 |
| **D3-20** | med | political_hierarchy §1.1, §6 | Monarch named **"Almund"** vs the canonical **"Almud"** (Almqvist) used elsewhere in the same doc | replace Almund→Almud |
| **D3-4** | low | settlement_layer L105/121/135 | §1.5/§1.6/§1.7 mis-leveled as H3, nesting them under §1.4 despite sibling numbering | promote to H2 |
| **D3-5** | low | settlement_layer §1.8 L160 | Village base-weight cites §1.2 + §1.4.1 as ranking source, but Village is in neither (same as H3 root) | add Village rows |
| **D3-6** | low | settlement_layer §1.3 L49 | "Public Order below 0 triggers riot" unreachable (Order 0–5 → PO 0–100); conflicts with "Order 0 = revolt" | trigger at 0 |
| **D3-9** | low | settlement_layer §4.2 | "Market" listed as a settlement type for Guild visibility; Market is a district sub-feature, not a type | remove/re-express |
| **D3-16** | low | settlement_adjacency §1.2 L34, §4 L131 | Still says "36 settlements" vs the canonical 37-scheme | update to 37 / banner |
| **D3-17** | low | geography YAML L1 vs L6/15; settlement_adjacency L12 vs L13 | Each file declares both CANONICAL and PROVISIONAL in its own header | pick one per file |

\* D3-2 verdict was *partial* (anchor confirmed, one sub-claim narrowed).

**Refuted (investigated, not confirmed):** D3-7 (§5.1 capture-bypass not actually self-contradictory),
D3-14 (premise about the S-023 Halvarshelm mapping was wrong), D3-21 (mechanics_index "all 15 territories"
note does not actually conflict with the PP-726 hierarchy).

---

## Disposition

Round-1 + round-2 together = **19 + 18 = 37 confirmed defects** plus 3 gaps and 2 design-rulings. Almost
all trace to the **half-applied PP-726 migration** (36→37) — a single coordinated propagation pass closes
the bulk. Ownership:
- **Lane A** (`designs/territory/**` content, `designs/provincial/**`): the doc-consistency fixes (most D3 + M-series + the M3-R renumbering + D3-20 Almud).
- **Lane B** (`canon/mechanics_index.yaml`, tooling): D3-18 / D3-19 / L1-L2 / M6 — regenerate `mechanics_index` drift_report + index pipelines.
- **Lane C** (`sim/territory/**`): H1 (T16 node), M5 (drift world-arg), G1–G3.
- **Jordan-gated:** L3 (allocate Bishop-Governor id), M7/Q1/Q2 design rulings, D3-10 Standing ceiling.

Nothing here is committed to canon or filed to the ledger — these are verified proposals.
