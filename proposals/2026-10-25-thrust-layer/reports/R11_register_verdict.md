# R11 — Missing in code: the register's verdict after the relay

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). Delivered in chat during the session of 2026-10-24/25 and reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Figures were taken **before** the register's measurements (`../01_MISSING_IN_CODE.md` §2, probes P1–P12); where they differ, `../02_MAJOR_TAKEAWAYS.md` §9 (Corrections) governs.

**Asked by the user:**

> carefully design using agonist-antagonist methodology what is missing in code based upon the above

---

The register survives only in part. Its measurements hold, but the lead design (G-01, typing the candidates) was wrong and is withdrawn. The antagonist found it passed over an open ruling, H-156 (`hole_register.yaml:3615`), which already covers this question. H-156 ran the CLAUDE.md §0 ladder, found that the `give`/`petition` precedent doesn't settle it, and left the row open. The register had called it "answered by precedent", which was false.

I re-opened each finding that changed a design or a headline, and re-ran what the critic couldn't. Of its 14 findings (A1–A14), all were upheld.

**Ranked by what they changed**
1. **G-01 design withdrawn.** The rule "stamp every referent with its collection class" fails on several shipped rows:
   - Record sub-kinds (`works`, `dispensation`) aren't collections.
   - `DocketItem` is a world read.
   - `determine` has two existence conjuncts of different kinds.
   - The existing partition forms untyped rows only on plain referents, so stamping every referent would starve them.
   - The proposed loader refusal would reject the shipped `comply` row.

   What survives is H-156's three options. Choosing among them is Jordan's decision, and it is the register's one new escalation.
2. **Measurement corrected.** P3b's "33.1%" counted `_admits` calls, not acts, and misclassified two kinds. P10 re-takes it per act: 32.2% of attempts at 2 seasons and 28.7% at 4 are refused at admission on a wrong-kind subject. The roughly one-third finding holds.
3. **Headline refusal share holds.** 76.2% / 76.8% on the driver's definition, 73.8% / 73.9% with graded losses excluded.
4. **G-16 re-owned.** The duel-terms seam belongs to PC-10b, and my fixture on every fight contradicted its text. The "default for an un-negotiated fight" question is answered: lethal, per PC-10b. That escalation is removed.
5. **Smaller corrections.**
   - G-02 is a limit R-05 already records.
   - G-03 has four readers of "refused", not two, and is split in two.
   - `build`, `found` and `work` can't execute by any typing (ED-IN-0297).
   - `endings_reached` is an existing executable terminus that the register and the thrust-layer design both missed (added to G-14).
   - The P6 "28 of 46" was a fit to the strings, not a measurement.

**Held when attacked**
- P1's capture: seed 0 re-ran to the same hash, and P10's totals equal P1's exactly.
- P4's death counts.
- G-12 and G-22.
- G-13 and G-19.
- The `ladders`→`goal_stages` rename, though the critic judged it not compelling.

`accept` deaths: 0 of 11 had a challenge aimed at the acceptor by the accept's subject (P11b), so G-15's claim holds at the pair level. Challenge events number only 15 against those 11 kills. Cutting the `accept` route still depends on PC-10b's H-240 route being chosen.

`[UNVERIFIED: the share of delivered questions fed by a refusal-kind claim]` was not measured. The control for any G-01 option has to read questions delivered and claims deposited, not just executed counts. The degree-aware retry change in G-03 also wasn't run, because it moves the hash by construction.

The player seat isn't covered. A player's acts bypass `opening_set`, so any formation filter binds NPCs only.

I stopped after this one round, per CLAUDE.md §0. Nothing is committed or pushed, and the tree is clean. I did not subscribe to PR activity.

Files are in `proposals/2026-10-25-thrust-layer/toy/`:
- `missing_in_code_v2.md` (§7 holds the pass record)
- `missing_in_code_v1.md`
- `probes/` (new: `p10_clean_remeasure.py`, `p11b_accept_challenge.py`, `p12_fallback_kinds.py`, with outputs)

Question for you: do you want the register and probes committed under `proposals/2026-10-25-thrust-layer/`, added to PR #506 or a new PR?
