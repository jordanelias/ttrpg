# Dossier C1 — Personal attributes, aliases & aggregates

**Headline.** The corpus does not have a 7-vs-9 attribute-roster disagreement — it has (at least)
**four** mutually-incompatible attribute rosters live at once (7 / 9 / 10 / 10, three of which are
never cross-referenced by ED-IN-0008 or `CURRENT.md`), one of which (`Recall`) is a fully
load-bearing attribute with **zero** registry or names_index presence at all; the registry's own
"IN FLUX" fold decisions (Cognition→Acuity, Spirit→Will) are each contradicted by a *ratified* ED on
the live-consumer side (ED-899's Cognition-named Command formula; and literally 100% — not "most" —
of Spirit/Will-consuming formulas use "Spirit"); Health and Stamina each carry three
mutually-inconsistent formula values across surfaces that self-cite each other as authoritative; and
none of this is catchable by tooling because every attr/agg key sits at `enforce: warn` and
`glossary.md` (which independently carries wrong numbers) isn't even in the names_index MIRRORS
block. Two of the census's own row verdicts (Agility "ORPHANED"; Resonant Style's cited formula)
are also wrong and are corrected below.

---

## Trace narrative

### The roster itself: 4 incompatible tables, not 2

- `references/descriptor_registry.yaml:30-44` — 9 attributes (3 body/mind/social), IN FLUX, primary
  names Strength/Endurance/Agility/Focus/**Acuity**/**Will**/Attunement/Charisma/Bonds, aliases carry
  legacy names (Vitality, Dexterity, Reasoning/Cognition, Spirit, Perception, Influence/Presence,
  Sincerity/Affability). Line 39 flags its own Cognition→Acuity fold as `[ASSUMPTION] ... Jordan veto`.
- `references/glossary.md:33-41` — 7 attributes: Agility, Attunement, **Cognition**, Endurance,
  **Presence**, **Spirit**, Strength. **Missing Focus and Bonds entirely** — not "un-aliased," simply
  absent from the table. Glossary line 31 self-flags the conflict with descriptor_registry but only
  as a 7-vs-9 count; it does not know about the two 10-attribute tables below.
- `params/core.md:140-145` — **10 attributes**: Physical (Agility, Endurance, Strength) / Mental
  (**Cognition**, **Recall**, Focus) / Social (Attunement, Bonds, Charisma) / Metaphysical
  (**Spirit**). Line 138: "Point pool at creation: 31 points across **10 attributes**." Cognition and
  Recall and Focus are three *separate* Mental attributes here — Acuity does not exist as a name at
  all, and Spirit is its own category, not an alias of anything.
- `designs/architecture/canonical_registry.md:140` — a **second, independent** 10-attribute table,
  byte-similar to params/core.md's: "Physical: Agility, Endurance, Strength. Mental: Cognition,
  Recall, Focus. Social: Attunement, Bonds, Charisma. Metaphysical: Spirit." This file's banner
  (`canonical_registry.md:2`) marks it "PARTIALLY SUPERSEDED (combat rows)" only — the attribute
  table is **not** flagged stale — yet `CURRENT.md` never references this file (grep: zero hits), so
  the `CURRENT.md`-first workflow (CLAUDE.md §9 routing) can never surface it as a 4th roster.

None of these four cross-reference all the others. `references/names_index.yaml:44-58` mirrors only
the registry's 9, at `enforce: warn` throughout, and does not carry glossary's 7, or either 10-table's
extra name (`Recall`) or grouping. **Finding F1.**

### Recall — a real 10th attribute with zero registry footprint

`params/core.md:151`: "**Recall (Rec):** ... Sets the per-History point cap — a History can never
hold more points than the character's Recall score." Live, ratified consumers found in this sweep:

- History point cap (`params/core.md:151`)
- Fieldwork Research / Reconstruct actions (`params/core.md:245`)
- Contest **Appraise pool = Attunement + Recall** (`params/contest.md:23,90,141,288,302`; PP-614/ED-893
  "consolidates Read/Judge/Appraise into single canonical entry")
- Contest positional cap "+2D Recall" (`params/contest_extensions.md:57`)
- Southernmost pool `Cognition + Recall` and Research roll `Recall + History` (`params/southernmost.md:15,95`)
- `designs/architecture/canonical_registry.md:146`: "Histories ... Cap = Recall score."

`grep -c "Recall"` across `references/descriptor_registry.yaml` and `references/names_index.yaml`:
**zero** in both. Recall is not aliased to anything in the 9-roster (it isn't Acuity, isn't Focus) —
it is simply missing. This is worse than the registered-but-warn-tier 9: it has no registry presence
whatsoever despite gating a ratified pool formula (Contest Appraise) and a ratified action-cost cap
(Fieldwork/History). **Finding F2.**

