# Digest proposalsB8

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: proposals dated 2026-09-20 or later and undated, not read in full by earlier digests. Folder `proposals/2026-10-29-parliament-and-debate/` (stress tests of the social-contest proposals P1/P2/P3/P4 and harnesses), `proposals/2026-11-04-content-parameters-docket/` and one PR log. None of these is RATIFIED canon; every stress-test file is a terminal-pass REFERENCE (CLAUDE.md §0 exception). "P1/P2/P3" = social-contest proposals 1 (one draw, one roster), 2 (staged proceeding), 3 (authority first); "AR" = the armature document (`2026-10-30-social-contest-armature.md`).

### proposals/2026-10-29-parliament-and-debate/2026-10-30-stress-test-proposal-1.md
- **What it is:** Stress test of P1 "One draw, one roster" against real code, 2026-10-31, terminal-pass REFERENCE, harness `stress_p1*.py`, logs `…-stress-log-p1-*.jsonl`.
- **Status:** "REFERENCE (2026-10-31). A terminal pass … changes no tracked file and allocates no ED/PP." Reading: historical evidence about an unbuilt proposal; findings about the code (not P1) are live facts to re-verify.
- **Bears on:** SC, FA, DICE, CORE, WR.
- **Content that matters:**
  - P1's 17 quoted probabilities reproduce exactly (`p_success`); closed form `E[m]=0.4N+0.8√N·softcap(s)−Ob` holds for N>=1 but BREAKS for N<1: the engine floors pool at 1D for mean and spread (:5, :16-17, claims 4-5).
  - Legitimacy index L (share of residents with live `commit` edge): church L=0 in 14 of 17 territories, 7/83 pooled; every church commit belongs to an office-holder; seeds 0-2 identical (one realm, not three) (:13, :81).
  - `speak` bands all emit a kind with identical alignment vector, so regard cannot reward a winning speaker: 0/197 decided judges flip; 98.4% of judge/speaker pairs have no regard (:20, :5).
  - The pool draw silently floors NaN, 0, negative, -6 weights at 1D; infinite N gives `inf` rolls, `p_success` NaN; with ceiling 3 and S27.4 (`ob > 2×pool`, `sigma.py:273`) an actor under 1.5D is REFUSED against an opponent above 4D, contradicting R-16 "priced, never refused" (:36-38).
  - Ceiling 3 inverts the status quo: P(meets) vs an equal falls to .380 at 6D then climbs to .980 at 30D (uncapped it falls to .247) (:62); at 12D the aptness price is clipped away so speech-kind choice is irrelevant (:70).
  - Live docket is keyed on party: 50 matters about one party, 1 docketed, 49 refused (`docketed(w, matter)`), so R-11 "many matters" is unreachable; a second `open_case` on a docketed matter is refused whatever the authority, so P1's appeal path has no docket path (:22, :62, :87). `void` appeal needs three unlisted changes (`DISPOSABLE_KINDS` at `effects_information.py:362-363`, a `_disposal` void site, a closure basis at `effects_governance.py:335-349`) (:108).
- **Conflicts / stale:** B1 "suite green; same season, smaller" BROKE: applying P1 B1 literally leaves `build_realm(0)` raising SystemExit (`corpus_run.py:356`, cast entry NPC-088 `capability: copying`); 14 files/38 tests fail; deleting the kernel (16 files, P1 says 18) breaks `test_sigma_leverage_parity` (collection error, 901 tests) (:5, :98-106). Citation line numbers in effects_information are off by ~25 lines (per P2 stress). [UNVERIFIED] whether the code has changed since HEAD `404e8023`.
- **Open items:** What a failed `speak` deposits is unstated (silence vs speech EV flips) (:71); no `authority:` default stated; `person_q.legitimacy` revert arm never measured (:117, :124); B5 choice layer (disposition operand, `commit_count`, `mutual`) unbuilt, so K1/K2/K6/K7 outcomes are not computable (:60).

### proposals/2026-10-29-parliament-and-debate/2026-10-30-stress-test-proposal-2.md
- **What it is:** Stress test of P2 "Staged proceeding", 2026-10-30, terminal-pass REFERENCE; harness `stress_p2.py`; HEAD `404e8023`.
- **Status:** "REFERENCE (2026-10-30). A terminal pass … allocates no ED/PP, queues no work and changes no tracked file." Reading: historical evidence about an unbuilt proposal; code findings still informative.
- **Bears on:** SC, FA, CORE, DICE.
- **Content that matters:**
  - P2's distinctive claim (case-file `Record.stages` holds the agenda so burning/seizing stalls the proceeding) is true only of MATTER maturing a stage: `determine` never reads the file, so burning it stalls nothing (:9, claim 4); `forge` mints a faction sheet and cannot forge a case file (claim 5); any person with `create_record` can overwrite the agenda by naming its id, 3/3 actors (claim 6, :22).
  - A stage whose due tick passes while its holder is absent NEVER matures (matter.py matures only at `due == w.tick`), 3/3 runs (claim 3, :19).
  - `open_case` declines both Record-disposing rows (`parliamentary_debate`, `council_of_state`), so a K6 parliament cannot be opened by the case-file route (claim 11, :27). Empty stage list accepted and filled with 3 default H-80 stages; stage labels unvalidated; NaN price gives a NaN obstacle that S27.4 does not refuse and ladder grades Failure (:52).
  - Staging is attrition, not stall: at equals only 4.3/10.1/66.0% (2D/5D/12D) of staged cases reach a disposal vs 26/38/79.6% for one draw (:65-72); a six-stage row costs at most 5 closing draws; 3-5 on plea paths. Two real stalls: forced-Partial with no cap (open mass 1.0 forever) and S27.4 refusal (24 of 648 grid cells) (:73, claims 15-16).
  - Plea game: deny weakly dominant in 21/27 configs; justify wins 6/27; concede-only strictly dominated 26/27 even at season cost .15; a conceding reward routed through the obstacle is clipped away in 6/9 under live ceiling 2 (:60 claims 17-20).
  - Computed play, 3 seeds × 2 seasons: 13 cases opened, 20 `determine.refused`, 0 determined; every case docketed under arrangement `None` (claim 25); King/Queen sit on 319/319 non-empty benches; 8 `determine` seats per realm, structure identical across seeds 0-2 (:76-77).
  - Scratch worktree: kernel deletion turns 6 test files + `sim_params` exporter red; deleting H-80 placeholder stages moves both pinned hashes (`873525df`→`40cf9490`; two-season `9e71dfe9`→`c7c86c67`); the `case` docket key moves BASE_HASHES[1],[2] and breaks `test_sc01_fired_slot` and `test_u7_remit` (:88-100).
- **Conflicts / stale:** 7 citations to `effects_information.py` / `gate.py` / `test_season_weather.py` missed by 4-25 lines (:47, :128-134). The "lapse when the file matures open (R-1)" has no reader in the tree (unverified).
- **Open items:** Who may forge a case file; a typed subsidiary matter `determine` can close (a docked subsidiary is a wedge, claim 9); no negotiation row, `disposal: mutual` has no reader (:209); per-act draw key `H(seed,tick,subject,purpose)` under collapse unverified (:217).

