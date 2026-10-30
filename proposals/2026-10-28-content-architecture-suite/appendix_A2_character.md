# A2 — The character: attributes, verbs, template, decision-making

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Appendix A2 of the suite, an analyst report copied from the session's `analysis/` into the suite at 07:10:35Z. Source: the session's own record of the analysis file written at 06:12:40Z (13,720 bytes; an independent `cat` at 06:45:53Z matches), recovered 2026-10-30 from the 2026-10-28 transcript (third pass). Edit-tool and heredoc changes found in the transcript were replayed in time order and the replayed size matches the size the session printed with `ls -la`. Text otherwise unchanged. Analyst reports are subagent output: figures in them are the analyst's, not verified here, and the suite's three-lens review (parts 07a to 07d, `critic_lens3.md`) found errors in some.

---
HEAD `be24c71` (B10-02 closed). Status: **BUILT** executes · **PLANNED** taken in adopted v10, unbuilt, revertible · **PROPOSED** held design · **NEW** this note.

## Verdicts
- **Q2:** Store **nine 1–7 attributes + Thread Sensitivity**. A verb never names an attribute: it names a **capability key**, and the key names one attribute. **Prowess := `faculty(p, verb)`**, the dice a person brings to a contested verb. This is the plan's shape (v10 M2, `workplans/valoria_master_workplan_v10_part6.md:33`; CR-20). None of it is built.
- **Precedent:** "attribute base + learned skill, capped" (Disco, Bannerlord) fits. The plan's `max(key, attribute)` kills training at the top; amend it to an additive excess (§2).
- **Q3:** A character is **one `Person` in four layers (capability, ambition, values, personality) on identity/position edges**. 13 fields BUILT; 2 fields + 2 tables PLANNED; personality PROPOSED (§3).
- **Decisions:** The engine chooses every act. The score reads values (pursuit × verb alignment) and stance toward the subject. It ignores capability, odds, goal text, scars and conviction (§6).

**Known state, checked:**
1. No verb carries an attribute: TRUE. `engine/season/verb_table.yaml` has 56 rows, no attribute field, 8 with `contests:`.
2. Prowess and aptitude are undefined: TRUE. DECIDED: prowess := faculty; "aptitude" retired, since it has three senses (`proposals/2026-10-16-attribute-derivation_aptitudes.md:8-14`).
3. The count: SETTLED at nine, tenth slot pending (ED-IN-0301, `registers/editorial_ledger_in.jsonl:87`).
4. `Person.attributes` is absent: TRUE (`engine/season/state/carriers.py:655-729`).
5. 15/7 vs 13 Convictions: the registry wins; the 13 are RETIRED (`references/descriptor_registry.yaml:224`). The live names are doctrine and stewardship, not the worksheet's faith/warden (ED-IN-0261 last row, `editorial_ledger_in.jsonl:50`).

## 1. Attributes and the verb→attribute rule
**VERDICT: yes**, nine suffice, and capability is one function of them.

**WHAT EXISTS:** The roster is BUILT data (`references/descriptor_registry.yaml:33-48`), with no importer in `engine/` (`engine/substrate/descriptors.py:50`). Every attribute reader is outside the season loop. In-loop, `seam/wrappers/sigma.py:119-131` gives everyone `pool_default=2` (`data/fixtures.py:414`).

**THE SET** (1–7; absent, never 0, when unauthored; readers are T2, outside the loop, unless marked):

