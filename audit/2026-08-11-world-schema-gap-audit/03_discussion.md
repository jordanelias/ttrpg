# World-Schema Gap Audit — discussion

## Status: REFERENCE — analysis of observations already filed. **Ratifies nothing.**

**Date:** 2026-08-11 · **Lane:** IN · **EDs:** ED-IN-0153 (audit), ED-IN-0154 (instrument defect) · **Base:** `63d4d0c`

| | |
|---|---|
| Method record | [`00_orchestration_plan.md`](00_orchestration_plan.md) |
| The 50 rows | [`01_gap_register.md`](01_gap_register.md) + parts 2–4 |
| Verdict, held decisions, residuals | [`02_verdict_and_residuals.md`](02_verdict_and_residuals.md) |
| **This document** | why the 50 rows fall into five patterns, what the schema gets *right*, and what the run got wrong |

> This is the discussion layer. Almost every claim resolves to a register row or to a `## §` of the
> two documents above; where it states a number measured *outside* the run, the measurement is given
> inline so it can be re-run. **Two passages do introduce material** and are marked `[NEW]` — an
> earlier version claimed the document introduced nothing, which adversarial review overturned.
>
> **Corrections applied after an independent read-only critic attacked this document** are marked
> ⚠ inline. Seven claims were overturned, including one that committed the exact error §4 argues
> against. They are corrected in place rather than quietly dropped, because the pattern of *how* a
> synthesis drifts from its sources is itself the finding (§6.1).

---

## 1. The question, and what "missing" was defined to mean

The repo already measures whether systems are **built**. `references/ENGINE_ATLAS.md` §2 carries
declared-vs-executed per module; the 15 `*_flow_skeleton_v1.md` §7 sections carry code-traced gap
lists; `KEY_INDEX.md` and `CONTRACT_INDEX.md` carry review queues. Asking "what is unbuilt?" again
would have rediscovered known debt and produced nothing.

So the audit asked a question nothing in the corpus asks systematically:

> **What does the world model logically require that the *schema* cannot express?**

The schema is exactly two authored surfaces — `systems/_architecture/key_type_registry_v30.md`
(55 key types) and `references/module_contracts.yaml` (27 modules). Everything in `references/` that
renders them is a **generated view**. That distinction did real work: a blank cell in a view means
*not declared*, which is a filing question; an absent type is a design question; an entity with no
contract at all is a modelling question. Three different answers, and the run had to keep them apart.

A module being merely unbuilt was explicitly **not** a finding. `declared_but_unimplemented` was
admissible only where the declaration itself is incoherent or the absence hides a missing schema
element.

---

## 2. Method, and why three axes

Three orthogonal decompositions of one subject, none seeing the others' output:

| Pass | Axis | Question | Lanes |
|---|---|---|---|
| **A · Strata** | the entity ladder | per rung: what does canon say this rung *is*, and which of those facts has no key and no contract? | 4 |
| **B · Lenses** | 18 domain lenses | per lens across every rung: what must the world remember, change, and announce? | 5 |
| **C · Config** | individuation | per entity class: what must be **authored** for an instance to be unique, consequential, legible? | 3 |

Then a read-only `valoria-critic` relay (4 clusters) and an Opus synthesis. **17 agents, 0 errors,
0 empty returns, `stop_reason: completed`, not degraded, 61 disputes recorded and 0 left
unadjudicated.** 75 raw findings → 50 register rows.

Two design choices earned their cost, and one didn't (§7).

**The relay, not a dialogue.** Critics received producer *output* and never producer *reasoning*, and
their independence is structural rather than declared: `hCritic()` resolves an agent whose tool list
is `Read, Grep, Glob` — no Write, no Edit, no Bash. What that bought is measured in §6: the critics
overturned three claims and caught two proposals that would have done damage.

