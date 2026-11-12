# Digest audit1

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane scope: the surviving audit corpus under `.audit/` (lesser weight than `.designs/`; context and referents). Social-contest code now lives at `systems/social_contest/sim/contest/` (earlier audits call it `sim/personal/contest/`); the `designs/...` paths they cite are now `.designs/...` or gone. Reading note: bulk JSON/data files were read through a structure-aware dump (every field of every record printed, long strings truncated at about 260-330 chars) rather than raw; where a file is data-only the entry says what was sampled.

### .audit/2026-06-03-contest-groundup/engine.py
- **What it is:** 59-line Python module, 2026-06-03, "the shared stochastic core" copy of the base d10 + σ-leverage engine used by the contest ground-up rebuild (no author-lane stated).
- **Status:** none (module docstring says "verified 2026-06-02 against params/core.md ... Fixed; not tuned here"). Reading: historical (a frozen copy; the live owner is `engine/dice_engine/dice_engine.py` and `engine/dice_engine/sigma_leverage.py`).
- **Bears on:** DICE, SC
- **Content that matters:**
  - Base model: net ~ Normal(0.40·pool, 0.80·√pool) at TN 7; die map 1→−1, 2-6→0, 7-9→+1, 10→+2; Ob 1-20 (`:10-13`).
  - `OVERWHELM_SIGMA = 0.85`: degree-3 bar = pool mean + 0.85·σ to hold Overwhelming near 21% across pool sizes (`:14-15`, `:54-57`); pool-less call keeps the legacy `2·ob` bar (`:58`).
  - σ-leverage: `M_MAX=1.5`, LEVEL minor/moderate/strong/major = 0.25/0.50/0.75/1.00, `eff_sigma = M_MAX·tanh(dσ/M_MAX)` (`:18-23`).
  - `net_boost` is the resolution-path advantage (a μ-shift of `eff_sigma·sigma_N(pool)`); `effective_ob` is declared DISPLAY-ONLY post ED-884/ED-934 so the Ob floor is never breached (`:24-38`).
  - Degree bands 0 Failure / 1 Partial / 2 Success / 3 Overwhelming (`:47-59`).
- **Conflicts / stale:** `OVERWHELM_SIGMA` no longer lives here: `engine/dice_engine/sigma_leverage.py:120` says "OVERWHELM_SIGMA MOVED 2026-08-27 (ED-SC-0032)"; `MU_PER_DIE`/`SD_PER_DIE` now owned at `engine/dice_engine/dice_engine.py:181` and aliased in `sigma_leverage.py:118-119`. Degree banding is now `degree_from_net` (`dice_engine.py:236`), so this copy is a superseded second owner (still-live only as audit evidence).
- **Open items:** none.

### .audit/2026-07-01-contest-gate-a-packet/verdict_log.json
- **What it is:** JSON, 5 adversarial-judge rounds (2026-07-01) on the Stage-1d / Gate-A social-contest rebuild diff (CR1/CR2/CR3 fold-in: three trackers Concentration + Face + Persuasion, Composure retired, ED-1055/ED-1056).
- **Status:** none; every round ends `tests_green: True`, `escalate: None`. Reading: historical; most code findings fixed, the design questions superseded by later contest work.
- **Bears on:** SC, DICE, PROCESS
- **Content that matters:**
  - Method: a judge verifies each claim by grep/AST/running the CI validator (e.g. ran `tools/validate_ed_citations.py`, exit 1, 4 OPEN_AS_BASIS violations because `_is_resolved()` excludes `provisional`), ruling upheld / overruled / deferred with severity (blocker/major/minor/nit) and a `spawns_ed` stub. Rounds 1-5 at lines `:2`, `:76`, `:127`, `:161`, `:206`.
  - Blockers R1: `canonical_sources.yaml` absent from the changeset (`ci_co_file_checker.py` Rule 1) and the ED-1055 provisional-citation violations; both "local pass is false because nothing is committed" (`:5-15`).
  - Major R1: "Face" names two incompatible things: `params/contest.md` Face = Charisma×3 (3-21) Rattled strain buffer vs kernel `Face = Standing` (0-10, START 5, ethos-built, monotonic-up, `Standing.strip()` never called) (`:22-33`); R2 adds that they are oppositely signed (`:103-108`).
  - R1/R4/R5: the CR3 tracker layer (`Face` alias, `TRACKERS`, `RETIRED_TRACKERS`, `.face/.concentration`) has no resolution consumer, only tests; three-trackers `WIRED` over-states (`:34-45`, `:194-199`); the judge overruled the "decorative" charge in R2 (`:109-114`) and R4/R5 (`:165-169`, `:210-214`) because Standing/Reserve are live, but upheld it as a nit in R4 (`:194-199`).
  - Recurrent defects found: dead imports (resolver.py:15-17), ED-902 cited alone instead of ED-901+ED-902+ED-933 chain (D0-minor), stale index line numbers after a 140-line insert (index says §8@293, actual 435) (`:136-141`), CRLF-hash canonical SHA pins (`:80-84`).
  - Open decisions carried each round: Face scale-binding; Composure retirement blast radius (knots §4.2 left untouched); may provisional EDs be cited as basis (`:71-75`, `:229-232`).
