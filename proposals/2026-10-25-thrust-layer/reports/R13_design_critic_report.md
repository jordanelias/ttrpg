# R13 — Design critic's report (read-only antagonist; findings F1–F16)

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). This is the agent's hand-back message, reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Under CLAUDE.md §0 an adversarial pass is a stage, not a deliverable; this file records a terminal verdict about artifacts that already exist, as the §0 exception permits, and asks nothing of a future session.

**Role:** antagonist (critic), read-only (`valoria-critic`; tools Read, Grep, Glob), opus. **Saw:** only the v1 design file and the working tree. **Disposition of every finding:** the adversarial-pass record at the end of `../00_THRUST_LAYER_DESIGN.md` (citations marked [c] there were opened by the critic and not re-opened by the orchestrator).

---

1. VERDICT
The design does not survive as written. Its worst problem is that the arc predicate in §1.2, which every B0/B6 falsifier depends on, is met vacuously by WITNESS bookkeeping. Every claim deposit is a gate-minted Receipt whose subject is the claim id, so any witnessed act already counts as a "world effect". Close behind are two more blockers: §4.3 contravenes a RULED succession carrier without naming it, and the §5.2 "standing gate" protects only three principals.

2. FINDINGS (worst first)

| ID | Sev | § | What is wrong | Evidence (opened) | Required fix |
|---|---|---|---|---|---|
| F1 | BLOCKER | §1.2, B0.1, B6.n | Clause (3) is vacuous. Every witnessed act yields `claim.deposited` Receipts whose subject is the claim id, which is "neither p nor a Tenure owned by p", and the causes link back to the act. Clause (2) is met by any self-write (`move` writes `Person.travel_leg`). So ARC = "moved toward a referent and was seen". The design's line "a claim deposit is not a Receipt" is false. The shuffled-causes null cannot catch this, because the links are real. | `loop/witness.py:654-657` `w.write("claim_ledger"…emits="claim.deposited", subject=c.id, causes=[e.id])`; `state/world.py:1144-1160` (the receipt subject is `subject=`) | Restrict (2)/(3) to a named set of `(kind, field)` pairs, excluding `claim_ledger` and interior fields. Add a planted case: a witnessed `move` must read FALSE. |
| F2 | BLOCKER | §4.3, S8 | The design chooses exactly the carrier Jordan rejected, and does not name the contravention in §9. The `succeed` edge is Person→Person, owned by the holder, and the death cascade closes it, so it is never live at the vacancy. This also duplicates IN-61. | `workplans/valoria_master_workplan_v9_part5.md:131` ("Carrier: RULED — Jordan ratified the title"; edge "ends at its owner's death"; `may_fill` must refuse `inheritance`, "else… the Widow Regent… confer the vacant throne"); `architecture/meta/04_CODE_ARCHITECTURE.md:195`; `state/world.py:646` | Delete §4.3 and B4.3; point to IN-61. |
| F3 | BLOCKER (user intent) | §5.2 | G1 guards seat only three principals. Limbs 2 and 3 admit any seat-holder whose purview reaches the rung, and anyone sworn to such a seat. The −1 `seat_holders` goals target unguarded Church seats (Cardinal of Justice, Senior Inquisitor, Confessor, Restoration leader). R3 then promotes those exact need questions. | `cohorts.yaml:127-130` (only `off_king`, `off_duchess_hafenmark`, `off_duke_varfell`); `world_q.py:1305-1315`; `goals.yaml:161-163` ("DECLARED RISK… `fight` forms on them") | State coverage honestly (3 of 31 seats). Author guard content for the seats meant by "authority". Measure harm aimed at seat-holders, with a control arm. |
| F4 | MAJOR | §3.3 R3 | R3 reintroduces the regression it claims to fix. Goal commits are minted at `since` 0, so every committed person's stage comes due on the same tick. A due stage stays due until the person-side predicate turns true. With `commit`, `determine` and `confer` refused on every attempt, stages stay unmet, so R3 converges on the unconditional tier-0 arm that starved news. The narration proposal names this pulse hazard. The falsifier's run length is unstated, and arms defaults to 2 seasons. | `harness/populated.py:709` `Tenure(…"commit", 0)`; `world_q.py:2608-2612`; `proposals/2026-10-13-narration-mechanisms.md:315`, `:47`; `harness/arms.py:236` | Make each run last longer than the largest Σdeadline. Make due-ness expire. Date stages from a `since` an act declared, not from world-gen. |
| F5 | MAJOR | §3.3, B3.2, B4.1, B6.n | The named instrument cannot produce the named measurements. arms is wired to `field_casualty_model` and returns act-subject tallies only. The 51/803 baseline comes from an uncommitted one-seed scratch run. The "`deadline: null` reproduces today's hash" control is wrong: R1/R2 move the hash whenever any ladder is authored. "Need share rises" cannot fail once R3 promotes. | `arms.py:135-170`; `narration-mechanisms.md:55` | Commit a real instrument. Use ladders-authored with R3 off vs on as the control. |
| F6 | MAJOR | §2.2, §4.4 | `of: referent` cannot be spelled: operands are a closed set and the builder exits on any other. The builder raises `SystemExit`, not `Unspecified`/`Forbidden`, so the B2.1 tests assert the wrong exception. §4.4's "advances only through a determination under arrangement X" has no stem. | `rosters.yaml:1847-1854`; `data/requires.py:973-978`, `:794-797` | Use `of: subject`, with R1 binding subject := each referent, and route it as a Layer-1 question. Drop "only" from §4.4. |
| F7 | MAJOR | §3.1 R2 | R2's own example fails. `confer` forms only on Office-classed referents, so a seat added to the plain referents never forms `confer`. It does form every unclassed verb on an office id, adding to S1's kind-mismatch refusals. | `verb_table.yaml:266-267` | Pass stage referents through `_stamped`'s classes (`world_q.py:2889-2897`). |
| F8 | MAJOR | §1.2, §2.2, §6C | The static check contradicts the design itself: §6 C's short stage (`interview`/`surveil`/`examine`, all writing nothing) would be refused by the design's own loader rule. Nothing in the game reads `advanced_by` (§3.2 step 3), so the refusal guards a process-only field, which CLAUDE.md §0.1 pt 5 forbids. | `verb_table.yaml:1446,1467,1508` (`writes: []`) | Delete `advanced_by` and the static check. |
| F9 | MAJOR | §1.2 | "A pure read over a finished world" is false. The question an act answered lives on the driver's `Scene`, not on the World, and need-formed acts cite no occasion. | `state/carriers.py:574-584`; `harness/soak.py:139-144`, `:262`; `world_q.py:2947-2948` | Read clause (1) from a live driver (soak's `_occasion_row`). |
| F10 | MAJOR | §4.2 | `held_document_declines` maps a verb to a document kind and declines that verb outright while the person holds such a document about himself. It cannot key on a covenant's named referent or on a `commit`. Composing on it either declines `fight` against everyone, or needs a new subject-keyed shape (shape divergence). | `rosters.yaml:2020-2033`; `decision/options.py:857-874` | Name it as a new reader and a Layer-1 question. |
| F11 | MAJOR | §9 | Contraventions are understated. (a) A typed ladder running to `closing` with successors is a type; ED-IN-0225's absence was "no type". The narration proposal's "storyline object that steers the sim — kept out" and #457 `:190` are not named. Jordan licensed hooks "so long as we don't script entire arcs". (b) The R3 deadline is a timer no act declared, unlike `oblige`'s `matures_at`, whose term an act declares (`term.declared_by`). (c) `Slain` contravenes Jordan's 2026-09-04 ruling ("accept the result"; the `Felled` edge is never swept). | archive `:3219-3221`; `narration-mechanisms.md:181`, `:183`; `research/by_lane/WR_world.md:271`; `proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md:618`; `04_CODE_ARCHITECTURE.md:366`; `rosters.yaml:837-840` | Name each contravention as such. |
| F12 | MAJOR | §4, §7, §8 | (a) `determine` decides only in hand-built worlds (H-163), and `commit` was refused 74 of 74, which blocks successor thrusts. (b) S1 waits on an unruled Jordan decision and sits in no workplan. (c) §4.1 keys on "his seat's goals", but only the two Altonian seats carry seat goals, so it fires for nobody. (d) B1.2 duplicates IN-12 step 5. | `workplans/valoria_master_workplan_v9_part2.md:31`; `narration-mechanisms.md:31`, `:47`; `goals.yaml:449-472`; `workplans/valoria_master_workplan_v9.md:255` | Cite H-163, IN-12 and the open S1 decision. Key §4.1 on goals of the seat's body and faction. |
| F13 | MAJOR | §10 D2/D3 | D2 does not survive CLAUDE.md §0's five steps: canon names the Church as the suppressor of Thread awareness. D3 ignores the affiliation spine (`einhir_restoration`, A-35). | `canon/03_canonical_timeline.md:98`; `rosters.yaml:2716` | Answer D2 from canon; reconsider D3. |
| F14 | MINOR | §9, §11 | Overreach on toy results. "~2.7× chain depth" and "~9.5 acts by ~5 actors" appear in no cited output. Falsified pre-registered predictions are omitted: H1, H4; K1, K3 (the bound peace), K5; R1. `+0.244` is quoted without its sibling arm's `+0.016 [-0.019,+0.051]`. | `exp_ladder_out.txt:39,42`; `exp_con_out.txt:6,15,17,19`; `out_v2.txt:117`; `posthoc_out.txt:24` | Report the falsified predictions next to the confirmed ones. |
| F15 | MINOR | §3.1 | Ladders attach only to `goals.yaml` ids, so R3 lifts faction goals above personal wants. That inverts A-33 (a misaligned head answers his own ambition first). | `valoria_master_workplan_v9_part5.md:178` | Name the inversion, or extend it to wants. |
| F16 | MINOR | various | Line slip: the "14 of 29" header is at `offices.yaml:64`, not `:66`. B4.1's "changes=[] always" asserts a literal. "≥1 seed where he declines" cannot fail, since 7 of 7 determines were refused. | — | Assert that no Receipt is minted during the step. |

