# 01_workings — audit provenance manifest

## Status: PROPOSED (audit working record — not canonical design text)

Raw structured outputs and working notes from the 2026-07-04 qualitative NERS audit workflow
(55 agents: 12 dossiers + 5 hunters + 7 lenses + 30 refuters/verifiers + critic). The synthesized
deliverables live one directory up. **Nothing in here is a verdict** — findings in these files
that do not appear in `../ners_qualitative_audit_v1.md` §3 were refuted, deferred-unverified, or
reclassified; check `refuted.json` / `deferred_unverified.json` before citing anything from a
dossier or hunt file as a defect.

| Path | Contents |
|---|---|
| `dossiers/*.json` | The 12 fixed-schema subsystem/shape dossiers (structured output, complete). |
| `dossiers/*.md` | Free-form working notes for the 5 dossier agents that wrote them (7 lanes returned JSON only — that is a scratch-discipline artifact, not missing coverage). |
| `hunts/*.json` + `*.md` | The 5 degenerate-play hunter outputs (23 candidate dominant lines). |
| `lenses/*.json` + `*.md` | The 7 cross-cutting lens outputs (throughlines tree, emergent narrative, playability, cohesion, centralization, sequence/lineage, threadwork applicability). |
| `refutations/*.md` | Per-finding adversarial refutation notes (consolidated from scattered agent-written paths, including a `undefined/` path bug — see audit §8 process note). |
| `confirmed.json` | The 5 findings that survived refutation, with full refuter records. |
| `refuted.json` | The 25 refuted candidates with refutation evidence — design intel (audit §7). |
| `tracked.json` | 62 candidates reclassified KNOWN-TRACKED (existing ED/HANDOFF/queue refs). |
| `p3.json` | 33 P3 candidates (not individually verified). |
| `deferred_unverified.json` | 32 P1/P2 candidates deferred by the verification cap (audit GAP-2). |
| `critic/` | Completeness-critic output (read with audit §8's corrections — it misread scratch placement as missing coverage). |

Workflow: run `wf_5c1fda26-f80` (`ners-qualitative-audit`), session branch
`claude/ners-audit-fable5-9cpfdz`, 2026-07-04.
