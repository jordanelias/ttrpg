# ED Options — Candidate Ledger Entries (deliberately NOT filed)

## Status: PROPOSED (candidates only — Jordan picks; nothing here is in the ledger)
## Date: 2026-07-05

**These are candidates, not allocations.** Per the read-only mandate (charter) and the merge-ratifies
convention (ED-1094), merging this PR ratifies the audit's *findings as findings* — it does **not**
adopt any option below. To adopt one: read `references/id_reservations.yaml` `next_free`, allocate a
lane-tagged `ED-SC-NNNN` (or `ED-IN-NNNN` where marked cross-cutting), bump, and co-commit per the
file's protocol — never max+1. The `ED-SC-A`…`ED-SC-K` letters below are placeholders, not IDs.

Severity vocabulary follows PR #77 (P1 blocks a viability path; P2 significant; P3 hygiene).

## The P0 decision docket (blocking — each needs a Jordan call, not just an edit)

| Placeholder | Candidate | Finding | Severity | The decision |
|---|---|---|---|---|
| ED-SC-A | Reconcile the Debate→Domain-Echo keying: §5.4 (track-band, loser-penalty) vs §6 (genre-keyed, no loser row) — pick one scheme or specify their composition, and update the non-chosen doc to reference it | N-4 | **P1** (blocks all echo wiring) | Band, genre, or composed (e.g. band gates magnitude, genre selects stat)? |
| ED-SC-B | Resolve the "Piety Track" name collision: one name for the 0–10 debate tracker across `scale_transitions_v30`/`npc_behavior_v30`/glossary vs `social_contest_v30`'s "Persuasion Track"; rename or alias the unrelated per-territory `params/bg/` "Piety Track (PT)" | N-4b | P2 | Which name wins, and which doc is the tracker's canonical home (glossary currently points at `conviction_track_v1.md`)? |
| ED-SC-C | Choose the kernel's canonical Argue-pool formula: canon-verbatim `(Primary×2)+History−Wounds+fatigue, floor 1` vs the kernel's `[SEED]` `max(5, faculty*2+3)` — and retire the loser | N-2 | **P1** (gates calibration, re-verdict, Godot export) | Keep canon formula (restores the low-pool regime) or ratify the floor-5 redesign? |
| ED-SC-D | Cap the Recall/Corroborate/Prep/Findings bonus stack in prose *before* Stage 4 wires the channels (the +8D doc-math hazard; genre/audience is already capped +2D) | KU-1 (L-A) | P2 | Global cap value and whether Findings share it. |

## Wiring candidates (the consequence spine — P1 of the D6 sequence)

| Placeholder | Candidate | Finding | Severity |
|---|---|---|---|
| ED-SC-E | Route `scene_dispatch` contest resolution to the promoted kernel API (`build_contest`/`resolve_contest`), retiring the legacy-stub path; author the party-derivation bridge (canon-backed derivation of contest parties from aggregate faction state, preserving the no-fabrication discipline); extend the campaign regression to assert at least one resolved contest | N-1 | **P1** |
| ED-SC-F | Wire Bout outcome → `sim/cross_scale/domain_echo.py` (replace `zoom_out({}, world)` with the real outcome mapping, per the ED-SC-A decision); call `parliamentary_vote` from the campaign loop | N-5 | **P1** (blocked by ED-SC-A) |
| ED-SC-G | Refresh `module_contracts.yaml` social_contest entry: resolver `d_sigma`-family, actual kernel surface, add `typed_params`/`godot_home` fields (even if null-with-reason) | N-3 | P2 |

## Stage-4 entry criteria candidates (fold into the ratified Stage 4 gate, not new stages)

| Placeholder | Candidate | Finding | Severity |
|---|---|---|---|
| ED-SC-H | Wire the Face/Rattled strain channel (the CR3 triangle's third leg) and the §9.3–9.4b thread junctures (P-14) as Stage-4 entry criteria | KU-3, KT-5 | P2 |
| ED-SC-I | Add a focalization/chronicler parameter to `narrative.py`'s `Chronicle` before any player-facing use (P-03), and commission its first consumer (arc-generator or convergence-detection feed) | N-8 | P3 (cheap now, expensive later) |

## Hygiene / index candidates (cross-cutting — `ED-IN` lane)

| Placeholder | Candidate | Finding | Severity |
|---|---|---|---|
| ED-IN-J | Refresh the throughline registry's social-contest citations (T-14/T-23 retired names; T-16/T-17 Solidarity boundary; T-24's relationship to COLLISION E); supersede or banner `valoria_ui_ux_v4_1.md` Part 6 (pre-CR3 contest) pointing at the walkthrough | N-9, N-6 | P2 |
| ED-IN-K | Re-run the rolling-engine resolution diagnostic against the σ-substrate kernel once ED-SC-C lands (the 2026-05-28 NERS-COMPLIANT verdict is stale-based); tag `RES_FLOOR`/`REBUT_CAP` as `[SEED]`; reconcile `params/contest.md:98`'s "Direct/Indirect" residue | N-10 + observations | P3 |

## Explicitly NOT candidates (tracked elsewhere — do not double-file)

- Stage 4 four-games build (KT-1): already the ratified next stage (workplan #39 / LA-19).
- Terminal Doubt (KT-2 / ED-1060): open with Jordan already.
- Coalition dominance (KT-3 / ED-297): ratified-as-intended.
- Audience-resistance plumbing (KT-9): reserved to the contest_rebuild ED range in code comments.
- HANDOFF_SC / CURRENT.md stage-currency refresh: routine currency maintenance, no ED needed.