- **Conflicts / stale:** At the working tree: resolver dead imports FIXED (`systems/social_contest/sim/contest/resolver.py:15-17` imports `FaceScale`, not `Face`/`TRACKERS`); the CR5 backfire now fires (`resolver.py:437` `c.face.strip_points`), so the "Standing.strip never called" finding is stale. Whether the Face Cha×3 vs Standing split was closed: [UNVERIFIED] (`FaceScale` exists in primitives, suggests a scale-binding was added). `RETIRED_TRACKERS` still exported in `__init__`/`primitives`/`wrapper`/`_kernel_tests`.
- **Open items:** the three decisions above; per this log nothing records Jordan's answers (the Gate-B log shows the Face/Composure item "still needs_jordan, ED-1056").

### .audit/2026-07-01-contest-gate-b-packet/verdict_log.json
- **What it is:** JSON, 4 judge rounds on Stage-2 / Gate-B (typed dictionaries: styles, interaction types, adjudicators, faction boosts, proceedings; Panel closure of ED-137 via `VoteAtClose`, ED-1057..ED-1060).
- **Status:** none; each round `tests_green: True`. Reading: historical; most items fixed in code.
- **Bears on:** SC, FA
- **Content that matters:**
  - R1 F1 (major): the Panel simple-majority rule was justified by a fabricated citation ("matches §10 BG parliamentary vote"); canon §10 is a Mandate-weighted pool and §7.2 lists seven heterogeneous aggregation rules (`:5-9`).
  - R1 F2 (major): a prebuilt `contract.Panel` object silently skipped the Panel closure and fell back to Tally/PersuasionTrack (`:11-15`).
  - R1/R2: six Stage-2 typed dictionaries marked WIRED but consumed nowhere in resolution (`:23-27`); no canonical proceeding routes to Panel (dead mechanic) (`:56-60`).
  - R2 F4 (major): Obscuring Styles (Suppression/Insinuation) strictly dominated by Precedent/Vision in single-exchange proceedings (Doubt Marker has no downstream) → ED-1060 Terminal Doubt; R3 found Terminal Doubt self-contradictory on direction (`:62-66`, `:131-135`); R4 found it written only for PersuasionTrack, while Casual Dispute / Personal Appeal resolve by `TallyAtClose` (`:247-251`).
  - R3 and R4: Royal Audience ≡ Guild Arbitration and Casual Dispute ≡ Personal Appeal are mechanically identical until resistance and asymmetric roles are plumbed (`:136-140`); Guilds faction boost carries "GM picks" in a no-GM engine (`:146-150`, `:252-256`); flavour text dishonesty ("bench" for a single judge, "vote" on a track proceeding, Private Negotiation invented mutual-consent).
