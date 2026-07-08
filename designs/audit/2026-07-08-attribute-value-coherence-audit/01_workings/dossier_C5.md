# Dossier C5 — Faction & Settlement Stats + Mandate Seam

Faction stats (Influence/Wealth/Military/Intel/Stability, 1-7) and settlement stats
(Legitimacy/Popular Support/Prosperity/Defense/Order) are individually well-registered
(`descriptor_registry.yaml`), but the derived layer built on top of them is where this cluster's
real coherence debt lives: the registry's own "not_descriptors" inventory silently drops most of
the faction-scale derived meters it claims to catalog (Treasury, Reputation, Discipline, Levies
Available, Intelligence Holdings) and one settlement one (Public Order); the settlement-scale
derived formulas (Local Economy/Garrison Strength/Public Order) are consumed as CANONICAL by
`module_contracts.yaml` (status: extracted, live gates) while their own home doc
(`derived_stats_v30.md §9`/`§14.1`) still stamps them **PENDING — Not canonicalized**, and their
citation chain resolves through a **nonexistent** file (`derived_stats_v1`); "Fort Level," feeding
that same Garrison Strength formula, turns out to be a **province/territory-tier** stat (0-4, 17
T-nodes) silently blended with a **settlement-tier** Defense stat (0-5, 37 nodes) with no doc
specifying the settlement↔province Fort-Level inheritance; "Discipline" is a live, load-bearing
name collision between a per-unit mass-battle stat (1-7, formation coherence, `mass_battle_v30`)
and the unrelated faction-derived meter (Stability×10) that nothing in the corpus disambiguates;
and Mandate remains genuinely bimodally defined (linear vs saturating) exactly as the census found,
with the linear form's own citation now stale against its cited source. Two items in the supplied
census turned out, on inspection of the working tree, to be **wrong**: the Military footnote-staleness
finding is confirmed verbatim, but the "Public Support" residual the census cites at
`settlement_layer_v30.md:631` does not exist there (that line correctly reads "Popular Support") —
the real, still-live residual is two rows in `references/mechanical_terms_index.md` that the tracking
ledger never looked at.

## Trace narrative (quantity by quantity)

