# P2 · Attributes, skills, histories: three packages

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Part 03 of the suite. Base: `rd_070811_P2_attributes_skills_histories.md` (the session's read at 07:08:11, line numbers stripped; identical to `clean_rd_070811_P2_attributes_skills_histories.md`). Replayed in time order, all applied: `heredoc_070834`, `heredoc_072636`, `heredoc_072706` (its part-03 edit), `heredoc_072811`. `heredoc_072726` disables its part-03 edit, consistent with `072706` having applied it. None failed. No later full read of this part exists, so the result could not be checked against one. The suite was written in a session of 2026-10-28 that committed nothing; its files existed only in that session's scratchpad. This directory is a reconstruction from the session transcript's surviving reads and patch scripts, not the original files. Recovered in a second pass (2026-10-30), each with its own provenance: parts 05 and 07a to 07d, and the lens-3 (directive-compliance) critic report (`critic_lens3.md`). Still not recovered: part 06 and appendices A1 to A5 (see `00_INDEX.md`). Edits the session made by tools other than Bash heredocs (Edit-tool calls) were not captured, so the text may differ from the session's final file in ways not recorded here. Where this text and the tree disagree, the tree wins; every figure and line citation is as of the session's HEAD (`ttrpg` be24c71) and is unre-verified.

---

*Part 03 of the review suite. Corrected after adjudication (07a to 07d); the ED-IN-0185 and registry quotations below were re-checked at source.*
HEAD `be24c71`. Proposals; nothing built or ruled. Drafted values carry `[ASSUMPTION; medium; Jordan to correct; revert: delete the cell]`.

**Verdict.** All three share the verb rule, the skill keys, a four-stage lifepath, the troop and kit templates and the TS writer (§1). They differ in what a stored score *does*. **Recommended: P2-A amended, with P2-B's Perception/Insight split held until the fieldwork verbs are built** (§6).

**In plain words.**
- An **attribute** is what a person *is*: strength, wit, presence. It is written once and moves only with age or a lasting wound.
- A **skill** is what he has *learned*: arguing, searching an archive, commanding. Training raises it, and each skill stands on one attribute.
- A **history** is *how he got here*: birthplace, schooling, trade, and the event that changed everything. It is read once, at world-build, to hand out starting skills, ties and one want of his own. After that, his history is what he did.

Attributes and skills set the dice; a history never does. A **verb** is an act the game resolves, and a **field** is a value on the sheet.

| item | P2-A · Plan, amended | P2-B · Demand eight | P2-C · Six as ceilings |
|---|---|---|---|
| base scores | 9 + TS named the tenth, on its own field | 8 (FOC→WIL, BON→CHA, ATT→PER+INS); TS off-roster | 6 (Frame Hand Wit Will Presence Sense), 1–5 |
| what a score does | dice: `attr + min(3, key−2) + practice` | as A | a floor and a ceiling on a key; never dice |
| progression | practice live (CR-18) and `train`; attributes move by age and wound | as A | `train`, a decisive-result write and decay; attributes fixed |
| history stored | 4 stage ids on the cast row only | as A | as A, plus the recorded ledger, scar and tenures |
| rulings overridden | none, but it reopens the tenth-attribute default confirmed in ED-IN-0301 (J-T2 asks for a yes) and amends M2 | ED-IN-0185's count | ED-IN-0185, J-13 (iii), Jordan's view 3 |
| instance cells (46 cast; design estimates) | 956 | 910 | 818 |
| arcs this area unlocks | family G (12) | G | G |

## 1. Common to all three

**The verb rule.** A verb row never names an attribute.
- **A contested row** (it declares `contests:`) maps `verb_capability: verb → key`; `key_base: key → {act, resist}` gives the attribute. `resist` defaults to `act`, which is ED-IN-0185 Q2's *"their corresponding score/2"*.
  - The obstacle is the opposing faculty/2, plus or minus a per-person modifier (Q2's *"(score/2)+x"*).
- **Module verbs** (`fight`, `accept`, `march`) map scores in the module's own adapter.
- **The other 45 of 56 rows** read no person quantity: `verb_table.yaml:33-35` says eligibility never gates on capability, and the count is derived (8 rows with `contests:` plus 3 graded inquiries, `rosters.yaml:1143-1145`).
- ⚠ CR-20's "LANDED ALREADY: `faculty`" is false at HEAD [NULL: `grep -rn "def faculty" engine modules`].

**Skill keys (14)**, of which only `copying` exists (`rosters.yaml:1232-1233`): `copying`, `argue`, `inquiry`, `lore`, `watch`, `insight`, `stealth`, `reckoning`, `command`, `arms:<family>`, `craft`, `labour`, `fieldcraft`, `thread`.
- **Threadwork:** `thread`, with TS added behind the built gate of 30.
- **Fieldwork:** `inquiry`, `watch`, `stealth`, `lore`.
- **Governance:** `argue` and `reckoning`.
- **Combat:** `arms` is weapon proficiency and feeds `Combatant.history` (`core.py:51-56`). Techniques stay `equipped` levels (ED-PC-0023), and the tradition is a person field, `school`, read by `familiarity` (`traditions.py:42`).

**"Aptitude" is retired.** Its three senses (`attribute-derivation.md:64-68`) become **skill key**, **base**, and **cap** (A, B) or **ceiling** (C). **Traits** are the personality layer: three offsets that set manner, never odds.

**Lifepath.** One row per stage option in `rosters.yaml: lifepath_templates`, extending CR-33's 34 vocations. A magnitude needs a `source:`, so the archived +1D values are cut.

| stage | grants | Klapp [ASSUMPTION] |
|---|---|---|
| origin (8) | `heritage`, conviction intensities, a TS seed if sourced | 1E Himmelenger Child: `central_einhir`, orthodoxy 4 |
| formation (7) | keys, a pursuit tilt | 2G Monastic Seclusion: `lore` |
| vocation (34) | 2 keys | 3-CH4 Church Archivist: `inquiry`, `lore` |
| catalyst (7+1) | one OUGHT commit with a `goal_stages` ladder (M20(b)), `tie` tenures, an optional scar | **4H Keeper of the Sealed Shelves** (NEW) |

**Klapp's catalyst as the hook.**
- **His want:** "the sealed texts are kept and read", from scholastics, his top pursuit at 0.35 (`npc_registry.yaml:1037`).
- **His own act raises his TS.** Each `research` of a Thread-significant Record adds a canon-sourced step through the one TS writer (part 02 §1; +1 is illustrative).
- **The seated person sees it first** (for example a Riskbreaker at the cathedral, if the player is seated there). Klapp starts at TS 12 `[ASSUMPTION; medium; Jordan to correct; his registry value is null, a [GAP], at npc_registry.yaml:1032]`, and co-located witnesses (Haelgrund among them) hold claims on his handling of the texts.
- **The player chooses:** `tell` Klapp, `tell` Haelgrund (→ `determine` → `ban`), or `conceal`.
- **How it ends.** At TS 30, `thread_read` opens to Klapp. Persons write every outcome.

**Troops and kit.** The troop stock (M3 A: a stored count by type under a commander; grade, discipline and morale read as queries) and the kit template (slots, weapons from physics, proficiency as practice keys; carrier decided by ruling 4) are specified once, in part 02 §1. Orders cost no scene budget and the delegate's faculty decides where another person carries the order out (part 01 §13).

## 2. Eight worked verbs (act / resist base)

| verb (lane) | key | A | B | C (the ceiling's base) |
|---|---|---|---|---|
| fight (combat) | arms | module: STR AGI END ACU ATT FOC WIL | as A, ATT split: reflex PER, reading INS | Frame Hand Wit Sense Will |
| tell (social) | copying | CHA / ATT | CHA / INS | Presence / Sense |
| argue (social) | argue | ACU / WIL | ACU / WIL | Wit / Will |
| research (fieldwork) | inquiry | ACU / ACU | ACU / ACU | Wit / Wit |
| surveil (fieldwork) | watch | ATT / AGI | PER / AGI | Sense / Hand |
| thread_read (threadwork) | thread | WIL + ⌊TS/10⌋, gate 30 | as A | Will + ⌊TS/10⌋ |
| determine (governance) | argue | ACU / ACU | ACU / ACU | Wit / Wit |
| march (faction) | command | module: Command is derived from Charisma and Cognition, clamped 1–7 (`core/exchange.py:55-64`); under the pool-quality model it does not enter the pool, and the code has no key-excess term (a `command` key's excess would be NEW) | as A | key, capped by Presence |

## 3. P2-A · The adopted plan, amended

**Premise.** Keep v10 M2's shape: nine stored scores, `faculty` through the pool only, live practice, lifepath templates. Make A2's and A6's corrections, and name TS the tenth.

**Specifies.** Scale 1–7, absent when unauthored. "Primary in" counts the moments where the score is the main input, in A6's 104-moment demand matrix.

| key | definition | primary in | base of |
|---|---|---|---|
| STR | force in a moment | 10 | labour |
| END | what the body bears | 11 | fieldcraft |
| AGI | speed, balance, fine hand | 15 (+7 stealth) | stealth, craft |
| FOC | holding attention | 1 | (combat concentration) |
| ACU | reasoning | 21 | argue, inquiry, lore, reckoning |
| WIL | resolve under pressure | 9 | thread |
| ATT | noticing; reading people | 27 | watch, insight |
| CHA | bearing others obey | 17 | copying, command |
| BON | holding ties | 7 | (knot gate, `knots.py:185`) |
| TS | perceiving the threads, 0–100 | 11 | addend on `thread` |

- **Faculty** = `attr[base] + min(3, max(0, key − pool_default)) + practice`. It replaces CR-20's `max`, under which training is invisible in anyone talented. Unkeyed attributes of 2 and 6 still roll 2 and 6.
- **TS's registry row** points at `Person.thread_sensitivity` (`carriers.py:717`), so no second copy exists.

**Resolves.** M2 kept. J-T2: TS. J-T4: age band and permanent wound, inert until `age_step` is on (Jordan's view 3, #505 §1).

**Rulings.** J-T2, a yes to TS (else the pending slot); the M2 amendment, additive excess (NEW; revert `max`); M3; J-T5.

**Plan.**
- **CR-20:** correct LANDED ALREADY, build `faculty`, add 14 `key_base` rows.
- **CR-33:** add stages 1, 2 and 4.
- **CL-ATTR:** the TS writer.

**Cells.** 46 × 21 (10 scores, 4 stage ids, 3 personality offsets, 3 kit slots, `born`) − 10 sourced TS (the registry authors 10 `ts:` rows, `npc_registry.yaml`) = **956**, plus 56 stage rows and 14 base rows. Agents draft them all.

**Arcs.** Family G (2 9 26 28 29 30 32 35 39 41 51 54) needs TS on persons with readers, the TS writer and a pooled `thread_read` (CP-T07-02). Coherence on persons stays a [GAP].

**Risks.** FOC stays an orphan; ATT drives 29% of the designed draws; the sheet carries two scales; top pools reach 12 dice, so run `resolution-diagnostic`.

**Falsifier.** Attribute 6 with key 5 rolls 9; a planted `max` makes it 6. **Control:** an all-absent realm at `practice_cap 0` keeps `content_hash`.

**Precedent.** Disco Elysium: the attribute sets a skill's start and cap (D7a T05:12-13). Koei: officer stats decide domestic work (T13:50). JA2: Leadership gates training (T14:26-41).

## 4. P2-B · Demand-derived eight, TS on its own field

**Premise.** Carry only the scores the verbs demand: A6's eight, with A's formula, keys and progression. TS stays a practitioner stat; the pending tenth slot is deleted.

**Specifies.** Eight scores; the figure after each is its "primary in" count (§3):
- STR 10, END 11, AGI 22, ACU 21;
- **PER**, noticing the world, 15;
- **INS**, reading what another wants or hides, 12;
- **WIL**, absorbing FOC, 10;
- **CHA**, absorbing BON, 24.

`watch` stands on PER and `insight` on INS. The knot cap becomes `CHA//2+1`.

**What each override costs.**
1. **ED-IN-0185 Q7.** Jordan's verbatim *"it will be 10 attributes"*, in an entry marked *"THE AGENDA IS CLOSED; DO NOT RE-RAISE IT"*. The registry also says *"THE COUNT IS RULED"* (`descriptor_registry.yaml:27`), so the override needs his explicit word. A6 reads Q7 as asking only for a workshop; the verbatim row says otherwise.
2. **ED-IN-0301's nine-key default.** It re-opens on his word; low cost.
3. **His social triad and the aggregates** (`:44-53`). Both are rewritten, and ED-IN-0193 is superseded.
4. **Knots.** More persons form them wherever CHA is above BON.
5. **Edits.** Five test lines and the Godot re-bind.

**Resolves.** J-T2 closes as irrelevant. Warmth (A6 escalation 2) is one score: being liked is others' `stance`.

**Rulings.** The ED-IN-0185 override (it overwrites ratified canon), M3 and J-T5.

**Plan.** As A; one ED-IN row (`next_free`); CR-19 reads INS.

**Cells.** 46 × 20 − 10 = **910**.

**Arcs.** G (12): it needs TS with readers, not TS in the count.

**Risks.** INS is the main input of none of the 21 built and module moments; the split bets on PROPOSED lexicons; CHA becomes the broad score (23%, 6 subsystems).

**Falsifier.** Re-run the matrix once REM-30 and the fieldwork verbs land: if PER or INS is the main input of fewer than 5 built verbs, the split was wrong. **Control:** an all-absent realm keeps the hash.

**Precedent.** Disco Elysium: 4 attributes × 6 skills (D6a R4:12). Warband: STR AGI INT CHA (D7a T02:89). D&D Wisdom as the broad stat [FROM MEMORY].

**What the built evidence does and does not separate** (a re-run of A6's matrix, `scratchpad/p2/probe.py` over its `matrix.py`).
1. **The dominance case rests on designed verbs.** On the 11 built or 21 built-and-module moments, ACU dominates every set at 55%. ATT's 29% exists only in the 83 lexicon draws.
2. **A6 contradicts itself on combat's `reading`.** Its matrix codes it as *notice* (PER); its module map sends it to INS.
3. **A ten-score variant passes A6's own tests and overrides nothing.** Split ATT, fold FOC into WIL, keep BON, and count TS. No score is orphaned (minimum 7) and the largest share is 22%, which fixes P2-A's two stated risks (FOC an orphan, ATT 29%). It is a named option in ruling 2 (part 01 §11) as **B-10**, and it is B's cheap revert.

## 5. P2-C · Few stored scores, a thick skill and history layer

**Premise.** Scores are innate limits: how far a person can go, and what he rolls untrained. Skills are the only dice. It is #505 run on the real verbs, with two names fixed.

**Specifies.** Six scores, 1–5, fixed. The figure after each is its "primary in" count (§3):
- **Frame**, force and toughness, 17. Renamed from Body, which collides with `Person.body`.
- **Hand**, quickness and fine hand, 22.
- **Wit**, reasoning and attention, 21.
- **Will**, composure and resolve, 10: *how well*, never *whether*.
- **Presence**, bearing and warmth, 24.
- **Sense**, noticing and reading people, 27.

Further rules:
- **Nerve becomes Will.** Jordan reads Composure and Nerve as one trait (#505 §10.3). Daring is the chooser's business, and the chooser has no risk term (`choose.py:149-151`), so daring is a [GAP], not a score.
- **The rule:**
  - floor = `max(1, attr−1)`; ceiling = `2·attr`; pool = `max(floor, key)`;
  - an unauthored score reads 3, so its floor is 2, today's `pool_default`.
- **Combat:** `arms` → `history`; Frame → `strength` and `end` (with the body bands); Hand → `agi`; Wit → `cog`; Sense → `att`; Will → `spirit` and `focus`.
- **One ladder.** `train` +1; a full success +1, at most once per key per season; −1 after 4 idle seasons [ASSUMPTION], never below the floor. CR-18's windowed arm is cut.
- **Office eligibility stays free of capability** (`verb_table.yaml:33`), so #505 §4.8 is dropped.

**Resolves.** J-T1: stored. J-T2: no tenth. J-T4: never. J-13 (iii): a key may be minted, since it cannot fall below the floor.

**Rulings.** ED-IN-0185; J-13 (iii); view 3; M3; J-T5.

**Plan.** Replace CR-18; rewrite CR-20 for six. NEW: the decisive-result writer with decay. NEW: combat's ladder onto `arms` (#505 C-4).

**Cells.** 46 × 18 − 10 = **818**, plus 2 tuning values for Jordan.

**Arcs.** G (12).

**Risks.** Frame loses the glass-cannon versus tank distinction (combat reads `strength` 17 times, `end` 6); re-rooting combat's ladder is the largest change here; decay moves every hash.

**Falsifier.** At least 90% of keys at ceiling after 20 seasons: cut the ceiling. The median key moving more than once a season: the gate is loose. **Control:** an all-absent realm keeps the hash.

**Precedent.** Bannerlord: the learning limit from attribute and focus (D7a T02:74). CK3: five skills plus traits (D6a R1:20, :70). GURPS: untrained rolls default to the attribute [FROM MEMORY].

## 6. Worked sheets, migration, recommendation

**Klapp** (NPC-039, Cardinal of Temperance, `offices.yaml:424`). All values [ASSUMPTION].

| | scores | draws |
|---|---|---|
| A | STR 2 END 3 AGI 2 FOC 6 ACU 6 WIL 4 ATT 4 CHA 4 BON 3; TS 12 | research 6, tell 4 |
| B | STR 2 END 3 AGI 2 ACU 6 PER 5 INS 3 WIL 6 CHA 4; TS 12 | research 6, tell 4 |
| C | Frame 2 Hand 2 Wit 5 Will 4 Presence 3 Sense 3; TS 12 | inquiry ceiling 10, floor 4 |

All three sheets hold keys `lore` and `inquiry`, school `none`, and catalyst 4H.

**Lord Steward Gerik Strand** (NPC-009, `offices.yaml:338`).
- **Lifepath:** 1A, 2B (`reckoning`), 3-CR1 (`argue`, `insight`), 4D-i.
- **Commit:** wanting efficient Crown administration and personal indispensability (`npc_registry.yaml:404` goals: "Efficient Crown administration", "Maintain personal indispensability"; the phrasing here is a paraphrase).
- **Scores:** A: STR 3 END 5 AGI 3 FOC 6 ACU 5 WIL 5 ATT 4 CHA 4 BON 2. C: Frame 3 Hand 3 Wit 4 Will 4 Presence 3 Sense 3.
- **Flattery** (`:405`) becomes a resist modifier: `(score/2) − 1` on a `tell` or `argue` that praises his competence.
- **As a delegate,** his `reckoning` decides the assessments and `requisition`s ordered through him.

**Migration.**

| surface | A | B | C |
|---|---|---|---|
| `descriptor_registry.yaml:33-48` | + a TS row with its own carrier | −focus, −bonds; attunement becomes perception and insight | 6 rows, scale 1–5 |
| CR positions | 20, 33 | 19, 20, 33 | 18 cut; 20, 33 |
| `CharacterData.gd:14-23` (10 legacy fields) | cognition→acuity, spirit→will; −recall | −recall, −focus, −bonds; +perception, +insight | 6 fields |
| tests | `faculty`; registry test +1 | `test_descriptor_registry.py:19,21,33,39,43` | as B, + decay and ceiling tests |

The 15-name pursuit roster is unchanged. Godot re-binds after the ruling (ED-1050).

**Recommendation: P2-A amended.**
- It keeps the plan's count, which is a default and not a finding: the built evidence cannot separate the sets (§4). It reopens ED-IN-0301's tenth-attribute default (J-T2 = TS) and asks one amendment (additive excess). B-10 is the alternative to weigh against it.
- Keeping FOC and BON costs two cells per person, and both have module readers.
- B's split becomes a B-10 roster change once PER and INS have built readers.
- C models a life best and costs most: three overrides and a re-rooted combat ladder.

**Common to all three:** everything in §1 and the shape of §2.