- **Conflicts / stale:** At the tree: "GM picks" fixed by ED-1061 (`dictionaries.py:427-436` "engine-derived, was GM picks"); prebuilt-Panel path fixed (`wrapper.py:156-165`); `guild_arbitration` now has Panel adjudicator (`modes.py:502` comment "Standard | Panel"), so Panel reachability is answered; `VoteAtClose` now has an `aggregation` parameter and a weighted branch (`resolver.py:121`, `dictionaries.py:674`), so the "simple majority only" decision moved. Default jurors still 7 in `VoteAtClose` (`resolver.py:121`) vs `PANEL_DEFAULT_JURORS` in dictionaries (`dictionaries.py:693`) [size value UNVERIFIED].
- **Open items:** Venue flavour voice (verb-first) and POV-locked flavours (`:263-268`); whether `Terminal Doubt` was registered in glossary/mechanical_terms_index (`:158-162`): [UNVERIFIED].

### .audit/2026-07-01-contest-gate-c-packet/GATE_C_packet.md
- **What it is:** 498-line agonist packet for Stage 3 / Gate C (CR4 stasis×genre, CR5 orientation self-gating, the adjudicator armature), ED-1062, dated 2026-07-01, three re-revisions folded in.
- **Status:** "AUDIT / GATE PACKET ... Not canon until Jordan ratifies" (`:1-2`). Reading: historical (superseded by the `2026-07-02-contest-gate-c-packet` rebuild, see next entries); code described is live.
- **Bears on:** SC, DICE, CHAR
- **Content that matters:**
  - CR4: +1D reception-pool die keyed on the orator's CHOSEN Style genre (`genre_of_style`: Precedent/Suppression→Memory, Vision/Insinuation→Projection) against the live stasis's primary genre, because keying on the move ground was a tautology (`Stasis.relevant` forces `move.ground == live`) (`:13-30`, `:134-164`); ground map FACT→Memory, DEFINITION→None (higher-order reframe, not a genre), CONSEQUENCE/FEASIBILITY→Projection (`:59-69`, `:147-154`).
  - CR5: self-Face backfire only on a deg==0 Obscuring move, magnitude `min(2, own Face)` via `Standing.strip_points` (fixed points; `strip()` scales by STRIP=0.8, so −1.6 was applied against a cited −2); the opponent-Face-attack half is DEFERRED and `orientation_channel` is a design-table label only (`:31-41`, `:70-76`, `:203-240`).
  - Armature: adjudicator gets a 4-axis Conviction vector; Style×position dot-product feeds a continuous δσ μ-shift (`ARMATURE_MAX_DSIGMA = level("moderate") = 0.50σ`) because a fractional pool bonus is floored by `roll_net` (`max(1,int(round(pool)))`) so off-axis 0.15 was byte-identical to flat (`:42-57`, `:259-267`); STYLE_AXIS table Precedent→Evidence, Vision→Consequence, Suppression→Authority, Insinuation→Insinuation (new invention; canon's 4th is Solidarity) with PRIMARY 1.0 / OFFAXIS 0.15 [SEED] (`:294-322`).
  - Gate-off when adjudicator == opponent (asymmetric proceedings) prevents double counting; Panel position = mean of members' positions (`:324-336`); verdict becomes conviction-sensitive, `flat < misaligned < aligned`, closing SIM-DEBT-04 (`:338-346`).
  - Appraise-reveal boundary for `armature_position`: Failure→misleading axis, Partial→register, Success→dominant axis, Overwhelming→axis + coarse strength band; exact vector never revealed (`:363-384`).
  - Verification claimed: `pytest sim tests/valoria` 1041 passed; kernel tests 377 passed (`:7-9`); golden-trace agôn parity held because armature is opt-in (`:10-11`).
- **Conflicts / stale:** Cites `designs/scene/social_contest_v30.md`, `npc_behavior_v30.md §1.3`, `modifier_system_spec.md §2.3` (now `.designs/` paths or retired); `sim/personal/contest/` is now `systems/social_contest/sim/contest/` (`style_axis_dsigma`, `cr5_self_backfire`, `ARMATURE_MAX_DSIGMA` confirmed present there). Test counts (1041, 377) are stale snapshots.
- **Open items:** Jordan forks at `:404-439`: STYLE_AXIS numeric projection and 4th axis (Insinuation vs Solidarity); Appraise-reveal boundary; epideictic loss (recommended accept 2-genre compression); CR5 Face-cost anchor and whether cost should grow with standing; fold the categorical opponent-aimed +1D into the continuous primitive (`:279-281`). Opponent-Face-attack half of CR5 stays unwired.
