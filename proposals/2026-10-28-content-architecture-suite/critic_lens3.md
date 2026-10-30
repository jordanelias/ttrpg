# Lens-3 critic report: directive compliance and completeness

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Report of the lens-3 critic (directive compliance and completeness) on the suite's parts 00 to 05, run once in the 2026-10-28 session after the suite was assembled. Text: the `message` field of the critic subagent's own hand-back call, timestamped 07:15:53 in the transcript, verbatim and unedited (12,914 characters). The brief it was given is the prompt of the Agent call of 07:11:18 and is appended below the report, verbatim. The first pass of the reconstruction recovered the other two critics' hand-backs (07:21:11 lens 2, 07:22:20 lens 1) and missed this one. Its line citations (`01:257`, `04:21` and the like) refer to the suite's files as they stood at about 07:11 to 07:15, before the three-lens corrections at 07:24 to 07:28; they do not match the line numbers of the files in this directory. Its findings are not applied here beyond what the session's own later patches did. The suite was written in a session of 2026-10-28 that committed nothing. This file is a reconstruction from the transcript (second pass, 2026-10-30). Where this text and the tree disagree, the tree wins.

---

**Verdict:** The suite answers all eight questions and most directives in substance. The parts Jordan has to act on (the index page, the storyline answer in §8, and the 13 rulings) are written for engineers. Four of its own parts contradict each other on points that carry his directives, and about half the rulings are not choices a non-programmer can make.

All files are under `/tmp/claude-0/-home-user-ttrpg/a0006cad-2382-5a52-b1f4-b17983d229b1/scratchpad/suite/`. I read 00, 01, 02, 03, 04 and 05 in full. I grepped 06, 07a–d and A1–A5, and checked the repo for PR numbers and K-MB-4. I re-verified no other figures.

## Findings, worst first

**1. Rulings that are not plain choices (lens e).** Location: 01:257-269, compressed again at 00:36.
- **Answerable as written:**
  - #9 (01:265): "whether the world is dying or only misunderstood".
  - #6 (01:262): plan before battle vs live command.
- **Partly answerable:**
  - #2 (01:258). It offers only "tenth = TS" vs "the eight". It leaves out P2-C and the B-10 variant (finding 9), and "by pointing at its existing field" needs a gloss.
- **Not answerable as written:**
  - #1 (01:257) gives "amends Layer 1 `04:793`" and states no consequence of saying no.
  - #3 (01:259) is a formula, "attribute + capped trained excess in place of `max`". The plain consequence ("talent currently hides training", 01:71) sits elsewhere.
  - #4 (01:260) is "a hold Tenure on an equipment object, or a stores kind on a rung". The real choice — a sword owned by the person (lootable, inheritable) vs town armoury stock with "no heirlooms" — is only at 02:89.
  - #5 (01:261) is a list of plumbing (B10-19 clause, schema, B4.1, `part12:276`). It also includes the `part12:276` amendment that 01:169 and 02:121 both say is "not a question for you".
  - #7 (01:263): "`utter` OUGHT + `commit`". The question (can new factions or towns be founded during play?) is never stated.
  - #8 (01:264): "after the `confer` load is measured".
  - #10 (01:266): "until a `foreign` relation has a producer". It never says what Altonia being on means in play.
  - #11 (01:267): "(it changes the content hash)". The design consequence is hidden: 02:48 says the flag frees orders "for every person, NPCs included", so every NPC lord also gets free orders and the whole simulated world changes.
- **Not Jordan's to rule, per CLAUDE.md §0's "`needs_jordan` is not a parking space":**
  - #12 (01:268). The suite itself says it contradicts ED-SC-0033 and ED-IN-0284, so it is closable as superseded.
  - #13 (01:269). 01:254 already lists "the Godot version is 4.7 (ED-GO-0002)" as settled, and deleting `KeyStore.gd` follows ED-1050 and ED-IN-0232. It is work, not a ruling. It is also out of scope and yet listed as a "joint ruling" of the recommended package (00:32, 01:271).
- **Count conflict:** 01:254 says "about 8 items need your ruling"; the list has 13.
- **Fix:**
  - Rewrite each ruling as "Choose X or Y; X means…; Y means…".
  - Close #12 and #13 by precedent.
  - Drop the ED-IN-0225 clause from #5.
  - State the NPC consequence in #11.