| key | definition | reader / source |
|---|---|---|
| STR | force the body puts out at once | combat impact, handling |
| END | what the body bears: exertion, harm, recovery | health, stamina (`modules/combat/combatant.py:20-47`) |
| AGI | speed and balance of response | tempo, reflex |
| FOC | holding attention against disruption | concentration; weakest member |
| ACU | reasoning, weighing evidence, reckoning | combat reading; command (2nd term) |
| WIL | resolve and nerve; holding a course | thread pool `2·WIL`, knot roll |
| ATT | noticing; reading people | reflex/reading terms; AX-7 competence (PLANNED CR-19) |
| CHA | bearing and voice that make others attend | command (`modules/mass_battle/core/exchange.py:57`) |
| BON | capacity to hold ties | knot gate and cap `⌊BON/2⌋+1` |
| TS 0–100+ | perception of the threads (practitioner stat) | BUILT `Person.thread_sensitivity`, gate 30 |

The definitions are mine; names, scale and groups are the registry's.

**PROWESS:**
- `faculty(p, verb)`, with `k = verb_capability[verb]`.
- Base: `attributes[vocation_attribute[k]]`. Practice: `capability[k]` + practice arm. Fallback: `pool_default`.
- Opposition: the opposing score/2 as Ob (H-127).
- Pool dice only. Per J-13, "Capability supplies dice and gates nothing" (`engine/season/rosters.yaml:1208-1212`).

**RULE SHAPE** (data tables only; nothing on the verb row):
1. An attribute reaches a verb **only if the row declares `contests:`** (V-2). Uncontested verbs differ by remit, holdings and information.
2. Pool verbs: `verb_capability: verb → key` (BUILT: tell, speak → `copying`), then `vocation_attribute: key → {act, resist}`. PLANNED as `key → act`.
   - **NEW:** an optional `resist:` column, defaulting to `act`. A hearer resists a tell by reading people, not by presence.
3. Module verbs (fight, accept, march): the module's adapter maps the nine attributes onto its own fields. Multi-attribute demand lives in the module (CP-T03-03/-04, REM-32).
4. Gates are only own, remit, hold, presence and typed own-state (`decision/options.py:463-466`). **V-2a answered no** by that precedent.

| verb (lane) | contests | key | act / resist | status |
|---|---|---|---|---|
| fight (combat) | the body | module; arms practice | STR impact, AGI tempo, END durability, ACU+ATT reading, FOC concentration / same | module pool `max(5,History+6)` (ED-901). The seam derives only `end` from body (`seam/wrappers/combat.py:129-138`) |
| tell (social) | a standing | copying | CHA / ATT | key BUILT; attribute PLANNED; resist NEW |
| argue (social) | a proposition | argue | ACU / WIL | PLANNED (REM-30 adds the key) |
| determine (governance) | a proposition | none → `pool_default` (`verb_table.yaml:383`) | ACU / ACU | NEW: map it to `argue` |
| confer, issue, revoke (governance) | none | none | none | BUILT: remit eligibility; office adds no modifier |
| research, examine (fieldwork) | graded via `social_contest.roll` (`rosters.yaml:1141-1144`) | inquiry | ACU / concealer ACU | PLANNED (REM-30) |
| thread_read (threadwork) | none; TS ≥ 30 gate | none | WIL + ⌊TS/10⌋ | gate BUILT (`verb_table.yaml:1530`); pool T2 (`systems/threadwork/sim/operations.py:235-247`); PLANNED adapter CP-T07-02 |
| march (faction) | a field | module; commander | `round((2·CHA+ACU)/3)` / rival commander | season command fixed at 4 (`modules/mass_battle/massbattle.py:183`); PLANNED REM-32 |

## 2. Precedent: base scores, skills, aptitudes, histories
**VERDICT:** take "attribute base + learned skill, capped". Histories only seed state.