**Pass C was not a lens.** Passes A and B ask what the engine must *remember and announce*. C asks
what must be *authored*. A world of 37 near-identical settlements and four stat-block factions emits
keys perfectly well and produces no narrative. Folding individuation into the lens pass would have
made it a topic; making it an axis made it the finding it turned out to be (§5).

---

## 3. The control: what the schema gets right

**A gap audit that reports only gaps is not a measurement** (CLAUDE.md §0.1 point 4). Every lane was
required to populate a `clean` list — surfaces it checked and found adequate — so a reader can tell a
clean surface from an unread one. Across 12 lanes: **75 findings and 59 clean entries** — near parity, which is the point. The strongest:

- **The two authored surfaces do not contradict each other.** `KEY_INDEX.md:37-39` review queue §2
  ("Contradictions") reads **None**, independently re-verified by two lanes. Where the registry and the
  contracts both speak, they agree. **Every gap in this register is an absence on both sides at once,
  never a disagreement** — which is what makes the backlog a filing-and-design task rather than a pile
  of rulings. ⚠ **Caveat, and it is uncomfortable:** this control rests on a *generated view*, and §6.1
  concludes that reasoning from a generated view is this audit's dominant error class. Neither authored
  surface was diffed by hand for this claim. It is the strongest control in the audit and it is
  instrument-dependent in exactly the way the audit warns about.
- ⚠ **`faction_politics` is the *contract* pattern done right — and it has no code.** Standing / Coup
  posture / Succession status are declared owned state, wired to their three keys, with per-§
  provenance (`module_contracts.yaml:889-921`), and two independent lanes reached for it as the
  template. The praise omitted three things it should carry: `:892` declares `sim_module: none` ("no
  dedicated code found"); `:914` marks the `faction_politics`/`faction_state` boundary
  **[OPEN — Jordan]**; and G-08 files a payload defect against `state.standing_change`, one of the
  three keys it is praised for. It is an exemplary *declaration*, not an exemplary system.
- ⚠ **Threadwork is the other template — but this run did not audit it.** The bucket migrations
  verify verbatim (`module_contracts.yaml:357` Coherence pool→track, ED-830/ED-IN-0029; `:358` Thread
  Fatigue track→clock, ED-694) and its emits are real. Two caveats the first version dropped: `:354`
  flags its emit *"NOT in registry (F2 class) … same event? [OPEN — Jordan]"*, and `:365` records
  doc-status ambiguity, also **[OPEN — Jordan]**. More importantly, `02` §4 item 1 instructs that
  threadwork produced **no finding** and must be treated as **unread, not clean** — so listing it among
  the strongest clean surfaces contradicts this audit's own residual. Its *contract shape* is a
  template; its *coverage here* is nil.
- **The Conviction Scar mechanism is fully wired schema-to-schema** — owned state, emitting key,
  and gates (`g_scar2`/`g_scar3`) — at the character rung, the rung otherwise weakest.
- ⚠ **5 of the 8 "nobody consumes" keys are deliberate registrations — but the 8 are not therefore
  closed.** The five are DECLARE-ONLY per **ED-IN-0014** (`key_type_registry_v30.md:1251-1252`);
  ED-IN-0096 is the later correction that emptied their `consuming_systems`. DECLARE-ONLY means the
  emit does **not** exist, so these five have neither producer nor consumer. Two more are the wildcard
  pair (a join defect, §6). The eighth, `meta.legacy_event`, is unaccounted by any of that — and
  `02` §3 item 4 holds **all eight** at ED-IN-0151 item c. An earlier version said the 8 were "mostly
  already dispositioned"; that converted a held fork into a mostly-closed one.
- ⚠ **8 of the 9 A6-violating module pairs are enumerated, which is not the same as absolved.** The
  arithmetic holds — `CONTRACT_INDEX.md:23` lists 9 pairs, `scale_transitions_v30.md:341` enumerates 8,
  the residue is `piety_track←scene_slate`. But §12.4's heading reads **"Known down-seams (Lane-B
  implementation targets)"** and its body says the emitters *"do not yet populate sub-scale targets"*.
  That is **enumerated open debt, not a non-defect**. An earlier version of this line called the 20 A6
  violations "a join artifact far more than a debt"; that inverts the source. They are *tracked*
  debt — which is better than untracked, and is not clean.
