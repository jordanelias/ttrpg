# The character template — part 2: §3A, the idealized master verb table and the verb × capacity-kind matrix

## Status: PROPOSED (2026-10-16). Corrected the same day against an independent critic's report (reconciliation table at the end of `_part3`). Not ratified; merge ratifies nothing unless Jordan so rules.
## Parts, in reading order: [head](2026-10-16-character-template.md) (§0–§3) · **this file** (§3A) · [`_part3`](2026-10-16-character-template_part3.md) (§4–§10).

**What this part is for.** Jordan: *"cross reference against a master verb table that is idealized as
if fully designed and built."* The question it answers is which **capacity kinds** the verbs, taken
together, would read if every system were complete. The head's §3 folds the result into Options A
and B. This part holds the evidence.

**Words.** A **capacity kind** is a kind of personal quantity a resolver reads to set the odds, the
cost, a gate or the size of an effect: one of the registry's nine attributes, practice, Thread
Sensitivity, temperament, Recall, or kit. (The first draft said "axis". That word is taken: the
engine's `AXES` in `engine/substrate/descriptors.py` is *"THE ONLY AXIS ROSTER IN THE ENGINE"*
(`:110`, `:124`), and the verb table's rows are *"celled on the seven axes"* (`verb_table.yaml:578`)
[CHECKED].) A person-held QUANTITY that is not a capacity (a claim in his own
ledger, a Record he holds, his `weight`, a stance row) is named where a row reads it, and never
counted as a capacity kind.

**Discipline.** No verb is invented. Every row names a source. **[CHECKED]** means opened in the
correction pass; **[CHECKED-draft]** means opened in the drafting pass and not re-opened since. The
tier tags are the head's (T1 loop code, T2 stub code, T3 ratified spec or v9 position, T4 design
intent, including the quarantined designs, cited by bare filename as the tree's own rows cite them).
In the "reads" columns, *today* is T1 only, and *when complete* is what a named T2–T4 source says
the verb would read. Where no source names a capacity kind, the cell says **none named**: a claim
about the sources, not about the game. **open** means a source names a quantity that a capacity
would plausibly set, and no source says which.

**The capacity-kind codes.** The registry's nine (`references/descriptor_registry.yaml:36-48`)
[CHECKED], each with the alias the stub code spells:

- **STR** Strength. **AGI** Agility. **END** Endurance.
- **FOC** Focus. **ACU** Acuity (code and the fieldwork design: Cognition; the alias is
  *"[ASSUMPTION] … Jordan veto"*, `:42`). **WIL** Will (code and designs: Spirit).
- **ATT** Attunement (code: `att`). **CHA** Charisma. **BON** Bonds.

Plus five codes that are not on the registry:

- **PRA** practice, or "History", per domain: what training writes.
- **TS** Thread Sensitivity (`descriptor_registry.yaml:61-65`, `practitioner_stats`; its derived
  Thread Pool Score is `floor(TS / 10)`) [CHECKED].
- **TMP** temperament (combat `disp`).
- **REC** Recall: primary for two inquiries in the fieldwork design (`fieldwork_v30.md:303`, `:306`)
  [CHECKED], and classed *"capacity, not attribute"* by the 2026-08-15 census
  (`proposals/2026-09-30-character-and-play-surface/10_verbs_and_attributes.md:152-156`) [CHECKED].
- **KIT** what a person carries.

**OFF** (office) and **BODY** (condition) are named where a verb reads them. They are not capacity
kinds: office is a Tenure and body is live state (head §3.3).

---

## A.1 The inclusion rule, and the count

**A row is a VERB when a source names it as an act a person (or the seat he exercises) chooses at
the season's scale, as an act of its own.** Five kinds of thing are therefore NOT rows, and the rule
is applied to every candidate, not only to the ones the first draft dropped:

| excluded as | members | why, and where its reads go |
|---|---|---|
| **a value of another verb's parameter** | `yield` | it is a value of `challenge_terms: [yield, blood, death]` and a stop rule inside `fight` (`workplans/valoria_master_workplan_v9_part7.md:58`) [CHECKED] |
| **a form or arm of another verb** | the charge; the spoken lie; resigning one's own seat; `form_knot` | the charge: *"no row is added (the charge is an `utter`)"* (`_part5.md:77`) [CHECKED]. The lie: *"an arm of `said_of`"*, the site where a teller chooses what to pass on (K-SC-6, `research/by_lane/SC_social_contest.md:710`) [CHECKED], so a form of `tell`. Resigning: *"Resignation composes on `release`"* (K-FA-3, `research/by_lane/FA_faction_actions.md:582`) [CHECKED]. `form_knot` (`systems/fieldwork/sim/knots.py:173`) [CHECKED] is the stub resolver of the shipped `tie / knot` row's `knot` half, so its reads are that row's |
| **a choice or check inside one verb's resolution** | the combat bout's terms; `engage`, `withdraw`; the seven contest move kinds; rally, reform, recall and the feint check | the bout's terms and IN-46's `{engage, withdraw}` (an [ASSUMPTION] in the plan, `_part4.md:34`) [CHECKED] are inside one `fight`. The move kinds `advance, hard, shift, support, pass, evidence, rebut` (`systems/social_contest/sim/contest/resolver.py:34`) [CHECKED] are inside one contest, so their reads fold into `tell` (the one contested social verb). Rally, reform, recall and the feint check are phase checks inside one field, so their reads fold into `march` (§A.4) |
| **a private helper** | `_charge_shock_sigma`, `_brace_setup_ok` | `modules/mass_battle/resolution.py:176`, `:132` [CHECKED]: leading-underscore functions, not orders |
| **superseded** | `practice` | *"K-4 (a `practice` verb) superseded by IN-12 step 9's `train`"* (`workplans/valoria_master_workplan_v9_part8.md:207`) [CHECKED]. (The first draft cited `_part7.md:51`, which says something else.) |

The thread operations' lane recommendation (K-WR-2, `research/by_lane/WR_world.md:538`)
[CHECKED-draft] is carried as the lane reference on the 7 STUBBED thread rows, not as rows of its own.

| status class | rows | how counted |
|---|---|---|
| **SHIPPED, resolvable** | **37** | `python -c "from engine.season.loop.driver import resolvable_verbs; print(len(resolvable_verbs()))"` → `37` [RAN] |
| **SHIPPED, not resolvable** | **8** | the 45 rows of `grep -n '^  - verb:' engine/season/verb_table.yaml` (→ 45 lines) minus `resolvable_verbs()` [RAN]: `carry`, `construe`, `evade / defy`, `exchange`, `forge`, `succeed`, `thread_read`, `tie / knot` |
| **PLANNED in v9** | **12** | IN-12 steps 6, 7, 9, 10, 13, 5, 11 (`_part5.md:71-78`) [CHECKED]: `seize`, `covenant`, `sabotage`, `tend`, `argue`, `train`, `conceal`, `forgive`, `arrest`, `pardon`, `interrogate`, `raze` |
| **STUBBED** (code outside the season loop) | **7** | the thread operations, `systems/threadwork/sim/operations.py:351, :375, :388, :397, :417, :434, :512` [CHECKED] |
| **DESIGN-ONLY** | **1** | the troop design's one new verb, raising a company (`proposals/2026-10-16-troop-stock-design.md` §3.1, `:494-496`; its working name is `conscript` at `:17` and `:84`, and its §3.1 heading still reads `levy`; the file was under a sibling's edit while this was read) [CHECKED] |
| **total** | **65** | |

**SHIPPED is a row count, not an execution count** (`CLAUDE.md` §0.2). Of the 45 rows, 8 cannot be
attempted at all. Of the 37 that can, the plan records 17 verbs executing in `corpus_run` after
IN-57 (*"executed verbs went 21 → 17"*, `_part5.md:471`) [CHECKED: the line; the run not repeated].
This pass ran the populated realm instead (§10 probe 6): four seasons at seed 0, the measured arm's
`World.content_hash()` equal to the untouched control's, 2432 acts. **25 verbs executed at least
once and 35 were attempted.** Per-verb counts are §A.2.1's last column. The 25 are all shipped and
resolvable; no unresolvable row executed, by construction.

---

## A.2 The table

### A.2.1 SHIPPED (45: 37 resolvable, 8 not)

`R?` is membership of `resolvable_verbs()` [RAN]. *Ex. (realm)* is the number of executions in four
populated-realm seasons at seed 0 (§10 probe 6) [RAN]. Every row also reads BODY indirectly, through
the scene budget (`engine/season/decision/budget.py:57-61`) [CHECKED-draft]; that is one shared cost,
not repeated per row.