**2. The mass-battle command ruling is presented as already decided.** 05:87 says "Decision taken (K-MB-4). The plan is fixed before battle… no live command." 01:262 lists the same question as ruling #6. In the repo, K-MB-4 is a research recommendation that "the marching faction choose its order of battle" (`/home/user/ttrpg/research/by_lane/MB_mass_battle.md:707`). It is not a ruling against live command. **Fix:** 05:87 should say "recommended" and point to ruling #6.

**3. A "matchup preview" breaks the no-forecast directive.** 02:60 says "a weapon-style triangle that falls out of the physics, shown as a matchup preview (T19:138)". A preview of a matchup is a forecast. It also contradicts 04:53 ("There is no fixed weapon triangle… learned by fighting") and 05:37 ("Matchup odds… stay internal"). **Fix:** delete "shown as a matchup preview" at 02:60.

**4. Where B10-S sits in the plan is stated three different ways.**
- 01:46: "after B10-10, before B10-11".
- 04:66: "moved ahead of B10-10".
- 02:91: "a DOSSIER position after B10-10 and before B10-S".

B10-10 is where attributes are built (01:42). If the slice comes before it, every seated person rolls 2 dice. **Fix:** pick one position and state the consequence.

**5. The management surface: the suite overrides Jordan's reading, then calls the override approved.**
- Jordan's directive: "the engine acts on the player's behalf directly and no character does it" (quoted at 01:289).
- 01:299 adopts that strong reading.
- 01:316 reverts to the weak reading, in which the seated character is the author and a delegate executes — exactly "a character does it".
- Ruling #11 then reads "weak reading approved" (01:267), on a list of things that need his ruling.
- **Fix:** put both readings in #11 as a live choice, with the plain difference. For example: under the weak reading, an unseated or interregnum player has no management menu.

**6. The basis of the "rung 1–2" decision contradicts itself, and "rung" is never explained.**
- A1:162: "an unseated person has 45 of 56 eligible, none seat-gated".
- 04:21: the rung-1/2 seat's 45 = "the 41 every person has, plus 4 seat rows".
- If A1 is right, a rung-1/2 seat adds nothing, which undercuts his "yes".
- 04:69 (P3-B risk) says to "offer one duchy seat among the starting persons". The suite never says which rung a duchy is (01:250 implies above rung 2), so Jordan cannot tell whether this overrides his decision.
- **Fix:** re-measure the 45 once, gloss "rung" at first use in 01, and say whether a duchy seat is inside rung 1–2.

**7. Unreadable to a non-programmer: the five worst passages (lens b).**
- 01:166-183 (storylines §8: the collisions and the row/person-side table). Example: "a T-b band read from the opener's own ledger… mints a staged Record, and the act declares the term, so T-c is satisfied". This is the answer to his own storylines directive.
- 01:324 (minigame contract): "prize row… `provider`… `module_entry`… host input builder… gate folds it into writes at RESOLVE, or at ENCOUNTER… token class… Receipt".
- 01:95 (how a character chooses): "score Σ axis weight × verb alignment + 2 × stance… softmax draw at τ = 0.1".
- 00:28-36 (the "one page" index). The page read first has a proposal table and a ruling list made of ids: "amends T-c and the fourth-motion default", "958 cells", "(1) M3…(2) J-T2…(4) J-T5…(11) the `management: true` flag".
- 04:21-22: "45 of 56 rows (`aperture 2 0`)… `claim_landed` questions give 41–63 options over 28–33 verbs… H-92".
- Runners-up:
  - 03:26-30, the verb rule (`verb_capability: verb → key`; `key_base: key → {act, resist}`).
  - 02:105, the pool card fields.
  - 01:103, "A creed `Proposition` plus the live `commit` Tenures" — Q4's answer opens in jargon.
- Never glossed in the main report: Tenure, Proposition, Rung, OUGHT, Record, claim/ledger, seat, rung, content_hash. Part 04's gloss of "seat" and "verb row" (04:3) is the only one.
- Tables with no sentence saying what to take from them: 03:71-80 (eight worked verbs), 03:222-227 (migration: engineering detail, no decision for Jordan), 04:31-42 (subsystem cards).
- **Fix:** a one-paragraph glossary at the head of 01. Replace the index table cells and ruling list with plain-language choices.

