# A6: the attribute set, re-derived from demand

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Part 06 of the suite (A6, attribute set re-derived from demand; the source of the 104-moment demand matrix behind `03_P2`). Source: the session's own record of a single Write tool call at 06:44:27Z (11,833 bytes, equal to the 07:10:36 listing of `suite/06`; copied unchanged at 07:10:35), recovered 2026-10-30 from the 2026-10-28 transcript (third pass). Edit-tool and heredoc changes found in the transcript were replayed in time order and the replayed size matches the size the session printed with `ls -la`. Text otherwise unchanged. Analyst reports are subagent output: figures in them are the analyst's, not verified here, and the suite's three-lens review (parts 07a to 07d, `critic_lens3.md`) found errors in some.

---

**VERDICT: No, the nine do not survive intact.** Six stay (STR END AGI ACU WIL CHA). Focus merges into Will, Bonds merges into Charisma, and Attunement splits into **Perception** and **Insight**: **eight attributes on 1–7**. Thread Sensitivity stays on its own carrier and does **not** become a tenth. [CONFIDENCE: medium. The designed-verb half of the matrix is my mapping of PROPOSED lexicons; the built half is verified.]

## 1. Demand matrix

**BUILT (season path, verified at HEAD `be24c71`):**
- `verb_table.yaml` has 56 rows. Eight carry `contests:`: `fight` and `accept` go to combat; `march` to mass battle; `tell`, `arrest`, `speak`, `argue` and `determine` to `social_contest.roll`. Three inquiries are graded through the same roll (`research`, `examine`, `surveil`, `rosters.yaml:1143-1145`).
- **45 of 56 rows read no person quantity**, by rule: eligibility is own, remit, hold or presence, never capability (`verb_table.yaml:33-35`).
- The 11 resolving moments read:
  - `Person.body`, turned into one combat field, `end` (`seam/wrappers/combat.py:130-138`);
  - `weight` and `stance` (`MassBattleInput`);
  - `capability[verb_capability[verb]]`, else `pool_default` (`sigma.py:119-131`). There are two rows, `tell` and `speak`, both mapped to `copying` (`rosters.yaml:1231-1233`); 1 of 430 persons holds that key.
- **None of the nine is read on the season path.** [NULL: `engine/season` has no `Person.attributes` and no `faculty`.] CR-20 lists `faculty` as LANDED ALREADY (`workplans/valoria_master_workplan_v10_part4.md:184`); it does not exist yet.

**MODULE code (T2, off the season path):**
- **Combat.** `Combatant(strength, agi, end, cog, att, spirit, focus, history, disp)` (`modules/combat/combatant.py:93`).
  - References: strength 17, agi 8, spirit 7, end 6, focus 4, att 3, cog 2.
  - `att` is used in two senses: `reflex = (2·agi+att)/3` and `reading = (2·cog+att)/3` (`combat_systems.py:171-172`).
  - `focus` feeds `conc_max = 3F+2S`, disruption and poise (`:1436,1452`).
- **Mass battle.** `derive_command(charisma, cognition)`, weighted 2:1 (`core/exchange.py:57-66`), Officer units only; the season loop does not feed it.
- **Threadwork.** Pool = `2·spirit + min(3, history+3) + ts//10` (`systems/threadwork/sim/operations.py:235-247`); Leap gate is TS ≥ 30. It is unplugged from the season loop (`loop/matter.py:135`).
- **Knots.** Gate and cap on `bonds` (`bonds//2+1`), roll on `spirit` (`systems/fieldwork/sim/knots.py:185-216`). The season's `tie / knot` row is uncontested and never calls it.

**DESIGNED:** 83 draws from the lexicons in `proposals/2026-10-16-verbs/` (files -09 to -18).

**Matrix:** 104 moments (11 built, 10 module, 83 designed), scripted at `/tmp/claude-0/-home-user-ttrpg/a0006cad-2382-5a52-b1f4-b17983d229b1/scratchpad/a6/matrix.py`. The cells are [REASONED].

| attribute | main input of | built / module / designed | subsystems (of 10) | finding |
|---|---|---|---|---|
| ATT | 27 | 2 / 0 / 25 | 9 | **dominant**; two capacities: *notice* 15, *read people* 12, in mostly different subsystems |
| ACU | 21 | 6 / 1 / 14 | 7 | |
| CHA | 17 | 4 / 1 / 12 | 4 | |
| AGI | 15 (22 with stealth) | 2 / 1 / 12 | 5 | |
| END | 11 | 2 / 1 / 8 | 3 | |
| TS | 11 | 0 / 4 / 7 | 1 | practitioner stat, by design |
| STR | 10 | 2 / 1 / 7 | 3 | |
| WIL | 9 | 0 / 2 / 7 | 2 | |
| BON | 7 | 0 / 1 / 6 | 3 | **orphan in code**: one off-path module reads it |
| FOC | 1 | 0 / 1 / 0 | 1 | **orphan**: secondary in 11 moments, the main input of none |