| # | verb (`verb_table.yaml` line) | lane | R? | reads today (T1): capacity kinds; *person-held quantities* | reads when complete (source, tier) | outcome a capacity would move | lane ref | Ex. (realm) |
|---|---|---|---|---|---|---|---|---|
| 1 | `carry` :105 | SC | no | none | none named | — | — | 0 |
| 2 | `commit` :123 | FA | yes | none | none named | — | — | 1 |
| 3 | `comply` :139 | IN | yes | none; *the actor's own ledger* (`own_ledger` of subject, `:148-154`) [CHECKED] | none named | — | — | 0 |
| 4 | `confer` :163 | FA | yes | OFF (the seat exercised, via `Act.via`) | none named | OPTIONS (office) | — | 1 |
| 5 | `convene` :183 | SC | yes | none | none named | — | — | 0 |
| 6 | `create_record` :194 | FI | yes | none | none named | — | — | 187 |
| 7 | `destroy_record` :205 | FI | yes | none | none named | — | — | 0 |
| 8 | `determine` :217 | SC | yes | OFF | none named. The proceedings design lists it in the "standing and the matter" domain, *"proposed"*, and binds no attribute (`10_verbs_and_attributes.md:144`) [CHECKED] (T4) | OPTIONS | — | 3 |
| 9 | `dispatch` :263 | IN | yes | OFF | none named | OPTIONS | — | 13 |
| 10 | `establish` :278 | FA | yes | OFF | none named | OPTIONS | — | 0 |
| 11 | `evade / defy` :292 | IN | no | none | none named | — | — | 0 |
| 12 | `exchange` :307 | SE | no | none | none named | — | K-SE-4 | 0 |
| 13 | `forge` :325 | FI | no | none | **open**: the row writes `Record.forgery_quality`, and no source says what sets its value | EFFECT, if a source rules one | M-FI-2 | 0 |
| 14 | `found` :354 | SE | yes | none | none named | — | — | 0 |
| 15 | `build` :377 | SE | yes | none | none named | — | — | 0 |
| 16 | `give` :400 | IN | yes | none; *a Record the actor holds* (`relation: held_by`, `:406-417`) [CHECKED] | none named | — | — | 1 |
| 17 | `issue` :428 | FA | yes | OFF | none named | OPTIONS | K-FA-12 | 5 |
| 18 | `fight` :475 | PC | yes | BODY → `end` (`seam/wrappers/combat.py:129-138`) [CHECKED] | STR AGI END ACU FOC WIL ATT PRA TMP KIT: every `Combatant` field (`modules/combat/combatant.py:93-94`) [CHECKED] (T2) | ODDS · EFFECT · COST (wounds) | M-PC-1, K-PC-1 | 16 |
| 19 | `challenge` :579 | PC | yes | none | none named | — | — | 14 |
| 20 | `accept` :600 | PC | yes | as `fight` | as `fight` (T2) | as `fight` | M-PC-1 | 28 |
| 21 | `requisition` :629 | SE | yes | OFF | none named | OPTIONS | K-SE-5 | 0 |
| 22 | `march` :664 | MB | yes | none: the side's members' `weight`, stance and loyalty, no commander (`seam/wrappers/mass_battle.py:175-200`) [CHECKED-draft] | CHA, ACU, through `derive_command` (`modules/mass_battle/core/exchange.py:57-66`; `hierarchy/units.py:2700-2722`, live while `COMMAND_SIGMA_ENABLED`, default on, `config.py:530`) [CHECKED] (T2). **Not through the exchange pool:** under `POOL_QUALITY_MODEL`, default on (`config.py:556`), the pool is `eff_power × eff_size` and *"Command is absent from this branch entirely"* (`exchange.py:103-126`) [CHECKED]. See §A.4 for where Command still reaches | GATE (reform) · ODDS (recall, feint) · COST (morale erosion) | M-MB-3, K-MB-2, M-NPC-13 | 18 |
| 23 | `migrate` :698 | SE | yes | none; *the migrant's own `weight`* against the destination's capacity (`loop/effects_migration.py:195`) [CHECKED] | none named | — | — | 0 |
| 24 | `move` :720 | IN | yes | none | none named | — | — | 55 |
| 25 | `oblige` :735 | FA | yes | none | none named | — | — | 16 |
| 26 | `open_case` :757 | SC | yes | none | none named | — | — | 8 |
| 27 | `petition` :782 | SC | yes | none | none named | — | K-SC-3 | 28 |
| 28 | `construe` :806 | SC | no | none | none named | — | — | 0 |
| 29 | `release` :822 | FA | yes | none | none named | — | — | 12 |
| 30 | `restore` :839 | SE | yes | none | **open**: the effect names an unbuilt `× f(degree)` term, the identity today because the act is uncontested (`loop/effects_economy.py:113-121`; H-164) [CHECKED]; no source says what would grade it | EFFECT | K-WR-3 | 0 |
| 31 | `revoke` :861 | FA | yes | OFF | none named | OPTIONS | — | 0 |
| 32 | `speak` :875 | SC | yes | **none**: the row has no `contests:` field (`:875-885`) [CHECKED], and the only path from `verb_capability` into the loop is `sigma.contest_input` (`seam/wrappers/sigma.py:132-147`) [CHECKED], reached by contested verbs only. The roster's `speak: "copying"` (`rosters.yaml:1107`) [CHECKED] is a mapping nothing reaches | PRA, **if** `speak` becomes contested: the proceedings design says *"`speak` becomes the contest"* (`10_verbs_and_attributes.md:123`) [CHECKED] (T4), and the existing mapping would then read `copying`. The same design binds no attribute: *"none bound"* (`:144`) [CHECKED] | ODDS | M-SC rows, K-SC-2 | 70 |
| 33 | `succeed` :886 | FA | no | none | none named | — | — | 0 |
| 34 | `survey` :917 | FI | yes | none; *the actor's own ledger* (`own_ledger` of subject, `:923-925`) [CHECKED] | none named | — | — | 10 |
| 35 | `tell` :936 | SC | yes | PRA, as an opposed pair: the actor's `copying` → pool, the subject's same key ÷ 2 → Ob (`sigma.py:97-129`) [CHECKED]; *the actor's own ledger* (its precondition is `own_ledger`, as `reconstruct`'s, `:1179`) [CHECKED] | PRA. The contest kernel's `faculty` → `Pool.size` and `Leverage.net` (`resolver.py:300-301`) [CHECKED-draft] (T2), a kernel the sibling proposal calls *"retiring"*, with attributes *"none bound"* (`10_verbs_and_attributes.md:144`) [CHECKED]. The seven move kinds fold in here; the `evidence` move reads the contestant's evidence items (`resolver.py:184-190`) [CHECKED], a person-held quantity, not a capacity kind. **CHA moves no outcome**: §A.4 | ODDS | K-SC-2, M-NPC-1 | 36 |
| 36 | `examine` :1083 | FI | yes | none | ACU (Cognition, *"Primary Attribute"*), and TS as a gate on the Buried depth, *"Buried (3) if TS ≥ 10"* (`fieldwork_v30.md:301`) [CHECKED] (T4, quarantined design) | ODDS · GATE (depth) · MEMORY | M-FI-3, K-FI-1 | 0 |
| 37 | `interview` :1105 | FI | yes | none | ATT (`fieldwork_v30.md:302`) [CHECKED] (T4). ⚠ That row is kept only as *"the current mechanical baseline"*: ED-FI-0004 folds Interview into the Dialogue Lattice (`:308`) [CHECKED] | ODDS · MEMORY | K-FI-1 | 20 |
| 38 | `research` :1121 | FI | yes | none | REC (`fieldwork_v30.md:303`) [CHECKED] (T4) | ODDS · MEMORY | K-FI-1 | 25 |
| 39 | `surveil` :1137 | FI | yes | none | ACU (`fieldwork_v30.md:304`) [CHECKED] (T4) | ODDS · MEMORY | K-FI-1 | 56 |
| 40 | `thread_read` :1157 | FI/WR | no | none: untyped, and so not resolvable (the row says so itself, `:1163`) [CHECKED] | WIL, PRA, TS: pool *"(Spirit × 2) + History + TPS"*, with TPS = TS ÷ 10, and *"TS ≥ 30 required"* (`fieldwork_v30.md:305`, `:351`) [CHECKED] (T4). K-3 types the TS precondition (`09_the_character_sheet.md:130`) [CHECKED] (T4, ratified as intent, `_part8.md:207`) [CHECKED] | ODDS · GATE | K-3 | 0 |
| 41 | `reconstruct` :1171 | FI | yes | none; *the actor's own ledger* (`own_ledger` of subject, `:1176-1178`) [CHECKED] | REC (`fieldwork_v30.md:306`) [CHECKED] (T4) | MEMORY | K-FI-1 | 111 |
| 42 | `tie / knot` :1186 | IN | no | none (H-182: the row has no effect) | for `knot`, from `form_knot`: BON as a gate (`bonds ≥ 5`, `knots.py:185-187`) and as a cap (`bonds // 2 + 1` knots, `:200-203`); TS as a party gate (either party `ts ≥ 30`, `:195-198`, `KNOT_TS_MIN_PARTY` `:54`); WIL and PRA as the formation roll, `spirit × 2 + history_relationships`, TN 7 (`:212-222`) [CHECKED] (T2). The disposition gate (`:189-193`) reads a stance, not a capacity. For `tie`: none named | GATE · ODDS | M-NPC rows | 0 |
| 43 | `transfer` :1198 | SE | yes | none | none named | — | — | 3 |
| 44 | `utter` :1218 | IN | yes | none | none named | — | K-FA-1 | 113 |
| 45 | `work` :1229 | SE | yes | none | **open**: as `restore` (`effects_economy.py:113-121`; H-164) [CHECKED] | EFFECT | M-SE-5 | 0 |