| way | example | fit (d10 pool, σ layer) |
|---|---|---|
| A. attributes with skills under them; attribute sets start and cap | Disco: 4×6, the attribute sets the skill's start and cap (digest D7a `T05:12-13`); Bannerlord: 6 attributes, 18 skills, learning limit from the attribute (`T02:8,:74`) | **best**: one monotone quantity per verb |
| B. point-buy + class/background, levels | BG3 (digest D6a `R4:79`) | no: classes and levels break "same rules for all" in a closed cast (ED-WR-0011) |
| C. skills by use, traits | KCD (`R4:122-123`); CK3 five skills + ~306 traits (`R1:20,:70`) | partial: use-growth = CR-18 practice; traits = the personality layer, not the pool |
| D. lifepath grants skills/stats | Burning Wheel, Traveller [FROM MEMORY]; Bannerlord backgrounds; archived `character_histories_v30.md` | yes, **as a creation template only** (CR-33) |
| E. attribute + skill both summed in full | World of Darkness, Shadowrun [FROM MEMORY]; archived Argue `(Primary×2)+History` | no: doubles magnitudes toward σ saturation [CONFIDENCE: medium — not diagnosed] |

**DECISION TAKEN:** amend CR-20's `max(key, attribute)` to `faculty = attribute + min(cap, max(0, key − pool_default)) + practice_addend`.
- Under `max`, training is invisible for anyone talented, since keys sit near 2–4 and attributes run to 7. That is an S defect (one of two routes dead) and an R loss.
- The amendment keeps CR-20's falsifier (unkeyed attributes 2 and 6 roll 2 and 6) and CR-33's "a grant at `pool_default` changes no pool".
- It is way A, not E: only the trained excess adds, and it is capped.
- Revert: `max`.

## 3. The character template (four layers)
**VERDICT:** a closed list of about 20 fields. Most are BUILT; the person-varying ones are empty (`capability` is empty on 83 of 83 persons).

| group | field | status |
|---|---|---|
| identity / position | `id`, `name` (no outcome reader), `weight` (a cohort at >1), `born` (age is a query) | BUILT |
| | `heritage` (5-member roster) | PLANNED CR-30 |
| | `tenures`: office = hold, faction = commit to a creed, home = reside, oath = oblige, ties = tie/knot | BUILT; faction and office are derived |
| **1 capability** (resolver only) | `attributes` (nine) | PLANNED CR-20 |
| | `capability` keys + `train` | BUILT, empty |
| | lifepath expansion; live practice | PLANNED CR-33, CR-18 |
| | `thread_sensitivity`, `body` | BUILT |
| | kit | GAP (J-T5). TAKE: a hold Tenure on an item, by the seat precedent |
| **2 ambition** (which questions exist) | commits to OUGHTs (`queries/world_q.py:2168`), seeded by `goals.yaml` | BUILT |
| | `want` text in `npcs.yaml` | BUILT, no reader |
| | thrust ladder | PROPOSED (CL-THRUST) |
| **3 values** (which option wins) | `pursuits` (15), `stance` | BUILT, scored |
| | `conviction` (5 affiliations, 0–5) | BUILT, inert at weight 0 |
| | `scar` | BUILT, inert at shift 0 |
| **4 personality** (manner) | offsets on rigid_flexible, grandiose_humble, deontological_instrumental (spread 0.15) | PROPOSED (`proposals/2026-10-24-character-layers-…md` §4) |
| knowledge / transient | `ledger` (the View), `travel_leg` | BUILT |
| [RETIRED] | `marks`, `beliefs`, `orient`/Self-Other (ED-IN-0261), 13 Convictions, Resonant Style, Truth (now Conviction, ED-IN-0251) | — |

**DECISION TAKEN:** build `personality` behind a spread-0 control.
- It is the only layer that separates persons sharing a faction and an office, which answers "too many similar stories".
- Its falsifier: spread 0 leaves `content_hash` equal.
- Revert: drop the field.

## 4. Histories / lifepath
**VERDICT:** a history grants **starting state**. It is never stored: its id lives on the cast row (CR-33).
- **PLANNED (CR-33):** 34 vocation rows in `rosters.yaml: lifepath_templates` expand into `capability` keys at `pool_default`. Archived dice magnitudes are cut.
- **NEW — all four stages, one table row each:**
  - **origin** → `heritage` + a conviction intensity (replaces the archived Truth modifiers);
  - **formation** → keys + a pursuit tilt;
  - **vocation** → keys;
  - **catalyst** → one authored OUGHT commit with a ladder (CL-THRUST), plus `tie` Tenures for its Knots.
