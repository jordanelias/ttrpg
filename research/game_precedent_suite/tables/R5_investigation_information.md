# R5 (v2, verified) — Investigation & information: six games vs Valoria (ids I1-I6)

Original: `../R5_investigation_information.md`. Verification pass 2026-10-22. Tags: [V2 url version/date] = read in a fetched page body this session; [S2 url] = search snippet only; [M] = memory, not re-checked; `?` = not established. Changes are listed in "Verification log".
Access notes. Fandom `/wiki/` pages return 403 but the MediaWiki `api.php` (action=query&prop=revisions) answered, so Obra Dinn, Shadows of Doubt, Pentiment, Disco Elysium and Kingdom Come wiki text was read that way (tag shows page + revision date). Dwarf Fortress wiki the same. Steam news feeds (`api.steampowered.com/ISteamNews`) gave primary patch notes and dev diaries for Shadows of Doubt (154 posts) and CK3 (714 posts). Still blocked: Paradox wiki and forum (Client Challenge), wiki.gg, breezewiki, web.archive.org (tunnel reset x3), primagames, gamerjournalist. WebSearch budget ran out partway; the last CK3 secrets query was not run.

## 1. Return of the Obra Dinn (Lucas Pope / 3909 LLC; first-person deduction; PC 2018-10-18, consoles 2019-10-18)
Date note: Wikipedia's infobox text says 18 Oct 2018 but its Development section says 17 Oct 2018: [CONTESTED by one day]. [V2 en.wikipedia.org/wiki/Return_of_the_Obra_Dinn 2026-10-22]
| id | val | how |
|---|---|---|
| I1 | YES | Memento Mortem pocket watch replays the seconds before a death; walk the frozen scene hunting names, clothes, voices. [V2 Wikipedia] |
| I2 | YES | Logbook fate = name + means of death + (if killed) killer's name, each picked from lists; 60 people. [V2 obradinn.fandom.com/wiki/General rev 2025-10-10; filmstories.co.uk/?p=83249] |
| I3 | NO | No news or rumour system; closed historical event. [M] |
| I4 | NO | None. [M] |
| I5 | PART | Unlabelled and ambiguous identities are puzzle content; the identity list marks a name already used. Not a player tool. [V2 wiki General for the list; "puzzle content" is [M]] |
| I6 | YES | Truth fixed and complete; logbook is a separate player belief; each identity carries a fixed difficulty of 1-3 triangles. [V2 wiki General] |
| M3 | PART (was NO) | No in-play consequence, but the closing letter has 3 tiers by fates solved (0-27, 30-56, 58 solvable). [V2 obradinn.fandom.com/wiki/Endings rev 2021-04-01] |
- Verification rule [V2 wiki General]: "If you have three correct fates in the book, the game will immediately 'lock-in' those fates" (print replaces handwriting, cannot be changed, identity leaves the picker). A fate is correct only when every field is (killer included); being named wrongly as someone else's killer does not stop the namer's own fate locking. Wikipedia: "correct fates are validated only in sets of three", the last six "in sets of two", and "some deaths will accept more than one solution" [V2 Wikipedia]. The wiki says plainly that brute-forcing is possible but unnecessary.
- Feedback leak [V2 filmstories.co.uk/?p=83249]: batching still tells you an entry is wrong when later batches lock without it; the reviewer describes cycling three candidate names across three batches ("that wasn't an actual deduction"). So the throttle slows guessing, it does not prevent it.
- Correction to the original: "58 of 60 needed to finish" is wrong. Once all memories are seen it rains, and you may leave at any count; the letter differs. 58 fates are solvable before the last chapter, and the final two (chapter VIII) need the monkey's hand from the ending-3 package. [V2 wiki General, Endings; Wikipedia says 58 of 60 "near the end"]
- Skill model: pure PLAYER skill, no stat, no dice. Valoria analogue: Claim ledger vs Event log exists as data; a player-facing belief board and a throttled verifier do not.

