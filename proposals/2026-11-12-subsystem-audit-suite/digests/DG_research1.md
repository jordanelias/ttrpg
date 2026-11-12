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