### Cognition→Acuity fold vs the ratified Cognition-primary Command formula

`references/descriptor_registry.yaml:39` folds Cognition into Acuity as an `[ASSUMPTION]`, vetoable.
But `params/mass_combat.md:139`: `Command = clamp(round((2×Charisma+Cognition)÷3),1,7)` *(ED-899:
Charisma primary, Cognition secondary — engine `CMD_CHA_WEIGHT`=2 / `CMD_COG_WEIGHT`=1, leading
canon)*. Same formula repeated at `params/mass_combat.md:361,369`,
`designs/provincial/mass_battle_v30.md:266`. The literal engine constant names are
`CMD_CHA_WEIGHT`/`CMD_COG_WEIGHT` — `tests/sim/mass_battle/config.py:155-159`, commented "[canonical:
Jordan directive 2026-06-02 — Cognition SECONDARY weight in derived Command; class-B]". ED-899 is a
**ratified** decision treating "Cognition" as the durable name of a mental attribute in a currently-
canonical formula; descriptor_registry's fold is an **unresolved** assumption pending veto. These are
two Jordan-decision surfaces in direct tension, and neither ED cites the other. **Finding F3.**

### Will vs Spirit — exhaustive check, not just "sweep found"

`grep -rn "\bWill\b"` across `params/*.md`, `designs/scene/derived_stats_v30.md`, and
`combat_engine_v1/config.py` returns **zero** attribute-sense hits (only "Popular Will" clock and
prose "will harm"). Every load-bearing formula that touches this attribute uses "Spirit":
Stamina (`params/core.md:159`, `(3×Endurance)+(2×Spirit)`), Concentration (`params/contest.md:140`,
`(3×Focus)+(2×Spirit)`; engine constant `CONC_SPIRIT=2.0` at `combat_engine_v1/config.py:61`), Thread
Fatigue (`params/core.md:162`, `Spirit×5`), Thread-Read pool (`params/core.md:247`, `(Spirit×2)+...`),
Health's Wound Interval (`designs/scene/derived_stats_v30.md:67`, `WI=round(End+4+0.4×Spirit)`,
carried verbatim into `module_contracts.yaml:827-828` `inputs: ["Endurance","Spirit","Strength",...]`).
`module_contracts.yaml` is a machine contract — its `derivations.inputs` literally reads "Spirit," not
the registry's canonical name "Will" (`attr.mind.will`), and not through any alias-resolution step
visible in the contract itself. Any Godot importer binding fields by registry canonical name would
have to know to substitute "Spirit" for "Will" with no contract-local pointer telling it to. This
extends census F-REG-004 from "primary/load-bearing name inverted in practice" to **100% inverted,
zero exceptions found**. **Finding F4.**

### Health — three live, mutually inconsistent formulas, each citing the next as authoritative

1. `references/glossary.md:47`: `Health (HP*) = Endurance`. Flatly wrong under every generation of
   the formula this sweep found — not even the oldest documented form.
2. `params/core.md:158`: `(End+6) × (MW+1)`, and in the same line: "**See
   `designs/scene/derived_stats_v30.md` §4.1 as authoritative.**"
3. `designs/scene/derived_stats_v30.md:67` (§4.1, "AUTHORITATIVE (PP-716)", D-A update ED-1021,
   ratified 2026-06-18): `round(WI × (MW+1) + 0.25 × Strength × Endurance)`,
   `WI = round(End + 4 + 0.4 × Spirit)`. This is a **different number** from (2) — ED-1021 added the
   Spirit-weighted WI term and the Strength buffer specifically "to reduce uniformity"
   (`derived_stats_v30.md:59`), so (2)'s flat `(End+6)` is the pre-ED-1021 value.
   `references/module_contracts.yaml:827-828` implements formula (3) correctly (`inputs:
   ["Endurance","Spirit","Strength","cumulative_damage"]`, formula string matches verbatim).

`params/core.md`'s own header (`params/core.md:1`) is dated `v0.14 / 2026-04-04` and was never bumped
to reflect ED-1021 (2026-06-18) even though its Health row *names* the doc that supersedes it. Per
CLAUDE.md §5's own resolution path ("resolve the subsystem head via CURRENT.md → read the prose
param/design doc"), a reader who does exactly that lands on formula (2), not the true-authoritative
(3). **Finding F5** (extends the CLAUDE.md-baseline Combat-Pool triple-carry pattern to a second
derived value).