## 2. Shadows of Doubt (ColePowered Games; first-person detective sim; early access 2023-04-24, left early access 2024-09-26 [V2 Wikipedia]; Steam patch notes at 42.04, 2026-09-16 [V2 Steam news API])
The original rested on 2023 guides. Since then: accusation (2023-09-25), kidnap cases, side jobs, modifiers (2025-09-18). Wiki pages cited are revisions from 2025-2026 on a v42 game.
| id | val | how |
|---|---|---|
| I1 | YES | Fingerprints, footprints, CCTV (last 24 h on a computer), call logs, V-mails, receipts; evidence is physical objects. [V2 store.steampowered.com/app/986130; sia.hackernoon.com guide 2023-09-28] |
| I2 | YES | Pin evidence on a Case Board, build 23-field citizen profiles, name a suspect on a Resolution Form. [V2 store page; shadows-of-doubt.fandom.com Citizen Profile rev 2025-06-05] |
| I3 | PART (was ?) | Newspapers carry case reports ("Articles ... may also contain information about recent murder cases"); no citizen-to-citizen rumour mechanic found. [V2 wiki Newspaper rev 2026-09-10; Steam news 39.09 2024-10-11] |
| I4 | NO | Player tails, photographs, bribes; side jobs include corporate-espionage Theft and Tailing contracts. No agent network. [V2 wiki Cases rev 2026-09-10] |
| I5 | PART (was ?) | Cover-up job (killer pays 1500 crows to have bodies disposed of), Hidden status; accusing can "blow your investigative cover". No forgery tool found. [V2 wiki Cases; Steam news 2023-09-25] |
| I6 | YES | Fully simulated citizens and routines; player knows only what they find. [V2 store page] |
| M3 | YES | Wrong name: -100 credits and the killer keeps killing. [V2 wiki Resolution Form rev 2025-02-27; Wikipedia: "fined ... real murderer will continue killing"] |
- Resolution Form (murder), exact payouts [V2 wiki Resolution Form rev 2025-02-27]: killer's full name is the ONLY required field (+1000 credits correct, -100 wrong); optional: arrest (+350), evidence placing killer at the scene (+500), murder weapon (+300), address (+50). A correct name resolves the case "even if the other four sections are left blank or filled out incorrectly". So only the name is a pass/fail exact match; the rest are graded rewards with no penalty. The original's "exact match field by field" is corrected. Kidnap form: name +1000/-100, arrest +50, den +50, rescue the victim within six in-game hours +50.
- Case generator [V2 wiki Cases]: six killer archetypes (Ripper, Corporate Cutthroat, Dating Service Stalker, Terrorist, Apartment Sniper, Rooftop Sniper), each leaving a signature evidence pattern (a Sniper leaves no fingerprints or footprints). Killers keep killing until a correct form is turned in, "or the player closes the case"; the wiki sentence is ambiguous and a forum anecdote says dropping does not stop them: unresolved. City, citizens, routines and murders generated per save [V2 Wikipedia].
- Citizen Profile = 23 identifying fields (name, photo, voice ID, fingerprint, address, telephone, workplace, handwriting type, pass code, ...), each rated High/Low usefulness; the name is the key to resolving [V2 wiki Citizen Profile]. The original's "23 random traits" is wrong (see log).
- Information is bought or chanced: SyncDisks "Charm" makes citizens 10/20/35/55% more likely to share information without payment, and Kaizen-Vlove's side effect makes them 25% less likely [V2 wiki SyncDisks rev 2026-05-20].
- Memory model [V2 colepowered.com devblog 8, 2018-09-15, early design, not re-verified for v42]: citizens log sightings; memories start about 100% accurate and fade by familiarity, distinctiveness, oddness, age, alertness; a citizen whose presence looks bad may lie; a press appeal can bring witnesses forward.
- Evidence decay [V2 sia.hackernoon.com guide 2023-09-28, single source]: fingerprints and blood "can disappear after a few in-game hours". Notebook history keeps the last 40 world objects [V2 Steam news 39.09 2024-10-11].
- Skill model: PLAYER skill. Closest of the six to a Valoria generated-case mode: sim state is truth, evidence are objects.

