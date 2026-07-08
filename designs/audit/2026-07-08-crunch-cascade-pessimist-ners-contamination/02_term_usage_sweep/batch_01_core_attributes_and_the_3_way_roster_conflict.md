# Term Usage Sweep — Batch 1: Core Attributes and the 3-way roster conflict

# Batch 1 Audit — Core Attributes and the 3-Way Roster Conflict

**Method note on scope.** Each grep below was run against the full working tree (2,370 tracked files). For terms returning 100–250 matching files, I opened every canonical/registry/generated/code site individually (these are the ones the classification step actually turns on) and sampled the remaining bulk — mostly `tests/sim/*.md` (frozen historical sim-run reports), `designs/audit/*.md` (dated audit folders), and `archives/`/`deprecated/` — enough to confirm they use period-appropriate terminology consistently; I did not open every one of the ~150–250 files per term line-by-line. Where I sampled rather than exhaustively opened, I say so and give the files I actually opened.

---

## 0. Foundational finding, applicable to all ten items below

Three files were named as the batch's canonical anchors. Reading all three directly, firsthand:

- **`references/glossary.md` Part One "Core Attributes" table, lines 33–41**: **7 attributes** — Agility, Attunement, Cognition, Endurance, Presence, Spirit, Strength. The table itself carries a banner (line 31): *"⚠️ IN FLUX (ED-IN-0025, 2026-07-07, C-VERIFY-19/21): this 7-attribute roster conflicts with `references/descriptor_registry.yaml`'s 9-attribute roster... Neither file defers to the other... Do not treat either table as settled."*
- **`references/descriptor_registry.yaml` `attributes:` block, lines 30–44**: **9 attributes** — body: Strength, Endurance, Agility; mind: Focus, Acuity (aliases: Reasoning, Cognition), Will (alias: Spirit); social: Attunement, Charisma (aliases: Influence, Presence), Bonds (aliases: Sincerity, Affability).
- **`params/core.md` `## Attributes` section, lines 137–145**: a **third, distinct count of 10** — "Point pool at creation: 31 points across 10 attributes" (line 138), and the table lists Physical (Agility, Endurance, Strength), Mental (Cognition, **Recall**, Focus), Social (Attunement, Bonds, Charisma), Metaphysical (Spirit) = 3+3+3+1 = **10**.

So the roster count is not a two-way 7-vs-9 conflict as the glossary's own banner describes — it is a **three-way** conflict: 7 / 9 / 10, and the third file (`params/core.md`) is not even reconcilable with the other two by simple aliasing, because it contains **Recall**, a term absent from both the glossary's 7 and the descriptor registry's 9. This is addressed in full in §10 below.

Also foundational: `references/names_index.yaml` (lines 45–53) declares itself a **mirror** of `descriptor_registry.yaml`'s 9-attribute roster (enforce: warn), and `references/alias_registry.yaml`'s `core_attributes:` block (lines 26–61) independently restates the **glossary's 7**, with zero awareness of Focus/Bonds/Acuity/Will as attributes (it files Focus under a separate `derived_stats:` block, line 89, range "1-5+" — the glossary's superseded framing, not the attribute framing). So there are, in inventory, **four** files that each assert an authoritative attribute roster (glossary, descriptor_registry, params/core.md, alias_registry), and they do not all agree with each other pairwise, let alone as a set.

---

## 1. Agility

**Home definition.** No single home. Two competing definitions exist:
- `references/glossary.md:35`: `Agility | — | 1–7 | Physical speed and coordination. Combat pool base.`
- `references/descriptor_registry.yaml:36`: `{key: attr.body.agility, name: Agility, aliases: [Dexterity]}`, scale "1-7" (line 31).
- `params/core.md:142`: Physical group member, no dedicated prose paragraph.

Range (1–7) agrees everywhere. The *description* — "Combat pool base" — is **stale and wrong** relative to current canon (see divergence below).

**Usage sweep.** 189 files match `Agility` repo-wide. Canonical/live sites opened: `references/glossary.md:35`, `references/descriptor_registry.yaml:36`, `references/alias_registry.yaml:28-30`, `references/names_index.yaml:47`, `params/core.md:142`, `designs/scene/combat_engine_v1/config.py` (no literal "Agility" string — used only as a physics input via `AGI_TEMPO_K` comment, config.py:54), `designs/scene/combat_design_v1.md` (multiple, e.g. lines 33-34, 70, 102-108, 437, 442 — legacy doc), `designs/scene/combat_v30.md` (PARTIALLY SUPERSEDED per CLAUDE.md), `sim/personal/combat.py:5,46` (DEPRECATED module, still imported live — see below), `references/mechanical_terms_index.md:79,95-97` (non-canonical PROPOSAL doc). Bulk sampled: `tests/sim/*.md` (~90 files, mostly pre-2026-05-29 R1 sim logs using the old Agility×2 formula, era-consistent with when they were written), `designs/audit/**` (~50 files, mostly combat-recovery/reframe audit folders discussing the Agility-pool-dominance defect that led to its removal).

