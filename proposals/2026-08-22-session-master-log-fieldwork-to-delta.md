# Session Master Log — fieldwork architecture through the delta, reconciled

## Status: RECORD — reconciliation and index over nine session documents, plus a comparative critique against precedent. Findings, not design. Nothing here rules anything. No `.py` touched. Content/design only; another session owns the restructure, and reconciliation against that work is pending.

**Date:** 2026-08-22 · **Lanes touched:** FI, IN, PC, SC, MB, FA, SE, WR
**Method:** agonist→antagonist throughout. Two Fable 5 read-only passes (wiring map; reconciliation) and one Opus research pass, each barred from regex/grep/pattern-matching for establishing findings; five independent read-only antagonists against the delta; and independent re-verification by parse or by reading of every claim that changed a published document.

---

## §0 HOW TO READ THIS

**This document restates nothing it can cite.** The nine session documents exist and are the authority for their own contents. What lives here and nowhere else is the reconciliation (§2), the falsifier record (§3), the pattern as it survived attack (§5), the content census (§6), and the comparative critique (§7).

**Trust order, when two surfaces disagree:**

> **§2 of this document** > **doc 7 §8** (the delta's own falsifier record) > **doc 7 body** > **docs 1–6** > any older surface.

**The nine sources.**

| # | Document | What it is *for* |
|---|---|---|
| 1 | `2026-08-18-fieldwork-architecture-and-nonadversarial-play.md` | the architecture; 19-game precedent survey; the substrate gaps GAP-A/GAP-B; §13 carries 15 Jordan rulings. Merged PR #318, PROPOSED |
| 2 | `2026-08-18-epistemic-propositions-and-provenance.md` | the belief layer (Propositions + Holdings); **supersedes doc 1 §11.2** |
| 3 | `2026-08-18-ruling-execution-plan.md` | 14 dependency-ordered steps, 5 blockers |
| 4 | `2026-08-19-obstacle-stat-and-identity-census.md` | 213 obstacle sites; the inert `tn` |
| 5 | `2026-08-19-roll-and-resolution-inventory.md` | AST-exact roll inventory; `references/` has zero runtime readers |
| 6 | `2026-08-19-subsystem-input-shape-and-narrative-robustness.md` | **the record of a plan the relay killed.** Its value *is* being the corpse; do not summarize it away |
| 7 | `2026-08-19-subsystem-delta-and-narrative-robustness.md` | the delta — three failure modes; §8 is its falsifier record |
| 8 | `2026-08-22-wiring-map.md` | every required connection: what to wire, where, and whether each end is coded or designed. 16 design gaps |
| 9 | **this document** | reconciliation, census, critique |

**A vocabulary note, per CLAUDE.md §4.** Doc 7 coined *hollow seam* and *starved seam*. They are session-local and are **not** used as load-bearing terms here. Where this document needs them it says the ordinary thing: *the caller fires and the body is a stub*; *the caller and body are real and the input is degenerate*.

---

## §1 THE SESSION IN ONE PAGE

Commissioned to design a fieldwork/investigation architecture from precedent, the session ran: **architecture** (doc 1) → **15 rulings** by Jordan, including that scripting narrative hooks and sequences is allowed while scripting entire arcs is not → **belief layer** (doc 2, superseding part of doc 1) → **execution plan** (doc 3) → **two mechanical censuses** (docs 4–5) → **a plan an antagonist destroyed** (doc 6) → **the delta** (doc 7) → **the wiring map** (doc 8) → **this reconciliation**.

Eight commits on `claude/fable5-investigations-architecture-1phbx9`. The arc of the session is best read in what it retracted: **twenty-two distinct corrections**, of which the three largest killed the session's own headline claims (§2, §3).

---

## §2 RECONCILIATION LEDGER

Where two documents disagree, or later verification broke an earlier claim.
**[in-doc]** = retracted inside the document that made the claim · **[later doc]** = retracted by a later session document · **[NEW]** = retracted for the first time here.

### §2.1 Already on the record — cite, do not re-litigate

| # | Claim | Asserted | Corrected | Status |
|---|---|---|---|---|
| 1 | The solvability invariant is "the only genuinely new idea" | doc 1 §8 (`:561`) | doc 1 §11.1 (`:635-677`) — it is the existing hook grammar (coup counter, assassination fuse, Crown Claim table) | [in-doc] |
| 2 | "The gap is one line" (the `evaluable` set) | doc 1 §4b.1 (`:279-280`) | doc 1 §11.4 C7 (`:748`) — a seam, not a gap | [in-doc] |
| 3 | Adopt `state.belief_revised` as the belief layer | doc 1 §5.4, §11.2 | doc 1 §12.3 (`:943-961`): free strings, no confidence, creed semantics, inert. Superseded by doc 2 | [in-doc + later doc] |
| 4 | "Not one of the five outcome vocabularies is the degree ladder" | doc 1 §11.8 (`:875`) | doc 1 §12.1 (`:910-915`): `mechanical.scene_exited.outcome_class` carries it verbatim | [in-doc] |
| 5 | "`scene_dispatch.py:349` needs no call-site change" | doc 1 §5.2 (`:393`) | doc 1 §12.2: `:354` does not pass `world`; **the comment is wrong about its own code** | [in-doc] |
| 6 | CLAUDE.md §6's "10/27 `doc: null`, 11/27 `[ASSUMPTION]`" | `CLAUDE.md:367-369` | doc 1 §4b.5: parsed figures are **9/27 and 10/27**; argument survives, arithmetic off | **cross-surface, edit not yet made** |
| 7 | Disposition "stored on `npe.NPC`" | doc 1 §6 (`:453`) | Ruled otherwise (doc 1 §13.3 Q9, doc 2 §10.1) — joins Holdings in `npc_memory`. Doc 3 §6.1 warns *"Anyone executing from §6 verbatim will re-home it wrongly"* | [later doc] |
| 8 | B4/R2 divergence test "executable today" | doc 3 §1 B4 | doc 4 §5.2/§8: fieldwork sims are stubs and produce no orderings — unrunnable as scoped | [later doc] |
| 9 | R1 census ≈15 sites; PC migration first | doc 3 §3 | doc 4 §8: **213 sites**; PC migration blocked on "what is a character's score" | [later doc] |
| 10 | "Every `ob=` comes from factions **or threadwork**" | doc 4 §2.1 (`:97`) | doc 5 §2.1: threadwork passes **no** obstacle to any roller; all 7 sites are `systems/factions/sim/` | [later doc] |
| 11 | Modules should "point at centralized definitions" | doc 1 §6, doc 2 §6 | doc 5 §7.1/§7.4: **`references/` has zero runtime readers** — the specified mechanism does not exist | [later doc] |
| 12 | Doc 6's original plan (inventories, 11-value axis, six-dimension metric) | doc 6 pre-history | doc 6 §1 — antagonist returned UNSOUND. **The document is the retraction** | [in-doc, by design] |
| 13 | Fourteen delta claims (see §3) | doc 7 drafts | doc 7 §8 — the falsifier record | [in-doc] |
| 14 | Suppress-roll Ob: `conviction_track_v30.md:204` (Church Mandate) vs `faction_layer_v30.md:699` (floor(Mandate/2)+1) | canon, not a session doc | surfaced doc 4 §2.2 | **open — two ratified surfaces conflict; only Jordan picks** |

### §2.2 Broken by verification in this pass **[NEW]**

**15 · Doc 7 §2.3's "enrich the call site — no new mechanism required" is 3/5 true.**
`Contest.resistance` is **metadata-only** by its own docstring (`wrapper.py:73-77`): *"NOT plumbed into resolution — the resolver reads no resistance and `Venue.base_ob` is not set from it. Wiring it is the reserved ED stub (ED-1055..1079)."* `resolver.py`'s only `resistance` occurrence is prose in a comment. And `_resolve_agon` (`wrapper.py:193-198`) builds `Bout(...)` **without** `armature=`, while `resolve_contest` has no armature parameter — so Style, the armature δσ and CR4 cannot be reached through the router at all.
**Survives:** policies, the dossier/evidence path, and `base_ob` via a prebuilt Venue. **"Cheapest large win" survives weakened; "no new mechanism required" does not.**

**16 · Doc 7 §6's "the single missing artifact is a loader" is broken in degree.** The recommendation survives; the costing does not. Four hidden prerequisites, all verified by parse or read:
- **No destination for the weights.** `ConvictionState` (`conviction.py:108-123`) has no baseline-weight field. The 81 weighted primaries have nowhere to land.
- **The territory join is mostly empty and format-mismatched.** **7 of 46** entries carry `territory`, formatted `"T15 (Southernmost)"` against `STARTING_OWNER`'s bare `'T1'..'T15','T17'` — and one entry names **T16**, which does not exist in that map.
- **The faction join is unmapped.** 20 distinct strings for four parliamentary factions.
- **A live data defect (NEW, same class as ED-IN-0121).** `npc_registry.yaml:835,:850` — unquoted `faction: Hafenmark (Inner Council #4)`. YAML reads ` #4)` as an inline comment, so NPC-081/082 load truncated with unbalanced parens. It survives for the same reason ED-IN-0121 did: zero loaders, so nothing checks.

**17 · Doc 7 §6's "46 fully-structured characters" is false as a population claim.** Those are the schema's **optional** fields. Measured across 46: `stats` **1**, `coherence` **1**, `age` **0**, `birthplace` 5, `territory` 7, `title` 7, `certainty` 8, `ts` 10, `notes` 15, `goals` 17, `resonant_style` 18, `arc_trajectory` 36, `cultural_label` 43, `self_other_initial` 28. Universal: `id`, `first_name`, `faction`, `role`, `status`, `source`, `convictions`.
**Honest form: 46 *identified* characters, all carrying a conviction profile, roughly a third deeply authored.**
Plus a schema defect a loader hits immediately: `cultural_label`, `self_other_initial` and `migration_notes` appear at **two nesting levels** across entries (top-level and nested under `convictions`). A loader reading one level silently misses most of the data.

**18 · Doc 7 §2.2's "`scene.contest_resolved` — the *only* type a default campaign emits" is false, and the correction enlarges the finding.** `faction_action.py::_emit_battle_concluded` (`:342`) builds a real `scene.battle_concluded` Key and is called **unconditionally** at `:480` after every resolved war action. Its docstring: *"THE FIRST KEY EMISSION OUTSIDE `echo_transport` (ED-IN-0122) … A substrate with one call site is a prototype, not an architecture."*
**The conclusion is unaffected — zero articulation callbacks still fire** — because `scene.battle_concluded` is **also** absent from `_TRIGGER_TYPE_IDS` (verified: 13 entries, not among them), while `key_graph.json` declares **four** consumers for it including `articulation_layer`. **So the registry-vs-roster inconsistency is two omitted rows, not one.**

**19 · GAP-B's framing needs nuance: the empty `causes[]` is doctrine at at least one site, not laziness.** `faction_action.py:386-389`: *"No upstream Key exists to cite: `resolve_mass_battle` is a plain call, not an emission. `[]` is the honest value — a fabricated cause is worse than no cause."*
**The real cause of GAP-B is that upstream resolutions are not emissions**, not that emitters are lazy. That changes what doc 3 step S3's cross-lane ask should ask for.

**20 · Two numbers that look contradictory and are not.** Doc 6 §3.1's "NPC: 5 axes" vs doc 7 §3's "NPC: 12 fields" — expressive axes vs dataclass fields. Doc 6 §3.2's "13 named characters" (the `systems/npcs/` docs) vs doc 7 §6's "46" (`references/npc_registry.yaml`) — **different surfaces; doc 6 never opened the registry.** No retraction owed; the referents are recorded here once.

### §2.3 Corrections owed to other surfaces, still unexecuted

1. **`CLAUDE.md:367-369`** — the 10/27 and 11/27 contract figures are 9/27 and 10/27 (ledger row 6). IN-lane edit, filed, not made.
2. **`references/npc_registry.yaml:835,:850`** — the comment-truncation defect (row 16). A two-character quoting fix; **not made this session** because the file is a registry and another session owns registry edits.
3. **`systems/factions/faction_canon_v30.md:6-7`** carries `## Status: CANONICAL` and `## Status: PROVISIONAL — pending ratification` **on consecutive lines**. Pre-existing; not this session's making.
4. **The Suppress-roll collision** (row 14) — two ratified surfaces disagree; Jordan's call.

---

## §3 FALSIFIER RECORD

Per CLAUDE.md §0.1 point 3: a result claim carries, in the same place, the check that would have shown it wrong.

**Doc 7 §8** carries fourteen overturned delta claims in full and is cited, not restated. Its headline entries: *"the gap is ONE function body"* (four structural blockers instead), *"13 triggers fire every season"* (zero fire), *"4 of `conviction.py`'s 9 are in no taxonomy"* (zero are — it is the legacy 9 verbatim), *"`owner_faction` populated for one settlement"* (37 of 37), *"`contest/narrative.py` is the only prose renderer"* (three more exist).

**New this pass:** ledger rows 15–19 above.

**Falsifiers named but NOT RUN — the open attack surface.** Consolidated here because no single document holds them:

| Unrun check | Owed by | Would settle |
|---|---|---|
| B1 content-hash stability across sessions | doc 3 | whether Proposition identity is reproducible |
| The 151-test count in doc 1's §7 gate | doc 1 | a gate's own arithmetic |
| An antagonist pass on threadwork | doc 7 §9 | doc 7 §2.1's threadwork claim, still producer-grade |
| An antagonist pass on mass_battle + world | doc 7 §7 | four findings carried at producer confidence |
| **A single campaign run with `record=True` and a print** | doc 8 §9 | **whether the contest Chronicle is really "one kwarg away"** — the claim doc 8 flags as its own most-likely-wrong |
| Executing a campaign to confirm battle-Key reachability | ledger row 18 | argued from code read, not from a run |

**The pattern in these:** every one is blocked by this session's design-only scope. **Nothing here has been executed.** That is a deliberate constraint, and it is also the single largest qualifier on everything above.

---

## §4 WHAT IS ESTABLISHED

One line per finding, with its citation and a MEASURED / JUDGMENT tag.

| Finding | Tag |
|---|---|
| **The population of Valoria is zero in every seeded campaign.** `generate_npc` has no world-gen or season-tick call site — a **ruled permanent deferral** (OI-05), whose "oversight" framing the corpus already retracted at `test_pipeline_reach.py:137-145` | MEASURED |
| **Key traffic is one-directional.** 7 of 165 traced subsystem inputs are Keys (≈4%), and those are substrate self-consumption — no gameplay subsystem reads a Key back | MEASURED (doc 6 §2) |
| **`tn` is accepted, stored, and never used** by the discrete dice owner; 19 inert TNs across the tree | MEASURED (docs 4–5) |
| **7 obstacle-bearing roll sites, all in one lane** (`systems/factions/sim/`); 36 production rolls total, AST-exact | MEASURED (doc 5) |
| **`Key.visibility` is written and never read** — the epistemological barrier, unimplemented | MEASURED (doc 1 GAP-A) |
| **`Key.causes` is essentially unpopulated** — but at least one empty is documented doctrine, not neglect | MEASURED + row 19 |
| **`references/` has zero runtime readers** — the "point at centralized definitions" mechanism does not exist for runtime modules | MEASURED (doc 5 §7.1) |
| **Articulation is a subscriber shell** — no emitter it listens for, no world reach, no result sink, no result types, no destination | MEASURED (doc 7 §2.2, doc 8 §3) |
| **The registry is loaderless, with four prerequisites, not one** | MEASURED (rows 16–17) |
| **`Contest.resistance` is derived and never consumed**; the resolver reads no resistance | MEASURED (row 15) |
| **The degree ladder was ruled, single-owned and guarded — and it HELD.** `massbattle.py:640-643` defers to `degree_from_net` *because* it has an owner and a guard | MEASURED — **and this is the control case** |
| Social contest runs live, and every contest is `logos_spammer` vs `logos_spammer` with a ±1 Mandate consequence spine | MEASURED (doc 7 §2.3) |
| Sixteen design gaps, each an unmade decision; two starting points need no ruling at all (`mass_seizure`'s call site; the omitted trigger rows) | JUDGMENT on scoping, MEASURED on each gap |

---

## §5 THE PATTERN, AS IT SURVIVED ATTACK

I proposed a synthesis: *every finding in this session is the same defect at a different altitude — a declared seam with nothing crossing it.* I asked for it to be killed rather than confirmed. **It was, and correctly.** The universal form is dead. What survives is smaller, and it predicts.

**Why the universal form failed — three reasons, each verified:**

1. **The degree ladder is the control case, not an instance.** It is a governed seam that **held**. The roller/obstacle story is not "nothing crossing" — traffic exists and crosses *off-seam*, forking into six private implementations. That is a **missing owner**, a different defect with a different fix (CLAUDE.md §0.1 point 5). Forcing it under the metaphor **erases the one success the session found.**
2. **Some instances are missing interfaces, not empty ones.** `ConvictionState` has no weight field; `NPC` has no name field. There is no declared seam to be empty.
3. **The settlement loader is a weak fit.** Its seam carries traffic — name, controller and stats cross for 37 of 37. Two cargo fields are dropped for want of destinations.

**The predictive test, on seams nobody in this session had examined — one of two held:**

- `engine/autoload/npc_ai.py` — **held.** Both entry points are `stubwire.stub_resolve`, no production caller, stubbed since 2026-05-17.
- **`engine/autoload/victory.py` — failed, decisively.** `mc_v18.py:269-274` calls `victory.check_all_factions(world)` **every season in the live loop**; a win sets `world.winner` and terminates the campaign; the implementation is real (15 territories, Accord ≥ 2, PS ≤ 6, sustained 2 seasons). **A declared seam with real traffic and real consequence.**

**The strongest rival explanation, argued honestly.** *"This is what honest deferral discipline looks like from the inside."* Nearly every large empty seam is **labeled, cited and guarded**: `stubwire.stub_resolve` is a designed single-owner primitive whose invocations are counted by ratchets; `generate_npc`'s deferral is pinned by two tests and an xfail manifest; `causes=[]` carries its reasoning inline; `resistance` names its reserved ED; articulation cites its docket. **This rival is largely correct about the big seams** — and it does **not** explain the small unlabeled rot: `temperaments.py:117` vs `:153-158`'s read/write asymmetry, and the `'Loyalty'`-scar test that asserts an intent flag rather than the effect. **The flattering explanation must not be allowed to absorb those.**

A second rival — *measurement artifact: we hunted unwired things and found unwired things* — is partly real (the briefs were delta-shaped; my own two-seam probe returned one empty of two) but insufficient, because the load-bearing numbers are **population statistics, not selections**: 165 traced inputs, 55 roll sites, 213 obstacle sites, 46 of 46 registry entries. A hunt biases which seams you describe; it cannot bias a full census.

### What survives — two families and a control

> **Family 1 — the Key/content layer is one-directional.** Keys flow *out* of the live loop and are never read *back in*; authored content has no runtime ingestion path. Every empty seam on the list is one half or the other: *visibility* = who may read Keys; *causes* = Key-to-Key input; *articulation* = the Key consumer; *Holdings* = the store Keys would write; *the loader* = content ingestion.
>
> **Family 2 — unowned operations fork.** Roller, obstacle, outcome vocabulary. **And the control shows the fix works: the guarded ladder did not fork.**
>
> **The empties are predominantly registered deferrals, not rot — but rot exists and is unlabeled.**

**What would falsify the surviving form:**

1. Find a **gameplay** subsystem that consumes a Key as input in the live loop → Family 1 is dead as stated. The parse is re-runnable.
2. Find a large empty seam with **no** stub label, docket citation, or pinning guard → mass moves from "deferral" to "rot." The temperaments pair is already one.
3. Build the loader: doc 7 §6 predicts four ticking systems go live at once. Row 16 says they will not without a weight field and a faction mapping. **Building it settles which.**
4. The "closed spine" claim must be stated as **the season accounting spine specifically**, not the strategic layer generally — doc 7 §2.1 already lists three built-but-uncalled strategic mechanisms.

---

## §6 CONTENT CENSUS — do we have the material?

The delta's animating question. Sizes and populations parsed or read this pass.

### Persons — the largest and most machine-ready corpus

**`references/npc_registry.yaml`** — 44.9 KB, **46 entries** (35 canonical, 11 proposed), machine-parseable modulo row 16's truncation defect. Population per field is in §2.2 row 17. Conviction vocabulary is **exactly the canonical 13**; 81 weighted primaries; 3 entries with none.

- **`goals` (39 sentences over 17 entries) are telegraphic role-descriptors, not situated intentions.** Median 2–4 words: *"Maintain substrate stability"*, *"Investigate heresy"*, *"Maximize Guilds Wealth"*. A minority carry a playable tension — *"Privately sympathize with Restoration Movement"*.
- **`arc_trajectory` (36 entries, median 111 chars) is the opposite — dense and specific**, cross-referencing arcs, EDs and stats: *"Flips if Elske Loyalty ≤ 2. Manuel II Palaiologos archetype"*; *"Royal Assassination Fuse target (Arc F Eliminated → Lenneth Widow Regent)"*.

**`systems/npcs/` — 19 prose docs, ≈460 KB.** `npc_behavior_v30.md` (106 KB, **CANONICAL**) is a full behavior *system*: per-NPC stance triangles as structured tables, convictions, resonant styles, TS, Truth, per-NPC Beliefs as quoted strings, Leadership Deviation Ob. `npc_roster_v30.md` (35 KB + 33 KB infill, CANONICAL) carries 13 deep profiles, each with a structural compromise and a **Behavioral AI profile with a named flaw and mechanical consequences** — Strand's flattery vulnerability is a −1 Ob rule. `npc_foils_v30.md` (38 KB) is a Ruler Diamond: 4 rulers × 4 axes × 6 pairings. `npc_character_analyses_v30.md` (67 KB) is literary analysis per NPC.

**`systems/characters/` — 226 KB**, including the numeric **13×4 axis matrix with composition rule** and a migration roster of **13 machine-parseable YAML profiles**.

**`goldenfurt_slice/npc_cast.md`** (14 KB) — 9 dossiers under a strict schema: ethic α/β, ambition with an escalation ladder and a `fires_card` binding, leverage {wants/fears/secret}, Knots, trajectory-if-blocked. **The most directly implementable person-content in the tree**, and collision-wired by design.

> **Person-content to person-runtime ratio: ≈700 KB authored, 0 bytes loaded.**

### Places — thin as prose, strong as structure

**37 settlement `description` strings, 3,788 bytes total** (25–268 chars, median 105). Kind: **functional gazetteer, structural not sensory** — *"Gransol province spoke. Salt-trade town."* Specific as world-model, empty as texture. `poi_catalog` is 17 territories × 4 **integer counts** — quantities awaiting content, not authored POIs.

**`goldenfurt_slice/` — 70.7 KB, one town worked end to end**: a 28-card local deck, 9 NPCs, a sim build spec, and a reproduction methodology. The existence proof for place-texture at depth 1-of-37.

### Factions, world, events, voice

**Factions:** 615 KB, headed by `faction_canon_v30.md` (52 KB) — per-faction Mission as YAML, **expected-conviction weight vectors** with cascade-fidelity as cosine similarity, and **institutional beliefs as first-person voice anchors** (*"Authority that is not earned this season is not authority next season"*). Runtime counterpart: 16 fields and a name comparison covering two of four factions.

**World/lore:** 259 KB of Solmund cultural corpus. Zero code citations (producer-grade, per doc 7 §7).

**Events:** 58 grounded cards (52 KB, PROPOSED) — each with historical grounding, a trigger predicate, a scale signature, 2–3 response branches with **concrete stat/tag deltas**, and a named follow-on arc actor. Zero implementing code.

**Voice: yes, and it is ratified.** `narrative_voice_canon_v30.md` (7.2 KB, **CANONICAL**, ED-1030) — an omniscient chronicle voice with a *falsifiable* lexical-register test (*"did the rare word save syllables"*), a 12-author grammar-latitude table, and a 20-item prohibition list including rendering rules for Coherence-0 beings and a no-performed-secrets discipline.

### The answer

> **The binding scarcity is not authored content, and it is not voice.** It is **ingestion** — loaders, a weight field, a name field, Key inputs — and, per doc 7 §5's one unbroken narrative finding, **subject matter for arguments**: no runtime object says what any contest is *about*.

---

## §7 COMPARATIVE CRITIQUE — measured against precedent

Precedent claims carry **DOCUMENTED** (dev paper/talk/patent/wiki-with-code-reference), **REPORTED** (credible secondary), or **INFERRED**. Sources are listed at §7.12.

### §7.1 The comparison inverts the anxiety

A **Caves of Qud** sultan is initialized with **six** properties — name, pronouns, birth year, birth region, location in birth region, and a **domain** — and its generated biographies appeared in **14 of the game's 150 most-popular Steam screenshots in six months** (DOCUMENTED, Grinblat & Bucklew, FDG 2017).

Our 46 registry entries all carry id, name, faction, role, status, source and a **13-conviction weighted profile**; a third carry substantially more. **Per-entity, we are not content-poor by the standard of a shipped, acclaimed history generator.**

The gap is that **every mechanism precedent uses to convert content into felt texture is one we have not built** — and two are ones we have designed *around* in ways the literature says will fail.

### §7.2 The expensive half is already done, and we do not know it

Kreminski, Wardrip-Fruin & Mateas set out what a simulation must provide before any story can be sifted from it (DOCUMENTED, *Authoring for Story Sifters*):

| Requirement | Their words | Ours |
|---|---|---|
| **A chronicler** | extracts potentially significant events | `KeyLog`, hashed into `CampaignResult` |
| **Causal bookkeeping** | *"information about the causality relationships between events … is not preserved or made retroactively available by most simulations"* | **`Key.causes[]`** |
| **Event polymorphism** | *"attach a variable-length list of string tags to each event … allows different sifting patterns to consider the same event"* — named as the cheapest high-value change | **`Key.symbolic_dimensions{}`** |

Ryan's diagnosis of the failure state is our position exactly: *"Mere simulation traces from an engine aren't enough to count as a narrative, and sometimes they look almost indistinguishable from a debugging console log."* (DOCUMENTED via Short.)

**This is a good position.** Most projects retrofit causal bookkeeping; the literature says it is far cheaper built in. We built it in. We lack the **sifter** and the **renderer** — and the field that makes a sifter possible is one we declare and do not fill.

> **PROPOSAL 1 — populate `causes[]` before building any renderer.** The chronicle is *downstream* of causal bookkeeping, not parallel to it. A render layer over an uncaused Key log can only produce Ryan's console log. **⚠ With row 19's nuance: at least one empty `causes[]` is doctrine — a fabricated cause is worse than none. The real work is upstream, making resolutions emissions.** That reframes GAP-B from "fill in the field" to "the events that would populate it are not Keys yet."

### §7.3 The warning that lands hardest on our actual design

**Diffuse causality.** Ryan uses **Prom Week** as the worked example: social state decomposed into six structures with **more than 3,500 weighted "sociocultural considerations"** summed to decide what a character wants and whether an approach succeeds (DOCUMENTED, McCoy et al., FDG 2011). His verdict: *"simulation causality can be too diffuse to make for good storytelling."* **When many weighted rules sum to a decision, no single legible reason exists** — so the system cannot say *why*.

Compare what we have specified: a **13×4 numeric matrix**; the composition rule `npc.armature_position[axis] = Σ_c npc.personal_convictions[c] × MATRIX[c][axis]`; **81 weighted conviction primaries**; and a CLASH/REINFORCE algebra resolving armature positions into δσ leverage. **That is a smaller Prom Week, heading for the same wall.**

Ryan names two remedies: **contingent unlocking** (some events possible only via a finite, nameable set of prior conditions) and **causal bookkeeping**.

> **PROPOSAL 2 — Jordan's scripted-hooks ruling *is* the remedy the literature prescribes. Name it as such and use it deliberately.** *Scripting hooks and sequences is allowed; scripting entire arcs is not* — the coup counter, the Crown Claim condition table, the Church-Influence theocratic threshold — **is contingent unlocking**. On Ryan's argument these are not a compromise with emergence; **they are what makes emergence legible.** A purely weighted system cannot produce a because-clause; a hooked one can.
>
> Design consequence: when a conviction-weighted sum decides something dramatically important, **gate it by a nameable hook rather than merely producing it from the sum.** The sum decides *whether*; the hook supplies *why*.

### §7.4 The layering problem we have, and who solved it

We have 46 authored named characters and an anonymous generator with no way to coexist. **RimWorld ships the solution** (DOCUMENTED, wiki mirroring the pawn-generation algorithm):

- Every pawn gets **either** a `shuffledBio` (random childhood + adulthood records) **or** a `solidBio` (hand-authored, fixed, named, locked surname).
- **25% chance a regular pawn attempts a solidBio; a faction leader always attempts one.**
- Candidates are filtered by gender, required surname, faction tags, leader status, **whether the bio has already been used this game** (authored characters are unique), and work-type compatibility.
- **If no authored bio survives, it falls back to shuffled.**
- **Both tiers produce the same object type**, so nothing downstream knows which it got.

That last property is the whole trick, and it answers our design gap 3 — *what does an authored person deserialize into?* **The precedent answer: the same thing a generated one does, or the layering does not work.**

The second half is better still. A RimWorld backstory holds, in one object: slot-tokened prose, skill deltas, **work-type enables and disables**, forced traits, spawn-category tags. **The prose and the constraint are the same record.**

> **The rule, stated plainly: a description you can ignore is decoration; a description that constrains the player is characterization.** RimWorld's backstories are felt because they **forbid** — a pawn who cannot do violence forces the colony to reorganize around them.
>
> Our `goals`, `resonant_style` and `arc_trajectory` are all **descriptive and forbid nothing.** That is the difference between our content and RimWorld's, and it is **not** a content-volume difference.

> **PROPOSAL 3 — adopt the two-tier funnel, and make one authored field constraining.** (a) The loader and `generate_npc` produce the same type, authored fields optional — which also dissolves row 17's population problem, since sparse authored data is the *expected* case, not a defect. (b) Authored people are a consume-once filtered pool that generation falls back from. (c) **`resonant_style` becomes a constraint, not a label.** It is already the shape of an armature Style key, and design gap 6 asks where a judge's position comes from. **The registry answers it.**

### §7.5 The mechanism that makes six fields feel like a life

**Qud's domain.** Each sultan gets one of ten — `glass`, `ice`, `might`, `scholarship` — and *"almost every gospel pattern contains a symbol that resolves through the domain"*, so it re-manifests event after event: icicles at her birth, an ice-encasement prohibition she fights, a frosty hammer, cities devastated by icy winds. *"Collectively they act as narrative force that pushes through the aggregated events of her life."* (DOCUMENTED.)

**We carry three domain-equivalents** — `resonant_style`, `cultural_label`, and the weighted conviction vector — and resolve none of them into rendered text, because we render no text.

**The harder half is the causality inversion**, and it bears directly on doc 7 §5's one unbroken finding:

> Qud's `sieges a city` gospel opens `Acting against #injustice#, #sultanName# led an army to the gates of #location#.` To fill `#injustice#`, the event inspects the sultan's state — allied frog factions become "the persecution of frogs." **And if no suitable cause exists, the event *creates* one** by writing frogs into her allied-factions property, then substituting. *"There's a full reversal of the expected causality; the effect causes the cause."*

Our contest kernel has `ground` — one of six abstract stasis tags — and no topic. **The Qud pattern says a debate's subject need not be decided beforehand; it can be resolved from participants' state at render time, and written back if absent.**

Two guardrails, both binding on us:

- **It is a lie, and it fails if the player can audit it.** Qud survives because its history is mythic and filtered through unreliable in-world accounts. **Our Key log is auditable** — so a rationalization must be *consistent with* the log, a constraint Qud did not face.
- **Coherence is bounded by archetype count.** Ten domains means the eleventh sultan reads as a reskin. Thirteen convictions in weighted combination give a far larger space — the same failure waits at a different scale.

> **PROPOSAL 4 — resolve contest subject from participant state at render time, with write-back, constrained against the Key log.** This closes the "no subject" gap **without inventing a topic ontology** — which is exactly why design gap 7 has stalled. **Don't author topics; author patterns that name a topic out of who is present and what they carry.**

### §7.6 The minimum state for a person — four rival answers

| Answer | Mechanism | Cost |
|---|---|---|
| **Memory of specific events** | Nemesis: name, rank, small trait set, **scars keyed to the method of prior death**, an append-only encounter log with dialogue keys (DOCUMENTED, US10926179B2) | Narrow by construction — one relationship type, one axis, one output, all about the player. Also **patent-fenced to ~2035** |
| **Accumulated opinion** | RimWorld/CK3: decaying, name-bound, stack-limited thoughts; trait-asymmetric opinion | Becomes spreadsheet grief when all thoughts are commensurable |
| **Stable idiosyncratic preferences** | Dwarf Fortress: 50 facets + 33 values, seven bands, **middle band renders nothing** | Description decouples from behavior; recurrence at scale |
| **A biased reading function over shared history** | WAWLT: per-character **sifting-pattern pools** — *"a melancholy character might be assigned a pool of sifting patterns that allow most social interactions to be interpreted as indicative of hostility"* (DOCUMENTED) | Requires a sifter to exist first |

**The fourth fits us and is the cheapest.** Not more attributes — **one pointer per entity into a pool of interpretation patterns.** Two characters observe identical events and produce different accounts. **That is character, and it costs a reference.**

It is also, structurally, what doc 2 already designed: a **Holding** — holder, prop_id, stance, confidence, support_refs, acquired_season — *is* a per-character reading of a shared world. **Precedent says that design is on the right line.**

**With one warning that is fatal and is about content, not architecture:**

> Ryan built the deepest character-knowledge simulation in the literature — belief facets with predecessors, parents, evidence lists, strength and accuracy; eleven evidence types including **confabulation** drawn from the town-wide attribute distribution, **transference**, **declaration** (*"an NPC who frequently tells the same lie might come to actually believe it"*), and **mutation** via a hand-authored belief-mutation graph — and then conceded: *"the knowledge subject to all this simulation is itself not very prone to generating narrative intrigue, since characters are mostly remembering and talking about such things as the hair and eye color of other characters."* (DOCUMENTED, Ryan & Mateas, *Game AI Pro 3* ch. 37; concession REPORTED via Short.)

**A perfect epistemic engine over trivial propositions produces trivia.**

> **PROPOSAL 5 — gate the Proposition schema on dramatic loading, in the schema itself.** Our epistemic layer must **not** be able to hold a proposition about a settlement's prosperity value. It must hold propositions about **allegiances, obligations, betrayals, secrets, culpability** — where being wrong costs something. Write this into the predicate vocabulary **before** B1, not as tuning to be discovered later. Ryan discovered it late and it cost him his thesis's best system.

**And one mechanism to take regardless:** Talk of the Town **skips knowledge simulation entirely** during its 140-year world-gen and **implants** beliefs at the end — accurate ones about family, friends, neighbours and coworkers, everyone else at probability `1 − 1/salience`. **Backstory need not be simulated to be consistent.** Our relational edges can be implanted at load rather than derived from a history we never ran.

### §7.7 The 37 discarded descriptions — the verdict is not "reinstate them"

The obvious remedy is a prose field on `Settlement`. **The evidence says that is the weakest available move.** Every successful place-texture mechanism in the survey is a place-*history* mechanism:

- **Qud villages:** name, faction, role-typed roster, and **exactly two generated historical events**, each with a **1-in-20 chance of rendering the village abandoned** — in which case it ships **remnants and clues**: a still-usable clay oven, standing structures, sometimes a monument (DOCUMENTED).
- **Qud sultan history:** visited places become **historic sites instantiated at world-gen**; items named in a life event become **real items placed there**; cities are **renamed by events**. *"Historical knowledge acts as a vector for players to find and engage with the material remnants."*
- **Dwarf Fortress Legends:** sites and civilizations are first-class historical entities — and with "Reveal All" off, **hidden until uncovered** through engravings on coins and statues, artifacts, books.
- **King of Dragon Pass:** inter-clan state is **Feud, Proximity, Raids won/lost including consecutive streaks, Slights remembered for years, Trade, Tribute** (REPORTED — exact variable names unconfirmed).

**Every one of those is a compressed memory of specific events, not an attribute.** *"Consecutive raids lost"* narrates itself; `prosperity 7` cannot. And the second property: **the prose predicts a findable thing.** The description is a treasure map, not atmosphere.

> **PROPOSAL 6 — make the descriptions the initial condition of a mutable history, and make the ledger that history.** We own the mechanism and it is orphaned: `ledger.py` holds **Precedent / Grudge / Debt / Reputation / Leverage** with dedupe, TTL and succession-survival — **zero production writers**. Those five kinds are *exactly* the KoDP variable class.
>
> So: (a) load `description` as the settlement's **founding entry**, not a static field; (b) wire the three unblocked events (parliamentary transfer, conquest, council verdict) to write tags, turning the ledger from schema into history; (c) require every description to name **one findable thing**.
>
> This converts "authored prose is discarded" from a plumbing complaint into the highest-value orphan wire on the map — and three of its four events are **blocked by nothing**.

### §7.8 The cheapest instantiation of 46 people — they do not have to act

Our loader problem assumes authored characters must become simulated actors. **Five design gaps block that. Precedent offers a route that bypasses all five.**

**King of Dragon Pass / Six Ages:** clan council members give advice in a mouse-over bubble on each event. **They never act.** Alexis Kennedy (DOCUMENTED, Failbetter design post): the low-commitment interaction means you always read it; it eases you into dense lore *"one frothing and sliding fact at a time"*; it makes you **choose council members for their personalities as well as their stats**; and *"you develop a surprisingly strong relationship with characters who only ever express themselves through transient speech bubbles."*

**Wildermyth** does the same — 11 personality values, the **top two** determining who speaks and how (REPORTED; first-party writeup not located).

**What it costs us: nothing that is currently blocked.** A conviction-weighted reaction line on an already-resolved event needs no territory key, no faction mapping, no weight field, no settlement membership. **It needs a name, a conviction vector, and a rendering slot — and 46 of 46 entries carry the first two.**

> **PROPOSAL 7 — instantiate the 46 as commentators before instantiating them as actors.** A genuinely different build from the loader, clearing all five of its design gaps by not needing them — and it **produces the first player-visible narrative text in the project's history**, which nothing else on the map does without passing through ED-IN-0073. It composes with §7.6: a commentator selected by conviction weights *is* a biased reading function at the cheapest fidelity.

### §7.9 The mechanism we most lack — a null band

**Dwarf Fortress holds 50 facets and 33 values, buckets each into seven bands, and the middle band generates no text at all** — roughly **78% of every dwarf's traits are silent**. The rendered personality is a concatenation of a handful of extreme deviations (DOCUMENTED).

**The lesson is not "have traits." It is "have a null band."** A system that renders every field for every entity produces mush. **DF's texture comes from what it refuses to say.**

The second-order mechanism is better: facets and values can **conflict**, and the conflict has its own authored text — low love-propensity *plus* high romance value renders as *"She never falls in love or develops positive feelings toward anything, and she is bothered by this since she sees romance as one of the highest ideals."* **The most characterful output in the system comes from two numbers disagreeing.**

We have the raw material and have never framed it this way: a character weighted toward both `Authority` and `Liberty`, or `Faith` and `Scholastic`, carries an internal contradiction **the 13×4 axis matrix can compute directly.**

> **PROPOSAL 8 — specify the null band before specifying the renderer.** Whatever ED-IN-0073's fork decides, the render layer must be told what **not** to say: a weight threshold below which a conviction is never mentioned, and a rule preferring **conflicts between high-weight convictions over the convictions themselves.** Decidable now, costs nothing, and constrains the fork productively instead of waiting on it.

**The failure to guard against:** DF is criticized because the personality text has *little observable behavioral consequence* — a dwarf described as patient and valuing tranquility repeatedly gets satisfaction from arguments (REPORTED — forum criticism, no developer acknowledgment; the class is real even if the strength is contested). **Description decoupled from behavior is the failure**, and our `resonant_style` is currently exactly that — which is why Proposal 3 makes it constraining.

### §7.10 What the evidence says we do **not** need

Each of these is something this project has built, planned, or worried about.

- **A causal simulation.** Qud chooses events **at random** and invents causes afterward. Causality can be a rendering-time property. *(Causal book*keeping* is still necessary — a log, not an engine.)*
- **A drama manager.** Ryan rejects it aesthetically (*"they do not actually happen, and they do not feel like they actually happen"*); Short adds the practical objection — you end up *"adding a lot of simulation content, and then adding a lot of drama management to ensure that content is rarely or never seen."*
- **A large trait vector.** DF's 50 facets are mostly silent; Wildermyth uses two of 11; Qud's sultans have six properties; Prom Week's 3,500 rules produce the documented diffuse-causality problem. **No evidence that more dimensions produce more texture, and some that they produce less legibility.** This bears directly on the descriptor roster being IN FLUX and on the ruled-but-unnamed tenth attribute.
- **Uniform coverage.** Salience-based selection is praised precisely because *"you're never committed to having uniform coverage for every possible situation."* **This is an argument against the instinct that all subsystems must reach equal robustness before any ships texture** — which was doc 6's original framing, and which the relay killed for different reasons.
- **Natural language generation.** Every rendering success in the survey is template-and-grammar substitution over authored fragments. Qud's entire voice comes from distilling a **40,000-word hand-written corpus** into replacement rules. **We have the corpus and the ratified voice spec; design gap 16 is that nothing consumes them.**
- **Simulating what can be implanted** (§7.6).
- **Full autonomy for authored characters** (§7.8).
- **Numeric distinctiveness.** Compton's 10,000 Bowls of Oatmeal: 10,000 mathematically unique bowls read as *"a lot of oatmeal."* **Perceptual uniqueness is the metric** — a few salient, nameable, consequential differences, not float precision across many fields.

### §7.11 The one genuine disagreement in the sources, and it is about us

Ryan argues emergent narrative needs **abstraction** — casting different characters in different situations rather than retelling stories about a fixed cast, because a fixed cast produces sameyness. **Emily Short is explicitly unsure**, and notes Fallen London and Mexica sidestep it by referring to characters **by title or function rather than granting them a name**.

For a project with 46 authored named characters plus an anonymous generator, this is live: **naming is what makes an entity memorable, and also what caps how many can exist before they blur.** Our `role` field — *Warden-Chief* — is exactly the title-or-function affordance Short describes, and it is one of the **seven fields populated on all 46**.

> **DESIGN GAP 17 (new): does rendered text lead with a person's name or their function?** The precedent says this determines how many people the world can hold before they stop being distinguishable. It is not on the wiring map's sixteen.

### §7.12 The proposals, ordered by what they unblock

| # | Proposal | Blocked by | Unblocks |
|---|---|---|---|
| **7** | Instantiate the 46 as **commentators, not actors** | **nothing** | first player-visible text; validates the content without the loader |
| **6** | **Ledger as settlement history**; descriptions as founding entries | **nothing** (3 of 4 events unblocked) | place texture; retires the "discarded prose" finding |
| **8** | **Specify the null band** before the render fork | **nothing** | constrains ED-IN-0073 productively |
| **2** | Name the scripted-hooks ruling as **contingent unlocking** | **nothing** (already ruled) | legibility of every weighted outcome |
| **5** | Gate **Proposition predicates on dramatic loading** | **nothing** (schema not built) | prevents Ryan's documented dead end |
| **1** | **`causes[]` before any renderer** — reframed upstream per row 19 | GAP-B's real cause | every sifting technique in the literature |
| **3** | Two-tier funnel; `resonant_style` becomes constraining | design gap 3 | authored/generated coexistence; judge positions |
| **4** | **Contest subject at render time** with write-back | design gap 7 | the "no subject" gap, without a topic ontology |

**Five of eight are blocked by nothing** — and none of the five requires the conviction-taxonomy ruling, the loader, or ED-IN-0073.

> **That is what this critique exists to produce.** The delta and the wiring map both concluded that narrative texture waits on a long dependency chain rooted in the person layer. **Measured against precedent, the five highest-value moves are not on that chain.**

**Sources:** Grinblat & Bucklew, *Subverting Historical Cause & Effect*, FDG 2017 · Ryan & Mateas, *Simulating Character Knowledge Phenomena in Talk of the Town*, Game AI Pro 3 ch. 37 · McCoy et al., *Prom Week: Social Physics as Gameplay*, FDG 2011 · Kreminski, Wardrip-Fruin & Mateas, *Authoring for Story Sifters* · Kreminski & Wardrip-Fruin, *Sketching a Map of the Storylets Design Space*, ICIDS 2018 · Kreminski et al., *Why Are We Like This?*, FDG 2020 · Evans & Short, *Versu*, IEEE TCIAIG 2014 · Short, *Beyond Branching* and the *Curating Simulated Storyworlds* series · Kennedy, *Anything Nice: King of Dragon Pass* · Compton, *So you want to build a generator…* · US Patent 10,926,179 B2 · Dwarf Fortress, RimWorld, CK3 and Caves of Qud wikis.

---

## §8 OPEN RULINGS QUEUE

Pointers, not argument. Deduplicated across doc 4 §9, doc 3 §1, doc 1 §13.2, doc 2 §10 and doc 8 §8.

**Canon rulings — nothing downstream moves without these:**

1. **Which conviction taxonomy governs** — `npe.py`'s 8 (canon-quoted at `investigation_systems_v30.md:84`), `conviction.py`'s 9 (self-superseded), or the canonical 13. *The registry uses the 13; the validator uses the 9; loading today evaporates 41 of 81 weighted primaries.*
2. **The Suppress-roll obstacle** — two ratified surfaces disagree (§2.1 row 14).
3. **What conviction weights live on** — no coded class holds one.
4. **The combat echo attribution model** — the named blocker on flipping `DISPATCH_COMBAT_BRIDGE`.
5. **ED-IN-0073's Q1–Q4 qualitative-rendering fork** — gates the entire render layer.

**Scoping decisions (13 more) are enumerated at doc 8 §8, plus design gap 17 at §7.11 here.**

**Needs no ruling — the two shortest complete paths:** `mass_seizure`'s call site (canon specifies its trigger), and the two omitted articulation trigger rows (the key-type registry already declares the consumers).

---

## §9 EXECUTION STATE

Doc 3's 14 steps, annotated with what the later censuses did to them.

| Change | Source |
|---|---|
| **B4 rescoped** — the divergence test cannot run against fieldwork actions; the sims are stubs | doc 4 §5.2 |
| **PC-first sequencing invalidated** — PC migration is blocked on "what is a character's score" | doc 4 §3 |
| **Step S3's `causes[]` ask reframed** — at least one empty is doctrine; the work is upstream | §2.2 row 19 |
| **The §2.3 "cheap win" re-costed** — 3 of 5 inputs, not 5 | §2.2 row 15 |
| **The loader re-costed** — four prerequisites, not one | §2.2 rows 16–17 |
| **"Point at centralized definitions" is not implementable as written** — `references/` has no runtime readers | doc 5 §7 |

---

## §10 COVERAGE

**Read in full this session (union across passes):** the nine session documents; `CLAUDE.md`; `engine/autoload/{game_state,victory,npc_ai}.py`; `engine/mc_v18.py`; `engine/cross_scale/{scene_dispatch,parliamentary_bridge,articulation,echo_transport,combat_bridge}.py`; `systems/settlements/sim/{registry,ledger,infrastructure,temperaments,settlement,adjacency}.py`; `systems/world/sim/npe.py`; `systems/characters/sim/{conviction,beliefs,companion}.py`; `systems/social_contest/sim/contest/{wrapper,policy,narrative}.py`; `systems/combat/combat_engine_v1/workbench/{narrate,trace}.py`; `systems/world/narrative_voice_canon_v30.md`; `systems/fieldwork/sim/knots.py`; `engine/tests/{test_world_population,test_pipeline_reach,test_knots_ed912}.py`.

**Parsed in full (not eyeballed):** `references/npc_registry.yaml` (all 46 entries, every field censused) · `systems/settlements/valoria_geography_v30.yaml` (all 37 settlements).

**Read in part:** `engine/substrate/keys.py` (:420-599) · `contest/resolver.py` (:140-219, :280-410) · `contest/agon_harness.py` (:190-249) · `systems/threadwork/sim/operations.py` (:1-120) · `systems/factions/sim/{mass_seizure,parliamentary_transfer,faction_action}.py` (partial) · `systems/overview/sim/{accounting,ci_track}.py` · the `systems/npcs/` corpus (sampled; sizes exact) · `proposals/grounded_event_card_deck_v1.md` (:1-110 + card enumeration) · `references/module_contracts.yaml` (:686-765).

**NOT opened, and therefore not ruled on:**
- `systems/overview/sim/season.py` — so **"every season" for the NPE call rests on a comment, not a read**.
- 14 of 17 `systems/factions/sim/` modules.
- `systems/social_contest/sim/parliamentary_vote.py` — the §10 Mandate penalty rests on a docstring.
- `contest/{primitives,dictionaries,rhetoric,armature}.py`.
- `systems/npcs/{npc_behavior,npc_roster,npc_foils,npc_character_analyses}_v30.md` beyond sampling; `npcs_flow_skeleton_v1.md`; `character_histories_v30_infill.md`; `conviction_track_v30*`.
- `engine/cross_scale/{domain_echo,zoom_in_out,handoff_rules}.py`; `engine/autoload/scene_slate.py`.
- The combat engine core (`wrapper`/`core`/`combatant`).
- **Whether anything emits `state.succession`** — relevant to the governor gap.

**⚠ SUPERSEDED 2026-08-22 by §11.** This section read: *"The largest qualifier on this entire document: nothing was executed."* **That is no longer true.** The §11 coverage-closing pass ran three non-mutating in-memory checks — the `record=True` chain, the contest kernel's `mechanics_selftest()`, and a seeded `base_ob` sweep — writing nothing to disk. §11 records what they settled. The rest of the qualifier stands: no campaign was run, and every other claim in this document is from reading and parsing.

**§10's not-opened list is now closed.** See §11 for what each file contained and which claims moved.

---

## §11 COVERAGE CLOSED — what the unread files contained

Three Fable 5 read-only passes read §10's entire not-opened list in full: the 14 unread `systems/factions/sim/` modules plus `season.py`; the whole social-contest kernel, `parliamentary_vote`/`stay`, the combat engine core and four never-opened cross-scale modules; and the complete 530 KB `systems/npcs/` corpus plus `character_histories_v30_infill` and `conviction_track_v30*`.

**Every claim below that changes a published statement was re-verified by me, by reading or parsing, before being written here.**

### §11.1 The three open questions, settled

| Question | Answer |
|---|---|
| Does `run_accounting` really fire every season? | **Yes — settled by read, not comment.** `mc_v18.py:260-267` → `season.py:69-72` (`run_accounting(world)`, unconditional, no flag) → `accounting.py:139` (`simulate_npc_actions`, unconditional). §10's open item is closed. |
| Is the §10 Mandate penalty real code? | **Yes, and it is live every season** — `parliamentary_vote.py:207-219` performs a real `adjust("L", …)` world write, reached via `mc_v18.py:148-152` with ECHO_TRANSPORT default ON. It was never just a docstring. |
| Does anything emit `state.succession`? | **No.** The only occurrences are articulation's consumer roster and a test. `key_graph.json` names its producer as `faction_politics` — **which exists only as a design doc**. And the Key's required payload (`prior_leader_id`, `new_leader_id`) has no coded source: `Faction` carries **no leader field of any kind**. Design gap 14 is three layers deep, not one. |

### §11.2 The claim I most doubted was right — and it was executed

Doc 8 §9 flagged its own E2 claim ("the contest Chronicle is one kwarg away") as most-likely-wrong, and named the check that would settle it. **The check was run.** At the exact live call shape, `resolve_contest(..., record=True)` → `_bout.log` (6 rows) → `narrative.summarize` → `Chronicle.render()` returned:

> *"[CLEAR WIN] B took it by 26%, the case resting on logos on quality-ground."*

**The chain is real.** The only missing piece is the destination (C2/C4), exactly as mapped.

**One scope condition, found by executing the other branch:** the Chronicle is correct only for winners in `{a, b, draw, clinch}`. Fed a banded PersuasionTrack verdict — the 4 tracker-`required` proceedings — it misclassifies, because `narrative.py:114` catches only `"draw"` and `:126` treats every band string as side B. Demonstrated output: **"[CLEAR WIN] committee took it by 7%…"**. The live path (`guild_arbitration`, an a/b/draw ballot) is safe.

### §11.3 A second unlabeled-rot hit — the Treaty mechanic is wholly inert

§5's falsifier (ii) asked for large empty seams with no stub label, no docket, no guard. The session had two. **This is the third, and the largest.**

`treaty_expiration_v30.md` is **CANONICAL** and calls the mechanic *"the primary Crown-nerf lever… without this mechanic Crown achieves 55-90% win-rate dominance."* In the live campaign it does nothing at all:

- `propose_treaty` is honestly stubbed — but its stated canonical path is false. It says formation *"is resolved in crown_initiative"*; `crown_initiative.py` (317 lines, read in full) contains **no treaty-formation code**. Its single treaty mention (`:195`) is a precondition check. **Senator Outward is implemented nowhere.**
- `process_treaty_expirations`, `register_treaty` and `get_active_treaties` have **zero callers of any kind, including tests** — and unlike the six stubs in the same package, they carry no stub label, no docket, and no pinning guard.
- The arc-boundary detector its docstring names, `season_manager.check_arc_boundary`, **also has zero callers**.
- `World.treaties` is declared, serialized and restored with **no production writer**.
- **A defect I verified directly:** `treaty.py:137` reads `roll = 0.95  # default to high-lapse if no rng`. With `TREATY_LAPSE_RATE_DEFAULT = 0.90` and a documented range of 0.90–0.95, `0.95 < 0.90` is **False** — the fallback **can never lapse a treaty at any canonical rate**. The comment states the opposite of what the code does.
- `register_treaty` keys by `tuple(sorted(parties))` while `game_state.py:190/:385` documents and rebuilds **frozenset** keys — a save/restore key-type asymmetry.

**Mass moves from "honest deferral" to "unlabeled rot" here**, and §5's rival explanation is correspondingly weakened — though only for this seam. Everything else opened in these passes was uniformly labeled: the six faction stubs carry stubwire + reason + docket + design gate **and** are pinned by `test_pipeline_reach.py:750-755`.

### §11.4 A live defect in the one path that runs every season

**The §10 "one-season" Mandate penalty is permanent as coded.** `parliamentary_vote.py:218` defers restoration to `season_manager` — and `season_manager.py` has no temporary-modifier machinery whatsoever. `Faction.reset_seasonal` (`game_state.py:134-136`) clears exactly two booleans. I read both. A canonically temporary −1 Mandate is applied forever, on the path this document calls the one that actually runs every season.

### §11.5 D5 is no longer a free win — my "shortest complete path" was wrong

The wiring map called `mass_seizure` *"the only D-item with no design gap"* and *"purely the call."* **False.** `mass_seizure.py:293` writes `t.accord = float(starting_accord)` — a canonical index (0–4) into a **continuous** field on the `ACCORD_MAP` scale `{0:1.0, 1:2.5, 2:4.0, 3:5.5, 4:7.0}`. The sibling site does it correctly (`parliamentary_transfer.py:278`: `ACCORD_MAP[accord_level]`), and `game_state.py:65-70` warns in its own words that modules **"MUST bucket through these helpers."** Wiring D5 as-is ships a wrong-scale write. Corrected in doc 8 §4.

### §11.6 §7.4 IS BROKEN — the corpus is dense with prose-and-constraint-in-one-record

**This is the most consequential correction in the fold-in, and it is against my own critique.**

§7.4 claimed our authored fields are *"descriptive and forbid nothing"*, unlike RimWorld where *"the prose and the constraint are the same record."* **True of the three registry fields it names. False of the authored corpus, decisively.** I verified both citations:

- `npc_behavior_v30.md:52` — one table row: *"Ethical Framework | Virtue (Crown) | **Aligned: −1 Ob on public, visible, virtuous action. Contradictory: +1 Ob on covert/expedient action.**"* Characterization and mechanical modifier, same record. That **is** the RimWorld property.
- `npc_behavior_v30.md:991` — *"An NPC with Disposition +4 or +5 toward their current faction **cannot** be targeted for recruitment"*, with **"Not recruitable"** as a table cell in the Ob ladder at `:1003`. That is a forbid, which is the specific thing I said we lacked.

And the corpus forbids repeatedly: a heretic *"cannot hold Standing ≥ 1"*; Thread-level evidence *"does not function"* against TS-0 NPCs; the orator *"cannot pivot"* after RS declaration; Edeyja *"never leaves the Southernmost"*; Maret *"cannot target RM"*. The PC lifepath is a closer RimWorld analogue still — origin prose + granted skill + Truth value + Knot in one record, including *"Scarred by the Unreal — **Immune** to Composure loss"*.

> **Corrected diagnosis.** Valoria does not lack authored constraint. It lacks an **executor** — every one of these forbids sits inside a resolution system with no runtime. The precedent comparison was aimed at the wrong layer. **Proposal 3's remedy survives** — the registry, the only parseable surface, really is constraint-free — but its rationale was wrong, and it should now read *"lift existing constraints into the parseable surface"* rather than *"invent one."*

### §11.7 §7.9 is partly false — a null band already exists, at two levels

I claimed we have no null band. The corpus specifies **when not to express** twice:

- **Interaction level:** outreach requires Disposition ≥ +2, demands require ≤ −2 (`npc_behavior_v30.md:901-912`). **The mid-band −1..+1 generates no personal-scene entry at all** — a structural silence band — with volume caps of 3 outreach / 2 demands per season.
- **Entity level:** Background NPCs render as *"Identity only… Reference only"*; demotion trigger 2 explicitly targets the mid-band (*"Disposition has been −1 to +1, unchanged for ≥ 4 seasons"*); non-named NPCs carry *"no Conviction, no Resonant Style, no Beliefs."*

**Proposal 8 survives but must be restated** as *extending an existing null-band pattern* rather than introducing the concept. What genuinely does not exist is its specific ask: a conviction-weight threshold below which a conviction is never mentioned, and the prefer-conflicts rule.

### §11.8 §7.6's "biased reading function" is already specified — twice, in canon

I proposed per-character biased interpretation as the minimum state for personhood, citing WAWLT. The corpus already specifies it:

- **The Ministry PAR census** is literally a per-perceiver reading function over one shared record: TS ≥ 30 reads the data as a Thread map *"automatic — no roll required"*; TS 10–29 gets *"an uneasy sense… cannot decode it"*; TS 0–9 *"sees only public health data. **No Thread-relevant information is perceived**"* (`npc_behavior_v30.md:339-347`).
- **Resonant Style** is a typed per-NPC reading function over arguments.

So §7.6 is not new design. It is the **unimplemented half of two existing CANONICAL specs** — and `npc_memory`, the contract that would hold it, greps to nothing tree-wide.

### §11.9 The bottom line survives — and the gap is one missing field

§6 concluded the scarcity is *"ingestion, and subject matter for arguments."* **The word doing the work is *runtime*, and it holds.** But the corpus is emphatically **not** all disposition and no proposition:

Per-NPC Beliefs are **authored propositions** — first-person, contestable, specific: *"Constitutional procedure IS justice"*; *"Almud is faltering — I must be ready to act when he cannot"*; *"Something is wrong in the deep records… I am afraid to find out."* The contest system already requires an argument to *"specifically address a known Belief"*, and belief revision to *"textually address the commitment."* Subject matter, revision mechanics and stakes are all specified.

**I parsed the registry to check where they live. They do not.** Its 22 top-level fields are `age, arc_trajectory, birthplace, certainty, coherence, convictions, cultural_label, faction, first_name, goals, id, last_name, notes, resonant_style, role, self_other_initial, source, stats, status, territory, title, ts`. **There is no `beliefs` field, and zero of 46 entries carry one.**

> **So the ingestion gap and the subject-matter gap are the same gap, at one specific field.** The cheapest closure of *"no runtime object says what any contest is about"* is not render-time topic synthesis — it is lifting ~35 already-authored Belief strings into the parseable surface. **Proposal 4 stays right for generated NPCs and, for the authored 46, re-solves a solved problem.**

### §11.10 What else changed

- **§4's obstacle row undercounts.** "7 obstacle-bearing roll sites" is right for *sites passing `ob=` to the owner*; **three more in the same package bear an obstacle applied outside the roll call** — `faction_action.py:540-541` (Muster, Ob 1) and `:562-563` (Govern, Ob 2), both **live**, plus `mass_seizure.py:261-268`. "All in one lane" holds either way.
- **Falsifier (i) survives a hard probe.** All four never-opened cross-scale modules were read in full — `domain_echo`, `zoom_in_out`, `handoff_rules`, `scene_slate`. **None imports the Key substrate or subscribes to anything.** Family 1 stands.
- **The degree-ladder control case is confirmed and extended.** Every degree decision in the factions package routes to the owner, including an explicit adapter that calls itself *"NOT a second ladder."* The combat core's `degree()` is a **deliberate, labeled hold** with its measured reason, its ED, and a declared-hold guard named in its own docstring — the opposite of a fork.
- **Doc 7 §2.1's orphan list grows.** Treaty Expiration joins it, and it is the only one carrying a live balance implication.
- **New defects, latent unless noted:** `scene_dispatch.py:313` cites `dictionaries._APPEAL_TO_GENRE`, **a symbol that exists nowhere in the package**; `faction.py:23-25` stores `reb_ob` (the §5.5 Rebuttal Ob) and nothing reads it — a new member of the inert-obstacle census; `zoom_in_out.py` computes `contested_figure_wound_ob` and `pc_incap_applied` for no consumer; `compute_thread_echo` has zero callers; `rhetoric.py:380-386` claims the Doubt Marker's *"both pieces are wired this stage"* while **no Doubt Marker exists in any kernel code**.
- **Content-in-code census.** `dictionaries.py` carries **12 authored player-facing `flavor` sentences**, declared *"real, final, player-facing UI-card copy"* and behaviourally pinned by tests that enforce honesty properties on the copy itself. **Zero campaign reach.** The §6 pattern — authored, finished, unreachable — reproduced in miniature inside the code.
- **Three surfaces assign different convictions to the same NPC.** Beyond the four rival rosters, the registry, `npc_behavior_v30` and the migration roster disagree per-character (Vossen, Almud, Maret, Baralta each differ), and the consolidation's own tie-break rule is contradicted by the registry. **§8's open ruling 1 understates the problem: settling *which taxonomy* does not settle *which assignment*.**
- **A fully-specified NPC is missing from the registry entirely** — Registrar Lennart Haelgrund, who carries three arcs, a home settlement, a TS value and the PAR mechanic, has no entry. NPC-004 is a *different* person sharing the surname.
- **Corpus size corrected:** `systems/npcs/` is ≈530 KB, of which ~75 KB is a SUPERSEDED duplicate and ~32 KB is stale auto-generated indexes. §6's ≈460 KB is right for the live material.