## 3. Pentiment (Obsidian; Josh Sawyer; narrative adventure; Windows/Xbox 2022-11-15, PS4/PS5/Switch 2024-02-22 [V2 Wikipedia 2026-10-22])
| id | val | how |
|---|---|---|
| I1 | YES | Gather testimony and evidence by spending time slots on suspects' quests; Sawyer designs around "rumor and innuendo". [V2 Wikipedia; fandom Ottilia page] |
| I2 | PART | Player picks who to accuse; by design no right answer exists. [V2 shacknews.com/article/146276; pentiment.fandom.com/wiki/Act_2 rev 2026-04-13] |
| I3 | PART | Gossip is dialogue content ("The Spinning Bee, where Andreas can gossip and learn more clues"); "This will be remembered" flags make later NPCs react. Scripted, not a propagating model. [V2 wiki Act 2; wiki Dialogue_system rev 2024-11-17; thegamer.com beginner tips. "Not simulated" is [M]] |
| I4 | NO | None. [M] |
| I5 | NO | Not a mechanic. [M] |
| I6 | PART (corrected) | Andreas always lacks full information; the killer is deliberately undecided, not a hidden authored fact. [V2 gamedeveloper.com interview; shacknews] |
| M3 | YES | Accusation outcomes persist: blame the widow and she is executed at the end of Act I; the Archdeacon is "biased". [V2 wiki Ottilia "Widow" Kemperyn rev 2024-08-29; gamedeveloper.com] |
| A3 | PART | Background gives dialogue options and persuasion points. [V2 wiki Dialogue_system; Wikipedia] |
- No canonical culprit [V2 shacknews.com, dated 2025-10-08]: Sawyer, asked who did it, "No! There isn't!"; "there cannot be a right answer". Game Developer: alibis were prototyped and cut ("All it does is exclude [suspects]... we're trying to rule people in, not rule them out"); investigation centres on motive, means matter mainly for the Baron; players argue to a biased Archdeacon. [V2 gamedeveloper.com/design/making-pentiment-s-most-macabre-murder-mysteries]
- Accuse structure [V2 wiki Act 2]: three stances - pick the likely killer, mete out improvised justice on whoever "deserves" the gallows, or "let the fates decide". Act I has four suspect quests (Steinauer, Ferenc, Matilda, the Widow) then the Archdeacon ends it; Act II has three (Brother Guy, Hanna, Martin Bauer) then soldiers arrive; Act III (1543) is historical research, not a trial.
- Time [CONTESTED]: wiki says time advances and you "never be able to complete every single quest, much less gather all evidence" [V2 wiki Act 2]; IGN via Wikipedia: "never given enough time" [V2 Wikipedia]; GameBanshee says "the game doesn't have an actual time limit", days are split into segments and digging up a grave or eavesdropping jumps the clock hours [V2 gamebanshee.com/9xhy8]. The original's "Act I about two days, Act II one day" was NOT confirmed; days per act is `?`.
- Checks: persuasion is a deterministic points threshold, no dice - prior key decisions and background add or subtract triangle points and Andreas "must meet or exceed a target number" (example: 2 points to earn the Baron's favour; 5 or less to keep the widow's cross hidden). [V2 wiki Dialogue_system, Persuasion rev 2023-07-07, Ottilia page]
- Skill model: PLAYER choice plus CHARACTER knowledge flags. The world reacts to the accusation, not to the truth: fits a no-GM engine better than a truth-match check.

## 4. L.A. Noire (Team Bondi / Rockstar; third-person detective; consoles May 2011, PC Nov 2011, Remaster 2017-11-14 [V2 Wikipedia 2026-10-22])
| id | val | how |
|---|---|---|
| I1 | YES | Sweep scene for clues; investigation music ends when all key clues found; notebook lists evidence. [V2 Wikipedia] |
| I2 | PART | Per answer: believe / doubt / accuse of lying (dev names were Coax / Force / Lie); accusing requires evidence. [V2 Wikipedia] |
| I3 | NO | None. [M] |
| I4 | NO | None. [M] |
| I5 | PART | Reading liars from facial animation is the core; player does not forge or disguise. [V2 Wikipedia for MotionScan "reactions to judge whether the interviewee is lying"; rest [M]] |
| I6 | YES | Hidden truth; player reads face and statement. [V2 Wikipedia] |
| M3 | PART | Charging the wrong suspect lowers the 5-star case rating; story is authored. [V2 Wikipedia] |
- Intuition [V2 Wikipedia]: each Rank gained earns an additional Intuition point, max Rank 20; spend on locating remaining clues, removing an answer in interrogation, or seeing the community-majority answer. In-game labels are Truth / Doubt / Lie [M]; Wikipedia uses believe / doubt / accuse.
- Verification: authored. Each answer has a fixed correct choice; two-suspect station charge feeds the rating. Skill model: PLAYER skill with a stat-like crutch (Intuition). No rolls.