### Faction stats: Influence, Wealth, Military, Intel, Stability
`references/descriptor_registry.yaml:61-70` declares one block, `faction_stats: {scale: "1-7", source:
params/factions/stats_1_7_scale.md, entries: [fac.influence, fac.wealth, fac.military, fac.intel,
fac.stability]}` — five keys, single scale string for all five. `references/glossary.md:105-109`
carries the semantic notes (Influence "cannot drop below 1"; Wealth "0 = cannot Trade"; Military "0 =
cannot Muster"; Intel no floor note; Stability "0 = Collapse trigger"). `params/bg/core.md:200-207`
("Stat Ceilings and Floors") gives explicit per-stat floors: Legitimacy 0, Popular_Support 0,
**Influence 1**, **Wealth 0**, **Military 0**, **Stability 0** — and **omits Intel entirely**. So the
registry's blanket `scale: "1-7"` (which literally reads as floor=1 for all five) contradicts its own
cited `source` doc's explicit floor table for four of five stats, and Intel has no independently
declared floor/ceiling anywhere in the corpus I could find (register says 1-7 by inheritance from the
blanket declaration only). `module_contracts.yaml:88` collapses all five into one `"faction stats 1-7"`
track entry (comment: "Military/Stability/etc."), i.e. the contract layer doesn't carry per-stat
identity or bounds at all — a coarser granularity than either the registry or the params floor table.
`module_contracts.yaml:606` derives faction Treasury income from settlement Prosperity, cross-checked
below.

Military specifically: `params/bg/core.md:165` states Crown Military = 5 in the v04 B5 starting-stats
table, with a footnote at `params/bg/core.md:172` reading "...UNRESOLVED (Jordan): Crown Military
here=5 CONFLICTS with stats_1_7_scale.md=4 (direction undetermined). See ED-869." But
`params/factions/stats_1_7_scale.md:19` already shows Crown Military = **5/6** with an inline note
"prior value 4 struck per ED-869 / Jordan 2026-05-31" — one calendar day **after** the `bg/core.md`
reconciliation-comment date (2026-05-30). The `bg/core.md` footnote is stale relative to the very
resolution it cites; this confirms the census's claim verbatim (census row: Military). NEW residual:
the footnote itself, not the underlying conflict (ED-869 is closed).

### Settlement stats: Legitimacy, Popular Support, Prosperity, Defense, Order
`references/descriptor_registry.yaml:76-82` registers `set.legitimacy` (0-7), `set.popular_support`
(0-7), `set.prosperity` (0-5), `set.defense` (0-5), `set.order` (0-5), sourced to
`designs/territory/settlement_layer_v30.md §1.8`. `designs/territory/settlement_layer_v30.md:147-179`
(§1.8, LPS-2e, Jordan ruling 2026-05-30) is a well-formed, self-consistent, internally-cross-referenced
section: it explicitly re-grains L/PS from faction-level (PP-686 v2) to per-settlement, defines Weight
`W_s = base(Type) + Prosperity_s + FacilityTier_s` with base(Type) values enumerated per settlement
type (Seat 3, City 3, Cathedral 3, Town 2, Fortress 2, Port 2, Village 1, Mine 1, Outpost 1) and
FacilityTier_s tied explicitly to §1.4's facility ladder (0-3). **Census correction:** the supplied
census row for "Settlement weight inputs (FacilityTier, base(Type), W_s)" calls its `defining_surface`
"AMBIGUOUS: no owning module" — that's wrong. §1.8 unambiguously owns and defines these terms in
prose. The real gap is narrower than "ambiguous": `module_contracts.yaml`'s `settlement_layer` module
`state:` block (lines 556-559) never declares `base(Type)`, `FacilityTier_s`, or `W_s` as state or
derivation outputs of their own — they appear only inline inside the Mandate derivation formula
(`module_contracts.yaml:598-601`). So the finding is **unregistered-in-the-contract-layer**, not
undefined-in-prose; the census's "AMBIGUOUS" framing overstates the gap.

`designs/provincial/faction_behavior_v30.md:8` and `designs/provincial/faction_canon_v30.md:9` both
carry an ED-FA-0004 (2026-07-07) implementation note that `sim/autoload/game_state.py` still models
`Faction = {L, Sta, W, I, Mil}` (faction-level L, no Mandate/PS/Treasury/αβγ engine) — this is
build-state (routing metadata per audit rule (b)), already KNOWN-TRACKED via the note's own ED-FA-0004
citation; not re-argued here.

`faction_behavior_v30.md:227-229` (§3.4 Popular Support) and `:285-287` (§3.5 Legitimacy) both retain
their full pre-LPS-2e per-territory dynamics tables beneath a one-line "[SUPERSEDED-BY LPS-1
(settlement_layer_v30 §1.8)...]" banner rather than being rewritten or struck — confirms the census's
divergence claim verbatim.

**"Public Support" residual — census claim does not hold at the cited location.** The census (and its
source, `references/name_collision_database.yaml:469`, `deprecated_term_residual`) claims the
deprecated term "Public Support" is still live at `settlement_layer_v30.md:631`. On inspection,
`settlement_layer_v30.md:631` reads `| Popular Support (PS) | 3 | Grass-roots base anchored by
founding NPC officers. |` — already correctly renamed. A repo-wide, case-insensitive grep for "public
support" turns up **zero** hits in `settlement_layer_v30.md`. The tracked residual is stale (the file
was fixed after the ledger entry was written, or the entry was wrong from authoring) and nobody
re-verified it against disk before both the ledger and the census repeated it — a small but concrete
instance of exactly the anti-pattern this audit's CLAUDE.md instructs against ("never trust memory or
summaries over disk"). The underlying problem is real, just mislocated: `references/mechanical_terms_index.md:196`
and `:1167` both still define **"Public Support (PS)" as canonical**, describing it as "Outcome
accumulator from Mission/Domain Action outcomes... faction_behavior §3.4" — i.e. carrying forward both
the deprecated *name* and the superseded *pre-LPS-2e conceptual model* (faction-level accumulator, not
the current per-settlement 0-7 track). This is the actual live residual; it is untracked at its real
location.

