# SC · DICE — what has already been designed for proceedings and the social contest, collated against Jordan's rulings of 2026-11-14: in code, in workplan v12, or in neither

Written: 2026-11-14, the pass between stage 1 (the Opus interrogation of the code,
`2026-11-14-social-contest-attribute-interrogation.md`, in flight at this read: 32 lines) and stage 2 (a Fable redesign).
Read at the working tree of branch `exec/v12-b00-b03` on 2026-11-14 (HEAD `97dafad`). Read-only on code and plan: nothing
outside this file was edited. Jordan (2026-11-14): *"we have already designed much of this at different stages, so collate
all that is currently missing from code and the workplan that I identified and pass off to fable"*; and, relayed during
the pass: *"you may find fragments of this in proposals or .designs or .audits"*; *"we also have research and proposals
about the psychology of argumentation and persuasion"*; *"and I believe those even have been broken down into
primitives"*.

**Depends on:** stage 1 (the interrogation; its findings on the live roll are not repeated here); B01 and B01a .01–.04
(drawn attributes, `engine/season/harness/pairs.py`); the Spirit-group ruling (R5 as amended by J-12: one key,
`attr.spirit.will`; not yet in `references/descriptor_registry.yaml`, which reads `attr.mind.will` at `:47`).
**Lands in batch:** none (a collation; stage 2 decides the fold).

## Status: PROPOSED

Design input, reference under CLAUDE.md §0.05: it describes designs and code, it is not a mechanism. Every source under
`.designs/`, `.audit/` and `proposals/` is cited for INTENT only (CLAUDE.md §1: `.designs/` and `.audit/` are quarantined
reference, never authority; nothing may load them); where a `.designs/` banner names an original path it is given once,
at first citation. Lanes owning the files it reads: SC (`modules/social_contest/`, `systems/social_contest/`), IN
(`engine/season/`), DICE (`engine/dice_engine/`).

Markers: `[UNVERIFIED]` — a claim whose source was not opened in this pass (or opened only at its headings);
`[ASSUMPTION: … — basis]`. Line numbers are those read on 2026-11-14.

**Status vocabulary used in the inventory (one meaning each):**

| status | means |
|---|---|
| `LIVE` | executes in the season loop today: `modules/social_contest/roll.py`, `engine/season/**` |
| `KERNEL` | written as code in `systems/social_contest/sim/contest/` (the SC05 kernel), which the season loop does NOT reach: SC-05 measured it and kept the one roll (`modules/social_contest/roll.py:16-37`); its retirement is Jordan's (`SM-15`), and v12 retires it at B24.33 (`workplan_v12_part22_cont.md:83`). Code, not game. |
| `V12` | an item of workplan v12 (`proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12/`) carries it; the handle is given |
| `BOTH` | `LIVE` and `V12` |
| `NONE` | designed somewhere, in neither the live code nor v12 (a `KERNEL`-only element counts as `NONE` for the game; the column says `KERNEL` so the code can be harvested) |

## 0. Jordan's rulings this collates against (abbreviated; verbatim in the interrogation's head and the coordinator's brief)

- **R1, the six roles.** Focus = staying on topic, not pulled into the irrelevant. Reason = constructing the argument,
  logical and evidentiary, able to account for the opponent's factual circumstances (resources, office, influence).
  Attunement = what will rattle the opponent, reading intent, reading the room, which kind of argument works on
  audience / adjudicator / opponent. Charisma = being listened to, compelling delivery. Grace = acting correctly for venue
  and occasion, being seen as respectable, remaining composed under difficulty. Will = keeping on arguing, self-belief,
  not getting rattled in the first place, the "x factor".
- **R2.** The subsystem uses all six in the manner specified.
- **R3.** Argue / speech / like verbs all call the social contest / proceedings subsystem: they all concern influencing
  people.
- **R4.** Proceedings have types set by what is at stake, which factions are involved, the venue, the adjudicators, the
  audience, how and what kind of arguments are presented and in what order, the verdict system; from heresy trial to
  parliamentary debate to private negotiation to rallying a crowd.
- **R5.** Spirit is its own attribute group holding ONE attribute, `attr.spirit.will` (renamed from `attr.mind.will`);
  ten attributes in all. As amended by Jordan's answer to J-12, relayed 2026-11-14: *"drop threadsensitivity, keep
  existing prac.thread_sensitivity"* — there is no `attr.spirit.threadsensitivity`; thread sensitivity stays the
  practitioner value `prac.thread_sensitivity`. (v12's B01a.06, `workplan_v12_part3.md:51`, `:161-167`, still adds the
  second key and counts eleven: §4 below.)
- **R6.** Dice are continuous (fractional dice and obstacles), no flat oppositions; tuning from curves over generated
  populations (`engine/season/harness/pairs.py`).
- **R7.** A duel is a restrained contest; a fight is pure combat (`unified/U1_GLOSSARY.md` rows).
- **J-11, answered during this pass** (verbatim in `2026-11-14-social-contest-jordan-rulings.md`, its row R6): *"a
  proceeding is a social contest is a run of exchanges. I guess if we're simply TELLING or LYING or SPEAK etc can be
  abridged auto proceedings"* — tell, lie and speak are abridged, automatic proceedings, not separate rolls outside the
  subsystem. It strengthens §4 items 1 and 2.

