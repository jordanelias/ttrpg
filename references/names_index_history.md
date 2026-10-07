# names_index.yaml — history and discussion

**Why this file exists.** `references/names_index.yaml` is read by `tools/names.py`,
`tools/export_names.py` (-> `engine/engine_params/names.json`) and the naming gates, and it sits close to
its register-size cap (`tools/ci_register_size_check.py`). Its dated narrative, rulings, renames and
"was X, now Y" commentary moved here (Jordan, 2026-10-06: *"you can extract all edit histories/discussion
from .yaml files in references and just make those a supplement"*).

**What stayed in the YAML:** the one-line purpose, how the file is read, the entry schema, the mirror
rules, the namespace-prefix table, every entry, and a one-line summary of each moved note where an editor
needs the fact to edit the entry correctly today. Every reader parses the file with `yaml.safe_load`, so
comment moves are invisible to code.

**Adding here, not there.** New dated narrative, rulings and provenance about a row go in this file under
the heading of the YAML section they concern; the YAML keeps only what an editor needs to act.

The moved text below is VERBATIM, grouped by the YAML's own sections. Nothing was deleted.

### Head: WHY (purpose and what the index replaced)

*(original lines 3-7 at 8b57336, verbatim)*

```yaml
# WHY: names used to be hardcoded and duplicated across 50+ prose docs, engine/params/, the
# registries, and the tools (ci_naming_check.py even hardcoded the deprecated proper
# noun). descriptor_registry.yaml already promised "a descriptor can be renamed HERE
# without rewriting any consumer" — this index makes that real for ALL named
# definitions, not just descriptors.
```

### Head: MIGRATION (how the file was seeded)

*(original lines 43-47 at 8b57336, verbatim)*

```yaml
# MIGRATION: seeded 2026-06-28 (attributes, faction/settlement stats, the proper-noun
# naming invariant, and the clean mechanic renames). 2026-07-01 (ED-1084): the rest of the
# proper-noun corpus folded in below as warn-tier `world.*` entries (generated from
# proper_noun_registry.yaml; ci_names_consistency keeps the pair agreeing). Remaining
# follow-up: flipping `warn -> block` per entry as each is triaged.
```

### ATTRIBUTES: why `Influence` was removed from the Charisma alias list

*(original lines 88-93 at 8b57336, verbatim)*

```yaml
  # `Influence` REMOVED from this alias list 2026-09-16: it was the canonical name of
  # `fac.influence` (a 0-7 faction stat, retired 2026-10-01 at plan position `29b`; the alias is NOT
  # restored by that retirement -- which attribute owns the word is a design call), so as an alias here
  # it made one string name two quantities. MEASURED before removing: every bare `Influence` in
  # the corpus is the roll stat (`conviction_track_v30.md` -- *"Influence vs Ob 2"*, *"Church
  # Influence vs Ob"*); none means Charisma, and no code read this list. `Presence` stays.
```

### CONVICTIONS: header (migration of the disambiguation gate)

*(original lines 102-106 at 8b57336, verbatim)*

```yaml
  # ── CONVICTIONS (the 7-axis character conviction class; new 2026-07-21, R2 / ED-IN-0082) ──
  # `context` is the §3.5 disambiguation gate, migrated VERBATIM from vector_audit's former
  # hardcoded SEED table (test_vector_audit pins byte-identical behaviour). vector_audit now
  # reads these FROM here (CLAUDE.md §8). enforce: warn — every display collides with a common
  # word. Single-quoted so YAML keeps the regex backslashes literal.
```

### PRESSURE POINTS: header

*(original lines 115-119 at 8b57336, verbatim)*

```yaml
  # ── PRESSURE POINTS (the 4-axis social-contest class; new 2026-07-21, R2 / ED-IN-0082) ──
  # Same shape as convictions: `context` is the §3.5 disambiguation gate, migrated VERBATIM from
  # vector_audit's former hardcoded SEED (test_vector_audit pins byte-identical). vector_audit
  # sources CLASSES['pressure_point'] + the SEED tokens FROM here (§8). enforce: warn — the
  # displays collide with common words.
```

### MECHANICS: header

*(original lines 125-129 at 8b57336, verbatim)*

```yaml
  # ── MECHANICS (strategic-layer mechanic tokens; new 2026-07-22, R2 namespacing / ED-IN-0082) ──
  # Namespaced ids so a generic "Stability"/"Mandate"/"Standing" is COLLISION-SAFE from the faction
  # stat `fac.stability` etc. (retired at `29b`; the namespace stays) — author with [[mech.stability]]. patterns
  # migrated verbatim from the hardcoded SEED; token_class: mechanic sources them into the audit
  # (category mechanic has no proper-noun mirror). enforce: warn (all collide with common words).
```

### CLOCK TRACKS: clock.ip — canonical second, rival third

*(original lines 142-146 at 8b57336, verbatim)*

```yaml
  # ⚠ CANONICAL SECOND, RIVAL THIRD (2026-09-16). This row carried ONLY 'Invasion Pressure' — which
  # is not the canonical expansion and is not the recorded rival either. Canon is INSTITUTIONAL
  # Pressure (`glossary.md`, `alias_registry.yaml`, `name_collision_database.yaml`), and the matcher
  # missed all 100 of its corpus occurrences while catching 28 of a name no registry blesses. The
  # rival STAYS: `patterns:` is a matcher list, not a definition, and finding drift is its job.
```

### CLOCK TRACKS: clock.pi — same defect, same block, same fix

*(original lines 148-149 at 8b57336, verbatim)*

```yaml
  # ⚠ SAME DEFECT, SAME BLOCK, SAME FIX. Canon is PUBLIC Instability (68 corpus occurrences, missed);
  # 'Political Instability' has 3 and no registry blesses it. Both matchers, canonical first.
```

### FACTION STATS: retired at plan position `29b`

*(original lines 154-158 at 8b57336, verbatim)*

```yaml
  # ── FACTION STATS: RETIRED at plan position `29b` (2026-10-01) ───────────────────────────────
  # `fac.influence`, `fac.wealth`, `fac.military`, `fac.intel`, `fac.stability` and `fac.legitimacy` mirrored
  # `descriptor_registry.yaml`'s `faction_stats` block, which left with `game_state.Faction` (`ID-13`), and
  # `tools/ci_names_consistency.py` refuses a mirror row with no registry entry. They are in git at
  # `5c5d8ec6:references/names_index.yaml`. `Legitimacy` is now `set.legitimacy` alone.
```

### SETTLEMENT STATS: set.facility_tier (ADDED)

*(original lines 166-169 at 8b57336, verbatim)*

```yaml
  # ADDED 2026-09-16, found the moment `ci_names_consistency.py` learned to check the OTHER
  # direction -- the second instance of the same gap as `fac.legitimacy` above. Declared in
  # `descriptor_registry.yaml:173` since 2026-07-08 (ED-IN-0029 D5 residual) and never mirrored
  # here. Its two aliases are transcribed from that row, not invented.
```

### PROPER-NOUN CORPUS FOLD-IN: NPC audit sourcing

*(original lines 255-262 at 8b57336, verbatim)*

```yaml
  # NPC audit sourcing (R2/ED-IN-0082, 2026-07-22): the 10 curated tracked NPCs carry
  # `token_class: npc` + explicit `patterns:` so the vector-audit sources them from HERE
  # (§8 "every rule lives once") instead of a hardcoded SEED roster. Patterns use the
  # FIRST NAME / TITLE and deliberately DROP the shared `Almqvist` dynasty surname (Jordan
  # 2026-07-22: "drop all Almqvist and use their first name … or title") — a family name is
  # ambiguous across four royals, so matching it would collide distinct people. `scale`
  # defaults to the token_class ('npc'). This also unifies the former Lisbeth/Grandmaster
  # Ehrenwall duplicate onto one token. Untagged characters below stay proper-noun tokens.
```

### territories: Schoenland filed with the places, classed as a faction

*(original lines 301-305 at 8b57336, verbatim)*

```yaml
  # ⚠ FILED WITH THE PLACES, CLASSED AS A FACTION, AND BOTH ARE RIGHT. Schoenland is a foreign
  # polity AND the eighth member of `engine/season/rosters.yaml: factions`, whose own note says
  # *"`Schoenland` IS A MEMBER AND IS FOREIGN"*. The class was simply never set, so `cast.py`'s
  # `_alias_map` -- which selects on `token_class: faction` -- saw seven of eight. The absences
  # at `rosters.yaml` :926 and :963 are about a LEADER and a `role_template`, not membership.
```

### factions: world.faction_x — the test faction

*(original lines 312-329 at 8b57336, verbatim)*

```yaml
  # ⚠⚠ A TEST FACTION, NOT CANON — RULED BY JORDAN 2026-09-18: *"place them all under 'faction x'
  # as a test faction"*. It exists so `engine/season/harness/governance_spine.py`'s generic governance spine
  # can seat offices at all: `office_faction` REFUSES an office naming neither a `body` nor a
  # `faction`, and a declared faction must be a member of this roster (`H-99` + §42.2's polarity
  # rule, *"no evidence of belonging is a refusal, never a default faction"*). So a fully generic
  # seat is forbidden by design, which is the code being right.
  # ⚠ IT IS DELIBERATELY UNMISTAKABLE. `faction x` names no polity, appears nowhere in
  # `systems/world/`, and would be absurd as canon — the same discipline as
  # `rosters.yaml: remit_default`, where a transparently wrong placeholder is safer than a
  # plausible one because nobody mistakes it for a design. An earlier attempt used `Crown`, which
  # would have made a fixture look like canon Crown structure.
  # ⚠ THIS ROW CARRIES NO `enforce:` TIER, AND AN EARLIER VERSION SET `enforce: off` ON THE
  # STATED GROUND THAT *"the naming guard must not nag about a fixture in prose"*. MEASURED
  # 2026-09-19: THAT NAG COULD NEVER HAVE FIRED. `tools/names.py: all_legacy` builds matchers
  # by iterating a row's `legacy:` list, and this row's is empty — so it contributes ZERO
  # matchers at every tier, and `off`, `warn`, `block` and omitting the field are
  # byte-identical here. The tier was a third enum value invented to solve a problem that did
  # not exist, and no validator would have caught that. Omitted rather than documented.
```

### factions: world.church — Church of Solmund ruling

*(original lines 332-338 at 8b57336, verbatim)*

```yaml
  # RULED by Jordan, 2026-09-13: "the church is Church of Solmund." This row said `Church` while
  # `engine/season/rosters.yaml: factions` said `Church of Solmund`, so two registries single-owned
  # one faction name and disagreed — a §8 violation that surfaced when `references/npc_registry.yaml`
  # (which uses the short form) was first read by executing code. `Church` becomes an ALIAS, not a
  # `legacy:` name: the gate enforces only `legacy` names, so the short form stays lawful prose and
  # nothing in the corpus is newly flagged. `patterns` is unchanged — a bare "Church" still MENTIONS
  # the faction, which is what that field is for.
```