### Mandate (bimodal definition)
Confirmed exactly as census states, with citations verified: `params/factions_personal.md:14` gives
the LINEAR form `round(0.5*Legitimacy + 0.5*Popular_Support)`, explicitly citing "faction_behavior_v30
§4" as its source. But the *current* text of that very section —
`designs/provincial/faction_behavior_v30.md:398-410` (§4, "REVISED by LPS-2e") — defines the SATURATING
form: `q_s=0.5·L_s+0.5·PS_s; W_s=base(Type)+Prosperity_s+FacilityTier_s; T=Σ W_s·(q_s/7);
Mandate=clamp(round(7T/(T+6)),0,7)`. The same saturating form is independently corroborated at
`designs/provincial/faction_canon_v30.md:213-216` and `references/module_contracts.yaml:598-601`
("Stage-4 sim bounded 0-7 over 30 seasons," Lesson-5 bound) — three independent surfaces vs. one
(`factions_personal.md:14`) whose own citation no longer matches what it cites. This is a live,
undecidable-by-an-engine-consumer P1: a Godot importer resolving Mandate via `factions_personal.md`
alone gets the wrong (and structurally simpler, unweighted) formula.

`derived_stats_v30.md:297` and `settlement_layer_v30.md:174-175` both independently confirm the
**Faction Legitimacy (derived) = Mandate × 20** meter is a *third*, differently-scaled "Legitimacy"
(0-140 buffer) layered on top of the *settlement*-scale Legitimacy stat (0-7) — this exact collision is
already flagged by the supplied census under its C2 cross-cluster row ("Faction Legitimacy (derived
meter)," line 212-214 of `quantity_census.md`); cited here as corroboration, not re-litigated as a new
finding.

