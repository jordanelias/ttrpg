# Digest research1

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: game precedent and historical research (`research/`, tier 3). Entries are in the order of the work-order extract but follow reading order (precedent suite first, because the brief names it); entries for files I did not read in full say so. Precedent games treated per file are named in "Bears on / Content". Reading budget note: the assigned set is about 4.8 MB; see the closing `[SKIPPED]` list for what could not be opened in full.

### research/game_precedent_suite/README.md
- **What it is:** index/method note of the 70-game precedent suite, 2026-10-22, lane IN, written against `51d7b05`.
- **Status:** "FILED — reference, not canon … tier 3 … resolves nothing at runtime"; live as an index.
- **Bears on:** PROCESS, all game tags (as method); SC/FI/MB/FA/SE/CHAR via the capability checklist.
- **Content that matters:**
  - Defines capability ids A1..M5 used by every table and tutorial (A character, B roster, C settlement, D governance, E economy, F mass military F1-F8, G personal combat, H social H1-H6, I information I1-I6, J special, K world, L NPC life, M meta) — the lingua franca to map Valoria features to precedent (:35).
  - Three layers: tables (what a game supports), tutorials (how it plays; eight headings each), dispositions (HAS/LACKS/DIFFERS/CONTRADICTS/DISCARD vs Valoria); 866 rows: 176 HAS, 323 LACKS, 155 DIFFERS, 94 CONTRADICTS, 118 DISCARD (:18).
  - "No LACKS row passed the five-step test … all stay design-level, reference only" (:18): the LACKS rows are NOT work items.
  - Tag discipline: [V2/V3 url date] page body read; [S2/S3] snippet only; [M] memory; `?` unknown; [CONTESTED] (:22). Fandom wikis blocked, so figures are leads, shapes are durable (:26-28).
  - Games indexed per file (:39-40): detective/noir = R5/T06 (Obra Dinn, Shadows of Doubt, Pentiment, L.A. Noire, + Disco Elysium, CK3 espionage); mass battle/campaign = R6/T07 (Total War, FoG II, Ultimate General, HOI4), R2/T02 (Bannerlord, Warband, Battle Brothers, Kenshi), T13 Koei, T17 EU4/Dominions/HoMM, T18 Brigandine/XCOM, T19 Triangle Strategy/Unicorn Overlord/Ace Attorney/Lacuna; social/RPG = R4/T05 (Disco, Griftlands, BG3, KCD), T16 Football Manager.
  - Lists `THROUGHLINES.md` (42 primitives, 13 templates, 10 throughlines) as part of the suite (:13) — not in my assignment.
