# The character template — part 2: §3A, the idealized master verb table and the verb × personal-input matrix

## Status: PROPOSED (2026-10-16). Corrected twice the same day against two independent critics' reports (both reconciliation tables at the end of `_part3`). Not ratified; merge ratifies nothing unless Jordan so rules.
## Parts, in reading order: [head](2026-10-16-character-template.md) (§0–§3) · **this file** (§3A) · [`_part3`](2026-10-16-character-template_part3.md) (§4–§10).

**What this part is for.** Jordan: *"cross reference against a master verb table that is idealized as
if fully designed and built."* The question it answers is which **personal inputs** the verbs, taken
together, would read if every system were complete. The head's §3 folds the result into Options A
and B. This part holds the evidence.

**Words.** A **personal input** is a quantity a resolver reads off a person to set the odds, the
cost, a gate or the size of an effect: one of the registry's nine attributes, practice, Thread
Sensitivity, temperament, resilience, Recall, or kit. **One rule:** BODY (live state the season
writes), OFF (an office, held by a Tenure) and person-held quantities (a claim in his own ledger, a
Record he holds, his `weight`, a stance row, his values) are named where a row reads them and are
never counted. (The first draft said "axis", the engine's word for *"THE ONLY AXIS ROSTER IN THE
ENGINE"*, `engine/substrate/descriptors.py:110`, `:124`; the second said "capacity kind", which
collides with the 2026-08-15 census's *"Capacities"* tier and with `world_q.capacity`, a settlement's
room. Head, "Words".)

**Discipline.** No verb is invented. Every row names a source. Tags are the head's: **[CHECKED]**
opened in the third pass; **[CHECKED-2]** opened in the second pass only; **[CHECKED-draft]** in the
drafting pass only; **[RAN]** run, with the artifact named in `_part3` §10. The tier tags are the
head's (T1 loop code, T2 stub code, T3 ratified spec, v9 position or ratified-as-intent design, T4
design intent, including the quarantined designs, cited by bare filename as the tree's own rows cite
them). **Where two sources disagree the higher tier wins; the loser is recorded in the row and not
counted.** In the "reads" columns, *today* is T1 only, and *when complete* is what a named T2–T4
source says the verb would read. Where no source names a personal input, the cell says **none
named**: a claim about the sources, not about the game. **open** means a source names a quantity
that a personal input would plausibly set, and no source says which.

**The codes.** The registry's nine (`references/descriptor_registry.yaml:36-48`) [CHECKED-2], each
with the alias the stub code spells:

- **STR** Strength. **AGI** Agility. **END** Endurance.
- **FOC** Focus. **ACU** Acuity (code and the fieldwork design: Cognition; the alias is
  *"[ASSUMPTION] … Jordan veto"*, `:42`). **WIL** Will (code and designs: Spirit).
- **ATT** Attunement (code: `att`). **CHA** Charisma. **BON** Bonds.

Plus six codes that are not on the registry:

- **PRA** practice, or "History", per domain: what training writes, and what `capability` holds.
- **TS** Thread Sensitivity (`descriptor_registry.yaml:61-65`, `practitioner_stats`; its derived
  Thread Pool Score is `floor(TS / 10)`) [CHECKED-2]. Not an attribute.
- **TMP** temperament (combat `disp`).
- **RES** resilience: threadwork's R-14 input, a per-actor integer that resists the Coherence cost,
  dark at the shipped gain 0 (`systems/threadwork/sim/operations.py:157`, `:249-274`) [CHECKED].
- **REC** Recall: no reader above T4 (head §3.1.1). The fieldwork design made it primary for two
  inquiries (`.designs/systems/fieldwork/reference/fieldwork_v30.md:303`, `:306`) [CHECKED], an
  attribute use the 2026-09-05 ruling overrides; the 2026-08-15 census classes it *"CAPACITY, not
  attribute — equip slots + learning rate; never rolled"*
  (`proposals/2026-08-15-character-and-faction-stats-and-progression.md:475`) [CHECKED].
- **KIT** what a person carries.

---

## A.1 The inclusion rule, and the count

**A row is a VERB when a source names it as an act a person (or the seat he exercises) chooses at
the season's scale, as an act of its own.** Six kinds of thing are therefore NOT rows, and the rule
is applied to every candidate:

| excluded as | members | why, and where its reads go |
|---|---|---|
| **a value of another verb's parameter** | `yield` | it is a value of `challenge_terms: [yield, blood, death]` and a stop rule inside `fight` (`workplans/valoria_master_workplan_v9_part7.md:58`) [CHECKED] |
| **a form or arm of another verb** | the charge; the spoken lie; resigning one's own seat; `form_knot` | the charge: *"no row is added (the charge is an `utter`)"* (`_part5.md:77`) [CHECKED]. The lie: *"an arm of `said_of`"*, the site where a teller chooses what to pass on (K-SC-6, `research/by_lane/SC_social_contest.md:710`) [CHECKED-2], so a form of `tell`. Resigning: *"Resignation composes on `release`"* (K-FA-3, `research/by_lane/FA_faction_actions.md:582`) [CHECKED-2]. `form_knot` (`systems/fieldwork/sim/knots.py:173`) [CHECKED-2] is the stub resolver of the shipped `tie / knot` row's `knot` half, so its reads are that row's |
| **a choice or check inside one verb's resolution** | the combat bout's terms; `engage`, `withdraw`; the seven contest move kinds; rally, reform, recall, the feint check and the span check | the bout's terms and IN-46's `{engage, withdraw}` (an [ASSUMPTION] in the plan, `_part4.md:34`) [CHECKED-2] are inside one `fight`. The move kinds `advance, hard, shift, support, pass, evidence, rebut` (`systems/social_contest/sim/contest/resolver.py:34`) [CHECKED-2] are inside one contest, so their reads fold into `tell` (the one contested social verb today). Rally, reform, recall, the feint check and the span check are phase checks inside one field, so their reads fold into `march` (§A.4) |
| **a private helper** | `_charge_shock_sigma`, `_brace_setup_ok` | `modules/mass_battle/resolution.py:176`, `:132` [CHECKED-2]: leading-underscore functions, not orders |
| **superseded** | `practice` | *"K-4 (… a `practice` verb as `capability`'s writer) is SUPERSEDED by IN-12 step 9's `train`"* (`workplans/valoria_master_workplan_v9_part7.md:51`) [CHECKED], and *"K-4 (a `practice` verb) superseded by IN-12 step 9's `train`"* (`workplans/valoria_master_workplan_v9_part8.md:207`) [CHECKED]. Both lines say it; the first critic's `_part7.md:51` was right |
| **scene-scale only** (no source names it at the season's scale) | the fieldwork design's exploration sub-types (terrain, Thread-aware, endurance-based); its six non-contest social actions, Read, Converse, Connect, Impress, Rumour, Negotiate, and Gift/Bribe; the Sincerity Gate; the concealment roll; the cover identity's setup roll | each is a roll inside one TTRPG scene: *"A social action represents one meaningful interaction within a scene"* (`fieldwork_v30.md:403`), made a dialogue choice in the Godot mode (`:765`) [CHECKED]. No season-scale source names any of them (a grep of `verb_table.yaml`, v9 `_part5` and the verb-coverage proposal's §9 headings for the six names found no verb) [RAN]. **Their reads are recorded, not counted**: Cognition, Attunement, Endurance for exploration (`:90-92`); Attunement for Read and Negotiate (`:408`, `:413`); **Charisma** for Converse, Impress and Rumour (`:409`, `:411`, `:412`); **Bonds rolled** for Connect (`:410`); Spirit for the Sincerity Gate (`:430`); Cognition × 2 + History for concealment (`:361`, `:617`); **Charisma** for the cover identity's setup (`:620`), the scene-scale counterpart of planned `conceal` (row 52) [CHECKED] |

The thread operations' lane recommendation (K-WR-2, `research/by_lane/WR_world.md:538`)
[CHECKED-draft] is carried as the lane reference on the 7 STUBBED thread rows, not as rows of its own.