### A.2.2 PLANNED in v9 (12)

| # | verb | lane · position | reads when complete (source) | target | outcome | lane ref |
|---|---|---|---|---|---|---|
| 46 | `seize` | IN · IN-12 step 6 (`_part5.md:71`) | none named | a warrant, then a rung hold | — | — |
| 47 | `covenant` | FA · step 7 (`:72`) | none named | a dispensation | — | K-FA-2 |
| 48 | `sabotage` | SE · step 9 (`:73`) | none named | `Site.condition` | — | — |
| 49 | `tend` | SE · step 9 (`:73`) | none named. The row writes `Person.body` up | `Person.body` | — | — |
| 50 | `argue` | SC · step 9 (`:73`) | **open**: it writes `Person.pursuits`; a persuasion that moves values is a natural PRA reader, and no source says so | the hearer's pursuits | — | — |
| 51 | `train` | IN · step 9 (`:73`) | **a writer, not a reader**: *"`train` forms and writes `Person.capability` only where a case names a vocation"* | `Person.capability` (PRA) | raises PRA | M-NPC-1, H-NPC-1 |
| 52 | `conceal` | IN · step 10 (`:74`) | none named | witness keys | — | K-19 |
| 53 | `forgive` | SC · step 13 (`:75`) | none named | stance | — | K-41 |
| 54 | `arrest` | SC · step 5 (`:76`) | none named | `detain` | — | K-05 |
| 55 | `pardon` | SC · step 5 (`:76`) | none named | `detain`, `ban` | — | K-05 |
| 56 | `interrogate` | SC · step 5 (`:76`) | **open**: an inquiry under coercion; the fieldwork design's inquiry table (`fieldwork_v30.md:301-306`) does not list it | testimony | MEMORY | M-FI-3 |
| 57 | `raze` | MB · step 11 (`:78`) | none named | `w.rungs` | — | K-06 |