⚠ **Numbering.** This file's R1–R7 are the brief's. The orchestrator's rulings file
(`proposals/2026-11-12-subsystem-audit-suite/proposals/2026-11-14-social-contest-jordan-rulings.md`, committed during
this pass) numbers R1–R10: its R1–R5 are this file's R1–R5; its R6 is J-11 (above); its R7 is the verb pass of 2026-11-13
(attributes, skill and office set every verb's dice; one to three averaged; brute functions do not roll; "the exception is
if the verb calls into being a subsystem"); its R8 is this file's R6; its R9 this file's R7; its R10 the fragments
pointers. Read that file for the verbatim words.

## 1. What the live code is, in one paragraph (for the "in code?" column)

The one social roll the season loop runs is `modules/social_contest/roll.py::roll` (`:197-206`): `net = roll_net(pool) +
net_boost(leverage, pool)` against `ob = obstacle(inp)`. The obstacle (`:147-194`) is the task's `difficulty`
(`rosters.yaml: task_difficulty`) plus the opposing person's score halved, minus the room
(`reception_gain · reception + proof_step · proofs`, `:175`, only when the prize row says `heard_by: bench`), plus an
examined document's `forgery_quality`, capped by `obstacle_ceiling` (per-pool solved cap, `:65-86`). The pool is
`faculty(w, person, verb)` (`engine/season/seam/wrappers/sigma.py:225`, `pool.py`): one governing score per verb. The
leverage is `effort` only (`sigma.py:164`, `advantage_sources`). There is one draw per act: no exchanges, no proceeding
type, no adjudicator type, no audience, no venue parameter (the venue catalogue `engine/season/venues.yaml` is buildings
for seating people, `:64-119`, with no rhetorical property), no composure or rattle state, no topic. The SC05 kernel
(`systems/social_contest/sim/contest/`) holds most of the archived design as code, unreached.

## 2. Inventory

Columns: **element** | **origin · source** (origin labels: `JORDAN` a ruling; `RATIFIED` a design carrying a ratified
status in its own file; `PROPOSAL`; `AUDIT`; `IS` the instruction suite; `V11` a v11 workplan item; `CANON`;
`CODE-COMMENT`; `RESEARCH`) | **in code?** | **in v12? (handle)** | **status**.

### 2.A Proceeding types and their parameters (R4)

Short names used below: **v30** = `.designs/systems/social_contest/reference/social_contest_v30.md` (original path
`systems/social_contest/reference/social_contest_v30.md`; its own Status line reads CANONICAL 2026-04-17, now archived);
**v2** = `.designs/systems/social_contest/reference/social_contest_system_v2.md` (SUPERSEDED by v30, `:9-24`); **PK** =
`proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-primitives-and-kinds.md`; **P4** = the same
directory's `2026-11-01-social-contest-proposal-4-authority-staged.md`; **PROC** = `proposals/2026-09-05-proceedings-subsystem/`
(ratified as intent only, ED-SC-0039, PK `:54`); **RED** = `.audit/2026-08-06-social-contest-three-lens-audit/04_reductive_audit_primitives_and_foundations.md`;
**K/** = `systems/social_contest/sim/contest/`; **HEAR_B** = `proposals/2026-11-12-subsystem-audit-suite/proposals/05_SC_playable_hearing_B.md`;
**OBS** = the suite's `U5c_SC_one_obstacle_form.md`; **wp** = `master/workplan_v12/workplan_v12_`.

| # | element | origin · source | in code? | in v12? (handle) | status |
|---|---|---|---|---|---|
| A01 | *Format follows context*: exchange count, role structure, audience weight and actions vary by institution and adjudicator; known before the contest | RATIFIED-then-superseded · v2 §1 `:42-48`; v30 keeps §1 empty (`:29-33`) | KERNEL (proceeding table, below) | partly: a rite and an arrangement row per sitting (B24.09, B24a.04) | V12 (partial) |
| A02 | **Eight proceedings**: Formal Contest (Parliament, 3 exchanges, alternating), Grand Contest (5), Royal Audience (3, Crown objects throughout, resistance halved for the petitioner), Church Tribunal (1–5 set by the Inquisitor, Inquisitor proposes, track biased to 6, opens at the FACT stasis), Guild Arbitration (3, symmetric before a Panel), Casual Dispute (1, no tracker), Private Negotiation (1–3, tracker optional), Personal Appeal (1) | RATIFIED (archived) · v30 §2 Step 5 `:105-116`, §7 `:395-406` | KERNEL `K/modes.py:485` (`PROCEEDINGS`), `K/dictionaries.py:503-603` | none as types; the kernel that holds them is deleted at B24.33 (`wp part22_cont.md:83`) | NONE (KERNEL) |
| A03 | **Adjudicator type** ×4 (expert judge, crowd, no adjudicator, panel), fixed for the contest; a change of type ends the contest and opens a new one | RATIFIED (archived) · v30 §2 Step 1 `:38-47` | KERNEL `K/dictionaries.py:351-383`; LIVE has only "a bench hears it" or not (`heard_by: bench`, `sigma.py:200-205`) | the bench as seats (`judging_set`, B24.10); a panel's ballot seat by seat (B24.11); a mutual row with no bench (B24.30); **no crowd, no expert-judge/panel distinction** | V12 (partial) |
| A04 | The adjudicator type sets the speaker's **primary attribute** (Cognition before a judge or panel, Charisma before a crowd, Attunement with no adjudicator); "the formula is the same; only the base attribute changes" | RATIFIED (archived) · v30 §3 `:127-136`; v2 design note `:141` | KERNEL as display metadata only; the audit found it "fires nowhere" (RED §7 `:195-210`) | no: B05.25 fixes attributes per VERB, not per adjudicator (`wp part8.md:303-324`) | NONE |
| A05 | **Stakes** recorded before the first exchange (what each side wins, loses, compromises) | RATIFIED (archived) · v30 §2 Step 6 `:119` | LIVE as `disposes:` per arrangement row (`engine/season/arrangements.yaml:99-307`), read at `loop/effects_information.py:427-429, :612-614` | B27.02 (a verdict's band chooses its consequence), B27.14 (several matters, design), B27.15 (`damages`, design) | BOTH (partial) |
| A06 | **Faction boost**: each faction's ethical mode boosts one genre or one orientation (Church Obscuring, Crown Revealing, Varfell Projection, Hafenmark Memory, Restoration Revealing, Guilds from the venue's adjudicator) | RATIFIED (archived) · v30 §2 Step 3 `:76-95`; ED-1061 | KERNEL `K/dictionaries.py:404-487` | no | NONE (RED §4 `:117-120` puts it on the kill list) |
| A07 | **Audience resistance** = mean Stability of represented factions −1; halved for the disadvantaged party in an asymmetric proceeding; eroded every two exchanges (ED-864) | RATIFIED (archived) · v30 §2 Step 4 `:102`, §7 `:398-402`, §6.3 `:387` | KERNEL (RED §9 `:236-239`: "dead resistance metadata") | no | NONE |
| A08 | **Persuasion Track** 0–10: ≥7 side A, ≤3 side B, 4–6 compromise, ≥9/≤1 total victory; chain contests restart from the last position | RATIFIED (archived) · v30 §2 Step 4 `:100`, §6 `:287-310`, §6.3 `:376-391` | KERNEL only; LIVE resolves one draw to four bands (`seam/ladder.py` → `degree_from_net`) | no: the hearing closes on one draw (HEAR_B "How a sitting runs", B24.06) | NONE |
| A09 | **Asymmetric proceedings**: the institution assigns proposer and respondent and they never alternate; the disadvantaged side's resistance is halved; the advantaged side takes no strain from CROSS | RATIFIED (archived) · v30 §7 `:398-402` | KERNEL | the rite's `bears:` (who must prove each rung, B24.09) and the inquisitorial rite (B24a.04) carry the role asymmetry; no compensation term | V12 (partial) |
| A10 | **Succession Contest**: a Grand Contest whose adjudicator is the faction's own body (Crown inner circle by Disposition; Hafenmark Parliament by Mandate-weighted vote; Varfell Jarl Assembly by quorum; Church College of Cardinals; Löwenritter Knight-Commanders by seniority; Guilds Council by Favour; Restoration organisers by consensus); track 3–7; a Compromise splits the faction | RATIFIED (archived) · v30 §7.2 `:408-445` | KERNEL `K/faction.py:86-126` (`succession`); LIVE has no succession row (`arrangements.yaml:52-55`) | the `succeed` draw reads the room's legitimacy and the deed race (B32.14, `wp part34.md:386`); the conclave and graded count (B32.20); no faction-keyed adjudicator | V12 (partial) |
| A11 | **Heresy Investigation lifecycle**: initiation (1 season), investigation proper (2–4 seasons, one interrogation each season), verdict (acquittal / insufficient evidence / tribunal recommended); eight closure conditions; one investigation per target per jurisdiction; Church self-investigation exception | RATIFIED (archived) · v30 §7.3 `:449-497`, PP-349 `:654` | no | no lifecycle; the Church's benches judge realm-wide (B32.17) and a church seat may open a case outside T9 (B24a.04) | NONE |
| A12 | **Excommunication Tribunal**: prerequisites (Church Mandate, Evidence, prior conviction), track starting at 7, no corroboration for the accused, 1–3 exchanges, graded consequences, revocation by an Act of Contrition | RATIFIED (archived) · v30 §7.1 `:632-649` | LIVE as the `excommunication_deliberation` row: `disposal: declared`, `quorum: 2`, `disposes: ban` (`arrangements.yaml:272-285`), counted by `world_q.declared_votes` | ballot seat by seat (B24.11); the Church's two sentences graded by band (B33.26); a religious sanction opened through a church seat (B21s.02) | BOTH (partial) |
| A13 | **Parliamentary Stay**: Parliament halts a Church filing one season while the Church's index is under 55 | RATIFIED (archived) · v30 §10.1 `:655-667` | no | a forum plea moves the case to another authority's stage (B24a.07); appeal to another authority (B24a.03); no Stay | NONE |
| A14 | **Board-game Parliamentary Vote** and the **Hybrid** contest (faction Mandate pools, lobbying capped to the compromise zone, committee referral) | RATIFIED (archived) · v30 §10 `:597-619`, §11 `:623-628` | KERNEL `K/faction.py:128-150` (`coalition_vote`) | a count licenses or blocks an owner's act (B24a.01, CR-58; R-29) | V12 (partial; different mechanism) |
| A15 | **Venue presets** ×4 with ethos/pathos/logos proof weights, a temporal register, a starting stasis, a win condition (`ProofBar`, `ThresholdRace`, `TallyAtClose`, `GraceThreshold`) and a fault catalogue | RATIFIED-in-code (CR1, ED-1055..1062; v30 §8 `:515`) · CODE-COMMENT | KERNEL `K/modes.py:66-85` | deleted with the kernel (B24.33) | NONE (KERNEL) |
| A16 | **Institutional regimes** ×3: fused arbiter (momentum is the verdict), deliberative body (momentum and verdict separate; a panel votes at close; "the vote can cross the room", Thucydides 3.36-49), scholastic disputation (tally to threshold, full fault list) | CODE-COMMENT (research 2026-06-04) | KERNEL `K/modes.py:95-154` | no | NONE (KERNEL) |
| A17 | **Six cross-cultural venues**, each with sources: public oration (Roman *contio*, Hippodrome; pathos-dominant, a crowd of 15, who wins the room), inquisition hearing (`ProofBar` 2.5, one evasion strike), excommunication court (a panel of 7, ethos .50), imperial petition (the sovereign's character dominates), secret council (Venetian Ten; a panel of 5 votes at close; documentary), memorial remonstrance (ethos, at personal risk) | CODE-COMMENT + RESEARCH (DOIs at each docstring) | KERNEL `K/modes.py:157-325` | no | NONE (KERNEL) — the nearest built thing to R4's "rallying a crowd" is `public_oration` |
| A18 | **Scaffold modes**: dyadic counsel (steer one listener), negotiation (typed envoy latitude, the overlap), ceremonial (nothing at issue; acclamation) | CODE-COMMENT | KERNEL stubs `K/modes.py:333-359` | no | NONE |
| A19 | **A proceeding is "just defined parameters"**: one host, the games are data rows (R-12, Jordan 2026-09-05; reaffirmed R-15, R-33: one action surface limited by contest type) | JORDAN · PROC `README.md:18`; PK `:41`, `:62` | LIVE loader `engine/season/data/arrangements.py`, nine rows | B24.09 (rites), B24a.04 (authority, two rites), B24.36 (`speech_kinds` held to its roster) | BOTH |
| A20 | **The structural axis**: three sets (parties, bench, floor) and `disposal` ∈ {bench, mutual, none, declared} | PROPOSAL (ratified as intent) · PROC `00_DERIVATION.md:45-83` `[UNVERIFIED: cited through PK :235-236]` | LIVE: bench, mutual, declared on rows; `none` unseeded (`arrangements.yaml:24-31`) | mutual (B24.30), declared (B24.11), `none` on `acclamation` (B32.15) | BOTH |
| A21 | **The thirteen arrangement keys** (`disposal`, `bench_basis`, `floor`, `records_dissent`, `venue_min_rank`, `term_required`, `appeal_basis`, `interposed`, `order`, `proofs`, `disposes`, `disposal_reach`, `quorum`) | PROPOSAL (ratified as intent) · PROC `03_PARAMETERS.md` Part D `:443-520`; `arrangements.yaml:8-15` | LIVE loaded; read at runtime: `disposes`, `disposal`, `quorum` only (`effects_information.py:427-429`, `:612-614`; `world_q.py:38`); the other ten have no reader (grep of `engine/season` for each key, 2026-11-14) | `order` read by the sitting (B24.06 step 1); `proofs` as admitted kinds (B05.21 T5, B24.17); `appeal_to` beside `appeal_basis` (B24a.03); the venue standard read from existing keys (B24.41 (3), design); `floor`, `records_dissent`, `disposal_reach`, `interposed`, `venue_min_rank` read by the institutions rows (B32, B33, B40) `[UNVERIFIED: each reader]` | BOTH (partial) |
| A22 | **The twelve games plus a thirteenth**: negotiation, negotiation through envoys, arbitration, legal trial, tribunal, interrogation, inquisition hearing, excommunication deliberation, parliamentary debate, council of state, audience / embassy, appeal to a higher authority, public debate; examination | PROPOSAL (ratified as intent) · PROC `03_PARAMETERS.md` Part E `:521-733`, F.1 `:744-781` | LIVE: nine seeded (`arrangements.yaml`); envoys, audience/embassy, appeal, public debate, examination unseeded (`:44-52`) | adds `acclamation` (B32.15), `audit` and `quo_warranto` (B33.18), consecration (B33.23); envoys, audience/embassy and public debate get no row | BOTH (partial) |
| A23 | **Latitude is derived from what is interposed** (six kinds: advocate, written channel, ceremony, paired envoy, office, procedure…), never a scalar; interposition buys impasse | PROPOSAL · PROC `03_PARAMETERS.md` B.1 `:59-82`; study Fig. 24 (`PROC/source/09-figures.md:1303`) | LIVE `interposed` loaded, unread | no item reads `interposed` for latitude `[UNVERIFIED: the five files that mention it were not read past the grep hit]` | NONE |
| A24 | **Genre is derived from the bench's remit** (past → forensic, the issue ladder runs; future → deliberative, no ladder; no bench → epideictic), set-valued; a genre-mismatched verb is refused and the refusal emits | PROPOSAL · PROC `03_PARAMETERS.md` B.3 `:110-135` | LIVE only as `speech_kinds.genres: [forensic]` on six rows (`arrangements.yaml:57-97`) | `speech_kinds` held to `ladder_rungs` (B24.36); the issue ladder (B24.03) | V12 (partial) |
| A25 | **Eight kinds of contest** (K1 dyadic influence, K2 negotiation, K3 adjudication with seven subkinds: accusatorial trial, inquisitorial hearing, political tribunal, arbitration, excommunication, appeal, audit; K4 petition and supplication; K5 panel and jury; K6 deliberation by count; K7 display; K8 contests over the contest) and the value each stage takes (convene, frame, gate, burden, acts, decide, dispose, reach, after) | PROPOSAL · PK §3 `:233-343`, §4 `:347-363`; P4 §5 `:513-538` | LIVE reaches K1 and a thin edge of K3 (PK `:320-322`) | K3 (B24, B24a, B27), K2 (B24.30), K4 (B28.04 the petition carried), K5 (B24.11), K6 (B24a.01), K8 (B24a.03, B24a.07); **K7 display has no item but the `acclamation` row (B32.15), which "decides nothing"** | V12 (partial) |
| A26 | **The axes that set procedure within a kind**: who decides, tense and mood of the question, burden, proof regime, order, symmetry, forum fixed or contested | PROPOSAL · PK `:240-248` | partial LIVE (`order`, `proofs` loaded) | burden (rite `bears:`), order (B24.06), proofs (B24.17) | V12 (partial) |
| A27 | **Kinds of authority**: negotiation's authority lies between the parties (imbalance from rung and leverage); a royal tribunal or parliament's is political, vested by the nation; a religious tribunal's is religious, modulated by royal authority if a royal person is involved; adjudicators hold offices relevant to that authority | JORDAN (R-34, 2026-10-30) · PK `:63` | no | `authority.by_faction`, `scope:` on offices, one `may_determine` with an authority conjunct (B24a.04) | V12 |
| A28 | **Legitimacy of the authority in the territory** scales its weight (a heresy proceeding where the Church is weak is not biased toward the Church) | JORDAN (R-36, 2026-10-30) · PK `:65`; P4 §3.6 `:208-230` | no | the legitimacy index, design only (B27.19, CR-65) | V12 (design only) |
| A29 | **Appeal**: no immediate re-contest before the same bench; an appeal to another authority is wanted, on new grounds only | JORDAN (R-35; A-39) · PK `:64`; `unified/DECISIONS_ANSWERED.md:46` | no | B24a.03 (appellate closure basis, `appeal_to`), B27.13 (`reverse` on new grounds) | V12 |
| A30 | **Reasons to convene** (a docketed matter, a vacancy, a shortage, a war…) and why salience fails even where the matter exists | PROPOSAL (reference) · `2026-10-29-reasons-to-convene.md` §4 `:65-87`, §7 `:125-139` | LIVE `convene` exists; forms rarely | consent-licensed acts give a ruler a reason to convene (B24a.01); one convening per seat (B32.22); the convening condition read before a sitting fires (B32.32) | V12 (partial) |
| A31 | **Parliament at four rungs** (kingdom, duchy, province, territory): the sitting in order, where a motion comes from, the council as one seat, how a vote is moved, what a result does | JORDAN (R-26) + PROPOSAL · `2026-10-29-parliament-and-debate.md` §2-§9 `:39-188` | no: the two Record-disposing rows (`parliamentary_debate`, `council_of_state`) decide nothing, `_eff_determine` declines a Record (`arrangements.yaml:265-271`) | B24a.01 (licence by count); the debate itself as exchanges: no | V12 (partial) |
| A32 | **Two rites** (accusatorial, inquisitorial), each a row of `bears:`, `moves:`, `faults:`, `disclosed:` | PROPOSAL · P4 §3.4 `:160-181`; HEAR_B edit 3 | no | B24.09 (one default rite), B24a.04 (the two values) | V12 |
| A33 | **Stages and pace** of a staged case (plea, proof, definition, justification, judgment; overdue stages mature) | PROPOSAL · P4 §3.5 `:182-207` | no | the case file's stages from the rite (B24a.05) | V12 |
| A34 | **Eighteen families of matter**, three axes every matter carries, and their mapping to the eight kinds; seven entry points from the world into a room | PROPOSAL (reference) · `2026-11-01-social-contest-matters-standpoints-and-fold.md` §2 `:67-186`, §3 `:188-283` | LIVE `DocketItem`; the entry points are measured there, not built | no item cites the file (grep of the v12 parts for `matters-standpoints`, 2026-11-14: none) | NONE |
| A35 | **Standpoints**: nine sources of difference; role is a standpoint toward the occasion; how standpoints become sides | PROPOSAL (reference) · same file §4 `:285-423` | no | no | NONE |
| A36 | **Acclamation**: a gathering before a crowd that decides nothing; what it produces is what those present heard | PROPOSAL · `15_INSTITUTIONS_BYZANTINE_E_accession_recall_and_the_crowd.md` edit 4 `[UNVERIFIED: read through the plan item]` | no | B32.15 (`disposal: none`, `floor: open`), its draw in the `succeed` arm (B32.14; `wp part41_cont.md:117-120`) | V12 |
| A37 | **The lot and the list** (Venetian roll, lot, ballot; three council seats by lot from a warranted list) | PROPOSAL · `15_INSTITUTIONS_VENICE_C_roll_lot_ballot.md` `[UNVERIFIED: through the plan]` | no | B32.27-B32.31 | V12 |
| A38 | **Audit and *quo warranto*** as hearings (an officer answers to those he governed; a held grant pleads its age) | PROPOSAL · `15_INSTITUTIONS_COLONIAL_C_audit_and_charter.md` edit 1 | no | B33.18-B33.20 | V12 |
| A39 | **Historical procedure as stage lists**: Venice's courts and two rites, the Senate, the Great Council's lot-and-ballot, heresy as a contest between crown and church; the inquisitorial process stage by stage, crown inquisitions, weak local legitimacy; thirteen families of pre-1600 decision procedure, each mapped to a `disposal` value | RESEARCH · `research/social_contest_procedures/01_venice_procedure.md` Parts 1-3 `:9-209`; `02_inquisition_heresy_procedure.md` §1-§3 `:11-128`; `04_decision_procedure_catalog.md` §2-§4 `:27-146` | no | no item cites them (grep of the v12 parts for `social_contest_procedures`, `rhetoric_oratory_contest`, `03_persuasion_mechanisms`, 2026-11-14: none) | NONE (input for R4's types) |
| A40 | **Reductive audit**: the 24 configurations reduce to four survivors (a tracked contest before a crowd; before a single burden-bearing judge; a panel ballot; an untracked private tally), "burden is the one variety-bearing parameter" | AUDIT · RED §8 `:216-231` | — | — | reference; against R4 (§6) |
| A41 | **Reductive audit**: venue, adjudicator, audience reduce to two concepts (the Venue row with `Pressure`; the Judge); "audience as a third concept dies" | AUDIT · RED §9 `:233-252` | — | — | reference; against R4 (§6) |

### 2.B The six attribute roles (R1, R2, R5)

**What the live social roll reads today** (for every B row): the pool is one attribute per verb through
`rosters.yaml: verb_capability` (`:1549-1562`) and `vocation_attribute` (`:1664-1667`): `tell`, `speak` → `copying` →
**Focus**; `argue`, `determine` → `argue` → **Presence** (Charisma); `interrogate`, `research`, `examine`, `surveil` →
`inquiry` → **Reason**; `lie` and `arrest` (`arms` → Coordination) fall elsewhere. **Attunement, Grace and Spirit enter the
social roll nowhere**: `opposed_by: {}` ships empty (`rosters.yaml:1668-1676`), and the one Attunement reader in the loop
is a receiver's competence at weighing told claims, shipped at gain 0 (`decision/options.py:1683-1720`). Grep of
`engine/` and `modules/` for `attr.social.grace`, `attr.mind.will` outside tests: only `modules/combat/attributes.py:49-50`.

| # | element | origin · source | in code? | in v12? (handle) | status |
|---|---|---|---|---|---|
| B01 | **Focus** = less likely to be distracted, less likely to let irrelevant information affect choices; low focus lets irrelevant information into a forecast | JORDAN · AR-23, AR-21 (`proposals/2026-11-05-attribute-rulings-by-subject.md:58-63`); ED-IN-0328 | LIVE as the pool of `tell`/`speak` under the reading *faithful reproduction* (`rosters.yaml:1628-1631`), not as staying on topic | `determine` names Focus, "keeping the irrelevant out" (B05.25 interim cell; `2026-11-13-verb-governing-attributes.md:181`); no move or fault in the hearing reads it | V12 (one verb) — R1's *topic* role unbuilt |
| B02 | **Focus defence** (strain absorbed: floor(Focus/2)×3) and **Concentration** = 3×Focus + 2×Spirit, −5 per exchange, −5 more on a loss, *Spent* at 0 (−2D, opponent +1D) | RATIFIED (archived) · v30 §4 Step 4 `:199`, Step 6 `:267-270` | KERNEL `Reserve` is attribute-free (RED §7 `:200-203`) | no | NONE |
| B03 | **Reason** = acuity, logic, understanding of concepts and facts, forecasting, what a choice entails | JORDAN · AR-21; ED-IN-0328 | LIVE as the inquiries' pool (`rosters.yaml:1666`); not in the social contest's arguing verbs | `argue`, `speak`, `tell`, `lie`, `determine` name Reason (B05.24/B05.25 cells, `2026-11-13-verb-governing-attributes.md:112-125, :181`); Jordan's teller point "reason" (B28.34) | V12 |
| B04 | Reason's R1 clause: **account for the opponent's factual circumstances** (resources, office, influence) | JORDAN (R1, 2026-11-14) | no | nearest: "knowledge of the other person" as levels per deed claim held (B28.34 (2), `attributed_deeds`); `rank_gap` and `stakes` obstacle terms (OBS §2 members 5, 6; B05.21 at step 0) — none keyed to Reason | NONE (as a Reason role) |
| B05 | **Cognition (= Reason) is primary before a judge or a panel** | RATIFIED (archived) · v30 §3 `:131-136` | KERNEL display | no | NONE |
| B06 | **Attunement** = understanding others' intentions in the moment and their pursuits, convictions, ambitions; reading an opponent's emotional state; how near he is to admitting defeat | JORDAN · AR-30, AR-38, AR-39, AR-41, AR-42 (`:76-81`) | LIVE only as the receiver's competence (gain 0) | `argue`, `tell`, `lie`, `interrogate` name it (B05.25); Attunement on bonds (B24.41 (5), design) | V12 (partial) |
| B07 | **Attunement informs how the arguer thinks the other is receiving the case and which style to deliver** — a choice-side input, not the pool | JORDAN · ED-IN-0350 (2026-11-05, `registers/editorial_ledger_in.jsonl:129`); `rosters.yaml:1631-1634` ("no code reads yet … owed to CR-92/CR-93") | no | not scheduled: B05.25 puts Attunement IN the averaged roll instead (`2026-11-13…:112`, "Jordan 2026-11-13 puts it in the roll") | NONE (the choice half) |
| B08 | **Appraise**: Attunement (+Recall) against the opponent's Charisma ÷ 2 reads the audience's boost and the adjudicator's armature in coarsening bands (Failure misleads; Partial coarse register; Success dominant axis; Overwhelming plus strength); never the exact weights | RATIFIED (archived) · v30 §4 Step 1 `:154-166`, armature `:188` | KERNEL `K/appraise.py:68-177` | the bench reading: each seat's lean deposited as a claim with a confidence the `insight` SKILL sets, drawn and sometimes wrong (B24.29; HCAP) — a skill, not the attribute | V12 (as a skill) |
| B09 | **First to speak** rolled on Attunement (higher net acts last, the information advantage) | RATIFIED (archived) · v30 §5 `:276-280` (ED-581; v2 `:234-241` had it deterministic) | KERNEL | the sitting orders attendees by the row's `order` (B24.06); no Attunement term | NONE |
| B10 | **Attunement primary with no adjudicator** (private negotiation, personal appeal) | RATIFIED (archived) · v30 §3 `:135` | KERNEL display | no | NONE |
| B11 | **Presence** (Charisma) = charisma, magnetism, social impact | JORDAN · AR-29 (`:87`) | LIVE: the pool of `argue` and `determine` (`rosters.yaml:1665`) | `argue`, `speak`, `carry`, `interrogate` name it (B05.25); Presence on obedience (B24.41 (4), design) | BOTH |
| B12 | **`argue`'s main component is Presence** | JORDAN · ED-IN-0350 | LIVE (`rosters.yaml:1630-1631`) | B05.25 keeps it first of three averaged | BOTH |
| B13 | **Charisma primary before a crowd**; the **Charisma modifier** adds to strain dealt; **Face_max = Charisma × 3** | RATIFIED (archived) · v30 §3 `:134`, §4 `:198`, §4 Step 6 `:247` | KERNEL (Face ceiling a display accessor; RED §7 `:202` "latent crash") | no | NONE |
| B14 | R1 Charisma clause: **being listened to**, compelling **delivery** (as distinct from the case's content) | JORDAN (R1) | no: one draw mixes content and delivery | no split; nearest: P4 "a speech kind chooses its faculty" (P4 §4.7 `:437-456`) | NONE |
| B15 | **Grace** = composure (calm under pressure, nerve), etiquette and manners; being seen as respectable and dignified, tied to royal conduct; a low office with high grace is thought well of; tied to promotion | JORDAN · ED-IN-0328; AR-33, AR-34, AR-35 (`:92-94`); registry comment `references/descriptor_registry.yaml:53` | LIVE: no reader | Grace → regard; promotion through `stance_term` (B24.41 (1), (2), design); `carry`, `speak`, `lie` name Grace (B05.25) | V12 (design + cells) |
| B16 | **Social contests may use Grace; venues may prioritise it; a parliament penalises one who is persuasive but "not doing it right"** | JORDAN · AR-32, AR-36, AR-36a (`:91, :95-96`) | no | the venue standard: shortfall demotes the result, surplus adds nothing (B24.41 (3), design); the `standard` obstacle term, the row's level (OBS §2 member 3; B05.21 at step 0, `wp part8_cont.md:159`) — neither reads Grace | V12 (unkeyed to Grace) |
| B17 | **The two profiles** as a falsifier pair: high Presence, low Grace wins the contest and loses regard; high Grace, low Presence wins regard and loses the contest; low Attunement, high Presence, low Grace forces opinion, unaware and unliked | JORDAN · AR-49, AR-50 (`:104-105`) | no | B24.41 (6) | V12 (design only) |
| B18 | **Spirit** (Will) = staying true to oneself, free of external influence or compulsion; tolerating harm, strain and stress; good results despite poor circumstances; "ignoring obstacle modifiers or adding modifiers to dice pool" | JORDAN · AR-44 (`:100`) | LIVE `attr.mind.will` held, not read by the social roll (`opposed_by: {}`) | the opposing attribute of `tell`, `interrogate`, `determine` (B05.25 `opposed_attribute`, `2026-11-13…:125-127, :181`); a self-plea's accuser opposes on Spirit (B28.35) | V12 (as resistance only) |
| B19 | R1 Will clauses: **keep arguing**, **self-belief**, **not getting rattled in the first place**, **the x factor** | JORDAN (R1) | no | no: v12 has Spirit only as the hearer's resistance (B18); AR-44's "ignoring obstacle modifiers" has no item | NONE |
| B20 | **Spirit is its own group, one key** `attr.spirit.will` | JORDAN (R5 as amended by J-12) | no (`references/descriptor_registry.yaml:47` reads `attr.mind.will`) | B01a.06 — but it also adds `attr.spirit.threadsensitivity` (eleven keys), which J-12 drops (`wp part3.md:51, :161-167`) | V12 (mismatched: §4) |
| B21 | **P4's four faculties** over attributes: eloquence (Charisma .7, Bonds .3), reasoning (Reason .6, Focus .4), reading (Attunement 1.0), composure (Spirit .7, Focus .3); each row weighs the faculties per role and rite (accusatorial prover: eloquence .4, reasoning .4, composure .2; inquisitorial respondent: composure .7, reasoning .3); a written petition weighs no eloquence | PROPOSAL · P4 §3.2 `:80-136` | no | not carried: v12 cites P4 only for B24a items (`wp part28_cont.md`); B05.25 averages per verb instead | NONE — the nearest earlier design to R2 |
| B22 | **Capability within a contest** = attribute + title + office + faction, according to venue and contest type; office both licenses acts and carries weight, venue-keyed; office weight affects roll and obstacle; Presence is the attribute part | JORDAN · R-31, R-38, R-41 (PK `:60, :67, :70`) | LIVE: office modifier no; attribute one per verb | office modifier as a level (B05.20, A-12); attributes per verb (B05.25); title, faction and venue-keying: no | V12 (partial) |
| B23 | **The pool's scale**: across capability, argument, evidence, leverage, standing it should be very hard to hold less than 5D | JORDAN · R-40 (PK `:69`) | no (`pool_default` 2) | base and floor five (A-6): `pool_floor` live 5, `pool_add` live 6, both at control 0 until set (B05.08, `wp part8.md:235-251`) | V12 |
| B24 | **The kernel's binding**: `Pool.size = max(5, 2·faculty + 3)`; `faculty` the only attribute that reaches resolution | CODE-COMMENT · P4 `:88-90` citing `K/resolver.py:184-195`, `K/primitives.py:208-211` | KERNEL | deleted (B24.33) | NONE |
| B25 | **Reductive audit**: Cognition, Charisma, Attunement, Focus, Spirit, Recall all "Flavour"; "either the one line ships … or the §3 attribute table is deleted" | AUDIT · RED §7 `:195-213` | — | — | reference (§6) |
| B26 | **The nine capacities are refused as stats**: they become requirements on steps (acts, held claims, or a dimension of capability); "reading the room is four different things and not a stat" | PROPOSAL · PROC `03_PARAMETERS.md` B.2 `:84-108`, Fig. 17 row `:41` | — | — | reference; against R1 (§6) |
| B27 | **Older attribute refusals**: a contest pool is "a derived score … not a character attribute" (J-13); "ignore their use of attributes" (2026-09-05) | JORDAN, superseded · quoted at P4 `:124-127` | — | — | superseded by R-31, R-41 and R1 (§6) |
| B28 | **Recall** (a v2/v30 attribute): the citation bonus and Appraise | RATIFIED (archived) · v30 `:155, :177` | no (not among the ten) | no | retired |

### 2.C Influence verbs (R3)

| # | element | origin · source | in code? | in v12? (handle) | status |
|---|---|---|---|---|---|
| C01 | **Every argue / speech verb calls the social contest or proceedings subsystem**, because they all concern influencing people | JORDAN (R3, 2026-11-14) | partly: see C02 | contradicted in form by B05.24/B05.25 (C03) | §4 |
| C02 | The verbs that **deal the social roll today**: `tell`, `lie`, `argue`, `speak`, `determine`, `interrogate`, plus `arrest` and the three inquiries (`rosters.yaml: task_difficulty` `:1596-1607`); the prize rows `a standing`, `a proposition`, `a matter` name the provider `social_contest` (`sigma.py:1-5`) | CODE-COMMENT | LIVE (one draw each) | the hearing takes `determine` on `a verdict` (B24.08); `speak` stays the single-draw filing act (B24.08) | BOTH |
| C03 | **Verb kinds**: (a) brute, never rolls; (b) efficacy act, one to three attributes averaged into a generic pool; (c) a hand-off to a subsystem, which reads the person by its own rule. The social verbs are (b); only `fight`, `accept`, `capture`, `march` are (c); `speak` "moves to (c) by its prize row" only when the hearing's nested run reads its own inputs | JORDAN (2026-11-13) + PROPOSAL · `2026-11-13-verb-governing-attributes.md` §0 `:26-75`, §2.8 `:233-246` | no | B05.24, B05.25 | V12 (against R3: §4) |
| C04 | **Fourteen move classes** (frame, assert, support, attack, probe, argue, concede/descend, escalate/translate, bind, withhold, display, assess covertly, side-channel, enforce); five verbs carry a social prize; `persuade`, `lodge`, `declare`, `vote` are not rows | PROPOSAL · PK §2.4 `:164-185` | LIVE: the frame, assert, argue, bind, enforce members | support, attack, concede as hearing moves (B24.03); escalate (B24a.03, B24a.07); withhold (`silence` fault); display, assess covertly, side-channel: no | V12 (partial) |
| C05 | `argue`, `lie`, `conceal` **drawn with a reason on every band**; a lie's bands differ, a caught liar exposed; a cover has a quality | PROPOSAL · `14_VERBS_SOCIAL1_C_persuasion_and_deceit.md` §1-§3 `:41-98` | LIVE `argue`, `lie` rows | B28.10, B28.11, B28.12 | V12 |
| C06 | A **petition carried** to a named room by a draw; forgiveness; a challenge naming its stakes; a commitment's band its strength | PROPOSAL · `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` | LIVE rows, undrawn | B28.04-B28.08 | V12 |
| C07 | A document reaches its addressee; an order obeyed, botched, evaded or defied by a draw; a covenant in force while both keep their word | PROPOSAL · `14_VERBS_SOCIAL1_B_documents_and_obedience.md` | LIVE rows | B28.02, B28.03, B28.09 | V12 |
| C08 | **A lost argument moves the arguer**; a half-landed one is called held; the size of the backward step a setting | PROPOSAL · `16_PESSIMIST_SC_D_an_argument_moves_someone.md` | LIVE `person_q.argued_pursuits` (`queries/person_q.py:723`) moves the hearer only | B27.05-B27.08 | BOTH |
| C09 | **Which ground moves whom**: four hearer traits (moved by evidence, consequence, authority, solidarity) each read only when its condition holds | PROPOSAL · `02_CHAR_which_ground_moves_whom.md` | no (`Person.traits` is v12's B04.07; grep of `engine/season/data/cast.py` for `traits`: none) | B04.07 (seating), B24.35 (the four rows) | V12 — parallels the v30 armature axes (E05) |
| C10 | **The persuasion terms**: the teller's roll by his reason, attunement, knowledge of the other person and of plausibility; the hearer's side by faction, opinion of the teller, fit with his understanding, benefit to him, his pursuits and axes, the teller's seat's rung | JORDAN (2026-11-13) · `2026-11-13-verb-governing-attributes.md` §2.6 `:201-220` | partial readers exist (that table's third column) | B28.34 (design), B28.35 (build, at control) | V12 |
| C11 | **The self-plea is opposed** by the accuser, else the bench's presiding holder | PROPOSAL · same file §2.7 `:222-231` | LIVE: nobody opposes a self-subject (`sigma.py:220-224`) | B28.35 | V12 |
| C12 | **Frank speech's four licensing conditions** (goodwill shown first, private, unrepeated, no visible advantage), a demote-only veto on `speak` whose failures are heard as attack, standing contest, characterisation, self-interest; an office waives it | PROPOSAL · PROC `03_PARAMETERS.md` B.4 `:137-198`; study Fig. 26 | no | no | NONE |
| C13 | **Speech kinds**: the charge ladder's six (deny, cite incompatible, impugn motive, concede fact, concede harm, hand the error back); ten promised; each priced, never refused; **a speech kind chooses its faculty** (plain argument → reasoning; hand the error back → eloquence) | PROPOSAL · `arrangements.yaml:57-97`; PROC `19_PLAN.md` step 7 `[UNVERIFIED]`; P4 §4.7 `:437-456` | LIVE loaded; no runtime reader (grep: only `data/arrangements.py`) | held to `ladder_rungs` (B24.36); the faculty per kind: no | V12 (roster only) |
| C14 | **The approach** on questioning (`press`) and its cost | PROPOSAL · `19_LACUNA_questioning_has_an_approach_and_a_cost.md`; OBS §3 `approach` | no | `interview` as a draw to engage, then the answer (B25.14); the `approach` leverage source's own item `[UNVERIFIED: not found by heading in B25]` | V12 (partial) |
| C15 | **Mass-battle rally** (an Attunement-based action) | RATIFIED-era backlog · v30 §12 `:711` ("belongs in mass_battle_v3"); v2 `:409` | no | no | NONE |
| C16 | **Scene access**: occupancy, precedence by rung of office, appointments, the petition that waits and intensifies | JORDAN (A-63, A-64) + PROPOSAL · `28_CORE_scene_access_A/B/C` | no | B28.16-B28.30 | V12 |

### 2.D Hearing and bench structure

| # | element | origin · source | in code? | in v12? (handle) | status |
|---|---|---|---|---|---|
| D01 | **The sitting**: attendees ordered by the row's `order`; each mover's view, decision, move, fault check, recorded `Exchange`; stops when all rest, effort is spent, or the ladder cannot descend; a **closing draw** that is today's roll with the board added as levels | PROPOSAL · HEAR_B "How a sitting runs" `:139-149` | no (`modules/social_contest/hearing.py` absent) | B24.05, B24.06, B24.10 | V12 |
| D02 | **Moves**: `present`, `answer`, `argue`, `impugn`, `concede`, `rest`; the bench's `rule` and `adjourn`; on a mutual row, `offer` and `accept` | PROPOSAL · HEAR_B `:115-126`; `05_SC_negotiation_scene.md` | no | B24.03, B24.30 | V12 |
| D03 | **The issue ladder** (procedure, fact, definition, justification) and who bears each rung | PROPOSAL · HEAR_B; `audits/05_SC_audit_addendum_B.md:242, :246` | no | B24.03, B24.09 (`bears:`) | V12 |
| D04 | **Faults**: `self_contradiction`, `silence` (two levels against, never an automatic concession), `forgery_found`, `irrelevance` | PROPOSAL · HEAR_B `:128-137` | no | B24.03, B24.06 | V12 |
| D05 | **The bench as seats**: derived from `determine` seats whose scope holds the venue; each seat's `modifier:` an office level; `lean` from his live public commits; each seat balloted (Success for, Failure against, Partial abstains); veto under quorum | JORDAN (A-12, A-14) + PROPOSAL · `U5c_SC_proceedings_residue.md` §6 `:140-165` | LIVE `world_q.judging_set` (`:642`), `declared_votes` (`:737`) as a precondition count | B24.11, B05.20 | BOTH |
| D06 | **Panel weighted by standing** (each juror's ballot counts by its bench weight) | JORDAN (R-2, ED-1057) · v30 §2 `:45`, §12 `:695` | KERNEL `K/dictionaries.py:685-727` | the per-seat ballot carries the seat modifier as a level, not a weight (B24.11) | V12 (different form) |
| D07 | **The bench's reading**, drawn and sometimes wrong, never revealed | PROPOSAL · `05_SC_hearing_capabilities.md` "Insight is a use" `:73-89` | no | B24.29 | V12 |
| D08 | **The case file and its exhibits**: a Record of kind `case`; proof kinds bearing on a rung; corroboration capped; `standing` of an exhibit; first heard at Overwhelming is harder to answer | PROPOSAL · `05_SC_evidence_and_rebuttal_B.md`; CR-61; ADM | LIVE: docket items name no case file | B24.01, B24.17-B24.28, B24a.05 | V12 |
| D09 | **The NPC's decider in the room** and what a move costs him (an item exposed, an enemy made, a concession witnessed, effort) | PROPOSAL · HEAR_B "Who decides" `:151-164` | no | B24.13 (build); B24.12 (cost terms, design; build unscheduled) | V12 (partial) |
| D10 | **Every ending writes**; a sitting is written on the case file and the Event | JORDAN (A-81) + IS · `IS-B2-SC-08` | no | B24.14, B24.38 | V12 |
| D11 | **Verdict ladder**: a sitting that cannot decide leaves a voided stage (mistrial); appeal above on new grounds | PROPOSAL · `19_LACUNA_verdict_ladder_and_reversal.md` | no | B27.12, B27.13 | V12 |
| D12 | A failed determination is counted and dismisses; **one asking per sitting**; nothing re-opened without something new | PROPOSAL · `05_SC_acquittal.md`; PRES §4 | no | B27.01 | V12 |
| D13 | **Whom a verdict serves**: the petitioner, or a seat he names | JORDAN (A-38) | no | B27.11 | V12 |
| D14 | **Negotiation as the same sitting under a mutual row**; `argue` changes what the other believes, never what he does; each party's `oblige` opened by his own act | PROPOSAL · `05_SC_negotiation_scene.md`; A-81 | LIVE `negotiation` row seeded, cannot complete in computed play (H-229, PK `:263`) | B24.30, B24.31; opened by `covenant` (B28.13) | V12 |
| D15 | **Corroboration and coalitions**: a declared ally rolls to add a die; sides with a lead per exchange; a shared Concentration pool | RATIFIED (archived) · v30 §4 Step 2b `:170`, §9.2 `:556-557` | KERNEL | "self or advocate" as a decision row (B24a.08); no coalition sides | V12 (partial) |
| D16 | **Preparation and imported findings**: Attunement + History before the contest; each finding cited adds a die to the first exchange, at most two | RATIFIED (archived) · v30 §9.1 `:541-554` (F-TRANS-11) | no | a citing `speak` files its items by its band (B24.25); FI findings as proofs (B24.22-B24.24) | V12 (partial) |
| D17 | **An advocate absorbs defeat but not a discovered lie**, which attaches to the principal | PROPOSAL · PROC `03_PARAMETERS.md` B.5 `:217-220`; study Fig. 24 | no | B24a.08 ("self or advocate") | V12 (partial) |
| D18 | **Chamber violence** forfeits for the violent party; an outside catastrophe postpones | RATIFIED (archived) · v30 §9.6 `:587`; v2 §9.6 `:327-328` | no | no | NONE (meets R7: a fight in the room) |
| D19 | **Adjudicator's response to thread use**, by the adjudicator's Truth (corrupted, irregular, noted, nothing); a visibility gate | RATIFIED (archived) · v30 §9.4b `:567-580` (ED-667) | no | no | NONE |
| D20 | **Kernel retirement**: the ten checks that the kernel's mechanisms arrived in the hearing, then deletion | PROPOSAL · `05_SC_sc05_kernel_disposition_B.md` | KERNEL present | B24.32, B24.33 | V12 |

### 2.E Exchanges: one roll or a run

| # | element | origin · source | in code? | in v12? (handle) | status |
|---|---|---|---|---|---|
| E01 | **The exchange**: Appraise → choose a style (genre × orientation) → corroborate → argue (both roll; first speaker declares first) → resolve by interaction (CLASH, REINFORCE, CROSS, TIE; an Obscuring win plants a Doubt Marker) → forfeit options (Regroup, Concede a Point) → strain, Face, Concentration | RATIFIED (archived) · v30 §4 `:152-272` | KERNEL `K/resolver.py`, `K/dictionaries.py:270-335` | no | NONE |
| E02 | **One draw per act** (pool against obstacle, `degree_from_net` to four bands; Partial writes a docket matter) | JORDAN (R-5, R-6, R-17, R-22) · PK `:34-35, :46, :51` | LIVE `modules/social_contest/roll.py:197-206` | kept as the closing draw (B24.06) | BOTH |
| E03 | **A run of exchanges with one closing draw** (a sitting's moves, each rolled move its own draw, the board entering the close as levels) | PROPOSAL · HEAR_B `:139-149` | no | B24.06, B24.07 (`sitting_exchanges` 0 = control), B24.37 (leaves 0) | V12 |
| E04 | **Serial acts, one draw each**, as the proceedings design's shape | PROPOSAL (ratified as intent) · PROC; PK `:401` | no | superseded by E03 | — |
| E05 | **Adjudicator armature**: a hidden vector over Evidence, Consequence, Authority, Insinuation; a Style's alignment with it enters as continuous σ-leverage, never a die; gated off where the adjudicator is the opponent | JORDAN (Gate C, 2026-07-02; ED-1062) · v30 §4 Step 3 `:182-188` | KERNEL `K/armature.py:191-451` | no; the hearer-trait rows (B24.35) are the nearest successor | NONE (KERNEL) |
| E06 | **Contest styles** (Precedent, Suppression, Vision, Insinuation) as genre × orientation; **Ciceronian stasis × genre** (only FACT sets Memory primary; only CONSEQUENCE/FEASIBILITY sets Projection; stasis only moves up) | RATIFIED (archived) · v30 §2 Step 2 `:56-68`, §8 CR4 `:519-520` | KERNEL `K/dictionaries.py:76-136`, `K/rhetoric.py:91-230` | no | NONE |
| E07 | **Doubt Marker**, **Terminal Doubt** (ED-1060, open), **CR5 self-Face backfire** on a failed Obscuring move | RATIFIED/OPEN (archived) · v30 `:220-234` | KERNEL `K/dictionaries.py:175-236`, `K/rhetoric.py:413` | no | NONE |
| E08 | **Citation bonus** (+2D a named verifiable source; one use per source in a Grand Contest); **Momentum** spent as successes; a **combined cap** on non-attribute bonuses (KU-1) | RATIFIED (archived) · v30 §4 Step 3 `:177-180`, `:97` | KERNEL partial | a citing `speak` (B24.25); the soft ceiling on all leverage (B05.52-B05.55) | V12 (different form) |
| E09 | **The plea's concession reward through the obstacle** (deny is not best alone) | PROPOSAL · CR-62; P4 §4.4 `:387-409` | no | B24a.06 | V12 |
| E10 | **Chain contests**: a Compromise reopens next season from the last position; deadlock; three compromises make a cold equilibrium | RATIFIED (archived) · v30 §6.3 `:376-391` | no (grep of `K/resolver.py` for `chain`: none) | no; A-80 (entrenchment must move the world) is the ruling it would serve | NONE |
| E11 | **The parts of a speech as stages** (exordium moves reception's goodwill, attention, receptiveness; narratio a ledger claim; partitio declares proofs, undeclared ones price worse; confirmatio/refutatio the opposed roll; peroratio a last high-variance move) | RESEARCH · `research/social_contest_procedures/03_persuasion_mechanisms.md` §1.2 `:21-37` | no | no | NONE |

### 2.F Topic and derailment (R1 Focus)

| # | element | origin · source | in code? | in v12? (handle) | status |
|---|---|---|---|---|---|
| F01 | **Focus as staying on topic**, not pulled from the argument into the irrelevant | JORDAN (R1) | no | no item keys a person's Focus to topic | NONE |
| F02 | **`irrelevance` fault**: an exhibit presented on another rung stands at half; the rite may set a strike count after which off-rung items do not enter | PROPOSAL · HEAR_B `:119`, `:128-137` | no | B24.03, B24.06 | V12 — a board condition; reads no attribute |
| F03 | **Evasion strikes**: deflecting the question is a point of defeat (one strike before an inquisitor or a secret council; disabled before a sovereign) | CODE-COMMENT · `K/modes.py:181-198, :241-256` | KERNEL | no | NONE (KERNEL) |
| F04 | **Nyāya defeat conditions** (*nigrahasthāna*, 22, adjudicated against a checklist; *chala*, *jāti*, *hetvābhāsa*) | RESEARCH · `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md` §5.1 `:202-208`; v30 CR5 `:230` | KERNEL `DefeatCatalogue` (`K/primitives.py:262`) | no | NONE |
| F05 | **Conduct under attack**: answering an immaterial attack concedes its relevance (Q2); faults of "temper, answering more than was asked, being drawn off the matter" (Quintilian VI.4) | RESEARCH · PROC `source/09-figures.md:344-422` (Fig. 9) | no | no | NONE |
| F06 | **Attention under load** (a double-absent capacity: what the room needs at the two moments attention is most committed elsewhere) | RESEARCH · PROC `source/09-figures.md:527-585` (Fig. 12) | no | no | NONE |
| F07 | **Undeclared proofs price worse** (*partitio*; a late addition "faulty and unseemly", DI I.33) | RESEARCH · `03_persuasion_mechanisms.md:32-35` | no | no | NONE |
| F08 | **Concentration** as a Focus-built stamina for the contest | RATIFIED (archived) · v30 `:267-270` | KERNEL attribute-free | no | NONE |

### 2.G Rattle and composure (R1 Attunement, Grace, Will)

| # | element | origin · source | in code? | in v12? (handle) | status |
|---|---|---|---|---|---|
| G01 | **Strain → Face → Rattled**: strain accumulates against Face; at threshold a Rattled mark (−1D per level, cumulative), cleared one per scene of rest; Face restored at scene change; attire and regalia add Face | RATIFIED (archived) · v30 §4 Step 6 `:240-258` | KERNEL: Face is the kernel's Standing, monotone up; no strain channel ("unimplemented in code", `:525-528`) | no | NONE |
| G02 | **Composure = Charisma + 6**; two Rattled marks = socially incapacitated; a Knot may absorb composure damage | RATIFIED then superseded · v2 §4 Step 6 `:213-223`; CR3 retired Composure as the contest tracker (v30 `:242`, `:530-535`) | no | no | superseded |
| G03 | **Spent** (Concentration 0: −2D, opponent +1D) and **Contest Fatigue** after a total defeat (−1D next social roll) | RATIFIED (archived) · v30 `:268-270`, `:310` | KERNEL `[UNVERIFIED]` | no | NONE |
| G04 | **Grace is composure** (calm under pressure, nerve) | JORDAN · ED-IN-0328; registry `:53` | no reader | `lie` names Grace as "the liar's nerve" (B05.25 cell, `2026-11-13…:117`) | V12 (one verb) |
| G05 | **Spirit tolerates harm, strain and stress** | JORDAN · AR-44 | no reader | as resistance to influence only (B05.25 `opposed_attribute`) | V12 (partial) |
| G06 | R1: **what is most likely to rattle the opponent** (Attunement) and **not getting rattled in the first place** (Will) | JORDAN (R1) | no | no rattle state exists in v12 | NONE |
| G07 | **Sitting-local penalties**: `silence` two levels against the silent side; a failed `impugn` a level against the mover for the sitting; a fault's levels against the side at fault | PROPOSAL · HEAR_B `:122-137` | no | B24.06 | V12 — the only rattle-like state planned |
| G08 | **Control of display** under attack ("voluntary control of display — withholding, and releasing deliberately. Not low reactivity"); **anger** is expensive and informational (counterparts concede more to anger; power moderates it) | RESEARCH · PROC `source/09-figures.md:405-421` | no | no | NONE |
| G09 | **Fears are leverage that can be pressed**; "a cornered man breaks toward the feared thing"; "pressure is the gap" | JORDAN (R-19, ED-SC-0035) · PK `:48` | no (grep of `engine/season/**/*.py` for `fear`, tests excluded: one prose hit, `decision/choose.py:412`) | no (grep of the SC and FI batch parts, `_part22` to `_part35`, for `fear`: none) | NONE |
| G10 | **How near the opponent is to breaking** (Attunement) | JORDAN · AR-42 | no | `interrogate` names Attunement on that ground (B05.25 cell, `2026-11-13…:127`) | V12 (one verb) |

### 2.H Venue and occasion (R1 Grace; R4 venue)

| # | element | origin · source | in code? | in v12? (handle) | status |
|---|---|---|---|---|---|
| H01 | **Grace as acting correctly for the venue and occasion**; venues prioritise it; a parliament penalises its lack | JORDAN (R1; AR-36, AR-36a) | no | B24.41 (3) venue standard (design); `standard` term (B05.21, step 0) | V12 (partial, unkeyed to Grace) |
| H02 | **`standard`: what the room demands**, the docketed arrangement row's level, an obstacle term on acts an audience hears | PROPOSAL · OBS §2 member 3 `:138`; `05_SC_obstacle_difficulty_and_modifiers_B.md` | no (`arrangements.yaml` rows carry no `standard:`) | B05.21; the two COL_C rows carry `standard:` (B33.18) | V12 |
| H03 | **The register matrix**: no safe manner; each manner is heard as its misreading (fluent → insincere; blunt → unsystematic; erudite → boastful …); the capacity is knowing which misreading one's own manner invites | RESEARCH · PROC `source/09-figures.md:317-342` (Fig. 8, Han Feizi 3) | no; the `registers[]` key was deleted (`arrangements.yaml:8-12`) | no | NONE |
| H04 | **Decorum beats utility** (Quintilian XI.1.8-11: expediency must yield to what is becoming); the *vir bonus*: perceived goodness is the strongest influence | RESEARCH · `03_persuasion_mechanisms.md` §1.3 `:39-50` | no | no | NONE |
| H05 | **Register checked against decorum**: the wrong register for the occasion succeeds at nothing and costs ethos | AUDIT-SOURCE · `.audit/2026-08-06-social-contest-three-lens-audit/sources/04_negotiation_and_persuasion.md` §4 N11 `:282-289` | no | no (rejected as a ladder: `03_persuasion_documents_adjudication.md:255-257`) | NONE |
| H06 | **Occasion-typed speech templates** (taking office, welcoming dignitaries, swearing peace, pleading a cause) | RESEARCH · `rhetoric_oratory_contest_research.md` §6.2 `:255-257` | no | no | NONE |
| H07 | **The venue is a rung, and the rung ordinal is the parameter**; people travel to it | PROPOSAL · PROC `03_PARAMETERS.md` C.1 `:327-391`; JORDAN R-27 ("a rung has never been a place") | LIVE `venue_min_rank` loaded, unread | `[UNVERIFIED: readers in B32/B33/B40]` | partial |
| H08 | **Buildings** (court, chancery, cathedral, chapter house, guildhall, moot hall, keep…) with the institution each serves | CODE (authored for play, ED-IN-0223) · `engine/season/venues.yaml:64-119` | LIVE for seating people only | no proceeding reads a building | LIVE (no rhetorical role) |
| H09 | **Precedence and seating settled before speech** (Kautilya; Liudprand) | RESEARCH · PK `:390` | no | precedence by rung of office on one person's lap (B28.21, A-64) | V12 (partial) |
| H10 | **The rhythm of an occasion**: a proceeding that never leaves its opening phase fails whatever its parts | RESEARCH · PROC `source/09-figures.md:886-891` (Fig. 17 B3) | no | no | NONE |
| H11 | **`ceremony` and `office` as interpositions**; an office waives frank speech's conditions | PROPOSAL · `arrangements.yaml:281`; PROC `03_PARAMETERS.md:149-156` | LIVE loaded, unread | no | NONE |

### 2.I Audience types (R4)

| # | element | origin · source | in code? | in v12? (handle) | status |
|---|---|---|---|---|---|
| I01 | **The audience as a parameter of the proceeding** | JORDAN (R4) | no | no audience typing | NONE |
| I02 | **A crowd as an adjudicator type** (reacts to delivery and force) | RATIFIED (archived) · v30 §2 Step 1 `:43` | KERNEL (a crowd is a `Panel`, `K/modes.py:440-447`) | no | NONE (KERNEL) |
| I03 | **The room's reception** (the bench's disposition toward the speaker) as an obstacle term; its favourable half as leverage | PROPOSAL (SC-02) · OBS §2 member 8, §3 `favour` | LIVE `reception_gain · reception` subtracted (`roll.py:175`; `sigma.py:215-218`) | re-sourced from commits (B24.02); favour as leverage, hostile room as a term (B05.17) | BOTH |
| I04 | **Floor**: open, closed, admitted | PROPOSAL · PROC `03_PARAMETERS.md` Part D | LIVE loaded, unread | `[UNVERIFIED: readers in B32/B33]` | partial |
| I05 | **Two reaches**: who witnessed the arguing and who learns the ruling | JORDAN (2026-09-06) · PROC `03_PARAMETERS.md` B.7 `:249-293` | LIVE WITNESS deposits to those present; `disposal_reach` unread | `[UNVERIFIED]` | partial |
| I06 | **Route by audience**: a high-stake bench weighs proofs, a distracted crowd weighs cues (rank, count); change made at high elaboration lasts | RESEARCH · `03_persuasion_mechanisms.md` §4 `:137`; `.audit/…/sources/04_negotiation_and_persuasion.md` N3 `:230-238` | no | no | NONE |
| I07 | **Audience type as a prior**: character by age and fortune (youth, age, prime; birth, wealth, power), overridden by what the speaker learns | RESEARCH · `03_persuasion_mechanisms.md` §2.5 `:107-115` | no | no | NONE |
| I08 | **Audience triage before speaking**: the assembly learned or ignorant, each friendly, indifferent or hostile; the opponent superior, equal or inferior; strategy conditioned on the triage | RESEARCH · `rhetoric_oratory_contest_research.md` §5.2 `:210-217` (Caraka) | no | no | NONE |
| I09 | **A body as factions plus indeterminates** (indeterminates courted one by one, cannot win alone) | AUDIT-SOURCE · `.audit/…/sources/04_negotiation_and_persuasion.md` N9 `:268-271` | no | bench seats with `lean` (B24.11) | V12 (partial) |
| I10 | **Social proof** as a count over `commit` edges, never a stored popularity | RESEARCH · `03_persuasion_mechanisms.md` §3 `:125` | no | `lean` per commit for bench seats (B24.11); the `dissent` term over the actor's own ledger (OBS member 13) `[UNVERIFIED: its item]` | V12 (partial) |
| I11 | **Rooms an act is heard by** (`audience_of`; `seat_body`, `residents`) | PROPOSAL · `U5c_VERBS_residue_and_governance_owner.md` §2 | no | B07.04 | V12 |
| I12 | **A crowd that decides nothing** (acclamation) | PROPOSAL · BYZ_E | no | B32.15 | V12 |
| I13 | **Preaching**: mass persuasion under borrowed authority (theme, division, amplification) | RESEARCH · `rhetoric_oratory_contest_research.md` §6.3 `:259-261` | no | no | NONE — nearest to "rallying a crowd" in the research |
| I14 | **Display** (K7): reception before a room with no formal power sets standing; a standing is forbidden as a stake (R-21) | PROPOSAL · PK §3.1 K7 `:308-312` | no | `acclamation` (B32.15) only | V12 (partial) |

### 2.J Verdict systems (R4)

| # | element | origin · source | in code? | in v12? (handle) | status |
|---|---|---|---|---|---|
| J01 | **Persuasion Track bands**; **exchange majority** where there is no tracker; a tied majority stalls with consequences | RATIFIED (archived) · v30 §2 Step 4 `:103`, §6 `:286-288` | KERNEL | no | NONE |
| J02 | **Win conditions**: `ProofBar`, `ThresholdRace`, `TallyAtClose`, `GraceThreshold`, `VoteAtClose` (jurors, noise, sharpness) | CODE-COMMENT · `K/modes.py:66-85, :121-140, :254` | KERNEL | no | NONE (KERNEL) |
| J03 | **One draw → four bands** by `degree_from_net`, the single owner | JORDAN (R-5) | LIVE | kept (B24.06) | BOTH |
| J04 | **A declared row needs `quorum` live commits** before `determine` forms | PROPOSAL (v11 CR-34) | LIVE `world_q.declared_votes` (`:737`), `arrangements.yaml:265-274` | replaced: "the count is no longer a gate; it is the odds" (B24.11 step 4) | BOTH |
| J05 | **Each seat balloted**: Success for, Failure against, Partial abstains; veto under quorum demotes to Failure | JORDAN (A-14) + PROPOSAL · PRES §6 | no | B24.06, B24.11 | V12 |
| J06 | **A count licenses or blocks the owner's own act** (consent, not command; no declaring verb, no stored tally) | JORDAN (R-29) · PK `:58` | no | B24a.01 | V12 |
| J07 | **Mutual agreement** (both commit) or impasse; an undecided outcome is legitimate | JORDAN (R-1) + PROPOSAL | LIVE row; cannot complete (H-229) | B24.30, B24.31 | V12 |
| J08 | **Lot**; **conclave and graded count** | PROPOSAL · VEN_C; PAP_B | no | B32.30; B32.20 | V12 |
| J09 | **Many matters, a vector of verdicts** ("win on one thing but partially lose three items and lose completely on five") | JORDAN (R-11) · PK `:40` | the per-matter ceiling only (H-213, `roll.py:107-110`) | the bundle's design (B27.14) | V12 (design) |
| J10 | **Mistrial** (a voided stage); **appeal above on new grounds** | PROPOSAL · `19_LACUNA_verdict_ladder_and_reversal.md` | no | B27.12, B27.13 | V12 |
| J11 | **Consensus, then lot, then majority** (the Althing cascade; 3-mark fines for procedural failure) | RESEARCH · PK `:385` | no | no | NONE |
| J12 | **Deliberation dynamics**: the first ballot predicts; majorities press normatively and informationally, minorities informationally only; movement accelerates; the first crossing to the minority is the one reversal | AUDIT-SOURCE · `.audit/…/sources/04_negotiation_and_persuasion.md` N10 `:273-280`; ranked first in `03_persuasion_documents_adjudication.md:149-153` | no | no: each seat draws once, independently (B24.11) | NONE |
| J13 | **Story model**: jurors build a causal narrative and accept by coverage and coherence; proof order shifts verdicts (78 % against 31 % in the 1988 mock-juror study, secondary) | RESEARCH · `03_persuasion_mechanisms.md` §4 `:139` | no | no | NONE |
| J14 | **Proof regimes**: two witnesses a full proof, confession "queen of proofs"; ordeal refused | RESEARCH · PK `:272`, `:379` | no | proof kinds and corroboration cap (B24.17); a withheld confession is no proof (B24.23); a confession on file by degree (B25.10) | V12 (partial) |
| J15 | **Thirteen decision-procedure families** (sortition, the athwart pair, council deliberation, assembly democracy, consensus, parliaments and estates, designated electors, succession, competitive examination …), each mapped to a `disposal` value | RESEARCH · `research/social_contest_procedures/04_decision_procedure_catalog.md` §2-§4 `:27-146` | no | no | NONE |
| J16 | **`records_dissent`** (whether a division is recorded; one key for the old `verdict_reasons`) | PROPOSAL · `arrangements.yaml:8-15` | LIVE loaded, unread | `[UNVERIFIED]` | partial |

### 2.K What a contest leaves behind

| # | element | origin · source | in code? | in v12? (handle) | status |
|---|---|---|---|---|---|
| K01 | **Obligations**: a decisive win binds the loser to a verifiable commitment for a term; violation costs; an NPC faction's priority tree is blocked from violating it; Wager obligations; interruption by death or collapse | RATIFIED (archived) · v30 §6.1 `:314-366`, §6.1.1 `:342-360` | LIVE `oblige` as a disposal (`arrangements.yaml:118, :306`) | each party's `oblige` by his own act (B24.31); what a sentence shares with a job (B27.26) | BOTH (partial) |
| K02 | **Domain echo** by winning genre (Memory → Mandate; Projection → +1D first Domain Action), magnitude from the band | JORDAN (ED-SC-0002) · v30 §6 `:298-308` | no | no | NONE |
| K03 | **Thread co-movement** by winning genre; **practitioner weaving** in a contest (+1D per 30 thread sensitivity; the Church may file on observation) | RATIFIED (archived) · v30 §6 `:290-295`, §9.3 `:559-560` | no | no | NONE (meets R5: `prac.thread_sensitivity` is the operand) |
| K04 | **A Conviction Scar** reached by an argument, signalled to the player | RATIFIED (archived) · v30 §6.2 `:368-372` | `[UNVERIFIED]` | a scar is a wound (B10.07, `wp part12.md:244`); the argument-to-scar route and its signal: `[UNVERIFIED]` | not established |
| K05 | **Opinion drift is world impact** ("even if it is just a change in opinions") | JORDAN (R-26) | LIVE `argued_pursuits` on the hearer | the arguer moved too (B27.05-B27.08) | BOTH |
| K06 | **The ruling is a durable object** (moved, copied, forged, seized, burned) | JORDAN (S-5, 2026-09-06) · PK `:84` | no (a contest leaves stat deltas or claims) | the case file as a Record (B24a.05); a vetoed motion a citable record (B27.21) | V12 |
| K07 | **Every scene writes** | JORDAN (A-81) | partial | B24.38 | V12 |
| K08 | **Attribution**: was the decision attributed to the persuader (decays, accrues a grievance) or self-attributed (durable, no resentment) | AUDIT-SOURCE · `.audit/…/sources/05_persuasion_in_the_era_sources.md` N16 `:155-159`; ranked second in `03_persuasion_documents_adjudication.md:149-155` | no | no (grep of every v12 part for `N16`, `self-attributed`: none) | NONE |

### 2.L Fragments in other subsystems' designs (each with the proceeding type it would belong to)

| # | fragment | origin · source | belongs to | in code? | in v12? | status |
|---|---|---|---|---|---|---|
| L01 | **Inquisitor ranks**: a Junior Inquisitor's initiation is a theological examination of a named suspect (a social contest, Ob 2); an Inquisitor may initiate heresy proceedings against non-leadership figures, a Senior one against Standing 4+ with a Cardinal's authorisation; a Bishop's Delegate holds ecclesiastical trials wherever the Church is present | RATIFIED (archived) · `.designs/systems/factions/reference/faction_politics_v30.md:523-525, :836` | heresy trial (who may open one, where) | partly: a church seat may open a case (B24a.04 builds the scope) | B24a.04, B32.17 | V12 (partial) |
| L02 | **Public Doctrinal Defense**: defending a theological position in public, "a form of Grand Debate", Ob 2, against a named opponent, as a Church rank requirement | RATIFIED (archived) · same file `:337` | a public disputation (scholastic) | no | no | NONE |
| L03 | **Heresy Investigation as a mandatory zoom-in**: the Inquisitor arrives; an interrogation scene (asymmetric contest per §7); resist, comply or redirect | RATIFIED (archived) · `.designs/systems/npcs/reference/npc_behavior_v30.md:140` (and `scale_transitions_v30` §4.3.2, cited at v30 `:497`) | heresy trial (the interrogation stage) | `interrogate` drawn (LIVE, one roll) | B25.11 (whose custody); interrogation row (`arrangements.yaml:217-229`) | BOTH (partial) |
| L04 | **Resonant style**: what an NPC's conviction leaves him open to (Evidence, Consequence, Authority, Solidarity — the last only through an active Knot), mapped to contest styles | RATIFIED (archived) · `.designs/systems/npcs/reference/npc_behavior_v30.md` §1.3 `:40-47` | every kind with a person target (R1 Attunement: what moves this man) | no | the four hearer traits `moved_by_*` (B24.35) are its successor | V12 |
| L05 | **Parliamentary Territory Transfer**: proposer's Influence against the holder's Legitimacy + 2; four bands (transfer and Legitimacy −1; transfer; a fresh casus belli; Stability −1 and holder Legitimacy +1); last-territory and self-transfer blocks | RATIFIED (archived, "CANONICAL — Pass 2h 2026-05-17") · `.designs/systems/factions/reference/parliamentary_transfer_v30.md` §1 `:28-56` | parliamentary debate at the realm rung (a motion's consequence) | no | land and seats on a won march (FA batches) `[UNVERIFIED: any item carries the parliamentary route]` | NONE |
| L06 | **Knot as a composure buffer**: a bond partner absorbs social strain; "Break Composure" damage 4 | RATIFIED (archived) · `.designs/systems/fieldwork/reference/knots_v30.md:55-64, :106`; v30 `:530-535` | every kind (the rattle economy) | no | a tie weighs the teller (B25.20, at 0) | NONE (as a buffer) |
| L07 | **Royal audience, parliamentary session, church inquiry, court** named as the formal adjudicated proceedings that respond to thread use; tavern arguments and private talk are not adjudicated | RATIFIED (archived) · v30 §9.4b `:569, :578` | a closed list of adjudicated venues | no | no | NONE |
| L08 | **Niflhel cannot enter formal or grand contests**; a private negotiation only, Attunement-primary | RATIFIED (archived) · v30 §9.7 `:589-593` | who may be a party (a faction-keyed eligibility) | no | no | NONE |

## 3. Designed, not in code, not in v12 — ranked by how much of Jordan's ruling each carries

"Not in code" here means not on the live path; `KERNEL` material counts as not in code (it is code the game does not
run, and v12 deletes it at B24.33). Rank 1 carries the most of R1–R4.

1. **P4's faculty layer** (B21; P4 §3.2 `:80-136`, §4.7 `:437-456`, §4.11 `:497-511`): attributes feed four faculties
   (eloquence, reasoning, reading, composure); each arrangement row weighs those faculties **per role and per rite**; **a
   speech kind chooses its faculty**; a written petition weighs no eloquence. It is the only earlier design in which the
   attribute that matters changes with the proceeding and with the move, which is what R2 asks ("in the manner that I
   specified") and what R4's "how and what kind of arguments" needs. It carries Charisma (eloquence), Reason (reasoning),
   Attunement (reading), Will (composure) and Focus (inside reasoning and composure); it has no place for Grace, and it
   predates the ten attributes (it uses Bonds). It worked three characters through every choice and showed that no option
   is dead for all three (P4 `:497-511`).
2. **The proceeding parameter space in the kernel and v30** (A02-A04, A06-A10, A15-A17; J01-J02): eight proceedings, four
   adjudicator types each with its primary attribute, asymmetric role assignment, and — in code — four venue presets, three
   institutional regimes and six cross-cultural venues, each a row of ethos/pathos/logos weights, temporal register,
   starting stasis, win condition and fault catalogue (`K/modes.py:66-325`). This is the nearest existing thing to R4's
   list (venue, adjudicators, audience, verdict system, order) and it includes a crowd (`public_oration`, a crowd of 15
   deciding by who wins the room) and a heresy hearing (`inquisition_hearing`, `ProofBar`, one evasion strike). B24.33
   deletes it; B24.32's ten checks carry none of the venue presets, win conditions, adjudicator types or crowds
   (`wp part22_cont.md:58-82`).
3. **The composure economy** (G01, G03, B02, B13, F08; v30 `:197-270`): strain dealt by the winner's Charisma and absorbed
   by the loser's Focus, accumulating against Face, producing Rattled marks (−1D each) and, on Concentration's exhaustion,
   Spent. It is the only design anywhere for R1's "rattle", "remaining composed" and "not getting rattled", and for Focus
   as sustained attention. Its arithmetic is the archived whole-dice ladder (×3 constants, flat −1D): it needs recasting
   onto R6's continuous levels.
4. **Appraise and the adjudicator armature** (B08, E05; v30 `:154-188`; `K/appraise.py`, `K/armature.py`): reading what
   moves this judge, in coarsening bands, with the exact weights never revealed; the chosen style's alignment entering as
   continuous σ-leverage. It is R1's Attunement clause "identifying what kind of argumentation is most effective for
   audience, adjudicator, opponent" already built as a mechanism; v12's bench reading (B24.29) keeps only the reveal of
   each seat's lean, through a skill.
5. **Frank speech, register and decorum** (C12, H03, H04, H05): the four licensing conditions on frank speech with a named
   misreading for each failure; the register matrix (each manner is heard as its own misreading); decorum over utility;
   the wrong register for the occasion costs ethos. Together they are the designed content of R1's Grace ("correct manner
   for the venue and occasion", "seen as respectable"). None reaches code or v12.
6. **Faults for deflection** (F03, F04): evasion strikes per venue, the Nyāya defeat conditions. They are R1's Focus
   ("not being pulled away from argument into something irrelevant") seen from the fault side; v12 keeps only
   `irrelevance` as a board condition (F02).
7. **Deliberation dynamics** (J12; N10): first ballot, majority and minority influence, acceleration, the first crossing
   as the one reversal. R4's "what system is used to render a verdict" for every body larger than one; ranked first of
   twenty by its own adjudication (`03_persuasion_documents_adjudication.md:149-153`). v12 draws each seat once, apart.
8. **The heresy-trial procedure** (A11, A13, A12's prerequisites): the investigation lifecycle across seasons, its eight
   closure conditions, one investigation per target per jurisdiction, the Parliamentary Stay. R4's "heresy trial".
9. **Audience typing** (I06, I07, I08, I13): route by audience (proofs for a high-stake bench, cues for a crowd), the
   age-and-fortune prior, the Caraka triage (learned or ignorant, friendly, indifferent or hostile), preaching as mass
   persuasion. R4's "who the audience is" and R1's Attunement ("read the room").
10. **Attribution** (K08; N16) and **supplication** (N17): whether the hearer believes he decided himself; the public
    humility that binds the stronger party, the wrong form for the community failing. Grace and Attunement in R1's sense.
11. **What follows a contest** (K02, K03): domain echo by genre, thread co-movement, practitioner weaving (an operand
    `prac.thread_sensitivity` now carries, R5 as amended).
12. **Chain contests, chamber violence** (E10, D18): a compromise reopening; violence in the chamber forfeits (R7's
    boundary between a contest and a fight).
13. **Interposition and latitude** (A23): what stands between a person and the exchange sets how much he matters.
14. **Matter families and standpoints** (A34, A35).
15. **Mass-battle rally** (C15), an Attunement action, never specified.

## 4. In v12, but not matching R1–R7 (an item that contradicts or under-delivers; the sentence named)

1. **B05.24 / B05.25 against R3** (*"argue/speech/etc verbs should all be calling the social contest/proceedings
   subsystem"*). B05.24 classes the social verbs as kind (b), efficacy acts that roll a generic pool of one to three
   averaged attributes, and reserves kind (c), the hand-off whose subsystem "reads the person by its own rule", for
   `fight`, `accept`, `capture`, `march` (`wp part8.md:288-302`; `2026-11-13-verb-governing-attributes.md:233-246`).
   `speak` moves to (c) only "when the hearing scene's nested run is built and reads its own inputs"; `argue`, `tell`,
   `lie`, `interrogate`, `determine` never do. Under R3 every one of them is a hand-off, so the subsystem, not the verb row,
   decides which attribute does what; J-11 (2026-11-14) makes `tell`, `lie` and `speak` "abridged auto proceedings", and the
   verb-pass ruling B05.24 itself carries exempts "a verb [that] calls into being a subsystem" from the averaged pool.
   B05.24's table therefore has the social rows in the wrong kind by Jordan's own exception.
2. **B05.25 against R1/R2** (*"the subsystem needs to be using all of these attributes in the manner that I specified"*).
   Averaging (`governing_mean`) makes each named attribute an equal share of one number. R1 gives each attribute a
   different job (staying on topic, building the case, reading, delivery, decorum and composure, persistence); a mean
   cannot express a job. Concretely: `argue` = mean(Presence, Attunement, Reason) puts Attunement into the dice, against
   ED-IN-0350's "attunement informs how character thinks the other character is receiving it and the best style of
   argument to deliver" (B07); Focus, Grace and Will are absent from `argue`; Will appears only as the hearer's
   `opposed_attribute`.
3. **B24.04 / B24.10 (the hearing's pools) against R2**: each rolled move draws on a SKILL (`argue` or `law` by rung;
   `impugn` → `argue`), and the speaker's pools are "the skills `hearing_moves`' `capability:` column names"
   (`wp part22.md:171-183, :269`). No move reads a role-specific attribute; the `irrelevance` fault reads the board, not the
   speaker's Focus (F02); nothing reads Grace or Will in the room.
4. **B24.29 against R1 Attunement** ("reading their intent, being able to read the room"): the bench reading's confidence
   is set by the `insight` skill (`{use: bench_reading, … key: insight}`, `wp part22_cont.md:12`), not by Attunement; and it
   reads seats' leans only, not the opponent's intent or "what is most likely to rattle" him.
5. **B24.41 and B24.12 are design-only, their builds unscheduled** (`wp part22_cont.md:216-230`: "Its builds are not
   scheduled in v12"; `wp part22.md:315`). Grace's venue role (R1, AR-36a), Grace on regard, the profile pair and the cost
   of a move in the room do not reach code in v12.
6. **B24.32 / B24.33 against R4**: the ten checks that license deleting the kernel test the hearing's own mechanisms
   (standing, concession, off-rung half weight, answer, silence, `bears`, ballots, effort, run shapes) and none of the
   kernel's proceeding parameters (venue presets, win conditions, adjudicator types, crowds, armature, composure). The
   deletion removes the one coded catalogue of proceeding types without carrying it; KERN_B's own falsifier ("if any of
   the ten checks cannot be written … that mechanism was not carried") does not see what is not on the list.
7. **B24.11 against R4 and R-2**: a bench is seats balloted one by one, each a separate draw; there is no adjudicator
   type, no crowd, no audience distinct from the bench, and the standing weight R-2 ruled for a panel (ED-1057) becomes a
   seat modifier level. Deliberation among seats (J12) is absent.
8. **B01a.06 against R5 as amended by J-12**: it adds `attr.spirit.threadsensitivity` and counts eleven attributes
   (`wp part3.md:51, :161-167`); J-12: *"drop threadsensitivity, keep existing prac.thread_sensitivity"*.
9. **B28.34 / B28.35 against R1 Reason** ("ability to account for opponent's factual circumstances like resources office
   influence"): the opponent's circumstances enter as hearer-side obstacle terms (faction, the seat's rung) and a level per
   deed claim held, at control, none keyed to the speaker's Reason (`wp part35_cont.md:314-349`).
10. **B28.07's words against R7**: "an accepted challenge is spent by the fight it licensed" (`wp part35.md:273`); the
    glossary now says a duel is not a fight (`unified/U1_GLOSSARY.md:385-386`). A vocabulary mismatch, not a mechanism one.
11. **R6 (curves, not centres)**: B24's gate adopts the curve reading (`wp part22.md:20`); A-79's centres are stated as single
    numbers ("an even argument on a routine matter fails 59%, half-lands 16%, carries 25%", `unified/DECISIONS_ANSWERED.md:105`),
    and B05.22 / B05.23 calibrate to targets C1–C8 on "the even line" `[UNVERIFIED: whether those targets are centres or
    curves; the items were read by heading only]`.

## 5. Jordan identified, never designed (each with the nearest existing design to extend)

| part of R1–R4 | nearest existing design | how near |
|---|---|---|
| R1 Focus: **resisting being pulled off the argument** as the speaker's own attribute (an opponent's diversion, an irrelevant attack, an off-rung bait) | HEAR_B's `irrelevance` fault (F02) + the kernel's evasion strikes (F03) + Fig. 9's Q2 / Q6 faults (F05) | the faults exist; no design lets Focus change the chance of committing one, nor names an opponent's move that baits it |
| R1 Reason: **accounting for the opponent's factual circumstances** (resources, office, influence) inside the case | N12 *Weigh* ("estimate the counterpart's real situation: resources, pressures, standing", `.audit/…/sources/05_persuasion_in_the_era_sources.md:126-133`); B28.34's "knowledge of the other person" | N12 states the act; nothing ties it to Reason or to the case's strength |
| R1 Attunement: **what is most likely to rattle the opponent** | N14 Reverse Scale (rejected as specified, `03_persuasion_documents_adjudication.md:251-252`); PK's open D-6; Aristotle's emotions need a precondition, a target and grounds (`03_persuasion_mechanisms.md` §2.4 `:86-105`) | the inverse (a lethal topic) was designed and rejected; a pressable weakness was never designed |
| R1 Attunement: **which kind of argument works on this audience, adjudicator, opponent** as a choice | v30 Appraise + armature (B08, E05); P4's "speech kind chooses its faculty" (C13); ED-IN-0350 | designed for the adjudicator (kernel); never for an opponent or a crowd |
| R1 Charisma: **being listened to** (attention as a precondition) separately from compelling delivery | exordium's three states, goodwill, attention, receptiveness (E11); N3 route (I06) | research only |
| R1 Grace: **remaining composed in the face of difficulty** inside a proceeding | the composure economy (G01) with Charisma and Focus; registry: Grace is composure (G04) | the economy exists but never names Grace |
| R1 Grace: **being seen as respectable** within the room | N20 advocate as evidence (the speaker's character admissible and attacked); B24.41 (1) Grace → regard (design) | the regard half is designed (unscheduled); the in-room half is not |
| R1 Will: **to keep arguing**, **self-belief**, **the x factor** | AR-44 "ignoring obstacle modifiers or adding modifiers to dice pool"; N8 escalation (concede always available and priced); v30 Regroup / Concede a Point (E01) | no design makes persistence a chance or a resource |
| R1 Will: **not getting rattled in the first place** | v30 Focus defence (B02) is the only resistance to strain, and it is Focus | Will's role here was never designed |
| R4: **stakes** as a type parameter (what is at stake sets the kind) | `disposes:` per row (A05); PROC's `stakes_grade` (terminal / costly / free), deleted (`arrangements.yaml:8-12`); OBS member 5 `stakes` | stakes set consequences, never the proceeding's form |
| R4: **which factions are involved** as a type parameter | v30 audience resistance from represented factions (A07); faction boosts (A06); R-34 authority by faction (B24a.04) | authority is keyed to faction; the proceeding's form is not |
| R4: **the order in which arguments and speeches are presented** | `order` key (alternating, rank, scripted; A21); the parts of a speech (E11); N11 arrangement as a slot budget; the story model's order effect (J13) | order of speakers is designed; order of arguments within a case is research only |
| R4: **rallying a crowd** | kernel `public_oration` venue (A17); acclamation (B32.15); preaching (I13); mass-battle rally (C15) | a crowd that decides nothing exists in v12; persuading a crowd to act has no design |
| R4: **one taxonomy from heresy trial to private negotiation to parliamentary debate to a crowd** | PK's eight kinds (A25) × P4's rows (A31-A33) × the kernel's venues (A15-A17) | three partial taxonomies, never joined into one table of parameters |

## 6. Research and psychology

Role keys: **Fo** focus (attention, distraction), **Re** reason (argument quality, evidence), **At** attunement (audience
analysis, reading intent), **Ch** charisma (delivery, source credibility), **Gr** grace (decorum, the venue's norms,
composure), **Wi** will (confidence, resilience, resistance). "Code" means the live path unless `KERNEL` is written.

### 6.0 What "primitive" means here, and whether a persuasion catalogue exists

- **The repo's sense** (CLAUDE.md §0): build from the single-owner primitive; a rule lives once. **The audit's sense**,
  the one the persuasion catalogue uses: *an operation on state that cannot be decomposed without losing its political
  meaning; appears in two independent historical systems, or one and an existing game; can be written as a rule with named
  inputs, resolution and outputs; composes without special-casing*
  (`.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md` §1.6 `:45-56`).
- **A persuasion primitives catalogue exists**: **N1–N20**, in two audit source documents, attached to an earlier
  vocabulary of fourteen mechanisms:
  - `sources/01_political_mechanics_primitives.md` §4 `:259-562`: **P1–P45** in seven families (standing and position;
    argument, "the stasis machine"; procedure; selection; information; obligation and enforcement; exchange);
  - `sources/03_consolidation.md` §2 `:58-114`: P1–P45 distilled to **M1–M14** ("a mechanism is code … a configuration is
    data");
  - `sources/04_negotiation_and_persuasion.md` §4 `:210-290`: **N1–N11** (persuasion psychology and rhetoric);
  - `sources/05_persuasion_in_the_era_sources.md` §2 `:122-179`: **N12–N20** (Guiguzi, Han Feizi, Rome, Carolingian
    supplication, *kishōmon*, Renaissance Italy);
  - adjudicated in `.audit/…/03_persuasion_documents_adjudication.md` §3 `:137-258`: "20 N-primitives → 5 mechanisms", a
    ranked short list, and an unhedged reject list.
- **Two later flattenings** sit beside it: PK §2 `:120-229` (2026-10-30; who is in the room, what is contested, what a
  person brings, move classes, persuasion modes, procedure, what follows), and RED §4 `:100-124` (eleven irreducible
  primitives). The proceedings study adds a **capacity map** of the speaker (nine capacities, PROC
  `source/09-figures.md:527-585`). All are `.audit/` or `proposals/` reference; none is loaded by anything.

### 6.1 The backbone: N1–N20, mapped

"Verdict" is the 2026-08-06 adjudication's (`03_persuasion_documents_adjudication.md` §3.1 `:149-159`, §3.6 `:245-257`).

| N | primitive · definition (abridged) | source | roles | proceeding parameter | mechanic implied | code | v12 | verdict |
|---|---|---|---|---|---|---|---|---|
| N1 | **Mind**: each hearer holds an aim (possibly hidden), a story, an elaboration state, lever susceptibilities, a pressure tolerance, a faction or none | `sources/04` `:214-217` | At (what is read) | audience, adjudicator | per-hearer state, never one number | partial: `Person` pursuits, convictions, ledger | hearer traits (B24.35) | configuration |
| N2 | **Story**: candidate narratives scored by coverage, consistency, per-mind plausibility, completeness (five slots), uniqueness; acceptance by coverage and coherence, confidence by uniqueness | `sources/04` `:219-229` (Pennington and Hastie) | Re | verdict system (a jury's) | coverage-and-coherence acceptance; order effect | no | partial: exhibits stand, contradict, are struck (B24.17-B24.19); fit with the hearer's understanding (B28.34) | rejected as a resolution object |
| N3 | **Route**: elaboration = f(motivation, ability); high → argument quality decides; low → cues decide; high-route change lasts, low-route change decays; "forcing the route" (rush, technicality, a late vote) | `sources/04` `:231-238` (Petty and Cacioppo) | Re vs Ch / Gr; Fo (distraction lowers ability) | audience, stakes, timing | a per-audience switch between proof and cue; durability by route | no | no | short list #4 (the durability half) |
| N4 | **Appeal**: logos (story coverage; high route), ethos (authority, liking, commitment; low route), pathos (reciprocity, social proof, scarcity; low route); unity multiplies | `sources/04` `:240-246` | Re (logos), Ch / Gr (ethos), At / Ch (pathos) | venue's proof weights | channel weights per venue | KERNEL venue `proof_ethos/pathos/logos` (`K/modes.py`); PK: "ruled out as fields" (`:191`) | no | lever map rejected |
| N5 | **Resistance**: a pressure tolerance; force beyond it produces reactance (the mind moves away, the mover loses standing); passive and active inoculation pre-empt a later appeal | `sources/04` `:248-254` (Brehm; McGuire) | Wi (the hearer's), At (sensing the limit) | audience | a ceiling and reversal on pressure; a prior exposure raising a later obstacle | no | Spirit as the hearer's opposing attribute (B05.25) | inoculation half: one of five mechanisms |
| N6 | **Anchor**: the first offer pulls the settlement; three counters; an extreme anchor on compatible preferences leaks | `sources/04` `:256-260` (Galinsky and Mussweiler) | Re, At | negotiation | first-offer reference point | no | an offer stands on the board (B24.30), no anchoring | earmarked behind `settle()` |
| N7 | **Logroll**: trading across issues valued differently; better joint value, rated less attractive | `sources/04` `:262-266` | Re | negotiation; many matters | acceptance against joint value | no | the bundle's design (B27.14) | earmarked |
| N8 | **Arena and escalation**: talk → status → coercion → force; the loser may escalate; concession always available and priced | `sources/04` `:268-272` (Dogs in the Vineyard) | Wi (keep on or concede); R7 (duel, fight) | the proceeding's escalation path | a ladder of arenas with fallout classes | no | challenge → accept → fight (B28.06, B28.07); `concede` (B24.03) | one of five mechanisms (cross-lane) |
| N9 | **Body**: factions (shared aims) and indeterminates (aims undisclosed, courted singly, cannot win alone) | `sources/04` `:274-277` (Reacting to the Past) | At | audience, adjudicators | a partitioned audience | no | seats with `lean` (B24.11) | short list #5 |
| N10 | **Deliberation**: first ballot predicts; majorities press normatively and informationally, minorities informationally only; acceleration; momentum; the first crossing as the one reversal; a tunable verdict asymmetry | `sources/04` `:279-286` (Devine; MacCoun and Kerr) | At (finding the pivotal mind), Ch | verdict system | dynamics after speaking stops | KERNEL `VoteAtClose` (static) | no (independent seat draws, B24.11) | short list #1 |
| N11 | **Arrangement and register**: six slots, each on its own target, under a budget; plain / middle / grand register checked against decorum (the wrong register succeeds at nothing and costs ethos); four closing operations | `sources/04` `:282-289` | Re (narratio, confirmatio), Gr (register, decorum), Ch (peroratio) | order of argument; venue's decorum | a slot budget; a register × venue match | no | no | register ladder rejected |
| N12 | **Read before speaking**: weigh (the counterpart's resources, pressures, standing), gauge (a disguised probe), assess; moves before assessment resolve badly or blind | `sources/05` `:126-133` (Guiguzi) | At, Re (weigh = R1's "account for the opponent's circumstances") | all kinds | assessment as a precondition | no | the bench reading (B24.29) | rejected as a primitive (existing hidden-state economy) |
| N13 | **Open–shut**: disclosure as a move; opening gathers, shutting protects and forces the other to fill the silence | `sources/05` `:135-139` | At, Fo | all kinds | an alternating disclosure choice | no | `present`, `rest`; the `silence` fault (B24.03) | earmarked |
| N14 | **Reverse scale**: each mind has one hidden subject that ends the encounter if touched | `sources/05` `:141-145` (Han Feizi *nilin*) | At | — | a hidden lethal topic | no | no | rejected as specified |
| N15 | **Concealed comprehension**: every move has a legibility; being seen to have read the target is itself harm in a paranoid forum | `sources/05` `:147-152` | At, Gr | venue (autocratic court) | a legibility cost per move | no | no | global form rejected; a venue-scoped fault deferrable |
| N16 | **Attribution**: self-attributed change lasts and leaves no resentment; persuader-attributed change decays and accrues a grievance | `sources/05` `:154-159` | Ch vs At | what follows | an outcome flag | no | no | short list #2 |
| N17 | **Supplication**: public humility costs the supplicant standing and costs the recipient more to refuse; the wrong form for the community fails; hierarchical or equal forms | `sources/05` `:161-165` (Koziol) | Gr | petition (K4) | a binding performance; form × community | KERNEL `GraceThreshold` venues | no (a petition is carried, B28.04) | short list #6 |
| N18 | **Self-cursing bond**: a two-part oath, split; its form escalates as trust falls | `sources/05` `:167-172` (*kishōmon*) | Wi | negotiation, covenant | bond form as a public trust reading | no | commitment and covenant drawn (B28.08, B28.09) | inflation rejected |
| N19 | **Composition contest**: who sits on the deciding body is fought before anything is said, over years | `sources/05` `:174-177` (*album iudicum*, *lex Aurelia*) | — (R4 adjudicators) | adjudicators | prior play writes the bench | no | who may fill a seat (B32.19); lot and list (B32.27-B32.30); membership contests (B27.20, design) | short list #3 |
| N20 | **Advocate as evidence**: the speaker's character is admissible and attacked; taking a case discharges or creates a debt | `sources/05` `:179-` (Roman *patronus*) | Gr, Ch (standing is part of the case) | interposition (advocate) | standing attackable directly | no | `impugn` an exhibit's origin (B24.03); self or advocate (B24a.08) | not ranked |

### 6.2 The fourteen mechanisms M1–M14 (the political vocabulary N attaches to), against code and v12

| M | mechanism | R4 parameter | code | v12 |
|---|---|---|---|---|
| M1 | Standing, per body, spendable, earned | who speaks with weight | `decision/options.py::standing_of` (aggregate, glossary `:106`) | standing passes down a seat (B32.07) |
| M2 | Scope: what a character may bind | authority | `state/gate.py` purview | `scope:` on offices (B24a.04) |
| M3 | Concealed value: a hidden true number, estimated with a band | evidence | `Record.forgery_quality` in the obstacle (`roll.py:180-182`) | the case file's exhibits (B24.17-B24.28) |
| M4 | Probe: narrow one band at a cost | evidence, assessment | the inquiries (`examine`, `research`, `surveil`) | B25, B26 (FI) |
| M5 | Claim with premises, warrant, provenance | argument | `Claim`, `Proposition` | — |
| M6 | Attack: undermine, rebut, undercut | argument kinds | no | `answer`, `impugn` (B24.03) |
| M7 | Gate: the ordered question stack, burden, competence, escape to another forum | issue ladder, burden, forum | no | issue ladder (B24.03), `bears:` (B24.09), forum stage (B24a.07) |
| M8 | Floor: who convenes, frames, speaks when; the slot budget | order, floor | `convene`; `order` key unread | `order` (B24.06) |
| M9 | Block: veto, return unsigned | verdict system | no | veto under quorum (B24.11) |
| M10 | Record: everything emitted is citable | what follows | Records | the case file (B24a.05) |
| M11 | Clock: session, enactment, term | pace | dates, terms | stages mature (B24a.05) |
| M12 | Compliance: declare, decree, roll, detect, sanction | enforcement | `comply`, `evade / defy` rows | drawn (B28.03) |
| M13 | Settlement: reservation, payment, scaled compromise, binding instrument | negotiation | `negotiation` row (cannot complete) | B24.30, B24.31, B28.13, B28.14 |
| M14 | Selection: how a body is constituted | adjudicators | `judging_set` | B32.19-B32.30 |

P1–P45 are not repeated: their families are listed in 6.0, and M1–M14's "Absorbs" column maps each P to its M
(`sources/03_consolidation.md:66-81`).

### 6.3 The speaker's capacities (the proceedings study)

| capacity | definition (abridged) | evidence grade in the study | roles | code | v12 |
|---|---|---|---|---|---|
| 1 calibration of reception | how will I be heard | evidenced; instructed perspective-taking raised confidence, not accuracy | At | no | no |
| 2 institutional classification | what the body's office requires it to decide (forensic, deliberative, epideictic) | propositional, "the cheapest" | Re | `speech_kinds.genres` unread | no |
| 3 elicitation | the read is got, not taken | "the one positive result in twenty-five experiments" | At | no | no |
| 4 evidential discrimination | a rule, not a perception | evidenced | Re | no | proof kinds (B24.17) |
| 5 control of display | withholding and releasing deliberately, "not low reactivity"; "the charisma result is adjacent" | partly evidenced | Ch, Gr, Wi | no | no |
| 6 rank-calibration | what size of claim one is entitled to make | tradition only | Gr | no | `rank_gap` term (OBS member 6) |
| 7 generative reframing | a favourable construction under time pressure | tradition only | Re | no | `construe` drawn (B25.16) |
| 8 memoria | — | tradition only | Re | no | no |
| 9 tempo | whether, when, how fast | tradition only | At | no | no |
| — allocation of attention under load | what the room requires when attention is committed elsewhere | double-absent | Fo | no | no |
| — inhibition | runs through the map: "the perception is available and does not govern the action" | — | Wi, Fo | no | no |

Source: PROC `source/09-figures.md:527-585` (Fig. 12), `:852-914` (Fig. 17). The proceedings design refused these as
stats (B26) and Jordan's R1 now names attributes for most of them: §8 row 3.

### 6.4 Further findings, one line each (role · mechanic · tree or v12)

| finding | source | roles | mechanic implied | in tree / v12 |
|---|---|---|---|---|
| Cicero's three duties (prove, please or win favour, move) are three channels, each with its own failure; style follows duty | `research/social_contest_procedures/03_persuasion_mechanisms.md` §1.1 `:13-19` | Re, Gr, Ch | three channels: leverage from proof, reception, aptness-priced leverage | no |
| Exordium makes the hearer well-disposed, attentive, receptive; *insinuatio* for a hostile or wearied hearer | same §1.2 `:25-26` | At, Ch | a pre-roll moving three reception states | no |
| Decorum beats utility; standing forbids some winning moves (Socrates) | same §1.3 `:43` | Gr | an aptness ceiling set by standing | no |
| Learn the judge's disposition (harsh, mild, pleasant, grave) and use or soften it; class emotions (envy of power, contempt of meanness, hatred of guilt) | same §1.3 `:44` | At | reception keyed to rank and the judge | no |
| "We must be moved ourselves before we attempt to move others" | same §1.3 `:45` | Wi, Ch | conviction as a precondition of pathos | no |
| An emotion needs a precondition in the audience, a named target and believed grounds; remove one and aptness is zero | same §2.4 `:86-105` | At | a three-part aptness test per emotional appeal | no |
| A type table by age and fortune is a prior, replaced by what the speaker learns | same §2.5 `:107-115` | At | a reception prior by rung, age, fortune | no |
| Reciprocity, commitment, social proof, authority, liking, scarcity, unity: each with mechanism, conditions, failure and a candid record (nudging contested after publication-bias correction) | same §3 `:117-131` | At, Ch, Gr | ledger debts, commit counts, office in pool or obstacle, shared faction weighting | partial: commits counted for bench seats (B24.11); office level (B05.20) |
| Reactance (anger plus negative cognitions after a freedom threat) | same §4 `:135` | Wi | pressure with a ceiling and reversal | no |
| Inoculation (a weakened counter-argument builds resistance; decays after two weeks) | same §4 `:136` | Wi, Re | a prior exposure raises the obstacle against that line | no |
| Elaboration likelihood (central versus peripheral) and its critique (unimodel) | same §4 `:137` | Re, Ch | a route flag on reception | no |
| Story model: order of proofs shifts verdicts | same §4 `:139` | Re | proof order shifts reception | no |
| The register matrix: each manner is heard as its misreading | PROC `source/09-figures.md:317-342` | Gr, At | a manner choice with a known misreading per venue | no |
| Conduct under attack: restraint, materiality, reframing, humour (highest return and variance; never at the wretched or the loved), a third party, silence and relocation; anger expensive and informational | PROC `source/09-figures.md:344-422` | Wi, Fo, Re, Gr | a fault table for the attacked speaker | no |
| Frank speech's four licensing conditions and their named failures | PROC `03_PARAMETERS.md` B.4.1 `:163-198` | Gr, At | a demote-only veto with emitted misreadings | no |
| Debate modes *vāda*, *jalpa*, *vitaṇḍā*; 22 defeat conditions | `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md` §5.1 `:202-208` | Fo, Re | mode by standing and audience; defeat by checklist | KERNEL `DefeatCatalogue` |
| Caraka's triage: friendly or hostile debate; the opponent's standing; the assembly learned or ignorant and friendly, indifferent or hostile; strategy conditioned on it | same §5.2 `:210-217` | At | an audience model as setup | no |
| Obstruction is bounded by one's own standing and the situation (Vācaspati) | same §5.3 `:219-221`; v30 CR5 `:230` | Gr | a licence for eristic moves | KERNEL CR5 |
| Occasion-typed public speeches (*ars arengandi*); preaching as mass persuasion under borrowed authority | same §6.2-§6.3 `:255-261` | Gr, Ch | a template per occasion; the crowd sermon | no |
| The petition's register indexed to rank (*ars dictaminis*, *inshā'*: salutatio, captatio benevolentiae, narratio, petitio, conclusio) | PK `:291`; rhetoric research §3.3, §6.1 | Gr | a petition's form graded against rank | no |
| Venice: two rites, the courts' routing, the Senate, lot and ballot; heresy as crown against church | `research/social_contest_procedures/01_venice_procedure.md` | — (R4) | per-proceeding stage lists | lot and list (B32.27-B32.30) |
| The inquisitorial process stage by stage; crown inquisitions; what a hostile place changed | `research/social_contest_procedures/02_inquisition_heresy_procedure.md` | — (R4) | the heresy trial's stages; legitimacy by territory | legitimacy index (B27.19, design) |
| Thirteen families of pre-1600 decision procedure, each a `disposal` value | `research/social_contest_procedures/04_decision_procedure_catalog.md` | — (R4) | the verdict-system roster | no |
| Duel of Wits's scaled compromise; Griftlands's warning that spending resources to influence rolls is "a lot less fun than fighting"; Dogs's flaw ("Give" immediately when losing); Reacting to the Past's audience as players | `research/game_precedent_suite/grounding/burning_wheel_and_griftlands.md` §1-§2; `.audit/…/sources/04_negotiation_and_persuasion.md` §3 `:152-208` | — | design warnings | no |
| The lane's own join: twelve of thirteen arrangement keys UNREACHED; the issue ladder CONTRADICTED in code (its name given to Fig. 27's charge ladder); deliberation dynamics, reception, frank speech UNREACHED | `research/by_lane/SC_social_contest.md` §4 `:197-233` | — | — | stands as of 2026-10-16; v12 reaches some (B24.03, B24.06) |

## 7. Reading list for Fable, in order of importance

1. **PK** — `proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-primitives-and-kinds.md`, whole (413
   lines): §1 (R-1 to R-41, Jordan's contest rulings with dates, `:22-116`), §2 (the primitives, `:120-229`), §3 (the eight
   kinds, `:233-343`), §4 (stage × kind, `:347-363`), §6 (gaps, `:397-409`). The prior collation of this subject; this file
   updates it to today's tree and to R1–R7.
2. **P4** — same directory, `2026-11-01-social-contest-proposal-4-authority-staged.md`: §3.2 (faculties, `:80-136`),
   §3.4-§3.7 (rite, stages, legitimacy, forum, `:160-245`), §4 (the nine choices and §4.11 by character, `:271-511`), §5
   (the kinds as rows, `:513-538`).
3. **The 2026-08-06 persuasion catalogue** — `.audit/2026-08-06-social-contest-three-lens-audit/sources/04_negotiation_and_persuasion.md`
   §2 (`:58-150`), §4 (N1–N11, `:210-290`), §5 (the Table, the Floor, the Verdict, `:293-365`);
   `sources/05_persuasion_in_the_era_sources.md` §1-§3 (`:10-226`); `03_persuasion_documents_adjudication.md` §3
   (`:137-258`).
4. **v30** — `.designs/systems/social_contest/reference/social_contest_v30.md` §2-§7 (`:36-499`), §8 (`:501-535`),
   §9.1-§9.4b (`:539-580`). Its parameter tables and the composure economy.
5. **The kernel, before B24.33 deletes it** — `systems/social_contest/sim/contest/modes.py:60-359` (venues, regimes,
   cross-cultural venues, scaffolds); `dictionaries.py:337-727` (adjudicators, boosts, proceedings, panel);
   `armature.py:191-451`; `appraise.py:68-177`; `primitives.py:11-310`.
6. **The psychology, as mechanism** — `research/social_contest_procedures/03_persuasion_mechanisms.md`, whole (161 lines).
7. **The proceedings study's figures** — `proposals/2026-09-05-proceedings-subsystem/source/09-figures.md`: Fig. 8
   (`:317`), Fig. 9 (`:344`), Fig. 12 (`:527`), Fig. 17 (`:852`), Figs. 23-27 (`:1237-1596`); and
   `03_PARAMETERS.md` Parts B-F (`:57-834`).
8. **Jordan's attribute rulings** — `proposals/2026-11-05-attribute-rulings-by-subject.md:36-114` (AR-21 to AR-50);
   `registers/editorial_ledger_in.jsonl:129` (ED-IN-0350).
9. **The verb-attribute rule v12 carries** — `proposals/2026-11-12-subsystem-audit-suite/proposals/2026-11-13-verb-governing-attributes.md`
   §0 (`:26-75`), §1 (`:76-95`), §2.1 (`:107-131`), §2.6-§2.8 (`:201-246`), §6 (`:322-346`).
10. **The hearing as v12 builds it** — the suite's `05_SC_playable_hearing_B.md` (whole), `05_SC_hearing_capabilities.md`,
    `05_SC_negotiation_scene.md`, `U5c_SC_proceedings_residue.md`, `U5c_SC_one_obstacle_form.md` §2-§3 (`:108-197`); and the
    plan's `workplan_v12_part22.md`, `_part22_cont.md` (B24), `_part28_cont.md:288-466` (B24a), `_part31.md`,
    `_part31_cont.md` (B27), `_part35.md`, `_part35_cont.md` (B28), `_part8.md:288-324` (B05.24, B05.25).
11. **Procedure research for R4's types** — `research/social_contest_procedures/01_venice_procedure.md`,
    `02_inquisition_heresy_procedure.md`, `04_decision_procedure_catalog.md` (each whole; 138-225 lines).
12. **Traditions** — `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md` §1.4, §2.1, §3.3, §4, §5,
    §6 (`:88-262`).
13. **The counter-case** — `.audit/…/04_reductive_audit_primitives_and_foundations.md` §4, §7-§9 (`:100-252`).
14. **Parliament and convening** — `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md` §2-§9
    (`:39-188`); `2026-10-29-reasons-to-convene.md` §4, §7 (`:65-139`).
15. **Matters and standpoints** — `2026-11-01-social-contest-matters-standpoints-and-fold.md` §3-§5 (`:188-610`).
16. **The political primitives** — `.audit/…/sources/01_political_mechanics_primitives.md` §1.6, §2.3, §4 (`:45-562`);
    `sources/03_consolidation.md` §2, §6 (`:58-497`).
17. **The lane's research join** — `research/by_lane/SC_social_contest.md` §4, §7-§8 (`:197-400`).
18. **Rulings and words** — `proposals/2026-11-12-subsystem-audit-suite/unified/DECISIONS_ANSWERED.md` rows A-4, A-5,
    A-6, A-7, A-12, A-14, A-25, A-26, A-38, A-39, A-71, A-79, A-80, A-81, A-98 (`:10-134`); `unified/U1_GLOSSARY.md:385-386`
    (fight, duel).
19. **Fragments elsewhere** — `.designs/systems/factions/reference/faction_politics_v30.md:337, :523-525, :836`;
    `.designs/systems/npcs/reference/npc_behavior_v30.md` §1.3 (`:40-47`), `:140`;
    `.designs/systems/factions/reference/parliamentary_transfer_v30.md` §1.
20. **Game precedent** — `research/game_precedent_suite/grounding/burning_wheel_and_griftlands.md` (whole).

Twenty entries; about 9,000 lines if read in full, of which entries 1-10 are about 5,000.

## 8. Contradictions between earlier designs (two sources deciding one thing differently)

| # | the thing | one source says | the other says | resolved? |
|---|---|---|---|---|
| 1 | Whether "reading the room" is an attribute | v30: Attunement reads the audience and the adjudicator (Appraise, `:154-188`); R1 (2026-11-14): Attunement is "being able to read the room" | PROC `03_PARAMETERS.md` B.2 `:84-108`: the nine capacities are refused as stats; Fig. 17 row `:41`: "reading the room is four different things and not a stat" | R1 is newest and Jordan's; the PROC refusal is superseded in direction, its decomposition kept as content |
| 2 | Attunement's place in `argue` | ED-IN-0350 (2026-11-05): Presence is the pool; Attunement "informs how character thinks the other character is receiving it and the best style of argument to deliver" (`rosters.yaml:1630-1634`) | `2026-11-13-verb-governing-attributes.md:112`: Attunement averaged into the roll ("Jordan 2026-11-13 puts it in the roll"; the teller's roll "is affected by his … attunement", `:203-204`) | not reconciled: two Jordan statements, the second relayed; R1 restates the first's sense |
| 3 | Which attribute is primary | v30 §3 `:127-136`: by adjudicator type | rosters / ED-IN-0350: by verb (`argue` → Presence); P4 §3.2: by faculty weighted per role and rite; B05.25: the mean of one to three per verb | open; R2 decides the principle, not the form |
| 4 | Who speaks first | v2 §5 `:234-241`: deterministic by Attunement (ED-138) | v30 §5 `:276-280`: rolled on Attunement (ED-581); PROC/arrangements: by the row's `order` | v30 superseded v2; the arrangement `order` supersedes both in v12 (B24.06) |
| 5 | Where composure lives | v2 `:215`: Composure = Charisma + 6 | v30 CR3 `:242-258`: retired into Face = Charisma × 3; registry `:53`: Grace is composure; P4 `:103`: the composure faculty = Spirit .7 + Focus .3 | four homes; R1 gives composure to Grace and "not rattled" to Will |
| 6 | Genre: chosen, derived, refused or priced | v30 §2 Step 2-3 `:49-95`: the orator picks a style; the primary genre follows the live stasis | PROC `03_PARAMETERS.md` B.3 `:124-127`: derived from the bench's remit, a mismatched verb refused; PROC `04_VERBS.md:252` (R-16): aptness priced, never refused `[UNVERIFIED: opened only through PK :45]` | R-16 governs the refusal question; "the design documents still disagree on price vs refuse" (`research/by_lane/SC_social_contest.md:217`) |
| 7 | The issue ladder's rungs | v30 / kernel: six grounds, FACT → FEASIBILITY (`K/rhetoric.py:91-160`) | PROC: four, procedural · conjecture · definition · quality (`03_PARAMETERS.md:234`); HEAR_B: procedure · fact · definition · justification (B24.03); `rosters.yaml: ladder_rungs` carries Fig. 27's charge ladder under the name "issue ladder" until B24.03 corrects the note | v12 takes HEAR_B's four; the kernel's six die at B24.33 |
| 8 | How a panel decides | R-2 / ED-1057: one ballot per juror at close, weighted by standing (`K/dictionaries.py:685`) | A-14: a vote is a draw on the voter inside the presiding person's act; PRES §6: each seat balloted with its modifier as a level | A-14 and PRES govern v12; the standing weight survives only as a level |
| 9 | Appeal | R-2 (2026-07-01): "appeals should not be a thing — let the decision ride" | R-35 (2026-10-30), A-39: an appeal to another authority is wanted, on new grounds | resolved by R-35 (PK `:107`) |
| 10 | Whether "audience" is a concept | v30: audience resistance, faction boosts, the crowd as adjudicator (`:43, :76-102`) | RED §9 `:233-252`: "audience as a third concept dies"; OBS: one `reception` term | R4 (2026-11-14) names the audience as a type parameter: against RED |
| 11 | How many kinds of proceeding | kernel: 24 configurations (RED `:220`); PROC: twelve games plus one | RED §8: four survivors; PK and P4: eight kinds (P4 splits K3 into a royal and a heresy tribunal) | open; R4 asks for types by several parameters, closer to the larger counts |
| 12 | Public display | kernel `public_oration` decides by who wins the room (`K/modes.py:166-179`) | PROC demotes public debate to a degenerate case; `disposes: standing` forbidden (R-21; PK `:311`); v12's `acclamation` "decides nothing" | R-21 governs what may be a stake; R4's "rallying a crowd" is not covered by either |
| 13 | What one exchange is | v30's exchange algebra (`:152-272`) | the kernel's bout; the live one draw; PROC's serial acts; HEAR_B's sitting with one closing draw (PK `:401`: "three resolvers share one name") | v12 takes the sitting |
| 14 | The opposed obstacle | R-5 (2026-08-14): the opponent's score ÷ 2 plus modifiers (`roll.py:95-100`) | A-26 / A-79: 0.4 per point of trained score, one rule for fights and arguments | A-79 governs; the live code still reads ÷ 2 |
| 15 | What excommunication disposes | PROC `03_PARAMETERS.md` §E.2: it "severs a `commit`" | #453 §8.1: a `ban` opened by `determine` (`arrangements.yaml:253-258`) | the row takes `ban` (an assumption, revertible) |
| 16 | Whether office adds to a roll | Layer 1 `03_VERBS_AND_LOOPS.md` §A.3: "a seat adds no verb and no modifier"; PROC Fig. 1: standing gates whether one is heard, "never a bonus to a pool" (`03_PARAMETERS.md:25`) | A-12, R-31, R-38: office licenses acts and carries weight, on roll and obstacle | Jordan's; the Layer 1 amendment text is owed (`DECISIONS_ANSWERED.md:18`) |
| 17 | Ethos, pathos, logos | the kernel's venues weight them (`K/modes.py`) | `06_RESOLUTION.md`: ethos and bias are not fields (PK `:191`) | open; the kernel dies at B24.33 |
| 18 | Genres: two or three | v30 RATIFIED the two-genre compression (Memory, Projection; `:523`) | PROC and Aristotle: three, derived from the bench | open |
| 19 | Whether a lie needs a mechanism | PROC `03_PARAMETERS.md` B.5 `:200-220`: "concealment and the lie need no mechanism" | `14_VERBS_SOCIAL1_C` §2: `lie` drawn with its own bands (B28.11); B05.25: Grace is "the liar's nerve" | v12 takes the drawn `lie` |
| 20 | Whether a detailed denial helps | the classical corpus: avoid detailed denial | the study's Fig. 9 (`:351-366`): corrections reduce belief and detailed ones do better | open on Jordan (D-7, PK `:112`) |
| 21 | Face and standing | v30: Face a stored, contest-local tracker reset at the end (`:250`) | S-7 (2026-09-06): standing is derived from stances, never a stored number (PK `:86`, `:154`) | S-7 governs |
| 22 | A panel's default size | `K/modes.py:456` `panel(size=5)` | `jurors=7`, `panel_size=7` (`K/modes.py:115, :127, :144`; RED `:250`) | dies with the kernel |

## 9. What I could not determine

- **Opened only through another document's citation**: PROC `00_DERIVATION.md`, `04_VERBS.md`, `05_PROCEDURE.md`,
  `06_RESOLUTION.md`, `07_THE_GAME.md`, `19_PLAN.md`, `21_RECONCILIATION.md`; every `15_INSTITUTIONS_*` file (read through
  the v12 items that copy them); `14_VERBS_SOCIAL2_*`; `16_PESSIMIST_SC_B`, `_C`, `_E`; `19_LACUNA_*` beyond their plan items;
  `proposals/2026-10-16-attributes-from-scratch*` (a fourteen-attribute roster P4 cites); the `.audit/2026-07-01-contest-*`
  gate packets; `.designs/systems/factions/reference/ci_political_v30.md`, `scale_transitions_v30` §4.3.2 and §5.4.
- **Readers not checked**: whether the institutions items (B32, B33, B40) read `floor`, `disposal_reach`, `venue_min_rank`,
  `interposed`, `records_dissent` at runtime or only write them on rows.
- **R6's reach into B05**: whether B05.22 / B05.23's calibration targets are single centres or curves over generated pairs.
- **Stage 1's findings**: the interrogation was 32 lines at this read; anything it establishes about the live roll later
  in the day is not reflected here.
- **Whether `research/fa_se_historical_precedent_research_v1.md:75-77`'s "13-family catalog"** is fully reproduced by
  `04_decision_procedure_catalog.md` (that file says the original survives and gives its location, §1; I did not open the
  original).
- **G09, K04, L05** are marked in place: a fear reader's absence was checked by grep only; the argument-to-scar route
  and any FA item for parliamentary transfer were not traced.
- **No probe was run**: every "in code" claim rests on reading the cited lines and on greps named in the cell; none
  executed the season loop.

## 10. Counts, and the fan-out

The inventory (§2.A-§2.L) holds the counts below, taken by script over the tables' last column on the finished file
(a row is counted once, by the first status word in that cell; `KERNEL`-only rows count as NONE for the game).

| measure | rows |
|---|---|
| elements in the inventory (§2.A 41, §2.B 28, §2.C 16, §2.D 20, §2.E 11, §2.F 8, §2.G 10, §2.H 11, §2.I 14, §2.J 16, §2.K 8, §2.L 8) | **191** |
| of which Jordan's rulings (origin cell names JORDAN) | 51 |
| in code on the live path (`LIVE` 1 + `BOTH` 18) | **19** (and 4 more `partial`: a key loaded, no reader) |
| in v12 (`V12` 84 + `BOTH` 18) | **102** (many partial; read the cell) |
| in both | **18** |
| missing from both (`NONE`) | **74**, of which 27 exist as kernel code that B24.33 deletes |
| other (reference 4, superseded 2, retired 1, not established 1, a pointer to §4 1, superseded-by-another-row 1) | 10 |

The research section (§6) is not counted above: 20 N-primitives, 14 M-mechanisms, 11 capacity rows and 25 one-line
findings; of the 20 N-primitives, one (N1, the hearer's interior) is partly in code on the live path and two (N4, N17) only in the
kernel; 11 have a partial v12 carrier, 9 have none.

**Fan-out: none.** This lane held no agent-spawning tool; every source was read by this producer. What a second reader
would have added: an independent pass over the `15_INSTITUTIONS_*` and `14_VERBS_SOCIAL2_*` files, which this pass read only
through the plan items that copy them (§9).