- ⚠ **NPE's 5-axis genome is a real hook with *some* variation — the strong version of this claim was
  false.** An earlier version said two generated NPCs "differ on every axis". Reading
  `systems/world/sim/npe.py:239-290`: stance starts at `base = 3` for every issue with ecology nudges
  keyed on **territory**, so two NPCs in the same territory get the *same* stance (`:249-259`); loyalty
  is deterministic given faction (`:276`); and the deviation die flips exactly **one** axis
  (`:279-284`). The claim was number-shaped, had no instrument behind it (no campaign was run), and
  appeared in neither `01` nor `02` — a §0.1 point-4 failure inside the section that opens by citing
  §0.1 point 4. What survives: variation exists and is real, and it is **narrower than the genome's
  five axes suggest**, which strengthens §5 rather than softening it.

---

## 4. Five structural patterns

The 50 rows are not 50 independent problems. They are five patterns with many instances, and the
distribution says which layer is weak: **`missing_owned_state` (16) and `missing_edge` (6) together
outnumber `missing_key_type` (6) nearly four to one.** The Key substrate is in better shape than the
contract layer. **The engine can mostly announce; it largely cannot hold.**

### P1 · Built and unowned

Not "unbuilt" — *built, live, mutating, and owned by no contract row*. This is the single most
common shape in the register.

- **`World.treaties`** is real, serialized and restored per campaign — a dict of `TreatyRecord(parties,
  terms, bound_arc, bound_season, active)` with six canon treaty types — and **no module owns it**
  (G-07). Diplomacy has a doc, real code in `treaty.py`, and `da.diplomatic_alliance`; treaties appear
  in nobody's `state:` block.
- **`Settlement.governor_id`** has a dedicated mutator with appointment *and* removal semantics, and
  no state row (G-04).
- **Territory temperament** is `## Status: CANONICAL`, drifts under `env.peninsular_strain_shock`,
  and aggregates population-weighted into faction effective temperament — with **no contract module**,
  its only implementation a zero-importer orphan (G-03).
- **Church Attention Pool** is written by 10+ canon triggers across 7+ subsystem docs. Every sibling
  clock — CI, IP, Turmoil, MS — has a row. It has none (G-25).
- **`env.population_change` is emitted by `settlement_layer`, which has no Population field to apply
  the delta to** (G-30). The key fires into nothing.

The common cause is visible in G-24: the bucket taxonomy is `{derived_value, track, clock, pool}` —
**four shapes, all for single-owner scalar quantities.** A treaty is a per-counterparty relation; an
NPC relational edge is a typed graph edge; a subnational foothold is a per-archetype map. None has a
legal shape, so each is stored as an untyped dict outside the schema. *This is one taxonomy decision
sitting underneath at least six rows*, which is why filing them separately would have been six
symptoms and one unaddressed cause.

### P2 · Nothing announces existence

**No key type at any family announces an entity coming into or going out of existence, at any tier.**
This was the run's strongest convergence — **four lanes across all three passes** (G-01).

Canon requires it in at least five places: Stage-4 Faction Declaration with a ratified starting stat
sheet; Collapse-to-city-state; Dissolution; Split; and `victory_v30` standing up an "Altonian
Governorate" *mid-campaign*. The one production path claiming to implement emergence sets a boolean
and returns.

The same absence at the territory rung is sharper still: under the ratified B12 hierarchy a
**province's existence is conditional** — it forms only while its constituent territories share a
holder and dissolves the instant they don't. No key carries formation *or* dissolution (G-27). The
world can change shape and no system can learn of it.

This is the pattern with the most severe downstream consequence, because an emergent-narrative engine
whose entities cannot be created at runtime has a fixed cast by construction.