- **Conflicts / stale:** README says dispositions are `D_T01..D_T10`; the assigned directory holds D_T02,03,04,07,08_also,09,09_also,10,10_also (D_T01, D_T05, D_T06 not in this lane's list although the brief cites `D_T06.md` and `D_T05.md`) [UNVERIFIED whether they exist].
- **Open items:** none; ends with game index.

### research/game_precedent_suite/tables/R5_investigation_information.md
- **What it is:** verified capability table, investigation and information, six games vs Valoria ids I1-I6; verification pass 2026-10-22.
- **Status:** none own line (header "v2, verified"); live as reference, tier 3.
- **Bears on:** FI, SC, CHAR, WR (detective/noir precedent).
- **Content that matters:**
  - Obra Dinn: fate = name + means + killer, each from lists; "three correct fates → lock-in", later sets of two; throttle slows but does not prevent guessing (:17-18). Pure player skill, no stat/dice (:20). Correction: "58 of 60 needed" is wrong (:19). Valoria analogue: Claim ledger vs Event log exists as data; no player-facing belief board or throttled verifier (:20).
  - Shadows of Doubt Resolution Form: killer's full name only pass/fail (+1000/-100), other fields (arrest +350, evidence +500, weapon +300, address +50) are graded rewards with no penalty; wrong name → killer keeps killing (:33). 23-field Citizen Profile (:35); six killer archetypes each with signature evidence (:34); memory model (devblog 8: accuracy fades, bad-look witnesses may lie) (:37); evidence decays in hours (:38).
  - Pentiment: no canonical culprit; world reacts to the ACCUSATION, not truth ("fits a no-GM engine better than a truth-match check") (:52,56); persuasion deterministic points threshold, no dice (:55); alibis prototyped and cut ("rule people in, not out") (:52).
  - L.A. Noire: believe/doubt/accuse per answer, accusing requires evidence; Intuition points as stat-like crutch; authored correct choice (:62,68-69).
  - Disco Elysium: active check skill+mods+2d6 vs difficulty, snake eyes/boxcars auto; passive = skill+mods+6 no dice; red checks never retried, white retry on changed conditions; Thought Cabinet = identity not case theory; no grader of the player's theory (:82-86).
  - CK3 (post-1.13 schemes): success chance rises per phase from schemer's intrigue, potential ceiling base 30%, up to ~5 role-typed agents, 6-month grace then monthly detection, every target notification a BREACH, max breaches destroys scheme; murder-block checks capped 75% (:99-101); hooks weak (single-use) / strong (reusable, rare) / perpetual (:103).
  - Cross-game table row for Valoria: "stat (dice) via social-contest roller for 3 verbs; none: result becomes a Claim; accuse verb only PROPOSED (t05 doc line 345)" (:117).
- **Conflicts / stale:** CK3 numbers are 1.13-1.20 era and explicitly "Not established" for breach maximum/discovery chance (:106,120). Valoria row refers to `proposals/2026-10-22-system-description/…t05/t06` (not opened) [UNVERIFIED].
- **Open items:** "Still unknown" list (:119-125): CK3 secrets numbers; Pentiment days-per-act; whether Shadows of Doubt citizens spread information (I3) or forgery exists (I5); whether any Disco system grades the player's theory. Absences in I3/I4/I5 of Obra Dinn, L.A. Noire, etc. remain [M] (:125).

### research/game_precedent_suite/tables/R6_mass_battle_campaign.md
- **What it is:** verified capability table, mass battle and campaign war: Total War (Rome II manual), Field of Glory II Medieval, Ultimate General, Hearts of Iron IV; 2026-10-22.
- **Status:** "(v2, verified)"; live as reference, tier 3.
- **Bears on:** MB, FA, SE (supply, muster), CORE (auto-resolve path).
- **Content that matters:**
  - Total War: units muster to a general in a region; >20 units auto-fielded as one force, rest as reinforcements, command "up to forty units" (:10-12); secret deployment phase with battle-type-fixed sides (:13); auto-resolve "compares the statistics of all the units", Rome II adds aggressive/protective/balanced auto-resolve stance (:15); community-measured wipe-out thresholds 0.3 / 0.2 / 0.92 (WH2 mod, not CA-published) (:25); stances (forced march, ambush, raiding) with ZOC (:24). Design lesson inferred: two resolvers for one fight (real-time and auto) with a known quality gap; Valoria's single automatic sim avoids that but gives no player-facing handle (:28).
  - FoG II Medieval (SQUARE grid, not hex): no auto-resolve at all (:40); cohesion test 2d6 with quality re-rolls, states Disrupted/Fragmented/Broken with -1/-2/-3 (:47); flank/rear charge counts only from behind the flank line, +200 POA/-1 cohesion if target engaged (:48); command range Troop 4/Field 8/Great 12 squares (:37); army breaks at 60% routed (:51); walls as terrain with POA bonuses (nearest to Valoria WALLS row DR +3) (:104).
  - HOI4: combat width 80 +40, terrain scales it (forest -0.20, hills -0.33, mountain -0.66), over-width penalty, stacking from 8 divisions, planning bonus 0.02 gain/0.01 decay/0.08 manual-order decay/max 0.3 (mirrors disagree: 0.5), supply 72 h grace then 30 days to worst penalty (:92-96). "Set intent, let the engine resolve" at aggregate, not spatial (:97).
  - Cross-game: battle→campaign persistence (M3) present in all four; Valoria's "M3 for battle is unobserved in the control run"; Valoria battle path has no supply; Valoria `march` hands the engine armies "built almost entirely from defaults" (F2/F3 gap) (:101-103).
  - Valoria army-rout line "60% of troops in routed subunits (plus hp < 100 for one subunit)" is the same shape as FoG II's 60% (:51,105).
- **Conflicts / stale:** Ultimate General rows mostly [M]/unverified (:60-72). Repo-side claims (tutorial §0, `engine/season/loop/resolve.py`, `sides.py`) not re-verified [UNVERIFIED].
- **Open items:** Still unknown list (:108-112): UG officer ratings/frontage; WH3 upkeep, 3K supply; current HOI4 widths; auto-resolve default values in WH3.

### research/game_precedent_suite/tables/R4_combat_social_rpgs.md
- **What it is:** verified capability table: Disco Elysium, Griftlands, Baldur's Gate 3, Kingdom Come: Deliverance I/II; 2026-10-22.
- **Status:** "(v2, verified)"; live as reference, tier 3.
- **Bears on:** SC, PC, CHAR, FI (Disco).
- **Content that matters:**
  - Disco odds table: 2d6 ≥ N with crit rules, 97.2% cap / 2.8% floor, +1 skill worth 11-17 points mid-range (:31-32). Passive = skill+mods+6; "anti-passive" checks fire when skill too low and cost Morale (:34). Skill drawbacks discourage min-max (:36). Hover shows pass probability (M4) (:25,31).
  - Griftlands: negotiation as a card battle against the opponent's "core argument", side arguments defended like allies; deck has diplomacy/manipulation/intimidation; your resolve persists between negotiations; five relationship stages with faction boons/banes (:54-55,67-69). Fail-forward by state change (:68). Reviewer's criticism: few reasons to want characters to dislike you (:72).
  - BG3: d20 + modifier vs DC; Karmic Dice per-faction debt makes failed rolls bias later rolls, symmetric for NPCs, an undisclosed fairness layer (:110); companion approval -100..100 scale, leaves at -50 (:111); per-trader Attitude, no global reputation, no trial in Crime (:112,102). Dialogue DC visibility CONTESTED (:109).
  - KCD: Speech compares your visible Charisma/Strength/reputation against opponent; reputation per town aggregated from individuals; D6 is fines/jail via witnesses with a rate table; no trial or judge scene found (:139,143,147). Your numbers shown, counterpart's only with Empathetic perk (:138).
  - Disco has NO trial/court mechanic (:26); none of the four has court argument against held evidence (BG3 Investigation has no clue board, :94).
- **Conflicts / stale:** Disco "fail-forward by design" is the author's inference (:35). KCD2 punishment numbers unsourced (:149).
- **Open items:** Still unknown (:153-159): Griftlands thresholds, KCD speech formula/random roll, BG3 dialogue DC distribution.

### research/game_precedent_suite/tables/R2_warband_sandbox.md
- **What it is:** verified capability table: Mount & Blade II Bannerlord, Warband, Battle Brothers, Kenshi; 2026-10-22.
- **Status:** "(v2, verified)"; live reference, tier 3.
- **Bears on:** MB, CHAR, FA, SE.
- **Content that matters:**
  - Bannerlord: clan tiers by renown 50/150/350/900/2350/6150; companion cap contested but 9 at tier 6; four companion roles (Scout, Engineer, Quartermaster, Surgeon) (:84-85,16); heroes' deaths a difficulty switch (:90); formations 1-8 and F1-F7 commands, delegate to sergeant (:45); persuasion a progress bar (:91); fief loyalty drifts to 50, rebellion <25 only if militia > garrison (:33); influence-priced votes with sponsor-relation effects (:87). Tax-rate control not found (:31).
  - Battle Brothers: 12-in-battle cap, roster cap origin-dependent (18/20 contested), permadeath/injury as the design core, world scales off 12 highest-level brothers, no land/governance (:151-156).
  - Kenshi: per-member job queue; squad AI manages base; per-body-part health; no level scaling; "world keeps changing whether or not you act" (:172-173,211-215).
  - Warband: rent automatic (not in person); marshal role; claimants (:96-98).
  - Closing observation: Kenshi "closest to Valoria's no-GM sandbox in feel" with no governance (:215).
- **Conflicts / stale:** Bannerlord patch numbers (1.4.8, Aug 2026) will date; war/policy costs `?` (:87,219).
- **Open items:** Still unknown (:218-225): vote costs, 1.4.x clan-tier table, tax control, BB roster cap.

### research/game_precedent_suite/tables/REPO_MENTIONS.md
- **What it is:** read-only scan (2026-10-22) of what the repo itself claims about each comparison-set game, with a wrong/stale list (section 4).
- **Status:** none own line; reference, tier 3. Byte-identical to `dispositions/repo_claims_checked.md` (cmp confirmed).
- **Bears on:** all (esp. FI, SC, MB, FA, SE, NPC/CHAR); PROCESS (provenance ceiling).
- **Content that matters:**
  - Provenance ceiling: specific figures about games are leads, durable findings are shapes (`research/00_INDEX.md:30-33`); four feeders are the companion `valoria_game_precedent_companion_v1*`, the verb-coverage doc VCD (`proposals/2026-10-03-verb-coverage-and-gap-fill.md`, 7 detective games + CK3 + RTK), uploaded surveys (not committed), and the verbs lexicon where nearly every game cell is `[MEMORY]` (:12-24).
  - Detective/noir coverage by depth: Shadows of Doubt deep in VCD (52 lines) but snippet-level; Pentiment medium-deep (VCD 28, `by_lane/FI` 13, `relay/G_EMERGENCE_PRECEDENT.md`); Disco Elysium medium, partly [UNV]; L.A. Noire medium, partly [MEMORY]; Obra Dinn "one mechanism (batch confirmation)" (5 files); Kingdom Come, Sunless Sea name-drops; Baldur's Gate 3, Darkest Dungeon, Eternal Darkness, Don't Starve, Bloodlines have ZERO repo hits (:28-61).
  - Mass battle: Total War deep (58/44 files) mostly through `proposals/2026-09-25-squad-engagement-concept-v5.md` cited 27 times as `[ASSUMPTION: basis: Total War]` anchors; the concept doc is non-canonical (:31,81); Ultimate General and Field of Glory are name-drops (:52,55,136). Football Manager = "the repo's model of the right shape" via ruled doctrine `auto_manual_resolution_duality_v1.md` (:148). Unicorn Overlord 14 files, Triangle Strategy 17, Brigandine 16 (:154).
  - Repo claims found WRONG/STALE (:158-168): (1) Battle Brothers fatigue: `.designs/.../derived_stats_v30.md:126-128` says armour adds per-action fatigue cost; in BB armour carries a Maximum Fatigue penalty; (2) Victoria 3 enactment numbers (100-day stages, x2/x1.5 multipliers, legitimacy <25/>90 rules) predate 1.3 and are not confirmed; the 2-year cooldown applies to cancelling; (3) Old World ambitions: repo says they "expire when the ruler dies" but unfinished ambitions pass to successors as limited-time legacies; ten ambitions = victory.
  - Repo's own admitted contradictions: M&B "layers do not couple" vs "fully fused" (`by_lane/PC:89`); Manor Lords/Banished births-vs-immigration (ED-SE-0051 vs `SE:107`); Tropico shack-squatting causation inverted (:167).
  - Games the repo leans on that are NOT in the comparison set: RTK/Nobunaga (59 files, "officer mode" declared precedent `player_agency_v30.md:36`), Dwarf Fortress, EU4, Jagged Alliance 2, RimWorld (mood 5/20/35), Dominions, Football Manager, Skyrim, Imperator, Nemesis, Caves of Qud, KoDP/Six Ages, Ace Attorney 18 files (:142-154).
- **Conflicts / stale:** this file is itself the checker; its method note says `proposals/2026-10-16-verbs/*`, UI v4 and `.audit/` workings were NOT read in full (:172).
- **Open items:** none; Dominions edition, Total War title, Anno/Patrician/FoG edition left unspecified on purpose (:174).

### research/game_precedent_suite/tables/R1_dynasty_realm.md
- **What it is:** verified capability table: Crusader Kings III, Victoria 3, Old World, Pathfinder: Kingmaker (read from game files/build notes); 2026-10-22.
- **Status:** "(v2, verified 2026-10-22)"; live reference tier 3.
- **Bears on:** FA, SE, CHAR, SC (council/laws/schemes); CORE (budgets).
- **Content that matters:**
  - CK3 scheme numbers from `common/scheme_values` (jesec/ck3-mod-base 1.20.1.2): phase base 120 d (t1 170, t3 70), success +0.45 per owner skill point per phase, potential base 30, hard cap 95 (100 contract), 5 breaches destroy, Murder cooldown 10 y, murder agents 5 slots (:89). Crown authority 4 levels, cooldown 20 y, Absolute = +25% vassal tax and levy (:37,92). Tax levels 0/2.5/10/15/25% (:38). Council: 6 seats, one task each, friend/rival efficiency +30/-30% (:81). CK3 battles are fully auto-resolved with no player control (F4 NO, F5 YES) (:49-50).
  - Victoria 3: 26 law groups/138 laws; enactment 3 phases, 100-day checkpoints (150/200 for some groups), 730-day cooldown after failure, 3 setbacks fail (:119); IG approval bands (:111); player acts as the STATE, not a character (:99); "control grain is the opposite of CK3: no individual reachable by the player" (:153).
  - Old World: Orders per turn determined by ruler Legitimacy ("hard limit on the number of decisions"), exact formula NOT established, v1's "~0.1 Orders per Legitimacy point" withdrawn (:205); several toggled victory conditions (:203); "10 Ambitions" is the Ambition victory only (:204); regents forced for child leaders up to age 6 (:173).
  - Kingmaker: 10 advisor roles, each kingdom event assigned an advisor with a roll shown, mercenaries as advisors with lower base chance (:216-219,238).
- **Conflicts / stale:** Vic3 1.15 live status unknown; Old World formula unknown; Kingmaker numbers pre-EE (:244-248).
- **Open items:** Still-unknown list (:243-248): CK3 agent types file, Vic3 one-enactment rule, OW Orders formula, Kingmaker role map.

### research/game_precedent_suite/dispositions/repo_claims_checked.md
- **What it is:** byte-identical duplicate of `tables/REPO_MENTIONS.md` (verified with cmp); see that entry.
- **Status:** same as REPO_MENTIONS; live reference, redundant copy.
- **Bears on:** PROCESS.
- **Content that matters:** nothing additional. A DOUBLED file: two copies of one 25,339-byte document in two directories.
- **Conflicts / stale:** README describes `dispositions/repo_claims_checked.md` as a separate "record of claims checked" (:31) though the file is the same text as the table-side `REPO_MENTIONS.md`.
- **Open items:** none.

### research/game_precedent_suite/dispositions/D_T07.md
- **What it is:** critic dispositions of the precedent for the Valoria threadwork tutorial (suite file 08): Eternal Darkness, Don't Starve, Vampire: Bloodlines, Darkest Dungeon II, Sunless Sea, Pathologic 2; code checked at `3aa908b`.
- **Status:** none own line; reference; the code-fact cells are the useful part.
- **Bears on:** WR (threadwork), CHAR, CORE.
- **Content that matters:**
  - 41 rows: HAS 9 / LACKS 12 / DIFFERS 10 / CONTRADICTS 2 / DISCARD 8; "No LACKS row survives the five-step test whole" (:59-61).
  - Coherence/threadwork state is reached only from `systems/threadwork/sim/operations.py` and `coherence.py`; `thread_read` is absent from `resolvable_verbs()` (47 verbs), so it is never formed (:11,57); `(Person, coherence)` is "unproduced", nothing emits the declared `coherence.changed` event (`engine/season/write_matrix.yaml:185-192`) (:48).
  - Own-aim Mending has no cost, cadence or raised Ob so set walks back at 0.85 per cast: code's own `[GAP]` at OPS:159-167 (:20,44).
  - Displacement bands are labels only: no pool, Ob or act changes before the crossing (:21); crossing removes no verb and changes no choice, no consequence for a witnessed working (:35,37,38).
  - `RESILIENCE_GAIN = 0` so practitioners never differ in endurance (:17).
  - verbs-13 cites stale line numbers (`verb_table.yaml:1212`, `rosters.yaml:2349-2354`) now at `:1410`, `:2671-2676` (:55).
- **Conflicts / stale:** the v3 `I1_verification` support for "thread_read attempted 0 times" cannot show it (acts refused before the fold are not counted) (:57). Line cites were opened at `3aa908b` and may have moved.
- **Open items:** Mending cost magnitude, Exposure carrier, season-level `recover` caller (K-WR-8).

### research/game_precedent_suite/dispositions/D_T02.md
- **What it is:** critic dispositions of the precedent for the Valoria tutorial on the season, persons and how an actor chooses (suite file 03), plus a re-measured seed-0 probe; 107 rows.
- **Status:** none own line; reference; code probes at `3aa908b`.
- **Bears on:** CORE, CHAR (decision layer / chooser), FA, SC, MB (Unicorn Overlord, Football Manager rows).
- **Content that matters:**
  - Per-person action budget = 5 + 1 per live `hold` minus body bands/legs (`engine/season/decision/budget.py:57-61`); `create_record`/`utter` have no precondition so mean budget rose 5.57 -> 6.41 -> 7.69 over two ticks and 11 of 74 persons exceeded the 10-action release ceiling (:20, row OW3); count is "wider than by-office design" (H-92) (:20,104).
  - Scene pricing: a plain scene costs 1, an extended one 2 whatever the verbs, per Jordan's 2026-09-02 ruling (`choose.py:653-657`, `budget.py:19-20`) (:21).
  - Chooser: Gumbel/Plackett-Luce sampling at tau=0.1 (`choose.py:376-392`) replacing argmax on measured defect H-96; a 0.1 pursuit gap reversed one time in four (:46). Chooser cannot check preconditions against the world (L2 person-side rule), so families `work` 77/0 and `migrate` 81/0 are formed and refused (:47).
  - Seam: `harness/play_surface.py:14-19,41-52` lets any callable decide for a person (advisor-approval and Unicorn-Overlord-style player-authored procedure shape; TESTS-ONLY); no rule language, no outcome prediction, no odds shown to chooser or callback (:29,95,83).
  - Goals: 35 goals with no progress measure, `goals.yaml:11-12` "never acts, nothing aggregates (A-31)": no code tests completion; no win/loss/ending (G17) (:22,23,33).
  - Stance term (+-4..20) dwarfs pursuit terms (~+-0.3); 13 uncelled verbs score 0; cohorts 37 of 83 choose by pure noise (:80). Default contest failure-modal (pool 2 vs Ob 2: Failure .74, Partial .19, Success .07) so most contested acts write nothing (:74).
  - Player seam claim "only human seam is dispatching_chooser" is false: `systems/social_contest/sim/contest/agon_harness.py:148-155` takes stdin (:105).
- **Conflicts / stale:** repo research docs mis-state Old World ambitions (OW7) and Football Manager "three fidelities of one match engine" (FM4: not established); attachment claims (GK2 pools, RimWorld mean time to break) corrected (:24,32,36,49).
- **Open items:** IN-46/IN-47 (suspend at ENCOUNTER, seat a player) scheduled by D-2; acts-per-person figure in T02 mis-stated (C2); heir/continuation rule absent (GK5).

### research/game_precedent_suite/dispositions/ATTACHMENTS_CROSSCHECK.md
- **What it is:** cross-check of four uploaded (uncommitted) survey documents (20G, 13G, 9T, EN) against the verified tables.
- **Status:** none own; reference.
- **Bears on:** PROCESS, FA, SE, WR, CHAR.
- **Content that matters:**
  - "Rumour as knowledge in transit is unoccupied" is FALSIFIED: Dwarf Fortress rumours spread witness to witness, KCD2 reputation diffuses between locations (:13).
  - "Belief with provenance and fabricable evidence is unique to The Guild 2" HOLDS within v2 (The Guild itself unexamined) (:14).
  - Zone-and-auto-allocate x delegate-to-named-agent is partly occupied (DF burrows/work-details/officers, RimWorld priorities/roles); labour-routing delegate still absent (:16).
  - Factual corrections: Suzerain ~450k launch-era (base about 1M+ words in Steam text), RimWorld mean time to break 4/0.8/0.5 days, Tropico 6 has 10 era-gated factions, Manor Lords Update #8 exists (:29-32).
  - Titles the attachments rest on that no v2 file examined: Pax Pamir, CK2, Imperator, Rome II, RTK/Nobunaga, Empires in Arms, Knights of Honor II, JA2, The Guild, Football Manager, etc. (:46).
- **Conflicts / stale:** none within; attachments are not in the repo and cannot be re-opened.
- **Open items:** untested gaps listed at :50 (rule-bound automaton opposition, dual scoring, multiplayer labour, fabricated-provenance belief).

### research/game_precedent_suite/dispositions/D_T03.md
- **What it is:** critic dispositions of precedent against the Valoria Personal Combat tutorial (suite file 04): Battle Brothers, KCD, JA2, XCOM primary; Kenshi, Griftlands, BG3, DD2, Wildermyth, EN; with a new read-only trace of every combat seam call over seeds 0-2.
- **Status:** none own; reference; code checked at `3aa908b`.
- **Bears on:** PC (primary), CORE, CHAR, FA (capture), MB (Unicorn Overlord-style auto/manual path).
- **Content that matters:**
  - Trace over seeds 0-2: 59 combat seam calls; subject Felled 26, Wounded 15, Untouched 18; in all 33 non-Felled calls the ACTOR was felled; 0 undecided (:17-18). So an attacker never wounds by winning; the loser takes the harm in every one of seven precedents but not in Valoria (row 25, "CONTRADICTS": `_eff_kill` reads the subject's wound only, `effects_combat.py:108,125`; seam returns both wound states, `seam/wrappers/combat.py:230`).
  - 0 of 39 resolved `accept`s answer a `challenge.issued` from their subject; 4 `accept`s are the challenger "accepting" against the man he challenged (kills 3) (:20-22, row 26) — contradicts the tutorial claim that a challenge exposes the issuer.
  - Engine has the KCD vocabulary (commit/feint/lunge, parry/dodge, riposte, stamina `modules/combat/wrapper.py:255-345`) drawn for BOTH sides with zero choice; the L09 lexicon rules the moves belong to the scene (IN-46), not verbs; until IN-46 the duel is "a spectator engine" (row 9). IN-46 (`proposals/2026-10-07-grid-mode-suspension.md`) decider set is [ASSUMPTION] {engage, withdraw} per turn; the tutorial's eight-move menu is L09 M11's (rows 16, 50).
  - Seam derives exactly one field (`end`) from body; kit/stats the pairing table measures as decisive (plate 90.0%, spear 95.5%) are unreachable from the season (row 1). `capability` is empty; no attribute a fight could read (row 15); `train` writes unread `capability`; no growth from fighting (row 8).
  - Closed-form exchange odds exist (`workbench/probabilities.py:109-123`), surfaced by a designer workbench only; Yield exists in the engine with disposition left to the caller, the season never yields (rows 5, 27). Upset floor ("95% cap, no matchup is ever certain") flips `result`, which the season never reads (rows 22, 40).
  - Hit location is out of scope (ED-PC-0055); one recoverable scalar `Person.body`; `tend` sets body to 1000 and the wound is permanent in practice because `tend` never lands (rows 4, 35).
  - Highest-value kill (the King) happens at tick 0 by an unprovoked `accept` and ends nothing; throne stays empty (row 19). Killing before witnesses has no sanction; stance written only by `march`/`forgive` (rows 13, 18).
- **Conflicts / stale:** suite claims T03 §5a "28% of mirror fights wound" and OV §5.2 "no repeat fight traced" are wrong/stale (rows 48-49).
- **Open items:** whether B-Y remediation touches `_eff_kill` not opened (:86-87); capture needs a Jordan ruling for a seatless captor; K-PC-1/M13 growth is Jordan's.

### research/game_precedent_suite/dispositions/D_T04.md
- **What it is:** critic dispositions of precedent against the Valoria Mass Battle tutorial (suite file 05); Total War, FoG II, Ultimate General, Dominions, HoMM, Unicorn Overlord, Bannerlord, Warband, Syx, Manor Lords, HOI4, JA2, Football Manager, Shadow Empire, Brigandine; includes a hand-built `march` probe on `build_realm(0|1|2)`.
- **Status:** none own; reference; code at `3aa908b`.
- **Bears on:** MB (primary), FA, SE, CORE, CHAR.
- **Content that matters:**
  - Season army is unchosen: one Line `infantry` subunit, P4 C4 D5, troops = sum of member weight, built in `MB.py:170-177` (`_faction_to_unit` deleted 2026-10-01) (rows 1, 27, 64); defenders = present members of `holder_faction_of(target)` (`sides.py:107-132`). Probe: march -> `march.declared` then `field.lost`, attackers body 1000->20, 6 defenders untouched, `fortification_of`=1.0 (WALLS) (:13). No realm field is ever fought in ctl (0 fields); no seed gives an attacker 100 troops (:96).
  - ONE resolver: `resolve_field` -> `_run_and_grade` -> same `run_battle(max_turns=18)` as engine-direct (`MB.py:283`), per the auto/manual duality doctrine (row 4); but nobody plays a field, and the season sets no Order (`MB.py:170-177`), no pre-battle intent step, no withdraw, no odds read (rows 3, 22, 27, 46). Football Manager's "instant ~ played" ladder is NOT established (row 58).
  - Engine-direct machinery exists but is unreachable from `march`: Orders with triggers (`immediate`, `tick:N`, `enemy_range:D`, `ally_at:D`, `own_strength:FRAC`, `signal:NAME`), roles/instructions, formations, octagon multiplier GREEN 1.0/YELLOW 1.5/RED 2.0 (`cfg:219`), `MULTI_SIDE_SHOCK` 0.5, ammunition 10 volleys +3 resupply, officers/span of control (`units:2700-2722`), command-0 rout (`orch:2220-2225`), army rout at 60% routed (`cfg:116` says single-subunit armies are provably inert) (rows 14-22, 29, 31, 40).
  - Gaps vs precedent (design-level): no levy/muster/recruit/upkeep (53 `VT` verb rows, none), no supply/attrition/posture, no siege state (WALLS is a binary DR +3), no rally (`rally_check` is an empty hook, `orch:288-290`), no general hurt in battle, no retreat/surrender verb, no captive/ransom (`detain` exists but `EC:255-320` writes none), winner gains nothing; a lost field kills nobody (`scaled_by_degree` floors body at 1) (rows 2, 7-10, 17-18, 34, 49).
  - Friction: one unbounded lognormal `exp(gauss(0,1.1))` per army multiplies every pool (`cfg:335`) vs FoG II's capped modifiers (row 12). Stochastic break between 0.15 and 0.30 losses is "Jordan historical research 2026-07-23" (`cfg:186-187`); TW 30%/20% wipe-out figures are a different quantity (row 6). Defender bias measured 44% (row 24); at realm weights <100 both sides rout on tick 1 so the 18-tick clock never runs (row 45).
  - Repo claims CONTRADICTED: `.designs/.../auto_manual_resolution_duality_v1.md:54` ("auto is unbiased"); `multiunit_envelopment_plan.md:35` (matches FoG ZOC: only flank/rear half true, no ZOC); squad-concept-v5:226 ("Unicorn Overlord tactics are all conditional": false); companion part5:172 ("_faction_to_unit ... garrison a boolean", deleted code); part5:166/187 (Dominions, Bannerlord fast path) (rows 5, 28, 43, 47, 58, 63, 64).
  - The tutorial's claim "the engine runs only under tests" is incomplete: the season loop's ENCOUNTER step calls the oracle end to end; H-175 "march EXECUTES" in `harness/aperture.py` counts only the Declared event; every one of 6 was also refused (rows 67-68).
- **Conflicts / stale:** see claims above; line cites at `3aa908b` may drift.
- **Open items:** J-C-31 (play vs auto), J-C-19 (death policy), J-C-4 (winner wounds/experience), M-1..M-6 verbs (`levy`, `muster`, `marshal`, `rally`, `retreat`, `besiege`) all [PROPOSED]; weight-to-troop conversion REM-32/JQ-4.

### research/game_precedent_suite/dispositions/D_T09.md
- **What it is:** critic dispositions for the Valoria factions/war/diplomacy tutorial (suite file 10), primary items: CK3, Bannerlord, Warband, HOI4, DAI, CK2, Imperator, Rome II, RTK, Nobunaga, KoH II, Pax Pamir, Empires in Arms, EU4, Stellaris, Brigandine, plus 20G/13G attachment parts; three read-only probes.
- **Status:** none own; reference; `3aa908b`.
- **Bears on:** FA (primary), SE, SC, CORE, CHAR.
- **Content that matters:**
  - Succession is absent: `succeed` has no effect (`verb_table.yaml:1096-1113`); the King (6 territories) dies in season 0 in all three seeds and tick-2 reads provinces Varfell 4 / Church 1 with 11 of 16 territories `uncontrolled`; no verb reopens a territory `hold` (`seize` refuses territories by kind and settlements whose holder is None) (rows 4, 5, 13, 36). Seven (not six) null-conferral seats incl. unauthored guild-leader seat `off_npc_084` (row 4).
  - War is an uttered WAR Proposition plus commits (`faction_q.py:219-252`); `at_war` gates nothing (no non-test caller); `march` asks no war state (`sides.py:107-128`); no truce/cost (rows 3, 25, 48). Computed war and computed defection: 0 in seeds 0-2 (rows 14, 28).
  - Vassalage inverted: `oblige` upkeep flows DOWN (seat pays each obligee), nothing owed up; obligee who is not a faction member marches with nobody (`mustered` reads `commit`) (rows 2, 15). `loyalty` = cosine of pursuits vs template (0-100), read only at world-gen, never in mustering or defection (rows 16, 26, 80).
  - Switching faction (`release` then `commit`) costs nothing and carries the holder's land (`faction_holding`, `world_q.py:1620-1653`) (rows 28, 43) — inverse of Pax Pamir. `seize` needs only one faction member present (`effects_information.py:926-931,959`); occupation is by single head (row 44). `dispatch` writes nothing (`verb_table.yaml:372-383`) so delegation is inert (rows 21, 24). 22 of 23 loop-built seats may march because fixture `remit_default` is labelled NOT CANON (row 61).
  - Dead-code-ish Queries: `sovereign_fraction` (no non-test caller; reads (0.4,304)->(0.8,314)), `uncontrolled` (one caller: a census line), `at_war`, faction `head` always None (rows 41, 47).
  - EU4 repo claim "estates loyalty floor ~40, nobody bothers" not found; lesson "a mechanism engineered not to fire is indistinguishable from one that does not exist" stands (row 52).
  - The tutorial's NPC/CHAR relevance: single published scoring rule at tau=0.1 for every actor (king and peasant cohort run the same chooser) (row 84).
- **Conflicts / stale:** attachment claims on KoH II (ungoverned yields about a tenth), RTK kin-lock, Imperator classes, Rome II "hold every region", EiA one-step battle refuted (rows 62, 63, 67, 75, 78, 90).
- **Open items:** `declare`, `conspire`, `recruit`, `assign`, covenant readers M1-M3 all [PROPOSED]; heir/succession; cohort commit ungated (errata C7).

### research/game_precedent_suite/dispositions/D_T10.md
- **What it is:** critic dispositions for the Valoria world/travel/survival/NPC-life tutorial (suite file 11), primary items: Kenshi, DF, RimWorld, Banished, DD2, Sunless Sea, Don't Starve, Pathologic 2, Bloodlines, Sims 4, Wildermyth, Medieval Dynasty, Nemesis, Qud, nine-title survey, EN Part VI-IX.
- **Status:** none own; reference; `3aa908b`.
- **Bears on:** CHAR, WR, SE, CORE (survival, NPC life, persistence).
- **Content that matters:**
  - Per-person hunger set aside by ED-IN-0255 (only cohorts eat, `world_q.py:1029`); the one need term `urgency(subsistence)` (`choose.py:217-238`) is identical for every candidate and "CANNOT CHANGE ANY DECISION" (row 8); no mood carrier: `Sensation` holds `subsistence` and `standing`, the latter raises when read (`carriers.py:388-410`) (rows 13, 76).
  - Healing: `tend` sets body to 1000 in one unpriced act, docstring [ASSUMPTION; medium; Jordan to correct] (`effects_combat.py:371-393`) (rows 3, 15, 23, 28, 33, 38): the sampled sanity/survival games all gate or price recovery. `tend` attempted 0 of 75.
  - Migration: admission reads only `population + weight <= capacity`; 0 of 367 admitted; refusals 81/81, 142/142, 141/141; 185 empty hearths never chosen; destinations only from ledger-named rungs (`world_q.py:1986-2010`, `effects_migration.py:203`) (rows 9, 18).
  - `age_step`, `illness_rate`, `body_step` all ship at 0, rates "Jordan's" (`fixtures.py:590-608`); all built persons have `age_at_build` 0 (rows 19, 31, 67). Combat is the only killer: 9 of 9 seed-0 deaths (row 66).
  - Stance never decays (`march` adds, `forgive` deletes, nothing else writes it; claims decay 5 a season) (row 61); a killing marks no winner and no rival (row 57); stores grow 0 -> 9,250 with no escalation (row 14).
  - Measured acts per acting person 8.14 then 9.37, max 15 (vs T10's "about 7"); `d.resolved` omits acts refused at admission (row 36).
  - Events carry `causes` chains (`travel.ended -> travel.moved -> act`), nothing renders them; recovery written but not announced (H-211) (rows 71, 85, 93). `person.individuated` 0 at every seed (row 20). Births HELD for Jordan (ED-WR-0011) (row 46).
  - Nine-title survey claims corrected: Banished 12-16-year die-off is lore; Medieval Dynasty pairing/averaging unsupported (rows 73-75).
- **Conflicts / stale:** T10 says 7 acts per person; `d.resolved` basis undercounts.
- **Open items:** `succeed` declined for want of estate transmission (7 of 32 seats unrefillable); M-WT-1..4 (distance/route/calendar) [PROPOSED].

### research/game_precedent_suite/dispositions/D_T08_also.md
- **What it is:** also-touches dispositions against the Valoria settlements/governance/economy tutorial (suite file 09); 62 rows (HAS 19 / LACKS 24 / DIFFERS 11 / CONTRADICTS 5 / DISCARD 3).
- **Status:** none own; reference; `3aa908b`.
- **Bears on:** SE (primary), FA, CORE, CHAR.
- **Content that matters:**
  - 7 (not 6) seats have no conferral basis: the six `conferral: null` rows (`offices.yaml:188-266`) plus unauthored guild-leader `off_npc_084` (`populated.py:1240-1250`); King and Duke of Valorsmark vacant at end of season 2 in all seeds (row 2).
  - `revoke` has no standing cost; only `off_duke_valorsmark` sits above a revocable seat (6 pairs) and that seat is vacant and unfillable by season 2, so after that no revoke can pass (row 5). `exchange` is declared with no effect; a hand-submitted `exchange` raises `Unspecified` and aborts the season (row 9). `coin` has no producer (`rosters.yaml:1420`).
  - Holding is never penalised: each hold adds a scene action (`budget.py:57-61`), CK3 domain limit / Stellaris empire size / Warband tax inefficiency charge for size (rows 3, 11, 38). Yield reads Site condition only (`matter.py:589-591`): no labour term, no population term, no governor term, so no famine spiral and a vacant seat costs no yield (rows 19, 20, 32).
  - Stores accumulate 0 -> 9,250 realm-wide in two seasons in all seeds and nothing reads the total (row 17). Upkeep is paid only by a holder's act (`effects_economy.py:287-292` "a MATTER payment would be a fourth clock"); 0 `term.renewed` in every seed (row 24). `migrate`: 185 of 211 hearths stood empty and the chooser picks full ones (row 21). Yield accrues at a built Site whether visited or not (HoMM shape) (row 37); `facility_tier` is absent from `engine/season/` (row 58).
  - AX-1 (Layer 1 `architecture/meta/01_AXIOMS.md:75-78`, "ONLY A PERSON ACTS") is why seats are filled by a person's `confer`, work areas are refused, and orders are emissions (rows 12, 53, 55). ED-IN-0255 (Jordan 2026-09-18) puts hunger on the cohort not on named persons (row 13). Larder walk (`world_q.py:902-911`) lets a cohort draw up the ladder but sideways only by `requisition`->`transfer` (row 30).
  - Siting not a decision: only hearth/community can be founded, every settlement authored; `works_cost` collides with SE-9(a)'s held question (row 49).
- **Conflicts / stale:** the edit targets propose specific text edits to the 2026-10-22 system-description T08 (a different, proposal-side doc). Companion `valoria_game_precedent_companion_v1.md:553` says HoMM accrual absent (stale; row 58); "every franchise deserts on non-payment" is false (row 59).
- **Open items:** M-TAX/IN-23 (tax rate), H-159/EC-G22 (lapse vs arrears), IN-48/H-108 delegation, `vote`/parliament RULED AND NOT BUILT (H-90), RB-5 hunger.

### research/game_precedent_suite/dispositions/D_T09_also.md
- **What it is:** also-touches dispositions against the Valoria factions/war/diplomacy tutorial (suite file 10); 70 rows (HAS 13 / DIFFERS 10 / CONTRADICTS 7 / DISCARD 5 / LACKS 35).
- **Status:** none own; reference; `3aa908b`.
- **Bears on:** FA (primary), SE, SC, MB, CHAR.
- **Content that matters:**
  - Production-caller greps: `at_war(` 0; `provinces_of`, `sovereign_fraction`, `leaders(`, `density(`, `loyalty(` (only world-gen seeding at `populated.py:620,1047`) have no loop caller; `uncontrolled` one census caller (rows 1, 3, 6, 10, 23, 35). `head` is always None; `Tenure.degree` rank has a carrier and no writer (row 69).
  - `march`/`seize` open against any foreign-held settlement with no declaration; `seize` of land with `holder_faction_of` None declines (H-166 unruled), so land freed by a defector or dead holder is frozen, not independent (rows 32, 47). Territory refusal `effects_information.py:933-935` is tagged [ASSUMPTION; medium; Jordan to correct], not a ruling (row 11).
  - `effects_combat.py:293-305`: a lost field writes grudge/morale rows on whichever side lost, defenders included (tutorial said attacker only) (row 30). Doc-only: `covenant` has no term; in force "when both holders are committed" (row 27); `confer` refuses to displace a holder with any live `commit`, so only `revoke` unseats a committed holder (row 49).
  - Belief provenance: forged faction sheet redirects petitions to the forger (forge 12/6/15 ok of 52/51/57); plant `give` ran once in three seeds (row 52). Nothing reads the "told_by" provenance to weight a decision.
  - `dispatch` writes nothing; WITNESS still puts `order.given` in all 79 living ledgers (hand-built) (row 31).
  - A member's own `move` into a rival town suffices to licence `seize` (`mustered` reads `contain`) (row 55). Cohorts hold no membership, so towns never defend themselves (row 36).
  - Morale: `person.died` 9/6/11 with 8/7/10 seats vacated by end of season 2; one refill (a self-conferral) (rows 38, 39).
- **Conflicts / stale:** repo files `by_lane/FA_faction_actions.md:109,117,125,126` carry claims v3 contradicts (Old World ambitions, GK2 budget = Politics, OE sole-conquest, desertion on non-payment); Victoria 3 enactment numbers PARTLY CONFIRMED for 1.13.11 (row 68, corrects REPO_MENTIONS's "STALE").
- **Open items:** `conspire`, `declare`, `recruit`, M2/M3 covenant readers, runtime faction founding (FA-G39/H-186) parked; JQ-4 weight->troop conversion; REM-27 first realm field.

### research/game_precedent_suite/dispositions/D_T10_also.md
- **What it is:** also-touches dispositions against the Valoria world/travel/survival/NPC-life tutorial (suite file 11); 69 rows (HAS 17 / LACKS 24 / DIFFERS 13 / CONTRADICTS 3 / DISCARD 12).
- **Status:** none own; reference; `3aa908b`.
- **Bears on:** WR, CHAR, SE, CORE.
- **Content that matters:**
  - ED-WR-0011 is RULED (Jordan 2026-09-13, Option A: closed authored cast of 46, no births "for now"; `census.py:39-40`) though L18 `proposals/2026-10-16-verbs/...-18-lexicon-npc-life-and-persons.md:85-86,705` and T10/file 12 still call it open (`needs_jordan: true`) (row 3) — an example of a stale `needs_jordan`.
  - `Person.born` is read only by `age_of`/`body_hazard`; every built person has age 0 (`age_at_build`; registry carries `age: null` on 29 of 46 rows) (rows 1, 26). Season factor table `season_factor_draw` ships empty; no year; the only exogenous MATTER inputs are yield, wear and leg end, no random draw at shipped values (rows 13, 20, 44).
  - `tend` restores a body whole in one act, magnitude marked `[ASSUMPTION; medium; Jordan to correct]` (`verb_table.yaml:1162`; `effects_combat.py:370-393`) (row 11). `condition.band_crossed` is emitted only by MATTER's hunger write (`matter.py:530`); combat wounds cross floors silently (row 39).
  - Distance enters neither score nor price: every destination costs one leg (`budget.py:60`); authored `adjacency`, `terrain_cost_matrix`, `march_budget` have no runtime reader (rows 4, 9). Persons have no routine: place changes only by own `move`; most executed moves go to the mover's own place (16/16, 16/17, 10/12) (row 15).
  - A cohort eats where it stands, visitors count against no capacity, so `move` can bring eaters to a larder `migrate` would refuse (row 33). L1-6 option B removes `subsistence` from `Sensation` and the call chain (remediation-01:40) (row 36).
  - MATTER hunger write roots its cause at the prior `body.changed` or ROOT, age/illness death is actorless: a starvation would not name the transfer that emptied the larder (row 49). Refusal kinds fold several causes: `travel.blocked`, `migrate.refused` (`effects_migration.py:77-79,165-175`) (row 55).
  - `.designs/.../player_agency_v30.md:61,63` claims "3-5 scene actions per season" and a 12-day Pathologic constraint: wrong; budget is `max(1, 5 + holds - body bands - legs)` and 5 buys 7 acts (row 61).
- **Conflicts / stale:** attachment RimWorld mean-time-to-break wrong (row 38).
- **Open items:** M-WT-1..4, RB-5, births, `succeed`/R-11, estate transmission.

### research/game_precedent_suite/tutorials/T06_investigation.md
- **What it is:** how-it-plays tutorials (eight headings per game) for the four detective/noir games Return of the Obra Dinn, Shadows of Doubt, Pentiment, L.A. Noire; read 2026-10-22.
- **Status:** none own; reference tier 3; [V3] tags = page body read.
- **Bears on:** FI (primary), SC (argument/evidence), CHAR, WR.
- **Content that matters:**
  - Obra Dinn: confirmation arrives in bursts (3 correct fates lock, last six in sets of two), wrong entries are never marked wrong, they stay handwritten; changing an identity does NOT update the killer name entered elsewhere, you fix both pages by hand (:24,66,73). 60 souls, fixed difficulty triangles per face, face blur = "game thinks you lack information" (:53,81). Lock is "a throttle, not a wall" (:74).
  - Shadows of Doubt: only the killer's name is graded (+1000/-100), others bonus-only; killer archetypes leave signature evidence (Ripper scrambled-name note, Cutthroat business card, Sniper no prints) so recognising type narrows the field (:152); prints/evidence decay, scene cleared if Enforcers wait; accuse-in-dialogue since 35.04 with reaction/blown cover; Social Credit gates scene access (SC7) (:97-98,119,140-141). Case board pauses the game; board is "the only place the form can be answered from" (:95,112).
  - Pentiment: no canonical culprit, no check of guilt; acts end at a story gate; accusation is itself a persuasion CHECK scored in triangle points (Act I Archdeacon: Orator +3, "gave your name politely" +2, "pedantic point about corpus delicti" -2; Act II "Accuse Martin": Rapscallion +3, Orator +3, plus points per fact found: missing scar, no sneezing, a name) (:211,215,226). So argument strength = background + evidence facts gathered, deterministic threshold, no dice. Biography choices (per act) unlock dialogue options and persuasion points, "not stats" (:166).
  - L.A. Noire: per-answer believe/doubt/accuse; ACCUSE requires a notebook item as proof, missing clue = option absent; wrong branch can lose information; each question has one fixed correct choice; blind best guess Doubt 45% (236 questions: 56 Truth, 106 Doubt, 74 Lie); Intuition points as crutch; no running theory board, notebook holds only facts (:249,262-265,301-302).
  - How a hypothesis is tested across the four: Obra Dinn batch lock; Shadows form at City Hall; Pentiment not tested; L.A. Noire one statement at a time (:73,154,227,302).
- **Conflicts / stale:** Pentiment time CONTESTED (wiki vs GameBanshee); Shadows of Doubt resubmission after wrong form `?`; attachment grep: zero hits for these games in the four uploads (:5).
- **Open items:** per-game `?` list at :77-81,156-158,230-233,305-309 (Pentiment days per act, Shadows case-board UI, Noire failed-case UI).

### research/game_precedent_suite/tutorials/T05_social_rpgs.md
- **What it is:** how-it-plays tutorials for Disco Elysium (Final Cut), Griftlands, Baldur's Gate 3, Kingdom Come: Deliverance I/II.
- **Status:** none own; reference tier 3.
- **Bears on:** SC (primary), PC, CHAR, FI.
- **Content that matters:**
  - Disco: clock moves only during dialogue; 24 skills as voices surfacing passive checks (skill+mods+6, no roll); active 2d6; ~10,287 passive and 211 anti-passive checks, 115 (Hand/Eye) to 899 (Empathy) passives per skill; "Kim auto-passes the Titus checks after 3-4 failures, so those checks are not real gates"; XP per task, 100 XP = 1 point; 53 thoughts / 12 slots; opening a task of hanged-man case is thread (:18-24,64,75). No court mechanic; endgame is a trial (The Return) (:70).
  - Griftlands: negotiation is a card game against core argument; relationship stage shifts core resolve -20/-10/+10/+20 for Loved/Liked/Disliked/Hated; stages are discrete and event-driven (attack = Disliked, murder = Hated, favours = Liked, gifts = Loved); "Influence and Dominance" player-side arguments; concede at turn start; negotiation intents shown as inner ring (:153,158-160); failed negotiation can force a fight (:149).
  - BG3: Karmic Dice hidden fairness layer changes outcomes without changing displayed odds; Add Bonus step before the roll; party member chosen to speak uses their modifier; background gives proficiencies but "does not impact dialogue" (:172,193-194,234).
  - KCD: build by doing (Speech from talking), Speech vs Intimidation vs Charisma icons beside timed dialogue options; Charisma averages visible clothing, dirt lowers it; witnessed crime -> fine/jail/talk/flee with reputation per town (:295,307,259).
  - Attachment grep: zero Disco/Griftlands/BG3/KCD claims in the four uploads (:84,314).
- **Conflicts / stale:** earlyguides says white checks one-time and red retryable: opposite of wiki [CONTESTED] (:80); Disco "% shown on hover is engine's own number" `?` (:81); KCD Master Strike per weapon class vs swords only [CONTESTED].
- **Open items:** Disco Morale cap, Kim opinion visibility; BG3 Bardic Inspiration in Add Bonus; KCD normal-mode difficulty setting.

### research/game_precedent_suite/tutorials/T07_mass_battle.md
- **What it is:** how-it-plays tutorials for Total War (WH3 / Three Kingdoms / Medieval II), Field of Glory II: Medieval, Ultimate General (Gettysburg/Civil War), Hearts of Iron IV; "Not compared to Valoria."
- **Status:** none own; reference tier 3.
- **Bears on:** MB (primary), FA, SE.
- **Content that matters:**
  - TW contact step: pre-battle panel shows strength comparison and projected result; choose Fight / Auto-resolve (3K "Delegate") / Withdraw; M2TW manual: auto-resolve "casualties may be heavier", General can die; 3K Delegate "ignores many possible player inputs"; WH3 odds shown "can be wrong" (:24,39). Army = Lord + 1-20 units (WH3), 3 generals x 6 (3K), General + 20 (M2TW) (:50). Recruit: money + upkeep, slots/pools, units arrive next turn; empty treasury at end of turn -> desertion (WH3) (:32,37).
  - Post-battle captive option (execute/ransom/release) and settlement option (Occupy/Loot/Sack/Raze) after EVERY win (:43-44); the Total War captive choice "small, race-bound numeric nudges"; faction/lord pick strongest choice (:80-83).
  - FoG II: square grid, 8 facings, per-unit AP (4 straight / 6 diagonal), Charge tooltip shows Win:Draw:Lose odds from 1000 sample resolutions, combat log (C) explains each round, no auto-resolve, difficulty is only force size ("AI does not cheat on combat or dice"), campaign persists experience/elan with ~15% losses holding parity (:108,115,148,164-165). Scenario types incl. Remove the Head, Escort Baggage, Flank March, Ambush (:105).
  - Ultimate General: units act on own initiative, player draws arrows or defensive line, division commanders act on their own; Gettysburg scores VP = objectives + 1 per casualty with win threshold; supply wagons 35,000 at $1; ammo shortage halves reload; reputation <20 ends the game (:193,195,209,234).
  - HOI4: battle plans per Army (front line, offensive line), planning bonus rewards preparation, "AI is specifically not allowed to be clever", manual override always allowed; dev admission "higher mobilization is (ALMOST) always better" -> a known-best setting is cosmetic unless opposed (:282,313).
- **Conflicts / stale:** HOI4 tutorial reliability low; HOI4 dev diary 41 says general commands 12 divisions vs defines 24 [CONTESTED]; no attachment mentions these games (:91,173,246,323).
- **Open items:** WH3/3K/M2TW upkeep numbers, WH3 turn length, 3K captive options; UG difficulty levels, flank multiplier; FoG II tutorial contents.

### research/game_precedent_suite/tutorials/T19_tactics_narrative.md
- **What it is:** how-it-plays tutorials for Triangle Strategy, Unicorn Overlord, Ace Attorney (Phoenix Wright Trilogy), Lacuna (sci-fi noir detective); no v2 table exists for these four.
- **Status:** none own; reference tier 3; Lacuna is "thinnest" (reviews only, no wiki).
- **Bears on:** MB (Unicorn Overlord squads/tactics), SC (Ace Attorney, Triangle Strategy voting), FI (Lacuna, Ace Attorney), CHAR, WR.
- **Content that matters:**
  - Ace Attorney: cross-examination loop; Court Record of evidence and profiles is kept, not consumed by presenting; a wrong Present is charged (20% in Game 1, 5%-steps later), never refused; an empty gauge = guilty verdict and Game Over; Press is mostly free; Psyche-Locks mark hidden secrets (1-5 locks), magatama breaking recovers 50%; Nov 2025 Story Mode removes failure; "one correct pair per round, space pruned to 2-4 statements" is Danganronpa's Non-stop Debate shape not Ace Attorney's (:172-174,208,211,226). Brute force by exhaustion possible; dominant: Press every statement first (:220-222).
  - Unicorn Overlord: squad of up to 5 characters with per-character Tactics (priority list, up to 2 conditions each); contact starts an automatic exchange in Initiative order using Active Skills (AP) and Passive Skills (PP); stage preview shows outcome prediction; an unconditional Slice placed first means Heal never used; "Optimize" auto-sets; Valor Points pay deployments and Valor Skills; guard posted per town earns gold/forage; Honors/Renown gate unit count (to 10), size (to 5), promotion (:93,104-116,135,146). Repo claim "all conditional" is wrong (:155).
  - Triangle Strategy: Scales of Conviction vote: 6-7 voters each with printed stance or Undecided, one persuasion attempt per voter, info items from the War Chronicle add arguments, hidden Serenoa conviction totals (Morality/Liberty/Utility, +50 per dialogue answer) set recruits and flip thresholds; 10 votes; 14 optional recruits at conviction thresholds 110-1,600; "three hidden axes per character" is wrong (axes are Serenoa's) (:17,23,58,77).
  - Lacuna: timed dialogue options (a few seconds), non-repeating conversations, phone logs clues/news/email, multiple-choice Sheets are structured hypotheses graded only by the story ("you don't have to be right to proceed"), autosave only, 8 epilogues from CDI standing x Zora x data leak; repo claim "temporal drift / watch the scene, learn rhythms" (`.designs/.../investigation_systems_v30.md:209`) NOT supported (:231,243,286,298).
  - No evidence decays in any of the four (clues persist in log/Court Record) (:4).
- **Conflicts / stale:** repo claims corrected: squad-engagement-concept-v5.md:226 (UO "all conditional"), REPO_MENTIONS Ace Attorney "fraction of a bar, never the case", "inventory as argument" (:155,226).
- **Open items:** UO squad count at start (CONTESTED), difficulty names; TS patch/difficulty; AA hours; Lacuna hard Game Over `?`.

### research/game_precedent_suite/tutorials/T16_managers_narrative.md
- **What it is:** how-it-plays tutorials for Football Manager 26, Caves of Qud, King of Dragon Pass, Six Ages: Ride Like the Wind; 2026-10-22; capability line B/F/H/L/M per game.
- **Status:** none own; reference tier 3; footballmanager.com/fmscout pages came through WebFetch extracts (not full reads).
- **Bears on:** MB (Football Manager manager role), CHAR/NPC, WR (emergent narrative, KoDP scenes), SC (KoDP scene responses), FA.
- **Content that matters:**
  - Football Manager: manager sets tactics as two shapes (In/Out of Possession) plus roles/duties and team instructions; picks XI; team talks/shouts/substitutions in play; delegates training, press, team talks to staff; "Continue" advances calendar until something needs you; match view modes include Instant Result; board expectations shown at club pick; tactic needs time to bed in (Tactical Familiarity, FM27 "Tactical Effectiveness") (:9-25,34-35,72). Repo claim "instant ~ played" NOT established: Operation Sports says Instant Result bypasses the match engine; no SI statement (:79) — the manager "right shape" in the repo (REPO_MENTIONS) rests on a plausible-not-established premise.
  - Caves of Qud: per-faction reputation tiers (-600/-250/250/600) decide who attacks; water ritual moves reputation across whole factions; breaking the bond -100..-200 with all factions; generate-then-rationalise verified for sultan history but history is generated for all periods at world creation, not "only when visited" (:103,114,154).
  - King of Dragon Pass: two actions per season, "time passes only when you initiate an action", the world answers each action with an authored scene (544 distinct events) whose OSL conditionals read persistent global variables (e.g. `.mood < 0`); outcomes are skill tests by the chosen leader (win/lose), not branch selection; scene selector is C++ and unpublished; advisors "disagree but pursue the course you set"; saga text is output only, memory is variables (:173,177,230-231). Questionnaire sets mythic profile and ancestors expect conduct.
  - Six Ages: Concerns beside the screen they concern; one Venture per year, same one cannot repeat; abstract combat rounds where both sides pick an option; "few if any situations so critical that a negative outcome will doom you" (:246-249,286).
- **Conflicts / stale:** REPO_MENTIONS "authored-branch selection by stored state" verified with two limits (outcomes are tests; selector unpublished). FM edition FM26 superseded by FM27 (2026-11-10) (:6).
- **Open items:** sacking rules, Instant Result post-match contents, Six Ages scripting (:82,295).

### research/diagrams/mass_battle_formations/README.md
- **What it is:** note on an engine-vs-history visual comparison of mass-battle deployment/pathing after ED-MB-0017 (Cannae, Leuctra, Leuthen, Roman triplex acies), ~July 2026; companion HTML/PNG/generator files.
- **Status:** no Status line; historical (a July-2026 one-off review artefact); `tests/valoria/test_deployment_geometry.py` pinned the geometry "until it was dropped 2026-11-04" (:15).
- **Bears on:** MB.
- **Content that matters:**
  - Fixes claimed and visually confirmed: no subunit overlap (P-1), symmetric double envelopment with wings wheeling opposite senses (P-2), echeloned refused flank (P-3) (:20-31).
  - Honest caveats: wrap completes only ~t16-t20; no cavalry ride-around closes the rear-centre (`_envelop_goal` models the infantry wrap only); single battle line, no triplex reserve/line-relief; envelopment "still often loses" in raw outcome (DG-6 over-decisiveness, ED-MB-0016) (:34-46).
  - Points to `audit/2026-07-22-mass-battle-stress-test/pathing_deployment_diagnosis.md` (a `.audit/` document after the rename) (:50).
- **Conflicts / stale:** references `audit/2026-07-22-...` path that is now `.audit/...` [UNVERIFIED]; the claim that a test pinned geometry is stale (test dropped 2026-11-04). Whether the referenced generator/PNG files still exist not checked.
- **Open items:** cavalry rear transit, reserve-line relief, envelopment reward (ED-MB-0016) as written; none tracked here.

### research/diagrams/mass_battle_formations/SOURCES.md
- **What it is:** link/citation list for historical formation diagrams (Cannae, Leuctra, Leuthen, triplex acies, phalanx/oblique order); explains images are not stored because the proxy blocked binary downloads.
- **Status:** no Status line; reference.
- **Bears on:** MB (history grounding).
- **Content that matters:**
  - Source anchors named: Polybius 3.107-118, Livy 22.44-49, Goldsworthy *Cannae* and *The Roman Army at War*, Xenophon *Hellenica* 6.4, Hanson, Sabin *Lost Battles*, Wikipedia battle maps (public domain West Point maps), Historia Civilis animations (:15-48).
  - Schematic SVGs are the author's own drawings "from the geometry described", not tracings (:53-57).
- **Conflicts / stale:** `schematic_*.svg/.html` files promised in this directory [UNVERIFIED present].
- **Open items:** none.

### research/diagrams/mass_battle_formations/perimeter_model/README.md
- **What it is:** machine-vision validation note for the perimeter target-point / normal model of formations (Line, Arrowhead, Column, GappedLine); 2026-07-23.
- **Status:** no Status line; reference.
- **Bears on:** MB (cell/perimeter geometry, `perimeter.py`).
- **Content that matters:**
  - Perimeter model: faces (yellow), major target points at face midpoints, minor at corners, sharp vertex when interior angle <=60 degrees, outward normals as required approach angle (:3-9).
  - Line panel matches Jordan's hand drawing; sharp-tip detection correct for Arrowhead base corners; the convex hull bridges GappedLine's internal lane so gapped formations need concave/internal-edge perimeter handling (:12-17).
  - Spec cited: `audit/2026-07-22-mass-battle-stress-test/perimeter_targeting_geometry_v1.md` (:17).
- **Conflicts / stale:** convex-hull limitation vs. current `perimeter.py` [UNVERIFIED].
- **Open items:** concave hull for gapped formations.

### research/provenance/2026-08-28-systems-integration-harvest/CORRECTIONS.md
- **What it is:** gate-A correction list for a 1,079-record harvest of the design corpus (2026-08-28): stale items to drop, settled-as-open items to close, merge keys, re-tags, standing limits.
- **Status:** none own; process/provenance, historical.
- **Bears on:** PROCESS (also CORE, FA, FI, SC: the lane gaps).
- **Content that matters:**
  - Drops verified FIXED: H1-038 mass_seizure accord (ED-FA-0037), H3-028 Faction.adjust bounds, H3-045 massbattle roll_pool tn (ED-IN-0196, `assert tn == 7`), conviction/npe rosters, knots scars (:3-9).
  - Closed against ruling: ED-IN-0046 D3 (2026-07-13) "Compact models as a recurring Debt subtype, not a 6th TAG_KINDS family: RULED"; six lanes converged on a settled question (:11-14) — "convergence measured agreement, not truth" pattern.
  - Standing limits: `systems/fieldwork/` (21 docs) and `systems/social_contest/` (6 docs + ~18 modules) were on NO manifest; the 5 fieldwork-investigation records are mistagged knot/faction facts; genuine strong-sense gaps ~150-190 of 471 (:34-40).
- **Conflicts / stale:** refers to `cross_scale_action_catalogue_v1.md:263-267` as restating the pre-ruling list (:15) [UNVERIFIED fixed].
- **Open items:** "Fix separately" for the catalogue.

### research/provenance/2026-08-28-systems-integration-harvest/GATE_A_BRIEF.md
- **What it is:** the antagonist work order for gate A of that harvest (citation truth, status truth, stale-vs-open, slice misclassification, coverage).
- **Status:** none own; process instruction, historical.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Method shape: antagonist has Read/Grep/Glob only; priority order citation truth, status truth, stale-vs-open confusion, slice misclassification (8-value closed set: primitive, derivative, formula, mechanic, process, ruling, content, gap), coverage (:19-52).
  - Lane H1 disclosed it did not re-open engine files it cited; `systems/npcs/` has zero Python files so any `built` record sourced there is suspect (:25-31).
  - "Convergence measured agreement, not truth": six lanes converged on an already-RULED question (:33-39).
- **Conflicts / stale:** points at a /tmp scratch path that no longer exists.
- **Open items:** none.

### research/pre_firearms_formations/00_MANIFEST.md
- **What it is:** manifest of the pre-firearms formations research corpus (2026-05-14, "external, no repo write"): task list, Jordan's vocabulary, chunk plan A-F (ancient to pre-Columbian, weight MAX on 1300-1525 Europe/Islamic-steppe), per-formation entry template.
- **Status:** `[2026-05-14] Manifest created. Chunk A in progress.` (stale: files 01-16 now exist); historical.
- **Bears on:** MB.
- **Content that matters:**
  - Vocabulary per Jordan: Grand formation, Unit formation, Unit, Strategy, Tactic (:12-18).
  - Deliverables: catalogue, strategy and tactics, matchup efficacy, battle-phase choreography (:6-10); entry template fields include composition, geometry (frontage/depth/intervals), equipment dependency, vulnerabilities (:35-45).
  - Chunk plan lists `09_throughlines.md`; the directory actually holds `09_throughlines_matchup.md` through `16_historical_vs_gamedesign_audit.md` (:29 vs ls).
- **Conflicts / stale:** chunk plan stops at F; later files (10-16) extend it.
- **Open items:** none.

### research/governance/00_MANIFEST.md
- **What it is:** manifest of the governance research corpus: 8 civilizations x 3 themes (modes, hierarchy/standing, conflicts), agonist-antagonist method; filed 2026-07-14, lane IN, ED-IN-0064.
- **Status:** "RESEARCH — filed 2026-07-14 ... analytic/reference, not a design ratification"; historical reference.
- **Bears on:** FA (governance), SC (proceedings background), SE, WR.
- **Content that matters:**
  - Civs: Ottoman, Roman (Republic to Dominate), Carolingian, HRE, Renaissance Italy (Florence/Milan/Genoa + Papal States), Venice, Han/Three Kingdoms, Shogunate Japan; Byzantium omitted (:22-32).
  - Each has `=> Valoria design hook:` lines mapping pattern to a mechanic; "proposals, not ratified canon" (:51-53). "Mandate of Heaven is history only ... never proposed as a Valoria mechanic" (design-lead ruling) (:55-58).
  - Maps to a PROPOSED 8-value `governance_mode` taxonomy and the `faction_politics` Standing ladder, Demotion Magnitude (:43-47).
  - Feeds `designs/audit/2026-07-14-scale-chain-and-decision-surface-map/` (dissolved path `designs/`) (:61-64).
- **Conflicts / stale:** `designs/` is a DISSOLVED tree (CLAUDE.md §3); the paths it cites resolve through the restructure ledger only.
- **Open items:** Byzantium "add later if wanted".

### research/emergent_narrative_literature/08_not_read.md
- **What it is:** honest list of candidates attempted-and-blocked, talks with no transcript, books not read, and named-but-unattempted works for the emergent-narrative literature corpus; 2026-10-28, lane IN, against `15593ac`.
- **Status:** "FILED — reference, not canon ... tier 3"; live.
- **Bears on:** WR, CHAR, FI, PROCESS.
- **Content that matters:**
  - Blocked: Sych 2023 thesis; Ryan 2018 *Curating Simulated Storyworlds* (covered only second-hand via Emily Short, tag S); Tanenbaum 2009; Tracery; Ryan/Mateas/Wardrip-Fruin 2015 four design challenges (only from abstract); Versu (Evans & Short 2014) unread; Sengers 1999 (:10-21).
  - Unread talks: Ingold, Ruskin (rule-matching dialogue), Levine, Sylvester RimWorld, Keenan Disco micro-reactivity, Hoge/de Plater Nemesis (:23-31).
  - "Claims about named games (Disco Elysium, Planescape: Torment, Crusader Kings, Wildermyth, Shadow of Mordor) in earlier notes were drawn from web-search excerpts and not re-verified" (:48).
  - Unattempted: Comme il Faut, Ensemble, Riedl & Young narrative planning, PaSSAGE, IDtension, Dormans, Yannakakis (:36-47).
- **Conflicts / stale:** none.
- **Open items:** the whole list (a gap map, not a queue).

### research/historical/mass_battle_gauge_grounding.md
- **What it is:** v2.4 historical/academic grounding for the mass-battle gauge bands (`tests/sim/gauge_mb.py`), dated 2026-06-15..17 (ED-1013/1017/1018/1019); self-authored by Claude.
- **Status:** "drives `tests/sim/gauge_mb.py` bands"; `[SELF-AUTHORED — bias risk]`; partly historical (Jun 2026 engine state; tests/sim is not tests/valoria).
- **Bears on:** MB (primary), PC (formation/cavalry), DICE.
- **Content that matters:**
  - Metric change: decisive split `decA = A_wins/(A_wins+B_wins)` instead of raw A%; draw rate validated separately; high draws near parity expected (Hillestad/Owen/Blumenthal 1995, Taylor 1979/83, Armstrong & Sodergren 2015) (:12-24).
  - Bands: Line mirror H1 42-58; wedge H2 48-62; envelopment H3 55-72; C1 frontal cavalry vs steady foot 35-55 (rebaselined from 52-80: Burkholder 2007 debunks cavalry dominance); C2/C6 braced 0-30 raw cavalry win; C5 cavalry vs shaken 65-98; C7 envelop holding line 65-100 (:53-72).
  - Cavalry "engine defects" were gauge-construction defects: brace recoil `PC_CHARGE_RECOIL=6` fires only on `brace` instruction; shaken shock keys off `morale/morale_start` (:80-83). Latent flag: reciprocal charge-recoil does not zone-gate (fires on flank/rear charge too) (`orchestration.py` ~L1647) (:105).
  - Per-subunit stamina and line relief ED-1017 (Sabin 2000, Zhmodikov 2000, du Picq, Clausewitz) (:124-139); troop-taxonomy stat home `TROOP_TYPE_STATS`/`Subunit.of_type` from `mass_battle_v30.md §B.2` (Levy P1/D1/M2 ... Knights Templar P5/D6/M6); Armour->`dr` and Endur->`stamina` deliberately NOT mapped (no scale bridge) (:143-159).
  - Per-subunit rout/erosion ED-1019: unit rout DERIVED (aggregate morale 0, or all subunits routed, or Command<=0); NO intra-unit cascade added (Jordan's call) (:163-182). `SUBUNIT_ROUT_FLOOR` was a dead stub (:165).
  - Hierarchy bearing: subunit-carried stamina/morale/discipline/rout is exactly the "each level carries its own state" structure Jordan's MB intent asks about; the doc shows it was built engine-direct.
- **Conflicts / stale:** line numbers (orchestration L413-417, L1647) from June 2026; file names `mass_battle/resolution.py`, `orchestration.py` may have moved (`modules/mass_battle/` now) [UNVERIFIED]; gauge lives in `tests/sim/` (not the shipping `tests/valoria` gate).
- **Open items:** the ten Jordan-vetoable judgment calls (:111-120), esp. intra-unit cascade, Armour->dr and Endur->stamina bridges, recoil zone-gating.

### research/historical/precedents_warfare.md
- **What it is:** 2026-04-17 historical precedent analysis for mass battle, army composition, feudal mustering, siege, territory seizure and accord/legitimacy (Crecy, Agincourt, Cannae, Hastings, Austerlitz, Constantinople 1453, Osaka, English levy, Swiss pike militia, Janissaries); companion to `precedents_analysis.md`. Read: §1-§3, §6.4-§8 (lines 1-140, 255-326); §4-§6.3 (lines 141-254) NOT read.
- **Status:** "ANALYSIS — feeds design refinements"; historical (April 2026, PP-675 era, units and Wealth/Prosperity/Accord vocabulary of the old design).
- **Bears on:** MB, FA, SE.
- **Content that matters:**
  - "Generalship dominates" axiom, `ECP = min(Size, Command) + Command`; general's death two-stage, Command to 0 (:25-28) — the ancestor of today's command-0 rout (`orch:2220-2225`).
  - Proposed Campaign Supply (units in hostile territory cost Wealth), Service Duration table for Levy 4 seasons / professionals paid, Morale Cascade (rout triggers a friendly Discipline Ob 1 check), siege civilian consequences (Prosperity -1/season), Siege Parley via Social Contest giving Accord 2 vs 1, settlement-type Muster bonuses (Fortress +1 Size for Heavy Infantry and Cavalry) (:34-133).
  - Post-commit audit (:293-326): committed Campaign Supply (simplified to flat Wealth -1/season), Levy Restriction ("cannot attack outside home territory"), Morale Cascade, Siege Civilian Consequences, Siege Parley, Show of Force, Fortress muster bonus, Accord by acquisition; CUT Militia, Sapper, per-unit supply, Service Duration timer ("bookkeeping, not narrative"). The design criterion: "does this mechanic contribute to the character-world feedback loop that generates emergent narrative?"
- **Conflicts / stale:** the mechanisms live in the dissolved `designs/`-era military layer; current code lacks campaign supply, rally, siege states (D_T04 rows 9-10, 17). Whether Levy Restriction/Campaign Supply exist anywhere in code [UNVERIFIED].
- **Open items:** Priority B/C items (Service Duration, Settlement Muster, Trade Mandate, Militia/Sapper) deliberately deferred or cut.

### research/historical/precedents_analysis.md
- **What it is:** 2026-04-17 historical precedent analysis for theocracy establishment (Papal States, Calvin's Geneva, Iran 1979, Tibet, HRE prince-bishoprics), invasion on the heels of civil war, movements into government, cultural revival/post-occupation governance; maps to Church of Solmund / RM / Altonia mechanics. Read lines 1-60 and 317-398; §2-§5 (lines 60-316) NOT read.
- **Status:** "ANALYSIS — not a design doc; feeds design refinements"; historical.
- **Bears on:** FA, WR (Church, RM, Altonia), SC.
- **Content that matters:**
  - Five theocracy establishment patterns: vacuum filling, competence-based capture, pre-positioned parallel infrastructure, military-religious alliance, gradual accumulation (:25-31); proposals Pastoral Assumption (low-Ob Church governor in a vacated settlement with a Chapel) and Parish Social Services (+0.5/+1 Stability) — "the Geneva trap" (:51-56).
  - Priority list of 12 additions (:317-338); self-audit of Church/RM/Altonian interactions (:342-376).
  - Post-commit audit: Altonian Alignment changed from player action to NPC AI behaviour ("players discover the betrayal through investigation — that IS the narrative moment"); cut RM Accord ceiling (invisible cap = frustration), Mutual Aid, Trade Mandate (:384-397).
- **Conflicts / stale:** vocabulary (CI, TC, PT, IP, Accord, Mandate, Presence) is the April-2026 design layer; whether those exist in `engine/season/` [UNVERIFIED]. Old World/Papal references are history not code.
- **Open items:** deprioritized items listed in precedents_warfare §8.

### research/by_lane/MB_mass_battle.md
- **What it is:** 2026-10-16 NERS-style critical evaluation of the mass-battle lane (history, game precedent, repository work), HEAD `d885abf`/`5445e34`, lane MB; ~770 lines. Read: §0 (11-67), §2 (134-178), §10-§11 (699-768); §1, §3-§9 NOT read in full.
- **Status:** "FILED — reference, not canon ... a critical evaluation"; recommendation IDs K-MB-1..12 are not entered in any plan until Jordan rules; live as an Oct-2026 snapshot (some line cites moved).
- **Bears on:** MB (primary), PC, FA, SE, CORE, CHAR.
- **Content that matters:**
  - Verdict: engine is the most history-cited code but the game never puts it into play. `march` builds one Line infantry subunit per side (power 4, command 4, discipline 5), troops = summed `Person.weight` (`massbattle.py:170-232`); the engine's `SUBUNIT_ROUT_FLOOR` of 80 (`config.py:117`) is checked every tick from tick 1, so every realm side (largest 6, total weight 120) routs; opposed march is always Lost (6v2, 11v1, 2v6, 79v1 all False; 200v1 True) (:13-23). Jordan 2026-10-16 rules the single 4/4 Line "a stub" and states armies are troops levied from settlements as their own resource, differing by equipment, experience and commander, assembled by factions from different subunits with subformations (:13).
  - A composite faction->army adapter already exists but is unused by the season: `build_army` (`systems/mass_battle/sim/engine.py:213-453`) builds several subunits each with shape/role, troop type (`Subunit.of_type`, includes a `levy` row) and `Officer`; `modules/mass_battle/` imports nothing from `systems/` (:13,25,160).
  - Gauge bands gate nothing: `valoria-ci.yml` never runs `gauge_mb.py`; `tests/valoria/test_gauge_invariants.py` engine-against-band tests are `xfail` "TRACKING tests, not gates" (:37-39). C5 ceiling 90->98 and C7 90->100 were raised after emergent values (:34). 15-30% rout band is a Jordan value ("Jordan historical research 2026-07-23", ED-MB-0031) with no research file, credited to du Picq who gives no percentage (:48-52). Several `[canonical:]` provenance tags point to files in FORKED directories (`cavalry_shock_design.md`, `mb_lanchester_design.md`, `sim_mb_06_v9_historical_spec.md`) (:41-47).
  - Precedent: PFF (16 pre-firearms files) "written from memory and never independently verified" (:40); personal-to-field rule "a personal->unit effect must be a fraction of unit size, never flat" (from Dominions, [UNVERIFIED] community consensus) is contradicted by `Command=0 -> instant rout` (`orchestration.py:2221`) and MBv30 §D.3 "player presence +1 Discipline" (:53,158,173). Total War "second resolver" warning is met vacuously: one `run_battle` but no played fidelity (:156). Squad-engagement concept v5's borrowings (FM, Total War, Unicorn Overlord, Door Kickers, Frozen Synapse, Scourge of War, Ultimate General, Symphony of War) are "named, not surveyed" (:145,175); roles partly wired: 9 of 16 instruction keywords drive a primitive (`hierarchy/units.py:71-101`) (:157).
  - Recommendations: K-MB-1 give settlements a levied troop stock (the `levy` verb as used, moving stores, is misnamed; Jordan); K-MB-2 build season armies through `build_army`/`of_type` and delete the one-Line stub; K-MB-3 experience on the stock (Jordan); K-MB-4 `march` gets an order-of-battle operand; K-MB-5 march requires `at_war`; K-MB-6 provision bound; K-MB-7 delete the unread survivor-ratio degree; K-MB-8 one margin ladder (`degree_from_net`) (overwrites ruled ED-IN-0279); K-MB-9 a lost field can kill (`person.died`; `max(1,...)` floor at `effects_combat.py:253`); K-MB-10 a head's fate yields to a personal `fight`; K-MB-11 delete empty `rally_check`/`threadwork_check`; K-MB-12 show the seat its own stock and own claims about the defenders (:699-750).
- **Conflicts / stale:** `_faction_to_unit` deleted 2026-10-01 but `08_mass_battle_units.md §1.5` still describes it (:144); plan part 7 cites paths that moved at `31c` (:55). D_T04 rows now supersede its absence claims where they differ (e.g. D_T04 found the march loop ran once in a season).
- **Open items:** the Jordan items: scale of men per weight, experience form (average vs stratified), played fidelity, at_war gate, death policy, commander fate.

### research/by_lane/FI_fieldwork_investigation.md
- **What it is:** 2026-10-16 NERS-style critical evaluation of the fieldwork/investigation lane, HEAD `021fd96`, lane FI; ~525 lines. Read: §0 (8-26), §2 (71-112), §10-§11 (473-531); other sections NOT read.
- **Status:** "FILED — reference, not canon ... a critical evaluation"; recommendations K-FI-* not entered in any plan; live snapshot (line pointers drifted).
- **Bears on:** FI (primary), SC, CHAR, WR, CORE.
- **Content that matters:**
  - Verdict: "Nothing in FI resolves." The six inquiry rows (VT:1083-1185) write `[]`, emit a content-free `finding.made`, declare no `contests:`; `thread_read` cannot be attempted (H-85); investigation is `in_loop: false`; `examine` "refused only" since IN-57 (:10-14). Ratified FI-01 contradicts its own falsifier (SKIP arm leaves Failure on `finding.none`) (:15). H-111 adopted answer unrecorded and "keyed" undefined (:16). Degree producer tension with the seams ruling; `rosters.yaml:1051` still reads investigation `UNRULED | UNRULED | UNRULED` while the ledger says CLOSED (:17).
  - Archived design (`fieldwork_v30.md`, `investigation_systems_v30.md`) is GM-dependent with 17 cross-file contradictions; FW's architecture was built on the RETIRED Key substrate (`EvidenceView(keylog)`, `Assertion` graded against KeyLog) (:22-23).
  - Precedent sourcing: FW §2 "nineteen precedents" holds 24 rows, 23 tagged `[HIGH]` on the author's own scale; VCD detective rows rest on two uploaded surveys (*Mechanics of Inquiry*, *Narrative Churn*) absent from repo; NONE of the six uploaded precedent documents names Shadows of Doubt, Obra Dinn, Golden Idol, GUMSHOE, Heaven's Vault, Disco, Pentiment, L.A. Noire, Lacuna, Paradise Killer, Outer Wilds, Blade Runner or Brindlewood (:21,79).
  - Game-by-game assessment: GUMSHOE misapplied; Blades fail-forward unreached (FI-01 Failure deposits nothing); Obra Dinn verification oracle rejected and Case Board unbuilt; Golden Idol/L.A. Noire/Sherlock typed evidence-bound assertion: the resolver `Assertion.assert_finding` was built on KeyLog, "no successor verb asserts a finding"; Disco "skills as fallible interlocutors" ruled into the Lattice REFINE but unbuilt; Heaven's Vault confidence = independent support chains vs code's channel-remove discount (H-199); Triangle Strategy hard information gate = scripting-drift warning (archived Depth axis is exactly that); CK3 secrets Exposure has no carrier (:89-102).
  - "COVERED" in VCD means a verb name exists, not that the act resolves: four of five covering verbs write nothing, one always refuses (:101).
  - Recommendations: K-FI-6 give every inquiry a yield (a successful `research` deposits the Record's content in the investigator's ledger via the existing content deposit `witness.py:398-421,682-710`); K-FI-1 competence at reading (AX-7 layer 2 unbuilt, `witness.py:495` actor exemption); K-FI-7 let a low-band inquiry be confidently wrong (Jordan); K-FI-5 concealer's score sets the obstacle; K-FI-3 `interview` yields testimony as the questioned person's own `tell`; K-FI-8 refused inquiry witnessable as an attempt (Jordan); K-FI-9 keep FI-02 role only with a provider; K-FI-11 show the player what his person holds about a matter via `view_ids(...,"question_relevant")` (:473-521).
  - Note this is the repo's own earlier statement that evidence as typed bindable object / evidence-cited argument is NOT in code (relevant to the brief's SC question).
- **Conflicts / stale:** pointer drift (`rosters.yaml:1051` etc.); K-FI-4 withdrawn: `examine` left the executed set at IN-57's attention-key change, not by its Site binding (:502).
- **Open items:** ED-FI-0001 absent from `HANDOFF_FI.md` Open table; K-37 no value space for `reconstruct`.

### research/by_lane/PC_personal_combat.md
- **What it is:** 2026-10-16 NERS-style critical evaluation of the personal-combat lane, HEAD `d885abf`/`5445e34`, lane PC; ~560 lines. Read: §0 (8-26), §2 (78-121); §1, §3-§11 NOT read (so the K-PC-* recommendation list at §10 is not digested here).
- **Status:** "FILED — reference, not canon ... a critical evaluation"; recommendations not entered in any plan until Jordan rules; live snapshot.
- **Bears on:** PC (primary), MB, CHAR, CORE.
- **Content that matters:**
  - Research unreached by the game: `modules/combat/fight.py:45-47` builds both parties as `Combatant(id, end=...)`; every other field default (`weapon='arming'`, `armor='light'`, `tradition='none'`, `history=3`, identical attributes); the seam wrapper says this is deliberate (`seam/wrappers/combat.py:34-39`); building Combatant from the person (#445 K-1/K-5) "NOT scheduled" (`..._part7.md:44`). So the 53-weapon morphology, armour tiers, traditions, abilities never run in play (:10).
  - HEMA research: one self-authored run on secondary web sources with no verifier; cites sources it could not read (Meyer after timeout, ARMA Fiore guide >10MB, armizare.org DNS failure, Wiktenauer 403) (:11).
  - Code comments point at dead paths: `plan_r1_RATIFIED.md` cited at `combat_systems.py:56,125,298,390,406,491`, `contact.py:2`, `weapons.py:892`; regex `designs/audit/` matches 23 lines in 7 `modules/combat/*.py` files; `HANDOFF_PC.md` points into `.designs/` (:12).
  - Duel verbs rest on Jordan's "3 accept" (graded assumption, medium): `accept` cannot read a standing challenge (0 of 12 executed acceptors held a `challenge` claim); PC-10 duel terms yield/blood/death [ASSUMPTION]; the season never declares a yield (`fight.py:52` calls `wrapper.fight(A, B, rng=rng)` without `yield_decl`, so `surrender_of` returns None) (:13).
  - Physics tied to cited constants: 2H/1H force ratio 1.25 (Oh 2022), agility exponent ~0.25 (Cross & Nathan 2009; Fleisig 2002), Williams armour RESIST table, `[SIM-CALIBRATE]`/`[FIAT]` marks; ED-PC-0035 publicly retracted a cherry-picked head-inertia claim; `UPSET_FLOOR` is a designer rule; Ob now derives from defender as `history/2` (ED-PC-0058, `core.py:100-128`) while catalogue says `DECISIVE_OB=3` (:14-21).
  - Facing reversed by Jordan ruling (one-handed profile, two-handed square, `FACING_REGIME_K=0.12`) against the research's finding that facing is per-guard; three comments still describe the old rule (`combat_systems.py:405-407`, `combatant.py:114`, `wrapper.py:135`) (:19).
  - Precedent: "no surveyed game precedent for the bout itself": Riddle of Steel, GURPS Martial Arts, Burning Wheel Fight!, KCD, For Honor, Mordhau, Hellish Quart all `[UNVERIFIED ... none surveyed]` (S/04 §1.5); Fire Emblem/FFT clash is one formula "unverified"; FM/Total War shape honoured: `fight` reads degree off the scene (a data-row mapping was withdrawn as "exactly the second resolver"); "Grid-based unit combat does not exist anywhere in the tree" (`_part2.md:181`); FFT jobs/JP/slots (PCA) held; Ogre Battle/Disco/Darklands chargen unreached; duelling is a "spectator engine" (:78-121).
  - The in-fight player decision (S-1) landed as a dispatch surface only, per `_part7.md:180` (:121).
- **Conflicts / stale:** D_T03 (Oct 22) supersedes with measured trace: attacker felled in all 33 non-Felled calls (the loser-takes-harm defect); `engine/cross_scale/` no longer exists.
- **Open items:** K-PC-1/M13 combatant-from-person, K-PC-2 `_eff_kill` subject-only, IN-46 two-mode path.

### research/by_lane/00_COMPARATIVE_ANALYSIS.md
- **What it is:** 2026-10-16 cross-lane synthesis of the ten lane evaluations (matrix, shared root causes, interaction map, reconciliation, consolidated missing-areas register C6, Jordan decision list C7, key recommendations C8); HEAD `bd8105b`; ~680 lines. Read: header, C0 verdict (24-39), C7 (517-558); C1-C6 and C8-C9 NOT read.
- **Status:** "FILED — reference, not canon ... no recommendation here enters a plan or ledger until Jordan so rules"; live Oct-2026 snapshot.
- **Bears on:** ALL (esp. CORE, CHAR, MB, PC, FI, SC, FA, SE, WR, GO).
- **Content that matters:**
  - Verdict: ten lanes describe one structural absence: persons "differ in what they want but not in what they hold, can do or know", so every scale seam (fight, contest, inquiry, levy, field army, player view) is fed a default or nothing (:26-29). Top interactions: (1) the troop chain (Jordan demands troops levied from settlements; tree sizes season side as one Line of summed `Person.weight`; verb `levy` moves `Rung.stores`); (2) per-person source: `Person.capability` empty on 429 of 430 corpus persons, combat seam builds `Combatant(a_id, end=a_end)` only, H-200 has zero plan mentions, source is J-13's remainder; (3) acts that carry no content (six inquiry rows write nothing, authored OUGHT predicate read by nothing H-185, every computed `utter` mints an OUGHT so war is never uttered); (4) no player surface and no pause (IN-46/IN-47 no build batch; R-04 hence M1 blocked); (5) population only shrinks (ED-WR-0011 closed cast) (:31-47).
  - C7 Jordan decisions: J-C-1 name of the store act; J-C-2 troops: a stock coupled to population vs uncoupled vs troops as people; J-C-3 capacity source (ten attributes, ED-IN-0185 Q7); J-C-4 standing winner's wounds; J-C-6 do persons lie (deception, G7/H-198/H-191); J-C-7 how a petition closes; J-C-8 failed/refused inquiry (error vs ignorance); J-C-12 what the player sees (AX-7 "no state hidden" vs §C.11 arithmetic the character holds); J-C-13 ending; J-C-15 war gate (`march` requires `at_war`); J-C-18 one substrate and the field's margin (`degree_from_net`); J-C-19 death in battle; J-C-20 commander's fate (duel at ENCOUNTER vs side fraction); J-C-21 experience on a stock; J-C-31 played fidelity (duel decision set J-15; player commanding a field) (:517-558).
- **Conflicts / stale:** Oct-16 snapshot; some J-C items were answered later (e.g. births ED-WR-0011 is ruled per D_T10_also row 3; D_T04 shows a realm field can fold once).
- **Open items:** all C7 items unless later ruled; R-C-* IDs index the C8 recommendations.
