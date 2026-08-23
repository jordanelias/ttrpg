# Suite 05 — Precedent, and Eight Proposals

**Status:** COMPARATIVE ANALYSIS + PROPOSALS (unratified). The precedent half describes published
systems and is tagged by evidence grade. The proposals half is design work and needs Jordan.

**Evidence tags on external claims**, used throughout — these are *not* verified against the Valoria
tree because they are not about it:

- **DOCUMENTED** — stated in a paper, postmortem or talk by the system's own authors.
- **REPORTED** — stated by a third party.
- **INFERRED** — my reading of a described mechanism.

Every **Valoria analogue** judgement, by contrast, was verified by reading Valoria code or design
documents. Analogue grades: **ANALOGUE** (the concept matches) · **PARTIAL** (structurally similar,
materially different) · **NOTHING**.

---

## §0 Why look outward at all

Valoria's problem is not that it lacks systems. It has a Key substrate with causal bookkeeping, a
conviction-axis matrix, a settlement memory ledger, a contest resolver with an argument armature, and
a campaign driver that runs. The problem measured in Suite 02 is that **almost none of it produces
anything a player would experience as a story** — the ledger has no callers, the voice canon has no
consumer, the chronicle has no home, and the population is zero.

That is a *narrative-generation* problem, and it is a solved-enough problem elsewhere to be worth
reading about before designing more mechanism.

---

## §1 The mechanisms, and what Valoria has

### §1.1 Caves of Qud — history generation

| Mechanism | Grade | Valoria |
|---|---|---|
| **Ex-post-facto rationalization** — pick the event first, then resolve its cause from world state; if no cause exists, **write one in** and substitute it | DOCUMENTED | **NOTHING.** The contest kernel has `ground` (six stasis tags) and no render-time subject synthesis. This is Proposal 4. |
| **A single `domain` re-manifesting across events** via grammar — 10 domains × 19 event types as narrative-thread glue | DOCUMENTED | **PARTIAL, and the earlier claim of equivalence was wrong.** `resonant_style` exists per NPC, but it is a *social-contest argument-style key*, not a life theme that recurs across a biography — and nothing renders it. See §3. |
| **Village = name + faction + two history events**, 1-in-20 abandoned, ships remnants and clues; the prose *predicts a findable thing* | DOCUMENTED | **PARTIAL.** `settlements/sim/ledger.py` is the compressed place-memory class and has zero callers (Suite 04 §3.3). No place-history renderer. |
| **Nested-grammar corpus + query language** for voice (~40k words) | DOCUMENTED | **PARTIAL.** `narrative_voice_canon_v30.md` exists; nothing consumes it. |

### §1.2 Prom Week / Comme il Faut — the negative lesson