### A.2.3 STUBBED, code outside the loop (7)

| # | verb | lane | reads in the stub (source, T2) | target | outcome | lane ref |
|---|---|---|---|---|---|---|
| 58 | Leap `attempt_leap` (`operations.py:351`) | WR | the thread pool `spirit × 2 + min(3, history + 3) + ts // 10`: WIL, PRA, TS (`_actor_pool`, `operations.py:235-247`) [CHECKED]; the Coherence cost is resisted by `resilience` (`:249-274`), whose gain ships 0 (`:157`) [CHECKED] | a target state | ODDS · COST | M-WR-1, K-WR-2 |
| 59 | Weaving `attempt_weaving` (`:375`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 60 | Pulling `attempt_pulling` (`:388`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 61 | Past-pulling `attempt_past_pulling` (`:397`) | WR | as Leap | a past moment | ODDS · COST | K-WR-2 |
| 62 | Locking `attempt_locking` (`:417`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 63 | Dissolution `attempt_dissolution` (`:434`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 64 | Mending `attempt_mending` (`:512`) | WR | as Leap | a configuration | ODDS · COST | K-WR-2, K-WR-3 |

### A.2.4 DESIGN-ONLY (1)

| # | verb | lane | reads (source, T4) | target | outcome | lane ref |
|---|---|---|---|---|---|---|
| 65 | raising a company (`conscript`, working name; §3.1 heading `levy`) | MB/SE | OFF (the raising seat). The company's grade sits in its own `capability` (`troop-stock-design.md:378`) [CHECKED]. **No actor capacity named** | a cohort's weight | OPTIONS | K-MB-1, K-SE-5 |

---

## A.3 The verb × capacity-kind matrix

Only rows with at least one sourced capacity kind appear. ● read by a T2 stub. ◆ read by a T4
design only. ○ read today (T1).

| verb (rows) | STR | AGI | END | FOC | ACU | WIL | ATT | CHA | BON | PRA | TS | TMP | REC | KIT | kinds |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `fight`, `accept` (18, 20) | ● | ● | ● | ● | ● | ● | ● | | | ● | | ● | | ● | 10 |
| `tie / knot` (42) | | | | | | ● | | | ● | ● | ● | | | | 4 |
| the 7 thread operations (58–64) | | | | | | ● | | | | ● | ● | | | | 3 |
| `thread_read` (40) | | | | | | ◆ | | | | ◆ | ◆ | | | | 3 |
| `march` (22) | | | | | ● | | | ● | | | | | | | 2 |
| `examine` (36) | | | | | ◆ | | | | | | ◆ | | | | 2 |
| `tell` (35) | | | | | | | | | | ○● | | | | | 1 |
| `speak` (32) | | | | | | | | | | ◆ | | | | | 1 |
| `interview` (37) | | | | | | | ◆ | | | | | | | | 1 |
| `surveil` (39) | | | | | ◆ | | | | | | | | | | 1 |
| `research`, `reconstruct` (38, 41) | | | | | | | | | | | | | ◆ | | 1 |

**Verbs by number of capacity kinds read when complete, and the counting rule.** One verb row counts
once. KIT counts. OFF, BODY and person-held quantities do not. A gate counts as a read (TS on
`examine`). **open** counts as 0 named. The counts were taken from the table above by hand and summed
to 65.

| kinds read | verbs | count |
|---|---|---|
| **3 or more** | `fight`, `accept`, `tie / knot`, `thread_read`, the 7 thread operations | **11** |
| **2** | `march`, `examine` | **2** |
| **1** | `tell`, `speak`, `interview`, `research`, `surveil`, `reconstruct` | **6** |
| **0 named, or open** | 33 shipped (3 of them **open**: `forge`, `restore`, `work`), all 12 planned (2 **open**: `argue`, `interrogate`), the 1 design-only verb | **46** |
| total | | **65** |

(46 = 33 + 12 + 1, of which 5 are **open** and 41 name nothing. The first draft's split, 9/5/14/55
of 83, counted non-verbs and an invented Charisma reader, and missed the knot's and the inquiry
verbs' sourced reads; it is withdrawn.)

**How thin each capacity kind is.**

- **STR, AGI, END, FOC, TMP, KIT**: only `fight`/`accept`.
- **CHA**: only `march`, through `derive_command`. It has no other reader that moves an outcome (§A.4).
- **BON**: only `tie / knot`, as a gate and a cap, never in a roll.
- **ATT**: `fight`/`accept`, and `interview` in the fieldwork design (T4).
- **ACU**: `fight`/`accept`, `march`, and `examine` and `surveil` in the fieldwork design.
- **WIL**: `fight`/`accept`, the knot roll, the thread operations, `thread_read`.
- **TS**: the thread operations, `thread_read`, the knot party gate, `examine`'s depth gate.
- **REC**: `research` and `reconstruct`, in the fieldwork design only. No code reads it.
- **PRA**: `fight`/`accept`, `tell`, `speak` (if contested), the knot roll, the thread operations,
  `thread_read`.

**Verbs that need no capacity.** 46 of 65 rows name none, or name a quantity no source assigns. That
is a finding about the SOURCES, not about the game. Most are office-, presence- or holding-gated
acts, whose OPTIONS turn on OFF or a held Tenure: `capability` *"supplies dice and GATES NOTHING"*
(`options.py:478-479`) [CHECKED-draft], and the sibling proposal: *"Every verb not in this table needs
**no** attribute … Those acts turn on remits, holdings and presence"* (`10_verbs_and_attributes.md:148-150`)
[CHECKED].

---

## A.4 The multi-kind verbs: roles and how the kinds combine

Jordan: *"some verbs may require multiple attributes."* For each verb reading two or more capacity
kinds, the role each plays and the combination as the source fixes it. Roles: **ODDS** (pool),
**DIFFICULTY** (Ob), **COST** (wounds, Coherence, stamina, morale), **GATE** (eligibility, a cap),
**EFFECT** (the size of what lands).

| verb | kinds → role | combination as the source fixes it | fixed or open |
|---|---|---|---|
| `fight` / `accept` | PRA → ODDS: the resolution pool `max(5, history + 6)`, *"Agility-INDEPENDENT … (ED-901)"* (`modules/combat/core.py:54-56`) [CHECKED]. ACU, ATT, PRA → reading: `(2·cog + att)/3 + K·(history − 3)` (`combat_systems.py:171`) [CHECKED-draft]. AGI, ATT → reflex (`:172`). AGI → tempo (`:113`). AGI, STR → balance (`:188`). END, WIL, STR → COST: `wound_interval(end, spirit)`, `health_full(end, spirit, strength)` (`combatant.py:30-40`). FOC → poise recovery, disruption resistance (`combat_systems.py:1436`, `:1452`). TMP → an aggression lean `(disp − 4)/3` (`:183`). AGI, PRA → initiative (`:1419-1421`). KIT → weapon and armour vectors [all CHECKED-draft] | **per-term weighted sums**, each term a separate channel of one bout. No single "fight score" exists | **fixed by the stub** (T2). Open on the season path: `fight.py:45` builds every field but `end` at the class default [CHECKED] |
| `tie / knot` | BON → GATE (≥ 5) and GATE (cap `bonds // 2 + 1`); TS → GATE (either party ≥ 30); WIL, PRA → ODDS | **gates in sequence, then a sum**: `spirit × 2 + history_relationships`, TN 7 (`knots.py:185-222`) [CHECKED] | **fixed by the stub** (T2). The season row has no effect yet (H-182) |
| the 7 thread operations | WIL, PRA, TS → ODDS; `resilience` → COST | **a sum**: `spirit × 2 + min(3, history + 3) + ts // 10` (`operations.py:235-247`) [CHECKED]. Resilience subtracts from the Coherence cost, floored at 0, at a shipped gain of 0 (`:249-274`, `:157`) [CHECKED] | **fixed by the stub** (T2). Whether `resilience` is WIL or a tenth attribute is **open**: *"'spirit' (resilience, R-14) is a candidate input only"* (`_part5.md:444`) [CHECKED] |
| `thread_read` | WIL, PRA, TS → ODDS; TS → GATE (≥ 30) | **the Leap sum**: *"Thread-Read is a Leap; all Leaps use (Spirit × 2) + History + TPS"* (`fieldwork_v30.md:351`) [CHECKED] | **fixed in a design** (T4); typed nowhere |
| `march` | CHA, ACU → Command (`derive_command`, weights 2 : 1, `config.py:532-533`) [CHECKED] → GATE, ODDS, COST | **one-then-other**: the attributes make Command once (`exchange.py:57-66`) [CHECKED]. At the defaults Command is **not** in the exchange pool (`exchange.py:103-126`; `config.py:556`) [CHECKED]. It reaches: the reform gate, Command ≥ 2 and ≥ Discipline + 1 (`orchestration.py:322-327`); the recall roll and the feint-recognition roll, each `roll_pool(command)` against Ob 2 (`:2589`, `:2598`); the morale-erosion divisor `dmg / (disc × command)` (`:2252`, `:2835`; `core/state.py:96`); yield eligibility (`core/state.py:105`); a unit's `h_per_size` (`units.py:2815`); rout at Command 0 (`:2893`) [all CHECKED]. `rally_check` is *"Empty hook — rally lands in a future cycle"* (`orchestration.py:288-290`) [CHECKED] and reads nothing | **fixed by the stub** (T2); the season wiring is the troop design's (T4) |
| `examine` | ACU → ODDS; TS → GATE (the Buried depth) | **a primary attribute and a depth gate** (`fieldwork_v30.md:301`) [CHECKED] | **fixed in a design** (T4); the season row reads neither |

**What the first draft got wrong here, and why it matters to the roster.**

- **Charisma has no contest reader that moves an outcome.** The kernel's `charisma` is used *"only
  to derive Face_current's ceiling"*, and those *"Derived accessors … Standing/Readiness/leak
  behaviour is bit-identical either way"* (`resolver.py:191-194`, `:226-229`) [CHECKED]. *"Charisma
  is NOT kernel state … it adds a derived VIEW"* (`primitives.py:128-131`) [CHECKED]. Its one
  non-test reader is a display line (`agon_harness.py:285-286`) [CHECKED]. The v30 contest design's
  adjudicator-primary attribute (`ADJUDICATOR_PRIMARY`: Cognition, Charisma, Attunement,
  `modes.py:426-431`) [CHECKED] is stored on the `Contest` as a label (`wrapper.py:74`, `:168`) and
  printed by the harness (`agon_harness.py:229`) [CHECKED]; nothing rolls it. So **Charisma's one
  outcome-moving reader is `derive_command`**.
- **Command's exchange-pool route is the stub's non-default branch.** Jordan, 2026-07-08, quoted at
  `exchange.py:104-107`: *"abandon combat pools being related to the commander"* [CHECKED]. A
  commander's quality still reaches a field through the gates, rolls and divisors above.

### A.4.1 The roster tested against co-occurrence

Jordan's test: a pair of kinds that always co-occurs is a merge candidate; a kind used only alongside
another is a sub-term.

- **STR, AGI, END, FOC and TMP co-occur only in `fight`/`accept`.** At the VERB level they are merge
  candidates. Inside the bout they never merge: each feeds a different term with a different role,
  and the stub keeps them apart. **The verb-level test cannot see inside a resolver**, so "merge"
  stays a candidate, not a finding.
- **CHA is used only alongside ACU, inside `derive_command`.** At the verb level that makes CHA a
  sub-term candidate. Inside Command, CHA carries twice ACU's weight (`config.py:532-533`), so it is
  not ACU's sub-term either. The test cannot see weights; this stays a candidate.
- **ACU appears without CHA**: combat reading, and `examine`/`surveil` in the fieldwork design.
- **WIL appears in combat, the knot roll, `thread_read` and the thread pool.** It is not a sub-term.
- **TS appears with WIL and PRA** (thread pool, `thread_read`, knot), and **alone as a gate**
  (`examine`'s depth, the knot's party gate). The registry scales it 0–100 as a practitioner stat.
- **BON appears only as a gate and a cap**, never in a roll. The 2026-08-15 proposal's class
  *"Capacities (gate what you may hold, never roll)"* (`proposals/2026-08-15-character-and-faction-stats-and-progression.md:124-125`)
  [CHECKED] fits it.
- **REC appears alone**, in two inquiries, in a design only. The same proposal puts it in the same
  class as BON (`:124-125`, `:202`) [CHECKED], while the fieldwork design rolls it as a primary
  attribute (`fieldwork_v30.md:303`, `:306`). The two sources disagree on whether Recall is ever rolled.
- **PRA appears with almost everything**, and its key differs by verb: `copying`, the contest
  `faculty`, combat `history`, thread `history`, knot `history_relationships`. **It is one kind per
  domain**, which is why it cannot be one of the ten (head §3.3).

### A.4.2 What each option does to a multi-kind verb

- **Option B (stored).** Each verb's resolver names its attribute inputs and fixes their combination
  in its own module, as the stubs already do. The template supplies the attributes; the verb owns the
  combination. A multi-kind verb costs nothing extra in the template.
- **Option A (derived).** Each verb names the PRACTICES it reads, plus BODY and KIT.
  - **Combat** collapses to one combat practice key, plus body, plus kit. The `Combatant`
    attributes sit at the class default for everyone, or are derived from practice. No source gives
    that derivation: **open**.
  - **Command** collapses to a command practice, set on `Officer.command` directly
    (`units.py:2711`) [CHECKED]: `derive_command` then has no inputs.
  - **The knot** loses BON (gate and cap) and WIL (roll): **open** (head §3.3).
  - **Under A, multi-kind verbs are where differences between persons disappear first.** That is
    the measurable cost of A (head §3.5).