### P3 · Arity too narrow

Payloads that cannot express the shape of the relation they report on.

- **`state.standing_change` carries no `faction_id` and no ladder identifier** (G-08). Standing is at
  minimum keyed `(npc × ladder)`: four independent 8-rank main-faction ladders plus sub-office
  ladders. Its two siblings in the same family, `state.coup_attempted` and `state.succession`, both
  already carry `faction_id` — so the fix composes on a precedent one line away. This was one of only
  two gaps two lanes reached independently.
- **`da.diplomatic_alliance` can only express a two-party treaty** (`faction_id` + `counterparty_faction`)
  where canon has guarantors and multi-party terms.

**A caution the critics attached to this pattern, and it generalises:** two lanes reasoned from a
key's `optional_payload_fields` table to *"this key cannot express a multi-target fan-out"* — while
`key_substrate_v30.md` §45-53 defines `targets[]` with per-target `impact_vector` and `stat_delta`,
which is exactly that channel. **Any future claim that a key cannot express an arity must cite the
substrate, not the type entry.**

### P4 · The ladder has a missing rung and five vocabularies

`scale_hierarchy_v1.md` is Jordan-ratified (B12, 2026-07-13) at *Country > Duchy > Province >
Territory > Settlement*. Measured by hand this session:

- **`engine/substrate/keys.py:65` is `SCALES = ("personal", "settlement", "territory", "peninsula")`**
  — four values. No `national`, no `duchy`, no `country`; also no `scene` and no `thread`.
- **`provincial` appears 0 times in the key type registry** (`grep -c provincial` → `0`), while
  `module_contracts.yaml` uses it as the scale for every faction module.
- The B12 Territory tier collapses back into the same 17 T-codes it was meant to sit beneath (G-21).

That is at least four parallel scale vocabularies, and the run found a fifth. **Nothing here was
resolved** — unification is HELD at ED-IN-0103 §6 fork 1, whose text bars any change "here or
anywhere else." The audit contributes two new measurements to that fork and proposes nothing (G-43).

The related open question is whether faction **tier** (local/provincial/national) is a *field* on the
existing contract or a *module per tier* (G-22). §5.1's own argument — that tiers are the same kind
of entity differing only in population held — points to tier-as-field, and the register records that
as a recommendation rather than a ruling.

### P5 · Individuation — see §5

---

## 5. The individuation axis

This axis exists because of a mid-session instruction: *what do characters, factions, settlements and
the world need in order to be unique and meaningful and to contribute to a robust emergent narrative?*
It produced the run's bleakest result, and the one most directly about whether the game works.

**The schema mostly cannot distinguish two instances of anything it does carry.** Three failure shapes
were named in the lane brief before the run, and all three were found:

**1 · Flavour with no hook** — a distinguishing trait no system reads.

Measured by hand this session against `systems/settlements/valoria_geography_v30.yaml` (17 provinces):
`spiritual_weight`, `proximity_calamity` and `starting_pros` are authored per province and have
**zero Python readers each** (`grep -rn <field> --include=*.py .` → `0`, `0`, `0`). The settlement
generator names these as the intended individuation source for religious character, wealth and
calamity exposure (G-48). They are authored, varied, and inert.

**2 · Hook with no variation** — a stat every instance carries at the same value.

`institutional_culture` is authored as *the* scalar meant to individuate a faction's Cascade behaviour
via the α_institution term. Measured by hand: **zero Python readers** (`grep -rn institutional_culture
--include=*.py .` → `0`), and across the six canonical factions the authored values are
`0.0, −0.1, −0.2, −0.1, +0.1, −0.1` — **three of six share −0.1** (G-49). The mechanism does not run,
and if it did, half the roster would be indistinguishable on it.

**3 · Hardcoded singleton** — identity as a named branch in code rather than data on the instance.
This is **scripting drift**, the failure mode CLAUDE.md §10 names, and the register ranks it high
regardless of rediscovery count because the defect is structural rather than statistical.