**The four tests:**
- **(a) Redundancy.** No pair is demanded together everywhere. The highest overlaps are AGI–STR at 0.39 (combat) and WIL–TS at 0.33 (thread pool); both diverge elsewhere. FOC–WIL is *functional* redundancy: Will already sits inside `conc_max` and stamina, and Focus's two other readers measure composure.
- **(b) Orphans.** FOC and BON.
- **(c) Gaps.** Stealth (main input of 8, in 6 subsystems), lore (secondary in 9), craft. All close as **capability keys on an existing base** (stealth on AGI, lore on ACU), not as new attributes; skills are not primaries (`attributes-from-scratch_part4.md:187-189`). "Endurance of mind" is Will.
- **(d) Dominance.** ATT is the main input of 29% of contested draws. After the split, the largest share is CHA at 23%, and every attribute is the main input of at least 10 moments.

**NERS cut test** (what dies if cut):
- **STR, END, AGI, ACU, CHA, WIL.** Real losses each, with nothing ruled in to supply them.
- **FOC.** Loses one sheet distinction, concentration vs resolve, which only combat reads. **False N-line:** Will supplies it.
- **BON.** Loses the knot gate and cap and "warmth". **False N-line:** being liked is others' `stance` (relational state), caring is a pursuit (`love`, `family`, `community`), and the rest is presence.
- **ATT.** Cutting either half loses 12–15 draws. Keeping both in one stat is the dominance defect (D&D Wisdom [FROM MEMORY]).

**E, scored last:** the eight have no orphan and no dominant stat; the nine have one orphan and a 29% dominant. More reads per stat, fewer stats.

## 2. Verdict on the nine

| | | |
|---|---|---|
| STR, END, ACU | **KEEP** | |
| AGI | **KEEP** | absorbs fine hand |
| WIL | **KEEP** | absorbs FOC and RES (as verbs-02 §II.4 advised) |
| CHA | **KEEP** | absorbs BON |
| FOC | **MERGE → WIL** | |
| BON | **MERGE → CHA** | knot cap becomes `CHA//2+1` |
| ATT | **SPLIT → PER + INS** | |
| TS | **not an attribute** | stays on `Person.thread_sensitivity` |

## 3. Recommended set: eight on 1–7, plus TS on its own 0–100 scale

| code | definition | code that reads it today | keys it would base |
|---|---|---|---|
| STR Strength | force a body puts out in a moment | combat impact, handling, bind, balance | labour (work, haul, mine, build) |
| END Endurance | what the body bears: exertion, road, hunger, harm | combat WI, health, stamina | fieldcraft (travel, forage, swim) |
| AGI Agility | speed, balance, precision of body and hand | combat tempo, reflex, balance | stealth; craft (forge, mint, heal) |
| ACU Acuity | reasoning, weighing evidence, reckoning | combat reading (2/3); command (1/3) | argue; inquiry (research, examine); reckoning (assess, tax, appraise) |
| PER Perception | noticing the world, keeping watch | combat reflex (1/3) | watch (surveil, search, track, scout, guard) |
| INS Insight | reading what another wants, fears or hides | combat reading (1/3) | insight (interview, interrogate, bargain, bribe) |
| WIL Will | composure and resolve under pressure | combat stamina, conc, disruption, poise; thread pool | thread (thread_read, weave, mend) |
| CHA Charisma | bearing that makes others attend, obey and like you | command (2/3); Face; knots | copying (tell, speak); command (march, rally) |

- **Smaller alternative: #505's six** (Body, Hand, Wit, Nerve, Presence, Sense; `proposals/2026-10-24-character-progression-adjudication.md:248`). Body folds STR and END, which combat reads separately, and collides with `Person.body`. Sense keeps the 29% dominance. Nerve is decision-side by #505's own §10.2.
- **Larger alternative: the eleven or the fourteen.** They add Recall (no reader), Fine hand (fits AGI), Nerve and Composure (chooser-side) and Warmth (stance plus pursuits). All new orphans.
- **The eight win:** every built reader keeps a source, with no orphan and no dominant stat.

## 4. `faculty(p, verb)` and `vocation_attribute` (shapes kept)

