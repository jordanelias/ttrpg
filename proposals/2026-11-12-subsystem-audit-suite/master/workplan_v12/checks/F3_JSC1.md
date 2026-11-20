# F3 J-SC-1 — Jordan's R11 (the dice of a speech) folded into the redesign and Batch B24p

## Status: PROPOSED (a log; reference under CLAUDE.md §0.05, nothing reads it at runtime; written 2026-11-14, branch `exec/v12-b00-b03`; deleted with the plan's other work files when v12 is adopted)

Ruling (Jordan, 2026-11-14): *"argument dice is Presence and/or Reason depending upon content of argument and venue"*. Answers J-SC-1. Paths: `RD` = `proposals/2026-11-12-subsystem-audit-suite/proposals/2026-11-14-social-contest-redesign`; `wp` = `proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12/workplan_v12_`.

**Rule chosen.** `w_reason = clamp(content class w_reason + type reason_bias, 0, 1)`, `w_presence = 1 - w_reason`; both cells held in tenths; the blend `weighted_tenth((reason, presence), (k, 10 - k))`, nearest tenth, a half up. Ladder step 4: the redesign adds a type-row cell to a move-row cell (`difficulty = type.difficulty + move.difficulty`, RD §B.7). The product-renormalised reading was refused at step 5 (undefined at `(1, 0)` against `(0, 1)`; harder to read off a row). Control: every `w_reason` 1.0, every bias 0 (the blend is Reason, so B24p.07's control equality and reading R1 hold unchanged).

| file | handle | change |
|---|---|---|
| `RD.md` | head `Depends on`; brief (3) | R1 to R11; the dice a blend |
| `RD.md` | §A.1 | `ground` names a content class; NEW row *content class* |
| `RD.md` | §A.3 | `Move.reason_weight`, `ProceedingType.reason_bias`, `ProceedingInput.ground_reason` |
| `RD.md` | §A.4 step 4 | the pool from the blend |
| `RD.md` | §B scratch readings | ⚠ taken with Reason alone as the dice; not a bound |
| `RD.md` | §B.2 | mechanism (a); NEW sub-block (a), the blend: the two weight tables, the rule, its ladder reasoning, `weighted_tenth`, control, shipped basis, the two uses of Presence `[ASSUMPTION]`, ED-IN-0350 superseded; sources; falsifier renamed with judicial and crowd arms; NEW slope falsifier `test_the_dice_lean_to_reason_or_presence_by_content_and_venue` |
| `RD.md` | §B.4 | mechanism note (separate from the blend); `enters`; `heard` sentence; falsifier renamed, arm (o) on the dice; control |
| `RD.md` | §B.7, §B.8 | `case` from the blend; control with `k` = 10; the table's Reason and Presence rows; the one shared operand |
| `RD_part2.md` | §C.1, §C.2, §C.3 notes, §C.4 | sixth key `reason_bias`; loader checks (venue bias on every row, tenths; every speech kind one content class); per-row values pointed to §B.2 a; `divert`'s `content: procedural` |
| `RD_part3.md` §E, `RD_part4.md` head | note | the plan's copy governs for R11; this copy not kept in step `[ASSUMPTION]` |
| `RD_part5.md` | §F.5 ids; §F.7 | H 50; J-SC-1 ANSWERED |
| `wp part22_b24p.md` | head (holds, Paths); BATCH GATE; IDS; SERIAL EDGES; FILE CENSUS; table rows .01, .03, .07 | R11 named; per-type Reason/Presence bounds `[ASSUMPTION]`; H 50 (50+4, range unchanged); `sigma_leverage.py` edge and census |
| `wp part22_b24p.md` | B24p.01 | `content_classes` roster (control 1.0); `content:` on grounds and `divert`; loader closure; NEW test `test_every_speech_kind_has_exactly_one_content_class`; four pass; glossary *content class* |
| `wp part22_b24p.md` | B24p.02 | the three record fields |
| `wp part22_b24p.md` | B24p.03 | six keys; `reason_bias` required, tenths, control 0; abridged keeps it; NEW test `test_every_proceeding_type_has_a_venue_bias_in_tenths`; glossary *venue bias* |
| `wp part22_b24p.md` | B24p.04 | 49th setting `speech_blend` (pointer row), slots 1–49, `>= 49` |
| `wp part22_b24p.md` | B24p.07 | SOURCE overrides ED-IN-0350's letter; NEW step 3 `_blend` and `sigma_leverage.weighted_tenth`; steps renumbered 4–6; tests: `test_weighted_tenth_is_the_governing_rule_weighted`, the two role tests in two arms, the slope test; falsifier, control, GATE |
| `wp part22_b24p_cont.md` | B24p.13 | builder fills `reason_weight`, `reason_bias`, `ground_reason`; NEW test `test_the_blend_weights_come_from_the_two_rows`; six pass |
| `wp part22_b24p_cont.md` | B24p.15 | H slot 49 → 50 |
| `wp part22_b24p_cont.md` | B24p.16 | ED-SC row records R11 and the ED-IN-0350 amendment |
| `wp part22_b24p_cont.md` | B24p.18 | operands at `k` = 4 (exact shares), third pass at `k` = 10 and 0; planted fault re-worded; control |
| `wp part22_b24p_cont.md` | B24p.23 | step 2 sets both blend tables; WHERE `rosters.yaml`; GATE bounds by type; two STOP falsifiers |
| `wp part22_b24p_cont.md` | reading R1 | control expectation explained (blend is Reason) |
| `V12_FOR_JORDAN.md` | J-SC-1 | ANSWERED, Jordan's words, what the plan does |
| `RD jordan-rulings` | R11 | verbatim and `[reading]` |
| `unified/DECISIONS_ANSWERED.md` | A-127 | the ruling; amends ED-IN-0350 |

No item added or split: B24p stays 24 positions, EST 14.1 h, part 2 §1 untouched.