- `engine/autoload/game_state.py:231` — `templar=(tid == 'T9')`. A real, writable, persisted,
  consequential field, set for exactly one territory by a hardcoded name comparison (G-15).
- ⚠ Faction-unique behaviour dispatches on string equality — **2 production sites, not the 8 an
  earlier version of this line reported.** The regex `.name == 'Crown'|'Church'|'Hafenmark'|'Varfell'`
  does return 8, but **6 of them are assertions in `engine/tests/test_parliamentary_action.py`**; the
  production dispatch sites matching it are `systems/factions/sim/faction_action.py:277` and `:293`.
  **The register's G-16 census is the correct one and is larger: 5 sites**, because three do not match
  that regex at all — `systems/overview/sim/ci_track.py:91` and `systems/factions/sim/mass_seizure.py:131`
  compare `t.owner ==`, and `systems/factions/sim/parliamentary_transfer.py:107` compares `initiator ==`.
  I substituted a literal string count for G-16's concept-level census and the two coincidentally
  collided on 8. **That is pattern-matching on the term instead of the concept — the error CLAUDE.md §0
  names as the costliest in this corpus — committed inside the paragraph arguing against scripting
  drift.** The finding stands and is *worse* than the bad number implied: the drift is spread across
  three comparison idioms in four modules, which is why a grep-shaped fix would miss most of it.

The last one carries the sharpest detail in the whole audit, and it is a *routing* defect rather than
an absence. A producer lane claimed no field anywhere lets a faction declare a unique action as data.
**The critic overturned it**: `registers/mechanics_index.yaml` carries `faction_unique_actions`, a
per-faction capability map, exactly the data structure required. Verified by hand this session: it has
**zero Python readers** (`grep -rn faction_unique_actions --include=*.py .` → `0`); it appears only in
the registry, the generated glossary views, a design doc, and the identifier census. So the primitive
that would make faction identity data **already exists and is unread**, while the behaviour it should
drive is hardcoded eight times over. Re-entered as G-16.

**The consequence, stated plainly:** what remains is near-identical instances plus a handful of
hardcoded singletons, so **a second campaign would differ from the first essentially by RNG seed.**
For a project whose stated goal is emergence, this is a more urgent finding than any individual
missing key.

---

## 6. What the adversarial pass changed

The critics returned 43 items the producers never reached and produced 61 disputes. The value is
measurable, not asserted:

**Three producer claims were overturned and do not enter the register as filed.** The
`faction_unique_actions` claim above is one; the lane had grepped two files. Two others fell the same
way — a claim about `Settlement.subnational`, and one more recorded in `02` §4 item 8.

**Two proposals would have caused damage if executed**, and are flagged rather than silently dropped
(`02` §4 item 9). The sharpest: the templar fix proposed siting the station by a `spiritual_weight`
threshold, resting on the stated premise that *"T9 is highest of all 17."* **That premise is false.**
Verified by hand this session against all 17 provinces: **T15 is 5, T9 is 4.** The proposed rule would
have sited the station in T15 — an uncontrolled, settlement-less calamity epicentre. A correct-looking
fix, adopted, would have moved a live mechanic to the wrong place.

**Three of my own pre-run leads were refuted**, which is the part worth recording, because I wrote
them into the lane briefs as grounding and they carried my authority:

1. I flagged *"Domain Echo: `classify_scene_outcome` requires an `echo['scene_outcome']` field no live
   producer sets — is that a missing `required_payload_field`?"* **No.** `scene.accord_echo` already
   carries `scene_outcome` (`key_type_registry_v30.md:974`). It is producer-side dormancy, not a
   schema gap.
2. I presented the **20 A6 cross-scale violations** as a gap surface. 8 of the 9 module pairs are
   enumerated down-seams in `scale_transitions_v30.md` §12.4. One is a real question.
