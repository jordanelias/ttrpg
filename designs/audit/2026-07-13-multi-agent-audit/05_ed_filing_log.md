# ED Filing Log — 2026-07-13 Multi-Agent Audit P1 Queue

**Filed by:** sequential ED-filing step (registry-owning agent) over `p1_queue.json` (17 items).
**Date:** 2026-07-13
**Protocol:** each item independently verified against the cited working-tree file/section before
filing; IDs allocated one lane at a time from `references/id_reservations.yaml` (`next_free`, never
max+1); `next_free` bumped and co-committed per lane. All new entries are `status: open`,
`needs_jordan: true` (automated-audit proposals, not yet Jordan-ratified).

**Result: 16 filed, 1 skipped.** Ledger lines appended to `canon/editorial_ledger_<lane>.jsonl`;
`references/id_reservations.yaml` `lane_ids` bumped for all 7 lanes touched.

---

## Filed (16)

| Queue # | ED ID | Lane | File / section (verified) | Verification note |
|---|---|---|---|---|
| 1 | **ED-MB-0008** | MB | `params/mass_combat.md` ~L191-200 vs ~L303-312 | Confirmed: PP-104 Projectile table Heavy DR LP=7/HP=5 vs PP-188 Volley table Heavy Piercing=3; ~2x apart, neither marked superseded. |
| 2 | **ED-MB-0009** | MB | `designs/provincial/mass_battle_v30.md` §A.14 (L698-699) | Confirmed: orphan fragment "must be converted to Mending Stability…" tagged `[EDGE-06 — P1]`; `find -iname '*stage5_clocks*'` returns nothing (cited doc does not exist). |
| 3 | **ED-MB-0010** | MB | `references/module_contracts.yaml` L468 | Confirmed: emits both `scene_outcome.battle_concluded` ("§8.5 verbatim") and correct `scene.battle_concluded`; inline comment already flags "[OPEN — Jordan]" drift. |
| 4 | **ED-SE-0045** | SE | `settlement_layer_v30.md` §1.3 L47 vs §1.8 L169 | Confirmed: `Prosperity × 50` labeled "Gold income contribution to faction Treasury" (L47) vs `Σ Prosperity × 10` faction Treasury income (L169). Same edge, two multipliers. Matches report §3.1 resolution. |
| 6 | **ED-SE-0046** | SE | `settlement_layer_v30.md` §1.2 (L30-39), §1.8 (L160), registry L358/L429 | Confirmed: Fortress-City (S-014) / Cathedral-City (S-036) absent from §1.2 table AND §1.8 base(Type) → W_s uncomputable for the 2 compound types; Village absent from §1.2 (present in §1.8). |
| 7 | **ED-SE-0047** | SE | `settlement_layer_v30.md` §4.7 (L877-878) | Confirmed: modifies "Settlement Wealth" / "Settlement Accord"; §1.3 REVISED schema is Prosperity/Defense/Order, Accord is province-derived. Invalid fields. |
| 8 | **ED-SE-0048** | SE | `settlement_adjacency_v30.md` §1.2 (L34,L36) vs `valoria_geography_v30.yaml` L569-587 | Confirmed: prose "36 settlements"/PP-723/49 edges vs YAML "PP-726 supersedes PP-723", 37 settlements/55 edges. S-ID drift confirmed (S-011 = Spelzdorf in settlement_layer registry vs Stillhelm Watch in YAML+adjacency). |
| 9 | **ED-IN-0046** | IN | `scale_transitions_v30.md` §3.3 (L51) | Confirmed: heading only, blank body (L52), no stub marker, unlike §3.4/§3.6 which carry `[EDITORIAL: ED-748]`. |
| 10 | **ED-IN-0047** | IN | `scale_transitions_v30.md` §1 L19, §3.2 L49 | Confirmed: "GM adjudication" (L19 mode table) and "GM recognises faction scope" (L49) vs no-GM invariant. Same class as ED-WR-0007. |
| 11 | **ED-IN-0048** | IN | `references/canonical_sources.yaml` L223-227 | Confirmed: registered head is `designs/scene/conviction_track_v30.md`; piety_track home `designs/personal/conviction_track_v1.md` exists on disk but is unregistered. Cross-cited to ED-SC-0003 (same naming-collision root cause, SC lane). *(Note: source finding called the registered doc "territorial"; it is the scene-scale head — `designs/territory/conviction_track_v30.md` does not exist.)* |
| 12 | **ED-SC-0016** | SC | `social_contest_v30.md` §7.2.1 L418-425 | Confirmed: Track 4=60/40, 5=55/45, 6=50/50 incoherent under "track-distance weighted" framing; ED-762 in flat ledger is a spec-progression entry with `_migration_flag: ID-CONFLICT` and an orphaned `_migration_alt` carrying the lost succession rationale. |
| 13 | **ED-FA-0035** | FA | `faction_behavior_v30.md` §3.7 L339-355 | Confirmed: `cascade_alignment_modifier` has no definition corpus-wide (all other occurrences are invocations); `expectation_alignment_modifier`'s `× {1,2}` is a bare set literal, magnitude discarded by `sign()`. |
| 14 | **ED-FI-0006** | FI | `fieldwork_v30.md` §2.2 L72 vs §2.3 L104 | Confirmed: §2.2 "+0.15 Ob/wound, NEVER −1D"; §2.3 "−1D per wound, per §2.2" (mis-cites §2.2's opposite rule). Cross-cited ED-PC-0005/0006 + ED-FI-0007. |
| 15 | **ED-FI-0007** | FI | `fieldwork_v30.md` §2.4 L141 vs `params/fieldwork.md` L231 | Confirmed: design doc flat "+1 Ob"; params co-file L231 explicitly "superseded by… +0.15 Ob per wound" under ED-PC-0006. Cross-cited ED-FI-0006. |
| 16 | **ED-FI-0008** | FI | `fieldwork_v30.md` §5.6b L529; `designs/personal/knots_v30.md` §9 L279 | Confirmed: both drain threadcut being's Coherence; P-06 (`canon/02_canon_constraints.md`) states "Coherence does not apply… FAIL if the mechanic applies Coherence to threadcut beings." Cross-file fix (fieldwork + personal/knots). |
| 17 | **ED-WR-0008** | WR | `designs/threadwork/threadwork_v30.md` line 40 | Confirmed: P-25 "Scale-based Mending Stability" override table ends at `| Object |` with zero data rows. |

### Filing-decision notes
- **Items 14 & 15 filed as SEPARATE FI EDs** (ED-FI-0006, ED-FI-0007), cross-citing each other,
  rather than merged — honoring the queue's one-item-at-a-time discipline while recording (in both
  entries) that they may be executed as a single combined wound-language propagation, per report §5.