Observations (outside my lane; reported, not ruled):
- The design never says how a player character enters this layer.
- A detained holder whose stage is due sorts in tier 0 and forms acts that the custody decline refuses (`verb_table.yaml:913`), which wastes scenes.

Cheapest observation that sinks the design: read `witness.py:654-657` together with `world.py:1144-1160`. It needs no run, and it sinks §1.2. The design's own candidate (count executed `determine`/`confer` over n seeds) is not the cheapest. It has also already been observed, and it came back negative (`narration-mechanisms.md:47`).

3. CITATION TALLY
About 125 opened; 114 held; 9 failed; 2 unverifiable.

Failed:
- §1.2: "a claim deposit is not a Receipt" (F1).
- §1.2: "pure read over a finished world" (F9).
- §2.2: `of: referent` via `build_typed_requires` (F6).
- §3.3: arms as the instrument (F5).
- R2's confer example (F7).
- §4.2: `held_document_declines` as a composition site (F10).
- §4.3: a succeed tenure held "to the vacant seat" (`04:195`, F2).
- Toy figures 2.7× and 9.5 (F14; counted as two).

Unverifiable: `narrative_engine_design_v2_churn.md:448` (the design gives no directory, and the markdown-sweep hook blocks a glob for it); `person_q.py:350-361`.

