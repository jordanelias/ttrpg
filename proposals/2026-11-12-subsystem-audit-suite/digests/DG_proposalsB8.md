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