3. I presented the **8 consumerless keys** as open. 5 are deliberate declare-only registrations
   (ED-IN-0096). The live question is narrower and different: `env.crisis` and
   `mechanical.season_change` declare wildcard consumers (`[all]`, `[all subscribing systems]`), which
   is a **join defect, not an absent declaration** — a distinction no lane would have drawn from the
   generated view alone.

A fourth correction came from Jordan mid-session and is recorded in full at `00` §7: **characters are
NPCs.** My grounding said *"no `Character` class exists anywhere in the tree"* — literally true,
verified by grep, and a claim about class *names* that invited a false conclusion about the *model*.
The gap relocated rather than closing: no contract owns character identity, and identity is recorded
twice at two grains with no bridge and no `settlement_id` anywhere. Lane A1 reached that framing
unprompted, which is the evidence the correction was to the record and not to the audit. ⚠ Stated
precisely: there is **no `settlement_id` on any character**. The unqualified form — "no `settlement_id`
anywhere" — is false (22 occurrences across `engine/tests/test_accord_echo.py`,
`tests/valoria/test_key_substrate.py`, `systems/settlements/sim/settlement.py`), and dropping the
qualifier is what made a true claim false.

### 6.1 What the corrections have in common — restated after being got wrong

⚠ An earlier version closed this section with *"four of the seven errors above are that single
mistake."* Both numbers were asserted without counting. §6 enumerates **nine** items (3 overturns,
2 damaging proposals, 3 refuted leads, 1 Jordan correction), and **at most two** are generated-view
errors: KEY_INDEX for the consumerless keys (G-42), CONTRACT_INDEX for A6 (G-47). A denominator and a
numerator both invented, used to land a tidy conclusion.

The honest version is two distinct patterns, and the second is the larger:

1. **Reasoning from a generated view instead of an authored source** (2 of 9). `KEY_INDEX.md` and
   `CONTRACT_INDEX.md` are joins; a blank cell means *not declared*, not *none*.
2. **Reasoning from the wrong authored surface** — the actual dominant class, and `02` §4 item 10 says
   so. Lanes read a key's `optional_payload_fields` table, which is authored, and concluded the key
   could not express an arity that `key_substrate_v30.md` defines one file away. The type entry does
   not describe the envelope.

The corrections in *this* document add a third, which is the one a synthesis layer is most exposed to:
**compression that drops a qualifier** — "no `settlement_id` on any character" → "anywhere";
"enumerated down-seams" → "not defects"; "governed but unrecorded" → "cannot proceed". Each started
true in the register and became false by being shortened.

---

## 7. The instrument defect, and a prediction this unit got wrong

**Recorded prominently because it conditions every number in the register, and because it falsifies a
prediction written down before the run.**

`00` §6 stated the rediscovery limit as: *"two lanes that reach one gap through different files will
not group, so the rediscovery count is a floor, never a ceiling. It under-reports corroboration; it
cannot over-report it."*

**Wrong in the direction that matters.** It did not under-report. It reported **nothing**: 75 findings
produced 75 groups, and every `rediscovery` value in the returned ranking is `1`. The corroboration
signal — the entire justification for running three method-disjoint passes rather than one — was
absent from the data handed to synthesis, which reconstructed it by hand from lane labels and claim
wording.

**Root cause** in `tools/wf_harness.js`: `hSameFinding` gates on `hFirstFile(a) === hFirstFile(b)`
*before* comparing content words, and `hFirstFile` returns the first file-shaped token in a finding's
free-text `evidence`. Two lanes describing one gap from different directions rarely lead with the same
citation, so the file-equality precondition zeroed the comparison before the fuzzy matcher ran.

**The owner predicted this exact failure and then inherited it.** Its comment on the *exact* key reads:
*"An exact key splits them into singletons and silently zeroes out the entire corroboration signal,
which is worse than not computing it: the output still has a `rediscovery` column, it just always
reads 1."* `hSameFinding` was written as the remedy and kept the precondition that causes it. This is
the §0.1 point-5 signature: correct for the shape it was written against, silently wrong for the shape
that arrived later.