4. WHAT HOLDS
- Thirteen verbs write nothing, out of 56 rows (`verb_table.yaml` 238, 418, 447, 772, 1043, 1189, 1296, 1446, 1467, 1483, 1508, 1531, 1546). I counted every `writes:` line.
- Seats: 31 in `seats:`. Revocation basis 16 null / 13 same-faction / 2 in-holdings. Conferral 6 null / 8 elected / 17 appointed. The two foreign seats are excluded (`offices.yaml:181-627`, `:595-596`).
- I suspected that no realm seat holds `dispatch`, which would make `arrest` and `march` unreachable. That suspicion is wrong: 22 of 29 loop-built seats keep it (`data/rosters.py:709-717`).
- The L5 precedent and the shape of `_standing_crossings` (`matter.py:79`, `:187-240`). The §4.1 crossing itself writes nothing.
- The ED-IN-0225 text (archive `:3209-3237`), and the four `.py` files that cite it (chronicle, populated, soak, storybar).
- The death-route table (`effects_combat.py:134-137`, `:317-326`; `fixtures.py:594`, `:606-608`, `:654`) and the ENDINGS counts (`ENDINGS_CLASSIFIED.yaml:23`).

5. UNVERIFIED BY ME, AND WHY
- I executed nothing (read-only): no seeds run, `regimes10.py` not run.
- Whether the WoundTracker can tell "down" from "dead".
- The Receipt subject on tenure writes (`World.write` was read only around `:1125-1164`).
- `choose.py:388`.
- Whether `covenant` executes in the realm.

Absolute path of the design under attack: thrust_layer_design_v1.md (not committed)

---

## Brief given to the agent (verbatim)

The instruction the agent received, so a reader can judge what it was and was not told.

~~~text
You are the ANTAGONIST (read-only critic) in an agonist→antagonist relay for the Valoria repo at /home/user/ttrpg. Read /home/user/ttrpg/CLAUDE.md first; its rules are your standard. You did not see how the design below was produced and you must not defer to it. Your job is to BREAK it against the working tree.

