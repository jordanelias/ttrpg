# Attribute derivation: what each practice, verb and subsystem requires of a person, flattened into one list of aptitudes

## Status: PROPOSED (2026-10-16). Not ratified. Merging it ratifies nothing unless Jordan so rules. It recommends; it decides nothing (J-T1 and J-T2 stay Jordan's).
## Lane: IN (cross-cutting), with PC, MB, SC, FI, WR, SE, FA, NPC as sources. IDs: none allocated.
## Read at the working tree of 2026-10-16 (uncommitted edits by sibling sessions present).
## Parts, in reading order: this file (head, §1 the flattened list, §2 practice domains, §3 per-practice interrogation) · [`_part2`](2026-10-16-attribute-derivation_part2.md) (§4 per-verb, §5 per-subsystem interrogation) · [`_part3`](2026-10-16-attribute-derivation_part3.md) (§6–§10, secondary: clusters, cross-tabs, the attribute recommendation, meta-rule, NERS, limits). The flattened list alone: [`_aptitudes`](2026-10-16-attribute-derivation_aptitudes.md).

**What this answers.** Jordan, 2026-10-16: *"perform interrogation of each 'PRA' to identify what kind
of skills/aptitudes are required for each. after doing so, we are to flatten our list and collate all
of these together to see what should be an attribute."* Then: *"like our VERB interrogation is supposed
to be doing this too"*; *"ie WHAT does each verb/subsystem require"*; and *"show me the flattened
aptitude list when it's done. we will work from those to think about attributes we have."* So the
primary deliverable is the flattened list in §1. The attribute recommendation is last, in `_part3`,
and is secondary.

**Words.**

- An **aptitude** is a capacity that underlies both learning and doing: stamina, memory, reading
  people. It is what makes one person better placed than another to do a thing well before either has
  practised it.
- A **practice** is learned domain skill that grows by doing: combat practice, administration,
  copying. In code it is a key of `Person.capability` (`engine/season/state/carriers.py:651`). It is
  the "PRA" code of the character-template proposal.
- A **draw** is one item (a practice domain, a verb or a subsystem) requiring one aptitude. Each item
  draws each aptitude at most once.
