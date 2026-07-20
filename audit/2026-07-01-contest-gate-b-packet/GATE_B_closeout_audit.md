GATE B CLOSEOUT: READY TO COMMIT. Independently re-verified everything; zero major/blocker findings, tests green.

TESTS (re-run by me): python -m pytest sim tests/valoria -q -> 1041 passed; python -m sim.personal.contest._kernel_tests -> 319 passed, 0 failed.

FOUR RATIFIED DECISIONS -- all verified in REAL CODE, not just ED text:
1. Panel aggregation = WEIGHTED-BY-STANDING (ED-1057): dictionaries.PANEL_AGGREGATION='weighted_by_standing'; resolver.VoteAtClose has the weighted branch (resolver.py:126-140) reading per-juror weight from the EXISTING Adjudicator.discipline field (max(0.0,float(getattr(m,'discipline',0.0)))), NOT a new field and NOT the contestant-side Standing class (naming-collision hazard explicitly documented+avoided in PANEL_CLOSURE). Seeded mixed-weight bench (0.9/0.1x4, close room, seed=42) diverges 296 A / 204 B -- goes both ways, does not mirror the highest-weight juror. VERIFIED.
2. Panel reachability = REBIND Guild Arbitration -> Panel (ED-1059): modes.PROCEEDINGS['guild_arbitration']['adjudicator']=='panel'; roster count still exactly 8; no appeal/escalation flag anywhere in the diff (contract.py appeal_axis is the pre-existing D0-1 axis, NOT in this diff); Guild Arbitration flavor updated to 'a bench of guild masters ... the masters weigh the stronger case'. VERIFIED.
3. Terminal Doubt (ED-1060): banded (PersuasionTrack) + tally (TallyAtClose) split present in DOUBT_MARKER_FIELD/DOUBT_MARKER; _doubt_marker_branches_specified() returns [] (both branches defined, guarded by kernel test); design-table commitment only, resolver does not yet consume orientation (Stage-3 CR5), so no resolution-number change was needed and none regressed. VERIFIED.
4. Guilds boost = context-derived-from-venue (ED-1061): literal 'GM picks' is GONE from the RULE prose in both params/contest.md and social_contest_v30.md (the only remaining hits are the <!-- --> correction breadcrumbs documenting the fix); dictionaries.guilds_boost_for(adjudicator) derives from adjudicator.character() dominant ethos/pathos/logos via _GUILDS_APPEAL_TO_BOOST, reusing the existing primitives.Appeal machinery (no new venue field); deterministic tie-break by Aristotelian order logos>pathos>ethos (verified: expert_judge/panel->Memory, crowd->Projection, no_adjudicator->Revealing, all deterministic). VERIFIED.

OTHER CHECKS:
- canonical_sources.yaml pins: recomputed git hash-object matches ALL THREE current files exactly (params/contest.md=79984a9a..., social_contest_v30.md=814b0e14..., social_contest_v30_index.md=5b6977a1...). Pins are current, not stale.
- id_reservations.yaml contest_rebuild.ED next_free=1062 -- correct (ED-1061 last filed), no gap, no collision.
- No git add/commit/push run: git diff --cached is empty; working tree shows M/?? only. Still an uncommitted proposal, as required.

NON-BLOCKING NITS (documentation-only, no behavior impact; I did NOT edit them, to keep the packet clean per the closeout posture -- flagging for the orchestrating session):
(a) wrapper.py:168 comment says the aggregation rule is 'simple majority ... a flagged OPEN DECISION FOR JORDAN' -- stale/wrong: the code path calls panel_win_condition() which defaults to PANEL_AGGREGATION='weighted_by_standing' (ratified). Suggested: 'weighted-by-standing, RATIFIED (ED-1057)'.
(b) resolver.py:106 and :127 attribute the weighted_by_standing aggregation to 'ED-1061' -- mis-citation; the Panel aggregation ratification is ED-1057 (ED-1061 is the Guilds boost). Line 115 already cites ED-1057 correctly, so the two ED-1061 references are the ones to correct.
(c) canonical_sources.yaml comment breadcrumbs (~lines 167-184) cite abbreviated hashes (3bb66e5f etc.) that don't match the final pins -- cosmetic only; the load-bearing canonical_sha__* fields are correct.
None of (a)/(b)/(c) affect behavior or tests; all three are safe one-line comment fixes.

Per the hard rule (ready_to_commit=true only if zero major/blocker AND tests green): both conditions met.