## 5. Disco Elysium (ZA/UM; isometric dialogue RPG; PC 2019-10-15, Final Cut 2021-03-30 PC/macOS/PS, 2021-10-12 Switch/Xbox [V2 Wikipedia 2026-10-22])
| id | val | how |
|---|---|---|
| I1 | YES | Passive and active skill checks surface clues; autopsy is a four-stage form full of passive checks. [V2 discoelysium.fandom.com/wiki/Skills rev 2026-06-24; Perform_field_autopsy rev 2025-01-29] |
| I2 | PART (re-worded) | Thought Cabinet: limited slots, internalise a thought over in-game hours, temporary penalty or bonus while researching, permanent after. Mostly identity and ideology, not case theories. [V2 wiki Thought_Cabinet rev 2025-09-19] |
| I3 | NO | None. [M] |
| I4 | NO | None. [M] |
| I5 | PART | High Drama can "detect and fabricate lies"; player may lie in dialogue. [V2 Wikipedia] |
| I6 | YES | Hidden facts are authored; skill thresholds decide what surfaces. [V2 wiki Skills] |
| M3 | YES | Red checks "cannot be retried, and success or failure will impact the story". [V2 wiki Skills] |
| A3 | YES | 24 skills under Intellect, Psyche, Physique, Motorics, six each; points on level-up. [V2 Wikipedia] |
- Active check [V2 wiki Skills]: skill level + modifiers + 2d6 vs difficulty; double ones auto-fails, double sixes auto-succeeds. Modifiers come from dice bought at the Novelty Dicemaker, clothing, drugs, active thoughts, previous choices.
- Passive check [V2 wiki Skills]: skill level + modifiers + 6, NO dice; it decides whether an option or flavour line appears. Difficulty table: Trivial 6-7 (skill 0-1), Easy 8-9 (2-3), Medium 10-11 (4-5), Challenging 12 (6), Formidable 13 (7), Legendary 14 (8), Heroic 15 (9), Godly 16-17, Impossible 18/20; none at 19. The original's "85% unlock at skill 4" is unverified and dropped.
- Retry rule [V2 wiki Skills]: white checks may be retried when requirements are met or a skill point is spent on the stat; red checks never. Failure is kept as content.
- Wikipedia: no real solution; "the primary case is nearly unworkable". The case advances by tasks (find the murder weapon, extract a motive, interrogate the suspect) [V2 wiki task pages 2022]; I found no grader of the player's own theory, so verification is by task completion (absence not proven beyond those pages).
- Skill model: CHARACTER STAT. Nearest to Valoria: dice-graded inquiry whose failure is content. Valoria has no passive-check or white/red retry concept [repo; no equivalent found].