| Mechanism | Grade | Valoria |
|---|---|---|
| **~3,500 signed-weight "sociocultural considerations"** summed to form desires and responses | DOCUMENTED | **ANALOGUE — and the warning applies to us.** |
| **Diffuse causality**: with thousands of small weights summed, no single legible reason survives for any outcome | DOCUMENTED (authors' own critique) | Valoria's 13×4 conviction-axis matrix, Σ composition, 81 weighted primaries and CLASH/REINFORCE are a smaller Prom Week. **The mechanism to steal here is the caution, not the machinery.** |
| **Social state decomposed into six typed structures** (Relationships, Networks, Statuses, Traits, Social Fact DB, Cultural KB) | DOCUMENTED | **PARTIAL** — the settlement ledger is the settlement-scale analogue; there is no social-fact database at personal scale. |

This is the single most important entry in the document. Valoria is **already building** the thing
Prom Week's authors identified as their own failure mode: outcomes produced by summing many small
weights, from which no player can reconstruct *why*. Adding more axes makes it worse, not better.

### §1.3 Talk of the Town — belief and fallibility

| Mechanism | Grade | Valoria |
|---|---|---|
| **Belief facets** — per-attribute mental models with owner, subject, value, **predecessor**, **parents**, **evidence[]**, strength, accuracy | DOCUMENTED | **PARTIAL / DESIGNED.** `Holding` in the 2026-08-18 epistemic proposal (holder, prop_id, stance, confidence, support_refs, acquired_season) is the structural analogue. Unbuilt, unratified. **0 of 46 registry entries carry a `beliefs` field.** |
| **Confidence = independent support chains** | DOCUMENTED | **DESIGNED.** The proposal defines independent support as support_refs whose `Key.causes` ancestries are disjoint — a real structural match to the Key substrate. |
| **Eleven evidence types** across five categories, incl. confabulation, transference, and **declaration** (tell the same lie often enough and you believe it); mutation via an authored belief-mutation graph | DOCUMENTED | **NOTHING.** Valoria has no fallibility model at all. NPCs cannot be wrong. |
| **Knowledge implantation** — belief simulation *skipped* during 140 years of world-gen; beliefs implanted at the end, accurate for family/friends/neighbours/coworkers and probabilistic otherwise. *"Backstory need not be simulated to be consistent."* | DOCUMENTED | **NOTHING built** — and it is the cheapest idea in this document. It says the expensive thing (simulating history) is optional. |

### §1.4 Narrative sifting — the render layer

| Mechanism | Grade | Valoria |
|---|---|---|
| **Chronicler** — extract significant events from simulation output | DOCUMENTED | **ANALOGUE.** `KeyLog`, hashed into `CampaignResult`. |
| **Causal bookkeeping** — record which events led to which, retroactively queryable | DOCUMENTED | **ANALOGUE, present and unpopulated.** `keys.py:147` `causes: list`, with invariant 3 (`:384`) enforcing that causes reference logged Keys. The field is real and the concept matches. The busiest emitter sets `causes=[]` by doctrine (Suite 04 §5). |
| **Event polymorphism** — a variable-length list of string tags per event, so multiple sifting patterns match one event | DOCUMENTED | **PARTIAL — softened from an earlier overclaim.** `keys.py:150` `symbolic_dimensions` is a **dict** (axis → value), not a tag list. Structurally cousinly, not identical. An earlier draft asserted equivalence. |
| **Per-character pools of sifting patterns** → biased interpretation (a melancholy character reads interactions as hostility) | DOCUMENTED | **PARTIAL.** Two canon analogues exist as *specs* with no runtime executor: the Ministry PAR census (`npc_behavior_v30.md:339-347`) and Resonant Style. |
| **The sifter itself** — overgenerate, then test; without it the output is a console log | DOCUMENTED | **NOTHING.** No sifter, no renderer. |
| **Drama managers rejected** as high-cost (build content, then suppress it) | DOCUMENTED | Correctly **not pursued**. |

### §1.5 Storylets — the under-mined thread

| Mechanism | Grade | Valoria |
|---|---|---|
| **Parametrized storylets / dynamic queries** — treat game state as a database, bind entities to named parameters, fire only if every parameter binds; the bindings then drive both surface text and effects | DOCUMENTED | **PARTIAL.** Valoria's scripted hooks (coup counter, Crown Claim condition table) are precondition-gated content with **no parametric binding layer**. This is the least-explored precedent relative to its fit — a binding layer is what would let one authored situation instantiate against whichever faction, settlement and NPC currently satisfy it. |
| **Salience-based selection** — specific-tagged storylets are rare but relevant; generic ones are fallbacks; *never commit to uniform coverage* | DOCUMENTED | **NOTHING coded.** The "no uniform coverage" argument is used in §4 below. |
| **Waypoint narrative** — steer a conversation through a topic graph | DOCUMENTED | **NOTHING.** Relates to the absent dialogue lattice. |

### §1.6 The null band

| Mechanism | Grade | Valoria |
|---|---|---|
| **Dwarf Fortress**: the large majority of generated personality traits produce **no** behavioural text — the silence is what makes the exceptions legible | REPORTED | **PARTIAL — and an earlier draft got this wrong.** Valoria already has a null band at two levels: `npc_behavior_v30.md:901-912` (a mid-band of −1..+1 generates no scene) and the Background-NPC "Reference only" tier. The claim that a null band is "the mechanism we most lack" was **false**. |
| **King of Dragon Pass**: council commentators — the same advisors react to each decision in character, so personality is expressed through *commentary on events*, not through events | REPORTED | **NOTHING.** This is Proposal 7, and it is the cheapest route to audible character in the whole document: it needs no new simulation, only a reaction surface over decisions that already happen. |

---

## §2 Eight proposals

All **unratified**. Ordered by (blocked-by-nothing first, then cost).

| # | Proposal | Blocked by | Cost | The precedent |
|---|---|---|---|---|
| **7** | **Council commentary** — named NPCs react in character to decisions already being made | nothing | low | KoDP |
| **8** | **Widen and use the null band** — make the existing silence deliberate and tune it, rather than adding expression | nothing | low | DF |
| **6** | **Place history** — wire the settlement ledger and render a place's remembered past | nothing (the ledger is written) | low–med | Qud villages |
| **1** | **Chronicler + causal bookkeeping + polymorphism** — populate `Key.causes`, then sift | Suite 04 Q3 (chronicle home) | med | narrative sifting |
| **5** | **Biased reading function** — resolve what an NPC *thinks happened* per perceiver | nothing | med | ToTT / WAWLT |
| **3** | **Consume-once funnels** — a source that fires for leaders and is consumed, so it cannot repeat | nothing | med | RimWorld bios |
| **4** | **Ex-post-facto subject synthesis** — pick the event, then write in its cause if none exists | Q3 | med–high | Qud |
| **2** | **Contingent unlocking, not diffuse weights** — scripted hooks that *gate* content rather than more summed axes | design call | high | Prom Week, negatively |

**Two corrections to how these were originally argued**, both caught by adversarial review:

- Proposal 5 was pitched as *"the one that fits us, the cheapest, and new."* It is **not new** — it is
  specified twice in canon already (the Ministry PAR census at `npc_behavior_v30.md:339-347`, and
  Resonant Style). The proposal is to *execute* an existing spec, which makes it cheaper than claimed
  and less novel.
- Proposal 3 was pitched on the premise that *"our authored fields forbid nothing."* **False.** The
  corpus is dense with forbids — `npc_behavior_v30.md:52` (aligned/contradictory Ob modifiers), `:991`
  ("cannot be targeted for recruitment"), the heretic "cannot hold Standing ≥ 1", the PC lifepath
  "Immune to Composure loss". The registry is the only constraint-free surface, and that is a property
  of the registry, not of the corpus.

**Recommendation, if only one lands: Proposal 7.** It requires no new simulation, no chronicle home,
and no design ruling. It attaches character to decisions the engine already makes, which is the
shortest path from "systems run" to "somebody in this world has an opinion about it."

---

## §3 The disagreement worth preserving

Two credible positions on abstraction, and this session did not resolve them:

- **The sifting position:** simulate richly, then *select* — overgenerate and test. Narrative quality
  comes from having enough raw material that a good sifter finds the interesting 1%.
- **The storylet position:** authored content bound to state beats generated content selected from
  noise. Simulate *thinly*, author *specifically*, bind at runtime.

Valoria is currently building toward the first while having none of the second's binding layer and
none of the first's sifter. The strategic question — **which of these Valoria is** — is upstream of
most of §2, and nobody has asked it.

ToTT's knowledge-implantation result (§1.3) is the strongest evidence for the storylet side: its
author concluded that 140 years of belief simulation could be skipped entirely and *implanted* at the
end without the world becoming inconsistent. That is a direct argument that expensive backstory
simulation buys less than it costs.

---

## §4 What Valoria does not need

Recorded because the temptation is real and precedent argues against each:

- **A drama manager.** Building content in order to suppress it is the expensive path, and the sifting
  literature says so explicitly.
- **More conviction axes.** Prom Week's authors' own diagnosis (§1.2) is that more summed weights
  destroy legibility. Valoria has 13 conviction names of which seven are inert (Suite 02 §2.3) — the
  problem is not axis count.
- **Uniform coverage.** The storylet literature is explicit that never committing to uniform coverage
  is what makes salience work. Valoria does not need a scene for every state; it needs good scenes for
  a few.
- **More simulation depth before a renderer exists.** Nothing currently renders anything. Depth added
  below an absent render layer is unobservable by construction.

---

## §5 Provenance

The precedent research is drawn from published papers, postmortems and author talks on Caves of Qud
history generation, Comme il Faut / Prom Week, Talk of the Town, narrative sifting and story sifters,
and the storylet design space, plus reported accounts of Dwarf Fortress personality expression and
King of Dragon Pass council commentary.

**All external claims are tagged in §1 and none are verified against the Valoria tree, because they
are not claims about it.** Everything in the "Valoria" column *is* verified, by reading Valoria code
or design documents — including the three places where verification overturned the argument (§1.4
polymorphism, §1.6 null band, §2's two corrections).

---

_Written 2026-08-23. The proposals are unratified and none has been implemented. The Valoria-side
analogue judgements were verified against `engine/substrate/keys.py`,
`systems/settlements/sim/ledger.py`, `references/npc_registry.yaml`, `systems/npcs/npc_behavior_v30.md`
and `proposals/2026-08-18-epistemic-propositions-and-provenance.md`._