### Local Economy / Garrison Strength / Public Order — canonicity is circular and partly broken
`designs/territory/settlement_layer_v30.md:43-45` states: "**Derived values (derived_stats_v1 §4):**
Settlement stats... produce derived values for the videogame layer" and cites "derived_stats_v1" as
source for the Local Economy/Garrison Strength/Public Order formulas. **`derived_stats_v1` does not
exist anywhere in the working tree** (`find -iname "derived_stats*"` returns only
`derived_stats_v30.md`, `derived_stats_v30_index.md`, and an unrelated audit file) — this citation is
broken. Meanwhile the *actual* current doc, `designs/scene/derived_stats_v30.md:372-380` (§9,
"Settlement Scale (PENDING)"), gives the identical three formulas and explicitly states: "Multipliers
and interaction design pending settlement_v30 development. **Not canonicalized.**" The same disclaimer
repeats at `derived_stats_v30.md:551-554` (§14.1 table, "PENDING" direction column for all three
settlement rows). So the two docs that should establish canonicity for these three formulas point at
each other in opposite, broken directions: `settlement_layer_v30` cites a nonexistent `derived_stats_v1`
as its source, while the real `derived_stats_v30` disclaims the same formulas as not-yet-canonical and
waiting on `settlement_v30` (which, per its own approval date 2026-04-17, already happened one day
*before* `derived_stats_v30`'s 2026-04-18 date). Despite this, `references/module_contracts.yaml:556-597`
treats all three as `status: extracted`, wires three live gates on them (`g_ord0`, `g_def0`, `g_dv0`),
and cites only `settlement_layer_v30 §1.3` — never noticing the sibling doc's PENDING disclaimer. This
is a P1: an engine consumer reading `module_contracts.yaml` alone would treat Local
Economy/Garrison Strength/Public Order as settled canon; reading `derived_stats_v30.md` alone says the
opposite.

`designs/provincial/clock_registry_v30.md:59` lists "Prosperity | 1–7 | ...params_board_game.md
§Territory Table" (**territory/BG-tier** Prosperity) in its "Per-Territory Tracks" section, then three
rows later (`clock_registry_v30.md:139-141`, "Settlement Derived Values") computes "Local Economy |
0–250 | Prosperity × 50 | settlement_layer_v30 §1.3" using a **different, settlement-tier** Prosperity
(0-5 per the registry). 5×50=250 checks out only under the settlement-scale (0-5) Prosperity, not the
1-7 territory-scale one two table-rows above it in the *same document* — the word "Prosperity" carries
two incompatible scales inside one file with no disambiguation between the two table sections. Also in
that same row block: "Garrison Strength | 0–250 | Defense × 20 + Fort Level × 30" — with Defense capped
at 5 (0-5, `descriptor_registry.yaml:81`) and Fort Level capped at 4 (`clock_registry_v30.md:61`, "Fort
Level | 0–4"), the arithmetic maximum is 5×20 + 4×30 = **220**, not 250 as stated — a minor
declared-vs-computed ceiling mismatch (P3).

### Fort Level — cross-scale binding gap (beyond the census's "unregistered" framing)
The census correctly flags Fort Level as `unregistered` (never a `state:` entry anywhere), but misses
the more serious problem: Fort Level is explicitly a **province/territory**-tier stat.
`settlement_layer_v30.md:22`: "All existing province-level mechanics (Accord, Piety Track, TCV, **Fort
Level**, Calamity radiation, adjacency) continue to operate at the province level." It is tracked per
one of the **17** T-nodes (`params/bg/geography.md:8-25`, e.g. "T3 | Lowenskyst | Crown | 3 | 3... Fort
max 4"), range 0-4 (`clock_registry_v30.md:61`). Yet the Garrison Strength formula that consumes it
(`settlement_layer_v30.md:48`, `module_contracts.yaml:591-592`) is declared as a **settlement**-scale
derived value (keyed off settlement Defense, one of the **37** settlements per §1.8's own
disambiguation of the two-tier map). No doc anywhere specifies how a settlement inherits "its"
province's Fort Level (1:1? does every settlement in a 3-settlement province see the same Fort 3? does
Fort Level itself need re-graining the same way L/PS were re-grained under LPS-2e?). This is the same
species of problem LPS-2e already solved once for L/PS and never got applied to Fort Level — a
genuinely NEW P2 finding, not previously tracked.

### Accord — answering the FOCUS question directly
Per `module_contracts.yaml:558`: `{name: "province Accord", bucket: derived_value, writable: false}`.
Per `settlement_layer_v30.md §1.3` (revised) and `module_contracts.yaml:571-575` (derivation
`floor(mean settlement Order)`): Accord is a **pure derived value**, not a stat and not a direct-write
delta target — full stop. `designs/provincial/peninsular_strain_v30.md:68` states this plainly:
"Prior direct-assignment rules (§2.3–2.4) now operate by modifying settlement Order values, which
cascade upward," and §2.5 (`peninsular_strain_v30.md:216-242`) gives an explicit Category A/Category B
redirect table mapping every "Accord set to N" / "Accord ±N" legacy rule onto an actual settlement
Order write. **But** `designs/architecture/scale_transitions_v30.md §5.5` (Domain Echo, lines
201-214) — the Key/Echo-armature-layer doc this audit is scoped to extend — still phrases its own
table in direct-delta language: "Accord +1 in that territory (queued to next Accounting)" /
"Accord −1 in that territory" (lines 209-212), and its one reconciliation sentence (line 208, "Accord
changes from personal scenes target the settlement... Province Accord recalculates at Accounting:
floor(mean(settlement Order))") never states outright that the write itself lands on settlement Order
— unlike `peninsular_strain_v30 §2.7` (lines 183-196), which does say plainly "the player's personal
actions can also affect Accord via Domain Echo... Cap: ±1 Order per settlement per season." The
Domain-Echo-layer doc is the one surface in the corpus that still reads as if Accord itself is
directly writable. Not behaviorally broken (peninsular_strain's redirect governs in practice) but a
real clarity/consistency gap in exactly the doc this audit's armature framing cares about most.

### Discipline — a genuine, load-bearing name collision (NEW, not in census)
`designs/scene/derived_stats_v30.md:298-360` (§8, §14.1) defines faction-scale **Discipline = Stability
× 10** (0-70 derived buffer, drains from failed Stability checks, census row confirmed at line 47 of
`quantity_census.md`). Separately, `designs/provincial/mass_battle_v30.md:154-236` (§A.2-A.4, ED-1019/
1020/1022/1026) defines **unit-scale Discipline (1-7)**, "organisational integrity," starting value =
`min(general's Command, ...)`, degrading when cumulative Size loss exceeds current Discipline, gating
Effective Power penalties, formation-hold speed, and per-sub-unit rout — a completely different
quantity, different scale, different owning module (`mass_battle`, not `faction_state`), with its own
extensive mechanical apparatus. Both are live/canonical, both use the bare word "Discipline" with zero
cross-reference or disambiguation anywhere in either doc, `descriptor_registry.yaml`, or
`references/glossary.md`. This is exactly the "explosion of attributes... developed in silos" pattern
the audit was chartered to find, and it is not present in the supplied census at all (checked: census's
only "Discipline" rows are lines 30 and 47, both faction-scale only).

### Registry's own derived-value inventory is materially incomplete (NEW)
`descriptor_registry.yaml:106-114` ("not_descriptors," meant to be the exhaustive catalog "so consumers
do not mistake them for registry-bound descriptors") lists `derived_values: [Health, Stamina, Composure,
Concentration, Thread Fatigue, Resolve, Garrison Strength, Local Economy, Mandate]` — 9 entries. But
`derived_stats_v30.md §14.1` (lines 533-547, the doc `descriptor_registry.yaml` itself does not cite
but which CLAUDE.md's §7/armature framing treats as the authoritative engine value map) tables at least
16 distinct derived values: the registry's 9, plus TroopCount, **Legitimacy (derived, ×20)**,
**Treasury (×100)**, **Levies Available (×2, ceiling)**, **Reputation (×15)**, **Discipline (×10)**,
**Intelligence Holdings (PENDING, ×Intel derive-on-use)**, and **Public Order (×20)** — eight items
entirely missing from the registry's catalog. Every one of the five faction-scale derived meters
(Legitimacy/Treasury/Levies/Reputation/Discipline) that this cluster's own FOCUS calls out is *absent*
from the registry's supposedly-exhaustive not_descriptors list. The census (line 47 of
`quantity_census.md`) marks the Treasury/Reputation/Discipline/Levies Available row `registered:
not_descriptors` and status `COHERENT` — that registration claim is **false**: none of those four names
appear at `descriptor_registry.yaml:107`. This is a finding against the census (mischaracterized
registration state) as well as a standalone NEW finding against the registry (incomplete inventory).
"Intelligence Holdings" additionally appears nowhere in the 88-row census at all — an orphaned,
uncensused derived value.

### BG-mode vs. registry stat divergence
Cross-checking `params/bg/core.md:165-171` (v04 B5 table) against `params/factions/stats_1_7_scale.md:19-25`
(BG columns) for all factions: Crown, Church, Hafenmark, Varfell, and Guilds match exactly across both
tables once the Military footnote-staleness (above) is set aside. **Löwenritter does not match:**
`bg/core.md:170` gives Löwenritter Wealth = 3 explicitly ("Löwenritter (Split) | 3 | 3 | 2 | 3 | 5 | 3 |
5" → L3/PS3/I2/W3/Mil5/Int3/Sta5), while `stats_1_7_scale.md:19-25`'s Löwenritter row shows **W(BG) = "—"**
(dash, no value) — one doc asserts a concrete Wealth value for the embedded/split faction, the other
declares it explicitly undefined. This is a small (P3) but real, previously-uncaptured BG-vs-registry-
source divergence — narrower than "does BG diverge from the registry's scale" (it doesn't, floors/
ceilings are shared) but real at the level of "does a specific faction's specific stat have an agreed
value across the two authoring surfaces" (it doesn't, for Löwenritter Wealth).

## Findings

| ID | Sev | Kind | Calib. | Claim | Evidence |
|---|---|---|---|---|---|
| C5-F1 | P1 | export-drift | NEW | Mandate is bimodally defined and one form's citation is now stale against its own cited source: `params/factions_personal.md:14` gives the LINEAR form citing "faction_behavior_v30 §4," but that section's current text (`faction_behavior_v30.md:398-410`) plus `faction_canon_v30.md:213-216` plus `module_contracts.yaml:598-601` all give the SATURATING, size-weighted, Stage-4-sim-validated form — 3 independent surfaces vs. 1 stale one. | params/factions_personal.md:14; designs/provincial/faction_behavior_v30.md:398-410; designs/provincial/faction_canon_v30.md:213-216; references/module_contracts.yaml:598-601 |
| C5-F2 | P1 | export-drift | NEW | Local Economy/Garrison Strength/Public Order have circular, broken canonicity: `settlement_layer_v30.md:43-45` cites a nonexistent file `derived_stats_v1 §4` as source; the real `derived_stats_v30.md §9`/§14.1 (lines 372-380, 551-554) explicitly disclaims the identical formulas as "PENDING... Not canonicalized"; `module_contracts.yaml:556-597` nonetheless treats them `status: extracted` with 3 live gates wired on them. | designs/territory/settlement_layer_v30.md:43-45; designs/scene/derived_stats_v30.md:372-380,551-554; references/module_contracts.yaml:556-597 |
| C5-F3 | P1 | collision | NEW | descriptor_registry.yaml declares one blanket `scale: "1-7"` for all 5 faction stats (Influence/Wealth/Military/Intel/Stability), but its own cited `source` doc's floor table (`params/bg/core.md:200-207`) gives per-stat floors of 0 for Wealth/Military/Stability and 1 only for Influence — and omits Intel's floor/ceiling entirely. A Godot consumer trusting the registry's blanket scale alone would clamp Wealth/Military/Stability at the wrong floor (1 instead of 0). | references/descriptor_registry.yaml:62-70; params/bg/core.md:200-207; references/glossary.md:105-109 |
| C5-F4 | P2 | collision | NEW | "Discipline" is a live, load-bearing name collision between a per-unit mass-battle stat (1-7, organisational integrity, extensive rout/formation mechanics, `mass_battle_v30.md:154-236`) and the unrelated faction-scale derived meter (Stability×10, `derived_stats_v30.md §8/§14.1`). Neither doc, the registry, nor the glossary cross-references or disambiguates the two. Not present in the supplied census. | designs/provincial/mass_battle_v30.md:154,169,224; designs/scene/derived_stats_v30.md:298,545 |
| C5-F5 | P2 | enforcement-gap | NEW | descriptor_registry.yaml's `not_descriptors.derived_values` list (meant to be the exhaustive derived-value catalog) has only 9 of the ~16 derived values `derived_stats_v30.md §14.1` actually tables — missing all 5 faction-scale meters this cluster is about (Legitimacy-derived, Treasury, Levies Available, Reputation, Discipline) plus Intelligence Holdings and Public Order. The census (row 47) marks these `registered: not_descriptors` / COHERENT — that registration claim is false on inspection of the registry file. | references/descriptor_registry.yaml:106-114; designs/scene/derived_stats_v30.md:533-547; designs/audit/2026-07-08-attribute-value-coherence-audit/02_census/quantity_census.md:47 |
| C5-F6 | P2 | key-binding-gap | NEW | Fort Level is a province/territory-tier stat (0-4, one of 17 T-nodes, `settlement_layer_v30.md:22`, `clock_registry_v30.md:61`, `params/bg/geography.md`) consumed by the Garrison Strength formula as if it were available per-settlement (one of 37 settlements, `settlement_layer_v30.md:48`, `module_contracts.yaml:591-592`) — no doc specifies the province→settlement Fort-Level inheritance mapping. Same class of gap LPS-2e already solved once for L/PS, left unresolved here. | designs/territory/settlement_layer_v30.md:22,48; references/module_contracts.yaml:591-592; designs/provincial/clock_registry_v30.md:61; params/bg/geography.md:8-25 |
| C5-F7 | P2 | stale | NEW | The tracked "Public Support" deprecated-term residual (`references/name_collision_database.yaml:469`) cites `settlement_layer_v30.md:631` — but that line already correctly reads "Popular Support"; a corpus-wide grep finds zero "Public Support" in that file. The census (line 166 of `quantity_census.md`) repeats the stale claim without re-verifying against disk. The real, untracked residual is `references/mechanical_terms_index.md:196` and `:1167`, which still define "Public Support (PS)" as canonical, carrying forward both the deprecated name and the superseded pre-LPS-2e conceptual model (a faction-level accumulator). | references/name_collision_database.yaml:469; designs/territory/settlement_layer_v30.md:631; references/mechanical_terms_index.md:196,1167; designs/audit/2026-07-08-attribute-value-coherence-audit/02_census/quantity_census.md:166 |
| C5-F8 | P2 | other | NEW | The Domain Echo layer (`designs/architecture/scale_transitions_v30.md §5.5`, lines 201-214) — the armature seam this audit is chartered to extend — still phrases Accord changes as direct deltas ("Accord +1 in that territory"), while the doc that actually governs Accord (`peninsular_strain_v30.md §2.5/§2.7`, lines 216-242, 183-196) explicitly redirects every such write to settlement Order. Accord is a pure `derived_value, writable: false` (`module_contracts.yaml:558`) — not a stat, not a delta target. Not behaviorally broken (peninsular_strain governs in practice) but the one doc that should say "this writes to Order" doesn't. | designs/architecture/scale_transitions_v30.md:201-214; designs/provincial/peninsular_strain_v30.md:68,183-196,216-242; references/module_contracts.yaml:558 |
| C5-F9 | P3 | other | NEW | Declared vs. computed ceiling mismatch and scale ambiguity in one table: `clock_registry_v30.md:139-141` states Garrison Strength range "0–250" but the arithmetic max under canonical bounds (Defense 0-5 × 20 + Fort Level 0-4 × 30) is 220; the same doc's "Prosperity" appears at two different scales three rows apart (territory-tier 1-7 at line 59 vs. settlement-tier 0-5 feeding Local Economy at line 140) with no disambiguation. | designs/provincial/clock_registry_v30.md:59,139-141; references/descriptor_registry.yaml:80,81 |
| C5-F10 | P3 | stale | NEW | Löwenritter Wealth diverges between BG authoring surfaces: `params/bg/core.md:170` gives Wealth=3 explicitly, `params/factions/stats_1_7_scale.md:19-25`'s W(BG) column shows "—" (undefined) for the same faction. | params/bg/core.md:170; params/factions/stats_1_7_scale.md:19-25 |
| C5-F11 | P3 | other | NEW (census correction) | The supplied census's "Settlement weight inputs (FacilityTier, base(Type), W_s)" row calls its defining surface "AMBIGUOUS: no owning module" — this overstates the gap. `settlement_layer_v30.md §1.8` (lines 159-165) unambiguously defines all three in prose (base(Type) per settlement type, FacilityTier tied to §1.4). The real, narrower gap is that `module_contracts.yaml`'s settlement_layer `state:` block never declares them as state/derivation entries of their own — an under-registration in the contract layer, not an undefined term in prose. | designs/territory/settlement_layer_v30.md:159-165; references/module_contracts.yaml:556-601; designs/audit/2026-07-08-attribute-value-coherence-audit/02_census/quantity_census.md (Settlement weight inputs row) |
| C5-F12 | P3 | stale | NEW | `params/factions/stats_1_7_scale.md`'s own "Starting Stats" table (lines 15-19) carries per-faction L/PS columns without any note that these are now merely per-settlement SEED values (per the LPS-2e migration note at `faction_behavior_v30.md:410`), even though the same file's header (line 3) explicitly states the faction lineup is 6-stat and excludes L/PS. `params/bg/core.md:160` self-documents the seeding rationale inline; `stats_1_7_scale.md` does not, despite being the doc the registry cites as its faction_stats `source`. | params/factions/stats_1_7_scale.md:3,15-19; designs/provincial/faction_behavior_v30.md:410; params/bg/core.md:160; references/descriptor_registry.yaml:63 |
| C5-F13 (KNOWN-TRACKED, confirmed) | P3 | stale | KNOWN-TRACKED | `params/bg/core.md:172`'s Crown-Military footnote is stale relative to its own cited resolution: it reads "UNRESOLVED... See ED-869" dated 2026-05-30, but `stats_1_7_scale.md:19` shows the ED-869 resolution (5/6, dated 2026-05-31, one day later) already applied. The underlying conflict (ED-869) is closed; only the footnote's staleness is new. | params/bg/core.md:165,172; params/factions/stats_1_7_scale.md:19 |

## Unification options (Jordan-rulable)

| ID | What | Recommended default | Feeds |
|---|---|---|---|
| C5-U1 | Retire the LINEAR Mandate formula from `params/factions_personal.md:14`, replacing its citation with the current SATURATING form (or a pointer to `settlement_layer_v30 §1.8`), so there is exactly one Mandate definition in the corpus. | Adopt the saturating form as sole canon (already the 3-surface consensus + Stage-4 sim validated); rewrite `factions_personal.md:14` to match. | workplan v6 T1 queue-13 (attribute-roster ratification); values_master regenerate-vs-retire (queue item 17) |
| C5-U2 | Resolve the Local Economy/Garrison Strength/Public Order canonicity circularity: fix `settlement_layer_v30.md:43`'s broken `derived_stats_v1` citation and either (a) formally promote the §9/§14.1 PENDING formulas to CANONICAL in `derived_stats_v30.md` (they already match `settlement_layer_v30` verbatim and are load-bearing in `module_contracts.yaml`'s gates), or (b) mark `module_contracts.yaml`'s settlement-derived-value entries `[ASSUMPTION]`-grade until ratified. | (a) — promote to CANONICAL; the formulas are unchanged and already treated as live everywhere except their own nominal home doc. | ED-1052 (typed engine-params scope); values_master regenerate-vs-retire |
| C5-U3 | Fix the registry's blanket faction_stats `scale: "1-7"` to carry per-stat floors (Influence floor 1; Wealth/Military/Intel/Stability floor 0, pending an explicit Intel floor ruling) matching `params/bg/core.md`'s ceiling table. | Split into per-entry `scale`/`floor` fields; default Intel floor to 0 (consistent with the other 4 non-Influence stats) pending explicit ruling. | workplan v6 T1 queue-13; ED-IN-0008 (naming-authority) |
| C5-U4 | Disambiguate "Discipline": rename the faction-derived meter (Stability×10) or the unit-scale mass-battle stat so the two stop sharing a bare name, and add a registry/glossary cross-reference either way. | Rename the faction-derived meter to "Faction Discipline" (or similar) in display/UI copy only (formula unchanged), leaving mass-battle's "Discipline" as the primary sense given its far larger mechanical footprint (§A.2-A.13, ED-1018-1027). | ED-IN-0008; registry_delta_candidates below |
| C5-U5 | Backfill `descriptor_registry.yaml`'s `not_descriptors.derived_values` list to match `derived_stats_v30.md §14.1` in full (add TroopCount, Legitimacy-derived, Treasury, Levies Available, Reputation, Discipline, Intelligence Holdings, Public Order). | Regenerate the list mechanically from §14.1's table so it can't silently drift again. | values_master regenerate-vs-retire (queue item 17); ED-1052 |
| C5-U6 | Specify the province→settlement Fort Level inheritance rule (does every settlement in a province share its province's Fort Level 1:1, or does Fort Level need its own LPS-2e-style re-graining to settlement level?). | Genuine design call — flagged, not ruled. Cheapest fix if no re-graining is wanted: state explicitly "settlement Fort Level = province Fort Level" in `settlement_layer_v30 §1.3`. | LB workplan (settlement/territory lane); feeds SE lane per lane-scoping convention |
| C5-U7 | Re-verify and correct `name_collision_database.yaml:469`'s stale "Public Support" residual citation; add the real residual at `mechanical_terms_index.md:196,1167` to the tracked-residual list. | Update the ledger entry's `at:` field and add the two `mechanical_terms_index.md` lines as a fresh residual. | `references/name_collision_database.yaml` maintenance (IN lane) |
| C5-U8 | Add an explicit "this writes to settlement Order, not to Accord directly" sentence to `scale_transitions_v30 §5.5`, mirroring `peninsular_strain_v30 §2.7`'s phrasing, so the armature-layer doc doesn't read as though Accord were still directly writable. | Add the sentence; no mechanical change needed (peninsular_strain already governs behavior). | armature §2.1 Domain Echo row maintenance (IN lane) |

## Registry delta candidates (armature §3 analog)

- `fort_level` — currently wholly unregistered; needs a `descriptor_registry.yaml` key (likely a new
  `territory_stat` or `province_stat` kind, distinct from `settlement_stat`) plus an explicit
  settlement-inheritance rule (C5-U6).
- `set.facility_tier` and a `w_settlement` (Settlement Weight) derived-value key — both defined in prose
  (`settlement_layer_v30 §1.8`/§1.4) but absent from both the registry and `module_contracts.yaml`
  state/derivation entries.
- The 8 missing `not_descriptors.derived_values` entries identified in C5-F5 (Legitimacy-derived,
  Treasury, Levies Available, Reputation, Discipline, Intelligence Holdings, Public Order, TroopCount).
- A disambiguating key pair for the two "Discipline" senses (e.g. `unit.discipline` vs
  `fac.discipline_derived`) once C5-U4 is ruled.