- **`faculty(p, verb)`** = `max(capability[k], attributes[vocation_attribute[k]])`, else `pool_default`, with `k = verb_capability[verb]` (CR-20). Attributes are the floor; #505's ceiling arm can compose on this later.
- **`vocation_attribute`** stays one attribute per key, and every key in §3 has exactly one natural base. Command's ACU third stays inside `derive_command` (module code).
- **Decision taken:** `inquiry` bases on ACU. `surveil` moves to `watch` → PER when the fieldwork verbs land, because its demand is *notice* (it shares `inquiry` today, CP-T01-01).
- **Opposition:** `_opposition_of` reads the subject's held key or the **same** attribute. This is the symmetric reading of ED-IN-0185 Q2, *"their corresponding score/2"*.
- **Modules take attributes at construction:**
  - Combatant: `strength`=STR, `agi`=AGI, `end`=END, `cog`=ACU, `spirit` and `focus`=WIL; `reflex` reads PER and `reading` reads INS.
  - Threadwork: `spirit`=WIL. Knots: `bonds` → CHA.

## 5. Touch list

1. **`references/descriptor_registry.yaml:24-53`.**
   - Delete `attr.mind.focus` (Focus becomes an alias of Will) and `attr.social.bonds` (Bonds, Sincerity and Affability become aliases of Charisma).
   - Replace `attr.social.attunement` with `attr.mind.perception` and `attr.social.insight` (Attunement a legacy alias of Insight).
   - Rewrite the count comment (`:26-31`) and the aggregate members (`:51-53`); the groups become 3 / 3 / 2. IN FLUX stays until Jordan rules.
2. **Re-derive, never hand-edit:** `references/names_index.yaml:75-84`, then `python tools/export_descriptors.py`, which writes `engine/engine_params/descriptors.json`; then `names.json`.
3. **`tests/valoria/test_descriptor_registry.py:19,21,33,39,43`.** These hard-code 9, 3 per category, `bonds` and the `agg.mind` members.
4. **CR-20** (`valoria_master_workplan_v10_part4.md:181-195`; `_part3.md:210`).
   - Nine keys become eight.
   - Delete "the pending tenth slot refuses a value": no slot exists, only a comment.
   - Correct LANDED ALREADY (`faculty` is unbuilt).
   - Add the §3 `vocation_attribute` rows.
5. **CR-33** (`:348-359`). The shape is unchanged; each lifepath key needs a `vocation_attribute` base, or "none".
6. **One ED-IN row**, numbered from `references/id_reservations.yaml` `next_free`. It supersedes ED-IN-0193's roster and closes J-T2.
7. **When combat first reads `Person`:** split `att` at `combat_systems.py:171-172` and in `combatant.py:93`. Re-tune the knot gate and cap at `knots.py:185,201`.
8. **Port** (`valoria-game`, read-only here). `resources/data_types/CharacterData.gd:14-23` already exports **ten legacy fields** (`cognition`, `recall`, `focus`, `bonds`, `spirit`, …) on 22 `.tres` files, despite the IN FLUX bar. Re-bind after the ruling, never before (ED-1050).

## 6. TS (J-T2) and "it will be 10 attributes"

- **J-T2 is irrelevant.** TS already has its own build-only carrier on its own 0–100 scale (`Person.thread_sensitivity`, `state/carriers.py:717`). Storing it again as `attributes['ts']` would be a second copy of a fact (§0.05 clause 3). The pending slot is deleted, not filled. TS stays the practitioner stat (ED-IN-0029) and enters `faculty` as an addend for the thread verbs.
- **"It will be 10" is ED-IN-0185**, 2026-08-14 (`editorial_ledger_in_archive.jsonl:137`).
  - Q7 asked only that the roster be *scheduled* as a workshop. The count came before any demand table existed, and the tenth was never named.
  - ED-IN-0301 confirmed nine keys "at the default", re-opening on his word, which he has now given.
  - Demand supports eight. Ten is reached only by keeping Bonds and counting TS.

## 7. Escalations

1. **The count.** Adopt eight attributes, with TS on its own carrier, overriding ED-IN-0185's ten. **Recommend yes.** If ten stands, keep Bonds and count TS, as verbs-02 did.
2. **Warmth vs presence.** One stat (recommended: being liked is others' stance, caring is a pursuit) or two (a beloved but unimposing person as a sheet fact). The two lead to materially different social games, and Bonds sits in his canon social triad.
3. **Who resists.** Opposition can read the same key (symmetric: a perceptive person resists being read) or a per-verb resisting attribute (Will resists threats and interrogation). **Recommend symmetric now**; the other option needs a resist column on `verb_capability`.