- **Item 16 (ED-FI-0008)** is a single ED spanning two files (fieldwork §5.6b + `knots_v30.md` §9);
  the identical P-06 defect is replicated in both and the ledger entry mandates a single-pass
  two-file fix (knots_v30 sits outside the fieldwork `canonical_sources` entries).
- **Item 11 (ED-IN-0048)** filed coordinated with open **ED-SC-0003** (cross-cited both directions in
  spirit) so IN's additive registration and SC's naming-collision resolution do not land
  incompatibly. Per report §2.6.
- **Items 1–3 (MB)** filed as three EDs cross-citing one another as a single MB provenance batch.

---

## Skipped (1)

| Queue # | Lane | File / section | Reason |
|---|---|---|---|
| 5 | SE | `settlement_layer_v30.md` §1.3 (Fort Level); `settlement_adjacency_v30.md` §2.2 | **Already tracked — not re-filed.** The core P1 (Fort Level consumed at settlement granularity in `Garrison Strength = Defense × 20 + Fort Level × 30`, §1.3 L48, but defined at province granularity per L22) is **already ratified and tracked under ED-SE-0006** (`canon/editorial_ledger_se.jsonl`, status **open**, execution pending): "Fort Level province-to-settlement inheritance rule (census C5-F6) — RATIFIED default: settlement value = province value." Re-filing would duplicate an existing, decided ledger item — the same anti-duplication discipline the report itself applies in its §5 exclusion list. The finding's residual (§2.2 of `settlement_adjacency_v30.md` mis-cites `mass_battle_v30 §A.4`, the Unit Stat Block, for a "+Fort Level to Defender Ob" fortification rule — L97) is a minor mis-citation that should fold into ED-SE-0006's execution pass, not stand as a new P1. Verified: ED-SE-0006 present on disk and covers the granularity ruling; the §2.2 mass_battle §A.4 citation confirmed at `settlement_adjacency_v30.md` L97. |

---

## Provenance
- **Queue:** `designs/audit/2026-07-13-multi-agent-audit/p1_queue.json` (17 items).
- **Source report:** `designs/audit/2026-07-13-multi-agent-audit/00_cross_reference_report.md` (§5 P1 queue).
- **Ledgers written:** `canon/editorial_ledger_{mb,se,in,sc,fa,fi,wr}.jsonl` (+1 line each, per lane
  count above).
- **Allocation ledger:** `references/id_reservations.yaml` `lane_ids.lanes` — bumped MB 8→11,
  SE 45→49, IN 46→49, SC 16→17, FA 35→36, FI 6→9, WR 8→9.
- All 16 new JSONL lines validated as parseable JSON post-write.
