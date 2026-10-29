# Reports — the chat and subagent reports of the thrust-layer session

## Status: REFERENCE — PROPOSED, HELD BACK IN FULL

Merging the PR that carries these files ratifies nothing in them (ED-1094's default is not applied). Reference under
CLAUDE.md §0.05: none of it is a mechanism, binds code, or creates a plan position or an obligation on a future session.
Under CLAUDE.md §0 an adversarial pass is a stage, not a deliverable; the four subagent reports (R12–R15) are kept as the
**terminal verdicts about artifacts that already exist** (the design and the register), which §0's exception allows to
live beside their subject, and for no other reason. Delete them if the exception becomes the general case.

This directory exists so that the session's reasoning has a surface: what was asked, what was answered, and what each
independent critic found. The documents the reports produced are one directory up:

- `../00_THRUST_LAYER_DESIGN.md` — the design (v2, after critic F1–F16)
- `../01_MISSING_IN_CODE.md` — the gap register (v2, after critic A1–A14)
- `../02_MAJOR_TAKEAWAYS.md` — the eight takeaways, expanded and corrected
- `../toy/` and `../probes/` — the code and saved outputs the reports cite

## Index

| File | What it is |
|---|---|
| [R01](R01_partial_top_down.md) | Is pure bottom-up emergence a problem; can partial top-down guides help (with oatmeal research) |
| [R02](R02_arcs_deconstruction_and_logic_tests.md) | Logic tests of top-down, bottom-up and hybrid emergence; deconstruction of the studied arcs |
| [R03](R03_sigma_leverage_correlate.md) | Is there a sigma-leverage correlate for the likelihood of subsequent events (preliminary findings) |
| [R04](R04_ladder_tribunal_best.md) | Is ladder plus threshold-raised tribunal the best? |
| [R05](R05_scripted_director_set_pieces.md) | A scripted director that injects set pieces rather than outcomes |
| [R06](R06_npc_deaths_clarification.md) | Does "94% end with both principals alive" mean NPC deaths |
| [R07](R07_arcs_without_deaths.md) | Arcs without NPC death; making death rare, fighting authority hard, killing consequential |
| [R08](R08_ten_axes.md) | The ten goal axes and the arc criterion |
| [R09](R09_design_verdict.md) | Design of the thrust layer by agonist-antagonist methodology (verdict after the relay) |
| [R10](R10_major_takeaways_as_first_delivered.md) | Major takeaways, as first delivered |
| [R11](R11_register_verdict.md) | Missing in code: the register's verdict after the relay |
| [R12](R12_design_producer_receipt.md) | Design producer's hand-back (the thrust-layer design, v1) |
| [R13](R13_design_critic_report.md) | Design critic's report (read-only antagonist; findings F1–F16) |
| [R14](R14_register_producer_receipt.md) | Register producer's hand-back (the missing-in-code register, v1) |
| [R15](R15_register_critic_report.md) | Register critic's report (read-only antagonist; findings A1–A14, O1) |

R01–R11 are the assistant's chat answers, in the order given, each under the user's own words. R12–R15 are the four
subagents' hand-back messages with the briefs they were given.

## How these were reproduced

- Chat reports (R01–R11) are verbatim from the session record. The user's mid-turn messages are marked "(sent mid-turn)".
- Subagent reports (R12–R15) are the text each agent sent through its hand-back call, verbatim, with its brief appended.
- **Path rewrites only.** The session's scratchpad paths are rewritten to the committed locations
  (`../toy/`, `../probes/`, `../00_THRUST_LAYER_DESIGN.md`). Documents that were not committed (the v1 drafts) are marked
  "(not committed)". Nothing else is edited.
- Where a report was later found wrong, a note under "Asked by the user" or in the takeaways §9 records it; the report
  itself is left as delivered.

## Known errors in the reports, in one place

See `../02_MAJOR_TAKEAWAYS.md` §9. The two that matter most: R09 and R10 say the candidate-typing question is "unruled and
sits in no workplan" (it is H-156, an open ruling), and several first-delivery refusal figures (929 of 1,318; 33%; 51 of
803; 28 of 46) are superseded by the register's probes.