DESIGN UNDER ATTACK: thrust_layer_design_v1.md (not committed) (read it in full). It proposes a "thrust layer" for engine/season/ (ambitions with a ladder of short/medium goals across ten authored axes; closure engines; rare death; a standing gate; significant consequences of a killing). The user's intent it must serve: an arc must affect the character AND their world; ambitions are an overall thrust with short/medium goals beneath; NPC death extremely rare or its consequences significant; it must be hard to fight anyone with authority/standing; there is no GM, the engine resolves everything. The user permits contravening existing rulings if each is NAMED. Toy-world experiment outputs the design cites are in proposals/2026-10-25-thrust-layer/toy/ (out_v2.txt, posthoc_out.txt, exp_ladder_out.txt, exp_setpiece_out.txt, exp_contest_out.txt, exp_con_out.txt, lb_more_out.txt, regimes10.py); they model the LOGIC of regimes in a toy world and are not evidence about Valoria.

ATTACK, in this order, and OPEN EVERY LINE YOU CITE (a citation you have not opened is not a citation; CLAUDE.md §0.1 pt 3):
 A. PROVENANCE. Open every path:line the design cites for a claim about the tree. Report each that does not say what the design says, each number it states that you can recompute (e.g., counts of verbs that write nothing, seats by revocation basis, goal rows), and each citation missing a line where one is needed. Give a tally: citations opened / held / failed.
 B. LAYER 1 AND §0.05/§8. Check placement and conformance against architecture/meta/04_CODE_ARCHITECTURE.md (read the rows relevant to each proposed module, loader, roster and query). Find any fact whose head would be prose, any second parser or second owner, any engine→subsystem import, any proposed guard that fails §0.1 pt 5's predicate (a guard whose subject is another guard, or an artifact load-bearing only on the process).
 C. DRIFT AND INJECTION. Find any mechanism that lets something other than a person's act write an outcome, special-cases an entity or outcome, or introduces an arc/story/thread carrier by another name. Check the design's R3 promotion rule and its closure engines against engine/season/loop/matter.py (_standing_crossings and the 'a crossing MAY NEVER PRODUCE AN OUTCOME' precedent) and against ED-IN-0225 and proposals/2026-10-13-narration-mechanisms.md §3.4-3.5.
 D. THE PREDICATE AND THE TESTS. Can the self-effect + world-effect arc predicate be satisfied vacuously (e.g., by bookkeeping writes)? For EVERY falsifier and control the design names, say whether it could actually observe the failure it claims to exclude (§0.1 pt 2, 3: an assertion that cannot fail is absent; a number without a control is not a measurement; a loop that asserts conditionally must assert that it asserted). Name the cheapest observation that would sink the design and say whether the design's own candidate is truly the cheapest.
 E. DEPENDENCIES AND FEASIBILITY. Is the build order sound? Find any batch that silently needs something not built or not scheduled in workplans/valoria_master_workplan_v9*.md; any step whose cell/stem/form the typed-requires grammar cannot spell; any claim about what currently executes that is wrong (check that the verbs it relies on are resolvable, not merely listed). The design reports a measured regression when the standing 'need' question was ranked first (queries/world_q.py attention_key docstring: events fell, news.told fell): check that its fix R3 does not reintroduce it.
 F. OVERREACH. List every place the design lets a toy-world finding stand in for a statement about Valoria, and every place it states a figure from proposals/2026-10-13-narration-mechanisms.md or the toy outputs without its grade.
 G. WHAT N-1 WOULD MISS. Name the one or two lenses the producer was likeliest to be blind to and attack through them (for example: the interaction of the standing gate with the existing access gate (admits_audience, guard_weight); who defends the caste order and hides the threadwork truth; cohort/settlement identity; what happens to a thrust when its holder is imprisoned, exiled or dies; the NPC lane's 46 cases that have no authored trajectory; how a player character enters this layer).

OUTPUT (fixed format, <= 1,800 words, no preamble):
 1. VERDICT in one sentence (does the design survive? what is the single worst problem?).
 2. FINDINGS table ranked worst first: ID | severity (BLOCKER/MAJOR/MINOR) | design section | what is wrong | evidence you OPENED (path:line, short quote) | required fix.
 3. CITATION TALLY (opened/held/failed) and the failed ones listed.
 4. WHAT HOLDS (<= 6 bullets): the design's claims you tried to break and could not, with what you tried.
 5. UNVERIFIED by you, and why.
You cannot write files; return the report as text. Do not propose a different design; fix the one in front of you. Canadian spelling.
~~~
