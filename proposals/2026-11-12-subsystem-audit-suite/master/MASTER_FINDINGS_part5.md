# The master findings — part 5: §10, the findings by subsystem (FI, FA, SE, WR, DICE, GO)

## Status: REFERENCE (part 5 of `master/MASTER_FINDINGS.md`; the row tables are generated from the closure tables `unified/U5_FINDINGS_CLOSURE_U5a.md`..`_U5d.md` by the lane's scratch extract, the syntheses written by lane MF; resolves nothing at runtime; dies with the suite)

Columns and order are the head part's §0. **evidence**: the closure row (`U5a:66` = `unified/U5_FINDINGS_CLOSURE_U5a.md` line 66), then the audit line that defines the finding where the extract found it (`audits/` implied), then the closure row's own evidence, cut to one line. **sev**: B blocks a requirement · D degrades narrative · C code matter · M design matter · H hygiene · — ungraded. **carrier**: the closure row's carrier cell, cut to one line (its short names are the closure table's, defined at the head of that table's section). **batch**: v12's handle; `→` before it on a SUPERSEDED row (the successor's batch); `— (stale)`, `— (disputed)`, `— (answered …)` where no fix is owed. Claims are the closure tables' one-liners, cut at about a hundred characters; outside code font the word *capability* is printed *skill* (A-98, as the suite's own vocabulary sweep did, `unified/work/A98_SWEEP.md`), and nothing else in a quoted cell is changed.


---

## FI — field investigation and knowledge

**What is wrong.** The information model is a sound basis (the witness barrier, the per-holder ledger, provenance, refraction, clause 4: two people in one realm hold different facts) and the fieldwork game on top of it is not yet a game, because almost nothing a person knows reaches another by a person's act (`audits/08_FI_audit.md` §0; F-FI-02): over three seeds, 0 to 7 of 10,000 to 12,000 held claims arrived by telling. A person's candidates move on a fact he has not witnessed (F-FI-01); investigation resolves and does not play (F-FI-03); a lie deceives only those it changes nothing for (F-FI-04); nothing said can be private and nothing hidden can be found (F-FI-06); the hand that did a killing cannot be passed on (F-FI-11). The pessimist (`16_PESSIMIST_FI.md` §0): the realm's busiest engine informs nobody; 73.7 % of executed acts are information verbs and 93.9 % of 74,510 Events are ledger bookkeeping; cutting every information verb makes the world *more* eventful. The lacuna lane (`19_LACUNA_*` §0): the carriers exist; the one missing act is a conclusion the investigator commits to, bound to its support, that the world answers later.

**What was decided.** A failed attempt on a guarded target is caught (A-96); news of an office travels realm-wide, news of a death by presence, trail and telling (A-32, A-33); a rumour may lose the doer but never replace him, and the engine authors no wrong conclusion (D-44, D-45); a refusal teaches its refuser privately (D-46); finding what is hidden needs its own design (A-109).

**What is built where.** **B11** carries the bulk (73 RESOLVED-BY rows: the claim-sourced referents, a rumour that travels, the playable inquiry, testimony that names a hand, the shortest playable case, the CR-29 reach channel first; the A-109 design item at its open); B24 the evidence interface into the hearing; B25 questioning; B26 the inquiry verbs (`examine`, `seize` a record, `destroy_record`). **What stays open:** which row forms a petition from a held conclusion (`08_FI_03_playable-inquiry:162`, INCOMPLETE); WITNESS's deposit rules unopened by sixteen proposals (`audits/25` U-05); two DISPUTED rows.

**Rows: 105** (RESOLVED-BY 95 · SUPERSEDED 5 · STALE/FP 3 · DISPUTED 2 · JORDAN 0).

| # | id | claim | sev | R | evidence | disposition | carrier | batch | owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | F-FI-11 | the hand that did a killing cannot be passed on | B | R-01, R-05, R-07 | `U5c:310` · `08_FI_audit_addendum_B.md:110` · `hearsay_doer_probe.py` | RESOLVED-BY | FI-06 | B11 | FI |
| 2 | F-FI-03 | investigation resolves and does not play | B | R-05 | `U5c:242` · `08_FI_audit.md:240` · `find.py:28-34`; found deposits 0 / 0 / 0 | RESOLVED-BY | FI-07 (Cut A, then §2); FI-03 as reconciled (§2's band gate dropped, §3 by CONC); PFI-D (the t… | B11, B26 | FI |
| 3 | F-FI-01 | a person's candidates move on a fact he has not witnessed or been told | B | R-07, R-08 | `U5c:240` · `08_FI_audit.md:151` · `r08_probe.py` P1, P2 with two controls; `p1_belief.py` `dead-silent` −28; ED-I… | RESOLVED-BY | FI-01 (seats, vacancies, aims, matters); PFI-C edit 4 (who exists and where: the same claim lo… | B11 | FI |
| 4 | F-FI-02 | nothing a person knows reaches another by a person's act | D | R-01, R-07 | `U5c:241` · `08_FI_audit.md:212` · `dynamics.py` (7 / 0 / 0 chained); `p2_chain.py` (the second teller says "a tel… | RESOLVED-BY | FI-02 as reconciled (C-14: arms `unshared`, `unshared_first`; tiers `[told, inferred, deed, qu… | B11 | FI |
| 5 | F-FI-12 | `examine` cannot form on a place | D | R-05 | `U5c:311` · `08_FI_audit_addendum_B.md:160` · `options.py:1213-1214` | RESOLVED-BY | FI-07 §2 (a) | B11 | FI |
| 6 | F-FI-09 | evidence is not a typed input to any contest | D | R-05, R-06 | `U5c:248` · `08_FI_audit.md:344` · H-285, H-301 | RESOLVED-BY | FI-05B with EVID and ADM | B24 | SC |
| 7 | F-FI-10 | what to say, whether to confide, what to forge are engine rules | D | R-06, R-08 | `U5c:249` · `08_FI_audit.md:364` · `person_q.py:1165`; `witness.py:113-138` | RESOLVED-BY | FI-02 §4 (`said`, `in_confidence` as choice-sourced operands); PES-E edit 2 (a lie's direction… | B11 | FI |
| 8 | F-FI-04 | a lie deceives only those it changes nothing for | D | R-07, R-08 | `U5c:243` · `08_FI_audit.md:265` · `options.py:1727`; 1 decline in 461 | RESOLVED-BY | FI-03 §2 and §4; PES-E (the record separates a liar from a garbled truth); PFI-A edit 3 (a lie… | B11 | FI |
| 9 | F-FI-05 | the largest source of what people hold is a channel that reads no person | D | R-07 | `U5c:244` · `08_FI_audit.md:291` · 6,033 of 12,351 claims; `fi_arms.py 0 3 nochron` | RESOLVED-BY | plan CR-29, taken first (FI-02 edit 1), with the gate FRES §2 adds (F-PES-FI-10: `march` and `… | B11 | FI |
| 10 | F-FI-06 | nothing said can be private; nothing hidden can be found | D | R-07 | `U5c:245` · `08_FI_audit.md:308` · H-323, H-324; `_circle_of` | RESOLVED-BY | deeds: B10-14 (CP-T06-09, -01, -02, -07) with PFI-C edits 1–2; speech: FI-02 §4 edit 8 (confid… | B11 | FI |
| 11 | F-FI-07 | `knots.py` holds state, draws unseeded, cites a dead path | H |  | `U5c:246` · `08_FI_audit.md:323` · `knots.py:156-157, :219-221, :347-378` | RESOLVED-BY | FI-04 §5; FI-08 §2 (the swallowed imports), §3 (the order for `_eff_tie`) | B11, B25 | FI |
| 12 | F-FI-08 | Event kinds and register rows that say something else | H |  | `U5c:247` · `08_FI_audit.md:335` · H-318, H-269 | RESOLVED-BY | FI-04 §1 (`inquiry.refused`), §5 (H-116); `argument.held` is carried once, by PES-D (C-15 merg… | B11, B27 | FI |
| 13 | F-FI-13 | the archived design set is forked against itself | H |  | `U5c:312` · `08_FI_audit_addendum_B.md:175` · addendum §B2b | RESOLVED-BY | no edit to the quarantine; FRES §3 states R-47's reading rule | B11 | FI |
| 14 | corrections | addendum C-3; first audit R-04; the told-false cells; FI-02 edit 2's `cell` tier | — | R-04 | `U5c:357` | RESOLVED-BY | the rows above (C-3 stale; R-04 disputed; PFI-A; C-14) | B11 | FI |
| 15 | R-01 | referents about others come from the ledger; R-07/R-08 text corrected | — | R-07, R-08 | `U5c:255` · ED-IN-0292 | RESOLVED-BY | FI-01 edits 2–5, 7 | B11 | FI |
| 16 | §6a hole rows | 59 primary rows verified | — |  | `U5c:290` · audit §6a | RESOLVED-BY | closed and stale heads: FRES §3; wrongly filed rows (H-62, H-92, H-106, H-138, H-182, H-217, H… | B11, B35, B11F2, B03, B21c, B27, B11 (design item, D-18) | FI |
| 17 | E-10 | left to SC: precedent, the opponent's commit, a judge evidence moves | — |  | `U5c:322` · EVID "rung" paragraph | RESOLVED-BY | FRES §4: precedent is an admitted `record` (the `resolution` Record, after CR-36/37); the oppo… | B04, B11, B21c | IN |
| 18 | R-25 | a hearer's regard rides `reception` | — |  | `U5c:279` · H-267 | SUPERSEDED | by G-60 / OBS §2–§3 (`regard` is its own term where no bench hears) | → B05 | IN |
| 19 | R-40 | forgery quality under the per-pool arm | — |  | `U5c:329` · PES-FI §2.2 | STALE/FP | the arm ships and bites (C-3's row above); the term is OBS's `subject` | — (stale) | IN |
| 20 | N-lines | N-1, N-2, N-5 false; N-3, N-4, N-6 narrowed; N-7 holds | — |  | `U5c:360` · PES-FI §1.2 | RESOLVED-BY | N-1: FI-02, FI-06; N-2: PFI-D and the cross-family sink; N-5: PFI-A; N-4: FRES §2's gate; N-6:… | B05, B11, B26 | IN |
| 21 | F-PES-FI-12 | 93.9% of the log is ledger bookkeeping | H |  | `U5c:355` · Event census | RESOLVED-BY | CR-29 removes the broadcast's share; one decay Event per claim per season is IN's (`01_CORE_cl… | B09, B11 | IN |
| 22 | F-PES-FI-13 | a Record's id where a person is meant; a hearth to itself; a man told he exists | H |  | `U5c:356` · `p3_forgery.py` | RESOLVED-BY | PFI-B edit 4; PFI-A edits 2–3 (existence is not garbled); the self-`transfer` is `02_CHAR_offe… | B10, B26, B11 | IN |
| 23 | R-02 | `goal_referents`' docstring reads the ruling backwards | — |  | `U5c:256` · `world_q.py:2836` | RESOLVED-BY | FI-01 edit 2 | B11 | FI |
| 24 | R-03 | own-edge stamps stay; others' state is ledger-gated | — |  | `U5c:257` · `docket_question` precedent | RESOLVED-BY | FI-01 "The rule" | B11 | FI |
| 25 | R-04 | Q2 clause 2 stays (adds no referent) | — |  | `U5c:258` · `p1_belief.py`, `p1d_where.py` | DISPUTED | this lane's evidence is the pessimist's: the clause removes referents on world truth (a silent… | — (disputed) | FI |
| 26 | R-05 | a third `said_slants` arm | — |  | `U5c:259` · H-272 | RESOLVED-BY | FI-02 as reconciled (C-14) | B11 | FI |
| 27 | R-06 | CR-29 first | — |  | `U5c:260` · F-PES-FI-10 | RESOLVED-BY | FI-02 edit 1; FRES §2 (the gate) | B11 | FI |
| 28 | R-07 | a scenario and a conclusion | — |  | `U5c:261` | RESOLVED-BY | FI-07; FI-03 §1, §3, §5; CONC | B11 | FI |
| 29 | R-08 | checking a telling is investigating; a caught teller is a question | — |  | `U5c:262` · H-271 | RESOLVED-BY | FI-03 §2 (as amended by FI-07 §2 (b)), §4 | B11 | FI |
| 30 | R-09 | H-111 and H-314 are answered by the plan | — |  | `U5c:263` · B10-14 | RESOLVED-BY | plan CP-T06-04, CP-T06-03 | B11 | FI |
| 31 | R-10 | `inquiry.refused` | — |  | `U5c:264` · CP-T05-03 precedent | RESOLVED-BY | FI-04 §1 | B11 | FI |
| 32 | R-11 | `argument.held` at Partial | — |  | `U5c:265` · `speak`'s `matter.held` | RESOLVED-BY | PES-D edit 1 (one carrier; FI-04 §1's row points to it, C-15) | B27, B11 | SC |
| 33 | R-12 | `research` needs presence | — |  | `U5c:266` · H-319 | RESOLVED-BY | FI-04 §2 | B11 | FI |
| 34 | R-13 | a repeated ungraded finding mints the same claim | — |  | `U5c:267` · H-320 | RESOLVED-BY | FI-04 §2 (moot per row once PFI-D withholds it and its product lands) | B11, B26 | FI |
| 35 | R-14 | `knots.py` hygiene | — |  | `U5c:268` | RESOLVED-BY | FI-04 §5 | B11 | FI |
| 36 | R-15 | a claim at confidence 0 still closes a trail | — |  | `U5c:269` · H-341 | RESOLVED-BY | FI-04 §2 | B11 | FI |
| 37 | R-16 | H-116's head is stale | — |  | `U5c:270` · 461 declines | RESOLVED-BY | FI-04 §5 | B11 | FI |
| 38 | R-17 | the `fieldwork` contract row describes the oracle; two ED-FI rows unwritten | — |  | `U5c:271` · `module_contracts.yaml:329-362` | RESOLVED-BY | FI-04 §5 | B11 | FI |
| 39 | R-18 | H-234: unrest news is a `reach` row | — |  | `U5c:272` | RESOLVED-BY | FI-02 edit 1 (inside CR-29's roster) | B11 | FI |
| 40 | R-19 | no faction channel | — |  | `U5c:273` · H-351 | RESOLVED-BY | no edit owed (ladder step 4: every channel is place-bound or edge-bound); members learn by tel… | B11 | FI |
| 41 | R-20 | bystanders hear; a garbled copy carries no flag | — |  | `U5c:274` · `_circle_of` docstring | SUPERSEDED | by the rulings the audit cites (H-323, H-345); FI-02 §4 edit 8 is the one change inside them | → B11 | FI |
| 42 | R-22 | `budget` counts Office holds only | — |  | `U5c:276` · H-92 `cite:` | SUPERSEDED | by R-39: measured and declined at IN-14; lands only after FI-02's traffic arm, with `test_n3`'… | → B11 | FI |
| 43 | R-23 | a razing is witnessed where it happened; custody receipts name the prisoner | — |  | `U5c:277` · H-231 | RESOLVED-BY | FI-04 §3 first bullet; the second bullet is carried once, by PES-C edit 1 (wider: an imposed `… | B11, B27 | FI |
| 44 | R-24 | `Record.ttl` has no reader; a writ never lapses | — |  | `U5c:278` · H-259 | RESOLVED-BY | FI-04 §4 first bullet; the in-force reading is `14_VERBS_SOCIAL1_B_documents_and_obedience.md`… | B28, B11 | SC |
| 45 | R-26 | `loop/witness` exceeds `04:178` five times; amend the row | — |  | `U5c:280` · `04` §A.2 row `loop/witness`; `witness.py` head | DISPUTED | Layer 1 is not edited to match the code (`CLAUDE.md` §0.05; UNIFICATION test 7; `layer-conform… | — (disputed) | FI |
| 46 | R-27 | `reconstruct`'s value space and product | — |  | `U5c:281` · K-37 | RESOLVED-BY | CONC (R-19-03, R-19-04) on FI-03 §3 | B11 | FI |
| 47 | R-28 | the confidence break path | — |  | `U5c:282` · H-204 | RESOLVED-BY | FI-02 (gate at `telling_privacy` 1.0) | B11 | FI |
| 48 | R-30 | `said` and confiding as operands | — |  | `U5c:284` · H-94 | RESOLVED-BY | FI-02 §4 | B11 | FI |
| 49 | R-33 | the archived Evidence Track | — |  | `U5c:287` · ED-IN-0319 | RESOLVED-BY | CONC (support over distinct origins, bound on the Proposition) | B11 | FI |
| 50 | §11 item 1 | is who holds a public seat common knowledge? | — |  | `U5c:288` · `fi_arms.py nochron`: marches 29 → 4 without a replacement | RESOLVED-BY | answered by Jordan as two cells of the one `reach` roster. The seat change ships realm-wide, w… | B11 | FI |
| 51 | §11 item 2 | the `loop/witness` may-read cell: amend or restore | — |  | `U5c:289` · `CLAUDE.md` §0.05; D-74 | RESOLVED-BY | FI-04 §6 (C-16). Closed on the decision register as D-74, taken B: fix the witness code, not L… | B11 | FI |
| 52 | §6b workplan | B10-14 cards kept; CR-29 first; CP-T06-05 preconditioned | — |  | `U5c:291` · audit §6b | RESOLVED-BY | FI-02 edit 1; FRES §2 (the order across both lanes and the pessimist) | B11 | FI |
| 53 | §13 classes A–J | arc needs by information class | — |  | `U5c:292` · audit §13 | RESOLVED-BY | A: CR-29, FI-02 §4 · B: CONC, FI-02, PFI-A · C: B10-14, FI-03 §4, CR-83 · D: FI-07, FI-05B, PF… | B11, B26, B24, B25, B11 (design item, D-18) | FI |
| 54 | §13 wrongly stated | Evidence Track; a hidden truth flag; self-ignorance of sensitivity; stored exposure; a faction AI | — |  | `U5c:293` | RESOLVED-BY | the audit's restatements stand; the first two by CONC; no stored track (`04` §B.3) | B11 | FI |
| 55 | §14, §15 | skill reads; hard-coded NPC rules | — |  | `U5c:294` · `options.py:1627` | RESOLVED-BY | the `credit` role and `opposes` rows on U1's surface (cross-family); FI-02 §4; FI-01 | B11 | FI |
| 56 | C-2 | R-22 was measured and declined | — |  | `U5c:301` · H-92 `cite:` | RESOLVED-BY | R-39; FI-04 §4 as amended | B11 | FI |
| 57 | C-4 | `observes:` must not be band-gated | — |  | `U5c:303` · H-218 | RESOLVED-BY | FI-07 §2 (b); FI-03 carries a Reconciled line | B11 | FI |
| 58 | C-5 | the narrow slant ships as its own arm | — |  | `U5c:304` · H-197 | RESOLVED-BY | FI-06 §5 | B11 | FI |
| 59 | C-6 | F-FI-01 is older than the requirement text | — |  | `U5c:305` · H-122 | RESOLVED-BY | no edit owed; FI-01 edit 7 corrects the text | B11 | FI |
| 60 | E-8 | a killing is citable only once its hand travels | — |  | `U5c:320` · F-FI-11 | RESOLVED-BY | FI-06 | B11 | FI |
| 61 | E-9 | the band ceiling is not taken now | — |  | `U5c:321` · H-301 | RESOLVED-BY | no edit owed; it becomes live when `Tenure.degree` has a reader (`05_SC_arrangement_rows_that_… | B27, B11 | SC |
| 62 | R-35 | `observes:` at every band | — |  | `U5c:324` | RESOLVED-BY | FI-07 §2 (b) | B11 | FI |
| 63 | R-36 | two slant arms | — |  | `U5c:325` | RESOLVED-BY | FI-06 §5; C-14 | B11 | FI |
| 64 | R-37 | `examine`'s `site` operand | — |  | `U5c:326` | RESOLVED-BY | FI-07 §2 (a) | B11 | FI |
| 65 | R-38 | the pairing travels | — |  | `U5c:327` | RESOLVED-BY | FI-06 | B11 | FI |
| 66 | R-39 | R-22 re-sequenced | — |  | `U5c:328` | RESOLVED-BY | FI-04 §4 as amended | B11 | FI |
| 67 | R-44 | the case is a `deed_doers` goal | — |  | `U5c:331` · IN-67 | RESOLVED-BY | FI-07 §1 | B11 | FI |
| 68 | R-46 | no Exposure meter | — |  | `U5c:333` | RESOLVED-BY | FI-07 §4 | B11 | FI |
| 69 | R-47 | forks inside the archive | — |  | `U5c:334` | RESOLVED-BY | FRES §3 | B11 | FI |
| 70 | F-PES-FI-01 | a deed leaves no trace but the memory of those present | B |  | `U5c:344` · `p5_crime.py` | RESOLVED-BY | PFI-C edits 1–3 with CP-T06-01, -02 | B11 | FI |
| 71 | F-PES-FI-02 | a rumour is one telling long; what is said is mostly that someone exists | D |  | `U5c:345` · `p2_chain.py`, `told_dump.py 0 2` | RESOLVED-BY | FI-02 as reconciled (C-14); PFI-A edits 1–3, 5 | B11 | FI |
| 72 | F-PES-FI-03 | a forged paper is believed by nobody in play; knowing it false changes nothing | D |  | `U5c:346` · `p3b_knows.py` | RESOLVED-BY | PFI-B edits 1–3; that a forgery travels at all is FI-07's scenario and the chooser's `give` (P… | B26, B11 | FI |
| 73 | F-PES-FI-04 | who exists and where is read from the truth | B |  | `U5c:347` · `p1_belief.py`, `p1d_where.py` | RESOLVED-BY | PFI-C edit 4 with FI-01; FRES §1 | B11 | FI |
| 74 | F-PES-FI-06 | distortion drifts anything stored as a number | D |  | `U5c:349` · `p2_proxy.py` | RESOLVED-BY | PFI-A edits 1–4 | B11 | FI |
| 75 | F-PES-FI-07 | a better look is worse than a failed one | D |  | `U5c:350` · `p4_detective.py` (0.15 at pool 2) | RESOLVED-BY | plan CP-T06-03 | B11 | FI |
| 76 | F-PES-FI-08 | a claim is a pointer; a death is said two ways | D |  | `U5c:351` · `p1c_exists.py` | RESOLVED-BY | PFI-C edit 3 (one vocabulary for an ending); the general case is CHAR's question projection (c… | B11 | FI |
| 77 | F-PES-FI-09 | news of a death does not travel | D |  | `U5c:352` · `fi_arms.py` arms | RESOLVED-BY | FI-06; FI-02; the `reach` cell for `person.died` is answered (A-33: presence, trail and tellin… | B11 | FI |
| 78 | F-PES-FI-10 | cutting `chronicle` alone stops the marches | D |  | `U5c:353` · `nochron` arm | RESOLVED-BY | FRES §2 (CR-29's gate) | B11 | FI |
| 79 | F-PES-FI-11 | fixed outcomes that could go either way | D |  | `U5c:354` · PES-FI §0 | RESOLVED-BY | CP-T06-03 (the lockout); C-12 (`interview`: the answer is the questioned person's draw); CONC… | B11 | FI |
| 80 | S-PES-FI-1 | may a garbled deed name the wrong person? | — |  | `U5c:358` · PFI-A "For Jordan" | SUPERSEDED | closed by the ladder at step 3: K-37 (ratified as intent, ED-IN-0288) admits no wrong value fr… | → B11 | FI |
| 81 | S-PES-FI-2 | how fast does a death travel compared with the seat it empties? | — |  | `U5c:359` · A-33 | RESOLVED-BY | answered by Jordan, A-33 (D-43: apart from the seat's news). Merged with FI §11 item 1: two ce… | B11 | FI |
| 82 | R-29 | the evidence interface | — |  | `U5c:283` | RESOLVED-BY | FI-05B | B24 | SC |
| 83 | R-32 | seven archived reliability tags | — |  | `U5c:286` | RESOLVED-BY | FI-05B E-1 (kind and weight derived, never stored) | B24 | SC |
| 84 | C-8 | the companion refuses contradiction-matching and steals the band ceiling | — |  | `U5c:307` · companion Part 2 §6 | RESOLVED-BY | FI-05B E-6, E-9 | B24 | SC |
| 85 | E-1 | one operand, ids only | — |  | `U5c:313` | RESOLVED-BY | FI-05B; EVID | B24 | SC |
| 86 | E-2 | the case file holds what was said; entered at Success+ | — |  | `U5c:314` · LACUNA C-1 | SUPERSEDED | by ADM (C-05): entry is keyed by the citing `speak`'s band, four results; FI-05B's text edited… | → B24 | SC |
| 87 | E-3 | a citation is a telling | — |  | `U5c:315` | RESOLVED-BY | FI-05B edit 2, with ADM's sentence (the deposit fires whether or not the item is entered) | B24 | SC |
| 88 | E-4 | two carriers, one fact each | — |  | `U5c:316` | RESOLVED-BY | FI-05B | B24 | SC |
| 89 | E-5 | three ways to answer | — |  | `U5c:317` · SC addendum C-4 | RESOLVED-BY | FI-05B edit 1; EVID rules 1–2; the owner of "contradicts" is `decision/options.py::contradicts… | B24 | SC |
| 90 | E-6 | an answer is a rolled act | — |  | `U5c:318` | RESOLVED-BY | EVID rules 1–2 (one rule in both files, sweep D-01) | B24 | SC |
| 91 | E-7 | bluster is the control; citing costs disclosure | — |  | `U5c:319` | RESOLVED-BY | FI-05B; EVID | B24 | SC |
| 92 | R-41, R-42, R-43 | `cites`; the `Said` on the stage; the found deposit is the impeaching item | — |  | `U5c:330` | RESOLVED-BY | FI-05B E-1, E-2, E-5 | B24 | SC |
| 93 | C-1 | the knot waits on rumour traffic, not on `_eff_tie` | — |  | `U5c:300` · H-182 `cite:` | RESOLVED-BY | FI-08 §3 | B25 | FI |
| 94 | C-9 | three old findings are now false; the swallowed imports remain | — |  | `U5c:308` · addendum §B7 runs 1–3 | RESOLVED-BY | FI-08 §2 for the imports; the three are recorded as stale | B25 | FI |
| 95 | R-34 | strain is a reading, not a field | — |  | `U5c:323` · `04` §A.3 row 9 | RESOLVED-BY | FI-08 §4 | B25 | FI |
| 96 | R-48 | a person witnesses through a knot he owns | — |  | `U5c:335` · `04:388` | RESOLVED-BY | FI-08 §1 | B25 | FI |
| 97 | R-50 | delete the `try/except` wrappers | — |  | `U5c:337` · `knots.py:347-378` | RESOLVED-BY | FI-08 §2 | B25 | FI |
| 98 | R-21 | `standing` is one constant for everyone | — |  | `U5c:275` · `04` §B.10 note on `Sensation` | STALE/FP | irrelevant at HEAD: no deposit mints a `person_predicates` claim and no chooser term reads `st… | — (stale) | FI |
| 99 | R-31 | one vocation for three inquiries | — |  | `U5c:285` · `verb_capability` | RESOLVED-BY | no engine edit owed: authoring (two data rows on the skill surface U1 decides) | B04 (B04.03) content | FI |
| 100 | C-3 | forgery quality is inert at the shipped fixtures, refused at quality 3 | — |  | `U5c:302` · `p4_detective.py 300` (PES-FI §2.2) | STALE/FP | false at HEAD: quality 0 → 1 moves Failure 68.3% → 91.0% at pool 2; nothing is refused (the pe… | — (stale) | FI |
| 101 | C-7 | Heavy Rain is named nowhere in the tree | — |  | `U5c:306` · addendum §B7 run 4 | RESOLVED-BY | R-49 (dropped as a referent; no file cites it for a design) | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FI |
| 102 | C-10 | the three-season runs | — |  | `U5c:309` · addendum §B7 run 3 | RESOLVED-BY | no edit owed (readings) | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FI |
| 103 | R-45 | Disposition is `regard` | — |  | `U5c:332` · ruling R7 | RESOLVED-BY | no edit owed (the code governs) | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FI |
| 104 | R-49 | Heavy Rain dropped | — |  | `U5c:336` | RESOLVED-BY | no edit owed | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FI |
| 105 | F-PES-FI-05 | the information verbs crowd the game out | D |  | `U5c:348` | RESOLVED-BY | `fi_arms.py 0 3 nofi`, `nod3` against `draw1` | B26 (B26.06) | FI |

---

## FA — factions, offices, war and land

**What is wrong.** A sound skeleton (authority is a property of the seat exercised; a faction is a derived view; no entity special-cased) without force or turnover (`audits/06_FA_audit.md` §0): 91 decrees in three seasons at seeds 0–2, none held, obeyed or defied (F-FA-01); power does not change hands (F-FA-02); the military verbs are open to clerks (F-FA-03); war has no producer (F-FA-04); there is no FA scenario or end condition (F-FA-07); a defeat costs bodies and never a holding or a seat (F-FA-13); men are levied by whoever minted a paper (F-FA-15). The pessimist (`16_PESSIMIST_FA.md` §0): the realm runs the same with every office empty and with every faction dissolved, inside the noise of the dice; a vacant seat is filled by the Crown or by nobody (F-PES-FA-01); the power to dismiss is one unfillable seat (F-PES-FA-02); royalty by noble conquest is not in the engine (F-PES-FA-06).

**What was decided.** Governance is the loop's own verbs, no module (A-10); a decree is proclaimed (A-21); command, not territory (A-22); custody suspends acts through the seat (A-23); a seat carries a modifier and three optional facts (A-12, A-13, `_part2` §4.3); a vote is a draw (A-14); the crown when the line fails is the deed race (A-19); war lives in the seats that wage it (A-20); a head strips an officer by a resistible draw (A-35), nobody judges the Confessor (A-36); land and the march (A-57 to A-70, A-73, A-74, A-103, `_part2` §4.4); a grant reduction is a revocation (A-105).

**What is built where.** **B21** the governance (51 RESOLVED-BY rows: the decree binds, remit by row, seat terms and turnover, war in the seats, the levy through the seat, the playable scenario and the shortest loop); B21b war (IN-36's cap, the claim as occasion), B21c seats and the Parliament constraint (CR-38 design-first), B21d the arc; B23 land; B32 and B33 the institutions kit; B40 its scenarios. **What stays open:** A-76's stand-in until H-90's Court Parliament; the ducal homes (`_part2` §5.2); one JORDAN row, answered by A-76.

**Rows: 118** (RESOLVED-BY 97 · SUPERSEDED 16 · STALE/FP 4 · DISPUTED 0 · JORDAN 1).

| # | id | claim | sev | R | evidence | disposition | carrier | batch | owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | F-FA-01 | a decree binds nobody and reaches nobody as a writ | B | R-02, R-04 | `U5d:56` · `06_FA_audit.md:132` · realm seeds 0–2: 29, 21, 41 writs, 0 answered; `comply` 0 of 33 (audit E-3, E-5) | RESOLVED-BY | DECREE edits 1–5 as reconciled (A-21: proclaimed is ruled, so edit 1 loses its `[ASSUMPTION]`;… | B21 | FA |
| 2 | F-PES-FA-02 | the power to dismiss is one unfillable seat; the ban cannot be undone; a detained officer governs | B | R-02, R-04 | `U5d:181` · `16_PESSIMIST_FA.md:502` · `pf2b` §1, §4, §5 | RESOLVED-BY | PES-FA-A edits 1–3; the detained officer: OWED-FA §2 (A-23: custody suspends acts through the… | B21 | FA |
| 3 | F-FA-02 | power does not change hands in computed play | B | R-04 | `U5d:57` · `06_FA_audit.md:161` · `confer` formed 5, attempted 0; `succession.claimed` 0 (E-3, E-5) | RESOLVED-BY | TERMS edits 1–5 (the term on the row); TERMS-B (which rows); DECREE edit 5 (`revoke` reads its… | B37, B21 | IN |
| 4 | F-PES-FA-01 | a vacant seat is filled by the Crown or by nobody | B | R-04, R-09 | `U5d:180` · `16_PESSIMIST_FA.md:492` · `pf1_static.py 0`; `pf2_premise.py 0` P2 | RESOLVED-BY | PES-FA-B edits 1–2; VB-C; the election arms; the crown's fallback is ruled (A-19) and carried… | B21 | FA |
| 5 | F-FA-07 | no FA scenario, digest or end condition | B |  | `U5d:62` · `06_FA_audit.md:258` · `harness/governance_spine.py` prints a census only | RESOLVED-BY | SCEN; LOOP-B (A-10 confirms the form: a scenario on the season loop, no module) | B21 | FA |
| 6 | F-PES-FA-06 | royalty by noble conquest is not in the engine | B |  | `U5d:185` · `16_PESSIMIST_FA.md:532` · grep and `pf1` (c) | RESOLVED-BY | `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md` (the seeded deeds), on A-17/A-18 (the south f… | B32 | FA |
| 7 | F-FA-03 | the military verbs are open to clerks by an unruled placeholder | D | R-04 | `U5d:58` · `06_FA_audit.md:191` · 26 of 33 seats may `march` (E-3) | RESOLVED-BY | REMIT edits 1–4 | B21 | FA |
| 8 | F-PES-FA-03 | "under the seat" is where a person sleeps | D | R-04 | `U5d:182` · `16_PESSIMIST_FA.md:511` · 18 of 34 seat-holders off their ground | RESOLVED-BY | PES-FA-C as reconciled (A-22: the predicate is the command basis: sworn men, holders of seats… | B21 | FA |
| 9 | F-PES-FA-04 | a faction cannot refuse a member; the governed are in none | D | R-04, R-06 | `U5d:183` · `16_PESSIMIST_FA.md:520` · `pf2` P4; `pf3_cut.py 0 2` | RESOLVED-BY | PES-FA-B edit 3; the governed: `U5d_SE_cohort_heavy_moves_and_caste.md` (A-56) | B38, B21 | WR |
| 10 | F-PES-FA-05 | anyone declares war for anyone | D | R-04 | `U5d:184` · `16_PESSIMIST_FA.md:527` · `pf2` P3 | RESOLVED-BY | PES-FA-B edit 4 with WAR-B (A-20) | B23, B21 | FA |
| 11 | F-FA-05 | an officer's choices do not read his office | D |  | `U5d:60` · `06_FA_audit.md:228` · `decision/choose.py` reads no seat (audit §15) | RESOLVED-BY | CAPS-FA edits 3–4 as reconciled (A-12: the seat's modifier may now reach the roll, not only th… | B04, B21d | IN |
| 12 | F-PES-FA-10 | the governance record does not carry its reasons | D |  | `U5d:189` · `16_PESSIMIST_FA.md:563` · audit §3.4 | RESOLVED-BY | OWED-FA §5; `01_CORE_reason_trail_in_the_act_store.md` (U5a) | B09, B21 | IN |
| 13 | F-FA-06 | orders and sittings are announcements | D |  | `U5d:61` · `06_FA_audit.md:246` · H-260; `determine` 0, 1, 0 (E-5) | RESOLVED-BY | DECREE (orders); OWED-FA §5 (what an order orders, R-27); sittings are SC's (`05_SC_playable_h… | B24, B21 | SC |
| 14 | F-FA-08 | a malformed term and two live holders end the season instead of refusing | D |  | `U5d:63` · `06_FA_audit.md:273` · `effects_governance.py:50-54` `[not re-opened]` | RESOLVED-BY | TERMS edit 2 (`_req_confer` refuses a malformed term); H-133 stays registered, unreached by an… | B21, B21b | FA |
| 15 | F-FA-15 | men are levied by whoever minted a paper | D |  | `U5d:157` · `06_FA_audit_addendum_B.md:147` · E-B3 | RESOLVED-BY | LEVY-B as reconciled (A-22: the cohort is "the unseated in its land") | B21 | FA |
| 16 | F-FA-16 | five of ten factions have no head; one has no members | D |  | `U5d:158` · `06_FA_audit_addendum_B.md:172` · E-B2 | RESOLVED-BY | TERMS-B edit 4 (two heads); the Guilds headless by design; R-34 (`faction x` excluded by name) | B21 | FA |
| 17 | F-PES-FA-07 | offices are free to cut | D |  | `U5d:186` · `16_PESSIMIST_FA.md:539` · `pf3_cut.py 0 2 NO_SEATS` | RESOLVED-BY | none of its own (a measure): the NO_SEATS arm is the gate of DECREE, TERMS and PES-FA-A–C (it… | B21 | FA |
| 18 | F-PES-FA-08 | two heads for one faction | D |  | `U5d:187` · `16_PESSIMIST_FA.md:546` · `pf5_heads.py` | RESOLVED-BY | OWED-FA §8 (`opinion_of` reads `faction_q.head` first) | B21 | FA |
| 19 | F-PES-FA-09 | a dead ruler's decrees are orphan paper | D |  | `U5d:188` · `16_PESSIMIST_FA.md:555` · `pf2` P1.5, P1.7 | RESOLVED-BY | OWED-FA §9 (a writ is the seat's; its `hold` passes with the seat) | B21 | FA |
| 20 | F-FA-04 | war has no producer and draws no response | D |  | `U5d:59` · `06_FA_audit.md:212` · `at_war` false at every seed; `tests/test_faction_q.py:223-262` (C-1) | RESOLVED-BY | plan CP-T09-02 (`declare`) with WAR-B edits 1–5 as reconciled (A-20) and VB-E; corrected in pa… | B23, B21b | FA |
| 21 | F-FA-13 | a defeat costs bodies and never a holding or a seat | D |  | `U5d:155` · `06_FA_audit_addendum_B.md:96` · `architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md:90`; `loop/effects_combat.py::… | RESOLVED-BY | **LAND** (`U5d_FA_land_and_seats_pass_on_a_won_march.md`, written by this lane on A-57, A-58 a… | B23 | FA |
| 22 | F-FA-09 | the contract file describes a faction the code retired | H |  | `U5d:64` · `06_FA_audit.md:286` · `module_contracts.yaml:127, :797` `[not re-opened]` | RESOLVED-BY | HYG item 5 (R-09) | B03 | IN |
| 23 | F-FA-10 | unreached query surface in `faction_q` | H |  | `U5d:65` · `06_FA_audit.md:295` · audit E-9 | RESOLVED-BY | HYG item 3 (R-10) | B03 | IN |
| 24 | F-FA-11 | `dispensation` and `oblige` say the opposite of what they do | H |  | `U5d:66` · `06_FA_audit.md:304` · H-262, H-298 | RESOLVED-BY | HYG item 4 (R-11, R-12); declared hash mover | B03 | IN |
| 25 | F-FA-12 | H-230 and H-206 describe a tree that no longer exists | H |  | `U5d:67` · `06_FA_audit.md:309` · `_eff_succeed`, `successions`, `death_subjects` in the tree | RESOLVED-BY | HYG item 1 (R-13) | B03 | IN |
| 26 | F-FA-17 | at tick 0 no rung holds a store | H |  | `U5d:159` · `06_FA_audit_addendum_B.md:188` · addendum E-B1 | RESOLVED-BY | `07_SE_treasury_granary_B.md`; the seeded start draws bounded stores (A-50, `21_PROCEDURAL_D_w… | B39, B12a-c | WR |
| 27 | F-PES-FA-12 | single-seed verb counts are one draw from a wide spread | H |  | `U5d:191` · `16_PESSIMIST_FA.md:572` · `oblige` 26 → 0 | RESOLVED-BY | none owed (a caution); gates in this family read at ≥ 2 dice seeds | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FA |
| 28 | H-206, H-230 | stale heads | — |  | `U5d:82` · `gate.py:1819-1832` | RESOLVED-BY | HYG item 1 | B03 | IN |
| 29 | H-252 | which clause refused | — |  | `U5d:84` · E-3 | RESOLVED-BY | HYG item 2 (R-14) | B03 | IN |
| 30 | H-262, H-298 | names | — |  | `U5d:86` | RESOLVED-BY | HYG item 4 | B03 | IN |
| 31 | `HANDOFF_FA.md` row 3 | orders authoring into `.designs/` | — |  | `U5d:97` | RESOLVED-BY | HYG item 6 (R-15) | B03 | IN |
| 32 | R-09, R-10, R-11, R-12, R-13, R-14, R-15 | hygiene rows | — |  | `U5d:111` | RESOLVED-BY | HYG items 5, 3, 4, 4, 1, 2, 6 | B03 | IN |
| 33 | H-207 | `confer` formed, never attempted | — |  | `U5d:83` · E-3 | RESOLVED-BY | TERMS (vacancies on a clock) and CAPS-FA edit 4 (the conferee is ranked) | B21, B04 | FA |
| 34 | NPC-008 (an office makes reform harder… | "wrongly stated against the architecture" | — |  | `U5d:128` · `04` §B.7 (to be amended on A-12; text owed, not applied) | SUPERSEDED | A-12: a seat may carry a modifier; the need stands as stated and is carried by CAPS-FA as reco… | → B04, B21c | IN |
| 35 | §14 (skill surface), §15 (chooser surfa… | whom to seat reads nothing about the candidate | — |  | `U5d:143` · audit §14 table | RESOLVED-BY | CAPS-FA; `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` owns the home | B04 | IN |
| 36 | H-91 | `remit:revoke` beside purview | — |  | `U5d:76` · `gate.py:370-375` `[not re-opened]` | STALE/FP | closed by precedent (R-05); OWED-FA §7 re-grades the row | — (stale) | FA |
| 37 | H-144 | measured; verified closed | — |  | `U5d:79` · `predicates.py:403-410` | STALE/FP | OWED-FA §7 re-grades the row | — (stale) | FA |
| 38 | H-260 | obeying and defying change nothing | — |  | `U5d:85` · measured on hand-placed writs | RESOLVED-BY | DECREE edit 4 | B21 | FA |
| 39 | H-290 | a malformed term raises | — |  | `U5d:87` | RESOLVED-BY | TERMS edit 2 | B21 | FA |
| 40 | H-294 | a ban bars openings only, everywhere | — |  | `U5d:89` | RESOLVED-BY | TERMS edit 6 (R-06: scoped to the banning seat's purview) | B21 | FA |
| 41 | H-352 | one purse per rung | — |  | `U5d:90` · `requisition.taken` 0, 1, 6 (E-5) | RESOLVED-BY | OWED-FA §6 (R-07: the `treasury:` anchor, built when reached); `07_SE_treasury_granary_B.md` o… | B12a-c, B21 | SE+WR |
| 42 | CP-T09-06 | the card misstates the present value | — |  | `U5d:93` · `offices.yaml:206` | RESOLVED-BY | PES-FA-A edit 1 (`null → inheritance` and the `successions` row) as reconciled (A-19) | B21 | FA |
| 43 | CR-54 | no design file | — |  | `U5d:94` | RESOLVED-BY | DECREE §4 and edit 5 | B21 | FA |
| 44 | R-01 | a writ reaches no addressee | — |  | `U5d:103` | RESOLVED-BY | DECREE edits 1–3 (A-21) | B21 | FA |
| 45 | R-02 | obeying and defying change nothing | — |  | `U5d:104` · ED-IN-0046, ED-IN-0047 `[ledger rows not re-opened]` | RESOLVED-BY | DECREE edit 4; the recall threshold opens the issuer's question and decides nothing (A-47, A-2… | B21 | FA |
| 46 | R-03 | `revoke` has no motive and reads no subject | — |  | `U5d:105` | RESOLVED-BY | DECREE edit 5 | B21 | FA |
| 47 | R-04 | which seats hold `dispatch` | — |  | `U5d:106` | RESOLVED-BY | REMIT edits 1–3 | B21 | FA |
| 48 | R-05 | is `remit:revoke` necessary | — |  | `U5d:107` | RESOLVED-BY | OWED-FA §7 (no code edit; the register row re-graded) | B21 | FA |
| 49 | R-06 | a ban's scope and reach | — |  | `U5d:108` | RESOLVED-BY | TERMS edit 6 | B21 | FA |
| 50 | R-07 | one purse per rung | — |  | `U5d:109` | RESOLVED-BY | OWED-FA §6 | B21 | FA |
| 51 | R-08 | faction of seat against membership of holder | — |  | `U5d:110` | RESOLVED-BY | none owed (leave two); PES-FA-B edit 3 adds admission to joining | B21 | FA |
| 52 | R-16 | the queen consort holds the King's remit | — |  | `U5d:112` · NPC-032 | RESOLVED-BY | REMIT edit 4 as reconciled: it lands with A-19's deed race so the throne is not stranded (F-PE… | B21 | FA |
| 53 | R-17 | no computed act declares a term | — |  | `U5d:113` | RESOLVED-BY | TERMS edit 1 | B21 | FA |
| 54 | R-18 | CP-T09-06's card | — |  | `U5d:114` | RESOLVED-BY | PES-FA-A edit 1 | B21 | FA |
| 55 | R-19 | no scenario, digest or end | — |  | `U5d:115` | RESOLVED-BY | SCEN; LOOP-B | B21 | FA |
| 56 | R-21 | Church and Löwenritter seats strippable by nobody | — |  | `U5d:117` · 2026-10-11 `revocation: null` | SUPERSEDED | A-35 (the head strips an officer by a resistible draw; Löwenritter unstrippable until a head s… | → B32, B21 | FA |
| 57 | §11 item 1 | is a decree public or paper | — |  | `U5d:118` | SUPERSEDED | A-21 (proclaimed); DECREE as written | → B21 | FA |
| 58 | NPC-083, NPC-038 (warrant), ARC-17, ARC… | orders answered; the superior responds | — |  | `U5d:126` · E-3, E-5 | RESOLVED-BY | DECREE | B21 | FA |
| 59 | NPC-008 (refill), NPC-070, NPC-006, NPC… | who is next in the chain | — |  | `U5d:129` | RESOLVED-BY | TERMS; TERMS-B | B21 | FA |
| 60 | NPC-020, NPC-031 (heir; the throne by c… | claim unobserved | — |  | `U5d:133` · E-6 | RESOLVED-BY | SCEN (`succession` situation); `22_HAPPENINGS_B_the_throne_is_never_stranded.md` as reconciled… | B21 | FA |
| 61 | NPC-032 | a consort with standing and no action economy | — |  | `U5d:136` · `aperture 2 0` | RESOLVED-BY | REMIT edit 4 (as R-16) | B21 | FA |
| 62 | NPC-036, NPC-072, NPC-082, NPC-034 | a command post matters | — |  | `U5d:138` · E-3 | RESOLVED-BY | REMIT | B21 | FA |
| 63 | NPC-037, NPC-013 | a treasury post moves resources | — |  | `U5d:139` · E-5 | RESOLVED-BY | OWED-FA §6 | B21 | FA |
| 64 | fourteen UNCLEAR needs (NPC-071, -034 t… | content debts on `npc_registry.yaml` and `offices.yaml` | — |  | `U5d:142` · E-8 | RESOLVED-BY | REMIT edit 3 (rows for unauthored seats); the generated cast (A-44, `21_PROCEDURAL_B_cast_and_… | B39, B21 | WR |
| 65 | C-2 | `marshal`, `surrender` and the army verbs are withheld by a fixture | — |  | `U5d:150` · `data/fixtures.py:1157` | RESOLVED-BY | MB's step 5 lifts the withholding (U5b); LEVY-B lands first | B21 | FA |
| 66 | C-6 | eight `elected` rows at `term: 8` do not fit the design | — |  | `U5d:154` · E-B2 | RESOLVED-BY | TERMS-B (three rows; life seats `null`), which supersedes TERMS's first authoring in content | B21 | FA |
| 67 | F-FA-18 | what an order orders exists only as prose | unrated in source |  | `U5d:160` · H-44 | RESOLVED-BY | OWED-FA §5 (R-27: a closed set of term shapes, built after an answered writ is observed); VB-D… | B21 | FA |
| 68 | R-24 | men by a Record's holder, stores by a seat | — |  | `U5d:163` | RESOLVED-BY | LEVY-B | B21 | FA |
| 69 | R-25, R-26 | heads; which seats take a term | — |  | `U5d:164` | RESOLVED-BY | TERMS-B | B21 | FA |
| 70 | R-27 | what a writ may order | — |  | `U5d:165` | RESOLVED-BY | OWED-FA §5 | B21 | FA |
| 71 | R-29 | faction weight has no reading | — |  | `U5d:167` | RESOLVED-BY | OWED-FA §4 as amended by A-42: `faction_q.weight` reads the authored territory/caste weight (f… | B21 | FA |
| 72 | §B6.2 item 2 | franchise | — |  | `U5d:173` | SUPERSEDED | A-42 (authored as the vote-block carrier); OWED-FA §4 | → B21 | FA |
| 73 | §4.1 | fixed outcomes in FA's code | — |  | `U5d:192` · `18_DETERMINISM_SWEEP.md` C-07, C-11 | RESOLVED-BY | VB-C (the draws); PES-FA-B edit 2 prices, never forbids | B21 | FA |
| 74 | H-90 | ladder and purview built; Parliament and delegation unbuilt | — |  | `U5d:75` | RESOLVED-BY | plan CR-35 to CR-37, IN-48; the vote's form is ruled (A-14: a draw on the voter inside the pre… | B32, B21c, B21b | FA |
| 75 | H-108 | delegation without a hold reverted | — |  | `U5d:77` | SUPERSEDED | A-10 (governance is the loop's own verbs) leaves IN-48 the owner; A-22 fixes whom a seat comma… | → B21b | FA |
| 76 | H-101 | closed at office scale by assumption | — |  | `U5d:80` · `gate.py:422-461` | RESOLVED-BY | plan CR-09 (the set form) | B21b | FA |
| 77 | H-158 | no computed act pays upkeep | — |  | `U5d:81` · not re-measured by the audit | RESOLVED-BY | `07_SE_population_census.md` (men under arms do not `work`, R-31); `04_MB_campaign_party_econo… | B31, B12a-c | MB |
| 78 | NPC-083 (methods handing influence to i… | no method operand | — |  | `U5d:127` | SUPERSEDED | SE's closure (Part 2: `07_SE_capability_and_chooser_surface.md`) | → B12a-c | SE+WR |
| 79 | NPC-020 (acts in his name diverge), NPC… | `dispatch` that sends; demand; treaty | — |  | `U5d:131` | RESOLVED-BY | plan CP-T09-08, CP-T09-02, CP-T09-03, FA-01 | B21b | FA |
| 80 | NPC-050 (campaign toward a higher seat)… | claims, deposition, clocks | — |  | `U5d:135` | RESOLVED-BY | plan CR-91, CR-37, CR-89, restated as "a threshold opens a mandatory scene" (A-47) | B21b, B21c, B21d | FA |
| 81 | NPC-003, NPC-041 | a leader with influence before any seat | — |  | `U5d:137` | RESOLVED-BY | plan IN-30, CR-39 | B21b, B21c | FA |
| 82 | R-28 | nothing between "no act" and "march" | — |  | `U5d:166` | RESOLVED-BY | plan CP-T09-03 (`covenant` as the instrument); no new verb | B21b | FA |
| 83 | R-31 | an army in being costs nothing | — |  | `U5d:169` | RESOLVED-BY | `07_SE_population_census.md` (cross-listed) | B12a-c | SE+WR |
| 84 | H-292, H-217 | elected seats fill by plain `confer`; no `succession` row | — |  | `U5d:88` · `FILLED_BY["elected"]` is `{conferral}` | RESOLVED-BY | plan CR-35 with the kit's election (`15_INSTITUTIONS_PAPACY_B_patronage_election_discipline.md… | B32, B21c | FA |
| 85 | NPC-020, NPC-050, NPC-081, NPC-052 | contested succession; election | — |  | `U5d:134` · H-217, H-292 | RESOLVED-BY | plan CR-35; A-19 (the deed race); A-14 (the vote) | B21c | FA |
| 86 | CR-88, CR-89, CR-91 | B10-17b unbuilt | — |  | `U5d:95` | RESOLVED-BY | the plan positions; CR-89's clocks open scenes and decide nothing (A-47) | B21d | FA |
| 87 | NPC-020, NPC-070 (an army reassesses it… | carrier yes, behaviour no | — |  | `U5d:132` | RESOLVED-BY | plan CR-88; the Split is a strife move (A-46) | B21d | FA |
| 88 | ARC-01, ARC-03 | a quantity that moves from the absence of any act ("wrongly stated against a ruling") | — |  | `U5d:141` · ED-IN-0345 `[ledger row not re-opened]` | RESOLVED-BY | restated on events that mark inaction (the audit's own restatement); plan CR-89 | B21d | FA |
| 89 | CP-T09-01 to -09, CR-09, CR-32, CR-35 t… | planned, unbuilt | — |  | `U5d:92` · no `declare`, `retain`, `conspire` row (E-2) | RESOLVED-BY | the plan positions; one clause each from WAR-B edits 5–6 | B23 | FA |
| 90 | C-7 | nothing a battle decides is read back by a governance verb (a Layer 1 shortfall) | — |  | `U5d:153` · `10_FACTIONS_AND_DEPLOYMENT.md:90` | RESOLVED-BY | LAND (as F-FA-13) | B23 | FA |
| 91 | F-FA-14 | under the planned `at_war`, one committer keeps two factions at war | unrated in source |  | `U5d:156` · `04:460` | RESOLVED-BY | WAR-B edits 1–4 as reconciled: A-20 rules (B), so the "lands only on that ruling" hold is lift… | B23 | FA |
| 92 | R-22 | Layer 1's battle roster names stakes the code does not pass ("keep β: a field writes presence") | — |  | `U5d:161` · `_eff_march`'s own tag ("revert: Jordan states α") is discharged as ruled, not… | RESOLVED-BY | β is ruled for the field's write (A-66); the stakes are met by the victor's choice: LAND edits… | B23 | FA |
| 93 | R-23 | whose edge a war is | — |  | `U5d:162` | RESOLVED-BY | WAR-B (A-20) | B23 | FA |
| 94 | R-32 | may `at_war` reach a verb's `requires` | — |  | `U5d:170` | RESOLVED-BY | WAR-B edit 7 (a) (no; an outcome Query) | B23 | FA |
| 95 | D-20 as re-ruled | what a won battle does to land and seats | — |  | `U5d:827` · `_eff_march`, `_seize_rung`, `_take_hold`, `occupies`, `gate.py:291-300` (each… | RESOLVED-BY | LAND (`U5d_FA_land_and_seats_pass_on_a_won_march.md`): rules 1–9, edits 1–7 | B23 | FA |
| 96 | `26_MASS_BATTLE_aggression_and_land.md`… | does the land pass when the beaten army was not the holder's | — |  | `U5d:828` | SUPERSEDED | A-65, A-66 (he chooses); LAND rule 4 | → B23 | FA |
| 97 | the same file §2, §4 (an unopposed entr… | open land cases | — |  | `U5d:829` | SUPERSEDED | A-67 to A-70; LAND rules 5–8, decisions D5, D6, D8 | → B23 | FA |
| 98 | A-66's marked assumption | is seizure a default or an act the victor forms | — |  | `U5d:830` · `_seize_rung` docstring | RESOLVED-BY | LAND, "The settled rules" 1–2: confirmed at the owner; `seize` is the existing act | B23 | FA |
| 99 | A-68's marked assumption (the parliamen… | "the kingdom parliament is functional" has no working state in code | — |  | `U5d:831` · body `Court Parliament` in `rosters.yaml: office_bodies`; arrangement `parliame… | JORDAN | (A) the Court Parliament when it is built (the rule waits; until then every unopposed entry is… | — (answered A-76) | FA |
| 100 | C-3 | the FA→MB interface was understated | — |  | `U5d:151` | RESOLVED-BY | corrected in the addendum §B4.2; `04_MB_campaign_party_economy.md` (U5b) | B31 | MB |
| 101 | H-21, H-41, H-99, H-100 | listed open; verified closed | — |  | `U5d:73` · `effects_governance.py:538-544`; `office.established` 1 (E-5); `REVOCATION_DISP… | STALE/FP | none owed (H-352 carries H-21's residue) | — (stale) | FA |
| 102 | H-70, H-156, H-161, H-163, H-281, H-297 | open; another lane's (CHAR, CORE, SC) | — |  | `U5d:74` · audit §6.1 "cross-listed" | SUPERSEDED | the owning closures (U5a for H-70, H-156; U5c for H-161, H-163, H-281, H-297) | — | FA |
| 103 | H-133 | two live holders on one office | — |  | `U5d:78` | RESOLVED-BY | none owed: stays registered (F-FA-08); no builder produces the state | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FA |
| 104 | H-353 | a seat's faction and a holder's membership are two records | — |  | `U5d:91` | STALE/FP | none owed (R-08: leave them two; `world_q.leaders`' docstring) | — (stale) | FA |
| 105 | FA-03, FA-07 | held, leave | — |  | `U5d:96` | RESOLVED-BY | none owed (reference) | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FA |
| 106 | R-20 | "registered module" against a subsystem with no verbs of its own | — |  | `U5d:116` | SUPERSEDED | A-10: the loop's own verbs; no governance module | — | FA |
| 107 | §11 item 2 | the standing requirement against Layer 1 for FA | — |  | `U5d:119` | SUPERSEDED | A-10 | — | FA |
| 108 | §11 item 3 | seats nobody can strip | — |  | `U5d:120` | SUPERSEDED | A-35, A-36 (as R-21) | — | FA |
| 109 | NPC-038, NPC-004, NPC-070 (removal) | removable only by death | — |  | `U5d:130` | SUPERSEDED | A-35 (as R-21) | — | FA |
| 110 | NPC-073, NPC-074, NPC-084, ARC-R18 | a council seat casts a position; a vote neither side wins | — |  | `U5d:140` | SUPERSEDED | SC's closure (U5c); the vote is A-14 | — | FA |
| 111 | C-1 | F-FA-04's "no producer" is true only of computed play | — |  | `U5d:149` · `tests/test_faction_q.py:223-262` | RESOLVED-BY | corrected in the addendum; no edit owed | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FA |
| 112 | C-4, C-5, C-8 | corrections of reading | — |  | `U5d:152` · E-B1, E-B6, E-B7 | RESOLVED-BY | corrected in the addendum; no edit owed | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FA |
| 113 | R-30 | who owns a split realm | — |  | `U5d:168` | RESOLVED-BY | none owed until a contested succession executes; the Split is A-46's | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FA |
| 114 | R-33, R-34 | NPC-089's rung; `faction x` | — |  | `U5d:171` | RESOLVED-BY | none owed (statements) | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FA |
| 115 | §B6.2 item 1 | whose word ends a war | — |  | `U5d:172` | SUPERSEDED | A-20 (the seats that wage it) | — | FA |
| 116 | §B8.2 (old findings re-verified; what t… | reading account | — |  | `U5d:174` | RESOLVED-BY | no edit owed; the transfers are carried by the kit (Part 5) | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | FA |
| 117 | F-PES-FA-11 | R-16 strands the throne one death earlier | unrated in source |  | `U5d:190` · `pf1`, `pf2b` §7 | RESOLVED-BY | as R-16: lands with A-19's race | B21 (B21.03, B21.16) | FA |
| 118 | §5 item | when the royal line fails, who may take the crown | — |  | `U5d:193` | SUPERSEDED | A-19 (the deed race) | — | FA |

---

## SE — settlements and the economy

**What is wrong.** A correct, conserved, well-factored accounting kernel under a world that gives it nothing to account for (`audits/07_SE_audit.md` §0): no scarcity, no differentiation, no population dynamics. Every settlement is the same economic object (F-SE-01; 8 of 37 settlements lie in no polygon, `U5d:212`; every settlement has the same three sites, `21_PROCEDURAL_GENERATION.md` §0); population is a constant that can only fall, falls whole and invisibly (F-SE-02); the only hunger event is a world-generation artefact pinned by a test (F-SE-03); the geography feeds the battlefield and nothing else (F-SE-06); there is no settlement scenario (F-SE-13); the people of a town act as one individual (F-SE-14). The pessimist (`16_PESSIMIST_SE.md` §0) took the food from eleven of 37 towns by hand: no grain moved toward them, no one left, traded, learned of it or was blamed; the starving healed themselves by `tend` each season (F-PES-SE-01; with F-PES-GAME-06, rest cures starvation); nothing in the layer is drawn (F-PES-SE-02); a founding cannot fail (F-PES-SE-06).

**What was decided.** The world's motion is the one four-band ladder, drawn (A-54); a fixed map, an empty founded household may lapse (A-55); the common people's heavy moves (A-56, with caste in regard, vote blocks and tiers, A-41, A-42); farm work an act (D-68); famine reports once (D-69); a lord left over an empty land (D-72); hidden places (A-109).

**What is built where.** **B12a, B12b, B12c** (one SE+WR close each, D-12) carry 60 RESOLVED-BY rows: ground and granaries, the treasury granary, the population census and its rising arm, hunger that binds, the material verbs and the valley scenario, `IS-B3-SE-06`'s build in B12c; B11F1 the cohort rows (CR-106, CR-107); B22 the army's supply; B38 the cohorts' heavy moves; B39 the lean year and a founded place that can fail. **What stays open:** `07_SE_capability_rate_B` is INCOMPLETE on two blocking items (a labour verb row and its caller, `U4_TRACEABILITY.md` §3); "no domain-action mechanism exists" (G-7); the B10-16 gates entry is BLOCKED; one DISPUTED row (F-SE-15).

**Rows: 85** (RESOLVED-BY 72 · SUPERSEDED 11 · STALE/FP 1 · DISPUTED 1 · JORDAN 0).

| # | id | claim | sev | R | evidence | disposition | carrier | batch | owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | F-SE-01 | every settlement is the same economic object | B |  | `U5d:212` · `07_SE_audit.md:245` · `se_bind.py`; 8 of 37 settlements in no polygon | RESOLVED-BY | GROUND (endowment by territory, R-SE-01) as annotated by the addendum's P-1 to P-6 | B12a-c | SE+WR |
| 2 | F-SE-02 | population is a constant that can only fall, falls whole, and its loss is invisible | B |  | `U5d:213` · `07_SE_audit.md:261` · `subsist.py:72` `[not re-opened]` | RESOLVED-BY | CENSUS §4 (thinning, R-SE-04 to -06) and REGROW-B (the rising arm) | B12a-c | SE+WR |
| 3 | F-SE-13 | there is no settlement scenario to play | B |  | `U5d:224` · `07_SE_audit.md:363` · audit §9 | RESOLVED-BY | VALLEY (with the addendum's P-13 change) | B12a-c | SE+WR |
| 4 | F-PES-SE-01 | a failing place changes nothing that any person does | B |  | `U5d:291` · `16_PESSIMIST_SE.md:549` · the fail arm: eleven towns starve unseen | RESOLVED-BY | PES-SE-A edits 2, 4; COHORT (the hungry cohort's petition, migration, refusal and riot, A-56);… | B38, B12a-c | WR |
| 5 | F-PES-SE-02 | nothing in the settlement layer is drawn | B |  | `U5d:292` · `16_PESSIMIST_SE.md:565` · `18_DETERMINISM_SWEEP.md:110` corrected by OWED-SE §8 | RESOLVED-BY | DRAWS edits 1–2 as reconciled (A-54: wear, harvest and hunger on the one four-band ladder); PE… | B12a-c | SE+WR |
| 6 | F-SE-19 | the realm can raise only levy, at no cost to the place | D |  | `U5d:271` · `07_SE_audit_addendum_B.md:394` | RESOLVED-BY | SUPPLY (R-SE-33, -35); `06_FA_levy_through_the_seat_B.md` | B21, B22 | FA |
| 7 | F-SE-03 | the realm's only hunger event is a world-gen artefact, and a test pins it | D |  | `U5d:214` · `07_SE_audit.md:272` · the audit's §1.4 control table | RESOLVED-BY | GROUND (stocked larders, R-SE-02) as reconciled: the starting stock is drawn within bounds (A-… | B12a-c | SE+WR |
| 8 | F-SE-04 | relief is one act, one kind, once | D |  | `U5d:215` · `07_SE_audit.md:282` · `harness/scarce.py` | RESOLVED-BY | GROUND §4 d (the remainder walk, R-SE-11); TREAS-B (the stock at the seat rung); PES-SE-A edit… | B12a-c | SE+WR |
| 9 | F-SE-05 | the fabric's raising arm does not reach in play | D |  | `U5d:216` · `07_SE_audit.md:295` · `restore` 0 attempts, seed 0, three seasons | RESOLVED-BY | OWED-SE §1 (the reading added to H-105's and H-171's cites; cause not isolated, so no code edi… | B12a-c | SE+WR |
| 10 | F-SE-06 | the geography feeds the battlefield and nothing else | D |  | `U5d:217` · `07_SE_audit.md:311` · 55 settlement edges, 26 territory edges, an 11-row cost matrix unread | RESOLVED-BY | TREAS-B (the granary's reach is the first reader); `09_WR_B_weather_with_memory_and_the_year.m… | B12a-c | SE+WR |
| 11 | F-SE-07 | what persons do to the economy is nil in size and partly a sink | D |  | `U5d:218` · `07_SE_audit.md:327` · `default_transfer_amount=1` (`fixtures.py:625`) | RESOLVED-BY | ARCN §3 b (amount as a choice, R-SE-24); OWED-SE §2 (CR-49's class on `transfer`, `migrate`) | B12a-c | SE+WR |
| 12 | F-SE-09 | capacity acts as noise and migration as churn | D |  | `U5d:220` · `07_SE_audit.md:340` · `aperture 3 0`: 16 migrations | RESOLVED-BY | OWED-SE §2 (CR-49's class for `migrate`'s `to`); CENSUS (weight gains a writer); COHORT (`migr… | B12a-c, B38 | SE+WR |
| 13 | F-SE-10 | a store move accepts a negative, zero or fractional amount | D |  | `U5d:221` · `07_SE_audit.md:351` · `effects_shared.py:120-136` | RESOLVED-BY | KERN-SE §2 (R-SE-07) | B12a-c | SE+WR |
| 14 | F-SE-17 | the proposed granary tier has no steward | D |  | `U5d:269` · `07_SE_audit_addendum_B.md:362` | RESOLVED-BY | TREAS-B (R-SE-28) | B12a-c | SE+WR |
| 15 | F-SE-18 | every quantity has one working arm, so any binding arm is a ratchet | D |  | `U5d:270` · `07_SE_audit_addendum_B.md:378` | RESOLVED-BY | REGROW-B (R-SE-26, -27) | B12a-c | SE+WR |
| 16 | F-SE-22 | the food dependency's recorded resolution points at trade | D |  | `U5d:274` · `07_SE_audit_addendum_B.md:425` · BALANCE-005; ED-SE-0009 `[not re-opened]` | RESOLVED-BY | TREAS-B (R-SE-30) | B12a-c | SE+WR |
| 17 | F-SE-23 | the relief ladder's top is the Crown's for three duchies and not for the other two | D |  | `U5d:275` · `07_SE_audit_addendum_B.md:440` · the addendum's probe | RESOLVED-BY | OWED-SE §5 | B12a-c | SE+WR |
| 18 | F-PES-SE-03 | a shared granary feeds towns in id order | D |  | `U5d:293` · `16_PESSIMIST_SE.md:576` | RESOLVED-BY | PES-SE-A edits 1–2 | B12a-c | SE+WR |
| 19 | F-PES-SE-04 | a death by hunger is recorded as a death by nothing | D |  | `U5d:294` · `16_PESSIMIST_SE.md:586` | RESOLVED-BY | PES-SE-A edit 3 | B12a-c | SE+WR |
| 20 | F-PES-SE-05 | the shipped supply fixture, turned on, reduces every army to its crash floor | D |  | `U5d:295` · `16_PESSIMIST_SE.md:595` · `pes_supply.py` | RESOLVED-BY | TREAS-B and SUPPLY; PES-SE-B edit 4 | B12a-c, B22 | SE+WR |
| 21 | F-PES-SE-07 | the harvest is not an event; the weather runs the mines | D |  | `U5d:297` · `16_PESSIMIST_SE.md:611` | RESOLVED-BY | PES-SE-B edits 1–2 as reconciled (A-54) | B12a-c | SE+WR |
| 22 | F-PES-SE-08 | a second garrison adds nothing and a new one halves the walls | D |  | `U5d:298` · `16_PESSIMIST_SE.md:616` | RESOLVED-BY | PES-SE-B edit 3 | B12a-c | SE+WR |
| 23 | F-PES-SE-09 | two fifths of production has no use; three objects have no reader | D |  | `U5d:299` · `16_PESSIMIST_SE.md:620` | RESOLVED-BY | OWED-SE §9 (R-PES-SE-05 to -08) | B12a-c | SE+WR |
| 24 | F-PES-SE-10 | want lowers the attempt to trade | D |  | `U5d:300` · `16_PESSIMIST_SE.md:626` | RESOLVED-BY | OWED-SE §7 (owed to CHAR's formation; U5a) | B12a-c | SE+WR |
| 25 | F-SE-20 | supply has no place and no duration | D |  | `U5d:272` · `07_SE_audit_addendum_B.md:409` | RESOLVED-BY | SUPPLY (R-SE-34, -36) as constrained by R-PES-SE-14 (one ration, charged once a season) | B22 | MB |
| 26 | F-SE-14 | the people of a town act as one individual | D |  | `U5d:225` · `07_SE_audit.md:366` · 708 of 1,529 resolved acts at seed 0 are cohorts' | RESOLVED-BY | COHORT (A-56: a cohort forms only the heavy moves) | B38 | WR |
| 27 | F-SE-12 | the world never grows | D |  | `U5d:223` · `07_SE_audit.md:357` · `found` 0 of 7, `build` 0 of 4 | SUPERSEDED | A-55 (fixed map); households within settlements are founded and may lapse (LAPSE); the produce… | → B39 | WR |
| 28 | F-PES-SE-06 | a founding cannot fail, cannot found a town, and leaves a lot nobody uses | D |  | `U5d:296` · `16_PESSIMIST_SE.md:604` | RESOLVED-BY | LAPSE as reconciled (A-55: fixed map; an empty founded household may lapse) | B39 | WR |
| 29 | F-SE-08 | 248 of 322 `condition.worn` Events report a wear that did not happen | H |  | `U5d:219` · `07_SE_audit.md:337` · the audit's count | RESOLVED-BY | KERN-SE §3 (R-SE-08) | B12a-c | SE+WR |
| 30 | F-SE-11 | a move to where the mover stands publishes as travel | H |  | `U5d:222` · `07_SE_audit.md:354` · 14 of 15 executed moves same-place | RESOLVED-BY | KERN-SE §4 (R-SE-09) | B12a-c | SE+WR |
| 31 | F-SE-21 | two lanes' skill edits collide | H |  | `U5d:273` · `07_SE_audit_addendum_B.md:415` | RESOLVED-BY | RATE-B as reconciled; the home is `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`'s | B12a-c | SE+WR |
| 32 | F-SE-24 | `amount_shares` at 1000 strips below subsistence with no consequence path | H |  | `U5d:276` · `07_SE_audit_addendum_B.md:449` | RESOLVED-BY | OWED-SE §6 (R-SE-38: the flip is sequenced after CP-T08-06) | B12a-c | SE+WR |
| 33 | F-PES-SE-12 | stocking the larders at world-gen coincides with every migration stopping | H |  | `U5d:302` · `16_PESSIMIST_SE.md:640` · the pessimist's two-arm run | RESOLVED-BY | OWED-SE §10 (a gate arm on GROUND's stocking edit); the drawn start (A-50) leaves some larders… | B12a-c | SE+WR |
| 34 | F-PES-SE-13 | smaller kernel defects | H |  | `U5d:303` · `16_PESSIMIST_SE.md:647` | RESOLVED-BY | OWED-SE §9 (R-PES-SE-13) and KERN-SE | B12a-c | SE+WR |
| 35 | F-PES-SE-11 | the story instruments cannot see a place | H |  | `U5d:301` · `16_PESSIMIST_SE.md:634` | RESOLVED-BY | none owed (§0.1 pt 5); `23_STORY_D_story_census_and_gate.md` reads places | B36 | WR |
| 36 | F-SE-15 | a season's cost grew with the tick in every arm run | H |  | `U5d:226` · `07_SE_audit.md:371` · audit §3 (`[not re-measured]`) | DISPUTED | none: the audit itself marks the reading load-confounded and names no cause; this lane has no… | — (disputed) | SE |
| 37 | F-SE-16 | the instruments cannot see the economy's loops | H |  | `U5d:227` · `07_SE_audit.md:377` | RESOLVED-BY | none owed (CLAUDE.md §0.1 pt 5: no instrument over an instrument); each SE proposal's gate nam… | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | SE |
| 38 | SE-04 (b), R-SE-20 | `Rung.envelope` declared, unwritten, unread | — |  | `U5d:245` · grep `[not re-opened]` | RESOLVED-BY | plan IN-44 (delete through its Layer 1 row); OWED-SE §3 | B12a-c, B03 | SE+WR |
| 39 | H-293, S-SE-2 | what custody takes from a ruler | — |  | `U5d:239` · #453 names the travel readers only | SUPERSEDED | A-23 (custody suspends acts through the seat); `U5d_FA_owed_edits.md` §2 | → B21 | FA |
| 40 | H-105, H-171 | cite `restore` executing in the realm | — |  | `U5d:233` · F-SE-05 | RESOLVED-BY | OWED-SE §1 (R-SE-16) | B12a-c | SE+WR |
| 41 | H-140, H-306, H-327 | same-place move; amounts; arrival teaches nothing | — |  | `U5d:234` | RESOLVED-BY | KERN-SE §4, §2, §5 | B12a-c | SE+WR |
| 42 | H-166 | who holds an unheld place | — |  | `U5d:236` · `effects_founding.py:51-89,170` | RESOLVED-BY | `09_WR_world_motion.md` edit 2 as reconciled (unheld land is taken by occupation; ground no pa… | B12a-c | SE+WR |
| 43 | H-236 | the lattice has no source (filed under SE by path) | — |  | `U5d:237` · T15 holds no Site | SUPERSEDED | WR's (Part 3: `09_WR_world_motion.md` edit 1; A-40 makes the wear a real condition of places) | → B12a-c | SE+WR |
| 44 | H-241 | `field_provisioning` built, shipped off | — |  | `U5d:238` · `fixtures.py:809` | RESOLVED-BY | SUPPLY; PES-SE-B edit 4 (the flip's load-time refusal); OWED-SE §4 (R-SE-22) | B22, B12a-c | MB |
| 45 | H-303 | a partly stocked rung blocks the walk | — |  | `U5d:240` | RESOLVED-BY | GROUND §4 d (R-SE-11) | B12a-c | SE+WR |
| 46 | H-305 | hunger's loss scales with headcount | — |  | `U5d:241` · `subsist.py:72` | RESOLVED-BY | CENSUS §4 a (R-SE-04) | B12a-c | SE+WR |
| 47 | H-309 | a seat holder who migrates keeps the seat | — |  | `U5d:242` | RESOLVED-BY | OWED-SE §1 (close the row, R-SE-17); the addendum's P-16 stands | B12a-c | SE+WR |
| 48 | H-304, H-307, H-168 | `tend` restores whole (PC's); over capacity at build; `migrate` only hand-built (now false) | — |  | `U5d:243` · `aperture 3 0` | RESOLVED-BY | PES-SE-A edit 4 (owed to PC, U5b); folded into F-SE-09; OWED-SE §1 (R-SE-18) | B12a-c | SE+WR |
| 49 | CR-40, CP-T08-01, -03, -04 to -08, -10,… | planned, unbuilt | — |  | `U5d:244` | RESOLVED-BY | the plan positions as amended by R-SE-01 to -05 and -19 (GROUND, CENSUS, OWED-SE §2) | B12a-c | SE+WR |
| 50 | `HANDOFF_SE` Open row 1 | waits on a closed ED | — |  | `U5d:246` · AM-E-15 | RESOLVED-BY | KERN-SE §6 (R-SE-13) | B12a-c | SE+WR |
| 51 | R-SE-01, -02, -03, -11 | endowment; stocking; the gate; the walk | — |  | `U5d:247` | RESOLVED-BY | GROUND | B12a-c | SE+WR |
| 52 | R-SE-04, -05, -06 | per-head loss; thinning; `empty` band | — |  | `U5d:248` | RESOLVED-BY | CENSUS | B12a-c | SE+WR |
| 53 | R-SE-07 to -10, -12 to -15 | kernel repairs and stale pointers | — |  | `U5d:249` | RESOLVED-BY | KERN-SE §2–§6 | B12a-c | SE+WR |
| 54 | R-SE-16, -17, -18 | register edits | — |  | `U5d:250` | RESOLVED-BY | OWED-SE §1 | B12a-c | SE+WR |
| 55 | R-SE-19 | `transfer`'s `to` binds the question's referent | — |  | `U5d:251` | RESOLVED-BY | OWED-SE §2 | B12a-c | SE+WR |
| 56 | R-SE-22 | the ration is a `min` over every eaten kind | — |  | `U5d:253` | RESOLVED-BY | OWED-SE §4 | B12a-c | SE+WR |
| 57 | R-SE-23, -24 | case worlds hold no eater; every store move is 1 unit | — |  | `U5d:254` | RESOLVED-BY | ARCN §3 a, b | B12a-c | SE+WR |
| 58 | R-SE-25 | no settlement verb reads a skill | — |  | `U5d:255` · H-164 | SUPERSEDED | by R-SE-32 (RATE-B) | → B12a-c | SE+WR |
| 59 | S-SE-1 | may a population recover | — |  | `U5d:256` · ED-SE-0051 `[ledger row not re-opened]` | SUPERSEDED | the register's ladder table ("Yes, bounded by food and room", the 2026-09-17 ruling) and the a… | → B12a-c | SE+WR |
| 60 | §13 NPC-083, NPC-037, NPC-013 | shortfall against orders; treasury post; the tithe | — |  | `U5d:257` · `corpus_run.build_at` seats no eater | RESOLVED-BY | ARCN §3 a, b; plan CP-T08-06, -07 | B12a-c | SE+WR |
| 61 | §13 NPC-090, ARC-20 | treaty trade; a trade dependency | — |  | `U5d:259` · `exchange` 0 of 79 | RESOLVED-BY | ARCN §3 c; GROUND; TREAS-B (R-SE-30: the gate is a person's store move across two duchies) | B12a-c | SE+WR |
| 62 | §14 (skill surface) | (c) and (e) superseded | — |  | `U5d:262` | SUPERSEDED | the addendum §6; RATE-B | → B12a-c | SE+WR |
| 63 | C-1 to C-8 | corrections to the first audit | — |  | `U5d:268` | RESOLVED-BY | made in the addendum; carried by TREAS-B (C-2, C-3), REGROW-B (C-1, C-8), RATE-B (C-5) | B12a-c | SE+WR |
| 64 | §2.4 ARC-37/39, NPC-007, EMG-11, NPC-08… | cases the first audit did not list | — |  | `U5d:278` | RESOLVED-BY | GROUND and OWED-SE §2 for SE's half; FA, FI, WR, CHAR own the rest (CR-107b; COHORT for ARC-14… | B12a-c, B38 | SE+WR |
| 65 | P-1 to P-16 | decisions on the first lane's placeholders | — |  | `U5d:279` | RESOLVED-BY | as the addendum's table: P-7 superseded by TREAS-B, P-10 by REGROW-B, P-14 by RATE-B; the rest… | B12a-c | SE+WR |
| 66 | R-SE-26, -27 | recovery; flight is an act | — |  | `U5d:280` | RESOLVED-BY | REGROW-B | B12a-c | SE+WR |
| 67 | R-SE-28, -29, -30 | where relief sits; relief is the rule; the trade channel | — |  | `U5d:281` · ED-IN-0255 `[not re-opened]` | RESOLVED-BY | TREAS-B | B12a-c | SE+WR |
| 68 | R-SE-31, -37, -38 | endowment annotations; `ration` is no verb; when `amount_shares` flips | — |  | `U5d:282` | RESOLVED-BY | OWED-SE §6 (notes for the builder of GROUND and ARCN) | B12a-c | SE+WR |
| 69 | R-SE-32 | the skill rate against the other surfaces | — |  | `U5d:283` | RESOLVED-BY | RATE-B | B12a-c | SE+WR |
| 70 | §6 "stewardship: no passive bonus from… | declined by the addendum | — |  | `U5d:285` | SUPERSEDED | A-54 (a steward's skill bears on the harvest draw) and A-12 (a seat may carry a modifier); RAT… | → B12a-c | SE+WR |
| 71 | R-PES-SE-01 to -04 | sharing; the crossing; causes; `tend` and hunger | — |  | `U5d:304` | RESOLVED-BY | PES-SE-A edits 1–4 | B12a-c | SE+WR |
| 72 | R-PES-SE-05, -07, -08, -09, -13 | ore's reader; hunger bands; `coin`; trade kinds; Site-kind names | — |  | `U5d:305` | RESOLVED-BY | OWED-SE §7, §9 | B12a-c | SE+WR |
| 73 | R-PES-SE-06, -10, -11, -12 | `Rung.yield`'s reader; grown kinds; walls; the flip | — |  | `U5d:306` | RESOLVED-BY | PES-SE-B edits 2, 1, 3, 4 | B12a-c | SE+WR |
| 74 | J-1 | does a chronic dearth speak | — |  | `U5d:308` · H-160 limit 3 | SUPERSEDED | the ladder table's D-69 (A: famine reports once; the never-stocked edge repaired); PES-SE-A ed… | → B12a-c | SE+WR |
| 75 | §5 lists; §6.3 owed | false N-lines; failed premises; items owed to other lanes | — |  | `U5d:311` | RESOLVED-BY | OWED-SE §8–§10; PC's `tend` is U5b's | B12a-c | SE+WR |
| 76 | R-SE-21 | a cohort's weight is 2 everywhere | — |  | `U5d:252` · H-170 | RESOLVED-BY | plan CR-107 (authored rows); the generated cast (A-44) authors cohorts with weights, `21_PROCE… | B39, B11F1 | WR |
| 77 | §13 ARC-46, ARC-07 | a depletable resource; a standing drain | — |  | `U5d:260` | RESOLVED-BY | SUPPLY (R-SE-34) | B22 | MB |
| 78 | R-SE-33 to -36 | hands under arms; the standing ration; training; the occupier | — |  | `U5d:284` | RESOLVED-BY | SUPPLY | B22 | MB |
| 79 | R-PES-SE-14 | one ration on two clocks | — |  | `U5d:307` | RESOLVED-BY | SUPPLY (a constraint on R-SE-34) | B22 | MB |
| 80 | H-149, CP-T08-09 | ruled and enforced; withdrawn | — |  | `U5d:235` · `test_march.py` | STALE/FP | none owed | — (stale) | SE |
| 81 | §13 NPC-083 (methods), ARC-44/ARC-01 (d… | "wrongly stated" | — |  | `U5d:258` · `rosters.yaml:79-80` | RESOLVED-BY | restated by the audit (the tier-4 redesign's; claim decay on a cohort's reasons); no SE edit | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | SE |
| 82 | §13 ARC-12, EMG-C3, NPC-001, NPC-003, N… | owned by FI, WR, FA | — |  | `U5d:261` | SUPERSEDED | the owning closures (U5c; Parts 1 and 3 here) | — | SE |
| 83 | §2.3 (twelve `.audit/` findings re-veri… | true, false now, moved, irrelevant | — |  | `U5d:277` · the addendum's table | RESOLVED-BY | none owed beyond the rows above (G-33 and G-04 false now; the stress-sim mechanics irrelevant,… | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | SE |
| 84 | J-2 | how does the world's own motion draw | — |  | `U5d:309` | SUPERSEDED | A-54 (the one four-band ladder) | — | SE |
| 85 | J-3 | may a place begin, and may a begun place end | — |  | `U5d:310` · SE-9(a) | SUPERSEDED | A-55 | — | SE |

---

## WR — the world's motion, stories and threadwork

**What is wrong.** A sound causal substrate and not yet a source of narrative (`audits/09_WR_audit.md` §0): seasons tick scene by scene, every Event carries its causes, nothing is triggered; but six seasons at seeds 0 and 1 produce no ending and one death (F-WR-01); strands collapse into one (F-WR-02); the story bar cannot fail (F-WR-03); the world's own motion ships off (F-WR-04); threadwork is not in the game and is not a module (F-WR-05); the realm closes by clock, not by act (F-WR-13); the chronicle prints who and when, never what (F-WR-14). The pessimist (`16_PESSIMIST_WR.md` §0): clocks that keep time for nobody; idle for 41 seasons the realm is one ramp in 37 identical places, its first noticeable Event at season 20; no story in computed play has a turn (F-PES-WR-01). Eras and regimes (`30_*` §0): the engine has strife and calls its realm-wide scope an era, with no era, no regime beyond a credit factor, no momentum that is a person's.

**What was decided.** The Thread wears places down, one site per territory (A-40); arcs end when a threshold opens a scene, never decides it (A-47); strands several and each able to end (A-45); eras, regimes and the houses' stances (A-82 to A-91, `_part2` §4.5, §4.6); A-92's lean (`L1-A92`); reveal only after the line ends (A-49); world cards draw bounded starting state (A-50); five years of prologue (A-51).

**What is built where.** B03 makes threadwork a module (edit 3); B12a-c the world's motion and the draws (33 RESOLVED-BY rows); B35 the Thread (the `Person.coherence` writer first); **B36** the story instruments that can fail (18 rows); B37p kin and life; B38 the eras, regimes, strands and the stances; B39 generation. **What stays open:** the strife master's five sentences (held, A-84); `30_WR_G` commit 1 does not build as written (P-31-5); the cast's opinion values (content).

**Rows: 83** (RESOLVED-BY 71 · SUPERSEDED 9 · STALE/FP 3 · DISPUTED 0 · JORDAN 0).

| # | id | claim | sev | R | evidence | disposition | carrier | batch | owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | F-WR-01 | no story in the shipped realm escalates or ends | B | R-01 | `U5d:330` · `09_WR_audit.md:130` · six seasons, seed 0: one strand of 234 moves; 0 deaths | RESOLVED-BY | INSTR edit 4 (the reading); the closing acts are other lanes' (PC's duel, SC's `determine`, FA… | B36 | WR |
| 2 | F-PES-WR-01 | no story in computed play has a turn | B | R-01 | `U5d:409` · `16_PESSIMIST_WR.md:445` | RESOLVED-BY | PES-WR-D edit 4 (the reading); the closing verbs are FA's, SC's and PC's | B36 | WR |
| 3 | F-WR-05 | threadwork is not in the game and is not a module | B | R-05 | `U5d:334` · `09_WR_audit.md:276` · `(Person, coherence)` unproduced, `write_matrix.yaml:200-206` (opened) | RESOLVED-BY | THREAD edit 3 (tables as typed data) and THREAD-B edits 1–4 (which supersede THREAD edits 1, 2… | B03, B35 | IN |
| 4 | F-WR-02 | a strand's conclusion does not discriminate; strands collapse into one | D | R-02 | `U5d:331` · `09_WR_audit.md:167` · E-08 | RESOLVED-BY | STRAND edits 1–3 as reconciled (A-45: several strands that can each end; edit 3 is now the rul… | B12a-c | SE+WR |
| 5 | F-PES-WR-02 | the Calamity has no source, no break and no answer | D | R-02 | `U5d:410` · `16_PESSIMIST_WR.md:461` | RESOLVED-BY | PES-WR-B edits 1–3 as reconciled (A-40: the wear is a real condition of places, one Site per t… | B12a-c | SE+WR |
| 6 | F-PES-WR-03 | the world's own change is one ramp in 37 places | D | R-03 | `U5d:411` · `16_PESSIMIST_WR.md:488` | SUPERSEDED | F-SE-01 (Part 2: GROUND) and F-PES-GAME-05 (Part 6) own it | → B12a-c | SE+WR |
| 7 | F-WR-03 | the story bar cannot fail, has no forcing arm, and one control is inverted | D | R-03 | `U5d:332` · `09_WR_audit.md:204` · `harness/storybar.py` `[not re-opened]` | RESOLVED-BY | INSTR edits 1–3 (R-01, R-02, R-18; plan CR-99 folded into edit 1) | B36, B11F2 | WR |
| 8 | F-WR-04 | the world's own motion ships off; the world's readings have no reader | D | R-04 | `U5d:333` · `09_WR_audit.md:244` · fixtures at 0 | RESOLVED-BY | MOTION edit 1; WEATHER-B edits 1–2 and DRAWS edits 1–2 as reconciled (A-54: one four-band ladd… | B12a-c | SE+WR |
| 9 | F-PES-WR-04 | CALENDAR can be removed and no reading notices | D | R-04 | `U5d:412` · `16_PESSIMIST_WR.md:524` · the cut arm | RESOLVED-BY | PES-WR-D edits 3, 5 (R-1) | B36 | WR |
| 10 | F-PES-WR-05 | the Thread is read off letters, finds nothing and costs nothing | D | R-05 | `U5d:413` · `16_PESSIMIST_WR.md:495` | RESOLVED-BY | PES-WR-D edit 2 (`referent_class: Site`); THREAD-B | B35, B36 | WR |
| 11 | F-WR-06 | the victory ending is unreachable on one territory; its register row is stale | D | R-06 | `U5d:335` · `09_WR_audit.md:303` · GD-1 | RESOLVED-BY | MOTION edit 3 (settled territories), reached by a draw (DRAWS edit 3) | B12a-c | SE+WR |
| 12 | F-PES-WR-06 | a journey is free, instant and certain | D | R-06 | `U5d:414` · `16_PESSIMIST_WR.md:506` | RESOLVED-BY | PES-WR-A | B12a-c | SE+WR |
| 13 | F-PES-WR-07 | the bodies clock is a coin, the same coin for everyone | D | R-07, R-09 | `U5d:415` · `16_PESSIMIST_WR.md:513` · `fixtures.py:692` | RESOLVED-BY | PES-WR-C as reconciled (A-15: no longer dark once the ages are authored); `22_HAPPENINGS_A` ow… | B37 | IN |
| 14 | F-WR-07 | the flow stamp's reach hangs on one Event kind | D | R-07 | `U5d:336` · `09_WR_audit.md:325` · dose 0 to 28% by seed | RESOLVED-BY | none of its own (the stamp is correct; its inputs are rare): it reads again once F-WR-01's clo… | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | WR |
| 15 | F-PES-WR-08 | every run is the same run | D | R-08 | `U5d:416` · `16_PESSIMIST_WR.md:530` | RESOLVED-BY | none of its own (the sum of F-WR-01 and the world's motion being off); the seeded start (A-50)… | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | WR |
| 16 | F-WR-09 | memory decay is half the log and grows | D | R-09 | `U5d:338` · `09_WR_audit.md:367` · 179,056 `claim.decayed` (E-08) | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` (U5a's; the ladder's D-48: forgetting computed when read) | B09 | IN |
| 17 | F-WR-24 | wear, strain, the hungry body, a lapse, endings and a strand's conclusion are fixed functions of state | D | R-09 | `U5d:390` · `09_WR_audit_addendum_B.md:91` | RESOLVED-BY | DRAWS edits 1–4 (R-37 to R-40), confirmed in form by A-54 and A-24 | B12a-c | SE+WR |
| 18 | F-WR-19 | the scheduled weather has no memory, no neighbours and a mean of 1.167 | D |  | `U5d:385` · `09_WR_audit_addendum_B.md:86` | RESOLVED-BY | WEATHER-B edits 1–2 as reconciled (A-54) | B12a-c | SE+WR |
| 19 | F-WR-20 | the second contest (the world's survival) has no reading and no ending | D |  | `U5d:386` · `09_WR_audit_addendum_B.md:87` | RESOLVED-BY | WEATHER-B edit 4; DRAWS edit 3 | B12a-c | SE+WR |
| 20 | F-PES-WR-11 | the band-crossing channel is dead from end to end | D |  | `U5d:419` · `16_PESSIMIST_WR.md:475` | RESOLVED-BY | PES-WR-B edit 4 | B12a-c | SE+WR |
| 21 | F-WR-17 | threadwork's designed session has no code and no plan position | D |  | `U5d:383` · `09_WR_audit_addendum_B.md:84` | RESOLVED-BY | THREAD-B edits 1–2 | B35 | WR |
| 22 | F-WR-13 | the realm closes by clock, not by act (23 lapsed against 3 determined) | D |  | `U5d:379` · `09_WR_audit_addendum_B.md:80` · three seeds, six seasons | RESOLVED-BY | READ-B edit 1 (R-29); the acts that close are other lanes' | B36 | WR |
| 23 | F-WR-14 | the chronicle prints who and when, never what, from no viewpoint | D |  | `U5d:380` · `09_WR_audit_addendum_B.md:81` · `world_q.py:4374-4441` | RESOLVED-BY | CHRON-B (R-28, R-32) as reconciled (A-49, A-33, A-43) | B36 | WR |
| 24 | F-WR-15 | no reading of open situations, tension or idle persons | D |  | `U5d:381` · `09_WR_audit_addendum_B.md:82` | RESOLVED-BY | READ-B | B36 | WR |
| 25 | F-WR-16 | flattening every person to the realm mean lowers no story reading | D |  | `U5d:382` · `09_WR_audit_addendum_B.md:83` · EB-01 | RESOLVED-BY | READ-B (the ablation kept as a reading); the fix is CHAR's (H-283, U5a) | B36 | WR |
| 26 | F-WR-08 | `ENDINGS_CLASSIFIED.yaml` is prose read by a builder | H | R-08 | `U5d:337` · `09_WR_audit.md:348` · `corpus_run.py:656-660` | RESOLVED-BY | ARCS-WR edit 3 (stop planting; correct the path) | B12a-c | SE+WR |
| 27 | F-PES-WR-09 | a Date due in the past never fires | H | R-09 | `U5d:417` · `16_PESSIMIST_WR.md:543` | RESOLVED-BY | PES-WR-D edit 1 (R-9) | B36 | WR |
| 28 | F-WR-12 | currency rows point at retired documents | H |  | `U5d:341` · `09_WR_audit.md:399` · `CURRENT.md:36, :28` `[not re-opened]` | RESOLVED-BY | PTR-B (text for the orchestrator: R-11, R-12, R-20) | B03 | IN |
| 29 | F-WR-22 | three hole rows rest on deaths that no longer occur at their seed | H |  | `U5d:388` · `09_WR_audit_addendum_B.md:89` | RESOLVED-BY | PTR-B (R-31) | B03 | IN |
| 30 | F-WR-10 | every cohort starves in season 0 and never again | H |  | `U5d:339` · `09_WR_audit.md:385` · `body.changed` 37 in season 0 | RESOLVED-BY | plan CR-22 with `07_SE_ground_and_granaries.md` as reconciled (the drawn start, A-50) | B12a-c | SE+WR |
| 31 | F-WR-11 | MATTER recovery is silent (H-211) | H |  | `U5d:340` · `09_WR_audit.md:393` · `matter.py:119, :690-711` | RESOLVED-BY | ARCS-WR edit 2 (the signed step) with OWED-WR §3 (F-WR-23's body Observation lands with it) | B12a-c | SE+WR |
| 32 | F-WR-21 | 248 of 322 `condition.worn` Events are writes of zero | H |  | `U5d:387` · `09_WR_audit_addendum_B.md:88` · EB-07 | RESOLVED-BY | READ-B edit 2 (R-30); `07_SE_kernel_repairs.md` §3 removes the write | B12a-c, B36 | SE+WR |
| 33 | F-WR-23 | a believed wound is never cleared | H |  | `U5d:389` · `09_WR_audit_addendum_B.md:90` · `world_q.py:3806-3812` | RESOLVED-BY | OWED-WR §3 (a body Observation on `tend` and on recovery; owed at PC's and CHAR's owner, seque… | B12a-c, B37p | SE+WR |
| 34 | F-WR-18 | the first lane's scenario shows the practitioner his own Coherence band | H |  | `U5d:384` · `09_WR_audit_addendum_B.md:85` · `data/requires.py:809` | RESOLVED-BY | THREAD-B edit 3 (R-25); UNKNOWABLE (A-43, for what others read of him) | B35 | WR |
| 35 | F-PES-WR-10 | "pressure" never fires | H |  | `U5d:418` · `16_PESSIMIST_WR.md:537` | RESOLVED-BY | PES-WR-D edit 1 | B36 | WR |
| 36 | §6.1 rows closed at HEAD (H-04, -05, -2… | listed open or unsure; verified closed | — |  | `U5d:342` · the audit's E-07, E-08, E-15 | STALE/FP | PTR-B carries the re-grade text for H-05, -27, -172 | — (stale) | IN |
| 37 | R-08, R-09 | the module; its tables | — |  | `U5d:355` | RESOLVED-BY | THREAD-B; THREAD edit 3 | B03, B35 | IN |
| 38 | R-11, R-12, R-20 | pointer text | — |  | `U5d:357` | RESOLVED-BY | PTR-B | B03 | IN |
| 39 | §2.2 corrections 1–11 | corrections to the first audit and to this addendum | — |  | `U5d:391` | RESOLVED-BY | made in place; THREAD-B supersedes THREAD edits 1, 2, 4; CHRON-B carries 8; R-25 carries 9 | B03, B36, B35 | IN |
| 40 | R-31 | re-point three rows | — |  | `U5d:397` | RESOLVED-BY | PTR-B | B03 | IN |
| 41 | §6: 19 rows closed at HEAD | H-04, -05, -27, -34, -40, -51, -95, -103, -107, -110, -118, -129, -172, -242, -243, -245, -246, -247, -3… | — |  | `U5d:400` · the addendum's table | STALE/FP | PTR-B for the rows whose text is owed | — (stale) | IN |
| 42 | §6: 4 rows whose measurement is stale | H-168, -209, -225, -230 | — |  | `U5d:402` | RESOLVED-BY | PTR-B (re-pointed); `U5d_SE_owed_edits.md` §1 for H-168 | B12a-c, B03 | SE+WR |
| 43 | R-14 | claim decay | — |  | `U5d:359` | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` | B09 | IN |
| 44 | §6: 6 rows open in this lane | H-102, -125, -135, -159, -164, -208 | — |  | `U5d:401` | RESOLVED-BY | READ-B (H-135's reading); CR-22 (H-125); TERMS-B (H-159); A-15 (H-208); H-102 and H-164 stay o… | B21, B36, B09, B12a-c | FA |
| 45 | H-102, H-125, H-159, H-232 | open as a sign, a value, a value, a refusal | — |  | `U5d:344` · E-05, E-08 | RESOLVED-BY | none owed by WR: H-125 is re-derived by CR-22; H-159 is FA's term (Part 1, TERMS-B); H-232 is… | B21, B12a-c | FA |
| 46 | H-176, H-186, H-235, H-236 | endings; insurgency; the lattice | — |  | `U5d:345` · E-13 | RESOLVED-BY | MOTION edits 3, 2, 1 | B12a-c | SE+WR |
| 47 | H-211 | a body only falls | — |  | `U5d:347` | RESOLVED-BY | ARCS-WR edit 2; plan CP-T10-04 | B12a-c, B37p | SE+WR |
| 48 | H-257, R-06 | a real execution reads KL, not XE | — |  | `U5d:349` | RESOLVED-BY | OWED-WR §1 (`strife.py:85`) | B12a-c | SE+WR |
| 49 | R-03, R-04, R-05 | lattice source; victory selector; unheld land | — |  | `U5d:353` | RESOLVED-BY | MOTION edits 1, 3, 2 (edit 2 stands under A-57/A-58: ground no party holds is outside the rule) | B12a-c | SE+WR |
| 50 | R-07 | a strand concludes on an opening kind | — |  | `U5d:354` | RESOLVED-BY | STRAND edits 1–2 | B12a-c | SE+WR |
| 51 | R-13 | a body only falls | — |  | `U5d:358` | RESOLVED-BY | ARCS-WR edit 2 | B12a-c | SE+WR |
| 52 | R-15, R-16 | the planted column; automatic clocks | — |  | `U5d:360` | RESOLVED-BY | ARCS-WR edits 3, 1, 4 as reconciled (A-47: the count opens a mandatory scene) | B12a-c | SE+WR |
| 53 | §13 ambient decay, bands, the lattice (… | in kind; needs a source | — |  | `U5d:363` · E-07, E-16 | RESOLVED-BY | MOTION edit 1; PES-WR-B | B12a-c | SE+WR |
| 54 | §13 private counters (ARC-34, -47, -31,… | a counter forces a step | — |  | `U5d:365` · `world_q.py:162-168` | RESOLVED-BY | ARCS-WR edit 1 as reconciled (A-47) | B12a-c | SE+WR |
| 55 | §13 "wrongly stated" (ARC-47/NSC-08 nev… | restated | — |  | `U5d:366` | RESOLVED-BY | ARCS-WR edit 4; A-47 keeps the restatement's core (the crossing decides nothing) and adds that… | B12a-c | SE+WR |
| 56 | §13 SCN-06, SCN-LOOP-C | drains and restorations summed | — |  | `U5d:370` · H-211 | RESOLVED-BY | ARCS-WR edit 2 | B12a-c | SE+WR |
| 57 | §13 the 19 `forced_by_threshold` cases | misrepresented by a planted holderless date | — |  | `U5d:372` · `corpus_run.py:656-660` | RESOLVED-BY | ARCS-WR edit 3; A-47 | B12a-c | SE+WR |
| 58 | R-23, R-26, R-27 | a leg's price; the Rupture's selector; a spell | — |  | `U5d:393` | RESOLVED-BY | WEATHER-B edits 3, 4, 1–2 | B12a-c | SE+WR |
| 59 | R-37, R-38, R-39 | wear drawn; endings drawn; a strand concludes on a drawn degree | — |  | `U5d:399` | RESOLVED-BY | DRAWS edits 1, 3, 4 | B12a-c | SE+WR |
| 60 | R-1 to R-12 | resolutions | — |  | `U5d:420` | RESOLVED-BY | PES-WR-A (R-5, R-6), -B (R-2, R-3), -C (R-7, R-8), -D (R-1, R-9 to R-12); R-4 is text for the… | B12a-c | SE+WR |
| 61 | §8 (items listed for other lanes) | illness not yet graded; the lattice flip a fixed-function collapse | — |  | `U5d:422` | RESOLVED-BY | PES-WR-C; PES-WR-B edits 1–2 before MOTION edit 1's flip | B12a-c, B37 | SE+WR |
| 62 | §11 item 3 | the slate | — |  | `U5d:362` · H-54 | SUPERSEDED | A-48 (a list of questions for the player; NPCs take the first); `11_GO_player_surface_contract… | → B34 | GO |
| 63 | §13 institutional clocks (ARC-46, -50,… | standing rises by itself | — |  | `U5d:367` | RESOLVED-BY | plan CR-89 (FA; Part 1) | B21d | FA |
| 64 | H-208, §11 item 2 | natural death deferred | — |  | `U5d:346` · ED-IN-0317 `[not re-opened]` | SUPERSEDED | A-15 (on, after the ages are authored); carrier `22_HAPPENINGS_A_a_death_is_rare_caused_and_dr… | → B37 | IN |
| 65 | B10-15, B10-18, CL-THRUST, CL-OPEN, CR-… | plan positions | — |  | `U5d:351` | RESOLVED-BY | the plan, with THREAD-B before CP-T07-02 (R-08) and CR-99 folded into INSTR edit 1 | B36, B35, B11F2 | WR |
| 66 | §13 threadwork cases (ARC-48, -05, -41,… | no working exists | — |  | `U5d:364` · `write_matrix.yaml:206` | RESOLVED-BY | THREAD-B; plan B10-15 (CP-T07-02 to -10); ARC-51's growth is CHAR's | B35 | WR |
| 67 | R-21, R-22, R-25, R-34, R-40 | host declaration; cost by direction; coherence world-only for its owner; a Partial's scope; contact, cos… | — |  | `U5d:392` | RESOLVED-BY | THREAD-B edits 1–3 | B35 | WR |
| 68 | R-01, R-02, R-18 | story bar | — |  | `U5d:352` | RESOLVED-BY | INSTR edits 1–3 | B36 | WR |
| 69 | R-28, R-32 | what a line is about; the journal's source | — |  | `U5d:395` | RESOLVED-BY | CHRON-B | B36 | WR |
| 70 | R-29, R-30 | closed by act or by clock; non-zero changes only | — |  | `U5d:396` | RESOLVED-BY | READ-B edits 1–2 | B36 | WR |
| 71 | §6.1 rows "not WR's" (H-32, -65, -107,… | another lane's mechanism | — |  | `U5d:343` | SUPERSEDED | the owning closures (U5a, U5b, U5c; Parts 1 and 2 here); the addendum's §6 re-reads each (3.2… | — | WR |
| 72 | H-238 | no corpus thread sensitivity | — |  | `U5d:348` · E-15 | RESOLVED-BY | none owed (answered at ladder step 1 by the row itself) | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | WR |
| 73 | H-274 | the stamp | — |  | `U5d:350` | RESOLVED-BY | as F-WR-07 | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | WR |
| 74 | R-10, R-17, R-19 | the empty thrust ladder; sixteen links read 0; live tenures at a move's tick | — |  | `U5d:356` | RESOLVED-BY | none owed (statements recorded in the audit; no code) | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | WR |
| 75 | §11 item 1 | the same-doer link | — |  | `U5d:361` · ED-IN-0316 | SUPERSEDED | A-45 (several strands) | — | WR |
| 76 | §13 ARC-02 | a state-change check with no actor | — |  | `U5d:368` | SUPERSEDED | A-15 | — | WR |
| 77 | §13 ARC-53, SCN-07, ARC-23 | represented today | — |  | `U5d:369` · `tend` 37/69 (E-07) | STALE/FP | none owed | — (stale) | WR |
| 78 | §13 ARC-07, NPC-052, ARC-01, ARC-44 | other lanes' | — |  | `U5d:371` | SUPERSEDED | U5b; Parts 1 and 2 | — | WR |
| 79 | §14 (skill surface; "banded scalar") | asked CHAR for a row kind | — |  | `U5d:373` | SUPERSEDED | the addendum's R-24 (none needed) | — | WR |
| 80 | R-24, R-33, R-35 | no "banded scalar"; no navigation skill; no Approach Training gate | — |  | `U5d:394` | RESOLVED-BY | none owed (A-11 confirms: training gates nothing; Thread Sensitivity is the one gate) | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | WR |
| 81 | R-36 | the Rendering Crisis's four beats | — |  | `U5d:398` | RESOLVED-BY | none owed (the Event alone; the journal tells) | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | WR |
| 82 | §6: 20 rows another lane's | read and left | — |  | `U5d:403` | SUPERSEDED | the owning closures | — | WR |
| 83 | §5, §6, §7 lists | false N-lines; premises; stories | — |  | `U5d:421` | RESOLVED-BY | none owed beyond the rows above | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | WR |

---

## DICE — the resolution substrate

**What is wrong.** The best-owned code in the tree, fed a constant (`audits/10_DICE_audit.md` §0): the face rule, the margin ladder and the exact odds each have one owner and the odds stated are the odds dealt (Failure 70.4 % dealt against 74.0 % exact at the pair 265 of 284 rolls used), but 564 of 568 graded rolls are at pool 2 with leverage 0.0 (F-DICE-01); the default outcome is nothing and the top band cannot occur (F-DICE-02); holding a score makes a person easier to oppose (F-DICE-03); two samplers sit half a success apart (F-DICE-05); one score feeds three pools (F-DICE-17); a field battle reads no person (F-DICE-18). The pessimist (`16_PESSIMIST_DICE.md` §0): the dice are sound and decide almost nothing; in 282 of 284 graded rolls no state changes (F-PES-DICE-01); at the shipped pair "everything draws" means "little happens" (F-PES-DICE-02). The one opposed rule (`29_ONE_OPPOSED_RULE.md` §0): one rule serves fight and argument and meets Jordan's three goals at once.

**What was decided.** The bell curve everywhere (A-5), score plus a base (A-6), two inputs (A-7), a wound a level (A-8), declared floats (A-29), one draw per key (A-30), the one opposed rule (A-26, A-71, A-79); luck in battle by named draws (A-59, A-77; D-34, the one JORDAN row here).

**What is built where.** B04 the skill home (10 RESOLVED-BY rows); **B05** the one roll (34 rows: one roller, one score, the obstacle composer, the believed odds' prior, `29_DICE_one_opposed_rule_form_and_tuning`, the `degree_from_net` docstring); B06 the keyed draw and the float contract (GO's carriers); B07 the task draw. **What stays open:** the joint calibration (`_part2` §5.1); the proposals built on whole dice are rewritten (A-5's consequence), and the SC tuning tables recomputed in B05.

**Rows: 77** (RESOLVED-BY 49 · SUPERSEDED 24 · STALE/FP 3 · DISPUTED 0 · JORDAN 1).

| # | id | claim | sev | R | evidence | disposition | carrier | batch | owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | C-5, F-DICE-17 | one score, three pools | B | R-06, R-09 | `U5a:572` · `10_DICE_audit_addendum_B.md:169` · E-B03: equals succeed 28 % in the social roll, 63–68 % in the other two | SUPERSEDED | by A-6: one pool rule, `max(pool_floor, score + addends + pool_add)`, at every site (U1 archit… | → B04 | IN |
| 2 | F-PES-DICE-01 | the degree changes no state (282 of 284 rolls) | B | R-09 | `U5a:633` · `16_PESSIMIST_DICE.md:423` · E-P6 | SUPERSEDED | the verb lanes' closures (seven rows that write nothing in any band: SC, FI, verbs SOCIAL; U5c… | — | IN |
| 3 | F-DICE-01 | the engine is fed a constant: every social roll is two dice, no leverage | B |  | `U5a:549` · `10_DICE_audit.md:139` · 568 graded rolls: 564 at pool 2, leverage 0.0 on all | RESOLVED-BY | U1 architecture §4–§6; CAP Part B (the roll's two inputs) and Part C (cast content, the attrib… | B05, B04 | IN |
| 4 | C-7, F-DICE-18 | a field battle reads no person | B |  | `U5a:574` · `10_DICE_audit_addendum_B.md:224` · E-B04: `MassBattleInput` byte-equal | RESOLVED-BY | MAP §D (the `field` site declared with no rows); the first rows are MB's (U5b); the form of fo… | B04 | IN |
| 5 | F-DICE-14 | the chooser's odds answer for one verb, and "cannot say" reads as certain | D |  | `U5a:562` · `10_DICE_audit.md:252` · E-19: 102 figures of 4,929 queries | RESOLVED-BY | `10_DICE_believed_odds_have_a_prior.md` Edits A–B; the fight's and field's believed estimate (… | B05, B04 | IN |
| 6 | C-1, F-DICE-15 | three obstacle axioms for one ruling; the field is an opposed roll | D |  | `U5a:568` · `10_DICE_audit_addendum_B.md:119` · `orchestration.py:1308-1309` | RESOLVED-BY | MAP §A ("the contest form", `static` or `opposed_roll`) and §G edit 9; the floor reads `OB_MIN… | B05, B04 | IN |
| 7 | F-DICE-20 | derived resources exist for one scene of one subsystem | D |  | `U5a:577` · `10_DICE_audit_addendum_B.md:263` · `combatant.py:172-183` | RESOLVED-BY | MAP §A (`resource` is a declared role with its one instance). No formula is carried: Health's… | B04 | IN |
| 8 | F-PES-DICE-07 | the record of a roll is its band | D |  | `U5a:639` · `16_PESSIMIST_DICE.md:546` · 208 failures: by 1 ×76, 2 ×94, 3 ×33, 4 ×5 | RESOLVED-BY | MAP §D `fed_by` with SC-B's `Margin.terms` (U5c); the margin itself is on the record (under A-… | B04 | IN |
| 9 | F-DICE-02 | the default outcome is nothing and the top band cannot occur | D |  | `U5a:550` · `10_DICE_audit.md:158` · `band_odds(2, 2) == (0.74, 0.19, 0.07, 0.0)` at the built regime | SUPERSEDED | by A-6 (score plus a base, floor five): the pair (2 dice, Ob 2) no longer exists. The audit's… | → B05 | IN |
| 10 | F-DICE-03 | holding a score makes a person easier to oppose | D |  | `U5a:551` · `10_DICE_audit.md:182` · E-07: 26.00 / 58.00 / 73.50 % | RESOLVED-BY | `10_DICE_one_score_two_roles.md` Edits A–B, as reconciled to A-7 (the score is the trained ran… | B05 | IN |
| 11 | F-DICE-05 | two samplers half a success apart | D |  | `U5a:553` · `10_DICE_audit.md:208` · E-06: Failure 38.59 against 46.42 % at pool 8, Ob 3 | SUPERSEDED | by A-5: one sampler. `10_DICE_exported_face_rule_and_band_edges.md` Edit B's claim-correction… | → B05 | IN |
| 12 | F-DICE-06 | the advantage channel has one member, one sign, and sums to zero | D |  | `U5a:554` · `10_DICE_audit.md:240` · leverage 0.0 on 568 of 568 | RESOLVED-BY | `10_DICE_advantage_sources_for_the_arcs.md` Edit A (signed); the `edge` rows of the uses table… | B05 | IN |
| 13 | C-3, F-DICE-16 | the wound's penalty was ruled (+0.15 Ob per wound); the first proposal departed from it | D |  | `U5a:570` · `10_DICE_audit_addendum_B.md:144` · E-B03: the two forms differ two- to four-fold | SUPERSEDED | by Jordan's answer A-8 (D-08): a wound is a level against the roll, as combat spends it; the f… | → B05 | IN |
| 14 | F-PES-DICE-02 | at the shipped pair "everything draws" means "little happens" | D |  | `U5a:634` · `16_PESSIMIST_DICE.md:441` · 16.5 % of today's effect at (2, 2.0) | RESOLVED-BY | TASK (the unopposed stand-in, `plain`, the throughput reading and refusal to ship); applied to… | B05 | IN |
| 15 | F-PES-DICE-03 | the ceiling is a wall; every shipped forgery stands on it | D |  | `U5a:635` · `16_PESSIMIST_DICE.md:466` · pools 1–12 read 10.00 % at their cap | RESOLVED-BY | SOFT (the cap's closed form follows the one sampler: DOE §1) | B05 | IN |
| 16 | F-PES-DICE-05 | a failed search is forgotten and retried; remembering alone changes nothing | D |  | `U5a:637` · `16_PESSIMIST_DICE.md:510` · 157 of 157 `finding.none` Events have no descendant; deposit alone: 19 of 42 ag… | RESOLVED-BY | DOE §4 (the actor-only deposit of `finding.none`, read by `refused_before` of `16_PESSIMIST_CO… | B09, B05 | IN |
| 17 | F-PES-DICE-06 | one die cannot succeed, and a zero cannot try | D |  | `U5a:638` · `16_PESSIMIST_DICE.md:532` · `band_odds(1, 2.0)` | SUPERSEDED | A-6 (no person rolls under five dice); TASK for the unopposed rows | → B05 | IN |
| 18 | F-DICE-04 | four rolled verbs name no skill | D |  | `U5a:552` · `10_DICE_audit.md:197` · E-09 | RESOLVED-BY | U1 architecture §5 (one value per verb row, decided across CORE, DICE, SC and FA: C-U5a-11) | B04 (B04.03, B04.19) | IN |
| 19 | F-PES-DICE-04 | a field is decided by a draw the dice engine never sees | D |  | `U5a:636` · `16_PESSIMIST_DICE.md:491` · friction's 5th–95th percentile 0.164–6.107 | JORDAN | D-34 (luck in battle: a hidden multiplier, or a named level) | — (answered A-59, A-77) | IN |
| 20 | F-DICE-22 | two unread tests are prose guards | H |  | `U5a:578` · `10_DICE_audit_addendum_B.md:300` | RESOLVED-BY | `01_CORE_tests_delete_what_cannot_fail.md` row 1 (`test_knot_pool_formula.py`); `tests/valoria… | B02, B05 | IN |
| 21 | F-PES-DICE-08 | the obstacle's floor reaches one term and not the sum | H |  | `U5a:640` · `16_PESSIMIST_DICE.md:554` · E-P1 | SUPERSEDED | `13_SC_tuning_tables.md` T1 (U5c) | → B05, B02 | IN |
| 22 | F-DICE-23 | a skill's rank has no ceiling | H |  | `U5a:579` · `10_DICE_audit_addendum_B.md:207` · `effects_combat.py:262-268` | RESOLVED-BY | U1 architecture §2 (`scale` on the definition row, read by `raised_capability`); CAP Part A | B04 | IN |
| 23 | F-DICE-07 | a second roller, and a ladder in two classes | H |  | `U5a:555` · `10_DICE_audit.md:272` · 6 of 10,000 tenth-step cells differ; the pessimist's swap test: 0 of 20,000 net… | RESOLVED-BY | `10_DICE_one_roller_one_fraction_rule.md` Edits A, C, D as reconciled (mass battle composes on… | B05 | IN |
| 24 | F-DICE-09 | the typed layer omits the facts every draw depends on | H |  | `U5a:557` · `10_DICE_audit.md:307` · E-11: six scalars exported | RESOLVED-BY | `10_DICE_exported_face_rule_and_band_edges.md` Edits A (band floors; the per-die pair asserted… | B05 | IN |
| 25 | F-DICE-11 | the extension seam is unreached by the loop and half open | H |  | `U5a:559` · `10_DICE_audit.md:333` · E-04 | RESOLVED-BY | DOE §3 rows 2–3 (context validated on entry; the dead `extension` parameter deleted) | B05 | IN |
| 26 | F-DICE-12 | half the advantage module's surface has no game caller | H |  | `U5a:560` · `10_DICE_audit.md:346` · E-17 | RESOLVED-BY | DOE §1 (under A-5 the Normal closed form becomes the odds function: `p_success` is no longer d… | B05 | IN |
| 27 | F-DICE-13 | stale passages at the owner | H |  | `U5a:561` · `10_DICE_audit.md:361` · lines cited in the finding | RESOLVED-BY | DOE §3 row 5 | B05 | IN |
| 28 | F-DICE-19 | below one die the sigma boost is a full die's | H |  | `U5a:576` · `10_DICE_audit_addendum_B.md:245` · E-B05 | RESOLVED-BY | DOE §1 (under the one sampler a sub-one-die aggregate's spread and boost both scale with the r… | B05 | IN |
| 29 | F-DICE-08 | three rules for a fraction of a die | H |  | `U5a:556` · `10_DICE_audit.md:294` · E-05 | SUPERSEDED | by A-5: the bell-curve sampler takes a fractional pool as it is; the rounding and the stochast… | — | IN |
| 30 | C-8, F-DICE-21 | the field speaks sigma in die-equivalents and tires twice | H |  | `U5a:575` · `10_DICE_audit_addendum_B.md:285` · `config.py:306` | SUPERSEDED | MB's closure (U5b); addendum §5.1 item 5 states the target | — | IN |
| 31 | F-PES-DICE-09 | the field's four stat checks are bare binaries | H |  | `U5a:641` · `16_PESSIMIST_DICE.md:562` · `orchestration.py:2093-2166` | SUPERSEDED | MB's closure (U5b) | — | IN |
| 32 | F-PES-DICE-10 | words: `argument.won` at Partial; a contest with one roller | H |  | `U5a:642` · `16_PESSIMIST_DICE.md:569` · H-269 | SUPERSEDED | the verb table's owner lane (SC, U5c) | — | IN |
| 33 | res. 21 (`CLAUDE.md` §7) | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:608` | RESOLVED-BY | `U5a_CORE_owed_edits.md` §G (the same sentence as T-22; merged) | B03 | IN |
| 34 | §5.3 | the weapon-carry cost is the `threshold` role, one leaf function | — |  | `U5a:582` | SUPERSEDED | PC's and MB's closures (U5b); the role is MAP §A's | → B04 | IN |
| 35 | §5.5 | order of landing | — |  | `U5a:583` | RESOLVED-BY | restated for the answers in CAP "Order" and DOE "Order" | B04, B05 | IN |
| 36 | H-126, H-127, H-213 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:596` | RESOLVED-BY | `10_DICE_one_score_two_roles.md` (H-127's scope); `16_PESSIMIST_DICE_soft_ceiling.md` (H-213);… | B05, B04 | IN |
| 37 | res. 25 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:612` | RESOLVED-BY | MAP §D (`fed_by`) with SC-B's `Margin.terms` (U5c): one record of a roll, proposed once | B04 | IN |
| 38 | F-DICE-10 | the room is a flat obstacle shift | unrated in source |  | `U5a:558` · E-08 | RESOLVED-BY | the favourable half moves to leverage by Jordan's answer A-25 (SC's composer: U5c); the senten… | B05 | IN |
| 39 | C-4 | the roller proposal's `grep` falsifier cannot read one line | — |  | `U5a:571` · E-B02 | RESOLVED-BY | `10_DICE_one_roller_one_fraction_rule.md` falsifier restated (Reconciled) | B05 | IN |
| 40 | C-6, H-152 | closed by a run (CP-T02-01) | — |  | `U5a:573` · `probe_h152.py`, three arms with a mutation | RESOLVED-BY | DOE §3 row 6 (the register row's head and owner) | B05 | IN |
| 41 | §5.1 items 1–6 | the shared roller meets mass battle's resolver | — |  | `U5a:580` | RESOLVED-BY | DOE §1 (items 1–5 restated for the one sampler); item 6's order against `11_GO_one_draw_owner.… | B06, B05 | IN |
| 42 | H-31 (regrade `ruled`), H-88 (close), H… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:591` | RESOLVED-BY | DOE §3 rows 7–9 | B05 | IN |
| 43 | H-152 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:592` | RESOLVED-BY | DOE §3 row 6 | B05 | IN |
| 44 | H-244 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:593` | STALE/FP | `10_DICE_believed_odds_have_a_prior.md` is what exercises it | — (stale) | IN |
| 45 | res. 1, 2 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:598` | RESOLVED-BY | `10_DICE_one_roller_one_fraction_rule.md` Edits A, C, D (Reconciled) | B05 | IN |
| 46 | res. 6, 7 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:601` | RESOLVED-BY | `10_DICE_exported_face_rule_and_band_edges.md` Edits A, D; one resolver name for all three pro… | B05 | IN |
| 47 | res. 8, 10 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:602` | RESOLVED-BY | `10_DICE_one_score_two_roles.md` Edits A–B (Reconciled); the verb values: U1 architecture §5 | B05 | IN |
| 48 | res. 9 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:603` | RESOLVED-BY | DOE §3 row 1 | B05 | IN |
| 49 | res. 11, 12, 13, 14, 15, 16, 20 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:604` | RESOLVED-BY | DOE §3 rows 2–5, 7–10 | B05 | IN |
| 50 | res. 17 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:605` | RESOLVED-BY | `10_DICE_advantage_sources_for_the_arcs.md` Edit A | B05 | IN |
| 51 | res. 18 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:606` | RESOLVED-BY | `10_DICE_advantage_sources_for_the_arcs.md` Edits B–D (`wounds` as the second advantage source… | B05 | IN |
| 52 | res. 23 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:610` | RESOLVED-BY | `10_DICE_believed_odds_have_a_prior.md` Edits A–B | B05 | IN |
| 53 | §13 ARC-53 (a wound persists; a faction… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:619` | RESOLVED-BY | DOE §2 (the wound term); the faction half is an `addend` over `Act.via` (FA's, U5d; Jordan's a… | B05 | IN |
| 54 | §13 NPC-085, SCN-12, SCN-04/07/LOOP-C,… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:620` | RESOLVED-BY | `10_DICE_advantage_sources_for_the_arcs.md` Edit E (each a named door waiting on another lane'… | B05 | IN |
| 55 | §14, §15 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:625` | RESOLVED-BY | U1 architecture; `10_DICE_believed_odds_have_a_prior.md` | B05 | IN |
| 56 | §13 ARC-06 (an implementation can fail… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:617` | RESOLVED-BY | `18_DETERMINISM_task_draw_for_uncontested_verbs.md` (PART 6) | B07 | IN |
| 57 | §9 "one roll as a decision"; §8 step 7… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:614` | RESOLVED-BY | `11_GO_player_surface_contract_B.md` (`Offer` rows carry odds; U5d) | B34 | GO |
| 58 | C-2 | the first audit's research skip was a false absence | — |  | `U5a:569` | RESOLVED-BY | the three leads are used in F-DICE-16, -17, -18 | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | IN |
| 59 | §5.2 | the duel round from the dice side | — |  | `U5a:581` | SUPERSEDED | PC's closure (U5b): an approach is an `edge` row, never a pool rule | — | IN |
| 60 | §5.6 item 1 | the wound's channel | — |  | `U5a:584` | SUPERSEDED | answered: A-8 (a level against) | — | IN |
| 61 | §5.6 item 2 | what a score is worth outside a fight | — |  | `U5a:585` | SUPERSEDED | answered: A-6 | — | IN |
| 62 | H-310 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:594` | SUPERSEDED | FI / SC (U5c) | — | IN |
| 63 | H-312 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:595` | RESOLVED-BY | U1 architecture §5 (`interrogate: inquiry`) | B04 (B04.03, B04.19) | IN |
| 64 | H-332, H-349, H-361; CP-T01-01 … -06; C… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:597` | STALE/FP | — | — (stale) | IN |
| 65 | res. 3, 4 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:599` | SUPERSEDED | A-5 (no whole-dice fraction rule) | — | IN |
| 66 | res. 5 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:600` | SUPERSEDED | A-5 (the audit decided "leave the offset, narrow ED-833"; Jordan answered the other way) | — | IN |
| 67 | res. 19 (SCN-05 restated: a spend buys… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:607` | RESOLVED-BY | same file, "The resolution" | B05 (B05.60) | IN |
| 68 | res. 22 (mass battle's survivor-ratio l… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:609` | SUPERSEDED | MB's closure (U5b); A-3 fixes the field's returned vocabulary (won, lost, drawn) | — | IN |
| 69 | res. 24 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:611` | SUPERSEDED | PC's and MB's closures (the `believed_estimate` role) | — | IN |
| 70 | §11 survivor (which sampler non-combat… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:613` | SUPERSEDED | answered: A-5 (the audit's Option B). Every edit the audit wrote "for A" is reconciled | — | IN |
| 71 | §13 ARC-22, NSC-04, NSC-07, SCN-01, ARC… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:615` | RESOLVED-BY | A-6 and U1 architecture §4 (the top band becomes reachable); band-distinct writes on `lie`, `s… | B04, B05 (B04.24, B05.05) | IN |
| 72 | §13 ARC-18, ARC-17 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:616` | STALE/FP | — | — (stale) | IN |
| 73 | §13 SCN-04 (difficulty from a stored di… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:618` | SUPERSEDED | SC's obstacle proposal (U5c) | — | IN |
| 74 | §13 SCN-05, SCN-02, ARC-23 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:621` | RESOLVED-BY | SCN-05: resolution 19. SCN-02 conflicts with ED-SC-0038 (named, SC's). ARC-23 (a skill require… | B05 (B05.60) | IN |
| 75 | §13 EMG-C2, NSC-05, SCN-08, NPC-052; EM… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:622` | SUPERSEDED | WR's and CORE-side happenings closures (U5d); the mechanism (a keyed rate draw) exists | — | IN |
| 76 | §13 NPC-001, NPC-004, NPC-075, ARC-22 (… | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:623` | RESOLVED-BY | U1 architecture §6 (cast content) | B04, BA1 (B04.09, BA1.01) | IN |
| 77 | §13 EMG-X6 | 3.3 `audits/10_DICE_audit.md` §6.1 rows, §6.2 resolutions 1… | — |  | `U5a:624` | SUPERSEDED | SC (U5c) | — | IN |

---

## GO — the port gate and the player surface

**What is wrong.** GO here is the oracle half of a port contract of which one position in ten is built, and that one holds: the realm's hash is identical under three `PYTHONHASHSEED` values and three CPython minors, every draw of a computed season is keyed, and the played and automated seasons are one code path (`audits/11_GO_audit.md` §0). The contract the port gate would freeze does not yet prove a port: its slices enter the combat engine 0, 2 and 4 times and fight one field battle across seeds 0–2 (F-GO-01); the float contract was unstated (F-GO-02); draws were built in two places (F-GO-03); 91 mass-battle tunables read from the environment and are exported nowhere (F-GO-04); PLAYABLE exists at one seam (F-GO-08); there is no save (F-GO-09); six lane dialects and no shared surface vocabulary (F-GO-15). The pessimist (`16_PESSIMIST_GO.md` §0): the port gate as planned would certify a game no player can read, and cannot tell; 160 to 194 times in a two-season run the offer names a person the seat holds no claim about. Its findings: the parity contract cannot see the player's surface (F-PES-GO-01); PLAYABLE's reach is one person's one verb (F-PES-GO-08); with F-GO-19, the offer is three to five times the legible size.

**What was decided.** Declared floats (A-29) and one draw per key with no recorder (A-30), both in Layer 1; the scene slate is a list of questions for the player, NPCs take the first (A-48); reveal after the line ends (A-49); no engine version is asserted (ED-GO-0002).

**What is built where.** B03 and B03g the early port landings (GO-09, GO-11, GO-01, GO-05, `--check` live before B04); B06 the float contract and the one draw owner (12 RESOLVED-BY rows); **B34** the player surface contract, fidelity and campaign modes, `Scene.cost` (16 rows); **B41** the port gate's order and coverage and the surface pins. **What stays open:** GO-06 and H-5 need a `valoria-game` checkout (BLOCKED); the surface pins' values (content); "no end state reaches a client and no save" is carried, not built (`U4_TRACEABILITY.md` §3).

**Rows: 62** (RESOLVED-BY 51 · SUPERSEDED 9 · STALE/FP 2 · DISPUTED 0 · JORDAN 0).

| # | id | claim | sev | R | evidence | disposition | carrier | batch | owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | F-GO-02 | the float contract is unstated; Layer 1 and the plan disagree | B |  | `U5d:442` · `11_GO_audit.md:142` · `04:1130`; 1,245 floats folded a season | RESOLVED-BY | FLOAT A, B, C as reconciled (A-29: declared floats now; the Layer 1 text for step 13 is owed,… | B06 | IN |
| 2 | F-GO-03 | draws are built in two places; replay never tests the port's samplers | B |  | `U5d:443` · `11_GO_audit.md:176` · `combat.py:397` (E4) | RESOLVED-BY | KEYED (A-30: one draw per key, no recorder) with DRAW as reconciled (one constructor and one s… | B06 | IN |
| 3 | F-GO-08 | PLAYABLE exists at one seam | B |  | `U5d:448` · `11_GO_audit.md:310` | RESOLVED-BY | SURF-B §6 (corrected by F-GO-18: two kinds of play) as reconciled (A-9: a turn is a short sequ… | B41, B34 | GO |
| 4 | F-GO-15 | no shared surface vocabulary; six lane dialects | B |  | `U5d:483` · `11_GO_audit_addendum_B.md:103` | RESOLVED-BY | SURF-B (R50) | B34 | GO |
| 5 | F-PES-GO-08 | PLAYABLE's reach is one person's one verb | B |  | `U5d:505` · `16_PESSIMIST_GO.md:584` · E2 | RESOLVED-BY | SURF-B §6; "one code path" shown for all 83 seats (resolution 11) | B34 | GO |
| 6 | F-GO-01 | the pinned slices barely enter the two largest modules | B |  | `U5d:441` · `11_GO_audit.md:115` · combat entered 0/2/4 times, a fought field 0/0/1 (E4) | RESOLVED-BY | GATE §3 (R1); PINS (the surface block) | B41 | GO |
| 7 | F-GO-04 | 91 mass-battle tunables read from the environment and exported nowhere | B |  | `U5d:444` · `11_GO_audit.md:204` · the audit's count | RESOLVED-BY | GATE §5 (R10) | B41 | GO |
| 8 | F-PES-GO-01 | the parity contract cannot see the player's surface | B |  | `U5d:498` · `16_PESSIMIST_GO.md:542` | RESOLVED-BY | PINS | B41 | GO |
| 9 | F-GO-13 | the UI set's content-level half is not in the tree | D |  | `U5d:481` · `11_GO_audit_addendum_B.md:57` | RESOLVED-BY | REF (R48: not reconstructed; the oracle's readings are the specification) | B03 | IN |
| 10 | F-GO-21 | two opposite answers to "what does the player know" | D |  | `U5d:489` · `11_GO_audit_addendum_B.md:213` | RESOLVED-BY | REF (R58, R59); the end-of-campaign half is A-49 | B03 | IN |
| 11 | F-GO-16 | a person cannot read what his own act came to | D |  | `U5d:484` · `11_GO_audit_addendum_B.md:127` | RESOLVED-BY | SURF-B §3 (`receipt`), with the measure corrected by F-PES-GO-11 (6 to 8%, three inquiry verbs) | B34, B03g | GO |
| 12 | F-PES-GO-05 | believed odds answer on 0.8% of candidates | D |  | `U5d:502` · `16_PESSIMIST_GO.md:567` | RESOLVED-BY | `10_DICE_believed_odds_have_a_prior.md` (U5a's; the pessimist's three edits listed for CHAR an… | B05, B06 | IN |
| 13 | F-GO-09 | no save; the canonical encoding cannot rebuild a world | D |  | `U5d:449` · `11_GO_audit.md:329` · `state/world.py:390`; no decoder (grep) | RESOLVED-BY | OWED-GO §1 (R44's snapshot, as a plan with a round-trip gate; A-29 makes a save a state snapsh… | B06 | IN |
| 14 | F-PES-GO-02 | GO-16 is a false N-line | D |  | `U5d:499` · `16_PESSIMIST_GO.md:551` · PES-GO §1.1 cut | RESOLVED-BY | KEYED (A-30) | B06 | IN |
| 15 | F-PES-GO-04 | "why" is `None` by construction | D |  | `U5d:501` · `16_PESSIMIST_GO.md:562` · `Seen.why` | RESOLVED-BY | WHY | B09 | IN |
| 16 | F-PES-GO-06 | what a person learns of others' acts is nothing for most | D |  | `U5d:503` · `16_PESSIMIST_GO.md:572` · 57 to 62% | RESOLVED-BY | WHY; `18_DETERMINISM_notice_is_a_draw.md` (U5a) | B11, B09 | FI |
| 17 | F-PES-GO-07 | the offer is half inert | D |  | `U5d:504` · `16_PESSIMIST_GO.md:578` · 21% of acts on fifteen rows | RESOLVED-BY | `16_PESSIMIST_CORE_a_refusal_is_remembered.md`, `16_PESSIMIST_FI_D_withhold_what_has_no_produc… | B26, B09 | FI |
| 18 | F-GO-07 | what the player is shown has an owner for the choice and none for the reason or the result | D |  | `U5d:447` · `11_GO_audit.md:284` | RESOLVED-BY | SURF-B §1–§4 (supersedes SURF §1–§4) | B34 | GO |
| 19 | F-GO-19 | the offer is three to five times the legible size | D |  | `U5d:487` · `11_GO_audit_addendum_B.md:185` · up to 544 rows (F-PES-GO-09) | RESOLVED-BY | SURF-B §2 (R55); MODES §3 (R56) as reconciled (A-48: the player triages a list of questions) | B34 | GO |
| 20 | F-PES-GO-03 | the offer names persons the seat does not know | D |  | `U5d:500` · `16_PESSIMIST_GO.md:556` · `seat_holders` | RESOLVED-BY | HELD §1–§3 (seat news ships realm-wide, A-32) | B34 | GO |
| 21 | F-PES-GO-09 | the offer's size has a tail of up to 544 rows | D |  | `U5d:506` · `16_PESSIMIST_GO.md:589` | RESOLVED-BY | SURF-B §2; MODES §3; A-48 | B34 | GO |
| 22 | F-PES-GO-10 | the creation sheet cannot tell seats apart and offers 37 cohorts | D |  | `U5d:507` · `16_PESSIMIST_GO.md:593` | RESOLVED-BY | HELD §4 (`CreationRow.holdings`, `cohort`); `U5d_SE_cohort_heavy_moves_and_caste.md` (a cohort… | B38, B34 | WR |
| 23 | F-GO-05 | halts have no portable form; GO-10 covers four sites | D |  | `U5d:445` · `11_GO_audit.md:231` · 172 in-loop raises | RESOLVED-BY | GATE §4 (R11) | B41 | GO |
| 24 | F-GO-06 | the gate freezes behaviour while the game is being invented; two edges wrong | D |  | `U5d:446` · `11_GO_audit.md:256` | RESOLVED-BY | GATE §1, §2 (R12, R13, R14) | B41 | GO |
| 25 | F-GO-10 | stale and contradictory text at the pointers a porter reads first | H |  | `U5d:450` · `11_GO_audit.md:344` · the audit's table | RESOLVED-BY | TEXT 1–13 | B03 | IN |
| 26 | F-GO-11 | the digest test's control half is spent | H |  | `U5d:451` · `11_GO_audit.md:360` · `test_go07_canonical_digest.py:282-311` `[not re-opened]` | RESOLVED-BY | TEXT 11 (R32) | B03 | IN |
| 27 | F-GO-14 | the newest UI document carries two dead tracks; its repair plan stopped | H |  | `U5d:482` · `11_GO_audit_addendum_B.md:89` | RESOLVED-BY | REF (R49) | B03 | IN |
| 28 | F-GO-20 | the Godot specification contradicts Layer 1 at five points | H |  | `U5d:488` · `11_GO_audit_addendum_B.md:204` | RESOLVED-BY | REF edit 1 (R66–R71) | B03 | IN |
| 29 | F-GO-12 | the determinism controls vary the hash seed, not the interpreter | H |  | `U5d:452` · `11_GO_audit.md:371` · the audit's E5: no drift reproduced at seed 0 | RESOLVED-BY | FLOAT (removes the cause at its owner); no guard (§0.1 pt 5) | B06 | IN |
| 30 | F-PES-GO-13 | exit line 4 lists a check that reports drift and passes | H |  | `U5d:510` · `16_PESSIMIST_GO.md:603` · the tool's own text | RESOLVED-BY | OWED-GO §3 (a card edit at B10-20's open) | B06 | IN |
| 31 | F-PES-GO-12 | no exported word for any Event kind or verb | H |  | `U5d:509` · `16_PESSIMIST_GO.md:600` | RESOLVED-BY | PINS (words for kinds and verbs) | B41 | GO |
| 32 | GO-07, GO-13, GO-14 | listed closed; verified closed | — |  | `U5d:453` · E3, E5, E8 | STALE/FP | none owed (GO-07's test trimmed by TEXT 11) | — (stale) | IN |
| 33 | GO-09, GO-11, GO-01, GO-05 | open; early landings | — |  | `U5d:454` | RESOLVED-BY | GATE §2 (R13, R14); TEXT 8, 9 | B41, B03 | GO |
| 34 | ED-1054 | stale navigation open since 2026-06-30 | — |  | `U5d:458` | RESOLVED-BY | TEXT (R35: closed; the banners are its resolution) | B03 | IN |
| 35 | R22–R32, R34, R35 | pointer and stale text | — |  | `U5d:467` | RESOLVED-BY | TEXT 1–13 | B03 | IN |
| 36 | §14 (skill surface; R31) | may a field bind to an attribute | — |  | `U5d:475` · `descriptors.json` | RESOLVED-BY | TEXT 10 | B03 | IN |
| 37 | R48–R78 | thirty-one resolutions | — |  | `U5d:490` | RESOLVED-BY | SURF-B (R50–R55, R57, R72–R74, R76–R78), MODES (R56, R60–R65), REF (R48, R49, R58, R59, R66–R7… | B34, B03 | GO |
| 38 | resolutions 1–11 | decided | — |  | `U5d:511` | RESOLVED-BY | PINS (1), KEYED (2), HELD (3, 6), WHY (9); 4 → F-PES-GO-05's row; 5 none; 7 → `03_PC_typed_out… | B14, B06, B41, B34, B09, B03g | PC |
| 39 | GO-10, GO-12, GO-08, GO-15 | open; under-scoped or mis-shaped | — |  | `U5d:455` | RESOLVED-BY | GATE §4, §5, §3, §1; DRAW (R8: every unseeded fallback refuses) | B06, B41 | IN |
| 40 | GO-16 | the draw recorder; premise false | — |  | `U5d:456` · PES-GO §1.1 | SUPERSEDED | A-30: not built; KEYED | → B06 | IN |
| 41 | R2, R3, R4 | float sums; transcendentals; "slice 3" | — |  | `U5d:461` | RESOLVED-BY | FLOAT A, B | B06 | IN |
| 42 | R5, §11 survivor | step 13's "integer domain" | — |  | `U5d:462` | SUPERSEDED | A-29 (declared floats now; integer state stays possible); FLOAT C | → B06 | IN |
| 43 | R6, R8 | one constructor; fallbacks refuse | — |  | `U5d:463` | RESOLVED-BY | DRAW | B06 | IN |
| 44 | R44 | no save | — |  | `U5d:468` | RESOLVED-BY | OWED-GO §1 | B06 | IN |
| 45 | R15–R20 | offer rows; `explain`; aftermath; scar Events; "a player must be able to"; PLAYABLE | — |  | `U5d:465` · addendum §B6.2 | SUPERSEDED | by SURF-B (R50–R57, R72–R78), which corrects R17 and R20 | → B34 | GO |
| 46 | R45, R46 | the UI design set; "witnessed" fidelity | — |  | `U5d:469` | RESOLVED-BY | SURF-B; MODES §2 (R62 refines R46) | B34 | GO |
| 47 | §13 ARC-R16 summary, ARC-46 history, AR… | readings a person lacks | — |  | `U5d:471` · E7 | RESOLVED-BY | SURF-B §3–§4 (`receipt`, `account`); SURF-B §2 for a history over his own claims | B34 | GO |
| 48 | §13 "players must be able to X" (53 nee… | per verb | — |  | `U5d:473` · 23 of 67 verbs execute (E10) | RESOLVED-BY | SURF-B §2 (`OFFER-CONTAINS`); each act is its verb lane's | B34 | GO |
| 49 | F-GO-17 | `AftermathRow.own_act` cannot be computed | unrated in source |  | `U5d:485` | RESOLVED-BY | SURF-B §4 (R52) | B34 | GO |
| 50 | F-GO-18 | two kinds of play; two choice surfaces missed | unrated in source |  | `U5d:486` | RESOLVED-BY | SURF-B §6 (R53, R54) | B34 | GO |
| 51 | R77 | the Scene Slate has no generator | — |  | `U5d:491` | SUPERSEDED | A-48: the slate is a list of questions offered to the player; NPCs take the first; SURF-B §1 a… | → B34 | GO |
| 52 | §B6.3 survivor | may the end of a campaign show what the person never knew | — |  | `U5d:492` | SUPERSEDED | A-49 (reveal after the line ends and no continuation is taken; never in play); MODES §4 as rec… | → B34 | GO |
| 53 | R1, R10–R14 | pins; tunables; halts; freeze; edges | — |  | `U5d:460` | RESOLVED-BY | GATE §1–§5 | B41 | GO |
| 54 | GO-06 | cross-repo reader, held | — |  | `U5d:457` | RESOLVED-BY | none owed (correctly held; another repository) | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | GO |
| 55 | Strategy Part VIII items 1–8 (R36–R43) | open items | — |  | `U5d:459` · R42 `[UNVERIFIED]` in the audit: stays marked | SUPERSEDED | closed by the ladder in the audit (the Key substrate retired; the oracle by ED-1050; no stat v… | — | GO |
| 56 | R7, R9, R33 | replay of the port's samplers; what GO-16 records; "statistical parity" | — |  | `U5d:464` | SUPERSEDED | A-30 and A-5: the port implements the same keyed hash and the one sampler; nothing is recorded… | — | GO |
| 57 | R21, R36–R43, R47 | superseded or irrelevant items | — |  | `U5d:466` | RESOLVED-BY | none owed | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | GO |
| 58 | §13 arcs represented today (ARC-R16, AR… | the world acts unattended; hidden quantities | — |  | `U5d:470` · 749 acts, 13,379 Events a season (E3) | STALE/FP | none owed (represented) | — (stale) | GO |
| 59 | §13 ARC-14, ARC-17 ("a single threshold… | wrongly stated (a player/NPC fork) | — |  | `U5d:472` | RESOLVED-BY | restated by the audit; A-47 keeps the threshold as the opener of a mandatory scene, never the… | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | GO |
| 60 | §13 ARC-09, NPC-088 and others cross-li… | not GO's | — |  | `U5d:474` | SUPERSEDED | U5a (CORE, CHAR) | — | GO |
| 61 | F-PES-GO-11 | corrects F-GO-16's measure | unrated in source |  | `U5d:508` | RESOLVED-BY | made in the audit | none owed (a pointer; `workplan_v12/COVERAGE.md` §A.2) | GO |
| 62 | §7 survivor | the draw | — |  | `U5d:512` | SUPERSEDED | A-30 | — | GO |
