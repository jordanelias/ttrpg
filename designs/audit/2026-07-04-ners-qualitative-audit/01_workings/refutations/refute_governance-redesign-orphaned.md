# Refutation notes — governance-redesign-orphaned

## Claim under test
governance_play_redesign_v1.md is a well-aimed fix but is absent from CURRENT.md's
settlement/territory head list and from HANDOFF_SE.md pending ("none"), "risking permanent
orphan status alongside its unbuilt G1 prerequisite."

## What is literally true
- CURRENT.md §settlement/territory row (line 28) lists only settlement_layer_v30 (+ adjacency,
  temperaments, geography). governance_play_redesign_v1.md is NOT listed. TRUE.
- HANDOFF_SE.md Pending / Next actions = "(none)". TRUE.
- governance_play_redesign_v1.md §Status = "PROPOSAL — drafted 2026-06-22". §5.2 gates the whole
  redesign on audit gap G1 (settlement registry). TRUE as written.

## What REFUTES the finding (working tree)
1. **G1 is BUILT, not "unbuilt."** The load-bearing severity premise is false:
   - `sim/territory/registry.py` (module docstring: "Settlement registry (closes audit gap G1)")
     and `sim/territory/ledger.py` both exist.
   - `tests/sim/territory_registry/test_registry_ledger.py` exists; goldenfurt README §79 records
     6 passing tests (AP economy, ledger-survives-succession, single Reputation, 3-settlement
     aggregation, registry-backed derived values, legacy 1:1 fallback).
   The finding's central risk driver ("unbuilt G1 prerequisite") contradicts disk.

2. **Far from orphaned — it is one of the most actively-developed territory-lane artifacts.**
   `designs/territory/goldenfurt_slice/` is a 5-file interlocking worked example OF this redesign:
   README, npc_cast, event_deck (28 cards), sim_build_spec, verification_findings. It ran an
   adversarial verification pass (32 findings, 15 high; bugs fixed, v1.1 revisions), and carries a
   staged S0–S6 build roadmap with S0–S1 landed. An "orphan" has no downstream build; this has a
   full one.

3. **Absence from CURRENT.md is CORRECT currency discipline, not orphaning.** CURRENT.md (lines
   10-13) is "the single human-readable index of what is LIVE/canonical … superseded/exploration
   lives elsewhere." A doc whose own Status is PROPOSAL is correctly excluded until ratified. Under
   the ED-1094 merge-ratifies convention, it would flip to canonical (and gain a CURRENT.md row)
   when its PR merges. It has not merged/ratified, so its exclusion is the system working as
   designed — a DELIBERATE, safeguarded gate, not accidental neglect.

## Intent evidence
- Ledger grep (canon/editorial_ledger.jsonl): no ED opened against governance_play_redesign; the
  governance hits (ED-682, ED-723) are unrelated. Not an ED-tracked defect either way.
- The redesign is self-gating (§5.2) and its slice README states plainly it is "content + spec
  only" until the sim stages land — this is a known, sequenced pre-ratification proposal, not a
  dropped one.
- A SIBLING lens in this very audit (lens_cohesion_interdependency.md line 35) already records
  "governance_play_redesign -> settlement (orphaned proposal)" and
  lens_playability_legibility.md line 74 notes it "unratified" — so even the observation is not
  novel to the audit; and neither treats it as a P2 risk requiring a tracking artifact.

## Residual true kernel (much smaller than claimed)
HANDOFF_SE.md logging "(none)" pending while S2–S6 slice work is genuinely in flight is a minor
continuity-hygiene gap. But CLAUDE.md §2 defines continuity as "git history + HANDOFF", and the
slice README + sim_build_spec §7 roadmap already serve as the working continuity surface. This is
P3 debt at most, not P2, and does not threaten orphaning.

## Verdict
REFUTED. The two load-bearing premises — "unbuilt G1" and "permanent orphan status" — are both
false against the working tree: G1 is built with passing tests, and an active multi-artifact
vertical slice with an S0–S6 roadmap is driving the redesign forward. Absence from CURRENT.md is
correct proposal-currency discipline (DELIBERATE, safeguarded). North-Star impact of the residual
hygiene kernel is negligible; the choice-widening design work is already progressing.