### Stamina — glossary carries a formula superseded twice over

`references/glossary.md:48`: `Stamina = Endurance + History + 1 (armour-modified)`.
`designs/scene/derived_stats_v30.md:505` documents the succession explicitly: `Stamina = End +
History + 1 − armour` → **superseded** by `End × 5` (ED-694) → **superseded** by RATIFIED S1
(2026-05-29) `(3×End)+(2×Spirit)`. The current formula is confirmed live at `params/core.md:159`,
`module_contracts.yaml:822` ("3*End+2*Spirit (full port; not in the slice)"), and
`combat_engine_v1/config.py` (Stamina is not a combat_engine_v1 state per se, but the ratified
formula is cross-cited there). Glossary's copy is thus **two supersessions behind**, despite its
header claiming a 2026-07-01 "maintenance pointer repaired" sweep and a 2026-04-30 content sweep
(PP-691) — neither touched this row. **Finding F6.**

### Focus — a name collision plus an internal self-contradiction

`references/descriptor_registry.yaml:38` — `Focus` is a mind `attribute_scalar`, 1-7, no aliases.
`references/glossary.md:52` (Derived Character Stats table) — a **different** row, also bare-named
"Focus," range **1–5+**, "Contact duration in Thread operation rounds" — filed as a *derived* stat,
not an attribute, in the same document whose own attribute table (`glossary.md:33-41`) omits "Focus"
altogether. Same word, different kind, different range, same file.

Separately, `params/core.md` disagrees with itself within 10 lines: line 152 ("**Focus (Foc):**
Concentration, discipline, precision under pressure. Governs Thread contact duration: Contact Rounds
= Focus score (range 1–7)") states the *original* rule, while line 162 (Derived Scores table, Thread
Fatigue row) states "Focus sets max operations per session (Focus − 1). (ED-694, **replaces Contact
Rounds = Focus**)" — the superseding rule. Line 152 is never marked struck/superseded even though
line 162 explicitly names it as replaced. **Finding F7.**

### Charisma/Influence vs fac.influence — a bare-string namespace collision

`descriptor_registry.yaml:43`: `Charisma` aliases include `Influence`. `descriptor_registry.yaml:65`:
`fac.influence` is an unrelated faction_stat (1-7 scale, faction domain). `names_index.yaml:52` and
`:61` both carry the literal string "Influence" — once as an attribute alias, once as a faction_stat
canonical name — with no namespace tag disambiguating them. Neither `ci_naming_check.py` nor
`ci_names_consistency.py` (keyed by registry `key:`, not display string) would catch prose that writes
bare "Influence" and lets a reader resolve it to the wrong scale's quantity. Same failure class as the
armature's C-INJ-12 `causes[]`/`cause_keys`/`origin_keys` unification (same word, different meaning,
no registry-level disambiguation). **Finding F11.**

### Aggregates — confirmed zero live consumers

`agg.body`/`agg.mind`/`agg.social` (`descriptor_registry.yaml:49-51`) appear only in: the registry
itself, `names_index.yaml:56-58` (warn-tier mirror), the **dead** `tests/registry/test_descriptor_registry.py`
(imports a module moved to `deprecated/`, defines no `test_*` function — CLAUDE.md baseline), and the
dead `deprecated/skills/valoria-orchestrator/scripts/descriptor_registry.py`. No design doc, params
table, module_contracts state/derivation, or engine config references `agg.*` anywhere. Census's
ORPHANED verdict for all three aggregates is confirmed correct.

### Correcting the census: Agility is not orphaned