**8. Material that looks productive but does not distil (lens c).**
- **The same material repeated in five places, with drift between copies.**
  - Troops, kit and management appear at 01 §13-15, 02 §1 (:47-61), 03 §1 (:57-67; troops in an attributes part), 04 §2 (:51-53) and 05 §3-4.
  - The Klapp example is told six ways (02:67-72, :77-87, :107-115, :143-146; 03:50-55; 04:61), with different mechanics:
    - The thread-sensitivity gain is "+1 TS" per research at 03:52, but "the act's declared TS step" per stage at 02:109.
    - Who sees it first is "the player" in 03:53 and a Riskbreaker in 04:61.
  - **Fix:** one owner per template (02 §1) and one canonical Klapp; the other parts point to them.
- **Cell counts promoted to the headline comparison.** 00:29 and 03:21 compare 958 / 912 / 820 cells. A 46-cell difference between proposals is meaningless, and the figures are "design estimates, untested" (01:281). **Fix:** drop them from the index.
- **Process telemetry addressed to Jordan.**
  - 00:40-42, "Corrections applied after adjudication" (a changelog of the agents' own errors).
  - 01:279, "Digest and analyst errors found and corrected".
  - 01:195, word counts for "threshold" 162, "CI" 382, "MS" 381.
  - 01:241, "Of the 128 verb names… 52 match".
  - 03:159-162, "My test of A6" (one agent disputing another).
  - **Fix:** cut these, or move them to the appendix.

**9. Proposals that are not truly distinct (lens d).**
- **P1-A is a strawman against the directive it exists to answer.** 02:100 says "Klapp's story runs in every world, which is a stock story… A is expected to raise the stock share." Its own falsifier predicts it fails Jordan's sameness concern.
- **P3-A is not an alternative.** It is the first build of P3-B (04:5 "shipped first as P3-A's text client"; 04:69 "B10-S = A's client"). The real choice is P3-B vs P3-C, plus the odds policy.
- **P2's best option by its own test is buried.** 03:162 says "B-10… passes A6's own tests and overrides nothing"; no score is orphaned and the largest share is 22%. It fixes P2-A's stated risks ("FOC stays an orphan; ATT drives 29%", 03:117). Yet B-10 is not a proposal and not in ruling #2.
- **P2-A's reason is circular.** "keeps Jordan's count and overrides nothing" (03:232) answers a directive that says the nine may be wrong. Meanwhile 01:52 admits "the built evidence cannot separate the sets". 01:52's "suffice" overclaims; it is a default, not a finding.
- **Fix:**
  - Make B-10 a named option in ruling #2.
  - Present P3 as B vs C.
  - Either give P1-A a real variety mechanism or label it the baseline rather than a proposal.

**10. P1-C crosses the "not whole arcs" directive, and the suite does not say so.** 02:13 and 02:139 propose "arcs as loaded templates (a real amendment)". That is the scripted-whole-arc form Jordan excluded. **Fix:** flag it as conflicting with the directive, or drop that clause from C.

**11. Q6's "how other games handle managing a settlement" is barely answered.** All there is: one "Compare" line (05:131: Manor Lords, Frostpunk, King of Dragon Pass, with no description) and the overseer bullets at 01:314. Main §5 (01:122-134) has no precedent at all, and its "action menu" lists verbs, not what the player experiences. **Fix:** in 01 §5, a short paragraph on what the player decides each turn in RTK, Knights of Honor II and CK3, what feedback comes back, and how that maps to the console.

**12. Q8 cannot be read arc by arc.**
- 01:199-209 gives capability families without arc numbers or the family letters.
- 02:100 and 02:130 then use the letters ("families B (summons), G", "part of I", "D needs `foreign`"), which are defined only in A5:96-104.
- Arcs are never named; "NEVER arcs" (01:185) is undefined.
- 02:130 says P1-B's ≈40 arcs needs `foreign`, while ruling #10 recommends Altonia off, so the recommended package's ≈40 depends on a ruling the suite recommends against.
- **Fix:** copy A5:96-104 into 01 §9, with arc names, and reconcile the ≈40 with ruling #10.

**13. Q2's precedent coverage is thin (soften).** It is three sentences (01:69), with Burning Wheel and Traveller "from memory". "Aptitude" is answered by retiring the word (01:73) rather than by showing how games handle aptitudes. Bannerlord's learning limit appears only inside P2-C (03:199). It is answered, not distilled.

**14. Prior PR work is mostly reused by its contents, with a gap (observation).** In the suite text only #505 is cited by number (02:26; 03:104, :166, :177, :183, :189).
- #501's CP-T ids are used throughout.
- #504 and #507 are v10 and its Layer 0 edits (`/home/user/ttrpg/references/restructure_ledger.md:3010`; `/home/user/ttrpg/proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-00-sequence.md:72`), and are implicit.
- #506's thrust gap register (G-01..G-29; `/home/user/ttrpg/proposals/2026-10-24-master-workplan-v10/ctl/coverage_check.py:9`) is cited only in A5:98, :102. The main §9 arc answer and the B4.1 summons recommendation never connect to it.
- **Fix:** one line in 01 §9 naming the #506 G-ids each capability closes.

**Directives checked and honoured:**
- No forecast, except finding 3.
- Fire Emblem-style window driven by his own combat system (04:44-49; 05 §3).
- Troops after RTK and Total War (02:53-56).
- Kit after tactical RPGs with physics-derived values (02:58-61).
- Each subsystem a minigame on the season loop (01 §14).
- Templates permitted (00:9; 02:3).
- His three "yes" decisions are recorded (01:24, :247-250). Their ledger rows are owed (00:38).

One round only, as instructed; no further audits proposed.

---

## The brief the critic was given (Agent call, 07:11:18)

You are the adversarial critic, LENS 3: DIRECTIVE COMPLIANCE AND COMPLETENESS. Subject: a review suite at /tmp/claude-0/-home-user-ttrpg/a0006cad-2382-5a52-b1f4-b17983d229b1/scratchpad/suite/ (read 00_INDEX.md, then 01_MAIN_REPORT.md, 02_P1_templates.md, 03_P2_attributes_skills_histories.md, 04_P3_player_surface.md, 05_A7_subsystem_merit.md). The reader is Jordan, a non-programmer game designer. The request, in his words (condensed): a high-level, strategic, top-down review answering eight questions: (1) how much worldly/character/narrative content exists as coded and what is missing per workplan v10 and the subsystem designs; (2) key character capability attributes, their relation to verbs, and how precedent games handle base scores, skills, aptitudes, histories; (3) the character template; (4) faction template; (5) settlement template; (6) what each subsystem needs to be legible and playable (precedents, action menus, gameplay opportunities, player experience; how other games handle managing a settlement); (7) whether event decks exist, a template, and what they apply to; (8) what is needed to achieve the old 55-arc register's arcs. Method demands: avoid AI work that looks productive but does not distil key concepts; plain language (he does not understand 'queries vs fields' without explanation); resolve conflicts by current code and precedents; MULTIPLE coherent proposals for (a) templates, (b) attributes/skills/histories/progression, (c) player surface per subsystem (available actions and choices); standing directives: freestanding storylines, set pieces and event decks (Klapp example) because pure emergence would make similar stories, but scripted hooks and sequences, not whole arcs; a management surface where the engine acts for the player (Romance of the Three Kingdoms / Crusader Kings feel) costing no scene budget; each subsystem a minigame on the season loop that is informed by, acts on and impacts world state; templates are permitted so unfilled instances are not 'missing content'; nine attributes may be wrong; troops after RTK and Total War, equipment after tactical RPGs; personal combat as a Fire Emblem-style attack window from his own dynamic system with NO forecast; reuse prior PR work (#501, #504/#507, #505, #506); his three 'yes' decisions (agent-drafted content, B10-S text-first slice before the port gate, first playable person at rung 1-2). Your job: check each of the eight questions and each directive against the suite and find (a) any question or directive not actually answered or honoured, with the place it should be; (b) places where the text is unreadable to a non-programmer (undefined jargon, ids with no gloss, tables without a sentence saying what to take from them) — name the five worst passages; (c) work that looks productive but does not distil (padding, duplicated passages across parts, catalogues with no decision attached) — name the worst; (d) proposals that are not truly distinct alternatives (a strawman B or C); (e) whether the 13-ruling list is something a non-programmer could answer (each ruling stated as a plain choice with consequences) and which ones are not. Report: verdict first (one sentence), then ranked findings worst first, each with suite file + quote or section, and the minimal fix. Terse; no praise. One round only; do not propose further audits.
