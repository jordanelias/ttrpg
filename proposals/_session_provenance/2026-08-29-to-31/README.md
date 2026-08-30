# Session provenance — the working context that drove the design, 2026-08-29 to 08-31

**Why this is committed.** These files were the shared context staged in an ephemeral session
scratchpad and read by ~30 subagent lanes across four exercises. The container that held them is
reclaimed on session end. They are committed because **later phases read them**, and because without
them the design documents cannot be audited — a reader can see what the lanes concluded but not what
they were told, which is exactly the information needed to detect priming. The arc review found a
real priming defect by reading a brief against a lane's output; that check is only possible if the
briefs survive.

**These are working documents, not design.** Nothing here is canon, ratified, or a mechanism. Under
`CLAUDE.md` §0.05 they are reference. Several contain claims later corrected — those corrections are
in the design documents and in the adjudication register, not retrofitted here, deliberately, so the
record shows what was believed at the time.

| file | what it is | phase it served |
|---|---|---|
| `AXIOM.md` | Jordan's containment axiom, captured mid-session — family and community as first-class rungs, faction as any aggregate at any scale | the from-scratch design |
| `NERS.md` | the NERS charter: elegance as a **ratio** against necessity and robustness, never a fourth averaged axis | the design, then the audit |
| `SPINE_INPUTS.md` | 18 failure modes extracted from the nine-throughline critique, stripped of remediation | the from-scratch design |
| `ARCH.md` | the modular hierarchy adjudication — the module tree **is** the containment ladder ⚠ contains an error corrected by C-1 in the adjudication register | the design lanes |
| `SETTING.md` | the setting content brief — caste, Church, Restoration, Knots, the person, the places | every writing lane |
| `PRECEDENT.md` | cross-game and historical precedent: steals, **nulls**, refusals, scale coupling | the design lanes |
| `BRIEF.md` | the shared writer brief binding all nine design lanes | the from-scratch suite |
| `AUDIT_BRIEF.md` | the NERS audit charter with the false-N-line hunt | the four audit critics |
| `CODESHAPE_FORBIDDEN.md` | PR #342's constraints extracted **verbatim** — forbidden list, ownership table, signatures | the compliance reviews |

Also staged in the same scratchpad and committed alongside the integration suite rather than here:
`PESSIMISTIC_NERS.md`, `RELAY.md`, `FINDINGS_DIGEST.md`.

**Not committed:** the extracted arc corpus (`arcs/`), recoverable at any time from ref
`v30-snapshot-2026-06-28` and therefore duplication rather than provenance.