**Not fixed here, deliberately.** The harness is copied verbatim into every workflow script and pinned
by a mutation-verified suite; the grouping rule needs its own expected-delta test, not a drop-in edit.
Filed as **ED-IN-0154**. The guard is the deliverable: a fixture of two paraphrases citing different
files must group to 2, or the pattern recurs invisibly — which is what happened here. Note that the
existing suite is green and mutation-verified and did not catch this, because it pins that `signal()`
never throws, not that grouping groups.

**Consequence:** the `×` column is a **synthesis reconstruction with named provenance, not a
measurement**. Rows at ×3 and ×4 reflect a judgment that lanes converged. Treat them as an ordering
hint. The one claim that survives independently is P2's: four lanes across three passes reached the
faction-lifecycle gap, and that convergence is legible in the lane outputs themselves.

---

## 8. Decision surface

**13 register rows carry `needs_jordan_ruling`; the held list in `02` §3 has 17 entries** because
several bundle multiple rows or raise items that are not rows at all. Ordered by how much each
unblocks:

1. **G-17 — who authors `references/rendering_dispositions.yaml`?** It governs **all 8 `propose_key`
   rows**. §10's precondition is RATIFIED (ED-IN-0026) and the file does not exist.
   ⚠ **Corrected by second-pass review — an earlier version of this item said "nothing in the key half
   of this register can proceed until this is answered or waived," and G-17 exists precisely to correct
   that overstatement.** `key_type_registry_v30.md:1287-1291` has A15 enforce the rule **report-only**
   against the existing 55-type roster first, flipping to blocking *"once `rendering_dispositions.yaml`
   exists and the backlog is at zero"* — standard warn→block discipline. So appends today are
   **governed and unrecorded, not mechanically refused**. The practical obligation is real but
   different: every `propose_key` row must ship its rendering-disposition row as a **co-artifact**, and
   a second obligation rides along that no proposal mentioned —
   `engine/engine_params/key_types.json` is GENERATED from the registry by `tools/export_key_types.py`,
   declares *"NEVER hand-edit"*, and pins registry order as significant. **Still start here**, because
   answering it is what makes the other seven rows shippable rather than merely arguable.
2. **G-24 — does the bucket taxonomy gain a relational shape?** Sits underneath at least six rows
   (treaties, relational edges, subnational footholds, sanctions). The largest single unlock in the
   contract half.
3. **G-21 / G-43 — does the B12 Territory tier enter the scales enum, and how do five vocabularies
   reconcile?** HELD at ED-IN-0103 fork 1. Blocks coherent expression of the ratified ladder.
4. **G-22 — faction tier as field, or module per tier?** Recommendation on the record is
   tier-as-field; the call is Jordan's.
5. **G-38 — is a singleton starting world an intentional design ruling?** If a second campaign is
   meant to differ by more than RNG seed, this is the question that says so.

**One row needs a *correction* rather than a ruling and should not wait on the above:** **G-18**, an
executable parser defect (`engine/substrate/keys.py:294`) where a trailing inline comment silently
voids a flow list.

⚠ **G-19 was listed here too and does not belong.** Its disposition is `needs_jordan_ruling`, it is
held item 14 of 17, and its own proposal states the fix *"changes an existing type's
`required_payload_fields`, which `key_type_registry_v30.md:1273-1278` makes a **Class A supersession
event** … it should be ruled before the additive field lands."* Grouping a Class-A supersession with a
one-line parser fix is precisely the misclassification that would have produced an unratified change.
The underlying defect is real — `meta.knot_formed` still carries the struck `Loose | Medium | Close`
enum, already propagated into the generated `key_types.json` — but it is Jordan's call, not a
correction.

---

## 9. Limits

Stated so a reader can tell a clean surface from an unread one. Full text in `02` §4.