- A draw's **role** is how the aptitude would move the outcome: **odds** (it adds to a pool),
  **difficulty/cost** (it sets or resists an obstacle or a cost: wounds, strain, fatigue), **eligibility**
  (a gate or a cap), **effect size** (how much lands), or **resists another** (the person as someone
  else's obstacle).
- This proposal avoids "axis" (the engine's `AXES` roster), "capacity" as a type name, and loose "kind".
  It writes "the nine" for the registry's nine attributes (`references/descriptor_registry.yaml:33-48`).
  Codes STR AGI END FOC ACU WIL ATT CHA BON, and TS, TMP, RES, REC, KIT, are the character template's
  (`proposals/2026-10-16-character-template_part2.md:34-57`).

**Evidence tiers** are the character template's. **T1** is code the season loop runs. **T2** is code
outside the loop (`modules/`, `systems/*/sim/`). **T3** is a ratified specification, a v9 plan
position, or a proposal the plan records as RATIFIED AS INTENT. **T4** is design intent only:
unratified proposals, the quarantined `.designs/` documents, and `research/by_lane/`. Under
`CLAUDE.md` §0.05 no design document shows a behaviour is correct. **Here the sources are cited as
evidence of what a design says an act REQUIRES, which is intent, not mechanism.**

- **NAMED (Tn)**: the source states the requirement, usually as the attribute it rolls and the reason it
  gives, such as the fieldwork design's *"Reasoning"* column (`FW:90-101`).
- **overridden**: named at T4 but overridden for DICE by a higher source. This is almost always the
  2026-09-05 ruling as the proceedings design glosses it (§3 note 1). Each overridden draw is counted
  and flagged.
- **INFERRED**: this proposal's reasoning. An inference never overrides a sourced statement.

**Abbreviated sources** (each opened in this pass unless tagged):

- **FW** `.designs/systems/fieldwork/reference/fieldwork_v30.md`
- **SCV** `.designs/systems/social_contest/reference/social_contest_v30.md` (superseded for dice by the
  T2 contest kernel)
- **HIST** `.designs/systems/characters/reference/character_histories_v30.md` (the lifepath "Histories")
- **MB** `.designs/systems/mass_battle/reference/mass_battle_v30.md`
- **AUG** `proposals/2026-08-15-character-and-faction-stats-and-progression.md`
- `threadwork_v30` is `.designs/systems/threadwork/reference/threadwork_v30.md`.
- The settlement documents are under `.designs/systems/settlements/reference/`.
- Code locators the character template already verified (`combat_systems.py`, `exchange.py`,
  `orchestration.py`, `engine.py`, `knots.py`, `operations.py`) are reused from its `_part2` §A.4 and
  were not re-opened, except `combatant.py:1-110`, which was.

**How the verb interrogation here differs from the character template's matrix.** The template's
verb × personal-input matrix (`2026-10-16-character-template_part2.md` §A.3) asks **what a resolver
READS** off a person, today or in a named stub or design. By that test 43 of 65 verbs read nothing,
and that is a true statement about the code and the sources. This proposal asks **what performing the
act well REQUIRES of the person** when the act is complete, whether or not anything reads it. A verb
the template scores 0 can therefore carry requirements here: 13 of the template's 43 zero rows do (§4,
the rows marked *graded* that the template's matrix omits). Each verb row also keeps two things apart:

- **ACT**: what the act itself asks of the actor;
- **DOMAIN**: which practice domains the act draws, interrogated once each in §3, not repeated per
  verb.

The template's reads stay visible in the column *resolver already names*. Verbs whose quality IS the
choice (`commit`, `confer`, `issue` …) carry no aptitude of their own. Their one requirement, choosing
well, is counted once, at the chooser (S10), and not 24 times. Pure bookkeeping verbs are reported as
such.

**Method, and what was not done.** The brief allowed up to six Sonnet readers for parallel batches.
**None was spawned: this lane's toolset holds no agent-dispatch tool**, so the three interrogations
were done by one reader, from one shared source pack. That costs the independence a fan-out would have
bought on the verdicts. §10 names the critic pass still owed. The interrogation was encoded once as
data. Every count below is reproducible from the evidence tables by the command in §1.

---

## 1. THE FLATTENED APTITUDE LIST (the primary deliverable)

**Key.**

- **One row per atomic aptitude**, ordered by total draws, descending. Ties go to the aptitude with
  more NAMED draws, then alphabetical.
- **Column 3** counts the practice domains (§2–§3) that draw the aptitude. **Column 4** counts verbs
  (§4), with distinct resolvers in brackets. The seven thread operations share one pool and `fight` and
  `accept` share one bout, so a thread aptitude's verb count overstates its breadth; **the bracket and
  column 5, subsystems (§5), are the breadth measures.** In parentheses: the ids of up to three items,
  NAMED and highest tier first.
- **Column 7** shows how many draws a source names (by tier), how many are overridden, and how many
  are inferred.
- **Column 8** maps the aptitude to the nine only where the registry's name or alias, or a source
  using that attribute for that function, says so. Otherwise it reads "none". **The list was NOT bent
  toward the nine** (Jordan: keep it raw). The only merges are exact synonyms, listed under the table.

| # | aptitude: what it is | PRA domains | verbs [distinct resolvers] | subsystems | total | named by source vs inferred | maps to the nine today |
|---|---|---|---|---|---|---|---|
| 1 | **Thread sensitivity** (`thread-sensitivity`, perceptual): perceiving the substrate | 3 (P05, P06, P07) | 10 [4] (#42, #58, #59) | 3 (S05, S04, S09) | 16 | named T2 11·T3 1·T4 4 | none of the nine (TS, a practitioner stat, registry :64) |
| 2 | **Concentration** (`concentration`, cognitive): sustaining mental effort over time; how much one can do in one sitting | 4 (P05, P02, P01) | 9 [3] (#58, #59, #60) | 3 (S05, S03, S04) | 16 | named T4 9; overridden 3; inferred 4 | FOC (+WIL): Concentration = 3·Focus + 2·Spirit (SCV:267); operations per contact = Focus − 1 (threadwork_v30:199) |
| 3 | **Stamina** (`stamina`, physical): sustained exertion before fatigue | 3 (P03, P15, P17) | 6 [5] (#18, #20, #39) | 5 (S01, S04, S09) | 14 | named T2 4·T4 4; inferred 6 | END (+WIL): `stamina_max = 3·end + 2·spirit` (combatant.py:43-44); FW:92 |
| 4 | **Reasoning** (`reasoning`, cognitive): logical and structural analysis | 6 (P08, P09, P19) | 5 [5] (#34, #36, #50) | 3 (S06, S03, S04) | 14 | named T4 5; overridden 6; inferred 3 | ACU (registry alias Reasoning, :42) |
| 5 | **Composure** (`composure`, volitional): keeping steady under pressure, strain or shock | 7 (P03, P02, P04) | 4 [3] (#18, #20, #50) | 3 (S01, S03, S04) | 14 | named T2 4; overridden 3; inferred 7 | FOC (poise recovery, disruption resistance, AUG:90; SCV:199 Focus defence); CHA in FW:640 (Composure = Cha + 6, retired as the contest tracker, SCV:242) |
| 6 | **Reading people** (`reading-people`, perceptual): perceiving another's state, intent or lies | 5 (P09, P10, P16) | 4 [4] (#37, #50, #12) | 5 (S06, S03, S04) | 14 | named T4 4; overridden 6; inferred 4 | ATT (FW:94 "reading people, sensing deception"; SCV:147) |
| 7 | **Will** (`will`, volitional): persistence of intent against resistance; the force a practitioner brings to the thread | 2 (P05, P06) | 9 [3] (#42, #58, #59) | 2 (S05, S04) | 13 | named T2 11·T4 2 | WIL (registry name, alias Spirit) |
| 8 | **Presence** (`presence`, social): bearing that draws attention and carries authority | 4 (P08, P09, P16) | 4 [4] (#32, #50, #52) | 4 (S04, S06, S03) | 12 | named T4 5; overridden 5; inferred 2 | CHA (registry alias Presence, :47; SCV:134; FW:98) |
| 9 | **Observation** (`observation`, perceptual): noticing physical detail | 5 (P04, P07, P08) | 4 [4] (#36, #39, #34) | 1 (S04) | 10 | named T4 1; overridden 4; inferred 5 | ACU (FW:93 Cognition, overridden for dice; HIST:177 Cognition to detect ambush) |
| 10 | **Contact endurance** (`contact-endurance`, volitional): how long one can hold contact with the thread before it breaks | 1 (P05) | 7 [1] (#58, #59, #60) | 1 (S05) | 9 | named T4 9 | WIL (threadwork_v30:195, threshold = Spirit × 5) |
| 11 | **Self-coherence** (`self-coherence`, volitional): resisting the erosion of one's own self under thread strain | 1 (P05) | 6 [1] (#58, #59, #60) | 2 (S05, S09) | 9 | named T2 8·T4 1 | none (RES, `resilience`; plan names "spirit (resilience, R-14)" a candidate input, _part5.md:444) |
| 12 | **Memory** (`memory`, cognitive): retaining and retrieving what one learned or saw | 5 (P13, P02, P07) | 2 [2] (#38, #41) | 2 (S03, S04) | 9 | named T4 1; overridden 6; inferred 2 | none of the nine (Recall, which the registry does not list) |
| 13 | **Patience** (`patience`, volitional): sustaining slow, unrewarded effort | 5 (P07, P09, P11) | 1 [1] (#38) | 3 (S04, S06, S08) | 9 | inferred 9 | none |
| 14 | **Strength** (`strength`, physical): raw force: lifting, striking, grappling, carrying | 3 (P03, P11, P17) | 3 [2] (#18, #20, #45) | 2 (S01, S08) | 8 | named T2 4; inferred 4 | STR (registry name; Impact = Strength + heft, AUG:88) |
| 15 | **Persuasiveness** (`persuasiveness`, social): moving another by appeal or argument | 2 (P16, P10) | 4 [4] (#27, #35, #37) | 2 (S04, S07) | 8 | named T4 2; inferred 6 | CHA (FW:409, Converse rolls Charisma) |
| 16 | **Dexterity** (`dexterity`, physical): fine control of the hands | 3 (P01, P11, P12) | 4 [4] (#13, #30, #48) | 1 (S08) | 8 | inferred 8 | AGI by alias only (registry :39 lists Dexterity as an alias); no code reads `agi` for hand work |
| 17 | **Anticipation** (`anticipation`, perceptual): reading an opponent's next move | 2 (P03, P04) | 3 [2] (#18, #20, #22) | 2 (S01, S02) | 7 | named T2 7 | ACU + ATT (reading `(2·Cog + Att)/3`, AUG:84); in a field, through Command (CHA, ACU) |
| 18 | **Judgment** (`judgment`, cognitive): choosing well under uncertainty and pressure | 2 (P09, P04) | 1 [1] (#22) | 4 (S06, S02, S07) | 7 | named T4 2; inferred 5 | none |
| 19 | **Toughness** (`toughness`, physical): absorbing wounds and pain before failing | 1 (P03) | 2 [1] (#18, #20) | 3 (S01, S05, S09) | 6 | named T2 4·T4 1; inferred 1 | END (+WIL, STR at low weight): `wound_interval`, `health_full` (combatant.py:30-40) |
| 20 | **Numeracy** (`numeracy`, cognitive): reckoning numbers, accounts and value | 3 (P09, P10, P19) | 1 [1] (#12) | 2 (S06, S08) | 6 | inferred 6 | none |
| 21 | **Planning** (`planning`, cognitive): foresight and sequencing toward a goal | 3 (P04, P09, P19) | 1 [1] (#22) | 2 (S02, S06) | 6 | inferred 6 | none (Command's Cognition term is never glossed) |
| 22 | **Balance** (`balance`, physical): footing and whole-body control | 2 (P03, P18) | 2 [1] (#18, #20) | 1 (S01) | 5 | named T2 4·T4 1 | AGI + STR (AUG:86) |
| 23 | **Quickness** (`quickness`, physical): speed of movement and of a body's working tempo | 2 (P03, P18) | 2 [1] (#18, #20) | 1 (S01) | 5 | named T2 4·T4 1 | AGI (tempo `BASE + K·(Agi−4)`, AUG:87) |
| 24 | **Boldness** (`boldness`, volitional): a disposition to press and attack rather than wait (temperament) | 1 (P03) | 2 [1] (#18, #20) | 2 (S01, S10) | 5 | named T2 4; inferred 1 | none (TMP, combat `disp`) |
| 25 | **Spatial sense** (`spatial-sense`, cognitive): pathfinding, maps, positions and ground | 3 (P04, P15, P11) | 0 [0] (—) | 2 (S04, S09) | 5 | named T4 4; inferred 1 | ACU (FW:90 Cognition, "pathfinding, cartography") |
| 26 | **Leadership** (`leadership`, social): getting others to follow, hold and rally | 1 (P04) | 1 [1] (#22) | 3 (S02, S06, S07) | 5 | named T2 3; inferred 2 | CHA (Command, Charisma primary 2:1, exchange.py:57-66; MB:306) |
| 27 | **Empathy** (`empathy`, social): feeling with another; rapport | 3 (P02, P06, P16) | 1 [1] (#37) | 1 (S03) | 5 | overridden 2; inferred 3 | ATT (SCV:147, Appraise is "empathetic perception") |
| 28 | **Verbal fluency** (`verbal-fluency`, cognitive): command of words, spoken and written | 1 (P02) | 3 [3] (#27, #32, #35) | 1 (S03) | 5 | inferred 5 | none |
| 29 | **Hardiness** (`hardiness`, physical): resisting cold, hunger, exposure and sickness | 1 (P15) | 1 [1] (#24) | 2 (S04, S09) | 4 | named T4 4 | END (FW:92 "exposure, harsh terrain"; FW:239) |
| 30 | **Reflexes** (`reflexes`, physical): speed of reaction to what was not foreseen | 1 (P03) | 2 [1] (#18, #20) | 1 (S01) | 4 | named T2 4 | AGI + ATT (reflex blend, AUG:85); FW:106 rolls initiative on ATT |
| 31 | **Relational depth** (`relational-depth`, social): capacity to form and hold deep bonds | 2 (P06, P16) | 1 [1] (#42) | 1 (S04) | 4 | named T2 2·T4 2 | BON (FW:479 "deep relational capacity that Bonds represents"; knots.py:185) |
| 32 | **Discipline** (`discipline`, volitional): self-control: holding to drill, method or practice | 1 (P05) | 1 [1] (#51) | 2 (S02, S05) | 4 | named T4 3; inferred 1 | FOC (HIST:293 Contemplative Focus, "years of discipline") |
| 33 | **Sincerity** (`sincerity`, social): genuineness that others can feel | 2 (P06, P16) | 1 [1] (#35) | 1 (S04) | 4 | named T4 3; inferred 1 | BON by alias (registry :48 Sincerity); but FW:430 rolls Spirit (WIL) for the Sincerity Check |
| 34 | **Situational awareness** (`situational-awareness`, perceptual): tracking many moving parts at once | 1 (P04) | 1 [1] (#22) | 2 (S02, S01) | 4 | named T2 3; inferred 1 | CHA + ACU only through Command as span of control (engine.py:93); none directly |
| 35 | **Discernment** (`discernment`, perceptual): judging how far to credit what one is told or reads | 0 (—) | 2 [2] (#8, #35) | 2 (S10, S03) | 4 | named T3 1; inferred 3 | none (AX-7's reader "competence", input open: J-T9) |
| 36 | **Deception** (`deception`, social): misleading convincingly | 1 (P08) | 2 [2] (#28, #52) | 1 (S04) | 4 | inferred 4 | none (FW rolls CHA for a cover identity, :620, and ACU for Cover, :575) |
| 37 | **Precision** (`precision`, physical): exactness in execution: fine work, copying, forgery | 2 (P01, P11) | 1 [1] (#13) | 1 (S08) | 4 | inferred 4 | none |
| 38 | **Land sense** (`land-sense`, perceptual): reading weather, terrain and soil | 2 (P15, P17) | 0 [0] (—) | 1 (S09) | 3 | named T4 3 | ACU (HIST:314, Seasons Reader rolls Cognition) |
| 39 | **Learning** (`learning`, cognitive): speed of acquiring and deepening a practice | 1 (P14) | 1 [1] (#51) | 1 (S07) | 3 | named T4 1; inferred 2 | none of the nine (Recall, HIST:35; spark check Spirit + Recall/2, HIST:41, so partly WIL) |
| 40 | **Inference** (`inference`, cognitive): assembling partial evidence into a coherent picture | 1 (P07) | 1 [1] (#41) | 1 (S04) | 3 | overridden 3 | none (FW:306 used Recall; overridden for dice) |
| 41 | **Recovery** (`recovery`, physical): regaining strength after strain | 1 (P05) | 0 [0] (—) | 1 (S05) | 2 | named T4 2 | WIL (threadwork_v30:203, meditation reduces fatigue by Spirit) |
| 42 | **Intimidation** (`intimidation`, social): compelling by threat | 0 (—) | 2 [2] (#54, #56) | 0 (—) | 2 | inferred 2 | none |
| 43 | **Quick thinking** (`quick-thinking`, cognitive): finding an apt answer under time pressure | 1 (P02) | 0 [0] (—) | 1 (S03) | 2 | inferred 2 | none |
| 44 | **Breadth** (`breadth`, cognitive): how many practices one can keep in use at once | 0 (—) | 1 [1] (#51) | 0 (—) | 1 | named T4 1 | none (Recall as equip slots, HIST:34, :521) |
| 45 | **Courage** (`courage`, volitional): facing danger without breaking | 0 (—) | 0 [0] (—) | 1 (S02) | 1 | inferred 1 | none |

**Totals.** 45 aptitudes; 303 draws, of which 154 are NAMED (T2 77, T3 2, T4 75), 38 overridden and 111
inferred (T1 0: no aptitude is named by code the season loop runs). The draws come from 19 practice domains, 35 graded verbs (of 65) and 10 subsystems. **Every
draw of patience, dexterity, numeracy, planning, verbal fluency, deception, precision, intimidation,
quick thinking and courage is INFERRED.** No source names those ten as requirements, so their rank
reflects this proposal's reading, not the corpus.

**Merges (exact synonyms only), and the splits the sources forced:**

- *attention span* and *sustained attention* are the same aptitude as `concentration`.
- *nerve* (HIST:312, Haggler's Nerve) and *steadiness* (AUG:478) are the same as `composure`.
- *vigilance* was not coined: it is `observation` sustained by `concentration`.
- **Split, not merged:**
  - *Endurance* splits into `stamina`, `toughness` and `hardiness`, because the sources use the one
    word for three functions: Endurance exploration (FW:92), the wound interval and health
    (`combatant.py:30-40`), and the travel exposure check (FW:239).
  - *Spirit* splits into `will`, `contact-endurance` (threadwork_v30:195) and `recovery`
    (threadwork_v30:203).
  - *Cognition* splits into `reasoning`, `observation`, `spatial-sense` and `land-sense`, by the
    fieldwork design's own *Reasoning* column (FW:90, :93) and HIST:314.
  - *Perception*, the registry's alias for Attunement, is an umbrella word and is not a slug.

**The command that reproduces columns 3–6** from this proposal's own evidence tables. A draw is
written `` `slug` (role, `` in exactly one cell of one evidence row.

```sh
python3 - <<'EOF'
import re, collections
base = 'proposals/2026-10-16-attribute-derivation'
t = open(base + '.md').read() + open(base + '_part2.md').read()
rows = [l for l in t.splitlines() if re.match(r'\| (P\d\d|S\d\d|\d+) \|', l)]
c = collections.Counter()
for l in rows:
    lv = 'P' if l.startswith('| P') else ('S' if l.startswith('| S') else 'V')
    for s in set(re.findall(r'`([a-z-]+)` \((?:odds|difficulty/cost|eligibility|effect size|resists another),', l)):
        c[(s, lv)] += 1
for s in sorted({s for s, _ in c}, key=lambda s: -sum(c[(s, l)] for l in 'PVS')):
    print(s, c[(s, 'P')], c[(s, 'V')], c[(s, 'S')], sum(c[(s, l)] for l in 'PVS'))
EOF
```

---

## 2. STAGE 1: EVERY PRACTICE DOMAIN

**Where a practice can live in code today.**

- `Person.capability: dict` (`carriers.py:651`).
- `rosters.yaml: verb_capability` maps `tell` and `speak` to the one key `copying`
  (`engine/season/rosters.yaml:1082-1107`). Its note: *"WHICH capability key each verb draws on is
  stated nowhere"*.
- `pool_default=2` is what everyone without a key draws (`engine/season/data/fixtures.py:381`).
- One corpus person carries a key: NPC-088, `{copying: 3}`
  (`engine/season/cases/exercises/NPC-088.yaml:30-33`).
- **No `practice_roster` exists in code.** It is the character template's proposed roster (its §6).
- `engine/season/data/cast.py` does not mention `capability`: `git grep -n capability
  engine/season/data/cast.py` printed nothing.

**Where practice lives in stubs and designs.**

- Combat's `history`, `skills`, `tradition` and `equipped` (`modules/combat/combatant.py:93-97`).
- Threadwork's `history` (`operations.py:235-247`) and the knot's `history_relationships`
  (`knots.py:212-222`).
- The contest kernel's `faculty` (`resolver.py:184-195`).
- The 2026-08-15 practice table (AUG:170), whose columns read *"investigative practice | tradecraft
  practice | forensic practice | command practice | administrative practice"* beside combat's History.
- The lifepath Histories (HIST), whose skill *Domain* column uses Scene Battle, Mass Battle, Debate,
  Investigation, Faction Play, Scene Battle (Thread), Medicine and Craft.
- The settlement actions' *"Governance History"*, *"Wealth-relevant History"*, *"Military-relevant
  History"* and *"local History"* (settlement_layer_v30.md:560-563).
- The fieldwork design's one History per action (FW:73).

**The domains, one row each.** Verb numbers are the rows of the template's master verb table
(`2026-10-16-character-template_part2.md` §A.2, 1–65).

| P | domain | sources (tier) | verbs it serves |
|---|---|---|---|
| P01 | copying (repeated copying of a text) | `rosters.yaml:1106-1107` (T1); NPC-088.yaml:19-33 (T1, corpus) | #35 `tell` (read, T1); #32 `speak` (mapped, never reached) |
| P02 | standing and the matter: argument, oratory, forensic practice, the proceeding faculty | `resolver.py:184-195`, `:300-301` (T2); `sigma.py:82-129` for contested social rows (T1/T3); AUG:170 *"forensic practice"* (T4); `10_verbs_and_attributes.md:144` (T4); SCV:129-135, :155, :197-199, :246-267 (T4, superseded for dice); HIST Debate skills, e.g. :228, :310, :349 (T4) | #8, #35, #50, #54, #56 (sigma-routed, T3); #32 (open); #5, #26, #27, #28, #44 |
| P03 | arms: personal combat (`history`; the six `skills` sub-keys bind, parry, dodge, balance, technique, grab; `tradition`; `equipped` techniques; weapon specialization) | `combatant.py:93-97` (T2); AUG §1.3, :84-92, and §10.3, :465-480 (T4); HIST:266, :311 (T4) | #18, #20; #19 |
| P04 | command: leading a field side | `Officer.command` accepts a given value (`units.py:2700-2722`, T2); AUG:145, :170 *"command practice"* (T4); HIST:267, :369, :177 (T4); officers' practice gates troop types, *"named officer with Cavalry History"* (`military_layer_v30.md:132-133`, T4) | #22; #57, #65 |
| P05 | threadwork: the Leap and the seven operations; `thread_read` is a Leap (FW:351) | `operations.py:235-247` (T2); threadwork_v30:163, :195-229 (T4); HIST:279 (T4) | #58–#64; #40 |
| P06 | relationships (the knot-forming practice) | `knots.py:212-222` (T2); FW:470-490 (T4) | #42 |
| P07 | inquiry (investigative practice) | `proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:473-476` (T3, contestable); AUG:170 (T4); FW:296-317 (T4); HIST:253, :380 (T4) | #36–#39, #41; #34 |
| P08 | tradecraft: cover, concealment, deception, counter-intelligence | AUG:170 *"tradecraft practice"* (T4); FW:361, :575, :620 (T4); HIST:339 (T4); K-SC-6, the spoken lie (`research/by_lane/SC_social_contest.md:710`, T4) | #52; the concealer's obstacle on #36–#41 (open); #13 |
| P09 | administration and domain actions (governance; HIST's "Faction Play") | AUG:147, :170 *"administrative practice"* (T4); settlement_layer_v30.md:560-563 and governance_play_redesign_v1.md:61-68, :87 (T4); HIST:75, :94, :313-314 (T4) | #4, #9, #10, #17, #21, #31, #46, #47, #55, #65 (each eligible by an office) |
| P10 | trade: bargaining, valuing goods, networks | HIST:242, :312, :379 (T4); M-SE-2 (`research/by_lane/SE_settlements_territory_economy.md` §8, T4) | #12, #43 |
| P11 | craft: making and repairing things, scribal forgery included | HIST:241 *"+2D on any roll involving your specific craft"*, :350 (T4) | #15, #30, #45, #13 |
| P12 | medicine: healing bodies, stabilizing the wounded | HIST:362 *"+1D Medicine"*, :378 *"−1 Ob stabilise"* (T4); MB:328 *"Medicine Ob 2"* (T4) | #49 |
| P13 | scholarship and lore: doctrine, Einhir lore, records, precedent | HIST:129, :141, :294, :313, :341, :381 (T4); FW:95 (T4) | #38, #41; #6 |
| P14 | literacy (Full / Trade / Functional / Illiterate) | HIST:44-55, :215 (T4) | #6, #13, #38 (INFERRED applicability) |
| P15 | travel, navigation and survival | FW:90, :92, :239 (T4); HIST:92, :178, :314, :322, :340 (T4) | #24, #34, #23 |
| P16 | socializing (scene-scale rapport: Read, Converse, Connect, Impress, Rumour, Negotiate) | FW:97-101, :401-438 (T4); HIST:310 (T4) | none at season scale (the template's §A.1 excludes them as scene-scale) |
| P17 | labour and husbandry | HIST:314 Crown Farmer (T4); M-SE-5, *"labour as an input to production"* (SE lane §8, T4) | #45 |
| P18 | physical stealth and evasion | HIST:165 *"+1D on Agility concealment"*, :382 *"Escape −1 Ob"*, :370 (T4) | none named at season scale |
| P19 | economic stewardship (*"Wealth-relevant History"*) | settlement_layer_v30.md:560; governance_play_redesign_v1.md:61 (T4) | #15 |

**19 domains: one at T1, five at T2, one at T3 (P07, contestable), twelve at T4.**

**Dropped, because no source names a practice:**

- *Politician* and *leader*. AUG:146 and :148 list them as **position** roles, carried by *"Standing
  ladder + Mandate/votes"* and *"Standing 7 / faction emergence"*, not by a practice.
- *Logistics* as a domain of its own. It appears only inside HIST:75's Heartland Roots, so it is
  folded into P09.
- *Horsemanship*, *seamanship* and *hunting* as domains of their own. Seamanship appears only as
  terrain bonuses (HIST:340 and the Fjord Sailor's defence on water), folded into P15 and P03.
- *Circles*: the network dice of the NPC designs (`npc_behavior_system_v1.md:176`, :197). It is a
  person-held quantity, who one knows, not a practice.

**The sigma-routed verbs' keys** (`determine`, `argue`, `arrest`, `interrogate`) are folded into P02:
*"the key is content"* (`2026-10-16-character-template_part2.md:169-170`), and no source names one.

---

## 3. STAGE 2a: WHAT EACH PRACTICE DOMAIN REQUIRES

**Fixed form.** For each domain:

- (a) what doing it well requires **physically**;
- (b) **cognitively**;
- (c) **perceptually**;
- (d) **socially or volitionally**;
- (e) what the sources name against what is inferred, as a count (named / overridden / inferred).

Each cell gives the aptitude, its role and its basis.

**Notes that bind the table.**

1. **The 2026-09-05 ruling.** Jordan's words are *"ignore their use of attributes"*
   (`04_VERBS.md:465-466`). The proceedings design author glosses them for the five inquiry acts:
   *"`capability` supplies the dice"* (`:473-476`, T3, contestable; template head §3.1.1). So the
   fieldwork *"Primary Attribute"* column is overridden as a source of DICE for `examine`,
   `interview`, `research`, `surveil` and `reconstruct`. It is kept here as what the design's author
   held the act to require, and tagged *overridden*. It does not reach `thread_read`.
2. **V-2 and V-3** (`10_verbs_and_attributes.md:198-199`) limit what CODE may read. They do not limit
   what an act requires, so they are applied in the recommendation (`_part3` §7), not here.
3. **J-13** (*"a social figure is derived, not stored"*, `workplans/valoria_master_workplan_v9_part5.md:433`)
   is about the subsystem's score, not the person's aptitude. Nothing here proposes storing a score.

| P | domain (best tier) | verbs it serves | (a) physical | (b) cognitive | (c) perceptual | (d) social / volitional | (e) named / overridden / inferred |
|---|---|---|---|---|---|---|---|
| P01 | copying (T1) | #35, #32 | `precision` (effect size, INFERRED: a copy is only as good as its fidelity); `dexterity` (effect size, INFERRED: hand-copying is hand work) | `concentration` (effect size, INFERRED: repeated copying is long, sustained work) | — | — | 0 / 0 / 3 |
| P02 | standing and the matter (argument, oratory, forensic practice) (T2) | #8, #35, #50, #54, #56, #32 | — | `reasoning` (odds, NAMED T4, overridden for dice: SCV:132 expert judge, Cognition: "evaluates logical structure"); `memory` (odds, NAMED T4, overridden for dice: SCV:155 Appraise rolls Attunement + Recall); `concentration` (difficulty/cost, NAMED T4, overridden for dice: SCV:246, :267 Concentration = 3·Focus + 2·Spirit); `verbal-fluency` (odds, INFERRED: argument is made of words); `quick-thinking` (odds, INFERRED: the rebut move kind (resolver.py:34) answers in the moment) | `reading-people` (odds, NAMED T4, overridden for dice: SCV:135 no adjudicator, Attunement; :147 Appraise) | `presence` (odds, NAMED T4, overridden for dice: SCV:134 crowd, Charisma: "delivery and authority"); `empathy` (odds, NAMED T4, overridden for dice: SCV:147 Appraise is "empathetic perception"); `composure` (difficulty/cost, NAMED T4, overridden for dice: SCV:199 Focus defence absorbs strain) | 0 / 7 / 2 |
| P03 | arms (personal combat: history, skills, tradition, techniques) (T2) | #18, #20, #19 | `strength` (effect size, NAMED T2: Impact, balance, health (AUG:86, :88; combatant.py:39-40)); `quickness` (odds, NAMED T2: tempo (combat_systems.py:113)); `reflexes` (odds, NAMED T2: reflex (combat_systems.py:172); initiative (:1419-1421)); `balance` (odds, NAMED T2: balance (combat_systems.py:188)); `stamina` (difficulty/cost, NAMED T2: `stamina_max` (combatant.py:43-44)); `toughness` (difficulty/cost, NAMED T2: `wound_interval`, `health_full` (combatant.py:30-40)) | — | `anticipation` (odds, NAMED T2: reading (combat_systems.py:171)) | `composure` (difficulty/cost, NAMED T2: poise recovery, disruption resistance (combat_systems.py:1436, :1452)); `boldness` (odds, NAMED T2: `disp` aggression lean (combat_systems.py:183)) | 9 / 0 / 0 |
| P04 | command (leading a field side) (T2) | #22, #65, #57 | — | `spatial-sense` (odds, NAMED T4: HIST:177 "identify terrain advantage"); `planning` (odds, INFERRED: tactic execution is a Command roll per tactic (MB:312); the Cognition term is unglossed); `judgment` (odds, INFERRED: recall of a pursuit and commit decisions are made under uncertainty) | `anticipation` (odds, NAMED T2: feint recognition `roll_pool(command)` (orchestration.py:2598)); `situational-awareness` (eligibility, NAMED T2: Command is "the span-of-control governor" (engine.py:93)); `observation` (odds, NAMED T4: HIST:177 Border Vigilance, Cognition to detect ambush, assess enemy strength; HIST:369 Eagle Eyes) | `leadership` (eligibility, NAMED T2: Command from Charisma 2 : 1 (exchange.py:57-66) → reform gate, morale-erosion divisor); `composure` (difficulty/cost, INFERRED: a general under attack keeps command or loses it (MB:327-343)) | 5 / 0 / 3 |
| P05 | threadwork (the Leap, the seven operations, thread_read) (T2) | #58, #59, #60, #61, #62, #63, #64, #40 | `recovery` (difficulty/cost, NAMED T4: meditation reduces fatigue by Spirit (threadwork_v30:203)) | `concentration` (eligibility, NAMED T4: Focus sets max operations per contact (threadwork_v30:199)) | `thread-sensitivity` (odds, NAMED T2: `ts // 10` (operations.py:235-247)) | `will` (odds, NAMED T2: `spirit × 2` (operations.py:235-247); threadwork_v30:163); `self-coherence` (difficulty/cost, NAMED T2: `resilience` resists the Coherence cost (operations.py:249-274), dark at gain 0); `contact-endurance` (eligibility, NAMED T4: Thread Fatigue threshold = Spirit × 5 (threadwork_v30:195)); `discipline` (eligibility, NAMED T4: HIST:293 Contemplative Focus, "years of discipline … hold rendering at bay") | 7 / 0 / 0 |
| P06 | relationships (knot-forming practice) (T2) | #42 | — | — | `thread-sensitivity` (eligibility, NAMED T2: either party `ts ≥ 30` (knots.py:195-198)) | `relational-depth` (eligibility, NAMED T2: `bonds ≥ 5` gate and cap (knots.py:185-203); FW:477-479); `sincerity` (odds, NAMED T4: Sincerity Check before an instrumental approach (FW:430)); `empathy` (odds, INFERRED: reaching Disposition +5 takes rapport (FW:410 Connect)); `will` (odds, NAMED T2: formation roll `spirit × 2` (knots.py:212-222); FW:483) | 4 / 0 / 1 |
| P07 | inquiry (investigative practice) (T3) | #36, #37, #38, #39, #41, #34 | — | `reasoning` (eligibility, NAMED T4, overridden for dice: FW:84, :446 Cognition ≥ 2 / ≥ 3 depth gates: "minimum cognitive capacity"); `memory` (odds, NAMED T4, overridden for dice: FW:95, :303 Research, Recall: "archives, oral histories … precedent"); `inference` (odds, NAMED T4, overridden for dice: FW:306 Reconstruct: "assemble existing evidence into a coherent picture"); `concentration` (odds, INFERRED: Surveil is observation "over extended time" (FW:304)) | `observation` (odds, NAMED T4, overridden for dice: FW:93, :301 Examine, Cognition: "examining objects … forensics"); `reading-people` (odds, NAMED T4, overridden for dice: FW:94, :302 Interview, Attunement: "reading people, sensing deception"); `thread-sensitivity` (eligibility, NAMED T4: depth gates TS ≥ 10 / ≥ 30 (FW:446-447, :301)) | `patience` (odds, INFERRED: three failures make a Desperate Trail (FW:337-345); persistence pays) | 1 / 5 / 2 |
| P08 | tradecraft (cover, concealment, deception, counter-intelligence) (T4) | #52, #36, #37, #38, #39, #40, #41, #13 | — | `reasoning` (resists another, NAMED T4: Cover = Cognition + History (FW:575); concealment pool Cognition × 2 (FW:361)) | `observation` (odds, INFERRED: HIST:339 Shadow Work (+1D surveillance / counter-intel) is practice) | `presence` (eligibility, NAMED T4: a cover identity needs a Charisma roll (FW:620)); `deception` (odds, INFERRED: HIST:339 Smooth Liar is a practice skill; the aptitude under it is unnamed); `composure` (difficulty/cost, INFERRED: exposure thresholds punish a slip (FW:588-597)) | 2 / 0 / 3 |
| P09 | administration and domain actions (governance; "Faction Play") (T4) | #4, #9, #10, #17, #21, #31, #46, #47, #55 | — | `reasoning` (odds, NAMED T4: Develop and Survey roll Cognition + History (settlement_layer_v30:560; governance_play_redesign_v1:87)); `judgment` (odds, NAMED T4: Hold Court adjudicates a dispute on Charisma/Cognition (governance_play_redesign_v1:64)); `numeracy` (odds, INFERRED: the Governor role is "AP × compliance + Ledger" (AUG:147)); `planning` (odds, INFERRED: administration sequences works over seasons) | `reading-people` (odds, NAMED T4: Administer rolls Attunement + Governance History (settlement_layer_v30:563)) | `presence` (odds, NAMED T4: Pacify rolls Charisma + local History (settlement_layer_v30:562); Keep Order by Consent, Charisma (governance_play_redesign_v1:63)); `patience` (odds, INFERRED: administration is slow work; no source states it) | 4 / 0 / 3 |
| P10 | trade (bargaining, valuing goods, networks) (T4) | #12, #43 | — | `numeracy` (odds, INFERRED: valuation and price); `memory` (odds, INFERRED: prices, routes, partners (HIST:379 Wide Network is practice)) | `reading-people` (odds, NAMED T4: Negotiate rolls Attunement (FW:413; a scene-scale analogue)) | `persuasiveness` (odds, INFERRED: closing a bargain); `composure` (difficulty/cost, INFERRED: HIST:312 Haggler's Nerve (−1 strain in negotiation) is practice; nerve is what bargaining taxes) | 1 / 0 / 4 |
| P11 | craft (making and repairing things; scribal forgery) (T4) | #15, #30, #45, #13 | `dexterity` (effect size, INFERRED: HIST:241 Craft Expertise names the practice only); `precision` (effect size, INFERRED: quality of the made thing); `strength` (effect size, INFERRED: smithing, building, masonry) | `spatial-sense` (effect size, INFERRED: building to plan) | — | `patience` (effect size, INFERRED: long work) | 0 / 0 / 5 |
| P12 | medicine (healing bodies, stabilising the wounded) (T4) | #49 | `dexterity` (odds, INFERRED: HIST:378 Field Medicine (−1 Ob stabilise) and MB:328 (Medicine Ob 2) name the practice only) | `memory` (odds, INFERRED: remedies) | `observation` (odds, INFERRED: diagnosis) | `composure` (odds, INFERRED: working on the wounded under fire (MB:328, Phase 5)) | 0 / 0 / 4 |
| P13 | scholarship and lore (doctrine, Einhir lore, records, precedent) (T4) | #38, #41, #6 | — | `memory` (odds, NAMED T4: FW:95 lore research, Recall; HIST:294 Archive Access "+1D on Recall-based rolls"; HIST:381 Treaty Language "+1D Recall"; HIST:129 "knowledge as recognition, not intellect"); `reasoning` (odds, INFERRED: interpreting doctrine and precedent) | — | `patience` (odds, INFERRED: archive work) | 1 / 0 / 2 |
| P14 | literacy (Full / Trade / Functional / Illiterate) (T4) | #6, #13, #38 | — | `learning` (eligibility, INFERRED: literacy is acquired (HIST:44-55); "available as spark" for the self-taught) | — | — | 0 / 0 / 1 |
| P15 | travel, navigation and survival (T4) | #24, #34, #23 | `stamina` (odds, NAMED T4: FW:92 Endurance-based exploration: "forced marches, exposure, harsh terrain"); `hardiness` (difficulty/cost, NAMED T4: FW:239 Endurance check per Calamity territory; HIST:92 Highland Toughness, :178 Cold Endurance) | `spatial-sense` (odds, NAMED T4: FW:90 Cognition: "pathfinding, cartography") | `land-sense` (odds, NAMED T4: HIST:314 Seasons Reader, "+1D Cognition for weather/terrain/agriculture"); `observation` (odds, INFERRED: spotting a route, a danger) | — | 4 / 0 / 1 |
| P16 | socializing (scene-scale rapport: Read, Converse, Connect, Impress, Rumour, Negotiate) (T4) | none at season scale | — | — | `reading-people` (odds, NAMED T4: Read and Negotiate roll Attunement (FW:97, :101, :408, :413)) | `presence` (odds, NAMED T4: Impress and Rumour roll Charisma (FW:98, :100, :411-412)); `persuasiveness` (odds, NAMED T4: Converse rolls Charisma: "shift Disposition" (FW:409)); `relational-depth` (odds, NAMED T4: Connect rolls Bonds: "building genuine trust" (FW:99, :410)); `sincerity` (odds, NAMED T4: Sincerity Check, Spirit (FW:430)); `empathy` (odds, INFERRED: rapport) | 5 / 0 / 1 |
| P17 | labour and husbandry (T4) | #45 | `stamina` (effect size, INFERRED: field and site work); `strength` (effect size, INFERRED: field and site work) | — | `land-sense` (effect size, NAMED T4: HIST:314 Seasons Reader (weather, agriculture)) | `patience` (effect size, INFERRED: seasonal work) | 1 / 0 / 3 |
| P18 | physical stealth and evasion (T4) | none at season scale | `balance` (odds, NAMED T4: HIST:165 Invisible, "+1D on Agility concealment" in crowds); `quickness` (odds, NAMED T4: HIST:382 Slippery, Escape −1 Ob, pursuit evasion) | — | — | `composure` (odds, INFERRED: holding still under a searcher's eye) | 2 / 0 / 1 |
| P19 | economic stewardship ("Wealth History") (T4) | #15 | — | `reasoning` (odds, NAMED T4: Develop rolls Cognition + Wealth-relevant History (settlement_layer_v30:560; governance_play_redesign_v1:61)); `numeracy` (odds, INFERRED: accounts); `planning` (odds, INFERRED: investment over seasons) | — | — | 1 / 0 / 2 |

**What the domain interrogation shows.**

- **Only P03 (arms), P04 (command), P05 (threadwork) and P06 (knots) have aptitudes named in code**
  (T2). Every other domain's aptitudes are named in designs (T4), overridden, or inferred.
- **P11 craft, P12 medicine, P14 literacy and P17 labour name only the practice.** Every aptitude under
  them is this proposal's.
- **The most-drawn aptitude across domains is `composure`**, in 7 of 19 domains. **`reasoning`** is in
  6. `reading-people`, `memory`, `observation` and `patience` are in 5 each (`patience` all inferred).
- **AUG:152-155 says the roles "are not distinguished by aptitude — they are distinguished by
  practice, instruments, and office".** The domain rows partly bear that out, and partly do not:
  - **Bearing it out:** reasoning, reading people and composure recur across most domains, so they
    do not tell domains apart.
  - **Against it:** a minority of aptitudes is confined to one or two domains:
    - quickness, reflexes and balance: arms and stealth;
    - will and self-coherence: threadwork and knots;
    - thread sensitivity: threadwork, knots and inquiry;
    - relational depth: knots and socializing;
    - land sense: travel and husbandry.

    Those do mark a domain. **Judgment call:** AUG's sentence holds for the six roles it tabulates
    (AUG:168-177). It does not hold for the domains it leaves out (threadwork, knots, travel, stealth).