Census row: "Agility ... status: ORPHANED ... no other consumer confirmed in this sweep." This is
wrong. `designs/scene/combat_v30.md:35` states explicitly that Agility "instead feeds the σ-leverage
TEMPO channel (initiative/quickness), not the pool size." Live engine constants:
`combat_engine_v1/config.py:54` `AGI_TEMPO_K=0.03` ("athleticism adds a little cadence"),
`combat_engine_v1/config.py:64` `REFLEX_AGI=2.0`. Live prose consumers beyond the engine:
`combat_v30.md:97-103` and `combat_design_v1.md:70,102-108,437,442` — Agility governs the Establish
Distance contest, Disarm Ob, Retrieve, Escape, disengage rolls, and the equal-Attunement initiative
tiebreaker. Agility was **redirected**, not orphaned. This is a finding against the census's
verification (build-state — "struck from one formula" — was miscast as a corpus-wide consumption
verdict, which the audit's own cardinal rule (b) warns against). **Finding F8.**

### Correcting the census: Resonant Style's cited "formula" is the wrong construct

Census row cites `designs/personal/conviction_track_v1.md:10-14`'s legacy 9-Conviction set
(Faith/Order/Reason/Equity/Precedent/Autonomy/Continuity/Community/Warden) as the enum Resonant Style
is "determined by." That taxonomy is explicitly superseded — `designs/npcs/npc_behavior_v30.md`'s own
blockquote (sourced from PP-684/PP-717) states "The legacy 9-Conviction set ... at `conviction_track_v1.md`
is superseded." More importantly, it is the wrong construct entirely: the actual canonical **Resonant
Style Taxonomy** is a 4-value enum — Evidence / Consequence / Authority / Solidarity
(`designs/npcs/npc_behavior_v30.md` §1.3, ~lines 32-38) — describing what an NPC is *vulnerable to*,
orthogonal to which Convictions (now the 13-set per `conviction_taxonomy_v30.md`, PP-684) the NPC
holds. `module_contracts.yaml:229-231`'s `g_scar2` gate ("Resonant Style X exposed") is consistent
with the real 4-style taxonomy. Recommend the census correct both the `formulas[].surface` citation
and reconsider the `kind: practitioner_stat` tag (Resonant Style is an NPC-conviction-vulnerability
construct, not a Thread-practitioner stat). **Finding F9** — a census-quality finding, filed here per
instructions to be adversarial with the census.

### Why none of this is CI-catchable (interlock restatement)

Every attr/agg/fac/set key in `names_index.yaml` is `enforce: warn` (verified across lines 44-73 —
no `enforce: block` anywhere in the attribute/aggregate/faction/settlement sections). The only
registry-specific test (`tests/registry/test_descriptor_registry.py`) is dead per CLAUDE.md baseline.
`glossary.md` (carrying its own independently-wrong Health/Stamina/Focus values, F5-F7) is outside the
names_index MIRRORS block entirely (glossary.md:31 self-admits this). `params/core.md` and
`canonical_registry.md` (the two 10-attribute tables, F1/F2) are not covered by any naming or roster
consistency check at all — they aren't even acknowledged as roster sources by the registry's own IN
FLUX note. The result: F1 through F9 above are all simultaneously true and none of them can trip a
CI gate today. **Finding F10.**

---

## Findings table

| ID | Sev | Kind | Calibration | Claim | Evidence |
|----|-----|------|-------------|-------|----------|
| F1 | P1 | collision | KNOWN-UNTRACKED (adjacent: ED-IN-0008) | Four incompatible attribute rosters (7/9/10/10) coexist; ED-IN-0008 only names 2 of the 4, and `CURRENT.md` never indexes `canonical_registry.md` | descriptor_registry.yaml:30-44; glossary.md:33-41; params/core.md:140-145; canonical_registry.md:140,2 |
| F2 | P2 | unregistered | NEW | `Recall` is a load-bearing 10th attribute with zero descriptor_registry/names_index presence, gating History caps + ratified Contest/Fieldwork/Southernmost pools | params/core.md:151,245; params/contest.md:23,90,141,288,302; contest_extensions.md:57; southernmost.md:15,95 |
| F3 | P1 | collision | NEW | ED-899 ratifies "Cognition" as primary in a live Command formula, directly contradicting descriptor_registry's own unresolved `[ASSUMPTION]` Cognition→Acuity fold | descriptor_registry.yaml:39; mass_combat.md:139,361,369; mass_battle_v30.md:266; tests/sim/mass_battle/config.py:155-159 |
| F4 | P1 | collision/key-binding-gap | KNOWN-TRACKED (ED-IN-0008) | 100% (not "most") of live formulas use "Spirit," never "Will"; module_contracts.yaml's machine-readable `derivations.inputs` names "Spirit" with no alias-resolution step visible in the contract | grep sweep, params/*, derived_stats_v30.md:67; module_contracts.yaml:827-828 |
| F5 | P1 | stale/export-drift | NEW | Health has 3 mutually inconsistent live formulas; params/core.md cites derived_stats_v30 as authoritative while printing the pre-ED-1021 value itself | glossary.md:47; params/core.md:158,1; derived_stats_v30.md:59,67; module_contracts.yaml:827-828 |
| F6 | P1 | stale | NEW | glossary.md's Stamina formula is two supersessions behind the ratified RATIFIED-S1 value | glossary.md:48; derived_stats_v30.md:505; params/core.md:159; module_contracts.yaml:822 |
| F7 | P2 | collision/stale | NEW | "Focus" names both the mind attribute (1-7) and an unrelated glossary "derived stat" (1-5+); params/core.md carries the pre-ED-694 Focus rule alongside the rule that replaces it | descriptor_registry.yaml:38; glossary.md:33-41,52; params/core.md:152,162 |
| F8 | P3 | other (census error) | NEW | Census's "Agility: ORPHANED" verdict is wrong — Agility is a live tempo/initiative/maneuver consumer, redirected not removed | combat_v30.md:35,97-103; combat_engine_v1/config.py:54,64; combat_design_v1.md:70,102-108,437,442 |
| F9 | P3 | other (census error) | NEW | Census's Resonant Style "formula" cites the superseded 9-Conviction taxonomy instead of the actual canonical 4-value Resonant Style Taxonomy | conviction_track_v1.md:10-14 (superseded, per npc_behavior_v30.md blockquote); npc_behavior_v30.md §1.3; module_contracts.yaml:229-231 |
| F10 | P2 | enforcement-gap | KNOWN-TRACKED (CLAUDE.md baseline; tests/registry dead test) | F1-F9 are all simultaneously uncatchable by CI: every attr/agg key is warn-tier, glossary is outside MIRRORS, the two 10-attribute tables aren't covered by any roster check at all | names_index.yaml:44-73; tests/registry/test_descriptor_registry.py; glossary.md:31 |
| F11 | P2 | synonym/collision | NEW | Bare string "Influence" collides between attr.social.charisma's alias and the unrelated fac.influence faction_stat, with no namespace disambiguation | descriptor_registry.yaml:43,65; names_index.yaml:52,61 |

## Unification options (Jordan-rulable)

| ID | What | Recommended default | Feeds |
|----|------|---------------------|-------|
| U1 | Which attribute roster is canonical: glossary's 7, registry's 9, or either 10-table? | Adopt the registry's 9 **plus Recall as a 10th key** (`attr.mind.recall`); retire glossary's Part-One tables and reconcile `canonical_registry.md`'s table to match or mark it superseded | workplan v6 T1 queue-13; ED-IN-0008 |
| U2 | Cognition→Acuity fold: proceed or reverse? | Reverse — keep "Cognition" as the durable attribute name; ED-899 already ratified it live with named engine constants, so folding it now requires an unwind, not a wait | descriptor_registry.yaml:39 `[ASSUMPTION]`; ED-IN-0008 |
| U3 | Will vs Spirit primary name | Flip registry primary to "Spirit" — zero live formula, zero engine constant, and zero design doc uses "Will"; the rename cost is 100% on the registry side, not the corpus | ED-IN-0008 |
| U4 | params/core.md's stale Health/Stamina rows | Regenerate params/core.md's Derived Scores table (lines 158-165) verbatim from derived_stats_v30.md §4.1/4.2 so the doc that names itself non-authoritative stops printing a different number | CLAUDE.md §5 pipeline; values_master regenerate-vs-retire (2026-07-01 queue item 17, adjacent) |
| U5 | glossary.md's Part One formula content (Health/Stamina/Focus rows) | Strip formulas/ranges from glossary's attribute and derived-stat tables entirely — glossary's own charter (glossary.md:1-8) is abbreviation expansion, not mechanical authority; point to params/core.md + derived_stats_v30 instead | ED-IN-0008; the glossary-mirror tooling gap glossary.md:31 already flags |
| U6 | `attr.social.charisma` alias "Influence" vs `fac.influence` | Either drop "Influence" as a Charisma alias (Presence covers the same ground) or add an explicit registry-level scope tag distinguishing personal-attribute vs faction-stat senses of the bare word | ED-IN-0008 (naming-authority conflict, adjacent) |

## Registry delta candidates

- `attr.mind.recall` — new `attribute_scalar` key; currently zero presence in descriptor_registry.yaml
  or names_index.yaml despite gating ratified Contest/Fieldwork/History/Southernmost formulas (F2).
- A `formula_pointer` field on `not_descriptors.derived_values` entries (Health, Stamina, Concentration,
  Thread Fatigue) naming the ONE authoritative section (e.g. `derived_stats_v30.md §4.1`) so
  params/core.md and glossary.md stop re-transcribing and drifting (F5, F6, F7).
- A scope/domain tag on `by_reference`/attribute aliases to disambiguate bare-word collisions across
  domains (e.g. "Influence" as attribute alias vs faction_stat) — the alias list currently has no
  mechanism to flag "this alias string is also used elsewhere for something unrelated" (F11).
- Thread Sensitivity (`practitioner_stat`, already flagged unregistered in the audit's verified
  baseline) — restated here as the analogous registry gap to Recall; both are load-bearing personal-
  scale quantities with zero registry key.