### proposals/2026-10-29-parliament-and-debate/2026-10-30-stress-test-proposal-3.md
- **What it is:** Stress test of P3 "Authority first", 2026-10-30, terminal-pass REFERENCE; harness `stress_p3.py`; five logs.
- **Status:** "REFERENCE (2026-10-30). A terminal pass … queues nothing and changes no tracked file." Reading: historical evidence about an unbuilt proposal; code findings informative.
- **Bears on:** SC, FA, CORE, WR.
- **Content that matters:**
  - Authority grouping recomputes exactly (31 determine-ish seats: Crown 19 / Hafenmark 4 / Varfell 4 / church 7 in P3's grouping; 3 church determine seats all scoped T9); 11 of 14 legitimacy figures reproduce (:5, claims 1,6,7).
  - Q1 (church seat re-anchored by `scope_rung` only) opens 0/19 cases in T1 and 0/4 in T4 (`case.unauthorized`); only moving `rung` as well works, which removes the arm limit it was meant to keep (claim 8, :33). Church bench is empty for 74/83 homes; polity can open at 82/83 homes, church 9/83 (:89-90).
  - `defy` strictly dominates appearing in 36/36 modelled cells (should read WEAK dominance per the log); the case file is a kind-`text` Record held by the opener so `evade/defy` on it is `compliance.impossible`; 160 real attempts, 0 executed (claims 15-16, :41).
  - Forum contest normal form: (commit own, commit own) = impasse is the only pure equilibrium; polity row beats church row on accuser's odds in 15/15 cells (:74, :76).
  - Legitimacy L identical across seeds 0-2; NaN → clamp01 gives 1.0; `opinion_full=0` raises ZeroDivisionError; territory-level L but cases heard at settlement/hearth (76% of settlements have ≤2 residents) (:59, :87-88).
  - Real rates (3 seeds × 8 seasons): `open_case` 72 attempted/28 opened; `determine` 65 attempted/3 executed (all `matter.undetermined`); `pardon` 45/all refused; `arrest` 4/0 made; `carry` 295/24 carried (:82). Mean-of-bench `n=2` is worse than n=1 (:61).
  - C1 deletions: 12 of 24 reachable files go red; `module_contracts.yaml:448-470` "stale" row is load-bearing (deleting it breaks 54/65 `test_u7_remit` and 9/13 `test_sc01_speak`) (:109-115).
- **Conflicts / stale:** Claims "arrest attempted 0 times" broke for seed 0 (4 attempts). P3 §9.1 "an empty bench… never a refusal" is false: a `determine.refused` Event is emitted (:95). Roll-call (:134+) includes my-own-defect lines (harness bugs kept).
- **Open items:** forum branch, warrant branch, appellate closure basis, expulsion rule, `evade/defy` reader do not exist in the tree (:119, :191); "a royal person involved" trigger rate unclear (17% of opened cases) (claim 26).

### proposals/2026-10-29-parliament-and-debate/2026-10-30-stress-test-report.md
- **What it is:** First stress-test report on the social contest module, kernel and the season-loop debate surface; 2026-10-30, run on Windows, HEAD `79b7defa`, five probes; terminal-pass REFERENCE.
- **Status:** "REFERENCE (2026-10-30). A terminal pass … allocates no ED/PP, queues no work and changes no code." Reading: historical; superseded in detail by the three per-proposal stress tests but its kernel and 13-season loop numbers are unique.
- **Bears on:** SC, CORE, DICE, PROCESS.
- **Content that matters:**
  - `modules/social_contest/roll.py` held under 75,132 edge trials: only the documented `ValueError` for ceiling below `OB_MIN`; NaN/inf inputs flow to NaN `net`/`ob` unrefused (:40, :43).
  - Leverage saturates smoothly via `1.5·tanh(x/1.5)` (`M_MAX=1.5`, `sigma_leverage.py:104,141`); at pool 3 equal readings at lv -2/-1 or +1/+2 are rounding artifacts of whole-number nets, corrected from an earlier "clamp" reading (:42).
  - The evaluated (not adopted) kernel `systems/social_contest/sim/contest/`: 751,619 resolutions, no crash, but draws from the process-global RNG in 86% of first resolutions (SC-05), empty `Panel` raises ZeroDivisionError, `None` policy raises AttributeError (:49-50).
  - Kernel proceedings differ hugely in weaker-side win share (casual 21.6% ... formal 0.04%); church_tribunal seat A wins 84.2% of decided with equal faculty; formal/grand contests end in `committee` ~99% at equal sides (:51-53).
  - Season loop seed 0, 13 seasons: season cost grew 11.7× (33 s → 387 s), docket grew to 72 items, 43 empty slots; 0-1 `matter.determined`, 4 `commitment.made`, 0 `argument.*`, 161 `duty.taken`; `question_aggregation_rule=all` collapses `date.scheduled` 51→3 and `duty.taken` 161→0 (:60-63).
  - `engine/season/tests/test_social_contest_module.py` has a path-separator test that fails on native Windows (:67).
- **Conflicts / stale:** Kernel findings concern a candidate the later proposals delete (R-14); run on HEAD `79b7defa`, later than-but-not-equal to `404e8023` used elsewhere. Season-loop counts are one seed.
- **Open items:** whether near-deterministic formal/grand proceedings and the church_tribunal seat asymmetry were intended (:51-53) — mooted by the kernel's deletion; season-cost growth with docket size not re-measured here [UNVERIFIED].

### proposals/2026-10-29-parliament-and-debate/2026-10-31-stress-test-attribution.md
- **What it is:** Sorts every finding of the three per-proposal stress tests into engine-side, proposal-side, or instrument; 2026-10-31, terminal-pass REFERENCE.
- **Status:** "REFERENCE (2026-10-31). A terminal pass on PR #536's reports … allocates nothing, queues nothing." Reading: live as an index of engine facts E1-E16 and content facts C1-C8 (verify before citing).
- **Bears on:** SC, FA, CORE, CHAR.
- **Content that matters:**
  - E1 (one case per docketed matter) is deliberate by the comment at `effects_information.py:355-361`; E2 (no appeal path, `pardon` closes only the exercised seat's edges) is documented closure basis: constraints to plan around (:19-20, :49).
  - E4: computed play does not reach a determination: `docket_named_arrangement` 0 in 24 seasons; 65 `determine` attempts, 3 executed, all `matter.undetermined` (:22).
  - E5-E6: MATTER matures stage only at `due == w.tick` (`matter.py:339-345`, opened); `determine` reads the docket only; no lapse reader (:23-24).
  - E13-E14: pool floors silently at 1D, NaN obstacle not refused by S27.4 and grades Failure, leverage moves in whole-number steps; `roll_net` rounds pool (.60 vs .50 continuous at 5D) (:31-32).
  - C1-C8 content facts: seeds 0-2 are one realm of 83 persons; capability authored for 0/83; commits sparse and held by officers; speak bands share one alignment vector; King/Queen on 319/319 benches; authority `parties` bench empty for 83/83; no producer feeds σ (:40-47).
  - Correction: comparison's claim that two proposals' "0 attempts" claims were wrong was misattributed; only P3's figures are contradicted (:123).
- **Conflicts / stale:** `[UNVERIFIED]` whether a refused act is silent (P2 says nothing emitted; P3 says `determine.refused` emitted) — may differ by refusal site (:125). `sigma.py:273` S27.4 line was not opened by this pass (:5).
- **Open items:** E-rows rest on reports' real/model labels; none re-run (:127).

### proposals/2026-10-29-parliament-and-debate/2026-11-01-probe-controls-seed0.json
- **What it is:** Output data of `probe_controls.py`, seed 0, 4 seasons (the "control" instrument for the matters/standpoints doc).
- **Status:** Data file, no Status line. Reading: evidence artifact, valid for the checkout `eaf4c9b`.
- **Bears on:** SC, CHAR, FA, WR.
- **Content that matters:**
  - Opinion-of-faction at t0 vs end is nearly the same (e.g. Hafenmark 43 pos/40 neg at t0), so the spread comes from the build; `Schoenland` and `faction x` read exactly 0 for all 83 persons (:5-176).
  - 83 persons at build, 78 at end (5 deaths) (:4, :89).
  - `C3_docket_items_with_date_and_matter_at_each_season_end` is `[0,0,0,0]`: no sitting ever filled with a matter (:90-95).
  - 67 `comply`/`evade / defy` acts: 52 comply, 15 defy; none on a dispensation; `C1_dispensations_in_world`=13, `C1_dispensation_addressee` empty (:179-202).
  - 45 forged Records: 44 with exactly 1 holder, 1 with none (:203-207).
  - Same-season claim copies: 1,122 groups with ≥2 holders, confidence differs in 59 (5%), source in the same 59 (:208-210).
- **Conflicts / stale:** none noted; data only.
- **Open items:** seed 0 only (the doc says seed 1 not examined).

### proposals/2026-10-29-parliament-and-debate/2026-11-01-probe-event-kinds-seed0.json
- **What it is:** Output of `probe_event_kinds.py`, seed 0, 4 seasons: Event-kind counts, resolved acts by verb, final docket.
- **Status:** Data file. Reading: evidence artifact.
- **Bears on:** CORE, SC, FA, MB, WR.
- **Content that matters:**
  - Dominant events: `claim.deposited` 35,700, `claim.decayed` 37,049; `condition.worn` 1,288; `term.matured` 762 (:5-8).
  - Social-subsystem events: `speech.unheard` 59, `case.opened` 5, `matter.turned` 3, `matter.advanced` 1, `determine.refused` 8, `pardon.refused` 8, `commitment.made` 6 (:31, :63-80); no `matter.determined`.
  - Refusal-heavy loop: `migrate.refused` 129, `challenge.refused` 125, `exchange.refused` 106, `transfer.refused` 104, `train.refused` 101, `forge.refused` 86 (:15-29). `march.declared` 78 / `march.refused` 67 (:23, :30).
  - Acts by verb: `oblige` 255, `utter` 194, `fight` 8, `speak` 4, `open_case` 16, `evade / defy` 15 (:82-128).
  - Final docket 28 items: 8 with matter, 20 Date-only; no `arrangement` set; `commits_live` 133 (OUGHT 128, HOLDS 5) (:129-269).
- **Conflicts / stale:** none noted.
- **Open items:** n/a (data).

### proposals/2026-10-29-parliament-and-debate/2026-11-01-probe-event-kinds-seed1.json
- **What it is:** Same as seed0 for seed 1, 4 seasons.
- **Status:** Data file. Reading: evidence artifact.
- **Bears on:** CORE, SC, FA.
- **Content that matters:**
  - Similar shape: `claim.deposited` 38,622; `march.declared` 129 (vs 78 seed 0); `duty.taken` 120 (vs 53); `determine.refused` 13; `case.opened` 3; `fight` 2 acts (:5-131).
  - `revoke` 8 acts all `revoke.refused`; `confer` 41 acts, `confer.refused` 38 (:41, :61, :121).
  - Docket 20 items, 19 Dates (:133-226); `commits_live` 131.
- **Conflicts / stale:** none noted.
- **Open items:** n/a.

### proposals/2026-10-29-parliament-and-debate/2026-11-01-probe-matters-intake-seed0.json
- **What it is:** Output of `probe_matters_intake.py`, seed 0, 4 seasons: question sources, claim stems, record kinds, tenures, opinion and pursuit spreads.
- **Status:** Data file. Reading: evidence artifact.
- **Bears on:** CHAR, CORE, SC, FI, WR.
- **Content that matters:**
  - Questions: `claim_landed` 15,642 vs `need` 495 summed over season starts; first question sources 226 vs 56 (:5-12).
  - Ledger claims 15,600: firsthand 11,712, told_by 3,866, inferred 22 (:185-190); top stems `seen` 6,421, `term.matured` 1,086, `dispensation.issued` 935 (:158-184).
  - Records by kind: text 342, faction_sheet 76, cover 52, petition 27, dispensation 13, works 2 (:235-242); live tenures: hold 731, contain 405, commit 133, reside 78, oblige 52 (:247-253).
  - 28 docket items, 0 naming an arrangement (:233-234); Propositions OUGHT 258, HOLDS 3 (:243-246).
  - 15 pursuit axes with sd; `stability` widest (0.02-0.80, sd .20), `happiness` narrowest (max .08); `persons_with_capability` 0; `persons_with_conviction` 42; offices 32 (:350-444).
- **Conflicts / stale:** the key `stamped_class_on_first_question` lists referent ids not classes (the doc says so, :654).
- **Open items:** n/a.

### proposals/2026-10-29-parliament-and-debate/2026-11-01-probe-routes-hand-built.json
- **What it is:** Output of `probe_routes_hand_built.py`: a hand-built bench world (from `test_u7_remit.py`) where `determine` fires; routes 1-4 of the fold.
- **Status:** Data file. Reading: evidence artifact.
- **Bears on:** SC, CHAR, FA.
- **Content that matters:**
  - A Partial `determine` emits `matter.determined` and opens an `oblige` edge on the party (p_mid→off_duke); second `determine` on the same party is `determine.refused` (:2-59).
  - Non-person matter: `case.opened` but `determine.refused` and the docket slot stays (:60-70).
  - Judge's pursuits move only at Success (`pursuit.moved` event) not at Partial (:71-127, :121-129).
  - Regard/legitimacy estimates of bystanders rise 0.01-0.066 at both Partial and Success (:78-169); five ledgers hold the determination (judge firsthand, four told_by) (:20-36).
- **Conflicts / stale:** none.
- **Open items:** only Partial and Success were reached in 80 tries per the doc.

### proposals/2026-10-29-parliament-and-debate/2026-11-01-social-contest-matters-standpoints-and-fold.md
- **What it is:** Companion to P4: how worldly matters enter the engine, 18 families of matter, nine sources of standpoint difference, and how decisions fold back into the season; 2026-11-01, with two critic rounds.
- **Status:** "PROPOSED (reference; resolves nothing, schedules nothing)". Reading: live as a code-verified description of intake/fold (checkout `eaf4c9b`); no ratified rulings are made in it.
- **Bears on:** SC, CORE, CHAR, FA, FI, WR.
- **Content that matters:**
  - No act fetches a matter: all intake passes through one pipe (Event → WITNESS fan-out → Claim in each holder's ledger → Question via `questions_for`, `world_q.py:3217`); seven entry points (claim landed, ambition `need`, standing occasion, sitting, docketed matter, standing crossing, a thing he said) (:67-106).
  - Over four seasons 15,642 `claim_landed` Questions vs 495 `need`; of 261 Propositions 258 OUGHT, 3 HOLDS (factions with no creed), so forensic matters have no carrier in computed play (:39-42, :131-135).
  - Eighteen families of matter (§3.3: wrong done, heresy, contempt, holding, office, grant, obligation, war/treaty, provision, place, standing, fact-finding, bargain, procedure, opinion, membership, trade/levy, body contest); families 4,5,6,9,13 blocked on absent sites (`hold` disposal site, `resolution` licence, consent conjunct) (:220-263).
  - `speak` writes nothing at any band; `determine` writes the disposal edge and moves the judge's pursuits via `consequence_pursuits` (`person_q.py:615`; `effects_information.py:561`); `comply`/`evade / defy` are emission-only (:484-506).
  - Probe: `matter.determined` 0, `pursuit.moved` 0, `arrest.made` 0, `pardon` 8/8 refused, `give` 7/7 refused, `covenant` 17/17 refused, `exchange` 106/106 refused; 67 `comply`/`defy` all `compliance.impossible` (seed 1: 43) (:508-534, :232-239).
  - Return path: six routes by witnessed claim, five by state (:558-587); only route 1 (witnessed decision) has a running pipe and carried no contest outcome; route 4 (deed told → regard/legitimacy) has readers but thin supply (`news.told` 14/20).
  - A matter with no person-party cannot be disposed (`determine` refuses at `party`); a dead party or a venue with no bench holds a slot forever; `matter.lapsed` is an Event no code emits (:171-184).
- **Conflicts / stale:** Says `module_contracts.yaml:464-486` older `social_contest` row is stale (:470, :733) while P3 stress shows its existence is load-bearing; `rosters.yaml: genres` "NOTHING DERIVES genre YET" vs doc's own mood derivation (second derivation of one codomain, :203-207). Opinion spread comes from the build, not play (control). Pace: S27.4/R-16 conflict inherited.
- **Open items:** Where the season waits for a played contest (R-24) is explicitly not designed (:605-607); `speak` has no write (parliament design §5 build 3); no speech-kind roster for deliberative/epideictic (:260-263); three Record kinds only name a referent (:108-112).

### proposals/2026-10-29-parliament-and-debate/2026-11-01-social-contest-proposal-4-authority-staged.md
- **What it is:** Social-contest Proposal 4 (authority first plus staged hearing, with computed player choices and a faculty layer), 2026-11-01, with a read-only critic pass appended.
- **Status:** "PROPOSED (reference; resolves nothing, schedules nothing)". Reading: live-as-proposal and not built; the critic's own verdict says it should NOT replace P1 as the base, only stand as the target specification for the choice layer once P1's core and the dead core run (:864-871).
- **Bears on:** SC, FA, CHAR, DICE, CORE.
- **Content that matters:**
  - Three authorities (`parties`, `polity`, `church`) via `authority.by_faction` in `rosters.yaml`; rites (accusatorial/inquisitorial/arbitral) as data in `arrangements.yaml`; stages `proof, definition, justification, judgment, forum, licence` as classification only; case file as new Record kind `case`; citation as a `dispensation` served by `give` (:63-78).
  - Faculty layer replaces `VERB_CAPABILITY`: `faculties:` table (eloquence, reasoning, reading, composure) over descriptor_registry attribute keys; `dice = 1.25·Σ faculty_weights·faculty_of ...` puts average (faculty 4) at R-40's 5D (:80-135). Attributes live nowhere on the live path (`Person.capability` empty 0/83; nine attributes on 1-7, default 1, a ruled tenth unnamed, `descriptor_registry.yaml:27-45`).
  - Draw channels: dice, obstacle = `min(ceiling, opp score÷2)` then opponent proofs÷2 then aptness; σ is the decider's own regard only on an act the decider performs (F8) (:137-158).
  - Plea (deny / concede fact / concede definition) fixes the question tried; Failure holds to next sitting, third Failure closes; ≤3 contested stages; MATTER should mature `due <= tick` (:182-206).
  - Ten player choices each computed (log `2026-11-01-stress-log-p4-choices.jsonl`); 14 of 14 survive "own test", 10 of 14 under headline weights, 3 fail per named character; forum for accuser lopsided toward church (153 of 162 cells at 2D) (:299-335, :834).
  - Sequencing A0-A7 (seven batches): A1 deletions (kernel, `VERB_CAPABILITY`, discrete call, H-80 labels), A2 dead core (computed `open_case` names its row; `determine` reached; test `docket_named_arrangement`>0 over 3 seeds), A3 draw + faculty, A4 authority/rite, A5 hearing, A6 forum/appeal/arm/legitimacy, A7 choice layer (:600-616).
  - Questions for Jordan (§11): church judging reach (`scope:` key), R-36 L from barrier index (F8), attributes into roll (J-13 vs R-31/R-41; critic: Q3 already answered by `workplans/valoria_master_workplan_v10_part6.md:33`), ceiling value (G1/R-37: 3 vs live 2), meaning of "a royal person is involved" (R-34) (:765-781, :849).
  - Critic BREAKS IT findings: A1 as ordered cannot be green (deletes `VERB_CAPABILITY` before replacement; readers at `data/verbs.py:1580`, `harness/corpus_run.py:353`, `sigma.py:143`, `test_u8_cast_fields.py:277-285`); most of the ten decisions have no verb row (plea, offer proof, speech kind, challenge a judge, name enemies, forum plea, come forward) (:843-844).
- **Conflicts / stale:** Cites `workplans/valoria_master_workplan_v9_part5.md:433` which the critic says does not exist (:849); the 'live ceiling 2' vs R-37's ruled 3 is an unresolved ruling conflict; "A5 burn the file stalls determine" depends on repair (c) and contradicts today's code (P2 stress claim 4); the proposal's own "ten decisions" are not acts the loop can form. Deterministic risk: grade caps rewrite band outside `degree_from_net` (R-6, R-8) (:837); AB 'no deterministic' rule: "burning is near-dominant" and 'defy weakly dominates evade in church' (:839) are costless corridors.
- **Open items:** Q1-Q5 above; church contempt cost (:839); appeal only from church benches (:841); NPC payoff weighting policy (:845); default faculty at 4 until sheets land (:842).

### proposals/2026-10-29-parliament-and-debate/lopsided_levers.py
- **What it is:** Harness (2026-10-30/31), second half of the "lopsided outcomes" inquiry on the evaluated kernel; probes narrative layer and levers for the weak side. Not a gate.
- **Status:** Code, no Status line. Reading: historical probe against a kernel (`systems/social_contest/sim/contest/`) that P3/P4 propose to delete (R-14); live only while that kernel exists.
- **Bears on:** SC, DICE.
- **Content that matters:**
  - Feeds real kernel track proceedings to `narrative.summarize` (written for winners 'a'/'b'; track proceedings return `A_decisive`, `committee`) (:1-5, :22-40).
  - Gives weak side (faculty 1 vs 4) levers: evidence on live ground, raised `standing_start`=8, institutional `Pressure(toward='a', institutional=1.0)` across `formal_contest`, `royal_audience`, `church_tribunal` (:51-73).
  - Imports `cell, side, Log, git, sc, ROOT` from `lopsided_mechanism` and `Pressure` from kernel `contract` (:17-19); sample-until-time-slice design logs n per cell (:9-10).
- **Conflicts / stale:** Depends on the kernel directory the proposals delete; any run after deletion fails at import. Uses `hash(...)` seed (varies with PYTHONHASHSEED) so non-replayable unless `PYTHONHASHSEED=0`.
- **Open items:** Output logs `2026-10-30-stress-log-lopsided-levers.jsonl` not in this assignment; the lopsided inquiry md (`2026-10-30-lopsided-outcomes-inquiry.md`) covers conclusions.

### proposals/2026-10-29-parliament-and-debate/lopsided_mechanism.py
- **What it is:** Harness (2026-10-30), decomposes why kernel proceedings are lopsided, one mechanism at a time (sections A geometry, B seat, C exchanges, D policy, E gap, F degree).
- **Status:** Code, no Status line. Reading: historical probe of the not-adopted kernel.
- **Bears on:** SC, DICE.
- **Content that matters:**
  - Defines `win_geometry` giving the advantage gap needed for decisive/total outcomes of `PersuasionTrack` (start, scale; decisive at 7 / 3, total at 9 / 1) (:60-72); `cell()` logs gap mean/sd and `A_decisive_threshold_in_sd` (:75-122).
  - Tests church_tribunal at canonical `start=6.0` vs neutral 5.0; casual_dispute at 1,2,3,5,8 exchanges; formal/grand contest under four policies (`logos`, `build_then_close`, `exploiter`, `demagogue`); formal_contest B faculty 1..7; reception degree distribution by faculty via `Bout._reception(A)` (:165-190).
  - Kernel pool law referenced: `sc.primitives.Pool.size(f)` and `Leverage.net(f, on_ground=True)` (:136-137).
- **Conflicts / stale:** Imports `Log, git` from `stress_probe.py` (same folder) — shared helper, coupled files. Kernel-dependent (see lopsided_levers).
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/probe_controls.py
- **What it is:** Read-only controls C1-C5 for the matters/standpoints/fold document (2026-11-01); `python probe_controls.py SEED SEASONS`.
- **Status:** Code. Reading: evidence instrument; live against checkout `eaf4c9b` but not a gate.
- **Bears on:** SC, CORE, CHAR.
- **Content that matters:**
  - Builds `P.build_realm(seed)`, `SeasonDriver`, `make_chooser(...)` with shipped fixtures; measures `world_q.opinion_of` per `FACTION_BY_PROP` at tick 0 and end (:26-47).
  - C1 classifies `comply`/`evade / defy` acts by the subject Record kind and whether the actor held it; C2 counts holders per forged record (`forgery_quality` > 0); C3 docket items with both date and matter at each season end; C5 confidence/source differences among same-(subject,predicate,when) claim copies (:49-86).
  - Uses `d.resolved`, `w.docket`, `p.ledger` as read surfaces.
- **Conflicts / stale:** Reads `Record.forgery_quality` via `getattr`; if the attribute moved, C2 silently reports 0 [UNVERIFIED].
- **Open items:** seed 0 only was run.

### proposals/2026-10-29-parliament-and-debate/probe_event_kinds.py
- **What it is:** 28-line read-only probe printing Event-kind counts, resolved-act verb counts, docket and live commit moods after N seasons.
- **Status:** Code. Reading: evidence instrument.
- **Bears on:** CORE, SC.
- **Content that matters:**
  - `Counter(e.kind for e in w.log)` and `Counter(a.verb for a in d.resolved)` are the two measured surfaces (:19-20); `w.dates` and `commit_objects_mood` via `w.propositions[...].mood` (:25-27).
  - Docket truncated to first 40 items (:24) — all 28/20 fit.
- **Conflicts / stale:** `sys.path` line made relative after the run (docstring :3).
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/probe_matters_intake.py
- **What it is:** Read-only probe of what reaches a person's ledger and question set (questions by source, claim stems, record kinds, tenure kinds, opinion and pursuit spreads, capability/conviction counts).
- **Status:** Code. Reading: evidence instrument.
- **Bears on:** CHAR, CORE, SC, FI.
- **Content that matters:**
  - Projects `world_q.questions_for(w, p)` once at each season start, before CALENDAR/MATTER and without `since` (:26-35) — the doc's "faced" counts are a projection (:660-663 of the md).
  - Mislabelled key `stamped_class_on_first_question` stores referent ids (:34-35, docstring :4).
  - Opinion divergence over `world_q.FACTION_BY_PROP`; swallows `opinion_of` exceptions silently (`except Exception: pass`, :63) — the controls probe counts them.
  - Counts `p.capability` and `p.conviction` (:88-89) — the source of "capability 0 of 78".
- **Conflicts / stale:** `probe_controls.py` is the control for this probe's divergence claims; the silent except means an exception-prone `opinion_of` would show smaller n [UNVERIFIED].
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/probe_routes_hand_built.py
- **What it is:** Hand-built-bench-world probe of return routes 1-4 of the fold (uses `engine/season/tests/test_u7_remit.py` helpers `_world, _fold, _open, _determine, _kinds`).
- **Status:** Code. Reading: evidence instrument; depends on private test helpers, so it breaks if `test_u7_remit` helpers move.
- **Bears on:** SC, CHAR, FA.
- **Content that matters:**
  - Part A loops up to 80 acts until a Partial `matter.determined`; inspects holders of the determination claim, next-round Questions, disposal edges, judge pursuits (:24-47). Part B: per-band bystander `person_q.regard` and `person_q.legitimacy` before/after (:49-63); gives bystanders pursuits (justice .5, honour .3, liberty .2) so legitimacy can move.
  - Runs `d.witness(mint_token(w, WriteClass.INTERIOR), o1 + o2)` to fan out the round (:35, :59).
- **Conflicts / stale:** Part A loop variable `n` reused after loop (:30) — if loop runs all 80 without break, A_act_id is 79 [UNVERIFIED]. Only Partial and Success reached in 80 tries (md :594).
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/social_contest_stress.py
- **What it is:** Stress harness (2026-10-30) for the live social-contest module `modules/social_contest/roll.py` and the evaluated kernel; sections suites, edges, module, kernel, props; time-budgeted, JSONL audit log.
- **Status:** Code. Reading: historical instrument (produced `2026-10-30-stress-log-social-contest.jsonl`).
- **Bears on:** SC, DICE, PROCESS.
- **Content that matters:**
  - Edge grids for `SocialContestInput` fields (pool -1..10,000; opposition None/neg/1e9/inf/NaN; ceiling incl. `OB_MIN-0.5`; leverage ±100/NaN; rooms; forgery) (:64-71); invariants checked: same seed same result, global RNG untouched, `ob` never above ceiling, undocumented exception on finite input (:74-125).
  - `module_stats` checks monotonicity of success in pool, leverage, opposition with Wilson intervals (:137-165).
  - Kernel fuzz over `sc.PROCEEDINGS × POLICIES × CANONICAL_ADJUDICATORS` including `Panel` of sizes 1,2,3,9 (:174-257); API edges: empty panel, bad policy, unknown names (:260-283); symmetry/position-bias per proceeding (:286-327).
  - Suites runner shells out to pytest for `engine/tests/test_contest_kernel.py`, `test_social_contest_module.py`, `test_sc01_obstacle_ceiling.py` (:330-344).
- **Conflicts / stale:** Names a test path that does not exist in first attempt (md :68). Kernel sections die when the kernel is deleted. Uses `hash(...)` seeds (PYTHONHASHSEED-dependent).
- **Open items:** None.

### proposals/2026-10-29-parliament-and-debate/stress_p1.py
- **What it is:** Stress harness for P1 "One draw, one roster" (960 lines); sections leg, model, chan, regard, bench, dom, kinds, pace, fail, extremes, real, equals; also `--rollcall` log summariser.
- **Status:** Code. Reading: historical instrument; its MODEL records (`Dice`, `Obstacle`, `Leverage`) are a model of P1, not code.
- **Bears on:** SC, DICE, CORE, CHAR.
- **Content that matters:**
  - `model_ob` composes via the live `sc_roll.obstacle`, with aptness added where forgery enters (:89-94); `closed_form_margin` is the armature's D.1 (:103-105); "real" functions used: `p_success`, `net_boost`, `roll_net_continuous`, `soft_cap`, `degree_from_net`.
  - Legitimacy L measured over `build_realm` seeds 0-2 as share of residents with live `commit` to `fac_crown`/`fac_church_of_solmund` per territory (`wq.enclosing_territory`, `wq.residence_of`, `wq.members`) (:114-197); T9 circularity measured via `wq.judging_set`.
  - Regard test: `V.align_kind` over `matter.carried/advanced/held/turned` identical across bands; judge-model deposits a firsthand deed claim then compares `pq.regard` (:415-496).
  - `sec_failure` uses `test_u7_remit` helpers for open_case×{1,2,5,50}, revoked seat, killed judge, vacated seats (:698-762); `sec_extremes` gives the S27.4 grid (`ob > 2*max(N,0)`) (:777-798).
  - `sec_void_appeal` is a stub delegating to `stress_p1_void.py` through env `P1_WT` (:765-773).
  - `rollcall()` emits the markdown roll-call used in the stress report (:904-921).
- **Conflicts / stale:** Dead code: the "control" in `sec_legitimacy` counts residents in a loop (`ok += 1`) and plants nothing (:175-183); `sec_bench` has a precedence-fragile expression `if off is None or not wq.sits_over(...) if hasattr(wq,'sits_over') else False` (:525); `sec_regard` only separates decided flips after a noted artefact. The evidence-density metric counts attributed deeds, not P1's actual "evidence".
- **Open items:** `person_q.legitimacy` revert arm unmeasured (:196).

### proposals/2026-10-29-parliament-and-debate/stress_p1_b1.py
- **What it is:** Harness applying P1's first batch B1 "delete" to a scratch git worktree in cumulative phases (P0, P1a, P1b, P1b2, P1b3, P1c, P1d, RUN) and running 31 test files per phase in parallel.
- **Status:** Code. Reading: historical instrument; edits only the worktree.
- **Bears on:** SC, CORE, PROCESS.
- **Content that matters:**
  - TESTS list (31 files) is the practical dependent-set for the kernel, `VERB_CAPABILITY` and arrangement-key deletions: `engine/tests/test_contest_kernel.py`, `test_sigma_leverage_parity.py`, `engine/season/tests/test_season_shape.py`, `test_arrangements.py`, `test_sc01_*`, `test_sc02_*`, `test_u7_remit.py`, `test_u8_cast_fields.py`, and 15 `tests/valoria/*` files (:19-49).
  - Edit functions encode what P1 B1 means: regex deletion of `reception/reception_gain/proofs/proof_step` fields and `roll.py` room term, deletion of `_UNREAD`/`reception`/`proofs` from `world_q.py`, removal of `bench_basis`/`records_dissent` need() blocks, `roll_net`→`roll_net_continuous`, `VERB_CAPABILITY = {}` (:119-197); generated JSON must be regenerated with `tools/export_sim_params.py --build` and `tools/link_values_pointers.py --build`, not hand-edited (:200-206).
  - `edit_p1b3` repoints `test_sigma_leverage_parity.py` by AST-dropping defs referencing `CD.` (:209-225).
- **Conflicts / stale:** A phase P1c failure is recorded in the logs as a ValueError from the first `drop` implementation (harness fixed since). `NOX` global changed by `main()`; `run_set` mutates module-global `TESTS` (:78-88).
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_p1_b1_modules.py
- **What it is:** 26-line script run inside a worktree to check P1 B1's observable: `sys.modules` after one season holds no `systems.social_contest`; same-seed `content_hash` equal twice.
- **Status:** Code. Reading: instrument; result was NULL ("already true at HEAD") per the P1 stress.
- **Bears on:** SC, CORE.
- **Content that matters:** builds `build_realm(0)`, one season with `P.SUBSIST`, records `w.content_hash()` and loaded `systems.social_contest*` modules, twice (:14-23).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_p1_void.py
- **What it is:** Harness testing P1's `void` appeal in a scratch worktree: edits `_DISPOSES_LITERALS` in `engine/season/data/arrangements.py:68` and appends an `appeal_to_crown` row (`disposes: void`) to `arrangements.yaml`, then re-runs itself as a child with `--child`.
- **Status:** Code. Reading: instrument; historical.
- **Bears on:** SC, FA.
- **Content that matters:**
  - Child trials: loader accepts the void row; `open_case` under the void row is `case.refused` since `void` not in `G.DISPOSABLE_KINDS` (`effects_information.py:362-363`); hand-planted void docket item gives `determine.refused`; second seat's `pardon` cannot close the lower bench's `detain`/`ban` (`effects_governance.py:335-349`) while the lower seat's own pardon can (:59-110).
  - Adds `Office('off_court','Judge','R',['determine','issue'],faction='Crown')` and a `Tenure('t_court','p_king','off_court','hold',since=0)` for the appeal seat (:86-87).
- **Conflicts / stale:** Appended row carries keys `bench_basis`, `records_dissent`, `venue_min_rank`, `appeal_basis` that P3/P4 delete; first run's lower-bench draw opened no restraint (closure test vacuous, kept as `unverified`).
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_probe.py
- **What it is:** Shared stress probe for the season-loop debate surface (`Log` JSONL class, `git()`, `make_world`, `run_seed`); imported by every other harness here.
- **Status:** Code, "Nothing here is a gate". Reading: live helper for this folder's harnesses only.
- **Bears on:** CORE, SC, PROCESS.
- **Content that matters:**
  - Defines the single JSONL log shape (one fsynced line per event) reused by all stress harnesses (:40-47).
  - Stop rule is first of crash / quiescent (no event gained) / wall-clock budget; no chosen horizon (:9-14, :95-110). `WATCH` event kinds list (:30-33). Sweeps `fixtures.sweep('question_aggregation_rule', rule)` and `'bench_quorum'` (:57-63).
  - Imports from `engine.season.harness.populated`: `build_realm, make_chooser, SeasonDriver, resolvable_verbs, H, draw_factory, P` (:27-28).
- **Conflicts / stale:** `season()` call passes `subsistence=P.SUBSIST` here but the later probes (`probe_*`) omit it — a signature drift between harnesses [UNVERIFIED which is current].
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_p2.py
- **What it is:** Stress harness for P2 "Staged proceeding" (1618 lines): `model` (exact Markov-chain DP over real band probabilities), `world` (real-code probes on `tiny_world`/`build_realm`), `batches`/`batches2`/`batches3` (S1/S4 edits applied in a scratch worktree with pytest per file).
- **Status:** Code. Reading: historical instrument; `SCRATCH` is a hard-coded path under another session's scratchpad (:34) so `batches*` cannot be re-run as-is.
- **Bears on:** SC, DICE, CORE.
- **Content that matters:**
  - Exact net pmf from the die rule `DIE = {-1:.1, 0:.5, 1:.3, 2:.1}` (:62) with `net_pmf` convolution; `bands()` grades via `DE.degree_from_net(k + net_boost(lev,pool), ob)` (:82-90) — control against `DE.roll_pool` MC at five cells (:99-113).
  - `chain()` is the author's model of P2's flowchart transition table (admit/forum/plea/proof/quality/judgment; Partial detours, Failure ends at admit/proof); `S274_refused(pool, ob) = ob > 2*max(pool,0)` is a RE-STATEMENT of `sigma.py:273`, not an import (:124-125, docstring :13).
  - Plea payoff model with severity scale O 1.0/S 0.75/P 0.35/F 0 and season cost; reward routed 'pre' (through `obstacle()`, clipped by ceiling) vs 'post' (:461-558).
  - `world`: w1 case-file lifecycle (declared stages, holder gap, burn, forge, `create_record` overwrite of agenda, seize via `S12._hold_document`), w2 forum/second case/eight rows, w3 failure injection, w4 realm data (`judging_set` reach per rung kind; King/Queen on benches), w5 seasons (falsifier) (:782-1283).
  - Batch edits are exact-text patches of `effects_information.py` (`_mint_document`, `_eff_open_case`, `_docket_item` key `case`), `arrangements.yaml` / `data/arrangements.py` keys and `seam/ladder.py` fallback and `seam/contest.py` `extension` param; pinned-hash constants hard-coded: seed 0 one-season `873525dfb363231695cefb17ad4b17a1`, seed 1 `3c6c0de3…`, seed 2 `07a0c784…` (:1131, :1595).
- **Conflicts / stale:** `cite_check` list gives the line numbers P2 cited; seven missed (see P2 stress). Hard-coded PIN hashes will be wrong after any output-moving change. The pool in the model is rounded `int(round(pool))` (:68) matching live `roll_net`, not the continuous path P4 wants.
- **Open items:** none beyond the stress report's.

### proposals/2026-10-29-parliament-and-debate/stress_p3.py
- **What it is:** Stress harness for P3 "Authority first" (1545 lines); decorator `@guarded` sections A, A2, B, B2, C, D, E, F, F2, G, G2, H, H2, H3, Q1hash, S1, S1b, S2, S4, S5, S6, S7, S7b, notes, skips, verdicts; defines its own `Log` class (does not import `stress_probe`).
- **Status:** Code. Reading: historical instrument; sections G2/S4 read the committed logs `…-p3-authority-seasons-s{0,1,2}.jsonl` by path, so they fail if those logs move; H needs env `P3_WORKTREE`.
- **Bears on:** SC, FA, CORE, CHAR.
- **Content that matters:**
  - Legitimacy formula verbatim: `L_from(mean_op, opinion_full) = clamp01(0.5 + mean_op/(2*opinion_full))`; `clamp01(NaN)` returns 1.0 in Python (`min(1.0,nan)`); built over `world_q.opinion_of(w, p, faction_prop_id(f))` for four factions with the territory-ancestry grouping (:105-137).
  - `BY_FACTION = {Crown/Hafenmark/Varfell: polity, Church of Solmund: church}`, everything else `parties` (:254) — the model of P3's `authority.by_faction`; seat grouping recomputed from `engine/season/offices.yaml` via `rosters.office_faction(body, faction)` (:257-313).
  - `Patch` context manager monkey-patches `gate.may_determine`, `world_q.judging_set` and the copies imported into `effects_information` and `world_q` — evidence that `may_determine` is bound at three import sites (:557-603).
  - Real-season tee: wraps `d.resolve` to count attempted acts per verb and event kinds; royal set = holders of realm-rung `Crown` seats (:460-545).
  - F5 test: `evade / defy` on the `open_case` Record; case file is kind `text` held by the opener (:812-826). `sec_S6` uses `f.w.write("exists", …, driver="Event", emits="person.died", causes=[ROOT])` to remove a person under AX-4 (:1095).
  - `sec_H` encodes the C1 deletion edits as exact-string patches against `data/arrangements.py` (keys `bench_basis`, `appeal_basis`, `venue_min_rank`, `records_dissent`) and `world_q.judging_set(..., matter)` (:1264-1309). H3: 57 occurrences of the four keys in engine/ and tests/ (:1458-1472).
- **Conflicts / stale:** Labels weak dominance "strictly" (corrected in `sec_notes`, :1402). `sec_S1` comment claims "NaN poisons p_success"; corrected in `sec_S1b` (:1183-1186). `sec_G2`'s nested double-open of the same log file per `matters_sample` line is quadratic but harmless. Hard-coded claimed L tables `CLAIMED_CHURCH/CROWN` (:101-102).
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_p4_choices.py
- **What it is:** Model harness (1216 lines) computing whether P4's ten player choices survive a Pareto-dominance and "ever best under a weight grid" test at pools 2/5/12; sections C0, C3, C3b, C1, C2, C2b, C4-C9, C10 (characters from attributes), C3c (P2 control), C3d (grace). Default log `2026-11-01-stress-log-p4-choices.jsonl`.
- **Status:** Code, "MODEL, not code". Reading: historical instrument; it imports only `engine/dice_engine` (`sigma_leverage.p_success`, `roll_net`, `roll_net_continuous`, `net_boost`, `soft_cap`; `degree_from_net`), nothing from `engine/season/` (:3-8).
- **Bears on:** SC, CHAR, DICE.
- **Content that matters:**
  - Pure model constants: `SEV = {3:1.0, 2:.75, 1:.35, 0:.10}`, `WEIGHT_GRID` (1,944 weightings), `HEADLINE_W = sev 1, stand .1, time .03, rel .1, keep .05, names .25` (:43-44, :249-307); bench fixed at 5D (`BENCH`, :308).
  - `ob_of(score, ceiling, mod, apt)` implements P4 departure D-1: `min(score/2, ceiling) + mod/2 + apt` so modifiers escape the ceiling (:90-97); S27.4 `ob > 2*max(N,1)` treated as held Failure and logged `blocked` (:100-108).
  - `stage()` implements repair (e): Failure holds up to `tries=3` and the third closes against the roller (:115-125); `hearing()` encodes plea semantics: deny→fact tried, concede_fact→definition (cap 1 grade), justify→respondent's roll (cap 2) (:148-191). Caps are applied to the grade after `degree_from_net`, i.e. outside the ladder (critic finding 5).
  - Capability layer: `FACULTY_MAP` for three attribute rosters (registry nine, scratch fourteen, scratch eight), `ROLE_WEIGHTS` per rite/role, `SPEECH_FACULTY`, `DICE_PER_FACULTY = 1.25`, `faculty()` as "the ONE OWNER of attribute -> faculty" (:902-952); characters commoner/advocate/scholar/average with hand-authored sheets (:914-927).
  - Defiance model: church-row contempt ban bite is zero in the model (`contempt_sev` multiplied by 0 for kind ban) (:449) — the critic's finding 7 (church contempt costs 0).
  - Known false starts kept: run-4 in-section control degenerate; superseded by C3c (:1136); `strong_when_needed` and `weak_now` cut (:579-580).
- **Conflicts / stale:** Every figure in P4 §4 is from this model, not from code. `defy_cell` hidden-state `q` is visible by construction ("favours the chooser", :463). `sec_characters` uses a no-op `"scholar" if False else "average"` (:976). Hard-coded `DEFAULT_LOG` path inside the proposals folder (:39).
- **Open items:** none.

### proposals/2026-11-04-content-parameters-docket/01_characters.md
- **What it is:** Chapter 01 of the content-parameters docket (lane IN, 2026-11-04): a collation of every parameter a character/NPC needs, with domain, required/optional, what exists now (HAS/STUB/NONE) and which code or plan calls for it; plus a complete 46-NPC + 37-cohort roster appendix.
- **Status:** "PROPOSED (2026-11-04). Collation of what code and the active plan call for; reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing." Reading: live as a measured snapshot (counts loaded from YAML on 2026-11-04); `00_MASTER_DOCKET.md` (not in this assignment) holds the legend.
- **Bears on:** CHAR, CORE, ARCS, FA, PC, WR.
- **Content that matters:**
  - Named cast: 46 rows in `references/npc_registry.yaml` (35 canonical, 11 proposed; only canonical seat an office, `populated.py:1615`); identity/pursuits/affiliations/faction/role authored 46/46, everything else thin: `age`/`born` 0/46, `weight` default 1, `body` default 1000, `stats` 1/46, `capability` 1/46 (NPC-088 `{copying:3}`), `ts` (thread sensitivity) 10/46 so 36 cannot attempt `thread_read` (:16, :58-68).
  - Pursuit weights for all 46 are flagged `[ASSUMPTION; medium; Jordan to correct]`; pursuit names ruled are `doctrine`/`stewardship`, the 2026-09-20 worksheet says `faith`/`warden` (code wins) (:34, :72, :127).
  - Closed sets Jordan must populate: 15 pursuits, 7 axes (15x7 projection, 89 of 105 nonzero), 5 affiliations (scale 0-5), 9 attributes (+1 unnamed, J-T2), 6 role templates (Guilds/Schoenland/Altonia have none so `loyalty` returns None), 1 capability key `copying`, 14 thrust axes, 7 faction leaders (:297-316).
  - Attributes have no carrier on `Person` (plan CR-20); four vocabularies coexist: registry nine, `Combatant` 8 args (`modules/combat/combatant.py:93`), cast `stats:` {cognition, focus, endurance, social}, held proposal's six (:177-194).
  - Cohorts: 37 population cohorts all `weight: 2` (smallest legal; H-170), 16 territory temperaments (alpha/beta in [0,1], T15 absent), 3 guard cohorts; cohort convictions HELD (ED-IN-0296) (:80-104).
  - Goals: 38 goals (faction 20, body 16, seat 2); thrust `axis` and `goal_stages` loader-supported with 0 rows authored (CL-THRUST) (:133-159). Kin/bonds, heritage (5), lifepath (34), kit/tradition, player-character creation and named-NPC arc content have no carrier: EMPTY/PLAN (:217-293). Arc: `arc_trajectory` free text on 36/46, no code reader (:284-293).
- **Conflicts / stale:** `NPC-081`/`NPC-082` faction cells unquoted so YAML drops the seat number (reported by `cast.defects()`) (:71); `cast.py` docstring says `ts` on 32 rows vs 10 measured (:73). Key-format re-check: temperament alpha/beta sourced from archived Key-substrate doc but read by live code (:434).
- **Open items:** the tenth attribute name (J-T2); every per-person attribute value; vocation->attribute rows; the 34 lifepath rows; kin/bond carrier decision (J-T3).

### proposals/2026-11-04-content-parameters-docket/03_geography_territory.md
- **What it is:** Chapter 03 of the content-parameters docket (lane IN, 2026-11-04): geography and territorial hierarchy parameters, measured by loading `systems/settlements/valoria_geography_v30.yaml` (G) and `engine/season/cohorts.yaml`, with a reader audit (UNREAD / NO-READER) per key.
- **Status:** "PROPOSED (2026-11-04). Collation … reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing." Reading: live as a snapshot of which geography keys code actually reads.
- **Bears on:** SE, MB, WR, CORE, FA.
- **Content that matters:**
  - Rung kinds are a closed set of eight `[person, hearth, community, settlement, territory, province, duchy, realm]` (`rosters.yaml:267-270`); province is DERIVED by `world_q.provinces_of` and not minted; the duchy-to-faction map is a literal tuple in `populated.py:1004-1007`, not a registry row (:13-29).
  - 17 territories (key is `provinces:` in G but rows are territories); read fields: `faction` (populated.py:1025,1441), `anchor` (`modules/mass_battle/terrain.py:181`), temperament `alpha`/`beta` for 16 (T15 none); UNREAD: name, region, sub, description, polygon, settlements list, `fort_level`, `proximity_calamity`, `spiritual_weight`, `starting_pros` (:31-52). CR-40 proposes deleting `starting_pros` x17.
  - Territory adjacency 26 edges read by `adjacent_territories()`; settlement adjacency 55 edges (road 54, sea 1) and the whole terrain cost matrix, vision_range, march_budget, lakes, bridges, forgetting_zone, `radiation_bands`, altonian_passes, scale anchors have NO reader; planned readers CP-T10-01 (route pricing) and CP-T10-02 (BFS band from T15) (:60-136).
  - 20 terrain polygons (8 types mapped by `terrain.py _TYPE_TO_ROW`; unlisted type -> OPEN_FLAT; `fjord_coast`->FOREST_BROKEN and `coast`->OPEN_FLAT by assumption, terrain.py:49-66) (:105-118).
  - 37 settlements: types Town 15, Village 14, Seat 2, Fortress 2, City 2, Fortress-City 1, Cathedral-City 1; `controller` key UNREAD (code reads territory `faction`); `stats` [Prosperity, Defense, Order] triplet UNREAD in engine/modules/tools (:73-89). POI catalog counts only (31 POIs, no names; ED-507 wants 2-6 per territory) (:138-147).
  - Foreign seat: one row (Altonia: territory code `ALT`, settlement `ALT-1`), flagged `[ASSUMPTION]`; homeland place names owed (:149-160).
- **Conflicts / stale:** G header says both "PROVISIONAL" and "CANONICAL"; G footer cites `designs/...` (dissolved tree); `terrain.py:134-137` records that G's `fort_level` disagreed with live `world_q.fortification_of` for T2; CR-40 claim of `starting_pros` disagreeing with retired `params_tables.yaml:6576` in 11 of 17 is UNVERIFIED (:57).
- **Open items:** Piety Track start for T16 and a split rule for the bipolar track (SE-06 HELD, B10-Z); a `province` threshold (none stated, `world_q.py:2186`); named POIs; Altonia homeland names.

### proposals/2026-11-04-content-parameters-docket/04_events_decks.md
- **What it is:** Chapter 04 of the docket (lane IN, 2026-11-04): events, decks, weather, storylines, endings, narration; scope narrowed mid-task (clocks/thresholds/threadwork belong to another chapter).
- **Status:** "PROPOSED (2026-11-04). Collation … merging ratifies nothing." Reading: live as an inventory; mostly records absence.
- **Bears on:** WR, CORE, ARCS, GO.
- **Content that matters:**
  - No event-deck or card carrier exists anywhere in code: `engine/season/tensions.yaml`, `data/tensions.py`, `scenarios.yaml`, a `tension_effects` roster and a `territory_yield_scale` fixture do NOT exist (grep 0) (:11-14). Tensions cards (6 drafted, draw 1 at build; Royal Crisis, Feldmark Famine, Cardinal Independence, Guild Fracture, Einhir Incident, Ministry Crisis) are PROPOSED-ONLY in `proposals/2026-10-28-content-architecture-suite/08_decks_and_template_in_engine_form.md` with plan CL-EVENTS commit 3 (B10-18) unbuilt (:30-42).
  - Goldenfurt deck: 28 cards, 12 of which have no engine form; opening build HELD on M26 (CL-OPEN, B10-19) (:44-57). Scenario rows (~60 per A5) planned in `scenarios.yaml`, refused keys: fires_at, outcome, deadline, standing/stance/tenure writes (:59-70).
  - Weather: `season_factor=1.0` (base) and `season_factor_draw=()` (control, shipped off) in `data/fixtures.py:494-500`, read by `world_q.py:1055-1120` (`season_factor_of`); `year_length` does not exist (grep 0) (:72-82).
  - Endings: `rosters.yaml: endings` has 2 members (peninsular_sovereignty victory:true, theocracy), read by `world_q.endings_reached` (:2366); no loss states; GD-1 clauses (Accord, Stability, sustain 2 seasons, treaties) uncarried; "Nothing halts on a reached ending" (:84-93).
  - `ENDINGS_CLASSIFIED.yaml`: 50 agent-classified rows (DECIDER 20, NEVER 10, ROLL 9, THRESHOLD 8, UNCLEAR 3; 19 forced by threshold), arcs 46-55 unclassified (:95-103). Case corpus `engine/season/cases/`: 54 ARC ids, 46 NPC ids, "never runtime data"; `ends_when` is prose that code evaluates none of (G-25) (:105-114).
  - Narration: `harness/chronicle.py` partly landed (NM-W1); NM-W4..W9 unbuilt/held; 0 authored fragments (:116-127).
- **Conflicts / stale:** A5 says grounded deck has 58 cards, file has 10 distinct `EVT-` ids; A5 says weather constant at `world_q.py:945`, actual owner at `:1062`; `chain/NPC3.yaml` fails `safe_load` (backtick) (:114).
- **Open items:** all event/tension/scenario content; year length and seasonal multipliers (Jordan sets); loss-state endings; classification of arcs 46-55.

### proposals/2026-11-04-content-parameters-docket/05_clocks_threadwork.md
- **What it is:** Chapter 05 of the docket (lane IN, 2026-11-04): clocks, timers, thresholds, conditional arcs, thrust axes, conviction tracks, threadwork and scale transitions; 98 parameter rows, with Key-retirement re-checks and a follow-up section.
- **Status:** "PROPOSED (2026-11-04). Collation … merging ratifies nothing." Reading: live inventory; rows marked RETIRED-KEY are dead sources.
- **Bears on:** WR, CORE, CHAR, FA, ARCS.
- **Content that matters:**
  - There is NO authored clock/track registry; the loop says "NO CLOCK GENERATES ANYTHING" (`loop/census.py:39`); only licensed fixture-driven clocks exist: matter wear (`wear_per_season.rates`, harbour/seam/body 10, others 0), Tenure `term` (`oblige_term` 4), claim decay (`claim_decay_per_season` 5), bodies (`body_step` 10, `age_step`/`illness_rate` ship 0), weather (`season_factor`) (:12-40). `matter.py` header counts "three" licensed clocks while bodies is a fourth (:50).
  - Dates are runtime-minted by `_eff_convene` (`effects_governance.py:409-456`); `World.dates` starts `{}`; cards/arcs may not carry dates (T-c) (:56-76).
  - Thresholds are fixtures/rosters/module constants only: `band_floors` per site kind marked "INVENTED" (H-08), `standing_band_floors (500,)`, `hunger_band_floors (1,2)`, scar thresholds 2/3 ruled (scar threshold 1 has no reader), `thread_sensitivity_gate` 30 `[ASSUMPTION, H-239]`; crossings emit Events and "MAY NEVER PRODUCE AN OUTCOME" (L5, `matter.py:79`) (:80-105).
  - Conditional arcs: `goal_stages` schema built (`data/goals.py:379-463`) with 0 rows; `axis:` on 0 of 38 goals; struck keys deadline/closing/successor/deal; B4.x docket-crossing and B6.n ladder content HELD (:109-138). Thrust axes roster: 14 members (10 user axes + 4 poles), 6 `opposes` pairs (:142-155).
  - Conviction tracks: 5 affiliations; `incompatible` half-matrix 5 of 10 pairs filled, 4 altonian pairs null "no source"; `affiliation_engagement` table read for sign only (:159-176).
  - Threadwork: a Python sim `systems/threadwork/sim/` (7 files) is `wiring.build: unwired` (`module_contracts.yaml:300-323`); the loop's only carrier is `Person.thread_sensitivity` (ts non-null 10/46; never written in play); `thread_read` requires TS >= 30 and writes nothing; no `Person.coherence`; no verb opens thread operations (:18, :180-210, :243-258). Constants in the sim (DEPTH_OB, COHERENCE_COST_BY_SCALE, ELASTIC_RANGE 6 etc.) are tagged `[JUSTIFIED ... invented, ED-WR-0010]` (:192).
  - Follow-up grep of threadwork sim for Key-substrate use found none; so sim constants are not RETIRED-KEY (:235).
- **Conflicts / stale:** `thread_sensitivity_gate` 30 duplicated in `DEPTH_TS_MINIMUM` of the sim (two owners, same number) (:102); `rosters.yaml:2779` lists threadwork `loop_resident` while contract says `unwired` (:207); `module_contracts.yaml:542` and `mechanics_index.yaml:140` call `ms_track` the "live tick" but it has no importer (:49); `SEASONS_PER_YEAR` vs `season_factor_draw` length — two owners of the year (:48); `affiliations` roster note says "count 4" vs 5 (:175); thrust design speaks of `ladders:`/`deadline` which code lacks (code wins) (:135).
- **Open items:** whether any authored clock registry is wanted (no position calls for one; M16 fourth motion "CONFIRMED AT THE DEFAULT" off); `age_step`/`illness_rate` magnitudes unruled; all threadwork host work (CP-T07-02..11) unbuilt; Calamity has no source in realm (G-21); tenth attribute J-T2.

### proposals/2026-11-04-content-parameters-docket/06_personal_combat.md
- **What it is:** Chapter 06 of the docket (lane IN, 2026-11-04): personal combat content/parameters — abilities, attributes, skills, levers, 54 weapons, armour, traditions, combatant record, 205 cfg keys, vocabulary — plus a complete actions/choices table (§15) of every entry point and in-bout decision site in `modules/combat/`; 132 rows.
- **Status:** "PROPOSED (2026-11-04). Collation … merging ratifies nothing." Reading: live measured inventory; §16 Key-retirement re-check found no Key-only sources.
- **Bears on:** PC, CHAR, CORE, MB.
- **Content that matters:**
  - The season seam passes the combat engine ONE field per party, `end` (= `max(1, 4 - body_band_penalty)`, `seam/wrappers/combat.py:130-153`); every other `Combatant` field is the class default; `PersonalCombatInput` = claimants, ends, wound_quantities; no `terms` field on the input (`fight.py:52` getattr default) (:10).
  - Chosen by the ENGINE, not a player: 0 player-selectable options in the module today; all in-bout choices (initiative, grip, facing, mode/head selection, half-sword, approach, stop-hit, disengage, aggressor, commit depth from a Beta draw, lunge, read contest, parry/dodge/wind, indes counter, attack roll via `core.resolve(pool, net_sigma, rng, ob)` with pool = max(5, History+6), bind, percussion stagger, grab outcomes disarm/throw/pin/control/foot_pin/escape) are seeded-rng/sigma-resolved (§15b, :286-315). Duel-mode player intents at six open moments are PROPOSED-ONLY (05_two_modes_of_one_bout.md).
  - Scene-level externally supplied choices exist only at the wrapper: `terms` {yield, blood, death} default death (LETHAL_TERMS) — result 0 = UNRESOLVED; Yield declaration with 95% UPSET_FLOOR flip applied to decided results; `max_bouts` default 12 (:272-284).
  - Rosters: 9 abilities (`ability_primitives.py:29`; 15 lever names read at call sites with no owner roster, 8 levers have no ability), 8 traditions (chinese, filipino have 0 abilities), 54 weapon records (50 base + 4 half-sword), armour as 4 tiers → 4 materials with code tables only (no per-item armour, no shield/ranged/mounted/formation record anywhere), 6 skill axes as call-site literals (`bind, grab, technique, balance, parry, dodge`) (:16-200).
  - `combat_engine_v1.json` typed export: `cfg` 205 numeric keys + `core` 25 keys, no `attributes` section (PC-14 unbuilt; `modules/combat/attributes.py` absent) (:12, :221-229). `Combatant` attribute defaults (strength 4, agi 4, end 4, cog 3, att 3, spirit 3, focus 3, history 3, disp 4) are STUBS; WoundTracker constants hard-coded in `combatant.py:17-27` (:43-63, :226).
  - Wound persistence between engagements is PROPOSED-ONLY (M-3); `body_ceiling`/`tend`/marks (CP-T03-07/08) unbuilt (:254-258).
- **Conflicts / stale:** `weapons.py` header says "53-weapon roster", measured 54; `ability_primitives.py:19` docstring "TWO populated morphology levers" stale; traditions/tradition.py comments describe a retired imposition gate (PC-16); `combatant.py` header cites design doc `derived_stats_v30` (reference only, code is the formula); PC-14 "about 44 reads" vs measured tally not reconciled.
- **Open items:** PC-14 attributes spec + schema bump; PC-17 21 generic abilities and `INIT_TEMPO_LEVER_K`; CP-T03-03 `arms_kinds`/`kits`/`arms_at_build` (JQ-2-gated); PC-10b `terms` on the input; whether `att` = Attunement or Attention (J-T2); the six skill axes have no declared closed set.

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR337.md
- **What it is:** Reading log of PR #337 (merged `d73b5d3`, 2026-08-27): an "architecture log" of 255 rows plus vocabulary, verification table, Godot scan, overlap and open-question sections, for the Systems Integration Master (4 parts) and Game Precedent Companion (2 parts). A session-provenance artifact, filed under `_session_provenance`, not design.
- **Status:** No Status line (a PR log); the log says both source documents are FILED reference that ratify nothing (ED-1094). Reading: historical; its claims describe the tree at commit `f567c13`/2026-08-28, before the Key substrate was retired (ED-IN-0232) and before the season loop (`engine/season/`) existed as the head, so most code claims are STALE.
- **Bears on:** PROCESS, FA, SE, CHAR, MB, PC, SC, FI, WR, CORE.
- **Content that matters:**
  - Headline measured distribution over 338 classified architectural things: BUILT 32%, DESIGNED 30%, PROPOSED 15%, INERT 13%, RULED-UNEXECUTED 6%, built-with-defect 4%; "the code exists, is correct, and nothing calls it" is as large a bucket as the whole proposal corpus (:19-22, A337-220).
  - Central finding then: the game "resolves without any people in it" (`world.npcs` empty in every seeded campaign), the "highest-fan-out blocker" (later ruled via ED-IN-0201 per the log); 8 of 8 lanes' cheapest fix was "a writer, not a mechanic" (F1/F2, A337-221/222).
  - Obstacle taxonomy U/SO/DO/BI (Unopposed, Statically-opposed, Dynamically-opposed, Bilateral): only 2 DO mechanisms in the tree (Contested Investigation, `rebut`); score/2 obstacle ruling executed at one site (A337-007/008/035/195).
  - Defects named then: Muster Wealth cost off by 100× (`adjust('W',-1)` / `MULTS['W']=100`); Total Victory rider permanent not one-season; `Faction.standing` mutated at 11 sites outside `adjust()`; Turmoil clause of Peninsular Sovereignty always-true; `InsurgencyRecord.L` never rewritten so promotion is unreachable (A337-051/064/097/134/136).
  - Methodology: ED-IN-0027 disposition ladder KEEP/REFINE/DISTILL/MERGE/PRUNE/CUT judged as-if-built; no subtractive verdict final until steelmanned; NERS gate (P-i legible odds ... P-v right engine); four rival integration proposals (P1 Close the Circuits, P2 Three Primitives, P3 The Disposal, P4 A Person's Season), recommended order P3→P1→P2→P4 (A337-232..247). Two instrument rules: reachability is not an import graph (deps resolved by string), and agreement across surfaces is evidence only if independent (A337-036).
  - Nine code claims verified true on the 2026-08 tree (TN7 refusal, Faction fields, `TAG_KINDS` closed 5 with `Leverage` not `Compact`, `Key.scale_signature`, etc.) (:347-371).
- **Conflicts / stale:** Rows resting on the Key substrate (`engine/substrate/keys.py`, echo transport, `TickScheduler`, `key_types.json`, accord-echo, `articulation`) are RETIRED (ED-IN-0232, CLAUDE.md §0); `systems/*/sim/` paths for factions/settlements/world are dissolved ("`sim/` dissolved", CLAUDE.md §3); rows citing `params_tables.yaml` rest on a retired file. The single-owner degree-ladder test and `dice_engine` facts remain live (cf. P1/P2/P3 stress). `confidence.broken`/`registry`-era rows (A337-044..) are a taxonomy for a tree that no longer exists.
- **Open items:** The 12 open items at §8 (person schema, accord-echo rulings, `MULTS['standing']`, province-accord write model, scale vocabulary, parliament rider sign, 27 personal-combat probability gates unruled, "No commander, no battle" gate-or-penalty) — most superseded by the season-loop architecture; the PC probability-gate scope question (A337-199) and the mass-battle commander question (A337-205/208) are the ones nothing else visibly answers.

---

## Cross-subsystem leads

- **SC (primary), CORE, DICE:** The social-contest stress suite (P1/P2/P3 + attribution + P4 + fold doc) gives a single code-verified fact base: computed play never reaches `determine` (3 of 65 attempts executed in 24 seasons; `docket_named_arrangement` 0), `speak` writes nothing at any band, `comply`/`evade / defy` are emission-only and 100% `compliance.impossible`, `give` refused 7/7, `pardon` refused 8/8, `covenant` 17/17, `exchange` 106/106. The SC audit lane should start from `2026-10-31-stress-test-attribution.md` rows E1-E16 and C1-C8 and the fold doc §5.5 route table.
- **DICE, SC, PC, MB:** The continuous closed form `E[m]=0.4N+0.8√N·softcap(s)−Ob` is wrong below 1D (engine floors at 1D for mean and spread); the live `roll_net` rounds the pool (`sigma_leverage.py:284`) so `p_success` (continuous) and play (discrete) disagree by up to ~15 points at 2D; S27.4 (`ob > 2×pool`, `sigma.py:273`) refuses acts where R-16 says "priced, never refused"; NaN obstacle is never refused and grades Failure; ceiling 3 (G1/R-37) makes odds against an equal non-monotone (.45 at 1D → .38 at 6D → .98 at 30D) so the "world resists change" premise holds only for pools under ~7D. DICE and PC audits should check whether the PC action probability gates (27 `rng.random()` vs computed-probability branches, per PR337 A337-199) were ever ruled in or out of the doctrine.
- **CHAR, SC, PC:** Attributes have no carrier on `Person` (CR-20); four attribute vocabularies coexist (registry nine; `Combatant` 8 args; cast `stats:` {cognition, focus, endurance, social}; held proposal six). `capability` is authored for 1 of 46 named persons, 0 cohort; `VERB_CAPABILITY` is a 2-row map whose only key is `copying`. P4's `faculties:` table is the only worked design for attribute→dice (1.25D per faculty point puts faculty 4 at R-40's 5D); the critic says unauthored attributes default to 1, giving every person 1.25D unless defaulted to the R-40 reference.
- **FA, SC, CORE:** The authority concept (`parties`/`polity`/`church`) does not exist in the tree: a Senior Inquisitor opened a royal-row `legal_trial`; the King/Queen sit on 319 of 319 non-empty benches; church benches are empty for 74/83 homes; Hafenmark has no determining seat; `parties` bench empty for 83/83 so seeded `arbitration` can never be determined. The FA lane needs this for any institution-procedure claim.
- **SE, WR, FI:** Chapter 03/04/05 of the docket show geography is mostly authored-but-unread: only `faction`, `anchor` and `alpha/beta` of territories are read; settlement `controller` and `stats` triplet, all adjacency edges, terrain cost matrix, vision/march blocks are NO-READER; 31 POIs have counts but no names. Events/decks/tensions/scenarios have no carrier at all; weather draw is off; endings has 2 members and nothing halts on one; threadwork sim is unwired and no `Person.coherence` exists. SE/WR audits should treat these as "authored data without a reader" rather than missing code.
- **CHAR, ARCS:** `ENDINGS_CLASSIFIED.yaml` (50 agent-classified rows; arcs 46-55 unclassified) and the case corpus (54 ARC ids, 46 NPC ids) are labelled "never runtime data"; `ends_when` is prose. No executable arc content exists for named persons (`arc_trajectory` free text on 36/46, no reader).
- **GO/PROCESS:** Several harnesses here have hard-coded paths into another session's scratchpad (`stress_p2.py:34`) or into sibling logs (`stress_p3.py` G2/S4); reproduction would need those paths fixed. `stress_probe.py` is the shared log/helper imported by `stress_p1.py`, `stress_p2.py`, `social_contest_stress.py`, `lopsided_*`, `stress_p1_b1.py`.

## Likely stale or superseded

- `proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR337.md`: whole file (tree of 2026-08-28; Key substrate retired; `sim/` dissolved; factions/settlements/world `sim` paths gone). Its F1/F2 "absent person" finding was superseded by ED-IN-0201 and the season loop.
- `2026-10-30-stress-test-report.md` kernel sections and 13-season numbers: the kernel (`systems/social_contest/sim/contest/`) is slated for deletion (R-14) and the run was at `79b7defa` on Windows; the three per-proposal stress tests and the attribution doc supersede its season-loop conclusions.
- Line-number citations to `engine/season/loop/effects_information.py` in the stress reports and P4 (`open_case :301/:274`, second-case refusal `:341/:352/:367/:368`, `_eff_determine :419/:446`): the file moved (`_eff_open_case` is now at `:367`, the docketed decline at `:434`); P2's own cite check already found 5 misses by ~25 lines.
- Pinned hashes quoted in the reports (`873525df…`, `9e71dfe9…`, seed 1 `3c6c0de3…`, seed 2 `07a0c784…`, and moved variants): valid for `404e8023` only.
- P1/P2/P3 stress "what would be broken by proposal" conclusions: the three proposals are superseded by P4 (which keeps P3's authority frame and P2's stages); P4 itself is PROPOSED, not built, and its critic says it should not replace P1 as the base.
- Docket chapters 01/03/04/05/06: counts measured 2026-11-04 (e.g. 46 NPCs, 54 weapons, 205 cfg keys, 98 clock rows); re-measure before citing.
- `systems/overview/sim/ms_track.py`, Key-era `module_contracts.yaml` rows `:300-323` and `:542`: flagged RETIRED-KEY or no-importer in chapter 05.

## Items that could change an audit finding

- **F-PC-04 (plain `fight` kills 200 of 200) and the no-deterministic rule:** `06_personal_combat.md` §15 shows the combat module's `fight` has a `terms` choice defaulting to `death` (`LETHAL_TERMS`) and the season seam never sends `terms`; a duel/yield/blood alternative exists in `wrapper.py` (`DUEL_TERMS`, Yield, `UPSET_FLOOR` 95% flip) but is unreachable from the season. This is both a cause of F-PC-04 and a ready-made repair surface (PC-10b / CP-T03-09). Also: the seam sends only `end` (derived from body bands); every other combatant field is a class default, so all fights are between identical fighters except for wounds.
- **Deterministic resolution in SC (G-65 / `05_SC_evidence_and_rebuttal_B.md`):** P4's grade caps (concession lowers the grade by 1 or 2) rewrite the band outside `degree_from_net` (R-6, R-8), and P4's plea table rewards `deny/concede/justify` with fixed caps — a fixed function of state, against the standing rule; the critic (finding 5) says to test an obstacle-routed reward first. Similarly in the stress reports: "a Failure at admit/proof ends the file" (P2) and "defy strictly dominates" (P3) are deterministic or free-choice corridors; P4's model makes church contempt cost 0 (finding 7). The live code's `determine` on a bench gives graded Partial/Success draws (consistent with the rule) but `open_case` second-case refusal, `pardon` closure basis, `destroy_record` needing a hold, and MATTER maturing only at `due == tick` are fixed predicates (eligibility, allowed under the rule).
- **Any finding that says "`determine` works / the proceeding resolves":** the code path works on hand-built worlds (`test_u7_remit` helpers) but computed play executes it 0-3 times in 24 seasons and always as `matter.undetermined`; any audit claim of playability for SC must carry that.
- **Any finding on `Person.capability`/attributes:** 0 of 83 persons (and 1 of 46 cast) carry capability; `corpus_run.py:356` raises `SystemExit` if a cast capability key has no `verb_capability` row, so emptying `VERB_CAPABILITY` breaks `build_realm(0)` (P1 stress; P4 critic finding 11).
- **Any finding on "one code path / integrates with the loop" for SC:** the module is World-free and the live seam is `social_contest.roll` in `module_contracts.yaml:52-56` plus prize rows; the `social_contest` row near `:448-470`/`:464-486` is stale in its `sim_module` path but load-bearing (deleting it fails 54/65 `test_u7_remit`, 9/13 `test_sc01_speak`).
- **Any finding on legitimacy/standing as a "field":** `person_q.legitimacy`/`world_q.opinion_of` are computed per read (S-7 no magnitude carrier); opinion of `Schoenland` and `faction x` is exactly 0 for all 83 persons (no `expected` goals/engaged poles); 8 of 16 territories read exactly L=.50; seeds 0-2 are one realm (n=1), so any "three seeds" statistic in other audits is n=1.
- **Any finding that "events/clocks/threadwork exist":** no event/tension/scenario/deck loader, no `year_length`, no authored clock registry, threadwork sim `unwired`; weather draw `()`. (Docket ch. 04/05.)
- **Mass battle / FA / SE:** docket ch. 03 shows `fort_level` in geography disagrees with live `world_q.fortification_of` for T2; settlement stats triplet and controller are unread; PR337 A337-205/208 (commander gate-or-penalty) is unanswered.