| status class | rows | how counted |
|---|---|---|
| **SHIPPED, resolvable** | **37** | `resolvable_verbs()` printed `resolvable_verbs 37` and the 37 names [RAN, `_part3` §10 probe 6, artifact `tmpl/aperture4.out`] |
| **SHIPPED, not resolvable** | **8** | the 45 rows of `grep -n '^  - verb:' engine/season/verb_table.yaml` minus `resolvable_verbs()` [RAN]: `carry`, `evade / defy`, `exchange`, `forge`, `construe`, `succeed`, `thread_read`, `tie / knot` |
| **PLANNED in v9** | **12** | IN-12 steps 6, 7, 9, 10, 13, 5, 11 (`_part5.md:71-78`) [CHECKED]: `seize`, `covenant`, `sabotage`, `tend`, `argue`, `train`, `conceal`, `forgive`, `arrest`, `pardon`, `interrogate`, `raze` |
| **STUBBED** (code outside the season loop) | **7** | the thread operations, `systems/threadwork/sim/operations.py:351, :375, :388, :397, :417, :434, :512` [CHECKED-2] |
| **DESIGN-ONLY** | **1** | the troop design's one new verb, raising a levy from a settlement's pool (its §3.1, "`conscript`: raise a levy from a settlement's pool"; `conscript` is a working name, and the name is that design's J-3) [CHECKED, by heading] |
| **total** | **65** | |

**SHIPPED is a row count, not an execution count** (`CLAUDE.md` §0.2). Of the 45 rows, 8 cannot be
attempted at all. Of the 37 that can, the plan records 17 verbs executing in `corpus_run` after
IN-57 (*"executed verbs went 21 → 17"*, `_part5.md:471`) [CHECKED-2: the line; the run not
repeated]. This pass re-ran the populated realm (§10 probe 6): four seasons at seed 0, the measured
arm's `World.content_hash()` equal to the untouched control's, 2432 acts in each arm. **25 verbs
executed at least once and 35 were attempted.** No unresolvable row was attempted or executed.
Per-verb counts are §A.2.1's last column.

---

## A.2 The table

### A.2.1 SHIPPED (45: 37 resolvable, 8 not)

Row line numbers [CHECKED-2]. `R?` is membership of `resolvable_verbs()`, and *Ex. (realm)* the
number of executions in four populated-realm seasons at seed 0; both [RAN] in this pass (§10 probe
6). Every row also reads BODY indirectly, through the scene budget
(`engine/season/decision/budget.py:57-61`) [CHECKED-draft]; that is one shared cost, never counted.

| # | verb (`verb_table.yaml` line) | lane | R? | reads today (T1): personal inputs; *person-held quantities* | reads when complete (source, tier) | outcome a personal input would move | lane ref | Ex. (realm) |
|---|---|---|---|---|---|---|---|---|
| 1 | `carry` :105 | SC | no | none | none named | — | none | 0 |
| 2 | `commit` :123 | FA | yes | none | none named | — | none | 1 |
| 3 | `comply` :139 | IN | yes | none; *the actor's own ledger* (`own_ledger` of subject, `:148-154`) [CHECKED-2] | none named | — | none | 0 |
| 4 | `confer` :163 | FA | yes | none; OFF (the seat exercised, via `Act.via`) | none named | OPTIONS (office) | none | 1 |
| 5 | `convene` :183 | SC | yes | none | none named | — | none | 0 |
| 6 | `create_record` :194 | FI | yes | none | none named | — | none | 187 |
| 7 | `destroy_record` :205 | FI | yes | none | none named | — | none | 0 |
| 8 | `determine` :217 | SC | yes | none; OFF | PRA, **if** it draws on its domain: the sibling proposal lists *"tell; speak and determine, proposed"* in one domain, whose aptitude enters through *"the capability key `copying`; the retiring kernel's abstract `faculty`"*, with attributes *"none bound"* (`proposals/2026-09-30-character-and-play-surface/10_verbs_and_attributes.md:144`) [CHECKED] (T4). Treated exactly as `speak` (row 32): no `verb_capability` mapping and no `contests:` today | ODDS | none | 3 |
| 9 | `dispatch` :263 | IN | yes | none; OFF | none named | OPTIONS | none | 13 |
| 10 | `establish` :278 | FA | yes | none; OFF | none named | OPTIONS | none | 0 |
| 11 | `evade / defy` :292 | IN | no | none | none named | — | none | 0 |
| 12 | `exchange` :307 | SE | no | none | none named | — | K-SE-4 | 0 |
| 13 | `forge` :325 | FI | no | none | **open**: the row writes `Record.forgery_quality`, and no source says what sets its value | EFFECT, if a source rules one | M-FI-2 | 0 |
| 14 | `found` :354 | SE | yes | none | none named | — | none | 0 |
| 15 | `build` :377 | SE | yes | none | none named | — | none | 0 |
| 16 | `give` :400 | IN | yes | none; *a Record the actor holds* (`relation: held_by`, `:406-417`) [CHECKED-2] | none named | — | none | 1 |
| 17 | `issue` :428 | FA | yes | none; OFF | none named | OPTIONS | K-FA-12 | 5 |
| 18 | `fight` :475 | PC | yes | none; BODY → `end` (`seam/wrappers/combat.py:129-138`) [CHECKED-2] | STR AGI END ACU FOC WIL ATT PRA TMP KIT: every `Combatant` field (`modules/combat/combatant.py:93-94`) [CHECKED-2] (T2). `contests: "the body"` (`:485`) [CHECKED] | ODDS · EFFECT · COST (wounds) | M-PC-1, K-PC-1 | 16 |
| 19 | `challenge` :579 | PC | yes | none | none named | — | none | 14 |
| 20 | `accept` :600 | PC | yes | as `fight` | as `fight` (T2). `contests: "the body"` (`:610`) [CHECKED] | as `fight` | M-PC-1 | 28 |
| 21 | `requisition` :629 | SE | yes | none; OFF | none named | OPTIONS | K-SE-5 | 0 |
| 22 | `march` :664 | MB | yes | none: the side's members' `weight`, stance and loyalty, no commander (`seam/wrappers/mass_battle.py:175-200`) [CHECKED-draft] | CHA, ACU, through `derive_command` (`modules/mass_battle/core/exchange.py:57-66`) [CHECKED]; `hierarchy/units.py:2700-2722`, live while `COMMAND_SIGMA_ENABLED`, default on, `config.py:530` [CHECKED-2] (T2). **Not through the exchange pool:** under `POOL_QUALITY_MODEL`, default on (`config.py:556`), the pool is `eff_power × eff_size` and *"Command is absent from this branch entirely"* (`exchange.py:103-126`) [CHECKED-2]. `contests: "a field"` (`:676`) [CHECKED]. §A.4 lists where Command still reaches | GATE (reform, span of control) · ODDS (recall, feint) · COST (morale erosion) | M-MB-3, K-MB-2, M-NPC-13 | 18 |
| 23 | `migrate` :698 | SE | yes | none; *the migrant's own `weight`* against the destination's room, `world_q.capacity` (`loop/effects_migration.py:195`) [CHECKED-2] | none named | — | none | 0 |
| 24 | `move` :720 | IN | yes | none | none named | — | none | 55 |
| 25 | `oblige` :735 | FA | yes | none | none named | — | none | 16 |
| 26 | `open_case` :757 | SC | yes | none | none named | — | none | 8 |
| 27 | `petition` :782 | SC | yes | none | none named | — | K-SC-3 | 28 |
| 28 | `construe` :806 | SC | no | none | none named | — | none | 0 |
| 29 | `release` :822 | FA | yes | none | none named | — | none | 12 |
| 30 | `restore` :839 | SE | yes | none | **open**: the effect names an unbuilt `× f(degree)` term, the identity today because the act is uncontested (`loop/effects_economy.py:113-121`; H-164) [CHECKED-2]; no source says what would grade it | EFFECT | K-WR-3 | 0 |
| 31 | `revoke` :861 | FA | yes | none; OFF | none named | OPTIONS | none | 0 |
| 32 | `speak` :875 | SC | yes | **none**: the row has no `contests:` field (`:875-885`) [CHECKED-2], and the only path from `verb_capability` into the loop is `sigma.contest_input` (`seam/wrappers/sigma.py:132-147`) [CHECKED], reached by contested verbs only. The roster's `speak: "copying"` (`rosters.yaml:1107`) [CHECKED] is a mapping nothing reaches | PRA, **if** `speak` becomes contested: the proceedings design says *"`speak` becomes the contest"* (`10_verbs_and_attributes.md:123`) [CHECKED] (T4), and the existing mapping would then read `copying`. The same row of the sibling's table binds no attribute: *"none bound"* (`:144`) [CHECKED] | ODDS | K-SC-2; M-SC rows [ids not enumerated] | 70 |
| 33 | `succeed` :886 | FA | no | none | none named | — | none | 0 |
| 34 | `survey` :917 | FI | yes | none; *the actor's own ledger* (`own_ledger` of subject, `:923-925`) [CHECKED-2] | none named | — | none | 10 |
| 35 | `tell` :936 | SC | yes | PRA, as an opposed pair: the teller's `copying` → pool; the HEARER's same key ÷ 2 → Ob. The opponent is the row's `counterparty: to`, *"THE HEARER IS THE SECOND SIDE, AND THE TOPIC IS NOT"* (`:950-951`; `loop/resolve.py:740-744`; `sigma.py:97-129`) [CHECKED]; *the teller's own ledger* (its `holds` conjunct is `own_ledger`, `:943-945`) [CHECKED]. `contests: "a standing"` (`:953`) [CHECKED] | PRA. The contest kernel's `faculty` → `Pool.size` and `Leverage.net` (`resolver.py:300-301`) [CHECKED-2] (T2), a kernel the sibling proposal calls *"retiring"*, with attributes *"none bound"* (`10_verbs_and_attributes.md:144`) [CHECKED]. The seven move kinds fold in here; the `evidence` move reads the contestant's evidence items (`resolver.py:184-190`) [CHECKED], a person-held quantity, not an input. **CHA moves no outcome**: §A.4. Recorded, not counted: the quarantined v30 contest design's Appraise *"Attunement + Recall"* and Concentration *"(3 × Focus) + (2 × Spirit)"* (`social_contest_v30.md:155`, `:267`) [CHECKED, by grep], superseded by the kernel | ODDS | K-SC-2, M-NPC-1 | 36 |
| 36 | `examine` :1083 | FI | yes | none | PRA: the 2026-09-05 ruling, *"`capability` supplies the dice"* (`proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:465-476`) [CHECKED] (T3; head §3.1.1). TS as a gate on the Buried depth, *"Buried (3) if TS ≥ 10"* (`fieldwork_v30.md:301`) [CHECKED] (T4; TS is not an attribute). Overridden: Cognition as *"Primary Attribute"* (same line) | ODDS · GATE (depth) · MEMORY | M-FI-3, K-FI-1 | 0 |
| 37 | `interview` :1105 | FI | yes | none | PRA (T3, as row 36). Overridden: Attunement (`fieldwork_v30.md:302`) [CHECKED]. Its Buried route is a Disposition of +3, a stance, not an input (same line). ⚠ That row is kept only as *"the current mechanical baseline"*: ED-FI-0004 folds Interview into the Dialogue Lattice (`:308`) [CHECKED] | ODDS · MEMORY | K-FI-1 | 20 |
| 38 | `research` :1121 | FI | yes | none | PRA (T3, as row 36). Overridden: Recall (`fieldwork_v30.md:303`) [CHECKED]. Its Buried route is *"institutional access"*, a holding, not an input (same line) | ODDS · MEMORY | K-FI-1 | 25 |
| 39 | `surveil` :1137 | FI | yes | none | PRA (T3, as row 36). Overridden: Cognition (`fieldwork_v30.md:304`) [CHECKED]. Reaches *"Up to Hidden (2)"* only, so no TS gate | ODDS · MEMORY | K-FI-1 | 56 |
| 40 | `thread_read` :1157 | FI/WR | no | none: untyped, and so not resolvable (the row says so itself, `:1163`) [CHECKED-2] | PRA (T3, as row 36: Thread-Read is the sixth act the ruling covers, `04_VERBS.md:460`) [CHECKED]; TS as a gate, *"TS ≥ 30 required"* (`fieldwork_v30.md:305`) [CHECKED], typed by K-3 (`09_the_character_sheet.md:130`) [CHECKED-2], **T3**: K-3 is RATIFIED AS INTENT (`_part8.md:207`) [CHECKED]. Overridden: the pool *"(Spirit × 2) + History + TPS"* (`fieldwork_v30.md:305`, `:351`) [CHECKED] (T4), whose Spirit and Thread Pool are both in the struck vocabulary (`04_VERBS.md:466`) | ODDS · GATE | none (K-3 is a plan position, not a lane ref) | 0 |
| 41 | `reconstruct` :1171 | FI | yes | none; *the actor's own ledger* (`own_ledger` of subject, `:1176-1178`) [CHECKED-2] | PRA (T3, as row 36). Overridden: Recall (`fieldwork_v30.md:306`) [CHECKED] | MEMORY | K-FI-1 | 111 |
| 42 | `tie / knot` :1186 | IN | no | none (H-182: the row has no effect) | for `knot`, from `form_knot`: BON as a gate (`bonds ≥ 5`, `knots.py:185-187`) and as a cap (`bonds // 2 + 1` knots, `:200-203`); TS as a party gate (either party `ts ≥ 30`, `:195-198`, `KNOT_TS_MIN_PARTY` `:54`); WIL and PRA as the formation roll, `spirit × 2 + history_relationships`, TN 7 (`:212-222`) [CHECKED-2] (T2). The disposition gate (`:189-193`) reads a stance, not an input. The fieldwork design states the same prerequisites (`fieldwork_v30.md:472-477`) and rolls *"Spirit × 2"* at Ob 2 (`:483`) [CHECKED] (T4). For `tie`: none named. The row declares no `contests:` | GATE · ODDS | none (K-NPC-6 bears on kin as a tie kind, `research/by_lane/NPC_npc_cast.md:516`) [CHECKED] | 0 |
| 43 | `transfer` :1198 | SE | yes | none | none named | — | none | 3 |
| 44 | `utter` :1218 | IN | yes | none | none named | — | K-FA-1 | 113 |
| 45 | `work` :1229 | SE | yes | none | **open**: as `restore` (`effects_economy.py:113-121`; H-164) [CHECKED-2] | EFFECT | M-SE-5 | 0 |

### A.2.2 PLANNED in v9 (12)

*retires* is the step's own column, *"retires (verbatim)"*, of #453 ids (the header at `_part5.md:68`, the rows at `:71-78`)
[CHECKED]: those are ids the step closes, **not** research lane refs. *lane ref* holds
`research/by_lane/` ids only. *contests:* is the verb's row in the verb-coverage proposal's §9
("New verbs"), a file RATIFIED AS INTENT for its §7 suite and §10.4 order
(`proposals/2026-10-03-verb-coverage-and-gap-fill.md`, its Status line) [CHECKED]; the `contests:`
lines below were opened by grep in this pass [CHECKED]. **A verb whose row routes it to the sigma
roll reads PRA when complete**: the roll's pool is the actor's `capability` under the verb's mapped
key (`sigma.py:82-109`) [CHECKED], and the key is content.

| # | verb | lane · position | `contests:` (§9 row) | reads when complete (source) | target | outcome | retires | lane ref |
|---|---|---|---|---|---|---|---|---|
| 46 | `seize` | IN · IN-12 step 6 (`_part5.md:71`) | none (`:1686`) | none named | a warrant, then a rung hold | — | K-04 | none |
| 47 | `covenant` | FA · step 7 (`:72`) | none (`:1769`) | none named | a dispensation | — | K-11, K-14, K-29, K-32, K-54 | K-FA-2 |
| 48 | `sabotage` | SE · step 9 (`:73`) | none (`:1877`) | none named | `Site.condition` | — | K-09, K-20, K-21 | none |
| 49 | `tend` | SE · step 9 (`:73`) | none (`:1933`) | none named. The row writes `Person.body` up | `Person.body` | — | K-09, K-20, K-21 | none |
| 50 | `argue` | SC · step 9 (`:73`) | *"`a proposition` (social_contest, interim `sigma_leverage`)"* (`:1902`) | PRA, through the sigma roll (T3) | the hearer's pursuits | ODDS | K-09, K-20, K-21 | none |
| 51 | `train` | IN · step 9 (`:73`) | none (`:1958`) | **a writer, not a reader**: *"`train` forms and writes `Person.capability` only where a case names a vocation"* | `Person.capability` (PRA) | raises PRA | K-09, K-20, K-21 | M-NPC-1, H-NPC-1 |
| 52 | `conceal` | IN · step 10 (`:74`) | none (`:1846`) | **none at T3**: the row has `requires: —` and `contests: none`, a `cover` Record whose `terms` is the actor (`2026-10-03-verb-coverage-and-gap-fill.md:1826-1851`) [CHECKED]. **Recorded, not counted:** the fieldwork design's scene-scale cover identity needs *"a successful Charisma roll Ob 2"* (`fieldwork_v30.md:620`), and its Cover is *"Cognition + most relevant History"* (`:575`) [CHECKED] (T4), CHA, ACU and PRA. T3 wins, and V-2 bars an attribute from a row with no `contests:` (head §3.3) | witness keys (attribution) | — | K-19 | none |
| 53 | `forgive` | SC · step 13 (`:75`) | none (`:2003`) | none named | stance | — | K-41, K-49 | none |
| 54 | `arrest` | SC · step 5 (`:76`) | *"`a standing` (`sigma_leverage`, interim) [CONFIDENCE: medium …"* (`:1594`) | PRA, through the sigma roll (T3) | `detain` | ODDS | K-05, K-18, K-26 | none |
| 55 | `pardon` | SC · step 5 (`:76`) | none (`:1727`) | none named | `detain`, `ban` | — | K-05, K-18, K-26 | none |
| 56 | `interrogate` | SC · step 5 (`:76`) | *"`a proposition` (social_contest, interim `sigma_leverage`)"* (`:1634`) | PRA, through the sigma roll (T3). The fieldwork design's inquiry table (`fieldwork_v30.md:299-306`) does not list it | testimony | ODDS · MEMORY | K-05, K-18, K-26 | M-FI-3 |
| 57 | `raze` | MB · step 11 (`:78`) | none (`:1814`) | none named | `w.rungs` | — | K-06 | none |

### A.2.3 STUBBED, code outside the loop (7)

| # | verb | lane | reads in the stub (source, T2) | target | outcome | lane ref |
|---|---|---|---|---|---|---|
| 58 | Leap `attempt_leap` (`operations.py:351`) | WR | the thread pool `spirit × 2 + min(3, history + 3) + ts // 10`: WIL, PRA, TS (`_actor_pool`, `operations.py:235-247`) [CHECKED]; the Coherence cost is resisted by `resilience`, RES (`:249-274`), whose gain ships 0 (`:157`) [CHECKED] | a target state | ODDS · COST | M-WR-1, K-WR-2 |
| 59 | Weaving `attempt_weaving` (`:375`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 60 | Pulling `attempt_pulling` (`:388`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 61 | Past-pulling `attempt_past_pulling` (`:397`) | WR | as Leap | a past moment | ODDS · COST | K-WR-2 |
| 62 | Locking `attempt_locking` (`:417`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 63 | Dissolution `attempt_dissolution` (`:434`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 64 | Mending `attempt_mending` (`:512`) | WR | as Leap | a configuration | ODDS · COST | K-WR-2, K-WR-3 |

### A.2.4 DESIGN-ONLY (1)

| # | verb | lane | reads (source, T4) | target | outcome | lane ref |
|---|---|---|---|---|---|---|
| 65 | raising a levy (`conscript`, a working name; the name is the troop design's J-3) | MB/SE | OFF: eligibility `remit:dispatch` and the seat's purview over the settlement (its §3.1, "`conscript`: raise a levy from a settlement's pool") [CHECKED, by heading]. **No actor input named** | the settlement rung's stores (a troop stock, under that design's J-1 default) | OPTIONS | K-MB-1, K-SE-5 |

---

## A.3 The verb × personal-input matrix

Only rows with at least one sourced personal input appear. ○ read today (T1). ● read by a T2 stub.
■ read by a T3 source (a ratified-as-intent design, a v9 position or a ratified K-row). ◆ read by a
T4 design only.

| verb (rows) | STR | AGI | END | FOC | ACU | WIL | ATT | CHA | BON | PRA | TS | TMP | RES | REC | KIT | inputs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `fight`, `accept` (18, 20) | ● | ● | ● | ● | ● | ● | ● | | | ● | | ● | | | ● | 10 |
| `tie / knot` (42) | | | | | | ● | | | ● | ● | ● | | | | | 4 |
| the 7 thread operations (58–64) | | | | | | ● | | | | ● | ● | | ● | | | 4 |
| `march` (22) | | | | | ● | | | ● | | | | | | | | 2 |
| `examine` (36) | | | | | | | | | | ■ | ◆ | | | | | 2 |
| `thread_read` (40) | | | | | | | | | | ■ | ■ | | | | | 2 |
| `tell` (35) | | | | | | | | | | ○● | | | | | | 1 |
| `speak`, `determine` (32, 8) | | | | | | | | | | ◆ | | | | | | 1 |
| `interview`, `research`, `surveil`, `reconstruct` (37, 38, 39, 41) | | | | | | | | | | ■ | | | | | | 1 |
| `arrest`, `argue`, `interrogate` (54, 50, 56) | | | | | | | | | | ■ | | | | | | 1 |

**Verbs by number of personal inputs read when complete, and the counting rule.** One verb row
counts once. KIT counts. OFF, BODY and person-held quantities never count (the rule under "Words").
A gate counts as a read (TS on `examine` and `thread_read`). A dark reader counts (RES: "when
complete" means the knob is armed). A reading a higher tier overrides does not count. **open**
counts as 0 named. The counts were taken from the matrix by hand and summed to 65.

| inputs read | verbs | count |
|---|---|---|
| **3 or more** | `fight`, `accept`, `tie / knot`, the 7 thread operations | **10** |
| **2** | `march`, `examine`, `thread_read` | **3** |
| **1** | `tell`, `speak`, `determine`, `interview`, `research`, `surveil`, `reconstruct`, `arrest`, `argue`, `interrogate` | **10** |
| **0 named, or open** | 32 shipped (3 of them **open**: `forge`, `restore`, `work`), 9 planned, the 1 design-only verb | **42** |
| total | | **65** |

**The derivation from the second pass's 11 / 2 / 6 / 46, one step at a time:**

1. The 2026-09-05 ruling (head §3.1.1): `thread_read` 3 → 2 (WIL struck; PRA, TS stay) moves from
   the 3+ bucket to the 2 bucket: **10 / 3 / 6 / 46**. `examine` stays at 2 (ACU → PRA; TS stays).
   `interview`, `research`, `surveil`, `reconstruct` stay at 1 (ATT, REC, ACU, REC → PRA).
2. RES gets a code and a column (second critic, finding 16): the 7 thread operations go 3 → 4; no
   bucket changes.
3. `determine` treated as `speak` (finding 16): 0 → 1: **10 / 3 / 7 / 45**.
4. The same rule applied to every planned verb whose §9 row routes it to the sigma roll: `arrest`
   0 → 1, `argue` open → 1, `interrogate` open → 1: **10 / 3 / 10 / 42**.
5. `conceal` stays at 0: T3 says no roll, and the fieldwork design's CHA, ACU and PRA readings are
   recorded on its row, not counted.

(42 = 32 + 9 + 1, of which 3 are **open** and 39 name nothing. The first draft's 9/5/14/55 of 83 and
the second pass's 11/2/6/46 are both withdrawn.)

**How thin each personal input is.**

- **STR, AGI, FOC, TMP, KIT**: only `fight`/`accept`.
- **END**: only `fight`/`accept` among verb rows; the fieldwork design's endurance-based exploration
  (`fieldwork_v30.md:92`) is scene-scale and not counted.
- **CHA**: only `march`, through `derive_command`. At T4 the fieldwork design rolls it for
  Converse, Impress, Rumour and a cover identity's setup, and sets Composure from it (`:409`,
  `:411-412`, `:620`, `:577`, `:640`) [CHECKED]: none of those is a verb row (§A.1), and the one that
  maps onto a row (`conceal`) is overridden by T3.
- **BON**: only `tie / knot`, as a gate and a cap. No CODE rolls it. The fieldwork design rolls it
  for Connect (`:410`) [CHECKED], a scene-scale act; so the census's *"Knot gate and count; never
  rolled"* (`2026-08-15-…-progression.md:476`) [CHECKED] holds for code and not for that design.
- **ATT**: only `fight`/`accept` (`interview`'s Attunement is overridden).
- **ACU**: `fight`/`accept` and `march` (`examine`'s and `surveil`'s Cognition is overridden).
- **WIL**: `fight`/`accept`, the knot roll, the thread operations (`thread_read`'s Spirit is overridden).
- **TS**: the thread operations, the knot party gate, `thread_read`'s gate (T3), `examine`'s depth
  gate (T4). TS is not an attribute, so the 2026-09-05 ruling does not reach it.
- **RES**: only the thread operations, dark.
- **REC**: **no verb row** once the ruling is applied.
- **PRA**: `fight`/`accept`, `tell`, `speak` and `determine` (T4), the six inquiry acts (T3), the knot
  roll, the thread operations, `arrest`, `argue`, `interrogate` (T3).

**Verbs that need no personal input.** 42 of 65 rows name none, or name a quantity no source
assigns. That is a finding about the SOURCES, not about the game. Most are office-, presence- or
holding-gated acts, whose OPTIONS turn on OFF or a held Tenure: `capability` *"supplies dice and
GATES NOTHING"* (`options.py:478-479`) [CHECKED-draft], and the sibling proposal: *"Every verb not in
this table needs **no** attribute … Those acts turn on remits, holdings and presence"*
(`10_verbs_and_attributes.md:148-150`) [CHECKED].

---

## A.4 The multi-input verbs: roles and how the inputs combine

Jordan: *"some verbs may require multiple attributes."* For each verb reading two or more personal
inputs, the role each plays and the combination as the source fixes it. Roles: **ODDS** (pool),
**DIFFICULTY** (Ob), **COST** (wounds, Coherence, stamina, morale), **GATE** (eligibility, a cap),
**EFFECT** (the size of what lands).

| verb | inputs → role | combination as the source fixes it | fixed or open |
|---|---|---|---|
| `fight` / `accept` | PRA → ODDS: the resolution pool `max(5, history + 6)`, *"Agility-INDEPENDENT … (ED-901)"* (`modules/combat/core.py:54-56`) [CHECKED-2]. ACU, ATT, PRA → reading: `(2·cog + att)/3 + K·(history − 3)` (`combat_systems.py:171`) [CHECKED-draft]. AGI, ATT → reflex (`:172`). AGI → tempo (`:113`). AGI, STR → balance (`:188`). END, WIL, STR → COST: `wound_interval(end, spirit)`, `health_full(end, spirit, strength)` (`combatant.py:30-40`). FOC → poise recovery, disruption resistance (`combat_systems.py:1436`, `:1452`). TMP → an aggression lean `(disp − 4)/3` (`:183`). AGI, PRA → initiative (`:1419-1421`). KIT → weapon and armour vectors [all CHECKED-draft] | **per-term weighted sums**, each term a separate channel of one bout: the arms domain's per-beat faculties (`10_verbs_and_attributes.md:142`) [CHECKED]. No single "fight score" exists | **fixed by the stub** (T2). Open on the season path: `fight.py:45` builds every field but `end` at the class default [CHECKED-2] |
| `tie / knot` | BON → GATE (≥ 5) and GATE (cap `bonds // 2 + 1`); TS → GATE (either party ≥ 30); WIL, PRA → ODDS | **gates in sequence, then a sum**: `spirit × 2 + history_relationships`, TN 7 (`knots.py:185-222`) [CHECKED-2] | **fixed by the stub** (T2). The season row has no effect yet (H-182) and declares no `contests:` |
| the 7 thread operations | WIL, PRA, TS → ODDS; RES → COST | **a sum**: `spirit × 2 + min(3, history + 3) + ts // 10` (`operations.py:235-247`) [CHECKED]. Resilience subtracts from the Coherence cost, floored at 0, at a shipped gain of 0 (`:249-274`, `:157`) [CHECKED] | **fixed by the stub** (T2). Whether RES is WIL or a tenth attribute is **open**: *"'spirit' (resilience, R-14) is a candidate input only"* (`_part5.md:444`) [CHECKED] |
| `thread_read` | PRA → ODDS; TS → GATE (≥ 30) | **dice from `capability`, behind a TS gate** (T3: the 2026-09-05 ruling; K-3) | **fixed as intent** (T3); typed nowhere. ⚠ **A methodology split, named:** the fieldwork design made Thread-Read *"a Leap; all Leaps use (Spirit × 2) + History + TPS"* (`fieldwork_v30.md:351`) [CHECKED], and the seven stub operations still do. Under the ruling `thread_read` no longer shares that pool. Not repaired here; it rides with §7.4's S finding |
| `march` | CHA, ACU → Command (`derive_command`, weights 2 : 1, `config.py:532-533`) [CHECKED-2], clamped 1–7 (`exchange.py:54`, `:65`) [CHECKED] → GATE, ODDS, COST | **one-then-other**: the attributes make Command once (`exchange.py:57-66`) [CHECKED]. At the defaults Command is **not** in the exchange pool (`exchange.py:103-126`; `config.py:556`) [CHECKED-2]. A derived Command reaches: the reform gate, Command ≥ 2 and ≥ Discipline + 1 (`orchestration.py:322-327`) [CHECKED-2]; the recall roll and the feint-recognition roll, each `roll_pool(command)` (`:2589`, `:2598`) [CHECKED]; the morale-erosion divisor `dmg / (disc × command)` (`:2252`, `:2835`; `core/state.py:96`) [CHECKED-2]; a unit's `h_per_size = max(1, min(discipline, command) + dr)` (`units.py:2815`) [CHECKED]; and **the span of control**: *"Command remains the span-of-control governor"* (`systems/mass_battle/sim/engine.py:93`; the checks against Command at `:327-331`, `:340-345`) [CHECKED], which the troop design trims at the builder (its `_part2` §4.4, `trim_to_command`) [CHECKED, by heading]. **It cannot reach** yield eligibility (`u.command > 0`, `core/state.py:105`) or rout at Command 0 (`units.py:2893`) [CHECKED]: a derived Command is clamped to ≥ 1, and Command 0 is the general-captured state, set outside `derive_command` (`orchestration.py:2221-2226`) [CHECKED]. `rally_check` is *"Empty hook — rally lands in a future cycle"* (`orchestration.py:288-290`) [CHECKED-2] and reads nothing | **fixed by the stub** (T2); the season wiring is the troop design's (T4) |
| `examine` | PRA → ODDS; TS → GATE (the Buried depth) | **dice from `capability`, a depth gate** (T3 for the dice; `fieldwork_v30.md:301` for the gate) [CHECKED] | **fixed as intent** for the dice (T3), in a design for the gate (T4); the season row reads neither. ⚠ The fieldwork design's general rows gate every investigation at Buried on TS ≥ 10 and at Liminal on TS ≥ 30 (`:44-45`, `:447`) [CHECKED], while its per-action column gives `interview` and `research` other routes to Buried (Disposition +3; institutional access) and caps `surveil` at Hidden (`:302-304`). This proposal reads the per-action column as the rule for each act. Read the other way, `interview` and `research` would each gain TS and move from the 1 bucket to the 2 bucket (to 10 / 5 / 8 / 42) |

**What the first draft got wrong here, and why it matters to the roster.**

- **Charisma has no contest reader that moves an outcome.** The kernel's `charisma` is *"a
  BUILD-TIME attribute (in player control), used only to derive Face_current's ceiling"*, and those
  *"Derived accessors … Standing/Readiness/leak behaviour is bit-identical either way"*
  (`resolver.py:191-194`, `:226-229`) [CHECKED for `:191-194`; CHECKED-2 for `:226-229`]. *"Charisma is
  NOT kernel state … it adds a derived VIEW"* (`primitives.py:128-131`) [CHECKED-2]. Its one non-test
  reader is a display line (`agon_harness.py:285-286`) [CHECKED-2]. The v30 contest design's
  adjudicator-primary attribute (`ADJUDICATOR_PRIMARY`: Cognition, Charisma, Attunement,
  `modes.py:426-431`) [CHECKED-2] is stored on the `Contest` as a label (`wrapper.py:74`, `:168`) and
  printed by the harness (`agon_harness.py:229`) [CHECKED-2]; nothing rolls it. So **Charisma's one
  outcome-moving reader is `derive_command`**.
- **Command's exchange-pool route is the stub's non-default branch.** Jordan, 2026-07-08, quoted at
  `exchange.py:104-107`: *"abandon combat pools being related to the commander"* [CHECKED-2]. A
  commander's quality still reaches a field through the gates, rolls, divisors and span above.

### A.4.1 The roster tested against co-occurrence

Jordan's test: a pair of inputs that always co-occurs is a merge candidate; an input used only
alongside another is a sub-term.

- **STR, AGI, FOC and TMP co-occur only in `fight`/`accept`** (END too, among verb rows). At the
  VERB level they are merge candidates. Inside the bout they never merge: each feeds a different term
  with a different role, and the stub keeps them apart. **The verb-level test cannot see inside a
  resolver**, so "merge" stays a candidate, not a finding.
- **CHA is used only alongside ACU, inside `derive_command`.** At the verb level that makes CHA a
  sub-term candidate. Inside Command, CHA carries twice ACU's weight (`config.py:532-533`), so it is
  not ACU's sub-term either. The test cannot see weights; this stays a candidate.
- **ACU appears without CHA** in combat reading only, now that `examine`'s and `surveil`'s Cognition
  are overridden.
- **WIL appears in combat, the knot roll and the thread pool.** It is not a sub-term.
- **TS appears with WIL and PRA** (thread pool, knot), **with PRA alone** (`thread_read`, `examine`),
  and **as a gate** in each of those but the thread pool. The registry scales it 0–100 as a
  practitioner stat.
- **RES appears only beside WIL, PRA and TS, in the thread operations.** At the verb level it is a
  sub-term candidate of the thread pool; the plan names it a candidate input for the tenth.
- **BON appears only as a gate and a cap** in code. The 2026-08-15 proposal's class *"Capacities
  (gate what you may hold, never roll)"* (`2026-08-15-…-progression.md:124-125`) [CHECKED] fits the
  code, and the fieldwork design's Connect roll (`fieldwork_v30.md:410`) does not.
- **REC appears in no verb row.**
- **PRA appears with almost everything**, and its key differs by verb: `copying`, the contest
  `faculty`, combat `history`, thread `history`, knot `history_relationships`, the inquiry dice. **It is
  one input per domain**, which is why it cannot be one of the ten (head §3.3).

### A.4.2 What each option does to a multi-input verb

- **Option B (stored).** Each DOMAIN's `faculty(domain)` names its attribute inputs and its practice
  key and fixes their combination once, in the resolver's own module (V-3,
  `10_verbs_and_attributes.md:199`) [CHECKED]; a verb reaches it only if its row declares
  `contests:` (V-2, `:198`) [CHECKED]. The template supplies the attributes; the domain owns the
  combination. So: `fight`/`accept` (`contests: "the body"`) and `march` (`"a field"`) qualify today.
  `tie / knot` and the thread operations need a `contests:` row before WIL may reach them (and the
  knot a domain: V-3's five, `10_verbs_and_attributes.md:142-146`, do not include one), and the
  knot's BON gate and cap read a bare attribute, which V-2 and V-3 forbid unless the proposed V-2a is
  ruled (head §3.7). The inquiry acts read no attribute while the 2026-09-05 ruling stands, and the
  live roster records that they must not be made contests (head §3.1.1). A multi-input verb costs
  nothing extra in the template.
- **Option A (derived).** Each verb names the PRACTICES it reads, plus BODY and KIT.
  - **Combat** collapses to one combat practice key, plus body, plus kit. The `Combatant`
    attributes sit at the class default for everyone, or are derived from practice. No source gives
    that derivation: **open**.
  - **Command** collapses to a command practice, set on `Officer.command` directly
    (`units.py:2711`) [CHECKED-2]: `derive_command` then has no inputs.
  - **The knot** loses BON (gate and cap) and WIL (roll): **open** (head §3.3).
  - **Under A, multi-input verbs are where differences between persons disappear first.** That is
    the measurable cost of A (head §3.5).
