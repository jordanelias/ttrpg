# Audit Verification — 2026-06-22 (audit-of-the-audits)

Independent adversarial re-verification of two prior diagnostics against their cited
canonical sources, to confirm which findings are still live, which have been remediated,
and where the audits themselves err.

**Targets**
- `designs/audit/2026-06-10-investigation-exploration-diagnostic/` (investigation / fieldwork; reversed an earlier PASS to NON-COMPLIANT)
- `designs/audit/2026-06-11-threadwork-resolution-diagnostic/` (threadwork; "design passes NERS / record layer fails S")

**Method.** Per-claim adversarial verification (extract → verify → recheck → adjudicate)
against the live design/params/canon files. The multi-agent workflow runs repeatedly hit a
server-side burst rate limit; the load-bearing claims were therefore verified in the main
loop by direct grep/read (rate-limit-immune), with a strictly-serial workflow corroborating
the long tail. Every verdict cites file:line.

## Bottom line

| Audit | Headline | Survives? |
|---|---|---|
| Investigation | NON-COMPLIANT (E-fail P1 indeterminacy + R-fail P2 ER-2) | **Holds, but only on P1-1.** R-fail leg fell (ER-2 landed 2026-06-22); P1-2 half-fixed; P1-3 propagation largely remediated. |
| Threadwork | design NERS-compliant all directions; record layer FAILS S | **Record-FAIL holds on RD-2/RD-3.** Headline P1 RD-1 fell (ER-2 landed); RD-4 cites phantom PP-604; horizontal STRONG-PASS overstated. |

Both audits were accurate when written and drove real fixes; both are now partly stale in
the **same** place — their shared engine-continuity finding (ER-2) landed 2026-06-22.

## Live defects (already filed 2026-06-11 — re-confirmed, no re-stage)
- **ED-912** P1-1 Disposition/Knot/Ob 3-way split — re-verified LIVE
- **ED-1010** RD-2 per-op Coherence cap homeless + A.10 −2/op contradiction — re-verified LIVE
- **ED-1011** RD-3 Coherence-0 dead pointer (params/core → params/threadwork empty) — re-verified LIVE

## Staged candidates → `ledger_candidates_jsonl_ready.jsonl` (Lane A to file)
- **VER-CAND-01** — close **ED-873 / ED-915 / ED-1012**: ER-2 continuity correction landed (params/core.md:80, git a3d3888c)
- **VER-CAND-02** — narrow **ED-913**: params Thread-Read → Spirit done; only the split `fieldwork_investigation.md` remains
- **VER-CAND-03** — narrow **ED-914**: canonical_sources fieldwork key + split parent paths remediated; PP-719 record + consolidation remain (audit's "0 ledger hits" → actually 1)
- **VER-CAND-04** — NEW P3: threadwork RD-4/Phase-0 cites **PP-604**, absent from both registers (phantom)
- **VER-CAND-05** — NEW P3: threadwork NERS horizontal-E STRONG-PASS ("verbatim, zero divergence") overstated → PASS
- **VER-CAND-06** — provenance: ED-912 / ED-1010 / ED-1011 independently re-verified live

**Discipline note.** Candidates are append-ready proposals; ID allocation and the ledger
status edits (ED-873/915/1012 close; ED-913/914 narrow) are Lane-A structural ops per
`references/lane_assignments.yaml`. Nothing here is committed or self-filed.