- Every magnitude needs a `source:`.
- **The catalyst is the freestanding-storyline hook:** a want not derived from office or faction. Outcomes are still written by persons choosing.
- [GAP: the content (46 cast lifepaths) is Jordan's (`workplans/valoria_master_workplan_v10.md:129`).]

## 5. Progression
**VERDICT:** practice moves, values erode, the body wears; attributes are set at creation.

**Ruled or taken:**
- `train` +1 on a held key (BUILT, `loop/effects_combat.py:421-446`).
- Practice: recent good results add dice, windowed and capped (PLANNED CR-18).
- Technique efficacy comes from invested level (ED-PC-0023).
- Pursuit shift 0.1 on a judgement (BUILT, `loop/effects_information.py:550,580`).
- Scars at 1/2/3 = destabilise / weight shift / crisis (ED-IN-0261, `queries/person_q.py:468-469`); the terminal branch was folded in by RS-1 (ED-IN-0291).
- Conviction is written at resolve (`loop/resolve.py:706`).
- Injuries move the body; ageing and illness ship at 0.

**Proposed (NEW):**
- Attributes change only by age band (body triad) and permanent wound, never by use. This follows Jordan's views 2 and 3 (`proposals/2026-10-24-character-progression-adjudication.md:61-67`). Inert until `age_step` is switched on.
- No mechanical player exceptionality.

## 6. How a character chooses (code first)
1. **Question:** `questions_for` (`queries/world_q.py:2717`). Sources are `claim_landed` and `need` (a live commit to an OUGHT), plus five standing occasions, ordered by `attention_key`. The rule `first` takes the head (`decision/questions.py:62`).
2. **View:** ≤12 own-ledger claim ids (AX-2).
3. **Budget:** `5 + offices − body bands − travel legs`, min 1 (`decision/budget.py:55-61`).
4. **Options:** `opening_set` takes the 56 rows and drops any that is withheld, fails own/remit/hold/presence or TS ≥ 30, or has no referent. The refusal gate is dormant.
5. **Score:** `Σ axis_w·align(verb,axis) + 2·stance_toward(subject) + urgency` (urgency is equal for all; `decision/choose.py:130-151`). **Values pick the verb, stance picks the target, the question picks the matter.**
6. **Draw:** Plackett-Luce over softmax at τ = 0.1; scenes packed greedily into the budget; one released per round. An empty set returns `[]` silently.

- **Who chooses:** the engine chooses everything. A player replaces the WHOLE chooser via `dispatching_chooser` (`harness/play_surface.py:41`); it has no caller outside tests.
- **Stored but unused by a choice:**
  - capability and attributes: there is no odds term. PLANNED CR-17 weights alignment by believed odds.
  - `name`, `born`, `weight`;
  - `scar` and `conviction` (gains 0);
  - goal and want text.
- **Departs from:**
  - `npc_behavior_v30` (archived): deterministic priority tree, Framework Ob modifiers, GM crisis table, Self-Other, "Stability ≤2" override [RETIRED];
  - `conviction_track_v1`: its d6 crisis table is absent;
  - the four-layers doc: personality unbuilt; CR-17 narrows its "never a chooser term";
  - the thrust ladders: unbuilt.

## Escalations
1. **J-T2, the tenth attribute.** TS satisfies "it will be 10 attributes" (`editorial_ledger_in_archive.jsonl:137`) with a field that already has readers, at the cost of a second scale. Nine would overwrite that ruling. I recommend TS.
2. **Practice and attributes: `max` vs additive excess.** `max` lets talent dominate and hides training; the excess makes trained talents exceptional, so the two give different games at the top. I recommend the excess (§2).