- **Whole subsystems produced nothing:** combat, social contest, fieldwork, threadwork beyond its
  template role, articulation, UI, victory beyond the Altonia residual. The swept rungs yielded ~50
  gaps; the unswept ones are **unread, not clean**.
- **Of the lenses, about 14 are visible in the findings.** World history and threadwork produced no
  finding under their own names. ⚠ **The denominator is itself unreliable:** this unit says "19 domain
  lenses" throughout, while `00_orchestration_plan.md`'s own enumeration lists **18**. The count was
  inherited from the original request and never reconciled against the list actually swept. Treat "14
  of 19" as "14 of 18-or-19" — the shortfall is real, its precise size is not established.
- **No cited PP number was provenance-verified.** Findings cite PP-666, PP-724, PP-687, PP-726 and
  others as authority, and CLAUDE.md §0 records that **433 of 452 distinct PP-NNN numbers cited in
  live surfaces resolve to no register on `main`** since the 2026-08-05 evacuation.
- **No finding was verified by execution.** Every "zero production callers" and "orphan" claim rests
  on grep plus the flow skeletons' own instrumented measurements. No campaign was run.
- **The `existing_tracking` field is systematically unreliable in the input** — roughly a dozen
  findings asserted "none found" after grepping `registers/editorial_ledger*.jsonl` **only**, while
  this corpus also files in surviving audit units and flow-skeleton §7 sections.

Three passes over one tree is not a completeness proof. It is a floor on coverage with a named shape.

---

## 10. Corrections logged this session

| What | Where |
|---|---|
| Characters are NPCs; the "no `Character` class" framing corrected and the finding relocated | `00` §7, ED-IN-0153 |
| `hRediscover` zeroes its own corroboration signal; the `00` §6 prediction falsified | §7 above, ED-IN-0154 |
| `scene.accord_echo` already carries `scene_outcome` — my lead refuted | §6 above |
| 8 of 9 A6 pairs are enumerated down-seams, not defects — my framing corrected | §6 above |
| 5 of 8 consumerless keys are deliberate; the live question is a wildcard join defect | §6 above |
| `test_id_reservations_walkback` — my allocation note *was* the narrative creeping back | commit `004f387` |
| `test_engine_atlas` — control run at `HEAD~1` first; the delta is §5's `audit` word count, +1 | commit `004f387` |
| **Found by adversarial critics on this document and `04`, after they were written** | ⚠ below |
| "60 findings across 12 lanes" — that was the 9-lane interim; correct is **75** | §3 |
| "8 sites" of faction string dispatch — 6 are tests; **2 production**, and G-16's real census is **5 across 3 idioms** | §5 |
| A6 pairs "are not defects" — §12.4 calls them *"Lane-B implementation targets"*; **enumerated debt** | §3 |
| NPE "differ on every axis" — unsupported; stance is territory-keyed, the die flips **one** axis | §3 |
| "no `settlement_id` anywhere" — false; the true claim is **on any character** | §6 |
| "four of the seven errors" — §6 has **nine** items and **two** are generated-view errors | §6.1 |
| G-19 grouped with G-18 as a do-now correction — it is a **Class A supersession**, held | §8 |
| `04`: consumerless keys "the emit exists" — **DECLARE-ONLY means it does not**; and the ED was **ED-IN-0014**, not 0096 | `04` §2.3 |
| `04`: "~140 consume edges" → **125**; roster wrong on 4 of 27; "six of eight" → **seven** | `04` §2, §5 |
| `04`: "emit sites dated after the measurement" — **no date supports it; two contradict it** | `04` §3.1 |
| **2nd-pass review, post-merge:** G-17 framing — appends are **report-only-governed, not mechanically refused**; the item asserted the very overstatement G-17 was written to correct | §8 |
| **2nd-pass review:** the lens list enumerates **18**, not 19 — an error in the original decomposition inherited by every downstream artifact | §2 · `00` §2 · `02` §4 · ED-IN-0153 |