## 6. Espionage / information war: Crusader Kings III (Paradox; grand strategy; latest in the Steam feed: Update 1.20.1.2, 2026-10-21 [V2 Steam news API])
Version warning: the original described the pre-1.13 scheme system. Schemes were reworked in 1.13.0 "Basileus" with Roads to Power (2024-09-24): "Reworked the Scheme System" [V2 Steam news 2024-09-24]. Everything below is post-1.13 unless marked old.
| id | val | how |
|---|---|---|
| I1 | PART | Spymaster council task "Find Secrets"; court Antiquarian task searches for rumours of artifact locations. [V2 Steam news DD#104 2022-08-23; DD#164 2025-03-11] |
| I2 | NO | No deduction act. [M] |
| I3 | PART (was NO) | Rumours exist only as (a) a breach notice to the scheme target ("rumours of someone plotting to kill them"), (b) scripted court events, (c) the Antiquarian task. No propagation between characters. [V2 DD#157 2024-09-17; DD#61 2021-05-25; DD#164] |
| I4 | YES | Schemes with up to ~5 role-typed agents; spymaster; target-side countermeasures. [V2 DD#157] |
| I5 | PART | "Fabricate Hook" scheme invents leverage; secrets can be exposed. No forged-document or disguise object. [V2 DD#104; Steam news 1.4.0 2021-06-08; PC Gamer 2019-11-27 "try to make something up"] |
| I6 | PART | Target learns of a scheme only through breaches or discovery; a "Discovered Secret Schemes" tab lists known ones. [V2 DD#157; Steam news 1.13.2 2024-10-23] |
| H3 | YES | Murder, seduce, sway, abduct, fabricate hook, etc.; agents, phases, odds. [V2 DD#157] |
- Scheme model (>=1.13) [V2 DD#157 2024-09-17, pre-release diary; 1.13.0 notes list the same parameters]: success chance starts low (sometimes below 0%) and rises each PHASE, by an amount set mostly by the schemer's intrigue; potential (the ceiling) has "a base of only 30%" so agents are required; phases also yield advantage points, spent to recruit agents and, at execution, to boost success; agents max "around 5", each with a role (speed, secrecy, success); most schemes are executed manually. Odds shown are coarse: "Odds replace the old scheme chance prediction - they don't give an exact value".
- Secrecy [V2 DD#157]: "a grace period of about six months, and then after that, a low chance to be detected monthly"; every target notification (rumour of the plot, agent rooted out, scheme exposed) is a BREACH, and at the maximum breach count the scheme is destroyed (the maximum is not given).
- Murder blocking [V2 DD#157]: two flat checks - one for a one-use blocker (best of the list, e.g. a dog), one summing repeatable blockers (e.g. bodyguards) "to a max of 75%".
- Later tuning [V2 Steam news]: 1.16.1 (2025-05-07) Steal Herd potential 40 to 30; 1.16.2.1 (2025-05-22) "Hostile Scheme success chance starts at a much lower level". Old model (<=1.12): monthly progress roll on power vs resistance, "you could not murder someone in less than ten months" [V2 DD#157]; the original's 95% success cap came from a modder comment [S2 steamcommunity.com/sharedfiles/filedetails/comments/3005790872], is not shown for >=1.13, and is CONTESTED.
- Hooks [V2 DD#130 2023-06-15; 1.10.0 notes 2023-08-22]: weak hooks are single-use and can be refused at a cost; strong hooks are reusable and "much rarer"; perpetual hooks (hostages, 1.10.0) are refusable like weak but reusable every few years. Weak hooks expire (1.4.0 stopped stacking same-expiry weak hooks). The original's "strong hook has a cooldown" (2019 preview) is not supported by any current source I read.
- Spymaster loop [V2 DD#157, DD#104]: spymaster tasks include Disrupt Schemes and Find Secrets; countermeasures are toggles with severe drawbacks, tiered by tenets and traditions. AI "unsavory" rulers run Find Secrets on vassals if detection risk is low, blackmail, and use the hooks to improve vassal contracts; Fabricate Hook is used on vassals whose contracts can be modified.
- Skill model: CHARACTER stat (intrigue, agents, spymaster). Same pattern as Valoria (office plus numbers), with no per-person belief ledger.
- Not established: secret discovery chance and strong/weak hook duration, breach maximum, per-agent potential numbers (see Still unknown).

## 7. Cross-game table (who does the reasoning)
| game | who reasons | how the game checks the deduction | wrong-accusation cost |
|---|---|---|---|
| Obra Dinn | player | fate must be fully correct; locked in sets of three | none; unlocked entries stay pending |
| Shadows of Doubt | player | killer's name exact-match; optional fields pay if right | -100 credits; killer keeps killing |
| Pentiment | player | not checked (no canonical culprit) | persistent, authored (execution, bias) |
| L.A. Noire | player (tells) | authored correct choice | lower case rating |
| Disco Elysium | stat + 2d6 | not checked; tasks complete by checks | permanent via red checks |
| CK3 | stat (intrigue, agents) | success chance bar at execution | breaches; scheme destroyed or exposed |
| Valoria | stat (dice) via social-contest roller for 3 verbs | none: result becomes a Claim | accuse verb only PROPOSED (t05 doc line 345) |

## Still unknown
- CK3 secrets: discovery chance of Find Secrets, number of breaches that destroys a scheme, per-agent-type potential, weak/strong hook duration. Tried: Steam news (714 posts, no numbers), PC Gamer 2019, guildorder (no numbers), Paradox wiki and forum (Client Challenge), GitHub code search (blocked), Sourcegraph (CK3 data not indexed). Settle with: CK3 `common/schemes` and `common/secret_types` files from an install, or the Paradox wiki Schemes/Secrets pages from a normal browser.
- Pentiment: days per act and what happens at the deadline in numbers. Tried: Wikipedia, GameBanshee, Game Developer, wiki Act 2 (primagames 403). Settle with: a playthrough or the wiki's per-act quest-day notes.
- Shadows of Doubt: whether citizens spread information to one another (I3) and any forgery or disguise tool (I5). Tried: wiki page titles (no gossip, forge, disguise pages), 154 Steam posts, devblog 8. Absence of a page title is not absence of a mechanic. Settle with: a v42 save search or the devs.
- Shadows of Doubt: current memory-fade and lying behaviour (devblog 8 is 2018 design).
- Disco Elysium: whether any game system grades the player's own theory. Tried: task pages. Settle with: full wiki task graph.
- Obra Dinn I3/I4/I5 and L.A. Noire I3/I4/I5, Disco I3/I4, Pentiment I4/I5 remain [M] (absence claims, not re-run).

## Sources
- https://en.wikipedia.org/wiki/Return_of_the_Obra_Dinn ; https://en.wikipedia.org/wiki/Shadows_of_Doubt ; https://en.wikipedia.org/wiki/Pentiment_(video_game) ; https://en.wikipedia.org/wiki/L.A._Noire ; https://en.wikipedia.org/wiki/Disco_Elysium (all fetched 2026-10-22)
- Obra Dinn: https://obradinn.fandom.com/wiki/General and /wiki/Endings (read via api.php, revs 2025-10-10 and 2021-04-01); https://filmstories.co.uk/?p=83249 ; https://store.steampowered.com/app/653530/Return_of_the_Obra_Dinn/
- Shadows of Doubt: https://store.steampowered.com/app/986130/Shadows_of_Doubt/ ; https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=986130 ; https://colepowered.com/shadows-of-doubt-devblog-8-simulating-a-city/ ; https://sia.hackernoon.com/shadows-of-doubt-a-guide-to-investigating-crime-scenes-and-solving-murder-cases ; https://shadows-of-doubt.fandom.com/wiki/Resolution_Form, /Cases, /Newspaper, /Citizen_Profile, /SyncDisks (api.php, revs 2025-02-27 to 2026-09-10)
- Pentiment: https://www.shacknews.com/article/146276/pentiment-josh-sawyer-no-correct-answer ; https://www.gamedeveloper.com/design/making-pentiment-s-most-macabre-murder-mysteries ; http://www.gamebanshee.com/9xhy8 and https://www.gamebanshee.com/9xdaf ; https://www.thegamer.com/pentiment-beginner-tips/ ; https://pentiment.fandom.com/wiki/Act_2, /Dialogue_system, /Persuasion, /Ottilia_%22Widow%22_Kemperyn (api.php)
- Disco Elysium: https://discoelysium.fandom.com/wiki/Skills, /Thought_Cabinet, /Perform_field_autopsy, /Find_the_murder_weapon, /Extract_a_motive (api.php, revs 2022-2026)
- CK3: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1158310 (Dev Diary #157, #130, #104, #61, #164; Update 1.13.0, 1.13.2, 1.16.1, 1.16.2.1, 1.20.1.2); https://www.pcgamer.com/crusader-kings-3s-schemes-simulate-seduction-and-murder/ (2019-11-27); https://steamcommunity.com/sharedfiles/filedetails/comments/3005790872 (search snippet only)
- Counterexamples: https://dwarffortresswiki.org/Rumor and /Intrigue and /Knowledge (api.php); https://kingdomcomedeliverance.fandom.com/wiki/Reputation (api.php, rev 2026-10-18)
- Valoria (repo, read-only): proposals/2026-10-22-system-description/...-07-t06-fieldwork-and-information.md, ...-06-t05-social-contest.md; engine/season/rosters.yaml; engine/season/requirements.yaml