**Divergence check.**
1. **"Combat pool base" is false as of the current canonical combat engine.** `params/core.md:161` (Derived Scores table): *"Combat Pool | max(5, Relevant History + 6) | min 5 | **Agility-INDEPENDENT** resolution pool — ratified 2026-05-29 R1 (ED-901; re-ratified ED-900/904...). Supersedes the struck (Agility × 2) + History + 3 form..."* Same in `designs/scene/derived_stats_v30.md:584` and `designs/scene/combat_design_v1.md:33-34`: *"`(Agility × 2) + Relevant History + 3` was STRUCK by the 2026-05-29 R1 ratification (ED-901...) — the resolution pool is Agility-independent."* Yet `references/glossary.md:35` and `references/mechanical_terms_index.md:79` (*"Agility | — | 1–7 | Physical speed and coordination. Base for Combat Pool."*) both still describe Agility as the Combat Pool base, with no update since the rename. Glossary's own header (line 3) says it was "last swept 2026-04-30" — before the 2026-05-29 R1 change — so this is a dateable staleness, not an ambiguity.
2. **`sim/personal/combat.py`** is explicitly headed `[DEPRECATED 2026-06-23 — superseded by combat_engine_v1]` (line 4) and states its formula is the old one (line 46: `# [canonical: combat_v30 §1 — "Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)"]`) — yet it is **still imported live**: `sim/cross_scale/scene_dispatch.py:96`: `import sim.personal.combat as combat`. The deprecation banner has not been backed by removing the live import.
3. Agility's actual current mechanical role — a σ-leverage **tempo/initiative** input, not a pool driver — is stated correctly only in the current combat engine: `designs/scene/combat_engine_v1/config.py:54` (`AGI_TEMPO_K=0.03 ... # athleticism adds a little cadence`) and `combat_design_v1.md:70` (initiative tiebreaker).

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/descriptor_registry.yaml:36` | CANONICAL DEFINITION (roster membership + range) | Named home for the attribute roster itself | Range agrees (1–7); has no formula claim to be stale |
| `references/glossary.md:35` | HARDCODED DUPLICATE | Independent prose restating range + role, no import mechanism | Range agrees; **role description ("Combat pool base") has drifted** — stale since 2026-05-29 R1 |
| `params/core.md:142` (table) | HARDCODED DUPLICATE (of roster membership) | Independent listing, 10-attribute frame | Range agrees; roster-membership frame itself conflicts with the other two (see §10) |
| `references/alias_registry.yaml:28-30` | HARDCODED DUPLICATE | Independent `core_attributes.agility` entry, no reference back to descriptor_registry or glossary | Range agrees; no role claim to drift |
| `references/names_index.yaml:47` | PULLED / REFERENCED | Explicit "MIRROR" of `descriptor_registry.yaml attributes` per file header (lines 28-29); `tools/ci_names_consistency.py` is the enforcement mechanism named in the header | Agrees (mirrors registry) |
| `tools/observability/lexicon_data.js` / `lexicon.json` | PULLED / REFERENCED | `// AUTO-GENERATED — do not hand-edit`; `generated_from` array lists `alias_registry.yaml`, `descriptor_registry.yaml`, `glossary.md` etc.; built by `tools/observability/build_lexicon.py` | Agrees with whatever its listed sources say (inherits their internal disagreement) |
| `references/mechanical_terms_index.md:79,95-97` | HARDCODED DUPLICATE | Independent prose table; file self-declares `## Status: PROPOSAL — diagnostic deliverable...not yet committed to canonical sources` (line 4) | **Drifted** — still describes Agility as Combat Pool base, dated 2026-05-08, predates the R1 change |
| `designs/scene/derived_stats_v30.md:584` | CANONICAL DEFINITION (of current pool formula, which supersedes Agility's old role) | Authoritative per-file `## Status: CANONICAL` header + explicit supersession note | N/A — this is the site that makes the others stale |
| `designs/scene/combat_design_v1.md` (throughout) | HARDCODED DUPLICATE, self-flagged struck | File itself marks its own old formula "STRUCK" at line 33-34, but retains dozens of other Agility-dependent action rules (Disarm, Escape, Tie Up, Retrieve) not re-verified against the new engine | Formula explicitly struck in-file; action-rule usages not re-audited |
| `sim/personal/combat.py:5,46` | HARDCODED DUPLICATE, self-flagged deprecated but still wired | Docstring banner says "Retained for reference/history only — do NOT wire new game code through this file," yet `sim/cross_scale/scene_dispatch.py:96` imports it | **Drifted** (implements the struck formula) and still reachable at runtime |
| `designs/scene/combat_engine_v1/config.py:54` | CANONICAL DEFINITION (of Agility's *current* role, tempo not pool) | Live Class-C engine config, the current combat head per `CURRENT.md` | Agrees (this IS the current truth) |
| `tests/sim/*.md` (~90 files, sampled) | HARDCODED DUPLICATE (bulk, era-consistent) | Frozen historical run reports predating the R1 ratification | Agree with the canon *at the time they were written*; not reconciled forward, but explicitly archival per `sim/README.md` |
| `designs/audit/**` combat-recovery folders (sampled) | Mixed — mostly meta-discussion of the very Agility-pool-dominance defect that caused the change, not independent restatement | N/A (discussion, not assertion) | N/A |

---

## 2. Attunement

**Home definition.**
- `references/glossary.md:36`: `Attunement | — | 1–7 | Sensitivity to people, environments, and Thread-adjacent phenomena.`
- `references/descriptor_registry.yaml:42`: `{key: attr.social.attunement, name: Attunement, aliases: [Perception]}`, scale 1–7.
- `params/core.md:144`: Social group member: `Attunement (Att)`.

This is the **cleanest** of the ten terms — all three anchors agree on name, range, and rough meaning; the only wrinkle is descriptor_registry's declared alias "Perception," which is essentially unused in the corpus (see below).

**Usage sweep.** 250-file grep cap hit (i.e., ≥250 files). Canonical/live sites opened: `designs/scene/fieldwork_v30.md:35,83,86,89,93` (§2.1 Primary Attribute table — Attunement drives Exploration/Thread-aware sensing, Investigation/Witness-informant, Socializing/Read and Negotiate), `designs/scene/combat_design_v1.md:70` (initiative: "Higher Attunement acts last"), `params/contest.md:23,302` and `designs/scene/social_contest_v30.md:145` (`Roll Attunement + Recall, TN 7...` — Appraise action), `params/core.md:144,246`. Bulk sampled: dozens of `tests/sim/*.md` and `designs/audit/**` files use Attunement consistently as a Thread-sensing/perception driver, e.g. `tests/sim/sim_x_01_combat_thread.md`.

**Divergence check.** None found in formula or range. The one soft finding: descriptor_registry's alias "Perception" (line 42) has **essentially no independent life** in the corpus — grepping for it turns up only the registry entries themselves (`descriptor_registry.yaml:42`, `names_index.yaml:51`) and one unrelated hit (`references/proper_noun_triage_round2.yaml:540`, "Thread Perception" — a different, proper-noun-ish token, not this alias). No design doc actually writes "Perception" to mean the Attunement attribute. This mirrors the Acuity/Will pattern (§3, §6 below) at smaller scale: a registry-declared alias that was never adopted in practice, though here it is filed as a **secondary** alias rather than a proposed primary rename, so the practical risk is lower.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/descriptor_registry.yaml:42` | CANONICAL DEFINITION | Named home, `attr.social.attunement` | — |
| `references/glossary.md:36` | HARDCODED DUPLICATE | Independent restatement, no import | Agrees (range + meaning both match) |
| `params/core.md:144` | HARDCODED DUPLICATE | Independent table row | Agrees |
| `references/alias_registry.yaml:32-36` | HARDCODED DUPLICATE | Independent entry, omits the "Perception" alias entirely | Agrees on what it states; simply doesn't carry the alias |
| `references/names_index.yaml:51` | PULLED / REFERENCED | Declared mirror of descriptor_registry (file header lines 28-29) | Agrees |
| `designs/scene/fieldwork_v30.md:35,83,86,89,93` | HARDCODED DUPLICATE (of role, not range) | Independent prose assigning Attunement as primary attribute for 5 distinct fieldwork sub-actions | Agrees with descriptor_registry's roster membership; fieldwork_v30.md is itself not listed as a row in `CURRENT.md`'s table (worth noting, though outside this batch's scope) |
| `params/contest.md:23,302`, `social_contest_v30.md:145` | HARDCODED DUPLICATE | Independent formula restatement (`Attunement + Recall`) | Agrees |
| `tools/observability/lexicon_data.js` | PULLED / REFERENCED | Same generator mechanism as §1 | Agrees (inherits sources) |
| Bulk `tests/sim/*.md`, `designs/audit/**` (sampled) | HARDCODED DUPLICATE (bulk) | Independent narrative/sim usage, consistent | Agrees |

---

## 3. Cognition / Acuity

**Home definition — this is where the roster conflict gets sharpest.**
- `references/glossary.md:37`: `Cognition | — | 1–7 | Reasoning, memory, analysis.` — **"Cognition" is the full, undecorated term**, no mention of "Acuity" anywhere in Part One.
- `references/descriptor_registry.yaml:39`: `{key: attr.mind.acuity, name: Acuity, aliases: [Reasoning, Cognition]}` with an inline comment: `# [ASSUMPTION] legacy 'Cognition' folds to Acuity -- Jordan veto`. Here **"Acuity" is declared the current primary name** and "Cognition" is demoted to a legacy alias, explicitly flagged `[ASSUMPTION]`-grade pending Jordan's veto — i.e., the registry itself marks this rename as not fully settled.
- `params/core.md:143,244-252`: uses **"Cognition (Cog)"** throughout, including the dedicated "Attribute Roles — Fieldwork (PP-628)" table (line 244) — no mention of "Acuity" anywhere in this file.

**Usage sweep.** `Cognition|Acuity` combined pattern matched 224 files. I additionally ran `\bAcuity\b` alone to isolate real adoption: **18 files total**, of which the actual list is: `references/descriptor_registry.yaml`, `references/names_index.yaml`, `references/glossary.md` (only inside the IN-FLUX banner quoting the registry, not as its own definition), `tools/observability/{lexicon_data.js, lexicon.json, decisions_data.js, decisions.json, console.html, DECISIONS.md}` (generated), `tests/registry/test_descriptor_registry.py` (tests the registry's own alias-resolution code), `tools/valoria_rename.py` (the rename executor tool, reads names_index.yaml), and five **audit/meta documents that are discussing the naming conflict itself** or an unrelated proposal (see below) — **zero** actual mechanical/design-prose documents (`params/core.md`, `designs/scene/fieldwork_v30.md`, `designs/provincial/mass_battle_v30.md`, `designs/scene/derived_stats_v30.md`, `designs/scene/social_contest_v30.md`, any `sim/` code) use "Acuity" as the attribute name. All of these use "Cognition" exclusively.

**Divergence check.**
1. **The registry's chosen "current primary" name has zero adoption in live mechanical content.** Every canonical formula that consumes this attribute writes "Cognition": `designs/provincial/mass_battle_v30.md:266` — `**Command = clamp(round((2 × Charisma + Cognition) ÷ 3), 1, 7)**` (ED-899, current) and its engine source `tests/sim/mass_battle/config.py:159` — `CMD_COG_WEIGHT = ... # Cognition SECONDARY weight in derived Command`; `designs/scene/fieldwork_v30.md:82,85,244` ("Cognition | Terrain/navigation exploration..."); `params/core.md:143-244`. "Acuity" as a formula input appears **nowhere**.
2. **A second, entirely unrelated "Acuity" exists in the corpus and was explicitly rejected.** `designs/audit/comprehensive_system_audit_2026-04-15.md:469-480` proposes **"Acuity" as a new fieldwork-fatigue derived resource** = `(Cognition + Focus)`, a depletable pool distinct from the Cognition attribute itself. `designs/architecture/integration_proposal_v30.md:200-204` explicitly **rejects** this proposal: *"Introducing Acuity as an additional resource would double-penalize investigation... Acuity should not be introduced."* This is a real case of **two genuinely distinct mechanics sharing one name** by coincidence: (a) the rejected April-2026 fieldwork-fatigue-resource proposal named "Acuity" (a derived value, Cognition+Focus, never adopted), and (b) the June-2026 `descriptor_registry.yaml` renamed-primary-attribute "Acuity" (replacing Cognition itself). Neither document references the other; the name collision appears to be coincidental, not intentional reuse.
3. Glossary's own IN-FLUX banner (line 31, quoted in §0) is itself the clearest first-party acknowledgment that this conflict is unresolved.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/descriptor_registry.yaml:39` | CANONICAL DEFINITION (of the *proposed* renamed roster) | Named home, explicitly `[ASSUMPTION]`-graded pending Jordan veto | Its own primary name ("Acuity") is **not adopted** anywhere downstream — see below |
| `references/glossary.md:37` | HARDCODED DUPLICATE (of the pre-rename name) | Independent restatement, "Cognition" only, no Acuity | Matches every live mechanical usage; disagrees with descriptor_registry's chosen primary |
| `params/core.md:143,244-252` | HARDCODED DUPLICATE | Independent table + dedicated fieldwork-roles table, "Cognition" only | Matches live usage; disagrees with descriptor_registry's primary |
| `designs/provincial/mass_battle_v30.md:266` | HARDCODED DUPLICATE (of formula, restated from engine) | Independent prose transcription of the Command formula | Agrees with `tests/sim/mass_battle/config.py` (its stated source of truth); uses "Cognition" not "Acuity" |
| `tests/sim/mass_battle/config.py:159` | CANONICAL DEFINITION (of the live Command-derivation weight) | `CMD_COG_WEIGHT` constant, labeled canonical by inline `[canonical: Jordan directive 2026-06-02]` comment; `mass_battle_v30.md`'s own ED-899 banner says the engine leads and the doc follows | — (this is the numeric source of truth) |
| `designs/scene/fieldwork_v30.md:82,85,244` | HARDCODED DUPLICATE | Independent §2.1 Primary Attribute table | Agrees with live usage; "Cognition" not "Acuity" |
| `references/names_index.yaml:49` | PULLED / REFERENCED | Declared mirror of descriptor_registry | Faithfully mirrors the unadopted "Acuity" rename |
| `references/mechanical_terms_index.md:81,104-106` | HARDCODED DUPLICATE, self-declared non-canonical | File header: `## Status: PROPOSAL...not yet committed to canonical sources` | Uses "Cognition"; also stale on Command formula (still cites the old equal-weight form, see §5) |
| `tools/observability/lexicon_data.js` etc. | PULLED / REFERENCED | `build_lexicon.py`, generated_from list includes descriptor_registry.yaml | Faithfully reflects the registry's unadopted rename |
| `tests/registry/test_descriptor_registry.py:19,26,34` | PULLED / REFERENCED (test of the registry mechanism itself) | Asserts `dr.resolve(reg, 'Spirit')['key'] == 'attr.mind.will'`-style alias resolution — tests the *fold* mechanism, not a live game usage | N/A — it's testing the registry's own code, not asserting the fold is adopted downstream |
| `tools/valoria_rename.py` | PULLED / REFERENCED | The rename-executor tool that would propagate a `names_index.yaml` canonical change if invoked | N/A — an unexecuted tool |
| `designs/audit/comprehensive_system_audit_2026-04-15.md:469-480` | UNCLEAR / NO CANONICAL SOURCE — this is a **different mechanic** (a rejected fieldwork resource), not the attribute | Independent proposal, explicitly not adopted | N/A — not the same referent as the attribute "Cognition/Acuity" |
| `designs/architecture/integration_proposal_v30.md:200-204` | Discussion/adjudication of the above proposal, not an independent restatement of either meaning | — | N/A |

---

## 4. Endurance

**Home definition.**
- `references/glossary.md:38`: `Endurance | — | 1–7 | Physical resilience. Determines Health and Stamina base.`
- `references/descriptor_registry.yaml:35`: `{key: attr.body.endurance, name: Endurance, aliases: [Vitality]}`, scale 1–7.
- `params/core.md:142`: Physical group member.

All three agree on name and range. The description ("Determines Health and Stamina base") is directionally correct but the actual formulas have moved on (see below).

**Usage sweep.** 217 files. Canonical/live sites opened: `designs/scene/derived_stats_v30.md §4.1, §4.2` (lines 55-122 — Health and Stamina formulas, both Endurance-driven but now with Spirit/Strength cross-terms), `params/core.md:154-166` (Derived Scores table), `designs/scene/combat_engine_v1/` (no direct Endurance constant, but `config.py` `STAMINA_REF=18.0` line 56 references the Stamina system it feeds), `references/mechanical_terms_index.md:82,92` (stale duplicate), `params/history/combat.md`, `designs/territory/settlement_layer_v30.md` (unrelated settlement-scale usage of the *word* "Endurance" was not found — settlement stats are Legitimacy/Popular Support/Prosperity/Defense/Order per `descriptor_registry.yaml:78-82`; this file appeared in the earlier Endurance grep because of narrative prose mentioning character endurance in a settlement-siege context, not a stat collision).

**Divergence check.**
1. **Health formula has moved twice since the glossary's "= Endurance" description.** `references/glossary.md:47`: `Health | HP* | = Endurance | Wound track. Resets per wound.` This is the **oldest, simplest form** and is superseded. Current: `designs/scene/derived_stats_v30.md:67` (`## Status: CANONICAL`, §4.1 marked "AUTHORITATIVE (PP-716)"): `Health (full) = round(WI × (Max Wounds + 1) + 0.25 × Strength × Endurance)`, where `WI = round(Endurance + 4 + 0.4 × Spirit)`. Also **"Wound track. Resets per wound"** is wrong — the current spec (`derived_stats_v30.md:70`) says wounds are **non-resetting**, clearing only at session end. `params/core.md:158` correctly reflects the current formula (it cross-references `derived_stats_v30.md §4.1 as authoritative`), so `params/core.md` and `derived_stats_v30.md` agree; `glossary.md:47` is the outlier and is three iterations of canon behind.
2. **Stamina formula**: `glossary.md:48`: `Stamina | — | Endurance + History + 1 (armour-modified)`. Current, ratified 2026-05-29 (`derived_stats_v30.md:98`, `params/core.md:159`): `Stamina = (3 × Endurance) + (2 × Spirit)`. Glossary's formula is the pre-ED-694/pre-S1 form, struck twice over.
3. **"Vitality" naming collision** (descriptor_registry's declared alias for Endurance, line 35) is a genuine terminological trap: historically "Vitality" was also the **derived Health stat's** name under ED-694 (`references/mechanical_terms_index.md:91`: *"Vitality | — | (PP-694) | Replaces Health terminology in combat_v30 ED-548/694."*), later reverted to "Health" by PP-716 (`derived_stats_v30.md:88`: *"'Vitality = Endurance × 10' was introduced by ED-694...PP-716 reverts the simplification... Stat name reverted from Vitality to Health"*). So "Vitality" has meant, at different times/in different files, (a) an alias for the attribute Endurance (descriptor_registry, current) and (b) the name of a wholly different derived value (the Health track, now-retired usage). A reader encountering "Vitality" in an older audit doc cannot tell which sense is meant without checking dates.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/descriptor_registry.yaml:35` | CANONICAL DEFINITION (roster) | Named home | — |
| `designs/scene/derived_stats_v30.md:55-122` | CANONICAL DEFINITION (of Health/Stamina formulas) | Self-declared `AUTHORITATIVE (PP-716)`, explicit "other documents reference this section rather than restating" instruction (line 57) | — (this is the source of truth) |
| `params/core.md:154-166` | PULLED / REFERENCED | Explicit citation: `**See `designs/scene/derived_stats_v30.md` §4.1 as authoritative.**` (line 158) | Agrees (correctly defers) |
| `references/glossary.md:38,47-48` | HARDCODED DUPLICATE | Independent prose, no reference to derived_stats_v30 | **Drifted** — both Health (`=Endurance`) and Stamina (`End+History+1`) formulas are two ratifications behind current canon |
| `references/mechanical_terms_index.md:82,91-92` | HARDCODED DUPLICATE, self-declared non-canonical | Independent table; explicitly a PROPOSAL doc | Drifted (uses the ED-694 Vitality-replaces-Health framing, itself since reverted by PP-716) |
| `references/alias_registry.yaml:42-46` | HARDCODED DUPLICATE | Independent entry | Agrees on range/name; carries no formula to drift |
| `references/names_index.yaml:46` | PULLED / REFERENCED | Declared mirror | Agrees |
| `designs/scene/combat_engine_v1/config.py:56` | CANONICAL DEFINITION (of current Stamina-consuming constant `STAMINA_REF`) | Live Class-C engine config | Agrees (consistent with the current Stamina formula's range) |
| Bulk `tests/sim/*.md`, `designs/audit/**` (sampled, ~150+ files) | HARDCODED DUPLICATE (bulk, mixed vintage) | Many predate the S1/ED-1021 formula changes | Mixed — era-consistent at time of writing, not reconciled forward |

---

## 5. Presence / Charisma

**Home definition — the second sharpest naming conflict in this batch.**
- `references/glossary.md:39`: `Presence | — | 1–7 | Social force and rhetorical gravity. Debate pool base.` — "Presence" is the only name given; no mention of "Charisma."
- `references/descriptor_registry.yaml:43`: `{key: attr.social.charisma, name: Charisma, aliases: [Influence, Presence]}` — **"Charisma" is primary**, "Presence" demoted to alias.
- `params/core.md:144`: Social group member listed as `Charisma (Cha)` — **params/core.md itself already uses "Charisma," not "Presence."**

**Usage sweep.** Combined `Presence|Charisma` pattern hit the 250-file cap. Decisive evidence of actual practice: `params/contest.md:3-4` — file header comment: *"PP-234: Full system redesign. Genre restructure (3→2), attribute renames (**Presence→Charisma**, Memory→Recall), Composure = Charisma + 6..."* — i.e., **the rename from Presence to Charisma is an old, already-executed patch (PP-234)**, predating even the glossary's most recent sweep. Every live formula site uses "Charisma": `designs/scene/social_contest_v30.md:35,124,145,186-187,236-251` (Argue Pool, Charisma modifier, Face/Composure formulas), `designs/scene/derived_stats_v30.md:132-160` (Composure = Charisma×3), `designs/provincial/mass_battle_v30.md:266` (Command formula), `tests/sim/mass_battle/config.py:158` (`CMD_CHA_WEIGHT`), `designs/scene/fieldwork_v30.md:90,92` (Impress/Rumour). "Presence" appears live only as a **noted historical rename entry**: `params/contest.md:660` — `| Presence → Charisma | Applied throughout. |` (a changelog row, not a live usage) and `params/contest.md:709` (a flagged-for-cleanup residual pointer: `| references/params_combat.md | Any Presence references |`).

**Divergence check.**
1. **Glossary and alias_registry still present "Presence" as the sole canonical name**, with **no acknowledgment that Charisma exists at all** in that table. `references/alias_registry.yaml:47-51`: `presence: {canonical: "Presence", abbreviations: [], category: stat, range: "1-7"}` — no `aliases: [Charisma]` field, unlike its Bonds/Attunement neighbors which do carry alias lists elsewhere. This is the **opposite direction** of drift from Cognition/Acuity (§3): here the *old* patch already executed the rename in the live corpus (PP-234) and the naming-authority files (glossary, alias_registry) simply never caught up, whereas for Cognition/Acuity the registry's rename was never picked up downstream. Both are the same underlying failure mode (registry drift), pointing in opposite directions.
2. **Command formula, again**: `references/glossary.md:121`: `Command — ... ⌈(Presence + Cognition) ÷ 2⌉ ... (PP-232)`. Current canonical, per `designs/provincial/mass_battle_v30.md:266`: `Command = clamp(round((2 × Charisma + Cognition) ÷ 3), 1, 7)` (ED-899, weighted 2:1, "supersedes the equal-weight ⌈(Cha+Cog)÷2⌉ form"). This is a **double** divergence in one line: (a) stale attribute name (Presence vs. Charisma) and (b) stale formula (equal-weight ⌈⌉ vs. the later 2:1-weighted `clamp(round(...))`). `references/mechanical_terms_index.md:83,101-103` repeats the same stale Presence-named, Command-formula-input framing (itself non-canonical/PROPOSAL-status, but still a corpus artifact that could mislead a reader).
3. `designs/scene/derived_stats_v30.md:266` (its §8 faction-scale table) does not use Presence/Charisma at all (that's a faction-stat table); no divergence there.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/descriptor_registry.yaml:43` | CANONICAL DEFINITION (roster, current primary name) | Named home | Agrees with actual corpus practice ("Charisma" is what's live) — the one case where the registry's chosen primary matches reality |
| `params/contest.md:3-4,660` | CANONICAL DEFINITION (of the rename event itself, PP-234) | Explicit patch citation and changelog row | — |
| `designs/scene/social_contest_v30.md` (throughout) | HARDCODED DUPLICATE | Independent prose, consistently "Charisma" | Agrees |
| `designs/scene/derived_stats_v30.md:132-160` | CANONICAL DEFINITION (of Composure formula) | Self-declared authoritative derived-stat spec | Agrees |
| `designs/provincial/mass_battle_v30.md:266` | HARDCODED DUPLICATE (of formula, restated from engine) | Prose restatement; doc's own banner says engine (`config.py`) leads | Agrees with engine |
| `tests/sim/mass_battle/config.py:158` | CANONICAL DEFINITION (of the Command-weight constant) | `CMD_CHA_WEIGHT`, inline `[canonical: Jordan directive 2026-06-02]` | — (source of truth) |
| `references/glossary.md:39,121` | HARDCODED DUPLICATE | Independent prose, "Presence" only, both the attribute description and the Command formula | **Drifted on both counts** — name (Presence vs Charisma) and formula (equal-weight vs 2:1-weighted) |
| `references/alias_registry.yaml:47-51` | HARDCODED DUPLICATE | Independent entry, no Charisma alias recorded | **Drifted** — doesn't even record that this attribute now also goes by Charisma |
| `references/names_index.yaml:52` | PULLED / REFERENCED | Declared mirror of descriptor_registry | Agrees (correctly shows Charisma primary, Presence alias) — i.e. names_index is actually *more current* than its sibling alias_registry.yaml |
| `references/mechanical_terms_index.md:83,101-103` | HARDCODED DUPLICATE, self-declared non-canonical | PROPOSAL-status file | Drifted (same double-stale Command formula as glossary) |
| `designs/scene/fieldwork_v30.md:90,92` | HARDCODED DUPLICATE | Independent §2.1 table | Agrees ("Charisma") |
| `tools/observability/lexicon_data.js` etc. | PULLED / REFERENCED | Generated via `build_lexicon.py` from the same source list | Inherits whichever of its sources it weights — reflects the underlying disagreement |
| Bulk `tests/sim/*.md` (sampled) | Mixed HARDCODED DUPLICATE | Pre-PP-234 files use "Presence"; post-PP-234 files use "Charisma" — genuinely bimodal by file date | Mixed, era-consistent |

---

## 6. Spirit / Will

**Home definition.**
- `references/glossary.md:40`: `Spirit | — | 1–7 | Internal coherence, resolve, and Thread operation capacity.`
- `references/descriptor_registry.yaml:40`: `{key: attr.mind.will, name: Will, aliases: [Spirit]}` — comment: `# 'spirit move': formerly standalone Spirit; legacy formulas resolve via alias`.
- `params/core.md:145,214`: Metaphysical group, standalone: `Spirit`. Notably `params/core.md:214` states explicitly: *"Spirit is unrelated to Certainty."*

**Usage sweep.** Combined pattern hit the 250-file cap for both `Spirit|Will`. Isolated `attr.mind.will`/canonical-Will occurrences: **only in the registry files and their direct test** — `references/descriptor_registry.yaml:40,50`, `references/names_index.yaml:50`, `tests/registry/test_descriptor_registry.py:19,26,34`. Every live mechanical formula uses "Spirit": `designs/scene/derived_stats_v30.md:66,98,151,231` (Wound Interval, Stamina, Concentration, Thread Fatigue — four separate formulas, all "Spirit"), `designs/scene/combat_engine_v1/config.py:61` (`CONC_SPIRIT=2.0 ... # Concentration = 3*Focus + 2*Spirit`), `params/core.md:145,214,247`, `designs/scene/fieldwork_v30.md:88,247` (Thread-Read pool). "Will" as an attribute name has **zero adoption outside the registry pair and its own unit test.**

**Divergence check.** Structurally identical to the Cognition/Acuity case (§3): the registry declares a rename that the entire rest of the corpus — including formulas ratified *after* the registry was created (e.g., ED-1021's D-A update to the Wound Interval, dated 2026-06-18, which is after the registry's 2026-06-06 ratification date) — continues to write using the pre-rename name "Spirit." This means even *new* canon authored after the registry existed did not adopt "Will." No case was found where "Will" appears as a load-bearing formula input anywhere in `params/`, `designs/`, or `sim/`.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/descriptor_registry.yaml:40` | CANONICAL DEFINITION (of the proposed renamed roster) | Named home, `[ASSUMPTION]`-adjacent per the file's general disclaimer (though this specific entry lacks the explicit `[ASSUMPTION]` tag that attr.mind.acuity carries — worth noting the inconsistency in how the two mind-attribute renames are flagged) | Not adopted anywhere downstream |
| `references/glossary.md:40` | HARDCODED DUPLICATE | Independent prose, "Spirit" only | Matches every live formula; disagrees with descriptor_registry's primary |
| `params/core.md:145,214` | HARDCODED DUPLICATE | Independent, "Spirit" only, plus an explicit relational claim ("Spirit is unrelated to Certainty") that has no analog under "Will" anywhere | Matches live usage |
| `designs/scene/derived_stats_v30.md:66,98,151,231` | CANONICAL DEFINITION (of four Spirit-consuming formulas, all post-dating the registry) | Self-declared authoritative; ED-1021 dated 2026-06-18, after registry's 2026-06-06 ratification | Internally self-consistent; none use "Will" |
| `designs/scene/combat_engine_v1/config.py:61` | CANONICAL DEFINITION (of the live engine constant) | `CONC_SPIRIT`, inline comment naming Jordan's ratification date | Uses "Spirit" |
| `references/names_index.yaml:50` | PULLED / REFERENCED | Declared mirror | Faithfully reflects the unadopted rename |
| `tests/registry/test_descriptor_registry.py:19,26,34` | PULLED / REFERENCED (tests the fold mechanism only) | `dr.resolve(reg, 'Spirit')['key'] == 'attr.mind.will'` | N/A — validates that the alias *resolves*, not that "Will" is used in play |
| `tools/observability/lexicon_data.js` etc. | PULLED / REFERENCED | `build_lexicon.py` | Reflects registry's unadopted rename |
| `references/alias_registry.yaml:52-56` | HARDCODED DUPLICATE | Independent entry, "Spirit" only, no "Will" alias recorded at all | Matches live usage; doesn't record the registry's rename |
| Bulk `tests/sim/*.md`, `designs/audit/**` (sampled, 200+ files) | HARDCODED DUPLICATE (bulk) | Universally "Spirit" | Agrees with live usage; none use "Will" |

---

## 7. Strength

**Home definition.**
- `references/glossary.md:41`: `Strength | — | 1–7 | Raw physical power. Weapon minimum requirement.`
- `references/descriptor_registry.yaml:34`: `{key: attr.body.strength, name: Strength, aliases: []}`, scale 1–7.
- `params/core.md:142`: Physical group member.

All three agree on name/range. No alias contention (unlike Endurance/Cognition/Spirit/Charisma).

**Usage sweep.** 217 files. Canonical/live sites: `designs/scene/derived_stats_v30.md:59,67,72` (Health formula's Strength term, "very-low-weight term proportional to Endurance," ED-1021), `designs/scene/combat_engine_v1/` weapon physics (config.py doesn't reference "Strength" by that literal string but the design docs around it do — e.g. `combat_design_v1.md:173,178` — "Impact = Strength + Heft(weight) — ADDITIVE force; NO Strength×weight multiplier"), `params/core.md:158` (Health formula, `0.25 × Strength × Endurance`). Legacy/superseded site: `designs/scene/combat_design_v1.md:353,361` — *"**Strength:** Headcount/health pool. At 0: destroyed... Effective CP = min(CP, current Strength)"* — this is describing **mass-combat Strength**, the pre-PP-232 unit stat that was renamed to **Size** (`references/glossary.md:123`: *"Size — Unit headcount stat (replaces Strength)... (PP-232)"*).

**Divergence check.**
1. **Two distinct "Strength" referents coexist in the corpus by design (not an error) but are easy to confuse if a reader doesn't know the PP-232 rename**: (a) the personal-character attribute (this item's home definition, still called Strength, unchanged), and (b) the pre-PP-232 **mass-combat unit stat**, renamed to **Size**, but still appearing under the old name "Strength" in `designs/scene/combat_design_v1.md:353,361` — a file whose own header banner (line 33-34) already flags other parts of itself as struck/superseded, but does not flag this passage. This is a real residual: an active (not archived) file still uses "Strength" to mean the mass-combat headcount stat that was renamed to "Size" in `references/glossary.md:123` and `references/alias_registry.yaml` (combat section, `size: {... note: "...Replaces Strength in mass combat."}`).
2. **Damage formula**: `designs/scene/combat_design_v1.md:173` states Strength contributes **additively** ("Impact = Strength + Heft(weight)... NO Strength×weight multiplier"), which is presented as struck at line 178 in favor of a different Coupling-based model — but derived_stats_v30.md's *current* Health formula (line 158, `0.25 × Strength × Endurance`) uses Strength **multiplicatively** against Endurance (not against weapon weight) as a Health-buffer term. These are not directly contradictory (different formulas, different purposes — one is weapon damage output, one is the defender's Health buffer) but a reader skimming both docs could easily conflate the two distinct "how does Strength multiply" claims.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/descriptor_registry.yaml:34` | CANONICAL DEFINITION | Named home | — |
| `references/glossary.md:41,123` | HARDCODED DUPLICATE (both the attribute entry and the Size/Strength rename note) | Independent prose | Agrees — correctly documents the Size rename in Part Five even while Part One doesn't cross-reference it |
| `params/core.md:142,158` | HARDCODED DUPLICATE | Independent | Agrees |
| `designs/scene/derived_stats_v30.md:59,67,72` | CANONICAL DEFINITION (of Health formula's Strength term) | Self-declared AUTHORITATIVE, ED-1021 | — |
| `designs/scene/combat_design_v1.md:353,361` | HARDCODED DUPLICATE, **stale referent** | Independent prose using the pre-PP-232 name for what is now "Size" | **Drifted / uses a retired name** for a different stat than this item's Strength; not flagged in-file the way the pool formula is |
| `references/alias_registry.yaml:56-61` (combat section, `size:` entry) | HARDCODED DUPLICATE | Independent entry correctly noting "Replaces Strength in mass combat" | Agrees (correctly documents the rename) |
| Bulk `tests/sim/*.md`, `designs/audit/**` (sampled) | HARDCODED DUPLICATE (bulk) | Mixed — some pre-PP-232 mass-combat sim logs use "Strength" for the unit stat, consistent with their era | Era-consistent, not reconciled forward |

---

## 8. Focus (as an attribute)

**Home definition — a genuine double-definition, not just a naming variant.**
- `references/glossary.md:52` (Part One, **"Derived Character Stats" table**, not the Core Attributes table): `Focus | — | 1–5+ | Contact duration in Thread operation rounds.` Glossary does **not** list Focus as a core attribute at all — it treats Focus as a *derived stat*.
- `references/descriptor_registry.yaml:38`: `{key: attr.mind.focus, name: Focus, aliases: []}` — filed under `mind:` in the **9-attribute roster**, scale 1–7. Descriptor_registry treats Focus as a **base attribute**.
- `params/core.md:143,152`: Mental group member, `Focus (Foc)`, range 1–7 (part of the "10 attributes" frame): *"Concentration, discipline, precision under pressure. Governs Thread contact duration: Contact Rounds = Focus score (range 1–7)."* — params/core.md also treats Focus as a **base attribute**, agreeing with descriptor_registry on classification and range, but its *mechanical claim* ("Contact Rounds = Focus score") is the very thing that has since been retired.

**Usage sweep.** 250-file cap. Canonical/live sites: `designs/scene/derived_stats_v30.md:151,158,231,249-259,540` (Concentration formula, Thread Fatigue section, §14.1 table), `designs/scene/combat_engine_v1/config.py:60-62,128` (`CONC_FOCUS=3.0`, `POISE_FOCUS_K=0.10 # Focus speeds structure recovery`), `designs/scene/social_contest_v30.md` (Focus defence in strain formula), `params/core.md:143,152`. 

**Divergence check.**
1. **Categorical mismatch**: glossary treats Focus as a *derived stat* (range "1–5+", meaning "contact duration itself"); descriptor_registry and params/core.md treat it as a *base attribute* (range 1–7) that merely *governs* contact duration. These are not compatible framings of the same number — one says Focus IS the duration (1–5+ rounds), the other says Focus is an attribute that PRODUCES a duration value via a separate formula. `references/alias_registry.yaml:89-93` sides with the glossary's framing, filing `focus:` under its `derived_stats:` block (not `core_attributes:`), range "1-5+" — i.e., **two of the four naming-authority files (glossary, alias_registry) classify Focus as a derived stat**, and **two (descriptor_registry, params/core.md) classify it as a base attribute** — a genuine unresolved four-way split on what kind of thing Focus even *is*, layered on top of the ordinary roster-count conflict.
2. **The mechanical claim itself has been retired.** `params/core.md:152`: *"Governs Thread contact duration: Contact Rounds = Focus score (range 1–7)."* Current canon, `designs/scene/derived_stats_v30.md:249-259` (§6.1, part of a file with `## Status: PROPOSAL — supersedes prior derived_stats_v30.md` at line 4, but whose Focus-role content is presented as settled, cross-referenced by `references/names_index.yaml` clock/mechanic renames): *"**Focus role change:** Focus no longer sets contact duration. Contact Rounds eliminated. Focus sets maximum operations per contact session..."* This exact rename is independently confirmed live in the naming registry: `references/names_index.yaml:118-123`: `thread.thread_fatigue: {canonical: Thread Fatigue, legacy: ["Contact Rounds"], ...}`. So `params/core.md:152`'s "Contact Rounds = Focus score" sentence describes a **mechanic (Contact Rounds) that the corpus's own naming registry lists as retired legacy vocabulary** — `params/core.md` has not been updated to match, even though it is the batch's own nominated canonical anchor for this term and even though `params/core.md` elsewhere (line 158) correctly defers to `derived_stats_v30.md` for the adjacent Health formula.
3. Glossary's range "1–5+" for Focus-as-contact-duration doesn't correspond to any live mechanic either; the current Focus-derived table is "Max Operations per Session" (`derived_stats_v30.md:249-256`, values 0/1/2/3/4+ for Focus 1/2/3/4/5+) — a different table with different semantics than "contact duration in rounds."

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/descriptor_registry.yaml:38` | CANONICAL DEFINITION (roster membership, as base attribute) | Named home | — |
| `references/glossary.md:52` | HARDCODED DUPLICATE, **different classification** | Independent, filed as derived stat not attribute | **Drifted** — wrong category and wrong range (1–5+ vs 1–7), plus describes a retired mechanic |
| `params/core.md:143,152` | HARDCODED DUPLICATE | Independent, correct classification (attribute) but **stale mechanical claim** | **Drifted** — "Contact Rounds = Focus" is retired per `derived_stats_v30.md §6.1` and `names_index.yaml:118-123` |
| `designs/scene/derived_stats_v30.md:151,231,249-259` | CANONICAL DEFINITION (of Focus's current derived roles: Concentration input, max-ops-per-session cap) | Self-declared spec, cites ED-902 | — |
| `references/alias_registry.yaml:89-93` | HARDCODED DUPLICATE, **different classification** | Independent, filed under `derived_stats:` | Same categorical drift as glossary |
| `references/names_index.yaml:48,118-123` | PULLED / REFERENCED (mixed) | attr.mind.focus mirrors descriptor_registry (attribute framing); separately, `thread.thread_fatigue` entry documents the Contact-Rounds retirement | Internally consistent with the *current* mechanic, but sits in the same file as the roster mirror that doesn't resolve the classification conflict with glossary |
| `designs/scene/combat_engine_v1/config.py:60-62,128` | CANONICAL DEFINITION (of live Focus-consuming constants) | `CONC_FOCUS`, `POISE_FOCUS_K` | Agrees with current derived-stat role |
| `references/mechanical_terms_index.md:97` | HARDCODED DUPLICATE, self-declared non-canonical | Repeats glossary's derived-stat framing verbatim ("Focus | 1–5+ | Contact duration...") | Drifted, same as glossary |
| Bulk `tests/sim/*.md` (sampled) | Mixed | Some older files use the retired Contact-Rounds framing, consistent with their era | Era-consistent, not reconciled forward |

---

## 9. Bonds

**Home definition — glossary is silent on this term entirely.**
- `references/glossary.md`: **zero occurrences of "Bonds" anywhere in the file.** I grepped the full file specifically and confirmed no hit. Bonds is absent from the 7-attribute Core Attributes table, absent from Derived Character Stats, absent from every other Part. This is not a stale-but-present entry like the others above — it is a **true gap**: the corpus's designated term-expansion authority does not define this term at all, despite it being load-bearing in current design (Knot formation gates, fieldwork Connect action).
- `references/descriptor_registry.yaml:44`: `{key: attr.social.bonds, name: Bonds, aliases: [Sincerity, Affability]}`, scale 1–7, filed as a base attribute.
- `params/core.md:144,147-149`: Social group member, with a dedicated explanatory paragraph (lines 147-149): *"**Bonds (Bon):** Governs relational *capacity* (ED-912 — Disposition is now a flat −5..+5, NOT Bonds-capped): (1) Knot prerequisite = Bonds ≥ 5...; (2) max Knot count = floor(Bonds/2)+1..."*

**Usage sweep.** 217 files. Canonical/live sites: `designs/scene/derived_stats_v30.md:388-394` (§10.1, "Disposition and the Bonds Attribute (ED-912 — decoupled)"), `designs/scene/fieldwork_v30.md:91` (Socializing/Connect, primary attribute), `params/core.md:147-149,240-252` (Bonds paragraph + Attribute Roles table), `canon/mechanics_index.yaml:294,350-351` (`pool: "(Bonds*2)+3"`, `max: "floor(Bonds/2)+1"`), `references/mechanical_terms_index.md:101` (miscategorized, see below).

**Divergence check.**
1. **Formula history conflict, resolved in canon but not everywhere reflected.** `references/mechanical_terms_index.md:101`: *"Bonds | — | 1–7 | Structural relationship capacity. **Caps Disposition Track (PP-684).**"* Current canon, `derived_stats_v30.md:388-390` (§10.1): *"Disposition is a flat −5..+5 (**ED-912 — supersedes the PP-684 'ceiling = Bonds'**)...The two are **decoupled**: Bonds no longer caps Disposition."* `params/core.md:147` correctly states the ED-912 supersession inline. `mechanical_terms_index.md` still states the old PP-684 "caps Disposition Track" framing as if current — this file is dated 2026-05-08 and self-declared PROPOSAL/non-canonical, but it is a live corpus artifact that misstates a superseded rule as active.
2. **Classification conflict, same shape as Focus (§8).** `mechanical_terms_index.md` files Bonds under its "§1.2 Derived Character Stats" table (line 101) rather than "§1.1 Core Attributes" (lines 79-85) — treating Bonds as a *derived* value, whereas `descriptor_registry.yaml` and `params/core.md` both treat it as a *base* attribute. Unlike Focus, glossary itself is silent here rather than actively disagreeing, but the disagreement between the other three files (descriptor_registry + params/core.md = base attribute, vs. mechanical_terms_index = derived stat) still stands.
3. **Formula agreement, for what it's worth**: `canon/mechanics_index.yaml:350-351` (`pool: "(Bonds*2)+3"`, `max: "floor(Bonds/2)+1"`) and `params/core.md:148` (`max Knot count = floor(Bonds/2)+1`) and `derived_stats_v30.md §14.4` (`Knot Pool = (Bonds × 2) + 3`) all agree — this specific formula is clean across the sites that do carry it.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/descriptor_registry.yaml:44` | CANONICAL DEFINITION (roster) | Named home | — |
| `references/glossary.md` | **UNCLEAR / NO CANONICAL SOURCE** — term absent entirely | No entry exists to classify | N/A — this is itself the finding: the batch's nominated glossary anchor has no Bonds entry at all |
| `params/core.md:144,147-149` | HARDCODED DUPLICATE (with a correct, current supersession note) | Independent paragraph, cites ED-912 explicitly | Agrees with current canon |
| `designs/scene/derived_stats_v30.md:388-394` | CANONICAL DEFINITION (of the Bonds/Disposition decoupling) | Self-declared authoritative section, ED-912 | — |
| `canon/mechanics_index.yaml:294,350-351` | PULLED / REFERENCED (formula echoing derived_stats/core, no independent derivation shown) — borderline HARDCODED, since the formula string is typed out rather than imported, but it is consistent | Restates the formula as a literal string in a machine-readable registry, with a "notes" field explicitly citing "same formula as Knot Max per derived_stats §10.1" (line 294) — i.e. it **names its source inline**, which nudges this toward PULLED/REFERENCED-by-citation rather than a silent duplicate | Agrees |
| `references/mechanical_terms_index.md:101` | HARDCODED DUPLICATE, self-declared non-canonical, **wrong classification + stale rule** | Independent, PROPOSAL-status | **Drifted** — states the pre-ED-912 "caps Disposition Track" rule as current, and miscategorizes Bonds as derived rather than base |
| `designs/scene/fieldwork_v30.md:91` | HARDCODED DUPLICATE | Independent §2.1 table entry (Socializing/Connect) | Agrees (roster membership + role) |
| `references/names_index.yaml:53` | PULLED / REFERENCED | Declared mirror | Agrees |
| `references/alias_registry.yaml` | **ABSENT** (same gap as glossary — Bonds is not in the `core_attributes:` block, lines 26-61) | — | N/A — confirms the alias_registry and glossary share this gap, consistent with alias_registry's stated seed source being the glossary (`# Seed source: references/glossary.md (2026-04-02)`, line 13) |

---

## 10. The attribute-roster count itself

Firsthand-confirmed, by direct reading (not by trusting any prior audit number):

| File | Firsthand count | Members |
|---|---|---|
| `references/glossary.md:33-41` | **7** | Agility, Attunement, Cognition, Endurance, Presence, Spirit, Strength |
| `references/descriptor_registry.yaml:30-44` | **9** | Strength, Endurance, Agility, Focus, Acuity, Will, Attunement, Charisma, Bonds |
| `params/core.md:140-145` (table) + line 138 (prose) | **10** | Agility, Endurance, Strength, Cognition, **Recall**, Focus, Attunement, Bonds, Charisma, Spirit — and the file's own prose independently confirms the count: *"Point pool at creation: 31 points across **10 attributes**."* |
| `references/alias_registry.yaml:26-61` (`core_attributes:` block) | **7** | Agility, Attunement, Cognition, Endurance, Presence, Spirit, Strength — i.e., a fourth file that independently reproduces the glossary's exact 7-item roster (by name and by omission of Focus/Bonds/Recall), filing Focus separately under `derived_stats:` |

This is **not** the two-way conflict the glossary's own banner (line 31) describes ("this 7-attribute roster conflicts with descriptor_registry.yaml's 9-attribute roster"). It is a genuine **three-way** conflict once `params/core.md` is read directly, and arguably **four-way** counting `alias_registry.yaml` as a second independent 7-roster witness. The critical, previously-unremarked-in-the-glossary-banner fact: **`params/core.md`'s 10th member is "Recall,"** a term that appears in **neither** the glossary's 7 nor the descriptor_registry's 9 as an attribute (descriptor_registry has no `attr.*.recall` key anywhere in its `attributes:` block). `references/mechanical_terms_index.md:121` files "Recall" under **§1.4 "Personal-scale narrative properties"** (a fourth category, distinct from both "Core Attributes" §1.1 and "Derived Character Stats" §1.2), describing it as *"Cap on History entries. Renamed from 'Memory (score)'..."* — i.e., a third, non-canonical corpus document has yet a **different** classification for Recall than params/core.md's "it's a Mental-group attribute" framing. `references/name_collision_database.yaml:98` (a fourth non-canonical vocabulary-audit document, dated 2026-05-08) files Recall under **silo_1 "Character Attributes"** general list (line 98) without resolving whether it's a base attribute or a derived cap — a fifth, still-different treatment.

So: not only does the count disagree (7 / 9 / 10), the *membership* disagrees in a way that simple aliasing cannot reconcile — three attributes present in `params/core.md`'s 10 (Focus, Bonds, and especially Recall) are handled by descriptor_registry/glossary through fold-in-as-attribute (Focus, Bonds) or **omission entirely** (Recall, which no live attribute-roster registry — descriptor_registry, names_index, alias_registry — carries as an attribute key at all; it exists only in prose param docs and the non-canonical vocabulary-audit files).

**Classification of the roster-count sites themselves:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with the others? |
|---|---|---|---|
| `references/descriptor_registry.yaml:12,30-44` | CANONICAL DEFINITION (self-declared: "Single source of truth for all quantified-qualitative descriptors," line 2; header comment line 12 explicitly declares "attribute roster -> 9 personal attributes...IN FLUX") | Named home, self-aware of its own instability | Disagrees with glossary (7) and params/core.md (10) |
| `references/glossary.md:29-41` | HARDCODED DUPLICATE, self-flagged unstable | Independent table, banner (line 31) names the descriptor_registry conflict but not the params/core.md one | Disagrees with descriptor_registry (9) and params/core.md (10); its own banner is itself **incomplete** (only names one of the two real conflicts) |
| `params/core.md:137-145` | HARDCODED DUPLICATE, **not flagged as unstable at all** | Independent table + independent prose confirmation ("31 points across 10 attributes"), no cross-reference to either the glossary or descriptor_registry rosters, no IN-FLUX banner | Disagrees with both; and unlike the other two, **carries no acknowledgment that a conflict exists** |
| `references/alias_registry.yaml:24-61` | HARDCODED DUPLICATE, **not flagged as unstable** | Independent `core_attributes:` block; file header says "Seed source: references/glossary.md (2026-04-02)" (line 13), so this is a **derived-by-hand-copy** duplicate of glossary's 7, not an independent editorial judgment — but it was never subsequently updated when descriptor_registry.yaml (ratified 2026-06-06) introduced the 9-roster, so it's now a stale copy of a table that was itself already contested | Agrees with glossary (matches its 7 exactly, by construction); disagrees with descriptor_registry and params/core.md |
| `references/names_index.yaml:44-53` | PULLED / REFERENCED | Declared mirror of descriptor_registry's 9 (file header lines 28-29); `tools/ci_names_consistency.py` named as the enforcement mechanism | Faithfully carries forward descriptor_registry's side of the conflict; does not resolve it against glossary or params/core.md |
| `tools/observability/lexicon_data.js` / `lexicon.json` | PULLED / REFERENCED | `build_lexicon.py`, generated_from list includes glossary.md, descriptor_registry.yaml, alias_registry.yaml simultaneously — i.e. this generated artifact **ingests all three conflicting sources at once** with no reconciliation logic evident in the file itself | Mechanically inherits the conflict rather than resolving it |
| `references/mechanical_terms_index.md` §1.1 (lines 79-85) + §1.4 (lines 112-128) | HARDCODED DUPLICATE, self-declared non-canonical PROPOSAL | Independent 7-item "Core Attributes" table (matching glossary) **plus** a separate "personal-scale narrative properties" list that includes Bonds and Recall outside that 7 | A fifth distinct partition of the same term-set, agreeing with none of the other three exactly |
| `references/name_collision_database.yaml:81-124` (silo_1) | HARDCODED DUPLICATE, self-declared audit tool ("Hook-checkable," dated 2026-05-08) | Independent flat list mixing attributes, derived stats, and narrative properties into one "Character Attributes" silo with no sub-partition at all | A sixth distinct treatment — flattens the very attribute/derived-stat distinction the other files fight over |

**Bottom line for item 10, stated factually per the task's instruction not to editorialize on severity**: three files nominated by this batch as anchors give three different counts (7, 9, 10) read directly off the page, a fourth structurally-independent file (`alias_registry.yaml`) reproduces one side of that conflict (7) without resolving it, and at least two further non-canonical corpus documents (`mechanical_terms_index.md`, `name_collision_database.yaml`) each propose yet another partition of the same underlying term set. Only one of the four primary files (`descriptor_registry.yaml`) explicitly flags its own count as unsettled; `params/core.md` — despite being the batch's third nominated anchor and despite being cited elsewhefe in this very corpus (`derived_stats_v30.md`, `CURRENT.md` "Dice/resolution" row) as a live, current head — carries its 10-attribute count with no hedge, cross-reference, or IN-FLUX marker of any kind.
